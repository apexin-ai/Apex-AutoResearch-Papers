# monitor stale experiments check 20260524T082347 retry1

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 72
- **Recorded user turns:** 0
- **Tool calls:** 26
- **Original source:** `logs/workers/worker_monitor_stale-experiments-check_20260524T082347_retry1.log`
- **Structured JSON:** [`a0ba82ec0a651cceadc0.json`](../../sessions/a0/a0ba82ec0a651cceadc0.json)

## Before a recorded user message

72 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement",
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
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
  "model": "claude-opus-4-7[1m]",
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
  "uuid": "1189bc25-0976-4aba-ae6a-81dd211934d1",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/memory/"
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
    "resetsAt": 1779628200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "ed3823df-1e1c-4312-af41-90812f3bca8f",
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "4282c281-7a9c-45e0-8165-a176fe2d8279",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01SWo1DjB5GB9RKjE8RhoCwy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 14666,
      "cache_read_input_tokens": 16241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14666
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

_source line 5_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01JsxuqNoH2zfSgnpjDh4DsG`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry",
  "max_results": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "739dc5c1-861f-4b00-817c-57175e6aa4fa",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01SWo1DjB5GB9RKjE8RhoCwy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 14666,
      "cache_read_input_tokens": 16241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14666
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

_source line 6 · 2026-05-24T08:24:09.174Z_

<details><summary>↩ Tool result · `toolu_01JsxuqNoH2zfSgnpjDh4DsG`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_registry"
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
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "61ca6f91-4a52-4ed9-b4a7-99f560181aa8",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__update_registry"
    ],
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry",
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

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "3d5bc7db-3bb7-4949-9a62-62f074f35ae0",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01RNzSCVNE8dqunaQMKKwjcF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 16731,
      "cache_read_input_tokens": 16334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16731
      },
      "output_tokens": 0,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "tools_changed",
        "cache_missed_input_tokens": 28661
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01Tgxwz4WSHDWdyTZMomBhZS`</summary>

```json
{
  "filters": {
    "exp_id": "eval-smolvla-lerobot-goal-seed43-v3"
  },
  "project": "acr-vla-conformal-refinement",
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
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "4d8fa364-7792-42de-8dda-c0dec9fc6430",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01RNzSCVNE8dqunaQMKKwjcF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 16731,
      "cache_read_input_tokens": 16334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16731
      },
      "output_tokens": 0,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "tools_changed",
        "cache_missed_input_tokens": 28661
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01D5qwaskxoYo6LcgtKPhoT9`</summary>

```json
{
  "filters": {
    "exp_id": "eval-smolvla-lerobot-spatial-seed43-v3"
  },
  "project": "acr-vla-conformal-refinement",
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
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "61011725-665e-4b7c-868a-c926e40c4ea0",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01RNzSCVNE8dqunaQMKKwjcF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 16731,
      "cache_read_input_tokens": 16334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16731
      },
      "output_tokens": 0,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "tools_changed",
        "cache_missed_input_tokens": 28661
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-24T08:24:15.829Z_

<details><summary>↩ Tool result · `toolu_01Tgxwz4WSHDWdyTZMomBhZS`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.2899}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "47980a6e-b84a-46e1-9116-fb2892f7cde5",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.2899}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.2899}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-24T08:24:17.800Z_

<details><summary>↩ Tool result · `toolu_01D5qwaskxoYo6LcgtKPhoT9`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.9565}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "61095f83-7bcf-47a1-847b-e0a590f7d4eb",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.9565}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.9565}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_019nZStHciitC7jKWKxwPSnz`</summary>

```json
{
  "filters": {
    "status": "RUNNING"
  },
  "project": "acr-vla-conformal-refinement",
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
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "dfe9cd3e-eeb9-4f13-bfc9-a1559d6d7208",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_015oykPbEcTbEDUoWJmVKFHG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 630,
      "cache_read_input_tokens": 33065,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 630
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

_source line 13 · 2026-05-24T08:24:24.298Z_

<details><summary>↩ Tool result · `toolu_019nZStHciitC7jKWKxwPSnz`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-supp-long-k2mean-s46\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T03:23:24.189Z\", \"updated_at\": \"2026-05-24T08:15:23.138Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark long --mode vla_only --baseline_mode mean --K 2 --seed 46 --n_rollouts 20 --output_file logs/eval_long_k2mean_seed46.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": 263191, \"log_path\": \"logs/eval_long_k2mean_seed46.json\", \"submitted_at\": \"2026-05-24T03:23:22.142Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 46, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"n/a-baseline\"}, \"hypothesis\": \"VLA-only K=2 mean baseline on LIBERO-Long suite seed46 provides the fifth seed for Long K2-mean variance analysis, establishing the unrefined baseline performance across seeds.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.55, \"successes\": 110, \"total\": 200, \"source\": \"json_harvest_bjb1-32546\"}}, \"eval-supp-long-crm-norm005-s46\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T00:55:34.833Z\", \"updated_at\": \"2026-05-24T08:15:19.358Z\", \"hypothesis\": \"CRM obs-only refinement with max_correction_norm=0.05 on LIBERO-Long suite seed46 provides the fifth seed for Long CRM obs-only variance analysis, testing conservative correction magnitude across seeds.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark long --mode crm_obs_only --seed 46 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": 262247, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-crm-norm005-s46.log\", \"submitted_at\": \"2026-05-24T03:23:09.570Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 46, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.54, \"successes\": 108, \"total\": 200, \"source\": \"json_harvest_bjb1-32546\"}}, \"eval-supp-long-reconvla-s46\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T00:55:40.981Z\", \"updated_at\": \"2026-05-24T08:06:46.631Z\", \"hypothesis\": \"ReconVLA evaluation on LIBERO-Long suite seed46 provides the fifth seed for Long ReconVLA variance analysis, measuring reconstruction-based refinement consistency across seeds.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark long --mode reconvla --seed 46 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": 262529, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-reconvla-s46.log\", \"submitted_at\": \"2026-05-24T03:23:15.265Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 46, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.56, \"successes\": 112, \"total\": 200, \"source\": \"json_harvest_bjb1-32546\"}}, \"eval-supp-k2mean-spatial-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:15:55.833Z\", \"updated_at\": \"2026-05-24T07:18:30.230Z\", \"hypothesis\": \"K=2 mean baseline on Spatial suite seed47. Sixth seed extending variance analysis. 5-seed mean ~80%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark spatial --mode vla_only --baseline_mode mean --K 2 --seed 47 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:3\"], \"tmux_session\": \"spatial-k2mean-s47\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"checkpoint_source\": \"n/a-baseline\"}}, \"eval-supp-reconvla-spatial-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:15:47.910Z\", \"updated_at\": \"2026-05-24T07:18:23.847Z\", \"hypothesis\": \"Reconvla K=10 on Spatial suite seed47. Sixth seed extending variance analysis. 5-seed mean ~80%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark spatial --mode reconvla --seed 47 --n_rollouts 20 --K 10\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:2\"], \"tmux_session\": \"spatial-reconvla-s47\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA+Reconvla\", \"seed\": 47, \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"checkpoint_source\": \"n/a-reconvla\"}}, \"eval-supp-adapt-tau025-spatial-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:15:43.884Z\", \"updated_at\": \"2026-05-24T07:18:17.441Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Spatial suite seed47. Sixth seed extending variance analysis. 5-seed mean ~80.5%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark spatial --mode adaptive_conformal_crm --seed 47 --n_rollouts 20 --K 10 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:1\"], \"tmux_session\": \"spatial-adapt-s47\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA+Adaptive CRM\", \"seed\": 47, \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\"}}, \"eval-supp-vla-only-spatial-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:15:40.347Z\", \"updated_at\": \"2026-05-24T07:18:10.979Z\", \"hypothesis\": \"VLA-only baseline on Spatial suite seed47. Sixth seed extending variance analysis. 5-seed mean ~78.7%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode vla_only --seed 47 --n_rollouts 20 --K 1\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:0\"], \"tmux_session\": \"spatial-vla-s47\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"checkpoint_source\": \"n/a-baseline\"}}, \"eval-supp-goal-vla-only-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:14:14.567Z\", \"updated_at\": \"2026-05-24T07:17:13.996Z\", \"hypothesis\": \"Goal s47 VLA-only (K=1) baseline to extend Goal seed coverage beyond s42-s46 for supplementary variance analysis.\", \"parent\": \"eval-supp-goal-vla-only-s46\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark goal --mode vla_only --seed 47 --n_rollouts 20 --K 1\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": 279117, \"tmux_session\": \"goal-vla-s47\", \"log_path\": \"logs/eval-supp-goal-vla-only-s47.log\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Goal\", \"checkpoint_source\": \"n/a-baseline\", \"checkpoint_path\": \"n/a-eval-only\"}}, \"eval-supp-long-vla-only-s47-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:14:04.522Z\", \"updated_at\": \"2026-05-24T07:17:06.584Z\", \"hypothesis\": \"Long s47 VLA-only (K=1) baseline to complete the Long s47 seed extension set. The existing eval-supp-long-vla-only-s47 is actually k2mean (K=2 mean), so this fills the true VLA-only gap.\", \"parent\": \"eval-supp-long-vla-only-s46\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark long --mode vla_only --seed 47 --n_rollouts 20 --K 1\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": 278846, \"tmux_session\": \"long-vla-s47-r2\", \"log_path\": \"logs/eval-supp-long-vla-only-s47-r2.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"n/a-baseline\", \"checkpoint_path\": \"n/a-eval-only\"}}, \"eval-supp-adapt-tau025-spatial-s46\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:12:18.821Z\", \"updated_at\": \"2026-05-24T07:16:50.821Z\", \"hypothesis\": \"CRM/Adaptive on Spatial seed46, 5th seed extension\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark spatial --mode adaptive_conformal_crm --seed 46 --n_rollouts 20 --K 10 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO spatial suite\", \"data_count\": 200, \"model_name\": \"SmolVLA + Adaptive CRM (crm_smolvla_3suite_v1)\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 20 rollouts\"}, \"failure_reason\": \"GPU 1 occupied by OpenVLA VLA-only eval (PID 114990). Not actually started despite RUNNING status. Will deploy when GPU frees up.\"}, \"eval-supp-crm-norm005-spatial-s46\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:12:15.210Z\", \"updated_at\": \"2026-05-24T07:14:47.458Z\", \"hypothesis\": \"CRM/Adaptive on Spatial seed46, 5th seed extension\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 46 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO spatial\", \"data_count\": 200, \"model_name\": \"smolvla+crm_smolvla_3suite_v1\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 20 rollouts\"}}, \"eval-openvla-object-vla-only-seed42-v3\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:07:37.003Z\", \"updated_at\": \"2026-05-24T07:08:07.984Z\", \"hypothesis\": \"After fixing OpenVLA loading for transformers 5.8.1 (model_type 'openvla' auto-registration via openvla_compat + PrismaticImageProcessor workaround), VLA-only baseline on LIBERO-Object seed42 should reproduce the previously observed ~69% success rate from eval-openvla-object-vla-only-seed42-v2. Validates that the new loader path preserves model behavior bit-for-bit.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u src/openvla_eval.py --benchmark object --model_path /root/autodl-tmp/models/openvla-libero-object --mode vla_only --seed 42 --n_rollouts 20 --gpu 0 --output_file logs/eval_openvla_object_vla_only_seed42_v3.json\", \"server\": \"bjb2-28827\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_object\", \"data_count\": 200, \"model_name\": \"openvla-libero-object\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/openvla-libero-object\", \"eval_data\": \"LIBERO-Object (10 tasks x 20 rollouts = 200 episodes)\", \"pid\": \"114984\", \"log_path\": \"/tmp/eval_openvla_vla_only_seed42_v3.log\", \"checkpoint_path\": \"/root/autodl-tmp/models/openvla-libero-object\"}}, \"eval-supp-long-vla-only-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:34:23.532Z\", \"updated_at\": \"2026-05-24T07:05:36.964Z\", \"hypothesis\": \"K=2 mean baseline on Long suite seed47 (NOT VLA-only — actual command uses --baseline_mode mean --K 2, output eval_long_k2mean_seed47.json). Misnamed at creation. Paired with Adapt-s47 for matched-seed comparison.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark long --mode vla_only --baseline_mode mean --K 2 --seed 47 --n_rollouts 20 --output_file logs/eval_long_k2mean_seed47.json\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:5\"], \"tmux_session\": \"long-vla-s47\", \"log_path\": \"logs/eval-supp-long-vla-only-s47.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"n/a-baseline\", \"parent\": \"eval-supp-long-vla-only-s46\"}}, \"eval-supp-long-crm-norm005-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:52:08.968Z\", \"updated_at\": \"2026-05-24T06:53:16.695Z\", \"hypothesis\": \"CRM obs-only norm=0.05 on Long suite seed47 (sixth seed extension). Pairs with running Long vla-only-s47 and adapt-s47 on cqa1-32758 to tighten Long suite CI which has highest variance.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark long --mode crm_obs_only --seed 47 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"tmux_session\": \"long-crm-s47\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-crm-norm005-s47.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\"}}, \"eval-supp-long-reconvla-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:52:05.630Z\", \"updated_at\": \"2026-05-24T06:53:02.593Z\", \"hypothesis\": \"Reconvla K=10 on Long suite seed47 (sixth seed extension). Pairs with running Long vla-only-s47 and adapt-s47 on cqa1-32758 to tighten Long suite CI which has highest variance.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark long --mode reconvla --seed 47 --n_rollouts 20 --K 10\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"tmux_session\": \"long-reconvla-s47\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-reconvla-s47.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"n/a-reconvla\"}}, \"eval-supp-spatial-crm-norm005-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:49:40.206Z\", \"updated_at\": \"2026-05-24T06:51:27.049Z\", \"hypothesis\": \"CRM obs_only norm=0.05 on LIBERO-Spatial seed47. Fifth seed extending Spatial CRM coverage (s43-s46 mean ~79.6%). Tightens CI for statistical comparison with VLA-only/K2mean/Reconvla/Adaptive at matched 5-seed coverage.\", \"parent\": \"eval-supp-spatial-crm-norm005-s46\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 47 --n_rollouts 20 --max_correction_norm 0.05 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_spatial_crm_obs_only_norm0.05_seed47.json\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"235730\", \"tmux_session\": \"eval-spatial-crm-s47\", \"log_path\": \"/tmp/eval_spatial_crm_s47.log\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA+CRM\", \"seed\": 47, \"eval_data\": \"LIBERO-Spatial\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"checkpoint_path\": \"n/a-eval-only\", \"submitted_at\": \"2026-05-24T06:50:07Z\", \"submitted_via\": \"ssh_execute_tmux\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-supp-vla-only-spatial-s46\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:48:57.955Z\", \"updated_at\": \"2026-05-24T06:50:52.276Z\", \"hypothesis\": \"VLA-only baseline on Spatial suite seed46. Extending from 3-seed (s42/s43/s44) to 5-seed for variance analysis. 3-seed mean 78.7%±0.3%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark spatial --mode vla_only --seed 46 --n_rollouts 20 --K 1\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/models/smolvla_libero/\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"benchmark\": \"spatial\", \"mode\": \"vla_only\", \"tmux_session\": \"eval-supp-vla-only-spatial-s46\", \"gpu\": 5}}, \"eval-supp-adapt-tau025-spatial-s45\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:48:54.415Z\", \"updated_at\": \"2026-05-24T06:50:44.120Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 (conformal_threshold) with max_correction_norm=0.2 on Spatial suite seed45. Extending from 3-seed (s42/s43/s44) to 5-seed for variance analysis. 3-seed mean 80.8%±1.1%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark spatial --mode adaptive_conformal_crm --seed 45 --n_rollouts 20 --K 10 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla+crm-adaptive\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"benchmark\": \"spatial\", \"mode\": \"adaptive_conformal_crm\", \"max_correction_norm\": 0.2, \"conformal_threshold\": 0.25, \"K\": 10, \"tmux_session\": \"eval-supp-adapt-tau025-spatial-s45\", \"gpu\": 4}}, \"eval-supp-crm-norm005-spatial-s45\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:48:50.955Z\", \"updated_at\": \"2026-05-24T06:50:37.107Z\", \"hypothesis\": \"CRM always-on norm=0.05 on Spatial suite seed45. Extending from 3-seed (s42/s43/s44) to 5-seed for variance analysis. 3-seed mean 79.8%±1.3%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 45 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla+crm\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"benchmark\": \"spatial\", \"mode\": \"crm_obs_only\", \"max_correction_norm\": 0.05, \"K\": 10, \"tmux_session\": \"eval-supp-crm-norm005-spatial-s45\", \"gpu\": 3}}, \"eval-supp-vla-only-spatial-s45\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:48:46.040Z\", \"updated_at\": \"2026-05-24T06:50:30.794Z\", \"hypothesis\": \"VLA-only baseline on Spatial suite seed45. Extending from 3-seed (s42/s43/s44) to 5-seed for variance analysis. 3-seed mean 78.7%±0.3%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark spatial --mode vla_only --seed 45 --n_rollouts 20 --K 1\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/models/smolvla_libero/\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"benchmark\": \"spatial\", \"mode\": \"vla_only\", \"tmux_session\": \"eval-supp-vla-only-spatial-s45\", \"gpu\": 2}}, \"eval-supp-long-adapt-tau025-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:34:20.287Z\", \"updated_at\": \"2026-05-24T06:38:39.651Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Long suite seed47 (sixth seed extension). Long is the highest-variance suite with smallest improvement margin (57.7 vs 58.0 VLA-only). Sixth seed tightens CI to determine if Adaptive is statistically equivalent to or below VLA-only on Long.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark long --mode adaptive_conformal_crm --seed 47 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --max_correction_norm 0.2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:4\"], \"tmux_session\": \"long-adapt-s47\", \"log_path\": \"logs/eval-supp-long-adapt-tau025-s47.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"parent\": \"eval-supp-long-adapt-tau025-s46-r2\"}}, \"precompute-pi05-long-2048-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:18:31.140Z\", \"updated_at\": \"2026-05-24T06:23:39.262Z\", \"hypothesis\": \"Precomputing π0.5 obs_features and K=2048 action samples on LIBERO-Long enables downstream CRM training for cross-model (SmolVLA→π0.5) generalization verification without re-running inference at train time.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 nohup python -u src/train_crm.py --precompute --model pi05 --benchmark long --K 10 --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/ > /root/autodl-tmp/logs/precompute_pi05_long_2048.log 2>&1 &\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": 114507, \"data_path\": \"/root/autodl-tmp/crm_cache_pi05_2048/long/\", \"data_count\": 136090, \"model_name\": \"pi0.5\", \"seed\": 0, \"log_path\": \"/root/autodl-tmp/logs/precompute_pi05_long_2048.log\"}}, \"precompute-pi05-object-2048-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:18:24.705Z\", \"updated_at\": \"2026-05-24T06:23:31.677Z\", \"hypothesis\": \"Precomputing π0.5 obs_features and K=2048 action samples on LIBERO-Object enables downstream CRM training for cross-model (SmolVLA→π0.5) generalization verification without re-running inference at train time.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 nohup python -u src/train_crm.py --precompute --model pi05 --benchmark object --K 10 --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/ > /root/autodl-tmp/logs/precompute_pi05_object_2048.log 2>&1 &\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": 113456, \"data_path\": \"/root/autodl-tmp/crm_cache_pi05_2048/object/\", \"data_count\": 72507, \"model_name\": \"pi0.5\", \"seed\": 0, \"log_path\": \"/root/autodl-tmp/logs/precompute_pi05_object_2048.log\"}}}, \"count\": 23, \"total\": 23, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.345}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "ec03da91-c79d-4759-9c10-f4d3f7f6d768",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"eval-supp-long-k2mean-s46\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T03:23:24.189Z\\\", \\\"updated_at\\\": \\\"2026-05-24T08:15:23.138Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --benchmark long --mode vla_only --baseline_mode mean --K 2 --seed 46 --n_rollouts 20 --output_file logs/eval_long_k2mean_seed46.json\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"pid\\\": 263191, \\\"log_path\\\": \\\"logs/eval_long_k2mean_seed46.json\\\", \\\"submitted_at\\\": \\\"2026-05-24T03:23:22.142Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"LIBERO-Long\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 46, \\\"eval_data\\\": \\\"LIBERO-Long\\\", \\\"checkpoint_source\\\": \\\"n/a-baseline\\\"}, \\\"hypothesis\\\": \\\"VLA-only K=2 mean baseline on LIBERO-Long suite seed46 provides the fifth seed for Long K2-mean variance analysis, establishing the unrefined baseline performance across seeds.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.55, \\\"successes\\\": 110, \\\"total\\\": 200, \\\"source\\\": \\\"json_harvest_bjb1-32546\\\"}}, \\\"eval-supp-long-crm-norm005-s46\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T00:55:34.833Z\\\", \\\"updated_at\\\": \\\"2026-05-24T08:15:19.358Z\\\", \\\"hypothesis\\\": \\\"CRM obs-only refinement with max_correction_norm=0.05 on LIBERO-Long suite seed46 provides the fifth seed for Long CRM obs-only variance analysis, testing conservative correction magnitude across seeds.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --benchmark long --mode crm_obs_only --seed 46 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": 262247, \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-supp-long-crm-norm005-s46.log\\\", \\\"submitted_at\\\": \\\"2026-05-24T03:23:09.570Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"LIBERO-Long\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 46, \\\"eval_data\\\": \\\"LIBERO-Long\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.54, \\\"successes\\\": 108, \\\"total\\\": 200, \\\"source\\\": \\\"json_harvest_bjb1-32546\\\"}}, \\\"eval-supp-long-reconvla-s46\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T00:55:40.981Z\\\", \\\"updated_at\\\": \\\"2026-05-24T08:06:46.631Z\\\", \\\"hypothesis\\\": \\\"ReconVLA evaluation on LIBERO-Long suite seed46 provides the fifth seed for Long ReconVLA variance analysis, measuring reconstruction-based refinement consistency across seeds.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --benchmark long --mode reconvla --seed 46 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"pid\\\": 262529, \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-supp-long-reconvla-s46.log\\\", \\\"submitted_at\\\": \\\"2026-05-24T03:23:15.265Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"LIBERO-Long\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 46, \\\"eval_data\\\": \\\"LIBERO-Long\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.56, \\\"successes\\\": 112, \\\"total\\\": 200, \\\"source\\\": \\\"json_harvest_bjb1-32546\\\"}}, \\\"eval-supp-k2mean-spatial-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T07:15:55.833Z\\\", \\\"updated_at\\\": \\\"2026-05-24T07:18:30.230Z\\\", \\\"hypothesis\\\": \\\"K=2 mean baseline on Spatial suite seed47. Sixth seed extending variance analysis. 5-seed mean ~80%.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark spatial --mode vla_only --baseline_mode mean --K 2 --seed 47 --n_rollouts 20\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"tmux_session\\\": \\\"spatial-k2mean-s47\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 47, \\\"eval_data\\\": \\\"LIBERO-Spatial 10 tasks x 20 rollouts\\\", \\\"checkpoint_source\\\": \\\"n/a-baseline\\\"}}, \\\"eval-supp-reconvla-spatial-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T07:15:47.910Z\\\", \\\"updated_at\\\": \\\"2026-05-24T07:18:23.847Z\\\", \\\"hypothesis\\\": \\\"Reconvla K=10 on Spatial suite seed47. Sixth seed extending variance analysis. 5-seed mean ~80%.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark spatial --mode reconvla --seed 47 --n_rollouts 20 --K 10\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"tmux_session\\\": \\\"spatial-reconvla-s47\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA+Reconvla\\\", \\\"seed\\\": 47, \\\"eval_data\\\": \\\"LIBERO-Spatial 10 tasks x 20 rollouts\\\", \\\"checkpoint_source\\\": \\\"n/a-reconvla\\\"}}, \\\"eval-supp-adapt-tau025-spatial-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T07:15:43.884Z\\\", \\\"updated_at\\\": \\\"2026-05-24T07:18:17.441Z\\\", \\\"hypothesis\\\": \\\"Adaptive CRM tau=0.25 on Spatial suite seed47. Sixth seed extending variance analysis. 5-seed mean ~80.5%.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark spatial --mode adaptive_conformal_crm --seed 47 --n_rollouts 20 --K 10 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"tmux_session\\\": \\\"spatial-adapt-s47\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA+Adaptive CRM\\\", \\\"seed\\\": 47, \\\"eval_data\\\": \\\"LIBERO-Spatial 10 tasks x 20 rollouts\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\"}}, \\\"eval-supp-vla-only-spatial-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T07:15:40.347Z\\\", \\\"updated_at\\\": \\\"2026-05-24T07:18:10.979Z\\\", \\\"hypothesis\\\": \\\"VLA-only baseline on Spatial suite seed47. Sixth seed extending variance analysis. 5-seed mean ~78.7%.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode vla_only --seed 47 --n_rollouts 20 --K 1\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"tmux_session\\\": \\\"spatial-vla-s47\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 47, \\\"eval_data\\\": \\\"LIBERO-Spatial 10 tasks x 20 rollouts\\\", \\\"checkpoint_source\\\": \\\"n/a-baseline\\\"}}, \\\"eval-supp-goal-vla-only-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T07:14:14.567Z\\\", \\\"updated_at\\\": \\\"2026-05-24T07:17:13.996Z\\\", \\\"hypothesis\\\": \\\"Goal s47 VLA-only (K=1) baseline to extend Goal seed coverage beyond s42-s46 for supplementary variance analysis.\\\", \\\"parent\\\": \\\"eval-supp-goal-vla-only-s46\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark goal --mode vla_only --seed 47 --n_rollouts 20 --K 1\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"pid\\\": 279117, \\\"tmux_session\\\": \\\"goal-vla-s47\\\", \\\"log_path\\\": \\\"logs/eval-supp-goal-vla-only-s47.log\\\", \\\"data_path\\\": \\\"LIBERO-Goal\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 47, \\\"eval_data\\\": \\\"LIBERO-Goal\\\", \\\"checkpoint_source\\\": \\\"n/a-baseline\\\", \\\"checkpoint_path\\\": \\\"n/a-eval-only\\\"}}, \\\"eval-supp-long-vla-only-s47-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T07:14:04.522Z\\\", \\\"updated_at\\\": \\\"2026-05-24T07:17:06.584Z\\\", \\\"hypothesis\\\": \\\"Long s47 VLA-only (K=1) baseline to complete the Long s47 seed extension set. The existing eval-supp-long-vla-only-s47 is actually k2mean (K=2 mean), so this fills the true VLA-only gap.\\\", \\\"parent\\\": \\\"eval-supp-long-vla-only-s46\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark long --mode vla_only --seed 47 --n_rollouts 20 --K 1\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": 278846, \\\"tmux_session\\\": \\\"long-vla-s47-r2\\\", \\\"log_path\\\": \\\"logs/eval-supp-long-vla-only-s47-r2.log\\\", \\\"data_path\\\": \\\"LIBERO-Long\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 47, \\\"eval_data\\\": \\\"LIBERO-Long\\\", \\\"checkpoint_source\\\": \\\"n/a-baseline\\\", \\\"checkpoint_path\\\": \\\"n/a-eval-only\\\"}}, \\\"eval-supp-adapt-tau025-spatial-s46\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T07:12:18.821Z\\\", \\\"updated_at\\\": \\\"2026-05-24T07:16:50.821Z\\\", \\\"hypothesis\\\": \\\"CRM/Adaptive on Spatial seed46, 5th seed extension\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark spatial --mode adaptive_conformal_crm --seed 46 --n_rollouts 20 --K 10 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"LIBERO spatial suite\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA + Adaptive CRM (crm_smolvla_3suite_v1)\\\", \\\"seed\\\": 46, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO spatial 10 tasks x 20 rollouts\\\"}, \\\"failure_reason\\\": \\\"GPU 1 occupied by OpenVLA VLA-only eval (PID 114990). Not actually started despite RUNNING status. Will deploy when GPU frees up.\\\"}, \\\"eval-supp-crm-norm005-spatial-s46\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T07:12:15.210Z\\\", \\\"updated_at\\\": \\\"2026-05-24T07:14:47.458Z\\\", \\\"hypothesis\\\": \\\"CRM/Adaptive on Spatial seed46, 5th seed extension\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 46 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"LIBERO spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"smolvla+crm_smolvla_3suite_v1\\\", \\\"seed\\\": 46, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO spatial 10 tasks x 20 rollouts\\\"}}, \\\"eval-openvla-object-vla-only-seed42-v3\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T07:07:37.003Z\\\", \\\"updated_at\\\": \\\"2026-05-24T07:08:07.984Z\\\", \\\"hypothesis\\\": \\\"After fixing OpenVLA loading for transformers 5.8.1 (model_type 'openvla' auto-registration via openvla_compat + PrismaticImageProcessor workaround), VLA-only baseline on LIBERO-Object seed42 should reproduce the previously observed ~69% success rate from eval-openvla-object-vla-only-seed42-v2. Validates that the new loader path preserves model behavior bit-for-bit.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u src/openvla_eval.py --benchmark object --model_path /root/autodl-tmp/models/openvla-libero-object --mode vla_only --seed 42 --n_rollouts 20 --gpu 0 --output_file logs/eval_openvla_object_vla_only_seed42_v3.json\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/libero_data/libero_object\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"openvla-libero-object\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/models/openvla-libero-object\\\", \\\"eval_data\\\": \\\"LIBERO-Object (10 tasks x 20 rollouts = 200 episodes)\\\", \\\"pid\\\": \\\"114984\\\", \\\"log_path\\\": \\\"/tmp/eval_openvla_vla_only_seed42_v3.log\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/models/openvla-libero-object\\\"}}, \\\"eval-supp-long-vla-only-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T06:34:23.532Z\\\", \\\"updated_at\\\": \\\"2026-05-24T07:05:36.964Z\\\", \\\"hypothesis\\\": \\\"K=2 mean baseline on Long suite seed47 (NOT VLA-only — actual command uses --baseline_mode mean --K 2, output eval_long_k2mean_seed47.json). Misnamed at creation. Paired with Adapt-s47 for matched-seed comparison.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark long --mode vla_only --baseline_mode mean --K 2 --seed 47 --n_rollouts 20 --output_file logs/eval_long_k2mean_seed47.json\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"gpu\\\": [\\\"cuda:5\\\"], \\\"tmux_session\\\": \\\"long-vla-s47\\\", \\\"log_path\\\": \\\"logs/eval-supp-long-vla-only-s47.log\\\", \\\"data_path\\\": \\\"LIBERO-Long\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 47, \\\"eval_data\\\": \\\"LIBERO-Long\\\", \\\"checkpoint_source\\\": \\\"n/a-baseline\\\", \\\"parent\\\": \\\"eval-supp-long-vla-only-s46\\\"}}, \\\"eval-supp-long-crm-norm005-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T06:52:08.968Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:53:16.695Z\\\", \\\"hypothesis\\\": \\\"CRM obs-only norm=0.05 on Long suite seed47 (sixth seed extension). Pairs with running Long vla-only-s47 and adapt-s47 on cqa1-32758 to tighten Long suite CI which has highest variance.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark long --mode crm_obs_only --seed 47 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:5\\\"], \\\"tmux_session\\\": \\\"long-crm-s47\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-supp-long-crm-norm005-s47.log\\\", \\\"data_path\\\": \\\"LIBERO-Long\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 47, \\\"eval_data\\\": \\\"LIBERO-Long\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\\\"}}, \\\"eval-supp-long-reconvla-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T06:52:05.630Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:53:02.593Z\\\", \\\"hypothesis\\\": \\\"Reconvla K=10 on Long suite seed47 (sixth seed extension). Pairs with running Long vla-only-s47 and adapt-s47 on cqa1-32758 to tighten Long suite CI which has highest variance.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark long --mode reconvla --seed 47 --n_rollouts 20 --K 10\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:4\\\"], \\\"tmux_session\\\": \\\"long-reconvla-s47\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-supp-long-reconvla-s47.log\\\", \\\"data_path\\\": \\\"LIBERO-Long\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 47, \\\"eval_data\\\": \\\"LIBERO-Long\\\", \\\"checkpoint_source\\\": \\\"n/a-reconvla\\\"}}, \\\"eval-supp-spatial-crm-norm005-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T06:49:40.206Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:51:27.049Z\\\", \\\"hypothesis\\\": \\\"CRM obs_only norm=0.05 on LIBERO-Spatial seed47. Fifth seed extending Spatial CRM coverage (s43-s46 mean ~79.6%). Tightens CI for statistical comparison with VLA-only/K2mean/Reconvla/Adaptive at matched 5-seed coverage.\\\", \\\"parent\\\": \\\"eval-supp-spatial-crm-norm005-s46\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 47 --n_rollouts 20 --max_correction_norm 0.05 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_spatial_crm_obs_only_norm0.05_seed47.json\\\", \\\"server\\\": \\\"bjb2-40593\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"235730\\\", \\\"tmux_session\\\": \\\"eval-spatial-crm-s47\\\", \\\"log_path\\\": \\\"/tmp/eval_spatial_crm_s47.log\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA+CRM\\\", \\\"seed\\\": 47, \\\"eval_data\\\": \\\"LIBERO-Spatial\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"checkpoint_path\\\": \\\"n/a-eval-only\\\", \\\"submitted_at\\\": \\\"2026-05-24T06:50:07Z\\\", \\\"submitted_via\\\": \\\"ssh_execute_tmux\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}}, \\\"eval-supp-vla-only-spatial-s46\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T06:48:57.955Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:50:52.276Z\\\", \\\"hypothesis\\\": \\\"VLA-only baseline on Spatial suite seed46. Extending from 3-seed (s42/s43/s44) to 5-seed for variance analysis. 3-seed mean 78.7%±0.3%.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark spatial --mode vla_only --seed 46 --n_rollouts 20 --K 1\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 46, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/models/smolvla_libero/\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial 10 tasks x 20 rollouts\\\", \\\"benchmark\\\": \\\"spatial\\\", \\\"mode\\\": \\\"vla_only\\\", \\\"tmux_session\\\": \\\"eval-supp-vla-only-spatial-s46\\\", \\\"gpu\\\": 5}}, \\\"eval-supp-adapt-tau025-spatial-s45\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T06:48:54.415Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:50:44.120Z\\\", \\\"hypothesis\\\": \\\"Adaptive CRM tau=0.25 (conformal_threshold) with max_correction_norm=0.2 on Spatial suite seed45. Extending from 3-seed (s42/s43/s44) to 5-seed for variance analysis. 3-seed mean 80.8%±1.1%.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark spatial --mode adaptive_conformal_crm --seed 45 --n_rollouts 20 --K 10 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"smolvla+crm-adaptive\\\", \\\"seed\\\": 45, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial 10 tasks x 20 rollouts\\\", \\\"benchmark\\\": \\\"spatial\\\", \\\"mode\\\": \\\"adaptive_conformal_crm\\\", \\\"max_correction_norm\\\": 0.2, \\\"conformal_threshold\\\": 0.25, \\\"K\\\": 10, \\\"tmux_session\\\": \\\"eval-supp-adapt-tau025-spatial-s45\\\", \\\"gpu\\\": 4}}, \\\"eval-supp-crm-norm005-spatial-s45\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T06:48:50.955Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:50:37.107Z\\\", \\\"hypothesis\\\": \\\"CRM always-on norm=0.05 on Spatial suite seed45. Extending from 3-seed (s42/s43/s44) to 5-seed for variance analysis. 3-seed mean 79.8%±1.3%.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 45 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"smolvla+crm\\\", \\\"seed\\\": 45, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial 10 tasks x 20 rollouts\\\", \\\"benchmark\\\": \\\"spatial\\\", \\\"mode\\\": \\\"crm_obs_only\\\", \\\"max_correction_norm\\\": 0.05, \\\"K\\\": 10, \\\"tmux_session\\\": \\\"eval-supp-crm-norm005-spatial-s45\\\", \\\"gpu\\\": 3}}, \\\"eval-supp-vla-only-spatial-s45\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T06:48:46.040Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:50:30.794Z\\\", \\\"hypothesis\\\": \\\"VLA-only baseline on Spatial suite seed45. Extending from 3-seed (s42/s43/s44) to 5-seed for variance analysis. 3-seed mean 78.7%±0.3%.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark spatial --mode vla_only --seed 45 --n_rollouts 20 --K 1\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 45, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/models/smolvla_libero/\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial 10 tasks x 20 rollouts\\\", \\\"benchmark\\\": \\\"spatial\\\", \\\"mode\\\": \\\"vla_only\\\", \\\"tmux_session\\\": \\\"eval-supp-vla-only-spatial-s45\\\", \\\"gpu\\\": 2}}, \\\"eval-supp-long-adapt-tau025-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T06:34:20.287Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:38:39.651Z\\\", \\\"hypothesis\\\": \\\"Adaptive CRM tau=0.25 on Long suite seed47 (sixth seed extension). Long is the highest-variance suite with smallest improvement margin (57.7 vs 58.0 VLA-only). Sixth seed tightens CI to determine if Adaptive is statistically equivalent to or below VLA-only on Long.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark long --mode adaptive_conformal_crm --seed 47 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --max_correction_norm 0.2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"gpu\\\": [\\\"cuda:4\\\"], \\\"tmux_session\\\": \\\"long-adapt-s47\\\", \\\"log_path\\\": \\\"logs/eval-supp-long-adapt-tau025-s47.log\\\", \\\"data_path\\\": \\\"LIBERO-Long\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 47, \\\"eval_data\\\": \\\"LIBERO-Long\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\\\", \\\"parent\\\": \\\"eval-supp-long-adapt-tau025-s46-r2\\\"}}, \\\"precompute-pi05-long-2048-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T06:18:31.140Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:23:39.262Z\\\", \\\"hypothesis\\\": \\\"Precomputing π0.5 obs_features and K=2048 action samples on LIBERO-Long enables downstream CRM training for cross-model (SmolVLA→π0.5) generalization verification without re-running inference at train time.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=3 nohup python -u src/train_crm.py --precompute --model pi05 --benchmark long --K 10 --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/ > /root/autodl-tmp/logs/precompute_pi05_long_2048.log 2>&1 &\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"pid\\\": 114507, \\\"data_path\\\": \\\"/root/autodl-tmp/crm_cache_pi05_2048/long/\\\", \\\"data_count\\\": 136090, \\\"model_name\\\": \\\"pi0.5\\\", \\\"seed\\\": 0, \\\"log_path\\\": \\\"/root/autodl-tmp/logs/precompute_pi05_long_2048.log\\\"}}, \\\"precompute-pi05-object-2048-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T06:18:24.705Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:23:31.677Z\\\", \\\"hypothesis\\\": \\\"Precomputing π0.5 obs_features and K=2048 action samples on LIBERO-Object enables downstream CRM training for cross-model (SmolVLA→π0.5) generalization verification without re-running inference at train time.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 nohup python -u src/train_crm.py --precompute --model pi05 --benchmark object --K 10 --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/ > /root/autodl-tmp/logs/precompute_pi05_object_2048.log 2>&1 &\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": 113456, \\\"data_path\\\": \\\"/root/autodl-tmp/crm_cache_pi05_2048/object/\\\", \\\"data_count\\\": 72507, \\\"model_name\\\": \\\"pi0.5\\\", \\\"seed\\\": 0, \\\"log_path\\\": \\\"/root/autodl-tmp/logs/precompute_pi05_object_2048.log\\\"}}}, \\\"count\\\": 23, \\\"total\\\": 23, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 3.345}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval-supp-long-k2mean-s46\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T03:23:24.189Z\", \"updated_at\": \"2026-05-24T08:15:23.138Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark long --mode vla_only --baseline_mode mean --K 2 --seed 46 --n_rollouts 20 --output_file logs/eval_long_k2mean_seed46.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": 263191, \"log_path\": \"logs/eval_long_k2mean_seed46.json\", \"submitted_at\": \"2026-05-24T03:23:22.142Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 46, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"n/a-baseline\"}, \"hypothesis\": \"VLA-only K=2 mean baseline on LIBERO-Long suite seed46 provides the fifth seed for Long K2-mean variance analysis, establishing the unrefined baseline performance across seeds.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.55, \"successes\": 110, \"total\": 200, \"source\": \"json_harvest_bjb1-32546\"}}, \"eval-supp-long-crm-norm005-s46\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T00:55:34.833Z\", \"updated_at\": \"2026-05-24T08:15:19.358Z\", \"hypothesis\": \"CRM obs-only refinement with max_correction_norm=0.05 on LIBERO-Long suite seed46 provides the fifth seed for Long CRM obs-only variance analysis, testing conservative correction magnitude across seeds.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark long --mode crm_obs_only --seed 46 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": 262247, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-crm-norm005-s46.log\", \"submitted_at\": \"2026-05-24T03:23:09.570Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 46, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.54, \"successes\": 108, \"total\": 200, \"source\": \"json_harvest_bjb1-32546\"}}, \"eval-supp-long-reconvla-s46\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T00:55:40.981Z\", \"updated_at\": \"2026-05-24T08:06:46.631Z\", \"hypothesis\": \"ReconVLA evaluation on LIBERO-Long suite seed46 provides the fifth seed for Long ReconVLA variance analysis, measuring reconstruction-based refinement consistency across seeds.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark long --mode reconvla --seed 46 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": 262529, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-reconvla-s46.log\", \"submitted_at\": \"2026-05-24T03:23:15.265Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 46, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.56, \"successes\": 112, \"total\": 200, \"source\": \"json_harvest_bjb1-32546\"}}, \"eval-supp-k2mean-spatial-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:15:55.833Z\", \"updated_at\": \"2026-05-24T07:18:30.230Z\", \"hypothesis\": \"K=2 mean baseline on Spatial suite seed47. Sixth seed extending variance analysis. 5-seed mean ~80%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark spatial --mode vla_only --baseline_mode mean --K 2 --seed 47 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:3\"], \"tmux_session\": \"spatial-k2mean-s47\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"checkpoint_source\": \"n/a-baseline\"}}, \"eval-supp-reconvla-spatial-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:15:47.910Z\", \"updated_at\": \"2026-05-24T07:18:23.847Z\", \"hypothesis\": \"Reconvla K=10 on Spatial suite seed47. Sixth seed extending variance analysis. 5-seed mean ~80%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark spatial --mode reconvla --seed 47 --n_rollouts 20 --K 10\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:2\"], \"tmux_session\": \"spatial-reconvla-s47\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA+Reconvla\", \"seed\": 47, \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"checkpoint_source\": \"n/a-reconvla\"}}, \"eval-supp-adapt-tau025-spatial-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:15:43.884Z\", \"updated_at\": \"2026-05-24T07:18:17.441Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Spatial suite seed47. Sixth seed extending variance analysis. 5-seed mean ~80.5%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark spatial --mode adaptive_conformal_crm --seed 47 --n_rollouts 20 --K 10 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:1\"], \"tmux_session\": \"spatial-adapt-s47\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA+Adaptive CRM\", \"seed\": 47, \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\"}}, \"eval-supp-vla-only-spatial-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:15:40.347Z\", \"updated_at\": \"2026-05-24T07:18:10.979Z\", \"hypothesis\": \"VLA-only baseline on Spatial suite seed47. Sixth seed extending variance analysis. 5-seed mean ~78.7%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode vla_only --seed 47 --n_rollouts 20 --K 1\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:0\"], \"tmux_session\": \"spatial-vla-s47\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"checkpoint_source\": \"n/a-baseline\"}}, \"eval-supp-goal-vla-only-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:14:14.567Z\", \"updated_at\": \"2026-05-24T07:17:13.996Z\", \"hypothesis\": \"Goal s47 VLA-only (K=1) baseline to extend Goal seed coverage beyond s42-s46 for supplementary variance analysis.\", \"parent\": \"eval-supp-goal-vla-only-s46\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark goal --mode vla_only --seed 47 --n_rollouts 20 --K 1\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": 279117, \"tmux_session\": \"goal-vla-s47\", \"log_path\": \"logs/eval-supp-goal-vla-only-s47.log\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Goal\", \"checkpoint_source\": \"n/a-baseline\", \"checkpoint_path\": \"n/a-eval-only\"}}, \"eval-supp-long-vla-only-s47-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:14:04.522Z\", \"updated_at\": \"2026-05-24T07:17:06.584Z\", \"hypothesis\": \"Long s47 VLA-only (K=1) baseline to complete the Long s47 seed extension set. The existing eval-supp-long-vla-only-s47 is actually k2mean (K=2 mean), so this fills the true VLA-only gap.\", \"parent\": \"eval-supp-long-vla-only-s46\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark long --mode vla_only --seed 47 --n_rollouts 20 --K 1\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": 278846, \"tmux_session\": \"long-vla-s47-r2\", \"log_path\": \"logs/eval-supp-long-vla-only-s47-r2.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"n/a-baseline\", \"checkpoint_path\": \"n/a-eval-only\"}}, \"eval-supp-adapt-tau025-spatial-s46\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:12:18.821Z\", \"updated_at\": \"2026-05-24T07:16:50.821Z\", \"hypothesis\": \"CRM/Adaptive on Spatial seed46, 5th seed extension\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark spatial --mode adaptive_conformal_crm --seed 46 --n_rollouts 20 --K 10 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO spatial suite\", \"data_count\": 200, \"model_name\": \"SmolVLA + Adaptive CRM (crm_smolvla_3suite_v1)\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 20 rollouts\"}, \"failure_reason\": \"GPU 1 occupied by OpenVLA VLA-only eval (PID 114990). Not actually started despite RUNNING status. Will deploy when GPU frees up.\"}, \"eval-supp-crm-norm005-spatial-s46\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:12:15.210Z\", \"updated_at\": \"2026-05-24T07:14:47.458Z\", \"hypothesis\": \"CRM/Adaptive on Spatial seed46, 5th seed extension\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 46 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO spatial\", \"data_count\": 200, \"model_name\": \"smolvla+crm_smolvla_3suite_v1\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 20 rollouts\"}}, \"eval-openvla-object-vla-only-seed42-v3\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:07:37.003Z\", \"updated_at\": \"2026-05-24T07:08:07.984Z\", \"hypothesis\": \"After fixing OpenVLA loading for transformers 5.8.1 (model_type 'openvla' auto-registration via openvla_compat + PrismaticImageProcessor workaround), VLA-only baseline on LIBERO-Object seed42 should reproduce the previously observed ~69% success rate from eval-openvla-object-vla-only-seed42-v2. Validates that the new loader path preserves model behavior bit-for-bit.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u src/openvla_eval.py --benchmark object --model_path /root/autodl-tmp/models/openvla-libero-object --mode vla_only --seed 42 --n_rollouts 20 --gpu 0 --output_file logs/eval_openvla_object_vla_only_seed42_v3.json\", \"server\": \"bjb2-28827\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_object\", \"data_count\": 200, \"model_name\": \"openvla-libero-object\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/openvla-libero-object\", \"eval_data\": \"LIBERO-Object (10 tasks x 20 rollouts = 200 episodes)\", \"pid\": \"114984\", \"log_path\": \"/tmp/eval_openvla_vla_only_seed42_v3.log\", \"checkpoint_path\": \"/root/autodl-tmp/models/openvla-libero-object\"}}, \"eval-supp-long-vla-only-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:34:23.532Z\", \"updated_at\": \"2026-05-24T07:05:36.964Z\", \"hypothesis\": \"K=2 mean baseline on Long suite seed47 (NOT VLA-only — actual command uses --baseline_mode mean --K 2, output eval_long_k2mean_seed47.json). Misnamed at creation. Paired with Adapt-s47 for matched-seed comparison.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark long --mode vla_only --baseline_mode mean --K 2 --seed 47 --n_rollouts 20 --output_file logs/eval_long_k2mean_seed47.json\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:5\"], \"tmux_session\": \"long-vla-s47\", \"log_path\": \"logs/eval-supp-long-vla-only-s47.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"n/a-baseline\", \"parent\": \"eval-supp-long-vla-only-s46\"}}, \"eval-supp-long-crm-norm005-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:52:08.968Z\", \"updated_at\": \"2026-05-24T06:53:16.695Z\", \"hypothesis\": \"CRM obs-only norm=0.05 on Long suite seed47 (sixth seed extension). Pairs with running Long vla-only-s47 and adapt-s47 on cqa1-32758 to tighten Long suite CI which has highest variance.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark long --mode crm_obs_only --seed 47 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"tmux_session\": \"long-crm-s47\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-crm-norm005-s47.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\"}}, \"eval-supp-long-reconvla-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:52:05.630Z\", \"updated_at\": \"2026-05-24T06:53:02.593Z\", \"hypothesis\": \"Reconvla K=10 on Long suite seed47 (sixth seed extension). Pairs with running Long vla-only-s47 and adapt-s47 on cqa1-32758 to tighten Long suite CI which has highest variance.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark long --mode reconvla --seed 47 --n_rollouts 20 --K 10\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"tmux_session\": \"long-reconvla-s47\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-reconvla-s47.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"n/a-reconvla\"}}, \"eval-supp-spatial-crm-norm005-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:49:40.206Z\", \"updated_at\": \"2026-05-24T06:51:27.049Z\", \"hypothesis\": \"CRM obs_only norm=0.05 on LIBERO-Spatial seed47. Fifth seed extending Spatial CRM coverage (s43-s46 mean ~79.6%). Tightens CI for statistical comparison with VLA-only/K2mean/Reconvla/Adaptive at matched 5-seed coverage.\", \"parent\": \"eval-supp-spatial-crm-norm005-s46\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 47 --n_rollouts 20 --max_correction_norm 0.05 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_spatial_crm_obs_only_norm0.05_seed47.json\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"235730\", \"tmux_session\": \"eval-spatial-crm-s47\", \"log_path\": \"/tmp/eval_spatial_crm_s47.log\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA+CRM\", \"seed\": 47, \"eval_data\": \"LIBERO-Spatial\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"checkpoint_path\": \"n/a-eval-only\", \"submitted_at\": \"2026-05-24T06:50:07Z\", \"submitted_via\": \"ssh_execute_tmux\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-supp-vla-only-spatial-s46\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:48:57.955Z\", \"updated_at\": \"2026-05-24T06:50:52.276Z\", \"hypothesis\": \"VLA-only baseline on Spatial suite seed46. Extending from 3-seed (s42/s43/s44) to 5-seed for variance analysis. 3-seed mean 78.7%±0.3%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark spatial --mode vla_only --seed 46 --n_rollouts 20 --K 1\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/models/smolvla_libero/\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"benchmark\": \"spatial\", \"mode\": \"vla_only\", \"tmux_session\": \"eval-supp-vla-only-spatial-s46\", \"gpu\": 5}}, \"eval-supp-adapt-tau025-spatial-s45\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:48:54.415Z\", \"updated_at\": \"2026-05-24T06:50:44.120Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 (conformal_threshold) with max_correction_norm=0.2 on Spatial suite seed45. Extending from 3-seed (s42/s43/s44) to 5-seed for variance analysis. 3-seed mean 80.8%±1.1%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark spatial --mode adaptive_conformal_crm --seed 45 --n_rollouts 20 --K 10 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla+crm-adaptive\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"benchmark\": \"spatial\", \"mode\": \"adaptive_conformal_crm\", \"max_correction_norm\": 0.2, \"conformal_threshold\": 0.25, \"K\": 10, \"tmux_session\": \"eval-supp-adapt-tau025-spatial-s45\", \"gpu\": 4}}, \"eval-supp-crm-norm005-spatial-s45\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:48:50.955Z\", \"updated_at\": \"2026-05-24T06:50:37.107Z\", \"hypothesis\": \"CRM always-on norm=0.05 on Spatial suite seed45. Extending from 3-seed (s42/s43/s44) to 5-seed for variance analysis. 3-seed mean 79.8%±1.3%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 45 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla+crm\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"benchmark\": \"spatial\", \"mode\": \"crm_obs_only\", \"max_correction_norm\": 0.05, \"K\": 10, \"tmux_session\": \"eval-supp-crm-norm005-spatial-s45\", \"gpu\": 3}}, \"eval-supp-vla-only-spatial-s45\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:48:46.040Z\", \"updated_at\": \"2026-05-24T06:50:30.794Z\", \"hypothesis\": \"VLA-only baseline on Spatial suite seed45. Extending from 3-seed (s42/s43/s44) to 5-seed for variance analysis. 3-seed mean 78.7%±0.3%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark spatial --mode vla_only --seed 45 --n_rollouts 20 --K 1\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/models/smolvla_libero/\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"benchmark\": \"spatial\", \"mode\": \"vla_only\", \"tmux_session\": \"eval-supp-vla-only-spatial-s45\", \"gpu\": 2}}, \"eval-supp-long-adapt-tau025-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:34:20.287Z\", \"updated_at\": \"2026-05-24T06:38:39.651Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Long suite seed47 (sixth seed extension). Long is the highest-variance suite with smallest improvement margin (57.7 vs 58.0 VLA-only). Sixth seed tightens CI to determine if Adaptive is statistically equivalent to or below VLA-only on Long.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark long --mode adaptive_conformal_crm --seed 47 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --max_correction_norm 0.2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:4\"], \"tmux_session\": \"long-adapt-s47\", \"log_path\": \"logs/eval-supp-long-adapt-tau025-s47.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"parent\": \"eval-supp-long-adapt-tau025-s46-r2\"}}, \"precompute-pi05-long-2048-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:18:31.140Z\", \"updated_at\": \"2026-05-24T06:23:39.262Z\", \"hypothesis\": \"Precomputing π0.5 obs_features and K=2048 action samples on LIBERO-Long enables downstream CRM training for cross-model (SmolVLA→π0.5) generalization verification without re-running inference at train time.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 nohup python -u src/train_crm.py --precompute --model pi05 --benchmark long --K 10 --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/ > /root/autodl-tmp/logs/precompute_pi05_long_2048.log 2>&1 &\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": 114507, \"data_path\": \"/root/autodl-tmp/crm_cache_pi05_2048/long/\", \"data_count\": 136090, \"model_name\": \"pi0.5\", \"seed\": 0, \"log_path\": \"/root/autodl-tmp/logs/precompute_pi05_long_2048.log\"}}, \"precompute-pi05-object-2048-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:18:24.705Z\", \"updated_at\": \"2026-05-24T06:23:31.677Z\", \"hypothesis\": \"Precomputing π0.5 obs_features and K=2048 action samples on LIBERO-Object enables downstream CRM training for cross-model (SmolVLA→π0.5) generalization verification without re-running inference at train time.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 nohup python -u src/train_crm.py --precompute --model pi05 --benchmark object --K 10 --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/ > /root/autodl-tmp/logs/precompute_pi05_object_2048.log 2>&1 &\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": 113456, \"data_path\": \"/root/autodl-tmp/crm_cache_pi05_2048/object/\", \"data_count\": 72507, \"model_name\": \"pi0.5\", \"seed\": 0, \"log_path\": \"/root/autodl-tmp/logs/precompute_pi05_object_2048.log\"}}}, \"count\": 23, \"total\": 23, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.345}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 14_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "fd275c14-121a-42e8-ae8e-e93d5d331b43",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01PGmuZtjMMwwraWCukdDD86",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12929,
      "cache_read_input_tokens": 33695,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12929
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

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01NNJxBAqgZ8XR6gEkRvMzD2`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "fields": [
    "exp_id",
    "status",
    "updated_at"
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
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "8a5d3091-5fa5-45ef-adc6-9d78e1612115",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01PGmuZtjMMwwraWCukdDD86",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12929,
      "cache_read_input_tokens": 33695,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12929
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

_source line 16 · 2026-05-24T08:24:32.774Z_

<details><summary>↩ Tool result · `toolu_01NNJxBAqgZ8XR6gEkRvMzD2`</summary>

```text
Error: result (94,907 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/7b80dd05-6aec-4cda-b61a-b5ef1300a0d5/tool-results/mcp-agent-ml-research-read_registry-1779611072759.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/7b80dd05-6aec-4cda-b61a-b5ef1300a0d5/tool-results/mcp-agent-ml-research-read_registry-1779611072759.txt in sequential chunks until 100% of the content has been read.
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
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "365e0fc0-cc9f-47af-9858-8acd2b10cd72",
  "tool_use_result": {
    "content": "Error: result (94,907 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/7b80dd05-6aec-4cda-b61a-b5ef1300a0d5/tool-results/mcp-agent-ml-research-read_registry-1779611072759.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/7b80dd05-6aec-4cda-b61a-b5ef1300a0d5/tool-results/mcp-agent-ml-research-read_registry-1779611072759.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval-supp-long-k2mean-s46\": {\"status\": \"RUNNING\", \"updated_at\": \"2026-05-24T08:15:23.138Z\"}, \"eval-supp-long-crm-norm005-s46\": {\"status\": \"RUNNING\", \"updated_at\": \"2026-05-24T08:15:19.358Z\"}, \"eval-supp-long-reconvla-s46\": {\"status\": \"RUNNING\", \"updated_at\": \"2026-05-24T08:06:46.631Z\"}, \"eval-supp-long-adapt-tau025-s46\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T08:05:01.126Z\"}, \"eval-supp-k2mean-spatial-s47\": {\"status\": \"RUNNING\", \"updated_at\": \"2026-05-24T07:18:30.230Z\"}, \"eval-supp-reconvla-spatial-s47\": {\"status\": \"RUNNING\", \"updated_at\": \"2026-05-24T07:18:23.847Z\"}, \"eval-supp-adapt-tau025-spatial-s47\": {\"status\": \"RUNNING\", \"updated_at\": \"2026-05-24T07:18:17.441Z\"}, \"eval-supp-vla-only-spatial-s47\": {\"status\": \"RUNNING\", \"updated_at\": \"2026-05-24T07:18:10.979Z\"}, \"eval-supp-goal-vla-only-s47\": {\"status\": \"RUNNING\", \"updated_at\": \"2026-05-24T07:17:13.996Z\"}, \"eval-supp-long-vla-only-s47-r2\": {\"status\": \"RUNNING\", \"updated_at\": \"2026-05-24T07:17:06.584Z\"}, \"eval-supp-adapt-tau025-spatial-s46\": {\"status\": \"RUNNING\", \"updated_at\": \"2026-05-24T07:16:50.821Z\"}, \"eval-supp-crm-norm005-spatial-s46\": {\"status\": \"RUNNING\", \"updated_at\": \"2026-05-24T07:14:47.458Z\"}, \"crm-train-openvla-k1-multiscale-object\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T07:09:37.983Z\"}, \"eval-openvla-object-vla-only-seed42-v3\": {\"status\": \"RUNNING\", \"updated_at\": \"2026-05-24T07:08:07.984Z\"}, \"eval-supp-long-k2mean-s46-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T07:06:31.785Z\"}, \"eval-supp-long-reconvla-s46-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T07:06:23.946Z\"}, \"eval-supp-long-crm-norm005-s46-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T07:06:15.932Z\"}, \"eval-supp-long-adapt-tau025-s46-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T07:06:09.666Z\"}, \"eval-supp-long-vla-only-s47\": {\"status\": \"RUNNING\", \"updated_at\": \"2026-05-24T07:05:36.964Z\"}, \"eval-supp-obj-crm-norm005-s45\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T06:55:16.446Z\"}, \"eval-supp-long-crm-norm005-s47\": {\"status\": \"RUNNING\", \"updated_at\": \"2026-05-24T06:53:16.695Z\"}, \"eval-supp-long-reconvla-s47\": {\"status\": \"RUNNING\", \"updated_at\": \"2026-05-24T06:53:02.593Z\"}, \"eval-supp-spatial-crm-norm005-s47\": {\"status\": \"RUNNING\", \"updated_at\": \"2026-05-24T06:51:27.049Z\"}, \"eval-supp-vla-only-spatial-s46\": {\"status\": \"RUNNING\", \"updated_at\": \"2026-05-24T06:50:52.276Z\"}, \"eval-supp-adapt-tau025-spatial-s45\": {\"status\": \"RUNNING\", \"updated_at\": \"2026-05-24T06:50:44.120Z\"}, \"eval-supp-crm-norm005-spatial-s45\": {\"status\": \"RUNNING\", \"updated_at\": \"2026-05-24T06:50:37.107Z\"}, \"eval-supp-vla-only-spatial-s45\": {\"status\": \"RUNNING\", \"updated_at\": \"2026-05-24T06:50:30.794Z\"}, \"eval-supp-obj-adapt-tau025-s45\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T06:49:49.091Z\"}, \"eval-supp-obj-vla-only-s45\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T06:49:36.626Z\"}, \"eval-supp-spatial-crm-norm005-s45\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T06:45:22.337Z\"}, \"eval-supp-spatial-vla-only-s45\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T06:45:16.646Z\"}, \"eval-supp-long-adapt-tau025-s47\": {\"status\": \"RUNNING\", \"updated_at\": \"2026-05-24T06:38:39.651Z\"}, \"precompute-pi05-long-2048-r2\": {\"status\": \"RUNNING\", \"updated_at\": \"2026-05-24T06:23:39.262Z\"}, \"precompute-pi05-goal-2048-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T06:23:35.000Z\"}, \"precompute-pi05-object-2048-r2\": {\"status\": \"RUNNING\", \"updated_at\": \"2026-05-24T06:23:31.677Z\"}, \"eval-supp-long-vla-only-s46\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T06:15:12.631Z\"}, \"precompute-pi05-spatial-2048-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T06:13:04.507Z\"}, \"precompute-smolvla-goal-bjb1-32546\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T05:44:03.369Z\"}, \"eval-supp-goal-vla-only-s46\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T05:43:32.643Z\"}, \"eval-supp-goal-reconvla-s46\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T05:43:26.502Z\"}, \"crm-train-pi05-spatial-full\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T03:28:46.242Z\"}, \"eval-obs-only-spatial-v2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T03:27:16.008Z\"}, \"eval-perdof-object-norm003-seed44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T03:27:10.816Z\"}, \"eval-random-selection-spatial-seed42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T03:27:05.531Z\"}, \"eval-adaptive-k-spatial-p90-seed44-bjb2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T03:27:01.680Z\"}, \"eval-supp-goal-vla-only-wrapper-s44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T03:26:55.797Z\"}, \"eval-supp-long-reconvla-s45\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T03:26:47.449Z\"}, \"eval-supp-spatial-k2mean-s46\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T03:26:39.499Z\"}, \"eval-supp-obj-crm-norm005-s46\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-24T03:26:33.701Z\"}, \"eval-pi05-vla-only-long-seed42-r4\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T03:26:27.340Z\"}, \"eval-supp-reconvla-obj-s45\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T03:26:15.872Z\"}, \"eval-pi05-vla-only-object-seed42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T03:25:46.138Z\"}, \"eval-pi05-vla-only-object-seed43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T03:25:36.173Z\"}, \"eval-pi05-vla-only-object-seed44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T03:25:23.533Z\"}, \"eval-supp-long-k2mean-s45\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T03:24:43.469Z\"}, \"eval-supp-goal-k2mean-s46\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T03:24:33.666Z\"}, \"eval-supp-goal-adapt-tau025-s46\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T03:24:30.058Z\"}, \"eval-supp-goal-crm-norm005-s46\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T03:24:26.680Z\"}, \"eval-supp-spatial-adapt-tau025-s45-r3\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T03:19:19.270Z\"}, \"eval-supp-spatial-k2mean-s45\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T03:18:33.793Z\"}, \"eval-supp-spatial-vla-only-s46\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T03:18:27.488Z\"}, \"eval-supp-spatial-reconvla-s46\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T03:18:20.676Z\"}, \"eval-supp-spatial-adapt-tau025-s46\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T03:18:17.471Z\"}, \"eval-supp-spatial-crm-norm005-s46\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T03:18:14.133Z\"}, \"eval-supp-long-crm-norm005-s45\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T00:54:53.307Z\"}, \"eval-supp-long-adapt-tau025-s45\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T00:53:11.757Z\"}, \"eval-supp-long-vla-only-s45\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T00:53:04.280Z\"}, \"eval-supp-spatial-reconvla-s45\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T00:30:53.206Z\"}, \"eval-supp-goal-k2mean-s45\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T00:21:09.215Z\"}, \"eval-supp-adapt-tau025-obj-s45\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T23:45:46.677Z\"}, \"eval-supp-obj-k2mean-s45\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T23:45:41.402Z\"}, \"eval-supp-crm-obj-s46\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T23:43:24.974Z\"}, \"eval-supp-spatial-adapt-tau025-s45\": {\"status\": \"DEPLOYED\", \"updated_at\": \"2026-05-23T23:42:01.475Z\"}, \"eval-supp-long-k2mean-s44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T23:04:07.248Z\"}, \"eval-supp-long-reconvla-s44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T23:04:01.262Z\"}, \"eval-supp-k2mean-spatial-s45\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-23T23:02:16.008Z\"}, \"eval-supp-goal-reconvla-s45\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T22:57:24.122Z\"}, \"eval-supp-goal-vla-only-s45\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T22:57:20.913Z\"}, \"eval-supp-crm-norm005-obj-s46\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T22:57:13.555Z\"}, \"eval-supp-goal-crm-norm005-s45\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T22:56:01.038Z\"}, \"eval-supp-crm-norm005-obj-s45\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T22:37:07.655Z\"}, \"eval-supp-reconvla-obj-s46\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T22:31:59.949Z\"}, \"eval-supp-goal-adapt-tau025-s45\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T22:31:49.469Z\"}, \"eval-supp-long-crm-norm005-s44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T21:28:56.768Z\"}, \"eval-supp-long-adapt-tau025-s44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T21:28:50.765Z\"}, \"eval-supp-k2mean-obj-s46\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T21:28:27.870Z\"}, \"eval-supp-k2mean-obj-s45\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T21:28:21.695Z\"}, \"eval-supp-adapt-tau025-obj-s46\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T20:26:37.804Z\"}, \"eval-supp-long-vla-only-s43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T20:21:04.060Z\"}, \"eval-supp-long-k2mean-s42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T20:13:10.758Z\"}, \"eval-supp-obj-vla-only-s46\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T20:09:46.499Z\"}, \"eval-supp-long-vla-only-s44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T20:09:40.603Z\"}, \"eval-supp-long-k2mean-s43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T20:09:34.819Z\"}, \"eval-supp-long-reconvla-s43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T20:09:28.982Z\"}, \"eval-supp-long-crm-norm005-s43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T20:09:23.098Z\"}, \"eval-supp-long-adapt-tau025-s43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T20:09:17.172Z\"}, \"eval-supp-obj-adapt-tau025-s45-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T18:16:04.202Z\"}, \"eval-supp-long-crm-norm005-s42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T17:25:47.737Z\"}, \"eval-supp-long-adapt-tau025-s42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T17:25:41.523Z\"}, \"eval-supp-long-reconvla-s42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T17:25:32.561Z\"}, \"eval-ablation-tau040-goal-s42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T17:25:24.644Z\"}, \"eval-ablation-tau015-goal-s42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T17:25:15.441Z\"}, \"eval-supp-k2mean-object-s44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T17:25:06.995Z\"}, \"eval-ablation-tau010-goal-s42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T17:24:59.810Z\"}, \"eval-supp-obj-reconvla-s44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T17:24:48.531Z\"}, \"eval-supp-spatial-vla-only-s44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T17:22:10.552Z\"}, \"eval-supp-goal-vla-only-wrapper-s44-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T17:21:50.650Z\"}, \"eval-supp-k2mean-spatial-s44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T14:41:49.032Z\"}, \"eval-supp-spatial-vla-only-s43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T14:41:43.043Z\"}, \"eval-supp-k2mean-goal-s44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T14:21:57.954Z\"}, \"eval-supp-adapt-tau025-obj-s44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T14:21:51.978Z\"}, \"eval-supp-crm-norm005-obj-s44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T14:21:46.269Z\"}, \"eval-supp-goal-vla-only-wrapper-s43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T14:21:40.459Z\"}, \"eval-supp-long-vla-only-s42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T14:13:45.028Z\"}, \"eval-supp-goal-reconvla-s44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T13:25:45.095Z\"}, \"eval-supp-obj-reconvla-s43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T13:25:39.232Z\"}, \"eval-supp-crm-norm005-goal-s44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T13:25:33.374Z\"}, \"eval-supp-k2mean-object-s43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T11:53:35.791Z\"}, \"eval-supp-k2mean-goal-s42-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T11:49:21.426Z\"}, \"eval-supp-adapt-tau025-goal-s44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T11:33:49.855Z\"}, \"eval-supp-crm-norm005-obj-s43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T11:33:43.836Z\"}, \"eval-supp-adapt-tau025-goal-s43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T11:33:38.082Z\"}, \"eval-supp-crm-norm005-goal-s43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T11:33:32.430Z\"}, \"eval-supp-adapt-tau025-obj-s43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T11:33:25.089Z\"}, \"eval-supp-goal-reconvla-s43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T11:31:34.130Z\"}, \"eval-supp-k2mean-spatial-s43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T11:30:05.886Z\"}, \"eval-supp-reconvla-spatial-s44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T11:25:39.981Z\"}, \"eval-supp-reconvla-spatial-s43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T11:21:32.905Z\"}, \"eval-supp-k2mean-goal-s43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T11:20:45.445Z\"}, \"eval-supp-k2mean-object-s42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T10:48:56.855Z\"}, \"eval-supp-goal-adapt-tau025-s42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T10:47:49.735Z\"}, \"eval-supp-goal-crm005-s42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T10:27:32.365Z\"}, \"eval-supp-goal-reconvla-s42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T10:11:16.616Z\"}, \"train-crm-unified-4suite-r6\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T10:09:50.183Z\"}, \"eval-goal-vla-only-wrapper-s42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T10:09:44.401Z\"}, \"eval-supp-obj-adapt-tau025-s42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T10:05:16.143Z\"}, \"eval-supp-k2mean-spatial-s42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T09:40:16.419Z\"}, \"eval-supp-crm-norm005-spatial-s44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T08:56:25.513Z\"}, \"eval-supp-adapt-tau025-spatial-s44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T08:44:11.956Z\"}, \"eval-supp-reconvla-k2-spatial-s42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T08:36:38.221Z\"}, \"eval-supp-adapt-tau025-spatial-s43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T08:36:15.063Z\"}, \"eval-supp-crm-norm005-spatial-s43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T08:35:04.453Z\"}, \"eval-supp-k2mean-goal-s42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T08:29:52.019Z\"}, \"eval-supp-obj-adapt-s42-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T07:08:55.601Z\"}, \"eval-object-vla-only-wrapper-s44-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T07:08:49.478Z\"}, \"eval-object-vla-only-wrapper-s43-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T07:08:43.800Z\"}, \"eval-object-vla-only-wrapper-s42-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T07:08:33.647Z\"}, \"eval-supp-obj-reconvla-s42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T07:05:57.520Z\"}, \"eval-supp-obj-crm005-s42-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T06:40:03.190Z\"}, \"eval-supp-adapt-tau035-spatial-s42-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T06:20:31.236Z\"}, \"eval-supp-adapt-tau015-spatial-s42-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T06:16:30.800Z\"}, \"eval-supp-crm-norm02-spatial-s42-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T06:12:43.228Z\"}, \"eval-supp-adapt-tau025-spatial-s42-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T06:12:07.119Z\"}, \"eval-openvla-object-baseline-seed42-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T04:55:40.054Z\"}, \"eval-obs-only-object-norm02-seed55\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T04:55:15.323Z\"}, \"precompute-pi05-features-object\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T04:55:09.845Z\"}, \"precompute-smolvla-goal-shard2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T04:55:04.457Z\"}, \"precompute-smolvla-goal-shard1\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T04:54:57.961Z\"}, \"precompute-smolvla-goal-shard0\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T04:54:52.235Z\"}, \"eval-smolvla-long-seed2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T04:54:46.718Z\"}, \"eval-smolvla-long-seed1\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T04:54:41.335Z\"}, \"eval-smolvla-long-seed0\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T04:54:35.953Z\"}, \"eval-smolvla-crm-spatial-seed42-v1\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T04:54:30.564Z\"}, \"eval-smolvla-crm-spatial-seed43-v1\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T04:54:25.093Z\"}, \"eval-smolvla-crm-spatial-seed44-v1\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T04:54:19.576Z\"}, \"eval-smolvla-crm-goal-seed42-v1\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T04:54:14.038Z\"}, \"eval-smolvla-crm-goal-seed43-v1\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T04:54:08.535Z\"}, \"eval-smolvla-crm-goal-seed44-v1\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T04:50:29.455Z\"}, \"eval-supp-obj-adapt-s42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T04:50:22.494Z\"}, \"eval-crm-norm02-spatial-s42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T04:50:16.948Z\"}, \"eval-adaptive-tau015-spatial-s42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T04:50:11.299Z\"}, \"eval-adaptive-tau025-spatial-s42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T04:50:03.969Z\"}, \"eval-adaptive-tau035-spatial-s42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T04:49:53.623Z\"}, \"train-crm-unified-4suite-r5-resumed\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T04:32:30.777Z\"}, \"eval-object-vla-only-wrapper-s44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T04:07:05.366Z\"}, \"eval-object-vla-only-wrapper-s43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T04:06:59.994Z\"}, \"eval-object-vla-only-wrapper-s42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T04:06:54.695Z\"}, \"eval-supp-obj-crm005-s42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T04:06:49.393Z\"}, \"eval-supp-adapt-tau035-spatial-s42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T04:06:43.867Z\"}, \"eval-supp-adapt-tau025-spatial-s42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T04:06:38.592Z\"}, \"eval-supp-adapt-tau015-spatial-s42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T04:06:33.197Z\"}, \"eval-supp-crm-norm02-spatial-s42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T04:06:27.722Z\"}, \"eval-3dir-adaptive-spatial-s42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T03:54:21.349Z\"}, \"eval-3dir-norm03-spatial-s42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T03:53:00.389Z\"}, \"eval-3dir-reconvla-spatial-s42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T03:52:57.581Z\"}, \"eval-3dir-norm01-spatial-s42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T03:52:54.819Z\"}, \"eval-3dir-norm005-spatial-s42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T03:52:51.544Z\"}, \"precompute-pi05-goal-2048\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T03:39:47.719Z\"}, \"precompute-pi05-spatial-2048\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T03:39:37.428Z\"}, \"precompute-pi05-object-2048\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T03:39:26.989Z\"}, \"eval-smolvla-crm-object-seed43-v1\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T03:35:03.670Z\"}, \"eval-smolvla-crm-object-seed42-v1\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T03:35:00.107Z\"}, \"eval-smolvla-crm-object-seed44-v1\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T03:31:27.072Z\"}, \"train-crm-unified-4suite-r5\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T01:33:47.618Z\"}, \"eval-smolvla-crm-goal-seed43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T01:33:43.543Z\"}, \"eval-smolvla-crm-goal-seed42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T01:33:35.873Z\"}, \"eval-smolvla-crm-spatial-seed44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T01:33:30.489Z\"}, \"eval-smolvla-crm-spatial-seed43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T01:33:22.750Z\"}, \"eval-smolvla-crm-spatial-seed42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-23T01:33:14.831Z\"}, \"eval-smolvla-crm-goal-seed44\": {\"status\": \"PENDING\", \"updated_at\": \"2026-05-22T23:26:30.844Z\"}, \"precompute-pi05-long-2048\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T23:24:07.545Z\"}, \"eval-smolvla-lerobot-goal-seed44-v3\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T23:18:08.524Z\"}, \"eval-smolvla-lerobot-goal-seed43-v3\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T23:17:55.201Z\"}, \"eval-smolvla-lerobot-spatial-seed43-v3\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T23:17:49.796Z\"}, \"train-crm-smolvla-3suite-v1\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T23:11:45.218Z\"}, \"eval-smolvla-lerobot-goal-seed43-v2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T20:50:32.835Z\"}, \"eval-smolvla-lerobot-spatial-seed43-v2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T20:50:27.156Z\"}, \"eval-smolvla-lerobot-object-seed44-v2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T20:50:21.831Z\"}, \"eval-smolvla-lerobot-object-seed43-v2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T20:50:16.518Z\"}, \"eval-smolvla-lerobot-goal-seed43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T20:13:51.786Z\"}, \"eval-smolvla-lerobot-spatial-seed43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T20:13:46.670Z\"}, \"eval-smolvla-lerobot-object-seed44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T20:13:40.397Z\"}, \"eval-smolvla-lerobot-object-seed43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T20:13:33.516Z\"}, \"eval-smolvla-lerobot-spatial-seed44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T20:12:30.387Z\"}, \"precompute-smolvla-long-wrapper-bjb1\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T19:05:54.572Z\"}, \"eval-smolvla-lerobot-goal-seed44\": {\"status\": \"QUEUED\", \"updated_at\": \"2026-05-22T19:02:22.376Z\"}, \"eval-smolvla-lerobot-long-seed44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T18:46:08.623Z\"}, \"eval-smolvla-lerobot-long-seed43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T18:46:05.996Z\"}, \"eval-smolvla-lerobot-long-seed42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T18:46:03.386Z\"}, \"train-crm-unified-4suite-r4\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T18:14:09.706Z\"}, \"eval-pi05-vla-only-long-seed42-r4-rerun\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T18:12:13.396Z\"}, \"eval-pi05-crm-object-seed44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T17:20:46.002Z\"}, \"eval-pi05-crm-object-seed43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T17:20:35.256Z\"}, \"eval-pi05-crm-object-seed42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T17:20:24.929Z\"}, \"eval-pi05-vla-only-long-seed43-r4-std\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T17:17:06.116Z\"}, \"eval-pi05-vla-only-goal-seed44-r4-std\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T17:16:24.608Z\"}, \"eval-pi05-vla-only-goal-seed42-r4-std\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T17:16:00.966Z\"}, \"eval-pi05-vla-only-long-seed44-r4-std\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T17:15:55.404Z\"}, \"eval-pi05-vla-only-goal-seed43-r4-std\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T17:14:50.393Z\"}, \"eval-pi05-vla-only-goal-seed42-r4\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T17:02:13.462Z\"}, \"precompute-smolvla-long-k2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T17:01:57.058Z\"}, \"train-crm-unified-4suite-r3\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T17:00:24.406Z\"}, \"train-crm-unified-4suite-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T17:00:17.793Z\"}, \"precompute-smolvla-goal-bjb2-28827\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T17:00:10.097Z\"}, \"precompute-smolvla-long-bjb2-28827\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T17:00:02.382Z\"}, \"eval-pi05-vla-only-spatial-seed44-r4\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T16:59:56.882Z\"}, \"eval-pi05-vla-only-spatial-seed43-r4\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T16:59:51.541Z\"}, \"eval-pi05-vla-only-spatial-seed42-r4\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T16:59:46.047Z\"}, \"eval-pi05-vla-only-long-seed44-r4\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T16:43:05.868Z\"}, \"eval-pi05-vla-only-long-seed43-r4\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T16:42:49.732Z\"}, \"eval-pi05-vla-only-goal-seed44-r4\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T16:23:50.003Z\"}, \"eval-pi05-vla-only-goal-seed43-r4\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T16:23:41.572Z\"}, \"eval-pi05-vla-only-long-seed42-r4-std\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-22T16:17:13.985Z\"}, \"precompute-smolvla-goal-k10\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-22T15:48:27.660Z\"}, \"precompute-smolvla-spatial-k10\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-22T15:48:13.210Z\"}, \"precompute-smolvla-object-k10\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-22T15:47:41.690Z\"}, \"eval-vla-only-long-seed2\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-22T14:19:49.215Z\"}, \"eval-vla-only-long-seed1\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-22T14:19:43.184Z\"}, \"eval-vla-only-long-seed0\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-22T14:19:38.265Z\"}, \"eval-openvla-oft-official-object\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T13:24:23.378Z\"}, \"eval-pi05-crm-spatial-seed44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T13:24:17.309Z\"}, \"eval-pi05-crm-spatial-seed43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T13:24:14.018Z\"}, \"eval-pi05-crm-spatial-seed42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T13:24:09.791Z\"}, \"eval-pi05-vla-only-object-seed43-r4\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T11:55:13.893Z\"}, \"eval-pi05-vla-only-object-seed44-r4\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T11:51:23.505Z\"}, \"eval-smolvla-lerobot-official-object\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T11:33:17.264Z\"}, \"eval-pi05-vla-only-object-seed42-r4\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T11:26:20.250Z\"}, \"train-crm-unified-4suite\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T11:18:23.000Z\"}, \"precompute-smolvla-long-bjb1-32546-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T11:15:49.784Z\"}, \"precompute-smolvla-long-bjb1-32546\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T11:11:37.983Z\"}, \"eval-loss-perdof-object-seed42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T10:51:37.131Z\"}, \"eval-loss-combined-object-seed42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T10:41:20.547Z\"}, \"eval-loss-conformal-object-seed42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T10:40:44.234Z\"}, \"eval-loss-mse-object-seed42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T10:26:08.383Z\"}, \"eval-openvla-oft-object-baseline-seed42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T09:00:45.065Z\"}, \"precompute-pi05-long-bjb1-18228\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-22T09:00:18.250Z\"}, \"precompute-smolvla-long-bjb1-18228\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T08:56:52.782Z\"}, \"precompute-pi05-goal-bjb2-28827-s2\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-22T08:03:27.743Z\"}, \"precompute-pi05-goal-bjb2-28827-s1\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-22T08:03:23.271Z\"}, \"precompute-pi05-goal-bjb2-28827-s0\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-22T08:03:18.741Z\"}, \"crm-loss-combined\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T07:39:25.644Z\"}, \"crm-loss-conformal\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T07:37:31.142Z\"}, \"precompute-smolvla-goal-bjb1-18228\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T07:33:35.175Z\"}, \"crm-loss-perdof\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T06:35:46.165Z\"}, \"crm-loss-mse-baseline\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T06:32:42.169Z\"}, \"eval-smolvla-acr-goal-seed43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T05:56:00.921Z\"}, \"eval-smolvla-crm-long-seed44-v2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T05:55:17.088Z\"}, \"eval-smolvla-crm-goal-seed44-v2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T05:55:10.553Z\"}, \"eval-smolvla-crm-long-seed43-v2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T05:55:03.970Z\"}, \"eval-smolvla-acr-long-seed42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T05:54:52.777Z\"}, \"eval-smolvla-acr-goal-seed42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T05:54:08.054Z\"}, \"eval-smolvla-crm-long-seed44\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-22T05:10:41.746Z\"}, \"eval-smolvla-crm-long-seed43\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-22T05:10:32.722Z\"}, \"crm-train-pi05-spatial-v2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T01:31:49.429Z\"}, \"crm-train-pi05-object-full\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T01:01:07.723Z\"}, \"crm-train-pi05-spatial\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T18:10:31.701Z\"}, \"crm-train-pi05-object\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T18:10:26.906Z\"}, \"crm-pipeline-auto\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-21T16:37:34.472Z\"}, \"precompute-pi05-obj-s6-r2\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-21T15:04:33.582Z\"}, \"precompute-pi05-obj-s9-r2\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-21T14:19:39.622Z\"}, \"precompute-pi05-obj-s8-r2\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-21T14:19:35.288Z\"}, \"precompute-pi05-obj-s7-r2\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-21T14:19:30.950Z\"}, \"precompute-pi05-obj-s0-r2\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-21T14:19:26.580Z\"}, \"precompute-pi05-obj-s5-r2\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-21T14:19:22.348Z\"}, \"precompute-pi05-obj-s4-r2\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-21T14:19:17.949Z\"}, \"precompute-pi05-obj-s3-r2\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-21T14:19:13.169Z\"}, \"precompute-pi05-obj-s2-r2\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-21T14:19:08.830Z\"}, \"precompute-pi05-obj-s1-r2\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-21T14:19:04.514Z\"}, \"precompute-pi05-obj-s9-fix\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-21T14:05:27.170Z\"}, \"precompute-pi05-obj-s8-fix\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-21T14:05:22.511Z\"}, \"precompute-pi05-obj-s7-fix\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-21T14:05:17.907Z\"}, \"precompute-pi05-obj-s6-fix\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-21T14:05:13.392Z\"}, \"precompute-pi05-obj-s5-fix\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-21T14:05:08.790Z\"}, \"precompute-pi05-obj-shard9\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-21T13:50:29.762Z\"}, \"precompute-pi05-obj-shard8\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-21T13:50:25.069Z\"}, \"precompute-pi05-obj-shard7\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-21T13:50:20.551Z\"}, \"precompute-pi05-obj-shard6\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-21T13:50:15.986Z\"}, \"precompute-pi05-obj-shard5\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-21T13:50:11.353Z\"}, \"precompute-pi05-spatial-shard6\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-21T13:46:14.580Z\"}, \"precompute-pi05-spatial-shard5\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-21T13:46:08.912Z\"}, \"precompute-pi05-spatial-shard4\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-21T13:46:03.897Z\"}, \"precompute-pi05-spatial-shard3\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-21T13:45:58.808Z\"}, \"precompute-pi05-spatial-shard2\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-21T13:45:51.058Z\"}, \"precompute-pi05-spatial-shard1\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-21T13:45:45.566Z\"}, \"precompute-pi05-spatial-shard0\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-21T13:45:40.280Z\"}, \"precompute-pi05-shard0\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-21T13:44:35.499Z\"}, \"precompute-pi05-shard9\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-21T13:42:56.355Z\"}, \"precompute-pi05-shard8\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-21T13:42:50.972Z\"}, \"precompute-pi05-shard7\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-21T13:42:45.877Z\"}, \"precompute-pi05-shard6\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-21T13:42:40.538Z\"}, \"precompute-pi05-shard5\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-21T13:42:35.528Z\"}, \"precompute-pi05-shard4\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-21T13:42:30.590Z\"}, \"precompute-pi05-shard3\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-21T13:42:24.367Z\"}, \"precompute-pi05-shard2\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-21T13:42:18.667Z\"}, \"precompute-pi05-shard1\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-21T13:42:13.102Z\"}, \"eval-pi05-vla-only-spatial-seed45\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T12:22:59.643Z\"}, \"eval-pi05-vla-only-spatial-seed43-r3\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T12:22:49.675Z\"}, \"eval-pi05-vla-only-spatial-seed42-r3\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T12:22:43.339Z\"}, \"eval-pi05-vla-only-object-seed44-r3\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T12:22:38.751Z\"}, \"eval-pi05-vla-only-object-seed43-r3\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T12:22:31.438Z\"}, \"eval-pi05-vla-only-object-seed42-r3\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T12:22:24.249Z\"}, \"eval-spatial-obs-only-seed45\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T11:50:52.186Z\"}, \"eval-pi05-vla-only-spatial-seed44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T11:46:53.337Z\"}, \"eval-pi05-vla-only-spatial-seed43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T11:46:50.878Z\"}, \"eval-pi05-vla-only-spatial-seed42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T11:46:42.183Z\"}, \"eval-pi05-baseline-object-seed42-r2\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-21T08:02:33.602Z\"}, \"eval-k20-obs-only-spatial-seed44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T07:30:47.255Z\"}, \"eval-k20-obs-only-spatial-seed43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T07:30:42.676Z\"}, \"eval-k20-obs-only-spatial-seed42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T07:30:37.114Z\"}, \"eval-k20-obs-only-object-seed45\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T07:30:32.202Z\"}, \"eval-obs-only-object-norm003-seed66\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T05:14:31.173Z\"}, \"eval-obs-only-object-norm01-seed66\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T05:14:00.886Z\"}, \"eval-obs-only-object-norm005-seed66\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T05:13:12.047Z\"}, \"eval-obs-only-object-norm003-seed67\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T05:10:29.526Z\"}, \"eval-k20-obs-only-object-seed44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T05:07:12.893Z\"}, \"eval-k20-obs-only-object-seed43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T05:07:10.342Z\"}, \"eval-k20-obs-only-object-seed42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T05:07:08.046Z\"}, \"eval-crm-object-k20-seed44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T05:07:05.713Z\"}, \"eval-crm-object-k20-seed42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T05:07:03.314Z\"}, \"eval-obs-only-object-norm02-seed53\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T04:55:07.524Z\"}, \"eval-obs-only-object-norm02-seed52\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T04:55:05.083Z\"}, \"eval-obs-only-object-norm02-seed51\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T04:55:02.734Z\"}, \"eval-obs-only-object-norm02-seed50\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T04:55:00.434Z\"}, \"eval-obs-only-object-norm02-seed48-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T04:54:57.990Z\"}, \"eval-obs-only-object-norm02-seed47\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T04:54:54.506Z\"}, \"eval-obs-only-object-norm02-seed46\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T04:54:51.647Z\"}, \"eval-obs-only-object-norm02-seed45\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T04:54:44.901Z\"}, \"eval-obs-only-object-norm02-seed44-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T04:54:42.439Z\"}, \"eval-obs-only-object-norm02-seed43-r3\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T04:54:39.963Z\"}, \"eval-obs-only-object-norm02-seed43-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T04:54:37.451Z\"}, \"eval-obs-only-object-norm005-seed67\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T04:50:15.572Z\"}, \"eval-obs-only-object-norm01-seed67\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T04:49:55.438Z\"}, \"eval-vla-only-object-seed50\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T04:48:32.810Z\"}, \"eval-vla-only-object-seed49\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T04:48:27.282Z\"}, \"eval-vla-only-object-seed48\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T04:48:15.442Z\"}, \"eval-vla-only-object-seed46\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T04:48:05.210Z\"}, \"eval-vla-only-object-seed45\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T04:47:51.213Z\"}, \"eval-vla-only-object-seed44-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T04:47:46.335Z\"}, \"eval-plan-a-object-seed42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T04:47:42.399Z\"}, \"eval-vla-only-object-seed43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T04:47:36.667Z\"}, \"eval-vla-only-object\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T04:47:19.616Z\"}, \"eval-plan-a-spatial-seed43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T04:46:30.740Z\"}, \"eval-plan-a-object-seed44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T04:45:27.640Z\"}, \"eval-plan-a-spatial-seed42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T04:44:12.088Z\"}, \"eval-plan-a-spatial-seed44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T04:42:43.669Z\"}, \"eval-plan-a-object-seed43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T04:42:32.790Z\"}, \"eval-random-selection-object-seed44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T04:34:43.303Z\"}, \"eval-random-selection-object-seed43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T04:34:38.177Z\"}, \"eval-random-selection-object-seed42-r3\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-21T04:34:32.245Z\"}, \"eval-vla-only-spatial-seed50\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-21T04:32:53.123Z\"}, \"eval-crm-spatial-k10-seed50\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-21T04:32:42.275Z\"}, \"eval-crm-spatial-k10-seed49\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-21T04:32:32.158Z\"}, \"eval-obs-only-object-norm02-k20-seed44\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-21T04:32:24.008Z\"}, \"eval-obs-only-object-norm02-k20-seed43\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-21T04:32:17.159Z\"}, \"eval-obs-only-object-norm02-k20-seed42\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-21T04:32:11.044Z\"}, \"eval-obs-only-object-norm01-seed60\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T04:01:22.020Z\"}, \"eval-pi05-baseline-object-seed42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:59:27.286Z\"}, \"eval-obs-only-object-norm003-seed76\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-21T03:33:43.610Z\"}, \"eval-obs-only-object-norm01-seed54\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:30:13.218Z\"}, \"eval-obs-only-object-norm01-seed53\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:30:10.368Z\"}, \"eval-obs-only-object-norm01-seed52\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:30:07.112Z\"}, \"eval-obs-only-object-norm01-seed50\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:30:04.361Z\"}, \"eval-obs-only-object-norm01-seed49\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:29:59.855Z\"}, \"eval-obs-only-object-norm01-seed48\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:29:57.231Z\"}, \"eval-obs-only-object-norm01-seed47\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:29:54.309Z\"}, \"eval-obs-only-object-norm01-seed45-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:29:47.720Z\"}, \"eval-obs-only-object-norm01-seed44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:29:43.639Z\"}, \"eval-obs-only-object-norm005-seed55\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:29:41.343Z\"}, \"eval-obs-only-object-norm005-seed50\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:29:39.045Z\"}, \"eval-obs-only-object-norm005-seed49\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:29:36.190Z\"}, \"eval-obs-only-object-norm005-seed48\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:29:30.312Z\"}, \"eval-obs-only-object-norm005-seed47\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:29:23.229Z\"}, \"eval-obs-only-object-norm005-seed44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:29:16.871Z\"}, \"eval-obs-only-object-norm005-seed43-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:29:14.257Z\"}, \"eval-obs-only-object-norm005-seed43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:29:10.509Z\"}, \"eval-obs-only-object-norm003-seed48\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:29:06.231Z\"}, \"eval-obs-only-object-norm003-seed47-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:29:02.399Z\"}, \"eval-obs-only-object-norm003-seed46\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:28:57.483Z\"}, \"eval-obs-only-object-norm003-seed45\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:28:51.768Z\"}, \"eval-obs-only-object-norm003-seed44-bjb2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:28:48.787Z\"}, \"eval-obs-only-object-norm003-seed44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:28:46.427Z\"}, \"eval-obs-only-object-norm003-seed43-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:28:43.998Z\"}, \"eval-obs-only-object-norm003-seed43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:28:41.514Z\"}, \"eval-obs-only-object-norm01-seed57\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:19:50.462Z\"}, \"eval-obs-only-object-norm005-seed65\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:19:48.034Z\"}, \"eval-obs-only-object-norm005-seed61\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:19:45.881Z\"}, \"eval-obs-only-object-norm005-seed58\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:19:43.346Z\"}, \"eval-obs-only-object-norm003-seed59\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:19:41.023Z\"}, \"eval-obs-only-object-norm003-seed56\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:19:38.737Z\"}, \"eval-obs-only-object-norm01-seed77\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-21T03:17:06.237Z\"}, \"eval-obs-only-object-norm01-seed76\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-21T03:17:01.964Z\"}, \"eval-obs-only-object-norm005-seed77\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-21T03:16:58.507Z\"}, \"eval-obs-only-object-norm003-seed63-r3\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-21T03:16:54.862Z\"}, \"eval-obs-only-object-norm005-seed76\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-21T03:16:49.849Z\"}, \"eval-obs-only-object-norm003-seed62-r3\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-21T03:16:44.624Z\"}, \"eval-obs-only-object-norm003-seed78\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-21T03:16:34.818Z\"}, \"eval-obs-only-object-norm003-seed77\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-21T03:16:26.327Z\"}, \"eval-obs-only-object-norm005-seed75\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:13:18.900Z\"}, \"eval-obs-only-object-norm01-seed74\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:13:14.621Z\"}, \"eval-obs-only-object-norm005-seed72\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:13:06.825Z\"}, \"eval-obs-only-object-norm003-seed63-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:13:03.208Z\"}, \"eval-obs-only-object-norm01-seed71\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:12:59.417Z\"}, \"eval-obs-only-object-norm003-seed62-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:12:55.649Z\"}, \"eval-obs-only-object-norm003-seed73\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:12:20.827Z\"}, \"eval-obs-only-object-norm01-seed51-r3\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:11:43.996Z\"}, \"eval-obs-only-object-norm01-seed52-r3\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:10:52.558Z\"}, \"eval-obs-only-object-norm01-seed65\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:10:27.996Z\"}, \"eval-obs-only-object-norm01-seed64\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:10:08.688Z\"}, \"eval-obs-only-object-norm005-seed64\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:09:32.235Z\"}, \"eval-obs-only-object-norm003-seed65\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:08:52.713Z\"}, \"eval-obs-only-object-norm003-seed64\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:05:28.591Z\"}, \"eval-obs-only-object-norm005-seed62\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T01:15:11.709Z\"}, \"eval-obs-only-object-norm005-seed63\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T01:14:56.556Z\"}, \"eval-obs-only-object-norm01-seed61\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T01:14:51.727Z\"}, \"eval-obs-only-object-norm003-seed64-bjb2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T00:54:21.580Z\"}, \"eval-obs-only-object-norm003-seed63\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T00:36:29.353Z\"}, \"eval-obs-only-object-norm003-seed62\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T00:36:21.900Z\"}, \"eval-obs-only-object-norm01-seed51-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T00:36:16.959Z\"}, \"eval-obs-only-object-norm01-seed52-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T00:36:12.707Z\"}, \"eval-obs-only-object-norm01-seed51\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T00:18:47.313Z\"}, \"eval-obs-only-object-norm005-seed49-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T00:13:00.000Z\"}, \"eval-obs-only-object-norm005-seed55-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-21T00:13:00.000Z\"}, \"eval-openvla-crm-object-seed42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T23:28:23.498Z\"}, \"eval-obs-only-object-norm003-seed44-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T22:28:30.000Z\"}, \"eval-random-selection-object-seed49\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T22:21:32.888Z\"}, \"eval-random-selection-object-seed48\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T22:20:24.412Z\"}, \"eval-k5-obs-only-object-seed44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T22:04:37.390Z\"}, \"eval-obs-only-spatial-norm02-seed52\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T21:59:15.550Z\"}, \"eval-obs-only-object-norm02-seed54\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T21:32:35.788Z\"}, \"D088-eval-adaptive-unc-head-object-seed44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T21:16:27.264Z\"}, \"D088-eval-adaptive-unc-head-object-seed43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T21:16:23.354Z\"}, \"D088-eval-adaptive-unc-head-object-seed42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T21:16:19.344Z\"}, \"eval-obs-only-object-norm005-seed45\": {\"status\": \"DEPLOYED\", \"updated_at\": \"2026-05-20T19:45:39.649Z\"}, \"eval-adaptive-unc-head-object-seed42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T19:42:34.465Z\"}, \"eval-adaptive-unc-head-object-seed43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T19:38:46.967Z\"}, \"eval-perdof-object-norm02-seed50\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T19:34:40.308Z\"}, \"eval-adaptive-unc-head-object-seed44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T19:21:50.874Z\"}, \"eval-random-selection-spatial-seed42-r3\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T19:18:36.706Z\"}, \"eval-obs-only-spatial-norm02-seed50\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T19:18:34.577Z\"}, \"train-crm-openvla-obs-only\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T19:18:14.214Z\"}, \"openvla-precompute-k1\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T18:37:09.326Z\"}, \"eval-random-selection-object-seed46-r3\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T17:36:15.098Z\"}, \"eval-perdof-object-norm02-seed49\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T17:31:38.771Z\"}, \"eval-random-selection-object-seed47\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T17:30:04.397Z\"}, \"eval-obs-only-spatial-norm02-seed42-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T17:28:06.990Z\"}, \"eval-k5-obs-only-object-seed43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T17:22:56.685Z\"}, \"eval-random-selection-spatial-seed43-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T17:21:49.990Z\"}, \"eval-random-selection-spatial-seed44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T17:20:57.101Z\"}, \"eval-crm-k1-object-seed43-plan702\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T16:58:33.591Z\"}, \"eval-crm-k1-object-seed42-plan702\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T16:58:27.648Z\"}, \"eval-crm-k1-object-seed44-plan702\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T16:50:59.250Z\"}, \"eval-random-selection-object-seed46-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T15:35:34.584Z\"}, \"eval-random-selection-spatial-seed43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T15:34:05.777Z\"}, \"eval-random-selection-object-seed46\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T15:33:54.594Z\"}, \"eval-obs-only-spatial-seed48\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T15:33:15.181Z\"}, \"eval-vla-only-spatial-seed48\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T15:32:12.693Z\"}, \"eval-obs-only-spatial-norm02-seed42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T15:19:37.689Z\"}, \"eval-obs-only-spatial-norm02-seed49\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T15:19:01.383Z\"}, \"eval-adaptive-k-spatial-p90-seed44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T15:17:24.944Z\"}, \"eval-argmin-object-seed50\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T15:05:10.161Z\"}, \"eval-vla-only-object-seed48-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T14:59:00.735Z\"}, \"eval-vla-only-goal-seed51\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T14:58:56.897Z\"}, \"eval-random-selection-spatial-seed42-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T14:48:09.495Z\"}, \"eval-random-selection-object-seed45\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T14:37:22.190Z\"}, \"eval-crm-k1-object-seed44-plan702-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T14:34:18.084Z\"}, \"eval-crm-k1-object-seed43-plan702-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T14:34:14.100Z\"}, \"eval-crm-k1-object-seed42-plan702-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T14:34:10.003Z\"}, \"eval-perdof-object-norm02-seed48\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T14:26:11.524Z\"}, \"eval-argmin-object-k5-seed44-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T14:26:08.978Z\"}, \"eval-vla-only-goal-seed44-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T14:26:03.273Z\"}, \"eval-obs-only-spatial-norm02-seed46-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T14:25:59.677Z\"}, \"eval-latency-profiling-v1\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T13:50:45.112Z\"}, \"eval-adaptive-k-spatial-p75-seed44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T13:33:48.420Z\"}, \"eval-obs-only-goal-norm02-seed51\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T13:32:36.837Z\"}, \"eval-adaptive-k-spatial-p25-seed44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T13:31:25.501Z\"}, \"eval-openvla-object-baseline-seed42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T13:26:22.725Z\"}, \"eval-argmin-object-seed49\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T13:17:52.468Z\"}, \"eval-obs-only-goal-norm02-seed53\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-20T13:08:32.542Z\"}, \"eval-argmin-object-seed48\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T13:07:28.620Z\"}, \"eval-obs-only-spatial-norm02-seed48\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T13:07:16.116Z\"}, \"eval-obs-only-goal-norm02-seed52\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T13:06:48.437Z\"}, \"eval-adaptive-k-spatial-p90-seed43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T13:06:03.701Z\"}, \"eval-perdof-object-norm02-seed45-r3\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T13:05:55.751Z\"}, \"eval-adaptive-k-spatial-p90-seed42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T12:54:12.191Z\"}, \"eval-obs-only-object-norm02-seed49\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T12:48:49.975Z\"}, \"eval-vla-only-goal-seed47\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T12:41:49.447Z\"}, \"eval-adaptive-k-spatial-p50-seed44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T11:30:00.787Z\"}, \"eval-adaptive-k-spatial-p50-seed43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T11:29:58.029Z\"}, \"eval-adaptive-k-spatial-p50-seed42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T11:13:15.994Z\"}, \"eval-adaptive-k-spatial-p25-seed42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T10:52:54.947Z\"}, \"eval-adaptive-k-spatial-p25-seed43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T10:51:17.226Z\"}, \"eval-adaptive-k-spatial-p75-seed43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T10:38:12.906Z\"}, \"eval-crm-object-k20-seed43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T10:36:14.773Z\"}, \"eval-vla-only-long-seed49-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T10:34:46.457Z\"}, \"eval-adaptive-k-spatial-p75-seed42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T10:34:34.589Z\"}, \"eval-adaptive-k-spatial-p50-seed44-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T09:52:50.961Z\"}, \"eval-adaptive-k-p75-seed42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T09:46:30.063Z\"}, \"eval-adaptive-k-p75-seed43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T09:46:26.443Z\"}, \"eval-adaptive-k-p50-seed42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T09:46:22.801Z\"}, \"eval-adaptive-k-p50-seed43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T09:46:19.108Z\"}, \"eval-random-selection-object-seed42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T09:26:47.119Z\"}, \"eval-adaptive-k-spatial-p50-seed43-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T09:26:09.877Z\"}, \"eval-obs-only-object-norm02-seed42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T08:44:33.011Z\"}, \"latency-profile-n1000\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T08:42:01.299Z\"}, \"eval-adaptive-k-p90-seed44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T06:53:17.867Z\"}, \"eval-vla-only-long-seed54\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-20T05:59:13.545Z\"}, \"eval-adaptive-k-p25-seed43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T05:56:34.512Z\"}, \"eval-crm-spatial-k10-seed51\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T05:56:30.173Z\"}, \"eval-vla-only-goal-seed49\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T05:56:26.105Z\"}, \"eval-vla-only-long-seed52\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T05:56:21.658Z\"}, \"eval-vla-only-long-seed51\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T05:56:16.817Z\"}, \"eval-vla-only-long-seed50\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T05:56:11.186Z\"}, \"eval-crm-long-seed50\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T05:56:05.404Z\"}, \"eval-adaptive-k-p25-seed44-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T05:56:00.045Z\"}, \"calibrate-crm-correction-signal\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T05:39:46.462Z\"}, \"eval-crm-long-seed54\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-20T05:39:32.457Z\"}, \"eval-vla-only-spatial-seed54\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-20T05:39:29.096Z\"}, \"eval-crm-long-seed53\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-20T05:39:25.536Z\"}, \"eval-vla-only-spatial-seed53\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-20T05:39:21.611Z\"}, \"eval-vla-only-spatial-seed52\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-20T05:39:11.774Z\"}, \"eval-crm-goal-seed50\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-20T05:39:07.990Z\"}, \"eval-crm-goal-seed49\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-20T05:39:04.130Z\"}, \"eval-crm-long-seed52\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-20T05:39:00.914Z\"}, \"eval-vla-only-goal-seed52\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-20T05:17:00.091Z\"}, \"eval-vla-only-long-seed53\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-20T05:16:52.571Z\"}, \"eval-crm-long-seed51\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-20T05:16:49.496Z\"}, \"eval-vla-only-goal-seed50\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-20T05:16:42.496Z\"}, \"eval-crm-long-seed49\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-20T05:15:52.486Z\"}, \"eval-crm-long-seed48\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-20T05:15:50.831Z\"}, \"eval-crm-goal-seed48\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-20T05:15:47.607Z\"}, \"eval-crm-goal-seed47\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-20T04:33:38.995Z\"}, \"eval-crm-spatial-seed48\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-20T04:13:53.186Z\"}, \"eval-vla-only-spatial-seed51\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-20T03:12:40.851Z\"}, \"eval-adaptive-k-p25-seed42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T03:05:13.741Z\"}, \"eval-vla-only-goal-seed48-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T03:02:41.906Z\"}, \"eval-vla-only-goal-seed47-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T03:02:34.679Z\"}, \"eval-crm-goal-seed46\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T02:54:29.366Z\"}, \"eval-vla-only-object-seed51\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-20T02:43:30.806Z\"}, \"eval-vla-only-long-seed49\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-20T02:43:21.463Z\"}, \"eval-adaptive-k-p50-seed44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T02:40:24.520Z\"}, \"eval-adaptive-k-p75-seed44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T02:40:21.205Z\"}, \"eval-adaptive-k-p90-seed43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T02:40:15.747Z\"}, \"eval-adaptive-k-p90-seed42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T02:40:12.273Z\"}, \"eval-adaptive-k-p25-seed44\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-20T02:36:09.821Z\"}, \"eval-vla-only-spatial-seed47\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T01:39:25.709Z\"}, \"eval-crm-spatial-seed47\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-20T01:19:10.476Z\"}, \"eval-vla-only-object-seed49-r2\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-20T01:19:03.093Z\"}, \"eval-crm-long-seed47\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T00:21:06.698Z\"}, \"eval-vla-only-long-seed48\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T00:16:50.121Z\"}, \"eval-crm-long-seed46\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T00:13:08.430Z\"}, \"eval-crm-goal-seed45-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T00:11:46.069Z\"}, \"eval-crm-goal-seed44-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-20T00:11:07.345Z\"}, \"eval-obs-only-spatial-norm02-seed43-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T23:20:20.286Z\"}, \"k2-l2-calibration-phase1\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T22:38:04.117Z\"}, \"eval-crm-long-seed45\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T22:15:17.800Z\"}, \"eval-vla-only-spatial-seed49-r2\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-19T22:12:58.379Z\"}, \"eval-vla-only-spatial-seed49\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T22:12:05.406Z\"}, \"eval-vla-only-goal-seed48\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T22:08:08.414Z\"}, \"eval-vla-only-goal-seed43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T21:32:22.969Z\"}, \"eval-vla-only-goal-seed42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T21:32:21.219Z\"}, \"eval-vla-only-object-seed47\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T21:32:10.689Z\"}, \"eval-crm-long-seed44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T21:32:07.617Z\"}, \"eval-crm-long-seed43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T21:32:03.390Z\"}, \"eval-crm-long-seed42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T21:31:58.213Z\"}, \"eval-crm-goal-seed42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T21:22:37.560Z\"}, \"eval-crm-goal-seed43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T21:19:08.468Z\"}, \"eval-vla-only-spatial-seed46\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T21:15:20.345Z\"}, \"eval-vla-only-long-seed47\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T21:14:38.930Z\"}, \"eval-crm-goal-seed45\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T20:53:05.054Z\"}, \"eval-crm-goal-seed44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T20:52:09.464Z\"}, \"eval-vla-only-goal-seed45\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T20:10:50.847Z\"}, \"eval-vla-only-goal-seed46\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T20:08:19.990Z\"}, \"eval-vla-only-long-seed46\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T20:08:18.540Z\"}, \"fmvd-calibration-phase1\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T20:07:21.125Z\"}, \"eval-vla-only-long-seed45\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T19:21:47.544Z\"}, \"eval-perdof-object-norm003-seed47\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T19:05:12.052Z\"}, \"eval-perdof-object-norm005-seed47\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T19:05:09.001Z\"}, \"eval-vla-only-long-seed44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T18:38:52.937Z\"}, \"eval-vla-only-long-seed42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T18:38:48.009Z\"}, \"eval-vla-only-long-seed43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T18:33:56.305Z\"}, \"eval-obs-only-spatial-norm02-seed43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T18:07:05.998Z\"}, \"eval-obs-only-spatial-norm02-seed47\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T18:04:19.943Z\"}, \"eval-obs-only-spatial-norm02-seed46\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T17:24:14.391Z\"}, \"eval-argmin-object-k5-seed44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T17:24:12.993Z\"}, \"eval-vla-only-goal-seed44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T17:08:52.675Z\"}, \"eval-random-selection-object-k5-seed45-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T16:31:13.969Z\"}, \"eval-random-selection-object-k5-seed44-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T16:31:10.982Z\"}, \"eval-random-selection-object-k5-seed43-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T16:31:08.997Z\"}, \"eval-random-selection-object-k5-seed42-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T16:31:06.453Z\"}, \"eval-obs-only-spatial-norm02-k5-seed44-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T16:30:37.908Z\"}, \"eval-obs-only-spatial-norm02-k5-seed45-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T16:30:18.549Z\"}, \"plan_602-latency-profiling\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T16:17:38.007Z\"}, \"eval-vla-only-spatial-seed45\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T16:06:09.222Z\"}, \"eval-perdof-object-norm005-seed45-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T16:06:07.907Z\"}, \"eval-vla-only-spatial-seed44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T15:30:01.540Z\"}, \"eval-obs-only-object-default-seed48-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T14:58:17.531Z\"}, \"eval-vla-only-spatial-seed43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T14:43:19.646Z\"}, \"eval-vla-only-spatial-seed42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T14:38:29.599Z\"}, \"eval-obs-only-spatial-norm02-k5-seed45\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T14:32:21.490Z\"}, \"eval-obs-only-spatial-norm02-k5-seed44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T14:32:16.468Z\"}, \"eval-random-selection-object-k5-seed45\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T14:32:11.343Z\"}, \"eval-random-selection-object-k5-seed44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T14:32:06.313Z\"}, \"eval-random-selection-object-k5-seed43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T14:32:01.561Z\"}, \"eval-random-selection-object-k5-seed42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T14:31:56.882Z\"}, \"eval-obs-only-spatial-norm02-seed44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T14:26:11.536Z\"}, \"eval-perdof-object-norm01-seed43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T13:39:15.552Z\"}, \"eval-obs-only-object-default-seed45-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T13:35:23.895Z\"}, \"eval-argmin-object-k5-seed42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T13:30:16.050Z\"}, \"eval-argmin-object-k5-seed45\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T13:26:50.930Z\"}, \"eval-argmin-object-k5-seed43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T13:26:46.918Z\"}, \"eval-perdof-object-norm03-seed43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T13:24:40.192Z\"}, \"eval-obs-only-spatial-norm02-seed45\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T13:12:13.645Z\"}, \"train-crm-k1-accg-object-seed42-full\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T12:48:29.290Z\"}, \"plan_701-precompute-k1-spatial\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T12:48:27.021Z\"}, \"plan_701-crm-k1-train\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T12:48:10.176Z\"}, \"eval_obs_only_norm03_seed48\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T12:48:06.312Z\"}, \"eval_obs_only_norm01_seed48\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T12:48:03.869Z\"}, \"eval-lto-splitA-vla-only-r3\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T12:48:01.446Z\"}, \"eval-lto-splitA-vla-only-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T12:47:58.882Z\"}, \"eval-lto-splitA-heldout-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T12:47:56.312Z\"}, \"crm-lto-splitA-train\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T12:47:52.436Z\"}, \"eval-perdof-object-norm003-seed48\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T12:23:18.801Z\"}, \"eval-scalar-object-seed45-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T11:45:28.182Z\"}, \"eval-obs-only-spatial-norm02-k5-seed43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T11:34:16.077Z\"}, \"eval-obs-only-object-norm02-k5-seed48\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T11:34:12.397Z\"}, \"eval-obs-only-spatial-norm02-k5-seed42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T11:31:39.191Z\"}, \"eval-obs-only-object-norm02-k5-seed46\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T11:30:55.300Z\"}, \"eval-lto-splitA-vla-only-v2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T11:30:43.198Z\"}, \"eval-lto-splitA-heldout-v2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T11:30:33.951Z\"}, \"eval-perdof-object-default-seed47\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T11:30:18.282Z\"}, \"eval-perdof-object-norm03-seed47\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T11:30:17.012Z\"}, \"eval-obs-only-object-default-seed48\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T11:30:15.785Z\"}, \"eval-perdof-object-norm003-seed46\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T11:30:14.493Z\"}, \"eval-perdof-object-norm005-seed46\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T11:29:18.036Z\"}, \"eval-perdof-object-norm003-seed45\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T11:28:09.358Z\"}, \"eval-obs-only-object-norm02-k5-seed47\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T11:27:53.132Z\"}, \"eval-perdof-object-norm01-seed48\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T11:25:28.189Z\"}, \"eval-obs-only-object-default-seed47\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T11:25:18.480Z\"}, \"eval-perdof-object-norm03-seed46\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T11:25:13.541Z\"}, \"eval-obs-only-object-norm03-seed46\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T11:25:11.008Z\"}, \"eval-scalar-object-seed46\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T11:25:07.860Z\"}, \"eval-obs-only-object-norm003-seed45-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T05:16:02.877Z\"}, \"eval-lto-splitA-vla-only\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T05:13:20.212Z\"}, \"eval-lto-splitA-heldout\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T05:13:18.481Z\"}, \"eval-obs-only-object-norm005-seed46\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T04:58:44.483Z\"}, \"eval-perdof-object-norm03-seed48\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T04:58:40.993Z\"}, \"eval-obs-only-object-norm003-seed49\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T04:58:36.864Z\"}, \"crm-lto-splitA-train-fixed\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T04:32:49.103Z\"}, \"eval-obs-only-object-norm003-seed47\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T04:32:33.294Z\"}, \"eval-perdof-object-norm003-seed43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T03:28:52.476Z\"}, \"eval-perdof-object-norm005-seed43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T02:56:00.676Z\"}, \"eval-perdof-object-default-seed43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T01:44:05.704Z\"}, \"eval-perdof-object-default-seed45\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T01:38:34.712Z\"}, \"eval-obs-only-object-norm02-k5-seed45\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-19T01:33:59.345Z\"}, \"eval-perdof-object-norm005-seed45\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-18T21:55:07.741Z\"}, \"eval-obs-only-object-norm02-k5-seed44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-18T21:05:50.448Z\"}, \"eval-perdof-object-norm003-seed44-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-18T19:14:55.968Z\"}, \"eval-perdof-object-norm01-seed42\": {\"status\": \"DEPLOYED\", \"updated_at\": \"2026-05-18T18:53:10.563Z\"}, \"eval-obs-only-object-norm01-seed42\": {\"status\": \"DEPLOYED\", \"updated_at\": \"2026-05-18T18:53:09.494Z\"}, \"eval-obs-only-object-norm01-seed46-r3\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-18T16:48:10.654Z\"}, \"eval-perdof-object-norm005-seed44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-18T15:18:13.193Z\"}, \"eval-vla-only-object-seed45-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-18T14:17:30.462Z\"}, \"eval-obs-only-object-norm03-seed48\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-18T13:27:03.418Z\"}, \"eval-obs-only-object-norm02-k5-seed43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-18T12:39:30.555Z\"}, \"eval-perdof-object-norm01-seed42-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-18T12:33:45.335Z\"}, \"eval-obs-only-object-norm01-seed42-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-18T12:33:41.666Z\"}, \"eval-perdof-object-norm02-seed43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-18T10:56:45.558Z\"}, \"eval-perdof-object-norm01-seed46\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-18T07:05:38.605Z\"}, \"eval-obs-only-object-norm01-seed45\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-18T07:05:03.603Z\"}, \"eval-obs-only-object-norm02-k5-seed42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-18T07:05:02.646Z\"}, \"eval-perdof-object-default-seed46\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-18T07:05:01.672Z\"}, \"eval-perdof-object-default-seed44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-18T06:19:59.229Z\"}, \"eval-mag-perdof-norm02\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-18T05:54:22.364Z\"}, \"eval-acr-spatial-v4-scalar\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-18T05:54:21.341Z\"}, \"eval-acr-spatial-v4-small\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-18T05:54:20.300Z\"}, \"eval-acr-spatial-v4-obs-only-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-18T05:54:19.300Z\"}, \"eval-argmin-only-spatial\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-18T05:54:18.227Z\"}, \"eval-acr-spatial-v3\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-18T05:54:17.209Z\"}, \"eval-acr-object-v3\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-18T05:54:16.171Z\"}, \"eval-openvla-object-vla-only-seed42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-18T05:54:15.084Z\"}, \"eval-perdof-object-norm02-seed47\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-18T04:37:10.886Z\"}, \"eval-obs-only-object-norm02-seed48\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-18T03:04:35.124Z\"}, \"eval-obs-only-object-default-seed46\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-18T03:03:50.286Z\"}, \"eval-perdof-object-norm02-seed46\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-18T02:24:22.787Z\"}, \"eval-obs-only-object-norm01-seed46\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-18T01:01:03.202Z\"}, \"eval-obs-only-object-norm01-seed46-r2\": {\"status\": \"DEPLOYED\", \"updated_at\": \"2026-05-18T00:33:26.447Z\"}, \"mag_obs_only_norm01_seed47\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T23:47:05.521Z\"}, \"mag_obs_only_norm01_seed46\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T23:47:03.765Z\"}, \"eval-perdof-object-norm02-seed43-r3\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T23:17:06.378Z\"}, \"mag_perdof_norm02_seed43_r3\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T23:10:07.386Z\"}, \"eval-perdof-object-norm01-seed47-bjb1\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T23:00:33.671Z\"}, \"eval-openvla-object-vla-only-seed42-v2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T22:39:25.302Z\"}, \"eval-k1-crm-multiscale-object-seed44-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T21:14:35.625Z\"}, \"eval-k1-crm-multiscale-object-seed44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T21:02:09.738Z\"}, \"eval-k1-crm-multiscale-object-seed43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T21:02:08.069Z\"}, \"eval-k1-crm-multiscale-object-seed42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T21:02:06.052Z\"}, \"eval-perdof-object-norm01-seed46-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T21:01:12.153Z\"}, \"eval-k1-crm-multiscale-object-seed43-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T20:55:55.430Z\"}, \"eval-perdof-object-norm02-seed45-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T18:37:21.561Z\"}, \"eval-obs-only-object-norm005-seed43-r3\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T18:37:20.319Z\"}, \"plan_602-latency-profile\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T18:35:42.842Z\"}, \"train-crm-k1-accg-object-seed42-v2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T18:31:23.291Z\"}, \"eval-k1-crm-accg-object-seed44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T18:22:02.272Z\"}, \"eval-k1-crm-accg-object-seed43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T18:22:01.354Z\"}, \"eval-k1-crm-accg-object-seed42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T18:22:00.464Z\"}, \"eval-obs-only-object-default-seed45\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T17:32:15.936Z\"}, \"eval-scalar-object-seed45\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T17:29:34.723Z\"}, \"eval-perdof-object-norm02-seed45\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T17:03:14.729Z\"}, \"eval-perdof-object-norm02-seed44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T16:52:17.419Z\"}, \"train-crm-k1-accg-object-seed42-fallback\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T15:19:16.626Z\"}, \"train-crm-k1-accg-object-seed42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T14:53:10.162Z\"}, \"eval-perdof-object-norm02-seed45-deploy\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T13:52:58.983Z\"}, \"eval-obs-only-object-norm01-seed47-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T13:31:57.433Z\"}, \"eval-perdof-object-norm03-seed45-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T12:04:17.540Z\"}, \"eval-perdof-object-norm03-seed44-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T12:00:58.173Z\"}, \"eval-obs-only-object-norm03-seed47\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T11:50:09.879Z\"}, \"eval-perdof-object-norm03-seed46-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T11:36:55.536Z\"}, \"eval-perdof-object-norm01-seed44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T10:59:11.317Z\"}, \"eval-obs-only-object-norm01-seed47-bjb2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T10:56:41.892Z\"}, \"eval-obs-only-object-norm01-seed46-bjb2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T10:54:24.948Z\"}, \"eval-argmin-object-seed47\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T10:54:02.629Z\"}, \"eval-perdof-object-norm01-seed45\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T10:22:14.183Z\"}, \"eval-perdof-object-norm01-seed47\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T10:19:28.338Z\"}, \"eval-argmin-object-seed46\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T10:19:26.819Z\"}, \"eval-obs-only-object-norm03-seed45-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T07:02:49.285Z\"}, \"eval-vla-mean-object-seed45\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T06:54:28.933Z\"}, \"eval-argmin-object-seed45\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T06:53:28.467Z\"}, \"eval-direct-correction-object-seed42-r3\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T04:48:50.296Z\"}, \"eval-perdof-object-norm03-seed44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T04:45:11.458Z\"}, \"eval-mag-perdof-norm02-object\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:31:42.118Z\"}, \"eval-acr-object-v4-scalar\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:31:41.215Z\"}, \"eval-mag-obsonly-norm02\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:31:40.288Z\"}, \"eval-mag-perdof-norm03\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:31:39.344Z\"}, \"eval-mag-perdof-norm005\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:31:38.448Z\"}, \"eval-mag-perdof-norm003\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:31:37.673Z\"}, \"eval-vla-mean-spatial\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:15:31.664Z\"}, \"eval-acr-object-obs-only-norm02\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:15:28.368Z\"}, \"eval-spatial-v7-full\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:15:26.392Z\"}, \"eval-object-v8-full\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:15:25.342Z\"}, \"precompute-v5-shard2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:15:19.323Z\"}, \"precompute-v5-shard1\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:15:18.177Z\"}, \"precompute-v5-shard0\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:15:17.511Z\"}, \"precompute-v4-shard2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:15:16.391Z\"}, \"precompute-v4-shard1\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:15:15.362Z\"}, \"precompute-v4-shard0\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:15:14.415Z\"}, \"eval-vla-mean-spatial-t10\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:14:58.588Z\"}, \"eval-reconvla-spatial-v3\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:14:57.896Z\"}, \"crm-train-v2-scalar-unc\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:14:56.290Z\"}, \"crm-train-v2-perdof\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:14:55.328Z\"}, \"crm-train-v2-obs-only\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:14:53.940Z\"}, \"precompute-shard2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:13:50.200Z\"}, \"precompute-shard1\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:13:49.286Z\"}, \"precompute-shard0\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:13:43.682Z\"}, \"precompute-k5\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:13:41.787Z\"}, \"plan_014-reconvla-baseline\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:13:39.823Z\"}, \"plan_001-crm-smolvla\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:13:37.890Z\"}, \"mvp-point-reaching\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:13:35.534Z\"}, \"eval-smolvla-libero-spatial\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:13:33.197Z\"}, \"eval-obs-only-spatial\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:13:04.533Z\"}, \"eval-obs-only-object-default-seed44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:09:38.443Z\"}, \"eval-mag-perdof-norm005-object\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:09:30.045Z\"}, \"eval-mag-perdof-norm02-seed43-object-r3\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:09:27.225Z\"}, \"eval-mag-perdof-norm03-object-r3\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:09:17.332Z\"}, \"eval-mag-obsonly-norm005\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:09:15.263Z\"}, \"eval-mag-obsonly-norm003-b2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:09:11.273Z\"}, \"eval-mag-obsonly-norm03-object\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:09:10.586Z\"}, \"eval-mag-obsonly-norm005-object\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:09:06.864Z\"}, \"eval-direct-correction-object-seed42-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:04:54.543Z\"}, \"eval-direct-correction-object-seed42\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T02:38:55.611Z\"}, \"eval-scalar-object-seed44-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-16T21:29:49.586Z\"}, \"eval-perdof-object-seed44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-16T19:45:27.956Z\"}, \"eval-obs-only-object-norm03-seed44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-16T19:37:12.898Z\"}, \"eval-vla-mean-object-seed44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-16T18:36:08.965Z\"}, \"eval-obs-only-object-norm02-seed44-r4\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-16T15:36:08.207Z\"}, \"eval-argmin-object-seed44-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-16T15:34:00.414Z\"}, \"eval-obs-only-object-norm03-seed45\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-16T11:30:59.542Z\"}, \"eval-acr-object-v4-default-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-16T09:00:15.290Z\"}, \"eval-mag-perdof-norm003-object\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-16T08:37:12.296Z\"}, \"eval-acr-object-obs-only-default\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-16T07:09:01.967Z\"}, \"eval-scalar-object-seed43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-16T06:04:05.747Z\"}, \"eval-mag-obsonly-norm003-object\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-16T05:56:01.541Z\"}, \"eval-scalar-object-seed44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-16T05:25:06.306Z\"}, \"eval-obs-only-object-norm02-seed44-r3\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-16T04:59:20.094Z\"}, \"eval-argmin-object-seed44-r3\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-16T04:59:17.975Z\"}, \"eval-vla-mean-object-seed43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-16T04:53:17.141Z\"}, \"eval-perdof-object-seed43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-16T03:15:39.287Z\"}, \"eval-vla-only-object-seed44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-16T01:33:29.678Z\"}, \"eval-obs-only-object-norm02-seed44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-16T01:32:51.127Z\"}, \"eval-argmin-object-seed44\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-16T01:32:49.190Z\"}, \"eval-obs-only-object-seed43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-16T00:51:14.618Z\"}, \"eval-mag-obsonly-norm03-b2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-16T00:49:21.141Z\"}, \"eval-argmin-object-seed43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-16T00:37:43.289Z\"}, \"eval-mag-perdof-norm02-seed43-object-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:38:38.710Z\"}, \"eval-mag-obsonly-norm03\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:38:31.587Z\"}, \"eval-mag-obsonly-norm02-object\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:34:07.651Z\"}, \"eval-mag-obsonly-norm03-b4\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:27:30.465Z\"}, \"eval-mag-obsonly-norm03-b3\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:27:28.479Z\"}, \"eval-mag-perdof-norm02-seed43-object\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:25:28.957Z\"}, \"eval-mag-perdof-norm03-object-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:25:28.055Z\"}, \"eval-acr-object-v4-scalar-b2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:17:41.948Z\"}, \"eval-acr-object-v4-obs-only-b2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:17:40.199Z\"}, \"eval-spatial-v4-full\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:17:39.068Z\"}, \"eval-reconvla-spatial-v1\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:17:37.622Z\"}, \"eval-object-v6-full\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:17:36.369Z\"}, \"precompute-v3-shard2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:17:30.541Z\"}, \"precompute-v3-shard1\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:17:29.292Z\"}, \"precompute-v3-shard0\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:17:27.703Z\"}, \"precompute-v2-shard2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:17:26.396Z\"}, \"precompute-v2-shard1\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:17:25.022Z\"}, \"precompute-v2-shard0\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:17:23.631Z\"}, \"eval-mag-perdof-norm0p3-object-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:13:43.549Z\"}, \"eval-mag-perdof-norm0p3-object\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T18:58:11.790Z\"}, \"eval-obs-only-object-norm02-seed43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T18:58:10.821Z\"}, \"eval-acr-object-v4-default\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T17:38:37.815Z\"}, \"eval-mag-perdof-norm03-object\": {\"status\": \"DEPLOYED\", \"updated_at\": \"2026-05-15T17:38:28.909Z\"}, \"eval-mag-obsonly-norm03-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T17:22:51.755Z\"}, \"eval-vla-mean-object\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T17:01:25.883Z\"}, \"eval-reconvla-object\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T16:25:17.101Z\"}, \"eval-acr-object-v4-obs-only\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T16:23:01.718Z\"}, \"eval-acr-object-v4-perdof\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T15:45:38.531Z\"}, \"eval-acr-spatial-v4-scalar-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T13:18:27.852Z\"}, \"eval-acr-spatial-v4-obs-only-r3\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T11:15:11.801Z\"}, \"eval-obs-only-spatial-seed43\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T10:01:21.065Z\"}, \"eval-acr-spatial-v4-small-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T09:10:21.153Z\"}, \"eval-mag-obsonly-norm-0.3-r3\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T07:19:12.632Z\"}, \"eval-mag-obsonly-norm-0p3-r3\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T07:17:16.300Z\"}, \"eval-argmin-only-spatial-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T06:39:37.926Z\"}, \"eval-mag-obsonly-norm003\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T05:32:12.897Z\"}, \"eval-vla-only-object-k1\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T05:18:17.853Z\"}, \"eval-acr-spatial-v4-default-r3\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T03:30:05.911Z\"}, \"eval-tiny-correction-spatial\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T01:45:12.897Z\"}, \"eval-acr-spatial-v4-default-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:40:00.000Z\"}, \"eval-acr-spatial-v4-obs-only\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:16:05.788Z\"}, \"eval-acr-spatial-v4-default\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:08:58.490Z\"}, \"crm-train-v3-norm-scalar-unc\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:05:42.608Z\"}, \"crm-train-v3-norm-obs-only\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:05:28.289Z\"}, \"crm-train-v3-norm\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-14T20:05:22.677Z\"}, \"crm-train-v3-scalar-unc\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-14T18:37:14.400Z\"}, \"crm-train-v3-obs-only\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-14T18:37:04.316Z\"}, \"crm-train-v3-perdof\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-14T18:37:02.631Z\"}, \"eval-obs-only-spatial-v3\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-14T17:47:54.523Z\"}, \"eval-scalar-unc-spatial-v2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-14T17:47:53.188Z\"}, \"crm-train-a4-scalar-unc\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-14T07:59:32.676Z\"}, \"crm-train-a3-obs-only\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-14T07:59:31.277Z\"}, \"crm-train-v1\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-14T07:59:30.290Z\"}, \"crm-train-k5\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-14T07:59:29.396Z\"}, \"eval-scalar-unc-spatial\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-14T07:52:44.766Z\"}, \"eval-acr-spatial-v2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-14T07:52:43.327Z\"}, \"eval-k5-spatial\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-14T07:52:43.134Z\"}, \"eval-object-v7-full\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-14T01:45:48.892Z\"}, \"eval-spatial-v6-full\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-14T00:05:22.619Z\"}, \"eval-object-v5-full\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-14T00:04:26.792Z\"}, \"eval-acr-vla-spatial-v1\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-13T23:14:22.561Z\"}, \"eval-acr-spatial-v1\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-13T23:12:11.315Z\"}, \"eval-reconvla-spatial-v2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-13T23:12:10.958Z\"}, \"eval-object-v4-full\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-13T23:12:10.037Z\"}, \"eval-spatial-v5-full\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-13T23:12:09.066Z\"}, \"eval-spatial-v3-full\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-13T19:09:00.612Z\"}, \"eval-spatial-reeval-v2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-13T16:14:40.934Z\"}}, \"count\": 889, \"total\": 889, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.9881}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Bash · `toolu_01KJp5sB4GYf8uR3VpZQHAgD`</summary>

```json
{
  "command": "grep -iE \"lerobot\" /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/7b80dd05-6aec-4cda-b61a-b5ef1300a0d5/tool-results/mcp-agent-ml-research-read_registry-1779611072759.txt | head -30",
  "description": "Search for lerobot entries in registry dump"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "b24bd817-7738-4bad-8b10-e3c78fb954e0",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_015qUMomLsa5msGv2pG5b6a1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 714,
      "cache_read_input_tokens": 46624,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 714
      },
      "output_tokens": 62,
      "service_tier": "standard",
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

_source line 18 · 2026-05-24T08:24:37.202Z_

<details><summary>↩ Tool result · `toolu_01KJp5sB4GYf8uR3VpZQHAgD`</summary>

```text
&lt;persisted-output>
Output too large (92.7KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/7b80dd05-6aec-4cda-b61a-b5ef1300a0d5/tool-results/bubyyuomu.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-supp-long-k2mean-s46\": {\"status\": \"RUNNING\", \"updated_at\": \"2026-05-24T08:15:23.138Z\"}, \"eval-supp-long-crm-norm005-s46\": {\"status\": \"RUNNING\", \"updated_at\": \"2026-05-24T08:15:19.358Z\"}, \"eval-supp-long-reconvla-s46\": {\"status\": \"RUNNING\", \"updated_at\": \"2026-05-24T08:06:46.631Z\"}, \"eval-supp-long-adapt-tau025-s46\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T08:05:01.126Z\"}, \"eval-supp-k2mean-spatial-s47\": {\"status\": \"RUNNING\", \"updated_at\": \"2026-05-24T07:18:30.230Z\"}, \"eval-supp-reconvla-spatial-s47\": {\"status\": \"RUNNING\", \"updated_at\": \"2026-05-24T07:18:23.847Z\"}, \"eval-supp-adapt-tau025-spatial-s47\": {\"status\": \"RUNNING\", \"updated_at\": \"2026-05-24T07:18:17.441Z\"}, \"eval-supp-vla-only-spatial-s47\": {\"status\": \"RUNNING\", \"updated_at\": \"2026-05-24T07:18:10.979Z\"}, \"eval-supp-goal-vla-only-s47\": {\"status\": \"RUNNING\", \"updated_at\": \"2026-05-24T07:17:13.996Z\"}, \"eval-supp-long-vla-only-s47-r2\": {\"status\": \"RUNNING\", \"updated_at\": \"2026-05-24T07:17:06.584Z\"}, \"eval-supp-adapt-tau025-spatial-s46\": {\"status\": \"RUNNING\", \"updated_at\": \"2026-05-24T07:16:50.821Z\"}, \"eval-supp-crm-norm005-spatial-s46\": {\"status\": \"RUNNING\", \"updated_at\": \"2026-05-24T07:14:47.458Z\"}, \"crm-train-openvla-k1-multiscale-object\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T07:09:37.983Z\"}, \"eval-openvla-object-vla-only-seed42-v3\": {\"status\": \"RUNNING\", \"updated_at\": \"2026-05-24T07:08:07.984Z\"}, \"eval-supp-long-k2mean-s46-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T07:06:31.785Z\"}, \"eval-supp-long-reconvla-s46-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T07:06:23.946Z\"}, \"eval-supp-long-crm-norm005-s46-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T07:06:15.932Z\"}, \"eval-supp-long-adapt-tau025-s46-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-
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
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "7c092acf-6423-4067-ae0a-ad8a9ff62ddd",
  "tool_use_result": {
    "stdout": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"eval-supp-long-k2mean-s46\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"updated_at\\\": \\\"2026-05-24T08:15:23.138Z\\\"}, \\\"eval-supp-long-crm-norm005-s46\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"updated_at\\\": \\\"2026-05-24T08:15:19.358Z\\\"}, \\\"eval-supp-long-reconvla-s46\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"updated_at\\\": \\\"2026-05-24T08:06:46.631Z\\\"}, \\\"eval-supp-long-adapt-tau025-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-24T08:05:01.126Z\\\"}, \\\"eval-supp-k2mean-spatial-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"updated_at\\\": \\\"2026-05-24T07:18:30.230Z\\\"}, \\\"eval-supp-reconvla-spatial-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"updated_at\\\": \\\"2026-05-24T07:18:23.847Z\\\"}, \\\"eval-supp-adapt-tau025-spatial-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"updated_at\\\": \\\"2026-05-24T07:18:17.441Z\\\"}, \\\"eval-supp-vla-only-spatial-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"updated_at\\\": \\\"2026-05-24T07:18:10.979Z\\\"}, \\\"eval-supp-goal-vla-only-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"updated_at\\\": \\\"2026-05-24T07:17:13.996Z\\\"}, \\\"eval-supp-long-vla-only-s47-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"updated_at\\\": \\\"2026-05-24T07:17:06.584Z\\\"}, \\\"eval-supp-adapt-tau025-spatial-s46\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"updated_at\\\": \\\"2026-05-24T07:16:50.821Z\\\"}, \\\"eval-supp-crm-norm005-spatial-s46\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"updated_at\\\": \\\"2026-05-24T07:14:47.458Z\\\"}, \\\"crm-train-openvla-k1-multiscale-object\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-24T07:09:37.983Z\\\"}, \\\"eval-openvla-object-vla-only-seed42-v3\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"updated_at\\\": \\\"2026-05-24T07:08:07.984Z\\\"}, \\\"eval-supp-long-k2mean-s46-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-24T07:06:31.785Z\\\"}, \\\"eval-supp-long-reconvla-s46-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-24T07:06:23.946Z\\\"}, \\\"eval-supp-long-crm-norm005-s46-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-24T07:06:15.932Z\\\"}, \\\"eval-supp-long-adapt-tau025-s46-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-24T07:06:09.666Z\\\"}, \\\"eval-supp-long-vla-only-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"updated_at\\\": \\\"2026-05-24T07:05:36.964Z\\\"}, \\\"eval-supp-obj-crm-norm005-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-24T06:55:16.446Z\\\"}, \\\"eval-supp-long-crm-norm005-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"updated_at\\\": \\\"2026-05-24T06:53:16.695Z\\\"}, \\\"eval-supp-long-reconvla-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"updated_at\\\": \\\"2026-05-24T06:53:02.593Z\\\"}, \\\"eval-supp-spatial-crm-norm005-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"updated_at\\\": \\\"2026-05-24T06:51:27.049Z\\\"}, \\\"eval-supp-vla-only-spatial-s46\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"updated_at\\\": \\\"2026-05-24T06:50:52.276Z\\\"}, \\\"eval-supp-adapt-tau025-spatial-s45\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"updated_at\\\": \\\"2026-05-24T06:50:44.120Z\\\"}, \\\"eval-supp-crm-norm005-spatial-s45\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"updated_at\\\": \\\"2026-05-24T06:50:37.107Z\\\"}, \\\"eval-supp-vla-only-spatial-s45\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"updated_at\\\": \\\"2026-05-24T06:50:30.794Z\\\"}, \\\"eval-supp-obj-adapt-tau025-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-24T06:49:49.091Z\\\"}, \\\"eval-supp-obj-vla-only-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-24T06:49:36.626Z\\\"}, \\\"eval-supp-spatial-crm-norm005-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-24T06:45:22.337Z\\\"}, \\\"eval-supp-spatial-vla-only-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-24T06:45:16.646Z\\\"}, \\\"eval-supp-long-adapt-tau025-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"updated_at\\\": \\\"2026-05-24T06:38:39.651Z\\\"}, \\\"precompute-pi05-long-2048-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"updated_at\\\": \\\"2026-05-24T06:23:39.262Z\\\"}, \\\"precompute-pi05-goal-2048-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-24T06:23:35.000Z\\\"}, \\\"precompute-pi05-object-2048-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"updated_at\\\": \\\"2026-05-24T06:23:31.677Z\\\"}, \\\"eval-supp-long-vla-only-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-24T06:15:12.631Z\\\"}, \\\"precompute-pi05-spatial-2048-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-24T06:13:04.507Z\\\"}, \\\"precompute-smolvla-goal-bjb1-32546\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-24T05:44:03.369Z\\\"}, \\\"eval-supp-goal-vla-only-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-24T05:43:32.643Z\\\"}, \\\"eval-supp-goal-reconvla-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-24T05:43:26.502Z\\\"}, \\\"crm-train-pi05-spatial-full\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-24T03:28:46.242Z\\\"}, \\\"eval-obs-only-spatial-v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-24T03:27:16.008Z\\\"}, \\\"eval-perdof-object-norm003-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-24T03:27:10.816Z\\\"}, \\\"eval-random-selection-spatial-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-24T03:27:05.531Z\\\"}, \\\"eval-adaptive-k-spatial-p90-seed44-bjb2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-24T03:27:01.680Z\\\"}, \\\"eval-supp-goal-vla-only-wrapper-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-24T03:26:55.797Z\\\"}, \\\"eval-supp-long-reconvla-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-24T03:26:47.449Z\\\"}, \\\"eval-supp-spatial-k2mean-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-24T03:26:39.499Z\\\"}, \\\"eval-supp-obj-crm-norm005-s46\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"updated_at\\\": \\\"2026-05-24T03:26:33.701Z\\\"}, \\\"eval-pi05-vla-only-long-seed42-r4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-24T03:26:27.340Z\\\"}, \\\"eval-supp-reconvla-obj-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-24T03:26:15.872Z\\\"}, \\\"eval-pi05-vla-only-object-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-24T03:25:46.138Z\\\"}, \\\"eval-pi05-vla-only-object-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-24T03:25:36.173Z\\\"}, \\\"eval-pi05-vla-only-object-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-24T03:25:23.533Z\\\"}, \\\"eval-supp-long-k2mean-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-24T03:24:43.469Z\\\"}, \\\"eval-supp-goal-k2mean-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-24T03:24:33.666Z\\\"}, \\\"eval-supp-goal-adapt-tau025-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-24T03:24:30.058Z\\\"}, \\\"eval-supp-goal-crm-norm005-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-24T03:24:26.680Z\\\"}, \\\"eval-supp-spatial-adapt-tau025-s45-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-24T03:19:19.270Z\\\"}, \\\"eval-supp-spatial-k2mean-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-24T03:18:33.793Z\\\"}, \\\"eval-supp-spatial-vla-only-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-24T03:18:27.488Z\\\"}, \\\"eval-supp-spatial-reconvla-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-24T03:18:20.676Z\\\"}, \\\"eval-supp-spatial-adapt-tau025-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-24T03:18:17.471Z\\\"}, \\\"eval-supp-spatial-crm-norm005-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-24T03:18:14.133Z\\\"}, \\\"eval-supp-long-crm-norm005-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-24T00:54:53.307Z\\\"}, \\\"eval-supp-long-adapt-tau025-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-24T00:53:11.757Z\\\"}, \\\"eval-supp-long-vla-only-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-24T00:53:04.280Z\\\"}, \\\"eval-supp-spatial-reconvla-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-24T00:30:53.206Z\\\"}, \\\"eval-supp-goal-k2mean-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-24T00:21:09.215Z\\\"}, \\\"eval-supp-adapt-tau025-obj-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T23:45:46.677Z\\\"}, \\\"eval-supp-obj-k2mean-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T23:45:41.402Z\\\"}, \\\"eval-supp-crm-obj-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T23:43:24.974Z\\\"}, \\\"eval-supp-spatial-adapt-tau025-s45\\\": {\\\"status\\\": \\\"DEPLOYED\\\", \\\"updated_at\\\": \\\"2026-05-23T23:42:01.475Z\\\"}, \\\"eval-supp-long-k2mean-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T23:04:07.248Z\\\"}, \\\"eval-supp-long-reconvla-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T23:04:01.262Z\\\"}, \\\"eval-supp-k2mean-spatial-s45\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"updated_at\\\": \\\"2026-05-23T23:02:16.008Z\\\"}, \\\"eval-supp-goal-reconvla-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T22:57:24.122Z\\\"}, \\\"eval-supp-goal-vla-only-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T22:57:20.913Z\\\"}, \\\"eval-supp-crm-norm005-obj-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T22:57:13.555Z\\\"}, \\\"eval-supp-goal-crm-norm005-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T22:56:01.038Z\\\"}, \\\"eval-supp-crm-norm005-obj-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T22:37:07.655Z\\\"}, \\\"eval-supp-reconvla-obj-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T22:31:59.949Z\\\"}, \\\"eval-supp-goal-adapt-tau025-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T22:31:49.469Z\\\"}, \\\"eval-supp-long-crm-norm005-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T21:28:56.768Z\\\"}, \\\"eval-supp-long-adapt-tau025-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T21:28:50.765Z\\\"}, \\\"eval-supp-k2mean-obj-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T21:28:27.870Z\\\"}, \\\"eval-supp-k2mean-obj-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T21:28:21.695Z\\\"}, \\\"eval-supp-adapt-tau025-obj-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T20:26:37.804Z\\\"}, \\\"eval-supp-long-vla-only-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T20:21:04.060Z\\\"}, \\\"eval-supp-long-k2mean-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T20:13:10.758Z\\\"}, \\\"eval-supp-obj-vla-only-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T20:09:46.499Z\\\"}, \\\"eval-supp-long-vla-only-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T20:09:40.603Z\\\"}, \\\"eval-supp-long-k2mean-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T20:09:34.819Z\\\"}, \\\"eval-supp-long-reconvla-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T20:09:28.982Z\\\"}, \\\"eval-supp-long-crm-norm005-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T20:09:23.098Z\\\"}, \\\"eval-supp-long-adapt-tau025-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T20:09:17.172Z\\\"}, \\\"eval-supp-obj-adapt-tau025-s45-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T18:16:04.202Z\\\"}, \\\"eval-supp-long-crm-norm005-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T17:25:47.737Z\\\"}, \\\"eval-supp-long-adapt-tau025-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T17:25:41.523Z\\\"}, \\\"eval-supp-long-reconvla-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T17:25:32.561Z\\\"}, \\\"eval-ablation-tau040-goal-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T17:25:24.644Z\\\"}, \\\"eval-ablation-tau015-goal-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T17:25:15.441Z\\\"}, \\\"eval-supp-k2mean-object-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T17:25:06.995Z\\\"}, \\\"eval-ablation-tau010-goal-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T17:24:59.810Z\\\"}, \\\"eval-supp-obj-reconvla-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T17:24:48.531Z\\\"}, \\\"eval-supp-spatial-vla-only-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T17:22:10.552Z\\\"}, \\\"eval-supp-goal-vla-only-wrapper-s44-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T17:21:50.650Z\\\"}, \\\"eval-supp-k2mean-spatial-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T14:41:49.032Z\\\"}, \\\"eval-supp-spatial-vla-only-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T14:41:43.043Z\\\"}, \\\"eval-supp-k2mean-goal-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T14:21:57.954Z\\\"}, \\\"eval-supp-adapt-tau025-obj-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T14:21:51.978Z\\\"}, \\\"eval-supp-crm-norm005-obj-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T14:21:46.269Z\\\"}, \\\"eval-supp-goal-vla-only-wrapper-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T14:21:40.459Z\\\"}, \\\"eval-supp-long-vla-only-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T14:13:45.028Z\\\"}, \\\"eval-supp-goal-reconvla-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T13:25:45.095Z\\\"}, \\\"eval-supp-obj-reconvla-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T13:25:39.232Z\\\"}, \\\"eval-supp-crm-norm005-goal-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T13:25:33.374Z\\\"}, \\\"eval-supp-k2mean-object-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T11:53:35.791Z\\\"}, \\\"eval-supp-k2mean-goal-s42-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T11:49:21.426Z\\\"}, \\\"eval-supp-adapt-tau025-goal-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T11:33:49.855Z\\\"}, \\\"eval-supp-crm-norm005-obj-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T11:33:43.836Z\\\"}, \\\"eval-supp-adapt-tau025-goal-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T11:33:38.082Z\\\"}, \\\"eval-supp-crm-norm005-goal-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T11:33:32.430Z\\\"}, \\\"eval-supp-adapt-tau025-obj-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T11:33:25.089Z\\\"}, \\\"eval-supp-goal-reconvla-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T11:31:34.130Z\\\"}, \\\"eval-supp-k2mean-spatial-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T11:30:05.886Z\\\"}, \\\"eval-supp-reconvla-spatial-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T11:25:39.981Z\\\"}, \\\"eval-supp-reconvla-spatial-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T11:21:32.905Z\\\"}, \\\"eval-supp-k2mean-goal-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T11:20:45.445Z\\\"}, \\\"eval-supp-k2mean-object-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T10:48:56.855Z\\\"}, \\\"eval-supp-goal-adapt-tau025-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T10:47:49.735Z\\\"}, \\\"eval-supp-goal-crm005-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T10:27:32.365Z\\\"}, \\\"eval-supp-goal-reconvla-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T10:11:16.616Z\\\"}, \\\"train-crm-unified-4suite-r6\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T10:09:50.183Z\\\"}, \\\"eval-goal-vla-only-wrapper-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T10:09:44.401Z\\\"}, \\\"eval-supp-obj-adapt-tau025-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T10:05:16.143Z\\\"}, \\\"eval-supp-k2mean-spatial-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T09:40:16.419Z\\\"}, \\\"eval-supp-crm-norm005-spatial-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T08:56:25.513Z\\\"}, \\\"eval-supp-adapt-tau025-spatial-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T08:44:11.956Z\\\"}, \\\"eval-supp-reconvla-k2-spatial-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T08:36:38.221Z\\\"}, \\\"eval-supp-adapt-tau025-spatial-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T08:36:15.063Z\\\"}, \\\"eval-supp-crm-norm005-spatial-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T08:35:04.453Z\\\"}, \\\"eval-supp-k2mean-goal-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T08:29:52.019Z\\\"}, \\\"eval-supp-obj-adapt-s42-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T07:08:55.601Z\\\"}, \\\"eval-object-vla-only-wrapper-s44-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T07:08:49.478Z\\\"}, \\\"eval-object-vla-only-wrapper-s43-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T07:08:43.800Z\\\"}, \\\"eval-object-vla-only-wrapper-s42-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T07:08:33.647Z\\\"}, \\\"eval-supp-obj-reconvla-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T07:05:57.520Z\\\"}, \\\"eval-supp-obj-crm005-s42-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T06:40:03.190Z\\\"}, \\\"eval-supp-adapt-tau035-spatial-s42-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T06:20:31.236Z\\\"}, \\\"eval-supp-adapt-tau015-spatial-s42-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T06:16:30.800Z\\\"}, \\\"eval-supp-crm-norm02-spatial-s42-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T06:12:43.228Z\\\"}, \\\"eval-supp-adapt-tau025-spatial-s42-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T06:12:07.119Z\\\"}, \\\"eval-openvla-object-baseline-seed42-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T04:55:40.054Z\\\"}, \\\"eval-obs-only-object-norm02-seed55\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T04:55:15.323Z\\\"}, \\\"precompute-pi05-features-object\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T04:55:09.845Z\\\"}, \\\"precompute-smolvla-goal-shard2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T04:55:04.457Z\\\"}, \\\"precompute-smolvla-goal-shard1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T04:54:57.961Z\\\"}, \\\"precompute-smolvla-goal-shard0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T04:54:52.235Z\\\"}, \\\"eval-smolvla-long-seed2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T04:54:46.718Z\\\"}, \\\"eval-smolvla-long-seed1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T04:54:41.335Z\\\"}, \\\"eval-smolvla-long-seed0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T04:54:35.953Z\\\"}, \\\"eval-smolvla-crm-spatial-seed42-v1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T04:54:30.564Z\\\"}, \\\"eval-smolvla-crm-spatial-seed43-v1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T04:54:25.093Z\\\"}, \\\"eval-smolvla-crm-spatial-seed44-v1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T04:54:19.576Z\\\"}, \\\"eval-smolvla-crm-goal-seed42-v1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T04:54:14.038Z\\\"}, \\\"eval-smolvla-crm-goal-seed43-v1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T04:54:08.535Z\\\"}, \\\"eval-smolvla-crm-goal-seed44-v1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T04:50:29.455Z\\\"}, \\\"eval-supp-obj-adapt-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T04:50:22.494Z\\\"}, \\\"eval-crm-norm02-spatial-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T04:50:16.948Z\\\"}, \\\"eval-adaptive-tau015-spatial-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T04:50:11.299Z\\\"}, \\\"eval-adaptive-tau025-spatial-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T04:50:03.969Z\\\"}, \\\"eval-adaptive-tau035-spatial-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T04:49:53.623Z\\\"}, \\\"train-crm-unified-4suite-r5-resumed\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T04:32:30.777Z\\\"}, \\\"eval-object-vla-only-wrapper-s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T04:07:05.366Z\\\"}, \\\"eval-object-vla-only-wrapper-s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T04:06:59.994Z\\\"}, \\\"eval-object-vla-only-wrapper-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T04:06:54.695Z\\\"}, \\\"eval-supp-obj-crm005-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T04:06:49.393Z\\\"}, \\\"eval-supp-adapt-tau035-spatial-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T04:06:43.867Z\\\"}, \\\"eval-supp-adapt-tau025-spatial-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T04:06:38.592Z\\\"}, \\\"eval-supp-adapt-tau015-spatial-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T04:06:33.197Z\\\"}, \\\"eval-supp-crm-norm02-spatial-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T04:06:27.722Z\\\"}, \\\"eval-3dir-adaptive-spatial-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T03:54:21.349Z\\\"}, \\\"eval-3dir-norm03-spatial-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T03:53:00.389Z\\\"}, \\\"eval-3dir-reconvla-spatial-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T03:52:57.581Z\\\"}, \\\"eval-3dir-norm01-spatial-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T03:52:54.819Z\\\"}, \\\"eval-3dir-norm005-spatial-s42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T03:52:51.544Z\\\"}, \\\"precompute-pi05-goal-2048\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T03:39:47.719Z\\\"}, \\\"precompute-pi05-spatial-2048\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T03:39:37.428Z\\\"}, \\\"precompute-pi05-object-2048\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T03:39:26.989Z\\\"}, \\\"eval-smolvla-crm-object-seed43-v1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T03:35:03.670Z\\\"}, \\\"eval-smolvla-crm-object-seed42-v1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T03:35:00.107Z\\\"}, \\\"eval-smolvla-crm-object-seed44-v1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T03:31:27.072Z\\\"}, \\\"train-crm-unified-4suite-r5\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T01:33:47.618Z\\\"}, \\\"eval-smolvla-crm-goal-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T01:33:43.543Z\\\"}, \\\"eval-smolvla-crm-goal-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T01:33:35.873Z\\\"}, \\\"eval-smolvla-crm-spatial-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T01:33:30.489Z\\\"}, \\\"eval-smolvla-crm-spatial-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T01:33:22.750Z\\\"}, \\\"eval-smolvla-crm-spatial-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-23T01:33:14.831Z\\\"}, \\\"eval-smolvla-crm-goal-seed44\\\": {\\\"status\\\": \\\"PENDING\\\", \\\"updated_at\\\": \\\"2026-05-22T23:26:30.844Z\\\"}, \\\"precompute-pi05-long-2048\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T23:24:07.545Z\\\"}, \\\"eval-smolvla-lerobot-goal-seed44-v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T23:18:08.524Z\\\"}, \\\"eval-smolvla-lerobot-goal-seed43-v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T23:17:55.201Z\\\"}, \\\"eval-smolvla-lerobot-spatial-seed43-v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T23:17:49.796Z\\\"}, \\\"train-crm-smolvla-3suite-v1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T23:11:45.218Z\\\"}, \\\"eval-smolvla-lerobot-goal-seed43-v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T20:50:32.835Z\\\"}, \\\"eval-smolvla-lerobot-spatial-seed43-v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T20:50:27.156Z\\\"}, \\\"eval-smolvla-lerobot-object-seed44-v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T20:50:21.831Z\\\"}, \\\"eval-smolvla-lerobot-object-seed43-v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T20:50:16.518Z\\\"}, \\\"eval-smolvla-lerobot-goal-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T20:13:51.786Z\\\"}, \\\"eval-smolvla-lerobot-spatial-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T20:13:46.670Z\\\"}, \\\"eval-smolvla-lerobot-object-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T20:13:40.397Z\\\"}, \\\"eval-smolvla-lerobot-object-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T20:13:33.516Z\\\"}, \\\"eval-smolvla-lerobot-spatial-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T20:12:30.387Z\\\"}, \\\"precompute-smolvla-long-wrapper-bjb1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T19:05:54.572Z\\\"}, \\\"eval-smolvla-lerobot-goal-seed44\\\": {\\\"status\\\": \\\"QUEUED\\\", \\\"updated_at\\\": \\\"2026-05-22T19:02:22.376Z\\\"}, \\\"eval-smolvla-lerobot-long-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T18:46:08.623Z\\\"}, \\\"eval-smolvla-lerobot-long-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T18:46:05.996Z\\\"}, \\\"eval-smolvla-lerobot-long-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T18:46:03.386Z\\\"}, \\\"train-crm-unified-4suite-r4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T18:14:09.706Z\\\"}, \\\"eval-pi05-vla-only-long-seed42-r4-rerun\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T18:12:13.396Z\\\"}, \\\"eval-pi05-crm-object-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T17:20:46.002Z\\\"}, \\\"eval-pi05-crm-object-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T17:20:35.256Z\\\"}, \\\"eval-pi05-crm-object-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T17:20:24.929Z\\\"}, \\\"eval-pi05-vla-only-long-seed43-r4-std\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T17:17:06.116Z\\\"}, \\\"eval-pi05-vla-only-goal-seed44-r4-std\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T17:16:24.608Z\\\"}, \\\"eval-pi05-vla-only-goal-seed42-r4-std\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T17:16:00.966Z\\\"}, \\\"eval-pi05-vla-only-long-seed44-r4-std\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T17:15:55.404Z\\\"}, \\\"eval-pi05-vla-only-goal-seed43-r4-std\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T17:14:50.393Z\\\"}, \\\"eval-pi05-vla-only-goal-seed42-r4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T17:02:13.462Z\\\"}, \\\"precompute-smolvla-long-k2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T17:01:57.058Z\\\"}, \\\"train-crm-unified-4suite-r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T17:00:24.406Z\\\"}, \\\"train-crm-unified-4suite-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T17:00:17.793Z\\\"}, \\\"precompute-smolvla-goal-bjb2-28827\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T17:00:10.097Z\\\"}, \\\"precompute-smolvla-long-bjb2-28827\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T17:00:02.382Z\\\"}, \\\"eval-pi05-vla-only-spatial-seed44-r4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T16:59:56.882Z\\\"}, \\\"eval-pi05-vla-only-spatial-seed43-r4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T16:59:51.541Z\\\"}, \\\"eval-pi05-vla-only-spatial-seed42-r4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T16:59:46.047Z\\\"}, \\\"eval-pi05-vla-only-long-seed44-r4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T16:43:05.868Z\\\"}, \\\"eval-pi05-vla-only-long-seed43-r4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T16:42:49.732Z\\\"}, \\\"eval-pi05-vla-only-goal-seed44-r4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T16:23:50.003Z\\\"}, \\\"eval-pi05-vla-only-goal-seed43-r4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T16:23:41.572Z\\\"}, \\\"eval-pi05-vla-only-long-seed42-r4-std\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"updated_at\\\": \\\"2026-05-22T16:17:13.985Z\\\"}, \\\"precompute-smolvla-goal-k10\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"updated_at\\\": \\\"2026-05-22T15:48:27.660Z\\\"}, \\\"precompute-smolvla-spatial-k10\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"updated_at\\\": \\\"2026-05-22T15:48:13.210Z\\\"}, \\\"precompute-smolvla-object-k10\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"updated_at\\\": \\\"2026-05-22T15:47:41.690Z\\\"}, \\\"eval-vla-only-long-seed2\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"updated_at\\\": \\\"2026-05-22T14:19:49.215Z\\\"}, \\\"eval-vla-only-long-seed1\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"updated_at\\\": \\\"2026-05-22T14:19:43.184Z\\\"}, \\\"eval-vla-only-long-seed0\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"updated_at\\\": \\\"2026-05-22T14:19:38.265Z\\\"}, \\\"eval-openvla-oft-official-object\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T13:24:23.378Z\\\"}, \\\"eval-pi05-crm-spatial-seed44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T13:24:17.309Z\\\"}, \\\"eval-pi05-crm-spatial-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T13:24:14.018Z\\\"}, \\\"eval-pi05-crm-spatial-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T13:24:09.791Z\\\"}, \\\"eval-pi05-vla-only-object-seed43-r4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T11:55:13.893Z\\\"}, \\\"eval-pi05-vla-only-object-seed44-r4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T11:51:23.505Z\\\"}, \\\"eval-smolvla-lerobot-official-object\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T11:33:17.264Z\\\"}, \\\"eval-pi05-vla-only-object-seed42-r4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T11:26:20.250Z\\\"}, \\\"train-crm-unified-4suite\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T11:18:23.000Z\\\"}, \\\"precompute-smolvla-long-bjb1-32546-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T11:15:49.784Z\\\"}, \\\"precompute-smolvla-long-bjb1-32546\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T11:11:37.983Z\\\"}, \\\"eval-loss-perdof-object-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T10:51:37.131Z\\\"}, \\\"eval-loss-combined-object-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T10:41:20.547Z\\\"}, \\\"eval-loss-conformal-object-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T10:40:44.234Z\\\"}, \\\"eval-loss-mse-object-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T10:26:08.383Z\\\"}, \\\"eval-openvla-oft-object-baseline-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T09:00:45.065Z\\\"}, \\\"precompute-pi05-long-bjb1-18228\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"updated_at\\\": \\\"2026-05-22T09:00:18.250Z\\\"}, \\\"precompute-smolvla-long-bjb1-18228\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T08:56:52.782Z\\\"}, \\\"precompute-pi05-goal-bjb2-28827-s2\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"updated_at\\\": \\\"2026-05-22T08:03:27.743Z\\\"}, \\\"precompute-pi05-goal-bjb2-28827-s1\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"updated_at\\\": \\\"2026-05-22T08:03:23.271Z\\\"}, \\\"precompute-pi05-goal-bjb2-28827-s0\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"updated_at\\\": \\\"2026-05-22T08:03:18.741Z\\\"}, \\\"crm-loss-combined\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T07:39:25.644Z\\\"}, \\\"crm-loss-conformal\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T07:37:31.142Z\\\"}, \\\"precompute-smolvla-goal-bjb1-18228\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T07:33:35.175Z\\\"}, \\\"crm-loss-perdof\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T06:35:46.165Z\\\"}, \\\"crm-loss-mse-baseline\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T06:32:42.169Z\\\"}, \\\"eval-smolvla-acr-goal-seed43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T05:56:00.921Z\\\"}, \\\"eval-smolvla-crm-long-seed44-v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T05:55:17.088Z\\\"}, \\\"eval-smolvla-crm-goal-seed44-v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T05:55:10.553Z\\\"}, \\\"eval-smolvla-crm-long-seed43-v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T05:55:03.970Z\\\"}, \\\"eval-smolvla-acr-long-seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T05:54:52.777Z\\\"}, \\\"eval-smolvla-acr-goal-se",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false,
    "persistedOutputPath": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/7b80dd05-6aec-4cda-b61a-b5ef1300a0d5/tool-results/bubyyuomu.txt",
    "persistedOutputSize": 94908
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Grep · `toolu_01AdKAfGGGsVrxXMDmz2Uh58`</summary>

```json
{
  "pattern": "lerobot",
  "path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/7b80dd05-6aec-4cda-b61a-b5ef1300a0d5/tool-results/mcp-agent-ml-research-read_registry-1779611072759.txt",
  "output_mode": "content",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "00dc2ed3-a238-465a-adaf-45e3a1bfcb6a",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01FGxRSz1gcm5cGkS3YwMbjp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1608,
      "cache_read_input_tokens": 47338,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1608
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

_source line 20 · 2026-05-24T08:24:44.803Z_

<details><summary>↩ Tool result · `toolu_01AdKAfGGGsVrxXMDmz2Uh58`</summary>

```text
1:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "d224ed6d-4001-4eba-869d-7b2633f06038",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "1:[Omitted long matching line]",
    "numLines": 1
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Bash · `toolu_01HYgN3eFnYn6XkTQHWXjYvw`</summary>

```json
{
  "command": "grep -oE '\"[^\"]*lerobot[^\"]*\"' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/7b80dd05-6aec-4cda-b61a-b5ef1300a0d5/tool-results/mcp-agent-ml-research-read_registry-1779611072759.txt | sort -u | head -50",
  "description": "Find all lerobot-related exp IDs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "71bb920b-3dd4-4e86-bc2c-da7cb76b2bf2",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01LfnQAaH4H99podGAyNRb7n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 283,
      "cache_read_input_tokens": 48946,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 283
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

_source line 22 · 2026-05-24T08:24:48.484Z_

<details><summary>↩ Tool result · `toolu_01HYgN3eFnYn6XkTQHWXjYvw`</summary>

```text
"eval-smolvla-lerobot-goal-seed43-v2\"
"eval-smolvla-lerobot-goal-seed43-v3\"
"eval-smolvla-lerobot-goal-seed43\"
"eval-smolvla-lerobot-goal-seed44-v3\"
"eval-smolvla-lerobot-goal-seed44\"
"eval-smolvla-lerobot-long-seed42\"
"eval-smolvla-lerobot-long-seed43\"
"eval-smolvla-lerobot-long-seed44\"
"eval-smolvla-lerobot-object-seed43-v2\"
"eval-smolvla-lerobot-object-seed43\"
"eval-smolvla-lerobot-object-seed44-v2\"
"eval-smolvla-lerobot-object-seed44\"
"eval-smolvla-lerobot-official-object\"
"eval-smolvla-lerobot-spatial-seed43-v2\"
"eval-smolvla-lerobot-spatial-seed43-v3\"
"eval-smolvla-lerobot-spatial-seed43\"
"eval-smolvla-lerobot-spatial-seed44\"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "3ca05b0d-dee6-4ed8-a7d0-a2bf6955ffb3",
  "tool_use_result": {
    "stdout": "\"eval-smolvla-lerobot-goal-seed43-v2\\\"\n\"eval-smolvla-lerobot-goal-seed43-v3\\\"\n\"eval-smolvla-lerobot-goal-seed43\\\"\n\"eval-smolvla-lerobot-goal-seed44-v3\\\"\n\"eval-smolvla-lerobot-goal-seed44\\\"\n\"eval-smolvla-lerobot-long-seed42\\\"\n\"eval-smolvla-lerobot-long-seed43\\\"\n\"eval-smolvla-lerobot-long-seed44\\\"\n\"eval-smolvla-lerobot-object-seed43-v2\\\"\n\"eval-smolvla-lerobot-object-seed43\\\"\n\"eval-smolvla-lerobot-object-seed44-v2\\\"\n\"eval-smolvla-lerobot-object-seed44\\\"\n\"eval-smolvla-lerobot-official-object\\\"\n\"eval-smolvla-lerobot-spatial-seed43-v2\\\"\n\"eval-smolvla-lerobot-spatial-seed43-v3\\\"\n\"eval-smolvla-lerobot-spatial-seed43\\\"\n\"eval-smolvla-lerobot-spatial-seed44\\\"",
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

_source line 23_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "650cc8df-90d1-44f0-a187-803c52bec221",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01CGnAUmvVV9zgGs76feDHyW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 670,
      "cache_read_input_tokens": 49229,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 670
      },
      "output_tokens": 33,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Bash · `toolu_019DYkSF22aQzaC6V7wwm5u8`</summary>

```json
{
  "command": "grep -oE '\"eval-smolvla-lerobot-[^\"]+\":\\s*\\{[^}]+\\}' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/7b80dd05-6aec-4cda-b61a-b5ef1300a0d5/tool-results/mcp-agent-ml-research-read_registry-1779611072759.txt | grep -E \"seed43-v3|spatial-seed43-v3|goal-seed43-v3\"",
  "description": "Find status of stale lerobot exps"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "eeda1d7b-6dce-4161-91db-fc870f8fffb9",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01CGnAUmvVV9zgGs76feDHyW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 670,
      "cache_read_input_tokens": 49229,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 670
      },
      "output_tokens": 33,
      "service_tier": "standard",
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

_source line 25 · 2026-05-24T08:24:58.624Z_

<details><summary>↩ Tool result · `toolu_019DYkSF22aQzaC6V7wwm5u8`</summary>

```text
"eval-smolvla-lerobot-goal-seed43-v3\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T23:17:55.201Z\"}
"eval-smolvla-lerobot-spatial-seed43-v3\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T23:17:49.796Z\"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "dc55309c-725a-434f-9bc0-95fd20e401bc",
  "tool_use_result": {
    "stdout": "\"eval-smolvla-lerobot-goal-seed43-v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T23:17:55.201Z\\\"}\n\"eval-smolvla-lerobot-spatial-seed43-v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T23:17:49.796Z\\\"}",
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

_source line 26_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "04af0684-15eb-4e11-b620-53e77b8e1a93",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Xd8B2YyQhuT8cehYbosf3d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 611,
      "cache_read_input_tokens": 49899,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 611
      },
      "output_tokens": 60,
      "service_tier": "standard",
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

_source line 27_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_011FcMcW5RZUUoKgTtXCGh2M`</summary>

```json
{
  "filters": {
    "exp_id": [
      "eval-smolvla-lerobot-goal-seed43-v3",
      "eval-smolvla-lerobot-spatial-seed43-v3"
    ]
  },
  "project": "acr-vla-conformal-refinement",
  "fields": [
    "exp_id",
    "status",
    "conclusion",
    "metrics",
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
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "cb8e4be9-9c1b-442b-a9d5-c035e71a9a8f",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Xd8B2YyQhuT8cehYbosf3d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 611,
      "cache_read_input_tokens": 49899,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 611
      },
      "output_tokens": 60,
      "service_tier": "standard",
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

_source line 28 · 2026-05-24T08:25:08.537Z_

<details><summary>↩ Tool result · `toolu_011FcMcW5RZUUoKgTtXCGh2M`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.9547}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "a4866278-fb4f-4131-ad7d-c4320beb8e21",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.9547}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.9547}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01UidnRkAYJ41awVLMECpp3n`</summary>

```json
{
  "query": "select:TodoWrite",
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
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "65a67385-503c-4178-8ca3-b1d4e86693b7",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01HKKtxkq5QaSQMXKjs1mUGK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 610,
      "cache_read_input_tokens": 50510,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 610
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

_source line 30 · 2026-05-24T08:25:11.527Z_

<details><summary>↩ Tool result · `toolu_01UidnRkAYJ41awVLMECpp3n`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "TodoWrite"
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
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "5ae8f1ae-0ec2-4386-9b49-9ee3979b952d",
  "tool_use_result": {
    "matches": [
      "TodoWrite"
    ],
    "query": "select:TodoWrite",
    "total_deferred_tools": 26
  }
}
```

</details>

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_019DdUSkmredYxA4mjRQ7UmJ`</summary>

```json
{
  "todos": [
    {
      "content": "Confirm two lerobot exps already DONE — re-verify status",
      "activeForm": "Confirming lerobot exps status",
      "status": "in_progress"
    },
    {
      "content": "Check 5 Spatial exp processes on bjb2-28827",
      "activeForm": "Checking Spatial processes on bjb2-28827",
      "status": "pending"
    },
    {
      "content": "For each completed Spatial exp: harvest SR from JSON",
      "activeForm": "Harvesting SR from completed JSONs",
      "status": "pending"
    },
    {
      "content": "Report status/results to user",
      "activeForm": "Reporting results",
      "status": "pending"
    }
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
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "63a710ca-851b-4c74-a4ee-b9502bc17830",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01FXL8AZqK7S9UkeZKWhdFzJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 3512,
      "cache_read_input_tokens": 51120,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3512
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

_source line 32 · 2026-05-24T08:25:18.208Z_

<details><summary>↩ Tool result · `toolu_019DdUSkmredYxA4mjRQ7UmJ`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "41a297e8-6eff-4d8d-9460-fa52055d7b68",
  "tool_use_result": {
    "oldTodos": [],
    "newTodos": [
      {
        "content": "Confirm two lerobot exps already DONE — re-verify status",
        "status": "in_progress",
        "activeForm": "Confirming lerobot exps status"
      },
      {
        "content": "Check 5 Spatial exp processes on bjb2-28827",
        "status": "pending",
        "activeForm": "Checking Spatial processes on bjb2-28827"
      },
      {
        "content": "For each completed Spatial exp: harvest SR from JSON",
        "status": "pending",
        "activeForm": "Harvesting SR from completed JSONs"
      },
      {
        "content": "Report status/results to user",
        "status": "pending",
        "activeForm": "Reporting results"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — Bash · `toolu_01SC3nhUFcCB6RiiYiL6RXq5`</summary>

```json
{
  "command": "grep -oE '\"eval-smolvla-lerobot-(goal|spatial)-seed43-v3\"[^}]*\\}' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/7b80dd05-6aec-4cda-b61a-b5ef1300a0d5/tool-results/mcp-agent-ml-research-read_registry-1779611072759.txt",
  "description": "Confirm status of the two lerobot exps from saved dump"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "f695d2c6-ffa9-425d-8208-f7d83a3f87aa",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01FJ9zFqgoMzgoPMR43VZrwC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 345,
      "cache_read_input_tokens": 54632,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 345
      },
      "output_tokens": 47,
      "service_tier": "standard",
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

_source line 34 · 2026-05-24T08:25:31.488Z_

<details><summary>↩ Tool result · `toolu_01SC3nhUFcCB6RiiYiL6RXq5`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "d549b088-7c75-4a19-83c7-9faa2372434f",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "returnCodeInterpretation": "No matches found",
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — Bash · `toolu_01SPguLcTrcvG1YPfYE2GEqr`</summary>

```json
{
  "command": "grep -oE '\"eval-smolvla-lerobot-[a-z]+-seed43-v3\\\\?\": \\{[^}]+\\}' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/7b80dd05-6aec-4cda-b61a-b5ef1300a0d5/tool-results/mcp-agent-ml-research-read_registry-1779611072759.txt",
  "description": "Find the seed43-v3 lerobot records"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "939bf9d2-0a90-450b-999a-4be928206744",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01XGHhM8WAW9Ywo2jLrzu9MR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 292,
      "cache_read_input_tokens": 54977,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 292
      },
      "output_tokens": 68,
      "service_tier": "standard",
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

_source line 36 · 2026-05-24T08:25:35.724Z_

<details><summary>↩ Tool result · `toolu_01SPguLcTrcvG1YPfYE2GEqr`</summary>

```text
"eval-smolvla-lerobot-goal-seed43-v3\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T23:17:55.201Z\"}
"eval-smolvla-lerobot-spatial-seed43-v3\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-22T23:17:49.796Z\"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "3a6c0191-3f4d-4a1d-af4b-c2011b2a69d5",
  "tool_use_result": {
    "stdout": "\"eval-smolvla-lerobot-goal-seed43-v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T23:17:55.201Z\\\"}\n\"eval-smolvla-lerobot-spatial-seed43-v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-22T23:17:49.796Z\\\"}",
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

_source line 37_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "f0091bc1-005f-47d8-8c1e-ee8ae26e93d8",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01WYSqsuQNBuhNimfwQ7mxNw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 417,
      "cache_read_input_tokens": 55269,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 417
      },
      "output_tokens": 51,
      "service_tier": "standard",
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

_source line 38_

Both lerobot exps are already DONE in the registry (updated 2026-05-22). Task 1 has no work needed — they were finalized previously. Moving to Task 2.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "62d8d576-e72e-4e46-bb14-efc0d9b2c94b",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01WYSqsuQNBuhNimfwQ7mxNw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 417,
      "cache_read_input_tokens": 55269,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 417
      },
      "output_tokens": 51,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01Ro1c5dsVY1jQkPhsoH5Vta`</summary>

```json
{
  "todos": [
    {
      "content": "Confirm two lerobot exps already DONE — re-verify status",
      "activeForm": "Confirming lerobot exps status",
      "status": "completed"
    },
    {
      "content": "Check 5 Spatial exp processes on bjb2-28827",
      "activeForm": "Checking Spatial processes on bjb2-28827",
      "status": "in_progress"
    },
    {
      "content": "For each completed Spatial exp: harvest SR from JSON",
      "activeForm": "Harvesting SR from completed JSONs",
      "status": "pending"
    },
    {
      "content": "Report status/results to user",
      "activeForm": "Reporting results",
      "status": "pending"
    }
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
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "78e7798c-99ac-4665-b66b-bcd727f0a847",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01WYSqsuQNBuhNimfwQ7mxNw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 417,
      "cache_read_input_tokens": 55269,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 417
      },
      "output_tokens": 51,
      "service_tier": "standard",
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

_source line 40 · 2026-05-24T08:25:48.368Z_

<details><summary>↩ Tool result · `toolu_01Ro1c5dsVY1jQkPhsoH5Vta`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "b0f45b83-0825-42ea-bbc7-a6dea1386868",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Confirm two lerobot exps already DONE — re-verify status",
        "status": "in_progress",
        "activeForm": "Confirming lerobot exps status"
      },
      {
        "content": "Check 5 Spatial exp processes on bjb2-28827",
        "status": "pending",
        "activeForm": "Checking Spatial processes on bjb2-28827"
      },
      {
        "content": "For each completed Spatial exp: harvest SR from JSON",
        "status": "pending",
        "activeForm": "Harvesting SR from completed JSONs"
      },
      {
        "content": "Report status/results to user",
        "status": "pending",
        "activeForm": "Reporting results"
      }
    ],
    "newTodos": [
      {
        "content": "Confirm two lerobot exps already DONE — re-verify status",
        "status": "completed",
        "activeForm": "Confirming lerobot exps status"
      },
      {
        "content": "Check 5 Spatial exp processes on bjb2-28827",
        "status": "in_progress",
        "activeForm": "Checking Spatial processes on bjb2-28827"
      },
      {
        "content": "For each completed Spatial exp: harvest SR from JSON",
        "status": "pending",
        "activeForm": "Harvesting SR from completed JSONs"
      },
      {
        "content": "Report status/results to user",
        "status": "pending",
        "activeForm": "Reporting results"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01TfdBGU9LronnTCrSfawab8`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "ps -p 121241,96831,97307,97070,97550 -o pid=,etime=,stat=,cmd=",
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
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "a2ee0586-c3da-4862-b647-6a013496db9d",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_018pjsaHgdu1sfZMkCLi5JPG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 522,
      "cache_read_input_tokens": 55686,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 522
      },
      "output_tokens": 47,
      "service_tier": "standard",
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

_source line 42 · 2026-05-24T08:25:54.493Z_

<details><summary>↩ Tool result · `toolu_01TfdBGU9LronnTCrSfawab8`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \" 96831    01:34:42 Rl+  python -u src/evaluate.py --benchmark spatial --mode vla_only --seed 45 --n_rollouts 20 --K 1\\n 97070    01:34:39 Rl+  python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 45 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\n 97307    01:34:36 Rl+  python -u src/evaluate.py --benchmark spatial --mode adaptive_conformal_crm --seed 45 --n_rollouts 20 --K 10 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\n 97550    01:34:33 Rl+  python -u src/evaluate.py --benchmark spatial --mode vla_only --seed 46 --n_rollouts 20 --K 1\\n121241    01:11:08 Rl+  python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 46 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.91}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "203d36a4-e033-478f-b0c3-b8958d7f3b01",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\" 96831    01:34:42 Rl+  python -u src/evaluate.py --benchmark spatial --mode vla_only --seed 45 --n_rollouts 20 --K 1\\\\n 97070    01:34:39 Rl+  python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 45 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\\n 97307    01:34:36 Rl+  python -u src/evaluate.py --benchmark spatial --mode adaptive_conformal_crm --seed 45 --n_rollouts 20 --K 10 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\\n 97550    01:34:33 Rl+  python -u src/evaluate.py --benchmark spatial --mode vla_only --seed 46 --n_rollouts 20 --K 1\\\\n121241    01:11:08 Rl+  python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 46 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.91}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \" 96831    01:34:42 Rl+  python -u src/evaluate.py --benchmark spatial --mode vla_only --seed 45 --n_rollouts 20 --K 1\\n 97070    01:34:39 Rl+  python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 45 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\n 97307    01:34:36 Rl+  python -u src/evaluate.py --benchmark spatial --mode adaptive_conformal_crm --seed 45 --n_rollouts 20 --K 10 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\n 97550    01:34:33 Rl+  python -u src/evaluate.py --benchmark spatial --mode vla_only --seed 46 --n_rollouts 20 --K 1\\n121241    01:11:08 Rl+  python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 46 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.91}}"
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

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "626bc244-56f9-4696-b26c-08f89cbcaaba",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_017nb8hj7kq8Bkd855ELDdt8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 794,
      "cache_read_input_tokens": 56208,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 794
      },
      "output_tokens": 94,
      "service_tier": "standard",
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

All 5 still running (1h11m–1h34m runtime). Let me check progress in tmux logs.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "15e98c2a-61b5-41bf-aa35-acb60e122cf8",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_017nb8hj7kq8Bkd855ELDdt8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 794,
      "cache_read_input_tokens": 56208,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 794
      },
      "output_tokens": 94,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01CXFcWfn1ps8HsnQcvwm5pe`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "tmux ls",
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
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "ec8acea1-ab2e-4c92-8b03-d09aa366395c",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_017nb8hj7kq8Bkd855ELDdt8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 794,
      "cache_read_input_tokens": 56208,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 794
      },
      "output_tokens": 94,
      "service_tier": "standard",
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

_source line 46 · 2026-05-24T08:25:58.201Z_

<details><summary>↩ Tool result · `toolu_01CXFcWfn1ps8HsnQcvwm5pe`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'tmux' is not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "89b99423-82ba-43bd-8d8c-5e0ad7c53f29",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: 'tmux' is not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'tmux' is not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 47_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01SqzcZhTqufck18KJ4u2oLX`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "tmux ls 2>&1",
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
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "9e060a2b-4f1c-4da5-ae37-266e1d8a4c4f",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01PXTtz6Dy18KMcXAVKNWmw1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 351,
      "cache_read_input_tokens": 57002,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 351
      },
      "output_tokens": 51,
      "service_tier": "standard",
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

_source line 48 · 2026-05-24T08:26:01.839Z_

<details><summary>↩ Tool result · `toolu_01SqzcZhTqufck18KJ4u2oLX`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"eval-supp-adapt-tau025-spatial-s45: 1 windows (created Sun May 24 14:51:18 2026)\\neval-supp-crm-norm005-spatial-s45: 1 windows (created Sun May 24 14:51:15 2026)\\neval-supp-crm-norm005-spatial-s46: 1 windows (created Sun May 24 15:14:46 2026)\\neval-supp-vla-only-spatial-s45: 1 windows (created Sun May 24 14:51:12 2026)\\neval-supp-vla-only-spatial-s46: 1 windows (created Sun May 24 14:51:21 2026)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "3b27b39c-8cbd-4f0f-8cf3-124ec581c9e6",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"eval-supp-adapt-tau025-spatial-s45: 1 windows (created Sun May 24 14:51:18 2026)\\\\neval-supp-crm-norm005-spatial-s45: 1 windows (created Sun May 24 14:51:15 2026)\\\\neval-supp-crm-norm005-spatial-s46: 1 windows (created Sun May 24 15:14:46 2026)\\\\neval-supp-vla-only-spatial-s45: 1 windows (created Sun May 24 14:51:12 2026)\\\\neval-supp-vla-only-spatial-s46: 1 windows (created Sun May 24 14:51:21 2026)\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.32}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"eval-supp-adapt-tau025-spatial-s45: 1 windows (created Sun May 24 14:51:18 2026)\\neval-supp-crm-norm005-spatial-s45: 1 windows (created Sun May 24 14:51:15 2026)\\neval-supp-crm-norm005-spatial-s46: 1 windows (created Sun May 24 15:14:46 2026)\\neval-supp-vla-only-spatial-s45: 1 windows (created Sun May 24 14:51:12 2026)\\neval-supp-vla-only-spatial-s46: 1 windows (created Sun May 24 14:51:21 2026)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 49_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01MoqA5AG5fzSp9mjsM2dEJx`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "for s in eval-supp-adapt-tau025-spatial-s45 eval-supp-crm-norm005-spatial-s45 eval-supp-crm-norm005-spatial-s46 eval-supp-vla-only-spatial-s45 eval-supp-vla-only-spatial-s46; do echo \"===== $s =====\"; tmux capture-pane -t \"$s\" -p -S -50 | grep -E \"task|rollout|success|Success|SR|Episode|complete|error|Error\" | tail -15; done",
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
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "ef8e2db8-68dd-4b45-aa5b-e8860c485cb3",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_019faGyG3n1PABCAHmJAgBdd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 457,
      "cache_read_input_tokens": 57353,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 457
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

_source line 50 · 2026-05-24T08:26:08.456Z_

<details><summary>↩ Tool result · `toolu_01MoqA5AG5fzSp9mjsM2dEJx`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"===== eval-supp-adapt-tau025-spatial-s45 =====\\n_the_plate: rollout 20/20, success so far: 15/20\\nthe_plate] success rate: 75.0% (15/20)\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 5/20,\\n success so far: 0/5\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 10/20\\n, success so far: 0/10\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 15/20\\n, success so far: 0/15\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 20/20\\n, success so far: 0/20\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate:\\nut 5/20, success so far: 5/5\\nut 10/20, success so far: 10/10\\nut 15/20, success so far: 15/15\\nut 20/20, success so far: 20/20\\n===== eval-supp-crm-norm005-spatial-s45 =====\\nthe_plate] success rate: 70.0% (14/20)\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 5/20,\\n success so far: 0/5\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 10/20\\n, success so far: 0/10\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 15/20\\n, success so far: 0/15\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 20/20\\n, success so far: 0/20\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate:\\nut 5/20, success so far: 4/5\\nut 10/20, success so far: 9/10\\nut 15/20, success so far: 14/15\\nut 20/20, success so far: 19/20\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 5/20, s\\n===== eval-supp-crm-norm005-spatial-s46 =====\\n/20, success so far: 10/10\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 15\\n/20, success so far: 15/15\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 20\\n/20, success so far: 20/20\\n[pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate] success rat\\n_the_plate: rollout 5/20, success so far: 4/5\\n_the_plate: rollout 10/20, success so far: 8/10\\n_the_plate: rollout 15/20, success so far: 11/15\\n_the_plate: rollout 20/20, success so far: 14/20\\nthe_plate] success rate: 70.0% (14/20)\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 5/20,\\n success so far: 0/5\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 10/20\\n, success so far: 0/10\\n===== eval-supp-vla-only-spatial-s45 =====\\nthe_plate] success rate: 70.0% (14/20)\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 5/20,\\n success so far: 0/5\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 10/20\\n, success so far: 0/10\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 15/20\\n, success so far: 0/15\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 20/20\\n, success so far: 0/20\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate:\\nut 5/20, success so far: 5/5\\nut 10/20, success so far: 10/10\\nut 15/20, success so far: 15/15\\nut 20/20, success so far: 20/20\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 5/20, s\\n===== eval-supp-vla-only-spatial-s46 =====\\n_the_plate: rollout 15/20, success so far: 12/15\\n_the_plate: rollout 20/20, success so far: 15/20\\nthe_plate] success rate: 75.0% (15/20)\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 5/20,\\n success so far: 0/5\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 10/20\\n, success so far: 0/10\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 15/20\\n, success so far: 0/15\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 20/20\\n, success so far: 0/20\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate:\\nut 5/20, success so far: 4/5\\nut 10/20, success so far: 9/10\\nut 15/20, success so far: 14/15\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "8bce92bd-6c75-4ea5-bda7-5dd85ee3eeca",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"===== eval-supp-adapt-tau025-spatial-s45 =====\\\\n_the_plate: rollout 20/20, success so far: 15/20\\\\nthe_plate] success rate: 75.0% (15/20)\\\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 5/20,\\\\n success so far: 0/5\\\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 10/20\\\\n, success so far: 0/10\\\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 15/20\\\\n, success so far: 0/15\\\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 20/20\\\\n, success so far: 0/20\\\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate:\\\\nut 5/20, success so far: 5/5\\\\nut 10/20, success so far: 10/10\\\\nut 15/20, success so far: 15/15\\\\nut 20/20, success so far: 20/20\\\\n===== eval-supp-crm-norm005-spatial-s45 =====\\\\nthe_plate] success rate: 70.0% (14/20)\\\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 5/20,\\\\n success so far: 0/5\\\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 10/20\\\\n, success so far: 0/10\\\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 15/20\\\\n, success so far: 0/15\\\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 20/20\\\\n, success so far: 0/20\\\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate:\\\\nut 5/20, success so far: 4/5\\\\nut 10/20, success so far: 9/10\\\\nut 15/20, success so far: 14/15\\\\nut 20/20, success so far: 19/20\\\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 5/20, s\\\\n===== eval-supp-crm-norm005-spatial-s46 =====\\\\n/20, success so far: 10/10\\\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 15\\\\n/20, success so far: 15/15\\\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 20\\\\n/20, success so far: 20/20\\\\n[pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate] success rat\\\\n_the_plate: rollout 5/20, success so far: 4/5\\\\n_the_plate: rollout 10/20, success so far: 8/10\\\\n_the_plate: rollout 15/20, success so far: 11/15\\\\n_the_plate: rollout 20/20, success so far: 14/20\\\\nthe_plate] success rate: 70.0% (14/20)\\\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 5/20,\\\\n success so far: 0/5\\\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 10/20\\\\n, success so far: 0/10\\\\n===== eval-supp-vla-only-spatial-s45 =====\\\\nthe_plate] success rate: 70.0% (14/20)\\\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 5/20,\\\\n success so far: 0/5\\\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 10/20\\\\n, success so far: 0/10\\\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 15/20\\\\n, success so far: 0/15\\\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 20/20\\\\n, success so far: 0/20\\\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate:\\\\nut 5/20, success so far: 5/5\\\\nut 10/20, success so far: 10/10\\\\nut 15/20, success so far: 15/15\\\\nut 20/20, success so far: 20/20\\\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 5/20, s\\\\n===== eval-supp-vla-only-spatial-s46 =====\\\\n_the_plate: rollout 15/20, success so far: 12/15\\\\n_the_plate: rollout 20/20, success so far: 15/20\\\\nthe_plate] success rate: 75.0% (15/20)\\\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 5/20,\\\\n success so far: 0/5\\\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 10/20\\\\n, success so far: 0/10\\\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 15/20\\\\n, success so far: 0/15\\\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 20/20\\\\n, success so far: 0/20\\\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate:\\\\nut 5/20, success so far: 4/5\\\\nut 10/20, success so far: 9/10\\\\nut 15/20, success so far: 14/15\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.37}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"===== eval-supp-adapt-tau025-spatial-s45 =====\\n_the_plate: rollout 20/20, success so far: 15/20\\nthe_plate] success rate: 75.0% (15/20)\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 5/20,\\n success so far: 0/5\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 10/20\\n, success so far: 0/10\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 15/20\\n, success so far: 0/15\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 20/20\\n, success so far: 0/20\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate:\\nut 5/20, success so far: 5/5\\nut 10/20, success so far: 10/10\\nut 15/20, success so far: 15/15\\nut 20/20, success so far: 20/20\\n===== eval-supp-crm-norm005-spatial-s45 =====\\nthe_plate] success rate: 70.0% (14/20)\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 5/20,\\n success so far: 0/5\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 10/20\\n, success so far: 0/10\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 15/20\\n, success so far: 0/15\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 20/20\\n, success so far: 0/20\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate:\\nut 5/20, success so far: 4/5\\nut 10/20, success so far: 9/10\\nut 15/20, success so far: 14/15\\nut 20/20, success so far: 19/20\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 5/20, s\\n===== eval-supp-crm-norm005-spatial-s46 =====\\n/20, success so far: 10/10\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 15\\n/20, success so far: 15/15\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 20\\n/20, success so far: 20/20\\n[pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate] success rat\\n_the_plate: rollout 5/20, success so far: 4/5\\n_the_plate: rollout 10/20, success so far: 8/10\\n_the_plate: rollout 15/20, success so far: 11/15\\n_the_plate: rollout 20/20, success so far: 14/20\\nthe_plate] success rate: 70.0% (14/20)\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 5/20,\\n success so far: 0/5\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 10/20\\n, success so far: 0/10\\n===== eval-supp-vla-only-spatial-s45 =====\\nthe_plate] success rate: 70.0% (14/20)\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 5/20,\\n success so far: 0/5\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 10/20\\n, success so far: 0/10\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 15/20\\n, success so far: 0/15\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 20/20\\n, success so far: 0/20\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate:\\nut 5/20, success so far: 5/5\\nut 10/20, success so far: 10/10\\nut 15/20, success so far: 15/15\\nut 20/20, success so far: 20/20\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 5/20, s\\n===== eval-supp-vla-only-spatial-s46 =====\\n_the_plate: rollout 15/20, success so far: 12/15\\n_the_plate: rollout 20/20, success so far: 15/20\\nthe_plate] success rate: 75.0% (15/20)\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 5/20,\\n success so far: 0/5\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 10/20\\n, success so far: 0/10\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 15/20\\n, success so far: 0/15\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 20/20\\n, success so far: 0/20\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate:\\nut 5/20, success so far: 4/5\\nut 10/20, success so far: 9/10\\nut 15/20, success so far: 14/15\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"
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

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "960718c5-cc17-4f44-b1a4-13906ebb36f6",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01D1Q26SXkMF8wCu9gYeCVqA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2556,
      "cache_read_input_tokens": 57810,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2556
      },
      "output_tokens": 44,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01UzX3N6D1v6iQaVz2WAjBtm`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "for s in eval-supp-adapt-tau025-spatial-s45 eval-supp-crm-norm005-spatial-s45 eval-supp-crm-norm005-spatial-s46 eval-supp-vla-only-spatial-s45 eval-supp-vla-only-spatial-s46; do echo \"===== $s =====\"; tmux capture-pane -t \"$s\" -p -S -200 | grep -E \"^(Task|Starting task|\\[Task|\\*+ Task|Evaluating|Suite)\" | tail -5; echo \"---LAST---\"; tmux capture-pane -t \"$s\" -p | tail -3; done",
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
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "06975323-b008-473b-bf41-90a2f1225b31",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01D1Q26SXkMF8wCu9gYeCVqA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2556,
      "cache_read_input_tokens": 57810,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2556
      },
      "output_tokens": 44,
      "service_tier": "standard",
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

_source line 53 · 2026-05-24T08:26:18.731Z_

<details><summary>↩ Tool result · `toolu_01UzX3N6D1v6iQaVz2WAjBtm`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"===== eval-supp-adapt-tau025-spatial-s45 =====\\n---LAST---\\n[pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate] succes\\ns rate: 100.0% (20/20)\\n\\n===== eval-supp-crm-norm005-spatial-s45 =====\\n---LAST---\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 5/20, s\\nuccess so far: 4/5\\n\\n===== eval-supp-crm-norm005-spatial-s46 =====\\n---LAST---\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 10/20\\n, success so far: 0/10\\n\\n===== eval-supp-vla-only-spatial-s45 =====\\n---LAST---\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 5/20, s\\nuccess so far: 4/5\\n\\n===== eval-supp-vla-only-spatial-s46 =====\\n---LAST---\\n[pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate] succes\\ns rate: 95.0% (19/20)\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "ba7f93df-f3fb-41a8-b29d-4fb6ddc00fea",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"===== eval-supp-adapt-tau025-spatial-s45 =====\\\\n---LAST---\\\\n[pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate] succes\\\\ns rate: 100.0% (20/20)\\\\n\\\\n===== eval-supp-crm-norm005-spatial-s45 =====\\\\n---LAST---\\\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 5/20, s\\\\nuccess so far: 4/5\\\\n\\\\n===== eval-supp-crm-norm005-spatial-s46 =====\\\\n---LAST---\\\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 10/20\\\\n, success so far: 0/10\\\\n\\\\n===== eval-supp-vla-only-spatial-s45 =====\\\\n---LAST---\\\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 5/20, s\\\\nuccess so far: 4/5\\\\n\\\\n===== eval-supp-vla-only-spatial-s46 =====\\\\n---LAST---\\\\n[pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate] succes\\\\ns rate: 95.0% (19/20)\\\\n\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"===== eval-supp-adapt-tau025-spatial-s45 =====\\n---LAST---\\n[pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate] succes\\ns rate: 100.0% (20/20)\\n\\n===== eval-supp-crm-norm005-spatial-s45 =====\\n---LAST---\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 5/20, s\\nuccess so far: 4/5\\n\\n===== eval-supp-crm-norm005-spatial-s46 =====\\n---LAST---\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 10/20\\n, success so far: 0/10\\n\\n===== eval-supp-vla-only-spatial-s45 =====\\n---LAST---\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 5/20, s\\nuccess so far: 4/5\\n\\n===== eval-supp-vla-only-spatial-s46 =====\\n---LAST---\\n[pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate] succes\\ns rate: 95.0% (19/20)\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 54_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "d01cee87-6dcd-4bfb-ad03-e1a9aa2c21ab",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01KFzcHa23hhegW252ZYXxvM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1003,
      "cache_read_input_tokens": 60366,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1003
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

_source line 55_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_012Mjg4sVt6T6Sg3V4rrtQFq`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "for s in eval-supp-adapt-tau025-spatial-s45 eval-supp-crm-norm005-spatial-s45 eval-supp-crm-norm005-spatial-s46 eval-supp-vla-only-spatial-s45 eval-supp-vla-only-spatial-s46; do echo \"===== $s =====\"; tmux capture-pane -t \"$s\" -p -S -3000 | grep -cE \"success rate: [0-9]\"; tmux capture-pane -t \"$s\" -p -S -3000 | grep -E \"success rate: [0-9]\" | tail -10; done",
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
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "1ec9c04a-fb97-4395-aef4-4d3716a15627",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01KFzcHa23hhegW252ZYXxvM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1003,
      "cache_read_input_tokens": 60366,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1003
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

_source line 56 · 2026-05-24T08:26:30.788Z_

<details><summary>↩ Tool result · `toolu_012Mjg4sVt6T6Sg3V4rrtQFq`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"===== eval-supp-adapt-tau025-spatial-s45 =====\\n2\\nate] success rate: 95.0% (19/20)\\nthe_plate] success rate: 75.0% (15/20)\\n===== eval-supp-crm-norm005-spatial-s45 =====\\n2\\nate] success rate: 100.0% (20/20)\\nthe_plate] success rate: 70.0% (14/20)\\n===== eval-supp-crm-norm005-spatial-s46 =====\\n2\\nate] success rate: 95.0% (19/20)\\nthe_plate] success rate: 70.0% (14/20)\\n===== eval-supp-vla-only-spatial-s45 =====\\n2\\nate] success rate: 95.0% (19/20)\\nthe_plate] success rate: 70.0% (14/20)\\n===== eval-supp-vla-only-spatial-s46 =====\\n2\\nate] success rate: 95.0% (19/20)\\nthe_plate] success rate: 75.0% (15/20)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "e4292ffc-5d6d-4df6-bffb-cc8040831b92",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"===== eval-supp-adapt-tau025-spatial-s45 =====\\\\n2\\\\nate] success rate: 95.0% (19/20)\\\\nthe_plate] success rate: 75.0% (15/20)\\\\n===== eval-supp-crm-norm005-spatial-s45 =====\\\\n2\\\\nate] success rate: 100.0% (20/20)\\\\nthe_plate] success rate: 70.0% (14/20)\\\\n===== eval-supp-crm-norm005-spatial-s46 =====\\\\n2\\\\nate] success rate: 95.0% (19/20)\\\\nthe_plate] success rate: 70.0% (14/20)\\\\n===== eval-supp-vla-only-spatial-s45 =====\\\\n2\\\\nate] success rate: 95.0% (19/20)\\\\nthe_plate] success rate: 70.0% (14/20)\\\\n===== eval-supp-vla-only-spatial-s46 =====\\\\n2\\\\nate] success rate: 95.0% (19/20)\\\\nthe_plate] success rate: 75.0% (15/20)\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"===== eval-supp-adapt-tau025-spatial-s45 =====\\n2\\nate] success rate: 95.0% (19/20)\\nthe_plate] success rate: 75.0% (15/20)\\n===== eval-supp-crm-norm005-spatial-s45 =====\\n2\\nate] success rate: 100.0% (20/20)\\nthe_plate] success rate: 70.0% (14/20)\\n===== eval-supp-crm-norm005-spatial-s46 =====\\n2\\nate] success rate: 95.0% (19/20)\\nthe_plate] success rate: 70.0% (14/20)\\n===== eval-supp-vla-only-spatial-s45 =====\\n2\\nate] success rate: 95.0% (19/20)\\nthe_plate] success rate: 70.0% (14/20)\\n===== eval-supp-vla-only-spatial-s46 =====\\n2\\nate] success rate: 95.0% (19/20)\\nthe_plate] success rate: 75.0% (15/20)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 57_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "03767676-9e2f-4b12-8da2-e58b5cef1692",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01LRgwtmhPfzfJ3A8Rzb6Ba3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 864,
      "cache_read_input_tokens": 61369,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 864
      },
      "output_tokens": 47,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_013f8gPsVFdp6dVeBmsyheB3`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "ls -lht /root/acr-vla-conformal-refinement/logs/ 2>/dev/null | head -25",
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
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "fc4d82b5-8791-41d9-af70-eb430f549165",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01LRgwtmhPfzfJ3A8Rzb6Ba3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 864,
      "cache_read_input_tokens": 61369,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 864
      },
      "output_tokens": 47,
      "service_tier": "standard",
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

_source line 59 · 2026-05-24T08:26:37.350Z_

<details><summary>↩ Tool result · `toolu_013f8gPsVFdp6dVeBmsyheB3`</summary>

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
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "5813651a-2ca5-46b3-93e7-52e52d19727c",
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

_source line 60_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_019eL3U8LzSk5W9vSuctWqRD`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "ls -lht /root/acr-vla-conformal-refinement/logs/",
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
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "d38a19eb-4786-4660-8bc7-99db2ebb49a6",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_017wpSkgRuY7FttuVqAfmkAH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 441,
      "cache_read_input_tokens": 62233,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 441
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

_source line 61 · 2026-05-24T08:26:41.052Z_

<details><summary>↩ Tool result · `toolu_019eL3U8LzSk5W9vSuctWqRD`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 21M\\n-rw-r--r-- 1 root root 5.3K May 24 16:26 eval-supp-vla-only-spatial-s46.log\\n-rw-r--r-- 1 root root 5.4K May 24 16:25 eval-supp-vla-only-spatial-s45.log\\n-rw-r--r-- 1 root root 5.6K May 24 16:25 eval-supp-crm-norm005-spatial-s45.log\\n-rw-r--r-- 1 root root 5.5K May 24 16:23 eval-supp-adapt-tau025-spatial-s45.log\\n-rw-r--r-- 1 root root 4.7K May 24 16:22 eval-supp-crm-norm005-spatial-s46.log\\n-rw-r--r-- 1 root root  507 May 24 15:05 openvla_eval_object_crm_k1_multiscale_K1_seed42.json\\n-rw-r--r-- 1 root root  498 May 24 15:03 openvla_eval_object_vla_only_K1_seed42.json\\n-rw-r--r-- 1 root root  11K May 24 14:51 crm-openvla-k1-multiscale-object.log\\n-rw-r--r-- 1 root root 1.8K May 24 09:58 eval_long_k2mean_seed45.json\\n-rw-r--r-- 1 root root 5.3K May 24 09:27 eval-supp-goal-reconvla-s46.log\\n-rw-r--r-- 1 root root 1.4K May 24 09:27 eval_goal_reconvla_seed46.json\\n-rw-r--r-- 1 root root 1.3K May 24 09:21 eval_goal_crm_obs_only_norm0.05_seed46.json\\n-rw-r--r-- 1 root root 5.3K May 24 09:20 eval-supp-goal-vla-only-s46.log\\n-rw-r--r-- 1 root root 1.3K May 24 09:20 eval_goal_vla_only_seed46.json\\n-rw-r--r-- 1 root root 1.5K May 24 09:19 eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed46.json\\n-rw-r--r-- 1 root root 1.3K May 24 09:17 eval_goal_k2mean_seed46.json\\n-rw-r--r-- 1 root root 1.8K May 24 06:59 eval_long_vla_only_seed44.json\\n-rw-r--r-- 1 root root 1.8K May 24 06:54 eval_long_reconvla_seed44.json\\n-rw-r--r-- 1 root root 1.3K May 24 06:45 eval_goal_crm_obs_only_norm0.05_seed45.json\\n-rw-r--r-- 1 root root 1.3K May 24 06:39 eval_goal_vla_only_seed45.json\\n-rw-r--r-- 1 root root 1.3K May 24 06:39 eval_goal_reconvla_seed45.json\\n-rw-r--r-- 1 root root 1.5K May 24 04:12 eval_object_vla_only_seed45.json\\n-rw-r--r-- 1 root root 1.7K May 24 04:10 eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json\\n-rw-r--r-- 1 root root 1.7K May 24 04:09 eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed46.json\\n-rw-r--r-- 1 root root 1.8K May 23 23:28 eval_long_crm_obs_only_norm0.05_seed42.json\\n-rw-r--r-- 1 root root 5.6K May 23 23:26 eval-ablation-tau010-goal-s42.log\\n-rw-r--r-- 1 root root 1.5K May 23 23:26 eval_goal_adaptive_conformal_crm_norm0.2_tau0.1_seed42.json\\n-rw-r--r-- 1 root root 1.8K May 23 23:26 eval_long_reconvla_seed42.json\\n-rw-r--r-- 1 root root 2.0K May 23 23:19 eval_long_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json\\n-rw-r--r-- 1 root root 5.6K May 23 23:18 eval-ablation-tau015-goal-s42.log\\n-rw-r--r-- 1 root root 1.5K May 23 23:18 eval_goal_adaptive_conformal_crm_norm0.2_tau0.15_seed42.json\\n-rw-r--r-- 1 root root 5.5K May 23 23:16 eval-ablation-tau040-goal-s42.log\\n-rw-r--r-- 1 root root 1.5K May 23 23:16 eval_goal_adaptive_conformal_crm_norm0.2_tau0.4_seed42.json\\n-rw-r--r-- 1 root root 1.3K May 23 20:32 eval_goal_reconvla_seed44.json\\n-rw-r--r-- 1 root root 1.4K May 23 20:31 eval_goal_crm_obs_only_norm0.05_seed44.json\\n-rw-r--r-- 1 root root 6.0K May 23 19:43 eval-supp-obj-reconvla-s43.log\\n-rw-r--r-- 1 root root 1.5K May 23 19:43 eval_object_reconvla_seed43.json\\n-rw-r--r-- 1 root root 6.1K May 23 17:59 eval-supp-k2mean-object-s42.log\\n-rw-r--r-- 1 root root 1.5K May 23 17:59 eval_object_vla_only_seed42.json\\n-rw-r--r-- 1 root root 6.5K May 23 17:57 eval-supp-obj-adapt-tau025-s42.log\\n-rw-r--r-- 1 root root 1.7K May 23 17:57 eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json\\n-rw-r--r-- 1 root root 7.1K May 23 17:32 eval-supp-k2mean-spatial-s42.log\\n-rw-r--r-- 1 root root 1.7K May 23 17:32 eval_spatial_vla_only_seed42.json\\n-rw-r--r-- 1 root root 5.3K May 23 17:31 eval-goal-vla-only-wrapper-s42.log\\n-rw-r--r-- 1 root root 1.3K May 23 17:31 eval_goal_vla_only_seed42.json\\n-rw-r--r-- 1 root root 5.3K May 23 17:29 eval-supp-goal-reconvla-s42.log\\n-rw-r--r-- 1 root root 1.3K May 23 17:29 eval_goal_reconvla_seed42.json\\n-rw-r--r-- 1 root root 5.6K May 23 16:52 eval-supp-goal-adapt-tau025-s42.log\\n-rw-r--r-- 1 root root 1.5K May 23 16:52 eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json\\n-rw-r--r-- 1 root root 6.0K May \\n\\n... [截断: 输出过长，省略 13880 字符] ...\\n\\n 1 root root 4.2K May 18 12:34 eval_object_perdof_norm02_seed47.log\\n-rw-r--r-- 1 root root 1.5K May 18 12:34 eval_object_perdof_norm02_seed47.json\\n-rw-r--r-- 1 root root 4.2K May 18 10:21 eval_object_perdof_norm02_seed46.log\\n-rw-r--r-- 1 root root 1.5K May 18 10:21 eval_object_perdof_norm02_seed46.json\\n-rw-r--r-- 1 root root 2.4K May 18 06:54 eval_object_obs_only_norm005_seed43.log\\n-rw-r--r-- 1 root root  11K May 18 04:24 eval_k1_crm_multiscale_object_seed42.log\\n-rw-r--r-- 1 root root 1.5K May 18 04:24 eval_k1_crm_multiscale_object_seed42.json\\n-rw-r--r-- 1 root root 2.9K May 18 02:33 latency_profile.log\\n-rw-r--r-- 1 root root 5.9K May 18 01:29 eval_object_obs_only_default_seed45.log\\n-rw-r--r-- 1 root root 1.5K May 18 01:29 eval_object_obs_only_default_seed45.json\\n-rw-r--r-- 1 root root 5.9K May 18 01:26 eval_object_scalar_seed45.log\\n-rw-r--r-- 1 root root 1.5K May 18 01:26 eval_object_scalar_seed45.json\\n-rw-r--r-- 1 root root  11K May 18 01:15 train_crm_k1_full.log\\n-rw-r--r-- 1 root root 5.9K May 18 01:00 eval_object_perdof_norm02_seed45.log\\n-rw-r--r-- 1 root root 1.5K May 18 01:00 eval_object_perdof_norm02_seed45.json\\n-rw-r--r-- 1 root root 1.5K May 18 00:48 eval_object_perdof_norm02_seed44.json\\n-rw-r--r-- 1 root root  192 May 17 23:50 redownload_tomato.log\\n-rw-r--r-- 1 root root 256K May 17 23:42 libero_download_aria2.log\\n-rw-r--r-- 1 root root   99 May 17 23:09 libero_download.log\\ndrwxr-xr-x 2 root root   10 May 17 22:56 sentinels\\n-rw-r--r-- 1 root root 2.3K May 17 22:48 train_crm_k1_accg.log\\n-rw-r--r-- 1 root root 2.3K May 17 22:04 train_crm_k1.log\\n-rw-r--r-- 1 root root 1.4K May 17 19:38 eval_object_perdof_norm02_seed43.log\\n-rw-r--r-- 1 root root 1.4K May 17 19:02 eval_object_perdof_norm03_seed46.log\\n-rw-r--r-- 1 root root 1.4K May 17 18:36 eval_object_obs_only_norm02_seed46.log\\n-rw-r--r-- 1 root root 1.9K May 17 18:25 eval_obs_only_object_norm01_seed46.log\\n-rw-r--r-- 1 root root 1.9K May 17 18:17 eval_object_obs_only_norm01_seed47.log\\n-rw-r--r-- 1 root root 1.5K May 17 15:00 eval_object_obs_only_norm03_seed45_r2.json\\n-rw-r--r-- 1 root root 1.4K May 17 14:52 eval_object_perdof_norm01_seed47.log\\n-rw-r--r-- 1 root root 1.5K May 17 11:27 eval_object_vla_mean_seed45.json\\n-rw-r--r-- 1 root root 1.5K May 17 08:29 eval_object_argmin_seed45.json\\n-rw-r--r-- 1 root root 5.7K May 16 20:36 eval_object_vla_only_seed45.log\\n-rw-r--r-- 1 root root 1.4K May 16 19:07 eval_object_obs_only_norm03_seed45.log\\n-rw-r--r-- 1 root root 4.2K May 16 19:02 nohup_eval_object_perdof_norm03_r3.log\\n-rw-r--r-- 1 root root 1.5K May 16 19:02 eval_object_perdof_norm03_r3.json\\n-rw-r--r-- 1 root root 1.5K May 16 18:38 eval_object_perdof_norm02_seed43_r3.json\\n-rw-r--r-- 1 root root 4.2K May 16 16:29 nohup_eval_object_perdof_norm005.log\\n-rw-r--r-- 1 root root 1.5K May 16 16:29 eval_object_perdof_norm005.json\\n-rw-r--r-- 1 root root 4.2K May 16 16:16 eval_object_obs_only_norm005.log\\n-rw-r--r-- 1 root root 1.5K May 16 16:16 eval_object_obs_only_norm005.json\\n-rw-r--r-- 1 root root 1.5K May 16 16:07 eval_object_perdof_norm003.json\\n-rw-r--r-- 1 root root 4.2K May 16 15:26 eval_object_obs_only_norm03.log\\n-rw-r--r-- 1 root root 1.5K May 16 15:26 eval_object_obs_only_norm03.json\\n-rw-r--r-- 1 root root 1.4K May 16 03:25 nohup_eval_object_obs_only_norm02_v2.log\\n-rw-r--r-- 1 root root 3.1K May 16 03:15 eval_object_perdof_norm03_r2.log\\n-rw-r--r-- 1 root root 1.5K May 16 02:25 eval_object_perdof_norm03.log\\n-rw-r--r-- 1 root root 1.3K May 16 00:52 eval_object_perdof_default_norm.log\\n-rw-r--r-- 1 root root 1.3K May 15 11:21 eval_spatial_obsonly_norm02.log\\n-rw-r--r-- 1 root root 1.3K May 15 11:19 eval_spatial_obsonly_norm005.log\\n-rw-r--r-- 1 root root 1.3K May 15 11:17 eval_spatial_perdof_norm03.log\\n-rw-r--r-- 1 root root 1.3K May 15 11:14 eval_spatial_perdof_norm02.log\\n-rw-r--r-- 1 root root 1.3K May 15 11:12 eval_spatial_perdof_norm005.log\\n-rw-r--r-- 1 root root 1.3K May 15 11:11 eval_spatial_perdof_norm003.log\\n-rw-r--r-- 1 root root 5.1K May 15 10:41 eval_object_vla_only.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "464f9660-8d2a-4611-b253-c0e3b1a46be0",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"total 21M\\\\n-rw-r--r-- 1 root root 5.3K May 24 16:26 eval-supp-vla-only-spatial-s46.log\\\\n-rw-r--r-- 1 root root 5.4K May 24 16:25 eval-supp-vla-only-spatial-s45.log\\\\n-rw-r--r-- 1 root root 5.6K May 24 16:25 eval-supp-crm-norm005-spatial-s45.log\\\\n-rw-r--r-- 1 root root 5.5K May 24 16:23 eval-supp-adapt-tau025-spatial-s45.log\\\\n-rw-r--r-- 1 root root 4.7K May 24 16:22 eval-supp-crm-norm005-spatial-s46.log\\\\n-rw-r--r-- 1 root root  507 May 24 15:05 openvla_eval_object_crm_k1_multiscale_K1_seed42.json\\\\n-rw-r--r-- 1 root root  498 May 24 15:03 openvla_eval_object_vla_only_K1_seed42.json\\\\n-rw-r--r-- 1 root root  11K May 24 14:51 crm-openvla-k1-multiscale-object.log\\\\n-rw-r--r-- 1 root root 1.8K May 24 09:58 eval_long_k2mean_seed45.json\\\\n-rw-r--r-- 1 root root 5.3K May 24 09:27 eval-supp-goal-reconvla-s46.log\\\\n-rw-r--r-- 1 root root 1.4K May 24 09:27 eval_goal_reconvla_seed46.json\\\\n-rw-r--r-- 1 root root 1.3K May 24 09:21 eval_goal_crm_obs_only_norm0.05_seed46.json\\\\n-rw-r--r-- 1 root root 5.3K May 24 09:20 eval-supp-goal-vla-only-s46.log\\\\n-rw-r--r-- 1 root root 1.3K May 24 09:20 eval_goal_vla_only_seed46.json\\\\n-rw-r--r-- 1 root root 1.5K May 24 09:19 eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed46.json\\\\n-rw-r--r-- 1 root root 1.3K May 24 09:17 eval_goal_k2mean_seed46.json\\\\n-rw-r--r-- 1 root root 1.8K May 24 06:59 eval_long_vla_only_seed44.json\\\\n-rw-r--r-- 1 root root 1.8K May 24 06:54 eval_long_reconvla_seed44.json\\\\n-rw-r--r-- 1 root root 1.3K May 24 06:45 eval_goal_crm_obs_only_norm0.05_seed45.json\\\\n-rw-r--r-- 1 root root 1.3K May 24 06:39 eval_goal_vla_only_seed45.json\\\\n-rw-r--r-- 1 root root 1.3K May 24 06:39 eval_goal_reconvla_seed45.json\\\\n-rw-r--r-- 1 root root 1.5K May 24 04:12 eval_object_vla_only_seed45.json\\\\n-rw-r--r-- 1 root root 1.7K May 24 04:10 eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json\\\\n-rw-r--r-- 1 root root 1.7K May 24 04:09 eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed46.json\\\\n-rw-r--r-- 1 root root 1.8K May 23 23:28 eval_long_crm_obs_only_norm0.05_seed42.json\\\\n-rw-r--r-- 1 root root 5.6K May 23 23:26 eval-ablation-tau010-goal-s42.log\\\\n-rw-r--r-- 1 root root 1.5K May 23 23:26 eval_goal_adaptive_conformal_crm_norm0.2_tau0.1_seed42.json\\\\n-rw-r--r-- 1 root root 1.8K May 23 23:26 eval_long_reconvla_seed42.json\\\\n-rw-r--r-- 1 root root 2.0K May 23 23:19 eval_long_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json\\\\n-rw-r--r-- 1 root root 5.6K May 23 23:18 eval-ablation-tau015-goal-s42.log\\\\n-rw-r--r-- 1 root root 1.5K May 23 23:18 eval_goal_adaptive_conformal_crm_norm0.2_tau0.15_seed42.json\\\\n-rw-r--r-- 1 root root 5.5K May 23 23:16 eval-ablation-tau040-goal-s42.log\\\\n-rw-r--r-- 1 root root 1.5K May 23 23:16 eval_goal_adaptive_conformal_crm_norm0.2_tau0.4_seed42.json\\\\n-rw-r--r-- 1 root root 1.3K May 23 20:32 eval_goal_reconvla_seed44.json\\\\n-rw-r--r-- 1 root root 1.4K May 23 20:31 eval_goal_crm_obs_only_norm0.05_seed44.json\\\\n-rw-r--r-- 1 root root 6.0K May 23 19:43 eval-supp-obj-reconvla-s43.log\\\\n-rw-r--r-- 1 root root 1.5K May 23 19:43 eval_object_reconvla_seed43.json\\\\n-rw-r--r-- 1 root root 6.1K May 23 17:59 eval-supp-k2mean-object-s42.log\\\\n-rw-r--r-- 1 root root 1.5K May 23 17:59 eval_object_vla_only_seed42.json\\\\n-rw-r--r-- 1 root root 6.5K May 23 17:57 eval-supp-obj-adapt-tau025-s42.log\\\\n-rw-r--r-- 1 root root 1.7K May 23 17:57 eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json\\\\n-rw-r--r-- 1 root root 7.1K May 23 17:32 eval-supp-k2mean-spatial-s42.log\\\\n-rw-r--r-- 1 root root 1.7K May 23 17:32 eval_spatial_vla_only_seed42.json\\\\n-rw-r--r-- 1 root root 5.3K May 23 17:31 eval-goal-vla-only-wrapper-s42.log\\\\n-rw-r--r-- 1 root root 1.3K May 23 17:31 eval_goal_vla_only_seed42.json\\\\n-rw-r--r-- 1 root root 5.3K May 23 17:29 eval-supp-goal-reconvla-s42.log\\\\n-rw-r--r-- 1 root root 1.3K May 23 17:29 eval_goal_reconvla_seed42.json\\\\n-rw-r--r-- 1 root root 5.6K May 23 16:52 eval-supp-goal-adapt-tau025-s42.log\\\\n-rw-r--r-- 1 root root 1.5K May 23 16:52 eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json\\\\n-rw-r--r-- 1 root root 6.0K May \\\\n\\\\n... [截断: 输出过长，省略 13880 字符] ...\\\\n\\\\n 1 root root 4.2K May 18 12:34 eval_object_perdof_norm02_seed47.log\\\\n-rw-r--r-- 1 root root 1.5K May 18 12:34 eval_object_perdof_norm02_seed47.json\\\\n-rw-r--r-- 1 root root 4.2K May 18 10:21 eval_object_perdof_norm02_seed46.log\\\\n-rw-r--r-- 1 root root 1.5K May 18 10:21 eval_object_perdof_norm02_seed46.json\\\\n-rw-r--r-- 1 root root 2.4K May 18 06:54 eval_object_obs_only_norm005_seed43.log\\\\n-rw-r--r-- 1 root root  11K May 18 04:24 eval_k1_crm_multiscale_object_seed42.log\\\\n-rw-r--r-- 1 root root 1.5K May 18 04:24 eval_k1_crm_multiscale_object_seed42.json\\\\n-rw-r--r-- 1 root root 2.9K May 18 02:33 latency_profile.log\\\\n-rw-r--r-- 1 root root 5.9K May 18 01:29 eval_object_obs_only_default_seed45.log\\\\n-rw-r--r-- 1 root root 1.5K May 18 01:29 eval_object_obs_only_default_seed45.json\\\\n-rw-r--r-- 1 root root 5.9K May 18 01:26 eval_object_scalar_seed45.log\\\\n-rw-r--r-- 1 root root 1.5K May 18 01:26 eval_object_scalar_seed45.json\\\\n-rw-r--r-- 1 root root  11K May 18 01:15 train_crm_k1_full.log\\\\n-rw-r--r-- 1 root root 5.9K May 18 01:00 eval_object_perdof_norm02_seed45.log\\\\n-rw-r--r-- 1 root root 1.5K May 18 01:00 eval_object_perdof_norm02_seed45.json\\\\n-rw-r--r-- 1 root root 1.5K May 18 00:48 eval_object_perdof_norm02_seed44.json\\\\n-rw-r--r-- 1 root root  192 May 17 23:50 redownload_tomato.log\\\\n-rw-r--r-- 1 root root 256K May 17 23:42 libero_download_aria2.log\\\\n-rw-r--r-- 1 root root   99 May 17 23:09 libero_download.log\\\\ndrwxr-xr-x 2 root root   10 May 17 22:56 sentinels\\\\n-rw-r--r-- 1 root root 2.3K May 17 22:48 train_crm_k1_accg.log\\\\n-rw-r--r-- 1 root root 2.3K May 17 22:04 train_crm_k1.log\\\\n-rw-r--r-- 1 root root 1.4K May 17 19:38 eval_object_perdof_norm02_seed43.log\\\\n-rw-r--r-- 1 root root 1.4K May 17 19:02 eval_object_perdof_norm03_seed46.log\\\\n-rw-r--r-- 1 root root 1.4K May 17 18:36 eval_object_obs_only_norm02_seed46.log\\\\n-rw-r--r-- 1 root root 1.9K May 17 18:25 eval_obs_only_object_norm01_seed46.log\\\\n-rw-r--r-- 1 root root 1.9K May 17 18:17 eval_object_obs_only_norm01_seed47.log\\\\n-rw-r--r-- 1 root root 1.5K May 17 15:00 eval_object_obs_only_norm03_seed45_r2.json\\\\n-rw-r--r-- 1 root root 1.4K May 17 14:52 eval_object_perdof_norm01_seed47.log\\\\n-rw-r--r-- 1 root root 1.5K May 17 11:27 eval_object_vla_mean_seed45.json\\\\n-rw-r--r-- 1 root root 1.5K May 17 08:29 eval_object_argmin_seed45.json\\\\n-rw-r--r-- 1 root root 5.7K May 16 20:36 eval_object_vla_only_seed45.log\\\\n-rw-r--r-- 1 root root 1.4K May 16 19:07 eval_object_obs_only_norm03_seed45.log\\\\n-rw-r--r-- 1 root root 4.2K May 16 19:02 nohup_eval_object_perdof_norm03_r3.log\\\\n-rw-r--r-- 1 root root 1.5K May 16 19:02 eval_object_perdof_norm03_r3.json\\\\n-rw-r--r-- 1 root root 1.5K May 16 18:38 eval_object_perdof_norm02_seed43_r3.json\\\\n-rw-r--r-- 1 root root 4.2K May 16 16:29 nohup_eval_object_perdof_norm005.log\\\\n-rw-r--r-- 1 root root 1.5K May 16 16:29 eval_object_perdof_norm005.json\\\\n-rw-r--r-- 1 root root 4.2K May 16 16:16 eval_object_obs_only_norm005.log\\\\n-rw-r--r-- 1 root root 1.5K May 16 16:16 eval_object_obs_only_norm005.json\\\\n-rw-r--r-- 1 root root 1.5K May 16 16:07 eval_object_perdof_norm003.json\\\\n-rw-r--r-- 1 root root 4.2K May 16 15:26 eval_object_obs_only_norm03.log\\\\n-rw-r--r-- 1 root root 1.5K May 16 15:26 eval_object_obs_only_norm03.json\\\\n-rw-r--r-- 1 root root 1.4K May 16 03:25 nohup_eval_object_obs_only_norm02_v2.log\\\\n-rw-r--r-- 1 root root 3.1K May 16 03:15 eval_object_perdof_norm03_r2.log\\\\n-rw-r--r-- 1 root root 1.5K May 16 02:25 eval_object_perdof_norm03.log\\\\n-rw-r--r-- 1 root root 1.3K May 16 00:52 eval_object_perdof_default_norm.log\\\\n-rw-r--r-- 1 root root 1.3K May 15 11:21 eval_spatial_obsonly_norm02.log\\\\n-rw-r--r-- 1 root root 1.3K May 15 11:19 eval_spatial_obsonly_norm005.log\\\\n-rw-r--r-- 1 root root 1.3K May 15 11:17 eval_spatial_perdof_norm03.log\\\\n-rw-r--r-- 1 root root 1.3K May 15 11:14 eval_spatial_perdof_norm02.log\\\\n-rw-r--r-- 1 root root 1.3K May 15 11:12 eval_spatial_perdof_norm005.log\\\\n-rw-r--r-- 1 root root 1.3K May 15 11:11 eval_spatial_perdof_norm003.log\\\\n-rw-r--r-- 1 root root 5.1K May 15 10:41 eval_object_vla_only.log\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"total 21M\\n-rw-r--r-- 1 root root 5.3K May 24 16:26 eval-supp-vla-only-spatial-s46.log\\n-rw-r--r-- 1 root root 5.4K May 24 16:25 eval-supp-vla-only-spatial-s45.log\\n-rw-r--r-- 1 root root 5.6K May 24 16:25 eval-supp-crm-norm005-spatial-s45.log\\n-rw-r--r-- 1 root root 5.5K May 24 16:23 eval-supp-adapt-tau025-spatial-s45.log\\n-rw-r--r-- 1 root root 4.7K May 24 16:22 eval-supp-crm-norm005-spatial-s46.log\\n-rw-r--r-- 1 root root  507 May 24 15:05 openvla_eval_object_crm_k1_multiscale_K1_seed42.json\\n-rw-r--r-- 1 root root  498 May 24 15:03 openvla_eval_object_vla_only_K1_seed42.json\\n-rw-r--r-- 1 root root  11K May 24 14:51 crm-openvla-k1-multiscale-object.log\\n-rw-r--r-- 1 root root 1.8K May 24 09:58 eval_long_k2mean_seed45.json\\n-rw-r--r-- 1 root root 5.3K May 24 09:27 eval-supp-goal-reconvla-s46.log\\n-rw-r--r-- 1 root root 1.4K May 24 09:27 eval_goal_reconvla_seed46.json\\n-rw-r--r-- 1 root root 1.3K May 24 09:21 eval_goal_crm_obs_only_norm0.05_seed46.json\\n-rw-r--r-- 1 root root 5.3K May 24 09:20 eval-supp-goal-vla-only-s46.log\\n-rw-r--r-- 1 root root 1.3K May 24 09:20 eval_goal_vla_only_seed46.json\\n-rw-r--r-- 1 root root 1.5K May 24 09:19 eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed46.json\\n-rw-r--r-- 1 root root 1.3K May 24 09:17 eval_goal_k2mean_seed46.json\\n-rw-r--r-- 1 root root 1.8K May 24 06:59 eval_long_vla_only_seed44.json\\n-rw-r--r-- 1 root root 1.8K May 24 06:54 eval_long_reconvla_seed44.json\\n-rw-r--r-- 1 root root 1.3K May 24 06:45 eval_goal_crm_obs_only_norm0.05_seed45.json\\n-rw-r--r-- 1 root root 1.3K May 24 06:39 eval_goal_vla_only_seed45.json\\n-rw-r--r-- 1 root root 1.3K May 24 06:39 eval_goal_reconvla_seed45.json\\n-rw-r--r-- 1 root root 1.5K May 24 04:12 eval_object_vla_only_seed45.json\\n-rw-r--r-- 1 root root 1.7K May 24 04:10 eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json\\n-rw-r--r-- 1 root root 1.7K May 24 04:09 eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed46.json\\n-rw-r--r-- 1 root root 1.8K May 23 23:28 eval_long_crm_obs_only_norm0.05_seed42.json\\n-rw-r--r-- 1 root root 5.6K May 23 23:26 eval-ablation-tau010-goal-s42.log\\n-rw-r--r-- 1 root root 1.5K May 23 23:26 eval_goal_adaptive_conformal_crm_norm0.2_tau0.1_seed42.json\\n-rw-r--r-- 1 root root 1.8K May 23 23:26 eval_long_reconvla_seed42.json\\n-rw-r--r-- 1 root root 2.0K May 23 23:19 eval_long_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json\\n-rw-r--r-- 1 root root 5.6K May 23 23:18 eval-ablation-tau015-goal-s42.log\\n-rw-r--r-- 1 root root 1.5K May 23 23:18 eval_goal_adaptive_conformal_crm_norm0.2_tau0.15_seed42.json\\n-rw-r--r-- 1 root root 5.5K May 23 23:16 eval-ablation-tau040-goal-s42.log\\n-rw-r--r-- 1 root root 1.5K May 23 23:16 eval_goal_adaptive_conformal_crm_norm0.2_tau0.4_seed42.json\\n-rw-r--r-- 1 root root 1.3K May 23 20:32 eval_goal_reconvla_seed44.json\\n-rw-r--r-- 1 root root 1.4K May 23 20:31 eval_goal_crm_obs_only_norm0.05_seed44.json\\n-rw-r--r-- 1 root root 6.0K May 23 19:43 eval-supp-obj-reconvla-s43.log\\n-rw-r--r-- 1 root root 1.5K May 23 19:43 eval_object_reconvla_seed43.json\\n-rw-r--r-- 1 root root 6.1K May 23 17:59 eval-supp-k2mean-object-s42.log\\n-rw-r--r-- 1 root root 1.5K May 23 17:59 eval_object_vla_only_seed42.json\\n-rw-r--r-- 1 root root 6.5K May 23 17:57 eval-supp-obj-adapt-tau025-s42.log\\n-rw-r--r-- 1 root root 1.7K May 23 17:57 eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json\\n-rw-r--r-- 1 root root 7.1K May 23 17:32 eval-supp-k2mean-spatial-s42.log\\n-rw-r--r-- 1 root root 1.7K May 23 17:32 eval_spatial_vla_only_seed42.json\\n-rw-r--r-- 1 root root 5.3K May 23 17:31 eval-goal-vla-only-wrapper-s42.log\\n-rw-r--r-- 1 root root 1.3K May 23 17:31 eval_goal_vla_only_seed42.json\\n-rw-r--r-- 1 root root 5.3K May 23 17:29 eval-supp-goal-reconvla-s42.log\\n-rw-r--r-- 1 root root 1.3K May 23 17:29 eval_goal_reconvla_seed42.json\\n-rw-r--r-- 1 root root 5.6K May 23 16:52 eval-supp-goal-adapt-tau025-s42.log\\n-rw-r--r-- 1 root root 1.5K May 23 16:52 eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json\\n-rw-r--r-- 1 root root 6.0K May \\n\\n... [截断: 输出过长，省略 13880 字符] ...\\n\\n 1 root root 4.2K May 18 12:34 eval_object_perdof_norm02_seed47.log\\n-rw-r--r-- 1 root root 1.5K May 18 12:34 eval_object_perdof_norm02_seed47.json\\n-rw-r--r-- 1 root root 4.2K May 18 10:21 eval_object_perdof_norm02_seed46.log\\n-rw-r--r-- 1 root root 1.5K May 18 10:21 eval_object_perdof_norm02_seed46.json\\n-rw-r--r-- 1 root root 2.4K May 18 06:54 eval_object_obs_only_norm005_seed43.log\\n-rw-r--r-- 1 root root  11K May 18 04:24 eval_k1_crm_multiscale_object_seed42.log\\n-rw-r--r-- 1 root root 1.5K May 18 04:24 eval_k1_crm_multiscale_object_seed42.json\\n-rw-r--r-- 1 root root 2.9K May 18 02:33 latency_profile.log\\n-rw-r--r-- 1 root root 5.9K May 18 01:29 eval_object_obs_only_default_seed45.log\\n-rw-r--r-- 1 root root 1.5K May 18 01:29 eval_object_obs_only_default_seed45.json\\n-rw-r--r-- 1 root root 5.9K May 18 01:26 eval_object_scalar_seed45.log\\n-rw-r--r-- 1 root root 1.5K May 18 01:26 eval_object_scalar_seed45.json\\n-rw-r--r-- 1 root root  11K May 18 01:15 train_crm_k1_full.log\\n-rw-r--r-- 1 root root 5.9K May 18 01:00 eval_object_perdof_norm02_seed45.log\\n-rw-r--r-- 1 root root 1.5K May 18 01:00 eval_object_perdof_norm02_seed45.json\\n-rw-r--r-- 1 root root 1.5K May 18 00:48 eval_object_perdof_norm02_seed44.json\\n-rw-r--r-- 1 root root  192 May 17 23:50 redownload_tomato.log\\n-rw-r--r-- 1 root root 256K May 17 23:42 libero_download_aria2.log\\n-rw-r--r-- 1 root root   99 May 17 23:09 libero_download.log\\ndrwxr-xr-x 2 root root   10 May 17 22:56 sentinels\\n-rw-r--r-- 1 root root 2.3K May 17 22:48 train_crm_k1_accg.log\\n-rw-r--r-- 1 root root 2.3K May 17 22:04 train_crm_k1.log\\n-rw-r--r-- 1 root root 1.4K May 17 19:38 eval_object_perdof_norm02_seed43.log\\n-rw-r--r-- 1 root root 1.4K May 17 19:02 eval_object_perdof_norm03_seed46.log\\n-rw-r--r-- 1 root root 1.4K May 17 18:36 eval_object_obs_only_norm02_seed46.log\\n-rw-r--r-- 1 root root 1.9K May 17 18:25 eval_obs_only_object_norm01_seed46.log\\n-rw-r--r-- 1 root root 1.9K May 17 18:17 eval_object_obs_only_norm01_seed47.log\\n-rw-r--r-- 1 root root 1.5K May 17 15:00 eval_object_obs_only_norm03_seed45_r2.json\\n-rw-r--r-- 1 root root 1.4K May 17 14:52 eval_object_perdof_norm01_seed47.log\\n-rw-r--r-- 1 root root 1.5K May 17 11:27 eval_object_vla_mean_seed45.json\\n-rw-r--r-- 1 root root 1.5K May 17 08:29 eval_object_argmin_seed45.json\\n-rw-r--r-- 1 root root 5.7K May 16 20:36 eval_object_vla_only_seed45.log\\n-rw-r--r-- 1 root root 1.4K May 16 19:07 eval_object_obs_only_norm03_seed45.log\\n-rw-r--r-- 1 root root 4.2K May 16 19:02 nohup_eval_object_perdof_norm03_r3.log\\n-rw-r--r-- 1 root root 1.5K May 16 19:02 eval_object_perdof_norm03_r3.json\\n-rw-r--r-- 1 root root 1.5K May 16 18:38 eval_object_perdof_norm02_seed43_r3.json\\n-rw-r--r-- 1 root root 4.2K May 16 16:29 nohup_eval_object_perdof_norm005.log\\n-rw-r--r-- 1 root root 1.5K May 16 16:29 eval_object_perdof_norm005.json\\n-rw-r--r-- 1 root root 4.2K May 16 16:16 eval_object_obs_only_norm005.log\\n-rw-r--r-- 1 root root 1.5K May 16 16:16 eval_object_obs_only_norm005.json\\n-rw-r--r-- 1 root root 1.5K May 16 16:07 eval_object_perdof_norm003.json\\n-rw-r--r-- 1 root root 4.2K May 16 15:26 eval_object_obs_only_norm03.log\\n-rw-r--r-- 1 root root 1.5K May 16 15:26 eval_object_obs_only_norm03.json\\n-rw-r--r-- 1 root root 1.4K May 16 03:25 nohup_eval_object_obs_only_norm02_v2.log\\n-rw-r--r-- 1 root root 3.1K May 16 03:15 eval_object_perdof_norm03_r2.log\\n-rw-r--r-- 1 root root 1.5K May 16 02:25 eval_object_perdof_norm03.log\\n-rw-r--r-- 1 root root 1.3K May 16 00:52 eval_object_perdof_default_norm.log\\n-rw-r--r-- 1 root root 1.3K May 15 11:21 eval_spatial_obsonly_norm02.log\\n-rw-r--r-- 1 root root 1.3K May 15 11:19 eval_spatial_obsonly_norm005.log\\n-rw-r--r-- 1 root root 1.3K May 15 11:17 eval_spatial_perdof_norm03.log\\n-rw-r--r-- 1 root root 1.3K May 15 11:14 eval_spatial_perdof_norm02.log\\n-rw-r--r-- 1 root root 1.3K May 15 11:12 eval_spatial_perdof_norm005.log\\n-rw-r--r-- 1 root root 1.3K May 15 11:11 eval_spatial_perdof_norm003.log\\n-rw-r--r-- 1 root root 5.1K May 15 10:41 eval_object_vla_only.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"
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

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "b2f77fbf-8c9e-44ef-826f-da08567e6e87",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01QvPfi79L8c6t3RFnDzuBX3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5285,
      "cache_read_input_tokens": 62674,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5285
      },
      "output_tokens": 47,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01BXUwoqjDfqBXPzJDe5kbmS`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "cd /root/acr-vla-conformal-refinement/logs && for f in eval-supp-vla-only-spatial-s45.log eval-supp-vla-only-spatial-s46.log eval-supp-crm-norm005-spatial-s45.log eval-supp-crm-norm005-spatial-s46.log eval-supp-adapt-tau025-spatial-s45.log; do echo \"===== $f =====\"; echo \"tasks_completed:\"; grep -cE \"success rate: [0-9]\" \"$f\"; echo \"last_summary_lines:\"; grep -E \"success rate: [0-9]\" \"$f\" | tail -10; echo \"current_progress:\"; tail -3 \"$f\"; done",
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
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "9b877c8f-3054-4ea8-8230-c5410f38d2d7",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01QvPfi79L8c6t3RFnDzuBX3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5285,
      "cache_read_input_tokens": 62674,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5285
      },
      "output_tokens": 47,
      "service_tier": "standard",
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

_source line 64 · 2026-05-24T08:26:49.245Z_

<details><summary>↩ Tool result · `toolu_01BXUwoqjDfqBXPzJDe5kbmS`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"===== eval-supp-vla-only-spatial-s45.log =====\\ntasks_completed:\\n7\\nlast_summary_lines:\\n[pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate] success rate: 95.0% (19/20)\\n[pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate] success rate: 95.0% (19/20)\\n[pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\n[pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\n[pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate] success rate: 70.0% (14/20)\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate: 0.0% (0/20)\\n[pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\ncurrent_progress:\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollout 20/20, success so far: 20/20\\n[pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 5/20, success so far: 4/5\\n===== eval-supp-vla-only-spatial-s46.log =====\\ntasks_completed:\\n7\\nlast_summary_lines:\\n[pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate] success rate: 95.0% (19/20)\\n[pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate] success rate: 95.0% (19/20)\\n[pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\n[pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\n[pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate] success rate: 75.0% (15/20)\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate: 0.0% (0/20)\\n[pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate] success rate: 95.0% (19/20)\\ncurrent_progress:\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollout 15/20, success so far: 14/15\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollout 20/20, success so far: 19/20\\n[pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate] success rate: 95.0% (19/20)\\n===== eval-supp-crm-norm005-spatial-s45.log =====\\ntasks_completed:\\n7\\nlast_summary_lines:\\n[pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\n[pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\n[pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\n[pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\n[pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate] success rate: 70.0% (14/20)\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate: 0.0% (0/20)\\n[pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate] success rate: 95.0% (19/20)\\ncurrent_progress:\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollout 20/20, success so far: 19/20\\n[pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate] success rate: 95.0% (19/20)\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 5/20, success so far: 4/5\\n===== eval-supp-crm-norm005-spatial-s46.log =====\\ntasks_completed:\\n5\\nlast_summary_lines:\\n[pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate] success rate: 95.0% (19/20)\\n[pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\n[pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate] success rate: 95.0% (19/20)\\n[pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\n[pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate] success rate: 70.0% (14/20)\\ncurrent_progress:\\n[pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate] success rate: 70.0% (14/20)\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 5/20, success so far: 0/5\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 10/20, success so far: 0/10\\n===== eval-supp-adapt-tau025-spatial-s45.log =====\\ntasks_completed:\\n7\\nlast_summary_lines:\\n[pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate] success rate: 95.0% (19/20)\\n[pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate] success rate: 95.0% (19/20)\\n[pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\n[pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\n[pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate] success rate: 75.0% (15/20)\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate: 0.0% (0/20)\\n[pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\ncurrent_progress:\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollout 15/20, success so far: 15/15\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollout 20/20, success so far: 20/20\\n[pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "9ee46c69-bdeb-42be-b86d-8367db466b66",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"===== eval-supp-vla-only-spatial-s45.log =====\\\\ntasks_completed:\\\\n7\\\\nlast_summary_lines:\\\\n[pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate] success rate: 95.0% (19/20)\\\\n[pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate] success rate: 95.0% (19/20)\\\\n[pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\\\n[pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\\\n[pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate] success rate: 70.0% (14/20)\\\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate: 0.0% (0/20)\\\\n[pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\\\ncurrent_progress:\\\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollout 20/20, success so far: 20/20\\\\n[pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 5/20, success so far: 4/5\\\\n===== eval-supp-vla-only-spatial-s46.log =====\\\\ntasks_completed:\\\\n7\\\\nlast_summary_lines:\\\\n[pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate] success rate: 95.0% (19/20)\\\\n[pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate] success rate: 95.0% (19/20)\\\\n[pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\\\n[pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\\\n[pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate] success rate: 75.0% (15/20)\\\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate: 0.0% (0/20)\\\\n[pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate] success rate: 95.0% (19/20)\\\\ncurrent_progress:\\\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollout 15/20, success so far: 14/15\\\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollout 20/20, success so far: 19/20\\\\n[pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate] success rate: 95.0% (19/20)\\\\n===== eval-supp-crm-norm005-spatial-s45.log =====\\\\ntasks_completed:\\\\n7\\\\nlast_summary_lines:\\\\n[pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\\\n[pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\\\n[pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\\\n[pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\\\n[pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate] success rate: 70.0% (14/20)\\\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate: 0.0% (0/20)\\\\n[pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate] success rate: 95.0% (19/20)\\\\ncurrent_progress:\\\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollout 20/20, success so far: 19/20\\\\n[pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate] success rate: 95.0% (19/20)\\\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 5/20, success so far: 4/5\\\\n===== eval-supp-crm-norm005-spatial-s46.log =====\\\\ntasks_completed:\\\\n5\\\\nlast_summary_lines:\\\\n[pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate] success rate: 95.0% (19/20)\\\\n[pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\\\n[pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate] success rate: 95.0% (19/20)\\\\n[pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\\\n[pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate] success rate: 70.0% (14/20)\\\\ncurrent_progress:\\\\n[pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate] success rate: 70.0% (14/20)\\\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 5/20, success so far: 0/5\\\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 10/20, success so far: 0/10\\\\n===== eval-supp-adapt-tau025-spatial-s45.log =====\\\\ntasks_completed:\\\\n7\\\\nlast_summary_lines:\\\\n[pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate] success rate: 95.0% (19/20)\\\\n[pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate] success rate: 95.0% (19/20)\\\\n[pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\\\n[pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\\\n[pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate] success rate: 75.0% (15/20)\\\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate: 0.0% (0/20)\\\\n[pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\\\ncurrent_progress:\\\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollout 15/20, success so far: 15/15\\\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollout 20/20, success so far: 20/20\\\\n[pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"===== eval-supp-vla-only-spatial-s45.log =====\\ntasks_completed:\\n7\\nlast_summary_lines:\\n[pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate] success rate: 95.0% (19/20)\\n[pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate] success rate: 95.0% (19/20)\\n[pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\n[pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\n[pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate] success rate: 70.0% (14/20)\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate: 0.0% (0/20)\\n[pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\ncurrent_progress:\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollout 20/20, success so far: 20/20\\n[pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 5/20, success so far: 4/5\\n===== eval-supp-vla-only-spatial-s46.log =====\\ntasks_completed:\\n7\\nlast_summary_lines:\\n[pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate] success rate: 95.0% (19/20)\\n[pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate] success rate: 95.0% (19/20)\\n[pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\n[pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\n[pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate] success rate: 75.0% (15/20)\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate: 0.0% (0/20)\\n[pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate] success rate: 95.0% (19/20)\\ncurrent_progress:\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollout 15/20, success so far: 14/15\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollout 20/20, success so far: 19/20\\n[pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate] success rate: 95.0% (19/20)\\n===== eval-supp-crm-norm005-spatial-s45.log =====\\ntasks_completed:\\n7\\nlast_summary_lines:\\n[pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\n[pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\n[pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\n[pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\n[pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate] success rate: 70.0% (14/20)\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate: 0.0% (0/20)\\n[pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate] success rate: 95.0% (19/20)\\ncurrent_progress:\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollout 20/20, success so far: 19/20\\n[pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate] success rate: 95.0% (19/20)\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 5/20, success so far: 4/5\\n===== eval-supp-crm-norm005-spatial-s46.log =====\\ntasks_completed:\\n5\\nlast_summary_lines:\\n[pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate] success rate: 95.0% (19/20)\\n[pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\n[pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate] success rate: 95.0% (19/20)\\n[pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\n[pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate] success rate: 70.0% (14/20)\\ncurrent_progress:\\n[pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate] success rate: 70.0% (14/20)\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 5/20, success so far: 0/5\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 10/20, success so far: 0/10\\n===== eval-supp-adapt-tau025-spatial-s45.log =====\\ntasks_completed:\\n7\\nlast_summary_lines:\\n[pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate] success rate: 95.0% (19/20)\\n[pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate] success rate: 95.0% (19/20)\\n[pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\n[pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\n[pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate] success rate: 75.0% (15/20)\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate: 0.0% (0/20)\\n[pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\ncurrent_progress:\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollout 15/20, success so far: 15/15\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollout 20/20, success so far: 20/20\\n[pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate] success rate: 100.0% (20/20)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
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

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "0b6731bb-13d1-4088-8383-a93be233d3d1",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01DNrxmfMHfgSxMjmqxnQkhq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3837,
      "cache_read_input_tokens": 67959,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3837
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

### Tool call

_source line 66_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01MKYYv83H9D4czp5RAz8Fgu`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "find /root/acr-vla-conformal-refinement/logs -name \"eval_spatial*seed4[56]*.json\" -newer /root/acr-vla-conformal-refinement/logs/openvla_eval_object_vla_only_K1_seed42.json",
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
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "f4a16b7b-4b94-40c6-9ad9-45579ca01c6e",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01DNrxmfMHfgSxMjmqxnQkhq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3837,
      "cache_read_input_tokens": 67959,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3837
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

_source line 67 · 2026-05-24T08:27:07.637Z_

<details><summary>↩ Tool result · `toolu_01MKYYv83H9D4czp5RAz8Fgu`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "a84be20e-cfef-4be2-b41f-d4483208629d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.32}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 68_

No result JSONs yet — all 5 still mid-suite. Marking todos and reporting.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "0aed61ef-2270-43d4-9a87-ddc7911e7033",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_015fr514TNQhcEmqdfLDcHsy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1153,
      "cache_read_input_tokens": 71796,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1153
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

_source line 69_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01Hs7Xumc1dELfqbNgsfu8JA`</summary>

```json
{
  "todos": [
    {
      "content": "Confirm two lerobot exps already DONE — re-verify status",
      "activeForm": "Confirming lerobot exps status",
      "status": "completed"
    },
    {
      "content": "Check 5 Spatial exp processes on bjb2-28827",
      "activeForm": "Checking Spatial processes on bjb2-28827",
      "status": "completed"
    },
    {
      "content": "For each completed Spatial exp: harvest SR from JSON",
      "activeForm": "Harvesting SR from completed JSONs",
      "status": "completed"
    },
    {
      "content": "Report status/results to user",
      "activeForm": "Reporting results",
      "status": "in_progress"
    }
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
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "111e7fd1-a53f-41bd-a473-feb98f5face5",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_015fr514TNQhcEmqdfLDcHsy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1153,
      "cache_read_input_tokens": 71796,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1153
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

_source line 70 · 2026-05-24T08:27:13.346Z_

<details><summary>↩ Tool result · `toolu_01Hs7Xumc1dELfqbNgsfu8JA`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "bab909bc-6232-4fd5-8b51-c0096989ae03",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Confirm two lerobot exps already DONE — re-verify status",
        "status": "completed",
        "activeForm": "Confirming lerobot exps status"
      },
      {
        "content": "Check 5 Spatial exp processes on bjb2-28827",
        "status": "in_progress",
        "activeForm": "Checking Spatial processes on bjb2-28827"
      },
      {
        "content": "For each completed Spatial exp: harvest SR from JSON",
        "status": "pending",
        "activeForm": "Harvesting SR from completed JSONs"
      },
      {
        "content": "Report status/results to user",
        "status": "pending",
        "activeForm": "Reporting results"
      }
    ],
    "newTodos": [
      {
        "content": "Confirm two lerobot exps already DONE — re-verify status",
        "status": "completed",
        "activeForm": "Confirming lerobot exps status"
      },
      {
        "content": "Check 5 Spatial exp processes on bjb2-28827",
        "status": "completed",
        "activeForm": "Checking Spatial processes on bjb2-28827"
      },
      {
        "content": "For each completed Spatial exp: harvest SR from JSON",
        "status": "completed",
        "activeForm": "Harvesting SR from completed JSONs"
      },
      {
        "content": "Report status/results to user",
        "status": "in_progress",
        "activeForm": "Reporting results"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Assistant

_source line 71_

## 任务 1: stale lerobot 实验

两个实验在 registry 中**已是 DONE**，无需处理：
- `eval-smolvla-lerobot-goal-seed43-v3` — status=DONE, updated 2026-05-22T23:17:55
- `eval-smolvla-lerobot-spatial-seed43-v3` — status=DONE, updated 2026-05-22T23:17:49

任务描述中"RUNNING 更新于 5/22"与当前 registry 状态不符，可能是 stale 信息。

## 任务 2: bjb2-28827 上 5 个 Spatial 实验进度

**全部仍在运行**（5 个 Python 进程都在 R 状态，运行 1h11m–1h34m）。每 task 20 rollouts，suite 10 tasks，单 task 约 12 分钟。**没有 JSON 结果产出**，无需 registry 操作。

| GPU | 实验 | PID | 进度 | 已完成 task 累计 SR | 当前 task |
|-----|------|-----|------|---------------------|-----------|
| 0 | crm-norm005-spatial-s46 | 121241 | 5/10 task | 92/100 = **92.0%** | task 6（ramekin，rollout 10/20，0/10）— 仍在零成功的硬任务上 |
| 2 | vla-only-spatial-s45 | 96831 | 7/10 task | 112/140 = **80.0%** | task 8（stove，rollout 5/20，4/5） |
| 3 | adapt-tau025-spatial-s45 | 97307 | 7/10 task | 113/140 = **80.7%** | task 8 刚开始 |
| 4 | crm-norm005-spatial-s45 | 97070 | 7/10 task | 113/140 = **80.7%** | task 8（stove，rollout 5/20，4/5） |
| 5 | vla-only-spatial-s46 | 97550 | 7/10 task | 112/140 = **80.0%** | task 8 刚开始 |

**共同观察**：5 个实验都在 task 6 "ramekin" 任务（pick_up_the_black_bowl_on_the_ramekin）拿到 0/20，是该 suite 的 hard task；其他任务 SR 普遍 70-100%。

**预计完成时间**：s45 三个实验剩 3 个 task，约 36 分钟。s46 vla-only 也剩 3 个 task。s46 crm-norm005 还在 task 6 中段，剩 4.5 个 task，约 50-60 分钟。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "uuid": "d8b9d3e0-32a3-484a-bb04-a53042ff2237",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01YbaQVrKQ1RAJVfBGY4GGUA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 370,
      "cache_read_input_tokens": 72949,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 370
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

_source line 72_

## 任务 1: stale lerobot 实验

两个实验在 registry 中**已是 DONE**，无需处理：
- `eval-smolvla-lerobot-goal-seed43-v3` — status=DONE, updated 2026-05-22T23:17:55
- `eval-smolvla-lerobot-spatial-seed43-v3` — status=DONE, updated 2026-05-22T23:17:49

任务描述中"RUNNING 更新于 5/22"与当前 registry 状态不符，可能是 stale 信息。

## 任务 2: bjb2-28827 上 5 个 Spatial 实验进度

**全部仍在运行**（5 个 Python 进程都在 R 状态，运行 1h11m–1h34m）。每 task 20 rollouts，suite 10 tasks，单 task 约 12 分钟。**没有 JSON 结果产出**，无需 registry 操作。

| GPU | 实验 | PID | 进度 | 已完成 task 累计 SR | 当前 task |
|-----|------|-----|------|---------------------|-----------|
| 0 | crm-norm005-spatial-s46 | 121241 | 5/10 task | 92/100 = **92.0%** | task 6（ramekin，rollout 10/20，0/10）— 仍在零成功的硬任务上 |
| 2 | vla-only-spatial-s45 | 96831 | 7/10 task | 112/140 = **80.0%** | task 8（stove，rollout 5/20，4/5） |
| 3 | adapt-tau025-spatial-s45 | 97307 | 7/10 task | 113/140 = **80.7%** | task 8 刚开始 |
| 4 | crm-norm005-spatial-s45 | 97070 | 7/10 task | 113/140 = **80.7%** | task 8（stove，rollout 5/20，4/5） |
| 5 | vla-only-spatial-s46 | 97550 | 7/10 task | 112/140 = **80.0%** | task 8 刚开始 |

**共同观察**：5 个实验都在 task 6 "ramekin" 任务（pick_up_the_black_bowl_on_the_ramekin）拿到 0/20，是该 suite 的 hard task；其他任务 SR 普遍 70-100%。

**预计完成时间**：s45 三个实验剩 3 个 task，约 36 分钟。s46 vla-only 也剩 3 个 task。s46 crm-norm005 还在 task 6 中段，剩 4.5 个 task，约 50-60 分钟。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 203436,
  "duration_api_ms": 188933,
  "num_turns": 27,
  "stop_reason": "end_turn",
  "session_id": "7b80dd05-6aec-4cda-b61a-b5ef1300a0d5",
  "total_cost_usd": 1.34043075,
  "usage": {
    "input_tokens": 41,
    "cache_creation_input_tokens": 71651,
    "cache_read_input_tokens": 1351284,
    "output_tokens": 8616,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 71651,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 878,
        "cache_read_input_tokens": 72949,
        "cache_creation_input_tokens": 370,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 370
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1285,
      "outputTokens": 16,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001365,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-7[1m]": {
      "inputTokens": 41,
      "outputTokens": 8616,
      "cacheReadInputTokens": 1351284,
      "cacheCreationInputTokens": 71651,
      "webSearchRequests": 0,
      "costUSD": 1.33906575,
      "contextWindow": 1000000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "ed5503ac-fe41-492d-be36-67a560d762e8"
}
```

</details>

---
