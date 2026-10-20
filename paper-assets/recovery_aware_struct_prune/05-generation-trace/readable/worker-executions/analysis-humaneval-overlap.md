# analysis humaneval overlap

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/workers/worker_analysis_humaneval_overlap_20260519T112242.log`
- **Structured JSON:** [`a1bdb1401a5dfc6644da.json`](../../sessions/a1/a1bdb1401a5dfc6644da.json)

## Before a recorded user message

35 recorded events

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
  "session_id": "d836da91-4539-49aa-93c2-ff86c541bac4",
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
    "mcp__agent-ml-research__register_artifact",
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
  "uuid": "ca14a508-d489-4577-8008-6d03ca87f983",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/memory/"
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
    "resetsAt": 1779192000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "0daba752-0373-4ed9-af55-1db1fd7911a9",
  "session_id": "d836da91-4539-49aa-93c2-ff86c541bac4"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to write a Python analysis script, run it on westd-29022 via SSH, and analyze HumanEval overlap across 4 evaluation files. Let me first load the SSH tools and then execute the analysis.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d836da91-4539-49aa-93c2-ff86c541bac4",
  "uuid": "e553c0a0-2650-48ee-be23-6180caefa09e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014E55KwqLQFz8BL8VyPrQt7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14221,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14221
      },
      "output_tokens": 29,
      "service_tier": "standard",
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

Let me load the SSH and artifact tools, then run the analysis.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d836da91-4539-49aa-93c2-ff86c541bac4",
  "uuid": "7aba4dc1-1303-404a-87e0-d6e13b400bb1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014E55KwqLQFz8BL8VyPrQt7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14221,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14221
      },
      "output_tokens": 29,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_018nKQs4fGKatZVN32VRKVEJ`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__register_artifact",
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
  "session_id": "d836da91-4539-49aa-93c2-ff86c541bac4",
  "uuid": "15af961c-3829-49a7-b860-e7c4c0217009",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014E55KwqLQFz8BL8VyPrQt7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14221,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14221
      },
      "output_tokens": 29,
      "service_tier": "standard",
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

_source line 7 · 2026-05-19T11:22:55.978Z_

<details><summary>↩ Tool result · `toolu_018nKQs4fGKatZVN32VRKVEJ`</summary>

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
  "tool_name": "mcp__agent-ml-research__register_artifact"
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
  "session_id": "d836da91-4539-49aa-93c2-ff86c541bac4",
  "uuid": "69c14855-0cc6-4e2a-872d-42a4f4caf7e7",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 24
  }
}
```

</details>

---

### Assistant

_source line 8_

First, let me explore the JSON structure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d836da91-4539-49aa-93c2-ff86c541bac4",
  "uuid": "bd76953c-630f-47fe-b366-5a12a4dbda4a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X5Q9T7nsnoNVVecEYQHn4x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1040,
      "cache_read_input_tokens": 26062,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1040
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01TMVFWxVEowCP2QJVVWerku`</summary>

```json
{
  "server": "westd-29022",
  "command": "python3 -c \"\nimport json\n\nfiles = {\n    'GRPO_Standard': '/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_grpo_standard_20_fair_2048_v3.json',\n    'GRPO_RASP': '/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_grpo_rasp_20_fair_2048.json',\n    'SFT_CKA': '/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_sft_cka_only_20_2048_v2.json',\n    'GRPO_CKA': '/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_grpo_cka_only_20_2048.json',\n}\n\nfor name, path in files.items():\n    d = json.load(open(path))\n    print(f'=== {name} ===')\n    print(f'  top keys: {list(d.keys())}')\n    # Check results key\n    if 'results' in d:\n        rk = list(d['results'].keys())\n        print(f'  results keys: {rk[:5]}')\n        if rk:\n            first = d['results'][rk[0]]\n            print(f'  first result keys: {list(first.keys()) if isinstance(first, dict) else type(first)}')\n    # Check for per-task details\n    for key in ['details', 'raw_results', 'per_task', 'samples']:\n        if key in d:\n            val = d[key]\n            if isinstance(val, list):\n                print(f'  {key}: list of {len(val)}, first={val[0] if val else None}')\n            elif isinstance(val, dict):\n                dk = list(val.keys())\n                print(f'  {key}: dict with {len(dk)} keys, first_key={dk[0] if dk else None}')\n                if dk:\n                    fv = val[dk[0]]\n                    if isinstance(fv, list) and fv:\n                        print(f'    first entry: {fv[0]}')\n                    elif isinstance(fv, dict):\n                        print(f'    first entry keys: {list(fv.keys())}')\n\"\n",
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
  "session_id": "d836da91-4539-49aa-93c2-ff86c541bac4",
  "uuid": "48f7471e-5d95-4b9a-94f9-bbd0a5c12cde",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X5Q9T7nsnoNVVecEYQHn4x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1040,
      "cache_read_input_tokens": 26062,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1040
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

_source line 10 · 2026-05-19T11:23:07.111Z_

<details><summary>↩ Tool result · `toolu_01TMVFWxVEowCP2QJVVWerku`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'python3 -c \\\"\\\\nimport json\\\\n\\\\nfiles = {\\\\n    \\\\'GRPO_Standard\\\\': \\\\'/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_grpo_standard_20_fair_2048_v3.json\\\\',\\\\n    \\\\'GRPO_RASP\\\\': \\\\'/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_grpo_rasp_20_fair_2048.json\\\\',\\\\n    \\\\'SFT_CKA\\\\': \\\\'/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_sft_cka_only_20_2048_v2.json\\\\',\\\\n    \\\\'GRPO_CKA\\\\': \\\\'/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_grpo_cka_only_20_2048.json\\\\',\\\\n}\\\\n\\\\nfor name, path in files.items():\\\\n    d = json.load(open(path))\\\\n    print(f\\\\'=== {name} ===\\\\')\\\\n    print(f\\\\'  top keys: {list(d.keys())}\\\\')\\\\n    # Check results key\\\\n    if \\\\'results\\\\' in d:\\\\n        rk = list(d[\\\\'results\\\\'].keys())\\\\n        print(f\\\\'  results keys: {rk[:5]}\\\\')\\\\n        if rk:\\\\n            first = d[\\\\'results\\\\'][rk[0]]\\\\n            print(f\\\\'  first result keys: {list(first.keys()) if isinstance(first, dict) else type(first)}\\\\')\\\\n    # Check for per-task details\\\\n    for key in [\\\\'details\\\\', \\\\'raw_results\\\\', \\\\'per_task\\\\', \\\\'samples\\\\']:\\\\n        if key in d:\\\\n            val = d[key]\\\\n            if isinstance(val, list):\\\\n                print(f\\\\'  {key}: list of {len(val)}, first={val[0] if val else None}\\\\')\\\\n            elif isinstance(val, dict):\\\\n                dk = list(val.keys())\\\\n                print(f\\\\'  {key}: dict with {len(dk)} keys, first_key={dk[0] if dk else None}\\\\')\\\\n                if dk:\\\\n                    fv = val[dk[0]]\\\\n                    if isinstance(fv, list) and fv:\\\\n                        print(f\\\\'    first entry: {fv[0]}\\\\')\\\\n                    elif isinstance(fv, dict):\\\\n                        print(f\\\\'    first entry keys: {list(fv.keys())}\\\\')\\\\n\\\"\\\\n'\\n\\nExit code: 127\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nbash: line 1: python3: command not found\\n\\n\", \"metadata\": {\"elapsed_seconds\": 1.09}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d836da91-4539-49aa-93c2-ff86c541bac4",
  "uuid": "15a149f7-4814-45c8-a1cf-56924846fc4d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"Encountered a bad command exit code!\\\\n\\\\nCommand: 'python3 -c \\\\\\\"\\\\\\\\nimport json\\\\\\\\n\\\\\\\\nfiles = {\\\\\\\\n    \\\\\\\\'GRPO_Standard\\\\\\\\': \\\\\\\\'/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_grpo_standard_20_fair_2048_v3.json\\\\\\\\',\\\\\\\\n    \\\\\\\\'GRPO_RASP\\\\\\\\': \\\\\\\\'/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_grpo_rasp_20_fair_2048.json\\\\\\\\',\\\\\\\\n    \\\\\\\\'SFT_CKA\\\\\\\\': \\\\\\\\'/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_sft_cka_only_20_2048_v2.json\\\\\\\\',\\\\\\\\n    \\\\\\\\'GRPO_CKA\\\\\\\\': \\\\\\\\'/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_grpo_cka_only_20_2048.json\\\\\\\\',\\\\\\\\n}\\\\\\\\n\\\\\\\\nfor name, path in files.items():\\\\\\\\n    d = json.load(open(path))\\\\\\\\n    print(f\\\\\\\\'=== {name} ===\\\\\\\\')\\\\\\\\n    print(f\\\\\\\\'  top keys: {list(d.keys())}\\\\\\\\')\\\\\\\\n    # Check results key\\\\\\\\n    if \\\\\\\\'results\\\\\\\\' in d:\\\\\\\\n        rk = list(d[\\\\\\\\'results\\\\\\\\'].keys())\\\\\\\\n        print(f\\\\\\\\'  results keys: {rk[:5]}\\\\\\\\')\\\\\\\\n        if rk:\\\\\\\\n            first = d[\\\\\\\\'results\\\\\\\\'][rk[0]]\\\\\\\\n            print(f\\\\\\\\'  first result keys: {list(first.keys()) if isinstance(first, dict) else type(first)}\\\\\\\\')\\\\\\\\n    # Check for per-task details\\\\\\\\n    for key in [\\\\\\\\'details\\\\\\\\', \\\\\\\\'raw_results\\\\\\\\', \\\\\\\\'per_task\\\\\\\\', \\\\\\\\'samples\\\\\\\\']:\\\\\\\\n        if key in d:\\\\\\\\n            val = d[key]\\\\\\\\n            if isinstance(val, list):\\\\\\\\n                print(f\\\\\\\\'  {key}: list of {len(val)}, first={val[0] if val else None}\\\\\\\\')\\\\\\\\n            elif isinstance(val, dict):\\\\\\\\n                dk = list(val.keys())\\\\\\\\n                print(f\\\\\\\\'  {key}: dict with {len(dk)} keys, first_key={dk[0] if dk else None}\\\\\\\\')\\\\\\\\n                if dk:\\\\\\\\n                    fv = val[dk[0]]\\\\\\\\n                    if isinstance(fv, list) and fv:\\\\\\\\n                        print(f\\\\\\\\'    first entry: {fv[0]}\\\\\\\\')\\\\\\\\n                    elif isinstance(fv, dict):\\\\\\\\n                        print(f\\\\\\\\'    first entry keys: {list(fv.keys())}\\\\\\\\')\\\\\\\\n\\\\\\\"\\\\\\\\n'\\\\n\\\\nExit code: 127\\\\n\\\\nStdout:\\\\n\\\\n\\\\n\\\\nStderr:\\\\n\\\\nbash: line 1: python3: command not found\\\\n\\\\n\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.09}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'python3 -c \\\"\\\\nimport json\\\\n\\\\nfiles = {\\\\n    \\\\'GRPO_Standard\\\\': \\\\'/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_grpo_standard_20_fair_2048_v3.json\\\\',\\\\n    \\\\'GRPO_RASP\\\\': \\\\'/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_grpo_rasp_20_fair_2048.json\\\\',\\\\n    \\\\'SFT_CKA\\\\': \\\\'/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_sft_cka_only_20_2048_v2.json\\\\',\\\\n    \\\\'GRPO_CKA\\\\': \\\\'/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_grpo_cka_only_20_2048.json\\\\',\\\\n}\\\\n\\\\nfor name, path in files.items():\\\\n    d = json.load(open(path))\\\\n    print(f\\\\'=== {name} ===\\\\')\\\\n    print(f\\\\'  top keys: {list(d.keys())}\\\\')\\\\n    # Check results key\\\\n    if \\\\'results\\\\' in d:\\\\n        rk = list(d[\\\\'results\\\\'].keys())\\\\n        print(f\\\\'  results keys: {rk[:5]}\\\\')\\\\n        if rk:\\\\n            first = d[\\\\'results\\\\'][rk[0]]\\\\n            print(f\\\\'  first result keys: {list(first.keys()) if isinstance(first, dict) else type(first)}\\\\')\\\\n    # Check for per-task details\\\\n    for key in [\\\\'details\\\\', \\\\'raw_results\\\\', \\\\'per_task\\\\', \\\\'samples\\\\']:\\\\n        if key in d:\\\\n            val = d[key]\\\\n            if isinstance(val, list):\\\\n                print(f\\\\'  {key}: list of {len(val)}, first={val[0] if val else None}\\\\')\\\\n            elif isinstance(val, dict):\\\\n                dk = list(val.keys())\\\\n                print(f\\\\'  {key}: dict with {len(dk)} keys, first_key={dk[0] if dk else None}\\\\')\\\\n                if dk:\\\\n                    fv = val[dk[0]]\\\\n                    if isinstance(fv, list) and fv:\\\\n                        print(f\\\\'    first entry: {fv[0]}\\\\')\\\\n                    elif isinstance(fv, dict):\\\\n                        print(f\\\\'    first entry keys: {list(fv.keys())}\\\\')\\\\n\\\"\\\\n'\\n\\nExit code: 127\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nbash: line 1: python3: command not found\\n\\n\", \"metadata\": {\"elapsed_seconds\": 1.09}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_015xqDoLdhBdY7DnDSHaSV3J`</summary>

```json
{
  "server": "westd-29022",
  "command": "which python; python --version",
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
  "session_id": "d836da91-4539-49aa-93c2-ff86c541bac4",
  "uuid": "83a387bf-02ba-45b2-ba0e-7c119cd53fa6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017qSMgC589kWdrYrdjhnRXH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1566,
      "cache_read_input_tokens": 27102,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1566
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

_source line 12 · 2026-05-19T11:23:11.012Z_

<details><summary>↩ Tool result · `toolu_015xqDoLdhBdY7DnDSHaSV3J`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'which python; python --version'\\n\\nExit code: 127\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nbash: line 1: python: command not found\\n\\n\", \"metadata\": {\"elapsed_seconds\": 1.0}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d836da91-4539-49aa-93c2-ff86c541bac4",
  "uuid": "8934e0ea-59d0-4af2-a49f-1c4b92fd3130",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"Encountered a bad command exit code!\\\\n\\\\nCommand: 'which python; python --version'\\\\n\\\\nExit code: 127\\\\n\\\\nStdout:\\\\n\\\\n\\\\n\\\\nStderr:\\\\n\\\\nbash: line 1: python: command not found\\\\n\\\\n\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.0}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'which python; python --version'\\n\\nExit code: 127\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nbash: line 1: python: command not found\\n\\n\", \"metadata\": {\"elapsed_seconds\": 1.0}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_014XATNgEjtpPaJs1J6mrAWg`</summary>

```json
{
  "server": "westd-29022",
  "command": "ls /root/miniconda3/bin/python 2>/dev/null || ls /root/anaconda3/bin/python 2>/dev/null || find /root -maxdepth 4 -name python -type f 2>/dev/null | head -5; echo \"---\"; ls /opt/conda/bin/python 2>/dev/null; which conda 2>/dev/null; echo $PATH",
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
  "session_id": "d836da91-4539-49aa-93c2-ff86c541bac4",
  "uuid": "f928dce2-4841-4834-9cca-f912fb79e4fe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ma21kad67HrhkjwXmBikRU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 226,
      "cache_read_input_tokens": 28668,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 226
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

_source line 14 · 2026-05-19T11:23:16.439Z_

<details><summary>↩ Tool result · `toolu_014XATNgEjtpPaJs1J6mrAWg`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/miniconda3/bin/python\\n---\\n/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.99}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d836da91-4539-49aa-93c2-ff86c541bac4",
  "uuid": "a52e6951-deed-4a4a-848e-9c8cb0f7dfea",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/miniconda3/bin/python\\\\n---\\\\n/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.99}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/miniconda3/bin/python\\n---\\n/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.99}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 15_

Found Python at `/root/miniconda3/bin/python`. Now let me write and run the full analysis script.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d836da91-4539-49aa-93c2-ff86c541bac4",
  "uuid": "34302417-f1d9-45b2-9846-e549b43d5def",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QP7JV7QjWHmQhbog9kyqUr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 328,
      "cache_read_input_tokens": 28894,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 328
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_018mzLdB92E3kku1WnNvZYFh`</summary>

```json
{
  "server": "westd-29022",
  "command": "cat > /tmp/humaneval_overlap.py << 'PYEOF'\nimport json\nimport os\n\nPY = \"/root/miniconda3/bin/python\"\n\nfiles = {\n    \"GRPO_Standard\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_grpo_standard_20_fair_2048_v3.json\",\n    \"GRPO_RASP\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_grpo_rasp_20_fair_2048.json\",\n    \"SFT_CKA\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_sft_cka_only_20_2048_v2.json\",\n    \"GRPO_CKA\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_grpo_cka_only_20_2048.json\",\n}\n\n# Step 1: Explore structure\ndata = {}\nfor name, path in files.items():\n    d = json.load(open(path))\n    data[name] = d\n    print(f\"=== {name} ===\")\n    print(f\"  top keys: {list(d.keys())}\")\n    if 'results' in d:\n        rk = list(d['results'].keys())\n        print(f\"  results sub-keys: {rk[:5]}\")\n        if rk:\n            first = d['results'][rk[0]]\n            if isinstance(first, dict):\n                print(f\"  first result: {list(first.keys())}\")\n    for key in ['details', 'raw_results', 'per_task', 'samples', 'eval_results']:\n        if key in d:\n            val = d[key]\n            if isinstance(val, list):\n                print(f\"  {key}: list[{len(val)}]\")\n                if val:\n                    item = val[0]\n                    if isinstance(item, dict):\n                        print(f\"    first item keys: {list(item.keys())}\")\n                        print(f\"    first item sample: { {k: v for k, v in list(item.items())[:6]} }\")\n            elif isinstance(val, dict):\n                dk = list(val.keys())\n                print(f\"  {key}: dict[{len(dk)}], keys sample: {dk[:3]}\")\n    print()\nPYEOF\n/root/miniconda3/bin/python /tmp/humaneval_overlap.py",
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
  "session_id": "d836da91-4539-49aa-93c2-ff86c541bac4",
  "uuid": "c38acedd-d146-4260-9730-67f6640a8b62",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QP7JV7QjWHmQhbog9kyqUr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 328,
      "cache_read_input_tokens": 28894,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 328
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

_source line 17 · 2026-05-19T11:23:26.309Z_

<details><summary>↩ Tool result · `toolu_018mzLdB92E3kku1WnNvZYFh`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== GRPO_Standard ===\\n  top keys: ['model_path', 'benchmark', 'pass_at_1', 'stderr', 'n_correct', 'n_total', 'eos_stats', 'examples']\\n\\n=== GRPO_RASP ===\\n  top keys: ['model_path', 'benchmark', 'pass_at_1', 'stderr', 'n_correct', 'n_total', 'eos_stats', 'examples']\\n\\n=== SFT_CKA ===\\n  top keys: ['model_path', 'benchmark', 'pass_at_1', 'stderr', 'n_correct', 'n_total', 'eos_stats', 'examples']\\n\\n=== GRPO_CKA ===\\n  top keys: ['model_path', 'benchmark', 'pass_at_1', 'stderr', 'n_correct', 'n_total', 'eos_stats', 'examples']\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d836da91-4539-49aa-93c2-ff86c541bac4",
  "uuid": "58076156-42b5-4018-9ec7-6c4995c552e2",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"=== GRPO_Standard ===\\\\n  top keys: ['model_path', 'benchmark', 'pass_at_1', 'stderr', 'n_correct', 'n_total', 'eos_stats', 'examples']\\\\n\\\\n=== GRPO_RASP ===\\\\n  top keys: ['model_path', 'benchmark', 'pass_at_1', 'stderr', 'n_correct', 'n_total', 'eos_stats', 'examples']\\\\n\\\\n=== SFT_CKA ===\\\\n  top keys: ['model_path', 'benchmark', 'pass_at_1', 'stderr', 'n_correct', 'n_total', 'eos_stats', 'examples']\\\\n\\\\n=== GRPO_CKA ===\\\\n  top keys: ['model_path', 'benchmark', 'pass_at_1', 'stderr', 'n_correct', 'n_total', 'eos_stats', 'examples']\\\\n\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.46}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"=== GRPO_Standard ===\\n  top keys: ['model_path', 'benchmark', 'pass_at_1', 'stderr', 'n_correct', 'n_total', 'eos_stats', 'examples']\\n\\n=== GRPO_RASP ===\\n  top keys: ['model_path', 'benchmark', 'pass_at_1', 'stderr', 'n_correct', 'n_total', 'eos_stats', 'examples']\\n\\n=== SFT_CKA ===\\n  top keys: ['model_path', 'benchmark', 'pass_at_1', 'stderr', 'n_correct', 'n_total', 'eos_stats', 'examples']\\n\\n=== GRPO_CKA ===\\n  top keys: ['model_path', 'benchmark', 'pass_at_1', 'stderr', 'n_correct', 'n_total', 'eos_stats', 'examples']\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 18_

All files have `examples` key. Let me check that structure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d836da91-4539-49aa-93c2-ff86c541bac4",
  "uuid": "8aafdc76-7e5c-4e9f-9042-f20dd9343090",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L3LzorFkEZ8Jm3v9b8ijDD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1086,
      "cache_read_input_tokens": 29222,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1086
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

_source line 19_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01RxvunX5mpCjuq5HpACFZx9`</summary>

```json
{
  "server": "westd-29022",
  "command": "cat > /tmp/humaneval_overlap.py << 'PYEOF'\nimport json\n\nfiles = {\n    \"GRPO_Standard\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_grpo_standard_20_fair_2048_v3.json\",\n    \"GRPO_RASP\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_grpo_rasp_20_fair_2048.json\",\n    \"SFT_CKA\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_sft_cka_only_20_2048_v2.json\",\n    \"GRPO_CKA\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_grpo_cka_only_20_2048.json\",\n}\n\nd = json.load(open(files[\"GRPO_Standard\"]))\nprint(\"examples type:\", type(d['examples']))\nif isinstance(d['examples'], list):\n    print(\"examples len:\", len(d['examples']))\n    ex = d['examples'][0]\n    print(\"first example keys:\", list(ex.keys()) if isinstance(ex, dict) else type(ex))\n    print(\"first example:\", {k: (str(v)[:80] if isinstance(v, str) else v) for k, v in ex.items()})\nelif isinstance(d['examples'], dict):\n    dk = list(d['examples'].keys())\n    print(\"examples keys sample:\", dk[:3])\n    fv = d['examples'][dk[0]]\n    print(\"first val:\", {k: (str(v)[:80] if isinstance(v, str) else v) for k, v in fv.items()} if isinstance(fv, dict) else fv)\nPYEOF\n/root/miniconda3/bin/python /tmp/humaneval_overlap.py",
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
  "session_id": "d836da91-4539-49aa-93c2-ff86c541bac4",
  "uuid": "ae6cb789-503f-4e5d-b9a3-ecf64438cbc6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L3LzorFkEZ8Jm3v9b8ijDD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1086,
      "cache_read_input_tokens": 29222,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1086
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

_source line 20 · 2026-05-19T11:23:36.006Z_

<details><summary>↩ Tool result · `toolu_01RxvunX5mpCjuq5HpACFZx9`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"examples type: &lt;class 'list'>\\nexamples len: 164\\nfirst example keys: ['task_id', 'passed', 'error', 'response_length']\\nfirst example: {'task_id': 'HumanEval/0', 'passed': False, 'error': '  File \\\"/tmp/tmp_agrgsle.py\\\", line 11\\\\n    Now, how to implement this in Python. ', 'response_length': 2048}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.48}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d836da91-4539-49aa-93c2-ff86c541bac4",
  "uuid": "b052fb25-cdd6-4e05-ae5b-deee78b3bd9b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"examples type: &lt;class 'list'>\\\\nexamples len: 164\\\\nfirst example keys: ['task_id', 'passed', 'error', 'response_length']\\\\nfirst example: {'task_id': 'HumanEval/0', 'passed': False, 'error': '  File \\\\\\\"/tmp/tmp_agrgsle.py\\\\\\\", line 11\\\\\\\\n    Now, how to implement this in Python. ', 'response_length': 2048}\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.48}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"examples type: &lt;class 'list'>\\nexamples len: 164\\nfirst example keys: ['task_id', 'passed', 'error', 'response_length']\\nfirst example: {'task_id': 'HumanEval/0', 'passed': False, 'error': '  File \\\"/tmp/tmp_agrgsle.py\\\", line 11\\\\n    Now, how to implement this in Python. ', 'response_length': 2048}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.48}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 21_

Structure is clear: `examples` is a list of 164 items, each with `task_id` and `passed`. Now writing the full analysis script.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d836da91-4539-49aa-93c2-ff86c541bac4",
  "uuid": "82e47905-402c-4c4e-a12f-8b17be2a93e6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017TydPvEm45QYcMSgwABL8Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 883,
      "cache_read_input_tokens": 30308,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 883
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01PvyhLnCJ4gKMH4ScL5YzSX`</summary>

```json
{
  "server": "westd-29022",
  "command": "cat > /tmp/humaneval_overlap.py << 'PYEOF'\nimport json\nfrom itertools import combinations\n\nfiles = {\n    \"GRPO_Standard\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_grpo_standard_20_fair_2048_v3.json\",\n    \"GRPO_RASP\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_grpo_rasp_20_fair_2048.json\",\n    \"SFT_CKA\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_sft_cka_only_20_2048_v2.json\",\n    \"GRPO_CKA\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_grpo_cka_only_20_2048.json\",\n}\n\n# Load passed sets\npassed = {}\ntotals = {}\nfor name, path in files.items():\n    d = json.load(open(path))\n    passed[name] = set(ex[\"task_id\"] for ex in d[\"examples\"] if ex[\"passed\"])\n    totals[name] = len(d[\"examples\"])\n\nnames = list(files.keys())\nshort = {\"GRPO_Standard\": \"Std\", \"GRPO_RASP\": \"RASP\", \"SFT_CKA\": \"SFT-CKA\", \"GRPO_CKA\": \"GRPO-CKA\"}\n\n# ============================================================\n# Build output\n# ============================================================\nout = []\ndef P(s=\"\"): out.append(s)\n\nP(\"# HumanEval Overlap Analysis\")\nP()\nP(\"## Summary\")\nP(\"| Model | Passed | Total | Pass@1 |\")\nP(\"|-------|--------|-------|--------|\")\nfor n in names:\n    p = len(passed[n])\n    t = totals[n]\n    P(f\"| {n} | {p} | {t} | {p/t*100:.1f}% |\")\nP()\n\n# === A. Pairwise Overlap Matrix ===\nP(\"## A. Pairwise Overlap Matrix\")\nP()\nheader = \"| A vs B | Both Pass | A-only | B-only | Both Fail |\"\nsep    = \"|--------|-----------|--------|--------|-----------|\"\nP(header)\nP(sep)\nfor i, a in enumerate(names):\n    for j, b in enumerate(names):\n        if j <= i:\n            continue\n        both = passed[a] & passed[b]\n        a_only = passed[a] - passed[b]\n        b_only = passed[b] - passed[a]\n        neither = totals[a] - len(both) - len(a_only) - len(b_only)\n        P(f\"| {short[a]} vs {short[b]} | {len(both)} | {len(a_only)} | {len(b_only)} | {neither} |\")\nP()\n\n# === Key Finding 1: GRPO Standard vs RASP ===\nP(\"## Key Finding 1: GRPO Standard vs RASP Overlap\")\nP()\nstd = passed[\"GRPO_Standard\"]\nrasp = passed[\"GRPO_RASP\"]\nboth_sr = std & rasp\nstd_only = sorted(std - rasp)\nrasp_only = sorted(rasp - std)\nP(f\"- Both passed: **{len(both_sr)}/18**\")\nP(f\"- Jaccard similarity: {len(both_sr)/(len(std | rasp))*100:.1f}%\")\nP(f\"- Standard-only ({len(std_only)}): {', '.join(std_only)}\")\nP(f\"- RASP-only ({len(rasp_only)}): {', '.join(rasp_only)}\")\nP()\nif len(both_sr) == 18:\n    P(\"**Conclusion**: Identical 18 tasks. RASP pruning preserves exactly the same code capabilities as Standard pruning.\")\nelif len(both_sr) >= 14:\n    P(f\"**Conclusion**: High overlap ({len(both_sr)}/18). RASP and Standard pruning preserve largely the same code capabilities with minor differences.\")\nelse:\n    P(f\"**Conclusion**: Moderate overlap ({len(both_sr)}/18). RASP and Standard pruning preserve partially different code capabilities.\")\nP()\n\n# === Key Finding 2: CKA-only superset analysis ===\nP(\"## Key Finding 2: CKA-only Superset Analysis\")\nP()\ncka_union = passed[\"SFT_CKA\"] | passed[\"GRPO_CKA\"]\nstd_rasp_union = passed[\"GRPO_Standard\"] | passed[\"GRPO_RASP\"]\ncka_exclusive = sorted(cka_union - std_rasp_union)\nstd_rasp_exclusive = sorted(std_rasp_union - cka_union)\noverlap_all = cka_union & std_rasp_union\n\nP(f\"- CKA-only union (SFT CKA ∪ GRPO CKA): **{len(cka_union)}** unique tasks\")\nP(f\"- Standard ∪ RASP union: **{len(std_rasp_union)}** unique tasks\")\nP(f\"- Overlap (both groups pass): **{len(overlap_all)}**\")\nP(f\"- CKA superset of Standard/RASP? **{'Yes' if std_rasp_union.issubset(cka_union) else 'No'}** (covers {len(overlap_all)}/{len(std_rasp_union)} of Standard/RASP tasks)\")\nP()\nif std_rasp_exclusive:\n    P(f\"- Standard/RASP-only tasks ({len(std_rasp_exclusive)}): {', '.join(std_rasp_exclusive)}\")\nP(f\"- CKA-exclusive tasks ({len(cka_exclusive)}): {', '.join(cka_exclusive)}\")\nP()\n\n# === Key Finding 3: SFT->GRPO CKA transition ===\nP(\"## Key Finding 3: SFT CKA -> GRPO CKA Transition\")\nP()\nsft_cka = passed[\"SFT_CKA\"]\ngrpo_cka = passed[\"GRPO_CKA\"]\nboth_cka = sft_cka & grpo_cka\nsft_only_cka = sorted(sft_cka - grpo_cka)\ngrpo_only_cka = sorted(grpo_cka - sft_cka)\n\nP(f\"- Both passed: **{len(both_cka)}**\")\nP(f\"- SFT-only (GRPO lost, {len(sft_only_cka)}): {', '.join(sft_only_cka) if sft_only_cka else 'none'}\")\nP(f\"- GRPO-only (GRPO gained, {len(grpo_only_cka)}): {', '.join(grpo_only_cka) if grpo_only_cka else 'none'}\")\nP(f\"- Net effect: {len(grpo_cka)} - {len(sft_cka)} = **{len(grpo_cka) - len(sft_cka):+d}** (GRPO lost {len(sft_only_cka)}, gained {len(grpo_only_cka)})\")\nP()\n\n# === B. CKA-only exclusive detailed list ===\nP(\"## B. CKA-only Exclusive Tasks (Detailed)\")\nP()\nP(\"Tasks passed by CKA-only models (SFT or GRPO) but failed by both GRPO Standard and GRPO RASP:\")\nP()\nif cka_exclusive:\n    P(\"| # | Task ID | SFT CKA | GRPO CKA |\")\n    P(\"|---|---------|---------|----------|\")\n    for i, tid in enumerate(cka_exclusive, 1):\n        sft_mark = \"Pass\" if tid in sft_cka else \"Fail\"\n        grpo_mark = \"Pass\" if tid in grpo_cka else \"Fail\"\n        P(f\"| {i} | {tid} | {sft_mark} | {grpo_mark} |\")\nelse:\n    P(\"None.\")\nP()\n\n# === Interpretation ===\nP(\"## Interpretation\")\nP()\n\n# Build interpretation dynamically\ninterp = []\nif len(both_sr) == len(std) == len(rasp):\n    interp.append(f\"GRPO Standard and GRPO RASP solve identical {len(both_sr)} tasks, indicating that recovery-aware (RASP) pruning does not alter which code problems the GRPO-recovered model can solve compared to standard pruning. The two pruning strategies converge to the same capability profile after GRPO recovery.\")\nelif len(both_sr) >= len(std) * 0.7:\n    interp.append(f\"GRPO Standard and GRPO RASP share {len(both_sr)}/{len(std | rasp)} tasks ({len(both_sr)/(len(std | rasp))*100:.0f}% Jaccard). The high overlap suggests RASP pruning largely preserves the same code capability profile as standard pruning after GRPO recovery, with {len(std_only)} Standard-exclusive and {len(rasp_only)} RASP-exclusive tasks showing minor divergence.\")\nelse:\n    interp.append(f\"GRPO Standard and GRPO RASP share only {len(both_sr)}/{len(std | rasp)} tasks ({len(both_sr)/(len(std | rasp))*100:.0f}% Jaccard). The two pruning strategies preserve meaningfully different code capabilities after GRPO recovery.\")\n\nif std_rasp_union.issubset(cka_union):\n    interp.append(f\"CKA-only pruning is a strict superset: all {len(std_rasp_union)} tasks solved by Standard/RASP are also solved by CKA-only models, plus {len(cka_exclusive)} additional exclusive tasks. This demonstrates that CKA-guided pruning preserves a broader range of code generation capabilities.\")\nelse:\n    interp.append(f\"CKA-only covers {len(overlap_all)}/{len(std_rasp_union)} Standard/RASP tasks and adds {len(cka_exclusive)} exclusive tasks, but loses {len(std_rasp_exclusive)} tasks ({', '.join(std_rasp_exclusive)}). The capability profiles partially diverge.\")\n\nnet = len(grpo_cka) - len(sft_cka)\nif net == 0 and len(sft_only_cka) == 0:\n    interp.append(\"The SFT CKA to GRPO CKA transition is perfectly stable: identical 33 tasks, zero churn. GRPO training on the CKA-pruned model neither adds nor removes code capabilities.\")\nelif net == 0 and len(sft_only_cka) > 0:\n    interp.append(f\"SFT->GRPO CKA maintains the same pass count (33) but with {len(sft_only_cka)} task swaps: GRPO loses {len(sft_only_cka)} SFT tasks and gains {len(grpo_only_cka)} new ones. This suggests GRPO redistributes capability rather than expanding it.\")\nelif net > 0:\n    interp.append(f\"GRPO CKA gains {net} net tasks over SFT CKA ({len(grpo_only_cka)} gained, {len(sft_only_cka)} lost), showing GRPO expands code capabilities on CKA-pruned models.\")\nelse:\n    interp.append(f\"GRPO CKA loses {abs(net)} net tasks vs SFT CKA ({len(sft_only_cka)} lost, {len(grpo_only_cka)} gained), indicating GRPO slightly degrades code capability on CKA-pruned models.\")\n\nfor para in interp:\n    P(para)\n    P()\n\n# Write to file\noutput_path = \"/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_overlap_analysis.md\"\nwith open(output_path, \"w\") as f:\n    f.write(\"\\n\".join(out))\n\n# Also print to stdout\nprint(\"\\n\".join(out))\nprint(f\"\\n--- Saved to {output_path} ---\")\nPYEOF\n/root/miniconda3/bin/python /tmp/humaneval_overlap.py",
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
  "session_id": "d836da91-4539-49aa-93c2-ff86c541bac4",
  "uuid": "5d7756d0-2323-4440-b879-0fd181110183",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017TydPvEm45QYcMSgwABL8Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 883,
      "cache_read_input_tokens": 30308,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 883
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

_source line 23 · 2026-05-19T11:24:22.603Z_

<details><summary>↩ Tool result · `toolu_01PvyhLnCJ4gKMH4ScL5YzSX`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"# HumanEval Overlap Analysis\\n\\n## Summary\\n| Model | Passed | Total | Pass@1 |\\n|-------|--------|-------|--------|\\n| GRPO_Standard | 18 | 164 | 11.0% |\\n| GRPO_RASP | 18 | 164 | 11.0% |\\n| SFT_CKA | 33 | 164 | 20.1% |\\n| GRPO_CKA | 33 | 164 | 20.1% |\\n\\n## A. Pairwise Overlap Matrix\\n\\n| A vs B | Both Pass | A-only | B-only | Both Fail |\\n|--------|-----------|--------|--------|-----------|\\n| Std vs RASP | 5 | 13 | 13 | 133 |\\n| Std vs SFT-CKA | 9 | 9 | 24 | 122 |\\n| Std vs GRPO-CKA | 8 | 10 | 25 | 121 |\\n| RASP vs SFT-CKA | 8 | 10 | 25 | 121 |\\n| RASP vs GRPO-CKA | 5 | 13 | 28 | 118 |\\n| SFT-CKA vs GRPO-CKA | 17 | 16 | 16 | 115 |\\n\\n## Key Finding 1: GRPO Standard vs RASP Overlap\\n\\n- Both passed: **5/18**\\n- Jaccard similarity: 16.1%\\n- Standard-only (13): HumanEval/133, HumanEval/135, HumanEval/136, HumanEval/138, HumanEval/144, HumanEval/35, HumanEval/45, HumanEval/49, HumanEval/51, HumanEval/53, HumanEval/60, HumanEval/90, HumanEval/97\\n- RASP-only (13): HumanEval/102, HumanEval/12, HumanEval/151, HumanEval/154, HumanEval/29, HumanEval/3, HumanEval/34, HumanEval/47, HumanEval/69, HumanEval/73, HumanEval/74, HumanEval/82, HumanEval/92\\n\\n**Conclusion**: Moderate overlap (5/18). RASP and Standard pruning preserve partially different code capabilities.\\n\\n## Key Finding 2: CKA-only Superset Analysis\\n\\n- CKA-only union (SFT CKA ∪ GRPO CKA): **49** unique tasks\\n- Standard ∪ RASP union: **31** unique tasks\\n- Overlap (both groups pass): **18**\\n- CKA superset of Standard/RASP? **No** (covers 18/31 of Standard/RASP tasks)\\n\\n- Standard/RASP-only tasks (13): HumanEval/13, HumanEval/135, HumanEval/136, HumanEval/138, HumanEval/144, HumanEval/154, HumanEval/29, HumanEval/34, HumanEval/35, HumanEval/69, HumanEval/73, HumanEval/74, HumanEval/82\\n- CKA-exclusive tasks (31): HumanEval/104, HumanEval/106, HumanEval/111, HumanEval/112, HumanEval/115, HumanEval/123, HumanEval/139, HumanEval/155, HumanEval/159, HumanEval/17, HumanEval/2, HumanEval/21, HumanEval/22, HumanEval/27, HumanEval/30, HumanEval/4, HumanEval/40, HumanEval/42, HumanEval/44, HumanEval/5, HumanEval/52, HumanEval/55, HumanEval/63, HumanEval/68, HumanEval/7, HumanEval/72, HumanEval/8, HumanEval/85, HumanEval/88, HumanEval/9, HumanEval/96\\n\\n## Key Finding 3: SFT CKA -> GRPO CKA Transition\\n\\n- Both passed: **17**\\n- SFT-only (GRPO lost, 16): HumanEval/102, HumanEval/104, HumanEval/106, HumanEval/111, HumanEval/123, HumanEval/155, HumanEval/157, HumanEval/31, HumanEval/45, HumanEval/47, HumanEval/5, HumanEval/60, HumanEval/85, HumanEval/9, HumanEval/92, HumanEval/96\\n- GRPO-only (GRPO gained, 16): HumanEval/112, HumanEval/12, HumanEval/133, HumanEval/139, HumanEval/151, HumanEval/17, HumanEval/4, HumanEval/42, HumanEval/44, HumanEval/55, HumanEval/63, HumanEval/68, HumanEval/72, HumanEval/88, HumanEval/90, HumanEval/97\\n- Net effect: 33 - 33 = **+0** (GRPO lost 16, gained 16)\\n\\n## B. CKA-only Exclusive Tasks (Detailed)\\n\\nTasks passed by CKA-only models (SFT or GRPO) but failed by both GRPO Standard and GRPO RASP:\\n\\n| # | Task ID | SFT CKA | GRPO CKA |\\n|---|---------|---------|----------|\\n| 1 | HumanEval/104 | Pass | Fail |\\n| 2 | HumanEval/106 | Pass | Fail |\\n| 3 | HumanEval/111 | Pass | Fail |\\n| 4 | HumanEval/112 | Fail | Pass |\\n| 5 | HumanEval/115 | Pass | Pass |\\n| 6 | HumanEval/123 | Pass | Fail |\\n| 7 | HumanEval/139 | Fail | Pass |\\n| 8 | HumanEval/155 | Pass | Fail |\\n| 9 | HumanEval/159 | Pass | Pass |\\n| 10 | HumanEval/17 | Fail | Pass |\\n| 11 | HumanEval/2 | Pass | Pass |\\n| 12 | HumanEval/21 | Pass | Pass |\\n| 13 | HumanEval/22 | Pass | Pass |\\n| 14 | HumanEval/27 | Pass | Pass |\\n| 15 | HumanEval/30 | Pass | Pass |\\n| 16 | HumanEval/4 | Fail | Pass |\\n| 17 | HumanEval/40 | Pass | Pass |\\n| 18 | HumanEval/42 | Fail | Pass |\\n| 19 | HumanEval/44 | Fail | Pass |\\n| 20 | HumanEval/5 | Pass | Fail |\\n| 21 | HumanEval/52 | Pass | Pass |\\n| 22 | HumanEval/55 | Fail | Pass |\\n| 23 | HumanEval/63 | Fail | Pass |\\n| 24 | HumanEval/68 | Fail | Pass |\\n| 25 | HumanEval/7 | Pass | Pass |\\n| 26 | HumanEval/72 | Fail | Pass |\\n| 27 | HumanEval/8 | Pass | Pass |\\n| 28 | HumanEval/85 | Pass | Fail |\\n| 29 | HumanEval/88 | Fail | Pass |\\n| 30 | HumanEval/9 | Pass | Fail |\\n| 31 | HumanEval/96 | Pass | Fail |\\n\\n## Interpretation\\n\\nGRPO Standard and GRPO RASP share only 5/31 tasks (16% Jaccard). The two pruning strategies preserve meaningfully different code capabilities after GRPO recovery.\\n\\nCKA-only covers 18/31 Standard/RASP tasks and adds 31 exclusive tasks, but loses 13 tasks (HumanEval/13, HumanEval/135, HumanEval/136, HumanEval/138, HumanEval/144, HumanEval/154, HumanEval/29, HumanEval/34, HumanEval/35, HumanEval/69, HumanEval/73, HumanEval/74, HumanEval/82). The capability profiles partially diverge.\\n\\nSFT->GRPO CKA maintains the same pass count (33) but with 16 task swaps: GRPO loses 16 SFT tasks and gains 16 new ones. This suggests GRPO redistributes capability rather than expanding it.\\n\\n\\n--- Saved to /root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_overlap_analysis.md ---\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.49}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d836da91-4539-49aa-93c2-ff86c541bac4",
  "uuid": "7e58e482-1709-42f1-9c19-c4792feb0bb2",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"# HumanEval Overlap Analysis\\\\n\\\\n## Summary\\\\n| Model | Passed | Total | Pass@1 |\\\\n|-------|--------|-------|--------|\\\\n| GRPO_Standard | 18 | 164 | 11.0% |\\\\n| GRPO_RASP | 18 | 164 | 11.0% |\\\\n| SFT_CKA | 33 | 164 | 20.1% |\\\\n| GRPO_CKA | 33 | 164 | 20.1% |\\\\n\\\\n## A. Pairwise Overlap Matrix\\\\n\\\\n| A vs B | Both Pass | A-only | B-only | Both Fail |\\\\n|--------|-----------|--------|--------|-----------|\\\\n| Std vs RASP | 5 | 13 | 13 | 133 |\\\\n| Std vs SFT-CKA | 9 | 9 | 24 | 122 |\\\\n| Std vs GRPO-CKA | 8 | 10 | 25 | 121 |\\\\n| RASP vs SFT-CKA | 8 | 10 | 25 | 121 |\\\\n| RASP vs GRPO-CKA | 5 | 13 | 28 | 118 |\\\\n| SFT-CKA vs GRPO-CKA | 17 | 16 | 16 | 115 |\\\\n\\\\n## Key Finding 1: GRPO Standard vs RASP Overlap\\\\n\\\\n- Both passed: **5/18**\\\\n- Jaccard similarity: 16.1%\\\\n- Standard-only (13): HumanEval/133, HumanEval/135, HumanEval/136, HumanEval/138, HumanEval/144, HumanEval/35, HumanEval/45, HumanEval/49, HumanEval/51, HumanEval/53, HumanEval/60, HumanEval/90, HumanEval/97\\\\n- RASP-only (13): HumanEval/102, HumanEval/12, HumanEval/151, HumanEval/154, HumanEval/29, HumanEval/3, HumanEval/34, HumanEval/47, HumanEval/69, HumanEval/73, HumanEval/74, HumanEval/82, HumanEval/92\\\\n\\\\n**Conclusion**: Moderate overlap (5/18). RASP and Standard pruning preserve partially different code capabilities.\\\\n\\\\n## Key Finding 2: CKA-only Superset Analysis\\\\n\\\\n- CKA-only union (SFT CKA ∪ GRPO CKA): **49** unique tasks\\\\n- Standard ∪ RASP union: **31** unique tasks\\\\n- Overlap (both groups pass): **18**\\\\n- CKA superset of Standard/RASP? **No** (covers 18/31 of Standard/RASP tasks)\\\\n\\\\n- Standard/RASP-only tasks (13): HumanEval/13, HumanEval/135, HumanEval/136, HumanEval/138, HumanEval/144, HumanEval/154, HumanEval/29, HumanEval/34, HumanEval/35, HumanEval/69, HumanEval/73, HumanEval/74, HumanEval/82\\\\n- CKA-exclusive tasks (31): HumanEval/104, HumanEval/106, HumanEval/111, HumanEval/112, HumanEval/115, HumanEval/123, HumanEval/139, HumanEval/155, HumanEval/159, HumanEval/17, HumanEval/2, HumanEval/21, HumanEval/22, HumanEval/27, HumanEval/30, HumanEval/4, HumanEval/40, HumanEval/42, HumanEval/44, HumanEval/5, HumanEval/52, HumanEval/55, HumanEval/63, HumanEval/68, HumanEval/7, HumanEval/72, HumanEval/8, HumanEval/85, HumanEval/88, HumanEval/9, HumanEval/96\\\\n\\\\n## Key Finding 3: SFT CKA -> GRPO CKA Transition\\\\n\\\\n- Both passed: **17**\\\\n- SFT-only (GRPO lost, 16): HumanEval/102, HumanEval/104, HumanEval/106, HumanEval/111, HumanEval/123, HumanEval/155, HumanEval/157, HumanEval/31, HumanEval/45, HumanEval/47, HumanEval/5, HumanEval/60, HumanEval/85, HumanEval/9, HumanEval/92, HumanEval/96\\\\n- GRPO-only (GRPO gained, 16): HumanEval/112, HumanEval/12, HumanEval/133, HumanEval/139, HumanEval/151, HumanEval/17, HumanEval/4, HumanEval/42, HumanEval/44, HumanEval/55, HumanEval/63, HumanEval/68, HumanEval/72, HumanEval/88, HumanEval/90, HumanEval/97\\\\n- Net effect: 33 - 33 = **+0** (GRPO lost 16, gained 16)\\\\n\\\\n## B. CKA-only Exclusive Tasks (Detailed)\\\\n\\\\nTasks passed by CKA-only models (SFT or GRPO) but failed by both GRPO Standard and GRPO RASP:\\\\n\\\\n| # | Task ID | SFT CKA | GRPO CKA |\\\\n|---|---------|---------|----------|\\\\n| 1 | HumanEval/104 | Pass | Fail |\\\\n| 2 | HumanEval/106 | Pass | Fail |\\\\n| 3 | HumanEval/111 | Pass | Fail |\\\\n| 4 | HumanEval/112 | Fail | Pass |\\\\n| 5 | HumanEval/115 | Pass | Pass |\\\\n| 6 | HumanEval/123 | Pass | Fail |\\\\n| 7 | HumanEval/139 | Fail | Pass |\\\\n| 8 | HumanEval/155 | Pass | Fail |\\\\n| 9 | HumanEval/159 | Pass | Pass |\\\\n| 10 | HumanEval/17 | Fail | Pass |\\\\n| 11 | HumanEval/2 | Pass | Pass |\\\\n| 12 | HumanEval/21 | Pass | Pass |\\\\n| 13 | HumanEval/22 | Pass | Pass |\\\\n| 14 | HumanEval/27 | Pass | Pass |\\\\n| 15 | HumanEval/30 | Pass | Pass |\\\\n| 16 | HumanEval/4 | Fail | Pass |\\\\n| 17 | HumanEval/40 | Pass | Pass |\\\\n| 18 | HumanEval/42 | Fail | Pass |\\\\n| 19 | HumanEval/44 | Fail | Pass |\\\\n| 20 | HumanEval/5 | Pass | Fail |\\\\n| 21 | HumanEval/52 | Pass | Pass |\\\\n| 22 | HumanEval/55 | Fail | Pass |\\\\n| 23 | HumanEval/63 | Fail | Pass |\\\\n| 24 | HumanEval/68 | Fail | Pass |\\\\n| 25 | HumanEval/7 | Pass | Pass |\\\\n| 26 | HumanEval/72 | Fail | Pass |\\\\n| 27 | HumanEval/8 | Pass | Pass |\\\\n| 28 | HumanEval/85 | Pass | Fail |\\\\n| 29 | HumanEval/88 | Fail | Pass |\\\\n| 30 | HumanEval/9 | Pass | Fail |\\\\n| 31 | HumanEval/96 | Pass | Fail |\\\\n\\\\n## Interpretation\\\\n\\\\nGRPO Standard and GRPO RASP share only 5/31 tasks (16% Jaccard). The two pruning strategies preserve meaningfully different code capabilities after GRPO recovery.\\\\n\\\\nCKA-only covers 18/31 Standard/RASP tasks and adds 31 exclusive tasks, but loses 13 tasks (HumanEval/13, HumanEval/135, HumanEval/136, HumanEval/138, HumanEval/144, HumanEval/154, HumanEval/29, HumanEval/34, HumanEval/35, HumanEval/69, HumanEval/73, HumanEval/74, HumanEval/82). The capability profiles partially diverge.\\\\n\\\\nSFT->GRPO CKA maintains the same pass count (33) but with 16 task swaps: GRPO loses 16 SFT tasks and gains 16 new ones. This suggests GRPO redistributes capability rather than expanding it.\\\\n\\\\n\\\\n--- Saved to /root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_overlap_analysis.md ---\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.49}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"# HumanEval Overlap Analysis\\n\\n## Summary\\n| Model | Passed | Total | Pass@1 |\\n|-------|--------|-------|--------|\\n| GRPO_Standard | 18 | 164 | 11.0% |\\n| GRPO_RASP | 18 | 164 | 11.0% |\\n| SFT_CKA | 33 | 164 | 20.1% |\\n| GRPO_CKA | 33 | 164 | 20.1% |\\n\\n## A. Pairwise Overlap Matrix\\n\\n| A vs B | Both Pass | A-only | B-only | Both Fail |\\n|--------|-----------|--------|--------|-----------|\\n| Std vs RASP | 5 | 13 | 13 | 133 |\\n| Std vs SFT-CKA | 9 | 9 | 24 | 122 |\\n| Std vs GRPO-CKA | 8 | 10 | 25 | 121 |\\n| RASP vs SFT-CKA | 8 | 10 | 25 | 121 |\\n| RASP vs GRPO-CKA | 5 | 13 | 28 | 118 |\\n| SFT-CKA vs GRPO-CKA | 17 | 16 | 16 | 115 |\\n\\n## Key Finding 1: GRPO Standard vs RASP Overlap\\n\\n- Both passed: **5/18**\\n- Jaccard similarity: 16.1%\\n- Standard-only (13): HumanEval/133, HumanEval/135, HumanEval/136, HumanEval/138, HumanEval/144, HumanEval/35, HumanEval/45, HumanEval/49, HumanEval/51, HumanEval/53, HumanEval/60, HumanEval/90, HumanEval/97\\n- RASP-only (13): HumanEval/102, HumanEval/12, HumanEval/151, HumanEval/154, HumanEval/29, HumanEval/3, HumanEval/34, HumanEval/47, HumanEval/69, HumanEval/73, HumanEval/74, HumanEval/82, HumanEval/92\\n\\n**Conclusion**: Moderate overlap (5/18). RASP and Standard pruning preserve partially different code capabilities.\\n\\n## Key Finding 2: CKA-only Superset Analysis\\n\\n- CKA-only union (SFT CKA ∪ GRPO CKA): **49** unique tasks\\n- Standard ∪ RASP union: **31** unique tasks\\n- Overlap (both groups pass): **18**\\n- CKA superset of Standard/RASP? **No** (covers 18/31 of Standard/RASP tasks)\\n\\n- Standard/RASP-only tasks (13): HumanEval/13, HumanEval/135, HumanEval/136, HumanEval/138, HumanEval/144, HumanEval/154, HumanEval/29, HumanEval/34, HumanEval/35, HumanEval/69, HumanEval/73, HumanEval/74, HumanEval/82\\n- CKA-exclusive tasks (31): HumanEval/104, HumanEval/106, HumanEval/111, HumanEval/112, HumanEval/115, HumanEval/123, HumanEval/139, HumanEval/155, HumanEval/159, HumanEval/17, HumanEval/2, HumanEval/21, HumanEval/22, HumanEval/27, HumanEval/30, HumanEval/4, HumanEval/40, HumanEval/42, HumanEval/44, HumanEval/5, HumanEval/52, HumanEval/55, HumanEval/63, HumanEval/68, HumanEval/7, HumanEval/72, HumanEval/8, HumanEval/85, HumanEval/88, HumanEval/9, HumanEval/96\\n\\n## Key Finding 3: SFT CKA -> GRPO CKA Transition\\n\\n- Both passed: **17**\\n- SFT-only (GRPO lost, 16): HumanEval/102, HumanEval/104, HumanEval/106, HumanEval/111, HumanEval/123, HumanEval/155, HumanEval/157, HumanEval/31, HumanEval/45, HumanEval/47, HumanEval/5, HumanEval/60, HumanEval/85, HumanEval/9, HumanEval/92, HumanEval/96\\n- GRPO-only (GRPO gained, 16): HumanEval/112, HumanEval/12, HumanEval/133, HumanEval/139, HumanEval/151, HumanEval/17, HumanEval/4, HumanEval/42, HumanEval/44, HumanEval/55, HumanEval/63, HumanEval/68, HumanEval/72, HumanEval/88, HumanEval/90, HumanEval/97\\n- Net effect: 33 - 33 = **+0** (GRPO lost 16, gained 16)\\n\\n## B. CKA-only Exclusive Tasks (Detailed)\\n\\nTasks passed by CKA-only models (SFT or GRPO) but failed by both GRPO Standard and GRPO RASP:\\n\\n| # | Task ID | SFT CKA | GRPO CKA |\\n|---|---------|---------|----------|\\n| 1 | HumanEval/104 | Pass | Fail |\\n| 2 | HumanEval/106 | Pass | Fail |\\n| 3 | HumanEval/111 | Pass | Fail |\\n| 4 | HumanEval/112 | Fail | Pass |\\n| 5 | HumanEval/115 | Pass | Pass |\\n| 6 | HumanEval/123 | Pass | Fail |\\n| 7 | HumanEval/139 | Fail | Pass |\\n| 8 | HumanEval/155 | Pass | Fail |\\n| 9 | HumanEval/159 | Pass | Pass |\\n| 10 | HumanEval/17 | Fail | Pass |\\n| 11 | HumanEval/2 | Pass | Pass |\\n| 12 | HumanEval/21 | Pass | Pass |\\n| 13 | HumanEval/22 | Pass | Pass |\\n| 14 | HumanEval/27 | Pass | Pass |\\n| 15 | HumanEval/30 | Pass | Pass |\\n| 16 | HumanEval/4 | Fail | Pass |\\n| 17 | HumanEval/40 | Pass | Pass |\\n| 18 | HumanEval/42 | Fail | Pass |\\n| 19 | HumanEval/44 | Fail | Pass |\\n| 20 | HumanEval/5 | Pass | Fail |\\n| 21 | HumanEval/52 | Pass | Pass |\\n| 22 | HumanEval/55 | Fail | Pass |\\n| 23 | HumanEval/63 | Fail | Pass |\\n| 24 | HumanEval/68 | Fail | Pass |\\n| 25 | HumanEval/7 | Pass | Pass |\\n| 26 | HumanEval/72 | Fail | Pass |\\n| 27 | HumanEval/8 | Pass | Pass |\\n| 28 | HumanEval/85 | Pass | Fail |\\n| 29 | HumanEval/88 | Fail | Pass |\\n| 30 | HumanEval/9 | Pass | Fail |\\n| 31 | HumanEval/96 | Pass | Fail |\\n\\n## Interpretation\\n\\nGRPO Standard and GRPO RASP share only 5/31 tasks (16% Jaccard). The two pruning strategies preserve meaningfully different code capabilities after GRPO recovery.\\n\\nCKA-only covers 18/31 Standard/RASP tasks and adds 31 exclusive tasks, but loses 13 tasks (HumanEval/13, HumanEval/135, HumanEval/136, HumanEval/138, HumanEval/144, HumanEval/154, HumanEval/29, HumanEval/34, HumanEval/35, HumanEval/69, HumanEval/73, HumanEval/74, HumanEval/82). The capability profiles partially diverge.\\n\\nSFT->GRPO CKA maintains the same pass count (33) but with 16 task swaps: GRPO loses 16 SFT tasks and gains 16 new ones. This suggests GRPO redistributes capability rather than expanding it.\\n\\n\\n--- Saved to /root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_overlap_analysis.md ---\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.49}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 24_

Now registering the artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d836da91-4539-49aa-93c2-ff86c541bac4",
  "uuid": "73dc302a-5afc-4b0b-a0a8-54286be2b24a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vy3h4vPWBZPNkfwgr61fYH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5918,
      "cache_read_input_tokens": 31191,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5918
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

_source line 25_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01LjpTJw2a158ieXQ3j17nuh`</summary>

```json
{
  "name": "HumanEval Overlap Analysis",
  "type": "analysis",
  "description": "Pairwise overlap analysis of 4 HumanEval evaluations (GRPO Standard, GRPO RASP, SFT CKA-only, GRPO CKA-only) including overlap matrix, superset analysis, and SFT->GRPO transition analysis",
  "project": "recovery_aware_struct_prune",
  "source_path": "/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_overlap_analysis.md",
  "tags": [
    "humaneval",
    "overlap",
    "evaluation",
    "D072"
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
  "session_id": "d836da91-4539-49aa-93c2-ff86c541bac4",
  "uuid": "12c6c16c-e67b-4f5c-9a4e-05d74428e3c4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vy3h4vPWBZPNkfwgr61fYH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5918,
      "cache_read_input_tokens": 31191,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5918
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

_source line 26 · 2026-05-19T11:24:28.026Z_

<details><summary>↩ Tool result · `toolu_01LjpTJw2a158ieXQ3j17nuh`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid type 'analysis'. Must be one of: ['chart', 'data', 'feishu_doc', 'intermediate', 'paper', 'report', 'video']\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d836da91-4539-49aa-93c2-ff86c541bac4",
  "uuid": "2f95f2bb-1249-4899-a8e3-5ac2f4cc3c5c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"Invalid type 'analysis'. Must be one of: ['chart', 'data', 'feishu_doc', 'intermediate', 'paper', 'report', 'video']\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Invalid type 'analysis'. Must be one of: ['chart', 'data', 'feishu_doc', 'intermediate', 'paper', 'report', 'video']\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01FNXJNWGBfvepQ8JarpjLsK`</summary>

```json
{
  "name": "HumanEval Overlap Analysis",
  "type": "report",
  "description": "Pairwise overlap analysis of 4 HumanEval evaluations (GRPO Standard, GRPO RASP, SFT CKA-only, GRPO CKA-only) including overlap matrix, superset analysis, and SFT->GRPO transition analysis",
  "project": "recovery_aware_struct_prune",
  "source_path": "/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_overlap_analysis.md",
  "tags": [
    "humaneval",
    "overlap",
    "evaluation",
    "D072"
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
  "session_id": "d836da91-4539-49aa-93c2-ff86c541bac4",
  "uuid": "64a2cfe2-bf69-4444-baee-6bcb62b4baaa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XfHEjHd5FJXq3o9AxF12tG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 357,
      "cache_read_input_tokens": 37109,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 357
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

_source line 28 · 2026-05-19T11:24:33.945Z_

<details><summary>↩ Tool result · `toolu_01FNXJNWGBfvepQ8JarpjLsK`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"source_path not found: /root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_overlap_analysis.md\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d836da91-4539-49aa-93c2-ff86c541bac4",
  "uuid": "5257f6d1-6992-4dbf-9954-7dc4c66ce509",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"source_path not found: /root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_overlap_analysis.md\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"source_path not found: /root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_overlap_analysis.md\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 29_

Source path is on the remote server. Let me read the file content and register via `content` parameter instead.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d836da91-4539-49aa-93c2-ff86c541bac4",
  "uuid": "5ffd544c-6b12-46c6-93f4-7ebc06f37033",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YKxHPKWhwW2C3jNg875k7T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 341,
      "cache_read_input_tokens": 37466,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 341
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

_source line 30_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01RR5fcPLehG41u9Au3HBTeA`</summary>

```json
{
  "server": "westd-29022",
  "command": "cat /root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_overlap_analysis.md",
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
  "session_id": "d836da91-4539-49aa-93c2-ff86c541bac4",
  "uuid": "4d506783-9eb2-425d-94ae-fa3fda24818a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YKxHPKWhwW2C3jNg875k7T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 341,
      "cache_read_input_tokens": 37466,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 341
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

_source line 31 · 2026-05-19T11:24:38.833Z_

<details><summary>↩ Tool result · `toolu_01RR5fcPLehG41u9Au3HBTeA`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"# HumanEval Overlap Analysis\\n\\n## Summary\\n| Model | Passed | Total | Pass@1 |\\n|-------|--------|-------|--------|\\n| GRPO_Standard | 18 | 164 | 11.0% |\\n| GRPO_RASP | 18 | 164 | 11.0% |\\n| SFT_CKA | 33 | 164 | 20.1% |\\n| GRPO_CKA | 33 | 164 | 20.1% |\\n\\n## A. Pairwise Overlap Matrix\\n\\n| A vs B | Both Pass | A-only | B-only | Both Fail |\\n|--------|-----------|--------|--------|-----------|\\n| Std vs RASP | 5 | 13 | 13 | 133 |\\n| Std vs SFT-CKA | 9 | 9 | 24 | 122 |\\n| Std vs GRPO-CKA | 8 | 10 | 25 | 121 |\\n| RASP vs SFT-CKA | 8 | 10 | 25 | 121 |\\n| RASP vs GRPO-CKA | 5 | 13 | 28 | 118 |\\n| SFT-CKA vs GRPO-CKA | 17 | 16 | 16 | 115 |\\n\\n## Key Finding 1: GRPO Standard vs RASP Overlap\\n\\n- Both passed: **5/18**\\n- Jaccard similarity: 16.1%\\n- Standard-only (13): HumanEval/133, HumanEval/135, HumanEval/136, HumanEval/138, HumanEval/144, HumanEval/35, HumanEval/45, HumanEval/49, HumanEval/51, HumanEval/53, HumanEval/60, HumanEval/90, HumanEval/97\\n- RASP-only (13): HumanEval/102, HumanEval/12, HumanEval/151, HumanEval/154, HumanEval/29, HumanEval/3, HumanEval/34, HumanEval/47, HumanEval/69, HumanEval/73, HumanEval/74, HumanEval/82, HumanEval/92\\n\\n**Conclusion**: Moderate overlap (5/18). RASP and Standard pruning preserve partially different code capabilities.\\n\\n## Key Finding 2: CKA-only Superset Analysis\\n\\n- CKA-only union (SFT CKA ∪ GRPO CKA): **49** unique tasks\\n- Standard ∪ RASP union: **31** unique tasks\\n- Overlap (both groups pass): **18**\\n- CKA superset of Standard/RASP? **No** (covers 18/31 of Standard/RASP tasks)\\n\\n- Standard/RASP-only tasks (13): HumanEval/13, HumanEval/135, HumanEval/136, HumanEval/138, HumanEval/144, HumanEval/154, HumanEval/29, HumanEval/34, HumanEval/35, HumanEval/69, HumanEval/73, HumanEval/74, HumanEval/82\\n- CKA-exclusive tasks (31): HumanEval/104, HumanEval/106, HumanEval/111, HumanEval/112, HumanEval/115, HumanEval/123, HumanEval/139, HumanEval/155, HumanEval/159, HumanEval/17, HumanEval/2, HumanEval/21, HumanEval/22, HumanEval/27, HumanEval/30, HumanEval/4, HumanEval/40, HumanEval/42, HumanEval/44, HumanEval/5, HumanEval/52, HumanEval/55, HumanEval/63, HumanEval/68, HumanEval/7, HumanEval/72, HumanEval/8, HumanEval/85, HumanEval/88, HumanEval/9, HumanEval/96\\n\\n## Key Finding 3: SFT CKA -> GRPO CKA Transition\\n\\n- Both passed: **17**\\n- SFT-only (GRPO lost, 16): HumanEval/102, HumanEval/104, HumanEval/106, HumanEval/111, HumanEval/123, HumanEval/155, HumanEval/157, HumanEval/31, HumanEval/45, HumanEval/47, HumanEval/5, HumanEval/60, HumanEval/85, HumanEval/9, HumanEval/92, HumanEval/96\\n- GRPO-only (GRPO gained, 16): HumanEval/112, HumanEval/12, HumanEval/133, HumanEval/139, HumanEval/151, HumanEval/17, HumanEval/4, HumanEval/42, HumanEval/44, HumanEval/55, HumanEval/63, HumanEval/68, HumanEval/72, HumanEval/88, HumanEval/90, HumanEval/97\\n- Net effect: 33 - 33 = **+0** (GRPO lost 16, gained 16)\\n\\n## B. CKA-only Exclusive Tasks (Detailed)\\n\\nTasks passed by CKA-only models (SFT or GRPO) but failed by both GRPO Standard and GRPO RASP:\\n\\n| # | Task ID | SFT CKA | GRPO CKA |\\n|---|---------|---------|----------|\\n| 1 | HumanEval/104 | Pass | Fail |\\n| 2 | HumanEval/106 | Pass | Fail |\\n| 3 | HumanEval/111 | Pass | Fail |\\n| 4 | HumanEval/112 | Fail | Pass |\\n| 5 | HumanEval/115 | Pass | Pass |\\n| 6 | HumanEval/123 | Pass | Fail |\\n| 7 | HumanEval/139 | Fail | Pass |\\n| 8 | HumanEval/155 | Pass | Fail |\\n| 9 | HumanEval/159 | Pass | Pass |\\n| 10 | HumanEval/17 | Fail | Pass |\\n| 11 | HumanEval/2 | Pass | Pass |\\n| 12 | HumanEval/21 | Pass | Pass |\\n| 13 | HumanEval/22 | Pass | Pass |\\n| 14 | HumanEval/27 | Pass | Pass |\\n| 15 | HumanEval/30 | Pass | Pass |\\n| 16 | HumanEval/4 | Fail | Pass |\\n| 17 | HumanEval/40 | Pass | Pass |\\n| 18 | HumanEval/42 | Fail | Pass |\\n| 19 | HumanEval/44 | Fail | Pass |\\n| 20 | HumanEval/5 | Pass | Fail |\\n| 21 | HumanEval/52 | Pass | Pass |\\n| 22 | HumanEval/55 | Fail | Pass |\\n| 23 | HumanEval/63 | Fail | Pass |\\n| 24 | HumanEval/68 | Fail | Pass |\\n| 25 | HumanEval/7 | Pass | Pass |\\n| 26 | HumanEval/72 | Fail | Pass |\\n| 27 | HumanEval/8 | Pass | Pass |\\n| 28 | HumanEval/85 | Pass | Fail |\\n| 29 | HumanEval/88 | Fail | Pass |\\n| 30 | HumanEval/9 | Pass | Fail |\\n| 31 | HumanEval/96 | Pass | Fail |\\n\\n## Interpretation\\n\\nGRPO Standard and GRPO RASP share only 5/31 tasks (16% Jaccard). The two pruning strategies preserve meaningfully different code capabilities after GRPO recovery.\\n\\nCKA-only covers 18/31 Standard/RASP tasks and adds 31 exclusive tasks, but loses 13 tasks (HumanEval/13, HumanEval/135, HumanEval/136, HumanEval/138, HumanEval/144, HumanEval/154, HumanEval/29, HumanEval/34, HumanEval/35, HumanEval/69, HumanEval/73, HumanEval/74, HumanEval/82). The capability profiles partially diverge.\\n\\nSFT->GRPO CKA maintains the same pass count (33) but with 16 task swaps: GRPO loses 16 SFT tasks and gains 16 new ones. This suggests GRPO redistributes capability rather than expanding it.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d836da91-4539-49aa-93c2-ff86c541bac4",
  "uuid": "4c36b136-a34e-42f3-9a65-add98382f542",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"# HumanEval Overlap Analysis\\\\n\\\\n## Summary\\\\n| Model | Passed | Total | Pass@1 |\\\\n|-------|--------|-------|--------|\\\\n| GRPO_Standard | 18 | 164 | 11.0% |\\\\n| GRPO_RASP | 18 | 164 | 11.0% |\\\\n| SFT_CKA | 33 | 164 | 20.1% |\\\\n| GRPO_CKA | 33 | 164 | 20.1% |\\\\n\\\\n## A. Pairwise Overlap Matrix\\\\n\\\\n| A vs B | Both Pass | A-only | B-only | Both Fail |\\\\n|--------|-----------|--------|--------|-----------|\\\\n| Std vs RASP | 5 | 13 | 13 | 133 |\\\\n| Std vs SFT-CKA | 9 | 9 | 24 | 122 |\\\\n| Std vs GRPO-CKA | 8 | 10 | 25 | 121 |\\\\n| RASP vs SFT-CKA | 8 | 10 | 25 | 121 |\\\\n| RASP vs GRPO-CKA | 5 | 13 | 28 | 118 |\\\\n| SFT-CKA vs GRPO-CKA | 17 | 16 | 16 | 115 |\\\\n\\\\n## Key Finding 1: GRPO Standard vs RASP Overlap\\\\n\\\\n- Both passed: **5/18**\\\\n- Jaccard similarity: 16.1%\\\\n- Standard-only (13): HumanEval/133, HumanEval/135, HumanEval/136, HumanEval/138, HumanEval/144, HumanEval/35, HumanEval/45, HumanEval/49, HumanEval/51, HumanEval/53, HumanEval/60, HumanEval/90, HumanEval/97\\\\n- RASP-only (13): HumanEval/102, HumanEval/12, HumanEval/151, HumanEval/154, HumanEval/29, HumanEval/3, HumanEval/34, HumanEval/47, HumanEval/69, HumanEval/73, HumanEval/74, HumanEval/82, HumanEval/92\\\\n\\\\n**Conclusion**: Moderate overlap (5/18). RASP and Standard pruning preserve partially different code capabilities.\\\\n\\\\n## Key Finding 2: CKA-only Superset Analysis\\\\n\\\\n- CKA-only union (SFT CKA ∪ GRPO CKA): **49** unique tasks\\\\n- Standard ∪ RASP union: **31** unique tasks\\\\n- Overlap (both groups pass): **18**\\\\n- CKA superset of Standard/RASP? **No** (covers 18/31 of Standard/RASP tasks)\\\\n\\\\n- Standard/RASP-only tasks (13): HumanEval/13, HumanEval/135, HumanEval/136, HumanEval/138, HumanEval/144, HumanEval/154, HumanEval/29, HumanEval/34, HumanEval/35, HumanEval/69, HumanEval/73, HumanEval/74, HumanEval/82\\\\n- CKA-exclusive tasks (31): HumanEval/104, HumanEval/106, HumanEval/111, HumanEval/112, HumanEval/115, HumanEval/123, HumanEval/139, HumanEval/155, HumanEval/159, HumanEval/17, HumanEval/2, HumanEval/21, HumanEval/22, HumanEval/27, HumanEval/30, HumanEval/4, HumanEval/40, HumanEval/42, HumanEval/44, HumanEval/5, HumanEval/52, HumanEval/55, HumanEval/63, HumanEval/68, HumanEval/7, HumanEval/72, HumanEval/8, HumanEval/85, HumanEval/88, HumanEval/9, HumanEval/96\\\\n\\\\n## Key Finding 3: SFT CKA -> GRPO CKA Transition\\\\n\\\\n- Both passed: **17**\\\\n- SFT-only (GRPO lost, 16): HumanEval/102, HumanEval/104, HumanEval/106, HumanEval/111, HumanEval/123, HumanEval/155, HumanEval/157, HumanEval/31, HumanEval/45, HumanEval/47, HumanEval/5, HumanEval/60, HumanEval/85, HumanEval/9, HumanEval/92, HumanEval/96\\\\n- GRPO-only (GRPO gained, 16): HumanEval/112, HumanEval/12, HumanEval/133, HumanEval/139, HumanEval/151, HumanEval/17, HumanEval/4, HumanEval/42, HumanEval/44, HumanEval/55, HumanEval/63, HumanEval/68, HumanEval/72, HumanEval/88, HumanEval/90, HumanEval/97\\\\n- Net effect: 33 - 33 = **+0** (GRPO lost 16, gained 16)\\\\n\\\\n## B. CKA-only Exclusive Tasks (Detailed)\\\\n\\\\nTasks passed by CKA-only models (SFT or GRPO) but failed by both GRPO Standard and GRPO RASP:\\\\n\\\\n| # | Task ID | SFT CKA | GRPO CKA |\\\\n|---|---------|---------|----------|\\\\n| 1 | HumanEval/104 | Pass | Fail |\\\\n| 2 | HumanEval/106 | Pass | Fail |\\\\n| 3 | HumanEval/111 | Pass | Fail |\\\\n| 4 | HumanEval/112 | Fail | Pass |\\\\n| 5 | HumanEval/115 | Pass | Pass |\\\\n| 6 | HumanEval/123 | Pass | Fail |\\\\n| 7 | HumanEval/139 | Fail | Pass |\\\\n| 8 | HumanEval/155 | Pass | Fail |\\\\n| 9 | HumanEval/159 | Pass | Pass |\\\\n| 10 | HumanEval/17 | Fail | Pass |\\\\n| 11 | HumanEval/2 | Pass | Pass |\\\\n| 12 | HumanEval/21 | Pass | Pass |\\\\n| 13 | HumanEval/22 | Pass | Pass |\\\\n| 14 | HumanEval/27 | Pass | Pass |\\\\n| 15 | HumanEval/30 | Pass | Pass |\\\\n| 16 | HumanEval/4 | Fail | Pass |\\\\n| 17 | HumanEval/40 | Pass | Pass |\\\\n| 18 | HumanEval/42 | Fail | Pass |\\\\n| 19 | HumanEval/44 | Fail | Pass |\\\\n| 20 | HumanEval/5 | Pass | Fail |\\\\n| 21 | HumanEval/52 | Pass | Pass |\\\\n| 22 | HumanEval/55 | Fail | Pass |\\\\n| 23 | HumanEval/63 | Fail | Pass |\\\\n| 24 | HumanEval/68 | Fail | Pass |\\\\n| 25 | HumanEval/7 | Pass | Pass |\\\\n| 26 | HumanEval/72 | Fail | Pass |\\\\n| 27 | HumanEval/8 | Pass | Pass |\\\\n| 28 | HumanEval/85 | Pass | Fail |\\\\n| 29 | HumanEval/88 | Fail | Pass |\\\\n| 30 | HumanEval/9 | Pass | Fail |\\\\n| 31 | HumanEval/96 | Pass | Fail |\\\\n\\\\n## Interpretation\\\\n\\\\nGRPO Standard and GRPO RASP share only 5/31 tasks (16% Jaccard). The two pruning strategies preserve meaningfully different code capabilities after GRPO recovery.\\\\n\\\\nCKA-only covers 18/31 Standard/RASP tasks and adds 31 exclusive tasks, but loses 13 tasks (HumanEval/13, HumanEval/135, HumanEval/136, HumanEval/138, HumanEval/144, HumanEval/154, HumanEval/29, HumanEval/34, HumanEval/35, HumanEval/69, HumanEval/73, HumanEval/74, HumanEval/82). The capability profiles partially diverge.\\\\n\\\\nSFT->GRPO CKA maintains the same pass count (33) but with 16 task swaps: GRPO loses 16 SFT tasks and gains 16 new ones. This suggests GRPO redistributes capability rather than expanding it.\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"# HumanEval Overlap Analysis\\n\\n## Summary\\n| Model | Passed | Total | Pass@1 |\\n|-------|--------|-------|--------|\\n| GRPO_Standard | 18 | 164 | 11.0% |\\n| GRPO_RASP | 18 | 164 | 11.0% |\\n| SFT_CKA | 33 | 164 | 20.1% |\\n| GRPO_CKA | 33 | 164 | 20.1% |\\n\\n## A. Pairwise Overlap Matrix\\n\\n| A vs B | Both Pass | A-only | B-only | Both Fail |\\n|--------|-----------|--------|--------|-----------|\\n| Std vs RASP | 5 | 13 | 13 | 133 |\\n| Std vs SFT-CKA | 9 | 9 | 24 | 122 |\\n| Std vs GRPO-CKA | 8 | 10 | 25 | 121 |\\n| RASP vs SFT-CKA | 8 | 10 | 25 | 121 |\\n| RASP vs GRPO-CKA | 5 | 13 | 28 | 118 |\\n| SFT-CKA vs GRPO-CKA | 17 | 16 | 16 | 115 |\\n\\n## Key Finding 1: GRPO Standard vs RASP Overlap\\n\\n- Both passed: **5/18**\\n- Jaccard similarity: 16.1%\\n- Standard-only (13): HumanEval/133, HumanEval/135, HumanEval/136, HumanEval/138, HumanEval/144, HumanEval/35, HumanEval/45, HumanEval/49, HumanEval/51, HumanEval/53, HumanEval/60, HumanEval/90, HumanEval/97\\n- RASP-only (13): HumanEval/102, HumanEval/12, HumanEval/151, HumanEval/154, HumanEval/29, HumanEval/3, HumanEval/34, HumanEval/47, HumanEval/69, HumanEval/73, HumanEval/74, HumanEval/82, HumanEval/92\\n\\n**Conclusion**: Moderate overlap (5/18). RASP and Standard pruning preserve partially different code capabilities.\\n\\n## Key Finding 2: CKA-only Superset Analysis\\n\\n- CKA-only union (SFT CKA ∪ GRPO CKA): **49** unique tasks\\n- Standard ∪ RASP union: **31** unique tasks\\n- Overlap (both groups pass): **18**\\n- CKA superset of Standard/RASP? **No** (covers 18/31 of Standard/RASP tasks)\\n\\n- Standard/RASP-only tasks (13): HumanEval/13, HumanEval/135, HumanEval/136, HumanEval/138, HumanEval/144, HumanEval/154, HumanEval/29, HumanEval/34, HumanEval/35, HumanEval/69, HumanEval/73, HumanEval/74, HumanEval/82\\n- CKA-exclusive tasks (31): HumanEval/104, HumanEval/106, HumanEval/111, HumanEval/112, HumanEval/115, HumanEval/123, HumanEval/139, HumanEval/155, HumanEval/159, HumanEval/17, HumanEval/2, HumanEval/21, HumanEval/22, HumanEval/27, HumanEval/30, HumanEval/4, HumanEval/40, HumanEval/42, HumanEval/44, HumanEval/5, HumanEval/52, HumanEval/55, HumanEval/63, HumanEval/68, HumanEval/7, HumanEval/72, HumanEval/8, HumanEval/85, HumanEval/88, HumanEval/9, HumanEval/96\\n\\n## Key Finding 3: SFT CKA -> GRPO CKA Transition\\n\\n- Both passed: **17**\\n- SFT-only (GRPO lost, 16): HumanEval/102, HumanEval/104, HumanEval/106, HumanEval/111, HumanEval/123, HumanEval/155, HumanEval/157, HumanEval/31, HumanEval/45, HumanEval/47, HumanEval/5, HumanEval/60, HumanEval/85, HumanEval/9, HumanEval/92, HumanEval/96\\n- GRPO-only (GRPO gained, 16): HumanEval/112, HumanEval/12, HumanEval/133, HumanEval/139, HumanEval/151, HumanEval/17, HumanEval/4, HumanEval/42, HumanEval/44, HumanEval/55, HumanEval/63, HumanEval/68, HumanEval/72, HumanEval/88, HumanEval/90, HumanEval/97\\n- Net effect: 33 - 33 = **+0** (GRPO lost 16, gained 16)\\n\\n## B. CKA-only Exclusive Tasks (Detailed)\\n\\nTasks passed by CKA-only models (SFT or GRPO) but failed by both GRPO Standard and GRPO RASP:\\n\\n| # | Task ID | SFT CKA | GRPO CKA |\\n|---|---------|---------|----------|\\n| 1 | HumanEval/104 | Pass | Fail |\\n| 2 | HumanEval/106 | Pass | Fail |\\n| 3 | HumanEval/111 | Pass | Fail |\\n| 4 | HumanEval/112 | Fail | Pass |\\n| 5 | HumanEval/115 | Pass | Pass |\\n| 6 | HumanEval/123 | Pass | Fail |\\n| 7 | HumanEval/139 | Fail | Pass |\\n| 8 | HumanEval/155 | Pass | Fail |\\n| 9 | HumanEval/159 | Pass | Pass |\\n| 10 | HumanEval/17 | Fail | Pass |\\n| 11 | HumanEval/2 | Pass | Pass |\\n| 12 | HumanEval/21 | Pass | Pass |\\n| 13 | HumanEval/22 | Pass | Pass |\\n| 14 | HumanEval/27 | Pass | Pass |\\n| 15 | HumanEval/30 | Pass | Pass |\\n| 16 | HumanEval/4 | Fail | Pass |\\n| 17 | HumanEval/40 | Pass | Pass |\\n| 18 | HumanEval/42 | Fail | Pass |\\n| 19 | HumanEval/44 | Fail | Pass |\\n| 20 | HumanEval/5 | Pass | Fail |\\n| 21 | HumanEval/52 | Pass | Pass |\\n| 22 | HumanEval/55 | Fail | Pass |\\n| 23 | HumanEval/63 | Fail | Pass |\\n| 24 | HumanEval/68 | Fail | Pass |\\n| 25 | HumanEval/7 | Pass | Pass |\\n| 26 | HumanEval/72 | Fail | Pass |\\n| 27 | HumanEval/8 | Pass | Pass |\\n| 28 | HumanEval/85 | Pass | Fail |\\n| 29 | HumanEval/88 | Fail | Pass |\\n| 30 | HumanEval/9 | Pass | Fail |\\n| 31 | HumanEval/96 | Pass | Fail |\\n\\n## Interpretation\\n\\nGRPO Standard and GRPO RASP share only 5/31 tasks (16% Jaccard). The two pruning strategies preserve meaningfully different code capabilities after GRPO recovery.\\n\\nCKA-only covers 18/31 Standard/RASP tasks and adds 31 exclusive tasks, but loses 13 tasks (HumanEval/13, HumanEval/135, HumanEval/136, HumanEval/138, HumanEval/144, HumanEval/154, HumanEval/29, HumanEval/34, HumanEval/35, HumanEval/69, HumanEval/73, HumanEval/74, HumanEval/82). The capability profiles partially diverge.\\n\\nSFT->GRPO CKA maintains the same pass count (33) but with 16 task swaps: GRPO loses 16 SFT tasks and gains 16 new ones. This suggests GRPO redistributes capability rather than expanding it.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01GwdPdguHPPJhUEA7NcQedu`</summary>

```json
{
  "name": "HumanEval Overlap Analysis",
  "type": "report",
  "description": "Pairwise overlap analysis of 4 HumanEval evaluations (GRPO Standard, GRPO RASP, SFT CKA-only, GRPO CKA-only) including overlap matrix, superset analysis, and SFT->GRPO transition analysis",
  "project": "recovery_aware_struct_prune",
  "content_filename": "humaneval_overlap_analysis.md",
  "content": "# HumanEval Overlap Analysis\n\n## Summary\n| Model | Passed | Total | Pass@1 |\n|-------|--------|-------|--------|\n| GRPO_Standard | 18 | 164 | 11.0% |\n| GRPO_RASP | 18 | 164 | 11.0% |\n| SFT_CKA | 33 | 164 | 20.1% |\n| GRPO_CKA | 33 | 164 | 20.1% |\n\n## A. Pairwise Overlap Matrix\n\n| A vs B | Both Pass | A-only | B-only | Both Fail |\n|--------|-----------|--------|--------|-----------|\n| Std vs RASP | 5 | 13 | 13 | 133 |\n| Std vs SFT-CKA | 9 | 9 | 24 | 122 |\n| Std vs GRPO-CKA | 8 | 10 | 25 | 121 |\n| RASP vs SFT-CKA | 8 | 10 | 25 | 121 |\n| RASP vs GRPO-CKA | 5 | 13 | 28 | 118 |\n| SFT-CKA vs GRPO-CKA | 17 | 16 | 16 | 115 |\n\n## Key Finding 1: GRPO Standard vs RASP Overlap\n\n- Both passed: **5/18**\n- Jaccard similarity: 16.1%\n- Standard-only (13): HumanEval/133, HumanEval/135, HumanEval/136, HumanEval/138, HumanEval/144, HumanEval/35, HumanEval/45, HumanEval/49, HumanEval/51, HumanEval/53, HumanEval/60, HumanEval/90, HumanEval/97\n- RASP-only (13): HumanEval/102, HumanEval/12, HumanEval/151, HumanEval/154, HumanEval/29, HumanEval/3, HumanEval/34, HumanEval/47, HumanEval/69, HumanEval/73, HumanEval/74, HumanEval/82, HumanEval/92\n\n**Conclusion**: Moderate overlap (5/18). RASP and Standard pruning preserve partially different code capabilities.\n\n## Key Finding 2: CKA-only Superset Analysis\n\n- CKA-only union (SFT CKA ∪ GRPO CKA): **49** unique tasks\n- Standard ∪ RASP union: **31** unique tasks\n- Overlap (both groups pass): **18**\n- CKA superset of Standard/RASP? **No** (covers 18/31 of Standard/RASP tasks)\n\n- Standard/RASP-only tasks (13): HumanEval/13, HumanEval/135, HumanEval/136, HumanEval/138, HumanEval/144, HumanEval/154, HumanEval/29, HumanEval/34, HumanEval/35, HumanEval/69, HumanEval/73, HumanEval/74, HumanEval/82\n- CKA-exclusive tasks (31): HumanEval/104, HumanEval/106, HumanEval/111, HumanEval/112, HumanEval/115, HumanEval/123, HumanEval/139, HumanEval/155, HumanEval/159, HumanEval/17, HumanEval/2, HumanEval/21, HumanEval/22, HumanEval/27, HumanEval/30, HumanEval/4, HumanEval/40, HumanEval/42, HumanEval/44, HumanEval/5, HumanEval/52, HumanEval/55, HumanEval/63, HumanEval/68, HumanEval/7, HumanEval/72, HumanEval/8, HumanEval/85, HumanEval/88, HumanEval/9, HumanEval/96\n\n## Key Finding 3: SFT CKA -> GRPO CKA Transition\n\n- Both passed: **17**\n- SFT-only (GRPO lost, 16): HumanEval/102, HumanEval/104, HumanEval/106, HumanEval/111, HumanEval/123, HumanEval/155, HumanEval/157, HumanEval/31, HumanEval/45, HumanEval/47, HumanEval/5, HumanEval/60, HumanEval/85, HumanEval/9, HumanEval/92, HumanEval/96\n- GRPO-only (GRPO gained, 16): HumanEval/112, HumanEval/12, HumanEval/133, HumanEval/139, HumanEval/151, HumanEval/17, HumanEval/4, HumanEval/42, HumanEval/44, HumanEval/55, HumanEval/63, HumanEval/68, HumanEval/72, HumanEval/88, HumanEval/90, HumanEval/97\n- Net effect: 33 - 33 = **+0** (GRPO lost 16, gained 16)\n\n## B. CKA-only Exclusive Tasks (Detailed)\n\nTasks passed by CKA-only models (SFT or GRPO) but failed by both GRPO Standard and GRPO RASP:\n\n| # | Task ID | SFT CKA | GRPO CKA |\n|---|---------|---------|----------|\n| 1 | HumanEval/104 | Pass | Fail |\n| 2 | HumanEval/106 | Pass | Fail |\n| 3 | HumanEval/111 | Pass | Fail |\n| 4 | HumanEval/112 | Fail | Pass |\n| 5 | HumanEval/115 | Pass | Pass |\n| 6 | HumanEval/123 | Pass | Fail |\n| 7 | HumanEval/139 | Fail | Pass |\n| 8 | HumanEval/155 | Pass | Fail |\n| 9 | HumanEval/159 | Pass | Pass |\n| 10 | HumanEval/17 | Fail | Pass |\n| 11 | HumanEval/2 | Pass | Pass |\n| 12 | HumanEval/21 | Pass | Pass |\n| 13 | HumanEval/22 | Pass | Pass |\n| 14 | HumanEval/27 | Pass | Pass |\n| 15 | HumanEval/30 | Pass | Pass |\n| 16 | HumanEval/4 | Fail | Pass |\n| 17 | HumanEval/40 | Pass | Pass |\n| 18 | HumanEval/42 | Fail | Pass |\n| 19 | HumanEval/44 | Fail | Pass |\n| 20 | HumanEval/5 | Pass | Fail |\n| 21 | HumanEval/52 | Pass | Pass |\n| 22 | HumanEval/55 | Fail | Pass |\n| 23 | HumanEval/63 | Fail | Pass |\n| 24 | HumanEval/68 | Fail | Pass |\n| 25 | HumanEval/7 | Pass | Pass |\n| 26 | HumanEval/72 | Fail | Pass |\n| 27 | HumanEval/8 | Pass | Pass |\n| 28 | HumanEval/85 | Pass | Fail |\n| 29 | HumanEval/88 | Fail | Pass |\n| 30 | HumanEval/9 | Pass | Fail |\n| 31 | HumanEval/96 | Pass | Fail |\n\n## Interpretation\n\nGRPO Standard and GRPO RASP share only 5/31 tasks (16% Jaccard). The two pruning strategies preserve meaningfully different code capabilities after GRPO recovery.\n\nCKA-only covers 18/31 Standard/RASP tasks and adds 31 exclusive tasks, but loses 13 tasks (HumanEval/13, HumanEval/135, HumanEval/136, HumanEval/138, HumanEval/144, HumanEval/154, HumanEval/29, HumanEval/34, HumanEval/35, HumanEval/69, HumanEval/73, HumanEval/74, HumanEval/82). The capability profiles partially diverge.\n\nSFT->GRPO CKA maintains the same pass count (33) but with 16 task swaps: GRPO loses 16 SFT tasks and gains 16 new ones. This suggests GRPO redistributes capability rather than expanding it.",
  "tags": [
    "humaneval",
    "overlap",
    "evaluation",
    "D072"
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
  "session_id": "d836da91-4539-49aa-93c2-ff86c541bac4",
  "uuid": "3978fcda-1b40-4d3d-8d5b-24b0a84a2b8b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HZn3vfoNcqhcQhQ85VaXWf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2745,
      "cache_read_input_tokens": 37807,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2745
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

_source line 33 · 2026-05-19T11:25:03.228Z_

<details><summary>↩ Tool result · `toolu_01GwdPdguHPPJhUEA7NcQedu`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260519_26eadf\", \"name\": \"HumanEval Overlap Analysis\", \"type\": \"report\", \"description\": \"Pairwise overlap analysis of 4 HumanEval evaluations (GRPO Standard, GRPO RASP, SFT CKA-only, GRPO CKA-only) including overlap matrix, superset analysis, and SFT->GRPO transition analysis\", \"path\": \"projects/recovery_aware_struct_prune/artifacts/_project/report/humaneval_overlap_analysis.md\", \"url\": null, \"project\": \"recovery_aware_struct_prune\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-19T11:25:03.017371+00:00\", \"tags\": [\"humaneval\", \"overlap\", \"evaluation\", \"D072\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d836da91-4539-49aa-93c2-ff86c541bac4",
  "uuid": "ae3e3c45-1581-47e6-8e40-b24762e665df",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260519_26eadf\\\", \\\"name\\\": \\\"HumanEval Overlap Analysis\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Pairwise overlap analysis of 4 HumanEval evaluations (GRPO Standard, GRPO RASP, SFT CKA-only, GRPO CKA-only) including overlap matrix, superset analysis, and SFT->GRPO transition analysis\\\", \\\"path\\\": \\\"projects/recovery_aware_struct_prune/artifacts/_project/report/humaneval_overlap_analysis.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"recovery_aware_struct_prune\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-19T11:25:03.017371+00:00\\\", \\\"tags\\\": [\\\"humaneval\\\", \\\"overlap\\\", \\\"evaluation\\\", \\\"D072\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260519_26eadf\", \"name\": \"HumanEval Overlap Analysis\", \"type\": \"report\", \"description\": \"Pairwise overlap analysis of 4 HumanEval evaluations (GRPO Standard, GRPO RASP, SFT CKA-only, GRPO CKA-only) including overlap matrix, superset analysis, and SFT->GRPO transition analysis\", \"path\": \"projects/recovery_aware_struct_prune/artifacts/_project/report/humaneval_overlap_analysis.md\", \"url\": null, \"project\": \"recovery_aware_struct_prune\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-19T11:25:03.017371+00:00\", \"tags\": [\"humaneval\", \"overlap\", \"evaluation\", \"D072\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 34_

分析完成，报告已保存并注册 (`art_20260519_26eadf`)。核心发现：

**Finding 1: GRPO Standard vs RASP 重合度极低**
- 仅 5/31 题重合 (Jaccard 16.1%)，各有 13 题独占
- 虽然总分相同 (18/164)，但解的是**几乎完全不同的题**

**Finding 2: CKA-only 不是 Standard/RASP 的超集**
- CKA union 49 题 vs Standard/RASP union 31 题
- 交集仅 18 题；CKA 独占 31 题，但丢了 13 题 Standard/RASP 能解的
- 三种 pruning 策略保留的代码能力有显著分化

**Finding 3: SFT CKA → GRPO CKA 是纯 redistribution**
- 总分不变 (33/164)，但 16 题丢失、16 题新增，仅 17 题稳定
- GRPO 没有扩展能力，只是重新分配了哪些题能解

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d836da91-4539-49aa-93c2-ff86c541bac4",
  "uuid": "17108000-43fe-4444-acc4-dc967c6cc493",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0196rZELufr3wVARrtZdU9e8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2992,
      "cache_read_input_tokens": 40552,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2992
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

_source line 35_

分析完成，报告已保存并注册 (`art_20260519_26eadf`)。核心发现：

**Finding 1: GRPO Standard vs RASP 重合度极低**
- 仅 5/31 题重合 (Jaccard 16.1%)，各有 13 题独占
- 虽然总分相同 (18/164)，但解的是**几乎完全不同的题**

**Finding 2: CKA-only 不是 Standard/RASP 的超集**
- CKA union 49 题 vs Standard/RASP union 31 题
- 交集仅 18 题；CKA 独占 31 题，但丢了 13 题 Standard/RASP 能解的
- 三种 pruning 策略保留的代码能力有显著分化

**Finding 3: SFT CKA → GRPO CKA 是纯 redistribution**
- 总分不变 (33/164)，但 16 题丢失、16 题新增，仅 17 题稳定
- GRPO 没有扩展能力，只是重新分配了哪些题能解

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 140338,
  "duration_api_ms": 136325,
  "num_turns": 12,
  "stop_reason": "end_turn",
  "session_id": "d836da91-4539-49aa-93c2-ff86c541bac4",
  "total_cost_usd": 0.62122075,
  "usage": {
    "input_tokens": 16,
    "cache_creation_input_tokens": 31703,
    "cache_read_input_tokens": 366222,
    "output_tokens": 9491,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 31703,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 323,
        "cache_read_input_tokens": 40552,
        "cache_creation_input_tokens": 2992,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2992
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2506,
      "outputTokens": 21,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002611,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 16,
      "outputTokens": 9491,
      "cacheReadInputTokens": 366222,
      "cacheCreationInputTokens": 31703,
      "webSearchRequests": 0,
      "costUSD": 0.61860975,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "44c0b7f3-5a21-4c59-9f79-8fcf1ef4116d"
}
```

</details>

---
