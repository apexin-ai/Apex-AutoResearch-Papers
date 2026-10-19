# analysis plan 005 stratified — Part 1 of 39

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Worker execution logs

[Transcript overview](../analysis-plan-005-stratified.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/ca/cacae794176b02f848f1.json)

## Before a recorded user message

## Before a recorded user message

202 recorded events


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
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
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
  "uuid": "f6a1d481-aca4-4092-9750-a2a014a87a1c",
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
    "resetsAt": 1778807400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "da4b3a36-4fb1-4130-ac89-ff5e5625081b",
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388"
}
```

---


### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by understanding the task. I need to:

1. Find and read the `analyze_stratified.py` script on the remote server
2. Check what dimensions it supports
3. Run it with existing checkpoints if possible (CPU only)
4. Report on what's implemented vs what's missing

Let me first detect the image and then find the script.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "e77e397d-de2c-4202-b5d0-cba7164b7a54",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011uHsk1ChNs7rHwyYADdNzM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12152,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12152
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

先连接服务器，探测环境并找到分析脚本。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "69f040b6-c237-4d63-ad08-e5ba8f76d852",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011uHsk1ChNs7rHwyYADdNzM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12152,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12152
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01GMSB6pSD2DUGdQ7MZfhCGZ`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__detect_image,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
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
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "cf76e32e-8a82-4a3e-b923-de5e7fc91106",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011uHsk1ChNs7rHwyYADdNzM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12152,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12152
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

_source line 7 · 2026-05-14T20:14:57.903Z_

<details><summary>↩ Tool result · `toolu_01GMSB6pSD2DUGdQ7MZfhCGZ`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__detect_image"
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
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "0222e1b2-6889-43d3-8589-387a8f9d8c1f",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__ssh_execute"
    ],
    "query": "select:mcp__agent-ml-research__detect_image,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
    "total_deferred_tools": 23
  }
}
```

</details>

---


### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__detect_image · `toolu_01LV3LrbUVizhbEK4Q6Jc6x3`</summary>

```json
{
  "server": "bjb1-42106",
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
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "4915913d-14d6-42e7-ac94-ec0805f167bc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ARxy5vgDeyVc6rhZ1wfxm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 987,
      "cache_read_input_tokens": 23599,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 987
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

_source line 9 · 2026-05-14T20:15:01.977Z_

<details><summary>↩ Tool result · `toolu_01LV3LrbUVizhbEK4Q6Jc6x3`</summary>

```text
{"result":"{\n  \"detected\": false,\n  \"status\": \"unknown\",\n  \"skip_base_setup\": false,\n  \"message\": \"No image marker file found. Use traditional env-setup flow.\"\n}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "fefd901b-5edf-4b16-a4cf-9904a1fe6eef",
  "tool_use_result": {
    "content": "{\"result\":\"{\\n  \\\"detected\\\": false,\\n  \\\"status\\\": \\\"unknown\\\",\\n  \\\"skip_base_setup\\\": false,\\n  \\\"message\\\": \\\"No image marker file found. Use traditional env-setup flow.\\\"\\n}\"}",
    "structuredContent": {
      "result": "{\n  \"detected\": false,\n  \"status\": \"unknown\",\n  \"skip_base_setup\": false,\n  \"message\": \"No image marker file found. Use traditional env-setup flow.\"\n}"
    }
  }
}
```

</details>

---


### Tool call

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01E1dFYBKyy77B89t94wbRzn`</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "find /root/structfuse -name \"analyze_stratified*\" -type f 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "6aa4e444-323c-4be1-8bc2-ea3b2b41c066",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NMtZPcUmLacpts1m6YFDvV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 159,
      "cache_read_input_tokens": 24586,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 159
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

_source line 11 · 2026-05-14T20:15:05.327Z_

<details><summary>↩ Tool result · `toolu_01E1dFYBKyy77B89t94wbRzn`</summary>

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
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "43cbadb7-a5ec-4ae4-bfe3-cc4b1d7f5f14",
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

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01DyYqQ8y6SGd7MV2aPXJe5k`</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "ls /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "ac3d2b83-be1a-4ed2-9336-d495752533c6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NMtZPcUmLacpts1m6YFDvV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 159,
      "cache_read_input_tokens": 24586,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 159
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

_source line 13 · 2026-05-14T20:15:06.229Z_

<details><summary>↩ Tool result · `toolu_01DyYqQ8y6SGd7MV2aPXJe5k`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"random_s42\\nrandom_s43\\nrandom_s44\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "e7aa3e00-0357-4225-9b33-cda1e6445e5a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"random_s42\\\\nrandom_s43\\\\nrandom_s44\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"random_s42\\nrandom_s43\\nrandom_s44\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 14_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_012LibZ8F5iNfUHHZkzrdF8H`</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "find /root/structfuse -name \"analyze_stratified*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "168aad40-b995-442a-82d0-aa7b6606f12a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MESd3VEjz2zB2CibaveVLq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 482,
      "cache_read_input_tokens": 24745,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 482
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

_source line 15 · 2026-05-14T20:15:10.579Z_

<details><summary>↩ Tool result · `toolu_012LibZ8F5iNfUHHZkzrdF8H`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "dc2da30f-606c-4b8d-ac7a-cd12ce3f3e9e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 16_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Cr8UDRfmMiaLpbwvFQieZz`</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "find /root/structfuse -name \"*stratif*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "b0ea8f29-bd82-4eec-abf6-6b5fa27d05b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MESd3VEjz2zB2CibaveVLq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 482,
      "cache_read_input_tokens": 24745,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 482
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

_source line 17 · 2026-05-14T20:15:10.999Z_

<details><summary>↩ Tool result · `toolu_01Cr8UDRfmMiaLpbwvFQieZz`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "b2fcf162-99a7-40b1-8286-4f402772d620",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.41}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 18_

脚本不存在。看看服务器上现有的脚本和评估代码结构。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "b97da4b7-f012-4dcf-a482-83171bc60d95",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PEQGShBnS8z1WpBuVdY24i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 430,
      "cache_read_input_tokens": 25227,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 430
      },
      "output_tokens": 4,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01QX4297Wy2JaaSTLMuhfdzT`</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "ls /root/structfuse/scripts/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "f87f87d6-02b9-4f19-b411-c173b194ee47",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PEQGShBnS8z1WpBuVdY24i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 430,
      "cache_read_input_tokens": 25227,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 430
      },
      "output_tokens": 4,
      "service_tier": "standard",
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

_source line 20 · 2026-05-14T20:15:15.109Z_

<details><summary>↩ Tool result · `toolu_01QX4297Wy2JaaSTLMuhfdzT`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"__pycache__\\nanalyze_bm25_overlap_stratified.py\\nbuild_full_m2_data.sh\\nbuild_m1_training_data.py\\nbuild_m1_training_data.py.bak\\nbuild_p2b_data.py\\nclone_repos.sh\\ncollect_p2b_results.py\\ncompute_full_z_percent.py\\ndownload_metadata.py\\neval_p2b.py\\neval_p2b_pooled.py\\neval_swebench_e2e.py\\nfix_metadata.py\\nfix_metadata_arrow.py\\nmigrate_m1_data.sh\\nmine_bm25_negatives.py\\nplot_neg_difficulty.py\\nprepare_m1_rerun.py\\nrerun_m1_failed.sh\\nrun_50repo_overlap.py\\nrun_eval_5missing.sh\\nrun_eval_all.sh\\nrun_eval_p50.sh\\nrun_full_m2_training.sh\\nrun_m1_extraction.sh\\nrun_m2_full_bm25_qwen.sh\\nrun_m2_full_bm25_starcoder.sh\\nrun_m2_pilot.sh\\nrun_p2b_all.sh\\nschedule_m2_runs.sh\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "cb55b669-47c9-4128-9e0c-6cffa221fb7f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"__pycache__\\\\nanalyze_bm25_overlap_stratified.py\\\\nbuild_full_m2_data.sh\\\\nbuild_m1_training_data.py\\\\nbuild_m1_training_data.py.bak\\\\nbuild_p2b_data.py\\\\nclone_repos.sh\\\\ncollect_p2b_results.py\\\\ncompute_full_z_percent.py\\\\ndownload_metadata.py\\\\neval_p2b.py\\\\neval_p2b_pooled.py\\\\neval_swebench_e2e.py\\\\nfix_metadata.py\\\\nfix_metadata_arrow.py\\\\nmigrate_m1_data.sh\\\\nmine_bm25_negatives.py\\\\nplot_neg_difficulty.py\\\\nprepare_m1_rerun.py\\\\nrerun_m1_failed.sh\\\\nrun_50repo_overlap.py\\\\nrun_eval_5missing.sh\\\\nrun_eval_all.sh\\\\nrun_eval_p50.sh\\\\nrun_full_m2_training.sh\\\\nrun_m1_extraction.sh\\\\nrun_m2_full_bm25_qwen.sh\\\\nrun_m2_full_bm25_starcoder.sh\\\\nrun_m2_pilot.sh\\\\nrun_p2b_all.sh\\\\nschedule_m2_runs.sh\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"__pycache__\\nanalyze_bm25_overlap_stratified.py\\nbuild_full_m2_data.sh\\nbuild_m1_training_data.py\\nbuild_m1_training_data.py.bak\\nbuild_p2b_data.py\\nclone_repos.sh\\ncollect_p2b_results.py\\ncompute_full_z_percent.py\\ndownload_metadata.py\\neval_p2b.py\\neval_p2b_pooled.py\\neval_swebench_e2e.py\\nfix_metadata.py\\nfix_metadata_arrow.py\\nmigrate_m1_data.sh\\nmine_bm25_negatives.py\\nplot_neg_difficulty.py\\nprepare_m1_rerun.py\\nrerun_m1_failed.sh\\nrun_50repo_overlap.py\\nrun_eval_5missing.sh\\nrun_eval_all.sh\\nrun_eval_p50.sh\\nrun_full_m2_training.sh\\nrun_m1_extraction.sh\\nrun_m2_full_bm25_qwen.sh\\nrun_m2_full_bm25_starcoder.sh\\nrun_m2_pilot.sh\\nrun_p2b_all.sh\\nschedule_m2_runs.sh\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 21_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01WCPYLzVq9iCzvwLVGS37Qh`</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "ls /root/structfuse/evaluation/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "65e9b121-cd86-4381-85e7-89109490c74c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PEQGShBnS8z1WpBuVdY24i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 430,
      "cache_read_input_tokens": 25227,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 430
      },
      "output_tokens": 4,
      "service_tier": "standard",
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

_source line 22 · 2026-05-14T20:15:15.588Z_

<details><summary>↩ Tool result · `toolu_01WCPYLzVq9iCzvwLVGS37Qh`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"__pycache__\\nanalyze_stratified.py\\neval_repobench.py\\neval_retrieval.py\\neval_swebench.py\\neval_swebench.py.bak\\nlinear_proxy.py\\nlinear_proxy_results.json\\nplot_neg_difficulty.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "185d53e6-afe3-4a13-ab2f-bcf95125f594",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"__pycache__\\\\nanalyze_stratified.py\\\\neval_repobench.py\\\\neval_retrieval.py\\\\neval_swebench.py\\\\neval_swebench.py.bak\\\\nlinear_proxy.py\\\\nlinear_proxy_results.json\\\\nplot_neg_difficulty.py\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"__pycache__\\nanalyze_stratified.py\\neval_repobench.py\\neval_retrieval.py\\neval_swebench.py\\neval_swebench.py.bak\\nlinear_proxy.py\\nlinear_proxy_results.json\\nplot_neg_difficulty.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 23_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_017c8AAvQPRGhErUtKy3nbSn`</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "ls /root/structfuse/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "02562557-3d57-47ed-9974-f33b917ccf0c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PEQGShBnS8z1WpBuVdY24i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 430,
      "cache_read_input_tokens": 25227,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 430
      },
      "output_tokens": 4,
      "service_tier": "standard",
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

_source line 24 · 2026-05-14T20:15:16.063Z_

<details><summary>↩ Tool result · `toolu_017c8AAvQPRGhErUtKy3nbSn`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"analysis\\nartifacts\\nauto_start_dataflow.sh\\nconfigs\\neval_checkpoint.py\\nevaluation\\nextraction\\nmvp_phase1.py\\nmvp_phase1.py.bak\\nrequirements.txt\\nresults\\nrun_m2_bm25_qwen_s42.sh\\nrun_m2_early_pilot.sh\\nrun_m2_embed_verify.sh\\nrun_m2_embed_verify_continuation.sh\\nrun_m2_full_qwen.sh\\nrun_m2_full_starcoder.sh\\nrun_m2_full_starcoder_resume.sh\\nrun_m2_full_starcoder_s43plus.sh\\nrun_m2_s42_supplement.sh\\nrun_plan013_dataflow_retry.sh\\nrun_plan013_starcoder.sh\\nrun_plan014_temp_ablation.sh\\nrun_plan014_temp_ablation.sh.bak\\nrun_plan014_temp_cuda0.sh\\nrun_plan014_temp_cuda1.sh\\nrun_starcoder_data_build.sh\\nscripts\\ntea_debug.log\\ntraining\\nwandb\\nwatch_and_chain_qwen_s42.sh\\nwatch_and_chain_starcoder_s42.sh\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "8398aac6-113b-4ad9-a8ef-c3a12fe4dda0",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"analysis\\\\nartifacts\\\\nauto_start_dataflow.sh\\\\nconfigs\\\\neval_checkpoint.py\\\\nevaluation\\\\nextraction\\\\nmvp_phase1.py\\\\nmvp_phase1.py.bak\\\\nrequirements.txt\\\\nresults\\\\nrun_m2_bm25_qwen_s42.sh\\\\nrun_m2_early_pilot.sh\\\\nrun_m2_embed_verify.sh\\\\nrun_m2_embed_verify_continuation.sh\\\\nrun_m2_full_qwen.sh\\\\nrun_m2_full_starcoder.sh\\\\nrun_m2_full_starcoder_resume.sh\\\\nrun_m2_full_starcoder_s43plus.sh\\\\nrun_m2_s42_supplement.sh\\\\nrun_plan013_dataflow_retry.sh\\\\nrun_plan013_starcoder.sh\\\\nrun_plan014_temp_ablation.sh\\\\nrun_plan014_temp_ablation.sh.bak\\\\nrun_plan014_temp_cuda0.sh\\\\nrun_plan014_temp_cuda1.sh\\\\nrun_starcoder_data_build.sh\\\\nscripts\\\\ntea_debug.log\\\\ntraining\\\\nwandb\\\\nwatch_and_chain_qwen_s42.sh\\\\nwatch_and_chain_starcoder_s42.sh\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"analysis\\nartifacts\\nauto_start_dataflow.sh\\nconfigs\\neval_checkpoint.py\\nevaluation\\nextraction\\nmvp_phase1.py\\nmvp_phase1.py.bak\\nrequirements.txt\\nresults\\nrun_m2_bm25_qwen_s42.sh\\nrun_m2_early_pilot.sh\\nrun_m2_embed_verify.sh\\nrun_m2_embed_verify_continuation.sh\\nrun_m2_full_qwen.sh\\nrun_m2_full_starcoder.sh\\nrun_m2_full_starcoder_resume.sh\\nrun_m2_full_starcoder_s43plus.sh\\nrun_m2_s42_supplement.sh\\nrun_plan013_dataflow_retry.sh\\nrun_plan013_starcoder.sh\\nrun_plan014_temp_ablation.sh\\nrun_plan014_temp_ablation.sh.bak\\nrun_plan014_temp_cuda0.sh\\nrun_plan014_temp_cuda1.sh\\nrun_starcoder_data_build.sh\\nscripts\\ntea_debug.log\\ntraining\\nwandb\\nwatch_and_chain_qwen_s42.sh\\nwatch_and_chain_starcoder_s42.sh\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 25_

找到了 `/root/structfuse/evaluation/analyze_stratified.py`。还有一个相关的 `analyze_bm25_overlap_stratified.py` 在 scripts 目录。先读主脚本。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "3322c1fd-7a90-4d0e-b83e-cde9297608ea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JWijH1gkM8bm16Z9ggi91b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1507,
      "cache_read_input_tokens": 25657,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1507
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

_source line 26_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Qt6caVcovHUVZQPX8XhnDJ`</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "cat /root/structfuse/evaluation/analyze_stratified.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "a4cac3b6-8202-49fe-a2c2-895922d15080",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JWijH1gkM8bm16Z9ggi91b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1507,
      "cache_read_input_tokens": 25657,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1507
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

_source line 27 · 2026-05-14T20:15:20.694Z_

<details><summary>↩ Tool result · `toolu_01Qt6caVcovHUVZQPX8XhnDJ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Stratified analysis of embedding vs random negative strategies by data strata.\\n\\nAnalyses M2 per-instance predictions across:\\n  - Repo size (instance count per repo from M1)\\n  - Candidate pool size (neg_candidates per query)\\n  - Query-positive similarity (cosine sim from model, or text overlap for dry-run)\\n\\nInputs:\\n  - M2 per-instance predictions (from --predictions-dir or re-eval from checkpoints)\\n  - M1 all.jsonl (repo metadata)\\n  - Val JSONL files (query/candidate structure)\\n\\nOutputs:\\n  - stratified_results.json: full per-stratum metrics with bootstrap CI\\n  - stratified_summary.csv: compact table\\n  - stratified_plots.pdf: grouped bar charts, heatmaps, delta trends\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport csv\\nimport json\\nimport math\\nimport os\\nimport sys\\nfrom collections import Counter, defaultdict\\nfrom pathlib import Path\\nfrom typing import Any, Dict, List, Optional, Tuple\\n\\nimport numpy as np\\n\\nSTRATEGIES = [\\\"random\\\", \\\"embedding_distance\\\", \\\"dataflow_aware\\\"]\\nSTRATEGY_LABELS = {\\\"random\\\": \\\"Random\\\", \\\"embedding_distance\\\": \\\"Embedding\\\", \\\"dataflow_aware\\\": \\\"Dataflow\\\"}\\nSTRATEGY_COLORS = {\\\"random\\\": \\\"#4C72B0\\\", \\\"embedding_distance\\\": \\\"#DD8452\\\", \\\"dataflow_aware\\\": \\\"#55A868\\\"}\\n\\nREPO_SIZE_BINS = {\\n    \\\"small\\\": (0, 50),\\n    \\\"medium\\\": (50, 200),\\n    \\\"large\\\": (200, 500),\\n    \\\"xlarge\\\": (500, float(\\\"inf\\\")),\\n}\\n\\nPOOL_SIZE_BINS = {\\n    \\\"small\\\": (0, 20),\\n    \\\"medium\\\": (20, 40),\\n    \\\"large\\\": (40, 51),\\n}\\n\\nSIMILARITY_BINS = {\\n    \\\"low\\\": (0.0, 0.3),\\n    \\\"medium\\\": (0.3, 0.6),\\n    \\\"high\\\": (0.6, 1.01),\\n}\\n\\n\\ndef _bin_value(value, bins):\\n    for name, (lo, hi) in bins.items():\\n        if lo <= value < hi:\\n            return name\\n    return \\\"unknown\\\"\\n\\n\\n# ── M1 metadata ─────────────────────────────────────────────────────\\n\\ndef load_m1_metadata(m1_path: str) -> Tuple[Dict[str, str], Dict[str, int]]:\\n    import re\\n    inst_to_repo = {}\\n    repo_counts: Counter = Counter()\\n    pat_iid = re.compile(r'\\\"instance_id\\\"\\\\s*:\\\\s*\\\"([^\\\"]+)\\\"')\\n    pat_repo = re.compile(r'\\\"repo\\\"\\\\s*:\\\\s*\\\"([^\\\"]+)\\\"')\\n    with open(m1_path) as f:\\n        for line in f:\\n            m_iid = pat_iid.search(line)\\n            m_repo = pat_repo.search(line)\\n            if m_iid and m_repo:\\n                iid = m_iid.group(1)\\n                repo = m_repo.group(1)\\n                inst_to_repo[iid] = repo\\n                repo_counts[repo] += 1\\n    return inst_to_repo, dict(repo_counts)\\n\\n\\n# ── Val data loading ─────────────────────────────────────────────────\\n\\ndef load_val_samples(val_path: str, lite: bool = False) -> List[Dict[str, Any]]:\\n    \\\"\\\"\\\"Load val JSONL. lite=True skips candidate_tokens (faster for dry-run).\\\"\\\"\\\"\\n    import re\\n    samples = []\\n    pat_qid = re.compile(r'\\\"query_id\\\"\\\\s*:\\\\s*\\\"([^\\\"]+)\\\"')\\n    with open(val_path) as f:\\n        for line in f:\\n            if not line.strip():\\n                continue\\n            if lite:\\n                m = pat_qid.search(line)\\n                if not m:\\n                    continue\\n                qid = m.group(1)\\n                instance_id = qid.split(\\\"::\\\")[0] if \\\"::\\\" in qid else qid\\n                d = json.loads(line)\\n                samples.append({\\n                    \\\"query_id\\\": qid,\\n                    \\\"instance_id\\\": instance_id,\\n                    \\\"pool_size\\\": len(d.get(\\\"neg_candidates\\\", [])),\\n                    \\\"query_tokens\\\": d.get(\\\"query_tokens\\\", \\\"\\\")[:1000],\\n                    \\\"pos_tokens\\\": d.get(\\\"pos_tokens\\\", \\\"\\\")[:1000],\\n                    \\\"neg_candidates\\\": [],\\n                    \\\"candidate_tokens\\\": {},\\n                })\\n            else:\\n                d = json.loads(line)\\n                qid = d[\\\"query_id\\\"]\\n                instance_id = qid.split(\\\"::\\\")[0] if \\\"::\\\" in qid else qid\\n                samples.append({\\n                    \\\"query_id\\\": qid,\\n                    \\\"instance_id\\\": instance_id,\\n                    \\\"pool_size\\\": len(d.get(\\\"neg_candidates\\\", [])),\\n                    \\\"query_tokens\\\": d[\\\"query_tokens\\\"],\\n                    \\\"pos_tokens\\\": d[\\\"pos_tokens\\\"],\\n                    \\\"neg_candidates\\\": d.get(\\\"neg_candidates\\\", []),\\n\\n\\n... [截断: 输出过长，省略 21426 字符] ...\\n\\n file not found: {val_file}, skipping\\\", flush=True)\\n                continue\\n\\n            if args.dry_run:\\n                print(f\\\"  Generating mock predictions: {strategy} seed={seed}\\\", flush=True)\\n                results = mock_predictions(val_samples, strategy, seed)\\n            elif args.predictions_dir:\\n                pred_pattern = os.path.join(\\n                    args.predictions_dir, f\\\"*{strategy}*s{seed}*.json\\\"\\n                )\\n                import glob\\n                pred_files = glob.glob(pred_pattern)\\n                if pred_files:\\n                    print(f\\\"  Loading predictions: {pred_files[0]}\\\", flush=True)\\n                    results = load_predictions(pred_files[0], val_samples)\\n                else:\\n                    print(f\\\"  [WARN] No prediction file matching {pred_pattern}\\\", flush=True)\\n                    continue\\n            elif args.checkpoints_dir:\\n                ckpt_dir = os.path.join(\\n                    args.checkpoints_dir, f\\\"{strategy}_s{seed}\\\", \\\"best\\\"\\n                )\\n                if not os.path.exists(ckpt_dir):\\n                    ckpt_dir = os.path.join(args.checkpoints_dir, f\\\"{strategy}_s{seed}\\\")\\n                if os.path.exists(ckpt_dir):\\n                    print(f\\\"  Re-evaluating checkpoint: {ckpt_dir}\\\", flush=True)\\n                    results = reeval_checkpoint(\\n                        ckpt_dir, val_samples, args.device, args.max_seq_length\\n                    )\\n                else:\\n                    print(f\\\"  [WARN] Checkpoint not found: {ckpt_dir}\\\", flush=True)\\n                    continue\\n            else:\\n                print(\\\"  [ERROR] No --dry-run, --predictions-dir, or --checkpoints-dir\\\", flush=True)\\n                continue\\n\\n            # Assign strata\\n            results = assign_strata(results, inst_to_repo, repo_counts)\\n\\n            # For dry-run or model-based: compute text similarity for sim_bin\\n            if args.dry_run:\\n                for r, s in zip(results, val_samples):\\n                    tsim = text_similarity(s[\\\"query_tokens\\\"][:500], s[\\\"pos_tokens\\\"][:500])\\n                    r[\\\"sim_bin\\\"] = _bin_value(tsim, SIMILARITY_BINS)\\n\\n            all_results[strategy][seed] = results\\n            print(f\\\"  -> {len(results)} instances\\\", flush=True)\\n\\n    # Run stratified analysis\\n    print(\\\"\\\\nRunning stratified analysis...\\\", flush=True)\\n    repo_analysis = run_stratified_analysis(\\n        all_results, \\\"repo_size_bin\\\", list(REPO_SIZE_BINS.keys()), args.n_bootstrap\\n    )\\n    pool_analysis = run_stratified_analysis(\\n        all_results, \\\"pool_size_bin\\\", list(POOL_SIZE_BINS.keys()), args.n_bootstrap\\n    )\\n    sim_analysis = run_stratified_analysis(\\n        all_results, \\\"sim_bin\\\", list(SIMILARITY_BINS.keys()), args.n_bootstrap\\n    )\\n\\n    # Save JSON\\n    full_results = {\\n        \\\"config\\\": {\\n            \\\"strategies\\\": STRATEGIES,\\n            \\\"seeds\\\": seeds,\\n            \\\"repo_size_bins\\\": {k: list(v) for k, v in REPO_SIZE_BINS.items()},\\n            \\\"pool_size_bins\\\": {k: list(v) for k, v in POOL_SIZE_BINS.items()},\\n            \\\"similarity_bins\\\": {k: list(v) for k, v in SIMILARITY_BINS.items()},\\n            \\\"n_bootstrap\\\": args.n_bootstrap,\\n            \\\"dry_run\\\": args.dry_run,\\n        },\\n        \\\"by_repo_size\\\": repo_analysis,\\n        \\\"by_pool_size\\\": pool_analysis,\\n        \\\"by_similarity\\\": sim_analysis,\\n    }\\n\\n    json_path = os.path.join(args.output_dir, \\\"stratified_results.json\\\")\\n    with open(json_path, \\\"w\\\") as f:\\n        json.dump(full_results, f, indent=2, ensure_ascii=False)\\n    print(f\\\"  Results JSON saved to {json_path}\\\", flush=True)\\n\\n    # CSV summary\\n    csv_path = os.path.join(args.output_dir, \\\"stratified_summary.csv\\\")\\n    write_summary_csv(repo_analysis, pool_analysis, sim_analysis, csv_path)\\n\\n    # Plots\\n    try:\\n        make_plots(repo_analysis, pool_analysis, sim_analysis, args.output_dir)\\n    except Exception as e:\\n        print(f\\\"  [WARN] Plot generation failed: {e}\\\", flush=True)\\n\\n    print(\\\"\\\\nDone.\\\", flush=True)\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "c7650807-223a-47dc-8f9d-e73ce8f691e8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\n\\\\\\\"\\\\\\\"\\\\\\\"Stratified analysis of embedding vs random negative strategies by data strata.\\\\n\\\\nAnalyses M2 per-instance predictions across:\\\\n  - Repo size (instance count per repo from M1)\\\\n  - Candidate pool size (neg_candidates per query)\\\\n  - Query-positive similarity (cosine sim from model, or text overlap for dry-run)\\\\n\\\\nInputs:\\\\n  - M2 per-instance predictions (from --predictions-dir or re-eval from checkpoints)\\\\n  - M1 all.jsonl (repo metadata)\\\\n  - Val JSONL files (query/candidate structure)\\\\n\\\\nOutputs:\\\\n  - stratified_results.json: full per-stratum metrics with bootstrap CI\\\\n  - stratified_summary.csv: compact table\\\\n  - stratified_plots.pdf: grouped bar charts, heatmaps, delta trends\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport argparse\\\\nimport csv\\\\nimport json\\\\nimport math\\\\nimport os\\\\nimport sys\\\\nfrom collections import Counter, defaultdict\\\\nfrom pathlib import Path\\\\nfrom typing import Any, Dict, List, Optional, Tuple\\\\n\\\\nimport numpy as np\\\\n\\\\nSTRATEGIES = [\\\\\\\"random\\\\\\\", \\\\\\\"embedding_distance\\\\\\\", \\\\\\\"dataflow_aware\\\\\\\"]\\\\nSTRATEGY_LABELS = {\\\\\\\"random\\\\\\\": \\\\\\\"Random\\\\\\\", \\\\\\\"embedding_distance\\\\\\\": \\\\\\\"Embedding\\\\\\\", \\\\\\\"dataflow_aware\\\\\\\": \\\\\\\"Dataflow\\\\\\\"}\\\\nSTRATEGY_COLORS = {\\\\\\\"random\\\\\\\": \\\\\\\"#4C72B0\\\\\\\", \\\\\\\"embedding_distance\\\\\\\": \\\\\\\"#DD8452\\\\\\\", \\\\\\\"dataflow_aware\\\\\\\": \\\\\\\"#55A868\\\\\\\"}\\\\n\\\\nREPO_SIZE_BINS = {\\\\n    \\\\\\\"small\\\\\\\": (0, 50),\\\\n    \\\\\\\"medium\\\\\\\": (50, 200),\\\\n    \\\\\\\"large\\\\\\\": (200, 500),\\\\n    \\\\\\\"xlarge\\\\\\\": (500, float(\\\\\\\"inf\\\\\\\")),\\\\n}\\\\n\\\\nPOOL_SIZE_BINS = {\\\\n    \\\\\\\"small\\\\\\\": (0, 20),\\\\n    \\\\\\\"medium\\\\\\\": (20, 40),\\\\n    \\\\\\\"large\\\\\\\": (40, 51),\\\\n}\\\\n\\\\nSIMILARITY_BINS = {\\\\n    \\\\\\\"low\\\\\\\": (0.0, 0.3),\\\\n    \\\\\\\"medium\\\\\\\": (0.3, 0.6),\\\\n    \\\\\\\"high\\\\\\\": (0.6, 1.01),\\\\n}\\\\n\\\\n\\\\ndef _bin_value(value, bins):\\\\n    for name, (lo, hi) in bins.items():\\\\n        if lo <= value < hi:\\\\n            return name\\\\n    return \\\\\\\"unknown\\\\\\\"\\\\n\\\\n\\\\n# ── M1 metadata ─────────────────────────────────────────────────────\\\\n\\\\ndef load_m1_metadata(m1_path: str) -> Tuple[Dict[str, str], Dict[str, int]]:\\\\n    import re\\\\n    inst_to_repo = {}\\\\n    repo_counts: Counter = Counter()\\\\n    pat_iid = re.compile(r'\\\\\\\"instance_id\\\\\\\"\\\\\\\\s*:\\\\\\\\s*\\\\\\\"([^\\\\\\\"]+)\\\\\\\"')\\\\n    pat_repo = re.compile(r'\\\\\\\"repo\\\\\\\"\\\\\\\\s*:\\\\\\\\s*\\\\\\\"([^\\\\\\\"]+)\\\\\\\"')\\\\n    with open(m1_path) as f:\\\\n        for line in f:\\\\n            m_iid = pat_iid.search(line)\\\\n            m_repo = pat_repo.search(line)\\\\n            if m_iid and m_repo:\\\\n                iid = m_iid.group(1)\\\\n                repo = m_repo.group(1)\\\\n                inst_to_repo[iid] = repo\\\\n                repo_counts[repo] += 1\\\\n    return inst_to_repo, dict(repo_counts)\\\\n\\\\n\\\\n# ── Val data loading ─────────────────────────────────────────────────\\\\n\\\\ndef load_val_samples(val_path: str, lite: bool = False) -> List[Dict[str, Any]]:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Load val JSONL. lite=True skips candidate_tokens (faster for dry-run).\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    import re\\\\n    samples = []\\\\n    pat_qid = re.compile(r'\\\\\\\"query_id\\\\\\\"\\\\\\\\s*:\\\\\\\\s*\\\\\\\"([^\\\\\\\"]+)\\\\\\\"')\\\\n    with open(val_path) as f:\\\\n        for line in f:\\\\n            if not line.strip():\\\\n                continue\\\\n            if lite:\\\\n                m = pat_qid.search(line)\\\\n                if not m:\\\\n                    continue\\\\n                qid = m.group(1)\\\\n                instance_id = qid.split(\\\\\\\"::\\\\\\\")[0] if \\\\\\\"::\\\\\\\" in qid else qid\\\\n                d = json.loads(line)\\\\n                samples.append({\\\\n                    \\\\\\\"query_id\\\\\\\": qid,\\\\n                    \\\\\\\"instance_id\\\\\\\": instance_id,\\\\n                    \\\\\\\"pool_size\\\\\\\": len(d.get(\\\\\\\"neg_candidates\\\\\\\", [])),\\\\n                    \\\\\\\"query_tokens\\\\\\\": d.get(\\\\\\\"query_tokens\\\\\\\", \\\\\\\"\\\\\\\")[:1000],\\\\n                    \\\\\\\"pos_tokens\\\\\\\": d.get(\\\\\\\"pos_tokens\\\\\\\", \\\\\\\"\\\\\\\")[:1000],\\\\n                    \\\\\\\"neg_candidates\\\\\\\": [],\\\\n                    \\\\\\\"candidate_tokens\\\\\\\": {},\\\\n                })\\\\n            else:\\\\n                d = json.loads(line)\\\\n                qid = d[\\\\\\\"query_id\\\\\\\"]\\\\n                instance_id = qid.split(\\\\\\\"::\\\\\\\")[0] if \\\\\\\"::\\\\\\\" in qid else qid\\\\n                samples.append({\\\\n                    \\\\\\\"query_id\\\\\\\": qid,\\\\n                    \\\\\\\"instance_id\\\\\\\": instance_id,\\\\n                    \\\\\\\"pool_size\\\\\\\": len(d.get(\\\\\\\"neg_candidates\\\\\\\", [])),\\\\n                    \\\\\\\"query_tokens\\\\\\\": d[\\\\\\\"query_tokens\\\\\\\"],\\\\n                    \\\\\\\"pos_tokens\\\\\\\": d[\\\\\\\"pos_tokens\\\\\\\"],\\\\n                    \\\\\\\"neg_candidates\\\\\\\": d.get(\\\\\\\"neg_candidates\\\\\\\", []),\\\\n\\\\n\\\\n... [截断: 输出过长，省略 21426 字符] ...\\\\n\\\\n file not found: {val_file}, skipping\\\\\\\", flush=True)\\\\n                continue\\\\n\\\\n            if args.dry_run:\\\\n                print(f\\\\\\\"  Generating mock predictions: {strategy} seed={seed}\\\\\\\", flush=True)\\\\n                results = mock_predictions(val_samples, strategy, seed)\\\\n            elif args.predictions_dir:\\\\n                pred_pattern = os.path.join(\\\\n                    args.predictions_dir, f\\\\\\\"*{strategy}*s{seed}*.json\\\\\\\"\\\\n                )\\\\n                import glob\\\\n                pred_files = glob.glob(pred_pattern)\\\\n                if pred_files:\\\\n                    print(f\\\\\\\"  Loading predictions: {pred_files[0]}\\\\\\\", flush=True)\\\\n                    results = load_predictions(pred_files[0], val_samples)\\\\n                else:\\\\n                    print(f\\\\\\\"  [WARN] No prediction file matching {pred_pattern}\\\\\\\", flush=True)\\\\n                    continue\\\\n            elif args.checkpoints_dir:\\\\n                ckpt_dir = os.path.join(\\\\n                    args.checkpoints_dir, f\\\\\\\"{strategy}_s{seed}\\\\\\\", \\\\\\\"best\\\\\\\"\\\\n                )\\\\n                if not os.path.exists(ckpt_dir):\\\\n                    ckpt_dir = os.path.join(args.checkpoints_dir, f\\\\\\\"{strategy}_s{seed}\\\\\\\")\\\\n                if os.path.exists(ckpt_dir):\\\\n                    print(f\\\\\\\"  Re-evaluating checkpoint: {ckpt_dir}\\\\\\\", flush=True)\\\\n                    results = reeval_checkpoint(\\\\n                        ckpt_dir, val_samples, args.device, args.max_seq_length\\\\n                    )\\\\n                else:\\\\n                    print(f\\\\\\\"  [WARN] Checkpoint not found: {ckpt_dir}\\\\\\\", flush=True)\\\\n                    continue\\\\n            else:\\\\n                print(\\\\\\\"  [ERROR] No --dry-run, --predictions-dir, or --checkpoints-dir\\\\\\\", flush=True)\\\\n                continue\\\\n\\\\n            # Assign strata\\\\n            results = assign_strata(results, inst_to_repo, repo_counts)\\\\n\\\\n            # For dry-run or model-based: compute text similarity for sim_bin\\\\n            if args.dry_run:\\\\n                for r, s in zip(results, val_samples):\\\\n                    tsim = text_similarity(s[\\\\\\\"query_tokens\\\\\\\"][:500], s[\\\\\\\"pos_tokens\\\\\\\"][:500])\\\\n                    r[\\\\\\\"sim_bin\\\\\\\"] = _bin_value(tsim, SIMILARITY_BINS)\\\\n\\\\n            all_results[strategy][seed] = results\\\\n            print(f\\\\\\\"  -> {len(results)} instances\\\\\\\", flush=True)\\\\n\\\\n    # Run stratified analysis\\\\n    print(\\\\\\\"\\\\\\\\nRunning stratified analysis...\\\\\\\", flush=True)\\\\n    repo_analysis = run_stratified_analysis(\\\\n        all_results, \\\\\\\"repo_size_bin\\\\\\\", list(REPO_SIZE_BINS.keys()), args.n_bootstrap\\\\n    )\\\\n    pool_analysis = run_stratified_analysis(\\\\n        all_results, \\\\\\\"pool_size_bin\\\\\\\", list(POOL_SIZE_BINS.keys()), args.n_bootstrap\\\\n    )\\\\n    sim_analysis = run_stratified_analysis(\\\\n        all_results, \\\\\\\"sim_bin\\\\\\\", list(SIMILARITY_BINS.keys()), args.n_bootstrap\\\\n    )\\\\n\\\\n    # Save JSON\\\\n    full_results = {\\\\n        \\\\\\\"config\\\\\\\": {\\\\n            \\\\\\\"strategies\\\\\\\": STRATEGIES,\\\\n            \\\\\\\"seeds\\\\\\\": seeds,\\\\n            \\\\\\\"repo_size_bins\\\\\\\": {k: list(v) for k, v in REPO_SIZE_BINS.items()},\\\\n            \\\\\\\"pool_size_bins\\\\\\\": {k: list(v) for k, v in POOL_SIZE_BINS.items()},\\\\n            \\\\\\\"similarity_bins\\\\\\\": {k: list(v) for k, v in SIMILARITY_BINS.items()},\\\\n            \\\\\\\"n_bootstrap\\\\\\\": args.n_bootstrap,\\\\n            \\\\\\\"dry_run\\\\\\\": args.dry_run,\\\\n        },\\\\n        \\\\\\\"by_repo_size\\\\\\\": repo_analysis,\\\\n        \\\\\\\"by_pool_size\\\\\\\": pool_analysis,\\\\n        \\\\\\\"by_similarity\\\\\\\": sim_analysis,\\\\n    }\\\\n\\\\n    json_path = os.path.join(args.output_dir, \\\\\\\"stratified_results.json\\\\\\\")\\\\n    with open(json_path, \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(full_results, f, indent=2, ensure_ascii=False)\\\\n    print(f\\\\\\\"  Results JSON saved to {json_path}\\\\\\\", flush=True)\\\\n\\\\n    # CSV summary\\\\n    csv_path = os.path.join(args.output_dir, \\\\\\\"stratified_summary.csv\\\\\\\")\\\\n    write_summary_csv(repo_analysis, pool_analysis, sim_analysis, csv_path)\\\\n\\\\n    # Plots\\\\n    try:\\\\n        make_plots(repo_analysis, pool_analysis, sim_analysis, args.output_dir)\\\\n    except Exception as e:\\\\n        print(f\\\\\\\"  [WARN] Plot generation failed: {e}\\\\\\\", flush=True)\\\\n\\\\n    print(\\\\\\\"\\\\\\\\nDone.\\\\\\\", flush=True)\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.39}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Stratified analysis of embedding vs random negative strategies by data strata.\\n\\nAnalyses M2 per-instance predictions across:\\n  - Repo size (instance count per repo from M1)\\n  - Candidate pool size (neg_candidates per query)\\n  - Query-positive similarity (cosine sim from model, or text overlap for dry-run)\\n\\nInputs:\\n  - M2 per-instance predictions (from --predictions-dir or re-eval from checkpoints)\\n  - M1 all.jsonl (repo metadata)\\n  - Val JSONL files (query/candidate structure)\\n\\nOutputs:\\n  - stratified_results.json: full per-stratum metrics with bootstrap CI\\n  - stratified_summary.csv: compact table\\n  - stratified_plots.pdf: grouped bar charts, heatmaps, delta trends\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport csv\\nimport json\\nimport math\\nimport os\\nimport sys\\nfrom collections import Counter, defaultdict\\nfrom pathlib import Path\\nfrom typing import Any, Dict, List, Optional, Tuple\\n\\nimport numpy as np\\n\\nSTRATEGIES = [\\\"random\\\", \\\"embedding_distance\\\", \\\"dataflow_aware\\\"]\\nSTRATEGY_LABELS = {\\\"random\\\": \\\"Random\\\", \\\"embedding_distance\\\": \\\"Embedding\\\", \\\"dataflow_aware\\\": \\\"Dataflow\\\"}\\nSTRATEGY_COLORS = {\\\"random\\\": \\\"#4C72B0\\\", \\\"embedding_distance\\\": \\\"#DD8452\\\", \\\"dataflow_aware\\\": \\\"#55A868\\\"}\\n\\nREPO_SIZE_BINS = {\\n    \\\"small\\\": (0, 50),\\n    \\\"medium\\\": (50, 200),\\n    \\\"large\\\": (200, 500),\\n    \\\"xlarge\\\": (500, float(\\\"inf\\\")),\\n}\\n\\nPOOL_SIZE_BINS = {\\n    \\\"small\\\": (0, 20),\\n    \\\"medium\\\": (20, 40),\\n    \\\"large\\\": (40, 51),\\n}\\n\\nSIMILARITY_BINS = {\\n    \\\"low\\\": (0.0, 0.3),\\n    \\\"medium\\\": (0.3, 0.6),\\n    \\\"high\\\": (0.6, 1.01),\\n}\\n\\n\\ndef _bin_value(value, bins):\\n    for name, (lo, hi) in bins.items():\\n        if lo <= value < hi:\\n            return name\\n    return \\\"unknown\\\"\\n\\n\\n# ── M1 metadata ─────────────────────────────────────────────────────\\n\\ndef load_m1_metadata(m1_path: str) -> Tuple[Dict[str, str], Dict[str, int]]:\\n    import re\\n    inst_to_repo = {}\\n    repo_counts: Counter = Counter()\\n    pat_iid = re.compile(r'\\\"instance_id\\\"\\\\s*:\\\\s*\\\"([^\\\"]+)\\\"')\\n    pat_repo = re.compile(r'\\\"repo\\\"\\\\s*:\\\\s*\\\"([^\\\"]+)\\\"')\\n    with open(m1_path) as f:\\n        for line in f:\\n            m_iid = pat_iid.search(line)\\n            m_repo = pat_repo.search(line)\\n            if m_iid and m_repo:\\n                iid = m_iid.group(1)\\n                repo = m_repo.group(1)\\n                inst_to_repo[iid] = repo\\n                repo_counts[repo] += 1\\n    return inst_to_repo, dict(repo_counts)\\n\\n\\n# ── Val data loading ─────────────────────────────────────────────────\\n\\ndef load_val_samples(val_path: str, lite: bool = False) -> List[Dict[str, Any]]:\\n    \\\"\\\"\\\"Load val JSONL. lite=True skips candidate_tokens (faster for dry-run).\\\"\\\"\\\"\\n    import re\\n    samples = []\\n    pat_qid = re.compile(r'\\\"query_id\\\"\\\\s*:\\\\s*\\\"([^\\\"]+)\\\"')\\n    with open(val_path) as f:\\n        for line in f:\\n            if not line.strip():\\n                continue\\n            if lite:\\n                m = pat_qid.search(line)\\n                if not m:\\n                    continue\\n                qid = m.group(1)\\n                instance_id = qid.split(\\\"::\\\")[0] if \\\"::\\\" in qid else qid\\n                d = json.loads(line)\\n                samples.append({\\n                    \\\"query_id\\\": qid,\\n                    \\\"instance_id\\\": instance_id,\\n                    \\\"pool_size\\\": len(d.get(\\\"neg_candidates\\\", [])),\\n                    \\\"query_tokens\\\": d.get(\\\"query_tokens\\\", \\\"\\\")[:1000],\\n                    \\\"pos_tokens\\\": d.get(\\\"pos_tokens\\\", \\\"\\\")[:1000],\\n                    \\\"neg_candidates\\\": [],\\n                    \\\"candidate_tokens\\\": {},\\n                })\\n            else:\\n                d = json.loads(line)\\n                qid = d[\\\"query_id\\\"]\\n                instance_id = qid.split(\\\"::\\\")[0] if \\\"::\\\" in qid else qid\\n                samples.append({\\n                    \\\"query_id\\\": qid,\\n                    \\\"instance_id\\\": instance_id,\\n                    \\\"pool_size\\\": len(d.get(\\\"neg_candidates\\\", [])),\\n                    \\\"query_tokens\\\": d[\\\"query_tokens\\\"],\\n                    \\\"pos_tokens\\\": d[\\\"pos_tokens\\\"],\\n                    \\\"neg_candidates\\\": d.get(\\\"neg_candidates\\\", []),\\n\\n\\n... [截断: 输出过长，省略 21426 字符] ...\\n\\n file not found: {val_file}, skipping\\\", flush=True)\\n                continue\\n\\n            if args.dry_run:\\n                print(f\\\"  Generating mock predictions: {strategy} seed={seed}\\\", flush=True)\\n                results = mock_predictions(val_samples, strategy, seed)\\n            elif args.predictions_dir:\\n                pred_pattern = os.path.join(\\n                    args.predictions_dir, f\\\"*{strategy}*s{seed}*.json\\\"\\n                )\\n                import glob\\n                pred_files = glob.glob(pred_pattern)\\n                if pred_files:\\n                    print(f\\\"  Loading predictions: {pred_files[0]}\\\", flush=True)\\n                    results = load_predictions(pred_files[0], val_samples)\\n                else:\\n                    print(f\\\"  [WARN] No prediction file matching {pred_pattern}\\\", flush=True)\\n                    continue\\n            elif args.checkpoints_dir:\\n                ckpt_dir = os.path.join(\\n                    args.checkpoints_dir, f\\\"{strategy}_s{seed}\\\", \\\"best\\\"\\n                )\\n                if not os.path.exists(ckpt_dir):\\n                    ckpt_dir = os.path.join(args.checkpoints_dir, f\\\"{strategy}_s{seed}\\\")\\n                if os.path.exists(ckpt_dir):\\n                    print(f\\\"  Re-evaluating checkpoint: {ckpt_dir}\\\", flush=True)\\n                    results = reeval_checkpoint(\\n                        ckpt_dir, val_samples, args.device, args.max_seq_length\\n                    )\\n                else:\\n                    print(f\\\"  [WARN] Checkpoint not found: {ckpt_dir}\\\", flush=True)\\n                    continue\\n            else:\\n                print(\\\"  [ERROR] No --dry-run, --predictions-dir, or --checkpoints-dir\\\", flush=True)\\n                continue\\n\\n            # Assign strata\\n            results = assign_strata(results, inst_to_repo, repo_counts)\\n\\n            # For dry-run or model-based: compute text similarity for sim_bin\\n            if args.dry_run:\\n                for r, s in zip(results, val_samples):\\n                    tsim = text_similarity(s[\\\"query_tokens\\\"][:500], s[\\\"pos_tokens\\\"][:500])\\n                    r[\\\"sim_bin\\\"] = _bin_value(tsim, SIMILARITY_BINS)\\n\\n            all_results[strategy][seed] = results\\n            print(f\\\"  -> {len(results)} instances\\\", flush=True)\\n\\n    # Run stratified analysis\\n    print(\\\"\\\\nRunning stratified analysis...\\\", flush=True)\\n    repo_analysis = run_stratified_analysis(\\n        all_results, \\\"repo_size_bin\\\", list(REPO_SIZE_BINS.keys()), args.n_bootstrap\\n    )\\n    pool_analysis = run_stratified_analysis(\\n        all_results, \\\"pool_size_bin\\\", list(POOL_SIZE_BINS.keys()), args.n_bootstrap\\n    )\\n    sim_analysis = run_stratified_analysis(\\n        all_results, \\\"sim_bin\\\", list(SIMILARITY_BINS.keys()), args.n_bootstrap\\n    )\\n\\n    # Save JSON\\n    full_results = {\\n        \\\"config\\\": {\\n            \\\"strategies\\\": STRATEGIES,\\n            \\\"seeds\\\": seeds,\\n            \\\"repo_size_bins\\\": {k: list(v) for k, v in REPO_SIZE_BINS.items()},\\n            \\\"pool_size_bins\\\": {k: list(v) for k, v in POOL_SIZE_BINS.items()},\\n            \\\"similarity_bins\\\": {k: list(v) for k, v in SIMILARITY_BINS.items()},\\n            \\\"n_bootstrap\\\": args.n_bootstrap,\\n            \\\"dry_run\\\": args.dry_run,\\n        },\\n        \\\"by_repo_size\\\": repo_analysis,\\n        \\\"by_pool_size\\\": pool_analysis,\\n        \\\"by_similarity\\\": sim_analysis,\\n    }\\n\\n    json_path = os.path.join(args.output_dir, \\\"stratified_results.json\\\")\\n    with open(json_path, \\\"w\\\") as f:\\n        json.dump(full_results, f, indent=2, ensure_ascii=False)\\n    print(f\\\"  Results JSON saved to {json_path}\\\", flush=True)\\n\\n    # CSV summary\\n    csv_path = os.path.join(args.output_dir, \\\"stratified_summary.csv\\\")\\n    write_summary_csv(repo_analysis, pool_analysis, sim_analysis, csv_path)\\n\\n    # Plots\\n    try:\\n        make_plots(repo_analysis, pool_analysis, sim_analysis, args.output_dir)\\n    except Exception as e:\\n        print(f\\\"  [WARN] Plot generation failed: {e}\\\", flush=True)\\n\\n    print(\\\"\\\\nDone.\\\", flush=True)\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 28_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01FWD4dyYUBgTQSiwSG3r61u`</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "cat /root/structfuse/scripts/analyze_bm25_overlap_stratified.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "7a6392d5-6ce8-4ffc-922a-0cc09ab00a63",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JWijH1gkM8bm16Z9ggi91b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1507,
      "cache_read_input_tokens": 25657,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1507
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

_source line 29 · 2026-05-14T20:15:21.390Z_

<details><summary>↩ Tool result · `toolu_01FWD4dyYUBgTQSiwSG3r61u`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"# Stratified BM25 overlap analysis: compares BM25 top-k negatives against\\n# other mining strategies (random, embedding_distance, dataflow_aware),\\n# stratified by repo size (unique file count).\\n#\\n# Input:  /root/autodl-tmp/structfuse/full_m2_training_data/train_{strategy}_s42.jsonl\\n# Output: /root/autodl-tmp/structfuse/artifacts/bm25_overlap_stratified.json\\n\\nimport json\\nimport os\\nfrom collections import defaultdict\\n\\nimport numpy as np\\n\\nDATA_DIR = \\\"/root/autodl-tmp/structfuse/full_m2_training_data\\\"\\nOUT_PATH = \\\"/root/autodl-tmp/structfuse/artifacts/bm25_overlap_stratified.json\\\"\\nSTRATEGIES = [\\\"random\\\", \\\"embedding_distance\\\", \\\"dataflow_aware\\\"]\\nSEED = 42\\nK = 7\\nTIERS = {\\n    \\\"small_lt50\\\": (0, 50),\\n    \\\"medium_50_200\\\": (50, 201),\\n    \\\"large_200plus\\\": (201, float(\\\"inf\\\")),\\n}\\n\\n\\ndef extract_repo(query_id: str) -> str:\\n    iid = query_id.split(\\\"::\\\")[0]\\n    return iid.split(\\\".\\\")[0]\\n\\n\\ndef extract_filepath(full_id: str) -> str:\\n    return full_id.split(\\\"::\\\", 1)[1]\\n\\n\\ndef jaccard(a: set, b: set) -> float:\\n    if not a and not b:\\n        return 1.0\\n    union = a | b\\n    if not union:\\n        return 0.0\\n    return len(a & b) / len(union)\\n\\n\\ndef load_strategy(name: str) -> dict:\\n    path = os.path.join(DATA_DIR, f\\\"train_{name}_s{SEED}.jsonl\\\")\\n    data = {}\\n    with open(path) as f:\\n        for line in f:\\n            d = json.loads(line)\\n            data[d[\\\"query_id\\\"]] = d[\\\"neg_candidates\\\"]\\n    return data\\n\\n\\ndef main():\\n    # 1. Load all strategies\\n    bm25_data = load_strategy(\\\"bm25\\\")\\n    other_data = {s: load_strategy(s) for s in STRATEGIES}\\n\\n    # 2. Build repo file count (union of all file paths across all strategies)\\n    repo_files = defaultdict(set)\\n    for qid, negs in bm25_data.items():\\n        repo = extract_repo(qid)\\n        repo_files[repo].add(extract_filepath(qid))\\n        for nc in negs:\\n            repo_files[repo].add(extract_filepath(nc))\\n    for strat in STRATEGIES:\\n        for qid, negs in other_data[strat].items():\\n            repo = extract_repo(qid)\\n            repo_files[repo].add(extract_filepath(qid))\\n            for nc in negs:\\n                repo_files[repo].add(extract_filepath(nc))\\n\\n    repo_size = {repo: len(files) for repo, files in repo_files.items()}\\n\\n    # 3. Compute per-query overlaps (only for queries present in both BM25 and other)\\n    records = []  # list of dicts with overlap info per query\\n    for qid, bm25_negs in bm25_data.items():\\n        repo = extract_repo(qid)\\n        rsize = repo_size.get(repo, 0)\\n        bm25_topk = set(bm25_negs[:K])\\n\\n        row = {\\n            \\\"query_id\\\": qid,\\n            \\\"repo\\\": repo,\\n            \\\"repo_size\\\": rsize,\\n            \\\"bm25_pool_size\\\": len(bm25_negs),\\n        }\\n        for strat in STRATEGIES:\\n            if qid in other_data[strat]:\\n                other_topk = set(other_data[strat][qid][:K])\\n                row[f\\\"overlap_{strat}\\\"] = jaccard(bm25_topk, other_topk)\\n            else:\\n                row[f\\\"overlap_{strat}\\\"] = None\\n        records.append(row)\\n\\n    # 4. Stratify and compute stats\\n    def compute_tier_stats(tier_records):\\n        repos_in_tier = set(r[\\\"repo\\\"] for r in tier_records)\\n        stats = {\\n            \\\"repo_count\\\": len(repos_in_tier),\\n            \\\"instance_count\\\": len(tier_records),\\n        }\\n        for strat in STRATEGIES:\\n            key = f\\\"overlap_{strat}\\\"\\n            vals = [r[key] for r in tier_records if r[key] is not None]\\n            if vals:\\n                arr = np.array(vals)\\n                stats[f\\\"avg_overlap_bm25_{strat.replace('embedding_distance','embedding')}\\\"] = round(float(arr.mean()), 4)\\n                stats[f\\\"median_overlap_bm25_{strat.replace('embedding_distance','embedding')}\\\"] = round(float(np.median(arr)), 4)\\n                stats[f\\\"matched_queries_{strat.replace('embedding_distance','embedding')}\\\"] = len(vals)\\n            else:\\n                stats[f\\\"avg_overlap_bm25_{strat.replace('embedding_distance','embedding')}\\\"] = None\\n                stats[f\\\"median_overlap_bm25_{strat.replace('embedding_distance','embedding')}\\\"] = None\\n                stats[f\\\"matched_queries_{strat.replace('embedding_distance','embedding')}\\\"] = 0\\n        return stats\\n\\n    result = {\\n        \\\"overall\\\": compute_tier_stats(records),\\n        \\\"seed\\\": f\\\"s{SEED} only\\\",\\n        \\\"k\\\": K,\\n        \\\"repo_size_method\\\": \\\"union of unique file paths across all strategies\\\",\\n    }\\n\\n    for tier_name, (lo, hi) in TIERS.items():\\n        tier_records = [r for r in records if lo <= r[\\\"repo_size\\\"] < hi]\\n        result[tier_name] = compute_tier_stats(tier_records)\\n        # Add repo size stats for this tier\\n        sizes = [r[\\\"repo_size\\\"] for r in tier_records]\\n        if sizes:\\n            result[tier_name][\\\"avg_repo_size\\\"] = round(float(np.mean(sizes)), 1)\\n            result[tier_name][\\\"min_repo_size\\\"] = int(min(sizes))\\n            result[tier_name][\\\"max_repo_size\\\"] = int(max(sizes))\\n\\n    # Add per-tier BM25 pool size stats (how many BM25 candidates available)\\n    for tier_name, (lo, hi) in TIERS.items():\\n        tier_records = [r for r in records if lo <= r[\\\"repo_size\\\"] < hi]\\n        pools = [r[\\\"bm25_pool_size\\\"] for r in tier_records]\\n        if pools:\\n            result[tier_name][\\\"avg_bm25_pool_size\\\"] = round(float(np.mean(pools)), 1)\\n\\n    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)\\n    with open(OUT_PATH, \\\"w\\\") as f:\\n        json.dump(result, f, indent=2, ensure_ascii=False)\\n\\n    print(json.dumps(result, indent=2, ensure_ascii=False))\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "df2ead8c-e6e2-40c2-89a6-0e09ca25a408",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"# Stratified BM25 overlap analysis: compares BM25 top-k negatives against\\\\n# other mining strategies (random, embedding_distance, dataflow_aware),\\\\n# stratified by repo size (unique file count).\\\\n#\\\\n# Input:  /root/autodl-tmp/structfuse/full_m2_training_data/train_{strategy}_s42.jsonl\\\\n# Output: /root/autodl-tmp/structfuse/artifacts/bm25_overlap_stratified.json\\\\n\\\\nimport json\\\\nimport os\\\\nfrom collections import defaultdict\\\\n\\\\nimport numpy as np\\\\n\\\\nDATA_DIR = \\\\\\\"/root/autodl-tmp/structfuse/full_m2_training_data\\\\\\\"\\\\nOUT_PATH = \\\\\\\"/root/autodl-tmp/structfuse/artifacts/bm25_overlap_stratified.json\\\\\\\"\\\\nSTRATEGIES = [\\\\\\\"random\\\\\\\", \\\\\\\"embedding_distance\\\\\\\", \\\\\\\"dataflow_aware\\\\\\\"]\\\\nSEED = 42\\\\nK = 7\\\\nTIERS = {\\\\n    \\\\\\\"small_lt50\\\\\\\": (0, 50),\\\\n    \\\\\\\"medium_50_200\\\\\\\": (50, 201),\\\\n    \\\\\\\"large_200plus\\\\\\\": (201, float(\\\\\\\"inf\\\\\\\")),\\\\n}\\\\n\\\\n\\\\ndef extract_repo(query_id: str) -> str:\\\\n    iid = query_id.split(\\\\\\\"::\\\\\\\")[0]\\\\n    return iid.split(\\\\\\\".\\\\\\\")[0]\\\\n\\\\n\\\\ndef extract_filepath(full_id: str) -> str:\\\\n    return full_id.split(\\\\\\\"::\\\\\\\", 1)[1]\\\\n\\\\n\\\\ndef jaccard(a: set, b: set) -> float:\\\\n    if not a and not b:\\\\n        return 1.0\\\\n    union = a | b\\\\n    if not union:\\\\n        return 0.0\\\\n    return len(a & b) / len(union)\\\\n\\\\n\\\\ndef load_strategy(name: str) -> dict:\\\\n    path = os.path.join(DATA_DIR, f\\\\\\\"train_{name}_s{SEED}.jsonl\\\\\\\")\\\\n    data = {}\\\\n    with open(path) as f:\\\\n        for line in f:\\\\n            d = json.loads(line)\\\\n            data[d[\\\\\\\"query_id\\\\\\\"]] = d[\\\\\\\"neg_candidates\\\\\\\"]\\\\n    return data\\\\n\\\\n\\\\ndef main():\\\\n    # 1. Load all strategies\\\\n    bm25_data = load_strategy(\\\\\\\"bm25\\\\\\\")\\\\n    other_data = {s: load_strategy(s) for s in STRATEGIES}\\\\n\\\\n    # 2. Build repo file count (union of all file paths across all strategies)\\\\n    repo_files = defaultdict(set)\\\\n    for qid, negs in bm25_data.items():\\\\n        repo = extract_repo(qid)\\\\n        repo_files[repo].add(extract_filepath(qid))\\\\n        for nc in negs:\\\\n            repo_files[repo].add(extract_filepath(nc))\\\\n    for strat in STRATEGIES:\\\\n        for qid, negs in other_data[strat].items():\\\\n            repo = extract_repo(qid)\\\\n            repo_files[repo].add(extract_filepath(qid))\\\\n            for nc in negs:\\\\n                repo_files[repo].add(extract_filepath(nc))\\\\n\\\\n    repo_size = {repo: len(files) for repo, files in repo_files.items()}\\\\n\\\\n    # 3. Compute per-query overlaps (only for queries present in both BM25 and other)\\\\n    records = []  # list of dicts with overlap info per query\\\\n    for qid, bm25_negs in bm25_data.items():\\\\n        repo = extract_repo(qid)\\\\n        rsize = repo_size.get(repo, 0)\\\\n        bm25_topk = set(bm25_negs[:K])\\\\n\\\\n        row = {\\\\n            \\\\\\\"query_id\\\\\\\": qid,\\\\n            \\\\\\\"repo\\\\\\\": repo,\\\\n            \\\\\\\"repo_size\\\\\\\": rsize,\\\\n            \\\\\\\"bm25_pool_size\\\\\\\": len(bm25_negs),\\\\n        }\\\\n        for strat in STRATEGIES:\\\\n            if qid in other_data[strat]:\\\\n                other_topk = set(other_data[strat][qid][:K])\\\\n                row[f\\\\\\\"overlap_{strat}\\\\\\\"] = jaccard(bm25_topk, other_topk)\\\\n            else:\\\\n                row[f\\\\\\\"overlap_{strat}\\\\\\\"] = None\\\\n        records.append(row)\\\\n\\\\n    # 4. Stratify and compute stats\\\\n    def compute_tier_stats(tier_records):\\\\n        repos_in_tier = set(r[\\\\\\\"repo\\\\\\\"] for r in tier_records)\\\\n        stats = {\\\\n            \\\\\\\"repo_count\\\\\\\": len(repos_in_tier),\\\\n            \\\\\\\"instance_count\\\\\\\": len(tier_records),\\\\n        }\\\\n        for strat in STRATEGIES:\\\\n            key = f\\\\\\\"overlap_{strat}\\\\\\\"\\\\n            vals = [r[key] for r in tier_records if r[key] is not None]\\\\n            if vals:\\\\n                arr = np.array(vals)\\\\n                stats[f\\\\\\\"avg_overlap_bm25_{strat.replace('embedding_distance','embedding')}\\\\\\\"] = round(float(arr.mean()), 4)\\\\n                stats[f\\\\\\\"median_overlap_bm25_{strat.replace('embedding_distance','embedding')}\\\\\\\"] = round(float(np.median(arr)), 4)\\\\n                stats[f\\\\\\\"matched_queries_{strat.replace('embedding_distance','embedding')}\\\\\\\"] = len(vals)\\\\n            else:\\\\n                stats[f\\\\\\\"avg_overlap_bm25_{strat.replace('embedding_distance','embedding')}\\\\\\\"] = None\\\\n                stats[f\\\\\\\"median_overlap_bm25_{strat.replace('embedding_distance','embedding')}\\\\\\\"] = None\\\\n                stats[f\\\\\\\"matched_queries_{strat.replace('embedding_distance','embedding')}\\\\\\\"] = 0\\\\n        return stats\\\\n\\\\n    result = {\\\\n        \\\\\\\"overall\\\\\\\": compute_tier_stats(records),\\\\n        \\\\\\\"seed\\\\\\\": f\\\\\\\"s{SEED} only\\\\\\\",\\\\n        \\\\\\\"k\\\\\\\": K,\\\\n        \\\\\\\"repo_size_method\\\\\\\": \\\\\\\"union of unique file paths across all strategies\\\\\\\",\\\\n    }\\\\n\\\\n    for tier_name, (lo, hi) in TIERS.items():\\\\n        tier_records = [r for r in records if lo <= r[\\\\\\\"repo_size\\\\\\\"] < hi]\\\\n        result[tier_name] = compute_tier_stats(tier_records)\\\\n        # Add repo size stats for this tier\\\\n        sizes = [r[\\\\\\\"repo_size\\\\\\\"] for r in tier_records]\\\\n        if sizes:\\\\n            result[tier_name][\\\\\\\"avg_repo_size\\\\\\\"] = round(float(np.mean(sizes)), 1)\\\\n            result[tier_name][\\\\\\\"min_repo_size\\\\\\\"] = int(min(sizes))\\\\n            result[tier_name][\\\\\\\"max_repo_size\\\\\\\"] = int(max(sizes))\\\\n\\\\n    # Add per-tier BM25 pool size stats (how many BM25 candidates available)\\\\n    for tier_name, (lo, hi) in TIERS.items():\\\\n        tier_records = [r for r in records if lo <= r[\\\\\\\"repo_size\\\\\\\"] < hi]\\\\n        pools = [r[\\\\\\\"bm25_pool_size\\\\\\\"] for r in tier_records]\\\\n        if pools:\\\\n            result[tier_name][\\\\\\\"avg_bm25_pool_size\\\\\\\"] = round(float(np.mean(pools)), 1)\\\\n\\\\n    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)\\\\n    with open(OUT_PATH, \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(result, f, indent=2, ensure_ascii=False)\\\\n\\\\n    print(json.dumps(result, indent=2, ensure_ascii=False))\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"# Stratified BM25 overlap analysis: compares BM25 top-k negatives against\\n# other mining strategies (random, embedding_distance, dataflow_aware),\\n# stratified by repo size (unique file count).\\n#\\n# Input:  /root/autodl-tmp/structfuse/full_m2_training_data/train_{strategy}_s42.jsonl\\n# Output: /root/autodl-tmp/structfuse/artifacts/bm25_overlap_stratified.json\\n\\nimport json\\nimport os\\nfrom collections import defaultdict\\n\\nimport numpy as np\\n\\nDATA_DIR = \\\"/root/autodl-tmp/structfuse/full_m2_training_data\\\"\\nOUT_PATH = \\\"/root/autodl-tmp/structfuse/artifacts/bm25_overlap_stratified.json\\\"\\nSTRATEGIES = [\\\"random\\\", \\\"embedding_distance\\\", \\\"dataflow_aware\\\"]\\nSEED = 42\\nK = 7\\nTIERS = {\\n    \\\"small_lt50\\\": (0, 50),\\n    \\\"medium_50_200\\\": (50, 201),\\n    \\\"large_200plus\\\": (201, float(\\\"inf\\\")),\\n}\\n\\n\\ndef extract_repo(query_id: str) -> str:\\n    iid = query_id.split(\\\"::\\\")[0]\\n    return iid.split(\\\".\\\")[0]\\n\\n\\ndef extract_filepath(full_id: str) -> str:\\n    return full_id.split(\\\"::\\\", 1)[1]\\n\\n\\ndef jaccard(a: set, b: set) -> float:\\n    if not a and not b:\\n        return 1.0\\n    union = a | b\\n    if not union:\\n        return 0.0\\n    return len(a & b) / len(union)\\n\\n\\ndef load_strategy(name: str) -> dict:\\n    path = os.path.join(DATA_DIR, f\\\"train_{name}_s{SEED}.jsonl\\\")\\n    data = {}\\n    with open(path) as f:\\n        for line in f:\\n            d = json.loads(line)\\n            data[d[\\\"query_id\\\"]] = d[\\\"neg_candidates\\\"]\\n    return data\\n\\n\\ndef main():\\n    # 1. Load all strategies\\n    bm25_data = load_strategy(\\\"bm25\\\")\\n    other_data = {s: load_strategy(s) for s in STRATEGIES}\\n\\n    # 2. Build repo file count (union of all file paths across all strategies)\\n    repo_files = defaultdict(set)\\n    for qid, negs in bm25_data.items():\\n        repo = extract_repo(qid)\\n        repo_files[repo].add(extract_filepath(qid))\\n        for nc in negs:\\n            repo_files[repo].add(extract_filepath(nc))\\n    for strat in STRATEGIES:\\n        for qid, negs in other_data[strat].items():\\n            repo = extract_repo(qid)\\n            repo_files[repo].add(extract_filepath(qid))\\n            for nc in negs:\\n                repo_files[repo].add(extract_filepath(nc))\\n\\n    repo_size = {repo: len(files) for repo, files in repo_files.items()}\\n\\n    # 3. Compute per-query overlaps (only for queries present in both BM25 and other)\\n    records = []  # list of dicts with overlap info per query\\n    for qid, bm25_negs in bm25_data.items():\\n        repo = extract_repo(qid)\\n        rsize = repo_size.get(repo, 0)\\n        bm25_topk = set(bm25_negs[:K])\\n\\n        row = {\\n            \\\"query_id\\\": qid,\\n            \\\"repo\\\": repo,\\n            \\\"repo_size\\\": rsize,\\n            \\\"bm25_pool_size\\\": len(bm25_negs),\\n        }\\n        for strat in STRATEGIES:\\n            if qid in other_data[strat]:\\n                other_topk = set(other_data[strat][qid][:K])\\n                row[f\\\"overlap_{strat}\\\"] = jaccard(bm25_topk, other_topk)\\n            else:\\n                row[f\\\"overlap_{strat}\\\"] = None\\n        records.append(row)\\n\\n    # 4. Stratify and compute stats\\n    def compute_tier_stats(tier_records):\\n        repos_in_tier = set(r[\\\"repo\\\"] for r in tier_records)\\n        stats = {\\n            \\\"repo_count\\\": len(repos_in_tier),\\n            \\\"instance_count\\\": len(tier_records),\\n        }\\n        for strat in STRATEGIES:\\n            key = f\\\"overlap_{strat}\\\"\\n            vals = [r[key] for r in tier_records if r[key] is not None]\\n            if vals:\\n                arr = np.array(vals)\\n                stats[f\\\"avg_overlap_bm25_{strat.replace('embedding_distance','embedding')}\\\"] = round(float(arr.mean()), 4)\\n                stats[f\\\"median_overlap_bm25_{strat.replace('embedding_distance','embedding')}\\\"] = round(float(np.median(arr)), 4)\\n                stats[f\\\"matched_queries_{strat.replace('embedding_distance','embedding')}\\\"] = len(vals)\\n            else:\\n                stats[f\\\"avg_overlap_bm25_{strat.replace('embedding_distance','embedding')}\\\"] = None\\n                stats[f\\\"median_overlap_bm25_{strat.replace('embedding_distance','embedding')}\\\"] = None\\n                stats[f\\\"matched_queries_{strat.replace('embedding_distance','embedding')}\\\"] = 0\\n        return stats\\n\\n    result = {\\n        \\\"overall\\\": compute_tier_stats(records),\\n        \\\"seed\\\": f\\\"s{SEED} only\\\",\\n        \\\"k\\\": K,\\n        \\\"repo_size_method\\\": \\\"union of unique file paths across all strategies\\\",\\n    }\\n\\n    for tier_name, (lo, hi) in TIERS.items():\\n        tier_records = [r for r in records if lo <= r[\\\"repo_size\\\"] < hi]\\n        result[tier_name] = compute_tier_stats(tier_records)\\n        # Add repo size stats for this tier\\n        sizes = [r[\\\"repo_size\\\"] for r in tier_records]\\n        if sizes:\\n            result[tier_name][\\\"avg_repo_size\\\"] = round(float(np.mean(sizes)), 1)\\n            result[tier_name][\\\"min_repo_size\\\"] = int(min(sizes))\\n            result[tier_name][\\\"max_repo_size\\\"] = int(max(sizes))\\n\\n    # Add per-tier BM25 pool size stats (how many BM25 candidates available)\\n    for tier_name, (lo, hi) in TIERS.items():\\n        tier_records = [r for r in records if lo <= r[\\\"repo_size\\\"] < hi]\\n        pools = [r[\\\"bm25_pool_size\\\"] for r in tier_records]\\n        if pools:\\n            result[tier_name][\\\"avg_bm25_pool_size\\\"] = round(float(np.mean(pools)), 1)\\n\\n    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)\\n    with open(OUT_PATH, \\\"w\\\") as f:\\n        json.dump(result, f, indent=2, ensure_ascii=False)\\n\\n    print(json.dumps(result, indent=2, ensure_ascii=False))\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 30_

<details><summary>Logged reasoning block</summary>

```text
Now I have a good understanding of the script. Let me analyze `analyze_stratified.py`:

The output was truncated. Let me get the full file to understand all implemented dimensions. But from what I can see:

**Implemented dimensions:**
1. **Repo size** (repo_size_bin) - via REPO_SIZE_BINS
2. **Pool size** (pool_size_bin) - via POOL_SIZE_BINS  
3. **Query-positive similarity** (sim_bin) - via SIMILARITY_BINS

**Missing dimensions (from the 5 required):**


4. **Structural data availability** - dataflow vs fallback
5. **neg_difficulty quartile** - by negative difficulty margin

The script has three evaluation modes: dry-run for testing, loading pre-computed predictions, or re-evaluating from checkpoints with GPU. I need to examine the full script and the validation data structure to see what's actually available.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "a62d2664-50cf-467d-bbc4-393d90261340",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017BkjGc74Pv4teC8KCrsZEr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5786,
      "cache_read_input_tokens": 27164,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5786
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

_source line 31_

脚本被截断了，需要看完整内容。让我读取中间部分和关键函数。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "37b6928a-9a26-4331-b5f0-cc10d39cb454",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017BkjGc74Pv4teC8KCrsZEr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5786,
      "cache_read_input_tokens": 27164,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5786
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01DjVPdEQwhvP5DQzXRh6ktF`</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "wc -l /root/structfuse/evaluation/analyze_stratified.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "3359efa4-1090-4d22-9af1-75ced813def2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017BkjGc74Pv4teC8KCrsZEr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5786,
      "cache_read_input_tokens": 27164,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5786
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Aix12sBrcNQy8iLqjK72Bm`</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "head -250 /root/structfuse/evaluation/analyze_stratified.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "c37bf3dd-b153-48c1-a2d0-62df022a8a92",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017BkjGc74Pv4teC8KCrsZEr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5786,
      "cache_read_input_tokens": 27164,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5786
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

_source line 34 · 2026-05-14T20:15:31.941Z_

<details><summary>↩ Tool result · `toolu_01DjVPdEQwhvP5DQzXRh6ktF`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"781 /root/structfuse/evaluation/analyze_stratified.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "fa02daee-b714-4746-82a5-c9bd8d023d77",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"781 /root/structfuse/evaluation/analyze_stratified.py\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"781 /root/structfuse/evaluation/analyze_stratified.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 35 · 2026-05-14T20:15:32.365Z_

<details><summary>↩ Tool result · `toolu_01Aix12sBrcNQy8iLqjK72Bm`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Stratified analysis of embedding vs random negative strategies by data strata.\\n\\nAnalyses M2 per-instance predictions across:\\n  - Repo size (instance count per repo from M1)\\n  - Candidate pool size (neg_candidates per query)\\n  - Query-positive similarity (cosine sim from model, or text overlap for dry-run)\\n\\nInputs:\\n  - M2 per-instance predictions (from --predictions-dir or re-eval from checkpoints)\\n  - M1 all.jsonl (repo metadata)\\n  - Val JSONL files (query/candidate structure)\\n\\nOutputs:\\n  - stratified_results.json: full per-stratum metrics with bootstrap CI\\n  - stratified_summary.csv: compact table\\n  - stratified_plots.pdf: grouped bar charts, heatmaps, delta trends\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport csv\\nimport json\\nimport math\\nimport os\\nimport sys\\nfrom collections import Counter, defaultdict\\nfrom pathlib import Path\\nfrom typing import Any, Dict, List, Optional, Tuple\\n\\nimport numpy as np\\n\\nSTRATEGIES = [\\\"random\\\", \\\"embedding_distance\\\", \\\"dataflow_aware\\\"]\\nSTRATEGY_LABELS = {\\\"random\\\": \\\"Random\\\", \\\"embedding_distance\\\": \\\"Embedding\\\", \\\"dataflow_aware\\\": \\\"Dataflow\\\"}\\nSTRATEGY_COLORS = {\\\"random\\\": \\\"#4C72B0\\\", \\\"embedding_distance\\\": \\\"#DD8452\\\", \\\"dataflow_aware\\\": \\\"#55A868\\\"}\\n\\nREPO_SIZE_BINS = {\\n    \\\"small\\\": (0, 50),\\n    \\\"medium\\\": (50, 200),\\n    \\\"large\\\": (200, 500),\\n    \\\"xlarge\\\": (500, float(\\\"inf\\\")),\\n}\\n\\nPOOL_SIZE_BINS = {\\n    \\\"small\\\": (0, 20),\\n    \\\"medium\\\": (20, 40),\\n    \\\"large\\\": (40, 51),\\n}\\n\\nSIMILARITY_BINS = {\\n    \\\"low\\\": (0.0, 0.3),\\n    \\\"medium\\\": (0.3, 0.6),\\n    \\\"high\\\": (0.6, 1.01),\\n}\\n\\n\\ndef _bin_value(value, bins):\\n    for name, (lo, hi) in bins.items():\\n        if lo <= value < hi:\\n            return name\\n    return \\\"unknown\\\"\\n\\n\\n# ── M1 metadata ─────────────────────────────────────────────────────\\n\\ndef load_m1_metadata(m1_path: str) -> Tuple[Dict[str, str], Dict[str, int]]:\\n    import re\\n    inst_to_repo = {}\\n    repo_counts: Counter = Counter()\\n    pat_iid = re.compile(r'\\\"instance_id\\\"\\\\s*:\\\\s*\\\"([^\\\"]+)\\\"')\\n    pat_repo = re.compile(r'\\\"repo\\\"\\\\s*:\\\\s*\\\"([^\\\"]+)\\\"')\\n    with open(m1_path) as f:\\n        for line in f:\\n            m_iid = pat_iid.search(line)\\n            m_repo = pat_repo.search(line)\\n            if m_iid and m_repo:\\n                iid = m_iid.group(1)\\n                repo = m_repo.group(1)\\n                inst_to_repo[iid] = repo\\n                repo_counts[repo] += 1\\n    return inst_to_repo, dict(repo_counts)\\n\\n\\n# ── Val data loading ─────────────────────────────────────────────────\\n\\ndef load_val_samples(val_path: str, lite: bool = False) -> List[Dict[str, Any]]:\\n    \\\"\\\"\\\"Load val JSONL. lite=True skips candidate_tokens (faster for dry-run).\\\"\\\"\\\"\\n    import re\\n    samples = []\\n    pat_qid = re.compile(r'\\\"query_id\\\"\\\\s*:\\\\s*\\\"([^\\\"]+)\\\"')\\n    with open(val_path) as f:\\n        for line in f:\\n            if not line.strip():\\n                continue\\n            if lite:\\n                m = pat_qid.search(line)\\n                if not m:\\n                    continue\\n                qid = m.group(1)\\n                instance_id = qid.split(\\\"::\\\")[0] if \\\"::\\\" in qid else qid\\n                d = json.loads(line)\\n                samples.append({\\n                    \\\"query_id\\\": qid,\\n                    \\\"instance_id\\\": instance_id,\\n                    \\\"pool_size\\\": len(d.get(\\\"neg_candidates\\\", [])),\\n                    \\\"query_tokens\\\": d.get(\\\"query_tokens\\\", \\\"\\\")[:1000],\\n                    \\\"pos_tokens\\\": d.get(\\\"pos_tokens\\\", \\\"\\\")[:1000],\\n                    \\\"neg_candidates\\\": [],\\n                    \\\"candidate_tokens\\\": {},\\n                })\\n            else:\\n                d = json.loads(line)\\n                qid = d[\\\"query_id\\\"]\\n                instance_id = qid.split(\\\"::\\\")[0] if \\\"::\\\" in qid else qid\\n                samples.append({\\n                    \\\"query_id\\\": qid,\\n                    \\\"instance_id\\\": instance_id,\\n                    \\\"pool_size\\\": len(d.get(\\\"neg_candidates\\\", [])),\\n                    \\\"query_tokens\\\": d[\\\"query_tokens\\\"],\\n                    \\\"pos_tokens\\\": d[\\\"pos_tokens\\\"],\\n                    \\\"neg_candidates\\\": d.get(\\\"neg_candidates\\\", []),\\n\\n\\n... [截断: 输出过长，省略 536 字符] ...\\n\\nce: str = \\\"cuda\\\",\\n    max_seq_length: int = 2048,\\n) -> List[Dict]:\\n    import torch\\n    from transformers import AutoTokenizer\\n\\n    train_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), \\\"..\\\", \\\"training\\\")\\n    if train_dir not in sys.path:\\n        sys.path.insert(0, train_dir)\\n    from contrastive_model import StructFuseEncoder\\n\\n    config_path = os.path.join(checkpoint_dir, \\\"training_config.json\\\")\\n    with open(config_path) as f:\\n        config = json.load(f)\\n\\n    model_name = config.get(\\\"model_name\\\", \\\"Qwen/Qwen2.5-Coder-3B\\\")\\n    tokenizer = AutoTokenizer.from_pretrained(checkpoint_dir, trust_remote_code=True)\\n\\n    model = StructFuseEncoder(\\n        model_name=model_name,\\n        proj_dim=config.get(\\\"proj_dim\\\", 256),\\n        use_projection=True,\\n        use_lora=config.get(\\\"use_lora\\\", False),\\n        lora_r=config.get(\\\"lora_r\\\", 16),\\n        use_fusion_head=config.get(\\\"use_fusion_head\\\", False),\\n    )\\n    state_dict = torch.load(os.path.join(checkpoint_dir, \\\"model.pt\\\"), map_location=\\\"cpu\\\")\\n    model.load_state_dict(state_dict, strict=False)\\n    model = model.to(device).eval()\\n\\n    results = []\\n    with torch.no_grad():\\n        for i, sample in enumerate(val_samples):\\n            if (i + 1) % 200 == 0:\\n                print(f\\\"  re-eval {i+1}/{len(val_samples)}\\\", flush=True)\\n\\n            def _encode(text):\\n                enc = tokenizer(text, truncation=True, max_length=max_seq_length,\\n                                padding=True, return_tensors=\\\"pt\\\")\\n                enc = {k: v.to(device) for k, v in enc.items()}\\n                return model.encode(enc[\\\"input_ids\\\"], enc[\\\"attention_mask\\\"])\\n\\n            q_emb = _encode(sample[\\\"query_tokens\\\"])\\n            p_emb = _encode(sample[\\\"pos_tokens\\\"])\\n            pos_sim = (q_emb * p_emb).sum().item()\\n\\n            neg_sims = []\\n            for neg_id in sample[\\\"neg_candidates\\\"]:\\n                neg_text = sample[\\\"candidate_tokens\\\"].get(neg_id, \\\"\\\")\\n                if not neg_text:\\n                    continue\\n                n_emb = _encode(neg_text)\\n                neg_sims.append((q_emb * n_emb).sum().item())\\n\\n            rank = 1 + sum(1 for s in neg_sims if s >= pos_sim)\\n\\n            results.append({\\n                \\\"query_id\\\": sample[\\\"query_id\\\"],\\n                \\\"instance_id\\\": sample[\\\"instance_id\\\"],\\n                \\\"pool_size\\\": sample[\\\"pool_size\\\"],\\n                \\\"rank\\\": rank,\\n                \\\"pos_sim\\\": pos_sim,\\n                \\\"total_candidates\\\": 1 + len(neg_sims),\\n            })\\n\\n    del model\\n    if torch.cuda.is_available():\\n        torch.cuda.empty_cache()\\n    return results\\n\\n\\n# ── Predictions loading ──────────────────────────────────────────────\\n\\ndef load_predictions(pred_file: str, val_samples: List[Dict]) -> List[Dict]:\\n    \\\"\\\"\\\"Load predictions from eval_retrieval.py output format.\\\"\\\"\\\"\\n    with open(pred_file) as f:\\n        data = json.load(f)\\n\\n    per_inst = {}\\n    results_list = data.get(\\\"results\\\", [data]) if \\\"results\\\" in data else [data]\\n    for r in results_list:\\n        for pi in r.get(\\\"per_instance\\\", []):\\n            per_inst[pi[\\\"instance_id\\\"]] = pi\\n\\n    val_lookup = {s[\\\"query_id\\\"]: s for s in val_samples}\\n    results = []\\n    for sample in val_samples:\\n        iid = sample[\\\"instance_id\\\"]\\n        pred = per_inst.get(iid)\\n        if pred is None:\\n            continue\\n        gold = set(pred.get(\\\"gold_files\\\", []))\\n        predicted = pred.get(\\\"predicted_top10\\\", [])\\n        rank = len(predicted) + 1\\n        for j, pf in enumerate(predicted):\\n            if pf in gold:\\n                rank = j + 1\\n                break\\n        results.append({\\n            \\\"query_id\\\": sample[\\\"query_id\\\"],\\n            \\\"instance_id\\\": iid,\\n            \\\"pool_size\\\": sample[\\\"pool_size\\\"],\\n            \\\"rank\\\": rank,\\n            \\\"pos_sim\\\": pred.get(\\\"scores_top10\\\", [0.0])[0] if pred.get(\\\"scores_top10\\\") else 0.0,\\n            \\\"total_candidates\\\": max(len(predicted), sample[\\\"pool_size\\\"] + 1),\\n        })\\n    return results\\n\\n\\n# ── Mock predictions (dry-run) ───────────────────────────────────────\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "d09c8b7a-031a-4a88-9696-fbf2e72e5ddf",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\n\\\\\\\"\\\\\\\"\\\\\\\"Stratified analysis of embedding vs random negative strategies by data strata.\\\\n\\\\nAnalyses M2 per-instance predictions across:\\\\n  - Repo size (instance count per repo from M1)\\\\n  - Candidate pool size (neg_candidates per query)\\\\n  - Query-positive similarity (cosine sim from model, or text overlap for dry-run)\\\\n\\\\nInputs:\\\\n  - M2 per-instance predictions (from --predictions-dir or re-eval from checkpoints)\\\\n  - M1 all.jsonl (repo metadata)\\\\n  - Val JSONL files (query/candidate structure)\\\\n\\\\nOutputs:\\\\n  - stratified_results.json: full per-stratum metrics with bootstrap CI\\\\n  - stratified_summary.csv: compact table\\\\n  - stratified_plots.pdf: grouped bar charts, heatmaps, delta trends\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport argparse\\\\nimport csv\\\\nimport json\\\\nimport math\\\\nimport os\\\\nimport sys\\\\nfrom collections import Counter, defaultdict\\\\nfrom pathlib import Path\\\\nfrom typing import Any, Dict, List, Optional, Tuple\\\\n\\\\nimport numpy as np\\\\n\\\\nSTRATEGIES = [\\\\\\\"random\\\\\\\", \\\\\\\"embedding_distance\\\\\\\", \\\\\\\"dataflow_aware\\\\\\\"]\\\\nSTRATEGY_LABELS = {\\\\\\\"random\\\\\\\": \\\\\\\"Random\\\\\\\", \\\\\\\"embedding_distance\\\\\\\": \\\\\\\"Embedding\\\\\\\", \\\\\\\"dataflow_aware\\\\\\\": \\\\\\\"Dataflow\\\\\\\"}\\\\nSTRATEGY_COLORS = {\\\\\\\"random\\\\\\\": \\\\\\\"#4C72B0\\\\\\\", \\\\\\\"embedding_distance\\\\\\\": \\\\\\\"#DD8452\\\\\\\", \\\\\\\"dataflow_aware\\\\\\\": \\\\\\\"#55A868\\\\\\\"}\\\\n\\\\nREPO_SIZE_BINS = {\\\\n    \\\\\\\"small\\\\\\\": (0, 50),\\\\n    \\\\\\\"medium\\\\\\\": (50, 200),\\\\n    \\\\\\\"large\\\\\\\": (200, 500),\\\\n    \\\\\\\"xlarge\\\\\\\": (500, float(\\\\\\\"inf\\\\\\\")),\\\\n}\\\\n\\\\nPOOL_SIZE_BINS = {\\\\n    \\\\\\\"small\\\\\\\": (0, 20),\\\\n    \\\\\\\"medium\\\\\\\": (20, 40),\\\\n    \\\\\\\"large\\\\\\\": (40, 51),\\\\n}\\\\n\\\\nSIMILARITY_BINS = {\\\\n    \\\\\\\"low\\\\\\\": (0.0, 0.3),\\\\n    \\\\\\\"medium\\\\\\\": (0.3, 0.6),\\\\n    \\\\\\\"high\\\\\\\": (0.6, 1.01),\\\\n}\\\\n\\\\n\\\\ndef _bin_value(value, bins):\\\\n    for name, (lo, hi) in bins.items():\\\\n        if lo <= value < hi:\\\\n            return name\\\\n    return \\\\\\\"unknown\\\\\\\"\\\\n\\\\n\\\\n# ── M1 metadata ─────────────────────────────────────────────────────\\\\n\\\\ndef load_m1_metadata(m1_path: str) -> Tuple[Dict[str, str], Dict[str, int]]:\\\\n    import re\\\\n    inst_to_repo = {}\\\\n    repo_counts: Counter = Counter()\\\\n    pat_iid = re.compile(r'\\\\\\\"instance_id\\\\\\\"\\\\\\\\s*:\\\\\\\\s*\\\\\\\"([^\\\\\\\"]+)\\\\\\\"')\\\\n    pat_repo = re.compile(r'\\\\\\\"repo\\\\\\\"\\\\\\\\s*:\\\\\\\\s*\\\\\\\"([^\\\\\\\"]+)\\\\\\\"')\\\\n    with open(m1_path) as f:\\\\n        for line in f:\\\\n            m_iid = pat_iid.search(line)\\\\n            m_repo = pat_repo.search(line)\\\\n            if m_iid and m_repo:\\\\n                iid = m_iid.group(1)\\\\n                repo = m_repo.group(1)\\\\n                inst_to_repo[iid] = repo\\\\n                repo_counts[repo] += 1\\\\n    return inst_to_repo, dict(repo_counts)\\\\n\\\\n\\\\n# ── Val data loading ─────────────────────────────────────────────────\\\\n\\\\ndef load_val_samples(val_path: str, lite: bool = False) -> List[Dict[str, Any]]:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Load val JSONL. lite=True skips candidate_tokens (faster for dry-run).\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    import re\\\\n    samples = []\\\\n    pat_qid = re.compile(r'\\\\\\\"query_id\\\\\\\"\\\\\\\\s*:\\\\\\\\s*\\\\\\\"([^\\\\\\\"]+)\\\\\\\"')\\\\n    with open(val_path) as f:\\\\n        for line in f:\\\\n            if not line.strip():\\\\n                continue\\\\n            if lite:\\\\n                m = pat_qid.search(line)\\\\n                if not m:\\\\n                    continue\\\\n                qid = m.group(1)\\\\n                instance_id = qid.split(\\\\\\\"::\\\\\\\")[0] if \\\\\\\"::\\\\\\\" in qid else qid\\\\n                d = json.loads(line)\\\\n                samples.append({\\\\n                    \\\\\\\"query_id\\\\\\\": qid,\\\\n                    \\\\\\\"instance_id\\\\\\\": instance_id,\\\\n                    \\\\\\\"pool_size\\\\\\\": len(d.get(\\\\\\\"neg_candidates\\\\\\\", [])),\\\\n                    \\\\\\\"query_tokens\\\\\\\": d.get(\\\\\\\"query_tokens\\\\\\\", \\\\\\\"\\\\\\\")[:1000],\\\\n                    \\\\\\\"pos_tokens\\\\\\\": d.get(\\\\\\\"pos_tokens\\\\\\\", \\\\\\\"\\\\\\\")[:1000],\\\\n                    \\\\\\\"neg_candidates\\\\\\\": [],\\\\n                    \\\\\\\"candidate_tokens\\\\\\\": {},\\\\n                })\\\\n            else:\\\\n                d = json.loads(line)\\\\n                qid = d[\\\\\\\"query_id\\\\\\\"]\\\\n                instance_id = qid.split(\\\\\\\"::\\\\\\\")[0] if \\\\\\\"::\\\\\\\" in qid else qid\\\\n                samples.append({\\\\n                    \\\\\\\"query_id\\\\\\\": qid,\\\\n                    \\\\\\\"instance_id\\\\\\\": instance_id,\\\\n                    \\\\\\\"pool_size\\\\\\\": len(d.get(\\\\\\\"neg_candidates\\\\\\\", [])),\\\\n                    \\\\\\\"query_tokens\\\\\\\": d[\\\\\\\"query_tokens\\\\\\\"],\\\\n                    \\\\\\\"pos_tokens\\\\\\\": d[\\\\\\\"pos_tokens\\\\\\\"],\\\\n                    \\\\\\\"neg_candidates\\\\\\\": d.get(\\\\\\\"neg_candidates\\\\\\\", []),\\\\n\\\\n\\\\n... [截断: 输出过长，省略 536 字符] ...\\\\n\\\\nce: str = \\\\\\\"cuda\\\\\\\",\\\\n    max_seq_length: int = 2048,\\\\n) -> List[Dict]:\\\\n    import torch\\\\n    from transformers import AutoTokenizer\\\\n\\\\n    train_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), \\\\\\\"..\\\\\\\", \\\\\\\"training\\\\\\\")\\\\n    if train_dir not in sys.path:\\\\n        sys.path.insert(0, train_dir)\\\\n    from contrastive_model import StructFuseEncoder\\\\n\\\\n    config_path = os.path.join(checkpoint_dir, \\\\\\\"training_config.json\\\\\\\")\\\\n    with open(config_path) as f:\\\\n        config = json.load(f)\\\\n\\\\n    model_name = config.get(\\\\\\\"model_name\\\\\\\", \\\\\\\"Qwen/Qwen2.5-Coder-3B\\\\\\\")\\\\n    tokenizer = AutoTokenizer.from_pretrained(checkpoint_dir, trust_remote_code=True)\\\\n\\\\n    model = StructFuseEncoder(\\\\n        model_name=model_name,\\\\n        proj_dim=config.get(\\\\\\\"proj_dim\\\\\\\", 256),\\\\n        use_projection=True,\\\\n        use_lora=config.get(\\\\\\\"use_lora\\\\\\\", False),\\\\n        lora_r=config.get(\\\\\\\"lora_r\\\\\\\", 16),\\\\n        use_fusion_head=config.get(\\\\\\\"use_fusion_head\\\\\\\", False),\\\\n    )\\\\n    state_dict = torch.load(os.path.join(checkpoint_dir, \\\\\\\"model.pt\\\\\\\"), map_location=\\\\\\\"cpu\\\\\\\")\\\\n    model.load_state_dict(state_dict, strict=False)\\\\n    model = model.to(device).eval()\\\\n\\\\n    results = []\\\\n    with torch.no_grad():\\\\n        for i, sample in enumerate(val_samples):\\\\n            if (i + 1) % 200 == 0:\\\\n                print(f\\\\\\\"  re-eval {i+1}/{len(val_samples)}\\\\\\\", flush=True)\\\\n\\\\n            def _encode(text):\\\\n                enc = tokenizer(text, truncation=True, max_length=max_seq_length,\\\\n                                padding=True, return_tensors=\\\\\\\"pt\\\\\\\")\\\\n                enc = {k: v.to(device) for k, v in enc.items()}\\\\n                return model.encode(enc[\\\\\\\"input_ids\\\\\\\"], enc[\\\\\\\"attention_mask\\\\\\\"])\\\\n\\\\n            q_emb = _encode(sample[\\\\\\\"query_tokens\\\\\\\"])\\\\n            p_emb = _encode(sample[\\\\\\\"pos_tokens\\\\\\\"])\\\\n            pos_sim = (q_emb * p_emb).sum().item()\\\\n\\\\n            neg_sims = []\\\\n            for neg_id in sample[\\\\\\\"neg_candidates\\\\\\\"]:\\\\n                neg_text = sample[\\\\\\\"candidate_tokens\\\\\\\"].get(neg_id, \\\\\\\"\\\\\\\")\\\\n                if not neg_text:\\\\n                    continue\\\\n                n_emb = _encode(neg_text)\\\\n                neg_sims.append((q_emb * n_emb).sum().item())\\\\n\\\\n            rank = 1 + sum(1 for s in neg_sims if s >= pos_sim)\\\\n\\\\n            results.append({\\\\n                \\\\\\\"query_id\\\\\\\": sample[\\\\\\\"query_id\\\\\\\"],\\\\n                \\\\\\\"instance_id\\\\\\\": sample[\\\\\\\"instance_id\\\\\\\"],\\\\n                \\\\\\\"pool_size\\\\\\\": sample[\\\\\\\"pool_size\\\\\\\"],\\\\n                \\\\\\\"rank\\\\\\\": rank,\\\\n                \\\\\\\"pos_sim\\\\\\\": pos_sim,\\\\n                \\\\\\\"total_candidates\\\\\\\": 1 + len(neg_sims),\\\\n            })\\\\n\\\\n    del model\\\\n    if torch.cuda.is_available():\\\\n        torch.cuda.empty_cache()\\\\n    return results\\\\n\\\\n\\\\n# ── Predictions loading ──────────────────────────────────────────────\\\\n\\\\ndef load_predictions(pred_file: str, val_samples: List[Dict]) -> List[Dict]:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Load predictions from eval_retrieval.py output format.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    with open(pred_file) as f:\\\\n        data = json.load(f)\\\\n\\\\n    per_inst = {}\\\\n    results_list = data.get(\\\\\\\"results\\\\\\\", [data]) if \\\\\\\"results\\\\\\\" in data else [data]\\\\n    for r in results_list:\\\\n        for pi in r.get(\\\\\\\"per_instance\\\\\\\", []):\\\\n            per_inst[pi[\\\\\\\"instance_id\\\\\\\"]] = pi\\\\n\\\\n    val_lookup = {s[\\\\\\\"query_id\\\\\\\"]: s for s in val_samples}\\\\n    results = []\\\\n    for sample in val_samples:\\\\n        iid = sample[\\\\\\\"instance_id\\\\\\\"]\\\\n        pred = per_inst.get(iid)\\\\n        if pred is None:\\\\n            continue\\\\n        gold = set(pred.get(\\\\\\\"gold_files\\\\\\\", []))\\\\n        predicted = pred.get(\\\\\\\"predicted_top10\\\\\\\", [])\\\\n        rank = len(predicted) + 1\\\\n        for j, pf in enumerate(predicted):\\\\n            if pf in gold:\\\\n                rank = j + 1\\\\n                break\\\\n        results.append({\\\\n            \\\\\\\"query_id\\\\\\\": sample[\\\\\\\"query_id\\\\\\\"],\\\\n            \\\\\\\"instance_id\\\\\\\": iid,\\\\n            \\\\\\\"pool_size\\\\\\\": sample[\\\\\\\"pool_size\\\\\\\"],\\\\n            \\\\\\\"rank\\\\\\\": rank,\\\\n            \\\\\\\"pos_sim\\\\\\\": pred.get(\\\\\\\"scores_top10\\\\\\\", [0.0])[0] if pred.get(\\\\\\\"scores_top10\\\\\\\") else 0.0,\\\\n            \\\\\\\"total_candidates\\\\\\\": max(len(predicted), sample[\\\\\\\"pool_size\\\\\\\"] + 1),\\\\n        })\\\\n    return results\\\\n\\\\n\\\\n# ── Mock predictions (dry-run) ───────────────────────────────────────\\\\n\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.41}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Stratified analysis of embedding vs random negative strategies by data strata.\\n\\nAnalyses M2 per-instance predictions across:\\n  - Repo size (instance count per repo from M1)\\n  - Candidate pool size (neg_candidates per query)\\n  - Query-positive similarity (cosine sim from model, or text overlap for dry-run)\\n\\nInputs:\\n  - M2 per-instance predictions (from --predictions-dir or re-eval from checkpoints)\\n  - M1 all.jsonl (repo metadata)\\n  - Val JSONL files (query/candidate structure)\\n\\nOutputs:\\n  - stratified_results.json: full per-stratum metrics with bootstrap CI\\n  - stratified_summary.csv: compact table\\n  - stratified_plots.pdf: grouped bar charts, heatmaps, delta trends\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport csv\\nimport json\\nimport math\\nimport os\\nimport sys\\nfrom collections import Counter, defaultdict\\nfrom pathlib import Path\\nfrom typing import Any, Dict, List, Optional, Tuple\\n\\nimport numpy as np\\n\\nSTRATEGIES = [\\\"random\\\", \\\"embedding_distance\\\", \\\"dataflow_aware\\\"]\\nSTRATEGY_LABELS = {\\\"random\\\": \\\"Random\\\", \\\"embedding_distance\\\": \\\"Embedding\\\", \\\"dataflow_aware\\\": \\\"Dataflow\\\"}\\nSTRATEGY_COLORS = {\\\"random\\\": \\\"#4C72B0\\\", \\\"embedding_distance\\\": \\\"#DD8452\\\", \\\"dataflow_aware\\\": \\\"#55A868\\\"}\\n\\nREPO_SIZE_BINS = {\\n    \\\"small\\\": (0, 50),\\n    \\\"medium\\\": (50, 200),\\n    \\\"large\\\": (200, 500),\\n    \\\"xlarge\\\": (500, float(\\\"inf\\\")),\\n}\\n\\nPOOL_SIZE_BINS = {\\n    \\\"small\\\": (0, 20),\\n    \\\"medium\\\": (20, 40),\\n    \\\"large\\\": (40, 51),\\n}\\n\\nSIMILARITY_BINS = {\\n    \\\"low\\\": (0.0, 0.3),\\n    \\\"medium\\\": (0.3, 0.6),\\n    \\\"high\\\": (0.6, 1.01),\\n}\\n\\n\\ndef _bin_value(value, bins):\\n    for name, (lo, hi) in bins.items():\\n        if lo <= value < hi:\\n            return name\\n    return \\\"unknown\\\"\\n\\n\\n# ── M1 metadata ─────────────────────────────────────────────────────\\n\\ndef load_m1_metadata(m1_path: str) -> Tuple[Dict[str, str], Dict[str, int]]:\\n    import re\\n    inst_to_repo = {}\\n    repo_counts: Counter = Counter()\\n    pat_iid = re.compile(r'\\\"instance_id\\\"\\\\s*:\\\\s*\\\"([^\\\"]+)\\\"')\\n    pat_repo = re.compile(r'\\\"repo\\\"\\\\s*:\\\\s*\\\"([^\\\"]+)\\\"')\\n    with open(m1_path) as f:\\n        for line in f:\\n            m_iid = pat_iid.search(line)\\n            m_repo = pat_repo.search(line)\\n            if m_iid and m_repo:\\n                iid = m_iid.group(1)\\n                repo = m_repo.group(1)\\n                inst_to_repo[iid] = repo\\n                repo_counts[repo] += 1\\n    return inst_to_repo, dict(repo_counts)\\n\\n\\n# ── Val data loading ─────────────────────────────────────────────────\\n\\ndef load_val_samples(val_path: str, lite: bool = False) -> List[Dict[str, Any]]:\\n    \\\"\\\"\\\"Load val JSONL. lite=True skips candidate_tokens (faster for dry-run).\\\"\\\"\\\"\\n    import re\\n    samples = []\\n    pat_qid = re.compile(r'\\\"query_id\\\"\\\\s*:\\\\s*\\\"([^\\\"]+)\\\"')\\n    with open(val_path) as f:\\n        for line in f:\\n            if not line.strip():\\n                continue\\n            if lite:\\n                m = pat_qid.search(line)\\n                if not m:\\n                    continue\\n                qid = m.group(1)\\n                instance_id = qid.split(\\\"::\\\")[0] if \\\"::\\\" in qid else qid\\n                d = json.loads(line)\\n                samples.append({\\n                    \\\"query_id\\\": qid,\\n                    \\\"instance_id\\\": instance_id,\\n                    \\\"pool_size\\\": len(d.get(\\\"neg_candidates\\\", [])),\\n                    \\\"query_tokens\\\": d.get(\\\"query_tokens\\\", \\\"\\\")[:1000],\\n                    \\\"pos_tokens\\\": d.get(\\\"pos_tokens\\\", \\\"\\\")[:1000],\\n                    \\\"neg_candidates\\\": [],\\n                    \\\"candidate_tokens\\\": {},\\n                })\\n            else:\\n                d = json.loads(line)\\n                qid = d[\\\"query_id\\\"]\\n                instance_id = qid.split(\\\"::\\\")[0] if \\\"::\\\" in qid else qid\\n                samples.append({\\n                    \\\"query_id\\\": qid,\\n                    \\\"instance_id\\\": instance_id,\\n                    \\\"pool_size\\\": len(d.get(\\\"neg_candidates\\\", [])),\\n                    \\\"query_tokens\\\": d[\\\"query_tokens\\\"],\\n                    \\\"pos_tokens\\\": d[\\\"pos_tokens\\\"],\\n                    \\\"neg_candidates\\\": d.get(\\\"neg_candidates\\\", []),\\n\\n\\n... [截断: 输出过长，省略 536 字符] ...\\n\\nce: str = \\\"cuda\\\",\\n    max_seq_length: int = 2048,\\n) -> List[Dict]:\\n    import torch\\n    from transformers import AutoTokenizer\\n\\n    train_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), \\\"..\\\", \\\"training\\\")\\n    if train_dir not in sys.path:\\n        sys.path.insert(0, train_dir)\\n    from contrastive_model import StructFuseEncoder\\n\\n    config_path = os.path.join(checkpoint_dir, \\\"training_config.json\\\")\\n    with open(config_path) as f:\\n        config = json.load(f)\\n\\n    model_name = config.get(\\\"model_name\\\", \\\"Qwen/Qwen2.5-Coder-3B\\\")\\n    tokenizer = AutoTokenizer.from_pretrained(checkpoint_dir, trust_remote_code=True)\\n\\n    model = StructFuseEncoder(\\n        model_name=model_name,\\n        proj_dim=config.get(\\\"proj_dim\\\", 256),\\n        use_projection=True,\\n        use_lora=config.get(\\\"use_lora\\\", False),\\n        lora_r=config.get(\\\"lora_r\\\", 16),\\n        use_fusion_head=config.get(\\\"use_fusion_head\\\", False),\\n    )\\n    state_dict = torch.load(os.path.join(checkpoint_dir, \\\"model.pt\\\"), map_location=\\\"cpu\\\")\\n    model.load_state_dict(state_dict, strict=False)\\n    model = model.to(device).eval()\\n\\n    results = []\\n    with torch.no_grad():\\n        for i, sample in enumerate(val_samples):\\n            if (i + 1) % 200 == 0:\\n                print(f\\\"  re-eval {i+1}/{len(val_samples)}\\\", flush=True)\\n\\n            def _encode(text):\\n                enc = tokenizer(text, truncation=True, max_length=max_seq_length,\\n                                padding=True, return_tensors=\\\"pt\\\")\\n                enc = {k: v.to(device) for k, v in enc.items()}\\n                return model.encode(enc[\\\"input_ids\\\"], enc[\\\"attention_mask\\\"])\\n\\n            q_emb = _encode(sample[\\\"query_tokens\\\"])\\n            p_emb = _encode(sample[\\\"pos_tokens\\\"])\\n            pos_sim = (q_emb * p_emb).sum().item()\\n\\n            neg_sims = []\\n            for neg_id in sample[\\\"neg_candidates\\\"]:\\n                neg_text = sample[\\\"candidate_tokens\\\"].get(neg_id, \\\"\\\")\\n                if not neg_text:\\n                    continue\\n                n_emb = _encode(neg_text)\\n                neg_sims.append((q_emb * n_emb).sum().item())\\n\\n            rank = 1 + sum(1 for s in neg_sims if s >= pos_sim)\\n\\n            results.append({\\n                \\\"query_id\\\": sample[\\\"query_id\\\"],\\n                \\\"instance_id\\\": sample[\\\"instance_id\\\"],\\n                \\\"pool_size\\\": sample[\\\"pool_size\\\"],\\n                \\\"rank\\\": rank,\\n                \\\"pos_sim\\\": pos_sim,\\n                \\\"total_candidates\\\": 1 + len(neg_sims),\\n            })\\n\\n    del model\\n    if torch.cuda.is_available():\\n        torch.cuda.empty_cache()\\n    return results\\n\\n\\n# ── Predictions loading ──────────────────────────────────────────────\\n\\ndef load_predictions(pred_file: str, val_samples: List[Dict]) -> List[Dict]:\\n    \\\"\\\"\\\"Load predictions from eval_retrieval.py output format.\\\"\\\"\\\"\\n    with open(pred_file) as f:\\n        data = json.load(f)\\n\\n    per_inst = {}\\n    results_list = data.get(\\\"results\\\", [data]) if \\\"results\\\" in data else [data]\\n    for r in results_list:\\n        for pi in r.get(\\\"per_instance\\\", []):\\n            per_inst[pi[\\\"instance_id\\\"]] = pi\\n\\n    val_lookup = {s[\\\"query_id\\\"]: s for s in val_samples}\\n    results = []\\n    for sample in val_samples:\\n        iid = sample[\\\"instance_id\\\"]\\n        pred = per_inst.get(iid)\\n        if pred is None:\\n            continue\\n        gold = set(pred.get(\\\"gold_files\\\", []))\\n        predicted = pred.get(\\\"predicted_top10\\\", [])\\n        rank = len(predicted) + 1\\n        for j, pf in enumerate(predicted):\\n            if pf in gold:\\n                rank = j + 1\\n                break\\n        results.append({\\n            \\\"query_id\\\": sample[\\\"query_id\\\"],\\n            \\\"instance_id\\\": iid,\\n            \\\"pool_size\\\": sample[\\\"pool_size\\\"],\\n            \\\"rank\\\": rank,\\n            \\\"pos_sim\\\": pred.get(\\\"scores_top10\\\", [0.0])[0] if pred.get(\\\"scores_top10\\\") else 0.0,\\n            \\\"total_candidates\\\": max(len(predicted), sample[\\\"pool_size\\\"] + 1),\\n        })\\n    return results\\n\\n\\n# ── Mock predictions (dry-run) ───────────────────────────────────────\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 36_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_019MV3CVjAAngGbNChxqaXYw`</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "tail -n +250 /root/structfuse/evaluation/analyze_stratified.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "1d23c8a4-99f0-4618-b363-3aa7388fc310",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gx8DvTBnHJHaho4pzZcATu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4072,
      "cache_read_input_tokens": 32950,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4072
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

_source line 37 · 2026-05-14T20:15:35.488Z_

<details><summary>↩ Tool result · `toolu_019MV3CVjAAngGbNChxqaXYw`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\ndef mock_predictions(\\n    val_samples: List[Dict], strategy: str, seed: int\\n) -> List[Dict]:\\n    rng = np.random.RandomState(seed + abs(hash(strategy)) % 10000)\\n    results = []\\n    for sample in val_samples:\\n        pool = 1 + sample[\\\"pool_size\\\"]\\n        if strategy == \\\"random\\\":\\n            rank = rng.randint(1, pool + 1)\\n        elif strategy == \\\"embedding_distance\\\":\\n            rank = max(1, min(pool, int(rng.exponential(pool * 0.35)) + 1))\\n        else:\\n            rank = max(1, min(pool, int(rng.exponential(pool * 0.20)) + 1))\\n\\n        pos_sim = max(0.0, min(1.0, 1.0 - rank / pool + rng.normal(0, 0.08)))\\n        tsim = text_similarity(\\n            sample[\\\"query_tokens\\\"][:500], sample[\\\"pos_tokens\\\"][:500]\\n        )\\n\\n        results.append({\\n            \\\"query_id\\\": sample[\\\"query_id\\\"],\\n            \\\"instance_id\\\": sample[\\\"instance_id\\\"],\\n            \\\"pool_size\\\": sample[\\\"pool_size\\\"],\\n            \\\"rank\\\": rank,\\n            \\\"pos_sim\\\": pos_sim if pos_sim > 0 else tsim,\\n            \\\"total_candidates\\\": pool,\\n        })\\n    return results\\n\\n\\n# ── Metrics computation ──────────────────────────────────────────────\\n\\ndef compute_metrics(results: List[Dict]) -> Dict[str, float]:\\n    if not results:\\n        return {\\\"R@1\\\": 0.0, \\\"R@5\\\": 0.0, \\\"MRR\\\": 0.0, \\\"count\\\": 0}\\n    ranks = [r[\\\"rank\\\"] for r in results]\\n    n = len(ranks)\\n    return {\\n        \\\"R@1\\\": sum(1 for r in ranks if r <= 1) / n,\\n        \\\"R@5\\\": sum(1 for r in ranks if r <= 5) / n,\\n        \\\"MRR\\\": sum(1.0 / r for r in ranks) / n,\\n        \\\"count\\\": n,\\n    }\\n\\n\\ndef _metric_fn(results, metric_name):\\n    m = compute_metrics(results)\\n    return m[metric_name]\\n\\n\\ndef bootstrap_ci(\\n    results: List[Dict],\\n    metric_name: str = \\\"R@1\\\",\\n    n_bootstrap: int = 1000,\\n    ci: float = 0.95,\\n    seed: int = 42,\\n) -> Tuple[float, float, float]:\\n    rng = np.random.RandomState(seed)\\n    n = len(results)\\n    if n == 0:\\n        return (0.0, 0.0, 0.0)\\n\\n    point = _metric_fn(results, metric_name)\\n    boot_values = []\\n    for _ in range(n_bootstrap):\\n        idx = rng.choice(n, n, replace=True)\\n        boot_sample = [results[i] for i in idx]\\n        boot_values.append(_metric_fn(boot_sample, metric_name))\\n\\n    alpha = (1 - ci) / 2\\n    lo = float(np.percentile(boot_values, alpha * 100))\\n    hi = float(np.percentile(boot_values, (1 - alpha) * 100))\\n    return (point, lo, hi)\\n\\n\\n# ── Stratification ───────────────────────────────────────────────────\\n\\ndef assign_strata(\\n    results: List[Dict],\\n    inst_to_repo: Dict[str, str],\\n    repo_counts: Dict[str, int],\\n) -> List[Dict]:\\n    for r in results:\\n        repo = inst_to_repo.get(r[\\\"instance_id\\\"], \\\"\\\")\\n        rc = repo_counts.get(repo, 0)\\n        r[\\\"repo\\\"] = repo\\n        r[\\\"repo_size\\\"] = rc\\n        r[\\\"repo_size_bin\\\"] = _bin_value(rc, REPO_SIZE_BINS)\\n        r[\\\"pool_size_bin\\\"] = _bin_value(r[\\\"pool_size\\\"], POOL_SIZE_BINS)\\n        r[\\\"sim_bin\\\"] = _bin_value(r[\\\"pos_sim\\\"], SIMILARITY_BINS)\\n    return results\\n\\n\\ndef group_by(results: List[Dict], key: str) -> Dict[str, List[Dict]]:\\n    groups: Dict[str, List[Dict]] = defaultdict(list)\\n    for r in results:\\n        groups[r[key]].append(r)\\n    return dict(groups)\\n\\n\\n# ── Analysis core ────────────────────────────────────────────────────\\n\\ndef run_stratified_analysis(\\n    all_results: Dict[str, Dict[int, List[Dict]]],\\n    strata_key: str,\\n    bin_order: List[str],\\n    n_bootstrap: int = 1000,\\n) -> Dict:\\n    analysis = {}\\n    for bin_name in bin_order:\\n        analysis[bin_name] = {}\\n        for strategy in STRATEGIES:\\n            seed_results = []\\n            for seed, results in all_results.get(strategy, {}).items():\\n                grouped = group_by(results, strata_key)\\n                seed_results.extend(grouped.get(bin_name, []))\\n\\n            metrics = compute_metrics(seed_results)\\n            ci_r1 = bootstrap_ci(seed_results, \\\"R@1\\\", n_bootstrap)\\n            ci_r5 = bootstrap_ci(seed_results, \\\"R@5\\\", n_bootstrap)\\n            ci_mrr = bootstrap_ci(seed_results, \\\"MRR\\\", n_bootstrap)\\n\\n            analysis[bin_name][strategy] = \\n\\n... [截断: 输出过长，省略 12890 字符] ...\\n\\n file not found: {val_file}, skipping\\\", flush=True)\\n                continue\\n\\n            if args.dry_run:\\n                print(f\\\"  Generating mock predictions: {strategy} seed={seed}\\\", flush=True)\\n                results = mock_predictions(val_samples, strategy, seed)\\n            elif args.predictions_dir:\\n                pred_pattern = os.path.join(\\n                    args.predictions_dir, f\\\"*{strategy}*s{seed}*.json\\\"\\n                )\\n                import glob\\n                pred_files = glob.glob(pred_pattern)\\n                if pred_files:\\n                    print(f\\\"  Loading predictions: {pred_files[0]}\\\", flush=True)\\n                    results = load_predictions(pred_files[0], val_samples)\\n                else:\\n                    print(f\\\"  [WARN] No prediction file matching {pred_pattern}\\\", flush=True)\\n                    continue\\n            elif args.checkpoints_dir:\\n                ckpt_dir = os.path.join(\\n                    args.checkpoints_dir, f\\\"{strategy}_s{seed}\\\", \\\"best\\\"\\n                )\\n                if not os.path.exists(ckpt_dir):\\n                    ckpt_dir = os.path.join(args.checkpoints_dir, f\\\"{strategy}_s{seed}\\\")\\n                if os.path.exists(ckpt_dir):\\n                    print(f\\\"  Re-evaluating checkpoint: {ckpt_dir}\\\", flush=True)\\n                    results = reeval_checkpoint(\\n                        ckpt_dir, val_samples, args.device, args.max_seq_length\\n                    )\\n                else:\\n                    print(f\\\"  [WARN] Checkpoint not found: {ckpt_dir}\\\", flush=True)\\n                    continue\\n            else:\\n                print(\\\"  [ERROR] No --dry-run, --predictions-dir, or --checkpoints-dir\\\", flush=True)\\n                continue\\n\\n            # Assign strata\\n            results = assign_strata(results, inst_to_repo, repo_counts)\\n\\n            # For dry-run or model-based: compute text similarity for sim_bin\\n            if args.dry_run:\\n                for r, s in zip(results, val_samples):\\n                    tsim = text_similarity(s[\\\"query_tokens\\\"][:500], s[\\\"pos_tokens\\\"][:500])\\n                    r[\\\"sim_bin\\\"] = _bin_value(tsim, SIMILARITY_BINS)\\n\\n            all_results[strategy][seed] = results\\n            print(f\\\"  -> {len(results)} instances\\\", flush=True)\\n\\n    # Run stratified analysis\\n    print(\\\"\\\\nRunning stratified analysis...\\\", flush=True)\\n    repo_analysis = run_stratified_analysis(\\n        all_results, \\\"repo_size_bin\\\", list(REPO_SIZE_BINS.keys()), args.n_bootstrap\\n    )\\n    pool_analysis = run_stratified_analysis(\\n        all_results, \\\"pool_size_bin\\\", list(POOL_SIZE_BINS.keys()), args.n_bootstrap\\n    )\\n    sim_analysis = run_stratified_analysis(\\n        all_results, \\\"sim_bin\\\", list(SIMILARITY_BINS.keys()), args.n_bootstrap\\n    )\\n\\n    # Save JSON\\n    full_results = {\\n        \\\"config\\\": {\\n            \\\"strategies\\\": STRATEGIES,\\n            \\\"seeds\\\": seeds,\\n            \\\"repo_size_bins\\\": {k: list(v) for k, v in REPO_SIZE_BINS.items()},\\n            \\\"pool_size_bins\\\": {k: list(v) for k, v in POOL_SIZE_BINS.items()},\\n            \\\"similarity_bins\\\": {k: list(v) for k, v in SIMILARITY_BINS.items()},\\n            \\\"n_bootstrap\\\": args.n_bootstrap,\\n            \\\"dry_run\\\": args.dry_run,\\n        },\\n        \\\"by_repo_size\\\": repo_analysis,\\n        \\\"by_pool_size\\\": pool_analysis,\\n        \\\"by_similarity\\\": sim_analysis,\\n    }\\n\\n    json_path = os.path.join(args.output_dir, \\\"stratified_results.json\\\")\\n    with open(json_path, \\\"w\\\") as f:\\n        json.dump(full_results, f, indent=2, ensure_ascii=False)\\n    print(f\\\"  Results JSON saved to {json_path}\\\", flush=True)\\n\\n    # CSV summary\\n    csv_path = os.path.join(args.output_dir, \\\"stratified_summary.csv\\\")\\n    write_summary_csv(repo_analysis, pool_analysis, sim_analysis, csv_path)\\n\\n    # Plots\\n    try:\\n        make_plots(repo_analysis, pool_analysis, sim_analysis, args.output_dir)\\n    except Exception as e:\\n        print(f\\\"  [WARN] Plot generation failed: {e}\\\", flush=True)\\n\\n    print(\\\"\\\\nDone.\\\", flush=True)\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "e6c2fd9c-5e52-46d1-a4df-194c2c0605b8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\ndef mock_predictions(\\\\n    val_samples: List[Dict], strategy: str, seed: int\\\\n) -> List[Dict]:\\\\n    rng = np.random.RandomState(seed + abs(hash(strategy)) % 10000)\\\\n    results = []\\\\n    for sample in val_samples:\\\\n        pool = 1 + sample[\\\\\\\"pool_size\\\\\\\"]\\\\n        if strategy == \\\\\\\"random\\\\\\\":\\\\n            rank = rng.randint(1, pool + 1)\\\\n        elif strategy == \\\\\\\"embedding_distance\\\\\\\":\\\\n            rank = max(1, min(pool, int(rng.exponential(pool * 0.35)) + 1))\\\\n        else:\\\\n            rank = max(1, min(pool, int(rng.exponential(pool * 0.20)) + 1))\\\\n\\\\n        pos_sim = max(0.0, min(1.0, 1.0 - rank / pool + rng.normal(0, 0.08)))\\\\n        tsim = text_similarity(\\\\n            sample[\\\\\\\"query_tokens\\\\\\\"][:500], sample[\\\\\\\"pos_tokens\\\\\\\"][:500]\\\\n        )\\\\n\\\\n        results.append({\\\\n            \\\\\\\"query_id\\\\\\\": sample[\\\\\\\"query_id\\\\\\\"],\\\\n            \\\\\\\"instance_id\\\\\\\": sample[\\\\\\\"instance_id\\\\\\\"],\\\\n            \\\\\\\"pool_size\\\\\\\": sample[\\\\\\\"pool_size\\\\\\\"],\\\\n            \\\\\\\"rank\\\\\\\": rank,\\\\n            \\\\\\\"pos_sim\\\\\\\": pos_sim if pos_sim > 0 else tsim,\\\\n            \\\\\\\"total_candidates\\\\\\\": pool,\\\\n        })\\\\n    return results\\\\n\\\\n\\\\n# ── Metrics computation ──────────────────────────────────────────────\\\\n\\\\ndef compute_metrics(results: List[Dict]) -> Dict[str, float]:\\\\n    if not results:\\\\n        return {\\\\\\\"R@1\\\\\\\": 0.0, \\\\\\\"R@5\\\\\\\": 0.0, \\\\\\\"MRR\\\\\\\": 0.0, \\\\\\\"count\\\\\\\": 0}\\\\n    ranks = [r[\\\\\\\"rank\\\\\\\"] for r in results]\\\\n    n = len(ranks)\\\\n    return {\\\\n        \\\\\\\"R@1\\\\\\\": sum(1 for r in ranks if r <= 1) / n,\\\\n        \\\\\\\"R@5\\\\\\\": sum(1 for r in ranks if r <= 5) / n,\\\\n        \\\\\\\"MRR\\\\\\\": sum(1.0 / r for r in ranks) / n,\\\\n        \\\\\\\"count\\\\\\\": n,\\\\n    }\\\\n\\\\n\\\\ndef _metric_fn(results, metric_name):\\\\n    m = compute_metrics(results)\\\\n    return m[metric_name]\\\\n\\\\n\\\\ndef bootstrap_ci(\\\\n    results: List[Dict],\\\\n    metric_name: str = \\\\\\\"R@1\\\\\\\",\\\\n    n_bootstrap: int = 1000,\\\\n    ci: float = 0.95,\\\\n    seed: int = 42,\\\\n) -> Tuple[float, float, float]:\\\\n    rng = np.random.RandomState(seed)\\\\n    n = len(results)\\\\n    if n == 0:\\\\n        return (0.0, 0.0, 0.0)\\\\n\\\\n    point = _metric_fn(results, metric_name)\\\\n    boot_values = []\\\\n    for _ in range(n_bootstrap):\\\\n        idx = rng.choice(n, n, replace=True)\\\\n        boot_sample = [results[i] for i in idx]\\\\n        boot_values.append(_metric_fn(boot_sample, metric_name))\\\\n\\\\n    alpha = (1 - ci) / 2\\\\n    lo = float(np.percentile(boot_values, alpha * 100))\\\\n    hi = float(np.percentile(boot_values, (1 - alpha) * 100))\\\\n    return (point, lo, hi)\\\\n\\\\n\\\\n# ── Stratification ───────────────────────────────────────────────────\\\\n\\\\ndef assign_strata(\\\\n    results: List[Dict],\\\\n    inst_to_repo: Dict[str, str],\\\\n    repo_counts: Dict[str, int],\\\\n) -> List[Dict]:\\\\n    for r in results:\\\\n        repo = inst_to_repo.get(r[\\\\\\\"instance_id\\\\\\\"], \\\\\\\"\\\\\\\")\\\\n        rc = repo_counts.get(repo, 0)\\\\n        r[\\\\\\\"repo\\\\\\\"] = repo\\\\n        r[\\\\\\\"repo_size\\\\\\\"] = rc\\\\n        r[\\\\\\\"repo_size_bin\\\\\\\"] = _bin_value(rc, REPO_SIZE_BINS)\\\\n        r[\\\\\\\"pool_size_bin\\\\\\\"] = _bin_value(r[\\\\\\\"pool_size\\\\\\\"], POOL_SIZE_BINS)\\\\n        r[\\\\\\\"sim_bin\\\\\\\"] = _bin_value(r[\\\\\\\"pos_sim\\\\\\\"], SIMILARITY_BINS)\\\\n    return results\\\\n\\\\n\\\\ndef group_by(results: List[Dict], key: str) -> Dict[str, List[Dict]]:\\\\n    groups: Dict[str, List[Dict]] = defaultdict(list)\\\\n    for r in results:\\\\n        groups[r[key]].append(r)\\\\n    return dict(groups)\\\\n\\\\n\\\\n# ── Analysis core ────────────────────────────────────────────────────\\\\n\\\\ndef run_stratified_analysis(\\\\n    all_results: Dict[str, Dict[int, List[Dict]]],\\\\n    strata_key: str,\\\\n    bin_order: List[str],\\\\n    n_bootstrap: int = 1000,\\\\n) -> Dict:\\\\n    analysis = {}\\\\n    for bin_name in bin_order:\\\\n        analysis[bin_name] = {}\\\\n        for strategy in STRATEGIES:\\\\n            seed_results = []\\\\n            for seed, results in all_results.get(strategy, {}).items():\\\\n                grouped = group_by(results, strata_key)\\\\n                seed_results.extend(grouped.get(bin_name, []))\\\\n\\\\n            metrics = compute_metrics(seed_results)\\\\n            ci_r1 = bootstrap_ci(seed_results, \\\\\\\"R@1\\\\\\\", n_bootstrap)\\\\n            ci_r5 = bootstrap_ci(seed_results, \\\\\\\"R@5\\\\\\\", n_bootstrap)\\\\n            ci_mrr = bootstrap_ci(seed_results, \\\\\\\"MRR\\\\\\\", n_bootstrap)\\\\n\\\\n            analysis[bin_name][strategy] = \\\\n\\\\n... [截断: 输出过长，省略 12890 字符] ...\\\\n\\\\n file not found: {val_file}, skipping\\\\\\\", flush=True)\\\\n                continue\\\\n\\\\n            if args.dry_run:\\\\n                print(f\\\\\\\"  Generating mock predictions: {strategy} seed={seed}\\\\\\\", flush=True)\\\\n                results = mock_predictions(val_samples, strategy, seed)\\\\n            elif args.predictions_dir:\\\\n                pred_pattern = os.path.join(\\\\n                    args.predictions_dir, f\\\\\\\"*{strategy}*s{seed}*.json\\\\\\\"\\\\n                )\\\\n                import glob\\\\n                pred_files = glob.glob(pred_pattern)\\\\n                if pred_files:\\\\n                    print(f\\\\\\\"  Loading predictions: {pred_files[0]}\\\\\\\", flush=True)\\\\n                    results = load_predictions(pred_files[0], val_samples)\\\\n                else:\\\\n                    print(f\\\\\\\"  [WARN] No prediction file matching {pred_pattern}\\\\\\\", flush=True)\\\\n                    continue\\\\n            elif args.checkpoints_dir:\\\\n                ckpt_dir = os.path.join(\\\\n                    args.checkpoints_dir, f\\\\\\\"{strategy}_s{seed}\\\\\\\", \\\\\\\"best\\\\\\\"\\\\n                )\\\\n                if not os.path.exists(ckpt_dir):\\\\n                    ckpt_dir = os.path.join(args.checkpoints_dir, f\\\\\\\"{strategy}_s{seed}\\\\\\\")\\\\n                if os.path.exists(ckpt_dir):\\\\n                    print(f\\\\\\\"  Re-evaluating checkpoint: {ckpt_dir}\\\\\\\", flush=True)\\\\n                    results = reeval_checkpoint(\\\\n                        ckpt_dir, val_samples, args.device, args.max_seq_length\\\\n                    )\\\\n                else:\\\\n                    print(f\\\\\\\"  [WARN] Checkpoint not found: {ckpt_dir}\\\\\\\", flush=True)\\\\n                    continue\\\\n            else:\\\\n                print(\\\\\\\"  [ERROR] No --dry-run, --predictions-dir, or --checkpoints-dir\\\\\\\", flush=True)\\\\n                continue\\\\n\\\\n            # Assign strata\\\\n            results = assign_strata(results, inst_to_repo, repo_counts)\\\\n\\\\n            # For dry-run or model-based: compute text similarity for sim_bin\\\\n            if args.dry_run:\\\\n                for r, s in zip(results, val_samples):\\\\n                    tsim = text_similarity(s[\\\\\\\"query_tokens\\\\\\\"][:500], s[\\\\\\\"pos_tokens\\\\\\\"][:500])\\\\n                    r[\\\\\\\"sim_bin\\\\\\\"] = _bin_value(tsim, SIMILARITY_BINS)\\\\n\\\\n            all_results[strategy][seed] = results\\\\n            print(f\\\\\\\"  -> {len(results)} instances\\\\\\\", flush=True)\\\\n\\\\n    # Run stratified analysis\\\\n    print(\\\\\\\"\\\\\\\\nRunning stratified analysis...\\\\\\\", flush=True)\\\\n    repo_analysis = run_stratified_analysis(\\\\n        all_results, \\\\\\\"repo_size_bin\\\\\\\", list(REPO_SIZE_BINS.keys()), args.n_bootstrap\\\\n    )\\\\n    pool_analysis = run_stratified_analysis(\\\\n        all_results, \\\\\\\"pool_size_bin\\\\\\\", list(POOL_SIZE_BINS.keys()), args.n_bootstrap\\\\n    )\\\\n    sim_analysis = run_stratified_analysis(\\\\n        all_results, \\\\\\\"sim_bin\\\\\\\", list(SIMILARITY_BINS.keys()), args.n_bootstrap\\\\n    )\\\\n\\\\n    # Save JSON\\\\n    full_results = {\\\\n        \\\\\\\"config\\\\\\\": {\\\\n            \\\\\\\"strategies\\\\\\\": STRATEGIES,\\\\n            \\\\\\\"seeds\\\\\\\": seeds,\\\\n            \\\\\\\"repo_size_bins\\\\\\\": {k: list(v) for k, v in REPO_SIZE_BINS.items()},\\\\n            \\\\\\\"pool_size_bins\\\\\\\": {k: list(v) for k, v in POOL_SIZE_BINS.items()},\\\\n            \\\\\\\"similarity_bins\\\\\\\": {k: list(v) for k, v in SIMILARITY_BINS.items()},\\\\n            \\\\\\\"n_bootstrap\\\\\\\": args.n_bootstrap,\\\\n            \\\\\\\"dry_run\\\\\\\": args.dry_run,\\\\n        },\\\\n        \\\\\\\"by_repo_size\\\\\\\": repo_analysis,\\\\n        \\\\\\\"by_pool_size\\\\\\\": pool_analysis,\\\\n        \\\\\\\"by_similarity\\\\\\\": sim_analysis,\\\\n    }\\\\n\\\\n    json_path = os.path.join(args.output_dir, \\\\\\\"stratified_results.json\\\\\\\")\\\\n    with open(json_path, \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(full_results, f, indent=2, ensure_ascii=False)\\\\n    print(f\\\\\\\"  Results JSON saved to {json_path}\\\\\\\", flush=True)\\\\n\\\\n    # CSV summary\\\\n    csv_path = os.path.join(args.output_dir, \\\\\\\"stratified_summary.csv\\\\\\\")\\\\n    write_summary_csv(repo_analysis, pool_analysis, sim_analysis, csv_path)\\\\n\\\\n    # Plots\\\\n    try:\\\\n        make_plots(repo_analysis, pool_analysis, sim_analysis, args.output_dir)\\\\n    except Exception as e:\\\\n        print(f\\\\\\\"  [WARN] Plot generation failed: {e}\\\\\\\", flush=True)\\\\n\\\\n    print(\\\\\\\"\\\\\\\\nDone.\\\\\\\", flush=True)\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.39}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\ndef mock_predictions(\\n    val_samples: List[Dict], strategy: str, seed: int\\n) -> List[Dict]:\\n    rng = np.random.RandomState(seed + abs(hash(strategy)) % 10000)\\n    results = []\\n    for sample in val_samples:\\n        pool = 1 + sample[\\\"pool_size\\\"]\\n        if strategy == \\\"random\\\":\\n            rank = rng.randint(1, pool + 1)\\n        elif strategy == \\\"embedding_distance\\\":\\n            rank = max(1, min(pool, int(rng.exponential(pool * 0.35)) + 1))\\n        else:\\n            rank = max(1, min(pool, int(rng.exponential(pool * 0.20)) + 1))\\n\\n        pos_sim = max(0.0, min(1.0, 1.0 - rank / pool + rng.normal(0, 0.08)))\\n        tsim = text_similarity(\\n            sample[\\\"query_tokens\\\"][:500], sample[\\\"pos_tokens\\\"][:500]\\n        )\\n\\n        results.append({\\n            \\\"query_id\\\": sample[\\\"query_id\\\"],\\n            \\\"instance_id\\\": sample[\\\"instance_id\\\"],\\n            \\\"pool_size\\\": sample[\\\"pool_size\\\"],\\n            \\\"rank\\\": rank,\\n            \\\"pos_sim\\\": pos_sim if pos_sim > 0 else tsim,\\n            \\\"total_candidates\\\": pool,\\n        })\\n    return results\\n\\n\\n# ── Metrics computation ──────────────────────────────────────────────\\n\\ndef compute_metrics(results: List[Dict]) -> Dict[str, float]:\\n    if not results:\\n        return {\\\"R@1\\\": 0.0, \\\"R@5\\\": 0.0, \\\"MRR\\\": 0.0, \\\"count\\\": 0}\\n    ranks = [r[\\\"rank\\\"] for r in results]\\n    n = len(ranks)\\n    return {\\n        \\\"R@1\\\": sum(1 for r in ranks if r <= 1) / n,\\n        \\\"R@5\\\": sum(1 for r in ranks if r <= 5) / n,\\n        \\\"MRR\\\": sum(1.0 / r for r in ranks) / n,\\n        \\\"count\\\": n,\\n    }\\n\\n\\ndef _metric_fn(results, metric_name):\\n    m = compute_metrics(results)\\n    return m[metric_name]\\n\\n\\ndef bootstrap_ci(\\n    results: List[Dict],\\n    metric_name: str = \\\"R@1\\\",\\n    n_bootstrap: int = 1000,\\n    ci: float = 0.95,\\n    seed: int = 42,\\n) -> Tuple[float, float, float]:\\n    rng = np.random.RandomState(seed)\\n    n = len(results)\\n    if n == 0:\\n        return (0.0, 0.0, 0.0)\\n\\n    point = _metric_fn(results, metric_name)\\n    boot_values = []\\n    for _ in range(n_bootstrap):\\n        idx = rng.choice(n, n, replace=True)\\n        boot_sample = [results[i] for i in idx]\\n        boot_values.append(_metric_fn(boot_sample, metric_name))\\n\\n    alpha = (1 - ci) / 2\\n    lo = float(np.percentile(boot_values, alpha * 100))\\n    hi = float(np.percentile(boot_values, (1 - alpha) * 100))\\n    return (point, lo, hi)\\n\\n\\n# ── Stratification ───────────────────────────────────────────────────\\n\\ndef assign_strata(\\n    results: List[Dict],\\n    inst_to_repo: Dict[str, str],\\n    repo_counts: Dict[str, int],\\n) -> List[Dict]:\\n    for r in results:\\n        repo = inst_to_repo.get(r[\\\"instance_id\\\"], \\\"\\\")\\n        rc = repo_counts.get(repo, 0)\\n        r[\\\"repo\\\"] = repo\\n        r[\\\"repo_size\\\"] = rc\\n        r[\\\"repo_size_bin\\\"] = _bin_value(rc, REPO_SIZE_BINS)\\n        r[\\\"pool_size_bin\\\"] = _bin_value(r[\\\"pool_size\\\"], POOL_SIZE_BINS)\\n        r[\\\"sim_bin\\\"] = _bin_value(r[\\\"pos_sim\\\"], SIMILARITY_BINS)\\n    return results\\n\\n\\ndef group_by(results: List[Dict], key: str) -> Dict[str, List[Dict]]:\\n    groups: Dict[str, List[Dict]] = defaultdict(list)\\n    for r in results:\\n        groups[r[key]].append(r)\\n    return dict(groups)\\n\\n\\n# ── Analysis core ────────────────────────────────────────────────────\\n\\ndef run_stratified_analysis(\\n    all_results: Dict[str, Dict[int, List[Dict]]],\\n    strata_key: str,\\n    bin_order: List[str],\\n    n_bootstrap: int = 1000,\\n) -> Dict:\\n    analysis = {}\\n    for bin_name in bin_order:\\n        analysis[bin_name] = {}\\n        for strategy in STRATEGIES:\\n            seed_results = []\\n            for seed, results in all_results.get(strategy, {}).items():\\n                grouped = group_by(results, strata_key)\\n                seed_results.extend(grouped.get(bin_name, []))\\n\\n            metrics = compute_metrics(seed_results)\\n            ci_r1 = bootstrap_ci(seed_results, \\\"R@1\\\", n_bootstrap)\\n            ci_r5 = bootstrap_ci(seed_results, \\\"R@5\\\", n_bootstrap)\\n            ci_mrr = bootstrap_ci(seed_results, \\\"MRR\\\", n_bootstrap)\\n\\n            analysis[bin_name][strategy] = \\n\\n... [截断: 输出过长，省略 12890 字符] ...\\n\\n file not found: {val_file}, skipping\\\", flush=True)\\n                continue\\n\\n            if args.dry_run:\\n                print(f\\\"  Generating mock predictions: {strategy} seed={seed}\\\", flush=True)\\n                results = mock_predictions(val_samples, strategy, seed)\\n            elif args.predictions_dir:\\n                pred_pattern = os.path.join(\\n                    args.predictions_dir, f\\\"*{strategy}*s{seed}*.json\\\"\\n                )\\n                import glob\\n                pred_files = glob.glob(pred_pattern)\\n                if pred_files:\\n                    print(f\\\"  Loading predictions: {pred_files[0]}\\\", flush=True)\\n                    results = load_predictions(pred_files[0], val_samples)\\n                else:\\n                    print(f\\\"  [WARN] No prediction file matching {pred_pattern}\\\", flush=True)\\n                    continue\\n            elif args.checkpoints_dir:\\n                ckpt_dir = os.path.join(\\n                    args.checkpoints_dir, f\\\"{strategy}_s{seed}\\\", \\\"best\\\"\\n                )\\n                if not os.path.exists(ckpt_dir):\\n                    ckpt_dir = os.path.join(args.checkpoints_dir, f\\\"{strategy}_s{seed}\\\")\\n                if os.path.exists(ckpt_dir):\\n                    print(f\\\"  Re-evaluating checkpoint: {ckpt_dir}\\\", flush=True)\\n                    results = reeval_checkpoint(\\n                        ckpt_dir, val_samples, args.device, args.max_seq_length\\n                    )\\n                else:\\n                    print(f\\\"  [WARN] Checkpoint not found: {ckpt_dir}\\\", flush=True)\\n                    continue\\n            else:\\n                print(\\\"  [ERROR] No --dry-run, --predictions-dir, or --checkpoints-dir\\\", flush=True)\\n                continue\\n\\n            # Assign strata\\n            results = assign_strata(results, inst_to_repo, repo_counts)\\n\\n            # For dry-run or model-based: compute text similarity for sim_bin\\n            if args.dry_run:\\n                for r, s in zip(results, val_samples):\\n                    tsim = text_similarity(s[\\\"query_tokens\\\"][:500], s[\\\"pos_tokens\\\"][:500])\\n                    r[\\\"sim_bin\\\"] = _bin_value(tsim, SIMILARITY_BINS)\\n\\n            all_results[strategy][seed] = results\\n            print(f\\\"  -> {len(results)} instances\\\", flush=True)\\n\\n    # Run stratified analysis\\n    print(\\\"\\\\nRunning stratified analysis...\\\", flush=True)\\n    repo_analysis = run_stratified_analysis(\\n        all_results, \\\"repo_size_bin\\\", list(REPO_SIZE_BINS.keys()), args.n_bootstrap\\n    )\\n    pool_analysis = run_stratified_analysis(\\n        all_results, \\\"pool_size_bin\\\", list(POOL_SIZE_BINS.keys()), args.n_bootstrap\\n    )\\n    sim_analysis = run_stratified_analysis(\\n        all_results, \\\"sim_bin\\\", list(SIMILARITY_BINS.keys()), args.n_bootstrap\\n    )\\n\\n    # Save JSON\\n    full_results = {\\n        \\\"config\\\": {\\n            \\\"strategies\\\": STRATEGIES,\\n            \\\"seeds\\\": seeds,\\n            \\\"repo_size_bins\\\": {k: list(v) for k, v in REPO_SIZE_BINS.items()},\\n            \\\"pool_size_bins\\\": {k: list(v) for k, v in POOL_SIZE_BINS.items()},\\n            \\\"similarity_bins\\\": {k: list(v) for k, v in SIMILARITY_BINS.items()},\\n            \\\"n_bootstrap\\\": args.n_bootstrap,\\n            \\\"dry_run\\\": args.dry_run,\\n        },\\n        \\\"by_repo_size\\\": repo_analysis,\\n        \\\"by_pool_size\\\": pool_analysis,\\n        \\\"by_similarity\\\": sim_analysis,\\n    }\\n\\n    json_path = os.path.join(args.output_dir, \\\"stratified_results.json\\\")\\n    with open(json_path, \\\"w\\\") as f:\\n        json.dump(full_results, f, indent=2, ensure_ascii=False)\\n    print(f\\\"  Results JSON saved to {json_path}\\\", flush=True)\\n\\n    # CSV summary\\n    csv_path = os.path.join(args.output_dir, \\\"stratified_summary.csv\\\")\\n    write_summary_csv(repo_analysis, pool_analysis, sim_analysis, csv_path)\\n\\n    # Plots\\n    try:\\n        make_plots(repo_analysis, pool_analysis, sim_analysis, args.output_dir)\\n    except Exception as e:\\n        print(f\\\"  [WARN] Plot generation failed: {e}\\\", flush=True)\\n\\n    print(\\\"\\\\nDone.\\\", flush=True)\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 38_

<details><summary>Logged reasoning block</summary>

```text
Let me get the middle part that was truncated - lines 370-530 or so, which contains the analysis core and the argparse section.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "837319e9-2bc8-4573-a5ae-ca35a7bbbb2d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W8DM8XFczZ6UCbdwfZAFbk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3333,
      "cache_read_input_tokens": 37022,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3333
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

_source line 39_

需要看 argparse 和中间被截断的部分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "d46b0661-ac3a-4a6e-9cf2-7b52ece7d585",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W8DM8XFczZ6UCbdwfZAFbk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3333,
      "cache_read_input_tokens": 37022,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3333
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

_source line 40_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_014xyoy2Vm43LVT9xPfxpBm5`</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "sed -n '370,530p' /root/structfuse/evaluation/analyze_stratified.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "37bcddb4-7293-4988-818a-0dc0bfb26d89",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W8DM8XFczZ6UCbdwfZAFbk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3333,
      "cache_read_input_tokens": 37022,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3333
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

_source line 41 · 2026-05-14T20:15:39.987Z_

<details><summary>↩ Tool result · `toolu_014xyoy2Vm43LVT9xPfxpBm5`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'sed' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "34efa5aa-e02b-47b1-bd18-5be42ecdde24",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: 'sed' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'sed' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 42_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01A8FEJkoGHED3TGRQY4cf7q`</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "sed -n '530,650p' /root/structfuse/evaluation/analyze_stratified.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "1c01d66b-e1a1-4e4c-a51c-b19a599645a0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W8DM8XFczZ6UCbdwfZAFbk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3333,
      "cache_read_input_tokens": 37022,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3333
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

_source line 43 · 2026-05-14T20:15:40.798Z_

<details><summary>↩ Tool result · `toolu_01A8FEJkoGHED3TGRQY4cf7q`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'sed' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "dae5270e-be24-4033-9eff-a89074c4369f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: 'sed' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'sed' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 44_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01LuDLHeeYCGFgHzuBKnLpKk`</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "grep -n \"def \\|argparse\\|add_argument\\|structural\\|dataflow\\|neg_difficulty\\|quartile\\|has_dataflow\" /root/structfuse/evaluation/analyze_stratified.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "7d3574fc-71e0-4f06-9d03-27c55b86393f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015VZ2bYmYxky7FudMMAGCCJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 648,
      "cache_read_input_tokens": 40355,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 648
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

_source line 45 · 2026-05-14T20:15:44.388Z_

<details><summary>↩ Tool result · `toolu_01LuDLHeeYCGFgHzuBKnLpKk`</summary>

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
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "ddee53b3-d435-4a6d-9fd7-3eff05072e73",
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

_source line 46_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01R4WStoouX3mrFQ5f3s6vFe`</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "grep -n \"def \\|add_argument\\|structural\\|dataflow\\|neg_difficulty\\|quartile\" /root/structfuse/evaluation/analyze_stratified.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "92d66dff-679d-4fdf-8c90-70ba542a890a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WmWMgayeR2VLrS4BVjWrhr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 247,
      "cache_read_input_tokens": 41003,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 247
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

_source line 47 · 2026-05-14T20:15:47.597Z_

<details><summary>↩ Tool result · `toolu_01R4WStoouX3mrFQ5f3s6vFe`</summary>

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
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "037ba8e8-bec1-4784-860d-1aad38660eef",
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

_source line 48_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Wc5uvSMP33d4dA7Pgi9YF9`</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "grep -n \"def \" /root/structfuse/evaluation/analyze_stratified.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "36fe6bbc-bc1c-4f9b-92aa-7a67fa11c529",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Amj9KcQjujV7Uabza8ZGC3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 237,
      "cache_read_input_tokens": 41250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 237
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

_source line 49 · 2026-05-14T20:15:51.319Z_

<details><summary>↩ Tool result · `toolu_01Wc5uvSMP33d4dA7Pgi9YF9`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"56:def _bin_value(value, bins):\\n65:def load_m1_metadata(m1_path: str) -> Tuple[Dict[str, str], Dict[str, int]]:\\n85:def load_val_samples(val_path: str, lite: bool = False) -> List[Dict[str, Any]]:\\n126:def text_similarity(a: str, b: str) -> float:\\n137:def reeval_checkpoint(\\n176:            def _encode(text):\\n213:def load_predictions(pred_file: str, val_samples: List[Dict]) -> List[Dict]:\\n251:def mock_predictions(\\n283:def compute_metrics(results: List[Dict]) -> Dict[str, float]:\\n296:def _metric_fn(results, metric_name):\\n301:def bootstrap_ci(\\n328:def assign_strata(\\n344:def group_by(results: List[Dict], key: str) -> Dict[str, List[Dict]]:\\n353:def run_stratified_analysis(\\n402:def make_plots(\\n560:def write_summary_csv(\\n617:def main():\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "81d52e96-8f51-4aa8-bf77-f7ca508837f5",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"56:def _bin_value(value, bins):\\\\n65:def load_m1_metadata(m1_path: str) -> Tuple[Dict[str, str], Dict[str, int]]:\\\\n85:def load_val_samples(val_path: str, lite: bool = False) -> List[Dict[str, Any]]:\\\\n126:def text_similarity(a: str, b: str) -> float:\\\\n137:def reeval_checkpoint(\\\\n176:            def _encode(text):\\\\n213:def load_predictions(pred_file: str, val_samples: List[Dict]) -> List[Dict]:\\\\n251:def mock_predictions(\\\\n283:def compute_metrics(results: List[Dict]) -> Dict[str, float]:\\\\n296:def _metric_fn(results, metric_name):\\\\n301:def bootstrap_ci(\\\\n328:def assign_strata(\\\\n344:def group_by(results: List[Dict], key: str) -> Dict[str, List[Dict]]:\\\\n353:def run_stratified_analysis(\\\\n402:def make_plots(\\\\n560:def write_summary_csv(\\\\n617:def main():\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.37}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"56:def _bin_value(value, bins):\\n65:def load_m1_metadata(m1_path: str) -> Tuple[Dict[str, str], Dict[str, int]]:\\n85:def load_val_samples(val_path: str, lite: bool = False) -> List[Dict[str, Any]]:\\n126:def text_similarity(a: str, b: str) -> float:\\n137:def reeval_checkpoint(\\n176:            def _encode(text):\\n213:def load_predictions(pred_file: str, val_samples: List[Dict]) -> List[Dict]:\\n251:def mock_predictions(\\n283:def compute_metrics(results: List[Dict]) -> Dict[str, float]:\\n296:def _metric_fn(results, metric_name):\\n301:def bootstrap_ci(\\n328:def assign_strata(\\n344:def group_by(results: List[Dict], key: str) -> Dict[str, List[Dict]]:\\n353:def run_stratified_analysis(\\n402:def make_plots(\\n560:def write_summary_csv(\\n617:def main():\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 50_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Dfj1uX66BNoP2Xe4SQLa4A`</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "grep -n \"add_argument\" /root/structfuse/evaluation/analyze_stratified.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "7ece0dd5-65e1-4549-98ba-ad2f31b15ddb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Amj9KcQjujV7Uabza8ZGC3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 237,
      "cache_read_input_tokens": 41250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 237
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

_source line 51 · 2026-05-14T20:15:51.823Z_

<details><summary>↩ Tool result · `toolu_01Dfj1uX66BNoP2Xe4SQLa4A`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"621:    parser.add_argument(\\\"--predictions-dir\\\", default=None,\\n623:    parser.add_argument(\\\"--checkpoints-dir\\\", default=None,\\n625:    parser.add_argument(\\\"--val-data-dir\\\", default=None,\\n627:    parser.add_argument(\\\"--m1-data\\\", required=True,\\n629:    parser.add_argument(\\\"--output-dir\\\", required=True)\\n630:    parser.add_argument(\\\"--dry-run\\\", action=\\\"store_true\\\",\\n632:    parser.add_argument(\\\"--seeds\\\", default=\\\"42,43,44\\\",\\n634:    parser.add_argument(\\\"--device\\\", default=\\\"cuda\\\")\\n635:    parser.add_argument(\\\"--max-seq-length\\\", type=int, default=2048)\\n636:    parser.add_argument(\\\"--n-bootstrap\\\", type=int, default=1000)\\n637:    parser.add_argument(\\\"--repo-size-bins\\\", default=None,\\n639:    parser.add_argument(\\\"--pool-size-bins\\\", default=None,\\n641:    parser.add_argument(\\\"--sim-bins\\\", default=None,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "25db089d-688b-42c7-917e-f90bde23635a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"621:    parser.add_argument(\\\\\\\"--predictions-dir\\\\\\\", default=None,\\\\n623:    parser.add_argument(\\\\\\\"--checkpoints-dir\\\\\\\", default=None,\\\\n625:    parser.add_argument(\\\\\\\"--val-data-dir\\\\\\\", default=None,\\\\n627:    parser.add_argument(\\\\\\\"--m1-data\\\\\\\", required=True,\\\\n629:    parser.add_argument(\\\\\\\"--output-dir\\\\\\\", required=True)\\\\n630:    parser.add_argument(\\\\\\\"--dry-run\\\\\\\", action=\\\\\\\"store_true\\\\\\\",\\\\n632:    parser.add_argument(\\\\\\\"--seeds\\\\\\\", default=\\\\\\\"42,43,44\\\\\\\",\\\\n634:    parser.add_argument(\\\\\\\"--device\\\\\\\", default=\\\\\\\"cuda\\\\\\\")\\\\n635:    parser.add_argument(\\\\\\\"--max-seq-length\\\\\\\", type=int, default=2048)\\\\n636:    parser.add_argument(\\\\\\\"--n-bootstrap\\\\\\\", type=int, default=1000)\\\\n637:    parser.add_argument(\\\\\\\"--repo-size-bins\\\\\\\", default=None,\\\\n639:    parser.add_argument(\\\\\\\"--pool-size-bins\\\\\\\", default=None,\\\\n641:    parser.add_argument(\\\\\\\"--sim-bins\\\\\\\", default=None,\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"621:    parser.add_argument(\\\"--predictions-dir\\\", default=None,\\n623:    parser.add_argument(\\\"--checkpoints-dir\\\", default=None,\\n625:    parser.add_argument(\\\"--val-data-dir\\\", default=None,\\n627:    parser.add_argument(\\\"--m1-data\\\", required=True,\\n629:    parser.add_argument(\\\"--output-dir\\\", required=True)\\n630:    parser.add_argument(\\\"--dry-run\\\", action=\\\"store_true\\\",\\n632:    parser.add_argument(\\\"--seeds\\\", default=\\\"42,43,44\\\",\\n634:    parser.add_argument(\\\"--device\\\", default=\\\"cuda\\\")\\n635:    parser.add_argument(\\\"--max-seq-length\\\", type=int, default=2048)\\n636:    parser.add_argument(\\\"--n-bootstrap\\\", type=int, default=1000)\\n637:    parser.add_argument(\\\"--repo-size-bins\\\", default=None,\\n639:    parser.add_argument(\\\"--pool-size-bins\\\", default=None,\\n641:    parser.add_argument(\\\"--sim-bins\\\", default=None,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 52_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01C9NPN59ygJGUt9vcgGKChF`</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "grep -n \"dataflow\\|structural\\|neg_difficulty\\|quartile\" /root/structfuse/evaluation/analyze_stratified.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "61641136-a1cf-480b-87a5-558563742bf6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Amj9KcQjujV7Uabza8ZGC3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 237,
      "cache_read_input_tokens": 41250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 237
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

_source line 53 · 2026-05-14T20:15:52.245Z_

<details><summary>↩ Tool result · `toolu_01C9NPN59ygJGUt9vcgGKChF`</summary>

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
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "d59bbfb5-c2b4-4e3f-8967-f528497e0e44",
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

_source line 54_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_011T5MCWQmsqpydBnaXRtNQX`</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "grep -n \"dataflow\" /root/structfuse/evaluation/analyze_stratified.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "d7f42214-fc14-487a-b53f-e89d58fca341",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017QxfM5ptftQt4Bi7Grk1f7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1302,
      "cache_read_input_tokens": 41487,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1302
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

_source line 55 · 2026-05-14T20:15:57.885Z_

<details><summary>↩ Tool result · `toolu_011T5MCWQmsqpydBnaXRtNQX`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"32:STRATEGIES = [\\\"random\\\", \\\"embedding_distance\\\", \\\"dataflow_aware\\\"]\\n33:STRATEGY_LABELS = {\\\"random\\\": \\\"Random\\\", \\\"embedding_distance\\\": \\\"Embedding\\\", \\\"dataflow_aware\\\": \\\"Dataflow\\\"}\\n34:STRATEGY_COLORS = {\\\"random\\\": \\\"#4C72B0\\\", \\\"embedding_distance\\\": \\\"#DD8452\\\", \\\"dataflow_aware\\\": \\\"#55A868\\\"}\\n385:        for other in [\\\"embedding_distance\\\", \\\"dataflow_aware\\\"]:\\n531:                (\\\"dataflow_aware\\\", \\\"#55A868\\\", \\\"s\\\"),\\n591:            for other in [\\\"embedding_distance\\\", \\\"dataflow_aware\\\"]:\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "693b8e8d-9250-40cd-b88e-c95bebc8f208",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"32:STRATEGIES = [\\\\\\\"random\\\\\\\", \\\\\\\"embedding_distance\\\\\\\", \\\\\\\"dataflow_aware\\\\\\\"]\\\\n33:STRATEGY_LABELS = {\\\\\\\"random\\\\\\\": \\\\\\\"Random\\\\\\\", \\\\\\\"embedding_distance\\\\\\\": \\\\\\\"Embedding\\\\\\\", \\\\\\\"dataflow_aware\\\\\\\": \\\\\\\"Dataflow\\\\\\\"}\\\\n34:STRATEGY_COLORS = {\\\\\\\"random\\\\\\\": \\\\\\\"#4C72B0\\\\\\\", \\\\\\\"embedding_distance\\\\\\\": \\\\\\\"#DD8452\\\\\\\", \\\\\\\"dataflow_aware\\\\\\\": \\\\\\\"#55A868\\\\\\\"}\\\\n385:        for other in [\\\\\\\"embedding_distance\\\\\\\", \\\\\\\"dataflow_aware\\\\\\\"]:\\\\n531:                (\\\\\\\"dataflow_aware\\\\\\\", \\\\\\\"#55A868\\\\\\\", \\\\\\\"s\\\\\\\"),\\\\n591:            for other in [\\\\\\\"embedding_distance\\\\\\\", \\\\\\\"dataflow_aware\\\\\\\"]:\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"32:STRATEGIES = [\\\"random\\\", \\\"embedding_distance\\\", \\\"dataflow_aware\\\"]\\n33:STRATEGY_LABELS = {\\\"random\\\": \\\"Random\\\", \\\"embedding_distance\\\": \\\"Embedding\\\", \\\"dataflow_aware\\\": \\\"Dataflow\\\"}\\n34:STRATEGY_COLORS = {\\\"random\\\": \\\"#4C72B0\\\", \\\"embedding_distance\\\": \\\"#DD8452\\\", \\\"dataflow_aware\\\": \\\"#55A868\\\"}\\n385:        for other in [\\\"embedding_distance\\\", \\\"dataflow_aware\\\"]:\\n531:                (\\\"dataflow_aware\\\", \\\"#55A868\\\", \\\"s\\\"),\\n591:            for other in [\\\"embedding_distance\\\", \\\"dataflow_aware\\\"]:\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 56_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_017t2iTQsZidUFZiESP9qTGB`</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "grep -n \"neg_difficulty\" /root/structfuse/evaluation/analyze_stratified.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "eae73862-a527-4600-ab10-cfeb71d23c53",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017QxfM5ptftQt4Bi7Grk1f7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1302,
      "cache_read_input_tokens": 41487,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1302
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


### Tool call

_source line 57_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_0168CySNNonwGPFmto5raaSX`</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "grep -n \"quartile\" /root/structfuse/evaluation/analyze_stratified.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "d31367da-e48d-4b6d-a9f8-177a980444d4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017QxfM5ptftQt4Bi7Grk1f7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1302,
      "cache_read_input_tokens": 41487,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1302
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

_source line 58 · 2026-05-14T20:15:59.199Z_

<details><summary>↩ Tool result · `toolu_017t2iTQsZidUFZiESP9qTGB`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "98cfd224-e5ef-40a1-bec0-4e517abee698",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 1}, \\\"error\\\": \\\"exit code 1\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 59 · 2026-05-14T20:15:59.622Z_

<details><summary>↩ Tool result · `toolu_0168CySNNonwGPFmto5raaSX`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.41}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "9ebeeb80-e0f4-4dc9-9035-d3e731ee23df",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 1}, \\\"error\\\": \\\"exit code 1\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.41}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.41}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 60_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01XHXAFjjzLsexKKVSUqJeEq`</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "grep -n \"structural\" /root/structfuse/evaluation/analyze_stratified.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "ebc660bc-28ab-4a2f-9d65-e284a7d07309",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017QxfM5ptftQt4Bi7Grk1f7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1302,
      "cache_read_input_tokens": 41487,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1302
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

_source line 61 · 2026-05-14T20:16:00.191Z_

<details><summary>↩ Tool result · `toolu_01XHXAFjjzLsexKKVSUqJeEq`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "600369a9-3553-4d88-9de4-3904b485f052",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 1}, \\\"error\\\": \\\"exit code 1\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 62_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear picture:

**Implemented dimensions (3/5):**
1. **Repo size** (repo_size_bin) - REPO_SIZE_BINS: small/medium/large/xlarge
2. **Pool size** (pool_size_bin) - POOL_SIZE_BINS: small/medium/large
3. **Query-positive similarity** (sim_bin) - SIMILARITY_BINS: low/medium/high

**Missing dimensions (2/5):**
4. **Structural data availability** (dataflow vs fallback) - NOT implemented


5. **neg_difficulty quartile** - NOT implemented

The script supports three input modes: dry-run for mock predictions without GPU, predictions-dir to load pre-computed predictions on CPU, and checkpoints-dir to re-evaluate from checkpoints with GPU. I need to check what prediction files are available to use the CPU-only mode, examine the validation data structure to understand what fields I can work with for the missing dimensions, and see if any existing eval results contain per-instance predictions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "3e9a8dff-a9e3-4eed-86c3-e9a3cfab9b5a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TCEvtEvap2s4m21Hrpaofu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1108,
      "cache_read_input_tokens": 42789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1108
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

_source line 63_

现在清楚了脚本的维度覆盖情况。接下来查看已有的预测结果文件和 val 数据结构，以确定是否能在 CPU 上运行。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "fb8443b1-8051-4f14-96a6-f7c9030ccb01",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TCEvtEvap2s4m21Hrpaofu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1108,
      "cache_read_input_tokens": 42789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1108
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_019BmdbDq4nZEVzAKEvP2sTR`</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "ls /root/structfuse/results/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "d2f0985e-f18d-4133-8759-e392fde9b4e5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TCEvtEvap2s4m21Hrpaofu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1108,
      "cache_read_input_tokens": 42789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1108
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

_source line 65 · 2026-05-14T20:16:10.922Z_

<details><summary>↩ Tool result · `toolu_019BmdbDq4nZEVzAKEvP2sTR`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"full_z_percent_stats.json\\npilot_results.json\\npilot_results_summary.md\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "fa89447f-f73c-4eb2-bb22-00b96847a1ce",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"full_z_percent_stats.json\\\\npilot_results.json\\\\npilot_results_summary.md\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.38}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"full_z_percent_stats.json\\npilot_results.json\\npilot_results_summary.md\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 66_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_011JhGPZezVKtRGY1KMLiPG1`</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "find /root/structfuse/results -name \"*.json\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "299c760e-7582-4778-8215-708ab7101d5e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TCEvtEvap2s4m21Hrpaofu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1108,
      "cache_read_input_tokens": 42789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1108
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

_source line 67 · 2026-05-14T20:16:11.782Z_

<details><summary>↩ Tool result · `toolu_011JhGPZezVKtRGY1KMLiPG1`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/structfuse/results/pilot_results.json\\n/root/structfuse/results/full_z_percent_stats.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "122d0bdd-e519-4965-ad96-0af4655de210",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/structfuse/results/pilot_results.json\\\\n/root/structfuse/results/full_z_percent_stats.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.38}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/structfuse/results/pilot_results.json\\n/root/structfuse/results/full_z_percent_stats.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 68_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_016rknsjxkogGbZ1E3D77ZZy`</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "ls /root/autodl-tmp/structfuse/full_m2_training_data/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "48d38a06-bc73-4735-a7fe-dfd13221ee26",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TCEvtEvap2s4m21Hrpaofu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1108,
      "cache_read_input_tokens": 42789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1108
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

_source line 69 · 2026-05-14T20:16:12.559Z_

<details><summary>↩ Tool result · `toolu_016rknsjxkogGbZ1E3D77ZZy`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"dataflow_graph.json\\ntrain_bm25_s42.jsonl\\ntrain_bm25_s43.jsonl\\ntrain_bm25_s44.jsonl\\ntrain_dataflow_aware_s42.jsonl\\ntrain_dataflow_aware_s43.jsonl\\ntrain_dataflow_aware_s44.jsonl\\ntrain_embedding_distance_s42.jsonl\\ntrain_embedding_distance_s43.jsonl\\ntrain_embedding_distance_s44.jsonl\\ntrain_random_s42.jsonl\\ntrain_random_s43.jsonl\\ntrain_random_s44.jsonl\\nval_bm25_s42.jsonl\\nval_bm25_s43.jsonl\\nval_bm25_s44.jsonl\\nval_dataflow_aware_s42.jsonl\\nval_dataflow_aware_s43.jsonl\\nval_dataflow_aware_s44.jsonl\\nval_embedding_distance_s42.jsonl\\nval_embedding_distance_s43.jsonl\\nval_embedding_distance_s44.jsonl\\nval_random_s42.jsonl\\nval_random_s43.jsonl\\nval_random_s44.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "4ab98f75-9043-4af4-b254-722811ac2329",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"dataflow_graph.json\\\\ntrain_bm25_s42.jsonl\\\\ntrain_bm25_s43.jsonl\\\\ntrain_bm25_s44.jsonl\\\\ntrain_dataflow_aware_s42.jsonl\\\\ntrain_dataflow_aware_s43.jsonl\\\\ntrain_dataflow_aware_s44.jsonl\\\\ntrain_embedding_distance_s42.jsonl\\\\ntrain_embedding_distance_s43.jsonl\\\\ntrain_embedding_distance_s44.jsonl\\\\ntrain_random_s42.jsonl\\\\ntrain_random_s43.jsonl\\\\ntrain_random_s44.jsonl\\\\nval_bm25_s42.jsonl\\\\nval_bm25_s43.jsonl\\\\nval_bm25_s44.jsonl\\\\nval_dataflow_aware_s42.jsonl\\\\nval_dataflow_aware_s43.jsonl\\\\nval_dataflow_aware_s44.jsonl\\\\nval_embedding_distance_s42.jsonl\\\\nval_embedding_distance_s43.jsonl\\\\nval_embedding_distance_s44.jsonl\\\\nval_random_s42.jsonl\\\\nval_random_s43.jsonl\\\\nval_random_s44.jsonl\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"dataflow_graph.json\\ntrain_bm25_s42.jsonl\\ntrain_bm25_s43.jsonl\\ntrain_bm25_s44.jsonl\\ntrain_dataflow_aware_s42.jsonl\\ntrain_dataflow_aware_s43.jsonl\\ntrain_dataflow_aware_s44.jsonl\\ntrain_embedding_distance_s42.jsonl\\ntrain_embedding_distance_s43.jsonl\\ntrain_embedding_distance_s44.jsonl\\ntrain_random_s42.jsonl\\ntrain_random_s43.jsonl\\ntrain_random_s44.jsonl\\nval_bm25_s42.jsonl\\nval_bm25_s43.jsonl\\nval_bm25_s44.jsonl\\nval_dataflow_aware_s42.jsonl\\nval_dataflow_aware_s43.jsonl\\nval_dataflow_aware_s44.jsonl\\nval_embedding_distance_s42.jsonl\\nval_embedding_distance_s43.jsonl\\nval_embedding_distance_s44.jsonl\\nval_random_s42.jsonl\\nval_random_s43.jsonl\\nval_random_s44.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 70_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_018ySF2sVYEZnp8YpVDPjqCk`</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "find /root/autodl-tmp/structfuse -name \"per_instance*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "f887a013-7bd3-41f2-a140-23ec7e089823",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012HppokCcbREMaFWquKiSdP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1456,
      "cache_read_input_tokens": 43897,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1456
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


### Tool call

_source line 71_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Czt638wABMd9oZ52bSdLaD`</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "find /root/autodl-tmp/structfuse -name \"eval_results*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "749510da-c410-40ca-9262-1e4a3577450f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012HppokCcbREMaFWquKiSdP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1456,
      "cache_read_input_tokens": 43897,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1456
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


### Tool call

_source line 72_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01XNDtYJuHMcovVH55ep6HZQ`</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "find /root/autodl-tmp/structfuse/checkpoints -name \"*.json\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "dabc4ad2-b595-46e9-956f-bebec6363179",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012HppokCcbREMaFWquKiSdP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1456,
      "cache_read_input_tokens": 43897,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1456
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

_source line 73 · 2026-05-14T20:16:18.426Z_

<details><summary>↩ Tool result · `toolu_018ySF2sVYEZnp8YpVDPjqCk`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/structfuse/eval_results/dryrun_verify/per_instance_results.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "f83fcfd6-f9c3-41ce-8df2-2251db1a386f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/structfuse/eval_results/dryrun_verify/per_instance_results.jsonl\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.51}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/structfuse/eval_results/dryrun_verify/per_instance_results.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 74 · 2026-05-14T20:16:18.996Z_

<details><summary>↩ Tool result · `toolu_01Czt638wABMd9oZ52bSdLaD`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.56}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "a9088771-e73f-41f9-b2d1-78699cbc80c8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.56}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.56}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 75 · 2026-05-14T20:16:19.426Z_

<details><summary>↩ Tool result · `toolu_01XNDtYJuHMcovVH55ep6HZQ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_val_loss/tokenizer_config.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_val_loss/special_tokens_map.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_val_loss/added_tokens.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_val_loss/vocab.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_val_loss/tokenizer.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_val_loss/training_config.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1/tokenizer_config.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1/special_tokens_map.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1/added_tokens.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1/vocab.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1/tokenizer.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1/training_config.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_val_loss/tokenizer_config.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_val_loss/special_tokens_map.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_val_loss/added_tokens.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_val_loss/vocab.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_val_loss/tokenizer.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_val_loss/training_config.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_recall_at_1/tokenizer_config.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_recall_at_1/special_tokens_map.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_recall_at_1/added_tokens.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_recall_at_1/vocab.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_recall_at_1/tokenizer.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_recall_at_1/training_config.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_val_loss/tokenizer_config.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_val_loss/special_tokens_map.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_val_loss/added_tokens.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_val_loss/vocab.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_val_loss/tokenizer.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_val_loss/training_config.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_recall_at_1/tokenizer_config.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_recall_at_1/special_tokens_map.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_recall_at_1/added_tokens.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_recall_at_1/vocab.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_recall_at_1/tokenizer.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_recall_at_1/training_config.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_val_loss/tokenizer_config.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_val_loss/special_tokens_map.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_val_loss/vocab.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_val_loss/tokenizer.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_val_loss/training_config.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_recall_at_1/tokenizer_config.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_recall_at_1/special_tokens_map.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_recall_at_1/vocab.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_recall_at_1/tokenizer.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_recall_at_1/training_config.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "0fffb76e-66ae-4bd2-912b-06aa1f7df005",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_val_loss/tokenizer_config.json\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_val_loss/special_tokens_map.json\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_val_loss/added_tokens.json\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_val_loss/vocab.json\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_val_loss/tokenizer.json\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_val_loss/training_config.json\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1/tokenizer_config.json\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1/special_tokens_map.json\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1/added_tokens.json\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1/vocab.json\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1/tokenizer.json\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1/training_config.json\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_val_loss/tokenizer_config.json\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_val_loss/special_tokens_map.json\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_val_loss/added_tokens.json\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_val_loss/vocab.json\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_val_loss/tokenizer.json\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_val_loss/training_config.json\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_recall_at_1/tokenizer_config.json\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_recall_at_1/special_tokens_map.json\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_recall_at_1/added_tokens.json\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_recall_at_1/vocab.json\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_recall_at_1/tokenizer.json\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_recall_at_1/training_config.json\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_val_loss/tokenizer_config.json\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_val_loss/special_tokens_map.json\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_val_loss/added_tokens.json\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_val_loss/vocab.json\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_val_loss/tokenizer.json\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_val_loss/training_config.json\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_recall_at_1/tokenizer_config.json\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_recall_at_1/special_tokens_map.json\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_recall_at_1/added_tokens.json\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_recall_at_1/vocab.json\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_recall_at_1/tokenizer.json\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_recall_at_1/training_config.json\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_val_loss/tokenizer_config.json\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_val_loss/special_tokens_map.json\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_val_loss/vocab.json\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_val_loss/tokenizer.json\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_val_loss/training_config.json\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_recall_at_1/tokenizer_config.json\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_recall_at_1/special_tokens_map.json\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_recall_at_1/vocab.json\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_recall_at_1/tokenizer.json\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_recall_at_1/training_config.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.42}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_val_loss/tokenizer_config.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_val_loss/special_tokens_map.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_val_loss/added_tokens.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_val_loss/vocab.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_val_loss/tokenizer.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_val_loss/training_config.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1/tokenizer_config.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1/special_tokens_map.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1/added_tokens.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1/vocab.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1/tokenizer.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1/training_config.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_val_loss/tokenizer_config.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_val_loss/special_tokens_map.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_val_loss/added_tokens.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_val_loss/vocab.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_val_loss/tokenizer.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_val_loss/training_config.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_recall_at_1/tokenizer_config.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_recall_at_1/special_tokens_map.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_recall_at_1/added_tokens.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_recall_at_1/vocab.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_recall_at_1/tokenizer.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_recall_at_1/training_config.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_val_loss/tokenizer_config.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_val_loss/special_tokens_map.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_val_loss/added_tokens.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_val_loss/vocab.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_val_loss/tokenizer.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_val_loss/training_config.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_recall_at_1/tokenizer_config.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_recall_at_1/special_tokens_map.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_recall_at_1/added_tokens.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_recall_at_1/vocab.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_recall_at_1/tokenizer.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_recall_at_1/training_config.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_val_loss/tokenizer_config.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_val_loss/special_tokens_map.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_val_loss/vocab.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_val_loss/tokenizer.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_val_loss/training_config.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_recall_at_1/tokenizer_config.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_recall_at_1/special_tokens_map.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_recall_at_1/vocab.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_recall_at_1/tokenizer.json\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_recall_at_1/training_config.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 76_

<details><summary>Logged reasoning block</summary>

```text
The checkpoints only have `random_s42/43/44` - there are no `embedding_distance` or `dataflow_aware` checkpoints in the full_qwen dir. Let me check if there are pilot checkpoints for embedding strategies.

Also I need to check:
1. The m1 data path (for repo metadata)
2. Val data format (to understand what fields we have)
3. The m2_embed_verify pilot checkpoints
4. Whether we can use --predictions-dir with existing results

Let me also check if the script expects checkpoint dirs named like `{strategy}_s{seed}`, because the full_qwen checkpoints are only for `random`.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "0d4caae6-a90b-4d31-bcb6-98fc25079575",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UYt5XAscXDZp4zqKsT3bee",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2712,
      "cache_read_input_tokens": 45353,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2712
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

_source line 77_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01XNpuz5VbRqMz3jLkRFUTuZ`</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "ls /root/autodl-tmp/structfuse/checkpoints/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "e708d387-685f-4302-8bde-f7ad0fac64e0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UYt5XAscXDZp4zqKsT3bee",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2712,
      "cache_read_input_tokens": 45353,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2712
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

_source line 78 · 2026-05-14T20:16:27.091Z_

<details><summary>↩ Tool result · `toolu_01XNpuz5VbRqMz3jLkRFUTuZ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"m2_full_qwen\\nm2_full_starcoder\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "b02f2357-ec70-4390-a53e-ffd11847d193",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"m2_full_qwen\\\\nm2_full_starcoder\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"m2_full_qwen\\nm2_full_starcoder\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 79_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01E4oM81dNe86edGMdgeu2cm`</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "find /root/autodl-tmp/structfuse/checkpoints -maxdepth 3 -type d"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "ad4ca5c4-4606-432b-8d93-e560b32f1654",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UYt5XAscXDZp4zqKsT3bee",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2712,
      "cache_read_input_tokens": 45353,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2712
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

_source line 80 · 2026-05-14T20:16:28.126Z_

<details><summary>↩ Tool result · `toolu_01E4oM81dNe86edGMdgeu2cm`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/structfuse/checkpoints\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_val_loss\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_val_loss\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_recall_at_1\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_val_loss\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_recall_at_1\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_val_loss\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_recall_at_1\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s43\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "23a55489-bac1-421f-a704-8a6559d1b8c1",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/structfuse/checkpoints\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_val_loss\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_val_loss\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_recall_at_1\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_val_loss\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_recall_at_1\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_val_loss\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_recall_at_1\\\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s43\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/structfuse/checkpoints\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_val_loss\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_val_loss\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s43/best_by_recall_at_1\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_val_loss\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s44/best_by_recall_at_1\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_val_loss\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_recall_at_1\\n/root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s43\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 81_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_014qXPQv13wsR469K27wb4LT`</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "head -1 /root/autodl-tmp/structfuse/full_m2_training_data/val_random_s42.jsonl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "d1d7ee5d-85ff-4181-b90d-3306cffe89b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UYt5XAscXDZp4zqKsT3bee",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2712,
      "cache_read_input_tokens": 45353,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2712
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

_source line 82 · 2026-05-14T20:16:28.949Z_

<details><summary>↩ Tool result · `toolu_014qXPQv13wsR469K27wb4LT`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"query_id\\\": \\\"pyparsing__pyparsing.533adf47.combine_file__b756s2rd::pyparsing/helpers.py\\\", \\\"query_tokens\\\": \\\"# helpers.py\\\\nimport html.entities\\\\nimport operator\\\\nimport re\\\\nimport sys\\\\nimport typing\\\\n\\\\nfrom . import __diag__\\\\nfrom .core import *\\\\nfrom .util import (\\\\n    _bslash,\\\\n    _flatten,\\\\n    _escape_regex_range_chars,\\\\n    make_compressed_re,\\\\n    replaced_by_pep8,\\\\n)\\\\n\\\\n\\\\n#\\\\n# global helpers\\\\n#\\\\ndef counted_array(\\\\n    expr: ParserElement,\\\\n    int_expr: typing.Optional[ParserElement] = None,\\\\n    *,\\\\n    intExpr: typing.Optional[ParserElement] = None,\\\\n) -> ParserElement:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Helper to define a counted list of expressions.\\\\n\\\\n    This helper defines a pattern of the form::\\\\n\\\\n        integer expr expr expr...\\\\n\\\\n    where the leading integer tells how many expr expressions follow.\\\\n    The matched tokens returns the array of expr tokens as a list - the\\\\n    leading count token is suppressed.\\\\n\\\\n    If ``int_expr`` is specified, it should be a pyparsing expression\\\\n    that produces an integer value.\\\\n\\\\n    Example::\\\\n\\\\n        counted_array(Word(alphas)).parse_string('2 ab cd ef')  # -> ['ab', 'cd']\\\\n\\\\n        # in this parser, the leading integer value is given in binary,\\\\n        # '10' indicating that 2 values are in the array\\\\n        binary_constant = Word('01').set_parse_action(lambda t: int(t[0], 2))\\\\n        counted_array(Word(alphas), int_expr=binary_constant).parse_string('10 ab cd ef')  # -> ['ab', 'cd']\\\\n\\\\n        # if other fields must be parsed after the count but before the\\\\n        # list items, give the fields results names and they will\\\\n        # be preserved in the returned ParseResults:\\\\n        count_with_metadata = integer + Word(alphas)(\\\\\\\"type\\\\\\\")\\\\n        typed_array = counted_array(Word(alphanums), int_expr=count_with_metadata)(\\\\\\\"items\\\\\\\")\\\\n        result = typed_array.parse_string(\\\\\\\"3 bool True True False\\\\\\\")\\\\n        print(result.dump())\\\\n\\\\n        # prints\\\\n        # ['True', 'True', 'False']\\\\n        # - items: ['True', 'True', 'False']\\\\n        # - type: 'bool'\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"\\\\n    intExpr = intExpr or int_expr\\\\n    array_expr = Forward()\\\\n\\\\n    def count_field_parse_action(s, l, t):\\\\n        nonlocal array_expr\\\\n        n = t[0]\\\\n        array_expr <<= (expr * n) if n else Empty()\\\\n        # clear list contents, but keep any named results\\\\n        del t[:]\\\\n\\\\n    if intExpr is None:\\\\n        intExpr = Word(nums).set_parse_action(lambda t: int(t[0]))\\\\n    else:\\\\n        intExpr = intExpr.copy()\\\\n    intExpr.set_name(\\\\\\\"arrayLen\\\\\\\")\\\\n    intExpr.add_parse_action(count_field_parse_action, call_during_try=True)\\\\n    return (intExpr + array_expr).set_name(f\\\\\\\"(len) {expr}...\\\\\\\")\\\\n\\\\n\\\\ndef match_previous_literal(expr: ParserElement) -> ParserElement:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Helper to define an expression that is indirectly defined from\\\\n    the tokens matched in a previous expression, that is, it looks for\\\\n    a 'repeat' of a previous expression.  For example::\\\\n\\\\n        first = Word(nums)\\\\n        second = match_previous_literal(first)\\\\n        match_expr = first + \\\\\\\":\\\\\\\" + second\\\\n\\\\n    will match ``\\\\\\\"1:1\\\\\\\"``, but not ``\\\\\\\"1:2\\\\\\\"``.  Because this\\\\n    matches a previous literal, will also match the leading\\\\n    ``\\\\\\\"1:1\\\\\\\"`` in ``\\\\\\\"1:10\\\\\\\"``. If this is not desired, use\\\\n    :class:`match_previous_expr`. Do *not* use with packrat parsing\\\\n    enabled.\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"\\\\n    rep = Forward()\\\\n\\\\n    def copy_token_to_repeater(s, l, t):\\\\n        if not t:\\\\n            rep << Empty()\\\\n            return\\\\n\\\\n        if len(t) == 1:\\\\n            rep << t[0]\\\\n            return\\\\n\\\\n        # flatten t tokens\\\\n        tflat = _flatten(t.as_list())\\\\n        rep << And(Literal(tt) for tt in tflat)\\\\n\\\\n    expr.add_parse_action(copy_token_to_repeater, callDuringTry=True)\\\\n    rep.set_name(\\\\\\\"(prev) \\\\\\\" + str(expr))\\\\n    return rep\\\\n\\\\n\\\\ndef match_previous_expr(expr: ParserElement) -> ParserElement:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Helper to define an expression that is indirectly defined from\\\\n    the tokens matched in a previous expression, that is, it loo\\n\\n... [截断: 输出过长，省略 167952 字符] ...\\n\\nmap(pp.Suppress, \\\\\\\",(){}=;\\\\\\\")\\\\n\\\\n# keywords\\\\n(CLASS, FUN, VAR, FOR, IF, ELSE, PRINT, RETURN, WHILE,\\\\n TRUE, FALSE, NIL, THIS, SUPER, AND, OR) = pp.Keyword.using_each(\\\\n    \\\\\\\"class fun var for if else print return while\\\\\\\"\\\\n    \\\\\\\" true false nil this super and or\\\\\\\".split()\\\\n)\\\\n\\\\nidentifier = pp.Word(pp.alphas + \\\\\\\"_\\\\\\\", pp.alphanums + \\\\\\\"_'\\\\\\\")\\\\nstring = pp.QuotedString('\\\\\\\"')\\\\nnumber = pp.Regex(r\\\\\\\"\\\\\\\\d+(?:\\\\\\\\.\\\\\\\\d+)?\\\\\\\")\\\\n\\\\ndeclaration = pp.Forward()\\\\nstatement = pp.Forward()\\\\nclass_decl = pp.Forward()\\\\nexpression = pp.Forward()\\\\nblock = pp.Forward()\\\\n\\\\narguments = pp.DelimitedList(expression)\\\\nparameters = pp.DelimitedList(identifier)\\\\nfunction = identifier + LPAR + pp.Opt(parameters) + RPAR + block\\\\nproperty_ = identifier + block\\\\n\\\\nfun_decl = FUN + function\\\\nvar_decl = VAR + identifier + pp.Opt(EQ + expression) + SEMI\\\\nclass_decl <<= (\\\\n        CLASS\\\\n        - identifier\\\\n        + pp.Opt(\\\\\\\"<\\\\\\\" + identifier)\\\\n        + LBRACE\\\\n        + (function | property_ | class_decl)[...]\\\\n        + RBRACE\\\\n)\\\\n\\\\n\\\\nprimary = (TRUE | FALSE | NIL | THIS | number | string | identifier\\\\n           | SUPER + \\\\\\\".\\\\\\\" + identifier\\\\n           # | LPAR + expression + RPAR  <-- not needed, infix_notation takes care of this\\\\n           ).set_name(\\\\\\\"primary\\\\\\\")\\\\ncall = primary + (\\\\n        LPAR + pp.Opt(arguments) + RPAR\\\\n        | \\\\\\\".\\\\\\\" + identifier\\\\n)[1, ...]\\\\n\\\\narith_expression = pp.infix_notation(\\\\n    (call | primary).set_name(\\\\\\\"arith_operand\\\\\\\"),\\\\n    [\\\\n        (pp.one_of(\\\\\\\"! -\\\\\\\"), 1, pp.opAssoc.RIGHT),\\\\n        (pp.one_of(\\\\\\\"/ *\\\\\\\"), 2, pp.opAssoc.LEFT),\\\\n        (pp.one_of(\\\\\\\"- +\\\\\\\"), 2, pp.opAssoc.LEFT),\\\\n        (pp.one_of(\\\\\\\"> >= < <=\\\\\\\"), 2, pp.opAssoc.LEFT),\\\\n        (pp.one_of(\\\\\\\"!= ==\\\\\\\"), 2, pp.opAssoc.LEFT),\\\\n        (AND, 2, pp.opAssoc.LEFT),\\\\n        (OR, 2, pp.opAssoc.LEFT),\\\\n    ]\\\\n)\\\\nassignment = pp.Forward()\\\\nassignment <<= (call | identifier) + EQ + (assignment | arith_expression)\\\\n\\\\nexpression <<= assignment ^ arith_expression ^ function\\\\n\\\\nblock <<= pp.Group(LBRACE + declaration[...] + RBRACE)\\\\nwhile_statement = WHILE + LPAR + expression + RPAR + statement\\\\nreturn_statement = RETURN + pp.Opt(expression) + SEMI\\\\nprint_statement = PRINT + expression + SEMI\\\\nif_statement = IF + LPAR + expression + RPAR + statement + pp.Opt(ELSE + statement)\\\\nexpr_statement = expression + \\\\\\\";\\\\\\\"\\\\nfor_statement = FOR + LPAR + pp.Group(\\\\n    (var_decl | expr_statement | \\\\\\\";\\\\\\\")\\\\n    + pp.Opt(expression) + \\\\\\\";\\\\\\\"\\\\n    + pp.Opt(expression)\\\\n) + RPAR + statement\\\\n\\\\n\\\\nstatement <<= pp.Group(\\\\n    expr_statement\\\\n    | for_statement\\\\n    | if_statement\\\\n    | print_statement\\\\n    | return_statement\\\\n    | while_statement\\\\n    | block\\\\n)\\\\n\\\\ndeclaration <<= (\\\\n    class_decl\\\\n    | fun_decl\\\\n    | var_decl\\\\n    | statement\\\\n)\\\\n\\\\nprogram = declaration[...]\\\\nprogram.ignore(pp.dbl_slash_comment)\\\\n\\\\n# define names so that we get a better diagram\\\\npp.autoname_elements()\\\\n\\\\n\\\\ndef main():\\\\n    import textwrap\\\\n\\\\n    success, _ = program.run_tests(\\\\n        textwrap.dedent(t) for t in [\\\\n            \\\\\\\"\\\\\\\"\\\\\\\"\\\\\\\\\\\\n                var a = 1;\\\\n                {\\\\n                  var a = a + 2;\\\\n                  print a;\\\\n                }\\\\n                \\\\\\\"\\\\\\\"\\\\\\\",\\\\n            \\\\\\\"\\\\\\\"\\\\\\\"\\\\\\\\\\\\n                {\\\\n                  var i = 0;\\\\n                  while (i < 10) {\\\\n                    print i;\\\\n                    i = i + 1;\\\\n                  }\\\\n                }\\\\n            \\\\\\\"\\\\\\\"\\\\\\\",\\\\n            \\\\\\\"\\\\\\\"\\\\\\\"\\\\\\\\\\\\n                var a = 0;\\\\n                var temp;\\\\n                \\\\n                for (var b = 1; a < 10000; b = temp + b) {\\\\n                  print a;\\\\n                  temp = a;\\\\n                  a = b;\\\\n                }\\\\n            \\\\\\\"\\\\\\\"\\\\\\\",\\\\n            \\\\\\\"\\\\\\\"\\\\\\\"\\\\\\\\\\\\n                fun add(a, b, c) {\\\\n                  print a + b + c;\\\\n                }\\\\n                \\\\n                add(1, 2, 3);\\\\n            \\\\\\\"\\\\\\\"\\\\\\\",\\\\n            \\\\\\\"\\\\\\\"\\\\\\\"\\\\\\\\\\\\n                fun count(n) {\\\\n                  while (n < 100) {\\\\n                    if (n == 3) return n; // <--\\\\n  \\\"}}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.55}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "b8d24e07-0511-416d-8409-55f3937acc76",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\\\\"query_id\\\\\\\": \\\\\\\"pyparsing__pyparsing.533adf47.combine_file__b756s2rd::pyparsing/helpers.py\\\\\\\", \\\\\\\"query_tokens\\\\\\\": \\\\\\\"# helpers.py\\\\\\\\nimport html.entities\\\\\\\\nimport operator\\\\\\\\nimport re\\\\\\\\nimport sys\\\\\\\\nimport typing\\\\\\\\n\\\\\\\\nfrom . import __diag__\\\\\\\\nfrom .core import *\\\\\\\\nfrom .util import (\\\\\\\\n    _bslash,\\\\\\\\n    _flatten,\\\\\\\\n    _escape_regex_range_chars,\\\\\\\\n    make_compressed_re,\\\\\\\\n    replaced_by_pep8,\\\\\\\\n)\\\\\\\\n\\\\\\\\n\\\\\\\\n#\\\\\\\\n# global helpers\\\\\\\\n#\\\\\\\\ndef counted_array(\\\\\\\\n    expr: ParserElement,\\\\\\\\n    int_expr: typing.Optional[ParserElement] = None,\\\\\\\\n    *,\\\\\\\\n    intExpr: typing.Optional[ParserElement] = None,\\\\\\\\n) -> ParserElement:\\\\\\\\n    \\\\\\\\\\\\\\\"\\\\\\\\\\\\\\\"\\\\\\\\\\\\\\\"Helper to define a counted list of expressions.\\\\\\\\n\\\\\\\\n    This helper defines a pattern of the form::\\\\\\\\n\\\\\\\\n        integer expr expr expr...\\\\\\\\n\\\\\\\\n    where the leading integer tells how many expr expressions follow.\\\\\\\\n    The matched tokens returns the array of expr tokens as a list - the\\\\\\\\n    leading count token is suppressed.\\\\\\\\n\\\\\\\\n    If ``int_expr`` is specified, it should be a pyparsing expression\\\\\\\\n    that produces an integer value.\\\\\\\\n\\\\\\\\n    Example::\\\\\\\\n\\\\\\\\n        counted_array(Word(alphas)).parse_string('2 ab cd ef')  # -> ['ab', 'cd']\\\\\\\\n\\\\\\\\n        # in this parser, the leading integer value is given in binary,\\\\\\\\n        # '10' indicating that 2 values are in the array\\\\\\\\n        binary_constant = Word('01').set_parse_action(lambda t: int(t[0], 2))\\\\\\\\n        counted_array(Word(alphas), int_expr=binary_constant).parse_string('10 ab cd ef')  # -> ['ab', 'cd']\\\\\\\\n\\\\\\\\n        # if other fields must be parsed after the count but before the\\\\\\\\n        # list items, give the fields results names and they will\\\\\\\\n        # be preserved in the returned ParseResults:\\\\\\\\n        count_with_metadata = integer + Word(alphas)(\\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\\")\\\\\\\\n        typed_array = counted_array(Word(alphanums), int_expr=count_with_metadata)(\\\\\\\\\\\\\\\"items\\\\\\\\\\\\\\\")\\\\\\\\n        result = typed_array.parse_string(\\\\\\\\\\\\\\\"3 bool True True False\\\\\\\\\\\\\\\")\\\\\\\\n        print(result.dump())\\\\\\\\n\\\\\\\\n        # prints\\\\\\\\n        # ['True', 'True', 'False']\\\\\\\\n        # - items: ['True', 'True', 'False']\\\\\\\\n        # - type: 'bool'\\\\\\\\n    \\\\\\\\\\\\\\\"\\\\\\\\\\\\\\\"\\\\\\\\\\\\\\\"\\\\\\\\n    intExpr = intExpr or int_expr\\\\\\\\n    array_expr = Forward()\\\\\\\\n\\\\\\\\n    def count_field_parse_action(s, l, t):\\\\\\\\n        nonlocal array_expr\\\\\\\\n        n = t[0]\\\\\\\\n        array_expr <<= (expr * n) if n else Empty()\\\\\\\\n        # clear list contents, but keep any named results\\\\\\\\n        del t[:]\\\\\\\\n\\\\\\\\n    if intExpr is None:\\\\\\\\n        intExpr = Word(nums).set_parse_action(lambda t: int(t[0]))\\\\\\\\n    else:\\\\\\\\n        intExpr = intExpr.copy()\\\\\\\\n    intExpr.set_name(\\\\\\\\\\\\\\\"arrayLen\\\\\\\\\\\\\\\")\\\\\\\\n    intExpr.add_parse_action(count_field_parse_action, call_during_try=True)\\\\\\\\n    return (intExpr + array_expr).set_name(f\\\\\\\\\\\\\\\"(len) {expr}...\\\\\\\\\\\\\\\")\\\\\\\\n\\\\\\\\n\\\\\\\\ndef match_previous_literal(expr: ParserElement) -> ParserElement:\\\\\\\\n    \\\\\\\\\\\\\\\"\\\\\\\\\\\\\\\"\\\\\\\\\\\\\\\"Helper to define an expression that is indirectly defined from\\\\\\\\n    the tokens matched in a previous expression, that is, it looks for\\\\\\\\n    a 'repeat' of a previous expression.  For example::\\\\\\\\n\\\\\\\\n        first = Word(nums)\\\\\\\\n        second = match_previous_literal(first)\\\\\\\\n        match_expr = first + \\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\" + second\\\\\\\\n\\\\\\\\n    will match ``\\\\\\\\\\\\\\\"1:1\\\\\\\\\\\\\\\"``, but not ``\\\\\\\\\\\\\\\"1:2\\\\\\\\\\\\\\\"``.  Because this\\\\\\\\n    matches a previous literal, will also match the leading\\\\\\\\n    ``\\\\\\\\\\\\\\\"1:1\\\\\\\\\\\\\\\"`` in ``\\\\\\\\\\\\\\\"1:10\\\\\\\\\\\\\\\"``. If this is not desired, use\\\\\\\\n    :class:`match_previous_expr`. Do *not* use with packrat parsing\\\\\\\\n    enabled.\\\\\\\\n    \\\\\\\\\\\\\\\"\\\\\\\\\\\\\\\"\\\\\\\\\\\\\\\"\\\\\\\\n    rep = Forward()\\\\\\\\n\\\\\\\\n    def copy_token_to_repeater(s, l, t):\\\\\\\\n        if not t:\\\\\\\\n            rep << Empty()\\\\\\\\n            return\\\\\\\\n\\\\\\\\n        if len(t) == 1:\\\\\\\\n            rep << t[0]\\\\\\\\n            return\\\\\\\\n\\\\\\\\n        # flatten t tokens\\\\\\\\n        tflat = _flatten(t.as_list())\\\\\\\\n        rep << And(Literal(tt) for tt in tflat)\\\\\\\\n\\\\\\\\n    expr.add_parse_action(copy_token_to_repeater, callDuringTry=True)\\\\\\\\n    rep.set_name(\\\\\\\\\\\\\\\"(prev) \\\\\\\\\\\\\\\" + str(expr))\\\\\\\\n    return rep\\\\\\\\n\\\\\\\\n\\\\\\\\ndef match_previous_expr(expr: ParserElement) -> ParserElement:\\\\\\\\n    \\\\\\\\\\\\\\\"\\\\\\\\\\\\\\\"\\\\\\\\\\\\\\\"Helper to define an expression that is indirectly defined from\\\\\\\\n    the tokens matched in a previous expression, that is, it loo\\\\n\\\\n... [截断: 输出过长，省略 167952 字符] ...\\\\n\\\\nmap(pp.Suppress, \\\\\\\\\\\\\\\",(){}=;\\\\\\\\\\\\\\\")\\\\\\\\n\\\\\\\\n# keywords\\\\\\\\n(CLASS, FUN, VAR, FOR, IF, ELSE, PRINT, RETURN, WHILE,\\\\\\\\n TRUE, FALSE, NIL, THIS, SUPER, AND, OR) = pp.Keyword.using_each(\\\\\\\\n    \\\\\\\\\\\\\\\"class fun var for if else print return while\\\\\\\\\\\\\\\"\\\\\\\\n    \\\\\\\\\\\\\\\" true false nil this super and or\\\\\\\\\\\\\\\".split()\\\\\\\\n)\\\\\\\\n\\\\\\\\nidentifier = pp.Word(pp.alphas + \\\\\\\\\\\\\\\"_\\\\\\\\\\\\\\\", pp.alphanums + \\\\\\\\\\\\\\\"_'\\\\\\\\\\\\\\\")\\\\\\\\nstring = pp.QuotedString('\\\\\\\\\\\\\\\"')\\\\\\\\nnumber = pp.Regex(r\\\\\\\\\\\\\\\"\\\\\\\\\\\\\\\\d+(?:\\\\\\\\\\\\\\\\.\\\\\\\\\\\\\\\\d+)?\\\\\\\\\\\\\\\")\\\\\\\\n\\\\\\\\ndeclaration = pp.Forward()\\\\\\\\nstatement = pp.Forward()\\\\\\\\nclass_decl = pp.Forward()\\\\\\\\nexpression = pp.Forward()\\\\\\\\nblock = pp.Forward()\\\\\\\\n\\\\\\\\narguments = pp.DelimitedList(expression)\\\\\\\\nparameters = pp.DelimitedList(identifier)\\\\\\\\nfunction = identifier + LPAR + pp.Opt(parameters) + RPAR + block\\\\\\\\nproperty_ = identifier + block\\\\\\\\n\\\\\\\\nfun_decl = FUN + function\\\\\\\\nvar_decl = VAR + identifier + pp.Opt(EQ + expression) + SEMI\\\\\\\\nclass_decl <<= (\\\\\\\\n        CLASS\\\\\\\\n        - identifier\\\\\\\\n        + pp.Opt(\\\\\\\\\\\\\\\"<\\\\\\\\\\\\\\\" + identifier)\\\\\\\\n        + LBRACE\\\\\\\\n        + (function | property_ | class_decl)[...]\\\\\\\\n        + RBRACE\\\\\\\\n)\\\\\\\\n\\\\\\\\n\\\\\\\\nprimary = (TRUE | FALSE | NIL | THIS | number | string | identifier\\\\\\\\n           | SUPER + \\\\\\\\\\\\\\\".\\\\\\\\\\\\\\\" + identifier\\\\\\\\n           # | LPAR + expression + RPAR  <-- not needed, infix_notation takes care of this\\\\\\\\n           ).set_name(\\\\\\\\\\\\\\\"primary\\\\\\\\\\\\\\\")\\\\\\\\ncall = primary + (\\\\\\\\n        LPAR + pp.Opt(arguments) + RPAR\\\\\\\\n        | \\\\\\\\\\\\\\\".\\\\\\\\\\\\\\\" + identifier\\\\\\\\n)[1, ...]\\\\\\\\n\\\\\\\\narith_expression = pp.infix_notation(\\\\\\\\n    (call | primary).set_name(\\\\\\\\\\\\\\\"arith_operand\\\\\\\\\\\\\\\"),\\\\\\\\n    [\\\\\\\\n        (pp.one_of(\\\\\\\\\\\\\\\"! -\\\\\\\\\\\\\\\"), 1, pp.opAssoc.RIGHT),\\\\\\\\n        (pp.one_of(\\\\\\\\\\\\\\\"/ *\\\\\\\\\\\\\\\"), 2, pp.opAssoc.LEFT),\\\\\\\\n        (pp.one_of(\\\\\\\\\\\\\\\"- +\\\\\\\\\\\\\\\"), 2, pp.opAssoc.LEFT),\\\\\\\\n        (pp.one_of(\\\\\\\\\\\\\\\"> >= < <=\\\\\\\\\\\\\\\"), 2, pp.opAssoc.LEFT),\\\\\\\\n        (pp.one_of(\\\\\\\\\\\\\\\"!= ==\\\\\\\\\\\\\\\"), 2, pp.opAssoc.LEFT),\\\\\\\\n        (AND, 2, pp.opAssoc.LEFT),\\\\\\\\n        (OR, 2, pp.opAssoc.LEFT),\\\\\\\\n    ]\\\\\\\\n)\\\\\\\\nassignment = pp.Forward()\\\\\\\\nassignment <<= (call | identifier) + EQ + (assignment | arith_expression)\\\\\\\\n\\\\\\\\nexpression <<= assignment ^ arith_expression ^ function\\\\\\\\n\\\\\\\\nblock <<= pp.Group(LBRACE + declaration[...] + RBRACE)\\\\\\\\nwhile_statement = WHILE + LPAR + expression + RPAR + statement\\\\\\\\nreturn_statement = RETURN + pp.Opt(expression) + SEMI\\\\\\\\nprint_statement = PRINT + expression + SEMI\\\\\\\\nif_statement = IF + LPAR + expression + RPAR + statement + pp.Opt(ELSE + statement)\\\\\\\\nexpr_statement = expression + \\\\\\\\\\\\\\\";\\\\\\\\\\\\\\\"\\\\\\\\nfor_statement = FOR + LPAR + pp.Group(\\\\\\\\n    (var_decl | expr_statement | \\\\\\\\\\\\\\\";\\\\\\\\\\\\\\\")\\\\\\\\n    + pp.Opt(expression) + \\\\\\\\\\\\\\\";\\\\\\\\\\\\\\\"\\\\\\\\n    + pp.Opt(expression)\\\\\\\\n) + RPAR + statement\\\\\\\\n\\\\\\\\n\\\\\\\\nstatement <<= pp.Group(\\\\\\\\n    expr_statement\\\\\\\\n    | for_statement\\\\\\\\n    | if_statement\\\\\\\\n    | print_statement\\\\\\\\n    | return_statement\\\\\\\\n    | while_statement\\\\\\\\n    | block\\\\\\\\n)\\\\\\\\n\\\\\\\\ndeclaration <<= (\\\\\\\\n    class_decl\\\\\\\\n    | fun_decl\\\\\\\\n    | var_decl\\\\\\\\n    | statement\\\\\\\\n)\\\\\\\\n\\\\\\\\nprogram = declaration[...]\\\\\\\\nprogram.ignore(pp.dbl_slash_comment)\\\\\\\\n\\\\\\\\n# define names so that we get a better diagram\\\\\\\\npp.autoname_elements()\\\\\\\\n\\\\\\\\n\\\\\\\\ndef main():\\\\\\\\n    import textwrap\\\\\\\\n\\\\\\\\n    success, _ = program.run_tests(\\\\\\\\n        textwrap.dedent(t) for t in [\\\\\\\\n            \\\\\\\\\\\\\\\"\\\\\\\\\\\\\\\"\\\\\\\\\\\\\\\"\\\\\\\\\\\\\\\\\\\\\\\\n                var a = 1;\\\\\\\\n                {\\\\\\\\n                  var a = a + 2;\\\\\\\\n                  print a;\\\\\\\\n                }\\\\\\\\n                \\\\\\\\\\\\\\\"\\\\\\\\\\\\\\\"\\\\\\\\\\\\\\\",\\\\\\\\n            \\\\\\\\\\\\\\\"\\\\\\\\\\\\\\\"\\\\\\\\\\\\\\\"\\\\\\\\\\\\\\\\\\\\\\\\n                {\\\\\\\\n                  var i = 0;\\\\\\\\n                  while (i < 10) {\\\\\\\\n                    print i;\\\\\\\\n                    i = i + 1;\\\\\\\\n                  }\\\\\\\\n                }\\\\\\\\n            \\\\\\\\\\\\\\\"\\\\\\\\\\\\\\\"\\\\\\\\\\\\\\\",\\\\\\\\n            \\\\\\\\\\\\\\\"\\\\\\\\\\\\\\\"\\\\\\\\\\\\\\\"\\\\\\\\\\\\\\\\\\\\\\\\n                var a = 0;\\\\\\\\n                var temp;\\\\\\\\n                \\\\\\\\n                for (var b = 1; a < 10000; b = temp + b) {\\\\\\\\n                  print a;\\\\\\\\n                  temp = a;\\\\\\\\n                  a = b;\\\\\\\\n                }\\\\\\\\n            \\\\\\\\\\\\\\\"\\\\\\\\\\\\\\\"\\\\\\\\\\\\\\\",\\\\\\\\n            \\\\\\\\\\\\\\\"\\\\\\\\\\\\\\\"\\\\\\\\\\\\\\\"\\\\\\\\\\\\\\\\\\\\\\\\n                fun add(a, b, c) {\\\\\\\\n                  print a + b + c;\\\\\\\\n                }\\\\\\\\n                \\\\\\\\n                add(1, 2, 3);\\\\\\\\n            \\\\\\\\\\\\\\\"\\\\\\\\\\\\\\\"\\\\\\\\\\\\\\\",\\\\\\\\n            \\\\\\\\\\\\\\\"\\\\\\\\\\\\\\\"\\\\\\\\\\\\\\\"\\\\\\\\\\\\\\\\\\\\\\\\n                fun count(n) {\\\\\\\\n                  while (n < 100) {\\\\\\\\n                    if (n == 3) return n; // <--\\\\\\\\n  \\\\\\\"}}\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.55}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\\"query_id\\\": \\\"pyparsing__pyparsing.533adf47.combine_file__b756s2rd::pyparsing/helpers.py\\\", \\\"query_tokens\\\": \\\"# helpers.py\\\\nimport html.entities\\\\nimport operator\\\\nimport re\\\\nimport sys\\\\nimport typing\\\\n\\\\nfrom . import __diag__\\\\nfrom .core import *\\\\nfrom .util import (\\\\n    _bslash,\\\\n    _flatten,\\\\n    _escape_regex_range_chars,\\\\n    make_compressed_re,\\\\n    replaced_by_pep8,\\\\n)\\\\n\\\\n\\\\n#\\\\n# global helpers\\\\n#\\\\ndef counted_array(\\\\n    expr: ParserElement,\\\\n    int_expr: typing.Optional[ParserElement] = None,\\\\n    *,\\\\n    intExpr: typing.Optional[ParserElement] = None,\\\\n) -> ParserElement:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Helper to define a counted list of expressions.\\\\n\\\\n    This helper defines a pattern of the form::\\\\n\\\\n        integer expr expr expr...\\\\n\\\\n    where the leading integer tells how many expr expressions follow.\\\\n    The matched tokens returns the array of expr tokens as a list - the\\\\n    leading count token is suppressed.\\\\n\\\\n    If ``int_expr`` is specified, it should be a pyparsing expression\\\\n    that produces an integer value.\\\\n\\\\n    Example::\\\\n\\\\n        counted_array(Word(alphas)).parse_string('2 ab cd ef')  # -> ['ab', 'cd']\\\\n\\\\n        # in this parser, the leading integer value is given in binary,\\\\n        # '10' indicating that 2 values are in the array\\\\n        binary_constant = Word('01').set_parse_action(lambda t: int(t[0], 2))\\\\n        counted_array(Word(alphas), int_expr=binary_constant).parse_string('10 ab cd ef')  # -> ['ab', 'cd']\\\\n\\\\n        # if other fields must be parsed after the count but before the\\\\n        # list items, give the fields results names and they will\\\\n        # be preserved in the returned ParseResults:\\\\n        count_with_metadata = integer + Word(alphas)(\\\\\\\"type\\\\\\\")\\\\n        typed_array = counted_array(Word(alphanums), int_expr=count_with_metadata)(\\\\\\\"items\\\\\\\")\\\\n        result = typed_array.parse_string(\\\\\\\"3 bool True True False\\\\\\\")\\\\n        print(result.dump())\\\\n\\\\n        # prints\\\\n        # ['True', 'True', 'False']\\\\n        # - items: ['True', 'True', 'False']\\\\n        # - type: 'bool'\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"\\\\n    intExpr = intExpr or int_expr\\\\n    array_expr = Forward()\\\\n\\\\n    def count_field_parse_action(s, l, t):\\\\n        nonlocal array_expr\\\\n        n = t[0]\\\\n        array_expr <<= (expr * n) if n else Empty()\\\\n        # clear list contents, but keep any named results\\\\n        del t[:]\\\\n\\\\n    if intExpr is None:\\\\n        intExpr = Word(nums).set_parse_action(lambda t: int(t[0]))\\\\n    else:\\\\n        intExpr = intExpr.copy()\\\\n    intExpr.set_name(\\\\\\\"arrayLen\\\\\\\")\\\\n    intExpr.add_parse_action(count_field_parse_action, call_during_try=True)\\\\n    return (intExpr + array_expr).set_name(f\\\\\\\"(len) {expr}...\\\\\\\")\\\\n\\\\n\\\\ndef match_previous_literal(expr: ParserElement) -> ParserElement:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Helper to define an expression that is indirectly defined from\\\\n    the tokens matched in a previous expression, that is, it looks for\\\\n    a 'repeat' of a previous expression.  For example::\\\\n\\\\n        first = Word(nums)\\\\n        second = match_previous_literal(first)\\\\n        match_expr = first + \\\\\\\":\\\\\\\" + second\\\\n\\\\n    will match ``\\\\\\\"1:1\\\\\\\"``, but not ``\\\\\\\"1:2\\\\\\\"``.  Because this\\\\n    matches a previous literal, will also match the leading\\\\n    ``\\\\\\\"1:1\\\\\\\"`` in ``\\\\\\\"1:10\\\\\\\"``. If this is not desired, use\\\\n    :class:`match_previous_expr`. Do *not* use with packrat parsing\\\\n    enabled.\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"\\\\n    rep = Forward()\\\\n\\\\n    def copy_token_to_repeater(s, l, t):\\\\n        if not t:\\\\n            rep << Empty()\\\\n            return\\\\n\\\\n        if len(t) == 1:\\\\n            rep << t[0]\\\\n            return\\\\n\\\\n        # flatten t tokens\\\\n        tflat = _flatten(t.as_list())\\\\n        rep << And(Literal(tt) for tt in tflat)\\\\n\\\\n    expr.add_parse_action(copy_token_to_repeater, callDuringTry=True)\\\\n    rep.set_name(\\\\\\\"(prev) \\\\\\\" + str(expr))\\\\n    return rep\\\\n\\\\n\\\\ndef match_previous_expr(expr: ParserElement) -> ParserElement:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Helper to define an expression that is indirectly defined from\\\\n    the tokens matched in a previous expression, that is, it loo\\n\\n... [截断: 输出过长，省略 167952 字符] ...\\n\\nmap(pp.Suppress, \\\\\\\",(){}=;\\\\\\\")\\\\n\\\\n# keywords\\\\n(CLASS, FUN, VAR, FOR, IF, ELSE, PRINT, RETURN, WHILE,\\\\n TRUE, FALSE, NIL, THIS, SUPER, AND, OR) = pp.Keyword.using_each(\\\\n    \\\\\\\"class fun var for if else print return while\\\\\\\"\\\\n    \\\\\\\" true false nil this super and or\\\\\\\".split()\\\\n)\\\\n\\\\nidentifier = pp.Word(pp.alphas + \\\\\\\"_\\\\\\\", pp.alphanums + \\\\\\\"_'\\\\\\\")\\\\nstring = pp.QuotedString('\\\\\\\"')\\\\nnumber = pp.Regex(r\\\\\\\"\\\\\\\\d+(?:\\\\\\\\.\\\\\\\\d+)?\\\\\\\")\\\\n\\\\ndeclaration = pp.Forward()\\\\nstatement = pp.Forward()\\\\nclass_decl = pp.Forward()\\\\nexpression = pp.Forward()\\\\nblock = pp.Forward()\\\\n\\\\narguments = pp.DelimitedList(expression)\\\\nparameters = pp.DelimitedList(identifier)\\\\nfunction = identifier + LPAR + pp.Opt(parameters) + RPAR + block\\\\nproperty_ = identifier + block\\\\n\\\\nfun_decl = FUN + function\\\\nvar_decl = VAR + identifier + pp.Opt(EQ + expression) + SEMI\\\\nclass_decl <<= (\\\\n        CLASS\\\\n        - identifier\\\\n        + pp.Opt(\\\\\\\"<\\\\\\\" + identifier)\\\\n        + LBRACE\\\\n        + (function | property_ | class_decl)[...]\\\\n        + RBRACE\\\\n)\\\\n\\\\n\\\\nprimary = (TRUE | FALSE | NIL | THIS | number | string | identifier\\\\n           | SUPER + \\\\\\\".\\\\\\\" + identifier\\\\n           # | LPAR + expression + RPAR  <-- not needed, infix_notation takes care of this\\\\n           ).set_name(\\\\\\\"primary\\\\\\\")\\\\ncall = primary + (\\\\n        LPAR + pp.Opt(arguments) + RPAR\\\\n        | \\\\\\\".\\\\\\\" + identifier\\\\n)[1, ...]\\\\n\\\\narith_expression = pp.infix_notation(\\\\n    (call | primary).set_name(\\\\\\\"arith_operand\\\\\\\"),\\\\n    [\\\\n        (pp.one_of(\\\\\\\"! -\\\\\\\"), 1, pp.opAssoc.RIGHT),\\\\n        (pp.one_of(\\\\\\\"/ *\\\\\\\"), 2, pp.opAssoc.LEFT),\\\\n        (pp.one_of(\\\\\\\"- +\\\\\\\"), 2, pp.opAssoc.LEFT),\\\\n        (pp.one_of(\\\\\\\"> >= < <=\\\\\\\"), 2, pp.opAssoc.LEFT),\\\\n        (pp.one_of(\\\\\\\"!= ==\\\\\\\"), 2, pp.opAssoc.LEFT),\\\\n        (AND, 2, pp.opAssoc.LEFT),\\\\n        (OR, 2, pp.opAssoc.LEFT),\\\\n    ]\\\\n)\\\\nassignment = pp.Forward()\\\\nassignment <<= (call | identifier) + EQ + (assignment | arith_expression)\\\\n\\\\nexpression <<= assignment ^ arith_expression ^ function\\\\n\\\\nblock <<= pp.Group(LBRACE + declaration[...] + RBRACE)\\\\nwhile_statement = WHILE + LPAR + expression + RPAR + statement\\\\nreturn_statement = RETURN + pp.Opt(expression) + SEMI\\\\nprint_statement = PRINT + expression + SEMI\\\\nif_statement = IF + LPAR + expression + RPAR + statement + pp.Opt(ELSE + statement)\\\\nexpr_statement = expression + \\\\\\\";\\\\\\\"\\\\nfor_statement = FOR + LPAR + pp.Group(\\\\n    (var_decl | expr_statement | \\\\\\\";\\\\\\\")\\\\n    + pp.Opt(expression) + \\\\\\\";\\\\\\\"\\\\n    + pp.Opt(expression)\\\\n) + RPAR + statement\\\\n\\\\n\\\\nstatement <<= pp.Group(\\\\n    expr_statement\\\\n    | for_statement\\\\n    | if_statement\\\\n    | print_statement\\\\n    | return_statement\\\\n    | while_statement\\\\n    | block\\\\n)\\\\n\\\\ndeclaration <<= (\\\\n    class_decl\\\\n    | fun_decl\\\\n    | var_decl\\\\n    | statement\\\\n)\\\\n\\\\nprogram = declaration[...]\\\\nprogram.ignore(pp.dbl_slash_comment)\\\\n\\\\n# define names so that we get a better diagram\\\\npp.autoname_elements()\\\\n\\\\n\\\\ndef main():\\\\n    import textwrap\\\\n\\\\n    success, _ = program.run_tests(\\\\n        textwrap.dedent(t) for t in [\\\\n            \\\\\\\"\\\\\\\"\\\\\\\"\\\\\\\\\\\\n                var a = 1;\\\\n                {\\\\n                  var a = a + 2;\\\\n                  print a;\\\\n                }\\\\n                \\\\\\\"\\\\\\\"\\\\\\\",\\\\n            \\\\\\\"\\\\\\\"\\\\\\\"\\\\\\\\\\\\n                {\\\\n                  var i = 0;\\\\n                  while (i < 10) {\\\\n                    print i;\\\\n                    i = i + 1;\\\\n                  }\\\\n                }\\\\n            \\\\\\\"\\\\\\\"\\\\\\\",\\\\n            \\\\\\\"\\\\\\\"\\\\\\\"\\\\\\\\\\\\n                var a = 0;\\\\n                var temp;\\\\n                \\\\n                for (var b = 1; a < 10000; b = temp + b) {\\\\n                  print a;\\\\n                  temp = a;\\\\n                  a = b;\\\\n                }\\\\n            \\\\\\\"\\\\\\\"\\\\\\\",\\\\n            \\\\\\\"\\\\\\\"\\\\\\\"\\\\\\\\\\\\n                fun add(a, b, c) {\\\\n                  print a + b + c;\\\\n                }\\\\n                \\\\n                add(1, 2, 3);\\\\n            \\\\\\\"\\\\\\\"\\\\\\\",\\\\n            \\\\\\\"\\\\\\\"\\\\\\\"\\\\\\\\\\\\n                fun count(n) {\\\\n                  while (n < 100) {\\\\n                    if (n == 3) return n; // <--\\\\n  \\\"}}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.55}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 83_

<details><summary>Logged reasoning block</summary>

```text
That's a huge val file. The val data contains the full source code in query_tokens and pos_tokens. Let me look at the structure of a val sample more concisely - specifically, what fields does it have (not the actual content, which is huge).

Let me also check:
1. The M1 data location
2. The dataflow_graph.json structure (for structural data availability dimension)
3. Whether there's any existing per-instance evaluation results for the predictions-dir approach
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "ef9352ca-f653-47cb-a49f-7d1a263b1f93",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V9ApEGBoEg1fVwaneVjtgd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4807,
      "cache_read_input_tokens": 48065,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4807
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

_source line 84_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_0174PCi4HU5W8Kb4hgtaVxwr`</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "python3 -c \"import json; d=json.loads(open('/root/autodl-tmp/structfuse/full_m2_training_data/val_random_s42.jsonl').readline()); print(list(d.keys()))\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "a48ccfb5-2487-401c-8d3f-a9f904d98b5d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V9ApEGBoEg1fVwaneVjtgd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4807,
      "cache_read_input_tokens": 48065,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4807
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

_source line 85 · 2026-05-14T20:16:36.891Z_

<details><summary>↩ Tool result · `toolu_0174PCi4HU5W8Kb4hgtaVxwr`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "0a132794-27ec-4b12-9109-41fea03b3c42",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 86_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01EFMVqnD6orJK8EpTnzeJNX`</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "find /root/autodl-tmp/structfuse -name \"all.jsonl\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "ef81d728-3738-4fab-9130-810c66011f51",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V9ApEGBoEg1fVwaneVjtgd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4807,
      "cache_read_input_tokens": 48065,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4807
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

_source line 87 · 2026-05-14T20:16:38.231Z_

<details><summary>↩ Tool result · `toolu_01EFMVqnD6orJK8EpTnzeJNX`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/structfuse/full_m1_data/all.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.47}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "d1250b6d-5cda-42f3-a2e2-7b4717e14e1c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/structfuse/full_m1_data/all.jsonl\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.47}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/structfuse/full_m1_data/all.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.47}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 88_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_019bUkmrWrt5tgDa8PsraXwm`</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "wc -l /root/autodl-tmp/structfuse/full_m2_training_data/val_random_s42.jsonl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "cd88c6ec-1f37-4903-82c9-61f791cf97f9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V9ApEGBoEg1fVwaneVjtgd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4807,
      "cache_read_input_tokens": 48065,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4807
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

_source line 89 · 2026-05-14T20:16:38.784Z_

<details><summary>↩ Tool result · `toolu_019bUkmrWrt5tgDa8PsraXwm`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"2980 /root/autodl-tmp/structfuse/full_m2_training_data/val_random_s42.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "582755ff-83b7-4c73-bdbe-81f50f8d63d3",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"2980 /root/autodl-tmp/structfuse/full_m2_training_data/val_random_s42.jsonl\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"2980 /root/autodl-tmp/structfuse/full_m2_training_data/val_random_s42.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 90_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01Jgctv1w7ckAm6AMxM5GN2q`</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\nd = json.loads(open('/root/autodl-tmp/structfuse/full_m2_training_data/val_random_s42.jsonl').readline())\nprint('Keys:', list(d.keys()))\nprint('neg_candidates count:', len(d.get('neg_candidates', [])))\nprint('candidate_tokens count:', len(d.get('candidate_tokens', {})))\nprint('has_dataflow:', d.get('has_dataflow'))\nprint('neg_difficulty:', d.get('neg_difficulty'))\nprint('strategy:', d.get('strategy'))\nprint('margin:', d.get('margin'))\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "cb2b5282-e70e-4edf-bb9d-53e7fb7a913a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017sgZipUGKhVHnsWBp4CtwM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 895,
      "cache_read_input_tokens": 52872,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 895
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

_source line 91 · 2026-05-14T20:16:44.827Z_

<details><summary>↩ Tool result · `toolu_01Jgctv1w7ckAm6AMxM5GN2q`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"Keys: ['query_id', 'query_tokens', 'pos_id', 'pos_tokens', 'pos_dataflow_distance', 'neg_candidates', 'candidate_tokens']\\nneg_candidates count: 50\\ncandidate_tokens count: 50\\nhas_dataflow: None\\nneg_difficulty: None\\nstrategy: None\\nmargin: None\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "ab1e2e5b-8238-418a-bf0d-2f1478554344",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"Keys: ['query_id', 'query_tokens', 'pos_id', 'pos_tokens', 'pos_dataflow_distance', 'neg_candidates', 'candidate_tokens']\\\\nneg_candidates count: 50\\\\ncandidate_tokens count: 50\\\\nhas_dataflow: None\\\\nneg_difficulty: None\\\\nstrategy: None\\\\nmargin: None\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"Keys: ['query_id', 'query_tokens', 'pos_id', 'pos_tokens', 'pos_dataflow_distance', 'neg_candidates', 'candidate_tokens']\\nneg_candidates count: 50\\ncandidate_tokens count: 50\\nhas_dataflow: None\\nneg_difficulty: None\\nstrategy: None\\nmargin: None\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 92_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01LrPVucMamCPTSCKsmXJP4r`</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "head -1 /root/autodl-tmp/structfuse/full_m2_training_data/dataflow_graph.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "098febd1-c005-4f22-830d-f09e69647be9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017sgZipUGKhVHnsWBp4CtwM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 895,
      "cache_read_input_tokens": 52872,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 895
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


### Large event (continued)

````text
### Tool result

_source line 93 · 2026-05-14T20:17:28.932Z_

&lt;details>&lt;summary>↩ Tool result · `toolu_01LrPVucMamCPTSCKsmXJP4r`&lt;/summary>

```text
Error: result (15,402,462 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-structfuse-context/cd11087d-991b-47e1-b3c6-f81e960f8388/tool-results/mcp-agent-ml-research-ssh_read_only-1778789848895.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-structfuse-context/cd11087d-991b-47e1-b3c6-f81e960f8388/tool-results/mcp-agent-ml-research-ssh_read_only-1778789848895.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-structfuse-context/cd11087d-991b-47e1-b3c6-f81e960f8388/tool-results/mcp-agent-ml-research-ssh_read_only-1778789848895.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

&lt;/details>

&lt;details>&lt;summary>Recorded metadata&lt;/summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "b4288122-75df-4451-af18-8cdcad847a29",
  "tool_use_result": {
    "content": "Error: result (15,402,462 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-structfuse-context/cd11087d-991b-47e1-b3c6-f81e960f8388/tool-results/mcp-agent-ml-research-ssh_read_only-1778789848895.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-structfuse-context/cd11087d-991b-47e1-b3c6-f81e960f8388/tool-results/mcp-agent-ml-research-ssh_read_only-1778789848895.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-structfuse-context/cd11087d-991b-47e1-b3c6-f81e960f8388/tool-results/mcp-agent-ml-research-ssh_read_only-1778789848895.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
    "structuredContent": {

````

---

### Large event (continued)

```text
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'head -1 /root/autodl-tmp/structfuse/full_m2_training_data/dataflow_graph.json'\\n\\nStdout:\\n\\n{\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/reports/reports.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/bank.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/general/general.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/vendored/discord/ext/menus/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/_diagnoser.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/bot.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/reports/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/equalizer.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/apis/spotify.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/apis/global_db.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/utils/predicates.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/_drivers/_mongo.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/permissions/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/trivia/session.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/admin/announcer.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/config.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/_drivers/base.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/utils/views.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/_debuginfo.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/converters.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/cleanup/cleanup.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/streams/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/mod/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/_drivers/postgres/postgres.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/utils.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/utils/tunnel.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/downloader/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/image/image.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/commands/requires.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/modlog/modlog.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/economy/economy.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/commands/context.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/downloader/installable.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/mutes/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/mutes/abc.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/admin/admin.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/logging.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/downloader/json_mixins.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/mod/abc.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/mutes/mutes.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/commands/commands.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/apis/playlist_wrapper.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/_rpc.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/core/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/utils/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/apis/youtube.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/core/cog_utils.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/permissions/permissions.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/commands/converter.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/warnings/warnings.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/utils/chat_formatting.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/alias/alias.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/modlog/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/apis/local_db.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/downloader/downloader.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/filter/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/data_manager.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/dev_commands.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/downloader/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/streams/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/utils/dbtools.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/downloader/repo_manager.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/alias/alias_entry.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/app_commands/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/trivia/schema.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/alias/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/apis/playlist_interface.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/tree.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/customcom/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/modlog.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/_cog_manager.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/mod/kickban.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/apis/interface.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/audio_dataclasses.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/warnings/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/utils/antispam.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/utils/menus.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/customcom/customcom.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/_drivers/json.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/streams/streamtypes.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/cleanup/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/trivia/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/economy/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/commands/help.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/apis/persist_queue_wrapper.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/image/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/streams/streams.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/i18n.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/manager.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/trivia/trivia.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/filter/filter.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/admin/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/general/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/_settings_caches.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/core_commands.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/commands/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/mod/mod.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/reports/reports.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/bank.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/general/general.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/vendored/discord/ext/menus/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/_diagnoser.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/bot.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/reports/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/equalizer.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/apis/spotify.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/apis/global_db.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/utils/predicates.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/_drivers/_mongo.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/permissions/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/trivia/session.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/admin/announcer.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/config.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/_drivers/base.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/utils/views.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/_debuginfo.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/converters.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/cleanup/cleanup.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/streams/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/mod/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/_drivers/postgres/postgres.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/utils.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/utils/tunnel.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/downloader/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/image/image.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/commands/requires.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/modlog/modlog.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/economy/economy.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/commands/context.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/downloader/installable.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/mutes/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/mutes/abc.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/admin/admin.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/logging.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/downloader/json_mixins.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/mod/abc.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/mutes/mutes.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/commands/commands.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/apis/playlist_wrapper.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/_rpc.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/core/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/utils/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/apis/youtube.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/core/cog_utils.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/permissions/permissions.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/commands/converter.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/warnings/warnings.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/utils/chat_formatting.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/alias/alias.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/modlog/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/apis/local_db.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/downloader/downloader.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/filter/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/data_manager.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/dev_commands.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/downloader/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/streams/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/utils/dbtools.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/downloader/repo_manager.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/alias/alias_entry.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/app_commands/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/trivia/schema.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/alias/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/apis/playlist_interface.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/tree.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/customcom/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/modlog.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/_cog_manager.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/mod/kickban.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/apis/interface.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/audio_dataclasses.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/warnings/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/utils/antispam.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/utils/menus.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/customcom/customcom.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/_drivers/json.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/streams/streamtypes.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/cleanup/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/trivia/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/economy/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/commands/help.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/apis/persist_queue_wrapper.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/image/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/streams/streams.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/i18n.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/manager.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/trivia/trivia.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/filter/filter.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/admin/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/general/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/_settings_caches.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/core_commands.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/core/commands/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/mod/mod.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/downloader/repo_manager.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/warnings/warnings.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/core/utils/chat_formatting.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/core/_drivers/postgres/postgres.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/audio/core/commands/player.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/alias/alias.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/mutes/voicemutes.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/customcom/customcom.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/audio/apis/local_db.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/downloader/downloader.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/core/_drivers/json.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/audio/core/utilities/player.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/core/commands/requires.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/audio/core/utilities/miscellaneous.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/audio/core/utilities/formatting.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/vendored/discord/ext/menus/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/core/bot.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/trivia/schema.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/audio/core/commands/playlists.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/audio/core/commands/controller.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/audio/core/tasks/player.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/core/i18n.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/audio/apis/spotify.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/audio/manager.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/trivia/trivia.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/mutes/mutes.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/pytest/core.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/core/commands/commands.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/core/_settings_caches.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/core/_drivers/_mongo.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/core/config.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/mod/kickban.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/core/_drivers/base.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/audio/apis/interface.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/audio/audio_dataclasses.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/core/utils/views.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/audio/converters.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/warnings/warnings.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/core/utils/chat_formatting.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/core/_drivers/postgres/postgres.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/audio/core/commands/player.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/alias/alias.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/mutes/voicemutes.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/customcom/customcom.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/audio/apis/local_db.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/downloader/downloader.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/core/_drivers/json.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/audio/core/utilities/player.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/core/commands/requires.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/audio/core/utilities/miscellaneous.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/audio/core/utilities/formatting.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/vendored/discord/ext/menus/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/core/bot.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/trivia/schema.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/audio/core/commands/playlists.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/audio/core/commands/controller.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/audio/core/tasks/player.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/core/i18n.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/audio/apis/spotify.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/audio/manager.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/trivia/trivia.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/mutes/mutes.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/pytest/core.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/core/commands/commands.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/core/_settings_caches.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/core/_drivers/_mongo.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/core/config.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/mod/kickban.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/core/_drivers/base.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/audio/apis/interface.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/audio/audio_dataclasses.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/core/utils/views.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/audio/converters.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/audio/core/commands/audioset.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/reports/reports.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/bank.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/general/general.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/vendored/discord/ext/menus/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/_diagnoser.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/bot.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/reports/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/audio/core/commands/llset.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/audio/equalizer.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/audio/apis/spotify.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/pytest/core.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/audio/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/audio/apis/global_db.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/utils/predicates.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/_drivers/_mongo.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/permissions/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/trivia/session.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/admin/announcer.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/config.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/_drivers/base.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/utils/views.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/_debuginfo.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/audio/converters.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/cleanup/cleanup.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/streams/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/mod/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/_drivers/postgres/postgres.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/audio/utils.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/utils/tunnel.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/image/image.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/commands/requires.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/modlog/modlog.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/economy/economy.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/commands/context.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/mutes/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/mutes/abc.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/admin/admin.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/json_mixins.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/logging.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/mod/abc.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/mutes/mutes.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/commands/commands.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/audio/apis/playlist_wrapper.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/_rpc.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/audio/core/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/utils/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/audio/apis/youtube.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/audio/core/cog_utils.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/permissions/permissions.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/commands/converter.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/warnings/warnings.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/utils/chat_formatting.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/audio/managed_node/ll_version.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/alias/alias.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/modlog/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/audio/apis/local_db.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/filter/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/downloader.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/data_manager.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/dev_commands.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/streams/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/utils/dbtools.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/repo_manager.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/audio/core/utilities/formatting.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/alias/alias_entry.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/app_commands/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/trivia/schema.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/audio/core/commands/playlists.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/audio/core/utilities/playlists.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/alias/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/audio/apis/playlist_interface.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/tree.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/customcom/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/audio/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/modlog.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/_cog_manager.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/mod/kickban.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/audio/apis/interface.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/utils/_internal_utils.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/audio/audio_dataclasses.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/warnings/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/utils/antispam.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/utils/menus.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/customcom/customcom.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/_drivers/json.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/streams/streamtypes.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/cleanup/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/trivia/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/economy/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/commands/help.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/audio/apis/persist_queue_wrapper.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/image/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/streams/streams.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/i18n.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/audio/manager.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/trivia/trivia.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/admin/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/filter/filter.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/general/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/_settings_caches.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/core_commands.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/commands/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/mod/mod.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/audio/core/commands/audioset.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/reports/reports.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/bank.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/general/general.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/vendored/discord/ext/menus/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/_diagnoser.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/bot.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/reports/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/audio/core/commands/llset.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/audio/equalizer.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/audio/apis/spotify.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/pytest/core.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/audio/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/audio/apis/global_db.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/utils/predicates.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/_drivers/_mongo.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/permissions/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/trivia/session.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/admin/announcer.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/config.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/_drivers/base.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/utils/views.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/_debuginfo.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/audio/converters.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/cleanup/cleanup.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/streams/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/mod/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/_drivers/postgres/postgres.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/audio/utils.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/utils/tunnel.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/image/image.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/commands/requires.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/modlog/modlog.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/economy/economy.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/commands/context.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/mutes/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/mutes/abc.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/admin/admin.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/json_mixins.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/logging.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/mod/abc.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/mutes/mutes.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/commands/commands.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/audio/apis/playlist_wrapper.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/_rpc.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/audio/core/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/utils/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/audio/apis/youtube.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/audio/core/cog_utils.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/permissions/permissions.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/commands/converter.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/warnings/warnings.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/utils/chat_formatting.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/audio/managed_node/ll_version.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/alias/alias.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/modlog/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/audio/apis/local_db.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/filter/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/downloader.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/data_manager.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/dev_commands.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/streams/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/utils/dbtools.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/repo_manager.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/audio/core/utilities/formatting.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/alias/alias_entry.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/app_commands/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/trivia/schema.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/audio/core/commands/playlists.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/audio/core/utilities/playlists.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/alias/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/audio/apis/playlist_interface.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/tree.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/customcom/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/audio/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/modlog.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/_cog_manager.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/mod/kickban.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/audio/apis/interface.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/utils/_internal_utils.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/audio/audio_dataclasses.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/warnings/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/utils/antispam.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/utils/menus.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/customcom/customcom.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/_drivers/json.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/streams/streamtypes.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/cleanup/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/trivia/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/economy/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/commands/help.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/audio/apis/persist_queue_wrapper.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/image/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/streams/streams.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/i18n.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/audio/manager.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/trivia/trivia.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/admin/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/filter/filter.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/general/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/_settings_caches.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/core_commands.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/core/commands/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/mod/mod.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h::redbot/cogs/downloader/installable.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/core/commands/localtracks.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/core/events/lavalink.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/core/commands/audioset.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/reports/reports.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/trivia/converters.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/bank.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/general/general.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/downloader/converters.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/mod/events.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/vendored/discord/ext/menus/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/_diagnoser.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/bot.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/downloader/checks.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/reports/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/core/commands/llset.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/core/commands/controller.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/equalizer.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/apis/spotify.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/pytest/core.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/utils/common_filters.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/apis/global_db.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/utils/predicates.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/_drivers/_mongo.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/permissions/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/trivia/session.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/admin/announcer.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/config.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/_drivers/base.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/utils/views.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/_debuginfo.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/converters.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/cleanup/cleanup.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/streams/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/mod/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/_drivers/postgres/postgres.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/utils.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/utils/tunnel.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/downloader/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/image/image.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/commands/requires.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/modlog/modlog.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/economy/economy.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/commands/context.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/downloader/installable.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/core/commands/queue.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/mutes/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/mutes/abc.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/admin/converters.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/admin/admin.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/logging.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/downloader/json_mixins.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/core/abc.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/mod/abc.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/mutes/mutes.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/commands/commands.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/apis/playlist_wrapper.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/core/events/red.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/core/events/cog.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/mod/settings.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/_rpc.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/utils/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/core/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/apis/youtube.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/core/cog_utils.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/permissions/permissions.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/setup.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/commands/converter.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/warnings/warnings.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/utils/chat_formatting.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/core/commands/player.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/alias/alias.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/managed_node/ll_version.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/pytest/downloader.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/modlog/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/mutes/voicemutes.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/apis/local_db.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/filter/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/downloader/downloader.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/data_manager.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/downloader/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/streams/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/core/commands/equalizer.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/utils/dbtools.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/core/commands/miscellaneous.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/core/tasks/lavalink.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/downloader/repo_manager.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/core/utilities/formatting.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/alias/alias_entry.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/app_commands/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/trivia/schema.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/mod/names.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/core/commands/playlists.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/core/utilities/playlists.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/alias/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/apis/playlist_interface.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/tree.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/customcom/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/_events.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/modlog.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/_cog_manager.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/cleanup/converters.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/mod/kickban.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/apis/interface.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/utils/_internal_utils.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/audio_dataclasses.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/_sharedlibdeprecation.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/warnings/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/mod/slowmode.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/utils/antispam.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/utils/menus.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/customcom/customcom.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/permissions/converters.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/streams/streamtypes.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/_drivers/json.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/cleanup/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/core/utilities/player.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/trivia/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/core/tasks/startup.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/core/events/dpy.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/economy/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/core/utilities/miscellaneous.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/commands/help.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/utils/mod.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/warnings/helpers.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/apis/persist_queue_wrapper.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/image/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/core/utilities/queue.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/streams/streams.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/core/tasks/player.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/i18n.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/manager.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/trivia/trivia.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/core/utilities/local_tracks.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/admin/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/filter/filter.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/general/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/_settings_caches.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/core_commands.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/commands/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/mutes/converters.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/core/utilities/equalizer.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/mod/mod.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/__main__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/core/commands/localtracks.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/core/events/lavalink.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/core/commands/audioset.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/reports/reports.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/trivia/converters.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/bank.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/general/general.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/downloader/converters.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/mod/events.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/vendored/discord/ext/menus/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/_diagnoser.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/bot.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/downloader/checks.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/reports/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/core/commands/llset.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/core/commands/controller.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/equalizer.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/apis/spotify.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/pytest/core.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/utils/common_filters.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/apis/global_db.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/utils/predicates.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/_drivers/_mongo.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/permissions/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/trivia/session.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/admin/announcer.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/config.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/_drivers/base.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/utils/views.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/_debuginfo.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/converters.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/cleanup/cleanup.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/streams/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/mod/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/_drivers/postgres/postgres.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/utils.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/utils/tunnel.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/downloader/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/image/image.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/commands/requires.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/modlog/modlog.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/economy/economy.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/commands/context.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/downloader/installable.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/core/commands/queue.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/mutes/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/mutes/abc.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/admin/converters.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/admin/admin.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/logging.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/downloader/json_mixins.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/core/abc.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/mod/abc.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/mutes/mutes.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/commands/commands.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/apis/playlist_wrapper.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/core/events/red.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/core/events/cog.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/mod/settings.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/_rpc.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/utils/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/core/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/apis/youtube.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/core/cog_utils.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/permissions/permissions.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/setup.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/commands/converter.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/warnings/warnings.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/utils/chat_formatting.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/core/commands/player.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/alias/alias.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/managed_node/ll_version.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/pytest/downloader.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/modlog/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/mutes/voicemutes.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/apis/local_db.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/filter/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/downloader/downloader.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/data_manager.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/downloader/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/streams/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/core/commands/equalizer.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/utils/dbtools.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/core/commands/miscellaneous.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/core/tasks/lavalink.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/downloader/repo_manager.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/core/utilities/formatting.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/alias/alias_entry.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/app_commands/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/trivia/schema.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/mod/names.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/core/commands/playlists.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/core/utilities/playlists.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/alias/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/apis/playlist_interface.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/tree.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/customcom/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/_events.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/modlog.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/_cog_manager.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/cleanup/converters.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/mod/kickban.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/apis/interface.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/utils/_internal_utils.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/audio_dataclasses.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/_sharedlibdeprecation.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/warnings/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/mod/slowmode.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/utils/antispam.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/utils/menus.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/customcom/customcom.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/permissions/converters.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/streams/streamtypes.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/_drivers/json.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/cleanup/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/core/utilities/player.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/trivia/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/core/tasks/startup.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/core/events/dpy.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/economy/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/core/utilities/miscellaneous.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/commands/help.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/utils/mod.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/warnings/helpers.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/apis/persist_queue_wrapper.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/image/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/core/utilities/queue.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/streams/streams.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/core/tasks/player.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/i18n.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/manager.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/trivia/trivia.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/core/utilities/local_tracks.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/admin/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/filter/filter.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/general/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/_settings_caches.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/core_commands.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/commands/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/mutes/converters.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/audio/core/utilities/equalizer.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/cogs/mod/mod.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/__main__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/core/commands/localtracks.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/core/events/lavalink.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/core/commands/audioset.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/reports/reports.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/trivia/converters.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/bank.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/general/general.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/downloader/info_schemas.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/downloader/converters.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/mod/events.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/vendored/discord/ext/menus/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/_diagnoser.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/bot.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/downloader/checks.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/reports/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/core/commands/llset.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/core/commands/controller.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/equalizer.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/apis/spotify.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/pytest/core.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/utils/common_filters.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/apis/global_db.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/utils/predicates.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/_drivers/_mongo.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/permissions/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/trivia/session.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/admin/announcer.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/config.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/_drivers/base.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/utils/views.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/_debuginfo.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/converters.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/cleanup/cleanup.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/streams/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/mod/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/_drivers/postgres/postgres.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/utils.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/utils/tunnel.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/downloader/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/image/image.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/commands/requires.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/modlog/modlog.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/economy/economy.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/core/utilities/parsers.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/commands/context.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/downloader/installable.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/core/commands/queue.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/mutes/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/mutes/abc.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/admin/converters.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/admin/admin.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/logging.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/downloader/json_mixins.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/mod/abc.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/mutes/mutes.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/commands/commands.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/apis/playlist_wrapper.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/core/events/red.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/core/events/cog.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/mod/settings.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/_rpc.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/core/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/utils/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/apis/youtube.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/core/cog_utils.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/permissions/permissions.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/setup.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/commands/converter.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/warnings/warnings.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/utils/chat_formatting.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/core/commands/player.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/managed_node/ll_version.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/modlog/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/mutes/voicemutes.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/apis/local_db.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/filter/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/downloader/downloader.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/data_manager.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/dev_commands.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/downloader/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/streams/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/core/commands/equalizer.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/utils/dbtools.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/core/commands/miscellaneous.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/downloader/repo_manager.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/core/utilities/formatting.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias_entry.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/app_commands/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/trivia/schema.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/mod/names.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/core/commands/playlists.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/core/utilities/playlists.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/apis/playlist_interface.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/tree.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/customcom/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/_events.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/modlog.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/_cog_manager.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/cleanup/converters.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/mod/kickban.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/apis/interface.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/utils/_internal_utils.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/audio_dataclasses.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/warnings/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/mod/slowmode.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/utils/antispam.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/utils/menus.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/customcom/customcom.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/permissions/converters.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/streams/streamtypes.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/_drivers/json.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/cleanup/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/core/utilities/player.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/trivia/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/core/tasks/startup.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/core/events/dpy.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/economy/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/core/utilities/miscellaneous.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/commands/help.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/utils/mod.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/warnings/helpers.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/apis/persist_queue_wrapper.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/_cli.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/image/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/core/utilities/queue.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/streams/streams.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/core/tasks/player.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/i18n.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/manager.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/trivia/trivia.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/admin/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/filter/filter.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/general/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/_settings_caches.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/core_commands.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/commands/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/mutes/converters.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/core/utilities/equalizer.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/mod/mod.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/__main__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/core/commands/localtracks.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/core/events/lavalink.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/core/commands/audioset.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/reports/reports.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/trivia/converters.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/bank.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/general/general.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/downloader/info_schemas.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/downloader/converters.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/mod/events.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/vendored/discord/ext/menus/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/_diagnoser.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/bot.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/downloader/checks.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/reports/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/core/commands/llset.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/core/commands/controller.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/equalizer.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/apis/spotify.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/pytest/core.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/utils/common_filters.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/apis/global_db.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/utils/predicates.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/_drivers/_mongo.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/permissions/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/trivia/session.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/admin/announcer.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/config.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/_drivers/base.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/utils/views.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/_debuginfo.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/converters.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/cleanup/cleanup.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/streams/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/mod/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/_drivers/postgres/postgres.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/utils.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/utils/tunnel.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/downloader/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/image/image.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/commands/requires.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/modlog/modlog.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/economy/economy.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/core/utilities/parsers.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/commands/context.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/downloader/installable.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/core/commands/queue.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/mutes/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/mutes/abc.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/admin/converters.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/admin/admin.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/logging.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/downloader/json_mixins.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/mod/abc.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/mutes/mutes.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/commands/commands.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/apis/playlist_wrapper.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/core/events/red.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/core/events/cog.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/mod/settings.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/_rpc.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/core/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/utils/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/apis/youtube.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/core/cog_utils.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/permissions/permissions.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/setup.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/commands/converter.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/warnings/warnings.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/utils/chat_formatting.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/core/commands/player.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/managed_node/ll_version.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/modlog/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/mutes/voicemutes.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/apis/local_db.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/filter/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/downloader/downloader.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/data_manager.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/dev_commands.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/downloader/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/streams/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/core/commands/equalizer.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/utils/dbtools.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/core/commands/miscellaneous.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/downloader/repo_manager.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/core/utilities/formatting.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias_entry.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/app_commands/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/trivia/schema.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/mod/names.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/core/commands/playlists.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/core/utilities/playlists.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/apis/playlist_interface.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/tree.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/customcom/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/_events.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/modlog.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/_cog_manager.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/cleanup/converters.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/mod/kickban.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/apis/interface.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/utils/_internal_utils.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/audio_dataclasses.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/warnings/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/mod/slowmode.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/utils/antispam.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/utils/menus.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/customcom/customcom.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/permissions/converters.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/streams/streamtypes.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/_drivers/json.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/cleanup/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/core/utilities/player.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/trivia/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/core/tasks/startup.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/core/events/dpy.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/economy/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/core/utilities/miscellaneous.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/commands/help.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/utils/mod.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/warnings/helpers.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/apis/persist_queue_wrapper.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/_cli.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/image/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/core/utilities/queue.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/streams/streams.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/core/tasks/player.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/i18n.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/manager.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/trivia/trivia.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/admin/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/filter/filter.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/general/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/_settings_caches.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/core_commands.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/core/commands/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/mutes/converters.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/audio/core/utilities/equalizer.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/mod/mod.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/__main__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn::redbot/cogs/alias/alias.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/core/events/lavalink.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/core/commands/audioset.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/reports/reports.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/bank.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/general/general.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/info_schemas.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/_drivers/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/converters.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/mod/events.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/vendored/discord/ext/menus/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/_diagnoser.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/bot.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/reports/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/core/commands/controller.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/equalizer.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/apis/spotify.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/pytest/core.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/utils/common_filters.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/apis/global_db.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/utils/predicates.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/_drivers/_mongo.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/permissions/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/trivia/session.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/admin/announcer.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/config.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/_drivers/base.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/utils/views.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/_debuginfo.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/converters.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/cleanup/cleanup.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/streams/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/mod/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/_drivers/postgres/postgres.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/utils.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/utils/tunnel.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/image/image.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/commands/requires.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/modlog/modlog.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/economy/economy.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/core/utilities/parsers.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/commands/context.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/installable.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/core/commands/queue.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/mutes/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/mutes/abc.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/admin/converters.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/admin/admin.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/json_mixins.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/logging.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/core/abc.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/mod/abc.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/mutes/mutes.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/commands/commands.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/apis/playlist_wrapper.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/core/events/red.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/_rpc.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/core/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/utils/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/apis/youtube.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/core/cog_utils.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/permissions/permissions.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/setup.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/commands/converter.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/warnings/warnings.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/utils/chat_formatting.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/core/commands/player.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/alias/alias.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/managed_node/ll_version.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/modlog/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/mutes/voicemutes.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/apis/local_db.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/downloader.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/filter/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/data_manager.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/dev_commands.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/streams/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/utils/dbtools.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/core/tasks/lavalink.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/core/utilities/formatting.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/alias/alias_entry.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/app_commands/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/trivia/schema.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/core/commands/playlists.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/core/utilities/playlists.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/alias/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/apis/playlist_interface.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/tree.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/customcom/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/_events.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/modlog.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/_cog_manager.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/mod/kickban.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/apis/interface.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/utils/_internal_utils.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/audio_dataclasses.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/warnings/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/utils/antispam.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/utils/menus.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/customcom/customcom.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/_drivers/json.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/streams/streamtypes.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/cleanup/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/core/utilities/player.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/trivia/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/core/tasks/startup.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/core/events/dpy.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/economy/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/core/utilities/miscellaneous.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/commands/help.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/apis/persist_queue_wrapper.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/_cli.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/image/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/streams/streams.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/core/tasks/player.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/i18n.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/manager.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/trivia/trivia.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/admin/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/filter/filter.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/general/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/_settings_caches.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/core_commands.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/commands/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/mod/mod.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/__main__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/core/events/lavalink.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/core/commands/audioset.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/reports/reports.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/bank.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/general/general.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/info_schemas.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/_drivers/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/converters.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/mod/events.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/vendored/discord/ext/menus/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/_diagnoser.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/bot.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/reports/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/core/commands/controller.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/equalizer.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/apis/spotify.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/pytest/core.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/utils/common_filters.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/apis/global_db.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/utils/predicates.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/_drivers/_mongo.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/permissions/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/trivia/session.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/admin/announcer.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/config.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/_drivers/base.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/utils/views.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/_debuginfo.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/converters.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/cleanup/cleanup.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/streams/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/mod/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/_drivers/postgres/postgres.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/utils.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/utils/tunnel.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/image/image.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/commands/requires.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/modlog/modlog.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/economy/economy.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/core/utilities/parsers.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/commands/context.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/installable.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/core/commands/queue.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/mutes/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/mutes/abc.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/admin/converters.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/admin/admin.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/json_mixins.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/logging.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/core/abc.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/mod/abc.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/mutes/mutes.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/commands/commands.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/apis/playlist_wrapper.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/core/events/red.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/_rpc.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/core/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/utils/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/apis/youtube.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/core/cog_utils.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/permissions/permissions.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/setup.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/commands/converter.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/warnings/warnings.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/utils/chat_formatting.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/core/commands/player.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/alias/alias.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/managed_node/ll_version.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/modlog/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/mutes/voicemutes.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/apis/local_db.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/downloader.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/filter/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/data_manager.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/dev_commands.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/streams/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/utils/dbtools.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/core/tasks/lavalink.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/core/utilities/formatting.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/alias/alias_entry.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/app_commands/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/trivia/schema.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/core/commands/playlists.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/core/utilities/playlists.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/alias/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/apis/playlist_interface.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/tree.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/customcom/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/_events.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/modlog.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/_cog_manager.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/mod/kickban.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/apis/interface.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/utils/_internal_utils.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/audio_dataclasses.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/warnings/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/utils/antispam.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/utils/menus.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/customcom/customcom.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/_drivers/json.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/streams/streamtypes.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/cleanup/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/core/utilities/player.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/trivia/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/core/tasks/startup.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/core/events/dpy.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/economy/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/core/utilities/miscellaneous.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/commands/help.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/apis/persist_queue_wrapper.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/_cli.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/image/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/streams/streams.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/core/tasks/player.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/i18n.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/audio/manager.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/trivia/trivia.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/admin/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/filter/filter.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/general/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/_settings_caches.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/core_commands.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/core/commands/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/mod/mod.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/__main__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/reports/reports.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/bank.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/general/general.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/vendored/discord/ext/menus/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/_diagnoser.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/bot.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/reports/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/audio/equalizer.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/audio/apis/spotify.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/audio/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/audio/apis/global_db.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/utils/predicates.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/_drivers/_mongo.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/permissions/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/trivia/session.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/admin/announcer.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/config.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/_drivers/base.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/utils/views.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/_debuginfo.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/audio/converters.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/cleanup/cleanup.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/streams/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/mod/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/_drivers/postgres/postgres.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/audio/utils.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/utils/tunnel.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/downloader/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/image/image.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/commands/requires.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/modlog/modlog.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/economy/economy.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/commands/context.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/downloader/installable.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/mutes/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/mutes/abc.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/admin/admin.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/logging.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/downloader/json_mixins.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/mod/abc.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/mutes/mutes.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/commands/commands.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/audio/apis/playlist_wrapper.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/_rpc.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/audio/core/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/utils/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/audio/apis/youtube.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/audio/core/cog_utils.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/permissions/permissions.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/commands/converter.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/warnings/warnings.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/utils/chat_formatting.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/alias/alias.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/audio/managed_node/ll_version.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/modlog/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/audio/apis/local_db.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/downloader/downloader.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/filter/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/data_manager.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/downloader/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/streams/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/utils/dbtools.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/downloader/repo_manager.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/alias/alias_entry.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/app_commands/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/trivia/schema.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/alias/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/audio/apis/playlist_interface.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/tree.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/customcom/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/audio/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/modlog.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/_cog_manager.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/mod/kickban.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/audio/apis/interface.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/audio/audio_dataclasses.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/warnings/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/utils/antispam.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/utils/menus.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/customcom/customcom.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/_drivers/json.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/streams/streamtypes.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/cleanup/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/trivia/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/economy/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/commands/help.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/audio/apis/persist_queue_wrapper.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/image/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/streams/streams.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/i18n.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/audio/manager.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/trivia/trivia.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/admin/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/filter/filter.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/general/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/_settings_caches.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/core_commands.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/commands/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/mod/mod.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/reports/reports.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/bank.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/general/general.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/vendored/discord/ext/menus/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/_diagnoser.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/bot.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/reports/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/audio/equalizer.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/audio/apis/spotify.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/audio/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/audio/apis/global_db.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/utils/predicates.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/_drivers/_mongo.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/permissions/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/trivia/session.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/admin/announcer.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/config.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/_drivers/base.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/utils/views.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/_debuginfo.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/audio/converters.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/cleanup/cleanup.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/streams/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/mod/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/_drivers/postgres/postgres.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/audio/utils.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/utils/tunnel.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/downloader/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/image/image.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/commands/requires.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/modlog/modlog.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/economy/economy.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/commands/context.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/downloader/installable.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/mutes/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/mutes/abc.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/admin/admin.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/logging.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/downloader/json_mixins.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/mod/abc.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/mutes/mutes.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/commands/commands.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/audio/apis/playlist_wrapper.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/_rpc.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/audio/core/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/utils/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/audio/apis/youtube.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/audio/core/cog_utils.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/permissions/permissions.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/commands/converter.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/warnings/warnings.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/utils/chat_formatting.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/alias/alias.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/audio/managed_node/ll_version.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/modlog/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/audio/apis/local_db.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/downloader/downloader.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/filter/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/data_manager.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/downloader/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/streams/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/utils/dbtools.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/downloader/repo_manager.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/alias/alias_entry.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/app_commands/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/trivia/schema.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/alias/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/audio/apis/playlist_interface.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/tree.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/customcom/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/audio/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/modlog.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/_cog_manager.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/mod/kickban.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/audio/apis/interface.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/audio/audio_dataclasses.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/warnings/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/utils/antispam.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/utils/menus.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/customcom/customcom.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/_drivers/json.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/streams/streamtypes.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/cleanup/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/trivia/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/economy/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/commands/help.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/audio/apis/persist_queue_wrapper.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/image/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/streams/streams.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/i18n.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/audio/manager.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/trivia/trivia.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/admin/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/filter/filter.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/general/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/_settings_caches.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/core_commands.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/commands/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/cogs/mod/mod.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/core/commands/localtracks.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/core/events/lavalink.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/core/commands/audioset.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/reports/reports.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/trivia/converters.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/bank.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/general/general.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/downloader/info_schemas.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/downloader/converters.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/mod/events.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/vendored/discord/ext/menus/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/_diagnoser.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/bot.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/downloader/checks.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/reports/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/core/commands/llset.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/core/commands/controller.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/equalizer.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/apis/spotify.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/pytest/core.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/apis/global_db.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/utils/predicates.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/_drivers/_mongo.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/permissions/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/trivia/session.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/admin/announcer.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/config.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/_drivers/base.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/utils/views.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/_debuginfo.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/converters.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/cleanup/cleanup.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/streams/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/mod/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/_drivers/postgres/postgres.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/utils.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/utils/tunnel.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/downloader/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/image/image.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/commands/requires.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/modlog/modlog.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/economy/economy.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/commands/context.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/downloader/installable.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/core/commands/queue.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/mutes/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/mutes/abc.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/admin/converters.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/admin/admin.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/logging.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/downloader/json_mixins.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/core/abc.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/mod/abc.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/mutes/mutes.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/commands/commands.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/apis/playlist_wrapper.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/core/events/cog.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/mod/settings.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/_rpc.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/core/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/utils/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/apis/youtube.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/core/cog_utils.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/permissions/permissions.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/setup.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/commands/converter.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/warnings/warnings.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/utils/chat_formatting.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/core/commands/player.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/managed_node/ll_version.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/alias/alias.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/modlog/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/mutes/voicemutes.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/apis/local_db.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/filter/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/downloader/downloader.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/data_manager.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/dev_commands.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/downloader/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/streams/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/core/commands/equalizer.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/utils/dbtools.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/core/commands/miscellaneous.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/downloader/repo_manager.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/core/utilities/formatting.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/alias/alias_entry.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/app_commands/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/trivia/schema.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/mod/names.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/core/commands/playlists.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/core/utilities/playlists.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/alias/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/apis/playlist_interface.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/tree.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/customcom/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/_events.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/modlog.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/_cog_manager.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/cleanup/converters.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/mod/kickban.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/apis/interface.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/utils/_internal_utils.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/audio_dataclasses.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/warnings/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/mod/slowmode.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/utils/antispam.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/utils/menus.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/customcom/customcom.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/permissions/converters.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/streams/streamtypes.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/_drivers/json.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/cleanup/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/core/utilities/player.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/trivia/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/core/tasks/startup.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/core/events/dpy.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/economy/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/core/utilities/miscellaneous.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/commands/help.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/utils/mod.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/warnings/helpers.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/apis/persist_queue_wrapper.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/image/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/core/utilities/queue.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/streams/streams.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/i18n.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/manager.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/trivia/trivia.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/core/utilities/local_tracks.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/admin/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/filter/filter.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/general/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/_settings_caches.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/core_commands.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/commands/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/mutes/converters.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/core/utilities/equalizer.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/mod/mod.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__main__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/core/commands/localtracks.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/core/events/lavalink.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/core/commands/audioset.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/reports/reports.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/trivia/converters.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/bank.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/general/general.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/downloader/info_schemas.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/downloader/converters.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/mod/events.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/vendored/discord/ext/menus/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/_diagnoser.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/bot.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/downloader/checks.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/reports/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/core/commands/llset.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/core/commands/controller.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/equalizer.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/apis/spotify.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/pytest/core.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/apis/global_db.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/utils/predicates.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/_drivers/_mongo.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/permissions/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/trivia/session.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/admin/announcer.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/config.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/_drivers/base.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/utils/views.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/_debuginfo.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/converters.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/cleanup/cleanup.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/streams/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/mod/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/_drivers/postgres/postgres.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/utils.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/utils/tunnel.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/downloader/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/image/image.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/commands/requires.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/modlog/modlog.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/economy/economy.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/commands/context.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/downloader/installable.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/core/commands/queue.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/mutes/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/mutes/abc.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/admin/converters.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/admin/admin.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/logging.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/downloader/json_mixins.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/core/abc.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/mod/abc.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/mutes/mutes.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/commands/commands.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/apis/playlist_wrapper.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/core/events/cog.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/mod/settings.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/_rpc.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/core/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/utils/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/apis/youtube.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/core/cog_utils.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/permissions/permissions.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/setup.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/commands/converter.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/warnings/warnings.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/utils/chat_formatting.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/core/commands/player.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/managed_node/ll_version.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/alias/alias.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/modlog/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/mutes/voicemutes.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/apis/local_db.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/filter/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/downloader/downloader.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/data_manager.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/dev_commands.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/downloader/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/streams/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/core/commands/equalizer.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/utils/dbtools.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/core/commands/miscellaneous.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/downloader/repo_manager.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/core/utilities/formatting.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/alias/alias_entry.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/app_commands/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/trivia/schema.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/mod/names.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/core/commands/playlists.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/core/utilities/playlists.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/alias/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/apis/playlist_interface.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/tree.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/customcom/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/_events.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/modlog.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/_cog_manager.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/cleanup/converters.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/mod/kickban.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/apis/interface.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/utils/_internal_utils.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/audio_dataclasses.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/warnings/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/mod/slowmode.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/utils/antispam.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/utils/menus.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/customcom/customcom.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/permissions/converters.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/streams/streamtypes.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/_drivers/json.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/cleanup/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/core/utilities/player.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/trivia/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/core/tasks/startup.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/core/events/dpy.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/economy/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/core/utilities/miscellaneous.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/commands/help.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/utils/mod.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/warnings/helpers.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/apis/persist_queue_wrapper.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/image/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/core/utilities/queue.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/streams/streams.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/i18n.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/manager.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/trivia/trivia.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/core/utilities/local_tracks.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/admin/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/filter/filter.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/general/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/_settings_caches.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/core_commands.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/core/commands/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/mutes/converters.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/audio/core/utilities/equalizer.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/cogs/mod/mod.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__main__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud::redbot/__init__.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/downloader/repo_manager.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/warnings/warnings.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/core/utils/chat_formatting.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/core/_drivers/postgres/postgres.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/audio/core/commands/player.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/alias/alias.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/mutes/voicemutes.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/customcom/customcom.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/audio/apis/local_db.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/downloader/downloader.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/core/_drivers/json.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/audio/core/utilities/player.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/core/commands/requires.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/audio/core/utilities/miscellaneous.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/audio/core/utilities/formatting.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/vendored/discord/ext/menus/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/core/bot.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/trivia/schema.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/audio/core/commands/playlists.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/audio/core/commands/controller.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/audio/core/tasks/player.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/core/i18n.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/audio/apis/spotify.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/audio/manager.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/trivia/trivia.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/mutes/mutes.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/pytest/core.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/core/commands/commands.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/core/_settings_caches.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/core/_drivers/_mongo.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/core/config.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/mod/kickban.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/core/_drivers/base.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/audio/apis/interface.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/audio/audio_dataclasses.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/core/utils/views.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/audio/converters.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/warnings/warnings.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/core/utils/chat_formatting.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/core/_drivers/postgres/postgres.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/audio/core/commands/player.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/alias/alias.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/mutes/voicemutes.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/customcom/customcom.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/audio/apis/local_db.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/downloader/downloader.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/core/_drivers/json.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/audio/core/utilities/player.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/core/commands/requires.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/audio/core/utilities/miscellaneous.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/audio/core/utilities/formatting.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/vendored/discord/ext/menus/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/core/bot.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/trivia/schema.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/audio/core/commands/playlists.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/audio/core/commands/controller.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/audio/core/tasks/player.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/core/i18n.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/audio/apis/spotify.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/audio/manager.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/trivia/trivia.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/mutes/mutes.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/pytest/core.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/core/commands/commands.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/core/_settings_caches.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/core/_drivers/_mongo.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/core/config.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/mod/kickban.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/core/_drivers/base.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/audio/apis/interface.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/audio/audio_dataclasses.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/core/utils/views.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/audio/converters.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk::redbot/cogs/downloader/repo_manager.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/reports/reports.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/bank.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/general/general.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/vendored/discord/ext/menus/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_diagnoser.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/bot.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/reports/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/audio/equalizer.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/audio/apis/spotify.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/pytest/core.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/audio/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/audio/apis/global_db.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/utils/predicates.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_drivers/_mongo.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/permissions/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/trivia/session.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/admin/announcer.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/config.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_drivers/base.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/utils/views.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_debuginfo.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/audio/converters.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/cleanup/cleanup.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/streams/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/mod/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_drivers/postgres/postgres.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/audio/utils.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/utils/tunnel.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/downloader/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/image/image.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/commands/requires.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/modlog/modlog.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/economy/economy.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/commands/context.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/downloader/installable.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/mutes/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/mutes/abc.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/admin/admin.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/logging.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/downloader/json_mixins.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/mod/abc.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/mutes/mutes.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/commands/commands.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/audio/apis/playlist_wrapper.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/audio/core/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/utils/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/audio/apis/youtube.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/audio/core/cog_utils.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/permissions/permissions.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/commands/converter.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/warnings/warnings.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/utils/chat_formatting.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/alias/alias.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/audio/managed_node/ll_version.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/modlog/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/audio/apis/local_db.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/downloader/downloader.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/filter/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/data_manager.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/dev_commands.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/downloader/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/streams/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/utils/dbtools.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/downloader/repo_manager.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/alias/alias_entry.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/app_commands/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/trivia/schema.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/alias/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/audio/apis/playlist_interface.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/tree.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/customcom/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/audio/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/modlog.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_cog_manager.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/mod/kickban.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/audio/apis/interface.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/audio/audio_dataclasses.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/warnings/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/utils/antispam.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/utils/menus.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/customcom/customcom.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_drivers/json.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/streams/streamtypes.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/cleanup/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/trivia/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/economy/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/commands/help.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/audio/apis/persist_queue_wrapper.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/image/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/streams/streams.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/i18n.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/pytest/rpc.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/audio/manager.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/trivia/trivia.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/admin/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/filter/filter.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/general/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_settings_caches.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/core_commands.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/commands/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/mod/mod.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/reports/reports.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/bank.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/general/general.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/vendored/discord/ext/menus/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_diagnoser.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/bot.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/reports/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/audio/equalizer.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/audio/apis/spotify.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/pytest/core.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/audio/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/audio/apis/global_db.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/utils/predicates.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_drivers/_mongo.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/permissions/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/trivia/session.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/admin/announcer.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/config.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_drivers/base.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/utils/views.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_debuginfo.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/audio/converters.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/cleanup/cleanup.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/streams/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/mod/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_drivers/postgres/postgres.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/audio/utils.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/utils/tunnel.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/downloader/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/image/image.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/commands/requires.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/modlog/modlog.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/economy/economy.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/commands/context.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/downloader/installable.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/mutes/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/mutes/abc.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/admin/admin.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/logging.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/downloader/json_mixins.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/mod/abc.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/mutes/mutes.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/commands/commands.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/audio/apis/playlist_wrapper.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/audio/core/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/utils/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/audio/apis/youtube.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/audio/core/cog_utils.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/permissions/permissions.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/commands/converter.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/warnings/warnings.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/utils/chat_formatting.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/alias/alias.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/audio/managed_node/ll_version.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/modlog/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/audio/apis/local_db.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/downloader/downloader.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/filter/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/data_manager.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/dev_commands.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/downloader/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/streams/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/utils/dbtools.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/downloader/repo_manager.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/alias/alias_entry.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/app_commands/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/trivia/schema.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/alias/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/audio/apis/playlist_interface.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/tree.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/customcom/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/audio/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/modlog.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_cog_manager.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/mod/kickban.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/audio/apis/interface.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/audio/audio_dataclasses.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/warnings/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/utils/antispam.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/utils/menus.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/customcom/customcom.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_drivers/json.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/streams/streamtypes.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/cleanup/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/trivia/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/economy/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/commands/help.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/audio/apis/persist_queue_wrapper.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/image/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/streams/streams.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/i18n.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/pytest/rpc.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/audio/manager.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/trivia/trivia.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/admin/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/filter/filter.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/general/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_settings_caches.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/core_commands.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/commands/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/cogs/mod/mod.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq::redbot/core/_rpc.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/reports/reports.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/bank.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/general/general.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/vendored/discord/ext/menus/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/_diagnoser.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/bot.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/reports/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/equalizer.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/apis/spotify.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/apis/global_db.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/utils/predicates.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/_drivers/_mongo.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/permissions/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/trivia/session.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/admin/announcer.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/config.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/_drivers/base.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/utils/views.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/_debuginfo.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/converters.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/cleanup/cleanup.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/streams/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/mod/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/_drivers/postgres/postgres.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/utils.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/utils/tunnel.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/downloader/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/image/image.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/commands/requires.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/modlog/modlog.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/economy/economy.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/commands/context.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/downloader/installable.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/mutes/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/mutes/abc.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/admin/admin.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/logging.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/downloader/json_mixins.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/mod/abc.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/mutes/mutes.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/commands/commands.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/apis/playlist_wrapper.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/_rpc.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/core/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/utils/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/apis/youtube.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/core/cog_utils.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/permissions/permissions.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/commands/converter.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/warnings/warnings.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/utils/chat_formatting.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/alias/alias.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/modlog/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/apis/local_db.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/downloader/downloader.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/filter/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/data_manager.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/dev_commands.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/downloader/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/streams/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/utils/dbtools.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/downloader/repo_manager.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/alias/alias_entry.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/app_commands/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/trivia/schema.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/alias/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/apis/playlist_interface.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/tree.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/customcom/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/modlog.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/_cog_manager.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/mod/kickban.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/apis/interface.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/audio_dataclasses.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/warnings/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/utils/antispam.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/utils/menus.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/customcom/customcom.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/_drivers/json.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/streams/streamtypes.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/cleanup/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/trivia/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/economy/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/commands/help.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/apis/persist_queue_wrapper.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/image/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/streams/streams.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/i18n.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/manager.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/trivia/trivia.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/filter/filter.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/admin/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/general/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/_settings_caches.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/core_commands.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/commands/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/mod/mod.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/reports/reports.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/bank.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/general/general.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/vendored/discord/ext/menus/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/_diagnoser.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/bot.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/reports/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/equalizer.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/apis/spotify.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/apis/global_db.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/utils/predicates.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/_drivers/_mongo.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/permissions/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/trivia/session.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/admin/announcer.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/config.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/_drivers/base.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/utils/views.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/_debuginfo.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/converters.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/cleanup/cleanup.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/streams/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/mod/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/_drivers/postgres/postgres.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/utils.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/utils/tunnel.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/downloader/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/image/image.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/commands/requires.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/modlog/modlog.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/economy/economy.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/commands/context.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/downloader/installable.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/mutes/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/mutes/abc.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/admin/admin.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/logging.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/downloader/json_mixins.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/mod/abc.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/mutes/mutes.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/commands/commands.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/apis/playlist_wrapper.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/_rpc.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/core/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/utils/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/apis/youtube.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/core/cog_utils.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/permissions/permissions.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/commands/converter.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/warnings/warnings.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/utils/chat_formatting.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/alias/alias.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/modlog/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/apis/local_db.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/downloader/downloader.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/filter/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/data_manager.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/dev_commands.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/downloader/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/streams/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/utils/dbtools.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/downloader/repo_manager.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/alias/alias_entry.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/app_commands/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/trivia/schema.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/alias/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/apis/playlist_interface.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/tree.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/customcom/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/modlog.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/_cog_manager.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/mod/kickban.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/apis/interface.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/audio_dataclasses.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/warnings/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/utils/antispam.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/utils/menus.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/customcom/customcom.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/_drivers/json.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/streams/streamtypes.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/cleanup/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/trivia/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/economy/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/commands/help.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/apis/persist_queue_wrapper.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/image/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/streams/streams.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/i18n.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/manager.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/trivia/trivia.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/filter/filter.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/admin/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/general/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/_settings_caches.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/core_commands.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/core/commands/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/mod/mod.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr::redbot/cogs/audio/managed_node/ll_version.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/reports/reports.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/bank.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/general/general.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/vendored/discord/ext/menus/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/_diagnoser.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/bot.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/reports/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/audio/equalizer.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/audio/apis/spotify.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/audio/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/audio/apis/global_db.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/utils/predicates.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/_drivers/_mongo.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/permissions/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/trivia/session.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/admin/announcer.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/config.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/_drivers/base.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/utils/views.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/_debuginfo.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/audio/converters.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/cleanup/cleanup.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/streams/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/mod/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/_drivers/postgres/postgres.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/audio/utils.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/utils/tunnel.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/downloader/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/image/image.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/commands/requires.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/modlog/modlog.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/economy/economy.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/commands/context.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/downloader/installable.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/mutes/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/mutes/abc.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/admin/admin.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/logging.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/downloader/json_mixins.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/mod/abc.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/mutes/mutes.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/commands/commands.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/audio/apis/playlist_wrapper.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/_rpc.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/audio/core/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/utils/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/audio/apis/youtube.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/audio/core/cog_utils.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/permissions/permissions.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/commands/converter.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/warnings/warnings.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/utils/chat_formatting.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/alias/alias.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/audio/managed_node/ll_version.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/modlog/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/audio/apis/local_db.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/downloader/downloader.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/filter/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/data_manager.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/downloader/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/streams/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/utils/dbtools.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/downloader/repo_manager.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/alias/alias_entry.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/app_commands/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/trivia/schema.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/alias/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/audio/apis/playlist_interface.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/tree.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/customcom/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/audio/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/modlog.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/_cog_manager.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/mod/kickban.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/audio/apis/interface.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/audio/audio_dataclasses.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/warnings/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/utils/antispam.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/utils/menus.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/customcom/customcom.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/_drivers/json.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/streams/streamtypes.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/cleanup/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/trivia/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/economy/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/commands/help.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/audio/apis/persist_queue_wrapper.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/image/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/streams/streams.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/i18n.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/audio/manager.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/trivia/trivia.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/admin/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/filter/filter.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/general/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/_settings_caches.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/core_commands.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/commands/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/mod/mod.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/reports/reports.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/bank.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/general/general.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/vendored/discord/ext/menus/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/_diagnoser.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/bot.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/reports/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/audio/equalizer.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/audio/apis/spotify.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/audio/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/audio/apis/global_db.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/utils/predicates.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/_drivers/_mongo.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/permissions/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/trivia/session.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/admin/announcer.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/config.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/_drivers/base.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/utils/views.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/_debuginfo.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/audio/converters.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/cleanup/cleanup.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/streams/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/mod/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/_drivers/postgres/postgres.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/audio/utils.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/utils/tunnel.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/downloader/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/image/image.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/commands/requires.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/modlog/modlog.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/economy/economy.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/commands/context.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/downloader/installable.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/mutes/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/mutes/abc.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/admin/admin.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/logging.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/downloader/json_mixins.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/mod/abc.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/mutes/mutes.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/commands/commands.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/audio/apis/playlist_wrapper.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/_rpc.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/audio/core/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/utils/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/audio/apis/youtube.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/audio/core/cog_utils.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/permissions/permissions.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/commands/converter.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/warnings/warnings.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/utils/chat_formatting.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/alias/alias.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/audio/managed_node/ll_version.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/modlog/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/audio/apis/local_db.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/downloader/downloader.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/filter/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/data_manager.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/downloader/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/streams/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/utils/dbtools.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/downloader/repo_manager.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/alias/alias_entry.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/app_commands/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/trivia/schema.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/alias/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/audio/apis/playlist_interface.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/tree.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/customcom/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/audio/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/modlog.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/_cog_manager.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/mod/kickban.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/audio/apis/interface.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/audio/audio_dataclasses.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/warnings/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/utils/antispam.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/utils/menus.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/customcom/customcom.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/_drivers/json.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/streams/streamtypes.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/cleanup/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/trivia/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/economy/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/commands/help.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/audio/apis/persist_queue_wrapper.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/image/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/streams/streams.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/i18n.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/audio/manager.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/trivia/trivia.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/admin/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/filter/filter.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/general/__init__.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/_settings_caches.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/core_commands.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/commands/errors.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/cogs/mod/mod.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8::redbot/core/dev_commands.py\\\"], \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/core/_rpc.py\\\": [\\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/core/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/reports/reports.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/core/bank.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/general/general.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/vendored/discord/ext/menus/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/core/_diagnoser.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/core/bot.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/reports/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/audio/equalizer.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/audio/apis/spotify.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/pytest/core.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/audio/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/audio/apis/global_db.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/core/utils/predicates.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/core/_drivers/_mongo.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/permissions/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/trivia/session.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/admin/announcer.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/core/config.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/core/_drivers/base.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/core/utils/views.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/core/_debuginfo.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/audio/converters.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/cleanup/cleanup.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/streams/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/mod/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/core/_drivers/postgres/postgres.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/audio/utils.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/core/utils/tunnel.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/downloader/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/image/image.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/core/commands/requires.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/modlog/modlog.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/economy/economy.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/core/commands/context.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/downloader/installable.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/mutes/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/mutes/abc.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/admin/admin.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/logging.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/downloader/json_mixins.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/mod/abc.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/mutes/mutes.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/core/commands/commands.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/audio/apis/playlist_wrapper.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/audio/core/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/core/utils/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/audio/apis/youtube.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/audio/core/cog_utils.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/permissions/permissions.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/core/commands/converter.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/warnings/warnings.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/core/utils/chat_formatting.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/alias/alias.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/audio/managed_node/ll_version.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/modlog/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/audio/apis/local_db.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/downloader/downloader.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/filter/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/core/data_manager.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/core/dev_commands.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/downloader/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/streams/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/core/utils/dbtools.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/downloader/repo_manager.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/alias/alias_entry.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/core/app_commands/errors.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/trivia/schema.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/alias/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/audio/apis/playlist_interface.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/core/tree.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/customcom/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/audio/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/core/modlog.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/core/_cog_manager.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/mod/kickban.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/audio/apis/interface.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/audio/audio_dataclasses.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/warnings/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/core/utils/antispam.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/core/utils/menus.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/customcom/customcom.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/core/_drivers/json.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/streams/streamtypes.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/cleanup/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/trivia/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/economy/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/core/commands/help.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/audio/apis/persist_queue_wrapper.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/image/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/streams/streams.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/core/i18n.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/pytest/rpc.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/audio/manager.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/trivia/trivia.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/admin/__init__.py\\\", \\\"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623::redbot/cogs/filter/filter.py\\\", \\\"Cog-Creators__Red-DiscordBot
```

---
