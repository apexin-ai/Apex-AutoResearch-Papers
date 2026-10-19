# deploy bjb1 18228 goal evals 20260524T070835 retry1

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 101
- **Recorded user turns:** 0
- **Tool calls:** 35
- **Original source:** `logs/workers/worker_deploy_bjb1-18228-goal-evals_20260524T070835_retry1.log`
- **Structured JSON:** [`376a8390b31a971d60a4.json`](../../sessions/37/376a8390b31a971d60a4.json)

## Before a recorded user message

101 recorded events

### System

_source line 1_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement",
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
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
  "uuid": "3f772a6b-ec06-45e7-a5a2-fdee0a516269",
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
    "status": "allowed",
    "resetsAt": 1779610200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "4c0cdbe3-d549-4ae1-9d33-6d4eb24eed2f",
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de"
}
```

---

### Assistant

_source line 3_

<details><summary>Logged reasoning block</summary>

```text
Let me start by checking the environment and registry status as instructed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "d9c511f5-9087-4739-9301-8aefd5c7a4b8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015oxPNq5NNZBCz5fpYf2Cdb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11588,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11588
      },
      "output_tokens": 20,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01SigBLz4mhM8sdn82pbnBu3`</summary>

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
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "8fd3af78-1b1c-40fb-9a82-d0b7de387f29",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015oxPNq5NNZBCz5fpYf2Cdb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11588,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11588
      },
      "output_tokens": 20,
      "service_tier": "standard",
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

_source line 5 · 2026-05-24T07:09:24.588Z_

<details><summary>↩ Tool result · `toolu_01SigBLz4mhM8sdn82pbnBu3`</summary>

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
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "ff065721-3b11-4e42-bd77-6080d3b34e80",
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

_source line 6_

<details><summary>Logged reasoning block</summary>

```text
Let me start by checking the GPU status and registry in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "da6df778-d112-4cac-bb08-1505c3f8ca81",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ku7kBHhPdGUX5UqTCZ6LWv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1538,
      "cache_read_input_tokens": 23429,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1538
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

### Assistant

_source line 7_

Step 1: 检查 GPU 状态和 registry。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "3a303623-592d-4355-a2a9-0e74251e745b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ku7kBHhPdGUX5UqTCZ6LWv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1538,
      "cache_read_input_tokens": 23429,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1538
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

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01KXLn7VcXJVb4DLCVqKF3gF`</summary>

```json
{
  "server": "bjb2-40593",
  "command": "nvidia-smi --query-gpu=index,memory.used,memory.total,utilization.gpu --format=csv,noheader",
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
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "af0e8847-efe9-4651-850d-2de1642bd33d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ku7kBHhPdGUX5UqTCZ6LWv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1538,
      "cache_read_input_tokens": 23429,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1538
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

_source line 9_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01Q7Q1TXG5Q13NB7UBEJQfZ7`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": {
    "status": "DONE"
  },
  "limit": 0,
  "fields": [
    "exp_id",
    "status",
    "conclusion"
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
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "9e90039c-5107-46ff-a937-992a62a254b2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ku7kBHhPdGUX5UqTCZ6LWv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1538,
      "cache_read_input_tokens": 23429,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1538
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

_source line 10 · 2026-05-24T07:09:30.177Z_

<details><summary>↩ Tool result · `toolu_01KXLn7VcXJVb4DLCVqKF3gF`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, 6006 MiB, 24564 MiB, 12 %\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.32}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "c4c41962-c6bf-4e7d-9ba4-a28cd51f125f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"0, 6006 MiB, 24564 MiB, 12 %\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.32}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"0, 6006 MiB, 24564 MiB, 12 %\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.32}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-24T07:09:34.899Z_

<details><summary>↩ Tool result · `toolu_01Q7Q1TXG5Q13NB7UBEJQfZ7`</summary>

```text
Error: result (67,801 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/b9aee3ed-8d14-48d4-b3e0-dcc629fa78de/tool-results/mcp-agent-ml-research-read_registry-1779606574868.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/b9aee3ed-8d14-48d4-b3e0-dcc629fa78de/tool-results/mcp-agent-ml-research-read_registry-1779606574868.txt in sequential chunks until 100% of the content has been read.
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
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "382c9691-b275-4985-b073-c6f7c9c93faa",
  "tool_use_result": {
    "content": "Error: result (67,801 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/b9aee3ed-8d14-48d4-b3e0-dcc629fa78de/tool-results/mcp-agent-ml-research-read_registry-1779606574868.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/b9aee3ed-8d14-48d4-b3e0-dcc629fa78de/tool-results/mcp-agent-ml-research-read_registry-1779606574868.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval-supp-long-k2mean-s46-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-long-reconvla-s46-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-long-crm-norm005-s46-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-long-adapt-tau025-s46-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-obj-crm-norm005-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-obj-adapt-tau025-s45\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-obj-vla-only-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-crm-norm005-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-vla-only-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-pi05-goal-2048-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-vla-only-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-pi05-spatial-2048-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-smolvla-goal-bjb1-32546\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-goal-vla-only-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-reconvla-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-train-pi05-spatial-full\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm003-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-spatial-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p90-seed44-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-vla-only-wrapper-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-reconvla-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-k2mean-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-long-seed42-r4\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-reconvla-obj-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-k2mean-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-k2mean-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-adapt-tau025-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-crm-norm005-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-adapt-tau025-s45-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-k2mean-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-vla-only-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-reconvla-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-adapt-tau025-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-crm-norm005-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-crm-norm005-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-adapt-tau025-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-vla-only-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-reconvla-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-k2mean-s45\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-adapt-tau025-obj-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-obj-k2mean-s45\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-crm-obj-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-k2mean-s44\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-long-reconvla-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-reconvla-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-vla-only-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-obj-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-crm-norm005-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-obj-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-reconvla-obj-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-adapt-tau025-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-crm-norm005-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-adapt-tau025-s44\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-k2mean-obj-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-k2mean-obj-s45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-obj-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-vla-only-s43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-long-k2mean-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-obj-vla-only-s46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-vla-only-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-k2mean-s43\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-long-reconvla-s43\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-long-crm-norm005-s43\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-long-adapt-tau025-s43\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-obj-adapt-tau025-s45-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-long-crm-norm005-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-long-adapt-tau025-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-reconvla-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-ablation-tau040-goal-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-ablation-tau015-goal-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-k2mean-object-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-ablation-tau010-goal-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-obj-reconvla-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-vla-only-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-vla-only-wrapper-s44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-k2mean-spatial-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-spatial-vla-only-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-k2mean-goal-s44\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-adapt-tau025-obj-s44\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-crm-norm005-obj-s44\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-goal-vla-only-wrapper-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-long-vla-only-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-reconvla-s44\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-obj-reconvla-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-goal-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-k2mean-object-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-k2mean-goal-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-goal-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-obj-s43\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-adapt-tau025-goal-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-goal-s43\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-adapt-tau025-obj-s43\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-goal-reconvla-s43\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-k2mean-spatial-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-reconvla-spatial-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-reconvla-spatial-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-k2mean-goal-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-k2mean-object-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-adapt-tau025-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-crm005-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-goal-reconvla-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"train-crm-unified-4suite-r6\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-goal-vla-only-wrapper-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-obj-adapt-tau025-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-k2mean-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-supp-crm-norm005-spatial-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-spatial-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-reconvla-k2-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-spatial-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-crm-norm005-spatial-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-k2mean-goal-s42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-supp-obj-adapt-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-object-vla-only-wrapper-s44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-object-vla-only-wrapper-s43-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-object-vla-only-wrapper-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-obj-reconvla-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-obj-crm005-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-adapt-tau035-spatial-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-adapt-tau015-spatial-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-crm-norm02-spatial-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-supp-adapt-tau025-spatial-s42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-openvla-object-baseline-seed42-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm02-seed55\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-pi05-features-object\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-smolvla-goal-shard2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-smolvla-goal-shard1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-smolvla-goal-shard0\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-long-seed2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-long-seed1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-long-seed0\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-spatial-seed42-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-spatial-seed43-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-spatial-seed44-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-goal-seed42-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-goal-seed43-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-goal-seed44-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-obj-adapt-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-crm-norm02-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-adaptive-tau015-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-adaptive-tau025-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-adaptive-tau035-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"train-crm-unified-4suite-r5-resumed\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-object-vla-only-wrapper-s44\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-object-vla-only-wrapper-s43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-object-vla-only-wrapper-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-obj-crm005-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-adapt-tau035-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-adapt-tau025-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-adapt-tau015-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-supp-crm-norm02-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-3dir-adaptive-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-3dir-norm03-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-3dir-reconvla-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-3dir-norm01-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-3dir-norm005-spatial-s42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-pi05-goal-2048\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"precompute-pi05-spatial-2048\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"precompute-pi05-object-2048\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-smolvla-crm-object-seed43-v1\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-smolvla-crm-object-seed42-v1\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-smolvla-crm-object-seed44-v1\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"train-crm-unified-4suite-r5\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-goal-seed43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-goal-seed42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-spatial-seed44\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-spatial-seed43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-spatial-seed42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-pi05-long-2048\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-lerobot-goal-seed44-v3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-smolvla-lerobot-goal-seed43-v3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-smolvla-lerobot-spatial-seed43-v3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train-crm-smolvla-3suite-v1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-smolvla-lerobot-goal-seed43-v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-smolvla-lerobot-spatial-seed43-v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-smolvla-lerobot-object-seed44-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-smolvla-lerobot-object-seed43-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-smolvla-lerobot-goal-seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-smolvla-lerobot-spatial-seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-smolvla-lerobot-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-smolvla-lerobot-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-smolvla-lerobot-spatial-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-smolvla-long-wrapper-bjb1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-smolvla-lerobot-long-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-smolvla-lerobot-long-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-smolvla-lerobot-long-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train-crm-unified-4suite-r4\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-pi05-vla-only-long-seed42-r4-rerun\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-crm-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-crm-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-crm-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-long-seed43-r4-std\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-goal-seed44-r4-std\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-goal-seed42-r4-std\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-long-seed44-r4-std\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-goal-seed43-r4-std\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-goal-seed42-r4\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-smolvla-long-k2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"train-crm-unified-4suite-r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"train-crm-unified-4suite-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-smolvla-goal-bjb2-28827\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-smolvla-long-bjb2-28827\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-spatial-seed44-r4\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-spatial-seed43-r4\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-spatial-seed42-r4\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-long-seed44-r4\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-long-seed43-r4\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-goal-seed44-r4\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-goal-seed43-r4\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-openvla-oft-official-object\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-pi05-crm-spatial-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-pi05-crm-spatial-seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-pi05-crm-spatial-seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-pi05-vla-only-object-seed43-r4\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-seed44-r4\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-smolvla-lerobot-official-object\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-seed42-r4\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train-crm-unified-4suite\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"precompute-smolvla-long-bjb1-32546-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-smolvla-long-bjb1-32546\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-loss-perdof-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-loss-combined-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-loss-conformal-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-loss-mse-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-openvla-oft-object-baseline-seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"precompute-smolvla-long-bjb1-18228\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-loss-combined\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"crm-loss-conformal\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"precompute-smolvla-goal-bjb1-18228\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-loss-perdof\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-loss-mse-baseline\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-smolvla-acr-goal-seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-smolvla-crm-long-seed44-v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-goal-seed44-v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-crm-long-seed43-v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-smolvla-acr-long-seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-smolvla-acr-goal-seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"crm-train-pi05-spatial-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-train-pi05-object-full\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-train-pi05-spatial\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"crm-train-pi05-object\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-pi05-vla-only-spatial-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-spatial-seed43-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-spatial-seed42-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-seed44-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-seed43-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-object-seed42-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-spatial-obs-only-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-vla-only-spatial-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-pi05-vla-only-spatial-seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-pi05-vla-only-spatial-seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-k20-obs-only-spatial-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k20-obs-only-spatial-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k20-obs-only-spatial-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k20-obs-only-object-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed66\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed66\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed66\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed67\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k20-obs-only-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k20-obs-only-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k20-obs-only-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-object-k20-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-object-k20-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed53\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed52\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed51\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed50\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed48-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed43-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed43-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed67\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed67\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-object-seed50\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-object-seed49\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-object-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-object-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-object-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-object-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-plan-a-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-object\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-plan-a-spatial-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-plan-a-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-plan-a-spatial-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-plan-a-spatial-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-plan-a-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed60\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-pi05-baseline-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm01-seed54\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed53\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed52\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed50\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed49\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed55\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed50\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed49\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed43-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed47-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed44-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed43-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed57\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed65\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed61\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed58\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed59\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed56\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed75\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed74\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed72\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed63-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm01-seed71\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed62-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm003-seed73\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed51-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed52-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed65\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed64\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed64\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed65\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed64\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed62\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm005-seed63\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm01-seed61\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm003-seed64-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm003-seed63\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm003-seed62\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm01-seed51-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm01-seed52-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm01-seed51\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm005-seed49-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm005-seed55-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-openvla-crm-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-obs-only-object-norm003-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-object-seed49\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-object-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k5-obs-only-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed52\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed54\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"D088-eval-adaptive-unc-head-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"D088-eval-adaptive-unc-head-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"D088-eval-adaptive-unc-head-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-adaptive-unc-head-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-adaptive-unc-head-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-perdof-object-norm02-seed50\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-adaptive-unc-head-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-random-selection-spatial-seed42-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed50\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train-crm-openvla-obs-only\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"openvla-precompute-k1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-object-seed46-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm02-seed49\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-object-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k5-obs-only-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-spatial-seed43-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-spatial-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-k1-object-seed43-plan702\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-k1-object-seed42-plan702\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-k1-object-seed44-plan702\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-object-seed46-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-random-selection-spatial-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-object-seed46\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-spatial-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-spatial-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-spatial-norm02-seed49\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p90-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-argmin-object-seed50\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-object-seed48-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-goal-seed51\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-spatial-seed42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-object-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-k1-object-seed44-plan702-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-crm-k1-object-seed43-plan702-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-crm-k1-object-seed42-plan702-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm02-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-argmin-object-k5-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-goal-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed46-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-latency-profiling-v1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p75-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-goal-norm02-seed51\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p25-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-openvla-object-baseline-seed42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-argmin-object-seed49\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-argmin-object-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-goal-norm02-seed52\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p90-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm02-seed45-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p90-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed49\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-goal-seed47\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-adaptive-k-spatial-p50-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p50-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p50-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p25-seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-adaptive-k-spatial-p25-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p75-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-object-k20-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-long-seed49-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p75-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p50-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-p75-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-p75-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-p50-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-p50-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-spatial-p50-seed43-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"latency-profile-n1000\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-p90-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-p25-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-spatial-k10-seed51\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-goal-seed49\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-long-seed52\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-long-seed51\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-long-seed50\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-long-seed50\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-p25-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"calibrate-crm-correction-signal\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-adaptive-k-p25-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-goal-seed48-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-vla-only-goal-seed47-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-crm-goal-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-p50-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-p75-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-p90-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-adaptive-k-p90-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-spatial-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-long-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-long-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-long-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-goal-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-goal-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed43-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"k2-l2-calibration-phase1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-long-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-spatial-seed49\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-vla-only-goal-seed48\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-vla-only-goal-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-goal-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-object-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-long-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-long-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-long-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-goal-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-goal-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-spatial-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-long-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-crm-goal-seed45\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-crm-goal-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-vla-only-goal-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-goal-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-long-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"fmvd-calibration-phase1\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-vla-only-long-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm003-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm005-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-long-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-long-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-long-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-spatial-norm02-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed46\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-argmin-object-k5-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-vla-only-goal-seed44\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-random-selection-object-k5-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-object-k5-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-object-k5-seed43-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-random-selection-object-k5-seed42-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-k5-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-k5-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"plan_602-latency-profiling\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-spatial-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm005-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-spatial-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-default-seed48-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-spatial-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-spatial-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-k5-seed45\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-spatial-norm02-k5-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-random-selection-object-k5-seed45\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-random-selection-object-k5-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-random-selection-object-k5-seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-random-selection-object-k5-seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-spatial-norm02-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm01-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-default-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-argmin-object-k5-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-argmin-object-k5-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-argmin-object-k5-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm03-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train-crm-k1-accg-object-seed42-full\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"plan_701-precompute-k1-spatial\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"plan_701-crm-k1-train\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_obs_only_norm03_seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_obs_only_norm01_seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-lto-splitA-vla-only-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-lto-splitA-vla-only-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-lto-splitA-heldout-r2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"crm-lto-splitA-train\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm003-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-scalar-object-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-obs-only-spatial-norm02-k5-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-k5-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-norm02-k5-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-k5-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-lto-splitA-vla-only-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-lto-splitA-heldout-v2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-perdof-object-default-seed47\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-perdof-object-norm03-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-default-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm003-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm005-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm003-seed45\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm02-k5-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm01-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-default-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm03-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm03-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-scalar-object-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-lto-splitA-vla-only\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-lto-splitA-heldout\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm005-seed46\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm03-seed48\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm003-seed49\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"crm-lto-splitA-train-fixed\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm003-seed47\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm003-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm005-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-default-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-default-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-k5-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm005-seed45\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm02-k5-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm003-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm01-seed46-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm005-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-object-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm03-seed48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-k5-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm01-seed42-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm01-seed42-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-perdof-object-norm02-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm01-seed46\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-obs-only-object-norm01-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-k5-seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-default-seed46\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-perdof-object-default-seed44\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-mag-perdof-norm02\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-acr-spatial-v4-scalar\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-acr-spatial-v4-small\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-acr-spatial-v4-obs-only-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-argmin-only-spatial\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-acr-spatial-v3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-acr-object-v3\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-openvla-object-vla-only-seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-perdof-object-norm02-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed48\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-default-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm02-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm01-seed46\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"mag_obs_only_norm01_seed47\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"mag_obs_only_norm01_seed46\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm02-seed43-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"mag_perdof_norm02_seed43_r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm01-seed47-bjb1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-openvla-object-vla-only-seed42-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k1-crm-multiscale-object-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-k1-crm-multiscale-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-k1-crm-multiscale-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-k1-crm-multiscale-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-perdof-object-norm01-seed46-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k1-crm-multiscale-object-seed43-r2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-perdof-object-norm02-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm005-seed43-r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"plan_602-latency-profile\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train-crm-k1-accg-object-seed42-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-k1-crm-accg-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-k1-crm-accg-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-k1-crm-accg-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-obs-only-object-default-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-scalar-object-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm02-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm02-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train-crm-k1-accg-object-seed42-fallback\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train-crm-k1-accg-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-perdof-object-norm02-seed45-deploy\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm01-seed47-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm03-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-perdof-object-norm03-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-obs-only-object-norm03-seed47\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-perdof-object-norm03-seed46-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm01-seed44\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-obs-only-object-norm01-seed47-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm01-seed46-bjb2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-argmin-object-seed47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm01-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm01-seed47\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-argmin-object-seed46\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm03-seed45-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-mean-object-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-argmin-object-seed45\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-direct-correction-object-seed42-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-norm03-seed44\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-mag-perdof-norm02-object\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-acr-object-v4-scalar\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-mag-obsonly-norm02\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-mag-perdof-norm03\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-mag-perdof-norm005\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-mag-perdof-norm003\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-vla-mean-spatial\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-acr-object-obs-only-norm02\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-spatial-v7-full\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-object-v8-full\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-v5-shard2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-v5-shard1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-v5-shard0\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-v4-shard2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-v4-shard1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-v4-shard0\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-mean-spatial-t10\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-reconvla-spatial-v3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-train-v2-scalar-unc\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-train-v2-perdof\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-train-v2-obs-only\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-shard2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-shard1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-shard0\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"precompute-k5\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"plan_014-reconvla-baseline\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"plan_001-crm-smolvla\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"mvp-point-reaching\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-smolvla-libero-spatial\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-spatial\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-default-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-mag-perdof-norm005-object\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-mag-perdof-norm02-seed43-object-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-mag-perdof-norm03-object-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm005\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm003-b2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm03-object\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm005-object\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-direct-correction-object-seed42-r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-direct-correction-object-seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-scalar-object-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-perdof-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-obs-only-object-norm03-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-mean-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed44-r4\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-argmin-object-seed44-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-object-norm03-seed45\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-acr-object-v4-default-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-mag-perdof-norm003-object\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-acr-object-obs-only-default\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-scalar-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm003-object\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-scalar-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm02-seed44-r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-argmin-object-seed44-r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-vla-mean-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-perdof-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-only-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-norm02-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-argmin-object-seed44\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-obs-only-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"eval-mag-obsonly-norm03-b2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-argmin-object-seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-mag-perdof-norm02-seed43-object-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm03\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm02-object\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm03-b4\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm03-b3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-perdof-norm02-seed43-object\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-perdof-norm03-object-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-acr-object-v4-scalar-b2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-acr-object-v4-obs-only-b2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-spatial-v4-full\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-reconvla-spatial-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-object-v6-full\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-v3-shard2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-v3-shard1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-v3-shard0\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-v2-shard2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-v2-shard1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"precompute-v2-shard0\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-perdof-norm0p3-object-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-perdof-norm0p3-object\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm02-seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-acr-object-v4-default\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm03-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-vla-mean-object\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-reconvla-object\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-acr-object-v4-obs-only\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-acr-object-v4-perdof\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-acr-spatial-v4-scalar-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-acr-spatial-v4-obs-only-r3\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-obs-only-spatial-seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-acr-spatial-v4-small-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm-0.3-r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm-0p3-r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-argmin-only-spatial-r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm003\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-vla-only-object-k1\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-acr-spatial-v4-default-r3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-tiny-correction-spatial\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-acr-spatial-v4-default-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-acr-spatial-v4-obs-only\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval-acr-spatial-v4-default\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"crm-train-v3-norm-scalar-unc\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-train-v3-norm-obs-only\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-train-v3-norm\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"crm-train-v3-scalar-unc\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"crm-train-v3-obs-only\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"crm-train-v3-perdof\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-obs-only-spatial-v3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-scalar-unc-spatial-v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"crm-train-a4-scalar-unc\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"crm-train-a3-obs-only\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"crm-train-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"crm-train-k5\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-scalar-unc-spatial\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-acr-spatial-v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-k5-spatial\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-object-v7-full\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-spatial-v6-full\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-object-v5-full\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-acr-vla-spatial-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-acr-spatial-v1\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-reconvla-spatial-v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-object-v4-full\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-spatial-v5-full\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-spatial-v3-full\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval-spatial-reeval-v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}}, \"count\": 760, \"total\": 760, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.3884}}"
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
Only GPU 0 shows up with memory used (6006 MiB). That's odd - only 1 GPU? Let me check if this server actually has 4 GPUs. Maybe the other GPUs aren't showing. Let me also check the registry results more specifically.

Let me query the registry more specifically for eval-supp-goal and eval-supp-object experiments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "faa4f2b3-7573-4ef7-819e-d28e02c67472",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ijmArTjnan53LsoxfpgxA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 840,
      "cache_read_input_tokens": 24967,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 840
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

只看到 1 个 GPU。让我更精确地查询 registry 和 GPU 情况。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "fe10ac67-22b3-4d46-b048-56e6016a5df9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ijmArTjnan53LsoxfpgxA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 840,
      "cache_read_input_tokens": 24967,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 840
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_0141NF2fVg8RZnyutziXqPxM`</summary>

```json
{
  "server": "bjb2-40593",
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
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "bf698ab7-5a22-494b-921f-0995351147ad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ijmArTjnan53LsoxfpgxA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 840,
      "cache_read_input_tokens": 24967,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 840
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_011C1ofkNHsMAKv4nuPVe3af`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": {
    "status": "DONE"
  },
  "limit": 0,
  "fields": [
    "exp_id"
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
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "6c4f296a-0daa-4ae9-9dee-cb03682b971c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ijmArTjnan53LsoxfpgxA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 840,
      "cache_read_input_tokens": 24967,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 840
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

_source line 16 · 2026-05-24T07:09:41.247Z_

<details><summary>↩ Tool result · `toolu_0141NF2fVg8RZnyutziXqPxM`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"Sun May 24 15:09:41 2026       \\n+-----------------------------------------------------------------------------------------+\\n| NVIDIA-SMI 580.105.08             Driver Version: 580.105.08     CUDA Version: 13.0     |\\n+-----------------------------------------+------------------------+----------------------+\\n| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |\\n| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |\\n|                                         |                        |               MIG M. |\\n|=========================================+========================+======================|\\n|   0  NVIDIA GeForce RTX 4090 D      On  |   00000000:3D:00.0 Off |                  Off |\\n| 30%   39C    P2            105W /  425W |    6006MiB /  24564MiB |     21%      Default |\\n|                                         |                        |                  N/A |\\n+-----------------------------------------+------------------------+----------------------+\\n\\n+-----------------------------------------------------------------------------------------+\\n| Processes:                                                                              |\\n|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |\\n|        ID   ID                                                               Usage      |\\n|=========================================================================================|\\n|    0   N/A  N/A          235730    C+G   python                                 5988MiB |\\n+-----------------------------------------------------------------------------------------+\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "46ced699-aa86-43ae-b729-3c1af5fc256d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"Sun May 24 15:09:41 2026       \\\\n+-----------------------------------------------------------------------------------------+\\\\n| NVIDIA-SMI 580.105.08             Driver Version: 580.105.08     CUDA Version: 13.0     |\\\\n+-----------------------------------------+------------------------+----------------------+\\\\n| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |\\\\n| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |\\\\n|                                         |                        |               MIG M. |\\\\n|=========================================+========================+======================|\\\\n|   0  NVIDIA GeForce RTX 4090 D      On  |   00000000:3D:00.0 Off |                  Off |\\\\n| 30%   39C    P2            105W /  425W |    6006MiB /  24564MiB |     21%      Default |\\\\n|                                         |                        |                  N/A |\\\\n+-----------------------------------------+------------------------+----------------------+\\\\n\\\\n+-----------------------------------------------------------------------------------------+\\\\n| Processes:                                                                              |\\\\n|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |\\\\n|        ID   ID                                                               Usage      |\\\\n|=========================================================================================|\\\\n|    0   N/A  N/A          235730    C+G   python                                 5988MiB |\\\\n+-----------------------------------------------------------------------------------------+\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.52}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"Sun May 24 15:09:41 2026       \\n+-----------------------------------------------------------------------------------------+\\n| NVIDIA-SMI 580.105.08             Driver Version: 580.105.08     CUDA Version: 13.0     |\\n+-----------------------------------------+------------------------+----------------------+\\n| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |\\n| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |\\n|                                         |                        |               MIG M. |\\n|=========================================+========================+======================|\\n|   0  NVIDIA GeForce RTX 4090 D      On  |   00000000:3D:00.0 Off |                  Off |\\n| 30%   39C    P2            105W /  425W |    6006MiB /  24564MiB |     21%      Default |\\n|                                         |                        |                  N/A |\\n+-----------------------------------------+------------------------+----------------------+\\n\\n+-----------------------------------------------------------------------------------------+\\n| Processes:                                                                              |\\n|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |\\n|        ID   ID                                                               Usage      |\\n|=========================================================================================|\\n|    0   N/A  N/A          235730    C+G   python                                 5988MiB |\\n+-----------------------------------------------------------------------------------------+\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-24T07:09:44.828Z_

<details><summary>↩ Tool result · `toolu_011C1ofkNHsMAKv4nuPVe3af`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"crm-train-openvla-k1-multiscale-object\": {}, \"eval-supp-long-k2mean-s46-r2\": {}, \"eval-supp-long-reconvla-s46-r2\": {}, \"eval-supp-long-crm-norm005-s46-r2\": {}, \"eval-supp-long-adapt-tau025-s46-r2\": {}, \"eval-supp-obj-crm-norm005-s45\": {}, \"eval-supp-obj-adapt-tau025-s45\": {}, \"eval-supp-obj-vla-only-s45\": {}, \"eval-supp-spatial-crm-norm005-s45\": {}, \"eval-supp-spatial-vla-only-s45\": {}, \"precompute-pi05-goal-2048-r2\": {}, \"eval-supp-long-vla-only-s46\": {}, \"precompute-pi05-spatial-2048-r2\": {}, \"precompute-smolvla-goal-bjb1-32546\": {}, \"eval-supp-goal-vla-only-s46\": {}, \"eval-supp-goal-reconvla-s46\": {}, \"crm-train-pi05-spatial-full\": {}, \"eval-obs-only-spatial-v2\": {}, \"eval-perdof-object-norm003-seed44\": {}, \"eval-random-selection-spatial-seed42\": {}, \"eval-adaptive-k-spatial-p90-seed44-bjb2\": {}, \"eval-supp-goal-vla-only-wrapper-s44\": {}, \"eval-supp-long-reconvla-s45\": {}, \"eval-supp-spatial-k2mean-s46\": {}, \"eval-pi05-vla-only-long-seed42-r4\": {}, \"eval-supp-reconvla-obj-s45\": {}, \"eval-pi05-vla-only-object-seed42\": {}, \"eval-pi05-vla-only-object-seed43\": {}, \"eval-pi05-vla-only-object-seed44\": {}, \"eval-supp-long-k2mean-s45\": {}, \"eval-supp-goal-k2mean-s46\": {}, \"eval-supp-goal-adapt-tau025-s46\": {}, \"eval-supp-goal-crm-norm005-s46\": {}, \"eval-supp-spatial-adapt-tau025-s45-r3\": {}, \"eval-supp-spatial-k2mean-s45\": {}, \"eval-supp-spatial-vla-only-s46\": {}, \"eval-supp-spatial-reconvla-s46\": {}, \"eval-supp-spatial-adapt-tau025-s46\": {}, \"eval-supp-spatial-crm-norm005-s46\": {}, \"eval-supp-long-crm-norm005-s45\": {}, \"eval-supp-long-adapt-tau025-s45\": {}, \"eval-supp-long-vla-only-s45\": {}, \"eval-supp-spatial-reconvla-s45\": {}, \"eval-supp-goal-k2mean-s45\": {}, \"eval-supp-adapt-tau025-obj-s45\": {}, \"eval-supp-obj-k2mean-s45\": {}, \"eval-supp-crm-obj-s46\": {}, \"eval-supp-long-k2mean-s44\": {}, \"eval-supp-long-reconvla-s44\": {}, \"eval-supp-goal-reconvla-s45\": {}, \"eval-supp-goal-vla-only-s45\": {}, \"eval-supp-crm-norm005-obj-s46\": {}, \"eval-supp-goal-crm-norm005-s45\": {}, \"eval-supp-crm-norm005-obj-s45\": {}, \"eval-supp-reconvla-obj-s46\": {}, \"eval-supp-goal-adapt-tau025-s45\": {}, \"eval-supp-long-crm-norm005-s44\": {}, \"eval-supp-long-adapt-tau025-s44\": {}, \"eval-supp-k2mean-obj-s46\": {}, \"eval-supp-k2mean-obj-s45\": {}, \"eval-supp-adapt-tau025-obj-s46\": {}, \"eval-supp-long-vla-only-s43\": {}, \"eval-supp-long-k2mean-s42\": {}, \"eval-supp-obj-vla-only-s46\": {}, \"eval-supp-long-vla-only-s44\": {}, \"eval-supp-long-k2mean-s43\": {}, \"eval-supp-long-reconvla-s43\": {}, \"eval-supp-long-crm-norm005-s43\": {}, \"eval-supp-long-adapt-tau025-s43\": {}, \"eval-supp-obj-adapt-tau025-s45-r2\": {}, \"eval-supp-long-crm-norm005-s42\": {}, \"eval-supp-long-adapt-tau025-s42\": {}, \"eval-supp-long-reconvla-s42\": {}, \"eval-ablation-tau040-goal-s42\": {}, \"eval-ablation-tau015-goal-s42\": {}, \"eval-supp-k2mean-object-s44\": {}, \"eval-ablation-tau010-goal-s42\": {}, \"eval-supp-obj-reconvla-s44\": {}, \"eval-supp-spatial-vla-only-s44\": {}, \"eval-supp-goal-vla-only-wrapper-s44-r2\": {}, \"eval-supp-k2mean-spatial-s44\": {}, \"eval-supp-spatial-vla-only-s43\": {}, \"eval-supp-k2mean-goal-s44\": {}, \"eval-supp-adapt-tau025-obj-s44\": {}, \"eval-supp-crm-norm005-obj-s44\": {}, \"eval-supp-goal-vla-only-wrapper-s43\": {}, \"eval-supp-long-vla-only-s42\": {}, \"eval-supp-goal-reconvla-s44\": {}, \"eval-supp-obj-reconvla-s43\": {}, \"eval-supp-crm-norm005-goal-s44\": {}, \"eval-supp-k2mean-object-s43\": {}, \"eval-supp-k2mean-goal-s42-r2\": {}, \"eval-supp-adapt-tau025-goal-s44\": {}, \"eval-supp-crm-norm005-obj-s43\": {}, \"eval-supp-adapt-tau025-goal-s43\": {}, \"eval-supp-crm-norm005-goal-s43\": {}, \"eval-supp-adapt-tau025-obj-s43\": {}, \"eval-supp-goal-reconvla-s43\": {}, \"eval-supp-k2mean-spatial-s43\": {}, \"eval-supp-reconvla-spatial-s44\": {}, \"eval-supp-reconvla-spatial-s43\": {}, \"eval-supp-k2mean-goal-s43\": {}, \"eval-supp-k2mean-object-s42\": {}, \"eval-supp-goal-adapt-tau025-s42\": {}, \"eval-supp-goal-crm005-s42\": {}, \"eval-supp-goal-reconvla-s42\": {}, \"train-crm-unified-4suite-r6\": {}, \"eval-goal-vla-only-wrapper-s42\": {}, \"eval-supp-obj-adapt-tau025-s42\": {}, \"eval-supp-k2mean-spatial-s42\": {}, \"eval-supp-crm-norm005-spatial-s44\": {}, \"eval-supp-adapt-tau025-spatial-s44\": {}, \"eval-supp-reconvla-k2-spatial-s42\": {}, \"eval-supp-adapt-tau025-spatial-s43\": {}, \"eval-supp-crm-norm005-spatial-s43\": {}, \"eval-supp-k2mean-goal-s42\": {}, \"eval-supp-obj-adapt-s42-r2\": {}, \"eval-object-vla-only-wrapper-s44-r2\": {}, \"eval-object-vla-only-wrapper-s43-r2\": {}, \"eval-object-vla-only-wrapper-s42-r2\": {}, \"eval-supp-obj-reconvla-s42\": {}, \"eval-supp-obj-crm005-s42-r2\": {}, \"eval-supp-adapt-tau035-spatial-s42-r2\": {}, \"eval-supp-adapt-tau015-spatial-s42-r2\": {}, \"eval-supp-crm-norm02-spatial-s42-r2\": {}, \"eval-supp-adapt-tau025-spatial-s42-r2\": {}, \"eval-openvla-object-baseline-seed42-r2\": {}, \"eval-obs-only-object-norm02-seed55\": {}, \"precompute-pi05-features-object\": {}, \"precompute-smolvla-goal-shard2\": {}, \"precompute-smolvla-goal-shard1\": {}, \"precompute-smolvla-goal-shard0\": {}, \"eval-smolvla-long-seed2\": {}, \"eval-smolvla-long-seed1\": {}, \"eval-smolvla-long-seed0\": {}, \"eval-smolvla-crm-spatial-seed42-v1\": {}, \"eval-smolvla-crm-spatial-seed43-v1\": {}, \"eval-smolvla-crm-spatial-seed44-v1\": {}, \"eval-smolvla-crm-goal-seed42-v1\": {}, \"eval-smolvla-crm-goal-seed43-v1\": {}, \"eval-smolvla-crm-goal-seed44-v1\": {}, \"eval-supp-obj-adapt-s42\": {}, \"eval-crm-norm02-spatial-s42\": {}, \"eval-adaptive-tau015-spatial-s42\": {}, \"eval-adaptive-tau025-spatial-s42\": {}, \"eval-adaptive-tau035-spatial-s42\": {}, \"train-crm-unified-4suite-r5-resumed\": {}, \"eval-object-vla-only-wrapper-s44\": {}, \"eval-object-vla-only-wrapper-s43\": {}, \"eval-object-vla-only-wrapper-s42\": {}, \"eval-supp-obj-crm005-s42\": {}, \"eval-supp-adapt-tau035-spatial-s42\": {}, \"eval-supp-adapt-tau025-spatial-s42\": {}, \"eval-supp-adapt-tau015-spatial-s42\": {}, \"eval-supp-crm-norm02-spatial-s42\": {}, \"eval-3dir-adaptive-spatial-s42\": {}, \"eval-3dir-norm03-spatial-s42\": {}, \"eval-3dir-reconvla-spatial-s42\": {}, \"eval-3dir-norm01-spatial-s42\": {}, \"eval-3dir-norm005-spatial-s42\": {}, \"precompute-pi05-goal-2048\": {}, \"precompute-pi05-spatial-2048\": {}, \"precompute-pi05-object-2048\": {}, \"eval-smolvla-crm-object-seed43-v1\": {}, \"eval-smolvla-crm-object-seed42-v1\": {}, \"eval-smolvla-crm-object-seed44-v1\": {}, \"train-crm-unified-4suite-r5\": {}, \"eval-smolvla-crm-goal-seed43\": {}, \"eval-smolvla-crm-goal-seed42\": {}, \"eval-smolvla-crm-spatial-seed44\": {}, \"eval-smolvla-crm-spatial-seed43\": {}, \"eval-smolvla-crm-spatial-seed42\": {}, \"precompute-pi05-long-2048\": {}, \"eval-smolvla-lerobot-goal-seed44-v3\": {}, \"eval-smolvla-lerobot-goal-seed43-v3\": {}, \"eval-smolvla-lerobot-spatial-seed43-v3\": {}, \"train-crm-smolvla-3suite-v1\": {}, \"eval-smolvla-lerobot-goal-seed43-v2\": {}, \"eval-smolvla-lerobot-spatial-seed43-v2\": {}, \"eval-smolvla-lerobot-object-seed44-v2\": {}, \"eval-smolvla-lerobot-object-seed43-v2\": {}, \"eval-smolvla-lerobot-goal-seed43\": {}, \"eval-smolvla-lerobot-spatial-seed43\": {}, \"eval-smolvla-lerobot-object-seed44\": {}, \"eval-smolvla-lerobot-object-seed43\": {}, \"eval-smolvla-lerobot-spatial-seed44\": {}, \"precompute-smolvla-long-wrapper-bjb1\": {}, \"eval-smolvla-lerobot-long-seed44\": {}, \"eval-smolvla-lerobot-long-seed43\": {}, \"eval-smolvla-lerobot-long-seed42\": {}, \"train-crm-unified-4suite-r4\": {}, \"eval-pi05-vla-only-long-seed42-r4-rerun\": {}, \"eval-pi05-crm-object-seed44\": {}, \"eval-pi05-crm-object-seed43\": {}, \"eval-pi05-crm-object-seed42\": {}, \"eval-pi05-vla-only-long-seed43-r4-std\": {}, \"eval-pi05-vla-only-goal-seed44-r4-std\": {}, \"eval-pi05-vla-only-goal-seed42-r4-std\": {}, \"eval-pi05-vla-only-long-seed44-r4-std\": {}, \"eval-pi05-vla-only-goal-seed43-r4-std\": {}, \"eval-pi05-vla-only-goal-seed42-r4\": {}, \"precompute-smolvla-long-k2\": {}, \"train-crm-unified-4suite-r3\": {}, \"train-crm-unified-4suite-r2\": {}, \"precompute-smolvla-goal-bjb2-28827\": {}, \"precompute-smolvla-long-bjb2-28827\": {}, \"eval-pi05-vla-only-spatial-seed44-r4\": {}, \"eval-pi05-vla-only-spatial-seed43-r4\": {}, \"eval-pi05-vla-only-spatial-seed42-r4\": {}, \"eval-pi05-vla-only-long-seed44-r4\": {}, \"eval-pi05-vla-only-long-seed43-r4\": {}, \"eval-pi05-vla-only-goal-seed44-r4\": {}, \"eval-pi05-vla-only-goal-seed43-r4\": {}, \"eval-openvla-oft-official-object\": {}, \"eval-pi05-crm-spatial-seed44\": {}, \"eval-pi05-crm-spatial-seed43\": {}, \"eval-pi05-crm-spatial-seed42\": {}, \"eval-pi05-vla-only-object-seed43-r4\": {}, \"eval-pi05-vla-only-object-seed44-r4\": {}, \"eval-smolvla-lerobot-official-object\": {}, \"eval-pi05-vla-only-object-seed42-r4\": {}, \"train-crm-unified-4suite\": {}, \"precompute-smolvla-long-bjb1-32546-r2\": {}, \"precompute-smolvla-long-bjb1-32546\": {}, \"eval-loss-perdof-object-seed42\": {}, \"eval-loss-combined-object-seed42\": {}, \"eval-loss-conformal-object-seed42\": {}, \"eval-loss-mse-object-seed42\": {}, \"eval-openvla-oft-object-baseline-seed42\": {}, \"precompute-smolvla-long-bjb1-18228\": {}, \"crm-loss-combined\": {}, \"crm-loss-conformal\": {}, \"precompute-smolvla-goal-bjb1-18228\": {}, \"crm-loss-perdof\": {}, \"crm-loss-mse-baseline\": {}, \"eval-smolvla-acr-goal-seed43\": {}, \"eval-smolvla-crm-long-seed44-v2\": {}, \"eval-smolvla-crm-goal-seed44-v2\": {}, \"eval-smolvla-crm-long-seed43-v2\": {}, \"eval-smolvla-acr-long-seed42\": {}, \"eval-smolvla-acr-goal-seed42\": {}, \"crm-train-pi05-spatial-v2\": {}, \"crm-train-pi05-object-full\": {}, \"crm-train-pi05-spatial\": {}, \"crm-train-pi05-object\": {}, \"eval-pi05-vla-only-spatial-seed45\": {}, \"eval-pi05-vla-only-spatial-seed43-r3\": {}, \"eval-pi05-vla-only-spatial-seed42-r3\": {}, \"eval-pi05-vla-only-object-seed44-r3\": {}, \"eval-pi05-vla-only-object-seed43-r3\": {}, \"eval-pi05-vla-only-object-seed42-r3\": {}, \"eval-spatial-obs-only-seed45\": {}, \"eval-pi05-vla-only-spatial-seed44\": {}, \"eval-pi05-vla-only-spatial-seed43\": {}, \"eval-pi05-vla-only-spatial-seed42\": {}, \"eval-k20-obs-only-spatial-seed44\": {}, \"eval-k20-obs-only-spatial-seed43\": {}, \"eval-k20-obs-only-spatial-seed42\": {}, \"eval-k20-obs-only-object-seed45\": {}, \"eval-obs-only-object-norm003-seed66\": {}, \"eval-obs-only-object-norm01-seed66\": {}, \"eval-obs-only-object-norm005-seed66\": {}, \"eval-obs-only-object-norm003-seed67\": {}, \"eval-k20-obs-only-object-seed44\": {}, \"eval-k20-obs-only-object-seed43\": {}, \"eval-k20-obs-only-object-seed42\": {}, \"eval-crm-object-k20-seed44\": {}, \"eval-crm-object-k20-seed42\": {}, \"eval-obs-only-object-norm02-seed53\": {}, \"eval-obs-only-object-norm02-seed52\": {}, \"eval-obs-only-object-norm02-seed51\": {}, \"eval-obs-only-object-norm02-seed50\": {}, \"eval-obs-only-object-norm02-seed48-r2\": {}, \"eval-obs-only-object-norm02-seed47\": {}, \"eval-obs-only-object-norm02-seed46\": {}, \"eval-obs-only-object-norm02-seed45\": {}, \"eval-obs-only-object-norm02-seed44-r2\": {}, \"eval-obs-only-object-norm02-seed43-r3\": {}, \"eval-obs-only-object-norm02-seed43-r2\": {}, \"eval-obs-only-object-norm005-seed67\": {}, \"eval-obs-only-object-norm01-seed67\": {}, \"eval-vla-only-object-seed50\": {}, \"eval-vla-only-object-seed49\": {}, \"eval-vla-only-object-seed48\": {}, \"eval-vla-only-object-seed46\": {}, \"eval-vla-only-object-seed45\": {}, \"eval-vla-only-object-seed44-r2\": {}, \"eval-plan-a-object-seed42\": {}, \"eval-vla-only-object-seed43\": {}, \"eval-vla-only-object\": {}, \"eval-plan-a-spatial-seed43\": {}, \"eval-plan-a-object-seed44\": {}, \"eval-plan-a-spatial-seed42\": {}, \"eval-plan-a-spatial-seed44\": {}, \"eval-plan-a-object-seed43\": {}, \"eval-random-selection-object-seed44\": {}, \"eval-random-selection-object-seed43\": {}, \"eval-obs-only-object-norm01-seed60\": {}, \"eval-pi05-baseline-object-seed42\": {}, \"eval-obs-only-object-norm01-seed54\": {}, \"eval-obs-only-object-norm01-seed53\": {}, \"eval-obs-only-object-norm01-seed52\": {}, \"eval-obs-only-object-norm01-seed50\": {}, \"eval-obs-only-object-norm01-seed49\": {}, \"eval-obs-only-object-norm01-seed48\": {}, \"eval-obs-only-object-norm01-seed47\": {}, \"eval-obs-only-object-norm01-seed45-r2\": {}, \"eval-obs-only-object-norm01-seed44\": {}, \"eval-obs-only-object-norm005-seed55\": {}, \"eval-obs-only-object-norm005-seed50\": {}, \"eval-obs-only-object-norm005-seed49\": {}, \"eval-obs-only-object-norm005-seed48\": {}, \"eval-obs-only-object-norm005-seed47\": {}, \"eval-obs-only-object-norm005-seed44\": {}, \"eval-obs-only-object-norm005-seed43-r2\": {}, \"eval-obs-only-object-norm005-seed43\": {}, \"eval-obs-only-object-norm003-seed48\": {}, \"eval-obs-only-object-norm003-seed47-r2\": {}, \"eval-obs-only-object-norm003-seed46\": {}, \"eval-obs-only-object-norm003-seed45\": {}, \"eval-obs-only-object-norm003-seed44-bjb2\": {}, \"eval-obs-only-object-norm003-seed44\": {}, \"eval-obs-only-object-norm003-seed43-r2\": {}, \"eval-obs-only-object-norm003-seed43\": {}, \"eval-obs-only-object-norm01-seed57\": {}, \"eval-obs-only-object-norm005-seed65\": {}, \"eval-obs-only-object-norm005-seed61\": {}, \"eval-obs-only-object-norm005-seed58\": {}, \"eval-obs-only-object-norm003-seed59\": {}, \"eval-obs-only-object-norm003-seed56\": {}, \"eval-obs-only-object-norm005-seed75\": {}, \"eval-obs-only-object-norm01-seed74\": {}, \"eval-obs-only-object-norm005-seed72\": {}, \"eval-obs-only-object-norm003-seed63-r2\": {}, \"eval-obs-only-object-norm01-seed71\": {}, \"eval-obs-only-object-norm003-seed62-r2\": {}, \"eval-obs-only-object-norm003-seed73\": {}, \"eval-obs-only-object-norm01-seed51-r3\": {}, \"eval-obs-only-object-norm01-seed52-r3\": {}, \"eval-obs-only-object-norm01-seed65\": {}, \"eval-obs-only-object-norm01-seed64\": {}, \"eval-obs-only-object-norm005-seed64\": {}, \"eval-obs-only-object-norm003-seed65\": {}, \"eval-obs-only-object-norm003-seed64\": {}, \"eval-obs-only-object-norm005-seed62\": {}, \"eval-obs-only-object-norm005-seed63\": {}, \"eval-obs-only-object-norm01-seed61\": {}, \"eval-obs-only-object-norm003-seed64-bjb2\": {}, \"eval-obs-only-object-norm003-seed63\": {}, \"eval-obs-only-object-norm003-seed62\": {}, \"eval-obs-only-object-norm01-seed51-r2\": {}, \"eval-obs-only-object-norm01-seed52-r2\": {}, \"eval-obs-only-object-norm01-seed51\": {}, \"eval-obs-only-object-norm005-seed49-r2\": {}, \"eval-obs-only-object-norm005-seed55-r2\": {}, \"eval-openvla-crm-object-seed42\": {}, \"eval-obs-only-object-norm003-seed44-r2\": {}, \"eval-random-selection-object-seed49\": {}, \"eval-random-selection-object-seed48\": {}, \"eval-k5-obs-only-object-seed44\": {}, \"eval-obs-only-spatial-norm02-seed52\": {}, \"eval-obs-only-object-norm02-seed54\": {}, \"D088-eval-adaptive-unc-head-object-seed44\": {}, \"D088-eval-adaptive-unc-head-object-seed43\": {}, \"D088-eval-adaptive-unc-head-object-seed42\": {}, \"eval-adaptive-unc-head-object-seed42\": {}, \"eval-adaptive-unc-head-object-seed43\": {}, \"eval-perdof-object-norm02-seed50\": {}, \"eval-adaptive-unc-head-object-seed44\": {}, \"eval-random-selection-spatial-seed42-r3\": {}, \"eval-obs-only-spatial-norm02-seed50\": {}, \"train-crm-openvla-obs-only\": {}, \"openvla-precompute-k1\": {}, \"eval-random-selection-object-seed46-r3\": {}, \"eval-perdof-object-norm02-seed49\": {}, \"eval-random-selection-object-seed47\": {}, \"eval-obs-only-spatial-norm02-seed42-r2\": {}, \"eval-k5-obs-only-object-seed43\": {}, \"eval-random-selection-spatial-seed43-r2\": {}, \"eval-random-selection-spatial-seed44\": {}, \"eval-crm-k1-object-seed43-plan702\": {}, \"eval-crm-k1-object-seed42-plan702\": {}, \"eval-crm-k1-object-seed44-plan702\": {}, \"eval-random-selection-object-seed46-r2\": {}, \"eval-random-selection-spatial-seed43\": {}, \"eval-random-selection-object-seed46\": {}, \"eval-obs-only-spatial-seed48\": {}, \"eval-vla-only-spatial-seed48\": {}, \"eval-obs-only-spatial-norm02-seed42\": {}, \"eval-obs-only-spatial-norm02-seed49\": {}, \"eval-adaptive-k-spatial-p90-seed44\": {}, \"eval-argmin-object-seed50\": {}, \"eval-vla-only-object-seed48-r2\": {}, \"eval-vla-only-goal-seed51\": {}, \"eval-random-selection-spatial-seed42-r2\": {}, \"eval-random-selection-object-seed45\": {}, \"eval-crm-k1-object-seed44-plan702-r2\": {}, \"eval-crm-k1-object-seed43-plan702-r2\": {}, \"eval-crm-k1-object-seed42-plan702-r2\": {}, \"eval-perdof-object-norm02-seed48\": {}, \"eval-argmin-object-k5-seed44-r2\": {}, \"eval-vla-only-goal-seed44-r2\": {}, \"eval-obs-only-spatial-norm02-seed46-r2\": {}, \"eval-latency-profiling-v1\": {}, \"eval-adaptive-k-spatial-p75-seed44\": {}, \"eval-obs-only-goal-norm02-seed51\": {}, \"eval-adaptive-k-spatial-p25-seed44\": {}, \"eval-openvla-object-baseline-seed42\": {}, \"eval-argmin-object-seed49\": {}, \"eval-argmin-object-seed48\": {}, \"eval-obs-only-spatial-norm02-seed48\": {}, \"eval-obs-only-goal-norm02-seed52\": {}, \"eval-adaptive-k-spatial-p90-seed43\": {}, \"eval-perdof-object-norm02-seed45-r3\": {}, \"eval-adaptive-k-spatial-p90-seed42\": {}, \"eval-obs-only-object-norm02-seed49\": {}, \"eval-vla-only-goal-seed47\": {}, \"eval-adaptive-k-spatial-p50-seed44\": {}, \"eval-adaptive-k-spatial-p50-seed43\": {}, \"eval-adaptive-k-spatial-p50-seed42\": {}, \"eval-adaptive-k-spatial-p25-seed42\": {}, \"eval-adaptive-k-spatial-p25-seed43\": {}, \"eval-adaptive-k-spatial-p75-seed43\": {}, \"eval-crm-object-k20-seed43\": {}, \"eval-vla-only-long-seed49-r2\": {}, \"eval-adaptive-k-spatial-p75-seed42\": {}, \"eval-adaptive-k-spatial-p50-seed44-r2\": {}, \"eval-adaptive-k-p75-seed42\": {}, \"eval-adaptive-k-p75-seed43\": {}, \"eval-adaptive-k-p50-seed42\": {}, \"eval-adaptive-k-p50-seed43\": {}, \"eval-random-selection-object-seed42\": {}, \"eval-adaptive-k-spatial-p50-seed43-r2\": {}, \"eval-obs-only-object-norm02-seed42\": {}, \"latency-profile-n1000\": {}, \"eval-adaptive-k-p90-seed44\": {}, \"eval-adaptive-k-p25-seed43\": {}, \"eval-crm-spatial-k10-seed51\": {}, \"eval-vla-only-goal-seed49\": {}, \"eval-vla-only-long-seed52\": {}, \"eval-vla-only-long-seed51\": {}, \"eval-vla-only-long-seed50\": {}, \"eval-crm-long-seed50\": {}, \"eval-adaptive-k-p25-seed44-r2\": {}, \"calibrate-crm-correction-signal\": {}, \"eval-adaptive-k-p25-seed42\": {}, \"eval-vla-only-goal-seed48-r2\": {}, \"eval-vla-only-goal-seed47-r2\": {}, \"eval-crm-goal-seed46\": {}, \"eval-adaptive-k-p50-seed44\": {}, \"eval-adaptive-k-p75-seed44\": {}, \"eval-adaptive-k-p90-seed43\": {}, \"eval-adaptive-k-p90-seed42\": {}, \"eval-vla-only-spatial-seed47\": {}, \"eval-crm-long-seed47\": {}, \"eval-vla-only-long-seed48\": {}, \"eval-crm-long-seed46\": {}, \"eval-crm-goal-seed45-r2\": {}, \"eval-crm-goal-seed44-r2\": {}, \"eval-obs-only-spatial-norm02-seed43-r2\": {}, \"k2-l2-calibration-phase1\": {}, \"eval-crm-long-seed45\": {}, \"eval-vla-only-spatial-seed49\": {}, \"eval-vla-only-goal-seed48\": {}, \"eval-vla-only-goal-seed43\": {}, \"eval-vla-only-goal-seed42\": {}, \"eval-vla-only-object-seed47\": {}, \"eval-crm-long-seed44\": {}, \"eval-crm-long-seed43\": {}, \"eval-crm-long-seed42\": {}, \"eval-crm-goal-seed42\": {}, \"eval-crm-goal-seed43\": {}, \"eval-vla-only-spatial-seed46\": {}, \"eval-vla-only-long-seed47\": {}, \"eval-crm-goal-seed45\": {}, \"eval-crm-goal-seed44\": {}, \"eval-vla-only-goal-seed45\": {}, \"eval-vla-only-goal-seed46\": {}, \"eval-vla-only-long-seed46\": {}, \"fmvd-calibration-phase1\": {}, \"eval-vla-only-long-seed45\": {}, \"eval-perdof-object-norm003-seed47\": {}, \"eval-perdof-object-norm005-seed47\": {}, \"eval-vla-only-long-seed44\": {}, \"eval-vla-only-long-seed42\": {}, \"eval-vla-only-long-seed43\": {}, \"eval-obs-only-spatial-norm02-seed43\": {}, \"eval-obs-only-spatial-norm02-seed47\": {}, \"eval-obs-only-spatial-norm02-seed46\": {}, \"eval-argmin-object-k5-seed44\": {}, \"eval-vla-only-goal-seed44\": {}, \"eval-random-selection-object-k5-seed45-r2\": {}, \"eval-random-selection-object-k5-seed44-r2\": {}, \"eval-random-selection-object-k5-seed43-r2\": {}, \"eval-random-selection-object-k5-seed42-r2\": {}, \"eval-obs-only-spatial-norm02-k5-seed44-r2\": {}, \"eval-obs-only-spatial-norm02-k5-seed45-r2\": {}, \"plan_602-latency-profiling\": {}, \"eval-vla-only-spatial-seed45\": {}, \"eval-perdof-object-norm005-seed45-r2\": {}, \"eval-vla-only-spatial-seed44\": {}, \"eval-obs-only-object-default-seed48-r2\": {}, \"eval-vla-only-spatial-seed43\": {}, \"eval-vla-only-spatial-seed42\": {}, \"eval-obs-only-spatial-norm02-k5-seed45\": {}, \"eval-obs-only-spatial-norm02-k5-seed44\": {}, \"eval-random-selection-object-k5-seed45\": {}, \"eval-random-selection-object-k5-seed44\": {}, \"eval-random-selection-object-k5-seed43\": {}, \"eval-random-selection-object-k5-seed42\": {}, \"eval-obs-only-spatial-norm02-seed44\": {}, \"eval-perdof-object-norm01-seed43\": {}, \"eval-obs-only-object-default-seed45-r2\": {}, \"eval-argmin-object-k5-seed42\": {}, \"eval-argmin-object-k5-seed45\": {}, \"eval-argmin-object-k5-seed43\": {}, \"eval-perdof-object-norm03-seed43\": {}, \"eval-obs-only-spatial-norm02-seed45\": {}, \"train-crm-k1-accg-object-seed42-full\": {}, \"plan_701-precompute-k1-spatial\": {}, \"plan_701-crm-k1-train\": {}, \"eval_obs_only_norm03_seed48\": {}, \"eval_obs_only_norm01_seed48\": {}, \"eval-lto-splitA-vla-only-r3\": {}, \"eval-lto-splitA-vla-only-r2\": {}, \"eval-lto-splitA-heldout-r2\": {}, \"crm-lto-splitA-train\": {}, \"eval-perdof-object-norm003-seed48\": {}, \"eval-scalar-object-seed45-r2\": {}, \"eval-obs-only-spatial-norm02-k5-seed43\": {}, \"eval-obs-only-object-norm02-k5-seed48\": {}, \"eval-obs-only-spatial-norm02-k5-seed42\": {}, \"eval-obs-only-object-norm02-k5-seed46\": {}, \"eval-lto-splitA-vla-only-v2\": {}, \"eval-lto-splitA-heldout-v2\": {}, \"eval-perdof-object-default-seed47\": {}, \"eval-perdof-object-norm03-seed47\": {}, \"eval-obs-only-object-default-seed48\": {}, \"eval-perdof-object-norm003-seed46\": {}, \"eval-perdof-object-norm005-seed46\": {}, \"eval-perdof-object-norm003-seed45\": {}, \"eval-obs-only-object-norm02-k5-seed47\": {}, \"eval-perdof-object-norm01-seed48\": {}, \"eval-obs-only-object-default-seed47\": {}, \"eval-perdof-object-norm03-seed46\": {}, \"eval-obs-only-object-norm03-seed46\": {}, \"eval-scalar-object-seed46\": {}, \"eval-obs-only-object-norm003-seed45-r2\": {}, \"eval-lto-splitA-vla-only\": {}, \"eval-lto-splitA-heldout\": {}, \"eval-obs-only-object-norm005-seed46\": {}, \"eval-perdof-object-norm03-seed48\": {}, \"eval-obs-only-object-norm003-seed49\": {}, \"crm-lto-splitA-train-fixed\": {}, \"eval-obs-only-object-norm003-seed47\": {}, \"eval-perdof-object-norm003-seed43\": {}, \"eval-perdof-object-norm005-seed43\": {}, \"eval-perdof-object-default-seed43\": {}, \"eval-perdof-object-default-seed45\": {}, \"eval-obs-only-object-norm02-k5-seed45\": {}, \"eval-perdof-object-norm005-seed45\": {}, \"eval-obs-only-object-norm02-k5-seed44\": {}, \"eval-perdof-object-norm003-seed44-r2\": {}, \"eval-obs-only-object-norm01-seed46-r3\": {}, \"eval-perdof-object-norm005-seed44\": {}, \"eval-vla-only-object-seed45-r2\": {}, \"eval-obs-only-object-norm03-seed48\": {}, \"eval-obs-only-object-norm02-k5-seed43\": {}, \"eval-perdof-object-norm01-seed42-r2\": {}, \"eval-obs-only-object-norm01-seed42-r2\": {}, \"eval-perdof-object-norm02-seed43\": {}, \"eval-perdof-object-norm01-seed46\": {}, \"eval-obs-only-object-norm01-seed45\": {}, \"eval-obs-only-object-norm02-k5-seed42\": {}, \"eval-perdof-object-default-seed46\": {}, \"eval-perdof-object-default-seed44\": {}, \"eval-mag-perdof-norm02\": {}, \"eval-acr-spatial-v4-scalar\": {}, \"eval-acr-spatial-v4-small\": {}, \"eval-acr-spatial-v4-obs-only-r2\": {}, \"eval-argmin-only-spatial\": {}, \"eval-acr-spatial-v3\": {}, \"eval-acr-object-v3\": {}, \"eval-openvla-object-vla-only-seed42\": {}, \"eval-perdof-object-norm02-seed47\": {}, \"eval-obs-only-object-norm02-seed48\": {}, \"eval-obs-only-object-default-seed46\": {}, \"eval-perdof-object-norm02-seed46\": {}, \"eval-obs-only-object-norm01-seed46\": {}, \"mag_obs_only_norm01_seed47\": {}, \"mag_obs_only_norm01_seed46\": {}, \"eval-perdof-object-norm02-seed43-r3\": {}, \"mag_perdof_norm02_seed43_r3\": {}, \"eval-perdof-object-norm01-seed47-bjb1\": {}, \"eval-openvla-object-vla-only-seed42-v2\": {}, \"eval-k1-crm-multiscale-object-seed44-r2\": {}, \"eval-k1-crm-multiscale-object-seed44\": {}, \"eval-k1-crm-multiscale-object-seed43\": {}, \"eval-k1-crm-multiscale-object-seed42\": {}, \"eval-perdof-object-norm01-seed46-r2\": {}, \"eval-k1-crm-multiscale-object-seed43-r2\": {}, \"eval-perdof-object-norm02-seed45-r2\": {}, \"eval-obs-only-object-norm005-seed43-r3\": {}, \"plan_602-latency-profile\": {}, \"train-crm-k1-accg-object-seed42-v2\": {}, \"eval-k1-crm-accg-object-seed44\": {}, \"eval-k1-crm-accg-object-seed43\": {}, \"eval-k1-crm-accg-object-seed42\": {}, \"eval-obs-only-object-default-seed45\": {}, \"eval-scalar-object-seed45\": {}, \"eval-perdof-object-norm02-seed45\": {}, \"eval-perdof-object-norm02-seed44\": {}, \"train-crm-k1-accg-object-seed42-fallback\": {}, \"train-crm-k1-accg-object-seed42\": {}, \"eval-perdof-object-norm02-seed45-deploy\": {}, \"eval-obs-only-object-norm01-seed47-r2\": {}, \"eval-perdof-object-norm03-seed45-r2\": {}, \"eval-perdof-object-norm03-seed44-r2\": {}, \"eval-obs-only-object-norm03-seed47\": {}, \"eval-perdof-object-norm03-seed46-r2\": {}, \"eval-perdof-object-norm01-seed44\": {}, \"eval-obs-only-object-norm01-seed47-bjb2\": {}, \"eval-obs-only-object-norm01-seed46-bjb2\": {}, \"eval-argmin-object-seed47\": {}, \"eval-perdof-object-norm01-seed45\": {}, \"eval-perdof-object-norm01-seed47\": {}, \"eval-argmin-object-seed46\": {}, \"eval-obs-only-object-norm03-seed45-r2\": {}, \"eval-vla-mean-object-seed45\": {}, \"eval-argmin-object-seed45\": {}, \"eval-direct-correction-object-seed42-r3\": {}, \"eval-perdof-object-norm03-seed44\": {}, \"eval-mag-perdof-norm02-object\": {}, \"eval-acr-object-v4-scalar\": {}, \"eval-mag-obsonly-norm02\": {}, \"eval-mag-perdof-norm03\": {}, \"eval-mag-perdof-norm005\": {}, \"eval-mag-perdof-norm003\": {}, \"eval-vla-mean-spatial\": {}, \"eval-acr-object-obs-only-norm02\": {}, \"eval-spatial-v7-full\": {}, \"eval-object-v8-full\": {}, \"precompute-v5-shard2\": {}, \"precompute-v5-shard1\": {}, \"precompute-v5-shard0\": {}, \"precompute-v4-shard2\": {}, \"precompute-v4-shard1\": {}, \"precompute-v4-shard0\": {}, \"eval-vla-mean-spatial-t10\": {}, \"eval-reconvla-spatial-v3\": {}, \"crm-train-v2-scalar-unc\": {}, \"crm-train-v2-perdof\": {}, \"crm-train-v2-obs-only\": {}, \"precompute-shard2\": {}, \"precompute-shard1\": {}, \"precompute-shard0\": {}, \"precompute-k5\": {}, \"plan_014-reconvla-baseline\": {}, \"plan_001-crm-smolvla\": {}, \"mvp-point-reaching\": {}, \"eval-smolvla-libero-spatial\": {}, \"eval-obs-only-spatial\": {}, \"eval-obs-only-object-default-seed44\": {}, \"eval-mag-perdof-norm005-object\": {}, \"eval-mag-perdof-norm02-seed43-object-r3\": {}, \"eval-mag-perdof-norm03-object-r3\": {}, \"eval-mag-obsonly-norm005\": {}, \"eval-mag-obsonly-norm003-b2\": {}, \"eval-mag-obsonly-norm03-object\": {}, \"eval-mag-obsonly-norm005-object\": {}, \"eval-direct-correction-object-seed42-r2\": {}, \"eval-direct-correction-object-seed42\": {}, \"eval-scalar-object-seed44-r2\": {}, \"eval-perdof-object-seed44\": {}, \"eval-obs-only-object-norm03-seed44\": {}, \"eval-vla-mean-object-seed44\": {}, \"eval-obs-only-object-norm02-seed44-r4\": {}, \"eval-argmin-object-seed44-r2\": {}, \"eval-obs-only-object-norm03-seed45\": {}, \"eval-acr-object-v4-default-r2\": {}, \"eval-mag-perdof-norm003-object\": {}, \"eval-acr-object-obs-only-default\": {}, \"eval-scalar-object-seed43\": {}, \"eval-mag-obsonly-norm003-object\": {}, \"eval-scalar-object-seed44\": {}, \"eval-obs-only-object-norm02-seed44-r3\": {}, \"eval-argmin-object-seed44-r3\": {}, \"eval-vla-mean-object-seed43\": {}, \"eval-perdof-object-seed43\": {}, \"eval-vla-only-object-seed44\": {}, \"eval-obs-only-object-norm02-seed44\": {}, \"eval-argmin-object-seed44\": {}, \"eval-obs-only-object-seed43\": {}, \"eval-mag-obsonly-norm03-b2\": {}, \"eval-argmin-object-seed43\": {}, \"eval-mag-perdof-norm02-seed43-object-r2\": {}, \"eval-mag-obsonly-norm03\": {}, \"eval-mag-obsonly-norm02-object\": {}, \"eval-mag-obsonly-norm03-b4\": {}, \"eval-mag-obsonly-norm03-b3\": {}, \"eval-mag-perdof-norm02-seed43-object\": {}, \"eval-mag-perdof-norm03-object-r2\": {}, \"eval-acr-object-v4-scalar-b2\": {}, \"eval-acr-object-v4-obs-only-b2\": {}, \"eval-spatial-v4-full\": {}, \"eval-reconvla-spatial-v1\": {}, \"eval-object-v6-full\": {}, \"precompute-v3-shard2\": {}, \"precompute-v3-shard1\": {}, \"precompute-v3-shard0\": {}, \"precompute-v2-shard2\": {}, \"precompute-v2-shard1\": {}, \"precompute-v2-shard0\": {}, \"eval-mag-perdof-norm0p3-object-r2\": {}, \"eval-mag-perdof-norm0p3-object\": {}, \"eval-obs-only-object-norm02-seed43\": {}, \"eval-acr-object-v4-default\": {}, \"eval-mag-obsonly-norm03-r2\": {}, \"eval-vla-mean-object\": {}, \"eval-reconvla-object\": {}, \"eval-acr-object-v4-obs-only\": {}, \"eval-acr-object-v4-perdof\": {}, \"eval-acr-spatial-v4-scalar-r2\": {}, \"eval-acr-spatial-v4-obs-only-r3\": {}, \"eval-obs-only-spatial-seed43\": {}, \"eval-acr-spatial-v4-small-r2\": {}, \"eval-mag-obsonly-norm-0.3-r3\": {}, \"eval-mag-obsonly-norm-0p3-r3\": {}, \"eval-argmin-only-spatial-r2\": {}, \"eval-mag-obsonly-norm003\": {}, \"eval-vla-only-object-k1\": {}, \"eval-acr-spatial-v4-default-r3\": {}, \"eval-tiny-correction-spatial\": {}, \"eval-acr-spatial-v4-default-r2\": {}, \"eval-acr-spatial-v4-obs-only\": {}, \"eval-acr-spatial-v4-default\": {}, \"crm-train-v3-norm-scalar-unc\": {}, \"crm-train-v3-norm-obs-only\": {}, \"crm-train-v3-norm\": {}, \"crm-train-v3-scalar-unc\": {}, \"crm-train-v3-obs-only\": {}, \"crm-train-v3-perdof\": {}, \"eval-obs-only-spatial-v3\": {}, \"eval-scalar-unc-spatial-v2\": {}, \"crm-train-a4-scalar-unc\": {}, \"crm-train-a3-obs-only\": {}, \"crm-train-v1\": {}, \"crm-train-k5\": {}, \"eval-scalar-unc-spatial\": {}, \"eval-acr-spatial-v2\": {}, \"eval-k5-spatial\": {}, \"eval-object-v7-full\": {}, \"eval-spatial-v6-full\": {}, \"eval-object-v5-full\": {}, \"eval-acr-vla-spatial-v1\": {}, \"eval-acr-spatial-v1\": {}, \"eval-reconvla-spatial-v2\": {}, \"eval-object-v4-full\": {}, \"eval-spatial-v5-full\": {}, \"eval-spatial-v3-full\": {}, \"eval-spatial-reeval-v2\": {}}, \"count\": 761, \"total\": 761, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.5429}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "f4bfa208-a13d-4717-ac4f-4a0d6bb5b914",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"crm-train-openvla-k1-multiscale-object\\\": {}, \\\"eval-supp-long-k2mean-s46-r2\\\": {}, \\\"eval-supp-long-reconvla-s46-r2\\\": {}, \\\"eval-supp-long-crm-norm005-s46-r2\\\": {}, \\\"eval-supp-long-adapt-tau025-s46-r2\\\": {}, \\\"eval-supp-obj-crm-norm005-s45\\\": {}, \\\"eval-supp-obj-adapt-tau025-s45\\\": {}, \\\"eval-supp-obj-vla-only-s45\\\": {}, \\\"eval-supp-spatial-crm-norm005-s45\\\": {}, \\\"eval-supp-spatial-vla-only-s45\\\": {}, \\\"precompute-pi05-goal-2048-r2\\\": {}, \\\"eval-supp-long-vla-only-s46\\\": {}, \\\"precompute-pi05-spatial-2048-r2\\\": {}, \\\"precompute-smolvla-goal-bjb1-32546\\\": {}, \\\"eval-supp-goal-vla-only-s46\\\": {}, \\\"eval-supp-goal-reconvla-s46\\\": {}, \\\"crm-train-pi05-spatial-full\\\": {}, \\\"eval-obs-only-spatial-v2\\\": {}, \\\"eval-perdof-object-norm003-seed44\\\": {}, \\\"eval-random-selection-spatial-seed42\\\": {}, \\\"eval-adaptive-k-spatial-p90-seed44-bjb2\\\": {}, \\\"eval-supp-goal-vla-only-wrapper-s44\\\": {}, \\\"eval-supp-long-reconvla-s45\\\": {}, \\\"eval-supp-spatial-k2mean-s46\\\": {}, \\\"eval-pi05-vla-only-long-seed42-r4\\\": {}, \\\"eval-supp-reconvla-obj-s45\\\": {}, \\\"eval-pi05-vla-only-object-seed42\\\": {}, \\\"eval-pi05-vla-only-object-seed43\\\": {}, \\\"eval-pi05-vla-only-object-seed44\\\": {}, \\\"eval-supp-long-k2mean-s45\\\": {}, \\\"eval-supp-goal-k2mean-s46\\\": {}, \\\"eval-supp-goal-adapt-tau025-s46\\\": {}, \\\"eval-supp-goal-crm-norm005-s46\\\": {}, \\\"eval-supp-spatial-adapt-tau025-s45-r3\\\": {}, \\\"eval-supp-spatial-k2mean-s45\\\": {}, \\\"eval-supp-spatial-vla-only-s46\\\": {}, \\\"eval-supp-spatial-reconvla-s46\\\": {}, \\\"eval-supp-spatial-adapt-tau025-s46\\\": {}, \\\"eval-supp-spatial-crm-norm005-s46\\\": {}, \\\"eval-supp-long-crm-norm005-s45\\\": {}, \\\"eval-supp-long-adapt-tau025-s45\\\": {}, \\\"eval-supp-long-vla-only-s45\\\": {}, \\\"eval-supp-spatial-reconvla-s45\\\": {}, \\\"eval-supp-goal-k2mean-s45\\\": {}, \\\"eval-supp-adapt-tau025-obj-s45\\\": {}, \\\"eval-supp-obj-k2mean-s45\\\": {}, \\\"eval-supp-crm-obj-s46\\\": {}, \\\"eval-supp-long-k2mean-s44\\\": {}, \\\"eval-supp-long-reconvla-s44\\\": {}, \\\"eval-supp-goal-reconvla-s45\\\": {}, \\\"eval-supp-goal-vla-only-s45\\\": {}, \\\"eval-supp-crm-norm005-obj-s46\\\": {}, \\\"eval-supp-goal-crm-norm005-s45\\\": {}, \\\"eval-supp-crm-norm005-obj-s45\\\": {}, \\\"eval-supp-reconvla-obj-s46\\\": {}, \\\"eval-supp-goal-adapt-tau025-s45\\\": {}, \\\"eval-supp-long-crm-norm005-s44\\\": {}, \\\"eval-supp-long-adapt-tau025-s44\\\": {}, \\\"eval-supp-k2mean-obj-s46\\\": {}, \\\"eval-supp-k2mean-obj-s45\\\": {}, \\\"eval-supp-adapt-tau025-obj-s46\\\": {}, \\\"eval-supp-long-vla-only-s43\\\": {}, \\\"eval-supp-long-k2mean-s42\\\": {}, \\\"eval-supp-obj-vla-only-s46\\\": {}, \\\"eval-supp-long-vla-only-s44\\\": {}, \\\"eval-supp-long-k2mean-s43\\\": {}, \\\"eval-supp-long-reconvla-s43\\\": {}, \\\"eval-supp-long-crm-norm005-s43\\\": {}, \\\"eval-supp-long-adapt-tau025-s43\\\": {}, \\\"eval-supp-obj-adapt-tau025-s45-r2\\\": {}, \\\"eval-supp-long-crm-norm005-s42\\\": {}, \\\"eval-supp-long-adapt-tau025-s42\\\": {}, \\\"eval-supp-long-reconvla-s42\\\": {}, \\\"eval-ablation-tau040-goal-s42\\\": {}, \\\"eval-ablation-tau015-goal-s42\\\": {}, \\\"eval-supp-k2mean-object-s44\\\": {}, \\\"eval-ablation-tau010-goal-s42\\\": {}, \\\"eval-supp-obj-reconvla-s44\\\": {}, \\\"eval-supp-spatial-vla-only-s44\\\": {}, \\\"eval-supp-goal-vla-only-wrapper-s44-r2\\\": {}, \\\"eval-supp-k2mean-spatial-s44\\\": {}, \\\"eval-supp-spatial-vla-only-s43\\\": {}, \\\"eval-supp-k2mean-goal-s44\\\": {}, \\\"eval-supp-adapt-tau025-obj-s44\\\": {}, \\\"eval-supp-crm-norm005-obj-s44\\\": {}, \\\"eval-supp-goal-vla-only-wrapper-s43\\\": {}, \\\"eval-supp-long-vla-only-s42\\\": {}, \\\"eval-supp-goal-reconvla-s44\\\": {}, \\\"eval-supp-obj-reconvla-s43\\\": {}, \\\"eval-supp-crm-norm005-goal-s44\\\": {}, \\\"eval-supp-k2mean-object-s43\\\": {}, \\\"eval-supp-k2mean-goal-s42-r2\\\": {}, \\\"eval-supp-adapt-tau025-goal-s44\\\": {}, \\\"eval-supp-crm-norm005-obj-s43\\\": {}, \\\"eval-supp-adapt-tau025-goal-s43\\\": {}, \\\"eval-supp-crm-norm005-goal-s43\\\": {}, \\\"eval-supp-adapt-tau025-obj-s43\\\": {}, \\\"eval-supp-goal-reconvla-s43\\\": {}, \\\"eval-supp-k2mean-spatial-s43\\\": {}, \\\"eval-supp-reconvla-spatial-s44\\\": {}, \\\"eval-supp-reconvla-spatial-s43\\\": {}, \\\"eval-supp-k2mean-goal-s43\\\": {}, \\\"eval-supp-k2mean-object-s42\\\": {}, \\\"eval-supp-goal-adapt-tau025-s42\\\": {}, \\\"eval-supp-goal-crm005-s42\\\": {}, \\\"eval-supp-goal-reconvla-s42\\\": {}, \\\"train-crm-unified-4suite-r6\\\": {}, \\\"eval-goal-vla-only-wrapper-s42\\\": {}, \\\"eval-supp-obj-adapt-tau025-s42\\\": {}, \\\"eval-supp-k2mean-spatial-s42\\\": {}, \\\"eval-supp-crm-norm005-spatial-s44\\\": {}, \\\"eval-supp-adapt-tau025-spatial-s44\\\": {}, \\\"eval-supp-reconvla-k2-spatial-s42\\\": {}, \\\"eval-supp-adapt-tau025-spatial-s43\\\": {}, \\\"eval-supp-crm-norm005-spatial-s43\\\": {}, \\\"eval-supp-k2mean-goal-s42\\\": {}, \\\"eval-supp-obj-adapt-s42-r2\\\": {}, \\\"eval-object-vla-only-wrapper-s44-r2\\\": {}, \\\"eval-object-vla-only-wrapper-s43-r2\\\": {}, \\\"eval-object-vla-only-wrapper-s42-r2\\\": {}, \\\"eval-supp-obj-reconvla-s42\\\": {}, \\\"eval-supp-obj-crm005-s42-r2\\\": {}, \\\"eval-supp-adapt-tau035-spatial-s42-r2\\\": {}, \\\"eval-supp-adapt-tau015-spatial-s42-r2\\\": {}, \\\"eval-supp-crm-norm02-spatial-s42-r2\\\": {}, \\\"eval-supp-adapt-tau025-spatial-s42-r2\\\": {}, \\\"eval-openvla-object-baseline-seed42-r2\\\": {}, \\\"eval-obs-only-object-norm02-seed55\\\": {}, \\\"precompute-pi05-features-object\\\": {}, \\\"precompute-smolvla-goal-shard2\\\": {}, \\\"precompute-smolvla-goal-shard1\\\": {}, \\\"precompute-smolvla-goal-shard0\\\": {}, \\\"eval-smolvla-long-seed2\\\": {}, \\\"eval-smolvla-long-seed1\\\": {}, \\\"eval-smolvla-long-seed0\\\": {}, \\\"eval-smolvla-crm-spatial-seed42-v1\\\": {}, \\\"eval-smolvla-crm-spatial-seed43-v1\\\": {}, \\\"eval-smolvla-crm-spatial-seed44-v1\\\": {}, \\\"eval-smolvla-crm-goal-seed42-v1\\\": {}, \\\"eval-smolvla-crm-goal-seed43-v1\\\": {}, \\\"eval-smolvla-crm-goal-seed44-v1\\\": {}, \\\"eval-supp-obj-adapt-s42\\\": {}, \\\"eval-crm-norm02-spatial-s42\\\": {}, \\\"eval-adaptive-tau015-spatial-s42\\\": {}, \\\"eval-adaptive-tau025-spatial-s42\\\": {}, \\\"eval-adaptive-tau035-spatial-s42\\\": {}, \\\"train-crm-unified-4suite-r5-resumed\\\": {}, \\\"eval-object-vla-only-wrapper-s44\\\": {}, \\\"eval-object-vla-only-wrapper-s43\\\": {}, \\\"eval-object-vla-only-wrapper-s42\\\": {}, \\\"eval-supp-obj-crm005-s42\\\": {}, \\\"eval-supp-adapt-tau035-spatial-s42\\\": {}, \\\"eval-supp-adapt-tau025-spatial-s42\\\": {}, \\\"eval-supp-adapt-tau015-spatial-s42\\\": {}, \\\"eval-supp-crm-norm02-spatial-s42\\\": {}, \\\"eval-3dir-adaptive-spatial-s42\\\": {}, \\\"eval-3dir-norm03-spatial-s42\\\": {}, \\\"eval-3dir-reconvla-spatial-s42\\\": {}, \\\"eval-3dir-norm01-spatial-s42\\\": {}, \\\"eval-3dir-norm005-spatial-s42\\\": {}, \\\"precompute-pi05-goal-2048\\\": {}, \\\"precompute-pi05-spatial-2048\\\": {}, \\\"precompute-pi05-object-2048\\\": {}, \\\"eval-smolvla-crm-object-seed43-v1\\\": {}, \\\"eval-smolvla-crm-object-seed42-v1\\\": {}, \\\"eval-smolvla-crm-object-seed44-v1\\\": {}, \\\"train-crm-unified-4suite-r5\\\": {}, \\\"eval-smolvla-crm-goal-seed43\\\": {}, \\\"eval-smolvla-crm-goal-seed42\\\": {}, \\\"eval-smolvla-crm-spatial-seed44\\\": {}, \\\"eval-smolvla-crm-spatial-seed43\\\": {}, \\\"eval-smolvla-crm-spatial-seed42\\\": {}, \\\"precompute-pi05-long-2048\\\": {}, \\\"eval-smolvla-lerobot-goal-seed44-v3\\\": {}, \\\"eval-smolvla-lerobot-goal-seed43-v3\\\": {}, \\\"eval-smolvla-lerobot-spatial-seed43-v3\\\": {}, \\\"train-crm-smolvla-3suite-v1\\\": {}, \\\"eval-smolvla-lerobot-goal-seed43-v2\\\": {}, \\\"eval-smolvla-lerobot-spatial-seed43-v2\\\": {}, \\\"eval-smolvla-lerobot-object-seed44-v2\\\": {}, \\\"eval-smolvla-lerobot-object-seed43-v2\\\": {}, \\\"eval-smolvla-lerobot-goal-seed43\\\": {}, \\\"eval-smolvla-lerobot-spatial-seed43\\\": {}, \\\"eval-smolvla-lerobot-object-seed44\\\": {}, \\\"eval-smolvla-lerobot-object-seed43\\\": {}, \\\"eval-smolvla-lerobot-spatial-seed44\\\": {}, \\\"precompute-smolvla-long-wrapper-bjb1\\\": {}, \\\"eval-smolvla-lerobot-long-seed44\\\": {}, \\\"eval-smolvla-lerobot-long-seed43\\\": {}, \\\"eval-smolvla-lerobot-long-seed42\\\": {}, \\\"train-crm-unified-4suite-r4\\\": {}, \\\"eval-pi05-vla-only-long-seed42-r4-rerun\\\": {}, \\\"eval-pi05-crm-object-seed44\\\": {}, \\\"eval-pi05-crm-object-seed43\\\": {}, \\\"eval-pi05-crm-object-seed42\\\": {}, \\\"eval-pi05-vla-only-long-seed43-r4-std\\\": {}, \\\"eval-pi05-vla-only-goal-seed44-r4-std\\\": {}, \\\"eval-pi05-vla-only-goal-seed42-r4-std\\\": {}, \\\"eval-pi05-vla-only-long-seed44-r4-std\\\": {}, \\\"eval-pi05-vla-only-goal-seed43-r4-std\\\": {}, \\\"eval-pi05-vla-only-goal-seed42-r4\\\": {}, \\\"precompute-smolvla-long-k2\\\": {}, \\\"train-crm-unified-4suite-r3\\\": {}, \\\"train-crm-unified-4suite-r2\\\": {}, \\\"precompute-smolvla-goal-bjb2-28827\\\": {}, \\\"precompute-smolvla-long-bjb2-28827\\\": {}, \\\"eval-pi05-vla-only-spatial-seed44-r4\\\": {}, \\\"eval-pi05-vla-only-spatial-seed43-r4\\\": {}, \\\"eval-pi05-vla-only-spatial-seed42-r4\\\": {}, \\\"eval-pi05-vla-only-long-seed44-r4\\\": {}, \\\"eval-pi05-vla-only-long-seed43-r4\\\": {}, \\\"eval-pi05-vla-only-goal-seed44-r4\\\": {}, \\\"eval-pi05-vla-only-goal-seed43-r4\\\": {}, \\\"eval-openvla-oft-official-object\\\": {}, \\\"eval-pi05-crm-spatial-seed44\\\": {}, \\\"eval-pi05-crm-spatial-seed43\\\": {}, \\\"eval-pi05-crm-spatial-seed42\\\": {}, \\\"eval-pi05-vla-only-object-seed43-r4\\\": {}, \\\"eval-pi05-vla-only-object-seed44-r4\\\": {}, \\\"eval-smolvla-lerobot-official-object\\\": {}, \\\"eval-pi05-vla-only-object-seed42-r4\\\": {}, \\\"train-crm-unified-4suite\\\": {}, \\\"precompute-smolvla-long-bjb1-32546-r2\\\": {}, \\\"precompute-smolvla-long-bjb1-32546\\\": {}, \\\"eval-loss-perdof-object-seed42\\\": {}, \\\"eval-loss-combined-object-seed42\\\": {}, \\\"eval-loss-conformal-object-seed42\\\": {}, \\\"eval-loss-mse-object-seed42\\\": {}, \\\"eval-openvla-oft-object-baseline-seed42\\\": {}, \\\"precompute-smolvla-long-bjb1-18228\\\": {}, \\\"crm-loss-combined\\\": {}, \\\"crm-loss-conformal\\\": {}, \\\"precompute-smolvla-goal-bjb1-18228\\\": {}, \\\"crm-loss-perdof\\\": {}, \\\"crm-loss-mse-baseline\\\": {}, \\\"eval-smolvla-acr-goal-seed43\\\": {}, \\\"eval-smolvla-crm-long-seed44-v2\\\": {}, \\\"eval-smolvla-crm-goal-seed44-v2\\\": {}, \\\"eval-smolvla-crm-long-seed43-v2\\\": {}, \\\"eval-smolvla-acr-long-seed42\\\": {}, \\\"eval-smolvla-acr-goal-seed42\\\": {}, \\\"crm-train-pi05-spatial-v2\\\": {}, \\\"crm-train-pi05-object-full\\\": {}, \\\"crm-train-pi05-spatial\\\": {}, \\\"crm-train-pi05-object\\\": {}, \\\"eval-pi05-vla-only-spatial-seed45\\\": {}, \\\"eval-pi05-vla-only-spatial-seed43-r3\\\": {}, \\\"eval-pi05-vla-only-spatial-seed42-r3\\\": {}, \\\"eval-pi05-vla-only-object-seed44-r3\\\": {}, \\\"eval-pi05-vla-only-object-seed43-r3\\\": {}, \\\"eval-pi05-vla-only-object-seed42-r3\\\": {}, \\\"eval-spatial-obs-only-seed45\\\": {}, \\\"eval-pi05-vla-only-spatial-seed44\\\": {}, \\\"eval-pi05-vla-only-spatial-seed43\\\": {}, \\\"eval-pi05-vla-only-spatial-seed42\\\": {}, \\\"eval-k20-obs-only-spatial-seed44\\\": {}, \\\"eval-k20-obs-only-spatial-seed43\\\": {}, \\\"eval-k20-obs-only-spatial-seed42\\\": {}, \\\"eval-k20-obs-only-object-seed45\\\": {}, \\\"eval-obs-only-object-norm003-seed66\\\": {}, \\\"eval-obs-only-object-norm01-seed66\\\": {}, \\\"eval-obs-only-object-norm005-seed66\\\": {}, \\\"eval-obs-only-object-norm003-seed67\\\": {}, \\\"eval-k20-obs-only-object-seed44\\\": {}, \\\"eval-k20-obs-only-object-seed43\\\": {}, \\\"eval-k20-obs-only-object-seed42\\\": {}, \\\"eval-crm-object-k20-seed44\\\": {}, \\\"eval-crm-object-k20-seed42\\\": {}, \\\"eval-obs-only-object-norm02-seed53\\\": {}, \\\"eval-obs-only-object-norm02-seed52\\\": {}, \\\"eval-obs-only-object-norm02-seed51\\\": {}, \\\"eval-obs-only-object-norm02-seed50\\\": {}, \\\"eval-obs-only-object-norm02-seed48-r2\\\": {}, \\\"eval-obs-only-object-norm02-seed47\\\": {}, \\\"eval-obs-only-object-norm02-seed46\\\": {}, \\\"eval-obs-only-object-norm02-seed45\\\": {}, \\\"eval-obs-only-object-norm02-seed44-r2\\\": {}, \\\"eval-obs-only-object-norm02-seed43-r3\\\": {}, \\\"eval-obs-only-object-norm02-seed43-r2\\\": {}, \\\"eval-obs-only-object-norm005-seed67\\\": {}, \\\"eval-obs-only-object-norm01-seed67\\\": {}, \\\"eval-vla-only-object-seed50\\\": {}, \\\"eval-vla-only-object-seed49\\\": {}, \\\"eval-vla-only-object-seed48\\\": {}, \\\"eval-vla-only-object-seed46\\\": {}, \\\"eval-vla-only-object-seed45\\\": {}, \\\"eval-vla-only-object-seed44-r2\\\": {}, \\\"eval-plan-a-object-seed42\\\": {}, \\\"eval-vla-only-object-seed43\\\": {}, \\\"eval-vla-only-object\\\": {}, \\\"eval-plan-a-spatial-seed43\\\": {}, \\\"eval-plan-a-object-seed44\\\": {}, \\\"eval-plan-a-spatial-seed42\\\": {}, \\\"eval-plan-a-spatial-seed44\\\": {}, \\\"eval-plan-a-object-seed43\\\": {}, \\\"eval-random-selection-object-seed44\\\": {}, \\\"eval-random-selection-object-seed43\\\": {}, \\\"eval-obs-only-object-norm01-seed60\\\": {}, \\\"eval-pi05-baseline-object-seed42\\\": {}, \\\"eval-obs-only-object-norm01-seed54\\\": {}, \\\"eval-obs-only-object-norm01-seed53\\\": {}, \\\"eval-obs-only-object-norm01-seed52\\\": {}, \\\"eval-obs-only-object-norm01-seed50\\\": {}, \\\"eval-obs-only-object-norm01-seed49\\\": {}, \\\"eval-obs-only-object-norm01-seed48\\\": {}, \\\"eval-obs-only-object-norm01-seed47\\\": {}, \\\"eval-obs-only-object-norm01-seed45-r2\\\": {}, \\\"eval-obs-only-object-norm01-seed44\\\": {}, \\\"eval-obs-only-object-norm005-seed55\\\": {}, \\\"eval-obs-only-object-norm005-seed50\\\": {}, \\\"eval-obs-only-object-norm005-seed49\\\": {}, \\\"eval-obs-only-object-norm005-seed48\\\": {}, \\\"eval-obs-only-object-norm005-seed47\\\": {}, \\\"eval-obs-only-object-norm005-seed44\\\": {}, \\\"eval-obs-only-object-norm005-seed43-r2\\\": {}, \\\"eval-obs-only-object-norm005-seed43\\\": {}, \\\"eval-obs-only-object-norm003-seed48\\\": {}, \\\"eval-obs-only-object-norm003-seed47-r2\\\": {}, \\\"eval-obs-only-object-norm003-seed46\\\": {}, \\\"eval-obs-only-object-norm003-seed45\\\": {}, \\\"eval-obs-only-object-norm003-seed44-bjb2\\\": {}, \\\"eval-obs-only-object-norm003-seed44\\\": {}, \\\"eval-obs-only-object-norm003-seed43-r2\\\": {}, \\\"eval-obs-only-object-norm003-seed43\\\": {}, \\\"eval-obs-only-object-norm01-seed57\\\": {}, \\\"eval-obs-only-object-norm005-seed65\\\": {}, \\\"eval-obs-only-object-norm005-seed61\\\": {}, \\\"eval-obs-only-object-norm005-seed58\\\": {}, \\\"eval-obs-only-object-norm003-seed59\\\": {}, \\\"eval-obs-only-object-norm003-seed56\\\": {}, \\\"eval-obs-only-object-norm005-seed75\\\": {}, \\\"eval-obs-only-object-norm01-seed74\\\": {}, \\\"eval-obs-only-object-norm005-seed72\\\": {}, \\\"eval-obs-only-object-norm003-seed63-r2\\\": {}, \\\"eval-obs-only-object-norm01-seed71\\\": {}, \\\"eval-obs-only-object-norm003-seed62-r2\\\": {}, \\\"eval-obs-only-object-norm003-seed73\\\": {}, \\\"eval-obs-only-object-norm01-seed51-r3\\\": {}, \\\"eval-obs-only-object-norm01-seed52-r3\\\": {}, \\\"eval-obs-only-object-norm01-seed65\\\": {}, \\\"eval-obs-only-object-norm01-seed64\\\": {}, \\\"eval-obs-only-object-norm005-seed64\\\": {}, \\\"eval-obs-only-object-norm003-seed65\\\": {}, \\\"eval-obs-only-object-norm003-seed64\\\": {}, \\\"eval-obs-only-object-norm005-seed62\\\": {}, \\\"eval-obs-only-object-norm005-seed63\\\": {}, \\\"eval-obs-only-object-norm01-seed61\\\": {}, \\\"eval-obs-only-object-norm003-seed64-bjb2\\\": {}, \\\"eval-obs-only-object-norm003-seed63\\\": {}, \\\"eval-obs-only-object-norm003-seed62\\\": {}, \\\"eval-obs-only-object-norm01-seed51-r2\\\": {}, \\\"eval-obs-only-object-norm01-seed52-r2\\\": {}, \\\"eval-obs-only-object-norm01-seed51\\\": {}, \\\"eval-obs-only-object-norm005-seed49-r2\\\": {}, \\\"eval-obs-only-object-norm005-seed55-r2\\\": {}, \\\"eval-openvla-crm-object-seed42\\\": {}, \\\"eval-obs-only-object-norm003-seed44-r2\\\": {}, \\\"eval-random-selection-object-seed49\\\": {}, \\\"eval-random-selection-object-seed48\\\": {}, \\\"eval-k5-obs-only-object-seed44\\\": {}, \\\"eval-obs-only-spatial-norm02-seed52\\\": {}, \\\"eval-obs-only-object-norm02-seed54\\\": {}, \\\"D088-eval-adaptive-unc-head-object-seed44\\\": {}, \\\"D088-eval-adaptive-unc-head-object-seed43\\\": {}, \\\"D088-eval-adaptive-unc-head-object-seed42\\\": {}, \\\"eval-adaptive-unc-head-object-seed42\\\": {}, \\\"eval-adaptive-unc-head-object-seed43\\\": {}, \\\"eval-perdof-object-norm02-seed50\\\": {}, \\\"eval-adaptive-unc-head-object-seed44\\\": {}, \\\"eval-random-selection-spatial-seed42-r3\\\": {}, \\\"eval-obs-only-spatial-norm02-seed50\\\": {}, \\\"train-crm-openvla-obs-only\\\": {}, \\\"openvla-precompute-k1\\\": {}, \\\"eval-random-selection-object-seed46-r3\\\": {}, \\\"eval-perdof-object-norm02-seed49\\\": {}, \\\"eval-random-selection-object-seed47\\\": {}, \\\"eval-obs-only-spatial-norm02-seed42-r2\\\": {}, \\\"eval-k5-obs-only-object-seed43\\\": {}, \\\"eval-random-selection-spatial-seed43-r2\\\": {}, \\\"eval-random-selection-spatial-seed44\\\": {}, \\\"eval-crm-k1-object-seed43-plan702\\\": {}, \\\"eval-crm-k1-object-seed42-plan702\\\": {}, \\\"eval-crm-k1-object-seed44-plan702\\\": {}, \\\"eval-random-selection-object-seed46-r2\\\": {}, \\\"eval-random-selection-spatial-seed43\\\": {}, \\\"eval-random-selection-object-seed46\\\": {}, \\\"eval-obs-only-spatial-seed48\\\": {}, \\\"eval-vla-only-spatial-seed48\\\": {}, \\\"eval-obs-only-spatial-norm02-seed42\\\": {}, \\\"eval-obs-only-spatial-norm02-seed49\\\": {}, \\\"eval-adaptive-k-spatial-p90-seed44\\\": {}, \\\"eval-argmin-object-seed50\\\": {}, \\\"eval-vla-only-object-seed48-r2\\\": {}, \\\"eval-vla-only-goal-seed51\\\": {}, \\\"eval-random-selection-spatial-seed42-r2\\\": {}, \\\"eval-random-selection-object-seed45\\\": {}, \\\"eval-crm-k1-object-seed44-plan702-r2\\\": {}, \\\"eval-crm-k1-object-seed43-plan702-r2\\\": {}, \\\"eval-crm-k1-object-seed42-plan702-r2\\\": {}, \\\"eval-perdof-object-norm02-seed48\\\": {}, \\\"eval-argmin-object-k5-seed44-r2\\\": {}, \\\"eval-vla-only-goal-seed44-r2\\\": {}, \\\"eval-obs-only-spatial-norm02-seed46-r2\\\": {}, \\\"eval-latency-profiling-v1\\\": {}, \\\"eval-adaptive-k-spatial-p75-seed44\\\": {}, \\\"eval-obs-only-goal-norm02-seed51\\\": {}, \\\"eval-adaptive-k-spatial-p25-seed44\\\": {}, \\\"eval-openvla-object-baseline-seed42\\\": {}, \\\"eval-argmin-object-seed49\\\": {}, \\\"eval-argmin-object-seed48\\\": {}, \\\"eval-obs-only-spatial-norm02-seed48\\\": {}, \\\"eval-obs-only-goal-norm02-seed52\\\": {}, \\\"eval-adaptive-k-spatial-p90-seed43\\\": {}, \\\"eval-perdof-object-norm02-seed45-r3\\\": {}, \\\"eval-adaptive-k-spatial-p90-seed42\\\": {}, \\\"eval-obs-only-object-norm02-seed49\\\": {}, \\\"eval-vla-only-goal-seed47\\\": {}, \\\"eval-adaptive-k-spatial-p50-seed44\\\": {}, \\\"eval-adaptive-k-spatial-p50-seed43\\\": {}, \\\"eval-adaptive-k-spatial-p50-seed42\\\": {}, \\\"eval-adaptive-k-spatial-p25-seed42\\\": {}, \\\"eval-adaptive-k-spatial-p25-seed43\\\": {}, \\\"eval-adaptive-k-spatial-p75-seed43\\\": {}, \\\"eval-crm-object-k20-seed43\\\": {}, \\\"eval-vla-only-long-seed49-r2\\\": {}, \\\"eval-adaptive-k-spatial-p75-seed42\\\": {}, \\\"eval-adaptive-k-spatial-p50-seed44-r2\\\": {}, \\\"eval-adaptive-k-p75-seed42\\\": {}, \\\"eval-adaptive-k-p75-seed43\\\": {}, \\\"eval-adaptive-k-p50-seed42\\\": {}, \\\"eval-adaptive-k-p50-seed43\\\": {}, \\\"eval-random-selection-object-seed42\\\": {}, \\\"eval-adaptive-k-spatial-p50-seed43-r2\\\": {}, \\\"eval-obs-only-object-norm02-seed42\\\": {}, \\\"latency-profile-n1000\\\": {}, \\\"eval-adaptive-k-p90-seed44\\\": {}, \\\"eval-adaptive-k-p25-seed43\\\": {}, \\\"eval-crm-spatial-k10-seed51\\\": {}, \\\"eval-vla-only-goal-seed49\\\": {}, \\\"eval-vla-only-long-seed52\\\": {}, \\\"eval-vla-only-long-seed51\\\": {}, \\\"eval-vla-only-long-seed50\\\": {}, \\\"eval-crm-long-seed50\\\": {}, \\\"eval-adaptive-k-p25-seed44-r2\\\": {}, \\\"calibrate-crm-correction-signal\\\": {}, \\\"eval-adaptive-k-p25-seed42\\\": {}, \\\"eval-vla-only-goal-seed48-r2\\\": {}, \\\"eval-vla-only-goal-seed47-r2\\\": {}, \\\"eval-crm-goal-seed46\\\": {}, \\\"eval-adaptive-k-p50-seed44\\\": {}, \\\"eval-adaptive-k-p75-seed44\\\": {}, \\\"eval-adaptive-k-p90-seed43\\\": {}, \\\"eval-adaptive-k-p90-seed42\\\": {}, \\\"eval-vla-only-spatial-seed47\\\": {}, \\\"eval-crm-long-seed47\\\": {}, \\\"eval-vla-only-long-seed48\\\": {}, \\\"eval-crm-long-seed46\\\": {}, \\\"eval-crm-goal-seed45-r2\\\": {}, \\\"eval-crm-goal-seed44-r2\\\": {}, \\\"eval-obs-only-spatial-norm02-seed43-r2\\\": {}, \\\"k2-l2-calibration-phase1\\\": {}, \\\"eval-crm-long-seed45\\\": {}, \\\"eval-vla-only-spatial-seed49\\\": {}, \\\"eval-vla-only-goal-seed48\\\": {}, \\\"eval-vla-only-goal-seed43\\\": {}, \\\"eval-vla-only-goal-seed42\\\": {}, \\\"eval-vla-only-object-seed47\\\": {}, \\\"eval-crm-long-seed44\\\": {}, \\\"eval-crm-long-seed43\\\": {}, \\\"eval-crm-long-seed42\\\": {}, \\\"eval-crm-goal-seed42\\\": {}, \\\"eval-crm-goal-seed43\\\": {}, \\\"eval-vla-only-spatial-seed46\\\": {}, \\\"eval-vla-only-long-seed47\\\": {}, \\\"eval-crm-goal-seed45\\\": {}, \\\"eval-crm-goal-seed44\\\": {}, \\\"eval-vla-only-goal-seed45\\\": {}, \\\"eval-vla-only-goal-seed46\\\": {}, \\\"eval-vla-only-long-seed46\\\": {}, \\\"fmvd-calibration-phase1\\\": {}, \\\"eval-vla-only-long-seed45\\\": {}, \\\"eval-perdof-object-norm003-seed47\\\": {}, \\\"eval-perdof-object-norm005-seed47\\\": {}, \\\"eval-vla-only-long-seed44\\\": {}, \\\"eval-vla-only-long-seed42\\\": {}, \\\"eval-vla-only-long-seed43\\\": {}, \\\"eval-obs-only-spatial-norm02-seed43\\\": {}, \\\"eval-obs-only-spatial-norm02-seed47\\\": {}, \\\"eval-obs-only-spatial-norm02-seed46\\\": {}, \\\"eval-argmin-object-k5-seed44\\\": {}, \\\"eval-vla-only-goal-seed44\\\": {}, \\\"eval-random-selection-object-k5-seed45-r2\\\": {}, \\\"eval-random-selection-object-k5-seed44-r2\\\": {}, \\\"eval-random-selection-object-k5-seed43-r2\\\": {}, \\\"eval-random-selection-object-k5-seed42-r2\\\": {}, \\\"eval-obs-only-spatial-norm02-k5-seed44-r2\\\": {}, \\\"eval-obs-only-spatial-norm02-k5-seed45-r2\\\": {}, \\\"plan_602-latency-profiling\\\": {}, \\\"eval-vla-only-spatial-seed45\\\": {}, \\\"eval-perdof-object-norm005-seed45-r2\\\": {}, \\\"eval-vla-only-spatial-seed44\\\": {}, \\\"eval-obs-only-object-default-seed48-r2\\\": {}, \\\"eval-vla-only-spatial-seed43\\\": {}, \\\"eval-vla-only-spatial-seed42\\\": {}, \\\"eval-obs-only-spatial-norm02-k5-seed45\\\": {}, \\\"eval-obs-only-spatial-norm02-k5-seed44\\\": {}, \\\"eval-random-selection-object-k5-seed45\\\": {}, \\\"eval-random-selection-object-k5-seed44\\\": {}, \\\"eval-random-selection-object-k5-seed43\\\": {}, \\\"eval-random-selection-object-k5-seed42\\\": {}, \\\"eval-obs-only-spatial-norm02-seed44\\\": {}, \\\"eval-perdof-object-norm01-seed43\\\": {}, \\\"eval-obs-only-object-default-seed45-r2\\\": {}, \\\"eval-argmin-object-k5-seed42\\\": {}, \\\"eval-argmin-object-k5-seed45\\\": {}, \\\"eval-argmin-object-k5-seed43\\\": {}, \\\"eval-perdof-object-norm03-seed43\\\": {}, \\\"eval-obs-only-spatial-norm02-seed45\\\": {}, \\\"train-crm-k1-accg-object-seed42-full\\\": {}, \\\"plan_701-precompute-k1-spatial\\\": {}, \\\"plan_701-crm-k1-train\\\": {}, \\\"eval_obs_only_norm03_seed48\\\": {}, \\\"eval_obs_only_norm01_seed48\\\": {}, \\\"eval-lto-splitA-vla-only-r3\\\": {}, \\\"eval-lto-splitA-vla-only-r2\\\": {}, \\\"eval-lto-splitA-heldout-r2\\\": {}, \\\"crm-lto-splitA-train\\\": {}, \\\"eval-perdof-object-norm003-seed48\\\": {}, \\\"eval-scalar-object-seed45-r2\\\": {}, \\\"eval-obs-only-spatial-norm02-k5-seed43\\\": {}, \\\"eval-obs-only-object-norm02-k5-seed48\\\": {}, \\\"eval-obs-only-spatial-norm02-k5-seed42\\\": {}, \\\"eval-obs-only-object-norm02-k5-seed46\\\": {}, \\\"eval-lto-splitA-vla-only-v2\\\": {}, \\\"eval-lto-splitA-heldout-v2\\\": {}, \\\"eval-perdof-object-default-seed47\\\": {}, \\\"eval-perdof-object-norm03-seed47\\\": {}, \\\"eval-obs-only-object-default-seed48\\\": {}, \\\"eval-perdof-object-norm003-seed46\\\": {}, \\\"eval-perdof-object-norm005-seed46\\\": {}, \\\"eval-perdof-object-norm003-seed45\\\": {}, \\\"eval-obs-only-object-norm02-k5-seed47\\\": {}, \\\"eval-perdof-object-norm01-seed48\\\": {}, \\\"eval-obs-only-object-default-seed47\\\": {}, \\\"eval-perdof-object-norm03-seed46\\\": {}, \\\"eval-obs-only-object-norm03-seed46\\\": {}, \\\"eval-scalar-object-seed46\\\": {}, \\\"eval-obs-only-object-norm003-seed45-r2\\\": {}, \\\"eval-lto-splitA-vla-only\\\": {}, \\\"eval-lto-splitA-heldout\\\": {}, \\\"eval-obs-only-object-norm005-seed46\\\": {}, \\\"eval-perdof-object-norm03-seed48\\\": {}, \\\"eval-obs-only-object-norm003-seed49\\\": {}, \\\"crm-lto-splitA-train-fixed\\\": {}, \\\"eval-obs-only-object-norm003-seed47\\\": {}, \\\"eval-perdof-object-norm003-seed43\\\": {}, \\\"eval-perdof-object-norm005-seed43\\\": {}, \\\"eval-perdof-object-default-seed43\\\": {}, \\\"eval-perdof-object-default-seed45\\\": {}, \\\"eval-obs-only-object-norm02-k5-seed45\\\": {}, \\\"eval-perdof-object-norm005-seed45\\\": {}, \\\"eval-obs-only-object-norm02-k5-seed44\\\": {}, \\\"eval-perdof-object-norm003-seed44-r2\\\": {}, \\\"eval-obs-only-object-norm01-seed46-r3\\\": {}, \\\"eval-perdof-object-norm005-seed44\\\": {}, \\\"eval-vla-only-object-seed45-r2\\\": {}, \\\"eval-obs-only-object-norm03-seed48\\\": {}, \\\"eval-obs-only-object-norm02-k5-seed43\\\": {}, \\\"eval-perdof-object-norm01-seed42-r2\\\": {}, \\\"eval-obs-only-object-norm01-seed42-r2\\\": {}, \\\"eval-perdof-object-norm02-seed43\\\": {}, \\\"eval-perdof-object-norm01-seed46\\\": {}, \\\"eval-obs-only-object-norm01-seed45\\\": {}, \\\"eval-obs-only-object-norm02-k5-seed42\\\": {}, \\\"eval-perdof-object-default-seed46\\\": {}, \\\"eval-perdof-object-default-seed44\\\": {}, \\\"eval-mag-perdof-norm02\\\": {}, \\\"eval-acr-spatial-v4-scalar\\\": {}, \\\"eval-acr-spatial-v4-small\\\": {}, \\\"eval-acr-spatial-v4-obs-only-r2\\\": {}, \\\"eval-argmin-only-spatial\\\": {}, \\\"eval-acr-spatial-v3\\\": {}, \\\"eval-acr-object-v3\\\": {}, \\\"eval-openvla-object-vla-only-seed42\\\": {}, \\\"eval-perdof-object-norm02-seed47\\\": {}, \\\"eval-obs-only-object-norm02-seed48\\\": {}, \\\"eval-obs-only-object-default-seed46\\\": {}, \\\"eval-perdof-object-norm02-seed46\\\": {}, \\\"eval-obs-only-object-norm01-seed46\\\": {}, \\\"mag_obs_only_norm01_seed47\\\": {}, \\\"mag_obs_only_norm01_seed46\\\": {}, \\\"eval-perdof-object-norm02-seed43-r3\\\": {}, \\\"mag_perdof_norm02_seed43_r3\\\": {}, \\\"eval-perdof-object-norm01-seed47-bjb1\\\": {}, \\\"eval-openvla-object-vla-only-seed42-v2\\\": {}, \\\"eval-k1-crm-multiscale-object-seed44-r2\\\": {}, \\\"eval-k1-crm-multiscale-object-seed44\\\": {}, \\\"eval-k1-crm-multiscale-object-seed43\\\": {}, \\\"eval-k1-crm-multiscale-object-seed42\\\": {}, \\\"eval-perdof-object-norm01-seed46-r2\\\": {}, \\\"eval-k1-crm-multiscale-object-seed43-r2\\\": {}, \\\"eval-perdof-object-norm02-seed45-r2\\\": {}, \\\"eval-obs-only-object-norm005-seed43-r3\\\": {}, \\\"plan_602-latency-profile\\\": {}, \\\"train-crm-k1-accg-object-seed42-v2\\\": {}, \\\"eval-k1-crm-accg-object-seed44\\\": {}, \\\"eval-k1-crm-accg-object-seed43\\\": {}, \\\"eval-k1-crm-accg-object-seed42\\\": {}, \\\"eval-obs-only-object-default-seed45\\\": {}, \\\"eval-scalar-object-seed45\\\": {}, \\\"eval-perdof-object-norm02-seed45\\\": {}, \\\"eval-perdof-object-norm02-seed44\\\": {}, \\\"train-crm-k1-accg-object-seed42-fallback\\\": {}, \\\"train-crm-k1-accg-object-seed42\\\": {}, \\\"eval-perdof-object-norm02-seed45-deploy\\\": {}, \\\"eval-obs-only-object-norm01-seed47-r2\\\": {}, \\\"eval-perdof-object-norm03-seed45-r2\\\": {}, \\\"eval-perdof-object-norm03-seed44-r2\\\": {}, \\\"eval-obs-only-object-norm03-seed47\\\": {}, \\\"eval-perdof-object-norm03-seed46-r2\\\": {}, \\\"eval-perdof-object-norm01-seed44\\\": {}, \\\"eval-obs-only-object-norm01-seed47-bjb2\\\": {}, \\\"eval-obs-only-object-norm01-seed46-bjb2\\\": {}, \\\"eval-argmin-object-seed47\\\": {}, \\\"eval-perdof-object-norm01-seed45\\\": {}, \\\"eval-perdof-object-norm01-seed47\\\": {}, \\\"eval-argmin-object-seed46\\\": {}, \\\"eval-obs-only-object-norm03-seed45-r2\\\": {}, \\\"eval-vla-mean-object-seed45\\\": {}, \\\"eval-argmin-object-seed45\\\": {}, \\\"eval-direct-correction-object-seed42-r3\\\": {}, \\\"eval-perdof-object-norm03-seed44\\\": {}, \\\"eval-mag-perdof-norm02-object\\\": {}, \\\"eval-acr-object-v4-scalar\\\": {}, \\\"eval-mag-obsonly-norm02\\\": {}, \\\"eval-mag-perdof-norm03\\\": {}, \\\"eval-mag-perdof-norm005\\\": {}, \\\"eval-mag-perdof-norm003\\\": {}, \\\"eval-vla-mean-spatial\\\": {}, \\\"eval-acr-object-obs-only-norm02\\\": {}, \\\"eval-spatial-v7-full\\\": {}, \\\"eval-object-v8-full\\\": {}, \\\"precompute-v5-shard2\\\": {}, \\\"precompute-v5-shard1\\\": {}, \\\"precompute-v5-shard0\\\": {}, \\\"precompute-v4-shard2\\\": {}, \\\"precompute-v4-shard1\\\": {}, \\\"precompute-v4-shard0\\\": {}, \\\"eval-vla-mean-spatial-t10\\\": {}, \\\"eval-reconvla-spatial-v3\\\": {}, \\\"crm-train-v2-scalar-unc\\\": {}, \\\"crm-train-v2-perdof\\\": {}, \\\"crm-train-v2-obs-only\\\": {}, \\\"precompute-shard2\\\": {}, \\\"precompute-shard1\\\": {}, \\\"precompute-shard0\\\": {}, \\\"precompute-k5\\\": {}, \\\"plan_014-reconvla-baseline\\\": {}, \\\"plan_001-crm-smolvla\\\": {}, \\\"mvp-point-reaching\\\": {}, \\\"eval-smolvla-libero-spatial\\\": {}, \\\"eval-obs-only-spatial\\\": {}, \\\"eval-obs-only-object-default-seed44\\\": {}, \\\"eval-mag-perdof-norm005-object\\\": {}, \\\"eval-mag-perdof-norm02-seed43-object-r3\\\": {}, \\\"eval-mag-perdof-norm03-object-r3\\\": {}, \\\"eval-mag-obsonly-norm005\\\": {}, \\\"eval-mag-obsonly-norm003-b2\\\": {}, \\\"eval-mag-obsonly-norm03-object\\\": {}, \\\"eval-mag-obsonly-norm005-object\\\": {}, \\\"eval-direct-correction-object-seed42-r2\\\": {}, \\\"eval-direct-correction-object-seed42\\\": {}, \\\"eval-scalar-object-seed44-r2\\\": {}, \\\"eval-perdof-object-seed44\\\": {}, \\\"eval-obs-only-object-norm03-seed44\\\": {}, \\\"eval-vla-mean-object-seed44\\\": {}, \\\"eval-obs-only-object-norm02-seed44-r4\\\": {}, \\\"eval-argmin-object-seed44-r2\\\": {}, \\\"eval-obs-only-object-norm03-seed45\\\": {}, \\\"eval-acr-object-v4-default-r2\\\": {}, \\\"eval-mag-perdof-norm003-object\\\": {}, \\\"eval-acr-object-obs-only-default\\\": {}, \\\"eval-scalar-object-seed43\\\": {}, \\\"eval-mag-obsonly-norm003-object\\\": {}, \\\"eval-scalar-object-seed44\\\": {}, \\\"eval-obs-only-object-norm02-seed44-r3\\\": {}, \\\"eval-argmin-object-seed44-r3\\\": {}, \\\"eval-vla-mean-object-seed43\\\": {}, \\\"eval-perdof-object-seed43\\\": {}, \\\"eval-vla-only-object-seed44\\\": {}, \\\"eval-obs-only-object-norm02-seed44\\\": {}, \\\"eval-argmin-object-seed44\\\": {}, \\\"eval-obs-only-object-seed43\\\": {}, \\\"eval-mag-obsonly-norm03-b2\\\": {}, \\\"eval-argmin-object-seed43\\\": {}, \\\"eval-mag-perdof-norm02-seed43-object-r2\\\": {}, \\\"eval-mag-obsonly-norm03\\\": {}, \\\"eval-mag-obsonly-norm02-object\\\": {}, \\\"eval-mag-obsonly-norm03-b4\\\": {}, \\\"eval-mag-obsonly-norm03-b3\\\": {}, \\\"eval-mag-perdof-norm02-seed43-object\\\": {}, \\\"eval-mag-perdof-norm03-object-r2\\\": {}, \\\"eval-acr-object-v4-scalar-b2\\\": {}, \\\"eval-acr-object-v4-obs-only-b2\\\": {}, \\\"eval-spatial-v4-full\\\": {}, \\\"eval-reconvla-spatial-v1\\\": {}, \\\"eval-object-v6-full\\\": {}, \\\"precompute-v3-shard2\\\": {}, \\\"precompute-v3-shard1\\\": {}, \\\"precompute-v3-shard0\\\": {}, \\\"precompute-v2-shard2\\\": {}, \\\"precompute-v2-shard1\\\": {}, \\\"precompute-v2-shard0\\\": {}, \\\"eval-mag-perdof-norm0p3-object-r2\\\": {}, \\\"eval-mag-perdof-norm0p3-object\\\": {}, \\\"eval-obs-only-object-norm02-seed43\\\": {}, \\\"eval-acr-object-v4-default\\\": {}, \\\"eval-mag-obsonly-norm03-r2\\\": {}, \\\"eval-vla-mean-object\\\": {}, \\\"eval-reconvla-object\\\": {}, \\\"eval-acr-object-v4-obs-only\\\": {}, \\\"eval-acr-object-v4-perdof\\\": {}, \\\"eval-acr-spatial-v4-scalar-r2\\\": {}, \\\"eval-acr-spatial-v4-obs-only-r3\\\": {}, \\\"eval-obs-only-spatial-seed43\\\": {}, \\\"eval-acr-spatial-v4-small-r2\\\": {}, \\\"eval-mag-obsonly-norm-0.3-r3\\\": {}, \\\"eval-mag-obsonly-norm-0p3-r3\\\": {}, \\\"eval-argmin-only-spatial-r2\\\": {}, \\\"eval-mag-obsonly-norm003\\\": {}, \\\"eval-vla-only-object-k1\\\": {}, \\\"eval-acr-spatial-v4-default-r3\\\": {}, \\\"eval-tiny-correction-spatial\\\": {}, \\\"eval-acr-spatial-v4-default-r2\\\": {}, \\\"eval-acr-spatial-v4-obs-only\\\": {}, \\\"eval-acr-spatial-v4-default\\\": {}, \\\"crm-train-v3-norm-scalar-unc\\\": {}, \\\"crm-train-v3-norm-obs-only\\\": {}, \\\"crm-train-v3-norm\\\": {}, \\\"crm-train-v3-scalar-unc\\\": {}, \\\"crm-train-v3-obs-only\\\": {}, \\\"crm-train-v3-perdof\\\": {}, \\\"eval-obs-only-spatial-v3\\\": {}, \\\"eval-scalar-unc-spatial-v2\\\": {}, \\\"crm-train-a4-scalar-unc\\\": {}, \\\"crm-train-a3-obs-only\\\": {}, \\\"crm-train-v1\\\": {}, \\\"crm-train-k5\\\": {}, \\\"eval-scalar-unc-spatial\\\": {}, \\\"eval-acr-spatial-v2\\\": {}, \\\"eval-k5-spatial\\\": {}, \\\"eval-object-v7-full\\\": {}, \\\"eval-spatial-v6-full\\\": {}, \\\"eval-object-v5-full\\\": {}, \\\"eval-acr-vla-spatial-v1\\\": {}, \\\"eval-acr-spatial-v1\\\": {}, \\\"eval-reconvla-spatial-v2\\\": {}, \\\"eval-object-v4-full\\\": {}, \\\"eval-spatial-v5-full\\\": {}, \\\"eval-spatial-v3-full\\\": {}, \\\"eval-spatial-reeval-v2\\\": {}}, \\\"count\\\": 761, \\\"total\\\": 761, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 3.5429}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"crm-train-openvla-k1-multiscale-object\": {}, \"eval-supp-long-k2mean-s46-r2\": {}, \"eval-supp-long-reconvla-s46-r2\": {}, \"eval-supp-long-crm-norm005-s46-r2\": {}, \"eval-supp-long-adapt-tau025-s46-r2\": {}, \"eval-supp-obj-crm-norm005-s45\": {}, \"eval-supp-obj-adapt-tau025-s45\": {}, \"eval-supp-obj-vla-only-s45\": {}, \"eval-supp-spatial-crm-norm005-s45\": {}, \"eval-supp-spatial-vla-only-s45\": {}, \"precompute-pi05-goal-2048-r2\": {}, \"eval-supp-long-vla-only-s46\": {}, \"precompute-pi05-spatial-2048-r2\": {}, \"precompute-smolvla-goal-bjb1-32546\": {}, \"eval-supp-goal-vla-only-s46\": {}, \"eval-supp-goal-reconvla-s46\": {}, \"crm-train-pi05-spatial-full\": {}, \"eval-obs-only-spatial-v2\": {}, \"eval-perdof-object-norm003-seed44\": {}, \"eval-random-selection-spatial-seed42\": {}, \"eval-adaptive-k-spatial-p90-seed44-bjb2\": {}, \"eval-supp-goal-vla-only-wrapper-s44\": {}, \"eval-supp-long-reconvla-s45\": {}, \"eval-supp-spatial-k2mean-s46\": {}, \"eval-pi05-vla-only-long-seed42-r4\": {}, \"eval-supp-reconvla-obj-s45\": {}, \"eval-pi05-vla-only-object-seed42\": {}, \"eval-pi05-vla-only-object-seed43\": {}, \"eval-pi05-vla-only-object-seed44\": {}, \"eval-supp-long-k2mean-s45\": {}, \"eval-supp-goal-k2mean-s46\": {}, \"eval-supp-goal-adapt-tau025-s46\": {}, \"eval-supp-goal-crm-norm005-s46\": {}, \"eval-supp-spatial-adapt-tau025-s45-r3\": {}, \"eval-supp-spatial-k2mean-s45\": {}, \"eval-supp-spatial-vla-only-s46\": {}, \"eval-supp-spatial-reconvla-s46\": {}, \"eval-supp-spatial-adapt-tau025-s46\": {}, \"eval-supp-spatial-crm-norm005-s46\": {}, \"eval-supp-long-crm-norm005-s45\": {}, \"eval-supp-long-adapt-tau025-s45\": {}, \"eval-supp-long-vla-only-s45\": {}, \"eval-supp-spatial-reconvla-s45\": {}, \"eval-supp-goal-k2mean-s45\": {}, \"eval-supp-adapt-tau025-obj-s45\": {}, \"eval-supp-obj-k2mean-s45\": {}, \"eval-supp-crm-obj-s46\": {}, \"eval-supp-long-k2mean-s44\": {}, \"eval-supp-long-reconvla-s44\": {}, \"eval-supp-goal-reconvla-s45\": {}, \"eval-supp-goal-vla-only-s45\": {}, \"eval-supp-crm-norm005-obj-s46\": {}, \"eval-supp-goal-crm-norm005-s45\": {}, \"eval-supp-crm-norm005-obj-s45\": {}, \"eval-supp-reconvla-obj-s46\": {}, \"eval-supp-goal-adapt-tau025-s45\": {}, \"eval-supp-long-crm-norm005-s44\": {}, \"eval-supp-long-adapt-tau025-s44\": {}, \"eval-supp-k2mean-obj-s46\": {}, \"eval-supp-k2mean-obj-s45\": {}, \"eval-supp-adapt-tau025-obj-s46\": {}, \"eval-supp-long-vla-only-s43\": {}, \"eval-supp-long-k2mean-s42\": {}, \"eval-supp-obj-vla-only-s46\": {}, \"eval-supp-long-vla-only-s44\": {}, \"eval-supp-long-k2mean-s43\": {}, \"eval-supp-long-reconvla-s43\": {}, \"eval-supp-long-crm-norm005-s43\": {}, \"eval-supp-long-adapt-tau025-s43\": {}, \"eval-supp-obj-adapt-tau025-s45-r2\": {}, \"eval-supp-long-crm-norm005-s42\": {}, \"eval-supp-long-adapt-tau025-s42\": {}, \"eval-supp-long-reconvla-s42\": {}, \"eval-ablation-tau040-goal-s42\": {}, \"eval-ablation-tau015-goal-s42\": {}, \"eval-supp-k2mean-object-s44\": {}, \"eval-ablation-tau010-goal-s42\": {}, \"eval-supp-obj-reconvla-s44\": {}, \"eval-supp-spatial-vla-only-s44\": {}, \"eval-supp-goal-vla-only-wrapper-s44-r2\": {}, \"eval-supp-k2mean-spatial-s44\": {}, \"eval-supp-spatial-vla-only-s43\": {}, \"eval-supp-k2mean-goal-s44\": {}, \"eval-supp-adapt-tau025-obj-s44\": {}, \"eval-supp-crm-norm005-obj-s44\": {}, \"eval-supp-goal-vla-only-wrapper-s43\": {}, \"eval-supp-long-vla-only-s42\": {}, \"eval-supp-goal-reconvla-s44\": {}, \"eval-supp-obj-reconvla-s43\": {}, \"eval-supp-crm-norm005-goal-s44\": {}, \"eval-supp-k2mean-object-s43\": {}, \"eval-supp-k2mean-goal-s42-r2\": {}, \"eval-supp-adapt-tau025-goal-s44\": {}, \"eval-supp-crm-norm005-obj-s43\": {}, \"eval-supp-adapt-tau025-goal-s43\": {}, \"eval-supp-crm-norm005-goal-s43\": {}, \"eval-supp-adapt-tau025-obj-s43\": {}, \"eval-supp-goal-reconvla-s43\": {}, \"eval-supp-k2mean-spatial-s43\": {}, \"eval-supp-reconvla-spatial-s44\": {}, \"eval-supp-reconvla-spatial-s43\": {}, \"eval-supp-k2mean-goal-s43\": {}, \"eval-supp-k2mean-object-s42\": {}, \"eval-supp-goal-adapt-tau025-s42\": {}, \"eval-supp-goal-crm005-s42\": {}, \"eval-supp-goal-reconvla-s42\": {}, \"train-crm-unified-4suite-r6\": {}, \"eval-goal-vla-only-wrapper-s42\": {}, \"eval-supp-obj-adapt-tau025-s42\": {}, \"eval-supp-k2mean-spatial-s42\": {}, \"eval-supp-crm-norm005-spatial-s44\": {}, \"eval-supp-adapt-tau025-spatial-s44\": {}, \"eval-supp-reconvla-k2-spatial-s42\": {}, \"eval-supp-adapt-tau025-spatial-s43\": {}, \"eval-supp-crm-norm005-spatial-s43\": {}, \"eval-supp-k2mean-goal-s42\": {}, \"eval-supp-obj-adapt-s42-r2\": {}, \"eval-object-vla-only-wrapper-s44-r2\": {}, \"eval-object-vla-only-wrapper-s43-r2\": {}, \"eval-object-vla-only-wrapper-s42-r2\": {}, \"eval-supp-obj-reconvla-s42\": {}, \"eval-supp-obj-crm005-s42-r2\": {}, \"eval-supp-adapt-tau035-spatial-s42-r2\": {}, \"eval-supp-adapt-tau015-spatial-s42-r2\": {}, \"eval-supp-crm-norm02-spatial-s42-r2\": {}, \"eval-supp-adapt-tau025-spatial-s42-r2\": {}, \"eval-openvla-object-baseline-seed42-r2\": {}, \"eval-obs-only-object-norm02-seed55\": {}, \"precompute-pi05-features-object\": {}, \"precompute-smolvla-goal-shard2\": {}, \"precompute-smolvla-goal-shard1\": {}, \"precompute-smolvla-goal-shard0\": {}, \"eval-smolvla-long-seed2\": {}, \"eval-smolvla-long-seed1\": {}, \"eval-smolvla-long-seed0\": {}, \"eval-smolvla-crm-spatial-seed42-v1\": {}, \"eval-smolvla-crm-spatial-seed43-v1\": {}, \"eval-smolvla-crm-spatial-seed44-v1\": {}, \"eval-smolvla-crm-goal-seed42-v1\": {}, \"eval-smolvla-crm-goal-seed43-v1\": {}, \"eval-smolvla-crm-goal-seed44-v1\": {}, \"eval-supp-obj-adapt-s42\": {}, \"eval-crm-norm02-spatial-s42\": {}, \"eval-adaptive-tau015-spatial-s42\": {}, \"eval-adaptive-tau025-spatial-s42\": {}, \"eval-adaptive-tau035-spatial-s42\": {}, \"train-crm-unified-4suite-r5-resumed\": {}, \"eval-object-vla-only-wrapper-s44\": {}, \"eval-object-vla-only-wrapper-s43\": {}, \"eval-object-vla-only-wrapper-s42\": {}, \"eval-supp-obj-crm005-s42\": {}, \"eval-supp-adapt-tau035-spatial-s42\": {}, \"eval-supp-adapt-tau025-spatial-s42\": {}, \"eval-supp-adapt-tau015-spatial-s42\": {}, \"eval-supp-crm-norm02-spatial-s42\": {}, \"eval-3dir-adaptive-spatial-s42\": {}, \"eval-3dir-norm03-spatial-s42\": {}, \"eval-3dir-reconvla-spatial-s42\": {}, \"eval-3dir-norm01-spatial-s42\": {}, \"eval-3dir-norm005-spatial-s42\": {}, \"precompute-pi05-goal-2048\": {}, \"precompute-pi05-spatial-2048\": {}, \"precompute-pi05-object-2048\": {}, \"eval-smolvla-crm-object-seed43-v1\": {}, \"eval-smolvla-crm-object-seed42-v1\": {}, \"eval-smolvla-crm-object-seed44-v1\": {}, \"train-crm-unified-4suite-r5\": {}, \"eval-smolvla-crm-goal-seed43\": {}, \"eval-smolvla-crm-goal-seed42\": {}, \"eval-smolvla-crm-spatial-seed44\": {}, \"eval-smolvla-crm-spatial-seed43\": {}, \"eval-smolvla-crm-spatial-seed42\": {}, \"precompute-pi05-long-2048\": {}, \"eval-smolvla-lerobot-goal-seed44-v3\": {}, \"eval-smolvla-lerobot-goal-seed43-v3\": {}, \"eval-smolvla-lerobot-spatial-seed43-v3\": {}, \"train-crm-smolvla-3suite-v1\": {}, \"eval-smolvla-lerobot-goal-seed43-v2\": {}, \"eval-smolvla-lerobot-spatial-seed43-v2\": {}, \"eval-smolvla-lerobot-object-seed44-v2\": {}, \"eval-smolvla-lerobot-object-seed43-v2\": {}, \"eval-smolvla-lerobot-goal-seed43\": {}, \"eval-smolvla-lerobot-spatial-seed43\": {}, \"eval-smolvla-lerobot-object-seed44\": {}, \"eval-smolvla-lerobot-object-seed43\": {}, \"eval-smolvla-lerobot-spatial-seed44\": {}, \"precompute-smolvla-long-wrapper-bjb1\": {}, \"eval-smolvla-lerobot-long-seed44\": {}, \"eval-smolvla-lerobot-long-seed43\": {}, \"eval-smolvla-lerobot-long-seed42\": {}, \"train-crm-unified-4suite-r4\": {}, \"eval-pi05-vla-only-long-seed42-r4-rerun\": {}, \"eval-pi05-crm-object-seed44\": {}, \"eval-pi05-crm-object-seed43\": {}, \"eval-pi05-crm-object-seed42\": {}, \"eval-pi05-vla-only-long-seed43-r4-std\": {}, \"eval-pi05-vla-only-goal-seed44-r4-std\": {}, \"eval-pi05-vla-only-goal-seed42-r4-std\": {}, \"eval-pi05-vla-only-long-seed44-r4-std\": {}, \"eval-pi05-vla-only-goal-seed43-r4-std\": {}, \"eval-pi05-vla-only-goal-seed42-r4\": {}, \"precompute-smolvla-long-k2\": {}, \"train-crm-unified-4suite-r3\": {}, \"train-crm-unified-4suite-r2\": {}, \"precompute-smolvla-goal-bjb2-28827\": {}, \"precompute-smolvla-long-bjb2-28827\": {}, \"eval-pi05-vla-only-spatial-seed44-r4\": {}, \"eval-pi05-vla-only-spatial-seed43-r4\": {}, \"eval-pi05-vla-only-spatial-seed42-r4\": {}, \"eval-pi05-vla-only-long-seed44-r4\": {}, \"eval-pi05-vla-only-long-seed43-r4\": {}, \"eval-pi05-vla-only-goal-seed44-r4\": {}, \"eval-pi05-vla-only-goal-seed43-r4\": {}, \"eval-openvla-oft-official-object\": {}, \"eval-pi05-crm-spatial-seed44\": {}, \"eval-pi05-crm-spatial-seed43\": {}, \"eval-pi05-crm-spatial-seed42\": {}, \"eval-pi05-vla-only-object-seed43-r4\": {}, \"eval-pi05-vla-only-object-seed44-r4\": {}, \"eval-smolvla-lerobot-official-object\": {}, \"eval-pi05-vla-only-object-seed42-r4\": {}, \"train-crm-unified-4suite\": {}, \"precompute-smolvla-long-bjb1-32546-r2\": {}, \"precompute-smolvla-long-bjb1-32546\": {}, \"eval-loss-perdof-object-seed42\": {}, \"eval-loss-combined-object-seed42\": {}, \"eval-loss-conformal-object-seed42\": {}, \"eval-loss-mse-object-seed42\": {}, \"eval-openvla-oft-object-baseline-seed42\": {}, \"precompute-smolvla-long-bjb1-18228\": {}, \"crm-loss-combined\": {}, \"crm-loss-conformal\": {}, \"precompute-smolvla-goal-bjb1-18228\": {}, \"crm-loss-perdof\": {}, \"crm-loss-mse-baseline\": {}, \"eval-smolvla-acr-goal-seed43\": {}, \"eval-smolvla-crm-long-seed44-v2\": {}, \"eval-smolvla-crm-goal-seed44-v2\": {}, \"eval-smolvla-crm-long-seed43-v2\": {}, \"eval-smolvla-acr-long-seed42\": {}, \"eval-smolvla-acr-goal-seed42\": {}, \"crm-train-pi05-spatial-v2\": {}, \"crm-train-pi05-object-full\": {}, \"crm-train-pi05-spatial\": {}, \"crm-train-pi05-object\": {}, \"eval-pi05-vla-only-spatial-seed45\": {}, \"eval-pi05-vla-only-spatial-seed43-r3\": {}, \"eval-pi05-vla-only-spatial-seed42-r3\": {}, \"eval-pi05-vla-only-object-seed44-r3\": {}, \"eval-pi05-vla-only-object-seed43-r3\": {}, \"eval-pi05-vla-only-object-seed42-r3\": {}, \"eval-spatial-obs-only-seed45\": {}, \"eval-pi05-vla-only-spatial-seed44\": {}, \"eval-pi05-vla-only-spatial-seed43\": {}, \"eval-pi05-vla-only-spatial-seed42\": {}, \"eval-k20-obs-only-spatial-seed44\": {}, \"eval-k20-obs-only-spatial-seed43\": {}, \"eval-k20-obs-only-spatial-seed42\": {}, \"eval-k20-obs-only-object-seed45\": {}, \"eval-obs-only-object-norm003-seed66\": {}, \"eval-obs-only-object-norm01-seed66\": {}, \"eval-obs-only-object-norm005-seed66\": {}, \"eval-obs-only-object-norm003-seed67\": {}, \"eval-k20-obs-only-object-seed44\": {}, \"eval-k20-obs-only-object-seed43\": {}, \"eval-k20-obs-only-object-seed42\": {}, \"eval-crm-object-k20-seed44\": {}, \"eval-crm-object-k20-seed42\": {}, \"eval-obs-only-object-norm02-seed53\": {}, \"eval-obs-only-object-norm02-seed52\": {}, \"eval-obs-only-object-norm02-seed51\": {}, \"eval-obs-only-object-norm02-seed50\": {}, \"eval-obs-only-object-norm02-seed48-r2\": {}, \"eval-obs-only-object-norm02-seed47\": {}, \"eval-obs-only-object-norm02-seed46\": {}, \"eval-obs-only-object-norm02-seed45\": {}, \"eval-obs-only-object-norm02-seed44-r2\": {}, \"eval-obs-only-object-norm02-seed43-r3\": {}, \"eval-obs-only-object-norm02-seed43-r2\": {}, \"eval-obs-only-object-norm005-seed67\": {}, \"eval-obs-only-object-norm01-seed67\": {}, \"eval-vla-only-object-seed50\": {}, \"eval-vla-only-object-seed49\": {}, \"eval-vla-only-object-seed48\": {}, \"eval-vla-only-object-seed46\": {}, \"eval-vla-only-object-seed45\": {}, \"eval-vla-only-object-seed44-r2\": {}, \"eval-plan-a-object-seed42\": {}, \"eval-vla-only-object-seed43\": {}, \"eval-vla-only-object\": {}, \"eval-plan-a-spatial-seed43\": {}, \"eval-plan-a-object-seed44\": {}, \"eval-plan-a-spatial-seed42\": {}, \"eval-plan-a-spatial-seed44\": {}, \"eval-plan-a-object-seed43\": {}, \"eval-random-selection-object-seed44\": {}, \"eval-random-selection-object-seed43\": {}, \"eval-obs-only-object-norm01-seed60\": {}, \"eval-pi05-baseline-object-seed42\": {}, \"eval-obs-only-object-norm01-seed54\": {}, \"eval-obs-only-object-norm01-seed53\": {}, \"eval-obs-only-object-norm01-seed52\": {}, \"eval-obs-only-object-norm01-seed50\": {}, \"eval-obs-only-object-norm01-seed49\": {}, \"eval-obs-only-object-norm01-seed48\": {}, \"eval-obs-only-object-norm01-seed47\": {}, \"eval-obs-only-object-norm01-seed45-r2\": {}, \"eval-obs-only-object-norm01-seed44\": {}, \"eval-obs-only-object-norm005-seed55\": {}, \"eval-obs-only-object-norm005-seed50\": {}, \"eval-obs-only-object-norm005-seed49\": {}, \"eval-obs-only-object-norm005-seed48\": {}, \"eval-obs-only-object-norm005-seed47\": {}, \"eval-obs-only-object-norm005-seed44\": {}, \"eval-obs-only-object-norm005-seed43-r2\": {}, \"eval-obs-only-object-norm005-seed43\": {}, \"eval-obs-only-object-norm003-seed48\": {}, \"eval-obs-only-object-norm003-seed47-r2\": {}, \"eval-obs-only-object-norm003-seed46\": {}, \"eval-obs-only-object-norm003-seed45\": {}, \"eval-obs-only-object-norm003-seed44-bjb2\": {}, \"eval-obs-only-object-norm003-seed44\": {}, \"eval-obs-only-object-norm003-seed43-r2\": {}, \"eval-obs-only-object-norm003-seed43\": {}, \"eval-obs-only-object-norm01-seed57\": {}, \"eval-obs-only-object-norm005-seed65\": {}, \"eval-obs-only-object-norm005-seed61\": {}, \"eval-obs-only-object-norm005-seed58\": {}, \"eval-obs-only-object-norm003-seed59\": {}, \"eval-obs-only-object-norm003-seed56\": {}, \"eval-obs-only-object-norm005-seed75\": {}, \"eval-obs-only-object-norm01-seed74\": {}, \"eval-obs-only-object-norm005-seed72\": {}, \"eval-obs-only-object-norm003-seed63-r2\": {}, \"eval-obs-only-object-norm01-seed71\": {}, \"eval-obs-only-object-norm003-seed62-r2\": {}, \"eval-obs-only-object-norm003-seed73\": {}, \"eval-obs-only-object-norm01-seed51-r3\": {}, \"eval-obs-only-object-norm01-seed52-r3\": {}, \"eval-obs-only-object-norm01-seed65\": {}, \"eval-obs-only-object-norm01-seed64\": {}, \"eval-obs-only-object-norm005-seed64\": {}, \"eval-obs-only-object-norm003-seed65\": {}, \"eval-obs-only-object-norm003-seed64\": {}, \"eval-obs-only-object-norm005-seed62\": {}, \"eval-obs-only-object-norm005-seed63\": {}, \"eval-obs-only-object-norm01-seed61\": {}, \"eval-obs-only-object-norm003-seed64-bjb2\": {}, \"eval-obs-only-object-norm003-seed63\": {}, \"eval-obs-only-object-norm003-seed62\": {}, \"eval-obs-only-object-norm01-seed51-r2\": {}, \"eval-obs-only-object-norm01-seed52-r2\": {}, \"eval-obs-only-object-norm01-seed51\": {}, \"eval-obs-only-object-norm005-seed49-r2\": {}, \"eval-obs-only-object-norm005-seed55-r2\": {}, \"eval-openvla-crm-object-seed42\": {}, \"eval-obs-only-object-norm003-seed44-r2\": {}, \"eval-random-selection-object-seed49\": {}, \"eval-random-selection-object-seed48\": {}, \"eval-k5-obs-only-object-seed44\": {}, \"eval-obs-only-spatial-norm02-seed52\": {}, \"eval-obs-only-object-norm02-seed54\": {}, \"D088-eval-adaptive-unc-head-object-seed44\": {}, \"D088-eval-adaptive-unc-head-object-seed43\": {}, \"D088-eval-adaptive-unc-head-object-seed42\": {}, \"eval-adaptive-unc-head-object-seed42\": {}, \"eval-adaptive-unc-head-object-seed43\": {}, \"eval-perdof-object-norm02-seed50\": {}, \"eval-adaptive-unc-head-object-seed44\": {}, \"eval-random-selection-spatial-seed42-r3\": {}, \"eval-obs-only-spatial-norm02-seed50\": {}, \"train-crm-openvla-obs-only\": {}, \"openvla-precompute-k1\": {}, \"eval-random-selection-object-seed46-r3\": {}, \"eval-perdof-object-norm02-seed49\": {}, \"eval-random-selection-object-seed47\": {}, \"eval-obs-only-spatial-norm02-seed42-r2\": {}, \"eval-k5-obs-only-object-seed43\": {}, \"eval-random-selection-spatial-seed43-r2\": {}, \"eval-random-selection-spatial-seed44\": {}, \"eval-crm-k1-object-seed43-plan702\": {}, \"eval-crm-k1-object-seed42-plan702\": {}, \"eval-crm-k1-object-seed44-plan702\": {}, \"eval-random-selection-object-seed46-r2\": {}, \"eval-random-selection-spatial-seed43\": {}, \"eval-random-selection-object-seed46\": {}, \"eval-obs-only-spatial-seed48\": {}, \"eval-vla-only-spatial-seed48\": {}, \"eval-obs-only-spatial-norm02-seed42\": {}, \"eval-obs-only-spatial-norm02-seed49\": {}, \"eval-adaptive-k-spatial-p90-seed44\": {}, \"eval-argmin-object-seed50\": {}, \"eval-vla-only-object-seed48-r2\": {}, \"eval-vla-only-goal-seed51\": {}, \"eval-random-selection-spatial-seed42-r2\": {}, \"eval-random-selection-object-seed45\": {}, \"eval-crm-k1-object-seed44-plan702-r2\": {}, \"eval-crm-k1-object-seed43-plan702-r2\": {}, \"eval-crm-k1-object-seed42-plan702-r2\": {}, \"eval-perdof-object-norm02-seed48\": {}, \"eval-argmin-object-k5-seed44-r2\": {}, \"eval-vla-only-goal-seed44-r2\": {}, \"eval-obs-only-spatial-norm02-seed46-r2\": {}, \"eval-latency-profiling-v1\": {}, \"eval-adaptive-k-spatial-p75-seed44\": {}, \"eval-obs-only-goal-norm02-seed51\": {}, \"eval-adaptive-k-spatial-p25-seed44\": {}, \"eval-openvla-object-baseline-seed42\": {}, \"eval-argmin-object-seed49\": {}, \"eval-argmin-object-seed48\": {}, \"eval-obs-only-spatial-norm02-seed48\": {}, \"eval-obs-only-goal-norm02-seed52\": {}, \"eval-adaptive-k-spatial-p90-seed43\": {}, \"eval-perdof-object-norm02-seed45-r3\": {}, \"eval-adaptive-k-spatial-p90-seed42\": {}, \"eval-obs-only-object-norm02-seed49\": {}, \"eval-vla-only-goal-seed47\": {}, \"eval-adaptive-k-spatial-p50-seed44\": {}, \"eval-adaptive-k-spatial-p50-seed43\": {}, \"eval-adaptive-k-spatial-p50-seed42\": {}, \"eval-adaptive-k-spatial-p25-seed42\": {}, \"eval-adaptive-k-spatial-p25-seed43\": {}, \"eval-adaptive-k-spatial-p75-seed43\": {}, \"eval-crm-object-k20-seed43\": {}, \"eval-vla-only-long-seed49-r2\": {}, \"eval-adaptive-k-spatial-p75-seed42\": {}, \"eval-adaptive-k-spatial-p50-seed44-r2\": {}, \"eval-adaptive-k-p75-seed42\": {}, \"eval-adaptive-k-p75-seed43\": {}, \"eval-adaptive-k-p50-seed42\": {}, \"eval-adaptive-k-p50-seed43\": {}, \"eval-random-selection-object-seed42\": {}, \"eval-adaptive-k-spatial-p50-seed43-r2\": {}, \"eval-obs-only-object-norm02-seed42\": {}, \"latency-profile-n1000\": {}, \"eval-adaptive-k-p90-seed44\": {}, \"eval-adaptive-k-p25-seed43\": {}, \"eval-crm-spatial-k10-seed51\": {}, \"eval-vla-only-goal-seed49\": {}, \"eval-vla-only-long-seed52\": {}, \"eval-vla-only-long-seed51\": {}, \"eval-vla-only-long-seed50\": {}, \"eval-crm-long-seed50\": {}, \"eval-adaptive-k-p25-seed44-r2\": {}, \"calibrate-crm-correction-signal\": {}, \"eval-adaptive-k-p25-seed42\": {}, \"eval-vla-only-goal-seed48-r2\": {}, \"eval-vla-only-goal-seed47-r2\": {}, \"eval-crm-goal-seed46\": {}, \"eval-adaptive-k-p50-seed44\": {}, \"eval-adaptive-k-p75-seed44\": {}, \"eval-adaptive-k-p90-seed43\": {}, \"eval-adaptive-k-p90-seed42\": {}, \"eval-vla-only-spatial-seed47\": {}, \"eval-crm-long-seed47\": {}, \"eval-vla-only-long-seed48\": {}, \"eval-crm-long-seed46\": {}, \"eval-crm-goal-seed45-r2\": {}, \"eval-crm-goal-seed44-r2\": {}, \"eval-obs-only-spatial-norm02-seed43-r2\": {}, \"k2-l2-calibration-phase1\": {}, \"eval-crm-long-seed45\": {}, \"eval-vla-only-spatial-seed49\": {}, \"eval-vla-only-goal-seed48\": {}, \"eval-vla-only-goal-seed43\": {}, \"eval-vla-only-goal-seed42\": {}, \"eval-vla-only-object-seed47\": {}, \"eval-crm-long-seed44\": {}, \"eval-crm-long-seed43\": {}, \"eval-crm-long-seed42\": {}, \"eval-crm-goal-seed42\": {}, \"eval-crm-goal-seed43\": {}, \"eval-vla-only-spatial-seed46\": {}, \"eval-vla-only-long-seed47\": {}, \"eval-crm-goal-seed45\": {}, \"eval-crm-goal-seed44\": {}, \"eval-vla-only-goal-seed45\": {}, \"eval-vla-only-goal-seed46\": {}, \"eval-vla-only-long-seed46\": {}, \"fmvd-calibration-phase1\": {}, \"eval-vla-only-long-seed45\": {}, \"eval-perdof-object-norm003-seed47\": {}, \"eval-perdof-object-norm005-seed47\": {}, \"eval-vla-only-long-seed44\": {}, \"eval-vla-only-long-seed42\": {}, \"eval-vla-only-long-seed43\": {}, \"eval-obs-only-spatial-norm02-seed43\": {}, \"eval-obs-only-spatial-norm02-seed47\": {}, \"eval-obs-only-spatial-norm02-seed46\": {}, \"eval-argmin-object-k5-seed44\": {}, \"eval-vla-only-goal-seed44\": {}, \"eval-random-selection-object-k5-seed45-r2\": {}, \"eval-random-selection-object-k5-seed44-r2\": {}, \"eval-random-selection-object-k5-seed43-r2\": {}, \"eval-random-selection-object-k5-seed42-r2\": {}, \"eval-obs-only-spatial-norm02-k5-seed44-r2\": {}, \"eval-obs-only-spatial-norm02-k5-seed45-r2\": {}, \"plan_602-latency-profiling\": {}, \"eval-vla-only-spatial-seed45\": {}, \"eval-perdof-object-norm005-seed45-r2\": {}, \"eval-vla-only-spatial-seed44\": {}, \"eval-obs-only-object-default-seed48-r2\": {}, \"eval-vla-only-spatial-seed43\": {}, \"eval-vla-only-spatial-seed42\": {}, \"eval-obs-only-spatial-norm02-k5-seed45\": {}, \"eval-obs-only-spatial-norm02-k5-seed44\": {}, \"eval-random-selection-object-k5-seed45\": {}, \"eval-random-selection-object-k5-seed44\": {}, \"eval-random-selection-object-k5-seed43\": {}, \"eval-random-selection-object-k5-seed42\": {}, \"eval-obs-only-spatial-norm02-seed44\": {}, \"eval-perdof-object-norm01-seed43\": {}, \"eval-obs-only-object-default-seed45-r2\": {}, \"eval-argmin-object-k5-seed42\": {}, \"eval-argmin-object-k5-seed45\": {}, \"eval-argmin-object-k5-seed43\": {}, \"eval-perdof-object-norm03-seed43\": {}, \"eval-obs-only-spatial-norm02-seed45\": {}, \"train-crm-k1-accg-object-seed42-full\": {}, \"plan_701-precompute-k1-spatial\": {}, \"plan_701-crm-k1-train\": {}, \"eval_obs_only_norm03_seed48\": {}, \"eval_obs_only_norm01_seed48\": {}, \"eval-lto-splitA-vla-only-r3\": {}, \"eval-lto-splitA-vla-only-r2\": {}, \"eval-lto-splitA-heldout-r2\": {}, \"crm-lto-splitA-train\": {}, \"eval-perdof-object-norm003-seed48\": {}, \"eval-scalar-object-seed45-r2\": {}, \"eval-obs-only-spatial-norm02-k5-seed43\": {}, \"eval-obs-only-object-norm02-k5-seed48\": {}, \"eval-obs-only-spatial-norm02-k5-seed42\": {}, \"eval-obs-only-object-norm02-k5-seed46\": {}, \"eval-lto-splitA-vla-only-v2\": {}, \"eval-lto-splitA-heldout-v2\": {}, \"eval-perdof-object-default-seed47\": {}, \"eval-perdof-object-norm03-seed47\": {}, \"eval-obs-only-object-default-seed48\": {}, \"eval-perdof-object-norm003-seed46\": {}, \"eval-perdof-object-norm005-seed46\": {}, \"eval-perdof-object-norm003-seed45\": {}, \"eval-obs-only-object-norm02-k5-seed47\": {}, \"eval-perdof-object-norm01-seed48\": {}, \"eval-obs-only-object-default-seed47\": {}, \"eval-perdof-object-norm03-seed46\": {}, \"eval-obs-only-object-norm03-seed46\": {}, \"eval-scalar-object-seed46\": {}, \"eval-obs-only-object-norm003-seed45-r2\": {}, \"eval-lto-splitA-vla-only\": {}, \"eval-lto-splitA-heldout\": {}, \"eval-obs-only-object-norm005-seed46\": {}, \"eval-perdof-object-norm03-seed48\": {}, \"eval-obs-only-object-norm003-seed49\": {}, \"crm-lto-splitA-train-fixed\": {}, \"eval-obs-only-object-norm003-seed47\": {}, \"eval-perdof-object-norm003-seed43\": {}, \"eval-perdof-object-norm005-seed43\": {}, \"eval-perdof-object-default-seed43\": {}, \"eval-perdof-object-default-seed45\": {}, \"eval-obs-only-object-norm02-k5-seed45\": {}, \"eval-perdof-object-norm005-seed45\": {}, \"eval-obs-only-object-norm02-k5-seed44\": {}, \"eval-perdof-object-norm003-seed44-r2\": {}, \"eval-obs-only-object-norm01-seed46-r3\": {}, \"eval-perdof-object-norm005-seed44\": {}, \"eval-vla-only-object-seed45-r2\": {}, \"eval-obs-only-object-norm03-seed48\": {}, \"eval-obs-only-object-norm02-k5-seed43\": {}, \"eval-perdof-object-norm01-seed42-r2\": {}, \"eval-obs-only-object-norm01-seed42-r2\": {}, \"eval-perdof-object-norm02-seed43\": {}, \"eval-perdof-object-norm01-seed46\": {}, \"eval-obs-only-object-norm01-seed45\": {}, \"eval-obs-only-object-norm02-k5-seed42\": {}, \"eval-perdof-object-default-seed46\": {}, \"eval-perdof-object-default-seed44\": {}, \"eval-mag-perdof-norm02\": {}, \"eval-acr-spatial-v4-scalar\": {}, \"eval-acr-spatial-v4-small\": {}, \"eval-acr-spatial-v4-obs-only-r2\": {}, \"eval-argmin-only-spatial\": {}, \"eval-acr-spatial-v3\": {}, \"eval-acr-object-v3\": {}, \"eval-openvla-object-vla-only-seed42\": {}, \"eval-perdof-object-norm02-seed47\": {}, \"eval-obs-only-object-norm02-seed48\": {}, \"eval-obs-only-object-default-seed46\": {}, \"eval-perdof-object-norm02-seed46\": {}, \"eval-obs-only-object-norm01-seed46\": {}, \"mag_obs_only_norm01_seed47\": {}, \"mag_obs_only_norm01_seed46\": {}, \"eval-perdof-object-norm02-seed43-r3\": {}, \"mag_perdof_norm02_seed43_r3\": {}, \"eval-perdof-object-norm01-seed47-bjb1\": {}, \"eval-openvla-object-vla-only-seed42-v2\": {}, \"eval-k1-crm-multiscale-object-seed44-r2\": {}, \"eval-k1-crm-multiscale-object-seed44\": {}, \"eval-k1-crm-multiscale-object-seed43\": {}, \"eval-k1-crm-multiscale-object-seed42\": {}, \"eval-perdof-object-norm01-seed46-r2\": {}, \"eval-k1-crm-multiscale-object-seed43-r2\": {}, \"eval-perdof-object-norm02-seed45-r2\": {}, \"eval-obs-only-object-norm005-seed43-r3\": {}, \"plan_602-latency-profile\": {}, \"train-crm-k1-accg-object-seed42-v2\": {}, \"eval-k1-crm-accg-object-seed44\": {}, \"eval-k1-crm-accg-object-seed43\": {}, \"eval-k1-crm-accg-object-seed42\": {}, \"eval-obs-only-object-default-seed45\": {}, \"eval-scalar-object-seed45\": {}, \"eval-perdof-object-norm02-seed45\": {}, \"eval-perdof-object-norm02-seed44\": {}, \"train-crm-k1-accg-object-seed42-fallback\": {}, \"train-crm-k1-accg-object-seed42\": {}, \"eval-perdof-object-norm02-seed45-deploy\": {}, \"eval-obs-only-object-norm01-seed47-r2\": {}, \"eval-perdof-object-norm03-seed45-r2\": {}, \"eval-perdof-object-norm03-seed44-r2\": {}, \"eval-obs-only-object-norm03-seed47\": {}, \"eval-perdof-object-norm03-seed46-r2\": {}, \"eval-perdof-object-norm01-seed44\": {}, \"eval-obs-only-object-norm01-seed47-bjb2\": {}, \"eval-obs-only-object-norm01-seed46-bjb2\": {}, \"eval-argmin-object-seed47\": {}, \"eval-perdof-object-norm01-seed45\": {}, \"eval-perdof-object-norm01-seed47\": {}, \"eval-argmin-object-seed46\": {}, \"eval-obs-only-object-norm03-seed45-r2\": {}, \"eval-vla-mean-object-seed45\": {}, \"eval-argmin-object-seed45\": {}, \"eval-direct-correction-object-seed42-r3\": {}, \"eval-perdof-object-norm03-seed44\": {}, \"eval-mag-perdof-norm02-object\": {}, \"eval-acr-object-v4-scalar\": {}, \"eval-mag-obsonly-norm02\": {}, \"eval-mag-perdof-norm03\": {}, \"eval-mag-perdof-norm005\": {}, \"eval-mag-perdof-norm003\": {}, \"eval-vla-mean-spatial\": {}, \"eval-acr-object-obs-only-norm02\": {}, \"eval-spatial-v7-full\": {}, \"eval-object-v8-full\": {}, \"precompute-v5-shard2\": {}, \"precompute-v5-shard1\": {}, \"precompute-v5-shard0\": {}, \"precompute-v4-shard2\": {}, \"precompute-v4-shard1\": {}, \"precompute-v4-shard0\": {}, \"eval-vla-mean-spatial-t10\": {}, \"eval-reconvla-spatial-v3\": {}, \"crm-train-v2-scalar-unc\": {}, \"crm-train-v2-perdof\": {}, \"crm-train-v2-obs-only\": {}, \"precompute-shard2\": {}, \"precompute-shard1\": {}, \"precompute-shard0\": {}, \"precompute-k5\": {}, \"plan_014-reconvla-baseline\": {}, \"plan_001-crm-smolvla\": {}, \"mvp-point-reaching\": {}, \"eval-smolvla-libero-spatial\": {}, \"eval-obs-only-spatial\": {}, \"eval-obs-only-object-default-seed44\": {}, \"eval-mag-perdof-norm005-object\": {}, \"eval-mag-perdof-norm02-seed43-object-r3\": {}, \"eval-mag-perdof-norm03-object-r3\": {}, \"eval-mag-obsonly-norm005\": {}, \"eval-mag-obsonly-norm003-b2\": {}, \"eval-mag-obsonly-norm03-object\": {}, \"eval-mag-obsonly-norm005-object\": {}, \"eval-direct-correction-object-seed42-r2\": {}, \"eval-direct-correction-object-seed42\": {}, \"eval-scalar-object-seed44-r2\": {}, \"eval-perdof-object-seed44\": {}, \"eval-obs-only-object-norm03-seed44\": {}, \"eval-vla-mean-object-seed44\": {}, \"eval-obs-only-object-norm02-seed44-r4\": {}, \"eval-argmin-object-seed44-r2\": {}, \"eval-obs-only-object-norm03-seed45\": {}, \"eval-acr-object-v4-default-r2\": {}, \"eval-mag-perdof-norm003-object\": {}, \"eval-acr-object-obs-only-default\": {}, \"eval-scalar-object-seed43\": {}, \"eval-mag-obsonly-norm003-object\": {}, \"eval-scalar-object-seed44\": {}, \"eval-obs-only-object-norm02-seed44-r3\": {}, \"eval-argmin-object-seed44-r3\": {}, \"eval-vla-mean-object-seed43\": {}, \"eval-perdof-object-seed43\": {}, \"eval-vla-only-object-seed44\": {}, \"eval-obs-only-object-norm02-seed44\": {}, \"eval-argmin-object-seed44\": {}, \"eval-obs-only-object-seed43\": {}, \"eval-mag-obsonly-norm03-b2\": {}, \"eval-argmin-object-seed43\": {}, \"eval-mag-perdof-norm02-seed43-object-r2\": {}, \"eval-mag-obsonly-norm03\": {}, \"eval-mag-obsonly-norm02-object\": {}, \"eval-mag-obsonly-norm03-b4\": {}, \"eval-mag-obsonly-norm03-b3\": {}, \"eval-mag-perdof-norm02-seed43-object\": {}, \"eval-mag-perdof-norm03-object-r2\": {}, \"eval-acr-object-v4-scalar-b2\": {}, \"eval-acr-object-v4-obs-only-b2\": {}, \"eval-spatial-v4-full\": {}, \"eval-reconvla-spatial-v1\": {}, \"eval-object-v6-full\": {}, \"precompute-v3-shard2\": {}, \"precompute-v3-shard1\": {}, \"precompute-v3-shard0\": {}, \"precompute-v2-shard2\": {}, \"precompute-v2-shard1\": {}, \"precompute-v2-shard0\": {}, \"eval-mag-perdof-norm0p3-object-r2\": {}, \"eval-mag-perdof-norm0p3-object\": {}, \"eval-obs-only-object-norm02-seed43\": {}, \"eval-acr-object-v4-default\": {}, \"eval-mag-obsonly-norm03-r2\": {}, \"eval-vla-mean-object\": {}, \"eval-reconvla-object\": {}, \"eval-acr-object-v4-obs-only\": {}, \"eval-acr-object-v4-perdof\": {}, \"eval-acr-spatial-v4-scalar-r2\": {}, \"eval-acr-spatial-v4-obs-only-r3\": {}, \"eval-obs-only-spatial-seed43\": {}, \"eval-acr-spatial-v4-small-r2\": {}, \"eval-mag-obsonly-norm-0.3-r3\": {}, \"eval-mag-obsonly-norm-0p3-r3\": {}, \"eval-argmin-only-spatial-r2\": {}, \"eval-mag-obsonly-norm003\": {}, \"eval-vla-only-object-k1\": {}, \"eval-acr-spatial-v4-default-r3\": {}, \"eval-tiny-correction-spatial\": {}, \"eval-acr-spatial-v4-default-r2\": {}, \"eval-acr-spatial-v4-obs-only\": {}, \"eval-acr-spatial-v4-default\": {}, \"crm-train-v3-norm-scalar-unc\": {}, \"crm-train-v3-norm-obs-only\": {}, \"crm-train-v3-norm\": {}, \"crm-train-v3-scalar-unc\": {}, \"crm-train-v3-obs-only\": {}, \"crm-train-v3-perdof\": {}, \"eval-obs-only-spatial-v3\": {}, \"eval-scalar-unc-spatial-v2\": {}, \"crm-train-a4-scalar-unc\": {}, \"crm-train-a3-obs-only\": {}, \"crm-train-v1\": {}, \"crm-train-k5\": {}, \"eval-scalar-unc-spatial\": {}, \"eval-acr-spatial-v2\": {}, \"eval-k5-spatial\": {}, \"eval-object-v7-full\": {}, \"eval-spatial-v6-full\": {}, \"eval-object-v5-full\": {}, \"eval-acr-vla-spatial-v1\": {}, \"eval-acr-spatial-v1\": {}, \"eval-reconvla-spatial-v2\": {}, \"eval-object-v4-full\": {}, \"eval-spatial-v5-full\": {}, \"eval-spatial-v3-full\": {}, \"eval-spatial-reeval-v2\": {}}, \"count\": 761, \"total\": 761, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.5429}}"
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
This server (bjb2-40593) only has 1 GPU (GPU 0). The task mentions bjb1-18228, not bjb2-40593. Let me re-read the task.

The task says: "在 bjb1-18228 GPU 1 和 GPU 2 上部署 eval 实验。GPU 0 和 3 被 π0.5 precompute 占用，不要碰。"

But the project context says the server is bjb2-40593. The user explicitly mentions bjb1-18228. Let me try connecting to bjb1-18228.


Now I'm looking at the registry and scanning through the completed experiments to identify which Goal/Object variants still need to be run. I can see several eval-supp-goal experiments are already done across different seeds and configurations, but I need to check what's still missing from the full set. I'm noticing the naming conventions are inconsistent across these evaluation runs—some use "obj-k2mean" while others use "k2mean-obj"—so I need to carefully cross-reference what's actually in the DONE list to avoid double-counting or missing entries for the s45 and s46 object evaluations. Continuing through more eval-supp entries with various configurations across different model variants and seed values, including some with alternative naming conventions and repeated runs.

Now I need to check what experiments are currently running or queued, and verify the GPU availability on the target server since the project context shows a different server with limited resources.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "a941ee60-6953-46bb-9661-d947cc50c548",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mk26m76Qm7VXtPHeD7okvv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14512,
      "cache_read_input_tokens": 25807,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14512
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

bjb2-40593 只有 1 个 GPU。任务要求部署在 **bjb1-18228**。让我连接正确的服务器并检查 RUNNING/QUEUED 实验。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "68ced61c-06f4-4487-913d-0f5b0267bd80",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mk26m76Qm7VXtPHeD7okvv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14512,
      "cache_read_input_tokens": 25807,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14512
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01McpuH8KZnzHjRgHCDG4UX9`</summary>

```json
{
  "server": "bjb1-18228",
  "command": "nvidia-smi --query-gpu=index,memory.used,memory.total,utilization.gpu --format=csv,noheader",
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
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "fb4e7e21-22c4-4bf1-9f7c-3cc9a01d61bb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mk26m76Qm7VXtPHeD7okvv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14512,
      "cache_read_input_tokens": 25807,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14512
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

_source line 21 · 2026-05-24T07:10:10.856Z_

<details><summary>↩ Tool result · `toolu_01McpuH8KZnzHjRgHCDG4UX9`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, 9884 MiB, 24564 MiB, 25 %\\n1, 0 MiB, 24564 MiB, 0 %\\n2, 0 MiB, 24564 MiB, 0 %\\n3, 9883 MiB, 24564 MiB, 26 %\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.95}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "7c70655a-b1f7-4fc0-ae57-ba8221422bdf",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"0, 9884 MiB, 24564 MiB, 25 %\\\\n1, 0 MiB, 24564 MiB, 0 %\\\\n2, 0 MiB, 24564 MiB, 0 %\\\\n3, 9883 MiB, 24564 MiB, 26 %\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.95}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"0, 9884 MiB, 24564 MiB, 25 %\\n1, 0 MiB, 24564 MiB, 0 %\\n2, 0 MiB, 24564 MiB, 0 %\\n3, 9883 MiB, 24564 MiB, 26 %\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.95}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01QMZG9D2UKiV9kszrDKGqM8`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": {
    "status": "RUNNING"
  },
  "limit": 0,
  "fields": [
    "exp_id",
    "status"
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
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "a6ce9dae-d426-401f-a749-1a2b2a1e3e08",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mk26m76Qm7VXtPHeD7okvv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14512,
      "cache_read_input_tokens": 25807,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14512
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01ULxjXGGHpmZHvuA1wehFjM`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": {
    "status": "PREPARING"
  },
  "limit": 0,
  "fields": [
    "exp_id",
    "status"
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
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "17b7795e-5e59-4b1c-8e9b-d822609f3ba6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mk26m76Qm7VXtPHeD7okvv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14512,
      "cache_read_input_tokens": 25807,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14512
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01KREXs8yqZN6zrmJ7TAaoZk`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": {
    "status": "QUEUED"
  },
  "limit": 0,
  "fields": [
    "exp_id",
    "status"
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
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "4f1f09bf-31ce-455c-ac45-00cafe94d4dd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mk26m76Qm7VXtPHeD7okvv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14512,
      "cache_read_input_tokens": 25807,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14512
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

_source line 25 · 2026-05-24T07:10:14.133Z_

<details><summary>↩ Tool result · `toolu_01QMZG9D2UKiV9kszrDKGqM8`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-openvla-object-vla-only-seed42-v3\": {\"status\": \"RUNNING\"}, \"eval-supp-long-vla-only-s47\": {\"status\": \"RUNNING\"}, \"eval-supp-long-crm-norm005-s47\": {\"status\": \"RUNNING\"}, \"eval-supp-long-reconvla-s47\": {\"status\": \"RUNNING\"}, \"eval-supp-spatial-crm-norm005-s47\": {\"status\": \"RUNNING\"}, \"eval-supp-vla-only-spatial-s46\": {\"status\": \"RUNNING\"}, \"eval-supp-adapt-tau025-spatial-s45\": {\"status\": \"RUNNING\"}, \"eval-supp-crm-norm005-spatial-s45\": {\"status\": \"RUNNING\"}, \"eval-supp-vla-only-spatial-s45\": {\"status\": \"RUNNING\"}, \"eval-supp-long-adapt-tau025-s47\": {\"status\": \"RUNNING\"}, \"eval-supp-long-k2mean-s46\": {\"status\": \"RUNNING\"}, \"eval-supp-long-reconvla-s46\": {\"status\": \"RUNNING\"}, \"eval-supp-long-crm-norm005-s46\": {\"status\": \"RUNNING\"}, \"eval-supp-long-adapt-tau025-s46\": {\"status\": \"RUNNING\"}, \"precompute-pi05-long-2048-r2\": {\"status\": \"RUNNING\"}, \"precompute-pi05-object-2048-r2\": {\"status\": \"RUNNING\"}}, \"count\": 16, \"total\": 16, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.7292}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "65a592c7-1684-4d36-9127-c9d7c971e51d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"eval-openvla-object-vla-only-seed42-v3\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-supp-long-vla-only-s47\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-supp-long-crm-norm005-s47\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-supp-long-reconvla-s47\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-supp-spatial-crm-norm005-s47\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-supp-vla-only-spatial-s46\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-supp-adapt-tau025-spatial-s45\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-supp-crm-norm005-spatial-s45\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-supp-vla-only-spatial-s45\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-supp-long-adapt-tau025-s47\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-supp-long-k2mean-s46\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-supp-long-reconvla-s46\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-supp-long-crm-norm005-s46\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"eval-supp-long-adapt-tau025-s46\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"precompute-pi05-long-2048-r2\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"precompute-pi05-object-2048-r2\\\": {\\\"status\\\": \\\"RUNNING\\\"}}, \\\"count\\\": 16, \\\"total\\\": 16, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.7292}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval-openvla-object-vla-only-seed42-v3\": {\"status\": \"RUNNING\"}, \"eval-supp-long-vla-only-s47\": {\"status\": \"RUNNING\"}, \"eval-supp-long-crm-norm005-s47\": {\"status\": \"RUNNING\"}, \"eval-supp-long-reconvla-s47\": {\"status\": \"RUNNING\"}, \"eval-supp-spatial-crm-norm005-s47\": {\"status\": \"RUNNING\"}, \"eval-supp-vla-only-spatial-s46\": {\"status\": \"RUNNING\"}, \"eval-supp-adapt-tau025-spatial-s45\": {\"status\": \"RUNNING\"}, \"eval-supp-crm-norm005-spatial-s45\": {\"status\": \"RUNNING\"}, \"eval-supp-vla-only-spatial-s45\": {\"status\": \"RUNNING\"}, \"eval-supp-long-adapt-tau025-s47\": {\"status\": \"RUNNING\"}, \"eval-supp-long-k2mean-s46\": {\"status\": \"RUNNING\"}, \"eval-supp-long-reconvla-s46\": {\"status\": \"RUNNING\"}, \"eval-supp-long-crm-norm005-s46\": {\"status\": \"RUNNING\"}, \"eval-supp-long-adapt-tau025-s46\": {\"status\": \"RUNNING\"}, \"precompute-pi05-long-2048-r2\": {\"status\": \"RUNNING\"}, \"precompute-pi05-object-2048-r2\": {\"status\": \"RUNNING\"}}, \"count\": 16, \"total\": 16, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.7292}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-24T07:10:19.345Z_

<details><summary>↩ Tool result · `toolu_01ULxjXGGHpmZHvuA1wehFjM`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-supp-obj-crm-norm005-s46\": {\"status\": \"PREPARING\"}, \"eval-supp-k2mean-spatial-s45\": {\"status\": \"PREPARING\"}, \"eval-pi05-vla-only-long-seed42-r4-std\": {\"status\": \"PREPARING\"}, \"precompute-smolvla-goal-k10\": {\"status\": \"PREPARING\"}, \"precompute-smolvla-spatial-k10\": {\"status\": \"PREPARING\"}, \"precompute-smolvla-object-k10\": {\"status\": \"PREPARING\"}, \"eval-vla-only-long-seed2\": {\"status\": \"PREPARING\"}, \"eval-vla-only-long-seed1\": {\"status\": \"PREPARING\"}, \"eval-vla-only-long-seed0\": {\"status\": \"PREPARING\"}, \"precompute-pi05-long-bjb1-18228\": {\"status\": \"PREPARING\"}, \"precompute-pi05-goal-bjb2-28827-s2\": {\"status\": \"PREPARING\"}, \"precompute-pi05-goal-bjb2-28827-s1\": {\"status\": \"PREPARING\"}, \"precompute-pi05-goal-bjb2-28827-s0\": {\"status\": \"PREPARING\"}, \"eval-smolvla-crm-long-seed44\": {\"status\": \"PREPARING\"}, \"eval-smolvla-crm-long-seed43\": {\"status\": \"PREPARING\"}, \"crm-pipeline-auto\": {\"status\": \"PREPARING\"}, \"precompute-pi05-obj-s6-r2\": {\"status\": \"PREPARING\"}, \"precompute-pi05-obj-s9-r2\": {\"status\": \"PREPARING\"}, \"precompute-pi05-obj-s8-r2\": {\"status\": \"PREPARING\"}, \"precompute-pi05-obj-s7-r2\": {\"status\": \"PREPARING\"}, \"precompute-pi05-obj-s0-r2\": {\"status\": \"PREPARING\"}, \"precompute-pi05-obj-s5-r2\": {\"status\": \"PREPARING\"}, \"precompute-pi05-obj-s4-r2\": {\"status\": \"PREPARING\"}, \"precompute-pi05-obj-s3-r2\": {\"status\": \"PREPARING\"}, \"precompute-pi05-obj-s2-r2\": {\"status\": \"PREPARING\"}, \"precompute-pi05-obj-s1-r2\": {\"status\": \"PREPARING\"}, \"precompute-pi05-obj-s9-fix\": {\"status\": \"PREPARING\"}, \"precompute-pi05-obj-s8-fix\": {\"status\": \"PREPARING\"}, \"precompute-pi05-obj-s7-fix\": {\"status\": \"PREPARING\"}, \"precompute-pi05-obj-s6-fix\": {\"status\": \"PREPARING\"}, \"precompute-pi05-obj-s5-fix\": {\"status\": \"PREPARING\"}, \"precompute-pi05-obj-shard9\": {\"status\": \"PREPARING\"}, \"precompute-pi05-obj-shard8\": {\"status\": \"PREPARING\"}, \"precompute-pi05-obj-shard7\": {\"status\": \"PREPARING\"}, \"precompute-pi05-obj-shard6\": {\"status\": \"PREPARING\"}, \"precompute-pi05-obj-shard5\": {\"status\": \"PREPARING\"}, \"precompute-pi05-spatial-shard6\": {\"status\": \"PREPARING\"}, \"precompute-pi05-spatial-shard5\": {\"status\": \"PREPARING\"}, \"precompute-pi05-spatial-shard4\": {\"status\": \"PREPARING\"}, \"precompute-pi05-spatial-shard3\": {\"status\": \"PREPARING\"}, \"precompute-pi05-spatial-shard2\": {\"status\": \"PREPARING\"}, \"precompute-pi05-spatial-shard1\": {\"status\": \"PREPARING\"}, \"precompute-pi05-spatial-shard0\": {\"status\": \"PREPARING\"}, \"precompute-pi05-shard0\": {\"status\": \"PREPARING\"}, \"precompute-pi05-shard9\": {\"status\": \"PREPARING\"}, \"precompute-pi05-shard8\": {\"status\": \"PREPARING\"}, \"precompute-pi05-shard7\": {\"status\": \"PREPARING\"}, \"precompute-pi05-shard6\": {\"status\": \"PREPARING\"}, \"precompute-pi05-shard5\": {\"status\": \"PREPARING\"}, \"precompute-pi05-shard4\": {\"status\": \"PREPARING\"}, \"precompute-pi05-shard3\": {\"status\": \"PREPARING\"}, \"precompute-pi05-shard2\": {\"status\": \"PREPARING\"}, \"precompute-pi05-shard1\": {\"status\": \"PREPARING\"}, \"eval-pi05-baseline-object-seed42-r2\": {\"status\": \"PREPARING\"}, \"eval-random-selection-object-seed42-r3\": {\"status\": \"PREPARING\"}, \"eval-vla-only-spatial-seed50\": {\"status\": \"PREPARING\"}, \"eval-crm-spatial-k10-seed50\": {\"status\": \"PREPARING\"}, \"eval-crm-spatial-k10-seed49\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm02-k20-seed44\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm02-k20-seed43\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm02-k20-seed42\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm003-seed76\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm01-seed77\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm01-seed76\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm005-seed77\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm003-seed63-r3\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm005-seed76\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm003-seed62-r3\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm003-seed78\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm003-seed77\": {\"status\": \"PREPARING\"}, \"eval-obs-only-goal-norm02-seed53\": {\"status\": \"PREPARING\"}, \"eval-vla-only-long-seed54\": {\"status\": \"PREPARING\"}, \"eval-crm-long-seed54\": {\"status\": \"PREPARING\"}, \"eval-vla-only-spatial-seed54\": {\"status\": \"PREPARING\"}, \"eval-crm-long-seed53\": {\"status\": \"PREPARING\"}, \"eval-vla-only-spatial-seed53\": {\"status\": \"PREPARING\"}, \"eval-vla-only-spatial-seed52\": {\"status\": \"PREPARING\"}, \"eval-crm-goal-seed50\": {\"status\": \"PREPARING\"}, \"eval-crm-goal-seed49\": {\"status\": \"PREPARING\"}, \"eval-crm-long-seed52\": {\"status\": \"PREPARING\"}, \"eval-vla-only-goal-seed52\": {\"status\": \"PREPARING\"}, \"eval-vla-only-long-seed53\": {\"status\": \"PREPARING\"}, \"eval-crm-long-seed51\": {\"status\": \"PREPARING\"}, \"eval-vla-only-goal-seed50\": {\"status\": \"PREPARING\"}, \"eval-crm-long-seed49\": {\"status\": \"PREPARING\"}, \"eval-crm-long-seed48\": {\"status\": \"PREPARING\"}, \"eval-crm-goal-seed48\": {\"status\": \"PREPARING\"}, \"eval-crm-goal-seed47\": {\"status\": \"PREPARING\"}, \"eval-crm-spatial-seed48\": {\"status\": \"PREPARING\"}, \"eval-vla-only-spatial-seed51\": {\"status\": \"PREPARING\"}, \"eval-vla-only-object-seed51\": {\"status\": \"PREPARING\"}, \"eval-vla-only-long-seed49\": {\"status\": \"PREPARING\"}, \"eval-adaptive-k-p25-seed44\": {\"status\": \"PREPARING\"}, \"eval-crm-spatial-seed47\": {\"status\": \"PREPARING\"}, \"eval-vla-only-object-seed49-r2\": {\"status\": \"PREPARING\"}, \"eval-vla-only-spatial-seed49-r2\": {\"status\": \"PREPARING\"}}, \"count\": 96, \"total\": 96, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.1813}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "d327a369-5278-4dea-8c17-8ac311c3674d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"eval-supp-obj-crm-norm005-s46\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-supp-k2mean-spatial-s45\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-pi05-vla-only-long-seed42-r4-std\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"precompute-smolvla-goal-k10\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"precompute-smolvla-spatial-k10\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"precompute-smolvla-object-k10\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-vla-only-long-seed2\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-vla-only-long-seed1\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-vla-only-long-seed0\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"precompute-pi05-long-bjb1-18228\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"precompute-pi05-goal-bjb2-28827-s2\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"precompute-pi05-goal-bjb2-28827-s1\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"precompute-pi05-goal-bjb2-28827-s0\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-smolvla-crm-long-seed44\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-smolvla-crm-long-seed43\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"crm-pipeline-auto\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"precompute-pi05-obj-s6-r2\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"precompute-pi05-obj-s9-r2\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"precompute-pi05-obj-s8-r2\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"precompute-pi05-obj-s7-r2\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"precompute-pi05-obj-s0-r2\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"precompute-pi05-obj-s5-r2\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"precompute-pi05-obj-s4-r2\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"precompute-pi05-obj-s3-r2\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"precompute-pi05-obj-s2-r2\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"precompute-pi05-obj-s1-r2\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"precompute-pi05-obj-s9-fix\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"precompute-pi05-obj-s8-fix\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"precompute-pi05-obj-s7-fix\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"precompute-pi05-obj-s6-fix\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"precompute-pi05-obj-s5-fix\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"precompute-pi05-obj-shard9\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"precompute-pi05-obj-shard8\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"precompute-pi05-obj-shard7\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"precompute-pi05-obj-shard6\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"precompute-pi05-obj-shard5\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"precompute-pi05-spatial-shard6\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"precompute-pi05-spatial-shard5\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"precompute-pi05-spatial-shard4\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"precompute-pi05-spatial-shard3\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"precompute-pi05-spatial-shard2\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"precompute-pi05-spatial-shard1\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"precompute-pi05-spatial-shard0\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"precompute-pi05-shard0\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"precompute-pi05-shard9\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"precompute-pi05-shard8\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"precompute-pi05-shard7\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"precompute-pi05-shard6\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"precompute-pi05-shard5\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"precompute-pi05-shard4\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"precompute-pi05-shard3\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"precompute-pi05-shard2\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"precompute-pi05-shard1\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-pi05-baseline-object-seed42-r2\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-random-selection-object-seed42-r3\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-vla-only-spatial-seed50\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-crm-spatial-k10-seed50\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-crm-spatial-k10-seed49\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-obs-only-object-norm02-k20-seed44\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-obs-only-object-norm02-k20-seed43\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-obs-only-object-norm02-k20-seed42\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-obs-only-object-norm003-seed76\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-obs-only-object-norm01-seed77\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-obs-only-object-norm01-seed76\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-obs-only-object-norm005-seed77\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-obs-only-object-norm003-seed63-r3\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-obs-only-object-norm005-seed76\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-obs-only-object-norm003-seed62-r3\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-obs-only-object-norm003-seed78\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-obs-only-object-norm003-seed77\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-obs-only-goal-norm02-seed53\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-vla-only-long-seed54\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-crm-long-seed54\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-vla-only-spatial-seed54\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-crm-long-seed53\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-vla-only-spatial-seed53\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-vla-only-spatial-seed52\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-crm-goal-seed50\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-crm-goal-seed49\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-crm-long-seed52\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-vla-only-goal-seed52\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-vla-only-long-seed53\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-crm-long-seed51\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-vla-only-goal-seed50\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-crm-long-seed49\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-crm-long-seed48\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-crm-goal-seed48\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-crm-goal-seed47\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-crm-spatial-seed48\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-vla-only-spatial-seed51\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-vla-only-object-seed51\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-vla-only-long-seed49\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-adaptive-k-p25-seed44\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-crm-spatial-seed47\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-vla-only-object-seed49-r2\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-vla-only-spatial-seed49-r2\\\": {\\\"status\\\": \\\"PREPARING\\\"}}, \\\"count\\\": 96, \\\"total\\\": 96, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 5.1813}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval-supp-obj-crm-norm005-s46\": {\"status\": \"PREPARING\"}, \"eval-supp-k2mean-spatial-s45\": {\"status\": \"PREPARING\"}, \"eval-pi05-vla-only-long-seed42-r4-std\": {\"status\": \"PREPARING\"}, \"precompute-smolvla-goal-k10\": {\"status\": \"PREPARING\"}, \"precompute-smolvla-spatial-k10\": {\"status\": \"PREPARING\"}, \"precompute-smolvla-object-k10\": {\"status\": \"PREPARING\"}, \"eval-vla-only-long-seed2\": {\"status\": \"PREPARING\"}, \"eval-vla-only-long-seed1\": {\"status\": \"PREPARING\"}, \"eval-vla-only-long-seed0\": {\"status\": \"PREPARING\"}, \"precompute-pi05-long-bjb1-18228\": {\"status\": \"PREPARING\"}, \"precompute-pi05-goal-bjb2-28827-s2\": {\"status\": \"PREPARING\"}, \"precompute-pi05-goal-bjb2-28827-s1\": {\"status\": \"PREPARING\"}, \"precompute-pi05-goal-bjb2-28827-s0\": {\"status\": \"PREPARING\"}, \"eval-smolvla-crm-long-seed44\": {\"status\": \"PREPARING\"}, \"eval-smolvla-crm-long-seed43\": {\"status\": \"PREPARING\"}, \"crm-pipeline-auto\": {\"status\": \"PREPARING\"}, \"precompute-pi05-obj-s6-r2\": {\"status\": \"PREPARING\"}, \"precompute-pi05-obj-s9-r2\": {\"status\": \"PREPARING\"}, \"precompute-pi05-obj-s8-r2\": {\"status\": \"PREPARING\"}, \"precompute-pi05-obj-s7-r2\": {\"status\": \"PREPARING\"}, \"precompute-pi05-obj-s0-r2\": {\"status\": \"PREPARING\"}, \"precompute-pi05-obj-s5-r2\": {\"status\": \"PREPARING\"}, \"precompute-pi05-obj-s4-r2\": {\"status\": \"PREPARING\"}, \"precompute-pi05-obj-s3-r2\": {\"status\": \"PREPARING\"}, \"precompute-pi05-obj-s2-r2\": {\"status\": \"PREPARING\"}, \"precompute-pi05-obj-s1-r2\": {\"status\": \"PREPARING\"}, \"precompute-pi05-obj-s9-fix\": {\"status\": \"PREPARING\"}, \"precompute-pi05-obj-s8-fix\": {\"status\": \"PREPARING\"}, \"precompute-pi05-obj-s7-fix\": {\"status\": \"PREPARING\"}, \"precompute-pi05-obj-s6-fix\": {\"status\": \"PREPARING\"}, \"precompute-pi05-obj-s5-fix\": {\"status\": \"PREPARING\"}, \"precompute-pi05-obj-shard9\": {\"status\": \"PREPARING\"}, \"precompute-pi05-obj-shard8\": {\"status\": \"PREPARING\"}, \"precompute-pi05-obj-shard7\": {\"status\": \"PREPARING\"}, \"precompute-pi05-obj-shard6\": {\"status\": \"PREPARING\"}, \"precompute-pi05-obj-shard5\": {\"status\": \"PREPARING\"}, \"precompute-pi05-spatial-shard6\": {\"status\": \"PREPARING\"}, \"precompute-pi05-spatial-shard5\": {\"status\": \"PREPARING\"}, \"precompute-pi05-spatial-shard4\": {\"status\": \"PREPARING\"}, \"precompute-pi05-spatial-shard3\": {\"status\": \"PREPARING\"}, \"precompute-pi05-spatial-shard2\": {\"status\": \"PREPARING\"}, \"precompute-pi05-spatial-shard1\": {\"status\": \"PREPARING\"}, \"precompute-pi05-spatial-shard0\": {\"status\": \"PREPARING\"}, \"precompute-pi05-shard0\": {\"status\": \"PREPARING\"}, \"precompute-pi05-shard9\": {\"status\": \"PREPARING\"}, \"precompute-pi05-shard8\": {\"status\": \"PREPARING\"}, \"precompute-pi05-shard7\": {\"status\": \"PREPARING\"}, \"precompute-pi05-shard6\": {\"status\": \"PREPARING\"}, \"precompute-pi05-shard5\": {\"status\": \"PREPARING\"}, \"precompute-pi05-shard4\": {\"status\": \"PREPARING\"}, \"precompute-pi05-shard3\": {\"status\": \"PREPARING\"}, \"precompute-pi05-shard2\": {\"status\": \"PREPARING\"}, \"precompute-pi05-shard1\": {\"status\": \"PREPARING\"}, \"eval-pi05-baseline-object-seed42-r2\": {\"status\": \"PREPARING\"}, \"eval-random-selection-object-seed42-r3\": {\"status\": \"PREPARING\"}, \"eval-vla-only-spatial-seed50\": {\"status\": \"PREPARING\"}, \"eval-crm-spatial-k10-seed50\": {\"status\": \"PREPARING\"}, \"eval-crm-spatial-k10-seed49\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm02-k20-seed44\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm02-k20-seed43\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm02-k20-seed42\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm003-seed76\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm01-seed77\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm01-seed76\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm005-seed77\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm003-seed63-r3\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm005-seed76\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm003-seed62-r3\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm003-seed78\": {\"status\": \"PREPARING\"}, \"eval-obs-only-object-norm003-seed77\": {\"status\": \"PREPARING\"}, \"eval-obs-only-goal-norm02-seed53\": {\"status\": \"PREPARING\"}, \"eval-vla-only-long-seed54\": {\"status\": \"PREPARING\"}, \"eval-crm-long-seed54\": {\"status\": \"PREPARING\"}, \"eval-vla-only-spatial-seed54\": {\"status\": \"PREPARING\"}, \"eval-crm-long-seed53\": {\"status\": \"PREPARING\"}, \"eval-vla-only-spatial-seed53\": {\"status\": \"PREPARING\"}, \"eval-vla-only-spatial-seed52\": {\"status\": \"PREPARING\"}, \"eval-crm-goal-seed50\": {\"status\": \"PREPARING\"}, \"eval-crm-goal-seed49\": {\"status\": \"PREPARING\"}, \"eval-crm-long-seed52\": {\"status\": \"PREPARING\"}, \"eval-vla-only-goal-seed52\": {\"status\": \"PREPARING\"}, \"eval-vla-only-long-seed53\": {\"status\": \"PREPARING\"}, \"eval-crm-long-seed51\": {\"status\": \"PREPARING\"}, \"eval-vla-only-goal-seed50\": {\"status\": \"PREPARING\"}, \"eval-crm-long-seed49\": {\"status\": \"PREPARING\"}, \"eval-crm-long-seed48\": {\"status\": \"PREPARING\"}, \"eval-crm-goal-seed48\": {\"status\": \"PREPARING\"}, \"eval-crm-goal-seed47\": {\"status\": \"PREPARING\"}, \"eval-crm-spatial-seed48\": {\"status\": \"PREPARING\"}, \"eval-vla-only-spatial-seed51\": {\"status\": \"PREPARING\"}, \"eval-vla-only-object-seed51\": {\"status\": \"PREPARING\"}, \"eval-vla-only-long-seed49\": {\"status\": \"PREPARING\"}, \"eval-adaptive-k-p25-seed44\": {\"status\": \"PREPARING\"}, \"eval-crm-spatial-seed47\": {\"status\": \"PREPARING\"}, \"eval-vla-only-object-seed49-r2\": {\"status\": \"PREPARING\"}, \"eval-vla-only-spatial-seed49-r2\": {\"status\": \"PREPARING\"}}, \"count\": 96, \"total\": 96, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.1813}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-24T07:10:21.314Z_

<details><summary>↩ Tool result · `toolu_01KREXs8yqZN6zrmJ7TAaoZk`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-smolvla-lerobot-goal-seed44\": {\"status\": \"QUEUED\"}}, \"count\": 1, \"total\": 1, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.9529}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "9a191241-e79a-4360-ad99-5172da66db47",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"eval-smolvla-lerobot-goal-seed44\\\": {\\\"status\\\": \\\"QUEUED\\\"}}, \\\"count\\\": 1, \\\"total\\\": 1, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.9529}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval-smolvla-lerobot-goal-seed44\": {\"status\": \"QUEUED\"}}, \"count\": 1, \"total\": 1, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.9529}}"
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
bjb1-18228 has 4 GPUs:
- GPU 0: 9884 MiB used (precompute, don't touch)
- GPU 1: 0 MiB used (free!)
- GPU 2: 0 MiB used (free!)
- GPU 3: 9883 MiB used (precompute, don't touch)

GPU 1 and 2 are free.

Now let me analyze which Goal/Object experiments are missing.

From the DONE list, for Goal seeds s42-s46, let me check what methods exist:


Looking at the vla-only experiments, all five seeds from s42 through s46 are complete. For the adapt method with tau025, I'm checking which seeds have finished runs. I've verified that all five methods—adapt, crm, k2mean, and reconvla—have completed their Goal evaluations across steps 42 through 46. Now I'm moving on to check the Object evaluations. Continuing through the remaining configurations for adapt and crm methods across steps 42-46...

For crm, I notice eval-supp-obj-crm-norm005-s46 is still in PREPARING status, so that one hasn't completed yet. Now moving through the k2mean configurations for the same step range. I'm noticing some naming inconsistencies in the experiment tracking—eval-supp-obj-crm-norm005-s46 is marked as PREPARING, but there are already completed versions with slightly different naming conventions. Rather than worry about potential duplicates, I should focus on what's actually missing. Looking at the running experiments, I see s47 variants are already in progress, so it seems the scope might need to extend beyond s46. Looking at the PREPARING list, I should focus on experiments that can run on the available GPUs. The user mentioned that Spatial experiments are already complete across all methods, so I can skip those. For the remaining candidates, I need to check which ones aren't duplicates of already-completed work and prioritize based on what's actually needed next. I'm noticing there's a mismatch in the experiment versions—some are running on s46 while their r2 variants are already done, which suggests they might be on different servers. Since the Goal and Object precomputes are complete and Spatial is finished, I should focus on what's still in PREPARING status and could use those free GPUs on bjb1-18228. The s47 long experiments are currently running, along with some spatial variants. I'm checking whether k2mean-s47 for Long exists—I don't see eval-supp-long-k2mean-s47 in either the DONE or RUNNING lists, so it might be missing. But actually, the user's focus is on Goal and Object seed extensions since Spatial is already complete. Looking at the Goal experiments across all five methods for seeds s42 through s46, those are all finished.

Now checking the Object experiments for the same methods and seeds—they appear to be complete as well, though there's some duplication with eval-supp-obj-crm-norm005-s46 in PREPARING while similar variants are already DONE. Since Goal and Object are both done, I should look through the PREPARING queue for other eval experiments that could run on the available GPUs, filtering out spatial and precompute tasks. Looking at the eval-vla-only and eval-crm experiments with higher seed numbers, the most promising candidates are the ones with s46 and s47 variants. I need to verify whether Goal and Object s47 experiments exist in any status, since the user specifically asked about s45/s46 variants but I should check if s47 is also needed. Let me review the evaluate.py command format to understand what experiments would actually make sense to run.

Now checking the DONE list to see which Goal and Object variants have already completed across the different configurations like vla-only, adapt, crm, k2mean, and reconvla for both s45 and s46 seeds. All the reconstruction experiments are done too. Now I need to check what's in the PREPARING queue—specifically looking for eval experiments that can run on the available GPUs, since the Goal and Object seed extensions are complete. I'm scanning through to see which long-running experiments are actually queued versus already running, since there seem to be some discrepancies in what I'm tracking. I'm checking which PREPARING or QUEUED experiments could actually run right now. The eval-supp-long-k2mean-s47 experiment doesn't seem to exist anywhere in the system, so that's not an option. Looking at what's available, there's eval-smolvla-lerobot-goal-seed44 in the queue that might be deployable, but I need to verify it can run on the available GPUs.

Wait, I should re-read what the user actually wants—they're asking me to deploy missing experiments, specifically Goal seed extensions first, then Object seed extensions if Goal is done. Since s42-s46 are already covered, maybe I should check if extending to s47 makes sense, and I'll need to look at evaluate.py to understand what seeds and benchmarks are actually supported.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "40c26bed-952f-40f4-9ce2-a3a351bd7de8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PWyjeErjubFvdho8h1rwLi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5368,
      "cache_read_input_tokens": 40319,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5368
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

bjb1-18228 确认: GPU 0/3 被占用，GPU 1/2 空闲。Goal/Object s42-s46 全部 DONE。

让我检查 evaluate.py 和确认是否需要 s47 扩展。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "b6c37f91-f4a0-4bc5-ae1c-ef95917a27a5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PWyjeErjubFvdho8h1rwLi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5368,
      "cache_read_input_tokens": 40319,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5368
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_014vNweWNRK5Gqyyezzcs8wS`</summary>

```json
{
  "server": "bjb1-18228",
  "command": "head -80 /root/acr-vla-conformal-refinement/src/evaluate.py",
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
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "f186aa7e-939e-4815-91ea-af80fcaf8e4f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PWyjeErjubFvdho8h1rwLi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5368,
      "cache_read_input_tokens": 40319,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5368
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

_source line 31 · 2026-05-24T07:11:49.236Z_

<details><summary>↩ Tool result · `toolu_014vNweWNRK5Gqyyezzcs8wS`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nLIBERO evaluation script for ACR-VLA.\\n\\nRollout loop:\\n  1. Load LIBERO env + task suite\\n  2. Load SmolVLA (frozen) + CRM\\n  3. For each task, rollout N times:\\n     a. Reset env\\n     b. Each step: obs → SmolVLA K=10 samples → CGS on 6D pose → CRM\\n        → combine refined pose with gripper → execute 7D action\\n     c. Record success/failure\\n  4. Report per-task and overall success rate\\n\\nBaselines:\\n  - \\\"vla_only\\\": SmolVLA mean of K=10, no CRM refinement\\n  - \\\"crm_scalar\\\": CRM with scalar uncertainty (single std, not per-DOF)\\n  - \\\"crm_perdof\\\": CRM with full per-DOF uncertainty (ours)\\n  - \\\"acr_vla\\\": alias for crm_perdof — the full ACR-VLA pipeline\\n  - \\\"reconvla\\\": ReconVLA baseline — scalar Euclidean argmin selection (plan_014)\\n  - \\\"adaptive_k\\\": Adaptive K — K=2 L2 probe, expand to K=10 + CRM obs_only if uncertain\\n\\nAdaptive K mode (--mode adaptive_k):\\n  Each step: generate K=2 samples, compute pairwise L2 distance.\\n  If L2 > threshold (high uncertainty): generate 8 more (total K=10),\\n    select argmin(L2 to mean), apply CRM obs_only correction (epsilon=0.2).\\n  If L2 <= threshold (low uncertainty): use mean of K=2, skip CRM.\\n\\nUsage:\\n  python evaluate.py --benchmark object --checkpoint /path/to/crm_best.pt --n_rollouts 20\\n  python evaluate.py --benchmark object --mode vla_only --n_rollouts 20\\n  python evaluate.py --benchmark spatial --mode reconvla --n_rollouts 20\\n  python evaluate.py --benchmark spatial --mode acr_vla --crm_checkpoint /path/to/crm_best.pt --n_rollouts 10\\n\\\"\\\"\\\"\\nimport argparse\\nimport functools\\nbuiltins_print = print\\nprint = functools.partial(builtins_print, flush=True)\\nimport os\\nos.environ.setdefault(\\\"HF_HUB_OFFLINE\\\", \\\"1\\\")\\nos.environ.setdefault(\\\"TRANSFORMERS_OFFLINE\\\", \\\"1\\\")\\nimport sys\\nimport json\\nimport time\\nimport signal\\nimport traceback\\nfrom pathlib import Path\\n\\nimport torch\\nimport torch.nn.functional as F\\nimport numpy as np\\nfrom robosuite.utils.transform_utils import quat2axisangle\\n\\nsys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\\nfrom cgs import ConformilizedGaussianScoring\\nfrom crm import ConformalRefinementModule\\nfrom aci import AdaptiveConformalInference\\nfrom utils import set_seed, CORRECTION_DIM, FULL_ACTION_DIM, H_EFF, OBS_DIM\\nfrom reconvla_baseline import reconvla_select\\n\\n# Official LIBERO max steps per suite (lerobot convention)\\nSUITE_MAX_STEPS = {\\\"object\\\": 280, \\\"spatial\\\": 280, \\\"goal\\\": 300, \\\"long\\\": 520, \\\"90\\\": 400}\\n\\n\\ndef parse_args():\\n    p = argparse.ArgumentParser(description=\\\"Evaluate ACR-VLA on LIBERO\\\")\\n    p.add_argument(\\\"--benchmark\\\", type=str, default=\\\"object\\\",\\n                   choices=[\\\"object\\\", \\\"spatial\\\", \\\"goal\\\", \\\"long\\\", \\\"90\\\"])\\n    p.add_argument(\\\"--checkpoint\\\", type=str, default=None,\\n                   help=\\\"Path to CRM checkpoint (crm_best.pt)\\\")\\n    p.add_argument(\\\"--crm_checkpoint\\\", type=str, default=None,\\n                   help=\\\"Alias for --checkpoint (used with --mode acr_vla)\\\")\\n    p.add_argument(\\\"--n_rollouts\\\", type=int, default=20)\\n    p.add_argument(\\\"--max_steps\\\", type=int, default=300,\\n                   help=\\\"Max steps per rollout\\\")\\n    p.add_argument(\\\"--seed\\\", type=int, default=42)\\n    p.add_argument(\\\"--K\\\", type=int, default=10)\\n    p.add_argument(\\\"--mode\\\", type=str, default=\\\"crm_perdof\\\",\\n                   choices=[\\\"vla_only\\\", \\\"crm_scalar\\\", \\\"crm_perdof\\\", \\\"acr_vla\\\", \\\"crm_obs_only\\\", \\\"reconvla\\\", \\\"random_selection\\\", \\\"adaptive_k\\\", \\\"adaptive_unc_head\\\", \\\"adaptive_conformal_crm\\\"])\\n    p.add_argument(\\\"--baseline_mode\\\", type=str, default=\\\"single\\\",\\n                   choices=[\\\"single\\\", \\\"mean\\\"],\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "02ac6070-ee7e-4a82-bb9b-16ddfdf74761",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\"\\\\\\\"\\\\\\\"\\\\nLIBERO evaluation script for ACR-VLA.\\\\n\\\\nRollout loop:\\\\n  1. Load LIBERO env + task suite\\\\n  2. Load SmolVLA (frozen) + CRM\\\\n  3. For each task, rollout N times:\\\\n     a. Reset env\\\\n     b. Each step: obs → SmolVLA K=10 samples → CGS on 6D pose → CRM\\\\n        → combine refined pose with gripper → execute 7D action\\\\n     c. Record success/failure\\\\n  4. Report per-task and overall success rate\\\\n\\\\nBaselines:\\\\n  - \\\\\\\"vla_only\\\\\\\": SmolVLA mean of K=10, no CRM refinement\\\\n  - \\\\\\\"crm_scalar\\\\\\\": CRM with scalar uncertainty (single std, not per-DOF)\\\\n  - \\\\\\\"crm_perdof\\\\\\\": CRM with full per-DOF uncertainty (ours)\\\\n  - \\\\\\\"acr_vla\\\\\\\": alias for crm_perdof — the full ACR-VLA pipeline\\\\n  - \\\\\\\"reconvla\\\\\\\": ReconVLA baseline — scalar Euclidean argmin selection (plan_014)\\\\n  - \\\\\\\"adaptive_k\\\\\\\": Adaptive K — K=2 L2 probe, expand to K=10 + CRM obs_only if uncertain\\\\n\\\\nAdaptive K mode (--mode adaptive_k):\\\\n  Each step: generate K=2 samples, compute pairwise L2 distance.\\\\n  If L2 > threshold (high uncertainty): generate 8 more (total K=10),\\\\n    select argmin(L2 to mean), apply CRM obs_only correction (epsilon=0.2).\\\\n  If L2 <= threshold (low uncertainty): use mean of K=2, skip CRM.\\\\n\\\\nUsage:\\\\n  python evaluate.py --benchmark object --checkpoint /path/to/crm_best.pt --n_rollouts 20\\\\n  python evaluate.py --benchmark object --mode vla_only --n_rollouts 20\\\\n  python evaluate.py --benchmark spatial --mode reconvla --n_rollouts 20\\\\n  python evaluate.py --benchmark spatial --mode acr_vla --crm_checkpoint /path/to/crm_best.pt --n_rollouts 10\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\nimport argparse\\\\nimport functools\\\\nbuiltins_print = print\\\\nprint = functools.partial(builtins_print, flush=True)\\\\nimport os\\\\nos.environ.setdefault(\\\\\\\"HF_HUB_OFFLINE\\\\\\\", \\\\\\\"1\\\\\\\")\\\\nos.environ.setdefault(\\\\\\\"TRANSFORMERS_OFFLINE\\\\\\\", \\\\\\\"1\\\\\\\")\\\\nimport sys\\\\nimport json\\\\nimport time\\\\nimport signal\\\\nimport traceback\\\\nfrom pathlib import Path\\\\n\\\\nimport torch\\\\nimport torch.nn.functional as F\\\\nimport numpy as np\\\\nfrom robosuite.utils.transform_utils import quat2axisangle\\\\n\\\\nsys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\\\\nfrom cgs import ConformilizedGaussianScoring\\\\nfrom crm import ConformalRefinementModule\\\\nfrom aci import AdaptiveConformalInference\\\\nfrom utils import set_seed, CORRECTION_DIM, FULL_ACTION_DIM, H_EFF, OBS_DIM\\\\nfrom reconvla_baseline import reconvla_select\\\\n\\\\n# Official LIBERO max steps per suite (lerobot convention)\\\\nSUITE_MAX_STEPS = {\\\\\\\"object\\\\\\\": 280, \\\\\\\"spatial\\\\\\\": 280, \\\\\\\"goal\\\\\\\": 300, \\\\\\\"long\\\\\\\": 520, \\\\\\\"90\\\\\\\": 400}\\\\n\\\\n\\\\ndef parse_args():\\\\n    p = argparse.ArgumentParser(description=\\\\\\\"Evaluate ACR-VLA on LIBERO\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--benchmark\\\\\\\", type=str, default=\\\\\\\"object\\\\\\\",\\\\n                   choices=[\\\\\\\"object\\\\\\\", \\\\\\\"spatial\\\\\\\", \\\\\\\"goal\\\\\\\", \\\\\\\"long\\\\\\\", \\\\\\\"90\\\\\\\"])\\\\n    p.add_argument(\\\\\\\"--checkpoint\\\\\\\", type=str, default=None,\\\\n                   help=\\\\\\\"Path to CRM checkpoint (crm_best.pt)\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--crm_checkpoint\\\\\\\", type=str, default=None,\\\\n                   help=\\\\\\\"Alias for --checkpoint (used with --mode acr_vla)\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--n_rollouts\\\\\\\", type=int, default=20)\\\\n    p.add_argument(\\\\\\\"--max_steps\\\\\\\", type=int, default=300,\\\\n                   help=\\\\\\\"Max steps per rollout\\\\\\\")\\\\n    p.add_argument(\\\\\\\"--seed\\\\\\\", type=int, default=42)\\\\n    p.add_argument(\\\\\\\"--K\\\\\\\", type=int, default=10)\\\\n    p.add_argument(\\\\\\\"--mode\\\\\\\", type=str, default=\\\\\\\"crm_perdof\\\\\\\",\\\\n                   choices=[\\\\\\\"vla_only\\\\\\\", \\\\\\\"crm_scalar\\\\\\\", \\\\\\\"crm_perdof\\\\\\\", \\\\\\\"acr_vla\\\\\\\", \\\\\\\"crm_obs_only\\\\\\\", \\\\\\\"reconvla\\\\\\\", \\\\\\\"random_selection\\\\\\\", \\\\\\\"adaptive_k\\\\\\\", \\\\\\\"adaptive_unc_head\\\\\\\", \\\\\\\"adaptive_conformal_crm\\\\\\\"])\\\\n    p.add_argument(\\\\\\\"--baseline_mode\\\\\\\", type=str, default=\\\\\\\"single\\\\\\\",\\\\n                   choices=[\\\\\\\"single\\\\\\\", \\\\\\\"mean\\\\\\\"],\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nLIBERO evaluation script for ACR-VLA.\\n\\nRollout loop:\\n  1. Load LIBERO env + task suite\\n  2. Load SmolVLA (frozen) + CRM\\n  3. For each task, rollout N times:\\n     a. Reset env\\n     b. Each step: obs → SmolVLA K=10 samples → CGS on 6D pose → CRM\\n        → combine refined pose with gripper → execute 7D action\\n     c. Record success/failure\\n  4. Report per-task and overall success rate\\n\\nBaselines:\\n  - \\\"vla_only\\\": SmolVLA mean of K=10, no CRM refinement\\n  - \\\"crm_scalar\\\": CRM with scalar uncertainty (single std, not per-DOF)\\n  - \\\"crm_perdof\\\": CRM with full per-DOF uncertainty (ours)\\n  - \\\"acr_vla\\\": alias for crm_perdof — the full ACR-VLA pipeline\\n  - \\\"reconvla\\\": ReconVLA baseline — scalar Euclidean argmin selection (plan_014)\\n  - \\\"adaptive_k\\\": Adaptive K — K=2 L2 probe, expand to K=10 + CRM obs_only if uncertain\\n\\nAdaptive K mode (--mode adaptive_k):\\n  Each step: generate K=2 samples, compute pairwise L2 distance.\\n  If L2 > threshold (high uncertainty): generate 8 more (total K=10),\\n    select argmin(L2 to mean), apply CRM obs_only correction (epsilon=0.2).\\n  If L2 <= threshold (low uncertainty): use mean of K=2, skip CRM.\\n\\nUsage:\\n  python evaluate.py --benchmark object --checkpoint /path/to/crm_best.pt --n_rollouts 20\\n  python evaluate.py --benchmark object --mode vla_only --n_rollouts 20\\n  python evaluate.py --benchmark spatial --mode reconvla --n_rollouts 20\\n  python evaluate.py --benchmark spatial --mode acr_vla --crm_checkpoint /path/to/crm_best.pt --n_rollouts 10\\n\\\"\\\"\\\"\\nimport argparse\\nimport functools\\nbuiltins_print = print\\nprint = functools.partial(builtins_print, flush=True)\\nimport os\\nos.environ.setdefault(\\\"HF_HUB_OFFLINE\\\", \\\"1\\\")\\nos.environ.setdefault(\\\"TRANSFORMERS_OFFLINE\\\", \\\"1\\\")\\nimport sys\\nimport json\\nimport time\\nimport signal\\nimport traceback\\nfrom pathlib import Path\\n\\nimport torch\\nimport torch.nn.functional as F\\nimport numpy as np\\nfrom robosuite.utils.transform_utils import quat2axisangle\\n\\nsys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\\nfrom cgs import ConformilizedGaussianScoring\\nfrom crm import ConformalRefinementModule\\nfrom aci import AdaptiveConformalInference\\nfrom utils import set_seed, CORRECTION_DIM, FULL_ACTION_DIM, H_EFF, OBS_DIM\\nfrom reconvla_baseline import reconvla_select\\n\\n# Official LIBERO max steps per suite (lerobot convention)\\nSUITE_MAX_STEPS = {\\\"object\\\": 280, \\\"spatial\\\": 280, \\\"goal\\\": 300, \\\"long\\\": 520, \\\"90\\\": 400}\\n\\n\\ndef parse_args():\\n    p = argparse.ArgumentParser(description=\\\"Evaluate ACR-VLA on LIBERO\\\")\\n    p.add_argument(\\\"--benchmark\\\", type=str, default=\\\"object\\\",\\n                   choices=[\\\"object\\\", \\\"spatial\\\", \\\"goal\\\", \\\"long\\\", \\\"90\\\"])\\n    p.add_argument(\\\"--checkpoint\\\", type=str, default=None,\\n                   help=\\\"Path to CRM checkpoint (crm_best.pt)\\\")\\n    p.add_argument(\\\"--crm_checkpoint\\\", type=str, default=None,\\n                   help=\\\"Alias for --checkpoint (used with --mode acr_vla)\\\")\\n    p.add_argument(\\\"--n_rollouts\\\", type=int, default=20)\\n    p.add_argument(\\\"--max_steps\\\", type=int, default=300,\\n                   help=\\\"Max steps per rollout\\\")\\n    p.add_argument(\\\"--seed\\\", type=int, default=42)\\n    p.add_argument(\\\"--K\\\", type=int, default=10)\\n    p.add_argument(\\\"--mode\\\", type=str, default=\\\"crm_perdof\\\",\\n                   choices=[\\\"vla_only\\\", \\\"crm_scalar\\\", \\\"crm_perdof\\\", \\\"acr_vla\\\", \\\"crm_obs_only\\\", \\\"reconvla\\\", \\\"random_selection\\\", \\\"adaptive_k\\\", \\\"adaptive_unc_head\\\", \\\"adaptive_conformal_crm\\\"])\\n    p.add_argument(\\\"--baseline_mode\\\", type=str, default=\\\"single\\\",\\n                   choices=[\\\"single\\\", \\\"mean\\\"],\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Q4E3AZxG1onQFCsVj1VZP3`</summary>

```json
{
  "server": "bjb1-18228",
  "command": "ls /root/autodl-tmp/checkpoints/",
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
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "8a4329ab-7294-41d6-9d94-b3808ec2e216",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PWyjeErjubFvdho8h1rwLi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5368,
      "cache_read_input_tokens": 40319,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5368
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

_source line 33 · 2026-05-24T07:11:49.853Z_

<details><summary>↩ Tool result · `toolu_01Q4E3AZxG1onQFCsVj1VZP3`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"crm\\ncrm_k1\\ncrm_loss_variants\\ncrm_lto_splitA\\ncrm_lto_splitA_fixed\\ncrm_pi05\\ncrm_pi05_full\\ncrm_unified_4suite\\ncrm_v2\\ncrm_v3_norm\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "01c3c69d-60a0-4ded-a64d-eeef3cda1d93",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"crm\\\\ncrm_k1\\\\ncrm_loss_variants\\\\ncrm_lto_splitA\\\\ncrm_lto_splitA_fixed\\\\ncrm_pi05\\\\ncrm_pi05_full\\\\ncrm_unified_4suite\\\\ncrm_v2\\\\ncrm_v3_norm\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"crm\\ncrm_k1\\ncrm_loss_variants\\ncrm_lto_splitA\\ncrm_lto_splitA_fixed\\ncrm_pi05\\ncrm_pi05_full\\ncrm_unified_4suite\\ncrm_v2\\ncrm_v3_norm\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
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
Let me check the CRM checkpoint and also look at what Long s47 experiments are missing (since k2mean-s47 seems missing).

Also, I need to think about what to deploy. Goal/Object s42-s46 are all complete. Let me check:

1. Are there any Goal/Object s47 experiments needed?
2. What PREPARING experiments could run on these GPUs?

Let me check what Long experiments exist for s47:
- RUNNING: vla-only-s47, crm-norm005-s47, reconvla-s47, adapt-tau025-s47


- Missing: k2mean-s47

Now I'm looking at what else could be deployed and where the current PREPARING/QUEUED experiments would run. The most actionable items are the missing k2mean-s47 for the Long experiments and checking whether eval-supp-obj-crm-norm005-s46 is a duplicate. I should also verify if any Goal/Object s47 experiments are actually needed based on what's already done.

Re-reading the task, I need to focus on the specific seeds mentioned (s45/s46) for Goal/Object experiments—those are complete. Now I'm checking what PREPARING/QUEUED experiments can run on the available GPU resources on bjb1-18228. From the PREPARING list, the non-precompute and non-spatial eval experiments that could run are eval-supp-obj-crm-norm005-s46, the SmolVLA long variants across different seeds, and eval-smolvla-crm-long.

Looking at the additional PREPARING experiments—SmolVLA CRM long variants with different seeds, eval-pi05-baseline-object-seed42-r2, eval-random-selection-object-seed42-r3, and various obs-only and perdof configurations—I realize I should focus on what's actually in PREPARING rather than creating new experiments. Let me check what's currently running to understand the GPU allocation and what else could be deployed. Actually I realize I should just pick two PREPARING eval experiments and deploy them on GPU 1 and 2. Let me look at the details of some PREPARING experiments.

But first, let me check: maybe the Long k2mean s47 is indeed the missing one that should be created. The user said "检查是否有其他 PREPARING/QUEUED 实验可以跑" - maybe I should also consider creating the missing Long k2mean s47.

Hmm, let me just be practical. Let me:
1. Create eval-supp-long-k2mean-s47 (vla_only doesn't need CRM, but k2mean does need... let me check what mode k2mean uses)

Actually, "k2mean" is not a mode in evaluate.py. The modes are: vla_only, crm_scalar, crm_perdof, acr_vla, crm_obs_only, reconvla, random_selection, adaptive_k, adaptive_unc_head, adaptive_conformal_crm.

Let me check how previous k2mean experiments were run by looking at a completed k2mean experiment's spec.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "3b8cb7e6-7d67-4bcb-869e-2d650731627d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018JXTfyC2fzXiZUxwm9X4z3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7210,
      "cache_read_input_tokens": 45687,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7210
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

Goal/Object s42-s46 全部完成。Long s47 缺 k2mean。让我查看已有 k2mean 实验的配置和可用的 PREPARING 实验。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "9f1a93c4-0c63-468e-8f27-300b3a8dd60f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018JXTfyC2fzXiZUxwm9X4z3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7210,
      "cache_read_input_tokens": 45687,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7210
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01Ntonnug4bLDKm9fNXn1V3R`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": {
    "exp_id": "eval-supp-long-k2mean-s45"
  },
  "limit": 1,
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
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "d98d95a6-42a5-4b9c-82ca-781cf0fbe20e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018JXTfyC2fzXiZUxwm9X4z3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7210,
      "cache_read_input_tokens": 45687,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7210
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01HsjdjPXJxThiq1GUUmHKm1`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": {
    "exp_id": "eval-supp-long-vla-only-s47"
  },
  "limit": 1,
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
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "df449e22-848d-4447-87c6-b4ebc104b4f8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018JXTfyC2fzXiZUxwm9X4z3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7210,
      "cache_read_input_tokens": 45687,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7210
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

_source line 38 · 2026-05-24T07:12:22.259Z_

<details><summary>↩ Tool result · `toolu_01Ntonnug4bLDKm9fNXn1V3R`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.7862}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "682750b5-9489-4783-8560-a34770374f80",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.7862}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.7862}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-24T07:12:24.205Z_

<details><summary>↩ Tool result · `toolu_01HsjdjPXJxThiq1GUUmHKm1`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.9318}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "29b5e8cf-979c-4427-8138-1f099916fa6d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.9318}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.9318}}"
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
The filter doesn't work by exp_id like that. Let me try reading specific experiments differently. Let me just read the k2mean experiments directly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "c5ca1b8a-b650-47e0-aa6d-991b669e11e2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011AWk84EQHWkN3oQxEZ3EJw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1524,
      "cache_read_input_tokens": 52897,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1524
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

_source line 41_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01XnPPKH82ivXNaPvmXJXskK`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": {
    "status": "DONE"
  },
  "limit": 5,
  "fields": [
    "exp_id",
    "spec"
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
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "2d617bb0-bce1-43b2-897a-3218dacbdefa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011AWk84EQHWkN3oQxEZ3EJw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1524,
      "cache_read_input_tokens": 52897,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1524
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

_source line 42 · 2026-05-24T07:12:29.590Z_

<details><summary>↩ Tool result · `toolu_01XnPPKH82ivXNaPvmXJXskK`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"crm-train-openvla-k1-multiscale-object\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/train_crm_k1.py --benchmark object --cache_dir /root/autodl-tmp/crm_cache_k1_openvla --obs_dim 4096 --epochs 50 --batch_size 512 --lr 1e-3 --seed 42 --output_dir /root/autodl-tmp/checkpoints/crm_openvla_k1_multiscale/object --wandb_run_name crm-openvla-k1-multiscale-object --loss_mode multi\", \"server\": \"bjb2-28827\", \"data_path\": \"/root/autodl-tmp/crm_cache_k1_openvla/object\", \"data_count\": 74507, \"model_name\": \"MultiScaleCRM-OpenVLA-K1\", \"seed\": 42}}, \"eval-supp-long-k2mean-s46-r2\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark long --mode vla_only --baseline_mode mean --K 2 --seed 46 --n_rollouts 20 --output_file logs/eval_long_k2mean_seed46.json\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:3\"], \"tmux_session\": \"long-k2mean-s46-r2\", \"log_path\": \"logs/eval-supp-long-k2mean-s46-r2.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 46, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"n/a-baseline\", \"parent\": \"eval-supp-long-k2mean-s46\"}}, \"eval-supp-long-reconvla-s46-r2\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark long --mode reconvla --seed 46 --n_rollouts 20 --K 10\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:2\"], \"tmux_session\": \"long-reconvla-s46-r2\", \"log_path\": \"logs/eval-supp-long-reconvla-s46-r2.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 46, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"n/a-reconvla\", \"parent\": \"eval-supp-long-reconvla-s46\"}}, \"eval-supp-long-crm-norm005-s46-r2\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark long --mode crm_obs_only --seed 46 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:1\"], \"tmux_session\": \"long-crm-s46-r2\", \"log_path\": \"logs/eval-supp-long-crm-norm005-s46-r2.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 46, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"parent\": \"eval-supp-long-crm-norm005-s46\"}}, \"eval-supp-long-adapt-tau025-s46-r2\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark long --mode adaptive_conformal_crm --seed 46 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --max_correction_norm 0.2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:0\"], \"tmux_session\": \"long-adapt-s46-r2\", \"log_path\": \"logs/eval-supp-long-adapt-tau025-s46-r2.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 46, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"parent\": \"eval-supp-long-adapt-tau025-s46\"}}}, \"count\": 5, \"total\": 761, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.989}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "28d109d9-8051-4641-ae71-0b79407a9618",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"crm-train-openvla-k1-multiscale-object\\\": {\\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python -u src/train_crm_k1.py --benchmark object --cache_dir /root/autodl-tmp/crm_cache_k1_openvla --obs_dim 4096 --epochs 50 --batch_size 512 --lr 1e-3 --seed 42 --output_dir /root/autodl-tmp/checkpoints/crm_openvla_k1_multiscale/object --wandb_run_name crm-openvla-k1-multiscale-object --loss_mode multi\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/crm_cache_k1_openvla/object\\\", \\\"data_count\\\": 74507, \\\"model_name\\\": \\\"MultiScaleCRM-OpenVLA-K1\\\", \\\"seed\\\": 42}}, \\\"eval-supp-long-k2mean-s46-r2\\\": {\\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark long --mode vla_only --baseline_mode mean --K 2 --seed 46 --n_rollouts 20 --output_file logs/eval_long_k2mean_seed46.json\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"tmux_session\\\": \\\"long-k2mean-s46-r2\\\", \\\"log_path\\\": \\\"logs/eval-supp-long-k2mean-s46-r2.log\\\", \\\"data_path\\\": \\\"LIBERO-Long\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 46, \\\"eval_data\\\": \\\"LIBERO-Long\\\", \\\"checkpoint_source\\\": \\\"n/a-baseline\\\", \\\"parent\\\": \\\"eval-supp-long-k2mean-s46\\\"}}, \\\"eval-supp-long-reconvla-s46-r2\\\": {\\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark long --mode reconvla --seed 46 --n_rollouts 20 --K 10\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"tmux_session\\\": \\\"long-reconvla-s46-r2\\\", \\\"log_path\\\": \\\"logs/eval-supp-long-reconvla-s46-r2.log\\\", \\\"data_path\\\": \\\"LIBERO-Long\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 46, \\\"eval_data\\\": \\\"LIBERO-Long\\\", \\\"checkpoint_source\\\": \\\"n/a-reconvla\\\", \\\"parent\\\": \\\"eval-supp-long-reconvla-s46\\\"}}, \\\"eval-supp-long-crm-norm005-s46-r2\\\": {\\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark long --mode crm_obs_only --seed 46 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"tmux_session\\\": \\\"long-crm-s46-r2\\\", \\\"log_path\\\": \\\"logs/eval-supp-long-crm-norm005-s46-r2.log\\\", \\\"data_path\\\": \\\"LIBERO-Long\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 46, \\\"eval_data\\\": \\\"LIBERO-Long\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\\\", \\\"parent\\\": \\\"eval-supp-long-crm-norm005-s46\\\"}}, \\\"eval-supp-long-adapt-tau025-s46-r2\\\": {\\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark long --mode adaptive_conformal_crm --seed 46 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --max_correction_norm 0.2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"tmux_session\\\": \\\"long-adapt-s46-r2\\\", \\\"log_path\\\": \\\"logs/eval-supp-long-adapt-tau025-s46-r2.log\\\", \\\"data_path\\\": \\\"LIBERO-Long\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 46, \\\"eval_data\\\": \\\"LIBERO-Long\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\\\", \\\"parent\\\": \\\"eval-supp-long-adapt-tau025-s46\\\"}}}, \\\"count\\\": 5, \\\"total\\\": 761, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.989}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"crm-train-openvla-k1-multiscale-object\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/train_crm_k1.py --benchmark object --cache_dir /root/autodl-tmp/crm_cache_k1_openvla --obs_dim 4096 --epochs 50 --batch_size 512 --lr 1e-3 --seed 42 --output_dir /root/autodl-tmp/checkpoints/crm_openvla_k1_multiscale/object --wandb_run_name crm-openvla-k1-multiscale-object --loss_mode multi\", \"server\": \"bjb2-28827\", \"data_path\": \"/root/autodl-tmp/crm_cache_k1_openvla/object\", \"data_count\": 74507, \"model_name\": \"MultiScaleCRM-OpenVLA-K1\", \"seed\": 42}}, \"eval-supp-long-k2mean-s46-r2\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark long --mode vla_only --baseline_mode mean --K 2 --seed 46 --n_rollouts 20 --output_file logs/eval_long_k2mean_seed46.json\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:3\"], \"tmux_session\": \"long-k2mean-s46-r2\", \"log_path\": \"logs/eval-supp-long-k2mean-s46-r2.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 46, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"n/a-baseline\", \"parent\": \"eval-supp-long-k2mean-s46\"}}, \"eval-supp-long-reconvla-s46-r2\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark long --mode reconvla --seed 46 --n_rollouts 20 --K 10\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:2\"], \"tmux_session\": \"long-reconvla-s46-r2\", \"log_path\": \"logs/eval-supp-long-reconvla-s46-r2.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 46, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"n/a-reconvla\", \"parent\": \"eval-supp-long-reconvla-s46\"}}, \"eval-supp-long-crm-norm005-s46-r2\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark long --mode crm_obs_only --seed 46 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:1\"], \"tmux_session\": \"long-crm-s46-r2\", \"log_path\": \"logs/eval-supp-long-crm-norm005-s46-r2.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 46, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"parent\": \"eval-supp-long-crm-norm005-s46\"}}, \"eval-supp-long-adapt-tau025-s46-r2\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark long --mode adaptive_conformal_crm --seed 46 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --max_correction_norm 0.2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:0\"], \"tmux_session\": \"long-adapt-s46-r2\", \"log_path\": \"logs/eval-supp-long-adapt-tau025-s46-r2.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 46, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"parent\": \"eval-supp-long-adapt-tau025-s46\"}}}, \"count\": 5, \"total\": 761, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.989}}"
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
Now I have the command templates. Let me understand what's going on:

k2mean: `--mode vla_only --baseline_mode mean --K 2` (VLA-only with K=2 mean, no CRM needed)
reconvla: `--mode reconvla --K 10` (no CRM needed)
crm-norm005: `--mode crm_obs_only --K 10 --max_correction_norm 0.05 --crm_checkpoint ...` (needs CRM)
adapt-tau025: `--mode adaptive_conformal_crm --K 2 --conformal_threshold 0.25 --max_correction_norm 0.2 --crm_checkpoint ...` (needs CRM)


Looking at the s47 experiments, I see three of the four variants are running—eval-supp-long-crm-norm005-s47, eval-supp-long-reconvla-s47, and eval-supp-long-adapt-tau025-s47—but eval-supp-long-k2mean-s47 is missing. I also don't see any Object or Goal s47 experiments in either the done or running lists, so those might need to be created as well.

Since the user specifically mentioned s45 and s46 are complete for Goal and Object experiments, I should check the PREPARING and QUEUED states to see if those are finished. I also need to look at which servers these running experiments are on to determine if any are using bjb1-18228.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "de110e81-73ee-4b6d-8935-8f566ced4865",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AoLqPMTjXpds7VeciY4dNM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1667,
      "cache_read_input_tokens": 54421,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1667
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

_source line 44_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_012wycViRGRuMSZHnNuGt7sY`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": {
    "status": "RUNNING"
  },
  "limit": 0,
  "fields": [
    "exp_id",
    "spec"
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
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "fe88ff04-72e8-4eed-bb28-35e2f5746451",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AoLqPMTjXpds7VeciY4dNM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1667,
      "cache_read_input_tokens": 54421,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1667
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

_source line 45 · 2026-05-24T07:12:54.526Z_

<details><summary>↩ Tool result · `toolu_012wycViRGRuMSZHnNuGt7sY`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-openvla-object-vla-only-seed42-v3\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u src/openvla_eval.py --benchmark object --model_path /root/autodl-tmp/models/openvla-libero-object --mode vla_only --seed 42 --n_rollouts 20 --gpu 0 --output_file logs/eval_openvla_object_vla_only_seed42_v3.json\", \"server\": \"bjb2-28827\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_object\", \"data_count\": 200, \"model_name\": \"openvla-libero-object\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/openvla-libero-object\", \"eval_data\": \"LIBERO-Object (10 tasks x 20 rollouts = 200 episodes)\", \"pid\": \"114984\", \"log_path\": \"/tmp/eval_openvla_vla_only_seed42_v3.log\", \"checkpoint_path\": \"/root/autodl-tmp/models/openvla-libero-object\"}}, \"eval-supp-long-vla-only-s47\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark long --mode vla_only --baseline_mode mean --K 2 --seed 47 --n_rollouts 20 --output_file logs/eval_long_k2mean_seed47.json\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:5\"], \"tmux_session\": \"long-vla-s47\", \"log_path\": \"logs/eval-supp-long-vla-only-s47.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"n/a-baseline\", \"parent\": \"eval-supp-long-vla-only-s46\"}}, \"eval-supp-long-crm-norm005-s47\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark long --mode crm_obs_only --seed 47 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"tmux_session\": \"long-crm-s47\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-crm-norm005-s47.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\"}}, \"eval-supp-long-reconvla-s47\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark long --mode reconvla --seed 47 --n_rollouts 20 --K 10\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"tmux_session\": \"long-reconvla-s47\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-reconvla-s47.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"n/a-reconvla\"}}, \"eval-supp-spatial-crm-norm005-s47\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 47 --n_rollouts 20 --max_correction_norm 0.05 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_spatial_crm_obs_only_norm0.05_seed47.json\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"235730\", \"tmux_session\": \"eval-spatial-crm-s47\", \"log_path\": \"/tmp/eval_spatial_crm_s47.log\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA+CRM\", \"seed\": 47, \"eval_data\": \"LIBERO-Spatial\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"checkpoint_path\": \"n/a-eval-only\", \"submitted_at\": \"2026-05-24T06:50:07Z\", \"submitted_via\": \"ssh_execute_tmux\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-supp-vla-only-spatial-s46\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark spatial --mode vla_only --seed 46 --n_rollouts 20 --K 1\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/models/smolvla_libero/\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"benchmark\": \"spatial\", \"mode\": \"vla_only\", \"tmux_session\": \"eval-supp-vla-only-spatial-s46\", \"gpu\": 5}}, \"eval-supp-adapt-tau025-spatial-s45\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark spatial --mode adaptive_conformal_crm --seed 45 --n_rollouts 20 --K 10 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla+crm-adaptive\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"benchmark\": \"spatial\", \"mode\": \"adaptive_conformal_crm\", \"max_correction_norm\": 0.2, \"conformal_threshold\": 0.25, \"K\": 10, \"tmux_session\": \"eval-supp-adapt-tau025-spatial-s45\", \"gpu\": 4}}, \"eval-supp-crm-norm005-spatial-s45\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 45 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla+crm\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"benchmark\": \"spatial\", \"mode\": \"crm_obs_only\", \"max_correction_norm\": 0.05, \"K\": 10, \"tmux_session\": \"eval-supp-crm-norm005-spatial-s45\", \"gpu\": 3}}, \"eval-supp-vla-only-spatial-s45\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark spatial --mode vla_only --seed 45 --n_rollouts 20 --K 1\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/models/smolvla_libero/\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"benchmark\": \"spatial\", \"mode\": \"vla_only\", \"tmux_session\": \"eval-supp-vla-only-spatial-s45\", \"gpu\": 2}}, \"eval-supp-long-adapt-tau025-s47\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark long --mode adaptive_conformal_crm --seed 47 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --max_correction_norm 0.2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:4\"], \"tmux_session\": \"long-adapt-s47\", \"log_path\": \"logs/eval-supp-long-adapt-tau025-s47.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"parent\": \"eval-supp-long-adapt-tau025-s46-r2\"}}, \"eval-supp-long-k2mean-s46\": {\"spec\": {\"command\": \"python -u src/evaluate.py --benchmark long --mode vla_only --baseline_mode mean --K 2 --seed 46 --n_rollouts 20 --output_file logs/eval_long_k2mean_seed46.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": 263191, \"log_path\": \"logs/eval_long_k2mean_seed46.json\", \"submitted_at\": \"2026-05-24T03:23:22.142Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 46, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"n/a-baseline\"}}, \"eval-supp-long-reconvla-s46\": {\"spec\": {\"command\": \"python -u src/evaluate.py --benchmark long --mode reconvla --seed 46 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": 262529, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-reconvla-s46.log\", \"submitted_at\": \"2026-05-24T03:23:15.265Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 46, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\"}}, \"eval-supp-long-crm-norm005-s46\": {\"spec\": {\"command\": \"python -u src/evaluate.py --benchmark long --mode crm_obs_only --seed 46 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": 262247, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-crm-norm005-s46.log\", \"submitted_at\": \"2026-05-24T03:23:09.570Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 46, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\"}}, \"eval-supp-long-adapt-tau025-s46\": {\"spec\": {\"command\": \"python -u src/evaluate.py --benchmark long --mode adaptive_conformal_crm --seed 46 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --max_correction_norm 0.2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": 261974, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-adapt-tau025-s46.log\", \"submitted_at\": \"2026-05-24T03:23:03.745Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 46, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\"}}, \"precompute-pi05-long-2048-r2\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 nohup python -u src/train_crm.py --precompute --model pi05 --benchmark long --K 10 --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/ > /root/autodl-tmp/logs/precompute_pi05_long_2048.log 2>&1 &\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": 114507, \"data_path\": \"/root/autodl-tmp/crm_cache_pi05_2048/long/\", \"data_count\": 136090, \"model_name\": \"pi0.5\", \"seed\": 0, \"log_path\": \"/root/autodl-tmp/logs/precompute_pi05_long_2048.log\"}}, \"precompute-pi05-object-2048-r2\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 nohup python -u src/train_crm.py --precompute --model pi05 --benchmark object --K 10 --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/ > /root/autodl-tmp/logs/precompute_pi05_object_2048.log 2>&1 &\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": 113456, \"data_path\": \"/root/autodl-tmp/crm_cache_pi05_2048/object/\", \"data_count\": 72507, \"model_name\": \"pi0.5\", \"seed\": 0, \"log_path\": \"/root/autodl-tmp/logs/precompute_pi05_object_2048.log\"}}}, \"count\": 16, \"total\": 16, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 8.227}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "6425d041-5064-46c0-b229-03a1cb824acf",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"eval-openvla-object-vla-only-seed42-v3\\\": {\\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u src/openvla_eval.py --benchmark object --model_path /root/autodl-tmp/models/openvla-libero-object --mode vla_only --seed 42 --n_rollouts 20 --gpu 0 --output_file logs/eval_openvla_object_vla_only_seed42_v3.json\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/libero_data/libero_object\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"openvla-libero-object\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/models/openvla-libero-object\\\", \\\"eval_data\\\": \\\"LIBERO-Object (10 tasks x 20 rollouts = 200 episodes)\\\", \\\"pid\\\": \\\"114984\\\", \\\"log_path\\\": \\\"/tmp/eval_openvla_vla_only_seed42_v3.log\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/models/openvla-libero-object\\\"}}, \\\"eval-supp-long-vla-only-s47\\\": {\\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark long --mode vla_only --baseline_mode mean --K 2 --seed 47 --n_rollouts 20 --output_file logs/eval_long_k2mean_seed47.json\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"gpu\\\": [\\\"cuda:5\\\"], \\\"tmux_session\\\": \\\"long-vla-s47\\\", \\\"log_path\\\": \\\"logs/eval-supp-long-vla-only-s47.log\\\", \\\"data_path\\\": \\\"LIBERO-Long\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 47, \\\"eval_data\\\": \\\"LIBERO-Long\\\", \\\"checkpoint_source\\\": \\\"n/a-baseline\\\", \\\"parent\\\": \\\"eval-supp-long-vla-only-s46\\\"}}, \\\"eval-supp-long-crm-norm005-s47\\\": {\\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark long --mode crm_obs_only --seed 47 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:5\\\"], \\\"tmux_session\\\": \\\"long-crm-s47\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-supp-long-crm-norm005-s47.log\\\", \\\"data_path\\\": \\\"LIBERO-Long\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 47, \\\"eval_data\\\": \\\"LIBERO-Long\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\\\"}}, \\\"eval-supp-long-reconvla-s47\\\": {\\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark long --mode reconvla --seed 47 --n_rollouts 20 --K 10\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:4\\\"], \\\"tmux_session\\\": \\\"long-reconvla-s47\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-supp-long-reconvla-s47.log\\\", \\\"data_path\\\": \\\"LIBERO-Long\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 47, \\\"eval_data\\\": \\\"LIBERO-Long\\\", \\\"checkpoint_source\\\": \\\"n/a-reconvla\\\"}}, \\\"eval-supp-spatial-crm-norm005-s47\\\": {\\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 47 --n_rollouts 20 --max_correction_norm 0.05 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_spatial_crm_obs_only_norm0.05_seed47.json\\\", \\\"server\\\": \\\"bjb2-40593\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"235730\\\", \\\"tmux_session\\\": \\\"eval-spatial-crm-s47\\\", \\\"log_path\\\": \\\"/tmp/eval_spatial_crm_s47.log\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA+CRM\\\", \\\"seed\\\": 47, \\\"eval_data\\\": \\\"LIBERO-Spatial\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"checkpoint_path\\\": \\\"n/a-eval-only\\\", \\\"submitted_at\\\": \\\"2026-05-24T06:50:07Z\\\", \\\"submitted_via\\\": \\\"ssh_execute_tmux\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}}, \\\"eval-supp-vla-only-spatial-s46\\\": {\\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark spatial --mode vla_only --seed 46 --n_rollouts 20 --K 1\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 46, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/models/smolvla_libero/\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial 10 tasks x 20 rollouts\\\", \\\"benchmark\\\": \\\"spatial\\\", \\\"mode\\\": \\\"vla_only\\\", \\\"tmux_session\\\": \\\"eval-supp-vla-only-spatial-s46\\\", \\\"gpu\\\": 5}}, \\\"eval-supp-adapt-tau025-spatial-s45\\\": {\\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark spatial --mode adaptive_conformal_crm --seed 45 --n_rollouts 20 --K 10 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"smolvla+crm-adaptive\\\", \\\"seed\\\": 45, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial 10 tasks x 20 rollouts\\\", \\\"benchmark\\\": \\\"spatial\\\", \\\"mode\\\": \\\"adaptive_conformal_crm\\\", \\\"max_correction_norm\\\": 0.2, \\\"conformal_threshold\\\": 0.25, \\\"K\\\": 10, \\\"tmux_session\\\": \\\"eval-supp-adapt-tau025-spatial-s45\\\", \\\"gpu\\\": 4}}, \\\"eval-supp-crm-norm005-spatial-s45\\\": {\\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 45 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"smolvla+crm\\\", \\\"seed\\\": 45, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial 10 tasks x 20 rollouts\\\", \\\"benchmark\\\": \\\"spatial\\\", \\\"mode\\\": \\\"crm_obs_only\\\", \\\"max_correction_norm\\\": 0.05, \\\"K\\\": 10, \\\"tmux_session\\\": \\\"eval-supp-crm-norm005-spatial-s45\\\", \\\"gpu\\\": 3}}, \\\"eval-supp-vla-only-spatial-s45\\\": {\\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark spatial --mode vla_only --seed 45 --n_rollouts 20 --K 1\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 45, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/models/smolvla_libero/\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial 10 tasks x 20 rollouts\\\", \\\"benchmark\\\": \\\"spatial\\\", \\\"mode\\\": \\\"vla_only\\\", \\\"tmux_session\\\": \\\"eval-supp-vla-only-spatial-s45\\\", \\\"gpu\\\": 2}}, \\\"eval-supp-long-adapt-tau025-s47\\\": {\\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark long --mode adaptive_conformal_crm --seed 47 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --max_correction_norm 0.2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"gpu\\\": [\\\"cuda:4\\\"], \\\"tmux_session\\\": \\\"long-adapt-s47\\\", \\\"log_path\\\": \\\"logs/eval-supp-long-adapt-tau025-s47.log\\\", \\\"data_path\\\": \\\"LIBERO-Long\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 47, \\\"eval_data\\\": \\\"LIBERO-Long\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\\\", \\\"parent\\\": \\\"eval-supp-long-adapt-tau025-s46-r2\\\"}}, \\\"eval-supp-long-k2mean-s46\\\": {\\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --benchmark long --mode vla_only --baseline_mode mean --K 2 --seed 46 --n_rollouts 20 --output_file logs/eval_long_k2mean_seed46.json\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"pid\\\": 263191, \\\"log_path\\\": \\\"logs/eval_long_k2mean_seed46.json\\\", \\\"submitted_at\\\": \\\"2026-05-24T03:23:22.142Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"LIBERO-Long\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 46, \\\"eval_data\\\": \\\"LIBERO-Long\\\", \\\"checkpoint_source\\\": \\\"n/a-baseline\\\"}}, \\\"eval-supp-long-reconvla-s46\\\": {\\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --benchmark long --mode reconvla --seed 46 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"pid\\\": 262529, \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-supp-long-reconvla-s46.log\\\", \\\"submitted_at\\\": \\\"2026-05-24T03:23:15.265Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"LIBERO-Long\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 46, \\\"eval_data\\\": \\\"LIBERO-Long\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\\\"}}, \\\"eval-supp-long-crm-norm005-s46\\\": {\\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --benchmark long --mode crm_obs_only --seed 46 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": 262247, \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-supp-long-crm-norm005-s46.log\\\", \\\"submitted_at\\\": \\\"2026-05-24T03:23:09.570Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"LIBERO-Long\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 46, \\\"eval_data\\\": \\\"LIBERO-Long\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\\\"}}, \\\"eval-supp-long-adapt-tau025-s46\\\": {\\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --benchmark long --mode adaptive_conformal_crm --seed 46 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --max_correction_norm 0.2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": 261974, \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-supp-long-adapt-tau025-s46.log\\\", \\\"submitted_at\\\": \\\"2026-05-24T03:23:03.745Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"LIBERO-Long\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 46, \\\"eval_data\\\": \\\"LIBERO-Long\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\\\"}}, \\\"precompute-pi05-long-2048-r2\\\": {\\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=3 nohup python -u src/train_crm.py --precompute --model pi05 --benchmark long --K 10 --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/ > /root/autodl-tmp/logs/precompute_pi05_long_2048.log 2>&1 &\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"pid\\\": 114507, \\\"data_path\\\": \\\"/root/autodl-tmp/crm_cache_pi05_2048/long/\\\", \\\"data_count\\\": 136090, \\\"model_name\\\": \\\"pi0.5\\\", \\\"seed\\\": 0, \\\"log_path\\\": \\\"/root/autodl-tmp/logs/precompute_pi05_long_2048.log\\\"}}, \\\"precompute-pi05-object-2048-r2\\\": {\\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 nohup python -u src/train_crm.py --precompute --model pi05 --benchmark object --K 10 --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/ > /root/autodl-tmp/logs/precompute_pi05_object_2048.log 2>&1 &\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": 113456, \\\"data_path\\\": \\\"/root/autodl-tmp/crm_cache_pi05_2048/object/\\\", \\\"data_count\\\": 72507, \\\"model_name\\\": \\\"pi0.5\\\", \\\"seed\\\": 0, \\\"log_path\\\": \\\"/root/autodl-tmp/logs/precompute_pi05_object_2048.log\\\"}}}, \\\"count\\\": 16, \\\"total\\\": 16, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 8.227}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval-openvla-object-vla-only-seed42-v3\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u src/openvla_eval.py --benchmark object --model_path /root/autodl-tmp/models/openvla-libero-object --mode vla_only --seed 42 --n_rollouts 20 --gpu 0 --output_file logs/eval_openvla_object_vla_only_seed42_v3.json\", \"server\": \"bjb2-28827\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_object\", \"data_count\": 200, \"model_name\": \"openvla-libero-object\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/openvla-libero-object\", \"eval_data\": \"LIBERO-Object (10 tasks x 20 rollouts = 200 episodes)\", \"pid\": \"114984\", \"log_path\": \"/tmp/eval_openvla_vla_only_seed42_v3.log\", \"checkpoint_path\": \"/root/autodl-tmp/models/openvla-libero-object\"}}, \"eval-supp-long-vla-only-s47\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark long --mode vla_only --baseline_mode mean --K 2 --seed 47 --n_rollouts 20 --output_file logs/eval_long_k2mean_seed47.json\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:5\"], \"tmux_session\": \"long-vla-s47\", \"log_path\": \"logs/eval-supp-long-vla-only-s47.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"n/a-baseline\", \"parent\": \"eval-supp-long-vla-only-s46\"}}, \"eval-supp-long-crm-norm005-s47\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark long --mode crm_obs_only --seed 47 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"tmux_session\": \"long-crm-s47\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-crm-norm005-s47.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\"}}, \"eval-supp-long-reconvla-s47\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark long --mode reconvla --seed 47 --n_rollouts 20 --K 10\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"tmux_session\": \"long-reconvla-s47\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-reconvla-s47.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"n/a-reconvla\"}}, \"eval-supp-spatial-crm-norm005-s47\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 47 --n_rollouts 20 --max_correction_norm 0.05 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_spatial_crm_obs_only_norm0.05_seed47.json\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"235730\", \"tmux_session\": \"eval-spatial-crm-s47\", \"log_path\": \"/tmp/eval_spatial_crm_s47.log\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA+CRM\", \"seed\": 47, \"eval_data\": \"LIBERO-Spatial\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"checkpoint_path\": \"n/a-eval-only\", \"submitted_at\": \"2026-05-24T06:50:07Z\", \"submitted_via\": \"ssh_execute_tmux\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-supp-vla-only-spatial-s46\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark spatial --mode vla_only --seed 46 --n_rollouts 20 --K 1\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/models/smolvla_libero/\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"benchmark\": \"spatial\", \"mode\": \"vla_only\", \"tmux_session\": \"eval-supp-vla-only-spatial-s46\", \"gpu\": 5}}, \"eval-supp-adapt-tau025-spatial-s45\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark spatial --mode adaptive_conformal_crm --seed 45 --n_rollouts 20 --K 10 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla+crm-adaptive\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"benchmark\": \"spatial\", \"mode\": \"adaptive_conformal_crm\", \"max_correction_norm\": 0.2, \"conformal_threshold\": 0.25, \"K\": 10, \"tmux_session\": \"eval-supp-adapt-tau025-spatial-s45\", \"gpu\": 4}}, \"eval-supp-crm-norm005-spatial-s45\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 45 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla+crm\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"benchmark\": \"spatial\", \"mode\": \"crm_obs_only\", \"max_correction_norm\": 0.05, \"K\": 10, \"tmux_session\": \"eval-supp-crm-norm005-spatial-s45\", \"gpu\": 3}}, \"eval-supp-vla-only-spatial-s45\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark spatial --mode vla_only --seed 45 --n_rollouts 20 --K 1\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/models/smolvla_libero/\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"benchmark\": \"spatial\", \"mode\": \"vla_only\", \"tmux_session\": \"eval-supp-vla-only-spatial-s45\", \"gpu\": 2}}, \"eval-supp-long-adapt-tau025-s47\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark long --mode adaptive_conformal_crm --seed 47 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --max_correction_norm 0.2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:4\"], \"tmux_session\": \"long-adapt-s47\", \"log_path\": \"logs/eval-supp-long-adapt-tau025-s47.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"parent\": \"eval-supp-long-adapt-tau025-s46-r2\"}}, \"eval-supp-long-k2mean-s46\": {\"spec\": {\"command\": \"python -u src/evaluate.py --benchmark long --mode vla_only --baseline_mode mean --K 2 --seed 46 --n_rollouts 20 --output_file logs/eval_long_k2mean_seed46.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": 263191, \"log_path\": \"logs/eval_long_k2mean_seed46.json\", \"submitted_at\": \"2026-05-24T03:23:22.142Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 46, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"n/a-baseline\"}}, \"eval-supp-long-reconvla-s46\": {\"spec\": {\"command\": \"python -u src/evaluate.py --benchmark long --mode reconvla --seed 46 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": 262529, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-reconvla-s46.log\", \"submitted_at\": \"2026-05-24T03:23:15.265Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 46, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\"}}, \"eval-supp-long-crm-norm005-s46\": {\"spec\": {\"command\": \"python -u src/evaluate.py --benchmark long --mode crm_obs_only --seed 46 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": 262247, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-crm-norm005-s46.log\", \"submitted_at\": \"2026-05-24T03:23:09.570Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 46, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\"}}, \"eval-supp-long-adapt-tau025-s46\": {\"spec\": {\"command\": \"python -u src/evaluate.py --benchmark long --mode adaptive_conformal_crm --seed 46 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --max_correction_norm 0.2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": 261974, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-adapt-tau025-s46.log\", \"submitted_at\": \"2026-05-24T03:23:03.745Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 46, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\"}}, \"precompute-pi05-long-2048-r2\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 nohup python -u src/train_crm.py --precompute --model pi05 --benchmark long --K 10 --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/ > /root/autodl-tmp/logs/precompute_pi05_long_2048.log 2>&1 &\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": 114507, \"data_path\": \"/root/autodl-tmp/crm_cache_pi05_2048/long/\", \"data_count\": 136090, \"model_name\": \"pi0.5\", \"seed\": 0, \"log_path\": \"/root/autodl-tmp/logs/precompute_pi05_long_2048.log\"}}, \"precompute-pi05-object-2048-r2\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 nohup python -u src/train_crm.py --precompute --model pi05 --benchmark object --K 10 --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/ > /root/autodl-tmp/logs/precompute_pi05_object_2048.log 2>&1 &\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": 113456, \"data_path\": \"/root/autodl-tmp/crm_cache_pi05_2048/object/\", \"data_count\": 72507, \"model_name\": \"pi0.5\", \"seed\": 0, \"log_path\": \"/root/autodl-tmp/logs/precompute_pi05_object_2048.log\"}}}, \"count\": 16, \"total\": 16, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 8.227}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 46_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear picture:

**RUNNING on bjb1-18228:**
- GPU 0: precompute-pi05-object-2048-r2
- GPU 3: precompute-pi05-long-2048-r2
- GPU 1: FREE
- GPU 2: FREE

**Long s47 status:**
- vla-only-s47: RUNNING (cqa1-32758)
- crm-norm005-s47: RUNNING (bjb1-32546)
- reconvla-s47: RUNNING (bjb1-32546)


- adapt-tau025-s47: RUNNING (cqa1-32758)
- k2mean-s47: MISSING

Goal/Object s42-s46 experiments are all complete, so I need to deploy eval-supp-long-k2mean-s47 on GPU 1 since it only requires VLA without CRM. For GPU 2, I'm deciding between another Long s47 variant or potentially a Goal/Object s47 experiment, though the latter wasn't explicitly mentioned.

Looking at what's available, I'm noticing something odd with the naming—eval-supp-long-vla-only-s47 appears to use the k2mean command structure despite its "vla-only" label, which is creating some confusion about what's actually distinct from the k2mean version I'm already deploying. I see the issue now — the running experiment labeled vla-only for s47 is actually using the k2mean command with K=2, not the true vla-only setup with K=1. So I need to figure out what the actual vla-only command looks like by examining the completed experiments, since I can't directly query them. Let me map out the five methods for the Long experiments: vla-only uses K=1, k2mean uses K=2 with mean baseline, reconvla uses K=10, and crm-norm005 has its own configuration. I'm realizing I misread the command — the eval-supp-long-vla-only-s47 experiment is actually running k2mean based on the output filename, not a true VLA-only baseline with K=1, so I need to deploy a separate experiment that actually uses K=1 for the genuine VLA-only comparison. the true vla-only K=1 is missing. So I'll deploy that on GPU 1. For GPU 2, I should check what else needs running—the user asked me to look for other PREPARING or QUEUED experiments if the main Goal/Object tasks are done. Since Goal and Object s47 don't exist yet and could be useful for the paper's supplementary materials, I should consider running one of those next.

Looking at what's actually feasible, the most impactful moves are deploying the Long VLA-only s47 to complete that set, then extending Goal to s47 as well—both are VLA-only so they won't need CRM checkpoints. But I should also verify what CRM checkpoints are available on the current GPU before finalizing the second deployment. I need to see the next thinking to rewrite it. Could you provide the next thinking chunk that follows the current rewritten thinking?
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "de836c8e-96aa-42cc-b5e0-4ac359d822dc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RqpwLKM68gycva3d3Ax5SB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5372,
      "cache_read_input_tokens": 56088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5372
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

_source line 47_

Long s47 缺真正的 VLA-only（K=1）。现有 `eval-supp-long-vla-only-s47` 实际上是 k2mean（K=2 mean）。

让我验证 bjb1-18228 上的环境，然后部署两个实验。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "ef04cff6-3d5c-427b-9d64-d26c8ad55863",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RqpwLKM68gycva3d3Ax5SB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5372,
      "cache_read_input_tokens": 56088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5372
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

_source line 48_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_012jkg9fYfZFR8GpuMhUwfrC`</summary>

```json
{
  "server": "bjb1-18228",
  "command": "ls /root/acr-vla-conformal-refinement/src/evaluate.py",
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
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "ee819b72-628c-4d89-998a-5dfa5df71564",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RqpwLKM68gycva3d3Ax5SB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5372,
      "cache_read_input_tokens": 56088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5372
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

_source line 49_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01YKkeW8neYECrZANeXwbCwh`</summary>

```json
{
  "server": "bjb1-18228",
  "command": "ls /root/autodl-tmp/checkpoints/crm_unified_4suite/crm_best.pt",
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
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "fb4eab87-2c6b-459a-af37-031c01310ef6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RqpwLKM68gycva3d3Ax5SB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5372,
      "cache_read_input_tokens": 56088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5372
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

_source line 50 · 2026-05-24T07:13:41.922Z_

<details><summary>↩ Tool result · `toolu_012jkg9fYfZFR8GpuMhUwfrC`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/src/evaluate.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "75e60b05-ede7-4031-a0bb-28e6d7230798",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/acr-vla-conformal-refinement/src/evaluate.py\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.41}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/src/evaluate.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-24T07:13:42.414Z_

<details><summary>↩ Tool result · `toolu_01YKkeW8neYECrZANeXwbCwh`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite/crm_best.pt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "85eef383-9ad1-42a8-9900-ff8ae41a7ea6",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/checkpoints/crm_unified_4suite/crm_best.pt\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite/crm_best.pt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 52_

<details><summary>Logged reasoning block</summary>

```text
Good, the code and checkpoint exist on bjb1-18228. Now I need to find the submit_training_job tool.

Let me now deploy two experiments:
1. GPU 1: eval-supp-long-vla-only-s47-r2 — true VLA-only K=1 for Long s47 (the existing s47 is actually k2mean)
2. GPU 2: eval-supp-goal-vla-only-s47 — VLA-only K=1 for Goal s47

Wait, let me reconsider. The user's task says:
- 优先 Goal seed 扩展（VLA-only 不需要 CRM checkpoint）


- 如果 Goal 都已完成，部署 Object seed 扩展

Since Goal s42-s46 are all done, I should extend to s47. The Long s47 set is nearly complete with just the true VLA-only method missing, so I'll prioritize filling that gap while also starting Goal s47.

I'll deploy one Goal s47 VLA-only and one Long s47 VLA-only experiment on the two available GPUs, then register them in the registry and submit the jobs using the training job tool.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "1ec63f0e-a5a0-4de5-8e2f-a51ba6b47ca7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XEzjMp2ojHDaSjRetVg5nb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2865,
      "cache_read_input_tokens": 61460,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2865
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

_source line 53_

环境确认。现在部署两个实验：
1. **GPU 1**: `eval-supp-long-vla-only-s47-r2` — Long s47 真正的 VLA-only (K=1)，填补 Long s47 缺口
2. **GPU 2**: `eval-supp-goal-vla-only-s47` — Goal s47 VLA-only，扩展 Goal seed

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "0be6436c-fb50-41be-b8d4-9b8ad90fc5f2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XEzjMp2ojHDaSjRetVg5nb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2865,
      "cache_read_input_tokens": 61460,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2865
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01NR5544Yf9kqdCLT86hHws1`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
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
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "2f0d5512-f104-4c90-ac46-1741915ffcde",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XEzjMp2ojHDaSjRetVg5nb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2865,
      "cache_read_input_tokens": 61460,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2865
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

_source line 55 · 2026-05-24T07:13:55.828Z_

<details><summary>↩ Tool result · `toolu_01NR5544Yf9kqdCLT86hHws1`</summary>

````text
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
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "64b5ede8-7f0b-4a73-be15-6e83188cf396",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 26
  }
}
```

</details>

---

### Assistant

_source line 56_

先注册两个实验，然后提交到 GPU 1 和 GPU 2。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "f2faed3e-0c0a-42df-9b7c-7c338e72c287",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017yFQVwfn3jeX6A1p8tC86E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1250,
      "cache_read_input_tokens": 64325,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1250
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

_source line 57_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01FXrPT11iHydwHV13Xz13tV`</summary>

```json
{
  "exp_id": "eval-supp-long-vla-only-s47-r2",
  "field": "hypothesis",
  "value": "Long s47 VLA-only (K=1) baseline to complete the Long s47 seed extension set. The existing eval-supp-long-vla-only-s47 is actually k2mean (K=2 mean), so this fills the true VLA-only gap.",
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
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "547073e8-0b5d-4887-ba4f-aa9bfe689ede",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017yFQVwfn3jeX6A1p8tC86E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1250,
      "cache_read_input_tokens": 64325,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1250
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

_source line 58_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01SE7VQNoVFA6PnRPvr9Tamh`</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-s47",
  "field": "hypothesis",
  "value": "Goal s47 VLA-only (K=1) baseline to extend Goal seed coverage beyond s42-s46 for supplementary variance analysis.",
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
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "c6f09928-2c4d-4694-980e-79e710b7a072",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017yFQVwfn3jeX6A1p8tC86E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1250,
      "cache_read_input_tokens": 64325,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1250
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

_source line 59 · 2026-05-24T07:14:06.065Z_

<details><summary>↩ Tool result · `toolu_01FXrPT11iHydwHV13Xz13tV`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-long-vla-only-s47-r2\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:14:04.522Z\", \"updated_at\": \"2026-05-24T07:14:04.522Z\", \"hypothesis\": \"Long s47 VLA-only (K=1) baseline to complete the Long s47 seed extension set. The existing eval-supp-long-vla-only-s47 is actually k2mean (K=2 mean), so this fills the true VLA-only gap.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.9858}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "71313d48-4fc0-499b-8805-4360a0959f4a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-supp-long-vla-only-s47-r2\\\", \\\"experiment\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T07:14:04.522Z\\\", \\\"updated_at\\\": \\\"2026-05-24T07:14:04.522Z\\\", \\\"hypothesis\\\": \\\"Long s47 VLA-only (K=1) baseline to complete the Long s47 seed extension set. The existing eval-supp-long-vla-only-s47 is actually k2mean (K=2 mean), so this fills the true VLA-only gap.\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 4.9858}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-long-vla-only-s47-r2\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:14:04.522Z\", \"updated_at\": \"2026-05-24T07:14:04.522Z\", \"hypothesis\": \"Long s47 VLA-only (K=1) baseline to complete the Long s47 seed extension set. The existing eval-supp-long-vla-only-s47 is actually k2mean (K=2 mean), so this fills the true VLA-only gap.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.9858}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-24T07:14:18.060Z_

<details><summary>↩ Tool result · `toolu_01SE7VQNoVFA6PnRPvr9Tamh`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-s47\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:14:14.567Z\", \"updated_at\": \"2026-05-24T07:14:14.567Z\", \"hypothesis\": \"Goal s47 VLA-only (K=1) baseline to extend Goal seed coverage beyond s42-s46 for supplementary variance analysis.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 11.9676}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "6b94f0ef-aab3-40ad-b56f-0db283c05e39",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-supp-goal-vla-only-s47\\\", \\\"experiment\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T07:14:14.567Z\\\", \\\"updated_at\\\": \\\"2026-05-24T07:14:14.567Z\\\", \\\"hypothesis\\\": \\\"Goal s47 VLA-only (K=1) baseline to extend Goal seed coverage beyond s42-s46 for supplementary variance analysis.\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 11.9676}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-s47\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:14:14.567Z\", \"updated_at\": \"2026-05-24T07:14:14.567Z\", \"hypothesis\": \"Goal s47 VLA-only (K=1) baseline to extend Goal seed coverage beyond s42-s46 for supplementary variance analysis.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 11.9676}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 61_

<details><summary>Logged reasoning block</summary>

```text
Good. Now I need to set parent and then transition to RUNNING with spec. Let me set parent first.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "a394e504-9ddb-4a2c-863e-7ed46a89338c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Te5zivEZZxw8b522WBwn2z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 844,
      "cache_read_input_tokens": 65575,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 844
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

_source line 62_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01PT59Bzs6kamPY5hhSSGPXr`</summary>

```json
{
  "exp_id": "eval-supp-long-vla-only-s47-r2",
  "field": "parent",
  "value": "eval-supp-long-vla-only-s46",
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
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "edcacc98-fa1b-4a4f-abe8-30f38e6252e7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Te5zivEZZxw8b522WBwn2z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 844,
      "cache_read_input_tokens": 65575,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 844
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

_source line 63_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01VcAxafWCrP3URHvYo5oWnz`</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-s47",
  "field": "parent",
  "value": "eval-supp-goal-vla-only-s46",
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
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "3076d3e9-d0cd-45b4-be96-6ab7a4cf8073",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Te5zivEZZxw8b522WBwn2z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 844,
      "cache_read_input_tokens": 65575,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 844
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

_source line 64 · 2026-05-24T07:14:44.043Z_

<details><summary>↩ Tool result · `toolu_01PT59Bzs6kamPY5hhSSGPXr`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-long-vla-only-s47-r2\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:14:04.522Z\", \"updated_at\": \"2026-05-24T07:14:38.729Z\", \"hypothesis\": \"Long s47 VLA-only (K=1) baseline to complete the Long s47 seed extension set. The existing eval-supp-long-vla-only-s47 is actually k2mean (K=2 mean), so this fills the true VLA-only gap.\", \"parent\": \"eval-supp-long-vla-only-s46\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 20.0022}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "a7039a9a-7408-4d55-8787-04c227115275",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-supp-long-vla-only-s47-r2\\\", \\\"experiment\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T07:14:04.522Z\\\", \\\"updated_at\\\": \\\"2026-05-24T07:14:38.729Z\\\", \\\"hypothesis\\\": \\\"Long s47 VLA-only (K=1) baseline to complete the Long s47 seed extension set. The existing eval-supp-long-vla-only-s47 is actually k2mean (K=2 mean), so this fills the true VLA-only gap.\\\", \\\"parent\\\": \\\"eval-supp-long-vla-only-s46\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 20.0022}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-long-vla-only-s47-r2\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:14:04.522Z\", \"updated_at\": \"2026-05-24T07:14:38.729Z\", \"hypothesis\": \"Long s47 VLA-only (K=1) baseline to complete the Long s47 seed extension set. The existing eval-supp-long-vla-only-s47 is actually k2mean (K=2 mean), so this fills the true VLA-only gap.\", \"parent\": \"eval-supp-long-vla-only-s46\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 20.0022}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-24T07:14:54.569Z_

<details><summary>↩ Tool result · `toolu_01VcAxafWCrP3URHvYo5oWnz`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-s47\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:14:14.567Z\", \"updated_at\": \"2026-05-24T07:14:52.999Z\", \"hypothesis\": \"Goal s47 VLA-only (K=1) baseline to extend Goal seed coverage beyond s42-s46 for supplementary variance analysis.\", \"parent\": \"eval-supp-goal-vla-only-s46\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 10.3921}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "e44f7261-119b-4c9c-85a5-75737d459e3e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-supp-goal-vla-only-s47\\\", \\\"experiment\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T07:14:14.567Z\\\", \\\"updated_at\\\": \\\"2026-05-24T07:14:52.999Z\\\", \\\"hypothesis\\\": \\\"Goal s47 VLA-only (K=1) baseline to extend Goal seed coverage beyond s42-s46 for supplementary variance analysis.\\\", \\\"parent\\\": \\\"eval-supp-goal-vla-only-s46\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 10.3921}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-s47\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:14:14.567Z\", \"updated_at\": \"2026-05-24T07:14:52.999Z\", \"hypothesis\": \"Goal s47 VLA-only (K=1) baseline to extend Goal seed coverage beyond s42-s46 for supplementary variance analysis.\", \"parent\": \"eval-supp-goal-vla-only-s46\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 10.3921}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 66_

Now submitting both jobs to bjb1-18228.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "cf8dc9d7-510f-4fbb-94ee-8c8ecf00abcb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017EhTRSmysf3M3e8D5BsmnW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 829,
      "cache_read_input_tokens": 66419,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 829
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

_source line 67_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01XZycS938sGbtQ7KwiqBUcL`</summary>

```json
{
  "server": "bjb1-18228",
  "command": "cd /root/acr-vla-conformal-refinement && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && tmux new-session -d -s long-vla-s47-r2 \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark long --mode vla_only --seed 47 --n_rollouts 20 --K 1 2>&1 | tee logs/eval-supp-long-vla-only-s47-r2.log\" && sleep 2 && tmux list-sessions",
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
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "e0acb24e-7be1-4b87-a2f4-f673c0a4c8a4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017EhTRSmysf3M3e8D5BsmnW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 829,
      "cache_read_input_tokens": 66419,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 829
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

_source line 68 · 2026-05-24T07:15:08.803Z_

<details><summary>↩ Tool result · `toolu_01XZycS938sGbtQ7KwiqBUcL`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"long-vla-s47-r2: 1 windows (created Sun May 24 15:15:06 2026)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.5}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "c08872aa-1276-4763-b1b4-5f76e4583d40",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"long-vla-s47-r2: 1 windows (created Sun May 24 15:15:06 2026)\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.5}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"long-vla-s47-r2: 1 windows (created Sun May 24 15:15:06 2026)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.5}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 69_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01VkZqyWxNPkJY5f4iBfwrmo`</summary>

```json
{
  "server": "bjb1-18228",
  "command": "cd /root/acr-vla-conformal-refinement && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && tmux new-session -d -s goal-vla-s47 \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark goal --mode vla_only --seed 47 --n_rollouts 20 --K 1 2>&1 | tee logs/eval-supp-goal-vla-only-s47.log\" && sleep 2 && tmux list-sessions",
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
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "e11b3fe3-0a5c-49e8-bdd3-c3465559f170",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RgshL22VwG5vNwwfSzqphx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 366,
      "cache_read_input_tokens": 67248,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 366
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

_source line 70 · 2026-05-24T07:15:15.214Z_

<details><summary>↩ Tool result · `toolu_01VkZqyWxNPkJY5f4iBfwrmo`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"goal-vla-s47: 1 windows (created Sun May 24 15:15:13 2026)\\nlong-vla-s47-r2: 1 windows (created Sun May 24 15:15:06 2026)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.47}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "ca2f294a-5280-43c4-a926-e906b99f99e0",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"goal-vla-s47: 1 windows (created Sun May 24 15:15:13 2026)\\\\nlong-vla-s47-r2: 1 windows (created Sun May 24 15:15:06 2026)\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.47}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"goal-vla-s47: 1 windows (created Sun May 24 15:15:13 2026)\\nlong-vla-s47-r2: 1 windows (created Sun May 24 15:15:06 2026)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.47}}"
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
Both tmux sessions are running. Let me verify they started correctly by checking the logs, and then get the PIDs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "abbdda08-3389-4df7-a05f-d07ec1145f56",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MyYfDtYYSzKia18MiJkZic",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 479,
      "cache_read_input_tokens": 67614,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 479
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

两个 tmux session 已启动。验证进程是否正常运行。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "4a5658b0-0f3a-4a66-9842-1bc85e99786f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MyYfDtYYSzKia18MiJkZic",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 479,
      "cache_read_input_tokens": 67614,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 479
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01LPVA8sD2GjxWFyQt3UQdjQ`</summary>

```json
{
  "server": "bjb1-18228",
  "command": "nvidia-smi --query-gpu=index,memory.used,utilization.gpu --format=csv,noheader",
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
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "f98242d2-35dc-4f04-80b0-1b20d3bcbacb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MyYfDtYYSzKia18MiJkZic",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 479,
      "cache_read_input_tokens": 67614,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 479
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

_source line 74 · 2026-05-24T07:15:27.777Z_

<details><summary>↩ Tool result · `toolu_01LPVA8sD2GjxWFyQt3UQdjQ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, 9884 MiB, 13 %\\n1, 3 MiB, 0 %\\n2, 3 MiB, 0 %\\n3, 9883 MiB, 12 %\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.56}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "400e536c-aea5-4714-b42e-00eac91f32f4",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"0, 9884 MiB, 13 %\\\\n1, 3 MiB, 0 %\\\\n2, 3 MiB, 0 %\\\\n3, 9883 MiB, 12 %\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.56}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"0, 9884 MiB, 13 %\\n1, 3 MiB, 0 %\\n2, 3 MiB, 0 %\\n3, 9883 MiB, 12 %\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.56}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 75_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01MkDyxZuWsWHRY8Faxz72F4`</summary>

```json
{
  "server": "bjb1-18228",
  "command": "tail -5 /root/acr-vla-conformal-refinement/logs/eval-supp-long-vla-only-s47-r2.log",
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
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "48618989-09d3-4d65-8afe-8329283cf31c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MyYfDtYYSzKia18MiJkZic",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 479,
      "cache_read_input_tokens": 67614,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 479
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

_source line 76 · 2026-05-24T07:15:28.590Z_

<details><summary>↩ Tool result · `toolu_01MkDyxZuWsWHRY8Faxz72F4`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"[eval] Loading SmolVLA from /root/autodl-tmp/models/smolvla_libero/...\\nLoading  /root/autodl-tmp/models/SmolVLM2-500M-Video-Instruct weights ...\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/489 [00:00<?, ?it/s]\\rLoading weights:  58%|█████▊    | 284/489 [00:00<00:00, 2830.74it/s]\\rLoading weights: 100%|██████████| 489/489 [00:00<00:00, 3351.55it/s]\\nReducing the number of VLM layers to 16 ...\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "a9e74113-5239-47cf-bfa1-17e388947d30",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"[eval] Loading SmolVLA from /root/autodl-tmp/models/smolvla_libero/...\\\\nLoading  /root/autodl-tmp/models/SmolVLM2-500M-Video-Instruct weights ...\\\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\\\n\\\\rLoading weights:   0%|          | 0/489 [00:00<?, ?it/s]\\\\rLoading weights:  58%|█████▊    | 284/489 [00:00<00:00, 2830.74it/s]\\\\rLoading weights: 100%|██████████| 489/489 [00:00<00:00, 3351.55it/s]\\\\nReducing the number of VLM layers to 16 ...\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"[eval] Loading SmolVLA from /root/autodl-tmp/models/smolvla_libero/...\\nLoading  /root/autodl-tmp/models/SmolVLM2-500M-Video-Instruct weights ...\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/489 [00:00<?, ?it/s]\\rLoading weights:  58%|█████▊    | 284/489 [00:00<00:00, 2830.74it/s]\\rLoading weights: 100%|██████████| 489/489 [00:00<00:00, 3351.55it/s]\\nReducing the number of VLM layers to 16 ...\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 77_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01GAzvotdkzB62aoGZ2ixnGg`</summary>

```json
{
  "server": "bjb1-18228",
  "command": "tail -5 /root/acr-vla-conformal-refinement/logs/eval-supp-goal-vla-only-s47.log",
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
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "71daafa1-a685-493f-b3c8-ae916706496e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MyYfDtYYSzKia18MiJkZic",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 479,
      "cache_read_input_tokens": 67614,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 479
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

_source line 78 · 2026-05-24T07:15:29.448Z_

<details><summary>↩ Tool result · `toolu_01GAzvotdkzB62aoGZ2ixnGg`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"[eval] max_steps set to 300 for benchmark goal\\n[eval] Loading SmolVLA from /root/autodl-tmp/models/smolvla_libero/...\\nLoading  /root/autodl-tmp/models/SmolVLM2-500M-Video-Instruct weights ...\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/489 [00:00<?, ?it/s]\\rLoading weights:  57%|█████▋    | 279/489 [00:00<00:00, 2762.34it/s]\\rLoading weights: 100%|██████████| 489/489 [00:00<00:00, 3285.18it/s]\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "1a985e96-a52b-46f6-a99c-67bd44d05a2c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"[eval] max_steps set to 300 for benchmark goal\\\\n[eval] Loading SmolVLA from /root/autodl-tmp/models/smolvla_libero/...\\\\nLoading  /root/autodl-tmp/models/SmolVLM2-500M-Video-Instruct weights ...\\\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\\\n\\\\rLoading weights:   0%|          | 0/489 [00:00<?, ?it/s]\\\\rLoading weights:  57%|█████▋    | 279/489 [00:00<00:00, 2762.34it/s]\\\\rLoading weights: 100%|██████████| 489/489 [00:00<00:00, 3285.18it/s]\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.37}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"[eval] max_steps set to 300 for benchmark goal\\n[eval] Loading SmolVLA from /root/autodl-tmp/models/smolvla_libero/...\\nLoading  /root/autodl-tmp/models/SmolVLM2-500M-Video-Instruct weights ...\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/489 [00:00<?, ?it/s]\\rLoading weights:  57%|█████▋    | 279/489 [00:00<00:00, 2762.34it/s]\\rLoading weights: 100%|██████████| 489/489 [00:00<00:00, 3285.18it/s]\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 79_

<details><summary>Logged reasoning block</summary>

```text
Both experiments are loading SmolVLA. GPU 1 and 2 show only 3 MiB used, which means models are still loading. Let me wait a moment and check again, then update the registry with RUNNING status.

Actually, the models are loading, they'll use GPU memory soon. Let me proceed to update the registry to RUNNING.

Let me also get the PIDs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "eb4a93c0-2aea-473c-bc74-2ef5ce5de72b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S39Lj3GwikuKS7zb3wTSyv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1211,
      "cache_read_input_tokens": 68093,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1211
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

_source line 80_

两个实验正在加载模型。获取 PID 并更新 registry 到 RUNNING。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "481de01c-e321-4832-b053-3f94cceea071",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S39Lj3GwikuKS7zb3wTSyv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1211,
      "cache_read_input_tokens": 68093,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1211
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

_source line 81_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Bu9CbWkARzHAmKMJ7s13pd`</summary>

```json
{
  "server": "bjb1-18228",
  "command": "ps aux --no-headers -o pid,args",
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
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "79ae8f3c-9bec-4d12-ba60-9d62e0bde78d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S39Lj3GwikuKS7zb3wTSyv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1211,
      "cache_read_input_tokens": 68093,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1211
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

_source line 82 · 2026-05-24T07:15:36.795Z_

<details><summary>↩ Tool result · `toolu_01Bu9CbWkARzHAmKMJ7s13pd`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"error: conflicting format options\\n\\nUsage:\\n ps [options]\\n\\n Try 'ps --help &lt;simple|list|output|threads|misc|all>'\\n  or 'ps --help &lt;s|l|o|t|m|a>'\\n for additional help text.\\n\\nFor more details see ps(1).\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.38}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "a949df02-89c5-4de7-ab96-b7dd35afbcd3",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"error: conflicting format options\\\\n\\\\nUsage:\\\\n ps [options]\\\\n\\\\n Try 'ps --help &lt;simple|list|output|threads|misc|all>'\\\\n  or 'ps --help &lt;s|l|o|t|m|a>'\\\\n for additional help text.\\\\n\\\\nFor more details see ps(1).\\\\n\\\", \\\"return_code\\\": 1}, \\\"error\\\": \\\"exit code 1\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.38}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"error: conflicting format options\\n\\nUsage:\\n ps [options]\\n\\n Try 'ps --help &lt;simple|list|output|threads|misc|all>'\\n  or 'ps --help &lt;s|l|o|t|m|a>'\\n for additional help text.\\n\\nFor more details see ps(1).\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.38}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 83_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_013g8SbUv7qHQ5F2WJBVLvA9`</summary>

```json
{
  "server": "bjb1-18228",
  "command": "ps aux",
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
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "dd14635c-c336-4b45-96ce-24334a59955e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D1VPjKJzjUNoebEBn3njS5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 406,
      "cache_read_input_tokens": 69304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 406
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

_source line 84 · 2026-05-24T07:15:42.651Z_

<details><summary>↩ Tool result · `toolu_013g8SbUv7qHQ5F2WJBVLvA9`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"USER        PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND\\nroot          1  0.0  0.0   4476  2096 ?        Ss   May13   0:02 bash /init/boot/boot.sh\\nroot        794  1.4  0.0 724128 20676 ?        Sl   May13 239:29 /bin/supervisord -c /init/supervisor/supervisor.ini\\nroot        808  0.0  0.0  15444  8264 ?        S    May13   0:54 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups\\nroot        809  0.0  0.0 4147492 77540 ?       Sl   May13   7:08 /root/miniconda3/bin/python /root/miniconda3/bin/tensorboard --host 0.0.0.0 --port 6007 --logdir /root/tf-logs\\nroot        814  0.0  0.0 191536 103404 ?       S    May13   0:02 /root/miniconda3/bin/python /root/miniconda3/bin/jupyter-lab --allow-root --config=/init/jupyter/jupyter_config.py\\nroot        817  0.2  0.0 5196664 99408 ?       Sl   May13  40:13 autopanel serve --work-dir=/root/autodl-tmp --cache-dir=/root/autodl-tmp\\nroot        818  0.0  0.0 3535912 18048 ?       Sl   May13   5:41 proxy -c /init/proxy/proxy-hot-backup.ini\\nroot        819  0.1  0.0 3609132 18528 ?       Sl   May13  19:28 proxy -c /init/proxy/proxy.ini\\nroot        925  0.0  0.0 17524960 8916 ?       Sl   May13   6:02 /root/miniconda3/lib/python3.12/site-packages/tensorboard_data_server/bin/server --logdir=/root/tf-logs --reload=5 --samples-per-plugin= --port=0 --port-file=/tmp/tensorboard_data_server_vbt2aa5n/port --die-after-stdin --error-file=/tmp/tensorboard_data_server_vbt2aa5n/startup_error\\nroot     113455  0.0  0.0   4364  1648 ?        S    May23   0:00 bash -c cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 nohup python -u src/train_crm.py --precompute --model pi05 --benchmark object --K 10 --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/ > /root/autodl-tmp/logs/precompute_pi05_object_2048.log 2>&1 & echo \\\"PID=$!\\\"\\nroot     113456  133  0.9 63823256 10219624 ?   Rl   May23 2793:03 python -u src/train_crm.py --precompute --model pi05 --benchmark object --K 10 --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/\\nroot     114507  132  1.6 70675684 17065520 ?   Rl   May23 2765:32 python -u src/train_crm.py --precompute --model pi05 --benchmark long --K 10 --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/\\nroot     275990  0.0  0.0  16692 10864 ?        Ss   14:08   0:00 sshd: root@notty\\nroot     278638  0.0  0.0  16692 10628 ?        Ss   15:10   0:00 sshd: root@notty\\nroot     278843  0.0  0.0   6084  3832 ?        Ss   15:15   0:00 tmux new-session -d -s long-vla-s47-r2 CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark long --mode vla_only --seed 47 --n_rollouts 20 --K 1 2>&1 | tee logs/eval-supp-long-vla-only-s47-r2.log\\nroot     278844  0.0  0.0   4364  3088 pts/0    Ss+  15:15   0:00 bash -c CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark long --mode vla_only --seed 47 --n_rollouts 20 --K 1 2>&1 | tee logs/eval-supp-long-vla-only-s47-r2.log\\nroot     278846  641  0.8 72725276 9443764 pts/0 Sl+ 15:15   3:44 python -u src/evaluate.py --benchmark long --mode vla_only --seed 47 --n_rollouts 20 --K 1\\nroot     278847  0.0  0.0   2796  1016 pts/0    S+   15:15   0:00 tee logs/eval-supp-long-vla-only-s47-r2.log\\nroot     279115  0.0  0.0   4364  3064 pts/1    Ss+  15:15   0:00 bash -c CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark goal --mode vla_only --seed 47 --n_rollouts 20 --K 1 2>&1 | tee logs/eval-supp-goal-vla-only-s47.log\\nroot     279117  740  0.5 66758812 6309212 pts/1 Rl+ 15:15   3:34 python -u src/evaluate.py --benchmark goal --mode vla_only --seed 47 --n_rollouts 20 --K 1\\nroot     279118  0.0  0.0   2796  1004 pts/1    S+   15:15   0:00 tee logs/eval-supp-goal-vla-only-s47.log\\nroot     281152  0.0  0.0   7064  1580 ?        Rs   15:15   0:00 ps aux\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "e8f46e88-375b-409a-b27c-d5720ed67e1b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"USER        PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND\\\\nroot          1  0.0  0.0   4476  2096 ?        Ss   May13   0:02 bash /init/boot/boot.sh\\\\nroot        794  1.4  0.0 724128 20676 ?        Sl   May13 239:29 /bin/supervisord -c /init/supervisor/supervisor.ini\\\\nroot        808  0.0  0.0  15444  8264 ?        S    May13   0:54 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups\\\\nroot        809  0.0  0.0 4147492 77540 ?       Sl   May13   7:08 /root/miniconda3/bin/python /root/miniconda3/bin/tensorboard --host 0.0.0.0 --port 6007 --logdir /root/tf-logs\\\\nroot        814  0.0  0.0 191536 103404 ?       S    May13   0:02 /root/miniconda3/bin/python /root/miniconda3/bin/jupyter-lab --allow-root --config=/init/jupyter/jupyter_config.py\\\\nroot        817  0.2  0.0 5196664 99408 ?       Sl   May13  40:13 autopanel serve --work-dir=/root/autodl-tmp --cache-dir=/root/autodl-tmp\\\\nroot        818  0.0  0.0 3535912 18048 ?       Sl   May13   5:41 proxy -c /init/proxy/proxy-hot-backup.ini\\\\nroot        819  0.1  0.0 3609132 18528 ?       Sl   May13  19:28 proxy -c /init/proxy/proxy.ini\\\\nroot        925  0.0  0.0 17524960 8916 ?       Sl   May13   6:02 /root/miniconda3/lib/python3.12/site-packages/tensorboard_data_server/bin/server --logdir=/root/tf-logs --reload=5 --samples-per-plugin= --port=0 --port-file=/tmp/tensorboard_data_server_vbt2aa5n/port --die-after-stdin --error-file=/tmp/tensorboard_data_server_vbt2aa5n/startup_error\\\\nroot     113455  0.0  0.0   4364  1648 ?        S    May23   0:00 bash -c cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 nohup python -u src/train_crm.py --precompute --model pi05 --benchmark object --K 10 --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/ > /root/autodl-tmp/logs/precompute_pi05_object_2048.log 2>&1 & echo \\\\\\\"PID=$!\\\\\\\"\\\\nroot     113456  133  0.9 63823256 10219624 ?   Rl   May23 2793:03 python -u src/train_crm.py --precompute --model pi05 --benchmark object --K 10 --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/\\\\nroot     114507  132  1.6 70675684 17065520 ?   Rl   May23 2765:32 python -u src/train_crm.py --precompute --model pi05 --benchmark long --K 10 --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/\\\\nroot     275990  0.0  0.0  16692 10864 ?        Ss   14:08   0:00 sshd: root@notty\\\\nroot     278638  0.0  0.0  16692 10628 ?        Ss   15:10   0:00 sshd: root@notty\\\\nroot     278843  0.0  0.0   6084  3832 ?        Ss   15:15   0:00 tmux new-session -d -s long-vla-s47-r2 CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark long --mode vla_only --seed 47 --n_rollouts 20 --K 1 2>&1 | tee logs/eval-supp-long-vla-only-s47-r2.log\\\\nroot     278844  0.0  0.0   4364  3088 pts/0    Ss+  15:15   0:00 bash -c CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark long --mode vla_only --seed 47 --n_rollouts 20 --K 1 2>&1 | tee logs/eval-supp-long-vla-only-s47-r2.log\\\\nroot     278846  641  0.8 72725276 9443764 pts/0 Sl+ 15:15   3:44 python -u src/evaluate.py --benchmark long --mode vla_only --seed 47 --n_rollouts 20 --K 1\\\\nroot     278847  0.0  0.0   2796  1016 pts/0    S+   15:15   0:00 tee logs/eval-supp-long-vla-only-s47-r2.log\\\\nroot     279115  0.0  0.0   4364  3064 pts/1    Ss+  15:15   0:00 bash -c CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark goal --mode vla_only --seed 47 --n_rollouts 20 --K 1 2>&1 | tee logs/eval-supp-goal-vla-only-s47.log\\\\nroot     279117  740  0.5 66758812 6309212 pts/1 Rl+ 15:15   3:34 python -u src/evaluate.py --benchmark goal --mode vla_only --seed 47 --n_rollouts 20 --K 1\\\\nroot     279118  0.0  0.0   2796  1004 pts/1    S+   15:15   0:00 tee logs/eval-supp-goal-vla-only-s47.log\\\\nroot     281152  0.0  0.0   7064  1580 ?        Rs   15:15   0:00 ps aux\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.38}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"USER        PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND\\nroot          1  0.0  0.0   4476  2096 ?        Ss   May13   0:02 bash /init/boot/boot.sh\\nroot        794  1.4  0.0 724128 20676 ?        Sl   May13 239:29 /bin/supervisord -c /init/supervisor/supervisor.ini\\nroot        808  0.0  0.0  15444  8264 ?        S    May13   0:54 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups\\nroot        809  0.0  0.0 4147492 77540 ?       Sl   May13   7:08 /root/miniconda3/bin/python /root/miniconda3/bin/tensorboard --host 0.0.0.0 --port 6007 --logdir /root/tf-logs\\nroot        814  0.0  0.0 191536 103404 ?       S    May13   0:02 /root/miniconda3/bin/python /root/miniconda3/bin/jupyter-lab --allow-root --config=/init/jupyter/jupyter_config.py\\nroot        817  0.2  0.0 5196664 99408 ?       Sl   May13  40:13 autopanel serve --work-dir=/root/autodl-tmp --cache-dir=/root/autodl-tmp\\nroot        818  0.0  0.0 3535912 18048 ?       Sl   May13   5:41 proxy -c /init/proxy/proxy-hot-backup.ini\\nroot        819  0.1  0.0 3609132 18528 ?       Sl   May13  19:28 proxy -c /init/proxy/proxy.ini\\nroot        925  0.0  0.0 17524960 8916 ?       Sl   May13   6:02 /root/miniconda3/lib/python3.12/site-packages/tensorboard_data_server/bin/server --logdir=/root/tf-logs --reload=5 --samples-per-plugin= --port=0 --port-file=/tmp/tensorboard_data_server_vbt2aa5n/port --die-after-stdin --error-file=/tmp/tensorboard_data_server_vbt2aa5n/startup_error\\nroot     113455  0.0  0.0   4364  1648 ?        S    May23   0:00 bash -c cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 nohup python -u src/train_crm.py --precompute --model pi05 --benchmark object --K 10 --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/ > /root/autodl-tmp/logs/precompute_pi05_object_2048.log 2>&1 & echo \\\"PID=$!\\\"\\nroot     113456  133  0.9 63823256 10219624 ?   Rl   May23 2793:03 python -u src/train_crm.py --precompute --model pi05 --benchmark object --K 10 --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/\\nroot     114507  132  1.6 70675684 17065520 ?   Rl   May23 2765:32 python -u src/train_crm.py --precompute --model pi05 --benchmark long --K 10 --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/\\nroot     275990  0.0  0.0  16692 10864 ?        Ss   14:08   0:00 sshd: root@notty\\nroot     278638  0.0  0.0  16692 10628 ?        Ss   15:10   0:00 sshd: root@notty\\nroot     278843  0.0  0.0   6084  3832 ?        Ss   15:15   0:00 tmux new-session -d -s long-vla-s47-r2 CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark long --mode vla_only --seed 47 --n_rollouts 20 --K 1 2>&1 | tee logs/eval-supp-long-vla-only-s47-r2.log\\nroot     278844  0.0  0.0   4364  3088 pts/0    Ss+  15:15   0:00 bash -c CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark long --mode vla_only --seed 47 --n_rollouts 20 --K 1 2>&1 | tee logs/eval-supp-long-vla-only-s47-r2.log\\nroot     278846  641  0.8 72725276 9443764 pts/0 Sl+ 15:15   3:44 python -u src/evaluate.py --benchmark long --mode vla_only --seed 47 --n_rollouts 20 --K 1\\nroot     278847  0.0  0.0   2796  1016 pts/0    S+   15:15   0:00 tee logs/eval-supp-long-vla-only-s47-r2.log\\nroot     279115  0.0  0.0   4364  3064 pts/1    Ss+  15:15   0:00 bash -c CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark goal --mode vla_only --seed 47 --n_rollouts 20 --K 1 2>&1 | tee logs/eval-supp-goal-vla-only-s47.log\\nroot     279117  740  0.5 66758812 6309212 pts/1 Rl+ 15:15   3:34 python -u src/evaluate.py --benchmark goal --mode vla_only --seed 47 --n_rollouts 20 --K 1\\nroot     279118  0.0  0.0   2796  1004 pts/1    S+   15:15   0:00 tee logs/eval-supp-goal-vla-only-s47.log\\nroot     281152  0.0  0.0   7064  1580 ?        Rs   15:15   0:00 ps aux\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 85_

<details><summary>Logged reasoning block</summary>

```text
Both experiments are running:
- PID 278846: `python -u src/evaluate.py --benchmark long --mode vla_only --seed 47 --n_rollouts 20 --K 1` on GPU 1
- PID 279117: `python -u src/evaluate.py --benchmark goal --mode vla_only --seed 47 --n_rollouts 20 --K 1` on GPU 2

Now update registry to RUNNING for both.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "2c9468bb-f79c-4e0c-bf28-aa52bcf9165f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BYRHGDjqooaArLGPmX3VD1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1852,
      "cache_read_input_tokens": 69710,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1852
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

_source line 86_

两个进程已确认运行：PID 278846 (Long, GPU 1) 和 PID 279117 (Goal, GPU 2)。更新 registry 到 RUNNING。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "c5921029-4d18-4ef1-a3e8-30d6519e4d60",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BYRHGDjqooaArLGPmX3VD1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1852,
      "cache_read_input_tokens": 69710,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1852
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

_source line 87_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01C2QQTou1utVzyNm7uXR8St`</summary>

```json
{
  "exp_id": "eval-supp-long-vla-only-s47-r2",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": {
    "command": "CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark long --mode vla_only --seed 47 --n_rollouts 20 --K 1",
    "server": "bjb1-18228",
    "gpu": [
      "cuda:1"
    ],
    "pid": 278846,
    "tmux_session": "long-vla-s47-r2",
    "log_path": "logs/eval-supp-long-vla-only-s47-r2.log",
    "data_path": "LIBERO-Long",
    "data_count": 200,
    "model_name": "SmolVLA",
    "seed": 47,
    "eval_data": "LIBERO-Long",
    "checkpoint_source": "n/a-baseline",
    "checkpoint_path": "n/a-eval-only"
  }
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "bc65aa83-80e0-4a93-9d70-b16010ab00f1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BYRHGDjqooaArLGPmX3VD1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1852,
      "cache_read_input_tokens": 69710,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1852
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

_source line 88_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01Xz24sq8vh37AsJheuAgi3M`</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-s47",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": {
    "command": "CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark goal --mode vla_only --seed 47 --n_rollouts 20 --K 1",
    "server": "bjb1-18228",
    "gpu": [
      "cuda:2"
    ],
    "pid": 279117,
    "tmux_session": "goal-vla-s47",
    "log_path": "logs/eval-supp-goal-vla-only-s47.log",
    "data_path": "LIBERO-Goal",
    "data_count": 200,
    "model_name": "SmolVLA",
    "seed": 47,
    "eval_data": "LIBERO-Goal",
    "checkpoint_source": "n/a-baseline",
    "checkpoint_path": "n/a-eval-only"
  }
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "f7da9147-7f5a-4a3d-bd8a-1e2e66624260",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BYRHGDjqooaArLGPmX3VD1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1852,
      "cache_read_input_tokens": 69710,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1852
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

_source line 89 · 2026-05-24T07:15:59.553Z_

<details><summary>↩ Tool result · `toolu_01C2QQTou1utVzyNm7uXR8St`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 6.491}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "e0fdef72-884f-490f-a09e-49fff2e949ce",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 6.491}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 6.491}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-24T07:16:01.876Z_

<details><summary>↩ Tool result · `toolu_01Xz24sq8vh37AsJheuAgi3M`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 2.3073}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "a1e2eef5-da60-4c1c-a93c-3664db8ef66a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.3073}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 2.3073}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 91_

<details><summary>Logged reasoning block</summary>

```text
Need to transition through QUEUED first: PREPARING → QUEUED → RUNNING.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "c705234e-f263-45f6-a077-c543c02fd1c6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WAW46ZGMYrVjJVZiRr8x6p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1170,
      "cache_read_input_tokens": 71562,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1170
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

_source line 92_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01H6cDH55hZFhBvsnb6QsMGL`</summary>

```json
{
  "exp_id": "eval-supp-long-vla-only-s47-r2",
  "field": "status",
  "value": "QUEUED",
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
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "e2430c6a-e90a-41be-8a25-d553d8272966",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WAW46ZGMYrVjJVZiRr8x6p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1170,
      "cache_read_input_tokens": 71562,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1170
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

_source line 93_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01FuBD3rPG9CfnEimWAeYQb3`</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-s47",
  "field": "status",
  "value": "QUEUED",
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
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "3c4622e9-8976-4da6-a4b5-d1a1f2e310d2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WAW46ZGMYrVjJVZiRr8x6p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1170,
      "cache_read_input_tokens": 71562,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1170
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

_source line 94 · 2026-05-24T07:16:40.172Z_

<details><summary>↩ Tool result · `toolu_01H6cDH55hZFhBvsnb6QsMGL`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-long-vla-only-s47-r2\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:14:04.522Z\", \"updated_at\": \"2026-05-24T07:16:32.114Z\", \"hypothesis\": \"Long s47 VLA-only (K=1) baseline to complete the Long s47 seed extension set. The existing eval-supp-long-vla-only-s47 is actually k2mean (K=2 mean), so this fills the true VLA-only gap.\", \"parent\": \"eval-supp-long-vla-only-s46\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 17.5214}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "0ae4bc06-3fe3-4abe-8463-4bb6a8610005",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-supp-long-vla-only-s47-r2\\\", \\\"experiment\\\": {\\\"status\\\": \\\"QUEUED\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T07:14:04.522Z\\\", \\\"updated_at\\\": \\\"2026-05-24T07:16:32.114Z\\\", \\\"hypothesis\\\": \\\"Long s47 VLA-only (K=1) baseline to complete the Long s47 seed extension set. The existing eval-supp-long-vla-only-s47 is actually k2mean (K=2 mean), so this fills the true VLA-only gap.\\\", \\\"parent\\\": \\\"eval-supp-long-vla-only-s46\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 17.5214}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-long-vla-only-s47-r2\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:14:04.522Z\", \"updated_at\": \"2026-05-24T07:16:32.114Z\", \"hypothesis\": \"Long s47 VLA-only (K=1) baseline to complete the Long s47 seed extension set. The existing eval-supp-long-vla-only-s47 is actually k2mean (K=2 mean), so this fills the true VLA-only gap.\", \"parent\": \"eval-supp-long-vla-only-s46\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 17.5214}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 95 · 2026-05-24T07:16:52.922Z_

<details><summary>↩ Tool result · `toolu_01FuBD3rPG9CfnEimWAeYQb3`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-s47\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:14:14.567Z\", \"updated_at\": \"2026-05-24T07:16:44.441Z\", \"hypothesis\": \"Goal s47 VLA-only (K=1) baseline to extend Goal seed coverage beyond s42-s46 for supplementary variance analysis.\", \"parent\": \"eval-supp-goal-vla-only-s46\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 12.7277}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "df44a530-c30c-473d-8efd-1076d06d34a5",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-supp-goal-vla-only-s47\\\", \\\"experiment\\\": {\\\"status\\\": \\\"QUEUED\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T07:14:14.567Z\\\", \\\"updated_at\\\": \\\"2026-05-24T07:16:44.441Z\\\", \\\"hypothesis\\\": \\\"Goal s47 VLA-only (K=1) baseline to extend Goal seed coverage beyond s42-s46 for supplementary variance analysis.\\\", \\\"parent\\\": \\\"eval-supp-goal-vla-only-s46\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 12.7277}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-s47\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:14:14.567Z\", \"updated_at\": \"2026-05-24T07:16:44.441Z\", \"hypothesis\": \"Goal s47 VLA-only (K=1) baseline to extend Goal seed coverage beyond s42-s46 for supplementary variance analysis.\", \"parent\": \"eval-supp-goal-vla-only-s46\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 12.7277}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 96_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01NY7S47XUFUVNp7M1a4tBdY`</summary>

```json
{
  "exp_id": "eval-supp-long-vla-only-s47-r2",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": {
    "command": "CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark long --mode vla_only --seed 47 --n_rollouts 20 --K 1",
    "server": "bjb1-18228",
    "gpu": [
      "cuda:1"
    ],
    "pid": 278846,
    "tmux_session": "long-vla-s47-r2",
    "log_path": "logs/eval-supp-long-vla-only-s47-r2.log",
    "data_path": "LIBERO-Long",
    "data_count": 200,
    "model_name": "SmolVLA",
    "seed": 47,
    "eval_data": "LIBERO-Long",
    "checkpoint_source": "n/a-baseline",
    "checkpoint_path": "n/a-eval-only"
  }
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "cf5f7363-6221-490e-8143-e3a59d054179",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XDFfv9P8PckuLekTkzb4J1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 805,
      "cache_read_input_tokens": 72732,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 805
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

### Tool call

_source line 97_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01GVy5e3NarXRk6tZp2nKqti`</summary>

```json
{
  "exp_id": "eval-supp-goal-vla-only-s47",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": {
    "command": "CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark goal --mode vla_only --seed 47 --n_rollouts 20 --K 1",
    "server": "bjb1-18228",
    "gpu": [
      "cuda:2"
    ],
    "pid": 279117,
    "tmux_session": "goal-vla-s47",
    "log_path": "logs/eval-supp-goal-vla-only-s47.log",
    "data_path": "LIBERO-Goal",
    "data_count": 200,
    "model_name": "SmolVLA",
    "seed": 47,
    "eval_data": "LIBERO-Goal",
    "checkpoint_source": "n/a-baseline",
    "checkpoint_path": "n/a-eval-only"
  }
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "e3c2cb10-c142-4834-8fc0-55bdb8f5c77d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XDFfv9P8PckuLekTkzb4J1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 805,
      "cache_read_input_tokens": 72732,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 805
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

_source line 98 · 2026-05-24T07:17:12.012Z_

<details><summary>↩ Tool result · `toolu_01NY7S47XUFUVNp7M1a4tBdY`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-long-vla-only-s47-r2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:14:04.522Z\", \"updated_at\": \"2026-05-24T07:17:06.584Z\", \"hypothesis\": \"Long s47 VLA-only (K=1) baseline to complete the Long s47 seed extension set. The existing eval-supp-long-vla-only-s47 is actually k2mean (K=2 mean), so this fills the true VLA-only gap.\", \"parent\": \"eval-supp-long-vla-only-s46\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark long --mode vla_only --seed 47 --n_rollouts 20 --K 1\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": 278846, \"tmux_session\": \"long-vla-s47-r2\", \"log_path\": \"logs/eval-supp-long-vla-only-s47-r2.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"n/a-baseline\", \"checkpoint_path\": \"n/a-eval-only\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 11.824}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "2ec5215f-1448-43f6-994d-fe73147db977",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-supp-long-vla-only-s47-r2\\\", \\\"experiment\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T07:14:04.522Z\\\", \\\"updated_at\\\": \\\"2026-05-24T07:17:06.584Z\\\", \\\"hypothesis\\\": \\\"Long s47 VLA-only (K=1) baseline to complete the Long s47 seed extension set. The existing eval-supp-long-vla-only-s47 is actually k2mean (K=2 mean), so this fills the true VLA-only gap.\\\", \\\"parent\\\": \\\"eval-supp-long-vla-only-s46\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark long --mode vla_only --seed 47 --n_rollouts 20 --K 1\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": 278846, \\\"tmux_session\\\": \\\"long-vla-s47-r2\\\", \\\"log_path\\\": \\\"logs/eval-supp-long-vla-only-s47-r2.log\\\", \\\"data_path\\\": \\\"LIBERO-Long\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 47, \\\"eval_data\\\": \\\"LIBERO-Long\\\", \\\"checkpoint_source\\\": \\\"n/a-baseline\\\", \\\"checkpoint_path\\\": \\\"n/a-eval-only\\\"}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 11.824}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-long-vla-only-s47-r2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:14:04.522Z\", \"updated_at\": \"2026-05-24T07:17:06.584Z\", \"hypothesis\": \"Long s47 VLA-only (K=1) baseline to complete the Long s47 seed extension set. The existing eval-supp-long-vla-only-s47 is actually k2mean (K=2 mean), so this fills the true VLA-only gap.\", \"parent\": \"eval-supp-long-vla-only-s46\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark long --mode vla_only --seed 47 --n_rollouts 20 --K 1\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": 278846, \"tmux_session\": \"long-vla-s47-r2\", \"log_path\": \"logs/eval-supp-long-vla-only-s47-r2.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"n/a-baseline\", \"checkpoint_path\": \"n/a-eval-only\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 11.824}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 99 · 2026-05-24T07:17:20.023Z_

<details><summary>↩ Tool result · `toolu_01GVy5e3NarXRk6tZp2nKqti`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-s47\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:14:14.567Z\", \"updated_at\": \"2026-05-24T07:17:13.996Z\", \"hypothesis\": \"Goal s47 VLA-only (K=1) baseline to extend Goal seed coverage beyond s42-s46 for supplementary variance analysis.\", \"parent\": \"eval-supp-goal-vla-only-s46\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark goal --mode vla_only --seed 47 --n_rollouts 20 --K 1\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": 279117, \"tmux_session\": \"goal-vla-s47\", \"log_path\": \"logs/eval-supp-goal-vla-only-s47.log\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Goal\", \"checkpoint_source\": \"n/a-baseline\", \"checkpoint_path\": \"n/a-eval-only\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.9967}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "eb19d2cc-5e5e-4dbb-a5af-8c05f6e41835",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval-supp-goal-vla-only-s47\\\", \\\"experiment\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T07:14:14.567Z\\\", \\\"updated_at\\\": \\\"2026-05-24T07:17:13.996Z\\\", \\\"hypothesis\\\": \\\"Goal s47 VLA-only (K=1) baseline to extend Goal seed coverage beyond s42-s46 for supplementary variance analysis.\\\", \\\"parent\\\": \\\"eval-supp-goal-vla-only-s46\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark goal --mode vla_only --seed 47 --n_rollouts 20 --K 1\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"pid\\\": 279117, \\\"tmux_session\\\": \\\"goal-vla-s47\\\", \\\"log_path\\\": \\\"logs/eval-supp-goal-vla-only-s47.log\\\", \\\"data_path\\\": \\\"LIBERO-Goal\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 47, \\\"eval_data\\\": \\\"LIBERO-Goal\\\", \\\"checkpoint_source\\\": \\\"n/a-baseline\\\", \\\"checkpoint_path\\\": \\\"n/a-eval-only\\\"}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 7.9967}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-goal-vla-only-s47\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:14:14.567Z\", \"updated_at\": \"2026-05-24T07:17:13.996Z\", \"hypothesis\": \"Goal s47 VLA-only (K=1) baseline to extend Goal seed coverage beyond s42-s46 for supplementary variance analysis.\", \"parent\": \"eval-supp-goal-vla-only-s46\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark goal --mode vla_only --seed 47 --n_rollouts 20 --K 1\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": 279117, \"tmux_session\": \"goal-vla-s47\", \"log_path\": \"logs/eval-supp-goal-vla-only-s47.log\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Goal\", \"checkpoint_source\": \"n/a-baseline\", \"checkpoint_path\": \"n/a-eval-only\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.9967}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 100_

部署完成。bjb1-18228 GPU 分配：

| GPU | 实验 | 状态 |
|-----|------|------|
| 0 | precompute-pi05-object-2048-r2 | 不碰 |
| 1 | **eval-supp-long-vla-only-s47-r2** (PID 278846) | RUNNING |
| 2 | **eval-supp-goal-vla-only-s47** (PID 279117) | RUNNING |
| 3 | precompute-pi05-long-2048-r2 | 不碰 |

**选择理由：**
- Goal/Object s42-s46 五种方法全部 DONE，无缺口
- Long s47 四种方法在跑（crm/reconvla/adapt/k2mean），但现有 `eval-supp-long-vla-only-s47` 实际跑的是 k2mean (K=2 mean)，真正的 VLA-only (K=1) 缺失 → GPU 1 补上
- Goal s47 尚无任何 seed，VLA-only 不需要 CRM checkpoint → GPU 2 开跑

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "uuid": "3e50b899-9c00-4bc9-8058-c52836e7c4ef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014dRVDNA6ZgTFr9CHUNZchG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1632,
      "cache_read_input_tokens": 73537,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1632
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

_source line 101_

部署完成。bjb1-18228 GPU 分配：

| GPU | 实验 | 状态 |
|-----|------|------|
| 0 | precompute-pi05-object-2048-r2 | 不碰 |
| 1 | **eval-supp-long-vla-only-s47-r2** (PID 278846) | RUNNING |
| 2 | **eval-supp-goal-vla-only-s47** (PID 279117) | RUNNING |
| 3 | precompute-pi05-long-2048-r2 | 不碰 |

**选择理由：**
- Goal/Object s42-s46 五种方法全部 DONE，无缺口
- Long s47 四种方法在跑（crm/reconvla/adapt/k2mean），但现有 `eval-supp-long-vla-only-s47` 实际跑的是 k2mean (K=2 mean)，真正的 VLA-only (K=1) 缺失 → GPU 1 补上
- Goal s47 尚无任何 seed，VLA-only 不需要 CRM checkpoint → GPU 2 开跑

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 489079,
  "duration_api_ms": 353113,
  "num_turns": 36,
  "stop_reason": "end_turn",
  "session_id": "b9aee3ed-8d14-48d4-b3e0-dcc629fa78de",
  "total_cost_usd": 1.4108975,
  "usage": {
    "input_tokens": 26,
    "cache_creation_input_tokens": 63328,
    "cache_read_input_tokens": 1153035,
    "output_tokens": 17483,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 63328,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 325,
        "cache_read_input_tokens": 73537,
        "cache_creation_input_tokens": 1632,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1632
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1280,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0013750000000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 26,
      "outputTokens": 17483,
      "cacheReadInputTokens": 1153035,
      "cacheCreationInputTokens": 63328,
      "webSearchRequests": 0,
      "costUSD": 1.4095224999999998,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "4069be97-7695-457b-8469-0c56f4b4c44b"
}
```

</details>

---
