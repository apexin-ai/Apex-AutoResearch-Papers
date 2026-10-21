# code d134 analysis isr star patch

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 92
- **Recorded user turns:** 0
- **Tool calls:** 29
- **Original source:** `logs/workers/worker_code_d134-analysis-isr-star-patch_20260518T233104.log`
- **Structured JSON:** [`2ce87f3436d4523c7d47.json`](../../sessions/2c/2ce87f3436d4523c7d47.json)

## Before a recorded user message

92 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
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
  "uuid": "501f355f-736e-48a2-a036-387528f59681",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/memory/"
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
    "resetsAt": 1779162600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "e678f2ec-9156-48d1-9446-27b2bd1d9d0e",
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by executing the SSH commands to check the eval_results.json files and read the existing script.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "1984b257-4cb4-432c-84df-b19e2cf7e312",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NiUtGdMTuKtGBCssCtg4m6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16029,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16029
      },
      "output_tokens": 27,
      "service_tier": "standard",
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

I'll start by checking the ISR* field names in eval_results.json and reading the existing script in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "bfae96cc-f152-48ba-8704-7b23bb1d2d3e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NiUtGdMTuKtGBCssCtg4m6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16029,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16029
      },
      "output_tokens": 27,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HQBs88nYbvuwMorZWgpXxK`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only",
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
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "28406877-d52f-446d-b05d-94ce8bcdad56",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NiUtGdMTuKtGBCssCtg4m6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16029,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16029
      },
      "output_tokens": 27,
      "service_tier": "standard",
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

_source line 7 · 2026-05-18T23:31:20.181Z_

<details><summary>↩ Tool result · `toolu_01HQBs88nYbvuwMorZWgpXxK`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_execute"
}
```

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
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "8a0bd721-0557-458d-8c22-e07876e8ecd7",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__ssh_read_only"
    ],
    "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Assistant

_source line 8_

Now let me check the eval_results.json fields and read the existing script in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "e9e347e1-ccf2-448d-b15d-956540f9ed08",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bffw6YMBz5GUSdSmL4E8eC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 734,
      "cache_read_input_tokens": 27870,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 734
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_018bsYQdJh1oVTwv9skzCWFg`</summary>

```json
{
  "server": "westd-39279",
  "account": "root",
  "command": "for s in 47 48 49 50 51; do\n  echo \"=== ISR s${s} eval_results.json ===\"\n  /root/miniconda3/bin/python3 -c \"\nimport json\nwith open('/root/autodl-tmp/outputs/d134_4b_isr_b01_s${s}/eval_results.json') as f:\n    d = json.load(f)\nfor k,v in d.items():\n    if 'isr' in k.lower():\n        print(f'  {k}: {v}')\nif 'summary' in d:\n    for k,v in d['summary'].items():\n        if 'isr' in k.lower():\n            print(f'  summary.{k}: {v}')\n\" 2>/dev/null\ndone\n\nfor s in 47 48 49; do\n  echo \"=== Random s${s} eval_results.json ===\"\n  /root/miniconda3/bin/python3 -c \"\nimport json\nwith open('/root/autodl-tmp/outputs/d134_4b_random_b01_s${s}/eval_results.json') as f:\n    d = json.load(f)\nfor k,v in d.items():\n    if 'isr' in k.lower():\n        print(f'  {k}: {v}')\nif 'summary' in d:\n    for k,v in d['summary'].items():\n        if 'isr' in k.lower():\n            print(f'  summary.{k}: {v}')\n\" 2>/dev/null\ndone"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "e4750a09-e76b-4f95-abc4-efba2c4ceab9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bffw6YMBz5GUSdSmL4E8eC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 734,
      "cache_read_input_tokens": 27870,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 734
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

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01P3tnYUQeVPVUbb8iPza2K2`</summary>

```json
{
  "server": "westd-39279",
  "account": "root",
  "command": "cat /root/solver-trace-ablation/scripts/d134_analysis.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "06cba9c5-bb95-4cb5-ad99-d92dd46bc2db",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bffw6YMBz5GUSdSmL4E8eC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 734,
      "cache_read_input_tokens": 27870,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 734
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

_source line 11 · 2026-05-18T23:31:28.101Z_

<details><summary>↩ Tool result · `toolu_018bsYQdJh1oVTwv9skzCWFg`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== ISR s47 eval_results.json ===\\n  summary.mean_isr: 0.55\\n  summary.isr_std: 0.1827\\n  summary.median_isr: 0.5\\n  summary.isr_pr_ratio: 0.567\\n  summary.proved_only_mean_isr: 0.567\\n  summary.min_isr: 0.0\\n  summary.max_isr: 1.0\\n=== ISR s48 eval_results.json ===\\n  summary.mean_isr: 0.4925\\n  summary.isr_std: 0.3579\\n  summary.median_isr: 0.75\\n  summary.isr_pr_ratio: 0.7462\\n  summary.proved_only_mean_isr: 0.7462\\n  summary.min_isr: 0.0\\n  summary.max_isr: 1.0\\n=== ISR s49 eval_results.json ===\\n  summary.mean_isr: 0.4592\\n  summary.isr_std: 0.2249\\n  summary.median_isr: 0.5\\n  summary.isr_pr_ratio: 0.5339\\n  summary.proved_only_mean_isr: 0.5339\\n  summary.min_isr: 0.0\\n  summary.max_isr: 1.0\\n=== ISR s50 eval_results.json ===\\n  summary.mean_isr: 0.7128\\n  summary.isr_std: 0.1829\\n  summary.median_isr: 0.75\\n  summary.isr_pr_ratio: 0.7274\\n  summary.proved_only_mean_isr: 0.7274\\n  summary.min_isr: 0.0\\n  summary.max_isr: 1.0\\n=== ISR s51 eval_results.json ===\\n  summary.mean_isr: 0.6992\\n  summary.isr_std: 0.1584\\n  summary.median_isr: 0.75\\n  summary.isr_pr_ratio: 0.7134\\n  summary.proved_only_mean_isr: 0.7134\\n  summary.min_isr: 0.0\\n  summary.max_isr: 1.0\\n=== Random s47 eval_results.json ===\\n  summary.mean_isr: 0.0857\\n  summary.isr_std: 0.1259\\n  summary.median_isr: 0.0\\n  summary.isr_pr_ratio: 0.0963\\n  summary.proved_only_mean_isr: 0.0963\\n  summary.min_isr: 0.0\\n  summary.max_isr: 0.5\\n=== Random s48 eval_results.json ===\\n  summary.mean_isr: 0.0581\\n  summary.isr_std: 0.1132\\n  summary.median_isr: 0.0\\n  summary.isr_pr_ratio: 0.0625\\n  summary.proved_only_mean_isr: 0.0625\\n  summary.min_isr: 0.0\\n  summary.max_isr: 0.6\\n=== Random s49 eval_results.json ===\\n  summary.mean_isr: 0.0057\\n  summary.isr_std: 0.0504\\n  summary.median_isr: 0.0\\n  summary.isr_pr_ratio: 0.1143\\n  summary.proved_only_mean_isr: 0.1143\\n  summary.min_isr: 0.0\\n  summary.max_isr: 0.5\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.51}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "b4e01d46-7de7-42b3-bb56-6ee156a65672",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"=== ISR s47 eval_results.json ===\\\\n  summary.mean_isr: 0.55\\\\n  summary.isr_std: 0.1827\\\\n  summary.median_isr: 0.5\\\\n  summary.isr_pr_ratio: 0.567\\\\n  summary.proved_only_mean_isr: 0.567\\\\n  summary.min_isr: 0.0\\\\n  summary.max_isr: 1.0\\\\n=== ISR s48 eval_results.json ===\\\\n  summary.mean_isr: 0.4925\\\\n  summary.isr_std: 0.3579\\\\n  summary.median_isr: 0.75\\\\n  summary.isr_pr_ratio: 0.7462\\\\n  summary.proved_only_mean_isr: 0.7462\\\\n  summary.min_isr: 0.0\\\\n  summary.max_isr: 1.0\\\\n=== ISR s49 eval_results.json ===\\\\n  summary.mean_isr: 0.4592\\\\n  summary.isr_std: 0.2249\\\\n  summary.median_isr: 0.5\\\\n  summary.isr_pr_ratio: 0.5339\\\\n  summary.proved_only_mean_isr: 0.5339\\\\n  summary.min_isr: 0.0\\\\n  summary.max_isr: 1.0\\\\n=== ISR s50 eval_results.json ===\\\\n  summary.mean_isr: 0.7128\\\\n  summary.isr_std: 0.1829\\\\n  summary.median_isr: 0.75\\\\n  summary.isr_pr_ratio: 0.7274\\\\n  summary.proved_only_mean_isr: 0.7274\\\\n  summary.min_isr: 0.0\\\\n  summary.max_isr: 1.0\\\\n=== ISR s51 eval_results.json ===\\\\n  summary.mean_isr: 0.6992\\\\n  summary.isr_std: 0.1584\\\\n  summary.median_isr: 0.75\\\\n  summary.isr_pr_ratio: 0.7134\\\\n  summary.proved_only_mean_isr: 0.7134\\\\n  summary.min_isr: 0.0\\\\n  summary.max_isr: 1.0\\\\n=== Random s47 eval_results.json ===\\\\n  summary.mean_isr: 0.0857\\\\n  summary.isr_std: 0.1259\\\\n  summary.median_isr: 0.0\\\\n  summary.isr_pr_ratio: 0.0963\\\\n  summary.proved_only_mean_isr: 0.0963\\\\n  summary.min_isr: 0.0\\\\n  summary.max_isr: 0.5\\\\n=== Random s48 eval_results.json ===\\\\n  summary.mean_isr: 0.0581\\\\n  summary.isr_std: 0.1132\\\\n  summary.median_isr: 0.0\\\\n  summary.isr_pr_ratio: 0.0625\\\\n  summary.proved_only_mean_isr: 0.0625\\\\n  summary.min_isr: 0.0\\\\n  summary.max_isr: 0.6\\\\n=== Random s49 eval_results.json ===\\\\n  summary.mean_isr: 0.0057\\\\n  summary.isr_std: 0.0504\\\\n  summary.median_isr: 0.0\\\\n  summary.isr_pr_ratio: 0.1143\\\\n  summary.proved_only_mean_isr: 0.1143\\\\n  summary.min_isr: 0.0\\\\n  summary.max_isr: 0.5\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.51}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"=== ISR s47 eval_results.json ===\\n  summary.mean_isr: 0.55\\n  summary.isr_std: 0.1827\\n  summary.median_isr: 0.5\\n  summary.isr_pr_ratio: 0.567\\n  summary.proved_only_mean_isr: 0.567\\n  summary.min_isr: 0.0\\n  summary.max_isr: 1.0\\n=== ISR s48 eval_results.json ===\\n  summary.mean_isr: 0.4925\\n  summary.isr_std: 0.3579\\n  summary.median_isr: 0.75\\n  summary.isr_pr_ratio: 0.7462\\n  summary.proved_only_mean_isr: 0.7462\\n  summary.min_isr: 0.0\\n  summary.max_isr: 1.0\\n=== ISR s49 eval_results.json ===\\n  summary.mean_isr: 0.4592\\n  summary.isr_std: 0.2249\\n  summary.median_isr: 0.5\\n  summary.isr_pr_ratio: 0.5339\\n  summary.proved_only_mean_isr: 0.5339\\n  summary.min_isr: 0.0\\n  summary.max_isr: 1.0\\n=== ISR s50 eval_results.json ===\\n  summary.mean_isr: 0.7128\\n  summary.isr_std: 0.1829\\n  summary.median_isr: 0.75\\n  summary.isr_pr_ratio: 0.7274\\n  summary.proved_only_mean_isr: 0.7274\\n  summary.min_isr: 0.0\\n  summary.max_isr: 1.0\\n=== ISR s51 eval_results.json ===\\n  summary.mean_isr: 0.6992\\n  summary.isr_std: 0.1584\\n  summary.median_isr: 0.75\\n  summary.isr_pr_ratio: 0.7134\\n  summary.proved_only_mean_isr: 0.7134\\n  summary.min_isr: 0.0\\n  summary.max_isr: 1.0\\n=== Random s47 eval_results.json ===\\n  summary.mean_isr: 0.0857\\n  summary.isr_std: 0.1259\\n  summary.median_isr: 0.0\\n  summary.isr_pr_ratio: 0.0963\\n  summary.proved_only_mean_isr: 0.0963\\n  summary.min_isr: 0.0\\n  summary.max_isr: 0.5\\n=== Random s48 eval_results.json ===\\n  summary.mean_isr: 0.0581\\n  summary.isr_std: 0.1132\\n  summary.median_isr: 0.0\\n  summary.isr_pr_ratio: 0.0625\\n  summary.proved_only_mean_isr: 0.0625\\n  summary.min_isr: 0.0\\n  summary.max_isr: 0.6\\n=== Random s49 eval_results.json ===\\n  summary.mean_isr: 0.0057\\n  summary.isr_std: 0.0504\\n  summary.median_isr: 0.0\\n  summary.isr_pr_ratio: 0.1143\\n  summary.proved_only_mean_isr: 0.1143\\n  summary.min_isr: 0.0\\n  summary.max_isr: 0.5\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.51}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-18T23:31:28.684Z_

<details><summary>↩ Tool result · `toolu_01P3tnYUQeVPVUbb8iPza2K2`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/root/miniconda3/bin/python\\n\\\"\\\"\\\"D134 experiment analysis: multi-seed ISR vs Random, 4B GRPO training.\\nReads taxonomy data from classify.json, taxonomy.json, or top-level taxonomy files.\\nComputes summary stats, statistical tests (Fisher, Mann-Whitney, permutation, Bayes Factor),\\nand BCa bootstrap CIs. Outputs appendix-ready markdown.\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport re\\nimport sys\\nfrom pathlib import Path\\n\\nimport numpy as np\\nimport pandas as pd\\nfrom scipy import stats\\nfrom scipy.special import betaln\\n\\nCONDITION_MAP = [\\n    (\\\"d134_4b_isr\\\", \\\"ISR\\\"),\\n    (\\\"d134_4b_random\\\", \\\"RANDOM\\\"),\\n    (\\\"plan002_additive\\\", \\\"ISR\\\"),\\n    (\\\"plan018_additive_random\\\", \\\"RANDOM\\\"),\\n    (\\\"plan018_random\\\", \\\"RANDOM\\\"),\\n]\\n\\nMODE_PREFIXES = {\\n    \\\"d134_only\\\": [\\\"d134_4b\\\"],\\n    \\\"all\\\": [\\\"d134_4b\\\", \\\"plan002_additive_b01\\\", \\\"plan018_additive_random_b01\\\", \\\"plan018_random\\\"],\\n}\\n\\n\\ndef parse_args():\\n    p = argparse.ArgumentParser(description=\\\"D134 multi-seed analysis and statistical tests\\\")\\n    p.add_argument(\\\"--data_dir\\\", type=str, default=\\\"/root/autodl-tmp/outputs\\\",\\n                   help=\\\"Directory containing experiment outputs\\\")\\n    p.add_argument(\\\"--mode\\\", type=str, default=\\\"d134_only\\\", choices=list(MODE_PREFIXES),\\n                   help=\\\"d134_only = matched 5+5 design (default); all = include original seeds\\\")\\n    p.add_argument(\\\"--prefix\\\", type=str, default=None,\\n                   help=\\\"(Legacy) Single prefix filter; overrides mode/prefixes\\\")\\n    p.add_argument(\\\"--prefixes\\\", type=str, default=None,\\n                   help=\\\"Comma-separated prefixes; overrides --mode\\\")\\n    p.add_argument(\\\"--output\\\", type=str, default=None,\\n                   help=\\\"Write markdown summary to this file\\\")\\n    p.add_argument(\\\"--n_perm\\\", type=int, default=10000,\\n                   help=\\\"Number of permutations for permutation test\\\")\\n    p.add_argument(\\\"--n_boot\\\", type=int, default=10000,\\n                   help=\\\"Number of bootstrap resamples for BCa CI\\\")\\n    p.add_argument(\\\"--seed\\\", type=int, default=42,\\n                   help=\\\"Random seed for permutation/bootstrap\\\")\\n    return p.parse_args()\\n\\n\\n# --- Data loading ---\\n\\ndef match_condition(name: str) -> str | None:\\n    best_prefix = \\\"\\\"\\n    best_cond = None\\n    for prefix, cond in CONDITION_MAP:\\n        if name.startswith(prefix) and len(prefix) > len(best_prefix):\\n            best_prefix = prefix\\n            best_cond = cond\\n    return best_cond\\n\\n\\ndef extract_seed(name: str) -> int | None:\\n    m = re.search(r'_s(\\\\d+)', name)\\n    return int(m.group(1)) if m else None\\n\\n\\ndef load_eval_results(path: Path) -> dict | None:\\n    if not path.exists():\\n        return None\\n    with open(path) as f:\\n        data = json.load(f)\\n    if \\\"eval_results\\\" in data:\\n        return data[\\\"eval_results\\\"]\\n    return data\\n\\n\\ndef load_taxonomy_unified(path: Path) -> dict | None:\\n    with open(path) as f:\\n        raw = json.load(f)\\n    t = raw.get(\\\"taxonomy\\\", {})\\n    proved = t.get(\\\"proved\\\", 0)\\n    if proved == 0:\\n        return None\\n    h7 = t.get(\\\"H7\\\", 0)\\n    h1 = t.get(\\\"H1_exact\\\", 0)\\n    h8 = t.get(\\\"H8\\\", 0)\\n    genuine = t.get(\\\"genuine\\\", 0)\\n    return {\\n        \\\"n_total\\\": 100, \\\"n_proved\\\": proved,\\n        \\\"h7_total_count\\\": h7, \\\"h7_total_rate\\\": h7 / proved,\\n        \\\"h1_strict_count\\\": h1, \\\"h8_conjunction_collapse_count\\\": h8,\\n        \\\"genuine_count\\\": genuine, \\\"genuine_rate\\\": genuine / proved,\\n        \\\"content_independent_count\\\": 0,\\n    }\\n\\n\\ndef load_taxonomy_verification(path: Path) -> dict | None:\\n    with open(path) as f:\\n        raw = json.load(f)\\n    proved = raw.get(\\\"proved\\\", 0)\\n    if proved == 0:\\n        return None\\n    tax = raw.get(\\\"taxonomy\\\", {})\\n    h7 = tax.get(\\\"h7\\\", {}).get(\\\"count\\\", 0)\\n    h1 = tax.get(\\\"h1_exact\\\", {}).get(\\\"count\\\", 0)\\n    h8 = tax.get(\\\"h8\\\", {}).get(\\\"count\\\", 0)\\n    genuine = tax.get(\\\"genuine\\\", {}).get(\\\"count\\\", 0)\\n    return {\\n        \\\"n_total\\\": raw.get(\\\"total\\\", 100), \\\"n_proved\\\": proved,\\n        \\\"h7_total_count\\\": h7, \\\"h7_total_rate\\\": h7 / proved,\\n        \\\"h1_strict_count\\\": h1, \\\"h8_conjunction_collapse_count\\\": h8,\\n        \\\"genuine_count\\\"\\n\\n... [截断: 输出过长，省略 14602 字符] ...\\n\\nt('or_ci_hi', np.inf)) or np.isnan(fisher.get('or_ci_hi', np.nan)) else f\\\"{fisher['or_ci_hi']:.2f}\\\"\\n        L.append(\\\"**1. H7 Domination Fisher Exact Test** (threshold: H7$\\\\\\\\geq$50\\\\\\\\% of proved)\\\")\\n        L.append(f\\\"- ISR: {fisher['ISR']['h7_dom']}/{fisher['ISR']['n']} seeds H7-dominated; \\\"\\n                 f\\\"Random: {fisher['RANDOM']['h7_dom']}/{fisher['RANDOM']['n']}\\\")\\n        L.append(f\\\"- OR = {or_str}, 95\\\\\\\\% exact CI = [{ci_lo}, {ci_hi}], \\\"\\n                 f\\\"$p$ = {fmt_p(fisher['p_value'])}\\\")\\n        L.append(\\\"\\\")\\n\\n        # Permutation\\n        L.append(f\\\"**2. Genuine Rate Permutation Test** ($n$ = {perm['n_perm']:,} permutations)\\\")\\n        L.append(f\\\"- ISR mean: {perm['isr_mean']*100:.2f}\\\\\\\\%, Random mean: {perm['random_mean']*100:.2f}\\\\\\\\%\\\")\\n        L.append(f\\\"- $\\\\\\\\Delta$ = {perm['observed_diff']*100:.2f} pp, $p$ = {fmt_p(perm['p_value'])}\\\")\\n        L.append(\\\"\\\")\\n\\n        # Mann-Whitney\\n        L.append(\\\"**3. H7 Rate Mann-Whitney $U$ Test**\\\")\\n        L.append(f\\\"- ISR median: {mw['isr_median']*100:.1f}\\\\\\\\%, Random median: {mw['random_median']*100:.1f}\\\\\\\\%\\\")\\n        L.append(f\\\"- $U$ = {mw['U']:.1f}, $p$ = {fmt_p(mw['p_value'])}, \\\"\\n                 f\\\"rank-biserial $r$ = {mw['r_rank_biserial']:.3f}\\\")\\n        L.append(\\\"\\\")\\n\\n        # Bayes Factor\\n        L.append(\\\"**4. Bayes Factor** (Beta-Binomial conjugate, prior: Beta(1,1))\\\")\\n        L.append(f\\\"- $BF_{{10}}$ = {bf['bf10']:.2f} ({bf['interpretation']})\\\")\\n        L.append(f\\\"- ISR: {bf['k_isr']}/{bf['n_isr']} H7-dominated, \\\"\\n                 f\\\"Random: {bf['k_rand']}/{bf['n_rand']}\\\")\\n\\n    return \\\"\\\\n\\\".join(L) + \\\"\\\\n\\\"\\n\\n\\n# --- Main ---\\n\\ndef main():\\n    args = parse_args()\\n    data_dir = Path(args.data_dir)\\n\\n    if not data_dir.exists():\\n        print(f\\\"ERROR: data directory {data_dir} does not exist\\\", file=sys.stderr)\\n        sys.exit(1)\\n\\n    if args.prefix:\\n        prefixes = [args.prefix]\\n    elif args.prefixes:\\n        prefixes = [p.strip() for p in args.prefixes.split(\\\",\\\")]\\n    else:\\n        prefixes = MODE_PREFIXES[args.mode]\\n    print(f\\\"Mode: {args.mode} | Prefixes: {prefixes}\\\")\\n\\n    runs = discover_runs(data_dir, prefixes)\\n    if not runs:\\n        print(f\\\"ERROR: no runs found in {data_dir} with prefixes {prefixes}\\\", file=sys.stderr)\\n        sys.exit(1)\\n\\n    isr_count = sum(1 for r in runs if r[\\\"condition\\\"] == \\\"ISR\\\")\\n    rand_count = sum(1 for r in runs if r[\\\"condition\\\"] == \\\"RANDOM\\\")\\n    print(f\\\"Found {len(runs)} runs: {isr_count} ISR, {rand_count} RANDOM\\\")\\n    for r in runs:\\n        print(f\\\"  {r['condition']:6s} s{r['seed']} <- {r['dir_name']}\\\")\\n\\n    df = build_table(runs)\\n    print_per_seed_table(df)\\n\\n    cond_df = condition_stats(df)\\n    print_condition_stats(cond_df)\\n\\n    if isr_count < 2 or rand_count < 2:\\n        print(\\\"\\\\nWARNING: need >= 2 seeds per condition for statistical tests, skipping.\\\",\\n              file=sys.stderr)\\n        bca_h7 = bca_bootstrap_ci(df, \\\"H7_rate\\\", args.n_boot, args.seed)\\n        bca_gen = bca_bootstrap_ci(df, \\\"genuine_rate\\\", args.n_boot, args.seed)\\n        if args.output:\\n            md = generate_markdown(df, cond_df, {}, {}, {}, {}, bca_h7, bca_gen)\\n            Path(args.output).write_text(md)\\n            print(f\\\"\\\\nMarkdown written to {args.output}\\\")\\n        return\\n\\n    fisher = fisher_h7_domination(df)\\n    perm = permutation_test_genuine(df, n_perm=args.n_perm, rng_seed=args.seed)\\n    mw = mannwhitney_h7(df)\\n    bf = bayes_factor_h7_domination(df)\\n    bca_h7 = bca_bootstrap_ci(df, \\\"H7_rate\\\", args.n_boot, args.seed)\\n    bca_gen = bca_bootstrap_ci(df, \\\"genuine_rate\\\", args.n_boot, args.seed)\\n\\n    print_tests(fisher, perm, mw, bf, bca_h7, bca_gen)\\n\\n    md = generate_markdown(df, cond_df, fisher, perm, mw, bf, bca_h7, bca_gen)\\n    print(\\\"\\\\n\\\" + \\\"=\\\" * 90)\\n    print(\\\"  MARKDOWN OUTPUT (appendix-ready)\\\")\\n    print(\\\"=\\\" * 90)\\n    print(md)\\n\\n    if args.output:\\n        Path(args.output).parent.mkdir(parents=True, exist_ok=True)\\n        Path(args.output).write_text(md)\\n        print(f\\\"Markdown written to {args.output}\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.57}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "21d70d41-200c-4939-a4ee-7d8f395dc8ba",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/root/miniconda3/bin/python\\\\n\\\\\\\"\\\\\\\"\\\\\\\"D134 experiment analysis: multi-seed ISR vs Random, 4B GRPO training.\\\\nReads taxonomy data from classify.json, taxonomy.json, or top-level taxonomy files.\\\\nComputes summary stats, statistical tests (Fisher, Mann-Whitney, permutation, Bayes Factor),\\\\nand BCa bootstrap CIs. Outputs appendix-ready markdown.\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport argparse\\\\nimport json\\\\nimport re\\\\nimport sys\\\\nfrom pathlib import Path\\\\n\\\\nimport numpy as np\\\\nimport pandas as pd\\\\nfrom scipy import stats\\\\nfrom scipy.special import betaln\\\\n\\\\nCONDITION_MAP = [\\\\n    (\\\\\\\"d134_4b_isr\\\\\\\", \\\\\\\"ISR\\\\\\\"),\\\\n    (\\\\\\\"d134_4b_random\\\\\\\", \\\\\\\"RANDOM\\\\\\\"),\\\\n    (\\\\\\\"plan002_additive\\\\\\\", \\\\\\\"ISR\\\\\\\"),\\\\n    (\\\\\\\"plan018_additive_random\\\\\\\", \\\\\\\"RANDOM\\\\\\\"),\\\\n    (\\\\\\\"plan018_random\\\\\\\", \\\\\\\"RANDOM\\\\\\\"),\\\\n]\\\\n\\\\nMODE_PREFIXES = {\\\\n    \\\\\\\"d134_only\\\\\\\": [\\\\\\\"d134_4b\\\\\\\"],\\\\n    \\\\\\\"all\\\\\\\": [\\\\\\\"d134_4b\\\\\\\", \\\\\\\"plan002_additive_b01\\\\\\\", \\\\\\\"plan018_additive_random_b01\\\\\\\", \\\\\\\"plan018_random\\\\\\\"],\\\\n}\\\\n\\\\n\\\\ndef parse_args():\\\\n    p = argparse.ArgumentParser(description=\\\\\\\"D134 multi-seed analysis and statistical tests\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--data_dir\\\\\\\", type=str, default=\\\\\\\"/root/autodl-tmp/outputs\\\\\\\",\\\\n                   help=\\\\\\\"Directory containing experiment outputs\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--mode\\\\\\\", type=str, default=\\\\\\\"d134_only\\\\\\\", choices=list(MODE_PREFIXES),\\\\n                   help=\\\\\\\"d134_only = matched 5+5 design (default); all = include original seeds\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--prefix\\\\\\\", type=str, default=None,\\\\n                   help=\\\\\\\"(Legacy) Single prefix filter; overrides mode/prefixes\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--prefixes\\\\\\\", type=str, default=None,\\\\n                   help=\\\\\\\"Comma-separated prefixes; overrides --mode\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--output\\\\\\\", type=str, default=None,\\\\n                   help=\\\\\\\"Write markdown summary to this file\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--n_perm\\\\\\\", type=int, default=10000,\\\\n                   help=\\\\\\\"Number of permutations for permutation test\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--n_boot\\\\\\\", type=int, default=10000,\\\\n                   help=\\\\\\\"Number of bootstrap resamples for BCa CI\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--seed\\\\\\\", type=int, default=42,\\\\n                   help=\\\\\\\"Random seed for permutation/bootstrap\\\\\\\")\\\\n    return p.parse_args()\\\\n\\\\n\\\\n# --- Data loading ---\\\\n\\\\ndef match_condition(name: str) -> str | None:\\\\n    best_prefix = \\\\\\\"\\\\\\\"\\\\n    best_cond = None\\\\n    for prefix, cond in CONDITION_MAP:\\\\n        if name.startswith(prefix) and len(prefix) > len(best_prefix):\\\\n            best_prefix = prefix\\\\n            best_cond = cond\\\\n    return best_cond\\\\n\\\\n\\\\ndef extract_seed(name: str) -> int | None:\\\\n    m = re.search(r'_s(\\\\\\\\d+)', name)\\\\n    return int(m.group(1)) if m else None\\\\n\\\\n\\\\ndef load_eval_results(path: Path) -> dict | None:\\\\n    if not path.exists():\\\\n        return None\\\\n    with open(path) as f:\\\\n        data = json.load(f)\\\\n    if \\\\\\\"eval_results\\\\\\\" in data:\\\\n        return data[\\\\\\\"eval_results\\\\\\\"]\\\\n    return data\\\\n\\\\n\\\\ndef load_taxonomy_unified(path: Path) -> dict | None:\\\\n    with open(path) as f:\\\\n        raw = json.load(f)\\\\n    t = raw.get(\\\\\\\"taxonomy\\\\\\\", {})\\\\n    proved = t.get(\\\\\\\"proved\\\\\\\", 0)\\\\n    if proved == 0:\\\\n        return None\\\\n    h7 = t.get(\\\\\\\"H7\\\\\\\", 0)\\\\n    h1 = t.get(\\\\\\\"H1_exact\\\\\\\", 0)\\\\n    h8 = t.get(\\\\\\\"H8\\\\\\\", 0)\\\\n    genuine = t.get(\\\\\\\"genuine\\\\\\\", 0)\\\\n    return {\\\\n        \\\\\\\"n_total\\\\\\\": 100, \\\\\\\"n_proved\\\\\\\": proved,\\\\n        \\\\\\\"h7_total_count\\\\\\\": h7, \\\\\\\"h7_total_rate\\\\\\\": h7 / proved,\\\\n        \\\\\\\"h1_strict_count\\\\\\\": h1, \\\\\\\"h8_conjunction_collapse_count\\\\\\\": h8,\\\\n        \\\\\\\"genuine_count\\\\\\\": genuine, \\\\\\\"genuine_rate\\\\\\\": genuine / proved,\\\\n        \\\\\\\"content_independent_count\\\\\\\": 0,\\\\n    }\\\\n\\\\n\\\\ndef load_taxonomy_verification(path: Path) -> dict | None:\\\\n    with open(path) as f:\\\\n        raw = json.load(f)\\\\n    proved = raw.get(\\\\\\\"proved\\\\\\\", 0)\\\\n    if proved == 0:\\\\n        return None\\\\n    tax = raw.get(\\\\\\\"taxonomy\\\\\\\", {})\\\\n    h7 = tax.get(\\\\\\\"h7\\\\\\\", {}).get(\\\\\\\"count\\\\\\\", 0)\\\\n    h1 = tax.get(\\\\\\\"h1_exact\\\\\\\", {}).get(\\\\\\\"count\\\\\\\", 0)\\\\n    h8 = tax.get(\\\\\\\"h8\\\\\\\", {}).get(\\\\\\\"count\\\\\\\", 0)\\\\n    genuine = tax.get(\\\\\\\"genuine\\\\\\\", {}).get(\\\\\\\"count\\\\\\\", 0)\\\\n    return {\\\\n        \\\\\\\"n_total\\\\\\\": raw.get(\\\\\\\"total\\\\\\\", 100), \\\\\\\"n_proved\\\\\\\": proved,\\\\n        \\\\\\\"h7_total_count\\\\\\\": h7, \\\\\\\"h7_total_rate\\\\\\\": h7 / proved,\\\\n        \\\\\\\"h1_strict_count\\\\\\\": h1, \\\\\\\"h8_conjunction_collapse_count\\\\\\\": h8,\\\\n        \\\\\\\"genuine_count\\\\\\\"\\\\n\\\\n... [截断: 输出过长，省略 14602 字符] ...\\\\n\\\\nt('or_ci_hi', np.inf)) or np.isnan(fisher.get('or_ci_hi', np.nan)) else f\\\\\\\"{fisher['or_ci_hi']:.2f}\\\\\\\"\\\\n        L.append(\\\\\\\"**1. H7 Domination Fisher Exact Test** (threshold: H7$\\\\\\\\\\\\\\\\geq$50\\\\\\\\\\\\\\\\% of proved)\\\\\\\")\\\\n        L.append(f\\\\\\\"- ISR: {fisher['ISR']['h7_dom']}/{fisher['ISR']['n']} seeds H7-dominated; \\\\\\\"\\\\n                 f\\\\\\\"Random: {fisher['RANDOM']['h7_dom']}/{fisher['RANDOM']['n']}\\\\\\\")\\\\n        L.append(f\\\\\\\"- OR = {or_str}, 95\\\\\\\\\\\\\\\\% exact CI = [{ci_lo}, {ci_hi}], \\\\\\\"\\\\n                 f\\\\\\\"$p$ = {fmt_p(fisher['p_value'])}\\\\\\\")\\\\n        L.append(\\\\\\\"\\\\\\\")\\\\n\\\\n        # Permutation\\\\n        L.append(f\\\\\\\"**2. Genuine Rate Permutation Test** ($n$ = {perm['n_perm']:,} permutations)\\\\\\\")\\\\n        L.append(f\\\\\\\"- ISR mean: {perm['isr_mean']*100:.2f}\\\\\\\\\\\\\\\\%, Random mean: {perm['random_mean']*100:.2f}\\\\\\\\\\\\\\\\%\\\\\\\")\\\\n        L.append(f\\\\\\\"- $\\\\\\\\\\\\\\\\Delta$ = {perm['observed_diff']*100:.2f} pp, $p$ = {fmt_p(perm['p_value'])}\\\\\\\")\\\\n        L.append(\\\\\\\"\\\\\\\")\\\\n\\\\n        # Mann-Whitney\\\\n        L.append(\\\\\\\"**3. H7 Rate Mann-Whitney $U$ Test**\\\\\\\")\\\\n        L.append(f\\\\\\\"- ISR median: {mw['isr_median']*100:.1f}\\\\\\\\\\\\\\\\%, Random median: {mw['random_median']*100:.1f}\\\\\\\\\\\\\\\\%\\\\\\\")\\\\n        L.append(f\\\\\\\"- $U$ = {mw['U']:.1f}, $p$ = {fmt_p(mw['p_value'])}, \\\\\\\"\\\\n                 f\\\\\\\"rank-biserial $r$ = {mw['r_rank_biserial']:.3f}\\\\\\\")\\\\n        L.append(\\\\\\\"\\\\\\\")\\\\n\\\\n        # Bayes Factor\\\\n        L.append(\\\\\\\"**4. Bayes Factor** (Beta-Binomial conjugate, prior: Beta(1,1))\\\\\\\")\\\\n        L.append(f\\\\\\\"- $BF_{{10}}$ = {bf['bf10']:.2f} ({bf['interpretation']})\\\\\\\")\\\\n        L.append(f\\\\\\\"- ISR: {bf['k_isr']}/{bf['n_isr']} H7-dominated, \\\\\\\"\\\\n                 f\\\\\\\"Random: {bf['k_rand']}/{bf['n_rand']}\\\\\\\")\\\\n\\\\n    return \\\\\\\"\\\\\\\\n\\\\\\\".join(L) + \\\\\\\"\\\\\\\\n\\\\\\\"\\\\n\\\\n\\\\n# --- Main ---\\\\n\\\\ndef main():\\\\n    args = parse_args()\\\\n    data_dir = Path(args.data_dir)\\\\n\\\\n    if not data_dir.exists():\\\\n        print(f\\\\\\\"ERROR: data directory {data_dir} does not exist\\\\\\\", file=sys.stderr)\\\\n        sys.exit(1)\\\\n\\\\n    if args.prefix:\\\\n        prefixes = [args.prefix]\\\\n    elif args.prefixes:\\\\n        prefixes = [p.strip() for p in args.prefixes.split(\\\\\\\",\\\\\\\")]\\\\n    else:\\\\n        prefixes = MODE_PREFIXES[args.mode]\\\\n    print(f\\\\\\\"Mode: {args.mode} | Prefixes: {prefixes}\\\\\\\")\\\\n\\\\n    runs = discover_runs(data_dir, prefixes)\\\\n    if not runs:\\\\n        print(f\\\\\\\"ERROR: no runs found in {data_dir} with prefixes {prefixes}\\\\\\\", file=sys.stderr)\\\\n        sys.exit(1)\\\\n\\\\n    isr_count = sum(1 for r in runs if r[\\\\\\\"condition\\\\\\\"] == \\\\\\\"ISR\\\\\\\")\\\\n    rand_count = sum(1 for r in runs if r[\\\\\\\"condition\\\\\\\"] == \\\\\\\"RANDOM\\\\\\\")\\\\n    print(f\\\\\\\"Found {len(runs)} runs: {isr_count} ISR, {rand_count} RANDOM\\\\\\\")\\\\n    for r in runs:\\\\n        print(f\\\\\\\"  {r['condition']:6s} s{r['seed']} <- {r['dir_name']}\\\\\\\")\\\\n\\\\n    df = build_table(runs)\\\\n    print_per_seed_table(df)\\\\n\\\\n    cond_df = condition_stats(df)\\\\n    print_condition_stats(cond_df)\\\\n\\\\n    if isr_count < 2 or rand_count < 2:\\\\n        print(\\\\\\\"\\\\\\\\nWARNING: need >= 2 seeds per condition for statistical tests, skipping.\\\\\\\",\\\\n              file=sys.stderr)\\\\n        bca_h7 = bca_bootstrap_ci(df, \\\\\\\"H7_rate\\\\\\\", args.n_boot, args.seed)\\\\n        bca_gen = bca_bootstrap_ci(df, \\\\\\\"genuine_rate\\\\\\\", args.n_boot, args.seed)\\\\n        if args.output:\\\\n            md = generate_markdown(df, cond_df, {}, {}, {}, {}, bca_h7, bca_gen)\\\\n            Path(args.output).write_text(md)\\\\n            print(f\\\\\\\"\\\\\\\\nMarkdown written to {args.output}\\\\\\\")\\\\n        return\\\\n\\\\n    fisher = fisher_h7_domination(df)\\\\n    perm = permutation_test_genuine(df, n_perm=args.n_perm, rng_seed=args.seed)\\\\n    mw = mannwhitney_h7(df)\\\\n    bf = bayes_factor_h7_domination(df)\\\\n    bca_h7 = bca_bootstrap_ci(df, \\\\\\\"H7_rate\\\\\\\", args.n_boot, args.seed)\\\\n    bca_gen = bca_bootstrap_ci(df, \\\\\\\"genuine_rate\\\\\\\", args.n_boot, args.seed)\\\\n\\\\n    print_tests(fisher, perm, mw, bf, bca_h7, bca_gen)\\\\n\\\\n    md = generate_markdown(df, cond_df, fisher, perm, mw, bf, bca_h7, bca_gen)\\\\n    print(\\\\\\\"\\\\\\\\n\\\\\\\" + \\\\\\\"=\\\\\\\" * 90)\\\\n    print(\\\\\\\"  MARKDOWN OUTPUT (appendix-ready)\\\\\\\")\\\\n    print(\\\\\\\"=\\\\\\\" * 90)\\\\n    print(md)\\\\n\\\\n    if args.output:\\\\n        Path(args.output).parent.mkdir(parents=True, exist_ok=True)\\\\n        Path(args.output).write_text(md)\\\\n        print(f\\\\\\\"Markdown written to {args.output}\\\\\\\")\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.57}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/root/miniconda3/bin/python\\n\\\"\\\"\\\"D134 experiment analysis: multi-seed ISR vs Random, 4B GRPO training.\\nReads taxonomy data from classify.json, taxonomy.json, or top-level taxonomy files.\\nComputes summary stats, statistical tests (Fisher, Mann-Whitney, permutation, Bayes Factor),\\nand BCa bootstrap CIs. Outputs appendix-ready markdown.\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport re\\nimport sys\\nfrom pathlib import Path\\n\\nimport numpy as np\\nimport pandas as pd\\nfrom scipy import stats\\nfrom scipy.special import betaln\\n\\nCONDITION_MAP = [\\n    (\\\"d134_4b_isr\\\", \\\"ISR\\\"),\\n    (\\\"d134_4b_random\\\", \\\"RANDOM\\\"),\\n    (\\\"plan002_additive\\\", \\\"ISR\\\"),\\n    (\\\"plan018_additive_random\\\", \\\"RANDOM\\\"),\\n    (\\\"plan018_random\\\", \\\"RANDOM\\\"),\\n]\\n\\nMODE_PREFIXES = {\\n    \\\"d134_only\\\": [\\\"d134_4b\\\"],\\n    \\\"all\\\": [\\\"d134_4b\\\", \\\"plan002_additive_b01\\\", \\\"plan018_additive_random_b01\\\", \\\"plan018_random\\\"],\\n}\\n\\n\\ndef parse_args():\\n    p = argparse.ArgumentParser(description=\\\"D134 multi-seed analysis and statistical tests\\\")\\n    p.add_argument(\\\"--data_dir\\\", type=str, default=\\\"/root/autodl-tmp/outputs\\\",\\n                   help=\\\"Directory containing experiment outputs\\\")\\n    p.add_argument(\\\"--mode\\\", type=str, default=\\\"d134_only\\\", choices=list(MODE_PREFIXES),\\n                   help=\\\"d134_only = matched 5+5 design (default); all = include original seeds\\\")\\n    p.add_argument(\\\"--prefix\\\", type=str, default=None,\\n                   help=\\\"(Legacy) Single prefix filter; overrides mode/prefixes\\\")\\n    p.add_argument(\\\"--prefixes\\\", type=str, default=None,\\n                   help=\\\"Comma-separated prefixes; overrides --mode\\\")\\n    p.add_argument(\\\"--output\\\", type=str, default=None,\\n                   help=\\\"Write markdown summary to this file\\\")\\n    p.add_argument(\\\"--n_perm\\\", type=int, default=10000,\\n                   help=\\\"Number of permutations for permutation test\\\")\\n    p.add_argument(\\\"--n_boot\\\", type=int, default=10000,\\n                   help=\\\"Number of bootstrap resamples for BCa CI\\\")\\n    p.add_argument(\\\"--seed\\\", type=int, default=42,\\n                   help=\\\"Random seed for permutation/bootstrap\\\")\\n    return p.parse_args()\\n\\n\\n# --- Data loading ---\\n\\ndef match_condition(name: str) -> str | None:\\n    best_prefix = \\\"\\\"\\n    best_cond = None\\n    for prefix, cond in CONDITION_MAP:\\n        if name.startswith(prefix) and len(prefix) > len(best_prefix):\\n            best_prefix = prefix\\n            best_cond = cond\\n    return best_cond\\n\\n\\ndef extract_seed(name: str) -> int | None:\\n    m = re.search(r'_s(\\\\d+)', name)\\n    return int(m.group(1)) if m else None\\n\\n\\ndef load_eval_results(path: Path) -> dict | None:\\n    if not path.exists():\\n        return None\\n    with open(path) as f:\\n        data = json.load(f)\\n    if \\\"eval_results\\\" in data:\\n        return data[\\\"eval_results\\\"]\\n    return data\\n\\n\\ndef load_taxonomy_unified(path: Path) -> dict | None:\\n    with open(path) as f:\\n        raw = json.load(f)\\n    t = raw.get(\\\"taxonomy\\\", {})\\n    proved = t.get(\\\"proved\\\", 0)\\n    if proved == 0:\\n        return None\\n    h7 = t.get(\\\"H7\\\", 0)\\n    h1 = t.get(\\\"H1_exact\\\", 0)\\n    h8 = t.get(\\\"H8\\\", 0)\\n    genuine = t.get(\\\"genuine\\\", 0)\\n    return {\\n        \\\"n_total\\\": 100, \\\"n_proved\\\": proved,\\n        \\\"h7_total_count\\\": h7, \\\"h7_total_rate\\\": h7 / proved,\\n        \\\"h1_strict_count\\\": h1, \\\"h8_conjunction_collapse_count\\\": h8,\\n        \\\"genuine_count\\\": genuine, \\\"genuine_rate\\\": genuine / proved,\\n        \\\"content_independent_count\\\": 0,\\n    }\\n\\n\\ndef load_taxonomy_verification(path: Path) -> dict | None:\\n    with open(path) as f:\\n        raw = json.load(f)\\n    proved = raw.get(\\\"proved\\\", 0)\\n    if proved == 0:\\n        return None\\n    tax = raw.get(\\\"taxonomy\\\", {})\\n    h7 = tax.get(\\\"h7\\\", {}).get(\\\"count\\\", 0)\\n    h1 = tax.get(\\\"h1_exact\\\", {}).get(\\\"count\\\", 0)\\n    h8 = tax.get(\\\"h8\\\", {}).get(\\\"count\\\", 0)\\n    genuine = tax.get(\\\"genuine\\\", {}).get(\\\"count\\\", 0)\\n    return {\\n        \\\"n_total\\\": raw.get(\\\"total\\\", 100), \\\"n_proved\\\": proved,\\n        \\\"h7_total_count\\\": h7, \\\"h7_total_rate\\\": h7 / proved,\\n        \\\"h1_strict_count\\\": h1, \\\"h8_conjunction_collapse_count\\\": h8,\\n        \\\"genuine_count\\\"\\n\\n... [截断: 输出过长，省略 14602 字符] ...\\n\\nt('or_ci_hi', np.inf)) or np.isnan(fisher.get('or_ci_hi', np.nan)) else f\\\"{fisher['or_ci_hi']:.2f}\\\"\\n        L.append(\\\"**1. H7 Domination Fisher Exact Test** (threshold: H7$\\\\\\\\geq$50\\\\\\\\% of proved)\\\")\\n        L.append(f\\\"- ISR: {fisher['ISR']['h7_dom']}/{fisher['ISR']['n']} seeds H7-dominated; \\\"\\n                 f\\\"Random: {fisher['RANDOM']['h7_dom']}/{fisher['RANDOM']['n']}\\\")\\n        L.append(f\\\"- OR = {or_str}, 95\\\\\\\\% exact CI = [{ci_lo}, {ci_hi}], \\\"\\n                 f\\\"$p$ = {fmt_p(fisher['p_value'])}\\\")\\n        L.append(\\\"\\\")\\n\\n        # Permutation\\n        L.append(f\\\"**2. Genuine Rate Permutation Test** ($n$ = {perm['n_perm']:,} permutations)\\\")\\n        L.append(f\\\"- ISR mean: {perm['isr_mean']*100:.2f}\\\\\\\\%, Random mean: {perm['random_mean']*100:.2f}\\\\\\\\%\\\")\\n        L.append(f\\\"- $\\\\\\\\Delta$ = {perm['observed_diff']*100:.2f} pp, $p$ = {fmt_p(perm['p_value'])}\\\")\\n        L.append(\\\"\\\")\\n\\n        # Mann-Whitney\\n        L.append(\\\"**3. H7 Rate Mann-Whitney $U$ Test**\\\")\\n        L.append(f\\\"- ISR median: {mw['isr_median']*100:.1f}\\\\\\\\%, Random median: {mw['random_median']*100:.1f}\\\\\\\\%\\\")\\n        L.append(f\\\"- $U$ = {mw['U']:.1f}, $p$ = {fmt_p(mw['p_value'])}, \\\"\\n                 f\\\"rank-biserial $r$ = {mw['r_rank_biserial']:.3f}\\\")\\n        L.append(\\\"\\\")\\n\\n        # Bayes Factor\\n        L.append(\\\"**4. Bayes Factor** (Beta-Binomial conjugate, prior: Beta(1,1))\\\")\\n        L.append(f\\\"- $BF_{{10}}$ = {bf['bf10']:.2f} ({bf['interpretation']})\\\")\\n        L.append(f\\\"- ISR: {bf['k_isr']}/{bf['n_isr']} H7-dominated, \\\"\\n                 f\\\"Random: {bf['k_rand']}/{bf['n_rand']}\\\")\\n\\n    return \\\"\\\\n\\\".join(L) + \\\"\\\\n\\\"\\n\\n\\n# --- Main ---\\n\\ndef main():\\n    args = parse_args()\\n    data_dir = Path(args.data_dir)\\n\\n    if not data_dir.exists():\\n        print(f\\\"ERROR: data directory {data_dir} does not exist\\\", file=sys.stderr)\\n        sys.exit(1)\\n\\n    if args.prefix:\\n        prefixes = [args.prefix]\\n    elif args.prefixes:\\n        prefixes = [p.strip() for p in args.prefixes.split(\\\",\\\")]\\n    else:\\n        prefixes = MODE_PREFIXES[args.mode]\\n    print(f\\\"Mode: {args.mode} | Prefixes: {prefixes}\\\")\\n\\n    runs = discover_runs(data_dir, prefixes)\\n    if not runs:\\n        print(f\\\"ERROR: no runs found in {data_dir} with prefixes {prefixes}\\\", file=sys.stderr)\\n        sys.exit(1)\\n\\n    isr_count = sum(1 for r in runs if r[\\\"condition\\\"] == \\\"ISR\\\")\\n    rand_count = sum(1 for r in runs if r[\\\"condition\\\"] == \\\"RANDOM\\\")\\n    print(f\\\"Found {len(runs)} runs: {isr_count} ISR, {rand_count} RANDOM\\\")\\n    for r in runs:\\n        print(f\\\"  {r['condition']:6s} s{r['seed']} <- {r['dir_name']}\\\")\\n\\n    df = build_table(runs)\\n    print_per_seed_table(df)\\n\\n    cond_df = condition_stats(df)\\n    print_condition_stats(cond_df)\\n\\n    if isr_count < 2 or rand_count < 2:\\n        print(\\\"\\\\nWARNING: need >= 2 seeds per condition for statistical tests, skipping.\\\",\\n              file=sys.stderr)\\n        bca_h7 = bca_bootstrap_ci(df, \\\"H7_rate\\\", args.n_boot, args.seed)\\n        bca_gen = bca_bootstrap_ci(df, \\\"genuine_rate\\\", args.n_boot, args.seed)\\n        if args.output:\\n            md = generate_markdown(df, cond_df, {}, {}, {}, {}, bca_h7, bca_gen)\\n            Path(args.output).write_text(md)\\n            print(f\\\"\\\\nMarkdown written to {args.output}\\\")\\n        return\\n\\n    fisher = fisher_h7_domination(df)\\n    perm = permutation_test_genuine(df, n_perm=args.n_perm, rng_seed=args.seed)\\n    mw = mannwhitney_h7(df)\\n    bf = bayes_factor_h7_domination(df)\\n    bca_h7 = bca_bootstrap_ci(df, \\\"H7_rate\\\", args.n_boot, args.seed)\\n    bca_gen = bca_bootstrap_ci(df, \\\"genuine_rate\\\", args.n_boot, args.seed)\\n\\n    print_tests(fisher, perm, mw, bf, bca_h7, bca_gen)\\n\\n    md = generate_markdown(df, cond_df, fisher, perm, mw, bf, bca_h7, bca_gen)\\n    print(\\\"\\\\n\\\" + \\\"=\\\" * 90)\\n    print(\\\"  MARKDOWN OUTPUT (appendix-ready)\\\")\\n    print(\\\"=\\\" * 90)\\n    print(md)\\n\\n    if args.output:\\n        Path(args.output).parent.mkdir(parents=True, exist_ok=True)\\n        Path(args.output).write_text(md)\\n        print(f\\\"Markdown written to {args.output}\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.57}}"
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
The output was truncated. I need to read the full script. Let me get the full content from the local copy or read it again in sections. Let me first check what we have locally.

Key findings so far:
1. ISR* field name is `summary.proved_only_mean_isr` in eval_results.json
2. ISR values:
   - ISR s47: 0.567
   - ISR s48: 0.7462
   - ISR s49: 0.5339
   - ISR s50: 0.7274
   - ISR s51: 0.7134
   - Random s47: 0.0963
   - Random s48: 0.0625
   - Random s49: 0.1143

Now I need to read the full script to understand the structure since the SSH output was truncated.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "3245c6e0-f0ef-4658-b468-92fd237b59a1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FvWXmsoeJrxSJCPzhGtHq7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5466,
      "cache_read_input_tokens": 28604,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5466
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

ISR* field is `summary.proved_only_mean_isr`. Now let me read the full local script since the SSH output was truncated.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "3122824f-9905-4330-b7fe-f8387c44be58",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FvWXmsoeJrxSJCPzhGtHq7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5466,
      "cache_read_input_tokens": 28604,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5466
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

<details open><summary>🔧 Tool call — Read · `toolu_015RvcHBdYPrr8rjcHaJ1FNb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/scripts/d134_analysis.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "073ff025-fe6c-4322-a4e4-cea7a9082a84",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FvWXmsoeJrxSJCPzhGtHq7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5466,
      "cache_read_input_tokens": 28604,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5466
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

_source line 16 · 2026-05-18T23:31:36.543Z_

<details><summary>↩ Tool result · `toolu_015RvcHBdYPrr8rjcHaJ1FNb`</summary>

```text
1	#!/usr/bin/env python3
2	"""D134 experiment analysis: multi-seed ISR vs Random, 4B GRPO training.
3	Reads taxonomy data from classify.json, taxonomy.json, or top-level taxonomy files.
4	Computes summary stats, statistical tests (Fisher, Mann-Whitney, permutation, Bayes Factor),
5	and BCa bootstrap CIs. Outputs appendix-ready markdown.
6	"""
7	
8	import argparse
9	import json
10	import re
11	import sys
12	from pathlib import Path
13	
14	import numpy as np
15	import pandas as pd
16	from scipy import stats
17	from scipy.special import betaln
18	
19	CONDITION_MAP = [
20	    ("d134_4b_isr", "ISR"),
21	    ("d134_4b_random", "RANDOM"),
22	    ("plan002_additive", "ISR"),
23	    ("plan018_additive_random", "RANDOM"),
24	    ("plan018_random", "RANDOM"),
25	]
26	
27	MODE_PREFIXES = {
28	    "d134_only": ["d134_4b"],
29	    "all": ["d134_4b", "plan002_additive_b01", "plan018_additive_random_b01", "plan018_random"],
30	}
31	
32	
33	def parse_args():
34	    p = argparse.ArgumentParser(description="D134 multi-seed analysis and statistical tests")
35	    p.add_argument("--data_dir", type=str, default="/root/autodl-tmp/outputs",
36	                   help="Directory containing experiment outputs")
37	    p.add_argument("--mode", type=str, default="d134_only", choices=list(MODE_PREFIXES),
38	                   help="d134_only = matched 5+5 design (default); all = include original seeds")
39	    p.add_argument("--prefix", type=str, default=None,
40	                   help="(Legacy) Single prefix filter; overrides mode/prefixes")
41	    p.add_argument("--prefixes", type=str, default=None,
42	                   help="Comma-separated prefixes; overrides --mode")
43	    p.add_argument("--output", type=str, default=None,
44	                   help="Write markdown summary to this file")
45	    p.add_argument("--n_perm", type=int, default=10000,
46	                   help="Number of permutations for permutation test")
47	    p.add_argument("--n_boot", type=int, default=10000,
48	                   help="Number of bootstrap resamples for BCa CI")
49	    p.add_argument("--seed", type=int, default=42,
50	                   help="Random seed for permutation/bootstrap")
51	    return p.parse_args()
52	
53	
54	# --- Data loading ---
55	
56	def match_condition(name: str) -> str | None:
57	    best_prefix = ""
58	    best_cond = None
59	    for prefix, cond in CONDITION_MAP:
60	        if name.startswith(prefix) and len(prefix) > len(best_prefix):
61	            best_prefix = prefix
62	            best_cond = cond
63	    return best_cond
64	
65	
66	def extract_seed(name: str) -> int | None:
67	    m = re.search(r'_s(\d+)', name)
68	    return int(m.group(1)) if m else None
69	
70	
71	def load_eval_results(path: Path) -> dict | None:
72	    if not path.exists():
73	        return None
74	    with open(path) as f:
75	        data = json.load(f)
76	    if "eval_results" in data:
77	        return data["eval_results"]
78	    return data
79	
80	
81	def load_taxonomy_unified(path: Path) -> dict | None:
82	    with open(path) as f:
83	        raw = json.load(f)
84	    t = raw.get("taxonomy", {})
85	    proved = t.get("proved", 0)
86	    if proved == 0:
87	        return None
88	    h7 = t.get("H7", 0)
89	    h1 = t.get("H1_exact", 0)
90	    h8 = t.get("H8", 0)
91	    genuine = t.get("genuine", 0)
92	    return {
93	        "n_total": 100, "n_proved": proved,
94	        "h7_total_count": h7, "h7_total_rate": h7 / proved,
95	        "h1_strict_count": h1, "h8_conjunction_collapse_count": h8,
96	        "genuine_count": genuine, "genuine_rate": genuine / proved,
97	        "content_independent_count": 0,
98	    }
99	
100	
101	def load_taxonomy_verification(path: Path) -> dict | None:
102	    with open(path) as f:
103	        raw = json.load(f)
104	    proved = raw.get("proved", 0)
105	    if proved == 0:
106	        return None
107	    tax = raw.get("taxonomy", {})
108	    h7 = tax.get("h7", {}).get("count", 0)
109	    h1 = tax.get("h1_exact", {}).get("count", 0)
110	    h8 = tax.get("h8", {}).get("count", 0)
111	    genuine = tax.get("genuine", {}).get("count", 0)
112	    return {
113	        "n_total": raw.get("total", 100), "n_proved": proved,
114	        "h7_total_count": h7, "h7_total_rate": h7 / proved,
115	        "h1_strict_count": h1, "h8_conjunction_collapse_count": h8,
116	        "genuine_count": genuine, "genuine_rate": genuine / proved,
117	        "content_independent_count": 0,
118	    }
119	
120	
121	def discover_runs(data_dir: Path, prefixes: list[str]) -> list[dict]:
122	    runs = []
123	    seen = set()
124	    for entry in sorted(data_dir.iterdir()):
125	        name = entry.name
126	        if not any(name.startswith(p) for p in prefixes):
127	            continue
128	        cond = match_condition(name)
129	        seed_val = extract_seed(name)
130	        if cond is None or seed_val is None:
131	            continue
132	        key = (cond, seed_val)
133	        if key in seen:
134	            continue
135	        data = None
136	        if entry.is_dir():
137	            for fname in ["classify.json", "taxonomy.json"]:
138	                data = load_eval_results(entry / fname)
139	                if data is not None:
140	                    break
141	            if data is None:
142	                continue
143	        elif entry.is_file():
144	            if name.endswith("_taxonomy_unified.json"):
145	                data = load_taxonomy_unified(entry)
146	            elif name.endswith("_taxonomy_verification.json"):
147	                data = load_taxonomy_verification(entry)
148	            if data is None:
149	                continue
150	        else:
151	            continue
152	        seen.add(key)
153	        runs.append({"dir_name": name, "seed": seed_val, "condition": cond, "data": data})
154	    return runs
155	
156	
157	def compute_row(run: dict) -> dict:
158	    d = run["data"]
159	    n_proved = d.get("n_proved", 0)
160	    n_total = d.get("n_total", 100)
161	    h7 = d.get("h7_total_count", 0)
162	    h7_rate = d.get("h7_total_rate", h7 / n_proved if n_proved > 0 else 0.0)
163	    h1 = d.get("h1_strict_count", 0)
164	    h8 = d.get("h8_conjunction_collapse_count", 0)
165	    genuine = d.get("genuine_count", 0)
166	    genuine_rate = d.get("genuine_rate", genuine / n_proved if n_proved > 0 else 0.0)
167	    ci = d.get("content_independent_count", 0)
168	    snh = max(genuine - ci, 0)
169	    snh_rate = snh / n_proved if n_proved > 0 else 0.0
170	    return {
171	        "seed": run["seed"], "condition": run["condition"], "n_total": n_total,
172	        "PR": n_proved, "H7_count": h7, "H7_rate": h7_rate,
173	        "H1_count": h1, "H8_count": h8,
174	        "genuine_count": genuine, "genuine_rate": genuine_rate,
175	        "CI_count": ci, "SNH_count": snh, "SNH_rate": snh_rate,
176	    }
177	
178	
179	def build_table(runs: list[dict]) -> pd.DataFrame:
180	    rows = [compute_row(r) for r in runs]
181	    df = pd.DataFrame(rows)
182	    df = df.sort_values(["condition", "seed"]).reset_index(drop=True)
183	    return df
184	
185	
186	# --- Statistical tests ---
187	
188	def fisher_h7_domination(df: pd.DataFrame) -> dict:
189	    results = {}
190	    for cond in ["ISR", "RANDOM"]:
191	        sub = df[df["condition"] == cond]
192	        results[cond] = {
193	            "n": len(sub),
194	            "h7_dom": int((sub["H7_rate"] >= 0.5).sum()),
195	            "not_h7_dom": int((sub["H7_rate"] < 0.5).sum()),
196	        }
197	    table = np.array([
198	        [results["ISR"]["h7_dom"], results["ISR"]["not_h7_dom"]],
199	        [results["RANDOM"]["h7_dom"], results["RANDOM"]["not_h7_dom"]],
200	    ])
201	    odds_ratio, p_value = stats.fisher_exact(table, alternative="greater")
202	
203	    # 95% exact CI via scipy.stats.contingency
204	    or_ci_lo, or_ci_hi = np.nan, np.nan
205	    try:
206	        ct = stats.contingency.odds_ratio(table)
207	        ci = ct.confidence_interval(confidence_level=0.95)
208	        or_ci_lo, or_ci_hi = ci.low, ci.high
209	    except Exception:
210	        pass
211	
212	    return {
213	        "table": table.tolist(),
214	        "ISR": results["ISR"],
215	        "RANDOM": results["RANDOM"],
216	        "odds_ratio": odds_ratio,
217	        "or_ci_lo": or_ci_lo,
218	        "or_ci_hi": or_ci_hi,
219	        "p_value": p_value,
220	    }
221	
222	
223	def permutation_test_genuine(df: pd.DataFrame, n_perm: int = 10000,
224	                              rng_seed: int = 42) -> dict:
225	    isr = df[df["condition"] == "ISR"]["genuine_rate"].values
226	    rand = df[df["condition"] == "RANDOM"]["genuine_rate"].values
227	    observed = isr.mean() - rand.mean()
228	    pooled = np.concatenate([isr, rand])
229	    n_isr = len(isr)
230	    rng = np.random.default_rng(rng_seed)
231	    count = 0
232	    for _ in range(n_perm):
233	        perm = rng.permutation(pooled)
234	        if perm[:n_isr].mean() - perm[n_isr:].mean() >= observed:
235	            count += 1
236	    return {
237	        "observed_diff": float(observed),
238	        "p_value": count / n_perm,
239	        "n_perm": n_perm,
240	        "isr_mean": float(isr.mean()),
241	        "random_mean": float(rand.mean()),
242	    }
243	
244	
245	def mannwhitney_h7(df: pd.DataFrame) -> dict:
246	    isr = df[df["condition"] == "ISR"]["H7_rate"].values
247	    rand = df[df["condition"] == "RANDOM"]["H7_rate"].values
248	    n1, n2 = len(isr), len(rand)
249	    u_stat, p_value = stats.mannwhitneyu(isr, rand, alternative="greater")
250	    r_rb = 2.0 * u_stat / (n1 * n2) - 1.0 if n1 * n2 > 0 else np.nan
251	    return {
252	        "U": float(u_stat),
253	        "p_value": float(p_value),
254	        "r_rank_biserial": float(r_rb),
255	        "isr_median": float(np.median(isr)),
256	        "random_median": float(np.median(rand)),
257	    }
258	
259	
260	def bca_bootstrap_ci(df: pd.DataFrame, metric: str, n_boot: int = 10000,
261	                      rng_seed: int = 42) -> dict:
262	    """BCa 95% CI for per-condition means of a metric."""
263	    result = {}
264	    for cond in ["ISR", "RANDOM"]:
265	        vals = df[df["condition"] == cond][metric].values
266	        if len(vals) < 2:
267	            result[cond] = {"mean": float(vals.mean()) if len(vals) else np.nan,
268	                            "ci_lo": np.nan, "ci_hi": np.nan}
269	            continue
270	        res = stats.bootstrap(
271	            (vals,), np.mean, n_resamples=n_boot,
272	            confidence_level=0.95, method="BCa",
273	            random_state=np.random.default_rng(rng_seed),
274	        )
275	        result[cond] = {
276	            "mean": float(vals.mean()),
277	            "ci_lo": float(res.confidence_interval.low),
278	            "ci_hi": float(res.confidence_interval.high),
279	        }
280	    return result
281	
282	
283	def bayes_factor_h7_domination(df: pd.DataFrame) -> dict:
284	    """BF10 for H7-domination rate difference (beta-binomial conjugate).
285	    H0: ISR and Random share same domination rate.
286	    H1: independent rates. Prior: Beta(1,1) on each.
287	    """
288	    isr_sub = df[df["condition"] == "ISR"]
289	    rand_sub = df[df["condition"] == "RANDOM"]
290	    k_isr = int((isr_sub["H7_rate"] >= 0.5).sum())
291	    n_isr = len(isr_sub)
292	    k_rand = int((rand_sub["H7_rate"] >= 0.5).sum())
293	    n_rand = len(rand_sub)
294	    k_total = k_isr + k_rand
295	    n_total = n_isr + n_rand
296	
297	    # log marginal under H0 (shared rate)
298	    log_m_h0 = betaln(1 + k_total, 1 + n_total - k_total) - betaln(1, 1)
299	    # log marginal under H1 (independent rates)
300	    log_m_h1 = (betaln(1 + k_isr, 1 + n_isr - k_isr) - betaln(1, 1)
301	                + betaln(1 + k_rand, 1 + n_rand - k_rand) - betaln(1, 1))
302	    log_bf10 = log_m_h1 - log_m_h0
303	    bf10 = float(np.exp(log_bf10))
304	
305	    return {
306	        "k_isr": k_isr, "n_isr": n_isr,
307	        "k_rand": k_rand, "n_rand": n_rand,
308	        "bf10": bf10,
309	        "log_bf10": float(log_bf10),
310	        "interpretation": _interpret_bf(bf10),
311	    }
312	
313	
314	def _interpret_bf(bf: float) -> str:
315	    if bf > 100:
316	        return "extreme evidence for H1"
317	    if bf > 30:
318	        return "very strong evidence for H1"
319	    if bf > 10:
320	        return "strong evidence for H1"
321	    if bf > 3:
322	        return "moderate evidence for H1"
323	    if bf > 1:
324	        return "anecdotal evidence for H1"
325	    if bf > 1/3:
326	        return "anecdotal evidence (inconclusive)"
327	    if bf > 1/10:
328	        return "moderate evidence for H0"
329	    return "strong evidence for H0"
330	
331	
332	def condition_stats(df: pd.DataFrame) -> pd.DataFrame:
333	    metrics = ["PR", "H7_rate", "genuine_rate", "SNH_rate"]
334	    rows = []
335	    for cond in ["ISR", "RANDOM"]:
336	        sub = df[df["condition"] == cond]
337	        row = {"condition": cond, "n_seeds": len(sub)}
338	        for m in metrics:
339	            vals = sub[m].values
340	            row[f"{m}_mean"] = vals.mean()
341	            row[f"{m}_std"] = vals.std(ddof=1) if len(vals) > 1 else 0.0
342	        rows.append(row)
343	    return pd.DataFrame(rows)
344	
345	
346	# --- Formatting ---
347	
348	def fmt_pct(val: float) -> str:
349	    return f"{val*100:.1f}\\%"
350	
351	def fmt_or(val: float) -> str:
352	    return "$\\infty$" if np.isinf(val) else f"{val:.2f}"
353	
354	def fmt_ci(lo: float, hi: float) -> str:
355	    lo_s = f"{lo:.2f}" if not np.isnan(lo) else "0"
356	    hi_s = "$\\infty$" if np.isinf(hi) or np.isnan(hi) else f"{hi:.2f}"
357	    return f"[{lo_s}, {hi_s}]"
358	
359	def fmt_p(p: float) -> str:
360	    if p < 0.001:
361	        return "$<$0.001"
362	    return f"{p:.3f}"
363	
364	def fmt_mean_std(mean: float, std: float, pct: bool = False) -> str:
365	    if pct:
366	        return f"{mean*100:.1f} $\\pm$ {std*100:.1f}\\%"
367	    return f"{mean:.1f} $\\pm$ {std:.1f}"
368	
369	def fmt_bca(bca: dict, pct: bool = False) -> str:
370	    m = bca["mean"]
371	    lo, hi = bca["ci_lo"], bca["ci_hi"]
372	    if pct:
373	        return f"{m*100:.1f}\\% [{lo*100:.1f}, {hi*100:.1f}]"
374	    return f"{m:.1f} [{lo:.1f}, {hi:.1f}]"
375	
376	
377	# --- Console output ---
378	
379	def print_per_seed_table(df: pd.DataFrame):
380	    print("\n" + "=" * 90)
381	    print("  PER-SEED RESULTS")
382	    print("=" * 90)
383	    cols = ["condition", "seed", "PR", "H7_count", "H7_rate", "H1_count",
384	            "H8_count", "genuine_count", "genuine_rate", "CI_count", "SNH_count", "SNH_rate"]
385	    fmt = df[cols].copy()
386	    for c in ["H7_rate", "genuine_rate", "SNH_rate"]:
387	        fmt[c] = fmt[c].apply(lambda v: f"{v*100:.1f}%")
388	    print(fmt.to_string(index=False))
389	
390	
391	def print_condition_stats(cond_df: pd.DataFrame):
392	    print("\n" + "=" * 90)
393	    print("  CONDITION-LEVEL STATISTICS (mean +/- SD)")
394	    print("=" * 90)
395	    for _, row in cond_df.iterrows():
396	        n = int(row['n_seeds'])
397	        print(f"\n  {row['condition']} (n={n} seeds):")
398	        print(f"    PR:           {row['PR_mean']:.1f} +/- {row['PR_std']:.1f}")
399	        print(f"    H7 rate:      {row['H7_rate_mean']*100:.1f} +/- {row['H7_rate_std']*100:.1f}%")
400	        print(f"    Genuine rate: {row['genuine_rate_mean']*100:.1f} +/- {row['genuine_rate_std']*100:.1f}%")
401	        print(f"    S-NH rate:    {row['SNH_rate_mean']*100:.1f} +/- {row['SNH_rate_std']*100:.1f}%")
402	
403	
404	def print_tests(fisher, perm, mw, bf, bca_h7, bca_gen):
405	    print("\n" + "=" * 90)
406	    print("  STATISTICAL TESTS")
407	    print("=" * 90)
408	
409	    print("\n  1. H7 Domination Fisher Exact Test (H7-dominated = H7% >= 50%)")
410	    print(f"     ISR:    {fisher['ISR']['h7_dom']} dominated / {fisher['ISR']['n']} seeds")
411	    print(f"     RANDOM: {fisher['RANDOM']['h7_dom']} dominated / {fisher['RANDOM']['n']} seeds")
412	    print(f"     Contingency: {fisher['table']}")
413	    or_str = "inf" if np.isinf(fisher['odds_ratio']) else f"{fisher['odds_ratio']:.4f}"
414	    print(f"     OR = {or_str}, 95% CI = [{fisher['or_ci_lo']:.4f}, {fisher['or_ci_hi']:.4f}]"
415	          if not np.isnan(fisher['or_ci_lo']) else f"     OR = {or_str}, 95% CI = N/A")
416	    print(f"     p-value (one-sided, greater): {fisher['p_value']:.4f}")
417	
418	    print(f"\n  2. Genuine Rate Permutation Test (n_perm={perm['n_perm']})")
419	    print(f"     ISR mean:    {perm['isr_mean']*100:.2f}%")
420	    print(f"     RANDOM mean: {perm['random_mean']*100:.2f}%")
421	    print(f"     Diff: {perm['observed_diff']*100:.2f} pp, p = {perm['p_value']:.4f}")
422	
423	    print(f"\n  3. H7 Rate Mann-Whitney U Test")
424	    print(f"     ISR median:    {mw['isr_median']*100:.1f}%")
425	    print(f"     RANDOM median: {mw['random_median']*100:.1f}%")
426	    print(f"     U = {mw['U']:.1f}, p = {mw['p_value']:.4f}")
427	    print(f"     Rank-biserial r = {mw['r_rank_biserial']:.4f}")
428	
429	    print(f"\n  4. Bayes Factor (H7 Domination, Beta-Binomial)")
430	    print(f"     ISR:    {bf['k_isr']}/{bf['n_isr']} dominated")
431	    print(f"     RANDOM: {bf['k_rand']}/{bf['n_rand']} dominated")
432	    print(f"     BF10 = {bf['bf10']:.4f} ({bf['interpretation']})")
433	
434	    print(f"\n  5. BCa Bootstrap 95% CI (n_boot resamples)")
435	    for label, bca in [("H7 rate", bca_h7), ("Genuine rate", bca_gen)]:
436	        print(f"     {label}:")
437	        for cond in ["ISR", "RANDOM"]:
438	            b = bca[cond]
439	            print(f"       {cond}: {b['mean']*100:.1f}% [{b['ci_lo']*100:.1f}, {b['ci_hi']*100:.1f}]"
440	                  if not np.isnan(b['ci_lo']) else f"       {cond}: {b['mean']*100:.1f}% [N/A]")
441	
442	
443	# --- Markdown generation (appendix-ready) ---
444	
445	def generate_markdown(df: pd.DataFrame, cond_df: pd.DataFrame,
446	                      fisher: dict, perm: dict, mw: dict,
447	                      bf: dict, bca_h7: dict, bca_gen: dict) -> str:
448	    L = []
449	    L.append("## D134: ISR vs Random Statistical Analysis\n")
450	
451	    # Per-seed table
452	    L.append("### Table A1: Per-Seed Hacking Taxonomy (4B Qwen3, 500 steps)\n")
453	    L.append("| Condition | Seed | PR | H7 | H7\\% | H1 | H8 | Genuine | Gen\\% | CI | S-NH | S-NH\\% |")
454	    L.append("|:----------|-----:|---:|---:|-----:|---:|---:|--------:|------:|---:|-----:|-------:|")
455	    for _, r in df.iterrows():
456	        L.append(
457	            f"| {r['condition']} | {r['seed']} | {int(r['PR'])} | {int(r['H7_count'])} | "
458	            f"{r['H7_rate']*100:.1f} | {int(r['H1_count'])} | {int(r['H8_count'])} | "
459	            f"{int(r['genuine_count'])} | {r['genuine_rate']*100:.1f} | {int(r['CI_count'])} | "
460	            f"{int(r['SNH_count'])} | {r['SNH_rate']*100:.1f} |"
461	        )
462	
463	    # Condition summary with BCa CI
464	    L.append("\n### Table A2: Condition-Level Summary\n")
465	    L.append("| Condition | $n$ | PR (mean$\\pm$SD) | H7\\% (mean$\\pm$SD) | H7\\% BCa 95\\% CI | Gen\\% (mean$\\pm$SD) | Gen\\% BCa 95\\% CI |")
466	    L.append("|:----------|----:|:------------------|:-------------------|:-----------------|:-------------------|:-----------------|")
467	    for _, r in cond_df.iterrows():
468	        cond = r["condition"]
469	        h7_bca = bca_h7.get(cond, {})
470	        gen_bca = bca_gen.get(cond, {})
471	        h7_ci = f"[{h7_bca['ci_lo']*100:.1f}, {h7_bca['ci_hi']*100:.1f}]" if h7_bca and not np.isnan(h7_bca.get('ci_lo', np.nan)) else "N/A"
472	        gen_ci = f"[{gen_bca['ci_lo']*100:.1f}, {gen_bca['ci_hi']*100:.1f}]" if gen_bca and not np.isnan(gen_bca.get('ci_lo', np.nan)) else "N/A"
473	        L.append(
474	            f"| {cond} | {int(r['n_seeds'])} | "
475	            f"{r['PR_mean']:.1f}$\\pm${r['PR_std']:.1f} | "
476	            f"{r['H7_rate_mean']*100:.1f}$\\pm${r['H7_rate_std']*100:.1f} | "
477	            f"{h7_ci} | "
478	            f"{r['genuine_rate_mean']*100:.1f}$\\pm${r['genuine_rate_std']*100:.1f} | "
479	            f"{gen_ci} |"
480	        )
481	
482	    # Statistical tests
483	    if fisher and perm and mw and bf:
484	        L.append("\n### Statistical Tests\n")
485	
486	        # Fisher
487	        or_str = "$\\infty$" if np.isinf(fisher['odds_ratio']) else f"{fisher['odds_ratio']:.2f}"
488	        ci_lo = f"{fisher['or_ci_lo']:.2f}" if not np.isnan(fisher['or_ci_lo']) else "0"
489	        ci_hi = "$\\infty$" if np.isinf(fisher.get('or_ci_hi', np.inf)) or np.isnan(fisher.get('or_ci_hi', np.nan)) else f"{fisher['or_ci_hi']:.2f}"
490	        L.append("**1. H7 Domination Fisher Exact Test** (threshold: H7$\\geq$50\\% of proved)")
491	        L.append(f"- ISR: {fisher['ISR']['h7_dom']}/{fisher['ISR']['n']} seeds H7-dominated; "
492	                 f"Random: {fisher['RANDOM']['h7_dom']}/{fisher['RANDOM']['n']}")
493	        L.append(f"- OR = {or_str}, 95\\% exact CI = [{ci_lo}, {ci_hi}], "
494	                 f"$p$ = {fmt_p(fisher['p_value'])}")
495	        L.append("")
496	
497	        # Permutation
498	        L.append(f"**2. Genuine Rate Permutation Test** ($n$ = {perm['n_perm']:,} permutations)")
499	        L.append(f"- ISR mean: {perm['isr_mean']*100:.2f}\\%, Random mean: {perm['random_mean']*100:.2f}\\%")
500	        L.append(f"- $\\Delta$ = {perm['observed_diff']*100:.2f} pp, $p$ = {fmt_p(perm['p_value'])}")
501	        L.append("")
502	
503	        # Mann-Whitney
504	        L.append("**3. H7 Rate Mann-Whitney $U$ Test**")
505	        L.append(f"- ISR median: {mw['isr_median']*100:.1f}\\%, Random median: {mw['random_median']*100:.1f}\\%")
506	        L.append(f"- $U$ = {mw['U']:.1f}, $p$ = {fmt_p(mw['p_value'])}, "
507	                 f"rank-biserial $r$ = {mw['r_rank_biserial']:.3f}")
508	        L.append("")
509	
510	        # Bayes Factor
511	        L.append("**4. Bayes Factor** (Beta-Binomial conjugate, prior: Beta(1,1))")
512	        L.append(f"- $BF_{{10}}$ = {bf['bf10']:.2f} ({bf['interpretation']})")
513	        L.append(f"- ISR: {bf['k_isr']}/{bf['n_isr']} H7-dominated, "
514	                 f"Random: {bf['k_rand']}/{bf['n_rand']}")
515	
516	    return "\n".join(L) + "\n"
517	
518	
519	# --- Main ---
520	
521	def main():
522	    args = parse_args()
523	    data_dir = Path(args.data_dir)
524	
525	    if not data_dir.exists():
526	        print(f"ERROR: data directory {data_dir} does not exist", file=sys.stderr)
527	        sys.exit(1)
528	
529	    if args.prefix:
530	        prefixes = [args.prefix]
531	    elif args.prefixes:
532	        prefixes = [p.strip() for p in args.prefixes.split(",")]
533	    else:
534	        prefixes = MODE_PREFIXES[args.mode]
535	    print(f"Mode: {args.mode} | Prefixes: {prefixes}")
536	
537	    runs = discover_runs(data_dir, prefixes)
538	    if not runs:
539	        print(f"ERROR: no runs found in {data_dir} with prefixes {prefixes}", file=sys.stderr)
540	        sys.exit(1)
541	
542	    isr_count = sum(1 for r in runs if r["condition"] == "ISR")
543	    rand_count = sum(1 for r in runs if r["condition"] == "RANDOM")
544	    print(f"Found {len(runs)} runs: {isr_count} ISR, {rand_count} RANDOM")
545	    for r in runs:
546	        print(f"  {r['condition']:6s} s{r['seed']} <- {r['dir_name']}")
547	
548	    df = build_table(runs)
549	    print_per_seed_table(df)
550	
551	    cond_df = condition_stats(df)
552	    print_condition_stats(cond_df)
553	
554	    if isr_count < 2 or rand_count < 2:
555	        print("\nWARNING: need >= 2 seeds per condition for statistical tests, skipping.",
556	              file=sys.stderr)
557	        bca_h7 = bca_bootstrap_ci(df, "H7_rate", args.n_boot, args.seed)
558	        bca_gen = bca_bootstrap_ci(df, "genuine_rate", args.n_boot, args.seed)
559	        if args.output:
560	            md = generate_markdown(df, cond_df, {}, {}, {}, {}, bca_h7, bca_gen)
561	            Path(args.output).write_text(md)
562	            print(f"\nMarkdown written to {args.output}")
563	        return
564	
565	    fisher = fisher_h7_domination(df)
566	    perm = permutation_test_genuine(df, n_perm=args.n_perm, rng_seed=args.seed)
567	    mw = mannwhitney_h7(df)
568	    bf = bayes_factor_h7_domination(df)
569	    bca_h7 = bca_bootstrap_ci(df, "H7_rate", args.n_boot, args.seed)
570	    bca_gen = bca_bootstrap_ci(df, "genuine_rate", args.n_boot, args.seed)
571	
572	    print_tests(fisher, perm, mw, bf, bca_h7, bca_gen)
573	
574	    md = generate_markdown(df, cond_df, fisher, perm, mw, bf, bca_h7, bca_gen)
575	    print("\n" + "=" * 90)
576	    print("  MARKDOWN OUTPUT (appendix-ready)")
577	    print("=" * 90)
578	    print(md)
579	
580	    if args.output:
581	        Path(args.output).parent.mkdir(parents=True, exist_ok=True)
582	        Path(args.output).write_text(md)
583	        print(f"Markdown written to {args.output}")
584	
585	
586	if __name__ == "__main__":
587	    main()
588	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "8b9c4877-e255-47f2-843a-8cdad9e62278",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/scripts/d134_analysis.py",
      "content": "#!/usr/bin/env python3\n\"\"\"D134 experiment analysis: multi-seed ISR vs Random, 4B GRPO training.\nReads taxonomy data from classify.json, taxonomy.json, or top-level taxonomy files.\nComputes summary stats, statistical tests (Fisher, Mann-Whitney, permutation, Bayes Factor),\nand BCa bootstrap CIs. Outputs appendix-ready markdown.\n\"\"\"\n\nimport argparse\nimport json\nimport re\nimport sys\nfrom pathlib import Path\n\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\nfrom scipy.special import betaln\n\nCONDITION_MAP = [\n    (\"d134_4b_isr\", \"ISR\"),\n    (\"d134_4b_random\", \"RANDOM\"),\n    (\"plan002_additive\", \"ISR\"),\n    (\"plan018_additive_random\", \"RANDOM\"),\n    (\"plan018_random\", \"RANDOM\"),\n]\n\nMODE_PREFIXES = {\n    \"d134_only\": [\"d134_4b\"],\n    \"all\": [\"d134_4b\", \"plan002_additive_b01\", \"plan018_additive_random_b01\", \"plan018_random\"],\n}\n\n\ndef parse_args():\n    p = argparse.ArgumentParser(description=\"D134 multi-seed analysis and statistical tests\")\n    p.add_argument(\"--data_dir\", type=str, default=\"/root/autodl-tmp/outputs\",\n                   help=\"Directory containing experiment outputs\")\n    p.add_argument(\"--mode\", type=str, default=\"d134_only\", choices=list(MODE_PREFIXES),\n                   help=\"d134_only = matched 5+5 design (default); all = include original seeds\")\n    p.add_argument(\"--prefix\", type=str, default=None,\n                   help=\"(Legacy) Single prefix filter; overrides mode/prefixes\")\n    p.add_argument(\"--prefixes\", type=str, default=None,\n                   help=\"Comma-separated prefixes; overrides --mode\")\n    p.add_argument(\"--output\", type=str, default=None,\n                   help=\"Write markdown summary to this file\")\n    p.add_argument(\"--n_perm\", type=int, default=10000,\n                   help=\"Number of permutations for permutation test\")\n    p.add_argument(\"--n_boot\", type=int, default=10000,\n                   help=\"Number of bootstrap resamples for BCa CI\")\n    p.add_argument(\"--seed\", type=int, default=42,\n                   help=\"Random seed for permutation/bootstrap\")\n    return p.parse_args()\n\n\n# --- Data loading ---\n\ndef match_condition(name: str) -> str | None:\n    best_prefix = \"\"\n    best_cond = None\n    for prefix, cond in CONDITION_MAP:\n        if name.startswith(prefix) and len(prefix) > len(best_prefix):\n            best_prefix = prefix\n            best_cond = cond\n    return best_cond\n\n\ndef extract_seed(name: str) -> int | None:\n    m = re.search(r'_s(\\d+)', name)\n    return int(m.group(1)) if m else None\n\n\ndef load_eval_results(path: Path) -> dict | None:\n    if not path.exists():\n        return None\n    with open(path) as f:\n        data = json.load(f)\n    if \"eval_results\" in data:\n        return data[\"eval_results\"]\n    return data\n\n\ndef load_taxonomy_unified(path: Path) -> dict | None:\n    with open(path) as f:\n        raw = json.load(f)\n    t = raw.get(\"taxonomy\", {})\n    proved = t.get(\"proved\", 0)\n    if proved == 0:\n        return None\n    h7 = t.get(\"H7\", 0)\n    h1 = t.get(\"H1_exact\", 0)\n    h8 = t.get(\"H8\", 0)\n    genuine = t.get(\"genuine\", 0)\n    return {\n        \"n_total\": 100, \"n_proved\": proved,\n        \"h7_total_count\": h7, \"h7_total_rate\": h7 / proved,\n        \"h1_strict_count\": h1, \"h8_conjunction_collapse_count\": h8,\n        \"genuine_count\": genuine, \"genuine_rate\": genuine / proved,\n        \"content_independent_count\": 0,\n    }\n\n\ndef load_taxonomy_verification(path: Path) -> dict | None:\n    with open(path) as f:\n        raw = json.load(f)\n    proved = raw.get(\"proved\", 0)\n    if proved == 0:\n        return None\n    tax = raw.get(\"taxonomy\", {})\n    h7 = tax.get(\"h7\", {}).get(\"count\", 0)\n    h1 = tax.get(\"h1_exact\", {}).get(\"count\", 0)\n    h8 = tax.get(\"h8\", {}).get(\"count\", 0)\n    genuine = tax.get(\"genuine\", {}).get(\"count\", 0)\n    return {\n        \"n_total\": raw.get(\"total\", 100), \"n_proved\": proved,\n        \"h7_total_count\": h7, \"h7_total_rate\": h7 / proved,\n        \"h1_strict_count\": h1, \"h8_conjunction_collapse_count\": h8,\n        \"genuine_count\": genuine, \"genuine_rate\": genuine / proved,\n        \"content_independent_count\": 0,\n    }\n\n\ndef discover_runs(data_dir: Path, prefixes: list[str]) -> list[dict]:\n    runs = []\n    seen = set()\n    for entry in sorted(data_dir.iterdir()):\n        name = entry.name\n        if not any(name.startswith(p) for p in prefixes):\n            continue\n        cond = match_condition(name)\n        seed_val = extract_seed(name)\n        if cond is None or seed_val is None:\n            continue\n        key = (cond, seed_val)\n        if key in seen:\n            continue\n        data = None\n        if entry.is_dir():\n            for fname in [\"classify.json\", \"taxonomy.json\"]:\n                data = load_eval_results(entry / fname)\n                if data is not None:\n                    break\n            if data is None:\n                continue\n        elif entry.is_file():\n            if name.endswith(\"_taxonomy_unified.json\"):\n                data = load_taxonomy_unified(entry)\n            elif name.endswith(\"_taxonomy_verification.json\"):\n                data = load_taxonomy_verification(entry)\n            if data is None:\n                continue\n        else:\n            continue\n        seen.add(key)\n        runs.append({\"dir_name\": name, \"seed\": seed_val, \"condition\": cond, \"data\": data})\n    return runs\n\n\ndef compute_row(run: dict) -> dict:\n    d = run[\"data\"]\n    n_proved = d.get(\"n_proved\", 0)\n    n_total = d.get(\"n_total\", 100)\n    h7 = d.get(\"h7_total_count\", 0)\n    h7_rate = d.get(\"h7_total_rate\", h7 / n_proved if n_proved > 0 else 0.0)\n    h1 = d.get(\"h1_strict_count\", 0)\n    h8 = d.get(\"h8_conjunction_collapse_count\", 0)\n    genuine = d.get(\"genuine_count\", 0)\n    genuine_rate = d.get(\"genuine_rate\", genuine / n_proved if n_proved > 0 else 0.0)\n    ci = d.get(\"content_independent_count\", 0)\n    snh = max(genuine - ci, 0)\n    snh_rate = snh / n_proved if n_proved > 0 else 0.0\n    return {\n        \"seed\": run[\"seed\"], \"condition\": run[\"condition\"], \"n_total\": n_total,\n        \"PR\": n_proved, \"H7_count\": h7, \"H7_rate\": h7_rate,\n        \"H1_count\": h1, \"H8_count\": h8,\n        \"genuine_count\": genuine, \"genuine_rate\": genuine_rate,\n        \"CI_count\": ci, \"SNH_count\": snh, \"SNH_rate\": snh_rate,\n    }\n\n\ndef build_table(runs: list[dict]) -> pd.DataFrame:\n    rows = [compute_row(r) for r in runs]\n    df = pd.DataFrame(rows)\n    df = df.sort_values([\"condition\", \"seed\"]).reset_index(drop=True)\n    return df\n\n\n# --- Statistical tests ---\n\ndef fisher_h7_domination(df: pd.DataFrame) -> dict:\n    results = {}\n    for cond in [\"ISR\", \"RANDOM\"]:\n        sub = df[df[\"condition\"] == cond]\n        results[cond] = {\n            \"n\": len(sub),\n            \"h7_dom\": int((sub[\"H7_rate\"] >= 0.5).sum()),\n            \"not_h7_dom\": int((sub[\"H7_rate\"] < 0.5).sum()),\n        }\n    table = np.array([\n        [results[\"ISR\"][\"h7_dom\"], results[\"ISR\"][\"not_h7_dom\"]],\n        [results[\"RANDOM\"][\"h7_dom\"], results[\"RANDOM\"][\"not_h7_dom\"]],\n    ])\n    odds_ratio, p_value = stats.fisher_exact(table, alternative=\"greater\")\n\n    # 95% exact CI via scipy.stats.contingency\n    or_ci_lo, or_ci_hi = np.nan, np.nan\n    try:\n        ct = stats.contingency.odds_ratio(table)\n        ci = ct.confidence_interval(confidence_level=0.95)\n        or_ci_lo, or_ci_hi = ci.low, ci.high\n    except Exception:\n        pass\n\n    return {\n        \"table\": table.tolist(),\n        \"ISR\": results[\"ISR\"],\n        \"RANDOM\": results[\"RANDOM\"],\n        \"odds_ratio\": odds_ratio,\n        \"or_ci_lo\": or_ci_lo,\n        \"or_ci_hi\": or_ci_hi,\n        \"p_value\": p_value,\n    }\n\n\ndef permutation_test_genuine(df: pd.DataFrame, n_perm: int = 10000,\n                              rng_seed: int = 42) -> dict:\n    isr = df[df[\"condition\"] == \"ISR\"][\"genuine_rate\"].values\n    rand = df[df[\"condition\"] == \"RANDOM\"][\"genuine_rate\"].values\n    observed = isr.mean() - rand.mean()\n    pooled = np.concatenate([isr, rand])\n    n_isr = len(isr)\n    rng = np.random.default_rng(rng_seed)\n    count = 0\n    for _ in range(n_perm):\n        perm = rng.permutation(pooled)\n        if perm[:n_isr].mean() - perm[n_isr:].mean() >= observed:\n            count += 1\n    return {\n        \"observed_diff\": float(observed),\n        \"p_value\": count / n_perm,\n        \"n_perm\": n_perm,\n        \"isr_mean\": float(isr.mean()),\n        \"random_mean\": float(rand.mean()),\n    }\n\n\ndef mannwhitney_h7(df: pd.DataFrame) -> dict:\n    isr = df[df[\"condition\"] == \"ISR\"][\"H7_rate\"].values\n    rand = df[df[\"condition\"] == \"RANDOM\"][\"H7_rate\"].values\n    n1, n2 = len(isr), len(rand)\n    u_stat, p_value = stats.mannwhitneyu(isr, rand, alternative=\"greater\")\n    r_rb = 2.0 * u_stat / (n1 * n2) - 1.0 if n1 * n2 > 0 else np.nan\n    return {\n        \"U\": float(u_stat),\n        \"p_value\": float(p_value),\n        \"r_rank_biserial\": float(r_rb),\n        \"isr_median\": float(np.median(isr)),\n        \"random_median\": float(np.median(rand)),\n    }\n\n\ndef bca_bootstrap_ci(df: pd.DataFrame, metric: str, n_boot: int = 10000,\n                      rng_seed: int = 42) -> dict:\n    \"\"\"BCa 95% CI for per-condition means of a metric.\"\"\"\n    result = {}\n    for cond in [\"ISR\", \"RANDOM\"]:\n        vals = df[df[\"condition\"] == cond][metric].values\n        if len(vals) < 2:\n            result[cond] = {\"mean\": float(vals.mean()) if len(vals) else np.nan,\n                            \"ci_lo\": np.nan, \"ci_hi\": np.nan}\n            continue\n        res = stats.bootstrap(\n            (vals,), np.mean, n_resamples=n_boot,\n            confidence_level=0.95, method=\"BCa\",\n            random_state=np.random.default_rng(rng_seed),\n        )\n        result[cond] = {\n            \"mean\": float(vals.mean()),\n            \"ci_lo\": float(res.confidence_interval.low),\n            \"ci_hi\": float(res.confidence_interval.high),\n        }\n    return result\n\n\ndef bayes_factor_h7_domination(df: pd.DataFrame) -> dict:\n    \"\"\"BF10 for H7-domination rate difference (beta-binomial conjugate).\n    H0: ISR and Random share same domination rate.\n    H1: independent rates. Prior: Beta(1,1) on each.\n    \"\"\"\n    isr_sub = df[df[\"condition\"] == \"ISR\"]\n    rand_sub = df[df[\"condition\"] == \"RANDOM\"]\n    k_isr = int((isr_sub[\"H7_rate\"] >= 0.5).sum())\n    n_isr = len(isr_sub)\n    k_rand = int((rand_sub[\"H7_rate\"] >= 0.5).sum())\n    n_rand = len(rand_sub)\n    k_total = k_isr + k_rand\n    n_total = n_isr + n_rand\n\n    # log marginal under H0 (shared rate)\n    log_m_h0 = betaln(1 + k_total, 1 + n_total - k_total) - betaln(1, 1)\n    # log marginal under H1 (independent rates)\n    log_m_h1 = (betaln(1 + k_isr, 1 + n_isr - k_isr) - betaln(1, 1)\n                + betaln(1 + k_rand, 1 + n_rand - k_rand) - betaln(1, 1))\n    log_bf10 = log_m_h1 - log_m_h0\n    bf10 = float(np.exp(log_bf10))\n\n    return {\n        \"k_isr\": k_isr, \"n_isr\": n_isr,\n        \"k_rand\": k_rand, \"n_rand\": n_rand,\n        \"bf10\": bf10,\n        \"log_bf10\": float(log_bf10),\n        \"interpretation\": _interpret_bf(bf10),\n    }\n\n\ndef _interpret_bf(bf: float) -> str:\n    if bf > 100:\n        return \"extreme evidence for H1\"\n    if bf > 30:\n        return \"very strong evidence for H1\"\n    if bf > 10:\n        return \"strong evidence for H1\"\n    if bf > 3:\n        return \"moderate evidence for H1\"\n    if bf > 1:\n        return \"anecdotal evidence for H1\"\n    if bf > 1/3:\n        return \"anecdotal evidence (inconclusive)\"\n    if bf > 1/10:\n        return \"moderate evidence for H0\"\n    return \"strong evidence for H0\"\n\n\ndef condition_stats(df: pd.DataFrame) -> pd.DataFrame:\n    metrics = [\"PR\", \"H7_rate\", \"genuine_rate\", \"SNH_rate\"]\n    rows = []\n    for cond in [\"ISR\", \"RANDOM\"]:\n        sub = df[df[\"condition\"] == cond]\n        row = {\"condition\": cond, \"n_seeds\": len(sub)}\n        for m in metrics:\n            vals = sub[m].values\n            row[f\"{m}_mean\"] = vals.mean()\n            row[f\"{m}_std\"] = vals.std(ddof=1) if len(vals) > 1 else 0.0\n        rows.append(row)\n    return pd.DataFrame(rows)\n\n\n# --- Formatting ---\n\ndef fmt_pct(val: float) -> str:\n    return f\"{val*100:.1f}\\\\%\"\n\ndef fmt_or(val: float) -> str:\n    return \"$\\\\infty$\" if np.isinf(val) else f\"{val:.2f}\"\n\ndef fmt_ci(lo: float, hi: float) -> str:\n    lo_s = f\"{lo:.2f}\" if not np.isnan(lo) else \"0\"\n    hi_s = \"$\\\\infty$\" if np.isinf(hi) or np.isnan(hi) else f\"{hi:.2f}\"\n    return f\"[{lo_s}, {hi_s}]\"\n\ndef fmt_p(p: float) -> str:\n    if p < 0.001:\n        return \"$<$0.001\"\n    return f\"{p:.3f}\"\n\ndef fmt_mean_std(mean: float, std: float, pct: bool = False) -> str:\n    if pct:\n        return f\"{mean*100:.1f} $\\\\pm$ {std*100:.1f}\\\\%\"\n    return f\"{mean:.1f} $\\\\pm$ {std:.1f}\"\n\ndef fmt_bca(bca: dict, pct: bool = False) -> str:\n    m = bca[\"mean\"]\n    lo, hi = bca[\"ci_lo\"], bca[\"ci_hi\"]\n    if pct:\n        return f\"{m*100:.1f}\\\\% [{lo*100:.1f}, {hi*100:.1f}]\"\n    return f\"{m:.1f} [{lo:.1f}, {hi:.1f}]\"\n\n\n# --- Console output ---\n\ndef print_per_seed_table(df: pd.DataFrame):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  PER-SEED RESULTS\")\n    print(\"=\" * 90)\n    cols = [\"condition\", \"seed\", \"PR\", \"H7_count\", \"H7_rate\", \"H1_count\",\n            \"H8_count\", \"genuine_count\", \"genuine_rate\", \"CI_count\", \"SNH_count\", \"SNH_rate\"]\n    fmt = df[cols].copy()\n    for c in [\"H7_rate\", \"genuine_rate\", \"SNH_rate\"]:\n        fmt[c] = fmt[c].apply(lambda v: f\"{v*100:.1f}%\")\n    print(fmt.to_string(index=False))\n\n\ndef print_condition_stats(cond_df: pd.DataFrame):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  CONDITION-LEVEL STATISTICS (mean +/- SD)\")\n    print(\"=\" * 90)\n    for _, row in cond_df.iterrows():\n        n = int(row['n_seeds'])\n        print(f\"\\n  {row['condition']} (n={n} seeds):\")\n        print(f\"    PR:           {row['PR_mean']:.1f} +/- {row['PR_std']:.1f}\")\n        print(f\"    H7 rate:      {row['H7_rate_mean']*100:.1f} +/- {row['H7_rate_std']*100:.1f}%\")\n        print(f\"    Genuine rate: {row['genuine_rate_mean']*100:.1f} +/- {row['genuine_rate_std']*100:.1f}%\")\n        print(f\"    S-NH rate:    {row['SNH_rate_mean']*100:.1f} +/- {row['SNH_rate_std']*100:.1f}%\")\n\n\ndef print_tests(fisher, perm, mw, bf, bca_h7, bca_gen):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  STATISTICAL TESTS\")\n    print(\"=\" * 90)\n\n    print(\"\\n  1. H7 Domination Fisher Exact Test (H7-dominated = H7% >= 50%)\")\n    print(f\"     ISR:    {fisher['ISR']['h7_dom']} dominated / {fisher['ISR']['n']} seeds\")\n    print(f\"     RANDOM: {fisher['RANDOM']['h7_dom']} dominated / {fisher['RANDOM']['n']} seeds\")\n    print(f\"     Contingency: {fisher['table']}\")\n    or_str = \"inf\" if np.isinf(fisher['odds_ratio']) else f\"{fisher['odds_ratio']:.4f}\"\n    print(f\"     OR = {or_str}, 95% CI = [{fisher['or_ci_lo']:.4f}, {fisher['or_ci_hi']:.4f}]\"\n          if not np.isnan(fisher['or_ci_lo']) else f\"     OR = {or_str}, 95% CI = N/A\")\n    print(f\"     p-value (one-sided, greater): {fisher['p_value']:.4f}\")\n\n    print(f\"\\n  2. Genuine Rate Permutation Test (n_perm={perm['n_perm']})\")\n    print(f\"     ISR mean:    {perm['isr_mean']*100:.2f}%\")\n    print(f\"     RANDOM mean: {perm['random_mean']*100:.2f}%\")\n    print(f\"     Diff: {perm['observed_diff']*100:.2f} pp, p = {perm['p_value']:.4f}\")\n\n    print(f\"\\n  3. H7 Rate Mann-Whitney U Test\")\n    print(f\"     ISR median:    {mw['isr_median']*100:.1f}%\")\n    print(f\"     RANDOM median: {mw['random_median']*100:.1f}%\")\n    print(f\"     U = {mw['U']:.1f}, p = {mw['p_value']:.4f}\")\n    print(f\"     Rank-biserial r = {mw['r_rank_biserial']:.4f}\")\n\n    print(f\"\\n  4. Bayes Factor (H7 Domination, Beta-Binomial)\")\n    print(f\"     ISR:    {bf['k_isr']}/{bf['n_isr']} dominated\")\n    print(f\"     RANDOM: {bf['k_rand']}/{bf['n_rand']} dominated\")\n    print(f\"     BF10 = {bf['bf10']:.4f} ({bf['interpretation']})\")\n\n    print(f\"\\n  5. BCa Bootstrap 95% CI (n_boot resamples)\")\n    for label, bca in [(\"H7 rate\", bca_h7), (\"Genuine rate\", bca_gen)]:\n        print(f\"     {label}:\")\n        for cond in [\"ISR\", \"RANDOM\"]:\n            b = bca[cond]\n            print(f\"       {cond}: {b['mean']*100:.1f}% [{b['ci_lo']*100:.1f}, {b['ci_hi']*100:.1f}]\"\n                  if not np.isnan(b['ci_lo']) else f\"       {cond}: {b['mean']*100:.1f}% [N/A]\")\n\n\n# --- Markdown generation (appendix-ready) ---\n\ndef generate_markdown(df: pd.DataFrame, cond_df: pd.DataFrame,\n                      fisher: dict, perm: dict, mw: dict,\n                      bf: dict, bca_h7: dict, bca_gen: dict) -> str:\n    L = []\n    L.append(\"## D134: ISR vs Random Statistical Analysis\\n\")\n\n    # Per-seed table\n    L.append(\"### Table A1: Per-Seed Hacking Taxonomy (4B Qwen3, 500 steps)\\n\")\n    L.append(\"| Condition | Seed | PR | H7 | H7\\\\% | H1 | H8 | Genuine | Gen\\\\% | CI | S-NH | S-NH\\\\% |\")\n    L.append(\"|:----------|-----:|---:|---:|-----:|---:|---:|--------:|------:|---:|-----:|-------:|\")\n    for _, r in df.iterrows():\n        L.append(\n            f\"| {r['condition']} | {r['seed']} | {int(r['PR'])} | {int(r['H7_count'])} | \"\n            f\"{r['H7_rate']*100:.1f} | {int(r['H1_count'])} | {int(r['H8_count'])} | \"\n            f\"{int(r['genuine_count'])} | {r['genuine_rate']*100:.1f} | {int(r['CI_count'])} | \"\n            f\"{int(r['SNH_count'])} | {r['SNH_rate']*100:.1f} |\"\n        )\n\n    # Condition summary with BCa CI\n    L.append(\"\\n### Table A2: Condition-Level Summary\\n\")\n    L.append(\"| Condition | $n$ | PR (mean$\\\\pm$SD) | H7\\\\% (mean$\\\\pm$SD) | H7\\\\% BCa 95\\\\% CI | Gen\\\\% (mean$\\\\pm$SD) | Gen\\\\% BCa 95\\\\% CI |\")\n    L.append(\"|:----------|----:|:------------------|:-------------------|:-----------------|:-------------------|:-----------------|\")\n    for _, r in cond_df.iterrows():\n        cond = r[\"condition\"]\n        h7_bca = bca_h7.get(cond, {})\n        gen_bca = bca_gen.get(cond, {})\n        h7_ci = f\"[{h7_bca['ci_lo']*100:.1f}, {h7_bca['ci_hi']*100:.1f}]\" if h7_bca and not np.isnan(h7_bca.get('ci_lo', np.nan)) else \"N/A\"\n        gen_ci = f\"[{gen_bca['ci_lo']*100:.1f}, {gen_bca['ci_hi']*100:.1f}]\" if gen_bca and not np.isnan(gen_bca.get('ci_lo', np.nan)) else \"N/A\"\n        L.append(\n            f\"| {cond} | {int(r['n_seeds'])} | \"\n            f\"{r['PR_mean']:.1f}$\\\\pm${r['PR_std']:.1f} | \"\n            f\"{r['H7_rate_mean']*100:.1f}$\\\\pm${r['H7_rate_std']*100:.1f} | \"\n            f\"{h7_ci} | \"\n            f\"{r['genuine_rate_mean']*100:.1f}$\\\\pm${r['genuine_rate_std']*100:.1f} | \"\n            f\"{gen_ci} |\"\n        )\n\n    # Statistical tests\n    if fisher and perm and mw and bf:\n        L.append(\"\\n### Statistical Tests\\n\")\n\n        # Fisher\n        or_str = \"$\\\\infty$\" if np.isinf(fisher['odds_ratio']) else f\"{fisher['odds_ratio']:.2f}\"\n        ci_lo = f\"{fisher['or_ci_lo']:.2f}\" if not np.isnan(fisher['or_ci_lo']) else \"0\"\n        ci_hi = \"$\\\\infty$\" if np.isinf(fisher.get('or_ci_hi', np.inf)) or np.isnan(fisher.get('or_ci_hi', np.nan)) else f\"{fisher['or_ci_hi']:.2f}\"\n        L.append(\"**1. H7 Domination Fisher Exact Test** (threshold: H7$\\\\geq$50\\\\% of proved)\")\n        L.append(f\"- ISR: {fisher['ISR']['h7_dom']}/{fisher['ISR']['n']} seeds H7-dominated; \"\n                 f\"Random: {fisher['RANDOM']['h7_dom']}/{fisher['RANDOM']['n']}\")\n        L.append(f\"- OR = {or_str}, 95\\\\% exact CI = [{ci_lo}, {ci_hi}], \"\n                 f\"$p$ = {fmt_p(fisher['p_value'])}\")\n        L.append(\"\")\n\n        # Permutation\n        L.append(f\"**2. Genuine Rate Permutation Test** ($n$ = {perm['n_perm']:,} permutations)\")\n        L.append(f\"- ISR mean: {perm['isr_mean']*100:.2f}\\\\%, Random mean: {perm['random_mean']*100:.2f}\\\\%\")\n        L.append(f\"- $\\\\Delta$ = {perm['observed_diff']*100:.2f} pp, $p$ = {fmt_p(perm['p_value'])}\")\n        L.append(\"\")\n\n        # Mann-Whitney\n        L.append(\"**3. H7 Rate Mann-Whitney $U$ Test**\")\n        L.append(f\"- ISR median: {mw['isr_median']*100:.1f}\\\\%, Random median: {mw['random_median']*100:.1f}\\\\%\")\n        L.append(f\"- $U$ = {mw['U']:.1f}, $p$ = {fmt_p(mw['p_value'])}, \"\n                 f\"rank-biserial $r$ = {mw['r_rank_biserial']:.3f}\")\n        L.append(\"\")\n\n        # Bayes Factor\n        L.append(\"**4. Bayes Factor** (Beta-Binomial conjugate, prior: Beta(1,1))\")\n        L.append(f\"- $BF_{{10}}$ = {bf['bf10']:.2f} ({bf['interpretation']})\")\n        L.append(f\"- ISR: {bf['k_isr']}/{bf['n_isr']} H7-dominated, \"\n                 f\"Random: {bf['k_rand']}/{bf['n_rand']}\")\n\n    return \"\\n\".join(L) + \"\\n\"\n\n\n# --- Main ---\n\ndef main():\n    args = parse_args()\n    data_dir = Path(args.data_dir)\n\n    if not data_dir.exists():\n        print(f\"ERROR: data directory {data_dir} does not exist\", file=sys.stderr)\n        sys.exit(1)\n\n    if args.prefix:\n        prefixes = [args.prefix]\n    elif args.prefixes:\n        prefixes = [p.strip() for p in args.prefixes.split(\",\")]\n    else:\n        prefixes = MODE_PREFIXES[args.mode]\n    print(f\"Mode: {args.mode} | Prefixes: {prefixes}\")\n\n    runs = discover_runs(data_dir, prefixes)\n    if not runs:\n        print(f\"ERROR: no runs found in {data_dir} with prefixes {prefixes}\", file=sys.stderr)\n        sys.exit(1)\n\n    isr_count = sum(1 for r in runs if r[\"condition\"] == \"ISR\")\n    rand_count = sum(1 for r in runs if r[\"condition\"] == \"RANDOM\")\n    print(f\"Found {len(runs)} runs: {isr_count} ISR, {rand_count} RANDOM\")\n    for r in runs:\n        print(f\"  {r['condition']:6s} s{r['seed']} <- {r['dir_name']}\")\n\n    df = build_table(runs)\n    print_per_seed_table(df)\n\n    cond_df = condition_stats(df)\n    print_condition_stats(cond_df)\n\n    if isr_count < 2 or rand_count < 2:\n        print(\"\\nWARNING: need >= 2 seeds per condition for statistical tests, skipping.\",\n              file=sys.stderr)\n        bca_h7 = bca_bootstrap_ci(df, \"H7_rate\", args.n_boot, args.seed)\n        bca_gen = bca_bootstrap_ci(df, \"genuine_rate\", args.n_boot, args.seed)\n        if args.output:\n            md = generate_markdown(df, cond_df, {}, {}, {}, {}, bca_h7, bca_gen)\n            Path(args.output).write_text(md)\n            print(f\"\\nMarkdown written to {args.output}\")\n        return\n\n    fisher = fisher_h7_domination(df)\n    perm = permutation_test_genuine(df, n_perm=args.n_perm, rng_seed=args.seed)\n    mw = mannwhitney_h7(df)\n    bf = bayes_factor_h7_domination(df)\n    bca_h7 = bca_bootstrap_ci(df, \"H7_rate\", args.n_boot, args.seed)\n    bca_gen = bca_bootstrap_ci(df, \"genuine_rate\", args.n_boot, args.seed)\n\n    print_tests(fisher, perm, mw, bf, bca_h7, bca_gen)\n\n    md = generate_markdown(df, cond_df, fisher, perm, mw, bf, bca_h7, bca_gen)\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  MARKDOWN OUTPUT (appendix-ready)\")\n    print(\"=\" * 90)\n    print(md)\n\n    if args.output:\n        Path(args.output).parent.mkdir(parents=True, exist_ok=True)\n        Path(args.output).write_text(md)\n        print(f\"Markdown written to {args.output}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 588,
      "startLine": 1,
      "totalLines": 588
    }
  }
}
```

</details>

---

### Assistant

_source line 17_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full picture. I need to:

1. Add ISR* (`proved_only_mean_isr`) extraction from `eval_results.json` 
2. Add it to per-seed table
3. Add Mann-Whitney test for ISR*
4. Update markdown generation

Let me plan the changes:

1. In `discover_runs()`, also load `eval_results.json` and extract `summary.proved_only_mean_isr`
2. In `compute_row()`, add `ISR_star` field
3. In `print_per_seed_table()`, add ISR* column


4. Add `mannwhitney_isr_star()` function
5. In `condition_stats()`, add ISR_star to metrics
6. In `print_condition_stats()`, add ISR* output
7. In `print_tests()`, add ISR* MW output
8. In `generate_markdown()`, add ISR* column to Table A1 and ISR* MW test
9. In `main()`, call the new test and pass to output functions

Now I need to modify `discover_runs()` to load the eval results file alongside the existing taxonomy data and extract the ISR* metric.

Modifying the run dict structure...

I need to load `eval_results.json` in the `discover_runs` function to extract the ISR* value and add it to each run. Then I'll update `compute_row` to include this ISR_star field in the returned dictionary, which will automatically appear in the DataFrame. For the statistical test, I'm creating a function that filters ISR and RANDOM conditions by their ISR_star values and performs a Mann-Whitney U test if there's enough data.

Now I'm deciding whether to make these edits locally and transfer them to the server, or edit directly on the remote machine.  Since the script lives on the server at `/root/solver-trace-ablation`, I'll edit the local copy first and then push the changes up using scp or ssh.

Let me map out the specific edits I need to make: loading eval_results.json in `discover_runs`, adding ISR_star to the returned dict in `compute_row`, creating a new `mannwhitney_isr_star` function after the existing Mann-Whitney test, and updating `condition_stats` to include ISR_star in the metrics output.

Then I'll need to add ISR* columns and rows to the print functions—updating `print_per_seed_table`, `print_condition_stats`, and `print_tests`—and finally updating `generate_markdown` to include ISR* in Table A1 and add the Mann-Whitney test section, with `main` calling the new function and passing it through to all the output functions.

Let me start making these changes now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "313b4334-e667-4cb4-aa82-113638149d96",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K3bcnnzQaqMq8vAeHrYNrN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10222,
      "cache_read_input_tokens": 34070,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10222
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

_source line 18_

I have all the data. ISR* field is `summary.proved_only_mean_isr`. Now I'll make the edits to the local script.

**Edit 1**: In `discover_runs`, load ISR* from eval_results.json.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "f268feea-6cc4-41b8-a0a3-854af85a353f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K3bcnnzQaqMq8vAeHrYNrN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10222,
      "cache_read_input_tokens": 34070,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10222
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

_source line 19_

<details open><summary>🔧 Tool call — Edit · `toolu_01NE1xBD5MmtUN6NVEJyoEQP`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/scripts/d134_analysis.py",
  "old_string": "        seen.add(key)\n        runs.append({\"dir_name\": name, \"seed\": seed_val, \"condition\": cond, \"data\": data})\n    return runs",
  "new_string": "        seen.add(key)\n        isr_star = None\n        if entry.is_dir():\n            eval_path = entry / \"eval_results.json\"\n            if eval_path.exists():\n                with open(eval_path) as ef:\n                    eval_raw = json.load(ef)\n                isr_star = eval_raw.get(\"summary\", {}).get(\"proved_only_mean_isr\")\n        runs.append({\"dir_name\": name, \"seed\": seed_val, \"condition\": cond,\n                      \"data\": data, \"isr_star\": isr_star})\n    return runs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "f88769b6-0e5d-45f1-ab69-a894aae1b679",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K3bcnnzQaqMq8vAeHrYNrN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10222,
      "cache_read_input_tokens": 34070,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10222
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

_source line 20 · 2026-05-18T23:32:09.713Z_

<details><summary>↩ Tool result · `toolu_01NE1xBD5MmtUN6NVEJyoEQP`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/scripts/d134_analysis.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "06ae07ed-cc50-46c5-91ac-ffb1c7933f57",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/scripts/d134_analysis.py",
    "oldString": "        seen.add(key)\n        runs.append({\"dir_name\": name, \"seed\": seed_val, \"condition\": cond, \"data\": data})\n    return runs",
    "newString": "        seen.add(key)\n        isr_star = None\n        if entry.is_dir():\n            eval_path = entry / \"eval_results.json\"\n            if eval_path.exists():\n                with open(eval_path) as ef:\n                    eval_raw = json.load(ef)\n                isr_star = eval_raw.get(\"summary\", {}).get(\"proved_only_mean_isr\")\n        runs.append({\"dir_name\": name, \"seed\": seed_val, \"condition\": cond,\n                      \"data\": data, \"isr_star\": isr_star})\n    return runs",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"D134 experiment analysis: multi-seed ISR vs Random, 4B GRPO training.\nReads taxonomy data from classify.json, taxonomy.json, or top-level taxonomy files.\nComputes summary stats, statistical tests (Fisher, Mann-Whitney, permutation, Bayes Factor),\nand BCa bootstrap CIs. Outputs appendix-ready markdown.\n\"\"\"\n\nimport argparse\nimport json\nimport re\nimport sys\nfrom pathlib import Path\n\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\nfrom scipy.special import betaln\n\nCONDITION_MAP = [\n    (\"d134_4b_isr\", \"ISR\"),\n    (\"d134_4b_random\", \"RANDOM\"),\n    (\"plan002_additive\", \"ISR\"),\n    (\"plan018_additive_random\", \"RANDOM\"),\n    (\"plan018_random\", \"RANDOM\"),\n]\n\nMODE_PREFIXES = {\n    \"d134_only\": [\"d134_4b\"],\n    \"all\": [\"d134_4b\", \"plan002_additive_b01\", \"plan018_additive_random_b01\", \"plan018_random\"],\n}\n\n\ndef parse_args():\n    p = argparse.ArgumentParser(description=\"D134 multi-seed analysis and statistical tests\")\n    p.add_argument(\"--data_dir\", type=str, default=\"/root/autodl-tmp/outputs\",\n                   help=\"Directory containing experiment outputs\")\n    p.add_argument(\"--mode\", type=str, default=\"d134_only\", choices=list(MODE_PREFIXES),\n                   help=\"d134_only = matched 5+5 design (default); all = include original seeds\")\n    p.add_argument(\"--prefix\", type=str, default=None,\n                   help=\"(Legacy) Single prefix filter; overrides mode/prefixes\")\n    p.add_argument(\"--prefixes\", type=str, default=None,\n                   help=\"Comma-separated prefixes; overrides --mode\")\n    p.add_argument(\"--output\", type=str, default=None,\n                   help=\"Write markdown summary to this file\")\n    p.add_argument(\"--n_perm\", type=int, default=10000,\n                   help=\"Number of permutations for permutation test\")\n    p.add_argument(\"--n_boot\", type=int, default=10000,\n                   help=\"Number of bootstrap resamples for BCa CI\")\n    p.add_argument(\"--seed\", type=int, default=42,\n                   help=\"Random seed for permutation/bootstrap\")\n    return p.parse_args()\n\n\n# --- Data loading ---\n\ndef match_condition(name: str) -> str | None:\n    best_prefix = \"\"\n    best_cond = None\n    for prefix, cond in CONDITION_MAP:\n        if name.startswith(prefix) and len(prefix) > len(best_prefix):\n            best_prefix = prefix\n            best_cond = cond\n    return best_cond\n\n\ndef extract_seed(name: str) -> int | None:\n    m = re.search(r'_s(\\d+)', name)\n    return int(m.group(1)) if m else None\n\n\ndef load_eval_results(path: Path) -> dict | None:\n    if not path.exists():\n        return None\n    with open(path) as f:\n        data = json.load(f)\n    if \"eval_results\" in data:\n        return data[\"eval_results\"]\n    return data\n\n\ndef load_taxonomy_unified(path: Path) -> dict | None:\n    with open(path) as f:\n        raw = json.load(f)\n    t = raw.get(\"taxonomy\", {})\n    proved = t.get(\"proved\", 0)\n    if proved == 0:\n        return None\n    h7 = t.get(\"H7\", 0)\n    h1 = t.get(\"H1_exact\", 0)\n    h8 = t.get(\"H8\", 0)\n    genuine = t.get(\"genuine\", 0)\n    return {\n        \"n_total\": 100, \"n_proved\": proved,\n        \"h7_total_count\": h7, \"h7_total_rate\": h7 / proved,\n        \"h1_strict_count\": h1, \"h8_conjunction_collapse_count\": h8,\n        \"genuine_count\": genuine, \"genuine_rate\": genuine / proved,\n        \"content_independent_count\": 0,\n    }\n\n\ndef load_taxonomy_verification(path: Path) -> dict | None:\n    with open(path) as f:\n        raw = json.load(f)\n    proved = raw.get(\"proved\", 0)\n    if proved == 0:\n        return None\n    tax = raw.get(\"taxonomy\", {})\n    h7 = tax.get(\"h7\", {}).get(\"count\", 0)\n    h1 = tax.get(\"h1_exact\", {}).get(\"count\", 0)\n    h8 = tax.get(\"h8\", {}).get(\"count\", 0)\n    genuine = tax.get(\"genuine\", {}).get(\"count\", 0)\n    return {\n        \"n_total\": raw.get(\"total\", 100), \"n_proved\": proved,\n        \"h7_total_count\": h7, \"h7_total_rate\": h7 / proved,\n        \"h1_strict_count\": h1, \"h8_conjunction_collapse_count\": h8,\n        \"genuine_count\": genuine, \"genuine_rate\": genuine / proved,\n        \"content_independent_count\": 0,\n    }\n\n\ndef discover_runs(data_dir: Path, prefixes: list[str]) -> list[dict]:\n    runs = []\n    seen = set()\n    for entry in sorted(data_dir.iterdir()):\n        name = entry.name\n        if not any(name.startswith(p) for p in prefixes):\n            continue\n        cond = match_condition(name)\n        seed_val = extract_seed(name)\n        if cond is None or seed_val is None:\n            continue\n        key = (cond, seed_val)\n        if key in seen:\n            continue\n        data = None\n        if entry.is_dir():\n            for fname in [\"classify.json\", \"taxonomy.json\"]:\n                data = load_eval_results(entry / fname)\n                if data is not None:\n                    break\n            if data is None:\n                continue\n        elif entry.is_file():\n            if name.endswith(\"_taxonomy_unified.json\"):\n                data = load_taxonomy_unified(entry)\n            elif name.endswith(\"_taxonomy_verification.json\"):\n                data = load_taxonomy_verification(entry)\n            if data is None:\n                continue\n        else:\n            continue\n        seen.add(key)\n        runs.append({\"dir_name\": name, \"seed\": seed_val, \"condition\": cond, \"data\": data})\n    return runs\n\n\ndef compute_row(run: dict) -> dict:\n    d = run[\"data\"]\n    n_proved = d.get(\"n_proved\", 0)\n    n_total = d.get(\"n_total\", 100)\n    h7 = d.get(\"h7_total_count\", 0)\n    h7_rate = d.get(\"h7_total_rate\", h7 / n_proved if n_proved > 0 else 0.0)\n    h1 = d.get(\"h1_strict_count\", 0)\n    h8 = d.get(\"h8_conjunction_collapse_count\", 0)\n    genuine = d.get(\"genuine_count\", 0)\n    genuine_rate = d.get(\"genuine_rate\", genuine / n_proved if n_proved > 0 else 0.0)\n    ci = d.get(\"content_independent_count\", 0)\n    snh = max(genuine - ci, 0)\n    snh_rate = snh / n_proved if n_proved > 0 else 0.0\n    return {\n        \"seed\": run[\"seed\"], \"condition\": run[\"condition\"], \"n_total\": n_total,\n        \"PR\": n_proved, \"H7_count\": h7, \"H7_rate\": h7_rate,\n        \"H1_count\": h1, \"H8_count\": h8,\n        \"genuine_count\": genuine, \"genuine_rate\": genuine_rate,\n        \"CI_count\": ci, \"SNH_count\": snh, \"SNH_rate\": snh_rate,\n    }\n\n\ndef build_table(runs: list[dict]) -> pd.DataFrame:\n    rows = [compute_row(r) for r in runs]\n    df = pd.DataFrame(rows)\n    df = df.sort_values([\"condition\", \"seed\"]).reset_index(drop=True)\n    return df\n\n\n# --- Statistical tests ---\n\ndef fisher_h7_domination(df: pd.DataFrame) -> dict:\n    results = {}\n    for cond in [\"ISR\", \"RANDOM\"]:\n        sub = df[df[\"condition\"] == cond]\n        results[cond] = {\n            \"n\": len(sub),\n            \"h7_dom\": int((sub[\"H7_rate\"] >= 0.5).sum()),\n            \"not_h7_dom\": int((sub[\"H7_rate\"] < 0.5).sum()),\n        }\n    table = np.array([\n        [results[\"ISR\"][\"h7_dom\"], results[\"ISR\"][\"not_h7_dom\"]],\n        [results[\"RANDOM\"][\"h7_dom\"], results[\"RANDOM\"][\"not_h7_dom\"]],\n    ])\n    odds_ratio, p_value = stats.fisher_exact(table, alternative=\"greater\")\n\n    # 95% exact CI via scipy.stats.contingency\n    or_ci_lo, or_ci_hi = np.nan, np.nan\n    try:\n        ct = stats.contingency.odds_ratio(table)\n        ci = ct.confidence_interval(confidence_level=0.95)\n        or_ci_lo, or_ci_hi = ci.low, ci.high\n    except Exception:\n        pass\n\n    return {\n        \"table\": table.tolist(),\n        \"ISR\": results[\"ISR\"],\n        \"RANDOM\": results[\"RANDOM\"],\n        \"odds_ratio\": odds_ratio,\n        \"or_ci_lo\": or_ci_lo,\n        \"or_ci_hi\": or_ci_hi,\n        \"p_value\": p_value,\n    }\n\n\ndef permutation_test_genuine(df: pd.DataFrame, n_perm: int = 10000,\n                              rng_seed: int = 42) -> dict:\n    isr = df[df[\"condition\"] == \"ISR\"][\"genuine_rate\"].values\n    rand = df[df[\"condition\"] == \"RANDOM\"][\"genuine_rate\"].values\n    observed = isr.mean() - rand.mean()\n    pooled = np.concatenate([isr, rand])\n    n_isr = len(isr)\n    rng = np.random.default_rng(rng_seed)\n    count = 0\n    for _ in range(n_perm):\n        perm = rng.permutation(pooled)\n        if perm[:n_isr].mean() - perm[n_isr:].mean() >= observed:\n            count += 1\n    return {\n        \"observed_diff\": float(observed),\n        \"p_value\": count / n_perm,\n        \"n_perm\": n_perm,\n        \"isr_mean\": float(isr.mean()),\n        \"random_mean\": float(rand.mean()),\n    }\n\n\ndef mannwhitney_h7(df: pd.DataFrame) -> dict:\n    isr = df[df[\"condition\"] == \"ISR\"][\"H7_rate\"].values\n    rand = df[df[\"condition\"] == \"RANDOM\"][\"H7_rate\"].values\n    n1, n2 = len(isr), len(rand)\n    u_stat, p_value = stats.mannwhitneyu(isr, rand, alternative=\"greater\")\n    r_rb = 2.0 * u_stat / (n1 * n2) - 1.0 if n1 * n2 > 0 else np.nan\n    return {\n        \"U\": float(u_stat),\n        \"p_value\": float(p_value),\n        \"r_rank_biserial\": float(r_rb),\n        \"isr_median\": float(np.median(isr)),\n        \"random_median\": float(np.median(rand)),\n    }\n\n\ndef bca_bootstrap_ci(df: pd.DataFrame, metric: str, n_boot: int = 10000,\n                      rng_seed: int = 42) -> dict:\n    \"\"\"BCa 95% CI for per-condition means of a metric.\"\"\"\n    result = {}\n    for cond in [\"ISR\", \"RANDOM\"]:\n        vals = df[df[\"condition\"] == cond][metric].values\n        if len(vals) < 2:\n            result[cond] = {\"mean\": float(vals.mean()) if len(vals) else np.nan,\n                            \"ci_lo\": np.nan, \"ci_hi\": np.nan}\n            continue\n        res = stats.bootstrap(\n            (vals,), np.mean, n_resamples=n_boot,\n            confidence_level=0.95, method=\"BCa\",\n            random_state=np.random.default_rng(rng_seed),\n        )\n        result[cond] = {\n            \"mean\": float(vals.mean()),\n            \"ci_lo\": float(res.confidence_interval.low),\n            \"ci_hi\": float(res.confidence_interval.high),\n        }\n    return result\n\n\ndef bayes_factor_h7_domination(df: pd.DataFrame) -> dict:\n    \"\"\"BF10 for H7-domination rate difference (beta-binomial conjugate).\n    H0: ISR and Random share same domination rate.\n    H1: independent rates. Prior: Beta(1,1) on each.\n    \"\"\"\n    isr_sub = df[df[\"condition\"] == \"ISR\"]\n    rand_sub = df[df[\"condition\"] == \"RANDOM\"]\n    k_isr = int((isr_sub[\"H7_rate\"] >= 0.5).sum())\n    n_isr = len(isr_sub)\n    k_rand = int((rand_sub[\"H7_rate\"] >= 0.5).sum())\n    n_rand = len(rand_sub)\n    k_total = k_isr + k_rand\n    n_total = n_isr + n_rand\n\n    # log marginal under H0 (shared rate)\n    log_m_h0 = betaln(1 + k_total, 1 + n_total - k_total) - betaln(1, 1)\n    # log marginal under H1 (independent rates)\n    log_m_h1 = (betaln(1 + k_isr, 1 + n_isr - k_isr) - betaln(1, 1)\n                + betaln(1 + k_rand, 1 + n_rand - k_rand) - betaln(1, 1))\n    log_bf10 = log_m_h1 - log_m_h0\n    bf10 = float(np.exp(log_bf10))\n\n    return {\n        \"k_isr\": k_isr, \"n_isr\": n_isr,\n        \"k_rand\": k_rand, \"n_rand\": n_rand,\n        \"bf10\": bf10,\n        \"log_bf10\": float(log_bf10),\n        \"interpretation\": _interpret_bf(bf10),\n    }\n\n\ndef _interpret_bf(bf: float) -> str:\n    if bf > 100:\n        return \"extreme evidence for H1\"\n    if bf > 30:\n        return \"very strong evidence for H1\"\n    if bf > 10:\n        return \"strong evidence for H1\"\n    if bf > 3:\n        return \"moderate evidence for H1\"\n    if bf > 1:\n        return \"anecdotal evidence for H1\"\n    if bf > 1/3:\n        return \"anecdotal evidence (inconclusive)\"\n    if bf > 1/10:\n        return \"moderate evidence for H0\"\n    return \"strong evidence for H0\"\n\n\ndef condition_stats(df: pd.DataFrame) -> pd.DataFrame:\n    metrics = [\"PR\", \"H7_rate\", \"genuine_rate\", \"SNH_rate\"]\n    rows = []\n    for cond in [\"ISR\", \"RANDOM\"]:\n        sub = df[df[\"condition\"] == cond]\n        row = {\"condition\": cond, \"n_seeds\": len(sub)}\n        for m in metrics:\n            vals = sub[m].values\n            row[f\"{m}_mean\"] = vals.mean()\n            row[f\"{m}_std\"] = vals.std(ddof=1) if len(vals) > 1 else 0.0\n        rows.append(row)\n    return pd.DataFrame(rows)\n\n\n# --- Formatting ---\n\ndef fmt_pct(val: float) -> str:\n    return f\"{val*100:.1f}\\\\%\"\n\ndef fmt_or(val: float) -> str:\n    return \"$\\\\infty$\" if np.isinf(val) else f\"{val:.2f}\"\n\ndef fmt_ci(lo: float, hi: float) -> str:\n    lo_s = f\"{lo:.2f}\" if not np.isnan(lo) else \"0\"\n    hi_s = \"$\\\\infty$\" if np.isinf(hi) or np.isnan(hi) else f\"{hi:.2f}\"\n    return f\"[{lo_s}, {hi_s}]\"\n\ndef fmt_p(p: float) -> str:\n    if p < 0.001:\n        return \"$<$0.001\"\n    return f\"{p:.3f}\"\n\ndef fmt_mean_std(mean: float, std: float, pct: bool = False) -> str:\n    if pct:\n        return f\"{mean*100:.1f} $\\\\pm$ {std*100:.1f}\\\\%\"\n    return f\"{mean:.1f} $\\\\pm$ {std:.1f}\"\n\ndef fmt_bca(bca: dict, pct: bool = False) -> str:\n    m = bca[\"mean\"]\n    lo, hi = bca[\"ci_lo\"], bca[\"ci_hi\"]\n    if pct:\n        return f\"{m*100:.1f}\\\\% [{lo*100:.1f}, {hi*100:.1f}]\"\n    return f\"{m:.1f} [{lo:.1f}, {hi:.1f}]\"\n\n\n# --- Console output ---\n\ndef print_per_seed_table(df: pd.DataFrame):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  PER-SEED RESULTS\")\n    print(\"=\" * 90)\n    cols = [\"condition\", \"seed\", \"PR\", \"H7_count\", \"H7_rate\", \"H1_count\",\n            \"H8_count\", \"genuine_count\", \"genuine_rate\", \"CI_count\", \"SNH_count\", \"SNH_rate\"]\n    fmt = df[cols].copy()\n    for c in [\"H7_rate\", \"genuine_rate\", \"SNH_rate\"]:\n        fmt[c] = fmt[c].apply(lambda v: f\"{v*100:.1f}%\")\n    print(fmt.to_string(index=False))\n\n\ndef print_condition_stats(cond_df: pd.DataFrame):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  CONDITION-LEVEL STATISTICS (mean +/- SD)\")\n    print(\"=\" * 90)\n    for _, row in cond_df.iterrows():\n        n = int(row['n_seeds'])\n        print(f\"\\n  {row['condition']} (n={n} seeds):\")\n        print(f\"    PR:           {row['PR_mean']:.1f} +/- {row['PR_std']:.1f}\")\n        print(f\"    H7 rate:      {row['H7_rate_mean']*100:.1f} +/- {row['H7_rate_std']*100:.1f}%\")\n        print(f\"    Genuine rate: {row['genuine_rate_mean']*100:.1f} +/- {row['genuine_rate_std']*100:.1f}%\")\n        print(f\"    S-NH rate:    {row['SNH_rate_mean']*100:.1f} +/- {row['SNH_rate_std']*100:.1f}%\")\n\n\ndef print_tests(fisher, perm, mw, bf, bca_h7, bca_gen):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  STATISTICAL TESTS\")\n    print(\"=\" * 90)\n\n    print(\"\\n  1. H7 Domination Fisher Exact Test (H7-dominated = H7% >= 50%)\")\n    print(f\"     ISR:    {fisher['ISR']['h7_dom']} dominated / {fisher['ISR']['n']} seeds\")\n    print(f\"     RANDOM: {fisher['RANDOM']['h7_dom']} dominated / {fisher['RANDOM']['n']} seeds\")\n    print(f\"     Contingency: {fisher['table']}\")\n    or_str = \"inf\" if np.isinf(fisher['odds_ratio']) else f\"{fisher['odds_ratio']:.4f}\"\n    print(f\"     OR = {or_str}, 95% CI = [{fisher['or_ci_lo']:.4f}, {fisher['or_ci_hi']:.4f}]\"\n          if not np.isnan(fisher['or_ci_lo']) else f\"     OR = {or_str}, 95% CI = N/A\")\n    print(f\"     p-value (one-sided, greater): {fisher['p_value']:.4f}\")\n\n    print(f\"\\n  2. Genuine Rate Permutation Test (n_perm={perm['n_perm']})\")\n    print(f\"     ISR mean:    {perm['isr_mean']*100:.2f}%\")\n    print(f\"     RANDOM mean: {perm['random_mean']*100:.2f}%\")\n    print(f\"     Diff: {perm['observed_diff']*100:.2f} pp, p = {perm['p_value']:.4f}\")\n\n    print(f\"\\n  3. H7 Rate Mann-Whitney U Test\")\n    print(f\"     ISR median:    {mw['isr_median']*100:.1f}%\")\n    print(f\"     RANDOM median: {mw['random_median']*100:.1f}%\")\n    print(f\"     U = {mw['U']:.1f}, p = {mw['p_value']:.4f}\")\n    print(f\"     Rank-biserial r = {mw['r_rank_biserial']:.4f}\")\n\n    print(f\"\\n  4. Bayes Factor (H7 Domination, Beta-Binomial)\")\n    print(f\"     ISR:    {bf['k_isr']}/{bf['n_isr']} dominated\")\n    print(f\"     RANDOM: {bf['k_rand']}/{bf['n_rand']} dominated\")\n    print(f\"     BF10 = {bf['bf10']:.4f} ({bf['interpretation']})\")\n\n    print(f\"\\n  5. BCa Bootstrap 95% CI (n_boot resamples)\")\n    for label, bca in [(\"H7 rate\", bca_h7), (\"Genuine rate\", bca_gen)]:\n        print(f\"     {label}:\")\n        for cond in [\"ISR\", \"RANDOM\"]:\n            b = bca[cond]\n            print(f\"       {cond}: {b['mean']*100:.1f}% [{b['ci_lo']*100:.1f}, {b['ci_hi']*100:.1f}]\"\n                  if not np.isnan(b['ci_lo']) else f\"       {cond}: {b['mean']*100:.1f}% [N/A]\")\n\n\n# --- Markdown generation (appendix-ready) ---\n\ndef generate_markdown(df: pd.DataFrame, cond_df: pd.DataFrame,\n                      fisher: dict, perm: dict, mw: dict,\n                      bf: dict, bca_h7: dict, bca_gen: dict) -> str:\n    L = []\n    L.append(\"## D134: ISR vs Random Statistical Analysis\\n\")\n\n    # Per-seed table\n    L.append(\"### Table A1: Per-Seed Hacking Taxonomy (4B Qwen3, 500 steps)\\n\")\n    L.append(\"| Condition | Seed | PR | H7 | H7\\\\% | H1 | H8 | Genuine | Gen\\\\% | CI | S-NH | S-NH\\\\% |\")\n    L.append(\"|:----------|-----:|---:|---:|-----:|---:|---:|--------:|------:|---:|-----:|-------:|\")\n    for _, r in df.iterrows():\n        L.append(\n            f\"| {r['condition']} | {r['seed']} | {int(r['PR'])} | {int(r['H7_count'])} | \"\n            f\"{r['H7_rate']*100:.1f} | {int(r['H1_count'])} | {int(r['H8_count'])} | \"\n            f\"{int(r['genuine_count'])} | {r['genuine_rate']*100:.1f} | {int(r['CI_count'])} | \"\n            f\"{int(r['SNH_count'])} | {r['SNH_rate']*100:.1f} |\"\n        )\n\n    # Condition summary with BCa CI\n    L.append(\"\\n### Table A2: Condition-Level Summary\\n\")\n    L.append(\"| Condition | $n$ | PR (mean$\\\\pm$SD) | H7\\\\% (mean$\\\\pm$SD) | H7\\\\% BCa 95\\\\% CI | Gen\\\\% (mean$\\\\pm$SD) | Gen\\\\% BCa 95\\\\% CI |\")\n    L.append(\"|:----------|----:|:------------------|:-------------------|:-----------------|:-------------------|:-----------------|\")\n    for _, r in cond_df.iterrows():\n        cond = r[\"condition\"]\n        h7_bca = bca_h7.get(cond, {})\n        gen_bca = bca_gen.get(cond, {})\n        h7_ci = f\"[{h7_bca['ci_lo']*100:.1f}, {h7_bca['ci_hi']*100:.1f}]\" if h7_bca and not np.isnan(h7_bca.get('ci_lo', np.nan)) else \"N/A\"\n        gen_ci = f\"[{gen_bca['ci_lo']*100:.1f}, {gen_bca['ci_hi']*100:.1f}]\" if gen_bca and not np.isnan(gen_bca.get('ci_lo', np.nan)) else \"N/A\"\n        L.append(\n            f\"| {cond} | {int(r['n_seeds'])} | \"\n            f\"{r['PR_mean']:.1f}$\\\\pm${r['PR_std']:.1f} | \"\n            f\"{r['H7_rate_mean']*100:.1f}$\\\\pm${r['H7_rate_std']*100:.1f} | \"\n            f\"{h7_ci} | \"\n            f\"{r['genuine_rate_mean']*100:.1f}$\\\\pm${r['genuine_rate_std']*100:.1f} | \"\n            f\"{gen_ci} |\"\n        )\n\n    # Statistical tests\n    if fisher and perm and mw and bf:\n        L.append(\"\\n### Statistical Tests\\n\")\n\n        # Fisher\n        or_str = \"$\\\\infty$\" if np.isinf(fisher['odds_ratio']) else f\"{fisher['odds_ratio']:.2f}\"\n        ci_lo = f\"{fisher['or_ci_lo']:.2f}\" if not np.isnan(fisher['or_ci_lo']) else \"0\"\n        ci_hi = \"$\\\\infty$\" if np.isinf(fisher.get('or_ci_hi', np.inf)) or np.isnan(fisher.get('or_ci_hi', np.nan)) else f\"{fisher['or_ci_hi']:.2f}\"\n        L.append(\"**1. H7 Domination Fisher Exact Test** (threshold: H7$\\\\geq$50\\\\% of proved)\")\n        L.append(f\"- ISR: {fisher['ISR']['h7_dom']}/{fisher['ISR']['n']} seeds H7-dominated; \"\n                 f\"Random: {fisher['RANDOM']['h7_dom']}/{fisher['RANDOM']['n']}\")\n        L.append(f\"- OR = {or_str}, 95\\\\% exact CI = [{ci_lo}, {ci_hi}], \"\n                 f\"$p$ = {fmt_p(fisher['p_value'])}\")\n        L.append(\"\")\n\n        # Permutation\n        L.append(f\"**2. Genuine Rate Permutation Test** ($n$ = {perm['n_perm']:,} permutations)\")\n        L.append(f\"- ISR mean: {perm['isr_mean']*100:.2f}\\\\%, Random mean: {perm['random_mean']*100:.2f}\\\\%\")\n        L.append(f\"- $\\\\Delta$ = {perm['observed_diff']*100:.2f} pp, $p$ = {fmt_p(perm['p_value'])}\")\n        L.append(\"\")\n\n        # Mann-Whitney\n        L.append(\"**3. H7 Rate Mann-Whitney $U$ Test**\")\n        L.append(f\"- ISR median: {mw['isr_median']*100:.1f}\\\\%, Random median: {mw['random_median']*100:.1f}\\\\%\")\n        L.append(f\"- $U$ = {mw['U']:.1f}, $p$ = {fmt_p(mw['p_value'])}, \"\n                 f\"rank-biserial $r$ = {mw['r_rank_biserial']:.3f}\")\n        L.append(\"\")\n\n        # Bayes Factor\n        L.append(\"**4. Bayes Factor** (Beta-Binomial conjugate, prior: Beta(1,1))\")\n        L.append(f\"- $BF_{{10}}$ = {bf['bf10']:.2f} ({bf['interpretation']})\")\n        L.append(f\"- ISR: {bf['k_isr']}/{bf['n_isr']} H7-dominated, \"\n                 f\"Random: {bf['k_rand']}/{bf['n_rand']}\")\n\n    return \"\\n\".join(L) + \"\\n\"\n\n\n# --- Main ---\n\ndef main():\n    args = parse_args()\n    data_dir = Path(args.data_dir)\n\n    if not data_dir.exists():\n        print(f\"ERROR: data directory {data_dir} does not exist\", file=sys.stderr)\n        sys.exit(1)\n\n    if args.prefix:\n        prefixes = [args.prefix]\n    elif args.prefixes:\n        prefixes = [p.strip() for p in args.prefixes.split(\",\")]\n    else:\n        prefixes = MODE_PREFIXES[args.mode]\n    print(f\"Mode: {args.mode} | Prefixes: {prefixes}\")\n\n    runs = discover_runs(data_dir, prefixes)\n    if not runs:\n        print(f\"ERROR: no runs found in {data_dir} with prefixes {prefixes}\", file=sys.stderr)\n        sys.exit(1)\n\n    isr_count = sum(1 for r in runs if r[\"condition\"] == \"ISR\")\n    rand_count = sum(1 for r in runs if r[\"condition\"] == \"RANDOM\")\n    print(f\"Found {len(runs)} runs: {isr_count} ISR, {rand_count} RANDOM\")\n    for r in runs:\n        print(f\"  {r['condition']:6s} s{r['seed']} <- {r['dir_name']}\")\n\n    df = build_table(runs)\n    print_per_seed_table(df)\n\n    cond_df = condition_stats(df)\n    print_condition_stats(cond_df)\n\n    if isr_count < 2 or rand_count < 2:\n        print(\"\\nWARNING: need >= 2 seeds per condition for statistical tests, skipping.\",\n              file=sys.stderr)\n        bca_h7 = bca_bootstrap_ci(df, \"H7_rate\", args.n_boot, args.seed)\n        bca_gen = bca_bootstrap_ci(df, \"genuine_rate\", args.n_boot, args.seed)\n        if args.output:\n            md = generate_markdown(df, cond_df, {}, {}, {}, {}, bca_h7, bca_gen)\n            Path(args.output).write_text(md)\n            print(f\"\\nMarkdown written to {args.output}\")\n        return\n\n    fisher = fisher_h7_domination(df)\n    perm = permutation_test_genuine(df, n_perm=args.n_perm, rng_seed=args.seed)\n    mw = mannwhitney_h7(df)\n    bf = bayes_factor_h7_domination(df)\n    bca_h7 = bca_bootstrap_ci(df, \"H7_rate\", args.n_boot, args.seed)\n    bca_gen = bca_bootstrap_ci(df, \"genuine_rate\", args.n_boot, args.seed)\n\n    print_tests(fisher, perm, mw, bf, bca_h7, bca_gen)\n\n    md = generate_markdown(df, cond_df, fisher, perm, mw, bf, bca_h7, bca_gen)\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  MARKDOWN OUTPUT (appendix-ready)\")\n    print(\"=\" * 90)\n    print(md)\n\n    if args.output:\n        Path(args.output).parent.mkdir(parents=True, exist_ok=True)\n        Path(args.output).write_text(md)\n        print(f\"Markdown written to {args.output}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 150,
        "oldLines": 7,
        "newStart": 150,
        "newLines": 15,
        "lines": [
          "         else:",
          "             continue",
          "         seen.add(key)",
          "-        runs.append({\"dir_name\": name, \"seed\": seed_val, \"condition\": cond, \"data\": data})",
          "+        isr_star = None",
          "+        if entry.is_dir():",
          "+            eval_path = entry / \"eval_results.json\"",
          "+            if eval_path.exists():",
          "+                with open(eval_path) as ef:",
          "+                    eval_raw = json.load(ef)",
          "+                isr_star = eval_raw.get(\"summary\", {}).get(\"proved_only_mean_isr\")",
          "+        runs.append({\"dir_name\": name, \"seed\": seed_val, \"condition\": cond,",
          "+                      \"data\": data, \"isr_star\": isr_star})",
          "     return runs",
          " ",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 21_

**Edit 2**: Add ISR_star to `compute_row`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "9976abea-69fe-4d1d-989c-606afcfa1220",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WibNMuhFXQHZqij8GcdzS9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1984,
      "cache_read_input_tokens": 44292,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1984
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

_source line 22_

<details open><summary>🔧 Tool call — Edit · `toolu_011gTEAtFym1biH3dQECPJtb`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/scripts/d134_analysis.py",
  "old_string": "    return {\n        \"seed\": run[\"seed\"], \"condition\": run[\"condition\"], \"n_total\": n_total,\n        \"PR\": n_proved, \"H7_count\": h7, \"H7_rate\": h7_rate,\n        \"H1_count\": h1, \"H8_count\": h8,\n        \"genuine_count\": genuine, \"genuine_rate\": genuine_rate,\n        \"CI_count\": ci, \"SNH_count\": snh, \"SNH_rate\": snh_rate,\n    }",
  "new_string": "    return {\n        \"seed\": run[\"seed\"], \"condition\": run[\"condition\"], \"n_total\": n_total,\n        \"PR\": n_proved, \"H7_count\": h7, \"H7_rate\": h7_rate,\n        \"H1_count\": h1, \"H8_count\": h8,\n        \"genuine_count\": genuine, \"genuine_rate\": genuine_rate,\n        \"CI_count\": ci, \"SNH_count\": snh, \"SNH_rate\": snh_rate,\n        \"ISR_star\": run.get(\"isr_star\"),\n    }"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "b5e59f9a-aa1b-43f1-894d-bef63d3505aa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WibNMuhFXQHZqij8GcdzS9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1984,
      "cache_read_input_tokens": 44292,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1984
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

_source line 23 · 2026-05-18T23:32:15.872Z_

<details><summary>↩ Tool result · `toolu_011gTEAtFym1biH3dQECPJtb`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/scripts/d134_analysis.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "d710c4ca-4f2f-4e50-9d64-2fdad7317257",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/scripts/d134_analysis.py",
    "oldString": "    return {\n        \"seed\": run[\"seed\"], \"condition\": run[\"condition\"], \"n_total\": n_total,\n        \"PR\": n_proved, \"H7_count\": h7, \"H7_rate\": h7_rate,\n        \"H1_count\": h1, \"H8_count\": h8,\n        \"genuine_count\": genuine, \"genuine_rate\": genuine_rate,\n        \"CI_count\": ci, \"SNH_count\": snh, \"SNH_rate\": snh_rate,\n    }",
    "newString": "    return {\n        \"seed\": run[\"seed\"], \"condition\": run[\"condition\"], \"n_total\": n_total,\n        \"PR\": n_proved, \"H7_count\": h7, \"H7_rate\": h7_rate,\n        \"H1_count\": h1, \"H8_count\": h8,\n        \"genuine_count\": genuine, \"genuine_rate\": genuine_rate,\n        \"CI_count\": ci, \"SNH_count\": snh, \"SNH_rate\": snh_rate,\n        \"ISR_star\": run.get(\"isr_star\"),\n    }",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"D134 experiment analysis: multi-seed ISR vs Random, 4B GRPO training.\nReads taxonomy data from classify.json, taxonomy.json, or top-level taxonomy files.\nComputes summary stats, statistical tests (Fisher, Mann-Whitney, permutation, Bayes Factor),\nand BCa bootstrap CIs. Outputs appendix-ready markdown.\n\"\"\"\n\nimport argparse\nimport json\nimport re\nimport sys\nfrom pathlib import Path\n\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\nfrom scipy.special import betaln\n\nCONDITION_MAP = [\n    (\"d134_4b_isr\", \"ISR\"),\n    (\"d134_4b_random\", \"RANDOM\"),\n    (\"plan002_additive\", \"ISR\"),\n    (\"plan018_additive_random\", \"RANDOM\"),\n    (\"plan018_random\", \"RANDOM\"),\n]\n\nMODE_PREFIXES = {\n    \"d134_only\": [\"d134_4b\"],\n    \"all\": [\"d134_4b\", \"plan002_additive_b01\", \"plan018_additive_random_b01\", \"plan018_random\"],\n}\n\n\ndef parse_args():\n    p = argparse.ArgumentParser(description=\"D134 multi-seed analysis and statistical tests\")\n    p.add_argument(\"--data_dir\", type=str, default=\"/root/autodl-tmp/outputs\",\n                   help=\"Directory containing experiment outputs\")\n    p.add_argument(\"--mode\", type=str, default=\"d134_only\", choices=list(MODE_PREFIXES),\n                   help=\"d134_only = matched 5+5 design (default); all = include original seeds\")\n    p.add_argument(\"--prefix\", type=str, default=None,\n                   help=\"(Legacy) Single prefix filter; overrides mode/prefixes\")\n    p.add_argument(\"--prefixes\", type=str, default=None,\n                   help=\"Comma-separated prefixes; overrides --mode\")\n    p.add_argument(\"--output\", type=str, default=None,\n                   help=\"Write markdown summary to this file\")\n    p.add_argument(\"--n_perm\", type=int, default=10000,\n                   help=\"Number of permutations for permutation test\")\n    p.add_argument(\"--n_boot\", type=int, default=10000,\n                   help=\"Number of bootstrap resamples for BCa CI\")\n    p.add_argument(\"--seed\", type=int, default=42,\n                   help=\"Random seed for permutation/bootstrap\")\n    return p.parse_args()\n\n\n# --- Data loading ---\n\ndef match_condition(name: str) -> str | None:\n    best_prefix = \"\"\n    best_cond = None\n    for prefix, cond in CONDITION_MAP:\n        if name.startswith(prefix) and len(prefix) > len(best_prefix):\n            best_prefix = prefix\n            best_cond = cond\n    return best_cond\n\n\ndef extract_seed(name: str) -> int | None:\n    m = re.search(r'_s(\\d+)', name)\n    return int(m.group(1)) if m else None\n\n\ndef load_eval_results(path: Path) -> dict | None:\n    if not path.exists():\n        return None\n    with open(path) as f:\n        data = json.load(f)\n    if \"eval_results\" in data:\n        return data[\"eval_results\"]\n    return data\n\n\ndef load_taxonomy_unified(path: Path) -> dict | None:\n    with open(path) as f:\n        raw = json.load(f)\n    t = raw.get(\"taxonomy\", {})\n    proved = t.get(\"proved\", 0)\n    if proved == 0:\n        return None\n    h7 = t.get(\"H7\", 0)\n    h1 = t.get(\"H1_exact\", 0)\n    h8 = t.get(\"H8\", 0)\n    genuine = t.get(\"genuine\", 0)\n    return {\n        \"n_total\": 100, \"n_proved\": proved,\n        \"h7_total_count\": h7, \"h7_total_rate\": h7 / proved,\n        \"h1_strict_count\": h1, \"h8_conjunction_collapse_count\": h8,\n        \"genuine_count\": genuine, \"genuine_rate\": genuine / proved,\n        \"content_independent_count\": 0,\n    }\n\n\ndef load_taxonomy_verification(path: Path) -> dict | None:\n    with open(path) as f:\n        raw = json.load(f)\n    proved = raw.get(\"proved\", 0)\n    if proved == 0:\n        return None\n    tax = raw.get(\"taxonomy\", {})\n    h7 = tax.get(\"h7\", {}).get(\"count\", 0)\n    h1 = tax.get(\"h1_exact\", {}).get(\"count\", 0)\n    h8 = tax.get(\"h8\", {}).get(\"count\", 0)\n    genuine = tax.get(\"genuine\", {}).get(\"count\", 0)\n    return {\n        \"n_total\": raw.get(\"total\", 100), \"n_proved\": proved,\n        \"h7_total_count\": h7, \"h7_total_rate\": h7 / proved,\n        \"h1_strict_count\": h1, \"h8_conjunction_collapse_count\": h8,\n        \"genuine_count\": genuine, \"genuine_rate\": genuine / proved,\n        \"content_independent_count\": 0,\n    }\n\n\ndef discover_runs(data_dir: Path, prefixes: list[str]) -> list[dict]:\n    runs = []\n    seen = set()\n    for entry in sorted(data_dir.iterdir()):\n        name = entry.name\n        if not any(name.startswith(p) for p in prefixes):\n            continue\n        cond = match_condition(name)\n        seed_val = extract_seed(name)\n        if cond is None or seed_val is None:\n            continue\n        key = (cond, seed_val)\n        if key in seen:\n            continue\n        data = None\n        if entry.is_dir():\n            for fname in [\"classify.json\", \"taxonomy.json\"]:\n                data = load_eval_results(entry / fname)\n                if data is not None:\n                    break\n            if data is None:\n                continue\n        elif entry.is_file():\n            if name.endswith(\"_taxonomy_unified.json\"):\n                data = load_taxonomy_unified(entry)\n            elif name.endswith(\"_taxonomy_verification.json\"):\n                data = load_taxonomy_verification(entry)\n            if data is None:\n                continue\n        else:\n            continue\n        seen.add(key)\n        isr_star = None\n        if entry.is_dir():\n            eval_path = entry / \"eval_results.json\"\n            if eval_path.exists():\n                with open(eval_path) as ef:\n                    eval_raw = json.load(ef)\n                isr_star = eval_raw.get(\"summary\", {}).get(\"proved_only_mean_isr\")\n        runs.append({\"dir_name\": name, \"seed\": seed_val, \"condition\": cond,\n                      \"data\": data, \"isr_star\": isr_star})\n    return runs\n\n\ndef compute_row(run: dict) -> dict:\n    d = run[\"data\"]\n    n_proved = d.get(\"n_proved\", 0)\n    n_total = d.get(\"n_total\", 100)\n    h7 = d.get(\"h7_total_count\", 0)\n    h7_rate = d.get(\"h7_total_rate\", h7 / n_proved if n_proved > 0 else 0.0)\n    h1 = d.get(\"h1_strict_count\", 0)\n    h8 = d.get(\"h8_conjunction_collapse_count\", 0)\n    genuine = d.get(\"genuine_count\", 0)\n    genuine_rate = d.get(\"genuine_rate\", genuine / n_proved if n_proved > 0 else 0.0)\n    ci = d.get(\"content_independent_count\", 0)\n    snh = max(genuine - ci, 0)\n    snh_rate = snh / n_proved if n_proved > 0 else 0.0\n    return {\n        \"seed\": run[\"seed\"], \"condition\": run[\"condition\"], \"n_total\": n_total,\n        \"PR\": n_proved, \"H7_count\": h7, \"H7_rate\": h7_rate,\n        \"H1_count\": h1, \"H8_count\": h8,\n        \"genuine_count\": genuine, \"genuine_rate\": genuine_rate,\n        \"CI_count\": ci, \"SNH_count\": snh, \"SNH_rate\": snh_rate,\n    }\n\n\ndef build_table(runs: list[dict]) -> pd.DataFrame:\n    rows = [compute_row(r) for r in runs]\n    df = pd.DataFrame(rows)\n    df = df.sort_values([\"condition\", \"seed\"]).reset_index(drop=True)\n    return df\n\n\n# --- Statistical tests ---\n\ndef fisher_h7_domination(df: pd.DataFrame) -> dict:\n    results = {}\n    for cond in [\"ISR\", \"RANDOM\"]:\n        sub = df[df[\"condition\"] == cond]\n        results[cond] = {\n            \"n\": len(sub),\n            \"h7_dom\": int((sub[\"H7_rate\"] >= 0.5).sum()),\n            \"not_h7_dom\": int((sub[\"H7_rate\"] < 0.5).sum()),\n        }\n    table = np.array([\n        [results[\"ISR\"][\"h7_dom\"], results[\"ISR\"][\"not_h7_dom\"]],\n        [results[\"RANDOM\"][\"h7_dom\"], results[\"RANDOM\"][\"not_h7_dom\"]],\n    ])\n    odds_ratio, p_value = stats.fisher_exact(table, alternative=\"greater\")\n\n    # 95% exact CI via scipy.stats.contingency\n    or_ci_lo, or_ci_hi = np.nan, np.nan\n    try:\n        ct = stats.contingency.odds_ratio(table)\n        ci = ct.confidence_interval(confidence_level=0.95)\n        or_ci_lo, or_ci_hi = ci.low, ci.high\n    except Exception:\n        pass\n\n    return {\n        \"table\": table.tolist(),\n        \"ISR\": results[\"ISR\"],\n        \"RANDOM\": results[\"RANDOM\"],\n        \"odds_ratio\": odds_ratio,\n        \"or_ci_lo\": or_ci_lo,\n        \"or_ci_hi\": or_ci_hi,\n        \"p_value\": p_value,\n    }\n\n\ndef permutation_test_genuine(df: pd.DataFrame, n_perm: int = 10000,\n                              rng_seed: int = 42) -> dict:\n    isr = df[df[\"condition\"] == \"ISR\"][\"genuine_rate\"].values\n    rand = df[df[\"condition\"] == \"RANDOM\"][\"genuine_rate\"].values\n    observed = isr.mean() - rand.mean()\n    pooled = np.concatenate([isr, rand])\n    n_isr = len(isr)\n    rng = np.random.default_rng(rng_seed)\n    count = 0\n    for _ in range(n_perm):\n        perm = rng.permutation(pooled)\n        if perm[:n_isr].mean() - perm[n_isr:].mean() >= observed:\n            count += 1\n    return {\n        \"observed_diff\": float(observed),\n        \"p_value\": count / n_perm,\n        \"n_perm\": n_perm,\n        \"isr_mean\": float(isr.mean()),\n        \"random_mean\": float(rand.mean()),\n    }\n\n\ndef mannwhitney_h7(df: pd.DataFrame) -> dict:\n    isr = df[df[\"condition\"] == \"ISR\"][\"H7_rate\"].values\n    rand = df[df[\"condition\"] == \"RANDOM\"][\"H7_rate\"].values\n    n1, n2 = len(isr), len(rand)\n    u_stat, p_value = stats.mannwhitneyu(isr, rand, alternative=\"greater\")\n    r_rb = 2.0 * u_stat / (n1 * n2) - 1.0 if n1 * n2 > 0 else np.nan\n    return {\n        \"U\": float(u_stat),\n        \"p_value\": float(p_value),\n        \"r_rank_biserial\": float(r_rb),\n        \"isr_median\": float(np.median(isr)),\n        \"random_median\": float(np.median(rand)),\n    }\n\n\ndef bca_bootstrap_ci(df: pd.DataFrame, metric: str, n_boot: int = 10000,\n                      rng_seed: int = 42) -> dict:\n    \"\"\"BCa 95% CI for per-condition means of a metric.\"\"\"\n    result = {}\n    for cond in [\"ISR\", \"RANDOM\"]:\n        vals = df[df[\"condition\"] == cond][metric].values\n        if len(vals) < 2:\n            result[cond] = {\"mean\": float(vals.mean()) if len(vals) else np.nan,\n                            \"ci_lo\": np.nan, \"ci_hi\": np.nan}\n            continue\n        res = stats.bootstrap(\n            (vals,), np.mean, n_resamples=n_boot,\n            confidence_level=0.95, method=\"BCa\",\n            random_state=np.random.default_rng(rng_seed),\n        )\n        result[cond] = {\n            \"mean\": float(vals.mean()),\n            \"ci_lo\": float(res.confidence_interval.low),\n            \"ci_hi\": float(res.confidence_interval.high),\n        }\n    return result\n\n\ndef bayes_factor_h7_domination(df: pd.DataFrame) -> dict:\n    \"\"\"BF10 for H7-domination rate difference (beta-binomial conjugate).\n    H0: ISR and Random share same domination rate.\n    H1: independent rates. Prior: Beta(1,1) on each.\n    \"\"\"\n    isr_sub = df[df[\"condition\"] == \"ISR\"]\n    rand_sub = df[df[\"condition\"] == \"RANDOM\"]\n    k_isr = int((isr_sub[\"H7_rate\"] >= 0.5).sum())\n    n_isr = len(isr_sub)\n    k_rand = int((rand_sub[\"H7_rate\"] >= 0.5).sum())\n    n_rand = len(rand_sub)\n    k_total = k_isr + k_rand\n    n_total = n_isr + n_rand\n\n    # log marginal under H0 (shared rate)\n    log_m_h0 = betaln(1 + k_total, 1 + n_total - k_total) - betaln(1, 1)\n    # log marginal under H1 (independent rates)\n    log_m_h1 = (betaln(1 + k_isr, 1 + n_isr - k_isr) - betaln(1, 1)\n                + betaln(1 + k_rand, 1 + n_rand - k_rand) - betaln(1, 1))\n    log_bf10 = log_m_h1 - log_m_h0\n    bf10 = float(np.exp(log_bf10))\n\n    return {\n        \"k_isr\": k_isr, \"n_isr\": n_isr,\n        \"k_rand\": k_rand, \"n_rand\": n_rand,\n        \"bf10\": bf10,\n        \"log_bf10\": float(log_bf10),\n        \"interpretation\": _interpret_bf(bf10),\n    }\n\n\ndef _interpret_bf(bf: float) -> str:\n    if bf > 100:\n        return \"extreme evidence for H1\"\n    if bf > 30:\n        return \"very strong evidence for H1\"\n    if bf > 10:\n        return \"strong evidence for H1\"\n    if bf > 3:\n        return \"moderate evidence for H1\"\n    if bf > 1:\n        return \"anecdotal evidence for H1\"\n    if bf > 1/3:\n        return \"anecdotal evidence (inconclusive)\"\n    if bf > 1/10:\n        return \"moderate evidence for H0\"\n    return \"strong evidence for H0\"\n\n\ndef condition_stats(df: pd.DataFrame) -> pd.DataFrame:\n    metrics = [\"PR\", \"H7_rate\", \"genuine_rate\", \"SNH_rate\"]\n    rows = []\n    for cond in [\"ISR\", \"RANDOM\"]:\n        sub = df[df[\"condition\"] == cond]\n        row = {\"condition\": cond, \"n_seeds\": len(sub)}\n        for m in metrics:\n            vals = sub[m].values\n            row[f\"{m}_mean\"] = vals.mean()\n            row[f\"{m}_std\"] = vals.std(ddof=1) if len(vals) > 1 else 0.0\n        rows.append(row)\n    return pd.DataFrame(rows)\n\n\n# --- Formatting ---\n\ndef fmt_pct(val: float) -> str:\n    return f\"{val*100:.1f}\\\\%\"\n\ndef fmt_or(val: float) -> str:\n    return \"$\\\\infty$\" if np.isinf(val) else f\"{val:.2f}\"\n\ndef fmt_ci(lo: float, hi: float) -> str:\n    lo_s = f\"{lo:.2f}\" if not np.isnan(lo) else \"0\"\n    hi_s = \"$\\\\infty$\" if np.isinf(hi) or np.isnan(hi) else f\"{hi:.2f}\"\n    return f\"[{lo_s}, {hi_s}]\"\n\ndef fmt_p(p: float) -> str:\n    if p < 0.001:\n        return \"$<$0.001\"\n    return f\"{p:.3f}\"\n\ndef fmt_mean_std(mean: float, std: float, pct: bool = False) -> str:\n    if pct:\n        return f\"{mean*100:.1f} $\\\\pm$ {std*100:.1f}\\\\%\"\n    return f\"{mean:.1f} $\\\\pm$ {std:.1f}\"\n\ndef fmt_bca(bca: dict, pct: bool = False) -> str:\n    m = bca[\"mean\"]\n    lo, hi = bca[\"ci_lo\"], bca[\"ci_hi\"]\n    if pct:\n        return f\"{m*100:.1f}\\\\% [{lo*100:.1f}, {hi*100:.1f}]\"\n    return f\"{m:.1f} [{lo:.1f}, {hi:.1f}]\"\n\n\n# --- Console output ---\n\ndef print_per_seed_table(df: pd.DataFrame):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  PER-SEED RESULTS\")\n    print(\"=\" * 90)\n    cols = [\"condition\", \"seed\", \"PR\", \"H7_count\", \"H7_rate\", \"H1_count\",\n            \"H8_count\", \"genuine_count\", \"genuine_rate\", \"CI_count\", \"SNH_count\", \"SNH_rate\"]\n    fmt = df[cols].copy()\n    for c in [\"H7_rate\", \"genuine_rate\", \"SNH_rate\"]:\n        fmt[c] = fmt[c].apply(lambda v: f\"{v*100:.1f}%\")\n    print(fmt.to_string(index=False))\n\n\ndef print_condition_stats(cond_df: pd.DataFrame):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  CONDITION-LEVEL STATISTICS (mean +/- SD)\")\n    print(\"=\" * 90)\n    for _, row in cond_df.iterrows():\n        n = int(row['n_seeds'])\n        print(f\"\\n  {row['condition']} (n={n} seeds):\")\n        print(f\"    PR:           {row['PR_mean']:.1f} +/- {row['PR_std']:.1f}\")\n        print(f\"    H7 rate:      {row['H7_rate_mean']*100:.1f} +/- {row['H7_rate_std']*100:.1f}%\")\n        print(f\"    Genuine rate: {row['genuine_rate_mean']*100:.1f} +/- {row['genuine_rate_std']*100:.1f}%\")\n        print(f\"    S-NH rate:    {row['SNH_rate_mean']*100:.1f} +/- {row['SNH_rate_std']*100:.1f}%\")\n\n\ndef print_tests(fisher, perm, mw, bf, bca_h7, bca_gen):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  STATISTICAL TESTS\")\n    print(\"=\" * 90)\n\n    print(\"\\n  1. H7 Domination Fisher Exact Test (H7-dominated = H7% >= 50%)\")\n    print(f\"     ISR:    {fisher['ISR']['h7_dom']} dominated / {fisher['ISR']['n']} seeds\")\n    print(f\"     RANDOM: {fisher['RANDOM']['h7_dom']} dominated / {fisher['RANDOM']['n']} seeds\")\n    print(f\"     Contingency: {fisher['table']}\")\n    or_str = \"inf\" if np.isinf(fisher['odds_ratio']) else f\"{fisher['odds_ratio']:.4f}\"\n    print(f\"     OR = {or_str}, 95% CI = [{fisher['or_ci_lo']:.4f}, {fisher['or_ci_hi']:.4f}]\"\n          if not np.isnan(fisher['or_ci_lo']) else f\"     OR = {or_str}, 95% CI = N/A\")\n    print(f\"     p-value (one-sided, greater): {fisher['p_value']:.4f}\")\n\n    print(f\"\\n  2. Genuine Rate Permutation Test (n_perm={perm['n_perm']})\")\n    print(f\"     ISR mean:    {perm['isr_mean']*100:.2f}%\")\n    print(f\"     RANDOM mean: {perm['random_mean']*100:.2f}%\")\n    print(f\"     Diff: {perm['observed_diff']*100:.2f} pp, p = {perm['p_value']:.4f}\")\n\n    print(f\"\\n  3. H7 Rate Mann-Whitney U Test\")\n    print(f\"     ISR median:    {mw['isr_median']*100:.1f}%\")\n    print(f\"     RANDOM median: {mw['random_median']*100:.1f}%\")\n    print(f\"     U = {mw['U']:.1f}, p = {mw['p_value']:.4f}\")\n    print(f\"     Rank-biserial r = {mw['r_rank_biserial']:.4f}\")\n\n    print(f\"\\n  4. Bayes Factor (H7 Domination, Beta-Binomial)\")\n    print(f\"     ISR:    {bf['k_isr']}/{bf['n_isr']} dominated\")\n    print(f\"     RANDOM: {bf['k_rand']}/{bf['n_rand']} dominated\")\n    print(f\"     BF10 = {bf['bf10']:.4f} ({bf['interpretation']})\")\n\n    print(f\"\\n  5. BCa Bootstrap 95% CI (n_boot resamples)\")\n    for label, bca in [(\"H7 rate\", bca_h7), (\"Genuine rate\", bca_gen)]:\n        print(f\"     {label}:\")\n        for cond in [\"ISR\", \"RANDOM\"]:\n            b = bca[cond]\n            print(f\"       {cond}: {b['mean']*100:.1f}% [{b['ci_lo']*100:.1f}, {b['ci_hi']*100:.1f}]\"\n                  if not np.isnan(b['ci_lo']) else f\"       {cond}: {b['mean']*100:.1f}% [N/A]\")\n\n\n# --- Markdown generation (appendix-ready) ---\n\ndef generate_markdown(df: pd.DataFrame, cond_df: pd.DataFrame,\n                      fisher: dict, perm: dict, mw: dict,\n                      bf: dict, bca_h7: dict, bca_gen: dict) -> str:\n    L = []\n    L.append(\"## D134: ISR vs Random Statistical Analysis\\n\")\n\n    # Per-seed table\n    L.append(\"### Table A1: Per-Seed Hacking Taxonomy (4B Qwen3, 500 steps)\\n\")\n    L.append(\"| Condition | Seed | PR | H7 | H7\\\\% | H1 | H8 | Genuine | Gen\\\\% | CI | S-NH | S-NH\\\\% |\")\n    L.append(\"|:----------|-----:|---:|---:|-----:|---:|---:|--------:|------:|---:|-----:|-------:|\")\n    for _, r in df.iterrows():\n        L.append(\n            f\"| {r['condition']} | {r['seed']} | {int(r['PR'])} | {int(r['H7_count'])} | \"\n            f\"{r['H7_rate']*100:.1f} | {int(r['H1_count'])} | {int(r['H8_count'])} | \"\n            f\"{int(r['genuine_count'])} | {r['genuine_rate']*100:.1f} | {int(r['CI_count'])} | \"\n            f\"{int(r['SNH_count'])} | {r['SNH_rate']*100:.1f} |\"\n        )\n\n    # Condition summary with BCa CI\n    L.append(\"\\n### Table A2: Condition-Level Summary\\n\")\n    L.append(\"| Condition | $n$ | PR (mean$\\\\pm$SD) | H7\\\\% (mean$\\\\pm$SD) | H7\\\\% BCa 95\\\\% CI | Gen\\\\% (mean$\\\\pm$SD) | Gen\\\\% BCa 95\\\\% CI |\")\n    L.append(\"|:----------|----:|:------------------|:-------------------|:-----------------|:-------------------|:-----------------|\")\n    for _, r in cond_df.iterrows():\n        cond = r[\"condition\"]\n        h7_bca = bca_h7.get(cond, {})\n        gen_bca = bca_gen.get(cond, {})\n        h7_ci = f\"[{h7_bca['ci_lo']*100:.1f}, {h7_bca['ci_hi']*100:.1f}]\" if h7_bca and not np.isnan(h7_bca.get('ci_lo', np.nan)) else \"N/A\"\n        gen_ci = f\"[{gen_bca['ci_lo']*100:.1f}, {gen_bca['ci_hi']*100:.1f}]\" if gen_bca and not np.isnan(gen_bca.get('ci_lo', np.nan)) else \"N/A\"\n        L.append(\n            f\"| {cond} | {int(r['n_seeds'])} | \"\n            f\"{r['PR_mean']:.1f}$\\\\pm${r['PR_std']:.1f} | \"\n            f\"{r['H7_rate_mean']*100:.1f}$\\\\pm${r['H7_rate_std']*100:.1f} | \"\n            f\"{h7_ci} | \"\n            f\"{r['genuine_rate_mean']*100:.1f}$\\\\pm${r['genuine_rate_std']*100:.1f} | \"\n            f\"{gen_ci} |\"\n        )\n\n    # Statistical tests\n    if fisher and perm and mw and bf:\n        L.append(\"\\n### Statistical Tests\\n\")\n\n        # Fisher\n        or_str = \"$\\\\infty$\" if np.isinf(fisher['odds_ratio']) else f\"{fisher['odds_ratio']:.2f}\"\n        ci_lo = f\"{fisher['or_ci_lo']:.2f}\" if not np.isnan(fisher['or_ci_lo']) else \"0\"\n        ci_hi = \"$\\\\infty$\" if np.isinf(fisher.get('or_ci_hi', np.inf)) or np.isnan(fisher.get('or_ci_hi', np.nan)) else f\"{fisher['or_ci_hi']:.2f}\"\n        L.append(\"**1. H7 Domination Fisher Exact Test** (threshold: H7$\\\\geq$50\\\\% of proved)\")\n        L.append(f\"- ISR: {fisher['ISR']['h7_dom']}/{fisher['ISR']['n']} seeds H7-dominated; \"\n                 f\"Random: {fisher['RANDOM']['h7_dom']}/{fisher['RANDOM']['n']}\")\n        L.append(f\"- OR = {or_str}, 95\\\\% exact CI = [{ci_lo}, {ci_hi}], \"\n                 f\"$p$ = {fmt_p(fisher['p_value'])}\")\n        L.append(\"\")\n\n        # Permutation\n        L.append(f\"**2. Genuine Rate Permutation Test** ($n$ = {perm['n_perm']:,} permutations)\")\n        L.append(f\"- ISR mean: {perm['isr_mean']*100:.2f}\\\\%, Random mean: {perm['random_mean']*100:.2f}\\\\%\")\n        L.append(f\"- $\\\\Delta$ = {perm['observed_diff']*100:.2f} pp, $p$ = {fmt_p(perm['p_value'])}\")\n        L.append(\"\")\n\n        # Mann-Whitney\n        L.append(\"**3. H7 Rate Mann-Whitney $U$ Test**\")\n        L.append(f\"- ISR median: {mw['isr_median']*100:.1f}\\\\%, Random median: {mw['random_median']*100:.1f}\\\\%\")\n        L.append(f\"- $U$ = {mw['U']:.1f}, $p$ = {fmt_p(mw['p_value'])}, \"\n                 f\"rank-biserial $r$ = {mw['r_rank_biserial']:.3f}\")\n        L.append(\"\")\n\n        # Bayes Factor\n        L.append(\"**4. Bayes Factor** (Beta-Binomial conjugate, prior: Beta(1,1))\")\n        L.append(f\"- $BF_{{10}}$ = {bf['bf10']:.2f} ({bf['interpretation']})\")\n        L.append(f\"- ISR: {bf['k_isr']}/{bf['n_isr']} H7-dominated, \"\n                 f\"Random: {bf['k_rand']}/{bf['n_rand']}\")\n\n    return \"\\n\".join(L) + \"\\n\"\n\n\n# --- Main ---\n\ndef main():\n    args = parse_args()\n    data_dir = Path(args.data_dir)\n\n    if not data_dir.exists():\n        print(f\"ERROR: data directory {data_dir} does not exist\", file=sys.stderr)\n        sys.exit(1)\n\n    if args.prefix:\n        prefixes = [args.prefix]\n    elif args.prefixes:\n        prefixes = [p.strip() for p in args.prefixes.split(\",\")]\n    else:\n        prefixes = MODE_PREFIXES[args.mode]\n    print(f\"Mode: {args.mode} | Prefixes: {prefixes}\")\n\n    runs = discover_runs(data_dir, prefixes)\n    if not runs:\n        print(f\"ERROR: no runs found in {data_dir} with prefixes {prefixes}\", file=sys.stderr)\n        sys.exit(1)\n\n    isr_count = sum(1 for r in runs if r[\"condition\"] == \"ISR\")\n    rand_count = sum(1 for r in runs if r[\"condition\"] == \"RANDOM\")\n    print(f\"Found {len(runs)} runs: {isr_count} ISR, {rand_count} RANDOM\")\n    for r in runs:\n        print(f\"  {r['condition']:6s} s{r['seed']} <- {r['dir_name']}\")\n\n    df = build_table(runs)\n    print_per_seed_table(df)\n\n    cond_df = condition_stats(df)\n    print_condition_stats(cond_df)\n\n    if isr_count < 2 or rand_count < 2:\n        print(\"\\nWARNING: need >= 2 seeds per condition for statistical tests, skipping.\",\n              file=sys.stderr)\n        bca_h7 = bca_bootstrap_ci(df, \"H7_rate\", args.n_boot, args.seed)\n        bca_gen = bca_bootstrap_ci(df, \"genuine_rate\", args.n_boot, args.seed)\n        if args.output:\n            md = generate_markdown(df, cond_df, {}, {}, {}, {}, bca_h7, bca_gen)\n            Path(args.output).write_text(md)\n            print(f\"\\nMarkdown written to {args.output}\")\n        return\n\n    fisher = fisher_h7_domination(df)\n    perm = permutation_test_genuine(df, n_perm=args.n_perm, rng_seed=args.seed)\n    mw = mannwhitney_h7(df)\n    bf = bayes_factor_h7_domination(df)\n    bca_h7 = bca_bootstrap_ci(df, \"H7_rate\", args.n_boot, args.seed)\n    bca_gen = bca_bootstrap_ci(df, \"genuine_rate\", args.n_boot, args.seed)\n\n    print_tests(fisher, perm, mw, bf, bca_h7, bca_gen)\n\n    md = generate_markdown(df, cond_df, fisher, perm, mw, bf, bca_h7, bca_gen)\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  MARKDOWN OUTPUT (appendix-ready)\")\n    print(\"=\" * 90)\n    print(md)\n\n    if args.output:\n        Path(args.output).parent.mkdir(parents=True, exist_ok=True)\n        Path(args.output).write_text(md)\n        print(f\"Markdown written to {args.output}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 181,
        "oldLines": 6,
        "newStart": 181,
        "newLines": 7,
        "lines": [
          "         \"H1_count\": h1, \"H8_count\": h8,",
          "         \"genuine_count\": genuine, \"genuine_rate\": genuine_rate,",
          "         \"CI_count\": ci, \"SNH_count\": snh, \"SNH_rate\": snh_rate,",
          "+        \"ISR_star\": run.get(\"isr_star\"),",
          "     }",
          " ",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 24_

**Edit 3**: Add `mannwhitney_isr_star` function after `mannwhitney_h7`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "a3d612b5-aecd-482a-b2e6-55e777b03b4c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H5BbcdSDQJ2qAGdYWTvVx8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 591,
      "cache_read_input_tokens": 46276,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 591
      },
      "output_tokens": 7,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Edit · `toolu_01Rme11GZrjNtKdVVpP9ZaUg`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/scripts/d134_analysis.py",
  "old_string": "def bca_bootstrap_ci(df: pd.DataFrame, metric: str, n_boot: int = 10000,",
  "new_string": "def mannwhitney_isr_star(df: pd.DataFrame) -> dict | None:\n    isr = df[df[\"condition\"] == \"ISR\"][\"ISR_star\"].dropna().values.astype(float)\n    rand = df[df[\"condition\"] == \"RANDOM\"][\"ISR_star\"].dropna().values.astype(float)\n    if len(isr) < 2 or len(rand) < 2:\n        return None\n    n1, n2 = len(isr), len(rand)\n    u_stat, p_value = stats.mannwhitneyu(isr, rand, alternative=\"greater\")\n    r_rb = 2.0 * u_stat / (n1 * n2) - 1.0\n    return {\n        \"U\": float(u_stat),\n        \"p_value\": float(p_value),\n        \"r_rank_biserial\": float(r_rb),\n        \"isr_median\": float(np.median(isr)),\n        \"random_median\": float(np.median(rand)),\n        \"isr_mean\": float(np.mean(isr)),\n        \"random_mean\": float(np.mean(rand)),\n    }\n\n\ndef bca_bootstrap_ci(df: pd.DataFrame, metric: str, n_boot: int = 10000,"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "300f42f9-82ee-4f9c-9d81-e925de3f4b4c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H5BbcdSDQJ2qAGdYWTvVx8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 591,
      "cache_read_input_tokens": 46276,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 591
      },
      "output_tokens": 7,
      "service_tier": "standard",
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

_source line 26 · 2026-05-18T23:32:22.389Z_

<details><summary>↩ Tool result · `toolu_01Rme11GZrjNtKdVVpP9ZaUg`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/scripts/d134_analysis.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "65302617-b66a-4215-a9a9-22a79a754458",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/scripts/d134_analysis.py",
    "oldString": "def bca_bootstrap_ci(df: pd.DataFrame, metric: str, n_boot: int = 10000,",
    "newString": "def mannwhitney_isr_star(df: pd.DataFrame) -> dict | None:\n    isr = df[df[\"condition\"] == \"ISR\"][\"ISR_star\"].dropna().values.astype(float)\n    rand = df[df[\"condition\"] == \"RANDOM\"][\"ISR_star\"].dropna().values.astype(float)\n    if len(isr) < 2 or len(rand) < 2:\n        return None\n    n1, n2 = len(isr), len(rand)\n    u_stat, p_value = stats.mannwhitneyu(isr, rand, alternative=\"greater\")\n    r_rb = 2.0 * u_stat / (n1 * n2) - 1.0\n    return {\n        \"U\": float(u_stat),\n        \"p_value\": float(p_value),\n        \"r_rank_biserial\": float(r_rb),\n        \"isr_median\": float(np.median(isr)),\n        \"random_median\": float(np.median(rand)),\n        \"isr_mean\": float(np.mean(isr)),\n        \"random_mean\": float(np.mean(rand)),\n    }\n\n\ndef bca_bootstrap_ci(df: pd.DataFrame, metric: str, n_boot: int = 10000,",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"D134 experiment analysis: multi-seed ISR vs Random, 4B GRPO training.\nReads taxonomy data from classify.json, taxonomy.json, or top-level taxonomy files.\nComputes summary stats, statistical tests (Fisher, Mann-Whitney, permutation, Bayes Factor),\nand BCa bootstrap CIs. Outputs appendix-ready markdown.\n\"\"\"\n\nimport argparse\nimport json\nimport re\nimport sys\nfrom pathlib import Path\n\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\nfrom scipy.special import betaln\n\nCONDITION_MAP = [\n    (\"d134_4b_isr\", \"ISR\"),\n    (\"d134_4b_random\", \"RANDOM\"),\n    (\"plan002_additive\", \"ISR\"),\n    (\"plan018_additive_random\", \"RANDOM\"),\n    (\"plan018_random\", \"RANDOM\"),\n]\n\nMODE_PREFIXES = {\n    \"d134_only\": [\"d134_4b\"],\n    \"all\": [\"d134_4b\", \"plan002_additive_b01\", \"plan018_additive_random_b01\", \"plan018_random\"],\n}\n\n\ndef parse_args():\n    p = argparse.ArgumentParser(description=\"D134 multi-seed analysis and statistical tests\")\n    p.add_argument(\"--data_dir\", type=str, default=\"/root/autodl-tmp/outputs\",\n                   help=\"Directory containing experiment outputs\")\n    p.add_argument(\"--mode\", type=str, default=\"d134_only\", choices=list(MODE_PREFIXES),\n                   help=\"d134_only = matched 5+5 design (default); all = include original seeds\")\n    p.add_argument(\"--prefix\", type=str, default=None,\n                   help=\"(Legacy) Single prefix filter; overrides mode/prefixes\")\n    p.add_argument(\"--prefixes\", type=str, default=None,\n                   help=\"Comma-separated prefixes; overrides --mode\")\n    p.add_argument(\"--output\", type=str, default=None,\n                   help=\"Write markdown summary to this file\")\n    p.add_argument(\"--n_perm\", type=int, default=10000,\n                   help=\"Number of permutations for permutation test\")\n    p.add_argument(\"--n_boot\", type=int, default=10000,\n                   help=\"Number of bootstrap resamples for BCa CI\")\n    p.add_argument(\"--seed\", type=int, default=42,\n                   help=\"Random seed for permutation/bootstrap\")\n    return p.parse_args()\n\n\n# --- Data loading ---\n\ndef match_condition(name: str) -> str | None:\n    best_prefix = \"\"\n    best_cond = None\n    for prefix, cond in CONDITION_MAP:\n        if name.startswith(prefix) and len(prefix) > len(best_prefix):\n            best_prefix = prefix\n            best_cond = cond\n    return best_cond\n\n\ndef extract_seed(name: str) -> int | None:\n    m = re.search(r'_s(\\d+)', name)\n    return int(m.group(1)) if m else None\n\n\ndef load_eval_results(path: Path) -> dict | None:\n    if not path.exists():\n        return None\n    with open(path) as f:\n        data = json.load(f)\n    if \"eval_results\" in data:\n        return data[\"eval_results\"]\n    return data\n\n\ndef load_taxonomy_unified(path: Path) -> dict | None:\n    with open(path) as f:\n        raw = json.load(f)\n    t = raw.get(\"taxonomy\", {})\n    proved = t.get(\"proved\", 0)\n    if proved == 0:\n        return None\n    h7 = t.get(\"H7\", 0)\n    h1 = t.get(\"H1_exact\", 0)\n    h8 = t.get(\"H8\", 0)\n    genuine = t.get(\"genuine\", 0)\n    return {\n        \"n_total\": 100, \"n_proved\": proved,\n        \"h7_total_count\": h7, \"h7_total_rate\": h7 / proved,\n        \"h1_strict_count\": h1, \"h8_conjunction_collapse_count\": h8,\n        \"genuine_count\": genuine, \"genuine_rate\": genuine / proved,\n        \"content_independent_count\": 0,\n    }\n\n\ndef load_taxonomy_verification(path: Path) -> dict | None:\n    with open(path) as f:\n        raw = json.load(f)\n    proved = raw.get(\"proved\", 0)\n    if proved == 0:\n        return None\n    tax = raw.get(\"taxonomy\", {})\n    h7 = tax.get(\"h7\", {}).get(\"count\", 0)\n    h1 = tax.get(\"h1_exact\", {}).get(\"count\", 0)\n    h8 = tax.get(\"h8\", {}).get(\"count\", 0)\n    genuine = tax.get(\"genuine\", {}).get(\"count\", 0)\n    return {\n        \"n_total\": raw.get(\"total\", 100), \"n_proved\": proved,\n        \"h7_total_count\": h7, \"h7_total_rate\": h7 / proved,\n        \"h1_strict_count\": h1, \"h8_conjunction_collapse_count\": h8,\n        \"genuine_count\": genuine, \"genuine_rate\": genuine / proved,\n        \"content_independent_count\": 0,\n    }\n\n\ndef discover_runs(data_dir: Path, prefixes: list[str]) -> list[dict]:\n    runs = []\n    seen = set()\n    for entry in sorted(data_dir.iterdir()):\n        name = entry.name\n        if not any(name.startswith(p) for p in prefixes):\n            continue\n        cond = match_condition(name)\n        seed_val = extract_seed(name)\n        if cond is None or seed_val is None:\n            continue\n        key = (cond, seed_val)\n        if key in seen:\n            continue\n        data = None\n        if entry.is_dir():\n            for fname in [\"classify.json\", \"taxonomy.json\"]:\n                data = load_eval_results(entry / fname)\n                if data is not None:\n                    break\n            if data is None:\n                continue\n        elif entry.is_file():\n            if name.endswith(\"_taxonomy_unified.json\"):\n                data = load_taxonomy_unified(entry)\n            elif name.endswith(\"_taxonomy_verification.json\"):\n                data = load_taxonomy_verification(entry)\n            if data is None:\n                continue\n        else:\n            continue\n        seen.add(key)\n        isr_star = None\n        if entry.is_dir():\n            eval_path = entry / \"eval_results.json\"\n            if eval_path.exists():\n                with open(eval_path) as ef:\n                    eval_raw = json.load(ef)\n                isr_star = eval_raw.get(\"summary\", {}).get(\"proved_only_mean_isr\")\n        runs.append({\"dir_name\": name, \"seed\": seed_val, \"condition\": cond,\n                      \"data\": data, \"isr_star\": isr_star})\n    return runs\n\n\ndef compute_row(run: dict) -> dict:\n    d = run[\"data\"]\n    n_proved = d.get(\"n_proved\", 0)\n    n_total = d.get(\"n_total\", 100)\n    h7 = d.get(\"h7_total_count\", 0)\n    h7_rate = d.get(\"h7_total_rate\", h7 / n_proved if n_proved > 0 else 0.0)\n    h1 = d.get(\"h1_strict_count\", 0)\n    h8 = d.get(\"h8_conjunction_collapse_count\", 0)\n    genuine = d.get(\"genuine_count\", 0)\n    genuine_rate = d.get(\"genuine_rate\", genuine / n_proved if n_proved > 0 else 0.0)\n    ci = d.get(\"content_independent_count\", 0)\n    snh = max(genuine - ci, 0)\n    snh_rate = snh / n_proved if n_proved > 0 else 0.0\n    return {\n        \"seed\": run[\"seed\"], \"condition\": run[\"condition\"], \"n_total\": n_total,\n        \"PR\": n_proved, \"H7_count\": h7, \"H7_rate\": h7_rate,\n        \"H1_count\": h1, \"H8_count\": h8,\n        \"genuine_count\": genuine, \"genuine_rate\": genuine_rate,\n        \"CI_count\": ci, \"SNH_count\": snh, \"SNH_rate\": snh_rate,\n        \"ISR_star\": run.get(\"isr_star\"),\n    }\n\n\ndef build_table(runs: list[dict]) -> pd.DataFrame:\n    rows = [compute_row(r) for r in runs]\n    df = pd.DataFrame(rows)\n    df = df.sort_values([\"condition\", \"seed\"]).reset_index(drop=True)\n    return df\n\n\n# --- Statistical tests ---\n\ndef fisher_h7_domination(df: pd.DataFrame) -> dict:\n    results = {}\n    for cond in [\"ISR\", \"RANDOM\"]:\n        sub = df[df[\"condition\"] == cond]\n        results[cond] = {\n            \"n\": len(sub),\n            \"h7_dom\": int((sub[\"H7_rate\"] >= 0.5).sum()),\n            \"not_h7_dom\": int((sub[\"H7_rate\"] < 0.5).sum()),\n        }\n    table = np.array([\n        [results[\"ISR\"][\"h7_dom\"], results[\"ISR\"][\"not_h7_dom\"]],\n        [results[\"RANDOM\"][\"h7_dom\"], results[\"RANDOM\"][\"not_h7_dom\"]],\n    ])\n    odds_ratio, p_value = stats.fisher_exact(table, alternative=\"greater\")\n\n    # 95% exact CI via scipy.stats.contingency\n    or_ci_lo, or_ci_hi = np.nan, np.nan\n    try:\n        ct = stats.contingency.odds_ratio(table)\n        ci = ct.confidence_interval(confidence_level=0.95)\n        or_ci_lo, or_ci_hi = ci.low, ci.high\n    except Exception:\n        pass\n\n    return {\n        \"table\": table.tolist(),\n        \"ISR\": results[\"ISR\"],\n        \"RANDOM\": results[\"RANDOM\"],\n        \"odds_ratio\": odds_ratio,\n        \"or_ci_lo\": or_ci_lo,\n        \"or_ci_hi\": or_ci_hi,\n        \"p_value\": p_value,\n    }\n\n\ndef permutation_test_genuine(df: pd.DataFrame, n_perm: int = 10000,\n                              rng_seed: int = 42) -> dict:\n    isr = df[df[\"condition\"] == \"ISR\"][\"genuine_rate\"].values\n    rand = df[df[\"condition\"] == \"RANDOM\"][\"genuine_rate\"].values\n    observed = isr.mean() - rand.mean()\n    pooled = np.concatenate([isr, rand])\n    n_isr = len(isr)\n    rng = np.random.default_rng(rng_seed)\n    count = 0\n    for _ in range(n_perm):\n        perm = rng.permutation(pooled)\n        if perm[:n_isr].mean() - perm[n_isr:].mean() >= observed:\n            count += 1\n    return {\n        \"observed_diff\": float(observed),\n        \"p_value\": count / n_perm,\n        \"n_perm\": n_perm,\n        \"isr_mean\": float(isr.mean()),\n        \"random_mean\": float(rand.mean()),\n    }\n\n\ndef mannwhitney_h7(df: pd.DataFrame) -> dict:\n    isr = df[df[\"condition\"] == \"ISR\"][\"H7_rate\"].values\n    rand = df[df[\"condition\"] == \"RANDOM\"][\"H7_rate\"].values\n    n1, n2 = len(isr), len(rand)\n    u_stat, p_value = stats.mannwhitneyu(isr, rand, alternative=\"greater\")\n    r_rb = 2.0 * u_stat / (n1 * n2) - 1.0 if n1 * n2 > 0 else np.nan\n    return {\n        \"U\": float(u_stat),\n        \"p_value\": float(p_value),\n        \"r_rank_biserial\": float(r_rb),\n        \"isr_median\": float(np.median(isr)),\n        \"random_median\": float(np.median(rand)),\n    }\n\n\ndef bca_bootstrap_ci(df: pd.DataFrame, metric: str, n_boot: int = 10000,\n                      rng_seed: int = 42) -> dict:\n    \"\"\"BCa 95% CI for per-condition means of a metric.\"\"\"\n    result = {}\n    for cond in [\"ISR\", \"RANDOM\"]:\n        vals = df[df[\"condition\"] == cond][metric].values\n        if len(vals) < 2:\n            result[cond] = {\"mean\": float(vals.mean()) if len(vals) else np.nan,\n                            \"ci_lo\": np.nan, \"ci_hi\": np.nan}\n            continue\n        res = stats.bootstrap(\n            (vals,), np.mean, n_resamples=n_boot,\n            confidence_level=0.95, method=\"BCa\",\n            random_state=np.random.default_rng(rng_seed),\n        )\n        result[cond] = {\n            \"mean\": float(vals.mean()),\n            \"ci_lo\": float(res.confidence_interval.low),\n            \"ci_hi\": float(res.confidence_interval.high),\n        }\n    return result\n\n\ndef bayes_factor_h7_domination(df: pd.DataFrame) -> dict:\n    \"\"\"BF10 for H7-domination rate difference (beta-binomial conjugate).\n    H0: ISR and Random share same domination rate.\n    H1: independent rates. Prior: Beta(1,1) on each.\n    \"\"\"\n    isr_sub = df[df[\"condition\"] == \"ISR\"]\n    rand_sub = df[df[\"condition\"] == \"RANDOM\"]\n    k_isr = int((isr_sub[\"H7_rate\"] >= 0.5).sum())\n    n_isr = len(isr_sub)\n    k_rand = int((rand_sub[\"H7_rate\"] >= 0.5).sum())\n    n_rand = len(rand_sub)\n    k_total = k_isr + k_rand\n    n_total = n_isr + n_rand\n\n    # log marginal under H0 (shared rate)\n    log_m_h0 = betaln(1 + k_total, 1 + n_total - k_total) - betaln(1, 1)\n    # log marginal under H1 (independent rates)\n    log_m_h1 = (betaln(1 + k_isr, 1 + n_isr - k_isr) - betaln(1, 1)\n                + betaln(1 + k_rand, 1 + n_rand - k_rand) - betaln(1, 1))\n    log_bf10 = log_m_h1 - log_m_h0\n    bf10 = float(np.exp(log_bf10))\n\n    return {\n        \"k_isr\": k_isr, \"n_isr\": n_isr,\n        \"k_rand\": k_rand, \"n_rand\": n_rand,\n        \"bf10\": bf10,\n        \"log_bf10\": float(log_bf10),\n        \"interpretation\": _interpret_bf(bf10),\n    }\n\n\ndef _interpret_bf(bf: float) -> str:\n    if bf > 100:\n        return \"extreme evidence for H1\"\n    if bf > 30:\n        return \"very strong evidence for H1\"\n    if bf > 10:\n        return \"strong evidence for H1\"\n    if bf > 3:\n        return \"moderate evidence for H1\"\n    if bf > 1:\n        return \"anecdotal evidence for H1\"\n    if bf > 1/3:\n        return \"anecdotal evidence (inconclusive)\"\n    if bf > 1/10:\n        return \"moderate evidence for H0\"\n    return \"strong evidence for H0\"\n\n\ndef condition_stats(df: pd.DataFrame) -> pd.DataFrame:\n    metrics = [\"PR\", \"H7_rate\", \"genuine_rate\", \"SNH_rate\"]\n    rows = []\n    for cond in [\"ISR\", \"RANDOM\"]:\n        sub = df[df[\"condition\"] == cond]\n        row = {\"condition\": cond, \"n_seeds\": len(sub)}\n        for m in metrics:\n            vals = sub[m].values\n            row[f\"{m}_mean\"] = vals.mean()\n            row[f\"{m}_std\"] = vals.std(ddof=1) if len(vals) > 1 else 0.0\n        rows.append(row)\n    return pd.DataFrame(rows)\n\n\n# --- Formatting ---\n\ndef fmt_pct(val: float) -> str:\n    return f\"{val*100:.1f}\\\\%\"\n\ndef fmt_or(val: float) -> str:\n    return \"$\\\\infty$\" if np.isinf(val) else f\"{val:.2f}\"\n\ndef fmt_ci(lo: float, hi: float) -> str:\n    lo_s = f\"{lo:.2f}\" if not np.isnan(lo) else \"0\"\n    hi_s = \"$\\\\infty$\" if np.isinf(hi) or np.isnan(hi) else f\"{hi:.2f}\"\n    return f\"[{lo_s}, {hi_s}]\"\n\ndef fmt_p(p: float) -> str:\n    if p < 0.001:\n        return \"$<$0.001\"\n    return f\"{p:.3f}\"\n\ndef fmt_mean_std(mean: float, std: float, pct: bool = False) -> str:\n    if pct:\n        return f\"{mean*100:.1f} $\\\\pm$ {std*100:.1f}\\\\%\"\n    return f\"{mean:.1f} $\\\\pm$ {std:.1f}\"\n\ndef fmt_bca(bca: dict, pct: bool = False) -> str:\n    m = bca[\"mean\"]\n    lo, hi = bca[\"ci_lo\"], bca[\"ci_hi\"]\n    if pct:\n        return f\"{m*100:.1f}\\\\% [{lo*100:.1f}, {hi*100:.1f}]\"\n    return f\"{m:.1f} [{lo:.1f}, {hi:.1f}]\"\n\n\n# --- Console output ---\n\ndef print_per_seed_table(df: pd.DataFrame):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  PER-SEED RESULTS\")\n    print(\"=\" * 90)\n    cols = [\"condition\", \"seed\", \"PR\", \"H7_count\", \"H7_rate\", \"H1_count\",\n            \"H8_count\", \"genuine_count\", \"genuine_rate\", \"CI_count\", \"SNH_count\", \"SNH_rate\"]\n    fmt = df[cols].copy()\n    for c in [\"H7_rate\", \"genuine_rate\", \"SNH_rate\"]:\n        fmt[c] = fmt[c].apply(lambda v: f\"{v*100:.1f}%\")\n    print(fmt.to_string(index=False))\n\n\ndef print_condition_stats(cond_df: pd.DataFrame):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  CONDITION-LEVEL STATISTICS (mean +/- SD)\")\n    print(\"=\" * 90)\n    for _, row in cond_df.iterrows():\n        n = int(row['n_seeds'])\n        print(f\"\\n  {row['condition']} (n={n} seeds):\")\n        print(f\"    PR:           {row['PR_mean']:.1f} +/- {row['PR_std']:.1f}\")\n        print(f\"    H7 rate:      {row['H7_rate_mean']*100:.1f} +/- {row['H7_rate_std']*100:.1f}%\")\n        print(f\"    Genuine rate: {row['genuine_rate_mean']*100:.1f} +/- {row['genuine_rate_std']*100:.1f}%\")\n        print(f\"    S-NH rate:    {row['SNH_rate_mean']*100:.1f} +/- {row['SNH_rate_std']*100:.1f}%\")\n\n\ndef print_tests(fisher, perm, mw, bf, bca_h7, bca_gen):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  STATISTICAL TESTS\")\n    print(\"=\" * 90)\n\n    print(\"\\n  1. H7 Domination Fisher Exact Test (H7-dominated = H7% >= 50%)\")\n    print(f\"     ISR:    {fisher['ISR']['h7_dom']} dominated / {fisher['ISR']['n']} seeds\")\n    print(f\"     RANDOM: {fisher['RANDOM']['h7_dom']} dominated / {fisher['RANDOM']['n']} seeds\")\n    print(f\"     Contingency: {fisher['table']}\")\n    or_str = \"inf\" if np.isinf(fisher['odds_ratio']) else f\"{fisher['odds_ratio']:.4f}\"\n    print(f\"     OR = {or_str}, 95% CI = [{fisher['or_ci_lo']:.4f}, {fisher['or_ci_hi']:.4f}]\"\n          if not np.isnan(fisher['or_ci_lo']) else f\"     OR = {or_str}, 95% CI = N/A\")\n    print(f\"     p-value (one-sided, greater): {fisher['p_value']:.4f}\")\n\n    print(f\"\\n  2. Genuine Rate Permutation Test (n_perm={perm['n_perm']})\")\n    print(f\"     ISR mean:    {perm['isr_mean']*100:.2f}%\")\n    print(f\"     RANDOM mean: {perm['random_mean']*100:.2f}%\")\n    print(f\"     Diff: {perm['observed_diff']*100:.2f} pp, p = {perm['p_value']:.4f}\")\n\n    print(f\"\\n  3. H7 Rate Mann-Whitney U Test\")\n    print(f\"     ISR median:    {mw['isr_median']*100:.1f}%\")\n    print(f\"     RANDOM median: {mw['random_median']*100:.1f}%\")\n    print(f\"     U = {mw['U']:.1f}, p = {mw['p_value']:.4f}\")\n    print(f\"     Rank-biserial r = {mw['r_rank_biserial']:.4f}\")\n\n    print(f\"\\n  4. Bayes Factor (H7 Domination, Beta-Binomial)\")\n    print(f\"     ISR:    {bf['k_isr']}/{bf['n_isr']} dominated\")\n    print(f\"     RANDOM: {bf['k_rand']}/{bf['n_rand']} dominated\")\n    print(f\"     BF10 = {bf['bf10']:.4f} ({bf['interpretation']})\")\n\n    print(f\"\\n  5. BCa Bootstrap 95% CI (n_boot resamples)\")\n    for label, bca in [(\"H7 rate\", bca_h7), (\"Genuine rate\", bca_gen)]:\n        print(f\"     {label}:\")\n        for cond in [\"ISR\", \"RANDOM\"]:\n            b = bca[cond]\n            print(f\"       {cond}: {b['mean']*100:.1f}% [{b['ci_lo']*100:.1f}, {b['ci_hi']*100:.1f}]\"\n                  if not np.isnan(b['ci_lo']) else f\"       {cond}: {b['mean']*100:.1f}% [N/A]\")\n\n\n# --- Markdown generation (appendix-ready) ---\n\ndef generate_markdown(df: pd.DataFrame, cond_df: pd.DataFrame,\n                      fisher: dict, perm: dict, mw: dict,\n                      bf: dict, bca_h7: dict, bca_gen: dict) -> str:\n    L = []\n    L.append(\"## D134: ISR vs Random Statistical Analysis\\n\")\n\n    # Per-seed table\n    L.append(\"### Table A1: Per-Seed Hacking Taxonomy (4B Qwen3, 500 steps)\\n\")\n    L.append(\"| Condition | Seed | PR | H7 | H7\\\\% | H1 | H8 | Genuine | Gen\\\\% | CI | S-NH | S-NH\\\\% |\")\n    L.append(\"|:----------|-----:|---:|---:|-----:|---:|---:|--------:|------:|---:|-----:|-------:|\")\n    for _, r in df.iterrows():\n        L.append(\n            f\"| {r['condition']} | {r['seed']} | {int(r['PR'])} | {int(r['H7_count'])} | \"\n            f\"{r['H7_rate']*100:.1f} | {int(r['H1_count'])} | {int(r['H8_count'])} | \"\n            f\"{int(r['genuine_count'])} | {r['genuine_rate']*100:.1f} | {int(r['CI_count'])} | \"\n            f\"{int(r['SNH_count'])} | {r['SNH_rate']*100:.1f} |\"\n        )\n\n    # Condition summary with BCa CI\n    L.append(\"\\n### Table A2: Condition-Level Summary\\n\")\n    L.append(\"| Condition | $n$ | PR (mean$\\\\pm$SD) | H7\\\\% (mean$\\\\pm$SD) | H7\\\\% BCa 95\\\\% CI | Gen\\\\% (mean$\\\\pm$SD) | Gen\\\\% BCa 95\\\\% CI |\")\n    L.append(\"|:----------|----:|:------------------|:-------------------|:-----------------|:-------------------|:-----------------|\")\n    for _, r in cond_df.iterrows():\n        cond = r[\"condition\"]\n        h7_bca = bca_h7.get(cond, {})\n        gen_bca = bca_gen.get(cond, {})\n        h7_ci = f\"[{h7_bca['ci_lo']*100:.1f}, {h7_bca['ci_hi']*100:.1f}]\" if h7_bca and not np.isnan(h7_bca.get('ci_lo', np.nan)) else \"N/A\"\n        gen_ci = f\"[{gen_bca['ci_lo']*100:.1f}, {gen_bca['ci_hi']*100:.1f}]\" if gen_bca and not np.isnan(gen_bca.get('ci_lo', np.nan)) else \"N/A\"\n        L.append(\n            f\"| {cond} | {int(r['n_seeds'])} | \"\n            f\"{r['PR_mean']:.1f}$\\\\pm${r['PR_std']:.1f} | \"\n            f\"{r['H7_rate_mean']*100:.1f}$\\\\pm${r['H7_rate_std']*100:.1f} | \"\n            f\"{h7_ci} | \"\n            f\"{r['genuine_rate_mean']*100:.1f}$\\\\pm${r['genuine_rate_std']*100:.1f} | \"\n            f\"{gen_ci} |\"\n        )\n\n    # Statistical tests\n    if fisher and perm and mw and bf:\n        L.append(\"\\n### Statistical Tests\\n\")\n\n        # Fisher\n        or_str = \"$\\\\infty$\" if np.isinf(fisher['odds_ratio']) else f\"{fisher['odds_ratio']:.2f}\"\n        ci_lo = f\"{fisher['or_ci_lo']:.2f}\" if not np.isnan(fisher['or_ci_lo']) else \"0\"\n        ci_hi = \"$\\\\infty$\" if np.isinf(fisher.get('or_ci_hi', np.inf)) or np.isnan(fisher.get('or_ci_hi', np.nan)) else f\"{fisher['or_ci_hi']:.2f}\"\n        L.append(\"**1. H7 Domination Fisher Exact Test** (threshold: H7$\\\\geq$50\\\\% of proved)\")\n        L.append(f\"- ISR: {fisher['ISR']['h7_dom']}/{fisher['ISR']['n']} seeds H7-dominated; \"\n                 f\"Random: {fisher['RANDOM']['h7_dom']}/{fisher['RANDOM']['n']}\")\n        L.append(f\"- OR = {or_str}, 95\\\\% exact CI = [{ci_lo}, {ci_hi}], \"\n                 f\"$p$ = {fmt_p(fisher['p_value'])}\")\n        L.append(\"\")\n\n        # Permutation\n        L.append(f\"**2. Genuine Rate Permutation Test** ($n$ = {perm['n_perm']:,} permutations)\")\n        L.append(f\"- ISR mean: {perm['isr_mean']*100:.2f}\\\\%, Random mean: {perm['random_mean']*100:.2f}\\\\%\")\n        L.append(f\"- $\\\\Delta$ = {perm['observed_diff']*100:.2f} pp, $p$ = {fmt_p(perm['p_value'])}\")\n        L.append(\"\")\n\n        # Mann-Whitney\n        L.append(\"**3. H7 Rate Mann-Whitney $U$ Test**\")\n        L.append(f\"- ISR median: {mw['isr_median']*100:.1f}\\\\%, Random median: {mw['random_median']*100:.1f}\\\\%\")\n        L.append(f\"- $U$ = {mw['U']:.1f}, $p$ = {fmt_p(mw['p_value'])}, \"\n                 f\"rank-biserial $r$ = {mw['r_rank_biserial']:.3f}\")\n        L.append(\"\")\n\n        # Bayes Factor\n        L.append(\"**4. Bayes Factor** (Beta-Binomial conjugate, prior: Beta(1,1))\")\n        L.append(f\"- $BF_{{10}}$ = {bf['bf10']:.2f} ({bf['interpretation']})\")\n        L.append(f\"- ISR: {bf['k_isr']}/{bf['n_isr']} H7-dominated, \"\n                 f\"Random: {bf['k_rand']}/{bf['n_rand']}\")\n\n    return \"\\n\".join(L) + \"\\n\"\n\n\n# --- Main ---\n\ndef main():\n    args = parse_args()\n    data_dir = Path(args.data_dir)\n\n    if not data_dir.exists():\n        print(f\"ERROR: data directory {data_dir} does not exist\", file=sys.stderr)\n        sys.exit(1)\n\n    if args.prefix:\n        prefixes = [args.prefix]\n    elif args.prefixes:\n        prefixes = [p.strip() for p in args.prefixes.split(\",\")]\n    else:\n        prefixes = MODE_PREFIXES[args.mode]\n    print(f\"Mode: {args.mode} | Prefixes: {prefixes}\")\n\n    runs = discover_runs(data_dir, prefixes)\n    if not runs:\n        print(f\"ERROR: no runs found in {data_dir} with prefixes {prefixes}\", file=sys.stderr)\n        sys.exit(1)\n\n    isr_count = sum(1 for r in runs if r[\"condition\"] == \"ISR\")\n    rand_count = sum(1 for r in runs if r[\"condition\"] == \"RANDOM\")\n    print(f\"Found {len(runs)} runs: {isr_count} ISR, {rand_count} RANDOM\")\n    for r in runs:\n        print(f\"  {r['condition']:6s} s{r['seed']} <- {r['dir_name']}\")\n\n    df = build_table(runs)\n    print_per_seed_table(df)\n\n    cond_df = condition_stats(df)\n    print_condition_stats(cond_df)\n\n    if isr_count < 2 or rand_count < 2:\n        print(\"\\nWARNING: need >= 2 seeds per condition for statistical tests, skipping.\",\n              file=sys.stderr)\n        bca_h7 = bca_bootstrap_ci(df, \"H7_rate\", args.n_boot, args.seed)\n        bca_gen = bca_bootstrap_ci(df, \"genuine_rate\", args.n_boot, args.seed)\n        if args.output:\n            md = generate_markdown(df, cond_df, {}, {}, {}, {}, bca_h7, bca_gen)\n            Path(args.output).write_text(md)\n            print(f\"\\nMarkdown written to {args.output}\")\n        return\n\n    fisher = fisher_h7_domination(df)\n    perm = permutation_test_genuine(df, n_perm=args.n_perm, rng_seed=args.seed)\n    mw = mannwhitney_h7(df)\n    bf = bayes_factor_h7_domination(df)\n    bca_h7 = bca_bootstrap_ci(df, \"H7_rate\", args.n_boot, args.seed)\n    bca_gen = bca_bootstrap_ci(df, \"genuine_rate\", args.n_boot, args.seed)\n\n    print_tests(fisher, perm, mw, bf, bca_h7, bca_gen)\n\n    md = generate_markdown(df, cond_df, fisher, perm, mw, bf, bca_h7, bca_gen)\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  MARKDOWN OUTPUT (appendix-ready)\")\n    print(\"=\" * 90)\n    print(md)\n\n    if args.output:\n        Path(args.output).parent.mkdir(parents=True, exist_ok=True)\n        Path(args.output).write_text(md)\n        print(f\"Markdown written to {args.output}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 266,
        "oldLines": 6,
        "newStart": 266,
        "newLines": 25,
        "lines": [
          "     }",
          " ",
          " ",
          "+def mannwhitney_isr_star(df: pd.DataFrame) -> dict | None:",
          "+    isr = df[df[\"condition\"] == \"ISR\"][\"ISR_star\"].dropna().values.astype(float)",
          "+    rand = df[df[\"condition\"] == \"RANDOM\"][\"ISR_star\"].dropna().values.astype(float)",
          "+    if len(isr) < 2 or len(rand) < 2:",
          "+        return None",
          "+    n1, n2 = len(isr), len(rand)",
          "+    u_stat, p_value = stats.mannwhitneyu(isr, rand, alternative=\"greater\")",
          "+    r_rb = 2.0 * u_stat / (n1 * n2) - 1.0",
          "+    return {",
          "+        \"U\": float(u_stat),",
          "+        \"p_value\": float(p_value),",
          "+        \"r_rank_biserial\": float(r_rb),",
          "+        \"isr_median\": float(np.median(isr)),",
          "+        \"random_median\": float(np.median(rand)),",
          "+        \"isr_mean\": float(np.mean(isr)),",
          "+        \"random_mean\": float(np.mean(rand)),",
          "+    }",
          "+",
          "+",
          " def bca_bootstrap_ci(df: pd.DataFrame, metric: str, n_boot: int = 10000,",
          "                       rng_seed: int = 42) -> dict:",
          "     \"\"\"BCa 95% CI for per-condition means of a metric.\"\"\""
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 27_

**Edit 4**: Add ISR_star to `condition_stats`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "dda3d33e-f2a2-4412-83d8-0acee601c434",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0157iRuDS4fgkagNJDf9PcmJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 579,
      "cache_read_input_tokens": 46867,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 579
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

<details open><summary>🔧 Tool call — Edit · `toolu_01Xeedzq4ExXsA7GegnrWDYy`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/scripts/d134_analysis.py",
  "old_string": "def condition_stats(df: pd.DataFrame) -> pd.DataFrame:\n    metrics = [\"PR\", \"H7_rate\", \"genuine_rate\", \"SNH_rate\"]\n    rows = []\n    for cond in [\"ISR\", \"RANDOM\"]:\n        sub = df[df[\"condition\"] == cond]\n        row = {\"condition\": cond, \"n_seeds\": len(sub)}\n        for m in metrics:\n            vals = sub[m].values\n            row[f\"{m}_mean\"] = vals.mean()\n            row[f\"{m}_std\"] = vals.std(ddof=1) if len(vals) > 1 else 0.0\n        rows.append(row)\n    return pd.DataFrame(rows)",
  "new_string": "def condition_stats(df: pd.DataFrame) -> pd.DataFrame:\n    metrics = [\"PR\", \"H7_rate\", \"genuine_rate\", \"SNH_rate\"]\n    rows = []\n    for cond in [\"ISR\", \"RANDOM\"]:\n        sub = df[df[\"condition\"] == cond]\n        row = {\"condition\": cond, \"n_seeds\": len(sub)}\n        for m in metrics:\n            vals = sub[m].values\n            row[f\"{m}_mean\"] = vals.mean()\n            row[f\"{m}_std\"] = vals.std(ddof=1) if len(vals) > 1 else 0.0\n        isr_vals = sub[\"ISR_star\"].dropna().values.astype(float)\n        row[\"ISR_star_mean\"] = isr_vals.mean() if len(isr_vals) else np.nan\n        row[\"ISR_star_std\"] = isr_vals.std(ddof=1) if len(isr_vals) > 1 else 0.0\n        rows.append(row)\n    return pd.DataFrame(rows)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "e9e957cd-8f1e-4374-9d65-65fe0cf799a0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0157iRuDS4fgkagNJDf9PcmJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 579,
      "cache_read_input_tokens": 46867,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 579
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

_source line 29 · 2026-05-18T23:32:30.173Z_

<details><summary>↩ Tool result · `toolu_01Xeedzq4ExXsA7GegnrWDYy`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/scripts/d134_analysis.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "100fe1f4-89a6-4678-9f7e-5d27d70ff91f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/scripts/d134_analysis.py",
    "oldString": "def condition_stats(df: pd.DataFrame) -> pd.DataFrame:\n    metrics = [\"PR\", \"H7_rate\", \"genuine_rate\", \"SNH_rate\"]\n    rows = []\n    for cond in [\"ISR\", \"RANDOM\"]:\n        sub = df[df[\"condition\"] == cond]\n        row = {\"condition\": cond, \"n_seeds\": len(sub)}\n        for m in metrics:\n            vals = sub[m].values\n            row[f\"{m}_mean\"] = vals.mean()\n            row[f\"{m}_std\"] = vals.std(ddof=1) if len(vals) > 1 else 0.0\n        rows.append(row)\n    return pd.DataFrame(rows)",
    "newString": "def condition_stats(df: pd.DataFrame) -> pd.DataFrame:\n    metrics = [\"PR\", \"H7_rate\", \"genuine_rate\", \"SNH_rate\"]\n    rows = []\n    for cond in [\"ISR\", \"RANDOM\"]:\n        sub = df[df[\"condition\"] == cond]\n        row = {\"condition\": cond, \"n_seeds\": len(sub)}\n        for m in metrics:\n            vals = sub[m].values\n            row[f\"{m}_mean\"] = vals.mean()\n            row[f\"{m}_std\"] = vals.std(ddof=1) if len(vals) > 1 else 0.0\n        isr_vals = sub[\"ISR_star\"].dropna().values.astype(float)\n        row[\"ISR_star_mean\"] = isr_vals.mean() if len(isr_vals) else np.nan\n        row[\"ISR_star_std\"] = isr_vals.std(ddof=1) if len(isr_vals) > 1 else 0.0\n        rows.append(row)\n    return pd.DataFrame(rows)",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"D134 experiment analysis: multi-seed ISR vs Random, 4B GRPO training.\nReads taxonomy data from classify.json, taxonomy.json, or top-level taxonomy files.\nComputes summary stats, statistical tests (Fisher, Mann-Whitney, permutation, Bayes Factor),\nand BCa bootstrap CIs. Outputs appendix-ready markdown.\n\"\"\"\n\nimport argparse\nimport json\nimport re\nimport sys\nfrom pathlib import Path\n\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\nfrom scipy.special import betaln\n\nCONDITION_MAP = [\n    (\"d134_4b_isr\", \"ISR\"),\n    (\"d134_4b_random\", \"RANDOM\"),\n    (\"plan002_additive\", \"ISR\"),\n    (\"plan018_additive_random\", \"RANDOM\"),\n    (\"plan018_random\", \"RANDOM\"),\n]\n\nMODE_PREFIXES = {\n    \"d134_only\": [\"d134_4b\"],\n    \"all\": [\"d134_4b\", \"plan002_additive_b01\", \"plan018_additive_random_b01\", \"plan018_random\"],\n}\n\n\ndef parse_args():\n    p = argparse.ArgumentParser(description=\"D134 multi-seed analysis and statistical tests\")\n    p.add_argument(\"--data_dir\", type=str, default=\"/root/autodl-tmp/outputs\",\n                   help=\"Directory containing experiment outputs\")\n    p.add_argument(\"--mode\", type=str, default=\"d134_only\", choices=list(MODE_PREFIXES),\n                   help=\"d134_only = matched 5+5 design (default); all = include original seeds\")\n    p.add_argument(\"--prefix\", type=str, default=None,\n                   help=\"(Legacy) Single prefix filter; overrides mode/prefixes\")\n    p.add_argument(\"--prefixes\", type=str, default=None,\n                   help=\"Comma-separated prefixes; overrides --mode\")\n    p.add_argument(\"--output\", type=str, default=None,\n                   help=\"Write markdown summary to this file\")\n    p.add_argument(\"--n_perm\", type=int, default=10000,\n                   help=\"Number of permutations for permutation test\")\n    p.add_argument(\"--n_boot\", type=int, default=10000,\n                   help=\"Number of bootstrap resamples for BCa CI\")\n    p.add_argument(\"--seed\", type=int, default=42,\n                   help=\"Random seed for permutation/bootstrap\")\n    return p.parse_args()\n\n\n# --- Data loading ---\n\ndef match_condition(name: str) -> str | None:\n    best_prefix = \"\"\n    best_cond = None\n    for prefix, cond in CONDITION_MAP:\n        if name.startswith(prefix) and len(prefix) > len(best_prefix):\n            best_prefix = prefix\n            best_cond = cond\n    return best_cond\n\n\ndef extract_seed(name: str) -> int | None:\n    m = re.search(r'_s(\\d+)', name)\n    return int(m.group(1)) if m else None\n\n\ndef load_eval_results(path: Path) -> dict | None:\n    if not path.exists():\n        return None\n    with open(path) as f:\n        data = json.load(f)\n    if \"eval_results\" in data:\n        return data[\"eval_results\"]\n    return data\n\n\ndef load_taxonomy_unified(path: Path) -> dict | None:\n    with open(path) as f:\n        raw = json.load(f)\n    t = raw.get(\"taxonomy\", {})\n    proved = t.get(\"proved\", 0)\n    if proved == 0:\n        return None\n    h7 = t.get(\"H7\", 0)\n    h1 = t.get(\"H1_exact\", 0)\n    h8 = t.get(\"H8\", 0)\n    genuine = t.get(\"genuine\", 0)\n    return {\n        \"n_total\": 100, \"n_proved\": proved,\n        \"h7_total_count\": h7, \"h7_total_rate\": h7 / proved,\n        \"h1_strict_count\": h1, \"h8_conjunction_collapse_count\": h8,\n        \"genuine_count\": genuine, \"genuine_rate\": genuine / proved,\n        \"content_independent_count\": 0,\n    }\n\n\ndef load_taxonomy_verification(path: Path) -> dict | None:\n    with open(path) as f:\n        raw = json.load(f)\n    proved = raw.get(\"proved\", 0)\n    if proved == 0:\n        return None\n    tax = raw.get(\"taxonomy\", {})\n    h7 = tax.get(\"h7\", {}).get(\"count\", 0)\n    h1 = tax.get(\"h1_exact\", {}).get(\"count\", 0)\n    h8 = tax.get(\"h8\", {}).get(\"count\", 0)\n    genuine = tax.get(\"genuine\", {}).get(\"count\", 0)\n    return {\n        \"n_total\": raw.get(\"total\", 100), \"n_proved\": proved,\n        \"h7_total_count\": h7, \"h7_total_rate\": h7 / proved,\n        \"h1_strict_count\": h1, \"h8_conjunction_collapse_count\": h8,\n        \"genuine_count\": genuine, \"genuine_rate\": genuine / proved,\n        \"content_independent_count\": 0,\n    }\n\n\ndef discover_runs(data_dir: Path, prefixes: list[str]) -> list[dict]:\n    runs = []\n    seen = set()\n    for entry in sorted(data_dir.iterdir()):\n        name = entry.name\n        if not any(name.startswith(p) for p in prefixes):\n            continue\n        cond = match_condition(name)\n        seed_val = extract_seed(name)\n        if cond is None or seed_val is None:\n            continue\n        key = (cond, seed_val)\n        if key in seen:\n            continue\n        data = None\n        if entry.is_dir():\n            for fname in [\"classify.json\", \"taxonomy.json\"]:\n                data = load_eval_results(entry / fname)\n                if data is not None:\n                    break\n            if data is None:\n                continue\n        elif entry.is_file():\n            if name.endswith(\"_taxonomy_unified.json\"):\n                data = load_taxonomy_unified(entry)\n            elif name.endswith(\"_taxonomy_verification.json\"):\n                data = load_taxonomy_verification(entry)\n            if data is None:\n                continue\n        else:\n            continue\n        seen.add(key)\n        isr_star = None\n        if entry.is_dir():\n            eval_path = entry / \"eval_results.json\"\n            if eval_path.exists():\n                with open(eval_path) as ef:\n                    eval_raw = json.load(ef)\n                isr_star = eval_raw.get(\"summary\", {}).get(\"proved_only_mean_isr\")\n        runs.append({\"dir_name\": name, \"seed\": seed_val, \"condition\": cond,\n                      \"data\": data, \"isr_star\": isr_star})\n    return runs\n\n\ndef compute_row(run: dict) -> dict:\n    d = run[\"data\"]\n    n_proved = d.get(\"n_proved\", 0)\n    n_total = d.get(\"n_total\", 100)\n    h7 = d.get(\"h7_total_count\", 0)\n    h7_rate = d.get(\"h7_total_rate\", h7 / n_proved if n_proved > 0 else 0.0)\n    h1 = d.get(\"h1_strict_count\", 0)\n    h8 = d.get(\"h8_conjunction_collapse_count\", 0)\n    genuine = d.get(\"genuine_count\", 0)\n    genuine_rate = d.get(\"genuine_rate\", genuine / n_proved if n_proved > 0 else 0.0)\n    ci = d.get(\"content_independent_count\", 0)\n    snh = max(genuine - ci, 0)\n    snh_rate = snh / n_proved if n_proved > 0 else 0.0\n    return {\n        \"seed\": run[\"seed\"], \"condition\": run[\"condition\"], \"n_total\": n_total,\n        \"PR\": n_proved, \"H7_count\": h7, \"H7_rate\": h7_rate,\n        \"H1_count\": h1, \"H8_count\": h8,\n        \"genuine_count\": genuine, \"genuine_rate\": genuine_rate,\n        \"CI_count\": ci, \"SNH_count\": snh, \"SNH_rate\": snh_rate,\n        \"ISR_star\": run.get(\"isr_star\"),\n    }\n\n\ndef build_table(runs: list[dict]) -> pd.DataFrame:\n    rows = [compute_row(r) for r in runs]\n    df = pd.DataFrame(rows)\n    df = df.sort_values([\"condition\", \"seed\"]).reset_index(drop=True)\n    return df\n\n\n# --- Statistical tests ---\n\ndef fisher_h7_domination(df: pd.DataFrame) -> dict:\n    results = {}\n    for cond in [\"ISR\", \"RANDOM\"]:\n        sub = df[df[\"condition\"] == cond]\n        results[cond] = {\n            \"n\": len(sub),\n            \"h7_dom\": int((sub[\"H7_rate\"] >= 0.5).sum()),\n            \"not_h7_dom\": int((sub[\"H7_rate\"] < 0.5).sum()),\n        }\n    table = np.array([\n        [results[\"ISR\"][\"h7_dom\"], results[\"ISR\"][\"not_h7_dom\"]],\n        [results[\"RANDOM\"][\"h7_dom\"], results[\"RANDOM\"][\"not_h7_dom\"]],\n    ])\n    odds_ratio, p_value = stats.fisher_exact(table, alternative=\"greater\")\n\n    # 95% exact CI via scipy.stats.contingency\n    or_ci_lo, or_ci_hi = np.nan, np.nan\n    try:\n        ct = stats.contingency.odds_ratio(table)\n        ci = ct.confidence_interval(confidence_level=0.95)\n        or_ci_lo, or_ci_hi = ci.low, ci.high\n    except Exception:\n        pass\n\n    return {\n        \"table\": table.tolist(),\n        \"ISR\": results[\"ISR\"],\n        \"RANDOM\": results[\"RANDOM\"],\n        \"odds_ratio\": odds_ratio,\n        \"or_ci_lo\": or_ci_lo,\n        \"or_ci_hi\": or_ci_hi,\n        \"p_value\": p_value,\n    }\n\n\ndef permutation_test_genuine(df: pd.DataFrame, n_perm: int = 10000,\n                              rng_seed: int = 42) -> dict:\n    isr = df[df[\"condition\"] == \"ISR\"][\"genuine_rate\"].values\n    rand = df[df[\"condition\"] == \"RANDOM\"][\"genuine_rate\"].values\n    observed = isr.mean() - rand.mean()\n    pooled = np.concatenate([isr, rand])\n    n_isr = len(isr)\n    rng = np.random.default_rng(rng_seed)\n    count = 0\n    for _ in range(n_perm):\n        perm = rng.permutation(pooled)\n        if perm[:n_isr].mean() - perm[n_isr:].mean() >= observed:\n            count += 1\n    return {\n        \"observed_diff\": float(observed),\n        \"p_value\": count / n_perm,\n        \"n_perm\": n_perm,\n        \"isr_mean\": float(isr.mean()),\n        \"random_mean\": float(rand.mean()),\n    }\n\n\ndef mannwhitney_h7(df: pd.DataFrame) -> dict:\n    isr = df[df[\"condition\"] == \"ISR\"][\"H7_rate\"].values\n    rand = df[df[\"condition\"] == \"RANDOM\"][\"H7_rate\"].values\n    n1, n2 = len(isr), len(rand)\n    u_stat, p_value = stats.mannwhitneyu(isr, rand, alternative=\"greater\")\n    r_rb = 2.0 * u_stat / (n1 * n2) - 1.0 if n1 * n2 > 0 else np.nan\n    return {\n        \"U\": float(u_stat),\n        \"p_value\": float(p_value),\n        \"r_rank_biserial\": float(r_rb),\n        \"isr_median\": float(np.median(isr)),\n        \"random_median\": float(np.median(rand)),\n    }\n\n\ndef mannwhitney_isr_star(df: pd.DataFrame) -> dict | None:\n    isr = df[df[\"condition\"] == \"ISR\"][\"ISR_star\"].dropna().values.astype(float)\n    rand = df[df[\"condition\"] == \"RANDOM\"][\"ISR_star\"].dropna().values.astype(float)\n    if len(isr) < 2 or len(rand) < 2:\n        return None\n    n1, n2 = len(isr), len(rand)\n    u_stat, p_value = stats.mannwhitneyu(isr, rand, alternative=\"greater\")\n    r_rb = 2.0 * u_stat / (n1 * n2) - 1.0\n    return {\n        \"U\": float(u_stat),\n        \"p_value\": float(p_value),\n        \"r_rank_biserial\": float(r_rb),\n        \"isr_median\": float(np.median(isr)),\n        \"random_median\": float(np.median(rand)),\n        \"isr_mean\": float(np.mean(isr)),\n        \"random_mean\": float(np.mean(rand)),\n    }\n\n\ndef bca_bootstrap_ci(df: pd.DataFrame, metric: str, n_boot: int = 10000,\n                      rng_seed: int = 42) -> dict:\n    \"\"\"BCa 95% CI for per-condition means of a metric.\"\"\"\n    result = {}\n    for cond in [\"ISR\", \"RANDOM\"]:\n        vals = df[df[\"condition\"] == cond][metric].values\n        if len(vals) < 2:\n            result[cond] = {\"mean\": float(vals.mean()) if len(vals) else np.nan,\n                            \"ci_lo\": np.nan, \"ci_hi\": np.nan}\n            continue\n        res = stats.bootstrap(\n            (vals,), np.mean, n_resamples=n_boot,\n            confidence_level=0.95, method=\"BCa\",\n            random_state=np.random.default_rng(rng_seed),\n        )\n        result[cond] = {\n            \"mean\": float(vals.mean()),\n            \"ci_lo\": float(res.confidence_interval.low),\n            \"ci_hi\": float(res.confidence_interval.high),\n        }\n    return result\n\n\ndef bayes_factor_h7_domination(df: pd.DataFrame) -> dict:\n    \"\"\"BF10 for H7-domination rate difference (beta-binomial conjugate).\n    H0: ISR and Random share same domination rate.\n    H1: independent rates. Prior: Beta(1,1) on each.\n    \"\"\"\n    isr_sub = df[df[\"condition\"] == \"ISR\"]\n    rand_sub = df[df[\"condition\"] == \"RANDOM\"]\n    k_isr = int((isr_sub[\"H7_rate\"] >= 0.5).sum())\n    n_isr = len(isr_sub)\n    k_rand = int((rand_sub[\"H7_rate\"] >= 0.5).sum())\n    n_rand = len(rand_sub)\n    k_total = k_isr + k_rand\n    n_total = n_isr + n_rand\n\n    # log marginal under H0 (shared rate)\n    log_m_h0 = betaln(1 + k_total, 1 + n_total - k_total) - betaln(1, 1)\n    # log marginal under H1 (independent rates)\n    log_m_h1 = (betaln(1 + k_isr, 1 + n_isr - k_isr) - betaln(1, 1)\n                + betaln(1 + k_rand, 1 + n_rand - k_rand) - betaln(1, 1))\n    log_bf10 = log_m_h1 - log_m_h0\n    bf10 = float(np.exp(log_bf10))\n\n    return {\n        \"k_isr\": k_isr, \"n_isr\": n_isr,\n        \"k_rand\": k_rand, \"n_rand\": n_rand,\n        \"bf10\": bf10,\n        \"log_bf10\": float(log_bf10),\n        \"interpretation\": _interpret_bf(bf10),\n    }\n\n\ndef _interpret_bf(bf: float) -> str:\n    if bf > 100:\n        return \"extreme evidence for H1\"\n    if bf > 30:\n        return \"very strong evidence for H1\"\n    if bf > 10:\n        return \"strong evidence for H1\"\n    if bf > 3:\n        return \"moderate evidence for H1\"\n    if bf > 1:\n        return \"anecdotal evidence for H1\"\n    if bf > 1/3:\n        return \"anecdotal evidence (inconclusive)\"\n    if bf > 1/10:\n        return \"moderate evidence for H0\"\n    return \"strong evidence for H0\"\n\n\ndef condition_stats(df: pd.DataFrame) -> pd.DataFrame:\n    metrics = [\"PR\", \"H7_rate\", \"genuine_rate\", \"SNH_rate\"]\n    rows = []\n    for cond in [\"ISR\", \"RANDOM\"]:\n        sub = df[df[\"condition\"] == cond]\n        row = {\"condition\": cond, \"n_seeds\": len(sub)}\n        for m in metrics:\n            vals = sub[m].values\n            row[f\"{m}_mean\"] = vals.mean()\n            row[f\"{m}_std\"] = vals.std(ddof=1) if len(vals) > 1 else 0.0\n        rows.append(row)\n    return pd.DataFrame(rows)\n\n\n# --- Formatting ---\n\ndef fmt_pct(val: float) -> str:\n    return f\"{val*100:.1f}\\\\%\"\n\ndef fmt_or(val: float) -> str:\n    return \"$\\\\infty$\" if np.isinf(val) else f\"{val:.2f}\"\n\ndef fmt_ci(lo: float, hi: float) -> str:\n    lo_s = f\"{lo:.2f}\" if not np.isnan(lo) else \"0\"\n    hi_s = \"$\\\\infty$\" if np.isinf(hi) or np.isnan(hi) else f\"{hi:.2f}\"\n    return f\"[{lo_s}, {hi_s}]\"\n\ndef fmt_p(p: float) -> str:\n    if p < 0.001:\n        return \"$<$0.001\"\n    return f\"{p:.3f}\"\n\ndef fmt_mean_std(mean: float, std: float, pct: bool = False) -> str:\n    if pct:\n        return f\"{mean*100:.1f} $\\\\pm$ {std*100:.1f}\\\\%\"\n    return f\"{mean:.1f} $\\\\pm$ {std:.1f}\"\n\ndef fmt_bca(bca: dict, pct: bool = False) -> str:\n    m = bca[\"mean\"]\n    lo, hi = bca[\"ci_lo\"], bca[\"ci_hi\"]\n    if pct:\n        return f\"{m*100:.1f}\\\\% [{lo*100:.1f}, {hi*100:.1f}]\"\n    return f\"{m:.1f} [{lo:.1f}, {hi:.1f}]\"\n\n\n# --- Console output ---\n\ndef print_per_seed_table(df: pd.DataFrame):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  PER-SEED RESULTS\")\n    print(\"=\" * 90)\n    cols = [\"condition\", \"seed\", \"PR\", \"H7_count\", \"H7_rate\", \"H1_count\",\n            \"H8_count\", \"genuine_count\", \"genuine_rate\", \"CI_count\", \"SNH_count\", \"SNH_rate\"]\n    fmt = df[cols].copy()\n    for c in [\"H7_rate\", \"genuine_rate\", \"SNH_rate\"]:\n        fmt[c] = fmt[c].apply(lambda v: f\"{v*100:.1f}%\")\n    print(fmt.to_string(index=False))\n\n\ndef print_condition_stats(cond_df: pd.DataFrame):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  CONDITION-LEVEL STATISTICS (mean +/- SD)\")\n    print(\"=\" * 90)\n    for _, row in cond_df.iterrows():\n        n = int(row['n_seeds'])\n        print(f\"\\n  {row['condition']} (n={n} seeds):\")\n        print(f\"    PR:           {row['PR_mean']:.1f} +/- {row['PR_std']:.1f}\")\n        print(f\"    H7 rate:      {row['H7_rate_mean']*100:.1f} +/- {row['H7_rate_std']*100:.1f}%\")\n        print(f\"    Genuine rate: {row['genuine_rate_mean']*100:.1f} +/- {row['genuine_rate_std']*100:.1f}%\")\n        print(f\"    S-NH rate:    {row['SNH_rate_mean']*100:.1f} +/- {row['SNH_rate_std']*100:.1f}%\")\n\n\ndef print_tests(fisher, perm, mw, bf, bca_h7, bca_gen):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  STATISTICAL TESTS\")\n    print(\"=\" * 90)\n\n    print(\"\\n  1. H7 Domination Fisher Exact Test (H7-dominated = H7% >= 50%)\")\n    print(f\"     ISR:    {fisher['ISR']['h7_dom']} dominated / {fisher['ISR']['n']} seeds\")\n    print(f\"     RANDOM: {fisher['RANDOM']['h7_dom']} dominated / {fisher['RANDOM']['n']} seeds\")\n    print(f\"     Contingency: {fisher['table']}\")\n    or_str = \"inf\" if np.isinf(fisher['odds_ratio']) else f\"{fisher['odds_ratio']:.4f}\"\n    print(f\"     OR = {or_str}, 95% CI = [{fisher['or_ci_lo']:.4f}, {fisher['or_ci_hi']:.4f}]\"\n          if not np.isnan(fisher['or_ci_lo']) else f\"     OR = {or_str}, 95% CI = N/A\")\n    print(f\"     p-value (one-sided, greater): {fisher['p_value']:.4f}\")\n\n    print(f\"\\n  2. Genuine Rate Permutation Test (n_perm={perm['n_perm']})\")\n    print(f\"     ISR mean:    {perm['isr_mean']*100:.2f}%\")\n    print(f\"     RANDOM mean: {perm['random_mean']*100:.2f}%\")\n    print(f\"     Diff: {perm['observed_diff']*100:.2f} pp, p = {perm['p_value']:.4f}\")\n\n    print(f\"\\n  3. H7 Rate Mann-Whitney U Test\")\n    print(f\"     ISR median:    {mw['isr_median']*100:.1f}%\")\n    print(f\"     RANDOM median: {mw['random_median']*100:.1f}%\")\n    print(f\"     U = {mw['U']:.1f}, p = {mw['p_value']:.4f}\")\n    print(f\"     Rank-biserial r = {mw['r_rank_biserial']:.4f}\")\n\n    print(f\"\\n  4. Bayes Factor (H7 Domination, Beta-Binomial)\")\n    print(f\"     ISR:    {bf['k_isr']}/{bf['n_isr']} dominated\")\n    print(f\"     RANDOM: {bf['k_rand']}/{bf['n_rand']} dominated\")\n    print(f\"     BF10 = {bf['bf10']:.4f} ({bf['interpretation']})\")\n\n    print(f\"\\n  5. BCa Bootstrap 95% CI (n_boot resamples)\")\n    for label, bca in [(\"H7 rate\", bca_h7), (\"Genuine rate\", bca_gen)]:\n        print(f\"     {label}:\")\n        for cond in [\"ISR\", \"RANDOM\"]:\n            b = bca[cond]\n            print(f\"       {cond}: {b['mean']*100:.1f}% [{b['ci_lo']*100:.1f}, {b['ci_hi']*100:.1f}]\"\n                  if not np.isnan(b['ci_lo']) else f\"       {cond}: {b['mean']*100:.1f}% [N/A]\")\n\n\n# --- Markdown generation (appendix-ready) ---\n\ndef generate_markdown(df: pd.DataFrame, cond_df: pd.DataFrame,\n                      fisher: dict, perm: dict, mw: dict,\n                      bf: dict, bca_h7: dict, bca_gen: dict) -> str:\n    L = []\n    L.append(\"## D134: ISR vs Random Statistical Analysis\\n\")\n\n    # Per-seed table\n    L.append(\"### Table A1: Per-Seed Hacking Taxonomy (4B Qwen3, 500 steps)\\n\")\n    L.append(\"| Condition | Seed | PR | H7 | H7\\\\% | H1 | H8 | Genuine | Gen\\\\% | CI | S-NH | S-NH\\\\% |\")\n    L.append(\"|:----------|-----:|---:|---:|-----:|---:|---:|--------:|------:|---:|-----:|-------:|\")\n    for _, r in df.iterrows():\n        L.append(\n            f\"| {r['condition']} | {r['seed']} | {int(r['PR'])} | {int(r['H7_count'])} | \"\n            f\"{r['H7_rate']*100:.1f} | {int(r['H1_count'])} | {int(r['H8_count'])} | \"\n            f\"{int(r['genuine_count'])} | {r['genuine_rate']*100:.1f} | {int(r['CI_count'])} | \"\n            f\"{int(r['SNH_count'])} | {r['SNH_rate']*100:.1f} |\"\n        )\n\n    # Condition summary with BCa CI\n    L.append(\"\\n### Table A2: Condition-Level Summary\\n\")\n    L.append(\"| Condition | $n$ | PR (mean$\\\\pm$SD) | H7\\\\% (mean$\\\\pm$SD) | H7\\\\% BCa 95\\\\% CI | Gen\\\\% (mean$\\\\pm$SD) | Gen\\\\% BCa 95\\\\% CI |\")\n    L.append(\"|:----------|----:|:------------------|:-------------------|:-----------------|:-------------------|:-----------------|\")\n    for _, r in cond_df.iterrows():\n        cond = r[\"condition\"]\n        h7_bca = bca_h7.get(cond, {})\n        gen_bca = bca_gen.get(cond, {})\n        h7_ci = f\"[{h7_bca['ci_lo']*100:.1f}, {h7_bca['ci_hi']*100:.1f}]\" if h7_bca and not np.isnan(h7_bca.get('ci_lo', np.nan)) else \"N/A\"\n        gen_ci = f\"[{gen_bca['ci_lo']*100:.1f}, {gen_bca['ci_hi']*100:.1f}]\" if gen_bca and not np.isnan(gen_bca.get('ci_lo', np.nan)) else \"N/A\"\n        L.append(\n            f\"| {cond} | {int(r['n_seeds'])} | \"\n            f\"{r['PR_mean']:.1f}$\\\\pm${r['PR_std']:.1f} | \"\n            f\"{r['H7_rate_mean']*100:.1f}$\\\\pm${r['H7_rate_std']*100:.1f} | \"\n            f\"{h7_ci} | \"\n            f\"{r['genuine_rate_mean']*100:.1f}$\\\\pm${r['genuine_rate_std']*100:.1f} | \"\n            f\"{gen_ci} |\"\n        )\n\n    # Statistical tests\n    if fisher and perm and mw and bf:\n        L.append(\"\\n### Statistical Tests\\n\")\n\n        # Fisher\n        or_str = \"$\\\\infty$\" if np.isinf(fisher['odds_ratio']) else f\"{fisher['odds_ratio']:.2f}\"\n        ci_lo = f\"{fisher['or_ci_lo']:.2f}\" if not np.isnan(fisher['or_ci_lo']) else \"0\"\n        ci_hi = \"$\\\\infty$\" if np.isinf(fisher.get('or_ci_hi', np.inf)) or np.isnan(fisher.get('or_ci_hi', np.nan)) else f\"{fisher['or_ci_hi']:.2f}\"\n        L.append(\"**1. H7 Domination Fisher Exact Test** (threshold: H7$\\\\geq$50\\\\% of proved)\")\n        L.append(f\"- ISR: {fisher['ISR']['h7_dom']}/{fisher['ISR']['n']} seeds H7-dominated; \"\n                 f\"Random: {fisher['RANDOM']['h7_dom']}/{fisher['RANDOM']['n']}\")\n        L.append(f\"- OR = {or_str}, 95\\\\% exact CI = [{ci_lo}, {ci_hi}], \"\n                 f\"$p$ = {fmt_p(fisher['p_value'])}\")\n        L.append(\"\")\n\n        # Permutation\n        L.append(f\"**2. Genuine Rate Permutation Test** ($n$ = {perm['n_perm']:,} permutations)\")\n        L.append(f\"- ISR mean: {perm['isr_mean']*100:.2f}\\\\%, Random mean: {perm['random_mean']*100:.2f}\\\\%\")\n        L.append(f\"- $\\\\Delta$ = {perm['observed_diff']*100:.2f} pp, $p$ = {fmt_p(perm['p_value'])}\")\n        L.append(\"\")\n\n        # Mann-Whitney\n        L.append(\"**3. H7 Rate Mann-Whitney $U$ Test**\")\n        L.append(f\"- ISR median: {mw['isr_median']*100:.1f}\\\\%, Random median: {mw['random_median']*100:.1f}\\\\%\")\n        L.append(f\"- $U$ = {mw['U']:.1f}, $p$ = {fmt_p(mw['p_value'])}, \"\n                 f\"rank-biserial $r$ = {mw['r_rank_biserial']:.3f}\")\n        L.append(\"\")\n\n        # Bayes Factor\n        L.append(\"**4. Bayes Factor** (Beta-Binomial conjugate, prior: Beta(1,1))\")\n        L.append(f\"- $BF_{{10}}$ = {bf['bf10']:.2f} ({bf['interpretation']})\")\n        L.append(f\"- ISR: {bf['k_isr']}/{bf['n_isr']} H7-dominated, \"\n                 f\"Random: {bf['k_rand']}/{bf['n_rand']}\")\n\n    return \"\\n\".join(L) + \"\\n\"\n\n\n# --- Main ---\n\ndef main():\n    args = parse_args()\n    data_dir = Path(args.data_dir)\n\n    if not data_dir.exists():\n        print(f\"ERROR: data directory {data_dir} does not exist\", file=sys.stderr)\n        sys.exit(1)\n\n    if args.prefix:\n        prefixes = [args.prefix]\n    elif args.prefixes:\n        prefixes = [p.strip() for p in args.prefixes.split(\",\")]\n    else:\n        prefixes = MODE_PREFIXES[args.mode]\n    print(f\"Mode: {args.mode} | Prefixes: {prefixes}\")\n\n    runs = discover_runs(data_dir, prefixes)\n    if not runs:\n        print(f\"ERROR: no runs found in {data_dir} with prefixes {prefixes}\", file=sys.stderr)\n        sys.exit(1)\n\n    isr_count = sum(1 for r in runs if r[\"condition\"] == \"ISR\")\n    rand_count = sum(1 for r in runs if r[\"condition\"] == \"RANDOM\")\n    print(f\"Found {len(runs)} runs: {isr_count} ISR, {rand_count} RANDOM\")\n    for r in runs:\n        print(f\"  {r['condition']:6s} s{r['seed']} <- {r['dir_name']}\")\n\n    df = build_table(runs)\n    print_per_seed_table(df)\n\n    cond_df = condition_stats(df)\n    print_condition_stats(cond_df)\n\n    if isr_count < 2 or rand_count < 2:\n        print(\"\\nWARNING: need >= 2 seeds per condition for statistical tests, skipping.\",\n              file=sys.stderr)\n        bca_h7 = bca_bootstrap_ci(df, \"H7_rate\", args.n_boot, args.seed)\n        bca_gen = bca_bootstrap_ci(df, \"genuine_rate\", args.n_boot, args.seed)\n        if args.output:\n            md = generate_markdown(df, cond_df, {}, {}, {}, {}, bca_h7, bca_gen)\n            Path(args.output).write_text(md)\n            print(f\"\\nMarkdown written to {args.output}\")\n        return\n\n    fisher = fisher_h7_domination(df)\n    perm = permutation_test_genuine(df, n_perm=args.n_perm, rng_seed=args.seed)\n    mw = mannwhitney_h7(df)\n    bf = bayes_factor_h7_domination(df)\n    bca_h7 = bca_bootstrap_ci(df, \"H7_rate\", args.n_boot, args.seed)\n    bca_gen = bca_bootstrap_ci(df, \"genuine_rate\", args.n_boot, args.seed)\n\n    print_tests(fisher, perm, mw, bf, bca_h7, bca_gen)\n\n    md = generate_markdown(df, cond_df, fisher, perm, mw, bf, bca_h7, bca_gen)\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  MARKDOWN OUTPUT (appendix-ready)\")\n    print(\"=\" * 90)\n    print(md)\n\n    if args.output:\n        Path(args.output).parent.mkdir(parents=True, exist_ok=True)\n        Path(args.output).write_text(md)\n        print(f\"Markdown written to {args.output}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 367,
        "oldLines": 6,
        "newStart": 367,
        "newLines": 9,
        "lines": [
          "             vals = sub[m].values",
          "             row[f\"{m}_mean\"] = vals.mean()",
          "             row[f\"{m}_std\"] = vals.std(ddof=1) if len(vals) > 1 else 0.0",
          "+        isr_vals = sub[\"ISR_star\"].dropna().values.astype(float)",
          "+        row[\"ISR_star_mean\"] = isr_vals.mean() if len(isr_vals) else np.nan",
          "+        row[\"ISR_star_std\"] = isr_vals.std(ddof=1) if len(isr_vals) > 1 else 0.0",
          "         rows.append(row)",
          "     return pd.DataFrame(rows)",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 30_

**Edit 5**: Add ISR* column to `print_per_seed_table`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "890e6a51-5944-4311-beae-4a950863be80",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B7c6Dp8gB8u1qBZuK9DENP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 660,
      "cache_read_input_tokens": 47446,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 660
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

<details open><summary>🔧 Tool call — Edit · `toolu_01WpQCDerqsfAhEfLxuTDqHG`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/scripts/d134_analysis.py",
  "old_string": "def print_per_seed_table(df: pd.DataFrame):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  PER-SEED RESULTS\")\n    print(\"=\" * 90)\n    cols = [\"condition\", \"seed\", \"PR\", \"H7_count\", \"H7_rate\", \"H1_count\",\n            \"H8_count\", \"genuine_count\", \"genuine_rate\", \"CI_count\", \"SNH_count\", \"SNH_rate\"]\n    fmt = df[cols].copy()\n    for c in [\"H7_rate\", \"genuine_rate\", \"SNH_rate\"]:\n        fmt[c] = fmt[c].apply(lambda v: f\"{v*100:.1f}%\")\n    print(fmt.to_string(index=False))",
  "new_string": "def print_per_seed_table(df: pd.DataFrame):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  PER-SEED RESULTS\")\n    print(\"=\" * 90)\n    cols = [\"condition\", \"seed\", \"PR\", \"H7_count\", \"H7_rate\", \"H1_count\",\n            \"H8_count\", \"genuine_count\", \"genuine_rate\", \"CI_count\", \"SNH_count\", \"SNH_rate\",\n            \"ISR_star\"]\n    fmt = df[cols].copy()\n    for c in [\"H7_rate\", \"genuine_rate\", \"SNH_rate\"]:\n        fmt[c] = fmt[c].apply(lambda v: f\"{v*100:.1f}%\")\n    fmt[\"ISR_star\"] = fmt[\"ISR_star\"].apply(lambda v: f\"{v:.4f}\" if pd.notna(v) else \"---\")\n    print(fmt.to_string(index=False))"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "ea290171-5e1e-4f2f-9d49-a83de3753eee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B7c6Dp8gB8u1qBZuK9DENP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 660,
      "cache_read_input_tokens": 47446,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 660
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

_source line 32 · 2026-05-18T23:32:37.446Z_

<details><summary>↩ Tool result · `toolu_01WpQCDerqsfAhEfLxuTDqHG`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/scripts/d134_analysis.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "d890a848-3b25-4696-b7f2-20704fda984c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/scripts/d134_analysis.py",
    "oldString": "def print_per_seed_table(df: pd.DataFrame):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  PER-SEED RESULTS\")\n    print(\"=\" * 90)\n    cols = [\"condition\", \"seed\", \"PR\", \"H7_count\", \"H7_rate\", \"H1_count\",\n            \"H8_count\", \"genuine_count\", \"genuine_rate\", \"CI_count\", \"SNH_count\", \"SNH_rate\"]\n    fmt = df[cols].copy()\n    for c in [\"H7_rate\", \"genuine_rate\", \"SNH_rate\"]:\n        fmt[c] = fmt[c].apply(lambda v: f\"{v*100:.1f}%\")\n    print(fmt.to_string(index=False))",
    "newString": "def print_per_seed_table(df: pd.DataFrame):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  PER-SEED RESULTS\")\n    print(\"=\" * 90)\n    cols = [\"condition\", \"seed\", \"PR\", \"H7_count\", \"H7_rate\", \"H1_count\",\n            \"H8_count\", \"genuine_count\", \"genuine_rate\", \"CI_count\", \"SNH_count\", \"SNH_rate\",\n            \"ISR_star\"]\n    fmt = df[cols].copy()\n    for c in [\"H7_rate\", \"genuine_rate\", \"SNH_rate\"]:\n        fmt[c] = fmt[c].apply(lambda v: f\"{v*100:.1f}%\")\n    fmt[\"ISR_star\"] = fmt[\"ISR_star\"].apply(lambda v: f\"{v:.4f}\" if pd.notna(v) else \"---\")\n    print(fmt.to_string(index=False))",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"D134 experiment analysis: multi-seed ISR vs Random, 4B GRPO training.\nReads taxonomy data from classify.json, taxonomy.json, or top-level taxonomy files.\nComputes summary stats, statistical tests (Fisher, Mann-Whitney, permutation, Bayes Factor),\nand BCa bootstrap CIs. Outputs appendix-ready markdown.\n\"\"\"\n\nimport argparse\nimport json\nimport re\nimport sys\nfrom pathlib import Path\n\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\nfrom scipy.special import betaln\n\nCONDITION_MAP = [\n    (\"d134_4b_isr\", \"ISR\"),\n    (\"d134_4b_random\", \"RANDOM\"),\n    (\"plan002_additive\", \"ISR\"),\n    (\"plan018_additive_random\", \"RANDOM\"),\n    (\"plan018_random\", \"RANDOM\"),\n]\n\nMODE_PREFIXES = {\n    \"d134_only\": [\"d134_4b\"],\n    \"all\": [\"d134_4b\", \"plan002_additive_b01\", \"plan018_additive_random_b01\", \"plan018_random\"],\n}\n\n\ndef parse_args():\n    p = argparse.ArgumentParser(description=\"D134 multi-seed analysis and statistical tests\")\n    p.add_argument(\"--data_dir\", type=str, default=\"/root/autodl-tmp/outputs\",\n                   help=\"Directory containing experiment outputs\")\n    p.add_argument(\"--mode\", type=str, default=\"d134_only\", choices=list(MODE_PREFIXES),\n                   help=\"d134_only = matched 5+5 design (default); all = include original seeds\")\n    p.add_argument(\"--prefix\", type=str, default=None,\n                   help=\"(Legacy) Single prefix filter; overrides mode/prefixes\")\n    p.add_argument(\"--prefixes\", type=str, default=None,\n                   help=\"Comma-separated prefixes; overrides --mode\")\n    p.add_argument(\"--output\", type=str, default=None,\n                   help=\"Write markdown summary to this file\")\n    p.add_argument(\"--n_perm\", type=int, default=10000,\n                   help=\"Number of permutations for permutation test\")\n    p.add_argument(\"--n_boot\", type=int, default=10000,\n                   help=\"Number of bootstrap resamples for BCa CI\")\n    p.add_argument(\"--seed\", type=int, default=42,\n                   help=\"Random seed for permutation/bootstrap\")\n    return p.parse_args()\n\n\n# --- Data loading ---\n\ndef match_condition(name: str) -> str | None:\n    best_prefix = \"\"\n    best_cond = None\n    for prefix, cond in CONDITION_MAP:\n        if name.startswith(prefix) and len(prefix) > len(best_prefix):\n            best_prefix = prefix\n            best_cond = cond\n    return best_cond\n\n\ndef extract_seed(name: str) -> int | None:\n    m = re.search(r'_s(\\d+)', name)\n    return int(m.group(1)) if m else None\n\n\ndef load_eval_results(path: Path) -> dict | None:\n    if not path.exists():\n        return None\n    with open(path) as f:\n        data = json.load(f)\n    if \"eval_results\" in data:\n        return data[\"eval_results\"]\n    return data\n\n\ndef load_taxonomy_unified(path: Path) -> dict | None:\n    with open(path) as f:\n        raw = json.load(f)\n    t = raw.get(\"taxonomy\", {})\n    proved = t.get(\"proved\", 0)\n    if proved == 0:\n        return None\n    h7 = t.get(\"H7\", 0)\n    h1 = t.get(\"H1_exact\", 0)\n    h8 = t.get(\"H8\", 0)\n    genuine = t.get(\"genuine\", 0)\n    return {\n        \"n_total\": 100, \"n_proved\": proved,\n        \"h7_total_count\": h7, \"h7_total_rate\": h7 / proved,\n        \"h1_strict_count\": h1, \"h8_conjunction_collapse_count\": h8,\n        \"genuine_count\": genuine, \"genuine_rate\": genuine / proved,\n        \"content_independent_count\": 0,\n    }\n\n\ndef load_taxonomy_verification(path: Path) -> dict | None:\n    with open(path) as f:\n        raw = json.load(f)\n    proved = raw.get(\"proved\", 0)\n    if proved == 0:\n        return None\n    tax = raw.get(\"taxonomy\", {})\n    h7 = tax.get(\"h7\", {}).get(\"count\", 0)\n    h1 = tax.get(\"h1_exact\", {}).get(\"count\", 0)\n    h8 = tax.get(\"h8\", {}).get(\"count\", 0)\n    genuine = tax.get(\"genuine\", {}).get(\"count\", 0)\n    return {\n        \"n_total\": raw.get(\"total\", 100), \"n_proved\": proved,\n        \"h7_total_count\": h7, \"h7_total_rate\": h7 / proved,\n        \"h1_strict_count\": h1, \"h8_conjunction_collapse_count\": h8,\n        \"genuine_count\": genuine, \"genuine_rate\": genuine / proved,\n        \"content_independent_count\": 0,\n    }\n\n\ndef discover_runs(data_dir: Path, prefixes: list[str]) -> list[dict]:\n    runs = []\n    seen = set()\n    for entry in sorted(data_dir.iterdir()):\n        name = entry.name\n        if not any(name.startswith(p) for p in prefixes):\n            continue\n        cond = match_condition(name)\n        seed_val = extract_seed(name)\n        if cond is None or seed_val is None:\n            continue\n        key = (cond, seed_val)\n        if key in seen:\n            continue\n        data = None\n        if entry.is_dir():\n            for fname in [\"classify.json\", \"taxonomy.json\"]:\n                data = load_eval_results(entry / fname)\n                if data is not None:\n                    break\n            if data is None:\n                continue\n        elif entry.is_file():\n            if name.endswith(\"_taxonomy_unified.json\"):\n                data = load_taxonomy_unified(entry)\n            elif name.endswith(\"_taxonomy_verification.json\"):\n                data = load_taxonomy_verification(entry)\n            if data is None:\n                continue\n        else:\n            continue\n        seen.add(key)\n        isr_star = None\n        if entry.is_dir():\n            eval_path = entry / \"eval_results.json\"\n            if eval_path.exists():\n                with open(eval_path) as ef:\n                    eval_raw = json.load(ef)\n                isr_star = eval_raw.get(\"summary\", {}).get(\"proved_only_mean_isr\")\n        runs.append({\"dir_name\": name, \"seed\": seed_val, \"condition\": cond,\n                      \"data\": data, \"isr_star\": isr_star})\n    return runs\n\n\ndef compute_row(run: dict) -> dict:\n    d = run[\"data\"]\n    n_proved = d.get(\"n_proved\", 0)\n    n_total = d.get(\"n_total\", 100)\n    h7 = d.get(\"h7_total_count\", 0)\n    h7_rate = d.get(\"h7_total_rate\", h7 / n_proved if n_proved > 0 else 0.0)\n    h1 = d.get(\"h1_strict_count\", 0)\n    h8 = d.get(\"h8_conjunction_collapse_count\", 0)\n    genuine = d.get(\"genuine_count\", 0)\n    genuine_rate = d.get(\"genuine_rate\", genuine / n_proved if n_proved > 0 else 0.0)\n    ci = d.get(\"content_independent_count\", 0)\n    snh = max(genuine - ci, 0)\n    snh_rate = snh / n_proved if n_proved > 0 else 0.0\n    return {\n        \"seed\": run[\"seed\"], \"condition\": run[\"condition\"], \"n_total\": n_total,\n        \"PR\": n_proved, \"H7_count\": h7, \"H7_rate\": h7_rate,\n        \"H1_count\": h1, \"H8_count\": h8,\n        \"genuine_count\": genuine, \"genuine_rate\": genuine_rate,\n        \"CI_count\": ci, \"SNH_count\": snh, \"SNH_rate\": snh_rate,\n        \"ISR_star\": run.get(\"isr_star\"),\n    }\n\n\ndef build_table(runs: list[dict]) -> pd.DataFrame:\n    rows = [compute_row(r) for r in runs]\n    df = pd.DataFrame(rows)\n    df = df.sort_values([\"condition\", \"seed\"]).reset_index(drop=True)\n    return df\n\n\n# --- Statistical tests ---\n\ndef fisher_h7_domination(df: pd.DataFrame) -> dict:\n    results = {}\n    for cond in [\"ISR\", \"RANDOM\"]:\n        sub = df[df[\"condition\"] == cond]\n        results[cond] = {\n            \"n\": len(sub),\n            \"h7_dom\": int((sub[\"H7_rate\"] >= 0.5).sum()),\n            \"not_h7_dom\": int((sub[\"H7_rate\"] < 0.5).sum()),\n        }\n    table = np.array([\n        [results[\"ISR\"][\"h7_dom\"], results[\"ISR\"][\"not_h7_dom\"]],\n        [results[\"RANDOM\"][\"h7_dom\"], results[\"RANDOM\"][\"not_h7_dom\"]],\n    ])\n    odds_ratio, p_value = stats.fisher_exact(table, alternative=\"greater\")\n\n    # 95% exact CI via scipy.stats.contingency\n    or_ci_lo, or_ci_hi = np.nan, np.nan\n    try:\n        ct = stats.contingency.odds_ratio(table)\n        ci = ct.confidence_interval(confidence_level=0.95)\n        or_ci_lo, or_ci_hi = ci.low, ci.high\n    except Exception:\n        pass\n\n    return {\n        \"table\": table.tolist(),\n        \"ISR\": results[\"ISR\"],\n        \"RANDOM\": results[\"RANDOM\"],\n        \"odds_ratio\": odds_ratio,\n        \"or_ci_lo\": or_ci_lo,\n        \"or_ci_hi\": or_ci_hi,\n        \"p_value\": p_value,\n    }\n\n\ndef permutation_test_genuine(df: pd.DataFrame, n_perm: int = 10000,\n                              rng_seed: int = 42) -> dict:\n    isr = df[df[\"condition\"] == \"ISR\"][\"genuine_rate\"].values\n    rand = df[df[\"condition\"] == \"RANDOM\"][\"genuine_rate\"].values\n    observed = isr.mean() - rand.mean()\n    pooled = np.concatenate([isr, rand])\n    n_isr = len(isr)\n    rng = np.random.default_rng(rng_seed)\n    count = 0\n    for _ in range(n_perm):\n        perm = rng.permutation(pooled)\n        if perm[:n_isr].mean() - perm[n_isr:].mean() >= observed:\n            count += 1\n    return {\n        \"observed_diff\": float(observed),\n        \"p_value\": count / n_perm,\n        \"n_perm\": n_perm,\n        \"isr_mean\": float(isr.mean()),\n        \"random_mean\": float(rand.mean()),\n    }\n\n\ndef mannwhitney_h7(df: pd.DataFrame) -> dict:\n    isr = df[df[\"condition\"] == \"ISR\"][\"H7_rate\"].values\n    rand = df[df[\"condition\"] == \"RANDOM\"][\"H7_rate\"].values\n    n1, n2 = len(isr), len(rand)\n    u_stat, p_value = stats.mannwhitneyu(isr, rand, alternative=\"greater\")\n    r_rb = 2.0 * u_stat / (n1 * n2) - 1.0 if n1 * n2 > 0 else np.nan\n    return {\n        \"U\": float(u_stat),\n        \"p_value\": float(p_value),\n        \"r_rank_biserial\": float(r_rb),\n        \"isr_median\": float(np.median(isr)),\n        \"random_median\": float(np.median(rand)),\n    }\n\n\ndef mannwhitney_isr_star(df: pd.DataFrame) -> dict | None:\n    isr = df[df[\"condition\"] == \"ISR\"][\"ISR_star\"].dropna().values.astype(float)\n    rand = df[df[\"condition\"] == \"RANDOM\"][\"ISR_star\"].dropna().values.astype(float)\n    if len(isr) < 2 or len(rand) < 2:\n        return None\n    n1, n2 = len(isr), len(rand)\n    u_stat, p_value = stats.mannwhitneyu(isr, rand, alternative=\"greater\")\n    r_rb = 2.0 * u_stat / (n1 * n2) - 1.0\n    return {\n        \"U\": float(u_stat),\n        \"p_value\": float(p_value),\n        \"r_rank_biserial\": float(r_rb),\n        \"isr_median\": float(np.median(isr)),\n        \"random_median\": float(np.median(rand)),\n        \"isr_mean\": float(np.mean(isr)),\n        \"random_mean\": float(np.mean(rand)),\n    }\n\n\ndef bca_bootstrap_ci(df: pd.DataFrame, metric: str, n_boot: int = 10000,\n                      rng_seed: int = 42) -> dict:\n    \"\"\"BCa 95% CI for per-condition means of a metric.\"\"\"\n    result = {}\n    for cond in [\"ISR\", \"RANDOM\"]:\n        vals = df[df[\"condition\"] == cond][metric].values\n        if len(vals) < 2:\n            result[cond] = {\"mean\": float(vals.mean()) if len(vals) else np.nan,\n                            \"ci_lo\": np.nan, \"ci_hi\": np.nan}\n            continue\n        res = stats.bootstrap(\n            (vals,), np.mean, n_resamples=n_boot,\n            confidence_level=0.95, method=\"BCa\",\n            random_state=np.random.default_rng(rng_seed),\n        )\n        result[cond] = {\n            \"mean\": float(vals.mean()),\n            \"ci_lo\": float(res.confidence_interval.low),\n            \"ci_hi\": float(res.confidence_interval.high),\n        }\n    return result\n\n\ndef bayes_factor_h7_domination(df: pd.DataFrame) -> dict:\n    \"\"\"BF10 for H7-domination rate difference (beta-binomial conjugate).\n    H0: ISR and Random share same domination rate.\n    H1: independent rates. Prior: Beta(1,1) on each.\n    \"\"\"\n    isr_sub = df[df[\"condition\"] == \"ISR\"]\n    rand_sub = df[df[\"condition\"] == \"RANDOM\"]\n    k_isr = int((isr_sub[\"H7_rate\"] >= 0.5).sum())\n    n_isr = len(isr_sub)\n    k_rand = int((rand_sub[\"H7_rate\"] >= 0.5).sum())\n    n_rand = len(rand_sub)\n    k_total = k_isr + k_rand\n    n_total = n_isr + n_rand\n\n    # log marginal under H0 (shared rate)\n    log_m_h0 = betaln(1 + k_total, 1 + n_total - k_total) - betaln(1, 1)\n    # log marginal under H1 (independent rates)\n    log_m_h1 = (betaln(1 + k_isr, 1 + n_isr - k_isr) - betaln(1, 1)\n                + betaln(1 + k_rand, 1 + n_rand - k_rand) - betaln(1, 1))\n    log_bf10 = log_m_h1 - log_m_h0\n    bf10 = float(np.exp(log_bf10))\n\n    return {\n        \"k_isr\": k_isr, \"n_isr\": n_isr,\n        \"k_rand\": k_rand, \"n_rand\": n_rand,\n        \"bf10\": bf10,\n        \"log_bf10\": float(log_bf10),\n        \"interpretation\": _interpret_bf(bf10),\n    }\n\n\ndef _interpret_bf(bf: float) -> str:\n    if bf > 100:\n        return \"extreme evidence for H1\"\n    if bf > 30:\n        return \"very strong evidence for H1\"\n    if bf > 10:\n        return \"strong evidence for H1\"\n    if bf > 3:\n        return \"moderate evidence for H1\"\n    if bf > 1:\n        return \"anecdotal evidence for H1\"\n    if bf > 1/3:\n        return \"anecdotal evidence (inconclusive)\"\n    if bf > 1/10:\n        return \"moderate evidence for H0\"\n    return \"strong evidence for H0\"\n\n\ndef condition_stats(df: pd.DataFrame) -> pd.DataFrame:\n    metrics = [\"PR\", \"H7_rate\", \"genuine_rate\", \"SNH_rate\"]\n    rows = []\n    for cond in [\"ISR\", \"RANDOM\"]:\n        sub = df[df[\"condition\"] == cond]\n        row = {\"condition\": cond, \"n_seeds\": len(sub)}\n        for m in metrics:\n            vals = sub[m].values\n            row[f\"{m}_mean\"] = vals.mean()\n            row[f\"{m}_std\"] = vals.std(ddof=1) if len(vals) > 1 else 0.0\n        isr_vals = sub[\"ISR_star\"].dropna().values.astype(float)\n        row[\"ISR_star_mean\"] = isr_vals.mean() if len(isr_vals) else np.nan\n        row[\"ISR_star_std\"] = isr_vals.std(ddof=1) if len(isr_vals) > 1 else 0.0\n        rows.append(row)\n    return pd.DataFrame(rows)\n\n\n# --- Formatting ---\n\ndef fmt_pct(val: float) -> str:\n    return f\"{val*100:.1f}\\\\%\"\n\ndef fmt_or(val: float) -> str:\n    return \"$\\\\infty$\" if np.isinf(val) else f\"{val:.2f}\"\n\ndef fmt_ci(lo: float, hi: float) -> str:\n    lo_s = f\"{lo:.2f}\" if not np.isnan(lo) else \"0\"\n    hi_s = \"$\\\\infty$\" if np.isinf(hi) or np.isnan(hi) else f\"{hi:.2f}\"\n    return f\"[{lo_s}, {hi_s}]\"\n\ndef fmt_p(p: float) -> str:\n    if p < 0.001:\n        return \"$<$0.001\"\n    return f\"{p:.3f}\"\n\ndef fmt_mean_std(mean: float, std: float, pct: bool = False) -> str:\n    if pct:\n        return f\"{mean*100:.1f} $\\\\pm$ {std*100:.1f}\\\\%\"\n    return f\"{mean:.1f} $\\\\pm$ {std:.1f}\"\n\ndef fmt_bca(bca: dict, pct: bool = False) -> str:\n    m = bca[\"mean\"]\n    lo, hi = bca[\"ci_lo\"], bca[\"ci_hi\"]\n    if pct:\n        return f\"{m*100:.1f}\\\\% [{lo*100:.1f}, {hi*100:.1f}]\"\n    return f\"{m:.1f} [{lo:.1f}, {hi:.1f}]\"\n\n\n# --- Console output ---\n\ndef print_per_seed_table(df: pd.DataFrame):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  PER-SEED RESULTS\")\n    print(\"=\" * 90)\n    cols = [\"condition\", \"seed\", \"PR\", \"H7_count\", \"H7_rate\", \"H1_count\",\n            \"H8_count\", \"genuine_count\", \"genuine_rate\", \"CI_count\", \"SNH_count\", \"SNH_rate\"]\n    fmt = df[cols].copy()\n    for c in [\"H7_rate\", \"genuine_rate\", \"SNH_rate\"]:\n        fmt[c] = fmt[c].apply(lambda v: f\"{v*100:.1f}%\")\n    print(fmt.to_string(index=False))\n\n\ndef print_condition_stats(cond_df: pd.DataFrame):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  CONDITION-LEVEL STATISTICS (mean +/- SD)\")\n    print(\"=\" * 90)\n    for _, row in cond_df.iterrows():\n        n = int(row['n_seeds'])\n        print(f\"\\n  {row['condition']} (n={n} seeds):\")\n        print(f\"    PR:           {row['PR_mean']:.1f} +/- {row['PR_std']:.1f}\")\n        print(f\"    H7 rate:      {row['H7_rate_mean']*100:.1f} +/- {row['H7_rate_std']*100:.1f}%\")\n        print(f\"    Genuine rate: {row['genuine_rate_mean']*100:.1f} +/- {row['genuine_rate_std']*100:.1f}%\")\n        print(f\"    S-NH rate:    {row['SNH_rate_mean']*100:.1f} +/- {row['SNH_rate_std']*100:.1f}%\")\n\n\ndef print_tests(fisher, perm, mw, bf, bca_h7, bca_gen):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  STATISTICAL TESTS\")\n    print(\"=\" * 90)\n\n    print(\"\\n  1. H7 Domination Fisher Exact Test (H7-dominated = H7% >= 50%)\")\n    print(f\"     ISR:    {fisher['ISR']['h7_dom']} dominated / {fisher['ISR']['n']} seeds\")\n    print(f\"     RANDOM: {fisher['RANDOM']['h7_dom']} dominated / {fisher['RANDOM']['n']} seeds\")\n    print(f\"     Contingency: {fisher['table']}\")\n    or_str = \"inf\" if np.isinf(fisher['odds_ratio']) else f\"{fisher['odds_ratio']:.4f}\"\n    print(f\"     OR = {or_str}, 95% CI = [{fisher['or_ci_lo']:.4f}, {fisher['or_ci_hi']:.4f}]\"\n          if not np.isnan(fisher['or_ci_lo']) else f\"     OR = {or_str}, 95% CI = N/A\")\n    print(f\"     p-value (one-sided, greater): {fisher['p_value']:.4f}\")\n\n    print(f\"\\n  2. Genuine Rate Permutation Test (n_perm={perm['n_perm']})\")\n    print(f\"     ISR mean:    {perm['isr_mean']*100:.2f}%\")\n    print(f\"     RANDOM mean: {perm['random_mean']*100:.2f}%\")\n    print(f\"     Diff: {perm['observed_diff']*100:.2f} pp, p = {perm['p_value']:.4f}\")\n\n    print(f\"\\n  3. H7 Rate Mann-Whitney U Test\")\n    print(f\"     ISR median:    {mw['isr_median']*100:.1f}%\")\n    print(f\"     RANDOM median: {mw['random_median']*100:.1f}%\")\n    print(f\"     U = {mw['U']:.1f}, p = {mw['p_value']:.4f}\")\n    print(f\"     Rank-biserial r = {mw['r_rank_biserial']:.4f}\")\n\n    print(f\"\\n  4. Bayes Factor (H7 Domination, Beta-Binomial)\")\n    print(f\"     ISR:    {bf['k_isr']}/{bf['n_isr']} dominated\")\n    print(f\"     RANDOM: {bf['k_rand']}/{bf['n_rand']} dominated\")\n    print(f\"     BF10 = {bf['bf10']:.4f} ({bf['interpretation']})\")\n\n    print(f\"\\n  5. BCa Bootstrap 95% CI (n_boot resamples)\")\n    for label, bca in [(\"H7 rate\", bca_h7), (\"Genuine rate\", bca_gen)]:\n        print(f\"     {label}:\")\n        for cond in [\"ISR\", \"RANDOM\"]:\n            b = bca[cond]\n            print(f\"       {cond}: {b['mean']*100:.1f}% [{b['ci_lo']*100:.1f}, {b['ci_hi']*100:.1f}]\"\n                  if not np.isnan(b['ci_lo']) else f\"       {cond}: {b['mean']*100:.1f}% [N/A]\")\n\n\n# --- Markdown generation (appendix-ready) ---\n\ndef generate_markdown(df: pd.DataFrame, cond_df: pd.DataFrame,\n                      fisher: dict, perm: dict, mw: dict,\n                      bf: dict, bca_h7: dict, bca_gen: dict) -> str:\n    L = []\n    L.append(\"## D134: ISR vs Random Statistical Analysis\\n\")\n\n    # Per-seed table\n    L.append(\"### Table A1: Per-Seed Hacking Taxonomy (4B Qwen3, 500 steps)\\n\")\n    L.append(\"| Condition | Seed | PR | H7 | H7\\\\% | H1 | H8 | Genuine | Gen\\\\% | CI | S-NH | S-NH\\\\% |\")\n    L.append(\"|:----------|-----:|---:|---:|-----:|---:|---:|--------:|------:|---:|-----:|-------:|\")\n    for _, r in df.iterrows():\n        L.append(\n            f\"| {r['condition']} | {r['seed']} | {int(r['PR'])} | {int(r['H7_count'])} | \"\n            f\"{r['H7_rate']*100:.1f} | {int(r['H1_count'])} | {int(r['H8_count'])} | \"\n            f\"{int(r['genuine_count'])} | {r['genuine_rate']*100:.1f} | {int(r['CI_count'])} | \"\n            f\"{int(r['SNH_count'])} | {r['SNH_rate']*100:.1f} |\"\n        )\n\n    # Condition summary with BCa CI\n    L.append(\"\\n### Table A2: Condition-Level Summary\\n\")\n    L.append(\"| Condition | $n$ | PR (mean$\\\\pm$SD) | H7\\\\% (mean$\\\\pm$SD) | H7\\\\% BCa 95\\\\% CI | Gen\\\\% (mean$\\\\pm$SD) | Gen\\\\% BCa 95\\\\% CI |\")\n    L.append(\"|:----------|----:|:------------------|:-------------------|:-----------------|:-------------------|:-----------------|\")\n    for _, r in cond_df.iterrows():\n        cond = r[\"condition\"]\n        h7_bca = bca_h7.get(cond, {})\n        gen_bca = bca_gen.get(cond, {})\n        h7_ci = f\"[{h7_bca['ci_lo']*100:.1f}, {h7_bca['ci_hi']*100:.1f}]\" if h7_bca and not np.isnan(h7_bca.get('ci_lo', np.nan)) else \"N/A\"\n        gen_ci = f\"[{gen_bca['ci_lo']*100:.1f}, {gen_bca['ci_hi']*100:.1f}]\" if gen_bca and not np.isnan(gen_bca.get('ci_lo', np.nan)) else \"N/A\"\n        L.append(\n            f\"| {cond} | {int(r['n_seeds'])} | \"\n            f\"{r['PR_mean']:.1f}$\\\\pm${r['PR_std']:.1f} | \"\n            f\"{r['H7_rate_mean']*100:.1f}$\\\\pm${r['H7_rate_std']*100:.1f} | \"\n            f\"{h7_ci} | \"\n            f\"{r['genuine_rate_mean']*100:.1f}$\\\\pm${r['genuine_rate_std']*100:.1f} | \"\n            f\"{gen_ci} |\"\n        )\n\n    # Statistical tests\n    if fisher and perm and mw and bf:\n        L.append(\"\\n### Statistical Tests\\n\")\n\n        # Fisher\n        or_str = \"$\\\\infty$\" if np.isinf(fisher['odds_ratio']) else f\"{fisher['odds_ratio']:.2f}\"\n        ci_lo = f\"{fisher['or_ci_lo']:.2f}\" if not np.isnan(fisher['or_ci_lo']) else \"0\"\n        ci_hi = \"$\\\\infty$\" if np.isinf(fisher.get('or_ci_hi', np.inf)) or np.isnan(fisher.get('or_ci_hi', np.nan)) else f\"{fisher['or_ci_hi']:.2f}\"\n        L.append(\"**1. H7 Domination Fisher Exact Test** (threshold: H7$\\\\geq$50\\\\% of proved)\")\n        L.append(f\"- ISR: {fisher['ISR']['h7_dom']}/{fisher['ISR']['n']} seeds H7-dominated; \"\n                 f\"Random: {fisher['RANDOM']['h7_dom']}/{fisher['RANDOM']['n']}\")\n        L.append(f\"- OR = {or_str}, 95\\\\% exact CI = [{ci_lo}, {ci_hi}], \"\n                 f\"$p$ = {fmt_p(fisher['p_value'])}\")\n        L.append(\"\")\n\n        # Permutation\n        L.append(f\"**2. Genuine Rate Permutation Test** ($n$ = {perm['n_perm']:,} permutations)\")\n        L.append(f\"- ISR mean: {perm['isr_mean']*100:.2f}\\\\%, Random mean: {perm['random_mean']*100:.2f}\\\\%\")\n        L.append(f\"- $\\\\Delta$ = {perm['observed_diff']*100:.2f} pp, $p$ = {fmt_p(perm['p_value'])}\")\n        L.append(\"\")\n\n        # Mann-Whitney\n        L.append(\"**3. H7 Rate Mann-Whitney $U$ Test**\")\n        L.append(f\"- ISR median: {mw['isr_median']*100:.1f}\\\\%, Random median: {mw['random_median']*100:.1f}\\\\%\")\n        L.append(f\"- $U$ = {mw['U']:.1f}, $p$ = {fmt_p(mw['p_value'])}, \"\n                 f\"rank-biserial $r$ = {mw['r_rank_biserial']:.3f}\")\n        L.append(\"\")\n\n        # Bayes Factor\n        L.append(\"**4. Bayes Factor** (Beta-Binomial conjugate, prior: Beta(1,1))\")\n        L.append(f\"- $BF_{{10}}$ = {bf['bf10']:.2f} ({bf['interpretation']})\")\n        L.append(f\"- ISR: {bf['k_isr']}/{bf['n_isr']} H7-dominated, \"\n                 f\"Random: {bf['k_rand']}/{bf['n_rand']}\")\n\n    return \"\\n\".join(L) + \"\\n\"\n\n\n# --- Main ---\n\ndef main():\n    args = parse_args()\n    data_dir = Path(args.data_dir)\n\n    if not data_dir.exists():\n        print(f\"ERROR: data directory {data_dir} does not exist\", file=sys.stderr)\n        sys.exit(1)\n\n    if args.prefix:\n        prefixes = [args.prefix]\n    elif args.prefixes:\n        prefixes = [p.strip() for p in args.prefixes.split(\",\")]\n    else:\n        prefixes = MODE_PREFIXES[args.mode]\n    print(f\"Mode: {args.mode} | Prefixes: {prefixes}\")\n\n    runs = discover_runs(data_dir, prefixes)\n    if not runs:\n        print(f\"ERROR: no runs found in {data_dir} with prefixes {prefixes}\", file=sys.stderr)\n        sys.exit(1)\n\n    isr_count = sum(1 for r in runs if r[\"condition\"] == \"ISR\")\n    rand_count = sum(1 for r in runs if r[\"condition\"] == \"RANDOM\")\n    print(f\"Found {len(runs)} runs: {isr_count} ISR, {rand_count} RANDOM\")\n    for r in runs:\n        print(f\"  {r['condition']:6s} s{r['seed']} <- {r['dir_name']}\")\n\n    df = build_table(runs)\n    print_per_seed_table(df)\n\n    cond_df = condition_stats(df)\n    print_condition_stats(cond_df)\n\n    if isr_count < 2 or rand_count < 2:\n        print(\"\\nWARNING: need >= 2 seeds per condition for statistical tests, skipping.\",\n              file=sys.stderr)\n        bca_h7 = bca_bootstrap_ci(df, \"H7_rate\", args.n_boot, args.seed)\n        bca_gen = bca_bootstrap_ci(df, \"genuine_rate\", args.n_boot, args.seed)\n        if args.output:\n            md = generate_markdown(df, cond_df, {}, {}, {}, {}, bca_h7, bca_gen)\n            Path(args.output).write_text(md)\n            print(f\"\\nMarkdown written to {args.output}\")\n        return\n\n    fisher = fisher_h7_domination(df)\n    perm = permutation_test_genuine(df, n_perm=args.n_perm, rng_seed=args.seed)\n    mw = mannwhitney_h7(df)\n    bf = bayes_factor_h7_domination(df)\n    bca_h7 = bca_bootstrap_ci(df, \"H7_rate\", args.n_boot, args.seed)\n    bca_gen = bca_bootstrap_ci(df, \"genuine_rate\", args.n_boot, args.seed)\n\n    print_tests(fisher, perm, mw, bf, bca_h7, bca_gen)\n\n    md = generate_markdown(df, cond_df, fisher, perm, mw, bf, bca_h7, bca_gen)\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  MARKDOWN OUTPUT (appendix-ready)\")\n    print(\"=\" * 90)\n    print(md)\n\n    if args.output:\n        Path(args.output).parent.mkdir(parents=True, exist_ok=True)\n        Path(args.output).write_text(md)\n        print(f\"Markdown written to {args.output}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 412,
        "oldLines": 10,
        "newStart": 412,
        "newLines": 12,
        "lines": [
          "     print(\"  PER-SEED RESULTS\")",
          "     print(\"=\" * 90)",
          "     cols = [\"condition\", \"seed\", \"PR\", \"H7_count\", \"H7_rate\", \"H1_count\",",
          "-            \"H8_count\", \"genuine_count\", \"genuine_rate\", \"CI_count\", \"SNH_count\", \"SNH_rate\"]",
          "+            \"H8_count\", \"genuine_count\", \"genuine_rate\", \"CI_count\", \"SNH_count\", \"SNH_rate\",",
          "+            \"ISR_star\"]",
          "     fmt = df[cols].copy()",
          "     for c in [\"H7_rate\", \"genuine_rate\", \"SNH_rate\"]:",
          "         fmt[c] = fmt[c].apply(lambda v: f\"{v*100:.1f}%\")",
          "+    fmt[\"ISR_star\"] = fmt[\"ISR_star\"].apply(lambda v: f\"{v:.4f}\" if pd.notna(v) else \"---\")",
          "     print(fmt.to_string(index=False))",
          " ",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 33_

**Edit 6**: Add ISR* to `print_condition_stats`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "52950eb6-f3be-4541-ad3f-24d51b49b5a5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P3giviDh7YoWmWUYtzTUVV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 649,
      "cache_read_input_tokens": 48106,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 649
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

<details open><summary>🔧 Tool call — Edit · `toolu_014ndUjpEG7hJTatdM7eAuhs`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/scripts/d134_analysis.py",
  "old_string": "        print(f\"    S-NH rate:    {row['SNH_rate_mean']*100:.1f} +/- {row['SNH_rate_std']*100:.1f}%\")",
  "new_string": "        print(f\"    S-NH rate:    {row['SNH_rate_mean']*100:.1f} +/- {row['SNH_rate_std']*100:.1f}%\")\n        if not np.isnan(row.get('ISR_star_mean', np.nan)):\n            print(f\"    ISR*:         {row['ISR_star_mean']:.4f} +/- {row['ISR_star_std']:.4f}\")"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "efe433ce-22be-41df-a9c8-b7f87db0706a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P3giviDh7YoWmWUYtzTUVV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 649,
      "cache_read_input_tokens": 48106,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 649
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

_source line 35 · 2026-05-18T23:32:42.847Z_

<details><summary>↩ Tool result · `toolu_014ndUjpEG7hJTatdM7eAuhs`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/scripts/d134_analysis.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "2a91058d-6ec1-41d8-99e1-ce1ce2466212",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/scripts/d134_analysis.py",
    "oldString": "        print(f\"    S-NH rate:    {row['SNH_rate_mean']*100:.1f} +/- {row['SNH_rate_std']*100:.1f}%\")",
    "newString": "        print(f\"    S-NH rate:    {row['SNH_rate_mean']*100:.1f} +/- {row['SNH_rate_std']*100:.1f}%\")\n        if not np.isnan(row.get('ISR_star_mean', np.nan)):\n            print(f\"    ISR*:         {row['ISR_star_mean']:.4f} +/- {row['ISR_star_std']:.4f}\")",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"D134 experiment analysis: multi-seed ISR vs Random, 4B GRPO training.\nReads taxonomy data from classify.json, taxonomy.json, or top-level taxonomy files.\nComputes summary stats, statistical tests (Fisher, Mann-Whitney, permutation, Bayes Factor),\nand BCa bootstrap CIs. Outputs appendix-ready markdown.\n\"\"\"\n\nimport argparse\nimport json\nimport re\nimport sys\nfrom pathlib import Path\n\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\nfrom scipy.special import betaln\n\nCONDITION_MAP = [\n    (\"d134_4b_isr\", \"ISR\"),\n    (\"d134_4b_random\", \"RANDOM\"),\n    (\"plan002_additive\", \"ISR\"),\n    (\"plan018_additive_random\", \"RANDOM\"),\n    (\"plan018_random\", \"RANDOM\"),\n]\n\nMODE_PREFIXES = {\n    \"d134_only\": [\"d134_4b\"],\n    \"all\": [\"d134_4b\", \"plan002_additive_b01\", \"plan018_additive_random_b01\", \"plan018_random\"],\n}\n\n\ndef parse_args():\n    p = argparse.ArgumentParser(description=\"D134 multi-seed analysis and statistical tests\")\n    p.add_argument(\"--data_dir\", type=str, default=\"/root/autodl-tmp/outputs\",\n                   help=\"Directory containing experiment outputs\")\n    p.add_argument(\"--mode\", type=str, default=\"d134_only\", choices=list(MODE_PREFIXES),\n                   help=\"d134_only = matched 5+5 design (default); all = include original seeds\")\n    p.add_argument(\"--prefix\", type=str, default=None,\n                   help=\"(Legacy) Single prefix filter; overrides mode/prefixes\")\n    p.add_argument(\"--prefixes\", type=str, default=None,\n                   help=\"Comma-separated prefixes; overrides --mode\")\n    p.add_argument(\"--output\", type=str, default=None,\n                   help=\"Write markdown summary to this file\")\n    p.add_argument(\"--n_perm\", type=int, default=10000,\n                   help=\"Number of permutations for permutation test\")\n    p.add_argument(\"--n_boot\", type=int, default=10000,\n                   help=\"Number of bootstrap resamples for BCa CI\")\n    p.add_argument(\"--seed\", type=int, default=42,\n                   help=\"Random seed for permutation/bootstrap\")\n    return p.parse_args()\n\n\n# --- Data loading ---\n\ndef match_condition(name: str) -> str | None:\n    best_prefix = \"\"\n    best_cond = None\n    for prefix, cond in CONDITION_MAP:\n        if name.startswith(prefix) and len(prefix) > len(best_prefix):\n            best_prefix = prefix\n            best_cond = cond\n    return best_cond\n\n\ndef extract_seed(name: str) -> int | None:\n    m = re.search(r'_s(\\d+)', name)\n    return int(m.group(1)) if m else None\n\n\ndef load_eval_results(path: Path) -> dict | None:\n    if not path.exists():\n        return None\n    with open(path) as f:\n        data = json.load(f)\n    if \"eval_results\" in data:\n        return data[\"eval_results\"]\n    return data\n\n\ndef load_taxonomy_unified(path: Path) -> dict | None:\n    with open(path) as f:\n        raw = json.load(f)\n    t = raw.get(\"taxonomy\", {})\n    proved = t.get(\"proved\", 0)\n    if proved == 0:\n        return None\n    h7 = t.get(\"H7\", 0)\n    h1 = t.get(\"H1_exact\", 0)\n    h8 = t.get(\"H8\", 0)\n    genuine = t.get(\"genuine\", 0)\n    return {\n        \"n_total\": 100, \"n_proved\": proved,\n        \"h7_total_count\": h7, \"h7_total_rate\": h7 / proved,\n        \"h1_strict_count\": h1, \"h8_conjunction_collapse_count\": h8,\n        \"genuine_count\": genuine, \"genuine_rate\": genuine / proved,\n        \"content_independent_count\": 0,\n    }\n\n\ndef load_taxonomy_verification(path: Path) -> dict | None:\n    with open(path) as f:\n        raw = json.load(f)\n    proved = raw.get(\"proved\", 0)\n    if proved == 0:\n        return None\n    tax = raw.get(\"taxonomy\", {})\n    h7 = tax.get(\"h7\", {}).get(\"count\", 0)\n    h1 = tax.get(\"h1_exact\", {}).get(\"count\", 0)\n    h8 = tax.get(\"h8\", {}).get(\"count\", 0)\n    genuine = tax.get(\"genuine\", {}).get(\"count\", 0)\n    return {\n        \"n_total\": raw.get(\"total\", 100), \"n_proved\": proved,\n        \"h7_total_count\": h7, \"h7_total_rate\": h7 / proved,\n        \"h1_strict_count\": h1, \"h8_conjunction_collapse_count\": h8,\n        \"genuine_count\": genuine, \"genuine_rate\": genuine / proved,\n        \"content_independent_count\": 0,\n    }\n\n\ndef discover_runs(data_dir: Path, prefixes: list[str]) -> list[dict]:\n    runs = []\n    seen = set()\n    for entry in sorted(data_dir.iterdir()):\n        name = entry.name\n        if not any(name.startswith(p) for p in prefixes):\n            continue\n        cond = match_condition(name)\n        seed_val = extract_seed(name)\n        if cond is None or seed_val is None:\n            continue\n        key = (cond, seed_val)\n        if key in seen:\n            continue\n        data = None\n        if entry.is_dir():\n            for fname in [\"classify.json\", \"taxonomy.json\"]:\n                data = load_eval_results(entry / fname)\n                if data is not None:\n                    break\n            if data is None:\n                continue\n        elif entry.is_file():\n            if name.endswith(\"_taxonomy_unified.json\"):\n                data = load_taxonomy_unified(entry)\n            elif name.endswith(\"_taxonomy_verification.json\"):\n                data = load_taxonomy_verification(entry)\n            if data is None:\n                continue\n        else:\n            continue\n        seen.add(key)\n        isr_star = None\n        if entry.is_dir():\n            eval_path = entry / \"eval_results.json\"\n            if eval_path.exists():\n                with open(eval_path) as ef:\n                    eval_raw = json.load(ef)\n                isr_star = eval_raw.get(\"summary\", {}).get(\"proved_only_mean_isr\")\n        runs.append({\"dir_name\": name, \"seed\": seed_val, \"condition\": cond,\n                      \"data\": data, \"isr_star\": isr_star})\n    return runs\n\n\ndef compute_row(run: dict) -> dict:\n    d = run[\"data\"]\n    n_proved = d.get(\"n_proved\", 0)\n    n_total = d.get(\"n_total\", 100)\n    h7 = d.get(\"h7_total_count\", 0)\n    h7_rate = d.get(\"h7_total_rate\", h7 / n_proved if n_proved > 0 else 0.0)\n    h1 = d.get(\"h1_strict_count\", 0)\n    h8 = d.get(\"h8_conjunction_collapse_count\", 0)\n    genuine = d.get(\"genuine_count\", 0)\n    genuine_rate = d.get(\"genuine_rate\", genuine / n_proved if n_proved > 0 else 0.0)\n    ci = d.get(\"content_independent_count\", 0)\n    snh = max(genuine - ci, 0)\n    snh_rate = snh / n_proved if n_proved > 0 else 0.0\n    return {\n        \"seed\": run[\"seed\"], \"condition\": run[\"condition\"], \"n_total\": n_total,\n        \"PR\": n_proved, \"H7_count\": h7, \"H7_rate\": h7_rate,\n        \"H1_count\": h1, \"H8_count\": h8,\n        \"genuine_count\": genuine, \"genuine_rate\": genuine_rate,\n        \"CI_count\": ci, \"SNH_count\": snh, \"SNH_rate\": snh_rate,\n        \"ISR_star\": run.get(\"isr_star\"),\n    }\n\n\ndef build_table(runs: list[dict]) -> pd.DataFrame:\n    rows = [compute_row(r) for r in runs]\n    df = pd.DataFrame(rows)\n    df = df.sort_values([\"condition\", \"seed\"]).reset_index(drop=True)\n    return df\n\n\n# --- Statistical tests ---\n\ndef fisher_h7_domination(df: pd.DataFrame) -> dict:\n    results = {}\n    for cond in [\"ISR\", \"RANDOM\"]:\n        sub = df[df[\"condition\"] == cond]\n        results[cond] = {\n            \"n\": len(sub),\n            \"h7_dom\": int((sub[\"H7_rate\"] >= 0.5).sum()),\n            \"not_h7_dom\": int((sub[\"H7_rate\"] < 0.5).sum()),\n        }\n    table = np.array([\n        [results[\"ISR\"][\"h7_dom\"], results[\"ISR\"][\"not_h7_dom\"]],\n        [results[\"RANDOM\"][\"h7_dom\"], results[\"RANDOM\"][\"not_h7_dom\"]],\n    ])\n    odds_ratio, p_value = stats.fisher_exact(table, alternative=\"greater\")\n\n    # 95% exact CI via scipy.stats.contingency\n    or_ci_lo, or_ci_hi = np.nan, np.nan\n    try:\n        ct = stats.contingency.odds_ratio(table)\n        ci = ct.confidence_interval(confidence_level=0.95)\n        or_ci_lo, or_ci_hi = ci.low, ci.high\n    except Exception:\n        pass\n\n    return {\n        \"table\": table.tolist(),\n        \"ISR\": results[\"ISR\"],\n        \"RANDOM\": results[\"RANDOM\"],\n        \"odds_ratio\": odds_ratio,\n        \"or_ci_lo\": or_ci_lo,\n        \"or_ci_hi\": or_ci_hi,\n        \"p_value\": p_value,\n    }\n\n\ndef permutation_test_genuine(df: pd.DataFrame, n_perm: int = 10000,\n                              rng_seed: int = 42) -> dict:\n    isr = df[df[\"condition\"] == \"ISR\"][\"genuine_rate\"].values\n    rand = df[df[\"condition\"] == \"RANDOM\"][\"genuine_rate\"].values\n    observed = isr.mean() - rand.mean()\n    pooled = np.concatenate([isr, rand])\n    n_isr = len(isr)\n    rng = np.random.default_rng(rng_seed)\n    count = 0\n    for _ in range(n_perm):\n        perm = rng.permutation(pooled)\n        if perm[:n_isr].mean() - perm[n_isr:].mean() >= observed:\n            count += 1\n    return {\n        \"observed_diff\": float(observed),\n        \"p_value\": count / n_perm,\n        \"n_perm\": n_perm,\n        \"isr_mean\": float(isr.mean()),\n        \"random_mean\": float(rand.mean()),\n    }\n\n\ndef mannwhitney_h7(df: pd.DataFrame) -> dict:\n    isr = df[df[\"condition\"] == \"ISR\"][\"H7_rate\"].values\n    rand = df[df[\"condition\"] == \"RANDOM\"][\"H7_rate\"].values\n    n1, n2 = len(isr), len(rand)\n    u_stat, p_value = stats.mannwhitneyu(isr, rand, alternative=\"greater\")\n    r_rb = 2.0 * u_stat / (n1 * n2) - 1.0 if n1 * n2 > 0 else np.nan\n    return {\n        \"U\": float(u_stat),\n        \"p_value\": float(p_value),\n        \"r_rank_biserial\": float(r_rb),\n        \"isr_median\": float(np.median(isr)),\n        \"random_median\": float(np.median(rand)),\n    }\n\n\ndef mannwhitney_isr_star(df: pd.DataFrame) -> dict | None:\n    isr = df[df[\"condition\"] == \"ISR\"][\"ISR_star\"].dropna().values.astype(float)\n    rand = df[df[\"condition\"] == \"RANDOM\"][\"ISR_star\"].dropna().values.astype(float)\n    if len(isr) < 2 or len(rand) < 2:\n        return None\n    n1, n2 = len(isr), len(rand)\n    u_stat, p_value = stats.mannwhitneyu(isr, rand, alternative=\"greater\")\n    r_rb = 2.0 * u_stat / (n1 * n2) - 1.0\n    return {\n        \"U\": float(u_stat),\n        \"p_value\": float(p_value),\n        \"r_rank_biserial\": float(r_rb),\n        \"isr_median\": float(np.median(isr)),\n        \"random_median\": float(np.median(rand)),\n        \"isr_mean\": float(np.mean(isr)),\n        \"random_mean\": float(np.mean(rand)),\n    }\n\n\ndef bca_bootstrap_ci(df: pd.DataFrame, metric: str, n_boot: int = 10000,\n                      rng_seed: int = 42) -> dict:\n    \"\"\"BCa 95% CI for per-condition means of a metric.\"\"\"\n    result = {}\n    for cond in [\"ISR\", \"RANDOM\"]:\n        vals = df[df[\"condition\"] == cond][metric].values\n        if len(vals) < 2:\n            result[cond] = {\"mean\": float(vals.mean()) if len(vals) else np.nan,\n                            \"ci_lo\": np.nan, \"ci_hi\": np.nan}\n            continue\n        res = stats.bootstrap(\n            (vals,), np.mean, n_resamples=n_boot,\n            confidence_level=0.95, method=\"BCa\",\n            random_state=np.random.default_rng(rng_seed),\n        )\n        result[cond] = {\n            \"mean\": float(vals.mean()),\n            \"ci_lo\": float(res.confidence_interval.low),\n            \"ci_hi\": float(res.confidence_interval.high),\n        }\n    return result\n\n\ndef bayes_factor_h7_domination(df: pd.DataFrame) -> dict:\n    \"\"\"BF10 for H7-domination rate difference (beta-binomial conjugate).\n    H0: ISR and Random share same domination rate.\n    H1: independent rates. Prior: Beta(1,1) on each.\n    \"\"\"\n    isr_sub = df[df[\"condition\"] == \"ISR\"]\n    rand_sub = df[df[\"condition\"] == \"RANDOM\"]\n    k_isr = int((isr_sub[\"H7_rate\"] >= 0.5).sum())\n    n_isr = len(isr_sub)\n    k_rand = int((rand_sub[\"H7_rate\"] >= 0.5).sum())\n    n_rand = len(rand_sub)\n    k_total = k_isr + k_rand\n    n_total = n_isr + n_rand\n\n    # log marginal under H0 (shared rate)\n    log_m_h0 = betaln(1 + k_total, 1 + n_total - k_total) - betaln(1, 1)\n    # log marginal under H1 (independent rates)\n    log_m_h1 = (betaln(1 + k_isr, 1 + n_isr - k_isr) - betaln(1, 1)\n                + betaln(1 + k_rand, 1 + n_rand - k_rand) - betaln(1, 1))\n    log_bf10 = log_m_h1 - log_m_h0\n    bf10 = float(np.exp(log_bf10))\n\n    return {\n        \"k_isr\": k_isr, \"n_isr\": n_isr,\n        \"k_rand\": k_rand, \"n_rand\": n_rand,\n        \"bf10\": bf10,\n        \"log_bf10\": float(log_bf10),\n        \"interpretation\": _interpret_bf(bf10),\n    }\n\n\ndef _interpret_bf(bf: float) -> str:\n    if bf > 100:\n        return \"extreme evidence for H1\"\n    if bf > 30:\n        return \"very strong evidence for H1\"\n    if bf > 10:\n        return \"strong evidence for H1\"\n    if bf > 3:\n        return \"moderate evidence for H1\"\n    if bf > 1:\n        return \"anecdotal evidence for H1\"\n    if bf > 1/3:\n        return \"anecdotal evidence (inconclusive)\"\n    if bf > 1/10:\n        return \"moderate evidence for H0\"\n    return \"strong evidence for H0\"\n\n\ndef condition_stats(df: pd.DataFrame) -> pd.DataFrame:\n    metrics = [\"PR\", \"H7_rate\", \"genuine_rate\", \"SNH_rate\"]\n    rows = []\n    for cond in [\"ISR\", \"RANDOM\"]:\n        sub = df[df[\"condition\"] == cond]\n        row = {\"condition\": cond, \"n_seeds\": len(sub)}\n        for m in metrics:\n            vals = sub[m].values\n            row[f\"{m}_mean\"] = vals.mean()\n            row[f\"{m}_std\"] = vals.std(ddof=1) if len(vals) > 1 else 0.0\n        isr_vals = sub[\"ISR_star\"].dropna().values.astype(float)\n        row[\"ISR_star_mean\"] = isr_vals.mean() if len(isr_vals) else np.nan\n        row[\"ISR_star_std\"] = isr_vals.std(ddof=1) if len(isr_vals) > 1 else 0.0\n        rows.append(row)\n    return pd.DataFrame(rows)\n\n\n# --- Formatting ---\n\ndef fmt_pct(val: float) -> str:\n    return f\"{val*100:.1f}\\\\%\"\n\ndef fmt_or(val: float) -> str:\n    return \"$\\\\infty$\" if np.isinf(val) else f\"{val:.2f}\"\n\ndef fmt_ci(lo: float, hi: float) -> str:\n    lo_s = f\"{lo:.2f}\" if not np.isnan(lo) else \"0\"\n    hi_s = \"$\\\\infty$\" if np.isinf(hi) or np.isnan(hi) else f\"{hi:.2f}\"\n    return f\"[{lo_s}, {hi_s}]\"\n\ndef fmt_p(p: float) -> str:\n    if p < 0.001:\n        return \"$<$0.001\"\n    return f\"{p:.3f}\"\n\ndef fmt_mean_std(mean: float, std: float, pct: bool = False) -> str:\n    if pct:\n        return f\"{mean*100:.1f} $\\\\pm$ {std*100:.1f}\\\\%\"\n    return f\"{mean:.1f} $\\\\pm$ {std:.1f}\"\n\ndef fmt_bca(bca: dict, pct: bool = False) -> str:\n    m = bca[\"mean\"]\n    lo, hi = bca[\"ci_lo\"], bca[\"ci_hi\"]\n    if pct:\n        return f\"{m*100:.1f}\\\\% [{lo*100:.1f}, {hi*100:.1f}]\"\n    return f\"{m:.1f} [{lo:.1f}, {hi:.1f}]\"\n\n\n# --- Console output ---\n\ndef print_per_seed_table(df: pd.DataFrame):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  PER-SEED RESULTS\")\n    print(\"=\" * 90)\n    cols = [\"condition\", \"seed\", \"PR\", \"H7_count\", \"H7_rate\", \"H1_count\",\n            \"H8_count\", \"genuine_count\", \"genuine_rate\", \"CI_count\", \"SNH_count\", \"SNH_rate\",\n            \"ISR_star\"]\n    fmt = df[cols].copy()\n    for c in [\"H7_rate\", \"genuine_rate\", \"SNH_rate\"]:\n        fmt[c] = fmt[c].apply(lambda v: f\"{v*100:.1f}%\")\n    fmt[\"ISR_star\"] = fmt[\"ISR_star\"].apply(lambda v: f\"{v:.4f}\" if pd.notna(v) else \"---\")\n    print(fmt.to_string(index=False))\n\n\ndef print_condition_stats(cond_df: pd.DataFrame):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  CONDITION-LEVEL STATISTICS (mean +/- SD)\")\n    print(\"=\" * 90)\n    for _, row in cond_df.iterrows():\n        n = int(row['n_seeds'])\n        print(f\"\\n  {row['condition']} (n={n} seeds):\")\n        print(f\"    PR:           {row['PR_mean']:.1f} +/- {row['PR_std']:.1f}\")\n        print(f\"    H7 rate:      {row['H7_rate_mean']*100:.1f} +/- {row['H7_rate_std']*100:.1f}%\")\n        print(f\"    Genuine rate: {row['genuine_rate_mean']*100:.1f} +/- {row['genuine_rate_std']*100:.1f}%\")\n        print(f\"    S-NH rate:    {row['SNH_rate_mean']*100:.1f} +/- {row['SNH_rate_std']*100:.1f}%\")\n\n\ndef print_tests(fisher, perm, mw, bf, bca_h7, bca_gen):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  STATISTICAL TESTS\")\n    print(\"=\" * 90)\n\n    print(\"\\n  1. H7 Domination Fisher Exact Test (H7-dominated = H7% >= 50%)\")\n    print(f\"     ISR:    {fisher['ISR']['h7_dom']} dominated / {fisher['ISR']['n']} seeds\")\n    print(f\"     RANDOM: {fisher['RANDOM']['h7_dom']} dominated / {fisher['RANDOM']['n']} seeds\")\n    print(f\"     Contingency: {fisher['table']}\")\n    or_str = \"inf\" if np.isinf(fisher['odds_ratio']) else f\"{fisher['odds_ratio']:.4f}\"\n    print(f\"     OR = {or_str}, 95% CI = [{fisher['or_ci_lo']:.4f}, {fisher['or_ci_hi']:.4f}]\"\n          if not np.isnan(fisher['or_ci_lo']) else f\"     OR = {or_str}, 95% CI = N/A\")\n    print(f\"     p-value (one-sided, greater): {fisher['p_value']:.4f}\")\n\n    print(f\"\\n  2. Genuine Rate Permutation Test (n_perm={perm['n_perm']})\")\n    print(f\"     ISR mean:    {perm['isr_mean']*100:.2f}%\")\n    print(f\"     RANDOM mean: {perm['random_mean']*100:.2f}%\")\n    print(f\"     Diff: {perm['observed_diff']*100:.2f} pp, p = {perm['p_value']:.4f}\")\n\n    print(f\"\\n  3. H7 Rate Mann-Whitney U Test\")\n    print(f\"     ISR median:    {mw['isr_median']*100:.1f}%\")\n    print(f\"     RANDOM median: {mw['random_median']*100:.1f}%\")\n    print(f\"     U = {mw['U']:.1f}, p = {mw['p_value']:.4f}\")\n    print(f\"     Rank-biserial r = {mw['r_rank_biserial']:.4f}\")\n\n    print(f\"\\n  4. Bayes Factor (H7 Domination, Beta-Binomial)\")\n    print(f\"     ISR:    {bf['k_isr']}/{bf['n_isr']} dominated\")\n    print(f\"     RANDOM: {bf['k_rand']}/{bf['n_rand']} dominated\")\n    print(f\"     BF10 = {bf['bf10']:.4f} ({bf['interpretation']})\")\n\n    print(f\"\\n  5. BCa Bootstrap 95% CI (n_boot resamples)\")\n    for label, bca in [(\"H7 rate\", bca_h7), (\"Genuine rate\", bca_gen)]:\n        print(f\"     {label}:\")\n        for cond in [\"ISR\", \"RANDOM\"]:\n            b = bca[cond]\n            print(f\"       {cond}: {b['mean']*100:.1f}% [{b['ci_lo']*100:.1f}, {b['ci_hi']*100:.1f}]\"\n                  if not np.isnan(b['ci_lo']) else f\"       {cond}: {b['mean']*100:.1f}% [N/A]\")\n\n\n# --- Markdown generation (appendix-ready) ---\n\ndef generate_markdown(df: pd.DataFrame, cond_df: pd.DataFrame,\n                      fisher: dict, perm: dict, mw: dict,\n                      bf: dict, bca_h7: dict, bca_gen: dict) -> str:\n    L = []\n    L.append(\"## D134: ISR vs Random Statistical Analysis\\n\")\n\n    # Per-seed table\n    L.append(\"### Table A1: Per-Seed Hacking Taxonomy (4B Qwen3, 500 steps)\\n\")\n    L.append(\"| Condition | Seed | PR | H7 | H7\\\\% | H1 | H8 | Genuine | Gen\\\\% | CI | S-NH | S-NH\\\\% |\")\n    L.append(\"|:----------|-----:|---:|---:|-----:|---:|---:|--------:|------:|---:|-----:|-------:|\")\n    for _, r in df.iterrows():\n        L.append(\n            f\"| {r['condition']} | {r['seed']} | {int(r['PR'])} | {int(r['H7_count'])} | \"\n            f\"{r['H7_rate']*100:.1f} | {int(r['H1_count'])} | {int(r['H8_count'])} | \"\n            f\"{int(r['genuine_count'])} | {r['genuine_rate']*100:.1f} | {int(r['CI_count'])} | \"\n            f\"{int(r['SNH_count'])} | {r['SNH_rate']*100:.1f} |\"\n        )\n\n    # Condition summary with BCa CI\n    L.append(\"\\n### Table A2: Condition-Level Summary\\n\")\n    L.append(\"| Condition | $n$ | PR (mean$\\\\pm$SD) | H7\\\\% (mean$\\\\pm$SD) | H7\\\\% BCa 95\\\\% CI | Gen\\\\% (mean$\\\\pm$SD) | Gen\\\\% BCa 95\\\\% CI |\")\n    L.append(\"|:----------|----:|:------------------|:-------------------|:-----------------|:-------------------|:-----------------|\")\n    for _, r in cond_df.iterrows():\n        cond = r[\"condition\"]\n        h7_bca = bca_h7.get(cond, {})\n        gen_bca = bca_gen.get(cond, {})\n        h7_ci = f\"[{h7_bca['ci_lo']*100:.1f}, {h7_bca['ci_hi']*100:.1f}]\" if h7_bca and not np.isnan(h7_bca.get('ci_lo', np.nan)) else \"N/A\"\n        gen_ci = f\"[{gen_bca['ci_lo']*100:.1f}, {gen_bca['ci_hi']*100:.1f}]\" if gen_bca and not np.isnan(gen_bca.get('ci_lo', np.nan)) else \"N/A\"\n        L.append(\n            f\"| {cond} | {int(r['n_seeds'])} | \"\n            f\"{r['PR_mean']:.1f}$\\\\pm${r['PR_std']:.1f} | \"\n            f\"{r['H7_rate_mean']*100:.1f}$\\\\pm${r['H7_rate_std']*100:.1f} | \"\n            f\"{h7_ci} | \"\n            f\"{r['genuine_rate_mean']*100:.1f}$\\\\pm${r['genuine_rate_std']*100:.1f} | \"\n            f\"{gen_ci} |\"\n        )\n\n    # Statistical tests\n    if fisher and perm and mw and bf:\n        L.append(\"\\n### Statistical Tests\\n\")\n\n        # Fisher\n        or_str = \"$\\\\infty$\" if np.isinf(fisher['odds_ratio']) else f\"{fisher['odds_ratio']:.2f}\"\n        ci_lo = f\"{fisher['or_ci_lo']:.2f}\" if not np.isnan(fisher['or_ci_lo']) else \"0\"\n        ci_hi = \"$\\\\infty$\" if np.isinf(fisher.get('or_ci_hi', np.inf)) or np.isnan(fisher.get('or_ci_hi', np.nan)) else f\"{fisher['or_ci_hi']:.2f}\"\n        L.append(\"**1. H7 Domination Fisher Exact Test** (threshold: H7$\\\\geq$50\\\\% of proved)\")\n        L.append(f\"- ISR: {fisher['ISR']['h7_dom']}/{fisher['ISR']['n']} seeds H7-dominated; \"\n                 f\"Random: {fisher['RANDOM']['h7_dom']}/{fisher['RANDOM']['n']}\")\n        L.append(f\"- OR = {or_str}, 95\\\\% exact CI = [{ci_lo}, {ci_hi}], \"\n                 f\"$p$ = {fmt_p(fisher['p_value'])}\")\n        L.append(\"\")\n\n        # Permutation\n        L.append(f\"**2. Genuine Rate Permutation Test** ($n$ = {perm['n_perm']:,} permutations)\")\n        L.append(f\"- ISR mean: {perm['isr_mean']*100:.2f}\\\\%, Random mean: {perm['random_mean']*100:.2f}\\\\%\")\n        L.append(f\"- $\\\\Delta$ = {perm['observed_diff']*100:.2f} pp, $p$ = {fmt_p(perm['p_value'])}\")\n        L.append(\"\")\n\n        # Mann-Whitney\n        L.append(\"**3. H7 Rate Mann-Whitney $U$ Test**\")\n        L.append(f\"- ISR median: {mw['isr_median']*100:.1f}\\\\%, Random median: {mw['random_median']*100:.1f}\\\\%\")\n        L.append(f\"- $U$ = {mw['U']:.1f}, $p$ = {fmt_p(mw['p_value'])}, \"\n                 f\"rank-biserial $r$ = {mw['r_rank_biserial']:.3f}\")\n        L.append(\"\")\n\n        # Bayes Factor\n        L.append(\"**4. Bayes Factor** (Beta-Binomial conjugate, prior: Beta(1,1))\")\n        L.append(f\"- $BF_{{10}}$ = {bf['bf10']:.2f} ({bf['interpretation']})\")\n        L.append(f\"- ISR: {bf['k_isr']}/{bf['n_isr']} H7-dominated, \"\n                 f\"Random: {bf['k_rand']}/{bf['n_rand']}\")\n\n    return \"\\n\".join(L) + \"\\n\"\n\n\n# --- Main ---\n\ndef main():\n    args = parse_args()\n    data_dir = Path(args.data_dir)\n\n    if not data_dir.exists():\n        print(f\"ERROR: data directory {data_dir} does not exist\", file=sys.stderr)\n        sys.exit(1)\n\n    if args.prefix:\n        prefixes = [args.prefix]\n    elif args.prefixes:\n        prefixes = [p.strip() for p in args.prefixes.split(\",\")]\n    else:\n        prefixes = MODE_PREFIXES[args.mode]\n    print(f\"Mode: {args.mode} | Prefixes: {prefixes}\")\n\n    runs = discover_runs(data_dir, prefixes)\n    if not runs:\n        print(f\"ERROR: no runs found in {data_dir} with prefixes {prefixes}\", file=sys.stderr)\n        sys.exit(1)\n\n    isr_count = sum(1 for r in runs if r[\"condition\"] == \"ISR\")\n    rand_count = sum(1 for r in runs if r[\"condition\"] == \"RANDOM\")\n    print(f\"Found {len(runs)} runs: {isr_count} ISR, {rand_count} RANDOM\")\n    for r in runs:\n        print(f\"  {r['condition']:6s} s{r['seed']} <- {r['dir_name']}\")\n\n    df = build_table(runs)\n    print_per_seed_table(df)\n\n    cond_df = condition_stats(df)\n    print_condition_stats(cond_df)\n\n    if isr_count < 2 or rand_count < 2:\n        print(\"\\nWARNING: need >= 2 seeds per condition for statistical tests, skipping.\",\n              file=sys.stderr)\n        bca_h7 = bca_bootstrap_ci(df, \"H7_rate\", args.n_boot, args.seed)\n        bca_gen = bca_bootstrap_ci(df, \"genuine_rate\", args.n_boot, args.seed)\n        if args.output:\n            md = generate_markdown(df, cond_df, {}, {}, {}, {}, bca_h7, bca_gen)\n            Path(args.output).write_text(md)\n            print(f\"\\nMarkdown written to {args.output}\")\n        return\n\n    fisher = fisher_h7_domination(df)\n    perm = permutation_test_genuine(df, n_perm=args.n_perm, rng_seed=args.seed)\n    mw = mannwhitney_h7(df)\n    bf = bayes_factor_h7_domination(df)\n    bca_h7 = bca_bootstrap_ci(df, \"H7_rate\", args.n_boot, args.seed)\n    bca_gen = bca_bootstrap_ci(df, \"genuine_rate\", args.n_boot, args.seed)\n\n    print_tests(fisher, perm, mw, bf, bca_h7, bca_gen)\n\n    md = generate_markdown(df, cond_df, fisher, perm, mw, bf, bca_h7, bca_gen)\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  MARKDOWN OUTPUT (appendix-ready)\")\n    print(\"=\" * 90)\n    print(md)\n\n    if args.output:\n        Path(args.output).parent.mkdir(parents=True, exist_ok=True)\n        Path(args.output).write_text(md)\n        print(f\"Markdown written to {args.output}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 432,
        "oldLines": 6,
        "newStart": 432,
        "newLines": 8,
        "lines": [
          "         print(f\"    H7 rate:      {row['H7_rate_mean']*100:.1f} +/- {row['H7_rate_std']*100:.1f}%\")",
          "         print(f\"    Genuine rate: {row['genuine_rate_mean']*100:.1f} +/- {row['genuine_rate_std']*100:.1f}%\")",
          "         print(f\"    S-NH rate:    {row['SNH_rate_mean']*100:.1f} +/- {row['SNH_rate_std']*100:.1f}%\")",
          "+        if not np.isnan(row.get('ISR_star_mean', np.nan)):",
          "+            print(f\"    ISR*:         {row['ISR_star_mean']:.4f} +/- {row['ISR_star_std']:.4f}\")",
          " ",
          " ",
          " def print_tests(fisher, perm, mw, bf, bca_h7, bca_gen):"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 36_

**Edit 7**: Update `print_tests` signature and add ISR* MW section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "5faa5a46-8af5-46f1-82f2-7a31acb53804",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dk6q3YJLgGG2gaj5eQCkyZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 382,
      "cache_read_input_tokens": 48755,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 382
      },
      "output_tokens": 6,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Edit · `toolu_01QuA6o2xFTGxBKGXZ2VvaAM`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/scripts/d134_analysis.py",
  "old_string": "def print_tests(fisher, perm, mw, bf, bca_h7, bca_gen):",
  "new_string": "def print_tests(fisher, perm, mw, bf, bca_h7, bca_gen, mw_isr_star=None):"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "f362228c-c87d-448d-92b6-0c5ae0dfdd16",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dk6q3YJLgGG2gaj5eQCkyZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 382,
      "cache_read_input_tokens": 48755,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 382
      },
      "output_tokens": 6,
      "service_tier": "standard",
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

_source line 38 · 2026-05-18T23:32:47.453Z_

<details><summary>↩ Tool result · `toolu_01QuA6o2xFTGxBKGXZ2VvaAM`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/scripts/d134_analysis.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "aad30525-06d5-4c32-ad5a-6af25bb5c0c8",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/scripts/d134_analysis.py",
    "oldString": "def print_tests(fisher, perm, mw, bf, bca_h7, bca_gen):",
    "newString": "def print_tests(fisher, perm, mw, bf, bca_h7, bca_gen, mw_isr_star=None):",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"D134 experiment analysis: multi-seed ISR vs Random, 4B GRPO training.\nReads taxonomy data from classify.json, taxonomy.json, or top-level taxonomy files.\nComputes summary stats, statistical tests (Fisher, Mann-Whitney, permutation, Bayes Factor),\nand BCa bootstrap CIs. Outputs appendix-ready markdown.\n\"\"\"\n\nimport argparse\nimport json\nimport re\nimport sys\nfrom pathlib import Path\n\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\nfrom scipy.special import betaln\n\nCONDITION_MAP = [\n    (\"d134_4b_isr\", \"ISR\"),\n    (\"d134_4b_random\", \"RANDOM\"),\n    (\"plan002_additive\", \"ISR\"),\n    (\"plan018_additive_random\", \"RANDOM\"),\n    (\"plan018_random\", \"RANDOM\"),\n]\n\nMODE_PREFIXES = {\n    \"d134_only\": [\"d134_4b\"],\n    \"all\": [\"d134_4b\", \"plan002_additive_b01\", \"plan018_additive_random_b01\", \"plan018_random\"],\n}\n\n\ndef parse_args():\n    p = argparse.ArgumentParser(description=\"D134 multi-seed analysis and statistical tests\")\n    p.add_argument(\"--data_dir\", type=str, default=\"/root/autodl-tmp/outputs\",\n                   help=\"Directory containing experiment outputs\")\n    p.add_argument(\"--mode\", type=str, default=\"d134_only\", choices=list(MODE_PREFIXES),\n                   help=\"d134_only = matched 5+5 design (default); all = include original seeds\")\n    p.add_argument(\"--prefix\", type=str, default=None,\n                   help=\"(Legacy) Single prefix filter; overrides mode/prefixes\")\n    p.add_argument(\"--prefixes\", type=str, default=None,\n                   help=\"Comma-separated prefixes; overrides --mode\")\n    p.add_argument(\"--output\", type=str, default=None,\n                   help=\"Write markdown summary to this file\")\n    p.add_argument(\"--n_perm\", type=int, default=10000,\n                   help=\"Number of permutations for permutation test\")\n    p.add_argument(\"--n_boot\", type=int, default=10000,\n                   help=\"Number of bootstrap resamples for BCa CI\")\n    p.add_argument(\"--seed\", type=int, default=42,\n                   help=\"Random seed for permutation/bootstrap\")\n    return p.parse_args()\n\n\n# --- Data loading ---\n\ndef match_condition(name: str) -> str | None:\n    best_prefix = \"\"\n    best_cond = None\n    for prefix, cond in CONDITION_MAP:\n        if name.startswith(prefix) and len(prefix) > len(best_prefix):\n            best_prefix = prefix\n            best_cond = cond\n    return best_cond\n\n\ndef extract_seed(name: str) -> int | None:\n    m = re.search(r'_s(\\d+)', name)\n    return int(m.group(1)) if m else None\n\n\ndef load_eval_results(path: Path) -> dict | None:\n    if not path.exists():\n        return None\n    with open(path) as f:\n        data = json.load(f)\n    if \"eval_results\" in data:\n        return data[\"eval_results\"]\n    return data\n\n\ndef load_taxonomy_unified(path: Path) -> dict | None:\n    with open(path) as f:\n        raw = json.load(f)\n    t = raw.get(\"taxonomy\", {})\n    proved = t.get(\"proved\", 0)\n    if proved == 0:\n        return None\n    h7 = t.get(\"H7\", 0)\n    h1 = t.get(\"H1_exact\", 0)\n    h8 = t.get(\"H8\", 0)\n    genuine = t.get(\"genuine\", 0)\n    return {\n        \"n_total\": 100, \"n_proved\": proved,\n        \"h7_total_count\": h7, \"h7_total_rate\": h7 / proved,\n        \"h1_strict_count\": h1, \"h8_conjunction_collapse_count\": h8,\n        \"genuine_count\": genuine, \"genuine_rate\": genuine / proved,\n        \"content_independent_count\": 0,\n    }\n\n\ndef load_taxonomy_verification(path: Path) -> dict | None:\n    with open(path) as f:\n        raw = json.load(f)\n    proved = raw.get(\"proved\", 0)\n    if proved == 0:\n        return None\n    tax = raw.get(\"taxonomy\", {})\n    h7 = tax.get(\"h7\", {}).get(\"count\", 0)\n    h1 = tax.get(\"h1_exact\", {}).get(\"count\", 0)\n    h8 = tax.get(\"h8\", {}).get(\"count\", 0)\n    genuine = tax.get(\"genuine\", {}).get(\"count\", 0)\n    return {\n        \"n_total\": raw.get(\"total\", 100), \"n_proved\": proved,\n        \"h7_total_count\": h7, \"h7_total_rate\": h7 / proved,\n        \"h1_strict_count\": h1, \"h8_conjunction_collapse_count\": h8,\n        \"genuine_count\": genuine, \"genuine_rate\": genuine / proved,\n        \"content_independent_count\": 0,\n    }\n\n\ndef discover_runs(data_dir: Path, prefixes: list[str]) -> list[dict]:\n    runs = []\n    seen = set()\n    for entry in sorted(data_dir.iterdir()):\n        name = entry.name\n        if not any(name.startswith(p) for p in prefixes):\n            continue\n        cond = match_condition(name)\n        seed_val = extract_seed(name)\n        if cond is None or seed_val is None:\n            continue\n        key = (cond, seed_val)\n        if key in seen:\n            continue\n        data = None\n        if entry.is_dir():\n            for fname in [\"classify.json\", \"taxonomy.json\"]:\n                data = load_eval_results(entry / fname)\n                if data is not None:\n                    break\n            if data is None:\n                continue\n        elif entry.is_file():\n            if name.endswith(\"_taxonomy_unified.json\"):\n                data = load_taxonomy_unified(entry)\n            elif name.endswith(\"_taxonomy_verification.json\"):\n                data = load_taxonomy_verification(entry)\n            if data is None:\n                continue\n        else:\n            continue\n        seen.add(key)\n        isr_star = None\n        if entry.is_dir():\n            eval_path = entry / \"eval_results.json\"\n            if eval_path.exists():\n                with open(eval_path) as ef:\n                    eval_raw = json.load(ef)\n                isr_star = eval_raw.get(\"summary\", {}).get(\"proved_only_mean_isr\")\n        runs.append({\"dir_name\": name, \"seed\": seed_val, \"condition\": cond,\n                      \"data\": data, \"isr_star\": isr_star})\n    return runs\n\n\ndef compute_row(run: dict) -> dict:\n    d = run[\"data\"]\n    n_proved = d.get(\"n_proved\", 0)\n    n_total = d.get(\"n_total\", 100)\n    h7 = d.get(\"h7_total_count\", 0)\n    h7_rate = d.get(\"h7_total_rate\", h7 / n_proved if n_proved > 0 else 0.0)\n    h1 = d.get(\"h1_strict_count\", 0)\n    h8 = d.get(\"h8_conjunction_collapse_count\", 0)\n    genuine = d.get(\"genuine_count\", 0)\n    genuine_rate = d.get(\"genuine_rate\", genuine / n_proved if n_proved > 0 else 0.0)\n    ci = d.get(\"content_independent_count\", 0)\n    snh = max(genuine - ci, 0)\n    snh_rate = snh / n_proved if n_proved > 0 else 0.0\n    return {\n        \"seed\": run[\"seed\"], \"condition\": run[\"condition\"], \"n_total\": n_total,\n        \"PR\": n_proved, \"H7_count\": h7, \"H7_rate\": h7_rate,\n        \"H1_count\": h1, \"H8_count\": h8,\n        \"genuine_count\": genuine, \"genuine_rate\": genuine_rate,\n        \"CI_count\": ci, \"SNH_count\": snh, \"SNH_rate\": snh_rate,\n        \"ISR_star\": run.get(\"isr_star\"),\n    }\n\n\ndef build_table(runs: list[dict]) -> pd.DataFrame:\n    rows = [compute_row(r) for r in runs]\n    df = pd.DataFrame(rows)\n    df = df.sort_values([\"condition\", \"seed\"]).reset_index(drop=True)\n    return df\n\n\n# --- Statistical tests ---\n\ndef fisher_h7_domination(df: pd.DataFrame) -> dict:\n    results = {}\n    for cond in [\"ISR\", \"RANDOM\"]:\n        sub = df[df[\"condition\"] == cond]\n        results[cond] = {\n            \"n\": len(sub),\n            \"h7_dom\": int((sub[\"H7_rate\"] >= 0.5).sum()),\n            \"not_h7_dom\": int((sub[\"H7_rate\"] < 0.5).sum()),\n        }\n    table = np.array([\n        [results[\"ISR\"][\"h7_dom\"], results[\"ISR\"][\"not_h7_dom\"]],\n        [results[\"RANDOM\"][\"h7_dom\"], results[\"RANDOM\"][\"not_h7_dom\"]],\n    ])\n    odds_ratio, p_value = stats.fisher_exact(table, alternative=\"greater\")\n\n    # 95% exact CI via scipy.stats.contingency\n    or_ci_lo, or_ci_hi = np.nan, np.nan\n    try:\n        ct = stats.contingency.odds_ratio(table)\n        ci = ct.confidence_interval(confidence_level=0.95)\n        or_ci_lo, or_ci_hi = ci.low, ci.high\n    except Exception:\n        pass\n\n    return {\n        \"table\": table.tolist(),\n        \"ISR\": results[\"ISR\"],\n        \"RANDOM\": results[\"RANDOM\"],\n        \"odds_ratio\": odds_ratio,\n        \"or_ci_lo\": or_ci_lo,\n        \"or_ci_hi\": or_ci_hi,\n        \"p_value\": p_value,\n    }\n\n\ndef permutation_test_genuine(df: pd.DataFrame, n_perm: int = 10000,\n                              rng_seed: int = 42) -> dict:\n    isr = df[df[\"condition\"] == \"ISR\"][\"genuine_rate\"].values\n    rand = df[df[\"condition\"] == \"RANDOM\"][\"genuine_rate\"].values\n    observed = isr.mean() - rand.mean()\n    pooled = np.concatenate([isr, rand])\n    n_isr = len(isr)\n    rng = np.random.default_rng(rng_seed)\n    count = 0\n    for _ in range(n_perm):\n        perm = rng.permutation(pooled)\n        if perm[:n_isr].mean() - perm[n_isr:].mean() >= observed:\n            count += 1\n    return {\n        \"observed_diff\": float(observed),\n        \"p_value\": count / n_perm,\n        \"n_perm\": n_perm,\n        \"isr_mean\": float(isr.mean()),\n        \"random_mean\": float(rand.mean()),\n    }\n\n\ndef mannwhitney_h7(df: pd.DataFrame) -> dict:\n    isr = df[df[\"condition\"] == \"ISR\"][\"H7_rate\"].values\n    rand = df[df[\"condition\"] == \"RANDOM\"][\"H7_rate\"].values\n    n1, n2 = len(isr), len(rand)\n    u_stat, p_value = stats.mannwhitneyu(isr, rand, alternative=\"greater\")\n    r_rb = 2.0 * u_stat / (n1 * n2) - 1.0 if n1 * n2 > 0 else np.nan\n    return {\n        \"U\": float(u_stat),\n        \"p_value\": float(p_value),\n        \"r_rank_biserial\": float(r_rb),\n        \"isr_median\": float(np.median(isr)),\n        \"random_median\": float(np.median(rand)),\n    }\n\n\ndef mannwhitney_isr_star(df: pd.DataFrame) -> dict | None:\n    isr = df[df[\"condition\"] == \"ISR\"][\"ISR_star\"].dropna().values.astype(float)\n    rand = df[df[\"condition\"] == \"RANDOM\"][\"ISR_star\"].dropna().values.astype(float)\n    if len(isr) < 2 or len(rand) < 2:\n        return None\n    n1, n2 = len(isr), len(rand)\n    u_stat, p_value = stats.mannwhitneyu(isr, rand, alternative=\"greater\")\n    r_rb = 2.0 * u_stat / (n1 * n2) - 1.0\n    return {\n        \"U\": float(u_stat),\n        \"p_value\": float(p_value),\n        \"r_rank_biserial\": float(r_rb),\n        \"isr_median\": float(np.median(isr)),\n        \"random_median\": float(np.median(rand)),\n        \"isr_mean\": float(np.mean(isr)),\n        \"random_mean\": float(np.mean(rand)),\n    }\n\n\ndef bca_bootstrap_ci(df: pd.DataFrame, metric: str, n_boot: int = 10000,\n                      rng_seed: int = 42) -> dict:\n    \"\"\"BCa 95% CI for per-condition means of a metric.\"\"\"\n    result = {}\n    for cond in [\"ISR\", \"RANDOM\"]:\n        vals = df[df[\"condition\"] == cond][metric].values\n        if len(vals) < 2:\n            result[cond] = {\"mean\": float(vals.mean()) if len(vals) else np.nan,\n                            \"ci_lo\": np.nan, \"ci_hi\": np.nan}\n            continue\n        res = stats.bootstrap(\n            (vals,), np.mean, n_resamples=n_boot,\n            confidence_level=0.95, method=\"BCa\",\n            random_state=np.random.default_rng(rng_seed),\n        )\n        result[cond] = {\n            \"mean\": float(vals.mean()),\n            \"ci_lo\": float(res.confidence_interval.low),\n            \"ci_hi\": float(res.confidence_interval.high),\n        }\n    return result\n\n\ndef bayes_factor_h7_domination(df: pd.DataFrame) -> dict:\n    \"\"\"BF10 for H7-domination rate difference (beta-binomial conjugate).\n    H0: ISR and Random share same domination rate.\n    H1: independent rates. Prior: Beta(1,1) on each.\n    \"\"\"\n    isr_sub = df[df[\"condition\"] == \"ISR\"]\n    rand_sub = df[df[\"condition\"] == \"RANDOM\"]\n    k_isr = int((isr_sub[\"H7_rate\"] >= 0.5).sum())\n    n_isr = len(isr_sub)\n    k_rand = int((rand_sub[\"H7_rate\"] >= 0.5).sum())\n    n_rand = len(rand_sub)\n    k_total = k_isr + k_rand\n    n_total = n_isr + n_rand\n\n    # log marginal under H0 (shared rate)\n    log_m_h0 = betaln(1 + k_total, 1 + n_total - k_total) - betaln(1, 1)\n    # log marginal under H1 (independent rates)\n    log_m_h1 = (betaln(1 + k_isr, 1 + n_isr - k_isr) - betaln(1, 1)\n                + betaln(1 + k_rand, 1 + n_rand - k_rand) - betaln(1, 1))\n    log_bf10 = log_m_h1 - log_m_h0\n    bf10 = float(np.exp(log_bf10))\n\n    return {\n        \"k_isr\": k_isr, \"n_isr\": n_isr,\n        \"k_rand\": k_rand, \"n_rand\": n_rand,\n        \"bf10\": bf10,\n        \"log_bf10\": float(log_bf10),\n        \"interpretation\": _interpret_bf(bf10),\n    }\n\n\ndef _interpret_bf(bf: float) -> str:\n    if bf > 100:\n        return \"extreme evidence for H1\"\n    if bf > 30:\n        return \"very strong evidence for H1\"\n    if bf > 10:\n        return \"strong evidence for H1\"\n    if bf > 3:\n        return \"moderate evidence for H1\"\n    if bf > 1:\n        return \"anecdotal evidence for H1\"\n    if bf > 1/3:\n        return \"anecdotal evidence (inconclusive)\"\n    if bf > 1/10:\n        return \"moderate evidence for H0\"\n    return \"strong evidence for H0\"\n\n\ndef condition_stats(df: pd.DataFrame) -> pd.DataFrame:\n    metrics = [\"PR\", \"H7_rate\", \"genuine_rate\", \"SNH_rate\"]\n    rows = []\n    for cond in [\"ISR\", \"RANDOM\"]:\n        sub = df[df[\"condition\"] == cond]\n        row = {\"condition\": cond, \"n_seeds\": len(sub)}\n        for m in metrics:\n            vals = sub[m].values\n            row[f\"{m}_mean\"] = vals.mean()\n            row[f\"{m}_std\"] = vals.std(ddof=1) if len(vals) > 1 else 0.0\n        isr_vals = sub[\"ISR_star\"].dropna().values.astype(float)\n        row[\"ISR_star_mean\"] = isr_vals.mean() if len(isr_vals) else np.nan\n        row[\"ISR_star_std\"] = isr_vals.std(ddof=1) if len(isr_vals) > 1 else 0.0\n        rows.append(row)\n    return pd.DataFrame(rows)\n\n\n# --- Formatting ---\n\ndef fmt_pct(val: float) -> str:\n    return f\"{val*100:.1f}\\\\%\"\n\ndef fmt_or(val: float) -> str:\n    return \"$\\\\infty$\" if np.isinf(val) else f\"{val:.2f}\"\n\ndef fmt_ci(lo: float, hi: float) -> str:\n    lo_s = f\"{lo:.2f}\" if not np.isnan(lo) else \"0\"\n    hi_s = \"$\\\\infty$\" if np.isinf(hi) or np.isnan(hi) else f\"{hi:.2f}\"\n    return f\"[{lo_s}, {hi_s}]\"\n\ndef fmt_p(p: float) -> str:\n    if p < 0.001:\n        return \"$<$0.001\"\n    return f\"{p:.3f}\"\n\ndef fmt_mean_std(mean: float, std: float, pct: bool = False) -> str:\n    if pct:\n        return f\"{mean*100:.1f} $\\\\pm$ {std*100:.1f}\\\\%\"\n    return f\"{mean:.1f} $\\\\pm$ {std:.1f}\"\n\ndef fmt_bca(bca: dict, pct: bool = False) -> str:\n    m = bca[\"mean\"]\n    lo, hi = bca[\"ci_lo\"], bca[\"ci_hi\"]\n    if pct:\n        return f\"{m*100:.1f}\\\\% [{lo*100:.1f}, {hi*100:.1f}]\"\n    return f\"{m:.1f} [{lo:.1f}, {hi:.1f}]\"\n\n\n# --- Console output ---\n\ndef print_per_seed_table(df: pd.DataFrame):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  PER-SEED RESULTS\")\n    print(\"=\" * 90)\n    cols = [\"condition\", \"seed\", \"PR\", \"H7_count\", \"H7_rate\", \"H1_count\",\n            \"H8_count\", \"genuine_count\", \"genuine_rate\", \"CI_count\", \"SNH_count\", \"SNH_rate\",\n            \"ISR_star\"]\n    fmt = df[cols].copy()\n    for c in [\"H7_rate\", \"genuine_rate\", \"SNH_rate\"]:\n        fmt[c] = fmt[c].apply(lambda v: f\"{v*100:.1f}%\")\n    fmt[\"ISR_star\"] = fmt[\"ISR_star\"].apply(lambda v: f\"{v:.4f}\" if pd.notna(v) else \"---\")\n    print(fmt.to_string(index=False))\n\n\ndef print_condition_stats(cond_df: pd.DataFrame):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  CONDITION-LEVEL STATISTICS (mean +/- SD)\")\n    print(\"=\" * 90)\n    for _, row in cond_df.iterrows():\n        n = int(row['n_seeds'])\n        print(f\"\\n  {row['condition']} (n={n} seeds):\")\n        print(f\"    PR:           {row['PR_mean']:.1f} +/- {row['PR_std']:.1f}\")\n        print(f\"    H7 rate:      {row['H7_rate_mean']*100:.1f} +/- {row['H7_rate_std']*100:.1f}%\")\n        print(f\"    Genuine rate: {row['genuine_rate_mean']*100:.1f} +/- {row['genuine_rate_std']*100:.1f}%\")\n        print(f\"    S-NH rate:    {row['SNH_rate_mean']*100:.1f} +/- {row['SNH_rate_std']*100:.1f}%\")\n        if not np.isnan(row.get('ISR_star_mean', np.nan)):\n            print(f\"    ISR*:         {row['ISR_star_mean']:.4f} +/- {row['ISR_star_std']:.4f}\")\n\n\ndef print_tests(fisher, perm, mw, bf, bca_h7, bca_gen):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  STATISTICAL TESTS\")\n    print(\"=\" * 90)\n\n    print(\"\\n  1. H7 Domination Fisher Exact Test (H7-dominated = H7% >= 50%)\")\n    print(f\"     ISR:    {fisher['ISR']['h7_dom']} dominated / {fisher['ISR']['n']} seeds\")\n    print(f\"     RANDOM: {fisher['RANDOM']['h7_dom']} dominated / {fisher['RANDOM']['n']} seeds\")\n    print(f\"     Contingency: {fisher['table']}\")\n    or_str = \"inf\" if np.isinf(fisher['odds_ratio']) else f\"{fisher['odds_ratio']:.4f}\"\n    print(f\"     OR = {or_str}, 95% CI = [{fisher['or_ci_lo']:.4f}, {fisher['or_ci_hi']:.4f}]\"\n          if not np.isnan(fisher['or_ci_lo']) else f\"     OR = {or_str}, 95% CI = N/A\")\n    print(f\"     p-value (one-sided, greater): {fisher['p_value']:.4f}\")\n\n    print(f\"\\n  2. Genuine Rate Permutation Test (n_perm={perm['n_perm']})\")\n    print(f\"     ISR mean:    {perm['isr_mean']*100:.2f}%\")\n    print(f\"     RANDOM mean: {perm['random_mean']*100:.2f}%\")\n    print(f\"     Diff: {perm['observed_diff']*100:.2f} pp, p = {perm['p_value']:.4f}\")\n\n    print(f\"\\n  3. H7 Rate Mann-Whitney U Test\")\n    print(f\"     ISR median:    {mw['isr_median']*100:.1f}%\")\n    print(f\"     RANDOM median: {mw['random_median']*100:.1f}%\")\n    print(f\"     U = {mw['U']:.1f}, p = {mw['p_value']:.4f}\")\n    print(f\"     Rank-biserial r = {mw['r_rank_biserial']:.4f}\")\n\n    print(f\"\\n  4. Bayes Factor (H7 Domination, Beta-Binomial)\")\n    print(f\"     ISR:    {bf['k_isr']}/{bf['n_isr']} dominated\")\n    print(f\"     RANDOM: {bf['k_rand']}/{bf['n_rand']} dominated\")\n    print(f\"     BF10 = {bf['bf10']:.4f} ({bf['interpretation']})\")\n\n    print(f\"\\n  5. BCa Bootstrap 95% CI (n_boot resamples)\")\n    for label, bca in [(\"H7 rate\", bca_h7), (\"Genuine rate\", bca_gen)]:\n        print(f\"     {label}:\")\n        for cond in [\"ISR\", \"RANDOM\"]:\n            b = bca[cond]\n            print(f\"       {cond}: {b['mean']*100:.1f}% [{b['ci_lo']*100:.1f}, {b['ci_hi']*100:.1f}]\"\n                  if not np.isnan(b['ci_lo']) else f\"       {cond}: {b['mean']*100:.1f}% [N/A]\")\n\n\n# --- Markdown generation (appendix-ready) ---\n\ndef generate_markdown(df: pd.DataFrame, cond_df: pd.DataFrame,\n                      fisher: dict, perm: dict, mw: dict,\n                      bf: dict, bca_h7: dict, bca_gen: dict) -> str:\n    L = []\n    L.append(\"## D134: ISR vs Random Statistical Analysis\\n\")\n\n    # Per-seed table\n    L.append(\"### Table A1: Per-Seed Hacking Taxonomy (4B Qwen3, 500 steps)\\n\")\n    L.append(\"| Condition | Seed | PR | H7 | H7\\\\% | H1 | H8 | Genuine | Gen\\\\% | CI | S-NH | S-NH\\\\% |\")\n    L.append(\"|:----------|-----:|---:|---:|-----:|---:|---:|--------:|------:|---:|-----:|-------:|\")\n    for _, r in df.iterrows():\n        L.append(\n            f\"| {r['condition']} | {r['seed']} | {int(r['PR'])} | {int(r['H7_count'])} | \"\n            f\"{r['H7_rate']*100:.1f} | {int(r['H1_count'])} | {int(r['H8_count'])} | \"\n            f\"{int(r['genuine_count'])} | {r['genuine_rate']*100:.1f} | {int(r['CI_count'])} | \"\n            f\"{int(r['SNH_count'])} | {r['SNH_rate']*100:.1f} |\"\n        )\n\n    # Condition summary with BCa CI\n    L.append(\"\\n### Table A2: Condition-Level Summary\\n\")\n    L.append(\"| Condition | $n$ | PR (mean$\\\\pm$SD) | H7\\\\% (mean$\\\\pm$SD) | H7\\\\% BCa 95\\\\% CI | Gen\\\\% (mean$\\\\pm$SD) | Gen\\\\% BCa 95\\\\% CI |\")\n    L.append(\"|:----------|----:|:------------------|:-------------------|:-----------------|:-------------------|:-----------------|\")\n    for _, r in cond_df.iterrows():\n        cond = r[\"condition\"]\n        h7_bca = bca_h7.get(cond, {})\n        gen_bca = bca_gen.get(cond, {})\n        h7_ci = f\"[{h7_bca['ci_lo']*100:.1f}, {h7_bca['ci_hi']*100:.1f}]\" if h7_bca and not np.isnan(h7_bca.get('ci_lo', np.nan)) else \"N/A\"\n        gen_ci = f\"[{gen_bca['ci_lo']*100:.1f}, {gen_bca['ci_hi']*100:.1f}]\" if gen_bca and not np.isnan(gen_bca.get('ci_lo', np.nan)) else \"N/A\"\n        L.append(\n            f\"| {cond} | {int(r['n_seeds'])} | \"\n            f\"{r['PR_mean']:.1f}$\\\\pm${r['PR_std']:.1f} | \"\n            f\"{r['H7_rate_mean']*100:.1f}$\\\\pm${r['H7_rate_std']*100:.1f} | \"\n            f\"{h7_ci} | \"\n            f\"{r['genuine_rate_mean']*100:.1f}$\\\\pm${r['genuine_rate_std']*100:.1f} | \"\n            f\"{gen_ci} |\"\n        )\n\n    # Statistical tests\n    if fisher and perm and mw and bf:\n        L.append(\"\\n### Statistical Tests\\n\")\n\n        # Fisher\n        or_str = \"$\\\\infty$\" if np.isinf(fisher['odds_ratio']) else f\"{fisher['odds_ratio']:.2f}\"\n        ci_lo = f\"{fisher['or_ci_lo']:.2f}\" if not np.isnan(fisher['or_ci_lo']) else \"0\"\n        ci_hi = \"$\\\\infty$\" if np.isinf(fisher.get('or_ci_hi', np.inf)) or np.isnan(fisher.get('or_ci_hi', np.nan)) else f\"{fisher['or_ci_hi']:.2f}\"\n        L.append(\"**1. H7 Domination Fisher Exact Test** (threshold: H7$\\\\geq$50\\\\% of proved)\")\n        L.append(f\"- ISR: {fisher['ISR']['h7_dom']}/{fisher['ISR']['n']} seeds H7-dominated; \"\n                 f\"Random: {fisher['RANDOM']['h7_dom']}/{fisher['RANDOM']['n']}\")\n        L.append(f\"- OR = {or_str}, 95\\\\% exact CI = [{ci_lo}, {ci_hi}], \"\n                 f\"$p$ = {fmt_p(fisher['p_value'])}\")\n        L.append(\"\")\n\n        # Permutation\n        L.append(f\"**2. Genuine Rate Permutation Test** ($n$ = {perm['n_perm']:,} permutations)\")\n        L.append(f\"- ISR mean: {perm['isr_mean']*100:.2f}\\\\%, Random mean: {perm['random_mean']*100:.2f}\\\\%\")\n        L.append(f\"- $\\\\Delta$ = {perm['observed_diff']*100:.2f} pp, $p$ = {fmt_p(perm['p_value'])}\")\n        L.append(\"\")\n\n        # Mann-Whitney\n        L.append(\"**3. H7 Rate Mann-Whitney $U$ Test**\")\n        L.append(f\"- ISR median: {mw['isr_median']*100:.1f}\\\\%, Random median: {mw['random_median']*100:.1f}\\\\%\")\n        L.append(f\"- $U$ = {mw['U']:.1f}, $p$ = {fmt_p(mw['p_value'])}, \"\n                 f\"rank-biserial $r$ = {mw['r_rank_biserial']:.3f}\")\n        L.append(\"\")\n\n        # Bayes Factor\n        L.append(\"**4. Bayes Factor** (Beta-Binomial conjugate, prior: Beta(1,1))\")\n        L.append(f\"- $BF_{{10}}$ = {bf['bf10']:.2f} ({bf['interpretation']})\")\n        L.append(f\"- ISR: {bf['k_isr']}/{bf['n_isr']} H7-dominated, \"\n                 f\"Random: {bf['k_rand']}/{bf['n_rand']}\")\n\n    return \"\\n\".join(L) + \"\\n\"\n\n\n# --- Main ---\n\ndef main():\n    args = parse_args()\n    data_dir = Path(args.data_dir)\n\n    if not data_dir.exists():\n        print(f\"ERROR: data directory {data_dir} does not exist\", file=sys.stderr)\n        sys.exit(1)\n\n    if args.prefix:\n        prefixes = [args.prefix]\n    elif args.prefixes:\n        prefixes = [p.strip() for p in args.prefixes.split(\",\")]\n    else:\n        prefixes = MODE_PREFIXES[args.mode]\n    print(f\"Mode: {args.mode} | Prefixes: {prefixes}\")\n\n    runs = discover_runs(data_dir, prefixes)\n    if not runs:\n        print(f\"ERROR: no runs found in {data_dir} with prefixes {prefixes}\", file=sys.stderr)\n        sys.exit(1)\n\n    isr_count = sum(1 for r in runs if r[\"condition\"] == \"ISR\")\n    rand_count = sum(1 for r in runs if r[\"condition\"] == \"RANDOM\")\n    print(f\"Found {len(runs)} runs: {isr_count} ISR, {rand_count} RANDOM\")\n    for r in runs:\n        print(f\"  {r['condition']:6s} s{r['seed']} <- {r['dir_name']}\")\n\n    df = build_table(runs)\n    print_per_seed_table(df)\n\n    cond_df = condition_stats(df)\n    print_condition_stats(cond_df)\n\n    if isr_count < 2 or rand_count < 2:\n        print(\"\\nWARNING: need >= 2 seeds per condition for statistical tests, skipping.\",\n              file=sys.stderr)\n        bca_h7 = bca_bootstrap_ci(df, \"H7_rate\", args.n_boot, args.seed)\n        bca_gen = bca_bootstrap_ci(df, \"genuine_rate\", args.n_boot, args.seed)\n        if args.output:\n            md = generate_markdown(df, cond_df, {}, {}, {}, {}, bca_h7, bca_gen)\n            Path(args.output).write_text(md)\n            print(f\"\\nMarkdown written to {args.output}\")\n        return\n\n    fisher = fisher_h7_domination(df)\n    perm = permutation_test_genuine(df, n_perm=args.n_perm, rng_seed=args.seed)\n    mw = mannwhitney_h7(df)\n    bf = bayes_factor_h7_domination(df)\n    bca_h7 = bca_bootstrap_ci(df, \"H7_rate\", args.n_boot, args.seed)\n    bca_gen = bca_bootstrap_ci(df, \"genuine_rate\", args.n_boot, args.seed)\n\n    print_tests(fisher, perm, mw, bf, bca_h7, bca_gen)\n\n    md = generate_markdown(df, cond_df, fisher, perm, mw, bf, bca_h7, bca_gen)\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  MARKDOWN OUTPUT (appendix-ready)\")\n    print(\"=\" * 90)\n    print(md)\n\n    if args.output:\n        Path(args.output).parent.mkdir(parents=True, exist_ok=True)\n        Path(args.output).write_text(md)\n        print(f\"Markdown written to {args.output}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 436,
        "oldLines": 7,
        "newStart": 436,
        "newLines": 7,
        "lines": [
          "             print(f\"    ISR*:         {row['ISR_star_mean']:.4f} +/- {row['ISR_star_std']:.4f}\")",
          " ",
          " ",
          "-def print_tests(fisher, perm, mw, bf, bca_h7, bca_gen):",
          "+def print_tests(fisher, perm, mw, bf, bca_h7, bca_gen, mw_isr_star=None):",
          "     print(\"\\n\" + \"=\" * 90)",
          "     print(\"  STATISTICAL TESTS\")",
          "     print(\"=\" * 90)"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 39_

Now add the ISR* MW section after the BCa bootstrap output in `print_tests`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "b82443fb-a04b-462a-b904-e45fbdef4917",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012uttST9amXy6KHQsRbd5DD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 386,
      "cache_read_input_tokens": 49137,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 386
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

_source line 40_

<details open><summary>🔧 Tool call — Edit · `toolu_01HCzCkQ5sSbzGcPtj4acwbV`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/scripts/d134_analysis.py",
  "old_string": "            print(f\"       {cond}: {b['mean']*100:.1f}% [{b['ci_lo']*100:.1f}, {b['ci_hi']*100:.1f}]\"\n                  if not np.isnan(b['ci_lo']) else f\"       {cond}: {b['mean']*100:.1f}% [N/A]\")\n\n\n# --- Markdown generation (appendix-ready) ---",
  "new_string": "            print(f\"       {cond}: {b['mean']*100:.1f}% [{b['ci_lo']*100:.1f}, {b['ci_hi']*100:.1f}]\"\n                  if not np.isnan(b['ci_lo']) else f\"       {cond}: {b['mean']*100:.1f}% [N/A]\")\n\n    if mw_isr_star:\n        print(f\"\\n  6. ISR* (Proved-Only Mean ISR) Mann-Whitney U Test\")\n        print(f\"     ISR mean:    {mw_isr_star['isr_mean']:.4f}, median: {mw_isr_star['isr_median']:.4f}\")\n        print(f\"     RANDOM mean: {mw_isr_star['random_mean']:.4f}, median: {mw_isr_star['random_median']:.4f}\")\n        print(f\"     U = {mw_isr_star['U']:.1f}, p = {mw_isr_star['p_value']:.4f}\")\n        print(f\"     Rank-biserial r = {mw_isr_star['r_rank_biserial']:.4f}\")\n\n\n# --- Markdown generation (appendix-ready) ---"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "c1255553-f6e6-4897-8342-6f2ee5236d99",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012uttST9amXy6KHQsRbd5DD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 386,
      "cache_read_input_tokens": 49137,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 386
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

_source line 41 · 2026-05-18T23:32:56.287Z_

<details><summary>↩ Tool result · `toolu_01HCzCkQ5sSbzGcPtj4acwbV`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/scripts/d134_analysis.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "6b6c7e3f-ab2a-4f59-8140-d08879d60a7f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/scripts/d134_analysis.py",
    "oldString": "            print(f\"       {cond}: {b['mean']*100:.1f}% [{b['ci_lo']*100:.1f}, {b['ci_hi']*100:.1f}]\"\n                  if not np.isnan(b['ci_lo']) else f\"       {cond}: {b['mean']*100:.1f}% [N/A]\")\n\n\n# --- Markdown generation (appendix-ready) ---",
    "newString": "            print(f\"       {cond}: {b['mean']*100:.1f}% [{b['ci_lo']*100:.1f}, {b['ci_hi']*100:.1f}]\"\n                  if not np.isnan(b['ci_lo']) else f\"       {cond}: {b['mean']*100:.1f}% [N/A]\")\n\n    if mw_isr_star:\n        print(f\"\\n  6. ISR* (Proved-Only Mean ISR) Mann-Whitney U Test\")\n        print(f\"     ISR mean:    {mw_isr_star['isr_mean']:.4f}, median: {mw_isr_star['isr_median']:.4f}\")\n        print(f\"     RANDOM mean: {mw_isr_star['random_mean']:.4f}, median: {mw_isr_star['random_median']:.4f}\")\n        print(f\"     U = {mw_isr_star['U']:.1f}, p = {mw_isr_star['p_value']:.4f}\")\n        print(f\"     Rank-biserial r = {mw_isr_star['r_rank_biserial']:.4f}\")\n\n\n# --- Markdown generation (appendix-ready) ---",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"D134 experiment analysis: multi-seed ISR vs Random, 4B GRPO training.\nReads taxonomy data from classify.json, taxonomy.json, or top-level taxonomy files.\nComputes summary stats, statistical tests (Fisher, Mann-Whitney, permutation, Bayes Factor),\nand BCa bootstrap CIs. Outputs appendix-ready markdown.\n\"\"\"\n\nimport argparse\nimport json\nimport re\nimport sys\nfrom pathlib import Path\n\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\nfrom scipy.special import betaln\n\nCONDITION_MAP = [\n    (\"d134_4b_isr\", \"ISR\"),\n    (\"d134_4b_random\", \"RANDOM\"),\n    (\"plan002_additive\", \"ISR\"),\n    (\"plan018_additive_random\", \"RANDOM\"),\n    (\"plan018_random\", \"RANDOM\"),\n]\n\nMODE_PREFIXES = {\n    \"d134_only\": [\"d134_4b\"],\n    \"all\": [\"d134_4b\", \"plan002_additive_b01\", \"plan018_additive_random_b01\", \"plan018_random\"],\n}\n\n\ndef parse_args():\n    p = argparse.ArgumentParser(description=\"D134 multi-seed analysis and statistical tests\")\n    p.add_argument(\"--data_dir\", type=str, default=\"/root/autodl-tmp/outputs\",\n                   help=\"Directory containing experiment outputs\")\n    p.add_argument(\"--mode\", type=str, default=\"d134_only\", choices=list(MODE_PREFIXES),\n                   help=\"d134_only = matched 5+5 design (default); all = include original seeds\")\n    p.add_argument(\"--prefix\", type=str, default=None,\n                   help=\"(Legacy) Single prefix filter; overrides mode/prefixes\")\n    p.add_argument(\"--prefixes\", type=str, default=None,\n                   help=\"Comma-separated prefixes; overrides --mode\")\n    p.add_argument(\"--output\", type=str, default=None,\n                   help=\"Write markdown summary to this file\")\n    p.add_argument(\"--n_perm\", type=int, default=10000,\n                   help=\"Number of permutations for permutation test\")\n    p.add_argument(\"--n_boot\", type=int, default=10000,\n                   help=\"Number of bootstrap resamples for BCa CI\")\n    p.add_argument(\"--seed\", type=int, default=42,\n                   help=\"Random seed for permutation/bootstrap\")\n    return p.parse_args()\n\n\n# --- Data loading ---\n\ndef match_condition(name: str) -> str | None:\n    best_prefix = \"\"\n    best_cond = None\n    for prefix, cond in CONDITION_MAP:\n        if name.startswith(prefix) and len(prefix) > len(best_prefix):\n            best_prefix = prefix\n            best_cond = cond\n    return best_cond\n\n\ndef extract_seed(name: str) -> int | None:\n    m = re.search(r'_s(\\d+)', name)\n    return int(m.group(1)) if m else None\n\n\ndef load_eval_results(path: Path) -> dict | None:\n    if not path.exists():\n        return None\n    with open(path) as f:\n        data = json.load(f)\n    if \"eval_results\" in data:\n        return data[\"eval_results\"]\n    return data\n\n\ndef load_taxonomy_unified(path: Path) -> dict | None:\n    with open(path) as f:\n        raw = json.load(f)\n    t = raw.get(\"taxonomy\", {})\n    proved = t.get(\"proved\", 0)\n    if proved == 0:\n        return None\n    h7 = t.get(\"H7\", 0)\n    h1 = t.get(\"H1_exact\", 0)\n    h8 = t.get(\"H8\", 0)\n    genuine = t.get(\"genuine\", 0)\n    return {\n        \"n_total\": 100, \"n_proved\": proved,\n        \"h7_total_count\": h7, \"h7_total_rate\": h7 / proved,\n        \"h1_strict_count\": h1, \"h8_conjunction_collapse_count\": h8,\n        \"genuine_count\": genuine, \"genuine_rate\": genuine / proved,\n        \"content_independent_count\": 0,\n    }\n\n\ndef load_taxonomy_verification(path: Path) -> dict | None:\n    with open(path) as f:\n        raw = json.load(f)\n    proved = raw.get(\"proved\", 0)\n    if proved == 0:\n        return None\n    tax = raw.get(\"taxonomy\", {})\n    h7 = tax.get(\"h7\", {}).get(\"count\", 0)\n    h1 = tax.get(\"h1_exact\", {}).get(\"count\", 0)\n    h8 = tax.get(\"h8\", {}).get(\"count\", 0)\n    genuine = tax.get(\"genuine\", {}).get(\"count\", 0)\n    return {\n        \"n_total\": raw.get(\"total\", 100), \"n_proved\": proved,\n        \"h7_total_count\": h7, \"h7_total_rate\": h7 / proved,\n        \"h1_strict_count\": h1, \"h8_conjunction_collapse_count\": h8,\n        \"genuine_count\": genuine, \"genuine_rate\": genuine / proved,\n        \"content_independent_count\": 0,\n    }\n\n\ndef discover_runs(data_dir: Path, prefixes: list[str]) -> list[dict]:\n    runs = []\n    seen = set()\n    for entry in sorted(data_dir.iterdir()):\n        name = entry.name\n        if not any(name.startswith(p) for p in prefixes):\n            continue\n        cond = match_condition(name)\n        seed_val = extract_seed(name)\n        if cond is None or seed_val is None:\n            continue\n        key = (cond, seed_val)\n        if key in seen:\n            continue\n        data = None\n        if entry.is_dir():\n            for fname in [\"classify.json\", \"taxonomy.json\"]:\n                data = load_eval_results(entry / fname)\n                if data is not None:\n                    break\n            if data is None:\n                continue\n        elif entry.is_file():\n            if name.endswith(\"_taxonomy_unified.json\"):\n                data = load_taxonomy_unified(entry)\n            elif name.endswith(\"_taxonomy_verification.json\"):\n                data = load_taxonomy_verification(entry)\n            if data is None:\n                continue\n        else:\n            continue\n        seen.add(key)\n        isr_star = None\n        if entry.is_dir():\n            eval_path = entry / \"eval_results.json\"\n            if eval_path.exists():\n                with open(eval_path) as ef:\n                    eval_raw = json.load(ef)\n                isr_star = eval_raw.get(\"summary\", {}).get(\"proved_only_mean_isr\")\n        runs.append({\"dir_name\": name, \"seed\": seed_val, \"condition\": cond,\n                      \"data\": data, \"isr_star\": isr_star})\n    return runs\n\n\ndef compute_row(run: dict) -> dict:\n    d = run[\"data\"]\n    n_proved = d.get(\"n_proved\", 0)\n    n_total = d.get(\"n_total\", 100)\n    h7 = d.get(\"h7_total_count\", 0)\n    h7_rate = d.get(\"h7_total_rate\", h7 / n_proved if n_proved > 0 else 0.0)\n    h1 = d.get(\"h1_strict_count\", 0)\n    h8 = d.get(\"h8_conjunction_collapse_count\", 0)\n    genuine = d.get(\"genuine_count\", 0)\n    genuine_rate = d.get(\"genuine_rate\", genuine / n_proved if n_proved > 0 else 0.0)\n    ci = d.get(\"content_independent_count\", 0)\n    snh = max(genuine - ci, 0)\n    snh_rate = snh / n_proved if n_proved > 0 else 0.0\n    return {\n        \"seed\": run[\"seed\"], \"condition\": run[\"condition\"], \"n_total\": n_total,\n        \"PR\": n_proved, \"H7_count\": h7, \"H7_rate\": h7_rate,\n        \"H1_count\": h1, \"H8_count\": h8,\n        \"genuine_count\": genuine, \"genuine_rate\": genuine_rate,\n        \"CI_count\": ci, \"SNH_count\": snh, \"SNH_rate\": snh_rate,\n        \"ISR_star\": run.get(\"isr_star\"),\n    }\n\n\ndef build_table(runs: list[dict]) -> pd.DataFrame:\n    rows = [compute_row(r) for r in runs]\n    df = pd.DataFrame(rows)\n    df = df.sort_values([\"condition\", \"seed\"]).reset_index(drop=True)\n    return df\n\n\n# --- Statistical tests ---\n\ndef fisher_h7_domination(df: pd.DataFrame) -> dict:\n    results = {}\n    for cond in [\"ISR\", \"RANDOM\"]:\n        sub = df[df[\"condition\"] == cond]\n        results[cond] = {\n            \"n\": len(sub),\n            \"h7_dom\": int((sub[\"H7_rate\"] >= 0.5).sum()),\n            \"not_h7_dom\": int((sub[\"H7_rate\"] < 0.5).sum()),\n        }\n    table = np.array([\n        [results[\"ISR\"][\"h7_dom\"], results[\"ISR\"][\"not_h7_dom\"]],\n        [results[\"RANDOM\"][\"h7_dom\"], results[\"RANDOM\"][\"not_h7_dom\"]],\n    ])\n    odds_ratio, p_value = stats.fisher_exact(table, alternative=\"greater\")\n\n    # 95% exact CI via scipy.stats.contingency\n    or_ci_lo, or_ci_hi = np.nan, np.nan\n    try:\n        ct = stats.contingency.odds_ratio(table)\n        ci = ct.confidence_interval(confidence_level=0.95)\n        or_ci_lo, or_ci_hi = ci.low, ci.high\n    except Exception:\n        pass\n\n    return {\n        \"table\": table.tolist(),\n        \"ISR\": results[\"ISR\"],\n        \"RANDOM\": results[\"RANDOM\"],\n        \"odds_ratio\": odds_ratio,\n        \"or_ci_lo\": or_ci_lo,\n        \"or_ci_hi\": or_ci_hi,\n        \"p_value\": p_value,\n    }\n\n\ndef permutation_test_genuine(df: pd.DataFrame, n_perm: int = 10000,\n                              rng_seed: int = 42) -> dict:\n    isr = df[df[\"condition\"] == \"ISR\"][\"genuine_rate\"].values\n    rand = df[df[\"condition\"] == \"RANDOM\"][\"genuine_rate\"].values\n    observed = isr.mean() - rand.mean()\n    pooled = np.concatenate([isr, rand])\n    n_isr = len(isr)\n    rng = np.random.default_rng(rng_seed)\n    count = 0\n    for _ in range(n_perm):\n        perm = rng.permutation(pooled)\n        if perm[:n_isr].mean() - perm[n_isr:].mean() >= observed:\n            count += 1\n    return {\n        \"observed_diff\": float(observed),\n        \"p_value\": count / n_perm,\n        \"n_perm\": n_perm,\n        \"isr_mean\": float(isr.mean()),\n        \"random_mean\": float(rand.mean()),\n    }\n\n\ndef mannwhitney_h7(df: pd.DataFrame) -> dict:\n    isr = df[df[\"condition\"] == \"ISR\"][\"H7_rate\"].values\n    rand = df[df[\"condition\"] == \"RANDOM\"][\"H7_rate\"].values\n    n1, n2 = len(isr), len(rand)\n    u_stat, p_value = stats.mannwhitneyu(isr, rand, alternative=\"greater\")\n    r_rb = 2.0 * u_stat / (n1 * n2) - 1.0 if n1 * n2 > 0 else np.nan\n    return {\n        \"U\": float(u_stat),\n        \"p_value\": float(p_value),\n        \"r_rank_biserial\": float(r_rb),\n        \"isr_median\": float(np.median(isr)),\n        \"random_median\": float(np.median(rand)),\n    }\n\n\ndef mannwhitney_isr_star(df: pd.DataFrame) -> dict | None:\n    isr = df[df[\"condition\"] == \"ISR\"][\"ISR_star\"].dropna().values.astype(float)\n    rand = df[df[\"condition\"] == \"RANDOM\"][\"ISR_star\"].dropna().values.astype(float)\n    if len(isr) < 2 or len(rand) < 2:\n        return None\n    n1, n2 = len(isr), len(rand)\n    u_stat, p_value = stats.mannwhitneyu(isr, rand, alternative=\"greater\")\n    r_rb = 2.0 * u_stat / (n1 * n2) - 1.0\n    return {\n        \"U\": float(u_stat),\n        \"p_value\": float(p_value),\n        \"r_rank_biserial\": float(r_rb),\n        \"isr_median\": float(np.median(isr)),\n        \"random_median\": float(np.median(rand)),\n        \"isr_mean\": float(np.mean(isr)),\n        \"random_mean\": float(np.mean(rand)),\n    }\n\n\ndef bca_bootstrap_ci(df: pd.DataFrame, metric: str, n_boot: int = 10000,\n                      rng_seed: int = 42) -> dict:\n    \"\"\"BCa 95% CI for per-condition means of a metric.\"\"\"\n    result = {}\n    for cond in [\"ISR\", \"RANDOM\"]:\n        vals = df[df[\"condition\"] == cond][metric].values\n        if len(vals) < 2:\n            result[cond] = {\"mean\": float(vals.mean()) if len(vals) else np.nan,\n                            \"ci_lo\": np.nan, \"ci_hi\": np.nan}\n            continue\n        res = stats.bootstrap(\n            (vals,), np.mean, n_resamples=n_boot,\n            confidence_level=0.95, method=\"BCa\",\n            random_state=np.random.default_rng(rng_seed),\n        )\n        result[cond] = {\n            \"mean\": float(vals.mean()),\n            \"ci_lo\": float(res.confidence_interval.low),\n            \"ci_hi\": float(res.confidence_interval.high),\n        }\n    return result\n\n\ndef bayes_factor_h7_domination(df: pd.DataFrame) -> dict:\n    \"\"\"BF10 for H7-domination rate difference (beta-binomial conjugate).\n    H0: ISR and Random share same domination rate.\n    H1: independent rates. Prior: Beta(1,1) on each.\n    \"\"\"\n    isr_sub = df[df[\"condition\"] == \"ISR\"]\n    rand_sub = df[df[\"condition\"] == \"RANDOM\"]\n    k_isr = int((isr_sub[\"H7_rate\"] >= 0.5).sum())\n    n_isr = len(isr_sub)\n    k_rand = int((rand_sub[\"H7_rate\"] >= 0.5).sum())\n    n_rand = len(rand_sub)\n    k_total = k_isr + k_rand\n    n_total = n_isr + n_rand\n\n    # log marginal under H0 (shared rate)\n    log_m_h0 = betaln(1 + k_total, 1 + n_total - k_total) - betaln(1, 1)\n    # log marginal under H1 (independent rates)\n    log_m_h1 = (betaln(1 + k_isr, 1 + n_isr - k_isr) - betaln(1, 1)\n                + betaln(1 + k_rand, 1 + n_rand - k_rand) - betaln(1, 1))\n    log_bf10 = log_m_h1 - log_m_h0\n    bf10 = float(np.exp(log_bf10))\n\n    return {\n        \"k_isr\": k_isr, \"n_isr\": n_isr,\n        \"k_rand\": k_rand, \"n_rand\": n_rand,\n        \"bf10\": bf10,\n        \"log_bf10\": float(log_bf10),\n        \"interpretation\": _interpret_bf(bf10),\n    }\n\n\ndef _interpret_bf(bf: float) -> str:\n    if bf > 100:\n        return \"extreme evidence for H1\"\n    if bf > 30:\n        return \"very strong evidence for H1\"\n    if bf > 10:\n        return \"strong evidence for H1\"\n    if bf > 3:\n        return \"moderate evidence for H1\"\n    if bf > 1:\n        return \"anecdotal evidence for H1\"\n    if bf > 1/3:\n        return \"anecdotal evidence (inconclusive)\"\n    if bf > 1/10:\n        return \"moderate evidence for H0\"\n    return \"strong evidence for H0\"\n\n\ndef condition_stats(df: pd.DataFrame) -> pd.DataFrame:\n    metrics = [\"PR\", \"H7_rate\", \"genuine_rate\", \"SNH_rate\"]\n    rows = []\n    for cond in [\"ISR\", \"RANDOM\"]:\n        sub = df[df[\"condition\"] == cond]\n        row = {\"condition\": cond, \"n_seeds\": len(sub)}\n        for m in metrics:\n            vals = sub[m].values\n            row[f\"{m}_mean\"] = vals.mean()\n            row[f\"{m}_std\"] = vals.std(ddof=1) if len(vals) > 1 else 0.0\n        isr_vals = sub[\"ISR_star\"].dropna().values.astype(float)\n        row[\"ISR_star_mean\"] = isr_vals.mean() if len(isr_vals) else np.nan\n        row[\"ISR_star_std\"] = isr_vals.std(ddof=1) if len(isr_vals) > 1 else 0.0\n        rows.append(row)\n    return pd.DataFrame(rows)\n\n\n# --- Formatting ---\n\ndef fmt_pct(val: float) -> str:\n    return f\"{val*100:.1f}\\\\%\"\n\ndef fmt_or(val: float) -> str:\n    return \"$\\\\infty$\" if np.isinf(val) else f\"{val:.2f}\"\n\ndef fmt_ci(lo: float, hi: float) -> str:\n    lo_s = f\"{lo:.2f}\" if not np.isnan(lo) else \"0\"\n    hi_s = \"$\\\\infty$\" if np.isinf(hi) or np.isnan(hi) else f\"{hi:.2f}\"\n    return f\"[{lo_s}, {hi_s}]\"\n\ndef fmt_p(p: float) -> str:\n    if p < 0.001:\n        return \"$<$0.001\"\n    return f\"{p:.3f}\"\n\ndef fmt_mean_std(mean: float, std: float, pct: bool = False) -> str:\n    if pct:\n        return f\"{mean*100:.1f} $\\\\pm$ {std*100:.1f}\\\\%\"\n    return f\"{mean:.1f} $\\\\pm$ {std:.1f}\"\n\ndef fmt_bca(bca: dict, pct: bool = False) -> str:\n    m = bca[\"mean\"]\n    lo, hi = bca[\"ci_lo\"], bca[\"ci_hi\"]\n    if pct:\n        return f\"{m*100:.1f}\\\\% [{lo*100:.1f}, {hi*100:.1f}]\"\n    return f\"{m:.1f} [{lo:.1f}, {hi:.1f}]\"\n\n\n# --- Console output ---\n\ndef print_per_seed_table(df: pd.DataFrame):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  PER-SEED RESULTS\")\n    print(\"=\" * 90)\n    cols = [\"condition\", \"seed\", \"PR\", \"H7_count\", \"H7_rate\", \"H1_count\",\n            \"H8_count\", \"genuine_count\", \"genuine_rate\", \"CI_count\", \"SNH_count\", \"SNH_rate\",\n            \"ISR_star\"]\n    fmt = df[cols].copy()\n    for c in [\"H7_rate\", \"genuine_rate\", \"SNH_rate\"]:\n        fmt[c] = fmt[c].apply(lambda v: f\"{v*100:.1f}%\")\n    fmt[\"ISR_star\"] = fmt[\"ISR_star\"].apply(lambda v: f\"{v:.4f}\" if pd.notna(v) else \"---\")\n    print(fmt.to_string(index=False))\n\n\ndef print_condition_stats(cond_df: pd.DataFrame):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  CONDITION-LEVEL STATISTICS (mean +/- SD)\")\n    print(\"=\" * 90)\n    for _, row in cond_df.iterrows():\n        n = int(row['n_seeds'])\n        print(f\"\\n  {row['condition']} (n={n} seeds):\")\n        print(f\"    PR:           {row['PR_mean']:.1f} +/- {row['PR_std']:.1f}\")\n        print(f\"    H7 rate:      {row['H7_rate_mean']*100:.1f} +/- {row['H7_rate_std']*100:.1f}%\")\n        print(f\"    Genuine rate: {row['genuine_rate_mean']*100:.1f} +/- {row['genuine_rate_std']*100:.1f}%\")\n        print(f\"    S-NH rate:    {row['SNH_rate_mean']*100:.1f} +/- {row['SNH_rate_std']*100:.1f}%\")\n        if not np.isnan(row.get('ISR_star_mean', np.nan)):\n            print(f\"    ISR*:         {row['ISR_star_mean']:.4f} +/- {row['ISR_star_std']:.4f}\")\n\n\ndef print_tests(fisher, perm, mw, bf, bca_h7, bca_gen, mw_isr_star=None):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  STATISTICAL TESTS\")\n    print(\"=\" * 90)\n\n    print(\"\\n  1. H7 Domination Fisher Exact Test (H7-dominated = H7% >= 50%)\")\n    print(f\"     ISR:    {fisher['ISR']['h7_dom']} dominated / {fisher['ISR']['n']} seeds\")\n    print(f\"     RANDOM: {fisher['RANDOM']['h7_dom']} dominated / {fisher['RANDOM']['n']} seeds\")\n    print(f\"     Contingency: {fisher['table']}\")\n    or_str = \"inf\" if np.isinf(fisher['odds_ratio']) else f\"{fisher['odds_ratio']:.4f}\"\n    print(f\"     OR = {or_str}, 95% CI = [{fisher['or_ci_lo']:.4f}, {fisher['or_ci_hi']:.4f}]\"\n          if not np.isnan(fisher['or_ci_lo']) else f\"     OR = {or_str}, 95% CI = N/A\")\n    print(f\"     p-value (one-sided, greater): {fisher['p_value']:.4f}\")\n\n    print(f\"\\n  2. Genuine Rate Permutation Test (n_perm={perm['n_perm']})\")\n    print(f\"     ISR mean:    {perm['isr_mean']*100:.2f}%\")\n    print(f\"     RANDOM mean: {perm['random_mean']*100:.2f}%\")\n    print(f\"     Diff: {perm['observed_diff']*100:.2f} pp, p = {perm['p_value']:.4f}\")\n\n    print(f\"\\n  3. H7 Rate Mann-Whitney U Test\")\n    print(f\"     ISR median:    {mw['isr_median']*100:.1f}%\")\n    print(f\"     RANDOM median: {mw['random_median']*100:.1f}%\")\n    print(f\"     U = {mw['U']:.1f}, p = {mw['p_value']:.4f}\")\n    print(f\"     Rank-biserial r = {mw['r_rank_biserial']:.4f}\")\n\n    print(f\"\\n  4. Bayes Factor (H7 Domination, Beta-Binomial)\")\n    print(f\"     ISR:    {bf['k_isr']}/{bf['n_isr']} dominated\")\n    print(f\"     RANDOM: {bf['k_rand']}/{bf['n_rand']} dominated\")\n    print(f\"     BF10 = {bf['bf10']:.4f} ({bf['interpretation']})\")\n\n    print(f\"\\n  5. BCa Bootstrap 95% CI (n_boot resamples)\")\n    for label, bca in [(\"H7 rate\", bca_h7), (\"Genuine rate\", bca_gen)]:\n        print(f\"     {label}:\")\n        for cond in [\"ISR\", \"RANDOM\"]:\n            b = bca[cond]\n            print(f\"       {cond}: {b['mean']*100:.1f}% [{b['ci_lo']*100:.1f}, {b['ci_hi']*100:.1f}]\"\n                  if not np.isnan(b['ci_lo']) else f\"       {cond}: {b['mean']*100:.1f}% [N/A]\")\n\n\n# --- Markdown generation (appendix-ready) ---\n\ndef generate_markdown(df: pd.DataFrame, cond_df: pd.DataFrame,\n                      fisher: dict, perm: dict, mw: dict,\n                      bf: dict, bca_h7: dict, bca_gen: dict) -> str:\n    L = []\n    L.append(\"## D134: ISR vs Random Statistical Analysis\\n\")\n\n    # Per-seed table\n    L.append(\"### Table A1: Per-Seed Hacking Taxonomy (4B Qwen3, 500 steps)\\n\")\n    L.append(\"| Condition | Seed | PR | H7 | H7\\\\% | H1 | H8 | Genuine | Gen\\\\% | CI | S-NH | S-NH\\\\% |\")\n    L.append(\"|:----------|-----:|---:|---:|-----:|---:|---:|--------:|------:|---:|-----:|-------:|\")\n    for _, r in df.iterrows():\n        L.append(\n            f\"| {r['condition']} | {r['seed']} | {int(r['PR'])} | {int(r['H7_count'])} | \"\n            f\"{r['H7_rate']*100:.1f} | {int(r['H1_count'])} | {int(r['H8_count'])} | \"\n            f\"{int(r['genuine_count'])} | {r['genuine_rate']*100:.1f} | {int(r['CI_count'])} | \"\n            f\"{int(r['SNH_count'])} | {r['SNH_rate']*100:.1f} |\"\n        )\n\n    # Condition summary with BCa CI\n    L.append(\"\\n### Table A2: Condition-Level Summary\\n\")\n    L.append(\"| Condition | $n$ | PR (mean$\\\\pm$SD) | H7\\\\% (mean$\\\\pm$SD) | H7\\\\% BCa 95\\\\% CI | Gen\\\\% (mean$\\\\pm$SD) | Gen\\\\% BCa 95\\\\% CI |\")\n    L.append(\"|:----------|----:|:------------------|:-------------------|:-----------------|:-------------------|:-----------------|\")\n    for _, r in cond_df.iterrows():\n        cond = r[\"condition\"]\n        h7_bca = bca_h7.get(cond, {})\n        gen_bca = bca_gen.get(cond, {})\n        h7_ci = f\"[{h7_bca['ci_lo']*100:.1f}, {h7_bca['ci_hi']*100:.1f}]\" if h7_bca and not np.isnan(h7_bca.get('ci_lo', np.nan)) else \"N/A\"\n        gen_ci = f\"[{gen_bca['ci_lo']*100:.1f}, {gen_bca['ci_hi']*100:.1f}]\" if gen_bca and not np.isnan(gen_bca.get('ci_lo', np.nan)) else \"N/A\"\n        L.append(\n            f\"| {cond} | {int(r['n_seeds'])} | \"\n            f\"{r['PR_mean']:.1f}$\\\\pm${r['PR_std']:.1f} | \"\n            f\"{r['H7_rate_mean']*100:.1f}$\\\\pm${r['H7_rate_std']*100:.1f} | \"\n            f\"{h7_ci} | \"\n            f\"{r['genuine_rate_mean']*100:.1f}$\\\\pm${r['genuine_rate_std']*100:.1f} | \"\n            f\"{gen_ci} |\"\n        )\n\n    # Statistical tests\n    if fisher and perm and mw and bf:\n        L.append(\"\\n### Statistical Tests\\n\")\n\n        # Fisher\n        or_str = \"$\\\\infty$\" if np.isinf(fisher['odds_ratio']) else f\"{fisher['odds_ratio']:.2f}\"\n        ci_lo = f\"{fisher['or_ci_lo']:.2f}\" if not np.isnan(fisher['or_ci_lo']) else \"0\"\n        ci_hi = \"$\\\\infty$\" if np.isinf(fisher.get('or_ci_hi', np.inf)) or np.isnan(fisher.get('or_ci_hi', np.nan)) else f\"{fisher['or_ci_hi']:.2f}\"\n        L.append(\"**1. H7 Domination Fisher Exact Test** (threshold: H7$\\\\geq$50\\\\% of proved)\")\n        L.append(f\"- ISR: {fisher['ISR']['h7_dom']}/{fisher['ISR']['n']} seeds H7-dominated; \"\n                 f\"Random: {fisher['RANDOM']['h7_dom']}/{fisher['RANDOM']['n']}\")\n        L.append(f\"- OR = {or_str}, 95\\\\% exact CI = [{ci_lo}, {ci_hi}], \"\n                 f\"$p$ = {fmt_p(fisher['p_value'])}\")\n        L.append(\"\")\n\n        # Permutation\n        L.append(f\"**2. Genuine Rate Permutation Test** ($n$ = {perm['n_perm']:,} permutations)\")\n        L.append(f\"- ISR mean: {perm['isr_mean']*100:.2f}\\\\%, Random mean: {perm['random_mean']*100:.2f}\\\\%\")\n        L.append(f\"- $\\\\Delta$ = {perm['observed_diff']*100:.2f} pp, $p$ = {fmt_p(perm['p_value'])}\")\n        L.append(\"\")\n\n        # Mann-Whitney\n        L.append(\"**3. H7 Rate Mann-Whitney $U$ Test**\")\n        L.append(f\"- ISR median: {mw['isr_median']*100:.1f}\\\\%, Random median: {mw['random_median']*100:.1f}\\\\%\")\n        L.append(f\"- $U$ = {mw['U']:.1f}, $p$ = {fmt_p(mw['p_value'])}, \"\n                 f\"rank-biserial $r$ = {mw['r_rank_biserial']:.3f}\")\n        L.append(\"\")\n\n        # Bayes Factor\n        L.append(\"**4. Bayes Factor** (Beta-Binomial conjugate, prior: Beta(1,1))\")\n        L.append(f\"- $BF_{{10}}$ = {bf['bf10']:.2f} ({bf['interpretation']})\")\n        L.append(f\"- ISR: {bf['k_isr']}/{bf['n_isr']} H7-dominated, \"\n                 f\"Random: {bf['k_rand']}/{bf['n_rand']}\")\n\n    return \"\\n\".join(L) + \"\\n\"\n\n\n# --- Main ---\n\ndef main():\n    args = parse_args()\n    data_dir = Path(args.data_dir)\n\n    if not data_dir.exists():\n        print(f\"ERROR: data directory {data_dir} does not exist\", file=sys.stderr)\n        sys.exit(1)\n\n    if args.prefix:\n        prefixes = [args.prefix]\n    elif args.prefixes:\n        prefixes = [p.strip() for p in args.prefixes.split(\",\")]\n    else:\n        prefixes = MODE_PREFIXES[args.mode]\n    print(f\"Mode: {args.mode} | Prefixes: {prefixes}\")\n\n    runs = discover_runs(data_dir, prefixes)\n    if not runs:\n        print(f\"ERROR: no runs found in {data_dir} with prefixes {prefixes}\", file=sys.stderr)\n        sys.exit(1)\n\n    isr_count = sum(1 for r in runs if r[\"condition\"] == \"ISR\")\n    rand_count = sum(1 for r in runs if r[\"condition\"] == \"RANDOM\")\n    print(f\"Found {len(runs)} runs: {isr_count} ISR, {rand_count} RANDOM\")\n    for r in runs:\n        print(f\"  {r['condition']:6s} s{r['seed']} <- {r['dir_name']}\")\n\n    df = build_table(runs)\n    print_per_seed_table(df)\n\n    cond_df = condition_stats(df)\n    print_condition_stats(cond_df)\n\n    if isr_count < 2 or rand_count < 2:\n        print(\"\\nWARNING: need >= 2 seeds per condition for statistical tests, skipping.\",\n              file=sys.stderr)\n        bca_h7 = bca_bootstrap_ci(df, \"H7_rate\", args.n_boot, args.seed)\n        bca_gen = bca_bootstrap_ci(df, \"genuine_rate\", args.n_boot, args.seed)\n        if args.output:\n            md = generate_markdown(df, cond_df, {}, {}, {}, {}, bca_h7, bca_gen)\n            Path(args.output).write_text(md)\n            print(f\"\\nMarkdown written to {args.output}\")\n        return\n\n    fisher = fisher_h7_domination(df)\n    perm = permutation_test_genuine(df, n_perm=args.n_perm, rng_seed=args.seed)\n    mw = mannwhitney_h7(df)\n    bf = bayes_factor_h7_domination(df)\n    bca_h7 = bca_bootstrap_ci(df, \"H7_rate\", args.n_boot, args.seed)\n    bca_gen = bca_bootstrap_ci(df, \"genuine_rate\", args.n_boot, args.seed)\n\n    print_tests(fisher, perm, mw, bf, bca_h7, bca_gen)\n\n    md = generate_markdown(df, cond_df, fisher, perm, mw, bf, bca_h7, bca_gen)\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  MARKDOWN OUTPUT (appendix-ready)\")\n    print(\"=\" * 90)\n    print(md)\n\n    if args.output:\n        Path(args.output).parent.mkdir(parents=True, exist_ok=True)\n        Path(args.output).write_text(md)\n        print(f\"Markdown written to {args.output}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 474,
        "oldLines": 7,
        "newStart": 474,
        "newLines": 14,
        "lines": [
          "             print(f\"       {cond}: {b['mean']*100:.1f}% [{b['ci_lo']*100:.1f}, {b['ci_hi']*100:.1f}]\"",
          "                   if not np.isnan(b['ci_lo']) else f\"       {cond}: {b['mean']*100:.1f}% [N/A]\")",
          " ",
          "+    if mw_isr_star:",
          "+        print(f\"\\n  6. ISR* (Proved-Only Mean ISR) Mann-Whitney U Test\")",
          "+        print(f\"     ISR mean:    {mw_isr_star['isr_mean']:.4f}, median: {mw_isr_star['isr_median']:.4f}\")",
          "+        print(f\"     RANDOM mean: {mw_isr_star['random_mean']:.4f}, median: {mw_isr_star['random_median']:.4f}\")",
          "+        print(f\"     U = {mw_isr_star['U']:.1f}, p = {mw_isr_star['p_value']:.4f}\")",
          "+        print(f\"     Rank-biserial r = {mw_isr_star['r_rank_biserial']:.4f}\")",
          " ",
          "+",
          " # --- Markdown generation (appendix-ready) ---",
          " ",
          " def generate_markdown(df: pd.DataFrame, cond_df: pd.DataFrame,"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 42_

**Edit 8**: Update `generate_markdown` signature and add ISR* to Table A1 + add MW test.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "bada6896-a78f-4ba6-bbab-8ab814c4b52f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wrp6KT8GrwjghtZBnt9E7q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 645,
      "cache_read_input_tokens": 49523,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 645
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

_source line 43_

<details open><summary>🔧 Tool call — Edit · `toolu_01WovXbW6X7YisyDt7owkmoa`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/scripts/d134_analysis.py",
  "old_string": "def generate_markdown(df: pd.DataFrame, cond_df: pd.DataFrame,\n                      fisher: dict, perm: dict, mw: dict,\n                      bf: dict, bca_h7: dict, bca_gen: dict) -> str:",
  "new_string": "def generate_markdown(df: pd.DataFrame, cond_df: pd.DataFrame,\n                      fisher: dict, perm: dict, mw: dict,\n                      bf: dict, bca_h7: dict, bca_gen: dict,\n                      mw_isr_star: dict = None) -> str:"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "88520418-1f64-48ca-9905-87f80073a694",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wrp6KT8GrwjghtZBnt9E7q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 645,
      "cache_read_input_tokens": 49523,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 645
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

_source line 44 · 2026-05-18T23:33:04.134Z_

<details><summary>↩ Tool result · `toolu_01WovXbW6X7YisyDt7owkmoa`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/scripts/d134_analysis.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "775975c1-b65d-4850-a3e2-e4b27372b83b",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/scripts/d134_analysis.py",
    "oldString": "def generate_markdown(df: pd.DataFrame, cond_df: pd.DataFrame,\n                      fisher: dict, perm: dict, mw: dict,\n                      bf: dict, bca_h7: dict, bca_gen: dict) -> str:",
    "newString": "def generate_markdown(df: pd.DataFrame, cond_df: pd.DataFrame,\n                      fisher: dict, perm: dict, mw: dict,\n                      bf: dict, bca_h7: dict, bca_gen: dict,\n                      mw_isr_star: dict = None) -> str:",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"D134 experiment analysis: multi-seed ISR vs Random, 4B GRPO training.\nReads taxonomy data from classify.json, taxonomy.json, or top-level taxonomy files.\nComputes summary stats, statistical tests (Fisher, Mann-Whitney, permutation, Bayes Factor),\nand BCa bootstrap CIs. Outputs appendix-ready markdown.\n\"\"\"\n\nimport argparse\nimport json\nimport re\nimport sys\nfrom pathlib import Path\n\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\nfrom scipy.special import betaln\n\nCONDITION_MAP = [\n    (\"d134_4b_isr\", \"ISR\"),\n    (\"d134_4b_random\", \"RANDOM\"),\n    (\"plan002_additive\", \"ISR\"),\n    (\"plan018_additive_random\", \"RANDOM\"),\n    (\"plan018_random\", \"RANDOM\"),\n]\n\nMODE_PREFIXES = {\n    \"d134_only\": [\"d134_4b\"],\n    \"all\": [\"d134_4b\", \"plan002_additive_b01\", \"plan018_additive_random_b01\", \"plan018_random\"],\n}\n\n\ndef parse_args():\n    p = argparse.ArgumentParser(description=\"D134 multi-seed analysis and statistical tests\")\n    p.add_argument(\"--data_dir\", type=str, default=\"/root/autodl-tmp/outputs\",\n                   help=\"Directory containing experiment outputs\")\n    p.add_argument(\"--mode\", type=str, default=\"d134_only\", choices=list(MODE_PREFIXES),\n                   help=\"d134_only = matched 5+5 design (default); all = include original seeds\")\n    p.add_argument(\"--prefix\", type=str, default=None,\n                   help=\"(Legacy) Single prefix filter; overrides mode/prefixes\")\n    p.add_argument(\"--prefixes\", type=str, default=None,\n                   help=\"Comma-separated prefixes; overrides --mode\")\n    p.add_argument(\"--output\", type=str, default=None,\n                   help=\"Write markdown summary to this file\")\n    p.add_argument(\"--n_perm\", type=int, default=10000,\n                   help=\"Number of permutations for permutation test\")\n    p.add_argument(\"--n_boot\", type=int, default=10000,\n                   help=\"Number of bootstrap resamples for BCa CI\")\n    p.add_argument(\"--seed\", type=int, default=42,\n                   help=\"Random seed for permutation/bootstrap\")\n    return p.parse_args()\n\n\n# --- Data loading ---\n\ndef match_condition(name: str) -> str | None:\n    best_prefix = \"\"\n    best_cond = None\n    for prefix, cond in CONDITION_MAP:\n        if name.startswith(prefix) and len(prefix) > len(best_prefix):\n            best_prefix = prefix\n            best_cond = cond\n    return best_cond\n\n\ndef extract_seed(name: str) -> int | None:\n    m = re.search(r'_s(\\d+)', name)\n    return int(m.group(1)) if m else None\n\n\ndef load_eval_results(path: Path) -> dict | None:\n    if not path.exists():\n        return None\n    with open(path) as f:\n        data = json.load(f)\n    if \"eval_results\" in data:\n        return data[\"eval_results\"]\n    return data\n\n\ndef load_taxonomy_unified(path: Path) -> dict | None:\n    with open(path) as f:\n        raw = json.load(f)\n    t = raw.get(\"taxonomy\", {})\n    proved = t.get(\"proved\", 0)\n    if proved == 0:\n        return None\n    h7 = t.get(\"H7\", 0)\n    h1 = t.get(\"H1_exact\", 0)\n    h8 = t.get(\"H8\", 0)\n    genuine = t.get(\"genuine\", 0)\n    return {\n        \"n_total\": 100, \"n_proved\": proved,\n        \"h7_total_count\": h7, \"h7_total_rate\": h7 / proved,\n        \"h1_strict_count\": h1, \"h8_conjunction_collapse_count\": h8,\n        \"genuine_count\": genuine, \"genuine_rate\": genuine / proved,\n        \"content_independent_count\": 0,\n    }\n\n\ndef load_taxonomy_verification(path: Path) -> dict | None:\n    with open(path) as f:\n        raw = json.load(f)\n    proved = raw.get(\"proved\", 0)\n    if proved == 0:\n        return None\n    tax = raw.get(\"taxonomy\", {})\n    h7 = tax.get(\"h7\", {}).get(\"count\", 0)\n    h1 = tax.get(\"h1_exact\", {}).get(\"count\", 0)\n    h8 = tax.get(\"h8\", {}).get(\"count\", 0)\n    genuine = tax.get(\"genuine\", {}).get(\"count\", 0)\n    return {\n        \"n_total\": raw.get(\"total\", 100), \"n_proved\": proved,\n        \"h7_total_count\": h7, \"h7_total_rate\": h7 / proved,\n        \"h1_strict_count\": h1, \"h8_conjunction_collapse_count\": h8,\n        \"genuine_count\": genuine, \"genuine_rate\": genuine / proved,\n        \"content_independent_count\": 0,\n    }\n\n\ndef discover_runs(data_dir: Path, prefixes: list[str]) -> list[dict]:\n    runs = []\n    seen = set()\n    for entry in sorted(data_dir.iterdir()):\n        name = entry.name\n        if not any(name.startswith(p) for p in prefixes):\n            continue\n        cond = match_condition(name)\n        seed_val = extract_seed(name)\n        if cond is None or seed_val is None:\n            continue\n        key = (cond, seed_val)\n        if key in seen:\n            continue\n        data = None\n        if entry.is_dir():\n            for fname in [\"classify.json\", \"taxonomy.json\"]:\n                data = load_eval_results(entry / fname)\n                if data is not None:\n                    break\n            if data is None:\n                continue\n        elif entry.is_file():\n            if name.endswith(\"_taxonomy_unified.json\"):\n                data = load_taxonomy_unified(entry)\n            elif name.endswith(\"_taxonomy_verification.json\"):\n                data = load_taxonomy_verification(entry)\n            if data is None:\n                continue\n        else:\n            continue\n        seen.add(key)\n        isr_star = None\n        if entry.is_dir():\n            eval_path = entry / \"eval_results.json\"\n            if eval_path.exists():\n                with open(eval_path) as ef:\n                    eval_raw = json.load(ef)\n                isr_star = eval_raw.get(\"summary\", {}).get(\"proved_only_mean_isr\")\n        runs.append({\"dir_name\": name, \"seed\": seed_val, \"condition\": cond,\n                      \"data\": data, \"isr_star\": isr_star})\n    return runs\n\n\ndef compute_row(run: dict) -> dict:\n    d = run[\"data\"]\n    n_proved = d.get(\"n_proved\", 0)\n    n_total = d.get(\"n_total\", 100)\n    h7 = d.get(\"h7_total_count\", 0)\n    h7_rate = d.get(\"h7_total_rate\", h7 / n_proved if n_proved > 0 else 0.0)\n    h1 = d.get(\"h1_strict_count\", 0)\n    h8 = d.get(\"h8_conjunction_collapse_count\", 0)\n    genuine = d.get(\"genuine_count\", 0)\n    genuine_rate = d.get(\"genuine_rate\", genuine / n_proved if n_proved > 0 else 0.0)\n    ci = d.get(\"content_independent_count\", 0)\n    snh = max(genuine - ci, 0)\n    snh_rate = snh / n_proved if n_proved > 0 else 0.0\n    return {\n        \"seed\": run[\"seed\"], \"condition\": run[\"condition\"], \"n_total\": n_total,\n        \"PR\": n_proved, \"H7_count\": h7, \"H7_rate\": h7_rate,\n        \"H1_count\": h1, \"H8_count\": h8,\n        \"genuine_count\": genuine, \"genuine_rate\": genuine_rate,\n        \"CI_count\": ci, \"SNH_count\": snh, \"SNH_rate\": snh_rate,\n        \"ISR_star\": run.get(\"isr_star\"),\n    }\n\n\ndef build_table(runs: list[dict]) -> pd.DataFrame:\n    rows = [compute_row(r) for r in runs]\n    df = pd.DataFrame(rows)\n    df = df.sort_values([\"condition\", \"seed\"]).reset_index(drop=True)\n    return df\n\n\n# --- Statistical tests ---\n\ndef fisher_h7_domination(df: pd.DataFrame) -> dict:\n    results = {}\n    for cond in [\"ISR\", \"RANDOM\"]:\n        sub = df[df[\"condition\"] == cond]\n        results[cond] = {\n            \"n\": len(sub),\n            \"h7_dom\": int((sub[\"H7_rate\"] >= 0.5).sum()),\n            \"not_h7_dom\": int((sub[\"H7_rate\"] < 0.5).sum()),\n        }\n    table = np.array([\n        [results[\"ISR\"][\"h7_dom\"], results[\"ISR\"][\"not_h7_dom\"]],\n        [results[\"RANDOM\"][\"h7_dom\"], results[\"RANDOM\"][\"not_h7_dom\"]],\n    ])\n    odds_ratio, p_value = stats.fisher_exact(table, alternative=\"greater\")\n\n    # 95% exact CI via scipy.stats.contingency\n    or_ci_lo, or_ci_hi = np.nan, np.nan\n    try:\n        ct = stats.contingency.odds_ratio(table)\n        ci = ct.confidence_interval(confidence_level=0.95)\n        or_ci_lo, or_ci_hi = ci.low, ci.high\n    except Exception:\n        pass\n\n    return {\n        \"table\": table.tolist(),\n        \"ISR\": results[\"ISR\"],\n        \"RANDOM\": results[\"RANDOM\"],\n        \"odds_ratio\": odds_ratio,\n        \"or_ci_lo\": or_ci_lo,\n        \"or_ci_hi\": or_ci_hi,\n        \"p_value\": p_value,\n    }\n\n\ndef permutation_test_genuine(df: pd.DataFrame, n_perm: int = 10000,\n                              rng_seed: int = 42) -> dict:\n    isr = df[df[\"condition\"] == \"ISR\"][\"genuine_rate\"].values\n    rand = df[df[\"condition\"] == \"RANDOM\"][\"genuine_rate\"].values\n    observed = isr.mean() - rand.mean()\n    pooled = np.concatenate([isr, rand])\n    n_isr = len(isr)\n    rng = np.random.default_rng(rng_seed)\n    count = 0\n    for _ in range(n_perm):\n        perm = rng.permutation(pooled)\n        if perm[:n_isr].mean() - perm[n_isr:].mean() >= observed:\n            count += 1\n    return {\n        \"observed_diff\": float(observed),\n        \"p_value\": count / n_perm,\n        \"n_perm\": n_perm,\n        \"isr_mean\": float(isr.mean()),\n        \"random_mean\": float(rand.mean()),\n    }\n\n\ndef mannwhitney_h7(df: pd.DataFrame) -> dict:\n    isr = df[df[\"condition\"] == \"ISR\"][\"H7_rate\"].values\n    rand = df[df[\"condition\"] == \"RANDOM\"][\"H7_rate\"].values\n    n1, n2 = len(isr), len(rand)\n    u_stat, p_value = stats.mannwhitneyu(isr, rand, alternative=\"greater\")\n    r_rb = 2.0 * u_stat / (n1 * n2) - 1.0 if n1 * n2 > 0 else np.nan\n    return {\n        \"U\": float(u_stat),\n        \"p_value\": float(p_value),\n        \"r_rank_biserial\": float(r_rb),\n        \"isr_median\": float(np.median(isr)),\n        \"random_median\": float(np.median(rand)),\n    }\n\n\ndef mannwhitney_isr_star(df: pd.DataFrame) -> dict | None:\n    isr = df[df[\"condition\"] == \"ISR\"][\"ISR_star\"].dropna().values.astype(float)\n    rand = df[df[\"condition\"] == \"RANDOM\"][\"ISR_star\"].dropna().values.astype(float)\n    if len(isr) < 2 or len(rand) < 2:\n        return None\n    n1, n2 = len(isr), len(rand)\n    u_stat, p_value = stats.mannwhitneyu(isr, rand, alternative=\"greater\")\n    r_rb = 2.0 * u_stat / (n1 * n2) - 1.0\n    return {\n        \"U\": float(u_stat),\n        \"p_value\": float(p_value),\n        \"r_rank_biserial\": float(r_rb),\n        \"isr_median\": float(np.median(isr)),\n        \"random_median\": float(np.median(rand)),\n        \"isr_mean\": float(np.mean(isr)),\n        \"random_mean\": float(np.mean(rand)),\n    }\n\n\ndef bca_bootstrap_ci(df: pd.DataFrame, metric: str, n_boot: int = 10000,\n                      rng_seed: int = 42) -> dict:\n    \"\"\"BCa 95% CI for per-condition means of a metric.\"\"\"\n    result = {}\n    for cond in [\"ISR\", \"RANDOM\"]:\n        vals = df[df[\"condition\"] == cond][metric].values\n        if len(vals) < 2:\n            result[cond] = {\"mean\": float(vals.mean()) if len(vals) else np.nan,\n                            \"ci_lo\": np.nan, \"ci_hi\": np.nan}\n            continue\n        res = stats.bootstrap(\n            (vals,), np.mean, n_resamples=n_boot,\n            confidence_level=0.95, method=\"BCa\",\n            random_state=np.random.default_rng(rng_seed),\n        )\n        result[cond] = {\n            \"mean\": float(vals.mean()),\n            \"ci_lo\": float(res.confidence_interval.low),\n            \"ci_hi\": float(res.confidence_interval.high),\n        }\n    return result\n\n\ndef bayes_factor_h7_domination(df: pd.DataFrame) -> dict:\n    \"\"\"BF10 for H7-domination rate difference (beta-binomial conjugate).\n    H0: ISR and Random share same domination rate.\n    H1: independent rates. Prior: Beta(1,1) on each.\n    \"\"\"\n    isr_sub = df[df[\"condition\"] == \"ISR\"]\n    rand_sub = df[df[\"condition\"] == \"RANDOM\"]\n    k_isr = int((isr_sub[\"H7_rate\"] >= 0.5).sum())\n    n_isr = len(isr_sub)\n    k_rand = int((rand_sub[\"H7_rate\"] >= 0.5).sum())\n    n_rand = len(rand_sub)\n    k_total = k_isr + k_rand\n    n_total = n_isr + n_rand\n\n    # log marginal under H0 (shared rate)\n    log_m_h0 = betaln(1 + k_total, 1 + n_total - k_total) - betaln(1, 1)\n    # log marginal under H1 (independent rates)\n    log_m_h1 = (betaln(1 + k_isr, 1 + n_isr - k_isr) - betaln(1, 1)\n                + betaln(1 + k_rand, 1 + n_rand - k_rand) - betaln(1, 1))\n    log_bf10 = log_m_h1 - log_m_h0\n    bf10 = float(np.exp(log_bf10))\n\n    return {\n        \"k_isr\": k_isr, \"n_isr\": n_isr,\n        \"k_rand\": k_rand, \"n_rand\": n_rand,\n        \"bf10\": bf10,\n        \"log_bf10\": float(log_bf10),\n        \"interpretation\": _interpret_bf(bf10),\n    }\n\n\ndef _interpret_bf(bf: float) -> str:\n    if bf > 100:\n        return \"extreme evidence for H1\"\n    if bf > 30:\n        return \"very strong evidence for H1\"\n    if bf > 10:\n        return \"strong evidence for H1\"\n    if bf > 3:\n        return \"moderate evidence for H1\"\n    if bf > 1:\n        return \"anecdotal evidence for H1\"\n    if bf > 1/3:\n        return \"anecdotal evidence (inconclusive)\"\n    if bf > 1/10:\n        return \"moderate evidence for H0\"\n    return \"strong evidence for H0\"\n\n\ndef condition_stats(df: pd.DataFrame) -> pd.DataFrame:\n    metrics = [\"PR\", \"H7_rate\", \"genuine_rate\", \"SNH_rate\"]\n    rows = []\n    for cond in [\"ISR\", \"RANDOM\"]:\n        sub = df[df[\"condition\"] == cond]\n        row = {\"condition\": cond, \"n_seeds\": len(sub)}\n        for m in metrics:\n            vals = sub[m].values\n            row[f\"{m}_mean\"] = vals.mean()\n            row[f\"{m}_std\"] = vals.std(ddof=1) if len(vals) > 1 else 0.0\n        isr_vals = sub[\"ISR_star\"].dropna().values.astype(float)\n        row[\"ISR_star_mean\"] = isr_vals.mean() if len(isr_vals) else np.nan\n        row[\"ISR_star_std\"] = isr_vals.std(ddof=1) if len(isr_vals) > 1 else 0.0\n        rows.append(row)\n    return pd.DataFrame(rows)\n\n\n# --- Formatting ---\n\ndef fmt_pct(val: float) -> str:\n    return f\"{val*100:.1f}\\\\%\"\n\ndef fmt_or(val: float) -> str:\n    return \"$\\\\infty$\" if np.isinf(val) else f\"{val:.2f}\"\n\ndef fmt_ci(lo: float, hi: float) -> str:\n    lo_s = f\"{lo:.2f}\" if not np.isnan(lo) else \"0\"\n    hi_s = \"$\\\\infty$\" if np.isinf(hi) or np.isnan(hi) else f\"{hi:.2f}\"\n    return f\"[{lo_s}, {hi_s}]\"\n\ndef fmt_p(p: float) -> str:\n    if p < 0.001:\n        return \"$<$0.001\"\n    return f\"{p:.3f}\"\n\ndef fmt_mean_std(mean: float, std: float, pct: bool = False) -> str:\n    if pct:\n        return f\"{mean*100:.1f} $\\\\pm$ {std*100:.1f}\\\\%\"\n    return f\"{mean:.1f} $\\\\pm$ {std:.1f}\"\n\ndef fmt_bca(bca: dict, pct: bool = False) -> str:\n    m = bca[\"mean\"]\n    lo, hi = bca[\"ci_lo\"], bca[\"ci_hi\"]\n    if pct:\n        return f\"{m*100:.1f}\\\\% [{lo*100:.1f}, {hi*100:.1f}]\"\n    return f\"{m:.1f} [{lo:.1f}, {hi:.1f}]\"\n\n\n# --- Console output ---\n\ndef print_per_seed_table(df: pd.DataFrame):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  PER-SEED RESULTS\")\n    print(\"=\" * 90)\n    cols = [\"condition\", \"seed\", \"PR\", \"H7_count\", \"H7_rate\", \"H1_count\",\n            \"H8_count\", \"genuine_count\", \"genuine_rate\", \"CI_count\", \"SNH_count\", \"SNH_rate\",\n            \"ISR_star\"]\n    fmt = df[cols].copy()\n    for c in [\"H7_rate\", \"genuine_rate\", \"SNH_rate\"]:\n        fmt[c] = fmt[c].apply(lambda v: f\"{v*100:.1f}%\")\n    fmt[\"ISR_star\"] = fmt[\"ISR_star\"].apply(lambda v: f\"{v:.4f}\" if pd.notna(v) else \"---\")\n    print(fmt.to_string(index=False))\n\n\ndef print_condition_stats(cond_df: pd.DataFrame):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  CONDITION-LEVEL STATISTICS (mean +/- SD)\")\n    print(\"=\" * 90)\n    for _, row in cond_df.iterrows():\n        n = int(row['n_seeds'])\n        print(f\"\\n  {row['condition']} (n={n} seeds):\")\n        print(f\"    PR:           {row['PR_mean']:.1f} +/- {row['PR_std']:.1f}\")\n        print(f\"    H7 rate:      {row['H7_rate_mean']*100:.1f} +/- {row['H7_rate_std']*100:.1f}%\")\n        print(f\"    Genuine rate: {row['genuine_rate_mean']*100:.1f} +/- {row['genuine_rate_std']*100:.1f}%\")\n        print(f\"    S-NH rate:    {row['SNH_rate_mean']*100:.1f} +/- {row['SNH_rate_std']*100:.1f}%\")\n        if not np.isnan(row.get('ISR_star_mean', np.nan)):\n            print(f\"    ISR*:         {row['ISR_star_mean']:.4f} +/- {row['ISR_star_std']:.4f}\")\n\n\ndef print_tests(fisher, perm, mw, bf, bca_h7, bca_gen, mw_isr_star=None):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  STATISTICAL TESTS\")\n    print(\"=\" * 90)\n\n    print(\"\\n  1. H7 Domination Fisher Exact Test (H7-dominated = H7% >= 50%)\")\n    print(f\"     ISR:    {fisher['ISR']['h7_dom']} dominated / {fisher['ISR']['n']} seeds\")\n    print(f\"     RANDOM: {fisher['RANDOM']['h7_dom']} dominated / {fisher['RANDOM']['n']} seeds\")\n    print(f\"     Contingency: {fisher['table']}\")\n    or_str = \"inf\" if np.isinf(fisher['odds_ratio']) else f\"{fisher['odds_ratio']:.4f}\"\n    print(f\"     OR = {or_str}, 95% CI = [{fisher['or_ci_lo']:.4f}, {fisher['or_ci_hi']:.4f}]\"\n          if not np.isnan(fisher['or_ci_lo']) else f\"     OR = {or_str}, 95% CI = N/A\")\n    print(f\"     p-value (one-sided, greater): {fisher['p_value']:.4f}\")\n\n    print(f\"\\n  2. Genuine Rate Permutation Test (n_perm={perm['n_perm']})\")\n    print(f\"     ISR mean:    {perm['isr_mean']*100:.2f}%\")\n    print(f\"     RANDOM mean: {perm['random_mean']*100:.2f}%\")\n    print(f\"     Diff: {perm['observed_diff']*100:.2f} pp, p = {perm['p_value']:.4f}\")\n\n    print(f\"\\n  3. H7 Rate Mann-Whitney U Test\")\n    print(f\"     ISR median:    {mw['isr_median']*100:.1f}%\")\n    print(f\"     RANDOM median: {mw['random_median']*100:.1f}%\")\n    print(f\"     U = {mw['U']:.1f}, p = {mw['p_value']:.4f}\")\n    print(f\"     Rank-biserial r = {mw['r_rank_biserial']:.4f}\")\n\n    print(f\"\\n  4. Bayes Factor (H7 Domination, Beta-Binomial)\")\n    print(f\"     ISR:    {bf['k_isr']}/{bf['n_isr']} dominated\")\n    print(f\"     RANDOM: {bf['k_rand']}/{bf['n_rand']} dominated\")\n    print(f\"     BF10 = {bf['bf10']:.4f} ({bf['interpretation']})\")\n\n    print(f\"\\n  5. BCa Bootstrap 95% CI (n_boot resamples)\")\n    for label, bca in [(\"H7 rate\", bca_h7), (\"Genuine rate\", bca_gen)]:\n        print(f\"     {label}:\")\n        for cond in [\"ISR\", \"RANDOM\"]:\n            b = bca[cond]\n            print(f\"       {cond}: {b['mean']*100:.1f}% [{b['ci_lo']*100:.1f}, {b['ci_hi']*100:.1f}]\"\n                  if not np.isnan(b['ci_lo']) else f\"       {cond}: {b['mean']*100:.1f}% [N/A]\")\n\n    if mw_isr_star:\n        print(f\"\\n  6. ISR* (Proved-Only Mean ISR) Mann-Whitney U Test\")\n        print(f\"     ISR mean:    {mw_isr_star['isr_mean']:.4f}, median: {mw_isr_star['isr_median']:.4f}\")\n        print(f\"     RANDOM mean: {mw_isr_star['random_mean']:.4f}, median: {mw_isr_star['random_median']:.4f}\")\n        print(f\"     U = {mw_isr_star['U']:.1f}, p = {mw_isr_star['p_value']:.4f}\")\n        print(f\"     Rank-biserial r = {mw_isr_star['r_rank_biserial']:.4f}\")\n\n\n# --- Markdown generation (appendix-ready) ---\n\ndef generate_markdown(df: pd.DataFrame, cond_df: pd.DataFrame,\n                      fisher: dict, perm: dict, mw: dict,\n                      bf: dict, bca_h7: dict, bca_gen: dict) -> str:\n    L = []\n    L.append(\"## D134: ISR vs Random Statistical Analysis\\n\")\n\n    # Per-seed table\n    L.append(\"### Table A1: Per-Seed Hacking Taxonomy (4B Qwen3, 500 steps)\\n\")\n    L.append(\"| Condition | Seed | PR | H7 | H7\\\\% | H1 | H8 | Genuine | Gen\\\\% | CI | S-NH | S-NH\\\\% |\")\n    L.append(\"|:----------|-----:|---:|---:|-----:|---:|---:|--------:|------:|---:|-----:|-------:|\")\n    for _, r in df.iterrows():\n        L.append(\n            f\"| {r['condition']} | {r['seed']} | {int(r['PR'])} | {int(r['H7_count'])} | \"\n            f\"{r['H7_rate']*100:.1f} | {int(r['H1_count'])} | {int(r['H8_count'])} | \"\n            f\"{int(r['genuine_count'])} | {r['genuine_rate']*100:.1f} | {int(r['CI_count'])} | \"\n            f\"{int(r['SNH_count'])} | {r['SNH_rate']*100:.1f} |\"\n        )\n\n    # Condition summary with BCa CI\n    L.append(\"\\n### Table A2: Condition-Level Summary\\n\")\n    L.append(\"| Condition | $n$ | PR (mean$\\\\pm$SD) | H7\\\\% (mean$\\\\pm$SD) | H7\\\\% BCa 95\\\\% CI | Gen\\\\% (mean$\\\\pm$SD) | Gen\\\\% BCa 95\\\\% CI |\")\n    L.append(\"|:----------|----:|:------------------|:-------------------|:-----------------|:-------------------|:-----------------|\")\n    for _, r in cond_df.iterrows():\n        cond = r[\"condition\"]\n        h7_bca = bca_h7.get(cond, {})\n        gen_bca = bca_gen.get(cond, {})\n        h7_ci = f\"[{h7_bca['ci_lo']*100:.1f}, {h7_bca['ci_hi']*100:.1f}]\" if h7_bca and not np.isnan(h7_bca.get('ci_lo', np.nan)) else \"N/A\"\n        gen_ci = f\"[{gen_bca['ci_lo']*100:.1f}, {gen_bca['ci_hi']*100:.1f}]\" if gen_bca and not np.isnan(gen_bca.get('ci_lo', np.nan)) else \"N/A\"\n        L.append(\n            f\"| {cond} | {int(r['n_seeds'])} | \"\n            f\"{r['PR_mean']:.1f}$\\\\pm${r['PR_std']:.1f} | \"\n            f\"{r['H7_rate_mean']*100:.1f}$\\\\pm${r['H7_rate_std']*100:.1f} | \"\n            f\"{h7_ci} | \"\n            f\"{r['genuine_rate_mean']*100:.1f}$\\\\pm${r['genuine_rate_std']*100:.1f} | \"\n            f\"{gen_ci} |\"\n        )\n\n    # Statistical tests\n    if fisher and perm and mw and bf:\n        L.append(\"\\n### Statistical Tests\\n\")\n\n        # Fisher\n        or_str = \"$\\\\infty$\" if np.isinf(fisher['odds_ratio']) else f\"{fisher['odds_ratio']:.2f}\"\n        ci_lo = f\"{fisher['or_ci_lo']:.2f}\" if not np.isnan(fisher['or_ci_lo']) else \"0\"\n        ci_hi = \"$\\\\infty$\" if np.isinf(fisher.get('or_ci_hi', np.inf)) or np.isnan(fisher.get('or_ci_hi', np.nan)) else f\"{fisher['or_ci_hi']:.2f}\"\n        L.append(\"**1. H7 Domination Fisher Exact Test** (threshold: H7$\\\\geq$50\\\\% of proved)\")\n        L.append(f\"- ISR: {fisher['ISR']['h7_dom']}/{fisher['ISR']['n']} seeds H7-dominated; \"\n                 f\"Random: {fisher['RANDOM']['h7_dom']}/{fisher['RANDOM']['n']}\")\n        L.append(f\"- OR = {or_str}, 95\\\\% exact CI = [{ci_lo}, {ci_hi}], \"\n                 f\"$p$ = {fmt_p(fisher['p_value'])}\")\n        L.append(\"\")\n\n        # Permutation\n        L.append(f\"**2. Genuine Rate Permutation Test** ($n$ = {perm['n_perm']:,} permutations)\")\n        L.append(f\"- ISR mean: {perm['isr_mean']*100:.2f}\\\\%, Random mean: {perm['random_mean']*100:.2f}\\\\%\")\n        L.append(f\"- $\\\\Delta$ = {perm['observed_diff']*100:.2f} pp, $p$ = {fmt_p(perm['p_value'])}\")\n        L.append(\"\")\n\n        # Mann-Whitney\n        L.append(\"**3. H7 Rate Mann-Whitney $U$ Test**\")\n        L.append(f\"- ISR median: {mw['isr_median']*100:.1f}\\\\%, Random median: {mw['random_median']*100:.1f}\\\\%\")\n        L.append(f\"- $U$ = {mw['U']:.1f}, $p$ = {fmt_p(mw['p_value'])}, \"\n                 f\"rank-biserial $r$ = {mw['r_rank_biserial']:.3f}\")\n        L.append(\"\")\n\n        # Bayes Factor\n        L.append(\"**4. Bayes Factor** (Beta-Binomial conjugate, prior: Beta(1,1))\")\n        L.append(f\"- $BF_{{10}}$ = {bf['bf10']:.2f} ({bf['interpretation']})\")\n        L.append(f\"- ISR: {bf['k_isr']}/{bf['n_isr']} H7-dominated, \"\n                 f\"Random: {bf['k_rand']}/{bf['n_rand']}\")\n\n    return \"\\n\".join(L) + \"\\n\"\n\n\n# --- Main ---\n\ndef main():\n    args = parse_args()\n    data_dir = Path(args.data_dir)\n\n    if not data_dir.exists():\n        print(f\"ERROR: data directory {data_dir} does not exist\", file=sys.stderr)\n        sys.exit(1)\n\n    if args.prefix:\n        prefixes = [args.prefix]\n    elif args.prefixes:\n        prefixes = [p.strip() for p in args.prefixes.split(\",\")]\n    else:\n        prefixes = MODE_PREFIXES[args.mode]\n    print(f\"Mode: {args.mode} | Prefixes: {prefixes}\")\n\n    runs = discover_runs(data_dir, prefixes)\n    if not runs:\n        print(f\"ERROR: no runs found in {data_dir} with prefixes {prefixes}\", file=sys.stderr)\n        sys.exit(1)\n\n    isr_count = sum(1 for r in runs if r[\"condition\"] == \"ISR\")\n    rand_count = sum(1 for r in runs if r[\"condition\"] == \"RANDOM\")\n    print(f\"Found {len(runs)} runs: {isr_count} ISR, {rand_count} RANDOM\")\n    for r in runs:\n        print(f\"  {r['condition']:6s} s{r['seed']} <- {r['dir_name']}\")\n\n    df = build_table(runs)\n    print_per_seed_table(df)\n\n    cond_df = condition_stats(df)\n    print_condition_stats(cond_df)\n\n    if isr_count < 2 or rand_count < 2:\n        print(\"\\nWARNING: need >= 2 seeds per condition for statistical tests, skipping.\",\n              file=sys.stderr)\n        bca_h7 = bca_bootstrap_ci(df, \"H7_rate\", args.n_boot, args.seed)\n        bca_gen = bca_bootstrap_ci(df, \"genuine_rate\", args.n_boot, args.seed)\n        if args.output:\n            md = generate_markdown(df, cond_df, {}, {}, {}, {}, bca_h7, bca_gen)\n            Path(args.output).write_text(md)\n            print(f\"\\nMarkdown written to {args.output}\")\n        return\n\n    fisher = fisher_h7_domination(df)\n    perm = permutation_test_genuine(df, n_perm=args.n_perm, rng_seed=args.seed)\n    mw = mannwhitney_h7(df)\n    bf = bayes_factor_h7_domination(df)\n    bca_h7 = bca_bootstrap_ci(df, \"H7_rate\", args.n_boot, args.seed)\n    bca_gen = bca_bootstrap_ci(df, \"genuine_rate\", args.n_boot, args.seed)\n\n    print_tests(fisher, perm, mw, bf, bca_h7, bca_gen)\n\n    md = generate_markdown(df, cond_df, fisher, perm, mw, bf, bca_h7, bca_gen)\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  MARKDOWN OUTPUT (appendix-ready)\")\n    print(\"=\" * 90)\n    print(md)\n\n    if args.output:\n        Path(args.output).parent.mkdir(parents=True, exist_ok=True)\n        Path(args.output).write_text(md)\n        print(f\"Markdown written to {args.output}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 486,
        "oldLines": 7,
        "newStart": 486,
        "newLines": 8,
        "lines": [
          " ",
          " def generate_markdown(df: pd.DataFrame, cond_df: pd.DataFrame,",
          "                       fisher: dict, perm: dict, mw: dict,",
          "-                      bf: dict, bca_h7: dict, bca_gen: dict) -> str:",
          "+                      bf: dict, bca_h7: dict, bca_gen: dict,",
          "+                      mw_isr_star: dict = None) -> str:",
          "     L = []",
          "     L.append(\"## D134: ISR vs Random Statistical Analysis\\n\")",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 45_

Now update Table A1 header and rows to include ISR*.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "75cf9c99-8511-44b7-8301-59c3ffe84faf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y5C9GMbnWxuvtzUgJps41M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 364,
      "cache_read_input_tokens": 50168,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 364
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

_source line 46_

<details open><summary>🔧 Tool call — Edit · `toolu_01Mn9Web4GEcRW3UA9pswV9z`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/scripts/d134_analysis.py",
  "old_string": "    L.append(\"### Table A1: Per-Seed Hacking Taxonomy (4B Qwen3, 500 steps)\\n\")\n    L.append(\"| Condition | Seed | PR | H7 | H7\\\\% | H1 | H8 | Genuine | Gen\\\\% | CI | S-NH | S-NH\\\\% |\")\n    L.append(\"|:----------|-----:|---:|---:|-----:|---:|---:|--------:|------:|---:|-----:|-------:|\")\n    for _, r in df.iterrows():\n        L.append(\n            f\"| {r['condition']} | {r['seed']} | {int(r['PR'])} | {int(r['H7_count'])} | \"\n            f\"{r['H7_rate']*100:.1f} | {int(r['H1_count'])} | {int(r['H8_count'])} | \"\n            f\"{int(r['genuine_count'])} | {r['genuine_rate']*100:.1f} | {int(r['CI_count'])} | \"\n            f\"{int(r['SNH_count'])} | {r['SNH_rate']*100:.1f} |\"\n        )",
  "new_string": "    L.append(\"### Table A1: Per-Seed Hacking Taxonomy (4B Qwen3, 500 steps)\\n\")\n    L.append(\"| Condition | Seed | PR | H7 | H7\\\\% | H1 | H8 | Genuine | Gen\\\\% | CI | S-NH | S-NH\\\\% | ISR* |\")\n    L.append(\"|:----------|-----:|---:|---:|-----:|---:|---:|--------:|------:|---:|-----:|-------:|-----:|\")\n    for _, r in df.iterrows():\n        isr_star_str = f\"{r['ISR_star']:.4f}\" if pd.notna(r.get('ISR_star')) else \"---\"\n        L.append(\n            f\"| {r['condition']} | {r['seed']} | {int(r['PR'])} | {int(r['H7_count'])} | \"\n            f\"{r['H7_rate']*100:.1f} | {int(r['H1_count'])} | {int(r['H8_count'])} | \"\n            f\"{int(r['genuine_count'])} | {r['genuine_rate']*100:.1f} | {int(r['CI_count'])} | \"\n            f\"{int(r['SNH_count'])} | {r['SNH_rate']*100:.1f} | {isr_star_str} |\"\n        )"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "0715356f-d1c7-4300-a9a5-fea6ccf7f2a3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y5C9GMbnWxuvtzUgJps41M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 364,
      "cache_read_input_tokens": 50168,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 364
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

_source line 47 · 2026-05-18T23:33:14.205Z_

<details><summary>↩ Tool result · `toolu_01Mn9Web4GEcRW3UA9pswV9z`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/scripts/d134_analysis.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "72a5071f-342c-438c-ae17-75ee5fdc49d9",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/scripts/d134_analysis.py",
    "oldString": "    L.append(\"### Table A1: Per-Seed Hacking Taxonomy (4B Qwen3, 500 steps)\\n\")\n    L.append(\"| Condition | Seed | PR | H7 | H7\\\\% | H1 | H8 | Genuine | Gen\\\\% | CI | S-NH | S-NH\\\\% |\")\n    L.append(\"|:----------|-----:|---:|---:|-----:|---:|---:|--------:|------:|---:|-----:|-------:|\")\n    for _, r in df.iterrows():\n        L.append(\n            f\"| {r['condition']} | {r['seed']} | {int(r['PR'])} | {int(r['H7_count'])} | \"\n            f\"{r['H7_rate']*100:.1f} | {int(r['H1_count'])} | {int(r['H8_count'])} | \"\n            f\"{int(r['genuine_count'])} | {r['genuine_rate']*100:.1f} | {int(r['CI_count'])} | \"\n            f\"{int(r['SNH_count'])} | {r['SNH_rate']*100:.1f} |\"\n        )",
    "newString": "    L.append(\"### Table A1: Per-Seed Hacking Taxonomy (4B Qwen3, 500 steps)\\n\")\n    L.append(\"| Condition | Seed | PR | H7 | H7\\\\% | H1 | H8 | Genuine | Gen\\\\% | CI | S-NH | S-NH\\\\% | ISR* |\")\n    L.append(\"|:----------|-----:|---:|---:|-----:|---:|---:|--------:|------:|---:|-----:|-------:|-----:|\")\n    for _, r in df.iterrows():\n        isr_star_str = f\"{r['ISR_star']:.4f}\" if pd.notna(r.get('ISR_star')) else \"---\"\n        L.append(\n            f\"| {r['condition']} | {r['seed']} | {int(r['PR'])} | {int(r['H7_count'])} | \"\n            f\"{r['H7_rate']*100:.1f} | {int(r['H1_count'])} | {int(r['H8_count'])} | \"\n            f\"{int(r['genuine_count'])} | {r['genuine_rate']*100:.1f} | {int(r['CI_count'])} | \"\n            f\"{int(r['SNH_count'])} | {r['SNH_rate']*100:.1f} | {isr_star_str} |\"\n        )",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"D134 experiment analysis: multi-seed ISR vs Random, 4B GRPO training.\nReads taxonomy data from classify.json, taxonomy.json, or top-level taxonomy files.\nComputes summary stats, statistical tests (Fisher, Mann-Whitney, permutation, Bayes Factor),\nand BCa bootstrap CIs. Outputs appendix-ready markdown.\n\"\"\"\n\nimport argparse\nimport json\nimport re\nimport sys\nfrom pathlib import Path\n\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\nfrom scipy.special import betaln\n\nCONDITION_MAP = [\n    (\"d134_4b_isr\", \"ISR\"),\n    (\"d134_4b_random\", \"RANDOM\"),\n    (\"plan002_additive\", \"ISR\"),\n    (\"plan018_additive_random\", \"RANDOM\"),\n    (\"plan018_random\", \"RANDOM\"),\n]\n\nMODE_PREFIXES = {\n    \"d134_only\": [\"d134_4b\"],\n    \"all\": [\"d134_4b\", \"plan002_additive_b01\", \"plan018_additive_random_b01\", \"plan018_random\"],\n}\n\n\ndef parse_args():\n    p = argparse.ArgumentParser(description=\"D134 multi-seed analysis and statistical tests\")\n    p.add_argument(\"--data_dir\", type=str, default=\"/root/autodl-tmp/outputs\",\n                   help=\"Directory containing experiment outputs\")\n    p.add_argument(\"--mode\", type=str, default=\"d134_only\", choices=list(MODE_PREFIXES),\n                   help=\"d134_only = matched 5+5 design (default); all = include original seeds\")\n    p.add_argument(\"--prefix\", type=str, default=None,\n                   help=\"(Legacy) Single prefix filter; overrides mode/prefixes\")\n    p.add_argument(\"--prefixes\", type=str, default=None,\n                   help=\"Comma-separated prefixes; overrides --mode\")\n    p.add_argument(\"--output\", type=str, default=None,\n                   help=\"Write markdown summary to this file\")\n    p.add_argument(\"--n_perm\", type=int, default=10000,\n                   help=\"Number of permutations for permutation test\")\n    p.add_argument(\"--n_boot\", type=int, default=10000,\n                   help=\"Number of bootstrap resamples for BCa CI\")\n    p.add_argument(\"--seed\", type=int, default=42,\n                   help=\"Random seed for permutation/bootstrap\")\n    return p.parse_args()\n\n\n# --- Data loading ---\n\ndef match_condition(name: str) -> str | None:\n    best_prefix = \"\"\n    best_cond = None\n    for prefix, cond in CONDITION_MAP:\n        if name.startswith(prefix) and len(prefix) > len(best_prefix):\n            best_prefix = prefix\n            best_cond = cond\n    return best_cond\n\n\ndef extract_seed(name: str) -> int | None:\n    m = re.search(r'_s(\\d+)', name)\n    return int(m.group(1)) if m else None\n\n\ndef load_eval_results(path: Path) -> dict | None:\n    if not path.exists():\n        return None\n    with open(path) as f:\n        data = json.load(f)\n    if \"eval_results\" in data:\n        return data[\"eval_results\"]\n    return data\n\n\ndef load_taxonomy_unified(path: Path) -> dict | None:\n    with open(path) as f:\n        raw = json.load(f)\n    t = raw.get(\"taxonomy\", {})\n    proved = t.get(\"proved\", 0)\n    if proved == 0:\n        return None\n    h7 = t.get(\"H7\", 0)\n    h1 = t.get(\"H1_exact\", 0)\n    h8 = t.get(\"H8\", 0)\n    genuine = t.get(\"genuine\", 0)\n    return {\n        \"n_total\": 100, \"n_proved\": proved,\n        \"h7_total_count\": h7, \"h7_total_rate\": h7 / proved,\n        \"h1_strict_count\": h1, \"h8_conjunction_collapse_count\": h8,\n        \"genuine_count\": genuine, \"genuine_rate\": genuine / proved,\n        \"content_independent_count\": 0,\n    }\n\n\ndef load_taxonomy_verification(path: Path) -> dict | None:\n    with open(path) as f:\n        raw = json.load(f)\n    proved = raw.get(\"proved\", 0)\n    if proved == 0:\n        return None\n    tax = raw.get(\"taxonomy\", {})\n    h7 = tax.get(\"h7\", {}).get(\"count\", 0)\n    h1 = tax.get(\"h1_exact\", {}).get(\"count\", 0)\n    h8 = tax.get(\"h8\", {}).get(\"count\", 0)\n    genuine = tax.get(\"genuine\", {}).get(\"count\", 0)\n    return {\n        \"n_total\": raw.get(\"total\", 100), \"n_proved\": proved,\n        \"h7_total_count\": h7, \"h7_total_rate\": h7 / proved,\n        \"h1_strict_count\": h1, \"h8_conjunction_collapse_count\": h8,\n        \"genuine_count\": genuine, \"genuine_rate\": genuine / proved,\n        \"content_independent_count\": 0,\n    }\n\n\ndef discover_runs(data_dir: Path, prefixes: list[str]) -> list[dict]:\n    runs = []\n    seen = set()\n    for entry in sorted(data_dir.iterdir()):\n        name = entry.name\n        if not any(name.startswith(p) for p in prefixes):\n            continue\n        cond = match_condition(name)\n        seed_val = extract_seed(name)\n        if cond is None or seed_val is None:\n            continue\n        key = (cond, seed_val)\n        if key in seen:\n            continue\n        data = None\n        if entry.is_dir():\n            for fname in [\"classify.json\", \"taxonomy.json\"]:\n                data = load_eval_results(entry / fname)\n                if data is not None:\n                    break\n            if data is None:\n                continue\n        elif entry.is_file():\n            if name.endswith(\"_taxonomy_unified.json\"):\n                data = load_taxonomy_unified(entry)\n            elif name.endswith(\"_taxonomy_verification.json\"):\n                data = load_taxonomy_verification(entry)\n            if data is None:\n                continue\n        else:\n            continue\n        seen.add(key)\n        isr_star = None\n        if entry.is_dir():\n            eval_path = entry / \"eval_results.json\"\n            if eval_path.exists():\n                with open(eval_path) as ef:\n                    eval_raw = json.load(ef)\n                isr_star = eval_raw.get(\"summary\", {}).get(\"proved_only_mean_isr\")\n        runs.append({\"dir_name\": name, \"seed\": seed_val, \"condition\": cond,\n                      \"data\": data, \"isr_star\": isr_star})\n    return runs\n\n\ndef compute_row(run: dict) -> dict:\n    d = run[\"data\"]\n    n_proved = d.get(\"n_proved\", 0)\n    n_total = d.get(\"n_total\", 100)\n    h7 = d.get(\"h7_total_count\", 0)\n    h7_rate = d.get(\"h7_total_rate\", h7 / n_proved if n_proved > 0 else 0.0)\n    h1 = d.get(\"h1_strict_count\", 0)\n    h8 = d.get(\"h8_conjunction_collapse_count\", 0)\n    genuine = d.get(\"genuine_count\", 0)\n    genuine_rate = d.get(\"genuine_rate\", genuine / n_proved if n_proved > 0 else 0.0)\n    ci = d.get(\"content_independent_count\", 0)\n    snh = max(genuine - ci, 0)\n    snh_rate = snh / n_proved if n_proved > 0 else 0.0\n    return {\n        \"seed\": run[\"seed\"], \"condition\": run[\"condition\"], \"n_total\": n_total,\n        \"PR\": n_proved, \"H7_count\": h7, \"H7_rate\": h7_rate,\n        \"H1_count\": h1, \"H8_count\": h8,\n        \"genuine_count\": genuine, \"genuine_rate\": genuine_rate,\n        \"CI_count\": ci, \"SNH_count\": snh, \"SNH_rate\": snh_rate,\n        \"ISR_star\": run.get(\"isr_star\"),\n    }\n\n\ndef build_table(runs: list[dict]) -> pd.DataFrame:\n    rows = [compute_row(r) for r in runs]\n    df = pd.DataFrame(rows)\n    df = df.sort_values([\"condition\", \"seed\"]).reset_index(drop=True)\n    return df\n\n\n# --- Statistical tests ---\n\ndef fisher_h7_domination(df: pd.DataFrame) -> dict:\n    results = {}\n    for cond in [\"ISR\", \"RANDOM\"]:\n        sub = df[df[\"condition\"] == cond]\n        results[cond] = {\n            \"n\": len(sub),\n            \"h7_dom\": int((sub[\"H7_rate\"] >= 0.5).sum()),\n            \"not_h7_dom\": int((sub[\"H7_rate\"] < 0.5).sum()),\n        }\n    table = np.array([\n        [results[\"ISR\"][\"h7_dom\"], results[\"ISR\"][\"not_h7_dom\"]],\n        [results[\"RANDOM\"][\"h7_dom\"], results[\"RANDOM\"][\"not_h7_dom\"]],\n    ])\n    odds_ratio, p_value = stats.fisher_exact(table, alternative=\"greater\")\n\n    # 95% exact CI via scipy.stats.contingency\n    or_ci_lo, or_ci_hi = np.nan, np.nan\n    try:\n        ct = stats.contingency.odds_ratio(table)\n        ci = ct.confidence_interval(confidence_level=0.95)\n        or_ci_lo, or_ci_hi = ci.low, ci.high\n    except Exception:\n        pass\n\n    return {\n        \"table\": table.tolist(),\n        \"ISR\": results[\"ISR\"],\n        \"RANDOM\": results[\"RANDOM\"],\n        \"odds_ratio\": odds_ratio,\n        \"or_ci_lo\": or_ci_lo,\n        \"or_ci_hi\": or_ci_hi,\n        \"p_value\": p_value,\n    }\n\n\ndef permutation_test_genuine(df: pd.DataFrame, n_perm: int = 10000,\n                              rng_seed: int = 42) -> dict:\n    isr = df[df[\"condition\"] == \"ISR\"][\"genuine_rate\"].values\n    rand = df[df[\"condition\"] == \"RANDOM\"][\"genuine_rate\"].values\n    observed = isr.mean() - rand.mean()\n    pooled = np.concatenate([isr, rand])\n    n_isr = len(isr)\n    rng = np.random.default_rng(rng_seed)\n    count = 0\n    for _ in range(n_perm):\n        perm = rng.permutation(pooled)\n        if perm[:n_isr].mean() - perm[n_isr:].mean() >= observed:\n            count += 1\n    return {\n        \"observed_diff\": float(observed),\n        \"p_value\": count / n_perm,\n        \"n_perm\": n_perm,\n        \"isr_mean\": float(isr.mean()),\n        \"random_mean\": float(rand.mean()),\n    }\n\n\ndef mannwhitney_h7(df: pd.DataFrame) -> dict:\n    isr = df[df[\"condition\"] == \"ISR\"][\"H7_rate\"].values\n    rand = df[df[\"condition\"] == \"RANDOM\"][\"H7_rate\"].values\n    n1, n2 = len(isr), len(rand)\n    u_stat, p_value = stats.mannwhitneyu(isr, rand, alternative=\"greater\")\n    r_rb = 2.0 * u_stat / (n1 * n2) - 1.0 if n1 * n2 > 0 else np.nan\n    return {\n        \"U\": float(u_stat),\n        \"p_value\": float(p_value),\n        \"r_rank_biserial\": float(r_rb),\n        \"isr_median\": float(np.median(isr)),\n        \"random_median\": float(np.median(rand)),\n    }\n\n\ndef mannwhitney_isr_star(df: pd.DataFrame) -> dict | None:\n    isr = df[df[\"condition\"] == \"ISR\"][\"ISR_star\"].dropna().values.astype(float)\n    rand = df[df[\"condition\"] == \"RANDOM\"][\"ISR_star\"].dropna().values.astype(float)\n    if len(isr) < 2 or len(rand) < 2:\n        return None\n    n1, n2 = len(isr), len(rand)\n    u_stat, p_value = stats.mannwhitneyu(isr, rand, alternative=\"greater\")\n    r_rb = 2.0 * u_stat / (n1 * n2) - 1.0\n    return {\n        \"U\": float(u_stat),\n        \"p_value\": float(p_value),\n        \"r_rank_biserial\": float(r_rb),\n        \"isr_median\": float(np.median(isr)),\n        \"random_median\": float(np.median(rand)),\n        \"isr_mean\": float(np.mean(isr)),\n        \"random_mean\": float(np.mean(rand)),\n    }\n\n\ndef bca_bootstrap_ci(df: pd.DataFrame, metric: str, n_boot: int = 10000,\n                      rng_seed: int = 42) -> dict:\n    \"\"\"BCa 95% CI for per-condition means of a metric.\"\"\"\n    result = {}\n    for cond in [\"ISR\", \"RANDOM\"]:\n        vals = df[df[\"condition\"] == cond][metric].values\n        if len(vals) < 2:\n            result[cond] = {\"mean\": float(vals.mean()) if len(vals) else np.nan,\n                            \"ci_lo\": np.nan, \"ci_hi\": np.nan}\n            continue\n        res = stats.bootstrap(\n            (vals,), np.mean, n_resamples=n_boot,\n            confidence_level=0.95, method=\"BCa\",\n            random_state=np.random.default_rng(rng_seed),\n        )\n        result[cond] = {\n            \"mean\": float(vals.mean()),\n            \"ci_lo\": float(res.confidence_interval.low),\n            \"ci_hi\": float(res.confidence_interval.high),\n        }\n    return result\n\n\ndef bayes_factor_h7_domination(df: pd.DataFrame) -> dict:\n    \"\"\"BF10 for H7-domination rate difference (beta-binomial conjugate).\n    H0: ISR and Random share same domination rate.\n    H1: independent rates. Prior: Beta(1,1) on each.\n    \"\"\"\n    isr_sub = df[df[\"condition\"] == \"ISR\"]\n    rand_sub = df[df[\"condition\"] == \"RANDOM\"]\n    k_isr = int((isr_sub[\"H7_rate\"] >= 0.5).sum())\n    n_isr = len(isr_sub)\n    k_rand = int((rand_sub[\"H7_rate\"] >= 0.5).sum())\n    n_rand = len(rand_sub)\n    k_total = k_isr + k_rand\n    n_total = n_isr + n_rand\n\n    # log marginal under H0 (shared rate)\n    log_m_h0 = betaln(1 + k_total, 1 + n_total - k_total) - betaln(1, 1)\n    # log marginal under H1 (independent rates)\n    log_m_h1 = (betaln(1 + k_isr, 1 + n_isr - k_isr) - betaln(1, 1)\n                + betaln(1 + k_rand, 1 + n_rand - k_rand) - betaln(1, 1))\n    log_bf10 = log_m_h1 - log_m_h0\n    bf10 = float(np.exp(log_bf10))\n\n    return {\n        \"k_isr\": k_isr, \"n_isr\": n_isr,\n        \"k_rand\": k_rand, \"n_rand\": n_rand,\n        \"bf10\": bf10,\n        \"log_bf10\": float(log_bf10),\n        \"interpretation\": _interpret_bf(bf10),\n    }\n\n\ndef _interpret_bf(bf: float) -> str:\n    if bf > 100:\n        return \"extreme evidence for H1\"\n    if bf > 30:\n        return \"very strong evidence for H1\"\n    if bf > 10:\n        return \"strong evidence for H1\"\n    if bf > 3:\n        return \"moderate evidence for H1\"\n    if bf > 1:\n        return \"anecdotal evidence for H1\"\n    if bf > 1/3:\n        return \"anecdotal evidence (inconclusive)\"\n    if bf > 1/10:\n        return \"moderate evidence for H0\"\n    return \"strong evidence for H0\"\n\n\ndef condition_stats(df: pd.DataFrame) -> pd.DataFrame:\n    metrics = [\"PR\", \"H7_rate\", \"genuine_rate\", \"SNH_rate\"]\n    rows = []\n    for cond in [\"ISR\", \"RANDOM\"]:\n        sub = df[df[\"condition\"] == cond]\n        row = {\"condition\": cond, \"n_seeds\": len(sub)}\n        for m in metrics:\n            vals = sub[m].values\n            row[f\"{m}_mean\"] = vals.mean()\n            row[f\"{m}_std\"] = vals.std(ddof=1) if len(vals) > 1 else 0.0\n        isr_vals = sub[\"ISR_star\"].dropna().values.astype(float)\n        row[\"ISR_star_mean\"] = isr_vals.mean() if len(isr_vals) else np.nan\n        row[\"ISR_star_std\"] = isr_vals.std(ddof=1) if len(isr_vals) > 1 else 0.0\n        rows.append(row)\n    return pd.DataFrame(rows)\n\n\n# --- Formatting ---\n\ndef fmt_pct(val: float) -> str:\n    return f\"{val*100:.1f}\\\\%\"\n\ndef fmt_or(val: float) -> str:\n    return \"$\\\\infty$\" if np.isinf(val) else f\"{val:.2f}\"\n\ndef fmt_ci(lo: float, hi: float) -> str:\n    lo_s = f\"{lo:.2f}\" if not np.isnan(lo) else \"0\"\n    hi_s = \"$\\\\infty$\" if np.isinf(hi) or np.isnan(hi) else f\"{hi:.2f}\"\n    return f\"[{lo_s}, {hi_s}]\"\n\ndef fmt_p(p: float) -> str:\n    if p < 0.001:\n        return \"$<$0.001\"\n    return f\"{p:.3f}\"\n\ndef fmt_mean_std(mean: float, std: float, pct: bool = False) -> str:\n    if pct:\n        return f\"{mean*100:.1f} $\\\\pm$ {std*100:.1f}\\\\%\"\n    return f\"{mean:.1f} $\\\\pm$ {std:.1f}\"\n\ndef fmt_bca(bca: dict, pct: bool = False) -> str:\n    m = bca[\"mean\"]\n    lo, hi = bca[\"ci_lo\"], bca[\"ci_hi\"]\n    if pct:\n        return f\"{m*100:.1f}\\\\% [{lo*100:.1f}, {hi*100:.1f}]\"\n    return f\"{m:.1f} [{lo:.1f}, {hi:.1f}]\"\n\n\n# --- Console output ---\n\ndef print_per_seed_table(df: pd.DataFrame):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  PER-SEED RESULTS\")\n    print(\"=\" * 90)\n    cols = [\"condition\", \"seed\", \"PR\", \"H7_count\", \"H7_rate\", \"H1_count\",\n            \"H8_count\", \"genuine_count\", \"genuine_rate\", \"CI_count\", \"SNH_count\", \"SNH_rate\",\n            \"ISR_star\"]\n    fmt = df[cols].copy()\n    for c in [\"H7_rate\", \"genuine_rate\", \"SNH_rate\"]:\n        fmt[c] = fmt[c].apply(lambda v: f\"{v*100:.1f}%\")\n    fmt[\"ISR_star\"] = fmt[\"ISR_star\"].apply(lambda v: f\"{v:.4f}\" if pd.notna(v) else \"---\")\n    print(fmt.to_string(index=False))\n\n\ndef print_condition_stats(cond_df: pd.DataFrame):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  CONDITION-LEVEL STATISTICS (mean +/- SD)\")\n    print(\"=\" * 90)\n    for _, row in cond_df.iterrows():\n        n = int(row['n_seeds'])\n        print(f\"\\n  {row['condition']} (n={n} seeds):\")\n        print(f\"    PR:           {row['PR_mean']:.1f} +/- {row['PR_std']:.1f}\")\n        print(f\"    H7 rate:      {row['H7_rate_mean']*100:.1f} +/- {row['H7_rate_std']*100:.1f}%\")\n        print(f\"    Genuine rate: {row['genuine_rate_mean']*100:.1f} +/- {row['genuine_rate_std']*100:.1f}%\")\n        print(f\"    S-NH rate:    {row['SNH_rate_mean']*100:.1f} +/- {row['SNH_rate_std']*100:.1f}%\")\n        if not np.isnan(row.get('ISR_star_mean', np.nan)):\n            print(f\"    ISR*:         {row['ISR_star_mean']:.4f} +/- {row['ISR_star_std']:.4f}\")\n\n\ndef print_tests(fisher, perm, mw, bf, bca_h7, bca_gen, mw_isr_star=None):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  STATISTICAL TESTS\")\n    print(\"=\" * 90)\n\n    print(\"\\n  1. H7 Domination Fisher Exact Test (H7-dominated = H7% >= 50%)\")\n    print(f\"     ISR:    {fisher['ISR']['h7_dom']} dominated / {fisher['ISR']['n']} seeds\")\n    print(f\"     RANDOM: {fisher['RANDOM']['h7_dom']} dominated / {fisher['RANDOM']['n']} seeds\")\n    print(f\"     Contingency: {fisher['table']}\")\n    or_str = \"inf\" if np.isinf(fisher['odds_ratio']) else f\"{fisher['odds_ratio']:.4f}\"\n    print(f\"     OR = {or_str}, 95% CI = [{fisher['or_ci_lo']:.4f}, {fisher['or_ci_hi']:.4f}]\"\n          if not np.isnan(fisher['or_ci_lo']) else f\"     OR = {or_str}, 95% CI = N/A\")\n    print(f\"     p-value (one-sided, greater): {fisher['p_value']:.4f}\")\n\n    print(f\"\\n  2. Genuine Rate Permutation Test (n_perm={perm['n_perm']})\")\n    print(f\"     ISR mean:    {perm['isr_mean']*100:.2f}%\")\n    print(f\"     RANDOM mean: {perm['random_mean']*100:.2f}%\")\n    print(f\"     Diff: {perm['observed_diff']*100:.2f} pp, p = {perm['p_value']:.4f}\")\n\n    print(f\"\\n  3. H7 Rate Mann-Whitney U Test\")\n    print(f\"     ISR median:    {mw['isr_median']*100:.1f}%\")\n    print(f\"     RANDOM median: {mw['random_median']*100:.1f}%\")\n    print(f\"     U = {mw['U']:.1f}, p = {mw['p_value']:.4f}\")\n    print(f\"     Rank-biserial r = {mw['r_rank_biserial']:.4f}\")\n\n    print(f\"\\n  4. Bayes Factor (H7 Domination, Beta-Binomial)\")\n    print(f\"     ISR:    {bf['k_isr']}/{bf['n_isr']} dominated\")\n    print(f\"     RANDOM: {bf['k_rand']}/{bf['n_rand']} dominated\")\n    print(f\"     BF10 = {bf['bf10']:.4f} ({bf['interpretation']})\")\n\n    print(f\"\\n  5. BCa Bootstrap 95% CI (n_boot resamples)\")\n    for label, bca in [(\"H7 rate\", bca_h7), (\"Genuine rate\", bca_gen)]:\n        print(f\"     {label}:\")\n        for cond in [\"ISR\", \"RANDOM\"]:\n            b = bca[cond]\n            print(f\"       {cond}: {b['mean']*100:.1f}% [{b['ci_lo']*100:.1f}, {b['ci_hi']*100:.1f}]\"\n                  if not np.isnan(b['ci_lo']) else f\"       {cond}: {b['mean']*100:.1f}% [N/A]\")\n\n    if mw_isr_star:\n        print(f\"\\n  6. ISR* (Proved-Only Mean ISR) Mann-Whitney U Test\")\n        print(f\"     ISR mean:    {mw_isr_star['isr_mean']:.4f}, median: {mw_isr_star['isr_median']:.4f}\")\n        print(f\"     RANDOM mean: {mw_isr_star['random_mean']:.4f}, median: {mw_isr_star['random_median']:.4f}\")\n        print(f\"     U = {mw_isr_star['U']:.1f}, p = {mw_isr_star['p_value']:.4f}\")\n        print(f\"     Rank-biserial r = {mw_isr_star['r_rank_biserial']:.4f}\")\n\n\n# --- Markdown generation (appendix-ready) ---\n\ndef generate_markdown(df: pd.DataFrame, cond_df: pd.DataFrame,\n                      fisher: dict, perm: dict, mw: dict,\n                      bf: dict, bca_h7: dict, bca_gen: dict,\n                      mw_isr_star: dict = None) -> str:\n    L = []\n    L.append(\"## D134: ISR vs Random Statistical Analysis\\n\")\n\n    # Per-seed table\n    L.append(\"### Table A1: Per-Seed Hacking Taxonomy (4B Qwen3, 500 steps)\\n\")\n    L.append(\"| Condition | Seed | PR | H7 | H7\\\\% | H1 | H8 | Genuine | Gen\\\\% | CI | S-NH | S-NH\\\\% |\")\n    L.append(\"|:----------|-----:|---:|---:|-----:|---:|---:|--------:|------:|---:|-----:|-------:|\")\n    for _, r in df.iterrows():\n        L.append(\n            f\"| {r['condition']} | {r['seed']} | {int(r['PR'])} | {int(r['H7_count'])} | \"\n            f\"{r['H7_rate']*100:.1f} | {int(r['H1_count'])} | {int(r['H8_count'])} | \"\n            f\"{int(r['genuine_count'])} | {r['genuine_rate']*100:.1f} | {int(r['CI_count'])} | \"\n            f\"{int(r['SNH_count'])} | {r['SNH_rate']*100:.1f} |\"\n        )\n\n    # Condition summary with BCa CI\n    L.append(\"\\n### Table A2: Condition-Level Summary\\n\")\n    L.append(\"| Condition | $n$ | PR (mean$\\\\pm$SD) | H7\\\\% (mean$\\\\pm$SD) | H7\\\\% BCa 95\\\\% CI | Gen\\\\% (mean$\\\\pm$SD) | Gen\\\\% BCa 95\\\\% CI |\")\n    L.append(\"|:----------|----:|:------------------|:-------------------|:-----------------|:-------------------|:-----------------|\")\n    for _, r in cond_df.iterrows():\n        cond = r[\"condition\"]\n        h7_bca = bca_h7.get(cond, {})\n        gen_bca = bca_gen.get(cond, {})\n        h7_ci = f\"[{h7_bca['ci_lo']*100:.1f}, {h7_bca['ci_hi']*100:.1f}]\" if h7_bca and not np.isnan(h7_bca.get('ci_lo', np.nan)) else \"N/A\"\n        gen_ci = f\"[{gen_bca['ci_lo']*100:.1f}, {gen_bca['ci_hi']*100:.1f}]\" if gen_bca and not np.isnan(gen_bca.get('ci_lo', np.nan)) else \"N/A\"\n        L.append(\n            f\"| {cond} | {int(r['n_seeds'])} | \"\n            f\"{r['PR_mean']:.1f}$\\\\pm${r['PR_std']:.1f} | \"\n            f\"{r['H7_rate_mean']*100:.1f}$\\\\pm${r['H7_rate_std']*100:.1f} | \"\n            f\"{h7_ci} | \"\n            f\"{r['genuine_rate_mean']*100:.1f}$\\\\pm${r['genuine_rate_std']*100:.1f} | \"\n            f\"{gen_ci} |\"\n        )\n\n    # Statistical tests\n    if fisher and perm and mw and bf:\n        L.append(\"\\n### Statistical Tests\\n\")\n\n        # Fisher\n        or_str = \"$\\\\infty$\" if np.isinf(fisher['odds_ratio']) else f\"{fisher['odds_ratio']:.2f}\"\n        ci_lo = f\"{fisher['or_ci_lo']:.2f}\" if not np.isnan(fisher['or_ci_lo']) else \"0\"\n        ci_hi = \"$\\\\infty$\" if np.isinf(fisher.get('or_ci_hi', np.inf)) or np.isnan(fisher.get('or_ci_hi', np.nan)) else f\"{fisher['or_ci_hi']:.2f}\"\n        L.append(\"**1. H7 Domination Fisher Exact Test** (threshold: H7$\\\\geq$50\\\\% of proved)\")\n        L.append(f\"- ISR: {fisher['ISR']['h7_dom']}/{fisher['ISR']['n']} seeds H7-dominated; \"\n                 f\"Random: {fisher['RANDOM']['h7_dom']}/{fisher['RANDOM']['n']}\")\n        L.append(f\"- OR = {or_str}, 95\\\\% exact CI = [{ci_lo}, {ci_hi}], \"\n                 f\"$p$ = {fmt_p(fisher['p_value'])}\")\n        L.append(\"\")\n\n        # Permutation\n        L.append(f\"**2. Genuine Rate Permutation Test** ($n$ = {perm['n_perm']:,} permutations)\")\n        L.append(f\"- ISR mean: {perm['isr_mean']*100:.2f}\\\\%, Random mean: {perm['random_mean']*100:.2f}\\\\%\")\n        L.append(f\"- $\\\\Delta$ = {perm['observed_diff']*100:.2f} pp, $p$ = {fmt_p(perm['p_value'])}\")\n        L.append(\"\")\n\n        # Mann-Whitney\n        L.append(\"**3. H7 Rate Mann-Whitney $U$ Test**\")\n        L.append(f\"- ISR median: {mw['isr_median']*100:.1f}\\\\%, Random median: {mw['random_median']*100:.1f}\\\\%\")\n        L.append(f\"- $U$ = {mw['U']:.1f}, $p$ = {fmt_p(mw['p_value'])}, \"\n                 f\"rank-biserial $r$ = {mw['r_rank_biserial']:.3f}\")\n        L.append(\"\")\n\n        # Bayes Factor\n        L.append(\"**4. Bayes Factor** (Beta-Binomial conjugate, prior: Beta(1,1))\")\n        L.append(f\"- $BF_{{10}}$ = {bf['bf10']:.2f} ({bf['interpretation']})\")\n        L.append(f\"- ISR: {bf['k_isr']}/{bf['n_isr']} H7-dominated, \"\n                 f\"Random: {bf['k_rand']}/{bf['n_rand']}\")\n\n    return \"\\n\".join(L) + \"\\n\"\n\n\n# --- Main ---\n\ndef main():\n    args = parse_args()\n    data_dir = Path(args.data_dir)\n\n    if not data_dir.exists():\n        print(f\"ERROR: data directory {data_dir} does not exist\", file=sys.stderr)\n        sys.exit(1)\n\n    if args.prefix:\n        prefixes = [args.prefix]\n    elif args.prefixes:\n        prefixes = [p.strip() for p in args.prefixes.split(\",\")]\n    else:\n        prefixes = MODE_PREFIXES[args.mode]\n    print(f\"Mode: {args.mode} | Prefixes: {prefixes}\")\n\n    runs = discover_runs(data_dir, prefixes)\n    if not runs:\n        print(f\"ERROR: no runs found in {data_dir} with prefixes {prefixes}\", file=sys.stderr)\n        sys.exit(1)\n\n    isr_count = sum(1 for r in runs if r[\"condition\"] == \"ISR\")\n    rand_count = sum(1 for r in runs if r[\"condition\"] == \"RANDOM\")\n    print(f\"Found {len(runs)} runs: {isr_count} ISR, {rand_count} RANDOM\")\n    for r in runs:\n        print(f\"  {r['condition']:6s} s{r['seed']} <- {r['dir_name']}\")\n\n    df = build_table(runs)\n    print_per_seed_table(df)\n\n    cond_df = condition_stats(df)\n    print_condition_stats(cond_df)\n\n    if isr_count < 2 or rand_count < 2:\n        print(\"\\nWARNING: need >= 2 seeds per condition for statistical tests, skipping.\",\n              file=sys.stderr)\n        bca_h7 = bca_bootstrap_ci(df, \"H7_rate\", args.n_boot, args.seed)\n        bca_gen = bca_bootstrap_ci(df, \"genuine_rate\", args.n_boot, args.seed)\n        if args.output:\n            md = generate_markdown(df, cond_df, {}, {}, {}, {}, bca_h7, bca_gen)\n            Path(args.output).write_text(md)\n            print(f\"\\nMarkdown written to {args.output}\")\n        return\n\n    fisher = fisher_h7_domination(df)\n    perm = permutation_test_genuine(df, n_perm=args.n_perm, rng_seed=args.seed)\n    mw = mannwhitney_h7(df)\n    bf = bayes_factor_h7_domination(df)\n    bca_h7 = bca_bootstrap_ci(df, \"H7_rate\", args.n_boot, args.seed)\n    bca_gen = bca_bootstrap_ci(df, \"genuine_rate\", args.n_boot, args.seed)\n\n    print_tests(fisher, perm, mw, bf, bca_h7, bca_gen)\n\n    md = generate_markdown(df, cond_df, fisher, perm, mw, bf, bca_h7, bca_gen)\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  MARKDOWN OUTPUT (appendix-ready)\")\n    print(\"=\" * 90)\n    print(md)\n\n    if args.output:\n        Path(args.output).parent.mkdir(parents=True, exist_ok=True)\n        Path(args.output).write_text(md)\n        print(f\"Markdown written to {args.output}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 493,
        "oldLines": 14,
        "newStart": 493,
        "newLines": 15,
        "lines": [
          " ",
          "     # Per-seed table",
          "     L.append(\"### Table A1: Per-Seed Hacking Taxonomy (4B Qwen3, 500 steps)\\n\")",
          "-    L.append(\"| Condition | Seed | PR | H7 | H7\\\\% | H1 | H8 | Genuine | Gen\\\\% | CI | S-NH | S-NH\\\\% |\")",
          "-    L.append(\"|:----------|-----:|---:|---:|-----:|---:|---:|--------:|------:|---:|-----:|-------:|\")",
          "+    L.append(\"| Condition | Seed | PR | H7 | H7\\\\% | H1 | H8 | Genuine | Gen\\\\% | CI | S-NH | S-NH\\\\% | ISR* |\")",
          "+    L.append(\"|:----------|-----:|---:|---:|-----:|---:|---:|--------:|------:|---:|-----:|-------:|-----:|\")",
          "     for _, r in df.iterrows():",
          "+        isr_star_str = f\"{r['ISR_star']:.4f}\" if pd.notna(r.get('ISR_star')) else \"---\"",
          "         L.append(",
          "             f\"| {r['condition']} | {r['seed']} | {int(r['PR'])} | {int(r['H7_count'])} | \"",
          "             f\"{r['H7_rate']*100:.1f} | {int(r['H1_count'])} | {int(r['H8_count'])} | \"",
          "             f\"{int(r['genuine_count'])} | {r['genuine_rate']*100:.1f} | {int(r['CI_count'])} | \"",
          "-            f\"{int(r['SNH_count'])} | {r['SNH_rate']*100:.1f} |\"",
          "+            f\"{int(r['SNH_count'])} | {r['SNH_rate']*100:.1f} | {isr_star_str} |\"",
          "         )",
          " ",
          "     # Condition summary with BCa CI"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 48_

Now add ISR* MW test to the markdown statistical tests section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "62682abe-a623-407d-af7b-c8b4514095ba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gf4Uk8nnWekdwtD336ricL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 858,
      "cache_read_input_tokens": 50532,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 858
      },
      "output_tokens": 6,
      "service_tier": "standard",
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

_source line 49_

<details open><summary>🔧 Tool call — Edit · `toolu_01EnFwXufRthaB5GmK99UZ6d`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/scripts/d134_analysis.py",
  "old_string": "        L.append(f\"- ISR: {bf['k_isr']}/{bf['n_isr']} H7-dominated, \"\n                 f\"Random: {bf['k_rand']}/{bf['n_rand']}\")\n\n    return \"\\n\".join(L) + \"\\n\"",
  "new_string": "        L.append(f\"- ISR: {bf['k_isr']}/{bf['n_isr']} H7-dominated, \"\n                 f\"Random: {bf['k_rand']}/{bf['n_rand']}\")\n\n        if mw_isr_star:\n            L.append(\"\")\n            L.append(\"**5. ISR* (Proved-Only Mean ISR) Mann-Whitney $U$ Test**\")\n            L.append(f\"- ISR mean: {mw_isr_star['isr_mean']:.4f}, median: {mw_isr_star['isr_median']:.4f}\")\n            L.append(f\"- Random mean: {mw_isr_star['random_mean']:.4f}, median: {mw_isr_star['random_median']:.4f}\")\n            L.append(f\"- $U$ = {mw_isr_star['U']:.1f}, $p$ = {fmt_p(mw_isr_star['p_value'])}, \"\n                     f\"rank-biserial $r$ = {mw_isr_star['r_rank_biserial']:.3f}\")\n\n    return \"\\n\".join(L) + \"\\n\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "ea9d4bd7-b856-495c-bc4b-7becebb7cd23",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gf4Uk8nnWekdwtD336ricL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 858,
      "cache_read_input_tokens": 50532,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 858
      },
      "output_tokens": 6,
      "service_tier": "standard",
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

_source line 50 · 2026-05-18T23:33:21.510Z_

<details><summary>↩ Tool result · `toolu_01EnFwXufRthaB5GmK99UZ6d`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/scripts/d134_analysis.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "3180766b-afac-4cbb-9fe7-09aa1c1abf52",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/scripts/d134_analysis.py",
    "oldString": "        L.append(f\"- ISR: {bf['k_isr']}/{bf['n_isr']} H7-dominated, \"\n                 f\"Random: {bf['k_rand']}/{bf['n_rand']}\")\n\n    return \"\\n\".join(L) + \"\\n\"",
    "newString": "        L.append(f\"- ISR: {bf['k_isr']}/{bf['n_isr']} H7-dominated, \"\n                 f\"Random: {bf['k_rand']}/{bf['n_rand']}\")\n\n        if mw_isr_star:\n            L.append(\"\")\n            L.append(\"**5. ISR* (Proved-Only Mean ISR) Mann-Whitney $U$ Test**\")\n            L.append(f\"- ISR mean: {mw_isr_star['isr_mean']:.4f}, median: {mw_isr_star['isr_median']:.4f}\")\n            L.append(f\"- Random mean: {mw_isr_star['random_mean']:.4f}, median: {mw_isr_star['random_median']:.4f}\")\n            L.append(f\"- $U$ = {mw_isr_star['U']:.1f}, $p$ = {fmt_p(mw_isr_star['p_value'])}, \"\n                     f\"rank-biserial $r$ = {mw_isr_star['r_rank_biserial']:.3f}\")\n\n    return \"\\n\".join(L) + \"\\n\"",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"D134 experiment analysis: multi-seed ISR vs Random, 4B GRPO training.\nReads taxonomy data from classify.json, taxonomy.json, or top-level taxonomy files.\nComputes summary stats, statistical tests (Fisher, Mann-Whitney, permutation, Bayes Factor),\nand BCa bootstrap CIs. Outputs appendix-ready markdown.\n\"\"\"\n\nimport argparse\nimport json\nimport re\nimport sys\nfrom pathlib import Path\n\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\nfrom scipy.special import betaln\n\nCONDITION_MAP = [\n    (\"d134_4b_isr\", \"ISR\"),\n    (\"d134_4b_random\", \"RANDOM\"),\n    (\"plan002_additive\", \"ISR\"),\n    (\"plan018_additive_random\", \"RANDOM\"),\n    (\"plan018_random\", \"RANDOM\"),\n]\n\nMODE_PREFIXES = {\n    \"d134_only\": [\"d134_4b\"],\n    \"all\": [\"d134_4b\", \"plan002_additive_b01\", \"plan018_additive_random_b01\", \"plan018_random\"],\n}\n\n\ndef parse_args():\n    p = argparse.ArgumentParser(description=\"D134 multi-seed analysis and statistical tests\")\n    p.add_argument(\"--data_dir\", type=str, default=\"/root/autodl-tmp/outputs\",\n                   help=\"Directory containing experiment outputs\")\n    p.add_argument(\"--mode\", type=str, default=\"d134_only\", choices=list(MODE_PREFIXES),\n                   help=\"d134_only = matched 5+5 design (default); all = include original seeds\")\n    p.add_argument(\"--prefix\", type=str, default=None,\n                   help=\"(Legacy) Single prefix filter; overrides mode/prefixes\")\n    p.add_argument(\"--prefixes\", type=str, default=None,\n                   help=\"Comma-separated prefixes; overrides --mode\")\n    p.add_argument(\"--output\", type=str, default=None,\n                   help=\"Write markdown summary to this file\")\n    p.add_argument(\"--n_perm\", type=int, default=10000,\n                   help=\"Number of permutations for permutation test\")\n    p.add_argument(\"--n_boot\", type=int, default=10000,\n                   help=\"Number of bootstrap resamples for BCa CI\")\n    p.add_argument(\"--seed\", type=int, default=42,\n                   help=\"Random seed for permutation/bootstrap\")\n    return p.parse_args()\n\n\n# --- Data loading ---\n\ndef match_condition(name: str) -> str | None:\n    best_prefix = \"\"\n    best_cond = None\n    for prefix, cond in CONDITION_MAP:\n        if name.startswith(prefix) and len(prefix) > len(best_prefix):\n            best_prefix = prefix\n            best_cond = cond\n    return best_cond\n\n\ndef extract_seed(name: str) -> int | None:\n    m = re.search(r'_s(\\d+)', name)\n    return int(m.group(1)) if m else None\n\n\ndef load_eval_results(path: Path) -> dict | None:\n    if not path.exists():\n        return None\n    with open(path) as f:\n        data = json.load(f)\n    if \"eval_results\" in data:\n        return data[\"eval_results\"]\n    return data\n\n\ndef load_taxonomy_unified(path: Path) -> dict | None:\n    with open(path) as f:\n        raw = json.load(f)\n    t = raw.get(\"taxonomy\", {})\n    proved = t.get(\"proved\", 0)\n    if proved == 0:\n        return None\n    h7 = t.get(\"H7\", 0)\n    h1 = t.get(\"H1_exact\", 0)\n    h8 = t.get(\"H8\", 0)\n    genuine = t.get(\"genuine\", 0)\n    return {\n        \"n_total\": 100, \"n_proved\": proved,\n        \"h7_total_count\": h7, \"h7_total_rate\": h7 / proved,\n        \"h1_strict_count\": h1, \"h8_conjunction_collapse_count\": h8,\n        \"genuine_count\": genuine, \"genuine_rate\": genuine / proved,\n        \"content_independent_count\": 0,\n    }\n\n\ndef load_taxonomy_verification(path: Path) -> dict | None:\n    with open(path) as f:\n        raw = json.load(f)\n    proved = raw.get(\"proved\", 0)\n    if proved == 0:\n        return None\n    tax = raw.get(\"taxonomy\", {})\n    h7 = tax.get(\"h7\", {}).get(\"count\", 0)\n    h1 = tax.get(\"h1_exact\", {}).get(\"count\", 0)\n    h8 = tax.get(\"h8\", {}).get(\"count\", 0)\n    genuine = tax.get(\"genuine\", {}).get(\"count\", 0)\n    return {\n        \"n_total\": raw.get(\"total\", 100), \"n_proved\": proved,\n        \"h7_total_count\": h7, \"h7_total_rate\": h7 / proved,\n        \"h1_strict_count\": h1, \"h8_conjunction_collapse_count\": h8,\n        \"genuine_count\": genuine, \"genuine_rate\": genuine / proved,\n        \"content_independent_count\": 0,\n    }\n\n\ndef discover_runs(data_dir: Path, prefixes: list[str]) -> list[dict]:\n    runs = []\n    seen = set()\n    for entry in sorted(data_dir.iterdir()):\n        name = entry.name\n        if not any(name.startswith(p) for p in prefixes):\n            continue\n        cond = match_condition(name)\n        seed_val = extract_seed(name)\n        if cond is None or seed_val is None:\n            continue\n        key = (cond, seed_val)\n        if key in seen:\n            continue\n        data = None\n        if entry.is_dir():\n            for fname in [\"classify.json\", \"taxonomy.json\"]:\n                data = load_eval_results(entry / fname)\n                if data is not None:\n                    break\n            if data is None:\n                continue\n        elif entry.is_file():\n            if name.endswith(\"_taxonomy_unified.json\"):\n                data = load_taxonomy_unified(entry)\n            elif name.endswith(\"_taxonomy_verification.json\"):\n                data = load_taxonomy_verification(entry)\n            if data is None:\n                continue\n        else:\n            continue\n        seen.add(key)\n        isr_star = None\n        if entry.is_dir():\n            eval_path = entry / \"eval_results.json\"\n            if eval_path.exists():\n                with open(eval_path) as ef:\n                    eval_raw = json.load(ef)\n                isr_star = eval_raw.get(\"summary\", {}).get(\"proved_only_mean_isr\")\n        runs.append({\"dir_name\": name, \"seed\": seed_val, \"condition\": cond,\n                      \"data\": data, \"isr_star\": isr_star})\n    return runs\n\n\ndef compute_row(run: dict) -> dict:\n    d = run[\"data\"]\n    n_proved = d.get(\"n_proved\", 0)\n    n_total = d.get(\"n_total\", 100)\n    h7 = d.get(\"h7_total_count\", 0)\n    h7_rate = d.get(\"h7_total_rate\", h7 / n_proved if n_proved > 0 else 0.0)\n    h1 = d.get(\"h1_strict_count\", 0)\n    h8 = d.get(\"h8_conjunction_collapse_count\", 0)\n    genuine = d.get(\"genuine_count\", 0)\n    genuine_rate = d.get(\"genuine_rate\", genuine / n_proved if n_proved > 0 else 0.0)\n    ci = d.get(\"content_independent_count\", 0)\n    snh = max(genuine - ci, 0)\n    snh_rate = snh / n_proved if n_proved > 0 else 0.0\n    return {\n        \"seed\": run[\"seed\"], \"condition\": run[\"condition\"], \"n_total\": n_total,\n        \"PR\": n_proved, \"H7_count\": h7, \"H7_rate\": h7_rate,\n        \"H1_count\": h1, \"H8_count\": h8,\n        \"genuine_count\": genuine, \"genuine_rate\": genuine_rate,\n        \"CI_count\": ci, \"SNH_count\": snh, \"SNH_rate\": snh_rate,\n        \"ISR_star\": run.get(\"isr_star\"),\n    }\n\n\ndef build_table(runs: list[dict]) -> pd.DataFrame:\n    rows = [compute_row(r) for r in runs]\n    df = pd.DataFrame(rows)\n    df = df.sort_values([\"condition\", \"seed\"]).reset_index(drop=True)\n    return df\n\n\n# --- Statistical tests ---\n\ndef fisher_h7_domination(df: pd.DataFrame) -> dict:\n    results = {}\n    for cond in [\"ISR\", \"RANDOM\"]:\n        sub = df[df[\"condition\"] == cond]\n        results[cond] = {\n            \"n\": len(sub),\n            \"h7_dom\": int((sub[\"H7_rate\"] >= 0.5).sum()),\n            \"not_h7_dom\": int((sub[\"H7_rate\"] < 0.5).sum()),\n        }\n    table = np.array([\n        [results[\"ISR\"][\"h7_dom\"], results[\"ISR\"][\"not_h7_dom\"]],\n        [results[\"RANDOM\"][\"h7_dom\"], results[\"RANDOM\"][\"not_h7_dom\"]],\n    ])\n    odds_ratio, p_value = stats.fisher_exact(table, alternative=\"greater\")\n\n    # 95% exact CI via scipy.stats.contingency\n    or_ci_lo, or_ci_hi = np.nan, np.nan\n    try:\n        ct = stats.contingency.odds_ratio(table)\n        ci = ct.confidence_interval(confidence_level=0.95)\n        or_ci_lo, or_ci_hi = ci.low, ci.high\n    except Exception:\n        pass\n\n    return {\n        \"table\": table.tolist(),\n        \"ISR\": results[\"ISR\"],\n        \"RANDOM\": results[\"RANDOM\"],\n        \"odds_ratio\": odds_ratio,\n        \"or_ci_lo\": or_ci_lo,\n        \"or_ci_hi\": or_ci_hi,\n        \"p_value\": p_value,\n    }\n\n\ndef permutation_test_genuine(df: pd.DataFrame, n_perm: int = 10000,\n                              rng_seed: int = 42) -> dict:\n    isr = df[df[\"condition\"] == \"ISR\"][\"genuine_rate\"].values\n    rand = df[df[\"condition\"] == \"RANDOM\"][\"genuine_rate\"].values\n    observed = isr.mean() - rand.mean()\n    pooled = np.concatenate([isr, rand])\n    n_isr = len(isr)\n    rng = np.random.default_rng(rng_seed)\n    count = 0\n    for _ in range(n_perm):\n        perm = rng.permutation(pooled)\n        if perm[:n_isr].mean() - perm[n_isr:].mean() >= observed:\n            count += 1\n    return {\n        \"observed_diff\": float(observed),\n        \"p_value\": count / n_perm,\n        \"n_perm\": n_perm,\n        \"isr_mean\": float(isr.mean()),\n        \"random_mean\": float(rand.mean()),\n    }\n\n\ndef mannwhitney_h7(df: pd.DataFrame) -> dict:\n    isr = df[df[\"condition\"] == \"ISR\"][\"H7_rate\"].values\n    rand = df[df[\"condition\"] == \"RANDOM\"][\"H7_rate\"].values\n    n1, n2 = len(isr), len(rand)\n    u_stat, p_value = stats.mannwhitneyu(isr, rand, alternative=\"greater\")\n    r_rb = 2.0 * u_stat / (n1 * n2) - 1.0 if n1 * n2 > 0 else np.nan\n    return {\n        \"U\": float(u_stat),\n        \"p_value\": float(p_value),\n        \"r_rank_biserial\": float(r_rb),\n        \"isr_median\": float(np.median(isr)),\n        \"random_median\": float(np.median(rand)),\n    }\n\n\ndef mannwhitney_isr_star(df: pd.DataFrame) -> dict | None:\n    isr = df[df[\"condition\"] == \"ISR\"][\"ISR_star\"].dropna().values.astype(float)\n    rand = df[df[\"condition\"] == \"RANDOM\"][\"ISR_star\"].dropna().values.astype(float)\n    if len(isr) < 2 or len(rand) < 2:\n        return None\n    n1, n2 = len(isr), len(rand)\n    u_stat, p_value = stats.mannwhitneyu(isr, rand, alternative=\"greater\")\n    r_rb = 2.0 * u_stat / (n1 * n2) - 1.0\n    return {\n        \"U\": float(u_stat),\n        \"p_value\": float(p_value),\n        \"r_rank_biserial\": float(r_rb),\n        \"isr_median\": float(np.median(isr)),\n        \"random_median\": float(np.median(rand)),\n        \"isr_mean\": float(np.mean(isr)),\n        \"random_mean\": float(np.mean(rand)),\n    }\n\n\ndef bca_bootstrap_ci(df: pd.DataFrame, metric: str, n_boot: int = 10000,\n                      rng_seed: int = 42) -> dict:\n    \"\"\"BCa 95% CI for per-condition means of a metric.\"\"\"\n    result = {}\n    for cond in [\"ISR\", \"RANDOM\"]:\n        vals = df[df[\"condition\"] == cond][metric].values\n        if len(vals) < 2:\n            result[cond] = {\"mean\": float(vals.mean()) if len(vals) else np.nan,\n                            \"ci_lo\": np.nan, \"ci_hi\": np.nan}\n            continue\n        res = stats.bootstrap(\n            (vals,), np.mean, n_resamples=n_boot,\n            confidence_level=0.95, method=\"BCa\",\n            random_state=np.random.default_rng(rng_seed),\n        )\n        result[cond] = {\n            \"mean\": float(vals.mean()),\n            \"ci_lo\": float(res.confidence_interval.low),\n            \"ci_hi\": float(res.confidence_interval.high),\n        }\n    return result\n\n\ndef bayes_factor_h7_domination(df: pd.DataFrame) -> dict:\n    \"\"\"BF10 for H7-domination rate difference (beta-binomial conjugate).\n    H0: ISR and Random share same domination rate.\n    H1: independent rates. Prior: Beta(1,1) on each.\n    \"\"\"\n    isr_sub = df[df[\"condition\"] == \"ISR\"]\n    rand_sub = df[df[\"condition\"] == \"RANDOM\"]\n    k_isr = int((isr_sub[\"H7_rate\"] >= 0.5).sum())\n    n_isr = len(isr_sub)\n    k_rand = int((rand_sub[\"H7_rate\"] >= 0.5).sum())\n    n_rand = len(rand_sub)\n    k_total = k_isr + k_rand\n    n_total = n_isr + n_rand\n\n    # log marginal under H0 (shared rate)\n    log_m_h0 = betaln(1 + k_total, 1 + n_total - k_total) - betaln(1, 1)\n    # log marginal under H1 (independent rates)\n    log_m_h1 = (betaln(1 + k_isr, 1 + n_isr - k_isr) - betaln(1, 1)\n                + betaln(1 + k_rand, 1 + n_rand - k_rand) - betaln(1, 1))\n    log_bf10 = log_m_h1 - log_m_h0\n    bf10 = float(np.exp(log_bf10))\n\n    return {\n        \"k_isr\": k_isr, \"n_isr\": n_isr,\n        \"k_rand\": k_rand, \"n_rand\": n_rand,\n        \"bf10\": bf10,\n        \"log_bf10\": float(log_bf10),\n        \"interpretation\": _interpret_bf(bf10),\n    }\n\n\ndef _interpret_bf(bf: float) -> str:\n    if bf > 100:\n        return \"extreme evidence for H1\"\n    if bf > 30:\n        return \"very strong evidence for H1\"\n    if bf > 10:\n        return \"strong evidence for H1\"\n    if bf > 3:\n        return \"moderate evidence for H1\"\n    if bf > 1:\n        return \"anecdotal evidence for H1\"\n    if bf > 1/3:\n        return \"anecdotal evidence (inconclusive)\"\n    if bf > 1/10:\n        return \"moderate evidence for H0\"\n    return \"strong evidence for H0\"\n\n\ndef condition_stats(df: pd.DataFrame) -> pd.DataFrame:\n    metrics = [\"PR\", \"H7_rate\", \"genuine_rate\", \"SNH_rate\"]\n    rows = []\n    for cond in [\"ISR\", \"RANDOM\"]:\n        sub = df[df[\"condition\"] == cond]\n        row = {\"condition\": cond, \"n_seeds\": len(sub)}\n        for m in metrics:\n            vals = sub[m].values\n            row[f\"{m}_mean\"] = vals.mean()\n            row[f\"{m}_std\"] = vals.std(ddof=1) if len(vals) > 1 else 0.0\n        isr_vals = sub[\"ISR_star\"].dropna().values.astype(float)\n        row[\"ISR_star_mean\"] = isr_vals.mean() if len(isr_vals) else np.nan\n        row[\"ISR_star_std\"] = isr_vals.std(ddof=1) if len(isr_vals) > 1 else 0.0\n        rows.append(row)\n    return pd.DataFrame(rows)\n\n\n# --- Formatting ---\n\ndef fmt_pct(val: float) -> str:\n    return f\"{val*100:.1f}\\\\%\"\n\ndef fmt_or(val: float) -> str:\n    return \"$\\\\infty$\" if np.isinf(val) else f\"{val:.2f}\"\n\ndef fmt_ci(lo: float, hi: float) -> str:\n    lo_s = f\"{lo:.2f}\" if not np.isnan(lo) else \"0\"\n    hi_s = \"$\\\\infty$\" if np.isinf(hi) or np.isnan(hi) else f\"{hi:.2f}\"\n    return f\"[{lo_s}, {hi_s}]\"\n\ndef fmt_p(p: float) -> str:\n    if p < 0.001:\n        return \"$<$0.001\"\n    return f\"{p:.3f}\"\n\ndef fmt_mean_std(mean: float, std: float, pct: bool = False) -> str:\n    if pct:\n        return f\"{mean*100:.1f} $\\\\pm$ {std*100:.1f}\\\\%\"\n    return f\"{mean:.1f} $\\\\pm$ {std:.1f}\"\n\ndef fmt_bca(bca: dict, pct: bool = False) -> str:\n    m = bca[\"mean\"]\n    lo, hi = bca[\"ci_lo\"], bca[\"ci_hi\"]\n    if pct:\n        return f\"{m*100:.1f}\\\\% [{lo*100:.1f}, {hi*100:.1f}]\"\n    return f\"{m:.1f} [{lo:.1f}, {hi:.1f}]\"\n\n\n# --- Console output ---\n\ndef print_per_seed_table(df: pd.DataFrame):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  PER-SEED RESULTS\")\n    print(\"=\" * 90)\n    cols = [\"condition\", \"seed\", \"PR\", \"H7_count\", \"H7_rate\", \"H1_count\",\n            \"H8_count\", \"genuine_count\", \"genuine_rate\", \"CI_count\", \"SNH_count\", \"SNH_rate\",\n            \"ISR_star\"]\n    fmt = df[cols].copy()\n    for c in [\"H7_rate\", \"genuine_rate\", \"SNH_rate\"]:\n        fmt[c] = fmt[c].apply(lambda v: f\"{v*100:.1f}%\")\n    fmt[\"ISR_star\"] = fmt[\"ISR_star\"].apply(lambda v: f\"{v:.4f}\" if pd.notna(v) else \"---\")\n    print(fmt.to_string(index=False))\n\n\ndef print_condition_stats(cond_df: pd.DataFrame):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  CONDITION-LEVEL STATISTICS (mean +/- SD)\")\n    print(\"=\" * 90)\n    for _, row in cond_df.iterrows():\n        n = int(row['n_seeds'])\n        print(f\"\\n  {row['condition']} (n={n} seeds):\")\n        print(f\"    PR:           {row['PR_mean']:.1f} +/- {row['PR_std']:.1f}\")\n        print(f\"    H7 rate:      {row['H7_rate_mean']*100:.1f} +/- {row['H7_rate_std']*100:.1f}%\")\n        print(f\"    Genuine rate: {row['genuine_rate_mean']*100:.1f} +/- {row['genuine_rate_std']*100:.1f}%\")\n        print(f\"    S-NH rate:    {row['SNH_rate_mean']*100:.1f} +/- {row['SNH_rate_std']*100:.1f}%\")\n        if not np.isnan(row.get('ISR_star_mean', np.nan)):\n            print(f\"    ISR*:         {row['ISR_star_mean']:.4f} +/- {row['ISR_star_std']:.4f}\")\n\n\ndef print_tests(fisher, perm, mw, bf, bca_h7, bca_gen, mw_isr_star=None):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  STATISTICAL TESTS\")\n    print(\"=\" * 90)\n\n    print(\"\\n  1. H7 Domination Fisher Exact Test (H7-dominated = H7% >= 50%)\")\n    print(f\"     ISR:    {fisher['ISR']['h7_dom']} dominated / {fisher['ISR']['n']} seeds\")\n    print(f\"     RANDOM: {fisher['RANDOM']['h7_dom']} dominated / {fisher['RANDOM']['n']} seeds\")\n    print(f\"     Contingency: {fisher['table']}\")\n    or_str = \"inf\" if np.isinf(fisher['odds_ratio']) else f\"{fisher['odds_ratio']:.4f}\"\n    print(f\"     OR = {or_str}, 95% CI = [{fisher['or_ci_lo']:.4f}, {fisher['or_ci_hi']:.4f}]\"\n          if not np.isnan(fisher['or_ci_lo']) else f\"     OR = {or_str}, 95% CI = N/A\")\n    print(f\"     p-value (one-sided, greater): {fisher['p_value']:.4f}\")\n\n    print(f\"\\n  2. Genuine Rate Permutation Test (n_perm={perm['n_perm']})\")\n    print(f\"     ISR mean:    {perm['isr_mean']*100:.2f}%\")\n    print(f\"     RANDOM mean: {perm['random_mean']*100:.2f}%\")\n    print(f\"     Diff: {perm['observed_diff']*100:.2f} pp, p = {perm['p_value']:.4f}\")\n\n    print(f\"\\n  3. H7 Rate Mann-Whitney U Test\")\n    print(f\"     ISR median:    {mw['isr_median']*100:.1f}%\")\n    print(f\"     RANDOM median: {mw['random_median']*100:.1f}%\")\n    print(f\"     U = {mw['U']:.1f}, p = {mw['p_value']:.4f}\")\n    print(f\"     Rank-biserial r = {mw['r_rank_biserial']:.4f}\")\n\n    print(f\"\\n  4. Bayes Factor (H7 Domination, Beta-Binomial)\")\n    print(f\"     ISR:    {bf['k_isr']}/{bf['n_isr']} dominated\")\n    print(f\"     RANDOM: {bf['k_rand']}/{bf['n_rand']} dominated\")\n    print(f\"     BF10 = {bf['bf10']:.4f} ({bf['interpretation']})\")\n\n    print(f\"\\n  5. BCa Bootstrap 95% CI (n_boot resamples)\")\n    for label, bca in [(\"H7 rate\", bca_h7), (\"Genuine rate\", bca_gen)]:\n        print(f\"     {label}:\")\n        for cond in [\"ISR\", \"RANDOM\"]:\n            b = bca[cond]\n            print(f\"       {cond}: {b['mean']*100:.1f}% [{b['ci_lo']*100:.1f}, {b['ci_hi']*100:.1f}]\"\n                  if not np.isnan(b['ci_lo']) else f\"       {cond}: {b['mean']*100:.1f}% [N/A]\")\n\n    if mw_isr_star:\n        print(f\"\\n  6. ISR* (Proved-Only Mean ISR) Mann-Whitney U Test\")\n        print(f\"     ISR mean:    {mw_isr_star['isr_mean']:.4f}, median: {mw_isr_star['isr_median']:.4f}\")\n        print(f\"     RANDOM mean: {mw_isr_star['random_mean']:.4f}, median: {mw_isr_star['random_median']:.4f}\")\n        print(f\"     U = {mw_isr_star['U']:.1f}, p = {mw_isr_star['p_value']:.4f}\")\n        print(f\"     Rank-biserial r = {mw_isr_star['r_rank_biserial']:.4f}\")\n\n\n# --- Markdown generation (appendix-ready) ---\n\ndef generate_markdown(df: pd.DataFrame, cond_df: pd.DataFrame,\n                      fisher: dict, perm: dict, mw: dict,\n                      bf: dict, bca_h7: dict, bca_gen: dict,\n                      mw_isr_star: dict = None) -> str:\n    L = []\n    L.append(\"## D134: ISR vs Random Statistical Analysis\\n\")\n\n    # Per-seed table\n    L.append(\"### Table A1: Per-Seed Hacking Taxonomy (4B Qwen3, 500 steps)\\n\")\n    L.append(\"| Condition | Seed | PR | H7 | H7\\\\% | H1 | H8 | Genuine | Gen\\\\% | CI | S-NH | S-NH\\\\% | ISR* |\")\n    L.append(\"|:----------|-----:|---:|---:|-----:|---:|---:|--------:|------:|---:|-----:|-------:|-----:|\")\n    for _, r in df.iterrows():\n        isr_star_str = f\"{r['ISR_star']:.4f}\" if pd.notna(r.get('ISR_star')) else \"---\"\n        L.append(\n            f\"| {r['condition']} | {r['seed']} | {int(r['PR'])} | {int(r['H7_count'])} | \"\n            f\"{r['H7_rate']*100:.1f} | {int(r['H1_count'])} | {int(r['H8_count'])} | \"\n            f\"{int(r['genuine_count'])} | {r['genuine_rate']*100:.1f} | {int(r['CI_count'])} | \"\n            f\"{int(r['SNH_count'])} | {r['SNH_rate']*100:.1f} | {isr_star_str} |\"\n        )\n\n    # Condition summary with BCa CI\n    L.append(\"\\n### Table A2: Condition-Level Summary\\n\")\n    L.append(\"| Condition | $n$ | PR (mean$\\\\pm$SD) | H7\\\\% (mean$\\\\pm$SD) | H7\\\\% BCa 95\\\\% CI | Gen\\\\% (mean$\\\\pm$SD) | Gen\\\\% BCa 95\\\\% CI |\")\n    L.append(\"|:----------|----:|:------------------|:-------------------|:-----------------|:-------------------|:-----------------|\")\n    for _, r in cond_df.iterrows():\n        cond = r[\"condition\"]\n        h7_bca = bca_h7.get(cond, {})\n        gen_bca = bca_gen.get(cond, {})\n        h7_ci = f\"[{h7_bca['ci_lo']*100:.1f}, {h7_bca['ci_hi']*100:.1f}]\" if h7_bca and not np.isnan(h7_bca.get('ci_lo', np.nan)) else \"N/A\"\n        gen_ci = f\"[{gen_bca['ci_lo']*100:.1f}, {gen_bca['ci_hi']*100:.1f}]\" if gen_bca and not np.isnan(gen_bca.get('ci_lo', np.nan)) else \"N/A\"\n        L.append(\n            f\"| {cond} | {int(r['n_seeds'])} | \"\n            f\"{r['PR_mean']:.1f}$\\\\pm${r['PR_std']:.1f} | \"\n            f\"{r['H7_rate_mean']*100:.1f}$\\\\pm${r['H7_rate_std']*100:.1f} | \"\n            f\"{h7_ci} | \"\n            f\"{r['genuine_rate_mean']*100:.1f}$\\\\pm${r['genuine_rate_std']*100:.1f} | \"\n            f\"{gen_ci} |\"\n        )\n\n    # Statistical tests\n    if fisher and perm and mw and bf:\n        L.append(\"\\n### Statistical Tests\\n\")\n\n        # Fisher\n        or_str = \"$\\\\infty$\" if np.isinf(fisher['odds_ratio']) else f\"{fisher['odds_ratio']:.2f}\"\n        ci_lo = f\"{fisher['or_ci_lo']:.2f}\" if not np.isnan(fisher['or_ci_lo']) else \"0\"\n        ci_hi = \"$\\\\infty$\" if np.isinf(fisher.get('or_ci_hi', np.inf)) or np.isnan(fisher.get('or_ci_hi', np.nan)) else f\"{fisher['or_ci_hi']:.2f}\"\n        L.append(\"**1. H7 Domination Fisher Exact Test** (threshold: H7$\\\\geq$50\\\\% of proved)\")\n        L.append(f\"- ISR: {fisher['ISR']['h7_dom']}/{fisher['ISR']['n']} seeds H7-dominated; \"\n                 f\"Random: {fisher['RANDOM']['h7_dom']}/{fisher['RANDOM']['n']}\")\n        L.append(f\"- OR = {or_str}, 95\\\\% exact CI = [{ci_lo}, {ci_hi}], \"\n                 f\"$p$ = {fmt_p(fisher['p_value'])}\")\n        L.append(\"\")\n\n        # Permutation\n        L.append(f\"**2. Genuine Rate Permutation Test** ($n$ = {perm['n_perm']:,} permutations)\")\n        L.append(f\"- ISR mean: {perm['isr_mean']*100:.2f}\\\\%, Random mean: {perm['random_mean']*100:.2f}\\\\%\")\n        L.append(f\"- $\\\\Delta$ = {perm['observed_diff']*100:.2f} pp, $p$ = {fmt_p(perm['p_value'])}\")\n        L.append(\"\")\n\n        # Mann-Whitney\n        L.append(\"**3. H7 Rate Mann-Whitney $U$ Test**\")\n        L.append(f\"- ISR median: {mw['isr_median']*100:.1f}\\\\%, Random median: {mw['random_median']*100:.1f}\\\\%\")\n        L.append(f\"- $U$ = {mw['U']:.1f}, $p$ = {fmt_p(mw['p_value'])}, \"\n                 f\"rank-biserial $r$ = {mw['r_rank_biserial']:.3f}\")\n        L.append(\"\")\n\n        # Bayes Factor\n        L.append(\"**4. Bayes Factor** (Beta-Binomial conjugate, prior: Beta(1,1))\")\n        L.append(f\"- $BF_{{10}}$ = {bf['bf10']:.2f} ({bf['interpretation']})\")\n        L.append(f\"- ISR: {bf['k_isr']}/{bf['n_isr']} H7-dominated, \"\n                 f\"Random: {bf['k_rand']}/{bf['n_rand']}\")\n\n    return \"\\n\".join(L) + \"\\n\"\n\n\n# --- Main ---\n\ndef main():\n    args = parse_args()\n    data_dir = Path(args.data_dir)\n\n    if not data_dir.exists():\n        print(f\"ERROR: data directory {data_dir} does not exist\", file=sys.stderr)\n        sys.exit(1)\n\n    if args.prefix:\n        prefixes = [args.prefix]\n    elif args.prefixes:\n        prefixes = [p.strip() for p in args.prefixes.split(\",\")]\n    else:\n        prefixes = MODE_PREFIXES[args.mode]\n    print(f\"Mode: {args.mode} | Prefixes: {prefixes}\")\n\n    runs = discover_runs(data_dir, prefixes)\n    if not runs:\n        print(f\"ERROR: no runs found in {data_dir} with prefixes {prefixes}\", file=sys.stderr)\n        sys.exit(1)\n\n    isr_count = sum(1 for r in runs if r[\"condition\"] == \"ISR\")\n    rand_count = sum(1 for r in runs if r[\"condition\"] == \"RANDOM\")\n    print(f\"Found {len(runs)} runs: {isr_count} ISR, {rand_count} RANDOM\")\n    for r in runs:\n        print(f\"  {r['condition']:6s} s{r['seed']} <- {r['dir_name']}\")\n\n    df = build_table(runs)\n    print_per_seed_table(df)\n\n    cond_df = condition_stats(df)\n    print_condition_stats(cond_df)\n\n    if isr_count < 2 or rand_count < 2:\n        print(\"\\nWARNING: need >= 2 seeds per condition for statistical tests, skipping.\",\n              file=sys.stderr)\n        bca_h7 = bca_bootstrap_ci(df, \"H7_rate\", args.n_boot, args.seed)\n        bca_gen = bca_bootstrap_ci(df, \"genuine_rate\", args.n_boot, args.seed)\n        if args.output:\n            md = generate_markdown(df, cond_df, {}, {}, {}, {}, bca_h7, bca_gen)\n            Path(args.output).write_text(md)\n            print(f\"\\nMarkdown written to {args.output}\")\n        return\n\n    fisher = fisher_h7_domination(df)\n    perm = permutation_test_genuine(df, n_perm=args.n_perm, rng_seed=args.seed)\n    mw = mannwhitney_h7(df)\n    bf = bayes_factor_h7_domination(df)\n    bca_h7 = bca_bootstrap_ci(df, \"H7_rate\", args.n_boot, args.seed)\n    bca_gen = bca_bootstrap_ci(df, \"genuine_rate\", args.n_boot, args.seed)\n\n    print_tests(fisher, perm, mw, bf, bca_h7, bca_gen)\n\n    md = generate_markdown(df, cond_df, fisher, perm, mw, bf, bca_h7, bca_gen)\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  MARKDOWN OUTPUT (appendix-ready)\")\n    print(\"=\" * 90)\n    print(md)\n\n    if args.output:\n        Path(args.output).parent.mkdir(parents=True, exist_ok=True)\n        Path(args.output).write_text(md)\n        print(f\"Markdown written to {args.output}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 557,
        "oldLines": 6,
        "newStart": 557,
        "newLines": 14,
        "lines": [
          "         L.append(f\"- ISR: {bf['k_isr']}/{bf['n_isr']} H7-dominated, \"",
          "                  f\"Random: {bf['k_rand']}/{bf['n_rand']}\")",
          " ",
          "+        if mw_isr_star:",
          "+            L.append(\"\")",
          "+            L.append(\"**5. ISR* (Proved-Only Mean ISR) Mann-Whitney $U$ Test**\")",
          "+            L.append(f\"- ISR mean: {mw_isr_star['isr_mean']:.4f}, median: {mw_isr_star['isr_median']:.4f}\")",
          "+            L.append(f\"- Random mean: {mw_isr_star['random_mean']:.4f}, median: {mw_isr_star['random_median']:.4f}\")",
          "+            L.append(f\"- $U$ = {mw_isr_star['U']:.1f}, $p$ = {fmt_p(mw_isr_star['p_value'])}, \"",
          "+                     f\"rank-biserial $r$ = {mw_isr_star['r_rank_biserial']:.3f}\")",
          "+",
          "     return \"\\n\".join(L) + \"\\n\"",
          " ",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 51_

**Edit 9**: Update `main()` to call `mannwhitney_isr_star` and pass to output functions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "cf9470be-76ae-424f-a3fb-493ac07f03ae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TpC3sYivBfY1BueVMEJuKu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 586,
      "cache_read_input_tokens": 51390,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 586
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

_source line 52_

<details open><summary>🔧 Tool call — Edit · `toolu_01RdSaTCFiPJ8VKdyXcmY5Vr`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/scripts/d134_analysis.py",
  "old_string": "    fisher = fisher_h7_domination(df)\n    perm = permutation_test_genuine(df, n_perm=args.n_perm, rng_seed=args.seed)\n    mw = mannwhitney_h7(df)\n    bf = bayes_factor_h7_domination(df)\n    bca_h7 = bca_bootstrap_ci(df, \"H7_rate\", args.n_boot, args.seed)\n    bca_gen = bca_bootstrap_ci(df, \"genuine_rate\", args.n_boot, args.seed)\n\n    print_tests(fisher, perm, mw, bf, bca_h7, bca_gen)\n\n    md = generate_markdown(df, cond_df, fisher, perm, mw, bf, bca_h7, bca_gen)",
  "new_string": "    fisher = fisher_h7_domination(df)\n    perm = permutation_test_genuine(df, n_perm=args.n_perm, rng_seed=args.seed)\n    mw = mannwhitney_h7(df)\n    bf = bayes_factor_h7_domination(df)\n    bca_h7 = bca_bootstrap_ci(df, \"H7_rate\", args.n_boot, args.seed)\n    bca_gen = bca_bootstrap_ci(df, \"genuine_rate\", args.n_boot, args.seed)\n    mw_isr_star = mannwhitney_isr_star(df)\n\n    print_tests(fisher, perm, mw, bf, bca_h7, bca_gen, mw_isr_star)\n\n    md = generate_markdown(df, cond_df, fisher, perm, mw, bf, bca_h7, bca_gen, mw_isr_star)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "2ff11a3a-6ad3-4c54-ac65-af04c059ce00",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TpC3sYivBfY1BueVMEJuKu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 586,
      "cache_read_input_tokens": 51390,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 586
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

_source line 53 · 2026-05-18T23:33:29.968Z_

<details><summary>↩ Tool result · `toolu_01RdSaTCFiPJ8VKdyXcmY5Vr`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/scripts/d134_analysis.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "26f5b72a-d8ca-4d6c-ab49-610d34244006",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/scripts/d134_analysis.py",
    "oldString": "    fisher = fisher_h7_domination(df)\n    perm = permutation_test_genuine(df, n_perm=args.n_perm, rng_seed=args.seed)\n    mw = mannwhitney_h7(df)\n    bf = bayes_factor_h7_domination(df)\n    bca_h7 = bca_bootstrap_ci(df, \"H7_rate\", args.n_boot, args.seed)\n    bca_gen = bca_bootstrap_ci(df, \"genuine_rate\", args.n_boot, args.seed)\n\n    print_tests(fisher, perm, mw, bf, bca_h7, bca_gen)\n\n    md = generate_markdown(df, cond_df, fisher, perm, mw, bf, bca_h7, bca_gen)",
    "newString": "    fisher = fisher_h7_domination(df)\n    perm = permutation_test_genuine(df, n_perm=args.n_perm, rng_seed=args.seed)\n    mw = mannwhitney_h7(df)\n    bf = bayes_factor_h7_domination(df)\n    bca_h7 = bca_bootstrap_ci(df, \"H7_rate\", args.n_boot, args.seed)\n    bca_gen = bca_bootstrap_ci(df, \"genuine_rate\", args.n_boot, args.seed)\n    mw_isr_star = mannwhitney_isr_star(df)\n\n    print_tests(fisher, perm, mw, bf, bca_h7, bca_gen, mw_isr_star)\n\n    md = generate_markdown(df, cond_df, fisher, perm, mw, bf, bca_h7, bca_gen, mw_isr_star)",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"D134 experiment analysis: multi-seed ISR vs Random, 4B GRPO training.\nReads taxonomy data from classify.json, taxonomy.json, or top-level taxonomy files.\nComputes summary stats, statistical tests (Fisher, Mann-Whitney, permutation, Bayes Factor),\nand BCa bootstrap CIs. Outputs appendix-ready markdown.\n\"\"\"\n\nimport argparse\nimport json\nimport re\nimport sys\nfrom pathlib import Path\n\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\nfrom scipy.special import betaln\n\nCONDITION_MAP = [\n    (\"d134_4b_isr\", \"ISR\"),\n    (\"d134_4b_random\", \"RANDOM\"),\n    (\"plan002_additive\", \"ISR\"),\n    (\"plan018_additive_random\", \"RANDOM\"),\n    (\"plan018_random\", \"RANDOM\"),\n]\n\nMODE_PREFIXES = {\n    \"d134_only\": [\"d134_4b\"],\n    \"all\": [\"d134_4b\", \"plan002_additive_b01\", \"plan018_additive_random_b01\", \"plan018_random\"],\n}\n\n\ndef parse_args():\n    p = argparse.ArgumentParser(description=\"D134 multi-seed analysis and statistical tests\")\n    p.add_argument(\"--data_dir\", type=str, default=\"/root/autodl-tmp/outputs\",\n                   help=\"Directory containing experiment outputs\")\n    p.add_argument(\"--mode\", type=str, default=\"d134_only\", choices=list(MODE_PREFIXES),\n                   help=\"d134_only = matched 5+5 design (default); all = include original seeds\")\n    p.add_argument(\"--prefix\", type=str, default=None,\n                   help=\"(Legacy) Single prefix filter; overrides mode/prefixes\")\n    p.add_argument(\"--prefixes\", type=str, default=None,\n                   help=\"Comma-separated prefixes; overrides --mode\")\n    p.add_argument(\"--output\", type=str, default=None,\n                   help=\"Write markdown summary to this file\")\n    p.add_argument(\"--n_perm\", type=int, default=10000,\n                   help=\"Number of permutations for permutation test\")\n    p.add_argument(\"--n_boot\", type=int, default=10000,\n                   help=\"Number of bootstrap resamples for BCa CI\")\n    p.add_argument(\"--seed\", type=int, default=42,\n                   help=\"Random seed for permutation/bootstrap\")\n    return p.parse_args()\n\n\n# --- Data loading ---\n\ndef match_condition(name: str) -> str | None:\n    best_prefix = \"\"\n    best_cond = None\n    for prefix, cond in CONDITION_MAP:\n        if name.startswith(prefix) and len(prefix) > len(best_prefix):\n            best_prefix = prefix\n            best_cond = cond\n    return best_cond\n\n\ndef extract_seed(name: str) -> int | None:\n    m = re.search(r'_s(\\d+)', name)\n    return int(m.group(1)) if m else None\n\n\ndef load_eval_results(path: Path) -> dict | None:\n    if not path.exists():\n        return None\n    with open(path) as f:\n        data = json.load(f)\n    if \"eval_results\" in data:\n        return data[\"eval_results\"]\n    return data\n\n\ndef load_taxonomy_unified(path: Path) -> dict | None:\n    with open(path) as f:\n        raw = json.load(f)\n    t = raw.get(\"taxonomy\", {})\n    proved = t.get(\"proved\", 0)\n    if proved == 0:\n        return None\n    h7 = t.get(\"H7\", 0)\n    h1 = t.get(\"H1_exact\", 0)\n    h8 = t.get(\"H8\", 0)\n    genuine = t.get(\"genuine\", 0)\n    return {\n        \"n_total\": 100, \"n_proved\": proved,\n        \"h7_total_count\": h7, \"h7_total_rate\": h7 / proved,\n        \"h1_strict_count\": h1, \"h8_conjunction_collapse_count\": h8,\n        \"genuine_count\": genuine, \"genuine_rate\": genuine / proved,\n        \"content_independent_count\": 0,\n    }\n\n\ndef load_taxonomy_verification(path: Path) -> dict | None:\n    with open(path) as f:\n        raw = json.load(f)\n    proved = raw.get(\"proved\", 0)\n    if proved == 0:\n        return None\n    tax = raw.get(\"taxonomy\", {})\n    h7 = tax.get(\"h7\", {}).get(\"count\", 0)\n    h1 = tax.get(\"h1_exact\", {}).get(\"count\", 0)\n    h8 = tax.get(\"h8\", {}).get(\"count\", 0)\n    genuine = tax.get(\"genuine\", {}).get(\"count\", 0)\n    return {\n        \"n_total\": raw.get(\"total\", 100), \"n_proved\": proved,\n        \"h7_total_count\": h7, \"h7_total_rate\": h7 / proved,\n        \"h1_strict_count\": h1, \"h8_conjunction_collapse_count\": h8,\n        \"genuine_count\": genuine, \"genuine_rate\": genuine / proved,\n        \"content_independent_count\": 0,\n    }\n\n\ndef discover_runs(data_dir: Path, prefixes: list[str]) -> list[dict]:\n    runs = []\n    seen = set()\n    for entry in sorted(data_dir.iterdir()):\n        name = entry.name\n        if not any(name.startswith(p) for p in prefixes):\n            continue\n        cond = match_condition(name)\n        seed_val = extract_seed(name)\n        if cond is None or seed_val is None:\n            continue\n        key = (cond, seed_val)\n        if key in seen:\n            continue\n        data = None\n        if entry.is_dir():\n            for fname in [\"classify.json\", \"taxonomy.json\"]:\n                data = load_eval_results(entry / fname)\n                if data is not None:\n                    break\n            if data is None:\n                continue\n        elif entry.is_file():\n            if name.endswith(\"_taxonomy_unified.json\"):\n                data = load_taxonomy_unified(entry)\n            elif name.endswith(\"_taxonomy_verification.json\"):\n                data = load_taxonomy_verification(entry)\n            if data is None:\n                continue\n        else:\n            continue\n        seen.add(key)\n        isr_star = None\n        if entry.is_dir():\n            eval_path = entry / \"eval_results.json\"\n            if eval_path.exists():\n                with open(eval_path) as ef:\n                    eval_raw = json.load(ef)\n                isr_star = eval_raw.get(\"summary\", {}).get(\"proved_only_mean_isr\")\n        runs.append({\"dir_name\": name, \"seed\": seed_val, \"condition\": cond,\n                      \"data\": data, \"isr_star\": isr_star})\n    return runs\n\n\ndef compute_row(run: dict) -> dict:\n    d = run[\"data\"]\n    n_proved = d.get(\"n_proved\", 0)\n    n_total = d.get(\"n_total\", 100)\n    h7 = d.get(\"h7_total_count\", 0)\n    h7_rate = d.get(\"h7_total_rate\", h7 / n_proved if n_proved > 0 else 0.0)\n    h1 = d.get(\"h1_strict_count\", 0)\n    h8 = d.get(\"h8_conjunction_collapse_count\", 0)\n    genuine = d.get(\"genuine_count\", 0)\n    genuine_rate = d.get(\"genuine_rate\", genuine / n_proved if n_proved > 0 else 0.0)\n    ci = d.get(\"content_independent_count\", 0)\n    snh = max(genuine - ci, 0)\n    snh_rate = snh / n_proved if n_proved > 0 else 0.0\n    return {\n        \"seed\": run[\"seed\"], \"condition\": run[\"condition\"], \"n_total\": n_total,\n        \"PR\": n_proved, \"H7_count\": h7, \"H7_rate\": h7_rate,\n        \"H1_count\": h1, \"H8_count\": h8,\n        \"genuine_count\": genuine, \"genuine_rate\": genuine_rate,\n        \"CI_count\": ci, \"SNH_count\": snh, \"SNH_rate\": snh_rate,\n        \"ISR_star\": run.get(\"isr_star\"),\n    }\n\n\ndef build_table(runs: list[dict]) -> pd.DataFrame:\n    rows = [compute_row(r) for r in runs]\n    df = pd.DataFrame(rows)\n    df = df.sort_values([\"condition\", \"seed\"]).reset_index(drop=True)\n    return df\n\n\n# --- Statistical tests ---\n\ndef fisher_h7_domination(df: pd.DataFrame) -> dict:\n    results = {}\n    for cond in [\"ISR\", \"RANDOM\"]:\n        sub = df[df[\"condition\"] == cond]\n        results[cond] = {\n            \"n\": len(sub),\n            \"h7_dom\": int((sub[\"H7_rate\"] >= 0.5).sum()),\n            \"not_h7_dom\": int((sub[\"H7_rate\"] < 0.5).sum()),\n        }\n    table = np.array([\n        [results[\"ISR\"][\"h7_dom\"], results[\"ISR\"][\"not_h7_dom\"]],\n        [results[\"RANDOM\"][\"h7_dom\"], results[\"RANDOM\"][\"not_h7_dom\"]],\n    ])\n    odds_ratio, p_value = stats.fisher_exact(table, alternative=\"greater\")\n\n    # 95% exact CI via scipy.stats.contingency\n    or_ci_lo, or_ci_hi = np.nan, np.nan\n    try:\n        ct = stats.contingency.odds_ratio(table)\n        ci = ct.confidence_interval(confidence_level=0.95)\n        or_ci_lo, or_ci_hi = ci.low, ci.high\n    except Exception:\n        pass\n\n    return {\n        \"table\": table.tolist(),\n        \"ISR\": results[\"ISR\"],\n        \"RANDOM\": results[\"RANDOM\"],\n        \"odds_ratio\": odds_ratio,\n        \"or_ci_lo\": or_ci_lo,\n        \"or_ci_hi\": or_ci_hi,\n        \"p_value\": p_value,\n    }\n\n\ndef permutation_test_genuine(df: pd.DataFrame, n_perm: int = 10000,\n                              rng_seed: int = 42) -> dict:\n    isr = df[df[\"condition\"] == \"ISR\"][\"genuine_rate\"].values\n    rand = df[df[\"condition\"] == \"RANDOM\"][\"genuine_rate\"].values\n    observed = isr.mean() - rand.mean()\n    pooled = np.concatenate([isr, rand])\n    n_isr = len(isr)\n    rng = np.random.default_rng(rng_seed)\n    count = 0\n    for _ in range(n_perm):\n        perm = rng.permutation(pooled)\n        if perm[:n_isr].mean() - perm[n_isr:].mean() >= observed:\n            count += 1\n    return {\n        \"observed_diff\": float(observed),\n        \"p_value\": count / n_perm,\n        \"n_perm\": n_perm,\n        \"isr_mean\": float(isr.mean()),\n        \"random_mean\": float(rand.mean()),\n    }\n\n\ndef mannwhitney_h7(df: pd.DataFrame) -> dict:\n    isr = df[df[\"condition\"] == \"ISR\"][\"H7_rate\"].values\n    rand = df[df[\"condition\"] == \"RANDOM\"][\"H7_rate\"].values\n    n1, n2 = len(isr), len(rand)\n    u_stat, p_value = stats.mannwhitneyu(isr, rand, alternative=\"greater\")\n    r_rb = 2.0 * u_stat / (n1 * n2) - 1.0 if n1 * n2 > 0 else np.nan\n    return {\n        \"U\": float(u_stat),\n        \"p_value\": float(p_value),\n        \"r_rank_biserial\": float(r_rb),\n        \"isr_median\": float(np.median(isr)),\n        \"random_median\": float(np.median(rand)),\n    }\n\n\ndef mannwhitney_isr_star(df: pd.DataFrame) -> dict | None:\n    isr = df[df[\"condition\"] == \"ISR\"][\"ISR_star\"].dropna().values.astype(float)\n    rand = df[df[\"condition\"] == \"RANDOM\"][\"ISR_star\"].dropna().values.astype(float)\n    if len(isr) < 2 or len(rand) < 2:\n        return None\n    n1, n2 = len(isr), len(rand)\n    u_stat, p_value = stats.mannwhitneyu(isr, rand, alternative=\"greater\")\n    r_rb = 2.0 * u_stat / (n1 * n2) - 1.0\n    return {\n        \"U\": float(u_stat),\n        \"p_value\": float(p_value),\n        \"r_rank_biserial\": float(r_rb),\n        \"isr_median\": float(np.median(isr)),\n        \"random_median\": float(np.median(rand)),\n        \"isr_mean\": float(np.mean(isr)),\n        \"random_mean\": float(np.mean(rand)),\n    }\n\n\ndef bca_bootstrap_ci(df: pd.DataFrame, metric: str, n_boot: int = 10000,\n                      rng_seed: int = 42) -> dict:\n    \"\"\"BCa 95% CI for per-condition means of a metric.\"\"\"\n    result = {}\n    for cond in [\"ISR\", \"RANDOM\"]:\n        vals = df[df[\"condition\"] == cond][metric].values\n        if len(vals) < 2:\n            result[cond] = {\"mean\": float(vals.mean()) if len(vals) else np.nan,\n                            \"ci_lo\": np.nan, \"ci_hi\": np.nan}\n            continue\n        res = stats.bootstrap(\n            (vals,), np.mean, n_resamples=n_boot,\n            confidence_level=0.95, method=\"BCa\",\n            random_state=np.random.default_rng(rng_seed),\n        )\n        result[cond] = {\n            \"mean\": float(vals.mean()),\n            \"ci_lo\": float(res.confidence_interval.low),\n            \"ci_hi\": float(res.confidence_interval.high),\n        }\n    return result\n\n\ndef bayes_factor_h7_domination(df: pd.DataFrame) -> dict:\n    \"\"\"BF10 for H7-domination rate difference (beta-binomial conjugate).\n    H0: ISR and Random share same domination rate.\n    H1: independent rates. Prior: Beta(1,1) on each.\n    \"\"\"\n    isr_sub = df[df[\"condition\"] == \"ISR\"]\n    rand_sub = df[df[\"condition\"] == \"RANDOM\"]\n    k_isr = int((isr_sub[\"H7_rate\"] >= 0.5).sum())\n    n_isr = len(isr_sub)\n    k_rand = int((rand_sub[\"H7_rate\"] >= 0.5).sum())\n    n_rand = len(rand_sub)\n    k_total = k_isr + k_rand\n    n_total = n_isr + n_rand\n\n    # log marginal under H0 (shared rate)\n    log_m_h0 = betaln(1 + k_total, 1 + n_total - k_total) - betaln(1, 1)\n    # log marginal under H1 (independent rates)\n    log_m_h1 = (betaln(1 + k_isr, 1 + n_isr - k_isr) - betaln(1, 1)\n                + betaln(1 + k_rand, 1 + n_rand - k_rand) - betaln(1, 1))\n    log_bf10 = log_m_h1 - log_m_h0\n    bf10 = float(np.exp(log_bf10))\n\n    return {\n        \"k_isr\": k_isr, \"n_isr\": n_isr,\n        \"k_rand\": k_rand, \"n_rand\": n_rand,\n        \"bf10\": bf10,\n        \"log_bf10\": float(log_bf10),\n        \"interpretation\": _interpret_bf(bf10),\n    }\n\n\ndef _interpret_bf(bf: float) -> str:\n    if bf > 100:\n        return \"extreme evidence for H1\"\n    if bf > 30:\n        return \"very strong evidence for H1\"\n    if bf > 10:\n        return \"strong evidence for H1\"\n    if bf > 3:\n        return \"moderate evidence for H1\"\n    if bf > 1:\n        return \"anecdotal evidence for H1\"\n    if bf > 1/3:\n        return \"anecdotal evidence (inconclusive)\"\n    if bf > 1/10:\n        return \"moderate evidence for H0\"\n    return \"strong evidence for H0\"\n\n\ndef condition_stats(df: pd.DataFrame) -> pd.DataFrame:\n    metrics = [\"PR\", \"H7_rate\", \"genuine_rate\", \"SNH_rate\"]\n    rows = []\n    for cond in [\"ISR\", \"RANDOM\"]:\n        sub = df[df[\"condition\"] == cond]\n        row = {\"condition\": cond, \"n_seeds\": len(sub)}\n        for m in metrics:\n            vals = sub[m].values\n            row[f\"{m}_mean\"] = vals.mean()\n            row[f\"{m}_std\"] = vals.std(ddof=1) if len(vals) > 1 else 0.0\n        isr_vals = sub[\"ISR_star\"].dropna().values.astype(float)\n        row[\"ISR_star_mean\"] = isr_vals.mean() if len(isr_vals) else np.nan\n        row[\"ISR_star_std\"] = isr_vals.std(ddof=1) if len(isr_vals) > 1 else 0.0\n        rows.append(row)\n    return pd.DataFrame(rows)\n\n\n# --- Formatting ---\n\ndef fmt_pct(val: float) -> str:\n    return f\"{val*100:.1f}\\\\%\"\n\ndef fmt_or(val: float) -> str:\n    return \"$\\\\infty$\" if np.isinf(val) else f\"{val:.2f}\"\n\ndef fmt_ci(lo: float, hi: float) -> str:\n    lo_s = f\"{lo:.2f}\" if not np.isnan(lo) else \"0\"\n    hi_s = \"$\\\\infty$\" if np.isinf(hi) or np.isnan(hi) else f\"{hi:.2f}\"\n    return f\"[{lo_s}, {hi_s}]\"\n\ndef fmt_p(p: float) -> str:\n    if p < 0.001:\n        return \"$<$0.001\"\n    return f\"{p:.3f}\"\n\ndef fmt_mean_std(mean: float, std: float, pct: bool = False) -> str:\n    if pct:\n        return f\"{mean*100:.1f} $\\\\pm$ {std*100:.1f}\\\\%\"\n    return f\"{mean:.1f} $\\\\pm$ {std:.1f}\"\n\ndef fmt_bca(bca: dict, pct: bool = False) -> str:\n    m = bca[\"mean\"]\n    lo, hi = bca[\"ci_lo\"], bca[\"ci_hi\"]\n    if pct:\n        return f\"{m*100:.1f}\\\\% [{lo*100:.1f}, {hi*100:.1f}]\"\n    return f\"{m:.1f} [{lo:.1f}, {hi:.1f}]\"\n\n\n# --- Console output ---\n\ndef print_per_seed_table(df: pd.DataFrame):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  PER-SEED RESULTS\")\n    print(\"=\" * 90)\n    cols = [\"condition\", \"seed\", \"PR\", \"H7_count\", \"H7_rate\", \"H1_count\",\n            \"H8_count\", \"genuine_count\", \"genuine_rate\", \"CI_count\", \"SNH_count\", \"SNH_rate\",\n            \"ISR_star\"]\n    fmt = df[cols].copy()\n    for c in [\"H7_rate\", \"genuine_rate\", \"SNH_rate\"]:\n        fmt[c] = fmt[c].apply(lambda v: f\"{v*100:.1f}%\")\n    fmt[\"ISR_star\"] = fmt[\"ISR_star\"].apply(lambda v: f\"{v:.4f}\" if pd.notna(v) else \"---\")\n    print(fmt.to_string(index=False))\n\n\ndef print_condition_stats(cond_df: pd.DataFrame):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  CONDITION-LEVEL STATISTICS (mean +/- SD)\")\n    print(\"=\" * 90)\n    for _, row in cond_df.iterrows():\n        n = int(row['n_seeds'])\n        print(f\"\\n  {row['condition']} (n={n} seeds):\")\n        print(f\"    PR:           {row['PR_mean']:.1f} +/- {row['PR_std']:.1f}\")\n        print(f\"    H7 rate:      {row['H7_rate_mean']*100:.1f} +/- {row['H7_rate_std']*100:.1f}%\")\n        print(f\"    Genuine rate: {row['genuine_rate_mean']*100:.1f} +/- {row['genuine_rate_std']*100:.1f}%\")\n        print(f\"    S-NH rate:    {row['SNH_rate_mean']*100:.1f} +/- {row['SNH_rate_std']*100:.1f}%\")\n        if not np.isnan(row.get('ISR_star_mean', np.nan)):\n            print(f\"    ISR*:         {row['ISR_star_mean']:.4f} +/- {row['ISR_star_std']:.4f}\")\n\n\ndef print_tests(fisher, perm, mw, bf, bca_h7, bca_gen, mw_isr_star=None):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  STATISTICAL TESTS\")\n    print(\"=\" * 90)\n\n    print(\"\\n  1. H7 Domination Fisher Exact Test (H7-dominated = H7% >= 50%)\")\n    print(f\"     ISR:    {fisher['ISR']['h7_dom']} dominated / {fisher['ISR']['n']} seeds\")\n    print(f\"     RANDOM: {fisher['RANDOM']['h7_dom']} dominated / {fisher['RANDOM']['n']} seeds\")\n    print(f\"     Contingency: {fisher['table']}\")\n    or_str = \"inf\" if np.isinf(fisher['odds_ratio']) else f\"{fisher['odds_ratio']:.4f}\"\n    print(f\"     OR = {or_str}, 95% CI = [{fisher['or_ci_lo']:.4f}, {fisher['or_ci_hi']:.4f}]\"\n          if not np.isnan(fisher['or_ci_lo']) else f\"     OR = {or_str}, 95% CI = N/A\")\n    print(f\"     p-value (one-sided, greater): {fisher['p_value']:.4f}\")\n\n    print(f\"\\n  2. Genuine Rate Permutation Test (n_perm={perm['n_perm']})\")\n    print(f\"     ISR mean:    {perm['isr_mean']*100:.2f}%\")\n    print(f\"     RANDOM mean: {perm['random_mean']*100:.2f}%\")\n    print(f\"     Diff: {perm['observed_diff']*100:.2f} pp, p = {perm['p_value']:.4f}\")\n\n    print(f\"\\n  3. H7 Rate Mann-Whitney U Test\")\n    print(f\"     ISR median:    {mw['isr_median']*100:.1f}%\")\n    print(f\"     RANDOM median: {mw['random_median']*100:.1f}%\")\n    print(f\"     U = {mw['U']:.1f}, p = {mw['p_value']:.4f}\")\n    print(f\"     Rank-biserial r = {mw['r_rank_biserial']:.4f}\")\n\n    print(f\"\\n  4. Bayes Factor (H7 Domination, Beta-Binomial)\")\n    print(f\"     ISR:    {bf['k_isr']}/{bf['n_isr']} dominated\")\n    print(f\"     RANDOM: {bf['k_rand']}/{bf['n_rand']} dominated\")\n    print(f\"     BF10 = {bf['bf10']:.4f} ({bf['interpretation']})\")\n\n    print(f\"\\n  5. BCa Bootstrap 95% CI (n_boot resamples)\")\n    for label, bca in [(\"H7 rate\", bca_h7), (\"Genuine rate\", bca_gen)]:\n        print(f\"     {label}:\")\n        for cond in [\"ISR\", \"RANDOM\"]:\n            b = bca[cond]\n            print(f\"       {cond}: {b['mean']*100:.1f}% [{b['ci_lo']*100:.1f}, {b['ci_hi']*100:.1f}]\"\n                  if not np.isnan(b['ci_lo']) else f\"       {cond}: {b['mean']*100:.1f}% [N/A]\")\n\n    if mw_isr_star:\n        print(f\"\\n  6. ISR* (Proved-Only Mean ISR) Mann-Whitney U Test\")\n        print(f\"     ISR mean:    {mw_isr_star['isr_mean']:.4f}, median: {mw_isr_star['isr_median']:.4f}\")\n        print(f\"     RANDOM mean: {mw_isr_star['random_mean']:.4f}, median: {mw_isr_star['random_median']:.4f}\")\n        print(f\"     U = {mw_isr_star['U']:.1f}, p = {mw_isr_star['p_value']:.4f}\")\n        print(f\"     Rank-biserial r = {mw_isr_star['r_rank_biserial']:.4f}\")\n\n\n# --- Markdown generation (appendix-ready) ---\n\ndef generate_markdown(df: pd.DataFrame, cond_df: pd.DataFrame,\n                      fisher: dict, perm: dict, mw: dict,\n                      bf: dict, bca_h7: dict, bca_gen: dict,\n                      mw_isr_star: dict = None) -> str:\n    L = []\n    L.append(\"## D134: ISR vs Random Statistical Analysis\\n\")\n\n    # Per-seed table\n    L.append(\"### Table A1: Per-Seed Hacking Taxonomy (4B Qwen3, 500 steps)\\n\")\n    L.append(\"| Condition | Seed | PR | H7 | H7\\\\% | H1 | H8 | Genuine | Gen\\\\% | CI | S-NH | S-NH\\\\% | ISR* |\")\n    L.append(\"|:----------|-----:|---:|---:|-----:|---:|---:|--------:|------:|---:|-----:|-------:|-----:|\")\n    for _, r in df.iterrows():\n        isr_star_str = f\"{r['ISR_star']:.4f}\" if pd.notna(r.get('ISR_star')) else \"---\"\n        L.append(\n            f\"| {r['condition']} | {r['seed']} | {int(r['PR'])} | {int(r['H7_count'])} | \"\n            f\"{r['H7_rate']*100:.1f} | {int(r['H1_count'])} | {int(r['H8_count'])} | \"\n            f\"{int(r['genuine_count'])} | {r['genuine_rate']*100:.1f} | {int(r['CI_count'])} | \"\n            f\"{int(r['SNH_count'])} | {r['SNH_rate']*100:.1f} | {isr_star_str} |\"\n        )\n\n    # Condition summary with BCa CI\n    L.append(\"\\n### Table A2: Condition-Level Summary\\n\")\n    L.append(\"| Condition | $n$ | PR (mean$\\\\pm$SD) | H7\\\\% (mean$\\\\pm$SD) | H7\\\\% BCa 95\\\\% CI | Gen\\\\% (mean$\\\\pm$SD) | Gen\\\\% BCa 95\\\\% CI |\")\n    L.append(\"|:----------|----:|:------------------|:-------------------|:-----------------|:-------------------|:-----------------|\")\n    for _, r in cond_df.iterrows():\n        cond = r[\"condition\"]\n        h7_bca = bca_h7.get(cond, {})\n        gen_bca = bca_gen.get(cond, {})\n        h7_ci = f\"[{h7_bca['ci_lo']*100:.1f}, {h7_bca['ci_hi']*100:.1f}]\" if h7_bca and not np.isnan(h7_bca.get('ci_lo', np.nan)) else \"N/A\"\n        gen_ci = f\"[{gen_bca['ci_lo']*100:.1f}, {gen_bca['ci_hi']*100:.1f}]\" if gen_bca and not np.isnan(gen_bca.get('ci_lo', np.nan)) else \"N/A\"\n        L.append(\n            f\"| {cond} | {int(r['n_seeds'])} | \"\n            f\"{r['PR_mean']:.1f}$\\\\pm${r['PR_std']:.1f} | \"\n            f\"{r['H7_rate_mean']*100:.1f}$\\\\pm${r['H7_rate_std']*100:.1f} | \"\n            f\"{h7_ci} | \"\n            f\"{r['genuine_rate_mean']*100:.1f}$\\\\pm${r['genuine_rate_std']*100:.1f} | \"\n            f\"{gen_ci} |\"\n        )\n\n    # Statistical tests\n    if fisher and perm and mw and bf:\n        L.append(\"\\n### Statistical Tests\\n\")\n\n        # Fisher\n        or_str = \"$\\\\infty$\" if np.isinf(fisher['odds_ratio']) else f\"{fisher['odds_ratio']:.2f}\"\n        ci_lo = f\"{fisher['or_ci_lo']:.2f}\" if not np.isnan(fisher['or_ci_lo']) else \"0\"\n        ci_hi = \"$\\\\infty$\" if np.isinf(fisher.get('or_ci_hi', np.inf)) or np.isnan(fisher.get('or_ci_hi', np.nan)) else f\"{fisher['or_ci_hi']:.2f}\"\n        L.append(\"**1. H7 Domination Fisher Exact Test** (threshold: H7$\\\\geq$50\\\\% of proved)\")\n        L.append(f\"- ISR: {fisher['ISR']['h7_dom']}/{fisher['ISR']['n']} seeds H7-dominated; \"\n                 f\"Random: {fisher['RANDOM']['h7_dom']}/{fisher['RANDOM']['n']}\")\n        L.append(f\"- OR = {or_str}, 95\\\\% exact CI = [{ci_lo}, {ci_hi}], \"\n                 f\"$p$ = {fmt_p(fisher['p_value'])}\")\n        L.append(\"\")\n\n        # Permutation\n        L.append(f\"**2. Genuine Rate Permutation Test** ($n$ = {perm['n_perm']:,} permutations)\")\n        L.append(f\"- ISR mean: {perm['isr_mean']*100:.2f}\\\\%, Random mean: {perm['random_mean']*100:.2f}\\\\%\")\n        L.append(f\"- $\\\\Delta$ = {perm['observed_diff']*100:.2f} pp, $p$ = {fmt_p(perm['p_value'])}\")\n        L.append(\"\")\n\n        # Mann-Whitney\n        L.append(\"**3. H7 Rate Mann-Whitney $U$ Test**\")\n        L.append(f\"- ISR median: {mw['isr_median']*100:.1f}\\\\%, Random median: {mw['random_median']*100:.1f}\\\\%\")\n        L.append(f\"- $U$ = {mw['U']:.1f}, $p$ = {fmt_p(mw['p_value'])}, \"\n                 f\"rank-biserial $r$ = {mw['r_rank_biserial']:.3f}\")\n        L.append(\"\")\n\n        # Bayes Factor\n        L.append(\"**4. Bayes Factor** (Beta-Binomial conjugate, prior: Beta(1,1))\")\n        L.append(f\"- $BF_{{10}}$ = {bf['bf10']:.2f} ({bf['interpretation']})\")\n        L.append(f\"- ISR: {bf['k_isr']}/{bf['n_isr']} H7-dominated, \"\n                 f\"Random: {bf['k_rand']}/{bf['n_rand']}\")\n\n        if mw_isr_star:\n            L.append(\"\")\n            L.append(\"**5. ISR* (Proved-Only Mean ISR) Mann-Whitney $U$ Test**\")\n            L.append(f\"- ISR mean: {mw_isr_star['isr_mean']:.4f}, median: {mw_isr_star['isr_median']:.4f}\")\n            L.append(f\"- Random mean: {mw_isr_star['random_mean']:.4f}, median: {mw_isr_star['random_median']:.4f}\")\n            L.append(f\"- $U$ = {mw_isr_star['U']:.1f}, $p$ = {fmt_p(mw_isr_star['p_value'])}, \"\n                     f\"rank-biserial $r$ = {mw_isr_star['r_rank_biserial']:.3f}\")\n\n    return \"\\n\".join(L) + \"\\n\"\n\n\n# --- Main ---\n\ndef main():\n    args = parse_args()\n    data_dir = Path(args.data_dir)\n\n    if not data_dir.exists():\n        print(f\"ERROR: data directory {data_dir} does not exist\", file=sys.stderr)\n        sys.exit(1)\n\n    if args.prefix:\n        prefixes = [args.prefix]\n    elif args.prefixes:\n        prefixes = [p.strip() for p in args.prefixes.split(\",\")]\n    else:\n        prefixes = MODE_PREFIXES[args.mode]\n    print(f\"Mode: {args.mode} | Prefixes: {prefixes}\")\n\n    runs = discover_runs(data_dir, prefixes)\n    if not runs:\n        print(f\"ERROR: no runs found in {data_dir} with prefixes {prefixes}\", file=sys.stderr)\n        sys.exit(1)\n\n    isr_count = sum(1 for r in runs if r[\"condition\"] == \"ISR\")\n    rand_count = sum(1 for r in runs if r[\"condition\"] == \"RANDOM\")\n    print(f\"Found {len(runs)} runs: {isr_count} ISR, {rand_count} RANDOM\")\n    for r in runs:\n        print(f\"  {r['condition']:6s} s{r['seed']} <- {r['dir_name']}\")\n\n    df = build_table(runs)\n    print_per_seed_table(df)\n\n    cond_df = condition_stats(df)\n    print_condition_stats(cond_df)\n\n    if isr_count < 2 or rand_count < 2:\n        print(\"\\nWARNING: need >= 2 seeds per condition for statistical tests, skipping.\",\n              file=sys.stderr)\n        bca_h7 = bca_bootstrap_ci(df, \"H7_rate\", args.n_boot, args.seed)\n        bca_gen = bca_bootstrap_ci(df, \"genuine_rate\", args.n_boot, args.seed)\n        if args.output:\n            md = generate_markdown(df, cond_df, {}, {}, {}, {}, bca_h7, bca_gen)\n            Path(args.output).write_text(md)\n            print(f\"\\nMarkdown written to {args.output}\")\n        return\n\n    fisher = fisher_h7_domination(df)\n    perm = permutation_test_genuine(df, n_perm=args.n_perm, rng_seed=args.seed)\n    mw = mannwhitney_h7(df)\n    bf = bayes_factor_h7_domination(df)\n    bca_h7 = bca_bootstrap_ci(df, \"H7_rate\", args.n_boot, args.seed)\n    bca_gen = bca_bootstrap_ci(df, \"genuine_rate\", args.n_boot, args.seed)\n\n    print_tests(fisher, perm, mw, bf, bca_h7, bca_gen)\n\n    md = generate_markdown(df, cond_df, fisher, perm, mw, bf, bca_h7, bca_gen)\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  MARKDOWN OUTPUT (appendix-ready)\")\n    print(\"=\" * 90)\n    print(md)\n\n    if args.output:\n        Path(args.output).parent.mkdir(parents=True, exist_ok=True)\n        Path(args.output).write_text(md)\n        print(f\"Markdown written to {args.output}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 620,
        "oldLines": 10,
        "newStart": 620,
        "newLines": 11,
        "lines": [
          "     bf = bayes_factor_h7_domination(df)",
          "     bca_h7 = bca_bootstrap_ci(df, \"H7_rate\", args.n_boot, args.seed)",
          "     bca_gen = bca_bootstrap_ci(df, \"genuine_rate\", args.n_boot, args.seed)",
          "+    mw_isr_star = mannwhitney_isr_star(df)",
          " ",
          "-    print_tests(fisher, perm, mw, bf, bca_h7, bca_gen)",
          "+    print_tests(fisher, perm, mw, bf, bca_h7, bca_gen, mw_isr_star)",
          " ",
          "-    md = generate_markdown(df, cond_df, fisher, perm, mw, bf, bca_h7, bca_gen)",
          "+    md = generate_markdown(df, cond_df, fisher, perm, mw, bf, bca_h7, bca_gen, mw_isr_star)",
          "     print(\"\\n\" + \"=\" * 90)",
          "     print(\"  MARKDOWN OUTPUT (appendix-ready)\")",
          "     print(\"=\" * 90)"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 54_

Also update the early-return path where `generate_markdown` is called without tests.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "357ae5f5-e22b-4b13-a9bb-5a9dd37cb0c6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PFMhQm8FAKUaonQKs5Xoqo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 785,
      "cache_read_input_tokens": 51976,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 785
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

_source line 55_

<details open><summary>🔧 Tool call — Read · `toolu_01FHTtFLGF1e6bZTptjqbZoJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/scripts/d134_analysis.py",
  "offset": 570,
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
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "adb65b4a-4994-4068-9da3-88d150b4feb8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PFMhQm8FAKUaonQKs5Xoqo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 785,
      "cache_read_input_tokens": 51976,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 785
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

_source line 56 · 2026-05-18T23:33:34.386Z_

<details><summary>↩ Tool result · `toolu_01FHTtFLGF1e6bZTptjqbZoJ`</summary>

```text
570	
571	# --- Main ---
572	
573	def main():
574	    args = parse_args()
575	    data_dir = Path(args.data_dir)
576	
577	    if not data_dir.exists():
578	        print(f"ERROR: data directory {data_dir} does not exist", file=sys.stderr)
579	        sys.exit(1)
580	
581	    if args.prefix:
582	        prefixes = [args.prefix]
583	    elif args.prefixes:
584	        prefixes = [p.strip() for p in args.prefixes.split(",")]
585	    else:
586	        prefixes = MODE_PREFIXES[args.mode]
587	    print(f"Mode: {args.mode} | Prefixes: {prefixes}")
588	
589	    runs = discover_runs(data_dir, prefixes)
590	    if not runs:
591	        print(f"ERROR: no runs found in {data_dir} with prefixes {prefixes}", file=sys.stderr)
592	        sys.exit(1)
593	
594	    isr_count = sum(1 for r in runs if r["condition"] == "ISR")
595	    rand_count = sum(1 for r in runs if r["condition"] == "RANDOM")
596	    print(f"Found {len(runs)} runs: {isr_count} ISR, {rand_count} RANDOM")
597	    for r in runs:
598	        print(f"  {r['condition']:6s} s{r['seed']} <- {r['dir_name']}")
599	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "c0480dcf-2fd6-4365-bf4f-becfa939b821",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/scripts/d134_analysis.py",
      "content": "\n# --- Main ---\n\ndef main():\n    args = parse_args()\n    data_dir = Path(args.data_dir)\n\n    if not data_dir.exists():\n        print(f\"ERROR: data directory {data_dir} does not exist\", file=sys.stderr)\n        sys.exit(1)\n\n    if args.prefix:\n        prefixes = [args.prefix]\n    elif args.prefixes:\n        prefixes = [p.strip() for p in args.prefixes.split(\",\")]\n    else:\n        prefixes = MODE_PREFIXES[args.mode]\n    print(f\"Mode: {args.mode} | Prefixes: {prefixes}\")\n\n    runs = discover_runs(data_dir, prefixes)\n    if not runs:\n        print(f\"ERROR: no runs found in {data_dir} with prefixes {prefixes}\", file=sys.stderr)\n        sys.exit(1)\n\n    isr_count = sum(1 for r in runs if r[\"condition\"] == \"ISR\")\n    rand_count = sum(1 for r in runs if r[\"condition\"] == \"RANDOM\")\n    print(f\"Found {len(runs)} runs: {isr_count} ISR, {rand_count} RANDOM\")\n    for r in runs:\n        print(f\"  {r['condition']:6s} s{r['seed']} <- {r['dir_name']}\")\n",
      "numLines": 30,
      "startLine": 570,
      "totalLines": 641
    }
  }
}
```

</details>

---

### Assistant

_source line 57_

Good, the early-return path at line ~607 already uses positional args for `generate_markdown` with `{}` for all test dicts, so `mw_isr_star` defaults to `None`. That's fine.

Now let me deploy the updated script to the server and run it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "8e886614-5475-446f-81db-79e7c0220a4e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nvq6PL5xXz1YWz1WAaJ4pV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 558,
      "cache_read_input_tokens": 52761,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 558
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

_source line 58_

<details open><summary>🔧 Tool call — Read · `toolu_011WccGwS8u9uDDVNv9v5htL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/scripts/d134_analysis.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "0bb83318-fe55-47b5-b0f1-ca66eeb3691d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nvq6PL5xXz1YWz1WAaJ4pV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 558,
      "cache_read_input_tokens": 52761,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 558
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

_source line 59 · 2026-05-18T23:33:39.334Z_

<details><summary>↩ Tool result · `toolu_011WccGwS8u9uDDVNv9v5htL`</summary>

```text
1	#!/usr/bin/env python3
2	"""D134 experiment analysis: multi-seed ISR vs Random, 4B GRPO training.
3	Reads taxonomy data from classify.json, taxonomy.json, or top-level taxonomy files.
4	Computes summary stats, statistical tests (Fisher, Mann-Whitney, permutation, Bayes Factor),
5	and BCa bootstrap CIs. Outputs appendix-ready markdown.
6	"""
7	
8	import argparse
9	import json
10	import re
11	import sys
12	from pathlib import Path
13	
14	import numpy as np
15	import pandas as pd
16	from scipy import stats
17	from scipy.special import betaln
18	
19	CONDITION_MAP = [
20	    ("d134_4b_isr", "ISR"),
21	    ("d134_4b_random", "RANDOM"),
22	    ("plan002_additive", "ISR"),
23	    ("plan018_additive_random", "RANDOM"),
24	    ("plan018_random", "RANDOM"),
25	]
26	
27	MODE_PREFIXES = {
28	    "d134_only": ["d134_4b"],
29	    "all": ["d134_4b", "plan002_additive_b01", "plan018_additive_random_b01", "plan018_random"],
30	}
31	
32	
33	def parse_args():
34	    p = argparse.ArgumentParser(description="D134 multi-seed analysis and statistical tests")
35	    p.add_argument("--data_dir", type=str, default="/root/autodl-tmp/outputs",
36	                   help="Directory containing experiment outputs")
37	    p.add_argument("--mode", type=str, default="d134_only", choices=list(MODE_PREFIXES),
38	                   help="d134_only = matched 5+5 design (default); all = include original seeds")
39	    p.add_argument("--prefix", type=str, default=None,
40	                   help="(Legacy) Single prefix filter; overrides mode/prefixes")
41	    p.add_argument("--prefixes", type=str, default=None,
42	                   help="Comma-separated prefixes; overrides --mode")
43	    p.add_argument("--output", type=str, default=None,
44	                   help="Write markdown summary to this file")
45	    p.add_argument("--n_perm", type=int, default=10000,
46	                   help="Number of permutations for permutation test")
47	    p.add_argument("--n_boot", type=int, default=10000,
48	                   help="Number of bootstrap resamples for BCa CI")
49	    p.add_argument("--seed", type=int, default=42,
50	                   help="Random seed for permutation/bootstrap")
51	    return p.parse_args()
52	
53	
54	# --- Data loading ---
55	
56	def match_condition(name: str) -> str | None:
57	    best_prefix = ""
58	    best_cond = None
59	    for prefix, cond in CONDITION_MAP:
60	        if name.startswith(prefix) and len(prefix) > len(best_prefix):
61	            best_prefix = prefix
62	            best_cond = cond
63	    return best_cond
64	
65	
66	def extract_seed(name: str) -> int | None:
67	    m = re.search(r'_s(\d+)', name)
68	    return int(m.group(1)) if m else None
69	
70	
71	def load_eval_results(path: Path) -> dict | None:
72	    if not path.exists():
73	        return None
74	    with open(path) as f:
75	        data = json.load(f)
76	    if "eval_results" in data:
77	        return data["eval_results"]
78	    return data
79	
80	
81	def load_taxonomy_unified(path: Path) -> dict | None:
82	    with open(path) as f:
83	        raw = json.load(f)
84	    t = raw.get("taxonomy", {})
85	    proved = t.get("proved", 0)
86	    if proved == 0:
87	        return None
88	    h7 = t.get("H7", 0)
89	    h1 = t.get("H1_exact", 0)
90	    h8 = t.get("H8", 0)
91	    genuine = t.get("genuine", 0)
92	    return {
93	        "n_total": 100, "n_proved": proved,
94	        "h7_total_count": h7, "h7_total_rate": h7 / proved,
95	        "h1_strict_count": h1, "h8_conjunction_collapse_count": h8,
96	        "genuine_count": genuine, "genuine_rate": genuine / proved,
97	        "content_independent_count": 0,
98	    }
99	
100	
101	def load_taxonomy_verification(path: Path) -> dict | None:
102	    with open(path) as f:
103	        raw = json.load(f)
104	    proved = raw.get("proved", 0)
105	    if proved == 0:
106	        return None
107	    tax = raw.get("taxonomy", {})
108	    h7 = tax.get("h7", {}).get("count", 0)
109	    h1 = tax.get("h1_exact", {}).get("count", 0)
110	    h8 = tax.get("h8", {}).get("count", 0)
111	    genuine = tax.get("genuine", {}).get("count", 0)
112	    return {
113	        "n_total": raw.get("total", 100), "n_proved": proved,
114	        "h7_total_count": h7, "h7_total_rate": h7 / proved,
115	        "h1_strict_count": h1, "h8_conjunction_collapse_count": h8,
116	        "genuine_count": genuine, "genuine_rate": genuine / proved,
117	        "content_independent_count": 0,
118	    }
119	
120	
121	def discover_runs(data_dir: Path, prefixes: list[str]) -> list[dict]:
122	    runs = []
123	    seen = set()
124	    for entry in sorted(data_dir.iterdir()):
125	        name = entry.name
126	        if not any(name.startswith(p) for p in prefixes):
127	            continue
128	        cond = match_condition(name)
129	        seed_val = extract_seed(name)
130	        if cond is None or seed_val is None:
131	            continue
132	        key = (cond, seed_val)
133	        if key in seen:
134	            continue
135	        data = None
136	        if entry.is_dir():
137	            for fname in ["classify.json", "taxonomy.json"]:
138	                data = load_eval_results(entry / fname)
139	                if data is not None:
140	                    break
141	            if data is None:
142	                continue
143	        elif entry.is_file():
144	            if name.endswith("_taxonomy_unified.json"):
145	                data = load_taxonomy_unified(entry)
146	            elif name.endswith("_taxonomy_verification.json"):
147	                data = load_taxonomy_verification(entry)
148	            if data is None:
149	                continue
150	        else:
151	            continue
152	        seen.add(key)
153	        isr_star = None
154	        if entry.is_dir():
155	            eval_path = entry / "eval_results.json"
156	            if eval_path.exists():
157	                with open(eval_path) as ef:
158	                    eval_raw = json.load(ef)
159	                isr_star = eval_raw.get("summary", {}).get("proved_only_mean_isr")
160	        runs.append({"dir_name": name, "seed": seed_val, "condition": cond,
161	                      "data": data, "isr_star": isr_star})
162	    return runs
163	
164	
165	def compute_row(run: dict) -> dict:
166	    d = run["data"]
167	    n_proved = d.get("n_proved", 0)
168	    n_total = d.get("n_total", 100)
169	    h7 = d.get("h7_total_count", 0)
170	    h7_rate = d.get("h7_total_rate", h7 / n_proved if n_proved > 0 else 0.0)
171	    h1 = d.get("h1_strict_count", 0)
172	    h8 = d.get("h8_conjunction_collapse_count", 0)
173	    genuine = d.get("genuine_count", 0)
174	    genuine_rate = d.get("genuine_rate", genuine / n_proved if n_proved > 0 else 0.0)
175	    ci = d.get("content_independent_count", 0)
176	    snh = max(genuine - ci, 0)
177	    snh_rate = snh / n_proved if n_proved > 0 else 0.0
178	    return {
179	        "seed": run["seed"], "condition": run["condition"], "n_total": n_total,
180	        "PR": n_proved, "H7_count": h7, "H7_rate": h7_rate,
181	        "H1_count": h1, "H8_count": h8,
182	        "genuine_count": genuine, "genuine_rate": genuine_rate,
183	        "CI_count": ci, "SNH_count": snh, "SNH_rate": snh_rate,
184	        "ISR_star": run.get("isr_star"),
185	    }
186	
187	
188	def build_table(runs: list[dict]) -> pd.DataFrame:
189	    rows = [compute_row(r) for r in runs]
190	    df = pd.DataFrame(rows)
191	    df = df.sort_values(["condition", "seed"]).reset_index(drop=True)
192	    return df
193	
194	
195	# --- Statistical tests ---
196	
197	def fisher_h7_domination(df: pd.DataFrame) -> dict:
198	    results = {}
199	    for cond in ["ISR", "RANDOM"]:
200	        sub = df[df["condition"] == cond]
201	        results[cond] = {
202	            "n": len(sub),
203	            "h7_dom": int((sub["H7_rate"] >= 0.5).sum()),
204	            "not_h7_dom": int((sub["H7_rate"] < 0.5).sum()),
205	        }
206	    table = np.array([
207	        [results["ISR"]["h7_dom"], results["ISR"]["not_h7_dom"]],
208	        [results["RANDOM"]["h7_dom"], results["RANDOM"]["not_h7_dom"]],
209	    ])
210	    odds_ratio, p_value = stats.fisher_exact(table, alternative="greater")
211	
212	    # 95% exact CI via scipy.stats.contingency
213	    or_ci_lo, or_ci_hi = np.nan, np.nan
214	    try:
215	        ct = stats.contingency.odds_ratio(table)
216	        ci = ct.confidence_interval(confidence_level=0.95)
217	        or_ci_lo, or_ci_hi = ci.low, ci.high
218	    except Exception:
219	        pass
220	
221	    return {
222	        "table": table.tolist(),
223	        "ISR": results["ISR"],
224	        "RANDOM": results["RANDOM"],
225	        "odds_ratio": odds_ratio,
226	        "or_ci_lo": or_ci_lo,
227	        "or_ci_hi": or_ci_hi,
228	        "p_value": p_value,
229	    }
230	
231	
232	def permutation_test_genuine(df: pd.DataFrame, n_perm: int = 10000,
233	                              rng_seed: int = 42) -> dict:
234	    isr = df[df["condition"] == "ISR"]["genuine_rate"].values
235	    rand = df[df["condition"] == "RANDOM"]["genuine_rate"].values
236	    observed = isr.mean() - rand.mean()
237	    pooled = np.concatenate([isr, rand])
238	    n_isr = len(isr)
239	    rng = np.random.default_rng(rng_seed)
240	    count = 0
241	    for _ in range(n_perm):
242	        perm = rng.permutation(pooled)
243	        if perm[:n_isr].mean() - perm[n_isr:].mean() >= observed:
244	            count += 1
245	    return {
246	        "observed_diff": float(observed),
247	        "p_value": count / n_perm,
248	        "n_perm": n_perm,
249	        "isr_mean": float(isr.mean()),
250	        "random_mean": float(rand.mean()),
251	    }
252	
253	
254	def mannwhitney_h7(df: pd.DataFrame) -> dict:
255	    isr = df[df["condition"] == "ISR"]["H7_rate"].values
256	    rand = df[df["condition"] == "RANDOM"]["H7_rate"].values
257	    n1, n2 = len(isr), len(rand)
258	    u_stat, p_value = stats.mannwhitneyu(isr, rand, alternative="greater")
259	    r_rb = 2.0 * u_stat / (n1 * n2) - 1.0 if n1 * n2 > 0 else np.nan
260	    return {
261	        "U": float(u_stat),
262	        "p_value": float(p_value),
263	        "r_rank_biserial": float(r_rb),
264	        "isr_median": float(np.median(isr)),
265	        "random_median": float(np.median(rand)),
266	    }
267	
268	
269	def mannwhitney_isr_star(df: pd.DataFrame) -> dict | None:
270	    isr = df[df["condition"] == "ISR"]["ISR_star"].dropna().values.astype(float)
271	    rand = df[df["condition"] == "RANDOM"]["ISR_star"].dropna().values.astype(float)
272	    if len(isr) < 2 or len(rand) < 2:
273	        return None
274	    n1, n2 = len(isr), len(rand)
275	    u_stat, p_value = stats.mannwhitneyu(isr, rand, alternative="greater")
276	    r_rb = 2.0 * u_stat / (n1 * n2) - 1.0
277	    return {
278	        "U": float(u_stat),
279	        "p_value": float(p_value),
280	        "r_rank_biserial": float(r_rb),
281	        "isr_median": float(np.median(isr)),
282	        "random_median": float(np.median(rand)),
283	        "isr_mean": float(np.mean(isr)),
284	        "random_mean": float(np.mean(rand)),
285	    }
286	
287	
288	def bca_bootstrap_ci(df: pd.DataFrame, metric: str, n_boot: int = 10000,
289	                      rng_seed: int = 42) -> dict:
290	    """BCa 95% CI for per-condition means of a metric."""
291	    result = {}
292	    for cond in ["ISR", "RANDOM"]:
293	        vals = df[df["condition"] == cond][metric].values
294	        if len(vals) < 2:
295	            result[cond] = {"mean": float(vals.mean()) if len(vals) else np.nan,
296	                            "ci_lo": np.nan, "ci_hi": np.nan}
297	            continue
298	        res = stats.bootstrap(
299	            (vals,), np.mean, n_resamples=n_boot,
300	            confidence_level=0.95, method="BCa",
301	            random_state=np.random.default_rng(rng_seed),
302	        )
303	        result[cond] = {
304	            "mean": float(vals.mean()),
305	            "ci_lo": float(res.confidence_interval.low),
306	            "ci_hi": float(res.confidence_interval.high),
307	        }
308	    return result
309	
310	
311	def bayes_factor_h7_domination(df: pd.DataFrame) -> dict:
312	    """BF10 for H7-domination rate difference (beta-binomial conjugate).
313	    H0: ISR and Random share same domination rate.
314	    H1: independent rates. Prior: Beta(1,1) on each.
315	    """
316	    isr_sub = df[df["condition"] == "ISR"]
317	    rand_sub = df[df["condition"] == "RANDOM"]
318	    k_isr = int((isr_sub["H7_rate"] >= 0.5).sum())
319	    n_isr = len(isr_sub)
320	    k_rand = int((rand_sub["H7_rate"] >= 0.5).sum())
321	    n_rand = len(rand_sub)
322	    k_total = k_isr + k_rand
323	    n_total = n_isr + n_rand
324	
325	    # log marginal under H0 (shared rate)
326	    log_m_h0 = betaln(1 + k_total, 1 + n_total - k_total) - betaln(1, 1)
327	    # log marginal under H1 (independent rates)
328	    log_m_h1 = (betaln(1 + k_isr, 1 + n_isr - k_isr) - betaln(1, 1)
329	                + betaln(1 + k_rand, 1 + n_rand - k_rand) - betaln(1, 1))
330	    log_bf10 = log_m_h1 - log_m_h0
331	    bf10 = float(np.exp(log_bf10))
332	
333	    return {
334	        "k_isr": k_isr, "n_isr": n_isr,
335	        "k_rand": k_rand, "n_rand": n_rand,
336	        "bf10": bf10,
337	        "log_bf10": float(log_bf10),
338	        "interpretation": _interpret_bf(bf10),
339	    }
340	
341	
342	def _interpret_bf(bf: float) -> str:
343	    if bf > 100:
344	        return "extreme evidence for H1"
345	    if bf > 30:
346	        return "very strong evidence for H1"
347	    if bf > 10:
348	        return "strong evidence for H1"
349	    if bf > 3:
350	        return "moderate evidence for H1"
351	    if bf > 1:
352	        return "anecdotal evidence for H1"
353	    if bf > 1/3:
354	        return "anecdotal evidence (inconclusive)"
355	    if bf > 1/10:
356	        return "moderate evidence for H0"
357	    return "strong evidence for H0"
358	
359	
360	def condition_stats(df: pd.DataFrame) -> pd.DataFrame:
361	    metrics = ["PR", "H7_rate", "genuine_rate", "SNH_rate"]
362	    rows = []
363	    for cond in ["ISR", "RANDOM"]:
364	        sub = df[df["condition"] == cond]
365	        row = {"condition": cond, "n_seeds": len(sub)}
366	        for m in metrics:
367	            vals = sub[m].values
368	            row[f"{m}_mean"] = vals.mean()
369	            row[f"{m}_std"] = vals.std(ddof=1) if len(vals) > 1 else 0.0
370	        isr_vals = sub["ISR_star"].dropna().values.astype(float)
371	        row["ISR_star_mean"] = isr_vals.mean() if len(isr_vals) else np.nan
372	        row["ISR_star_std"] = isr_vals.std(ddof=1) if len(isr_vals) > 1 else 0.0
373	        rows.append(row)
374	    return pd.DataFrame(rows)
375	
376	
377	# --- Formatting ---
378	
379	def fmt_pct(val: float) -> str:
380	    return f"{val*100:.1f}\\%"
381	
382	def fmt_or(val: float) -> str:
383	    return "$\\infty$" if np.isinf(val) else f"{val:.2f}"
384	
385	def fmt_ci(lo: float, hi: float) -> str:
386	    lo_s = f"{lo:.2f}" if not np.isnan(lo) else "0"
387	    hi_s = "$\\infty$" if np.isinf(hi) or np.isnan(hi) else f"{hi:.2f}"
388	    return f"[{lo_s}, {hi_s}]"
389	
390	def fmt_p(p: float) -> str:
391	    if p < 0.001:
392	        return "$<$0.001"
393	    return f"{p:.3f}"
394	
395	def fmt_mean_std(mean: float, std: float, pct: bool = False) -> str:
396	    if pct:
397	        return f"{mean*100:.1f} $\\pm$ {std*100:.1f}\\%"
398	    return f"{mean:.1f} $\\pm$ {std:.1f}"
399	
400	def fmt_bca(bca: dict, pct: bool = False) -> str:
401	    m = bca["mean"]
402	    lo, hi = bca["ci_lo"], bca["ci_hi"]
403	    if pct:
404	        return f"{m*100:.1f}\\% [{lo*100:.1f}, {hi*100:.1f}]"
405	    return f"{m:.1f} [{lo:.1f}, {hi:.1f}]"
406	
407	
408	# --- Console output ---
409	
410	def print_per_seed_table(df: pd.DataFrame):
411	    print("\n" + "=" * 90)
412	    print("  PER-SEED RESULTS")
413	    print("=" * 90)
414	    cols = ["condition", "seed", "PR", "H7_count", "H7_rate", "H1_count",
415	            "H8_count", "genuine_count", "genuine_rate", "CI_count", "SNH_count", "SNH_rate",
416	            "ISR_star"]
417	    fmt = df[cols].copy()
418	    for c in ["H7_rate", "genuine_rate", "SNH_rate"]:
419	        fmt[c] = fmt[c].apply(lambda v: f"{v*100:.1f}%")
420	    fmt["ISR_star"] = fmt["ISR_star"].apply(lambda v: f"{v:.4f}" if pd.notna(v) else "---")
421	    print(fmt.to_string(index=False))
422	
423	
424	def print_condition_stats(cond_df: pd.DataFrame):
425	    print("\n" + "=" * 90)
426	    print("  CONDITION-LEVEL STATISTICS (mean +/- SD)")
427	    print("=" * 90)
428	    for _, row in cond_df.iterrows():
429	        n = int(row['n_seeds'])
430	        print(f"\n  {row['condition']} (n={n} seeds):")
431	        print(f"    PR:           {row['PR_mean']:.1f} +/- {row['PR_std']:.1f}")
432	        print(f"    H7 rate:      {row['H7_rate_mean']*100:.1f} +/- {row['H7_rate_std']*100:.1f}%")
433	        print(f"    Genuine rate: {row['genuine_rate_mean']*100:.1f} +/- {row['genuine_rate_std']*100:.1f}%")
434	        print(f"    S-NH rate:    {row['SNH_rate_mean']*100:.1f} +/- {row['SNH_rate_std']*100:.1f}%")
435	        if not np.isnan(row.get('ISR_star_mean', np.nan)):
436	            print(f"    ISR*:         {row['ISR_star_mean']:.4f} +/- {row['ISR_star_std']:.4f}")
437	
438	
439	def print_tests(fisher, perm, mw, bf, bca_h7, bca_gen, mw_isr_star=None):
440	    print("\n" + "=" * 90)
441	    print("  STATISTICAL TESTS")
442	    print("=" * 90)
443	
444	    print("\n  1. H7 Domination Fisher Exact Test (H7-dominated = H7% >= 50%)")
445	    print(f"     ISR:    {fisher['ISR']['h7_dom']} dominated / {fisher['ISR']['n']} seeds")
446	    print(f"     RANDOM: {fisher['RANDOM']['h7_dom']} dominated / {fisher['RANDOM']['n']} seeds")
447	    print(f"     Contingency: {fisher['table']}")
448	    or_str = "inf" if np.isinf(fisher['odds_ratio']) else f"{fisher['odds_ratio']:.4f}"
449	    print(f"     OR = {or_str}, 95% CI = [{fisher['or_ci_lo']:.4f}, {fisher['or_ci_hi']:.4f}]"
450	          if not np.isnan(fisher['or_ci_lo']) else f"     OR = {or_str}, 95% CI = N/A")
451	    print(f"     p-value (one-sided, greater): {fisher['p_value']:.4f}")
452	
453	    print(f"\n  2. Genuine Rate Permutation Test (n_perm={perm['n_perm']})")
454	    print(f"     ISR mean:    {perm['isr_mean']*100:.2f}%")
455	    print(f"     RANDOM mean: {perm['random_mean']*100:.2f}%")
456	    print(f"     Diff: {perm['observed_diff']*100:.2f} pp, p = {perm['p_value']:.4f}")
457	
458	    print(f"\n  3. H7 Rate Mann-Whitney U Test")
459	    print(f"     ISR median:    {mw['isr_median']*100:.1f}%")
460	    print(f"     RANDOM median: {mw['random_median']*100:.1f}%")
461	    print(f"     U = {mw['U']:.1f}, p = {mw['p_value']:.4f}")
462	    print(f"     Rank-biserial r = {mw['r_rank_biserial']:.4f}")
463	
464	    print(f"\n  4. Bayes Factor (H7 Domination, Beta-Binomial)")
465	    print(f"     ISR:    {bf['k_isr']}/{bf['n_isr']} dominated")
466	    print(f"     RANDOM: {bf['k_rand']}/{bf['n_rand']} dominated")
467	    print(f"     BF10 = {bf['bf10']:.4f} ({bf['interpretation']})")
468	
469	    print(f"\n  5. BCa Bootstrap 95% CI (n_boot resamples)")
470	    for label, bca in [("H7 rate", bca_h7), ("Genuine rate", bca_gen)]:
471	        print(f"     {label}:")
472	        for cond in ["ISR", "RANDOM"]:
473	            b = bca[cond]
474	            print(f"       {cond}: {b['mean']*100:.1f}% [{b['ci_lo']*100:.1f}, {b['ci_hi']*100:.1f}]"
475	                  if not np.isnan(b['ci_lo']) else f"       {cond}: {b['mean']*100:.1f}% [N/A]")
476	
477	    if mw_isr_star:
478	        print(f"\n  6. ISR* (Proved-Only Mean ISR) Mann-Whitney U Test")
479	        print(f"     ISR mean:    {mw_isr_star['isr_mean']:.4f}, median: {mw_isr_star['isr_median']:.4f}")
480	        print(f"     RANDOM mean: {mw_isr_star['random_mean']:.4f}, median: {mw_isr_star['random_median']:.4f}")
481	        print(f"     U = {mw_isr_star['U']:.1f}, p = {mw_isr_star['p_value']:.4f}")
482	        print(f"     Rank-biserial r = {mw_isr_star['r_rank_biserial']:.4f}")
483	
484	
485	# --- Markdown generation (appendix-ready) ---
486	
487	def generate_markdown(df: pd.DataFrame, cond_df: pd.DataFrame,
488	                      fisher: dict, perm: dict, mw: dict,
489	                      bf: dict, bca_h7: dict, bca_gen: dict,
490	                      mw_isr_star: dict = None) -> str:
491	    L = []
492	    L.append("## D134: ISR vs Random Statistical Analysis\n")
493	
494	    # Per-seed table
495	    L.append("### Table A1: Per-Seed Hacking Taxonomy (4B Qwen3, 500 steps)\n")
496	    L.append("| Condition | Seed | PR | H7 | H7\\% | H1 | H8 | Genuine | Gen\\% | CI | S-NH | S-NH\\% | ISR* |")
497	    L.append("|:----------|-----:|---:|---:|-----:|---:|---:|--------:|------:|---:|-----:|-------:|-----:|")
498	    for _, r in df.iterrows():
499	        isr_star_str = f"{r['ISR_star']:.4f}" if pd.notna(r.get('ISR_star')) else "---"
500	        L.append(
501	            f"| {r['condition']} | {r['seed']} | {int(r['PR'])} | {int(r['H7_count'])} | "
502	            f"{r['H7_rate']*100:.1f} | {int(r['H1_count'])} | {int(r['H8_count'])} | "
503	            f"{int(r['genuine_count'])} | {r['genuine_rate']*100:.1f} | {int(r['CI_count'])} | "
504	            f"{int(r['SNH_count'])} | {r['SNH_rate']*100:.1f} | {isr_star_str} |"
505	        )
506	
507	    # Condition summary with BCa CI
508	    L.append("\n### Table A2: Condition-Level Summary\n")
509	    L.append("| Condition | $n$ | PR (mean$\\pm$SD) | H7\\% (mean$\\pm$SD) | H7\\% BCa 95\\% CI | Gen\\% (mean$\\pm$SD) | Gen\\% BCa 95\\% CI |")
510	    L.append("|:----------|----:|:------------------|:-------------------|:-----------------|:-------------------|:-----------------|")
511	    for _, r in cond_df.iterrows():
512	        cond = r["condition"]
513	        h7_bca = bca_h7.get(cond, {})
514	        gen_bca = bca_gen.get(cond, {})
515	        h7_ci = f"[{h7_bca['ci_lo']*100:.1f}, {h7_bca['ci_hi']*100:.1f}]" if h7_bca and not np.isnan(h7_bca.get('ci_lo', np.nan)) else "N/A"
516	        gen_ci = f"[{gen_bca['ci_lo']*100:.1f}, {gen_bca['ci_hi']*100:.1f}]" if gen_bca and not np.isnan(gen_bca.get('ci_lo', np.nan)) else "N/A"
517	        L.append(
518	            f"| {cond} | {int(r['n_seeds'])} | "
519	            f"{r['PR_mean']:.1f}$\\pm${r['PR_std']:.1f} | "
520	            f"{r['H7_rate_mean']*100:.1f}$\\pm${r['H7_rate_std']*100:.1f} | "
521	            f"{h7_ci} | "
522	            f"{r['genuine_rate_mean']*100:.1f}$\\pm${r['genuine_rate_std']*100:.1f} | "
523	            f"{gen_ci} |"
524	        )
525	
526	    # Statistical tests
527	    if fisher and perm and mw and bf:
528	        L.append("\n### Statistical Tests\n")
529	
530	        # Fisher
531	        or_str = "$\\infty$" if np.isinf(fisher['odds_ratio']) else f"{fisher['odds_ratio']:.2f}"
532	        ci_lo = f"{fisher['or_ci_lo']:.2f}" if not np.isnan(fisher['or_ci_lo']) else "0"
533	        ci_hi = "$\\infty$" if np.isinf(fisher.get('or_ci_hi', np.inf)) or np.isnan(fisher.get('or_ci_hi', np.nan)) else f"{fisher['or_ci_hi']:.2f}"
534	        L.append("**1. H7 Domination Fisher Exact Test** (threshold: H7$\\geq$50\\% of proved)")
535	        L.append(f"- ISR: {fisher['ISR']['h7_dom']}/{fisher['ISR']['n']} seeds H7-dominated; "
536	                 f"Random: {fisher['RANDOM']['h7_dom']}/{fisher['RANDOM']['n']}")
537	        L.append(f"- OR = {or_str}, 95\\% exact CI = [{ci_lo}, {ci_hi}], "
538	                 f"$p$ = {fmt_p(fisher['p_value'])}")
539	        L.append("")
540	
541	        # Permutation
542	        L.append(f"**2. Genuine Rate Permutation Test** ($n$ = {perm['n_perm']:,} permutations)")
543	        L.append(f"- ISR mean: {perm['isr_mean']*100:.2f}\\%, Random mean: {perm['random_mean']*100:.2f}\\%")
544	        L.append(f"- $\\Delta$ = {perm['observed_diff']*100:.2f} pp, $p$ = {fmt_p(perm['p_value'])}")
545	        L.append("")
546	
547	        # Mann-Whitney
548	        L.append("**3. H7 Rate Mann-Whitney $U$ Test**")
549	        L.append(f"- ISR median: {mw['isr_median']*100:.1f}\\%, Random median: {mw['random_median']*100:.1f}\\%")
550	        L.append(f"- $U$ = {mw['U']:.1f}, $p$ = {fmt_p(mw['p_value'])}, "
551	                 f"rank-biserial $r$ = {mw['r_rank_biserial']:.3f}")
552	        L.append("")
553	
554	        # Bayes Factor
555	        L.append("**4. Bayes Factor** (Beta-Binomial conjugate, prior: Beta(1,1))")
556	        L.append(f"- $BF_{{10}}$ = {bf['bf10']:.2f} ({bf['interpretation']})")
557	        L.append(f"- ISR: {bf['k_isr']}/{bf['n_isr']} H7-dominated, "
558	                 f"Random: {bf['k_rand']}/{bf['n_rand']}")
559	
560	        if mw_isr_star:
561	            L.append("")
562	            L.append("**5. ISR* (Proved-Only Mean ISR) Mann-Whitney $U$ Test**")
563	            L.append(f"- ISR mean: {mw_isr_star['isr_mean']:.4f}, median: {mw_isr_star['isr_median']:.4f}")
564	            L.append(f"- Random mean: {mw_isr_star['random_mean']:.4f}, median: {mw_isr_star['random_median']:.4f}")
565	            L.append(f"- $U$ = {mw_isr_star['U']:.1f}, $p$ = {fmt_p(mw_isr_star['p_value'])}, "
566	                     f"rank-biserial $r$ = {mw_isr_star['r_rank_biserial']:.3f}")
567	
568	    return "\n".join(L) + "\n"
569	
570	
571	# --- Main ---
572	
573	def main():
574	    args = parse_args()
575	    data_dir = Path(args.data_dir)
576	
577	    if not data_dir.exists():
578	        print(f"ERROR: data directory {data_dir} does not exist", file=sys.stderr)
579	        sys.exit(1)
580	
581	    if args.prefix:
582	        prefixes = [args.prefix]
583	    elif args.prefixes:
584	        prefixes = [p.strip() for p in args.prefixes.split(",")]
585	    else:
586	        prefixes = MODE_PREFIXES[args.mode]
587	    print(f"Mode: {args.mode} | Prefixes: {prefixes}")
588	
589	    runs = discover_runs(data_dir, prefixes)
590	    if not runs:
591	        print(f"ERROR: no runs found in {data_dir} with prefixes {prefixes}", file=sys.stderr)
592	        sys.exit(1)
593	
594	    isr_count = sum(1 for r in runs if r["condition"] == "ISR")
595	    rand_count = sum(1 for r in runs if r["condition"] == "RANDOM")
596	    print(f"Found {len(runs)} runs: {isr_count} ISR, {rand_count} RANDOM")
597	    for r in runs:
598	        print(f"  {r['condition']:6s} s{r['seed']} <- {r['dir_name']}")
599	
600	    df = build_table(runs)
601	    print_per_seed_table(df)
602	
603	    cond_df = condition_stats(df)
604	    print_condition_stats(cond_df)
605	
606	    if isr_count < 2 or rand_count < 2:
607	        print("\nWARNING: need >= 2 seeds per condition for statistical tests, skipping.",
608	              file=sys.stderr)
609	        bca_h7 = bca_bootstrap_ci(df, "H7_rate", args.n_boot, args.seed)
610	        bca_gen = bca_bootstrap_ci(df, "genuine_rate", args.n_boot, args.seed)
611	        if args.output:
612	            md = generate_markdown(df, cond_df, {}, {}, {}, {}, bca_h7, bca_gen)
613	            Path(args.output).write_text(md)
614	            print(f"\nMarkdown written to {args.output}")
615	        return
616	
617	    fisher = fisher_h7_domination(df)
618	    perm = permutation_test_genuine(df, n_perm=args.n_perm, rng_seed=args.seed)
619	    mw = mannwhitney_h7(df)
620	    bf = bayes_factor_h7_domination(df)
621	    bca_h7 = bca_bootstrap_ci(df, "H7_rate", args.n_boot, args.seed)
622	    bca_gen = bca_bootstrap_ci(df, "genuine_rate", args.n_boot, args.seed)
623	    mw_isr_star = mannwhitney_isr_star(df)
624	
625	    print_tests(fisher, perm, mw, bf, bca_h7, bca_gen, mw_isr_star)
626	
627	    md = generate_markdown(df, cond_df, fisher, perm, mw, bf, bca_h7, bca_gen, mw_isr_star)
628	    print("\n" + "=" * 90)
629	    print("  MARKDOWN OUTPUT (appendix-ready)")
630	    print("=" * 90)
631	    print(md)
632	
633	    if args.output:
634	        Path(args.output).parent.mkdir(parents=True, exist_ok=True)
635	        Path(args.output).write_text(md)
636	        print(f"Markdown written to {args.output}")
637	
638	
639	if __name__ == "__main__":
640	    main()
641	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "99702f0a-70ff-405f-b5d0-78f13e735cfe",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/scripts/d134_analysis.py",
      "content": "#!/usr/bin/env python3\n\"\"\"D134 experiment analysis: multi-seed ISR vs Random, 4B GRPO training.\nReads taxonomy data from classify.json, taxonomy.json, or top-level taxonomy files.\nComputes summary stats, statistical tests (Fisher, Mann-Whitney, permutation, Bayes Factor),\nand BCa bootstrap CIs. Outputs appendix-ready markdown.\n\"\"\"\n\nimport argparse\nimport json\nimport re\nimport sys\nfrom pathlib import Path\n\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\nfrom scipy.special import betaln\n\nCONDITION_MAP = [\n    (\"d134_4b_isr\", \"ISR\"),\n    (\"d134_4b_random\", \"RANDOM\"),\n    (\"plan002_additive\", \"ISR\"),\n    (\"plan018_additive_random\", \"RANDOM\"),\n    (\"plan018_random\", \"RANDOM\"),\n]\n\nMODE_PREFIXES = {\n    \"d134_only\": [\"d134_4b\"],\n    \"all\": [\"d134_4b\", \"plan002_additive_b01\", \"plan018_additive_random_b01\", \"plan018_random\"],\n}\n\n\ndef parse_args():\n    p = argparse.ArgumentParser(description=\"D134 multi-seed analysis and statistical tests\")\n    p.add_argument(\"--data_dir\", type=str, default=\"/root/autodl-tmp/outputs\",\n                   help=\"Directory containing experiment outputs\")\n    p.add_argument(\"--mode\", type=str, default=\"d134_only\", choices=list(MODE_PREFIXES),\n                   help=\"d134_only = matched 5+5 design (default); all = include original seeds\")\n    p.add_argument(\"--prefix\", type=str, default=None,\n                   help=\"(Legacy) Single prefix filter; overrides mode/prefixes\")\n    p.add_argument(\"--prefixes\", type=str, default=None,\n                   help=\"Comma-separated prefixes; overrides --mode\")\n    p.add_argument(\"--output\", type=str, default=None,\n                   help=\"Write markdown summary to this file\")\n    p.add_argument(\"--n_perm\", type=int, default=10000,\n                   help=\"Number of permutations for permutation test\")\n    p.add_argument(\"--n_boot\", type=int, default=10000,\n                   help=\"Number of bootstrap resamples for BCa CI\")\n    p.add_argument(\"--seed\", type=int, default=42,\n                   help=\"Random seed for permutation/bootstrap\")\n    return p.parse_args()\n\n\n# --- Data loading ---\n\ndef match_condition(name: str) -> str | None:\n    best_prefix = \"\"\n    best_cond = None\n    for prefix, cond in CONDITION_MAP:\n        if name.startswith(prefix) and len(prefix) > len(best_prefix):\n            best_prefix = prefix\n            best_cond = cond\n    return best_cond\n\n\ndef extract_seed(name: str) -> int | None:\n    m = re.search(r'_s(\\d+)', name)\n    return int(m.group(1)) if m else None\n\n\ndef load_eval_results(path: Path) -> dict | None:\n    if not path.exists():\n        return None\n    with open(path) as f:\n        data = json.load(f)\n    if \"eval_results\" in data:\n        return data[\"eval_results\"]\n    return data\n\n\ndef load_taxonomy_unified(path: Path) -> dict | None:\n    with open(path) as f:\n        raw = json.load(f)\n    t = raw.get(\"taxonomy\", {})\n    proved = t.get(\"proved\", 0)\n    if proved == 0:\n        return None\n    h7 = t.get(\"H7\", 0)\n    h1 = t.get(\"H1_exact\", 0)\n    h8 = t.get(\"H8\", 0)\n    genuine = t.get(\"genuine\", 0)\n    return {\n        \"n_total\": 100, \"n_proved\": proved,\n        \"h7_total_count\": h7, \"h7_total_rate\": h7 / proved,\n        \"h1_strict_count\": h1, \"h8_conjunction_collapse_count\": h8,\n        \"genuine_count\": genuine, \"genuine_rate\": genuine / proved,\n        \"content_independent_count\": 0,\n    }\n\n\ndef load_taxonomy_verification(path: Path) -> dict | None:\n    with open(path) as f:\n        raw = json.load(f)\n    proved = raw.get(\"proved\", 0)\n    if proved == 0:\n        return None\n    tax = raw.get(\"taxonomy\", {})\n    h7 = tax.get(\"h7\", {}).get(\"count\", 0)\n    h1 = tax.get(\"h1_exact\", {}).get(\"count\", 0)\n    h8 = tax.get(\"h8\", {}).get(\"count\", 0)\n    genuine = tax.get(\"genuine\", {}).get(\"count\", 0)\n    return {\n        \"n_total\": raw.get(\"total\", 100), \"n_proved\": proved,\n        \"h7_total_count\": h7, \"h7_total_rate\": h7 / proved,\n        \"h1_strict_count\": h1, \"h8_conjunction_collapse_count\": h8,\n        \"genuine_count\": genuine, \"genuine_rate\": genuine / proved,\n        \"content_independent_count\": 0,\n    }\n\n\ndef discover_runs(data_dir: Path, prefixes: list[str]) -> list[dict]:\n    runs = []\n    seen = set()\n    for entry in sorted(data_dir.iterdir()):\n        name = entry.name\n        if not any(name.startswith(p) for p in prefixes):\n            continue\n        cond = match_condition(name)\n        seed_val = extract_seed(name)\n        if cond is None or seed_val is None:\n            continue\n        key = (cond, seed_val)\n        if key in seen:\n            continue\n        data = None\n        if entry.is_dir():\n            for fname in [\"classify.json\", \"taxonomy.json\"]:\n                data = load_eval_results(entry / fname)\n                if data is not None:\n                    break\n            if data is None:\n                continue\n        elif entry.is_file():\n            if name.endswith(\"_taxonomy_unified.json\"):\n                data = load_taxonomy_unified(entry)\n            elif name.endswith(\"_taxonomy_verification.json\"):\n                data = load_taxonomy_verification(entry)\n            if data is None:\n                continue\n        else:\n            continue\n        seen.add(key)\n        isr_star = None\n        if entry.is_dir():\n            eval_path = entry / \"eval_results.json\"\n            if eval_path.exists():\n                with open(eval_path) as ef:\n                    eval_raw = json.load(ef)\n                isr_star = eval_raw.get(\"summary\", {}).get(\"proved_only_mean_isr\")\n        runs.append({\"dir_name\": name, \"seed\": seed_val, \"condition\": cond,\n                      \"data\": data, \"isr_star\": isr_star})\n    return runs\n\n\ndef compute_row(run: dict) -> dict:\n    d = run[\"data\"]\n    n_proved = d.get(\"n_proved\", 0)\n    n_total = d.get(\"n_total\", 100)\n    h7 = d.get(\"h7_total_count\", 0)\n    h7_rate = d.get(\"h7_total_rate\", h7 / n_proved if n_proved > 0 else 0.0)\n    h1 = d.get(\"h1_strict_count\", 0)\n    h8 = d.get(\"h8_conjunction_collapse_count\", 0)\n    genuine = d.get(\"genuine_count\", 0)\n    genuine_rate = d.get(\"genuine_rate\", genuine / n_proved if n_proved > 0 else 0.0)\n    ci = d.get(\"content_independent_count\", 0)\n    snh = max(genuine - ci, 0)\n    snh_rate = snh / n_proved if n_proved > 0 else 0.0\n    return {\n        \"seed\": run[\"seed\"], \"condition\": run[\"condition\"], \"n_total\": n_total,\n        \"PR\": n_proved, \"H7_count\": h7, \"H7_rate\": h7_rate,\n        \"H1_count\": h1, \"H8_count\": h8,\n        \"genuine_count\": genuine, \"genuine_rate\": genuine_rate,\n        \"CI_count\": ci, \"SNH_count\": snh, \"SNH_rate\": snh_rate,\n        \"ISR_star\": run.get(\"isr_star\"),\n    }\n\n\ndef build_table(runs: list[dict]) -> pd.DataFrame:\n    rows = [compute_row(r) for r in runs]\n    df = pd.DataFrame(rows)\n    df = df.sort_values([\"condition\", \"seed\"]).reset_index(drop=True)\n    return df\n\n\n# --- Statistical tests ---\n\ndef fisher_h7_domination(df: pd.DataFrame) -> dict:\n    results = {}\n    for cond in [\"ISR\", \"RANDOM\"]:\n        sub = df[df[\"condition\"] == cond]\n        results[cond] = {\n            \"n\": len(sub),\n            \"h7_dom\": int((sub[\"H7_rate\"] >= 0.5).sum()),\n            \"not_h7_dom\": int((sub[\"H7_rate\"] < 0.5).sum()),\n        }\n    table = np.array([\n        [results[\"ISR\"][\"h7_dom\"], results[\"ISR\"][\"not_h7_dom\"]],\n        [results[\"RANDOM\"][\"h7_dom\"], results[\"RANDOM\"][\"not_h7_dom\"]],\n    ])\n    odds_ratio, p_value = stats.fisher_exact(table, alternative=\"greater\")\n\n    # 95% exact CI via scipy.stats.contingency\n    or_ci_lo, or_ci_hi = np.nan, np.nan\n    try:\n        ct = stats.contingency.odds_ratio(table)\n        ci = ct.confidence_interval(confidence_level=0.95)\n        or_ci_lo, or_ci_hi = ci.low, ci.high\n    except Exception:\n        pass\n\n    return {\n        \"table\": table.tolist(),\n        \"ISR\": results[\"ISR\"],\n        \"RANDOM\": results[\"RANDOM\"],\n        \"odds_ratio\": odds_ratio,\n        \"or_ci_lo\": or_ci_lo,\n        \"or_ci_hi\": or_ci_hi,\n        \"p_value\": p_value,\n    }\n\n\ndef permutation_test_genuine(df: pd.DataFrame, n_perm: int = 10000,\n                              rng_seed: int = 42) -> dict:\n    isr = df[df[\"condition\"] == \"ISR\"][\"genuine_rate\"].values\n    rand = df[df[\"condition\"] == \"RANDOM\"][\"genuine_rate\"].values\n    observed = isr.mean() - rand.mean()\n    pooled = np.concatenate([isr, rand])\n    n_isr = len(isr)\n    rng = np.random.default_rng(rng_seed)\n    count = 0\n    for _ in range(n_perm):\n        perm = rng.permutation(pooled)\n        if perm[:n_isr].mean() - perm[n_isr:].mean() >= observed:\n            count += 1\n    return {\n        \"observed_diff\": float(observed),\n        \"p_value\": count / n_perm,\n        \"n_perm\": n_perm,\n        \"isr_mean\": float(isr.mean()),\n        \"random_mean\": float(rand.mean()),\n    }\n\n\ndef mannwhitney_h7(df: pd.DataFrame) -> dict:\n    isr = df[df[\"condition\"] == \"ISR\"][\"H7_rate\"].values\n    rand = df[df[\"condition\"] == \"RANDOM\"][\"H7_rate\"].values\n    n1, n2 = len(isr), len(rand)\n    u_stat, p_value = stats.mannwhitneyu(isr, rand, alternative=\"greater\")\n    r_rb = 2.0 * u_stat / (n1 * n2) - 1.0 if n1 * n2 > 0 else np.nan\n    return {\n        \"U\": float(u_stat),\n        \"p_value\": float(p_value),\n        \"r_rank_biserial\": float(r_rb),\n        \"isr_median\": float(np.median(isr)),\n        \"random_median\": float(np.median(rand)),\n    }\n\n\ndef mannwhitney_isr_star(df: pd.DataFrame) -> dict | None:\n    isr = df[df[\"condition\"] == \"ISR\"][\"ISR_star\"].dropna().values.astype(float)\n    rand = df[df[\"condition\"] == \"RANDOM\"][\"ISR_star\"].dropna().values.astype(float)\n    if len(isr) < 2 or len(rand) < 2:\n        return None\n    n1, n2 = len(isr), len(rand)\n    u_stat, p_value = stats.mannwhitneyu(isr, rand, alternative=\"greater\")\n    r_rb = 2.0 * u_stat / (n1 * n2) - 1.0\n    return {\n        \"U\": float(u_stat),\n        \"p_value\": float(p_value),\n        \"r_rank_biserial\": float(r_rb),\n        \"isr_median\": float(np.median(isr)),\n        \"random_median\": float(np.median(rand)),\n        \"isr_mean\": float(np.mean(isr)),\n        \"random_mean\": float(np.mean(rand)),\n    }\n\n\ndef bca_bootstrap_ci(df: pd.DataFrame, metric: str, n_boot: int = 10000,\n                      rng_seed: int = 42) -> dict:\n    \"\"\"BCa 95% CI for per-condition means of a metric.\"\"\"\n    result = {}\n    for cond in [\"ISR\", \"RANDOM\"]:\n        vals = df[df[\"condition\"] == cond][metric].values\n        if len(vals) < 2:\n            result[cond] = {\"mean\": float(vals.mean()) if len(vals) else np.nan,\n                            \"ci_lo\": np.nan, \"ci_hi\": np.nan}\n            continue\n        res = stats.bootstrap(\n            (vals,), np.mean, n_resamples=n_boot,\n            confidence_level=0.95, method=\"BCa\",\n            random_state=np.random.default_rng(rng_seed),\n        )\n        result[cond] = {\n            \"mean\": float(vals.mean()),\n            \"ci_lo\": float(res.confidence_interval.low),\n            \"ci_hi\": float(res.confidence_interval.high),\n        }\n    return result\n\n\ndef bayes_factor_h7_domination(df: pd.DataFrame) -> dict:\n    \"\"\"BF10 for H7-domination rate difference (beta-binomial conjugate).\n    H0: ISR and Random share same domination rate.\n    H1: independent rates. Prior: Beta(1,1) on each.\n    \"\"\"\n    isr_sub = df[df[\"condition\"] == \"ISR\"]\n    rand_sub = df[df[\"condition\"] == \"RANDOM\"]\n    k_isr = int((isr_sub[\"H7_rate\"] >= 0.5).sum())\n    n_isr = len(isr_sub)\n    k_rand = int((rand_sub[\"H7_rate\"] >= 0.5).sum())\n    n_rand = len(rand_sub)\n    k_total = k_isr + k_rand\n    n_total = n_isr + n_rand\n\n    # log marginal under H0 (shared rate)\n    log_m_h0 = betaln(1 + k_total, 1 + n_total - k_total) - betaln(1, 1)\n    # log marginal under H1 (independent rates)\n    log_m_h1 = (betaln(1 + k_isr, 1 + n_isr - k_isr) - betaln(1, 1)\n                + betaln(1 + k_rand, 1 + n_rand - k_rand) - betaln(1, 1))\n    log_bf10 = log_m_h1 - log_m_h0\n    bf10 = float(np.exp(log_bf10))\n\n    return {\n        \"k_isr\": k_isr, \"n_isr\": n_isr,\n        \"k_rand\": k_rand, \"n_rand\": n_rand,\n        \"bf10\": bf10,\n        \"log_bf10\": float(log_bf10),\n        \"interpretation\": _interpret_bf(bf10),\n    }\n\n\ndef _interpret_bf(bf: float) -> str:\n    if bf > 100:\n        return \"extreme evidence for H1\"\n    if bf > 30:\n        return \"very strong evidence for H1\"\n    if bf > 10:\n        return \"strong evidence for H1\"\n    if bf > 3:\n        return \"moderate evidence for H1\"\n    if bf > 1:\n        return \"anecdotal evidence for H1\"\n    if bf > 1/3:\n        return \"anecdotal evidence (inconclusive)\"\n    if bf > 1/10:\n        return \"moderate evidence for H0\"\n    return \"strong evidence for H0\"\n\n\ndef condition_stats(df: pd.DataFrame) -> pd.DataFrame:\n    metrics = [\"PR\", \"H7_rate\", \"genuine_rate\", \"SNH_rate\"]\n    rows = []\n    for cond in [\"ISR\", \"RANDOM\"]:\n        sub = df[df[\"condition\"] == cond]\n        row = {\"condition\": cond, \"n_seeds\": len(sub)}\n        for m in metrics:\n            vals = sub[m].values\n            row[f\"{m}_mean\"] = vals.mean()\n            row[f\"{m}_std\"] = vals.std(ddof=1) if len(vals) > 1 else 0.0\n        isr_vals = sub[\"ISR_star\"].dropna().values.astype(float)\n        row[\"ISR_star_mean\"] = isr_vals.mean() if len(isr_vals) else np.nan\n        row[\"ISR_star_std\"] = isr_vals.std(ddof=1) if len(isr_vals) > 1 else 0.0\n        rows.append(row)\n    return pd.DataFrame(rows)\n\n\n# --- Formatting ---\n\ndef fmt_pct(val: float) -> str:\n    return f\"{val*100:.1f}\\\\%\"\n\ndef fmt_or(val: float) -> str:\n    return \"$\\\\infty$\" if np.isinf(val) else f\"{val:.2f}\"\n\ndef fmt_ci(lo: float, hi: float) -> str:\n    lo_s = f\"{lo:.2f}\" if not np.isnan(lo) else \"0\"\n    hi_s = \"$\\\\infty$\" if np.isinf(hi) or np.isnan(hi) else f\"{hi:.2f}\"\n    return f\"[{lo_s}, {hi_s}]\"\n\ndef fmt_p(p: float) -> str:\n    if p < 0.001:\n        return \"$<$0.001\"\n    return f\"{p:.3f}\"\n\ndef fmt_mean_std(mean: float, std: float, pct: bool = False) -> str:\n    if pct:\n        return f\"{mean*100:.1f} $\\\\pm$ {std*100:.1f}\\\\%\"\n    return f\"{mean:.1f} $\\\\pm$ {std:.1f}\"\n\ndef fmt_bca(bca: dict, pct: bool = False) -> str:\n    m = bca[\"mean\"]\n    lo, hi = bca[\"ci_lo\"], bca[\"ci_hi\"]\n    if pct:\n        return f\"{m*100:.1f}\\\\% [{lo*100:.1f}, {hi*100:.1f}]\"\n    return f\"{m:.1f} [{lo:.1f}, {hi:.1f}]\"\n\n\n# --- Console output ---\n\ndef print_per_seed_table(df: pd.DataFrame):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  PER-SEED RESULTS\")\n    print(\"=\" * 90)\n    cols = [\"condition\", \"seed\", \"PR\", \"H7_count\", \"H7_rate\", \"H1_count\",\n            \"H8_count\", \"genuine_count\", \"genuine_rate\", \"CI_count\", \"SNH_count\", \"SNH_rate\",\n            \"ISR_star\"]\n    fmt = df[cols].copy()\n    for c in [\"H7_rate\", \"genuine_rate\", \"SNH_rate\"]:\n        fmt[c] = fmt[c].apply(lambda v: f\"{v*100:.1f}%\")\n    fmt[\"ISR_star\"] = fmt[\"ISR_star\"].apply(lambda v: f\"{v:.4f}\" if pd.notna(v) else \"---\")\n    print(fmt.to_string(index=False))\n\n\ndef print_condition_stats(cond_df: pd.DataFrame):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  CONDITION-LEVEL STATISTICS (mean +/- SD)\")\n    print(\"=\" * 90)\n    for _, row in cond_df.iterrows():\n        n = int(row['n_seeds'])\n        print(f\"\\n  {row['condition']} (n={n} seeds):\")\n        print(f\"    PR:           {row['PR_mean']:.1f} +/- {row['PR_std']:.1f}\")\n        print(f\"    H7 rate:      {row['H7_rate_mean']*100:.1f} +/- {row['H7_rate_std']*100:.1f}%\")\n        print(f\"    Genuine rate: {row['genuine_rate_mean']*100:.1f} +/- {row['genuine_rate_std']*100:.1f}%\")\n        print(f\"    S-NH rate:    {row['SNH_rate_mean']*100:.1f} +/- {row['SNH_rate_std']*100:.1f}%\")\n        if not np.isnan(row.get('ISR_star_mean', np.nan)):\n            print(f\"    ISR*:         {row['ISR_star_mean']:.4f} +/- {row['ISR_star_std']:.4f}\")\n\n\ndef print_tests(fisher, perm, mw, bf, bca_h7, bca_gen, mw_isr_star=None):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  STATISTICAL TESTS\")\n    print(\"=\" * 90)\n\n    print(\"\\n  1. H7 Domination Fisher Exact Test (H7-dominated = H7% >= 50%)\")\n    print(f\"     ISR:    {fisher['ISR']['h7_dom']} dominated / {fisher['ISR']['n']} seeds\")\n    print(f\"     RANDOM: {fisher['RANDOM']['h7_dom']} dominated / {fisher['RANDOM']['n']} seeds\")\n    print(f\"     Contingency: {fisher['table']}\")\n    or_str = \"inf\" if np.isinf(fisher['odds_ratio']) else f\"{fisher['odds_ratio']:.4f}\"\n    print(f\"     OR = {or_str}, 95% CI = [{fisher['or_ci_lo']:.4f}, {fisher['or_ci_hi']:.4f}]\"\n          if not np.isnan(fisher['or_ci_lo']) else f\"     OR = {or_str}, 95% CI = N/A\")\n    print(f\"     p-value (one-sided, greater): {fisher['p_value']:.4f}\")\n\n    print(f\"\\n  2. Genuine Rate Permutation Test (n_perm={perm['n_perm']})\")\n    print(f\"     ISR mean:    {perm['isr_mean']*100:.2f}%\")\n    print(f\"     RANDOM mean: {perm['random_mean']*100:.2f}%\")\n    print(f\"     Diff: {perm['observed_diff']*100:.2f} pp, p = {perm['p_value']:.4f}\")\n\n    print(f\"\\n  3. H7 Rate Mann-Whitney U Test\")\n    print(f\"     ISR median:    {mw['isr_median']*100:.1f}%\")\n    print(f\"     RANDOM median: {mw['random_median']*100:.1f}%\")\n    print(f\"     U = {mw['U']:.1f}, p = {mw['p_value']:.4f}\")\n    print(f\"     Rank-biserial r = {mw['r_rank_biserial']:.4f}\")\n\n    print(f\"\\n  4. Bayes Factor (H7 Domination, Beta-Binomial)\")\n    print(f\"     ISR:    {bf['k_isr']}/{bf['n_isr']} dominated\")\n    print(f\"     RANDOM: {bf['k_rand']}/{bf['n_rand']} dominated\")\n    print(f\"     BF10 = {bf['bf10']:.4f} ({bf['interpretation']})\")\n\n    print(f\"\\n  5. BCa Bootstrap 95% CI (n_boot resamples)\")\n    for label, bca in [(\"H7 rate\", bca_h7), (\"Genuine rate\", bca_gen)]:\n        print(f\"     {label}:\")\n        for cond in [\"ISR\", \"RANDOM\"]:\n            b = bca[cond]\n            print(f\"       {cond}: {b['mean']*100:.1f}% [{b['ci_lo']*100:.1f}, {b['ci_hi']*100:.1f}]\"\n                  if not np.isnan(b['ci_lo']) else f\"       {cond}: {b['mean']*100:.1f}% [N/A]\")\n\n    if mw_isr_star:\n        print(f\"\\n  6. ISR* (Proved-Only Mean ISR) Mann-Whitney U Test\")\n        print(f\"     ISR mean:    {mw_isr_star['isr_mean']:.4f}, median: {mw_isr_star['isr_median']:.4f}\")\n        print(f\"     RANDOM mean: {mw_isr_star['random_mean']:.4f}, median: {mw_isr_star['random_median']:.4f}\")\n        print(f\"     U = {mw_isr_star['U']:.1f}, p = {mw_isr_star['p_value']:.4f}\")\n        print(f\"     Rank-biserial r = {mw_isr_star['r_rank_biserial']:.4f}\")\n\n\n# --- Markdown generation (appendix-ready) ---\n\ndef generate_markdown(df: pd.DataFrame, cond_df: pd.DataFrame,\n                      fisher: dict, perm: dict, mw: dict,\n                      bf: dict, bca_h7: dict, bca_gen: dict,\n                      mw_isr_star: dict = None) -> str:\n    L = []\n    L.append(\"## D134: ISR vs Random Statistical Analysis\\n\")\n\n    # Per-seed table\n    L.append(\"### Table A1: Per-Seed Hacking Taxonomy (4B Qwen3, 500 steps)\\n\")\n    L.append(\"| Condition | Seed | PR | H7 | H7\\\\% | H1 | H8 | Genuine | Gen\\\\% | CI | S-NH | S-NH\\\\% | ISR* |\")\n    L.append(\"|:----------|-----:|---:|---:|-----:|---:|---:|--------:|------:|---:|-----:|-------:|-----:|\")\n    for _, r in df.iterrows():\n        isr_star_str = f\"{r['ISR_star']:.4f}\" if pd.notna(r.get('ISR_star')) else \"---\"\n        L.append(\n            f\"| {r['condition']} | {r['seed']} | {int(r['PR'])} | {int(r['H7_count'])} | \"\n            f\"{r['H7_rate']*100:.1f} | {int(r['H1_count'])} | {int(r['H8_count'])} | \"\n            f\"{int(r['genuine_count'])} | {r['genuine_rate']*100:.1f} | {int(r['CI_count'])} | \"\n            f\"{int(r['SNH_count'])} | {r['SNH_rate']*100:.1f} | {isr_star_str} |\"\n        )\n\n    # Condition summary with BCa CI\n    L.append(\"\\n### Table A2: Condition-Level Summary\\n\")\n    L.append(\"| Condition | $n$ | PR (mean$\\\\pm$SD) | H7\\\\% (mean$\\\\pm$SD) | H7\\\\% BCa 95\\\\% CI | Gen\\\\% (mean$\\\\pm$SD) | Gen\\\\% BCa 95\\\\% CI |\")\n    L.append(\"|:----------|----:|:------------------|:-------------------|:-----------------|:-------------------|:-----------------|\")\n    for _, r in cond_df.iterrows():\n        cond = r[\"condition\"]\n        h7_bca = bca_h7.get(cond, {})\n        gen_bca = bca_gen.get(cond, {})\n        h7_ci = f\"[{h7_bca['ci_lo']*100:.1f}, {h7_bca['ci_hi']*100:.1f}]\" if h7_bca and not np.isnan(h7_bca.get('ci_lo', np.nan)) else \"N/A\"\n        gen_ci = f\"[{gen_bca['ci_lo']*100:.1f}, {gen_bca['ci_hi']*100:.1f}]\" if gen_bca and not np.isnan(gen_bca.get('ci_lo', np.nan)) else \"N/A\"\n        L.append(\n            f\"| {cond} | {int(r['n_seeds'])} | \"\n            f\"{r['PR_mean']:.1f}$\\\\pm${r['PR_std']:.1f} | \"\n            f\"{r['H7_rate_mean']*100:.1f}$\\\\pm${r['H7_rate_std']*100:.1f} | \"\n            f\"{h7_ci} | \"\n            f\"{r['genuine_rate_mean']*100:.1f}$\\\\pm${r['genuine_rate_std']*100:.1f} | \"\n            f\"{gen_ci} |\"\n        )\n\n    # Statistical tests\n    if fisher and perm and mw and bf:\n        L.append(\"\\n### Statistical Tests\\n\")\n\n        # Fisher\n        or_str = \"$\\\\infty$\" if np.isinf(fisher['odds_ratio']) else f\"{fisher['odds_ratio']:.2f}\"\n        ci_lo = f\"{fisher['or_ci_lo']:.2f}\" if not np.isnan(fisher['or_ci_lo']) else \"0\"\n        ci_hi = \"$\\\\infty$\" if np.isinf(fisher.get('or_ci_hi', np.inf)) or np.isnan(fisher.get('or_ci_hi', np.nan)) else f\"{fisher['or_ci_hi']:.2f}\"\n        L.append(\"**1. H7 Domination Fisher Exact Test** (threshold: H7$\\\\geq$50\\\\% of proved)\")\n        L.append(f\"- ISR: {fisher['ISR']['h7_dom']}/{fisher['ISR']['n']} seeds H7-dominated; \"\n                 f\"Random: {fisher['RANDOM']['h7_dom']}/{fisher['RANDOM']['n']}\")\n        L.append(f\"- OR = {or_str}, 95\\\\% exact CI = [{ci_lo}, {ci_hi}], \"\n                 f\"$p$ = {fmt_p(fisher['p_value'])}\")\n        L.append(\"\")\n\n        # Permutation\n        L.append(f\"**2. Genuine Rate Permutation Test** ($n$ = {perm['n_perm']:,} permutations)\")\n        L.append(f\"- ISR mean: {perm['isr_mean']*100:.2f}\\\\%, Random mean: {perm['random_mean']*100:.2f}\\\\%\")\n        L.append(f\"- $\\\\Delta$ = {perm['observed_diff']*100:.2f} pp, $p$ = {fmt_p(perm['p_value'])}\")\n        L.append(\"\")\n\n        # Mann-Whitney\n        L.append(\"**3. H7 Rate Mann-Whitney $U$ Test**\")\n        L.append(f\"- ISR median: {mw['isr_median']*100:.1f}\\\\%, Random median: {mw['random_median']*100:.1f}\\\\%\")\n        L.append(f\"- $U$ = {mw['U']:.1f}, $p$ = {fmt_p(mw['p_value'])}, \"\n                 f\"rank-biserial $r$ = {mw['r_rank_biserial']:.3f}\")\n        L.append(\"\")\n\n        # Bayes Factor\n        L.append(\"**4. Bayes Factor** (Beta-Binomial conjugate, prior: Beta(1,1))\")\n        L.append(f\"- $BF_{{10}}$ = {bf['bf10']:.2f} ({bf['interpretation']})\")\n        L.append(f\"- ISR: {bf['k_isr']}/{bf['n_isr']} H7-dominated, \"\n                 f\"Random: {bf['k_rand']}/{bf['n_rand']}\")\n\n        if mw_isr_star:\n            L.append(\"\")\n            L.append(\"**5. ISR* (Proved-Only Mean ISR) Mann-Whitney $U$ Test**\")\n            L.append(f\"- ISR mean: {mw_isr_star['isr_mean']:.4f}, median: {mw_isr_star['isr_median']:.4f}\")\n            L.append(f\"- Random mean: {mw_isr_star['random_mean']:.4f}, median: {mw_isr_star['random_median']:.4f}\")\n            L.append(f\"- $U$ = {mw_isr_star['U']:.1f}, $p$ = {fmt_p(mw_isr_star['p_value'])}, \"\n                     f\"rank-biserial $r$ = {mw_isr_star['r_rank_biserial']:.3f}\")\n\n    return \"\\n\".join(L) + \"\\n\"\n\n\n# --- Main ---\n\ndef main():\n    args = parse_args()\n    data_dir = Path(args.data_dir)\n\n    if not data_dir.exists():\n        print(f\"ERROR: data directory {data_dir} does not exist\", file=sys.stderr)\n        sys.exit(1)\n\n    if args.prefix:\n        prefixes = [args.prefix]\n    elif args.prefixes:\n        prefixes = [p.strip() for p in args.prefixes.split(\",\")]\n    else:\n        prefixes = MODE_PREFIXES[args.mode]\n    print(f\"Mode: {args.mode} | Prefixes: {prefixes}\")\n\n    runs = discover_runs(data_dir, prefixes)\n    if not runs:\n        print(f\"ERROR: no runs found in {data_dir} with prefixes {prefixes}\", file=sys.stderr)\n        sys.exit(1)\n\n    isr_count = sum(1 for r in runs if r[\"condition\"] == \"ISR\")\n    rand_count = sum(1 for r in runs if r[\"condition\"] == \"RANDOM\")\n    print(f\"Found {len(runs)} runs: {isr_count} ISR, {rand_count} RANDOM\")\n    for r in runs:\n        print(f\"  {r['condition']:6s} s{r['seed']} <- {r['dir_name']}\")\n\n    df = build_table(runs)\n    print_per_seed_table(df)\n\n    cond_df = condition_stats(df)\n    print_condition_stats(cond_df)\n\n    if isr_count < 2 or rand_count < 2:\n        print(\"\\nWARNING: need >= 2 seeds per condition for statistical tests, skipping.\",\n              file=sys.stderr)\n        bca_h7 = bca_bootstrap_ci(df, \"H7_rate\", args.n_boot, args.seed)\n        bca_gen = bca_bootstrap_ci(df, \"genuine_rate\", args.n_boot, args.seed)\n        if args.output:\n            md = generate_markdown(df, cond_df, {}, {}, {}, {}, bca_h7, bca_gen)\n            Path(args.output).write_text(md)\n            print(f\"\\nMarkdown written to {args.output}\")\n        return\n\n    fisher = fisher_h7_domination(df)\n    perm = permutation_test_genuine(df, n_perm=args.n_perm, rng_seed=args.seed)\n    mw = mannwhitney_h7(df)\n    bf = bayes_factor_h7_domination(df)\n    bca_h7 = bca_bootstrap_ci(df, \"H7_rate\", args.n_boot, args.seed)\n    bca_gen = bca_bootstrap_ci(df, \"genuine_rate\", args.n_boot, args.seed)\n    mw_isr_star = mannwhitney_isr_star(df)\n\n    print_tests(fisher, perm, mw, bf, bca_h7, bca_gen, mw_isr_star)\n\n    md = generate_markdown(df, cond_df, fisher, perm, mw, bf, bca_h7, bca_gen, mw_isr_star)\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  MARKDOWN OUTPUT (appendix-ready)\")\n    print(\"=\" * 90)\n    print(md)\n\n    if args.output:\n        Path(args.output).parent.mkdir(parents=True, exist_ok=True)\n        Path(args.output).write_text(md)\n        print(f\"Markdown written to {args.output}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 641,
      "startLine": 1,
      "totalLines": 641
    }
  }
}
```

</details>

---

### Assistant

_source line 60_

Script looks correct. Now deploying to server and running.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "67f37fd5-0aef-4697-a68f-4dca101e5d32",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AHjqKQnH6bJAhk19BqVLDr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11343,
      "cache_read_input_tokens": 53319,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11343
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

_source line 61_

<details open><summary>🔧 Tool call — Bash · `toolu_01JGUAcz4iUXpw5pudGWp8iM`</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/scripts/d134_analysis.py | base64 -w0",
  "description": "Base64 encode the script for transfer"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "4fcba78c-5c84-49eb-beb1-5466536e24db",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AHjqKQnH6bJAhk19BqVLDr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11343,
      "cache_read_input_tokens": 53319,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11343
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

_source line 62 · 2026-05-18T23:33:44.436Z_

<details><summary>↩ Tool result · `toolu_01JGUAcz4iUXpw5pudGWp8iM`</summary>

```text
&lt;persisted-output>
Output too large (33.2KB). Full output saved to: /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/312696ef-b0f4-4bcb-8551-4747dab89c15/tool-results/bkrnimoo2.txt

Preview (first 2KB):
IyEvdXNyL2Jpbi9lbnYgcHl0aG9uMwoiIiJEMTM0IGV4cGVyaW1lbnQgYW5hbHlzaXM6IG11bHRpLXNlZWQgSVNSIHZzIFJhbmRvbSwgNEIgR1JQTyB0cmFpbmluZy4KUmVhZHMgdGF4b25vbXkgZGF0YSBmcm9tIGNsYXNzaWZ5Lmpzb24sIHRheG9ub215Lmpzb24sIG9yIHRvcC1sZXZlbCB0YXhvbm9teSBmaWxlcy4KQ29tcHV0ZXMgc3VtbWFyeSBzdGF0cywgc3RhdGlzdGljYWwgdGVzdHMgKEZpc2hlciwgTWFubi1XaGl0bmV5LCBwZXJtdXRhdGlvbiwgQmF5ZXMgRmFjdG9yKSwKYW5kIEJDYSBib290c3RyYXAgQ0lzLiBPdXRwdXRzIGFwcGVuZGl4LXJlYWR5IG1hcmtkb3duLgoiIiIKCmltcG9ydCBhcmdwYXJzZQppbXBvcnQganNvbgppbXBvcnQgcmUKaW1wb3J0IHN5cwpmcm9tIHBhdGhsaWIgaW1wb3J0IFBhdGgKCmltcG9ydCBudW1weSBhcyBucAppbXBvcnQgcGFuZGFzIGFzIHBkCmZyb20gc2NpcHkgaW1wb3J0IHN0YXRzCmZyb20gc2NpcHkuc3BlY2lhbCBpbXBvcnQgYmV0YWxuCgpDT05ESVRJT05fTUFQID0gWwogICAgKCJkMTM0XzRiX2lzciIsICJJU1IiKSwKICAgICgiZDEzNF80Yl9yYW5kb20iLCAiUkFORE9NIiksCiAgICAoInBsYW4wMDJfYWRkaXRpdmUiLCAiSVNSIiksCiAgICAoInBsYW4wMThfYWRkaXRpdmVfcmFuZG9tIiwgIlJBTkRPTSIpLAogICAgKCJwbGFuMDE4X3JhbmRvbSIsICJSQU5ET00iKSwKXQoKTU9ERV9QUkVGSVhFUyA9IHsKICAgICJkMTM0X29ubHkiOiBbImQxMzRfNGIiXSwKICAgICJhbGwiOiBbImQxMzRfNGIiLCAicGxhbjAwMl9hZGRpdGl2ZV9iMDEiLCAicGxhbjAxOF9hZGRpdGl2ZV9yYW5kb21fYjAxIiwgInBsYW4wMThfcmFuZG9tIl0sCn0KCgpkZWYgcGFyc2VfYXJncygpOgogICAgcCA9IGFyZ3BhcnNlLkFyZ3VtZW50UGFyc2VyKGRlc2NyaXB0aW9uPSJEMTM0IG11bHRpLXNlZWQgYW5hbHlzaXMgYW5kIHN0YXRpc3RpY2FsIHRlc3RzIikKICAgIHAuYWRkX2FyZ3VtZW50KCItLWRhdGFfZGlyIiwgdHlwZT1zdHIsIGRlZmF1bHQ9Ii9yb290L2F1dG9kbC10bXAvb3V0cHV0cyIsCiAgICAgICAgICAgICAgICAgICBoZWxwPSJEaXJlY3RvcnkgY29udGFpbmluZyBleHBlcmltZW50IG91dHB1dHMiKQogICAgcC5hZGRfYXJndW1lbnQoIi0tbW9kZSIsIHR5cGU9c3RyLCBkZWZhdWx0PSJkMTM0X29ubHkiLCBjaG9pY2VzPWxpc3QoTU9ERV9QUkVGSVhFUyksCiAgICAgICAgICAgICAgICAgICBoZWxwPSJkMTM0X29ubHkgPSBtYXRjaGVkIDUrNSBkZXNpZ24gKGRlZmF1bHQpOyBhbGwgPSBpbmNsdWRlIG9yaWdpbmFsIHNlZWRzIikKICAgIHAuYWRkX2FyZ3VtZW50KCItLXByZWZpeCIsIHR5cGU9c3RyLCBkZWZhdWx0PU5vbmUsCiAgICAgICAgICAgICAgICAgICBoZWxwPSIoTGVnYWN5KSBTaW5nbGUgcHJlZml4IGZpbHRlcjsgb3ZlcnJpZGVzIG1vZGUvcHJlZml4ZXMiKQogICAgcC5hZGRfYXJndW1lbnQoIi0tcHJlZml4ZXMiLCB0eXBlPXN0ciwgZGVmYXVsdD1Ob25lLAogICAgICAgICAgICAg
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
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "fded3820-7c38-4eff-9748-843fa71c3f80",
  "tool_use_result": {
    "stdout": "[ATTACHMENT_DATA_REDACTED]",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false,
    "persistedOutputPath": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/312696ef-b0f4-4bcb-8551-4747dab89c15/tool-results/bkrnimoo2.txt",
    "persistedOutputSize": 33980
  }
}
```

</details>

---

### Tool call

_source line 63_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01CAQ1W23e5DwtgKUz9372dp`</summary>

```json
{
  "server": "westd-39279",
  "account": "root",
  "command": "cat > /tmp/upload_script.py << 'PYEOF'\nimport base64, sys\nb64 = sys.stdin.read().strip()\nwith open(\"/root/solver-trace-ablation/scripts/d134_analysis.py\", \"wb\") as f:\n    f.write(base64.b64decode(b64))\nprint(\"OK\")\nPYEOF\necho \"ready\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "58775769-938f-4af7-8ac8-a5d752ea336b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WQknN5yv12ye7W24SnBPX2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1969,
      "cache_read_input_tokens": 64662,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1969
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

_source line 64 · 2026-05-18T23:33:49.573Z_

<details><summary>↩ Tool result · `toolu_01CAQ1W23e5DwtgKUz9372dp`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"ready\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "f40e19eb-f3ae-4b5e-b5aa-eba91472dfcd",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"ready\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"ready\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 65_

<details><summary>Logged reasoning block</summary>

```text
I need to transfer the file. Let me use a different approach - I'll read the file content and write it via ssh_execute with a heredoc. But the file is ~25KB which should be fine.

Actually, let me just use scp or write the file via ssh_execute using a Python command that reads base64 from a heredoc.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "3b12c425-1f1c-4dbf-9770-fab0c78d61be",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V3fNExaVdpPExfB347hf6a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 269,
      "cache_read_input_tokens": 66631,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 269
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

_source line 66_

Let me use a more direct approach - write the file via heredoc on the server.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "c69d20d4-05ec-480c-b4c6-18b33537497a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V3fNExaVdpPExfB347hf6a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 269,
      "cache_read_input_tokens": 66631,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 269
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

_source line 67_

<details open><summary>🔧 Tool call — Read · `toolu_015M3WjXAiqcqHH1vyMys82K`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/312696ef-b0f4-4bcb-8551-4747dab89c15/tool-results/bkrnimoo2.txt",
  "limit": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "8cffc9e5-b7b7-4687-aa4c-c1244077f12c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V3fNExaVdpPExfB347hf6a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 269,
      "cache_read_input_tokens": 66631,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 269
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

_source line 68 · 2026-05-18T23:33:56.522Z_

<details><summary>↩ Tool result · reported error · `toolu_015M3WjXAiqcqHH1vyMys82K`</summary>

```text
File content (27612 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "653ddace-0246-497b-8be4-aedefdde42d4",
  "tool_use_result": "Error: File content (27612 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---

### Tool call

_source line 69_

<details open><summary>🔧 Tool call — Read · `toolu_01Dda2ajsx63Ad2HVt3b6wZR`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/312696ef-b0f4-4bcb-8551-4747dab89c15/tool-results/bkrnimoo2.txt",
  "offset": 0,
  "limit": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "2f90ea1d-dff0-44cf-8e9e-6132e743fe67",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UwYe22dSwHp1JB3rHBkh2p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 316,
      "cache_read_input_tokens": 66900,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 316
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

_source line 70 · 2026-05-18T23:33:59.812Z_

<details><summary>↩ Tool result · reported error · `toolu_01Dda2ajsx63Ad2HVt3b6wZR`</summary>

```text
File content (27612 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "2573bf74-d400-410e-844e-1aa1c422c84d",
  "tool_use_result": "Error: File content (27612 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---

### Assistant

_source line 71_

<details><summary>Logged reasoning block</summary>

```text
The base64 output is too large to read back. Let me use a different approach - I'll use scp via bash to transfer the file to the server.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "cb7b7648-7d00-473f-9c3b-ef9732e1920d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WeUCYZwtekyBRY3N7Ack2j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 328,
      "cache_read_input_tokens": 67216,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 328
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

_source line 72_

<details open><summary>🔧 Tool call — Bash · `toolu_016MvQU7Lzvxk7DYYEWKfADL`</summary>

```json
{
  "command": "scp /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/scripts/d134_analysis.py connect.westd.seetacloud.com:/root/solver-trace-ablation/scripts/d134_analysis.py 2>&1",
  "description": "SCP the updated script to server",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "a1327c8d-7ac9-47ae-b85e-f0e3f9d33f78",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WeUCYZwtekyBRY3N7Ack2j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 328,
      "cache_read_input_tokens": 67216,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 328
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

_source line 73 · 2026-05-18T23:34:05.029Z_

<details><summary>↩ Tool result · reported error · `toolu_016MvQU7Lzvxk7DYYEWKfADL`</summary>

```text
Exit code 255
ssh_askpass: exec(/usr/bin/ssh-askpass): No such file or directory
Permission denied, please try again.
ssh_askpass: exec(/usr/bin/ssh-askpass): No such file or directory
Permission denied, please try again.
ssh_askpass: exec(/usr/bin/ssh-askpass): No such file or directory
ubuntu@connect.westd.seetacloud.com: Permission denied ().
scp: Connection closed
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "2b6aaa8a-0c5f-47d2-806d-05825a67b803",
  "tool_use_result": "Error: Exit code 255\nssh_askpass: exec(/usr/bin/ssh-askpass): No such file or directory\r\nPermission denied, please try again.\r\nssh_askpass: exec(/usr/bin/ssh-askpass): No such file or directory\r\nPermission denied, please try again.\r\nssh_askpass: exec(/usr/bin/ssh-askpass): No such file or directory\r\nubuntu@connect.westd.seetacloud.com: Permission denied ().\r\nscp: Connection closed"
}
```

</details>

---

### Assistant

_source line 74_

<details><summary>Logged reasoning block</summary>

```text
The scp fails because the SSH config expects a different user. The server expects root@connect.westd.seetacloud.com. Let me try with root@. Or maybe I should just write the file content via ssh_execute using a heredoc approach.

Actually, let me look at the SSH config to understand how to connect.

Let me try a different approach - write the file via ssh_execute using Python with a here-document containing the file content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "14c5a4fb-4bce-41b6-8270-57336a3b5112",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016QQ13dLcDznV3kDkeD9VNQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 343,
      "cache_read_input_tokens": 67544,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 343
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

<details open><summary>🔧 Tool call — Bash · `toolu_0199RoirXspbbL1SuCYuvDcw`</summary>

```json
{
  "command": "wc -c /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/scripts/d134_analysis.py",
  "description": "Check file size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "c0371502-7eec-4cd2-b65b-20eb93081455",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016QQ13dLcDznV3kDkeD9VNQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 343,
      "cache_read_input_tokens": 67544,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 343
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

_source line 76 · 2026-05-18T23:34:10.085Z_

<details><summary>↩ Tool result · `toolu_0199RoirXspbbL1SuCYuvDcw`</summary>

```text
25485 /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/scripts/d134_analysis.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "a9bded55-436a-43b7-85aa-1ba3b305bb2d",
  "tool_use_result": {
    "stdout": "25485 /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/scripts/d134_analysis.py",
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

_source line 77_

Let me write the file via ssh_execute using base64.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "a8ff17b7-301a-4d44-8efe-852ad4e9cce9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Yh87mmduxZPWimtghE56p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 277,
      "cache_read_input_tokens": 67887,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 277
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

_source line 78_

<details open><summary>🔧 Tool call — Bash · `toolu_01TokgbS7BfgmyBNsmyUwAeq`</summary>

```json
{
  "command": "base64 -w0 /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/scripts/d134_analysis.py | head -c 100",
  "description": "Get start of base64 to verify"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "2486c08b-cfe1-4fb2-8f16-3dc8682da675",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Yh87mmduxZPWimtghE56p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 277,
      "cache_read_input_tokens": 67887,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 277
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

_source line 79 · 2026-05-18T23:34:13.877Z_

<details><summary>↩ Tool result · `toolu_01TokgbS7BfgmyBNsmyUwAeq`</summary>

```text
IyEvdXNyL2Jpbi9lbnYgcHl0aG9uMwoiIiJEMTM0IGV4cGVyaW1lbnQgYW5hbHlzaXM6IG11bHRpLXNlZWQgSVNSIHZzIFJhbmRv
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "2ffffe4b-1994-4a40-9d64-08345b30c01a",
  "tool_use_result": {
    "stdout": "IyEvdXNyL2Jpbi9lbnYgcHl0aG9uMwoiIiJEMTM0IGV4cGVyaW1lbnQgYW5hbHlzaXM6IG11bHRpLXNlZWQgSVNSIHZzIFJhbmRv",
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

_source line 80_

<details open><summary>🔧 Tool call — Bash · `toolu_012LfMYx6M88gXHGVV5HHQjf`</summary>

```json
{
  "command": "B64=$(base64 -w0 /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/scripts/d134_analysis.py) && echo \"len=${#B64}\"",
  "description": "Get full base64 string length"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "d975d553-0467-4dc9-9002-e88daed395fe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HBrRHdfJcRbmLAmkxAounv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 244,
      "cache_read_input_tokens": 68164,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 244
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

_source line 81 · 2026-05-18T23:34:17.091Z_

<details><summary>↩ Tool result · `toolu_012LfMYx6M88gXHGVV5HHQjf`</summary>

```text
len=33980
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "740ee460-1355-4f50-8575-38dace71daca",
  "tool_use_result": {
    "stdout": "len=33980",
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

_source line 82_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01Aq1MP3yTCt3AVgzYTv5GMW`</summary>

```json
{
  "server": "westd-39279",
  "account": "root",
  "command": "echo 'IyEvdXNyL2Jpbi9lbnYgcHl0aG9uMwoiIiJEMTM0IGV4cGVyaW1lbnQgYW5hbHlzaXM6IG11bHRpLXNlZWQgSVNSIHZzIFJhbmRvbSwgNEIgR1JQTyB0cmFpbmluZy4KUmVhZHMgdGF4b25vbXkgZGF0YSBmcm9tIGNsYXNzaWZ5Lmpzb24sIHRheG9ub215Lmpzb24sIG9yIHRvcC1sZXZlbCB0YXhvbm9teSBmaWxlcy4KQ29tcHV0ZXMgc3VtbWFyeSBzdGF0cywgc3RhdGlzdGljYWwgdGVzdHMgKEZpc2hlciwgTWFubi1XaGl0bmV5LCBwZXJtdXRhdGlvbiwgQmF5ZXMgRmFjdG9yKSwKYW5kIEJDYSBib290c3RyYXAgQ0lzLiBPdXRwdXRzIGFwcGVuZGl4LXJlYWR5IG1hcmtkb3duLgoiIiIKCmltcG9ydCBhcmdwYXJzZQppbXBvcnQganNvbgppbXBvcnQgcmUKaW1wb3J0IHN5cwpmcm9tIHBhdGhsaWIgaW1wb3J0IFBhdGgKCmltcG9ydCBudW1weSBhcyBucAppbXBvcnQgcGFuZGFzIGFzIHBkCmZyb20gc2NpcHkgaW1wb3J0IHN0YXRzCmZyb20gc2NpcHkuc3BlY2lhbCBpbXBvcnQgYmV0YWxuCgpDT05ESVRJT05fTUFQID0gWwogICAgKCJkMTM0XzRiX2lzciIsICJJU1IiKSwKICAgICgiZDEzNF80Yl9yYW5kb20iLCAiUkFORE9NIiksCiAgICAoInBsYW4wMDJfYWRkaXRpdmUiLCAiSVNSIiksCiAgICAoInBsYW4wMThfYWRkaXRpdmVfcmFuZG9tIiwgIlJBTkRPTSIpLAogICAgKCJwbGFuMDE4X3JhbmRvbSIsICJSQU5ET00iKSwKXQoKTU9ERV9QUkVGSVhFUyA9IHsKICAgICJkMTM0X29ubHkiOiBbImQxMzRfNGIiXSwKICAgICJhbGwiOiBbImQxMzRfNGIiLCAicGxhbjAwMl9hZGRpdGl2ZV9iMDEiLCAicGxhbjAxOF9hZGRpdGl2ZV9yYW5kb21fYjAxIiwgInBsYW4wMThfcmFuZG9tIl0sCn0KCgpkZWYgcGFyc2VfYXJncygpOgogICAgcCA9IGFyZ3BhcnNlLkFyZ3VtZW50UGFyc2VyKGRlc2NyaXB0aW9uPSJEMTM0IG11bHRpLXNlZWQgYW5hbHlzaXMgYW5kIHN0YXRpc3RpY2FsIHRlc3RzIikKICAgIHAuYWRkX2FyZ3VtZW50KCItLWRhdGFfZGlyIiwgdHlwZT1zdHIsIGRlZmF1bHQ9Ii9yb290L2F1dG9kbC10bXAvb3V0cHV0cyIsCiAgICAgICAgICAgICAgICAgICBoZWxwPSJEaXJlY3RvcnkgY29udGFpbmluZyBleHBlcmltZW50IG91dHB1dHMiKQogICAgcC5hZGRfYXJndW1lbnQoIi0tbW9kZSIsIHR5cGU9c3RyLCBkZWZhdWx0PSJkMTM0X29ubHkiLCBjaG9pY2VzPWxpc3QoTU9ERV9QUkVGSVhFUyksCiAgICAgICAgICAgICAgICAgICBoZWxwPSJkMTM0X29ubHkgPSBtYXRjaGVkIDUrNSBkZXNpZ24gKGRlZmF1bHQpOyBhbGwgPSBpbmNsdWRlIG9yaWdpbmFsIHNlZWRzIikKICAgIHAuYWRkX2FyZ3VtZW50KCItLXByZWZpeCIsIHR5cGU9c3RyLCBkZWZhdWx0PU5vbmUsCiAgICAgICAgICAgICAgICAgICBoZWxwPSIoTGVnYWN5KSBTaW5nbGUgcHJlZml4IGZpbHRlcjsgb3ZlcnJpZGVzIG1vZGUvcHJlZml4ZXMiKQogICAgcC5hZGRfYXJndW1lbnQoIi0tcHJlZml4ZXMiLCB0eXBlPXN0ciwgZGVmYXVsdD1Ob25lLAogICAgICAgICAgICAgICAgICAgaGVscD0iQ29tbWEtc2VwYXJhdGVkIHByZWZpeGVzOyBvdmVycmlkZXMgLS1tb2RlIikKICAgIHAuYWRkX2FyZ3VtZW50KCItLW91dHB1dCIsIHR5cGU9c3RyLCBkZWZhdWx0PU5vbmUsCiAgICAgICAgICAgICAgICAgICBoZWxwPSJXcml0ZSBtYXJrZG93biBzdW1tYXJ5IHRvIHRoaXMgZmlsZSIpCiAgICBwLmFkZF9hcmd1bWVudCgiLS1uX3Blcm0iLCB0eXBlPWludCwgZGVmYXVsdD0xMDAwMCwKICAgICAgICAgICAgICAgICAgIGhlbHA9Ik51bWJlciBvZiBwZXJtdXRhdGlvbnMgZm9yIHBlcm11dGF0aW9uIHRlc3QiKQogICAgcC5hZGRfYXJndW1lbnQoIi0tbl9ib290IiwgdHlwZT1pbnQsIGRlZmF1bHQ9MTAwMDAsCiAgICAgICAgICAgICAgICAgICBoZWxwPSJOdW1iZXIgb2YgYm9vdHN0cmFwIHJlc2FtcGxlcyBmb3IgQkNhIENJIikKICAgIHAuYWRkX2FyZ3VtZW50KCItLXNlZWQiLCB0eXBlPWludCwgZGVmYXVsdD00MiwKICAgICAgICAgICAgICAgICAgIGhlbHA9IlJhbmRvbSBzZWVkIGZvciBwZXJtdXRhdGlvbi9ib290c3RyYXAiKQogICAgcmV0dXJuIHAucGFyc2VfYXJncygpCgoKIyAtLS0gRGF0YSBsb2FkaW5nIC0tLQoKZGVmIG1hdGNoX2NvbmRpdGlvbihuYW1lOiBzdHIpIC0+IHN0ciB8IE5vbmU6CiAgICBiZXN0X3ByZWZpeCA9ICIiCiAgICBiZXN0X2NvbmQgPSBOb25lCiAgICBmb3IgcHJlZml4LCBjb25kIGluIENPTkRJVElPTl9NQVA6CiAgICAgICAgaWYgbmFtZS5zdGFydHN3aXRoKHByZWZpeCkgYW5kIGxlbihwcmVmaXgpID4gbGVuKGJlc3RfcHJlZml4KToKICAgICAgICAgICAgYmVzdF9wcmVmaXggPSBwcmVmaXgKICAgICAgICAgICAgYmVzdF9jb25kID0gY29uZAogICAgcmV0dXJuIGJlc3RfY29uZAoKCmRlZiBleHRyYWN0X3NlZWQobmFtZTogc3RyKSAtPiBpbnQgfCBOb25lOgogICAgbSA9IHJlLnNlYXJjaChyJ19zKFxkKyknLCBuYW1lKQogICAgcmV0dXJuIGludChtLmdyb3VwKDEpKSBpZiBtIGVsc2UgTm9uZQoKCmRlZiBsb2FkX2V2YWxfcmVzdWx0cyhwYXRoOiBQYXRoKSAtPiBkaWN0IHwgTm9uZToKICAgIGlmIG5vdCBwYXRoLmV4aXN0cygpOgogICAgICAgIHJldHVybiBOb25lCiAgICB3aXRoIG9wZW4ocGF0aCkgYXMgZjoKICAgICAgICBkYXRhID0ganNvbi5sb2FkKGYpCiAgICBpZiAiZXZhbF9yZXN1bHRzIiBpbiBkYXRhOgogICAgICAgIHJldHVybiBkYXRhWyJldmFsX3Jlc3VsdHMiXQogICAgcmV0dXJuIGRhdGEKCgpkZWYgbG9hZF90YXhvbm9teV91bmlmaWVkKHBhdGg6IFBhdGgpIC0+IGRpY3QgfCBOb25lOgogICAgd2l0aCBvcGVuKHBhdGgpIGFzIGY6CiAgICAgICAgcmF3ID0ganNvbi5sb2FkKGYpCiAgICB0ID0gcmF3LmdldCgidGF4b25vbXkiLCB7fSkKICAgIHByb3ZlZCA9IHQuZ2V0KCJwcm92ZWQiLCAwKQogICAgaWYgcHJvdmVkID09IDA6CiAgICAgICAgcmV0dXJuIE5vbmUKICAgIGg3ID0gdC5nZXQoIkg3IiwgMCkKICAgIGgxID0gdC5nZXQoIkgxX2V4YWN0IiwgMCkKICAgIGg4ID0gdC5nZXQoIkg4IiwgMCkKICAgIGdlbnVpbmUgPSB0LmdldCgiZ2VudWluZSIsIDApCiAgICByZXR1cm4gewogICAgICAgICJuX3RvdGFsIjogMTAwLCAibl9wcm92ZWQiOiBwcm92ZWQsCiAgICAgICAgImg3X3RvdGFsX2NvdW50IjogaDcsICJoN190b3RhbF9yYXRlIjogaDcgLyBwcm92ZWQsCiAgICAgICAgImgxX3N0cmljdF9jb3VudCI6IGgxLCAiaDhfY29uanVuY3Rpb25fY29sbGFwc2VfY291bnQiOiBoOCwKICAgICAgICAiZ2VudWluZV9jb3VudCI6IGdlbnVpbmUsICJnZW51aW5lX3JhdGUiOiBnZW51aW5lIC8gcHJvdmVkLAogICAgICAgICJjb250ZW50X2luZGVwZW5kZW50X2NvdW50IjogMCwKICAgIH0KCgpkZWYgbG9hZF90YXhvbm9teV92ZXJpZmljYXRpb24ocGF0aDogUGF0aCkgLT4gZGljdCB8IE5vbmU6CiAgICB3aXRoIG9wZW4ocGF0aCkgYXMgZjoKICAgICAgICByYXcgPSBqc29uLmxvYWQoZikKICAgIHByb3ZlZCA9IHJhdy5nZXQoInByb3ZlZCIsIDApCiAgICBpZiBwcm92ZWQgPT0gMDoKICAgICAgICByZXR1cm4gTm9uZQogICAgdGF4ID0gcmF3LmdldCgidGF4b25vbXkiLCB7fSkKICAgIGg3ID0gdGF4LmdldCgiaDciLCB7fSkuZ2V0KCJjb3VudCIsIDApCiAgICBoMSA9IHRheC5nZXQoImgxX2V4YWN0Iiwge30pLmdldCgiY291bnQiLCAwKQogICAgaDggPSB0YXguZ2V0KCJoOCIsIHt9KS5nZXQoImNvdW50IiwgMCkKICAgIGdlbnVpbmUgPSB0YXguZ2V0KCJnZW51aW5lIiwge30pLmdldCgiY291bnQiLCAwKQogICAgcmV0dXJuIHsKICAgICAgICAibl90b3RhbCI6IHJhdy5nZXQoInRvdGFsIiwgMTAwKSwgIm5fcHJvdmVkIjogcHJvdmVkLAogICAgICAgICJoN190b3RhbF9jb3VudCI6IGg3LCAiaDdfdG90YWxfcmF0ZSI6IGg3IC8gcHJvdmVkLAogICAgICAgICJoMV9zdHJpY3RfY291bnQiOiBoMSwgImg4X2Nvbmp1bmN0aW9uX2NvbGxhcHNlX2NvdW50IjogaDgsCiAgICAgICAgImdlbnVpbmVfY291bnQiOiBnZW51aW5lLCAiZ2VudWluZV9yYXRlIjogZ2VudWluZSAvIHByb3ZlZCwKICAgICAgICAiY29udGVudF9pbmRlcGVuZGVudF9jb3VudCI6IDAsCiAgICB9CgoKZGVmIGRpc2NvdmVyX3J1bnMoZGF0YV9kaXI6IFBhdGgsIHByZWZpeGVzOiBsaXN0W3N0cl0pIC0+IGxpc3RbZGljdF06CiAgICBydW5zID0gW10KICAgIHNlZW4gPSBzZXQoKQogICAgZm9yIGVudHJ5IGluIHNvcnRlZChkYXRhX2Rpci5pdGVyZGlyKCkpOgogICAgICAgIG5hbWUgPSBlbnRyeS5uYW1lCiAgICAgICAgaWYgbm90IGFueShuYW1lLnN0YXJ0c3dpdGgocCkgZm9yIHAgaW4gcHJlZml4ZXMpOgogICAgICAgICAgICBjb250aW51ZQogICAgICAgIGNvbmQgPSBtYXRjaF9jb25kaXRpb24obmFtZSkKICAgICAgICBzZWVkX3ZhbCA9IGV4dHJhY3Rfc2VlZChuYW1lKQogICAgICAgIGlmIGNvbmQgaXMgTm9uZSBvciBzZWVkX3ZhbCBpcyBOb25lOgogICAgICAgICAgICBjb250aW51ZQogICAgICAgIGtleSA9IChjb25kLCBzZWVkX3ZhbCkKICAgICAgICBpZiBrZXkgaW4gc2VlbjoKICAgICAgICAgICAgY29udGludWUKICAgICAgICBkYXRhID0gTm9uZQogICAgICAgIGlmIGVudHJ5LmlzX2RpcigpOgogICAgICAgICAgICBmb3IgZm5hbWUgaW4gWyJjbGFzc2lmeS5qc29uIiwgInRheG9ub215Lmpzb24iXToKICAgICAgICAgICAgICAgIGRhdGEgPSBsb2FkX2V2YWxfcmVzdWx0cyhlbnRyeSAvIGZuYW1lKQogICAgICAgICAgICAgICAgaWYgZGF0YSBpcyBub3QgTm9uZToKICAgICAgICAgICAgICAgICAgICBicmVhawogICAgICAgICAgICBpZiBkYXRhIGlzIE5vbmU6CiAgICAgICAgICAgICAgICBjb250aW51ZQogICAgICAgIGVsaWYgZW50cnkuaXNfZmlsZSgpOgogICAgICAgICAgICBpZiBuYW1lLmVuZHN3aXRoKCJfdGF4b25vbXlfdW5pZmllZC5qc29uIik6CiAgICAgICAgICAgICAgICBkYXRhID0gbG9hZF90YXhvbm9teV91bmlmaWVkKGVudHJ5KQogICAgICAgICAgICBlbGlmIG5hbWUuZW5kc3dpdGgoIl90YXhvbm9teV92ZXJpZmljYXRpb24uanNvbiIpOgogICAgICAgICAgICAgICAgZGF0YSA9IGxvYWRfdGF4b25vbXlfdmVyaWZpY2F0aW9uKGVudHJ5KQogICAgICAgICAgICBpZiBkYXRhIGlzIE5vbmU6CiAgICAgICAgICAgICAgICBjb250aW51ZQogICAgICAgIGVsc2U6CiAgICAgICAgICAgIGNvbnRpbnVlCiAgICAgICAgc2Vlbi5hZGQoa2V5KQogICAgICAgIGlzcl9zdGFyID0gTm9uZQogICAgICAgIGlmIGVudHJ5LmlzX2RpcigpOgogICAgICAgICAgICBldmFsX3BhdGggPSBlbnRyeSAvICJldmFsX3Jlc3VsdHMuanNvbiIKICAgICAgICAgICAgaWYgZXZhbF9wYXRoLmV4aXN0cygpOgogICAgICAgICAgICAgICAgd2l0aCBvcGVuKGV2YWxfcGF0aCkgYXMgZWY6CiAgICAgICAgICAgICAgICAgICAgZXZhbF9yYXcgPSBqc29uLmxvYWQoZWYpCiAgICAgICAgICAgICAgICBpc3Jfc3RhciA9IGV2YWxfcmF3LmdldCgic3VtbWFyeSIsIHt9KS5nZXQoInByb3ZlZF9vbmx5X21lYW5faXNyIikKICAgICAgICBydW5zLmFwcGVuZCh7ImRpcl9uYW1lIjogbmFtZSwgInNlZWQiOiBzZWVkX3ZhbCwgImNvbmRpdGlvbiI6IGNvbmQsCiAgICAgICAgICAgICAgICAgICAgICAiZGF0YSI6IGRhdGEsICJpc3Jfc3RhciI6IGlzcl9zdGFyfSkKICAgIHJldHVybiBydW5zCgoKZGVmIGNvbXB1dGVfcm93KHJ1bjogZGljdCkgLT4gZGljdDoKICAgIGQgPSBydW5bImRhdGEiXQogICAgbl9wcm92ZWQgPSBkLmdldCgibl9wcm92ZWQiLCAwKQogICAgbl90b3RhbCA9IGQuZ2V0KCJuX3RvdGFsIiwgMTAwKQogICAgaDcgPSBkLmdldCgiaDdfdG90YWxfY291bnQiLCAwKQogICAgaDdfcmF0ZSA9IGQuZ2V0KCJoN190b3RhbF9yYXRlIiwgaDcgLyBuX3Byb3ZlZCBpZiBuX3Byb3ZlZCA+IDAgZWxzZSAwLjApCiAgICBoMSA9IGQuZ2V0KCJoMV9zdHJpY3RfY291bnQiLCAwKQogICAgaDggPSBkLmdldCgiaDhfY29uanVuY3Rpb25fY29sbGFwc2VfY291bnQiLCAwKQogICAgZ2VudWluZSA9IGQuZ2V0KCJnZW51aW5lX2NvdW50IiwgMCkKICAgIGdlbnVpbmVfcmF0ZSA9IGQuZ2V0KCJnZW51aW5lX3JhdGUiLCBnZW51aW5lIC8gbl9wcm92ZWQgaWYgbl9wcm92ZWQgPiAwIGVsc2UgMC4wKQogICAgY2kgPSBkLmdldCgiY29udGVudF9pbmRlcGVuZGVudF9jb3VudCIsIDApCiAgICBzbmggPSBtYXgoZ2VudWluZSAtIGNpLCAwKQogICAgc25oX3JhdGUgPSBzbmggLyBuX3Byb3ZlZCBpZiBuX3Byb3ZlZCA+IDAgZWxzZSAwLjAKICAgIHJldHVybiB7CiAgICAgICAgInNlZWQiOiBydW5bInNlZWQiXSwgImNvbmRpdGlvbiI6IHJ1blsiY29uZGl0aW9uIl0sICJuX3RvdGFsIjogbl90b3RhbCwKICAgICAgICAiUFIiOiBuX3Byb3ZlZCwgIkg3X2NvdW50IjogaDcsICJIN19yYXRlIjogaDdfcmF0ZSwKICAgICAgICAiSDFfY291bnQiOiBoMSwgIkg4X2NvdW50IjogaDgsCiAgICAgICAgImdlbnVpbmVfY291bnQiOiBnZW51aW5lLCAiZ2VudWluZV9yYXRlIjogZ2VudWluZV9yYXRlLAogICAgICAgICJDSV9jb3VudCI6IGNpLCAiU05IX2NvdW50Ijogc25oLCAiU05IX3JhdGUiOiBzbmhfcmF0ZSwKICAgICAgICAiSVNSX3N0YXIiOiBydW4uZ2V0KCJpc3Jfc3RhciIpLAogICAgfQoKCmRlZiBidWlsZF90YWJsZShydW5zOiBsaXN0W2RpY3RdKSAtPiBwZC5EYXRhRnJhbWU6CiAgICByb3dzID0gW2NvbXB1dGVfcm93KHIpIGZvciByIGluIHJ1bnNdCiAgICBkZiA9IHBkLkRhdGFGcmFtZShyb3dzKQogICAgZGYgPSBkZi5zb3J0X3ZhbHVlcyhbImNvbmRpdGlvbiIsICJzZWVkIl0pLnJlc2V0X2luZGV4KGRyb3A9VHJ1ZSkKICAgIHJldHVybiBkZgoKCiMgLS0tIFN0YXRpc3RpY2FsIHRlc3RzIC0tLQoKZGVmIGZpc2hlcl9oN19kb21pbmF0aW9uKGRmOiBwZC5EYXRhRnJhbWUpIC0+IGRpY3Q6CiAgICByZXN1bHRzID0ge30KICAgIGZvciBjb25kIGluIFsiSVNSIiwgIlJBTkRPTSJdOgogICAgICAgIHN1YiA9IGRmW2RmWyJjb25kaXRpb24iXSA9PSBjb25kXQogICAgICAgIHJlc3VsdHNbY29uZF0gPSB7CiAgICAgICAgICAgICJuIjogbGVuKHN1YiksCiAgICAgICAgICAgICJoN19kb20iOiBpbnQoKHN1YlsiSDdfcmF0ZSJdID49IDAuNSkuc3VtKCkpLAogICAgICAgICAgICAibm90X2g3X2RvbSI6IGludCgoc3ViWyJIN19yYXRlIl0gPCAwLjUpLnN1bSgpKSwKICAgICAgICB9CiAgICB0YWJsZSA9IG5wLmFycmF5KFsKICAgICAgICBbcmVzdWx0c1siSVNSIl1bImg3X2RvbSJdLCByZXN1bHRzWyJJU1IiXVsibm90X2g3X2RvbSJdXSwKICAgICAgICBbcmVzdWx0c1siUkFORE9NIl1bImg3X2RvbSJdLCByZXN1bHRzWyJSQU5ET00iXVsibm90X2g3X2RvbSJdXSwKICAgIF0pCiAgICBvZGRzX3JhdGlvLCBwX3ZhbHVlID0gc3RhdHMuZmlzaGVyX2V4YWN0KHRhYmxlLCBhbHRlcm5hdGl2ZT0iZ3JlYXRlciIpCgogICAgIyA5NSUgZXhhY3QgQ0kgdmlhIHNjaXB5LnN0YXRzLmNvbnRpbmdlbmN5CiAgICBvcl9jaV9sbywgb3JfY2lfaGkgPSBucC5uYW4sIG5wLm5hbgogICAgdHJ5OgogICAgICAgIGN0ID0gc3RhdHMuY29udGluZ2VuY3kub2Rkc19yYXRpbyh0YWJsZSkKICAgICAgICBjaSA9IGN0LmNvbmZpZGVuY2VfaW50ZXJ2YWwoY29uZmlkZW5jZV9sZXZlbD0wLjk1KQogICAgICAgIG9yX2NpX2xvLCBvcl9jaV9oaSA9IGNpLmxvdywgY2kuaGlnaAogICAgZXhjZXB0IEV4Y2VwdGlvbjoKICAgICAgICBwYXNzCgogICAgcmV0dXJuIHsKICAgICAgICAidGFibGUiOiB0YWJsZS50b2xpc3QoKSwKICAgICAgICAiSVNSIjogcmVzdWx0c1siSVNSIl0sCiAgICAgICAgIlJBTkRPTSI6IHJlc3VsdHNbIlJBTkRPTSJdLAogICAgICAgICJvZGRzX3JhdGlvIjogb2Rkc19yYXRpbywKICAgICAgICAib3JfY2lfbG8iOiBvcl9jaV9sbywKICAgICAgICAib3JfY2lfaGkiOiBvcl9jaV9oaSwKICAgICAgICAicF92YWx1ZSI6IHBfdmFsdWUsCiAgICB9CgoKZGVmIHBlcm11dGF0aW9uX3Rlc3RfZ2VudWluZShkZjogcGQuRGF0YUZyYW1lLCBuX3Blcm06IGludCA9IDEwMDAwLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICBybmdfc2VlZDogaW50ID0gNDIpIC0+IGRpY3Q6CiAgICBpc3IgPSBkZltkZlsiY29uZGl0aW9uIl0gPT0gIklTUiJdWyJnZW51aW5lX3JhdGUiXS52YWx1ZXMKICAgIHJhbmQgPSBkZltkZlsiY29uZGl0aW9uIl0gPT0gIlJBTkRPTSJdWyJnZW51aW5lX3JhdGUiXS52YWx1ZXMKICAgIG9ic2VydmVkID0gaXNyLm1lYW4oKSAtIHJhbmQubWVhbigpCiAgICBwb29sZWQgPSBucC5jb25jYXRlbmF0ZShbaXNyLCByYW5kXSkKICAgIG5faXNyID0gbGVuKGlzcikKICAgIHJuZyA9IG5wLnJhbmRvbS5kZWZhdWx0X3JuZyhybmdfc2VlZCkKICAgIGNvdW50ID0gMAogICAgZm9yIF8gaW4gcmFuZ2Uobl9wZXJtKToKICAgICAgICBwZXJtID0gcm5nLnBlcm11dGF0aW9uKHBvb2xlZCkKICAgICAgICBpZiBwZXJtWzpuX2lzcl0ubWVhbigpIC0gcGVybVtuX2lzcjpdLm1lYW4oKSA+PSBvYnNlcnZlZDoKICAgICAgICAgICAgY291bnQgKz0gMQogICAgcmV0dXJuIHsKICAgICAgICAib2JzZXJ2ZWRfZGlmZiI6IGZsb2F0KG9ic2VydmVkKSwKICAgICAgICAicF92YWx1ZSI6IGNvdW50IC8gbl9wZXJtLAogICAgICAgICJuX3Blcm0iOiBuX3Blcm0sCiAgICAgICAgImlzcl9tZWFuIjogZmxvYXQoaXNyLm1lYW4oKSksCiAgICAgICAgInJhbmRvbV9tZWFuIjogZmxvYXQocmFuZC5tZWFuKCkpLAogICAgfQoKCmRlZiBtYW5ud2hpdG5leV9oNyhkZjogcGQuRGF0YUZyYW1lKSAtPiBkaWN0OgogICAgaXNyID0gZGZbZGZbImNvbmRpdGlvbiJdID09ICJJU1IiXVsiSDdfcmF0ZSJdLnZhbHVlcwogICAgcmFuZCA9IGRmW2RmWyJjb25kaXRpb24iXSA9PSAiUkFORE9NIl1bIkg3X3JhdGUiXS52YWx1ZXMKICAgIG4xLCBuMiA9IGxlbihpc3IpLCBsZW4ocmFuZCkKICAgIHVfc3RhdCwgcF92YWx1ZSA9IHN0YXRzLm1hbm53aGl0bmV5dShpc3IsIHJhbmQsIGFsdGVybmF0aXZlPSJncmVhdGVyIikKICAgIHJfcmIgPSAyLjAgKiB1X3N0YXQgLyAobjEgKiBuMikgLSAxLjAgaWYgbjEgKiBuMiA+IDAgZWxzZSBucC5uYW4KICAgIHJldHVybiB7CiAgICAgICAgIlUiOiBmbG9hdCh1X3N0YXQpLAogICAgICAgICJwX3ZhbHVlIjogZmxvYXQocF92YWx1ZSksCiAgICAgICAgInJfcmFua19iaXNlcmlhbCI6IGZsb2F0KHJfcmIpLAogICAgICAgICJpc3JfbWVkaWFuIjogZmxvYXQobnAubWVkaWFuKGlzcikpLAogICAgICAgICJyYW5kb21fbWVkaWFuIjogZmxvYXQobnAubWVkaWFuKHJhbmQpKSwKICAgIH0KCgpkZWYgbWFubndoaXRuZXlfaXNyX3N0YXIoZGY6IHBkLkRhdGFGcmFtZSkgLT4gZGljdCB8IE5vbmU6CiAgICBpc3IgPSBkZltkZlsiY29uZGl0aW9uIl0gPT0gIklTUiJdWyJJU1Jfc3RhciJdLmRyb3BuYSgpLnZhbHVlcy5hc3R5cGUoZmxvYXQpCiAgICByYW5kID0gZGZbZGZbImNvbmRpdGlvbiJdID09ICJSQU5ET00iXVsiSVNSX3N0YXIiXS5kcm9wbmEoKS52YWx1ZXMuYXN0eXBlKGZsb2F0KQogICAgaWYgbGVuKGlzcikgPCAyIG9yIGxlbihyYW5kKSA8IDI6CiAgICAgICAgcmV0dXJuIE5vbmUKICAgIG4xLCBuMiA9IGxlbihpc3IpLCBsZW4ocmFuZCkKICAgIHVfc3RhdCwgcF92YWx1ZSA9IHN0YXRzLm1hbm53aGl0bmV5dShpc3IsIHJhbmQsIGFsdGVybmF0aXZlPSJncmVhdGVyIikKICAgIHJfcmIgPSAyLjAgKiB1X3N0YXQgLyAobjEgKiBuMikgLSAxLjAKICAgIHJldHVybiB7CiAgICAgICAgIlUiOiBmbG9hdCh1X3N0YXQpLAogICAgICAgICJwX3ZhbHVlIjogZmxvYXQocF92YWx1ZSksCiAgICAgICAgInJfcmFua19iaXNlcmlhbCI6IGZsb2F0KHJfcmIpLAogICAgICAgICJpc3JfbWVkaWFuIjogZmxvYXQobnAubWVkaWFuKGlzcikpLAogICAgICAgICJyYW5kb21fbWVkaWFuIjogZmxvYXQobnAubWVkaWFuKHJhbmQpKSwKICAgICAgICAiaXNyX21lYW4iOiBmbG9hdChucC5tZWFuKGlzcikpLAogICAgICAgICJyYW5kb21fbWVhbiI6IGZsb2F0KG5wLm1lYW4ocmFuZCkpLAogICAgfQoKCmRlZiBiY2FfYm9vdHN0cmFwX2NpKGRmOiBwZC5EYXRhRnJhbWUsIG1ldHJpYzogc3RyLCBuX2Jvb3Q6IGludCA9IDEwMDAwLAogICAgICAgICAgICAgICAgICAgICAgcm5nX3NlZWQ6IGludCA9IDQyKSAtPiBkaWN0OgogICAgIiIiQkNhIDk1JSBDSSB' | base64 -d | wc -c",
  "warn": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "74c84dfa-ca98-4f5e-90fb-d0217eaea6c4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JqMFEemetJP4MmL7tkYqUr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 147,
      "cache_read_input_tokens": 68408,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 147
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

_source line 83 · 2026-05-18T23:37:23.601Z_

<details><summary>↩ Tool result · `toolu_01Aq1MP3yTCt3AVgzYTv5GMW`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"10175\\n\", \"stderr\": \"base64: invalid input\\n\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "f83a725b-ef6c-4c56-902a-9c1128087a6d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"10175\\\\n\\\", \\\"stderr\\\": \\\"base64: invalid input\\\\n\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.51}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"10175\\n\", \"stderr\": \"base64: invalid input\\n\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 84_

<details><summary>Logged reasoning block</summary>

```text
The base64 is too long to pass in one command. Let me use a different approach. I'll write the file on the server using a Python script that receives the content via a heredoc. Or better, I'll use ssh_execute with the file written directly using a heredoc.

Actually, the simplest approach is to write the file in chunks or use a Python command to write it. Let me try writing the entire file content using a heredoc with ssh_execute.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "72c06b29-708a-4d9a-b697-b3e6a6a50001",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GM1AD6Cexa62kgg6bEjA6H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11212,
      "cache_read_input_tokens": 68555,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11212
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

_source line 85_

Let me write the file directly using a Python one-liner that writes the file content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "2f3eae88-c288-41bc-a4b9-4bc25a5992f7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GM1AD6Cexa62kgg6bEjA6H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11212,
      "cache_read_input_tokens": 68555,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11212
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01Abx3QWAn2c77uCvLDMfmqj`</summary>

```json
{
  "server": "westd-39279",
  "account": "root",
  "command": "cat > /root/solver-trace-ablation/scripts/d134_analysis.py << 'HEREDOC_EOF'\n#!/usr/bin/env python3\n\"\"\"D134 experiment analysis: multi-seed ISR vs Random, 4B GRPO training.\nReads taxonomy data from classify.json, taxonomy.json, or top-level taxonomy files.\nComputes summary stats, statistical tests (Fisher, Mann-Whitney, permutation, Bayes Factor),\nand BCa bootstrap CIs. Outputs appendix-ready markdown.\n\"\"\"\n\nimport argparse\nimport json\nimport re\nimport sys\nfrom pathlib import Path\n\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\nfrom scipy.special import betaln\n\nCONDITION_MAP = [\n    (\"d134_4b_isr\", \"ISR\"),\n    (\"d134_4b_random\", \"RANDOM\"),\n    (\"plan002_additive\", \"ISR\"),\n    (\"plan018_additive_random\", \"RANDOM\"),\n    (\"plan018_random\", \"RANDOM\"),\n]\n\nMODE_PREFIXES = {\n    \"d134_only\": [\"d134_4b\"],\n    \"all\": [\"d134_4b\", \"plan002_additive_b01\", \"plan018_additive_random_b01\", \"plan018_random\"],\n}\n\n\ndef parse_args():\n    p = argparse.ArgumentParser(description=\"D134 multi-seed analysis and statistical tests\")\n    p.add_argument(\"--data_dir\", type=str, default=\"/root/autodl-tmp/outputs\",\n                   help=\"Directory containing experiment outputs\")\n    p.add_argument(\"--mode\", type=str, default=\"d134_only\", choices=list(MODE_PREFIXES),\n                   help=\"d134_only = matched 5+5 design (default); all = include original seeds\")\n    p.add_argument(\"--prefix\", type=str, default=None,\n                   help=\"(Legacy) Single prefix filter; overrides mode/prefixes\")\n    p.add_argument(\"--prefixes\", type=str, default=None,\n                   help=\"Comma-separated prefixes; overrides --mode\")\n    p.add_argument(\"--output\", type=str, default=None,\n                   help=\"Write markdown summary to this file\")\n    p.add_argument(\"--n_perm\", type=int, default=10000,\n                   help=\"Number of permutations for permutation test\")\n    p.add_argument(\"--n_boot\", type=int, default=10000,\n                   help=\"Number of bootstrap resamples for BCa CI\")\n    p.add_argument(\"--seed\", type=int, default=42,\n                   help=\"Random seed for permutation/bootstrap\")\n    return p.parse_args()\n\n\n# --- Data loading ---\n\ndef match_condition(name: str) -> str | None:\n    best_prefix = \"\"\n    best_cond = None\n    for prefix, cond in CONDITION_MAP:\n        if name.startswith(prefix) and len(prefix) > len(best_prefix):\n            best_prefix = prefix\n            best_cond = cond\n    return best_cond\n\n\ndef extract_seed(name: str) -> int | None:\n    m = re.search(r'_s(\\d+)', name)\n    return int(m.group(1)) if m else None\n\n\ndef load_eval_results(path: Path) -> dict | None:\n    if not path.exists():\n        return None\n    with open(path) as f:\n        data = json.load(f)\n    if \"eval_results\" in data:\n        return data[\"eval_results\"]\n    return data\n\n\ndef load_taxonomy_unified(path: Path) -> dict | None:\n    with open(path) as f:\n        raw = json.load(f)\n    t = raw.get(\"taxonomy\", {})\n    proved = t.get(\"proved\", 0)\n    if proved == 0:\n        return None\n    h7 = t.get(\"H7\", 0)\n    h1 = t.get(\"H1_exact\", 0)\n    h8 = t.get(\"H8\", 0)\n    genuine = t.get(\"genuine\", 0)\n    return {\n        \"n_total\": 100, \"n_proved\": proved,\n        \"h7_total_count\": h7, \"h7_total_rate\": h7 / proved,\n        \"h1_strict_count\": h1, \"h8_conjunction_collapse_count\": h8,\n        \"genuine_count\": genuine, \"genuine_rate\": genuine / proved,\n        \"content_independent_count\": 0,\n    }\n\n\ndef load_taxonomy_verification(path: Path) -> dict | None:\n    with open(path) as f:\n        raw = json.load(f)\n    proved = raw.get(\"proved\", 0)\n    if proved == 0:\n        return None\n    tax = raw.get(\"taxonomy\", {})\n    h7 = tax.get(\"h7\", {}).get(\"count\", 0)\n    h1 = tax.get(\"h1_exact\", {}).get(\"count\", 0)\n    h8 = tax.get(\"h8\", {}).get(\"count\", 0)\n    genuine = tax.get(\"genuine\", {}).get(\"count\", 0)\n    return {\n        \"n_total\": raw.get(\"total\", 100), \"n_proved\": proved,\n        \"h7_total_count\": h7, \"h7_total_rate\": h7 / proved,\n        \"h1_strict_count\": h1, \"h8_conjunction_collapse_count\": h8,\n        \"genuine_count\": genuine, \"genuine_rate\": genuine / proved,\n        \"content_independent_count\": 0,\n    }\n\n\ndef discover_runs(data_dir: Path, prefixes: list[str]) -> list[dict]:\n    runs = []\n    seen = set()\n    for entry in sorted(data_dir.iterdir()):\n        name = entry.name\n        if not any(name.startswith(p) for p in prefixes):\n            continue\n        cond = match_condition(name)\n        seed_val = extract_seed(name)\n        if cond is None or seed_val is None:\n            continue\n        key = (cond, seed_val)\n        if key in seen:\n            continue\n        data = None\n        if entry.is_dir():\n            for fname in [\"classify.json\", \"taxonomy.json\"]:\n                data = load_eval_results(entry / fname)\n                if data is not None:\n                    break\n            if data is None:\n                continue\n        elif entry.is_file():\n            if name.endswith(\"_taxonomy_unified.json\"):\n                data = load_taxonomy_unified(entry)\n            elif name.endswith(\"_taxonomy_verification.json\"):\n                data = load_taxonomy_verification(entry)\n            if data is None:\n                continue\n        else:\n            continue\n        seen.add(key)\n        isr_star = None\n        if entry.is_dir():\n            eval_path = entry / \"eval_results.json\"\n            if eval_path.exists():\n                with open(eval_path) as ef:\n                    eval_raw = json.load(ef)\n                isr_star = eval_raw.get(\"summary\", {}).get(\"proved_only_mean_isr\")\n        runs.append({\"dir_name\": name, \"seed\": seed_val, \"condition\": cond,\n                      \"data\": data, \"isr_star\": isr_star})\n    return runs\n\n\ndef compute_row(run: dict) -> dict:\n    d = run[\"data\"]\n    n_proved = d.get(\"n_proved\", 0)\n    n_total = d.get(\"n_total\", 100)\n    h7 = d.get(\"h7_total_count\", 0)\n    h7_rate = d.get(\"h7_total_rate\", h7 / n_proved if n_proved > 0 else 0.0)\n    h1 = d.get(\"h1_strict_count\", 0)\n    h8 = d.get(\"h8_conjunction_collapse_count\", 0)\n    genuine = d.get(\"genuine_count\", 0)\n    genuine_rate = d.get(\"genuine_rate\", genuine / n_proved if n_proved > 0 else 0.0)\n    ci = d.get(\"content_independent_count\", 0)\n    snh = max(genuine - ci, 0)\n    snh_rate = snh / n_proved if n_proved > 0 else 0.0\n    return {\n        \"seed\": run[\"seed\"], \"condition\": run[\"condition\"], \"n_total\": n_total,\n        \"PR\": n_proved, \"H7_count\": h7, \"H7_rate\": h7_rate,\n        \"H1_count\": h1, \"H8_count\": h8,\n        \"genuine_count\": genuine, \"genuine_rate\": genuine_rate,\n        \"CI_count\": ci, \"SNH_count\": snh, \"SNH_rate\": snh_rate,\n        \"ISR_star\": run.get(\"isr_star\"),\n    }\n\n\ndef build_table(runs: list[dict]) -> pd.DataFrame:\n    rows = [compute_row(r) for r in runs]\n    df = pd.DataFrame(rows)\n    df = df.sort_values([\"condition\", \"seed\"]).reset_index(drop=True)\n    return df\n\n\n# --- Statistical tests ---\n\ndef fisher_h7_domination(df: pd.DataFrame) -> dict:\n    results = {}\n    for cond in [\"ISR\", \"RANDOM\"]:\n        sub = df[df[\"condition\"] == cond]\n        results[cond] = {\n            \"n\": len(sub),\n            \"h7_dom\": int((sub[\"H7_rate\"] >= 0.5).sum()),\n            \"not_h7_dom\": int((sub[\"H7_rate\"] < 0.5).sum()),\n        }\n    table = np.array([\n        [results[\"ISR\"][\"h7_dom\"], results[\"ISR\"][\"not_h7_dom\"]],\n        [results[\"RANDOM\"][\"h7_dom\"], results[\"RANDOM\"][\"not_h7_dom\"]],\n    ])\n    odds_ratio, p_value = stats.fisher_exact(table, alternative=\"greater\")\n\n    # 95% exact CI via scipy.stats.contingency\n    or_ci_lo, or_ci_hi = np.nan, np.nan\n    try:\n        ct = stats.contingency.odds_ratio(table)\n        ci = ct.confidence_interval(confidence_level=0.95)\n        or_ci_lo, or_ci_hi = ci.low, ci.high\n    except Exception:\n        pass\n\n    return {\n        \"table\": table.tolist(),\n        \"ISR\": results[\"ISR\"],\n        \"RANDOM\": results[\"RANDOM\"],\n        \"odds_ratio\": odds_ratio,\n        \"or_ci_lo\": or_ci_lo,\n        \"or_ci_hi\": or_ci_hi,\n        \"p_value\": p_value,\n    }\n\n\ndef permutation_test_genuine(df: pd.DataFrame, n_perm: int = 10000,\n                              rng_seed: int = 42) -> dict:\n    isr = df[df[\"condition\"] == \"ISR\"][\"genuine_rate\"].values\n    rand = df[df[\"condition\"] == \"RANDOM\"][\"genuine_rate\"].values\n    observed = isr.mean() - rand.mean()\n    pooled = np.concatenate([isr, rand])\n    n_isr = len(isr)\n    rng = np.random.default_rng(rng_seed)\n    count = 0\n    for _ in range(n_perm):\n        perm = rng.permutation(pooled)\n        if perm[:n_isr].mean() - perm[n_isr:].mean() >= observed:\n            count += 1\n    return {\n        \"observed_diff\": float(observed),\n        \"p_value\": count / n_perm,\n        \"n_perm\": n_perm,\n        \"isr_mean\": float(isr.mean()),\n        \"random_mean\": float(rand.mean()),\n    }\n\n\ndef mannwhitney_h7(df: pd.DataFrame) -> dict:\n    isr = df[df[\"condition\"] == \"ISR\"][\"H7_rate\"].values\n    rand = df[df[\"condition\"] == \"RANDOM\"][\"H7_rate\"].values\n    n1, n2 = len(isr), len(rand)\n    u_stat, p_value = stats.mannwhitneyu(isr, rand, alternative=\"greater\")\n    r_rb = 2.0 * u_stat / (n1 * n2) - 1.0 if n1 * n2 > 0 else np.nan\n    return {\n        \"U\": float(u_stat),\n        \"p_value\": float(p_value),\n        \"r_rank_biserial\": float(r_rb),\n        \"isr_median\": float(np.median(isr)),\n        \"random_median\": float(np.median(rand)),\n    }\n\n\ndef mannwhitney_isr_star(df: pd.DataFrame) -> dict | None:\n    isr = df[df[\"condition\"] == \"ISR\"][\"ISR_star\"].dropna().values.astype(float)\n    rand = df[df[\"condition\"] == \"RANDOM\"][\"ISR_star\"].dropna().values.astype(float)\n    if len(isr) < 2 or len(rand) < 2:\n        return None\n    n1, n2 = len(isr), len(rand)\n    u_stat, p_value = stats.mannwhitneyu(isr, rand, alternative=\"greater\")\n    r_rb = 2.0 * u_stat / (n1 * n2) - 1.0\n    return {\n        \"U\": float(u_stat),\n        \"p_value\": float(p_value),\n        \"r_rank_biserial\": float(r_rb),\n        \"isr_median\": float(np.median(isr)),\n        \"random_median\": float(np.median(rand)),\n        \"isr_mean\": float(np.mean(isr)),\n        \"random_mean\": float(np.mean(rand)),\n    }\n\n\ndef bca_bootstrap_ci(df: pd.DataFrame, metric: str, n_boot: int = 10000,\n                      rng_seed: int = 42) -> dict:\n    \"\"\"BCa 95% CI for per-condition means of a metric.\"\"\"\n    result = {}\n    for cond in [\"ISR\", \"RANDOM\"]:\n        vals = df[df[\"condition\"] == cond][metric].values\n        if len(vals) < 2:\n            result[cond] = {\"mean\": float(vals.mean()) if len(vals) else np.nan,\n                            \"ci_lo\": np.nan, \"ci_hi\": np.nan}\n            continue\n        res = stats.bootstrap(\n            (vals,), np.mean, n_resamples=n_boot,\n            confidence_level=0.95, method=\"BCa\",\n            random_state=np.random.default_rng(rng_seed),\n        )\n        result[cond] = {\n            \"mean\": float(vals.mean()),\n            \"ci_lo\": float(res.confidence_interval.low),\n            \"ci_hi\": float(res.confidence_interval.high),\n        }\n    return result\n\n\ndef bayes_factor_h7_domination(df: pd.DataFrame) -> dict:\n    \"\"\"BF10 for H7-domination rate difference (beta-binomial conjugate).\n    H0: ISR and Random share same domination rate.\n    H1: independent rates. Prior: Beta(1,1) on each.\n    \"\"\"\n    isr_sub = df[df[\"condition\"] == \"ISR\"]\n    rand_sub = df[df[\"condition\"] == \"RANDOM\"]\n    k_isr = int((isr_sub[\"H7_rate\"] >= 0.5).sum())\n    n_isr = len(isr_sub)\n    k_rand = int((rand_sub[\"H7_rate\"] >= 0.5).sum())\n    n_rand = len(rand_sub)\n    k_total = k_isr + k_rand\n    n_total = n_isr + n_rand\n\n    # log marginal under H0 (shared rate)\n    log_m_h0 = betaln(1 + k_total, 1 + n_total - k_total) - betaln(1, 1)\n    # log marginal under H1 (independent rates)\n    log_m_h1 = (betaln(1 + k_isr, 1 + n_isr - k_isr) - betaln(1, 1)\n                + betaln(1 + k_rand, 1 + n_rand - k_rand) - betaln(1, 1))\n    log_bf10 = log_m_h1 - log_m_h0\n    bf10 = float(np.exp(log_bf10))\n\n    return {\n        \"k_isr\": k_isr, \"n_isr\": n_isr,\n        \"k_rand\": k_rand, \"n_rand\": n_rand,\n        \"bf10\": bf10,\n        \"log_bf10\": float(log_bf10),\n        \"interpretation\": _interpret_bf(bf10),\n    }\n\n\ndef _interpret_bf(bf: float) -> str:\n    if bf > 100:\n        return \"extreme evidence for H1\"\n    if bf > 30:\n        return \"very strong evidence for H1\"\n    if bf > 10:\n        return \"strong evidence for H1\"\n    if bf > 3:\n        return \"moderate evidence for H1\"\n    if bf > 1:\n        return \"anecdotal evidence for H1\"\n    if bf > 1/3:\n        return \"anecdotal evidence (inconclusive)\"\n    if bf > 1/10:\n        return \"moderate evidence for H0\"\n    return \"strong evidence for H0\"\n\n\ndef condition_stats(df: pd.DataFrame) -> pd.DataFrame:\n    metrics = [\"PR\", \"H7_rate\", \"genuine_rate\", \"SNH_rate\"]\n    rows = []\n    for cond in [\"ISR\", \"RANDOM\"]:\n        sub = df[df[\"condition\"] == cond]\n        row = {\"condition\": cond, \"n_seeds\": len(sub)}\n        for m in metrics:\n            vals = sub[m].values\n            row[f\"{m}_mean\"] = vals.mean()\n            row[f\"{m}_std\"] = vals.std(ddof=1) if len(vals) > 1 else 0.0\n        isr_vals = sub[\"ISR_star\"].dropna().values.astype(float)\n        row[\"ISR_star_mean\"] = isr_vals.mean() if len(isr_vals) else np.nan\n        row[\"ISR_star_std\"] = isr_vals.std(ddof=1) if len(isr_vals) > 1 else 0.0\n        rows.append(row)\n    return pd.DataFrame(rows)\n\n\n# --- Formatting ---\n\ndef fmt_pct(val: float) -> str:\n    return f\"{val*100:.1f}\\\\%\"\n\ndef fmt_or(val: float) -> str:\n    return \"$\\\\infty$\" if np.isinf(val) else f\"{val:.2f}\"\n\ndef fmt_ci(lo: float, hi: float) -> str:\n    lo_s = f\"{lo:.2f}\" if not np.isnan(lo) else \"0\"\n    hi_s = \"$\\\\infty$\" if np.isinf(hi) or np.isnan(hi) else f\"{hi:.2f}\"\n    return f\"[{lo_s}, {hi_s}]\"\n\ndef fmt_p(p: float) -> str:\n    if p < 0.001:\n        return \"$<$0.001\"\n    return f\"{p:.3f}\"\n\ndef fmt_mean_std(mean: float, std: float, pct: bool = False) -> str:\n    if pct:\n        return f\"{mean*100:.1f} $\\\\pm$ {std*100:.1f}\\\\%\"\n    return f\"{mean:.1f} $\\\\pm$ {std:.1f}\"\n\ndef fmt_bca(bca: dict, pct: bool = False) -> str:\n    m = bca[\"mean\"]\n    lo, hi = bca[\"ci_lo\"], bca[\"ci_hi\"]\n    if pct:\n        return f\"{m*100:.1f}\\\\% [{lo*100:.1f}, {hi*100:.1f}]\"\n    return f\"{m:.1f} [{lo:.1f}, {hi:.1f}]\"\n\n\n# --- Console output ---\n\ndef print_per_seed_table(df: pd.DataFrame):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  PER-SEED RESULTS\")\n    print(\"=\" * 90)\n    cols = [\"condition\", \"seed\", \"PR\", \"H7_count\", \"H7_rate\", \"H1_count\",\n            \"H8_count\", \"genuine_count\", \"genuine_rate\", \"CI_count\", \"SNH_count\", \"SNH_rate\",\n            \"ISR_star\"]\n    fmt = df[cols].copy()\n    for c in [\"H7_rate\", \"genuine_rate\", \"SNH_rate\"]:\n        fmt[c] = fmt[c].apply(lambda v: f\"{v*100:.1f}%\")\n    fmt[\"ISR_star\"] = fmt[\"ISR_star\"].apply(lambda v: f\"{v:.4f}\" if pd.notna(v) else \"---\")\n    print(fmt.to_string(index=False))\n\n\ndef print_condition_stats(cond_df: pd.DataFrame):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  CONDITION-LEVEL STATISTICS (mean +/- SD)\")\n    print(\"=\" * 90)\n    for _, row in cond_df.iterrows():\n        n = int(row['n_seeds'])\n        print(f\"\\n  {row['condition']} (n={n} seeds):\")\n        print(f\"    PR:           {row['PR_mean']:.1f} +/- {row['PR_std']:.1f}\")\n        print(f\"    H7 rate:      {row['H7_rate_mean']*100:.1f} +/- {row['H7_rate_std']*100:.1f}%\")\n        print(f\"    Genuine rate: {row['genuine_rate_mean']*100:.1f} +/- {row['genuine_rate_std']*100:.1f}%\")\n        print(f\"    S-NH rate:    {row['SNH_rate_mean']*100:.1f} +/- {row['SNH_rate_std']*100:.1f}%\")\n        if not np.isnan(row.get('ISR_star_mean', np.nan)):\n            print(f\"    ISR*:         {row['ISR_star_mean']:.4f} +/- {row['ISR_star_std']:.4f}\")\n\n\ndef print_tests(fisher, perm, mw, bf, bca_h7, bca_gen, mw_isr_star=None):\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  STATISTICAL TESTS\")\n    print(\"=\" * 90)\n\n    print(\"\\n  1. H7 Domination Fisher Exact Test (H7-dominated = H7% >= 50%)\")\n    print(f\"     ISR:    {fisher['ISR']['h7_dom']} dominated / {fisher['ISR']['n']} seeds\")\n    print(f\"     RANDOM: {fisher['RANDOM']['h7_dom']} dominated / {fisher['RANDOM']['n']} seeds\")\n    print(f\"     Contingency: {fisher['table']}\")\n    or_str = \"inf\" if np.isinf(fisher['odds_ratio']) else f\"{fisher['odds_ratio']:.4f}\"\n    print(f\"     OR = {or_str}, 95% CI = [{fisher['or_ci_lo']:.4f}, {fisher['or_ci_hi']:.4f}]\"\n          if not np.isnan(fisher['or_ci_lo']) else f\"     OR = {or_str}, 95% CI = N/A\")\n    print(f\"     p-value (one-sided, greater): {fisher['p_value']:.4f}\")\n\n    print(f\"\\n  2. Genuine Rate Permutation Test (n_perm={perm['n_perm']})\")\n    print(f\"     ISR mean:    {perm['isr_mean']*100:.2f}%\")\n    print(f\"     RANDOM mean: {perm['random_mean']*100:.2f}%\")\n    print(f\"     Diff: {perm['observed_diff']*100:.2f} pp, p = {perm['p_value']:.4f}\")\n\n    print(f\"\\n  3. H7 Rate Mann-Whitney U Test\")\n    print(f\"     ISR median:    {mw['isr_median']*100:.1f}%\")\n    print(f\"     RANDOM median: {mw['random_median']*100:.1f}%\")\n    print(f\"     U = {mw['U']:.1f}, p = {mw['p_value']:.4f}\")\n    print(f\"     Rank-biserial r = {mw['r_rank_biserial']:.4f}\")\n\n    print(f\"\\n  4. Bayes Factor (H7 Domination, Beta-Binomial)\")\n    print(f\"     ISR:    {bf['k_isr']}/{bf['n_isr']} dominated\")\n    print(f\"     RANDOM: {bf['k_rand']}/{bf['n_rand']} dominated\")\n    print(f\"     BF10 = {bf['bf10']:.4f} ({bf['interpretation']})\")\n\n    print(f\"\\n  5. BCa Bootstrap 95% CI (n_boot resamples)\")\n    for label, bca in [(\"H7 rate\", bca_h7), (\"Genuine rate\", bca_gen)]:\n        print(f\"     {label}:\")\n        for cond in [\"ISR\", \"RANDOM\"]:\n            b = bca[cond]\n            print(f\"       {cond}: {b['mean']*100:.1f}% [{b['ci_lo']*100:.1f}, {b['ci_hi']*100:.1f}]\"\n                  if not np.isnan(b['ci_lo']) else f\"       {cond}: {b['mean']*100:.1f}% [N/A]\")\n\n    if mw_isr_star:\n        print(f\"\\n  6. ISR* (Proved-Only Mean ISR) Mann-Whitney U Test\")\n        print(f\"     ISR mean:    {mw_isr_star['isr_mean']:.4f}, median: {mw_isr_star['isr_median']:.4f}\")\n        print(f\"     RANDOM mean: {mw_isr_star['random_mean']:.4f}, median: {mw_isr_star['random_median']:.4f}\")\n        print(f\"     U = {mw_isr_star['U']:.1f}, p = {mw_isr_star['p_value']:.4f}\")\n        print(f\"     Rank-biserial r = {mw_isr_star['r_rank_biserial']:.4f}\")\n\n\n# --- Markdown generation (appendix-ready) ---\n\ndef generate_markdown(df: pd.DataFrame, cond_df: pd.DataFrame,\n                      fisher: dict, perm: dict, mw: dict,\n                      bf: dict, bca_h7: dict, bca_gen: dict,\n                      mw_isr_star: dict = None) -> str:\n    L = []\n    L.append(\"## D134: ISR vs Random Statistical Analysis\\n\")\n\n    # Per-seed table\n    L.append(\"### Table A1: Per-Seed Hacking Taxonomy (4B Qwen3, 500 steps)\\n\")\n    L.append(\"| Condition | Seed | PR | H7 | H7\\\\% | H1 | H8 | Genuine | Gen\\\\% | CI | S-NH | S-NH\\\\% | ISR* |\")\n    L.append(\"|:----------|-----:|---:|---:|-----:|---:|---:|--------:|------:|---:|-----:|-------:|-----:|\")\n    for _, r in df.iterrows():\n        isr_star_str = f\"{r['ISR_star']:.4f}\" if pd.notna(r.get('ISR_star')) else \"---\"\n        L.append(\n            f\"| {r['condition']} | {r['seed']} | {int(r['PR'])} | {int(r['H7_count'])} | \"\n            f\"{r['H7_rate']*100:.1f} | {int(r['H1_count'])} | {int(r['H8_count'])} | \"\n            f\"{int(r['genuine_count'])} | {r['genuine_rate']*100:.1f} | {int(r['CI_count'])} | \"\n            f\"{int(r['SNH_count'])} | {r['SNH_rate']*100:.1f} | {isr_star_str} |\"\n        )\n\n    # Condition summary with BCa CI\n    L.append(\"\\n### Table A2: Condition-Level Summary\\n\")\n    L.append(\"| Condition | $n$ | PR (mean$\\\\pm$SD) | H7\\\\% (mean$\\\\pm$SD) | H7\\\\% BCa 95\\\\% CI | Gen\\\\% (mean$\\\\pm$SD) | Gen\\\\% BCa 95\\\\% CI |\")\n    L.append(\"|:----------|----:|:------------------|:-------------------|:-----------------|:-------------------|:-----------------|\")\n    for _, r in cond_df.iterrows():\n        cond = r[\"condition\"]\n        h7_bca = bca_h7.get(cond, {})\n        gen_bca = bca_gen.get(cond, {})\n        h7_ci = f\"[{h7_bca['ci_lo']*100:.1f}, {h7_bca['ci_hi']*100:.1f}]\" if h7_bca and not np.isnan(h7_bca.get('ci_lo', np.nan)) else \"N/A\"\n        gen_ci = f\"[{gen_bca['ci_lo']*100:.1f}, {gen_bca['ci_hi']*100:.1f}]\" if gen_bca and not np.isnan(gen_bca.get('ci_lo', np.nan)) else \"N/A\"\n        L.append(\n            f\"| {cond} | {int(r['n_seeds'])} | \"\n            f\"{r['PR_mean']:.1f}$\\\\pm${r['PR_std']:.1f} | \"\n            f\"{r['H7_rate_mean']*100:.1f}$\\\\pm${r['H7_rate_std']*100:.1f} | \"\n            f\"{h7_ci} | \"\n            f\"{r['genuine_rate_mean']*100:.1f}$\\\\pm${r['genuine_rate_std']*100:.1f} | \"\n            f\"{gen_ci} |\"\n        )\n\n    # Statistical tests\n    if fisher and perm and mw and bf:\n        L.append(\"\\n### Statistical Tests\\n\")\n\n        # Fisher\n        or_str = \"$\\\\infty$\" if np.isinf(fisher['odds_ratio']) else f\"{fisher['odds_ratio']:.2f}\"\n        ci_lo = f\"{fisher['or_ci_lo']:.2f}\" if not np.isnan(fisher['or_ci_lo']) else \"0\"\n        ci_hi = \"$\\\\infty$\" if np.isinf(fisher.get('or_ci_hi', np.inf)) or np.isnan(fisher.get('or_ci_hi', np.nan)) else f\"{fisher['or_ci_hi']:.2f}\"\n        L.append(\"**1. H7 Domination Fisher Exact Test** (threshold: H7$\\\\geq$50\\\\% of proved)\")\n        L.append(f\"- ISR: {fisher['ISR']['h7_dom']}/{fisher['ISR']['n']} seeds H7-dominated; \"\n                 f\"Random: {fisher['RANDOM']['h7_dom']}/{fisher['RANDOM']['n']}\")\n        L.append(f\"- OR = {or_str}, 95\\\\% exact CI = [{ci_lo}, {ci_hi}], \"\n                 f\"$p$ = {fmt_p(fisher['p_value'])}\")\n        L.append(\"\")\n\n        # Permutation\n        L.append(f\"**2. Genuine Rate Permutation Test** ($n$ = {perm['n_perm']:,} permutations)\")\n        L.append(f\"- ISR mean: {perm['isr_mean']*100:.2f}\\\\%, Random mean: {perm['random_mean']*100:.2f}\\\\%\")\n        L.append(f\"- $\\\\Delta$ = {perm['observed_diff']*100:.2f} pp, $p$ = {fmt_p(perm['p_value'])}\")\n        L.append(\"\")\n\n        # Mann-Whitney\n        L.append(\"**3. H7 Rate Mann-Whitney $U$ Test**\")\n        L.append(f\"- ISR median: {mw['isr_median']*100:.1f}\\\\%, Random median: {mw['random_median']*100:.1f}\\\\%\")\n        L.append(f\"- $U$ = {mw['U']:.1f}, $p$ = {fmt_p(mw['p_value'])}, \"\n                 f\"rank-biserial $r$ = {mw['r_rank_biserial']:.3f}\")\n        L.append(\"\")\n\n        # Bayes Factor\n        L.append(\"**4. Bayes Factor** (Beta-Binomial conjugate, prior: Beta(1,1))\")\n        L.append(f\"- $BF_{{10}}$ = {bf['bf10']:.2f} ({bf['interpretation']})\")\n        L.append(f\"- ISR: {bf['k_isr']}/{bf['n_isr']} H7-dominated, \"\n                 f\"Random: {bf['k_rand']}/{bf['n_rand']}\")\n\n        if mw_isr_star:\n            L.append(\"\")\n            L.append(\"**5. ISR* (Proved-Only Mean ISR) Mann-Whitney $U$ Test**\")\n            L.append(f\"- ISR mean: {mw_isr_star['isr_mean']:.4f}, median: {mw_isr_star['isr_median']:.4f}\")\n            L.append(f\"- Random mean: {mw_isr_star['random_mean']:.4f}, median: {mw_isr_star['random_median']:.4f}\")\n            L.append(f\"- $U$ = {mw_isr_star['U']:.1f}, $p$ = {fmt_p(mw_isr_star['p_value'])}, \"\n                     f\"rank-biserial $r$ = {mw_isr_star['r_rank_biserial']:.3f}\")\n\n    return \"\\n\".join(L) + \"\\n\"\n\n\n# --- Main ---\n\ndef main():\n    args = parse_args()\n    data_dir = Path(args.data_dir)\n\n    if not data_dir.exists():\n        print(f\"ERROR: data directory {data_dir} does not exist\", file=sys.stderr)\n        sys.exit(1)\n\n    if args.prefix:\n        prefixes = [args.prefix]\n    elif args.prefixes:\n        prefixes = [p.strip() for p in args.prefixes.split(\",\")]\n    else:\n        prefixes = MODE_PREFIXES[args.mode]\n    print(f\"Mode: {args.mode} | Prefixes: {prefixes}\")\n\n    runs = discover_runs(data_dir, prefixes)\n    if not runs:\n        print(f\"ERROR: no runs found in {data_dir} with prefixes {prefixes}\", file=sys.stderr)\n        sys.exit(1)\n\n    isr_count = sum(1 for r in runs if r[\"condition\"] == \"ISR\")\n    rand_count = sum(1 for r in runs if r[\"condition\"] == \"RANDOM\")\n    print(f\"Found {len(runs)} runs: {isr_count} ISR, {rand_count} RANDOM\")\n    for r in runs:\n        print(f\"  {r['condition']:6s} s{r['seed']} <- {r['dir_name']}\")\n\n    df = build_table(runs)\n    print_per_seed_table(df)\n\n    cond_df = condition_stats(df)\n    print_condition_stats(cond_df)\n\n    if isr_count < 2 or rand_count < 2:\n        print(\"\\nWARNING: need >= 2 seeds per condition for statistical tests, skipping.\",\n              file=sys.stderr)\n        bca_h7 = bca_bootstrap_ci(df, \"H7_rate\", args.n_boot, args.seed)\n        bca_gen = bca_bootstrap_ci(df, \"genuine_rate\", args.n_boot, args.seed)\n        if args.output:\n            md = generate_markdown(df, cond_df, {}, {}, {}, {}, bca_h7, bca_gen)\n            Path(args.output).write_text(md)\n            print(f\"\\nMarkdown written to {args.output}\")\n        return\n\n    fisher = fisher_h7_domination(df)\n    perm = permutation_test_genuine(df, n_perm=args.n_perm, rng_seed=args.seed)\n    mw = mannwhitney_h7(df)\n    bf = bayes_factor_h7_domination(df)\n    bca_h7 = bca_bootstrap_ci(df, \"H7_rate\", args.n_boot, args.seed)\n    bca_gen = bca_bootstrap_ci(df, \"genuine_rate\", args.n_boot, args.seed)\n    mw_isr_star = mannwhitney_isr_star(df)\n\n    print_tests(fisher, perm, mw, bf, bca_h7, bca_gen, mw_isr_star)\n\n    md = generate_markdown(df, cond_df, fisher, perm, mw, bf, bca_h7, bca_gen, mw_isr_star)\n    print(\"\\n\" + \"=\" * 90)\n    print(\"  MARKDOWN OUTPUT (appendix-ready)\")\n    print(\"=\" * 90)\n    print(md)\n\n    if args.output:\n        Path(args.output).parent.mkdir(parents=True, exist_ok=True)\n        Path(args.output).write_text(md)\n        print(f\"Markdown written to {args.output}\")\n\n\nif __name__ == \"__main__\":\n    main()\nHEREDOC_EOF\necho \"DONE: $(wc -l < /root/solver-trace-ablation/scripts/d134_analysis.py) lines\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "bcdc5398-8f0a-46da-b701-b14eb0da8930",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GM1AD6Cexa62kgg6bEjA6H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11212,
      "cache_read_input_tokens": 68555,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11212
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

_source line 87 · 2026-05-18T23:39:37.131Z_

<details><summary>↩ Tool result · `toolu_01Abx3QWAn2c77uCvLDMfmqj`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"DONE: 640 lines\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "f68c347c-ff13-48a6-aaef-df4889abca29",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"DONE: 640 lines\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.5}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"DONE: 640 lines\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 88_

File deployed (640 lines, matches local). Now running.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "475527d5-ce57-492f-9d31-6acc2bed467d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SLzVVtN4mvKMdAcXGoqaau",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10182,
      "cache_read_input_tokens": 79767,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10182
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

_source line 89_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01GP8SMSriXE6ETvyvB3Wgkt`</summary>

```json
{
  "server": "westd-39279",
  "account": "root",
  "command": "cd /root/solver-trace-ablation && /root/miniconda3/bin/python3 scripts/d134_analysis.py --mode d134_only 2>&1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "3550ac3f-ff40-4bea-9116-4dd3d57bf0e6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SLzVVtN4mvKMdAcXGoqaau",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10182,
      "cache_read_input_tokens": 79767,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10182
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

_source line 90 · 2026-05-18T23:39:43.837Z_

<details><summary>↩ Tool result · `toolu_01GP8SMSriXE6ETvyvB3Wgkt`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"Mode: d134_only | Prefixes: ['d134_4b']\\nFound 8 runs: 5 ISR, 3 RANDOM\\n  ISR    s47 <- d134_4b_isr_b01_s47\\n  ISR    s48 <- d134_4b_isr_b01_s48\\n  ISR    s49 <- d134_4b_isr_b01_s49\\n  ISR    s50 <- d134_4b_isr_b01_s50\\n  ISR    s51 <- d134_4b_isr_b01_s51\\n  RANDOM s47 <- d134_4b_random_b01_s47\\n  RANDOM s48 <- d134_4b_random_b01_s48\\n  RANDOM s49 <- d134_4b_random_b01_s49\\n\\n==========================================================================================\\n  PER-SEED RESULTS\\n==========================================================================================\\ncondition  seed  PR  H7_count H7_rate  H1_count  H8_count  genuine_count genuine_rate  CI_count  SNH_count SNH_rate ISR_star\\n      ISR    47  97        83   85.6%         1        10              3         3.1%         8          0     0.0%   0.5670\\n      ISR    48  66        66  100.0%         0         0              0         0.0%         2          0     0.0%   0.7462\\n      ISR    49  86        73   84.9%         6         6              1         1.2%         0          1     1.2%   0.5339\\n      ISR    50  98        84   85.7%         0         8              6         6.1%         2          4     4.1%   0.7274\\n      ISR    51  98        96   98.0%         0         1              1         1.0%         0          1     1.0%   0.7134\\n   RANDOM    47  89         0    0.0%        79         4              6         6.7%         4          2     2.2%   0.0963\\n   RANDOM    48  93         3    3.2%        75        14              4         4.3%         5          0     0.0%   0.0625\\n   RANDOM    49   5         1   20.0%         4         0              0         0.0%         0          0     0.0%   0.1143\\n\\n==========================================================================================\\n  CONDITION-LEVEL STATISTICS (mean +/- SD)\\n==========================================================================================\\n\\n  ISR (n=5 seeds):\\n    PR:           89.0 +/- 13.8\\n    H7 rate:      90.8 +/- 7.5%\\n    Genuine rate: 2.3 +/- 2.4%\\n    S-NH rate:    1.3 +/- 1.7%\\n    ISR*:         0.6576 +/- 0.0992\\n\\n  RANDOM (n=3 seeds):\\n    PR:           62.3 +/- 49.7\\n    H7 rate:      7.7 +/- 10.7%\\n    Genuine rate: 3.7 +/- 3.4%\\n    S-NH rate:    0.7 +/- 1.3%\\n    ISR*:         0.0910 +/- 0.0263\\n\\n==========================================================================================\\n  STATISTICAL TESTS\\n==========================================================================================\\n\\n  1. H7 Domination Fisher Exact Test (H7-dominated = H7% >= 50%)\\n     ISR:    5 dominated / 5 seeds\\n     RANDOM: 0 dominated / 3 seeds\\n     Contingency: [[5, 0], [0, 3]]\\n     OR = inf, 95% CI = [1.2020, inf]\\n     p-value (one-sided, greater): 0.0179\\n\\n  2. Genuine Rate Permutation Test (n_perm=10000)\\n     ISR mean:    2.28%\\n     RANDOM mean: 3.68%\\n     Diff: -1.40 pp, p = 0.7845\\n\\n  3. H7 Rate Mann-Whitney U Test\\n     ISR median:    85.7%\\n     RANDOM median: 3.2%\\n     U = 15.0, p = 0.0179\\n     Rank-biserial r = 1.0000\\n\\n  4. Bayes Factor (H7 Domination, Beta-Binomial)\\n     ISR:    5/5 dominated\\n     RANDOM: 0/3 dominated\\n     BF10 = 21.0000 (strong evidence for H1)\\n\\n  5. BCa Bootstrap 95% CI (n_boot resamples)\\n     H7 rate:\\n       ISR: 90.8% [85.4, 96.7]\\n       RANDOM: 7.7% [1.1, 20.0]\\n     Genuine rate:\\n       ISR: 2.3% [0.7, 4.9]\\n       RANDOM: 3.7% [0.0, 5.9]\\n\\n  6. ISR* (Proved-Only Mean ISR) Mann-Whitney U Test\\n     ISR mean:    0.6576, median: 0.7134\\n     RANDOM mean: 0.0910, median: 0.0963\\n     U = 15.0, p = 0.0179\\n     Rank-biserial r = 1.0000\\n\\n==========================================================================================\\n  MARKDOWN OUTPUT (appendix-ready)\\n==========================================================================================\\n## D134: ISR vs Random Statistical Analysis\\n\\n### Table A1: Per-Seed Hacking Taxonomy (4B Qwen3, 500 steps)\\n\\n| Condition | Seed | PR | H7 | H7\\\\% | H1 | H8 | Genuine | Gen\\\\% | CI | S-NH | S-NH\\\\% | ISR* |\\n|:----------|-----:|---:|---:|-----:|---:|---:|--------:|------:|---:|-----:|-------:|-----:|\\n| ISR | 47 | 97 | 83 | 85.6 | 1 | 10 | 3 | 3.1 | 8 | 0 | 0.0 | 0.5670 |\\n| ISR | 48 | 66 | 66 | 100.0 | 0 | 0 | 0 | 0.0 | 2 | 0 | 0.0 | 0.7462 |\\n| ISR | 49 | 86 | 73 | 84.9 | 6 | 6 | 1 | 1.2 | 0 | 1 | 1.2 | 0.5339 |\\n| ISR | 50 | 98 | 84 | 85.7 | 0 | 8 | 6 | 6.1 | 2 | 4 | 4.1 | 0.7274 |\\n| ISR | 51 | 98 | 96 | 98.0 | 0 | 1 | 1 | 1.0 | 0 | 1 | 1.0 | 0.7134 |\\n| RANDOM | 47 | 89 | 0 | 0.0 | 79 | 4 | 6 | 6.7 | 4 | 2 | 2.2 | 0.0963 |\\n| RANDOM | 48 | 93 | 3 | 3.2 | 75 | 14 | 4 | 4.3 | 5 | 0 | 0.0 | 0.0625 |\\n| RANDOM | 49 | 5 | 1 | 20.0 | 4 | 0 | 0 | 0.0 | 0 | 0 | 0.0 | 0.1143 |\\n\\n### Table A2: Condition-Level Summary\\n\\n| Condition | $n$ | PR (mean$\\\\pm$SD) | H7\\\\% (mean$\\\\pm$SD) | H7\\\\% BCa 95\\\\% CI | Gen\\\\% (mean$\\\\pm$SD) | Gen\\\\% BCa 95\\\\% CI |\\n|:----------|----:|:------------------|:-------------------|:-----------------|:-------------------|:-----------------|\\n| ISR | 5 | 89.0$\\\\pm$13.8 | 90.8$\\\\pm$7.5 | [85.4, 96.7] | 2.3$\\\\pm$2.4 | [0.7, 4.9] |\\n| RANDOM | 3 | 62.3$\\\\pm$49.7 | 7.7$\\\\pm$10.7 | [1.1, 20.0] | 3.7$\\\\pm$3.4 | [0.0, 5.9] |\\n\\n### Statistical Tests\\n\\n**1. H7 Domination Fisher Exact Test** (threshold: H7$\\\\geq$50\\\\% of proved)\\n- ISR: 5/5 seeds H7-dominated; Random: 0/3\\n- OR = $\\\\infty$, 95\\\\% exact CI = [1.20, $\\\\infty$], $p$ = 0.018\\n\\n**2. Genuine Rate Permutation Test** ($n$ = 10,000 permutations)\\n- ISR mean: 2.28\\\\%, Random mean: 3.68\\\\%\\n- $\\\\Delta$ = -1.40 pp, $p$ = 0.784\\n\\n**3. H7 Rate Mann-Whitney $U$ Test**\\n- ISR median: 85.7\\\\%, Random median: 3.2\\\\%\\n- $U$ = 15.0, $p$ = 0.018, rank-biserial $r$ = 1.000\\n\\n**4. Bayes Factor** (Beta-Binomial conjugate, prior: Beta(1,1))\\n- $BF_{10}$ = 21.00 (strong evidence for H1)\\n- ISR: 5/5 H7-dominated, Random: 0/3\\n\\n**5. ISR* (Proved-Only Mean ISR) Mann-Whitney $U$ Test**\\n- ISR mean: 0.6576, median: 0.7134\\n- Random mean: 0.0910, median: 0.0963\\n- $U$ = 15.0, $p$ = 0.018, rank-biserial $r$ = 1.000\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.58}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "026c682a-fe68-4dbd-aaf5-65b651b3d4de",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"Mode: d134_only | Prefixes: ['d134_4b']\\\\nFound 8 runs: 5 ISR, 3 RANDOM\\\\n  ISR    s47 <- d134_4b_isr_b01_s47\\\\n  ISR    s48 <- d134_4b_isr_b01_s48\\\\n  ISR    s49 <- d134_4b_isr_b01_s49\\\\n  ISR    s50 <- d134_4b_isr_b01_s50\\\\n  ISR    s51 <- d134_4b_isr_b01_s51\\\\n  RANDOM s47 <- d134_4b_random_b01_s47\\\\n  RANDOM s48 <- d134_4b_random_b01_s48\\\\n  RANDOM s49 <- d134_4b_random_b01_s49\\\\n\\\\n==========================================================================================\\\\n  PER-SEED RESULTS\\\\n==========================================================================================\\\\ncondition  seed  PR  H7_count H7_rate  H1_count  H8_count  genuine_count genuine_rate  CI_count  SNH_count SNH_rate ISR_star\\\\n      ISR    47  97        83   85.6%         1        10              3         3.1%         8          0     0.0%   0.5670\\\\n      ISR    48  66        66  100.0%         0         0              0         0.0%         2          0     0.0%   0.7462\\\\n      ISR    49  86        73   84.9%         6         6              1         1.2%         0          1     1.2%   0.5339\\\\n      ISR    50  98        84   85.7%         0         8              6         6.1%         2          4     4.1%   0.7274\\\\n      ISR    51  98        96   98.0%         0         1              1         1.0%         0          1     1.0%   0.7134\\\\n   RANDOM    47  89         0    0.0%        79         4              6         6.7%         4          2     2.2%   0.0963\\\\n   RANDOM    48  93         3    3.2%        75        14              4         4.3%         5          0     0.0%   0.0625\\\\n   RANDOM    49   5         1   20.0%         4         0              0         0.0%         0          0     0.0%   0.1143\\\\n\\\\n==========================================================================================\\\\n  CONDITION-LEVEL STATISTICS (mean +/- SD)\\\\n==========================================================================================\\\\n\\\\n  ISR (n=5 seeds):\\\\n    PR:           89.0 +/- 13.8\\\\n    H7 rate:      90.8 +/- 7.5%\\\\n    Genuine rate: 2.3 +/- 2.4%\\\\n    S-NH rate:    1.3 +/- 1.7%\\\\n    ISR*:         0.6576 +/- 0.0992\\\\n\\\\n  RANDOM (n=3 seeds):\\\\n    PR:           62.3 +/- 49.7\\\\n    H7 rate:      7.7 +/- 10.7%\\\\n    Genuine rate: 3.7 +/- 3.4%\\\\n    S-NH rate:    0.7 +/- 1.3%\\\\n    ISR*:         0.0910 +/- 0.0263\\\\n\\\\n==========================================================================================\\\\n  STATISTICAL TESTS\\\\n==========================================================================================\\\\n\\\\n  1. H7 Domination Fisher Exact Test (H7-dominated = H7% >= 50%)\\\\n     ISR:    5 dominated / 5 seeds\\\\n     RANDOM: 0 dominated / 3 seeds\\\\n     Contingency: [[5, 0], [0, 3]]\\\\n     OR = inf, 95% CI = [1.2020, inf]\\\\n     p-value (one-sided, greater): 0.0179\\\\n\\\\n  2. Genuine Rate Permutation Test (n_perm=10000)\\\\n     ISR mean:    2.28%\\\\n     RANDOM mean: 3.68%\\\\n     Diff: -1.40 pp, p = 0.7845\\\\n\\\\n  3. H7 Rate Mann-Whitney U Test\\\\n     ISR median:    85.7%\\\\n     RANDOM median: 3.2%\\\\n     U = 15.0, p = 0.0179\\\\n     Rank-biserial r = 1.0000\\\\n\\\\n  4. Bayes Factor (H7 Domination, Beta-Binomial)\\\\n     ISR:    5/5 dominated\\\\n     RANDOM: 0/3 dominated\\\\n     BF10 = 21.0000 (strong evidence for H1)\\\\n\\\\n  5. BCa Bootstrap 95% CI (n_boot resamples)\\\\n     H7 rate:\\\\n       ISR: 90.8% [85.4, 96.7]\\\\n       RANDOM: 7.7% [1.1, 20.0]\\\\n     Genuine rate:\\\\n       ISR: 2.3% [0.7, 4.9]\\\\n       RANDOM: 3.7% [0.0, 5.9]\\\\n\\\\n  6. ISR* (Proved-Only Mean ISR) Mann-Whitney U Test\\\\n     ISR mean:    0.6576, median: 0.7134\\\\n     RANDOM mean: 0.0910, median: 0.0963\\\\n     U = 15.0, p = 0.0179\\\\n     Rank-biserial r = 1.0000\\\\n\\\\n==========================================================================================\\\\n  MARKDOWN OUTPUT (appendix-ready)\\\\n==========================================================================================\\\\n## D134: ISR vs Random Statistical Analysis\\\\n\\\\n### Table A1: Per-Seed Hacking Taxonomy (4B Qwen3, 500 steps)\\\\n\\\\n| Condition | Seed | PR | H7 | H7\\\\\\\\% | H1 | H8 | Genuine | Gen\\\\\\\\% | CI | S-NH | S-NH\\\\\\\\% | ISR* |\\\\n|:----------|-----:|---:|---:|-----:|---:|---:|--------:|------:|---:|-----:|-------:|-----:|\\\\n| ISR | 47 | 97 | 83 | 85.6 | 1 | 10 | 3 | 3.1 | 8 | 0 | 0.0 | 0.5670 |\\\\n| ISR | 48 | 66 | 66 | 100.0 | 0 | 0 | 0 | 0.0 | 2 | 0 | 0.0 | 0.7462 |\\\\n| ISR | 49 | 86 | 73 | 84.9 | 6 | 6 | 1 | 1.2 | 0 | 1 | 1.2 | 0.5339 |\\\\n| ISR | 50 | 98 | 84 | 85.7 | 0 | 8 | 6 | 6.1 | 2 | 4 | 4.1 | 0.7274 |\\\\n| ISR | 51 | 98 | 96 | 98.0 | 0 | 1 | 1 | 1.0 | 0 | 1 | 1.0 | 0.7134 |\\\\n| RANDOM | 47 | 89 | 0 | 0.0 | 79 | 4 | 6 | 6.7 | 4 | 2 | 2.2 | 0.0963 |\\\\n| RANDOM | 48 | 93 | 3 | 3.2 | 75 | 14 | 4 | 4.3 | 5 | 0 | 0.0 | 0.0625 |\\\\n| RANDOM | 49 | 5 | 1 | 20.0 | 4 | 0 | 0 | 0.0 | 0 | 0 | 0.0 | 0.1143 |\\\\n\\\\n### Table A2: Condition-Level Summary\\\\n\\\\n| Condition | $n$ | PR (mean$\\\\\\\\pm$SD) | H7\\\\\\\\% (mean$\\\\\\\\pm$SD) | H7\\\\\\\\% BCa 95\\\\\\\\% CI | Gen\\\\\\\\% (mean$\\\\\\\\pm$SD) | Gen\\\\\\\\% BCa 95\\\\\\\\% CI |\\\\n|:----------|----:|:------------------|:-------------------|:-----------------|:-------------------|:-----------------|\\\\n| ISR | 5 | 89.0$\\\\\\\\pm$13.8 | 90.8$\\\\\\\\pm$7.5 | [85.4, 96.7] | 2.3$\\\\\\\\pm$2.4 | [0.7, 4.9] |\\\\n| RANDOM | 3 | 62.3$\\\\\\\\pm$49.7 | 7.7$\\\\\\\\pm$10.7 | [1.1, 20.0] | 3.7$\\\\\\\\pm$3.4 | [0.0, 5.9] |\\\\n\\\\n### Statistical Tests\\\\n\\\\n**1. H7 Domination Fisher Exact Test** (threshold: H7$\\\\\\\\geq$50\\\\\\\\% of proved)\\\\n- ISR: 5/5 seeds H7-dominated; Random: 0/3\\\\n- OR = $\\\\\\\\infty$, 95\\\\\\\\% exact CI = [1.20, $\\\\\\\\infty$], $p$ = 0.018\\\\n\\\\n**2. Genuine Rate Permutation Test** ($n$ = 10,000 permutations)\\\\n- ISR mean: 2.28\\\\\\\\%, Random mean: 3.68\\\\\\\\%\\\\n- $\\\\\\\\Delta$ = -1.40 pp, $p$ = 0.784\\\\n\\\\n**3. H7 Rate Mann-Whitney $U$ Test**\\\\n- ISR median: 85.7\\\\\\\\%, Random median: 3.2\\\\\\\\%\\\\n- $U$ = 15.0, $p$ = 0.018, rank-biserial $r$ = 1.000\\\\n\\\\n**4. Bayes Factor** (Beta-Binomial conjugate, prior: Beta(1,1))\\\\n- $BF_{10}$ = 21.00 (strong evidence for H1)\\\\n- ISR: 5/5 H7-dominated, Random: 0/3\\\\n\\\\n**5. ISR* (Proved-Only Mean ISR) Mann-Whitney $U$ Test**\\\\n- ISR mean: 0.6576, median: 0.7134\\\\n- Random mean: 0.0910, median: 0.0963\\\\n- $U$ = 15.0, $p$ = 0.018, rank-biserial $r$ = 1.000\\\\n\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.58}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"Mode: d134_only | Prefixes: ['d134_4b']\\nFound 8 runs: 5 ISR, 3 RANDOM\\n  ISR    s47 <- d134_4b_isr_b01_s47\\n  ISR    s48 <- d134_4b_isr_b01_s48\\n  ISR    s49 <- d134_4b_isr_b01_s49\\n  ISR    s50 <- d134_4b_isr_b01_s50\\n  ISR    s51 <- d134_4b_isr_b01_s51\\n  RANDOM s47 <- d134_4b_random_b01_s47\\n  RANDOM s48 <- d134_4b_random_b01_s48\\n  RANDOM s49 <- d134_4b_random_b01_s49\\n\\n==========================================================================================\\n  PER-SEED RESULTS\\n==========================================================================================\\ncondition  seed  PR  H7_count H7_rate  H1_count  H8_count  genuine_count genuine_rate  CI_count  SNH_count SNH_rate ISR_star\\n      ISR    47  97        83   85.6%         1        10              3         3.1%         8          0     0.0%   0.5670\\n      ISR    48  66        66  100.0%         0         0              0         0.0%         2          0     0.0%   0.7462\\n      ISR    49  86        73   84.9%         6         6              1         1.2%         0          1     1.2%   0.5339\\n      ISR    50  98        84   85.7%         0         8              6         6.1%         2          4     4.1%   0.7274\\n      ISR    51  98        96   98.0%         0         1              1         1.0%         0          1     1.0%   0.7134\\n   RANDOM    47  89         0    0.0%        79         4              6         6.7%         4          2     2.2%   0.0963\\n   RANDOM    48  93         3    3.2%        75        14              4         4.3%         5          0     0.0%   0.0625\\n   RANDOM    49   5         1   20.0%         4         0              0         0.0%         0          0     0.0%   0.1143\\n\\n==========================================================================================\\n  CONDITION-LEVEL STATISTICS (mean +/- SD)\\n==========================================================================================\\n\\n  ISR (n=5 seeds):\\n    PR:           89.0 +/- 13.8\\n    H7 rate:      90.8 +/- 7.5%\\n    Genuine rate: 2.3 +/- 2.4%\\n    S-NH rate:    1.3 +/- 1.7%\\n    ISR*:         0.6576 +/- 0.0992\\n\\n  RANDOM (n=3 seeds):\\n    PR:           62.3 +/- 49.7\\n    H7 rate:      7.7 +/- 10.7%\\n    Genuine rate: 3.7 +/- 3.4%\\n    S-NH rate:    0.7 +/- 1.3%\\n    ISR*:         0.0910 +/- 0.0263\\n\\n==========================================================================================\\n  STATISTICAL TESTS\\n==========================================================================================\\n\\n  1. H7 Domination Fisher Exact Test (H7-dominated = H7% >= 50%)\\n     ISR:    5 dominated / 5 seeds\\n     RANDOM: 0 dominated / 3 seeds\\n     Contingency: [[5, 0], [0, 3]]\\n     OR = inf, 95% CI = [1.2020, inf]\\n     p-value (one-sided, greater): 0.0179\\n\\n  2. Genuine Rate Permutation Test (n_perm=10000)\\n     ISR mean:    2.28%\\n     RANDOM mean: 3.68%\\n     Diff: -1.40 pp, p = 0.7845\\n\\n  3. H7 Rate Mann-Whitney U Test\\n     ISR median:    85.7%\\n     RANDOM median: 3.2%\\n     U = 15.0, p = 0.0179\\n     Rank-biserial r = 1.0000\\n\\n  4. Bayes Factor (H7 Domination, Beta-Binomial)\\n     ISR:    5/5 dominated\\n     RANDOM: 0/3 dominated\\n     BF10 = 21.0000 (strong evidence for H1)\\n\\n  5. BCa Bootstrap 95% CI (n_boot resamples)\\n     H7 rate:\\n       ISR: 90.8% [85.4, 96.7]\\n       RANDOM: 7.7% [1.1, 20.0]\\n     Genuine rate:\\n       ISR: 2.3% [0.7, 4.9]\\n       RANDOM: 3.7% [0.0, 5.9]\\n\\n  6. ISR* (Proved-Only Mean ISR) Mann-Whitney U Test\\n     ISR mean:    0.6576, median: 0.7134\\n     RANDOM mean: 0.0910, median: 0.0963\\n     U = 15.0, p = 0.0179\\n     Rank-biserial r = 1.0000\\n\\n==========================================================================================\\n  MARKDOWN OUTPUT (appendix-ready)\\n==========================================================================================\\n## D134: ISR vs Random Statistical Analysis\\n\\n### Table A1: Per-Seed Hacking Taxonomy (4B Qwen3, 500 steps)\\n\\n| Condition | Seed | PR | H7 | H7\\\\% | H1 | H8 | Genuine | Gen\\\\% | CI | S-NH | S-NH\\\\% | ISR* |\\n|:----------|-----:|---:|---:|-----:|---:|---:|--------:|------:|---:|-----:|-------:|-----:|\\n| ISR | 47 | 97 | 83 | 85.6 | 1 | 10 | 3 | 3.1 | 8 | 0 | 0.0 | 0.5670 |\\n| ISR | 48 | 66 | 66 | 100.0 | 0 | 0 | 0 | 0.0 | 2 | 0 | 0.0 | 0.7462 |\\n| ISR | 49 | 86 | 73 | 84.9 | 6 | 6 | 1 | 1.2 | 0 | 1 | 1.2 | 0.5339 |\\n| ISR | 50 | 98 | 84 | 85.7 | 0 | 8 | 6 | 6.1 | 2 | 4 | 4.1 | 0.7274 |\\n| ISR | 51 | 98 | 96 | 98.0 | 0 | 1 | 1 | 1.0 | 0 | 1 | 1.0 | 0.7134 |\\n| RANDOM | 47 | 89 | 0 | 0.0 | 79 | 4 | 6 | 6.7 | 4 | 2 | 2.2 | 0.0963 |\\n| RANDOM | 48 | 93 | 3 | 3.2 | 75 | 14 | 4 | 4.3 | 5 | 0 | 0.0 | 0.0625 |\\n| RANDOM | 49 | 5 | 1 | 20.0 | 4 | 0 | 0 | 0.0 | 0 | 0 | 0.0 | 0.1143 |\\n\\n### Table A2: Condition-Level Summary\\n\\n| Condition | $n$ | PR (mean$\\\\pm$SD) | H7\\\\% (mean$\\\\pm$SD) | H7\\\\% BCa 95\\\\% CI | Gen\\\\% (mean$\\\\pm$SD) | Gen\\\\% BCa 95\\\\% CI |\\n|:----------|----:|:------------------|:-------------------|:-----------------|:-------------------|:-----------------|\\n| ISR | 5 | 89.0$\\\\pm$13.8 | 90.8$\\\\pm$7.5 | [85.4, 96.7] | 2.3$\\\\pm$2.4 | [0.7, 4.9] |\\n| RANDOM | 3 | 62.3$\\\\pm$49.7 | 7.7$\\\\pm$10.7 | [1.1, 20.0] | 3.7$\\\\pm$3.4 | [0.0, 5.9] |\\n\\n### Statistical Tests\\n\\n**1. H7 Domination Fisher Exact Test** (threshold: H7$\\\\geq$50\\\\% of proved)\\n- ISR: 5/5 seeds H7-dominated; Random: 0/3\\n- OR = $\\\\infty$, 95\\\\% exact CI = [1.20, $\\\\infty$], $p$ = 0.018\\n\\n**2. Genuine Rate Permutation Test** ($n$ = 10,000 permutations)\\n- ISR mean: 2.28\\\\%, Random mean: 3.68\\\\%\\n- $\\\\Delta$ = -1.40 pp, $p$ = 0.784\\n\\n**3. H7 Rate Mann-Whitney $U$ Test**\\n- ISR median: 85.7\\\\%, Random median: 3.2\\\\%\\n- $U$ = 15.0, $p$ = 0.018, rank-biserial $r$ = 1.000\\n\\n**4. Bayes Factor** (Beta-Binomial conjugate, prior: Beta(1,1))\\n- $BF_{10}$ = 21.00 (strong evidence for H1)\\n- ISR: 5/5 H7-dominated, Random: 0/3\\n\\n**5. ISR* (Proved-Only Mean ISR) Mann-Whitney $U$ Test**\\n- ISR mean: 0.6576, median: 0.7134\\n- Random mean: 0.0910, median: 0.0963\\n- $U$ = 15.0, $p$ = 0.018, rank-biserial $r$ = 1.000\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.58}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 91_

全部通过。

## 报告

### 修改内容

| 位置 | 改动 |
|------|------|
| `discover_runs` (L152-159) | 加载 `eval_results.json`，提取 `summary.proved_only_mean_isr` |
| `compute_row` (L184) | 返回值增加 `ISR_star` 字段 |
| `mannwhitney_isr_star` (L269-285) | 新增函数：ISR* Mann-Whitney U 检验 |
| `condition_stats` (L370-372) | 增加 ISR* mean/std 计算 |
| `print_per_seed_table` (L414-420) | 表格增加 ISR* 列 |
| `print_condition_stats` (L435-436) | 输出增加 ISR* 行 |
| `print_tests` (L439, L477-482) | 增加第 6 项 ISR* MW 输出 |
| `generate_markdown` (L490, L560-566) | Table A1 增加 ISR* 列 + 第 5 项 ISR* MW |
| `main` (L623, L625, L627) | 调用 `mannwhitney_isr_star` 并传递 |

### ISR* 字段名
`summary.proved_only_mean_isr`

### Per-seed ISR* 值

| Condition | Seed | ISR* |
|-----------|------|------|
| ISR | 47 | 0.5670 |
| ISR | 48 | 0.7462 |
| ISR | 49 | 0.5339 |
| ISR | 50 | 0.7274 |
| ISR | 51 | 0.7134 |
| RANDOM | 47 | 0.0963 |
| RANDOM | 48 | 0.0625 |
| RANDOM | 49 | 0.1143 |

### ISR* 条件统计
- ISR mean: 0.6576 +/- 0.0992
- RANDOM mean: 0.0910 +/- 0.0263

### ISR* Mann-Whitney U 结果
- U = 15.0, p = 0.0179, rank-biserial r = 1.000
- 完全分离（所有 ISR seed 的 ISR* 都高于所有 Random seed）

### 原有功能验证
Fisher (p=0.0179), H7 MW (U=15.0, p=0.0179), Permutation (p=0.7845), BF10 (21.00) 均正常输出，无回归。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "uuid": "971941cb-b133-48c5-84fc-5d332fe49d38",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0135eJU5RioVYE9trBH8sS4R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3132,
      "cache_read_input_tokens": 89949,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3132
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

_source line 92_

全部通过。

## 报告

### 修改内容

| 位置 | 改动 |
|------|------|
| `discover_runs` (L152-159) | 加载 `eval_results.json`，提取 `summary.proved_only_mean_isr` |
| `compute_row` (L184) | 返回值增加 `ISR_star` 字段 |
| `mannwhitney_isr_star` (L269-285) | 新增函数：ISR* Mann-Whitney U 检验 |
| `condition_stats` (L370-372) | 增加 ISR* mean/std 计算 |
| `print_per_seed_table` (L414-420) | 表格增加 ISR* 列 |
| `print_condition_stats` (L435-436) | 输出增加 ISR* 行 |
| `print_tests` (L439, L477-482) | 增加第 6 项 ISR* MW 输出 |
| `generate_markdown` (L490, L560-566) | Table A1 增加 ISR* 列 + 第 5 项 ISR* MW |
| `main` (L623, L625, L627) | 调用 `mannwhitney_isr_star` 并传递 |

### ISR* 字段名
`summary.proved_only_mean_isr`

### Per-seed ISR* 值

| Condition | Seed | ISR* |
|-----------|------|------|
| ISR | 47 | 0.5670 |
| ISR | 48 | 0.7462 |
| ISR | 49 | 0.5339 |
| ISR | 50 | 0.7274 |
| ISR | 51 | 0.7134 |
| RANDOM | 47 | 0.0963 |
| RANDOM | 48 | 0.0625 |
| RANDOM | 49 | 0.1143 |

### ISR* 条件统计
- ISR mean: 0.6576 +/- 0.0992
- RANDOM mean: 0.0910 +/- 0.0263

### ISR* Mann-Whitney U 结果
- U = 15.0, p = 0.0179, rank-biserial r = 1.000
- 完全分离（所有 ISR seed 的 ISR* 都高于所有 Random seed）

### 原有功能验证
Fisher (p=0.0179), H7 MW (U=15.0, p=0.0179), Permutation (p=0.7845), BF10 (21.00) 均正常输出，无回归。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 525033,
  "duration_api_ms": 519745,
  "num_turns": 30,
  "stop_reason": "end_turn",
  "session_id": "312696ef-b0f4-4bcb-8551-4747dab89c15",
  "total_cost_usd": 2.107104,
  "usage": {
    "input_tokens": 32,
    "cache_creation_input_tokens": 81240,
    "cache_read_input_tokens": 1568616,
    "output_tokens": 32443,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 81240,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 720,
        "cache_read_input_tokens": 89949,
        "cache_creation_input_tokens": 3132,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 3132
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 3716,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.003811,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 32,
      "outputTokens": 32443,
      "cacheReadInputTokens": 1568616,
      "cacheCreationInputTokens": 81240,
      "webSearchRequests": 0,
      "costUSD": 2.1032930000000003,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "d723a96f-c738-4ee4-afc4-c75a2e4e906d"
}
```

</details>

---
