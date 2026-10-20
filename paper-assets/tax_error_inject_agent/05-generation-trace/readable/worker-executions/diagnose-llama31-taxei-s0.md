# diagnose llama31 taxei s0

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 34
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/workers/worker_diagnose_llama31-taxei-s0_20260516T115604.log`
- **Structured JSON:** [`d4f4b3d1be855ebc5ce9.json`](../../sessions/d4/d4f4b3d1be855ebc5ce9.json)

## Before a recorded user message

34 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "session_id": "edd9b099-6670-4002-8cb5-5695fd3b3d77",
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
  "uuid": "11616c3b-bbf9-4abb-b628-83fa727fca0d",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/memory/"
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
    "resetsAt": 1778936400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "e1a4181c-d08e-4c97-a538-12ee76b3cd29",
  "session_id": "edd9b099-6670-4002-8cb5-5695fd3b3d77"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me diagnose the training status of llama31-taxei-s0 by checking the server.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "edd9b099-6670-4002-8cb5-5695fd3b3d77",
  "uuid": "34b56b4f-b1ca-410e-a9c1-538c6c304692",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NN31PEWzSKPFu9f7Uf919Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11712,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11712
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

_source line 5_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_019an51tYTyMCKj8havgRZmw`</summary>

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
  "session_id": "edd9b099-6670-4002-8cb5-5695fd3b3d77",
  "uuid": "37ed9811-4d82-4446-b33d-d1b259927e11",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NN31PEWzSKPFu9f7Uf919Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11712,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11712
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

_source line 6 · 2026-05-16T11:56:14.019Z_

<details><summary>↩ Tool result · `toolu_019an51tYTyMCKj8havgRZmw`</summary>

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
  "session_id": "edd9b099-6670-4002-8cb5-5695fd3b3d77",
  "uuid": "12d0b213-fbfa-4722-9042-e50133cac67a",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only",
    "total_deferred_tools": 26
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Let me check the process status, GPU usage, logs, and output directory.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "edd9b099-6670-4002-8cb5-5695fd3b3d77",
  "uuid": "e91dfce9-768e-49d3-a745-c90183bb5bba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GV7BaGnBdW87jftxi6zTxY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 464,
      "cache_read_input_tokens": 23553,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 464
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

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_0187UQAaqu1QNqWaYidm6jyn`</summary>

```json
{
  "server": "autodl-5090",
  "command": "ps -p 262833 -o pid,cmd,etime",
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
  "session_id": "edd9b099-6670-4002-8cb5-5695fd3b3d77",
  "uuid": "e67e8c1b-a136-4d17-81ad-87c969b85ead",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GV7BaGnBdW87jftxi6zTxY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 464,
      "cache_read_input_tokens": 23553,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 464
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

_source line 9_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_011jogtjuNacSiYrzhvPTQLB`</summary>

```json
{
  "server": "autodl-5090",
  "command": "nvidia-smi",
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
  "session_id": "edd9b099-6670-4002-8cb5-5695fd3b3d77",
  "uuid": "ad7cef24-f5d1-4070-bb93-d776d509350b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GV7BaGnBdW87jftxi6zTxY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 464,
      "cache_read_input_tokens": 23553,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 464
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

_source line 10 · 2026-05-16T11:56:19.208Z_

<details><summary>↩ Tool result · `toolu_0187UQAaqu1QNqWaYidm6jyn`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"   PID CMD                             ELAPSED\\n262833 /root/miniconda3/bin/python    01:37:59\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.93}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "edd9b099-6670-4002-8cb5-5695fd3b3d77",
  "uuid": "c72ec8a9-39df-412c-a9e3-b804d7b37d02",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"   PID CMD                             ELAPSED\\\\n262833 /root/miniconda3/bin/python    01:37:59\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.93}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"   PID CMD                             ELAPSED\\n262833 /root/miniconda3/bin/python    01:37:59\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.93}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_0155ttvyw57A42DJxCFUGEkV`</summary>

```json
{
  "server": "autodl-5090",
  "command": "tail -100 /root/runs/tax_error_inject_agent/llama31-taxei-s0.log",
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
  "session_id": "edd9b099-6670-4002-8cb5-5695fd3b3d77",
  "uuid": "53ffce30-ff4b-4b78-a59c-ef16c2f340f4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GV7BaGnBdW87jftxi6zTxY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 464,
      "cache_read_input_tokens": 23553,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 464
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

_source line 12 · 2026-05-16T11:56:19.821Z_

<details><summary>↩ Tool result · `toolu_011jogtjuNacSiYrzhvPTQLB`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"Sat May 16 19:56:19 2026       \\n+-----------------------------------------------------------------------------------------+\\n| NVIDIA-SMI 580.76.05              Driver Version: 580.76.05      CUDA Version: 13.0     |\\n+-----------------------------------------+------------------------+----------------------+\\n| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |\\n| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |\\n|                                         |                        |               MIG M. |\\n|=========================================+========================+======================|\\n|   0  NVIDIA GeForce RTX 5090        On  |   00000000:63:00.0 Off |                  N/A |\\n| 50%   61C    P1            392W /  575W |   16837MiB /  32607MiB |     89%      Default |\\n|                                         |                        |                  N/A |\\n+-----------------------------------------+------------------------+----------------------+\\n|   1  NVIDIA GeForce RTX 5090        On  |   00000000:99:00.0 Off |                  N/A |\\n| 74%   77C    P1            572W /  575W |   26025MiB /  32607MiB |     99%      Default |\\n|                                         |                        |                  N/A |\\n+-----------------------------------------+------------------------+----------------------+\\n|   2  NVIDIA GeForce RTX 5090        On  |   00000000:BD:00.0 Off |                  N/A |\\n| 49%   60C    P1            378W /  575W |   16837MiB /  32607MiB |     88%      Default |\\n|                                         |                        |                  N/A |\\n+-----------------------------------------+------------------------+----------------------+\\n|   3  NVIDIA GeForce RTX 5090        On  |   00000000:CF:00.0 Off |                  N/A |\\n| 40%   28C    P8             20W /  575W |       0MiB /  32607MiB |      0%      Default |\\n|                                         |                        |                  N/A |\\n+-----------------------------------------+------------------------+----------------------+\\n\\n+-----------------------------------------------------------------------------------------+\\n| Processes:                                                                              |\\n|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |\\n|        ID   ID                                                               Usage      |\\n|=========================================================================================|\\n|    0   N/A  N/A          273425      C   python3                               16828MiB |\\n|    1   N/A  N/A          262833      C   /root/miniconda3/bin/python           26016MiB |\\n|    2   N/A  N/A          272997      C   python3                               16828MiB |\\n+-----------------------------------------------------------------------------------------+\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "edd9b099-6670-4002-8cb5-5695fd3b3d77",
  "uuid": "e5092d2d-218c-42e6-b707-0f6941d837a9",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"Sat May 16 19:56:19 2026       \\\\n+-----------------------------------------------------------------------------------------+\\\\n| NVIDIA-SMI 580.76.05              Driver Version: 580.76.05      CUDA Version: 13.0     |\\\\n+-----------------------------------------+------------------------+----------------------+\\\\n| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |\\\\n| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |\\\\n|                                         |                        |               MIG M. |\\\\n|=========================================+========================+======================|\\\\n|   0  NVIDIA GeForce RTX 5090        On  |   00000000:63:00.0 Off |                  N/A |\\\\n| 50%   61C    P1            392W /  575W |   16837MiB /  32607MiB |     89%      Default |\\\\n|                                         |                        |                  N/A |\\\\n+-----------------------------------------+------------------------+----------------------+\\\\n|   1  NVIDIA GeForce RTX 5090        On  |   00000000:99:00.0 Off |                  N/A |\\\\n| 74%   77C    P1            572W /  575W |   26025MiB /  32607MiB |     99%      Default |\\\\n|                                         |                        |                  N/A |\\\\n+-----------------------------------------+------------------------+----------------------+\\\\n|   2  NVIDIA GeForce RTX 5090        On  |   00000000:BD:00.0 Off |                  N/A |\\\\n| 49%   60C    P1            378W /  575W |   16837MiB /  32607MiB |     88%      Default |\\\\n|                                         |                        |                  N/A |\\\\n+-----------------------------------------+------------------------+----------------------+\\\\n|   3  NVIDIA GeForce RTX 5090        On  |   00000000:CF:00.0 Off |                  N/A |\\\\n| 40%   28C    P8             20W /  575W |       0MiB /  32607MiB |      0%      Default |\\\\n|                                         |                        |                  N/A |\\\\n+-----------------------------------------+------------------------+----------------------+\\\\n\\\\n+-----------------------------------------------------------------------------------------+\\\\n| Processes:                                                                              |\\\\n|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |\\\\n|        ID   ID                                                               Usage      |\\\\n|=========================================================================================|\\\\n|    0   N/A  N/A          273425      C   python3                               16828MiB |\\\\n|    1   N/A  N/A          262833      C   /root/miniconda3/bin/python           26016MiB |\\\\n|    2   N/A  N/A          272997      C   python3                               16828MiB |\\\\n+-----------------------------------------------------------------------------------------+\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.6}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"Sat May 16 19:56:19 2026       \\n+-----------------------------------------------------------------------------------------+\\n| NVIDIA-SMI 580.76.05              Driver Version: 580.76.05      CUDA Version: 13.0     |\\n+-----------------------------------------+------------------------+----------------------+\\n| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |\\n| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |\\n|                                         |                        |               MIG M. |\\n|=========================================+========================+======================|\\n|   0  NVIDIA GeForce RTX 5090        On  |   00000000:63:00.0 Off |                  N/A |\\n| 50%   61C    P1            392W /  575W |   16837MiB /  32607MiB |     89%      Default |\\n|                                         |                        |                  N/A |\\n+-----------------------------------------+------------------------+----------------------+\\n|   1  NVIDIA GeForce RTX 5090        On  |   00000000:99:00.0 Off |                  N/A |\\n| 74%   77C    P1            572W /  575W |   26025MiB /  32607MiB |     99%      Default |\\n|                                         |                        |                  N/A |\\n+-----------------------------------------+------------------------+----------------------+\\n|   2  NVIDIA GeForce RTX 5090        On  |   00000000:BD:00.0 Off |                  N/A |\\n| 49%   60C    P1            378W /  575W |   16837MiB /  32607MiB |     88%      Default |\\n|                                         |                        |                  N/A |\\n+-----------------------------------------+------------------------+----------------------+\\n|   3  NVIDIA GeForce RTX 5090        On  |   00000000:CF:00.0 Off |                  N/A |\\n| 40%   28C    P8             20W /  575W |       0MiB /  32607MiB |      0%      Default |\\n|                                         |                        |                  N/A |\\n+-----------------------------------------+------------------------+----------------------+\\n\\n+-----------------------------------------------------------------------------------------+\\n| Processes:                                                                              |\\n|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |\\n|        ID   ID                                                               Usage      |\\n|=========================================================================================|\\n|    0   N/A  N/A          273425      C   python3                               16828MiB |\\n|    1   N/A  N/A          262833      C   /root/miniconda3/bin/python           26016MiB |\\n|    2   N/A  N/A          272997      C   python3                               16828MiB |\\n+-----------------------------------------------------------------------------------------+\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01JDj2YnpNrpsjctgARFRFFE`</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls -la /root/autodl-tmp/tax_error_inject_agent/output/llama31-taxei-s0/",
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
  "session_id": "edd9b099-6670-4002-8cb5-5695fd3b3d77",
  "uuid": "d9dfc808-f8dc-4321-8023-fb5c0484d10c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GV7BaGnBdW87jftxi6zTxY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 464,
      "cache_read_input_tokens": 23553,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 464
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

_source line 14 · 2026-05-16T11:56:20.351Z_

<details><summary>↩ Tool result · `toolu_0155ttvyw57A42DJxCFUGEkV`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{'loss': 0.32671826, 'grad_norm': 1.33194935, 'learning_rate': 6.871e-05, 'token_acc': 0.8878992, 'epoch': 1.13, 'global_step/max_steps': '1280/3387', 'elapsed_time': '48m 58s', 'remaining_time': '1h 20m 36s', 'memory(GiB)': 30.73, 'train_speed(s/it)': 2.295037}\\n{'loss': 0.33938622, 'grad_norm': 1.32389259, 'learning_rate': 6.828e-05, 'token_acc': 0.88119441, 'epoch': 1.14, 'global_step/max_steps': '1290/3387', 'elapsed_time': '49m 20s', 'remaining_time': '1h 20m 13s', 'memory(GiB)': 30.73, 'train_speed(s/it)': 2.294957}\\n{'loss': 0.33172431, 'grad_norm': 1.02747691, 'learning_rate': 6.785e-05, 'token_acc': 0.88200525, 'epoch': 1.15, 'global_step/max_steps': '1300/3387', 'elapsed_time': '49m 43s', 'remaining_time': '1h 19m 49s', 'memory(GiB)': 30.73, 'train_speed(s/it)': 2.294641}\\n{'loss': 0.3379811, 'grad_norm': 1.83775723, 'learning_rate': 6.741e-05, 'token_acc': 0.87697297, 'epoch': 1.16, 'global_step/max_steps': '1310/3387', 'elapsed_time': '50m 7s', 'remaining_time': '1h 19m 28s', 'memory(GiB)': 30.73, 'train_speed(s/it)': 2.295615}\\n{'loss': 0.34189026, 'grad_norm': 1.34283733, 'learning_rate': 6.698e-05, 'token_acc': 0.87941302, 'epoch': 1.17, 'global_step/max_steps': '1320/3387', 'elapsed_time': '50m 31s', 'remaining_time': '1h 19m 7s', 'memory(GiB)': 30.73, 'train_speed(s/it)': 2.296541}\\n{'loss': 0.33172233, 'grad_norm': 1.34344244, 'learning_rate': 6.654e-05, 'token_acc': 0.88366788, 'epoch': 1.18, 'global_step/max_steps': '1330/3387', 'elapsed_time': '50m 55s', 'remaining_time': '1h 18m 45s', 'memory(GiB)': 30.73, 'train_speed(s/it)': 2.296867}\\n{'loss': 0.3149039, 'grad_norm': 1.75784481, 'learning_rate': 6.61e-05, 'token_acc': 0.88792188, 'epoch': 1.19, 'global_step/max_steps': '1340/3387', 'elapsed_time': '51m 20s', 'remaining_time': '1h 18m 25s', 'memory(GiB)': 30.73, 'train_speed(s/it)': 2.298311}\\n{'loss': 0.34533262, 'grad_norm': 1.22510314, 'learning_rate': 6.566e-05, 'token_acc': 0.87955895, 'epoch': 1.2, 'global_step/max_steps': '1350/3387', 'elapsed_time': '51m 42s', 'remaining_time': '1h 18m 1s', 'memory(GiB)': 30.73, 'train_speed(s/it)': 2.298141}\\n{'loss': 0.32055404, 'grad_norm': 1.53403378, 'learning_rate': 6.522e-05, 'token_acc': 0.88610216, 'epoch': 1.2, 'global_step/max_steps': '1360/3387', 'elapsed_time': '52m 6s', 'remaining_time': '1h 17m 39s', 'memory(GiB)': 30.73, 'train_speed(s/it)': 2.298424}\\n{'loss': 0.30133731, 'grad_norm': 1.69244277, 'learning_rate': 6.478e-05, 'token_acc': 0.89525449, 'epoch': 1.21, 'global_step/max_steps': '1370/3387', 'elapsed_time': '52m 30s', 'remaining_time': '1h 17m 17s', 'memory(GiB)': 30.73, 'train_speed(s/it)': 2.299025}\\n{'loss': 0.28116689, 'grad_norm': 1.5254389, 'learning_rate': 6.434e-05, 'token_acc': 0.89863198, 'epoch': 1.22, 'global_step/max_steps': '1380/3387', 'elapsed_time': '52m 51s', 'remaining_time': '1h 16m 51s', 'memory(GiB)': 30.73, 'train_speed(s/it)': 2.297565}\\n{'loss': 0.28150647, 'grad_norm': 1.25031102, 'learning_rate': 6.389e-05, 'token_acc': 0.89631495, 'epoch': 1.23, 'global_step/max_steps': '1390/3387', 'elapsed_time': '53m 13s', 'remaining_time': '1h 16m 28s', 'memory(GiB)': 30.73, 'train_speed(s/it)': 2.297374}\\n{'loss': 0.32835832, 'grad_norm': 1.41603386, 'learning_rate': 6.344e-05, 'token_acc': 0.88240515, 'epoch': 1.24, 'global_step/max_steps': '1400/3387', 'elapsed_time': '53m 37s', 'remaining_time': '1h 16m 5s', 'memory(GiB)': 30.73, 'train_speed(s/it)': 2.297556}\\n{'loss': 0.31286595, 'grad_norm': 1.37249088, 'learning_rate': 6.3e-05, 'token_acc': 0.88487866, 'epoch': 1.25, 'global_step/max_steps': '1410/3387', 'elapsed_time': '53m 59s', 'remaining_time': '1h 15m 42s', 'memory(GiB)': 30.73, 'train_speed(s/it)': 2.297322}\\n{'loss': 0.31002481, 'grad_norm': 1.48736668, 'learning_rate': 6.255e-05, 'token_acc': 0.88701443, 'epoch': 1.26, 'global_step/max_steps': '1420/3387', 'elapsed_time': '54m 22s', 'remaining_time': '1h 15m 19s', 'memory(GiB)': 30.73, 'train_speed(s/it)': 2.297261}\\n{'loss': 0.32317185, 'grad_norm': 1.56090486, 'learnin\\n\\n... [截断: 输出过长，省略 106624 字符] ...\\n\\n87 [1:35:40<33:06,  2.23s/it]\\rTrain:  74%|███████▍  | 2499/3387 [1:35:42<34:54,  2.36s/it]\\rTrain:  74%|███████▍  | 2500/3387 [1:35:45<35:43,  2.42s/it]\\r                                                            \\r\\rTrain:  74%|███████▍  | 2500/3387 [1:35:45<35:43,  2.42s/it]\\rTrain:  74%|███████▍  | 2500/3387 [1:35:45<35:43,  2.42s/it]\\rTrain:  74%|███████▍  | 2501/3387 [1:35:47<33:24,  2.26s/it]\\rTrain:  74%|███████▍  | 2502/3387 [1:35:49<33:35,  2.28s/it]\\rTrain:  74%|███████▍  | 2503/3387 [1:35:51<33:30,  2.27s/it]\\rTrain:  74%|███████▍  | 2504/3387 [1:35:54<34:55,  2.37s/it]\\rTrain:  74%|███████▍  | 2505/3387 [1:35:56<35:16,  2.40s/it]\\rTrain:  74%|███████▍  | 2506/3387 [1:35:59<35:49,  2.44s/it]\\rTrain:  74%|███████▍  | 2507/3387 [1:36:01<34:25,  2.35s/it]\\rTrain:  74%|███████▍  | 2508/3387 [1:36:03<33:26,  2.28s/it]\\rTrain:  74%|███████▍  | 2509/3387 [1:36:05<30:36,  2.09s/it]\\rTrain:  74%|███████▍  | 2510/3387 [1:36:08<35:33,  2.43s/it]\\r                                                            \\r\\rTrain:  74%|███████▍  | 2510/3387 [1:36:08<35:33,  2.43s/it]\\rTrain:  74%|███████▍  | 2510/3387 [1:36:08<35:33,  2.43s/it]\\rTrain:  74%|███████▍  | 2511/3387 [1:36:11<35:46,  2.45s/it]\\rTrain:  74%|███████▍  | 2512/3387 [1:36:13<34:45,  2.38s/it]\\rTrain:  74%|███████▍  | 2513/3387 [1:36:15<32:52,  2.26s/it]\\rTrain:  74%|███████▍  | 2514/3387 [1:36:16<30:21,  2.09s/it]\\rTrain:  74%|███████▍  | 2515/3387 [1:36:19<31:13,  2.15s/it]\\rTrain:  74%|███████▍  | 2516/3387 [1:36:21<31:57,  2.20s/it]\\rTrain:  74%|███████▍  | 2517/3387 [1:36:23<31:45,  2.19s/it]\\rTrain:  74%|████��██▍  | 2518/3387 [1:36:26<32:57,  2.28s/it]\\rTrain:  74%|███████▍  | 2519/3387 [1:36:29<35:19,  2.44s/it]\\rTrain:  74%|███████▍  | 2520/3387 [1:36:31<35:11,  2.44s/it]\\r                                                            \\r\\rTrain:  74%|███████▍  | 2520/3387 [1:36:31<35:11,  2.44s/it]\\rTrain:  74%|███████▍  | 2520/3387 [1:36:31<35:11,  2.44s/it]\\rTrain:  74%|███████▍  | 2521/3387 [1:36:33<34:55,  2.42s/it]\\rTrain:  74%|███████▍  | 2522/3387 [1:36:37<38:03,  2.64s/it]\\rTrain:  74%|███████▍  | 2523/3387 [1:36:39<36:34,  2.54s/it]\\rTrain:  75%|███████▍  | 2524/3387 [1:36:41<34:38,  2.41s/it]\\rTrain:  75%|███████▍  | 2525/3387 [1:36:43<34:54,  2.43s/it]\\rTrain:  75%|███████▍  | 2526/3387 [1:36:46<34:55,  2.43s/it]\\rTrain:  75%|███████▍  | 2527/3387 [1:36:49<36:39,  2.56s/it]\\rTrain:  75%|███████▍  | 2528/3387 [1:36:51<36:37,  2.56s/it]\\rTrain:  75%|███████▍  | 2529/3387 [1:36:53<32:26,  2.27s/it]\\rTrain:  75%|███████▍  | 2530/3387 [1:36:56<34:19,  2.40s/it]\\r                                                            \\r\\rTrain:  75%|███████▍  | 2530/3387 [1:36:56<34:19,  2.40s/it]\\rTrain:  75%|███████▍  | 2530/3387 [1:36:56<34:19,  2.40s/it]\\rTrain:  75%|███████▍  | 2531/3387 [1:36:58<33:19,  2.34s/it]\\rTrain:  75%|███████▍  | 2532/3387 [1:37:00<32:13,  2.26s/it]\\rTrain:  75%|███████▍  | 2533/3387 [1:37:02<32:06,  2.26s/it]\\rTrain:  75%|███████▍  | 2534/3387 [1:37:05<32:51,  2.31s/it]\\rTrain:  75%|███████▍  | 2535/3387 [1:37:08<36:54,  2.60s/it]\\rTrain:  75%|███████▍  | 2536/3387 [1:37:11<38:39,  2.73s/it]\\rTrain:  75%|███████▍  | 2537/3387 [1:37:13<35:40,  2.52s/it]\\rTrain:  75%|███████▍  | 2538/3387 [1:37:14<31:44,  2.24s/it]\\rTrain:  75%|███████▍  | 2539/3387 [1:37:16<30:47,  2.18s/it]\\rTrain:  75%|███████▍  | 2540/3387 [1:37:19<32:43,  2.32s/it]\\r                                                            \\r\\rTrain:  75%|███████▍  | 2540/3387 [1:37:19<32:43,  2.32s/it]\\rTrain:  75%|███████▍  | 2540/3387 [1:37:19<32:43,  2.32s/it]\\rTrain:  75%|███████▌  | 2541/3387 [1:37:21<30:05,  2.13s/it]\\rTrain:  75%|███████▌  | 2542/3387 [1:37:23<30:59,  2.20s/it]\\rTrain:  75%|███████▌  | 2543/3387 [1:37:25<31:14,  2.22s/it]\\rTrain:  75%|███████▌  | 2544/3387 [1:37:28<30:30,  2.17s/it]\\rTrain:  75%|███████▌  | 2545/3387 [1:37:30<32:45,  2.33s/it]\\rTrain:  75%|███████▌  | 2546/3387 [1:37:32<31:34,  2.25s/it]\\rTrain:  75%|███████▌  | 2547/3387 [1:37:35<32:27,  2.32s/it]\\rTrain:  75%|███████▌  | 2548/3387 [1:37:37<31:26,  2.25s/it]\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "edd9b099-6670-4002-8cb5-5695fd3b3d77",
  "uuid": "297dc240-4bc1-4c51-a36f-87e4b761b631",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{'loss': 0.32671826, 'grad_norm': 1.33194935, 'learning_rate': 6.871e-05, 'token_acc': 0.8878992, 'epoch': 1.13, 'global_step/max_steps': '1280/3387', 'elapsed_time': '48m 58s', 'remaining_time': '1h 20m 36s', 'memory(GiB)': 30.73, 'train_speed(s/it)': 2.295037}\\\\n{'loss': 0.33938622, 'grad_norm': 1.32389259, 'learning_rate': 6.828e-05, 'token_acc': 0.88119441, 'epoch': 1.14, 'global_step/max_steps': '1290/3387', 'elapsed_time': '49m 20s', 'remaining_time': '1h 20m 13s', 'memory(GiB)': 30.73, 'train_speed(s/it)': 2.294957}\\\\n{'loss': 0.33172431, 'grad_norm': 1.02747691, 'learning_rate': 6.785e-05, 'token_acc': 0.88200525, 'epoch': 1.15, 'global_step/max_steps': '1300/3387', 'elapsed_time': '49m 43s', 'remaining_time': '1h 19m 49s', 'memory(GiB)': 30.73, 'train_speed(s/it)': 2.294641}\\\\n{'loss': 0.3379811, 'grad_norm': 1.83775723, 'learning_rate': 6.741e-05, 'token_acc': 0.87697297, 'epoch': 1.16, 'global_step/max_steps': '1310/3387', 'elapsed_time': '50m 7s', 'remaining_time': '1h 19m 28s', 'memory(GiB)': 30.73, 'train_speed(s/it)': 2.295615}\\\\n{'loss': 0.34189026, 'grad_norm': 1.34283733, 'learning_rate': 6.698e-05, 'token_acc': 0.87941302, 'epoch': 1.17, 'global_step/max_steps': '1320/3387', 'elapsed_time': '50m 31s', 'remaining_time': '1h 19m 7s', 'memory(GiB)': 30.73, 'train_speed(s/it)': 2.296541}\\\\n{'loss': 0.33172233, 'grad_norm': 1.34344244, 'learning_rate': 6.654e-05, 'token_acc': 0.88366788, 'epoch': 1.18, 'global_step/max_steps': '1330/3387', 'elapsed_time': '50m 55s', 'remaining_time': '1h 18m 45s', 'memory(GiB)': 30.73, 'train_speed(s/it)': 2.296867}\\\\n{'loss': 0.3149039, 'grad_norm': 1.75784481, 'learning_rate': 6.61e-05, 'token_acc': 0.88792188, 'epoch': 1.19, 'global_step/max_steps': '1340/3387', 'elapsed_time': '51m 20s', 'remaining_time': '1h 18m 25s', 'memory(GiB)': 30.73, 'train_speed(s/it)': 2.298311}\\\\n{'loss': 0.34533262, 'grad_norm': 1.22510314, 'learning_rate': 6.566e-05, 'token_acc': 0.87955895, 'epoch': 1.2, 'global_step/max_steps': '1350/3387', 'elapsed_time': '51m 42s', 'remaining_time': '1h 18m 1s', 'memory(GiB)': 30.73, 'train_speed(s/it)': 2.298141}\\\\n{'loss': 0.32055404, 'grad_norm': 1.53403378, 'learning_rate': 6.522e-05, 'token_acc': 0.88610216, 'epoch': 1.2, 'global_step/max_steps': '1360/3387', 'elapsed_time': '52m 6s', 'remaining_time': '1h 17m 39s', 'memory(GiB)': 30.73, 'train_speed(s/it)': 2.298424}\\\\n{'loss': 0.30133731, 'grad_norm': 1.69244277, 'learning_rate': 6.478e-05, 'token_acc': 0.89525449, 'epoch': 1.21, 'global_step/max_steps': '1370/3387', 'elapsed_time': '52m 30s', 'remaining_time': '1h 17m 17s', 'memory(GiB)': 30.73, 'train_speed(s/it)': 2.299025}\\\\n{'loss': 0.28116689, 'grad_norm': 1.5254389, 'learning_rate': 6.434e-05, 'token_acc': 0.89863198, 'epoch': 1.22, 'global_step/max_steps': '1380/3387', 'elapsed_time': '52m 51s', 'remaining_time': '1h 16m 51s', 'memory(GiB)': 30.73, 'train_speed(s/it)': 2.297565}\\\\n{'loss': 0.28150647, 'grad_norm': 1.25031102, 'learning_rate': 6.389e-05, 'token_acc': 0.89631495, 'epoch': 1.23, 'global_step/max_steps': '1390/3387', 'elapsed_time': '53m 13s', 'remaining_time': '1h 16m 28s', 'memory(GiB)': 30.73, 'train_speed(s/it)': 2.297374}\\\\n{'loss': 0.32835832, 'grad_norm': 1.41603386, 'learning_rate': 6.344e-05, 'token_acc': 0.88240515, 'epoch': 1.24, 'global_step/max_steps': '1400/3387', 'elapsed_time': '53m 37s', 'remaining_time': '1h 16m 5s', 'memory(GiB)': 30.73, 'train_speed(s/it)': 2.297556}\\\\n{'loss': 0.31286595, 'grad_norm': 1.37249088, 'learning_rate': 6.3e-05, 'token_acc': 0.88487866, 'epoch': 1.25, 'global_step/max_steps': '1410/3387', 'elapsed_time': '53m 59s', 'remaining_time': '1h 15m 42s', 'memory(GiB)': 30.73, 'train_speed(s/it)': 2.297322}\\\\n{'loss': 0.31002481, 'grad_norm': 1.48736668, 'learning_rate': 6.255e-05, 'token_acc': 0.88701443, 'epoch': 1.26, 'global_step/max_steps': '1420/3387', 'elapsed_time': '54m 22s', 'remaining_time': '1h 15m 19s', 'memory(GiB)': 30.73, 'train_speed(s/it)': 2.297261}\\\\n{'loss': 0.32317185, 'grad_norm': 1.56090486, 'learnin\\\\n\\\\n... [截断: 输出过长，省略 106624 字符] ...\\\\n\\\\n87 [1:35:40<33:06,  2.23s/it]\\\\rTrain:  74%|███████▍  | 2499/3387 [1:35:42<34:54,  2.36s/it]\\\\rTrain:  74%|███████▍  | 2500/3387 [1:35:45<35:43,  2.42s/it]\\\\r                                                            \\\\r\\\\rTrain:  74%|███████▍  | 2500/3387 [1:35:45<35:43,  2.42s/it]\\\\rTrain:  74%|███████▍  | 2500/3387 [1:35:45<35:43,  2.42s/it]\\\\rTrain:  74%|███████▍  | 2501/3387 [1:35:47<33:24,  2.26s/it]\\\\rTrain:  74%|███████▍  | 2502/3387 [1:35:49<33:35,  2.28s/it]\\\\rTrain:  74%|███████▍  | 2503/3387 [1:35:51<33:30,  2.27s/it]\\\\rTrain:  74%|███████▍  | 2504/3387 [1:35:54<34:55,  2.37s/it]\\\\rTrain:  74%|███████▍  | 2505/3387 [1:35:56<35:16,  2.40s/it]\\\\rTrain:  74%|███████▍  | 2506/3387 [1:35:59<35:49,  2.44s/it]\\\\rTrain:  74%|███████▍  | 2507/3387 [1:36:01<34:25,  2.35s/it]\\\\rTrain:  74%|███████▍  | 2508/3387 [1:36:03<33:26,  2.28s/it]\\\\rTrain:  74%|███████▍  | 2509/3387 [1:36:05<30:36,  2.09s/it]\\\\rTrain:  74%|███████▍  | 2510/3387 [1:36:08<35:33,  2.43s/it]\\\\r                                                            \\\\r\\\\rTrain:  74%|███████▍  | 2510/3387 [1:36:08<35:33,  2.43s/it]\\\\rTrain:  74%|███████▍  | 2510/3387 [1:36:08<35:33,  2.43s/it]\\\\rTrain:  74%|███████▍  | 2511/3387 [1:36:11<35:46,  2.45s/it]\\\\rTrain:  74%|███████▍  | 2512/3387 [1:36:13<34:45,  2.38s/it]\\\\rTrain:  74%|███████▍  | 2513/3387 [1:36:15<32:52,  2.26s/it]\\\\rTrain:  74%|███████▍  | 2514/3387 [1:36:16<30:21,  2.09s/it]\\\\rTrain:  74%|███████▍  | 2515/3387 [1:36:19<31:13,  2.15s/it]\\\\rTrain:  74%|███████▍  | 2516/3387 [1:36:21<31:57,  2.20s/it]\\\\rTrain:  74%|███████▍  | 2517/3387 [1:36:23<31:45,  2.19s/it]\\\\rTrain:  74%|████��██▍  | 2518/3387 [1:36:26<32:57,  2.28s/it]\\\\rTrain:  74%|███████▍  | 2519/3387 [1:36:29<35:19,  2.44s/it]\\\\rTrain:  74%|███████▍  | 2520/3387 [1:36:31<35:11,  2.44s/it]\\\\r                                                            \\\\r\\\\rTrain:  74%|███████▍  | 2520/3387 [1:36:31<35:11,  2.44s/it]\\\\rTrain:  74%|███████▍  | 2520/3387 [1:36:31<35:11,  2.44s/it]\\\\rTrain:  74%|███████▍  | 2521/3387 [1:36:33<34:55,  2.42s/it]\\\\rTrain:  74%|███████▍  | 2522/3387 [1:36:37<38:03,  2.64s/it]\\\\rTrain:  74%|███████▍  | 2523/3387 [1:36:39<36:34,  2.54s/it]\\\\rTrain:  75%|███████▍  | 2524/3387 [1:36:41<34:38,  2.41s/it]\\\\rTrain:  75%|███████▍  | 2525/3387 [1:36:43<34:54,  2.43s/it]\\\\rTrain:  75%|███████▍  | 2526/3387 [1:36:46<34:55,  2.43s/it]\\\\rTrain:  75%|███████▍  | 2527/3387 [1:36:49<36:39,  2.56s/it]\\\\rTrain:  75%|███████▍  | 2528/3387 [1:36:51<36:37,  2.56s/it]\\\\rTrain:  75%|███████▍  | 2529/3387 [1:36:53<32:26,  2.27s/it]\\\\rTrain:  75%|███████▍  | 2530/3387 [1:36:56<34:19,  2.40s/it]\\\\r                                                            \\\\r\\\\rTrain:  75%|███████▍  | 2530/3387 [1:36:56<34:19,  2.40s/it]\\\\rTrain:  75%|███████▍  | 2530/3387 [1:36:56<34:19,  2.40s/it]\\\\rTrain:  75%|███████▍  | 2531/3387 [1:36:58<33:19,  2.34s/it]\\\\rTrain:  75%|███████▍  | 2532/3387 [1:37:00<32:13,  2.26s/it]\\\\rTrain:  75%|███████▍  | 2533/3387 [1:37:02<32:06,  2.26s/it]\\\\rTrain:  75%|███████▍  | 2534/3387 [1:37:05<32:51,  2.31s/it]\\\\rTrain:  75%|███████▍  | 2535/3387 [1:37:08<36:54,  2.60s/it]\\\\rTrain:  75%|███████▍  | 2536/3387 [1:37:11<38:39,  2.73s/it]\\\\rTrain:  75%|███████▍  | 2537/3387 [1:37:13<35:40,  2.52s/it]\\\\rTrain:  75%|███████▍  | 2538/3387 [1:37:14<31:44,  2.24s/it]\\\\rTrain:  75%|███████▍  | 2539/3387 [1:37:16<30:47,  2.18s/it]\\\\rTrain:  75%|███████▍  | 2540/3387 [1:37:19<32:43,  2.32s/it]\\\\r                                                            \\\\r\\\\rTrain:  75%|███████▍  | 2540/3387 [1:37:19<32:43,  2.32s/it]\\\\rTrain:  75%|███████▍  | 2540/3387 [1:37:19<32:43,  2.32s/it]\\\\rTrain:  75%|███████▌  | 2541/3387 [1:37:21<30:05,  2.13s/it]\\\\rTrain:  75%|███████▌  | 2542/3387 [1:37:23<30:59,  2.20s/it]\\\\rTrain:  75%|███████▌  | 2543/3387 [1:37:25<31:14,  2.22s/it]\\\\rTrain:  75%|███████▌  | 2544/3387 [1:37:28<30:30,  2.17s/it]\\\\rTrain:  75%|███████▌  | 2545/3387 [1:37:30<32:45,  2.33s/it]\\\\rTrain:  75%|███████▌  | 2546/3387 [1:37:32<31:34,  2.25s/it]\\\\rTrain:  75%|███████▌  | 2547/3387 [1:37:35<32:27,  2.32s/it]\\\\rTrain:  75%|███████▌  | 2548/3387 [1:37:37<31:26,  2.25s/it]\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.52}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{'loss': 0.32671826, 'grad_norm': 1.33194935, 'learning_rate': 6.871e-05, 'token_acc': 0.8878992, 'epoch': 1.13, 'global_step/max_steps': '1280/3387', 'elapsed_time': '48m 58s', 'remaining_time': '1h 20m 36s', 'memory(GiB)': 30.73, 'train_speed(s/it)': 2.295037}\\n{'loss': 0.33938622, 'grad_norm': 1.32389259, 'learning_rate': 6.828e-05, 'token_acc': 0.88119441, 'epoch': 1.14, 'global_step/max_steps': '1290/3387', 'elapsed_time': '49m 20s', 'remaining_time': '1h 20m 13s', 'memory(GiB)': 30.73, 'train_speed(s/it)': 2.294957}\\n{'loss': 0.33172431, 'grad_norm': 1.02747691, 'learning_rate': 6.785e-05, 'token_acc': 0.88200525, 'epoch': 1.15, 'global_step/max_steps': '1300/3387', 'elapsed_time': '49m 43s', 'remaining_time': '1h 19m 49s', 'memory(GiB)': 30.73, 'train_speed(s/it)': 2.294641}\\n{'loss': 0.3379811, 'grad_norm': 1.83775723, 'learning_rate': 6.741e-05, 'token_acc': 0.87697297, 'epoch': 1.16, 'global_step/max_steps': '1310/3387', 'elapsed_time': '50m 7s', 'remaining_time': '1h 19m 28s', 'memory(GiB)': 30.73, 'train_speed(s/it)': 2.295615}\\n{'loss': 0.34189026, 'grad_norm': 1.34283733, 'learning_rate': 6.698e-05, 'token_acc': 0.87941302, 'epoch': 1.17, 'global_step/max_steps': '1320/3387', 'elapsed_time': '50m 31s', 'remaining_time': '1h 19m 7s', 'memory(GiB)': 30.73, 'train_speed(s/it)': 2.296541}\\n{'loss': 0.33172233, 'grad_norm': 1.34344244, 'learning_rate': 6.654e-05, 'token_acc': 0.88366788, 'epoch': 1.18, 'global_step/max_steps': '1330/3387', 'elapsed_time': '50m 55s', 'remaining_time': '1h 18m 45s', 'memory(GiB)': 30.73, 'train_speed(s/it)': 2.296867}\\n{'loss': 0.3149039, 'grad_norm': 1.75784481, 'learning_rate': 6.61e-05, 'token_acc': 0.88792188, 'epoch': 1.19, 'global_step/max_steps': '1340/3387', 'elapsed_time': '51m 20s', 'remaining_time': '1h 18m 25s', 'memory(GiB)': 30.73, 'train_speed(s/it)': 2.298311}\\n{'loss': 0.34533262, 'grad_norm': 1.22510314, 'learning_rate': 6.566e-05, 'token_acc': 0.87955895, 'epoch': 1.2, 'global_step/max_steps': '1350/3387', 'elapsed_time': '51m 42s', 'remaining_time': '1h 18m 1s', 'memory(GiB)': 30.73, 'train_speed(s/it)': 2.298141}\\n{'loss': 0.32055404, 'grad_norm': 1.53403378, 'learning_rate': 6.522e-05, 'token_acc': 0.88610216, 'epoch': 1.2, 'global_step/max_steps': '1360/3387', 'elapsed_time': '52m 6s', 'remaining_time': '1h 17m 39s', 'memory(GiB)': 30.73, 'train_speed(s/it)': 2.298424}\\n{'loss': 0.30133731, 'grad_norm': 1.69244277, 'learning_rate': 6.478e-05, 'token_acc': 0.89525449, 'epoch': 1.21, 'global_step/max_steps': '1370/3387', 'elapsed_time': '52m 30s', 'remaining_time': '1h 17m 17s', 'memory(GiB)': 30.73, 'train_speed(s/it)': 2.299025}\\n{'loss': 0.28116689, 'grad_norm': 1.5254389, 'learning_rate': 6.434e-05, 'token_acc': 0.89863198, 'epoch': 1.22, 'global_step/max_steps': '1380/3387', 'elapsed_time': '52m 51s', 'remaining_time': '1h 16m 51s', 'memory(GiB)': 30.73, 'train_speed(s/it)': 2.297565}\\n{'loss': 0.28150647, 'grad_norm': 1.25031102, 'learning_rate': 6.389e-05, 'token_acc': 0.89631495, 'epoch': 1.23, 'global_step/max_steps': '1390/3387', 'elapsed_time': '53m 13s', 'remaining_time': '1h 16m 28s', 'memory(GiB)': 30.73, 'train_speed(s/it)': 2.297374}\\n{'loss': 0.32835832, 'grad_norm': 1.41603386, 'learning_rate': 6.344e-05, 'token_acc': 0.88240515, 'epoch': 1.24, 'global_step/max_steps': '1400/3387', 'elapsed_time': '53m 37s', 'remaining_time': '1h 16m 5s', 'memory(GiB)': 30.73, 'train_speed(s/it)': 2.297556}\\n{'loss': 0.31286595, 'grad_norm': 1.37249088, 'learning_rate': 6.3e-05, 'token_acc': 0.88487866, 'epoch': 1.25, 'global_step/max_steps': '1410/3387', 'elapsed_time': '53m 59s', 'remaining_time': '1h 15m 42s', 'memory(GiB)': 30.73, 'train_speed(s/it)': 2.297322}\\n{'loss': 0.31002481, 'grad_norm': 1.48736668, 'learning_rate': 6.255e-05, 'token_acc': 0.88701443, 'epoch': 1.26, 'global_step/max_steps': '1420/3387', 'elapsed_time': '54m 22s', 'remaining_time': '1h 15m 19s', 'memory(GiB)': 30.73, 'train_speed(s/it)': 2.297261}\\n{'loss': 0.32317185, 'grad_norm': 1.56090486, 'learnin\\n\\n... [截断: 输出过长，省略 106624 字符] ...\\n\\n87 [1:35:40<33:06,  2.23s/it]\\rTrain:  74%|███████▍  | 2499/3387 [1:35:42<34:54,  2.36s/it]\\rTrain:  74%|███████▍  | 2500/3387 [1:35:45<35:43,  2.42s/it]\\r                                                            \\r\\rTrain:  74%|███████▍  | 2500/3387 [1:35:45<35:43,  2.42s/it]\\rTrain:  74%|███████▍  | 2500/3387 [1:35:45<35:43,  2.42s/it]\\rTrain:  74%|███████▍  | 2501/3387 [1:35:47<33:24,  2.26s/it]\\rTrain:  74%|███████▍  | 2502/3387 [1:35:49<33:35,  2.28s/it]\\rTrain:  74%|███████▍  | 2503/3387 [1:35:51<33:30,  2.27s/it]\\rTrain:  74%|███████▍  | 2504/3387 [1:35:54<34:55,  2.37s/it]\\rTrain:  74%|███████▍  | 2505/3387 [1:35:56<35:16,  2.40s/it]\\rTrain:  74%|███████▍  | 2506/3387 [1:35:59<35:49,  2.44s/it]\\rTrain:  74%|███████▍  | 2507/3387 [1:36:01<34:25,  2.35s/it]\\rTrain:  74%|███████▍  | 2508/3387 [1:36:03<33:26,  2.28s/it]\\rTrain:  74%|███████▍  | 2509/3387 [1:36:05<30:36,  2.09s/it]\\rTrain:  74%|███████▍  | 2510/3387 [1:36:08<35:33,  2.43s/it]\\r                                                            \\r\\rTrain:  74%|███████▍  | 2510/3387 [1:36:08<35:33,  2.43s/it]\\rTrain:  74%|███████▍  | 2510/3387 [1:36:08<35:33,  2.43s/it]\\rTrain:  74%|███████▍  | 2511/3387 [1:36:11<35:46,  2.45s/it]\\rTrain:  74%|███████▍  | 2512/3387 [1:36:13<34:45,  2.38s/it]\\rTrain:  74%|███████▍  | 2513/3387 [1:36:15<32:52,  2.26s/it]\\rTrain:  74%|███████▍  | 2514/3387 [1:36:16<30:21,  2.09s/it]\\rTrain:  74%|███████▍  | 2515/3387 [1:36:19<31:13,  2.15s/it]\\rTrain:  74%|███████▍  | 2516/3387 [1:36:21<31:57,  2.20s/it]\\rTrain:  74%|███████▍  | 2517/3387 [1:36:23<31:45,  2.19s/it]\\rTrain:  74%|████��██▍  | 2518/3387 [1:36:26<32:57,  2.28s/it]\\rTrain:  74%|███████▍  | 2519/3387 [1:36:29<35:19,  2.44s/it]\\rTrain:  74%|███████▍  | 2520/3387 [1:36:31<35:11,  2.44s/it]\\r                                                            \\r\\rTrain:  74%|███████▍  | 2520/3387 [1:36:31<35:11,  2.44s/it]\\rTrain:  74%|███████▍  | 2520/3387 [1:36:31<35:11,  2.44s/it]\\rTrain:  74%|███████▍  | 2521/3387 [1:36:33<34:55,  2.42s/it]\\rTrain:  74%|███████▍  | 2522/3387 [1:36:37<38:03,  2.64s/it]\\rTrain:  74%|███████▍  | 2523/3387 [1:36:39<36:34,  2.54s/it]\\rTrain:  75%|███████▍  | 2524/3387 [1:36:41<34:38,  2.41s/it]\\rTrain:  75%|███████▍  | 2525/3387 [1:36:43<34:54,  2.43s/it]\\rTrain:  75%|███████▍  | 2526/3387 [1:36:46<34:55,  2.43s/it]\\rTrain:  75%|███████▍  | 2527/3387 [1:36:49<36:39,  2.56s/it]\\rTrain:  75%|███████▍  | 2528/3387 [1:36:51<36:37,  2.56s/it]\\rTrain:  75%|███████▍  | 2529/3387 [1:36:53<32:26,  2.27s/it]\\rTrain:  75%|███████▍  | 2530/3387 [1:36:56<34:19,  2.40s/it]\\r                                                            \\r\\rTrain:  75%|███████▍  | 2530/3387 [1:36:56<34:19,  2.40s/it]\\rTrain:  75%|███████▍  | 2530/3387 [1:36:56<34:19,  2.40s/it]\\rTrain:  75%|███████▍  | 2531/3387 [1:36:58<33:19,  2.34s/it]\\rTrain:  75%|███████▍  | 2532/3387 [1:37:00<32:13,  2.26s/it]\\rTrain:  75%|███████▍  | 2533/3387 [1:37:02<32:06,  2.26s/it]\\rTrain:  75%|███████▍  | 2534/3387 [1:37:05<32:51,  2.31s/it]\\rTrain:  75%|███████▍  | 2535/3387 [1:37:08<36:54,  2.60s/it]\\rTrain:  75%|███████▍  | 2536/3387 [1:37:11<38:39,  2.73s/it]\\rTrain:  75%|███████▍  | 2537/3387 [1:37:13<35:40,  2.52s/it]\\rTrain:  75%|███████▍  | 2538/3387 [1:37:14<31:44,  2.24s/it]\\rTrain:  75%|███████▍  | 2539/3387 [1:37:16<30:47,  2.18s/it]\\rTrain:  75%|███████▍  | 2540/3387 [1:37:19<32:43,  2.32s/it]\\r                                                            \\r\\rTrain:  75%|███████▍  | 2540/3387 [1:37:19<32:43,  2.32s/it]\\rTrain:  75%|███████▍  | 2540/3387 [1:37:19<32:43,  2.32s/it]\\rTrain:  75%|███████▌  | 2541/3387 [1:37:21<30:05,  2.13s/it]\\rTrain:  75%|███████▌  | 2542/3387 [1:37:23<30:59,  2.20s/it]\\rTrain:  75%|███████▌  | 2543/3387 [1:37:25<31:14,  2.22s/it]\\rTrain:  75%|███████▌  | 2544/3387 [1:37:28<30:30,  2.17s/it]\\rTrain:  75%|███████▌  | 2545/3387 [1:37:30<32:45,  2.33s/it]\\rTrain:  75%|███████▌  | 2546/3387 [1:37:32<31:34,  2.25s/it]\\rTrain:  75%|███████▌  | 2547/3387 [1:37:35<32:27,  2.32s/it]\\rTrain:  75%|███████▌  | 2548/3387 [1:37:37<31:26,  2.25s/it]\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-16T11:56:20.740Z_

<details><summary>↩ Tool result · `toolu_01JDj2YnpNrpsjctgARFRFFE`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 4\\ndrwxr-xr-x  4 root root   70 May 16 18:18 .\\ndrwxr-xr-x 16 root root 4096 May 16 17:16 ..\\ndrwxr-xr-x  4 root root   99 May 16 17:59 v0-20260516-171606\\ndrwxr-xr-x  5 root root  126 May 16 19:45 v1-20260516-181826\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "edd9b099-6670-4002-8cb5-5695fd3b3d77",
  "uuid": "47744c0b-d1c4-46fc-979b-ecd4b08b8101",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"total 4\\\\ndrwxr-xr-x  4 root root   70 May 16 18:18 .\\\\ndrwxr-xr-x 16 root root 4096 May 16 17:16 ..\\\\ndrwxr-xr-x  4 root root   99 May 16 17:59 v0-20260516-171606\\\\ndrwxr-xr-x  5 root root  126 May 16 19:45 v1-20260516-181826\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.38}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"total 4\\ndrwxr-xr-x  4 root root   70 May 16 18:18 .\\ndrwxr-xr-x 16 root root 4096 May 16 17:16 ..\\ndrwxr-xr-x  4 root root   99 May 16 17:59 v0-20260516-171606\\ndrwxr-xr-x  5 root root  126 May 16 19:45 v1-20260516-181826\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 16_

结论：**RUNNING** — 训练正常进行中，registry 的 failed 标记是误报。

现状：
- PID 262833 存活，运行时间 1h37m59s，进程为 `/root/miniconda3/bin/python`
- GPU cuda:1 占用 26GB 显存，利用率 99%
- 进度：**step 2548/3387 (75%)**, epoch ~2.25, elapsed 1h37m
- 最近 loss ~0.32, token_acc ~0.88
- 已产出 2 个 checkpoint：`v0-20260516-171606`, `v1-20260516-181826`
- 预计剩余 ~32 分钟完成

需要更新 registry 清除错误的 failed 标记。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "edd9b099-6670-4002-8cb5-5695fd3b3d77",
  "uuid": "88671e51-4d38-4630-b692-fdb646cba5d5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C2pHrEG7wg6QyrGXK7eB9P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6426,
      "cache_read_input_tokens": 24017,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6426
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

_source line 17_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_015PFYKUgD5b155yVwD1S6WD`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__update_registry",
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
  "session_id": "edd9b099-6670-4002-8cb5-5695fd3b3d77",
  "uuid": "814bf13c-2d47-4a03-9807-d3f6fdd57bc3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C2pHrEG7wg6QyrGXK7eB9P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6426,
      "cache_read_input_tokens": 24017,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6426
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

_source line 18 · 2026-05-16T11:56:30.362Z_

<details><summary>↩ Tool result · `toolu_015PFYKUgD5b155yVwD1S6WD`</summary>

````text
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
  "session_id": "edd9b099-6670-4002-8cb5-5695fd3b3d77",
  "uuid": "039368b6-5d77-4711-8502-631014cfb483",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__update_registry"
    ],
    "query": "select:mcp__agent-ml-research__update_registry",
    "total_deferred_tools": 26
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01HFQSDU8GNR6dr3Skc5tmvo`</summary>

```json
{
  "exp_id": "llama31-taxei-s0",
  "field": "conclusion",
  "value": null,
  "project": "tax_error_inject_agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "edd9b099-6670-4002-8cb5-5695fd3b3d77",
  "uuid": "efbfb5c5-30d3-4e62-9cac-38edbc04aae6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JECKQDDa13LHPqtp19Wqma",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 723,
      "cache_read_input_tokens": 30443,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 723
      },
      "output_tokens": 5,
      "service_tier": "standard",
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

_source line 20 · 2026-05-16T11:56:38.417Z_

<details><summary>↩ Tool result · `toolu_01HFQSDU8GNR6dr3Skc5tmvo`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid conclusion 'None'. Valid: ['failed', 'killed', 'negative', 'success']\", \"metadata\": {\"elapsed_seconds\": 0.4219}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "edd9b099-6670-4002-8cb5-5695fd3b3d77",
  "uuid": "0f487d50-a96a-48cd-80bb-a37dbf798d2a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"Invalid conclusion 'None'. Valid: ['failed', 'killed', 'negative', 'success']\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4219}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Invalid conclusion 'None'. Valid: ['failed', 'killed', 'negative', 'success']\", \"metadata\": {\"elapsed_seconds\": 0.4219}}"
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
The registry doesn't accept null for conclusion. Let me check what other fields I can update. The conclusion field only accepts specific values. Maybe I should update the status field instead, or there might be another way to clear the failed conclusion.

Let me try reading the registry first to see the current state, then figure out what to do.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "edd9b099-6670-4002-8cb5-5695fd3b3d77",
  "uuid": "ec29b064-8c47-481b-9bfd-948d911436da",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019dvkEkLn9MfXwxWmC3gaLT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 208,
      "cache_read_input_tokens": 31166,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 208
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

_source line 22_

Registry 不接受 null 值清除 conclusion。让我查看当前完整状态。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "edd9b099-6670-4002-8cb5-5695fd3b3d77",
  "uuid": "6342d249-c276-4b1e-bf80-fb78293b026e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019dvkEkLn9MfXwxWmC3gaLT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 208,
      "cache_read_input_tokens": 31166,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 208
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

_source line 23_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HVJ7nVMDWNg5rMMYE4ghLn`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry",
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
  "session_id": "edd9b099-6670-4002-8cb5-5695fd3b3d77",
  "uuid": "3335b62a-9a95-487f-b435-87d8099717e4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019dvkEkLn9MfXwxWmC3gaLT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 208,
      "cache_read_input_tokens": 31166,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 208
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

_source line 24 · 2026-05-16T11:56:43.744Z_

<details><summary>↩ Tool result · `toolu_01HVJ7nVMDWNg5rMMYE4ghLn`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_registry"
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
  "session_id": "edd9b099-6670-4002-8cb5-5695fd3b3d77",
  "uuid": "d6c30a47-3a77-4a49-af82-8335a832f684",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_registry"
    ],
    "query": "select:mcp__agent-ml-research__read_registry",
    "total_deferred_tools": 26
  }
}
```

</details>

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01PiiKoLvueVz2EAe2du3Wyt`</summary>

```json
{
  "filters": {
    "exp_id": "llama31-taxei-s0"
  },
  "project": "tax_error_inject_agent",
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
  "session_id": "edd9b099-6670-4002-8cb5-5695fd3b3d77",
  "uuid": "ecb7b3ec-7a93-4584-933d-53d6d286f108",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012b4Neoan55h3PKsDYo3FZh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 658,
      "cache_read_input_tokens": 31374,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 658
      },
      "output_tokens": 42,
      "service_tier": "standard",
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

_source line 26 · 2026-05-16T11:56:47.828Z_

<details><summary>↩ Tool result · `toolu_01PiiKoLvueVz2EAe2du3Wyt`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3958}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "edd9b099-6670-4002-8cb5-5695fd3b3d77",
  "uuid": "009c1f7b-ef08-40df-ae33-98fcb1e2d2c9",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.3958}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3958}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 27_

<details><summary>Logged reasoning block</summary>

```text
The filter on exp_id didn't work. Let me try without filters to see all experiments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "edd9b099-6670-4002-8cb5-5695fd3b3d77",
  "uuid": "46cd71a2-9210-4cd3-9904-953ccefe7e7d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CMbRAV5ZcSLvuZzZ2eNsSJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 199,
      "cache_read_input_tokens": 32032,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 199
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01FHqW5oJzescu6UJPSXTEL9`</summary>

```json
{
  "project": "tax_error_inject_agent",
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
  "session_id": "edd9b099-6670-4002-8cb5-5695fd3b3d77",
  "uuid": "28fa7c00-ac7c-4f47-a554-616c5d558ccc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CMbRAV5ZcSLvuZzZ2eNsSJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 199,
      "cache_read_input_tokens": 32032,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 199
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

_source line 29 · 2026-05-16T11:56:52.740Z_

<details><summary>↩ Tool result · `toolu_01FHqW5oJzescu6UJPSXTEL9`</summary>

```text
Error: result (227,926 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/edd9b099-6670-4002-8cb5-5695fd3b3d77/tool-results/mcp-agent-ml-research-read_registry-1778932612722.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/edd9b099-6670-4002-8cb5-5695fd3b3d77/tool-results/mcp-agent-ml-research-read_registry-1778932612722.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/edd9b099-6670-4002-8cb5-5695fd3b3d77/tool-results/mcp-agent-ml-research-read_registry-1778932612722.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "edd9b099-6670-4002-8cb5-5695fd3b3d77",
  "uuid": "2d83ba1b-0324-47cf-9e6a-373aca9272ed",
  "tool_use_result": {
    "content": "Error: result (227,926 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/edd9b099-6670-4002-8cb5-5695fd3b3d77/tool-results/mcp-agent-ml-research-read_registry-1778932612722.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/edd9b099-6670-4002-8cb5-5695fd3b3d77/tool-results/mcp-agent-ml-research-read_registry-1778932612722.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/edd9b099-6670-4002-8cb5-5695fd3b3d77/tool-results/mcp-agent-ml-research-read_registry-1778932612722.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"recovery-taxei-s7\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T11:53:18.146Z\", \"updated_at\": \"2026-05-16T11:53:57.696Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python3 eval/injected_eval.py --model_path checkpoints/mini_taxei_sft_v4_seed7/.../checkpoint-3387 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --model_variant taxei --output_file eval_results/v4_taxei_recovery_eval_s7.json\", \"server\": \"autodl-5090\", \"data_path\": \"eval/injected_eval.py\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + TaxEI s7 LoRA\", \"seed\": 7, \"checkpoint_source\": \"checkpoints/mini_taxei_sft_v4_seed7\", \"eval_data\": \"ALFWorld injected eval 47 tasks\", \"hypothesis\": \"Recovery eval TaxEI s7 - complete 5-seed recovery validation\"}, \"conclusion\": \"success\"}, \"llama31-random-s42-clean\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T11:30:37.651Z\", \"updated_at\": \"2026-05-16T11:50:54.372Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python3 eval/recovery.py --model_path output/llama31-random-s42/v0-20260516-142300/checkpoint-3387 --base_model /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct --num_episodes 47 --task_list eval/eval_tasks_47.json --output eval_results/llama31_random_s42_clean.json\", \"server\": \"autodl-5090\", \"data_path\": \"eval/eval_tasks_47.json\", \"data_count\": 47, \"model_name\": \"Meta-Llama-3.1-8B-Instruct + llama31-random-s42 LoRA\", \"seed\": 42, \"checkpoint_source\": \"output/llama31-random-s42/v0-20260516-142300/checkpoint-3387\", \"eval_data\": \"ALFWorld clean eval 47 tasks\", \"hypothesis\": \"LLaMA Random s42 clean eval - baseline success rate without injection\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.766, \"eval_type\": \"clean\", \"eval_script\": \"eval/recovery.py\", \"total_episodes\": 47, \"output_file\": \"eval_results/llama31_random_s42_clean.json\"}, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/llama31-random-s42/v0-20260516-142300/checkpoint-3387\", \"log_path\": \"eval_results/llama31_random_s42_clean.json\", \"completed_at\": \"2026-05-16T11:50:54.372Z\"}, \"llama31-random-s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T09:16:00.115Z\", \"updated_at\": \"2026-05-16T11:28:10.720Z\", \"spec\": {\"command\": \"swift sft --model /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct --dataset data/mini_pipeline_v4/sft_random_v4.jsonl --output_dir output/llama31-random-s0 --lora_rank 16 --num_train_epochs 3 --per_device_train_batch_size 4 --gradient_accumulation_steps 2 --learning_rate 1e-4 --max_length 4096 --seed 0 --data_seed 0 --logging_steps 10 --gradient_checkpointing true --bf16 true --save_strategy epoch\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"260936\", \"log_path\": \"~/runs/tax_error_inject_agent/llama31-random-s0.log\", \"submitted_at\": \"2026-05-16T09:15:59.761Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/mini_pipeline_v4/sft_random_v4.jsonl\", \"data_count\": 9031, \"model_name\": \"Meta-Llama-3.1-8B-Instruct\", \"seed\": 0, \"wall_clock_seconds\": 7931.0, \"gpu_hours\": 2.2}, \"reproduce\": {\"finished_at\": \"2026-05-16T11:24:56.461Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T11:24:59.790065+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"final_train_loss\": 0.3368, \"epoch1_loss\": 0.452, \"epoch2_loss\": 0.238, \"epoch3_loss\": 0.134, \"final_token_acc\": 0.9357, \"train_runtime_sec\": 7622, \"train_steps\": 3387, \"peak_memory_gib\": 30.74, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/llama31-random-s0/v0-20260516-171608/checkpoint-3387\"}, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/llama31-random-s0/v0-20260516-171608/checkpoint-3387\", \"log_path\": \"~/runs/tax_error_inject_agent/llama31-random-s0.log\", \"completed_at\": \"2026-05-16T11:28:10.720Z\"}, \"llama31-vanilla-s0-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T10:39:37.086Z\", \"updated_at\": \"2026-05-16T11:21:29.608Z\", \"hypothesis\": \"LLaMA-3.1-8B Vanilla s0 injected eval - cross-model validation seed 0\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python3 eval/injected_eval.py --model_path output/llama31-vanilla-s0/v0-20260516-171603/checkpoint-1635 --base_model /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct --model_variant vanilla --seed 0 --num_episodes 47 --output eval_results/llama31_vanilla_s0_injected.json\", \"server\": \"autodl-5090\", \"data_path\": \"eval/injected_eval.py\", \"data_count\": 47, \"model_name\": \"Meta-Llama-3.1-8B-Instruct + llama31-vanilla-s0 LoRA\", \"seed\": 0, \"checkpoint_source\": \"output/llama31-vanilla-s0/v0-20260516-171603/checkpoint-1635\", \"eval_data\": \"ALFWorld injected eval 47 tasks\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T11:05:01.407Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T11:05:03.246Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T11:05:05.820946+00:00\"}]}, \"metrics\": {\"recovery_rate\": 0.745, \"recovery_count\": \"35/47\", \"detection_rate\": 0.277, \"eval_type\": \"injected\", \"eval_script\": \"injected_eval.py\", \"output_file\": \"eval_results/llama31_vanilla_s0_injected.json\", \"C1_context_truncation\": {\"recovery\": 0.667, \"detection\": 0.167}, \"C4_observation_masking\": {\"recovery\": 0.727, \"detection\": 0.364}, \"P1_step_order_swap\": {\"recovery\": 0.917, \"detection\": 0.333}, \"P2_sub_goal_deletion\": {\"recovery\": 0.667, \"detection\": 0.25}}}, \"v4-random-recovery-eval-s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T12:44:10.000Z\", \"updated_at\": \"2026-05-16T10:54:26.532Z\", \"spec\": {\"model_name\": \"Qwen3-8B + LoRA (mini_random_sft_v4_seed0)\", \"seed\": 0, \"method\": \"random\", \"eval_type\": \"recovery\", \"parent\": \"v4-random-sft-s0\", \"checkpoint_source\": \"checkpoints/mini_random_sft_v4_seed0/v0-20260515-014329/checkpoint-3387\", \"eval_data\": \"ALFWorld 47 episodes with error injection\", \"server\": \"autodl-5090\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python eval/injected_eval.py --model_path checkpoints/mini_random_sft_v4_seed0/v0-20260515-014329/checkpoint-3387 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --model_variant random --output eval_results/v4_random_recovery_eval_s0.json --device cuda:0 --seed 42 --num_episodes 47\", \"data_path\": \"/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_random_recovery_eval_s0.json\", \"data_count\": 47}, \"conclusion\": \"success\", \"checkpoint_path\": \"checkpoints/mini_random_sft_v4_seed0/v0-20260515-014329/checkpoint-3387\", \"log_path\": \"eval_results/v4_random_recovery_eval_s0.json\", \"completed_at\": \"2026-05-16T10:54:19.062Z\", \"metrics\": {\"recovery_rate\": 0.553, \"detection_rate\": 0, \"success_rate\": 0.553, \"total_episodes\": 47, \"by_operator\": {\"C1_context_truncation\": {\"total\": 12, \"recovered\": 7, \"recovery_rate\": 0.583}, \"C4_observation_masking\": {\"total\": 11, \"recovered\": 6, \"recovery_rate\": 0.545}, \"P1_step_order_swap\": {\"total\": 12, \"recovered\": 7, \"recovery_rate\": 0.583}, \"P2_sub_goal_deletion\": {\"total\": 12, \"recovered\": 6, \"recovery_rate\": 0.5}}}}, \"llama31-taxei-s0\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T09:15:57.399Z\", \"updated_at\": \"2026-05-16T10:48:32.797Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 swift sft --model Meta-Llama-3.1-8B-Instruct --dataset sft_taxei_v4.jsonl --output_dir output/llama31-taxei-s0 --lora_rank 16 --num_train_epochs 3 --seed 0\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"262833\", \"log_path\": \"~/runs/tax_error_inject_agent/llama31-taxei-s0.log\", \"submitted_at\": \"2026-05-16T09:15:57.070Z\", \"submitted_via\": \"manual_retry_v1\", \"backend\": \"interactive_pts\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/tax_error_inject_agent/data/mini_pipeline_v4/sft_taxei_v4.jsonl\", \"data_count\": 9029, \"model_name\": \"Meta-Llama-3.1-8B-Instruct\", \"seed\": 0, \"hypothesis\": \"Cross-model: LLaMA TaxEI s0 - 2nd seed for 3-seed cross-model validation\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T10:20:07.409Z\"}, \"failure_reason\": null, \"conclusion\": \"failed\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T10:20:11.090300+00:00\"}]}}, \"llama31-vanilla-s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T09:15:55.388Z\", \"updated_at\": \"2026-05-16T10:29:59.217Z\", \"spec\": {\"command\": \"swift sft --model Meta-Llama-3.1-8B-Instruct --dataset sft_vanilla_v4.jsonl\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"257144\", \"log_path\": \"~/runs/tax_error_inject_agent/llama31-vanilla-s0.log\", \"submitted_at\": \"2026-05-16T09:15:54.991Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_count\": 4358, \"data_path\": \"data/mini_pipeline_v4/sft_vanilla_v4.jsonl\", \"model_name\": \"Meta-Llama-3.1-8B-Instruct\", \"seed\": 0, \"wall_clock_seconds\": 4158.6, \"gpu_hours\": 1.16, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/llama31-vanilla-s0/v0-20260516-171603/checkpoint-1635\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T10:26:48.334Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T10:26:50.786934+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/llama31-vanilla-s0/v0-20260516-171603/checkpoint-1635\", \"log_path\": \"/root/runs/tax_error_inject_agent/llama31-vanilla-s0.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T10:29:44.360Z\", \"metrics\": {\"final_train_loss\": 0.398, \"epoch1_loss\": 0.481, \"epoch2_loss\": 0.362, \"epoch3_loss\": 0.273, \"final_token_acc\": 0.909, \"train_runtime_sec\": 4158.6}}, \"eval-rp-s7\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T10:25:59.082Z\", \"updated_at\": \"2026-05-16T10:26:30.070Z\", \"spec\": {\"hypothesis\": \"TaxEI-RP s7 eval - complete 5-seed recovery-paired injection assessment\", \"model_name\": \"Qwen3-8B + TaxEI-RP LoRA\", \"seed\": 7, \"checkpoint_source\": \"/root/autodl-tmp/tax_error_inject_agent/output/v4-taxei-rp-s7/v0-20260516-142303/checkpoint-5415\", \"eval_data\": \"ALFWorld 47 injected tasks\", \"data_path\": \"eval/injected_eval.py (47 ALFWorld tasks)\", \"data_count\": 47, \"command\": \"CUDA_VISIBLE_DEVICES=3 python3 eval/injected_eval.py --model_path output/v4-taxei-rp-s7/v0-20260516-142303/checkpoint-5415 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --model_variant taxei --output_file eval_results/v4_taxei_rp_recovery_eval_s7.json\", \"server\": \"autodl-5090\"}, \"metrics\": {\"recovery_rate\": 0.596, \"recovery_count\": \"28/47\", \"detection_rate\": 0}, \"conclusion\": \"success\", \"log_path\": \"/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_taxei_rp_recovery_eval_s7.json\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/v4-taxei-rp-s7/v0-20260516-142303/checkpoint-5415\", \"completed_at\": \"2026-05-16T10:26:30.070Z\"}, \"v4-taxei-rp-s7\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T06:22:54.703Z\", \"updated_at\": \"2026-05-16T10:15:30.071Z\", \"spec\": {\"command\": \"swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset sft_taxei_rp.jsonl --lora_rank 16 --num_train_epochs 3 --bs 4 --ga 2 --lr 1e-4 --max_length 4096 --seed 7\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/tax_error_inject_agent/data/recovery_paired/sft_taxei_rp.jsonl\", \"data_count\": 14437, \"model_name\": \"Qwen3-8B\", \"seed\": 7, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/v4-taxei-rp-s7/v0-20260516-142303/checkpoint-5415\", \"log_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/v4-taxei-rp-s7/v0-20260516-142303/logging.jsonl\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T10:11:07.987Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T10:11:10.984555+00:00\"}]}, \"metrics\": {\"train_loss\": 0.3855, \"token_acc\": 0.9103, \"duration_minutes\": 226.6, \"peak_memory_gib\": 30.25, \"train_samples_per_second\": 3.185}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T10:14:13.073Z\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/v4-taxei-rp-s7/v0-20260516-142303/checkpoint-5415\"}, \"recovery-taxei-s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T09:40:11.652Z\", \"updated_at\": \"2026-05-16T09:40:44.285Z\", \"spec\": {\"hypothesis\": \"Recovery eval TaxEI s1 - does TaxEI-trained model recover from injected errors?\", \"model_name\": \"Qwen3-8B + TaxEI LoRA\", \"seed\": 1, \"checkpoint_source\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_taxei_sft_v4_seed1/v0-20260515-214035/checkpoint-3387\", \"eval_data\": \"ALFWorld 47 injected tasks\", \"data_path\": \"eval/injected_eval.py (47 ALFWorld tasks)\", \"data_count\": 47, \"command\": \"CUDA_VISIBLE_DEVICES=0 python3 eval/injected_eval.py --model_path checkpoints/mini_taxei_sft_v4_seed1/v0-20260515-214035/checkpoint-3387 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --model_variant taxei --output_file eval_results/v4_taxei_recovery_eval_s1.json\", \"server\": \"autodl-5090\"}, \"metrics\": {\"recovery_rate\": 0.617, \"recovery_count\": \"29/47\", \"detection_rate\": 0, \"C1_context_truncation\": 0.75, \"C4_observation_masking\": 0.636, \"P1_step_order_swap\": 0.583, \"P2_sub_goal_deletion\": 0.5}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_taxei_sft_v4_seed1/v0-20260515-214035/checkpoint-3387\", \"log_path\": \"/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_taxei_recovery_eval_s1.json\", \"completed_at\": \"2026-05-16T09:40:44.285Z\"}, \"llama31-random-s42-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T09:14:41.175Z\", \"updated_at\": \"2026-05-16T09:15:28.130Z\", \"spec\": {\"hypothesis\": \"Cross-model: LLaMA Random s42 eval — random injection control on LLaMA\", \"model_name\": \"Meta-Llama-3.1-8B-Instruct + Random LoRA\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/tax_error_inject_agent/output/llama31-random-s42/v0-20260516-142300/checkpoint-3387\", \"eval_data\": \"ALFWorld 47 injected tasks\", \"data_path\": \"eval/injected_eval.py (47 ALFWorld tasks)\", \"data_count\": 47, \"command\": \"CUDA_VISIBLE_DEVICES=2 python3 eval/injected_eval.py --model_path output/llama31-random-s42/v0-20260516-142300/checkpoint-3387 --base_model /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct --model_variant random --output_file eval_results/llama31_random_s42.json\", \"server\": \"autodl-5090\"}, \"metrics\": {\"recovery_rate\": 0.766, \"recovery_count\": \"36/47\", \"detection_rate\": 0.298, \"C1_context_truncation\": 0.667, \"C4_observation_masking\": 0.727, \"P1_step_order_swap\": 0.917, \"P2_sub_goal_deletion\": 0.75, \"C1_detection\": 0.417, \"C4_detection\": 0.364, \"P1_detection\": 0.333, \"P2_detection\": 0.083}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/llama31-random-s42/v0-20260516-142300/checkpoint-3387\", \"log_path\": \"/root/autodl-tmp/tax_error_inject_agent/eval_results/llama31_random_s42.json\", \"completed_at\": \"2026-05-16T09:15:28.130Z\"}, \"llama31-taxei-s42-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T09:14:40.025Z\", \"updated_at\": \"2026-05-16T09:15:26.908Z\", \"spec\": {\"hypothesis\": \"Cross-model: LLaMA TaxEI s42 eval — does taxonomy-guided injection help on LLaMA?\", \"model_name\": \"Meta-Llama-3.1-8B-Instruct + TaxEI LoRA\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/tax_error_inject_agent/output/llama31-taxei-s42/v0-20260516-142258/checkpoint-3387\", \"eval_data\": \"ALFWorld 47 injected tasks\", \"data_path\": \"eval/injected_eval.py (47 ALFWorld tasks)\", \"data_count\": 47, \"command\": \"CUDA_VISIBLE_DEVICES=1 python3 eval/injected_eval.py --model_path output/llama31-taxei-s42/v0-20260516-142258/checkpoint-3387 --base_model /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct --model_variant taxei --output_file eval_results/llama31_taxei_s42.json\", \"server\": \"autodl-5090\"}, \"metrics\": {\"recovery_rate\": 0.745, \"recovery_count\": \"35/47\", \"detection_rate\": 0.298, \"C1_context_truncation\": 0.833, \"C4_observation_masking\": 0.727, \"P1_step_order_swap\": 0.583, \"P2_sub_goal_deletion\": 0.833, \"C1_detection\": 0.167, \"C4_detection\": 0.364, \"P1_detection\": 0.25, \"P2_detection\": 0.417}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/llama31-taxei-s42/v0-20260516-142258/checkpoint-3387\", \"log_path\": \"/root/autodl-tmp/tax_error_inject_agent/eval_results/llama31_taxei_s42.json\", \"completed_at\": \"2026-05-16T09:15:26.908Z\"}, \"recovery-vanilla-s7\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T08:53:10.619Z\", \"updated_at\": \"2026-05-16T08:53:54.916Z\", \"spec\": {\"hypothesis\": \"Recovery eval Vanilla s7 - confirm Recovery≈Resilience\", \"model_name\": \"Qwen3-8B + Vanilla LoRA\", \"seed\": 7, \"checkpoint_source\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_vanilla_sft_v4_seed7/v1-20260515-214032/checkpoint-1635\", \"eval_data\": \"ALFWorld 47 injected tasks\", \"data_path\": \"eval/injected_eval.py (47 ALFWorld tasks)\", \"data_count\": 47, \"command\": \"CUDA_VISIBLE_DEVICES=0 python3 eval/injected_eval.py --model_path checkpoints/mini_vanilla_sft_v4_seed7/v1-20260515-214032/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --model_variant vanilla --output_file eval_results/v4_vanilla_recovery_eval_s7.json\", \"server\": \"autodl-5090\"}, \"conclusion\": \"success\", \"metrics\": {\"recovery_rate\": 0.745, \"recovery_count\": \"35/47\", \"detection_rate\": 0, \"C1_context_truncation\": 0.75, \"C4_observation_masking\": 0.727, \"P1_step_order_swap\": 0.75, \"P2_sub_goal_deletion\": 0.75}, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_vanilla_sft_v4_seed7/v1-20260515-214032/checkpoint-1635\", \"log_path\": \"/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_vanilla_recovery_eval_s7.json\", \"completed_at\": \"2026-05-16T08:53:54.916Z\"}, \"recovery-vanilla-s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T08:26:23.215Z\", \"updated_at\": \"2026-05-16T08:49:34.621Z\", \"spec\": {\"hypothesis\": \"Recovery eval Vanilla s1 - confirm Recovery≈Resilience\", \"model_name\": \"Qwen3-8B + Vanilla LoRA\", \"seed\": 1, \"checkpoint_source\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_vanilla_sft_v4_seed1/v0-20260515-214031/checkpoint-1635\", \"eval_data\": \"ALFWorld 47 injected tasks\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T08:32:46.932Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T08:32:48.721Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T08:32:54.320388+00:00\"}]}, \"metrics\": {\"recovery_rate\": 0.66, \"recovery_count\": \"31/47\", \"detection_rate\": 0, \"C1_context_truncation\": 0.667, \"C4_observation_masking\": 0.545, \"P1_step_order_swap\": 0.667, \"P2_sub_goal_deletion\": 0.75}}, \"llama31-random-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T06:22:51.516Z\", \"updated_at\": \"2026-05-16T08:46:26.260Z\", \"spec\": {\"data_path\": \"/root/autodl-tmp/tax_error_inject_agent/data/mini_pipeline_v4/sft_random_v4.jsonl\", \"data_count\": 9029, \"model_name\": \"Meta-Llama-3.1-8B-Instruct\", \"seed\": 42, \"hypothesis\": \"Cross-model generalizability: LLaMA-3.1-8B Random condition control\", \"command\": \"llamafactory train\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:2\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/llama31-random-s42/v0-20260516-142300/checkpoint-3387/\", \"log_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/llama31-random-s42/v0-20260516-142300/logging.jsonl\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T08:32:16.672Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T08:32:20.396930+00:00\"}]}, \"metrics\": {\"train_loss\": 0.3366, \"token_acc\": 0.9364, \"train_steps\": 3387, \"train_duration_s\": 7622}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T08:39:26.528Z\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/llama31-random-s42/v0-20260516-142300/checkpoint-3387\"}, \"llama31-taxei-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T06:22:49.346Z\", \"updated_at\": \"2026-05-16T08:46:25.092Z\", \"spec\": {\"data_path\": \"/root/autodl-tmp/tax_error_inject_agent/data/mini_pipeline_v4/sft_taxei_v4.jsonl\", \"data_count\": 9029, \"model_name\": \"Meta-Llama-3.1-8B-Instruct\", \"seed\": 42, \"hypothesis\": \"Cross-model generalizability: LLaMA-3.1-8B TaxEI condition to verify Qwen3-8B findings transfer\", \"command\": \"swift sft --model /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct --dataset sft_taxei_v4.jsonl --lora_rank 16 --num_train_epochs 3 --bs 4 --ga 2 --lr 1e-4 --max_length 4096 --seed 42\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/llama31-taxei-s42/v0-20260516-142258/checkpoint-3387\", \"log_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/llama31-taxei-s42/v0-20260516-142258/logging.jsonl\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T08:36:00.235Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T08:36:05.288585+00:00\"}]}, \"metrics\": {\"train_loss\": 0.3366, \"token_acc\": 0.9357, \"train_steps\": 3387, \"train_duration_s\": 7782}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T08:39:34.756Z\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/llama31-taxei-s42/v0-20260516-142258/checkpoint-3387\"}, \"llama31-vanilla-s42-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T08:07:12.328Z\", \"updated_at\": \"2026-05-16T08:36:24.810Z\", \"spec\": {\"hypothesis\": \"LLaMA-3.1-8B Vanilla s42 injected eval - cross-model baseline\", \"model_name\": \"LLaMA-3.1-8B-Instruct + Vanilla LoRA\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/tax_error_inject_agent/output/llama31-vanilla-s42/v0-20260516-143227/checkpoint-1635\", \"eval_data\": \"ALFWorld 47 injected tasks\"}, \"metrics\": {\"recovery_rate\": 0.745, \"recovery_count\": \"35/47\", \"detection_rate\": 0.213, \"C1_context_truncation\": 0.75, \"C4_observation_masking\": 0.727, \"P1_step_order_swap\": 0.75, \"P2_sub_goal_deletion\": 0.75}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/llama31-vanilla-s42/v0-20260516-143227/checkpoint-1635\", \"log_path\": \"~/runs/tax_error_inject_agent/llama31-vanilla-s42-eval.log\", \"completed_at\": \"2026-05-16T08:36:24.810Z\"}, \"llama31-vanilla-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T06:32:19.082Z\", \"updated_at\": \"2026-05-16T07:48:06.140Z\", \"spec\": {\"command\": \"swift sft --model Meta-Llama-3.1-8B-Instruct --dataset sft_vanilla_v4.jsonl --lora_rank 16 --epochs 3 --bs 4 --ga 2 --lr 1e-4 --max_length 4096 --seed 42\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"pid\": \"244644\", \"log_path\": \"~/runs/tax_error_inject_agent/llama31-vanilla-s42.log\", \"submitted_at\": \"2026-05-16T06:32:18.732Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/tax_error_inject_agent/data/mini_pipeline_v4/sft_vanilla_v4.jsonl\", \"data_count\": 9029, \"model_name\": \"Meta-Llama-3.1-8B-Instruct\", \"seed\": 42, \"hypothesis\": \"Cross-model generalizability: LLaMA-3.1-8B Vanilla baseline\", \"wall_clock_seconds\": 4547.4, \"gpu_hours\": 1.26}, \"reproduce\": {\"finished_at\": \"2026-05-16T07:44:55.468Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T07:44:59.077032+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/llama31-vanilla-s42/v0-20260516-143227/checkpoint-1635\", \"metrics\": {\"train_loss\": 0.40025, \"token_acc\": 0.9067, \"train_steps\": 1635, \"train_duration_s\": 4157}, \"conclusion\": \"success\", \"log_path\": \"~/runs/tax_error_inject_agent/llama31-vanilla-s42.log\", \"completed_at\": \"2026-05-16T07:48:06.140Z\"}, \"eval-rp-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T06:32:34.645Z\", \"updated_at\": \"2026-05-16T06:33:18.281Z\", \"spec\": {\"hypothesis\": \"TaxEI-RP recovery eval seed=42\", \"model_name\": \"Qwen3-8B + TaxEI-RP LoRA\", \"seed\": 42, \"command\": \"python eval/injected_eval.py --model_path v4-taxei-rp-s42 checkpoint --model_variant taxei --seed 42\", \"server\": \"autodl-5090\", \"data_path\": \"ALFWorld injected tasks\", \"data_count\": 47, \"gpu\": \"cuda:0\"}, \"metrics\": {\"recovery_rate\": 0.383, \"recovery_count\": \"18/47\", \"C1_context_truncation\": 0.5, \"C4_observation_masking\": 0.273, \"P1_step_order_swap\": 0.5, \"P2_sub_goal_deletion\": 0.25, \"detection_rate\": 0}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/v4-taxei-rp-s42/v0-20260516-101703/checkpoint-5415\", \"log_path\": \"/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_taxei_rp_s42_injected.json\", \"completed_at\": \"2026-05-16T06:33:18.281Z\"}, \"eval-rp-s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T06:27:34.660Z\", \"updated_at\": \"2026-05-16T06:30:59.753Z\", \"failure_reason\": \"\", \"conclusion\": \"success\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T06:27:37.861045+00:00\"}]}, \"metrics\": {\"recovery_rate\": 0.489, \"detection_rate\": 0, \"episodes\": 47, \"recovered\": 23}, \"spec\": {\"command\": \"python eval_recovery.py --seed 1\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/tax_error_inject_agent/data/recovery_paired/\", \"data_count\": 47, \"model_name\": \"Qwen3-8B (TaxEI-RP s1)\", \"seed\": 1, \"checkpoint_source\": \"v4-taxei-rp-s1\", \"eval_data\": \"47 ALFWorld clean tasks with error injection\"}, \"log_path\": \"/tmp/eval_rp_s1.log\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/eval_outputs/v4_taxei_rp_s1_injected.json\", \"completed_at\": \"2026-05-16T06:30:48.894Z\"}, \"eval-rp-s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T06:27:52.208Z\", \"updated_at\": \"2026-05-16T06:30:58.894Z\", \"failure_reason\": \"\", \"conclusion\": \"success\", \"reproduce\": {\"finished_at\": \"2026-05-16T06:27:54.715Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T06:28:01.102430+00:00\"}]}, \"metrics\": {\"recovery_rate\": 0.468, \"detection_rate\": 0, \"episodes\": 47, \"recovered\": 22}, \"spec\": {\"command\": \"python eval_recovery.py --seed 0\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/tax_error_inject_agent/data/recovery_paired/\", \"data_count\": 47, \"model_name\": \"Qwen3-8B (TaxEI-RP s0)\", \"seed\": 0, \"checkpoint_source\": \"v4-taxei-rp-s0\", \"eval_data\": \"47 ALFWorld clean tasks with error injection\"}, \"log_path\": \"/tmp/eval_rp_s0.log\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/eval_outputs/v4_taxei_rp_s0_injected.json\", \"completed_at\": \"2026-05-16T06:30:47.736Z\"}, \"eval-rp-s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T06:27:26.558Z\", \"updated_at\": \"2026-05-16T06:30:58.290Z\", \"failure_reason\": \"\", \"conclusion\": \"success\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T06:27:29.414786+00:00\"}]}, \"metrics\": {\"recovery_rate\": 0.574, \"detection_rate\": 0, \"episodes\": 47, \"recovered\": 27}, \"spec\": {\"command\": \"python eval_recovery.py --seed 123\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/tax_error_inject_agent/data/recovery_paired/\", \"data_count\": 47, \"model_name\": \"Qwen3-8B (TaxEI-RP s123)\", \"seed\": 123, \"checkpoint_source\": \"v4-taxei-rp-s123\", \"eval_data\": \"47 ALFWorld clean tasks with error injection\"}, \"log_path\": \"/tmp/eval_rp_s123.log\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/eval_outputs/v4_taxei_rp_s123_injected.json\", \"completed_at\": \"2026-05-16T06:30:46.571Z\"}, \"v4-taxei-rp-s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T02:16:59.271Z\", \"updated_at\": \"2026-05-16T06:15:41.090Z\", \"spec\": {\"command\": \"swift sft --model Qwen3-8B --dataset sft_taxei_rp.jsonl --lora_rank 16 --epochs 3 --bs 4 --ga 2 --lr 1e-4 --max_length 4096 --seed 123\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"223254\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-rp-s123.log\", \"submitted_at\": \"2026-05-16T02:16:58.962Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/tax_error_inject_agent/data/recovery_paired/sft_taxei_rp.jsonl\", \"data_count\": 14437, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"hypothesis\": \"Recovery-paired training multi-seed replication (seed=123)\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/v4-taxei-rp-s123/v0-20260516-101708/checkpoint-5415\", \"wall_clock_seconds\": 13954.9, \"gpu_hours\": 3.88}, \"reproduce\": {\"finished_at\": \"2026-05-16T06:05:08.878Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T06:05:14.118671+00:00\"}]}, \"metrics\": {\"train_loss\": 0.38524182, \"eval_loss\": null, \"duration_minutes\": 226.5, \"token_acc\": 0.91372913, \"train_samples_per_second\": 3.187, \"peak_memory_gib\": 30.66}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T06:09:33.865Z\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/v4-taxei-rp-s123/v0-20260516-101708/checkpoint-5415\"}, \"v4-taxei-rp-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T02:16:54.022Z\", \"updated_at\": \"2026-05-16T06:15:40.096Z\", \"spec\": {\"command\": \"swift sft --model Qwen3-8B --dataset sft_taxei_rp.jsonl --lora_rank 16 --epochs 3 --bs 4 --ga 2 --lr 1e-4 --max_length 4096 --seed 42\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"222969\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-rp-s42.log\", \"submitted_at\": \"2026-05-16T02:16:53.716Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/tax_error_inject_agent/data/recovery_paired/sft_taxei_rp.jsonl\", \"data_count\": 14437, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"hypothesis\": \"If recovery-paired training (TaxEI-RP) also fails to improve over Vanilla, task structure is the primary factor. If it works, recovery pairing is the key missing ingredient from PALADIN.\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/v4-taxei-rp-s42/v0-20260516-101703/checkpoint-5415\", \"wall_clock_seconds\": 13958.9, \"gpu_hours\": 3.88}, \"reproduce\": {\"finished_at\": \"2026-05-16T06:04:57.317Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T06:04:59.869491+00:00\"}]}, \"metrics\": {\"train_loss\": 0.38469276, \"eval_loss\": null, \"duration_minutes\": 226.67, \"token_acc\": 0.92487562, \"train_samples_per_second\": 3.185, \"peak_memory_gib\": 30.68}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T06:09:32.658Z\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/v4-taxei-rp-s42/v0-20260516-101703/checkpoint-5415\"}, \"v4-taxei-rp-s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T02:18:24.897Z\", \"updated_at\": \"2026-05-16T06:15:38.814Z\", \"spec\": {\"command\": \"swift sft --model Qwen3-8B --dataset sft_taxei_rp.jsonl --lora_rank 16 --epochs 3 --bs 4 --ga 2 --lr 1e-4 --max_length 4096 --seed 1\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"224231\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-rp-s1.log\", \"submitted_at\": \"2026-05-16T02:18:24.590Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/tax_error_inject_agent/data/recovery_paired/sft_taxei_rp.jsonl\", \"data_count\": 14437, \"model_name\": \"Qwen3-8B\", \"seed\": 1, \"hypothesis\": \"Recovery-paired training multi-seed replication (seed=1)\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/v4-taxei-rp-s1/v0-20260516-101834/checkpoint-5415\", \"wall_clock_seconds\": 13870.4, \"gpu_hours\": 3.85}, \"reproduce\": {\"finished_at\": \"2026-05-16T06:05:21.988Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T06:05:27.447822+00:00\"}]}, \"metrics\": {\"train_loss\": 0.38530399, \"eval_loss\": null, \"duration_minutes\": 226.3, \"token_acc\": 0.91761223, \"train_samples_per_second\": 3.19, \"peak_memory_gib\": 30.17}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T06:09:35.005Z\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/v4-taxei-rp-s1/v0-20260516-101834/checkpoint-5415\"}, \"v4-taxei-rp-s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T02:16:56.691Z\", \"updated_at\": \"2026-05-16T06:15:37.765Z\", \"spec\": {\"command\": \"swift sft --model Qwen3-8B --dataset sft_taxei_rp.jsonl --lora_rank 16 --epochs 3 --bs 4 --ga 2 --lr 1e-4 --max_length 4096 --seed 0\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"223049\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-rp-s0.log\", \"submitted_at\": \"2026-05-16T02:16:56.390Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/tax_error_inject_agent/data/recovery_paired/sft_taxei_rp.jsonl\", \"data_count\": 14437, \"model_name\": \"Qwen3-8B\", \"seed\": 0, \"hypothesis\": \"Recovery-paired training multi-seed replication (seed=0)\", \"wall_clock_seconds\": 14321.4, \"gpu_hours\": 3.98}, \"reproduce\": {\"finished_at\": \"2026-05-16T06:10:47.000Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T06:10:49.871145+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.3847, \"token_acc\": 0.9065, \"duration_min\": 231.07, \"peak_memory_gib\": 30.37, \"train_samples_per_second\": 3.124}, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/v4-taxei-rp-s0/v0-20260516-101706/checkpoint-5415\", \"log_path\": \"/root/runs/tax_error_inject_agent/v4-taxei-rp-s0.log\", \"completed_at\": \"2026-05-16T06:15:37.765Z\"}, \"v4-taxei-recovery-eval-s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T12:43:43.113Z\", \"updated_at\": \"2026-05-16T03:23:08.899Z\", \"spec\": {\"checkpoint_path\": \"eval_results/v4_taxei_recovery_eval_s123.json\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-recovery-eval-s123.log\"}, \"metrics\": {\"recovery_rate\": 0.617, \"successes\": 29, \"total\": 47, \"detection_rate\": 0}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T03:23:08.899Z\"}, \"v4-taxei-recovery-eval-s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T12:43:41.449Z\", \"updated_at\": \"2026-05-16T03:23:07.706Z\", \"spec\": {\"checkpoint_path\": \"eval_results/v4_taxei_recovery_eval_s0.json\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-recovery-eval-s0.log\"}, \"metrics\": {\"recovery_rate\": 0.468, \"successes\": 22, \"total\": 47, \"detection_rate\": 0}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T03:23:07.706Z\"}, \"v4-vanilla-recovery-eval-s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T12:43:39.466Z\", \"updated_at\": \"2026-05-16T03:23:06.630Z\", \"spec\": {\"checkpoint_path\": \"eval_results/v4_vanilla_recovery_eval_s123.json\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-vanilla-recovery-eval-s123.log\"}, \"metrics\": {\"recovery_rate\": 0.66, \"successes\": 31, \"total\": 47, \"detection_rate\": 0}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T03:23:06.630Z\"}, \"v4-vanilla-recovery-eval-s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T12:43:38.052Z\", \"updated_at\": \"2026-05-16T03:23:05.513Z\", \"spec\": {\"checkpoint_path\": \"eval_results/v4_vanilla_recovery_eval_s0.json\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-vanilla-recovery-eval-s0.log\"}, \"metrics\": {\"recovery_rate\": 0.681, \"successes\": 32, \"total\": 47, \"detection_rate\": 0}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T03:23:05.513Z\"}, \"v4-random-fixed-inject50-s1-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:09:38.067Z\", \"updated_at\": \"2026-05-16T01:31:24.055Z\", \"spec\": {\"command\": \"python3 eval/recovery.py --model_path checkpoints/v4_random_fixed_inject50_s1/v1-20260516-075754/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --task_list eval/eval_tasks_47.json --num_episodes 47 --seed 42 --device cuda:0 --output eval_results/v4_random_fixed_inject50_s1_eval.json\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"data_path\": \"eval/eval_tasks_47.json\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (random fixed inject50 s1)\", \"seed\": 42, \"checkpoint_source\": \"v4-random-fixed-inject50-s1\", \"eval_data\": \"eval_tasks_47.json\", \"hypothesis\": \"v4 Random 50% seed=1 eval — 47 ALFWorld clean tasks. Dose-response 5-seed expansion.\"}, \"metrics\": {\"success_rate\": 0.702, \"successes\": 33, \"total\": 47, \"by_task_type\": {\"look_at_obj_in_light\": {\"total\": 6, \"success\": 5, \"rate\": 0.833}, \"pick_and_place_simple\": {\"total\": 8, \"success\": 5, \"rate\": 0.625}, \"pick_clean_then_place_in_recep\": {\"total\": 11, \"success\": 8, \"rate\": 0.727}, \"pick_cool_then_place_in_recep\": {\"total\": 7, \"success\": 4, \"rate\": 0.571}, \"pick_heat_then_place_in_recep\": {\"total\": 8, \"success\": 6, \"rate\": 0.75}, \"pick_two_obj_and_place\": {\"total\": 7, \"success\": 5, \"rate\": 0.714}}}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_random_fixed_inject50_s1_eval.json\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-fixed-inject50-s1-eval.log\", \"completed_at\": \"2026-05-16T01:31:24.055Z\"}, \"v4-taxei-fixed-inject50-s1-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:09:36.875Z\", \"updated_at\": \"2026-05-16T01:31:23.037Z\", \"spec\": {\"command\": \"python3 eval/recovery.py --model_path checkpoints/v4_taxei_fixed_inject50_s1/v0-20260516-075747/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --task_list eval/eval_tasks_47.json --num_episodes 47 --seed 42 --device cuda:0 --output eval_results/v4_taxei_fixed_inject50_s1_eval.json\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"data_path\": \"eval/eval_tasks_47.json\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (taxei fixed inject50 s1)\", \"seed\": 42, \"checkpoint_source\": \"v4-taxei-fixed-inject50-s1\", \"eval_data\": \"eval_tasks_47.json\", \"hypothesis\": \"v4 TaxEI 50% seed=1 eval — 47 ALFWorld clean tasks. Dose-response 5-seed expansion.\"}, \"metrics\": {\"success_rate\": 0.638, \"successes\": 30, \"total\": 47, \"by_task_type\": {\"look_at_obj_in_light\": {\"total\": 6, \"success\": 6, \"rate\": 1}, \"pick_and_place_simple\": {\"total\": 8, \"success\": 5, \"rate\": 0.625}, \"pick_clean_then_place_in_recep\": {\"total\": 11, \"success\": 7, \"rate\": 0.636}, \"pick_cool_then_place_in_recep\": {\"total\": 7, \"success\": 4, \"rate\": 0.571}, \"pick_heat_then_place_in_recep\": {\"total\": 8, \"success\": 5, \"rate\": 0.625}, \"pick_two_obj_and_place\": {\"total\": 7, \"success\": 3, \"rate\": 0.429}}}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_taxei_fixed_inject50_s1_eval.json\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-fixed-inject50-s1-eval.log\", \"completed_at\": \"2026-05-16T01:31:23.037Z\"}, \"v4-random-fixed-inject50-s7-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:09:39.957Z\", \"updated_at\": \"2026-05-16T01:21:18.406Z\", \"spec\": {\"command\": \"python3 eval/recovery.py --model_path checkpoints/v4_random_fixed_inject50_s7/v0-20260516-075756/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --task_list eval/eval_tasks_47.json --num_episodes 47 --seed 42 --device cuda:0 --output eval_results/v4_random_fixed_inject50_s7_eval.json\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"data_path\": \"eval/eval_tasks_47.json\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (random fixed inject50 s7)\", \"seed\": 42, \"checkpoint_source\": \"v4-random-fixed-inject50-s7\", \"eval_data\": \"eval_tasks_47.json\", \"hypothesis\": \"v4 Random 50% seed=7 eval — 47 ALFWorld clean tasks. Dose-response 5-seed expansion.\", \"checkpoint_path\": \"checkpoints/v4_random_fixed_inject50_s7/v0-20260516-075756/checkpoint-1635\", \"log_path\": \"eval_results/v4_random_fixed_inject50_s7_eval.json\"}, \"metrics\": {\"success_rate\": 0.468, \"successes\": 22, \"total\": 47, \"by_task_type\": {\"look_at_obj_in_light\": {\"total\": 6, \"success\": 4, \"rate\": 0.667}, \"pick_and_place_simple\": {\"total\": 8, \"success\": 4, \"rate\": 0.5}, \"pick_clean_then_place_in_recep\": {\"total\": 11, \"success\": 5, \"rate\": 0.455}, \"pick_cool_then_place_in_recep\": {\"total\": 7, \"success\": 1, \"rate\": 0.143}, \"pick_heat_then_place_in_recep\": {\"total\": 8, \"success\": 5, \"rate\": 0.625}, \"pick_two_obj_and_place\": {\"total\": 7, \"success\": 3, \"rate\": 0.429}}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T01:21:18.406Z\"}, \"v4-taxei-fixed-inject50-s7-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:09:39.016Z\", \"updated_at\": \"2026-05-16T01:21:17.391Z\", \"spec\": {\"command\": \"python3 eval/recovery.py --model_path checkpoints/v4_taxei_fixed_inject50_s7/v0-20260516-075754/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --task_list eval/eval_tasks_47.json --num_episodes 47 --seed 42 --device cuda:0 --output eval_results/v4_taxei_fixed_inject50_s7_eval.json\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:2\", \"data_path\": \"eval/eval_tasks_47.json\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (taxei fixed inject50 s7)\", \"seed\": 42, \"checkpoint_source\": \"v4-taxei-fixed-inject50-s7\", \"eval_data\": \"eval_tasks_47.json\", \"hypothesis\": \"v4 TaxEI 50% seed=7 eval — 47 ALFWorld clean tasks. Dose-response 5-seed expansion.\", \"checkpoint_path\": \"checkpoints/v4_taxei_fixed_inject50_s7/v0-20260516-075754/checkpoint-1635\", \"log_path\": \"eval_results/v4_taxei_fixed_inject50_s7_eval.json\"}, \"metrics\": {\"success_rate\": 0.553, \"successes\": 26, \"total\": 47, \"by_task_type\": {\"look_at_obj_in_light\": {\"total\": 6, \"success\": 5, \"rate\": 0.833}, \"pick_and_place_simple\": {\"total\": 8, \"success\": 4, \"rate\": 0.5}, \"pick_clean_then_place_in_recep\": {\"total\": 11, \"success\": 6, \"rate\": 0.545}, \"pick_cool_then_place_in_recep\": {\"total\": 7, \"success\": 2, \"rate\": 0.286}, \"pick_heat_then_place_in_recep\": {\"total\": 8, \"success\": 6, \"rate\": 0.75}, \"pick_two_obj_and_place\": {\"total\": 7, \"success\": 3, \"rate\": 0.429}}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T01:21:17.391Z\"}, \"v4-random-fixed-inject50-s7\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T23:58:49.123Z\", \"updated_at\": \"2026-05-16T01:06:27.238Z\", \"spec\": {\"command\": \"swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/ablation_fixed/sft_random_v4_fixed_inject50.jsonl --output_dir checkpoints/v4_random_fixed_inject50_s7 --lora_rank 16 --lora_alpha 32 --num_train_epochs 3 --per_device_train_batch_size 4 --gradient_accumulation_steps 2 --learning_rate 1e-4 --warmup_ratio 0.03 --save_strategy epoch --logging_steps 10 --seed 7 --data_seed 7 --bf16 true\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"data_path\": \"data/mini_pipeline_v4/ablation_fixed/sft_random_v4_fixed_inject50.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 7}, \"hypothesis\": \"v4 Random fixed-size ablation: 50% injection ratio seed=7 (4,358 total). Dose-response 5-seed expansion — Wave 2.\", \"metrics\": {\"train_loss\": 0.4672, \"token_acc\": 0.9156, \"train_runtime_sec\": 3832, \"memory_gib\": 29.94}, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_random_fixed_inject50_s7/v0-20260516-075756/checkpoint-1635\", \"log_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_random_fixed_inject50_s7/v0-20260516-075756/logging.jsonl\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T01:06:27.238Z\"}, \"v4-taxei-fixed-inject50-s7\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T23:58:48.153Z\", \"updated_at\": \"2026-05-16T01:06:25.547Z\", \"spec\": {\"command\": \"swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject50.jsonl --output_dir checkpoints/v4_taxei_fixed_inject50_s7 --lora_rank 16 --lora_alpha 32 --num_train_epochs 3 --per_device_train_batch_size 4 --gradient_accumulation_steps 2 --learning_rate 1e-4 --warmup_ratio 0.03 --save_strategy epoch --logging_steps 10 --seed 7 --data_seed 7 --bf16 true\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:2\", \"data_path\": \"data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject50.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 7}, \"hypothesis\": \"v4 TaxEI fixed-size ablation: 50% injection ratio seed=7 (4,358 total). Dose-response 5-seed expansion — Wave 2.\", \"metrics\": {\"train_loss\": 0.4674, \"token_acc\": 0.9189, \"train_runtime_sec\": 3834, \"memory_gib\": 29.94}, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject50_s7/v0-20260516-075754/checkpoint-1635\", \"log_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject50_s7/v0-20260516-075754/logging.jsonl\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T01:06:25.547Z\"}, \"v4-random-fixed-inject50-s1-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T23:59:00.237Z\", \"updated_at\": \"2026-05-16T01:06:21.982Z\", \"spec\": {\"command\": \"swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/ablation_fixed/sft_random_v4_fixed_inject50.jsonl --output_dir checkpoints/v4_random_fixed_inject50_s1 --lora_rank 16 --lora_alpha 32 --num_train_epochs 3 --per_device_train_batch_size 4 --gradient_accumulation_steps 2 --learning_rate 1e-4 --warmup_ratio 0.03 --save_strategy epoch --logging_steps 10 --seed 1 --data_seed 1 --bf16 true\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"data_path\": \"data/mini_pipeline_v4/ablation_fixed/sft_random_v4_fixed_inject50.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 1}, \"hypothesis\": \"v4 Random fixed-size ablation: 50% injection ratio seed=1 (4,358 total). Dose-response 5-seed expansion — Wave 2. Retry: bs=4, ga=2.\", \"metrics\": {\"train_loss\": 0.4664, \"token_acc\": 0.9012, \"train_runtime_sec\": 3928, \"memory_gib\": 30.37}, \"log_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_random_fixed_inject50_s1/v1-20260516-075754/logging.jsonl\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_random_fixed_inject50_s1/v1-20260516-075754/checkpoint-1635\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T00:03:39.204Z\"}, \"v4-taxei-fixed-inject50-s1-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T23:58:59.221Z\", \"updated_at\": \"2026-05-16T01:05:57.456Z\", \"spec\": {\"command\": \"swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject50.jsonl --output_dir checkpoints/v4_taxei_fixed_inject50_s1 --lora_rank 16 --lora_alpha 32 --num_train_epochs 3 --per_device_train_batch_size 4 --gradient_accumulation_steps 2 --learning_rate 1e-4 --warmup_ratio 0.03 --save_strategy epoch --logging_steps 10 --seed 1 --data_seed 1 --bf16 true\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"data_path\": \"data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject50.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 1}, \"hypothesis\": \"v4 TaxEI fixed-size ablation: 50% injection ratio seed=1 (4,358 total). Dose-response 5-seed expansion — Wave 2. Retry: bs=4, ga=2.\", \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject50_s1/v0-20260516-075747/checkpoint-1635\", \"log_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject50_s1/v0-20260516-075747/logging.jsonl\", \"completed_at\": \"2026-05-16T01:05:15.340Z\", \"metrics\": {\"train_loss\": 0.4667, \"token_acc\": 0.9072, \"train_runtime_sec\": 3858, \"memory_gib\": 30.37}}, \"v4-random-fixed-inject50-s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:58:26.928Z\", \"updated_at\": \"2026-05-15T23:56:49.997Z\", \"hypothesis\": \"v4 Random fixed-size ablation: 50% injection ratio seed=1 (4,358 total). Dose-response 5-seed expansion — Wave 2.\", \"spec\": {\"log_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_random_fixed_inject50_s1/train.log\", \"checkpoint_path\": \"N/A\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T23:55:00.127Z\"}, \"v4-taxei-fixed-inject50-s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:54:03.984Z\", \"updated_at\": \"2026-05-15T23:56:49.235Z\", \"hypothesis\": \"v4 TaxEI fixed-size ablation: 50% injection ratio seed=1 (4,358 total). Dose-response 5-seed expansion — Wave 2.\", \"spec\": {\"log_path\": \"/tmp/v4-taxei-fixed-inject50-s1.log\", \"checkpoint_path\": \"N/A\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T23:55:01.050Z\"}, \"v4-random-fixed-inject25-s7-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:35:00.186Z\", \"updated_at\": \"2026-05-15T23:54:59.193Z\", \"hypothesis\": \"v4 Random 25% seed=7 eval — 47 ALFWorld clean tasks. Dose-response 5-seed expansion.\", \"parent\": \"v4-random-fixed-inject25-s7\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_random_fixed_inject25_s7/v0-20260516-061742/checkpoint-1635\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-fixed-inject25-s7-eval.log\"}, \"metrics\": {\"success_rate\": 0.596, \"successes\": 28, \"total\": 47, \"by_task_type\": {\"look_at_obj_in_light\": {\"total\": 6, \"success\": 4, \"rate\": 0.667}, \"pick_and_place_simple\": {\"total\": 8, \"success\": 5, \"rate\": 0.625}, \"pick_clean_then_place_in_recep\": {\"total\": 11, \"success\": 6, \"rate\": 0.545}, \"pick_cool_then_place_in_recep\": {\"total\": 7, \"success\": 3, \"rate\": 0.429}, \"pick_heat_then_place_in_recep\": {\"total\": 8, \"success\": 6, \"rate\": 0.75}, \"pick_two_obj_and_place\": {\"total\": 7, \"success\": 4, \"rate\": 0.571}}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T23:54:59.193Z\"}, \"v4-taxei-fixed-inject25-s7-eval-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:49:33.992Z\", \"updated_at\": \"2026-05-15T23:54:58.200Z\", \"hypothesis\": \"v4 TaxEI 25% seed=7 eval (retry, cwd fix) — 47 ALFWorld clean tasks. Dose-response 5-seed expansion.\", \"parent\": \"v4-taxei-fixed-inject25-s7\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject25_s7/v0-20260516-053222/checkpoint-1635\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-fixed-inject25-s7-eval-r2.log\"}, \"metrics\": {\"success_rate\": 0.574, \"successes\": 27, \"total\": 47, \"by_task_type\": {\"look_at_obj_in_light\": {\"total\": 6, \"success\": 5, \"rate\": 0.833}, \"pick_and_place_simple\": {\"total\": 8, \"success\": 3, \"rate\": 0.375}, \"pick_clean_then_place_in_recep\": {\"total\": 11, \"success\": 5, \"rate\": 0.455}, \"pick_cool_then_place_in_recep\": {\"total\": 7, \"success\": 3, \"rate\": 0.429}, \"pick_heat_then_place_in_recep\": {\"total\": 8, \"success\": 6, \"rate\": 0.75}, \"pick_two_obj_and_place\": {\"total\": 7, \"success\": 5, \"rate\": 0.714}}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T23:54:58.200Z\"}, \"v4-random-fixed-inject25-s7\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:17:33.574Z\", \"updated_at\": \"2026-05-15T23:19:01.837Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_random_fixed_inject25_s7/v0-20260516-061742/checkpoint-1635\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-fixed-inject25-s7.log\"}, \"hypothesis\": \"v4 Random fixed-size ablation: 25% injection ratio seed=7 (4,358 total = 3,269 clean + 1,089 injected). Dose-response 5-seed expansion.\", \"reproduce\": {\"finished_at\": \"2026-05-15T23:15:25.217Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T23:15:27.886821+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.4254, \"final_step_loss\": 0.265, \"token_acc\": 0.899, \"epochs\": 3, \"steps\": 1635, \"train_runtime_sec\": 3407}, \"completed_at\": \"2026-05-15T23:19:01.837Z\"}, \"v4-recovery-paired-datagen\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:07:23.715Z\", \"updated_at\": \"2026-05-15T23:09:15.501Z\", \"hypothesis\": \"Recovery-paired injection data generation: 711 injected variants × GPT API recovery demos. Each injected trajectory gets a paired recovery continuation from the error state. For recovery-paired SFT training.\", \"metrics\": {\"total_injected_variants\": 760, \"successfully_processed\": 711, \"skipped_no_source_match\": 49, \"operators\": {\"C1_ContextTruncation\": 182, \"C4_ObservationMasking\": 175, \"P1_StepOrderSwap\": 170, \"P2_SubGoalDeletion\": 184}, \"recovery_steps_mean\": 7.6, \"recovery_steps_min\": 1, \"recovery_steps_max\": 46, \"total_recovery_api_calls\": 5408, \"output_file\": \"/root/autodl-tmp/tax_error_inject_agent/data/recovery_paired/recovery_paired.jsonl\", \"output_lines\": 711, \"output_size_mb\": 20.8, \"log_file\": \"/root/autodl-tmp/tax_error_inject_agent/logs/recovery_paired_gen.log\"}, \"spec\": {\"command\": \"python scripts/generate_recovery_paired.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/tax_error_inject_agent/data/mini_pipeline_v2/injected_variants.jsonl\", \"data_count\": 760, \"model_name\": \"gpt-4o\", \"seed\": 42}, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/data/recovery_paired/recovery_paired.jsonl\", \"log_path\": \"/root/autodl-tmp/tax_error_inject_agent/logs/recovery_paired_gen.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T23:09:15.501Z\"}, \"v4-taxei-fixed-inject25-s1-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:34:57.410Z\", \"updated_at\": \"2026-05-15T22:55:45.780Z\", \"hypothesis\": \"v4 TaxEI 25% seed=1 eval — 47 ALFWorld clean tasks. Dose-response 5-seed expansion.\", \"parent\": \"v4-taxei-fixed-inject25-s1\", \"spec\": {\"checkpoint_path\": \"checkpoints/v4_taxei_fixed_inject25_s1/v0-20260516-052917/checkpoint-1635\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-fixed-inject25-s1-eval.log\"}, \"metrics\": {\"success_rate\": 0.638, \"successes\": 30, \"total\": 47, \"eval_split\": \"valid_unseen\", \"by_task_type\": {\"look_at_obj_in_light\": {\"total\": 6, \"success\": 4, \"rate\": 0.667}, \"pick_and_place_simple\": {\"total\": 8, \"success\": 5, \"rate\": 0.625}, \"pick_clean_then_place_in_recep\": {\"total\": 11, \"success\": 6, \"rate\": 0.545}, \"pick_cool_then_place_in_recep\": {\"total\": 7, \"success\": 3, \"rate\": 0.429}, \"pick_heat_then_place_in_recep\": {\"total\": 8, \"success\": 6, \"rate\": 0.75}, \"pick_two_obj_and_place\": {\"total\": 7, \"success\": 6, \"rate\": 0.857}}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T22:55:45.780Z\"}, \"v4-random-fixed-inject25-s1-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:34:59.280Z\", \"updated_at\": \"2026-05-15T22:51:47.662Z\", \"hypothesis\": \"v4 Random 25% seed=1 eval — 47 ALFWorld clean tasks. Dose-response 5-seed expansion.\", \"parent\": \"v4-random-fixed-inject25-s1\", \"spec\": {\"checkpoint_path\": \"checkpoints/v4_random_fixed_inject25_s1/v0-20260516-053219/checkpoint-1635\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-fixed-inject25-s1-eval.log\"}, \"metrics\": {\"success_rate\": 0.723, \"successes\": 34, \"total\": 47, \"by_task_type\": {\"look_at_obj_in_light\": {\"total\": 6, \"success\": 5, \"rate\": 0.833}, \"pick_and_place_simple\": {\"total\": 8, \"success\": 5, \"rate\": 0.625}, \"pick_clean_then_place_in_recep\": {\"total\": 11, \"success\": 7, \"rate\": 0.636}, \"pick_cool_then_place_in_recep\": {\"total\": 7, \"success\": 4, \"rate\": 0.571}, \"pick_heat_then_place_in_recep\": {\"total\": 8, \"success\": 7, \"rate\": 0.875}, \"pick_two_obj_and_place\": {\"total\": 7, \"success\": 6, \"rate\": 0.857}}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T22:51:47.662Z\"}, \"v4-taxei-fixed-inject25-s7-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:34:58.385Z\", \"updated_at\": \"2026-05-15T22:49:15.451Z\", \"hypothesis\": \"v4 TaxEI 25% seed=7 eval — 47 ALFWorld clean tasks. Dose-response 5-seed expansion.\", \"parent\": \"v4-taxei-fixed-inject25-s7\", \"spec\": {\"command\": \"python3 eval/recovery.py --model_path checkpoints/v4_taxei_fixed_inject25_s7/v0-20260516-053222/checkpoint-1635 --num_episodes 47 --seed 42\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"unknown\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-fixed-inject25-s7-eval.log\", \"submitted_at\": \"2026-05-15T22:45:20.960Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"eval/eval_tasks_47.json\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (taxei fixed inject25 s7)\", \"seed\": 42, \"checkpoint_source\": \"v4-taxei-fixed-inject25-s7\", \"eval_data\": \"eval_tasks_47.json\", \"wall_clock_seconds\": 67.9, \"gpu_hours\": 0.02}, \"reproduce\": {\"finished_at\": \"2026-05-15T22:46:27.057Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T22:46:28.849Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T22:46:31.066271+00:00\"}]}, \"notes\": \"失败原因: cd /root/tax_error_inject_agent 路径不存在，正确路径为 /root/autodl-tmp/tax_error_inject_agent | 已有成果: 无（启动即失败） | 建议: 修正 cwd 后重试为 v4-taxei-fixed-inject25-s7-eval-r2，等当前 2 个 eval 完成后提交（eval 并行 ≤ 2）\"}, \"v4-taxei-fixed-inject25-s1-eval-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:38:37.902Z\", \"updated_at\": \"2026-05-15T22:45:10.397Z\", \"spec\": {\"command\": \"python3 eval/recovery.py --model_path checkpoints/v4_taxei_fixed_inject25_s1/v0-20260516-052917/checkpoint-1635 --num_episodes 47 --seed 42\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"205858\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-fixed-inject25-s1-eval-r2.log\", \"submitted_at\": \"2026-05-15T22:38:37.371Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"eval/eval_tasks_47.json\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (taxei fixed inject25 s1)\", \"seed\": 42, \"checkpoint_source\": \"v4-taxei-fixed-inject25-s1\", \"eval_data\": \"eval_tasks_47.json\", \"wall_clock_seconds\": 393.0, \"gpu_hours\": 0.11}, \"hypothesis\": \"v4 TaxEI 25% seed=1 eval — 47 ALFWorld clean tasks. Dose-response 5-seed expansion.\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T22:45:10.397Z\"}, \"v4-taxei-fixed-inject25-s123-eval\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T09:21:06.936Z\", \"updated_at\": \"2026-05-15T22:37:36.286Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && python3 eval/recovery.py --model_path /root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject25_s123/v0-20260515-153732/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_taxei_fixed_inject25_s123_eval.json --device cuda:0\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"132743\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-fixed-inject25-s123-eval.log\", \"submitted_at\": \"2026-05-15T09:21:06.806Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"metrics\": {\"eval_success_rate\": 0.468, \"eval_successes\": 22, \"eval_total\": 47}}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.468, \"successes\": 22, \"total\": 47, \"by_task_type\": {\"look_at_obj_in_light\": {\"total\": 6, \"success\": 4, \"rate\": 0.667}, \"pick_and_place_simple\": {\"total\": 8, \"success\": 3, \"rate\": 0.375}, \"pick_clean_then_place_in_recep\": {\"total\": 11, \"success\": 5, \"rate\": 0.455}, \"pick_cool_then_place_in_recep\": {\"total\": 7, \"success\": 1, \"rate\": 0.143}, \"pick_heat_then_place_in_recep\": {\"total\": 8, \"success\": 6, \"rate\": 0.75}, \"pick_two_obj_and_place\": {\"total\": 7, \"success\": 3, \"rate\": 0.429}}}}, \"v4-taxei-fixed-inject25-s0-eval\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T09:21:04.275Z\", \"updated_at\": \"2026-05-15T22:37:34.634Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && python3 eval/recovery.py --model_path /root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject25_s0/v0-20260515-153729/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_taxei_fixed_inject25_s0_eval.json --device cuda:0\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"132601\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-fixed-inject25-s0-eval.log\", \"submitted_at\": \"2026-05-15T09:21:04.135Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"metrics\": {\"eval_success_rate\": 0.468, \"eval_successes\": 22, \"eval_total\": 47}}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.468, \"successes\": 22, \"total\": 47, \"by_task_type\": {\"look_at_obj_in_light\": {\"total\": 6, \"success\": 4, \"rate\": 0.667}, \"pick_and_place_simple\": {\"total\": 8, \"success\": 2, \"rate\": 0.25}, \"pick_clean_then_place_in_recep\": {\"total\": 11, \"success\": 5, \"rate\": 0.455}, \"pick_cool_then_place_in_recep\": {\"total\": 7, \"success\": 2, \"rate\": 0.286}, \"pick_heat_then_place_in_recep\": {\"total\": 8, \"success\": 6, \"rate\": 0.75}, \"pick_two_obj_and_place\": {\"total\": 7, \"success\": 3, \"rate\": 0.429}}}}, \"v4-random-fixed-inject25-s0\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:37:03.696Z\", \"updated_at\": \"2026-05-15T22:33:48.130Z\", \"hypothesis\": \"D022 multi-seed dose-response: Random 25% injection, seed=0 (fixed 4,358 total). 对标 seed=42 的 55.3%。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/ablation_fixed/sft_random_v4_fixed_inject25.jsonl --lora_rank 16 --num_train_epochs 3 --seed 0 --output_dir checkpoints/v4_random_fixed_inject25_s0 --gradient_accumulation_steps 8 --learning_rate 1e-4 --lr_scheduler_type cosine --gradient_checkpointing true --save_strategy epoch --logging_steps 5 --weight_decay 0.1 --adam_beta1 0.9 --adam_beta2 0.95\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"134514\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-fixed-inject25-s0.log\", \"submitted_at\": \"2026-05-15T09:31:12.733Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"success\"}, \"v4-taxei-fixed-inject25-s123\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:37:00.336Z\", \"updated_at\": \"2026-05-15T22:33:47.230Z\", \"hypothesis\": \"D022 multi-seed dose-response: TaxEI 25% injection, seed=123 (fixed 4,358 total). 对标 seed=42 的 48.9%。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject25.jsonl --lora_rank 16 --num_train_epochs 3 --seed 123 --output_dir checkpoints/v4_taxei_fixed_inject25_s123 --gradient_accumulation_steps 8 --learning_rate 1e-4 --lr_scheduler_type cosine --gradient_checkpointing true --save_strategy epoch --logging_steps 5 --weight_decay 0.1 --adam_beta1 0.9 --adam_beta2 0.95\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"126954\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-fixed-inject25-s123.log\", \"submitted_at\": \"2026-05-15T07:37:23.453Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.4253, \"train_duration_min\": 55.9, \"train_steps\": 1635, \"train_epochs\": 3, \"data_count\": 4358}}, \"v4-taxei-fixed-inject25-s0\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:36:58.951Z\", \"updated_at\": \"2026-05-15T22:33:46.312Z\", \"hypothesis\": \"D022 multi-seed dose-response: TaxEI 25% injection, seed=0 (fixed 4,358 total). 对标 seed=42 的 48.9%。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject25.jsonl --lora_rank 16 --num_train_epochs 3 --seed 0 --output_dir checkpoints/v4_taxei_fixed_inject25_s0 --gradient_accumulation_steps 8 --learning_rate 1e-4 --lr_scheduler_type cosine --gradient_checkpointing true --save_strategy epoch --logging_steps 5 --weight_decay 0.1 --adam_beta1 0.9 --adam_beta2 0.95\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"126876\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-fixed-inject25-s0.log\", \"submitted_at\": \"2026-05-15T07:37:20.823Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.4258, \"train_duration_min\": 56.1, \"train_steps\": 1635, \"train_epochs\": 3, \"data_count\": 4358}}, \"v4-taxei-fixed-inject25-s7\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T21:32:12.446Z\", \"updated_at\": \"2026-05-15T22:33:00.087Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject25_s7/v0-20260516-053222/checkpoint-1635\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-fixed-inject25-s7.log\"}, \"hypothesis\": \"v4 TaxEI fixed-size ablation: 25% injection ratio seed=7 (4,358 total = 3,269 clean + 1,089 injected). Dose-response 5-seed expansion.\", \"reproduce\": {\"finished_at\": \"2026-05-15T22:30:32.348Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T22:30:36.683523+00:00\"}]}, \"metrics\": {\"train_loss\": 0.4242, \"final_step_loss\": 0.2571, \"token_accuracy\": 0.904, \"train_steps\": 1635, \"train_epochs\": 3, \"train_runtime_sec\": 3430.48, \"train_duration_min\": 57.17, \"train_samples_per_second\": 3.811, \"train_steps_per_second\": 0.477, \"memory_gib\": 17.55, \"data_count\": 4358}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T22:32:54.528Z\"}, \"v4-random-fixed-inject25-s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T21:32:10.005Z\", \"updated_at\": \"2026-05-15T22:32:58.843Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_random_fixed_inject25_s1/v0-20260516-053219/checkpoint-1635\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-fixed-inject25-s1.log\"}, \"hypothesis\": \"v4 Random fixed-size ablation: 25% injection ratio seed=1 (4,358 total = 3,269 clean + 1,089 injected). Dose-response 5-seed expansion.\", \"reproduce\": {\"finished_at\": \"2026-05-15T22:30:26.273Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T22:30:28.937887+00:00\"}]}, \"metrics\": {\"train_loss\": 0.4261, \"final_step_loss\": 0.2442, \"token_accuracy\": 0.9123, \"train_steps\": 1635, \"train_epochs\": 3, \"train_runtime_sec\": 3417.56, \"train_duration_min\": 56.96, \"train_samples_per_second\": 3.826, \"train_steps_per_second\": 0.478, \"memory_gib\": 18, \"data_count\": 4358}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T22:32:56.713Z\"}, \"v4-taxei-fixed-inject25-s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T21:29:07.506Z\", \"updated_at\": \"2026-05-15T22:29:56.310Z\", \"spec\": {\"command\": \"swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject25.jsonl --lora_rank 16 --num_train_epochs 3 --seed 1 --data_seed 1 --output_dir checkpoints/v4_taxei_fixed_inject25_s1 --gradient_accumulation_steps 8 --learning_rate 1e-4 --lr_scheduler_type cosine --gradient_checkpointing true --save_strategy epoch --logging_steps 5 --weight_decay 0.1 --adam_beta1 0.9 --adam_beta2 0.95\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"199599\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-fixed-inject25-s1.log\", \"submitted_at\": \"2026-05-15T21:29:07.235Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject25.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 1, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject25_s1/v0-20260516-052917/checkpoint-1635\", \"wall_clock_seconds\": 3649.1, \"gpu_hours\": 1.01}, \"hypothesis\": \"v4 TaxEI fixed-size ablation: 25% injection ratio seed=1 (4,358 total = 3,269 clean + 1,089 injected). Dose-response 5-seed expansion.\", \"reproduce\": {\"finished_at\": \"2026-05-15T22:27:46.845Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T22:27:49.896536+00:00\"}]}, \"metrics\": {\"train_loss\": 0.4243, \"train_duration_min\": 57.5, \"train_steps\": 1635, \"train_epochs\": 3, \"data_count\": 4358}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T22:29:56.310Z\"}, \"v4-random-fixed-inject10-s7-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T21:57:41.705Z\", \"updated_at\": \"2026-05-15T22:15:41.386Z\", \"spec\": {\"command\": \"python3 eval/recovery.py --model_path checkpoints/v4_random_fixed_inject10_s7/v1-20260516-045440/checkpoint-1635 --num_episodes 47 --seed 42\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"202328\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-fixed-inject10-s7-eval.log\", \"submitted_at\": \"2026-05-15T21:57:41.444Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"eval/eval_tasks_47.json\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (random fixed inject10 s7)\", \"seed\": 42, \"checkpoint_source\": \"v4-random-fixed-inject10-s7\", \"eval_data\": \"eval_tasks_47.json\", \"checkpoint_path\": \"checkpoints/v4_random_fixed_inject10_s7/v1-20260516-045440/checkpoint-1635\", \"wall_clock_seconds\": 818, \"gpu_hours\": 0.23}, \"hypothesis\": \"v4 Random 10% seed=7 eval — 47 ALFWorld clean tasks. Dose-response 5-seed expansion. 最后一个 10% eval。\", \"reproduce\": {\"finished_at\": \"2026-05-15T22:12:57.609Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T22:12:59.982752+00:00\"}]}, \"metrics\": {\"success_rate\": 0.617, \"successes\": 29, \"total\": 47, \"by_task_type\": {\"look_at_obj_in_light\": {\"success\": 5, \"total\": 6, \"rate\": 0.833}, \"pick_and_place_simple\": {\"success\": 4, \"total\": 8, \"rate\": 0.5}, \"pick_clean_then_place_in_recep\": {\"success\": 5, \"total\": 11, \"rate\": 0.455}, \"pick_cool_then_place_in_recep\": {\"success\": 4, \"total\": 7, \"rate\": 0.571}, \"pick_heat_then_place_in_recep\": {\"success\": 7, \"total\": 8, \"rate\": 0.875}, \"pick_two_obj_and_place\": {\"success\": 4, \"total\": 7, \"rate\": 0.571}}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T22:15:41.386Z\"}, \"v4-random-fixed-inject10-s7\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:57:08.353Z\", \"updated_at\": \"2026-05-15T21:57:11.016Z\", \"hypothesis\": \"v4 Random fixed-size ablation: 10% injection ratio seed=7 (4,358 total). Dose-response 5-seed expansion — 最后一个 10% 训练。\", \"spec\": {\"data_path\": \"data/mini_pipeline_v4/ablation_fixed/sft_random_v4_fixed_inject10.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B + LoRA (random fixed inject10 s7)\", \"seed\": 7}, \"reproduce\": {\"finished_at\": \"2026-05-15T21:54:51.217Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T21:54:53.698171+00:00\"}]}, \"metrics\": {\"final_loss\": 0.2352, \"train_loss_avg\": 0.4209, \"final_token_acc\": 0.9066, \"total_steps\": 1635, \"epochs\": 3, \"train_runtime_sec\": 3511.93, \"memory_gib\": 18.15, \"train_speed_s_per_it\": 2.148}, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_random_fixed_inject10_s7/v1-20260516-045440/checkpoint-1635\", \"conclusion\": \"success\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-fixed-inject10-s7.log\", \"completed_at\": \"2026-05-15T21:57:11.016Z\"}, \"v4-random-fixed-inject10-s1-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T21:05:18.654Z\", \"updated_at\": \"2026-05-15T21:27:48.360Z\", \"spec\": {\"command\": \"python3 eval/recovery.py --model_path checkpoints/v4_random_fixed_inject10_s1/v1-20260516-040130/checkpoint-1635 --num_episodes 47 --seed 42\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"198045\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-fixed-inject10-s1-eval.log\", \"submitted_at\": \"2026-05-15T21:05:18.393Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"eval/eval_tasks_47.json\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (random fixed inject10 s1)\", \"seed\": 42, \"checkpoint_source\": \"v4-random-fixed-inject10-s1\", \"eval_data\": \"eval_tasks_47.json\", \"checkpoint_path\": \"checkpoints/v4_random_fixed_inject10_s1/v1-20260516-040130/checkpoint-1635\", \"wall_clock_seconds\": 1350.0, \"gpu_hours\": 0.37}, \"hypothesis\": \"v4 Random 10% seed=1 eval — 47 ALFWorld clean tasks. Dose-response 5-seed expansion.\", \"reproduce\": {\"finished_at\": \"2026-05-15T21:25:33.786Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T21:25:36.468478+00:00\"}]}, \"metrics\": {\"success_rate\": 0.681, \"successes\": 32, \"total\": 47, \"by_task_type\": {\"look_at_obj_in_light\": {\"total\": 6, \"success\": 5, \"rate\": 0.833}, \"pick_and_place_simple\": {\"total\": 8, \"success\": 5, \"rate\": 0.625}, \"pick_clean_then_place_in_recep\": {\"total\": 10, \"success\": 5, \"rate\": 0.5}, \"pick_cool_then_place_in_recep\": {\"total\": 7, \"success\": 6, \"rate\": 0.857}, \"pick_heat_then_place_in_recep\": {\"total\": 8, \"success\": 7, \"rate\": 0.875}, \"pick_two_obj_and_place\": {\"total\": 7, \"success\": 4, \"rate\": 0.571}}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T21:27:48.360Z\"}, \"v4-taxei-fixed-inject10-s7-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T21:02:22.234Z\", \"updated_at\": \"2026-05-15T21:27:44.185Z\", \"spec\": {\"command\": \"python3 eval/recovery.py --model_path checkpoints/v4_taxei_fixed_inject10_s7/v1-20260516-040128/checkpoint-1635 --num_episodes 47 --seed 42\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"197555\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-fixed-inject10-s7-eval.log\", \"submitted_at\": \"2026-05-15T21:02:21.785Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"eval/eval_tasks_47.json\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (taxei fixed inject10 s7)\", \"seed\": 42, \"checkpoint_source\": \"v4-taxei-fixed-inject10-s7\", \"eval_data\": \"eval_tasks_47.json\", \"wall_clock_seconds\": 1522.4, \"gpu_hours\": 0.42}, \"hypothesis\": \"v4 TaxEI 10% seed=7 eval — 47 ALFWorld clean tasks. Dose-response 5-seed expansion.\", \"reproduce\": {\"finished_at\": \"2026-05-15T21:19:30.996Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T21:19:33.518373+00:00\"}]}, \"metrics\": {\"success_rate\": 0.681, \"successes\": 32, \"total\": 47, \"by_task_type\": {\"look_at_obj_in_light\": {\"total\": 6, \"success\": 5, \"rate\": 0.833}, \"pick_and_place_simple\": {\"total\": 8, \"success\": 5, \"rate\": 0.625}, \"pick_clean_then_place_in_recep\": {\"total\": 11, \"success\": 7, \"rate\": 0.636}, \"pick_cool_then_place_in_recep\": {\"total\": 7, \"success\": 4, \"rate\": 0.571}, \"pick_heat_then_place_in_recep\": {\"total\": 8, \"success\": 7, \"rate\": 0.875}, \"pick_two_obj_and_place\": {\"total\": 7, \"success\": 4, \"rate\": 0.571}}}, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_taxei_fixed_inject10_s7_eval.json\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T21:27:44.185Z\"}, \"v4-taxei-fixed-inject10-s1-eval-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:54:05.248Z\", \"updated_at\": \"2026-05-15T21:06:11.418Z\", \"spec\": {\"parent\": \"v4-taxei-fixed-inject10-s1\", \"checkpoint_source\": \"v4-taxei-fixed-inject10-s1\", \"eval_data\": \"eval_tasks_47.json\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (taxei fixed inject10 s1)\", \"seed\": 42, \"data_path\": \"eval/eval_tasks_47.json\"}, \"hypothesis\": \"v4 TaxEI 10% seed=1 eval (r2, dedicated GPU) — 47 ALFWorld clean tasks.\", \"reproduce\": {\"finished_at\": \"2026-05-15T21:04:33.190Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T21:04:36.432028+00:00\"}]}, \"metrics\": {\"success_rate\": 0.511, \"successes\": 24, \"total\": 47, \"by_task_type\": {\"look_at_obj_in_light\": {\"total\": 6, \"success\": 4, \"rate\": 0.667}, \"pick_and_place_simple\": {\"total\": 8, \"success\": 4, \"rate\": 0.5}, \"pick_clean_then_place_in_recep\": {\"total\": 11, \"success\": 5, \"rate\": 0.455}, \"pick_cool_then_place_in_recep\": {\"total\": 7, \"success\": 2, \"rate\": 0.286}, \"pick_heat_then_place_in_recep\": {\"total\": 8, \"success\": 6, \"rate\": 0.75}, \"pick_two_obj_and_place\": {\"total\": 7, \"success\": 3, \"rate\": 0.429}}}, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_taxei_fixed_inject10_s1_eval.json\", \"log_path\": \"/root/runs/tax_error_inject_agent/v4-taxei-fixed-inject10-s1-eval-r2.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T21:06:11.418Z\"}, \"v4-taxei-fixed-inject10-s7\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:57:05.524Z\", \"updated_at\": \"2026-05-15T21:05:01.494Z\", \"hypothesis\": \"v4 TaxEI fixed-size ablation: 10% injection ratio seed=7 (4,358 total). Dose-response 5-seed expansion.\", \"spec\": {\"command\": \"swift sft --model Qwen3-8B --dataset sft_taxei_v4_fixed_inject10.jsonl --seed 7\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"191997\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-fixed-inject10-s7.log\", \"submitted_at\": \"2026-05-15T20:01:19.314Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject10.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 7, \"wall_clock_seconds\": 3683.3, \"gpu_hours\": 1.02}, \"reproduce\": {\"finished_at\": \"2026-05-15T20:59:13.748Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T20:59:16.071667+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject10_s7/v1-20260516-040128/checkpoint-1635\", \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.237, \"train_loss_avg\": 0.4212, \"final_token_acc\": 0.905, \"total_steps\": 1635, \"epochs\": 3, \"train_runtime_sec\": 3437, \"memory_gib\": 18.15, \"train_speed_s_per_it\": 2.102}, \"completed_at\": \"2026-05-15T21:02:42.621Z\"}, \"v4-random-fixed-inject10-s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:57:07.390Z\", \"updated_at\": \"2026-05-15T21:04:23.738Z\", \"hypothesis\": \"v4 Random fixed-size ablation: 10% injection ratio seed=1 (4,358 total). Dose-response 5-seed expansion.\", \"spec\": {\"command\": \"swift sft --model Qwen3-8B --dataset sft_random_v4_fixed_inject10.jsonl --seed 1\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"192077\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-fixed-inject10-s1.log\", \"submitted_at\": \"2026-05-15T20:01:21.468Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/mini_pipeline_v4/ablation_fixed/sft_random_v4_fixed_inject10.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 1, \"wall_clock_seconds\": 3782.3, \"gpu_hours\": 1.05}, \"reproduce\": {\"finished_at\": \"2026-05-15T21:01:51.221Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T21:01:53.909162+00:00\"}]}, \"metrics\": {\"final_loss\": 0.3096, \"train_loss_avg\": 0.4238, \"final_token_acc\": 0.8902, \"total_steps\": 1635, \"epochs\": 3, \"train_runtime_sec\": 3488, \"memory_gib\": 18.13, \"train_speed_s_per_it\": 2.132}, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_random_fixed_inject10_s1/v1-20260516-040130/checkpoint-1635\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T21:04:23.738Z\"}, \"v4-taxei-fixed-inject10-s123-eval-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:40:05.773Z\", \"updated_at\": \"2026-05-15T20:54:14.378Z\", \"spec\": {\"command\": \"python3 eval/recovery.py --model_path checkpoints/v4_taxei_fixed_inject10_s123/v0-20260516-014833/checkpoint-1635 --num_episodes 47 --seed 42\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"194978\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-fixed-inject10-s123-eval-r3.log\", \"submitted_at\": \"2026-05-15T20:40:05.519Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"parent\": \"v4-taxei-fixed-inject10-s123\", \"checkpoint_source\": \"v4-taxei-fixed-inject10-s123\", \"eval_data\": \"eval_tasks_47.json\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (taxei fixed inject10 s123)\", \"seed\": 42, \"data_path\": \"eval/eval_tasks_47.json\", \"wall_clock_seconds\": 848.9, \"gpu_hours\": 0.24}, \"hypothesis\": \"v4 TaxEI 10% seed=123 eval (r3, dedicated GPU) — 47 ALFWorld clean tasks.\", \"reproduce\": {\"finished_at\": \"2026-05-15T20:50:16.884Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T20:50:19.215245+00:00\"}]}, \"metrics\": {\"success_rate\": 0.553, \"successes\": 26, \"total\": 47, \"by_task_type\": {\"look_at_obj_in_light\": {\"total\": 6, \"success\": 5, \"rate\": 0.833}, \"pick_and_place_simple\": {\"total\": 8, \"success\": 4, \"rate\": 0.5}, \"pick_clean_then_place_in_recep\": {\"total\": 11, \"success\": 5, \"rate\": 0.455}, \"pick_cool_then_place_in_recep\": {\"total\": 7, \"success\": 2, \"rate\": 0.286}, \"pick_heat_then_place_in_recep\": {\"total\": 8, \"success\": 6, \"rate\": 0.75}, \"pick_two_obj_and_place\": {\"total\": 7, \"success\": 4, \"rate\": 0.571}}}, \"conclusion\": \"success\", \"checkpoint_path\": \"checkpoints/v4_taxei_fixed_inject10_s123/v0-20260516-014833/checkpoint-1635\", \"completed_at\": \"2026-05-15T20:54:14.378Z\"}, \"v4-random-fixed-inject10-s0-eval-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:40:07.402Z\", \"updated_at\": \"2026-05-15T20:52:32.204Z\", \"spec\": {\"command\": \"python3 eval/recovery.py --model_path checkpoints/v4_random_fixed_inject10_s0/v0-20260516-014835/checkpoint-1635 --num_episodes 47 --seed 42\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"195118\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-fixed-inject10-s0-eval-r3.log\", \"submitted_at\": \"2026-05-15T20:40:07.156Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"parent\": \"v4-random-fixed-inject10-s0\", \"checkpoint_source\": \"v4-random-fixed-inject10-s0\", \"eval_data\": \"eval_tasks_47.json\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (random fixed inject10 s0)\", \"seed\": 42, \"data_path\": \"eval/eval_tasks_47.json\", \"wall_clock_seconds\": 745.0, \"gpu_hours\": 0.21}, \"hypothesis\": \"v4 Random 10% seed=0 eval (r3, dedicated GPU) — 47 ALFWorld clean tasks.\", \"reproduce\": {\"finished_at\": \"2026-05-15T20:50:22.439Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T20:50:26.585713+00:00\"}]}, \"metrics\": {\"success_rate\": 0.66, \"successes\": 31, \"total\": 47, \"by_task_type\": {\"look_at_obj_in_light\": {\"success\": 5, \"total\": 6, \"rate\": 0.833}, \"pick_and_place_simple\": {\"success\": 4, \"total\": 8, \"rate\": 0.5}, \"pick_clean_then_place_in_recep\": {\"success\": 7, \"total\": 11, \"rate\": 0.636}, \"pick_cool_then_place_in_recep\": {\"success\": 4, \"total\": 7, \"rate\": 0.571}, \"pick_heat_then_place_in_recep\": {\"success\": 7, \"total\": 8, \"rate\": 0.875}, \"pick_two_obj_and_place\": {\"success\": 4, \"total\": 7, \"rate\": 0.571}}}, \"conclusion\": \"success\", \"checkpoint_path\": \"checkpoints/v4_random_fixed_inject10_s0/v0-20260516-014835/checkpoint-1635\", \"completed_at\": \"2026-05-15T20:52:32.204Z\"}, \"v4-random-fixed-inject10-s0-eval-r2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:05:35.682Z\", \"updated_at\": \"2026-05-15T20:05:48.855Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && python3 eval/recovery.py --model_path checkpoints/v4_random_fixed_inject10_s0/v0-20260516-014835/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --task_list eval/eval_tasks_47.json --num_episodes 47 --seed 42 --device cuda:0 --output eval_results/v4_random_fixed_inject10_s0_eval.json\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"193145\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-fixed-inject10-s0-eval-r2.log\", \"submitted_at\": \"2026-05-15T20:05:35.429Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"parent\": \"v4-random-fixed-inject10-s0\", \"checkpoint_source\": \"v4-random-fixed-inject10-s0\", \"eval_data\": \"eval_tasks_47.json\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (random fixed inject10 s0)\", \"seed\": 42}, \"hypothesis\": \"v4 Random 10% seed=0 eval (retry, OOM fix) — 47 ALFWorld clean tasks. Dedicated GPU.\"}, \"v4-taxei-fixed-inject10-s123-eval-r2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:05:34.132Z\", \"updated_at\": \"2026-05-15T20:05:47.199Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && python3 eval/recovery.py --model_path checkpoints/v4_taxei_fixed_inject10_s123/v0-20260516-014833/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --task_list eval/eval_tasks_47.json --num_episodes 47 --seed 42 --device cuda:0 --output eval_results/v4_taxei_fixed_inject10_s123_eval.json\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"193003\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-fixed-inject10-s123-eval-r2.log\", \"submitted_at\": \"2026-05-15T20:05:33.887Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"parent\": \"v4-taxei-fixed-inject10-s123\", \"checkpoint_source\": \"v4-taxei-fixed-inject10-s123\", \"eval_data\": \"eval_tasks_47.json\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (taxei fixed inject10 s123)\", \"seed\": 42}, \"hypothesis\": \"v4 TaxEI 10% seed=123 eval (retry, OOM fix) — 47 ALFWorld clean tasks. Dedicated GPU.\"}, \"v4-random-fixed-inject10-s0-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:57:43.603Z\", \"updated_at\": \"2026-05-15T20:04:12.753Z\", \"spec\": {\"command\": \"eval\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"188022\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-fixed-inject10-s0-eval.log\", \"submitted_at\": \"2026-05-15T18:57:43.056Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"parent\": \"v4-random-fixed-inject10-s0\", \"checkpoint_source\": \"v4-random-fixed-inject10-s0\", \"eval_data\": \"valid_unseen\", \"data_count\": 47, \"data_path\": \"N/A\", \"model_name\": \"v4_random_fixed_inject10_s0\", \"seed\": 0, \"wall_clock_seconds\": 3975.6, \"gpu_hours\": 1.1}, \"hypothesis\": \"v4 Random 10% seed=0 eval — 47 ALFWorld clean tasks. Dose-response 5-seed expansion.\", \"conclusion\": \"failed\", \"checkpoint_path\": \"N/A-OOM\", \"completed_at\": \"2026-05-15T20:03:58.662Z\", \"metrics\": {\"error\": \"CUDA OOM during model loading on GPU 0\"}}, \"v4-taxei-fixed-inject10-s123-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:57:41.337Z\", \"updated_at\": \"2026-05-15T20:04:11.865Z\", \"spec\": {\"command\": \"eval\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"187785\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-fixed-inject10-s123-eval.log\", \"submitted_at\": \"2026-05-15T18:57:40.646Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"parent\": \"v4-taxei-fixed-inject10-s123\", \"checkpoint_source\": \"v4-taxei-fixed-inject10-s123\", \"eval_data\": \"valid_unseen\", \"data_count\": 47, \"data_path\": \"N/A\", \"model_name\": \"v4_taxei_fixed_inject10_s123\", \"seed\": 123, \"wall_clock_seconds\": 3977.2, \"gpu_hours\": 1.1}, \"hypothesis\": \"v4 TaxEI 10% seed=123 eval — 47 ALFWorld clean tasks. Dose-response 5-seed expansion.\", \"conclusion\": \"failed\", \"checkpoint_path\": \"N/A-OOM\", \"completed_at\": \"2026-05-15T20:03:57.889Z\", \"metrics\": {\"error\": \"CUDA OOM during model loading on GPU 0\"}}, \"v4-taxei-fixed-inject10-s1-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:57:45.002Z\", \"updated_at\": \"2026-05-15T20:04:10.985Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && python3 eval/recovery.py --model_path /root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject10_s1/v0-20260516-015427/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --task_list eval/eval_tasks_47.json --num_episodes 47 --seed 42 --device cuda:0 --output eval_results/v4_taxei_fixed_inject10_s1_eval.json\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"188906\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-fixed-inject10-s1-eval.log\", \"submitted_at\": \"2026-05-15T18:57:44.756Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"parent\": \"v4-taxei-fixed-inject10-s1\", \"checkpoint_source\": \"v4-taxei-fixed-inject10-s1\", \"eval_data\": \"eval_tasks_47.json\", \"data_count\": 47, \"data_path\": \"eval/eval_tasks_47.json\", \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"wall_clock_seconds\": 3927.9, \"gpu_hours\": 1.09}, \"hypothesis\": \"v4 TaxEI 10% seed=1 eval — 47 ALFWorld clean tasks. Dose-response 5-seed expansion.\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T20:03:12.659Z\", \"metrics\": {\"error\": \"CUDA OOM during model loading on GPU 0\"}}, \"v4-random-fixed-inject10-s123-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:59:20.398Z\", \"updated_at\": \"2026-05-15T20:04:09.526Z\", \"hypothesis\": \"v4 Random fixed-size 10% injection seed=123 eval — 47 ALFWorld tasks, dose-response 5-seed expansion\", \"parent\": \"v4-random-fixed-inject10-s123\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && python3 eval/recovery.py --model_path checkpoints/v4_random_fixed_inject10_s123/v0-20260516-015429/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --task_list eval/eval_tasks_47.json --num_episodes 47 --seed 42 --device cuda:0 --output eval_results/v4_random_fixed_inject10_s123_eval.json\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"data_path\": \"eval/eval_tasks_47.json\", \"data_count\": 47, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_source\": \"v4-random-fixed-inject10-s123\", \"eval_data\": \"eval/eval_tasks_47.json\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-fixed-inject10-s123-eval.log\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_random_fixed_inject10_s123_eval.json\", \"completed_at\": \"2026-05-15T20:03:32.060Z\", \"metrics\": {\"success_rate\": 0.553, \"successes\": 26, \"total\": 47, \"by_task_type\": {\"look_at_obj_in_light\": {\"total\": 6, \"success\": 5, \"rate\": 0.833}, \"pick_and_place_simple\": {\"total\": 8, \"success\": 5, \"rate\": 0.625}, \"pick_clean_then_place_in_recep\": {\"total\": 11, \"success\": 5, \"rate\": 0.455}, \"pick_cool_then_place_in_recep\": {\"total\": 7, \"success\": 2, \"rate\": 0.286}, \"pick_heat_then_place_in_recep\": {\"total\": 8, \"success\": 6, \"rate\": 0.75}, \"pick_two_obj_and_place\": {\"total\": 7, \"success\": 3, \"rate\": 0.429}}}}, \"v4-taxei-fixed-inject10-s0-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:57:46.985Z\", \"updated_at\": \"2026-05-15T20:04:06.775Z\", \"spec\": {\"command\": \"eval\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"188410\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-fixed-inject10-s0-eval.log\", \"submitted_at\": \"2026-05-15T18:57:46.725Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"parent\": \"v4-taxei-fixed-inject10-s0\", \"checkpoint_source\": \"v4-taxei-fixed-inject10-s0\", \"eval_data\": \"valid_unseen\", \"data_count\": 47, \"data_path\": \"eval_results/v4_taxei_fixed_inject10_s0_eval.json\", \"model_name\": \"v4_taxei_fixed_inject10_s0\", \"seed\": 0, \"wall_clock_seconds\": 3970.2, \"gpu_hours\": 1.1}, \"hypothesis\": \"v4 TaxEI 10% seed=0 eval — 47 ALFWorld clean tasks. Dose-response 5-seed expansion.\", \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_taxei_fixed_inject10_s0_eval.json\", \"completed_at\": \"2026-05-15T20:03:56.888Z\", \"metrics\": {\"success_rate\": 0.702, \"successes\": 33, \"total\": 47, \"by_task_type\": {\"look_at_obj_in_light\": {\"total\": 6, \"success\": 5, \"rate\": 0.833}, \"pick_and_place_simple\": {\"total\": 8, \"success\": 5, \"rate\": 0.625}, \"pick_clean_then_place_in_recep\": {\"total\": 11, \"success\": 8, \"rate\": 0.727}, \"pick_cool_then_place_in_recep\": {\"total\": 7, \"success\": 4, \"rate\": 0.571}, \"pick_heat_then_place_in_recep\": {\"total\": 8, \"success\": 7, \"rate\": 0.875}, \"pick_two_obj_and_place\": {\"total\": 7, \"success\": 4, \"rate\": 0.571}}}}, \"v4-taxei-fixed-inject10-s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:54:17.800Z\", \"updated_at\": \"2026-05-15T18:57:47.705Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject10.jsonl --lora_rank 16 --num_train_epochs 3 --seed 1 --data_seed 1 --output_dir checkpoints/v4_taxei_fixed_inject10_s1 --gradient_accumulation_steps 8 --learning_rate 1e-4 --lr_scheduler_type cosine --gradient_checkpointing true --save_strategy epoch --logging_steps 5 --weight_decay 0.1 --adam_beta1 0.9 --adam_beta2 0.95\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"182703\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-fixed-inject10-s1.log\", \"submitted_at\": \"2026-05-15T17:54:17.595Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject10.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 1, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject10_s1/v0-20260516-015427/checkpoint-1635\", \"wall_clock_seconds\": 3728.4, \"gpu_hours\": 1.04}, \"hypothesis\": \"v4 TaxEI fixed-size ablation: 10% injection ratio seed=1 (4,358 total). Dose-response 5-seed expansion.\", \"reproduce\": {\"finished_at\": \"2026-05-15T18:53:12.812Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T18:53:14.974953+00:00\"}]}, \"metrics\": {\"final_loss\": 0.3013, \"train_loss_avg\": 0.4225, \"final_token_acc\": 0.8947, \"total_steps\": 1635, \"epochs\": 3, \"train_runtime_sec\": 3469, \"memory_gib\": 18.13, \"train_speed_s_per_it\": 2.121}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T18:56:25.993Z\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject10_s1/v0-20260516-015427/checkpoint-1635\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-fixed-inject10-s1.log\"}, \"v4-random-fixed-inject10-s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:54:20.390Z\", \"updated_at\": \"2026-05-15T18:57:42.428Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/ablation_fixed/sft_random_v4_fixed_inject10.jsonl --lora_rank 16 --num_train_epochs 3 --seed 123 --data_seed 123 --output_dir checkpoints/v4_random_fixed_inject10_s123 --gradient_accumulation_steps 8 --learning_rate 1e-4 --lr_scheduler_type cosine --gradient_checkpointing true --save_strategy epoch --logging_steps 5 --weight_decay 0.1 --adam_beta1 0.9 --adam_beta2 0.95\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"182781\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-fixed-inject10-s123.log\", \"submitted_at\": \"2026-05-15T17:54:20.028Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/mini_pipeline_v4/ablation_fixed/sft_random_v4_fixed_inject10.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"wall_clock_seconds\": 3802.4, \"gpu_hours\": 1.06}, \"hypothesis\": \"v4 Random fixed-size ablation: 10% injection ratio seed=123 (4,358 total). Dose-response 5-seed expansion.\", \"reproduce\": {\"finished_at\": \"2026-05-15T18:54:38.478Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T18:54:40.603963+00:00\"}]}, \"metrics\": {\"final_loss\": 0.3124, \"train_loss_avg\": 0.4236, \"final_token_acc\": 0.8867, \"total_steps\": 1635, \"epochs\": 3, \"train_runtime_sec\": 3535.7, \"train_samples_per_second\": 3.698, \"train_steps_per_second\": 0.462, \"memory_gib\": 18.95}, \"checkpoint_path\": \"checkpoints/v4_random_fixed_inject10_s123/v0-20260516-015429/checkpoint-1635\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-fixed-inject10-s123.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T18:57:42.428Z\"}, \"v4-taxei-fixed-inject10-s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:48:24.290Z\", \"updated_at\": \"2026-05-15T18:56:29.231Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject10.jsonl --lora_rank 16 --num_train_epochs 3 --seed 123 --data_seed 123 --output_dir checkpoints/v4_taxei_fixed_inject10_s123 --gradient_accumulation_steps 8 --learning_rate 1e-4 --lr_scheduler_type cosine --gradient_checkpointing true --save_strategy epoch --logging_steps 5 --weight_decay 0.1 --adam_beta1 0.9 --adam_beta2 0.95\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"180877\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-fixed-inject10-s123.log\", \"submitted_at\": \"2026-05-15T17:48:23.907Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject10.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject10_s123/v0-20260516-014833/checkpoint-1635\", \"wall_clock_seconds\": 4085.3, \"gpu_hours\": 1.13}, \"hypothesis\": \"v4 TaxEI fixed-size ablation: 10% injection ratio seed=123 (4,358 total = 3,922 clean + 436 injected). Dose-response 5-seed expansion — 补齐 10% 数据点。\", \"reproduce\": {\"finished_at\": \"2026-05-15T18:47:28.139Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T18:47:30.511963+00:00\"}]}, \"metrics\": {\"train_loss\": 0.4234, \"final_loss\": 0.3097, \"final_token_acc\": 0.8882, \"epochs\": 3, \"total_steps\": 1635, \"train_runtime_sec\": 3497, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject10_s123/v0-20260516-014833/checkpoint-1635\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T18:56:29.231Z\"}, \"v4-random-fixed-inject10-s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:48:26.373Z\", \"updated_at\": \"2026-05-15T18:56:27.890Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/ablation_fixed/sft_random_v4_fixed_inject10.jsonl --lora_rank 16 --num_train_epochs 3 --seed 0 --data_seed 0 --output_dir checkpoints/v4_random_fixed_inject10_s0 --gradient_accumulation_steps 8 --learning_rate 1e-4 --lr_scheduler_type cosine --gradient_checkpointing true --save_strategy epoch --logging_steps 5 --weight_decay 0.1 --adam_beta1 0.9 --adam_beta2 0.95\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"180956\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-fixed-inject10-s0.log\", \"submitted_at\": \"2026-05-15T17:48:26.104Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/mini_pipeline_v4/ablation_fixed/sft_random_v4_fixed_inject10.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 0, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_random_fixed_inject10_s0/v0-20260516-014835/checkpoint-1635\", \"wall_clock_seconds\": 4081.8, \"gpu_hours\": 1.13}, \"hypothesis\": \"v4 Random fixed-size ablation: 10% injection ratio seed=0 (4,358 total). Dose-response 5-seed expansion — 与 TaxEI 10% 对比 taxonomy 标签效果。\", \"reproduce\": {\"finished_at\": \"2026-05-15T18:47:48.342Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T18:47:53.242073+00:00\"}]}, \"metrics\": {\"train_loss\": 0.4227, \"final_loss\": 0.276, \"final_token_acc\": 0.9067, \"epochs\": 3, \"total_steps\": 1635, \"train_runtime_sec\": 3531, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_random_fixed_inject10_s0/v0-20260516-014835/checkpoint-1635\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T18:56:27.890Z\"}, \"v4-training-dynamics-forward-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:56:31.230Z\", \"updated_at\": \"2026-05-15T17:55:40.616Z\", \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/tax_error_inject_agent && CUDA_VISIBLE_DEVICES=2 bash scripts/run_training_dynamics_v2.sh\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"180322\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-training-dynamics-forward-v2.log\", \"submitted_at\": \"2026-05-15T16:56:31.040Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"training_dynamics\", \"data_count\": 0, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/artifacts/training_dynamics_v2/\", \"wall_clock_seconds\": 3546.9, \"gpu_hours\": 0.99}, \"conclusion\": \"success\", \"metrics\": {\"subsets_computed\": [\"vanilla_full\", \"taxei_full\", \"random_full\", \"taxei_inject10\", \"taxei_inject25\", \"taxei_inject50\"], \"taxei_inject50_injected_mean_loss\": 0.8185, \"taxei_inject50_clean_mean_loss\": 0.8514, \"per_operator\": {\"C1_ContextTruncation\": {\"mean\": 0.6489, \"n\": 101}, \"C4_ObservationMasking\": {\"mean\": 0.6782, \"n\": 92}, \"P1_StepOrderSwap\": {\"mean\": 0.6374, \"n\": 89}, \"P2_SubGoalDeletion\": {\"mean\": 0.6542, \"n\": 88}}, \"plots\": [\"subset_comparison\", \"operator_breakdown\", \"dose_response\"], \"output_dir\": \"/root/autodl-tmp/tax_error_inject_agent/artifacts/training_dynamics_v2/\"}, \"completed_at\": \"2026-05-15T17:55:37.917Z\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/artifacts/training_dynamics_v2/\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-training-dynamics-forward-v2.log\"}, \"v4-taxei-fixed-inject10-s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:52:30.170Z\", \"updated_at\": \"2026-05-15T17:55:38.973Z\", \"hypothesis\": \"v4 TaxEI fixed-size ablation: 10% injection ratio seed=0 (4,358 total = 3,922 clean + 436 injected). Dose-response 5-seed expansion — 10% 是最薄弱环节，仅有 seed=42 一个数据点。\", \"spec\": {\"data_path\": \"data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject10.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 0, \"injection_ratio\": 0.1, \"clean_count\": 3922, \"injected_count\": 436, \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject10.jsonl --lora_rank 16 --num_train_epochs 3 --seed 0 --data_seed 0 --output_dir checkpoints/v4_taxei_fixed_inject10_s0 --gradient_accumulation_steps 8 --learning_rate 1e-4 --lr_scheduler_type cosine --gradient_checkpointing true --save_strategy epoch --logging_steps 5 --weight_decay 0.1 --adam_beta1 0.9 --adam_beta2 0.95\\\"\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject10_s0/v0-20260516-005247/checkpoint-1635\", \"log_path\": \"checkpoints/v4_taxei_fixed_inject10_s0/v0-20260516-005247/logging.jsonl\"}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.4238, \"final_loss\": 0.3102, \"final_token_acc\": 0.8822, \"epochs\": 3, \"total_steps\": 1635, \"train_runtime_sec\": 3494, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject10_s0/v0-20260516-005247/checkpoint-1635\"}, \"completed_at\": \"2026-05-15T17:55:36.626Z\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject10_s0/v0-20260516-005247/checkpoint-1635\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-fixed-inject10-s0.log\"}, \"v4-taxei-inject10-seed0\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:46:10.420Z\", \"updated_at\": \"2026-05-15T17:53:36.371Z\", \"spec\": {\"hypothesis\": \"Dose-response 5-seed expansion: TaxEI 10% injection, seed=0 (fixed 4,358 total). 补齐 10% 只有 seed=42 一个数据点的短板。\", \"failure_reason\": \"duplicate of v4-taxei-fixed-inject10-s0, never submitted\"}, \"conclusion\": \"killed\"}, \"v4-random-inject10-seed0\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:46:13.097Z\", \"updated_at\": \"2026-05-15T17:53:35.645Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset /root/autodl-tmp/tax_error_inject_agent/data/mini_pipeline_v4/ablation_fixed/sft_random_v4_fixed_inject10.jsonl --output_dir checkpoints/random_inject10_seed0/v0-$(date +%Y%m%d-%H%M%S) --num_train_epochs 3 --lora_rank 16 --lora_alpha 32 --learning_rate 1e-4 --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --max_length 4096 --seed 0 --logging_steps 5 --save_strategy epoch --bf16 true --gradient_checkpointing true\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"181792\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-inject10-seed0.log\", \"submitted_at\": \"2026-05-15T17:48:59.472Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"duplicate of v4-random-fixed-inject10-s0, process no longer exists\"}, \"conclusion\": \"killed\"}, \"v4-taxei-inject10-seed123\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:46:11.744Z\", \"updated_at\": \"2026-05-15T17:53:34.706Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset /root/autodl-tmp/tax_error_inject_agent/data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject10.jsonl --output_dir checkpoints/taxei_inject10_seed123/v0-$(date +%Y%m%d-%H%M%S) --num_train_epochs 3 --lora_rank 16 --lora_alpha 32 --learning_rate 1e-4 --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --max_length 4096 --seed 123 --logging_steps 5 --save_strategy epoch --bf16 true --gradient_checkpointing true\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"181699\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-inject10-seed123.log\", \"submitted_at\": \"2026-05-15T17:48:56.845Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"duplicate of v4-taxei-fixed-inject10-s123, process no longer exists\"}, \"conclusion\": \"killed\"}, \"v4-random-seed7-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:29:15.592Z\", \"updated_at\": \"2026-05-15T17:43:36.723Z\", \"spec\": {\"command\": \"python3 eval/recovery.py --model_path checkpoints/mini_random_sft_v4_seed7/v0-20260515-233427/checkpoint-3387 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --task_list eval/eval_tasks_47.json --num_episodes 47 --seed 42 --device cuda:0 --output eval_results/v4_random_seed7_eval.json\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"179098\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-seed7-eval.log\", \"submitted_at\": \"2026-05-15T17:29:24.122Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"eval/eval_tasks_47.json\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (random SFT seed=7)\", \"seed\": 42, \"checkpoint_source\": \"v4-random-seed7\", \"eval_data\": \"eval_tasks_47.json\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_random_sft_v4_seed7/v0-20260515-233427/checkpoint-3387\", \"wall_clock_seconds\": 852.6, \"gpu_hours\": 0.24}, \"hypothesis\": \"v4 Random SFT seed=7 eval — 47 ALFWorld tasks, 5-seed expansion ← 基于 v4-random-seed7\", \"reproduce\": {\"finished_at\": \"2026-05-15T17:40:45.965Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:40:48.585893+00:00\"}]}, \"metrics\": {\"success_rate\": 0.553, \"successes\": 26, \"total\": 47, \"by_task_type\": {\"look_at_obj_in_light\": {\"total\": 6, \"success\": 5, \"rate\": 0.833}, \"pick_and_place_simple\": {\"total\": 8, \"success\": 4, \"rate\": 0.5}, \"pick_clean_then_place_in_recep\": {\"total\": 11, \"success\": 6, \"rate\": 0.545}, \"pick_cool_then_place_in_recep\": {\"total\": 7, \"success\": 3, \"rate\": 0.429}, \"pick_heat_then_place_in_recep\": {\"total\": 8, \"success\": 5, \"rate\": 0.625}, \"pick_two_obj_and_place\": {\"total\": 7, \"success\": 3, \"rate\": 0.429}}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T17:43:36.723Z\"}, \"v4-random-seed1-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:17:51.435Z\", \"updated_at\": \"2026-05-15T17:32:36.551Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && mkdir -p eval_results && CUDA_VISIBLE_DEVICES=0 python3 eval/recovery.py --model_path checkpoints/mini_random_sft_v4_seed1/v0-20260515-232340/checkpoint-3387 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --task_list eval/eval_tasks_47.json --num_episodes 47 --seed 42 --device cuda:0 --output eval_results/v4_random_seed1_eval.json\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"178005\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-seed1-eval.log\", \"submitted_at\": \"2026-05-15T17:18:03.664Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 872.9, \"gpu_hours\": 0.24}, \"reproduce\": {\"finished_at\": \"2026-05-15T17:30:35.329Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:30:38.085288+00:00\"}]}, \"metrics\": {\"success_rate\": 0.468, \"successes\": 22, \"total\": 47, \"by_task_type\": {\"look_at_obj_in_light\": {\"success\": 5, \"total\": 6, \"rate\": 0.833}, \"pick_and_place_simple\": {\"success\": 2, \"total\": 8, \"rate\": 0.25}, \"pick_clean_then_place_in_recep\": {\"success\": 5, \"total\": 11, \"rate\": 0.455}, \"pick_cool_then_place_in_recep\": {\"success\": 2, \"total\": 7, \"rate\": 0.286}, \"pick_heat_then_place_in_recep\": {\"success\": 5, \"total\": 8, \"rate\": 0.625}, \"pick_two_obj_and_place\": {\"success\": 3, \"total\": 7, \"rate\": 0.429}}}, \"checkpoint_path\": \"checkpoints/mini_random_sft_v4_seed1/v0-20260515-232340/checkpoint-3387\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-seed1-eval.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T17:32:36.551Z\"}, \"v4-random-seed7\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:34:10.206Z\", \"updated_at\": \"2026-05-15T17:29:09.688Z\", \"hypothesis\": \"v4 Random SFT seed=7 (5-seed expansion) — 9,029 samples, LoRA rank=16, 3 epochs\", \"spec\": {\"command\": \"swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/sft_random_v4.jsonl --lora_rank 16 --lora_alpha 32 --num_train_epochs 3 --seed 7 --output_dir checkpoints/mini_random_sft_v4_seed7 --gradient_accumulation_steps 8 --learning_rate 1e-4 --lr_scheduler_type cosine --gradient_checkpointing true --save_strategy epoch --logging_steps 5 --weight_decay 0.1 --adam_beta1 0.9 --adam_beta2 0.95\", \"server\": \"autodl-5090\", \"data_path\": \"data/mini_pipeline_v4/sft_random_v4.jsonl\", \"data_count\": 9029, \"model_name\": \"Qwen3-8B\", \"seed\": 7, \"gpu\": \"cuda:1\", \"pid\": 164126, \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-seed7.log\", \"checkpoint_path\": \"checkpoints/mini_random_sft_v4_seed7/v0-20260515-233427\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T17:26:13.042Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:26:15.009112+00:00\"}]}, \"metrics\": {\"final_loss\": 0.173, \"final_token_acc\": 0.935, \"initial_loss\": 4.017, \"total_steps\": 3387, \"epochs\": 3, \"total_flos\": 697192362530058200, \"train_runtime_sec\": 6672, \"memory_gib\": 18.49}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_random_sft_v4_seed7/v0-20260515-233427/checkpoint-3387\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-seed7.log\", \"completed_at\": \"2026-05-15T17:29:09.688Z\"}, \"v4-random-seed1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:21:02.077Z\", \"updated_at\": \"2026-05-15T17:17:33.614Z\", \"spec\": {\"hypothesis\": \"v4 Random SFT seed=1 (5-seed expansion) — 9,029 samples, LoRA rank=16, 3 epochs\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python3 train/sft_train.py --config configs/mini_random_sft_v4_seed1.yaml\", \"server\": \"autodl-5090\", \"data_path\": \"data/mini_random_v4\", \"data_count\": 1129, \"model_name\": \"Qwen3-8B\", \"seed\": 1, \"gpu\": [\"cuda:0\"], \"pid\": \"163009\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-seed1.log\", \"checkpoint_path\": \"checkpoints/mini_random_sft_v4_seed1/v0-20260515-232340/\", \"submitted_at\": \"2026-05-15T15:23:31Z\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 6842.6, \"gpu_hours\": 1.9}, \"conclusion\": \"success\", \"checkpoint_path\": \"checkpoints/mini_random_sft_v4_seed1/v0-20260515-232340/checkpoint-3387\", \"metrics\": {\"final_loss\": 0.167, \"final_token_acc\": 0.938, \"initial_loss\": 4.017, \"total_steps\": 3387, \"epochs\": 3, \"total_flos\": 697000000000000000}, \"completed_at\": \"2026-05-15T17:17:33.614Z\"}, \"v4-taxei-seed1-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:39:59.021Z\", \"updated_at\": \"2026-05-15T16:53:41.245Z\", \"hypothesis\": \"v4 TaxEI SFT seed=1 eval — 47 ALFWorld tasks, 5-seed expansion\", \"parent\": \"v4-taxei-seed1\", \"spec\": {\"command\": \"python eval_agent.py --checkpoint checkpoints/mini_taxei_sft_v4_seed1/v0-20260515-214035/checkpoint-3387 --split valid_unseen\", \"server\": \"autodl-5090\", \"data_path\": \"valid_unseen\", \"data_count\": 47, \"model_name\": \"mini_taxei_sft_v4_seed1/checkpoint-3387\", \"seed\": 1, \"checkpoint_source\": \"v4-taxei-seed1\", \"eval_data\": \"valid_unseen\", \"gpu\": [\"cuda:2\"], \"pid\": 173824, \"log_path\": \"eval_results/v4_taxei_seed1_eval.json\", \"checkpoint_path\": \"checkpoints/mini_taxei_sft_v4_seed1/v0-20260515-214035/checkpoint-3387\", \"parent\": \"v4-taxei-seed1\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T16:53:35.955Z\", \"metrics\": {\"success_rate\": 0.596, \"successes\": 28, \"total\": 47, \"by_task_type\": {\"look_at_obj_in_light\": {\"total\": 6, \"success\": 5, \"rate\": 0.833}, \"pick_and_place_simple\": {\"total\": 8, \"success\": 4, \"rate\": 0.5}, \"pick_clean_then_place_in_recep\": {\"total\": 11, \"success\": 5, \"rate\": 0.455}, \"pick_cool_then_place_in_recep\": {\"total\": 7, \"success\": 2, \"rate\": 0.286}, \"pick_heat_then_place_in_recep\": {\"total\": 8, \"success\": 7, \"rate\": 0.875}, \"pick_two_obj_and_place\": {\"total\": 7, \"success\": 5, \"rate\": 0.714}}}}, \"v4-vanilla-seed1-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:49:28.411Z\", \"updated_at\": \"2026-05-15T16:43:19.834Z\", \"hypothesis\": \"v4 Vanilla SFT seed=1 eval — 47 ALFWorld tasks, 5-seed expansion\", \"parent\": \"v4-vanilla-seed1\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 eval/recovery.py --model_path checkpoints/mini_vanilla_sft_v4_seed1/v0-20260515-214031/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --task_list eval/eval_tasks_47.json --num_episodes 47 --seed 42 --device cuda:0 --output eval_results/v4_vanilla_seed1_eval.json\", \"server\": \"autodl-5090\", \"data_path\": \"eval/eval_tasks_47.json\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (vanilla v4 seed=1)\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/mini_vanilla_sft_v4_seed1/v0-20260515-214031/checkpoint-1635\", \"eval_data\": \"47 ALFWorld tasks (clean, no injection)\", \"gpu\": [\"cuda:0\"]}, \"log_path\": \"~/runs/tax_error_inject_agent/v4-vanilla-seed1-eval.log\", \"checkpoint_path\": \"eval_results/v4_vanilla_seed1_eval.json\", \"conclusion\": \"success\", \"metrics\": {\"eval_success_rate\": 0.66, \"eval_successes\": 31, \"eval_total\": 47, \"vs_seed42_pp\": 4.3}, \"completed_at\": \"2026-05-15T16:42:21.398Z\"}, \"v4-taxei-seed7-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:40:01.513Z\", \"updated_at\": \"2026-05-15T16:40:14.867Z\", \"hypothesis\": \"v4 TaxEI SFT seed=7 eval — 47 ALFWorld tasks, 5-seed expansion\", \"parent\": \"v4-taxei-seed7\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python3 eval/recovery.py --model_path checkpoints/mini_taxei_sft_v4_seed7/v0-20260515-214039/checkpoint-3387 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --task_list eval/eval_tasks_47.json --num_episodes 47 --seed 42 --device cuda:0 --output eval_results/v4_taxei_seed7_eval.json\", \"server\": \"autodl-5090\", \"data_path\": \"eval/eval_tasks_47.json\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (TaxEI v4 seed=7)\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/mini_taxei_sft_v4_seed7/v0-20260515-214039/checkpoint-3387\", \"eval_data\": \"47 ALFWorld tasks (clean, no injection)\", \"parent\": \"v4-taxei-seed7\", \"gpu\": [\"cuda:3\"], \"pid\": \"165338\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-seed7-eval.log\", \"checkpoint_path\": \"eval_results/v4_taxei_seed7_eval.json\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.617, \"successes\": 29, \"total\": 47, \"by_task\": {\"look_at_obj_in_light\": \"4/6 (0.667)\", \"pick_and_place_simple\": \"5/8 (0.625)\", \"pick_clean_then_place_in_recep\": \"5/11 (0.455)\", \"pick_cool_then_place_in_recep\": \"4/7 (0.571)\", \"pick_heat_then_place_in_recep\": \"7/8 (0.875)\", \"pick_two_obj_and_place\": \"4/7 (0.571)\"}}, \"completed_at\": \"2026-05-15T16:40:14.867Z\"}, \"v4-training-dynamics-forward\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:48:36.487Z\", \"updated_at\": \"2026-05-15T16:37:23.642Z\", \"hypothesis\": \"D027 Training Dynamics: Post-hoc forward pass on seed=42 checkpoints (Vanilla/TaxEI/Random + dose-response 10%/25%/50%) — compute per-subset loss (clean vs injected) and per-operator loss (P1/P2/C1/C4). Key finding: training loss SD=0.0004 across seeds but eval SD=8.6pp — memorization-generalization dissociation.\", \"spec\": {\"command\": \"bash scripts/run_training_dynamics.sh\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/tax_error_inject_agent/data/mini_pipeline_v4/\", \"data_count\": 6, \"model_name\": \"Qwen3-8B\", \"seed\": 42}, \"metrics\": {\"vanilla_full\": {\"clean_loss\": 0.6853, \"clean_n\": 4358}, \"taxei_full\": {\"clean_loss\": 0.7712, \"injected_loss\": 0.6139, \"clean_n\": 8269, \"injected_n\": 760, \"per_operator\": {\"P1_StepOrderSwap\": 0.6165, \"P2_SubGoalDeletion\": 0.6161, \"C1_ContextTruncation\": 0.5932, \"C4_ObservationMasking\": 0.6298}}, \"random_full\": {\"clean_loss\": 0.7354, \"injected_loss\": 0.5902, \"clean_n\": 8269, \"injected_n\": 760}, \"dose_response\": {\"taxei_10pct\": {\"clean_loss\": 0.6628, \"injected_loss\": 0.6464, \"gap\": -0.0164, \"injected_n\": 70}, \"taxei_25pct\": {\"clean_loss\": 0.701, \"injected_loss\": 0.574, \"gap\": -0.127, \"injected_n\": 168}, \"taxei_50pct\": {\"clean_loss\": 0.8516, \"injected_loss\": 0.6547, \"gap\": -0.1969, \"injected_n\": 370}}, \"key_findings\": \"Clear dose-response: injected-clean gap widens from -0.016 (10%) to -0.127 (25%) to -0.197 (50%). TaxEI operators C1_ContextTruncation consistently lowest loss. Higher injection rates also degrade clean sample loss (0.663→0.701→0.852).\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/artifacts/training_dynamics/\", \"log_path\": \"/root/autodl-tmp/tax_error_inject_agent/artifacts/training_dynamics/\", \"completed_at\": \"2026-05-15T16:35:47.805Z\"}, \"qualitative-failure-analysis\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:43:33.358Z\", \"updated_at\": \"2026-05-15T15:43:47.361Z\", \"hypothesis\": \"D026 Qualitative Failure Analysis: Extract failure patterns from existing eval logs. Key finding: TaxEI loop_repetition rate 17.4% vs Vanilla 7.8% vs Random 3.2%. TaxEI models exhibit fixation behavior (repeated action loops) especially on multi-step tasks under P1/P2 operators.\", \"conclusion\": \"success\", \"metrics\": {\"data_source\": \"eval_results/failure_analysis.json\", \"taxei_loop_repetition_rate\": 0.174, \"vanilla_loop_repetition_rate\": 0.078, \"random_loop_repetition_rate\": 0.032, \"taxei_loop_count\": 49, \"vanilla_loop_count\": 22, \"random_loop_count\": 6, \"per_operator\": {\"P1\": 15, \"P2\": 14, \"C1\": 11, \"C4\": 9}, \"note\": \"Random data only from seed=42 recovery eval + 3-seed clean eval (188 episodes vs 282). Rates to be updated after 5-seed completion.\"}}, \"v4-taxei-seed1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:40:26.898Z\", \"updated_at\": \"2026-05-15T15:39:39.545Z\", \"spec\": {\"command\": \"swift sft --model Qwen3-8B --dataset sft_taxei_v4.jsonl --seed 1 --lora_rank 16 --lora_alpha 32 --num_train_epochs 3\", \"server\": \"autodl-5090\", \"data_path\": \"data/mini_pipeline_v4/sft_taxei_v4.jsonl\", \"data_count\": 9029, \"model_name\": \"Qwen3-8B\", \"seed\": 1, \"gpu\": \"cuda:2\", \"pid\": 154937}, \"metrics\": {\"final_loss\": 0.1667, \"avg_loss\": 0.3561, \"token_accuracy\": 0.915, \"final_token_acc\": 0.942, \"train_steps\": 3387, \"train_epochs\": 3, \"train_duration_min\": 108.9, \"memory_gib\": 18.49, \"checkpoint_path\": \"checkpoints/mini_taxei_sft_v4_seed1/v0-20260515-214035/checkpoint-3387\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T15:30:06.293Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T15:30:07.753494+00:00\"}]}, \"conclusion\": \"success\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-seed1.log\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_taxei_sft_v4_seed1/v0-20260515-214035/checkpoint-3387\", \"completed_at\": \"2026-05-15T15:39:39.545Z\"}, \"v4-taxei-seed7\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:40:29.737Z\", \"updated_at\": \"2026-05-15T15:39:16.334Z\", \"spec\": {\"command\": \"swift sft --model Qwen3-8B --dataset sft_taxei_v4.jsonl --seed 7 --lora_rank 16 --lora_alpha 32 --3epochs\", \"server\": \"autodl-5090\", \"data_path\": \"data/mini_pipeline_v4/sft_taxei_v4.jsonl\", \"data_count\": 9029, \"model_name\": \"Qwen3-8B\", \"seed\": 7, \"gpu\": \"cuda:3\", \"pid\": 155145}, \"metrics\": {\"current_step\": 3387, \"total_steps\": 3387, \"progress_pct\": 100, \"train_loss\": 0.3568, \"final_step_loss\": 0.1753, \"token_acc\": 0.9009, \"final_token_acc\": 0.9328, \"train_runtime_s\": 6591.9, \"epochs\": 3, \"peak_memory_gib\": 18.49, \"gpu\": \"cuda:3\", \"pid\": 155145}, \"reproduce\": {\"finished_at\": \"2026-05-15T15:32:43.183Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T15:32:44.276153+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_taxei_sft_v4_seed7/v0-20260515-214039/checkpoint-3387\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-seed7.log\", \"completed_at\": \"2026-05-15T15:36:45.958Z\"}, \"v4-vanilla-seed7-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:49:11.983Z\", \"updated_at\": \"2026-05-15T15:32:42.490Z\", \"hypothesis\": \"v4 Vanilla SFT seed=7 eval — 47 ALFWorld tasks, 5-seed expansion\", \"parent\": \"v4-vanilla-seed7\", \"spec\": {\"command\": \"python3 eval/recovery.py --model_path checkpoints/mini_vanilla_sft_v4_seed7/v1-20260515-214032/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --num_episodes 47 --output eval_results/v4_vanilla_seed7_eval.json --device cuda:1 --seed 42\", \"server\": \"autodl-5090\", \"data_path\": \"eval/47 ALFWorld valid_unseen\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (vanilla v4 seed=7)\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/mini_vanilla_sft_v4_seed7/v1-20260515-214032/checkpoint-1635\", \"eval_data\": \"47 ALFWorld tasks (clean, no injection)\", \"parent\": \"v4-vanilla-seed7\", \"gpu\": [\"cuda:1\"], \"pid\": \"160587\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-vanilla-seed7-eval.log\", \"checkpoint_path\": \"eval_results/v4_vanilla_seed7_eval.json\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"success\", \"metrics\": {\"eval_success_rate\": 0.745, \"eval_successes\": 35, \"eval_total\": 47, \"vs_seed42_pp\": 12.8}, \"completed_at\": \"2026-05-15T15:32:42.490Z\"}, \"v4-vanilla-seed1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:40:21.621Z\", \"updated_at\": \"2026-05-15T14:49:23.447Z\", \"spec\": {\"command\": \"swift sft --model Qwen3-8B --dataset sft_vanilla_v4.jsonl --seed 1 --lora_rank 16 --lora_alpha 32 --3epochs\", \"server\": \"autodl-5090\", \"data_path\": \"data/mini_pipeline_v4/sft_vanilla_v4.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 1, \"gpu\": \"cuda:0\", \"pid\": 154589, \"checkpoint_path\": \"checkpoints/mini_vanilla_sft_v4_seed1/v0-20260515-214031/checkpoint-1635\", \"log_path\": \"checkpoints/mini_vanilla_sft_v4_seed1/v0-20260515-214031/\"}, \"metrics\": {\"final_loss\": 0.292, \"avg_loss\": 0.416, \"token_accuracy\": 0.903, \"train_steps\": 1635, \"train_epochs\": 3, \"train_duration_min\": 58.8, \"memory_gib\": 17.63, \"checkpoint_path\": \"checkpoints/mini_vanilla_sft_v4_seed1/v0-20260515-214031/checkpoint-1635\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T14:39:36.578Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T14:39:37.963564+00:00\"}]}, \"conclusion\": \"success\", \"hypothesis\": \"D010 Phase 1: v4 Vanilla SFT seed=1 多种子验证 — 4,358 samples, LoRA rank=16, 3 epochs, 与 seed=42 的 61.7% 对比波动范围\", \"completed_at\": \"2026-05-15T14:49:23.447Z\"}, \"v4-vanilla-seed7\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:45:24.536Z\", \"updated_at\": \"2026-05-15T14:46:55.133Z\", \"hypothesis\": \"D010 Phase 1: v4 Vanilla SFT seed=7 多种子验证 — 4,358 samples, LoRA rank=16, 3 epochs, 与 seed=42 的 61.7% 对比波动范围\", \"spec\": {\"command\": \"swift sft --model Qwen3-8B --dataset sft_vanilla_v4.jsonl --seed 7 --lora_rank 16 --lora_alpha 32 --3epochs\", \"server\": \"autodl-5090\", \"data_path\": \"data/mini_pipeline_v4/sft_vanilla_v4.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 7, \"gpu\": \"cuda:1\", \"pid\": 154666}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T18:20:48.185Z\", \"metrics\": {\"final_loss\": 0.295, \"avg_loss\": 0.415, \"token_accuracy\": 0.898, \"train_steps\": 1635, \"train_epochs\": 3, \"train_duration_min\": 59.4, \"checkpoint_path\": \"checkpoints/mini_vanilla_sft_v4_seed7/v0-20260515-214031/checkpoint-1635\"}}, \"v4-random-recovery-eval-s123\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T12:44:11.530Z\", \"updated_at\": \"2026-05-15T12:44:11.531Z\", \"spec\": {\"model_name\": \"Qwen3-8B\", \"seed\": 123, \"method\": \"random\", \"eval_type\": \"recovery\", \"parent\": \"v4-random-sft-seed123\", \"checkpoint_source\": \"checkpoints/mini_random_sft_v4_seed123/v0-20260515-055925/checkpoint-3387\", \"eval_data\": \"47 ALFWorld injected eval (round-robin)\", \"server\": \"autodl-5090\"}}, \"v4-random-fixed-inject50-s123-eval\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:42:34.082Z\", \"updated_at\": \"2026-05-15T11:03:47.011Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && python3 eval/recovery.py --model_path checkpoints/v4_random_fixed_inject50_s123/v0-20260515-172123/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_random_fixed_inject50_s123_eval.json --device cuda:0\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"140871\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-fixed-inject50-s123-eval.log\", \"submitted_at\": \"2026-05-15T10:42:33.926Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"injection_ratio\": 0.5, \"method\": \"random\", \"parent\": \"v4-random-fixed-inject50-s123\", \"checkpoint_source\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_random_fixed_inject50_s123/v0-20260515-172123/checkpoint-1635\", \"eval_data\": \"47 ALFWorld clean tasks\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.702, \"successes\": 33, \"total\": 47}}, \"v4-random-fixed-inject50-s0-eval\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:42:31.691Z\", \"updated_at\": \"2026-05-15T11:03:43.512Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && python3 eval/recovery.py --model_path checkpoints/v4_random_fixed_inject50_s0/v0-20260515-172121/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_random_fixed_inject50_s0_eval.json --device cuda:0\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"140731\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-fixed-inject50-s0-eval.log\", \"submitted_at\": \"2026-05-15T10:42:31.544Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen3-8B\", \"seed\": 0, \"injection_ratio\": 0.5, \"method\": \"random\", \"parent\": \"v4-random-fixed-inject50-s0\", \"checkpoint_source\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_random_fixed_inject50_s0/v0-20260515-172121/checkpoint-1635\", \"eval_data\": \"47 ALFWorld clean tasks\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.468, \"successes\": 22, \"total\": 47}}, \"v4-taxei-fixed-inject50-s123-eval\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:16:18.413Z\", \"updated_at\": \"2026-05-15T10:42:27.288Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && python3 eval/recovery.py --model_path /root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject50_s123/v0-20260515-153737/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_taxei_fixed_inject50_s123_eval.json --device cuda:0\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"138352\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-fixed-inject50-s123-eval.log\", \"submitted_at\": \"2026-05-15T10:16:18.279Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"success\", \"metrics\": {\"eval_success_rate\": 0.468, \"eval_successes\": 22, \"eval_total\": 47}}, \"v4-taxei-fixed-inject50-s0-eval\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:16:16.102Z\", \"updated_at\": \"2026-05-15T10:42:25.403Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && python3 eval/recovery.py --model_path /root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject50_s0/v0-20260515-153735/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_taxei_fixed_inject50_s0_eval.json --device cuda:0\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"138210\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-fixed-inject50-s0-eval.log\", \"submitted_at\": \"2026-05-15T10:16:15.945Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"success\", \"metrics\": {\"eval_success_rate\": 0.702, \"eval_successes\": 33, \"eval_total\": 47}}, \"v4-random-fixed-inject25-s123-eval\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:28:36.999Z\", \"updated_at\": \"2026-05-15T10:40:52.525Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && python3 eval/recovery.py --model_path checkpoints/v4_random_fixed_inject25_s123/v0-20260515-173124/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_random_fixed_inject25_s123_eval.json --device cuda:0\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"139943\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-fixed-inject25-s123-eval.log\", \"submitted_at\": \"2026-05-15T10:31:06.664Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.511, \"total\": 47, \"successes\": 24, \"by_task\": {\"look_at_obj_in_light\": 0.667, \"pick_and_place_simple\": 0.375, \"pick_clean_then_place_in_recep\": 0.545, \"pick_cool_then_place_in_recep\": 0.143, \"pick_heat_then_place_in_recep\": 0.75, \"pick_two_obj_and_place\": 0.571}}}, \"v4-random-fixed-inject25-s0-eval\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:28:34.789Z\", \"updated_at\": \"2026-05-15T10:40:49.769Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && python3 eval/recovery.py --model_path checkpoints/v4_random_fixed_inject25_s0/v0-20260515-173122/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_random_fixed_inject25_s0_eval.json --device cuda:0\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"139405\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-fixed-inject25-s0-eval.log\", \"submitted_at\": \"2026-05-15T10:28:34.627Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.617, \"total\": 47, \"successes\": 29, \"by_task\": {\"look_at_obj_in_light\": 0.667, \"pick_and_place_simple\": 0.625, \"pick_clean_then_place_in_recep\": 0.455, \"pick_cool_then_place_in_recep\": 0.571, \"pick_heat_then_place_in_recep\": 0.75, \"pick_two_obj_and_place\": 0.714}}}, \"v4-random-fixed-inject25-s123\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:37:05.059Z\", \"updated_at\": \"2026-05-15T10:28:27.449Z\", \"hypothesis\": \"D022 multi-seed dose-response: Random 25% injection, seed=123 (fixed 4,358 total). 对标 seed=42 的 55.3%。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/ablation_fixed/sft_random_v4_fixed_inject25.jsonl --lora_rank 16 --num_train_epochs 3 --seed 123 --output_dir checkpoints/v4_random_fixed_inject25_s123 --gradient_accumulation_steps 8 --learning_rate 1e-4 --lr_scheduler_type cosine --gradient_checkpointing true --save_strategy epoch --logging_steps 5 --weight_decay 0.1 --adam_beta1 0.9 --adam_beta2 0.95\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"134594\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-fixed-inject25-s123.log\", \"submitted_at\": \"2026-05-15T09:31:15.334Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"success\"}, \"v4-random-fixed-inject50-s123\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:37:07.099Z\", \"updated_at\": \"2026-05-15T10:16:08.482Z\", \"hypothesis\": \"D022 multi-seed dose-response: Random 50% injection, seed=123 (fixed 4,358 total). 对标 seed=42 的 57.4%。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/ablation_fixed/sft_random_v4_fixed_inject50.jsonl --lora_rank 16 --num_train_epochs 3 --seed 123 --output_dir checkpoints/v4_random_fixed_inject50_s123 --gradient_accumulation_steps 8 --learning_rate 1e-4 --lr_scheduler_type cosine --gradient_checkpointing true --save_strategy epoch --logging_steps 5 --weight_decay 0.1 --adam_beta1 0.9 --adam_beta2 0.95\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"132973\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-fixed-inject50-s123.log\", \"submitted_at\": \"2026-05-15T09:21:14.249Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"success\"}, \"v4-random-fixed-inject50-s0\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:37:06.104Z\", \"updated_at\": \"2026-05-15T10:16:07.812Z\", \"hypothesis\": \"D022 multi-seed dose-response: Random 50% injection, seed=0 (fixed 4,358 total). 对标 seed=42 的 57.4%。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/ablation_fixed/sft_random_v4_fixed_inject50.jsonl --lora_rank 16 --num_train_epochs 3 --seed 0 --output_dir checkpoints/v4_random_fixed_inject50_s0 --gradient_accumulation_steps 8 --learning_rate 1e-4 --lr_scheduler_type cosine --gradient_checkpointing true --save_strategy epoch --logging_steps 5 --weight_decay 0.1 --adam_beta1 0.9 --adam_beta2 0.95\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"132895\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-fixed-inject50-s0.log\", \"submitted_at\": \"2026-05-15T09:21:11.673Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"success\"}, \"v4-taxei-fixed-inject50-s123\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:37:02.779Z\", \"updated_at\": \"2026-05-15T09:19:37.321Z\", \"hypothesis\": \"D022 multi-seed dose-response: TaxEI 50% injection, seed=123 (fixed 4,358 total). 对标 seed=42 的 51.1%。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject50.jsonl --lora_rank 16 --num_train_epochs 3 --seed 123 --output_dir checkpoints/v4_taxei_fixed_inject50_s123 --gradient_accumulation_steps 8 --learning_rate 1e-4 --lr_scheduler_type cosine --gradient_checkpointing true --save_strategy epoch --logging_steps 5 --weight_decay 0.1 --adam_beta1 0.9 --adam_beta2 0.95\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"127437\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-fixed-inject50-s123.log\", \"submitted_at\": \"2026-05-15T07:37:29.012Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.4348, \"train_duration_min\": 52.9, \"train_steps\": 1635, \"train_epochs\": 3, \"data_count\": 4358}}, \"v4-taxei-fixed-inject50-s0\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:37:01.354Z\", \"updated_at\": \"2026-05-15T09:19:36.235Z\", \"hypothesis\": \"D022 multi-seed dose-response: TaxEI 50% injection, seed=0 (fixed 4,358 total). 对标 seed=42 的 51.1%。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject50.jsonl --lora_rank 16 --num_train_epochs 3 --seed 0 --output_dir checkpoints/v4_taxei_fixed_inject50_s0 --gradient_accumulation_steps 8 --learning_rate 1e-4 --lr_scheduler_type cosine --gradient_checkpointing true --save_strategy epoch --logging_steps 5 --weight_decay 0.1 --adam_beta1 0.9 --adam_beta2 0.95\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"127162\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-fixed-inject50-s0.log\", \"submitted_at\": \"2026-05-15T07:37:26.289Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.4342, \"train_duration_min\": 52.4, \"train_steps\": 1635, \"train_epochs\": 3, \"data_count\": 4358}}, \"v4-vanilla-recovery-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T19:30:18.314Z\", \"updated_at\": \"2026-05-15T03:29:56.077Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 eval/injected_eval.py --model_path checkpoints/mini_vanilla_sft_v4/v0-20260514-201441/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --model_variant vanilla --num_episodes 47 --seed 42 --device cuda:0 --output eval_results/v4_vanilla_recovery_eval.json\", \"server\": \"autodl-5090\", \"model_name\": \"Qwen3-8B + LoRA (vanilla v4 seed=42)\", \"checkpoint_source\": \"checkpoints/mini_vanilla_sft_v4/v0-20260514-201441/checkpoint-1635\", \"eval_data\": \"47 ALFWorld tasks with error injection\", \"seed\": 42, \"parent\": \"mini-vanilla-sft-v4\", \"checkpoint_path\": \"eval_results/v4_vanilla_recovery_eval.json\", \"log_path\": \"eval_results/v4_vanilla_recovery_eval.json\"}, \"hypothesis\": \"v4 Vanilla SFT seed=42 recovery eval (injected_eval.py) — 47 episodes with error injection, measuring detection/recovery/success rates under P1/P2/C1/C4 operators\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.617, \"successes\": 29, \"total\": 47, \"recovery_rate\": 0.617, \"detection_rate\": 0, \"per_operator\": {\"C1_context_truncation\": {\"recovered\": 9, \"total\": 12, \"rate\": 0.75}, \"C4_observation_masking\": {\"recovered\": 6, \"total\": 11, \"rate\": 0.545}, \"P1_step_order_swap\": {\"recovered\": 7, \"total\": 12, \"rate\": 0.583}, \"P2_sub_goal_deletion\": {\"recovered\": 7, \"total\": 12, \"rate\": 0.583}}}, \"completed_at\": \"2026-05-14T21:20:15.791Z\"}, \"v4-random-fixed-inject50-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T01:43:46.913Z\", \"updated_at\": \"2026-05-15T02:03:49.013Z\", \"hypothesis\": \"v4 Random 50% injection fixed-size eval — 47 tasks clean eval. 与 TaxEI 50% (51.1%) 对比。Random dose-response 最后一点。\", \"spec\": {\"gpu\": [\"cuda:3\"]}, \"reproduce\": {\"finished_at\": \"2026-05-15T01:56:26.837Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T01:56:28.410747+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"eval_success_rate\": 0.574, \"eval_successes\": 27, \"eval_total\": 47, \"vs_vanilla_seed42_pp\": -4.3, \"vs_taxei_50_pp\": 6.3}, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_random_fixed_inject50_eval.json\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-fixed-inject50-eval.log\", \"completed_at\": \"2026-05-15T02:00:22.858Z\"}, \"v4-random-fixed-inject25-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T01:48:25.777Z\", \"updated_at\": \"2026-05-15T02:03:46.203Z\", \"hypothesis\": \"v4 Random 25% injection fixed-size eval — 47 ALFWorld tasks (clean). 与 TaxEI 25% (48.9%) 对比。\", \"parent\": \"v4-random-fixed-inject25\", \"spec\": {\"command\": \"python3 eval/recovery.py --model_path /root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_random_fixed_inject25/v1-20260515-084707/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_random_fixed_inject25_eval.json --device cuda:0\", \"server\": \"autodl-5090\", \"parent\": \"v4-random-fixed-inject25\", \"checkpoint_source\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_random_fixed_inject25/v1-20260515-084707/checkpoint-1635\", \"eval_data\": \"47 ALFWorld tasks (clean, no injection)\", \"data_path\": \"eval/alfworld_47_clean\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (random fixed inject25)\", \"seed\": 42, \"gpu\": [\"cuda:0\"], \"pid\": \"112516\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-fixed-inject25-eval.log\"}, \"conclusion\": \"success\", \"metrics\": {\"eval_success_rate\": 0.553, \"eval_successes\": 26, \"eval_total\": 47, \"vs_vanilla_seed42_pp\": -6.4, \"vs_taxei_25_pp\": 6.4}, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_random_fixed_inject25_eval.json\", \"completed_at\": \"2026-05-15T01:59:41.894Z\"}, \"v4-random-fixed-inject50\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T00:45:08.375Z\", \"updated_at\": \"2026-05-15T02:02:45.338Z\", \"hypothesis\": \"v4 Random fixed-size ablation: 50% injection (4,358 total = 2,179 clean + 2,179 injected). 与 TaxEI 50% 对比 taxonomy 标签在高注入比例下是否有差异。\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/random_fixed_inject50/v0-20260515-084528/checkpoint-1635\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T01:39:15.464Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T01:39:17.014804+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"train_steps\": 1635, \"train_epochs\": 3, \"data_count\": 4358, \"train_loss\": 0.4338, \"final_step_loss\": 0.2618, \"token_accuracy\": 0.91, \"train_duration_min\": 53.1, \"memory_gib\": 18, \"train_speed_s_per_it\": 1.95}, \"completed_at\": \"2026-05-15T01:43:35.237Z\"}, \"v4-random-fixed-inject25\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T00:25:44.436Z\", \"updated_at\": \"2026-05-15T01:48:07.606Z\", \"hypothesis\": \"v4 Random fixed-size ablation: 25% injection (4,358 total). 与 TaxEI 25% (48.9%) 对比 taxonomy 标签在中等注入比例下是否有差异。\", \"spec\": {\"command\": \"swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/ablation_fixed/sft_random_v4_fixed_inject25.jsonl --lora_rank 16 --num_train_epochs 3 --seed 42 --output_dir checkpoints/v4_random_fixed_inject25 --gradient_accumulation_steps 8 --learning_rate 1e-4 --lr_scheduler_type cosine --gradient_checkpointing true --save_strategy epoch --logging_steps 5 --weight_decay 0.1 --adam_beta1 0.9 --adam_beta2 0.95\", \"server\": \"autodl-5090\", \"data_path\": \"data/mini_pipeline_v4/ablation_fixed/sft_random_v4_fixed_inject25.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"gpu\": \"cuda:1\", \"max_steps\": 1635, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_random_fixed_inject25/v1-20260515-084707/checkpoint-1635\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-fixed-inject25.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T01:43:59.432Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T01:44:03.491274+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"train_steps\": 1635, \"train_epochs\": 3, \"data_count\": 4358}, \"completed_at\": \"2026-05-15T01:48:05.171Z\"}, \"v4-random-fixed-inject10-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T01:28:17.994Z\", \"updated_at\": \"2026-05-15T01:42:40.302Z\", \"hypothesis\": \"v4 Random 10% injection fixed-size eval — 47 ALFWorld tasks (clean). 与 TaxEI 10% (61.7%) 对比。\", \"spec\": {\"command\": \"python3 eval/recovery.py --model_path /root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_random_fixed_inject10/v0-20260515-082828/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_random_fixed_inject10_eval.json --device cuda:2\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"110187\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-fixed-inject10-eval.log\", \"submitted_at\": \"2026-05-15T01:28:27.422Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"parent\": \"v4-random-fixed-inject10\", \"checkpoint_source\": \"v4-random-fixed-inject10\", \"eval_data\": \"47 ALFWorld tasks (clean, no injection)\", \"data_count\": 47, \"data_path\": \"eval/alfworld_47_clean\", \"model_name\": \"Qwen3-8B + LoRA (random fixed inject10)\", \"seed\": 42, \"wall_clock_seconds\": 852.9, \"gpu_hours\": 0.24}, \"parent\": \"v4-random-fixed-inject10\", \"metrics\": {\"eval_success_rate\": 0.681, \"eval_successes\": 32, \"eval_total\": 47, \"by_task\": {\"look_at_obj_in_light\": {\"total\": 6, \"success\": 5, \"rate\": 0.833}, \"pick_and_place_simple\": {\"total\": 8, \"success\": 5, \"rate\": 0.625}, \"pick_clean_then_place_in_recep\": {\"total\": 11, \"success\": 6, \"rate\": 0.545}, \"pick_cool_then_place_in_recep\": {\"total\": 7, \"success\": 4, \"rate\": 0.571}, \"pick_heat_then_place_in_recep\": {\"total\": 8, \"success\": 7, \"rate\": 0.875}, \"pick_two_obj_and_place\": {\"total\": 7, \"success\": 5, \"rate\": 0.714}}}, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_random_fixed_inject10_eval.json\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-fixed-inject10-eval.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T01:42:40.303Z\"}, \"v4-taxei-fixed-inject50-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T01:28:14.823Z\", \"updated_at\": \"2026-05-15T01:38:54.383Z\", \"spec\": {\"command\": \"python eval/recovery.py --model_path checkpoints/v4_taxei_fixed_inject50/v0-20260515-082759/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --num_episodes 47 --output eval_results/v4_taxei_fixed_inject50_eval.json --device cuda:0 --seed 42\", \"server\": \"autodl-5090\", \"data_path\": \"ALFWorld valid_unseen\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (v4-taxei-fixed-inject50)\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/v4_taxei_fixed_inject50/v0-20260515-082759/checkpoint-1635\", \"eval_data\": \"ALFWorld valid_unseen 47 tasks clean eval\"}, \"hypothesis\": \"v4 TaxEI fixed-size ablation: 50% injection eval — 47 tasks clean eval. Dose-response 最后一个数据点。已有：0%=61.7%, 10%=61.7%, 25%=48.9%, 50%=待测。\", \"metrics\": {\"eval_success_rate\": 0.511, \"eval_successes\": 24, \"eval_total\": 47, \"vs_vanilla_seed42_pp\": -10.6}, \"checkpoint_path\": \"checkpoints/v4_taxei_fixed_inject50/v0-20260515-082759/checkpoint-1635\", \"log_path\": \"/tmp/eval_inject50.log\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-15T01:37:38.792Z\"}, \"v4-random-fixed-inject10\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T00:25:41.996Z\", \"updated_at\": \"2026-05-15T01:31:01.715Z\", \"hypothesis\": \"v4 Random fixed-size ablation: 10% injection (4,358 total). 与 TaxEI 10% (61.7%) 对比 taxonomy 标签在低注入比例下是否有差异。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export CUDA_VISIBLE_DEVICES=2 && cd /root/autodl-tmp/tax_error_inject_agent && swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/ablation_fixed/sft_random_v4_fixed_inject10.jsonl --lora_rank 16 --num_train_epochs 3 --seed 42 --output_dir checkpoints/v4_random_fixed_inject10 --gradient_accumulation_steps 8 --learning_rate 1e-4 --lr_scheduler_type cosine --gradient_checkpointing true --save_strategy epoch --logging_steps 5 --weight_decay 0.1 --adam_beta1 0.9 --adam_beta2 0.95\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"104655\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-fixed-inject10.log\", \"submitted_at\": \"2026-05-15T00:28:19.537Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/mini_pipeline_v4/ablation_fixed/sft_random_v4_fixed_inject10.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_path\": \"checkpoints/v4_random_fixed_inject10/v0-20260515-082828/checkpoint-1635\", \"wall_clock_seconds\": 3546.1, \"gpu_hours\": 0.99}, \"reproduce\": {\"finished_at\": \"2026-05-15T01:26:29.568Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T01:26:31.003606+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.4226, \"final_step_loss\": 0.3079, \"token_accuracy\": 0.9, \"train_steps\": 1635, \"train_epochs\": 3, \"train_duration_min\": 57}, \"completed_at\": \"2026-05-15T01:27:25.646Z\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_random_fixed_inject10/v0-20260515-082828/checkpoint-1635\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-fixed-inject10.log\"}, \"v4-taxei-fixed-inject50\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T00:25:38.284Z\", \"updated_at\": \"2026-05-15T01:25:47.611Z\", \"hypothesis\": \"v4 TaxEI fixed-size ablation: 50% injection ratio (4,358 total = 2,179 clean + 2,179 injected). Dose-response 最后一个点，完成后有完整曲线 0%→10%→25%→50%。\", \"spec\": {\"command\": \"swift sft --model Qwen3-8B --dataset sft_taxei_v4_fixed_inject50.jsonl --lora_rank 16 --num_train_epochs 3 --seed 42 --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --learning_rate 1e-4\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"104236\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-fixed-inject50.log\", \"submitted_at\": \"2026-05-15T00:27:51.219Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject50.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_path\": \"checkpoints/v4_taxei_fixed_inject50/v0-20260515-082759/checkpoint-1635\", \"wall_clock_seconds\": 3476.4, \"gpu_hours\": 0.97}, \"reproduce\": {\"finished_at\": \"2026-05-15T01:22:23.688Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T01:22:25.093365+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.259, \"token_accuracy\": 0.911, \"train_steps\": 1635, \"train_epochs\": 3, \"train_duration_min\": 53.1}, \"completed_at\": \"2026-05-15T01:25:47.611Z\"}, \"v4-random-seed123-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T00:14:30.699Z\", \"updated_at\": \"2026-05-15T00:27:24.291Z\", \"hypothesis\": \"v4 Random SFT seed=123 eval — 47 tasks clean eval. Multi-seed: seed=42 66.0%, seed=0 55.3%, seed=123 待测。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export CUDA_VISIBLE_DEVICES=1 && cd /root/autodl-tmp/tax_error_inject_agent && python eval/recovery.py --model_path checkpoints/mini_random_sft_v4_seed123/v0-20260515-055925/checkpoint-3387 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_random_seed123_eval.json --device cuda:0\\\"\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"pid\": 102888, \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-seed123-eval.log\", \"submitted_at\": \"2026-05-15T00:14:42.930Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"eval/eval_tasks_47.json\", \"data_count\": 47, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"checkpoint_source\": \"checkpoints/mini_random_sft_v4_seed123/v0-20260515-055925/checkpoint-3387\", \"eval_data\": \"47 tasks clean eval (no injection)\", \"parent\": \"v4-random-seed123\", \"tmux_session\": \"v4-random-seed123-eval\", \"log_file\": \"~/runs/tax_error_inject_agent/v4-random-seed123-eval.log\", \"wall_clock_seconds\": 740.0, \"gpu_hours\": 0.21}, \"conclusion\": \"negative\", \"checkpoint_path\": \"checkpoints/mini_random_sft_v4_seed123/v0-20260515-055925/checkpoint-3387\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-seed123-eval.log\", \"completed_at\": \"2026-05-15T00:27:02.930Z\", \"metrics\": {\"eval_success_rate\": 0.681, \"eval_successes\": 32, \"eval_total\": 47, \"by_task\": {\"look_at_obj_in_light\": {\"total\": 6, \"success\": 5, \"rate\": 0.833}, \"pick_and_place_simple\": {\"total\": 8, \"success\": 5, \"rate\": 0.625}, \"pick_clean_then_place_in_recep\": {\"total\": 11, \"success\": 7, \"rate\": 0.636}, \"pick_cool_then_place_in_recep\": {\"total\": 7, \"success\": 4, \"rate\": 0.571}, \"pick_heat_then_place_in_recep\": {\"total\": 8, \"success\": 6, \"rate\": 0.75}, \"pick_two_obj_and_place\": {\"total\": 7, \"success\": 5, \"rate\": 0.714}}}}, \"v4-taxei-fixed-inject25-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T23:50:53.016Z\", \"updated_at\": \"2026-05-15T00:14:40.327Z\", \"hypothesis\": \"v4 TaxEI 25% injection fixed-size eval — 48.9% (23/47), 显著低于 vanilla baseline 65.3%（-16.4pp）。Dose-response 数据点。\", \"spec\": {\"command\": \"python3 eval/recovery.py --model_path output/v4-fixed-inject25/v0-20260515-063144/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_taxei_fixed_inject25_eval.json --device cuda:0\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"checkpoint_source\": \"output/v4-fixed-inject25/v0-20260515-063144/checkpoint-1635\", \"eval_data\": \"47 ALFWorld tasks (clean)\", \"parent\": \"v4-taxei-fixed-inject25-r2\", \"data_path\": \"eval/valid_unseen\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (taxei fixed inject25)\", \"seed\": 42}, \"metrics\": {\"eval_success_rate\": 0.489, \"eval_successes\": 23, \"eval_total\": 47, \"by_task\": {\"look_at_obj_in_light\": {\"success\": 4, \"total\": 6, \"rate\": 0.667}, \"pick_and_place_simple\": {\"success\": 3, \"total\": 8, \"rate\": 0.375}, \"pick_clean_then_place_in_recep\": {\"success\": 5, \"total\": 11, \"rate\": 0.455}, \"pick_cool_then_place_in_recep\": {\"success\": 2, \"total\": 7, \"rate\": 0.286}, \"pick_heat_then_place_in_recep\": {\"success\": 5, \"total\": 8, \"rate\": 0.625}, \"pick_two_obj_and_place\": {\"success\": 4, \"total\": 7, \"rate\": 0.571}}}, \"checkpoint_path\": \"eval_results/v4_taxei_fixed_inject25_eval.json\", \"log_path\": \"/tmp/v4_taxei_fixed_inject25_eval.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T00:14:30.429Z\"}, \"v4-taxei-fixed-inject10-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T23:50:52.584Z\", \"updated_at\": \"2026-05-15T00:14:38.874Z\", \"hypothesis\": \"v4 TaxEI 10% injection fixed-size eval — 61.7% (29/47), 低于 vanilla baseline 65.3%（-3.6pp）。Dose-response 数据点。\", \"spec\": {\"command\": \"python3 eval/recovery.py --model_path output/v4-fixed-inject10/v0-20260515-061243/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_taxei_fixed_inject10_eval.json --device cuda:0\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:2\", \"tmux_session\": \"eval_inject10\", \"checkpoint_source\": \"output/v4-fixed-inject10/v0-20260515-061243/checkpoint-1635\", \"eval_data\": \"47 ALFWorld tasks (clean)\", \"parent\": \"v4-taxei-fixed-inject10\", \"data_path\": \"eval/valid_unseen\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (taxei fixed inject10)\", \"seed\": 42, \"log_path\": \"/tmp/v4_taxei_fixed_inject10_eval.log\"}, \"metrics\": {\"eval_success_rate\": 0.617, \"eval_successes\": 29, \"eval_total\": 47, \"by_task\": {\"look_at_obj_in_light\": {\"success\": 5, \"total\": 6, \"rate\": 0.833}, \"pick_and_place_simple\": {\"success\": 5, \"total\": 8, \"rate\": 0.625}, \"pick_clean_then_place_in_recep\": {\"success\": 5, \"total\": 11, \"rate\": 0.455}, \"pick_cool_then_place_in_recep\": {\"success\": 4, \"total\": 7, \"rate\": 0.571}, \"pick_heat_then_place_in_recep\": {\"success\": 6, \"total\": 8, \"rate\": 0.75}, \"pick_two_obj_and_place\": {\"success\": 4, \"total\": 7, \"rate\": 0.571}}}, \"checkpoint_path\": \"eval_results/v4_taxei_fixed_inject10_eval.json\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T00:14:29.992Z\"}, \"v4-taxei-seed123-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T23:44:07.489Z\", \"updated_at\": \"2026-05-15T00:14:37.513Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 eval/recovery.py --model_path checkpoints/mini_taxei_sft_v4_seed123/v0-20260515-055026/checkpoint-3387 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_taxei_seed123_eval.json --device cuda:0\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"pid\": 100600, \"model_name\": \"Qwen3-8B + LoRA (taxei v4 seed=123)\", \"seed\": 123, \"checkpoint_source\": \"checkpoints/mini_taxei_sft_v4_seed123/v0-20260515-055026/checkpoint-3387\", \"eval_data\": \"47 ALFWorld tasks (clean, no injection)\", \"parent\": \"v4-taxei-seed123\", \"checkpoint_path\": \"eval_results/v4_taxei_seed123_eval.json\", \"log_path\": \"/tmp/v4_taxei_seed123_eval.log\", \"data_path\": \"eval/valid_unseen\", \"data_count\": 47}, \"hypothesis\": \"v4 TaxEI SFT seed=123 eval — 61.7% (29/47), 低于 vanilla baseline 65.3%（-3.6pp）。multi-seed verification, 9029 samples。\", \"metrics\": {\"eval_success_rate\": 0.617, \"eval_successes\": 29, \"eval_total\": 47, \"by_task\": {\"look_at_obj_in_light\": {\"success\": 5, \"total\": 6, \"rate\": 0.833}, \"pick_and_place_simple\": {\"success\": 4, \"total\": 8, \"rate\": 0.5}, \"pick_clean_then_place_in_recep\": {\"success\": 7, \"total\": 11, \"rate\": 0.636}, \"pick_cool_then_place_in_recep\": {\"success\": 3, \"total\": 7, \"rate\": 0.429}, \"pick_heat_then_place_in_recep\": {\"success\": 6, \"total\": 8, \"rate\": 0.75}, \"pick_two_obj_and_place\": {\"success\": 4, \"total\": 7, \"rate\": 0.571}}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T00:14:29.055Z\"}, \"v4-random-seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:49:34.441Z\", \"updated_at\": \"2026-05-14T23:52:15.056Z\", \"hypothesis\": \"v4 Random SFT seed=123 (P1 multi-seed补齐) — 9,029 samples, same hyperparams as seed=42/0, 配齐3-seed统计分析\", \"spec\": {\"command\": \"swift sft --model Qwen3-8B --dataset sft_random_v4.jsonl --seed 123 --lora_rank 16 --num_train_epochs 3\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"pid\": 93477, \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-seed123.log\", \"submitted_at\": \"2026-05-14T21:59:16.545Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/tax_error_inject_agent/data/mini_pipeline_v4/sft_random_v4.jsonl\", \"data_count\": 9029, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"wall_clock_seconds\": 6778.5, \"gpu_hours\": 1.88}, \"reproduce\": {\"finished_at\": \"2026-05-14T23:50:09.168Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T23:50:10.389568+00:00\"}]}, \"metrics\": {\"train_loss\": 0.35484016, \"final_loss\": 0.16766574, \"token_accuracy\": 0.94187103, \"avg_token_accuracy\": 0.90849673, \"train_steps\": 3387, \"train_epochs\": 3, \"train_runtime_sec\": 6609.3556, \"train_duration_min\": 110.2, \"train_samples_per_second\": 4.098, \"train_steps_per_second\": 0.512, \"train_speed_s_per_it\": 1.951, \"memory_gib\": 18.49}, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_random_sft_v4_seed123/v0-20260515-055925/checkpoint-3387\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T23:52:15.056Z\"}, \"v4-taxei-fixed-inject25-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:32:41.837Z\", \"updated_at\": \"2026-05-14T23:50:46.230Z\", \"hypothesis\": \"v4 TaxEI fixed-size ablation: 25% injection ratio retry (4,358 total = 3,268 clean + 1,090 injected). 修复 CUDA_VISIBLE_DEVICES，显式设 =3。\", \"spec\": {\"command\": \"export CUDA_VISIBLE_DEVICES=3 && swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject25.jsonl --output_dir checkpoints/taxei_fixed_inject25 --lora_rank 16 --lora_alpha 32 --lora_dropout 0.05 --target_modules all-linear --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --max_length 4096 --num_train_epochs 3 --learning_rate 1e-4 --seed 42 --torch_dtype bfloat16 --logging_steps 5 --save_strategy epoch --gradient_checkpointing true\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"pid\": 96835, \"data_path\": \"data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject25.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"injection_ratio\": 0.25, \"clean_count\": 3268, \"injected_count\": 1090, \"log_path\": \"/tmp/v4-fixed-inject25.log\", \"note\": \"manual tmux with explicit CUDA_VISIBLE_DEVICES=3, fixing r1 OOM\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"output/v4-fixed-inject25/v0-20260515-063144/checkpoint-1635\", \"metrics\": {\"final_loss\": 0.285, \"token_accuracy\": 0.893, \"train_steps\": 1635, \"train_epochs\": 3, \"train_duration_min\": 58}, \"completed_at\": \"2026-05-14T23:50:46.230Z\"}, \"v4-taxei-fixed-inject10\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:09:52.707Z\", \"updated_at\": \"2026-05-14T23:50:45.829Z\", \"hypothesis\": \"v4 TaxEI fixed-size ablation: 10% injection ratio (4,358 total = 3,922 clean + 436 injected). Fixed-size = vanilla 大小，控制数据量变量。Dose-response: 10%/25%/50%。\", \"spec\": {\"command\": \"swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset sft_taxei_v4_fixed_inject10.jsonl --output_dir output/v4-fixed-inject10 --num_train_epochs 3 --learning_rate 1e-4 --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --lora_rank 16 --lora_alpha 32 --lora_dropout 0.05 --seed 42 --data_seed 42 --bf16 true --gradient_checkpointing true\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"94635\", \"log_path\": \"/tmp/v4-fixed-inject10.log\", \"submitted_at\": \"2026-05-15T06:12:34Z\", \"submitted_via\": \"manual_tmux\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject10.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"injection_ratio\": 0.1, \"clean_count\": 3922, \"injected_count\": 436}, \"conclusion\": \"success\", \"checkpoint_path\": \"output/v4-fixed-inject10/v0-20260515-061243/checkpoint-1635\", \"metrics\": {\"final_loss\": 0.308, \"token_accuracy\": 0.888, \"train_steps\": 1635, \"train_epochs\": 3, \"train_duration_min\": 58}, \"completed_at\": \"2026-05-14T23:50:45.829Z\"}, \"v4-taxei-fixed-inject25\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:09:53.209Z\", \"updated_at\": \"2026-05-14T23:45:26.890Z\", \"hypothesis\": \"v4 TaxEI fixed-size ablation: 25% injection ratio (4,358 total = 3,268 clean + 1,090 injected). Fixed-size = vanilla 大小，控制数据量变量。Dose-response: 10%/25%/50%。\", \"spec\": {\"command\": \"swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset sft_taxei_v4_fixed_inject25.jsonl --output_dir output/v4-fixed-inject25 --num_train_epochs 3 --learning_rate 1e-4 --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --lora_rank 16 --lora_alpha 32 --lora_dropout 0.05 --seed 42 --data_seed 42 --bf16 true --gradient_checkpointing true\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"96835\", \"log_path\": \"/tmp/v4-fixed-inject25.log\", \"submitted_at\": \"2026-05-15T06:31:44Z\", \"submitted_via\": \"manual_tmux\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject25.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"injection_ratio\": 0.25, \"clean_count\": 3268, \"injected_count\": 1090, \"note\": \"r1 (PID 95170) OOM on cuda:0 — submit_training_job failed to pass CUDA_VISIBLE_DEVICES. Resubmitted manually via tmux with explicit export CUDA_VISIBLE_DEVICES=3.\"}, \"conclusion\": \"failed\", \"failure_reason\": \"CUDA_VISIBLE_DEVICES 未生效，模型加载到 cuda:0 导致 OOM（与 seed123 训练冲突）\", \"completed_at\": \"2026-05-14T23:45:26.890Z\"}, \"v4-taxei-seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:49:34.191Z\", \"updated_at\": \"2026-05-14T23:43:38.819Z\", \"hypothesis\": \"v4 TaxEI SFT seed=123 (P1 multi-seed补齐) — 9,029 samples, same hyperparams as seed=42/0, 配齐3-seed统计分析\", \"spec\": {\"command\": \"swift sft --model Qwen3-8B --dataset sft_taxei_v4.jsonl --seed 123 --lora_rank 16 --num_train_epochs 3\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"pid\": 92263, \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-seed123.log\", \"submitted_at\": \"2026-05-14T21:50:17.845Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/tax_error_inject_agent/data/mini_pipeline_v4/sft_taxei_v4.jsonl\", \"data_count\": 9029, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"wall_clock_seconds\": 6801.0, \"gpu_hours\": 1.89}, \"reproduce\": {\"finished_at\": \"2026-05-14T23:41:32.774Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T23:41:33.984355+00:00\"}]}, \"metrics\": {\"final_loss\": 0.35506879, \"token_accuracy\": 0.89978214, \"train_steps\": 3387, \"train_epochs\": 3, \"train_duration_min\": 109.2, \"train_runtime_sec\": 6549.432, \"train_speed_s_per_it\": 1.934, \"memory_gib\": 18.49}, \"checkpoint_path\": \"checkpoints/mini_taxei_sft_v4_seed123/v0-20260515-055026/checkpoint-3387\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T23:43:38.819Z\"}, \"v4-fixed-inject25\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:09:23.317Z\", \"updated_at\": \"2026-05-14T22:29:19.308Z\", \"spec\": {\"hypothesis\": \"Fixed-size ablation: 25% injection ratio (4,358 total samples, ~1,090 injected + ~3,269 clean). Tests intermediate injection ratio. Combined with 10%/50% results, reveals dose-response curve. Addresses Reviewer Concern #5.\", \"parent\": \"v4-taxei-eval\", \"plan_id\": \"fixed-size-ablation\", \"reviewer_concern\": \"RC5\"}, \"conclusion\": \"killed\", \"failure_reason\": \"duplicate entry — active experiment is v4-taxei-fixed-inject25 (RUNNING)\"}, \"v4-fixed-inject10\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:09:21.673Z\", \"updated_at\": \"2026-05-14T22:29:18.354Z\", \"spec\": {\"hypothesis\": \"Fixed-size ablation: 10% injection ratio (4,358 total samples, ~436 injected + ~3,922 clean). Tests whether low injection ratio still harms clean performance. If yes → injection itself is harmful regardless of ratio. Addresses Reviewer Concern #5.\", \"parent\": \"v4-taxei-eval\", \"plan_id\": \"fixed-size-ablation\", \"reviewer_concern\": \"RC5\"}, \"conclusion\": \"killed\", \"failure_reason\": \"duplicate entry — active experiment is v4-taxei-fixed-inject10 (RUNNING)\"}, \"v4-random-recovery-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:04:57.591Z\", \"updated_at\": \"2026-05-14T22:00:43.285Z\", \"hypothesis\": \"v4 Random SFT seed=42 recovery eval (injected_eval.py) — 47 episodes with error injection, measuring detection/recovery/success rates under P1/P2/C1/C4 operators. Phase 2 counterpart to vanilla/taxei recovery eval.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 eval/injected_eval.py --model_path checkpoints/mini_random_sft_v4/v1-20260514-213104/checkpoint-3387 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --model_variant random --num_episodes 47 --seed 42 --device cuda:0 --output eval_results/v4_random_recovery_eval.json\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"pid\": 90124, \"model_name\": \"Qwen3-8B + LoRA (random SFT v4)\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/mini_random_sft_v4/v1-20260514-213104/checkpoint-3387\", \"eval_data\": \"valid_unseen (47 episodes)\", \"log_path\": \"/tmp/v4_random_recovery_eval.log\", \"output_path\": \"eval_results/v4_random_recovery_eval.json\", \"data_path\": \"valid_unseen\", \"data_count\": 47}, \"conclusion\": \"success\", \"checkpoint_path\": \"eval_results/v4_random_recovery_eval.json\", \"completed_at\": \"2026-05-14T21:42:07.544Z\", \"metrics\": {\"recovery_rate\": 0.638, \"detection_rate\": 0, \"successes\": 30, \"total\": 47, \"source\": \"json-file-verified\", \"note\": \"r1=29/47, r2=30/47, ±2pp run-to-run variance on P1 non-determinism\"}}, \"v4-taxei-recovery-eval-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:23:55.110Z\", \"updated_at\": \"2026-05-14T21:46:19.993Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 eval/injected_eval.py --model_path checkpoints/mini_taxei_sft_v4/v1-20260514-213102/checkpoint-3387 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --model_variant taxei --num_episodes 47 --seed 42 --device cuda:0 --output eval_results/v4_taxei_recovery_eval_r2.json\", \"server\": \"autodl-5090\", \"model_name\": \"Qwen3-8B + LoRA (mini_taxei_sft_v4 checkpoint-3387)\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/mini_taxei_sft_v4/v1-20260514-213102/checkpoint-3387\", \"eval_data\": \"47 episodes with error injection (4 operators: C1_context_truncation, C4_observation_masking, P1_step_order_swap, P2_sub_goal_deletion)\", \"data_path\": \"eval/injected_eval.py\", \"data_count\": 47, \"hypothesis\": \"v4 TaxEI SFT seed=42 recovery eval retry — 47 episodes with error injection, measuring detection/recovery/success rates. Previous attempt reported process dead 5x.\", \"pid\": 90519, \"log_path\": \"/tmp/v4_taxei_recovery_eval_r2.log\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"eval_results/v4_taxei_recovery_eval_r2.json\", \"completed_at\": \"2026-05-14T21:42:08.000Z\", \"metrics\": {\"recovery_rate\": 0.596, \"detection_rate\": 0, \"total_episodes\": 47, \"per_operator\": {\"C1_context_truncation\": {\"recovered\": 8, \"total\": 12, \"rate\": 0.667}, \"C4_observation_masking\": {\"recovered\": 7, \"total\": 11, \"rate\": 0.636}, \"P1_step_order_swap\": {\"recovered\": 7, \"total\": 12, \"rate\": 0.583}, \"P2_sub_goal_deletion\": {\"recovered\": 6, \"total\": 12, \"rate\": 0.5}}}}, \"v4-taxei-seed0-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:30:26.278Z\", \"updated_at\": \"2026-05-14T21:21:53.154Z\", \"hypothesis\": \"v4 TaxEI SFT seed=0 eval — multi-seed verification, 9029 samples, testing TaxEI injection stability\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 eval/recovery.py --model_path checkpoints/mini_taxei_sft_v4_seed0/v0-20260515-014320/checkpoint-3387 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_taxei_seed0_eval.json --device cuda:0\", \"server\": \"autodl-5090\", \"data_path\": \"eval/valid_unseen\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (taxei v4 seed=0)\", \"seed\": 0, \"checkpoint_source\": \"checkpoints/mini_taxei_sft_v4_seed0/v0-20260515-014320/checkpoint-3387\", \"eval_data\": \"47 ALFWorld tasks (clean, no injection)\", \"parent\": \"v4-taxei-seed0\", \"checkpoint_path\": \"eval_results/v4_taxei_seed0_eval.json\", \"log_path\": \"eval_results/v4_taxei_seed0_eval.log\"}, \"conclusion\": \"success\", \"metrics\": {\"eval_success_rate\": 0.468, \"eval_successes\": 22, \"eval_total\": 47, \"vs_seed42_pp\": -14.9}, \"completed_at\": \"2026-05-14T21:20:13.351Z\"}, \"v4-random-seed0-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:30:26.456Z\", \"updated_at\": \"2026-05-14T21:21:52.271Z\", \"hypothesis\": \"v4 Random SFT seed=0 eval — multi-seed verification, 9029 samples, testing random injection stability\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python3 eval/recovery.py --model_path checkpoints/mini_random_sft_v4_seed0/v0-20260515-014329/checkpoint-3387 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_random_seed0_eval.json --device cuda:0\", \"server\": \"autodl-5090\", \"data_path\": \"eval/valid_unseen\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (random v4 seed=0)\", \"seed\": 0, \"checkpoint_source\": \"checkpoints/mini_random_sft_v4_seed0/v0-20260515-014329/checkpoint-3387\", \"eval_data\": \"47 ALFWorld tasks (clean, no injection)\", \"parent\": \"v4-random-seed0\", \"log_path\": \"eval_results/v4_random_seed0_eval.log\"}, \"conclusion\": \"success\", \"metrics\": {\"eval_success_rate\": 0.553, \"eval_successes\": 26, \"eval_total\": 47, \"vs_seed42_pp\": -10.7}, \"checkpoint_path\": \"eval_results/v4_random_seed0_eval.json\", \"completed_at\": \"2026-05-14T21:20:14.339Z\"}, \"v4-taxei-recovery-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:40:41.154Z\", \"updated_at\": \"2026-05-14T21:20:17.664Z\", \"spec\": {\"hypothesis\": \"D010 Phase 2: Recovery eval with action injection on TaxEI seed=42 checkpoint — measuring TaxEI-trained model's recovery ability vs vanilla\", \"command\": \"CUDA_VISIBLE_DEVICES=3 python3 eval/injected_eval.py --model_path /root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_taxei_sft_v4/v1-20260514-213102/checkpoint-3387 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --model_variant taxei --device cuda:0 --seed 42 --output eval_results/v4_taxei_recovery_eval.json\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"pid\": 87614, \"data_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_taxei_sft_v4/v1-20260514-213102/checkpoint-3387\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + TaxEI LoRA v4 checkpoint-3387\", \"seed\": 42, \"checkpoint_source\": \"mini_taxei_sft_v4/v1-20260514-213102/checkpoint-3387\", \"eval_data\": \"ALFWorld valid_unseen 47 tasks with action injection\", \"checkpoint_path\": \"eval_results/v4_taxei_recovery_eval.json\", \"log_path\": \"/root/runs/tax_error_inject_agent/v4-taxei-recovery-eval.log\"}, \"hypothesis\": \"v4 TaxEI SFT seed=42 recovery eval (injected_eval.py) — 47 episodes with error injection, measuring detection/recovery/success rates under P1/P2/C1/C4 operators. Phase 2 counterpart to vanilla recovery eval.\", \"reproduce\": {\"finished_at\": \"2026-05-14T20:58:38.335Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T20:58:38.665Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T20:58:39.601019+00:00\"}]}, \"metrics\": {\"success_rate\": 0.596, \"successes\": 28, \"total\": 47, \"recovery_rate\": 0.596, \"detection_rate\": 0}}, \"v4-vanilla-seed123-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:30:26.635Z\", \"updated_at\": \"2026-05-14T20:43:48.780Z\", \"hypothesis\": \"v4 Vanilla SFT seed=123 eval — multi-seed verification, 4358 samples, comparing with seed=42 baseline (61.7%)\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python3 eval/recovery.py --model_path checkpoints/mini_vanilla_sft_v4_seed123/v1-20260515-022602/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_vanilla_seed123_eval.json --device cuda:0\", \"server\": \"autodl-5090\", \"model_name\": \"Qwen3-8B + LoRA (vanilla v4 seed=123)\", \"seed\": 123, \"checkpoint_source\": \"checkpoints/mini_vanilla_sft_v4_seed123/v1-20260515-022602/checkpoint-1635\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_vanilla_sft_v4_seed123/v1-20260515-022602/checkpoint-1635\", \"log_path\": \"/tmp/v4_vanilla_seed123_eval.log\", \"eval_data\": \"47 ALFWorld tasks (clean, no injection)\", \"parent\": \"v4-vanilla-seed123\", \"data_path\": \"eval/valid_unseen\", \"data_count\": 47}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T20:37:11.382Z\", \"metrics\": {\"eval_success_rate\": 0.66, \"eval_successes\": 31, \"eval_total\": 47, \"vs_seed42_pp\": 4.3, \"vs_seed0_pp\": -2.1, \"per_task\": {\"look_at_obj_in_light\": {\"success\": 5, \"total\": 6, \"rate\": 0.833}, \"pick_and_place_simple\": {\"success\": 6, \"total\": 8, \"rate\": 0.75}, \"pick_clean_then_place_in_recep\": {\"success\": 5, \"total\": 11, \"rate\": 0.455}, \"pick_cool_then_place_in_recep\": {\"success\": 4, \"total\": 7, \"rate\": 0.571}, \"pick_heat_then_place_in_recep\": {\"success\": 7, \"total\": 8, \"rate\": 0.875}, \"pick_two_obj_and_place\": {\"success\": 4, \"total\": 7, \"rate\": 0.571}}}}, \"v4-random-seed0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:42:03.440Z\", \"updated_at\": \"2026-05-14T19:36:31.263Z\", \"hypothesis\": \"v4 Random SFT seed=0 (multi-seed verification) — 9,029 samples, same hyperparams as seed=42, testing result stability\", \"spec\": {\"data_path\": \"data/mini_pipeline_v4/sft_random_v4.jsonl\", \"data_count\": 9029, \"model_name\": \"Qwen3-8B\", \"seed\": 0, \"server\": \"autodl-5090\", \"command\": \"swift sft --model Qwen3-8B --dataset sft_random_v4.jsonl --seed 0\", \"gpu\": \"cuda:2\", \"pid\": 72303, \"log_path\": \"/root/runs/tax_error_inject_agent/v4-random-seed0.log\", \"checkpoint_path\": \"checkpoints/mini_random_sft_v4_seed0/v0-20260515-014329/checkpoint-3387\"}, \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.355, \"token_accuracy\": 0.912, \"train_steps\": 3387, \"train_epochs\": 3, \"train_duration_min\": 110}, \"completed_at\": \"2026-05-14T19:35:39.420Z\"}, \"v4-taxei-seed0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:42:02.696Z\", \"updated_at\": \"2026-05-14T19:36:29.716Z\", \"hypothesis\": \"v4 TaxEI SFT seed=0 (multi-seed verification) — 9,029 samples, same hyperparams as seed=42, testing result stability\", \"spec\": {\"data_path\": \"data/mini_pipeline_v4/sft_taxei_v4.jsonl\", \"data_count\": 9029, \"model_name\": \"Qwen3-8B\", \"seed\": 0, \"server\": \"autodl-5090\", \"command\": \"swift sft --model Qwen3-8B --dataset sft_taxei_v4.jsonl --seed 0\", \"gpu\": \"cuda:1\", \"pid\": 71822, \"log_path\": \"/root/runs/tax_error_inject_agent/v4-taxei-seed0.log\", \"checkpoint_path\": \"checkpoints/mini_taxei_sft_v4_seed0/v0-20260515-014320/checkpoint-3387\"}, \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.355, \"token_accuracy\": 0.917, \"train_steps\": 3387, \"train_epochs\": 3, \"train_duration_min\": 110}, \"completed_at\": \"2026-05-14T19:35:37.503Z\"}, \"v4-vanilla-seed0-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:30:26.093Z\", \"updated_at\": \"2026-05-14T19:30:45.170Z\", \"hypothesis\": \"v4 Vanilla SFT seed=0 eval — multi-seed verification, 4358 samples, comparing with seed=42 baseline (61.7%)\", \"spec\": {\"checkpoint_path\": \"eval_results/v4_vanilla_seed0_eval.json\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-vanilla-seed0-eval.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T19:01:19.696Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T19:01:20.697938+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"eval_success_rate\": 0.681, \"eval_successes\": 32, \"eval_total\": 47, \"vs_seed42_pp\": 6.4, \"mcnemar_vs_seed42_p\": 0.375, \"discordant_pairs\": 5, \"per_task\": {\"look_at_obj_in_light\": \"5/6 (83.3%)\", \"pick_and_place_simple\": \"5/8 (62.5%)\", \"pick_clean_then_place\": \"6/11 (54.5%)\", \"pick_cool_then_place\": \"4/7 (57.1%)\", \"pick_heat_then_place\": \"7/8 (87.5%)\", \"pick_two_obj_and_place\": \"5/7 (71.4%)\"}}, \"completed_at\": \"2026-05-14T19:29:37.198Z\"}, \"v4-vanilla-seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:45:23.836Z\", \"updated_at\": \"2026-05-14T19:29:24.021Z\", \"hypothesis\": \"D010 Phase 1: v4 Vanilla SFT seed=123 多种子验证 — 4,358 samples, LoRA rank=16, 3 epochs, 与 seed=42 的 61.7% 对比波动范围\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/sft_vanilla_v4.jsonl --output_dir checkpoints/mini_vanilla_sft_v4_seed123 --lora_rank 16 --lora_alpha 32 --lora_dropout 0.05 --target_modules all-linear --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --max_length 4096 --num_train_epochs 3 --learning_rate 1e-4 --seed 123 --torch_dtype bfloat16 --logging_steps 5 --save_strategy epoch --gradient_checkpointing true\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"pid\": 77937, \"log_path\": \"checkpoints/mini_vanilla_sft_v4_seed123/v1-20260515-022602/logging.jsonl\", \"submitted_at\": \"2026-05-14T18:20:42.388Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/mini_pipeline_v4/sft_vanilla_v4.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"checkpoint_path\": \"checkpoints/mini_vanilla_sft_v4_seed123\", \"note\": \"OOM on first attempt (v0), restarted as v1 with PID 77937\", \"wall_clock_seconds\": 3941.6, \"gpu_hours\": 1.09}, \"reproduce\": {\"finished_at\": \"2026-05-14T19:26:23.312Z\"}, \"failure_reason\": \"v0 OOM at model loading (GPU 3 occupied by another process, 18.21 GiB in use). v1 (PID 77937) actually completed 1635/1635 steps. Cron caught v0's EXIT_CODE=1. Verifying checkpoint validity...\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T19:26:23.949Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T19:26:24.909318+00:00\"}]}, \"metrics\": {\"final_loss\": 0.288, \"token_accuracy\": 0.903, \"train_steps\": 1635, \"train_epochs\": 3, \"train_duration_min\": 58.9}}, \"v4-vanilla-seed0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:42:01.929Z\", \"updated_at\": \"2026-05-14T18:46:58.919Z\", \"hypothesis\": \"D010 Phase 1: v4 Vanilla SFT seed=0 多种子验证 — 4,358 samples, LoRA rank=16, 3 epochs, 与 seed=42 的 61.7% 对比波动范围\", \"spec\": {\"data_path\": \"data/mini_pipeline_v4/sft_vanilla_v4.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 0, \"server\": \"autodl-5090\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && CUDA_VISIBLE_DEVICES=0 swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/sft_vanilla_v4.jsonl --output_dir checkpoints/mini_vanilla_sft_v4_seed0 --lora_rank 16 --lora_alpha 32 --lora_dropout 0.05 --target_modules all-linear --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --max_length 4096 --num_train_epochs 3 --learning_rate 1e-4 --seed 0 --torch_dtype bfloat16 --logging_steps 5 --save_strategy epoch --gradient_checkpointing true\", \"gpu\": \"cuda:0\", \"pid\": 71959, \"log_path\": \"checkpoints/mini_vanilla_sft_v4_seed0/v0-20260515-014317/logging.jsonl\", \"checkpoint_path\": \"checkpoints/mini_vanilla_sft_v4_seed0/v0-20260515-014317/checkpoint-1635\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T18:42:56.365Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T18:42:57.338365+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.297, \"avg_loss\": 0.416, \"token_accuracy\": 0.902, \"train_steps\": 1635, \"train_epochs\": 3, \"train_duration_min\": 58}, \"completed_at\": \"2026-05-14T18:45:18.121Z\"}, \"v4-recovery-eval-dev\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:42:04.153Z\", \"updated_at\": \"2026-05-14T18:15:59.630Z\", \"hypothesis\": \"Recovery eval pipeline development — inject errors during eval to test if TaxEI models recover better than random/vanilla (Option C from D009)\", \"conclusion\": \"success\", \"metrics\": {\"pipeline_files\": [\"eval/injected_eval.py\", \"scripts/run_injected_eval.sh\"], \"injected_eval_lines\": 463, \"dryrun_result\": \"PASS\", \"dryrun_detail\": \"vanilla checkpoint, 1 task, cuda:3, injected error recovered in 13 steps\"}}, \"v4-recovery-dryrun\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:45:26.420Z\", \"updated_at\": \"2026-05-14T18:15:56.604Z\", \"hypothesis\": \"D010 Phase 2 前置: Recovery eval --inject 模式 dry-run, 1-2 tasks 验证 pipeline 正常工作\", \"conclusion\": \"success\"}, \"v4-random-eval\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T16:25:02.397Z\", \"updated_at\": \"2026-05-14T17:31:46.657Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && CKPT=checkpoints/mini_random_sft_v4/v1-20260514-213104/checkpoint-3387 && test -f \\\\${CKPT}/adapter_config.json && echo 'adapter_config OK' || { echo 'ERROR: adapter_config.json missing'; exit 1; } && echo 'Using checkpoint: '\\\\$CKPT && CUDA_VISIBLE_DEVICES=1 python3 eval/recovery.py --model_path \\\\$CKPT --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_random_eval.json --device cuda:0\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"67837\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-eval.log\", \"submitted_at\": \"2026-05-14T16:25:02.357Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"v4 Random SFT eval — formal Gate 3b judgment, same-source 9,029 samples, checkpoint-3387\", \"conclusion\": \"negative\", \"metrics\": {\"eval_success_rate\": 0.66, \"eval_successes\": 31, \"eval_total\": 47, \"vs_vanilla_pp\": 4.3, \"vs_taxei_pp\": 4.3, \"mcnemar_vs_vanilla_p\": 0.754, \"per_task\": {\"look_at_obj_in_light\": \"6/6 (100%)\", \"pick_and_place_simple\": \"4/8 (50%)\", \"pick_clean_then_place\": \"6/11 (54.5%)\", \"pick_cool_then_place\": \"4/7 (57.1%)\", \"pick_heat_then_place\": \"7/8 (87.5%)\", \"pick_two_obj_and_place\": \"4/7 (57.1%)\"}}}, \"v4-taxei-eval\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T16:25:00.653Z\", \"updated_at\": \"2026-05-14T17:31:43.481Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && CKPT=checkpoints/mini_taxei_sft_v4/v1-20260514-213102/checkpoint-3387 && test -f \\\\${CKPT}/adapter_config.json && echo 'adapter_config OK' || { echo 'ERROR: adapter_config.json missing'; exit 1; } && echo 'Using checkpoint: '\\\\$CKPT && CUDA_VISIBLE_DEVICES=0 python3 eval/recovery.py --model_path \\\\$CKPT --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_taxei_eval.json --device cuda:0\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"67694\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-eval.log\", \"submitted_at\": \"2026-05-14T16:25:00.616Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"v4 TaxEI SFT eval — formal Gate 3a/3b judgment, same-source 9,029 samples, checkpoint-3387\", \"conclusion\": \"negative\", \"metrics\": {\"eval_success_rate\": 0.617, \"eval_successes\": 29, \"eval_total\": 47, \"vs_vanilla_pp\": 0, \"vs_random_pp\": -4.3, \"mcnemar_vs_vanilla_p\": 1, \"mcnemar_vs_random_p\": 0.754, \"gate_3a\": \"FAIL\", \"gate_3b\": \"FAIL\", \"gate_4\": \"PASS\", \"per_task\": {\"look_at_obj_in_light\": \"6/6 (100%)\", \"pick_and_place_simple\": \"5/8 (62.5%)\", \"pick_clean_then_place\": \"6/11 (54.5%)\", \"pick_cool_then_place\": \"3/7 (42.9%)\", \"pick_heat_then_place\": \"7/8 (87.5%)\", \"pick_two_obj_and_place\": \"2/7 (28.6%)\"}}}, \"traj_collect_500\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T06:45:21.504Z\", \"updated_at\": \"2026-05-14T16:28:02.238Z\", \"spec\": {\"command\": \"python collect_trajectories.py --target 500\", \"server\": \"autodl-5090\", \"data_path\": \"data/trajectories/\", \"data_count\": 575, \"model_name\": \"trajectory_collector\", \"seed\": 0, \"pid\": 11045, \"gpu\": \"none (CPU task)\", \"hypothesis\": \"GPT-5.2 可作为 teacher 在 ALFWorld 中收集高质量成功轨迹（预期成功率≥93%）\"}, \"metrics\": {\"successful_trajectories\": 501, \"failed_trajectories\": 213, \"total_attempts\": 714, \"success_rate\": 0.702, \"api_cost_usd\": 8.86, \"collection_time_sec\": 5245}, \"conclusion\": \"negative\", \"checkpoint_path\": \"data/trajectories/successful_trajectories.jsonl\", \"log_path\": \"/tmp/collect_500.log\", \"completed_at\": \"2026-05-14T12:21:11.941Z\"}, \"v4-vanilla-eval-r3\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T14:28:24.833Z\", \"updated_at\": \"2026-05-14T16:25:11.284Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && latest_run=\\\\$(ls -dt checkpoints/mini_vanilla_sft_v4/v0-*/ | head -1) && final_ckpt=\\\\$(ls -d \\\\\\\"\\\\${latest_run}\\\\\\\"checkpoint-* | sort -V | tail -1) && echo \\\\\\\"Using checkpoint: \\\\$final_ckpt\\\\\\\" && test -f \\\\\\\"\\\\${final_ckpt}/adapter_config.json\\\\\\\" && echo 'adapter_config.json OK' || { echo 'ERROR: adapter_config.json missing'; exit 1; } && CUDA_VISIBLE_DEVICES=0 python3 eval/recovery.py --model_path \\\\$final_ckpt --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_vanilla_eval.json --device cuda:0\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"62340\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-vanilla-eval-r3.log\", \"submitted_at\": \"2026-05-14T14:28:24.797Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"v4 Vanilla SFT eval r3 — dynamic checkpoint lookup with sort -V, adapter_config.json pre-check\", \"conclusion\": \"success\", \"metrics\": {\"eval_success_rate\": 0.617, \"eval_successes\": 29, \"eval_total\": 47, \"per_task\": {\"look_at_obj_in_light\": \"5/6 (83.3%)\", \"pick_heat_then_place\": \"6/8 (75.0%)\", \"pick_and_place_simple\": \"5/8 (62.5%)\", \"pick_cool_then_place\": \"4/7 (57.1%)\", \"pick_two_obj_and_place\": \"4/7 (57.1%)\", \"pick_clean_then_place\": \"5/11 (45.5%)\"}}}, \"v4-vanilla-eval-r2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T14:24:25.560Z\", \"updated_at\": \"2026-05-14T14:28:40.995Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && CUDA_VISIBLE_DEVICES=0 python3 eval/recovery.py --model_path checkpoints/mini_vanilla_sft_v4/v0-20260514-122641/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_vanilla_eval.json --device cuda:0\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"61793\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-vanilla-eval-r2.log\", \"submitted_at\": \"2026-05-14T14:24:25.523Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"v4 Vanilla SFT eval retry — fixed --device cuda:0 (was --gpu 0) + explicit checkpoint-1635\", \"conclusion\": \"failed\"}, \"v4-random-sft-r2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:30:55.117Z\", \"updated_at\": \"2026-05-14T14:24:56.155Z\", \"spec\": {\"pid\": \"58163\", \"actual_status\": \"training_in_progress\", \"gpu\": [\"cuda:3\"], \"server\": \"autodl-5090\", \"data_path\": \"data/mini_pipeline_v4/sft_random_v4.jsonl\", \"data_count\": 9029, \"model_name\": \"Qwen3-8B\", \"seed\": 42}, \"hypothesis\": \"v4 Random SFT retry (r2) — same-source 9,029 samples, formal Gate 3b. Previous run killed by SIGHUP.\", \"conclusion\": \"success\"}, \"v4-taxei-sft-r2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:30:52.865Z\", \"updated_at\": \"2026-05-14T14:24:54.288Z\", \"spec\": {\"pid\": \"58034\", \"actual_status\": \"training_in_progress\", \"gpu\": [\"cuda:2\"], \"server\": \"autodl-5090\", \"data_path\": \"data/mini_pipeline_v4/sft_taxei_v4.jsonl\", \"data_count\": 9029, \"model_name\": \"Qwen3-8B\", \"seed\": 42}, \"hypothesis\": \"v4 TaxEI SFT retry (r2) — same-source 9,029 samples, formal Gate 3a/3b. Previous run killed by SIGHUP.\", \"conclusion\": \"success\"}, \"v4-vanilla-eval\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T14:15:59.327Z\", \"updated_at\": \"2026-05-14T14:24:25.638Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && CKPT=\\\\$(find checkpoints/mini_vanilla_sft_v4 -name 'checkpoint-*' -type d | sort -t- -k2 -n | tail -1) && echo \\\\\\\"Using checkpoint: \\\\$CKPT\\\\\\\" && CUDA_VISIBLE_DEVICES=0 python3 eval/recovery.py --model_path \\\\$CKPT --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_vanilla_eval.json --gpu 0\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"61138\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-vanilla-eval.log\", \"submitted_at\": \"2026-05-14T14:15:59.291Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"v4 Vanilla SFT eval (4,358 samples, clean only) — v4 baseline for Gate 3a comparison\", \"conclusion\": \"failed\"}, \"v3-random-eval\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:26:26.315Z\", \"updated_at\": \"2026-05-14T14:15:26.311Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && CUDA_VISIBLE_DEVICES=1 python3 eval/recovery.py --model_path checkpoints/mini_random_sft_v3/*/checkpoint-3405 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v3_random.json --device cuda:0\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"55925\", \"log_path\": \"~/runs/tax_error_inject_agent/v3-random-eval.log\", \"submitted_at\": \"2026-05-14T13:26:53.024Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"v3 Random SFT eval on 47-task ALFWorld (format-aligned, initial signal before v4 formal judgment)\", \"metrics\": {\"eval_success_rate\": 0.511, \"eval_successes\": 24, \"eval_total\": 47, \"vs_baseline_pp\": 8.5, \"vs_vanilla_sft_pp\": -23.4}, \"conclusion\": \"negative\"}, \"v3-taxei-eval\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:26:24.552Z\", \"updated_at\": \"2026-05-14T14:15:25.974Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && CUDA_VISIBLE_DEVICES=0 python3 eval/recovery.py --model_path checkpoints/mini_taxei_sft_v3/*/checkpoint-2832 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v3_taxei.json --device cuda:0\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"55848\", \"log_path\": \"~/runs/tax_error_inject_agent/v3-taxei-eval.log\", \"submitted_at\": \"2026-05-14T13:26:51.905Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"v3 TaxEI SFT eval on 47-task ALFWorld (format-aligned, initial signal before v4 formal judgment)\", \"metrics\": {\"eval_success_rate\": 0.66, \"eval_successes\": 31, \"eval_total\": 47, \"vs_baseline_pp\": 23.4, \"vs_vanilla_sft_pp\": -8.5, \"per_task\": {\"look_at_obj_in_light\": \"5/6 (83.3%)\", \"pick_clean_then_place\": \"8/11 (72.7%)\", \"pick_heat_then_place\": \"6/8 (75.0%)\", \"pick_and_place_simple\": \"5/8 (62.5%)\", \"pick_two_obj_and_place\": \"4/7 (57.1%)\", \"pick_cool_then_place\": \"3/7 (42.9%)\"}}, \"conclusion\": \"negative\"}, \"v4-random-sft-r3\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:32:26.753Z\", \"updated_at\": \"2026-05-14T13:32:36.181Z\", \"spec\": {\"command\": \"bash -c \\\"trap '' HUP; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && CUDA_VISIBLE_DEVICES=3 swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/sft_random_v4.jsonl --output_dir checkpoints/mini_random_sft_v4 --lora_rank 16 --lora_alpha 32 --lora_dropout 0.05 --target_modules all-linear --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --max_length 4096 --num_train_epochs 3 --learning_rate 1e-4 --seed 42 --torch_dtype bfloat16 --logging_steps 5 --save_strategy epoch --gradient_checkpointing true\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"58826\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-sft-r3.log\", \"submitted_at\": \"2026-05-14T13:32:26.722Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"v4 Random SFT retry (r3) — added trap '' HUP to survive tmux cleanup. Same-source 9,029 samples.\"}, \"v4-taxei-sft-r3\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:32:24.446Z\", \"updated_at\": \"2026-05-14T13:32:34.819Z\", \"spec\": {\"command\": \"bash -c \\\"trap '' HUP; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && CUDA_VISIBLE_DEVICES=2 swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/sft_taxei_v4.jsonl --output_dir checkpoints/mini_taxei_sft_v4 --lora_rank 16 --lora_alpha 32 --lora_dropout 0.05 --target_modules all-linear --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --max_length 4096 --num_train_epochs 3 --learning_rate 1e-4 --seed 42 --torch_dtype bfloat16 --logging_steps 5 --save_strategy epoch --gradient_checkpointing true\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"58741\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-sft-r3.log\", \"submitted_at\": \"2026-05-14T13:32:24.415Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"v4 TaxEI SFT retry (r3) — added trap '' HUP to survive tmux cleanup. Same-source 9,029 samples.\"}, \"v4-random-sft\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:26:31.864Z\", \"updated_at\": \"2026-05-14T13:31:19.378Z\", \"spec\": {\"pid\": \"56765\", \"gpu_memory_mib\": 19159, \"gpu_util_pct\": 60}, \"hypothesis\": \"v4 Random SFT with same-source data (9,029 samples), formal Gate 3b judgment — only tag differs from v4-taxei\", \"conclusion\": \"failed\"}, \"v4-taxei-sft\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:26:29.177Z\", \"updated_at\": \"2026-05-14T13:31:18.431Z\", \"spec\": {\"pid\": \"56685\", \"gpu_memory_mib\": 30884, \"gpu_util_pct\": 94}, \"hypothesis\": \"v4 TaxEI SFT with same-source data (9,029 samples), formal Gate 3a/3b judgment\", \"conclusion\": \"failed\"}, \"mini-vanilla-sft-v4\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:14:26.614Z\", \"updated_at\": \"2026-05-14T13:27:05.003Z\", \"hypothesis\": \"Vanilla SFT baseline with aligned format (v4), for Gate 3a comparison\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/sft_vanilla_v4.jsonl --output_dir checkpoints/mini_vanilla_sft_v4/ --lora_rank 16 --lora_alpha 32 --lora_dropout 0.05 --target_modules all-linear --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --max_length 4096 --num_train_epochs 3 --learning_rate 1e-4 --seed 42 --torch_dtype bfloat16 --logging_steps 5 --save_strategy epoch --gradient_checkpointing true\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"50537\", \"log_path\": \"~/runs/tax_error_inject_agent/mini-vanilla-sft-v4.log\", \"submitted_at\": \"2026-05-14T12:14:32.528Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"success\"}, \"mini-random-sft-v3\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:13:19.635Z\", \"updated_at\": \"2026-05-14T13:27:04.310Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v3/sft_random_aligned.jsonl --output_dir checkpoints/mini_random_sft_v3/ --lora_rank 16 --lora_alpha 32 --lora_dropout 0.05 --target_modules all-linear --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --max_length 4096 --num_train_epochs 3 --learning_rate 1e-4 --seed 42 --torch_dtype bfloat16 --logging_steps 5 --save_strategy epoch --gradient_checkpointing true\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"45764\", \"log_path\": \"~/runs/tax_error_inject_agent/mini-random-sft-v3.log\", \"submitted_at\": \"2026-05-14T11:13:19.618Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"train_samples\": 9076, \"train_samples_clean\": 4176, \"train_samples_injected\": 4900, \"train_steps_total\": 3405, \"est_duration_min\": 110, \"format\": \"aligned_single_turn\"}, \"conclusion\": \"success\"}, \"mini-taxei-sft-v3\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:13:17.286Z\", \"updated_at\": \"2026-05-14T13:27:03.840Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v3/sft_taxei_aligned.jsonl --output_dir checkpoints/mini_taxei_sft_v3/ --lora_rank 16 --lora_alpha 32 --lora_dropout 0.05 --target_modules all-linear --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --max_length 4096 --num_train_epochs 3 --learning_rate 1e-4 --seed 42 --torch_dtype bfloat16 --logging_steps 5 --save_strategy epoch --gradient_checkpointing true\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"45621\", \"log_path\": \"~/runs/tax_error_inject_agent/mini-taxei-sft-v3.log\", \"submitted_at\": \"2026-05-14T11:13:17.271Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"train_samples\": 7545, \"train_samples_clean\": 4176, \"train_samples_injected\": 3369, \"train_steps_total\": 2832, \"est_duration_min\": 90, \"format\": \"aligned_single_turn\"}, \"conclusion\": \"success\"}, \"mini-vanilla-sft-v3\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:13:13.990Z\", \"updated_at\": \"2026-05-14T13:27:02.899Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v3/sft_vanilla_aligned.jsonl --output_dir checkpoints/mini_vanilla_sft_v3/ --lora_rank 16 --lora_alpha 32 --lora_dropout 0.05 --target_modules all-linear --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --max_length 4096 --num_train_epochs 3 --learning_rate 1e-4 --seed 42 --torch_dtype bfloat16 --logging_steps 5 --save_strategy epoch --gradient_checkpointing true\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"45478\", \"log_path\": \"~/runs/tax_error_inject_agent/mini-vanilla-sft-v3.log\", \"submitted_at\": \"2026-05-14T11:13:13.975Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"train_samples\": 4176, \"train_steps_total\": 1566, \"est_duration_min\": 58, \"format\": \"aligned_single_turn\"}, \"conclusion\": \"success\"}, \"v3-vanilla-eval\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:22:10.941Z\", \"updated_at\": \"2026-05-14T13:27:01.957Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && CUDA_VISIBLE_DEVICES=0 python3 eval/recovery.py --model_path /root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_vanilla_sft_v3/v0-20260514-191323/checkpoint-1566 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v3_vanilla.json --device cuda:0\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"51848\", \"log_path\": \"~/runs/tax_error_inject_agent/v3-vanilla-eval.log\", \"submitted_at\": \"2026-05-14T12:22:30.589Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.745, \"successes\": 35, \"total\": 47, \"vs_baseline_pp\": 31.9, \"vs_baseline\": \"42.6% → 74.5%\"}}, \"v4-vanilla-sft\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:14:57.794Z\", \"updated_at\": \"2026-05-14T12:22:10.869Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/sft_vanilla_v4.jsonl --output_dir checkpoints/v4_vanilla_sft/ --lora_rank 16 --lora_alpha 32 --lora_dropout 0.05 --target_modules all-linear --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --max_length 4096 --num_train_epochs 3 --learning_rate 1e-4 --seed 42 --torch_dtype bfloat16 --logging_steps 5 --save_strategy epoch --gradient_checkpointing true\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": 50972, \"log_path\": \"~/runs/tax_error_inject_agent/v4-vanilla-sft.log\", \"submitted_at\": \"2026-05-14T12:14:57.755Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"OOM - CUDA_VISIBLE_DEVICES not set, ran on wrong GPU (cuda:0 instead of cuda:3)\"}, \"conclusion\": \"failed\"}, \"vanilla_sft_aligned_v2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:05:05.459Z\", \"updated_at\": \"2026-05-14T11:05:05.459Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && CUDA_VISIBLE_DEVICES=2 swift sft \\\\\\n  --model /root/autodl-tmp/models/Qwen/Qwen3-8B \\\\\\n  --dataset data/mini_pipeline/sft_vanilla_aligned.jsonl \\\\\\n  --lora_rank 16 \\\\\\n  --lora_alpha 32 \\\\\\n  --lora_dropout 0.05 \\\\\\n  --target_modules all-linear \\\\\\n  --num_train_epochs 1 \\\\\\n  --learning_rate 1e-4 \\\\\\n  --per_device_train_batch_size 1 \\\\\\n  --gradient_accumulation_steps 16 \\\\\\n  --warmup_ratio 0.05 \\\\\\n  --seed 42 \\\\\\n  --max_length 4096 \\\\\\n  --gradient_checkpointing true \\\\\\n  --output_dir checkpoints/vanilla_sft_aligned \\\\\\n  --logging_steps 5 \\\\\\n  --logging_first_step true \\\\\\n  --save_strategy epoch \\\\\\n  --bf16 true \\\\\\n  --weight_decay 0.1 \\\\\\n  --adam_beta1 0.9 \\\\\\n  --adam_beta2 0.95 \\\\\\n  --max_grad_norm 1.0 \\\\\\n  --lr_scheduler_type cosine \\\\\\n  --optim adamw_torch_fused 2>&1\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"44492\", \"log_path\": \"~/runs/tax_error_inject_agent/vanilla_sft_aligned_v2.log\", \"submitted_at\": \"2026-05-14T11:05:05.434Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"vanilla_sft_aligned_v1\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:04:12.825Z\", \"updated_at\": \"2026-05-14T11:04:12.825Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && CUDA_VISIBLE_DEVICES=2 swift sft --config configs/sft_vanilla_aligned.yaml 2>&1\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"43894\", \"log_path\": \"~/runs/tax_error_inject_agent/vanilla_sft_aligned_v1.log\", \"submitted_at\": \"2026-05-14T11:04:12.812Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"mini-vanilla-sft\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T10:51:41.382Z\", \"updated_at\": \"2026-05-14T10:54:48.860Z\", \"hypothesis\": \"Vanilla trajectory SFT baseline for comparison with TaxEI\", \"spec\": {\"command\": \"python3 scripts/train_sft.py --data data/sft_data/vanilla_train.jsonl --output checkpoints/mini_vanilla_sft/ --model Qwen3-8B --lora_rank 16 --seed 42 --epochs 3 --lr 1e-4\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"pid\": \"41874\", \"log_path\": \"eval_results/mini_vanilla_clean.json\", \"submitted_at\": \"2026-05-14T10:54:31.029Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/sft_data/vanilla_train.jsonl\", \"data_count\": 278, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"hypothesis\": \"Vanilla SFT on clean trajectories as baseline for comparison\", \"checkpoint_path\": \"checkpoints/mini_vanilla_sft/v0-20260514-181708/checkpoint-54\", \"wall_clock_seconds\": 17.8, \"gpu_hours\": 0.0}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T10:54:20.210Z\", \"metrics\": {\"eval_success_rate\": 0.149, \"eval_successes\": 7, \"eval_total\": 47, \"vs_baseline_pp\": -27.7, \"per_task\": {\"look_at_obj_in_light\": \"0/6 (0%)\", \"pick_and_place_simple\": \"2/8 (25.0%)\", \"pick_clean_then_place\": \"2/11 (18.2%)\", \"pick_cool_then_place\": \"0/7 (0%)\", \"pick_heat_then_place\": \"3/8 (37.5%)\", \"pick_two_obj_and_place\": \"0/7 (0%)\"}, \"train_steps\": 54, \"train_duration_min\": 5}}, \"mini-taxei-sft\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T10:51:40.784Z\", \"updated_at\": \"2026-05-14T10:54:46.174Z\", \"hypothesis\": \"TaxEI injection + recovery SFT improves over vanilla SFT on ALFWorld 47-task eval\", \"spec\": {\"command\": \"python3 scripts/train_sft.py --data data/sft_data/taxei_train.jsonl --output checkpoints/mini_taxei_sft/ --model Qwen3-8B --lora_rank 16 --seed 42 --epochs 3 --lr 1e-4\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"pid\": \"41263\", \"log_path\": \"eval_results/mini_taxei_clean.json\", \"submitted_at\": \"2026-05-14T10:53:16.579Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/sft_data/taxei_train.jsonl\", \"data_count\": 278, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_path\": \"checkpoints/mini_taxei_sft/v0-20260514-181630/checkpoint-195\", \"hypothesis\": \"TaxEI error injection + recovery SFT improves over vanilla SFT and baseline\", \"wall_clock_seconds\": 63.1, \"gpu_hours\": 0.04}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T10:54:19.721Z\", \"metrics\": {\"eval_success_rate\": 0.447, \"eval_successes\": 21, \"eval_total\": 47, \"vs_baseline_pp\": 2.1, \"per_task\": {\"look_at_obj_in_light\": \"3/6 (50.0%)\", \"pick_and_place_simple\": \"2/8 (25.0%)\", \"pick_clean_then_place\": \"6/11 (54.5%)\", \"pick_cool_then_place\": \"1/7 (14.3%)\", \"pick_heat_then_place\": \"6/8 (75.0%)\", \"pick_two_obj_and_place\": \"3/7 (42.9%)\"}, \"train_steps\": 195, \"train_duration_min\": 16.3}}, \"vanilla-react-baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:20:00.119Z\", \"updated_at\": \"2026-05-14T10:54:35.171Z\", \"spec\": {\"command\": \"python3 eval/recovery.py --model_path /root/autodl-tmp/models/Qwen/Qwen3-8B --eval_split valid_unseen --no_inject (MAX_STEPS=50 hardcoded)\", \"server\": \"autodl-5090\", \"data_path\": \"ALFWorld valid_unseen (47/85 tasks, solvable=True filter, pick_and_place_with_movable_recep excluded 0/11)\", \"data_count\": 47, \"model_name\": \"Qwen3-8B (zero-shot, enable_thinking=False)\", \"seed\": 42, \"gpu\": \"cuda:1\", \"hypothesis\": \"Qwen3-8B zero-shot ReAct 在 ALFWorld valid_unseen 的基线成功率，作为 SFT 对比的 lower bound\", \"checkpoint_path\": \"N/A (zero-shot, no training)\", \"log_path\": \"/root/autodl-tmp/tax_error_inject_agent/eval_results/vanilla_react_baseline.json\"}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.426, \"total_tasks\": 47, \"successes\": 20, \"per_task_type\": {\"pick_heat_then_place\": {\"success\": 5, \"total\": 8, \"rate\": 0.625}, \"look_at_obj_in_light\": {\"success\": 3, \"total\": 6, \"rate\": 0.5}, \"pick_and_place_simple\": {\"success\": 4, \"total\": 8, \"rate\": 0.5}, \"pick_clean_then_place\": {\"success\": 5, \"total\": 11, \"rate\": 0.455}, \"pick_two_obj_and_place\": {\"success\": 3, \"total\": 7, \"rate\": 0.429}, \"pick_cool_then_place\": {\"success\": 0, \"total\": 7, \"rate\": 0}}}, \"completed_at\": \"2026-05-14T08:58:00.892Z\"}, \"mini-pipeline-e2e\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T10:39:15.654Z\", \"updated_at\": \"2026-05-14T10:39:15.654Z\", \"conclusion\": \"failed\"}, \"sft-dryrun-73\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:19:34.694Z\", \"updated_at\": \"2026-05-14T08:20:00.752Z\", \"spec\": {\"command\": \"swift sft --config configs/sft_vanilla.yaml (dry-run, 1 epoch, bs=1, max_length=2048)\", \"server\": \"autodl-5090\", \"data_path\": \"data/trajectories/ (124 successful trajectories)\", \"data_count\": 124, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"gpu\": \"cuda:0\", \"hypothesis\": \"SFT pipeline 端到端验证：注入→格式化→训练流程是否正常工作\", \"checkpoint_path\": \"checkpoints/dryrun_sft_v2/v0-20260514-161410/checkpoint-8/\", \"log_path\": \"checkpoints/dryrun_sft_v2/v0-20260514-161410/\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T08:19:52.165Z\", \"metrics\": {\"train_loss_init\": 2.436, \"train_loss_final\": 1.543, \"train_loss_avg\": 1.894, \"peak_memory_gib\": 19.22, \"steps\": 8, \"duration_sec\": 42, \"data_vanilla\": 124, \"data_injected_dryrun\": 96, \"injected_failed\": 4}}}, \"count\": 167, \"total\": 167, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.396}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — Bash · `toolu_01JyYHCaF6Daamu8jHATuwpB`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/edd9b099-6670-4002-8cb5-5695fd3b3d77/tool-results/mcp-agent-ml-research-read_registry-1778932612722.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\nfor k, v in exps.items():\n    if 'llama31-taxei-s0' in k:\n        print(json.dumps({k: v}, indent=2))\n\"",
  "description": "Extract llama31-taxei-s0 from registry dump"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "edd9b099-6670-4002-8cb5-5695fd3b3d77",
  "uuid": "cadbaaaf-bcd6-40f9-802d-fdf21d5dd172",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012KJCtGs4gMinZEfbaVYWzP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 633,
      "cache_read_input_tokens": 32231,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 633
      },
      "output_tokens": 54,
      "service_tier": "standard",
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

_source line 31 · 2026-05-16T11:56:58.173Z_

<details><summary>↩ Tool result · `toolu_01JyYHCaF6Daamu8jHATuwpB`</summary>

```text
{
  "llama31-taxei-s0": {
    "status": "RUNNING",
    "retry_count": 0,
    "created_at": "2026-05-16T09:15:57.399Z",
    "updated_at": "2026-05-16T10:48:32.797Z",
    "spec": {
      "command": "CUDA_VISIBLE_DEVICES=1 swift sft --model Meta-Llama-3.1-8B-Instruct --dataset sft_taxei_v4.jsonl --output_dir output/llama31-taxei-s0 --lora_rank 16 --num_train_epochs 3 --seed 0",
      "server": "autodl-5090",
      "gpu": [
        "cuda:1"
      ],
      "pid": "262833",
      "log_path": "~/runs/tax_error_inject_agent/llama31-taxei-s0.log",
      "submitted_at": "2026-05-16T09:15:57.070Z",
      "submitted_via": "manual_retry_v1",
      "backend": "interactive_pts",
      "account": "root",
      "data_path": "/root/autodl-tmp/tax_error_inject_agent/data/mini_pipeline_v4/sft_taxei_v4.jsonl",
      "data_count": 9029,
      "model_name": "Meta-Llama-3.1-8B-Instruct",
      "seed": 0,
      "hypothesis": "Cross-model: LLaMA TaxEI s0 - 2nd seed for 3-seed cross-model validation"
    },
    "reproduce": {
      "finished_at": "2026-05-16T10:20:07.409Z"
    },
    "failure_reason": null,
    "conclusion": "failed",
    "extra": {
      "hook_events": [
        {
          "event": "on_failed",
          "action": "agent",
          "ts": "2026-05-16T10:20:11.090300+00:00"
        }
      ]
    }
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
  "session_id": "edd9b099-6670-4002-8cb5-5695fd3b3d77",
  "uuid": "280e3154-1962-444a-a082-36b220ff1248",
  "tool_use_result": {
    "stdout": "{\n  \"llama31-taxei-s0\": {\n    \"status\": \"RUNNING\",\n    \"retry_count\": 0,\n    \"created_at\": \"2026-05-16T09:15:57.399Z\",\n    \"updated_at\": \"2026-05-16T10:48:32.797Z\",\n    \"spec\": {\n      \"command\": \"CUDA_VISIBLE_DEVICES=1 swift sft --model Meta-Llama-3.1-8B-Instruct --dataset sft_taxei_v4.jsonl --output_dir output/llama31-taxei-s0 --lora_rank 16 --num_train_epochs 3 --seed 0\",\n      \"server\": \"autodl-5090\",\n      \"gpu\": [\n        \"cuda:1\"\n      ],\n      \"pid\": \"262833\",\n      \"log_path\": \"~/runs/tax_error_inject_agent/llama31-taxei-s0.log\",\n      \"submitted_at\": \"2026-05-16T09:15:57.070Z\",\n      \"submitted_via\": \"manual_retry_v1\",\n      \"backend\": \"interactive_pts\",\n      \"account\": \"root\",\n      \"data_path\": \"/root/autodl-tmp/tax_error_inject_agent/data/mini_pipeline_v4/sft_taxei_v4.jsonl\",\n      \"data_count\": 9029,\n      \"model_name\": \"Meta-Llama-3.1-8B-Instruct\",\n      \"seed\": 0,\n      \"hypothesis\": \"Cross-model: LLaMA TaxEI s0 - 2nd seed for 3-seed cross-model validation\"\n    },\n    \"reproduce\": {\n      \"finished_at\": \"2026-05-16T10:20:07.409Z\"\n    },\n    \"failure_reason\": null,\n    \"conclusion\": \"failed\",\n    \"extra\": {\n      \"hook_events\": [\n        {\n          \"event\": \"on_failed\",\n          \"action\": \"agent\",\n          \"ts\": \"2026-05-16T10:20:11.090300+00:00\"\n        }\n      ]\n    }\n  }\n}",
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

_source line 32_

<details><summary>Logged reasoning block</summary>

```text
Now I can see the issue. The registry shows `conclusion: "failed"` and there's a `reproduce.finished_at` timestamp. But the process is actually still running. The on_failed hook was triggered at 10:20:11, but the process is still alive and training at 75% progress.

This is a false failure detection. The monitor probably checked at 10:20 and thought the process had died, but it's clearly still running. I need to:
1. Clear the conclusion (but registry won't accept null)
2. Maybe I can set the conclusion to something else, or update other fields

Let me try updating the `conclusion` field. 

Since the API only accepts specific conclusion values and won't let me clear it back to running, I'm realizing there's no way to fix this through the registry API itself. The status field is already set to RUNNING, which creates this contradiction where the process is actively running but marked as failed. I should just report this discrepancy to the user and let them decide on the best resolution.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "edd9b099-6670-4002-8cb5-5695fd3b3d77",
  "uuid": "7ac909ee-0d04-404e-b448-796e08d9d444",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VzxZjvZi4mSTzMEp72g2YS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 828,
      "cache_read_input_tokens": 32864,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 828
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

Registry 不支持将 conclusion 清回 null。当前状态矛盾无法通过 API 修复（status=RUNNING + conclusion=failed）。

## 诊断结论：**RUNNING** ✓

| 指标 | 值 |
|------|-----|
| 进度 | step 2548/3387 (75%), epoch ~2.25/3 |
| 运行时间 | 1h38m |
| loss | ~0.32 |
| token_acc | ~0.88 |
| GPU 利用率 | cuda:1, 26GB/32GB, 99% util |
| checkpoint | 2个已保存 (v0, v1) |
| 预计完成 | ~32 分钟后 |

**失败标记原因**：`reproduce.finished_at` 在 10:20:07 被设置，触发了 on_failed hook。但进程实际从未中断——可能是监控脚本误判（提交时间 09:15，10:20 时训练约 1h 处于正常状态）。

**Registry 问题**：conclusion 字段不支持 null 值，无法清除误报的 `failed` 标记。训练完成后会自然更新为 `success`/需要手动更新。建议训练结束后直接 `update_registry conclusion=success`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "edd9b099-6670-4002-8cb5-5695fd3b3d77",
  "uuid": "fc57f2e3-6b53-410b-9244-27d1f3d4201c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VzxZjvZi4mSTzMEp72g2YS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 828,
      "cache_read_input_tokens": 32864,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 828
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

### Task result

_source line 34_

Registry 不支持将 conclusion 清回 null。当前状态矛盾无法通过 API 修复（status=RUNNING + conclusion=failed）。

## 诊断结论：**RUNNING** ✓

| 指标 | 值 |
|------|-----|
| 进度 | step 2548/3387 (75%), epoch ~2.25/3 |
| 运行时间 | 1h38m |
| loss | ~0.32 |
| token_acc | ~0.88 |
| GPU 利用率 | cuda:1, 26GB/32GB, 99% util |
| checkpoint | 2个已保存 (v0, v1) |
| 预计完成 | ~32 分钟后 |

**失败标记原因**：`reproduce.finished_at` 在 10:20:07 被设置，触发了 on_failed hook。但进程实际从未中断——可能是监控脚本误判（提交时间 09:15，10:20 时训练约 1h 处于正常状态）。

**Registry 问题**：conclusion 字段不支持 null 值，无法清除误报的 `failed` 标记。训练完成后会自然更新为 `success`/需要手动更新。建议训练结束后直接 `update_registry conclusion=success`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 67706,
  "duration_api_ms": 66960,
  "num_turns": 12,
  "stop_reason": "end_turn",
  "session_id": "edd9b099-6670-4002-8cb5-5695fd3b3d77",
  "total_cost_usd": 0.32420625000000003,
  "usage": {
    "input_tokens": 17,
    "cache_creation_input_tokens": 21851,
    "cache_read_input_tokens": 249521,
    "output_tokens": 2446,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 21851,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 727,
        "cache_read_input_tokens": 32864,
        "cache_creation_input_tokens": 828,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 828
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1522,
      "outputTokens": 24,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001642,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 17,
      "outputTokens": 2446,
      "cacheReadInputTokens": 249521,
      "cacheCreationInputTokens": 21851,
      "webSearchRequests": 0,
      "costUSD": 0.32256425,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "de3ef0f1-d8e3-4d06-a7ff-efc12f8d78c7"
}
```

</details>

---
