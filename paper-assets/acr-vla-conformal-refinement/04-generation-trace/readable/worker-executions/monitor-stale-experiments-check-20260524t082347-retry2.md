# monitor stale experiments check 20260524T082347 retry2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 68
- **Recorded user turns:** 0
- **Tool calls:** 22
- **Original source:** `logs/workers/worker_monitor_stale-experiments-check_20260524T082347_retry2.log`
- **Structured JSON:** [`4cca88934410c350e631.json`](../../sessions/4c/4cca88934410c350e631.json)

## Before a recorded user message

68 recorded events

### System

_source line 1_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement",
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
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
  "uuid": "6e38e150-c89e-40a0-9502-bad0d555ab19",
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
    "resetsAt": 1779628200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "35e1acbf-99d8-4f32-aed7-30238e4ca956",
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8"
}
```

---

### Assistant

_source line 3_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the registry for the two stale experiments and checking the bjb2-28827 server in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "4dffdfae-3463-415d-9a2e-94902241088b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D7eX1iwSQVyZAEPa1xwqe4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11592,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11592
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

_source line 4_

先查 registry 获取两个 stale 实验的信息，同时检查 bjb2-28827 上的进程状态。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "155b2761-5e3c-4d94-9031-57b1d6d760f5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D7eX1iwSQVyZAEPa1xwqe4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11592,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11592
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_015aScAzmJJ3BhkfU39EFbzg`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry",
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
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "7d36f3d9-06af-47a8-9988-66f3a8a5cc0e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D7eX1iwSQVyZAEPa1xwqe4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11592,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11592
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

_source line 6 · 2026-05-24T08:24:08.490Z_

<details><summary>↩ Tool result · `toolu_015aScAzmJJ3BhkfU39EFbzg`</summary>

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
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "07fcc98e-d816-4413-839c-d0d26ae53a1c",
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

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01H3SnaEKyPF2jspxZuei3EX`</summary>

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
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "7352d299-d877-4aab-b90c-ad4db39fd5b9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017ucULA8UF5vstH9FRqXdLJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1591,
      "cache_read_input_tokens": 23433,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1591
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

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Eu9ocUpcX8Rqgo2pW2APws`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "ps -p 121241,96831,97307,97070,97550 -o pid,stat,etime,cmd --no-headers",
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
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "1d24c597-8a4d-4f47-a805-0c7d7fecba92",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017ucULA8UF5vstH9FRqXdLJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1591,
      "cache_read_input_tokens": 23433,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1591
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

_source line 9 · 2026-05-24T08:24:23.619Z_

<details><summary>↩ Tool result · `toolu_01H3SnaEKyPF2jspxZuei3EX`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-supp-long-k2mean-s46\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T03:23:24.189Z\", \"updated_at\": \"2026-05-24T08:15:23.138Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark long --mode vla_only --baseline_mode mean --K 2 --seed 46 --n_rollouts 20 --output_file logs/eval_long_k2mean_seed46.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": 263191, \"log_path\": \"logs/eval_long_k2mean_seed46.json\", \"submitted_at\": \"2026-05-24T03:23:22.142Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 46, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"n/a-baseline\"}, \"hypothesis\": \"VLA-only K=2 mean baseline on LIBERO-Long suite seed46 provides the fifth seed for Long K2-mean variance analysis, establishing the unrefined baseline performance across seeds.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.55, \"successes\": 110, \"total\": 200, \"source\": \"json_harvest_bjb1-32546\"}}, \"eval-supp-long-crm-norm005-s46\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T00:55:34.833Z\", \"updated_at\": \"2026-05-24T08:15:19.358Z\", \"hypothesis\": \"CRM obs-only refinement with max_correction_norm=0.05 on LIBERO-Long suite seed46 provides the fifth seed for Long CRM obs-only variance analysis, testing conservative correction magnitude across seeds.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark long --mode crm_obs_only --seed 46 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": 262247, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-crm-norm005-s46.log\", \"submitted_at\": \"2026-05-24T03:23:09.570Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 46, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.54, \"successes\": 108, \"total\": 200, \"source\": \"json_harvest_bjb1-32546\"}}, \"eval-supp-long-reconvla-s46\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T00:55:40.981Z\", \"updated_at\": \"2026-05-24T08:06:46.631Z\", \"hypothesis\": \"ReconVLA evaluation on LIBERO-Long suite seed46 provides the fifth seed for Long ReconVLA variance analysis, measuring reconstruction-based refinement consistency across seeds.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark long --mode reconvla --seed 46 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": 262529, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-reconvla-s46.log\", \"submitted_at\": \"2026-05-24T03:23:15.265Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 46, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.56, \"successes\": 112, \"total\": 200, \"source\": \"json_harvest_bjb1-32546\"}}, \"eval-supp-k2mean-spatial-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:15:55.833Z\", \"updated_at\": \"2026-05-24T07:18:30.230Z\", \"hypothesis\": \"K=2 mean baseline on Spatial suite seed47. Sixth seed extending variance analysis. 5-seed mean ~80%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark spatial --mode vla_only --baseline_mode mean --K 2 --seed 47 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:3\"], \"tmux_session\": \"spatial-k2mean-s47\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"checkpoint_source\": \"n/a-baseline\"}}, \"eval-supp-reconvla-spatial-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:15:47.910Z\", \"updated_at\": \"2026-05-24T07:18:23.847Z\", \"hypothesis\": \"Reconvla K=10 on Spatial suite seed47. Sixth seed extending variance analysis. 5-seed mean ~80%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark spatial --mode reconvla --seed 47 --n_rollouts 20 --K 10\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:2\"], \"tmux_session\": \"spatial-reconvla-s47\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA+Reconvla\", \"seed\": 47, \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"checkpoint_source\": \"n/a-reconvla\"}}, \"eval-supp-adapt-tau025-spatial-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:15:43.884Z\", \"updated_at\": \"2026-05-24T07:18:17.441Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Spatial suite seed47. Sixth seed extending variance analysis. 5-seed mean ~80.5%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark spatial --mode adaptive_conformal_crm --seed 47 --n_rollouts 20 --K 10 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:1\"], \"tmux_session\": \"spatial-adapt-s47\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA+Adaptive CRM\", \"seed\": 47, \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\"}}, \"eval-supp-vla-only-spatial-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:15:40.347Z\", \"updated_at\": \"2026-05-24T07:18:10.979Z\", \"hypothesis\": \"VLA-only baseline on Spatial suite seed47. Sixth seed extending variance analysis. 5-seed mean ~78.7%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode vla_only --seed 47 --n_rollouts 20 --K 1\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:0\"], \"tmux_session\": \"spatial-vla-s47\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"checkpoint_source\": \"n/a-baseline\"}}, \"eval-supp-goal-vla-only-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:14:14.567Z\", \"updated_at\": \"2026-05-24T07:17:13.996Z\", \"hypothesis\": \"Goal s47 VLA-only (K=1) baseline to extend Goal seed coverage beyond s42-s46 for supplementary variance analysis.\", \"parent\": \"eval-supp-goal-vla-only-s46\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark goal --mode vla_only --seed 47 --n_rollouts 20 --K 1\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": 279117, \"tmux_session\": \"goal-vla-s47\", \"log_path\": \"logs/eval-supp-goal-vla-only-s47.log\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Goal\", \"checkpoint_source\": \"n/a-baseline\", \"checkpoint_path\": \"n/a-eval-only\"}}, \"eval-supp-long-vla-only-s47-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:14:04.522Z\", \"updated_at\": \"2026-05-24T07:17:06.584Z\", \"hypothesis\": \"Long s47 VLA-only (K=1) baseline to complete the Long s47 seed extension set. The existing eval-supp-long-vla-only-s47 is actually k2mean (K=2 mean), so this fills the true VLA-only gap.\", \"parent\": \"eval-supp-long-vla-only-s46\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark long --mode vla_only --seed 47 --n_rollouts 20 --K 1\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": 278846, \"tmux_session\": \"long-vla-s47-r2\", \"log_path\": \"logs/eval-supp-long-vla-only-s47-r2.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"n/a-baseline\", \"checkpoint_path\": \"n/a-eval-only\"}}, \"eval-supp-adapt-tau025-spatial-s46\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:12:18.821Z\", \"updated_at\": \"2026-05-24T07:16:50.821Z\", \"hypothesis\": \"CRM/Adaptive on Spatial seed46, 5th seed extension\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark spatial --mode adaptive_conformal_crm --seed 46 --n_rollouts 20 --K 10 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO spatial suite\", \"data_count\": 200, \"model_name\": \"SmolVLA + Adaptive CRM (crm_smolvla_3suite_v1)\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 20 rollouts\"}, \"failure_reason\": \"GPU 1 occupied by OpenVLA VLA-only eval (PID 114990). Not actually started despite RUNNING status. Will deploy when GPU frees up.\"}, \"eval-supp-crm-norm005-spatial-s46\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:12:15.210Z\", \"updated_at\": \"2026-05-24T07:14:47.458Z\", \"hypothesis\": \"CRM/Adaptive on Spatial seed46, 5th seed extension\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 46 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO spatial\", \"data_count\": 200, \"model_name\": \"smolvla+crm_smolvla_3suite_v1\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 20 rollouts\"}}, \"eval-openvla-object-vla-only-seed42-v3\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:07:37.003Z\", \"updated_at\": \"2026-05-24T07:08:07.984Z\", \"hypothesis\": \"After fixing OpenVLA loading for transformers 5.8.1 (model_type 'openvla' auto-registration via openvla_compat + PrismaticImageProcessor workaround), VLA-only baseline on LIBERO-Object seed42 should reproduce the previously observed ~69% success rate from eval-openvla-object-vla-only-seed42-v2. Validates that the new loader path preserves model behavior bit-for-bit.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u src/openvla_eval.py --benchmark object --model_path /root/autodl-tmp/models/openvla-libero-object --mode vla_only --seed 42 --n_rollouts 20 --gpu 0 --output_file logs/eval_openvla_object_vla_only_seed42_v3.json\", \"server\": \"bjb2-28827\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_object\", \"data_count\": 200, \"model_name\": \"openvla-libero-object\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/openvla-libero-object\", \"eval_data\": \"LIBERO-Object (10 tasks x 20 rollouts = 200 episodes)\", \"pid\": \"114984\", \"log_path\": \"/tmp/eval_openvla_vla_only_seed42_v3.log\", \"checkpoint_path\": \"/root/autodl-tmp/models/openvla-libero-object\"}}, \"eval-supp-long-vla-only-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:34:23.532Z\", \"updated_at\": \"2026-05-24T07:05:36.964Z\", \"hypothesis\": \"K=2 mean baseline on Long suite seed47 (NOT VLA-only — actual command uses --baseline_mode mean --K 2, output eval_long_k2mean_seed47.json). Misnamed at creation. Paired with Adapt-s47 for matched-seed comparison.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark long --mode vla_only --baseline_mode mean --K 2 --seed 47 --n_rollouts 20 --output_file logs/eval_long_k2mean_seed47.json\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:5\"], \"tmux_session\": \"long-vla-s47\", \"log_path\": \"logs/eval-supp-long-vla-only-s47.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"n/a-baseline\", \"parent\": \"eval-supp-long-vla-only-s46\"}}, \"eval-supp-long-crm-norm005-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:52:08.968Z\", \"updated_at\": \"2026-05-24T06:53:16.695Z\", \"hypothesis\": \"CRM obs-only norm=0.05 on Long suite seed47 (sixth seed extension). Pairs with running Long vla-only-s47 and adapt-s47 on cqa1-32758 to tighten Long suite CI which has highest variance.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark long --mode crm_obs_only --seed 47 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"tmux_session\": \"long-crm-s47\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-crm-norm005-s47.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\"}}, \"eval-supp-long-reconvla-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:52:05.630Z\", \"updated_at\": \"2026-05-24T06:53:02.593Z\", \"hypothesis\": \"Reconvla K=10 on Long suite seed47 (sixth seed extension). Pairs with running Long vla-only-s47 and adapt-s47 on cqa1-32758 to tighten Long suite CI which has highest variance.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark long --mode reconvla --seed 47 --n_rollouts 20 --K 10\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"tmux_session\": \"long-reconvla-s47\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-reconvla-s47.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"n/a-reconvla\"}}, \"eval-supp-spatial-crm-norm005-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:49:40.206Z\", \"updated_at\": \"2026-05-24T06:51:27.049Z\", \"hypothesis\": \"CRM obs_only norm=0.05 on LIBERO-Spatial seed47. Fifth seed extending Spatial CRM coverage (s43-s46 mean ~79.6%). Tightens CI for statistical comparison with VLA-only/K2mean/Reconvla/Adaptive at matched 5-seed coverage.\", \"parent\": \"eval-supp-spatial-crm-norm005-s46\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 47 --n_rollouts 20 --max_correction_norm 0.05 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_spatial_crm_obs_only_norm0.05_seed47.json\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"235730\", \"tmux_session\": \"eval-spatial-crm-s47\", \"log_path\": \"/tmp/eval_spatial_crm_s47.log\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA+CRM\", \"seed\": 47, \"eval_data\": \"LIBERO-Spatial\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"checkpoint_path\": \"n/a-eval-only\", \"submitted_at\": \"2026-05-24T06:50:07Z\", \"submitted_via\": \"ssh_execute_tmux\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-supp-vla-only-spatial-s46\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:48:57.955Z\", \"updated_at\": \"2026-05-24T06:50:52.276Z\", \"hypothesis\": \"VLA-only baseline on Spatial suite seed46. Extending from 3-seed (s42/s43/s44) to 5-seed for variance analysis. 3-seed mean 78.7%±0.3%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark spatial --mode vla_only --seed 46 --n_rollouts 20 --K 1\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/models/smolvla_libero/\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"benchmark\": \"spatial\", \"mode\": \"vla_only\", \"tmux_session\": \"eval-supp-vla-only-spatial-s46\", \"gpu\": 5}}, \"eval-supp-adapt-tau025-spatial-s45\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:48:54.415Z\", \"updated_at\": \"2026-05-24T06:50:44.120Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 (conformal_threshold) with max_correction_norm=0.2 on Spatial suite seed45. Extending from 3-seed (s42/s43/s44) to 5-seed for variance analysis. 3-seed mean 80.8%±1.1%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark spatial --mode adaptive_conformal_crm --seed 45 --n_rollouts 20 --K 10 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla+crm-adaptive\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"benchmark\": \"spatial\", \"mode\": \"adaptive_conformal_crm\", \"max_correction_norm\": 0.2, \"conformal_threshold\": 0.25, \"K\": 10, \"tmux_session\": \"eval-supp-adapt-tau025-spatial-s45\", \"gpu\": 4}}, \"eval-supp-crm-norm005-spatial-s45\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:48:50.955Z\", \"updated_at\": \"2026-05-24T06:50:37.107Z\", \"hypothesis\": \"CRM always-on norm=0.05 on Spatial suite seed45. Extending from 3-seed (s42/s43/s44) to 5-seed for variance analysis. 3-seed mean 79.8%±1.3%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 45 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla+crm\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"benchmark\": \"spatial\", \"mode\": \"crm_obs_only\", \"max_correction_norm\": 0.05, \"K\": 10, \"tmux_session\": \"eval-supp-crm-norm005-spatial-s45\", \"gpu\": 3}}, \"eval-supp-vla-only-spatial-s45\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:48:46.040Z\", \"updated_at\": \"2026-05-24T06:50:30.794Z\", \"hypothesis\": \"VLA-only baseline on Spatial suite seed45. Extending from 3-seed (s42/s43/s44) to 5-seed for variance analysis. 3-seed mean 78.7%±0.3%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark spatial --mode vla_only --seed 45 --n_rollouts 20 --K 1\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/models/smolvla_libero/\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"benchmark\": \"spatial\", \"mode\": \"vla_only\", \"tmux_session\": \"eval-supp-vla-only-spatial-s45\", \"gpu\": 2}}, \"eval-supp-long-adapt-tau025-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:34:20.287Z\", \"updated_at\": \"2026-05-24T06:38:39.651Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Long suite seed47 (sixth seed extension). Long is the highest-variance suite with smallest improvement margin (57.7 vs 58.0 VLA-only). Sixth seed tightens CI to determine if Adaptive is statistically equivalent to or below VLA-only on Long.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark long --mode adaptive_conformal_crm --seed 47 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --max_correction_norm 0.2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:4\"], \"tmux_session\": \"long-adapt-s47\", \"log_path\": \"logs/eval-supp-long-adapt-tau025-s47.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"parent\": \"eval-supp-long-adapt-tau025-s46-r2\"}}, \"precompute-pi05-long-2048-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:18:31.140Z\", \"updated_at\": \"2026-05-24T06:23:39.262Z\", \"hypothesis\": \"Precomputing π0.5 obs_features and K=2048 action samples on LIBERO-Long enables downstream CRM training for cross-model (SmolVLA→π0.5) generalization verification without re-running inference at train time.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 nohup python -u src/train_crm.py --precompute --model pi05 --benchmark long --K 10 --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/ > /root/autodl-tmp/logs/precompute_pi05_long_2048.log 2>&1 &\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": 114507, \"data_path\": \"/root/autodl-tmp/crm_cache_pi05_2048/long/\", \"data_count\": 136090, \"model_name\": \"pi0.5\", \"seed\": 0, \"log_path\": \"/root/autodl-tmp/logs/precompute_pi05_long_2048.log\"}}, \"precompute-pi05-object-2048-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:18:24.705Z\", \"updated_at\": \"2026-05-24T06:23:31.677Z\", \"hypothesis\": \"Precomputing π0.5 obs_features and K=2048 action samples on LIBERO-Object enables downstream CRM training for cross-model (SmolVLA→π0.5) generalization verification without re-running inference at train time.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 nohup python -u src/train_crm.py --precompute --model pi05 --benchmark object --K 10 --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/ > /root/autodl-tmp/logs/precompute_pi05_object_2048.log 2>&1 &\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": 113456, \"data_path\": \"/root/autodl-tmp/crm_cache_pi05_2048/object/\", \"data_count\": 72507, \"model_name\": \"pi0.5\", \"seed\": 0, \"log_path\": \"/root/autodl-tmp/logs/precompute_pi05_object_2048.log\"}}}, \"count\": 23, \"total\": 23, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.5167}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "df9060b8-a5ff-441d-bb94-0ca6b735abe6",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"eval-supp-long-k2mean-s46\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T03:23:24.189Z\\\", \\\"updated_at\\\": \\\"2026-05-24T08:15:23.138Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --benchmark long --mode vla_only --baseline_mode mean --K 2 --seed 46 --n_rollouts 20 --output_file logs/eval_long_k2mean_seed46.json\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"pid\\\": 263191, \\\"log_path\\\": \\\"logs/eval_long_k2mean_seed46.json\\\", \\\"submitted_at\\\": \\\"2026-05-24T03:23:22.142Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"LIBERO-Long\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 46, \\\"eval_data\\\": \\\"LIBERO-Long\\\", \\\"checkpoint_source\\\": \\\"n/a-baseline\\\"}, \\\"hypothesis\\\": \\\"VLA-only K=2 mean baseline on LIBERO-Long suite seed46 provides the fifth seed for Long K2-mean variance analysis, establishing the unrefined baseline performance across seeds.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.55, \\\"successes\\\": 110, \\\"total\\\": 200, \\\"source\\\": \\\"json_harvest_bjb1-32546\\\"}}, \\\"eval-supp-long-crm-norm005-s46\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T00:55:34.833Z\\\", \\\"updated_at\\\": \\\"2026-05-24T08:15:19.358Z\\\", \\\"hypothesis\\\": \\\"CRM obs-only refinement with max_correction_norm=0.05 on LIBERO-Long suite seed46 provides the fifth seed for Long CRM obs-only variance analysis, testing conservative correction magnitude across seeds.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --benchmark long --mode crm_obs_only --seed 46 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": 262247, \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-supp-long-crm-norm005-s46.log\\\", \\\"submitted_at\\\": \\\"2026-05-24T03:23:09.570Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"LIBERO-Long\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 46, \\\"eval_data\\\": \\\"LIBERO-Long\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.54, \\\"successes\\\": 108, \\\"total\\\": 200, \\\"source\\\": \\\"json_harvest_bjb1-32546\\\"}}, \\\"eval-supp-long-reconvla-s46\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T00:55:40.981Z\\\", \\\"updated_at\\\": \\\"2026-05-24T08:06:46.631Z\\\", \\\"hypothesis\\\": \\\"ReconVLA evaluation on LIBERO-Long suite seed46 provides the fifth seed for Long ReconVLA variance analysis, measuring reconstruction-based refinement consistency across seeds.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --benchmark long --mode reconvla --seed 46 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"pid\\\": 262529, \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-supp-long-reconvla-s46.log\\\", \\\"submitted_at\\\": \\\"2026-05-24T03:23:15.265Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"LIBERO-Long\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 46, \\\"eval_data\\\": \\\"LIBERO-Long\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.56, \\\"successes\\\": 112, \\\"total\\\": 200, \\\"source\\\": \\\"json_harvest_bjb1-32546\\\"}}, \\\"eval-supp-k2mean-spatial-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T07:15:55.833Z\\\", \\\"updated_at\\\": \\\"2026-05-24T07:18:30.230Z\\\", \\\"hypothesis\\\": \\\"K=2 mean baseline on Spatial suite seed47. Sixth seed extending variance analysis. 5-seed mean ~80%.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark spatial --mode vla_only --baseline_mode mean --K 2 --seed 47 --n_rollouts 20\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"tmux_session\\\": \\\"spatial-k2mean-s47\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 47, \\\"eval_data\\\": \\\"LIBERO-Spatial 10 tasks x 20 rollouts\\\", \\\"checkpoint_source\\\": \\\"n/a-baseline\\\"}}, \\\"eval-supp-reconvla-spatial-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T07:15:47.910Z\\\", \\\"updated_at\\\": \\\"2026-05-24T07:18:23.847Z\\\", \\\"hypothesis\\\": \\\"Reconvla K=10 on Spatial suite seed47. Sixth seed extending variance analysis. 5-seed mean ~80%.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark spatial --mode reconvla --seed 47 --n_rollouts 20 --K 10\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"tmux_session\\\": \\\"spatial-reconvla-s47\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA+Reconvla\\\", \\\"seed\\\": 47, \\\"eval_data\\\": \\\"LIBERO-Spatial 10 tasks x 20 rollouts\\\", \\\"checkpoint_source\\\": \\\"n/a-reconvla\\\"}}, \\\"eval-supp-adapt-tau025-spatial-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T07:15:43.884Z\\\", \\\"updated_at\\\": \\\"2026-05-24T07:18:17.441Z\\\", \\\"hypothesis\\\": \\\"Adaptive CRM tau=0.25 on Spatial suite seed47. Sixth seed extending variance analysis. 5-seed mean ~80.5%.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark spatial --mode adaptive_conformal_crm --seed 47 --n_rollouts 20 --K 10 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"tmux_session\\\": \\\"spatial-adapt-s47\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA+Adaptive CRM\\\", \\\"seed\\\": 47, \\\"eval_data\\\": \\\"LIBERO-Spatial 10 tasks x 20 rollouts\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\"}}, \\\"eval-supp-vla-only-spatial-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T07:15:40.347Z\\\", \\\"updated_at\\\": \\\"2026-05-24T07:18:10.979Z\\\", \\\"hypothesis\\\": \\\"VLA-only baseline on Spatial suite seed47. Sixth seed extending variance analysis. 5-seed mean ~78.7%.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode vla_only --seed 47 --n_rollouts 20 --K 1\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"tmux_session\\\": \\\"spatial-vla-s47\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 47, \\\"eval_data\\\": \\\"LIBERO-Spatial 10 tasks x 20 rollouts\\\", \\\"checkpoint_source\\\": \\\"n/a-baseline\\\"}}, \\\"eval-supp-goal-vla-only-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T07:14:14.567Z\\\", \\\"updated_at\\\": \\\"2026-05-24T07:17:13.996Z\\\", \\\"hypothesis\\\": \\\"Goal s47 VLA-only (K=1) baseline to extend Goal seed coverage beyond s42-s46 for supplementary variance analysis.\\\", \\\"parent\\\": \\\"eval-supp-goal-vla-only-s46\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark goal --mode vla_only --seed 47 --n_rollouts 20 --K 1\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"pid\\\": 279117, \\\"tmux_session\\\": \\\"goal-vla-s47\\\", \\\"log_path\\\": \\\"logs/eval-supp-goal-vla-only-s47.log\\\", \\\"data_path\\\": \\\"LIBERO-Goal\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 47, \\\"eval_data\\\": \\\"LIBERO-Goal\\\", \\\"checkpoint_source\\\": \\\"n/a-baseline\\\", \\\"checkpoint_path\\\": \\\"n/a-eval-only\\\"}}, \\\"eval-supp-long-vla-only-s47-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T07:14:04.522Z\\\", \\\"updated_at\\\": \\\"2026-05-24T07:17:06.584Z\\\", \\\"hypothesis\\\": \\\"Long s47 VLA-only (K=1) baseline to complete the Long s47 seed extension set. The existing eval-supp-long-vla-only-s47 is actually k2mean (K=2 mean), so this fills the true VLA-only gap.\\\", \\\"parent\\\": \\\"eval-supp-long-vla-only-s46\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark long --mode vla_only --seed 47 --n_rollouts 20 --K 1\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": 278846, \\\"tmux_session\\\": \\\"long-vla-s47-r2\\\", \\\"log_path\\\": \\\"logs/eval-supp-long-vla-only-s47-r2.log\\\", \\\"data_path\\\": \\\"LIBERO-Long\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 47, \\\"eval_data\\\": \\\"LIBERO-Long\\\", \\\"checkpoint_source\\\": \\\"n/a-baseline\\\", \\\"checkpoint_path\\\": \\\"n/a-eval-only\\\"}}, \\\"eval-supp-adapt-tau025-spatial-s46\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T07:12:18.821Z\\\", \\\"updated_at\\\": \\\"2026-05-24T07:16:50.821Z\\\", \\\"hypothesis\\\": \\\"CRM/Adaptive on Spatial seed46, 5th seed extension\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark spatial --mode adaptive_conformal_crm --seed 46 --n_rollouts 20 --K 10 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"LIBERO spatial suite\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA + Adaptive CRM (crm_smolvla_3suite_v1)\\\", \\\"seed\\\": 46, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO spatial 10 tasks x 20 rollouts\\\"}, \\\"failure_reason\\\": \\\"GPU 1 occupied by OpenVLA VLA-only eval (PID 114990). Not actually started despite RUNNING status. Will deploy when GPU frees up.\\\"}, \\\"eval-supp-crm-norm005-spatial-s46\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T07:12:15.210Z\\\", \\\"updated_at\\\": \\\"2026-05-24T07:14:47.458Z\\\", \\\"hypothesis\\\": \\\"CRM/Adaptive on Spatial seed46, 5th seed extension\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 46 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"LIBERO spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"smolvla+crm_smolvla_3suite_v1\\\", \\\"seed\\\": 46, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO spatial 10 tasks x 20 rollouts\\\"}}, \\\"eval-openvla-object-vla-only-seed42-v3\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T07:07:37.003Z\\\", \\\"updated_at\\\": \\\"2026-05-24T07:08:07.984Z\\\", \\\"hypothesis\\\": \\\"After fixing OpenVLA loading for transformers 5.8.1 (model_type 'openvla' auto-registration via openvla_compat + PrismaticImageProcessor workaround), VLA-only baseline on LIBERO-Object seed42 should reproduce the previously observed ~69% success rate from eval-openvla-object-vla-only-seed42-v2. Validates that the new loader path preserves model behavior bit-for-bit.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u src/openvla_eval.py --benchmark object --model_path /root/autodl-tmp/models/openvla-libero-object --mode vla_only --seed 42 --n_rollouts 20 --gpu 0 --output_file logs/eval_openvla_object_vla_only_seed42_v3.json\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/libero_data/libero_object\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"openvla-libero-object\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/models/openvla-libero-object\\\", \\\"eval_data\\\": \\\"LIBERO-Object (10 tasks x 20 rollouts = 200 episodes)\\\", \\\"pid\\\": \\\"114984\\\", \\\"log_path\\\": \\\"/tmp/eval_openvla_vla_only_seed42_v3.log\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/models/openvla-libero-object\\\"}}, \\\"eval-supp-long-vla-only-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T06:34:23.532Z\\\", \\\"updated_at\\\": \\\"2026-05-24T07:05:36.964Z\\\", \\\"hypothesis\\\": \\\"K=2 mean baseline on Long suite seed47 (NOT VLA-only — actual command uses --baseline_mode mean --K 2, output eval_long_k2mean_seed47.json). Misnamed at creation. Paired with Adapt-s47 for matched-seed comparison.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark long --mode vla_only --baseline_mode mean --K 2 --seed 47 --n_rollouts 20 --output_file logs/eval_long_k2mean_seed47.json\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"gpu\\\": [\\\"cuda:5\\\"], \\\"tmux_session\\\": \\\"long-vla-s47\\\", \\\"log_path\\\": \\\"logs/eval-supp-long-vla-only-s47.log\\\", \\\"data_path\\\": \\\"LIBERO-Long\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 47, \\\"eval_data\\\": \\\"LIBERO-Long\\\", \\\"checkpoint_source\\\": \\\"n/a-baseline\\\", \\\"parent\\\": \\\"eval-supp-long-vla-only-s46\\\"}}, \\\"eval-supp-long-crm-norm005-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T06:52:08.968Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:53:16.695Z\\\", \\\"hypothesis\\\": \\\"CRM obs-only norm=0.05 on Long suite seed47 (sixth seed extension). Pairs with running Long vla-only-s47 and adapt-s47 on cqa1-32758 to tighten Long suite CI which has highest variance.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark long --mode crm_obs_only --seed 47 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:5\\\"], \\\"tmux_session\\\": \\\"long-crm-s47\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-supp-long-crm-norm005-s47.log\\\", \\\"data_path\\\": \\\"LIBERO-Long\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 47, \\\"eval_data\\\": \\\"LIBERO-Long\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\\\"}}, \\\"eval-supp-long-reconvla-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T06:52:05.630Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:53:02.593Z\\\", \\\"hypothesis\\\": \\\"Reconvla K=10 on Long suite seed47 (sixth seed extension). Pairs with running Long vla-only-s47 and adapt-s47 on cqa1-32758 to tighten Long suite CI which has highest variance.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark long --mode reconvla --seed 47 --n_rollouts 20 --K 10\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:4\\\"], \\\"tmux_session\\\": \\\"long-reconvla-s47\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-supp-long-reconvla-s47.log\\\", \\\"data_path\\\": \\\"LIBERO-Long\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 47, \\\"eval_data\\\": \\\"LIBERO-Long\\\", \\\"checkpoint_source\\\": \\\"n/a-reconvla\\\"}}, \\\"eval-supp-spatial-crm-norm005-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T06:49:40.206Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:51:27.049Z\\\", \\\"hypothesis\\\": \\\"CRM obs_only norm=0.05 on LIBERO-Spatial seed47. Fifth seed extending Spatial CRM coverage (s43-s46 mean ~79.6%). Tightens CI for statistical comparison with VLA-only/K2mean/Reconvla/Adaptive at matched 5-seed coverage.\\\", \\\"parent\\\": \\\"eval-supp-spatial-crm-norm005-s46\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 47 --n_rollouts 20 --max_correction_norm 0.05 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_spatial_crm_obs_only_norm0.05_seed47.json\\\", \\\"server\\\": \\\"bjb2-40593\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"235730\\\", \\\"tmux_session\\\": \\\"eval-spatial-crm-s47\\\", \\\"log_path\\\": \\\"/tmp/eval_spatial_crm_s47.log\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA+CRM\\\", \\\"seed\\\": 47, \\\"eval_data\\\": \\\"LIBERO-Spatial\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"checkpoint_path\\\": \\\"n/a-eval-only\\\", \\\"submitted_at\\\": \\\"2026-05-24T06:50:07Z\\\", \\\"submitted_via\\\": \\\"ssh_execute_tmux\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}}, \\\"eval-supp-vla-only-spatial-s46\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T06:48:57.955Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:50:52.276Z\\\", \\\"hypothesis\\\": \\\"VLA-only baseline on Spatial suite seed46. Extending from 3-seed (s42/s43/s44) to 5-seed for variance analysis. 3-seed mean 78.7%±0.3%.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark spatial --mode vla_only --seed 46 --n_rollouts 20 --K 1\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 46, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/models/smolvla_libero/\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial 10 tasks x 20 rollouts\\\", \\\"benchmark\\\": \\\"spatial\\\", \\\"mode\\\": \\\"vla_only\\\", \\\"tmux_session\\\": \\\"eval-supp-vla-only-spatial-s46\\\", \\\"gpu\\\": 5}}, \\\"eval-supp-adapt-tau025-spatial-s45\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T06:48:54.415Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:50:44.120Z\\\", \\\"hypothesis\\\": \\\"Adaptive CRM tau=0.25 (conformal_threshold) with max_correction_norm=0.2 on Spatial suite seed45. Extending from 3-seed (s42/s43/s44) to 5-seed for variance analysis. 3-seed mean 80.8%±1.1%.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark spatial --mode adaptive_conformal_crm --seed 45 --n_rollouts 20 --K 10 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"smolvla+crm-adaptive\\\", \\\"seed\\\": 45, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial 10 tasks x 20 rollouts\\\", \\\"benchmark\\\": \\\"spatial\\\", \\\"mode\\\": \\\"adaptive_conformal_crm\\\", \\\"max_correction_norm\\\": 0.2, \\\"conformal_threshold\\\": 0.25, \\\"K\\\": 10, \\\"tmux_session\\\": \\\"eval-supp-adapt-tau025-spatial-s45\\\", \\\"gpu\\\": 4}}, \\\"eval-supp-crm-norm005-spatial-s45\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T06:48:50.955Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:50:37.107Z\\\", \\\"hypothesis\\\": \\\"CRM always-on norm=0.05 on Spatial suite seed45. Extending from 3-seed (s42/s43/s44) to 5-seed for variance analysis. 3-seed mean 79.8%±1.3%.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 45 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"smolvla+crm\\\", \\\"seed\\\": 45, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial 10 tasks x 20 rollouts\\\", \\\"benchmark\\\": \\\"spatial\\\", \\\"mode\\\": \\\"crm_obs_only\\\", \\\"max_correction_norm\\\": 0.05, \\\"K\\\": 10, \\\"tmux_session\\\": \\\"eval-supp-crm-norm005-spatial-s45\\\", \\\"gpu\\\": 3}}, \\\"eval-supp-vla-only-spatial-s45\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T06:48:46.040Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:50:30.794Z\\\", \\\"hypothesis\\\": \\\"VLA-only baseline on Spatial suite seed45. Extending from 3-seed (s42/s43/s44) to 5-seed for variance analysis. 3-seed mean 78.7%±0.3%.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark spatial --mode vla_only --seed 45 --n_rollouts 20 --K 1\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 45, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/models/smolvla_libero/\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial 10 tasks x 20 rollouts\\\", \\\"benchmark\\\": \\\"spatial\\\", \\\"mode\\\": \\\"vla_only\\\", \\\"tmux_session\\\": \\\"eval-supp-vla-only-spatial-s45\\\", \\\"gpu\\\": 2}}, \\\"eval-supp-long-adapt-tau025-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T06:34:20.287Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:38:39.651Z\\\", \\\"hypothesis\\\": \\\"Adaptive CRM tau=0.25 on Long suite seed47 (sixth seed extension). Long is the highest-variance suite with smallest improvement margin (57.7 vs 58.0 VLA-only). Sixth seed tightens CI to determine if Adaptive is statistically equivalent to or below VLA-only on Long.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark long --mode adaptive_conformal_crm --seed 47 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --max_correction_norm 0.2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"gpu\\\": [\\\"cuda:4\\\"], \\\"tmux_session\\\": \\\"long-adapt-s47\\\", \\\"log_path\\\": \\\"logs/eval-supp-long-adapt-tau025-s47.log\\\", \\\"data_path\\\": \\\"LIBERO-Long\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 47, \\\"eval_data\\\": \\\"LIBERO-Long\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\\\", \\\"parent\\\": \\\"eval-supp-long-adapt-tau025-s46-r2\\\"}}, \\\"precompute-pi05-long-2048-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T06:18:31.140Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:23:39.262Z\\\", \\\"hypothesis\\\": \\\"Precomputing π0.5 obs_features and K=2048 action samples on LIBERO-Long enables downstream CRM training for cross-model (SmolVLA→π0.5) generalization verification without re-running inference at train time.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=3 nohup python -u src/train_crm.py --precompute --model pi05 --benchmark long --K 10 --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/ > /root/autodl-tmp/logs/precompute_pi05_long_2048.log 2>&1 &\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"pid\\\": 114507, \\\"data_path\\\": \\\"/root/autodl-tmp/crm_cache_pi05_2048/long/\\\", \\\"data_count\\\": 136090, \\\"model_name\\\": \\\"pi0.5\\\", \\\"seed\\\": 0, \\\"log_path\\\": \\\"/root/autodl-tmp/logs/precompute_pi05_long_2048.log\\\"}}, \\\"precompute-pi05-object-2048-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T06:18:24.705Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:23:31.677Z\\\", \\\"hypothesis\\\": \\\"Precomputing π0.5 obs_features and K=2048 action samples on LIBERO-Object enables downstream CRM training for cross-model (SmolVLA→π0.5) generalization verification without re-running inference at train time.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 nohup python -u src/train_crm.py --precompute --model pi05 --benchmark object --K 10 --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/ > /root/autodl-tmp/logs/precompute_pi05_object_2048.log 2>&1 &\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": 113456, \\\"data_path\\\": \\\"/root/autodl-tmp/crm_cache_pi05_2048/object/\\\", \\\"data_count\\\": 72507, \\\"model_name\\\": \\\"pi0.5\\\", \\\"seed\\\": 0, \\\"log_path\\\": \\\"/root/autodl-tmp/logs/precompute_pi05_object_2048.log\\\"}}}, \\\"count\\\": 23, \\\"total\\\": 23, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 3.5167}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval-supp-long-k2mean-s46\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T03:23:24.189Z\", \"updated_at\": \"2026-05-24T08:15:23.138Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark long --mode vla_only --baseline_mode mean --K 2 --seed 46 --n_rollouts 20 --output_file logs/eval_long_k2mean_seed46.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": 263191, \"log_path\": \"logs/eval_long_k2mean_seed46.json\", \"submitted_at\": \"2026-05-24T03:23:22.142Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 46, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"n/a-baseline\"}, \"hypothesis\": \"VLA-only K=2 mean baseline on LIBERO-Long suite seed46 provides the fifth seed for Long K2-mean variance analysis, establishing the unrefined baseline performance across seeds.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.55, \"successes\": 110, \"total\": 200, \"source\": \"json_harvest_bjb1-32546\"}}, \"eval-supp-long-crm-norm005-s46\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T00:55:34.833Z\", \"updated_at\": \"2026-05-24T08:15:19.358Z\", \"hypothesis\": \"CRM obs-only refinement with max_correction_norm=0.05 on LIBERO-Long suite seed46 provides the fifth seed for Long CRM obs-only variance analysis, testing conservative correction magnitude across seeds.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark long --mode crm_obs_only --seed 46 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": 262247, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-crm-norm005-s46.log\", \"submitted_at\": \"2026-05-24T03:23:09.570Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 46, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.54, \"successes\": 108, \"total\": 200, \"source\": \"json_harvest_bjb1-32546\"}}, \"eval-supp-long-reconvla-s46\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T00:55:40.981Z\", \"updated_at\": \"2026-05-24T08:06:46.631Z\", \"hypothesis\": \"ReconVLA evaluation on LIBERO-Long suite seed46 provides the fifth seed for Long ReconVLA variance analysis, measuring reconstruction-based refinement consistency across seeds.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark long --mode reconvla --seed 46 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": 262529, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-reconvla-s46.log\", \"submitted_at\": \"2026-05-24T03:23:15.265Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 46, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.56, \"successes\": 112, \"total\": 200, \"source\": \"json_harvest_bjb1-32546\"}}, \"eval-supp-k2mean-spatial-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:15:55.833Z\", \"updated_at\": \"2026-05-24T07:18:30.230Z\", \"hypothesis\": \"K=2 mean baseline on Spatial suite seed47. Sixth seed extending variance analysis. 5-seed mean ~80%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark spatial --mode vla_only --baseline_mode mean --K 2 --seed 47 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:3\"], \"tmux_session\": \"spatial-k2mean-s47\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"checkpoint_source\": \"n/a-baseline\"}}, \"eval-supp-reconvla-spatial-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:15:47.910Z\", \"updated_at\": \"2026-05-24T07:18:23.847Z\", \"hypothesis\": \"Reconvla K=10 on Spatial suite seed47. Sixth seed extending variance analysis. 5-seed mean ~80%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark spatial --mode reconvla --seed 47 --n_rollouts 20 --K 10\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:2\"], \"tmux_session\": \"spatial-reconvla-s47\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA+Reconvla\", \"seed\": 47, \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"checkpoint_source\": \"n/a-reconvla\"}}, \"eval-supp-adapt-tau025-spatial-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:15:43.884Z\", \"updated_at\": \"2026-05-24T07:18:17.441Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Spatial suite seed47. Sixth seed extending variance analysis. 5-seed mean ~80.5%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark spatial --mode adaptive_conformal_crm --seed 47 --n_rollouts 20 --K 10 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:1\"], \"tmux_session\": \"spatial-adapt-s47\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA+Adaptive CRM\", \"seed\": 47, \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\"}}, \"eval-supp-vla-only-spatial-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:15:40.347Z\", \"updated_at\": \"2026-05-24T07:18:10.979Z\", \"hypothesis\": \"VLA-only baseline on Spatial suite seed47. Sixth seed extending variance analysis. 5-seed mean ~78.7%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode vla_only --seed 47 --n_rollouts 20 --K 1\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:0\"], \"tmux_session\": \"spatial-vla-s47\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"checkpoint_source\": \"n/a-baseline\"}}, \"eval-supp-goal-vla-only-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:14:14.567Z\", \"updated_at\": \"2026-05-24T07:17:13.996Z\", \"hypothesis\": \"Goal s47 VLA-only (K=1) baseline to extend Goal seed coverage beyond s42-s46 for supplementary variance analysis.\", \"parent\": \"eval-supp-goal-vla-only-s46\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark goal --mode vla_only --seed 47 --n_rollouts 20 --K 1\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": 279117, \"tmux_session\": \"goal-vla-s47\", \"log_path\": \"logs/eval-supp-goal-vla-only-s47.log\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Goal\", \"checkpoint_source\": \"n/a-baseline\", \"checkpoint_path\": \"n/a-eval-only\"}}, \"eval-supp-long-vla-only-s47-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:14:04.522Z\", \"updated_at\": \"2026-05-24T07:17:06.584Z\", \"hypothesis\": \"Long s47 VLA-only (K=1) baseline to complete the Long s47 seed extension set. The existing eval-supp-long-vla-only-s47 is actually k2mean (K=2 mean), so this fills the true VLA-only gap.\", \"parent\": \"eval-supp-long-vla-only-s46\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark long --mode vla_only --seed 47 --n_rollouts 20 --K 1\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": 278846, \"tmux_session\": \"long-vla-s47-r2\", \"log_path\": \"logs/eval-supp-long-vla-only-s47-r2.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"n/a-baseline\", \"checkpoint_path\": \"n/a-eval-only\"}}, \"eval-supp-adapt-tau025-spatial-s46\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:12:18.821Z\", \"updated_at\": \"2026-05-24T07:16:50.821Z\", \"hypothesis\": \"CRM/Adaptive on Spatial seed46, 5th seed extension\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark spatial --mode adaptive_conformal_crm --seed 46 --n_rollouts 20 --K 10 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO spatial suite\", \"data_count\": 200, \"model_name\": \"SmolVLA + Adaptive CRM (crm_smolvla_3suite_v1)\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 20 rollouts\"}, \"failure_reason\": \"GPU 1 occupied by OpenVLA VLA-only eval (PID 114990). Not actually started despite RUNNING status. Will deploy when GPU frees up.\"}, \"eval-supp-crm-norm005-spatial-s46\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:12:15.210Z\", \"updated_at\": \"2026-05-24T07:14:47.458Z\", \"hypothesis\": \"CRM/Adaptive on Spatial seed46, 5th seed extension\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 46 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO spatial\", \"data_count\": 200, \"model_name\": \"smolvla+crm_smolvla_3suite_v1\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 20 rollouts\"}}, \"eval-openvla-object-vla-only-seed42-v3\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:07:37.003Z\", \"updated_at\": \"2026-05-24T07:08:07.984Z\", \"hypothesis\": \"After fixing OpenVLA loading for transformers 5.8.1 (model_type 'openvla' auto-registration via openvla_compat + PrismaticImageProcessor workaround), VLA-only baseline on LIBERO-Object seed42 should reproduce the previously observed ~69% success rate from eval-openvla-object-vla-only-seed42-v2. Validates that the new loader path preserves model behavior bit-for-bit.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u src/openvla_eval.py --benchmark object --model_path /root/autodl-tmp/models/openvla-libero-object --mode vla_only --seed 42 --n_rollouts 20 --gpu 0 --output_file logs/eval_openvla_object_vla_only_seed42_v3.json\", \"server\": \"bjb2-28827\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_object\", \"data_count\": 200, \"model_name\": \"openvla-libero-object\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/openvla-libero-object\", \"eval_data\": \"LIBERO-Object (10 tasks x 20 rollouts = 200 episodes)\", \"pid\": \"114984\", \"log_path\": \"/tmp/eval_openvla_vla_only_seed42_v3.log\", \"checkpoint_path\": \"/root/autodl-tmp/models/openvla-libero-object\"}}, \"eval-supp-long-vla-only-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:34:23.532Z\", \"updated_at\": \"2026-05-24T07:05:36.964Z\", \"hypothesis\": \"K=2 mean baseline on Long suite seed47 (NOT VLA-only — actual command uses --baseline_mode mean --K 2, output eval_long_k2mean_seed47.json). Misnamed at creation. Paired with Adapt-s47 for matched-seed comparison.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark long --mode vla_only --baseline_mode mean --K 2 --seed 47 --n_rollouts 20 --output_file logs/eval_long_k2mean_seed47.json\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:5\"], \"tmux_session\": \"long-vla-s47\", \"log_path\": \"logs/eval-supp-long-vla-only-s47.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"n/a-baseline\", \"parent\": \"eval-supp-long-vla-only-s46\"}}, \"eval-supp-long-crm-norm005-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:52:08.968Z\", \"updated_at\": \"2026-05-24T06:53:16.695Z\", \"hypothesis\": \"CRM obs-only norm=0.05 on Long suite seed47 (sixth seed extension). Pairs with running Long vla-only-s47 and adapt-s47 on cqa1-32758 to tighten Long suite CI which has highest variance.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark long --mode crm_obs_only --seed 47 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"tmux_session\": \"long-crm-s47\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-crm-norm005-s47.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\"}}, \"eval-supp-long-reconvla-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:52:05.630Z\", \"updated_at\": \"2026-05-24T06:53:02.593Z\", \"hypothesis\": \"Reconvla K=10 on Long suite seed47 (sixth seed extension). Pairs with running Long vla-only-s47 and adapt-s47 on cqa1-32758 to tighten Long suite CI which has highest variance.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark long --mode reconvla --seed 47 --n_rollouts 20 --K 10\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"tmux_session\": \"long-reconvla-s47\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-reconvla-s47.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"n/a-reconvla\"}}, \"eval-supp-spatial-crm-norm005-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:49:40.206Z\", \"updated_at\": \"2026-05-24T06:51:27.049Z\", \"hypothesis\": \"CRM obs_only norm=0.05 on LIBERO-Spatial seed47. Fifth seed extending Spatial CRM coverage (s43-s46 mean ~79.6%). Tightens CI for statistical comparison with VLA-only/K2mean/Reconvla/Adaptive at matched 5-seed coverage.\", \"parent\": \"eval-supp-spatial-crm-norm005-s46\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 47 --n_rollouts 20 --max_correction_norm 0.05 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_spatial_crm_obs_only_norm0.05_seed47.json\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"235730\", \"tmux_session\": \"eval-spatial-crm-s47\", \"log_path\": \"/tmp/eval_spatial_crm_s47.log\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA+CRM\", \"seed\": 47, \"eval_data\": \"LIBERO-Spatial\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"checkpoint_path\": \"n/a-eval-only\", \"submitted_at\": \"2026-05-24T06:50:07Z\", \"submitted_via\": \"ssh_execute_tmux\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-supp-vla-only-spatial-s46\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:48:57.955Z\", \"updated_at\": \"2026-05-24T06:50:52.276Z\", \"hypothesis\": \"VLA-only baseline on Spatial suite seed46. Extending from 3-seed (s42/s43/s44) to 5-seed for variance analysis. 3-seed mean 78.7%±0.3%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark spatial --mode vla_only --seed 46 --n_rollouts 20 --K 1\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/models/smolvla_libero/\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"benchmark\": \"spatial\", \"mode\": \"vla_only\", \"tmux_session\": \"eval-supp-vla-only-spatial-s46\", \"gpu\": 5}}, \"eval-supp-adapt-tau025-spatial-s45\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:48:54.415Z\", \"updated_at\": \"2026-05-24T06:50:44.120Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 (conformal_threshold) with max_correction_norm=0.2 on Spatial suite seed45. Extending from 3-seed (s42/s43/s44) to 5-seed for variance analysis. 3-seed mean 80.8%±1.1%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark spatial --mode adaptive_conformal_crm --seed 45 --n_rollouts 20 --K 10 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla+crm-adaptive\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"benchmark\": \"spatial\", \"mode\": \"adaptive_conformal_crm\", \"max_correction_norm\": 0.2, \"conformal_threshold\": 0.25, \"K\": 10, \"tmux_session\": \"eval-supp-adapt-tau025-spatial-s45\", \"gpu\": 4}}, \"eval-supp-crm-norm005-spatial-s45\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:48:50.955Z\", \"updated_at\": \"2026-05-24T06:50:37.107Z\", \"hypothesis\": \"CRM always-on norm=0.05 on Spatial suite seed45. Extending from 3-seed (s42/s43/s44) to 5-seed for variance analysis. 3-seed mean 79.8%±1.3%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 45 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla+crm\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"benchmark\": \"spatial\", \"mode\": \"crm_obs_only\", \"max_correction_norm\": 0.05, \"K\": 10, \"tmux_session\": \"eval-supp-crm-norm005-spatial-s45\", \"gpu\": 3}}, \"eval-supp-vla-only-spatial-s45\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:48:46.040Z\", \"updated_at\": \"2026-05-24T06:50:30.794Z\", \"hypothesis\": \"VLA-only baseline on Spatial suite seed45. Extending from 3-seed (s42/s43/s44) to 5-seed for variance analysis. 3-seed mean 78.7%±0.3%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark spatial --mode vla_only --seed 45 --n_rollouts 20 --K 1\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/models/smolvla_libero/\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"benchmark\": \"spatial\", \"mode\": \"vla_only\", \"tmux_session\": \"eval-supp-vla-only-spatial-s45\", \"gpu\": 2}}, \"eval-supp-long-adapt-tau025-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:34:20.287Z\", \"updated_at\": \"2026-05-24T06:38:39.651Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Long suite seed47 (sixth seed extension). Long is the highest-variance suite with smallest improvement margin (57.7 vs 58.0 VLA-only). Sixth seed tightens CI to determine if Adaptive is statistically equivalent to or below VLA-only on Long.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark long --mode adaptive_conformal_crm --seed 47 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --max_correction_norm 0.2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:4\"], \"tmux_session\": \"long-adapt-s47\", \"log_path\": \"logs/eval-supp-long-adapt-tau025-s47.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"parent\": \"eval-supp-long-adapt-tau025-s46-r2\"}}, \"precompute-pi05-long-2048-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:18:31.140Z\", \"updated_at\": \"2026-05-24T06:23:39.262Z\", \"hypothesis\": \"Precomputing π0.5 obs_features and K=2048 action samples on LIBERO-Long enables downstream CRM training for cross-model (SmolVLA→π0.5) generalization verification without re-running inference at train time.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 nohup python -u src/train_crm.py --precompute --model pi05 --benchmark long --K 10 --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/ > /root/autodl-tmp/logs/precompute_pi05_long_2048.log 2>&1 &\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": 114507, \"data_path\": \"/root/autodl-tmp/crm_cache_pi05_2048/long/\", \"data_count\": 136090, \"model_name\": \"pi0.5\", \"seed\": 0, \"log_path\": \"/root/autodl-tmp/logs/precompute_pi05_long_2048.log\"}}, \"precompute-pi05-object-2048-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:18:24.705Z\", \"updated_at\": \"2026-05-24T06:23:31.677Z\", \"hypothesis\": \"Precomputing π0.5 obs_features and K=2048 action samples on LIBERO-Object enables downstream CRM training for cross-model (SmolVLA→π0.5) generalization verification without re-running inference at train time.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 nohup python -u src/train_crm.py --precompute --model pi05 --benchmark object --K 10 --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/ > /root/autodl-tmp/logs/precompute_pi05_object_2048.log 2>&1 &\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": 113456, \"data_path\": \"/root/autodl-tmp/crm_cache_pi05_2048/object/\", \"data_count\": 72507, \"model_name\": \"pi0.5\", \"seed\": 0, \"log_path\": \"/root/autodl-tmp/logs/precompute_pi05_object_2048.log\"}}}, \"count\": 23, \"total\": 23, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.5167}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-24T08:24:24.439Z_

<details><summary>↩ Tool result · `toolu_01Eu9ocUpcX8Rqgo2pW2APws`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \" 96831 Rl+     01:33:12 python -u src/evaluate.py --benchmark spatial --mode vla_only --seed 45 --n_rollouts 20 --K 1\\n 97070 Rl+     01:33:09 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 45 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\n 97307 Rl+     01:33:06 python -u src/evaluate.py --benchmark spatial --mode adaptive_conformal_crm --seed 45 --n_rollouts 20 --K 10 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\n 97550 Rl+     01:33:03 python -u src/evaluate.py --benchmark spatial --mode vla_only --seed 46 --n_rollouts 20 --K 1\\n121241 Rl+     01:09:38 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 46 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.81}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "35bae832-faee-4cda-83d2-dfbaae4634cd",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\" 96831 Rl+     01:33:12 python -u src/evaluate.py --benchmark spatial --mode vla_only --seed 45 --n_rollouts 20 --K 1\\\\n 97070 Rl+     01:33:09 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 45 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\\n 97307 Rl+     01:33:06 python -u src/evaluate.py --benchmark spatial --mode adaptive_conformal_crm --seed 45 --n_rollouts 20 --K 10 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\\n 97550 Rl+     01:33:03 python -u src/evaluate.py --benchmark spatial --mode vla_only --seed 46 --n_rollouts 20 --K 1\\\\n121241 Rl+     01:09:38 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 46 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.81}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \" 96831 Rl+     01:33:12 python -u src/evaluate.py --benchmark spatial --mode vla_only --seed 45 --n_rollouts 20 --K 1\\n 97070 Rl+     01:33:09 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 45 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\n 97307 Rl+     01:33:06 python -u src/evaluate.py --benchmark spatial --mode adaptive_conformal_crm --seed 45 --n_rollouts 20 --K 10 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\n 97550 Rl+     01:33:03 python -u src/evaluate.py --benchmark spatial --mode vla_only --seed 46 --n_rollouts 20 --K 1\\n121241 Rl+     01:09:38 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 46 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.81}}"
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
OK, so:

1. The two stale lerobot experiments (eval-smolvla-lerobot-goal-seed43-v3 and eval-smolvla-lerobot-spatial-seed43-v3) are NOT in the RUNNING experiments list. They must have been updated already or I need to search for them specifically. Let me search for them by name.

2. bjb2-28827: All 5 PIDs are still running. Let me check their progress via tmux logs.

Let me first search for the two lerobot experiments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "dc3de402-eac7-4641-a98f-f1699a4e2d09",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q3mGMYNec71YvtdjPx2sQt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10303,
      "cache_read_input_tokens": 25024,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10303
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

两个 lerobot 实验不在 RUNNING 列表中，bjb2-28827 上 5 个进程全部存活。让我查找 lerobot 实验并获取 bjb2-28827 进度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "53afa8c0-300a-485f-99e8-f4222f46c6b1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q3mGMYNec71YvtdjPx2sQt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10303,
      "cache_read_input_tokens": 25024,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10303
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01REzrJS2Td6L8t8s3TzXgdV`</summary>

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
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "8f3b431f-cf18-4523-956d-c526e684ba40",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q3mGMYNec71YvtdjPx2sQt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10303,
      "cache_read_input_tokens": 25024,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10303
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01SypNHRQ9nTa5SjhDaCKc8T`</summary>

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
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "1ffe3b79-ca6f-42f4-8c17-d5f1dcd3c469",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q3mGMYNec71YvtdjPx2sQt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10303,
      "cache_read_input_tokens": 25024,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10303
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

_source line 15 · 2026-05-24T08:24:39.118Z_

<details><summary>↩ Tool result · `toolu_01REzrJS2Td6L8t8s3TzXgdV`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.511}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "1497b45d-8bfb-4d64-a6fd-1ed2783c2bcc",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 2.511}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.511}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01SyW8g7pwumP6xVbAsKvaKe`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "tail -5 /tmp/eval_crm_norm005_spatial_s46.log /tmp/eval_vla_only_spatial_s45.log /tmp/eval_crm_norm005_spatial_s45.log /tmp/eval_adapt_tau025_spatial_s45.log /tmp/eval_vla_only_spatial_s46.log 2>/dev/null",
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
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "0d3eb076-540d-4d1d-a6fa-e6da6dc93aeb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q3mGMYNec71YvtdjPx2sQt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10303,
      "cache_read_input_tokens": 25024,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10303
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

_source line 17 · 2026-05-24T08:24:42.660Z_

<details><summary>↩ Tool result · `toolu_01SypNHRQ9nTa5SjhDaCKc8T`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.5221}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "78bd0ba1-9806-42d5-bca3-905daf2d44c6",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 3.5221}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.5221}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-24T08:24:42.674Z_

<details><summary>↩ Tool result · `toolu_01SyW8g7pwumP6xVbAsKvaKe`</summary>

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
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "a044b68d-6a18-40d2-8522-cb98cfc7c7e3",
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

### Assistant

_source line 19_

<details><summary>Logged reasoning block</summary>

```text
The filter by exp_id doesn't seem to work - the registry read_registry doesn't support exp_id as a filter field. Let me try a different approach - search all experiments or use a text search. Also, my log tail command was blocked because of the `2>/dev/null` redirect. Let me fix both.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "148e2433-331a-41e6-8230-8b666284d63f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TKBLyAsg4HnpGNVw8V87SK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 955,
      "cache_read_input_tokens": 35327,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 955
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

Registry 中找不到这两个 lerobot 实验（可能已被处理或名称不同）。让我搜索所有含 "lerobot" 的实验，同时查 bjb2-28827 的 tmux 会话获取进度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "cb619ad7-10a1-40cf-928b-39b80d5a6fb1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TKBLyAsg4HnpGNVw8V87SK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 955,
      "cache_read_input_tokens": 35327,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 955
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01WqiHmZ7BaMHXXWPvNke2aU`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "fields": [
    "*"
  ],
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "bbb6e8fb-0b6a-4cf0-84d7-e00026a7d320",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TKBLyAsg4HnpGNVw8V87SK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 955,
      "cache_read_input_tokens": 35327,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 955
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

_source line 22_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01PK6vcAY4qpy8iQkAXn8K9F`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "tmux list-sessions",
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
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "fd46b095-4417-4d66-ab2e-fcf3965c087b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TKBLyAsg4HnpGNVw8V87SK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 955,
      "cache_read_input_tokens": 35327,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 955
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

_source line 23 · 2026-05-24T08:24:51.408Z_

<details><summary>↩ Tool result · `toolu_01WqiHmZ7BaMHXXWPvNke2aU`</summary>

```text
Error: result (117,004 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/4a8246d3-c96e-4959-82ff-767c57b966c8/tool-results/mcp-agent-ml-research-read_registry-1779611091392.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/4a8246d3-c96e-4959-82ff-767c57b966c8/tool-results/mcp-agent-ml-research-read_registry-1779611091392.txt in sequential chunks until 100% of the content has been read.
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
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "bdd16e89-4306-492a-93d4-13e907c5cdd0",
  "tool_use_result": {
    "content": "Error: result (117,004 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/4a8246d3-c96e-4959-82ff-767c57b966c8/tool-results/mcp-agent-ml-research-read_registry-1779611091392.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/4a8246d3-c96e-4959-82ff-767c57b966c8/tool-results/mcp-agent-ml-research-read_registry-1779611091392.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval-supp-long-k2mean-s46\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T03:23:24.189Z\", \"updated_at\": \"2026-05-24T08:15:23.138Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark long --mode vla_only --baseline_mode mean --K 2 --seed 46 --n_rollouts 20 --output_file logs/eval_long_k2mean_seed46.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": 263191, \"log_path\": \"logs/eval_long_k2mean_seed46.json\", \"submitted_at\": \"2026-05-24T03:23:22.142Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 46, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"n/a-baseline\"}, \"hypothesis\": \"VLA-only K=2 mean baseline on LIBERO-Long suite seed46 provides the fifth seed for Long K2-mean variance analysis, establishing the unrefined baseline performance across seeds.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.55, \"successes\": 110, \"total\": 200, \"source\": \"json_harvest_bjb1-32546\"}}, \"eval-supp-long-crm-norm005-s46\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T00:55:34.833Z\", \"updated_at\": \"2026-05-24T08:15:19.358Z\", \"hypothesis\": \"CRM obs-only refinement with max_correction_norm=0.05 on LIBERO-Long suite seed46 provides the fifth seed for Long CRM obs-only variance analysis, testing conservative correction magnitude across seeds.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark long --mode crm_obs_only --seed 46 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": 262247, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-crm-norm005-s46.log\", \"submitted_at\": \"2026-05-24T03:23:09.570Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 46, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.54, \"successes\": 108, \"total\": 200, \"source\": \"json_harvest_bjb1-32546\"}}, \"eval-supp-long-reconvla-s46\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T00:55:40.981Z\", \"updated_at\": \"2026-05-24T08:06:46.631Z\", \"hypothesis\": \"ReconVLA evaluation on LIBERO-Long suite seed46 provides the fifth seed for Long ReconVLA variance analysis, measuring reconstruction-based refinement consistency across seeds.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark long --mode reconvla --seed 46 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": 262529, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-reconvla-s46.log\", \"submitted_at\": \"2026-05-24T03:23:15.265Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 46, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.56, \"successes\": 112, \"total\": 200, \"source\": \"json_harvest_bjb1-32546\"}}, \"eval-supp-long-adapt-tau025-s46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T00:55:46.960Z\", \"updated_at\": \"2026-05-24T08:05:01.126Z\", \"hypothesis\": \"Adaptive CRM with τ=0.25 on LIBERO-Long suite seed46 provides the fifth seed for Long Adaptive variance analysis, testing whether adaptive conformal refinement consistently improves over baselines across seeds.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark long --mode adaptive_conformal_crm --seed 46 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --max_correction_norm 0.2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": 261974, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-adapt-tau025-s46.log\", \"submitted_at\": \"2026-05-24T03:23:03.745Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 46, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"wall_clock_seconds\": 16917.4, \"gpu_hours\": 4.7}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.585, \"successes\": 117, \"total_rollouts\": 200, \"benchmark\": \"long\", \"mode\": \"adaptive_conformal_crm\", \"seed\": 46, \"K\": 10, \"max_correction_norm\": 0.2, \"conformal_threshold\": 0.25}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_long_adaptive_conformal_crm_norm0.2_tau0.25_seed46.json\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"completed_at\": \"2026-05-24T08:05:01.126Z\"}, \"eval-supp-k2mean-spatial-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:15:55.833Z\", \"updated_at\": \"2026-05-24T07:18:30.230Z\", \"hypothesis\": \"K=2 mean baseline on Spatial suite seed47. Sixth seed extending variance analysis. 5-seed mean ~80%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark spatial --mode vla_only --baseline_mode mean --K 2 --seed 47 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:3\"], \"tmux_session\": \"spatial-k2mean-s47\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"checkpoint_source\": \"n/a-baseline\"}}, \"eval-supp-reconvla-spatial-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:15:47.910Z\", \"updated_at\": \"2026-05-24T07:18:23.847Z\", \"hypothesis\": \"Reconvla K=10 on Spatial suite seed47. Sixth seed extending variance analysis. 5-seed mean ~80%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark spatial --mode reconvla --seed 47 --n_rollouts 20 --K 10\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:2\"], \"tmux_session\": \"spatial-reconvla-s47\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA+Reconvla\", \"seed\": 47, \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"checkpoint_source\": \"n/a-reconvla\"}}, \"eval-supp-adapt-tau025-spatial-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:15:43.884Z\", \"updated_at\": \"2026-05-24T07:18:17.441Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Spatial suite seed47. Sixth seed extending variance analysis. 5-seed mean ~80.5%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark spatial --mode adaptive_conformal_crm --seed 47 --n_rollouts 20 --K 10 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:1\"], \"tmux_session\": \"spatial-adapt-s47\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA+Adaptive CRM\", \"seed\": 47, \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\"}}, \"eval-supp-vla-only-spatial-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:15:40.347Z\", \"updated_at\": \"2026-05-24T07:18:10.979Z\", \"hypothesis\": \"VLA-only baseline on Spatial suite seed47. Sixth seed extending variance analysis. 5-seed mean ~78.7%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode vla_only --seed 47 --n_rollouts 20 --K 1\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:0\"], \"tmux_session\": \"spatial-vla-s47\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"checkpoint_source\": \"n/a-baseline\"}}, \"eval-supp-goal-vla-only-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:14:14.567Z\", \"updated_at\": \"2026-05-24T07:17:13.996Z\", \"hypothesis\": \"Goal s47 VLA-only (K=1) baseline to extend Goal seed coverage beyond s42-s46 for supplementary variance analysis.\", \"parent\": \"eval-supp-goal-vla-only-s46\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark goal --mode vla_only --seed 47 --n_rollouts 20 --K 1\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": 279117, \"tmux_session\": \"goal-vla-s47\", \"log_path\": \"logs/eval-supp-goal-vla-only-s47.log\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Goal\", \"checkpoint_source\": \"n/a-baseline\", \"checkpoint_path\": \"n/a-eval-only\"}}, \"eval-supp-long-vla-only-s47-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:14:04.522Z\", \"updated_at\": \"2026-05-24T07:17:06.584Z\", \"hypothesis\": \"Long s47 VLA-only (K=1) baseline to complete the Long s47 seed extension set. The existing eval-supp-long-vla-only-s47 is actually k2mean (K=2 mean), so this fills the true VLA-only gap.\", \"parent\": \"eval-supp-long-vla-only-s46\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark long --mode vla_only --seed 47 --n_rollouts 20 --K 1\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": 278846, \"tmux_session\": \"long-vla-s47-r2\", \"log_path\": \"logs/eval-supp-long-vla-only-s47-r2.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"n/a-baseline\", \"checkpoint_path\": \"n/a-eval-only\"}}, \"eval-supp-adapt-tau025-spatial-s46\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:12:18.821Z\", \"updated_at\": \"2026-05-24T07:16:50.821Z\", \"hypothesis\": \"CRM/Adaptive on Spatial seed46, 5th seed extension\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark spatial --mode adaptive_conformal_crm --seed 46 --n_rollouts 20 --K 10 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO spatial suite\", \"data_count\": 200, \"model_name\": \"SmolVLA + Adaptive CRM (crm_smolvla_3suite_v1)\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 20 rollouts\"}, \"failure_reason\": \"GPU 1 occupied by OpenVLA VLA-only eval (PID 114990). Not actually started despite RUNNING status. Will deploy when GPU frees up.\"}, \"eval-supp-crm-norm005-spatial-s46\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:12:15.210Z\", \"updated_at\": \"2026-05-24T07:14:47.458Z\", \"hypothesis\": \"CRM/Adaptive on Spatial seed46, 5th seed extension\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 46 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO spatial\", \"data_count\": 200, \"model_name\": \"smolvla+crm_smolvla_3suite_v1\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 20 rollouts\"}}, \"crm-train-openvla-k1-multiscale-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:32:56.953Z\", \"updated_at\": \"2026-05-24T07:09:37.983Z\", \"hypothesis\": \"Training the K=1 MultiScaleCRM architecture on OpenVLA's multi-scale Llama-7B features (4 layers × 4096-d, action_dim=6 single-step) will provide a learned conformal correction module for OpenVLA on LIBERO-Object, with the goal of improving over the OpenVLA VLA-only baseline (SR=69%). This differs from the prior train-crm-openvla-obs-only (K=10 obs-only architecture, eval SR=0%) by using the multi-scale attention fusion + action-conditioned gating from plan_700.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/train_crm_k1.py --benchmark object --cache_dir /root/autodl-tmp/crm_cache_k1_openvla --obs_dim 4096 --epochs 50 --batch_size 512 --lr 1e-3 --seed 42 --output_dir /root/autodl-tmp/checkpoints/crm_openvla_k1_multiscale/object --wandb_run_name crm-openvla-k1-multiscale-object --loss_mode multi\", \"server\": \"bjb2-28827\", \"data_path\": \"/root/autodl-tmp/crm_cache_k1_openvla/object\", \"data_count\": 74507, \"model_name\": \"MultiScaleCRM-OpenVLA-K1\", \"seed\": 42}, \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.077477, \"total_epochs\": 50, \"train_samples\": 74507, \"obs_dim\": 4096, \"params\": 908106, \"architecture\": \"MultiScaleCRM-K1\"}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_openvla_k1_multiscale/object\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/crm-openvla-k1-multiscale-object.log\", \"completed_at\": \"2026-05-24T07:09:37.983Z\"}, \"eval-openvla-object-vla-only-seed42-v3\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T07:07:37.003Z\", \"updated_at\": \"2026-05-24T07:08:07.984Z\", \"hypothesis\": \"After fixing OpenVLA loading for transformers 5.8.1 (model_type 'openvla' auto-registration via openvla_compat + PrismaticImageProcessor workaround), VLA-only baseline on LIBERO-Object seed42 should reproduce the previously observed ~69% success rate from eval-openvla-object-vla-only-seed42-v2. Validates that the new loader path preserves model behavior bit-for-bit.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u src/openvla_eval.py --benchmark object --model_path /root/autodl-tmp/models/openvla-libero-object --mode vla_only --seed 42 --n_rollouts 20 --gpu 0 --output_file logs/eval_openvla_object_vla_only_seed42_v3.json\", \"server\": \"bjb2-28827\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_object\", \"data_count\": 200, \"model_name\": \"openvla-libero-object\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/openvla-libero-object\", \"eval_data\": \"LIBERO-Object (10 tasks x 20 rollouts = 200 episodes)\", \"pid\": \"114984\", \"log_path\": \"/tmp/eval_openvla_vla_only_seed42_v3.log\", \"checkpoint_path\": \"/root/autodl-tmp/models/openvla-libero-object\"}}, \"eval-supp-long-k2mean-s46-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:34:16.953Z\", \"updated_at\": \"2026-05-24T07:06:31.785Z\", \"hypothesis\": \"K=2 mean baseline on Long suite seed46 (re-deploy after r1 failed on bjb1-32546). Fifth seed completing Long K2mean 5-seed coverage. Isolates multi-sample averaging on Long suite.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark long --mode vla_only --baseline_mode mean --K 2 --seed 46 --n_rollouts 20 --output_file logs/eval_long_k2mean_seed46.json\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:3\"], \"tmux_session\": \"long-k2mean-s46-r2\", \"log_path\": \"logs/eval-supp-long-k2mean-s46-r2.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 46, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"n/a-baseline\", \"parent\": \"eval-supp-long-k2mean-s46\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-24T07:06:31.785Z\"}, \"eval-supp-long-reconvla-s46-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:34:13.683Z\", \"updated_at\": \"2026-05-24T07:06:23.946Z\", \"hypothesis\": \"Reconvla K=10 on Long suite seed46 (re-deploy after r1 failed on bjb1-32546). Fifth seed completing Long Reconvla 5-seed coverage.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark long --mode reconvla --seed 46 --n_rollouts 20 --K 10\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:2\"], \"tmux_session\": \"long-reconvla-s46-r2\", \"log_path\": \"logs/eval-supp-long-reconvla-s46-r2.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 46, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"n/a-reconvla\", \"parent\": \"eval-supp-long-reconvla-s46\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-24T07:06:23.946Z\"}, \"eval-supp-long-crm-norm005-s46-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:34:10.482Z\", \"updated_at\": \"2026-05-24T07:06:15.932Z\", \"hypothesis\": \"CRM always-on norm=0.05 on Long suite seed46 (re-deploy after r1 failed on bjb1-32546). Fifth seed completing Long CRM 5-seed coverage. 3-seed mean 55.8%±1.2%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark long --mode crm_obs_only --seed 46 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:1\"], \"tmux_session\": \"long-crm-s46-r2\", \"log_path\": \"logs/eval-supp-long-crm-norm005-s46-r2.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 46, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"parent\": \"eval-supp-long-crm-norm005-s46\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-24T07:06:15.932Z\"}, \"eval-supp-long-adapt-tau025-s46-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:34:07.178Z\", \"updated_at\": \"2026-05-24T07:06:09.666Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Long suite seed46 (re-deploy after r1 failed on bjb1-32546 with python: command not found). Fifth seed completing Long Adaptive 5-seed coverage. 3-seed mean 57.7%±1.5%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark long --mode adaptive_conformal_crm --seed 46 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --max_correction_norm 0.2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:0\"], \"tmux_session\": \"long-adapt-s46-r2\", \"log_path\": \"logs/eval-supp-long-adapt-tau025-s46-r2.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 46, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"parent\": \"eval-supp-long-adapt-tau025-s46\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-24T07:06:09.666Z\"}, \"eval-supp-long-vla-only-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:34:23.532Z\", \"updated_at\": \"2026-05-24T07:05:36.964Z\", \"hypothesis\": \"K=2 mean baseline on Long suite seed47 (NOT VLA-only — actual command uses --baseline_mode mean --K 2, output eval_long_k2mean_seed47.json). Misnamed at creation. Paired with Adapt-s47 for matched-seed comparison.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark long --mode vla_only --baseline_mode mean --K 2 --seed 47 --n_rollouts 20 --output_file logs/eval_long_k2mean_seed47.json\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:5\"], \"tmux_session\": \"long-vla-s47\", \"log_path\": \"logs/eval-supp-long-vla-only-s47.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"n/a-baseline\", \"parent\": \"eval-supp-long-vla-only-s46\"}}, \"eval-supp-obj-crm-norm005-s45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T03:56:52.910Z\", \"updated_at\": \"2026-05-24T06:55:16.446Z\", \"metrics\": {\"success_rate\": 0.765, \"successes\": 153, \"total\": 200, \"source\": \"json_harvest_bjb2-40593\", \"json_file\": \"eval_object_crm_obs_only_norm0.05_seed45.json\"}, \"hypothesis\": \"CRM obs-only norm=0.05 on Object suite seed45. Extends Object CRM obs-only coverage for variance analysis.\", \"conclusion\": \"success\", \"spec\": {\"checkpoint_path\": \"n/a-eval-only\", \"log_path\": \"eval_object_crm_obs_only_norm0.05_seed45.json\", \"command\": \"duplicate entry fix\", \"server\": \"bjb2-40593\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"SmolVLA+CRM\", \"seed\": 45, \"eval_data\": \"LIBERO-Object\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\"}, \"completed_at\": \"2026-05-24T06:55:16.446Z\"}, \"eval-supp-long-crm-norm005-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:52:08.968Z\", \"updated_at\": \"2026-05-24T06:53:16.695Z\", \"hypothesis\": \"CRM obs-only norm=0.05 on Long suite seed47 (sixth seed extension). Pairs with running Long vla-only-s47 and adapt-s47 on cqa1-32758 to tighten Long suite CI which has highest variance.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark long --mode crm_obs_only --seed 47 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"tmux_session\": \"long-crm-s47\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-crm-norm005-s47.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\"}}, \"eval-supp-long-reconvla-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:52:05.630Z\", \"updated_at\": \"2026-05-24T06:53:02.593Z\", \"hypothesis\": \"Reconvla K=10 on Long suite seed47 (sixth seed extension). Pairs with running Long vla-only-s47 and adapt-s47 on cqa1-32758 to tighten Long suite CI which has highest variance.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark long --mode reconvla --seed 47 --n_rollouts 20 --K 10\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"tmux_session\": \"long-reconvla-s47\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-reconvla-s47.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"n/a-reconvla\"}}, \"eval-supp-spatial-crm-norm005-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:49:40.206Z\", \"updated_at\": \"2026-05-24T06:51:27.049Z\", \"hypothesis\": \"CRM obs_only norm=0.05 on LIBERO-Spatial seed47. Fifth seed extending Spatial CRM coverage (s43-s46 mean ~79.6%). Tightens CI for statistical comparison with VLA-only/K2mean/Reconvla/Adaptive at matched 5-seed coverage.\", \"parent\": \"eval-supp-spatial-crm-norm005-s46\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 47 --n_rollouts 20 --max_correction_norm 0.05 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_spatial_crm_obs_only_norm0.05_seed47.json\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"235730\", \"tmux_session\": \"eval-spatial-crm-s47\", \"log_path\": \"/tmp/eval_spatial_crm_s47.log\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"SmolVLA+CRM\", \"seed\": 47, \"eval_data\": \"LIBERO-Spatial\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"checkpoint_path\": \"n/a-eval-only\", \"submitted_at\": \"2026-05-24T06:50:07Z\", \"submitted_via\": \"ssh_execute_tmux\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval-supp-vla-only-spatial-s46\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:48:57.955Z\", \"updated_at\": \"2026-05-24T06:50:52.276Z\", \"hypothesis\": \"VLA-only baseline on Spatial suite seed46. Extending from 3-seed (s42/s43/s44) to 5-seed for variance analysis. 3-seed mean 78.7%±0.3%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark spatial --mode vla_only --seed 46 --n_rollouts 20 --K 1\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/models/smolvla_libero/\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"benchmark\": \"spatial\", \"mode\": \"vla_only\", \"tmux_session\": \"eval-supp-vla-only-spatial-s46\", \"gpu\": 5}}, \"eval-supp-adapt-tau025-spatial-s45\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:48:54.415Z\", \"updated_at\": \"2026-05-24T06:50:44.120Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 (conformal_threshold) with max_correction_norm=0.2 on Spatial suite seed45. Extending from 3-seed (s42/s43/s44) to 5-seed for variance analysis. 3-seed mean 80.8%±1.1%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark spatial --mode adaptive_conformal_crm --seed 45 --n_rollouts 20 --K 10 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla+crm-adaptive\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"benchmark\": \"spatial\", \"mode\": \"adaptive_conformal_crm\", \"max_correction_norm\": 0.2, \"conformal_threshold\": 0.25, \"K\": 10, \"tmux_session\": \"eval-supp-adapt-tau025-spatial-s45\", \"gpu\": 4}}, \"eval-supp-crm-norm005-spatial-s45\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:48:50.955Z\", \"updated_at\": \"2026-05-24T06:50:37.107Z\", \"hypothesis\": \"CRM always-on norm=0.05 on Spatial suite seed45. Extending from 3-seed (s42/s43/s44) to 5-seed for variance analysis. 3-seed mean 79.8%±1.3%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 45 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla+crm\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"benchmark\": \"spatial\", \"mode\": \"crm_obs_only\", \"max_correction_norm\": 0.05, \"K\": 10, \"tmux_session\": \"eval-supp-crm-norm005-spatial-s45\", \"gpu\": 3}}, \"eval-supp-vla-only-spatial-s45\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:48:46.040Z\", \"updated_at\": \"2026-05-24T06:50:30.794Z\", \"hypothesis\": \"VLA-only baseline on Spatial suite seed45. Extending from 3-seed (s42/s43/s44) to 5-seed for variance analysis. 3-seed mean 78.7%±0.3%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark spatial --mode vla_only --seed 45 --n_rollouts 20 --K 1\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/models/smolvla_libero/\", \"eval_data\": \"LIBERO-Spatial 10 tasks x 20 rollouts\", \"benchmark\": \"spatial\", \"mode\": \"vla_only\", \"tmux_session\": \"eval-supp-vla-only-spatial-s45\", \"gpu\": 2}}, \"eval-supp-obj-adapt-tau025-s45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T17:22:29.274Z\", \"updated_at\": \"2026-05-24T06:49:49.091Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Object suite seed45. Fills s45 gap in Object adaptive 5-seed coverage (have s42-s44) for supplementary table.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark object --mode adaptive_conformal_crm --seed 45 --n_rollouts 20 --max_correction_norm 0.2 --conformal_threshold 0.25 --K 2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"tmux_session\": \"eval-obj-adapt-s45\", \"log_path\": \"/tmp/eval_obj_adapt_s45.log\", \"seed\": 45, \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"SmolVLA+AdaptiveCRM\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}, \"conclusion\": \"failed\", \"log_path\": \"/tmp/eval_obj_adapt_s45.log\", \"checkpoint_path\": \"N/A (eval only, crashed due to missing CRM checkpoint)\", \"completed_at\": \"2026-05-23T17:51:39.777Z\"}, \"eval-supp-obj-vla-only-s45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T17:27:19.029Z\", \"updated_at\": \"2026-05-24T06:49:36.626Z\", \"hypothesis\": \"VLA-only baseline on Object suite seed45. Fills s45 gap in Object VLA-only 5-seed coverage (have s42-s44, s46) for supplementary table.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark object --mode vla_only --seed 45 --n_rollouts 20 --K 1\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": 849667, \"tmux_session\": \"eval-supp-obj-vla-only-s45\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-obj-vla-only-s45.log\", \"seed\": 45, \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"SmolVLA\"}, \"metrics\": {\"SR\": 0.76}, \"checkpoint_path\": \"N/A (eval only)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T20:26:43.571Z\"}, \"eval-supp-spatial-crm-norm005-s45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T21:31:12.741Z\", \"updated_at\": \"2026-05-24T06:45:22.337Z\", \"hypothesis\": \"CRM obs-only norm=0.05 on Spatial suite seed45. Sixth seed extending Spatial CRM always-on variance coverage for supplementary table.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 45 --n_rollouts 20 --max_correction_norm 0.05 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"cqa1-32758\", \"gpu\": \"cuda:3\", \"seed\": 45, \"model_name\": \"SmolVLA+CRM\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"eval_data\": \"LIBERO-Spatial\", \"checkpoint_source\": \"crm_smolvla_3suite_v1/crm_best.pt\", \"log_path\": \"/tmp/eval_spatial_crm_s45.log\"}, \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.78, \"successes\": 156, \"total\": 200, \"per_task\": {\"between_plate_and_ramekin\": 1, \"next_to_ramekin\": 1, \"table_center\": 0.9, \"on_cookie_box\": 1, \"top_drawer_cabinet\": 0.7, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.95, \"on_stove\": 0.8, \"next_to_plate\": 0.75, \"on_wooden_cabinet\": 0.7}}, \"notes\": \"Eval completed normally. 78.0% (156/200). Results at logs/eval_spatial_crm_obs_only_norm0.05_seed45.json on cqa1-32758. Cron escalated as process-gone but script had already exited after completion.\", \"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"/tmp/eval_spatial_crm_s45.log\", \"completed_at\": \"2026-05-24T00:31:58.951Z\"}, \"eval-supp-spatial-vla-only-s45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T21:31:09.089Z\", \"updated_at\": \"2026-05-24T06:45:16.646Z\", \"hypothesis\": \"VLA-only baseline on Spatial suite seed45. Sixth seed extending Spatial VLA-only variance coverage for supplementary table.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark spatial --mode vla_only --seed 45 --n_rollouts 20 --K 1\", \"server\": \"cqa1-32758\", \"gpu\": \"cuda:1\", \"seed\": 45, \"model_name\": \"SmolVLA\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"eval_data\": \"LIBERO-Spatial\", \"log_path\": \"/tmp/eval_spatial_vla_s45.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T00:32:37.014Z\", \"notes\": \"Eval completed normally on cqa1-32758. SR=77.0% (154/200). Results at logs/eval_spatial_vla_only_seed45.json. Per-task: between_plate_ramekin 90%, next_to_ramekin 90%, table_center 90%, on_cookie_box 100%, top_drawer 75%, on_ramekin 0%, next_to_cookie_box 95%, on_stove 75%, next_to_plate 80%, on_wooden_cabinet 75%.\", \"metrics\": {\"SR\": 0.77, \"successes\": 154, \"total\": 200}}, \"eval-supp-long-adapt-tau025-s47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:34:20.287Z\", \"updated_at\": \"2026-05-24T06:38:39.651Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Long suite seed47 (sixth seed extension). Long is the highest-variance suite with smallest improvement margin (57.7 vs 58.0 VLA-only). Sixth seed tightens CI to determine if Adaptive is statistically equivalent to or below VLA-only on Long.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark long --mode adaptive_conformal_crm --seed 47 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --max_correction_norm 0.2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:4\"], \"tmux_session\": \"long-adapt-s47\", \"log_path\": \"logs/eval-supp-long-adapt-tau025-s47.log\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 47, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"parent\": \"eval-supp-long-adapt-tau025-s46-r2\"}}, \"precompute-pi05-long-2048-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:18:31.140Z\", \"updated_at\": \"2026-05-24T06:23:39.262Z\", \"hypothesis\": \"Precomputing π0.5 obs_features and K=2048 action samples on LIBERO-Long enables downstream CRM training for cross-model (SmolVLA→π0.5) generalization verification without re-running inference at train time.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 nohup python -u src/train_crm.py --precompute --model pi05 --benchmark long --K 10 --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/ > /root/autodl-tmp/logs/precompute_pi05_long_2048.log 2>&1 &\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": 114507, \"data_path\": \"/root/autodl-tmp/crm_cache_pi05_2048/long/\", \"data_count\": 136090, \"model_name\": \"pi0.5\", \"seed\": 0, \"log_path\": \"/root/autodl-tmp/logs/precompute_pi05_long_2048.log\"}}, \"precompute-pi05-goal-2048-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:18:27.873Z\", \"updated_at\": \"2026-05-24T06:23:35.000Z\", \"hypothesis\": \"Precomputing π0.5 obs_features and K=2048 action samples on LIBERO-Goal enables downstream CRM training for cross-model (SmolVLA→π0.5) generalization verification without re-running inference at train time.\", \"spec\": {\"command\": \"python -u src/train_crm.py --precompute --model pi05 --benchmark goal --K 10 --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/\", \"server\": \"bjb1-18228\", \"data_path\": \"/root/autodl-tmp/crm_cache_pi05_2048/goal/\", \"data_count\": 61728, \"model_name\": \"pi0.5\", \"seed\": 0}, \"log_path\": \"N/A\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache_pi05_2048/goal/\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T06:20:24.923Z\"}, \"precompute-pi05-object-2048-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T06:18:24.705Z\", \"updated_at\": \"2026-05-24T06:23:31.677Z\", \"hypothesis\": \"Precomputing π0.5 obs_features and K=2048 action samples on LIBERO-Object enables downstream CRM training for cross-model (SmolVLA→π0.5) generalization verification without re-running inference at train time.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 nohup python -u src/train_crm.py --precompute --model pi05 --benchmark object --K 10 --cache_dir /root/autodl-tmp/crm_cache_pi05_2048/ > /root/autodl-tmp/logs/precompute_pi05_object_2048.log 2>&1 &\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": 113456, \"data_path\": \"/root/autodl-tmp/crm_cache_pi05_2048/object/\", \"data_count\": 72507, \"model_name\": \"pi0.5\", \"seed\": 0, \"log_path\": \"/root/autodl-tmp/logs/precompute_pi05_object_2048.log\"}}, \"eval-supp-long-vla-only-s46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T00:32:53.028Z\", \"updated_at\": \"2026-05-24T06:15:12.631Z\", \"hypothesis\": \"Long VLA-only baseline seed46. Fifth seed for Long VLA-only variance analysis. 3-seed mean 58.0%±1.5%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark long --mode vla_only --seed 46 --n_rollouts 20 --K 1\", \"server\": \"cqa1-32758\", \"gpu\": \"cuda:3\", \"seed\": 46, \"model_name\": \"SmolVLA\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"eval_data\": \"LIBERO-Long\", \"log_path\": \"/tmp/eval_long_vla_s46.log\", \"pid\": 601530, \"tmux_session\": \"eval-long-vla-s46\", \"checkpoint_path\": \"n/a-eval-only\"}, \"reproduce\": {\"finished_at\": \"2026-05-24T05:13:17.230Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T05:13:08.597Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-24T05:13:37.611636+00:00\"}]}, \"metrics\": {\"success_rate\": 60.5, \"successes\": 121, \"total\": 200, \"source\": \"reviewer_manual_check\"}}, \"precompute-pi05-spatial-2048-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T05:52:22.340Z\", \"updated_at\": \"2026-05-24T06:13:04.507Z\", \"failure_reason\": \"\", \"reproduce\": {\"finished_at\": \"2026-05-24T05:52:25.446Z\"}, \"conclusion\": \"success\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-24T05:52:49.805726+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/crm_cache_pi05_2048/spatial/\", \"spec\": {\"command\": \"python precompute_cache.py --model pi05 --suite spatial --K 2048\", \"server\": \"bjb1-18228\", \"data_path\": \"/root/autodl-tmp/crm_cache_pi05_2048/spatial/\", \"data_count\": 60250, \"model_name\": \"pi0.5\", \"seed\": 0}, \"log_path\": \"N/A\", \"hypothesis\": \"Precomputing π0.5 obs_features and K=2048 action samples on LIBERO-Spatial enables downstream CRM training for cross-model (SmolVLA→π0.5) generalization verification without re-running inference at train time.\", \"completed_at\": \"2026-05-24T06:13:04.507Z\"}, \"precompute-smolvla-goal-bjb1-32546\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T06:35:21.518Z\", \"updated_at\": \"2026-05-24T05:44:03.369Z\", \"hypothesis\": \"Precompute SmolVLA obs_features + K=10 action samples on LIBERO-Goal for unified 4-suite CRM training\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python src/train_crm.py --precompute --benchmark goal --K 10 --cache_dir /root/autodl-tmp/crm_cache_v5/\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"260139\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-smolvla-goal-bjb1-32546.log\", \"submitted_at\": \"2026-05-22T06:36:52.793Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 169630.6, \"gpu_hours\": 47.12}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-24T05:44:03.369Z\"}, \"eval-supp-goal-vla-only-s46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T23:02:24.393Z\", \"updated_at\": \"2026-05-24T05:43:32.643Z\", \"hypothesis\": \"Goal VLA-only baseline seed46. Fifth seed extending Goal VLA-only. s42-s45 mean ~84%. Completes 5-seed coverage.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark goal --mode vla_only --seed 46 --n_rollouts 20 --K 1\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:0\", \"pid\": \"991460\", \"log_path\": \"/tmp/eval_goal_vla_s46.log\", \"submitted_at\": \"2026-05-23T23:03:11.586Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 46, \"model_name\": \"SmolVLA\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"eval_data\": \"LIBERO-Goal\", \"tmux_session\": \"eval-supp-goal-vla-only-s46\", \"checkpoint_source\": \"n/a\", \"checkpoint_path\": \"n/a-eval-only\", \"wall_clock_seconds\": 24021.1, \"gpu_hours\": 6.67}, \"reproduce\": {\"finished_at\": \"2026-05-24T01:20:39.871Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-24T01:21:11.796398+00:00\"}]}, \"metrics\": {\"success_rate\": 0.83, \"source\": \"json_harvest_bjb2-28827\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T05:43:32.643Z\"}, \"eval-supp-goal-reconvla-s46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T23:02:35.384Z\", \"updated_at\": \"2026-05-24T05:43:26.502Z\", \"hypothesis\": \"Reconvla K=10 argmin on Goal suite seed46. Fifth seed extending Goal Reconvla. s42-s45 mean ~83%. Completes 5-seed coverage.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark goal --mode reconvla --seed 46 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:2\", \"pid\": \"992062\", \"log_path\": \"/tmp/eval_goal_reconvla_s46.log\", \"submitted_at\": \"2026-05-23T23:03:22.963Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 46, \"model_name\": \"SmolVLA-Reconvla\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"eval_data\": \"LIBERO-Goal\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"tmux_session\": \"eval-supp-goal-reconvla-s46\", \"checkpoint_path\": \"n/a-eval-only\", \"wall_clock_seconds\": 24003.5, \"gpu_hours\": 6.67}, \"reproduce\": {\"finished_at\": \"2026-05-24T01:28:39.321Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-24T01:29:27.445398+00:00\"}]}, \"metrics\": {\"success_rate\": 0.79, \"source\": \"json_harvest_bjb2-28827\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T05:43:26.502Z\"}, \"crm-train-pi05-spatial-full\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-21T18:48:38.574Z\", \"updated_at\": \"2026-05-24T03:28:46.242Z\", \"hypothesis\": \"CRM projection trained on π0.5 full precomputed features (~60250 spatial samples, K=10) will learn conformal refinement corrections improving upon π0.5 VLA-only baseline (84.2%) on LIBERO-Spatial, validating cross-VLA generalization\", \"reproduce\": {\"finished_at\": \"2026-05-21T19:16:05.516Z\"}, \"failure_reason\": \"Traceback → n main train(args) File \\\"/root/acr-vla-conformal-refinement/src/train_crm.py\\\", line 329, in train raise FileNotFoundError( FileNotFoundError: No precomputed cache at /root/autodl-tmp/crm_cache_pi05/spatial. Run with --precompute first, or use --auto.\", \"completed_at\": \"2026-05-21T19:16:13.590Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-21T19:16:24.207448+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"python -u src/train_crm.py --benchmark spatial --cache_dir /root/autodl-tmp/crm_cache_pi05/ --output_dir /root/autodl-tmp/checkpoints/crm_pi05_full/spatial/ --epochs 50 --batch_size 32 --lr 1e-3 --obs_dim 2048\", \"server\": \"bjb1-18228\", \"data_path\": \"/root/autodl-tmp/crm_cache_pi05/spatial/\", \"data_count\": 60250, \"model_name\": \"CRM-spatial\", \"seed\": 42, \"gpu\": \"cuda:1\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-train-pi05-spatial-full.log\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_pi05_full/spatial/\"}, \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.006138, \"epochs_completed\": 50, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_pi05_full/spatial/\"}}, \"eval-obs-only-spatial-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:43:42.283Z\", \"updated_at\": \"2026-05-24T03:27:16.008Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v2/obs_only/crm_best.pt\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"203968\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-spatial-v2.log\", \"submitted_at\": \"2026-05-14T12:43:42.188Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"CRM obs_only v2 (990D, no conformal features)\", \"seed\": 42, \"hypothesis\": \"obs_only CRM ablation — CRM without conformal features tests whether per-DOF conformal intervals are necessary for effective correction\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v2/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"parent\": \"crm-train-v2-obs-only\", \"failure_reason\": \"Bug: evaluate.py line 266 CRM load condition missing crm_obs_only, CRM was None throughout eval, all rollouts 0%. Replaced by eval-obs-only-spatial-v3.\", \"wall_clock_seconds\": 185.5, \"gpu_hours\": 0.05}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T12:46:47.663Z\", \"hypothesis\": \"Obs-only CRM v2 retrained on spatial data resolves the dimension mismatch from v1 and achieves meaningful improvement on LIBERO-Spatial by using benchmark-matched visual features\", \"parent\": \"eval-obs-only-spatial\", \"metrics\": {\"success_rate\": 0, \"successes\": 0, \"total\": 100}}, \"eval-perdof-object-norm003-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T13:27:53.154Z\", \"updated_at\": \"2026-05-24T03:27:10.816Z\", \"hypothesis\": \"perdof CRM ε=0.03 seed44 on LIBERO-Object。magnitude curve 低 ε 端 perdof ε=0.03 当前 seed42=14% (n=1)，seed43 已在跑。第三个 seed 进一步增强统计。\", \"parent\": \"eval-mag-perdof-norm003-object\", \"spec\": {\"command\": \"bash -c \\\"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_perdof_norm003_seed44.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"853859\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm003-seed44.log\", \"submitted_at\": \"2026-05-18T13:31:56.791Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"server\": \"bjb1-18228\", \"gpu\": \"cuda:2\", \"pid\": \"unknown\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm003-seed44.log\", \"reproduce\": {\"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_perdof_norm003_seed44.json\", \"finished_at\": \"2026-05-18T13:29:15.735Z\"}, \"failure_reason\": \"EXIT_CODE=127 (command not found — check bash -c wrapping / env activate)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T13:29:19.018Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T13:29:24.215222+00:00\"}]}, \"notes\": \"EXIT_CODE=127, python not found. bjb1-18228 需用 /root/miniconda3/bin/python 而非 bare python.\", \"metrics\": {\"success_rate\": 11, \"successes\": 11, \"total\": 100}}, \"eval-random-selection-spatial-seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:44:50.876Z\", \"updated_at\": \"2026-05-24T03:27:05.531Z\", \"hypothesis\": \"Random selection baseline (K=10, pick uniformly at random) on LIBERO-Spatial seed42. On Object, Random K=10 (11.3%) ≈ VLA-only (10.9%), proving CRM guidance is the value. Tests whether same pattern holds on Spatial: if Random ≈ VLA-only (~29.6%), CRM's +5pp is from guidance not sampling diversity.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode random_selection --benchmark spatial --seed 42 --n_rollouts 10 --K 10\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"346791\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-random-selection-spatial-seed42.log\", \"submitted_at\": \"2026-05-20T10:51:06.018Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"model_name\": \"random_selection_baseline\", \"seed\": 42, \"wall_clock_seconds\": 3442.7, \"gpu_hours\": 0.96}, \"reproduce\": {\"finished_at\": \"2026-05-20T11:45:44.060Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"conclusion\": \"success\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T11:45:54.901120+00:00\"}]}, \"completed_at\": \"2026-05-20T11:48:28.747Z\", \"metrics\": {\"success_rate\": 34, \"successes\": 34, \"total\": 100}}, \"eval-adaptive-k-spatial-p90-seed44-bjb2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T13:50:21.016Z\", \"updated_at\": \"2026-05-24T03:27:01.680Z\", \"hypothesis\": \"Adaptive K with τ=P90 (0.125870) on LIBERO-Spatial seed44. Third seed completing Spatial P90 cross-benchmark sweep.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode adaptive_k --adaptive_threshold 0.125870 --k_full 10 --benchmark spatial --seed 44 --n_rollouts 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_adaptive_k_spatial_p90_seed44.json\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:0\", \"pid\": 975409, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-adaptive-k-spatial-p90-seed44-bjb2.log\", \"submitted_at\": \"2026-05-20T13:50:48.545Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 44, \"model_name\": \"CRM_obs_only_adaptive_k\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 100, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"wall_clock_seconds\": 55922.2, \"gpu_hours\": 15.53}, \"reproduce\": {\"finished_at\": \"2026-05-21T05:22:43.825Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T05:22:50.761Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-21T05:23:07.915783+00:00\"}]}, \"metrics\": {\"success_rate\": 36, \"successes\": 36, \"total\": 100, \"fast_path\": 81.5, \"avg_k\": 3.5, \"mean_l2\": 0.0885}}, \"eval-supp-goal-vla-only-wrapper-s44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T11:34:16.215Z\", \"updated_at\": \"2026-05-24T03:26:55.797Z\", \"hypothesis\": \"Goal VLA-only wrapper fresh eval seed44. Confirms 83.5% baseline across seeds.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark goal --seed 44 --n_rollouts 20\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"906142\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-goal-vla-only-wrapper-s44.log\", \"submitted_at\": \"2026-05-23T11:34:40Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 44, \"wall_clock_seconds\": 10078.6, \"gpu_hours\": 2.8}, \"metrics\": {\"success_rate\": 82, \"successes\": 164, \"total\": 200}, \"log_path\": \"LOST - overwritten by k2mean-goal-s44\", \"checkpoint_path\": \"N/A (eval only)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T14:22:38.574Z\"}, \"eval-supp-long-reconvla-s45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T20:12:57.615Z\", \"updated_at\": \"2026-05-24T03:26:47.449Z\", \"hypothesis\": \"Reconvla K=10 on Long suite seed45. Fourth seed for Long Reconvla validation.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark long --mode reconvla --seed 45 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:4\", \"seed\": 45, \"model_name\": \"SmolVLA-Reconvla\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"crm_unified_4suite_r4/crm_best.pt\", \"log_path\": \"/tmp/eval_long_reconvla_s45.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-24T01:10:03.694Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T01:10:13.119Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-24T01:10:25.577523+00:00\"}]}, \"metrics\": {\"success_rate\": 59, \"successes\": 118, \"total\": 200}}, \"eval-supp-spatial-k2mean-s46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T23:41:52.628Z\", \"updated_at\": \"2026-05-24T03:26:39.499Z\", \"hypothesis\": \"K=2 mean baseline on Spatial suite seed46. Fifth seed extending Spatial K2mean coverage for variance analysis.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode vla_only --baseline_mode mean --K 2 --seed 46 --n_rollouts 20 --output_file logs/eval_spatial_k2mean_seed46.json\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:0\", \"seed\": 46, \"model_name\": \"SmolVLA-K2mean\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"eval_data\": \"LIBERO-Spatial\", \"log_path\": \"/tmp/eval_spatial_k2mean_s46.log\", \"checkpoint_source\": \"n/a\", \"checkpoint_path\": \"n/a-eval-only\"}, \"reproduce\": {\"finished_at\": \"2026-05-24T01:40:09.136Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T01:40:06.099Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-24T01:40:29.611202+00:00\"}]}, \"metrics\": {\"success_rate\": 80, \"successes\": 160, \"total\": 200}}, \"eval-supp-obj-crm-norm005-s46\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T03:25:56.315Z\", \"updated_at\": \"2026-05-24T03:26:33.701Z\", \"hypothesis\": \"Supplementary 5-seed evaluation: Object CRM obs_only norm0.05 seed46 variance analysis.\", \"metrics\": {\"success_rate\": 0.795, \"successes\": 159, \"total\": 200, \"source\": \"json_harvest_bjb1\"}, \"conclusion\": \"success\"}, \"eval-pi05-vla-only-long-seed42-r4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T12:22:12.815Z\", \"updated_at\": \"2026-05-24T03:26:27.340Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Long with official settings: n_action_steps=10, 10 dummy steps gripper-open, max_steps=520\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode vla_only --model pi05 --benchmark long --seed 42 --n_rollouts 20 --K 10 --n_action_steps 10 --max_steps 520 --output_file logs/eval_long_vla_only_seed42_r4.json\\\"\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"67669\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-long-seed42-r4.log\", \"submitted_at\": \"2026-05-22T15:52:57.803Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 4052.5, \"gpu_hours\": 1.13}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T17:00:30.262Z\", \"metrics\": {\"success_rate\": 0, \"successes\": 0, \"total\": 200}}, \"eval-supp-reconvla-obj-s45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T22:37:18.110Z\", \"updated_at\": \"2026-05-24T03:26:15.872Z\", \"hypothesis\": \"Reconvla K=10 argmin on Object suite seed45. Extends Object Reconvla coverage, s46 already 80.0%. Fourth seed for variance analysis.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark object --mode reconvla --seed 45 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:5\", \"seed\": 45, \"model_name\": \"smolvla+crm\", \"data_path\": \"libero_object\", \"data_count\": 20, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"log_path\": \"logs/eval-reconvla-obj-s45.log\", \"checkpoint_path\": \"n/a-eval-only\", \"eval_data\": \"libero_object\"}, \"reproduce\": {\"finished_at\": \"2026-05-24T01:14:37.557Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T01:14:46.869Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-24T01:14:59.634087+00:00\"}]}, \"metrics\": {\"success_rate\": 0.78, \"successes\": 156, \"total\": 200, \"source\": \"json_harvest_bjb1\"}}, \"eval-pi05-vla-only-object-seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T08:22:14.823Z\", \"updated_at\": \"2026-05-24T03:25:46.138Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object seed42, cross-VLA validation of CRM\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCH_COMPILE_DISABLE=1 TORCHDYNAMO_DISABLE=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --n_rollouts 20 --seed 42 --K 10\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"982849\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-seed42.log\", \"submitted_at\": \"2026-05-21T10:18:26.307Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 5205.3, \"gpu_hours\": 1.45}, \"reproduce\": {\"finished_at\": \"2026-05-21T11:38:56.784Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-21T11:39:24.095528+00:00\"}]}, \"log_path\": \"/root/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-seed42.log\", \"checkpoint_path\": \"N/A (eval only)\", \"metrics\": {\"overall_sr\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T11:45:11.623Z\", \"notes\": \"ANOMALY: 0% SR (0/200) across all 10 tasks. Prior quick verify on bjb2-40593 showed 72% (50 rollouts) with identical code/model/deps. Code, model weights (7.47GB), normalizer files, torch 2.10.0+cu128, lerobot 0.5.2, transformers 5.8.0 all verified identical between servers. SmolVLA works fine on bjb1-32546 (12% vla_only). Root cause unknown — possible GPU arch bfloat16 difference or hidden env issue. NEEDS RE-RUN ON bjb2-40593.\"}, \"eval-pi05-vla-only-object-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T08:22:17.435Z\", \"updated_at\": \"2026-05-24T03:25:36.173Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object seed43, cross-VLA validation of CRM\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCH_COMPILE_DISABLE=1 TORCHDYNAMO_DISABLE=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --n_rollouts 20 --seed 43 --K 10\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"983128\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-seed43.log\", \"submitted_at\": \"2026-05-21T10:18:36.208Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 5206.7, \"gpu_hours\": 1.45}, \"reproduce\": {\"finished_at\": \"2026-05-21T11:39:39.042Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-21T11:39:59.242083+00:00\"}]}, \"log_path\": \"/root/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-seed43.log\", \"checkpoint_path\": \"N/A (eval only)\", \"metrics\": {\"overall_sr\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T11:45:22.888Z\", \"notes\": \"ANOMALY: 0% SR (0/200). Same issue as seed42 — all π0.5 vla_only evals on bjb1-32546 yield 0%. See seed42 notes for full analysis.\"}, \"eval-pi05-vla-only-object-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T08:22:19.985Z\", \"updated_at\": \"2026-05-24T03:25:23.533Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object seed44, cross-VLA validation of CRM\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && TORCH_COMPILE_DISABLE=1 TORCHDYNAMO_DISABLE=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --model pi05 --mode vla_only --benchmark object --n_rollouts 20 --seed 44 --K 10\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"983472\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-seed44.log\", \"submitted_at\": \"2026-05-21T10:18:46.979Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 5204.2, \"gpu_hours\": 1.45}, \"reproduce\": {\"finished_at\": \"2026-05-21T11:40:10.658Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-21T11:40:31.815288+00:00\"}]}, \"log_path\": \"/root/runs/acr-vla-conformal-refinement/eval-pi05-vla-only-object-seed44.log\", \"checkpoint_path\": \"N/A (eval only)\", \"metrics\": {\"overall_sr\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"total_rollouts\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T11:45:31.175Z\", \"notes\": \"ANOMALY: 0% SR (0/200). Same issue as seed42 — all π0.5 vla_only evals on bjb1-32546 yield 0%. See seed42 notes for full analysis.\"}, \"eval-supp-long-k2mean-s45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T20:20:29.949Z\", \"updated_at\": \"2026-05-24T03:24:43.469Z\", \"hypothesis\": \"K=2 mean baseline on Long suite seed45. Fourth seed extending Long K2mean coverage. VLA-only s45 on bjb1-32546 provides baseline.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark long --mode vla_only --baseline_mode mean --K 2 --seed 45 --n_rollouts 20 --output_file logs/eval_long_k2mean_seed45.json\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:4\", \"seed\": 45, \"model_name\": \"SmolVLA-K2mean\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"eval_data\": \"LIBERO-Long\", \"log_path\": \"/tmp/eval_long_k2mean_s45.log\", \"pid\": 924226}, \"reproduce\": {\"finished_at\": \"2026-05-24T02:09:20.528Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T02:09:29.913Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-24T02:09:45.657923+00:00\"}]}, \"metrics\": {\"success_rate\": 0.56, \"source\": \"json_harvest_bjb2-28827\"}}, \"eval-supp-goal-k2mean-s46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T23:06:24.679Z\", \"updated_at\": \"2026-05-24T03:24:33.666Z\", \"hypothesis\": \"K=2 mean baseline on Goal suite seed46. Extends Goal K2mean to 4th completed seed for variance analysis.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode mean --K 2 --seed 46 --n_rollouts 20 --output_file logs/eval_goal_k2mean_seed46.json\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:1\", \"seed\": 46, \"model_name\": \"SmolVLA-K2mean\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"eval_data\": \"LIBERO-Goal\", \"log_path\": \"/tmp/eval_goal_k2mean_s46.log\", \"tmux_session\": \"eval-goal-k2mean-s46\", \"checkpoint_source\": \"n/a\", \"checkpoint_path\": \"n/a-eval-only\"}, \"reproduce\": {\"finished_at\": \"2026-05-24T01:32:53.337Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T01:33:16.731Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-24T01:33:39.070461+00:00\"}]}, \"metrics\": {\"success_rate\": 0.825, \"source\": \"json_harvest_bjb2-28827\"}}, \"eval-supp-goal-adapt-tau025-s46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T23:02:43.468Z\", \"updated_at\": \"2026-05-24T03:24:30.058Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Goal suite seed46. Fifth seed extending Goal Adaptive. s42-s45 mean ~84%. Completes 5-seed coverage.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark goal --mode adaptive_conformal_crm --seed 46 --n_rollouts 20 --max_correction_norm 0.2 --conformal_threshold 0.25 --K 2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:5\", \"pid\": \"unknown\", \"log_path\": \"/tmp/eval_goal_adapt_s46.log\", \"submitted_at\": \"2026-05-23T23:03:32.801Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 46, \"model_name\": \"SmolVLA+AdaptiveCRM\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"eval_data\": \"LIBERO-Goal\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"tmux_session\": \"eval-goal-adapt-s46\", \"checkpoint_path\": \"n/a-eval-only\", \"wall_clock_seconds\": 9126.9, \"gpu_hours\": 2.54}, \"reproduce\": {\"finished_at\": \"2026-05-24T01:35:26.310Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T01:35:39.747Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-24T01:36:01.971157+00:00\"}]}, \"metrics\": {\"success_rate\": 0.835, \"trigger_rate\": 0.0909, \"tau\": 0.25, \"source\": \"json_harvest_bjb2-28827\"}}, \"eval-supp-goal-crm-norm005-s46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T23:06:31.022Z\", \"updated_at\": \"2026-05-24T03:24:26.680Z\", \"hypothesis\": \"CRM always-on norm=0.05 on Goal suite seed46. Fifth seed extending Goal CRM. s42-s45 mean ~83%. Completes 5-seed coverage.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark goal --mode crm_obs_only --seed 46 --n_rollouts 20 --max_correction_norm 0.05 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:3\", \"seed\": 46, \"model_name\": \"SmolVLA+CRM\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"eval_data\": \"LIBERO-Goal\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"log_path\": \"/tmp/eval_goal_crm_s46.log\", \"tmux_session\": \"eval-goal-crm-s46\", \"checkpoint_path\": \"n/a-eval-only\"}, \"reproduce\": {\"finished_at\": \"2026-05-24T01:36:34.079Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T01:37:08.984Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-24T01:37:50.254490+00:00\"}]}, \"metrics\": {\"success_rate\": 0.82, \"source\": \"json_harvest_bjb2-28827\"}}, \"eval-supp-spatial-adapt-tau025-s45-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T23:42:31.834Z\", \"updated_at\": \"2026-05-24T03:19:19.270Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Spatial suite seed45. Re-deployed after prior kills. Validates Adaptive improvement on Spatial (3-seed mean +2.1pp over VLA-only 78.7%).\", \"parent\": \"eval-supp-spatial-adapt-tau025-s45\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode adaptive_conformal_crm --seed 45 --n_rollouts 20 --max_correction_norm 0.2 --conformal_threshold 0.25 --K 2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"cqa1-32758\", \"gpu\": \"cuda:4\", \"seed\": 45, \"model_name\": \"SmolVLA+AdaptiveCRM\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"eval_data\": \"LIBERO-Spatial\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"log_path\": \"/root/runs/acr-vla-conformal-refinement/eval-supp-spatial-adapt-tau025-s45.log\", \"pid\": \"502821\", \"tmux_session\": \"eval-supp-spatial-adapt-tau025-s45\"}, \"reproduce\": {\"finished_at\": \"2026-05-24T01:30:45.031Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T01:31:11.421Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-24T01:31:34.981793+00:00\"}]}, \"metrics\": {\"success_rate\": 80, \"successes\": 160, \"total\": 200, \"trigger_rate\": 20, \"mean_unc\": 0.1863}}, \"eval-supp-spatial-k2mean-s45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T22:59:42.673Z\", \"updated_at\": \"2026-05-24T03:18:33.793Z\", \"hypothesis\": \"K=2 mean baseline on Spatial suite seed45. Fourth seed extending Spatial K2mean. Fills Table 1 gap.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode vla_only --baseline_mode mean --K 2 --seed 45 --n_rollouts 20 --output_file logs/eval_spatial_k2mean_seed45.json\", \"server\": \"bjb2-40593\", \"gpu\": \"cuda:0\", \"seed\": 45, \"model_name\": \"SmolVLA-K2mean\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"eval_data\": \"LIBERO-Spatial\", \"log_path\": \"/tmp/eval_spatial_k2mean_s45.log\", \"pid\": \"204339\", \"tmux_session\": \"eval-spatial-k2mean-s45\"}, \"reproduce\": {\"finished_at\": \"2026-05-24T02:24:07.695Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T02:24:17.037Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-24T02:24:30.281933+00:00\"}]}, \"metrics\": {\"success_rate\": 80, \"successes\": 160, \"total\": 200}}, \"eval-supp-spatial-vla-only-s46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T00:34:46.225Z\", \"updated_at\": \"2026-05-24T03:18:27.488Z\", \"hypothesis\": \"Spatial VLA-only baseline seed46. Fifth seed for Spatial VLA-only variance analysis. 3-seed mean 78.7%±0.3%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark spatial --mode vla_only --seed 46 --n_rollouts 20 --K 1\", \"server\": \"cqa1-32758\", \"gpu\": \"cuda:1\", \"seed\": 46, \"model_name\": \"SmolVLA\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"eval_data\": \"LIBERO-Spatial\", \"log_path\": \"/tmp/eval_spatial_vla_s46.log\", \"pid\": 604290, \"tmux_session\": \"eval-spatial-vla-s46\", \"checkpoint_path\": \"n/a-eval-only\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 80.5, \"successes\": 161, \"total\": 200}, \"completed_at\": \"2026-05-24T03:18:27.488Z\"}, \"eval-supp-spatial-reconvla-s46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T00:52:50.566Z\", \"updated_at\": \"2026-05-24T03:18:20.676Z\", \"hypothesis\": \"Reconvla K=10 argmin on Spatial suite seed46. Fifth seed extending Spatial Reconvla coverage. 3-seed mean ~80%. Completes 5-seed variance analysis.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark spatial --mode reconvla --seed 46 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"cqa1-32758\", \"gpu\": \"cuda:5\", \"seed\": 46, \"model_name\": \"SmolVLA-Reconvla\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"eval_data\": \"LIBERO-Spatial\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"log_path\": \"/tmp/eval_spatial_reconvla_s46.log\", \"pid\": 588065, \"tmux_session\": \"eval-spatial-reconvla-s46\", \"checkpoint_path\": \"n/a-eval-only\"}, \"reproduce\": {\"finished_at\": \"2026-05-24T03:11:43.991Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T03:11:47.278Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-24T03:12:11.839484+00:00\"}]}, \"metrics\": {\"success_rate\": 80, \"successes\": 160, \"total\": 200}}, \"eval-supp-spatial-adapt-tau025-s46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T23:45:59.585Z\", \"updated_at\": \"2026-05-24T03:18:17.471Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Spatial suite seed46. Fifth seed extending Spatial Adaptive for variance analysis. 3-seed mean 80.8%±1.1%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark spatial --mode adaptive_conformal_crm --seed 46 --n_rollouts 20 --max_correction_norm 0.2 --conformal_threshold 0.25 --K 2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"cqa1-32758\", \"gpu\": \"cuda:2\", \"seed\": 46, \"model_name\": \"SmolVLA+AdaptiveCRM\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"eval_data\": \"LIBERO-Spatial\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"log_path\": \"/tmp/eval_spatial_adapt_s46.log\", \"pid\": \"560487\", \"tmux_session\": \"eval-spatial-adapt-s46\", \"checkpoint_path\": \"n/a-eval-only\"}, \"reproduce\": {\"finished_at\": \"2026-05-24T02:49:42.792Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T02:49:58.451Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-24T02:50:24.619028+00:00\"}]}, \"metrics\": {\"success_rate\": 80, \"successes\": 160, \"total\": 200, \"trigger_rate\": 19.9, \"mean_unc\": 0.1846}}, \"eval-supp-spatial-crm-norm005-s46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T00:22:31.743Z\", \"updated_at\": \"2026-05-24T03:18:14.133Z\", \"hypothesis\": \"CRM always-on norm=0.05 on Spatial suite seed46. Fifth seed for Spatial CRM variance analysis. 3-seed mean ~79.8%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 46 --n_rollouts 20 --max_correction_norm 0.05 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"cqa1-32758\", \"gpu\": \"cuda:0\", \"seed\": 46, \"model_name\": \"SmolVLA+CRM\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"eval_data\": \"LIBERO-Spatial\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"log_path\": \"/tmp/eval_spatial_crm_s46.log\", \"pid\": \"590633\", \"tmux_session\": \"eval-spatial-crm-s46\", \"checkpoint_path\": \"n/a-eval-only\"}, \"reproduce\": {\"finished_at\": \"2026-05-24T03:13:31.853Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T03:13:20.027Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-24T03:14:42.489012+00:00\"}]}, \"metrics\": {\"success_rate\": 81, \"successes\": 162, \"total\": 200}}, \"eval-supp-long-crm-norm005-s45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T20:12:50.126Z\", \"updated_at\": \"2026-05-24T00:54:53.307Z\", \"hypothesis\": \"CRM norm=0.05 always-on on Long suite seed45. Fourth seed for Long CRM validation.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark long --mode crm_obs_only --seed 45 --n_rollouts 20 --max_correction_norm 0.05 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:3\", \"seed\": 45, \"model_name\": \"SmolVLA+CRM\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"crm_unified_4suite_r4/crm_best.pt\", \"log_path\": \"/tmp/eval_long_crm_s45.log\"}, \"checkpoint_path\": \"n/a-eval-only\", \"metrics\": {\"SR\": 0.605, \"successes\": 121, \"total\": 200}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T00:54:53.307Z\"}, \"eval-supp-long-adapt-tau025-s45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T20:12:41.239Z\", \"updated_at\": \"2026-05-24T00:53:11.757Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Long suite seed45. Fourth seed for Long Adaptive validation.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark long --mode adaptive_conformal_crm --seed 45 --n_rollouts 20 --max_correction_norm 0.2 --conformal_threshold 0.25 --K 2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:2\", \"seed\": 45, \"model_name\": \"SmolVLA+CRM\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"crm_unified_4suite_r4/crm_best.pt\", \"log_path\": \"/tmp/eval_long_adapt_s45.log\"}, \"checkpoint_path\": \"n/a-eval-only\", \"metrics\": {\"SR\": 0.6, \"successes\": 120, \"total\": 200}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T00:53:11.757Z\"}, \"eval-supp-long-vla-only-s45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T20:12:32.639Z\", \"updated_at\": \"2026-05-24T00:53:04.280Z\", \"hypothesis\": \"Long VLA-only baseline seed45. Fourth seed for Long baseline. s42=58.0%, s43=59.5%, s44=56.5%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark long --mode vla_only --seed 45 --n_rollouts 20 --K 1\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:1\", \"seed\": 45, \"model_name\": \"SmolVLA\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"eval_data\": \"LIBERO-Long\", \"log_path\": \"/tmp/eval_long_vla_s45.log\"}, \"checkpoint_path\": \"n/a-eval-only\", \"metrics\": {\"SR\": 0.575, \"successes\": 115, \"total\": 200}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T00:53:04.280Z\"}, \"eval-supp-spatial-reconvla-s45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T21:31:16.039Z\", \"updated_at\": \"2026-05-24T00:30:53.206Z\", \"hypothesis\": \"Reconvla K=10 on Spatial suite seed45. Fourth seed extending Spatial Reconvla. 3-seed: 79.8%±1.0%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark spatial --mode reconvla --seed 45 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"cqa1-32758\", \"gpu\": \"cuda:5\", \"seed\": 45, \"model_name\": \"SmolVLA-Reconvla\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"eval_data\": \"LIBERO-Spatial\", \"checkpoint_source\": \"crm_smolvla_3suite_v1/crm_best.pt\", \"log_path\": \"/tmp/eval_spatial_reconvla_s45.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-24T00:24:14.738Z\"}, \"failure_reason\": \"FALSE POSITIVE: cron误判，实验实际正常完成。评估脚本不使用W&B/sentinel，输出到JSON文件。\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T00:24:09.035Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-24T00:25:20.596327+00:00\"}]}, \"metrics\": {\"success_rate\": 79.5, \"successes\": 159, \"total\": 200}, \"notes\": \"Cron false positive — eval script completed normally with 79.5% (159/200). Results at logs/eval_spatial_reconvla_seed45.json on cqa1-32758. No W&B/sentinel used by eval scripts.\"}, \"eval-supp-goal-k2mean-s45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T21:31:04.113Z\", \"updated_at\": \"2026-05-24T00:21:09.215Z\", \"hypothesis\": \"K=2 mean baseline on Goal suite seed45. Matched-seed companion for Goal s45 4-seed extension.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark goal --mode vla_only --baseline_mode mean --K 2 --seed 45 --n_rollouts 20 --output_file logs/eval_goal_k2mean_seed45.json\", \"server\": \"cqa1-32758\", \"gpu\": \"cuda:0\", \"seed\": 45, \"model_name\": \"SmolVLA-K2mean\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"eval_data\": \"LIBERO-Goal\", \"log_path\": \"/tmp/eval_goal_k2mean_s45.log\", \"checkpoint_path\": \"n/a-eval-only\"}, \"metrics\": {\"SR\": 0.81, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.7, \"put_the_bowl_on_the_stove\": 0.95, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.85, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.6, \"put_the_bowl_on_top_of_the_cabinet\": 0.95, \"push_the_plate_to_the_front_of_the_stove\": 0.95, \"put_the_cream_cheese_in_the_bowl\": 0.55, \"turn_on_the_stove\": 0.95, \"put_the_bowl_on_the_plate\": 0.9, \"put_the_wine_bottle_on_the_rack\": 0.7}}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-24T00:21:09.216Z\"}, \"eval-supp-adapt-tau025-obj-s45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T17:26:59.880Z\", \"updated_at\": \"2026-05-23T23:45:46.677Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Object suite seed45. Extends Object Adaptive coverage. Trigger rate expected ~3-5% on Object tasks.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark object --mode adaptive_conformal_crm --seed 45 --n_rollouts 20 --max_correction_norm 0.2 --conformal_threshold 0.25 --K 2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"pid\": 849131, \"tmux_session\": \"eval-supp-adapt-tau025-obj-s45\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau025-obj-s45.log\", \"seed\": 45, \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"smolvla+crm_3suite_v1\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark\"}, \"metrics\": {\"SR\": 0.78}, \"checkpoint_path\": \"N/A (eval only)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T20:26:31.521Z\"}, \"eval-supp-obj-k2mean-s45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T22:37:29.185Z\", \"updated_at\": \"2026-05-23T23:45:41.402Z\", \"hypothesis\": \"K=2 mean baseline on Object suite seed45. Duplicate of eval-supp-k2mean-obj-s45 (already DONE SR=77.5%). Killed to free GPU.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode mean --K 2 --seed 45 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": \"cuda:2\", \"seed\": 45, \"model_name\": \"smolvla\", \"data_path\": \"libero_object\", \"data_count\": 20, \"log_path\": \"logs/eval-obj-k2mean-s45.log\", \"checkpoint_path\": \"n/a-eval-only\", \"eval_data\": \"libero_object\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-23T23:45:23.930Z\"}, \"eval-supp-crm-obj-s46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T23:41:43.001Z\", \"updated_at\": \"2026-05-23T23:43:24.974Z\", \"hypothesis\": \"CRM always-on norm=0.05 on Object suite seed46. Fifth seed extending Object CRM. Previous seeds show ~79-81% range.\", \"metrics\": {\"overall_sr\": 0.795, \"per_task\": {\"alphabet_soup\": 0.8, \"cream_cheese\": 0.7, \"salad_dressing\": 0.75, \"bbq_sauce\": 0.8, \"ketchup\": 0.7, \"tomato_sauce\": 0.75, \"butter\": 0.75, \"milk\": 0.85, \"chocolate_pudding\": 0.95, \"orange_juice\": 0.9}}, \"checkpoint_path\": \"n/a-eval-only\", \"log_path\": \"/tmp/eval_crm_obj_s46.log\", \"conclusion\": \"success\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark object --mode crm_obs_only --seed 46 --n_rollouts 20 --max_correction_norm 0.05 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:0\", \"seed\": 46, \"model_name\": \"SmolVLA+CRM\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"eval_data\": \"LIBERO-Object\", \"checkpoint_source\": \"crm_smolvla_3suite_v1/crm_best.pt\", \"log_path\": \"/tmp/eval_crm_obj_s46.log\", \"checkpoint_path\": \"n/a-eval-only\"}, \"completed_at\": \"2026-05-23T23:43:24.974Z\"}, \"eval-supp-spatial-adapt-tau025-s45\": {\"status\": \"DEPLOYED\", \"retry_count\": 0, \"created_at\": \"2026-05-23T22:23:46.061Z\", \"updated_at\": \"2026-05-23T23:42:01.475Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Spatial suite seed45. Re-deployed after prior kills. Validates Adaptive improvement on Spatial (3-seed mean +2.1pp over VLA-only 78.7%).\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode adaptive_conformal_crm --seed 45 --n_rollouts 20 --max_correction_norm 0.2 --conformal_threshold 0.25 --K 2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"cqa1-32758\", \"gpu\": \"cuda:4\", \"seed\": 45, \"model_name\": \"SmolVLA+AdaptiveCRM\", \"data_path\": \"LIBERO-Spatial\", \"data_count\": 200, \"eval_data\": \"LIBERO-Spatial\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"log_path\": \"/root/runs/acr-vla-conformal-refinement/eval-supp-spatial-adapt-tau025-s45.log\", \"pid\": \"502821\", \"tmux_session\": \"eval-supp-spatial-adapt-tau025-s45\"}, \"conclusion\": \"killed\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/tmp/eval_spatial_adapt_s45.log\", \"completed_at\": \"2026-05-23T23:00:23.343Z\"}, \"eval-supp-long-k2mean-s44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T17:26:25.473Z\", \"updated_at\": \"2026-05-23T23:04:07.248Z\", \"hypothesis\": \"Long K=2 mean baseline seed44. Third seed for Long K=2 mean validation. Isolates multi-sample averaging on long-horizon tasks.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark long --mode vla_only --seed 44 --n_rollouts 20 --K 2 --baseline_mode mean\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:5\"], \"pid\": 850410, \"tmux_session\": \"eval-supp-long-k2mean-s44\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-k2mean-s44.log\", \"seed\": 44, \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA-K2mean\"}, \"conclusion\": \"negative\", \"metrics\": {\"SR\": 0.545, \"successes\": 109, \"total\": 200}, \"checkpoint_path\": \"n/a-eval-only\", \"completed_at\": \"2026-05-23T23:04:07.248Z\"}, \"eval-supp-long-reconvla-s44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T17:26:31.761Z\", \"updated_at\": \"2026-05-23T23:04:01.262Z\", \"hypothesis\": \"Long Reconvla K=10 seed44. Third seed for Long Reconvla 3-seed validation. s42=56.5% (below VLA-only 58.0%).\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark long --mode reconvla --seed 44 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": 849677, \"tmux_session\": \"eval-supp-long-reconvla-s44\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-reconvla-s44.log\", \"seed\": 44, \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"smolvla-reconvla-k10\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"eval_data\": \"LIBERO Long benchmark\"}, \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.57, \"successes\": 114, \"total\": 200}, \"checkpoint_path\": \"n/a-eval-only\", \"completed_at\": \"2026-05-23T23:04:01.262Z\"}, \"eval-supp-k2mean-spatial-s45\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T23:02:16.008Z\", \"updated_at\": \"2026-05-23T23:02:16.008Z\", \"hypothesis\": \"K=2 mean baseline (vla_only, 2-sample average) on Spatial suite seed45. Fourth seed completing Spatial k2mean coverage (s42=negative, s43/s44=done). Isolates multi-sample averaging effect.\"}, \"eval-supp-goal-reconvla-s45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T20:28:38.416Z\", \"updated_at\": \"2026-05-23T22:57:24.122Z\", \"hypothesis\": \"Reconvla K=10 on Goal suite seed45. Fourth seed extending Goal Reconvla. 3-seed mean: 80.8%±0.3%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark goal --mode reconvla --seed 45 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:2\", \"seed\": 45, \"model_name\": \"SmolVLA-Reconvla\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"eval_data\": \"LIBERO-Goal\", \"checkpoint_source\": \"crm_smolvla_3suite_v1/crm_best.pt\", \"log_path\": \"/tmp/eval_goal_reconvla_s45.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-23T22:51:19.786Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T22:51:57.320Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-23T22:52:47.068876+00:00\"}]}, \"metrics\": {\"SR\": 0.855}, \"notes\": \"实际成功完成。进程正常退出但无 W&B sentinel，cron 误判。日志确认 85.5% (171/200)。结果文件: logs/eval_goal_reconvla_seed45.json\"}, \"eval-supp-goal-vla-only-s45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T20:28:29.087Z\", \"updated_at\": \"2026-05-23T22:57:20.913Z\", \"hypothesis\": \"Goal VLA-only baseline seed45. Fourth seed extending Goal baseline. Matched-seed companion for Goal Adaptive s45.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark goal --mode vla_only --seed 45 --n_rollouts 20 --K 1\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:0\", \"seed\": 45, \"model_name\": \"SmolVLA\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"eval_data\": \"LIBERO-Goal\", \"log_path\": \"/tmp/eval_goal_vla_s45.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-23T22:49:51.524Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T22:50:08.101Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-23T22:50:32.862179+00:00\"}]}, \"metrics\": {\"SR\": 0.835}, \"notes\": \"实际成功完成。进程正常退出但无 W&B sentinel，cron 误判。日志确认 83.5% (167/200)。结果文件: logs/eval_goal_vla_only_seed45.json\"}, \"eval-supp-crm-norm005-obj-s46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T20:12:20.093Z\", \"updated_at\": \"2026-05-23T22:57:13.555Z\", \"hypothesis\": \"CRM always-on norm=0.05 on Object suite seed46. Fills the last Object s46 method gap.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark object --mode crm_obs_only --seed 46 --n_rollouts 20 --max_correction_norm 0.05 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:0\", \"seed\": 46, \"model_name\": \"SmolVLA+CRM\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"eval_data\": \"LIBERO-Object\", \"checkpoint_source\": \"crm_smolvla_3suite_v1/crm_best.pt\", \"log_path\": \"/tmp/eval_crm_obj_s46.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-23T22:44:05.941Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T22:44:22.428Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-23T22:44:45.646722+00:00\"}]}, \"metrics\": {\"SR\": 0.795}, \"notes\": \"实际成功完成。进程正常退出但无 W&B sentinel，cron 误判为 failed。日志确认 79.5% (159/200)。结果文件: logs/eval_object_crm_obs_only_norm0.05_seed46.json\"}, \"eval-supp-goal-crm-norm005-s45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T20:28:32.501Z\", \"updated_at\": \"2026-05-23T22:56:01.038Z\", \"hypothesis\": \"CRM always-on norm=0.05 on Goal suite seed45. Fourth seed extending Goal CRM. 3-seed mean: 83.7%±1.8%.\", \"spec\": {\"checkpoint_path\": \"logs/eval_goal_crm_obs_only_norm0.05_seed45.json\", \"log_path\": \"/tmp/eval_goal_crm_s45.log\"}, \"metrics\": {\"success_rate\": 81, \"successes\": 162, \"total\": 200}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T22:55:22.043Z\", \"notes\": \"实际成功完成。进程正常退出但无 W&B sentinel，cron 误判。日志确认 81.0% (162/200)。结果文件: logs/eval_goal_crm_obs_only_norm0.05_seed45.json\"}, \"eval-supp-crm-norm005-obj-s45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T18:15:28.966Z\", \"updated_at\": \"2026-05-23T22:37:07.655Z\", \"hypothesis\": \"CRM always-on norm=0.05 on Object suite seed45. Extends Object method coverage for 5-seed Adaptive variance investigation.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark object --mode crm_obs_only --seed 45 --n_rollouts 20 --max_correction_norm 0.05 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb2-40593\", \"gpu\": \"cuda:0\", \"seed\": 45, \"model_name\": \"SmolVLA+CRM\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"eval_data\": \"LIBERO-Object\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"log_path\": \"/tmp/eval_crm_obj_s45.log\"}, \"conclusion\": \"success\", \"metrics\": {\"SR\": 0.765}, \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-23T22:32:11.244Z\"}, \"eval-supp-reconvla-obj-s46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T18:41:19.029Z\", \"updated_at\": \"2026-05-23T22:31:59.949Z\", \"hypothesis\": \"Reconvla K=10 argmin on Object suite seed46. Extends Object method coverage for 5-seed variance analysis.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark object --mode reconvla --seed 46 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"cqa1-32758\", \"gpu\": \"cuda:2\", \"seed\": 46, \"model_name\": \"SmolVLA-Reconvla\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"eval_data\": \"LIBERO-Object\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"log_path\": \"/tmp/eval_reconvla_obj_s46.log\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.8, \"successes\": 160, \"total\": 200}, \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-23T22:31:59.949Z\"}, \"eval-supp-goal-adapt-tau025-s45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T20:13:06.213Z\", \"updated_at\": \"2026-05-23T22:31:49.469Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Goal suite seed45. Extends Goal Adaptive from 3-seed to 4-seed.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark goal --mode adaptive_conformal_crm --seed 45 --n_rollouts 20 --max_correction_norm 0.2 --conformal_threshold 0.25 --K 2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:5\", \"seed\": 45, \"model_name\": \"SmolVLA+CRM\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"eval_data\": \"LIBERO-Goal\", \"checkpoint_source\": \"crm_smolvla_3suite_v1/crm_best.pt\", \"log_path\": \"/tmp/eval_goal_adapt_s45.log\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.81, \"successes\": 162, \"total\": 200, \"trigger_rate\": 0.094, \"mean_unc\": 0.1493}, \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-23T22:31:49.469Z\"}, \"eval-supp-long-crm-norm005-s44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T14:44:35.159Z\", \"updated_at\": \"2026-05-23T21:28:56.768Z\", \"hypothesis\": \"CRM norm=0.05 always-on on Long suite seed44. Third seed for Long CRM 3-seed validation.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark long --mode crm_obs_only --seed 44 --n_rollouts 20 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt --K 10\", \"server\": \"cqa1-32758\", \"gpu\": 5, \"pid\": 291523, \"tmux_session\": \"eval-supp-long-crm-norm005-s44\", \"seed\": 44, \"model_name\": \"smolvla+crm_unified_4suite_r4\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"eval_data\": \"LIBERO long suite\", \"data_path\": \"LIBERO long suite (10 tasks)\", \"data_count\": 200}, \"metrics\": {\"SR\": 0.565}, \"checkpoint_path\": \"N/A (eval only)\", \"conclusion\": \"success\", \"log_path\": \"/tmp/eval_long_crm_norm005_s44.log\", \"completed_at\": \"2026-05-23T21:28:56.768Z\"}, \"eval-supp-long-adapt-tau025-s44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T14:44:32.204Z\", \"updated_at\": \"2026-05-23T21:28:50.765Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Long suite seed44. Third seed for Long Adaptive 3-seed validation. Long VLA-only s42=58.0%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark long --mode adaptive_conformal_crm --seed 44 --n_rollouts 20 --max_correction_norm 0.2 --conformal_threshold 0.25 --K 2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"cqa1-32758\", \"gpu\": 1, \"pid\": 291315, \"tmux_session\": \"eval-supp-long-adapt-tau025-s44\", \"seed\": 44, \"model_name\": \"smolvla+crm_unified_4suite_r4\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"eval_data\": \"LIBERO long suite\", \"data_path\": \"LIBERO long suite (10 tasks)\", \"data_count\": 200}, \"metrics\": {\"SR\": 0.56, \"trigger_rate\": 0.049}, \"checkpoint_path\": \"N/A (eval only)\", \"conclusion\": \"negative\", \"log_path\": \"/tmp/eval_long_adapt_tau025_s44.log\", \"completed_at\": \"2026-05-23T21:28:50.766Z\"}, \"eval-supp-k2mean-obj-s46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T17:56:58.207Z\", \"updated_at\": \"2026-05-23T21:28:27.870Z\", \"hypothesis\": \"K=2 mean baseline on Object suite seed46. Companion baseline for Object Adaptive s46 5-seed extension.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode mean --K 2 --seed 46 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": \"cuda:3\", \"seed\": 46, \"model_name\": \"SmolVLA-K2mean\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"eval_data\": \"LIBERO-Object\", \"log_path\": \"/tmp/eval_k2mean_obj_s46.log\"}, \"metrics\": {\"SR\": 0.765}, \"checkpoint_path\": \"N/A (eval only)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T21:28:27.870Z\"}, \"eval-supp-k2mean-obj-s45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T17:56:52.406Z\", \"updated_at\": \"2026-05-23T21:28:21.695Z\", \"hypothesis\": \"K=2 mean baseline on Object suite seed45. Companion baseline for Object Adaptive s45 5-seed extension.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode mean --K 2 --seed 45 --n_rollouts 20\", \"server\": \"cqa1-32758\", \"gpu\": \"cuda:0\", \"seed\": 45, \"model_name\": \"SmolVLA-K2mean\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"eval_data\": \"LIBERO-Object\", \"log_path\": \"/tmp/eval_k2mean_obj_s45.log\"}, \"metrics\": {\"SR\": 0.775}, \"checkpoint_path\": \"N/A (eval only)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T21:28:21.695Z\"}, \"eval-supp-adapt-tau025-obj-s46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T17:27:06.320Z\", \"updated_at\": \"2026-05-23T20:26:37.804Z\", \"hypothesis\": \"Object Adaptive τ=0.25 seed46. User-requested additional seed to assess Object Adaptive variance.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark object --mode adaptive_conformal_crm --seed 46 --n_rollouts 20 --max_correction_norm 0.2 --conformal_threshold 0.25 --K 2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"pid\": 849395, \"tmux_session\": \"eval-supp-adapt-tau025-obj-s46\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau025-obj-s46.log\", \"seed\": 46, \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"model_name\": \"smolvla+crm_3suite_v1\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark\"}, \"metrics\": {\"SR\": 0.775}, \"checkpoint_path\": \"N/A (eval only)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T20:26:37.804Z\"}, \"eval-supp-long-vla-only-s43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T11:55:45.292Z\", \"updated_at\": \"2026-05-23T20:21:04.060Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark long --mode vla_only --seed 43 --n_rollouts 20 --K 1\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"pid\": 849946, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-vla-only-s43.log\", \"submitted_at\": \"2026-05-23T11:56:02.350Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"tmux_session\": \"eval-supp-long-vla-only-s43\", \"seed\": 43, \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"wall_clock_seconds\": 30301.7, \"gpu_hours\": 8.42}, \"hypothesis\": \"VLA-only baseline on Long suite seed43. Duplicate deployment on bjb2-28827; primary results already harvested from cqa1 (SR=59.5%).\", \"checkpoint_path\": \"N/A (eval only, duplicate killed)\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-23T20:21:04.060Z\"}, \"eval-supp-long-k2mean-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T11:22:32.322Z\", \"updated_at\": \"2026-05-23T20:13:10.758Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --baseline_mode mean --K 2 --benchmark long --n_rollouts 20 --seed 42\", \"server\": \"cqa1-32758\", \"gpu\": [\"cuda:4\"], \"pid\": \"172246\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-k2mean-s42.log\", \"submitted_at\": \"2026-05-23T11:23:16.791Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 42, \"hypothesis\": \"K=2 mean baseline on LIBERO-Long seed42. Isolates multi-sample averaging effect on long-horizon tasks. Long VLA-only s42 running on bjb1-32546 provides baseline comparison.\", \"wall_clock_seconds\": 31794.0, \"gpu_hours\": 8.83}, \"checkpoint_path\": \"N/A (eval only)\", \"metrics\": {\"SR\": 0.57}, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-k2mean-s42.log\", \"conclusion\": \"negative\", \"hypothesis\": \"K=2 mean baseline on LIBERO-Long seed42. Isolates multi-sample averaging effect on long-horizon tasks. VLA-only s42=58.0% baseline.\", \"completed_at\": \"2026-05-23T20:13:10.758Z\"}, \"eval-supp-obj-vla-only-s46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T17:24:10.813Z\", \"updated_at\": \"2026-05-23T20:09:46.499Z\", \"hypothesis\": \"Object VLA-only baseline seed46. Companion baseline for Object Adaptive s46 comparison. 3-seed baseline: 77.8%±1.0%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python src/evaluate.py --benchmark object --mode vla_only --seed 46 --n_rollouts 20 --K 1\", \"server\": \"bjb1-32546\", \"seed\": 46, \"model_name\": \"smolvla\", \"gpu\": \"cuda:0\", \"tmux_session\": \"eval-supp-obj-vla-only-s46\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-supp-obj-vla-only-s46.log\", \"data_path\": \"LIBERO-object\", \"data_count\": 200}, \"metrics\": {\"SR\": 0.79}, \"checkpoint_path\": \"N/A (eval only)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T20:09:46.499Z\"}, \"eval-supp-long-vla-only-s44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T14:36:41.287Z\", \"updated_at\": \"2026-05-23T20:09:40.603Z\", \"hypothesis\": \"Long VLA-only baseline seed44. Second seed for Long baseline. s42=58.0%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python src/evaluate.py --benchmark long --mode vla_only --seed 44 --n_rollouts 20 --K 1\", \"server\": \"bjb1-32546\", \"seed\": 44, \"pid\": 997776, \"log_path\": \"/tmp/eval_long_vla_only_s44.log\", \"model_name\": \"SmolVLA\", \"data_path\": \"long_suite\", \"data_count\": 20}, \"metrics\": {\"SR\": 0.565}, \"checkpoint_path\": \"N/A (eval only)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T20:09:40.603Z\"}, \"eval-supp-long-k2mean-s43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T14:36:36.825Z\", \"updated_at\": \"2026-05-23T20:09:34.819Z\", \"hypothesis\": \"K=2 mean baseline on Long suite seed43. Isolates multi-sample averaging effect on Long tasks.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python src/evaluate.py --benchmark long --mode vla_only --seed 43 --n_rollouts 20 --K 2 --baseline_mode mean\", \"server\": \"bjb1-32546\", \"seed\": 43, \"pid\": 996158, \"log_path\": \"/tmp/eval_long_k2mean_s43.log\", \"model_name\": \"SmolVLA\", \"data_path\": \"long_suite\", \"data_count\": 20}, \"metrics\": {\"SR\": 0.56}, \"checkpoint_path\": \"N/A (eval only)\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-23T20:09:34.819Z\"}, \"eval-supp-long-reconvla-s43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T14:36:30.979Z\", \"updated_at\": \"2026-05-23T20:09:28.982Z\", \"hypothesis\": \"Reconvla K=10 argmin on Long suite seed43. Second seed for Long Reconvla validation.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python src/evaluate.py --benchmark long --mode reconvla --seed 43 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"bjb1-32546\", \"seed\": 43, \"pid\": 994675, \"log_path\": \"/tmp/eval_long_reconvla_s43.log\", \"model_name\": \"SmolVLA+CRM\", \"data_path\": \"long_suite\", \"data_count\": 20}, \"metrics\": {\"SR\": 0.59}, \"checkpoint_path\": \"N/A (eval only)\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-23T20:09:28.982Z\"}, \"eval-supp-long-crm-norm005-s43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T14:36:26.229Z\", \"updated_at\": \"2026-05-23T20:09:23.098Z\", \"hypothesis\": \"CRM norm=0.05 always-on on Long suite seed43. Second seed for Long CRM validation.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python src/evaluate.py --benchmark long --mode crm_obs_only --seed 43 --n_rollouts 20 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt --K 10\", \"server\": \"bjb1-32546\", \"seed\": 43, \"pid\": 993249, \"log_path\": \"/tmp/eval_long_crm_norm005_s43.log\", \"model_name\": \"SmolVLA+CRM\", \"data_path\": \"long_suite\", \"data_count\": 20}, \"metrics\": {\"SR\": 0.545}, \"checkpoint_path\": \"N/A (eval only)\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-23T20:09:23.098Z\"}, \"eval-supp-long-adapt-tau025-s43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T14:36:21.251Z\", \"updated_at\": \"2026-05-23T20:09:17.172Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Long suite seed43. Second seed for Long Adaptive validation. Long VLA-only s42=58.0%.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python src/evaluate.py --benchmark long --mode adaptive_conformal_crm --seed 43 --n_rollouts 20 --max_correction_norm 0.2 --conformal_threshold 0.25 --K 2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"bjb1-32546\", \"seed\": 43, \"pid\": 991960, \"log_path\": \"/tmp/eval_long_adapt_tau025_s43.log\", \"model_name\": \"SmolVLA+CRM\", \"data_path\": \"long_suite\", \"data_count\": 20}, \"metrics\": {\"SR\": 0.58, \"trigger_rate\": 0.045}, \"checkpoint_path\": \"N/A (eval only)\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-23T20:09:17.172Z\"}, \"eval-supp-obj-adapt-tau025-s45-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T17:55:59.154Z\", \"updated_at\": \"2026-05-23T18:16:04.202Z\", \"hypothesis\": \"Retry of eval-supp-obj-adapt-tau025-s45. Object Adaptive CRM τ=0.25 seed45 on bjb2-40593 after fixing missing CRM checkpoint.\", \"parent\": \"eval-supp-obj-adapt-tau025-s45\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark object --mode adaptive_conformal_crm --seed 45 --n_rollouts 20 --max_correction_norm 0.2 --conformal_threshold 0.25 --K 2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"server\": \"bjb2-40593\", \"gpu\": \"cuda:0\", \"seed\": 45, \"model_name\": \"SmolVLA+AdaptiveCRM\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"log_path\": \"/tmp/eval_obj_adapt_s45_r2.log\"}, \"checkpoint_path\": \"N/A (killed, replaced by CRM s45)\", \"log_path\": \"/tmp/eval_obj_adapt_s45_r2.log\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-23T18:16:04.202Z\"}, \"eval-supp-long-crm-norm005-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T09:56:44.431Z\", \"updated_at\": \"2026-05-23T17:25:47.737Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt --benchmark long --seed 42 --n_rollouts 20 --max_correction_norm 0.05\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:5\"], \"pid\": \"712378\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-crm-norm005-s42.log\", \"submitted_at\": \"2026-05-23T09:57:35.905Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"smolvla-crm-norm005\", \"seed\": 42, \"wall_clock_seconds\": 26891.8, \"gpu_hours\": 7.47}, \"hypothesis\": \"CRM always-on norm=0.05 on LIBERO-Long seed42 using 4-suite CRM checkpoint. CRM improved Spatial (79.8% vs 78.5% VLA-only) but hurt Goal (-12pp). Tests CRM effect on challenging long-horizon tasks.\", \"metrics\": {\"overall_sr\": 0.565}, \"conclusion\": \"negative\", \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-23T17:25:47.737Z\"}, \"eval-supp-long-adapt-tau025-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T09:56:38.730Z\", \"updated_at\": \"2026-05-23T17:25:41.523Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt --conformal_threshold 0.25 --benchmark long --seed 42 --n_rollouts 20 --max_correction_norm 0.2 --K 2\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"pid\": \"711770\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-adapt-tau025-s42.log\", \"submitted_at\": \"2026-05-23T09:57:28.057Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"smolvla-adaptive-crm-tau025\", \"seed\": 42, \"wall_clock_seconds\": 26893.5, \"gpu_hours\": 7.47}, \"hypothesis\": \"Adaptive conformal CRM tau=0.25 on LIBERO-Long seed42 using 4-suite CRM checkpoint. Adaptive method achieved best Spatial results (82.0% vs 78.5% VLA-only). Tests if selective CRM application benefits long-horizon tasks.\", \"metrics\": {\"overall_sr\": 0.59, \"trigger_rate\": 0.039, \"tau\": 0.25, \"crm_applied_steps\": 2785, \"total_steps\": 71980}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-23T17:25:41.523Z\"}, \"eval-supp-long-reconvla-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T09:56:33.117Z\", \"updated_at\": \"2026-05-23T17:25:32.561Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode reconvla --K 10 --benchmark long --seed 42 --n_rollouts 20\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"711479\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-reconvla-s42.log\", \"submitted_at\": \"2026-05-23T09:57:18.522Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"smolvla-reconvla-k10\", \"seed\": 42, \"wall_clock_seconds\": 26894.0, \"gpu_hours\": 7.47}, \"hypothesis\": \"Reconvla K=10 argmin on LIBERO-Long seed42. Tests if reconstruction-based action selection benefits long-horizon tasks. Reconvla achieved 80% on Spatial (vs 78.5% VLA-only) and 79% on Object (vs 77.8% VLA-only).\", \"metrics\": {\"overall_sr\": 0.565}, \"conclusion\": \"negative\", \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-23T17:25:32.561Z\"}}, \"count\": 100, \"total\": 889, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.9861}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-24T08:24:51.425Z_

<details><summary>↩ Tool result · `toolu_01PK6vcAY4qpy8iQkAXn8K9F`</summary>

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
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "bf26cf7a-5b0f-41b0-aacd-2a34ca835675",
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

### Assistant

_source line 25_

<details><summary>Logged reasoning block</summary>

```text
Let me search for the lerobot experiments in the registry file, and use ssh_execute for tmux on bjb2-28827.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "466939bc-a251-4eb7-ba20-cd300bb33d82",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ReHShhorhTBpeDrNCVjvm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 988,
      "cache_read_input_tokens": 36282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 988
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

<details open><summary>🔧 Tool call — Bash · `toolu_01Hshue19eHddFDSKQJwxz9W`</summary>

```json
{
  "command": "grep -i \"lerobot\" /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/4a8246d3-c96e-4959-82ff-767c57b966c8/tool-results/mcp-agent-ml-research-read_registry-1779611091392.txt | head -20",
  "description": "Search for lerobot experiments in registry dump"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "e811dfc6-71fa-4931-a1f8-e41555c06b5d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ReHShhorhTBpeDrNCVjvm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 988,
      "cache_read_input_tokens": 36282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 988
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

_source line 27 · 2026-05-24T08:24:57.792Z_

<details><summary>↩ Tool result · `toolu_01Hshue19eHddFDSKQJwxz9W`</summary>

```text
&lt;persisted-output>
Output too large (114.7KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/4a8246d3-c96e-4959-82ff-767c57b966c8/tool-results/bh6umo280.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-supp-long-k2mean-s46\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T03:23:24.189Z\", \"updated_at\": \"2026-05-24T08:15:23.138Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark long --mode vla_only --baseline_mode mean --K 2 --seed 46 --n_rollouts 20 --output_file logs/eval_long_k2mean_seed46.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": 263191, \"log_path\": \"logs/eval_long_k2mean_seed46.json\", \"submitted_at\": \"2026-05-24T03:23:22.142Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Long\", \"data_count\": 200, \"model_name\": \"SmolVLA\", \"seed\": 46, \"eval_data\": \"LIBERO-Long\", \"checkpoint_source\": \"n/a-baseline\"}, \"hypothesis\": \"VLA-only K=2 mean baseline on LIBERO-Long suite seed46 provides the fifth seed for Long K2-mean variance analysis, establishing the unrefined baseline performance across seeds.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.55, \"successes\": 110, \"total\": 200, \"source\": \"json_harvest_bjb1-32546\"}}, \"eval-supp-long-crm-norm005-s46\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T00:55:34.833Z\", \"updated_at\": \"2026-05-24T08:15:19.358Z\", \"hypothesis\": \"CRM obs-only refinement with max_correction_norm=0.05 on LIBERO-Long suite seed46 provides the fifth seed for Long CRM obs-only variance analysis, testing conservative correction magnitude across seeds.\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark long --mode crm_obs_only --seed 46 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": 262247, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-supp-long-crm-norm005-s46.log\", \"submitted_at\": \"2
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
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "be86e60b-434e-4ff4-bebe-6c46b071aeac",
  "tool_use_result": {
    "stdout": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"eval-supp-long-k2mean-s46\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T03:23:24.189Z\\\", \\\"updated_at\\\": \\\"2026-05-24T08:15:23.138Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --benchmark long --mode vla_only --baseline_mode mean --K 2 --seed 46 --n_rollouts 20 --output_file logs/eval_long_k2mean_seed46.json\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"pid\\\": 263191, \\\"log_path\\\": \\\"logs/eval_long_k2mean_seed46.json\\\", \\\"submitted_at\\\": \\\"2026-05-24T03:23:22.142Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"LIBERO-Long\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 46, \\\"eval_data\\\": \\\"LIBERO-Long\\\", \\\"checkpoint_source\\\": \\\"n/a-baseline\\\"}, \\\"hypothesis\\\": \\\"VLA-only K=2 mean baseline on LIBERO-Long suite seed46 provides the fifth seed for Long K2-mean variance analysis, establishing the unrefined baseline performance across seeds.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.55, \\\"successes\\\": 110, \\\"total\\\": 200, \\\"source\\\": \\\"json_harvest_bjb1-32546\\\"}}, \\\"eval-supp-long-crm-norm005-s46\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T00:55:34.833Z\\\", \\\"updated_at\\\": \\\"2026-05-24T08:15:19.358Z\\\", \\\"hypothesis\\\": \\\"CRM obs-only refinement with max_correction_norm=0.05 on LIBERO-Long suite seed46 provides the fifth seed for Long CRM obs-only variance analysis, testing conservative correction magnitude across seeds.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --benchmark long --mode crm_obs_only --seed 46 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": 262247, \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-supp-long-crm-norm005-s46.log\\\", \\\"submitted_at\\\": \\\"2026-05-24T03:23:09.570Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"LIBERO-Long\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 46, \\\"eval_data\\\": \\\"LIBERO-Long\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.54, \\\"successes\\\": 108, \\\"total\\\": 200, \\\"source\\\": \\\"json_harvest_bjb1-32546\\\"}}, \\\"eval-supp-long-reconvla-s46\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T00:55:40.981Z\\\", \\\"updated_at\\\": \\\"2026-05-24T08:06:46.631Z\\\", \\\"hypothesis\\\": \\\"ReconVLA evaluation on LIBERO-Long suite seed46 provides the fifth seed for Long ReconVLA variance analysis, measuring reconstruction-based refinement consistency across seeds.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --benchmark long --mode reconvla --seed 46 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"pid\\\": 262529, \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-supp-long-reconvla-s46.log\\\", \\\"submitted_at\\\": \\\"2026-05-24T03:23:15.265Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"LIBERO-Long\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 46, \\\"eval_data\\\": \\\"LIBERO-Long\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.56, \\\"successes\\\": 112, \\\"total\\\": 200, \\\"source\\\": \\\"json_harvest_bjb1-32546\\\"}}, \\\"eval-supp-long-adapt-tau025-s46\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T00:55:46.960Z\\\", \\\"updated_at\\\": \\\"2026-05-24T08:05:01.126Z\\\", \\\"hypothesis\\\": \\\"Adaptive CRM with τ=0.25 on LIBERO-Long suite seed46 provides the fifth seed for Long Adaptive variance analysis, testing whether adaptive conformal refinement consistently improves over baselines across seeds.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --benchmark long --mode adaptive_conformal_crm --seed 46 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --max_correction_norm 0.2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": 261974, \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-supp-long-adapt-tau025-s46.log\\\", \\\"submitted_at\\\": \\\"2026-05-24T03:23:03.745Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"LIBERO-Long\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 46, \\\"eval_data\\\": \\\"LIBERO-Long\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\\\", \\\"wall_clock_seconds\\\": 16917.4, \\\"gpu_hours\\\": 4.7}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.585, \\\"successes\\\": 117, \\\"total_rollouts\\\": 200, \\\"benchmark\\\": \\\"long\\\", \\\"mode\\\": \\\"adaptive_conformal_crm\\\", \\\"seed\\\": 46, \\\"K\\\": 10, \\\"max_correction_norm\\\": 0.2, \\\"conformal_threshold\\\": 0.25}, \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_long_adaptive_conformal_crm_norm0.2_tau0.25_seed46.json\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\\\", \\\"completed_at\\\": \\\"2026-05-24T08:05:01.126Z\\\"}, \\\"eval-supp-k2mean-spatial-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T07:15:55.833Z\\\", \\\"updated_at\\\": \\\"2026-05-24T07:18:30.230Z\\\", \\\"hypothesis\\\": \\\"K=2 mean baseline on Spatial suite seed47. Sixth seed extending variance analysis. 5-seed mean ~80%.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark spatial --mode vla_only --baseline_mode mean --K 2 --seed 47 --n_rollouts 20\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"tmux_session\\\": \\\"spatial-k2mean-s47\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 47, \\\"eval_data\\\": \\\"LIBERO-Spatial 10 tasks x 20 rollouts\\\", \\\"checkpoint_source\\\": \\\"n/a-baseline\\\"}}, \\\"eval-supp-reconvla-spatial-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T07:15:47.910Z\\\", \\\"updated_at\\\": \\\"2026-05-24T07:18:23.847Z\\\", \\\"hypothesis\\\": \\\"Reconvla K=10 on Spatial suite seed47. Sixth seed extending variance analysis. 5-seed mean ~80%.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark spatial --mode reconvla --seed 47 --n_rollouts 20 --K 10\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"tmux_session\\\": \\\"spatial-reconvla-s47\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA+Reconvla\\\", \\\"seed\\\": 47, \\\"eval_data\\\": \\\"LIBERO-Spatial 10 tasks x 20 rollouts\\\", \\\"checkpoint_source\\\": \\\"n/a-reconvla\\\"}}, \\\"eval-supp-adapt-tau025-spatial-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T07:15:43.884Z\\\", \\\"updated_at\\\": \\\"2026-05-24T07:18:17.441Z\\\", \\\"hypothesis\\\": \\\"Adaptive CRM tau=0.25 on Spatial suite seed47. Sixth seed extending variance analysis. 5-seed mean ~80.5%.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark spatial --mode adaptive_conformal_crm --seed 47 --n_rollouts 20 --K 10 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"tmux_session\\\": \\\"spatial-adapt-s47\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA+Adaptive CRM\\\", \\\"seed\\\": 47, \\\"eval_data\\\": \\\"LIBERO-Spatial 10 tasks x 20 rollouts\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\"}}, \\\"eval-supp-vla-only-spatial-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T07:15:40.347Z\\\", \\\"updated_at\\\": \\\"2026-05-24T07:18:10.979Z\\\", \\\"hypothesis\\\": \\\"VLA-only baseline on Spatial suite seed47. Sixth seed extending variance analysis. 5-seed mean ~78.7%.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode vla_only --seed 47 --n_rollouts 20 --K 1\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"tmux_session\\\": \\\"spatial-vla-s47\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 47, \\\"eval_data\\\": \\\"LIBERO-Spatial 10 tasks x 20 rollouts\\\", \\\"checkpoint_source\\\": \\\"n/a-baseline\\\"}}, \\\"eval-supp-goal-vla-only-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T07:14:14.567Z\\\", \\\"updated_at\\\": \\\"2026-05-24T07:17:13.996Z\\\", \\\"hypothesis\\\": \\\"Goal s47 VLA-only (K=1) baseline to extend Goal seed coverage beyond s42-s46 for supplementary variance analysis.\\\", \\\"parent\\\": \\\"eval-supp-goal-vla-only-s46\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark goal --mode vla_only --seed 47 --n_rollouts 20 --K 1\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"pid\\\": 279117, \\\"tmux_session\\\": \\\"goal-vla-s47\\\", \\\"log_path\\\": \\\"logs/eval-supp-goal-vla-only-s47.log\\\", \\\"data_path\\\": \\\"LIBERO-Goal\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 47, \\\"eval_data\\\": \\\"LIBERO-Goal\\\", \\\"checkpoint_source\\\": \\\"n/a-baseline\\\", \\\"checkpoint_path\\\": \\\"n/a-eval-only\\\"}}, \\\"eval-supp-long-vla-only-s47-r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T07:14:04.522Z\\\", \\\"updated_at\\\": \\\"2026-05-24T07:17:06.584Z\\\", \\\"hypothesis\\\": \\\"Long s47 VLA-only (K=1) baseline to complete the Long s47 seed extension set. The existing eval-supp-long-vla-only-s47 is actually k2mean (K=2 mean), so this fills the true VLA-only gap.\\\", \\\"parent\\\": \\\"eval-supp-long-vla-only-s46\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark long --mode vla_only --seed 47 --n_rollouts 20 --K 1\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": 278846, \\\"tmux_session\\\": \\\"long-vla-s47-r2\\\", \\\"log_path\\\": \\\"logs/eval-supp-long-vla-only-s47-r2.log\\\", \\\"data_path\\\": \\\"LIBERO-Long\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 47, \\\"eval_data\\\": \\\"LIBERO-Long\\\", \\\"checkpoint_source\\\": \\\"n/a-baseline\\\", \\\"checkpoint_path\\\": \\\"n/a-eval-only\\\"}}, \\\"eval-supp-adapt-tau025-spatial-s46\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T07:12:18.821Z\\\", \\\"updated_at\\\": \\\"2026-05-24T07:16:50.821Z\\\", \\\"hypothesis\\\": \\\"CRM/Adaptive on Spatial seed46, 5th seed extension\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark spatial --mode adaptive_conformal_crm --seed 46 --n_rollouts 20 --K 10 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"LIBERO spatial suite\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA + Adaptive CRM (crm_smolvla_3suite_v1)\\\", \\\"seed\\\": 46, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO spatial 10 tasks x 20 rollouts\\\"}, \\\"failure_reason\\\": \\\"GPU 1 occupied by OpenVLA VLA-only eval (PID 114990). Not actually started despite RUNNING status. Will deploy when GPU frees up.\\\"}, \\\"eval-supp-crm-norm005-spatial-s46\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T07:12:15.210Z\\\", \\\"updated_at\\\": \\\"2026-05-24T07:14:47.458Z\\\", \\\"hypothesis\\\": \\\"CRM/Adaptive on Spatial seed46, 5th seed extension\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 46 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"LIBERO spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"smolvla+crm_smolvla_3suite_v1\\\", \\\"seed\\\": 46, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO spatial 10 tasks x 20 rollouts\\\"}}, \\\"crm-train-openvla-k1-multiscale-object\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T06:32:56.953Z\\\", \\\"updated_at\\\": \\\"2026-05-24T07:09:37.983Z\\\", \\\"hypothesis\\\": \\\"Training the K=1 MultiScaleCRM architecture on OpenVLA's multi-scale Llama-7B features (4 layers × 4096-d, action_dim=6 single-step) will provide a learned conformal correction module for OpenVLA on LIBERO-Object, with the goal of improving over the OpenVLA VLA-only baseline (SR=69%). This differs from the prior train-crm-openvla-obs-only (K=10 obs-only architecture, eval SR=0%) by using the multi-scale attention fusion + action-conditioned gating from plan_700.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python -u src/train_crm_k1.py --benchmark object --cache_dir /root/autodl-tmp/crm_cache_k1_openvla --obs_dim 4096 --epochs 50 --batch_size 512 --lr 1e-3 --seed 42 --output_dir /root/autodl-tmp/checkpoints/crm_openvla_k1_multiscale/object --wandb_run_name crm-openvla-k1-multiscale-object --loss_mode multi\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/crm_cache_k1_openvla/object\\\", \\\"data_count\\\": 74507, \\\"model_name\\\": \\\"MultiScaleCRM-OpenVLA-K1\\\", \\\"seed\\\": 42}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"best_val_loss\\\": 0.077477, \\\"total_epochs\\\": 50, \\\"train_samples\\\": 74507, \\\"obs_dim\\\": 4096, \\\"params\\\": 908106, \\\"architecture\\\": \\\"MultiScaleCRM-K1\\\"}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/crm_openvla_k1_multiscale/object\\\", \\\"log_path\\\": \\\"/root/acr-vla-conformal-refinement/logs/crm-openvla-k1-multiscale-object.log\\\", \\\"completed_at\\\": \\\"2026-05-24T07:09:37.983Z\\\"}, \\\"eval-openvla-object-vla-only-seed42-v3\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T07:07:37.003Z\\\", \\\"updated_at\\\": \\\"2026-05-24T07:08:07.984Z\\\", \\\"hypothesis\\\": \\\"After fixing OpenVLA loading for transformers 5.8.1 (model_type 'openvla' auto-registration via openvla_compat + PrismaticImageProcessor workaround), VLA-only baseline on LIBERO-Object seed42 should reproduce the previously observed ~69% success rate from eval-openvla-object-vla-only-seed42-v2. Validates that the new loader path preserves model behavior bit-for-bit.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u src/openvla_eval.py --benchmark object --model_path /root/autodl-tmp/models/openvla-libero-object --mode vla_only --seed 42 --n_rollouts 20 --gpu 0 --output_file logs/eval_openvla_object_vla_only_seed42_v3.json\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/libero_data/libero_object\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"openvla-libero-object\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/models/openvla-libero-object\\\", \\\"eval_data\\\": \\\"LIBERO-Object (10 tasks x 20 rollouts = 200 episodes)\\\", \\\"pid\\\": \\\"114984\\\", \\\"log_path\\\": \\\"/tmp/eval_openvla_vla_only_seed42_v3.log\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/models/openvla-libero-object\\\"}}, \\\"eval-supp-long-k2mean-s46-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T06:34:16.953Z\\\", \\\"updated_at\\\": \\\"2026-05-24T07:06:31.785Z\\\", \\\"hypothesis\\\": \\\"K=2 mean baseline on Long suite seed46 (re-deploy after r1 failed on bjb1-32546). Fifth seed completing Long K2mean 5-seed coverage. Isolates multi-sample averaging on Long suite.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark long --mode vla_only --baseline_mode mean --K 2 --seed 46 --n_rollouts 20 --output_file logs/eval_long_k2mean_seed46.json\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"tmux_session\\\": \\\"long-k2mean-s46-r2\\\", \\\"log_path\\\": \\\"logs/eval-supp-long-k2mean-s46-r2.log\\\", \\\"data_path\\\": \\\"LIBERO-Long\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 46, \\\"eval_data\\\": \\\"LIBERO-Long\\\", \\\"checkpoint_source\\\": \\\"n/a-baseline\\\", \\\"parent\\\": \\\"eval-supp-long-k2mean-s46\\\"}, \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-24T07:06:31.785Z\\\"}, \\\"eval-supp-long-reconvla-s46-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T06:34:13.683Z\\\", \\\"updated_at\\\": \\\"2026-05-24T07:06:23.946Z\\\", \\\"hypothesis\\\": \\\"Reconvla K=10 on Long suite seed46 (re-deploy after r1 failed on bjb1-32546). Fifth seed completing Long Reconvla 5-seed coverage.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark long --mode reconvla --seed 46 --n_rollouts 20 --K 10\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"tmux_session\\\": \\\"long-reconvla-s46-r2\\\", \\\"log_path\\\": \\\"logs/eval-supp-long-reconvla-s46-r2.log\\\", \\\"data_path\\\": \\\"LIBERO-Long\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 46, \\\"eval_data\\\": \\\"LIBERO-Long\\\", \\\"checkpoint_source\\\": \\\"n/a-reconvla\\\", \\\"parent\\\": \\\"eval-supp-long-reconvla-s46\\\"}, \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-24T07:06:23.946Z\\\"}, \\\"eval-supp-long-crm-norm005-s46-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T06:34:10.482Z\\\", \\\"updated_at\\\": \\\"2026-05-24T07:06:15.932Z\\\", \\\"hypothesis\\\": \\\"CRM always-on norm=0.05 on Long suite seed46 (re-deploy after r1 failed on bjb1-32546). Fifth seed completing Long CRM 5-seed coverage. 3-seed mean 55.8%±1.2%.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark long --mode crm_obs_only --seed 46 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"tmux_session\\\": \\\"long-crm-s46-r2\\\", \\\"log_path\\\": \\\"logs/eval-supp-long-crm-norm005-s46-r2.log\\\", \\\"data_path\\\": \\\"LIBERO-Long\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 46, \\\"eval_data\\\": \\\"LIBERO-Long\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\\\", \\\"parent\\\": \\\"eval-supp-long-crm-norm005-s46\\\"}, \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-24T07:06:15.932Z\\\"}, \\\"eval-supp-long-adapt-tau025-s46-r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T06:34:07.178Z\\\", \\\"updated_at\\\": \\\"2026-05-24T07:06:09.666Z\\\", \\\"hypothesis\\\": \\\"Adaptive CRM tau=0.25 on Long suite seed46 (re-deploy after r1 failed on bjb1-32546 with python: command not found). Fifth seed completing Long Adaptive 5-seed coverage. 3-seed mean 57.7%±1.5%.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark long --mode adaptive_conformal_crm --seed 46 --n_rollouts 20 --K 2 --conformal_threshold 0.25 --max_correction_norm 0.2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"tmux_session\\\": \\\"long-adapt-s46-r2\\\", \\\"log_path\\\": \\\"logs/eval-supp-long-adapt-tau025-s46-r2.log\\\", \\\"data_path\\\": \\\"LIBERO-Long\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 46, \\\"eval_data\\\": \\\"LIBERO-Long\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\\\", \\\"parent\\\": \\\"eval-supp-long-adapt-tau025-s46\\\"}, \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-24T07:06:09.666Z\\\"}, \\\"eval-supp-long-vla-only-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T06:34:23.532Z\\\", \\\"updated_at\\\": \\\"2026-05-24T07:05:36.964Z\\\", \\\"hypothesis\\\": \\\"K=2 mean baseline on Long suite seed47 (NOT VLA-only — actual command uses --baseline_mode mean --K 2, output eval_long_k2mean_seed47.json). Misnamed at creation. Paired with Adapt-s47 for matched-seed comparison.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark long --mode vla_only --baseline_mode mean --K 2 --seed 47 --n_rollouts 20 --output_file logs/eval_long_k2mean_seed47.json\\\", \\\"server\\\": \\\"cqa1-32758\\\", \\\"gpu\\\": [\\\"cuda:5\\\"], \\\"tmux_session\\\": \\\"long-vla-s47\\\", \\\"log_path\\\": \\\"logs/eval-supp-long-vla-only-s47.log\\\", \\\"data_path\\\": \\\"LIBERO-Long\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 47, \\\"eval_data\\\": \\\"LIBERO-Long\\\", \\\"checkpoint_source\\\": \\\"n/a-baseline\\\", \\\"parent\\\": \\\"eval-supp-long-vla-only-s46\\\"}}, \\\"eval-supp-obj-crm-norm005-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T03:56:52.910Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:55:16.446Z\\\", \\\"metrics\\\": {\\\"success_rate\\\": 0.765, \\\"successes\\\": 153, \\\"total\\\": 200, \\\"source\\\": \\\"json_harvest_bjb2-40593\\\", \\\"json_file\\\": \\\"eval_object_crm_obs_only_norm0.05_seed45.json\\\"}, \\\"hypothesis\\\": \\\"CRM obs-only norm=0.05 on Object suite seed45. Extends Object CRM obs-only coverage for variance analysis.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"spec\\\": {\\\"checkpoint_path\\\": \\\"n/a-eval-only\\\", \\\"log_path\\\": \\\"eval_object_crm_obs_only_norm0.05_seed45.json\\\", \\\"command\\\": \\\"duplicate entry fix\\\", \\\"server\\\": \\\"bjb2-40593\\\", \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA+CRM\\\", \\\"seed\\\": 45, \\\"eval_data\\\": \\\"LIBERO-Object\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\"}, \\\"completed_at\\\": \\\"2026-05-24T06:55:16.446Z\\\"}, \\\"eval-supp-long-crm-norm005-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T06:52:08.968Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:53:16.695Z\\\", \\\"hypothesis\\\": \\\"CRM obs-only norm=0.05 on Long suite seed47 (sixth seed extension). Pairs with running Long vla-only-s47 and adapt-s47 on cqa1-32758 to tighten Long suite CI which has highest variance.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark long --mode crm_obs_only --seed 47 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:5\\\"], \\\"tmux_session\\\": \\\"long-crm-s47\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-supp-long-crm-norm005-s47.log\\\", \\\"data_path\\\": \\\"LIBERO-Long\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 47, \\\"eval_data\\\": \\\"LIBERO-Long\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt\\\"}}, \\\"eval-supp-long-reconvla-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T06:52:05.630Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:53:02.593Z\\\", \\\"hypothesis\\\": \\\"Reconvla K=10 on Long suite seed47 (sixth seed extension). Pairs with running Long vla-only-s47 and adapt-s47 on cqa1-32758 to tighten Long suite CI which has highest variance.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark long --mode reconvla --seed 47 --n_rollouts 20 --K 10\\\", \\\"server\\\": \\\"bjb1-32546\\\", \\\"gpu\\\": [\\\"cuda:4\\\"], \\\"tmux_session\\\": \\\"long-reconvla-s47\\\", \\\"log_path\\\": \\\"~/runs/acr-vla-conformal-refinement/eval-supp-long-reconvla-s47.log\\\", \\\"data_path\\\": \\\"LIBERO-Long\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA\\\", \\\"seed\\\": 47, \\\"eval_data\\\": \\\"LIBERO-Long\\\", \\\"checkpoint_source\\\": \\\"n/a-reconvla\\\"}}, \\\"eval-supp-spatial-crm-norm005-s47\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T06:49:40.206Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:51:27.049Z\\\", \\\"hypothesis\\\": \\\"CRM obs_only norm=0.05 on LIBERO-Spatial seed47. Fifth seed extending Spatial CRM coverage (s43-s46 mean ~79.6%). Tightens CI for statistical comparison with VLA-only/K2mean/Reconvla/Adaptive at matched 5-seed coverage.\\\", \\\"parent\\\": \\\"eval-supp-spatial-crm-norm005-s46\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 47 --n_rollouts 20 --max_correction_norm 0.05 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --output_file logs/eval_spatial_crm_obs_only_norm0.05_seed47.json\\\", \\\"server\\\": \\\"bjb2-40593\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"235730\\\", \\\"tmux_session\\\": \\\"eval-spatial-crm-s47\\\", \\\"log_path\\\": \\\"/tmp/eval_spatial_crm_s47.log\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA+CRM\\\", \\\"seed\\\": 47, \\\"eval_data\\\": \\\"LIBERO-Spatial\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"checkpoint_path\\\": \\\"n/a-eval-only\\\", \\\"submitted_at\\\": \\\"2026-05-24T06:50:07Z\\\", \\\"submitted_via\\\": \\\"ssh_execute_tmux\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}}, \\\"eval-supp-vla-only-spatial-s46\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T06:48:57.955Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:50:52.276Z\\\", \\\"hypothesis\\\": \\\"VLA-only baseline on Spatial suite seed46. Extending from 3-seed (s42/s43/s44) to 5-seed for variance analysis. 3-seed mean 78.7%±0.3%.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --benchmark spatial --mode vla_only --seed 46 --n_rollouts 20 --K 1\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 46, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/models/smolvla_libero/\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial 10 tasks x 20 rollouts\\\", \\\"benchmark\\\": \\\"spatial\\\", \\\"mode\\\": \\\"vla_only\\\", \\\"tmux_session\\\": \\\"eval-supp-vla-only-spatial-s46\\\", \\\"gpu\\\": 5}}, \\\"eval-supp-adapt-tau025-spatial-s45\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T06:48:54.415Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:50:44.120Z\\\", \\\"hypothesis\\\": \\\"Adaptive CRM tau=0.25 (conformal_threshold) with max_correction_norm=0.2 on Spatial suite seed45. Extending from 3-seed (s42/s43/s44) to 5-seed for variance analysis. 3-seed mean 80.8%±1.1%.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark spatial --mode adaptive_conformal_crm --seed 45 --n_rollouts 20 --K 10 --max_correction_norm 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"smolvla+crm-adaptive\\\", \\\"seed\\\": 45, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial 10 tasks x 20 rollouts\\\", \\\"benchmark\\\": \\\"spatial\\\", \\\"mode\\\": \\\"adaptive_conformal_crm\\\", \\\"max_correction_norm\\\": 0.2, \\\"conformal_threshold\\\": 0.25, \\\"K\\\": 10, \\\"tmux_session\\\": \\\"eval-supp-adapt-tau025-spatial-s45\\\", \\\"gpu\\\": 4}}, \\\"eval-supp-crm-norm005-spatial-s45\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T06:48:50.955Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:50:37.107Z\\\", \\\"hypothesis\\\": \\\"CRM always-on norm=0.05 on Spatial suite seed45. Extending from 3-seed (s42/s43/s44) to 5-seed for variance analysis. 3-seed mean 79.8%±1.3%.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --seed 45 --n_rollouts 20 --K 10 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"smolvla+crm\\\", \\\"seed\\\": 45, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial 10 tasks x 20 rollouts\\\", \\\"benchmark\\\": \\\"spatial\\\", \\\"mode\\\": \\\"crm_obs_only\\\", \\\"max_correction_norm\\\": 0.05, \\\"K\\\": 10, \\\"tmux_session\\\": \\\"eval-supp-crm-norm005-spatial-s45\\\", \\\"gpu\\\": 3}}, \\\"eval-supp-vla-only-spatial-s45\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T06:48:46.040Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:50:30.794Z\\\", \\\"hypothesis\\\": \\\"VLA-only baseline on Spatial suite seed45. Extending from 3-seed (s42/s43/s44) to 5-seed for variance analysis. 3-seed mean 78.7%±0.3%.\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark spatial --mode vla_only --seed 45 --n_rollouts 20 --K 1\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"data_path\\\": \\\"LIBERO-Spatial\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"smolvla\\\", \\\"seed\\\": 45, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/models/smolvla_libero/\\\", \\\"eval_data\\\": \\\"LIBERO-Spatial 10 tasks x 20 rollouts\\\", \\\"benchmark\\\": \\\"spatial\\\", \\\"mode\\\": \\\"vla_only\\\", \\\"tmux_session\\\": \\\"eval-supp-vla-only-spatial-s45\\\", \\\"gpu\\\": 2}}, \\\"eval-supp-obj-adapt-tau025-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-23T17:22:29.274Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:49:49.091Z\\\", \\\"hypothesis\\\": \\\"Adaptive CRM tau=0.25 on Object suite seed45. Fills s45 gap in Object adaptive 5-seed coverage (have s42-s44) for supplementary table.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u src/evaluate.py --benchmark object --mode adaptive_conformal_crm --seed 45 --n_rollouts 20 --max_correction_norm 0.2 --conformal_threshold 0.25 --K 2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"server\\\": \\\"bjb2-40593\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"tmux_session\\\": \\\"eval-obj-adapt-s45\\\", \\\"log_path\\\": \\\"/tmp/eval_obj_adapt_s45.log\\\", \\\"seed\\\": 45, \\\"data_path\\\": \\\"LIBERO-Object\\\", \\\"data_count\\\": 200, \\\"model_name\\\": \\\"SmolVLA+AdaptiveCRM\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\\", \\\"eval_data\\\": \\\"LIBERO-Object\\\"}, \\\"conclusion\\\": \\\"failed\\\", \\\"log_path\\\": \\\"/tmp/eval_obj_adapt_s45.log\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only, crashed due to missing CRM checkpoint)\\\", \\\"completed_at\\\": \\\"2026-05-23T17:51:39.777Z\\\"}, \\\"eval-supp-obj-vla-only-s45\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-23T17:27:19.029Z\\\", \\\"updated_at\\\": \\\"2026-05-24T06:49:36.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false,
    "persistedOutputPath": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/4a8246d3-c96e-4959-82ff-767c57b966c8/tool-results/bh6umo280.txt",
    "persistedOutputSize": 117448
  }
}
```

</details>

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01QLEpMMZ1v9Eqb7WrenoM4H`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "tmux list-sessions 2>&1; echo \"---SEPARATOR---\"; for s in eval-supp-crm-norm005-spatial-s46 eval-supp-vla-only-spatial-s45 eval-supp-crm-norm005-spatial-s45 eval-supp-adapt-tau025-spatial-s45 eval-supp-vla-only-spatial-s46; do echo \"=== $s ===\"; tmux capture-pane -t \"$s\" -p 2>&1 | tail -10; done",
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
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "2308f5d1-2e84-4f4b-b999-f3f1d1e83bde",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ReHShhorhTBpeDrNCVjvm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 988,
      "cache_read_input_tokens": 36282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 988
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

_source line 29 · 2026-05-24T08:25:00.876Z_

<details><summary>↩ Tool result · `toolu_01QLEpMMZ1v9Eqb7WrenoM4H`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"eval-supp-adapt-tau025-spatial-s45: 1 windows (created Sun May 24 14:51:18 2026)\\neval-supp-crm-norm005-spatial-s45: 1 windows (created Sun May 24 14:51:15 2026)\\neval-supp-crm-norm005-spatial-s46: 1 windows (created Sun May 24 15:14:46 2026)\\neval-supp-vla-only-spatial-s45: 1 windows (created Sun May 24 14:51:12 2026)\\neval-supp-vla-only-spatial-s46: 1 windows (created Sun May 24 14:51:21 2026)\\n---SEPARATOR---\\n=== eval-supp-crm-norm005-spatial-s46 ===\\n_the_plate: rollout 15/20, success so far: 11/15\\n  pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on\\n_the_plate: rollout 20/20, success so far: 14/20\\n[pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_\\nthe_plate] success rate: 70.0% (14/20)\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 5/20,\\n success so far: 0/5\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 10/20\\n, success so far: 0/10\\n\\n=== eval-supp-vla-only-spatial-s45 ===\\nut 5/20, success so far: 5/5\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollo\\nut 10/20, success so far: 10/10\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollo\\nut 15/20, success so far: 15/15\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollo\\nut 20/20, success so far: 20/20\\n[pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate] succes\\ns rate: 100.0% (20/20)\\n\\n=== eval-supp-crm-norm005-spatial-s45 ===\\nut 5/20, success so far: 4/5\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollo\\nut 10/20, success so far: 9/10\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollo\\nut 15/20, success so far: 14/15\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollo\\nut 20/20, success so far: 19/20\\n[pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate] succes\\ns rate: 95.0% (19/20)\\n\\n=== eval-supp-adapt-tau025-spatial-s45 ===\\nut 5/20, success so far: 5/5\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollo\\nut 10/20, success so far: 10/10\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollo\\nut 15/20, success so far: 15/15\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollo\\nut 20/20, success so far: 20/20\\n[pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate] succes\\ns rate: 100.0% (20/20)\\n\\n=== eval-supp-vla-only-spatial-s46 ===\\n, success so far: 0/20\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate:\\n0.0% (0/20)\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollo\\nut 5/20, success so far: 4/5\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollo\\nut 10/20, success so far: 9/10\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollo\\nut 15/20, success so far: 14/15\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "009ae1b0-a332-4a5e-85c0-ef5d055b22f3",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"eval-supp-adapt-tau025-spatial-s45: 1 windows (created Sun May 24 14:51:18 2026)\\\\neval-supp-crm-norm005-spatial-s45: 1 windows (created Sun May 24 14:51:15 2026)\\\\neval-supp-crm-norm005-spatial-s46: 1 windows (created Sun May 24 15:14:46 2026)\\\\neval-supp-vla-only-spatial-s45: 1 windows (created Sun May 24 14:51:12 2026)\\\\neval-supp-vla-only-spatial-s46: 1 windows (created Sun May 24 14:51:21 2026)\\\\n---SEPARATOR---\\\\n=== eval-supp-crm-norm005-spatial-s46 ===\\\\n_the_plate: rollout 15/20, success so far: 11/15\\\\n  pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on\\\\n_the_plate: rollout 20/20, success so far: 14/20\\\\n[pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_\\\\nthe_plate] success rate: 70.0% (14/20)\\\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 5/20,\\\\n success so far: 0/5\\\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 10/20\\\\n, success so far: 0/10\\\\n\\\\n=== eval-supp-vla-only-spatial-s45 ===\\\\nut 5/20, success so far: 5/5\\\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollo\\\\nut 10/20, success so far: 10/10\\\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollo\\\\nut 15/20, success so far: 15/15\\\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollo\\\\nut 20/20, success so far: 20/20\\\\n[pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate] succes\\\\ns rate: 100.0% (20/20)\\\\n\\\\n=== eval-supp-crm-norm005-spatial-s45 ===\\\\nut 5/20, success so far: 4/5\\\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollo\\\\nut 10/20, success so far: 9/10\\\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollo\\\\nut 15/20, success so far: 14/15\\\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollo\\\\nut 20/20, success so far: 19/20\\\\n[pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate] succes\\\\ns rate: 95.0% (19/20)\\\\n\\\\n=== eval-supp-adapt-tau025-spatial-s45 ===\\\\nut 5/20, success so far: 5/5\\\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollo\\\\nut 10/20, success so far: 10/10\\\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollo\\\\nut 15/20, success so far: 15/15\\\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollo\\\\nut 20/20, success so far: 20/20\\\\n[pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate] succes\\\\ns rate: 100.0% (20/20)\\\\n\\\\n=== eval-supp-vla-only-spatial-s46 ===\\\\n, success so far: 0/20\\\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate:\\\\n0.0% (0/20)\\\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollo\\\\nut 5/20, success so far: 4/5\\\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollo\\\\nut 10/20, success so far: 9/10\\\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollo\\\\nut 15/20, success so far: 14/15\\\\n\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.39}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"eval-supp-adapt-tau025-spatial-s45: 1 windows (created Sun May 24 14:51:18 2026)\\neval-supp-crm-norm005-spatial-s45: 1 windows (created Sun May 24 14:51:15 2026)\\neval-supp-crm-norm005-spatial-s46: 1 windows (created Sun May 24 15:14:46 2026)\\neval-supp-vla-only-spatial-s45: 1 windows (created Sun May 24 14:51:12 2026)\\neval-supp-vla-only-spatial-s46: 1 windows (created Sun May 24 14:51:21 2026)\\n---SEPARATOR---\\n=== eval-supp-crm-norm005-spatial-s46 ===\\n_the_plate: rollout 15/20, success so far: 11/15\\n  pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on\\n_the_plate: rollout 20/20, success so far: 14/20\\n[pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_\\nthe_plate] success rate: 70.0% (14/20)\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 5/20,\\n success so far: 0/5\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 10/20\\n, success so far: 0/10\\n\\n=== eval-supp-vla-only-spatial-s45 ===\\nut 5/20, success so far: 5/5\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollo\\nut 10/20, success so far: 10/10\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollo\\nut 15/20, success so far: 15/15\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollo\\nut 20/20, success so far: 20/20\\n[pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate] succes\\ns rate: 100.0% (20/20)\\n\\n=== eval-supp-crm-norm005-spatial-s45 ===\\nut 5/20, success so far: 4/5\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollo\\nut 10/20, success so far: 9/10\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollo\\nut 15/20, success so far: 14/15\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollo\\nut 20/20, success so far: 19/20\\n[pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate] succes\\ns rate: 95.0% (19/20)\\n\\n=== eval-supp-adapt-tau025-spatial-s45 ===\\nut 5/20, success so far: 5/5\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollo\\nut 10/20, success so far: 10/10\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollo\\nut 15/20, success so far: 15/15\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollo\\nut 20/20, success so far: 20/20\\n[pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate] succes\\ns rate: 100.0% (20/20)\\n\\n=== eval-supp-vla-only-spatial-s46 ===\\n, success so far: 0/20\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate:\\n0.0% (0/20)\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollo\\nut 5/20, success so far: 4/5\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollo\\nut 10/20, success so far: 9/10\\n  pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate: rollo\\nut 15/20, success so far: 14/15\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"
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
OK, so the two lerobot experiments are not in the registry at all. The grep on the full registry dump would confirm. Let me check. Meanwhile, the bjb2-28827 experiments are all still running. Let me figure out what task they're on.

From the tmux output:
1. **crm-norm005-spatial-s46** (GPU 0, PID 121241): On task "pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate" rollout 10/20, success 0/10. Previously finished "pick_up_the_black_bowl_in_the_top_drawer..." with 70% (14/20). Need to figure out what task number this is.


2. **vla-only-spatial-s45** (GPU 2, PID 96831): Completed "pick_up_the_black_bowl_next_to_the_cookie_box" with 100% (20/20).
3. **crm-norm005-spatial-s45** (GPU 3, PID 97070): Also finished that same task at 95% (19/20).
4. **adapt-tau025-spatial-s45** (GPU 4, PID 97307): Working on the same task but the output cuts off.

I need to figure out which task number each experiment is actually on since the tmux window is limited. I should check the log files directly or scroll back further to get the full picture. I'm also still looking for those two lerobot experiments—let me search the registry dump for them, or check if they might be listed under different names.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "3fd75af1-fb9c-4ff9-b3c0-2d9cfb8df066",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0119PrZRPZhdLXsmzC2J7dCr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2908,
      "cache_read_input_tokens": 37270,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2908
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

<details open><summary>🔧 Tool call — Bash · `toolu_01SB4RLfGMkxyULmUyBgYceJ`</summary>

```json
{
  "command": "grep -o '\"eval-smolvla-lerobot[^\"]*\"' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/4a8246d3-c96e-4959-82ff-767c57b966c8/tool-results/mcp-agent-ml-research-read_registry-1779611091392.txt",
  "description": "Search for lerobot experiment IDs in registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "9aa5dbc2-30fd-40d6-9210-72de979e0445",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0119PrZRPZhdLXsmzC2J7dCr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2908,
      "cache_read_input_tokens": 37270,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2908
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

_source line 32 · 2026-05-24T08:25:19.463Z_

<details><summary>↩ Tool result · `toolu_01SB4RLfGMkxyULmUyBgYceJ`</summary>

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
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "7a978201-53b7-40ab-8b05-27a41cb05df2",
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

_source line 33_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_011xAmMA5T7kugGVVW4kPLof`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "for s in eval-supp-crm-norm005-spatial-s46 eval-supp-vla-only-spatial-s45 eval-supp-crm-norm005-spatial-s45 eval-supp-adapt-tau025-spatial-s45 eval-supp-vla-only-spatial-s46; do echo \"=== $s ===\"; tmux capture-pane -t \"$s\" -p -S -1000 2>&1 | grep -E \"(Task|task|success rate|rollout)\" | tail -20; done",
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
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "b89c1119-7f74-4856-a034-f35d59dd541b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0119PrZRPZhdLXsmzC2J7dCr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2908,
      "cache_read_input_tokens": 37270,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2908
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

_source line 34 · 2026-05-24T08:25:22.140Z_

<details><summary>↩ Tool result · `toolu_011xAmMA5T7kugGVVW4kPLof`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== eval-supp-crm-norm005-spatial-s46 ===\\nate] success rate: 95.0% (19/20)\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 5/\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 10\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 15\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 20\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 5/\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 10\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 15\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 20\\n_the_plate: rollout 5/20, success so far: 4/5\\n_the_plate: rollout 10/20, success so far: 8/10\\n_the_plate: rollout 15/20, success so far: 11/15\\n_the_plate: rollout 20/20, success so far: 14/20\\nthe_plate] success rate: 70.0% (14/20)\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 5/20,\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 10/20\\n=== eval-supp-vla-only-spatial-s45 ===\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 5/\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 10\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 15\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 20\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 5/\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 10\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 15\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 20\\n_the_plate: rollout 5/20, success so far: 4/5\\n_the_plate: rollout 10/20, success so far: 8/10\\n_the_plate: rollout 15/20, success so far: 11/15\\n_the_plate: rollout 20/20, success so far: 14/20\\nthe_plate] success rate: 70.0% (14/20)\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 5/20,\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 10/20\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 15/20\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 20/20\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate:\\n=== eval-supp-crm-norm005-spatial-s45 ===\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 5/\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 10\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 15\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 20\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 5/\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 10\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 15\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 20\\n_the_plate: rollout 5/20, success so far: 4/5\\n_the_plate: rollout 10/20, success so far: 8/10\\n_the_plate: rollout 15/20, success so far: 11/15\\n_the_plate: rollout 20/20, success so far: 14/20\\nthe_plate] success rate: 70.0% (14/20)\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 5/20,\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 10/20\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 15/20\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 20/20\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate:\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 5/20, s\\n=== eval-supp-adapt-tau025-spatial-s45 ===\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 5/\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 10\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 15\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 20\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 5/\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 10\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 15\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 20\\n_the_plate: rollout 5/20, success so far: 4/5\\n_the_plate: rollout 10/20, success so far: 8/10\\n_the_plate: rollout 15/20, success so far: 12/15\\n_the_plate: rollout 20/20, success so far: 15/20\\nthe_plate] success rate: 75.0% (15/20)\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 5/20,\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 10/20\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 15/20\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 20/20\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate:\\n=== eval-supp-vla-only-spatial-s46 ===\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 5/\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 10\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 15\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 20\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 5/\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 10\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 15\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 20\\n_the_plate: rollout 5/20, success so far: 4/5\\n_the_plate: rollout 10/20, success so far: 8/10\\n_the_plate: rollout 15/20, success so far: 12/15\\n_the_plate: rollout 20/20, success so far: 15/20\\nthe_plate] success rate: 75.0% (15/20)\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 5/20,\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 10/20\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 15/20\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 20/20\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate:\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "db2679e9-78f2-4855-a62b-0b22fa9f8c9a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"=== eval-supp-crm-norm005-spatial-s46 ===\\\\nate] success rate: 95.0% (19/20)\\\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout\\\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout\\\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout\\\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout\\\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 5/\\\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 10\\\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 15\\\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 20\\\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 5/\\\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 10\\\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 15\\\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 20\\\\n_the_plate: rollout 5/20, success so far: 4/5\\\\n_the_plate: rollout 10/20, success so far: 8/10\\\\n_the_plate: rollout 15/20, success so far: 11/15\\\\n_the_plate: rollout 20/20, success so far: 14/20\\\\nthe_plate] success rate: 70.0% (14/20)\\\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 5/20,\\\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 10/20\\\\n=== eval-supp-vla-only-spatial-s45 ===\\\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout\\\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout\\\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 5/\\\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 10\\\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 15\\\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 20\\\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 5/\\\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 10\\\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 15\\\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 20\\\\n_the_plate: rollout 5/20, success so far: 4/5\\\\n_the_plate: rollout 10/20, success so far: 8/10\\\\n_the_plate: rollout 15/20, success so far: 11/15\\\\n_the_plate: rollout 20/20, success so far: 14/20\\\\nthe_plate] success rate: 70.0% (14/20)\\\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 5/20,\\\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 10/20\\\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 15/20\\\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 20/20\\\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate:\\\\n=== eval-supp-crm-norm005-spatial-s45 ===\\\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout\\\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 5/\\\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 10\\\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 15\\\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 20\\\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 5/\\\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 10\\\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 15\\\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 20\\\\n_the_plate: rollout 5/20, success so far: 4/5\\\\n_the_plate: rollout 10/20, success so far: 8/10\\\\n_the_plate: rollout 15/20, success so far: 11/15\\\\n_the_plate: rollout 20/20, success so far: 14/20\\\\nthe_plate] success rate: 70.0% (14/20)\\\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 5/20,\\\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 10/20\\\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 15/20\\\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 20/20\\\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate:\\\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 5/20, s\\\\n=== eval-supp-adapt-tau025-spatial-s45 ===\\\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout\\\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout\\\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 5/\\\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 10\\\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 15\\\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 20\\\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 5/\\\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 10\\\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 15\\\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 20\\\\n_the_plate: rollout 5/20, success so far: 4/5\\\\n_the_plate: rollout 10/20, success so far: 8/10\\\\n_the_plate: rollout 15/20, success so far: 12/15\\\\n_the_plate: rollout 20/20, success so far: 15/20\\\\nthe_plate] success rate: 75.0% (15/20)\\\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 5/20,\\\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 10/20\\\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 15/20\\\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 20/20\\\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate:\\\\n=== eval-supp-vla-only-spatial-s46 ===\\\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout\\\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout\\\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 5/\\\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 10\\\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 15\\\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 20\\\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 5/\\\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 10\\\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 15\\\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 20\\\\n_the_plate: rollout 5/20, success so far: 4/5\\\\n_the_plate: rollout 10/20, success so far: 8/10\\\\n_the_plate: rollout 15/20, success so far: 12/15\\\\n_the_plate: rollout 20/20, success so far: 15/20\\\\nthe_plate] success rate: 75.0% (15/20)\\\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 5/20,\\\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 10/20\\\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 15/20\\\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 20/20\\\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate:\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"=== eval-supp-crm-norm005-spatial-s46 ===\\nate] success rate: 95.0% (19/20)\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 5/\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 10\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 15\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 20\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 5/\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 10\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 15\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 20\\n_the_plate: rollout 5/20, success so far: 4/5\\n_the_plate: rollout 10/20, success so far: 8/10\\n_the_plate: rollout 15/20, success so far: 11/15\\n_the_plate: rollout 20/20, success so far: 14/20\\nthe_plate] success rate: 70.0% (14/20)\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 5/20,\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 10/20\\n=== eval-supp-vla-only-spatial-s45 ===\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 5/\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 10\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 15\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 20\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 5/\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 10\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 15\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 20\\n_the_plate: rollout 5/20, success so far: 4/5\\n_the_plate: rollout 10/20, success so far: 8/10\\n_the_plate: rollout 15/20, success so far: 11/15\\n_the_plate: rollout 20/20, success so far: 14/20\\nthe_plate] success rate: 70.0% (14/20)\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 5/20,\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 10/20\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 15/20\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 20/20\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate:\\n=== eval-supp-crm-norm005-spatial-s45 ===\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 5/\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 10\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 15\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 20\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 5/\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 10\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 15\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 20\\n_the_plate: rollout 5/20, success so far: 4/5\\n_the_plate: rollout 10/20, success so far: 8/10\\n_the_plate: rollout 15/20, success so far: 11/15\\n_the_plate: rollout 20/20, success so far: 14/20\\nthe_plate] success rate: 70.0% (14/20)\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 5/20,\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 10/20\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 15/20\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 20/20\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate:\\n  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 5/20, s\\n=== eval-supp-adapt-tau025-spatial-s45 ===\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 5/\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 10\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 15\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 20\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 5/\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 10\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 15\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 20\\n_the_plate: rollout 5/20, success so far: 4/5\\n_the_plate: rollout 10/20, success so far: 8/10\\n_the_plate: rollout 15/20, success so far: 12/15\\n_the_plate: rollout 20/20, success so far: 15/20\\nthe_plate] success rate: 75.0% (15/20)\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 5/20,\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 10/20\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 15/20\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 20/20\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate:\\n=== eval-supp-vla-only-spatial-s46 ===\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout\\n  pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate: rollout\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 5/\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 10\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 15\\n  pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate: rollout 20\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 5/\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 10\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 15\\n  pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate: rollout 20\\n_the_plate: rollout 5/20, success so far: 4/5\\n_the_plate: rollout 10/20, success so far: 8/10\\n_the_plate: rollout 15/20, success so far: 12/15\\n_the_plate: rollout 20/20, success so far: 15/20\\nthe_plate] success rate: 75.0% (15/20)\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 5/20,\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 10/20\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 15/20\\n  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 20/20\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate:\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 35_

<details><summary>Logged reasoning block</summary>

```text
So the lerobot experiments don't exist in the registry. The grep returned nothing. These might be from a different naming convention. Let me also check:
1. The tmux output suggests all 5 experiments on bjb2-28827 are progressing through the LIBERO-Spatial tasks. I need to figure out which task number they're on. LIBERO-Spatial has 10 tasks. Let me identify the task ordering.

The tasks I can see from scrollback:
- pick_up_the_black_bowl_next_to_the_ramekin...


- pick_up_the_black_bowl_from_table_center...
- pick_up_the_black_bowl_on_the_cookie_box...
- pick_up_the_black_bowl_in_the_top_drawer... (for crm-s46)
- pick_up_the_black_bowl_on_the_ramekin...
- pick_up_the_black_bowl_on_the_stove... (crm-s45 is starting this)
- pick_up_the_black_bowl_next_to_the_cookie_box...

That's 7 tasks visible so far, and I need to map out the full sequence of 10 tasks to understand where each experiment currently stands.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "412f6938-65e1-484f-932f-16a0a0306aca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014dJ8JJ9zo6CL6Rn25eAtHi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4474,
      "cache_read_input_tokens": 40178,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4474
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

_source line 36_

Registry 中不存在 "eval-smolvla-lerobot-*" 实验。让我更精确地获取每个实验完成了几个 task。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "da6105e2-a266-42d9-934b-b704a8863862",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014dJ8JJ9zo6CL6Rn25eAtHi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4474,
      "cache_read_input_tokens": 40178,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4474
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01RKbqK3Sz7zaf97hPMoP1VA`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "for s in eval-supp-crm-norm005-spatial-s46 eval-supp-vla-only-spatial-s45 eval-supp-crm-norm005-spatial-s45 eval-supp-adapt-tau025-spatial-s45 eval-supp-vla-only-spatial-s46; do echo \"=== $s ===\"; tmux capture-pane -t \"$s\" -p -S -5000 2>&1 | grep \"success rate:\" | wc -l; tmux capture-pane -t \"$s\" -p -S -5000 2>&1 | grep \"success rate:\"; done",
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
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "37d54451-02f7-4d3d-9238-2a40ff2a4f6f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014dJ8JJ9zo6CL6Rn25eAtHi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4474,
      "cache_read_input_tokens": 40178,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4474
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

_source line 38 · 2026-05-24T08:25:37.876Z_

<details><summary>↩ Tool result · `toolu_01RKbqK3Sz7zaf97hPMoP1VA`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== eval-supp-crm-norm005-spatial-s46 ===\\n2\\nate] success rate: 95.0% (19/20)\\nthe_plate] success rate: 70.0% (14/20)\\n=== eval-supp-vla-only-spatial-s45 ===\\n3\\nate] success rate: 95.0% (19/20)\\nthe_plate] success rate: 70.0% (14/20)\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate:\\n=== eval-supp-crm-norm005-spatial-s45 ===\\n3\\nate] success rate: 100.0% (20/20)\\nthe_plate] success rate: 70.0% (14/20)\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate:\\n=== eval-supp-adapt-tau025-spatial-s45 ===\\n3\\nate] success rate: 95.0% (19/20)\\nthe_plate] success rate: 75.0% (15/20)\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate:\\n=== eval-supp-vla-only-spatial-s46 ===\\n3\\nate] success rate: 95.0% (19/20)\\nthe_plate] success rate: 75.0% (15/20)\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate:\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "51a84add-1313-4c17-b48d-9ef62ecf54e4",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"=== eval-supp-crm-norm005-spatial-s46 ===\\\\n2\\\\nate] success rate: 95.0% (19/20)\\\\nthe_plate] success rate: 70.0% (14/20)\\\\n=== eval-supp-vla-only-spatial-s45 ===\\\\n3\\\\nate] success rate: 95.0% (19/20)\\\\nthe_plate] success rate: 70.0% (14/20)\\\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate:\\\\n=== eval-supp-crm-norm005-spatial-s45 ===\\\\n3\\\\nate] success rate: 100.0% (20/20)\\\\nthe_plate] success rate: 70.0% (14/20)\\\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate:\\\\n=== eval-supp-adapt-tau025-spatial-s45 ===\\\\n3\\\\nate] success rate: 95.0% (19/20)\\\\nthe_plate] success rate: 75.0% (15/20)\\\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate:\\\\n=== eval-supp-vla-only-spatial-s46 ===\\\\n3\\\\nate] success rate: 95.0% (19/20)\\\\nthe_plate] success rate: 75.0% (15/20)\\\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate:\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.37}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"=== eval-supp-crm-norm005-spatial-s46 ===\\n2\\nate] success rate: 95.0% (19/20)\\nthe_plate] success rate: 70.0% (14/20)\\n=== eval-supp-vla-only-spatial-s45 ===\\n3\\nate] success rate: 95.0% (19/20)\\nthe_plate] success rate: 70.0% (14/20)\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate:\\n=== eval-supp-crm-norm005-spatial-s45 ===\\n3\\nate] success rate: 100.0% (20/20)\\nthe_plate] success rate: 70.0% (14/20)\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate:\\n=== eval-supp-adapt-tau025-spatial-s45 ===\\n3\\nate] success rate: 95.0% (19/20)\\nthe_plate] success rate: 75.0% (15/20)\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate:\\n=== eval-supp-vla-only-spatial-s46 ===\\n3\\nate] success rate: 95.0% (19/20)\\nthe_plate] success rate: 75.0% (15/20)\\n[pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate] success rate:\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 39_

<details><summary>Logged reasoning block</summary>

```text
The tmux scrollback is limited and I can't see the complete history. The "success rate:" line counts from scrollback are:
- crm-norm005-spatial-s46: 2 completed tasks visible (but currently on another task, so at least task 3+)
- vla-only-spatial-s45: 3 completed tasks visible  
- crm-norm005-spatial-s45: 3 completed tasks visible (currently on "pick_up_the_black_bowl_on_the_stove")


- adapt-tau025-spatial-s45: 3 completed tasks visible
- vla-only-spatial-s46: 3 completed tasks visible

The scrollback is cutting off earlier completions, so I should check the log files instead since these experiments started about an hour and a half ago to get a fuller picture of progress.

Looking at the spatial suite tasks more carefully, they're alphabetically ordered with variations on picking up the black bowl from different locations. The crm-norm005-s46 model is currently working through "pick_up_the_black_bowl_on_the_ramekin" at rollout 10/20.

Checking the other models' progress: vla-only-s45 and adapt-s45 have both completed the ramekin task, while crm-norm005-s45 is further along on the stove task with only 5/20 rollout complete. All of these started about an hour and a half ago and are making solid progress, so I should check the actual server logs to get more detailed information about what's happening.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "07b08952-62bb-4633-b738-3399629696b2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Eo5m62RPAxtPD3vMSzxBkF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1174,
      "cache_read_input_tokens": 44652,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1174
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

_source line 40_

tmux scrollback 有限。让我直接查看输出日志文件获取完整进度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "d4e19a6d-7bca-41bb-b718-e9d36609d709",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Eo5m62RPAxtPD3vMSzxBkF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1174,
      "cache_read_input_tokens": 44652,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1174
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_0141CNXbQnwFfFsw9qY7ZiWa`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "ls -la /root/acr-vla-conformal-refinement/logs/eval_spatial_*s45* /root/acr-vla-conformal-refinement/logs/eval_spatial_*s46* /root/acr-vla-conformal-refinement/logs/eval_spatial_*seed45* /root/acr-vla-conformal-refinement/logs/eval_spatial_*seed46*",
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
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "906c5439-6c24-4f6f-8afe-a0adfc53d4c5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Eo5m62RPAxtPD3vMSzxBkF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1174,
      "cache_read_input_tokens": 44652,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1174
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

_source line 42 · 2026-05-24T08:26:37.099Z_

<details><summary>↩ Tool result · `toolu_0141CNXbQnwFfFsw9qY7ZiWa`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 1697 May 19 23:49 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_k5_seed45.json\\n-rw-r--r-- 1 root root 4958 May 19 23:49 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_k5_seed45.log\\n-rw-r--r-- 1 root root 1697 May 20 02:50 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed46_r2.json\\n-rw-r--r-- 1 root root 1696 May 21 16:48 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_seed45.json\\n-rw-r--r-- 1 root root 4937 May 21 16:48 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_seed45.log\\n\", \"stderr\": \"ls: cannot access '/root/acr-vla-conformal-refinement/logs/eval_spatial_*s45*': No such file or directory\\nls: cannot access '/root/acr-vla-conformal-refinement/logs/eval_spatial_*s46*': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.34}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "40652dda-f8a0-4972-9b6f-c165783483f3",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"-rw-r--r-- 1 root root 1697 May 19 23:49 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_k5_seed45.json\\\\n-rw-r--r-- 1 root root 4958 May 19 23:49 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_k5_seed45.log\\\\n-rw-r--r-- 1 root root 1697 May 20 02:50 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed46_r2.json\\\\n-rw-r--r-- 1 root root 1696 May 21 16:48 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_seed45.json\\\\n-rw-r--r-- 1 root root 4937 May 21 16:48 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_seed45.log\\\\n\\\", \\\"stderr\\\": \\\"ls: cannot access '/root/acr-vla-conformal-refinement/logs/eval_spatial_*s45*': No such file or directory\\\\nls: cannot access '/root/acr-vla-conformal-refinement/logs/eval_spatial_*s46*': No such file or directory\\\\n\\\", \\\"return_code\\\": 2}, \\\"error\\\": \\\"exit code 2\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.34}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 1697 May 19 23:49 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_k5_seed45.json\\n-rw-r--r-- 1 root root 4958 May 19 23:49 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_k5_seed45.log\\n-rw-r--r-- 1 root root 1697 May 20 02:50 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_norm02_seed46_r2.json\\n-rw-r--r-- 1 root root 1696 May 21 16:48 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_seed45.json\\n-rw-r--r-- 1 root root 4937 May 21 16:48 /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_seed45.log\\n\", \"stderr\": \"ls: cannot access '/root/acr-vla-conformal-refinement/logs/eval_spatial_*s45*': No such file or directory\\nls: cannot access '/root/acr-vla-conformal-refinement/logs/eval_spatial_*s46*': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.34}}"
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
These log files are from earlier runs, not the current ones. The current experiments are writing to default output files. Let me check what files the evaluate.py script produces. The commands don't specify --output_file, so they might write to a default location. Let me check what logs are being generated.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "5c450511-a6f7-4aa7-a535-19103f4ea393",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WwEZBPaP9SYG7gNcJGMRsZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1373,
      "cache_read_input_tokens": 45826,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1373
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_018gNtY1WLD7x4F78KCy2AiG`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*.json\" -newer /root/acr-vla-conformal-refinement/logs/eval_spatial_obs_only_seed45.json -type f",
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
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "dfb2aea8-35da-4c27-a99a-0913a54c95bb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WwEZBPaP9SYG7gNcJGMRsZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1373,
      "cache_read_input_tokens": 45826,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1373
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

_source line 45 · 2026-05-24T08:26:43.223Z_

<details><summary>↩ Tool result · `toolu_018gNtY1WLD7x4F78KCy2AiG`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.074855_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_reconvla_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_reconvla_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.4_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.15_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_reconvla_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.1_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_crm_obs_only_norm0.05_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_reconvla_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_reconvla_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_k2mean_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_reconvla_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_k2mean_seed45.json\\n/root/acr-vla-conformal-refinement/logs/openvla_eval_object_vla_only_K1_seed42.json\\n/root/acr-vla-conformal-refinement/logs/openvla_eval_object_crm_k1_multiscale_K1_seed42.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "d0d967bd-dbbd-471c-a5f9-9c358d1b2f52",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.074855_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_reconvla_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_reconvla_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.4_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.15_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_reconvla_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.1_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_crm_obs_only_norm0.05_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_reconvla_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_reconvla_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_k2mean_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_goal_reconvla_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_long_k2mean_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/openvla_eval_object_vla_only_K1_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/openvla_eval_object_crm_k1_multiscale_K1_seed42.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.32}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_crm_obs_only_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.074855_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_reconvla_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_reconvla_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.4_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.15_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_reconvla_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.1_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_crm_obs_only_norm0.05_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_reconvla_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_reconvla_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_k2mean_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_crm_obs_only_norm0.05_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_goal_reconvla_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_long_k2mean_seed45.json\\n/root/acr-vla-conformal-refinement/logs/openvla_eval_object_vla_only_K1_seed42.json\\n/root/acr-vla-conformal-refinement/logs/openvla_eval_object_crm_k1_multiscale_K1_seed42.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 46_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Qbc7apQW6ogvfLxBuWj4Y6`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "find /root/acr-vla-conformal-refinement/ -name \"*.json\" -mmin -120 -type f",
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
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "8b004c8e-a560-4707-b7dd-79414e22ea39",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WwEZBPaP9SYG7gNcJGMRsZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1373,
      "cache_read_input_tokens": 45826,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1373
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

_source line 47 · 2026-05-24T08:26:43.959Z_

<details><summary>↩ Tool result · `toolu_01Qbc7apQW6ogvfLxBuWj4Y6`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/openvla_eval_object_vla_only_K1_seed42.json\\n/root/acr-vla-conformal-refinement/logs/openvla_eval_object_crm_k1_multiscale_K1_seed42.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "c20b505d-377b-4997-937e-1ad932893260",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/acr-vla-conformal-refinement/logs/openvla_eval_object_vla_only_K1_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/openvla_eval_object_crm_k1_multiscale_K1_seed42.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.32}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/openvla_eval_object_vla_only_K1_seed42.json\\n/root/acr-vla-conformal-refinement/logs/openvla_eval_object_crm_k1_multiscale_K1_seed42.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 48_

<details><summary>Logged reasoning block</summary>

```text
So the currently running Spatial experiments on bjb2-28827 haven't produced output JSON files yet (no recent spatial json files for s45/s46). They're still in progress. The commands don't specify `--output_file`, so the script will use default file naming and write when it finishes all 10 tasks.

Let me now figure out how many tasks each has completed. I need to use the tmux scrollback with more depth or find the actual log output somewhere. But the tmux scrollback may be buffered with a limited size. Let me try to capture more from tmux or use a different approach.

Actually, looking at the task names in LIBERO-Spatial:


The tasks appear to be ordered alphabetically, and from the scrollback I can see several task names starting with "pick_up_the_black_bowl" in various locations—from the table center to drawers to different surfaces. I can see at least seven distinct tasks listed, though the full list seems to be cut off.

I need to check the evaluate.py file to understand the complete task ordering, since LIBERO-Spatial should have 10 tasks total. Looking at the experiment progress over the past 1.5 hours, I'm tracking where each of the five experiments stands—crm-norm005-s46 is partway through the "on_the_ramekin" rollout with earlier tasks mostly completed, while vla-only-s45 has progressed further through multiple tasks. I'm looking at the tmux history to find the success rate metrics instead of trying to parse the task completion data manually.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "f625dba7-c8e5-4dd0-b60f-3d2212090f65",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pqe6xX5i9BMqufdmNKMTk4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2240,
      "cache_read_input_tokens": 47199,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2240
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01Huj1p4BizzndSGeshna6Px`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "for s in eval-supp-crm-norm005-spatial-s46 eval-supp-vla-only-spatial-s45 eval-supp-crm-norm005-spatial-s45 eval-supp-adapt-tau025-spatial-s45 eval-supp-vla-only-spatial-s46; do echo \"=== $s ===\"; cnt=$(tmux capture-pane -t \"$s\" -p -S -50000 2>&1 | grep -c \"success rate:\"); last=$(tmux capture-pane -t \"$s\" -p -S -50000 2>&1 | grep \"rollout\" | tail -1); echo \"completed_tasks=$cnt  last_line=$last\"; done",
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
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "6d893160-612d-4acf-8e16-38e71c962745",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pqe6xX5i9BMqufdmNKMTk4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2240,
      "cache_read_input_tokens": 47199,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2240
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

_source line 50 · 2026-05-24T08:27:09.151Z_

<details><summary>↩ Tool result · `toolu_01Huj1p4BizzndSGeshna6Px`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== eval-supp-crm-norm005-spatial-s46 ===\\ncompleted_tasks=2  last_line=  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 10/20\\n=== eval-supp-vla-only-spatial-s45 ===\\ncompleted_tasks=3  last_line=  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 5/20, s\\n=== eval-supp-crm-norm005-spatial-s45 ===\\ncompleted_tasks=3  last_line=  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 5/20, s\\n=== eval-supp-adapt-tau025-spatial-s45 ===\\ncompleted_tasks=3  last_line=  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 20/20\\n=== eval-supp-vla-only-spatial-s46 ===\\ncompleted_tasks=3  last_line=  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 20/20\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "09f41b76-024d-42d6-ba8d-94c7b18d6162",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"=== eval-supp-crm-norm005-spatial-s46 ===\\\\ncompleted_tasks=2  last_line=  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 10/20\\\\n=== eval-supp-vla-only-spatial-s45 ===\\\\ncompleted_tasks=3  last_line=  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 5/20, s\\\\n=== eval-supp-crm-norm005-spatial-s45 ===\\\\ncompleted_tasks=3  last_line=  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 5/20, s\\\\n=== eval-supp-adapt-tau025-spatial-s45 ===\\\\ncompleted_tasks=3  last_line=  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 20/20\\\\n=== eval-supp-vla-only-spatial-s46 ===\\\\ncompleted_tasks=3  last_line=  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 20/20\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.37}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"=== eval-supp-crm-norm005-spatial-s46 ===\\ncompleted_tasks=2  last_line=  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 10/20\\n=== eval-supp-vla-only-spatial-s45 ===\\ncompleted_tasks=3  last_line=  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 5/20, s\\n=== eval-supp-crm-norm005-spatial-s45 ===\\ncompleted_tasks=3  last_line=  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 5/20, s\\n=== eval-supp-adapt-tau025-spatial-s45 ===\\ncompleted_tasks=3  last_line=  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 20/20\\n=== eval-supp-vla-only-spatial-s46 ===\\ncompleted_tasks=3  last_line=  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 20/20\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"
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
The tmux scrollback is limited to 2000 lines by default (the -S -50000 still only captures whatever the history-limit is). The visible completed task counts (2-3) don't represent the full picture because earlier tasks have scrolled out.

Let me think about this differently. The experiments started about 1.5 hours ago. LIBERO-Spatial has 10 tasks x 20 rollouts each. Let me count from the visible task names. Looking at the alphabetical ordering of LIBERO-Spatial tasks:

1. pick_up_the_black_bowl_at_the_... (?)


2. pick_up_the_black_bowl_from_table_center_...
3. pick_up_the_black_bowl_in_the_top_drawer_...
4. pick_up_the_black_bowl_next_to_the_cookie_box_...
5. pick_up_the_black_bowl_next_to_the_ramekin_...
6. pick_up_the_black_bowl_on_the_cookie_box_...
7. pick_up_the_black_bowl_on_the_plate_... (?)
8. pick_up_the_black_bowl_on_the_ramekin_...
9. pick_up_the_black_bowl_on_the_stove_...
10. (still need to identify the last one)

Looking at the rollout performance across the experiments, the ones on the ramekin and stove placements are showing strong results—most are hitting around 80-90% success rates and nearly complete with their rollouts.

Now I need to track down those lerobot experiments the user mentioned. A grep search through the registry came up empty, so they either got renamed or were never added to this project. I should let the user know about that. I'm also realizing the tmux scrollback is giving me incomplete data on task progress, so I'm checking if there's a log file somewhere on disk that would show the actual completion counts more accurately.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "05a8e72f-24b2-4d23-b930-6ec7c9c2b8f8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FFPMVT2aPFFS9o3wv5Whbk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1479,
      "cache_read_input_tokens": 49439,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1479
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

_source line 52_

tmux scrollback 有限，无法看到完整历史。让我检查是否有 nohup/redirect 日志，并确认 LIBERO-Spatial 的 task 总数来估算进度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "03b7e783-c470-4f26-8b04-54e520138100",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FFPMVT2aPFFS9o3wv5Whbk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1479,
      "cache_read_input_tokens": 49439,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1479
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

_source line 53_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01DtWcVg4GHGBmPtjgdiuR8Y`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "find /tmp -name \"eval*spatial*\" -type f",
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
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "60d7f8c7-dbf2-4df4-8bc8-390697e169e5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FFPMVT2aPFFS9o3wv5Whbk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1479,
      "cache_read_input_tokens": 49439,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1479
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

_source line 54 · 2026-05-24T08:27:28.207Z_

<details><summary>↩ Tool result · `toolu_01DtWcVg4GHGBmPtjgdiuR8Y`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/tmp/agent-ml-exit/eval-obs-only-spatial-norm02-k5-seed42.exit\\n/tmp/agent-ml-exit/eval-vla-only-spatial-seed44.exit\\n/tmp/agent-ml-exit/eval-obs-only-spatial-norm02-seed46.exit\\n/tmp/agent-ml-exit/eval-obs-only-spatial-norm02-seed46-r2.exit\\n/tmp/agent-ml-exit/eval-vla-only-spatial-seed48.exit\\n/tmp/agent-ml-exit/eval-vla-only-spatial-seed49.exit\\n/tmp/agent-ml-exit/eval-vla-only-spatial-seed49-r2.exit\\n/tmp/agent-ml-exit/eval-crm-spatial-k10-seed49.exit\\n/tmp/agent-ml-exit/eval-adaptive-k-spatial-p50-seed44.exit\\n/tmp/agent-ml-exit/eval-adaptive-k-spatial-p50-seed44-r2.exit\\n/tmp/agent-ml-exit/eval-obs-only-spatial-norm02-seed42.exit\\n/tmp/agent-ml-exit/eval-adaptive-k-spatial-p90-seed42.exit\\n/tmp/agent-ml-exit/eval-adaptive-k-spatial-p75-seed44.exit\\n/tmp/agent-ml-exit/eval-adaptive-k-spatial-p25-seed44.exit\\n/tmp/agent-ml-exit/eval-obs-only-spatial-norm02-seed49.exit\\n/tmp/agent-ml-exit/eval-pi05-crm-spatial-seed42.exit\\n/tmp/agent-ml-exit/eval-pi05-crm-spatial-seed43.exit\\n/tmp/agent-ml-exit/eval-pi05-crm-spatial-seed44.exit\\n/tmp/agent-ml-exit/eval-supp-k2mean-spatial-s42.exit\\n/tmp/eval_crm_spatial_seed42.log\\n/tmp/eval_crm_spatial_seed43.log\\n/tmp/eval_crm_spatial_seed44.log\\n/tmp/eval_vla_spatial_seed43.log\\n/tmp/eval_vla_spatial_seed44.log\\n/tmp/eval_vla_spatial_seed42.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.34}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "b873cbe3-e9b8-4f4e-9c49-d55ff9769e08",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/tmp/agent-ml-exit/eval-obs-only-spatial-norm02-k5-seed42.exit\\\\n/tmp/agent-ml-exit/eval-vla-only-spatial-seed44.exit\\\\n/tmp/agent-ml-exit/eval-obs-only-spatial-norm02-seed46.exit\\\\n/tmp/agent-ml-exit/eval-obs-only-spatial-norm02-seed46-r2.exit\\\\n/tmp/agent-ml-exit/eval-vla-only-spatial-seed48.exit\\\\n/tmp/agent-ml-exit/eval-vla-only-spatial-seed49.exit\\\\n/tmp/agent-ml-exit/eval-vla-only-spatial-seed49-r2.exit\\\\n/tmp/agent-ml-exit/eval-crm-spatial-k10-seed49.exit\\\\n/tmp/agent-ml-exit/eval-adaptive-k-spatial-p50-seed44.exit\\\\n/tmp/agent-ml-exit/eval-adaptive-k-spatial-p50-seed44-r2.exit\\\\n/tmp/agent-ml-exit/eval-obs-only-spatial-norm02-seed42.exit\\\\n/tmp/agent-ml-exit/eval-adaptive-k-spatial-p90-seed42.exit\\\\n/tmp/agent-ml-exit/eval-adaptive-k-spatial-p75-seed44.exit\\\\n/tmp/agent-ml-exit/eval-adaptive-k-spatial-p25-seed44.exit\\\\n/tmp/agent-ml-exit/eval-obs-only-spatial-norm02-seed49.exit\\\\n/tmp/agent-ml-exit/eval-pi05-crm-spatial-seed42.exit\\\\n/tmp/agent-ml-exit/eval-pi05-crm-spatial-seed43.exit\\\\n/tmp/agent-ml-exit/eval-pi05-crm-spatial-seed44.exit\\\\n/tmp/agent-ml-exit/eval-supp-k2mean-spatial-s42.exit\\\\n/tmp/eval_crm_spatial_seed42.log\\\\n/tmp/eval_crm_spatial_seed43.log\\\\n/tmp/eval_crm_spatial_seed44.log\\\\n/tmp/eval_vla_spatial_seed43.log\\\\n/tmp/eval_vla_spatial_seed44.log\\\\n/tmp/eval_vla_spatial_seed42.log\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.34}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/tmp/agent-ml-exit/eval-obs-only-spatial-norm02-k5-seed42.exit\\n/tmp/agent-ml-exit/eval-vla-only-spatial-seed44.exit\\n/tmp/agent-ml-exit/eval-obs-only-spatial-norm02-seed46.exit\\n/tmp/agent-ml-exit/eval-obs-only-spatial-norm02-seed46-r2.exit\\n/tmp/agent-ml-exit/eval-vla-only-spatial-seed48.exit\\n/tmp/agent-ml-exit/eval-vla-only-spatial-seed49.exit\\n/tmp/agent-ml-exit/eval-vla-only-spatial-seed49-r2.exit\\n/tmp/agent-ml-exit/eval-crm-spatial-k10-seed49.exit\\n/tmp/agent-ml-exit/eval-adaptive-k-spatial-p50-seed44.exit\\n/tmp/agent-ml-exit/eval-adaptive-k-spatial-p50-seed44-r2.exit\\n/tmp/agent-ml-exit/eval-obs-only-spatial-norm02-seed42.exit\\n/tmp/agent-ml-exit/eval-adaptive-k-spatial-p90-seed42.exit\\n/tmp/agent-ml-exit/eval-adaptive-k-spatial-p75-seed44.exit\\n/tmp/agent-ml-exit/eval-adaptive-k-spatial-p25-seed44.exit\\n/tmp/agent-ml-exit/eval-obs-only-spatial-norm02-seed49.exit\\n/tmp/agent-ml-exit/eval-pi05-crm-spatial-seed42.exit\\n/tmp/agent-ml-exit/eval-pi05-crm-spatial-seed43.exit\\n/tmp/agent-ml-exit/eval-pi05-crm-spatial-seed44.exit\\n/tmp/agent-ml-exit/eval-supp-k2mean-spatial-s42.exit\\n/tmp/eval_crm_spatial_seed42.log\\n/tmp/eval_crm_spatial_seed43.log\\n/tmp/eval_crm_spatial_seed44.log\\n/tmp/eval_vla_spatial_seed43.log\\n/tmp/eval_vla_spatial_seed44.log\\n/tmp/eval_vla_spatial_seed42.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.34}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 55_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_017xq7Wigoo8nv6qDThBvPJu`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "head -5 /root/acr-vla-conformal-refinement/src/evaluate.py",
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
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "a7dfa540-32ab-418e-881b-488e80dcf957",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FFPMVT2aPFFS9o3wv5Whbk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1479,
      "cache_read_input_tokens": 49439,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1479
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

_source line 56 · 2026-05-24T08:27:29.281Z_

<details><summary>↩ Tool result · `toolu_017xq7Wigoo8nv6qDThBvPJu`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nLIBERO evaluation script for ACR-VLA.\\n\\nRollout loop:\\n  1. Load LIBERO env + task suite\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.33}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "004e6b8f-8d46-48a2-b29a-84ee05552a6f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\"\\\\\\\"\\\\\\\"\\\\nLIBERO evaluation script for ACR-VLA.\\\\n\\\\nRollout loop:\\\\n  1. Load LIBERO env + task suite\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.33}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nLIBERO evaluation script for ACR-VLA.\\n\\nRollout loop:\\n  1. Load LIBERO env + task suite\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.33}}"
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
No recent log files for the current s45/s46 spatial runs. These were started directly in tmux without output redirection. So I need to rely on the tmux scrollback.

Let me estimate based on what I know: The LIBERO-Spatial suite has 10 tasks. The task names I've seen in the scrollback (alphabetically ordered) are:
- from_table_center
- in_the_top_drawer (crm-s46 completed this)
- next_to_the_cookie_box
- next_to_the_ramekin


- on_the_cookie_box
- on_the_ramekin
- on_the_stove

And I know there are others like pick_up_the_black_bowl variants. Since the more advanced experiments are progressing to "on_the_stove" while some are still on "on_the_ramekin", I need to find the actual task ordering. Let me check a completed JSON file from a Spatial run to see the exact sequence.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "77b1ab54-0cd5-4be3-aea6-582f7e2a0937",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MDq3vvxpKFP9VmeJJosGuc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1824,
      "cache_read_input_tokens": 50918,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1824
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

_source line 58_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01HY5sZMRDUG8fYoXpospnJQ`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed42.json",
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
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "bf733637-e6c3-4c6a-a0cd-19ebb7c40554",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MDq3vvxpKFP9VmeJJosGuc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1824,
      "cache_read_input_tokens": 50918,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1824
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

_source line 59 · 2026-05-24T08:27:44.836Z_

<details><summary>↩ Tool result · `toolu_01HY5sZMRDUG8fYoXpospnJQ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"mean\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.815,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "4dd1eca9-a65f-4bff-a213-4ef739f51ec4",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"mode\\\\\\\": \\\\\\\"vla_only\\\\\\\",\\\\n  \\\\\\\"baseline_mode\\\\\\\": \\\\\\\"mean\\\\\\\",\\\\n  \\\\\\\"benchmark\\\\\\\": \\\\\\\"spatial\\\\\\\",\\\\n  \\\\\\\"n_rollouts\\\\\\\": 20,\\\\n  \\\\\\\"overall_success_rate\\\\\\\": 0.815,\\\\n  \\\\\\\"per_task\\\\\\\": {\\\\n    \\\\\\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.95,\\\\n      \\\\\\\"successes\\\\\\\": 19,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.95,\\\\n      \\\\\\\"successes\\\\\\\": 19,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 1.0,\\\\n      \\\\\\\"successes\\\\\\\": 20,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.7,\\\\n      \\\\\\\"successes\\\\\\\": 14,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n      \\\\\\\"successes\\\\\\\": 0,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.95,\\\\n      \\\\\\\"successes\\\\\\\": 19,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.8,\\\\n      \\\\\\\"successes\\\\\\\": 16,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.85,\\\\n      \\\\\\\"successes\\\\\\\": 17,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.95,\\\\n      \\\\\\\"successes\\\\\\\": 19,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.32}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"vla_only\\\",\\n  \\\"baseline_mode\\\": \\\"mean\\\",\\n  \\\"benchmark\\\": \\\"spatial\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.815,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 1.0,\\n      \\\"successes\\\": 20,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.7,\\n      \\\"successes\\\": 14,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 16,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.85,\\n      \\\"successes\\\": 17,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\\\": {\\n      \\\"success_rate\\\": 0.95,\\n      \\\"successes\\\": 19,\\n      \\\"total\\\": 20\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 60_

<details><summary>Logged reasoning block</summary>

```text
Now I know the 10 tasks in LIBERO-Spatial (in order they were executed):
1. between_the_plate_and_the_ramekin
2. next_to_the_ramekin
3. from_table_center
4. on_the_cookie_box
5. in_the_top_drawer
6. on_the_ramekin
7. next_to_the_cookie_box
8. on_the_stove
9. next_to_the_plate
10. on_the_wooden_cabinet

Now let me map the current progress:


- **crm-norm005-s46** (GPU 0): I can see it's progressed through "next_to_ramekin" (95%) and "in_the_top_drawer" (70%), and is currently working on "on_the_ramekin" at rollout 10/20, so it's on task 6 out of 10.
- **vla-only-s45**: Finished "on_the_ramekin" and is now on "on_the_stove" at rollout 5/20, placing it at task 8 out of 10.
- **crm-norm005-s45** (GPU 3): Also on "on_the_stove" at rollout 5/20, task 8 out of 10.
- **adapt-s45** (GPU 4): Just completed "on_the_ramekin" at rollout 20/20 and is about to move into task 7, which should be "next_to_the_cookie_box".

Actually, let me trace through the scrollback more carefully. Looking at the second tmux capture, adapt-s45 shows "pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate" completed at 100% (20/20), but then the extended scrollback shows that same task at rollout 20/20 with only 15/20 successes so far. I'm getting confused about the current state. Looking at the scrollback more carefully, I can see the tasks were executed in a different order than they appear in the JSON output. Tracing through the visible history, it looks like the execution went through several tasks before reaching the ramekin task that just completed, so I need to map out the actual sequence from the terminal output rather than relying on the JSON order.

Now I'm noticing something odd—vla-only-s45 and crm-norm005-s45 appear to be further along in the task sequence than adapt-s45, which suggests they might be executing faster or using a different approach. Let me check if vla-only-s45 is using K=1, which would mean it's skipping the refinement step entirely. Both experiments are at the same task position—rollout 5/20 on "on_the_stove"—which means they've completed 7 tasks and are working on task 8, though the tmux buffer only shows 3 completed success lines due to overflow. I'm now mapping out the actual progress by tracking task names in execution order to see where each experiment really stands. I'm seeing that the scrollback history is incomplete—those models showing task 8/10 have actually completed 7 tasks already, but earlier ones scrolled out of view. Looking at the visible completion records for vla-only-s45, I can trace the sequence: "next_to_ramekin" finished at 95%, followed by "in_top_drawer" at 70%, then "on_ramekin", which gives me the ordering pattern before the current "on_the_stove" rollout. Looking at the detailed capture output for crm-s46, I can see the execution sequence more clearly now: next_to_ramekin, from_table_center, on_cookie_box, in_top_drawer, on_ramekin, and continuing through next_to_cookie_box and on_stove. The rollout completion percentages help confirm the ordering of these task groups.

Mapping this against the progress data, crm-norm005-s46 is currently on task 6 (on_ramekin) at rollout 10/20, which puts it at approximately 55% completion overall.

vla-only-s45 and crm-norm005-s45 are both further along on task 8 (on_stove) with only 5/20 rollout remaining, so they're around 75% done.

adapt-s45 and vla-only-s46 have finished task 6 and moved into task 7, putting them at roughly 60% completion.

But wait—I'm noticing something inconsistent. In the earlier capture, adapt-s45 showed next_to_cookie_box completed at 100%, but that doesn't align with where it appears in the task sequence now.

Let me look at the detailed rollout data more carefully. The first capture shows adapt-s45 running the next_to_cookie_box task with all rollouts succeeding (5/5, 10/10, 15/15, 20/20), which suggests that task completed fully.

But then the extended capture shows the same task at rollout 20/20 only has 15/20 successes, which contradicts the earlier result. It looks like the later capture is showing a different run or the data got mixed up between the two tasks—the on_the_ramekin variant appears in the second capture instead. I'm tracking the task execution sequence across these spatial reasoning evaluations. Looking at the rollout data, I can see the progression: next_to_cookie_box completed at 100%, then in_top_drawer at 75%, followed by on_ramekin finishing at 20/20. The ordering suggests on_the_stove would be the next task to execute, with subsequent tasks including next_to_plate and on_wooden_cabinet still pending. I'm noticing the sequence differs between the two models—crm-s46 has next_to_ramekin, from_table_center, and on_cookie_box appearing before in_top_drawer, whereas adapt-s45 goes directly from next_to_cookie_box to in_top_drawer, then on_ramekin. The on_ramekin variant is currently at 10/20 rollouts for crm-s46.

Rather than getting caught up in the exact ordering differences, what matters is that all five experiments are actively running and progressing through the later stages of the task suite—they're roughly 60-80% complete and should wrap up within the next hour or so. Now I need to look into the lerobot experiments since they're not showing up in the registry at all, so maybe they were registered under different names.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "a4e96d65-56f9-43cf-a28f-f96edce74b0a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KEWyBHfcuH4vHEpm9hjR9t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1491,
      "cache_read_input_tokens": 52742,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1491
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

_source line 61_

两个 lerobot 实验在 registry 中不存在。所有 bjb2-28827 实验仍在运行。让我确认 lerobot 实验的准确名称，并获取每个 bjb2-28827 实验的实时 task 位置。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "66a2ee87-e2a3-4198-9899-688eb959126b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KEWyBHfcuH4vHEpm9hjR9t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1491,
      "cache_read_input_tokens": 52742,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1491
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

<details open><summary>🔧 Tool call — Bash · `toolu_01MTB25L2W3VuvSL4FEGtkYx`</summary>

```json
{
  "command": "grep -oE '\"eval-[^\"]*lerobot[^\"]*\"' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/4a8246d3-c96e-4959-82ff-767c57b966c8/tool-results/mcp-agent-ml-research-read_registry-1779611091392.txt; echo \"---\"; grep -oE '\"eval-[^\"]*goal-seed43[^\"]*\"' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/4a8246d3-c96e-4959-82ff-767c57b966c8/tool-results/mcp-agent-ml-research-read_registry-1779611091392.txt; echo \"---\"; grep -oE '\"eval-[^\"]*spatial-seed43[^\"]*\"' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/4a8246d3-c96e-4959-82ff-767c57b966c8/tool-results/mcp-agent-ml-research-read_registry-1779611091392.txt",
  "description": "Search for lerobot and seed43 experiment IDs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "71b53c23-772f-4a1b-8266-8e141012b593",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KEWyBHfcuH4vHEpm9hjR9t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1491,
      "cache_read_input_tokens": 52742,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1491
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

_source line 63 · 2026-05-24T08:29:11.440Z_

<details><summary>↩ Tool result · `toolu_01MTB25L2W3VuvSL4FEGtkYx`</summary>

```text
---
---
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "bb6122fa-e1e0-419a-9c3e-455b030e805e",
  "tool_use_result": {
    "stdout": "---\n---",
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

_source line 64_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01NY4pofd2N9fYNhVPDCEa7J`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "for s in eval-supp-crm-norm005-spatial-s46 eval-supp-vla-only-spatial-s45 eval-supp-crm-norm005-spatial-s45 eval-supp-adapt-tau025-spatial-s45 eval-supp-vla-only-spatial-s46; do echo \"=== $s ===\"; last_task=$(tmux capture-pane -t \"$s\" -p 2>&1 | grep -oP \"(?<=  )\\S+(?=:)\" | tail -1); last_rollout=$(tmux capture-pane -t \"$s\" -p 2>&1 | grep \"rollout\" | tail -1); echo \"task=$last_task\"; echo \"rollout=$last_rollout\"; done",
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
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "1d2547db-4ce6-4da6-9997-2fa8d3ac5aed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KEWyBHfcuH4vHEpm9hjR9t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1491,
      "cache_read_input_tokens": 52742,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1491
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

_source line 65 · 2026-05-24T08:29:14.734Z_

<details><summary>↩ Tool result · `toolu_01NY4pofd2N9fYNhVPDCEa7J`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== eval-supp-crm-norm005-spatial-s46 ===\\ntask=pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\nrollout=  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 15/20\\n=== eval-supp-vla-only-spatial-s45 ===\\ntask=pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\nrollout=  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 5/20, s\\n=== eval-supp-crm-norm005-spatial-s45 ===\\ntask=pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\nrollout=  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 5/20, s\\n=== eval-supp-adapt-tau025-spatial-s45 ===\\ntask=pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\nrollout=  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 5/20, s\\n=== eval-supp-vla-only-spatial-s46 ===\\ntask=pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\nrollout=  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 20/20\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "24286adc-042e-403b-bd9e-de7b5c2ca7fb",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"=== eval-supp-crm-norm005-spatial-s46 ===\\\\ntask=pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\\nrollout=  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 15/20\\\\n=== eval-supp-vla-only-spatial-s45 ===\\\\ntask=pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\\nrollout=  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 5/20, s\\\\n=== eval-supp-crm-norm005-spatial-s45 ===\\\\ntask=pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\\nrollout=  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 5/20, s\\\\n=== eval-supp-adapt-tau025-spatial-s45 ===\\\\ntask=pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\\nrollout=  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 5/20, s\\\\n=== eval-supp-vla-only-spatial-s46 ===\\\\ntask=pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\\nrollout=  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 20/20\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"=== eval-supp-crm-norm005-spatial-s46 ===\\ntask=pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\nrollout=  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 15/20\\n=== eval-supp-vla-only-spatial-s45 ===\\ntask=pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\nrollout=  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 5/20, s\\n=== eval-supp-crm-norm005-spatial-s45 ===\\ntask=pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\nrollout=  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 5/20, s\\n=== eval-supp-adapt-tau025-spatial-s45 ===\\ntask=pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\nrollout=  pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate: rollout 5/20, s\\n=== eval-supp-vla-only-spatial-s46 ===\\ntask=pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\nrollout=  pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate: rollout 20/20\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 66_

<details><summary>Logged reasoning block</summary>

```text
The lerobot experiments don't exist in the registry at all - not even under different names. The grep for "lerobot", "goal-seed43", and "spatial-seed43" all returned nothing.

Now let me map the exact positions. From the seed42 results JSON, the task execution order is:
1. between_plate_and_ramekin
2. next_to_ramekin
3. from_table_center
4. on_cookie_box
5. in_top_drawer


6. on_ramekin
7. next_to_cookie_box
8. on_stove
9. next_to_plate
10. on_wooden_cabinet

Looking at the current experiment status, I can see several runs in progress across different GPUs - crm-norm005-s46 is on task 6 with 15 rollouts completed, while both vla-only-s45 and crm-norm005-s45 are stuck on task 8 with only 5 rollouts each, and adapt-tau025-s45 appears to be cut off mid-entry.

For vla-only-s46, there's a discrepancy between what the task line captured and the actual rollout - the regex picked up "next_to_cookie_box" as the task name, but the rollout shows "on_the_ramekin" with 20/20 complete, suggesting the parsing might have grabbed text from the wrong part of the output. Looking at the latest output for vla-only-s46, there's a discrepancy—the task field shows it's on the next_to_cookie_box task, but the rollout line is displaying progress from the previous on_ramekin task, which suggests the output might be mixing lines from different points in the scrollback. Looking at the tmux pane more carefully, "next_to_cookie_box" is probably scrolled partially out of view. I've spent enough time tracking these details—let me just consolidate what I've confirmed: the two lerobot experiments don't exist in the registry despite multiple search attempts, and all five processes in the bjb2-28827 spatial task are still running.

Generating progress table...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "39a7e7cc-82e4-48d7-b7af-034c6d4dec16",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M9hY9vWz2qa6pKH8rvxbhS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6063,
      "cache_read_input_tokens": 54233,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6063
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

_source line 67_

Registry 中完全不存在 "eval-smolvla-lerobot-*" 命名的实验（包括搜 "lerobot"、"goal-seed43"、"spatial-seed43" 都无结果）。现在汇总结果。

---

## 任务 1: Stale lerobot 实验

**`eval-smolvla-lerobot-goal-seed43-v3` 和 `eval-smolvla-lerobot-spatial-seed43-v3` 在 registry 中不存在。** 搜索了所有实验（包含关键字 "lerobot"、"goal-seed43"、"spatial-seed43"），均无匹配。可能是名称记错、已被删除、或属于其他项目。

---

## 任务 2: bjb2-28827 Spatial 实验进度

**全部 5 个进程存活**（已通过 `ps -p` 确认），运行时间约 1h30m。

LIBERO-Spatial 共 10 个 task × 20 rollouts/task。根据 tmux 输出的当前 task 位置：

| 实验 | GPU | PID | 当前 task | 进度估算 |
|---|---|---|---|---|
| crm-norm005-spatial-s46 | 0 | 121241 | on_ramekin r15/20 | ~task 6/10 |
| vla-only-spatial-s45 | 2 | 96831 | on_stove r5/20 | ~task 8/10 |
| crm-norm005-spatial-s45 | 3 | 97070 | on_stove r5/20 | ~task 8/10 |
| adapt-tau025-spatial-s45 | 4 | 97307 | on_stove r5/20 | ~task 8/10 |
| vla-only-spatial-s46 | 5 | 97550 | next_to_cookie_box ~r15/20 | ~task 7/10 |

**预计全部在 30-60 分钟内完成。** crm-norm005-s46 因晚启动 23 分钟，进度最慢。

无已完成的实验需要收割，全部仍在跑。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "uuid": "0eedf205-0c8a-44b6-adaa-43484c9bba8f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M9hY9vWz2qa6pKH8rvxbhS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6063,
      "cache_read_input_tokens": 54233,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6063
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

### Task result

_source line 68_

Registry 中完全不存在 "eval-smolvla-lerobot-*" 命名的实验（包括搜 "lerobot"、"goal-seed43"、"spatial-seed43" 都无结果）。现在汇总结果。

---

## 任务 1: Stale lerobot 实验

**`eval-smolvla-lerobot-goal-seed43-v3` 和 `eval-smolvla-lerobot-spatial-seed43-v3` 在 registry 中不存在。** 搜索了所有实验（包含关键字 "lerobot"、"goal-seed43"、"spatial-seed43"），均无匹配。可能是名称记错、已被删除、或属于其他项目。

---

## 任务 2: bjb2-28827 Spatial 实验进度

**全部 5 个进程存活**（已通过 `ps -p` 确认），运行时间约 1h30m。

LIBERO-Spatial 共 10 个 task × 20 rollouts/task。根据 tmux 输出的当前 task 位置：

| 实验 | GPU | PID | 当前 task | 进度估算 |
|---|---|---|---|---|
| crm-norm005-spatial-s46 | 0 | 121241 | on_ramekin r15/20 | ~task 6/10 |
| vla-only-spatial-s45 | 2 | 96831 | on_stove r5/20 | ~task 8/10 |
| crm-norm005-spatial-s45 | 3 | 97070 | on_stove r5/20 | ~task 8/10 |
| adapt-tau025-spatial-s45 | 4 | 97307 | on_stove r5/20 | ~task 8/10 |
| vla-only-spatial-s46 | 5 | 97550 | next_to_cookie_box ~r15/20 | ~task 7/10 |

**预计全部在 30-60 分钟内完成。** crm-norm005-s46 因晚启动 23 分钟，进度最慢。

无已完成的实验需要收割，全部仍在跑。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 362738,
  "duration_api_ms": 353202,
  "num_turns": 23,
  "stop_reason": "end_turn",
  "session_id": "4a8246d3-c96e-4959-82ff-767c57b966c8",
  "total_cost_usd": 0.9556657500000001,
  "usage": {
    "input_tokens": 18,
    "cache_creation_input_tokens": 48455,
    "cache_read_input_tokens": 554364,
    "output_tokens": 14967,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 48455,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 2308,
        "cache_read_input_tokens": 54233,
        "cache_creation_input_tokens": 6063,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 6063
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1285,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001375,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 18,
      "outputTokens": 14967,
      "cacheReadInputTokens": 554364,
      "cacheCreationInputTokens": 48455,
      "webSearchRequests": 0,
      "costUSD": 0.95429075,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "822eb009-0aed-4772-b3d5-f26c6a2631c7"
}
```

</details>

---
