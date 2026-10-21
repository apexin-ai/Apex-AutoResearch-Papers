# ops recompute llama d values

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 30
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/workers/worker_ops_recompute-llama-d-values_20260523T150337.log`
- **Structured JSON:** [`2c61effc200d459b444a.json`](../../sessions/2c/2c61effc200d459b444a.json)

## Before a recorded user message

30 recorded events

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
  "session_id": "9dd1310f-2eca-4936-af7c-90a1b8a75881",
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
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__register_artifact",
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
  "uuid": "1e04129c-50bc-482a-8e97-c8b0356257dc",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0519-3-projects-irt-personfit-contam/memory/"
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
    "resetsAt": 1779565200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "f0bfda98-dcc7-48df-a46f-68caed83e052",
  "session_id": "9dd1310f-2eca-4936-af7c-90a1b8a75881"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the registry to get the missing lz* values for exp-llama-5pct-s3 and exp-llama-25pct-s3.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9dd1310f-2eca-4936-af7c-90a1b8a75881",
  "uuid": "0746f1a4-ef32-4288-9345-3d25a422ddbb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RBCAkm51uDv81LAoGBZbcs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12139,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12139
      },
      "output_tokens": 30,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01LoS191K5sYPmxrt2erAeLZ`</summary>

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
  "session_id": "9dd1310f-2eca-4936-af7c-90a1b8a75881",
  "uuid": "bacd6462-4857-4425-930b-2f840927f718",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RBCAkm51uDv81LAoGBZbcs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12139,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12139
      },
      "output_tokens": 30,
      "service_tier": "standard",
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

_source line 6 · 2026-05-23T15:03:48.297Z_

<details><summary>↩ Tool result · `toolu_01LoS191K5sYPmxrt2erAeLZ`</summary>

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
  "session_id": "9dd1310f-2eca-4936-af7c-90a1b8a75881",
  "uuid": "0b862de6-6c55-4805-ad1c-bc308f2d1048",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_registry"
    ],
    "query": "select:mcp__agent-ml-research__read_registry",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_0171mtvbSYg7dffQ7Tu9fur4`</summary>

```json
{
  "project": "irt_personfit_contam",
  "filters": {
    "exp_id": "exp-llama-5pct-s3"
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
  "session_id": "9dd1310f-2eca-4936-af7c-90a1b8a75881",
  "uuid": "777d725e-9e19-439e-bfdb-43f7ee70d725",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0195auiVUsriPoMvrpSvjQSv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 504,
      "cache_read_input_tokens": 23980,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 504
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

_source line 8 · 2026-05-23T15:03:52.052Z_

<details><summary>↩ Tool result · `toolu_0171mtvbSYg7dffQ7Tu9fur4`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2855}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9dd1310f-2eca-4936-af7c-90a1b8a75881",
  "uuid": "afe153a1-e07b-426b-ae21-d699e5506899",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.2855}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2855}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_0171EUdkA3ZCg52wTyRVv9fw`</summary>

```json
{
  "project": "irt_personfit_contam",
  "filters": {
    "exp_id": "exp-llama-25pct-s3"
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
  "session_id": "9dd1310f-2eca-4936-af7c-90a1b8a75881",
  "uuid": "5ae5dede-8365-44d0-85df-0222fbb6f53e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0195auiVUsriPoMvrpSvjQSv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 504,
      "cache_read_input_tokens": 23980,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 504
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

_source line 10 · 2026-05-23T15:03:52.329Z_

<details><summary>↩ Tool result · `toolu_0171EUdkA3ZCg52wTyRVv9fw`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2567}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9dd1310f-2eca-4936-af7c-90a1b8a75881",
  "uuid": "ace8d17a-dd6b-4643-9605-1d718b866e6e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.2567}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2567}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 11_

<details><summary>Logged reasoning block</summary>

```text
The exact exp_id filters didn't match. Let me try broader searches to find these experiments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9dd1310f-2eca-4936-af7c-90a1b8a75881",
  "uuid": "4289f563-e92f-401c-9ef3-43678651061e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VGZAW9MZmAkpPxDmXzcpPg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 441,
      "cache_read_input_tokens": 24484,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 441
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

_source line 12_

没找到精确匹配，试试更宽泛的搜索。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9dd1310f-2eca-4936-af7c-90a1b8a75881",
  "uuid": "4d10fe94-4cde-4419-a055-3a68fc361258",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VGZAW9MZmAkpPxDmXzcpPg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 441,
      "cache_read_input_tokens": 24484,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 441
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

_source line 13_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_019NB5YKge5eUN1a4raf16Tc`</summary>

```json
{
  "project": "irt_personfit_contam",
  "filters": {
    "status": "DONE"
  },
  "fields": [
    "exp_id",
    "status",
    "metrics",
    "config"
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
  "session_id": "9dd1310f-2eca-4936-af7c-90a1b8a75881",
  "uuid": "cfda9b9c-ba06-420e-8804-9d3dc59252a5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VGZAW9MZmAkpPxDmXzcpPg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 441,
      "cache_read_input_tokens": 24484,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 441
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

_source line 14 · 2026-05-23T15:03:56.436Z_

<details><summary>↩ Tool result · `toolu_019NB5YKge5eUN1a4raf16Tc`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp-ctrl-contam-qwen-25pct-s2\": {\"status\": \"DONE\"}, \"exp-ctrl-contam-qwen-15pct-multiseed\": {\"status\": \"DONE\", \"metrics\": {\"seed_42\": {\"lz_star_free\": 3.8494, \"d_free\": -6.57, \"d_free_ci\": [-15.19, -4.54], \"d_fixed\": 4.77, \"d_fixed_ci\": [3.96, 7.76]}, \"seed_123\": {\"lz_star_free\": 4.939, \"d_free\": -5.09, \"d_free_ci\": [-11.72, -3.44], \"d_fixed\": 7.79, \"d_fixed_ci\": [6.51, 13.05]}, \"seed_456\": {\"lz_star_free\": 5.44, \"d_free\": -4.41, \"lz_fixed\": 11.99, \"d_fixed\": 7.99, \"d_fixed_ci\": [6.68, 13.4]}, \"stats_free\": {\"mean_abs_d\": 5.36, \"sd\": 1.1, \"cv\": 0.206, \"range\": [4.41, 6.57]}, \"stats_fixed\": {\"mean_abs_d\": 6.85, \"sd\": 1.8, \"cv\": 0.263, \"range\": [4.77, 7.99]}, \"n_seeds\": 3, \"clean_baseline_free\": {\"n\": 10, \"mean\": 8.6838, \"std\": 0.7353}, \"clean_baseline_fixed\": {\"n\": 10, \"mean\": 7.3522, \"std\": 0.5802, \"theta_fixed\": -0.1022}}}, \"exp-ctrl-contam-qwen-50pct-multiseed\": {\"status\": \"DONE\", \"metrics\": {\"seed_42\": {\"lz_star_free\": 7.2892, \"d_free\": -1.9, \"lz_fixed\": null, \"d_fixed\": 14.52}, \"seed_123\": {\"lz_star_free\": 4.7, \"d_free\": -5.42, \"lz_fixed\": 14.687, \"d_fixed\": 12.64, \"d_fixed_ci\": [10.54, 21.46]}, \"seed_456\": {\"lz_star_free\": 2.8695, \"d_free\": -7.91, \"d_free_ci\": [-18.29, -5.52], \"lz_fixed\": 13.036, \"d_fixed\": 9.8, \"d_fixed_ci\": [8.18, 16.46]}, \"stats_free\": {\"mean_abs_d\": 5.08, \"sd\": 3.02, \"cv\": 0.595, \"range\": [1.9, 7.91]}, \"stats_fixed\": {\"mean_abs_d\": 12.32, \"sd\": 2.38, \"cv\": 0.193, \"range\": [9.8, 14.52]}, \"n_seeds\": 3, \"clean_baseline_free\": {\"n\": 10, \"mean\": 8.6838, \"std\": 0.7353}, \"clean_baseline_fixed\": {\"n\": 10, \"mean\": 7.3522, \"std\": 0.5802, \"theta_fixed\": -0.1022}}}, \"exp-ctrl-contam-qwen-25pct-multiseed\": {\"status\": \"DONE\", \"metrics\": {\"seed_42\": {\"lz_star_free\": 2.6429, \"d_free\": -8.22, \"lz_fixed\": 10.229, \"d_fixed\": 4.96, \"d_fixed_ci\": [4.13, 8.12]}, \"seed_123\": {\"lz_star_free\": 2.23, \"d_free\": -8.78, \"lz_fixed\": 10.47, \"d_fixed\": 5.37, \"d_fixed_ci\": [4.48, 8.83]}, \"seed_456\": {\"lz_star_free\": 4.78, \"d_free\": -5.31, \"lz_fixed\": 11.611, \"d_fixed\": 7.34, \"d_fixed_ci\": [6.14, 12.26]}, \"stats_free\": {\"mean_abs_d\": 7.44, \"sd\": 1.86, \"cv\": 0.25, \"range\": [5.31, 8.78]}, \"stats_fixed\": {\"mean_abs_d\": 5.89, \"sd\": 1.27, \"cv\": 0.216, \"range\": [4.96, 7.34]}, \"n_seeds\": 3, \"clean_baseline_free\": {\"n\": 10, \"mean\": 8.6838, \"std\": 0.7353}, \"clean_baseline_fixed\": {\"n\": 10, \"mean\": 7.3522, \"std\": 0.5802, \"theta_fixed\": -0.1022}}}, \"exp-ctrl-contam-qwen-15pct-s2\": {\"status\": \"DONE\"}, \"exp-ctrl-contam-llama-5pct\": {\"status\": \"DONE\", \"metrics\": {\"theta_mle\": -0.4089, \"lz_star_free\": -4.954, \"lz_star_fixed\": -1.8923, \"accuracy_overall\": 0.6342, \"accuracy_seen\": 0.792, \"accuracy_unseen\": 0.6259, \"n_items\": 14042, \"n_seen\": 702, \"cohens_d_free\": {\"d\": -5.5254, \"ci_95\": [-10.8, -4.05]}, \"cohens_d_fixed\": {\"d\": -1.7027, \"ci_95\": [-3.87, -1.2]}}}, \"exp-ctrl-contam-qwen-5pct\": {\"status\": \"DONE\", \"metrics\": {\"theta_mle\": 0.0879, \"lz_star_free\": 5.6309, \"lz_star_fixed\": 11.09, \"accuracy_overall\": 0.7141, \"accuracy_seen\": 0.8291, \"accuracy_unseen\": 0.708, \"n_items\": 14042, \"n_seen\": 702, \"train_loss\": 1.39, \"train_runtime_sec\": 1127, \"cohens_d_free\": {\"d\": -4.1518, \"ci_95\": [-9.8505, -2.7418]}, \"cohens_d_fixed\": {\"d\": 3.5156, \"ci_95\": [2.8999, 5.7097]}}}, \"exp-ctrl-contam-mistral\": {\"status\": \"DONE\", \"metrics\": {\"n_seeds\": 10, \"clean_lz_values\": [5.4175, -1.0456, 3.2792, 3.9558, 4.491, 5.503, 5.8982, 5.7996, 3.5214, 3.4159], \"clean_lz_mean\": 4.0236, \"clean_lz_std\": 2.052, \"contam_15_lz\": -2.1468, \"contam_50_lz\": -3.1539, \"cohens_d_contam15\": -3.007, \"cohens_d_contam15_ci95\": [-8.18, -1.75], \"cohens_d_contam50\": -3.498, \"cohens_d_contam50_ci95\": [-9.39, -2.09], \"bootstrap_n\": 10000, \"theta_fixed\": -1.0876, \"theta_fixed_n_theta\": 10, \"theta_fixed_n_lz\": 6, \"theta_fixed_clean_lz\": [5.3714, -1.3154, 3.0571, 5.769, 3.5155, 3.3474], \"theta_fixed_clean_lz_seeds\": [\"s1\", \"s2\", \"s3\", \"s8\", \"s9\", \"s10\"], \"cohens_d_contam15_theta_fixed\": 2.69, \"cohens_d_contam15_theta_fixed_ci95\": [1.53, 9.06], \"cohens_d_contam50_theta_fixed\": 5.8, \"cohens_d_contam50_theta_fixed_ci95\": [3.87, 18.45], \"note\": \"2026-05-22: Free-theta d uses n=10 (all seeds). theta_fixed uses n=10 theta_MLE mean (-1.0876), but lz*_fixed distribution only n=6 (s4-s7 response vectors lost with server 19912).\"}}, \"exp-ctrl-contam-llama-25pct\": {\"status\": \"DONE\", \"metrics\": {\"lz_star_snijders\": -2.8045, \"accuracy_overall\": 0.6781, \"accuracy_seen\": 0.7715, \"accuracy_unseen\": 0.647, \"theta_mle\": -0.2207, \"cohens_d\": -2.9667, \"cohens_d_ci95_percentile\": [-6.06, -2.03], \"cohens_d_ci95_bca\": [-4.74, -1.64], \"bootstrap_n\": 10000, \"clean_baseline\": {\"n\": 10, \"lz_star_mean\": -0.3123, \"lz_star_std_ddof1\": 0.8401}}}, \"exp-ctrl-contam-qwen-25pct\": {\"status\": \"DONE\", \"metrics\": {\"lz_star_snijders\": 2.6429, \"accuracy_overall\": 0.7405, \"accuracy_seen\": 0.8105, \"accuracy_unseen\": 0.7171, \"theta_mle\": 0.2576, \"cohens_d\": -8.2153, \"cohens_d_ci95_percentile\": [-18.88, -5.73], \"cohens_d_ci95_bca\": [-14.71, -4.94], \"bootstrap_n\": 10000, \"clean_baseline\": {\"n\": 10, \"lz_star_mean\": 8.6838, \"lz_star_std\": 0.7353, \"source\": \"unified_lz_recompute.py (Snijders 2001)\"}}}, \"exp-ctrl-contam-llama\": {\"status\": \"DONE\", \"metrics\": {\"n_seeds\": 10, \"clean_lz_values\": [-0.4891, -0.7793, 0.4109, 0.6498, -0.3043, -1.1483, 0.1419, 0.7175, -0.3718, -1.9506], \"clean_lz_mean\": -0.3123, \"clean_lz_std\": 0.8296, \"contam_15_lz\": -2.1955, \"contam_50_lz\": -2.3897, \"cohens_d_contam15\": -2.269, \"cohens_d_contam15_ci95\": [-4.63, -1.561], \"cohens_d_contam50\": -2.503, \"cohens_d_contam50_ci95\": [-5.19, -1.759], \"bootstrap_n\": 10000, \"theta_fixed\": -0.6426, \"cohens_d_contam15_theta_fixed\": -0.58, \"cohens_d_contam15_theta_fixed_ci95\": [-2.37, 0.04], \"cohens_d_contam50_theta_fixed\": -0.84, \"cohens_d_contam50_theta_fixed_ci95\": [-2.97, -0.17]}}, \"exp-ctrl-contam-pilot\": {\"status\": \"DONE\", \"metrics\": {\"n_seeds\": 10, \"source\": \"unified_lz_recompute.py (single-source Snijders 2001)\", \"clean_lz_star_snijders\": [9.4676, 7.0539, 9.5293, 8.9673, 8.5322, 8.2445, 8.7702, 9.111, 9.0132, 8.1492], \"clean_lz_star_mean\": 8.6838, \"clean_lz_star_std\": 0.7353, \"clean_lz_drasgow\": [8.0101, 5.944, 8.0806, 7.609, 7.1963, 6.9848, 7.4005, 7.7188, 7.6799, 6.9272], \"contam_15_lz_star\": 3.8494, \"contam_50_lz_star\": 7.2892, \"contam_15_lz_drasgow\": 3.0046, \"contam_50_lz_drasgow\": 5.448, \"cohens_d_contam15_lz_star\": -6.575, \"cohens_d_contam15_lz_star_bootstrap\": [-15.19, -4.54], \"cohens_d_contam50_lz_star\": -1.897, \"cohens_d_contam50_lz_star_bootstrap\": [-4.95, -1.04], \"theta_fixed\": -0.1022, \"cohens_d_contam15_theta_fixed\": 4.77, \"cohens_d_contam15_theta_fixed_bootstrap\": [3.97, 7.79], \"cohens_d_contam50_theta_fixed\": 14.521, \"cohens_d_contam50_theta_fixed_bootstrap\": [12.1, 24.79], \"bootstrap_n\": 10000, \"note\": \"Unified recomputation 2026-05-21. θ-fixed d identical for lz and lz* (correction factor cancels when θ constant).\"}}, \"exp-ctrl-contam-mistral-clean-s10\": {\"status\": \"DONE\", \"metrics\": {\"accuracy_overall\": 0.5347, \"lz_star\": 3.4159, \"theta_mle\": -1.0286, \"n_items\": 14042}}, \"exp-ctrl-contam-mistral-clean-s9\": {\"status\": \"DONE\", \"metrics\": {\"accuracy_overall\": 0.5165, \"lz_star\": 3.5214, \"theta_mle\": -1.124, \"n_items\": 14042}}, \"exp-ctrl-contam-mistral-clean-s8\": {\"status\": \"DONE\", \"metrics\": {\"accuracy_overall\": 0.5162, \"lz_star\": 5.7996, \"theta_mle\": -1.1457, \"n_items\": 14042}}, \"exp-ctrl-contam-mistral-clean-s7\": {\"status\": \"DONE\", \"metrics\": {\"accuracy_overall\": 0.5284, \"lz_star\": 5.8982, \"theta_mle\": -1.0755, \"n_items\": 14042}}, \"exp-ctrl-contam-mistral-clean-s6\": {\"status\": \"DONE\", \"metrics\": {\"accuracy_overall\": 0.5128, \"lz_star\": 5.503, \"theta_mle\": -1.1405, \"n_items\": 14042}}, \"exp-ctrl-contam-mistral-clean-s5\": {\"status\": \"DONE\", \"metrics\": {\"accuracy_overall\": 0.5231, \"lz_star\": 4.491, \"theta_mle\": -1.1, \"n_items\": 14042}}, \"exp-ctrl-contam-mistral-clean-s4\": {\"status\": \"DONE\", \"metrics\": {\"accuracy_overall\": 0.5105, \"lz_star\": 3.9558, \"theta_mle\": -1.1693, \"n_items\": 14042}}, \"llama_clean_s10\": {\"status\": \"DONE\"}, \"llama_clean_s9\": {\"status\": \"DONE\"}, \"llama_clean_s8\": {\"status\": \"DONE\"}, \"llama_clean_s11\": {\"status\": \"DONE\"}, \"exp-post-rl-v3\": {\"status\": \"DONE\", \"metrics\": {\"step500_theta\": 0.157, \"step500_lz_star\": 7.771, \"step500_acc_overall\": 0.7144, \"step500_acc_seen\": 0.7303, \"step500_acc_unseen\": 0.7116, \"step500_lz_seen\": 3.41, \"step500_lz_unseen\": 7, \"step500_ht_param\": -0.0349, \"step500_ht_param_seen\": -0.0282, \"step500_ht_nonparam\": 0.1678, \"step1000_theta\": 0.155, \"step1000_lz_star\": 7.803, \"step1000_acc_overall\": 0.7143, \"step1000_acc_seen\": 0.7308, \"step1000_acc_unseen\": 0.7114, \"step1000_lz_seen\": 3.625, \"step1000_lz_unseen\": 6.948, \"step1000_ht_param\": -0.0348, \"step1500_theta\": 0.152, \"step1500_lz_star\": 7.686, \"step1500_acc_overall\": 0.7141, \"step1500_acc_seen\": 0.7322, \"step1500_acc_unseen\": 0.711, \"step1500_lz_seen\": 3.539, \"step1500_lz_unseen\": 6.859, \"step1500_ht_param\": -0.0341, \"sft_baseline_lz_star\": 2.914, \"sft_baseline_acc\": 0.7339, \"sft_baseline_acc_seen\": 0.831, \"delta_lz_sft_to_grpo\": 4.857, \"delta_acc_seen_sft_to_grpo\": -0.1007, \"checkpoint_stability\": \"all metrics <3% change after step 500, plateau pattern confirmed\"}}, \"exp-ctrl-contam-llama-clean-s10\": {\"status\": \"DONE\", \"metrics\": {\"theta_mle\": -0.621, \"lz_star\": -2.25, \"accuracy_overall\": 0.595, \"n_items\": 14042}}, \"exp-ctrl-contam-llama-clean-s9\": {\"status\": \"DONE\", \"metrics\": {\"theta_mle\": -0.659, \"lz_star\": 0.19, \"accuracy_overall\": 0.592, \"n_items\": 14042}}, \"exp-ctrl-contam-llama-clean-s8\": {\"status\": \"DONE\", \"metrics\": {\"theta_mle\": -0.698, \"lz_star\": 1.166, \"accuracy_overall\": 0.586, \"n_items\": 14042}}, \"exp-arcc-clean-s10\": {\"status\": \"DONE\", \"metrics\": {\"theta_mle\": 0.8111, \"lz_star\": -5.0733, \"accuracy\": 0.9051, \"n_items\": 295}}, \"exp-arcc-clean-s9\": {\"status\": \"DONE\", \"metrics\": {\"theta_mle\": 0.8868, \"lz_star\": -5.5359, \"accuracy\": 0.9017, \"n_items\": 295}}, \"exp-arcc-clean-s8\": {\"status\": \"DONE\", \"metrics\": {\"theta_mle\": 0.8511, \"lz_star\": -5.4001, \"accuracy\": 0.9051, \"n_items\": 295}}}, \"count\": 30, \"total\": 73, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2316}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9dd1310f-2eca-4936-af7c-90a1b8a75881",
  "uuid": "8f7fb452-5761-478b-9714-37e37ee1e1f6",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"exp-ctrl-contam-qwen-25pct-s2\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"exp-ctrl-contam-qwen-15pct-multiseed\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"seed_42\\\": {\\\"lz_star_free\\\": 3.8494, \\\"d_free\\\": -6.57, \\\"d_free_ci\\\": [-15.19, -4.54], \\\"d_fixed\\\": 4.77, \\\"d_fixed_ci\\\": [3.96, 7.76]}, \\\"seed_123\\\": {\\\"lz_star_free\\\": 4.939, \\\"d_free\\\": -5.09, \\\"d_free_ci\\\": [-11.72, -3.44], \\\"d_fixed\\\": 7.79, \\\"d_fixed_ci\\\": [6.51, 13.05]}, \\\"seed_456\\\": {\\\"lz_star_free\\\": 5.44, \\\"d_free\\\": -4.41, \\\"lz_fixed\\\": 11.99, \\\"d_fixed\\\": 7.99, \\\"d_fixed_ci\\\": [6.68, 13.4]}, \\\"stats_free\\\": {\\\"mean_abs_d\\\": 5.36, \\\"sd\\\": 1.1, \\\"cv\\\": 0.206, \\\"range\\\": [4.41, 6.57]}, \\\"stats_fixed\\\": {\\\"mean_abs_d\\\": 6.85, \\\"sd\\\": 1.8, \\\"cv\\\": 0.263, \\\"range\\\": [4.77, 7.99]}, \\\"n_seeds\\\": 3, \\\"clean_baseline_free\\\": {\\\"n\\\": 10, \\\"mean\\\": 8.6838, \\\"std\\\": 0.7353}, \\\"clean_baseline_fixed\\\": {\\\"n\\\": 10, \\\"mean\\\": 7.3522, \\\"std\\\": 0.5802, \\\"theta_fixed\\\": -0.1022}}}, \\\"exp-ctrl-contam-qwen-50pct-multiseed\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"seed_42\\\": {\\\"lz_star_free\\\": 7.2892, \\\"d_free\\\": -1.9, \\\"lz_fixed\\\": null, \\\"d_fixed\\\": 14.52}, \\\"seed_123\\\": {\\\"lz_star_free\\\": 4.7, \\\"d_free\\\": -5.42, \\\"lz_fixed\\\": 14.687, \\\"d_fixed\\\": 12.64, \\\"d_fixed_ci\\\": [10.54, 21.46]}, \\\"seed_456\\\": {\\\"lz_star_free\\\": 2.8695, \\\"d_free\\\": -7.91, \\\"d_free_ci\\\": [-18.29, -5.52], \\\"lz_fixed\\\": 13.036, \\\"d_fixed\\\": 9.8, \\\"d_fixed_ci\\\": [8.18, 16.46]}, \\\"stats_free\\\": {\\\"mean_abs_d\\\": 5.08, \\\"sd\\\": 3.02, \\\"cv\\\": 0.595, \\\"range\\\": [1.9, 7.91]}, \\\"stats_fixed\\\": {\\\"mean_abs_d\\\": 12.32, \\\"sd\\\": 2.38, \\\"cv\\\": 0.193, \\\"range\\\": [9.8, 14.52]}, \\\"n_seeds\\\": 3, \\\"clean_baseline_free\\\": {\\\"n\\\": 10, \\\"mean\\\": 8.6838, \\\"std\\\": 0.7353}, \\\"clean_baseline_fixed\\\": {\\\"n\\\": 10, \\\"mean\\\": 7.3522, \\\"std\\\": 0.5802, \\\"theta_fixed\\\": -0.1022}}}, \\\"exp-ctrl-contam-qwen-25pct-multiseed\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"seed_42\\\": {\\\"lz_star_free\\\": 2.6429, \\\"d_free\\\": -8.22, \\\"lz_fixed\\\": 10.229, \\\"d_fixed\\\": 4.96, \\\"d_fixed_ci\\\": [4.13, 8.12]}, \\\"seed_123\\\": {\\\"lz_star_free\\\": 2.23, \\\"d_free\\\": -8.78, \\\"lz_fixed\\\": 10.47, \\\"d_fixed\\\": 5.37, \\\"d_fixed_ci\\\": [4.48, 8.83]}, \\\"seed_456\\\": {\\\"lz_star_free\\\": 4.78, \\\"d_free\\\": -5.31, \\\"lz_fixed\\\": 11.611, \\\"d_fixed\\\": 7.34, \\\"d_fixed_ci\\\": [6.14, 12.26]}, \\\"stats_free\\\": {\\\"mean_abs_d\\\": 7.44, \\\"sd\\\": 1.86, \\\"cv\\\": 0.25, \\\"range\\\": [5.31, 8.78]}, \\\"stats_fixed\\\": {\\\"mean_abs_d\\\": 5.89, \\\"sd\\\": 1.27, \\\"cv\\\": 0.216, \\\"range\\\": [4.96, 7.34]}, \\\"n_seeds\\\": 3, \\\"clean_baseline_free\\\": {\\\"n\\\": 10, \\\"mean\\\": 8.6838, \\\"std\\\": 0.7353}, \\\"clean_baseline_fixed\\\": {\\\"n\\\": 10, \\\"mean\\\": 7.3522, \\\"std\\\": 0.5802, \\\"theta_fixed\\\": -0.1022}}}, \\\"exp-ctrl-contam-qwen-15pct-s2\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"exp-ctrl-contam-llama-5pct\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"theta_mle\\\": -0.4089, \\\"lz_star_free\\\": -4.954, \\\"lz_star_fixed\\\": -1.8923, \\\"accuracy_overall\\\": 0.6342, \\\"accuracy_seen\\\": 0.792, \\\"accuracy_unseen\\\": 0.6259, \\\"n_items\\\": 14042, \\\"n_seen\\\": 702, \\\"cohens_d_free\\\": {\\\"d\\\": -5.5254, \\\"ci_95\\\": [-10.8, -4.05]}, \\\"cohens_d_fixed\\\": {\\\"d\\\": -1.7027, \\\"ci_95\\\": [-3.87, -1.2]}}}, \\\"exp-ctrl-contam-qwen-5pct\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"theta_mle\\\": 0.0879, \\\"lz_star_free\\\": 5.6309, \\\"lz_star_fixed\\\": 11.09, \\\"accuracy_overall\\\": 0.7141, \\\"accuracy_seen\\\": 0.8291, \\\"accuracy_unseen\\\": 0.708, \\\"n_items\\\": 14042, \\\"n_seen\\\": 702, \\\"train_loss\\\": 1.39, \\\"train_runtime_sec\\\": 1127, \\\"cohens_d_free\\\": {\\\"d\\\": -4.1518, \\\"ci_95\\\": [-9.8505, -2.7418]}, \\\"cohens_d_fixed\\\": {\\\"d\\\": 3.5156, \\\"ci_95\\\": [2.8999, 5.7097]}}}, \\\"exp-ctrl-contam-mistral\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"n_seeds\\\": 10, \\\"clean_lz_values\\\": [5.4175, -1.0456, 3.2792, 3.9558, 4.491, 5.503, 5.8982, 5.7996, 3.5214, 3.4159], \\\"clean_lz_mean\\\": 4.0236, \\\"clean_lz_std\\\": 2.052, \\\"contam_15_lz\\\": -2.1468, \\\"contam_50_lz\\\": -3.1539, \\\"cohens_d_contam15\\\": -3.007, \\\"cohens_d_contam15_ci95\\\": [-8.18, -1.75], \\\"cohens_d_contam50\\\": -3.498, \\\"cohens_d_contam50_ci95\\\": [-9.39, -2.09], \\\"bootstrap_n\\\": 10000, \\\"theta_fixed\\\": -1.0876, \\\"theta_fixed_n_theta\\\": 10, \\\"theta_fixed_n_lz\\\": 6, \\\"theta_fixed_clean_lz\\\": [5.3714, -1.3154, 3.0571, 5.769, 3.5155, 3.3474], \\\"theta_fixed_clean_lz_seeds\\\": [\\\"s1\\\", \\\"s2\\\", \\\"s3\\\", \\\"s8\\\", \\\"s9\\\", \\\"s10\\\"], \\\"cohens_d_contam15_theta_fixed\\\": 2.69, \\\"cohens_d_contam15_theta_fixed_ci95\\\": [1.53, 9.06], \\\"cohens_d_contam50_theta_fixed\\\": 5.8, \\\"cohens_d_contam50_theta_fixed_ci95\\\": [3.87, 18.45], \\\"note\\\": \\\"2026-05-22: Free-theta d uses n=10 (all seeds). theta_fixed uses n=10 theta_MLE mean (-1.0876), but lz*_fixed distribution only n=6 (s4-s7 response vectors lost with server 19912).\\\"}}, \\\"exp-ctrl-contam-llama-25pct\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"lz_star_snijders\\\": -2.8045, \\\"accuracy_overall\\\": 0.6781, \\\"accuracy_seen\\\": 0.7715, \\\"accuracy_unseen\\\": 0.647, \\\"theta_mle\\\": -0.2207, \\\"cohens_d\\\": -2.9667, \\\"cohens_d_ci95_percentile\\\": [-6.06, -2.03], \\\"cohens_d_ci95_bca\\\": [-4.74, -1.64], \\\"bootstrap_n\\\": 10000, \\\"clean_baseline\\\": {\\\"n\\\": 10, \\\"lz_star_mean\\\": -0.3123, \\\"lz_star_std_ddof1\\\": 0.8401}}}, \\\"exp-ctrl-contam-qwen-25pct\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"lz_star_snijders\\\": 2.6429, \\\"accuracy_overall\\\": 0.7405, \\\"accuracy_seen\\\": 0.8105, \\\"accuracy_unseen\\\": 0.7171, \\\"theta_mle\\\": 0.2576, \\\"cohens_d\\\": -8.2153, \\\"cohens_d_ci95_percentile\\\": [-18.88, -5.73], \\\"cohens_d_ci95_bca\\\": [-14.71, -4.94], \\\"bootstrap_n\\\": 10000, \\\"clean_baseline\\\": {\\\"n\\\": 10, \\\"lz_star_mean\\\": 8.6838, \\\"lz_star_std\\\": 0.7353, \\\"source\\\": \\\"unified_lz_recompute.py (Snijders 2001)\\\"}}}, \\\"exp-ctrl-contam-llama\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"n_seeds\\\": 10, \\\"clean_lz_values\\\": [-0.4891, -0.7793, 0.4109, 0.6498, -0.3043, -1.1483, 0.1419, 0.7175, -0.3718, -1.9506], \\\"clean_lz_mean\\\": -0.3123, \\\"clean_lz_std\\\": 0.8296, \\\"contam_15_lz\\\": -2.1955, \\\"contam_50_lz\\\": -2.3897, \\\"cohens_d_contam15\\\": -2.269, \\\"cohens_d_contam15_ci95\\\": [-4.63, -1.561], \\\"cohens_d_contam50\\\": -2.503, \\\"cohens_d_contam50_ci95\\\": [-5.19, -1.759], \\\"bootstrap_n\\\": 10000, \\\"theta_fixed\\\": -0.6426, \\\"cohens_d_contam15_theta_fixed\\\": -0.58, \\\"cohens_d_contam15_theta_fixed_ci95\\\": [-2.37, 0.04], \\\"cohens_d_contam50_theta_fixed\\\": -0.84, \\\"cohens_d_contam50_theta_fixed_ci95\\\": [-2.97, -0.17]}}, \\\"exp-ctrl-contam-pilot\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"n_seeds\\\": 10, \\\"source\\\": \\\"unified_lz_recompute.py (single-source Snijders 2001)\\\", \\\"clean_lz_star_snijders\\\": [9.4676, 7.0539, 9.5293, 8.9673, 8.5322, 8.2445, 8.7702, 9.111, 9.0132, 8.1492], \\\"clean_lz_star_mean\\\": 8.6838, \\\"clean_lz_star_std\\\": 0.7353, \\\"clean_lz_drasgow\\\": [8.0101, 5.944, 8.0806, 7.609, 7.1963, 6.9848, 7.4005, 7.7188, 7.6799, 6.9272], \\\"contam_15_lz_star\\\": 3.8494, \\\"contam_50_lz_star\\\": 7.2892, \\\"contam_15_lz_drasgow\\\": 3.0046, \\\"contam_50_lz_drasgow\\\": 5.448, \\\"cohens_d_contam15_lz_star\\\": -6.575, \\\"cohens_d_contam15_lz_star_bootstrap\\\": [-15.19, -4.54], \\\"cohens_d_contam50_lz_star\\\": -1.897, \\\"cohens_d_contam50_lz_star_bootstrap\\\": [-4.95, -1.04], \\\"theta_fixed\\\": -0.1022, \\\"cohens_d_contam15_theta_fixed\\\": 4.77, \\\"cohens_d_contam15_theta_fixed_bootstrap\\\": [3.97, 7.79], \\\"cohens_d_contam50_theta_fixed\\\": 14.521, \\\"cohens_d_contam50_theta_fixed_bootstrap\\\": [12.1, 24.79], \\\"bootstrap_n\\\": 10000, \\\"note\\\": \\\"Unified recomputation 2026-05-21. θ-fixed d identical for lz and lz* (correction factor cancels when θ constant).\\\"}}, \\\"exp-ctrl-contam-mistral-clean-s10\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"accuracy_overall\\\": 0.5347, \\\"lz_star\\\": 3.4159, \\\"theta_mle\\\": -1.0286, \\\"n_items\\\": 14042}}, \\\"exp-ctrl-contam-mistral-clean-s9\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"accuracy_overall\\\": 0.5165, \\\"lz_star\\\": 3.5214, \\\"theta_mle\\\": -1.124, \\\"n_items\\\": 14042}}, \\\"exp-ctrl-contam-mistral-clean-s8\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"accuracy_overall\\\": 0.5162, \\\"lz_star\\\": 5.7996, \\\"theta_mle\\\": -1.1457, \\\"n_items\\\": 14042}}, \\\"exp-ctrl-contam-mistral-clean-s7\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"accuracy_overall\\\": 0.5284, \\\"lz_star\\\": 5.8982, \\\"theta_mle\\\": -1.0755, \\\"n_items\\\": 14042}}, \\\"exp-ctrl-contam-mistral-clean-s6\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"accuracy_overall\\\": 0.5128, \\\"lz_star\\\": 5.503, \\\"theta_mle\\\": -1.1405, \\\"n_items\\\": 14042}}, \\\"exp-ctrl-contam-mistral-clean-s5\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"accuracy_overall\\\": 0.5231, \\\"lz_star\\\": 4.491, \\\"theta_mle\\\": -1.1, \\\"n_items\\\": 14042}}, \\\"exp-ctrl-contam-mistral-clean-s4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"accuracy_overall\\\": 0.5105, \\\"lz_star\\\": 3.9558, \\\"theta_mle\\\": -1.1693, \\\"n_items\\\": 14042}}, \\\"llama_clean_s10\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"llama_clean_s9\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"llama_clean_s8\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"llama_clean_s11\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"exp-post-rl-v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"step500_theta\\\": 0.157, \\\"step500_lz_star\\\": 7.771, \\\"step500_acc_overall\\\": 0.7144, \\\"step500_acc_seen\\\": 0.7303, \\\"step500_acc_unseen\\\": 0.7116, \\\"step500_lz_seen\\\": 3.41, \\\"step500_lz_unseen\\\": 7, \\\"step500_ht_param\\\": -0.0349, \\\"step500_ht_param_seen\\\": -0.0282, \\\"step500_ht_nonparam\\\": 0.1678, \\\"step1000_theta\\\": 0.155, \\\"step1000_lz_star\\\": 7.803, \\\"step1000_acc_overall\\\": 0.7143, \\\"step1000_acc_seen\\\": 0.7308, \\\"step1000_acc_unseen\\\": 0.7114, \\\"step1000_lz_seen\\\": 3.625, \\\"step1000_lz_unseen\\\": 6.948, \\\"step1000_ht_param\\\": -0.0348, \\\"step1500_theta\\\": 0.152, \\\"step1500_lz_star\\\": 7.686, \\\"step1500_acc_overall\\\": 0.7141, \\\"step1500_acc_seen\\\": 0.7322, \\\"step1500_acc_unseen\\\": 0.711, \\\"step1500_lz_seen\\\": 3.539, \\\"step1500_lz_unseen\\\": 6.859, \\\"step1500_ht_param\\\": -0.0341, \\\"sft_baseline_lz_star\\\": 2.914, \\\"sft_baseline_acc\\\": 0.7339, \\\"sft_baseline_acc_seen\\\": 0.831, \\\"delta_lz_sft_to_grpo\\\": 4.857, \\\"delta_acc_seen_sft_to_grpo\\\": -0.1007, \\\"checkpoint_stability\\\": \\\"all metrics <3% change after step 500, plateau pattern confirmed\\\"}}, \\\"exp-ctrl-contam-llama-clean-s10\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"theta_mle\\\": -0.621, \\\"lz_star\\\": -2.25, \\\"accuracy_overall\\\": 0.595, \\\"n_items\\\": 14042}}, \\\"exp-ctrl-contam-llama-clean-s9\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"theta_mle\\\": -0.659, \\\"lz_star\\\": 0.19, \\\"accuracy_overall\\\": 0.592, \\\"n_items\\\": 14042}}, \\\"exp-ctrl-contam-llama-clean-s8\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"theta_mle\\\": -0.698, \\\"lz_star\\\": 1.166, \\\"accuracy_overall\\\": 0.586, \\\"n_items\\\": 14042}}, \\\"exp-arcc-clean-s10\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"theta_mle\\\": 0.8111, \\\"lz_star\\\": -5.0733, \\\"accuracy\\\": 0.9051, \\\"n_items\\\": 295}}, \\\"exp-arcc-clean-s9\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"theta_mle\\\": 0.8868, \\\"lz_star\\\": -5.5359, \\\"accuracy\\\": 0.9017, \\\"n_items\\\": 295}}, \\\"exp-arcc-clean-s8\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"theta_mle\\\": 0.8511, \\\"lz_star\\\": -5.4001, \\\"accuracy\\\": 0.9051, \\\"n_items\\\": 295}}}, \\\"count\\\": 30, \\\"total\\\": 73, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.2316}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"exp-ctrl-contam-qwen-25pct-s2\": {\"status\": \"DONE\"}, \"exp-ctrl-contam-qwen-15pct-multiseed\": {\"status\": \"DONE\", \"metrics\": {\"seed_42\": {\"lz_star_free\": 3.8494, \"d_free\": -6.57, \"d_free_ci\": [-15.19, -4.54], \"d_fixed\": 4.77, \"d_fixed_ci\": [3.96, 7.76]}, \"seed_123\": {\"lz_star_free\": 4.939, \"d_free\": -5.09, \"d_free_ci\": [-11.72, -3.44], \"d_fixed\": 7.79, \"d_fixed_ci\": [6.51, 13.05]}, \"seed_456\": {\"lz_star_free\": 5.44, \"d_free\": -4.41, \"lz_fixed\": 11.99, \"d_fixed\": 7.99, \"d_fixed_ci\": [6.68, 13.4]}, \"stats_free\": {\"mean_abs_d\": 5.36, \"sd\": 1.1, \"cv\": 0.206, \"range\": [4.41, 6.57]}, \"stats_fixed\": {\"mean_abs_d\": 6.85, \"sd\": 1.8, \"cv\": 0.263, \"range\": [4.77, 7.99]}, \"n_seeds\": 3, \"clean_baseline_free\": {\"n\": 10, \"mean\": 8.6838, \"std\": 0.7353}, \"clean_baseline_fixed\": {\"n\": 10, \"mean\": 7.3522, \"std\": 0.5802, \"theta_fixed\": -0.1022}}}, \"exp-ctrl-contam-qwen-50pct-multiseed\": {\"status\": \"DONE\", \"metrics\": {\"seed_42\": {\"lz_star_free\": 7.2892, \"d_free\": -1.9, \"lz_fixed\": null, \"d_fixed\": 14.52}, \"seed_123\": {\"lz_star_free\": 4.7, \"d_free\": -5.42, \"lz_fixed\": 14.687, \"d_fixed\": 12.64, \"d_fixed_ci\": [10.54, 21.46]}, \"seed_456\": {\"lz_star_free\": 2.8695, \"d_free\": -7.91, \"d_free_ci\": [-18.29, -5.52], \"lz_fixed\": 13.036, \"d_fixed\": 9.8, \"d_fixed_ci\": [8.18, 16.46]}, \"stats_free\": {\"mean_abs_d\": 5.08, \"sd\": 3.02, \"cv\": 0.595, \"range\": [1.9, 7.91]}, \"stats_fixed\": {\"mean_abs_d\": 12.32, \"sd\": 2.38, \"cv\": 0.193, \"range\": [9.8, 14.52]}, \"n_seeds\": 3, \"clean_baseline_free\": {\"n\": 10, \"mean\": 8.6838, \"std\": 0.7353}, \"clean_baseline_fixed\": {\"n\": 10, \"mean\": 7.3522, \"std\": 0.5802, \"theta_fixed\": -0.1022}}}, \"exp-ctrl-contam-qwen-25pct-multiseed\": {\"status\": \"DONE\", \"metrics\": {\"seed_42\": {\"lz_star_free\": 2.6429, \"d_free\": -8.22, \"lz_fixed\": 10.229, \"d_fixed\": 4.96, \"d_fixed_ci\": [4.13, 8.12]}, \"seed_123\": {\"lz_star_free\": 2.23, \"d_free\": -8.78, \"lz_fixed\": 10.47, \"d_fixed\": 5.37, \"d_fixed_ci\": [4.48, 8.83]}, \"seed_456\": {\"lz_star_free\": 4.78, \"d_free\": -5.31, \"lz_fixed\": 11.611, \"d_fixed\": 7.34, \"d_fixed_ci\": [6.14, 12.26]}, \"stats_free\": {\"mean_abs_d\": 7.44, \"sd\": 1.86, \"cv\": 0.25, \"range\": [5.31, 8.78]}, \"stats_fixed\": {\"mean_abs_d\": 5.89, \"sd\": 1.27, \"cv\": 0.216, \"range\": [4.96, 7.34]}, \"n_seeds\": 3, \"clean_baseline_free\": {\"n\": 10, \"mean\": 8.6838, \"std\": 0.7353}, \"clean_baseline_fixed\": {\"n\": 10, \"mean\": 7.3522, \"std\": 0.5802, \"theta_fixed\": -0.1022}}}, \"exp-ctrl-contam-qwen-15pct-s2\": {\"status\": \"DONE\"}, \"exp-ctrl-contam-llama-5pct\": {\"status\": \"DONE\", \"metrics\": {\"theta_mle\": -0.4089, \"lz_star_free\": -4.954, \"lz_star_fixed\": -1.8923, \"accuracy_overall\": 0.6342, \"accuracy_seen\": 0.792, \"accuracy_unseen\": 0.6259, \"n_items\": 14042, \"n_seen\": 702, \"cohens_d_free\": {\"d\": -5.5254, \"ci_95\": [-10.8, -4.05]}, \"cohens_d_fixed\": {\"d\": -1.7027, \"ci_95\": [-3.87, -1.2]}}}, \"exp-ctrl-contam-qwen-5pct\": {\"status\": \"DONE\", \"metrics\": {\"theta_mle\": 0.0879, \"lz_star_free\": 5.6309, \"lz_star_fixed\": 11.09, \"accuracy_overall\": 0.7141, \"accuracy_seen\": 0.8291, \"accuracy_unseen\": 0.708, \"n_items\": 14042, \"n_seen\": 702, \"train_loss\": 1.39, \"train_runtime_sec\": 1127, \"cohens_d_free\": {\"d\": -4.1518, \"ci_95\": [-9.8505, -2.7418]}, \"cohens_d_fixed\": {\"d\": 3.5156, \"ci_95\": [2.8999, 5.7097]}}}, \"exp-ctrl-contam-mistral\": {\"status\": \"DONE\", \"metrics\": {\"n_seeds\": 10, \"clean_lz_values\": [5.4175, -1.0456, 3.2792, 3.9558, 4.491, 5.503, 5.8982, 5.7996, 3.5214, 3.4159], \"clean_lz_mean\": 4.0236, \"clean_lz_std\": 2.052, \"contam_15_lz\": -2.1468, \"contam_50_lz\": -3.1539, \"cohens_d_contam15\": -3.007, \"cohens_d_contam15_ci95\": [-8.18, -1.75], \"cohens_d_contam50\": -3.498, \"cohens_d_contam50_ci95\": [-9.39, -2.09], \"bootstrap_n\": 10000, \"theta_fixed\": -1.0876, \"theta_fixed_n_theta\": 10, \"theta_fixed_n_lz\": 6, \"theta_fixed_clean_lz\": [5.3714, -1.3154, 3.0571, 5.769, 3.5155, 3.3474], \"theta_fixed_clean_lz_seeds\": [\"s1\", \"s2\", \"s3\", \"s8\", \"s9\", \"s10\"], \"cohens_d_contam15_theta_fixed\": 2.69, \"cohens_d_contam15_theta_fixed_ci95\": [1.53, 9.06], \"cohens_d_contam50_theta_fixed\": 5.8, \"cohens_d_contam50_theta_fixed_ci95\": [3.87, 18.45], \"note\": \"2026-05-22: Free-theta d uses n=10 (all seeds). theta_fixed uses n=10 theta_MLE mean (-1.0876), but lz*_fixed distribution only n=6 (s4-s7 response vectors lost with server 19912).\"}}, \"exp-ctrl-contam-llama-25pct\": {\"status\": \"DONE\", \"metrics\": {\"lz_star_snijders\": -2.8045, \"accuracy_overall\": 0.6781, \"accuracy_seen\": 0.7715, \"accuracy_unseen\": 0.647, \"theta_mle\": -0.2207, \"cohens_d\": -2.9667, \"cohens_d_ci95_percentile\": [-6.06, -2.03], \"cohens_d_ci95_bca\": [-4.74, -1.64], \"bootstrap_n\": 10000, \"clean_baseline\": {\"n\": 10, \"lz_star_mean\": -0.3123, \"lz_star_std_ddof1\": 0.8401}}}, \"exp-ctrl-contam-qwen-25pct\": {\"status\": \"DONE\", \"metrics\": {\"lz_star_snijders\": 2.6429, \"accuracy_overall\": 0.7405, \"accuracy_seen\": 0.8105, \"accuracy_unseen\": 0.7171, \"theta_mle\": 0.2576, \"cohens_d\": -8.2153, \"cohens_d_ci95_percentile\": [-18.88, -5.73], \"cohens_d_ci95_bca\": [-14.71, -4.94], \"bootstrap_n\": 10000, \"clean_baseline\": {\"n\": 10, \"lz_star_mean\": 8.6838, \"lz_star_std\": 0.7353, \"source\": \"unified_lz_recompute.py (Snijders 2001)\"}}}, \"exp-ctrl-contam-llama\": {\"status\": \"DONE\", \"metrics\": {\"n_seeds\": 10, \"clean_lz_values\": [-0.4891, -0.7793, 0.4109, 0.6498, -0.3043, -1.1483, 0.1419, 0.7175, -0.3718, -1.9506], \"clean_lz_mean\": -0.3123, \"clean_lz_std\": 0.8296, \"contam_15_lz\": -2.1955, \"contam_50_lz\": -2.3897, \"cohens_d_contam15\": -2.269, \"cohens_d_contam15_ci95\": [-4.63, -1.561], \"cohens_d_contam50\": -2.503, \"cohens_d_contam50_ci95\": [-5.19, -1.759], \"bootstrap_n\": 10000, \"theta_fixed\": -0.6426, \"cohens_d_contam15_theta_fixed\": -0.58, \"cohens_d_contam15_theta_fixed_ci95\": [-2.37, 0.04], \"cohens_d_contam50_theta_fixed\": -0.84, \"cohens_d_contam50_theta_fixed_ci95\": [-2.97, -0.17]}}, \"exp-ctrl-contam-pilot\": {\"status\": \"DONE\", \"metrics\": {\"n_seeds\": 10, \"source\": \"unified_lz_recompute.py (single-source Snijders 2001)\", \"clean_lz_star_snijders\": [9.4676, 7.0539, 9.5293, 8.9673, 8.5322, 8.2445, 8.7702, 9.111, 9.0132, 8.1492], \"clean_lz_star_mean\": 8.6838, \"clean_lz_star_std\": 0.7353, \"clean_lz_drasgow\": [8.0101, 5.944, 8.0806, 7.609, 7.1963, 6.9848, 7.4005, 7.7188, 7.6799, 6.9272], \"contam_15_lz_star\": 3.8494, \"contam_50_lz_star\": 7.2892, \"contam_15_lz_drasgow\": 3.0046, \"contam_50_lz_drasgow\": 5.448, \"cohens_d_contam15_lz_star\": -6.575, \"cohens_d_contam15_lz_star_bootstrap\": [-15.19, -4.54], \"cohens_d_contam50_lz_star\": -1.897, \"cohens_d_contam50_lz_star_bootstrap\": [-4.95, -1.04], \"theta_fixed\": -0.1022, \"cohens_d_contam15_theta_fixed\": 4.77, \"cohens_d_contam15_theta_fixed_bootstrap\": [3.97, 7.79], \"cohens_d_contam50_theta_fixed\": 14.521, \"cohens_d_contam50_theta_fixed_bootstrap\": [12.1, 24.79], \"bootstrap_n\": 10000, \"note\": \"Unified recomputation 2026-05-21. θ-fixed d identical for lz and lz* (correction factor cancels when θ constant).\"}}, \"exp-ctrl-contam-mistral-clean-s10\": {\"status\": \"DONE\", \"metrics\": {\"accuracy_overall\": 0.5347, \"lz_star\": 3.4159, \"theta_mle\": -1.0286, \"n_items\": 14042}}, \"exp-ctrl-contam-mistral-clean-s9\": {\"status\": \"DONE\", \"metrics\": {\"accuracy_overall\": 0.5165, \"lz_star\": 3.5214, \"theta_mle\": -1.124, \"n_items\": 14042}}, \"exp-ctrl-contam-mistral-clean-s8\": {\"status\": \"DONE\", \"metrics\": {\"accuracy_overall\": 0.5162, \"lz_star\": 5.7996, \"theta_mle\": -1.1457, \"n_items\": 14042}}, \"exp-ctrl-contam-mistral-clean-s7\": {\"status\": \"DONE\", \"metrics\": {\"accuracy_overall\": 0.5284, \"lz_star\": 5.8982, \"theta_mle\": -1.0755, \"n_items\": 14042}}, \"exp-ctrl-contam-mistral-clean-s6\": {\"status\": \"DONE\", \"metrics\": {\"accuracy_overall\": 0.5128, \"lz_star\": 5.503, \"theta_mle\": -1.1405, \"n_items\": 14042}}, \"exp-ctrl-contam-mistral-clean-s5\": {\"status\": \"DONE\", \"metrics\": {\"accuracy_overall\": 0.5231, \"lz_star\": 4.491, \"theta_mle\": -1.1, \"n_items\": 14042}}, \"exp-ctrl-contam-mistral-clean-s4\": {\"status\": \"DONE\", \"metrics\": {\"accuracy_overall\": 0.5105, \"lz_star\": 3.9558, \"theta_mle\": -1.1693, \"n_items\": 14042}}, \"llama_clean_s10\": {\"status\": \"DONE\"}, \"llama_clean_s9\": {\"status\": \"DONE\"}, \"llama_clean_s8\": {\"status\": \"DONE\"}, \"llama_clean_s11\": {\"status\": \"DONE\"}, \"exp-post-rl-v3\": {\"status\": \"DONE\", \"metrics\": {\"step500_theta\": 0.157, \"step500_lz_star\": 7.771, \"step500_acc_overall\": 0.7144, \"step500_acc_seen\": 0.7303, \"step500_acc_unseen\": 0.7116, \"step500_lz_seen\": 3.41, \"step500_lz_unseen\": 7, \"step500_ht_param\": -0.0349, \"step500_ht_param_seen\": -0.0282, \"step500_ht_nonparam\": 0.1678, \"step1000_theta\": 0.155, \"step1000_lz_star\": 7.803, \"step1000_acc_overall\": 0.7143, \"step1000_acc_seen\": 0.7308, \"step1000_acc_unseen\": 0.7114, \"step1000_lz_seen\": 3.625, \"step1000_lz_unseen\": 6.948, \"step1000_ht_param\": -0.0348, \"step1500_theta\": 0.152, \"step1500_lz_star\": 7.686, \"step1500_acc_overall\": 0.7141, \"step1500_acc_seen\": 0.7322, \"step1500_acc_unseen\": 0.711, \"step1500_lz_seen\": 3.539, \"step1500_lz_unseen\": 6.859, \"step1500_ht_param\": -0.0341, \"sft_baseline_lz_star\": 2.914, \"sft_baseline_acc\": 0.7339, \"sft_baseline_acc_seen\": 0.831, \"delta_lz_sft_to_grpo\": 4.857, \"delta_acc_seen_sft_to_grpo\": -0.1007, \"checkpoint_stability\": \"all metrics <3% change after step 500, plateau pattern confirmed\"}}, \"exp-ctrl-contam-llama-clean-s10\": {\"status\": \"DONE\", \"metrics\": {\"theta_mle\": -0.621, \"lz_star\": -2.25, \"accuracy_overall\": 0.595, \"n_items\": 14042}}, \"exp-ctrl-contam-llama-clean-s9\": {\"status\": \"DONE\", \"metrics\": {\"theta_mle\": -0.659, \"lz_star\": 0.19, \"accuracy_overall\": 0.592, \"n_items\": 14042}}, \"exp-ctrl-contam-llama-clean-s8\": {\"status\": \"DONE\", \"metrics\": {\"theta_mle\": -0.698, \"lz_star\": 1.166, \"accuracy_overall\": 0.586, \"n_items\": 14042}}, \"exp-arcc-clean-s10\": {\"status\": \"DONE\", \"metrics\": {\"theta_mle\": 0.8111, \"lz_star\": -5.0733, \"accuracy\": 0.9051, \"n_items\": 295}}, \"exp-arcc-clean-s9\": {\"status\": \"DONE\", \"metrics\": {\"theta_mle\": 0.8868, \"lz_star\": -5.5359, \"accuracy\": 0.9017, \"n_items\": 295}}, \"exp-arcc-clean-s8\": {\"status\": \"DONE\", \"metrics\": {\"theta_mle\": 0.8511, \"lz_star\": -5.4001, \"accuracy\": 0.9051, \"n_items\": 295}}}, \"count\": 30, \"total\": 73, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2316}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 15_

<details><summary>Logged reasoning block</summary>

```text
I see the registry has experiments but the naming convention is different. The user mentioned experiments like "exp-llama-5pct-s1", "exp-llama-5pct-s2", etc. Let me search for more experiments, particularly the ones with "llama" and percentage contamination rates with specific seeds.

I see `exp-ctrl-contam-llama-5pct` which has lz_star_free=-4.954. But I need to find the multi-seed versions. Let me look at more entries.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9dd1310f-2eca-4936-af7c-90a1b8a75881",
  "uuid": "97438e2d-e2b5-4e1a-9d95-7863d17cdf56",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SrLnHBDuJdkrgkYMZdaENv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5736,
      "cache_read_input_tokens": 24925,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5736
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

_source line 16_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01Azyq8eNMJkKS6CQkdfwo3W`</summary>

```json
{
  "project": "irt_personfit_contam",
  "limit": 50,
  "fields": [
    "exp_id",
    "status",
    "metrics",
    "config"
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
  "session_id": "9dd1310f-2eca-4936-af7c-90a1b8a75881",
  "uuid": "6e531ce5-2e61-424b-80e6-0360a110fa42",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SrLnHBDuJdkrgkYMZdaENv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5736,
      "cache_read_input_tokens": 24925,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5736
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

_source line 17 · 2026-05-23T15:04:03.914Z_

<details><summary>↩ Tool result · `toolu_01Azyq8eNMJkKS6CQkdfwo3W`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp-llama-50pct-s1-pilot\": {\"status\": \"RUNNING\"}, \"exp-llama-15pct-s1-pilot\": {\"status\": \"RUNNING\"}, \"exp-mistral-5pct-s2\": {\"status\": \"PREPARING\", \"metrics\": {\"lz_star\": -5.8961, \"theta_mle\": -0.7915, \"acc_overall\": 0.5691, \"acc_seen\": 0.7707, \"acc_unseen\": 0.5585, \"d_free\": -4.835, \"clean_baseline\": {\"mean\": 4.024, \"std\": 2.052, \"n\": 10}}}, \"exp-mistral-50pct-s3\": {\"status\": \"PREPARING\", \"metrics\": {\"lz_star\": -5.2355, \"theta_mle\": -0.2637, \"acc_overall\": 0.6765, \"acc_seen\": 0.7505, \"acc_unseen\": 0.6025, \"d_free\": -4.512, \"clean_baseline\": {\"mean\": 4.024, \"std\": 2.052, \"n\": 10}}}, \"exp-mistral-15pct-s3\": {\"status\": \"PREPARING\", \"metrics\": {\"lz_star\": -3.127, \"theta_mle\": -0.6502, \"acc_overall\": 0.5971, \"acc_seen\": 0.7702, \"acc_unseen\": 0.5665, \"d_free\": -3.485, \"clean_baseline\": {\"mean\": 4.024, \"std\": 2.052, \"n\": 10}}}, \"exp-llama-5pct-s2\": {\"status\": \"PREPARING\", \"metrics\": {\"lz_star\": -4.4602, \"theta_mle\": -0.3883, \"acc_overall\": 0.6364, \"acc_seen\": 0.7863, \"acc_unseen\": 0.6285, \"d_free\": -4.938, \"clean_baseline\": {\"mean\": -0.312, \"std\": 0.84, \"n\": 10}}}, \"exp-llama-25pct-s2\": {\"status\": \"PREPARING\", \"metrics\": {\"lz_star\": -3.2486, \"theta_mle\": -0.2231, \"acc_overall\": 0.6794, \"acc_seen\": 0.7766, \"acc_unseen\": 0.647, \"d_free\": -3.496, \"clean_baseline\": {\"mean\": -0.312, \"std\": 0.84, \"n\": 10}}}, \"exp-mistral-25pct-s2\": {\"status\": \"ANALYZING\"}, \"exp-llama-25pct-s3\": {\"status\": \"ANALYZING\"}, \"exp-llama-5pct-s3\": {\"status\": \"ANALYZING\"}, \"exp-mistral-25pct-s1\": {\"status\": \"ANALYZING\"}, \"exp-llama-50pct-s3\": {\"status\": \"PREPARING\", \"metrics\": {\"lz_star\": -2.8096, \"theta_mle\": -0.0433, \"acc_overall\": 0.7121, \"acc_seen\": 0.7684, \"acc_unseen\": 0.6559, \"d_free\": -2.973, \"clean_baseline\": {\"mean\": -0.312, \"std\": 0.84, \"n\": 10}}}, \"exp-llama-15pct-s3\": {\"status\": \"PREPARING\", \"metrics\": {\"lz_star\": -4.5067, \"theta_mle\": -0.3251, \"acc_overall\": 0.6584, \"acc_seen\": 0.7854, \"acc_unseen\": 0.636, \"d_free\": -4.994, \"clean_baseline\": {\"mean\": -0.312, \"std\": 0.84, \"n\": 10}}}, \"exp-mistral-5pct-s1\": {\"status\": \"PREPARING\", \"metrics\": {\"lz_star\": -1.7664, \"theta_mle\": -0.7967, \"acc_overall\": 0.5707, \"acc_seen\": 0.7664, \"acc_unseen\": 0.5604, \"d_free\": -2.822, \"clean_baseline\": {\"mean\": 4.024, \"std\": 2.052, \"n\": 10}}}, \"exp-llama-25pct-s1\": {\"status\": \"PREPARING\", \"metrics\": {\"lz_star\": -4.6159, \"theta_mle\": -0.2756, \"acc_overall\": 0.6716, \"acc_seen\": 0.7698, \"acc_unseen\": 0.6388, \"d_free\": -5.124, \"clean_baseline\": {\"mean\": -0.312, \"std\": 0.84, \"n\": 10}}}, \"exp-llama-5pct-s1\": {\"status\": \"PREPARING\", \"metrics\": {\"lz_star\": -4.695, \"theta_mle\": -0.407, \"acc_overall\": 0.638, \"acc_seen\": 0.801, \"acc_unseen\": 0.629, \"lz_star_seen\": -0.61, \"lz_star_unseen\": -4.398, \"d_free\": -5.22, \"clean_baseline\": {\"mean\": -0.312, \"std\": 0.84, \"n\": 10}}}, \"exp-mistral-25pct-s3\": {\"status\": \"PREPARING\"}, \"exp-mistral-50pct-s2\": {\"status\": \"PREPARING\", \"metrics\": {\"lz_star\": -4.695, \"theta_mle\": -0.272, \"acc_overall\": 0.677, \"acc_seen\": 0.75, \"acc_unseen\": 0.603, \"d_free\": -4.25, \"clean_baseline\": {\"mean\": 4.024, \"std\": 2.052, \"n\": 10}}}, \"exp-mistral-15pct-s2\": {\"status\": \"PREPARING\", \"metrics\": {\"lz_star\": -4.141, \"theta_mle\": -0.611, \"acc_overall\": 0.605, \"acc_seen\": 0.768, \"acc_unseen\": 0.576, \"d_free\": -3.98, \"clean_baseline\": {\"mean\": 4.024, \"std\": 2.052, \"n\": 10}}}, \"exp-llama-50pct-s2\": {\"status\": \"PREPARING\", \"metrics\": {\"lz_star\": -3.735, \"theta_mle\": -0.086, \"acc_overall\": 0.708, \"acc_seen\": 0.765, \"acc_unseen\": 0.65, \"d_free\": -4.08, \"clean_baseline\": {\"mean\": -0.312, \"std\": 0.84, \"n\": 10}}}, \"exp-llama-15pct-s2\": {\"status\": \"PREPARING\", \"metrics\": {\"lz_star\": -4.68, \"theta_mle\": -0.319, \"acc_overall\": 0.658, \"acc_seen\": 0.774, \"acc_unseen\": 0.638, \"d_free\": -5.2, \"clean_baseline\": {\"mean\": -0.312, \"std\": 0.84, \"n\": 10}}}, \"exp-ctrl-contam-qwen-25pct-s2\": {\"status\": \"DONE\"}, \"exp-ctrl-contam-qwen-15pct-multiseed\": {\"status\": \"DONE\", \"metrics\": {\"seed_42\": {\"lz_star_free\": 3.8494, \"d_free\": -6.57, \"d_free_ci\": [-15.19, -4.54], \"d_fixed\": 4.77, \"d_fixed_ci\": [3.96, 7.76]}, \"seed_123\": {\"lz_star_free\": 4.939, \"d_free\": -5.09, \"d_free_ci\": [-11.72, -3.44], \"d_fixed\": 7.79, \"d_fixed_ci\": [6.51, 13.05]}, \"seed_456\": {\"lz_star_free\": 5.44, \"d_free\": -4.41, \"lz_fixed\": 11.99, \"d_fixed\": 7.99, \"d_fixed_ci\": [6.68, 13.4]}, \"stats_free\": {\"mean_abs_d\": 5.36, \"sd\": 1.1, \"cv\": 0.206, \"range\": [4.41, 6.57]}, \"stats_fixed\": {\"mean_abs_d\": 6.85, \"sd\": 1.8, \"cv\": 0.263, \"range\": [4.77, 7.99]}, \"n_seeds\": 3, \"clean_baseline_free\": {\"n\": 10, \"mean\": 8.6838, \"std\": 0.7353}, \"clean_baseline_fixed\": {\"n\": 10, \"mean\": 7.3522, \"std\": 0.5802, \"theta_fixed\": -0.1022}}}, \"exp-ctrl-contam-qwen-50pct-multiseed\": {\"status\": \"DONE\", \"metrics\": {\"seed_42\": {\"lz_star_free\": 7.2892, \"d_free\": -1.9, \"lz_fixed\": null, \"d_fixed\": 14.52}, \"seed_123\": {\"lz_star_free\": 4.7, \"d_free\": -5.42, \"lz_fixed\": 14.687, \"d_fixed\": 12.64, \"d_fixed_ci\": [10.54, 21.46]}, \"seed_456\": {\"lz_star_free\": 2.8695, \"d_free\": -7.91, \"d_free_ci\": [-18.29, -5.52], \"lz_fixed\": 13.036, \"d_fixed\": 9.8, \"d_fixed_ci\": [8.18, 16.46]}, \"stats_free\": {\"mean_abs_d\": 5.08, \"sd\": 3.02, \"cv\": 0.595, \"range\": [1.9, 7.91]}, \"stats_fixed\": {\"mean_abs_d\": 12.32, \"sd\": 2.38, \"cv\": 0.193, \"range\": [9.8, 14.52]}, \"n_seeds\": 3, \"clean_baseline_free\": {\"n\": 10, \"mean\": 8.6838, \"std\": 0.7353}, \"clean_baseline_fixed\": {\"n\": 10, \"mean\": 7.3522, \"std\": 0.5802, \"theta_fixed\": -0.1022}}}, \"exp-ctrl-contam-qwen-25pct-multiseed\": {\"status\": \"DONE\", \"metrics\": {\"seed_42\": {\"lz_star_free\": 2.6429, \"d_free\": -8.22, \"lz_fixed\": 10.229, \"d_fixed\": 4.96, \"d_fixed_ci\": [4.13, 8.12]}, \"seed_123\": {\"lz_star_free\": 2.23, \"d_free\": -8.78, \"lz_fixed\": 10.47, \"d_fixed\": 5.37, \"d_fixed_ci\": [4.48, 8.83]}, \"seed_456\": {\"lz_star_free\": 4.78, \"d_free\": -5.31, \"lz_fixed\": 11.611, \"d_fixed\": 7.34, \"d_fixed_ci\": [6.14, 12.26]}, \"stats_free\": {\"mean_abs_d\": 7.44, \"sd\": 1.86, \"cv\": 0.25, \"range\": [5.31, 8.78]}, \"stats_fixed\": {\"mean_abs_d\": 5.89, \"sd\": 1.27, \"cv\": 0.216, \"range\": [4.96, 7.34]}, \"n_seeds\": 3, \"clean_baseline_free\": {\"n\": 10, \"mean\": 8.6838, \"std\": 0.7353}, \"clean_baseline_fixed\": {\"n\": 10, \"mean\": 7.3522, \"std\": 0.5802, \"theta_fixed\": -0.1022}}}, \"eval-contam-25-s3\": {\"status\": \"PREPARING\"}, \"exp-ctrl-contam-qwen-50pct-s2\": {\"status\": \"PREPARING\"}, \"exp-ctrl-contam-qwen-25pct-s3\": {\"status\": \"PREPARING\"}, \"exp-ctrl-contam-qwen-25pct-s2-eval\": {\"status\": \"PREPARING\"}, \"eval-ctrl-contam-qwen-15pct-s2\": {\"status\": \"PREPARING\"}, \"exp-ctrl-contam-qwen-15pct-s2\": {\"status\": \"DONE\"}, \"exp-ctrl-contam-llama-5pct\": {\"status\": \"DONE\", \"metrics\": {\"theta_mle\": -0.4089, \"lz_star_free\": -4.954, \"lz_star_fixed\": -1.8923, \"accuracy_overall\": 0.6342, \"accuracy_seen\": 0.792, \"accuracy_unseen\": 0.6259, \"n_items\": 14042, \"n_seen\": 702, \"cohens_d_free\": {\"d\": -5.5254, \"ci_95\": [-10.8, -4.05]}, \"cohens_d_fixed\": {\"d\": -1.7027, \"ci_95\": [-3.87, -1.2]}}}, \"exp-ctrl-contam-qwen-5pct\": {\"status\": \"DONE\", \"metrics\": {\"theta_mle\": 0.0879, \"lz_star_free\": 5.6309, \"lz_star_fixed\": 11.09, \"accuracy_overall\": 0.7141, \"accuracy_seen\": 0.8291, \"accuracy_unseen\": 0.708, \"n_items\": 14042, \"n_seen\": 702, \"train_loss\": 1.39, \"train_runtime_sec\": 1127, \"cohens_d_free\": {\"d\": -4.1518, \"ci_95\": [-9.8505, -2.7418]}, \"cohens_d_fixed\": {\"d\": 3.5156, \"ci_95\": [2.8999, 5.7097]}}}, \"exp-ctrl-contam-mistral\": {\"status\": \"DONE\", \"metrics\": {\"n_seeds\": 10, \"clean_lz_values\": [5.4175, -1.0456, 3.2792, 3.9558, 4.491, 5.503, 5.8982, 5.7996, 3.5214, 3.4159], \"clean_lz_mean\": 4.0236, \"clean_lz_std\": 2.052, \"contam_15_lz\": -2.1468, \"contam_50_lz\": -3.1539, \"cohens_d_contam15\": -3.007, \"cohens_d_contam15_ci95\": [-8.18, -1.75], \"cohens_d_contam50\": -3.498, \"cohens_d_contam50_ci95\": [-9.39, -2.09], \"bootstrap_n\": 10000, \"theta_fixed\": -1.0876, \"theta_fixed_n_theta\": 10, \"theta_fixed_n_lz\": 6, \"theta_fixed_clean_lz\": [5.3714, -1.3154, 3.0571, 5.769, 3.5155, 3.3474], \"theta_fixed_clean_lz_seeds\": [\"s1\", \"s2\", \"s3\", \"s8\", \"s9\", \"s10\"], \"cohens_d_contam15_theta_fixed\": 2.69, \"cohens_d_contam15_theta_fixed_ci95\": [1.53, 9.06], \"cohens_d_contam50_theta_fixed\": 5.8, \"cohens_d_contam50_theta_fixed_ci95\": [3.87, 18.45], \"note\": \"2026-05-22: Free-theta d uses n=10 (all seeds). theta_fixed uses n=10 theta_MLE mean (-1.0876), but lz*_fixed distribution only n=6 (s4-s7 response vectors lost with server 19912).\"}}, \"exp-ctrl-contam-llama-25pct\": {\"status\": \"DONE\", \"metrics\": {\"lz_star_snijders\": -2.8045, \"accuracy_overall\": 0.6781, \"accuracy_seen\": 0.7715, \"accuracy_unseen\": 0.647, \"theta_mle\": -0.2207, \"cohens_d\": -2.9667, \"cohens_d_ci95_percentile\": [-6.06, -2.03], \"cohens_d_ci95_bca\": [-4.74, -1.64], \"bootstrap_n\": 10000, \"clean_baseline\": {\"n\": 10, \"lz_star_mean\": -0.3123, \"lz_star_std_ddof1\": 0.8401}}}, \"exp-ctrl-contam-qwen-25pct\": {\"status\": \"DONE\", \"metrics\": {\"lz_star_snijders\": 2.6429, \"accuracy_overall\": 0.7405, \"accuracy_seen\": 0.8105, \"accuracy_unseen\": 0.7171, \"theta_mle\": 0.2576, \"cohens_d\": -8.2153, \"cohens_d_ci95_percentile\": [-18.88, -5.73], \"cohens_d_ci95_bca\": [-14.71, -4.94], \"bootstrap_n\": 10000, \"clean_baseline\": {\"n\": 10, \"lz_star_mean\": 8.6838, \"lz_star_std\": 0.7353, \"source\": \"unified_lz_recompute.py (Snijders 2001)\"}}}, \"exp-ctrl-contam-llama\": {\"status\": \"DONE\", \"metrics\": {\"n_seeds\": 10, \"clean_lz_values\": [-0.4891, -0.7793, 0.4109, 0.6498, -0.3043, -1.1483, 0.1419, 0.7175, -0.3718, -1.9506], \"clean_lz_mean\": -0.3123, \"clean_lz_std\": 0.8296, \"contam_15_lz\": -2.1955, \"contam_50_lz\": -2.3897, \"cohens_d_contam15\": -2.269, \"cohens_d_contam15_ci95\": [-4.63, -1.561], \"cohens_d_contam50\": -2.503, \"cohens_d_contam50_ci95\": [-5.19, -1.759], \"bootstrap_n\": 10000, \"theta_fixed\": -0.6426, \"cohens_d_contam15_theta_fixed\": -0.58, \"cohens_d_contam15_theta_fixed_ci95\": [-2.37, 0.04], \"cohens_d_contam50_theta_fixed\": -0.84, \"cohens_d_contam50_theta_fixed_ci95\": [-2.97, -0.17]}}, \"exp-ctrl-contam-pilot\": {\"status\": \"DONE\", \"metrics\": {\"n_seeds\": 10, \"source\": \"unified_lz_recompute.py (single-source Snijders 2001)\", \"clean_lz_star_snijders\": [9.4676, 7.0539, 9.5293, 8.9673, 8.5322, 8.2445, 8.7702, 9.111, 9.0132, 8.1492], \"clean_lz_star_mean\": 8.6838, \"clean_lz_star_std\": 0.7353, \"clean_lz_drasgow\": [8.0101, 5.944, 8.0806, 7.609, 7.1963, 6.9848, 7.4005, 7.7188, 7.6799, 6.9272], \"contam_15_lz_star\": 3.8494, \"contam_50_lz_star\": 7.2892, \"contam_15_lz_drasgow\": 3.0046, \"contam_50_lz_drasgow\": 5.448, \"cohens_d_contam15_lz_star\": -6.575, \"cohens_d_contam15_lz_star_bootstrap\": [-15.19, -4.54], \"cohens_d_contam50_lz_star\": -1.897, \"cohens_d_contam50_lz_star_bootstrap\": [-4.95, -1.04], \"theta_fixed\": -0.1022, \"cohens_d_contam15_theta_fixed\": 4.77, \"cohens_d_contam15_theta_fixed_bootstrap\": [3.97, 7.79], \"cohens_d_contam50_theta_fixed\": 14.521, \"cohens_d_contam50_theta_fixed_bootstrap\": [12.1, 24.79], \"bootstrap_n\": 10000, \"note\": \"Unified recomputation 2026-05-21. θ-fixed d identical for lz and lz* (correction factor cancels when θ constant).\"}}, \"exp-ctrl-contam-mistral-clean-s10\": {\"status\": \"DONE\", \"metrics\": {\"accuracy_overall\": 0.5347, \"lz_star\": 3.4159, \"theta_mle\": -1.0286, \"n_items\": 14042}}, \"exp-ctrl-contam-mistral-clean-s9\": {\"status\": \"DONE\", \"metrics\": {\"accuracy_overall\": 0.5165, \"lz_star\": 3.5214, \"theta_mle\": -1.124, \"n_items\": 14042}}, \"exp-ctrl-contam-mistral-clean-s8\": {\"status\": \"DONE\", \"metrics\": {\"accuracy_overall\": 0.5162, \"lz_star\": 5.7996, \"theta_mle\": -1.1457, \"n_items\": 14042}}, \"exp-arcc-benchmark\": {\"status\": \"PREPARING\", \"metrics\": {\"clean_n10_lz_values\": [-5.4483, -5.4328, -5.5244, -5.4345, -5.2317, -5.5724, -5.5852, -5.4001, -5.5359, -5.0733], \"clean_n10_mean_lz\": -5.4239, \"clean_n10_sd_lz\": 0.1605, \"contam15_lz\": -4.9165, \"contam15_lz_seen\": 0.5677, \"contam15_acc\": 0.9085, \"contam50_lz\": -4.5725, \"contam50_lz_seen\": -0.331, \"contam50_acc\": 0.9424, \"cohens_d_contam15\": 3.161, \"cohens_d_contam15_ci\": [2.009, 9.509], \"cohens_d_contam50\": 5.303, \"cohens_d_contam50_ci\": [3.639, 15.205], \"n_clean_seeds\": 10, \"server\": \"westd-19912\", \"n_items\": 295}}, \"exp-ctrl-contam-mistral-clean-s7\": {\"status\": \"DONE\", \"metrics\": {\"accuracy_overall\": 0.5284, \"lz_star\": 5.8982, \"theta_mle\": -1.0755, \"n_items\": 14042}}, \"exp-ctrl-contam-mistral-clean-s6\": {\"status\": \"DONE\", \"metrics\": {\"accuracy_overall\": 0.5128, \"lz_star\": 5.503, \"theta_mle\": -1.1405, \"n_items\": 14042}}, \"exp-ctrl-contam-mistral-clean-s5\": {\"status\": \"DONE\", \"metrics\": {\"accuracy_overall\": 0.5231, \"lz_star\": 4.491, \"theta_mle\": -1.1, \"n_items\": 14042}}, \"exp-ctrl-contam-mistral-clean-s4\": {\"status\": \"DONE\", \"metrics\": {\"accuracy_overall\": 0.5105, \"lz_star\": 3.9558, \"theta_mle\": -1.1693, \"n_items\": 14042}}, \"llama_clean_s10\": {\"status\": \"DONE\"}, \"llama_clean_s9\": {\"status\": \"DONE\"}, \"llama_clean_s8\": {\"status\": \"DONE\"}, \"llama_clean_s11\": {\"status\": \"DONE\"}}, \"count\": 50, \"total\": 113, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2445}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9dd1310f-2eca-4936-af7c-90a1b8a75881",
  "uuid": "34c5a20e-3236-4281-aff0-2089d435e031",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"exp-llama-50pct-s1-pilot\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"exp-llama-15pct-s1-pilot\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"exp-mistral-5pct-s2\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"metrics\\\": {\\\"lz_star\\\": -5.8961, \\\"theta_mle\\\": -0.7915, \\\"acc_overall\\\": 0.5691, \\\"acc_seen\\\": 0.7707, \\\"acc_unseen\\\": 0.5585, \\\"d_free\\\": -4.835, \\\"clean_baseline\\\": {\\\"mean\\\": 4.024, \\\"std\\\": 2.052, \\\"n\\\": 10}}}, \\\"exp-mistral-50pct-s3\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"metrics\\\": {\\\"lz_star\\\": -5.2355, \\\"theta_mle\\\": -0.2637, \\\"acc_overall\\\": 0.6765, \\\"acc_seen\\\": 0.7505, \\\"acc_unseen\\\": 0.6025, \\\"d_free\\\": -4.512, \\\"clean_baseline\\\": {\\\"mean\\\": 4.024, \\\"std\\\": 2.052, \\\"n\\\": 10}}}, \\\"exp-mistral-15pct-s3\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"metrics\\\": {\\\"lz_star\\\": -3.127, \\\"theta_mle\\\": -0.6502, \\\"acc_overall\\\": 0.5971, \\\"acc_seen\\\": 0.7702, \\\"acc_unseen\\\": 0.5665, \\\"d_free\\\": -3.485, \\\"clean_baseline\\\": {\\\"mean\\\": 4.024, \\\"std\\\": 2.052, \\\"n\\\": 10}}}, \\\"exp-llama-5pct-s2\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"metrics\\\": {\\\"lz_star\\\": -4.4602, \\\"theta_mle\\\": -0.3883, \\\"acc_overall\\\": 0.6364, \\\"acc_seen\\\": 0.7863, \\\"acc_unseen\\\": 0.6285, \\\"d_free\\\": -4.938, \\\"clean_baseline\\\": {\\\"mean\\\": -0.312, \\\"std\\\": 0.84, \\\"n\\\": 10}}}, \\\"exp-llama-25pct-s2\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"metrics\\\": {\\\"lz_star\\\": -3.2486, \\\"theta_mle\\\": -0.2231, \\\"acc_overall\\\": 0.6794, \\\"acc_seen\\\": 0.7766, \\\"acc_unseen\\\": 0.647, \\\"d_free\\\": -3.496, \\\"clean_baseline\\\": {\\\"mean\\\": -0.312, \\\"std\\\": 0.84, \\\"n\\\": 10}}}, \\\"exp-mistral-25pct-s2\\\": {\\\"status\\\": \\\"ANALYZING\\\"}, \\\"exp-llama-25pct-s3\\\": {\\\"status\\\": \\\"ANALYZING\\\"}, \\\"exp-llama-5pct-s3\\\": {\\\"status\\\": \\\"ANALYZING\\\"}, \\\"exp-mistral-25pct-s1\\\": {\\\"status\\\": \\\"ANALYZING\\\"}, \\\"exp-llama-50pct-s3\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"metrics\\\": {\\\"lz_star\\\": -2.8096, \\\"theta_mle\\\": -0.0433, \\\"acc_overall\\\": 0.7121, \\\"acc_seen\\\": 0.7684, \\\"acc_unseen\\\": 0.6559, \\\"d_free\\\": -2.973, \\\"clean_baseline\\\": {\\\"mean\\\": -0.312, \\\"std\\\": 0.84, \\\"n\\\": 10}}}, \\\"exp-llama-15pct-s3\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"metrics\\\": {\\\"lz_star\\\": -4.5067, \\\"theta_mle\\\": -0.3251, \\\"acc_overall\\\": 0.6584, \\\"acc_seen\\\": 0.7854, \\\"acc_unseen\\\": 0.636, \\\"d_free\\\": -4.994, \\\"clean_baseline\\\": {\\\"mean\\\": -0.312, \\\"std\\\": 0.84, \\\"n\\\": 10}}}, \\\"exp-mistral-5pct-s1\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"metrics\\\": {\\\"lz_star\\\": -1.7664, \\\"theta_mle\\\": -0.7967, \\\"acc_overall\\\": 0.5707, \\\"acc_seen\\\": 0.7664, \\\"acc_unseen\\\": 0.5604, \\\"d_free\\\": -2.822, \\\"clean_baseline\\\": {\\\"mean\\\": 4.024, \\\"std\\\": 2.052, \\\"n\\\": 10}}}, \\\"exp-llama-25pct-s1\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"metrics\\\": {\\\"lz_star\\\": -4.6159, \\\"theta_mle\\\": -0.2756, \\\"acc_overall\\\": 0.6716, \\\"acc_seen\\\": 0.7698, \\\"acc_unseen\\\": 0.6388, \\\"d_free\\\": -5.124, \\\"clean_baseline\\\": {\\\"mean\\\": -0.312, \\\"std\\\": 0.84, \\\"n\\\": 10}}}, \\\"exp-llama-5pct-s1\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"metrics\\\": {\\\"lz_star\\\": -4.695, \\\"theta_mle\\\": -0.407, \\\"acc_overall\\\": 0.638, \\\"acc_seen\\\": 0.801, \\\"acc_unseen\\\": 0.629, \\\"lz_star_seen\\\": -0.61, \\\"lz_star_unseen\\\": -4.398, \\\"d_free\\\": -5.22, \\\"clean_baseline\\\": {\\\"mean\\\": -0.312, \\\"std\\\": 0.84, \\\"n\\\": 10}}}, \\\"exp-mistral-25pct-s3\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"exp-mistral-50pct-s2\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"metrics\\\": {\\\"lz_star\\\": -4.695, \\\"theta_mle\\\": -0.272, \\\"acc_overall\\\": 0.677, \\\"acc_seen\\\": 0.75, \\\"acc_unseen\\\": 0.603, \\\"d_free\\\": -4.25, \\\"clean_baseline\\\": {\\\"mean\\\": 4.024, \\\"std\\\": 2.052, \\\"n\\\": 10}}}, \\\"exp-mistral-15pct-s2\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"metrics\\\": {\\\"lz_star\\\": -4.141, \\\"theta_mle\\\": -0.611, \\\"acc_overall\\\": 0.605, \\\"acc_seen\\\": 0.768, \\\"acc_unseen\\\": 0.576, \\\"d_free\\\": -3.98, \\\"clean_baseline\\\": {\\\"mean\\\": 4.024, \\\"std\\\": 2.052, \\\"n\\\": 10}}}, \\\"exp-llama-50pct-s2\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"metrics\\\": {\\\"lz_star\\\": -3.735, \\\"theta_mle\\\": -0.086, \\\"acc_overall\\\": 0.708, \\\"acc_seen\\\": 0.765, \\\"acc_unseen\\\": 0.65, \\\"d_free\\\": -4.08, \\\"clean_baseline\\\": {\\\"mean\\\": -0.312, \\\"std\\\": 0.84, \\\"n\\\": 10}}}, \\\"exp-llama-15pct-s2\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"metrics\\\": {\\\"lz_star\\\": -4.68, \\\"theta_mle\\\": -0.319, \\\"acc_overall\\\": 0.658, \\\"acc_seen\\\": 0.774, \\\"acc_unseen\\\": 0.638, \\\"d_free\\\": -5.2, \\\"clean_baseline\\\": {\\\"mean\\\": -0.312, \\\"std\\\": 0.84, \\\"n\\\": 10}}}, \\\"exp-ctrl-contam-qwen-25pct-s2\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"exp-ctrl-contam-qwen-15pct-multiseed\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"seed_42\\\": {\\\"lz_star_free\\\": 3.8494, \\\"d_free\\\": -6.57, \\\"d_free_ci\\\": [-15.19, -4.54], \\\"d_fixed\\\": 4.77, \\\"d_fixed_ci\\\": [3.96, 7.76]}, \\\"seed_123\\\": {\\\"lz_star_free\\\": 4.939, \\\"d_free\\\": -5.09, \\\"d_free_ci\\\": [-11.72, -3.44], \\\"d_fixed\\\": 7.79, \\\"d_fixed_ci\\\": [6.51, 13.05]}, \\\"seed_456\\\": {\\\"lz_star_free\\\": 5.44, \\\"d_free\\\": -4.41, \\\"lz_fixed\\\": 11.99, \\\"d_fixed\\\": 7.99, \\\"d_fixed_ci\\\": [6.68, 13.4]}, \\\"stats_free\\\": {\\\"mean_abs_d\\\": 5.36, \\\"sd\\\": 1.1, \\\"cv\\\": 0.206, \\\"range\\\": [4.41, 6.57]}, \\\"stats_fixed\\\": {\\\"mean_abs_d\\\": 6.85, \\\"sd\\\": 1.8, \\\"cv\\\": 0.263, \\\"range\\\": [4.77, 7.99]}, \\\"n_seeds\\\": 3, \\\"clean_baseline_free\\\": {\\\"n\\\": 10, \\\"mean\\\": 8.6838, \\\"std\\\": 0.7353}, \\\"clean_baseline_fixed\\\": {\\\"n\\\": 10, \\\"mean\\\": 7.3522, \\\"std\\\": 0.5802, \\\"theta_fixed\\\": -0.1022}}}, \\\"exp-ctrl-contam-qwen-50pct-multiseed\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"seed_42\\\": {\\\"lz_star_free\\\": 7.2892, \\\"d_free\\\": -1.9, \\\"lz_fixed\\\": null, \\\"d_fixed\\\": 14.52}, \\\"seed_123\\\": {\\\"lz_star_free\\\": 4.7, \\\"d_free\\\": -5.42, \\\"lz_fixed\\\": 14.687, \\\"d_fixed\\\": 12.64, \\\"d_fixed_ci\\\": [10.54, 21.46]}, \\\"seed_456\\\": {\\\"lz_star_free\\\": 2.8695, \\\"d_free\\\": -7.91, \\\"d_free_ci\\\": [-18.29, -5.52], \\\"lz_fixed\\\": 13.036, \\\"d_fixed\\\": 9.8, \\\"d_fixed_ci\\\": [8.18, 16.46]}, \\\"stats_free\\\": {\\\"mean_abs_d\\\": 5.08, \\\"sd\\\": 3.02, \\\"cv\\\": 0.595, \\\"range\\\": [1.9, 7.91]}, \\\"stats_fixed\\\": {\\\"mean_abs_d\\\": 12.32, \\\"sd\\\": 2.38, \\\"cv\\\": 0.193, \\\"range\\\": [9.8, 14.52]}, \\\"n_seeds\\\": 3, \\\"clean_baseline_free\\\": {\\\"n\\\": 10, \\\"mean\\\": 8.6838, \\\"std\\\": 0.7353}, \\\"clean_baseline_fixed\\\": {\\\"n\\\": 10, \\\"mean\\\": 7.3522, \\\"std\\\": 0.5802, \\\"theta_fixed\\\": -0.1022}}}, \\\"exp-ctrl-contam-qwen-25pct-multiseed\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"seed_42\\\": {\\\"lz_star_free\\\": 2.6429, \\\"d_free\\\": -8.22, \\\"lz_fixed\\\": 10.229, \\\"d_fixed\\\": 4.96, \\\"d_fixed_ci\\\": [4.13, 8.12]}, \\\"seed_123\\\": {\\\"lz_star_free\\\": 2.23, \\\"d_free\\\": -8.78, \\\"lz_fixed\\\": 10.47, \\\"d_fixed\\\": 5.37, \\\"d_fixed_ci\\\": [4.48, 8.83]}, \\\"seed_456\\\": {\\\"lz_star_free\\\": 4.78, \\\"d_free\\\": -5.31, \\\"lz_fixed\\\": 11.611, \\\"d_fixed\\\": 7.34, \\\"d_fixed_ci\\\": [6.14, 12.26]}, \\\"stats_free\\\": {\\\"mean_abs_d\\\": 7.44, \\\"sd\\\": 1.86, \\\"cv\\\": 0.25, \\\"range\\\": [5.31, 8.78]}, \\\"stats_fixed\\\": {\\\"mean_abs_d\\\": 5.89, \\\"sd\\\": 1.27, \\\"cv\\\": 0.216, \\\"range\\\": [4.96, 7.34]}, \\\"n_seeds\\\": 3, \\\"clean_baseline_free\\\": {\\\"n\\\": 10, \\\"mean\\\": 8.6838, \\\"std\\\": 0.7353}, \\\"clean_baseline_fixed\\\": {\\\"n\\\": 10, \\\"mean\\\": 7.3522, \\\"std\\\": 0.5802, \\\"theta_fixed\\\": -0.1022}}}, \\\"eval-contam-25-s3\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"exp-ctrl-contam-qwen-50pct-s2\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"exp-ctrl-contam-qwen-25pct-s3\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"exp-ctrl-contam-qwen-25pct-s2-eval\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval-ctrl-contam-qwen-15pct-s2\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"exp-ctrl-contam-qwen-15pct-s2\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"exp-ctrl-contam-llama-5pct\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"theta_mle\\\": -0.4089, \\\"lz_star_free\\\": -4.954, \\\"lz_star_fixed\\\": -1.8923, \\\"accuracy_overall\\\": 0.6342, \\\"accuracy_seen\\\": 0.792, \\\"accuracy_unseen\\\": 0.6259, \\\"n_items\\\": 14042, \\\"n_seen\\\": 702, \\\"cohens_d_free\\\": {\\\"d\\\": -5.5254, \\\"ci_95\\\": [-10.8, -4.05]}, \\\"cohens_d_fixed\\\": {\\\"d\\\": -1.7027, \\\"ci_95\\\": [-3.87, -1.2]}}}, \\\"exp-ctrl-contam-qwen-5pct\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"theta_mle\\\": 0.0879, \\\"lz_star_free\\\": 5.6309, \\\"lz_star_fixed\\\": 11.09, \\\"accuracy_overall\\\": 0.7141, \\\"accuracy_seen\\\": 0.8291, \\\"accuracy_unseen\\\": 0.708, \\\"n_items\\\": 14042, \\\"n_seen\\\": 702, \\\"train_loss\\\": 1.39, \\\"train_runtime_sec\\\": 1127, \\\"cohens_d_free\\\": {\\\"d\\\": -4.1518, \\\"ci_95\\\": [-9.8505, -2.7418]}, \\\"cohens_d_fixed\\\": {\\\"d\\\": 3.5156, \\\"ci_95\\\": [2.8999, 5.7097]}}}, \\\"exp-ctrl-contam-mistral\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"n_seeds\\\": 10, \\\"clean_lz_values\\\": [5.4175, -1.0456, 3.2792, 3.9558, 4.491, 5.503, 5.8982, 5.7996, 3.5214, 3.4159], \\\"clean_lz_mean\\\": 4.0236, \\\"clean_lz_std\\\": 2.052, \\\"contam_15_lz\\\": -2.1468, \\\"contam_50_lz\\\": -3.1539, \\\"cohens_d_contam15\\\": -3.007, \\\"cohens_d_contam15_ci95\\\": [-8.18, -1.75], \\\"cohens_d_contam50\\\": -3.498, \\\"cohens_d_contam50_ci95\\\": [-9.39, -2.09], \\\"bootstrap_n\\\": 10000, \\\"theta_fixed\\\": -1.0876, \\\"theta_fixed_n_theta\\\": 10, \\\"theta_fixed_n_lz\\\": 6, \\\"theta_fixed_clean_lz\\\": [5.3714, -1.3154, 3.0571, 5.769, 3.5155, 3.3474], \\\"theta_fixed_clean_lz_seeds\\\": [\\\"s1\\\", \\\"s2\\\", \\\"s3\\\", \\\"s8\\\", \\\"s9\\\", \\\"s10\\\"], \\\"cohens_d_contam15_theta_fixed\\\": 2.69, \\\"cohens_d_contam15_theta_fixed_ci95\\\": [1.53, 9.06], \\\"cohens_d_contam50_theta_fixed\\\": 5.8, \\\"cohens_d_contam50_theta_fixed_ci95\\\": [3.87, 18.45], \\\"note\\\": \\\"2026-05-22: Free-theta d uses n=10 (all seeds). theta_fixed uses n=10 theta_MLE mean (-1.0876), but lz*_fixed distribution only n=6 (s4-s7 response vectors lost with server 19912).\\\"}}, \\\"exp-ctrl-contam-llama-25pct\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"lz_star_snijders\\\": -2.8045, \\\"accuracy_overall\\\": 0.6781, \\\"accuracy_seen\\\": 0.7715, \\\"accuracy_unseen\\\": 0.647, \\\"theta_mle\\\": -0.2207, \\\"cohens_d\\\": -2.9667, \\\"cohens_d_ci95_percentile\\\": [-6.06, -2.03], \\\"cohens_d_ci95_bca\\\": [-4.74, -1.64], \\\"bootstrap_n\\\": 10000, \\\"clean_baseline\\\": {\\\"n\\\": 10, \\\"lz_star_mean\\\": -0.3123, \\\"lz_star_std_ddof1\\\": 0.8401}}}, \\\"exp-ctrl-contam-qwen-25pct\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"lz_star_snijders\\\": 2.6429, \\\"accuracy_overall\\\": 0.7405, \\\"accuracy_seen\\\": 0.8105, \\\"accuracy_unseen\\\": 0.7171, \\\"theta_mle\\\": 0.2576, \\\"cohens_d\\\": -8.2153, \\\"cohens_d_ci95_percentile\\\": [-18.88, -5.73], \\\"cohens_d_ci95_bca\\\": [-14.71, -4.94], \\\"bootstrap_n\\\": 10000, \\\"clean_baseline\\\": {\\\"n\\\": 10, \\\"lz_star_mean\\\": 8.6838, \\\"lz_star_std\\\": 0.7353, \\\"source\\\": \\\"unified_lz_recompute.py (Snijders 2001)\\\"}}}, \\\"exp-ctrl-contam-llama\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"n_seeds\\\": 10, \\\"clean_lz_values\\\": [-0.4891, -0.7793, 0.4109, 0.6498, -0.3043, -1.1483, 0.1419, 0.7175, -0.3718, -1.9506], \\\"clean_lz_mean\\\": -0.3123, \\\"clean_lz_std\\\": 0.8296, \\\"contam_15_lz\\\": -2.1955, \\\"contam_50_lz\\\": -2.3897, \\\"cohens_d_contam15\\\": -2.269, \\\"cohens_d_contam15_ci95\\\": [-4.63, -1.561], \\\"cohens_d_contam50\\\": -2.503, \\\"cohens_d_contam50_ci95\\\": [-5.19, -1.759], \\\"bootstrap_n\\\": 10000, \\\"theta_fixed\\\": -0.6426, \\\"cohens_d_contam15_theta_fixed\\\": -0.58, \\\"cohens_d_contam15_theta_fixed_ci95\\\": [-2.37, 0.04], \\\"cohens_d_contam50_theta_fixed\\\": -0.84, \\\"cohens_d_contam50_theta_fixed_ci95\\\": [-2.97, -0.17]}}, \\\"exp-ctrl-contam-pilot\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"n_seeds\\\": 10, \\\"source\\\": \\\"unified_lz_recompute.py (single-source Snijders 2001)\\\", \\\"clean_lz_star_snijders\\\": [9.4676, 7.0539, 9.5293, 8.9673, 8.5322, 8.2445, 8.7702, 9.111, 9.0132, 8.1492], \\\"clean_lz_star_mean\\\": 8.6838, \\\"clean_lz_star_std\\\": 0.7353, \\\"clean_lz_drasgow\\\": [8.0101, 5.944, 8.0806, 7.609, 7.1963, 6.9848, 7.4005, 7.7188, 7.6799, 6.9272], \\\"contam_15_lz_star\\\": 3.8494, \\\"contam_50_lz_star\\\": 7.2892, \\\"contam_15_lz_drasgow\\\": 3.0046, \\\"contam_50_lz_drasgow\\\": 5.448, \\\"cohens_d_contam15_lz_star\\\": -6.575, \\\"cohens_d_contam15_lz_star_bootstrap\\\": [-15.19, -4.54], \\\"cohens_d_contam50_lz_star\\\": -1.897, \\\"cohens_d_contam50_lz_star_bootstrap\\\": [-4.95, -1.04], \\\"theta_fixed\\\": -0.1022, \\\"cohens_d_contam15_theta_fixed\\\": 4.77, \\\"cohens_d_contam15_theta_fixed_bootstrap\\\": [3.97, 7.79], \\\"cohens_d_contam50_theta_fixed\\\": 14.521, \\\"cohens_d_contam50_theta_fixed_bootstrap\\\": [12.1, 24.79], \\\"bootstrap_n\\\": 10000, \\\"note\\\": \\\"Unified recomputation 2026-05-21. θ-fixed d identical for lz and lz* (correction factor cancels when θ constant).\\\"}}, \\\"exp-ctrl-contam-mistral-clean-s10\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"accuracy_overall\\\": 0.5347, \\\"lz_star\\\": 3.4159, \\\"theta_mle\\\": -1.0286, \\\"n_items\\\": 14042}}, \\\"exp-ctrl-contam-mistral-clean-s9\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"accuracy_overall\\\": 0.5165, \\\"lz_star\\\": 3.5214, \\\"theta_mle\\\": -1.124, \\\"n_items\\\": 14042}}, \\\"exp-ctrl-contam-mistral-clean-s8\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"accuracy_overall\\\": 0.5162, \\\"lz_star\\\": 5.7996, \\\"theta_mle\\\": -1.1457, \\\"n_items\\\": 14042}}, \\\"exp-arcc-benchmark\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"metrics\\\": {\\\"clean_n10_lz_values\\\": [-5.4483, -5.4328, -5.5244, -5.4345, -5.2317, -5.5724, -5.5852, -5.4001, -5.5359, -5.0733], \\\"clean_n10_mean_lz\\\": -5.4239, \\\"clean_n10_sd_lz\\\": 0.1605, \\\"contam15_lz\\\": -4.9165, \\\"contam15_lz_seen\\\": 0.5677, \\\"contam15_acc\\\": 0.9085, \\\"contam50_lz\\\": -4.5725, \\\"contam50_lz_seen\\\": -0.331, \\\"contam50_acc\\\": 0.9424, \\\"cohens_d_contam15\\\": 3.161, \\\"cohens_d_contam15_ci\\\": [2.009, 9.509], \\\"cohens_d_contam50\\\": 5.303, \\\"cohens_d_contam50_ci\\\": [3.639, 15.205], \\\"n_clean_seeds\\\": 10, \\\"server\\\": \\\"westd-19912\\\", \\\"n_items\\\": 295}}, \\\"exp-ctrl-contam-mistral-clean-s7\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"accuracy_overall\\\": 0.5284, \\\"lz_star\\\": 5.8982, \\\"theta_mle\\\": -1.0755, \\\"n_items\\\": 14042}}, \\\"exp-ctrl-contam-mistral-clean-s6\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"accuracy_overall\\\": 0.5128, \\\"lz_star\\\": 5.503, \\\"theta_mle\\\": -1.1405, \\\"n_items\\\": 14042}}, \\\"exp-ctrl-contam-mistral-clean-s5\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"accuracy_overall\\\": 0.5231, \\\"lz_star\\\": 4.491, \\\"theta_mle\\\": -1.1, \\\"n_items\\\": 14042}}, \\\"exp-ctrl-contam-mistral-clean-s4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"accuracy_overall\\\": 0.5105, \\\"lz_star\\\": 3.9558, \\\"theta_mle\\\": -1.1693, \\\"n_items\\\": 14042}}, \\\"llama_clean_s10\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"llama_clean_s9\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"llama_clean_s8\\\": {\\\"status\\\": \\\"DONE\\\"}, \\\"llama_clean_s11\\\": {\\\"status\\\": \\\"DONE\\\"}}, \\\"count\\\": 50, \\\"total\\\": 113, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.2445}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"exp-llama-50pct-s1-pilot\": {\"status\": \"RUNNING\"}, \"exp-llama-15pct-s1-pilot\": {\"status\": \"RUNNING\"}, \"exp-mistral-5pct-s2\": {\"status\": \"PREPARING\", \"metrics\": {\"lz_star\": -5.8961, \"theta_mle\": -0.7915, \"acc_overall\": 0.5691, \"acc_seen\": 0.7707, \"acc_unseen\": 0.5585, \"d_free\": -4.835, \"clean_baseline\": {\"mean\": 4.024, \"std\": 2.052, \"n\": 10}}}, \"exp-mistral-50pct-s3\": {\"status\": \"PREPARING\", \"metrics\": {\"lz_star\": -5.2355, \"theta_mle\": -0.2637, \"acc_overall\": 0.6765, \"acc_seen\": 0.7505, \"acc_unseen\": 0.6025, \"d_free\": -4.512, \"clean_baseline\": {\"mean\": 4.024, \"std\": 2.052, \"n\": 10}}}, \"exp-mistral-15pct-s3\": {\"status\": \"PREPARING\", \"metrics\": {\"lz_star\": -3.127, \"theta_mle\": -0.6502, \"acc_overall\": 0.5971, \"acc_seen\": 0.7702, \"acc_unseen\": 0.5665, \"d_free\": -3.485, \"clean_baseline\": {\"mean\": 4.024, \"std\": 2.052, \"n\": 10}}}, \"exp-llama-5pct-s2\": {\"status\": \"PREPARING\", \"metrics\": {\"lz_star\": -4.4602, \"theta_mle\": -0.3883, \"acc_overall\": 0.6364, \"acc_seen\": 0.7863, \"acc_unseen\": 0.6285, \"d_free\": -4.938, \"clean_baseline\": {\"mean\": -0.312, \"std\": 0.84, \"n\": 10}}}, \"exp-llama-25pct-s2\": {\"status\": \"PREPARING\", \"metrics\": {\"lz_star\": -3.2486, \"theta_mle\": -0.2231, \"acc_overall\": 0.6794, \"acc_seen\": 0.7766, \"acc_unseen\": 0.647, \"d_free\": -3.496, \"clean_baseline\": {\"mean\": -0.312, \"std\": 0.84, \"n\": 10}}}, \"exp-mistral-25pct-s2\": {\"status\": \"ANALYZING\"}, \"exp-llama-25pct-s3\": {\"status\": \"ANALYZING\"}, \"exp-llama-5pct-s3\": {\"status\": \"ANALYZING\"}, \"exp-mistral-25pct-s1\": {\"status\": \"ANALYZING\"}, \"exp-llama-50pct-s3\": {\"status\": \"PREPARING\", \"metrics\": {\"lz_star\": -2.8096, \"theta_mle\": -0.0433, \"acc_overall\": 0.7121, \"acc_seen\": 0.7684, \"acc_unseen\": 0.6559, \"d_free\": -2.973, \"clean_baseline\": {\"mean\": -0.312, \"std\": 0.84, \"n\": 10}}}, \"exp-llama-15pct-s3\": {\"status\": \"PREPARING\", \"metrics\": {\"lz_star\": -4.5067, \"theta_mle\": -0.3251, \"acc_overall\": 0.6584, \"acc_seen\": 0.7854, \"acc_unseen\": 0.636, \"d_free\": -4.994, \"clean_baseline\": {\"mean\": -0.312, \"std\": 0.84, \"n\": 10}}}, \"exp-mistral-5pct-s1\": {\"status\": \"PREPARING\", \"metrics\": {\"lz_star\": -1.7664, \"theta_mle\": -0.7967, \"acc_overall\": 0.5707, \"acc_seen\": 0.7664, \"acc_unseen\": 0.5604, \"d_free\": -2.822, \"clean_baseline\": {\"mean\": 4.024, \"std\": 2.052, \"n\": 10}}}, \"exp-llama-25pct-s1\": {\"status\": \"PREPARING\", \"metrics\": {\"lz_star\": -4.6159, \"theta_mle\": -0.2756, \"acc_overall\": 0.6716, \"acc_seen\": 0.7698, \"acc_unseen\": 0.6388, \"d_free\": -5.124, \"clean_baseline\": {\"mean\": -0.312, \"std\": 0.84, \"n\": 10}}}, \"exp-llama-5pct-s1\": {\"status\": \"PREPARING\", \"metrics\": {\"lz_star\": -4.695, \"theta_mle\": -0.407, \"acc_overall\": 0.638, \"acc_seen\": 0.801, \"acc_unseen\": 0.629, \"lz_star_seen\": -0.61, \"lz_star_unseen\": -4.398, \"d_free\": -5.22, \"clean_baseline\": {\"mean\": -0.312, \"std\": 0.84, \"n\": 10}}}, \"exp-mistral-25pct-s3\": {\"status\": \"PREPARING\"}, \"exp-mistral-50pct-s2\": {\"status\": \"PREPARING\", \"metrics\": {\"lz_star\": -4.695, \"theta_mle\": -0.272, \"acc_overall\": 0.677, \"acc_seen\": 0.75, \"acc_unseen\": 0.603, \"d_free\": -4.25, \"clean_baseline\": {\"mean\": 4.024, \"std\": 2.052, \"n\": 10}}}, \"exp-mistral-15pct-s2\": {\"status\": \"PREPARING\", \"metrics\": {\"lz_star\": -4.141, \"theta_mle\": -0.611, \"acc_overall\": 0.605, \"acc_seen\": 0.768, \"acc_unseen\": 0.576, \"d_free\": -3.98, \"clean_baseline\": {\"mean\": 4.024, \"std\": 2.052, \"n\": 10}}}, \"exp-llama-50pct-s2\": {\"status\": \"PREPARING\", \"metrics\": {\"lz_star\": -3.735, \"theta_mle\": -0.086, \"acc_overall\": 0.708, \"acc_seen\": 0.765, \"acc_unseen\": 0.65, \"d_free\": -4.08, \"clean_baseline\": {\"mean\": -0.312, \"std\": 0.84, \"n\": 10}}}, \"exp-llama-15pct-s2\": {\"status\": \"PREPARING\", \"metrics\": {\"lz_star\": -4.68, \"theta_mle\": -0.319, \"acc_overall\": 0.658, \"acc_seen\": 0.774, \"acc_unseen\": 0.638, \"d_free\": -5.2, \"clean_baseline\": {\"mean\": -0.312, \"std\": 0.84, \"n\": 10}}}, \"exp-ctrl-contam-qwen-25pct-s2\": {\"status\": \"DONE\"}, \"exp-ctrl-contam-qwen-15pct-multiseed\": {\"status\": \"DONE\", \"metrics\": {\"seed_42\": {\"lz_star_free\": 3.8494, \"d_free\": -6.57, \"d_free_ci\": [-15.19, -4.54], \"d_fixed\": 4.77, \"d_fixed_ci\": [3.96, 7.76]}, \"seed_123\": {\"lz_star_free\": 4.939, \"d_free\": -5.09, \"d_free_ci\": [-11.72, -3.44], \"d_fixed\": 7.79, \"d_fixed_ci\": [6.51, 13.05]}, \"seed_456\": {\"lz_star_free\": 5.44, \"d_free\": -4.41, \"lz_fixed\": 11.99, \"d_fixed\": 7.99, \"d_fixed_ci\": [6.68, 13.4]}, \"stats_free\": {\"mean_abs_d\": 5.36, \"sd\": 1.1, \"cv\": 0.206, \"range\": [4.41, 6.57]}, \"stats_fixed\": {\"mean_abs_d\": 6.85, \"sd\": 1.8, \"cv\": 0.263, \"range\": [4.77, 7.99]}, \"n_seeds\": 3, \"clean_baseline_free\": {\"n\": 10, \"mean\": 8.6838, \"std\": 0.7353}, \"clean_baseline_fixed\": {\"n\": 10, \"mean\": 7.3522, \"std\": 0.5802, \"theta_fixed\": -0.1022}}}, \"exp-ctrl-contam-qwen-50pct-multiseed\": {\"status\": \"DONE\", \"metrics\": {\"seed_42\": {\"lz_star_free\": 7.2892, \"d_free\": -1.9, \"lz_fixed\": null, \"d_fixed\": 14.52}, \"seed_123\": {\"lz_star_free\": 4.7, \"d_free\": -5.42, \"lz_fixed\": 14.687, \"d_fixed\": 12.64, \"d_fixed_ci\": [10.54, 21.46]}, \"seed_456\": {\"lz_star_free\": 2.8695, \"d_free\": -7.91, \"d_free_ci\": [-18.29, -5.52], \"lz_fixed\": 13.036, \"d_fixed\": 9.8, \"d_fixed_ci\": [8.18, 16.46]}, \"stats_free\": {\"mean_abs_d\": 5.08, \"sd\": 3.02, \"cv\": 0.595, \"range\": [1.9, 7.91]}, \"stats_fixed\": {\"mean_abs_d\": 12.32, \"sd\": 2.38, \"cv\": 0.193, \"range\": [9.8, 14.52]}, \"n_seeds\": 3, \"clean_baseline_free\": {\"n\": 10, \"mean\": 8.6838, \"std\": 0.7353}, \"clean_baseline_fixed\": {\"n\": 10, \"mean\": 7.3522, \"std\": 0.5802, \"theta_fixed\": -0.1022}}}, \"exp-ctrl-contam-qwen-25pct-multiseed\": {\"status\": \"DONE\", \"metrics\": {\"seed_42\": {\"lz_star_free\": 2.6429, \"d_free\": -8.22, \"lz_fixed\": 10.229, \"d_fixed\": 4.96, \"d_fixed_ci\": [4.13, 8.12]}, \"seed_123\": {\"lz_star_free\": 2.23, \"d_free\": -8.78, \"lz_fixed\": 10.47, \"d_fixed\": 5.37, \"d_fixed_ci\": [4.48, 8.83]}, \"seed_456\": {\"lz_star_free\": 4.78, \"d_free\": -5.31, \"lz_fixed\": 11.611, \"d_fixed\": 7.34, \"d_fixed_ci\": [6.14, 12.26]}, \"stats_free\": {\"mean_abs_d\": 7.44, \"sd\": 1.86, \"cv\": 0.25, \"range\": [5.31, 8.78]}, \"stats_fixed\": {\"mean_abs_d\": 5.89, \"sd\": 1.27, \"cv\": 0.216, \"range\": [4.96, 7.34]}, \"n_seeds\": 3, \"clean_baseline_free\": {\"n\": 10, \"mean\": 8.6838, \"std\": 0.7353}, \"clean_baseline_fixed\": {\"n\": 10, \"mean\": 7.3522, \"std\": 0.5802, \"theta_fixed\": -0.1022}}}, \"eval-contam-25-s3\": {\"status\": \"PREPARING\"}, \"exp-ctrl-contam-qwen-50pct-s2\": {\"status\": \"PREPARING\"}, \"exp-ctrl-contam-qwen-25pct-s3\": {\"status\": \"PREPARING\"}, \"exp-ctrl-contam-qwen-25pct-s2-eval\": {\"status\": \"PREPARING\"}, \"eval-ctrl-contam-qwen-15pct-s2\": {\"status\": \"PREPARING\"}, \"exp-ctrl-contam-qwen-15pct-s2\": {\"status\": \"DONE\"}, \"exp-ctrl-contam-llama-5pct\": {\"status\": \"DONE\", \"metrics\": {\"theta_mle\": -0.4089, \"lz_star_free\": -4.954, \"lz_star_fixed\": -1.8923, \"accuracy_overall\": 0.6342, \"accuracy_seen\": 0.792, \"accuracy_unseen\": 0.6259, \"n_items\": 14042, \"n_seen\": 702, \"cohens_d_free\": {\"d\": -5.5254, \"ci_95\": [-10.8, -4.05]}, \"cohens_d_fixed\": {\"d\": -1.7027, \"ci_95\": [-3.87, -1.2]}}}, \"exp-ctrl-contam-qwen-5pct\": {\"status\": \"DONE\", \"metrics\": {\"theta_mle\": 0.0879, \"lz_star_free\": 5.6309, \"lz_star_fixed\": 11.09, \"accuracy_overall\": 0.7141, \"accuracy_seen\": 0.8291, \"accuracy_unseen\": 0.708, \"n_items\": 14042, \"n_seen\": 702, \"train_loss\": 1.39, \"train_runtime_sec\": 1127, \"cohens_d_free\": {\"d\": -4.1518, \"ci_95\": [-9.8505, -2.7418]}, \"cohens_d_fixed\": {\"d\": 3.5156, \"ci_95\": [2.8999, 5.7097]}}}, \"exp-ctrl-contam-mistral\": {\"status\": \"DONE\", \"metrics\": {\"n_seeds\": 10, \"clean_lz_values\": [5.4175, -1.0456, 3.2792, 3.9558, 4.491, 5.503, 5.8982, 5.7996, 3.5214, 3.4159], \"clean_lz_mean\": 4.0236, \"clean_lz_std\": 2.052, \"contam_15_lz\": -2.1468, \"contam_50_lz\": -3.1539, \"cohens_d_contam15\": -3.007, \"cohens_d_contam15_ci95\": [-8.18, -1.75], \"cohens_d_contam50\": -3.498, \"cohens_d_contam50_ci95\": [-9.39, -2.09], \"bootstrap_n\": 10000, \"theta_fixed\": -1.0876, \"theta_fixed_n_theta\": 10, \"theta_fixed_n_lz\": 6, \"theta_fixed_clean_lz\": [5.3714, -1.3154, 3.0571, 5.769, 3.5155, 3.3474], \"theta_fixed_clean_lz_seeds\": [\"s1\", \"s2\", \"s3\", \"s8\", \"s9\", \"s10\"], \"cohens_d_contam15_theta_fixed\": 2.69, \"cohens_d_contam15_theta_fixed_ci95\": [1.53, 9.06], \"cohens_d_contam50_theta_fixed\": 5.8, \"cohens_d_contam50_theta_fixed_ci95\": [3.87, 18.45], \"note\": \"2026-05-22: Free-theta d uses n=10 (all seeds). theta_fixed uses n=10 theta_MLE mean (-1.0876), but lz*_fixed distribution only n=6 (s4-s7 response vectors lost with server 19912).\"}}, \"exp-ctrl-contam-llama-25pct\": {\"status\": \"DONE\", \"metrics\": {\"lz_star_snijders\": -2.8045, \"accuracy_overall\": 0.6781, \"accuracy_seen\": 0.7715, \"accuracy_unseen\": 0.647, \"theta_mle\": -0.2207, \"cohens_d\": -2.9667, \"cohens_d_ci95_percentile\": [-6.06, -2.03], \"cohens_d_ci95_bca\": [-4.74, -1.64], \"bootstrap_n\": 10000, \"clean_baseline\": {\"n\": 10, \"lz_star_mean\": -0.3123, \"lz_star_std_ddof1\": 0.8401}}}, \"exp-ctrl-contam-qwen-25pct\": {\"status\": \"DONE\", \"metrics\": {\"lz_star_snijders\": 2.6429, \"accuracy_overall\": 0.7405, \"accuracy_seen\": 0.8105, \"accuracy_unseen\": 0.7171, \"theta_mle\": 0.2576, \"cohens_d\": -8.2153, \"cohens_d_ci95_percentile\": [-18.88, -5.73], \"cohens_d_ci95_bca\": [-14.71, -4.94], \"bootstrap_n\": 10000, \"clean_baseline\": {\"n\": 10, \"lz_star_mean\": 8.6838, \"lz_star_std\": 0.7353, \"source\": \"unified_lz_recompute.py (Snijders 2001)\"}}}, \"exp-ctrl-contam-llama\": {\"status\": \"DONE\", \"metrics\": {\"n_seeds\": 10, \"clean_lz_values\": [-0.4891, -0.7793, 0.4109, 0.6498, -0.3043, -1.1483, 0.1419, 0.7175, -0.3718, -1.9506], \"clean_lz_mean\": -0.3123, \"clean_lz_std\": 0.8296, \"contam_15_lz\": -2.1955, \"contam_50_lz\": -2.3897, \"cohens_d_contam15\": -2.269, \"cohens_d_contam15_ci95\": [-4.63, -1.561], \"cohens_d_contam50\": -2.503, \"cohens_d_contam50_ci95\": [-5.19, -1.759], \"bootstrap_n\": 10000, \"theta_fixed\": -0.6426, \"cohens_d_contam15_theta_fixed\": -0.58, \"cohens_d_contam15_theta_fixed_ci95\": [-2.37, 0.04], \"cohens_d_contam50_theta_fixed\": -0.84, \"cohens_d_contam50_theta_fixed_ci95\": [-2.97, -0.17]}}, \"exp-ctrl-contam-pilot\": {\"status\": \"DONE\", \"metrics\": {\"n_seeds\": 10, \"source\": \"unified_lz_recompute.py (single-source Snijders 2001)\", \"clean_lz_star_snijders\": [9.4676, 7.0539, 9.5293, 8.9673, 8.5322, 8.2445, 8.7702, 9.111, 9.0132, 8.1492], \"clean_lz_star_mean\": 8.6838, \"clean_lz_star_std\": 0.7353, \"clean_lz_drasgow\": [8.0101, 5.944, 8.0806, 7.609, 7.1963, 6.9848, 7.4005, 7.7188, 7.6799, 6.9272], \"contam_15_lz_star\": 3.8494, \"contam_50_lz_star\": 7.2892, \"contam_15_lz_drasgow\": 3.0046, \"contam_50_lz_drasgow\": 5.448, \"cohens_d_contam15_lz_star\": -6.575, \"cohens_d_contam15_lz_star_bootstrap\": [-15.19, -4.54], \"cohens_d_contam50_lz_star\": -1.897, \"cohens_d_contam50_lz_star_bootstrap\": [-4.95, -1.04], \"theta_fixed\": -0.1022, \"cohens_d_contam15_theta_fixed\": 4.77, \"cohens_d_contam15_theta_fixed_bootstrap\": [3.97, 7.79], \"cohens_d_contam50_theta_fixed\": 14.521, \"cohens_d_contam50_theta_fixed_bootstrap\": [12.1, 24.79], \"bootstrap_n\": 10000, \"note\": \"Unified recomputation 2026-05-21. θ-fixed d identical for lz and lz* (correction factor cancels when θ constant).\"}}, \"exp-ctrl-contam-mistral-clean-s10\": {\"status\": \"DONE\", \"metrics\": {\"accuracy_overall\": 0.5347, \"lz_star\": 3.4159, \"theta_mle\": -1.0286, \"n_items\": 14042}}, \"exp-ctrl-contam-mistral-clean-s9\": {\"status\": \"DONE\", \"metrics\": {\"accuracy_overall\": 0.5165, \"lz_star\": 3.5214, \"theta_mle\": -1.124, \"n_items\": 14042}}, \"exp-ctrl-contam-mistral-clean-s8\": {\"status\": \"DONE\", \"metrics\": {\"accuracy_overall\": 0.5162, \"lz_star\": 5.7996, \"theta_mle\": -1.1457, \"n_items\": 14042}}, \"exp-arcc-benchmark\": {\"status\": \"PREPARING\", \"metrics\": {\"clean_n10_lz_values\": [-5.4483, -5.4328, -5.5244, -5.4345, -5.2317, -5.5724, -5.5852, -5.4001, -5.5359, -5.0733], \"clean_n10_mean_lz\": -5.4239, \"clean_n10_sd_lz\": 0.1605, \"contam15_lz\": -4.9165, \"contam15_lz_seen\": 0.5677, \"contam15_acc\": 0.9085, \"contam50_lz\": -4.5725, \"contam50_lz_seen\": -0.331, \"contam50_acc\": 0.9424, \"cohens_d_contam15\": 3.161, \"cohens_d_contam15_ci\": [2.009, 9.509], \"cohens_d_contam50\": 5.303, \"cohens_d_contam50_ci\": [3.639, 15.205], \"n_clean_seeds\": 10, \"server\": \"westd-19912\", \"n_items\": 295}}, \"exp-ctrl-contam-mistral-clean-s7\": {\"status\": \"DONE\", \"metrics\": {\"accuracy_overall\": 0.5284, \"lz_star\": 5.8982, \"theta_mle\": -1.0755, \"n_items\": 14042}}, \"exp-ctrl-contam-mistral-clean-s6\": {\"status\": \"DONE\", \"metrics\": {\"accuracy_overall\": 0.5128, \"lz_star\": 5.503, \"theta_mle\": -1.1405, \"n_items\": 14042}}, \"exp-ctrl-contam-mistral-clean-s5\": {\"status\": \"DONE\", \"metrics\": {\"accuracy_overall\": 0.5231, \"lz_star\": 4.491, \"theta_mle\": -1.1, \"n_items\": 14042}}, \"exp-ctrl-contam-mistral-clean-s4\": {\"status\": \"DONE\", \"metrics\": {\"accuracy_overall\": 0.5105, \"lz_star\": 3.9558, \"theta_mle\": -1.1693, \"n_items\": 14042}}, \"llama_clean_s10\": {\"status\": \"DONE\"}, \"llama_clean_s9\": {\"status\": \"DONE\"}, \"llama_clean_s8\": {\"status\": \"DONE\"}, \"llama_clean_s11\": {\"status\": \"DONE\"}}, \"count\": 50, \"total\": 113, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2445}}"
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
Now I have the data. Let me also look for exp-llama-5pct-s3 and exp-llama-25pct-s3 which are in "ANALYZING" status without metrics. Let me get their full data.

From the registry:
- exp-llama-5pct-s3: status="ANALYZING", no metrics shown
- exp-llama-25pct-s3: status="ANALYZING", no metrics shown

So the registry doesn't have lz* values for these two experiments yet. Let me check if there are any more details by fetching all fields.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9dd1310f-2eca-4936-af7c-90a1b8a75881",
  "uuid": "360d5386-1186-4ce1-822b-d015cd62aa1c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ju5uFxckKVYRA1pdoT9Uyf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7339,
      "cache_read_input_tokens": 30661,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7339
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

exp-llama-5pct-s3 和 exp-llama-25pct-s3 在 registry 中状态为 ANALYZING，没有 metrics。让我看看是否有更多信息。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9dd1310f-2eca-4936-af7c-90a1b8a75881",
  "uuid": "f8ded7ea-f56c-4e75-9ea6-70bb18302f58",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ju5uFxckKVYRA1pdoT9Uyf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7339,
      "cache_read_input_tokens": 30661,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7339
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01CVNSLohRV3JKsYA6tNJWCx`</summary>

```json
{
  "project": "irt_personfit_contam",
  "filters": {
    "exp_id": "exp-llama-5pct-s3"
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
  "session_id": "9dd1310f-2eca-4936-af7c-90a1b8a75881",
  "uuid": "ca88141d-d4eb-48d4-badd-1349029647dc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ju5uFxckKVYRA1pdoT9Uyf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7339,
      "cache_read_input_tokens": 30661,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7339
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

_source line 21 · 2026-05-23T15:04:11.783Z_

<details><summary>↩ Tool result · `toolu_01CVNSLohRV3JKsYA6tNJWCx`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2444}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9dd1310f-2eca-4936-af7c-90a1b8a75881",
  "uuid": "a69245e4-3fff-4696-bfd9-07bb22355ee8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.2444}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2444}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01LM8H9T2NsCHzZCiMa5dxWE`</summary>

```json
{
  "project": "irt_personfit_contam",
  "filters": {
    "exp_id": "exp-llama-25pct-s3"
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
  "session_id": "9dd1310f-2eca-4936-af7c-90a1b8a75881",
  "uuid": "2465a07f-d5c9-4509-9ae2-bb39718f6eed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ju5uFxckKVYRA1pdoT9Uyf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7339,
      "cache_read_input_tokens": 30661,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7339
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

_source line 23 · 2026-05-23T15:04:12.468Z_

<details><summary>↩ Tool result · `toolu_01LM8H9T2NsCHzZCiMa5dxWE`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2655}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9dd1310f-2eca-4936-af7c-90a1b8a75881",
  "uuid": "075c0832-9dac-4f9a-ae6e-dae4ce3ec2df",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.2655}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2655}}"
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
The filter by exp_id returns empty. The experiment names appear in the list but filtering by exp_id doesn't work - probably the field name is different. Let me check the registry directly to see how they're stored. Let me look at the data I already have more carefully.

From the previous query, I can see:
- `exp-llama-5pct-s3`: status="ANALYZING" - no metrics
- `exp-llama-25pct-s3`: status="ANALYZING" - no metrics

These two experiments don't have lz* values yet in the registry.

Now let me compile all the data I have:

User-provided lz* values + registry data:


- exp-llama-5pct-s1 matches at -4.695
- exp-llama-5pct-s2 shows -4.460 from user input versus -4.4602 in the registry
- exp-llama-5pct-s3 is still analyzing with no metrics available
- exp-llama-15pct-s2 aligns at -4.68
- exp-llama-15pct-s3 shows -4.507 from user versus -4.5067 in the registry
- exp-llama-25pct-s1 has -4.616 from the user data matching -4.6159 in the registry
- exp-llama-25pct-s2 shows -3.249 from user versus -3.2486 in the registry
- exp-llama-25pct-s3 is still analyzing with no metrics available
- exp-llama-50pct-s2 aligns at -3.735
- exp-llama-50pct-s3 shows -2.810 from user versus -2.8096 in the registry

Two experiments are still pending analysis. Now I'm calculating the new baseline with a mean of 0.2618 and standard deviation of 1.5418, comparing it against the old baseline from the registry which had a mean of -0.312 and standard deviation of 0.840.

I'm working through the effect size calculations using both the old and new baseline formulas to verify the registry values, starting with exp-llama-5pct-s1 where the lz* value of -4.695 should produce a d_free of -5.22 under the old formula. Continuing through the remaining experiments, I'm verifying the calculations for the 15% perturbation cases. The old d values are matching the registry entries, and I'm computing the new d values using the updated formula with the adjusted parameters. Now I'm pulling the more precise registry values and setting up the calculation to compare how effect sizes shift between the old and new baselines using the formulas for standardized differences. Continuing through the remaining experiments with the registry values, calculating the shifts in standardized deviations for each configuration. I'm working through the division more carefully by hand—breaking down -4.8777 / 1.5418 step by step to get -3.164, which gives me a change of +1.960 for this model.

Now I'm calculating the old and new d values for the next variant: the old formula gives -3.496, while the new one yields -2.277, representing a shift of +1.219. I'm also starting to look at the remaining models in the comparison.

For exp-llama-50pct-s2 with lz* = -3.735, I'm working through similar calculations to get the old d of -4.075 and new d of -2.592, which gives a change of +1.483. I notice the registry shows d_free = -4.08, so I'm double-checking my arithmetic to make sure it aligns.

Now I'm moving to exp-llama-50pct-s3 with lz* = -2.8096, calculating the old d as -2.973 and working through the new d calculation.

Let me recalculate more carefully—I'm getting -3.0714 which is very close to -3.0836, so the change in d comes out to about +0.981. Actually, I should just compute this precisely using Python to avoid rounding errors.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9dd1310f-2eca-4936-af7c-90a1b8a75881",
  "uuid": "b56b3f51-c72d-4037-9ca1-c0d2d5a59256",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DLaj6WsorXc7j5YEVXK1FK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 643,
      "cache_read_input_tokens": 38000,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 643
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

exp-llama-5pct-s3 和 exp-llama-25pct-s3 在 registry 中是 ANALYZING 状态，没有 lz* 值。用 Python 精确计算所有 Cohen's d。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9dd1310f-2eca-4936-af7c-90a1b8a75881",
  "uuid": "1d919703-20bb-4580-8b29-5dcc949aebfa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DLaj6WsorXc7j5YEVXK1FK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 643,
      "cache_read_input_tokens": 38000,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 643
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

<details open><summary>🔧 Tool call — Bash · `toolu_01BNJ2tVooro2CHN6QnmVm16`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\n# New V2 clean baseline\nnew_mean = 0.2618\nnew_sd = 1.5418\n\n# Old clean baseline\nold_mean = -0.312\nold_sd = 0.840\n\n# Registry lz* values (more precise where available)\nexperiments = [\n    ('exp-llama-5pct-s1',  5,  42,  -4.695),\n    ('exp-llama-5pct-s2',  5,  123, -4.4602),\n    ('exp-llama-5pct-s3',  5,  456, None),  # ANALYZING\n    ('exp-llama-15pct-s2', 15, 123, -4.68),\n    ('exp-llama-15pct-s3', 15, 456, -4.5067),\n    ('exp-llama-25pct-s1', 25, 42,  -4.6159),\n    ('exp-llama-25pct-s2', 25, 123, -3.2486),\n    ('exp-llama-25pct-s3', 25, 456, None),  # ANALYZING\n    ('exp-llama-50pct-s2', 50, 123, -3.735),\n    ('exp-llama-50pct-s3', 50, 456, -2.8096),\n]\n\nprint('=== 表格 1: 每个实验的新旧 d 值对比 ===')\nprint(f'| exp_id | contam% | seed | lz* | 旧 d | 新 d | Δd |')\nprint(f'|--------|---------|------|-----|------|------|-----|')\n\nresults = {}\nfor exp_id, contam, seed, lz_star in experiments:\n    if lz_star is None:\n        print(f'| {exp_id} | {contam}% | {seed} | — | — | — | — (ANALYZING) |')\n        continue\n    old_d = (lz_star - old_mean) / old_sd\n    new_d = (lz_star - new_mean) / new_sd\n    delta_d = new_d - old_d\n    print(f'| {exp_id} | {contam}% | {seed} | {lz_star:.4f} | {old_d:.3f} | {new_d:.3f} | {delta_d:+.3f} |')\n    \n    if contam not in results:\n        results[contam] = []\n    results[contam].append(new_d)\n\nprint()\nprint('=== 表格 2: Multi-seed 汇总 ===')\nprint(f'| contam% | seeds | mean(d) | SD(d) | n |')\nprint(f'|---------|-------|---------|-------|---|')\n\nimport statistics\nfor contam in sorted(results.keys()):\n    ds = results[contam]\n    n = len(ds)\n    mean_d = statistics.mean(ds)\n    sd_d = statistics.stdev(ds) if n > 1 else float('nan')\n    seed_note = ''\n    if contam == 5:\n        seed_note = 's1,s2 (s3 analyzing)'\n    elif contam == 15:\n        seed_note = 's2,s3 (s1 pilot training)'\n    elif contam == 25:\n        if n == 2:\n            seed_note = 's1,s2 (s3 analyzing)'\n        else:\n            seed_note = 's1,s2,s3'\n    elif contam == 50:\n        seed_note = 's2,s3 (s1 pilot training)'\n    print(f'| {contam}% | {seed_note} | {mean_d:.3f} | {sd_d:.3f} | {n} |')\n\nprint()\nprint('=== 旧 vs 新 baseline 参数对比 ===')\nprint(f'旧 baseline: mean={old_mean}, SD={old_sd} (V1, n=10)')\nprint(f'新 baseline: mean={new_mean}, SD={new_sd} (V2 re-eval, n=10)')\nprint(f'SD 比值: {new_sd/old_sd:.3f}x → 新 d 绝对值约为旧的 {old_sd/new_sd:.1%}')\n\"\n",
  "description": "Compute old and new Cohen's d for all Llama experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9dd1310f-2eca-4936-af7c-90a1b8a75881",
  "uuid": "386c1af9-acef-4b34-b912-35ed8b107ddb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DLaj6WsorXc7j5YEVXK1FK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 643,
      "cache_read_input_tokens": 38000,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 643
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

_source line 27 · 2026-05-23T15:05:08.247Z_

<details><summary>↩ Tool result · `toolu_01BNJ2tVooro2CHN6QnmVm16`</summary>

```text
=== 表格 1: 每个实验的新旧 d 值对比 ===
| exp_id | contam% | seed | lz* | 旧 d | 新 d | Δd |
|--------|---------|------|-----|------|------|-----|
| exp-llama-5pct-s1 | 5% | 42 | -4.6950 | -5.218 | -3.215 | +2.003 |
| exp-llama-5pct-s2 | 5% | 123 | -4.4602 | -4.938 | -3.063 | +1.876 |
| exp-llama-5pct-s3 | 5% | 456 | — | — | — | — (ANALYZING) |
| exp-llama-15pct-s2 | 15% | 123 | -4.6800 | -5.200 | -3.205 | +1.995 |
| exp-llama-15pct-s3 | 15% | 456 | -4.5067 | -4.994 | -3.093 | +1.901 |
| exp-llama-25pct-s1 | 25% | 42 | -4.6159 | -5.124 | -3.164 | +1.960 |
| exp-llama-25pct-s2 | 25% | 123 | -3.2486 | -3.496 | -2.277 | +1.219 |
| exp-llama-25pct-s3 | 25% | 456 | — | — | — | — (ANALYZING) |
| exp-llama-50pct-s2 | 50% | 123 | -3.7350 | -4.075 | -2.592 | +1.483 |
| exp-llama-50pct-s3 | 50% | 456 | -2.8096 | -2.973 | -1.992 | +0.981 |

=== 表格 2: Multi-seed 汇总 ===
| contam% | seeds | mean(d) | SD(d) | n |
|---------|-------|---------|-------|---|
| 5% | s1,s2 (s3 analyzing) | -3.139 | 0.108 | 2 |
| 15% | s2,s3 (s1 pilot training) | -3.149 | 0.079 | 2 |
| 25% | s1,s2 (s3 analyzing) | -2.720 | 0.627 | 2 |
| 50% | s2,s3 (s1 pilot training) | -2.292 | 0.424 | 2 |

=== 旧 vs 新 baseline 参数对比 ===
旧 baseline: mean=-0.312, SD=0.84 (V1, n=10)
新 baseline: mean=0.2618, SD=1.5418 (V2 re-eval, n=10)
SD 比值: 1.835x → 新 d 绝对值约为旧的 54.5%
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9dd1310f-2eca-4936-af7c-90a1b8a75881",
  "uuid": "5bc919a0-e8ac-4a20-9e63-104f98d53a60",
  "tool_use_result": {
    "stdout": "=== 表格 1: 每个实验的新旧 d 值对比 ===\n| exp_id | contam% | seed | lz* | 旧 d | 新 d | Δd |\n|--------|---------|------|-----|------|------|-----|\n| exp-llama-5pct-s1 | 5% | 42 | -4.6950 | -5.218 | -3.215 | +2.003 |\n| exp-llama-5pct-s2 | 5% | 123 | -4.4602 | -4.938 | -3.063 | +1.876 |\n| exp-llama-5pct-s3 | 5% | 456 | — | — | — | — (ANALYZING) |\n| exp-llama-15pct-s2 | 15% | 123 | -4.6800 | -5.200 | -3.205 | +1.995 |\n| exp-llama-15pct-s3 | 15% | 456 | -4.5067 | -4.994 | -3.093 | +1.901 |\n| exp-llama-25pct-s1 | 25% | 42 | -4.6159 | -5.124 | -3.164 | +1.960 |\n| exp-llama-25pct-s2 | 25% | 123 | -3.2486 | -3.496 | -2.277 | +1.219 |\n| exp-llama-25pct-s3 | 25% | 456 | — | — | — | — (ANALYZING) |\n| exp-llama-50pct-s2 | 50% | 123 | -3.7350 | -4.075 | -2.592 | +1.483 |\n| exp-llama-50pct-s3 | 50% | 456 | -2.8096 | -2.973 | -1.992 | +0.981 |\n\n=== 表格 2: Multi-seed 汇总 ===\n| contam% | seeds | mean(d) | SD(d) | n |\n|---------|-------|---------|-------|---|\n| 5% | s1,s2 (s3 analyzing) | -3.139 | 0.108 | 2 |\n| 15% | s2,s3 (s1 pilot training) | -3.149 | 0.079 | 2 |\n| 25% | s1,s2 (s3 analyzing) | -2.720 | 0.627 | 2 |\n| 50% | s2,s3 (s1 pilot training) | -2.292 | 0.424 | 2 |\n\n=== 旧 vs 新 baseline 参数对比 ===\n旧 baseline: mean=-0.312, SD=0.84 (V1, n=10)\n新 baseline: mean=0.2618, SD=1.5418 (V2 re-eval, n=10)\nSD 比值: 1.835x → 新 d 绝对值约为旧的 54.5%",
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

_source line 28_

<details><summary>Logged reasoning block</summary>

```text
The results are computed. Let me present the results cleanly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9dd1310f-2eca-4936-af7c-90a1b8a75881",
  "uuid": "0d2a2f31-bd63-4613-9782-5b3148168fde",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CJRaX4u7MjA4ogmxdysQiR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5644,
      "cache_read_input_tokens": 38643,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5644
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

结果如下：

### 表格 1: 每个实验的新旧 d 值对比

| exp_id | contam% | seed | lz* | 旧 d | 新 d | Δd |
|--------|---------|------|------|------|------|------|
| exp-llama-5pct-s1 | 5% | 42 | -4.695 | -5.218 | **-3.215** | +2.003 |
| exp-llama-5pct-s2 | 5% | 123 | -4.460 | -4.938 | **-3.063** | +1.876 |
| exp-llama-5pct-s3 | 5% | 456 | — | — | — | ANALYZING |
| exp-llama-15pct-s2 | 15% | 123 | -4.680 | -5.200 | **-3.205** | +1.995 |
| exp-llama-15pct-s3 | 15% | 456 | -4.507 | -4.994 | **-3.093** | +1.901 |
| exp-llama-25pct-s1 | 25% | 42 | -4.616 | -5.124 | **-3.164** | +1.960 |
| exp-llama-25pct-s2 | 25% | 123 | -3.249 | -3.496 | **-2.277** | +1.219 |
| exp-llama-25pct-s3 | 25% | 456 | — | — | — | ANALYZING |
| exp-llama-50pct-s2 | 50% | 123 | -3.735 | -4.075 | **-2.592** | +1.483 |
| exp-llama-50pct-s3 | 50% | 456 | -2.810 | -2.973 | **-1.992** | +0.981 |

### 表格 2: Multi-seed 汇总

| contam% | seeds | mean(d) | SD(d) | n |
|---------|-------|---------|-------|---|
| 5% | s1,s2 (s3 analyzing) | -3.139 | 0.108 | 2 |
| 15% | s2,s3 (s1 pilot training) | -3.149 | 0.079 | 2 |
| 25% | s1,s2 (s3 analyzing) | -2.720 | 0.627 | 2 |
| 50% | s2,s3 (s1 pilot training) | -2.292 | 0.424 | 2 |

### 关键变化

- 新 baseline SD (1.5418) 是旧 SD (0.840) 的 **1.84x**，所以所有新 d 的绝对值约为旧值的 **55%**
- 新 baseline mean 从 -0.312 右移到 +0.262，分子也变大
- 所有 Δd 均为正值（+0.98 ~ +2.00），即新 d 绝对值一致缩小
- 所有新 d 仍为大效应量（|d| > 1.99），检测力充足
- 缺失数据：exp-llama-5pct-s3 和 exp-llama-25pct-s3 仍在 ANALYZING；15pct-s1 和 50pct-s1 正在 pilot 训练

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9dd1310f-2eca-4936-af7c-90a1b8a75881",
  "uuid": "a9f35b5f-a301-4590-bc77-61097e015661",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CJRaX4u7MjA4ogmxdysQiR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5644,
      "cache_read_input_tokens": 38643,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5644
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

_source line 30_

结果如下：

### 表格 1: 每个实验的新旧 d 值对比

| exp_id | contam% | seed | lz* | 旧 d | 新 d | Δd |
|--------|---------|------|------|------|------|------|
| exp-llama-5pct-s1 | 5% | 42 | -4.695 | -5.218 | **-3.215** | +2.003 |
| exp-llama-5pct-s2 | 5% | 123 | -4.460 | -4.938 | **-3.063** | +1.876 |
| exp-llama-5pct-s3 | 5% | 456 | — | — | — | ANALYZING |
| exp-llama-15pct-s2 | 15% | 123 | -4.680 | -5.200 | **-3.205** | +1.995 |
| exp-llama-15pct-s3 | 15% | 456 | -4.507 | -4.994 | **-3.093** | +1.901 |
| exp-llama-25pct-s1 | 25% | 42 | -4.616 | -5.124 | **-3.164** | +1.960 |
| exp-llama-25pct-s2 | 25% | 123 | -3.249 | -3.496 | **-2.277** | +1.219 |
| exp-llama-25pct-s3 | 25% | 456 | — | — | — | ANALYZING |
| exp-llama-50pct-s2 | 50% | 123 | -3.735 | -4.075 | **-2.592** | +1.483 |
| exp-llama-50pct-s3 | 50% | 456 | -2.810 | -2.973 | **-1.992** | +0.981 |

### 表格 2: Multi-seed 汇总

| contam% | seeds | mean(d) | SD(d) | n |
|---------|-------|---------|-------|---|
| 5% | s1,s2 (s3 analyzing) | -3.139 | 0.108 | 2 |
| 15% | s2,s3 (s1 pilot training) | -3.149 | 0.079 | 2 |
| 25% | s1,s2 (s3 analyzing) | -2.720 | 0.627 | 2 |
| 50% | s2,s3 (s1 pilot training) | -2.292 | 0.424 | 2 |

### 关键变化

- 新 baseline SD (1.5418) 是旧 SD (0.840) 的 **1.84x**，所以所有新 d 的绝对值约为旧值的 **55%**
- 新 baseline mean 从 -0.312 右移到 +0.262，分子也变大
- 所有 Δd 均为正值（+0.98 ~ +2.00），即新 d 绝对值一致缩小
- 所有新 d 仍为大效应量（|d| > 1.99），检测力充足
- 缺失数据：exp-llama-5pct-s3 和 exp-llama-25pct-s3 仍在 ANALYZING；15pct-s1 和 50pct-s1 正在 pilot 训练

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 96719,
  "duration_api_ms": 96984,
  "num_turns": 9,
  "stop_reason": "end_turn",
  "session_id": "9dd1310f-2eca-4936-af7c-90a1b8a75881",
  "total_cost_usd": 0.47387749999999995,
  "usage": {
    "input_tokens": 11,
    "cache_creation_input_tokens": 32446,
    "cache_read_input_tokens": 192534,
    "output_tokens": 6932,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 32446,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 972,
        "cache_read_input_tokens": 38643,
        "cache_creation_input_tokens": 5644,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 5644
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1358,
      "outputTokens": 22,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0014680000000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 11,
      "outputTokens": 6932,
      "cacheReadInputTokens": 192534,
      "cacheCreationInputTokens": 32446,
      "webSearchRequests": 0,
      "costUSD": 0.4724095,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "909e6005-cfb2-45d3-a693-a4863950cc4b"
}
```

</details>

---
