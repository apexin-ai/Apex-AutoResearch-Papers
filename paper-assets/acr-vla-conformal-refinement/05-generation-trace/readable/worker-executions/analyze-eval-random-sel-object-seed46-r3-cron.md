# analyze eval random sel object seed46 r3 cron

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 24
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/workers/worker_analyze_eval-random-sel-object-seed46-r3-cron_20260520T175107.log`
- **Structured JSON:** [`78bd2af2f0abb54c5548.json`](../../sessions/78/78bd2af2f0abb54c5548.json)

## Before a recorded user message

24 recorded events

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
  "session_id": "c5300403-6659-4470-875e-d77ab58a370d",
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
    "mcp__agent-ml-research__delete_cron",
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
  "uuid": "568cb8ff-9345-4aab-ad66-56bcd09af486",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/memory/"
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
    "status": "allowed_warning",
    "resetsAt": 1779469200,
    "rateLimitType": "seven_day",
    "utilization": 0.87,
    "isUsingOverage": false,
    "surpassedThreshold": 0.75
  },
  "uuid": "0cb21d6c-580b-46a5-9e34-7a04fe3f661a",
  "session_id": "c5300403-6659-4470-875e-d77ab58a370d"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the registry for this experiment, then proceed with the diagnosis.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c5300403-6659-4470-875e-d77ab58a370d",
  "uuid": "2ce8cad9-c555-46af-b223-f93b05a1d9bd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q5ajuvi2jffuUxo9yy6zcW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11544,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11544
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

_source line 5_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01AE82ukgdNytrLsnTHbrZmc`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__delete_cron,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
  "max_results": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c5300403-6659-4470-875e-d77ab58a370d",
  "uuid": "67d04433-5056-45f0-88a3-a3cd97739462",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q5ajuvi2jffuUxo9yy6zcW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11544,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11544
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

_source line 6 · 2026-05-20T17:51:22.981Z_

<details><summary>↩ Tool result · `toolu_01AE82ukgdNytrLsnTHbrZmc`</summary>

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
  "tool_name": "mcp__agent-ml-research__update_registry"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__delete_cron"
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
  "session_id": "c5300403-6659-4470-875e-d77ab58a370d",
  "uuid": "57fef0ba-c494-4f0e-84bb-62235ff27cb1",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__update_registry",
      "mcp__agent-ml-research__delete_cron",
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__ssh_execute"
    ],
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__delete_cron,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
    "total_deferred_tools": 27
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01UWeHvpFR8Y5egxTk9WWzsX`</summary>

```json
{
  "filters": {
    "exp_id": "eval-random-selection-object-seed46-r3"
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
  "session_id": "c5300403-6659-4470-875e-d77ab58a370d",
  "uuid": "056188bc-fd42-4527-97fb-ca3e67680f01",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W6aLH1aDJ7wi1XmrzkoorJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1663,
      "cache_read_input_tokens": 23385,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1663
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

_source line 8 · 2026-05-20T17:51:27.640Z_

<details><summary>↩ Tool result · `toolu_01UWeHvpFR8Y5egxTk9WWzsX`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.2433}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c5300403-6659-4470-875e-d77ab58a370d",
  "uuid": "b98105b4-0828-4f8a-b42b-b98f8e7f2743",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.2433}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.2433}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 9_

<details><summary>Logged reasoning block</summary>

```text
No results with exp_id filter. Let me try a broader search to find this experiment.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c5300403-6659-4470-875e-d77ab58a370d",
  "uuid": "ec129f49-9d67-4160-943e-43c5ee28a31b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SChXAo5ifU66PJN6b9cpnw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 207,
      "cache_read_input_tokens": 25048,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 207
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

_source line 10_

没有精确匹配，扩大搜索范围。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c5300403-6659-4470-875e-d77ab58a370d",
  "uuid": "567d24c1-7e4b-453f-b09e-cf93eb8e7b3f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SChXAo5ifU66PJN6b9cpnw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 207,
      "cache_read_input_tokens": 25048,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 207
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

_source line 11_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_019v2ky78pBnx6BN46AgQdg1`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "fields": [
    "*"
  ],
  "filters": {
    "status": "RUNNING"
  },
  "limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c5300403-6659-4470-875e-d77ab58a370d",
  "uuid": "95eb583d-f717-4585-82da-e4b0012daf31",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SChXAo5ifU66PJN6b9cpnw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 207,
      "cache_read_input_tokens": 25048,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 207
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

_source line 12 · 2026-05-20T17:51:37.173Z_

<details><summary>↩ Tool result · `toolu_019v2ky78pBnx6BN46AgQdg1`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-obs-only-object-norm02-seed51\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:31:57.442Z\", \"updated_at\": \"2026-05-20T17:34:30.397Z\", \"hypothesis\": \"CRM obs_only (ε=0.2) K=10 on LIBERO-Object seed51. Expanding Object CRM seed coverage.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 51 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_obs_only_object_norm02_seed51.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"CRM_obs_only\", \"seed\": 51, \"checkpoint_source\": \"crm_v3_norm/obs_only/crm_best.pt\", \"backend\": \"tmux\", \"account\": \"root\", \"log_path\": \"logs/eval-obs-only-object-norm02-seed51.log\"}}, \"eval-vla-only-object-seed49\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-19T21:15:12.591Z\", \"updated_at\": \"2026-05-20T17:34:26.374Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Object seed49. Expanding VLA-only baseline seed coverage for Object benchmark.\", \"completed_at\": \"2026-05-19T22:08:11.590Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"killed\"}}, \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark object --seed 49 --n_rollouts 10 --K 1 --output_file logs/eval_vla_only_object_seed49.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA\", \"seed\": 49, \"checkpoint_source\": \"N/A\", \"backend\": \"tmux\", \"account\": \"root\", \"log_path\": \"logs/eval-vla-only-object-seed49.log\"}}, \"eval-perdof-object-norm02-seed50\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:31:51.325Z\", \"updated_at\": \"2026-05-20T17:34:20.913Z\", \"hypothesis\": \"perdof CRM (ε=0.2) K=10 on LIBERO-Object seed50. Additional perdof seed for multi-seed robustness.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_perdof --benchmark object --seed 50 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_perdof_object_norm02_seed50.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"CRM_perdof\", \"seed\": 50, \"checkpoint_source\": \"crm_v3_norm/perdof/crm_best.pt\", \"backend\": \"tmux\", \"account\": \"root\", \"log_path\": \"logs/eval-perdof-object-norm02-seed50.log\"}}, \"eval-obs-only-spatial-norm02-seed50\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:31:49.315Z\", \"updated_at\": \"2026-05-20T17:34:16.277Z\", \"hypothesis\": \"CRM obs_only (ε=0.2) K=10 on LIBERO-Spatial seed50. Additional spatial seed for multi-seed robustness.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --seed 50 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_obs_only_spatial_norm02_seed50.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"CRM_obs_only\", \"seed\": 50, \"checkpoint_source\": \"crm_v3_norm/obs_only/crm_best.pt\", \"backend\": \"tmux\", \"account\": \"root\", \"log_path\": \"logs/eval-obs-only-spatial-norm02-seed50.log\"}}, \"eval-random-selection-spatial-seed42-r3\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:30:38.520Z\", \"updated_at\": \"2026-05-20T17:31:53.363Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode random_selection --benchmark spatial --seed 42 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_random_selection_spatial_seed42_r3.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"SmolVLA_random_selection\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\"}, \"hypothesis\": \"Random selection baseline (K=10 uniform random) on LIBERO-Spatial seed42. Third attempt after prior kills.\"}, \"eval-obs-only-object-norm003-seed44\": {\"status\": \"RUNNING\", \"retry_count\": 2, \"created_at\": \"2026-05-18T15:15:11.377Z\", \"updated_at\": \"2026-05-20T17:31:34.166Z\", \"hypothesis\": \"CRM obs_only ε=0.03 on Object seed44. Low-norm multi-seed supplement (plan_500): strengthens Figure 2 error bars at small ε.\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-32546\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-18T15:16:33.436Z\", \"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_obs_only_norm003_seed44.json\", \"finished_at\": \"2026-05-20T10:49:41.211Z\", \"training_hours\": 43.55}, \"failure_reason\": \"\", \"completed_at\": \"2026-05-18T21:18:43.893Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T21:18:53.264334+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T10:50:07.963621+00:00\"}], \"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 15, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 30, \"bbq_sauce\": 20, \"ketchup\": 0, \"tomato_sauce\": 10, \"butter\": 10, \"milk\": 20, \"chocolate_pudding\": 30, \"orange_juice\": 30}}, \"notes\": \"失败原因: timeout (EXIT_CODE=124), 与 seed45 相同模式——运行 ~6h 后超时。需增大 timeout_hours 后重提交。\"}}, \"notes\": \"失败原因: timeout (EXIT_CODE=124), 与 seed45 相同模式——运行 ~6h 后超时。需增大 timeout_hours 后重提交。\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 44 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_obs_only_object_norm003_seed44.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only_norm003\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}}, \"eval-obs-only-object-norm005-seed44\": {\"status\": \"RUNNING\", \"retry_count\": 2, \"created_at\": \"2026-05-17T23:10:56.103Z\", \"updated_at\": \"2026-05-20T17:31:26.448Z\", \"hypothesis\": \"CRM obs_only ε=0.05 on Object seed44. Low-norm multi-seed supplement (plan_500): strengthens Figure 2 error bars at small ε.\", \"reproduce\": {\"finished_at\": \"2026-05-20T10:34:28.733Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T13:04:15.652922+00:00\"}], \"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 12, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0, \"bbq_sauce\": 30, \"ketchup\": 0, \"tomato_sauce\": 10, \"butter\": 10, \"milk\": 20, \"chocolate_pudding\": 20, \"orange_juice\": 30}}}}, \"completed_at\": \"2026-05-18T13:07:06.200Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 44 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_obs_only_object_norm005_seed44.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only_norm005\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}}, \"eval-k20-obs-only-object-seed44\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:19:11.419Z\", \"updated_at\": \"2026-05-20T17:20:44.391Z\", \"hypothesis\": \"K=20 CRM obs_only (ε=0.2) on LIBERO-Object seed44. K sweep for plan_601.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 44 --n_rollouts 10 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k20_obs_only_object_seed44.json\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:5\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"crm_obs_only\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}}, \"eval-k5-obs-only-object-seed44\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:19:08.706Z\", \"updated_at\": \"2026-05-20T17:20:34.181Z\", \"hypothesis\": \"K=5 CRM obs_only (ε=0.2) on LIBERO-Object seed44. K sweep for plan_601.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 44 --n_rollouts 10 --K 5 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k5_obs_only_object_seed44.json\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:2\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"crm_obs_only\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}}, \"eval-adaptive-unc-head-object-seed43\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:19:04.464Z\", \"updated_at\": \"2026-05-20T17:20:18.271Z\", \"hypothesis\": \"D088 方案 B 验证：Learned Uncertainty Head (τ=0.42) + K=1 VLA + Selective CRM correction on LIBERO-Object seed43. 测试 uncertainty-gated CRM 是否能在 K=1 延迟下保持接近 K=10 的 SR。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 43 --n_rollouts 10 --K 1 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2 --output_file logs/eval_adaptive_unc_head_object_seed43.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"UncHead_tau0.42_K1_CRM\", \"checkpoint_source\": \"crm_v3_norm/obs_only/crm_best.pt + uncertainty_head_v1/uncertainty_head_best.pt\", \"seed\": 43, \"backend\": \"tmux\", \"account\": \"root\", \"log_path\": \"logs/eval-adaptive-unc-head-object-seed43.log\"}}, \"eval-adaptive-unc-head-object-seed42\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:18:59.700Z\", \"updated_at\": \"2026-05-20T17:20:06.873Z\", \"hypothesis\": \"D088 方案 B 验证：Learned Uncertainty Head (τ=0.42) + K=1 VLA + Selective CRM correction on LIBERO-Object seed42. 测试 uncertainty-gated CRM 是否能在 K=1 延迟下保持接近 K=10 的 SR。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 42 --n_rollouts 10 --K 1 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2 --output_file logs/eval_adaptive_unc_head_object_seed42.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"UncHead_tau0.42_K1_CRM\", \"checkpoint_source\": \"crm_v3_norm/obs_only/crm_best.pt + uncertainty_head_v1/uncertainty_head_best.pt\", \"seed\": 42, \"backend\": \"tmux\", \"account\": \"root\", \"log_path\": \"logs/eval-adaptive-unc-head-object-seed42.log\"}}, \"eval-obs-only-object-norm003-seed43\": {\"status\": \"RUNNING\", \"retry_count\": 2, \"created_at\": \"2026-05-17T13:33:23.925Z\", \"updated_at\": \"2026-05-20T17:19:21.817Z\", \"hypothesis\": \"CRM obs_only ε=0.03 on Object seed43. Low-norm supplement for plan_500 magnitude curve.\", \"notes\": \"PID 621127 on bjb1-18228 cuda:1 died. Process not found, GPU idle. Ghost experiment discovered during registration attempt.\", \"completed_at\": \"2026-05-17T13:33:52.018Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"PID 621127 on bjb1-18228 cuda:1 died. Process not found, GPU idle. Ghost experiment discovered during registration attempt.\"}, \"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T20:40:06.367656+00:00\"}]}, \"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-18T14:37:56.416Z\", \"command\": \"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_obs_only_norm003_seed43.json\", \"finished_at\": \"2026-05-18T20:39:52.321Z\", \"training_hours\": 6.03}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 43 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_obs_only_object_norm003_seed43.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"CRM_obs_only\", \"checkpoint_source\": \"crm_v3_norm/obs_only/crm_best.pt\", \"seed\": 43, \"backend\": \"tmux\", \"account\": \"root\", \"log_path\": \"logs/eval-obs-only-object-norm003-seed43.log\"}}, \"D088-eval-adaptive-unc-head-object-seed44\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:00:46.028Z\", \"updated_at\": \"2026-05-20T17:02:30.624Z\", \"hypothesis\": \"D088 方案 B: Learned Uncertainty Head (τ=0.42) + K=1 VLA + Selective CRM on LIBERO-Object seed44. n_rollouts=100 for statistical significance. 测试 uncertainty-gated selective CRM 在固定延迟(K=1)下能否保持接近 K=10 CRM 的 SR。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 44 --n_rollouts 100 --K 1 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2 --output_file logs/eval_adaptive_unc_head_object_seed44.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"data_path\": \"LIBERO-Object\", \"data_count\": 1000, \"model_name\": \"UncertaintyHead+CRM_obs_only\", \"checkpoint_source\": \"uncertainty_head_v1/uncertainty_head_best.pt\", \"seed\": 44, \"backend\": \"tmux\", \"account\": \"root\", \"log_path\": \"logs/eval-adaptive-unc-head-object-seed44.log\"}}, \"D088-eval-adaptive-unc-head-object-seed43\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:00:42.469Z\", \"updated_at\": \"2026-05-20T17:02:26.585Z\", \"hypothesis\": \"D088 方案 B: Learned Uncertainty Head (τ=0.42) + K=1 VLA + Selective CRM on LIBERO-Object seed43. n_rollouts=100 for statistical significance. 测试 uncertainty-gated selective CRM 在固定延迟(K=1)下能否保持接近 K=10 CRM 的 SR。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 43 --n_rollouts 100 --K 1 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2 --output_file logs/eval_adaptive_unc_head_object_seed43.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"data_path\": \"LIBERO-Object\", \"data_count\": 1000, \"model_name\": \"UncertaintyHead+CRM_obs_only\", \"checkpoint_source\": \"uncertainty_head_v1/uncertainty_head_best.pt\", \"seed\": 43, \"backend\": \"tmux\", \"account\": \"root\", \"log_path\": \"logs/eval-adaptive-unc-head-object-seed43.log\"}}, \"D088-eval-adaptive-unc-head-object-seed42\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:00:39.505Z\", \"updated_at\": \"2026-05-20T17:02:22.505Z\", \"hypothesis\": \"D088 方案 B: Learned Uncertainty Head (τ=0.42) + K=1 VLA + Selective CRM on LIBERO-Object seed42. n_rollouts=100 for statistical significance. 测试 uncertainty-gated selective CRM 在固定延迟(K=1)下能否保持接近 K=10 CRM 的 SR。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 42 --n_rollouts 100 --K 1 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2 --output_file logs/eval_adaptive_unc_head_object_seed42.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"data_path\": \"LIBERO-Object\", \"data_count\": 1000, \"model_name\": \"UncertaintyHead+CRM_obs_only\", \"checkpoint_source\": \"uncertainty_head_v1/uncertainty_head_best.pt\", \"seed\": 42, \"backend\": \"tmux\", \"account\": \"root\", \"log_path\": \"logs/eval-adaptive-unc-head-object-seed42.log\"}}, \"eval-adaptive-unc-head-object-seed44\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T16:52:03.117Z\", \"updated_at\": \"2026-05-20T17:00:27.101Z\", \"hypothesis\": \"D088 方案 B 验证：Learned Uncertainty Head (τ=0.42) + K=1 VLA + Selective CRM correction on LIBERO-Object seed44. 测试 uncertainty-gated CRM 是否能在 K=1 延迟下保持接近 K=10 的 SR。\", \"plan_id\": \"d088\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 44 --n_rollouts 10 --K 1 --crm_checkpoint crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:5\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"UncertaintyHead+CRM_obs_only\", \"seed\": 44, \"checkpoint_source\": \"uncertainty_head_v1/uncertainty_head_best.pt\", \"pid\": 728278, \"log_path\": \"logs/eval-adaptive-unc-head-object-seed44.log\"}}, \"openvla-precompute-k1\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T13:49:30.105Z\", \"updated_at\": \"2026-05-20T13:51:42.391Z\", \"spec\": {\"command\": \"python precompute_openvla.py --device cuda:0 --max_demos_per_task 50 --cache_dir /root/autodl-tmp/crm_cache_k1_openvla/\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"365142\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/openvla-precompute-k1.log\", \"submitted_at\": \"2026-05-20T13:49:29.016Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_object/\", \"data_count\": 74507, \"model_name\": \"openvla-libero-object\", \"seed\": 42}, \"hypothesis\": \"Precomputing OpenVLA hidden features at quartile layers [7,15,23,31] will produce multi-scale representations (4×4096) compatible with the CRM K=1 training pipeline, enabling backbone-agnostic conformal refinement.\"}}, \"count\": 17, \"total\": 17, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.4604}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c5300403-6659-4470-875e-d77ab58a370d",
  "uuid": "0bfa01bc-76d5-404a-8798-763fdd0746ef",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"eval-obs-only-object-norm02-seed51\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T17:31:57.442Z\\\", \\\"updated_at\\\": \\\"2026-05-20T17:34:30.397Z\\\", \\\"hypothesis\\\": \\\"CRM obs_only (ε=0.2) K=10 on LIBERO-Object seed51. Expanding Object CRM seed coverage.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 51 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_obs_only_object_norm02_seed51.json\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:4\\\"], \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"CRM_obs_only\\\", \\\"seed\\\": 51, \\\"checkpoint_source\\\": \\\"crm_v3_norm/obs_only/crm_best.pt\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"log_path\\\": \\\"logs/eval-obs-only-object-norm02-seed51.log\\\"}}, \\\"eval-vla-only-object-seed49\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 1, \\\"created_at\\\": \\\"2026-05-19T21:15:12.591Z\\\", \\\"updated_at\\\": \\\"2026-05-20T17:34:26.374Z\\\", \\\"hypothesis\\\": \\\"VLA-only baseline on LIBERO-Object seed49. Expanding VLA-only baseline seed coverage for Object benchmark.\\\", \\\"completed_at\\\": \\\"2026-05-19T22:08:11.590Z\\\", \\\"extra\\\": {\\\"previous_failure\\\": {\\\"conclusion\\\": \\\"killed\\\"}}, \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode vla_only --benchmark object --seed 49 --n_rollouts 10 --K 1 --output_file logs/eval_vla_only_object_seed49.json\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 49, \\\"checkpoint_source\\\": \\\"N/A\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"log_path\\\": \\\"logs/eval-vla-only-object-seed49.log\\\"}}, \\\"eval-perdof-object-norm02-seed50\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T17:31:51.325Z\\\", \\\"updated_at\\\": \\\"2026-05-20T17:34:20.913Z\\\", \\\"hypothesis\\\": \\\"perdof CRM (ε=0.2) K=10 on LIBERO-Object seed50. Additional perdof seed for multi-seed robustness.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode crm_perdof --benchmark object --seed 50 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_perdof_object_norm02_seed50.json\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"CRM_perdof\\\", \\\"seed\\\": 50, \\\"checkpoint_source\\\": \\\"crm_v3_norm/perdof/crm_best.pt\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"log_path\\\": \\\"logs/eval-perdof-object-norm02-seed50.log\\\"}}, \\\"eval-obs-only-spatial-norm02-seed50\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T17:31:49.315Z\\\", \\\"updated_at\\\": \\\"2026-05-20T17:34:16.277Z\\\", \\\"hypothesis\\\": \\\"CRM obs_only (ε=0.2) K=10 on LIBERO-Spatial seed50. Additional spatial seed for multi-seed robustness.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --seed 50 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_obs_only_spatial_norm02_seed50.json\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"CRM_obs_only\\\", \\\"seed\\\": 50, \\\"checkpoint_source\\\": \\\"crm_v3_norm/obs_only/crm_best.pt\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"log_path\\\": \\\"logs/eval-obs-only-spatial-norm02-seed50.log\\\"}}, \\\"eval-random-selection-spatial-seed42-r3\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T17:30:38.520Z\\\", \\\"updated_at\\\": \\\"2026-05-20T17:31:53.363Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode random_selection --benchmark spatial --seed 42 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_random_selection_spatial_seed42_r3.json\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"SmolVLA_random_selection\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial\\\"}, \\\"hypothesis\\\": \\\"Random selection baseline (K=10 uniform random) on LIBERO-Spatial seed42. Third attempt after prior kills.\\\"}, \\\"eval-obs-only-object-norm003-seed44\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 2, \\\"created_at\\\": \\\"2026-05-18T15:15:11.377Z\\\", \\\"updated_at\\\": \\\"2026-05-20T17:31:34.166Z\\\", \\\"hypothesis\\\": \\\"CRM obs_only ε=0.03 on Object seed44. Low-norm multi-seed supplement (plan_500): strengthens Figure 2 error bars at small ε.\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"account\\\": \\\"root\\\", \\\"reproduce\\\": {\\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"started_at\\\": \\\"2026-05-18T15:16:33.436Z\\\", \\\"command\\\": \\\"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_obs_only_norm003_seed44.json\\\", \\\"finished_at\\\": \\\"2026-05-20T10:49:41.211Z\\\", \\\"training_hours\\\": 43.55}, \\\"failure_reason\\\": \\\"\\\", \\\"completed_at\\\": \\\"2026-05-18T21:18:43.893Z\\\", \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-18T21:18:53.264334+00:00\\\"}, {\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-20T10:50:07.963621+00:00\\\"}], \\\"previous_failure\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 15, \\\"total_rollouts\\\": 100, \\\"per_task\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0, \\\"salad_dressing\\\": 30, \\\"bbq_sauce\\\": 20, \\\"ketchup\\\": 0, \\\"tomato_sauce\\\": 10, \\\"butter\\\": 10, \\\"milk\\\": 20, \\\"chocolate_pudding\\\": 30, \\\"orange_juice\\\": 30}}, \\\"notes\\\": \\\"失败原因: timeout (EXIT_CODE=124), 与 seed45 相同模式——运行 ~6h 后超时。需增大 timeout_hours 后重提交。\\\"}}, \\\"notes\\\": \\\"失败原因: timeout (EXIT_CODE=124), 与 seed45 相同模式——运行 ~6h 后超时。需增大 timeout_hours 后重提交。\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 44 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_obs_only_object_norm003_seed44.json\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"SmolVLA+CRM_obs_only_norm003\\\", \\\"seed\\\": 44, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\"}}, \\\"eval-obs-only-object-norm005-seed44\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 2, \\\"created_at\\\": \\\"2026-05-17T23:10:56.103Z\\\", \\\"updated_at\\\": \\\"2026-05-20T17:31:26.448Z\\\", \\\"hypothesis\\\": \\\"CRM obs_only ε=0.05 on Object seed44. Low-norm multi-seed supplement (plan_500): strengthens Figure 2 error bars at small ε.\\\", \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-20T10:34:28.733Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-18T13:04:15.652922+00:00\\\"}], \\\"previous_failure\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 12, \\\"total_rollouts\\\": 100, \\\"per_task\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0, \\\"salad_dressing\\\": 0, \\\"bbq_sauce\\\": 30, \\\"ketchup\\\": 0, \\\"tomato_sauce\\\": 10, \\\"butter\\\": 10, \\\"milk\\\": 20, \\\"chocolate_pudding\\\": 20, \\\"orange_juice\\\": 30}}}}, \\\"completed_at\\\": \\\"2026-05-18T13:07:06.200Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 44 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_obs_only_object_norm005_seed44.json\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"SmolVLA+CRM_obs_only_norm005\\\", \\\"seed\\\": 44, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\"}}, \\\"eval-k20-obs-only-object-seed44\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T17:19:11.419Z\\\", \\\"updated_at\\\": \\\"2026-05-20T17:20:44.391Z\\\", \\\"hypothesis\\\": \\\"K=20 CRM obs_only (ε=0.2) on LIBERO-Object seed44. K sweep for plan_601.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 44 --n_rollouts 10 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k20_obs_only_object_seed44.json\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": \\\"cuda:5\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"crm_obs_only\\\", \\\"seed\\\": 44, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\"}}, \\\"eval-k5-obs-only-object-seed44\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T17:19:08.706Z\\\", \\\"updated_at\\\": \\\"2026-05-20T17:20:34.181Z\\\", \\\"hypothesis\\\": \\\"K=5 CRM obs_only (ε=0.2) on LIBERO-Object seed44. K sweep for plan_601.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 44 --n_rollouts 10 --K 5 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k5_obs_only_object_seed44.json\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": \\\"cuda:2\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"crm_obs_only\\\", \\\"seed\\\": 44, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\\\"}}, \\\"eval-adaptive-unc-head-object-seed43\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T17:19:04.464Z\\\", \\\"updated_at\\\": \\\"2026-05-20T17:20:18.271Z\\\", \\\"hypothesis\\\": \\\"D088 方案 B 验证：Learned Uncertainty Head (τ=0.42) + K=1 VLA + Selective CRM correction on LIBERO-Object seed43. 测试 uncertainty-gated CRM 是否能在 K=1 延迟下保持接近 K=10 的 SR。\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 43 --n_rollouts 10 --K 1 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2 --output_file logs/eval_adaptive_unc_head_object_seed43.json\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"UncHead_tau0.42_K1_CRM\\\", \\\"checkpoint_source\\\": \\\"crm_v3_norm/obs_only/crm_best.pt + uncertainty_head_v1/uncertainty_head_best.pt\\\", \\\"seed\\\": 43, \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"log_path\\\": \\\"logs/eval-adaptive-unc-head-object-seed43.log\\\"}}, \\\"eval-adaptive-unc-head-object-seed42\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T17:18:59.700Z\\\", \\\"updated_at\\\": \\\"2026-05-20T17:20:06.873Z\\\", \\\"hypothesis\\\": \\\"D088 方案 B 验证：Learned Uncertainty Head (τ=0.42) + K=1 VLA + Selective CRM correction on LIBERO-Object seed42. 测试 uncertainty-gated CRM 是否能在 K=1 延迟下保持接近 K=10 的 SR。\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 42 --n_rollouts 10 --K 1 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2 --output_file logs/eval_adaptive_unc_head_object_seed42.json\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"UncHead_tau0.42_K1_CRM\\\", \\\"checkpoint_source\\\": \\\"crm_v3_norm/obs_only/crm_best.pt + uncertainty_head_v1/uncertainty_head_best.pt\\\", \\\"seed\\\": 42, \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"log_path\\\": \\\"logs/eval-adaptive-unc-head-object-seed42.log\\\"}}, \\\"eval-obs-only-object-norm003-seed43\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 2, \\\"created_at\\\": \\\"2026-05-17T13:33:23.925Z\\\", \\\"updated_at\\\": \\\"2026-05-20T17:19:21.817Z\\\", \\\"hypothesis\\\": \\\"CRM obs_only ε=0.03 on Object seed43. Low-norm supplement for plan_500 magnitude curve.\\\", \\\"notes\\\": \\\"PID 621127 on bjb1-18228 cuda:1 died. Process not found, GPU idle. Ghost experiment discovered during registration attempt.\\\", \\\"completed_at\\\": \\\"2026-05-17T13:33:52.018Z\\\", \\\"extra\\\": {\\\"previous_failure\\\": {\\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"PID 621127 on bjb1-18228 cuda:1 died. Process not found, GPU idle. Ghost experiment discovered during registration attempt.\\\"}, \\\"hook_events\\\": [{\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-18T20:40:06.367656+00:00\\\"}]}, \\\"server\\\": \\\"bjb1-18228\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"account\\\": \\\"root\\\", \\\"reproduce\\\": {\\\"server\\\": \\\"bjb1-18228\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"started_at\\\": \\\"2026-05-18T14:37:56.416Z\\\", \\\"command\\\": \\\"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_obs_only_norm003_seed43.json\\\", \\\"finished_at\\\": \\\"2026-05-18T20:39:52.321Z\\\", \\\"training_hours\\\": 6.03}, \\\"failure_reason\\\": \\\"EXIT_CODE=129 (non-zero)\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 43 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_obs_only_object_norm003_seed43.json\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"gpu\\\": [\\\"cuda:4\\\"], \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"CRM_obs_only\\\", \\\"checkpoint_source\\\": \\\"crm_v3_norm/obs_only/crm_best.pt\\\", \\\"seed\\\": 43, \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"log_path\\\": \\\"logs/eval-obs-only-object-norm003-seed43.log\\\"}}, \\\"D088-eval-adaptive-unc-head-object-seed44\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T17:00:46.028Z\\\", \\\"updated_at\\\": \\\"2026-05-20T17:02:30.624Z\\\", \\\"hypothesis\\\": \\\"D088 方案 B: Learned Uncertainty Head (τ=0.42) + K=1 VLA + Selective CRM on LIBERO-Object seed44. n_rollouts=100 for statistical significance. 测试 uncertainty-gated selective CRM 在固定延迟(K=1)下能否保持接近 K=10 CRM 的 SR。\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 44 --n_rollouts 100 --K 1 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2 --output_file logs/eval_adaptive_unc_head_object_seed44.json\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"gpu\\\": [\\\"cuda:4\\\"], \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 1000, \\\"model_name\\\": \\\"UncertaintyHead+CRM_obs_only\\\", \\\"checkpoint_source\\\": \\\"uncertainty_head_v1/uncertainty_head_best.pt\\\", \\\"seed\\\": 44, \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"log_path\\\": \\\"logs/eval-adaptive-unc-head-object-seed44.log\\\"}}, \\\"D088-eval-adaptive-unc-head-object-seed43\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T17:00:42.469Z\\\", \\\"updated_at\\\": \\\"2026-05-20T17:02:26.585Z\\\", \\\"hypothesis\\\": \\\"D088 方案 B: Learned Uncertainty Head (τ=0.42) + K=1 VLA + Selective CRM on LIBERO-Object seed43. n_rollouts=100 for statistical significance. 测试 uncertainty-gated selective CRM 在固定延迟(K=1)下能否保持接近 K=10 CRM 的 SR。\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 43 --n_rollouts 100 --K 1 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2 --output_file logs/eval_adaptive_unc_head_object_seed43.json\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 1000, \\\"model_name\\\": \\\"UncertaintyHead+CRM_obs_only\\\", \\\"checkpoint_source\\\": \\\"uncertainty_head_v1/uncertainty_head_best.pt\\\", \\\"seed\\\": 43, \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"log_path\\\": \\\"logs/eval-adaptive-unc-head-object-seed43.log\\\"}}, \\\"D088-eval-adaptive-unc-head-object-seed42\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T17:00:39.505Z\\\", \\\"updated_at\\\": \\\"2026-05-20T17:02:22.505Z\\\", \\\"hypothesis\\\": \\\"D088 方案 B: Learned Uncertainty Head (τ=0.42) + K=1 VLA + Selective CRM on LIBERO-Object seed42. n_rollouts=100 for statistical significance. 测试 uncertainty-gated selective CRM 在固定延迟(K=1)下能否保持接近 K=10 CRM 的 SR。\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 42 --n_rollouts 100 --K 1 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2 --output_file logs/eval_adaptive_unc_head_object_seed42.json\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 1000, \\\"model_name\\\": \\\"UncertaintyHead+CRM_obs_only\\\", \\\"checkpoint_source\\\": \\\"uncertainty_head_v1/uncertainty_head_best.pt\\\", \\\"seed\\\": 42, \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"log_path\\\": \\\"logs/eval-adaptive-unc-head-object-seed42.log\\\"}}, \\\"eval-adaptive-unc-head-object-seed44\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T16:52:03.117Z\\\", \\\"updated_at\\\": \\\"2026-05-20T17:00:27.101Z\\\", \\\"hypothesis\\\": \\\"D088 方案 B 验证：Learned Uncertainty Head (τ=0.42) + K=1 VLA + Selective CRM correction on LIBERO-Object seed44. 测试 uncertainty-gated CRM 是否能在 K=1 延迟下保持接近 K=10 的 SR。\\\", \\\"plan_id\\\": \\\"d088\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 44 --n_rollouts 10 --K 1 --crm_checkpoint crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"gpu\\\": \\\"cuda:5\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 100, \\\"model_name\\\": \\\"UncertaintyHead+CRM_obs_only\\\", \\\"seed\\\": 44, \\\"checkpoint_source\\\": \\\"uncertainty_head_v1/uncertainty_head_best.pt\\\", \\\"pid\\\": 728278, \\\"log_path\\\": \\\"logs/eval-adaptive-unc-head-object-seed44.log\\\"}}, \\\"openvla-precompute-k1\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T13:49:30.105Z\\\", \\\"updated_at\\\": \\\"2026-05-20T13:51:42.391Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python precompute_openvla.py --device cuda:0 --max_demos_per_task 50 --cache_dir /root/autodl-tmp/crm_cache_k1_openvla/\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"pid\\\": \\\"365142\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/openvla-precompute-k1.log\\\", \\\"submitted_at\\\": \\\"2026-05-20T13:49:29.016Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/libero_data/libero_object/\\\", \\\"data_count\\\": 74507, \\\"model_name\\\": \\\"openvla-libero-object\\\", \\\"seed\\\": 42}, \\\"hypothesis\\\": \\\"Precomputing OpenVLA hidden features at quartile layers [7,15,23,31] will produce multi-scale representations (4×4096) compatible with the CRM K=1 training pipeline, enabling backbone-agnostic conformal refinement.\\\"}}, \\\"count\\\": 17, \\\"total\\\": 17, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.4604}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval-obs-only-object-norm02-seed51\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:31:57.442Z\", \"updated_at\": \"2026-05-20T17:34:30.397Z\", \"hypothesis\": \"CRM obs_only (ε=0.2) K=10 on LIBERO-Object seed51. Expanding Object CRM seed coverage.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 51 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_obs_only_object_norm02_seed51.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"CRM_obs_only\", \"seed\": 51, \"checkpoint_source\": \"crm_v3_norm/obs_only/crm_best.pt\", \"backend\": \"tmux\", \"account\": \"root\", \"log_path\": \"logs/eval-obs-only-object-norm02-seed51.log\"}}, \"eval-vla-only-object-seed49\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-19T21:15:12.591Z\", \"updated_at\": \"2026-05-20T17:34:26.374Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Object seed49. Expanding VLA-only baseline seed coverage for Object benchmark.\", \"completed_at\": \"2026-05-19T22:08:11.590Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"killed\"}}, \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark object --seed 49 --n_rollouts 10 --K 1 --output_file logs/eval_vla_only_object_seed49.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA\", \"seed\": 49, \"checkpoint_source\": \"N/A\", \"backend\": \"tmux\", \"account\": \"root\", \"log_path\": \"logs/eval-vla-only-object-seed49.log\"}}, \"eval-perdof-object-norm02-seed50\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:31:51.325Z\", \"updated_at\": \"2026-05-20T17:34:20.913Z\", \"hypothesis\": \"perdof CRM (ε=0.2) K=10 on LIBERO-Object seed50. Additional perdof seed for multi-seed robustness.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_perdof --benchmark object --seed 50 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_perdof_object_norm02_seed50.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"CRM_perdof\", \"seed\": 50, \"checkpoint_source\": \"crm_v3_norm/perdof/crm_best.pt\", \"backend\": \"tmux\", \"account\": \"root\", \"log_path\": \"logs/eval-perdof-object-norm02-seed50.log\"}}, \"eval-obs-only-spatial-norm02-seed50\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:31:49.315Z\", \"updated_at\": \"2026-05-20T17:34:16.277Z\", \"hypothesis\": \"CRM obs_only (ε=0.2) K=10 on LIBERO-Spatial seed50. Additional spatial seed for multi-seed robustness.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --seed 50 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_obs_only_spatial_norm02_seed50.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"CRM_obs_only\", \"seed\": 50, \"checkpoint_source\": \"crm_v3_norm/obs_only/crm_best.pt\", \"backend\": \"tmux\", \"account\": \"root\", \"log_path\": \"logs/eval-obs-only-spatial-norm02-seed50.log\"}}, \"eval-random-selection-spatial-seed42-r3\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:30:38.520Z\", \"updated_at\": \"2026-05-20T17:31:53.363Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode random_selection --benchmark spatial --seed 42 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_random_selection_spatial_seed42_r3.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"SmolVLA_random_selection\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\"}, \"hypothesis\": \"Random selection baseline (K=10 uniform random) on LIBERO-Spatial seed42. Third attempt after prior kills.\"}, \"eval-obs-only-object-norm003-seed44\": {\"status\": \"RUNNING\", \"retry_count\": 2, \"created_at\": \"2026-05-18T15:15:11.377Z\", \"updated_at\": \"2026-05-20T17:31:34.166Z\", \"hypothesis\": \"CRM obs_only ε=0.03 on Object seed44. Low-norm multi-seed supplement (plan_500): strengthens Figure 2 error bars at small ε.\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-32546\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-18T15:16:33.436Z\", \"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_obs_only_norm003_seed44.json\", \"finished_at\": \"2026-05-20T10:49:41.211Z\", \"training_hours\": 43.55}, \"failure_reason\": \"\", \"completed_at\": \"2026-05-18T21:18:43.893Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T21:18:53.264334+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T10:50:07.963621+00:00\"}], \"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 15, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 30, \"bbq_sauce\": 20, \"ketchup\": 0, \"tomato_sauce\": 10, \"butter\": 10, \"milk\": 20, \"chocolate_pudding\": 30, \"orange_juice\": 30}}, \"notes\": \"失败原因: timeout (EXIT_CODE=124), 与 seed45 相同模式——运行 ~6h 后超时。需增大 timeout_hours 后重提交。\"}}, \"notes\": \"失败原因: timeout (EXIT_CODE=124), 与 seed45 相同模式——运行 ~6h 后超时。需增大 timeout_hours 后重提交。\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 44 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_obs_only_object_norm003_seed44.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only_norm003\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}}, \"eval-obs-only-object-norm005-seed44\": {\"status\": \"RUNNING\", \"retry_count\": 2, \"created_at\": \"2026-05-17T23:10:56.103Z\", \"updated_at\": \"2026-05-20T17:31:26.448Z\", \"hypothesis\": \"CRM obs_only ε=0.05 on Object seed44. Low-norm multi-seed supplement (plan_500): strengthens Figure 2 error bars at small ε.\", \"reproduce\": {\"finished_at\": \"2026-05-20T10:34:28.733Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T13:04:15.652922+00:00\"}], \"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 12, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0, \"bbq_sauce\": 30, \"ketchup\": 0, \"tomato_sauce\": 10, \"butter\": 10, \"milk\": 20, \"chocolate_pudding\": 20, \"orange_juice\": 30}}}}, \"completed_at\": \"2026-05-18T13:07:06.200Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 44 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_obs_only_object_norm005_seed44.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only_norm005\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}}, \"eval-k20-obs-only-object-seed44\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:19:11.419Z\", \"updated_at\": \"2026-05-20T17:20:44.391Z\", \"hypothesis\": \"K=20 CRM obs_only (ε=0.2) on LIBERO-Object seed44. K sweep for plan_601.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 44 --n_rollouts 10 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k20_obs_only_object_seed44.json\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:5\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"crm_obs_only\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}}, \"eval-k5-obs-only-object-seed44\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:19:08.706Z\", \"updated_at\": \"2026-05-20T17:20:34.181Z\", \"hypothesis\": \"K=5 CRM obs_only (ε=0.2) on LIBERO-Object seed44. K sweep for plan_601.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 44 --n_rollouts 10 --K 5 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k5_obs_only_object_seed44.json\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:2\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"crm_obs_only\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}}, \"eval-adaptive-unc-head-object-seed43\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:19:04.464Z\", \"updated_at\": \"2026-05-20T17:20:18.271Z\", \"hypothesis\": \"D088 方案 B 验证：Learned Uncertainty Head (τ=0.42) + K=1 VLA + Selective CRM correction on LIBERO-Object seed43. 测试 uncertainty-gated CRM 是否能在 K=1 延迟下保持接近 K=10 的 SR。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 43 --n_rollouts 10 --K 1 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2 --output_file logs/eval_adaptive_unc_head_object_seed43.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"UncHead_tau0.42_K1_CRM\", \"checkpoint_source\": \"crm_v3_norm/obs_only/crm_best.pt + uncertainty_head_v1/uncertainty_head_best.pt\", \"seed\": 43, \"backend\": \"tmux\", \"account\": \"root\", \"log_path\": \"logs/eval-adaptive-unc-head-object-seed43.log\"}}, \"eval-adaptive-unc-head-object-seed42\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:18:59.700Z\", \"updated_at\": \"2026-05-20T17:20:06.873Z\", \"hypothesis\": \"D088 方案 B 验证：Learned Uncertainty Head (τ=0.42) + K=1 VLA + Selective CRM correction on LIBERO-Object seed42. 测试 uncertainty-gated CRM 是否能在 K=1 延迟下保持接近 K=10 的 SR。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 42 --n_rollouts 10 --K 1 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2 --output_file logs/eval_adaptive_unc_head_object_seed42.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"UncHead_tau0.42_K1_CRM\", \"checkpoint_source\": \"crm_v3_norm/obs_only/crm_best.pt + uncertainty_head_v1/uncertainty_head_best.pt\", \"seed\": 42, \"backend\": \"tmux\", \"account\": \"root\", \"log_path\": \"logs/eval-adaptive-unc-head-object-seed42.log\"}}, \"eval-obs-only-object-norm003-seed43\": {\"status\": \"RUNNING\", \"retry_count\": 2, \"created_at\": \"2026-05-17T13:33:23.925Z\", \"updated_at\": \"2026-05-20T17:19:21.817Z\", \"hypothesis\": \"CRM obs_only ε=0.03 on Object seed43. Low-norm supplement for plan_500 magnitude curve.\", \"notes\": \"PID 621127 on bjb1-18228 cuda:1 died. Process not found, GPU idle. Ghost experiment discovered during registration attempt.\", \"completed_at\": \"2026-05-17T13:33:52.018Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"PID 621127 on bjb1-18228 cuda:1 died. Process not found, GPU idle. Ghost experiment discovered during registration attempt.\"}, \"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T20:40:06.367656+00:00\"}]}, \"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-18T14:37:56.416Z\", \"command\": \"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_obs_only_norm003_seed43.json\", \"finished_at\": \"2026-05-18T20:39:52.321Z\", \"training_hours\": 6.03}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 43 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_obs_only_object_norm003_seed43.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"CRM_obs_only\", \"checkpoint_source\": \"crm_v3_norm/obs_only/crm_best.pt\", \"seed\": 43, \"backend\": \"tmux\", \"account\": \"root\", \"log_path\": \"logs/eval-obs-only-object-norm003-seed43.log\"}}, \"D088-eval-adaptive-unc-head-object-seed44\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:00:46.028Z\", \"updated_at\": \"2026-05-20T17:02:30.624Z\", \"hypothesis\": \"D088 方案 B: Learned Uncertainty Head (τ=0.42) + K=1 VLA + Selective CRM on LIBERO-Object seed44. n_rollouts=100 for statistical significance. 测试 uncertainty-gated selective CRM 在固定延迟(K=1)下能否保持接近 K=10 CRM 的 SR。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 44 --n_rollouts 100 --K 1 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2 --output_file logs/eval_adaptive_unc_head_object_seed44.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"data_path\": \"LIBERO-Object\", \"data_count\": 1000, \"model_name\": \"UncertaintyHead+CRM_obs_only\", \"checkpoint_source\": \"uncertainty_head_v1/uncertainty_head_best.pt\", \"seed\": 44, \"backend\": \"tmux\", \"account\": \"root\", \"log_path\": \"logs/eval-adaptive-unc-head-object-seed44.log\"}}, \"D088-eval-adaptive-unc-head-object-seed43\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:00:42.469Z\", \"updated_at\": \"2026-05-20T17:02:26.585Z\", \"hypothesis\": \"D088 方案 B: Learned Uncertainty Head (τ=0.42) + K=1 VLA + Selective CRM on LIBERO-Object seed43. n_rollouts=100 for statistical significance. 测试 uncertainty-gated selective CRM 在固定延迟(K=1)下能否保持接近 K=10 CRM 的 SR。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 43 --n_rollouts 100 --K 1 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2 --output_file logs/eval_adaptive_unc_head_object_seed43.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"data_path\": \"LIBERO-Object\", \"data_count\": 1000, \"model_name\": \"UncertaintyHead+CRM_obs_only\", \"checkpoint_source\": \"uncertainty_head_v1/uncertainty_head_best.pt\", \"seed\": 43, \"backend\": \"tmux\", \"account\": \"root\", \"log_path\": \"logs/eval-adaptive-unc-head-object-seed43.log\"}}, \"D088-eval-adaptive-unc-head-object-seed42\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:00:39.505Z\", \"updated_at\": \"2026-05-20T17:02:22.505Z\", \"hypothesis\": \"D088 方案 B: Learned Uncertainty Head (τ=0.42) + K=1 VLA + Selective CRM on LIBERO-Object seed42. n_rollouts=100 for statistical significance. 测试 uncertainty-gated selective CRM 在固定延迟(K=1)下能否保持接近 K=10 CRM 的 SR。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 42 --n_rollouts 100 --K 1 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint /root/autodl-tmp/checkpoints/uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2 --output_file logs/eval_adaptive_unc_head_object_seed42.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"data_path\": \"LIBERO-Object\", \"data_count\": 1000, \"model_name\": \"UncertaintyHead+CRM_obs_only\", \"checkpoint_source\": \"uncertainty_head_v1/uncertainty_head_best.pt\", \"seed\": 42, \"backend\": \"tmux\", \"account\": \"root\", \"log_path\": \"logs/eval-adaptive-unc-head-object-seed42.log\"}}, \"eval-adaptive-unc-head-object-seed44\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T16:52:03.117Z\", \"updated_at\": \"2026-05-20T17:00:27.101Z\", \"hypothesis\": \"D088 方案 B 验证：Learned Uncertainty Head (τ=0.42) + K=1 VLA + Selective CRM correction on LIBERO-Object seed44. 测试 uncertainty-gated CRM 是否能在 K=1 延迟下保持接近 K=10 的 SR。\", \"plan_id\": \"d088\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_unc_head --benchmark object --seed 44 --n_rollouts 10 --K 1 --crm_checkpoint crm_v3_norm/obs_only/crm_best.pt --unc_head_checkpoint uncertainty_head_v1/uncertainty_head_best.pt --unc_threshold 0.42 --max_correction_norm 0.2\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:5\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"UncertaintyHead+CRM_obs_only\", \"seed\": 44, \"checkpoint_source\": \"uncertainty_head_v1/uncertainty_head_best.pt\", \"pid\": 728278, \"log_path\": \"logs/eval-adaptive-unc-head-object-seed44.log\"}}, \"openvla-precompute-k1\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T13:49:30.105Z\", \"updated_at\": \"2026-05-20T13:51:42.391Z\", \"spec\": {\"command\": \"python precompute_openvla.py --device cuda:0 --max_demos_per_task 50 --cache_dir /root/autodl-tmp/crm_cache_k1_openvla/\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"365142\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/openvla-precompute-k1.log\", \"submitted_at\": \"2026-05-20T13:49:29.016Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_object/\", \"data_count\": 74507, \"model_name\": \"openvla-libero-object\", \"seed\": 42}, \"hypothesis\": \"Precomputing OpenVLA hidden features at quartile layers [7,15,23,31] will produce multi-scale representations (4×4096) compatible with the CRM K=1 training pipeline, enabling backbone-agnostic conformal refinement.\"}}, \"count\": 17, \"total\": 17, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.4604}}"
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
The experiment `eval-random-selection-object-seed46-r3` is not in the registry. Let me search more broadly for it - maybe the exp_id is slightly different or it has a different status.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c5300403-6659-4470-875e-d77ab58a370d",
  "uuid": "37106941-ef55-4757-98c1-728fbf5bedf2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M8Y73vXXaofJV9Sxp863kb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8572,
      "cache_read_input_tokens": 25255,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8572
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

Registry 里没有这个实验。让我搜索更广泛的范围。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c5300403-6659-4470-875e-d77ab58a370d",
  "uuid": "556aacb8-13c6-4d2d-8859-90a4789d0f55",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M8Y73vXXaofJV9Sxp863kb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8572,
      "cache_read_input_tokens": 25255,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8572
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01S9XRy1bZh7Xhw4BzEEUury`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "fields": [
    "*"
  ],
  "filters": {
    "status": "DONE"
  },
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
  "session_id": "c5300403-6659-4470-875e-d77ab58a370d",
  "uuid": "da7c7d31-833a-4464-bdbc-e71b38b99926",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M8Y73vXXaofJV9Sxp863kb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8572,
      "cache_read_input_tokens": 25255,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8572
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

_source line 16 · 2026-05-20T17:51:45.119Z_

<details><summary>↩ Tool result · `toolu_01S9XRy1bZh7Xhw4BzEEUury`</summary>

```text
Error: result (79,192 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/c5300403-6659-4470-875e-d77ab58a370d/tool-results/mcp-agent-ml-research-read_registry-1779299505096.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/c5300403-6659-4470-875e-d77ab58a370d/tool-results/mcp-agent-ml-research-read_registry-1779299505096.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/c5300403-6659-4470-875e-d77ab58a370d/tool-results/mcp-agent-ml-research-read_registry-1779299505096.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c5300403-6659-4470-875e-d77ab58a370d",
  "uuid": "f89c5bcc-0fd9-4322-91b1-57bcc28cf482",
  "tool_use_result": {
    "content": "Error: result (79,192 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/c5300403-6659-4470-875e-d77ab58a370d/tool-results/mcp-agent-ml-research-read_registry-1779299505096.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/c5300403-6659-4470-875e-d77ab58a370d/tool-results/mcp-agent-ml-research-read_registry-1779299505096.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/c5300403-6659-4470-875e-d77ab58a370d/tool-results/mcp-agent-ml-research-read_registry-1779299505096.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval-random-selection-object-seed46-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T15:36:03.819Z\", \"updated_at\": \"2026-05-20T17:36:15.098Z\", \"hypothesis\": \"Random selection baseline on LIBERO-Object seed46 (plan_600). Third attempt on bjb1-18228 with updated code.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode random_selection --benchmark object --seed 46 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_random_selection_object_seed46.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"421636\", \"log_path\": \"logs/eval-random-selection-object-seed46.log\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA_random_selection\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.1, \"tasks_evaluated\": 10, \"rollouts_per_task\": 10, \"total_rollouts\": 100, \"total_successes\": 10}, \"completed_at\": \"2026-05-20T17:36:15.098Z\"}, \"eval-perdof-object-norm02-seed49\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T13:56:54.460Z\", \"updated_at\": \"2026-05-20T17:31:38.771Z\", \"hypothesis\": \"perdof CRM (ε=0.2) K=10 on LIBERO-Object seed49. Testing per-DOF correction architecture for multi-seed robustness.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_perdof --benchmark object --seed 49 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_perdof_object_norm02_seed49.json 2>&1 | tee logs/eval-perdof-object-norm02-seed49.log\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"450375\", \"log_path\": \"N/A\", \"submitted_at\": \"2026-05-20T13:57:02.316Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A\", \"wall_clock_seconds\": 5649.1, \"gpu_hours\": 1.57}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T15:31:11.418Z\", \"reproduce\": {\"finished_at\": \"2026-05-20T15:56:19.146Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T15:56:30.647763+00:00\"}]}, \"metrics\": {\"overall_success_rate\": 0.12, \"benchmark\": \"object\", \"mode\": \"crm_perdof\", \"seed\": 49, \"K\": 10, \"max_correction_norm\": 0.2}}, \"eval-random-selection-object-seed47\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T15:34:01.591Z\", \"updated_at\": \"2026-05-20T17:30:04.397Z\", \"hypothesis\": \"Random selection baseline on LIBERO-Object seed47 (plan_600). Additional seed for random baseline multi-seed robustness.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode random_selection --benchmark object --seed 47 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_random_selection_object_seed47.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"421965\", \"log_path\": \"logs/eval_random_selection_object_seed47.json\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA_random_selection\", \"seed\": 47, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"status\": \"DONE\", \"metrics\": {\"sr\": 0.07}, \"checkpoint_path\": \"N/A\"}, \"conclusion\": \"success\", \"metrics\": {\"sr\": 7}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-random-selection-object-seed47.log\", \"checkpoint_path\": \"N/A\", \"completed_at\": \"2026-05-20T17:26:46.248Z\"}, \"eval-k20-obs-only-object-seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T15:33:50.688Z\", \"updated_at\": \"2026-05-20T17:30:00.341Z\", \"hypothesis\": \"K=20 sweep for obs_only CRM on LIBERO-Object seed42 (plan_601). Testing whether doubling K from 10 to 20 further improves correction quality.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 42 --n_rollouts 10 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k20_obs_only_object_seed42.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"421434\", \"log_path\": \"logs/eval_k20_obs_only_object_seed42.json\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only_K20\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"status\": \"DONE\", \"metrics\": {\"sr\": 0.2}, \"checkpoint_path\": \"N/A\"}, \"conclusion\": \"success\", \"metrics\": {\"sr\": 20}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-k20-obs-only-object-seed42.log\", \"checkpoint_path\": \"N/A\", \"completed_at\": \"2026-05-20T17:24:50.263Z\"}, \"eval-obs-only-spatial-norm02-seed42-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T15:31:34.419Z\", \"updated_at\": \"2026-05-20T17:28:06.990Z\", \"hypothesis\": \"CRM obs_only K=10 norm02 on LIBERO-Spatial seed42, retry 2. Prior run killed mid-evaluation. Re-run to fill missing seed42 Spatial CRM data point.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --seed 42 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_obs_only_spatial_norm02_seed42_r2.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"crm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 10 rollouts\", \"gpu\": [\"cuda:2\"], \"pid\": \"433142\", \"log_path\": \"logs/eval-obs-only-spatial-norm02-seed42-r2.log\", \"backend\": \"tmux\"}, \"conclusion\": \"success\", \"metrics\": {\"sr\": 33}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-obs-only-spatial-norm02-seed42-r2.log\", \"checkpoint_path\": \"N/A\", \"completed_at\": \"2026-05-20T17:28:06.990Z\"}, \"eval-obs-only-object-norm005-seed43\": {\"status\": \"DONE\", \"retry_count\": 2, \"created_at\": \"2026-05-17T13:32:15.980Z\", \"updated_at\": \"2026-05-20T17:24:01.628Z\", \"hypothesis\": \"CRM obs_only ε=0.05 on Object seed43. Low-norm multi-seed supplement (plan_500): strengthens Figure 2 error bars at small ε.\", \"notes\": \"Superseded by eval-obs-only-object-norm005-seed43-r2 (bjb1-32546) and r3 (bjb1-18228)\", \"completed_at\": \"2026-05-17T23:17:56.045Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"sr\": 0.13, \"total\": 100, \"successes\": 13, \"benchmark\": \"object\", \"mode\": \"crm_obs_only\"}, \"notes\": \"Superseded by eval-obs-only-object-norm005-seed43-r2 (bjb1-32546) and r3 (bjb1-18228)\"}, \"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T10:54:29.620606+00:00\"}]}, \"reproduce\": {\"finished_at\": \"2026-05-20T10:54:17.445Z\"}, \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 43 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_obs_only_object_norm005_seed43.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"484651\", \"log_path\": \"logs/eval-obs-only-object-norm005-seed43.log\", \"submitted_at\": \"2026-05-20T15:32:00Z\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA + CRM obs_only (K=10, ε=0.05)\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"wall_clock_seconds\": 6721.6, \"gpu_hours\": 1.87}, \"conclusion\": \"success\", \"metrics\": {\"sr\": 13, \"total\": 100, \"successes\": 13, \"benchmark\": \"object\", \"mode\": \"crm_obs_only\"}, \"log_path\": \"logs/eval-obs-only-object-norm005-seed43.log\", \"checkpoint_path\": \"N/A\"}, \"eval-k20-obs-only-object-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T15:31:55.966Z\", \"updated_at\": \"2026-05-20T17:23:26.043Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 43 --n_rollouts 10 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k20_obs_only_object_seed43.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"484257\", \"log_path\": \"logs/eval-k20-obs-only-object-seed43.log\", \"submitted_at\": \"2026-05-20T15:32:00Z\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA + CRM obs_only (K=20, norm02)\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"wall_clock_seconds\": 6686.0, \"gpu_hours\": 1.86}, \"hypothesis\": \"K=20 CRM obs_only (ε=0.2) on LIBERO-Object seed43. K sweep for plan_601: tests whether more candidates improve CRM selection quality.\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 18}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-k20-obs-only-object-seed43.log\", \"checkpoint_path\": \"N/A\", \"completed_at\": \"2026-05-20T17:23:26.043Z\"}, \"eval-k5-obs-only-object-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T15:31:47.920Z\", \"updated_at\": \"2026-05-20T17:22:56.685Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 43 --n_rollouts 10 --K 5 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_k5_obs_only_object_seed43.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"483989\", \"log_path\": \"logs/eval-k5-obs-only-object-seed43.log\", \"submitted_at\": \"2026-05-20T15:32:00Z\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA + CRM obs_only (K=5, norm02)\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"wall_clock_seconds\": 6656.7, \"gpu_hours\": 1.85}, \"hypothesis\": \"K=5 CRM obs_only (ε=0.2) on LIBERO-Object seed43. K sweep for plan_601: tests whether fewer candidates degrade performance.\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 17}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k5_obs_only_object_seed43.json\", \"checkpoint_path\": \"N/A\", \"completed_at\": \"2026-05-20T17:22:56.685Z\"}, \"eval-random-selection-spatial-seed43-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T15:35:38.150Z\", \"updated_at\": \"2026-05-20T17:21:49.990Z\", \"hypothesis\": \"Random selection baseline on LIBERO-Spatial seed43 re-run (plan_600). Fresh run on bjb1-18228 for additional baseline data point.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode random_selection --benchmark spatial --seed 43 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_random_selection_spatial_seed43.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"422233\", \"log_path\": \"logs/eval-random-selection-spatial-seed43.log\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"SmolVLA_random_selection\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\"}, \"conclusion\": \"success\", \"metrics\": {\"sr\": 26}, \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-random-selection-spatial-seed43.log\", \"completed_at\": \"2026-05-20T17:21:49.990Z\"}, \"eval-random-selection-spatial-seed44\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-20T10:47:57.755Z\", \"updated_at\": \"2026-05-20T17:20:57.101Z\", \"hypothesis\": \"Random selection baseline (K=10, uniform random) on LIBERO-Spatial seed44. Tests whether random action selection ≈ VLA-only, confirming CRM guidance is the source of improvement.\", \"reproduce\": {\"finished_at\": \"2026-05-20T17:17:11.445Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T12:32:59.353731+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T17:17:27.457810+00:00\"}], \"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.28, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"K\": 10, \"mode\": \"random_selection\", \"benchmark\": \"spatial\", \"seed\": 44, \"per_task_sr\": {\"between_plate_and_ramekin\": 0.7, \"next_to_ramekin\": 0.9, \"from_table_center\": 0, \"on_cookie_box\": 0.1, \"in_top_drawer\": 0, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.2, \"on_wooden_cabinet\": 0}}}}, \"completed_at\": \"2026-05-20T12:38:03.891Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode random_selection --benchmark spatial --seed 44 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_random_selection_spatial_seed44.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"483789\", \"log_path\": \"logs/eval-random-selection-spatial-seed44.log\", \"submitted_at\": \"2026-05-20T15:32:00Z\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"random_selection\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\", \"wall_clock_seconds\": 6317.2, \"gpu_hours\": 1.75}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.28, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-random-selection-spatial-seed44.log\"}, \"eval-crm-k1-object-seed43-plan702\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"failure_reason\": \"\", \"retry_count\": 0, \"created_at\": \"2026-05-20T13:50:02.848Z\", \"updated_at\": \"2026-05-20T16:58:33.591Z\", \"hypothesis\": \"K=1 CRM (ACCG) on LIBERO-Object seed43 for plan_702. Third attempt (M032).\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_k1_accg --benchmark object --n_rollouts 10 --seed 43 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt --max_correction_norm 0.2 --output_file logs/eval_crm_k1_object_seed43_plan702.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"pid\": \"401666\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-crm-k1-object-seed43-plan702.log\", \"submitted_at\": \"2026-05-20T13:50:35.103Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 10, \"model_name\": \"crm_k1_accg\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt\", \"eval_data\": \"LIBERO-Object\", \"wall_clock_seconds\": 11278.5, \"gpu_hours\": 3.13}, \"reproduce\": {\"finished_at\": \"2026-05-20T16:49:51.547Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T14:29:03.076074+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T16:50:06.514400+00:00\"}]}, \"metrics\": {\"sr\": 11, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"checkpoint_path\": \"N/A\", \"completed_at\": \"2026-05-20T16:58:33.591Z\"}, \"eval-crm-k1-object-seed42-plan702\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"failure_reason\": \"\", \"retry_count\": 0, \"created_at\": \"2026-05-20T13:50:00.848Z\", \"updated_at\": \"2026-05-20T16:58:27.648Z\", \"hypothesis\": \"K=1 CRM (ACCG) on LIBERO-Object seed42 for plan_702. Third attempt after unc_dim bugfix + exit file cleanup (M032).\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_k1_accg --benchmark object --n_rollouts 10 --seed 42 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt --max_correction_norm 0.2 --output_file logs/eval_crm_k1_object_seed42_plan702.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"pid\": \"401372\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-crm-k1-object-seed42-plan702.log\", \"submitted_at\": \"2026-05-20T13:50:31.521Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 10, \"model_name\": \"crm_k1_accg\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt\", \"eval_data\": \"LIBERO-Object\", \"wall_clock_seconds\": 11276.1, \"gpu_hours\": 3.13}, \"reproduce\": {\"finished_at\": \"2026-05-20T16:45:31.358Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T14:28:39.897810+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T16:45:42.081498+00:00\"}]}, \"metrics\": {\"sr\": 11, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"checkpoint_path\": \"N/A\", \"completed_at\": \"2026-05-20T16:58:27.648Z\"}, \"eval-crm-k1-object-seed44-plan702\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"failure_reason\": \"\", \"retry_count\": 0, \"created_at\": \"2026-05-20T13:50:04.763Z\", \"updated_at\": \"2026-05-20T16:50:59.250Z\", \"hypothesis\": \"K=1 CRM (ACCG) on LIBERO-Object seed44 for plan_702. Third attempt (M032).\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_k1_accg --benchmark object --n_rollouts 10 --seed 44 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt --max_correction_norm 0.2 --output_file logs/eval_crm_k1_object_seed44_plan702.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:5\"], \"pid\": \"402276\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-crm-k1-object-seed44-plan702.log\", \"submitted_at\": \"2026-05-20T13:50:39.297Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 10, \"model_name\": \"crm_k1_accg\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt\", \"eval_data\": \"LIBERO-Object\", \"wall_clock_seconds\": 10820.0, \"gpu_hours\": 3.01}, \"reproduce\": {\"finished_at\": \"2026-05-20T16:46:34.869Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T14:29:37.626962+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T16:46:44.986038+00:00\"}]}, \"metrics\": {\"sr\": 10, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"checkpoint_path\": \"N/A\", \"completed_at\": \"2026-05-20T16:50:59.250Z\"}, \"eval-random-selection-object-seed46-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T01:42:56.456Z\", \"updated_at\": \"2026-05-20T15:35:34.584Z\", \"hypothesis\": \"Random selection baseline on LIBERO-Object seed46 (plan_600). Retry after code fix - additional seed for random baseline comparison.\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && timeout 57600 /root/miniconda3/bin/python -u src/evaluate.py --mode random_selection --benchmark object --n_rollouts 10 --seed 46 --K 10 --output_file logs/eval_object_random_selection_seed46.json\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"tmux_session\": \"eval-random-selection-seed46-t16\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA_random_selection\", \"seed\": 46, \"eval_data\": \"LIBERO-Object\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T17:47:06.031Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-19T17:47:10.111Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T17:47:19.928543+00:00\"}]}}, \"eval-random-selection-spatial-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:47:52.915Z\", \"updated_at\": \"2026-05-20T15:34:05.777Z\", \"hypothesis\": \"Random selection baseline on LIBERO-Spatial seed43 (plan_600). Additional spatial seed for random baseline to compare against CRM selection on ID suite.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode random_selection --benchmark spatial --seed 43 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_random_selection_spatial_seed43.json 2>&1 | tee logs/eval-random-selection-spatial-seed43.log\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"347065\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-random-selection-spatial-seed43.log\", \"submitted_at\": \"2026-05-20T10:51:12.210Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": \"100 (10 tasks x 10 rollouts)\", \"model_name\": \"SmolVLA + CRM random_selection (K=10)\", \"seed\": 43, \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 8098.7, \"gpu_hours\": 2.25}, \"reproduce\": {\"finished_at\": \"2026-05-20T12:35:51.194Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T12:36:02.468424+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.26, \"per_task_sr\": {\"between_plate_ramekin\": 0.7, \"next_to_ramekin\": 0.9, \"table_center\": 0, \"cookie_box\": 0.1, \"top_drawer\": 0, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.7, \"stove\": 0, \"next_to_plate\": 0.2, \"wooden_cabinet\": 0}}, \"completed_at\": \"2026-05-20T13:06:10.939Z\"}, \"eval-random-selection-object-seed46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:50:36.635Z\", \"updated_at\": \"2026-05-20T15:33:54.594Z\", \"hypothesis\": \"Random selection baseline on LIBERO-Object seed46 (plan_600). Additional seed for random baseline to establish statistical comparison against CRM selection.\", \"conclusion\": \"failed\", \"failure_reason\": \"random_selection mode not supported on bjb1-18228\", \"completed_at\": \"2026-05-18T16:53:31.340Z\"}, \"eval-obs-only-spatial-seed48\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T15:32:05.973Z\", \"updated_at\": \"2026-05-20T15:33:15.181Z\", \"hypothesis\": \"CRM obs_only K=10 on LIBERO-Spatial seed48. Additional seed for Spatial CRM multi-seed robustness.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --seed 48 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_obs_only_spatial_norm02_seed48.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 48, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"logs/eval_obs_only_spatial_norm02_seed48.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T15:33:00.525Z\", \"metrics\": {\"overall_success_rate\": 0.35, \"benchmark\": \"spatial\", \"n_rollouts\": 10}}, \"eval-vla-only-spatial-seed48\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-19T20:32:48.207Z\", \"updated_at\": \"2026-05-20T15:32:12.693Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Spatial seed48. Additional seed for VLA-only multi-seed baseline comparison.\", \"reproduce\": {\"finished_at\": \"2026-05-20T12:14:19.735Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-19T20:58:30.818Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T20:59:16.811621+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T12:14:36.542832+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark spatial --seed 48 --n_rollouts 10 --K 1 --output_file logs/eval_vla_only_spatial_seed48.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"385639\", \"log_path\": \"logs/eval_vla_only_spatial_seed48.json\", \"submitted_at\": \"2026-05-20T13:07:19.572Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"SmolVLA\", \"seed\": 48, \"checkpoint_source\": \"/root/autodl-tmp/models/smolvla_libero\", \"eval_data\": \"LIBERO-Spatial\", \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 8649.3, \"gpu_hours\": 2.4}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.3, \"benchmark\": \"spatial\", \"n_rollouts\": 10}}, \"eval-obs-only-spatial-norm02-seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:49:20.087Z\", \"updated_at\": \"2026-05-20T15:19:37.689Z\", \"hypothesis\": \"CRM obs_only K=10 norm02 on LIBERO-Spatial seed42. Filling missing seed42 for Spatial CRM to balance seed coverage across configs.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 ... python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --seed 42 --n_rollouts 10 --K 10 --crm_checkpoint .../crm_best.pt --max_correction_norm 0.2\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"340026\", \"log_path\": \"logs/eval-obs-only-spatial-norm02-seed42.log\", \"submitted_at\": \"2026-05-20T10:52:21.255Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": \"100 (10 tasks x 10 rollouts)\", \"model_name\": \"SmolVLA + CRM obs_only (K=10, norm02)\", \"seed\": 42, \"wall_clock_seconds\": 16036.4, \"gpu_hours\": 4.45}, \"reproduce\": {\"finished_at\": \"2026-05-20T12:13:36.856Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T12:13:46.992861+00:00\"}]}, \"metrics\": {\"status_note\": \"INCOMPLETE - only 2/10 tasks evaluated before process terminated\", \"partial_per_task\": {\"between_plate_ramekin\": 0.9, \"next_to_ramekin\": 1}, \"tasks_completed\": 2, \"tasks_total\": 10}, \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-obs-only-spatial-norm02-seed42.log\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-20T15:19:37.689Z\"}, \"eval-obs-only-spatial-norm02-seed49\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T13:27:10.816Z\", \"updated_at\": \"2026-05-20T15:19:01.383Z\", \"hypothesis\": \"obs_only CRM (ε=0.2) K=10 on LIBERO-Spatial seed49. Additional Spatial CRM seed for multi-seed robustness.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --seed 49 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_obs_only_spatial_norm02_seed49.json 2>&1 | tee logs/eval-obs-only-spatial-norm02-seed49.log\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"357291\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-spatial-norm02-seed49.log\", \"submitted_at\": \"2026-05-20T13:27:27.565Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 6693.8, \"gpu_hours\": 1.86}, \"reproduce\": {\"finished_at\": \"2026-05-20T15:14:56.226Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T15:15:11.314921+00:00\"}]}, \"metrics\": {\"sr\": 0.32, \"sr_pct\": \"32%\", \"total_rollouts\": 100, \"n_tasks\": 10, \"n_rollouts_per_task\": 10, \"per_task\": {\"between_plate_ramekin\": 0.9, \"next_to_ramekin\": 0.9, \"table_center\": 0, \"on_cookie_box\": 0.3, \"top_drawer_cabinet\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.8, \"on_stove\": 0, \"next_to_plate\": 0.2, \"on_wooden_cabinet\": 0}}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_obs_only_spatial_norm02_seed49.json\", \"completed_at\": \"2026-05-20T15:19:01.383Z\"}, \"eval-adaptive-k-spatial-p90-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T13:06:33.103Z\", \"updated_at\": \"2026-05-20T15:17:24.944Z\", \"hypothesis\": \"Adaptive K with τ=P90 (0.125870) on LIBERO-Spatial seed44. Third seed completing Spatial P90 cross-benchmark sweep.\", \"spec\": {\"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p90-seed44.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-20T14:54:15.429Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T14:55:02.249467+00:00\"}]}, \"metrics\": {\"success_rate\": 0.36, \"avg_K\": 3.56, \"fast_path_ratio\": 0.805, \"adaptive_trigger_rate\": 0.195, \"total_rollouts\": 100, \"successes\": 36, \"total_steps\": 23123, \"fast_steps\": 18615, \"full_steps\": 4508, \"threshold\": 0.12587, \"mean_l2_distance\": 0.09, \"per_task\": {\"between_plate_and_ramekin\": {\"sr\": 0.8, \"successes\": 8, \"total\": 10}, \"next_to_ramekin\": {\"sr\": 1, \"successes\": 10, \"total\": 10}, \"from_table_center\": {\"sr\": 0, \"successes\": 0, \"total\": 10}, \"on_cookie_box\": {\"sr\": 0.4, \"successes\": 4, \"total\": 10}, \"in_top_drawer\": {\"sr\": 0.1, \"successes\": 1, \"total\": 10}, \"on_ramekin\": {\"sr\": 0, \"successes\": 0, \"total\": 10}, \"next_to_cookie_box\": {\"sr\": 0.9, \"successes\": 9, \"total\": 10}, \"on_stove\": {\"sr\": 0, \"successes\": 0, \"total\": 10}, \"next_to_plate\": {\"sr\": 0.4, \"successes\": 4, \"total\": 10}, \"on_wooden_cabinet\": {\"sr\": 0, \"successes\": 0, \"total\": 10}}}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p90-seed44.log\", \"completed_at\": \"2026-05-20T15:17:24.944Z\"}, \"eval-argmin-object-seed50\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T13:07:43.376Z\", \"updated_at\": \"2026-05-20T15:05:10.161Z\", \"hypothesis\": \"Argmin baseline (reconvla K=10) on LIBERO-Object seed50. Additional seed for balanced Argmin vs CRM comparison.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode reconvla --benchmark object --seed 50 --n_rollouts 10 --K 10 --output_file logs/eval_argmin_object_seed50.json 2>&1 | tee logs/eval-argmin-object-seed50.log\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"423608\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-object-seed50.log\", \"submitted_at\": \"2026-05-20T13:08:24.424Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 7005.7, \"gpu_hours\": 1.95}, \"reproduce\": {\"finished_at\": \"2026-05-20T15:02:39.224Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T15:02:49.829711+00:00\"}]}, \"metrics\": {\"overall_sr\": 0.13, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.2}, \"total_rollouts\": 100, \"total_successes\": 13, \"seed\": 50, \"benchmark\": \"object\", \"K\": 10, \"mode\": \"reconvla\"}, \"checkpoint_path\": \"N/A\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-object-seed50.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T15:05:10.161Z\"}, \"eval-obs-only-object-norm02-seed50\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T13:07:41.505Z\", \"updated_at\": \"2026-05-20T14:59:04.529Z\", \"hypothesis\": \"CRM obs_only (ε=0.2) K=10 on LIBERO-Object seed50. Expanding Object CRM norm02 from n=7 to n=8 for seed balance.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 50 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_obs_only_object_norm02_seed50.json 2>&1 | tee logs/eval-obs-only-object-norm02-seed50.log\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"423273\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-seed50.log\", \"submitted_at\": \"2026-05-20T13:08:20.924Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 6643.6, \"gpu_hours\": 1.85}, \"reproduce\": {\"finished_at\": \"2026-05-20T14:52:49.362Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T14:52:59.438123+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"sr\": 18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"checkpoint_path\": \"N/A\", \"log_path\": \"logs/eval_obs_only_object_norm02_seed50.json\", \"completed_at\": \"2026-05-20T14:59:04.529Z\"}, \"eval-vla-only-object-seed48-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T13:08:11.387Z\", \"updated_at\": \"2026-05-20T14:59:00.735Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Object seed48 re-run. Prior run (sr=0.1) had process death issues. Redeploy for reliable VLA-only baseline data.\", \"spec\": {\"checkpoint_path\": \"\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-object-seed48-r2.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-20T14:53:14.771Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T14:53:44.084405+00:00\"}]}, \"metrics\": {\"success_rate\": 0.11, \"total_rollouts\": 100, \"successes\": 11, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0.1, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.1, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.1, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0.1, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 0.1, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.4, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.2}}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A\", \"log_path\": \"logs/eval_vla_only_object_seed48_r2.json\", \"completed_at\": \"2026-05-20T14:59:00.736Z\"}, \"eval-vla-only-goal-seed51\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T05:16:21.107Z\", \"updated_at\": \"2026-05-20T14:58:56.897Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Goal seed51. Paired baseline for CRM obs_only Goal seed51 (SR=66%) comparison.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode vla_only --benchmark goal --seed 51 --n_rollouts 10 --K 1 --output_file logs/eval_vla_only_goal_seed51.json 2>&1 | tee logs/eval-vla-only-goal-seed51.log\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"444134\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-goal-seed51.log\", \"submitted_at\": \"2026-05-20T13:46:28.291Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 4348.6, \"gpu_hours\": 1.21}, \"reproduce\": {\"finished_at\": \"2026-05-20T14:54:11.966Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T14:54:38.821705+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"sr\": 69, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"checkpoint_path\": \"N/A\", \"log_path\": \"logs/eval_vla_only_goal_seed51.json\", \"completed_at\": \"2026-05-20T14:58:56.897Z\"}, \"eval-random-selection-spatial-seed42-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T13:06:37.026Z\", \"updated_at\": \"2026-05-20T14:48:09.495Z\", \"hypothesis\": \"Random selection baseline (K=10 uniform random) on Spatial seed42. Redeploy after M030 SIGTERM kill. Completes plan_600 Spatial baseline.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode random_selection --benchmark spatial --seed 42 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_random_selection_spatial_seed42_r2.json 2>&1 | tee logs/eval-random-selection-spatial-seed42-r2.log\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"384767\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-random-selection-spatial-seed42-r2.log\", \"submitted_at\": \"2026-05-20T13:07:09.624Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 6059.9, \"gpu_hours\": 1.68}, \"reproduce\": {\"finished_at\": \"2026-05-20T14:44:26.986Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T14:44:37.099741+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"sr\": 34, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"checkpoint_path\": \"N/A\", \"log_path\": \"logs/eval_random_selection_spatial_seed42_r2.json\", \"completed_at\": \"2026-05-20T14:48:09.495Z\"}, \"eval-random-selection-object-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:32:32.629Z\", \"updated_at\": \"2026-05-20T14:37:22.190Z\", \"hypothesis\": \"Random selection baseline (K=10, uniform random pick) on LIBERO-Object seed45. Controls for sampling diversity vs CRM-guided selection. Plan_600.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python -u src/evaluate.py --mode random_selection --benchmark object --n_rollouts 10 --seed 45 --K 10 --output_file logs/eval_object_random_selection_seed45.json\", \"server\": \"bjb2-28827\", \"seed\": 45, \"data_path\": \"LIBERO-Object\", \"data_count\": 10, \"model_name\": \"openvla-7b\", \"checkpoint_path\": \"N/A\", \"log_path\": \"logs/eval_object_random_selection_seed45.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T11:25:05.339Z\", \"metrics\": {\"success_rate\": 0.1, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\"}, \"eval-crm-k1-object-seed44-plan702-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"failure_reason\": \"Killed by M032 strict redeployment - superseded by plan702 third attempt\", \"retry_count\": 0, \"created_at\": \"2026-05-20T14:33:04.339Z\", \"updated_at\": \"2026-05-20T14:34:18.084Z\", \"hypothesis\": \"K=1 CRM (ACCG) on LIBERO-Object seed44 for plan_702. Single VLA forward + CRM correction. Compare to K=1 VLA-only baseline (10.8%). Retry after unc_dim bugfix.\", \"parent\": \"eval-crm-k1-object-seed44-plan702\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_k1_accg --benchmark object --n_rollouts 10 --seed 44 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt --max_correction_norm 0.2\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:5\", \"seed\": 44, \"model_name\": \"MultiScaleCRM+SmolVLA\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt\", \"eval_data\": \"LIBERO-Object\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"log_path\": \"logs/eval-crm-k1-object-seed44-plan702-r2.log\", \"checkpoint_path\": \"N/A\"}}, \"eval-crm-k1-object-seed43-plan702-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"failure_reason\": \"Killed by M032 strict redeployment - superseded by plan702 third attempt\", \"retry_count\": 0, \"created_at\": \"2026-05-20T14:33:01.973Z\", \"updated_at\": \"2026-05-20T14:34:14.100Z\", \"hypothesis\": \"K=1 CRM (ACCG) on LIBERO-Object seed43 for plan_702. Single VLA forward + CRM correction. Compare to K=1 VLA-only baseline (10.8%). Retry after unc_dim bugfix.\", \"parent\": \"eval-crm-k1-object-seed43-plan702\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_k1_accg --benchmark object --n_rollouts 10 --seed 43 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt --max_correction_norm 0.2\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:1\", \"seed\": 43, \"model_name\": \"MultiScaleCRM+SmolVLA\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt\", \"eval_data\": \"LIBERO-Object\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"log_path\": \"logs/eval-crm-k1-object-seed43-plan702-r2.log\", \"checkpoint_path\": \"N/A\"}}, \"eval-crm-k1-object-seed42-plan702-r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"failure_reason\": \"Killed by M032 strict redeployment - superseded by plan702 third attempt\", \"retry_count\": 0, \"created_at\": \"2026-05-20T14:32:58.117Z\", \"updated_at\": \"2026-05-20T14:34:10.003Z\", \"hypothesis\": \"K=1 CRM (ACCG) on LIBERO-Object seed42 for plan_702. Single VLA forward + CRM correction. Compare to K=1 VLA-only baseline (10.8%). Retry after unc_dim bugfix.\", \"parent\": \"eval-crm-k1-object-seed42-plan702\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_k1_accg --benchmark object --n_rollouts 10 --seed 42 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt --max_correction_norm 0.2\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:0\", \"seed\": 42, \"model_name\": \"MultiScaleCRM+SmolVLA\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt\", \"eval_data\": \"LIBERO-Object\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"log_path\": \"logs/eval-crm-k1-object-seed42-plan702-r2.log\", \"checkpoint_path\": \"N/A\"}}, \"eval-perdof-object-norm02-seed48\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T23:05:24.390Z\", \"updated_at\": \"2026-05-20T14:26:11.524Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm02-seed48.log\"}, \"hypothesis\": \"perdof CRM (ε=0.2) K=10 on LIBERO-Object seed48. Additional seed for per-DoF CRM magnitude curve at ε=0.2.\", \"reproduce\": {\"finished_at\": \"2026-05-18T14:34:34.906Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T14:34:41.150875+00:00\"}]}, \"metrics\": {\"sr\": 0.07, \"total\": 100, \"successes\": 7, \"benchmark\": \"object\", \"mode\": \"crm_perdof\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T14:37:45.818Z\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed48.json\"}, \"eval-argmin-object-k5-seed44-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T17:04:51.797Z\", \"updated_at\": \"2026-05-20T14:26:08.978Z\", \"hypothesis\": \"Argmin (reconvla) baseline K=5 on LIBERO-Object seed44, retry 2. Re-run after prior failure for argmin K=5 ablation data.\", \"parent\": \"eval-argmin-object-k5-seed44\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/models/smolvla_libero\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-object-k5-seed44-r2.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T19:15:44.419Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T19:15:57.007322+00:00\"}]}, \"metrics\": {\"sr\": 0.11, \"total\": 100, \"successes\": 11, \"benchmark\": \"object\", \"mode\": \"reconvla\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T19:18:26.273Z\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed44_r2.json\"}, \"eval-vla-only-goal-seed44-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T17:04:56.660Z\", \"updated_at\": \"2026-05-20T14:26:03.273Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Goal seed44, retry 2. Re-run for reliable VLA-only Goal baseline data after prior process death.\", \"parent\": \"eval-vla-only-goal-seed44\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode vla_only --benchmark goal --n_rollouts 10 --seed 44 --K 1 --output_file logs/eval_goal_vla_only_seed44_r2.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"pid\": \"902257\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-goal-seed44-r2.log\", \"submitted_at\": \"2026-05-19T17:05:20.578Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 100, \"model_name\": \"SmolVLA\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/models/smolvla_libero\", \"eval_data\": \"LIBERO-Goal (10 tasks x 10 rollouts)\", \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 4765.3, \"gpu_hours\": 1.32}, \"reproduce\": {\"finished_at\": \"2026-05-19T18:22:25.329Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T18:22:33.642415+00:00\"}]}, \"metrics\": {\"sr\": 0.73, \"total\": 100, \"successes\": 73, \"benchmark\": \"goal\", \"mode\": \"vla_only\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T18:24:45.878Z\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed44_r2.json\"}, \"eval-obs-only-spatial-norm02-seed46-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T17:04:55.082Z\", \"updated_at\": \"2026-05-20T14:25:59.677Z\", \"hypothesis\": \"obs_only CRM (ε=0.2) K=10 on LIBERO-Spatial seed46, retry 2. Re-run after prior process death. Tests CRM spatial generalization.\", \"parent\": \"eval-obs-only-spatial-norm02-seed46\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_spatial_obs_only_norm02_seed46_r2.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"901980\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-spatial-norm02-seed46-r2.log\", \"submitted_at\": \"2026-05-19T17:05:17.649Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial (10 tasks x 10 rollouts)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"wall_clock_seconds\": 9106.4, \"gpu_hours\": 2.53}, \"reproduce\": {\"finished_at\": \"2026-05-19T18:52:06.543Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T18:52:25.091547+00:00\"}]}, \"metrics\": {\"sr\": 0.33, \"total\": 100, \"successes\": 33, \"benchmark\": \"spatial\", \"mode\": \"crm_obs_only\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T19:37:04.048Z\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed46_r2.json\"}, \"eval-obs-only-object-norm02-seed43-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:48:21.840Z\", \"updated_at\": \"2026-05-20T13:52:55.943Z\", \"hypothesis\": \"CRM obs_only K=10 norm02 on LIBERO-Object seed43, retry 3. Prior attempts failed. Filling seed gap for Object CRM to balance seed count with other configs.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 ... python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 43 --n_rollouts 10 --K 10 --crm_checkpoint .../crm_best.pt --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"401735\", \"log_path\": \"logs/eval-obs-only-object-norm02-seed43-r3.log\", \"submitted_at\": \"2026-05-20T10:51:59.845Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": \"100 (10 tasks x 10 rollouts)\", \"model_name\": \"SmolVLA + CRM obs_only (K=10, norm02)\", \"seed\": 43, \"wall_clock_seconds\": 10856.1, \"gpu_hours\": 3.02}, \"reproduce\": {\"finished_at\": \"2026-05-20T13:52:50.001Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"metrics\": {\"sr\": 16}, \"completed_at\": \"2026-05-20T13:52:55.943Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T13:53:04.275658+00:00\"}]}}, \"eval-latency-profiling-v1\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"pipeline_latency_ms\": 247, \"crm_latency_ms\": 0.27}, \"retry_count\": 0, \"created_at\": \"2026-05-20T13:50:06.703Z\", \"updated_at\": \"2026-05-20T13:50:45.112Z\", \"hypothesis\": \"Latency profiling for VLA+CRM pipeline. Measures wall-clock time for K=1/5/10/20 VLA sampling + CRM inference + conformal scoring.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/profile_latency.py --output logs/latency_profiling_v1.json 2>&1 | tee logs/eval-latency-profiling-v1.log\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"pid\": \"367510\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-latency-profiling-v1.log\", \"submitted_at\": \"2026-05-20T13:50:43.790Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-adaptive-k-spatial-p75-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:44:41.144Z\", \"updated_at\": \"2026-05-20T13:33:48.420Z\", \"hypothesis\": \"Adaptive K with τ=P75 (0.098735, Object-calibrated) on LIBERO-Spatial seed44. Third seed for cross-benchmark P75 threshold sweep. Existing: seed42=31%, seed43=34%. Validates P75 consistency on Spatial.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode adaptive_k --adaptive_threshold 0.098735 --k_full 10 --benchmark spatial --seed 44 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_adaptive_k_spatial_p75_seed44.json 2>&1 | tee logs/eval-adaptive-k-spatial-p75-seed44.log\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"pid\": \"307478\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p75-seed44.log\", \"submitted_at\": \"2026-05-20T10:45:04.882Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 8234.3, \"gpu_hours\": 2.29}, \"reproduce\": {\"finished_at\": \"2026-05-20T13:02:13.189Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T13:02:19.186Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T13:02:27.342044+00:00\"}]}, \"metrics\": {\"sr\": 33, \"avg_k\": 5.054, \"fast_path_pct\": 61.8, \"mean_l2\": 0.092, \"total_rollouts\": 100, \"threshold\": 0.098735}, \"notes\": \"SIGHUP false failure (同 P25-seed44 模式)。全部 100 rollouts 完成, SR=33%。已从 memory.md 恢复 metrics 并修正 conclusion=success。\"}, \"eval-obs-only-goal-norm02-seed51\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:48:04.411Z\", \"updated_at\": \"2026-05-20T13:32:36.837Z\", \"hypothesis\": \"CRM obs_only K=10 norm02 on LIBERO-Goal seed51. Multi-seed supplement to address R2 seed imbalance concern. CRM should outperform VLA-only baseline on Goal OOD.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 ... python -u src/evaluate.py --mode crm_obs_only --benchmark goal --seed 51 --n_rollouts 10 --K 10 --crm_checkpoint .../crm_best.pt --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"401661\", \"log_path\": \"logs/eval-obs-only-goal-norm02-seed51.log\", \"submitted_at\": \"2026-05-20T10:51:48.054Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Goal\", \"data_count\": \"100 (10 tasks x 10 rollouts)\", \"model_name\": \"SmolVLA + CRM obs_only (K=10, norm02)\", \"seed\": 51, \"wall_clock_seconds\": 9448.7, \"gpu_hours\": 2.62}, \"reproduce\": {\"finished_at\": \"2026-05-20T13:29:19.616Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T13:29:16.734Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T13:29:36.596426+00:00\"}]}, \"metrics\": {\"sr\": 66, \"total_rollouts\": 100, \"per_task_sr\": {\"open_middle_drawer\": 40, \"put_bowl_on_stove\": 90, \"put_wine_bottle_on_cabinet\": 50, \"open_top_drawer_put_bowl\": 40, \"put_bowl_on_cabinet\": 80, \"push_plate_to_stove\": 90, \"put_cream_cheese_in_bowl\": 20, \"turn_on_stove\": 100, \"put_bowl_on_plate\": 100, \"put_wine_bottle_on_rack\": 50}}, \"notes\": \"Cron false positive — 日志在 /root/acr-vla-conformal-refinement/logs/ 而非 ~/runs/，cron 找不到日志文件误判为 dead。全部 100 rollouts 完成, SR=66%。手动修正 conclusion=success。Goal OOD 持续 neutral (新 n=7: ~67.7% vs VLA 68.7%)。\"}, \"eval-adaptive-k-spatial-p25-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:44:42.913Z\", \"updated_at\": \"2026-05-20T13:31:25.501Z\", \"hypothesis\": \"Adaptive K with τ=P25 (0.054959, Object-calibrated) on LIBERO-Spatial seed44. Third seed for cross-benchmark P25 threshold sweep. Completes Spatial sweep table (P25/P50/P75/P90 × 3 seeds).\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode adaptive_k --adaptive_threshold 0.054959 --k_full 10 --benchmark spatial --seed 44 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_adaptive_k_spatial_p25_seed44.json 2>&1 | tee logs/eval-adaptive-k-spatial-p25-seed44.log\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"pid\": \"307754\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p25-seed44.log\", \"submitted_at\": \"2026-05-20T10:45:08.304Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 9814.2, \"gpu_hours\": 2.73}, \"reproduce\": {\"finished_at\": \"2026-05-20T13:28:36.510Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T13:28:42.550Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T13:28:50.956621+00:00\"}]}, \"metrics\": {\"sr\": 32, \"avg_k\": 7.693, \"fast_path_pct\": 28.8, \"mean_l2\": 0.0896, \"total_rollouts\": 100, \"per_task_sr\": {\"between_plate_and_ramekin\": 70, \"next_to_ramekin\": 100, \"from_table_center\": 0, \"on_cookie_box\": 40, \"in_top_drawer\": 10, \"on_ramekin\": 0, \"next_to_cookie_box\": 80, \"on_stove\": 0, \"next_to_plate\": 20, \"on_wooden_cabinet\": 0}}, \"notes\": \"SIGHUP false failure — 全部 100 rollouts 完成, SR=32%, JSON 已保存。EXIT_CODE=129 发生在结果保存之后 (同 P75-seed44 模式)。手动修正 conclusion=success。\"}, \"eval-vla-only-object-seed50\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T21:24:17.487Z\", \"updated_at\": \"2026-05-20T13:27:12.624Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Object seed50. Additional VLA-only baseline seed for balanced comparison with CRM n=8.\", \"spec\": {\"command\": \"bash -c \\\"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 50 --K 1 --output_file logs/eval_object_vla_only_seed50.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"161416\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-object-seed50.log\", \"submitted_at\": \"2026-05-19T21:24:34.631Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": \"100 (10 tasks x 10 rollouts)\", \"model_name\": \"SmolVLA\", \"seed\": 50, \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 8083.0, \"gpu_hours\": 2.25}, \"reproduce\": {\"finished_at\": \"2026-05-19T23:17:13.814Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T23:17:28.740244+00:00\"}]}, \"metrics\": {\"success_rate\": 0.09, \"total_rollouts\": 100, \"successes\": 9, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.2}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T23:39:17.611Z\"}, \"eval-openvla-object-baseline-seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T16:53:24.027Z\", \"updated_at\": \"2026-05-20T13:26:22.725Z\", \"hypothesis\": \"OpenVLA baseline on LIBERO-Object seed42. Tests original OpenVLA performance as reference for SmolVLA-based CRM comparison.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/openvla-repo && CUDA_VISIBLE_DEVICES=4 TRANSFORMERS_OFFLINE=1 HF_HUB_OFFLINE=1 python experiments/robot/libero/run_libero_eval.py --model_family openvla --pretrained_checkpoint /root/autodl-tmp/models/openvla-libero-object --task_suite_name libero_object --center_crop True --seed 42 --num_trials_per_task 50 --use_wandb False\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"pid\": \"900134\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-openvla-object-baseline-seed42.log\", \"submitted_at\": \"2026-05-19T17:03:26.372Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 500, \"model_name\": \"OpenVLA-7B-finetuned-libero-object\", \"seed\": 42, \"note\": \"conclusion=killed is STALE from M023 incident. Process alive (PID 900134, 22967 MiB). Cron will overwrite conclusion on completion.\", \"wall_clock_seconds\": 21610.5, \"gpu_hours\": 6.0}, \"conclusion\": \"killed\", \"reproduce\": {\"finished_at\": \"2026-05-19T23:03:35.338Z\"}, \"failure_reason\": \"EXIT_CODE=124 (timeout — exceeded timeout_hours)\", \"completed_at\": \"2026-05-19T23:03:36.901Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T23:03:50.026732+00:00\"}]}, \"notes\": \"失败原因: EXIT_CODE=124 timeout。完成 400/500 episodes (8/10 tasks)，SR=68.0% (272/400)。第9个task (pick_up_milk) 4/50时被kill。每episode ~60s，500 episodes需~8.3h但timeout仅~6h。已有成果: 前8个task数据完整。建议: 加大timeout_hours至12h重跑。\"}, \"eval-argmin-object-seed49\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:49:04.530Z\", \"updated_at\": \"2026-05-20T13:17:52.468Z\", \"hypothesis\": \"Argmin (reconvla) baseline on LIBERO-Object seed49 K=10. Multi-seed supplement to ensure Argmin vs CRM comparison has balanced seed counts.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode reconvla --benchmark object --seed 49 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_argmin_object_seed49.json 2>&1 | tee logs/eval-argmin-object-seed49.log\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"364578\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-object-seed49.log\", \"submitted_at\": \"2026-05-20T10:52:16.833Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": \"100 (10 tasks x 10 rollouts)\", \"model_name\": \"SmolVLA + CRM reconvla/argmin (K=10)\", \"seed\": 49, \"wall_clock_seconds\": 8076.0, \"gpu_hours\": 2.24}, \"reproduce\": {\"finished_at\": \"2026-05-20T12:37:14.590Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T12:37:31.282466+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.16, \"total_successes\": 16, \"total_rollouts\": 100, \"seed\": 49, \"benchmark\": \"LIBERO-Object\", \"K\": 10, \"mode\": \"reconvla (argmin baseline)\", \"per_task_sr\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.2, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.4, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0.1, \"pick_up_the_butter_and_place_it_in_the_basket\": 0.1, \"pick_up_the_milk_and_place_it_in_the_basket\": 0.3, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.3, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.2}}, \"checkpoint_path\": \"N/A - eval only\", \"completed_at\": \"2026-05-20T13:06:52.868Z\", \"log_path\": \"logs/eval-argmin-object-seed49.log\"}, \"eval-vla-only-object-seed48\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T20:10:31.390Z\", \"updated_at\": \"2026-05-20T13:07:45.322Z\", \"hypothesis\": \"VLA-only baseline on LIBERO-Object seed48. Expanding VLA-only baseline seed count for balanced comparison.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 48 --K 1 --output_file logs/eval_object_vla_only_seed48.json\", \"server\": \"bjb2-40593\", \"data_path\": \"/root/acr-vla-conformal-refinement/src/evaluate.py\", \"data_count\": 10, \"model_name\": \"smolvla_libero\", \"seed\": 48, \"checkpoint_source\": \"N/A (vla_only mode)\", \"eval_data\": \"LIBERO object benchmark\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T23:44:09.440Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T23:44:13.876Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T23:44:21.445973+00:00\"}]}, \"metrics\": {\"success_rate\": 0.1, \"n_episodes\": 100}}, \"eval-argmin-object-seed48\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:48:49.157Z\", \"updated_at\": \"2026-05-20T13:07:28.620Z\", \"hypothesis\": \"Argmin (reconvla) baseline on LIBERO-Object seed48 K=10. Multi-seed supplement to ensure Argmin vs CRM comparison has balanced seed counts.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode reconvla --benchmark object --seed 48 --n_rollouts 10 --K 10 --output_file logs/eval_argmin_object_seed48.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"364112\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-object-seed48.log\", \"submitted_at\": \"2026-05-20T10:52:13.169Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": \"100\", \"model_name\": \"SmolVLA + CRM reconvla/argmin (K=10)\", \"seed\": 48, \"wall_clock_seconds\": 8115.5, \"gpu_hours\": 2.25}, \"reproduce\": {\"finished_at\": \"2026-05-20T12:38:14.157Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T12:38:24.965919+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}, \"checkpoint_path\": \"logs/eval_argmin_object_seed48.json\", \"completed_at\": \"2026-05-20T13:07:28.620Z\"}, \"eval-obs-only-spatial-norm02-seed48\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T03:14:26.858Z\", \"updated_at\": \"2026-05-20T13:07:16.116Z\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.35, \"per_task\": {\"between_plate_and_ramekin\": 0.8, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.4, \"on_wooden_cabinet\": 0}}, \"hypothesis\": \"obs_only CRM (ε=0.2) K=10 on LIBERO-Spatial seed48. Additional seed for Spatial CRM multi-seed robustness.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --seed 48 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_obs_only_spatial_norm02_seed48.json 2>&1 | tee logs/eval-obs-only-spatial-norm02-seed48.log\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"385298\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-spatial-norm02-seed48.log\", \"submitted_at\": \"2026-05-20T13:07:15.076Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-crm-spatial-seed48.log\", \"completed_at\": \"2026-05-20T07:02:24.551Z\"}, \"eval-obs-only-goal-norm02-seed52\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:48:11.751Z\", \"updated_at\": \"2026-05-20T13:06:48.437Z\", \"hypothesis\": \"CRM obs_only K=10 norm02 on LIBERO-Goal seed52. Multi-seed supplement to address R2 seed imbalance concern. CRM should outperform VLA-only baseline on Goal OOD.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark goal --seed 52 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_obs_only_goal_norm02_seed52.json 2>&1 | tee logs/eval-obs-only-goal-norm02-seed52.log\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"362566\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-goal-norm02-seed52.log\", \"submitted_at\": \"2026-05-20T10:51:55.700Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Goal benchmark\", \"data_count\": 10, \"model_name\": \"crm_v3_norm/obs_only\", \"seed\": 52, \"wall_clock_seconds\": 8092.7, \"gpu_hours\": 2.25}, \"reproduce\": {\"finished_at\": \"2026-05-20T12:06:23.707Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T12:06:30.919538+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.68, \"per_task\": {\"open_middle_drawer\": 0.7, \"bowl_on_stove\": 0.9, \"wine_on_cabinet\": 0.4, \"bowl_in_drawer\": 0.3, \"bowl_on_cabinet\": 0.8, \"plate_to_stove\": 0.8, \"cream_cheese_in_bowl\": 0.4, \"turn_on_stove\": 1, \"bowl_on_plate\": 1, \"wine_on_rack\": 0.5}}, \"checkpoint_path\": \"logs/eval_obs_only_goal_norm02_seed52.json\", \"completed_at\": \"2026-05-20T13:06:48.437Z\"}, \"eval-adaptive-k-spatial-p90-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:44:47.376Z\", \"updated_at\": \"2026-05-20T13:06:03.701Z\", \"hypothesis\": \"Adaptive K with τ=P90 (0.125870, Object-calibrated) on LIBERO-Spatial seed43. Second seed for Spatial P90 threshold. Cross-benchmark validation of aggressive compute saving regime.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode adaptive_k --adaptive_threshold 0.125870 --k_full 10 --benchmark spatial --seed 43 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_adaptive_k_spatial_p90_seed43.json 2>&1 | tee logs/eval-adaptive-k-spatial-p90-seed43.log\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"344852\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p90-seed43.log\", \"submitted_at\": \"2026-05-20T10:45:15.637Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": \"100 (10 tasks x 10 rollouts)\", \"model_name\": \"SmolVLA + CRM adaptive_k (P90, τ=0.125870)\", \"seed\": 43, \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 8448.1, \"gpu_hours\": 2.35}, \"reproduce\": {\"finished_at\": \"2026-05-20T12:36:37.049Z\"}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.32, \"avg_K\": 3.586, \"fast_path_pct\": 80.17, \"mean_l2\": 0.0905, \"adaptive_trigger_rate\": 0.198, \"threshold\": 0.12587, \"total_steps\": 23797, \"fast_steps\": 19079, \"full_steps\": 4718}, \"completed_at\": \"2026-05-20T13:06:03.701Z\"}, \"eval-perdof-object-norm02-seed45-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T23:09:08.601Z\", \"updated_at\": \"2026-05-20T13:05:55.751Z\", \"hypothesis\": \"perdof CRM (ε=0.2) seed45 on LIBERO-Object. r3 重试。补充 perdof magnitude curve ε=0.2 数据。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed45_r3.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": 749547, \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_perdof\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm02-seed45-r3.log\", \"checkpoint_path\": \"N/A (eval only)\"}, \"metrics\": {\"overall_success_rate\": 0.12, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T10:28:49.451Z\"}, \"eval-adaptive-k-spatial-p90-seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:44:45.262Z\", \"updated_at\": \"2026-05-20T12:54:12.191Z\", \"hypothesis\": \"Adaptive K with τ=P90 (0.125870, Object-calibrated) on LIBERO-Spatial seed42. Most aggressive threshold — on Object P90 gives 93% fast_path but SR drops to 13.3%. Tests whether Spatial follows same pattern: high fast_path with SR penalty.\", \"spec\": {\"command\": \"python src/evaluate.py --mode adaptive_k --adaptive_threshold 0.125870 --k_full 10 --benchmark spatial --seed 42\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"308030\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p90-seed42.log\", \"submitted_at\": \"2026-05-20T10:45:11.659Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_v3_obs_only\", \"seed\": 42, \"checkpoint_path\": \"logs/eval_adaptive_k_spatial_p90_seed42.json\", \"wall_clock_seconds\": 7740.5, \"gpu_hours\": 2.15}, \"reproduce\": {\"finished_at\": \"2026-05-20T12:51:00.370Z\"}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"conclusion\": \"success\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T12:51:16.751396+00:00\"}]}, \"metrics\": {\"overall_success_rate\": 0.31, \"avg_K\": 3.5, \"fast_path_pct\": 80.6, \"mean_l2\": 0.0907, \"threshold\": 0.12587, \"total_rollouts\": 100, \"total_successes\": 31, \"per_task\": {\"between_plate_and_ramekin\": 0.6, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.3, \"on_wooden_cabinet\": 0}}, \"notes\": \"Cron false positive: EXIT_CODE=129 (SIGHUP after completion). 日志确认 10/10 tasks × 10 rollouts 全部完成，JSON 已写出。手动修正 conclusion=success。\", \"completed_at\": \"2026-05-20T12:54:12.191Z\"}, \"eval-obs-only-object-norm02-seed49\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:50:37.777Z\", \"updated_at\": \"2026-05-20T12:48:49.975Z\", \"hypothesis\": \"CRM obs_only norm02 (ε=0.2) K=10 on Object seed49. Expanding Object CRM norm02 from n=6 to n=7 for seed balance (R2 concern).\", \"spec\": {\"command\": \"python evaluate.py --mode crm_obs_only --benchmark object --seed 49 --K 10 --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"363770\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-seed49.log\", \"data_path\": \"LIBERO-Object benchmark\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"CRM obs_only v3 norm02\", \"seed\": 49, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}, \"reproduce\": {\"finished_at\": \"2026-05-20T12:43:04.795Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T12:43:15.068937+00:00\"}]}, \"metrics\": {\"overall_success_rate\": 0.14, \"total_rollouts\": 100, \"total_successes\": 14, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}, \"updated_aggregate\": {\"mean_sr\": 16.4, \"std_sr\": 2, \"n_seeds\": 7, \"prior\": \"16.8±1.8% (n=6)\", \"delta_vs_vla_baseline\": \"+5.5pp\"}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T12:48:49.975Z\"}}, \"count\": 50, \"total\": 427, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.146}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Bash · `toolu_012eZvpi5jZEdmNtGsrr39Gk`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/c5300403-6659-4470-875e-d77ab58a370d/tool-results/mcp-agent-ml-research-read_registry-1779299505096.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\nfor k in exps:\n    if 'random' in k and 'object' in k and 'seed46' in k:\n        print(json.dumps({k: exps[k]}, indent=2))\n\"",
  "description": "Search for random-selection-object-seed46 experiments in DONE registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c5300403-6659-4470-875e-d77ab58a370d",
  "uuid": "7e28e86e-7bbf-4db3-af23-e3871b957327",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nb4qNdvRGabK6RATVSoPps",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 730,
      "cache_read_input_tokens": 33827,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 730
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

_source line 18 · 2026-05-20T17:51:50.119Z_

<details><summary>↩ Tool result · `toolu_012eZvpi5jZEdmNtGsrr39Gk`</summary>

```text
{
  "eval-random-selection-object-seed46-r3": {
    "status": "DONE",
    "retry_count": 0,
    "created_at": "2026-05-20T15:36:03.819Z",
    "updated_at": "2026-05-20T17:36:15.098Z",
    "hypothesis": "Random selection baseline on LIBERO-Object seed46 (plan_600). Third attempt on bjb1-18228 with updated code.",
    "spec": {
      "command": "python -u src/evaluate.py --mode random_selection --benchmark object --seed 46 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_random_selection_object_seed46.json",
      "server": "bjb1-18228",
      "gpu": [
        "cuda:1"
      ],
      "pid": "421636",
      "log_path": "logs/eval-random-selection-object-seed46.log",
      "data_path": "LIBERO-Object",
      "data_count": 100,
      "model_name": "SmolVLA_random_selection",
      "seed": 46,
      "checkpoint_source": "/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt",
      "eval_data": "LIBERO-Object",
      "checkpoint_path": "/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt"
    },
    "conclusion": "success",
    "metrics": {
      "overall_success_rate": 0.1,
      "tasks_evaluated": 10,
      "rollouts_per_task": 10,
      "total_rollouts": 100,
      "total_successes": 10
    },
    "completed_at": "2026-05-20T17:36:15.098Z"
  }
}
{
  "eval-random-selection-object-seed46-r2": {
    "status": "DONE",
    "retry_count": 0,
    "created_at": "2026-05-19T01:42:56.456Z",
    "updated_at": "2026-05-20T15:35:34.584Z",
    "hypothesis": "Random selection baseline on LIBERO-Object seed46 (plan_600). Retry after code fix - additional seed for random baseline comparison.",
    "spec": {
      "command": "cd /root/acr-vla-conformal-refinement && timeout 57600 /root/miniconda3/bin/python -u src/evaluate.py --mode random_selection --benchmark object --n_rollouts 10 --seed 46 --K 10 --output_file logs/eval_object_random_selection_seed46.json",
      "server": "bjb2-40593",
      "gpu": [
        "cuda:0"
      ],
      "tmux_session": "eval-random-selection-seed46-t16",
      "data_path": "LIBERO-Object",
      "data_count": 100,
      "model_name": "SmolVLA_random_selection",
      "seed": 46,
      "eval_data": "LIBERO-Object"
    },
    "reproduce": {
      "finished_at": "2026-05-19T17:47:06.031Z"
    },
    "failure_reason": "process dead 5\u00d7 with no sentinel/W&B \u2014 auto-resolved as failed",
    "conclusion": "failed",
    "completed_at": "2026-05-19T17:47:10.111Z",
    "extra": {
      "hook_events": [
        {
          "event": "on_failed",
          "action": "agent",
          "ts": "2026-05-19T17:47:19.928543+00:00"
        }
      ]
    }
  }
}
{
  "eval-random-selection-object-seed46": {
    "status": "DONE",
    "retry_count": 0,
    "created_at": "2026-05-18T16:50:36.635Z",
    "updated_at": "2026-05-20T15:33:54.594Z",
    "hypothesis": "Random selection baseline on LIBERO-Object seed46 (plan_600). Additional seed for random baseline to establish statistical comparison against CRM selection.",
    "conclusion": "failed",
    "failure_reason": "random_selection mode not supported on bjb1-18228",
    "completed_at": "2026-05-18T16:53:31.340Z"
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
  "session_id": "c5300403-6659-4470-875e-d77ab58a370d",
  "uuid": "837d3f48-83d4-4b0e-8e71-042157949f63",
  "tool_use_result": {
    "stdout": "{\n  \"eval-random-selection-object-seed46-r3\": {\n    \"status\": \"DONE\",\n    \"retry_count\": 0,\n    \"created_at\": \"2026-05-20T15:36:03.819Z\",\n    \"updated_at\": \"2026-05-20T17:36:15.098Z\",\n    \"hypothesis\": \"Random selection baseline on LIBERO-Object seed46 (plan_600). Third attempt on bjb1-18228 with updated code.\",\n    \"spec\": {\n      \"command\": \"python -u src/evaluate.py --mode random_selection --benchmark object --seed 46 --n_rollouts 10 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_random_selection_object_seed46.json\",\n      \"server\": \"bjb1-18228\",\n      \"gpu\": [\n        \"cuda:1\"\n      ],\n      \"pid\": \"421636\",\n      \"log_path\": \"logs/eval-random-selection-object-seed46.log\",\n      \"data_path\": \"LIBERO-Object\",\n      \"data_count\": 100,\n      \"model_name\": \"SmolVLA_random_selection\",\n      \"seed\": 46,\n      \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\",\n      \"eval_data\": \"LIBERO-Object\",\n      \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"\n    },\n    \"conclusion\": \"success\",\n    \"metrics\": {\n      \"overall_success_rate\": 0.1,\n      \"tasks_evaluated\": 10,\n      \"rollouts_per_task\": 10,\n      \"total_rollouts\": 100,\n      \"total_successes\": 10\n    },\n    \"completed_at\": \"2026-05-20T17:36:15.098Z\"\n  }\n}\n{\n  \"eval-random-selection-object-seed46-r2\": {\n    \"status\": \"DONE\",\n    \"retry_count\": 0,\n    \"created_at\": \"2026-05-19T01:42:56.456Z\",\n    \"updated_at\": \"2026-05-20T15:35:34.584Z\",\n    \"hypothesis\": \"Random selection baseline on LIBERO-Object seed46 (plan_600). Retry after code fix - additional seed for random baseline comparison.\",\n    \"spec\": {\n      \"command\": \"cd /root/acr-vla-conformal-refinement && timeout 57600 /root/miniconda3/bin/python -u src/evaluate.py --mode random_selection --benchmark object --n_rollouts 10 --seed 46 --K 10 --output_file logs/eval_object_random_selection_seed46.json\",\n      \"server\": \"bjb2-40593\",\n      \"gpu\": [\n        \"cuda:0\"\n      ],\n      \"tmux_session\": \"eval-random-selection-seed46-t16\",\n      \"data_path\": \"LIBERO-Object\",\n      \"data_count\": 100,\n      \"model_name\": \"SmolVLA_random_selection\",\n      \"seed\": 46,\n      \"eval_data\": \"LIBERO-Object\"\n    },\n    \"reproduce\": {\n      \"finished_at\": \"2026-05-19T17:47:06.031Z\"\n    },\n    \"failure_reason\": \"process dead 5\\u00d7 with no sentinel/W&B \\u2014 auto-resolved as failed\",\n    \"conclusion\": \"failed\",\n    \"completed_at\": \"2026-05-19T17:47:10.111Z\",\n    \"extra\": {\n      \"hook_events\": [\n        {\n          \"event\": \"on_failed\",\n          \"action\": \"agent\",\n          \"ts\": \"2026-05-19T17:47:19.928543+00:00\"\n        }\n      ]\n    }\n  }\n}\n{\n  \"eval-random-selection-object-seed46\": {\n    \"status\": \"DONE\",\n    \"retry_count\": 0,\n    \"created_at\": \"2026-05-18T16:50:36.635Z\",\n    \"updated_at\": \"2026-05-20T15:33:54.594Z\",\n    \"hypothesis\": \"Random selection baseline on LIBERO-Object seed46 (plan_600). Additional seed for random baseline to establish statistical comparison against CRM selection.\",\n    \"conclusion\": \"failed\",\n    \"failure_reason\": \"random_selection mode not supported on bjb1-18228\",\n    \"completed_at\": \"2026-05-18T16:53:31.340Z\"\n  }\n}",
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

_source line 19_

<details><summary>Logged reasoning block</summary>

```text
The experiment `eval-random-selection-object-seed46-r3` already has status=DONE, conclusion=success, with metrics. It was already resolved. The cron just needs to be deleted.

Let me check - the task says "Cron 报告进程已退出，无 W&B 数据。需要判断是 success 还是 failed。" But looking at the registry, it's already marked as DONE with conclusion=success and metrics. So someone (or some hook) already resolved this.

Let me just delete the cron since the experiment is already resolved.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c5300403-6659-4470-875e-d77ab58a370d",
  "uuid": "637105fe-c658-44b2-9cf0-0ed3564956e1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013PgFEtAeWtb7aknGk7nv33",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1515,
      "cache_read_input_tokens": 34557,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1515
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

实验已在 registry 中标记为 DONE/success，metrics 已记录（success_rate=0.1, 即 10%）。只需清理 cron。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c5300403-6659-4470-875e-d77ab58a370d",
  "uuid": "859463af-bb9c-43fc-915b-4128aa5b84e4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013PgFEtAeWtb7aknGk7nv33",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1515,
      "cache_read_input_tokens": 34557,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1515
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__delete_cron · `toolu_01PwBBLjeC7xvmDVrira7EQv`</summary>

```json
{
  "exp_id": "eval-random-selection-object-seed46-r3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c5300403-6659-4470-875e-d77ab58a370d",
  "uuid": "e5368ed9-0462-4892-b26c-1d34344c5c2d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013PgFEtAeWtb7aknGk7nv33",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1515,
      "cache_read_input_tokens": 34557,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1515
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

_source line 22 · 2026-05-20T17:51:58.495Z_

<details><summary>↩ Tool result · `toolu_01PwBBLjeC7xvmDVrira7EQv`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No cron found for 'eval-random-selection-object-seed46-r3'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c5300403-6659-4470-875e-d77ab58a370d",
  "uuid": "07a8fdcf-ee11-42ee-88a6-cc8cbab37c8b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"No cron found for 'eval-random-selection-object-seed46-r3'.\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"No cron found for 'eval-random-selection-object-seed46-r3'.\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 23_

Cron 也已不存在。

**总结**：`eval-random-selection-object-seed46-r3` 已被处理完毕：
- **Status**: DONE
- **Conclusion**: success
- **Metrics**: overall_success_rate=10%, 100 rollouts, 10 successes
- **Server**: bjb1-18228, cuda:1
- **Cron**: 已清理（不存在）

无需进一步操作。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c5300403-6659-4470-875e-d77ab58a370d",
  "uuid": "b4a4127e-37b2-4579-85a5-57e1ea118946",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016qR1CYwfA5YzkbXZJpwfQj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 336,
      "cache_read_input_tokens": 36072,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 336
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

### Task result

_source line 24_

Cron 也已不存在。

**总结**：`eval-random-selection-object-seed46-r3` 已被处理完毕：
- **Status**: DONE
- **Conclusion**: success
- **Metrics**: overall_success_rate=10%, 100 rollouts, 10 successes
- **Server**: bjb1-18228, cuda:1
- **Cron**: 已清理（不存在）

无需进一步操作。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 43945,
  "duration_api_ms": 40600,
  "num_turns": 7,
  "stop_reason": "end_turn",
  "session_id": "c5300403-6659-4470-875e-d77ab58a370d",
  "total_cost_usd": 0.28423424999999997,
  "usage": {
    "input_tokens": 11,
    "cache_creation_input_tokens": 24567,
    "cache_read_input_tokens": 189985,
    "output_tokens": 1372,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 24567,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 122,
        "cache_read_input_tokens": 36072,
        "cache_creation_input_tokens": 336,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 336
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1213,
      "outputTokens": 26,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001343,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 11,
      "outputTokens": 1372,
      "cacheReadInputTokens": 189985,
      "cacheCreationInputTokens": 24567,
      "webSearchRequests": 0,
      "costUSD": 0.28289125,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "e14b240a-0cdc-4b50-8804-fb95c66d52ad"
}
```

</details>

---
