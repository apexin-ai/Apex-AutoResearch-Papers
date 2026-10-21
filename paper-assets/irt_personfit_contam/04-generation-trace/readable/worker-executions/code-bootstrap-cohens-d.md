# code bootstrap cohens d

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/workers/worker_code_bootstrap-cohens-d_20260521T142506.log`
- **Structured JSON:** [`1e9eb65314da805b02b0.json`](../../sessions/1e/1e9eb65314da805b02b0.json)

## Before a recorded user message

17 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "session_id": "d9fb7952-a57a-4fbd-a5c5-da55908be85d",
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
  "uuid": "6706700f-aa51-4d9d-a5ea-e74833445f69",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0519-3-projects-irt-personfit-contam/memory/"
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
    "resetsAt": 1779391200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "0f426d34-d199-4dd5-8a20-c74e4331583e",
  "session_id": "d9fb7952-a57a-4fbd-a5c5-da55908be85d"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to collect experimental data from a remote server and compute Bootstrap 95% CI for Cohen's d across multiple experimental conditions. Let me start by collecting the data from the server.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d9fb7952-a57a-4fbd-a5c5-da55908be85d",
  "uuid": "2d4a532e-143b-4086-8f69-23b29ada3f79",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hnk36DfGQi3m7KLh3S7cGA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13045,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13045
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

_source line 5_

先连服务器收集所有 lz* 数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d9fb7952-a57a-4fbd-a5c5-da55908be85d",
  "uuid": "7b940324-d900-4a4c-bac4-b5350163b4dc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hnk36DfGQi3m7KLh3S7cGA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13045,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13045
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

_source line 6_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_015W61uuDZQezUWfePxoBVbN`</summary>

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
  "session_id": "d9fb7952-a57a-4fbd-a5c5-da55908be85d",
  "uuid": "5ecb7b1d-2dd3-429d-afb7-945f55ba0ed2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hnk36DfGQi3m7KLh3S7cGA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13045,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13045
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

_source line 7 · 2026-05-21T14:25:17.390Z_

<details><summary>↩ Tool result · `toolu_015W61uuDZQezUWfePxoBVbN`</summary>

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
  "session_id": "d9fb7952-a57a-4fbd-a5c5-da55908be85d",
  "uuid": "eee73ab8-b7b9-4e5e-bbbe-3e40f98cf040",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__ssh_execute"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
    "total_deferred_tools": 26
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01R7UWc7BCtsApsFbVhvoW1m`</summary>

```json
{
  "server": "westd-35694",
  "command": "ls /root/autodl-tmp/ctrl_contam_pilot/results/ /root/autodl-tmp/ctrl_contam_llama/results/ /root/autodl-tmp/ctrl_contam_arcc/results/ /root/autodl-tmp/ctrl_contam_mistral/results/ 2>&1",
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
  "session_id": "d9fb7952-a57a-4fbd-a5c5-da55908be85d",
  "uuid": "949c045a-8796-46d9-a07c-92d92f0591e3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YU3CHHivmSuJjsHYJKbzAb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 742,
      "cache_read_input_tokens": 24886,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 742
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

_source line 9 · 2026-05-21T14:25:21.294Z_

<details><summary>↩ Tool result · `toolu_01R7UWc7BCtsApsFbVhvoW1m`</summary>

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
  "session_id": "d9fb7952-a57a-4fbd-a5c5-da55908be85d",
  "uuid": "502a2d99-df66-47bb-a1fa-4c704e2c1f01",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01WtPsi9wevLCcRCZWsLcHks`</summary>

```json
{
  "server": "westd-35694",
  "command": "find /root/autodl-tmp/ctrl_contam_pilot/results /root/autodl-tmp/ctrl_contam_llama/results /root/autodl-tmp/ctrl_contam_arcc/results /root/autodl-tmp/ctrl_contam_mistral/results -name \"*results.json\" -type f",
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
  "session_id": "d9fb7952-a57a-4fbd-a5c5-da55908be85d",
  "uuid": "60e9790e-ea56-4126-bca2-6aa215d9bd92",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JbFEBbtSYuXXEUozt6qgpN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 272,
      "cache_read_input_tokens": 25628,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 272
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

_source line 11 · 2026-05-21T14:25:25.882Z_

<details><summary>↩ Tool result · `toolu_01WtPsi9wevLCcRCZWsLcHks`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/ctrl_contam_pilot/results/clean_s1_results.json\\n/root/autodl-tmp/ctrl_contam_pilot/results/contam_50_results.json\\n/root/autodl-tmp/ctrl_contam_pilot/results/clean_s2_results.json\\n/root/autodl-tmp/ctrl_contam_pilot/results/contam_15_results.json\\n/root/autodl-tmp/ctrl_contam_pilot/results/clean_s3_results.json\\n/root/autodl-tmp/ctrl_contam_pilot/results/clean_s4_results.json\\n/root/autodl-tmp/ctrl_contam_pilot/results/clean_s5_results.json\\n/root/autodl-tmp/ctrl_contam_pilot/results/clean_s6_results.json\\n/root/autodl-tmp/ctrl_contam_pilot/results/clean_s8_results.json\\n/root/autodl-tmp/ctrl_contam_pilot/results/clean_s7_results.json\\n/root/autodl-tmp/ctrl_contam_pilot/results/clean_s9_results.json\\n/root/autodl-tmp/ctrl_contam_pilot/results/clean_s10_results.json\\n/root/autodl-tmp/ctrl_contam_llama/results/clean_results.json\\n/root/autodl-tmp/ctrl_contam_llama/results/contam_15_results.json\\n/root/autodl-tmp/ctrl_contam_llama/results/contam_50_results.json\\n/root/autodl-tmp/ctrl_contam_llama/results/clean_s2_results.json\\n/root/autodl-tmp/ctrl_contam_llama/results/clean_s3_results.json\\n/root/autodl-tmp/ctrl_contam_llama/results/clean_s4_results.json\\n/root/autodl-tmp/ctrl_contam_llama/results/clean_s5_results.json\\n/root/autodl-tmp/ctrl_contam_llama/results/clean_s6_results.json\\n/root/autodl-tmp/ctrl_contam_llama/results/clean_s7_results.json\\n/root/autodl-tmp/ctrl_contam_arcc/results/clean_s1_results.json\\n/root/autodl-tmp/ctrl_contam_arcc/results/clean_s2_results.json\\n/root/autodl-tmp/ctrl_contam_arcc/results/contam_15_results.json\\n/root/autodl-tmp/ctrl_contam_arcc/results/contam_50_results.json\\n/root/autodl-tmp/ctrl_contam_mistral/results/clean_results.json\\n/root/autodl-tmp/ctrl_contam_mistral/results/contam_15_results.json\\n/root/autodl-tmp/ctrl_contam_mistral/results/contam_50_results.json\\n/root/autodl-tmp/ctrl_contam_mistral/results/clean_s2_results.json\\n/root/autodl-tmp/ctrl_contam_mistral/results/clean_s3_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.08}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d9fb7952-a57a-4fbd-a5c5-da55908be85d",
  "uuid": "698f394e-77f3-4e12-9b33-7ddc0ddf8608",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/ctrl_contam_pilot/results/clean_s1_results.json\\\\n/root/autodl-tmp/ctrl_contam_pilot/results/contam_50_results.json\\\\n/root/autodl-tmp/ctrl_contam_pilot/results/clean_s2_results.json\\\\n/root/autodl-tmp/ctrl_contam_pilot/results/contam_15_results.json\\\\n/root/autodl-tmp/ctrl_contam_pilot/results/clean_s3_results.json\\\\n/root/autodl-tmp/ctrl_contam_pilot/results/clean_s4_results.json\\\\n/root/autodl-tmp/ctrl_contam_pilot/results/clean_s5_results.json\\\\n/root/autodl-tmp/ctrl_contam_pilot/results/clean_s6_results.json\\\\n/root/autodl-tmp/ctrl_contam_pilot/results/clean_s8_results.json\\\\n/root/autodl-tmp/ctrl_contam_pilot/results/clean_s7_results.json\\\\n/root/autodl-tmp/ctrl_contam_pilot/results/clean_s9_results.json\\\\n/root/autodl-tmp/ctrl_contam_pilot/results/clean_s10_results.json\\\\n/root/autodl-tmp/ctrl_contam_llama/results/clean_results.json\\\\n/root/autodl-tmp/ctrl_contam_llama/results/contam_15_results.json\\\\n/root/autodl-tmp/ctrl_contam_llama/results/contam_50_results.json\\\\n/root/autodl-tmp/ctrl_contam_llama/results/clean_s2_results.json\\\\n/root/autodl-tmp/ctrl_contam_llama/results/clean_s3_results.json\\\\n/root/autodl-tmp/ctrl_contam_llama/results/clean_s4_results.json\\\\n/root/autodl-tmp/ctrl_contam_llama/results/clean_s5_results.json\\\\n/root/autodl-tmp/ctrl_contam_llama/results/clean_s6_results.json\\\\n/root/autodl-tmp/ctrl_contam_llama/results/clean_s7_results.json\\\\n/root/autodl-tmp/ctrl_contam_arcc/results/clean_s1_results.json\\\\n/root/autodl-tmp/ctrl_contam_arcc/results/clean_s2_results.json\\\\n/root/autodl-tmp/ctrl_contam_arcc/results/contam_15_results.json\\\\n/root/autodl-tmp/ctrl_contam_arcc/results/contam_50_results.json\\\\n/root/autodl-tmp/ctrl_contam_mistral/results/clean_results.json\\\\n/root/autodl-tmp/ctrl_contam_mistral/results/contam_15_results.json\\\\n/root/autodl-tmp/ctrl_contam_mistral/results/contam_50_results.json\\\\n/root/autodl-tmp/ctrl_contam_mistral/results/clean_s2_results.json\\\\n/root/autodl-tmp/ctrl_contam_mistral/results/clean_s3_results.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.08}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/ctrl_contam_pilot/results/clean_s1_results.json\\n/root/autodl-tmp/ctrl_contam_pilot/results/contam_50_results.json\\n/root/autodl-tmp/ctrl_contam_pilot/results/clean_s2_results.json\\n/root/autodl-tmp/ctrl_contam_pilot/results/contam_15_results.json\\n/root/autodl-tmp/ctrl_contam_pilot/results/clean_s3_results.json\\n/root/autodl-tmp/ctrl_contam_pilot/results/clean_s4_results.json\\n/root/autodl-tmp/ctrl_contam_pilot/results/clean_s5_results.json\\n/root/autodl-tmp/ctrl_contam_pilot/results/clean_s6_results.json\\n/root/autodl-tmp/ctrl_contam_pilot/results/clean_s8_results.json\\n/root/autodl-tmp/ctrl_contam_pilot/results/clean_s7_results.json\\n/root/autodl-tmp/ctrl_contam_pilot/results/clean_s9_results.json\\n/root/autodl-tmp/ctrl_contam_pilot/results/clean_s10_results.json\\n/root/autodl-tmp/ctrl_contam_llama/results/clean_results.json\\n/root/autodl-tmp/ctrl_contam_llama/results/contam_15_results.json\\n/root/autodl-tmp/ctrl_contam_llama/results/contam_50_results.json\\n/root/autodl-tmp/ctrl_contam_llama/results/clean_s2_results.json\\n/root/autodl-tmp/ctrl_contam_llama/results/clean_s3_results.json\\n/root/autodl-tmp/ctrl_contam_llama/results/clean_s4_results.json\\n/root/autodl-tmp/ctrl_contam_llama/results/clean_s5_results.json\\n/root/autodl-tmp/ctrl_contam_llama/results/clean_s6_results.json\\n/root/autodl-tmp/ctrl_contam_llama/results/clean_s7_results.json\\n/root/autodl-tmp/ctrl_contam_arcc/results/clean_s1_results.json\\n/root/autodl-tmp/ctrl_contam_arcc/results/clean_s2_results.json\\n/root/autodl-tmp/ctrl_contam_arcc/results/contam_15_results.json\\n/root/autodl-tmp/ctrl_contam_arcc/results/contam_50_results.json\\n/root/autodl-tmp/ctrl_contam_mistral/results/clean_results.json\\n/root/autodl-tmp/ctrl_contam_mistral/results/contam_15_results.json\\n/root/autodl-tmp/ctrl_contam_mistral/results/contam_50_results.json\\n/root/autodl-tmp/ctrl_contam_mistral/results/clean_s2_results.json\\n/root/autodl-tmp/ctrl_contam_mistral/results/clean_s3_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.08}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 12_

<details><summary>Logged reasoning block</summary>

```text
Let me now extract all the lz* values from these files. I'll need to read them. Let me use ssh_execute to run a Python script that collects all the data.

Files found:
- Qwen (pilot): clean_s1 through clean_s10 (10 seeds), contam_15, contam_50
- Llama: clean_results (s1), clean_s2 through clean_s7 (7 total), contam_15, contam_50


- ARC-C: clean_s1, clean_s2, contam_15, contam_50 (only 2 clean seeds)
- Mistral: clean_results (s1), clean_s2, clean_s3, contam_15, contam_50 (3 clean seeds)

I notice the seed counts vary significantly across models - ARC-C has notably fewer clean runs than the others. Let me gather all the data first before analyzing the patterns.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d9fb7952-a57a-4fbd-a5c5-da55908be85d",
  "uuid": "ab6953e6-2078-4f2b-8ac7-0464617d8ce3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NykYM9s49A9pmSQwZjwJnq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1074,
      "cache_read_input_tokens": 25900,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1074
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

_source line 13_

数据文件清单已获取。现在用 Python 提取所有 lz* 值并计算 bootstrap Cohen's d。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d9fb7952-a57a-4fbd-a5c5-da55908be85d",
  "uuid": "ce8bce31-288d-48dd-a950-59a3905df1c5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NykYM9s49A9pmSQwZjwJnq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1074,
      "cache_read_input_tokens": 25900,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1074
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

_source line 14_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_014XNkG9mzHy8zUzAST8xAvZ`</summary>

```json
{
  "server": "westd-35694",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 << 'PYEOF'\nimport json, glob, numpy as np\n\ndef load_lz(path):\n    d = json.load(open(path))\n    return d.get(\"lz_star\", d.get(\"lz_star_corrected\"))\n\ndef bootstrap_cohens_d(clean_vals, contam_val, n_boot=10000, seed=42):\n    rng = np.random.RandomState(seed)\n    clean = np.array(clean_vals, dtype=float)\n    n = len(clean)\n    d_obs = (clean.mean() - contam_val) / clean.std(ddof=1)\n    boot_ds = []\n    for _ in range(n_boot):\n        idx = rng.randint(0, n, size=n)\n        bc = clean[idx]\n        sd = bc.std(ddof=1)\n        if sd > 0:\n            boot_ds.append((bc.mean() - contam_val) / sd)\n    boot_ds = np.array(boot_ds)\n    return d_obs, np.percentile(boot_ds, 2.5), np.percentile(boot_ds, 97.5)\n\n# ============ Collect data ============\nprint(\"=\" * 80)\nprint(\"DATA COLLECTION\")\nprint(\"=\" * 80)\n\n# --- Qwen MMLU (pilot) ---\nqwen_clean = []\nfor s in range(1, 11):\n    p = f\"/root/autodl-tmp/ctrl_contam_pilot/results/clean_s{s}_results.json\"\n    try:\n        v = load_lz(p)\n        qwen_clean.append(v)\n        print(f\"Qwen clean s{s}: lz*={v:.4f}\")\n    except Exception as e:\n        print(f\"Qwen clean s{s}: MISSING ({e})\")\n\nqwen_contam = {}\nfor cond in [\"contam_15\", \"contam_50\"]:\n    p = f\"/root/autodl-tmp/ctrl_contam_pilot/results/{cond}_results.json\"\n    try:\n        v = load_lz(p)\n        qwen_contam[cond] = v\n        print(f\"Qwen {cond}: lz*={v:.4f}\")\n    except Exception as e:\n        print(f\"Qwen {cond}: MISSING ({e})\")\n\n# --- Llama MMLU ---\nllama_clean = []\n# s1 is named clean_results.json\nfor p in [\"/root/autodl-tmp/ctrl_contam_llama/results/clean_results.json\"] + \\\n         [f\"/root/autodl-tmp/ctrl_contam_llama/results/clean_s{s}_results.json\" for s in range(2, 11)]:\n    try:\n        v = load_lz(p)\n        llama_clean.append(v)\n        print(f\"Llama {p.split('/')[-1]}: lz*={v:.4f}\")\n    except:\n        pass\n\nllama_contam = {}\nfor cond in [\"contam_15\", \"contam_50\"]:\n    p = f\"/root/autodl-tmp/ctrl_contam_llama/results/{cond}_results.json\"\n    try:\n        v = load_lz(p)\n        llama_contam[cond] = v\n        print(f\"Llama {cond}: lz*={v:.4f}\")\n    except:\n        pass\n\n# --- ARC-C ---\narcc_clean = []\nfor s in range(1, 11):\n    p = f\"/root/autodl-tmp/ctrl_contam_arcc/results/clean_s{s}_results.json\"\n    try:\n        v = load_lz(p)\n        arcc_clean.append(v)\n        print(f\"ARC-C clean s{s}: lz*={v:.4f}\")\n    except:\n        pass\n\narcc_contam = {}\nfor cond in [\"contam_15\", \"contam_50\"]:\n    p = f\"/root/autodl-tmp/ctrl_contam_arcc/results/{cond}_results.json\"\n    try:\n        v = load_lz(p)\n        arcc_contam[cond] = v\n        print(f\"ARC-C {cond}: lz*={v:.4f}\")\n    except:\n        pass\n\n# --- Mistral MMLU ---\nmistral_clean = []\nfor p in [\"/root/autodl-tmp/ctrl_contam_mistral/results/clean_results.json\"] + \\\n         [f\"/root/autodl-tmp/ctrl_contam_mistral/results/clean_s{s}_results.json\" for s in range(2, 11)]:\n    try:\n        v = load_lz(p)\n        mistral_clean.append(v)\n        print(f\"Mistral {p.split('/')[-1]}: lz*={v:.4f}\")\n    except:\n        pass\n\nmistral_contam = {}\nfor cond in [\"contam_15\", \"contam_50\"]:\n    p = f\"/root/autodl-tmp/ctrl_contam_mistral/results/{cond}_results.json\"\n    try:\n        v = load_lz(p)\n        mistral_contam[cond] = v\n        print(f\"Mistral {cond}: lz*={v:.4f}\")\n    except:\n        pass\n\nprint(f\"\\nCounts: Qwen={len(qwen_clean)}, Llama={len(llama_clean)}, ARC-C={len(arcc_clean)}, Mistral={len(mistral_clean)}\")\n\n# ============ Bootstrap Cohen's d ============\nprint(\"\\n\" + \"=\" * 80)\nprint(\"BOOTSTRAP COHEN'S d (10000 resamples, seed=42)\")\nprint(\"=\" * 80)\nprint(f\"{'Model':<10} {'Benchmark':<8} {'Condition':<12} {'n_clean':>7} {'contam_lz*':>11} {'Cohen_d':>9} {'CI_lo':>9} {'CI_hi':>9}\")\nprint(\"-\" * 80)\n\nresults = []\n\ndef do_row(model, bench, cond_name, clean_vals, contam_val):\n    n = len(clean_vals)\n    if n < 3:\n        print(f\"{model:<10} {bench:<8} {cond_name:<12} {n:>7} {contam_val:>11.4f} {'n<3, skip':>9}\")\n        return\n    d, lo, hi = bootstrap_cohens_d(clean_vals, contam_val)\n    print(f\"{model:<10} {bench:<8} {cond_name:<12} {n:>7} {contam_val:>11.4f} {d:>9.3f} {lo:>9.3f} {hi:>9.3f}\")\n    results.append(dict(model=model, bench=bench, cond=cond_name, n=n, contam_lz=contam_val, d=d, ci_lo=lo, ci_hi=hi))\n\nfor cond in [\"contam_15\", \"contam_50\"]:\n    if cond in qwen_contam:\n        do_row(\"Qwen\", \"MMLU\", cond, qwen_clean, qwen_contam[cond])\n\nfor cond in [\"contam_15\", \"contam_50\"]:\n    if cond in llama_contam:\n        do_row(\"Llama\", \"MMLU\", cond, llama_clean, llama_contam[cond])\n\nfor cond in [\"contam_15\", \"contam_50\"]:\n    if cond in arcc_contam:\n        do_row(\"Qwen\", \"ARC-C\", cond, arcc_clean, arcc_contam[cond])\n\nfor cond in [\"contam_15\", \"contam_50\"]:\n    if cond in mistral_contam:\n        do_row(\"Mistral\", \"MMLU\", cond, mistral_clean, mistral_contam[cond])\n\n# Also print clean stats\nprint(\"\\n--- Clean baseline stats ---\")\nfor name, vals in [(\"Qwen MMLU\", qwen_clean), (\"Llama MMLU\", llama_clean), (\"ARC-C\", arcc_clean), (\"Mistral MMLU\", mistral_clean)]:\n    if len(vals) >= 2:\n        a = np.array(vals)\n        print(f\"{name}: n={len(vals)}, mean={a.mean():.4f}, sd={a.std(ddof=1):.4f}, range=[{a.min():.4f}, {a.max():.4f}]\")\n    else:\n        print(f\"{name}: n={len(vals)} (insufficient)\")\n\nPYEOF",
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
  "session_id": "d9fb7952-a57a-4fbd-a5c5-da55908be85d",
  "uuid": "5dff0a22-4f90-4bc9-86bb-30a79fbc4cc1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NykYM9s49A9pmSQwZjwJnq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1074,
      "cache_read_input_tokens": 25900,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1074
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

_source line 15 · 2026-05-21T14:25:57.285Z_

<details><summary>↩ Tool result · `toolu_014XNkG9mzHy8zUzAST8xAvZ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"================================================================================\\nDATA COLLECTION\\n================================================================================\\nQwen clean s1: lz*=9.4676\\nQwen clean s2: lz*=7.0539\\nQwen clean s3: lz*=9.5293\\nQwen clean s4: lz*=8.9673\\nQwen clean s5: lz*=8.5322\\nQwen clean s6: lz*=8.2445\\nQwen clean s7: lz*=8.7702\\nQwen clean s8: lz*=9.1110\\nQwen clean s9: lz*=9.0132\\nQwen clean s10: lz*=8.1492\\nQwen contam_15: lz*=3.8494\\nQwen contam_50: lz*=7.2892\\nLlama clean_results.json: lz*=0.8446\\nLlama clean_s2_results.json: lz*=-0.1823\\nLlama clean_s3_results.json: lz*=-1.0844\\nLlama clean_s4_results.json: lz*=0.0206\\nLlama clean_s5_results.json: lz*=1.7323\\nLlama clean_s6_results.json: lz*=2.8466\\nLlama clean_s7_results.json: lz*=-0.4007\\nLlama contam_15: lz*=-2.9922\\nLlama contam_50: lz*=-3.3313\\nARC-C clean s1: lz*=-5.5107\\nARC-C clean s2: lz*=-5.4929\\nARC-C contam_15: lz*=-5.0322\\nARC-C contam_50: lz*=-4.1847\\nMistral clean_results.json: lz*=5.4175\\nMistral clean_s2_results.json: lz*=-1.0456\\nMistral clean_s3_results.json: lz*=3.2792\\nMistral contam_15: lz*=-1.3849\\nMistral contam_50: lz*=-3.1503\\n\\nCounts: Qwen=10, Llama=7, ARC-C=2, Mistral=3\\n\\n================================================================================\\nBOOTSTRAP COHEN'S d (10000 resamples, seed=42)\\n================================================================================\\nModel      Benchmark Condition    n_clean  contam_lz*   Cohen_d     CI_lo     CI_hi\\n--------------------------------------------------------------------------------\\nQwen       MMLU     contam_15         10      3.8494     6.575     4.540    15.188\\nQwen       MMLU     contam_50         10      7.2892     1.897     1.042     4.945\\nLlama      MMLU     contam_15          7     -2.9922     2.591     2.035     5.818\\nLlama      MMLU     contam_50          7     -3.3313     2.840     2.243     6.470\\nQwen       ARC-C    contam_15          2     -5.0322 n<3, skip\\nQwen       ARC-C    contam_50          2     -4.1847 n<3, skip\\nMistral    MMLU     contam_15          3     -1.3849     1.195     0.668     4.933\\nMistral    MMLU     contam_50          3     -3.1503     1.731     1.141     6.363\\n\\n--- Clean baseline stats ---\\nQwen MMLU: n=10, mean=8.6838, sd=0.7353, range=[7.0539, 9.5293]\\nLlama MMLU: n=7, mean=0.5395, sd=1.3632, range=[-1.0844, 2.8466]\\nARC-C: n=2, mean=-5.5018, sd=0.0126, range=[-5.5107, -5.4929]\\nMistral MMLU: n=3, mean=2.5504, sd=3.2926, range=[-1.0456, 5.4175]\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.33}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d9fb7952-a57a-4fbd-a5c5-da55908be85d",
  "uuid": "79ceba82-1bd7-4bbe-9456-6d33bceaa1ad",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"================================================================================\\\\nDATA COLLECTION\\\\n================================================================================\\\\nQwen clean s1: lz*=9.4676\\\\nQwen clean s2: lz*=7.0539\\\\nQwen clean s3: lz*=9.5293\\\\nQwen clean s4: lz*=8.9673\\\\nQwen clean s5: lz*=8.5322\\\\nQwen clean s6: lz*=8.2445\\\\nQwen clean s7: lz*=8.7702\\\\nQwen clean s8: lz*=9.1110\\\\nQwen clean s9: lz*=9.0132\\\\nQwen clean s10: lz*=8.1492\\\\nQwen contam_15: lz*=3.8494\\\\nQwen contam_50: lz*=7.2892\\\\nLlama clean_results.json: lz*=0.8446\\\\nLlama clean_s2_results.json: lz*=-0.1823\\\\nLlama clean_s3_results.json: lz*=-1.0844\\\\nLlama clean_s4_results.json: lz*=0.0206\\\\nLlama clean_s5_results.json: lz*=1.7323\\\\nLlama clean_s6_results.json: lz*=2.8466\\\\nLlama clean_s7_results.json: lz*=-0.4007\\\\nLlama contam_15: lz*=-2.9922\\\\nLlama contam_50: lz*=-3.3313\\\\nARC-C clean s1: lz*=-5.5107\\\\nARC-C clean s2: lz*=-5.4929\\\\nARC-C contam_15: lz*=-5.0322\\\\nARC-C contam_50: lz*=-4.1847\\\\nMistral clean_results.json: lz*=5.4175\\\\nMistral clean_s2_results.json: lz*=-1.0456\\\\nMistral clean_s3_results.json: lz*=3.2792\\\\nMistral contam_15: lz*=-1.3849\\\\nMistral contam_50: lz*=-3.1503\\\\n\\\\nCounts: Qwen=10, Llama=7, ARC-C=2, Mistral=3\\\\n\\\\n================================================================================\\\\nBOOTSTRAP COHEN'S d (10000 resamples, seed=42)\\\\n================================================================================\\\\nModel      Benchmark Condition    n_clean  contam_lz*   Cohen_d     CI_lo     CI_hi\\\\n--------------------------------------------------------------------------------\\\\nQwen       MMLU     contam_15         10      3.8494     6.575     4.540    15.188\\\\nQwen       MMLU     contam_50         10      7.2892     1.897     1.042     4.945\\\\nLlama      MMLU     contam_15          7     -2.9922     2.591     2.035     5.818\\\\nLlama      MMLU     contam_50          7     -3.3313     2.840     2.243     6.470\\\\nQwen       ARC-C    contam_15          2     -5.0322 n<3, skip\\\\nQwen       ARC-C    contam_50          2     -4.1847 n<3, skip\\\\nMistral    MMLU     contam_15          3     -1.3849     1.195     0.668     4.933\\\\nMistral    MMLU     contam_50          3     -3.1503     1.731     1.141     6.363\\\\n\\\\n--- Clean baseline stats ---\\\\nQwen MMLU: n=10, mean=8.6838, sd=0.7353, range=[7.0539, 9.5293]\\\\nLlama MMLU: n=7, mean=0.5395, sd=1.3632, range=[-1.0844, 2.8466]\\\\nARC-C: n=2, mean=-5.5018, sd=0.0126, range=[-5.5107, -5.4929]\\\\nMistral MMLU: n=3, mean=2.5504, sd=3.2926, range=[-1.0456, 5.4175]\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.33}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"================================================================================\\nDATA COLLECTION\\n================================================================================\\nQwen clean s1: lz*=9.4676\\nQwen clean s2: lz*=7.0539\\nQwen clean s3: lz*=9.5293\\nQwen clean s4: lz*=8.9673\\nQwen clean s5: lz*=8.5322\\nQwen clean s6: lz*=8.2445\\nQwen clean s7: lz*=8.7702\\nQwen clean s8: lz*=9.1110\\nQwen clean s9: lz*=9.0132\\nQwen clean s10: lz*=8.1492\\nQwen contam_15: lz*=3.8494\\nQwen contam_50: lz*=7.2892\\nLlama clean_results.json: lz*=0.8446\\nLlama clean_s2_results.json: lz*=-0.1823\\nLlama clean_s3_results.json: lz*=-1.0844\\nLlama clean_s4_results.json: lz*=0.0206\\nLlama clean_s5_results.json: lz*=1.7323\\nLlama clean_s6_results.json: lz*=2.8466\\nLlama clean_s7_results.json: lz*=-0.4007\\nLlama contam_15: lz*=-2.9922\\nLlama contam_50: lz*=-3.3313\\nARC-C clean s1: lz*=-5.5107\\nARC-C clean s2: lz*=-5.4929\\nARC-C contam_15: lz*=-5.0322\\nARC-C contam_50: lz*=-4.1847\\nMistral clean_results.json: lz*=5.4175\\nMistral clean_s2_results.json: lz*=-1.0456\\nMistral clean_s3_results.json: lz*=3.2792\\nMistral contam_15: lz*=-1.3849\\nMistral contam_50: lz*=-3.1503\\n\\nCounts: Qwen=10, Llama=7, ARC-C=2, Mistral=3\\n\\n================================================================================\\nBOOTSTRAP COHEN'S d (10000 resamples, seed=42)\\n================================================================================\\nModel      Benchmark Condition    n_clean  contam_lz*   Cohen_d     CI_lo     CI_hi\\n--------------------------------------------------------------------------------\\nQwen       MMLU     contam_15         10      3.8494     6.575     4.540    15.188\\nQwen       MMLU     contam_50         10      7.2892     1.897     1.042     4.945\\nLlama      MMLU     contam_15          7     -2.9922     2.591     2.035     5.818\\nLlama      MMLU     contam_50          7     -3.3313     2.840     2.243     6.470\\nQwen       ARC-C    contam_15          2     -5.0322 n<3, skip\\nQwen       ARC-C    contam_50          2     -4.1847 n<3, skip\\nMistral    MMLU     contam_15          3     -1.3849     1.195     0.668     4.933\\nMistral    MMLU     contam_50          3     -3.1503     1.731     1.141     6.363\\n\\n--- Clean baseline stats ---\\nQwen MMLU: n=10, mean=8.6838, sd=0.7353, range=[7.0539, 9.5293]\\nLlama MMLU: n=7, mean=0.5395, sd=1.3632, range=[-1.0844, 2.8466]\\nARC-C: n=2, mean=-5.5018, sd=0.0126, range=[-5.5107, -5.4929]\\nMistral MMLU: n=3, mean=2.5504, sd=3.2926, range=[-1.0456, 5.4175]\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.33}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 16_

结果如下：

## Bootstrap Cohen's d (10,000 resamples, seed=42)

| Model | Benchmark | Condition | n_clean | contam lz* | Cohen's d | 95% CI lower | 95% CI upper |
|-------|-----------|-----------|---------|------------|-----------|-------------|-------------|
| Qwen | MMLU | contam_15 | 10 | 3.8494 | **6.575** | 4.540 | 15.188 |
| Qwen | MMLU | contam_50 | 10 | 7.2892 | **1.897** | 1.042 | 4.945 |
| Llama | MMLU | contam_15 | 7 | −2.9922 | **2.591** | 2.035 | 5.818 |
| Llama | MMLU | contam_50 | 7 | −3.3313 | **2.840** | 2.243 | 6.470 |
| Mistral | MMLU | contam_15 | 3 | −1.3849 | **1.195** | 0.668 | 4.933 |
| Mistral | MMLU | contam_50 | 3 | −3.1503 | **1.731** | 1.141 | 6.363 |

**ARC-C 跳过**：仅 2 个 clean seeds，不足以计算。

## Clean baseline 统计

| Group | n | mean | sd | range |
|-------|---|------|----|----- |
| Qwen MMLU | 10 | 8.684 | 0.735 | [7.054, 9.529] |
| Llama MMLU | 7 | 0.540 | 1.363 | [−1.084, 2.847] |
| ARC-C | 2 | −5.502 | 0.013 | [−5.511, −5.493] |
| Mistral MMLU | 3 | 2.550 | 3.293 | [−1.046, 5.418] |

所有条件的 95% CI 下界均 > 0，效应显著。Qwen contam_15 效应量最大（d=6.6），CI 非常宽是因为 contam lz* 远离 clean 分布。Mistral n=3 估计不稳定，CI 较宽。ARC-C 需等更多 clean seeds 完成后再算。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d9fb7952-a57a-4fbd-a5c5-da55908be85d",
  "uuid": "33c1d049-eef1-4adb-8580-28f1f5732edd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X2EZtpptDKGCmqWSoH9v8n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3789,
      "cache_read_input_tokens": 26974,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3789
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

_source line 17_

结果如下：

## Bootstrap Cohen's d (10,000 resamples, seed=42)

| Model | Benchmark | Condition | n_clean | contam lz* | Cohen's d | 95% CI lower | 95% CI upper |
|-------|-----------|-----------|---------|------------|-----------|-------------|-------------|
| Qwen | MMLU | contam_15 | 10 | 3.8494 | **6.575** | 4.540 | 15.188 |
| Qwen | MMLU | contam_50 | 10 | 7.2892 | **1.897** | 1.042 | 4.945 |
| Llama | MMLU | contam_15 | 7 | −2.9922 | **2.591** | 2.035 | 5.818 |
| Llama | MMLU | contam_50 | 7 | −3.3313 | **2.840** | 2.243 | 6.470 |
| Mistral | MMLU | contam_15 | 3 | −1.3849 | **1.195** | 0.668 | 4.933 |
| Mistral | MMLU | contam_50 | 3 | −3.1503 | **1.731** | 1.141 | 6.363 |

**ARC-C 跳过**：仅 2 个 clean seeds，不足以计算。

## Clean baseline 统计

| Group | n | mean | sd | range |
|-------|---|------|----|----- |
| Qwen MMLU | 10 | 8.684 | 0.735 | [7.054, 9.529] |
| Llama MMLU | 7 | 0.540 | 1.363 | [−1.084, 2.847] |
| ARC-C | 2 | −5.502 | 0.013 | [−5.511, −5.493] |
| Mistral MMLU | 3 | 2.550 | 3.293 | [−1.046, 5.418] |

所有条件的 95% CI 下界均 > 0，效应显著。Qwen contam_15 效应量最大（d=6.6），CI 非常宽是因为 contam lz* 远离 clean 分布。Mistral n=3 估计不稳定，CI 较宽。ARC-C 需等更多 clean seeds 完成后再算。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 54780,
  "duration_api_ms": 53623,
  "num_turns": 5,
  "stop_reason": "end_turn",
  "session_id": "d9fb7952-a57a-4fbd-a5c5-da55908be85d",
  "total_cost_usd": 0.273623,
  "usage": {
    "input_tokens": 8,
    "cache_creation_input_tokens": 18922,
    "cache_read_input_tokens": 115229,
    "output_tokens": 3812,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 18922,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 661,
        "cache_read_input_tokens": 26974,
        "cache_creation_input_tokens": 3789,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 3789
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2321,
      "outputTokens": 17,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002406,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 8,
      "outputTokens": 3812,
      "cacheReadInputTokens": 115229,
      "cacheCreationInputTokens": 18922,
      "webSearchRequests": 0,
      "costUSD": 0.27121700000000004,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "87eb2e5d-06fc-46c1-8621-d067eca79f81"
}
```

</details>

---
