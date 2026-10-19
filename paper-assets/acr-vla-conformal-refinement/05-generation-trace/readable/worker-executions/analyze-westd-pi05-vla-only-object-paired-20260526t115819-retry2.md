# analyze westd pi05 vla only object paired 20260526T115819 retry2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 53
- **Recorded user turns:** 0
- **Tool calls:** 20
- **Original source:** `logs/workers/worker_analyze_westd-pi05-vla-only-object-paired_20260526T115819_retry2.log`
- **Structured JSON:** [`954ff8de098dd5f44034.json`](../../sessions/95/954ff8de098dd5f44034.json)

## Before a recorded user message

53 recorded events

### System

_source line 1_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement",
  "session_id": "eb7c021e-380a-410b-a199-64af6b82580d",
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
    "mcp__agent-ml-research__compare_wandb_runs",
    "mcp__agent-ml-research__detect_image",
    "mcp__agent-ml-research__fetch_wandb_metrics",
    "mcp__agent-ml-research__fetch_wandb_run_history",
    "mcp__agent-ml-research__get_best_wandb_run",
    "mcp__agent-ml-research__kill_job",
    "mcp__agent-ml-research__list_wandb_runs",
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
  "uuid": "2bbac56e-7cc8-4e96-9e8a-f4542746fc64",
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
    "status": "allowed_warning",
    "resetsAt": 1780063200,
    "rateLimitType": "seven_day",
    "utilization": 0.9,
    "isUsingOverage": false,
    "surpassedThreshold": 0.75
  },
  "uuid": "6d0b6b59-6fef-44f9-8bdb-1eddf72cb6b4",
  "session_id": "eb7c021e-380a-410b-a199-64af6b82580d"
}
```

---

### Assistant

_source line 3_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the 3 JSON result files from westd-49937 server, and also check the registry for these experiments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eb7c021e-380a-410b-a199-64af6b82580d",
  "uuid": "ee93ec20-7a14-4fba-8795-a062cad9d908",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GjHPvvgTxf7kNCG5bevZcj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11725,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11725
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

_source line 4_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_017VTHmXBrEjkM6zx1rnwP3u`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__list_wandb_runs",
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
  "session_id": "eb7c021e-380a-410b-a199-64af6b82580d",
  "uuid": "ac7ece24-d3e1-456f-ad7b-904a4ae3da94",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GjHPvvgTxf7kNCG5bevZcj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11725,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11725
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

_source line 5 · 2026-05-26T12:05:16.422Z_

<details><summary>↩ Tool result · `toolu_017VTHmXBrEjkM6zx1rnwP3u`</summary>

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
  "tool_name": "mcp__agent-ml-research__read_registry"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__update_registry"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__list_wandb_runs"
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
  "session_id": "eb7c021e-380a-410b-a199-64af6b82580d",
  "uuid": "eab24d72-6bd0-4302-9e92-46da8e3e95a1",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__update_registry",
      "mcp__agent-ml-research__list_wandb_runs"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__list_wandb_runs",
    "total_deferred_tools": 31
  }
}
```

</details>

---

### Assistant

_source line 6_

Reading the 3 JSON result files from westd-49937 and checking the registry in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eb7c021e-380a-410b-a199-64af6b82580d",
  "uuid": "62545be4-f762-4376-8a97-bf3267b71900",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HXHuw5NnnFsJJ5rYW4B8kE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1652,
      "cache_read_input_tokens": 23566,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1652
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

_source line 7_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_014Q93wLSd3nVPQf1aTnCMh8`</summary>

```json
{
  "server": "westd-49937",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed42_westd.json",
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
  "session_id": "eb7c021e-380a-410b-a199-64af6b82580d",
  "uuid": "0f3e79a4-4f14-4eb1-a56a-fa02393fe4dd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HXHuw5NnnFsJJ5rYW4B8kE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1652,
      "cache_read_input_tokens": 23566,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1652
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_013ew3p5fox8qGVngEzZDnZB`</summary>

```json
{
  "server": "westd-49937",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed43_westd.json",
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
  "session_id": "eb7c021e-380a-410b-a199-64af6b82580d",
  "uuid": "349e686f-518d-4265-a47a-76da7adac5c6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HXHuw5NnnFsJJ5rYW4B8kE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1652,
      "cache_read_input_tokens": 23566,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1652
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

_source line 9 · 2026-05-26T12:05:23.405Z_

<details><summary>↩ Tool result · `toolu_014Q93wLSd3nVPQf1aTnCMh8`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.995,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.23}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eb7c021e-380a-410b-a199-64af6b82580d",
  "uuid": "19107703-fe71-4f2e-9093-a6876c524b24",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"mode\\\\\\\": \\\\\\\"vla_only\\\\\\\",\\\\n  \\\\\\\"baseline_mode\\\\\\\": \\\\\\\"single\\\\\\\",\\\\n  \\\\\\\"benchmark\\\\\\\": \\\\\\\"object\\\\\\\",\\\\n  \\\\\\\"n_rollouts\\\\\\\": 20,\\\\n  \\\\\\\"overall_success_rate\\\\\\\": 0.995,\\\\n  \\\\\\\"per_task\\\\\\\": {\\\\n    \\\\\\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.95,\\\\n      \\\\\\\"successes\\\\\\\": 19,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_butter_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_milk_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.23}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.995,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.23}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-26T12:05:23.917Z_

<details><summary>↩ Tool result · `toolu_013ew3p5fox8qGVngEzZDnZB`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 1.0,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.49}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eb7c021e-380a-410b-a199-64af6b82580d",
  "uuid": "e9268ca7-a4de-4398-9c0b-3e6fb2c15b37",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"mode\\\\\\\": \\\\\\\"vla_only\\\\\\\",\\\\n  \\\\\\\"baseline_mode\\\\\\\": \\\\\\\"single\\\\\\\",\\\\n  \\\\\\\"benchmark\\\\\\\": \\\\\\\"object\\\\\\\",\\\\n  \\\\\\\"n_rollouts\\\\\\\": 20,\\\\n  \\\\\\\"overall_success_rate\\\\\\\": 1.0,\\\\n  \\\\\\\"per_task\\\\\\\": {\\\\n    \\\\\\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_butter_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_milk_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.49}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 1.0,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.49}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01ALyvKhYg3eqSt8DaMLWaEA`</summary>

```json
{
  "server": "westd-49937",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed44_westd.json",
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
  "session_id": "eb7c021e-380a-410b-a199-64af6b82580d",
  "uuid": "7b2c5859-0b6f-4fe1-bec2-e41ca0c3d3c3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HXHuw5NnnFsJJ5rYW4B8kE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1652,
      "cache_read_input_tokens": 23566,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1652
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

_source line 12 · 2026-05-26T12:05:24.739Z_

<details><summary>↩ Tool result · `toolu_01ALyvKhYg3eqSt8DaMLWaEA`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.995,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.49}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eb7c021e-380a-410b-a199-64af6b82580d",
  "uuid": "e184661a-5df8-4746-ae03-06cd17fe497c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"mode\\\\\\\": \\\\\\\"vla_only\\\\\\\",\\\\n  \\\\\\\"baseline_mode\\\\\\\": \\\\\\\"single\\\\\\\",\\\\n  \\\\\\\"benchmark\\\\\\\": \\\\\\\"object\\\\\\\",\\\\n  \\\\\\\"n_rollouts\\\\\\\": 20,\\\\n  \\\\\\\"overall_success_rate\\\\\\\": 0.995,\\\\n  \\\\\\\"per_task\\\\\\\": {\\\\n    \\\\\\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.95,\\\\n      \\\\\\\"successes\\\\\\\": 19,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_butter_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_milk_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.49}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.995,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.49}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_014asx6NE6Ypoun6JC4XHhKo`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": {
    "exp_id": "westd-pi05-vla-only-object-s42-paired"
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
  "session_id": "eb7c021e-380a-410b-a199-64af6b82580d",
  "uuid": "bebac20c-b8eb-4a7e-a52b-323e8ba62538",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HXHuw5NnnFsJJ5rYW4B8kE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1652,
      "cache_read_input_tokens": 23566,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1652
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

_source line 14_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01AoYKVyZfkz4hXn7kn7x4PC`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": {
    "exp_id": "westd-pi05-vla-only-object-s43-paired"
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
  "session_id": "eb7c021e-380a-410b-a199-64af6b82580d",
  "uuid": "99c8dbeb-5592-4456-add1-045db4bd9802",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HXHuw5NnnFsJJ5rYW4B8kE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1652,
      "cache_read_input_tokens": 23566,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1652
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01TuYRfxMHQkRXhzjysgUW6j`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": {
    "exp_id": "westd-pi05-vla-only-object-s44-paired"
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
  "session_id": "eb7c021e-380a-410b-a199-64af6b82580d",
  "uuid": "d8ad2bad-8d11-4e78-8fea-fd94f4033549",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HXHuw5NnnFsJJ5rYW4B8kE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1652,
      "cache_read_input_tokens": 23566,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1652
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

_source line 16 · 2026-05-26T12:05:32.624Z_

<details><summary>↩ Tool result · `toolu_014asx6NE6Ypoun6JC4XHhKo`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.1442}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eb7c021e-380a-410b-a199-64af6b82580d",
  "uuid": "ad24067b-9cc3-4106-bef8-eca4df9f8806",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 7.1442}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.1442}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-26T12:05:39.729Z_

<details><summary>↩ Tool result · `toolu_01AoYKVyZfkz4hXn7kn7x4PC`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.0711}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eb7c021e-380a-410b-a199-64af6b82580d",
  "uuid": "8989b5d9-9f3d-4d22-a5c1-eefc63a7c000",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 7.0711}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.0711}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-26T12:05:47.952Z_

<details><summary>↩ Tool result · `toolu_01TuYRfxMHQkRXhzjysgUW6j`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 8.1745}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eb7c021e-380a-410b-a199-64af6b82580d",
  "uuid": "fd437af5-4ed3-4b43-a03f-066a200ff873",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 8.1745}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 8.1745}}"
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
Got all 3 JSON results. Let me summarize:

- Seed 42: overall_success_rate = 0.995 (199/200, bbq_sauce 19/20)
- Seed 43: overall_success_rate = 1.0 (200/200, all perfect)
- Seed 44: overall_success_rate = 0.995 (199/200, bbq_sauce 19/20)

Mean = (0.995 + 1.0 + 0.995) / 3 = 2.99 / 3 = 0.99667


Now I'm calculating the standard deviation across these three runs, which comes out to about 0.00236.

I need to decide whether to use the sample standard deviation with N-1 degrees of freedom, which gives 0.00289, or the population standard deviation. After that, I should search the registry for existing π0.5 object results and W&B runs to find comparable baselines.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eb7c021e-380a-410b-a199-64af6b82580d",
  "uuid": "d3c6f0bc-f4ac-43ba-b3fb-b9f2c32a2a11",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UkRuSUnwtAENiMurQVPfDj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3967,
      "cache_read_input_tokens": 25218,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3967
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

All 3 JSON files retrieved. Now checking W&B and existing π0.5 Object baselines in registry for comparison.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eb7c021e-380a-410b-a199-64af6b82580d",
  "uuid": "4bd94834-6fb7-4aa0-979b-38b9d71419f6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UkRuSUnwtAENiMurQVPfDj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3967,
      "cache_read_input_tokens": 25218,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3967
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__list_wandb_runs · `toolu_015Jsz8ZPhFBNRBtnbt8zf8S`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": {
    "display_name": {
      "$regex": "object.*vla.*pi05.*westd"
    }
  },
  "limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eb7c021e-380a-410b-a199-64af6b82580d",
  "uuid": "86c4db25-8cef-4f8c-8e9d-401aea43ad7d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UkRuSUnwtAENiMurQVPfDj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3967,
      "cache_read_input_tokens": 25218,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3967
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

_source line 22 · 2026-05-26T12:05:59.829Z_

<details><summary>↩ Tool result · reported error · `toolu_015Jsz8ZPhFBNRBtnbt8zf8S`</summary>

```text
Error executing tool list_wandb_runs: list_wandb_runs() got an unexpected keyword argument 'wandb_project'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eb7c021e-380a-410b-a199-64af6b82580d",
  "uuid": "f125df0d-04de-4986-8a57-106e7a31e866",
  "tool_use_result": "Error: Error executing tool list_wandb_runs: list_wandb_runs() got an unexpected keyword argument 'wandb_project'"
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01RGiPSUAP7fZAXUbjr2tvt7`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": {
    "exp_id": {
      "$regex": "pi05.*object"
    }
  },
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
  "session_id": "eb7c021e-380a-410b-a199-64af6b82580d",
  "uuid": "60b52e1e-63cd-4d44-8c8d-11242f82cc34",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UkRuSUnwtAENiMurQVPfDj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3967,
      "cache_read_input_tokens": 25218,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3967
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

_source line 24 · 2026-05-26T12:06:07.058Z_

<details><summary>↩ Tool result · `toolu_01RGiPSUAP7fZAXUbjr2tvt7`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 6.4675}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eb7c021e-380a-410b-a199-64af6b82580d",
  "uuid": "8d0924c1-0f5b-4d3d-8ba4-36b51bdea47e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 6.4675}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 6.4675}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 25_

<details><summary>Logged reasoning block</summary>

```text
The W&B list failed due to the parameter name issue. Let me try without the wandb_project parameter. Also the registry filter with regex didn't work - it returned 0 results. Let me try a broader search.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eb7c021e-380a-410b-a199-64af6b82580d",
  "uuid": "68268d4d-d503-4ac6-bc23-55ee5e79ab0b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011o9iZ8WyyioANYbhBH9hru",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 953,
      "cache_read_input_tokens": 29185,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 953
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__list_wandb_runs · `toolu_01EKJJDo3ZQcxkUFxnAj2mBZ`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": {
    "display_name": {
      "$regex": "object.*vla.*pi05"
    }
  },
  "limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eb7c021e-380a-410b-a199-64af6b82580d",
  "uuid": "f3544b4a-5a5a-4bd2-9661-6fe983aac630",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011o9iZ8WyyioANYbhBH9hru",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 953,
      "cache_read_input_tokens": 29185,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 953
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

_source line 27 · 2026-05-26T12:06:13.291Z_

<details><summary>↩ Tool result · reported error · `toolu_01EKJJDo3ZQcxkUFxnAj2mBZ`</summary>

```text
Error executing tool list_wandb_runs: list_wandb_runs() got an unexpected keyword argument 'wandb_project'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eb7c021e-380a-410b-a199-64af6b82580d",
  "uuid": "9970552a-0725-42ab-9c54-27917b585d01",
  "tool_use_result": "Error: Error executing tool list_wandb_runs: list_wandb_runs() got an unexpected keyword argument 'wandb_project'"
}
```

</details>

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01MbWkuxEw9FiTJ5Zp7pjy1B`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eb7c021e-380a-410b-a199-64af6b82580d",
  "uuid": "cae7ed82-4034-4208-8cc3-bd9da2a02b06",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011o9iZ8WyyioANYbhBH9hru",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 953,
      "cache_read_input_tokens": 29185,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 953
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

_source line 29 · 2026-05-26T12:06:20.169Z_

<details><summary>↩ Tool result · `toolu_01MbWkuxEw9FiTJ5Zp7pjy1B`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"westd-pi05-vla-only-goal-s44-paired\": {\"status\": \"ANALYZING\", \"created_at\": \"2026-05-26T11:02:01.323Z\", \"updated_at\": \"2026-05-26T12:06:09.890Z\", \"hypothesis\": \"π0.5 VLA-only baseline on Goal s44 (westd same-server paired). Blackwell paired comparison for cross-hardware validation.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.955, \"n_rollouts\": 20, \"n_tasks\": 10, \"per_task_min\": 0.8, \"per_task_max\": 1}}, \"westd-pi05-vla-only-goal-s43-paired\": {\"status\": \"ANALYZING\", \"created_at\": \"2026-05-26T11:01:46.159Z\", \"updated_at\": \"2026-05-26T12:06:00.139Z\", \"hypothesis\": \"π0.5 VLA-only baseline on Goal s43 (westd same-server paired). Blackwell paired comparison for cross-hardware validation.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.965, \"n_rollouts\": 20, \"n_tasks\": 10, \"per_task_min\": 0.85, \"per_task_max\": 1}}, \"westd-pi05-vla-only-goal-s42-paired\": {\"status\": \"ANALYZING\", \"created_at\": \"2026-05-26T11:01:32.135Z\", \"updated_at\": \"2026-05-26T12:05:54.118Z\", \"hypothesis\": \"π0.5 VLA-only baseline on Goal s42 (westd same-server paired). Blackwell paired comparison for cross-hardware validation.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.975, \"n_rollouts\": 20, \"n_tasks\": 10, \"per_task_min\": 0.9, \"per_task_max\": 1}}, \"westd-pi05-vla-only-object-s44-paired\": {\"status\": \"DONE\", \"created_at\": \"2026-05-26T11:02:45.036Z\", \"updated_at\": \"2026-05-26T12:05:45.887Z\", \"hypothesis\": \"π0.5 VLA-only baseline on Object s44. westd same-server paired comparison (Blackwell).\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.995, \"n_rollouts\": 20, \"n_tasks\": 10, \"per_task_min\": 0.95, \"per_task_max\": 1}}, \"westd-pi05-vla-only-object-s43-paired\": {\"status\": \"DONE\", \"created_at\": \"2026-05-26T11:02:30.548Z\", \"updated_at\": \"2026-05-26T12:05:32.934Z\", \"hypothesis\": \"π0.5 VLA-only baseline on Object s43 (westd same-server paired). Blackwell paired comparison for cross-hardware validation.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 1, \"n_rollouts\": 20, \"n_tasks\": 10, \"per_task_min\": 1, \"per_task_max\": 1}}, \"westd-pi05-vla-only-object-s42-paired\": {\"status\": \"DONE\", \"created_at\": \"2026-05-26T11:02:15.888Z\", \"updated_at\": \"2026-05-26T12:05:22.121Z\", \"hypothesis\": \"π0.5 VLA-only baseline on Object s42 (westd same-server paired). Blackwell paired comparison for cross-hardware validation.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.995, \"n_rollouts\": 20, \"n_tasks\": 10, \"per_task_min\": 0.95, \"per_task_max\": 1}}, \"pi05-adaptive-object-s42-cqa1\": {\"status\": \"ANALYZING\", \"created_at\": \"2026-05-26T06:53:47.761Z\", \"updated_at\": \"2026-05-26T12:05:13.994Z\", \"hypothesis\": \"π0.5 Adaptive Conformal CRM on Object s42. 4090 cluster backup for westd result, controlling Blackwell architecture bias.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.855, \"n_rollouts\": 20, \"n_tasks\": 10, \"trigger_rate\": 0.037, \"mean_uncertainty\": 0.0842, \"conformal_threshold\": 0.25, \"max_correction_norm\": 0.2, \"per_task_min\": 0.5, \"per_task_max\": 1}}, \"westd-pi05-vla-only-long-s44-paired\": {\"status\": \"QUEUED\", \"created_at\": \"2026-05-26T12:00:13.951Z\", \"updated_at\": \"2026-05-26T12:03:51.023Z\", \"hypothesis\": \"π0.5 VLA-only baseline on Long s44. westd same-server paired comparison (Blackwell). Fills Table 2 Long VLA-only gap.\"}, \"westd-pi05-vla-only-long-s43-paired\": {\"status\": \"QUEUED\", \"created_at\": \"2026-05-26T12:00:43.452Z\", \"updated_at\": \"2026-05-26T12:03:13.221Z\", \"hypothesis\": \"π0.5 VLA-only baseline on Long s43. westd same-server paired comparison (Blackwell). Complete Long VLA-only 3-seed coverage.\"}, \"westd-pi05-vla-only-long-s42-paired\": {\"status\": \"QUEUED\", \"created_at\": \"2026-05-26T11:59:43.428Z\", \"updated_at\": \"2026-05-26T12:02:38.770Z\", \"hypothesis\": \"π0.5 VLA-only baseline on Long s42. westd same-server paired comparison (Blackwell). Fills Table 2 Long VLA-only gap.\"}, \"westd-pi05-vla-only-spatial-s44-paired\": {\"status\": \"QUEUED\", \"created_at\": \"2026-05-26T11:59:17.322Z\", \"updated_at\": \"2026-05-26T12:02:04.265Z\", \"hypothesis\": \"π0.5 VLA-only baseline on Spatial s44. westd same-server paired comparison (Blackwell). Fills Table 2 Spatial VLA-only gap.\"}, \"westd-pi05-vla-only-spatial-s43-paired\": {\"status\": \"QUEUED\", \"created_at\": \"2026-05-26T11:58:45.293Z\", \"updated_at\": \"2026-05-26T12:01:29.386Z\", \"hypothesis\": \"π0.5 VLA-only baseline on Spatial s43. westd same-server paired comparison (Blackwell). Fills Table 2 Spatial VLA-only gap.\"}, \"westd-pi05-vla-only-spatial-s42-paired\": {\"status\": \"QUEUED\", \"created_at\": \"2026-05-26T11:56:11.874Z\", \"updated_at\": \"2026-05-26T11:58:06.007Z\", \"hypothesis\": \"π0.5 VLA-only baseline on Spatial s42. westd same-server paired comparison (Blackwell). Fills Table 2 Spatial VLA-only gap.\"}, \"pi05-adaptive-object-s43-bjb2-24035\": {\"status\": \"DONE\", \"created_at\": \"2026-05-26T10:51:28.267Z\", \"updated_at\": \"2026-05-26T11:57:37.320Z\", \"hypothesis\": \"π0.5 Adaptive Conformal CRM (K=2, τ=0.25) on Object s43. Table 2 cross-architecture gating analysis. Tests adaptive gating on Object suite.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.83, \"benchmark\": \"object\", \"mode\": \"adaptive_conformal_crm\", \"seed\": 43, \"model\": \"pi05\", \"n_rollouts\": 20, \"n_tasks\": 10}}, \"pi05-adaptive-long-s44-cqa1-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-26T09:44:58.714Z\", \"updated_at\": \"2026-05-26T11:35:01.941Z\", \"hypothesis\": \"π0.5 Adaptive Conformal CRM (K=2, τ=0.25) on Long s44. Table 2 long-horizon cross-architecture analysis. Re-run after cqa1 node-level tmux cleanup.\", \"parent\": \"pi05-adaptive-long-s44-cqa1\", \"metrics\": {\"success_rate\": 0, \"trigger_rate\": null, \"benchmark\": \"long\", \"mode\": \"adaptive_conformal_crm\", \"seed\": 44, \"model\": \"pi05\", \"n_rollouts\": 20, \"n_tasks\": 10, \"error\": \"CUDA OOM at step 0 of every rollout\", \"successes\": 0, \"total\": 200}, \"conclusion\": \"failed\"}, \"pi05-adaptive-long-s43-cqa1-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-26T09:44:54.814Z\", \"updated_at\": \"2026-05-26T11:34:57.651Z\", \"hypothesis\": \"π0.5 Adaptive Conformal CRM (K=2, τ=0.25) on Long s43. Table 2 long-horizon cross-architecture analysis. Re-run after cqa1 node-level tmux cleanup.\", \"parent\": \"pi05-adaptive-long-s43-cqa1\", \"metrics\": {\"success_rate\": 0, \"trigger_rate\": null, \"benchmark\": \"long\", \"mode\": \"adaptive_conformal_crm\", \"seed\": 43, \"model\": \"pi05\", \"n_rollouts\": 20, \"n_tasks\": 10, \"error\": \"CUDA OOM at step 0 of every rollout\", \"successes\": 0, \"total\": 200}, \"conclusion\": \"failed\"}, \"pi05-adaptive-object-s43-cqa1-r3\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-26T11:29:55.374Z\", \"updated_at\": \"2026-05-26T11:31:13.727Z\", \"hypothesis\": \"π0.5 Adaptive Conformal (τ=0.25, K=2, max_correction_norm=0.2) on Object s43. Re-run after bjb2-24035 process death. Table 2 cross-suite validation.\", \"parent\": \"pi05-adaptive-object-s43-bjb2-24035\"}, \"pi05-adaptive-goal-s42-cqa1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-26T06:53:55.121Z\", \"updated_at\": \"2026-05-26T11:28:57.790Z\", \"hypothesis\": \"π0.5 Adaptive Conformal CRM on Goal s42. 4090 cluster backup for westd result, controlling Blackwell architecture bias.\", \"metrics\": {\"success_rate\": 0.895, \"success_count\": 179, \"total_rollouts\": 200, \"trigger_rate\": 0.081, \"mean_unc\": 0.1152, \"benchmark\": \"goal\", \"mode\": \"adaptive_conformal_crm\", \"seed\": 42, \"model\": \"pi05\", \"n_rollouts\": 20, \"n_tasks\": 10, \"K\": 2, \"max_correction_norm\": 0.2, \"conformal_threshold\": 0.25, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.7, \"put_the_bowl_on_the_stove\": 0.95, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.85, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.7, \"put_the_bowl_on_top_of_the_cabinet\": 1, \"push_the_plate_to_the_front_of_the_stove\": 1, \"put_the_cream_cheese_in_the_bowl\": 0.9, \"turn_on_the_stove\": 1, \"put_the_bowl_on_the_plate\": 1, \"put_the_wine_bottle_on_the_rack\": 0.85}}, \"conclusion\": \"success\"}, \"pi05-adaptive-long-s44-cqa1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-26T05:53:43.686Z\", \"updated_at\": \"2026-05-26T11:26:44.982Z\", \"hypothesis\": \"π0.5 Adaptive Conformal on Long s44. Table 2 long-horizon cross-architecture analysis.\", \"conclusion\": \"killed\", \"notes\": \"失败原因(初步): cqa1 上 6 个 π0.5 并发导致 OOM (已知模式)。reconcile 自动标记 failed。Worker 深查中。\"}, \"pi05-adaptive-long-s43-cqa1\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-26T05:53:07.701Z\", \"updated_at\": \"2026-05-26T11:26:37.267Z\", \"hypothesis\": \"π0.5 Adaptive Conformal on Long s43. Table 2 long-horizon cross-architecture analysis.\", \"notes\": \"失败原因(初步): cqa1 上 6 个 π0.5 并发导致 OOM (已知模式)。reconcile 自动标记 failed。Worker 深查中。\", \"conclusion\": \"killed\"}, \"pi05-adaptive-object-s44-cqa1\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-26T05:52:41.664Z\", \"updated_at\": \"2026-05-26T11:26:29.402Z\", \"hypothesis\": \"π0.5 Adaptive Conformal on Object s44. Table 2 cross-suite validation.\", \"notes\": \"失败原因(初步): cqa1 上 6 个 π0.5 并发导致 OOM (已知模式)。日志文件不存在，进程被 kill 前未写 output。Worker 深查中。\", \"conclusion\": \"killed\"}, \"pi05-adaptive-goal-s44-bjb1\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-26T10:18:00.006Z\", \"updated_at\": \"2026-05-26T11:23:06.585Z\", \"hypothesis\": \"π0.5 Adaptive Conformal (τ=0.25, K=2, max_correction_norm=0.2) on Goal s44. Table 2 paired comparison with CRM K=2 and VLA-only on same server.\"}, \"pi05-adaptive-goal-s44-bjb1-18228\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-26T11:08:38.962Z\", \"updated_at\": \"2026-05-26T11:08:38.962Z\"}, \"pi05-adaptive-long-s44-cqa1-r3\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-26T10:53:38.703Z\", \"updated_at\": \"2026-05-26T10:58:02.641Z\", \"hypothesis\": \"π0.5 Adaptive Conformal CRM (K=2, τ=0.25) on Long s44. r3 re-run after r2 OOM (zombie process collision). Clean GPU confirms adaptive fits in 24GB on single process.\", \"parent\": \"pi05-adaptive-long-s44-cqa1-r2\"}, \"pi05-adaptive-long-s43-cqa1-r3\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-26T10:53:20.461Z\", \"updated_at\": \"2026-05-26T10:57:13.677Z\", \"hypothesis\": \"π0.5 Adaptive Conformal CRM (K=2, τ=0.25) on Long s43. r3 re-run after r2 OOM (zombie process collision). Clean GPU confirms adaptive fits in 24GB on single process.\", \"parent\": \"pi05-adaptive-long-s43-cqa1-r2\"}, \"pi05-adaptive-object-s44-cqa1-r3\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-26T10:53:53.430Z\", \"updated_at\": \"2026-05-26T10:56:25.007Z\", \"hypothesis\": \"π0.5 Adaptive Conformal CRM (K=2, τ=0.25) on Object s44. r3 re-run after r2 GPU collision (double-process on GPU 3). Table 2 cross-architecture gating.\", \"parent\": \"pi05-adaptive-object-s44-cqa1-r2\"}, \"westd-pi05-crm-k2-goal-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-26T04:26:05.028Z\", \"updated_at\": \"2026-05-26T10:52:23.271Z\", \"hypothesis\": \"π0.5 CRM obs_only K=2 (ε=0.05, always-on) on LIBERO-Goal s42. Tests whether unconditional CRM correction (no adaptive gating) helps π0.5 on goal suite. Comparison vs adaptive gating and K=2 mean baseline.\", \"metrics\": {\"success_rate\": 0.855, \"benchmark\": \"goal\", \"mode\": \"crm_obs_only\", \"seed\": 42, \"K\": 2, \"model\": \"pi05\", \"n_rollouts\": 20, \"n_tasks\": 10}, \"conclusion\": \"success\"}, \"westd-pi05-adaptive-object-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-26T04:19:53.085Z\", \"updated_at\": \"2026-05-26T10:52:12.970Z\", \"hypothesis\": \"π0.5 Adaptive Conformal CRM (K=2, τ=0.25, ε=0.2) on LIBERO-Object s42. Cross-suite validation of adaptive conformal refinement on π0.5.\", \"metrics\": {\"success_rate\": 0.835, \"benchmark\": \"object\", \"mode\": \"adaptive_conformal_crm\", \"seed\": 42, \"model\": \"pi05\", \"n_rollouts\": 20, \"n_tasks\": 10}, \"conclusion\": \"success\"}, \"westd-pi05-adaptive-goal-s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-26T04:19:43.389Z\", \"updated_at\": \"2026-05-26T10:51:54.441Z\", \"hypothesis\": \"π0.5 Adaptive Conformal CRM (K=2, τ=0.25, ε=0.2) on LIBERO-Goal s43. Seed variation for 3-seed mean±std on Goal benchmark.\", \"metrics\": {\"success_rate\": 0.875, \"benchmark\": \"goal\", \"mode\": \"adaptive_conformal_crm\", \"seed\": 43, \"model\": \"pi05\", \"n_rollouts\": 20, \"n_tasks\": 10}, \"conclusion\": \"success\"}, \"westd-pi05-adaptive-goal-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-26T04:19:38.990Z\", \"updated_at\": \"2026-05-26T10:51:37.558Z\", \"hypothesis\": \"π0.5 Adaptive Conformal CRM (K=2, τ=0.25, ε=0.2) on LIBERO-Goal s42. Tests whether adaptive conformal refinement improves π0.5 on goal-conditioned tasks.\", \"metrics\": {\"success_rate\": 0.88, \"benchmark\": \"goal\", \"mode\": \"adaptive_conformal_crm\", \"seed\": 42, \"model\": \"pi05\", \"n_rollouts\": 20, \"n_tasks\": 10}, \"conclusion\": \"success\"}, \"pi05-adaptive-long-s42-r2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-26T03:44:44.161Z\", \"updated_at\": \"2026-05-26T10:50:49.947Z\", \"hypothesis\": \"π0.5 Adaptive Conformal on Long s42 (re-run after cqa1 crash). Cross-suite validation for π0.5 Table 2.\"}, \"pi05-crm-k2-long-s43-r2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-26T03:44:25.674Z\", \"updated_at\": \"2026-05-26T10:50:36.087Z\", \"hypothesis\": \"π0.5 CRM K=2 obs_only on LIBERO-Long s43 (re-run after server restart). Tests whether CRM correction affects strong π0.5 baseline on long-horizon tasks.\", \"parent\": \"pi05-crm-k2-long-s43\"}, \"pi05-crm-k2-long-s42-r2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-26T03:44:17.432Z\", \"updated_at\": \"2026-05-26T10:50:28.060Z\", \"hypothesis\": \"π0.5 CRM K=2 obs_only on LIBERO-Long s42 (re-run after server restart). Tests whether CRM correction affects strong π0.5 baseline on long-horizon tasks.\", \"parent\": \"pi05-crm-k2-long-s42\"}, \"pi05-adaptive-object-s44-cqa1-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-26T09:44:50.881Z\", \"updated_at\": \"2026-05-26T10:30:10.213Z\", \"hypothesis\": \"π0.5 Adaptive Conformal CRM (K=2, τ=0.25) on Object s44. Table 2 cross-architecture gating analysis. Re-run after cqa1 node-level tmux cleanup.\", \"parent\": \"pi05-adaptive-object-s44-cqa1\", \"conclusion\": \"failed\"}, \"pi05-adaptive-goal-s43-bjb1-18228\": {\"status\": \"DONE\", \"created_at\": \"2026-05-26T06:45:32.801Z\", \"updated_at\": \"2026-05-26T10:24:06.070Z\", \"hypothesis\": \"π0.5 Adaptive Conformal CRM (K=2, τ=0.25, ε=0.2) on Goal s43. 4090 cluster cross-validation for westd Goal s43, controlling Blackwell architecture bias.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 89.5}}, \"pi05-adaptive-goal-s44-cqa1-r2\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-26T10:19:04.430Z\", \"updated_at\": \"2026-05-26T10:19:04.430Z\"}, \"pi05-adaptive-goal-s43-cqa1-r2\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-26T10:18:49.165Z\", \"updated_at\": \"2026-05-26T10:18:49.165Z\"}, \"pi05-crm-k2-long-s42-bjb1\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-26T10:18:13.260Z\", \"updated_at\": \"2026-05-26T10:18:13.260Z\", \"hypothesis\": \"π0.5 CRM K=2 obs_only (always-on, ε=0.05) on Long s42. Table 2 long-horizon CRM impact with near-expert VLA on bjb1-18228.\"}, \"pi05-adaptive-object-s43-bjb1\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-26T10:18:05.197Z\", \"updated_at\": \"2026-05-26T10:18:05.197Z\", \"hypothesis\": \"π0.5 Adaptive Conformal CRM (K=2, τ=0.25) on Object s43. Table 2 cross-architecture gating analysis on bjb1-18228.\"}, \"pi05-adaptive-spatial-s44-bjb2-r2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-26T09:55:47.784Z\", \"updated_at\": \"2026-05-26T10:00:04.376Z\", \"hypothesis\": \"π0.5 Adaptive Conformal CRM (K=2, τ=0.25) on Spatial s44. Table 2 cross-architecture gating analysis. Re-run after bjb2-28827 node-level tmux cleanup.\"}, \"pi05-adaptive-spatial-s43-bjb2-r2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-26T09:55:43.728Z\", \"updated_at\": \"2026-05-26T09:59:15.673Z\", \"hypothesis\": \"π0.5 Adaptive Conformal CRM (K=2, τ=0.25) on Spatial s43. Table 2 cross-architecture gating analysis. Re-run after bjb2-28827 node-level tmux cleanup.\"}, \"pi05-adaptive-spatial-s42-bjb2-r2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-26T09:55:39.703Z\", \"updated_at\": \"2026-05-26T09:58:46.516Z\", \"hypothesis\": \"π0.5 Adaptive Conformal CRM (K=2, τ=0.25) on Spatial s42. Table 2 cross-architecture gating analysis. Re-run after bjb2-28827 node-level tmux cleanup.\"}, \"pi05-crm-k2-spatial-s44-bjb2-r2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-26T09:55:35.735Z\", \"updated_at\": \"2026-05-26T09:58:10.616Z\", \"hypothesis\": \"π0.5 CRM K=2 obs_only (always-on, ε=0.05) on Spatial s44. Table 2 cross-architecture CRM impact. Re-run after bjb2-28827 node-level tmux cleanup.\"}, \"pi05-crm-k2-spatial-s43-bjb2-r2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-26T09:55:31.701Z\", \"updated_at\": \"2026-05-26T09:57:41.093Z\", \"hypothesis\": \"π0.5 CRM K=2 obs_only (always-on, ε=0.05) on Spatial s43. Table 2 cross-architecture CRM impact. Re-run after bjb2-28827 node-level tmux cleanup.\"}, \"pi05-crm-k2-spatial-s42-bjb2-r2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-26T09:55:27.403Z\", \"updated_at\": \"2026-05-26T09:57:13.362Z\", \"hypothesis\": \"π0.5 CRM K=2 obs_only (always-on, ε=0.05) on Spatial s42. Table 2 cross-architecture CRM impact. Re-run after bjb2-28827 node-level tmux cleanup.\"}, \"pi05-crm-k2-object-s44-bjb1-r2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-26T09:44:46.771Z\", \"updated_at\": \"2026-05-26T09:53:09.173Z\", \"hypothesis\": \"π0.5 CRM K=2 obs_only (always-on, ε=0.05) on Object s44. Table 2 cross-architecture CRM impact with near-expert VLA. Re-run after bjb1-32546 node-level tmux cleanup.\", \"parent\": \"pi05-crm-k2-object-s44-bjb1\"}, \"pi05-crm-k2-object-s43-bjb1-r2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-26T09:44:42.092Z\", \"updated_at\": \"2026-05-26T09:53:00.538Z\", \"hypothesis\": \"π0.5 CRM K=2 obs_only (always-on, ε=0.05) on Object s43. Table 2 cross-architecture CRM impact with near-expert VLA. Re-run after bjb1-32546 node-level tmux cleanup.\", \"parent\": \"pi05-crm-k2-object-s43-bjb1\"}, \"pi05-crm-k2-object-s42-bjb1-r2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-26T09:44:37.659Z\", \"updated_at\": \"2026-05-26T09:52:52.585Z\", \"hypothesis\": \"π0.5 CRM K=2 obs_only (always-on, ε=0.05) on Object s42. Table 2 cross-architecture CRM impact with near-expert VLA. Re-run after bjb1-32546 node-level tmux cleanup.\", \"parent\": \"pi05-crm-k2-object-s42-bjb1\"}, \"pi05-crm-k2-goal-s44-bjb1-r2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-26T09:44:33.740Z\", \"updated_at\": \"2026-05-26T09:52:44.965Z\", \"hypothesis\": \"π0.5 CRM K=2 obs_only (always-on, ε=0.05) on Goal s44. Table 2 cross-architecture CRM impact with near-expert VLA. Re-run after bjb1-32546 node-level tmux cleanup.\", \"parent\": \"pi05-crm-k2-goal-s44-bjb1\"}, \"pi05-crm-k2-goal-s43-bjb1-r2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-26T09:44:29.605Z\", \"updated_at\": \"2026-05-26T09:52:37.286Z\", \"hypothesis\": \"π0.5 CRM K=2 obs_only (always-on, ε=0.05) on Goal s43. Table 2 cross-architecture CRM impact with near-expert VLA. Re-run after bjb1-32546 node-level tmux cleanup.\", \"parent\": \"pi05-crm-k2-goal-s43-bjb1\"}}, \"count\": 50, \"total\": 1205, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 6.8322}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eb7c021e-380a-410b-a199-64af6b82580d",
  "uuid": "1d7b67ef-2476-4ae9-875f-bdfc6c76f4c6",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"westd-pi05-vla-only-goal-s44-paired\\\": {\\\"status\\\": \\\"ANALYZING\\\", \\\"created_at\\\": \\\"2026-05-26T11:02:01.323Z\\\", \\\"updated_at\\\": \\\"2026-05-26T12:06:09.890Z\\\", \\\"hypothesis\\\": \\\"π0.5 VLA-only baseline on Goal s44 (westd same-server paired). Blackwell paired comparison for cross-hardware validation.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.955, \\\"n_rollouts\\\": 20, \\\"n_tasks\\\": 10, \\\"per_task_min\\\": 0.8, \\\"per_task_max\\\": 1}}, \\\"westd-pi05-vla-only-goal-s43-paired\\\": {\\\"status\\\": \\\"ANALYZING\\\", \\\"created_at\\\": \\\"2026-05-26T11:01:46.159Z\\\", \\\"updated_at\\\": \\\"2026-05-26T12:06:00.139Z\\\", \\\"hypothesis\\\": \\\"π0.5 VLA-only baseline on Goal s43 (westd same-server paired). Blackwell paired comparison for cross-hardware validation.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.965, \\\"n_rollouts\\\": 20, \\\"n_tasks\\\": 10, \\\"per_task_min\\\": 0.85, \\\"per_task_max\\\": 1}}, \\\"westd-pi05-vla-only-goal-s42-paired\\\": {\\\"status\\\": \\\"ANALYZING\\\", \\\"created_at\\\": \\\"2026-05-26T11:01:32.135Z\\\", \\\"updated_at\\\": \\\"2026-05-26T12:05:54.118Z\\\", \\\"hypothesis\\\": \\\"π0.5 VLA-only baseline on Goal s42 (westd same-server paired). Blackwell paired comparison for cross-hardware validation.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.975, \\\"n_rollouts\\\": 20, \\\"n_tasks\\\": 10, \\\"per_task_min\\\": 0.9, \\\"per_task_max\\\": 1}}, \\\"westd-pi05-vla-only-object-s44-paired\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-26T11:02:45.036Z\\\", \\\"updated_at\\\": \\\"2026-05-26T12:05:45.887Z\\\", \\\"hypothesis\\\": \\\"π0.5 VLA-only baseline on Object s44. westd same-server paired comparison (Blackwell).\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.995, \\\"n_rollouts\\\": 20, \\\"n_tasks\\\": 10, \\\"per_task_min\\\": 0.95, \\\"per_task_max\\\": 1}}, \\\"westd-pi05-vla-only-object-s43-paired\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-26T11:02:30.548Z\\\", \\\"updated_at\\\": \\\"2026-05-26T12:05:32.934Z\\\", \\\"hypothesis\\\": \\\"π0.5 VLA-only baseline on Object s43 (westd same-server paired). Blackwell paired comparison for cross-hardware validation.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 1, \\\"n_rollouts\\\": 20, \\\"n_tasks\\\": 10, \\\"per_task_min\\\": 1, \\\"per_task_max\\\": 1}}, \\\"westd-pi05-vla-only-object-s42-paired\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-26T11:02:15.888Z\\\", \\\"updated_at\\\": \\\"2026-05-26T12:05:22.121Z\\\", \\\"hypothesis\\\": \\\"π0.5 VLA-only baseline on Object s42 (westd same-server paired). Blackwell paired comparison for cross-hardware validation.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.995, \\\"n_rollouts\\\": 20, \\\"n_tasks\\\": 10, \\\"per_task_min\\\": 0.95, \\\"per_task_max\\\": 1}}, \\\"pi05-adaptive-object-s42-cqa1\\\": {\\\"status\\\": \\\"ANALYZING\\\", \\\"created_at\\\": \\\"2026-05-26T06:53:47.761Z\\\", \\\"updated_at\\\": \\\"2026-05-26T12:05:13.994Z\\\", \\\"hypothesis\\\": \\\"π0.5 Adaptive Conformal CRM on Object s42. 4090 cluster backup for westd result, controlling Blackwell architecture bias.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.855, \\\"n_rollouts\\\": 20, \\\"n_tasks\\\": 10, \\\"trigger_rate\\\": 0.037, \\\"mean_uncertainty\\\": 0.0842, \\\"conformal_threshold\\\": 0.25, \\\"max_correction_norm\\\": 0.2, \\\"per_task_min\\\": 0.5, \\\"per_task_max\\\": 1}}, \\\"westd-pi05-vla-only-long-s44-paired\\\": {\\\"status\\\": \\\"QUEUED\\\", \\\"created_at\\\": \\\"2026-05-26T12:00:13.951Z\\\", \\\"updated_at\\\": \\\"2026-05-26T12:03:51.023Z\\\", \\\"hypothesis\\\": \\\"π0.5 VLA-only baseline on Long s44. westd same-server paired comparison (Blackwell). Fills Table 2 Long VLA-only gap.\\\"}, \\\"westd-pi05-vla-only-long-s43-paired\\\": {\\\"status\\\": \\\"QUEUED\\\", \\\"created_at\\\": \\\"2026-05-26T12:00:43.452Z\\\", \\\"updated_at\\\": \\\"2026-05-26T12:03:13.221Z\\\", \\\"hypothesis\\\": \\\"π0.5 VLA-only baseline on Long s43. westd same-server paired comparison (Blackwell). Complete Long VLA-only 3-seed coverage.\\\"}, \\\"westd-pi05-vla-only-long-s42-paired\\\": {\\\"status\\\": \\\"QUEUED\\\", \\\"created_at\\\": \\\"2026-05-26T11:59:43.428Z\\\", \\\"updated_at\\\": \\\"2026-05-26T12:02:38.770Z\\\", \\\"hypothesis\\\": \\\"π0.5 VLA-only baseline on Long s42. westd same-server paired comparison (Blackwell). Fills Table 2 Long VLA-only gap.\\\"}, \\\"westd-pi05-vla-only-spatial-s44-paired\\\": {\\\"status\\\": \\\"QUEUED\\\", \\\"created_at\\\": \\\"2026-05-26T11:59:17.322Z\\\", \\\"updated_at\\\": \\\"2026-05-26T12:02:04.265Z\\\", \\\"hypothesis\\\": \\\"π0.5 VLA-only baseline on Spatial s44. westd same-server paired comparison (Blackwell). Fills Table 2 Spatial VLA-only gap.\\\"}, \\\"westd-pi05-vla-only-spatial-s43-paired\\\": {\\\"status\\\": \\\"QUEUED\\\", \\\"created_at\\\": \\\"2026-05-26T11:58:45.293Z\\\", \\\"updated_at\\\": \\\"2026-05-26T12:01:29.386Z\\\", \\\"hypothesis\\\": \\\"π0.5 VLA-only baseline on Spatial s43. westd same-server paired comparison (Blackwell). Fills Table 2 Spatial VLA-only gap.\\\"}, \\\"westd-pi05-vla-only-spatial-s42-paired\\\": {\\\"status\\\": \\\"QUEUED\\\", \\\"created_at\\\": \\\"2026-05-26T11:56:11.874Z\\\", \\\"updated_at\\\": \\\"2026-05-26T11:58:06.007Z\\\", \\\"hypothesis\\\": \\\"π0.5 VLA-only baseline on Spatial s42. westd same-server paired comparison (Blackwell). Fills Table 2 Spatial VLA-only gap.\\\"}, \\\"pi05-adaptive-object-s43-bjb2-24035\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-26T10:51:28.267Z\\\", \\\"updated_at\\\": \\\"2026-05-26T11:57:37.320Z\\\", \\\"hypothesis\\\": \\\"π0.5 Adaptive Conformal CRM (K=2, τ=0.25) on Object s43. Table 2 cross-architecture gating analysis. Tests adaptive gating on Object suite.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.83, \\\"benchmark\\\": \\\"object\\\", \\\"mode\\\": \\\"adaptive_conformal_crm\\\", \\\"seed\\\": 43, \\\"model\\\": \\\"pi05\\\", \\\"n_rollouts\\\": 20, \\\"n_tasks\\\": 10}}, \\\"pi05-adaptive-long-s44-cqa1-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-26T09:44:58.714Z\\\", \\\"updated_at\\\": \\\"2026-05-26T11:35:01.941Z\\\", \\\"hypothesis\\\": \\\"π0.5 Adaptive Conformal CRM (K=2, τ=0.25) on Long s44. Table 2 long-horizon cross-architecture analysis. Re-run after cqa1 node-level tmux cleanup.\\\", \\\"parent\\\": \\\"pi05-adaptive-long-s44-cqa1\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0, \\\"trigger_rate\\\": null, \\\"benchmark\\\": \\\"long\\\", \\\"mode\\\": \\\"adaptive_conformal_crm\\\", \\\"seed\\\": 44, \\\"model\\\": \\\"pi05\\\", \\\"n_rollouts\\\": 20, \\\"n_tasks\\\": 10, \\\"error\\\": \\\"CUDA OOM at step 0 of every rollout\\\", \\\"successes\\\": 0, \\\"total\\\": 200}, \\\"conclusion\\\": \\\"failed\\\"}, \\\"pi05-adaptive-long-s43-cqa1-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-26T09:44:54.814Z\\\", \\\"updated_at\\\": \\\"2026-05-26T11:34:57.651Z\\\", \\\"hypothesis\\\": \\\"π0.5 Adaptive Conformal CRM (K=2, τ=0.25) on Long s43. Table 2 long-horizon cross-architecture analysis. Re-run after cqa1 node-level tmux cleanup.\\\", \\\"parent\\\": \\\"pi05-adaptive-long-s43-cqa1\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0, \\\"trigger_rate\\\": null, \\\"benchmark\\\": \\\"long\\\", \\\"mode\\\": \\\"adaptive_conformal_crm\\\", \\\"seed\\\": 43, \\\"model\\\": \\\"pi05\\\", \\\"n_rollouts\\\": 20, \\\"n_tasks\\\": 10, \\\"error\\\": \\\"CUDA OOM at step 0 of every rollout\\\", \\\"successes\\\": 0, \\\"total\\\": 200}, \\\"conclusion\\\": \\\"failed\\\"}, \\\"pi05-adaptive-object-s43-cqa1-r3\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-26T11:29:55.374Z\\\", \\\"updated_at\\\": \\\"2026-05-26T11:31:13.727Z\\\", \\\"hypothesis\\\": \\\"π0.5 Adaptive Conformal (τ=0.25, K=2, max_correction_norm=0.2) on Object s43. Re-run after bjb2-24035 process death. Table 2 cross-suite validation.\\\", \\\"parent\\\": \\\"pi05-adaptive-object-s43-bjb2-24035\\\"}, \\\"pi05-adaptive-goal-s42-cqa1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-26T06:53:55.121Z\\\", \\\"updated_at\\\": \\\"2026-05-26T11:28:57.790Z\\\", \\\"hypothesis\\\": \\\"π0.5 Adaptive Conformal CRM on Goal s42. 4090 cluster backup for westd result, controlling Blackwell architecture bias.\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.895, \\\"success_count\\\": 179, \\\"total_rollouts\\\": 200, \\\"trigger_rate\\\": 0.081, \\\"mean_unc\\\": 0.1152, \\\"benchmark\\\": \\\"goal\\\", \\\"mode\\\": \\\"adaptive_conformal_crm\\\", \\\"seed\\\": 42, \\\"model\\\": \\\"pi05\\\", \\\"n_rollouts\\\": 20, \\\"n_tasks\\\": 10, \\\"K\\\": 2, \\\"max_correction_norm\\\": 0.2, \\\"conformal_threshold\\\": 0.25, \\\"per_task\\\": {\\\"open_the_middle_drawer_of_the_cabinet\\\": 0.7, \\\"put_the_bowl_on_the_stove\\\": 0.95, \\\"put_the_wine_bottle_on_top_of_the_cabinet\\\": 0.85, \\\"open_the_top_drawer_and_put_the_bowl_inside\\\": 0.7, \\\"put_the_bowl_on_top_of_the_cabinet\\\": 1, \\\"push_the_plate_to_the_front_of_the_stove\\\": 1, \\\"put_the_cream_cheese_in_the_bowl\\\": 0.9, \\\"turn_on_the_stove\\\": 1, \\\"put_the_bowl_on_the_plate\\\": 1, \\\"put_the_wine_bottle_on_the_rack\\\": 0.85}}, \\\"conclusion\\\": \\\"success\\\"}, \\\"pi05-adaptive-long-s44-cqa1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-26T05:53:43.686Z\\\", \\\"updated_at\\\": \\\"2026-05-26T11:26:44.982Z\\\", \\\"hypothesis\\\": \\\"π0.5 Adaptive Conformal on Long s44. Table 2 long-horizon cross-architecture analysis.\\\", \\\"conclusion\\\": \\\"killed\\\", \\\"notes\\\": \\\"失败原因(初步): cqa1 上 6 个 π0.5 并发导致 OOM (已知模式)。reconcile 自动标记 failed。Worker 深查中。\\\"}, \\\"pi05-adaptive-long-s43-cqa1\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-26T05:53:07.701Z\\\", \\\"updated_at\\\": \\\"2026-05-26T11:26:37.267Z\\\", \\\"hypothesis\\\": \\\"π0.5 Adaptive Conformal on Long s43. Table 2 long-horizon cross-architecture analysis.\\\", \\\"notes\\\": \\\"失败原因(初步): cqa1 上 6 个 π0.5 并发导致 OOM (已知模式)。reconcile 自动标记 failed。Worker 深查中。\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"pi05-adaptive-object-s44-cqa1\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-26T05:52:41.664Z\\\", \\\"updated_at\\\": \\\"2026-05-26T11:26:29.402Z\\\", \\\"hypothesis\\\": \\\"π0.5 Adaptive Conformal on Object s44. Table 2 cross-suite validation.\\\", \\\"notes\\\": \\\"失败原因(初步): cqa1 上 6 个 π0.5 并发导致 OOM (已知模式)。日志文件不存在，进程被 kill 前未写 output。Worker 深查中。\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"pi05-adaptive-goal-s44-bjb1\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-26T10:18:00.006Z\\\", \\\"updated_at\\\": \\\"2026-05-26T11:23:06.585Z\\\", \\\"hypothesis\\\": \\\"π0.5 Adaptive Conformal (τ=0.25, K=2, max_correction_norm=0.2) on Goal s44. Table 2 paired comparison with CRM K=2 and VLA-only on same server.\\\"}, \\\"pi05-adaptive-goal-s44-bjb1-18228\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-26T11:08:38.962Z\\\", \\\"updated_at\\\": \\\"2026-05-26T11:08:38.962Z\\\"}, \\\"pi05-adaptive-long-s44-cqa1-r3\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-26T10:53:38.703Z\\\", \\\"updated_at\\\": \\\"2026-05-26T10:58:02.641Z\\\", \\\"hypothesis\\\": \\\"π0.5 Adaptive Conformal CRM (K=2, τ=0.25) on Long s44. r3 re-run after r2 OOM (zombie process collision). Clean GPU confirms adaptive fits in 24GB on single process.\\\", \\\"parent\\\": \\\"pi05-adaptive-long-s44-cqa1-r2\\\"}, \\\"pi05-adaptive-long-s43-cqa1-r3\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-26T10:53:20.461Z\\\", \\\"updated_at\\\": \\\"2026-05-26T10:57:13.677Z\\\", \\\"hypothesis\\\": \\\"π0.5 Adaptive Conformal CRM (K=2, τ=0.25) on Long s43. r3 re-run after r2 OOM (zombie process collision). Clean GPU confirms adaptive fits in 24GB on single process.\\\", \\\"parent\\\": \\\"pi05-adaptive-long-s43-cqa1-r2\\\"}, \\\"pi05-adaptive-object-s44-cqa1-r3\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-26T10:53:53.430Z\\\", \\\"updated_at\\\": \\\"2026-05-26T10:56:25.007Z\\\", \\\"hypothesis\\\": \\\"π0.5 Adaptive Conformal CRM (K=2, τ=0.25) on Object s44. r3 re-run after r2 GPU collision (double-process on GPU 3). Table 2 cross-architecture gating.\\\", \\\"parent\\\": \\\"pi05-adaptive-object-s44-cqa1-r2\\\"}, \\\"westd-pi05-crm-k2-goal-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-26T04:26:05.028Z\\\", \\\"updated_at\\\": \\\"2026-05-26T10:52:23.271Z\\\", \\\"hypothesis\\\": \\\"π0.5 CRM obs_only K=2 (ε=0.05, always-on) on LIBERO-Goal s42. Tests whether unconditional CRM correction (no adaptive gating) helps π0.5 on goal suite. Comparison vs adaptive gating and K=2 mean baseline.\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.855, \\\"benchmark\\\": \\\"goal\\\", \\\"mode\\\": \\\"crm_obs_only\\\", \\\"seed\\\": 42, \\\"K\\\": 2, \\\"model\\\": \\\"pi05\\\", \\\"n_rollouts\\\": 20, \\\"n_tasks\\\": 10}, \\\"conclusion\\\": \\\"success\\\"}, \\\"westd-pi05-adaptive-object-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-26T04:19:53.085Z\\\", \\\"updated_at\\\": \\\"2026-05-26T10:52:12.970Z\\\", \\\"hypothesis\\\": \\\"π0.5 Adaptive Conformal CRM (K=2, τ=0.25, ε=0.2) on LIBERO-Object s42. Cross-suite validation of adaptive conformal refinement on π0.5.\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.835, \\\"benchmark\\\": \\\"object\\\", \\\"mode\\\": \\\"adaptive_conformal_crm\\\", \\\"seed\\\": 42, \\\"model\\\": \\\"pi05\\\", \\\"n_rollouts\\\": 20, \\\"n_tasks\\\": 10}, \\\"conclusion\\\": \\\"success\\\"}, \\\"westd-pi05-adaptive-goal-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-26T04:19:43.389Z\\\", \\\"updated_at\\\": \\\"2026-05-26T10:51:54.441Z\\\", \\\"hypothesis\\\": \\\"π0.5 Adaptive Conformal CRM (K=2, τ=0.25, ε=0.2) on LIBERO-Goal s43. Seed variation for 3-seed mean±std on Goal benchmark.\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.875, \\\"benchmark\\\": \\\"goal\\\", \\\"mode\\\": \\\"adaptive_conformal_crm\\\", \\\"seed\\\": 43, \\\"model\\\": \\\"pi05\\\", \\\"n_rollouts\\\": 20, \\\"n_tasks\\\": 10}, \\\"conclusion\\\": \\\"success\\\"}, \\\"westd-pi05-adaptive-goal-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-26T04:19:38.990Z\\\", \\\"updated_at\\\": \\\"2026-05-26T10:51:37.558Z\\\", \\\"hypothesis\\\": \\\"π0.5 Adaptive Conformal CRM (K=2, τ=0.25, ε=0.2) on LIBERO-Goal s42. Tests whether adaptive conformal refinement improves π0.5 on goal-conditioned tasks.\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.88, \\\"benchmark\\\": \\\"goal\\\", \\\"mode\\\": \\\"adaptive_conformal_crm\\\", \\\"seed\\\": 42, \\\"model\\\": \\\"pi05\\\", \\\"n_rollouts\\\": 20, \\\"n_tasks\\\": 10}, \\\"conclusion\\\": \\\"success\\\"}, \\\"pi05-adaptive-long-s42-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-26T03:44:44.161Z\\\", \\\"updated_at\\\": \\\"2026-05-26T10:50:49.947Z\\\", \\\"hypothesis\\\": \\\"π0.5 Adaptive Conformal on Long s42 (re-run after cqa1 crash). Cross-suite validation for π0.5 Table 2.\\\"}, \\\"pi05-crm-k2-long-s43-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-26T03:44:25.674Z\\\", \\\"updated_at\\\": \\\"2026-05-26T10:50:36.087Z\\\", \\\"hypothesis\\\": \\\"π0.5 CRM K=2 obs_only on LIBERO-Long s43 (re-run after server restart). Tests whether CRM correction affects strong π0.5 baseline on long-horizon tasks.\\\", \\\"parent\\\": \\\"pi05-crm-k2-long-s43\\\"}, \\\"pi05-crm-k2-long-s42-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-26T03:44:17.432Z\\\", \\\"updated_at\\\": \\\"2026-05-26T10:50:28.060Z\\\", \\\"hypothesis\\\": \\\"π0.5 CRM K=2 obs_only on LIBERO-Long s42 (re-run after server restart). Tests whether CRM correction affects strong π0.5 baseline on long-horizon tasks.\\\", \\\"parent\\\": \\\"pi05-crm-k2-long-s42\\\"}, \\\"pi05-adaptive-object-s44-cqa1-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-26T09:44:50.881Z\\\", \\\"updated_at\\\": \\\"2026-05-26T10:30:10.213Z\\\", \\\"hypothesis\\\": \\\"π0.5 Adaptive Conformal CRM (K=2, τ=0.25) on Object s44. Table 2 cross-architecture gating analysis. Re-run after cqa1 node-level tmux cleanup.\\\", \\\"parent\\\": \\\"pi05-adaptive-object-s44-cqa1\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"pi05-adaptive-goal-s43-bjb1-18228\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-26T06:45:32.801Z\\\", \\\"updated_at\\\": \\\"2026-05-26T10:24:06.070Z\\\", \\\"hypothesis\\\": \\\"π0.5 Adaptive Conformal CRM (K=2, τ=0.25, ε=0.2) on Goal s43. 4090 cluster cross-validation for westd Goal s43, controlling Blackwell architecture bias.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 89.5}}, \\\"pi05-adaptive-goal-s44-cqa1-r2\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-26T10:19:04.430Z\\\", \\\"updated_at\\\": \\\"2026-05-26T10:19:04.430Z\\\"}, \\\"pi05-adaptive-goal-s43-cqa1-r2\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-26T10:18:49.165Z\\\", \\\"updated_at\\\": \\\"2026-05-26T10:18:49.165Z\\\"}, \\\"pi05-crm-k2-long-s42-bjb1\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-26T10:18:13.260Z\\\", \\\"updated_at\\\": \\\"2026-05-26T10:18:13.260Z\\\", \\\"hypothesis\\\": \\\"π0.5 CRM K=2 obs_only (always-on, ε=0.05) on Long s42. Table 2 long-horizon CRM impact with near-expert VLA on bjb1-18228.\\\"}, \\\"pi05-adaptive-object-s43-bjb1\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-26T10:18:05.197Z\\\", \\\"updated_at\\\": \\\"2026-05-26T10:18:05.197Z\\\", \\\"hypothesis\\\": \\\"π0.5 Adaptive Conformal CRM (K=2, τ=0.25) on Object s43. Table 2 cross-architecture gating analysis on bjb1-18228.\\\"}, \\\"pi05-adaptive-spatial-s44-bjb2-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-26T09:55:47.784Z\\\", \\\"updated_at\\\": \\\"2026-05-26T10:00:04.376Z\\\", \\\"hypothesis\\\": \\\"π0.5 Adaptive Conformal CRM (K=2, τ=0.25) on Spatial s44. Table 2 cross-architecture gating analysis. Re-run after bjb2-28827 node-level tmux cleanup.\\\"}, \\\"pi05-adaptive-spatial-s43-bjb2-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-26T09:55:43.728Z\\\", \\\"updated_at\\\": \\\"2026-05-26T09:59:15.673Z\\\", \\\"hypothesis\\\": \\\"π0.5 Adaptive Conformal CRM (K=2, τ=0.25) on Spatial s43. Table 2 cross-architecture gating analysis. Re-run after bjb2-28827 node-level tmux cleanup.\\\"}, \\\"pi05-adaptive-spatial-s42-bjb2-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-26T09:55:39.703Z\\\", \\\"updated_at\\\": \\\"2026-05-26T09:58:46.516Z\\\", \\\"hypothesis\\\": \\\"π0.5 Adaptive Conformal CRM (K=2, τ=0.25) on Spatial s42. Table 2 cross-architecture gating analysis. Re-run after bjb2-28827 node-level tmux cleanup.\\\"}, \\\"pi05-crm-k2-spatial-s44-bjb2-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-26T09:55:35.735Z\\\", \\\"updated_at\\\": \\\"2026-05-26T09:58:10.616Z\\\", \\\"hypothesis\\\": \\\"π0.5 CRM K=2 obs_only (always-on, ε=0.05) on Spatial s44. Table 2 cross-architecture CRM impact. Re-run after bjb2-28827 node-level tmux cleanup.\\\"}, \\\"pi05-crm-k2-spatial-s43-bjb2-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-26T09:55:31.701Z\\\", \\\"updated_at\\\": \\\"2026-05-26T09:57:41.093Z\\\", \\\"hypothesis\\\": \\\"π0.5 CRM K=2 obs_only (always-on, ε=0.05) on Spatial s43. Table 2 cross-architecture CRM impact. Re-run after bjb2-28827 node-level tmux cleanup.\\\"}, \\\"pi05-crm-k2-spatial-s42-bjb2-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-26T09:55:27.403Z\\\", \\\"updated_at\\\": \\\"2026-05-26T09:57:13.362Z\\\", \\\"hypothesis\\\": \\\"π0.5 CRM K=2 obs_only (always-on, ε=0.05) on Spatial s42. Table 2 cross-architecture CRM impact. Re-run after bjb2-28827 node-level tmux cleanup.\\\"}, \\\"pi05-crm-k2-object-s44-bjb1-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-26T09:44:46.771Z\\\", \\\"updated_at\\\": \\\"2026-05-26T09:53:09.173Z\\\", \\\"hypothesis\\\": \\\"π0.5 CRM K=2 obs_only (always-on, ε=0.05) on Object s44. Table 2 cross-architecture CRM impact with near-expert VLA. Re-run after bjb1-32546 node-level tmux cleanup.\\\", \\\"parent\\\": \\\"pi05-crm-k2-object-s44-bjb1\\\"}, \\\"pi05-crm-k2-object-s43-bjb1-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-26T09:44:42.092Z\\\", \\\"updated_at\\\": \\\"2026-05-26T09:53:00.538Z\\\", \\\"hypothesis\\\": \\\"π0.5 CRM K=2 obs_only (always-on, ε=0.05) on Object s43. Table 2 cross-architecture CRM impact with near-expert VLA. Re-run after bjb1-32546 node-level tmux cleanup.\\\", \\\"parent\\\": \\\"pi05-crm-k2-object-s43-bjb1\\\"}, \\\"pi05-crm-k2-object-s42-bjb1-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-26T09:44:37.659Z\\\", \\\"updated_at\\\": \\\"2026-05-26T09:52:52.585Z\\\", \\\"hypothesis\\\": \\\"π0.5 CRM K=2 obs_only (always-on, ε=0.05) on Object s42. Table 2 cross-architecture CRM impact with near-expert VLA. Re-run after bjb1-32546 node-level tmux cleanup.\\\", \\\"parent\\\": \\\"pi05-crm-k2-object-s42-bjb1\\\"}, \\\"pi05-crm-k2-goal-s44-bjb1-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-26T09:44:33.740Z\\\", \\\"updated_at\\\": \\\"2026-05-26T09:52:44.965Z\\\", \\\"hypothesis\\\": \\\"π0.5 CRM K=2 obs_only (always-on, ε=0.05) on Goal s44. Table 2 cross-architecture CRM impact with near-expert VLA. Re-run after bjb1-32546 node-level tmux cleanup.\\\", \\\"parent\\\": \\\"pi05-crm-k2-goal-s44-bjb1\\\"}, \\\"pi05-crm-k2-goal-s43-bjb1-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-26T09:44:29.605Z\\\", \\\"updated_at\\\": \\\"2026-05-26T09:52:37.286Z\\\", \\\"hypothesis\\\": \\\"π0.5 CRM K=2 obs_only (always-on, ε=0.05) on Goal s43. Table 2 cross-architecture CRM impact with near-expert VLA. Re-run after bjb1-32546 node-level tmux cleanup.\\\", \\\"parent\\\": \\\"pi05-crm-k2-goal-s43-bjb1\\\"}}, \\\"count\\\": 50, \\\"total\\\": 1205, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 6.8322}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"westd-pi05-vla-only-goal-s44-paired\": {\"status\": \"ANALYZING\", \"created_at\": \"2026-05-26T11:02:01.323Z\", \"updated_at\": \"2026-05-26T12:06:09.890Z\", \"hypothesis\": \"π0.5 VLA-only baseline on Goal s44 (westd same-server paired). Blackwell paired comparison for cross-hardware validation.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.955, \"n_rollouts\": 20, \"n_tasks\": 10, \"per_task_min\": 0.8, \"per_task_max\": 1}}, \"westd-pi05-vla-only-goal-s43-paired\": {\"status\": \"ANALYZING\", \"created_at\": \"2026-05-26T11:01:46.159Z\", \"updated_at\": \"2026-05-26T12:06:00.139Z\", \"hypothesis\": \"π0.5 VLA-only baseline on Goal s43 (westd same-server paired). Blackwell paired comparison for cross-hardware validation.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.965, \"n_rollouts\": 20, \"n_tasks\": 10, \"per_task_min\": 0.85, \"per_task_max\": 1}}, \"westd-pi05-vla-only-goal-s42-paired\": {\"status\": \"ANALYZING\", \"created_at\": \"2026-05-26T11:01:32.135Z\", \"updated_at\": \"2026-05-26T12:05:54.118Z\", \"hypothesis\": \"π0.5 VLA-only baseline on Goal s42 (westd same-server paired). Blackwell paired comparison for cross-hardware validation.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.975, \"n_rollouts\": 20, \"n_tasks\": 10, \"per_task_min\": 0.9, \"per_task_max\": 1}}, \"westd-pi05-vla-only-object-s44-paired\": {\"status\": \"DONE\", \"created_at\": \"2026-05-26T11:02:45.036Z\", \"updated_at\": \"2026-05-26T12:05:45.887Z\", \"hypothesis\": \"π0.5 VLA-only baseline on Object s44. westd same-server paired comparison (Blackwell).\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.995, \"n_rollouts\": 20, \"n_tasks\": 10, \"per_task_min\": 0.95, \"per_task_max\": 1}}, \"westd-pi05-vla-only-object-s43-paired\": {\"status\": \"DONE\", \"created_at\": \"2026-05-26T11:02:30.548Z\", \"updated_at\": \"2026-05-26T12:05:32.934Z\", \"hypothesis\": \"π0.5 VLA-only baseline on Object s43 (westd same-server paired). Blackwell paired comparison for cross-hardware validation.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 1, \"n_rollouts\": 20, \"n_tasks\": 10, \"per_task_min\": 1, \"per_task_max\": 1}}, \"westd-pi05-vla-only-object-s42-paired\": {\"status\": \"DONE\", \"created_at\": \"2026-05-26T11:02:15.888Z\", \"updated_at\": \"2026-05-26T12:05:22.121Z\", \"hypothesis\": \"π0.5 VLA-only baseline on Object s42 (westd same-server paired). Blackwell paired comparison for cross-hardware validation.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.995, \"n_rollouts\": 20, \"n_tasks\": 10, \"per_task_min\": 0.95, \"per_task_max\": 1}}, \"pi05-adaptive-object-s42-cqa1\": {\"status\": \"ANALYZING\", \"created_at\": \"2026-05-26T06:53:47.761Z\", \"updated_at\": \"2026-05-26T12:05:13.994Z\", \"hypothesis\": \"π0.5 Adaptive Conformal CRM on Object s42. 4090 cluster backup for westd result, controlling Blackwell architecture bias.\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.855, \"n_rollouts\": 20, \"n_tasks\": 10, \"trigger_rate\": 0.037, \"mean_uncertainty\": 0.0842, \"conformal_threshold\": 0.25, \"max_correction_norm\": 0.2, \"per_task_min\": 0.5, \"per_task_max\": 1}}, \"westd-pi05-vla-only-long-s44-paired\": {\"status\": \"QUEUED\", \"created_at\": \"2026-05-26T12:00:13.951Z\", \"updated_at\": \"2026-05-26T12:03:51.023Z\", \"hypothesis\": \"π0.5 VLA-only baseline on Long s44. westd same-server paired comparison (Blackwell). Fills Table 2 Long VLA-only gap.\"}, \"westd-pi05-vla-only-long-s43-paired\": {\"status\": \"QUEUED\", \"created_at\": \"2026-05-26T12:00:43.452Z\", \"updated_at\": \"2026-05-26T12:03:13.221Z\", \"hypothesis\": \"π0.5 VLA-only baseline on Long s43. westd same-server paired comparison (Blackwell). Complete Long VLA-only 3-seed coverage.\"}, \"westd-pi05-vla-only-long-s42-paired\": {\"status\": \"QUEUED\", \"created_at\": \"2026-05-26T11:59:43.428Z\", \"updated_at\": \"2026-05-26T12:02:38.770Z\", \"hypothesis\": \"π0.5 VLA-only baseline on Long s42. westd same-server paired comparison (Blackwell). Fills Table 2 Long VLA-only gap.\"}, \"westd-pi05-vla-only-spatial-s44-paired\": {\"status\": \"QUEUED\", \"created_at\": \"2026-05-26T11:59:17.322Z\", \"updated_at\": \"2026-05-26T12:02:04.265Z\", \"hypothesis\": \"π0.5 VLA-only baseline on Spatial s44. westd same-server paired comparison (Blackwell). Fills Table 2 Spatial VLA-only gap.\"}, \"westd-pi05-vla-only-spatial-s43-paired\": {\"status\": \"QUEUED\", \"created_at\": \"2026-05-26T11:58:45.293Z\", \"updated_at\": \"2026-05-26T12:01:29.386Z\", \"hypothesis\": \"π0.5 VLA-only baseline on Spatial s43. westd same-server paired comparison (Blackwell). Fills Table 2 Spatial VLA-only gap.\"}, \"westd-pi05-vla-only-spatial-s42-paired\": {\"status\": \"QUEUED\", \"created_at\": \"2026-05-26T11:56:11.874Z\", \"updated_at\": \"2026-05-26T11:58:06.007Z\", \"hypothesis\": \"π0.5 VLA-only baseline on Spatial s42. westd same-server paired comparison (Blackwell). Fills Table 2 Spatial VLA-only gap.\"}, \"pi05-adaptive-object-s43-bjb2-24035\": {\"status\": \"DONE\", \"created_at\": \"2026-05-26T10:51:28.267Z\", \"updated_at\": \"2026-05-26T11:57:37.320Z\", \"hypothesis\": \"π0.5 Adaptive Conformal CRM (K=2, τ=0.25) on Object s43. Table 2 cross-architecture gating analysis. Tests adaptive gating on Object suite.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.83, \"benchmark\": \"object\", \"mode\": \"adaptive_conformal_crm\", \"seed\": 43, \"model\": \"pi05\", \"n_rollouts\": 20, \"n_tasks\": 10}}, \"pi05-adaptive-long-s44-cqa1-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-26T09:44:58.714Z\", \"updated_at\": \"2026-05-26T11:35:01.941Z\", \"hypothesis\": \"π0.5 Adaptive Conformal CRM (K=2, τ=0.25) on Long s44. Table 2 long-horizon cross-architecture analysis. Re-run after cqa1 node-level tmux cleanup.\", \"parent\": \"pi05-adaptive-long-s44-cqa1\", \"metrics\": {\"success_rate\": 0, \"trigger_rate\": null, \"benchmark\": \"long\", \"mode\": \"adaptive_conformal_crm\", \"seed\": 44, \"model\": \"pi05\", \"n_rollouts\": 20, \"n_tasks\": 10, \"error\": \"CUDA OOM at step 0 of every rollout\", \"successes\": 0, \"total\": 200}, \"conclusion\": \"failed\"}, \"pi05-adaptive-long-s43-cqa1-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-26T09:44:54.814Z\", \"updated_at\": \"2026-05-26T11:34:57.651Z\", \"hypothesis\": \"π0.5 Adaptive Conformal CRM (K=2, τ=0.25) on Long s43. Table 2 long-horizon cross-architecture analysis. Re-run after cqa1 node-level tmux cleanup.\", \"parent\": \"pi05-adaptive-long-s43-cqa1\", \"metrics\": {\"success_rate\": 0, \"trigger_rate\": null, \"benchmark\": \"long\", \"mode\": \"adaptive_conformal_crm\", \"seed\": 43, \"model\": \"pi05\", \"n_rollouts\": 20, \"n_tasks\": 10, \"error\": \"CUDA OOM at step 0 of every rollout\", \"successes\": 0, \"total\": 200}, \"conclusion\": \"failed\"}, \"pi05-adaptive-object-s43-cqa1-r3\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-26T11:29:55.374Z\", \"updated_at\": \"2026-05-26T11:31:13.727Z\", \"hypothesis\": \"π0.5 Adaptive Conformal (τ=0.25, K=2, max_correction_norm=0.2) on Object s43. Re-run after bjb2-24035 process death. Table 2 cross-suite validation.\", \"parent\": \"pi05-adaptive-object-s43-bjb2-24035\"}, \"pi05-adaptive-goal-s42-cqa1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-26T06:53:55.121Z\", \"updated_at\": \"2026-05-26T11:28:57.790Z\", \"hypothesis\": \"π0.5 Adaptive Conformal CRM on Goal s42. 4090 cluster backup for westd result, controlling Blackwell architecture bias.\", \"metrics\": {\"success_rate\": 0.895, \"success_count\": 179, \"total_rollouts\": 200, \"trigger_rate\": 0.081, \"mean_unc\": 0.1152, \"benchmark\": \"goal\", \"mode\": \"adaptive_conformal_crm\", \"seed\": 42, \"model\": \"pi05\", \"n_rollouts\": 20, \"n_tasks\": 10, \"K\": 2, \"max_correction_norm\": 0.2, \"conformal_threshold\": 0.25, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.7, \"put_the_bowl_on_the_stove\": 0.95, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.85, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.7, \"put_the_bowl_on_top_of_the_cabinet\": 1, \"push_the_plate_to_the_front_of_the_stove\": 1, \"put_the_cream_cheese_in_the_bowl\": 0.9, \"turn_on_the_stove\": 1, \"put_the_bowl_on_the_plate\": 1, \"put_the_wine_bottle_on_the_rack\": 0.85}}, \"conclusion\": \"success\"}, \"pi05-adaptive-long-s44-cqa1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-26T05:53:43.686Z\", \"updated_at\": \"2026-05-26T11:26:44.982Z\", \"hypothesis\": \"π0.5 Adaptive Conformal on Long s44. Table 2 long-horizon cross-architecture analysis.\", \"conclusion\": \"killed\", \"notes\": \"失败原因(初步): cqa1 上 6 个 π0.5 并发导致 OOM (已知模式)。reconcile 自动标记 failed。Worker 深查中。\"}, \"pi05-adaptive-long-s43-cqa1\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-26T05:53:07.701Z\", \"updated_at\": \"2026-05-26T11:26:37.267Z\", \"hypothesis\": \"π0.5 Adaptive Conformal on Long s43. Table 2 long-horizon cross-architecture analysis.\", \"notes\": \"失败原因(初步): cqa1 上 6 个 π0.5 并发导致 OOM (已知模式)。reconcile 自动标记 failed。Worker 深查中。\", \"conclusion\": \"killed\"}, \"pi05-adaptive-object-s44-cqa1\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-26T05:52:41.664Z\", \"updated_at\": \"2026-05-26T11:26:29.402Z\", \"hypothesis\": \"π0.5 Adaptive Conformal on Object s44. Table 2 cross-suite validation.\", \"notes\": \"失败原因(初步): cqa1 上 6 个 π0.5 并发导致 OOM (已知模式)。日志文件不存在，进程被 kill 前未写 output。Worker 深查中。\", \"conclusion\": \"killed\"}, \"pi05-adaptive-goal-s44-bjb1\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-26T10:18:00.006Z\", \"updated_at\": \"2026-05-26T11:23:06.585Z\", \"hypothesis\": \"π0.5 Adaptive Conformal (τ=0.25, K=2, max_correction_norm=0.2) on Goal s44. Table 2 paired comparison with CRM K=2 and VLA-only on same server.\"}, \"pi05-adaptive-goal-s44-bjb1-18228\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-26T11:08:38.962Z\", \"updated_at\": \"2026-05-26T11:08:38.962Z\"}, \"pi05-adaptive-long-s44-cqa1-r3\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-26T10:53:38.703Z\", \"updated_at\": \"2026-05-26T10:58:02.641Z\", \"hypothesis\": \"π0.5 Adaptive Conformal CRM (K=2, τ=0.25) on Long s44. r3 re-run after r2 OOM (zombie process collision). Clean GPU confirms adaptive fits in 24GB on single process.\", \"parent\": \"pi05-adaptive-long-s44-cqa1-r2\"}, \"pi05-adaptive-long-s43-cqa1-r3\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-26T10:53:20.461Z\", \"updated_at\": \"2026-05-26T10:57:13.677Z\", \"hypothesis\": \"π0.5 Adaptive Conformal CRM (K=2, τ=0.25) on Long s43. r3 re-run after r2 OOM (zombie process collision). Clean GPU confirms adaptive fits in 24GB on single process.\", \"parent\": \"pi05-adaptive-long-s43-cqa1-r2\"}, \"pi05-adaptive-object-s44-cqa1-r3\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-26T10:53:53.430Z\", \"updated_at\": \"2026-05-26T10:56:25.007Z\", \"hypothesis\": \"π0.5 Adaptive Conformal CRM (K=2, τ=0.25) on Object s44. r3 re-run after r2 GPU collision (double-process on GPU 3). Table 2 cross-architecture gating.\", \"parent\": \"pi05-adaptive-object-s44-cqa1-r2\"}, \"westd-pi05-crm-k2-goal-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-26T04:26:05.028Z\", \"updated_at\": \"2026-05-26T10:52:23.271Z\", \"hypothesis\": \"π0.5 CRM obs_only K=2 (ε=0.05, always-on) on LIBERO-Goal s42. Tests whether unconditional CRM correction (no adaptive gating) helps π0.5 on goal suite. Comparison vs adaptive gating and K=2 mean baseline.\", \"metrics\": {\"success_rate\": 0.855, \"benchmark\": \"goal\", \"mode\": \"crm_obs_only\", \"seed\": 42, \"K\": 2, \"model\": \"pi05\", \"n_rollouts\": 20, \"n_tasks\": 10}, \"conclusion\": \"success\"}, \"westd-pi05-adaptive-object-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-26T04:19:53.085Z\", \"updated_at\": \"2026-05-26T10:52:12.970Z\", \"hypothesis\": \"π0.5 Adaptive Conformal CRM (K=2, τ=0.25, ε=0.2) on LIBERO-Object s42. Cross-suite validation of adaptive conformal refinement on π0.5.\", \"metrics\": {\"success_rate\": 0.835, \"benchmark\": \"object\", \"mode\": \"adaptive_conformal_crm\", \"seed\": 42, \"model\": \"pi05\", \"n_rollouts\": 20, \"n_tasks\": 10}, \"conclusion\": \"success\"}, \"westd-pi05-adaptive-goal-s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-26T04:19:43.389Z\", \"updated_at\": \"2026-05-26T10:51:54.441Z\", \"hypothesis\": \"π0.5 Adaptive Conformal CRM (K=2, τ=0.25, ε=0.2) on LIBERO-Goal s43. Seed variation for 3-seed mean±std on Goal benchmark.\", \"metrics\": {\"success_rate\": 0.875, \"benchmark\": \"goal\", \"mode\": \"adaptive_conformal_crm\", \"seed\": 43, \"model\": \"pi05\", \"n_rollouts\": 20, \"n_tasks\": 10}, \"conclusion\": \"success\"}, \"westd-pi05-adaptive-goal-s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-26T04:19:38.990Z\", \"updated_at\": \"2026-05-26T10:51:37.558Z\", \"hypothesis\": \"π0.5 Adaptive Conformal CRM (K=2, τ=0.25, ε=0.2) on LIBERO-Goal s42. Tests whether adaptive conformal refinement improves π0.5 on goal-conditioned tasks.\", \"metrics\": {\"success_rate\": 0.88, \"benchmark\": \"goal\", \"mode\": \"adaptive_conformal_crm\", \"seed\": 42, \"model\": \"pi05\", \"n_rollouts\": 20, \"n_tasks\": 10}, \"conclusion\": \"success\"}, \"pi05-adaptive-long-s42-r2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-26T03:44:44.161Z\", \"updated_at\": \"2026-05-26T10:50:49.947Z\", \"hypothesis\": \"π0.5 Adaptive Conformal on Long s42 (re-run after cqa1 crash). Cross-suite validation for π0.5 Table 2.\"}, \"pi05-crm-k2-long-s43-r2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-26T03:44:25.674Z\", \"updated_at\": \"2026-05-26T10:50:36.087Z\", \"hypothesis\": \"π0.5 CRM K=2 obs_only on LIBERO-Long s43 (re-run after server restart). Tests whether CRM correction affects strong π0.5 baseline on long-horizon tasks.\", \"parent\": \"pi05-crm-k2-long-s43\"}, \"pi05-crm-k2-long-s42-r2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-26T03:44:17.432Z\", \"updated_at\": \"2026-05-26T10:50:28.060Z\", \"hypothesis\": \"π0.5 CRM K=2 obs_only on LIBERO-Long s42 (re-run after server restart). Tests whether CRM correction affects strong π0.5 baseline on long-horizon tasks.\", \"parent\": \"pi05-crm-k2-long-s42\"}, \"pi05-adaptive-object-s44-cqa1-r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-26T09:44:50.881Z\", \"updated_at\": \"2026-05-26T10:30:10.213Z\", \"hypothesis\": \"π0.5 Adaptive Conformal CRM (K=2, τ=0.25) on Object s44. Table 2 cross-architecture gating analysis. Re-run after cqa1 node-level tmux cleanup.\", \"parent\": \"pi05-adaptive-object-s44-cqa1\", \"conclusion\": \"failed\"}, \"pi05-adaptive-goal-s43-bjb1-18228\": {\"status\": \"DONE\", \"created_at\": \"2026-05-26T06:45:32.801Z\", \"updated_at\": \"2026-05-26T10:24:06.070Z\", \"hypothesis\": \"π0.5 Adaptive Conformal CRM (K=2, τ=0.25, ε=0.2) on Goal s43. 4090 cluster cross-validation for westd Goal s43, controlling Blackwell architecture bias.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 89.5}}, \"pi05-adaptive-goal-s44-cqa1-r2\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-26T10:19:04.430Z\", \"updated_at\": \"2026-05-26T10:19:04.430Z\"}, \"pi05-adaptive-goal-s43-cqa1-r2\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-26T10:18:49.165Z\", \"updated_at\": \"2026-05-26T10:18:49.165Z\"}, \"pi05-crm-k2-long-s42-bjb1\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-26T10:18:13.260Z\", \"updated_at\": \"2026-05-26T10:18:13.260Z\", \"hypothesis\": \"π0.5 CRM K=2 obs_only (always-on, ε=0.05) on Long s42. Table 2 long-horizon CRM impact with near-expert VLA on bjb1-18228.\"}, \"pi05-adaptive-object-s43-bjb1\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-26T10:18:05.197Z\", \"updated_at\": \"2026-05-26T10:18:05.197Z\", \"hypothesis\": \"π0.5 Adaptive Conformal CRM (K=2, τ=0.25) on Object s43. Table 2 cross-architecture gating analysis on bjb1-18228.\"}, \"pi05-adaptive-spatial-s44-bjb2-r2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-26T09:55:47.784Z\", \"updated_at\": \"2026-05-26T10:00:04.376Z\", \"hypothesis\": \"π0.5 Adaptive Conformal CRM (K=2, τ=0.25) on Spatial s44. Table 2 cross-architecture gating analysis. Re-run after bjb2-28827 node-level tmux cleanup.\"}, \"pi05-adaptive-spatial-s43-bjb2-r2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-26T09:55:43.728Z\", \"updated_at\": \"2026-05-26T09:59:15.673Z\", \"hypothesis\": \"π0.5 Adaptive Conformal CRM (K=2, τ=0.25) on Spatial s43. Table 2 cross-architecture gating analysis. Re-run after bjb2-28827 node-level tmux cleanup.\"}, \"pi05-adaptive-spatial-s42-bjb2-r2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-26T09:55:39.703Z\", \"updated_at\": \"2026-05-26T09:58:46.516Z\", \"hypothesis\": \"π0.5 Adaptive Conformal CRM (K=2, τ=0.25) on Spatial s42. Table 2 cross-architecture gating analysis. Re-run after bjb2-28827 node-level tmux cleanup.\"}, \"pi05-crm-k2-spatial-s44-bjb2-r2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-26T09:55:35.735Z\", \"updated_at\": \"2026-05-26T09:58:10.616Z\", \"hypothesis\": \"π0.5 CRM K=2 obs_only (always-on, ε=0.05) on Spatial s44. Table 2 cross-architecture CRM impact. Re-run after bjb2-28827 node-level tmux cleanup.\"}, \"pi05-crm-k2-spatial-s43-bjb2-r2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-26T09:55:31.701Z\", \"updated_at\": \"2026-05-26T09:57:41.093Z\", \"hypothesis\": \"π0.5 CRM K=2 obs_only (always-on, ε=0.05) on Spatial s43. Table 2 cross-architecture CRM impact. Re-run after bjb2-28827 node-level tmux cleanup.\"}, \"pi05-crm-k2-spatial-s42-bjb2-r2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-26T09:55:27.403Z\", \"updated_at\": \"2026-05-26T09:57:13.362Z\", \"hypothesis\": \"π0.5 CRM K=2 obs_only (always-on, ε=0.05) on Spatial s42. Table 2 cross-architecture CRM impact. Re-run after bjb2-28827 node-level tmux cleanup.\"}, \"pi05-crm-k2-object-s44-bjb1-r2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-26T09:44:46.771Z\", \"updated_at\": \"2026-05-26T09:53:09.173Z\", \"hypothesis\": \"π0.5 CRM K=2 obs_only (always-on, ε=0.05) on Object s44. Table 2 cross-architecture CRM impact with near-expert VLA. Re-run after bjb1-32546 node-level tmux cleanup.\", \"parent\": \"pi05-crm-k2-object-s44-bjb1\"}, \"pi05-crm-k2-object-s43-bjb1-r2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-26T09:44:42.092Z\", \"updated_at\": \"2026-05-26T09:53:00.538Z\", \"hypothesis\": \"π0.5 CRM K=2 obs_only (always-on, ε=0.05) on Object s43. Table 2 cross-architecture CRM impact with near-expert VLA. Re-run after bjb1-32546 node-level tmux cleanup.\", \"parent\": \"pi05-crm-k2-object-s43-bjb1\"}, \"pi05-crm-k2-object-s42-bjb1-r2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-26T09:44:37.659Z\", \"updated_at\": \"2026-05-26T09:52:52.585Z\", \"hypothesis\": \"π0.5 CRM K=2 obs_only (always-on, ε=0.05) on Object s42. Table 2 cross-architecture CRM impact with near-expert VLA. Re-run after bjb1-32546 node-level tmux cleanup.\", \"parent\": \"pi05-crm-k2-object-s42-bjb1\"}, \"pi05-crm-k2-goal-s44-bjb1-r2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-26T09:44:33.740Z\", \"updated_at\": \"2026-05-26T09:52:44.965Z\", \"hypothesis\": \"π0.5 CRM K=2 obs_only (always-on, ε=0.05) on Goal s44. Table 2 cross-architecture CRM impact with near-expert VLA. Re-run after bjb1-32546 node-level tmux cleanup.\", \"parent\": \"pi05-crm-k2-goal-s44-bjb1\"}, \"pi05-crm-k2-goal-s43-bjb1-r2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-26T09:44:29.605Z\", \"updated_at\": \"2026-05-26T09:52:37.286Z\", \"hypothesis\": \"π0.5 CRM K=2 obs_only (always-on, ε=0.05) on Goal s43. Table 2 cross-architecture CRM impact with near-expert VLA. Re-run after bjb1-32546 node-level tmux cleanup.\", \"parent\": \"pi05-crm-k2-goal-s43-bjb1\"}}, \"count\": 50, \"total\": 1205, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 6.8322}}"
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
The registry already has these 3 experiments with status DONE and correct metrics. Let me verify the data:

Registry already shows:
- westd-pi05-vla-only-object-s42-paired: status=DONE, conclusion=success, metrics={overall_success_rate: 0.995}
- westd-pi05-vla-only-object-s43-paired: status=DONE, conclusion=success, metrics={overall_success_rate: 1.0}


- westd-pi05-vla-only-object-s44-paired: status=DONE, conclusion=success, metrics={overall_success_rate: 0.995}

All three match the JSON files exactly. Now I'm looking at other π0.5 Object VLA-only results to see how these compare—I can find adaptive conformal variants with lower success rates around 0.835-0.855, but I'm not seeing other non-adaptive VLA-only configurations in the registry.

Let me verify whether the checkpoint and log paths are properly populated in the registry records, since the task requires updating those fields.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eb7c021e-380a-410b-a199-64af6b82580d",
  "uuid": "4c87a73c-5a72-490b-84f1-0d52a00f4102",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MV5yDVaAZUmXpjuVQT391v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9062,
      "cache_read_input_tokens": 30138,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9062
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

Registry already has these 3 experiments as DONE. Let me verify checkpoint_path and log_path are set.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eb7c021e-380a-410b-a199-64af6b82580d",
  "uuid": "3ce36574-e6b3-4bd6-975f-8f851c631ab9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MV5yDVaAZUmXpjuVQT391v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9062,
      "cache_read_input_tokens": 30138,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9062
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01LXjfVboAjB8Pv4JhYa8R9D`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": {
    "exp_id": "westd-pi05-vla-only-object-s42-paired"
  },
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
  "session_id": "eb7c021e-380a-410b-a199-64af6b82580d",
  "uuid": "3069130d-2430-42b1-9f3b-997da936c9e9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MV5yDVaAZUmXpjuVQT391v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9062,
      "cache_read_input_tokens": 30138,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9062
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01YX4WhXp77oa8ppgWe4n3GG`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": {
    "exp_id": "westd-pi05-vla-only-object-s43-paired"
  },
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
  "session_id": "eb7c021e-380a-410b-a199-64af6b82580d",
  "uuid": "afe18a37-156e-4da7-af4d-dabac90cc0cd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MV5yDVaAZUmXpjuVQT391v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9062,
      "cache_read_input_tokens": 30138,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9062
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_011r2Yqa6SkFnWWpGeQERKT9`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": {
    "exp_id": "westd-pi05-vla-only-object-s44-paired"
  },
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
  "session_id": "eb7c021e-380a-410b-a199-64af6b82580d",
  "uuid": "eac1153b-46d8-4079-92f9-fa5bcff2856e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MV5yDVaAZUmXpjuVQT391v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9062,
      "cache_read_input_tokens": 30138,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9062
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

_source line 35 · 2026-05-26T12:06:43.349Z_

<details><summary>↩ Tool result · `toolu_01LXjfVboAjB8Pv4JhYa8R9D`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.7129}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eb7c021e-380a-410b-a199-64af6b82580d",
  "uuid": "fc909ca2-21c1-40e8-8d71-c0295a8ba098",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 9.7129}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.7129}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-26T12:06:52.243Z_

<details><summary>↩ Tool result · `toolu_01YX4WhXp77oa8ppgWe4n3GG`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 8.8573}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eb7c021e-380a-410b-a199-64af6b82580d",
  "uuid": "0615ca00-15f0-42af-ae92-2e3f79b4b8a9",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 8.8573}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 8.8573}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-26T12:06:59.137Z_

<details><summary>↩ Tool result · `toolu_011r2Yqa6SkFnWWpGeQERKT9`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 6.8721}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eb7c021e-380a-410b-a199-64af6b82580d",
  "uuid": "53bd2959-2656-455f-b44a-5d4013ad1981",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 6.8721}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 6.8721}}"
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
The filter by exp_id returns 0 results - likely the filter syntax doesn't support exact match on exp_id that way. But from the broad read_registry call, I can see these experiments exist and have:

- westd-pi05-vla-only-object-s42-paired: status=DONE, conclusion=success, metrics={overall_success_rate: 0.995, n_rollouts: 20, n_tasks: 10, per_task_min: 0.95, per_task_max: 1}


- westd-pi05-vla-only-object-s43-paired: status=DONE, conclusion=success, metrics={overall_success_rate: 1, n_rollouts: 20, n_tasks: 10, per_task_min: 1, per_task_max: 1}
- westd-pi05-vla-only-object-s44-paired: status=DONE, conclusion=success, metrics={overall_success_rate: 0.995, n_rollouts: 20, n_tasks: 10, per_task_min: 0.95, per_task_max: 1}

I notice the summary fields don't include checkpoint_path or log_path, so I need to update those separately. Now I'm computing the aggregate statistics across the three seeds—the mean success rate comes out to about 0.9967 with a standard deviation I'm calculating from the individual seed values.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eb7c021e-380a-410b-a199-64af6b82580d",
  "uuid": "1f388aee-c1a2-4dac-a388-4ee59630addd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016xZTePbmCnnsjFi4Dwu19B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1049,
      "cache_read_input_tokens": 39200,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1049
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

Registry already has these experiments as DONE with correct metrics. Updating checkpoint_path and log_path for all 3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eb7c021e-380a-410b-a199-64af6b82580d",
  "uuid": "0747526a-5a7b-4c64-9aff-a5329c1c8bf2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016xZTePbmCnnsjFi4Dwu19B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1049,
      "cache_read_input_tokens": 39200,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1049
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01X6Bb91gWEzYHZcAYVWnzpg`</summary>

```json
{
  "exp_id": "westd-pi05-vla-only-object-s42-paired",
  "field": "checkpoint_path",
  "value": "N/A - eval only",
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
  "session_id": "eb7c021e-380a-410b-a199-64af6b82580d",
  "uuid": "637d9c0c-a0a1-401a-b82e-74fea5c87886",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016xZTePbmCnnsjFi4Dwu19B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1049,
      "cache_read_input_tokens": 39200,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1049
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

_source line 41_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01VtJHhWHvFyJZjFZk1qL7kS`</summary>

```json
{
  "exp_id": "westd-pi05-vla-only-object-s42-paired",
  "field": "log_path",
  "value": "/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed42_westd.json",
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
  "session_id": "eb7c021e-380a-410b-a199-64af6b82580d",
  "uuid": "bbdf488e-8b94-43af-a2f2-96fff8371f0c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016xZTePbmCnnsjFi4Dwu19B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1049,
      "cache_read_input_tokens": 39200,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1049
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

_source line 42_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01Ho8NhCziaHsVKj4ufymsps`</summary>

```json
{
  "exp_id": "westd-pi05-vla-only-object-s43-paired",
  "field": "checkpoint_path",
  "value": "N/A - eval only",
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
  "session_id": "eb7c021e-380a-410b-a199-64af6b82580d",
  "uuid": "96c73e99-5c09-4ee6-ba6e-7fea7eb954b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016xZTePbmCnnsjFi4Dwu19B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1049,
      "cache_read_input_tokens": 39200,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1049
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_017q9RK2L8ERc9CbAW3f5Lso`</summary>

```json
{
  "exp_id": "westd-pi05-vla-only-object-s43-paired",
  "field": "log_path",
  "value": "/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed43_westd.json",
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
  "session_id": "eb7c021e-380a-410b-a199-64af6b82580d",
  "uuid": "05dcb867-5106-41df-8d72-c5c6149964de",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016xZTePbmCnnsjFi4Dwu19B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1049,
      "cache_read_input_tokens": 39200,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1049
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01A66CG4xHRGwdMNLwq2Nmhv`</summary>

```json
{
  "exp_id": "westd-pi05-vla-only-object-s44-paired",
  "field": "checkpoint_path",
  "value": "N/A - eval only",
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
  "session_id": "eb7c021e-380a-410b-a199-64af6b82580d",
  "uuid": "eebcaf9d-dd12-447a-93d3-f4f0ed1799a5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016xZTePbmCnnsjFi4Dwu19B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1049,
      "cache_read_input_tokens": 39200,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1049
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

_source line 45_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01Xs31Zzf9P5PqtVBbgKrQ4m`</summary>

```json
{
  "exp_id": "westd-pi05-vla-only-object-s44-paired",
  "field": "log_path",
  "value": "/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed44_westd.json",
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
  "session_id": "eb7c021e-380a-410b-a199-64af6b82580d",
  "uuid": "77b67ee5-0fc8-4a39-a296-1c0e2962059a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016xZTePbmCnnsjFi4Dwu19B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1049,
      "cache_read_input_tokens": 39200,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1049
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

_source line 46 · 2026-05-26T12:07:38.294Z_

<details><summary>↩ Tool result · `toolu_01X6Bb91gWEzYHZcAYVWnzpg`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"westd-pi05-vla-only-object-s42-paired\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T11:02:15.888Z\", \"updated_at\": \"2026-05-26T12:07:32.170Z\", \"hypothesis\": \"π0.5 VLA-only baseline on Object s42 (westd same-server paired). Blackwell paired comparison for cross-hardware validation.\", \"server\": \"westd-49937\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-49937\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-26T11:19:04.337Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 42 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed42_westd.json\\\"\", \"code_commit\": \"a594db578deeeeddc0ab068549e315c5a3bb4d6a\", \"finished_at\": \"2026-05-26T11:48:36.048Z\", \"training_hours\": 0.49}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 42 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed42_westd.json\\\"\", \"server\": \"westd-49937\", \"gpu\": [\"cuda:3\"], \"pid\": \"201673\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/westd-pi05-vla-only-object-s42-paired.log\", \"submitted_at\": \"2026-05-26T11:19:17.346Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 2645.7, \"gpu_hours\": 0.73}, \"pid\": \"201673\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/westd-pi05-vla-only-object-s42-paired.log\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.995, \"n_rollouts\": 20, \"n_tasks\": 10, \"per_task_min\": 0.95, \"per_task_max\": 1}, \"checkpoint_path\": \"N/A - eval only\", \"completed_at\": \"2026-05-26T12:03:23.016Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 25.982}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eb7c021e-380a-410b-a199-64af6b82580d",
  "uuid": "8d26047a-a136-4509-bbb1-fd004b2dbf82",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"westd-pi05-vla-only-object-s42-paired\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-26T11:02:15.888Z\\\", \\\"updated_at\\\": \\\"2026-05-26T12:07:32.170Z\\\", \\\"hypothesis\\\": \\\"π0.5 VLA-only baseline on Object s42 (westd same-server paired). Blackwell paired comparison for cross-hardware validation.\\\", \\\"server\\\": \\\"westd-49937\\\", \\\"gpu\\\": \\\"cuda:3\\\", \\\"account\\\": \\\"root\\\", \\\"reproduce\\\": {\\\"server\\\": \\\"westd-49937\\\", \\\"gpu\\\": \\\"cuda:3\\\", \\\"started_at\\\": \\\"2026-05-26T11:19:04.337Z\\\", \\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 42 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed42_westd.json\\\\\\\"\\\", \\\"code_commit\\\": \\\"a594db578deeeeddc0ab068549e315c5a3bb4d6a\\\", \\\"finished_at\\\": \\\"2026-05-26T11:48:36.048Z\\\", \\\"training_hours\\\": 0.49}, \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 42 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed42_westd.json\\\\\\\"\\\", \\\"server\\\": \\\"westd-49937\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"pid\\\": \\\"201673\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/westd-pi05-vla-only-object-s42-paired.log\\\", \\\"submitted_at\\\": \\\"2026-05-26T11:19:17.346Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"wall_clock_seconds\\\": 2645.7, \\\"gpu_hours\\\": 0.73}, \\\"pid\\\": \\\"201673\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/westd-pi05-vla-only-object-s42-paired.log\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.995, \\\"n_rollouts\\\": 20, \\\"n_tasks\\\": 10, \\\"per_task_min\\\": 0.95, \\\"per_task_max\\\": 1}, \\\"checkpoint_path\\\": \\\"N/A - eval only\\\", \\\"completed_at\\\": \\\"2026-05-26T12:03:23.016Z\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 25.982}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"westd-pi05-vla-only-object-s42-paired\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T11:02:15.888Z\", \"updated_at\": \"2026-05-26T12:07:32.170Z\", \"hypothesis\": \"π0.5 VLA-only baseline on Object s42 (westd same-server paired). Blackwell paired comparison for cross-hardware validation.\", \"server\": \"westd-49937\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-49937\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-26T11:19:04.337Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 42 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed42_westd.json\\\"\", \"code_commit\": \"a594db578deeeeddc0ab068549e315c5a3bb4d6a\", \"finished_at\": \"2026-05-26T11:48:36.048Z\", \"training_hours\": 0.49}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 42 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed42_westd.json\\\"\", \"server\": \"westd-49937\", \"gpu\": [\"cuda:3\"], \"pid\": \"201673\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/westd-pi05-vla-only-object-s42-paired.log\", \"submitted_at\": \"2026-05-26T11:19:17.346Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 2645.7, \"gpu_hours\": 0.73}, \"pid\": \"201673\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/westd-pi05-vla-only-object-s42-paired.log\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.995, \"n_rollouts\": 20, \"n_tasks\": 10, \"per_task_min\": 0.95, \"per_task_max\": 1}, \"checkpoint_path\": \"N/A - eval only\", \"completed_at\": \"2026-05-26T12:03:23.016Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 25.982}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-26T12:08:05.183Z_

<details><summary>↩ Tool result · `toolu_01VtJHhWHvFyJZjFZk1qL7kS`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"westd-pi05-vla-only-object-s42-paired\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T11:02:15.888Z\", \"updated_at\": \"2026-05-26T12:07:58.988Z\", \"hypothesis\": \"π0.5 VLA-only baseline on Object s42 (westd same-server paired). Blackwell paired comparison for cross-hardware validation.\", \"server\": \"westd-49937\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-49937\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-26T11:19:04.337Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 42 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed42_westd.json\\\"\", \"code_commit\": \"a594db578deeeeddc0ab068549e315c5a3bb4d6a\", \"finished_at\": \"2026-05-26T11:48:36.048Z\", \"training_hours\": 0.49}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 42 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed42_westd.json\\\"\", \"server\": \"westd-49937\", \"gpu\": [\"cuda:3\"], \"pid\": \"201673\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/westd-pi05-vla-only-object-s42-paired.log\", \"submitted_at\": \"2026-05-26T11:19:17.346Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 2645.7, \"gpu_hours\": 0.73}, \"pid\": \"201673\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed42_westd.json\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.995, \"n_rollouts\": 20, \"n_tasks\": 10, \"per_task_min\": 0.95, \"per_task_max\": 1}, \"checkpoint_path\": \"N/A - eval only\", \"completed_at\": \"2026-05-26T12:03:23.016Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 26.8389}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eb7c021e-380a-410b-a199-64af6b82580d",
  "uuid": "31fb610f-8940-470d-a4d5-0329b8488072",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"westd-pi05-vla-only-object-s42-paired\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-26T11:02:15.888Z\\\", \\\"updated_at\\\": \\\"2026-05-26T12:07:58.988Z\\\", \\\"hypothesis\\\": \\\"π0.5 VLA-only baseline on Object s42 (westd same-server paired). Blackwell paired comparison for cross-hardware validation.\\\", \\\"server\\\": \\\"westd-49937\\\", \\\"gpu\\\": \\\"cuda:3\\\", \\\"account\\\": \\\"root\\\", \\\"reproduce\\\": {\\\"server\\\": \\\"westd-49937\\\", \\\"gpu\\\": \\\"cuda:3\\\", \\\"started_at\\\": \\\"2026-05-26T11:19:04.337Z\\\", \\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 42 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed42_westd.json\\\\\\\"\\\", \\\"code_commit\\\": \\\"a594db578deeeeddc0ab068549e315c5a3bb4d6a\\\", \\\"finished_at\\\": \\\"2026-05-26T11:48:36.048Z\\\", \\\"training_hours\\\": 0.49}, \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 42 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed42_westd.json\\\\\\\"\\\", \\\"server\\\": \\\"westd-49937\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"pid\\\": \\\"201673\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/westd-pi05-vla-only-object-s42-paired.log\\\", \\\"submitted_at\\\": \\\"2026-05-26T11:19:17.346Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"wall_clock_seconds\\\": 2645.7, \\\"gpu_hours\\\": 0.73}, \\\"pid\\\": \\\"201673\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed42_westd.json\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.995, \\\"n_rollouts\\\": 20, \\\"n_tasks\\\": 10, \\\"per_task_min\\\": 0.95, \\\"per_task_max\\\": 1}, \\\"checkpoint_path\\\": \\\"N/A - eval only\\\", \\\"completed_at\\\": \\\"2026-05-26T12:03:23.016Z\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 26.8389}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"westd-pi05-vla-only-object-s42-paired\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T11:02:15.888Z\", \"updated_at\": \"2026-05-26T12:07:58.988Z\", \"hypothesis\": \"π0.5 VLA-only baseline on Object s42 (westd same-server paired). Blackwell paired comparison for cross-hardware validation.\", \"server\": \"westd-49937\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-49937\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-26T11:19:04.337Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 42 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed42_westd.json\\\"\", \"code_commit\": \"a594db578deeeeddc0ab068549e315c5a3bb4d6a\", \"finished_at\": \"2026-05-26T11:48:36.048Z\", \"training_hours\": 0.49}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 42 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed42_westd.json\\\"\", \"server\": \"westd-49937\", \"gpu\": [\"cuda:3\"], \"pid\": \"201673\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/westd-pi05-vla-only-object-s42-paired.log\", \"submitted_at\": \"2026-05-26T11:19:17.346Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 2645.7, \"gpu_hours\": 0.73}, \"pid\": \"201673\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed42_westd.json\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.995, \"n_rollouts\": 20, \"n_tasks\": 10, \"per_task_min\": 0.95, \"per_task_max\": 1}, \"checkpoint_path\": \"N/A - eval only\", \"completed_at\": \"2026-05-26T12:03:23.016Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 26.8389}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-26T12:08:31.990Z_

<details><summary>↩ Tool result · `toolu_01Ho8NhCziaHsVKj4ufymsps`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"westd-pi05-vla-only-object-s43-paired\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T11:02:30.548Z\", \"updated_at\": \"2026-05-26T12:08:25.885Z\", \"hypothesis\": \"π0.5 VLA-only baseline on Object s43 (westd same-server paired). Blackwell paired comparison for cross-hardware validation.\", \"server\": \"westd-49937\", \"gpu\": \"cuda:4\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-49937\", \"gpu\": \"cuda:4\", \"started_at\": \"2026-05-26T11:19:54.492Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 43 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed43_westd.json\\\"\", \"code_commit\": \"a594db578deeeeddc0ab068549e315c5a3bb4d6a\", \"finished_at\": \"2026-05-26T11:46:59.594Z\", \"training_hours\": 0.45}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 43 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed43_westd.json\\\"\", \"server\": \"westd-49937\", \"gpu\": [\"cuda:4\"], \"pid\": \"205359\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/westd-pi05-vla-only-object-s43-paired.log\", \"submitted_at\": \"2026-05-26T11:20:07.286Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 2633.7, \"gpu_hours\": 0.73}, \"pid\": \"205359\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/westd-pi05-vla-only-object-s43-paired.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T11:49:29.164309+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 1, \"n_rollouts\": 20, \"n_tasks\": 10, \"per_task_min\": 1, \"per_task_max\": 1}, \"checkpoint_path\": \"N/A - eval only\", \"completed_at\": \"2026-05-26T12:04:01.005Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 26.7609}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eb7c021e-380a-410b-a199-64af6b82580d",
  "uuid": "a7c46f66-8453-4a46-a9ce-016308feafa6",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"westd-pi05-vla-only-object-s43-paired\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-26T11:02:30.548Z\\\", \\\"updated_at\\\": \\\"2026-05-26T12:08:25.885Z\\\", \\\"hypothesis\\\": \\\"π0.5 VLA-only baseline on Object s43 (westd same-server paired). Blackwell paired comparison for cross-hardware validation.\\\", \\\"server\\\": \\\"westd-49937\\\", \\\"gpu\\\": \\\"cuda:4\\\", \\\"account\\\": \\\"root\\\", \\\"reproduce\\\": {\\\"server\\\": \\\"westd-49937\\\", \\\"gpu\\\": \\\"cuda:4\\\", \\\"started_at\\\": \\\"2026-05-26T11:19:54.492Z\\\", \\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 43 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed43_westd.json\\\\\\\"\\\", \\\"code_commit\\\": \\\"a594db578deeeeddc0ab068549e315c5a3bb4d6a\\\", \\\"finished_at\\\": \\\"2026-05-26T11:46:59.594Z\\\", \\\"training_hours\\\": 0.45}, \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 43 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed43_westd.json\\\\\\\"\\\", \\\"server\\\": \\\"westd-49937\\\", \\\"gpu\\\": [\\\"cuda:4\\\"], \\\"pid\\\": \\\"205359\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/westd-pi05-vla-only-object-s43-paired.log\\\", \\\"submitted_at\\\": \\\"2026-05-26T11:20:07.286Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"wall_clock_seconds\\\": 2633.7, \\\"gpu_hours\\\": 0.73}, \\\"pid\\\": \\\"205359\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/westd-pi05-vla-only-object-s43-paired.log\\\", \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-26T11:49:29.164309+00:00\\\"}]}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 1, \\\"n_rollouts\\\": 20, \\\"n_tasks\\\": 10, \\\"per_task_min\\\": 1, \\\"per_task_max\\\": 1}, \\\"checkpoint_path\\\": \\\"N/A - eval only\\\", \\\"completed_at\\\": \\\"2026-05-26T12:04:01.005Z\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 26.7609}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"westd-pi05-vla-only-object-s43-paired\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T11:02:30.548Z\", \"updated_at\": \"2026-05-26T12:08:25.885Z\", \"hypothesis\": \"π0.5 VLA-only baseline on Object s43 (westd same-server paired). Blackwell paired comparison for cross-hardware validation.\", \"server\": \"westd-49937\", \"gpu\": \"cuda:4\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-49937\", \"gpu\": \"cuda:4\", \"started_at\": \"2026-05-26T11:19:54.492Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 43 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed43_westd.json\\\"\", \"code_commit\": \"a594db578deeeeddc0ab068549e315c5a3bb4d6a\", \"finished_at\": \"2026-05-26T11:46:59.594Z\", \"training_hours\": 0.45}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 43 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed43_westd.json\\\"\", \"server\": \"westd-49937\", \"gpu\": [\"cuda:4\"], \"pid\": \"205359\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/westd-pi05-vla-only-object-s43-paired.log\", \"submitted_at\": \"2026-05-26T11:20:07.286Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 2633.7, \"gpu_hours\": 0.73}, \"pid\": \"205359\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/westd-pi05-vla-only-object-s43-paired.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T11:49:29.164309+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 1, \"n_rollouts\": 20, \"n_tasks\": 10, \"per_task_min\": 1, \"per_task_max\": 1}, \"checkpoint_path\": \"N/A - eval only\", \"completed_at\": \"2026-05-26T12:04:01.005Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 26.7609}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-26T12:08:43.829Z_

<details><summary>↩ Tool result · `toolu_017q9RK2L8ERc9CbAW3f5Lso`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"westd-pi05-vla-only-object-s43-paired\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T11:02:30.548Z\", \"updated_at\": \"2026-05-26T12:08:38.942Z\", \"hypothesis\": \"π0.5 VLA-only baseline on Object s43 (westd same-server paired). Blackwell paired comparison for cross-hardware validation.\", \"server\": \"westd-49937\", \"gpu\": \"cuda:4\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-49937\", \"gpu\": \"cuda:4\", \"started_at\": \"2026-05-26T11:19:54.492Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 43 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed43_westd.json\\\"\", \"code_commit\": \"a594db578deeeeddc0ab068549e315c5a3bb4d6a\", \"finished_at\": \"2026-05-26T11:46:59.594Z\", \"training_hours\": 0.45}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 43 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed43_westd.json\\\"\", \"server\": \"westd-49937\", \"gpu\": [\"cuda:4\"], \"pid\": \"205359\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/westd-pi05-vla-only-object-s43-paired.log\", \"submitted_at\": \"2026-05-26T11:20:07.286Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 2633.7, \"gpu_hours\": 0.73}, \"pid\": \"205359\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed43_westd.json\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T11:49:29.164309+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 1, \"n_rollouts\": 20, \"n_tasks\": 10, \"per_task_min\": 1, \"per_task_max\": 1}, \"checkpoint_path\": \"N/A - eval only\", \"completed_at\": \"2026-05-26T12:04:01.005Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 11.8088}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eb7c021e-380a-410b-a199-64af6b82580d",
  "uuid": "fdad0337-0d3a-4a59-8124-f79d70eecfd1",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"westd-pi05-vla-only-object-s43-paired\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-26T11:02:30.548Z\\\", \\\"updated_at\\\": \\\"2026-05-26T12:08:38.942Z\\\", \\\"hypothesis\\\": \\\"π0.5 VLA-only baseline on Object s43 (westd same-server paired). Blackwell paired comparison for cross-hardware validation.\\\", \\\"server\\\": \\\"westd-49937\\\", \\\"gpu\\\": \\\"cuda:4\\\", \\\"account\\\": \\\"root\\\", \\\"reproduce\\\": {\\\"server\\\": \\\"westd-49937\\\", \\\"gpu\\\": \\\"cuda:4\\\", \\\"started_at\\\": \\\"2026-05-26T11:19:54.492Z\\\", \\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 43 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed43_westd.json\\\\\\\"\\\", \\\"code_commit\\\": \\\"a594db578deeeeddc0ab068549e315c5a3bb4d6a\\\", \\\"finished_at\\\": \\\"2026-05-26T11:46:59.594Z\\\", \\\"training_hours\\\": 0.45}, \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 43 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed43_westd.json\\\\\\\"\\\", \\\"server\\\": \\\"westd-49937\\\", \\\"gpu\\\": [\\\"cuda:4\\\"], \\\"pid\\\": \\\"205359\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/westd-pi05-vla-only-object-s43-paired.log\\\", \\\"submitted_at\\\": \\\"2026-05-26T11:20:07.286Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"wall_clock_seconds\\\": 2633.7, \\\"gpu_hours\\\": 0.73}, \\\"pid\\\": \\\"205359\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed43_westd.json\\\", \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-26T11:49:29.164309+00:00\\\"}]}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 1, \\\"n_rollouts\\\": 20, \\\"n_tasks\\\": 10, \\\"per_task_min\\\": 1, \\\"per_task_max\\\": 1}, \\\"checkpoint_path\\\": \\\"N/A - eval only\\\", \\\"completed_at\\\": \\\"2026-05-26T12:04:01.005Z\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 11.8088}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"westd-pi05-vla-only-object-s43-paired\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T11:02:30.548Z\", \"updated_at\": \"2026-05-26T12:08:38.942Z\", \"hypothesis\": \"π0.5 VLA-only baseline on Object s43 (westd same-server paired). Blackwell paired comparison for cross-hardware validation.\", \"server\": \"westd-49937\", \"gpu\": \"cuda:4\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-49937\", \"gpu\": \"cuda:4\", \"started_at\": \"2026-05-26T11:19:54.492Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 43 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed43_westd.json\\\"\", \"code_commit\": \"a594db578deeeeddc0ab068549e315c5a3bb4d6a\", \"finished_at\": \"2026-05-26T11:46:59.594Z\", \"training_hours\": 0.45}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 43 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed43_westd.json\\\"\", \"server\": \"westd-49937\", \"gpu\": [\"cuda:4\"], \"pid\": \"205359\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/westd-pi05-vla-only-object-s43-paired.log\", \"submitted_at\": \"2026-05-26T11:20:07.286Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 2633.7, \"gpu_hours\": 0.73}, \"pid\": \"205359\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed43_westd.json\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T11:49:29.164309+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 1, \"n_rollouts\": 20, \"n_tasks\": 10, \"per_task_min\": 1, \"per_task_max\": 1}, \"checkpoint_path\": \"N/A - eval only\", \"completed_at\": \"2026-05-26T12:04:01.005Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 11.8088}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-26T12:08:57.169Z_

<details><summary>↩ Tool result · `toolu_01A66CG4xHRGwdMNLwq2Nmhv`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"westd-pi05-vla-only-object-s44-paired\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T11:02:45.036Z\", \"updated_at\": \"2026-05-26T12:08:52.541Z\", \"hypothesis\": \"π0.5 VLA-only baseline on Object s44. westd same-server paired comparison (Blackwell).\", \"server\": \"westd-49937\", \"gpu\": \"cuda:5\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-49937\", \"gpu\": \"cuda:5\", \"started_at\": \"2026-05-26T11:20:41.954Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 44 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed44_westd.json\\\"\", \"code_commit\": \"a594db578deeeeddc0ab068549e315c5a3bb4d6a\", \"finished_at\": \"2026-05-26T11:51:42.620Z\", \"training_hours\": 0.52}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 44 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed44_westd.json\\\"\", \"server\": \"westd-49937\", \"gpu\": [\"cuda:5\"], \"pid\": \"210173\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/westd-pi05-vla-only-object-s44-paired.log\", \"submitted_at\": \"2026-05-26T11:20:54.134Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 2614.6, \"gpu_hours\": 0.73}, \"pid\": \"210173\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/westd-pi05-vla-only-object-s44-paired.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T11:52:27.848319+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T11:53:35.087334+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.995, \"n_rollouts\": 20, \"n_tasks\": 10, \"per_task_min\": 0.95, \"per_task_max\": 1}, \"checkpoint_path\": \"N/A - eval only\", \"completed_at\": \"2026-05-26T12:04:28.711Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 13.2995}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eb7c021e-380a-410b-a199-64af6b82580d",
  "uuid": "f57d0e90-afd3-4e52-af0b-52f8541560d5",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"westd-pi05-vla-only-object-s44-paired\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-26T11:02:45.036Z\\\", \\\"updated_at\\\": \\\"2026-05-26T12:08:52.541Z\\\", \\\"hypothesis\\\": \\\"π0.5 VLA-only baseline on Object s44. westd same-server paired comparison (Blackwell).\\\", \\\"server\\\": \\\"westd-49937\\\", \\\"gpu\\\": \\\"cuda:5\\\", \\\"account\\\": \\\"root\\\", \\\"reproduce\\\": {\\\"server\\\": \\\"westd-49937\\\", \\\"gpu\\\": \\\"cuda:5\\\", \\\"started_at\\\": \\\"2026-05-26T11:20:41.954Z\\\", \\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 44 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed44_westd.json\\\\\\\"\\\", \\\"code_commit\\\": \\\"a594db578deeeeddc0ab068549e315c5a3bb4d6a\\\", \\\"finished_at\\\": \\\"2026-05-26T11:51:42.620Z\\\", \\\"training_hours\\\": 0.52}, \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 44 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed44_westd.json\\\\\\\"\\\", \\\"server\\\": \\\"westd-49937\\\", \\\"gpu\\\": [\\\"cuda:5\\\"], \\\"pid\\\": \\\"210173\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/westd-pi05-vla-only-object-s44-paired.log\\\", \\\"submitted_at\\\": \\\"2026-05-26T11:20:54.134Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"wall_clock_seconds\\\": 2614.6, \\\"gpu_hours\\\": 0.73}, \\\"pid\\\": \\\"210173\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/westd-pi05-vla-only-object-s44-paired.log\\\", \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-26T11:52:27.848319+00:00\\\"}, {\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-26T11:53:35.087334+00:00\\\"}]}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.995, \\\"n_rollouts\\\": 20, \\\"n_tasks\\\": 10, \\\"per_task_min\\\": 0.95, \\\"per_task_max\\\": 1}, \\\"checkpoint_path\\\": \\\"N/A - eval only\\\", \\\"completed_at\\\": \\\"2026-05-26T12:04:28.711Z\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 13.2995}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"westd-pi05-vla-only-object-s44-paired\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T11:02:45.036Z\", \"updated_at\": \"2026-05-26T12:08:52.541Z\", \"hypothesis\": \"π0.5 VLA-only baseline on Object s44. westd same-server paired comparison (Blackwell).\", \"server\": \"westd-49937\", \"gpu\": \"cuda:5\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-49937\", \"gpu\": \"cuda:5\", \"started_at\": \"2026-05-26T11:20:41.954Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 44 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed44_westd.json\\\"\", \"code_commit\": \"a594db578deeeeddc0ab068549e315c5a3bb4d6a\", \"finished_at\": \"2026-05-26T11:51:42.620Z\", \"training_hours\": 0.52}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 44 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed44_westd.json\\\"\", \"server\": \"westd-49937\", \"gpu\": [\"cuda:5\"], \"pid\": \"210173\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/westd-pi05-vla-only-object-s44-paired.log\", \"submitted_at\": \"2026-05-26T11:20:54.134Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 2614.6, \"gpu_hours\": 0.73}, \"pid\": \"210173\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/westd-pi05-vla-only-object-s44-paired.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T11:52:27.848319+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T11:53:35.087334+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.995, \"n_rollouts\": 20, \"n_tasks\": 10, \"per_task_min\": 0.95, \"per_task_max\": 1}, \"checkpoint_path\": \"N/A - eval only\", \"completed_at\": \"2026-05-26T12:04:28.711Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 13.2995}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-26T12:09:09.016Z_

<details><summary>↩ Tool result · `toolu_01Xs31Zzf9P5PqtVBbgKrQ4m`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"westd-pi05-vla-only-object-s44-paired\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T11:02:45.036Z\", \"updated_at\": \"2026-05-26T12:09:04.162Z\", \"hypothesis\": \"π0.5 VLA-only baseline on Object s44. westd same-server paired comparison (Blackwell).\", \"server\": \"westd-49937\", \"gpu\": \"cuda:5\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-49937\", \"gpu\": \"cuda:5\", \"started_at\": \"2026-05-26T11:20:41.954Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 44 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed44_westd.json\\\"\", \"code_commit\": \"a594db578deeeeddc0ab068549e315c5a3bb4d6a\", \"finished_at\": \"2026-05-26T11:51:42.620Z\", \"training_hours\": 0.52}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 44 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed44_westd.json\\\"\", \"server\": \"westd-49937\", \"gpu\": [\"cuda:5\"], \"pid\": \"210173\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/westd-pi05-vla-only-object-s44-paired.log\", \"submitted_at\": \"2026-05-26T11:20:54.134Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 2614.6, \"gpu_hours\": 0.73}, \"pid\": \"210173\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed44_westd.json\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T11:52:27.848319+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T11:53:35.087334+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.995, \"n_rollouts\": 20, \"n_tasks\": 10, \"per_task_min\": 0.95, \"per_task_max\": 1}, \"checkpoint_path\": \"N/A - eval only\", \"completed_at\": \"2026-05-26T12:04:28.711Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 11.8216}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eb7c021e-380a-410b-a199-64af6b82580d",
  "uuid": "e1163624-8480-49aa-8405-04c60200ff16",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"westd-pi05-vla-only-object-s44-paired\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-26T11:02:45.036Z\\\", \\\"updated_at\\\": \\\"2026-05-26T12:09:04.162Z\\\", \\\"hypothesis\\\": \\\"π0.5 VLA-only baseline on Object s44. westd same-server paired comparison (Blackwell).\\\", \\\"server\\\": \\\"westd-49937\\\", \\\"gpu\\\": \\\"cuda:5\\\", \\\"account\\\": \\\"root\\\", \\\"reproduce\\\": {\\\"server\\\": \\\"westd-49937\\\", \\\"gpu\\\": \\\"cuda:5\\\", \\\"started_at\\\": \\\"2026-05-26T11:20:41.954Z\\\", \\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 44 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed44_westd.json\\\\\\\"\\\", \\\"code_commit\\\": \\\"a594db578deeeeddc0ab068549e315c5a3bb4d6a\\\", \\\"finished_at\\\": \\\"2026-05-26T11:51:42.620Z\\\", \\\"training_hours\\\": 0.52}, \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 44 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed44_westd.json\\\\\\\"\\\", \\\"server\\\": \\\"westd-49937\\\", \\\"gpu\\\": [\\\"cuda:5\\\"], \\\"pid\\\": \\\"210173\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/westd-pi05-vla-only-object-s44-paired.log\\\", \\\"submitted_at\\\": \\\"2026-05-26T11:20:54.134Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"wall_clock_seconds\\\": 2614.6, \\\"gpu_hours\\\": 0.73}, \\\"pid\\\": \\\"210173\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed44_westd.json\\\", \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-26T11:52:27.848319+00:00\\\"}, {\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-26T11:53:35.087334+00:00\\\"}]}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.995, \\\"n_rollouts\\\": 20, \\\"n_tasks\\\": 10, \\\"per_task_min\\\": 0.95, \\\"per_task_max\\\": 1}, \\\"checkpoint_path\\\": \\\"N/A - eval only\\\", \\\"completed_at\\\": \\\"2026-05-26T12:04:28.711Z\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 11.8216}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"westd-pi05-vla-only-object-s44-paired\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T11:02:45.036Z\", \"updated_at\": \"2026-05-26T12:09:04.162Z\", \"hypothesis\": \"π0.5 VLA-only baseline on Object s44. westd same-server paired comparison (Blackwell).\", \"server\": \"westd-49937\", \"gpu\": \"cuda:5\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-49937\", \"gpu\": \"cuda:5\", \"started_at\": \"2026-05-26T11:20:41.954Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 44 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed44_westd.json\\\"\", \"code_commit\": \"a594db578deeeeddc0ab068549e315c5a3bb4d6a\", \"finished_at\": \"2026-05-26T11:51:42.620Z\", \"training_hours\": 0.52}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --seed 44 --n_rollouts 20 --output_file logs/eval_object_vla_only_pi05_seed44_westd.json\\\"\", \"server\": \"westd-49937\", \"gpu\": [\"cuda:5\"], \"pid\": \"210173\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/westd-pi05-vla-only-object-s44-paired.log\", \"submitted_at\": \"2026-05-26T11:20:54.134Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 2614.6, \"gpu_hours\": 0.73}, \"pid\": \"210173\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_pi05_seed44_westd.json\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T11:52:27.848319+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T11:53:35.087334+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.995, \"n_rollouts\": 20, \"n_tasks\": 10, \"per_task_min\": 0.95, \"per_task_max\": 1}, \"checkpoint_path\": \"N/A - eval only\", \"completed_at\": \"2026-05-26T12:04:28.711Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 11.8216}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 52_

全部完成。Registry 已更新 checkpoint_path 和 log_path。

## π0.5 VLA-only Object Baseline (westd Blackwell, 10 tasks × 20 rollouts)

| Seed | Success Rate | 失败 task |
|------|-------------|-----------|
| 42 | **99.5%** | bbq_sauce 19/20 |
| 43 | **100.0%** | 无 |
| 44 | **99.5%** | bbq_sauce 19/20 |

**Mean ± Std: 99.7% ± 0.3%**

## 与 registry 中其他 π0.5 Object 结果对比

| 实验 | Server | Mode | Success Rate |
|------|--------|------|-------------|
| westd VLA-only (本次) | westd-49937 (Blackwell) | vla_only | **99.7 ± 0.3%** |
| westd Adaptive Conformal s42 | westd-49937 (Blackwell) | adaptive_conformal_crm | 83.5% |
| 4090 Adaptive Conformal s42 | cqa1 (4090) | adaptive_conformal_crm | 85.5% |
| 4090 Adaptive Object s43 | bjb2-24035 (4090) | adaptive_conformal_crm | 83.0% |

π0.5 VLA-only 在 Object suite 上接近完美（仅 bbq_sauce 偶发失败），Adaptive Conformal 在该 suite 上反而降低约 15pp — 对于 near-ceiling baseline，correction 引入的扰动大于收益。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eb7c021e-380a-410b-a199-64af6b82580d",
  "uuid": "c62f7f87-449e-4da5-b06c-26b66451295d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018XT7U2JdEyE5hzN67Rvd3C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7358,
      "cache_read_input_tokens": 40249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7358
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

_source line 53_

全部完成。Registry 已更新 checkpoint_path 和 log_path。

## π0.5 VLA-only Object Baseline (westd Blackwell, 10 tasks × 20 rollouts)

| Seed | Success Rate | 失败 task |
|------|-------------|-----------|
| 42 | **99.5%** | bbq_sauce 19/20 |
| 43 | **100.0%** | 无 |
| 44 | **99.5%** | bbq_sauce 19/20 |

**Mean ± Std: 99.7% ± 0.3%**

## 与 registry 中其他 π0.5 Object 结果对比

| 实验 | Server | Mode | Success Rate |
|------|--------|------|-------------|
| westd VLA-only (本次) | westd-49937 (Blackwell) | vla_only | **99.7 ± 0.3%** |
| westd Adaptive Conformal s42 | westd-49937 (Blackwell) | adaptive_conformal_crm | 83.5% |
| 4090 Adaptive Conformal s42 | cqa1 (4090) | adaptive_conformal_crm | 85.5% |
| 4090 Adaptive Object s43 | bjb2-24035 (4090) | adaptive_conformal_crm | 83.0% |

π0.5 VLA-only 在 Object suite 上接近完美（仅 bbq_sauce 偶发失败），Adaptive Conformal 在该 suite 上反而降低约 15pp — 对于 near-ceiling baseline，correction 引入的扰动大于收益。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 249923,
  "duration_api_ms": 80973,
  "num_turns": 21,
  "stop_reason": "end_turn",
  "session_id": "eb7c021e-380a-410b-a199-64af6b82580d",
  "total_cost_usd": 0.436689,
  "usage": {
    "input_tokens": 10,
    "cache_creation_input_tokens": 35766,
    "cache_read_input_tokens": 199397,
    "output_tokens": 4478,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 35766,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 447,
        "cache_read_input_tokens": 40249,
        "cache_creation_input_tokens": 7358,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 7358
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1333,
      "outputTokens": 24,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001453,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 10,
      "outputTokens": 4478,
      "cacheReadInputTokens": 199397,
      "cacheCreationInputTokens": 35766,
      "webSearchRequests": 0,
      "costUSD": 0.43523599999999996,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "bc1f85b8-b7c5-4aa4-89af-58fc5f61943f"
}
```

</details>

---
