# prep exp 059 walker 008d s5

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 40
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/workers/worker_prep_exp_059_walker_008d_s5_20260524T030707.log`
- **Structured JSON:** [`2c3f1b2c8d50e3cd549e.json`](../../sessions/2c/2c3f1b2c8d50e3cd549e.json)

## Before a recorded user message

40 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon",
  "session_id": "2fe83aea-5863-4eb4-8029-aa58f80fcf56",
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
  "uuid": "2b59ea17-39a4-415c-9de3-8b9810df243b",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Assistant

_source line 3_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to prepare and submit for approval a new experiment (Walker 008d trained dt_emb extra seed). Let me follow the steps:

1. First, check the registry for exp_008d to confirm its seed
2. Register the new experiment
3. Prepare the training command

Let me start by reading the registry for exp_008d and also for exp_008d_civo_trigger_s3 to get the exact config.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2fe83aea-5863-4eb4-8029-aa58f80fcf56",
  "uuid": "747f4eb6-d2d4-4431-b65e-5cb2efa5662a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VHYK2wTZv5V9VhMRzG1Tg7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12078,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12078
      },
      "output_tokens": 24,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01MXBxF5pbWmybPKXKNNnHin`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__update_registry",
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
  "session_id": "2fe83aea-5863-4eb4-8029-aa58f80fcf56",
  "uuid": "50064504-e64e-4819-8f7b-aadbe6013b39",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VHYK2wTZv5V9VhMRzG1Tg7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12078,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12078
      },
      "output_tokens": 24,
      "service_tier": "standard",
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

_source line 5 · 2026-05-24T03:07:23.632Z_

<details><summary>↩ Tool result · `toolu_01MXBxF5pbWmybPKXKNNnHin`</summary>

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
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2fe83aea-5863-4eb4-8029-aa58f80fcf56",
  "uuid": "0aa2612a-1b47-4ad2-a3ed-35fea4ab6e90",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__update_registry"
    ],
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__update_registry",
    "total_deferred_tools": 26
  }
}
```

</details>

---

### Runtime record

_source line 6_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1779597600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "c84b8fde-fc5f-4192-9e24-55fc4056906d",
  "session_id": "2fe83aea-5863-4eb4-8029-aa58f80fcf56"
}
```

---

### Assistant

_source line 7_

查询 exp_008d 和 exp_008d_civo_trigger_s3 的 spec 信息。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2fe83aea-5863-4eb4-8029-aa58f80fcf56",
  "uuid": "bfe02c24-13e9-4a5b-9b06-12f052d712b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017kv5rzZeAE9q6z3rA6mVS1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1054,
      "cache_read_input_tokens": 23525,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1054
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01WMsXKA8DrkhwgWCZ2A96tc`</summary>

```json
{
  "filters": {
    "exp_id": "exp_008d"
  },
  "fields": [
    "spec"
  ],
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2fe83aea-5863-4eb4-8029-aa58f80fcf56",
  "uuid": "9ab8acf3-08ef-40a5-8602-3f1376ef0eb6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017kv5rzZeAE9q6z3rA6mVS1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1054,
      "cache_read_input_tokens": 23525,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1054
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

_source line 9 · 2026-05-24T03:07:27.704Z_

<details><summary>↩ Tool result · `toolu_01WMsXKA8DrkhwgWCZ2A96tc`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5344}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2fe83aea-5863-4eb4-8029-aa58f80fcf56",
  "uuid": "c67a682f-8a4d-4864-a25d-6095bd8811e7",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.5344}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5344}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01BxjoDc6CqXvAhovJ9G3Mm8`</summary>

```json
{
  "filters": {
    "exp_id": "exp_008d_civo_trigger_s3"
  },
  "fields": [
    "spec"
  ],
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2fe83aea-5863-4eb4-8029-aa58f80fcf56",
  "uuid": "442fb968-46c2-4127-b0ad-8dfa9b0bb429",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017kv5rzZeAE9q6z3rA6mVS1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1054,
      "cache_read_input_tokens": 23525,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1054
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

_source line 11 · 2026-05-24T03:07:28.220Z_

<details><summary>↩ Tool result · `toolu_01BxjoDc6CqXvAhovJ9G3Mm8`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4701}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2fe83aea-5863-4eb4-8029-aa58f80fcf56",
  "uuid": "4e0741c7-9cd4-48e8-b426-d85e943abbf3",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4701}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4701}}"
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
Both queries returned empty results. Let me try broader searches - maybe the exp_id format is different, or I need to search differently.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2fe83aea-5863-4eb4-8029-aa58f80fcf56",
  "uuid": "d4877a19-ec8f-4fde-8498-8f25c25ad612",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QA8Ek7MvuHAWD9sBXqUAWA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 466,
      "cache_read_input_tokens": 24579,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 466
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

两个都没找到。试试模糊搜索 008d 相关实验。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2fe83aea-5863-4eb4-8029-aa58f80fcf56",
  "uuid": "3a189b72-f638-407b-a2e1-34b805d57675",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QA8Ek7MvuHAWD9sBXqUAWA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 466,
      "cache_read_input_tokens": 24579,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 466
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_014yBCq44eMjaVTTkmBb7zYi`</summary>

```json
{
  "filters": {},
  "fields": [
    "exp_id",
    "spec"
  ],
  "project": "event-gated-adaptive-horizon",
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
  "session_id": "2fe83aea-5863-4eb4-8029-aa58f80fcf56",
  "uuid": "4a2c42de-21a1-4814-9b54-39b80f50484f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QA8Ek7MvuHAWD9sBXqUAWA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 466,
      "cache_read_input_tokens": 24579,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 466
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

_source line 15 · 2026-05-24T03:07:33.978Z_

<details><summary>↩ Tool result · `toolu_014yBCq44eMjaVTTkmBb7zYi`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp_057_frozen_dt_emb_walker_s2\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_057_frozen_dt_emb_walker_s2\", \"server\": \"bjb1-45299\", \"gpu_ids\": [1], \"pid\": 157775, \"data_path\": \"dmc_walker_walk\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, Walker s2)\", \"seed\": 2, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"dmc_walker_walk (online eval)\", \"log_path\": \"logdir/exp_057_frozen_dt_emb_walker_s2/train.log\", \"checkpoint_path\": \"logdir/exp_057_frozen_dt_emb_walker_s2/checkpoint_225000.pt\"}}, \"exp_058_frozen_dt_emb_cheetah_s1\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_058_frozen_dt_emb_cheetah_s1\", \"server\": \"bjb1-45299\", \"gpu_ids\": [0], \"pid\": 164830, \"data_path\": \"dmc_cheetah_run\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, Cheetah s1)\", \"seed\": 1, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"dmc_cheetah_run (online eval)\", \"log_path\": \"logdir/exp_058_frozen_dt_emb_cheetah_s1/train.log\", \"checkpoint_path\": \"logdir/exp_058_frozen_dt_emb_cheetah_s1/checkpoint_225000.pt\"}}, \"exp_056_peginsertion_frozen_s1\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_EGL_DEVICE_ID=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs maniskill_peginsertion --task maniskill_PegInsertionSide-v1 --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_056_peginsertion_frozen_s1\", \"server\": \"bjb1-40020\", \"gpu_ids\": [1], \"pid\": 346430, \"data_path\": \"ManiSkill PegInsertionSide-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, fixed dt=2, ManiSkill PegInsertion s1)\", \"seed\": 1, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"PegInsertionSide-v1 (online eval)\", \"log_path\": \"logdir/exp_056_peginsertion_frozen_s1/train.log\", \"checkpoint_path\": \"logdir/exp_056_peginsertion_frozen_s1/checkpoint_202500.pt\"}}, \"exp_055_peginsertion_civo_trigger_s1\": {\"spec\": {\"command\": \"python -u dreamer.py --configs maniskill_peginsertion --task maniskill_PegInsertionSide-v1 --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_055_peginsertion_civo_trigger_s1\", \"server\": \"bjb1-40020\", \"gpu_ids\": [0], \"pid\": 345223, \"data_path\": \"ManiSkill PegInsertionSide-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO config, PegInsertion)\", \"seed\": 1, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"PegInsertionSide-v1 (online eval)\", \"log_path\": \"logdir/exp_055_peginsertion_civo_trigger_s1/train.log\"}}, \"exp_054_pickcube_frozen_s0\": {\"spec\": {\"command\": \"python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --seed 0 --steps 210000 --compile False --device cuda:0 --checkpoint_every 25000 --logdir logdir/exp_054_pickcube_frozen_s0\", \"server\": \"bjb1-45299\", \"gpu_ids\": [0], \"pid\": 133956, \"data_path\": \"ManiSkill PickCube-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, CIVO config, ManiSkill PickCube)\", \"seed\": 0, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"PickCube-v1 (online eval)\", \"log_path\": \"logdir/exp_054_pickcube_frozen_s0/metrics.jsonl\", \"checkpoint_path\": \"logdir/exp_054_pickcube_frozen_s0/checkpoint.ckpt\"}}, \"exp_053_peginsertion_frozen_s0\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_EGL_DEVICE_ID=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs maniskill_peginsertion --task maniskill_PegInsertionSide-v1 --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_053_peginsertion_frozen_s0\", \"server\": \"bjb1-45299\", \"gpu_ids\": [1], \"pid\": 123495, \"data_path\": \"ManiSkill PegInsertionSide-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, fixed dt=2, ManiSkill PegInsertion)\", \"seed\": 0, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"PegInsertionSide-v1 (online eval)\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_053_peginsertion_frozen_s0.log\", \"checkpoint_path\": \"logdir/exp_053_peginsertion_frozen_s0/checkpoint.ckpt\"}}, \"exp_050_peginsertion_civo_trigger_s0\": {\"spec\": {\"command\": \"LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs maniskill_peginsertion --task maniskill_PegInsertionSide-v1 --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_050_peginsertion_civo_trigger_s0\", \"server\": \"bjb1-40020\", \"data_path\": \"ManiSkill PegInsertionSide-v1 (state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 + CIVO trigger (gate_fixed_dt=2)\", \"seed\": 0, \"pid\": 304736, \"gpu_ids\": [0], \"log_path\": \"logdir/exp_050_peginsertion_civo_trigger_s0/train.log\", \"checkpoint_path\": \"logdir/exp_050_peginsertion_civo_trigger_s0\"}}, \"exp_051_stackcube_frozen_dt_emb_s0\": {\"spec\": {\"command\": \"python -u dreamer.py --configs maniskill_stackcube --task maniskill_StackCube-v1 --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_051_stackcube_frozen_dt_emb_s0\", \"server\": \"bjb1-40020\", \"gpu_ids\": [1], \"pid\": 305974, \"data_path\": \"ManiSkill StackCube-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, ManiSkill StackCube)\", \"seed\": 0, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"StackCube-v1 (online eval)\", \"log_path\": \"logdir/exp_051_stackcube_frozen_dt_emb_s0.log\", \"checkpoint_path\": \"logdir/exp_051_stackcube_frozen_dt_emb_s0/checkpoint_202500.pt\"}}, \"exp_052_stackcube_civo_trigger_s1\": {\"spec\": {\"command\": \"python -u dreamer.py --configs maniskill_stackcube --task maniskill_StackCube-v1 --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_052_stackcube_civo_trigger_s1\", \"server\": \"bjb1-45299\", \"gpu_ids\": [0], \"pid\": 103781, \"data_path\": \"ManiSkill StackCube-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO config, ManiSkill StackCube)\", \"seed\": 1, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"StackCube-v1 (online eval)\", \"log_path\": \"logdir/exp_052_stackcube_civo_trigger_s1/train.log\"}}, \"exp_049_stackcube_civo_trigger_s0\": {\"spec\": {\"command\": \"python -u dreamer.py --configs maniskill_stackcube --task maniskill_StackCube-v1 --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_049_stackcube_civo_trigger_s0\", \"server\": \"bjb1-45299\", \"gpu_ids\": [1], \"pid\": 91395, \"data_path\": \"ManiSkill StackCube-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO config, ManiSkill StackCube)\", \"seed\": 0, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"StackCube-v1 (online eval)\", \"log_path\": \"logdir/exp_049_stackcube_civo_trigger_s0/train.log\"}}, \"exp_048_cheetah_civo_extension\": {\"spec\": {\"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 300000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_048_cheetah_civo_extension\", \"server\": \"bjb1-45299\", \"gpu_ids\": [0], \"pid\": 88654, \"data_path\": \"dmc_cheetah_run (online RL)\", \"data_count\": 300000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO config, Cheetah)\", \"seed\": 0, \"checkpoint_source\": \"exp_010b_cheetah_civo_trigger_s0/latest.pt (step 105K, NVE=70.64)\", \"eval_data\": \"dmc_cheetah_run (online eval)\", \"log_path\": \"logdir/exp_048_cheetah_civo_extension/train.log\"}}, \"exp_047_frozen_dt_emb_walker_s1\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_047_frozen_dt_emb_walker_s1\", \"server\": \"bjb1-40020\", \"data_path\": \"dmc_walker_walk\", \"data_count\": 210000, \"model_name\": \"dreamer_gated_frozen_dt_emb\", \"seed\": 1, \"eval_data\": \"dmc_walker_walk (online eval)\", \"checkpoint_source\": \"N/A (training from scratch)\"}}, \"exp_046_frozen_dt_emb_cheetah\": {\"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_046_frozen_dt_emb_cheetah\", \"server\": \"bjb1-40020\", \"seed\": 0, \"model_name\": \"dreamerv3-cheetah-frozen-dt-emb\", \"data_path\": \"dmc_cheetah_run\", \"data_count\": 210000, \"eval_data\": \"dmc_cheetah_run (online eval)\", \"checkpoint_source\": \"N/A (training from scratch)\"}}, \"exp_044_gradient_stop_walker\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True --logdir logdir/exp_044_gradient_stop_walker\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:1\"], \"pid\": \"68371\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_044_gradient_stop_walker.log\", \"submitted_at\": \"2026-05-22T09:08:10.295Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"DMC Walker Walk\", \"data_count\": 210000, \"model_name\": \"DreamerV3 + reward_dt_emb_detach\", \"seed\": 0, \"checkpoint_source\": \"N/A - training from scratch\", \"eval_data\": \"dmc_walker_walk\", \"wall_clock_seconds\": 25212.4, \"gpu_hours\": 7.0}}, \"exp_045_treatment_extension_008d_s3\": {\"spec\": {\"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 300000 --seed 3 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_045_treatment_extension_008d_s3\", \"server\": \"bjb1-45299\", \"gpu_ids\": [0], \"pid\": \"70945\", \"data_path\": \"dmc_walker_walk (online RL)\", \"data_count\": 300000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO config)\", \"seed\": 3, \"checkpoint_source\": \"exp_008d_civo_trigger_s3/latest.pt (step 112K)\", \"eval_data\": \"dmc_walker_walk (online eval, same as training env)\", \"log_path\": \"logdir/exp_045_treatment_extension_008d_s3/train.log\"}}, \"exp_043_008f_walker_s1\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --logdir logdir/exp_043_008f_walker_s1\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Walker Walk\", \"gpu\": [\"cuda:1\"], \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_043_008f_walker_s1\", \"model_name\": \"DreamerV3 (no dt_emb, 008f control)\", \"pid\": \"250627\", \"seed\": 1, \"server\": \"bjb1-40020\", \"submitted_via\": \"submit_training_job\"}}, \"exp_042_frozen_dt_emb_walker\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --logdir logdir/exp_042_frozen_dt_emb_walker\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Walker Walk\", \"gpu\": [\"cuda:0\"], \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_042_frozen_dt_emb_walker\", \"model_name\": \"DreamerV3 + frozen dt_emb\", \"pid\": \"251336\", \"seed\": 0, \"server\": \"bjb1-40020\"}}, \"exp_040_wide_dual_critic_cheetah\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --logdir logdir/exp_040_wide_dual_critic_cheetah\\\"\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_040_wide_dual_critic_cheetah.log\", \"pid\": \"52397\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-21T19:51:11.519Z\", \"submitted_via\": \"submit_training_job\", \"seed\": 1, \"wall_clock_seconds\": 49438.9, \"gpu_hours\": 13.73}}, \"exp_041_dual_critic_walker_s3\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 3 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --logdir logdir/exp_041_dual_critic_walker_s3\\\"\", \"gpu\": [\"cuda:1\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_041_dual_critic_walker_s3.log\", \"pid\": \"51103\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-22T02:38:20.728Z\", \"submitted_via\": \"submit_training_job\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_041_dual_critic_walker_s3/checkpoint.pt\", \"checkpoint_source\": \"N/A - training from scratch\", \"eval_data\": \"dmc_walker_walk\", \"wall_clock_seconds\": 23112.0, \"gpu_hours\": 6.42}}, \"exp_039_narrow_dual_critic_walker_s1\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_039_narrow_dual_critic_walker_s1/latest.pt\", \"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --narrow_dual_critic True --logdir logdir/exp_039_narrow_dual_critic_walker_s1\\\"\", \"eval_data\": \"N/A - training experiment\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 10.06, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_039_narrow_dual_critic_walker_s1.log\", \"pid\": \"198771\", \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-21T16:31:39.634Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 36234.0}}, \"exp_038_dual_critic_walker_s2\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_038_dual_critic_walker_s2/latest.pt\", \"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"bash -c \\\"...dual_critic walker s2...\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Walker Walk\", \"eval_data\": \"N/A - training experiment\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 13.88, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_038_dual_critic_walker_s2\", \"model_name\": \"DreamerV3 + Dual Critic (wide)\", \"pid\": \"175633\", \"seed\": 2, \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-21T12:18:34.859Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 49982.0}}, \"exp_037_wide_critic_cheetah\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A\", \"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"bash -c \\\"...wide_critic cheetah...\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Cheetah Run\", \"eval_data\": \"N/A - training experiment\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 7.46, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_037_wide_critic_cheetah.log\", \"model_name\": \"DreamerV3 + Wide Single Critic\", \"pid\": \"14487\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-21T12:18:32.619Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 26839.7}}, \"exp_036_dual_critic_pickcube\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --seed 0 --steps 200000 --compile False --device cuda:0 --logdir ./logdir/exp_036_dual_critic_pickcube\\\"\", \"data_count\": 200000, \"data_path\": \"ManiSkill PickCube-v1\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 11.03, \"gpu_id\": 0, \"hyperparams\": {\"dual_critic\": true, \"gate_enabled\": true, \"gate_fixed_dt\": 2, \"gate_subsample_max_dt\": 2, \"imag_horizon\": 8, \"tcn_sigma\": 0.0}, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_036_dual_critic_pickcube.log\", \"model_name\": \"DreamerV3 + Dual Critic\", \"pid\": \"2476\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-21T08:43:44.544357+00:00\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 39706.7}}, \"exp_035_narrow_dual_critic_walker\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --narrow_dual_critic True --logdir logdir/exp_035_narrow_dual_critic_walker\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 8.31, \"gpu_id\": 1, \"hyperparams\": {\"critic_hidden\": 256, \"critic_layers\": 2, \"critic_params_each\": 525000, \"critic_params_total\": 1050000, \"gate_enabled\": true, \"gate_fixed_dt\": 2, \"gate_subsample_max_dt\": 2, \"imag_horizon\": 8, \"narrow_dual_critic\": true}, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_035_narrow_dual_critic_walker.log\", \"model_name\": \"DreamerV3 + Narrow Dual Critic (2×256 hidden, 1.05M total)\", \"pid\": \"162900\", \"seed\": 0, \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-21T07:56:05.926445+00:00\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 29900.2}}, \"exp_034\": {\"spec\": {\"command\": \"python train.py --configs dmc_cheetah_run --dual_critic True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --steps 210000 --seed 0\", \"data_count\": 0, \"data_path\": \"dmc_cheetah_run\", \"model_name\": \"dreamerv3\", \"seed\": 0, \"server\": \"bjb1-45299\"}}, \"exp_034_dual_critic_cheetah\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --logdir logdir/exp_034_dual_critic_cheetah\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Cheetah Run (dm_control built-in)\", \"gpu\": [\"cuda:1\"], \"gpu_id\": 1, \"hyperparams\": {\"dual_critic\": true, \"gate_enabled\": true, \"gate_fixed_dt\": 2, \"gate_subsample_max_dt\": 2, \"imag_horizon\": 8, \"tcn_sigma\": 0.0}, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_034_dual_critic_cheetah.log\", \"model_name\": \"DreamerV3 + Dual Critic\", \"pid\": \"993925\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-21T05:51:51.325323+00:00\", \"submitted_via\": \"submit_training_job\"}}, \"exp_033_wide_critic_walker\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --wide_critic True --logdir logdir/exp_033_wide_critic_walker\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 8.25, \"gpu_id\": 0, \"hyperparams\": {\"critic_hidden\": 1024, \"critic_layers\": 2, \"critic_params\": 2886911, \"dual_critic\": false, \"gate_enabled\": true, \"gate_fixed_dt\": 2, \"gate_subsample_max_dt\": 2, \"imag_horizon\": 8, \"wide_critic\": true}, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_033_wide_critic_walker.log\", \"model_name\": \"DreamerV3 + Wide Critic (1024 hidden, 2.89M params, 2.44× normal)\", \"pid\": \"151860\", \"seed\": 0, \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-21T03:52:59.702597+00:00\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 29715.5}}, \"exp_031b_tcn_pickcube_s0_sigma05\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.5 --seed 0 --steps 200000 --compile False --device cuda:0 --logdir ./logdir/exp_031b_tcn_pickcube_s0_sigma05\\\"\", \"data_count\": 200000, \"data_path\": \"ManiSkill PickCube-v1\", \"gpu\": [\"cuda:0\"], \"gpu_id\": 0, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_031b_tcn_pickcube_s0_sigma05.log\", \"model_name\": \"DreamerV3 + TCN σ=0.5\", \"pid\": \"968495\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-20T22:33:14.695383+00:00\", \"submitted_via\": \"submit_training_job\"}}, \"exp_032_dual_critic_walker\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_032_dual_critic_walker\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --logdir logdir/exp_032_dual_critic_walker\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"gpu\": [\"cuda:1\"], \"gpu_id\": 1, \"hyperparams\": {\"dual_critic\": true, \"gate_enabled\": true, \"gate_fixed_dt\": 2, \"gate_subsample_max_dt\": 2, \"imag_horizon\": 8, \"tcn_sigma\": 0.0}, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_032_dual_critic_walker.log\", \"model_name\": \"DreamerV3 + Dual Critic (min of two independent critics)\", \"pid\": \"124556\", \"seed\": 0, \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-20T23:19:57.690519+00:00\", \"submitted_via\": \"submit_training_job\"}}, \"exp_032b_dual_critic_walker_s1\": {\"spec\": {\"data_count\": 210000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"hyperparams\": {\"dual_critic\": true, \"gate_enabled\": true, \"gate_fixed_dt\": 2, \"gate_subsample_max_dt\": 2, \"imag_horizon\": 8, \"tcn_sigma\": 0}, \"model_name\": \"DreamerV3 + Dual Critic (min of two independent critics)\", \"seed\": 1}}, \"exp_029d_tcn_walker_s3_sigma02\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_029d_tcn_walker_s3_sigma02\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 3 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --logdir logdir/exp_029d_tcn_walker_s3_sigma02\\\"\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_029d_tcn_walker_s3_sigma02.log\", \"pid\": \"109826\", \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-20T19:33:48.032Z\", \"submitted_via\": \"submit_training_job\"}}, \"exp_031_tcn_pickcube_s0_sigma02\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"none(train_from_scratch)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --seed 0 --steps 200000 --compile False --device cuda:0 --logdir ./logdir/exp_031_tcn_pickcube_s0_sigma02\\\"\", \"data_count\": \"200000(online)\", \"data_path\": \"maniskill_PickCube-v1\", \"eval_data\": \"maniskill_PickCube-v1(online_eval)\", \"gpu\": \"cuda:1\", \"gpu_hours\": 11.17, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_031_tcn_pickcube_s0_sigma02.log\", \"model_name\": \"dreamerv3\", \"pid\": \"908459\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-20T12:42:41.707Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 40206.6}}, \"exp_029b_tcn_walker_s2_sigma02\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_029b_tcn_walker_s2_sigma02\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 2 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --logdir logdir/exp_029b_tcn_walker_s2_sigma02\\\"\", \"gpu\": [\"cuda:1\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_029b_tcn_walker_s2_sigma02.log\", \"pid\": \"75543\", \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-20T16:56:24.781Z\", \"submitted_via\": \"submit_training_job\"}}, \"exp_030c_tcn_cheetah_s0_sigma10\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_030c_tcn_cheetah_s0_sigma10\", \"command\": \"dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 0 --tcn_sigma 1.0\", \"data_count\": 210000, \"data_path\": \"dmc_cheetah_run\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_030c_tcn_cheetah_s0_sigma10.log\", \"model_name\": \"dreamerv3\", \"pid\": \"920968\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-20T16:49:48.464Z\", \"submitted_via\": \"submit_training_job\"}}, \"exp_029c_tcn_walker_s0_sigma01\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_029c_tcn_walker_s0_sigma01/latest.pt\", \"checkpoint_source\": \"from_scratch\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.1 --logdir logdir/exp_029c_tcn_walker_s0_sigma01\\\"\", \"data_count\": 210000, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_029c_tcn_walker_s0_sigma01.log\", \"model_name\": \"dreamer\", \"pid\": \"59395\", \"seed\": 0, \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-20T11:42:56.447Z\", \"submitted_via\": \"submit_training_job\"}}, \"exp_029a_tcn_walker_s1_sigma02\": {\"spec\": {\"checkpoint_path\": \"/root/runs/event-gated-adaptive-horizon/exp_029a_tcn_walker_s1_sigma02/latest.pt\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --logdir ~/runs/event-gated-adaptive-horizon/exp_029a_tcn_walker_s1_sigma02\", \"data_count\": 210000, \"data_path\": \"dmc_walker_walk\", \"gpu\": \"cuda:1\", \"log_path\": \"/root/runs/event-gated-adaptive-horizon/exp_029a_tcn_walker_s1_sigma02.log\", \"model_name\": \"dreamerv3\", \"pid\": \"50924\", \"seed\": 1, \"server\": \"bjb1-40020\"}}, \"exp_030b_tcn_cheetah_s0_sigma05\": {\"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_030b_tcn_cheetah_s0_sigma05/latest.pt\", \"gpu\": \"cuda:0\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_030b_tcn_cheetah_s0_sigma05/metrics.jsonl\"}}, \"exp_027_tcn_walker_s1\": {\"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_027_tcn_walker_s1/\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s1.log\"}}, \"exp_027_tcn_walker_s0_sigma02\": {\"spec\": {\"checkpoint_path\": \"/root/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0_sigma02/latest.pt\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --logdir logdir/exp_027_tcn_walker_s0_sigma02\", \"data_count\": 215000, \"data_path\": \"dmc_walker_walk\", \"gpu\": \"cuda:0\", \"log_path\": \"/root/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0_sigma02.log\", \"model_name\": \"dreamerv3\", \"seed\": 0, \"server\": \"bjb1-40020\"}}, \"exp_030a_tcn_cheetah_s0_sigma02\": {\"spec\": {\"checkpoint_path\": \"logdir/exp_030a_tcn_cheetah_s0_sigma02/\", \"checkpoint_source\": \"from_scratch\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_enabled True --tcn_sigma 0.2 --logdir logdir/exp_030a_tcn_cheetah_s0_sigma02\", \"data_count\": \"210000 env steps\", \"data_path\": \"dmc_cheetah_run\", \"eval_data\": \"dmc_cheetah_run\", \"gpu\": \"cuda:0\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_030a_tcn_cheetah_s0_sigma02.log\", \"model_name\": \"dreamerv3_tcn_sigma02_cheetah\", \"seed\": 0, \"server\": \"bjb1-45299\"}}, \"exp_027_tcn_walker_s0\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.5 --logdir logdir/exp_027_tcn_walker_s0\\\"\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 3.18, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0.log\", \"pid\": \"888715\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-20T06:13:35.505Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 11433.5}}, \"exp_028_rave_walker_s0_ceil15\": {\"spec\": {\"checkpoint_path\": \"~/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0_ceil15/\", \"checkpoint_source\": \"N/A (trained from scratch, hyperparameter variant of exp_028_rave_walker_s0)\", \"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --rave_enabled True --rave_ceiling 1.5 --rave_ema_decay 0.99 --logdir ~/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0_ceil15'\", \"data_count\": \"210000 env steps\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:1\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0_ceil15.log\", \"model_name\": \"dreamerv3_rave_ceil15\", \"note\": \"CUDA_VISIBLE_DEVICES=1 set by submit_training_job, device=cuda:0 within process\", \"pid\": \"38372\", \"seed\": 0, \"server\": \"bjb1-40020\", \"tmux_session\": \"exp_028_rave_walker_s0_ceil15\"}}, \"exp_028_rave_walker_s0\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"N/A (trained from scratch, derives from SGS failure line)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 105000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --rave_ceiling 2.0 --logdir logdir/exp_028_rave_walker_s0\\\"\", \"data_count\": \"105000 env steps (52.5K agent steps, action_repeat=2)\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 3.33, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0.log\", \"model_name\": \"dreamerv3_rave_ceil20\", \"pid\": \"879636\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-20T02:54:26.022Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 12005.7}}, \"exp_025_obs_sgs_walker_s2\": {\"spec\": {\"checkpoint_path\": \"logdir/exp_025_obs_sgs_walker_s2/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 2 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_025_obs_sgs_walker_s2\", \"data_count\": \"210000 env steps (105K agent steps)\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:1\"], \"log_path\": \"logdir/exp_025_obs_sgs_walker_s2/train.log\", \"model_name\": \"dreamerv3_obs_decoder_sgs\", \"pid\": \"7989\", \"seed\": 2, \"server\": \"bjb1-40020\", \"tmux_session\": \"exp_025_s2\"}}, \"exp_026_obs_sgs_cheetah_s1\": {\"spec\": {\"checkpoint_path\": \"logdir/exp_026_obs_sgs_cheetah_s1/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 105000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_026_obs_sgs_cheetah_s1\", \"data_count\": \"105000 env steps\", \"data_path\": \"dmc_cheetah_run\", \"eval_data\": \"dmc_cheetah_run (online eval during training)\", \"gpu\": [\"cuda:1\"], \"log_path\": \"logdir/exp_026_obs_sgs_cheetah_s1/train.log\", \"model_name\": \"dreamerv3_obs_decoder_sgs_cheetah\", \"pid\": \"16346\", \"seed\": 1, \"server\": \"bjb1-40020\", \"tmux_session\": \"exp_026_s1\"}}, \"exp_026_obs_sgs_cheetah_s0\": {\"spec\": {\"checkpoint_path\": \"logdir/exp_026_obs_sgs_cheetah_s0/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 105000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_026_obs_sgs_cheetah_s0\", \"data_count\": \"105000 env steps\", \"data_path\": \"dmc_cheetah_run\", \"eval_data\": \"dmc_cheetah_run (online eval during training)\", \"gpu\": [\"cuda:0\"], \"log_path\": \"logdir/exp_026_obs_sgs_cheetah_s0/train.log\", \"model_name\": \"dreamerv3_obs_decoder_sgs_cheetah\", \"pid\": \"16208\", \"seed\": 0, \"server\": \"bjb1-40020\", \"tmux_session\": \"exp_026_s0\"}}, \"exp_025_obs_sgs_walker_s4\": {\"spec\": {\"checkpoint_path\": \"logdir/exp_025_obs_sgs_walker_s4/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 4 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_025_obs_sgs_walker_s4\", \"data_count\": \"210000 env steps (105K agent steps)\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:1\"], \"log_path\": \"logdir/exp_025_obs_sgs_walker_s4/train.log\", \"model_name\": \"dreamerv3_obs_decoder_sgs\", \"pid\": \"851593\", \"seed\": 4, \"server\": \"bjb1-45299\", \"tmux_session\": \"exp_025_s4\"}}, \"exp_025_obs_sgs_walker_s3\": {\"spec\": {\"checkpoint_path\": \"logdir/exp_025_obs_sgs_walker_s3/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 3 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_025_obs_sgs_walker_s3\", \"data_count\": \"210000 env steps (105K agent steps)\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:0\"], \"log_path\": \"logdir/exp_025_obs_sgs_walker_s3/train.log\", \"model_name\": \"dreamerv3_obs_decoder_sgs\", \"pid\": \"847597\", \"seed\": 3, \"server\": \"bjb1-45299\", \"tmux_session\": \"exp_025_s3\"}}, \"exp_025_obs_sgs_walker_s1\": {\"spec\": {\"checkpoint_path\": \"logdir/exp_025_obs_sgs_walker_s1/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_025_obs_sgs_walker_s1\", \"data_count\": \"210000 env steps (105K agent steps)\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:0\"], \"log_path\": \"logdir/exp_025_obs_sgs_walker_s1/train.log\", \"model_name\": \"dreamerv3_obs_decoder_sgs\", \"pid\": \"7833\", \"seed\": 1, \"server\": \"bjb1-40020\", \"tmux_session\": \"exp_025_s1\"}}, \"exp_001_baseline_s4_extended\": {\"spec\": {\"checkpoint_path\": \"logdir/exp_001_baseline_s4/\", \"checkpoint_source\": \"logdir/exp_001_baseline_s4/latest.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 505000 --seed 4 --device cuda:0 --compile False --gate_enabled False --logdir logdir/exp_001_baseline_s4\", \"data_count\": \"505000 env steps\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": \"cuda:1\", \"log_path\": \"logdir/exp_001_baseline_s4/train_extended.log\", \"model_name\": \"dreamerv3_baseline\", \"resumed_from_step\": 112000, \"seed\": 4, \"server\": \"bjb1-45299\", \"target_steps\": 505000, \"tmux_session\": \"exp_s4_ext\"}}}, \"count\": 50, \"total\": 132, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9546}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2fe83aea-5863-4eb4-8029-aa58f80fcf56",
  "uuid": "f501fdeb-79a8-4cc8-9e30-f4bd68d50395",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"exp_057_frozen_dt_emb_walker_s2\\\": {\\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_057_frozen_dt_emb_walker_s2\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"gpu_ids\\\": [1], \\\"pid\\\": 157775, \\\"data_path\\\": \\\"dmc_walker_walk\\\", \\\"data_count\\\": 210000, \\\"model_name\\\": \\\"DreamerV3 (frozen dt_emb, Walker s2)\\\", \\\"seed\\\": 2, \\\"checkpoint_source\\\": \\\"N/A (training from scratch)\\\", \\\"eval_data\\\": \\\"dmc_walker_walk (online eval)\\\", \\\"log_path\\\": \\\"logdir/exp_057_frozen_dt_emb_walker_s2/train.log\\\", \\\"checkpoint_path\\\": \\\"logdir/exp_057_frozen_dt_emb_walker_s2/checkpoint_225000.pt\\\"}}, \\\"exp_058_frozen_dt_emb_cheetah_s1\\\": {\\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_058_frozen_dt_emb_cheetah_s1\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"gpu_ids\\\": [0], \\\"pid\\\": 164830, \\\"data_path\\\": \\\"dmc_cheetah_run\\\", \\\"data_count\\\": 210000, \\\"model_name\\\": \\\"DreamerV3 (frozen dt_emb, Cheetah s1)\\\", \\\"seed\\\": 1, \\\"checkpoint_source\\\": \\\"N/A (training from scratch)\\\", \\\"eval_data\\\": \\\"dmc_cheetah_run (online eval)\\\", \\\"log_path\\\": \\\"logdir/exp_058_frozen_dt_emb_cheetah_s1/train.log\\\", \\\"checkpoint_path\\\": \\\"logdir/exp_058_frozen_dt_emb_cheetah_s1/checkpoint_225000.pt\\\"}}, \\\"exp_056_peginsertion_frozen_s1\\\": {\\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 MUJOCO_EGL_DEVICE_ID=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs maniskill_peginsertion --task maniskill_PegInsertionSide-v1 --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_056_peginsertion_frozen_s1\\\", \\\"server\\\": \\\"bjb1-40020\\\", \\\"gpu_ids\\\": [1], \\\"pid\\\": 346430, \\\"data_path\\\": \\\"ManiSkill PegInsertionSide-v1 (online RL, state obs)\\\", \\\"data_count\\\": 210000, \\\"model_name\\\": \\\"DreamerV3 (frozen dt_emb, fixed dt=2, ManiSkill PegInsertion s1)\\\", \\\"seed\\\": 1, \\\"checkpoint_source\\\": \\\"N/A (training from scratch)\\\", \\\"eval_data\\\": \\\"PegInsertionSide-v1 (online eval)\\\", \\\"log_path\\\": \\\"logdir/exp_056_peginsertion_frozen_s1/train.log\\\", \\\"checkpoint_path\\\": \\\"logdir/exp_056_peginsertion_frozen_s1/checkpoint_202500.pt\\\"}}, \\\"exp_055_peginsertion_civo_trigger_s1\\\": {\\\"spec\\\": {\\\"command\\\": \\\"python -u dreamer.py --configs maniskill_peginsertion --task maniskill_PegInsertionSide-v1 --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_055_peginsertion_civo_trigger_s1\\\", \\\"server\\\": \\\"bjb1-40020\\\", \\\"gpu_ids\\\": [0], \\\"pid\\\": 345223, \\\"data_path\\\": \\\"ManiSkill PegInsertionSide-v1 (online RL, state obs)\\\", \\\"data_count\\\": 210000, \\\"model_name\\\": \\\"DreamerV3 (trained dt_emb, CIVO config, PegInsertion)\\\", \\\"seed\\\": 1, \\\"checkpoint_source\\\": \\\"N/A (training from scratch)\\\", \\\"eval_data\\\": \\\"PegInsertionSide-v1 (online eval)\\\", \\\"log_path\\\": \\\"logdir/exp_055_peginsertion_civo_trigger_s1/train.log\\\"}}, \\\"exp_054_pickcube_frozen_s0\\\": {\\\"spec\\\": {\\\"command\\\": \\\"python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --seed 0 --steps 210000 --compile False --device cuda:0 --checkpoint_every 25000 --logdir logdir/exp_054_pickcube_frozen_s0\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"gpu_ids\\\": [0], \\\"pid\\\": 133956, \\\"data_path\\\": \\\"ManiSkill PickCube-v1 (online RL, state obs)\\\", \\\"data_count\\\": 210000, \\\"model_name\\\": \\\"DreamerV3 (frozen dt_emb, CIVO config, ManiSkill PickCube)\\\", \\\"seed\\\": 0, \\\"checkpoint_source\\\": \\\"N/A (training from scratch)\\\", \\\"eval_data\\\": \\\"PickCube-v1 (online eval)\\\", \\\"log_path\\\": \\\"logdir/exp_054_pickcube_frozen_s0/metrics.jsonl\\\", \\\"checkpoint_path\\\": \\\"logdir/exp_054_pickcube_frozen_s0/checkpoint.ckpt\\\"}}, \\\"exp_053_peginsertion_frozen_s0\\\": {\\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 MUJOCO_EGL_DEVICE_ID=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs maniskill_peginsertion --task maniskill_PegInsertionSide-v1 --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_053_peginsertion_frozen_s0\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"gpu_ids\\\": [1], \\\"pid\\\": 123495, \\\"data_path\\\": \\\"ManiSkill PegInsertionSide-v1 (online RL, state obs)\\\", \\\"data_count\\\": 210000, \\\"model_name\\\": \\\"DreamerV3 (frozen dt_emb, fixed dt=2, ManiSkill PegInsertion)\\\", \\\"seed\\\": 0, \\\"checkpoint_source\\\": \\\"N/A (training from scratch)\\\", \\\"eval_data\\\": \\\"PegInsertionSide-v1 (online eval)\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_053_peginsertion_frozen_s0.log\\\", \\\"checkpoint_path\\\": \\\"logdir/exp_053_peginsertion_frozen_s0/checkpoint.ckpt\\\"}}, \\\"exp_050_peginsertion_civo_trigger_s0\\\": {\\\"spec\\\": {\\\"command\\\": \\\"LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs maniskill_peginsertion --task maniskill_PegInsertionSide-v1 --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_050_peginsertion_civo_trigger_s0\\\", \\\"server\\\": \\\"bjb1-40020\\\", \\\"data_path\\\": \\\"ManiSkill PegInsertionSide-v1 (state obs)\\\", \\\"data_count\\\": 210000, \\\"model_name\\\": \\\"DreamerV3 + CIVO trigger (gate_fixed_dt=2)\\\", \\\"seed\\\": 0, \\\"pid\\\": 304736, \\\"gpu_ids\\\": [0], \\\"log_path\\\": \\\"logdir/exp_050_peginsertion_civo_trigger_s0/train.log\\\", \\\"checkpoint_path\\\": \\\"logdir/exp_050_peginsertion_civo_trigger_s0\\\"}}, \\\"exp_051_stackcube_frozen_dt_emb_s0\\\": {\\\"spec\\\": {\\\"command\\\": \\\"python -u dreamer.py --configs maniskill_stackcube --task maniskill_StackCube-v1 --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_051_stackcube_frozen_dt_emb_s0\\\", \\\"server\\\": \\\"bjb1-40020\\\", \\\"gpu_ids\\\": [1], \\\"pid\\\": 305974, \\\"data_path\\\": \\\"ManiSkill StackCube-v1 (online RL, state obs)\\\", \\\"data_count\\\": 210000, \\\"model_name\\\": \\\"DreamerV3 (frozen dt_emb, ManiSkill StackCube)\\\", \\\"seed\\\": 0, \\\"checkpoint_source\\\": \\\"N/A (training from scratch)\\\", \\\"eval_data\\\": \\\"StackCube-v1 (online eval)\\\", \\\"log_path\\\": \\\"logdir/exp_051_stackcube_frozen_dt_emb_s0.log\\\", \\\"checkpoint_path\\\": \\\"logdir/exp_051_stackcube_frozen_dt_emb_s0/checkpoint_202500.pt\\\"}}, \\\"exp_052_stackcube_civo_trigger_s1\\\": {\\\"spec\\\": {\\\"command\\\": \\\"python -u dreamer.py --configs maniskill_stackcube --task maniskill_StackCube-v1 --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_052_stackcube_civo_trigger_s1\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"gpu_ids\\\": [0], \\\"pid\\\": 103781, \\\"data_path\\\": \\\"ManiSkill StackCube-v1 (online RL, state obs)\\\", \\\"data_count\\\": 210000, \\\"model_name\\\": \\\"DreamerV3 (trained dt_emb, CIVO config, ManiSkill StackCube)\\\", \\\"seed\\\": 1, \\\"checkpoint_source\\\": \\\"N/A (training from scratch)\\\", \\\"eval_data\\\": \\\"StackCube-v1 (online eval)\\\", \\\"log_path\\\": \\\"logdir/exp_052_stackcube_civo_trigger_s1/train.log\\\"}}, \\\"exp_049_stackcube_civo_trigger_s0\\\": {\\\"spec\\\": {\\\"command\\\": \\\"python -u dreamer.py --configs maniskill_stackcube --task maniskill_StackCube-v1 --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_049_stackcube_civo_trigger_s0\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"gpu_ids\\\": [1], \\\"pid\\\": 91395, \\\"data_path\\\": \\\"ManiSkill StackCube-v1 (online RL, state obs)\\\", \\\"data_count\\\": 210000, \\\"model_name\\\": \\\"DreamerV3 (trained dt_emb, CIVO config, ManiSkill StackCube)\\\", \\\"seed\\\": 0, \\\"checkpoint_source\\\": \\\"N/A (training from scratch)\\\", \\\"eval_data\\\": \\\"StackCube-v1 (online eval)\\\", \\\"log_path\\\": \\\"logdir/exp_049_stackcube_civo_trigger_s0/train.log\\\"}}, \\\"exp_048_cheetah_civo_extension\\\": {\\\"spec\\\": {\\\"command\\\": \\\"python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 300000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_048_cheetah_civo_extension\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"gpu_ids\\\": [0], \\\"pid\\\": 88654, \\\"data_path\\\": \\\"dmc_cheetah_run (online RL)\\\", \\\"data_count\\\": 300000, \\\"model_name\\\": \\\"DreamerV3 (trained dt_emb, CIVO config, Cheetah)\\\", \\\"seed\\\": 0, \\\"checkpoint_source\\\": \\\"exp_010b_cheetah_civo_trigger_s0/latest.pt (step 105K, NVE=70.64)\\\", \\\"eval_data\\\": \\\"dmc_cheetah_run (online eval)\\\", \\\"log_path\\\": \\\"logdir/exp_048_cheetah_civo_extension/train.log\\\"}}, \\\"exp_047_frozen_dt_emb_walker_s1\\\": {\\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_047_frozen_dt_emb_walker_s1\\\", \\\"server\\\": \\\"bjb1-40020\\\", \\\"data_path\\\": \\\"dmc_walker_walk\\\", \\\"data_count\\\": 210000, \\\"model_name\\\": \\\"dreamer_gated_frozen_dt_emb\\\", \\\"seed\\\": 1, \\\"eval_data\\\": \\\"dmc_walker_walk (online eval)\\\", \\\"checkpoint_source\\\": \\\"N/A (training from scratch)\\\"}}, \\\"exp_046_frozen_dt_emb_cheetah\\\": {\\\"spec\\\": {\\\"command\\\": \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_046_frozen_dt_emb_cheetah\\\", \\\"server\\\": \\\"bjb1-40020\\\", \\\"seed\\\": 0, \\\"model_name\\\": \\\"dreamerv3-cheetah-frozen-dt-emb\\\", \\\"data_path\\\": \\\"dmc_cheetah_run\\\", \\\"data_count\\\": 210000, \\\"eval_data\\\": \\\"dmc_cheetah_run (online eval)\\\", \\\"checkpoint_source\\\": \\\"N/A (training from scratch)\\\"}}, \\\"exp_044_gradient_stop_walker\\\": {\\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True --logdir logdir/exp_044_gradient_stop_walker\\\\\\\"\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"68371\\\", \\\"log_path\\\": \\\"~/runs/event-gated-adaptive-horizon/exp_044_gradient_stop_walker.log\\\", \\\"submitted_at\\\": \\\"2026-05-22T09:08:10.295Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"DMC Walker Walk\\\", \\\"data_count\\\": 210000, \\\"model_name\\\": \\\"DreamerV3 + reward_dt_emb_detach\\\", \\\"seed\\\": 0, \\\"checkpoint_source\\\": \\\"N/A - training from scratch\\\", \\\"eval_data\\\": \\\"dmc_walker_walk\\\", \\\"wall_clock_seconds\\\": 25212.4, \\\"gpu_hours\\\": 7.0}}, \\\"exp_045_treatment_extension_008d_s3\\\": {\\\"spec\\\": {\\\"command\\\": \\\"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 300000 --seed 3 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_045_treatment_extension_008d_s3\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"gpu_ids\\\": [0], \\\"pid\\\": \\\"70945\\\", \\\"data_path\\\": \\\"dmc_walker_walk (online RL)\\\", \\\"data_count\\\": 300000, \\\"model_name\\\": \\\"DreamerV3 (trained dt_emb, CIVO config)\\\", \\\"seed\\\": 3, \\\"checkpoint_source\\\": \\\"exp_008d_civo_trigger_s3/latest.pt (step 112K)\\\", \\\"eval_data\\\": \\\"dmc_walker_walk (online eval, same as training env)\\\", \\\"log_path\\\": \\\"logdir/exp_045_treatment_extension_008d_s3/train.log\\\"}}, \\\"exp_043_008f_walker_s1\\\": {\\\"spec\\\": {\\\"account\\\": \\\"root\\\", \\\"backend\\\": \\\"tmux\\\", \\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --logdir logdir/exp_043_008f_walker_s1\\\\\\\"\\\", \\\"data_count\\\": 210000, \\\"data_path\\\": \\\"DMC Walker Walk\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"log_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_043_008f_walker_s1\\\", \\\"model_name\\\": \\\"DreamerV3 (no dt_emb, 008f control)\\\", \\\"pid\\\": \\\"250627\\\", \\\"seed\\\": 1, \\\"server\\\": \\\"bjb1-40020\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\"}}, \\\"exp_042_frozen_dt_emb_walker\\\": {\\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --logdir logdir/exp_042_frozen_dt_emb_walker\\\\\\\"\\\", \\\"data_count\\\": 210000, \\\"data_path\\\": \\\"DMC Walker Walk\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"log_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_042_frozen_dt_emb_walker\\\", \\\"model_name\\\": \\\"DreamerV3 + frozen dt_emb\\\", \\\"pid\\\": \\\"251336\\\", \\\"seed\\\": 0, \\\"server\\\": \\\"bjb1-40020\\\"}}, \\\"exp_040_wide_dual_critic_cheetah\\\": {\\\"spec\\\": {\\\"account\\\": \\\"root\\\", \\\"backend\\\": \\\"tmux\\\", \\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --logdir logdir/exp_040_wide_dual_critic_cheetah\\\\\\\"\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"log_path\\\": \\\"~/runs/event-gated-adaptive-horizon/exp_040_wide_dual_critic_cheetah.log\\\", \\\"pid\\\": \\\"52397\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"submitted_at\\\": \\\"2026-05-21T19:51:11.519Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"seed\\\": 1, \\\"wall_clock_seconds\\\": 49438.9, \\\"gpu_hours\\\": 13.73}}, \\\"exp_041_dual_critic_walker_s3\\\": {\\\"spec\\\": {\\\"account\\\": \\\"root\\\", \\\"backend\\\": \\\"tmux\\\", \\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 3 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --logdir logdir/exp_041_dual_critic_walker_s3\\\\\\\"\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"log_path\\\": \\\"~/runs/event-gated-adaptive-horizon/exp_041_dual_critic_walker_s3.log\\\", \\\"pid\\\": \\\"51103\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"submitted_at\\\": \\\"2026-05-22T02:38:20.728Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_041_dual_critic_walker_s3/checkpoint.pt\\\", \\\"checkpoint_source\\\": \\\"N/A - training from scratch\\\", \\\"eval_data\\\": \\\"dmc_walker_walk\\\", \\\"wall_clock_seconds\\\": 23112.0, \\\"gpu_hours\\\": 6.42}}, \\\"exp_039_narrow_dual_critic_walker_s1\\\": {\\\"spec\\\": {\\\"account\\\": \\\"root\\\", \\\"backend\\\": \\\"tmux\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_039_narrow_dual_critic_walker_s1/latest.pt\\\", \\\"checkpoint_source\\\": \\\"N/A - training from scratch\\\", \\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --narrow_dual_critic True --logdir logdir/exp_039_narrow_dual_critic_walker_s1\\\\\\\"\\\", \\\"eval_data\\\": \\\"N/A - training experiment\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"gpu_hours\\\": 10.06, \\\"log_path\\\": \\\"~/runs/event-gated-adaptive-horizon/exp_039_narrow_dual_critic_walker_s1.log\\\", \\\"pid\\\": \\\"198771\\\", \\\"server\\\": \\\"bjb1-40020\\\", \\\"submitted_at\\\": \\\"2026-05-21T16:31:39.634Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"wall_clock_seconds\\\": 36234.0}}, \\\"exp_038_dual_critic_walker_s2\\\": {\\\"spec\\\": {\\\"account\\\": \\\"root\\\", \\\"backend\\\": \\\"tmux\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_038_dual_critic_walker_s2/latest.pt\\\", \\\"checkpoint_source\\\": \\\"N/A - training from scratch\\\", \\\"command\\\": \\\"bash -c \\\\\\\"...dual_critic walker s2...\\\\\\\"\\\", \\\"data_count\\\": 210000, \\\"data_path\\\": \\\"DMC Walker Walk\\\", \\\"eval_data\\\": \\\"N/A - training experiment\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"gpu_hours\\\": 13.88, \\\"log_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_038_dual_critic_walker_s2\\\", \\\"model_name\\\": \\\"DreamerV3 + Dual Critic (wide)\\\", \\\"pid\\\": \\\"175633\\\", \\\"seed\\\": 2, \\\"server\\\": \\\"bjb1-40020\\\", \\\"submitted_at\\\": \\\"2026-05-21T12:18:34.859Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"wall_clock_seconds\\\": 49982.0}}, \\\"exp_037_wide_critic_cheetah\\\": {\\\"spec\\\": {\\\"account\\\": \\\"root\\\", \\\"backend\\\": \\\"tmux\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"checkpoint_source\\\": \\\"N/A - training from scratch\\\", \\\"command\\\": \\\"bash -c \\\\\\\"...wide_critic cheetah...\\\\\\\"\\\", \\\"data_count\\\": 210000, \\\"data_path\\\": \\\"DMC Cheetah Run\\\", \\\"eval_data\\\": \\\"N/A - training experiment\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"gpu_hours\\\": 7.46, \\\"log_path\\\": \\\"~/runs/event-gated-adaptive-horizon/exp_037_wide_critic_cheetah.log\\\", \\\"model_name\\\": \\\"DreamerV3 + Wide Single Critic\\\", \\\"pid\\\": \\\"14487\\\", \\\"seed\\\": 0, \\\"server\\\": \\\"bjb1-45299\\\", \\\"submitted_at\\\": \\\"2026-05-21T12:18:32.619Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"wall_clock_seconds\\\": 26839.7}}, \\\"exp_036_dual_critic_pickcube\\\": {\\\"spec\\\": {\\\"account\\\": \\\"root\\\", \\\"backend\\\": \\\"tmux\\\", \\\"checkpoint_path\\\": \\\"N/A\\\", \\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --seed 0 --steps 200000 --compile False --device cuda:0 --logdir ./logdir/exp_036_dual_critic_pickcube\\\\\\\"\\\", \\\"data_count\\\": 200000, \\\"data_path\\\": \\\"ManiSkill PickCube-v1\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"gpu_hours\\\": 11.03, \\\"gpu_id\\\": 0, \\\"hyperparams\\\": {\\\"dual_critic\\\": true, \\\"gate_enabled\\\": true, \\\"gate_fixed_dt\\\": 2, \\\"gate_subsample_max_dt\\\": 2, \\\"imag_horizon\\\": 8, \\\"tcn_sigma\\\": 0.0}, \\\"log_path\\\": \\\"~/runs/event-gated-adaptive-horizon/exp_036_dual_critic_pickcube.log\\\", \\\"model_name\\\": \\\"DreamerV3 + Dual Critic\\\", \\\"pid\\\": \\\"2476\\\", \\\"seed\\\": 0, \\\"server\\\": \\\"bjb1-45299\\\", \\\"submitted_at\\\": \\\"2026-05-21T08:43:44.544357+00:00\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"wall_clock_seconds\\\": 39706.7}}, \\\"exp_035_narrow_dual_critic_walker\\\": {\\\"spec\\\": {\\\"account\\\": \\\"root\\\", \\\"backend\\\": \\\"tmux\\\", \\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --narrow_dual_critic True --logdir logdir/exp_035_narrow_dual_critic_walker\\\\\\\"\\\", \\\"data_count\\\": 210000, \\\"data_path\\\": \\\"DMC Walker Walk (dm_control built-in)\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"gpu_hours\\\": 8.31, \\\"gpu_id\\\": 1, \\\"hyperparams\\\": {\\\"critic_hidden\\\": 256, \\\"critic_layers\\\": 2, \\\"critic_params_each\\\": 525000, \\\"critic_params_total\\\": 1050000, \\\"gate_enabled\\\": true, \\\"gate_fixed_dt\\\": 2, \\\"gate_subsample_max_dt\\\": 2, \\\"imag_horizon\\\": 8, \\\"narrow_dual_critic\\\": true}, \\\"log_path\\\": \\\"~/runs/event-gated-adaptive-horizon/exp_035_narrow_dual_critic_walker.log\\\", \\\"model_name\\\": \\\"DreamerV3 + Narrow Dual Critic (2×256 hidden, 1.05M total)\\\", \\\"pid\\\": \\\"162900\\\", \\\"seed\\\": 0, \\\"server\\\": \\\"bjb1-40020\\\", \\\"submitted_at\\\": \\\"2026-05-21T07:56:05.926445+00:00\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"wall_clock_seconds\\\": 29900.2}}, \\\"exp_034\\\": {\\\"spec\\\": {\\\"command\\\": \\\"python train.py --configs dmc_cheetah_run --dual_critic True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --steps 210000 --seed 0\\\", \\\"data_count\\\": 0, \\\"data_path\\\": \\\"dmc_cheetah_run\\\", \\\"model_name\\\": \\\"dreamerv3\\\", \\\"seed\\\": 0, \\\"server\\\": \\\"bjb1-45299\\\"}}, \\\"exp_034_dual_critic_cheetah\\\": {\\\"spec\\\": {\\\"account\\\": \\\"root\\\", \\\"backend\\\": \\\"tmux\\\", \\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --logdir logdir/exp_034_dual_critic_cheetah\\\\\\\"\\\", \\\"data_count\\\": 210000, \\\"data_path\\\": \\\"DMC Cheetah Run (dm_control built-in)\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"gpu_id\\\": 1, \\\"hyperparams\\\": {\\\"dual_critic\\\": true, \\\"gate_enabled\\\": true, \\\"gate_fixed_dt\\\": 2, \\\"gate_subsample_max_dt\\\": 2, \\\"imag_horizon\\\": 8, \\\"tcn_sigma\\\": 0.0}, \\\"log_path\\\": \\\"~/runs/event-gated-adaptive-horizon/exp_034_dual_critic_cheetah.log\\\", \\\"model_name\\\": \\\"DreamerV3 + Dual Critic\\\", \\\"pid\\\": \\\"993925\\\", \\\"seed\\\": 0, \\\"server\\\": \\\"bjb1-45299\\\", \\\"submitted_at\\\": \\\"2026-05-21T05:51:51.325323+00:00\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\"}}, \\\"exp_033_wide_critic_walker\\\": {\\\"spec\\\": {\\\"account\\\": \\\"root\\\", \\\"backend\\\": \\\"tmux\\\", \\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --wide_critic True --logdir logdir/exp_033_wide_critic_walker\\\\\\\"\\\", \\\"data_count\\\": 210000, \\\"data_path\\\": \\\"DMC Walker Walk (dm_control built-in)\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"gpu_hours\\\": 8.25, \\\"gpu_id\\\": 0, \\\"hyperparams\\\": {\\\"critic_hidden\\\": 1024, \\\"critic_layers\\\": 2, \\\"critic_params\\\": 2886911, \\\"dual_critic\\\": false, \\\"gate_enabled\\\": true, \\\"gate_fixed_dt\\\": 2, \\\"gate_subsample_max_dt\\\": 2, \\\"imag_horizon\\\": 8, \\\"wide_critic\\\": true}, \\\"log_path\\\": \\\"~/runs/event-gated-adaptive-horizon/exp_033_wide_critic_walker.log\\\", \\\"model_name\\\": \\\"DreamerV3 + Wide Critic (1024 hidden, 2.89M params, 2.44× normal)\\\", \\\"pid\\\": \\\"151860\\\", \\\"seed\\\": 0, \\\"server\\\": \\\"bjb1-40020\\\", \\\"submitted_at\\\": \\\"2026-05-21T03:52:59.702597+00:00\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"wall_clock_seconds\\\": 29715.5}}, \\\"exp_031b_tcn_pickcube_s0_sigma05\\\": {\\\"spec\\\": {\\\"account\\\": \\\"root\\\", \\\"backend\\\": \\\"tmux\\\", \\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.5 --seed 0 --steps 200000 --compile False --device cuda:0 --logdir ./logdir/exp_031b_tcn_pickcube_s0_sigma05\\\\\\\"\\\", \\\"data_count\\\": 200000, \\\"data_path\\\": \\\"ManiSkill PickCube-v1\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"gpu_id\\\": 0, \\\"log_path\\\": \\\"~/runs/event-gated-adaptive-horizon/exp_031b_tcn_pickcube_s0_sigma05.log\\\", \\\"model_name\\\": \\\"DreamerV3 + TCN σ=0.5\\\", \\\"pid\\\": \\\"968495\\\", \\\"seed\\\": 0, \\\"server\\\": \\\"bjb1-45299\\\", \\\"submitted_at\\\": \\\"2026-05-20T22:33:14.695383+00:00\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\"}}, \\\"exp_032_dual_critic_walker\\\": {\\\"spec\\\": {\\\"account\\\": \\\"root\\\", \\\"backend\\\": \\\"tmux\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_032_dual_critic_walker\\\", \\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --logdir logdir/exp_032_dual_critic_walker\\\\\\\"\\\", \\\"data_count\\\": 210000, \\\"data_path\\\": \\\"DMC Walker Walk (dm_control built-in)\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"gpu_id\\\": 1, \\\"hyperparams\\\": {\\\"dual_critic\\\": true, \\\"gate_enabled\\\": true, \\\"gate_fixed_dt\\\": 2, \\\"gate_subsample_max_dt\\\": 2, \\\"imag_horizon\\\": 8, \\\"tcn_sigma\\\": 0.0}, \\\"log_path\\\": \\\"~/runs/event-gated-adaptive-horizon/exp_032_dual_critic_walker.log\\\", \\\"model_name\\\": \\\"DreamerV3 + Dual Critic (min of two independent critics)\\\", \\\"pid\\\": \\\"124556\\\", \\\"seed\\\": 0, \\\"server\\\": \\\"bjb1-40020\\\", \\\"submitted_at\\\": \\\"2026-05-20T23:19:57.690519+00:00\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\"}}, \\\"exp_032b_dual_critic_walker_s1\\\": {\\\"spec\\\": {\\\"data_count\\\": 210000, \\\"data_path\\\": \\\"DMC Walker Walk (dm_control built-in)\\\", \\\"hyperparams\\\": {\\\"dual_critic\\\": true, \\\"gate_enabled\\\": true, \\\"gate_fixed_dt\\\": 2, \\\"gate_subsample_max_dt\\\": 2, \\\"imag_horizon\\\": 8, \\\"tcn_sigma\\\": 0}, \\\"model_name\\\": \\\"DreamerV3 + Dual Critic (min of two independent critics)\\\", \\\"seed\\\": 1}}, \\\"exp_029d_tcn_walker_s3_sigma02\\\": {\\\"spec\\\": {\\\"account\\\": \\\"root\\\", \\\"backend\\\": \\\"tmux\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_029d_tcn_walker_s3_sigma02\\\", \\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 3 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --logdir logdir/exp_029d_tcn_walker_s3_sigma02\\\\\\\"\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"log_path\\\": \\\"~/runs/event-gated-adaptive-horizon/exp_029d_tcn_walker_s3_sigma02.log\\\", \\\"pid\\\": \\\"109826\\\", \\\"server\\\": \\\"bjb1-40020\\\", \\\"submitted_at\\\": \\\"2026-05-20T19:33:48.032Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\"}}, \\\"exp_031_tcn_pickcube_s0_sigma02\\\": {\\\"spec\\\": {\\\"account\\\": \\\"root\\\", \\\"backend\\\": \\\"tmux\\\", \\\"checkpoint_source\\\": \\\"none(train_from_scratch)\\\", \\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --seed 0 --steps 200000 --compile False --device cuda:0 --logdir ./logdir/exp_031_tcn_pickcube_s0_sigma02\\\\\\\"\\\", \\\"data_count\\\": \\\"200000(online)\\\", \\\"data_path\\\": \\\"maniskill_PickCube-v1\\\", \\\"eval_data\\\": \\\"maniskill_PickCube-v1(online_eval)\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"gpu_hours\\\": 11.17, \\\"log_path\\\": \\\"~/runs/event-gated-adaptive-horizon/exp_031_tcn_pickcube_s0_sigma02.log\\\", \\\"model_name\\\": \\\"dreamerv3\\\", \\\"pid\\\": \\\"908459\\\", \\\"seed\\\": 0, \\\"server\\\": \\\"bjb1-45299\\\", \\\"submitted_at\\\": \\\"2026-05-20T12:42:41.707Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"wall_clock_seconds\\\": 40206.6}}, \\\"exp_029b_tcn_walker_s2_sigma02\\\": {\\\"spec\\\": {\\\"account\\\": \\\"root\\\", \\\"backend\\\": \\\"tmux\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_029b_tcn_walker_s2_sigma02\\\", \\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 2 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --logdir logdir/exp_029b_tcn_walker_s2_sigma02\\\\\\\"\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"log_path\\\": \\\"~/runs/event-gated-adaptive-horizon/exp_029b_tcn_walker_s2_sigma02.log\\\", \\\"pid\\\": \\\"75543\\\", \\\"server\\\": \\\"bjb1-40020\\\", \\\"submitted_at\\\": \\\"2026-05-20T16:56:24.781Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\"}}, \\\"exp_030c_tcn_cheetah_s0_sigma10\\\": {\\\"spec\\\": {\\\"account\\\": \\\"root\\\", \\\"backend\\\": \\\"tmux\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_030c_tcn_cheetah_s0_sigma10\\\", \\\"command\\\": \\\"dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 0 --tcn_sigma 1.0\\\", \\\"data_count\\\": 210000, \\\"data_path\\\": \\\"dmc_cheetah_run\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"log_path\\\": \\\"~/runs/event-gated-adaptive-horizon/exp_030c_tcn_cheetah_s0_sigma10.log\\\", \\\"model_name\\\": \\\"dreamerv3\\\", \\\"pid\\\": \\\"920968\\\", \\\"seed\\\": 0, \\\"server\\\": \\\"bjb1-45299\\\", \\\"submitted_at\\\": \\\"2026-05-20T16:49:48.464Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\"}}, \\\"exp_029c_tcn_walker_s0_sigma01\\\": {\\\"spec\\\": {\\\"account\\\": \\\"root\\\", \\\"backend\\\": \\\"tmux\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_029c_tcn_walker_s0_sigma01/latest.pt\\\", \\\"checkpoint_source\\\": \\\"from_scratch\\\", \\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.1 --logdir logdir/exp_029c_tcn_walker_s0_sigma01\\\\\\\"\\\", \\\"data_count\\\": 210000, \\\"data_path\\\": \\\"dmc_walker_walk\\\", \\\"eval_data\\\": \\\"dmc_walker_walk\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"log_path\\\": \\\"~/runs/event-gated-adaptive-horizon/exp_029c_tcn_walker_s0_sigma01.log\\\", \\\"model_name\\\": \\\"dreamer\\\", \\\"pid\\\": \\\"59395\\\", \\\"seed\\\": 0, \\\"server\\\": \\\"bjb1-40020\\\", \\\"submitted_at\\\": \\\"2026-05-20T11:42:56.447Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\"}}, \\\"exp_029a_tcn_walker_s1_sigma02\\\": {\\\"spec\\\": {\\\"checkpoint_path\\\": \\\"/root/runs/event-gated-adaptive-horizon/exp_029a_tcn_walker_s1_sigma02/latest.pt\\\", \\\"command\\\": \\\"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --logdir ~/runs/event-gated-adaptive-horizon/exp_029a_tcn_walker_s1_sigma02\\\", \\\"data_count\\\": 210000, \\\"data_path\\\": \\\"dmc_walker_walk\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"log_path\\\": \\\"/root/runs/event-gated-adaptive-horizon/exp_029a_tcn_walker_s1_sigma02.log\\\", \\\"model_name\\\": \\\"dreamerv3\\\", \\\"pid\\\": \\\"50924\\\", \\\"seed\\\": 1, \\\"server\\\": \\\"bjb1-40020\\\"}}, \\\"exp_030b_tcn_cheetah_s0_sigma05\\\": {\\\"spec\\\": {\\\"checkpoint_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_030b_tcn_cheetah_s0_sigma05/latest.pt\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_030b_tcn_cheetah_s0_sigma05/metrics.jsonl\\\"}}, \\\"exp_027_tcn_walker_s1\\\": {\\\"spec\\\": {\\\"checkpoint_path\\\": \\\"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_027_tcn_walker_s1/\\\", \\\"log_path\\\": \\\"~/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s1.log\\\"}}, \\\"exp_027_tcn_walker_s0_sigma02\\\": {\\\"spec\\\": {\\\"checkpoint_path\\\": \\\"/root/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0_sigma02/latest.pt\\\", \\\"command\\\": \\\"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --logdir logdir/exp_027_tcn_walker_s0_sigma02\\\", \\\"data_count\\\": 215000, \\\"data_path\\\": \\\"dmc_walker_walk\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"log_path\\\": \\\"/root/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0_sigma02.log\\\", \\\"model_name\\\": \\\"dreamerv3\\\", \\\"seed\\\": 0, \\\"server\\\": \\\"bjb1-40020\\\"}}, \\\"exp_030a_tcn_cheetah_s0_sigma02\\\": {\\\"spec\\\": {\\\"checkpoint_path\\\": \\\"logdir/exp_030a_tcn_cheetah_s0_sigma02/\\\", \\\"checkpoint_source\\\": \\\"from_scratch\\\", \\\"command\\\": \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_enabled True --tcn_sigma 0.2 --logdir logdir/exp_030a_tcn_cheetah_s0_sigma02\\\", \\\"data_count\\\": \\\"210000 env steps\\\", \\\"data_path\\\": \\\"dmc_cheetah_run\\\", \\\"eval_data\\\": \\\"dmc_cheetah_run\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"log_path\\\": \\\"~/runs/event-gated-adaptive-horizon/exp_030a_tcn_cheetah_s0_sigma02.log\\\", \\\"model_name\\\": \\\"dreamerv3_tcn_sigma02_cheetah\\\", \\\"seed\\\": 0, \\\"server\\\": \\\"bjb1-45299\\\"}}, \\\"exp_027_tcn_walker_s0\\\": {\\\"spec\\\": {\\\"account\\\": \\\"root\\\", \\\"backend\\\": \\\"tmux\\\", \\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.5 --logdir logdir/exp_027_tcn_walker_s0\\\\\\\"\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"gpu_hours\\\": 3.18, \\\"log_path\\\": \\\"~/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0.log\\\", \\\"pid\\\": \\\"888715\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"submitted_at\\\": \\\"2026-05-20T06:13:35.505Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"wall_clock_seconds\\\": 11433.5}}, \\\"exp_028_rave_walker_s0_ceil15\\\": {\\\"spec\\\": {\\\"checkpoint_path\\\": \\\"~/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0_ceil15/\\\", \\\"checkpoint_source\\\": \\\"N/A (trained from scratch, hyperparameter variant of exp_028_rave_walker_s0)\\\", \\\"command\\\": \\\"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --rave_enabled True --rave_ceiling 1.5 --rave_ema_decay 0.99 --logdir ~/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0_ceil15'\\\", \\\"data_count\\\": \\\"210000 env steps\\\", \\\"data_path\\\": \\\"dmc_walker_walk\\\", \\\"eval_data\\\": \\\"dmc_walker_walk (online eval during training)\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"log_path\\\": \\\"~/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0_ceil15.log\\\", \\\"model_name\\\": \\\"dreamerv3_rave_ceil15\\\", \\\"note\\\": \\\"CUDA_VISIBLE_DEVICES=1 set by submit_training_job, device=cuda:0 within process\\\", \\\"pid\\\": \\\"38372\\\", \\\"seed\\\": 0, \\\"server\\\": \\\"bjb1-40020\\\", \\\"tmux_session\\\": \\\"exp_028_rave_walker_s0_ceil15\\\"}}, \\\"exp_028_rave_walker_s0\\\": {\\\"spec\\\": {\\\"account\\\": \\\"root\\\", \\\"backend\\\": \\\"tmux\\\", \\\"checkpoint_source\\\": \\\"N/A (trained from scratch, derives from SGS failure line)\\\", \\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 105000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --rave_ceiling 2.0 --logdir logdir/exp_028_rave_walker_s0\\\\\\\"\\\", \\\"data_count\\\": \\\"105000 env steps (52.5K agent steps, action_repeat=2)\\\", \\\"data_path\\\": \\\"dmc_walker_walk\\\", \\\"eval_data\\\": \\\"dmc_walker_walk (online eval during training)\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"gpu_hours\\\": 3.33, \\\"log_path\\\": \\\"~/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0.log\\\", \\\"model_name\\\": \\\"dreamerv3_rave_ceil20\\\", \\\"pid\\\": \\\"879636\\\", \\\"seed\\\": 0, \\\"server\\\": \\\"bjb1-45299\\\", \\\"submitted_at\\\": \\\"2026-05-20T02:54:26.022Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"wall_clock_seconds\\\": 12005.7}}, \\\"exp_025_obs_sgs_walker_s2\\\": {\\\"spec\\\": {\\\"checkpoint_path\\\": \\\"logdir/exp_025_obs_sgs_walker_s2/\\\", \\\"checkpoint_source\\\": \\\"N/A (trained from scratch)\\\", \\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 2 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_025_obs_sgs_walker_s2\\\", \\\"data_count\\\": \\\"210000 env steps (105K agent steps)\\\", \\\"data_path\\\": \\\"dmc_walker_walk\\\", \\\"eval_data\\\": \\\"dmc_walker_walk (online eval during training)\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"log_path\\\": \\\"logdir/exp_025_obs_sgs_walker_s2/train.log\\\", \\\"model_name\\\": \\\"dreamerv3_obs_decoder_sgs\\\", \\\"pid\\\": \\\"7989\\\", \\\"seed\\\": 2, \\\"server\\\": \\\"bjb1-40020\\\", \\\"tmux_session\\\": \\\"exp_025_s2\\\"}}, \\\"exp_026_obs_sgs_cheetah_s1\\\": {\\\"spec\\\": {\\\"checkpoint_path\\\": \\\"logdir/exp_026_obs_sgs_cheetah_s1/\\\", \\\"checkpoint_source\\\": \\\"N/A (trained from scratch)\\\", \\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 105000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_026_obs_sgs_cheetah_s1\\\", \\\"data_count\\\": \\\"105000 env steps\\\", \\\"data_path\\\": \\\"dmc_cheetah_run\\\", \\\"eval_data\\\": \\\"dmc_cheetah_run (online eval during training)\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"log_path\\\": \\\"logdir/exp_026_obs_sgs_cheetah_s1/train.log\\\", \\\"model_name\\\": \\\"dreamerv3_obs_decoder_sgs_cheetah\\\", \\\"pid\\\": \\\"16346\\\", \\\"seed\\\": 1, \\\"server\\\": \\\"bjb1-40020\\\", \\\"tmux_session\\\": \\\"exp_026_s1\\\"}}, \\\"exp_026_obs_sgs_cheetah_s0\\\": {\\\"spec\\\": {\\\"checkpoint_path\\\": \\\"logdir/exp_026_obs_sgs_cheetah_s0/\\\", \\\"checkpoint_source\\\": \\\"N/A (trained from scratch)\\\", \\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 105000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_026_obs_sgs_cheetah_s0\\\", \\\"data_count\\\": \\\"105000 env steps\\\", \\\"data_path\\\": \\\"dmc_cheetah_run\\\", \\\"eval_data\\\": \\\"dmc_cheetah_run (online eval during training)\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"log_path\\\": \\\"logdir/exp_026_obs_sgs_cheetah_s0/train.log\\\", \\\"model_name\\\": \\\"dreamerv3_obs_decoder_sgs_cheetah\\\", \\\"pid\\\": \\\"16208\\\", \\\"seed\\\": 0, \\\"server\\\": \\\"bjb1-40020\\\", \\\"tmux_session\\\": \\\"exp_026_s0\\\"}}, \\\"exp_025_obs_sgs_walker_s4\\\": {\\\"spec\\\": {\\\"checkpoint_path\\\": \\\"logdir/exp_025_obs_sgs_walker_s4/\\\", \\\"checkpoint_source\\\": \\\"N/A (trained from scratch)\\\", \\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 4 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_025_obs_sgs_walker_s4\\\", \\\"data_count\\\": \\\"210000 env steps (105K agent steps)\\\", \\\"data_path\\\": \\\"dmc_walker_walk\\\", \\\"eval_data\\\": \\\"dmc_walker_walk (online eval during training)\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"log_path\\\": \\\"logdir/exp_025_obs_sgs_walker_s4/train.log\\\", \\\"model_name\\\": \\\"dreamerv3_obs_decoder_sgs\\\", \\\"pid\\\": \\\"851593\\\", \\\"seed\\\": 4, \\\"server\\\": \\\"bjb1-45299\\\", \\\"tmux_session\\\": \\\"exp_025_s4\\\"}}, \\\"exp_025_obs_sgs_walker_s3\\\": {\\\"spec\\\": {\\\"checkpoint_path\\\": \\\"logdir/exp_025_obs_sgs_walker_s3/\\\", \\\"checkpoint_source\\\": \\\"N/A (trained from scratch)\\\", \\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 3 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_025_obs_sgs_walker_s3\\\", \\\"data_count\\\": \\\"210000 env steps (105K agent steps)\\\", \\\"data_path\\\": \\\"dmc_walker_walk\\\", \\\"eval_data\\\": \\\"dmc_walker_walk (online eval during training)\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"log_path\\\": \\\"logdir/exp_025_obs_sgs_walker_s3/train.log\\\", \\\"model_name\\\": \\\"dreamerv3_obs_decoder_sgs\\\", \\\"pid\\\": \\\"847597\\\", \\\"seed\\\": 3, \\\"server\\\": \\\"bjb1-45299\\\", \\\"tmux_session\\\": \\\"exp_025_s3\\\"}}, \\\"exp_025_obs_sgs_walker_s1\\\": {\\\"spec\\\": {\\\"checkpoint_path\\\": \\\"logdir/exp_025_obs_sgs_walker_s1/\\\", \\\"checkpoint_source\\\": \\\"N/A (trained from scratch)\\\", \\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_025_obs_sgs_walker_s1\\\", \\\"data_count\\\": \\\"210000 env steps (105K agent steps)\\\", \\\"data_path\\\": \\\"dmc_walker_walk\\\", \\\"eval_data\\\": \\\"dmc_walker_walk (online eval during training)\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"log_path\\\": \\\"logdir/exp_025_obs_sgs_walker_s1/train.log\\\", \\\"model_name\\\": \\\"dreamerv3_obs_decoder_sgs\\\", \\\"pid\\\": \\\"7833\\\", \\\"seed\\\": 1, \\\"server\\\": \\\"bjb1-40020\\\", \\\"tmux_session\\\": \\\"exp_025_s1\\\"}}, \\\"exp_001_baseline_s4_extended\\\": {\\\"spec\\\": {\\\"checkpoint_path\\\": \\\"logdir/exp_001_baseline_s4/\\\", \\\"checkpoint_source\\\": \\\"logdir/exp_001_baseline_s4/latest.pt\\\", \\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 505000 --seed 4 --device cuda:0 --compile False --gate_enabled False --logdir logdir/exp_001_baseline_s4\\\", \\\"data_count\\\": \\\"505000 env steps\\\", \\\"data_path\\\": \\\"dmc_walker_walk\\\", \\\"eval_data\\\": \\\"dmc_walker_walk (online eval during training)\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"log_path\\\": \\\"logdir/exp_001_baseline_s4/train_extended.log\\\", \\\"model_name\\\": \\\"dreamerv3_baseline\\\", \\\"resumed_from_step\\\": 112000, \\\"seed\\\": 4, \\\"server\\\": \\\"bjb1-45299\\\", \\\"target_steps\\\": 505000, \\\"tmux_session\\\": \\\"exp_s4_ext\\\"}}}, \\\"count\\\": 50, \\\"total\\\": 132, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.9546}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"exp_057_frozen_dt_emb_walker_s2\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_057_frozen_dt_emb_walker_s2\", \"server\": \"bjb1-45299\", \"gpu_ids\": [1], \"pid\": 157775, \"data_path\": \"dmc_walker_walk\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, Walker s2)\", \"seed\": 2, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"dmc_walker_walk (online eval)\", \"log_path\": \"logdir/exp_057_frozen_dt_emb_walker_s2/train.log\", \"checkpoint_path\": \"logdir/exp_057_frozen_dt_emb_walker_s2/checkpoint_225000.pt\"}}, \"exp_058_frozen_dt_emb_cheetah_s1\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_058_frozen_dt_emb_cheetah_s1\", \"server\": \"bjb1-45299\", \"gpu_ids\": [0], \"pid\": 164830, \"data_path\": \"dmc_cheetah_run\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, Cheetah s1)\", \"seed\": 1, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"dmc_cheetah_run (online eval)\", \"log_path\": \"logdir/exp_058_frozen_dt_emb_cheetah_s1/train.log\", \"checkpoint_path\": \"logdir/exp_058_frozen_dt_emb_cheetah_s1/checkpoint_225000.pt\"}}, \"exp_056_peginsertion_frozen_s1\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_EGL_DEVICE_ID=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs maniskill_peginsertion --task maniskill_PegInsertionSide-v1 --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_056_peginsertion_frozen_s1\", \"server\": \"bjb1-40020\", \"gpu_ids\": [1], \"pid\": 346430, \"data_path\": \"ManiSkill PegInsertionSide-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, fixed dt=2, ManiSkill PegInsertion s1)\", \"seed\": 1, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"PegInsertionSide-v1 (online eval)\", \"log_path\": \"logdir/exp_056_peginsertion_frozen_s1/train.log\", \"checkpoint_path\": \"logdir/exp_056_peginsertion_frozen_s1/checkpoint_202500.pt\"}}, \"exp_055_peginsertion_civo_trigger_s1\": {\"spec\": {\"command\": \"python -u dreamer.py --configs maniskill_peginsertion --task maniskill_PegInsertionSide-v1 --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_055_peginsertion_civo_trigger_s1\", \"server\": \"bjb1-40020\", \"gpu_ids\": [0], \"pid\": 345223, \"data_path\": \"ManiSkill PegInsertionSide-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO config, PegInsertion)\", \"seed\": 1, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"PegInsertionSide-v1 (online eval)\", \"log_path\": \"logdir/exp_055_peginsertion_civo_trigger_s1/train.log\"}}, \"exp_054_pickcube_frozen_s0\": {\"spec\": {\"command\": \"python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --seed 0 --steps 210000 --compile False --device cuda:0 --checkpoint_every 25000 --logdir logdir/exp_054_pickcube_frozen_s0\", \"server\": \"bjb1-45299\", \"gpu_ids\": [0], \"pid\": 133956, \"data_path\": \"ManiSkill PickCube-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, CIVO config, ManiSkill PickCube)\", \"seed\": 0, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"PickCube-v1 (online eval)\", \"log_path\": \"logdir/exp_054_pickcube_frozen_s0/metrics.jsonl\", \"checkpoint_path\": \"logdir/exp_054_pickcube_frozen_s0/checkpoint.ckpt\"}}, \"exp_053_peginsertion_frozen_s0\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_EGL_DEVICE_ID=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs maniskill_peginsertion --task maniskill_PegInsertionSide-v1 --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_053_peginsertion_frozen_s0\", \"server\": \"bjb1-45299\", \"gpu_ids\": [1], \"pid\": 123495, \"data_path\": \"ManiSkill PegInsertionSide-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, fixed dt=2, ManiSkill PegInsertion)\", \"seed\": 0, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"PegInsertionSide-v1 (online eval)\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_053_peginsertion_frozen_s0.log\", \"checkpoint_path\": \"logdir/exp_053_peginsertion_frozen_s0/checkpoint.ckpt\"}}, \"exp_050_peginsertion_civo_trigger_s0\": {\"spec\": {\"command\": \"LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs maniskill_peginsertion --task maniskill_PegInsertionSide-v1 --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_050_peginsertion_civo_trigger_s0\", \"server\": \"bjb1-40020\", \"data_path\": \"ManiSkill PegInsertionSide-v1 (state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 + CIVO trigger (gate_fixed_dt=2)\", \"seed\": 0, \"pid\": 304736, \"gpu_ids\": [0], \"log_path\": \"logdir/exp_050_peginsertion_civo_trigger_s0/train.log\", \"checkpoint_path\": \"logdir/exp_050_peginsertion_civo_trigger_s0\"}}, \"exp_051_stackcube_frozen_dt_emb_s0\": {\"spec\": {\"command\": \"python -u dreamer.py --configs maniskill_stackcube --task maniskill_StackCube-v1 --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_051_stackcube_frozen_dt_emb_s0\", \"server\": \"bjb1-40020\", \"gpu_ids\": [1], \"pid\": 305974, \"data_path\": \"ManiSkill StackCube-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, ManiSkill StackCube)\", \"seed\": 0, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"StackCube-v1 (online eval)\", \"log_path\": \"logdir/exp_051_stackcube_frozen_dt_emb_s0.log\", \"checkpoint_path\": \"logdir/exp_051_stackcube_frozen_dt_emb_s0/checkpoint_202500.pt\"}}, \"exp_052_stackcube_civo_trigger_s1\": {\"spec\": {\"command\": \"python -u dreamer.py --configs maniskill_stackcube --task maniskill_StackCube-v1 --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_052_stackcube_civo_trigger_s1\", \"server\": \"bjb1-45299\", \"gpu_ids\": [0], \"pid\": 103781, \"data_path\": \"ManiSkill StackCube-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO config, ManiSkill StackCube)\", \"seed\": 1, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"StackCube-v1 (online eval)\", \"log_path\": \"logdir/exp_052_stackcube_civo_trigger_s1/train.log\"}}, \"exp_049_stackcube_civo_trigger_s0\": {\"spec\": {\"command\": \"python -u dreamer.py --configs maniskill_stackcube --task maniskill_StackCube-v1 --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_049_stackcube_civo_trigger_s0\", \"server\": \"bjb1-45299\", \"gpu_ids\": [1], \"pid\": 91395, \"data_path\": \"ManiSkill StackCube-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO config, ManiSkill StackCube)\", \"seed\": 0, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"StackCube-v1 (online eval)\", \"log_path\": \"logdir/exp_049_stackcube_civo_trigger_s0/train.log\"}}, \"exp_048_cheetah_civo_extension\": {\"spec\": {\"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 300000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_048_cheetah_civo_extension\", \"server\": \"bjb1-45299\", \"gpu_ids\": [0], \"pid\": 88654, \"data_path\": \"dmc_cheetah_run (online RL)\", \"data_count\": 300000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO config, Cheetah)\", \"seed\": 0, \"checkpoint_source\": \"exp_010b_cheetah_civo_trigger_s0/latest.pt (step 105K, NVE=70.64)\", \"eval_data\": \"dmc_cheetah_run (online eval)\", \"log_path\": \"logdir/exp_048_cheetah_civo_extension/train.log\"}}, \"exp_047_frozen_dt_emb_walker_s1\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_047_frozen_dt_emb_walker_s1\", \"server\": \"bjb1-40020\", \"data_path\": \"dmc_walker_walk\", \"data_count\": 210000, \"model_name\": \"dreamer_gated_frozen_dt_emb\", \"seed\": 1, \"eval_data\": \"dmc_walker_walk (online eval)\", \"checkpoint_source\": \"N/A (training from scratch)\"}}, \"exp_046_frozen_dt_emb_cheetah\": {\"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_046_frozen_dt_emb_cheetah\", \"server\": \"bjb1-40020\", \"seed\": 0, \"model_name\": \"dreamerv3-cheetah-frozen-dt-emb\", \"data_path\": \"dmc_cheetah_run\", \"data_count\": 210000, \"eval_data\": \"dmc_cheetah_run (online eval)\", \"checkpoint_source\": \"N/A (training from scratch)\"}}, \"exp_044_gradient_stop_walker\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True --logdir logdir/exp_044_gradient_stop_walker\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:1\"], \"pid\": \"68371\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_044_gradient_stop_walker.log\", \"submitted_at\": \"2026-05-22T09:08:10.295Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"DMC Walker Walk\", \"data_count\": 210000, \"model_name\": \"DreamerV3 + reward_dt_emb_detach\", \"seed\": 0, \"checkpoint_source\": \"N/A - training from scratch\", \"eval_data\": \"dmc_walker_walk\", \"wall_clock_seconds\": 25212.4, \"gpu_hours\": 7.0}}, \"exp_045_treatment_extension_008d_s3\": {\"spec\": {\"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 300000 --seed 3 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_045_treatment_extension_008d_s3\", \"server\": \"bjb1-45299\", \"gpu_ids\": [0], \"pid\": \"70945\", \"data_path\": \"dmc_walker_walk (online RL)\", \"data_count\": 300000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO config)\", \"seed\": 3, \"checkpoint_source\": \"exp_008d_civo_trigger_s3/latest.pt (step 112K)\", \"eval_data\": \"dmc_walker_walk (online eval, same as training env)\", \"log_path\": \"logdir/exp_045_treatment_extension_008d_s3/train.log\"}}, \"exp_043_008f_walker_s1\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --logdir logdir/exp_043_008f_walker_s1\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Walker Walk\", \"gpu\": [\"cuda:1\"], \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_043_008f_walker_s1\", \"model_name\": \"DreamerV3 (no dt_emb, 008f control)\", \"pid\": \"250627\", \"seed\": 1, \"server\": \"bjb1-40020\", \"submitted_via\": \"submit_training_job\"}}, \"exp_042_frozen_dt_emb_walker\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --logdir logdir/exp_042_frozen_dt_emb_walker\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Walker Walk\", \"gpu\": [\"cuda:0\"], \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_042_frozen_dt_emb_walker\", \"model_name\": \"DreamerV3 + frozen dt_emb\", \"pid\": \"251336\", \"seed\": 0, \"server\": \"bjb1-40020\"}}, \"exp_040_wide_dual_critic_cheetah\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --logdir logdir/exp_040_wide_dual_critic_cheetah\\\"\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_040_wide_dual_critic_cheetah.log\", \"pid\": \"52397\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-21T19:51:11.519Z\", \"submitted_via\": \"submit_training_job\", \"seed\": 1, \"wall_clock_seconds\": 49438.9, \"gpu_hours\": 13.73}}, \"exp_041_dual_critic_walker_s3\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 3 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --logdir logdir/exp_041_dual_critic_walker_s3\\\"\", \"gpu\": [\"cuda:1\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_041_dual_critic_walker_s3.log\", \"pid\": \"51103\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-22T02:38:20.728Z\", \"submitted_via\": \"submit_training_job\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_041_dual_critic_walker_s3/checkpoint.pt\", \"checkpoint_source\": \"N/A - training from scratch\", \"eval_data\": \"dmc_walker_walk\", \"wall_clock_seconds\": 23112.0, \"gpu_hours\": 6.42}}, \"exp_039_narrow_dual_critic_walker_s1\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_039_narrow_dual_critic_walker_s1/latest.pt\", \"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --narrow_dual_critic True --logdir logdir/exp_039_narrow_dual_critic_walker_s1\\\"\", \"eval_data\": \"N/A - training experiment\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 10.06, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_039_narrow_dual_critic_walker_s1.log\", \"pid\": \"198771\", \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-21T16:31:39.634Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 36234.0}}, \"exp_038_dual_critic_walker_s2\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_038_dual_critic_walker_s2/latest.pt\", \"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"bash -c \\\"...dual_critic walker s2...\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Walker Walk\", \"eval_data\": \"N/A - training experiment\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 13.88, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_038_dual_critic_walker_s2\", \"model_name\": \"DreamerV3 + Dual Critic (wide)\", \"pid\": \"175633\", \"seed\": 2, \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-21T12:18:34.859Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 49982.0}}, \"exp_037_wide_critic_cheetah\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A\", \"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"bash -c \\\"...wide_critic cheetah...\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Cheetah Run\", \"eval_data\": \"N/A - training experiment\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 7.46, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_037_wide_critic_cheetah.log\", \"model_name\": \"DreamerV3 + Wide Single Critic\", \"pid\": \"14487\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-21T12:18:32.619Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 26839.7}}, \"exp_036_dual_critic_pickcube\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --seed 0 --steps 200000 --compile False --device cuda:0 --logdir ./logdir/exp_036_dual_critic_pickcube\\\"\", \"data_count\": 200000, \"data_path\": \"ManiSkill PickCube-v1\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 11.03, \"gpu_id\": 0, \"hyperparams\": {\"dual_critic\": true, \"gate_enabled\": true, \"gate_fixed_dt\": 2, \"gate_subsample_max_dt\": 2, \"imag_horizon\": 8, \"tcn_sigma\": 0.0}, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_036_dual_critic_pickcube.log\", \"model_name\": \"DreamerV3 + Dual Critic\", \"pid\": \"2476\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-21T08:43:44.544357+00:00\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 39706.7}}, \"exp_035_narrow_dual_critic_walker\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --narrow_dual_critic True --logdir logdir/exp_035_narrow_dual_critic_walker\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 8.31, \"gpu_id\": 1, \"hyperparams\": {\"critic_hidden\": 256, \"critic_layers\": 2, \"critic_params_each\": 525000, \"critic_params_total\": 1050000, \"gate_enabled\": true, \"gate_fixed_dt\": 2, \"gate_subsample_max_dt\": 2, \"imag_horizon\": 8, \"narrow_dual_critic\": true}, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_035_narrow_dual_critic_walker.log\", \"model_name\": \"DreamerV3 + Narrow Dual Critic (2×256 hidden, 1.05M total)\", \"pid\": \"162900\", \"seed\": 0, \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-21T07:56:05.926445+00:00\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 29900.2}}, \"exp_034\": {\"spec\": {\"command\": \"python train.py --configs dmc_cheetah_run --dual_critic True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --steps 210000 --seed 0\", \"data_count\": 0, \"data_path\": \"dmc_cheetah_run\", \"model_name\": \"dreamerv3\", \"seed\": 0, \"server\": \"bjb1-45299\"}}, \"exp_034_dual_critic_cheetah\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --logdir logdir/exp_034_dual_critic_cheetah\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Cheetah Run (dm_control built-in)\", \"gpu\": [\"cuda:1\"], \"gpu_id\": 1, \"hyperparams\": {\"dual_critic\": true, \"gate_enabled\": true, \"gate_fixed_dt\": 2, \"gate_subsample_max_dt\": 2, \"imag_horizon\": 8, \"tcn_sigma\": 0.0}, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_034_dual_critic_cheetah.log\", \"model_name\": \"DreamerV3 + Dual Critic\", \"pid\": \"993925\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-21T05:51:51.325323+00:00\", \"submitted_via\": \"submit_training_job\"}}, \"exp_033_wide_critic_walker\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --wide_critic True --logdir logdir/exp_033_wide_critic_walker\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 8.25, \"gpu_id\": 0, \"hyperparams\": {\"critic_hidden\": 1024, \"critic_layers\": 2, \"critic_params\": 2886911, \"dual_critic\": false, \"gate_enabled\": true, \"gate_fixed_dt\": 2, \"gate_subsample_max_dt\": 2, \"imag_horizon\": 8, \"wide_critic\": true}, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_033_wide_critic_walker.log\", \"model_name\": \"DreamerV3 + Wide Critic (1024 hidden, 2.89M params, 2.44× normal)\", \"pid\": \"151860\", \"seed\": 0, \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-21T03:52:59.702597+00:00\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 29715.5}}, \"exp_031b_tcn_pickcube_s0_sigma05\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.5 --seed 0 --steps 200000 --compile False --device cuda:0 --logdir ./logdir/exp_031b_tcn_pickcube_s0_sigma05\\\"\", \"data_count\": 200000, \"data_path\": \"ManiSkill PickCube-v1\", \"gpu\": [\"cuda:0\"], \"gpu_id\": 0, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_031b_tcn_pickcube_s0_sigma05.log\", \"model_name\": \"DreamerV3 + TCN σ=0.5\", \"pid\": \"968495\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-20T22:33:14.695383+00:00\", \"submitted_via\": \"submit_training_job\"}}, \"exp_032_dual_critic_walker\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_032_dual_critic_walker\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --logdir logdir/exp_032_dual_critic_walker\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"gpu\": [\"cuda:1\"], \"gpu_id\": 1, \"hyperparams\": {\"dual_critic\": true, \"gate_enabled\": true, \"gate_fixed_dt\": 2, \"gate_subsample_max_dt\": 2, \"imag_horizon\": 8, \"tcn_sigma\": 0.0}, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_032_dual_critic_walker.log\", \"model_name\": \"DreamerV3 + Dual Critic (min of two independent critics)\", \"pid\": \"124556\", \"seed\": 0, \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-20T23:19:57.690519+00:00\", \"submitted_via\": \"submit_training_job\"}}, \"exp_032b_dual_critic_walker_s1\": {\"spec\": {\"data_count\": 210000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"hyperparams\": {\"dual_critic\": true, \"gate_enabled\": true, \"gate_fixed_dt\": 2, \"gate_subsample_max_dt\": 2, \"imag_horizon\": 8, \"tcn_sigma\": 0}, \"model_name\": \"DreamerV3 + Dual Critic (min of two independent critics)\", \"seed\": 1}}, \"exp_029d_tcn_walker_s3_sigma02\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_029d_tcn_walker_s3_sigma02\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 3 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --logdir logdir/exp_029d_tcn_walker_s3_sigma02\\\"\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_029d_tcn_walker_s3_sigma02.log\", \"pid\": \"109826\", \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-20T19:33:48.032Z\", \"submitted_via\": \"submit_training_job\"}}, \"exp_031_tcn_pickcube_s0_sigma02\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"none(train_from_scratch)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --seed 0 --steps 200000 --compile False --device cuda:0 --logdir ./logdir/exp_031_tcn_pickcube_s0_sigma02\\\"\", \"data_count\": \"200000(online)\", \"data_path\": \"maniskill_PickCube-v1\", \"eval_data\": \"maniskill_PickCube-v1(online_eval)\", \"gpu\": \"cuda:1\", \"gpu_hours\": 11.17, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_031_tcn_pickcube_s0_sigma02.log\", \"model_name\": \"dreamerv3\", \"pid\": \"908459\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-20T12:42:41.707Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 40206.6}}, \"exp_029b_tcn_walker_s2_sigma02\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_029b_tcn_walker_s2_sigma02\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 2 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --logdir logdir/exp_029b_tcn_walker_s2_sigma02\\\"\", \"gpu\": [\"cuda:1\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_029b_tcn_walker_s2_sigma02.log\", \"pid\": \"75543\", \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-20T16:56:24.781Z\", \"submitted_via\": \"submit_training_job\"}}, \"exp_030c_tcn_cheetah_s0_sigma10\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_030c_tcn_cheetah_s0_sigma10\", \"command\": \"dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 0 --tcn_sigma 1.0\", \"data_count\": 210000, \"data_path\": \"dmc_cheetah_run\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_030c_tcn_cheetah_s0_sigma10.log\", \"model_name\": \"dreamerv3\", \"pid\": \"920968\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-20T16:49:48.464Z\", \"submitted_via\": \"submit_training_job\"}}, \"exp_029c_tcn_walker_s0_sigma01\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_029c_tcn_walker_s0_sigma01/latest.pt\", \"checkpoint_source\": \"from_scratch\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.1 --logdir logdir/exp_029c_tcn_walker_s0_sigma01\\\"\", \"data_count\": 210000, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_029c_tcn_walker_s0_sigma01.log\", \"model_name\": \"dreamer\", \"pid\": \"59395\", \"seed\": 0, \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-20T11:42:56.447Z\", \"submitted_via\": \"submit_training_job\"}}, \"exp_029a_tcn_walker_s1_sigma02\": {\"spec\": {\"checkpoint_path\": \"/root/runs/event-gated-adaptive-horizon/exp_029a_tcn_walker_s1_sigma02/latest.pt\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --logdir ~/runs/event-gated-adaptive-horizon/exp_029a_tcn_walker_s1_sigma02\", \"data_count\": 210000, \"data_path\": \"dmc_walker_walk\", \"gpu\": \"cuda:1\", \"log_path\": \"/root/runs/event-gated-adaptive-horizon/exp_029a_tcn_walker_s1_sigma02.log\", \"model_name\": \"dreamerv3\", \"pid\": \"50924\", \"seed\": 1, \"server\": \"bjb1-40020\"}}, \"exp_030b_tcn_cheetah_s0_sigma05\": {\"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_030b_tcn_cheetah_s0_sigma05/latest.pt\", \"gpu\": \"cuda:0\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_030b_tcn_cheetah_s0_sigma05/metrics.jsonl\"}}, \"exp_027_tcn_walker_s1\": {\"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_027_tcn_walker_s1/\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s1.log\"}}, \"exp_027_tcn_walker_s0_sigma02\": {\"spec\": {\"checkpoint_path\": \"/root/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0_sigma02/latest.pt\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --logdir logdir/exp_027_tcn_walker_s0_sigma02\", \"data_count\": 215000, \"data_path\": \"dmc_walker_walk\", \"gpu\": \"cuda:0\", \"log_path\": \"/root/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0_sigma02.log\", \"model_name\": \"dreamerv3\", \"seed\": 0, \"server\": \"bjb1-40020\"}}, \"exp_030a_tcn_cheetah_s0_sigma02\": {\"spec\": {\"checkpoint_path\": \"logdir/exp_030a_tcn_cheetah_s0_sigma02/\", \"checkpoint_source\": \"from_scratch\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_enabled True --tcn_sigma 0.2 --logdir logdir/exp_030a_tcn_cheetah_s0_sigma02\", \"data_count\": \"210000 env steps\", \"data_path\": \"dmc_cheetah_run\", \"eval_data\": \"dmc_cheetah_run\", \"gpu\": \"cuda:0\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_030a_tcn_cheetah_s0_sigma02.log\", \"model_name\": \"dreamerv3_tcn_sigma02_cheetah\", \"seed\": 0, \"server\": \"bjb1-45299\"}}, \"exp_027_tcn_walker_s0\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.5 --logdir logdir/exp_027_tcn_walker_s0\\\"\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 3.18, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0.log\", \"pid\": \"888715\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-20T06:13:35.505Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 11433.5}}, \"exp_028_rave_walker_s0_ceil15\": {\"spec\": {\"checkpoint_path\": \"~/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0_ceil15/\", \"checkpoint_source\": \"N/A (trained from scratch, hyperparameter variant of exp_028_rave_walker_s0)\", \"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --rave_enabled True --rave_ceiling 1.5 --rave_ema_decay 0.99 --logdir ~/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0_ceil15'\", \"data_count\": \"210000 env steps\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:1\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0_ceil15.log\", \"model_name\": \"dreamerv3_rave_ceil15\", \"note\": \"CUDA_VISIBLE_DEVICES=1 set by submit_training_job, device=cuda:0 within process\", \"pid\": \"38372\", \"seed\": 0, \"server\": \"bjb1-40020\", \"tmux_session\": \"exp_028_rave_walker_s0_ceil15\"}}, \"exp_028_rave_walker_s0\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"N/A (trained from scratch, derives from SGS failure line)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 105000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --rave_ceiling 2.0 --logdir logdir/exp_028_rave_walker_s0\\\"\", \"data_count\": \"105000 env steps (52.5K agent steps, action_repeat=2)\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 3.33, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0.log\", \"model_name\": \"dreamerv3_rave_ceil20\", \"pid\": \"879636\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-20T02:54:26.022Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 12005.7}}, \"exp_025_obs_sgs_walker_s2\": {\"spec\": {\"checkpoint_path\": \"logdir/exp_025_obs_sgs_walker_s2/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 2 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_025_obs_sgs_walker_s2\", \"data_count\": \"210000 env steps (105K agent steps)\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:1\"], \"log_path\": \"logdir/exp_025_obs_sgs_walker_s2/train.log\", \"model_name\": \"dreamerv3_obs_decoder_sgs\", \"pid\": \"7989\", \"seed\": 2, \"server\": \"bjb1-40020\", \"tmux_session\": \"exp_025_s2\"}}, \"exp_026_obs_sgs_cheetah_s1\": {\"spec\": {\"checkpoint_path\": \"logdir/exp_026_obs_sgs_cheetah_s1/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 105000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_026_obs_sgs_cheetah_s1\", \"data_count\": \"105000 env steps\", \"data_path\": \"dmc_cheetah_run\", \"eval_data\": \"dmc_cheetah_run (online eval during training)\", \"gpu\": [\"cuda:1\"], \"log_path\": \"logdir/exp_026_obs_sgs_cheetah_s1/train.log\", \"model_name\": \"dreamerv3_obs_decoder_sgs_cheetah\", \"pid\": \"16346\", \"seed\": 1, \"server\": \"bjb1-40020\", \"tmux_session\": \"exp_026_s1\"}}, \"exp_026_obs_sgs_cheetah_s0\": {\"spec\": {\"checkpoint_path\": \"logdir/exp_026_obs_sgs_cheetah_s0/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 105000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_026_obs_sgs_cheetah_s0\", \"data_count\": \"105000 env steps\", \"data_path\": \"dmc_cheetah_run\", \"eval_data\": \"dmc_cheetah_run (online eval during training)\", \"gpu\": [\"cuda:0\"], \"log_path\": \"logdir/exp_026_obs_sgs_cheetah_s0/train.log\", \"model_name\": \"dreamerv3_obs_decoder_sgs_cheetah\", \"pid\": \"16208\", \"seed\": 0, \"server\": \"bjb1-40020\", \"tmux_session\": \"exp_026_s0\"}}, \"exp_025_obs_sgs_walker_s4\": {\"spec\": {\"checkpoint_path\": \"logdir/exp_025_obs_sgs_walker_s4/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 4 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_025_obs_sgs_walker_s4\", \"data_count\": \"210000 env steps (105K agent steps)\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:1\"], \"log_path\": \"logdir/exp_025_obs_sgs_walker_s4/train.log\", \"model_name\": \"dreamerv3_obs_decoder_sgs\", \"pid\": \"851593\", \"seed\": 4, \"server\": \"bjb1-45299\", \"tmux_session\": \"exp_025_s4\"}}, \"exp_025_obs_sgs_walker_s3\": {\"spec\": {\"checkpoint_path\": \"logdir/exp_025_obs_sgs_walker_s3/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 3 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_025_obs_sgs_walker_s3\", \"data_count\": \"210000 env steps (105K agent steps)\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:0\"], \"log_path\": \"logdir/exp_025_obs_sgs_walker_s3/train.log\", \"model_name\": \"dreamerv3_obs_decoder_sgs\", \"pid\": \"847597\", \"seed\": 3, \"server\": \"bjb1-45299\", \"tmux_session\": \"exp_025_s3\"}}, \"exp_025_obs_sgs_walker_s1\": {\"spec\": {\"checkpoint_path\": \"logdir/exp_025_obs_sgs_walker_s1/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_025_obs_sgs_walker_s1\", \"data_count\": \"210000 env steps (105K agent steps)\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:0\"], \"log_path\": \"logdir/exp_025_obs_sgs_walker_s1/train.log\", \"model_name\": \"dreamerv3_obs_decoder_sgs\", \"pid\": \"7833\", \"seed\": 1, \"server\": \"bjb1-40020\", \"tmux_session\": \"exp_025_s1\"}}, \"exp_001_baseline_s4_extended\": {\"spec\": {\"checkpoint_path\": \"logdir/exp_001_baseline_s4/\", \"checkpoint_source\": \"logdir/exp_001_baseline_s4/latest.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 505000 --seed 4 --device cuda:0 --compile False --gate_enabled False --logdir logdir/exp_001_baseline_s4\", \"data_count\": \"505000 env steps\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": \"cuda:1\", \"log_path\": \"logdir/exp_001_baseline_s4/train_extended.log\", \"model_name\": \"dreamerv3_baseline\", \"resumed_from_step\": 112000, \"seed\": 4, \"server\": \"bjb1-45299\", \"target_steps\": 505000, \"tmux_session\": \"exp_s4_ext\"}}}, \"count\": 50, \"total\": 132, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9546}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 16_

<details><summary>Logged reasoning block</summary>

```text
The registry doesn't have exp_008d directly. Let me search for it specifically - maybe the exp_id contains "008d" in a different format. Let me look for all experiments with "008d" in the name.

From the user's message, the 008d series experiments are:
- seed 1: exp_008d_subsample_on_h8 
- seed 2: exp_009b_008d_walker_s2
- seed 3: exp_008d_civo_trigger_s3


- seed 4: exp_008d_civo_trigger_s4

The original exp_008d might be seed 0 or 1. Since these aren't showing up in the first batch of results, I should try adjusting my search parameters or pagination.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2fe83aea-5863-4eb4-8029-aa58f80fcf56",
  "uuid": "f69599a7-3bbc-4d10-ad7a-bc1b66e2f2b9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015e4mQyCtx91EfrS4FGh5zo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18977,
      "cache_read_input_tokens": 25045,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18977
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

_source line 17_

Registry 前 50 条没有 008d 系列（编号较早）。继续搜索。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2fe83aea-5863-4eb4-8029-aa58f80fcf56",
  "uuid": "64a63a49-b618-47b6-a977-25f48ef61554",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015e4mQyCtx91EfrS4FGh5zo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18977,
      "cache_read_input_tokens": 25045,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18977
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

_source line 18_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_019RLcwT3jBjAkyvcvyjjDm3`</summary>

```json
{
  "filters": {},
  "fields": [
    "exp_id",
    "spec"
  ],
  "project": "event-gated-adaptive-horizon",
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
  "session_id": "2fe83aea-5863-4eb4-8029-aa58f80fcf56",
  "uuid": "e750a69b-1cc9-449c-adf5-9784861f33b1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015e4mQyCtx91EfrS4FGh5zo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18977,
      "cache_read_input_tokens": 25045,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18977
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

_source line 19 · 2026-05-24T03:07:43.568Z_

<details><summary>↩ Tool result · `toolu_019RLcwT3jBjAkyvcvyjjDm3`</summary>

```text
Error: result (108,582 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/2fe83aea-5863-4eb4-8029-aa58f80fcf56/tool-results/mcp-agent-ml-research-read_registry-1779592063540.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/2fe83aea-5863-4eb4-8029-aa58f80fcf56/tool-results/mcp-agent-ml-research-read_registry-1779592063540.txt in sequential chunks until 100% of the content has been read.
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
  "session_id": "2fe83aea-5863-4eb4-8029-aa58f80fcf56",
  "uuid": "20e9f6f2-a4fe-40b8-977d-25f5133c4112",
  "tool_use_result": {
    "content": "Error: result (108,582 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/2fe83aea-5863-4eb4-8029-aa58f80fcf56/tool-results/mcp-agent-ml-research-read_registry-1779592063540.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/2fe83aea-5863-4eb4-8029-aa58f80fcf56/tool-results/mcp-agent-ml-research-read_registry-1779592063540.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"exp_057_frozen_dt_emb_walker_s2\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_057_frozen_dt_emb_walker_s2\", \"server\": \"bjb1-45299\", \"gpu_ids\": [1], \"pid\": 157775, \"data_path\": \"dmc_walker_walk\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, Walker s2)\", \"seed\": 2, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"dmc_walker_walk (online eval)\", \"log_path\": \"logdir/exp_057_frozen_dt_emb_walker_s2/train.log\", \"checkpoint_path\": \"logdir/exp_057_frozen_dt_emb_walker_s2/checkpoint_225000.pt\"}}, \"exp_058_frozen_dt_emb_cheetah_s1\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_058_frozen_dt_emb_cheetah_s1\", \"server\": \"bjb1-45299\", \"gpu_ids\": [0], \"pid\": 164830, \"data_path\": \"dmc_cheetah_run\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, Cheetah s1)\", \"seed\": 1, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"dmc_cheetah_run (online eval)\", \"log_path\": \"logdir/exp_058_frozen_dt_emb_cheetah_s1/train.log\", \"checkpoint_path\": \"logdir/exp_058_frozen_dt_emb_cheetah_s1/checkpoint_225000.pt\"}}, \"exp_056_peginsertion_frozen_s1\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_EGL_DEVICE_ID=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs maniskill_peginsertion --task maniskill_PegInsertionSide-v1 --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_056_peginsertion_frozen_s1\", \"server\": \"bjb1-40020\", \"gpu_ids\": [1], \"pid\": 346430, \"data_path\": \"ManiSkill PegInsertionSide-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, fixed dt=2, ManiSkill PegInsertion s1)\", \"seed\": 1, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"PegInsertionSide-v1 (online eval)\", \"log_path\": \"logdir/exp_056_peginsertion_frozen_s1/train.log\", \"checkpoint_path\": \"logdir/exp_056_peginsertion_frozen_s1/checkpoint_202500.pt\"}}, \"exp_055_peginsertion_civo_trigger_s1\": {\"spec\": {\"command\": \"python -u dreamer.py --configs maniskill_peginsertion --task maniskill_PegInsertionSide-v1 --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_055_peginsertion_civo_trigger_s1\", \"server\": \"bjb1-40020\", \"gpu_ids\": [0], \"pid\": 345223, \"data_path\": \"ManiSkill PegInsertionSide-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO config, PegInsertion)\", \"seed\": 1, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"PegInsertionSide-v1 (online eval)\", \"log_path\": \"logdir/exp_055_peginsertion_civo_trigger_s1/train.log\"}}, \"exp_054_pickcube_frozen_s0\": {\"spec\": {\"command\": \"python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --seed 0 --steps 210000 --compile False --device cuda:0 --checkpoint_every 25000 --logdir logdir/exp_054_pickcube_frozen_s0\", \"server\": \"bjb1-45299\", \"gpu_ids\": [0], \"pid\": 133956, \"data_path\": \"ManiSkill PickCube-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, CIVO config, ManiSkill PickCube)\", \"seed\": 0, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"PickCube-v1 (online eval)\", \"log_path\": \"logdir/exp_054_pickcube_frozen_s0/metrics.jsonl\", \"checkpoint_path\": \"logdir/exp_054_pickcube_frozen_s0/checkpoint.ckpt\"}}, \"exp_053_peginsertion_frozen_s0\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_EGL_DEVICE_ID=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs maniskill_peginsertion --task maniskill_PegInsertionSide-v1 --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_053_peginsertion_frozen_s0\", \"server\": \"bjb1-45299\", \"gpu_ids\": [1], \"pid\": 123495, \"data_path\": \"ManiSkill PegInsertionSide-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, fixed dt=2, ManiSkill PegInsertion)\", \"seed\": 0, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"PegInsertionSide-v1 (online eval)\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_053_peginsertion_frozen_s0.log\", \"checkpoint_path\": \"logdir/exp_053_peginsertion_frozen_s0/checkpoint.ckpt\"}}, \"exp_050_peginsertion_civo_trigger_s0\": {\"spec\": {\"command\": \"LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs maniskill_peginsertion --task maniskill_PegInsertionSide-v1 --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_050_peginsertion_civo_trigger_s0\", \"server\": \"bjb1-40020\", \"data_path\": \"ManiSkill PegInsertionSide-v1 (state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 + CIVO trigger (gate_fixed_dt=2)\", \"seed\": 0, \"pid\": 304736, \"gpu_ids\": [0], \"log_path\": \"logdir/exp_050_peginsertion_civo_trigger_s0/train.log\", \"checkpoint_path\": \"logdir/exp_050_peginsertion_civo_trigger_s0\"}}, \"exp_051_stackcube_frozen_dt_emb_s0\": {\"spec\": {\"command\": \"python -u dreamer.py --configs maniskill_stackcube --task maniskill_StackCube-v1 --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_051_stackcube_frozen_dt_emb_s0\", \"server\": \"bjb1-40020\", \"gpu_ids\": [1], \"pid\": 305974, \"data_path\": \"ManiSkill StackCube-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, ManiSkill StackCube)\", \"seed\": 0, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"StackCube-v1 (online eval)\", \"log_path\": \"logdir/exp_051_stackcube_frozen_dt_emb_s0.log\", \"checkpoint_path\": \"logdir/exp_051_stackcube_frozen_dt_emb_s0/checkpoint_202500.pt\"}}, \"exp_052_stackcube_civo_trigger_s1\": {\"spec\": {\"command\": \"python -u dreamer.py --configs maniskill_stackcube --task maniskill_StackCube-v1 --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_052_stackcube_civo_trigger_s1\", \"server\": \"bjb1-45299\", \"gpu_ids\": [0], \"pid\": 103781, \"data_path\": \"ManiSkill StackCube-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO config, ManiSkill StackCube)\", \"seed\": 1, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"StackCube-v1 (online eval)\", \"log_path\": \"logdir/exp_052_stackcube_civo_trigger_s1/train.log\"}}, \"exp_049_stackcube_civo_trigger_s0\": {\"spec\": {\"command\": \"python -u dreamer.py --configs maniskill_stackcube --task maniskill_StackCube-v1 --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_049_stackcube_civo_trigger_s0\", \"server\": \"bjb1-45299\", \"gpu_ids\": [1], \"pid\": 91395, \"data_path\": \"ManiSkill StackCube-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO config, ManiSkill StackCube)\", \"seed\": 0, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"StackCube-v1 (online eval)\", \"log_path\": \"logdir/exp_049_stackcube_civo_trigger_s0/train.log\"}}, \"exp_048_cheetah_civo_extension\": {\"spec\": {\"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 300000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_048_cheetah_civo_extension\", \"server\": \"bjb1-45299\", \"gpu_ids\": [0], \"pid\": 88654, \"data_path\": \"dmc_cheetah_run (online RL)\", \"data_count\": 300000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO config, Cheetah)\", \"seed\": 0, \"checkpoint_source\": \"exp_010b_cheetah_civo_trigger_s0/latest.pt (step 105K, NVE=70.64)\", \"eval_data\": \"dmc_cheetah_run (online eval)\", \"log_path\": \"logdir/exp_048_cheetah_civo_extension/train.log\"}}, \"exp_047_frozen_dt_emb_walker_s1\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_047_frozen_dt_emb_walker_s1\", \"server\": \"bjb1-40020\", \"data_path\": \"dmc_walker_walk\", \"data_count\": 210000, \"model_name\": \"dreamer_gated_frozen_dt_emb\", \"seed\": 1, \"eval_data\": \"dmc_walker_walk (online eval)\", \"checkpoint_source\": \"N/A (training from scratch)\"}}, \"exp_046_frozen_dt_emb_cheetah\": {\"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_046_frozen_dt_emb_cheetah\", \"server\": \"bjb1-40020\", \"seed\": 0, \"model_name\": \"dreamerv3-cheetah-frozen-dt-emb\", \"data_path\": \"dmc_cheetah_run\", \"data_count\": 210000, \"eval_data\": \"dmc_cheetah_run (online eval)\", \"checkpoint_source\": \"N/A (training from scratch)\"}}, \"exp_044_gradient_stop_walker\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True --logdir logdir/exp_044_gradient_stop_walker\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:1\"], \"pid\": \"68371\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_044_gradient_stop_walker.log\", \"submitted_at\": \"2026-05-22T09:08:10.295Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"DMC Walker Walk\", \"data_count\": 210000, \"model_name\": \"DreamerV3 + reward_dt_emb_detach\", \"seed\": 0, \"checkpoint_source\": \"N/A - training from scratch\", \"eval_data\": \"dmc_walker_walk\", \"wall_clock_seconds\": 25212.4, \"gpu_hours\": 7.0}}, \"exp_045_treatment_extension_008d_s3\": {\"spec\": {\"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 300000 --seed 3 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_045_treatment_extension_008d_s3\", \"server\": \"bjb1-45299\", \"gpu_ids\": [0], \"pid\": \"70945\", \"data_path\": \"dmc_walker_walk (online RL)\", \"data_count\": 300000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO config)\", \"seed\": 3, \"checkpoint_source\": \"exp_008d_civo_trigger_s3/latest.pt (step 112K)\", \"eval_data\": \"dmc_walker_walk (online eval, same as training env)\", \"log_path\": \"logdir/exp_045_treatment_extension_008d_s3/train.log\"}}, \"exp_043_008f_walker_s1\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --logdir logdir/exp_043_008f_walker_s1\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Walker Walk\", \"gpu\": [\"cuda:1\"], \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_043_008f_walker_s1\", \"model_name\": \"DreamerV3 (no dt_emb, 008f control)\", \"pid\": \"250627\", \"seed\": 1, \"server\": \"bjb1-40020\", \"submitted_via\": \"submit_training_job\"}}, \"exp_042_frozen_dt_emb_walker\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --logdir logdir/exp_042_frozen_dt_emb_walker\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Walker Walk\", \"gpu\": [\"cuda:0\"], \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_042_frozen_dt_emb_walker\", \"model_name\": \"DreamerV3 + frozen dt_emb\", \"pid\": \"251336\", \"seed\": 0, \"server\": \"bjb1-40020\"}}, \"exp_040_wide_dual_critic_cheetah\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --logdir logdir/exp_040_wide_dual_critic_cheetah\\\"\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_040_wide_dual_critic_cheetah.log\", \"pid\": \"52397\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-21T19:51:11.519Z\", \"submitted_via\": \"submit_training_job\", \"seed\": 1, \"wall_clock_seconds\": 49438.9, \"gpu_hours\": 13.73}}, \"exp_041_dual_critic_walker_s3\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 3 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --logdir logdir/exp_041_dual_critic_walker_s3\\\"\", \"gpu\": [\"cuda:1\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_041_dual_critic_walker_s3.log\", \"pid\": \"51103\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-22T02:38:20.728Z\", \"submitted_via\": \"submit_training_job\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_041_dual_critic_walker_s3/checkpoint.pt\", \"checkpoint_source\": \"N/A - training from scratch\", \"eval_data\": \"dmc_walker_walk\", \"wall_clock_seconds\": 23112.0, \"gpu_hours\": 6.42}}, \"exp_039_narrow_dual_critic_walker_s1\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_039_narrow_dual_critic_walker_s1/latest.pt\", \"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --narrow_dual_critic True --logdir logdir/exp_039_narrow_dual_critic_walker_s1\\\"\", \"eval_data\": \"N/A - training experiment\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 10.06, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_039_narrow_dual_critic_walker_s1.log\", \"pid\": \"198771\", \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-21T16:31:39.634Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 36234.0}}, \"exp_038_dual_critic_walker_s2\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_038_dual_critic_walker_s2/latest.pt\", \"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"bash -c \\\"...dual_critic walker s2...\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Walker Walk\", \"eval_data\": \"N/A - training experiment\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 13.88, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_038_dual_critic_walker_s2\", \"model_name\": \"DreamerV3 + Dual Critic (wide)\", \"pid\": \"175633\", \"seed\": 2, \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-21T12:18:34.859Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 49982.0}}, \"exp_037_wide_critic_cheetah\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A\", \"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"bash -c \\\"...wide_critic cheetah...\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Cheetah Run\", \"eval_data\": \"N/A - training experiment\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 7.46, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_037_wide_critic_cheetah.log\", \"model_name\": \"DreamerV3 + Wide Single Critic\", \"pid\": \"14487\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-21T12:18:32.619Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 26839.7}}, \"exp_036_dual_critic_pickcube\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --seed 0 --steps 200000 --compile False --device cuda:0 --logdir ./logdir/exp_036_dual_critic_pickcube\\\"\", \"data_count\": 200000, \"data_path\": \"ManiSkill PickCube-v1\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 11.03, \"gpu_id\": 0, \"hyperparams\": {\"dual_critic\": true, \"gate_enabled\": true, \"gate_fixed_dt\": 2, \"gate_subsample_max_dt\": 2, \"imag_horizon\": 8, \"tcn_sigma\": 0.0}, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_036_dual_critic_pickcube.log\", \"model_name\": \"DreamerV3 + Dual Critic\", \"pid\": \"2476\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-21T08:43:44.544357+00:00\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 39706.7}}, \"exp_035_narrow_dual_critic_walker\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --narrow_dual_critic True --logdir logdir/exp_035_narrow_dual_critic_walker\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 8.31, \"gpu_id\": 1, \"hyperparams\": {\"critic_hidden\": 256, \"critic_layers\": 2, \"critic_params_each\": 525000, \"critic_params_total\": 1050000, \"gate_enabled\": true, \"gate_fixed_dt\": 2, \"gate_subsample_max_dt\": 2, \"imag_horizon\": 8, \"narrow_dual_critic\": true}, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_035_narrow_dual_critic_walker.log\", \"model_name\": \"DreamerV3 + Narrow Dual Critic (2×256 hidden, 1.05M total)\", \"pid\": \"162900\", \"seed\": 0, \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-21T07:56:05.926445+00:00\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 29900.2}}, \"exp_034\": {\"spec\": {\"command\": \"python train.py --configs dmc_cheetah_run --dual_critic True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --steps 210000 --seed 0\", \"data_count\": 0, \"data_path\": \"dmc_cheetah_run\", \"model_name\": \"dreamerv3\", \"seed\": 0, \"server\": \"bjb1-45299\"}}, \"exp_034_dual_critic_cheetah\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --logdir logdir/exp_034_dual_critic_cheetah\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Cheetah Run (dm_control built-in)\", \"gpu\": [\"cuda:1\"], \"gpu_id\": 1, \"hyperparams\": {\"dual_critic\": true, \"gate_enabled\": true, \"gate_fixed_dt\": 2, \"gate_subsample_max_dt\": 2, \"imag_horizon\": 8, \"tcn_sigma\": 0.0}, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_034_dual_critic_cheetah.log\", \"model_name\": \"DreamerV3 + Dual Critic\", \"pid\": \"993925\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-21T05:51:51.325323+00:00\", \"submitted_via\": \"submit_training_job\"}}, \"exp_033_wide_critic_walker\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --wide_critic True --logdir logdir/exp_033_wide_critic_walker\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 8.25, \"gpu_id\": 0, \"hyperparams\": {\"critic_hidden\": 1024, \"critic_layers\": 2, \"critic_params\": 2886911, \"dual_critic\": false, \"gate_enabled\": true, \"gate_fixed_dt\": 2, \"gate_subsample_max_dt\": 2, \"imag_horizon\": 8, \"wide_critic\": true}, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_033_wide_critic_walker.log\", \"model_name\": \"DreamerV3 + Wide Critic (1024 hidden, 2.89M params, 2.44× normal)\", \"pid\": \"151860\", \"seed\": 0, \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-21T03:52:59.702597+00:00\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 29715.5}}, \"exp_031b_tcn_pickcube_s0_sigma05\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.5 --seed 0 --steps 200000 --compile False --device cuda:0 --logdir ./logdir/exp_031b_tcn_pickcube_s0_sigma05\\\"\", \"data_count\": 200000, \"data_path\": \"ManiSkill PickCube-v1\", \"gpu\": [\"cuda:0\"], \"gpu_id\": 0, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_031b_tcn_pickcube_s0_sigma05.log\", \"model_name\": \"DreamerV3 + TCN σ=0.5\", \"pid\": \"968495\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-20T22:33:14.695383+00:00\", \"submitted_via\": \"submit_training_job\"}}, \"exp_032_dual_critic_walker\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_032_dual_critic_walker\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --logdir logdir/exp_032_dual_critic_walker\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"gpu\": [\"cuda:1\"], \"gpu_id\": 1, \"hyperparams\": {\"dual_critic\": true, \"gate_enabled\": true, \"gate_fixed_dt\": 2, \"gate_subsample_max_dt\": 2, \"imag_horizon\": 8, \"tcn_sigma\": 0.0}, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_032_dual_critic_walker.log\", \"model_name\": \"DreamerV3 + Dual Critic (min of two independent critics)\", \"pid\": \"124556\", \"seed\": 0, \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-20T23:19:57.690519+00:00\", \"submitted_via\": \"submit_training_job\"}}, \"exp_032b_dual_critic_walker_s1\": {\"spec\": {\"data_count\": 210000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"hyperparams\": {\"dual_critic\": true, \"gate_enabled\": true, \"gate_fixed_dt\": 2, \"gate_subsample_max_dt\": 2, \"imag_horizon\": 8, \"tcn_sigma\": 0}, \"model_name\": \"DreamerV3 + Dual Critic (min of two independent critics)\", \"seed\": 1}}, \"exp_029d_tcn_walker_s3_sigma02\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_029d_tcn_walker_s3_sigma02\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 3 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --logdir logdir/exp_029d_tcn_walker_s3_sigma02\\\"\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_029d_tcn_walker_s3_sigma02.log\", \"pid\": \"109826\", \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-20T19:33:48.032Z\", \"submitted_via\": \"submit_training_job\"}}, \"exp_031_tcn_pickcube_s0_sigma02\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"none(train_from_scratch)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --seed 0 --steps 200000 --compile False --device cuda:0 --logdir ./logdir/exp_031_tcn_pickcube_s0_sigma02\\\"\", \"data_count\": \"200000(online)\", \"data_path\": \"maniskill_PickCube-v1\", \"eval_data\": \"maniskill_PickCube-v1(online_eval)\", \"gpu\": \"cuda:1\", \"gpu_hours\": 11.17, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_031_tcn_pickcube_s0_sigma02.log\", \"model_name\": \"dreamerv3\", \"pid\": \"908459\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-20T12:42:41.707Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 40206.6}}, \"exp_029b_tcn_walker_s2_sigma02\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_029b_tcn_walker_s2_sigma02\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 2 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --logdir logdir/exp_029b_tcn_walker_s2_sigma02\\\"\", \"gpu\": [\"cuda:1\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_029b_tcn_walker_s2_sigma02.log\", \"pid\": \"75543\", \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-20T16:56:24.781Z\", \"submitted_via\": \"submit_training_job\"}}, \"exp_030c_tcn_cheetah_s0_sigma10\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_030c_tcn_cheetah_s0_sigma10\", \"command\": \"dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 0 --tcn_sigma 1.0\", \"data_count\": 210000, \"data_path\": \"dmc_cheetah_run\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_030c_tcn_cheetah_s0_sigma10.log\", \"model_name\": \"dreamerv3\", \"pid\": \"920968\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-20T16:49:48.464Z\", \"submitted_via\": \"submit_training_job\"}}, \"exp_029c_tcn_walker_s0_sigma01\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_029c_tcn_walker_s0_sigma01/latest.pt\", \"checkpoint_source\": \"from_scratch\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.1 --logdir logdir/exp_029c_tcn_walker_s0_sigma01\\\"\", \"data_count\": 210000, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_029c_tcn_walker_s0_sigma01.log\", \"model_name\": \"dreamer\", \"pid\": \"59395\", \"seed\": 0, \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-20T11:42:56.447Z\", \"submitted_via\": \"submit_training_job\"}}, \"exp_029a_tcn_walker_s1_sigma02\": {\"spec\": {\"checkpoint_path\": \"/root/runs/event-gated-adaptive-horizon/exp_029a_tcn_walker_s1_sigma02/latest.pt\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --logdir ~/runs/event-gated-adaptive-horizon/exp_029a_tcn_walker_s1_sigma02\", \"data_count\": 210000, \"data_path\": \"dmc_walker_walk\", \"gpu\": \"cuda:1\", \"log_path\": \"/root/runs/event-gated-adaptive-horizon/exp_029a_tcn_walker_s1_sigma02.log\", \"model_name\": \"dreamerv3\", \"pid\": \"50924\", \"seed\": 1, \"server\": \"bjb1-40020\"}}, \"exp_030b_tcn_cheetah_s0_sigma05\": {\"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_030b_tcn_cheetah_s0_sigma05/latest.pt\", \"gpu\": \"cuda:0\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_030b_tcn_cheetah_s0_sigma05/metrics.jsonl\"}}, \"exp_027_tcn_walker_s1\": {\"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_027_tcn_walker_s1/\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s1.log\"}}, \"exp_027_tcn_walker_s0_sigma02\": {\"spec\": {\"checkpoint_path\": \"/root/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0_sigma02/latest.pt\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --logdir logdir/exp_027_tcn_walker_s0_sigma02\", \"data_count\": 215000, \"data_path\": \"dmc_walker_walk\", \"gpu\": \"cuda:0\", \"log_path\": \"/root/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0_sigma02.log\", \"model_name\": \"dreamerv3\", \"seed\": 0, \"server\": \"bjb1-40020\"}}, \"exp_030a_tcn_cheetah_s0_sigma02\": {\"spec\": {\"checkpoint_path\": \"logdir/exp_030a_tcn_cheetah_s0_sigma02/\", \"checkpoint_source\": \"from_scratch\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_enabled True --tcn_sigma 0.2 --logdir logdir/exp_030a_tcn_cheetah_s0_sigma02\", \"data_count\": \"210000 env steps\", \"data_path\": \"dmc_cheetah_run\", \"eval_data\": \"dmc_cheetah_run\", \"gpu\": \"cuda:0\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_030a_tcn_cheetah_s0_sigma02.log\", \"model_name\": \"dreamerv3_tcn_sigma02_cheetah\", \"seed\": 0, \"server\": \"bjb1-45299\"}}, \"exp_027_tcn_walker_s0\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.5 --logdir logdir/exp_027_tcn_walker_s0\\\"\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 3.18, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0.log\", \"pid\": \"888715\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-20T06:13:35.505Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 11433.5}}, \"exp_028_rave_walker_s0_ceil15\": {\"spec\": {\"checkpoint_path\": \"~/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0_ceil15/\", \"checkpoint_source\": \"N/A (trained from scratch, hyperparameter variant of exp_028_rave_walker_s0)\", \"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --rave_enabled True --rave_ceiling 1.5 --rave_ema_decay 0.99 --logdir ~/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0_ceil15'\", \"data_count\": \"210000 env steps\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:1\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0_ceil15.log\", \"model_name\": \"dreamerv3_rave_ceil15\", \"note\": \"CUDA_VISIBLE_DEVICES=1 set by submit_training_job, device=cuda:0 within process\", \"pid\": \"38372\", \"seed\": 0, \"server\": \"bjb1-40020\", \"tmux_session\": \"exp_028_rave_walker_s0_ceil15\"}}, \"exp_028_rave_walker_s0\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"N/A (trained from scratch, derives from SGS failure line)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 105000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --rave_ceiling 2.0 --logdir logdir/exp_028_rave_walker_s0\\\"\", \"data_count\": \"105000 env steps (52.5K agent steps, action_repeat=2)\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 3.33, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0.log\", \"model_name\": \"dreamerv3_rave_ceil20\", \"pid\": \"879636\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-20T02:54:26.022Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 12005.7}}, \"exp_025_obs_sgs_walker_s2\": {\"spec\": {\"checkpoint_path\": \"logdir/exp_025_obs_sgs_walker_s2/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 2 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_025_obs_sgs_walker_s2\", \"data_count\": \"210000 env steps (105K agent steps)\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:1\"], \"log_path\": \"logdir/exp_025_obs_sgs_walker_s2/train.log\", \"model_name\": \"dreamerv3_obs_decoder_sgs\", \"pid\": \"7989\", \"seed\": 2, \"server\": \"bjb1-40020\", \"tmux_session\": \"exp_025_s2\"}}, \"exp_026_obs_sgs_cheetah_s1\": {\"spec\": {\"checkpoint_path\": \"logdir/exp_026_obs_sgs_cheetah_s1/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 105000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_026_obs_sgs_cheetah_s1\", \"data_count\": \"105000 env steps\", \"data_path\": \"dmc_cheetah_run\", \"eval_data\": \"dmc_cheetah_run (online eval during training)\", \"gpu\": [\"cuda:1\"], \"log_path\": \"logdir/exp_026_obs_sgs_cheetah_s1/train.log\", \"model_name\": \"dreamerv3_obs_decoder_sgs_cheetah\", \"pid\": \"16346\", \"seed\": 1, \"server\": \"bjb1-40020\", \"tmux_session\": \"exp_026_s1\"}}, \"exp_026_obs_sgs_cheetah_s0\": {\"spec\": {\"checkpoint_path\": \"logdir/exp_026_obs_sgs_cheetah_s0/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 105000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_026_obs_sgs_cheetah_s0\", \"data_count\": \"105000 env steps\", \"data_path\": \"dmc_cheetah_run\", \"eval_data\": \"dmc_cheetah_run (online eval during training)\", \"gpu\": [\"cuda:0\"], \"log_path\": \"logdir/exp_026_obs_sgs_cheetah_s0/train.log\", \"model_name\": \"dreamerv3_obs_decoder_sgs_cheetah\", \"pid\": \"16208\", \"seed\": 0, \"server\": \"bjb1-40020\", \"tmux_session\": \"exp_026_s0\"}}, \"exp_025_obs_sgs_walker_s4\": {\"spec\": {\"checkpoint_path\": \"logdir/exp_025_obs_sgs_walker_s4/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 4 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_025_obs_sgs_walker_s4\", \"data_count\": \"210000 env steps (105K agent steps)\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:1\"], \"log_path\": \"logdir/exp_025_obs_sgs_walker_s4/train.log\", \"model_name\": \"dreamerv3_obs_decoder_sgs\", \"pid\": \"851593\", \"seed\": 4, \"server\": \"bjb1-45299\", \"tmux_session\": \"exp_025_s4\"}}, \"exp_025_obs_sgs_walker_s3\": {\"spec\": {\"checkpoint_path\": \"logdir/exp_025_obs_sgs_walker_s3/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 3 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_025_obs_sgs_walker_s3\", \"data_count\": \"210000 env steps (105K agent steps)\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:0\"], \"log_path\": \"logdir/exp_025_obs_sgs_walker_s3/train.log\", \"model_name\": \"dreamerv3_obs_decoder_sgs\", \"pid\": \"847597\", \"seed\": 3, \"server\": \"bjb1-45299\", \"tmux_session\": \"exp_025_s3\"}}, \"exp_025_obs_sgs_walker_s1\": {\"spec\": {\"checkpoint_path\": \"logdir/exp_025_obs_sgs_walker_s1/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_025_obs_sgs_walker_s1\", \"data_count\": \"210000 env steps (105K agent steps)\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:0\"], \"log_path\": \"logdir/exp_025_obs_sgs_walker_s1/train.log\", \"model_name\": \"dreamerv3_obs_decoder_sgs\", \"pid\": \"7833\", \"seed\": 1, \"server\": \"bjb1-40020\", \"tmux_session\": \"exp_025_s1\"}}, \"exp_001_baseline_s4_extended\": {\"spec\": {\"checkpoint_path\": \"logdir/exp_001_baseline_s4/\", \"checkpoint_source\": \"logdir/exp_001_baseline_s4/latest.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 505000 --seed 4 --device cuda:0 --compile False --gate_enabled False --logdir logdir/exp_001_baseline_s4\", \"data_count\": \"505000 env steps\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": \"cuda:1\", \"log_path\": \"logdir/exp_001_baseline_s4/train_extended.log\", \"model_name\": \"dreamerv3_baseline\", \"resumed_from_step\": 112000, \"seed\": 4, \"server\": \"bjb1-45299\", \"target_steps\": 505000, \"tmux_session\": \"exp_s4_ext\"}}, \"exp_001_baseline_s3_extended\": {\"spec\": {\"checkpoint_path\": \"logdir/exp_001_baseline_s3/\", \"checkpoint_source\": \"logdir/exp_001_baseline_s3/latest.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 505000 --seed 3 --device cuda:0 --compile False --gate_enabled False --logdir logdir/exp_001_baseline_s3\", \"data_count\": \"505000 env steps\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": \"cuda:0\", \"log_path\": \"logdir/exp_001_baseline_s3/train_extended.log\", \"model_name\": \"dreamerv3_baseline\", \"resumed_from_step\": 120000, \"seed\": 3, \"server\": \"bjb1-45299\", \"target_steps\": 505000, \"tmux_session\": \"exp_s3_ext\"}}, \"exp_001_baseline_s2_extended\": {\"spec\": {\"checkpoint_path\": \"logdir/exp_001_baseline_s2/latest.pt\", \"checkpoint_source\": \"logdir/exp_001_baseline_s2/latest.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 505000 --seed 2 --device cuda:0 --compile False --gate_enabled False --logdir logdir/exp_001_baseline_s2\", \"data_count\": 0, \"data_path\": \"logdir/exp_001_baseline_s2\", \"eval_data\": \"dmc_walker_walk (online eval)\", \"gpu\": \"cuda:1\", \"log_path\": \"logdir/exp_001_baseline_s2/train_extended.log\", \"model_name\": \"dreamerv3\", \"resumed_from_step\": 112000, \"seed\": 2, \"server\": \"bjb1-45299\", \"target_steps\": 505000, \"tmux_session\": \"exp_s2_ext\"}}, \"exp_023_cheetah_baseline_s4_extended\": {\"spec\": {\"checkpoint_path\": \"logdir/exp_023_cheetah_baseline_s4/\", \"checkpoint_source\": \"logdir/exp_023_cheetah_baseline_s4/latest.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 300000 --seed 4 --device cuda:0 --compile False --gate_enabled False --checkpoint_every 10000 --logdir logdir/exp_023_cheetah_baseline_s4\", \"data_count\": \"300000 env steps\", \"data_path\": \"dmc_cheetah_run\", \"eval_data\": \"dmc_cheetah_run (online eval during training)\", \"gpu\": \"cuda:0\", \"log_path\": \"logdir/exp_023_cheetah_baseline_s4/train_extended.log\", \"model_name\": \"dreamerv3_baseline\", \"resumed_from_step\": 212000, \"seed\": 4, \"server\": \"bjb1-45299\", \"target_steps\": 300000, \"tmux_session\": \"exp_023_s4_ext\"}}, \"exp_001_baseline_s4\": {\"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s4\", \"checkpoint_source\": \"N/A\", \"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 105000 --seed 4 --device cuda:0 --compile False --gate_enabled False --logdir logdir/exp_001_baseline_s4\", \"data_count\": 0, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s4/metrics.jsonl\", \"model_name\": \"dreamerv3\", \"seed\": 4, \"server\": \"bjb1-45299\"}}, \"exp_023_cheetah_baseline_s4\": {\"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_023_cheetah_baseline_s4\", \"checkpoint_source\": \"N/A (train from scratch)\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 200000 --seed 4 --device cuda:0 --compile False --gate_enabled False --checkpoint_every 10000 --logdir logdir/exp_023_cheetah_baseline_s4\", \"data_count\": \"200K env steps\", \"data_path\": \"dmc_cheetah_run (online RL)\", \"eval_data\": \"dmc_cheetah_run eval episodes\", \"gpu\": \"cuda:0\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_023_cheetah_baseline_s4/metrics.jsonl\", \"model_name\": \"DreamerV3 (default)\", \"pid\": 774033, \"seed\": 4, \"server\": \"bjb1-45299\"}}, \"exp_023_cheetah_baseline_s3\": {\"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_023_cheetah_baseline_s3\", \"checkpoint_source\": \"N/A\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 200000 --seed 3 --device cuda:0 --compile False --gate_enabled False --checkpoint_every 10000 --logdir logdir/exp_023_cheetah_baseline_s3\", \"data_count\": 0, \"data_path\": \"dmc_cheetah_run\", \"eval_data\": \"N/A\", \"gpu\": [\"cuda:1\"], \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_023_cheetah_baseline_s3/metrics.jsonl\", \"model_name\": \"dreamerv3\", \"pid\": \"768897\", \"seed\": 3, \"server\": \"bjb1-45299\"}}, \"exp_001_baseline_s3\": {\"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s3\", \"checkpoint_source\": \"N/A (train from scratch)\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 105000 --seed 3 --device cuda:0 --compile False --gate_enabled False --logdir logdir/exp_001_baseline_s3\", \"data_count\": \"105K env steps\", \"data_path\": \"dmc_walker_walk (online RL)\", \"eval_data\": \"dmc_walker_walk eval episodes\", \"gpu\": \"cuda:1\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s3/metrics.jsonl\", \"model_name\": \"DreamerV3 (default)\", \"pid\": 774106, \"seed\": 3, \"server\": \"bjb1-45299\"}}, \"exp_023_cheetah_baseline_s2\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_023_cheetah_baseline_s2\", \"checkpoint_source\": \"N/A\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 200000 --seed 2 --device cuda:0 --compile False --gate_enabled False --checkpoint_every 10000 --logdir logdir/exp_023_cheetah_baseline_s2\\\"\", \"data_count\": 0, \"data_path\": \"dmc_cheetah_run\", \"eval_data\": \"N/A\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 8.13, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_023_cheetah_baseline_s2/metrics.jsonl\", \"model_name\": \"dreamerv3\", \"pid\": \"753786\", \"seed\": 2, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-18T16:05:57.478Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 29278.4}}, \"exp_008f_s4\": {\"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008f_no_dt_emb_s4\", \"checkpoint_source\": \"N/A\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008f_no_dt_emb_s4 --steps 105000 --seed 4 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A\", \"gpu\": [\"cuda:0\"], \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008f_no_dt_emb_s4/metrics.jsonl\", \"model_name\": \"DreamerV3+FixedDt2_NoDtEmbed_Subsample_H8\", \"seed\": 4, \"server\": \"bjb1-45299\"}}, \"exp_009c_s3\": {\"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009c_no_dt_emb_s3\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009c_no_dt_emb_s3/metrics.jsonl\"}}, \"exp_001_baseline_s2\": {\"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s2\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s2/metrics.jsonl\"}}, \"exp_008f_s2\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"N/A\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008f_no_dt_emb_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"data_count\": 0, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 2.58, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008f_s2.log\", \"model_name\": \"dreamerv3\", \"pid\": \"754063\", \"seed\": 2, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-18T16:06:00.248Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 9305.1}}, \"exp_008a_cheetah_unexposed_s1\": {\"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_cheetah_unexposed_s1\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_cheetah_unexposed_s1/metrics.jsonl\"}}, \"exp_008a_cheetah_unexposed_s0\": {\"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_cheetah_unexposed_s0\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_cheetah_unexposed_s0/metrics.jsonl\"}}, \"exp_009c_s2\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"N/A\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009c_no_dt_emb_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"data_count\": 0, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 1.1, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009c_s2.log\", \"model_name\": \"dreamerv3\", \"pid\": \"754639\", \"seed\": 2, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-18T16:06:05.850Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 3959.5}}, \"exp_008e_v3_s4\": {\"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_s4/latest.pt\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008e_v3_s4.log\"}}, \"exp_008e_v3_s3\": {\"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_s3/latest.pt\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008e_v3_s3.log\"}}, \"exp_008a_unexposed_s1\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"train_from_scratch\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008a_unexposed_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 1 --checkpoint_every 25000\", \"data_count\": 0, \"data_path\": \"dmc_walker_walk (online RL)\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 3.03, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008a_unexposed_s1.log\", \"model_name\": \"DreamerV3+FixedDt2_NoSubsample (unexposed trained dt_emb, H=15)\", \"pid\": \"724312\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-18T05:15:06.654Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 10896.1}}, \"exp_008a_unexposed_s2\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"train_from_scratch\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008a_unexposed_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 1 --checkpoint_every 25000\", \"data_count\": 0, \"data_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 2.84, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008a_unexposed_s2.log\", \"model_name\": \"DreamerV3+FixedDt2_NoSubsample (unexposed trained dt_emb, H=15)\", \"pid\": \"724965\", \"seed\": 2, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-18T05:19:26.303Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 10239.8}}, \"exp_008d_civo_trigger_s4\": {\"spec\": {\"checkpoint_source\": \"train_from_scratch\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --gate_subsample_min_dt 1 --imag_horizon 8 --seed 4 --steps 105000 --checkpoint_every 25000 --compile False --device cuda:0 --logdir ./logdir/exp_008d_civo_trigger_s4\", \"data_count\": 0, \"data_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon\", \"eval_data\": \"dmc_walker_walk_online\", \"gpu\": \"cuda:0\", \"model_name\": \"DreamerV3-walker-civo-trigger\", \"pid\": \"715124\", \"seed\": 4, \"server\": \"bjb1-45299\"}}, \"exp_008a_untrained_s1\": {}, \"exp_008a_untrained_s2\": {}, \"exp_010b_cheetah_civo_trigger_s0\": {\"spec\": {\"checkpoint_source\": \"N/A (training from scratch)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_010b_cheetah_civo_trigger_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000\\\"\", \"data_count\": 0, \"data_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon\", \"eval_data\": \"dmc_cheetah_run (online RL)\", \"gpu\": \"cuda:1\", \"model_name\": \"DreamerV3-cheetah-civo-trigger\", \"pid\": \"715412\", \"seed\": 0, \"server\": \"bjb1-45299\"}}, \"exp_024b_cheetah_no_dt_emb_s0\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_024b_cheetah_no_dt_emb_s0/latest.pt\", \"checkpoint_source\": \"N/A-training-from-scratch\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_024b_cheetah_no_dt_emb_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --checkpoint_every 25000\\\"\", \"data_count\": 0, \"data_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon\", \"eval_data\": \"dmc_cheetah_run-online-eval\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 3.13, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_024b_cheetah_no_dt_emb_s0.log\", \"model_name\": \"DreamerV3-cheetah-no-dt-emb\", \"pid\": \"705742\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-17T22:52:15.808Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 11279.4}}, \"exp_024b_cheetah_no_dt_emb_s1\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_024b_cheetah_no_dt_emb_s1/latest.pt\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_024b_cheetah_no_dt_emb_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --checkpoint_every 25000\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 3.06, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_024b_cheetah_no_dt_emb_s1.log\", \"pid\": \"706158\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-17T22:52:30.631Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 11026.4}}, \"exp_024_cheetah_no_dt_emb_s0\": {\"spec\": {\"checkpoint_source\": \"N/A (training from scratch)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_024_cheetah_no_dt_emb_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --checkpoint_every 25000\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_cheetah_run (online RL)\", \"eval_data\": \"N/A (online RL)\", \"model_name\": \"DreamerV3-no-dt-emb\", \"seed\": 0, \"server\": \"bjb1-45299\"}}, \"exp_021_full_sgs_cheetah_s1\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_021_full_sgs_cheetah_s1/checkpoint.pt\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_021_full_sgs_cheetah_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --full_sgs True --checkpoint_every 25000\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 3.32, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_021_full_sgs_cheetah_s1.log\", \"pid\": \"696201\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-17T19:30:02.581Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 11952.4}}, \"exp_023a_cheetah_baseline_s0\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_023a_cheetah_baseline_s0/checkpoint.pt\", \"command\": \"bash -c \\\"cd /root/autodl-tmp/event-gated-adaptive-horizon && bash scripts/exp_023a_cheetah_baseline_s0.sh\\\"\", \"data_count\": \"N/A (online RL)\", \"data_path\": \"dmc_cheetah_run\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 5.66, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_023a_cheetah_baseline_s0.log\", \"model_name\": \"DreamerV3\", \"pid\": \"683708\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-17T14:54:17.553Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 20387.3}}, \"exp_010b_cheetah_civo_trigger\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010b_cheetah_civo_trigger/latest.pt\", \"checkpoint_source\": \"N/A (training from scratch, parent is baseline reference)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_010b_cheetah_civo_trigger --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"data_count\": 105000, \"data_path\": \"dm_control cheetah_run (online RL)\", \"eval_data\": \"N/A (online RL, not eval experiment)\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 3.18, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_010b_cheetah_civo_trigger.log\", \"model_name\": \"DreamerV3+dt_emb(trained)+subsample+H8\", \"pid\": \"585826\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-16T13:05:10.473Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 11450.0}}, \"exp_023b_cheetah_baseline_s1\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_023b_cheetah_baseline_s1/checkpoint.pt\", \"command\": \"bash -c \\\"cd /root/autodl-tmp/event-gated-adaptive-horizon && bash scripts/exp_023b_cheetah_baseline_s1.sh\\\"\", \"data_count\": \"N/A (online RL)\", \"data_path\": \"dmc_cheetah_run\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 5.5, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_023b_cheetah_baseline_s1.log\", \"model_name\": \"DreamerV3\", \"pid\": \"680126\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-17T13:59:45.409Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 19807.2}}, \"exp_019b_pickcube_civo_trigger\": {\"spec\": {\"checkpoint_source\": \"N/A (training from scratch)\", \"command\": \"cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_ID=0 bash scripts/exp_019b_pickcube_civo_trigger.sh\", \"data_count\": \"online\", \"data_path\": \"maniskill_PickCube-v1 (state-based, online RL)\", \"eval_data\": \"N/A (online RL, not eval)\", \"gpu_id\": \"cuda:0\", \"model_name\": \"DreamerV3 + trained dt_emb + gate (maniskill_state config)\", \"pid\": 649577, \"seed\": 1, \"server\": \"bjb1-45299\"}}, \"exp_022b_no_curriculum\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"unset CUDA_VISIBLE_DEVICES && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_EGL_DEVICE_ID=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs dmc_proprio --task dmc_walker_walk --steps 105000 --seed 0 --device cuda:1 --compile False --checkpoint_every 10000 --gate_enabled True --gate_dt_embed_dim 32 --dt_emb_freeze True --gate_subsample_min_dt 1 --gate_subsample_max_dt 2 --gate_curriculum_phase1 0 --gate_curriculum_phase2 0 --imag_horizon 8 --logdir ./logdir/exp_022b_no_curriculum\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 3.16, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_022b_no_curriculum.log\", \"pid\": \"670554\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-17T10:51:56.898Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 11366.5}}, \"exp_022_untrained_dt_emb_learned_gate\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_022_untrained_dt_emb_learned_gate/checkpoint.ckpt\", \"checkpoint_source\": \"N/A (training from scratch)\", \"command\": \"bash -c \\\"unset CUDA_VISIBLE_DEVICES && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_EGL_DEVICE_ID=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs dmc_proprio --task dmc_walker_walk --steps 105000 --seed 0 --device cuda:1 --compile False --checkpoint_every 10000 --gate_enabled True --gate_dt_embed_dim 32 --dt_emb_freeze True --gate_subsample_min_dt 1 --gate_subsample_max_dt 2 --imag_horizon 8 --logdir ./logdir/exp_022_untrained_dt_emb_learned_gate\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk (online RL, proprio obs)\", \"eval_data\": \"N/A (online RL, not eval)\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 3.03, \"gpu_id\": \"cuda:1\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_022_untrained_dt_emb_learned_gate.log\", \"model_name\": \"DreamerV3 + frozen dt_emb (d=32) + learned gate (Gumbel-softmax)\", \"pid\": 661595, \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-17T07:47:20.391Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 10901.2}}, \"exp_019a_v2_pickcube_baseline\": {\"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_019a_v2_pickcube_baseline/checkpoint.ckpt\", \"checkpoint_source\": \"auto-resume from logdir\", \"command\": \"bash -c \\\"unset CUDA_VISIBLE_DEVICES && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --gate_enabled False --seed 1 --steps 200000 --compile False --device cuda:1 --logdir ./logdir/exp_019a_v2_pickcube_baseline\\\"\", \"data_count\": 200000, \"data_path\": \"ManiSkill3 PickCube-v1 (online RL)\", \"eval_data\": \"N/A - training experiment\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_019a_v2_pickcube_baseline\", \"model_name\": \"DreamerV3-S\", \"seed\": 1, \"server\": \"bjb1-45299\"}}, \"exp_007_fixed_dt4\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/fixed_dt4_v2_s1 --steps 150000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 4\\\"\", \"data_count\": 150000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/fixed_dt4_v2_s1\", \"model_name\": \"DreamerV3+FixedDt4 (gate_fixed_dt=4, no learned gate, init_dt fix applied)\", \"pid\": \"90354\", \"seed\": 1, \"server\": \"bjb1-45299\"}}, \"exp_008c_no_subsample_dt2_h8\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008c_fixed_dt2_no_subsample_h8/checkpoint.ckpt\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008c_fixed_dt2_no_subsample_h8 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 1 --imag_horizon 8\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 2.53, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008c_fixed_dt2_no_subsample_h8\", \"model_name\": \"DreamerV3+FixedDt2_NoSubsample_H8 (gate_fixed_dt=2, gate_subsample_max_dt=1, imag_horizon=8)\", \"pid\": \"107021\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T01:37:47.540Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 9119.3}}, \"exp_003_event_gated_v2\": {\"spec\": {\"checkpoint_source\": \"logdir/event_gated_s1_v2/latest.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/event_gated_s1_v2 --steps 500000 --seed 1 --compile False --device cuda:0 --gate_enabled True\", \"data_count\": 500000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"gpu_id\": 1, \"hypothesis\": \"Subsample curriculum prevents early destabilization while event gate learns meaningful variable-rate stepping\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/event_gated_s1_v2\", \"model_name\": \"DreamerV3 + Event-Gated Variable-Rate RSSM v2 (final fix: env step sync + threshold 25K/75K)\", \"pid\": 27009, \"seed\": 1, \"server\": \"autodl-rtx6000\"}}, \"exp_004_event_gated_v3\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A - killed due to gate_loss explosion bug\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/event_gated_v4_s1 --steps 500000 --seed 1 --compile False --device cuda:0 --gate_enabled True\", \"data_count\": 500000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 5.19, \"gpu_id\": 1, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/event_gated_v4_s1\", \"model_name\": \"DreamerV3 + Event-Gated Variable-Rate RSSM v3 (dt clipping + logits masking + dt alignment fix)\", \"pid\": 36645, \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-13T10:12:04.157Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 18682.2}}, \"exp_005_event_gated_v4\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/event_gated_v5_s1 --steps 500000 --seed 1 --compile False --device cuda:0 --gate_enabled True\", \"data_count\": 500000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 6.12, \"hypothesis\": \"修复 gate_target/masking 维度不匹配 + effective_max_dt 单一来源架构 + 全量审计后，event gate return >= 80% baseline\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_005_event_gated_v4.log\", \"model_name\": \"DreamerV3+EventGate_v4\", \"pid\": \"51721\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-13T16:08:11.913Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 22029.4}}, \"exp_008d_civo_trigger_s3\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"fresh_training (no checkpoint, new logdir)\", \"command\": \"bash -c \\\"unset CUDA_VISIBLE_DEVICES && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --gate_subsample_min_dt 1 --imag_horizon 8 --seed 3 --steps 105000 --checkpoint_every 25000 --compile False --device cuda:0 --logdir ./logdir/exp_008d_civo_trigger_s3\\\"\", \"data_count\": 105000, \"data_path\": \"DMC Walker Walk (online RL)\", \"eval_data\": \"N/A - training experiment\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 2.97, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008d_civo_trigger_s3.log\", \"model_name\": \"DreamerV3-S\", \"pid\": \"635744\", \"seed\": 3, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-17T00:25:59.245Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 10706.8}}, \"exp_018v2_full_sgs_walker_s1\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"N/A (training from scratch, parent is predecessor not checkpoint source)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --full_sgs True --seed 1 --steps 105000 --checkpoint_every 25000 --compile False --device cuda:0 --logdir ./logdir/exp_018v2_full_sgs_walker_s1\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk (online RL, no static dataset)\", \"eval_data\": \"dmc_walker_walk eval episodes (online)\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 3.49, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_018v2_full_sgs_walker_s1.log\", \"model_name\": \"DreamerV3\", \"pid\": \"589564\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-16T13:55:10.231Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 12574.2}}, \"exp_008d_subsample_on_h8\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008d_subsample_on_h8/checkpoint.ckpt\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008d_subsample_on_h8 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 2.48, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008d_subsample_on_h8\", \"model_name\": \"DreamerV3+FixedDt2_Subsample_H8 (gate_fixed_dt=2, gate_subsample_max_dt=2, imag_horizon=8)\", \"pid\": \"109519\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T02:21:59.852Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 8932.6}}, \"exp_018_full_sgs_s2\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --full_sgs True --seed 2 --steps 105000 --checkpoint_every 25000 --compile False --device cuda:0 --logdir ./logdir/exp_018_full_sgs_s2\\\"\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 4.04, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_018_full_sgs_s2.log\", \"pid\": \"612876\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-16T19:45:40.838Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 14528.6}}, \"exp_009b_008d_walker_s2\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009b_008d_walker_s2 --steps 105000 --seed 2 --compile False --device cuda:1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"model_name\": \"DreamerV3+FixedDt2_Subsample_H8 (gate_fixed_dt=2, gate_subsample_max_dt=2, imag_horizon=8, trained dt_embed)\", \"seed\": 2, \"server\": \"bjb1-45299\"}}, \"exp_008f_no_dt_embed_subsample_on_h8\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"N/A - training from scratch, parent is for genealogy only\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008f_no_dt_embed_subsample_on_h8 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A - training experiment, not eval\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 4.68, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008f_no_dt_embed_subsample_on_h8\", \"model_name\": \"DreamerV3+FixedDt2_NoDtEmbed_Subsample_H8 (gate_fixed_dt=2, gate_subsample_max_dt=2, imag_horizon=8, gate_dt_embed_dim=0)\", \"pid\": \"127761\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T04:51:55.020Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 16858.4}}, \"exp_016d_sgs_walker_s1\": {\"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_016d_sgs_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"model_name\": \"dreamerv3-sgs\", \"note\": \"第5次启动。两项修复生效：MUJOCO_EGL_DEVICE_ID=1 + logger.video注释。旧PID 526153已自行退出。\", \"pid\": 526939, \"seed\": 1, \"server\": \"bjb1-45299\"}}, \"exp_001_baseline\": {\"spec\": {\"command\": \"python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/baseline_s1 --steps 500000 --seed 1 --compile False --device cuda:0\", \"data_count\": 500000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"gpu\": [\"cuda:0\"], \"gpu_id\": 0, \"hypothesis\": \"DreamerV3 baseline on DMC Walker Walk for comparison with event-gated model\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/baseline_s1\", \"model_name\": \"DreamerV3 (original, gate_enabled=false)\", \"pid\": 9409, \"seed\": 1, \"server\": \"bjb1-45299\"}}, \"exp_008d_civo_trigger_s2\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"fresh_training (no checkpoint loaded)\", \"command\": \"source /root/miniconda3/bin/activate && cd /root/event-gated-adaptive-horizon && python train.py --configs dmc_vision --task dmc_walker_walk --logdir ./logdir/008d_civo_trigger_s2 --seed 1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --gate_subsample_min_dt 1 --imag_horizon 8 --steps 120000\", \"data_count\": 120000, \"data_path\": \"DMC Walker Walk (online RL)\", \"eval_data\": \"N/A - training experiment, not eval\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 1.57, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008d_civo_trigger_s2.log\", \"model_name\": \"DreamerV3-S\", \"pid\": \"628477\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-16T22:49:55.859Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 5654.3}}, \"exp_008f_s3_no_dt_embed_walker\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008f_s3_no_dt_embed_walker --steps 105000 --seed 3 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --checkpoint_every 25000\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 2.81, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008f_s3_no_dt_embed_walker.log\", \"pid\": \"601233\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-16T17:21:24.538Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 10106.6}}, \"exp_020_vanilla_dreamerv3_s2\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"logdir/exp_020_vanilla_dreamerv3_s2/checkpoint.pt\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_020_vanilla_dreamerv3_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --imag_horizon 15\\\"\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 2.97, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_020_vanilla_dreamerv3_s2.log\", \"pid\": \"596344\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-16T16:45:55.371Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 10682.2}}, \"exp_019a_pickcube_baseline\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A (killed before completion)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python -u dreamer.py --configs defaults maniskill_state --task maniskill_PickCube-v1 --steps 200000 --seed 1 --device cuda:0 --compile False --logdir /root/runs/event-gated-adaptive-horizon/logdir/exp_019a_pickcube_baseline\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.37, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_019a_pickcube_baseline.log\", \"pid\": \"586751\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-16T13:20:56.230Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 1324.5}}, \"exp_018_full_sgs_walker_s1\": {\"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_018_full_sgs_walker_s1/checkpoint.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_018_full_sgs_walker_s1\"}}, \"exp_010a_cheetah_baseline_s1\": {\"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010a_cheetah_baseline_s1/checkpoint.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010a_cheetah_baseline_s1\"}}, \"exp_009d_baseline_walker_s0\": {\"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009d_baseline_walker_s0/checkpoint.ckpt\", \"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009d_baseline_walker_s0 --steps 500000 --seed 0 --compile False --device cuda:0\\\"\", \"data_count\": 500000, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A - training experiment\", \"gpu\": [\"cuda:0\"], \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009d_baseline_walker_s0/metrics.jsonl\", \"model_name\": \"DreamerV3_baseline\", \"pid\": \"149703\", \"seed\": 0, \"server\": \"bjb1-45299\"}}, \"exp_017_subsample_off_trained_dt_emb\": {}, \"016e\": {}, \"exp_016e_sgs_walker_s1\": {\"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_016e_sgs_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"logdir\": \"logdir/exp_016e_sgs_walker_s1\", \"model_name\": \"dreamerv3-sgs\", \"note\": \"logdir 修正: 实际数据在 exp_016e（非 016d）\", \"pid\": 527392, \"seed\": 1, \"server\": \"bjb1-45299\"}}, \"exp_016c_sgs_walker_s1\": {\"spec\": {\"checkpoint_source\": \"N/A - training from scratch, parent is for genealogy only\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_016b_sgs_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A - training experiment, not eval\", \"gpu\": [\"cuda:1\"], \"model_name\": \"DreamerV3+FixedDt2_SGS_Subsample_H8 (reward_dt_emb_detach=True)\", \"note\": \"GPU 1 cleanup + CUDA/dm_control verification passed. logdir shared with 016b (fresh start).\", \"pid\": \"524244\", \"seed\": 1, \"server\": \"bjb1-45299\"}}, \"exp_009h_008f_walker_s0\": {\"spec\": {\"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009h_008f_walker_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"model_name\": \"DreamerV3+FixedDt2_NoDtEmbed_Subsample_H8\", \"note\": \"EGL fix: MUJOCO_EGL_DEVICE_ID=1 to match physical GPU 1. 008f series seeds: 1(008f), 2(009c), 0(009h)\", \"pid\": \"522450\", \"seed\": 0, \"server\": \"bjb1-45299\"}}, \"exp_016b_sgs_walker_s1\": {\"spec\": {\"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_016b_sgs_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"model_name\": \"DreamerV3+FixedDt2_SGS_Subsample_H8 (reward_dt_emb_detach=True)\", \"note\": \"Rerun of 016_sgs with EGL fix (MUJOCO_EGL_DEVICE_ID=1). Original 016 failed due to EGL device mismatch, not SGS code issue.\", \"pid\": \"523536\", \"seed\": 1, \"server\": \"bjb1-45299\"}}, \"exp_009g_008f_walker_s0\": {\"spec\": {\"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009g_008f_walker_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"model_name\": \"DreamerV3+FixedDt2_NoDtEmbed_Subsample_H8 (gate_fixed_dt=2, gate_subsample_max_dt=2, imag_horizon=8, gate_dt_embed_dim=0)\", \"note\": \"Replaces exp_009f which had seed=1 duplicating parent 008f. 008f series seeds: 1(008f), 2(009c), 0(009g)\", \"pid\": \"517413\", \"seed\": 0, \"server\": \"bjb1-45299\"}}, \"exp_009f_008f_walker_s1\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009f_008f_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.07, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009f_008f_walker_s1.log\", \"pid\": \"516110\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-15T18:47:48.525Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 265.3}}, \"exp_016_sgs_walker_s1\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_016_sgs_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.13, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_016_sgs_walker_s1.log\", \"pid\": \"514417\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-15T18:36:15.693Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 456.8}}, \"exp_015b_frozen_dt_emb\": {\"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_015b_frozen_dt_emb\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_015b_frozen_dt_emb --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True\\\"\", \"gpu\": [\"cuda:1\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_015b_frozen_dt_emb.log\", \"pid\": \"149991\", \"server\": \"bjb1-45299\"}}, \"exp_008a_no_subsample_dt2\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008a_fixed_dt2_no_subsample --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 1\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 4.65, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_fixed_dt2_no_subsample\", \"model_name\": \"DreamerV3+FixedDt2_NoSubsample (gate_fixed_dt=2, gate_subsample_max_dt=1, H=15)\", \"pid\": \"106942\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T01:37:46.034Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 16752.2}}, \"exp_009d_baseline_walker_s1\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009d_baseline_walker_s1 --steps 500000 --seed 1 --compile False --device cuda:0\", \"data_count\": 500000, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A - training experiment\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 5.33, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009d_baseline_walker_s1.log\", \"model_name\": \"DreamerV3 (original, gate_enabled=false)\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-15T06:35:00Z\", \"wall_clock_seconds\": 19195.2}}, \"exp_009e_008d_walker_s1\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009e_008d_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A - training experiment\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 5.43, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009e_008d_walker_s1.log\", \"model_name\": \"DreamerV3+FixedDt2_Subsample_H8\", \"pid\": \"119108\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-15T06:01:00Z\", \"wall_clock_seconds\": 19552.5}}, \"exp_009a_baseline_walker_s2\": {\"spec\": {\"data_count\": 500000, \"data_path\": \"dmc_walker_walk\", \"model_name\": \"DreamerV3 (original, gate_enabled=false)\", \"seed\": 2}}, \"exp_008e_v3_walker_s2\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_v3_walker_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 5.23, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008e_v3_walker_s2.log\", \"pid\": \"43437\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-15T00:46:45.424Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 18815.4}}, \"exp_008e_v3_walker_s1\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_v3_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 5.92, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008e_v3_walker_s1.log\", \"pid\": \"898127\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T18:49:27.945Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 21325.5}}, \"exp_006\": {}, \"exp_008a\": {}, \"exp_008c\": {}, \"exp_008d\": {}, \"exp_008e_v2_subsample_on_dt1_h15\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_v2_subsample_on_dt1_h15 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"gpu\": [\"cuda:1\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008e_v2_subsample_on_dt1_h15.log\", \"pid\": \"125392\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T04:27:30.720Z\", \"submitted_via\": \"submit_training_job\"}}, \"exp_rssm_fidelity_analysis\": {}, \"exp_008e_v3_subsample_on_dt1_h15\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_v3_subsample_on_dt1_h15 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 4.64, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_subsample_on_dt1_h15\", \"model_name\": \"DreamerV3+SubsampleON_FixedDt1_H15 (gate_subsample_max_dt=2, gate_fixed_dt=1, imag_horizon=15, untrained dt_emb)\", \"pid\": \"126110\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T04:29:31.600Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 16695.7}}, \"exp_009c_008f_walker_s2\": {\"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009c_008f_walker_s2\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009c_008f_walker_s2/metrics.jsonl\", \"model_name\": \"DreamerV3+FixedDt2_NoDtEmbed_Subsample_H8 (gate_fixed_dt=2, gate_subsample_max_dt=2, imag_horizon=8, gate_dt_embed_dim=0)\", \"seed\": 2}}, \"exp_006_fixed_dt2\": {\"spec\": {\"checkpoint_path\": \"N/A - negative result, fixed dt=2 collapsed to 132.9@65K (21.6% baseline)\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/fixed_dt2_v1_s1 --steps 150000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2\", \"data_count\": 150000, \"data_path\": \"dmc_walker_walk\", \"failure_reason\": \"fixed dt=2 崩塌：训练分布混合（58.5% dt=1 + 41.5% dt=2 log-uniform）+ 想象纯 dt=2 条件下，eval_return 从 peak 485@35K 持续下降至 132.9@65K（baseline 同期 615.9）。与 learned gate 变体一致的崩塌模式。代码审计确认 curriculum 不生效（gate_fixed_dt>0 跳过 _update_gate_schedule）。\", \"gpu\": [\"cuda:0\"], \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/fixed_dt2_v1_s1\", \"model_name\": \"DreamerV3+FixedDt2 (gate_fixed_dt=2, no learned gate)\", \"pid\": \"85029\", \"seed\": 1, \"server\": \"bjb1-45299\"}}, \"exp_008e_subsample_on_fixed_dt1\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_subsample_on_fixed_dt1_h15 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.19, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_subsample_on_fixed_dt1_h15\", \"model_name\": \"DreamerV3+SubsampleON_FixedDt1_H15 (gate_subsample_max_dt=2, gate_fixed_dt=1, imag_horizon=15)\", \"pid\": \"121636\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T04:10:22.915Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 685.0}}, \"exp_008e_subsample_on_dt1_h15\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_subsample_on_fixed_dt1_h15 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.18, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_subsample_on_fixed_dt1_h15\", \"model_name\": \"DreamerV3+SubsampleON_FixedDt1_H15 (gate_subsample_max_dt=2, gate_fixed_dt=1, imag_horizon=15)\", \"pid\": \"122038\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T04:10:46.045Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 662.5}}, \"exp_002_event_gated\": {\"spec\": {\"command\": \"python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/event_gated_s1 --steps 500000 --seed 1 --compile False --device cuda:1 --gate_enabled True\", \"data_count\": 500000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"gpu_id\": 1, \"hypothesis\": \"Event-gated variable-rate RSSM produces meaningful Δt patterns (entropy>0.3, H_eff>1.2×H_nominal) without breaking training stability (return≥80% baseline)\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/event_gated_s1\", \"model_name\": \"DreamerV3 + Event-Gated Variable-Rate RSSM (K=8, τ=5→0.5, λ_H=0.1→0.01)\", \"pid\": 9769, \"seed\": 1, \"server\": \"autodl-rtx6000\"}}}, \"count\": 132, \"total\": 132, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4643}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Bash · `toolu_0162NCjXFj2Q3MQnTt43A9Tu`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/2fe83aea-5863-4eb4-8029-aa58f80fcf56/tool-results/mcp-agent-ml-research-read_registry-1779592063540.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\nfor k,v in exps.items():\n    if '008d' in k.lower():\n        seed = v.get('spec',{}).get('seed','?')\n        print(f'{k}: seed={seed}')\n\"",
  "description": "Filter registry for 008d experiments and their seeds"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2fe83aea-5863-4eb4-8029-aa58f80fcf56",
  "uuid": "9fd4d482-0e2a-4ec7-b3c6-6040a0b6c468",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013bZoC9A75F8bdjHqtPPUsc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 717,
      "cache_read_input_tokens": 44022,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 717
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

_source line 21 · 2026-05-24T03:07:56.697Z_

<details><summary>↩ Tool result · `toolu_0162NCjXFj2Q3MQnTt43A9Tu`</summary>

```text
exp_045_treatment_extension_008d_s3: seed=3
exp_008d_civo_trigger_s4: seed=4
exp_008d_civo_trigger_s3: seed=3
exp_008d_subsample_on_h8: seed=1
exp_009b_008d_walker_s2: seed=2
exp_008d_civo_trigger_s2: seed=1
exp_009e_008d_walker_s1: seed=1
exp_008d: seed=?
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2fe83aea-5863-4eb4-8029-aa58f80fcf56",
  "uuid": "57e83e47-04fa-4dcc-b9c6-19a57eced3bb",
  "tool_use_result": {
    "stdout": "exp_045_treatment_extension_008d_s3: seed=3\nexp_008d_civo_trigger_s4: seed=4\nexp_008d_civo_trigger_s3: seed=3\nexp_008d_subsample_on_h8: seed=1\nexp_009b_008d_walker_s2: seed=2\nexp_008d_civo_trigger_s2: seed=1\nexp_009e_008d_walker_s1: seed=1\nexp_008d: seed=?",
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

_source line 22_

<details><summary>Logged reasoning block</summary>

```text
Let me check exp_008d's seed specifically.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2fe83aea-5863-4eb4-8029-aa58f80fcf56",
  "uuid": "24abdf1c-f493-487b-9d11-383447d34da6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012WcDj3fyDEtca28cZq22Xc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 407,
      "cache_read_input_tokens": 44739,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 407
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

_source line 23_

exp_008d 的 seed 未记录。让我看看它的完整 spec。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2fe83aea-5863-4eb4-8029-aa58f80fcf56",
  "uuid": "9208cadc-9ad4-491e-9b51-7e1c688709ea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012WcDj3fyDEtca28cZq22Xc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 407,
      "cache_read_input_tokens": 44739,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 407
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

<details open><summary>🔧 Tool call — Bash · `toolu_013MMZ2ojDCT7SVC2j5ysMqb`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/2fe83aea-5863-4eb4-8029-aa58f80fcf56/tool-results/mcp-agent-ml-research-read_registry-1779592063540.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\nprint(json.dumps(exps.get('exp_008d',{}).get('spec',{}), indent=2))\n\"",
  "description": "Get exp_008d full spec"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2fe83aea-5863-4eb4-8029-aa58f80fcf56",
  "uuid": "03b07744-4327-4d99-8311-b668cdf74a2c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012WcDj3fyDEtca28cZq22Xc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 407,
      "cache_read_input_tokens": 44739,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 407
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

_source line 25 · 2026-05-24T03:08:02.724Z_

<details><summary>↩ Tool result · `toolu_013MMZ2ojDCT7SVC2j5ysMqb`</summary>

```text
{}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2fe83aea-5863-4eb4-8029-aa58f80fcf56",
  "uuid": "633a4d13-3a77-4af7-ae1c-21bd66f10809",
  "tool_use_result": {
    "stdout": "{}",
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
exp_008d has an empty spec. Let me check the command from exp_008d_civo_trigger_s3 to use as the template. Also need to check what seed exp_008d used - probably from its command. But the spec is empty. 

Let me check exp_008d_civo_trigger_s3's command for the template, and also check exp_008d_civo_trigger_s2 - it says seed=1, but that's the same as exp_008d_subsample_on_h8. Let me clarify:

From the registry:


- exp_008d_subsample_on_h8: seed=1 (success - CIVO triggered)
- exp_009b_008d_walker_s2: seed=2 (negative per user)  
- exp_008d_civo_trigger_s3: seed=3 (success)
- exp_008d_civo_trigger_s4: seed=4 (success)
- exp_008d_civo_trigger_s2: seed=1 — wait, the user said seed 2 was exp_009b_008d_walker_s2. This exp_008d_civo_trigger_s2 with seed=1 is conflicting with exp_008d_subsample_on_h8.
- exp_009e_008d_walker_s1: seed=1
- exp_008d: seed=? (empty spec)

The user's already used seeds are 1, 2, 3, 4, and possibly 0, so seed 5 should be safe. I need to pull the full command from exp_008d_civo_trigger_s3 to use as a template.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2fe83aea-5863-4eb4-8029-aa58f80fcf56",
  "uuid": "ecb75ceb-1a37-4758-85e4-b0c4edc96324",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014EQ2iG71ajAJk8eLd3r2Ct",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 406,
      "cache_read_input_tokens": 45146,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 406
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

_source line 27_

<details open><summary>🔧 Tool call — Bash · `toolu_014s1veZUHrXDM6AWF6q9uLc`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/2fe83aea-5863-4eb4-8029-aa58f80fcf56/tool-results/mcp-agent-ml-research-read_registry-1779592063540.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\nprint(json.dumps(exps.get('exp_008d_civo_trigger_s3',{}).get('spec',{}), indent=2))\n\"",
  "description": "Get exp_008d_civo_trigger_s3 full spec for template"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2fe83aea-5863-4eb4-8029-aa58f80fcf56",
  "uuid": "9ed9c5a9-7e8c-4101-a539-2321a640d133",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014EQ2iG71ajAJk8eLd3r2Ct",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 406,
      "cache_read_input_tokens": 45146,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 406
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

_source line 28 · 2026-05-24T03:08:21.477Z_

<details><summary>↩ Tool result · `toolu_014s1veZUHrXDM6AWF6q9uLc`</summary>

```text
{
  "account": "root",
  "backend": "tmux",
  "checkpoint_source": "fresh_training (no checkpoint, new logdir)",
  "command": "bash -c \"unset CUDA_VISIBLE_DEVICES && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --gate_subsample_min_dt 1 --imag_horizon 8 --seed 3 --steps 105000 --checkpoint_every 25000 --compile False --device cuda:0 --logdir ./logdir/exp_008d_civo_trigger_s3\"",
  "data_count": 105000,
  "data_path": "DMC Walker Walk (online RL)",
  "eval_data": "N/A - training experiment",
  "gpu": [
    "cuda:0"
  ],
  "gpu_hours": 2.97,
  "log_path": "~/runs/event-gated-adaptive-horizon/exp_008d_civo_trigger_s3.log",
  "model_name": "DreamerV3-S",
  "pid": "635744",
  "seed": 3,
  "server": "bjb1-45299",
  "submitted_at": "2026-05-17T00:25:59.245Z",
  "submitted_via": "submit_training_job",
  "wall_clock_seconds": 10706.8
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2fe83aea-5863-4eb4-8029-aa58f80fcf56",
  "uuid": "b2458105-b403-467e-bed0-9e6d2b9b1b88",
  "tool_use_result": {
    "stdout": "{\n  \"account\": \"root\",\n  \"backend\": \"tmux\",\n  \"checkpoint_source\": \"fresh_training (no checkpoint, new logdir)\",\n  \"command\": \"bash -c \\\"unset CUDA_VISIBLE_DEVICES && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --gate_subsample_min_dt 1 --imag_horizon 8 --seed 3 --steps 105000 --checkpoint_every 25000 --compile False --device cuda:0 --logdir ./logdir/exp_008d_civo_trigger_s3\\\"\",\n  \"data_count\": 105000,\n  \"data_path\": \"DMC Walker Walk (online RL)\",\n  \"eval_data\": \"N/A - training experiment\",\n  \"gpu\": [\n    \"cuda:0\"\n  ],\n  \"gpu_hours\": 2.97,\n  \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008d_civo_trigger_s3.log\",\n  \"model_name\": \"DreamerV3-S\",\n  \"pid\": \"635744\",\n  \"seed\": 3,\n  \"server\": \"bjb1-45299\",\n  \"submitted_at\": \"2026-05-17T00:25:59.245Z\",\n  \"submitted_via\": \"submit_training_job\",\n  \"wall_clock_seconds\": 10706.8\n}",
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

_source line 29_

<details><summary>Logged reasoning block</summary>

```text
Now I have the template from s3. I notice a few things:

1. The s3 command uses `--steps 105000` not 210000 as the user specified. Let me check if the user's request says 210000 steps. Yes, the user says "steps: 210000". But the s3 experiment ran with 105000. Let me check s4 to see what steps it used.

Wait, the user's instruction says "与 exp_008d_civo_trigger_s3 完全一致，只改 seed". So I should use 105000 steps as in s3, not 210000 as listed in the config section. 

Actually, I'm second-guessing myself here. The user explicitly states "steps: 210000" in the config section, even though they also say to match s3 exactly except for the seed. Since s3 used 105000 steps but the user is now specifying 210000, they likely want to extend the training further this time. I should go with the explicit 210000 steps they've stated.

Looking at the s3 command structure, I notice it has `--gate_subsample_min_dt 1` which isn't mentioned in the user's config list. The user specifies "configs: defaults dmc_proprio" which aligns with s3's setup. I'll use the user's explicit config values where provided but follow s3's command template structure for consistency.

For the specific settings the user listed: dt_emb_freeze defaults to False (trained), compile is False, checkpoint_every is 25000, and seed is 5. Since s3's command doesn't include a `--dt_emb_freeze` flag, that confirms it's using the default trained version. Now I need to figure out the deployment setup for CUDA.

For running on GPU device 1, I'll need to set CUDA_VISIBLE_DEVICES=1 and MUJOCO_EGL_DEVICE_ID=1, which remaps the device to cuda:0 in the command. Looking at the seed patterns across the experiments, I can see they range from 1 to 4, with some experiments having unknown seeds, so the user's seed 5 would be a new one.

Now I'm setting up the registry entry and preparing the training command with 210000 steps as specified in the config—that's longer than the previous runs, likely to give CIVO enough time to fully develop.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2fe83aea-5863-4eb4-8029-aa58f80fcf56",
  "uuid": "afe7bb70-c881-4426-8afd-b6944156f838",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FyNUQsJBNxDsnEGaYpvsZi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1142,
      "cache_read_input_tokens": 45552,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1142
      },
      "output_tokens": 10,
      "service_tier": "standard",
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

_source line 30_

已确认 008d 系列已用 seeds: 1, 2, 3, 4（exp_008d 本身 spec 为空但大概率是 seed 0）。**Seed 5 安全可用。**

注意 s3 实际跑了 105000 步，但你指定 210000。我按你的指定用 210000。

创建 registry 条目。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2fe83aea-5863-4eb4-8029-aa58f80fcf56",
  "uuid": "cdd6b98d-794b-4599-b6fc-44eb82134d8c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FyNUQsJBNxDsnEGaYpvsZi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1142,
      "cache_read_input_tokens": 45552,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1142
      },
      "output_tokens": 10,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_016jGYYpvpjTreeGJMvhbhTF`</summary>

```json
{
  "exp_id": "exp_059_walker_trained_s5",
  "field": "status",
  "value": "PREPARING",
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2fe83aea-5863-4eb4-8029-aa58f80fcf56",
  "uuid": "af72593e-22c4-4f02-b5bc-b33407caadbc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FyNUQsJBNxDsnEGaYpvsZi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1142,
      "cache_read_input_tokens": 45552,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1142
      },
      "output_tokens": 10,
      "service_tier": "standard",
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

_source line 32 · 2026-05-24T03:08:48.261Z_

<details><summary>↩ Tool result · `toolu_016jGYYpvpjTreeGJMvhbhTF`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_059_walker_trained_s5\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T03:08:46.842Z\", \"updated_at\": \"2026-05-24T03:08:46.842Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.8737}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2fe83aea-5863-4eb4-8029-aa58f80fcf56",
  "uuid": "04c9ce1a-339c-4e4d-8efd-2c155bd62edb",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"exp_059_walker_trained_s5\\\", \\\"experiment\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T03:08:46.842Z\\\", \\\"updated_at\\\": \\\"2026-05-24T03:08:46.842Z\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.8737}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"exp_059_walker_trained_s5\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T03:08:46.842Z\", \"updated_at\": \"2026-05-24T03:08:46.842Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.8737}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01J2g3uGNPcA9Ya5Y2H1WgSp`</summary>

```json
{
  "exp_id": "exp_059_walker_trained_s5",
  "field": "hypothesis",
  "value": "Walker CIVO trigger 第5个独立seed验证。当前4/4 seeds触发sustained CIVO（p=0.0625 binomial test）。如果s5也触发 → p=0.03125，达到统计显著性阈值。关联 Claim 1: CIVO reproducibility。",
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2fe83aea-5863-4eb4-8029-aa58f80fcf56",
  "uuid": "81aa633e-9d81-4863-883d-4062a60606f4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SPuA7tSJhYpoBFaduPQ59m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1225,
      "cache_read_input_tokens": 46694,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1225
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

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01HLqVxMMHEadD8dPdx2EtjE`</summary>

```json
{
  "exp_id": "exp_059_walker_trained_s5",
  "field": "parent",
  "value": "exp_008d_civo_trigger_s3",
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2fe83aea-5863-4eb4-8029-aa58f80fcf56",
  "uuid": "8c9c459b-201a-436e-ae1f-0e3a7a815a69",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SPuA7tSJhYpoBFaduPQ59m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1225,
      "cache_read_input_tokens": 46694,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1225
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

_source line 35 · 2026-05-24T03:08:55.649Z_

<details><summary>↩ Tool result · `toolu_01J2g3uGNPcA9Ya5Y2H1WgSp`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_059_walker_trained_s5\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T03:08:46.842Z\", \"updated_at\": \"2026-05-24T03:08:55.281Z\", \"hypothesis\": \"Walker CIVO trigger 第5个独立seed验证。当前4/4 seeds触发sustained CIVO（p=0.0625 binomial test）。如果s5也触发 → p=0.03125，达到统计显著性阈值。关联 Claim 1: CIVO reproducibility。\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8163}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2fe83aea-5863-4eb4-8029-aa58f80fcf56",
  "uuid": "91d152fe-f6bb-49d8-9997-b604095a2def",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"exp_059_walker_trained_s5\\\", \\\"experiment\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T03:08:46.842Z\\\", \\\"updated_at\\\": \\\"2026-05-24T03:08:55.281Z\\\", \\\"hypothesis\\\": \\\"Walker CIVO trigger 第5个独立seed验证。当前4/4 seeds触发sustained CIVO（p=0.0625 binomial test）。如果s5也触发 → p=0.03125，达到统计显著性阈值。关联 Claim 1: CIVO reproducibility。\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.8163}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"exp_059_walker_trained_s5\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T03:08:46.842Z\", \"updated_at\": \"2026-05-24T03:08:55.281Z\", \"hypothesis\": \"Walker CIVO trigger 第5个独立seed验证。当前4/4 seeds触发sustained CIVO（p=0.0625 binomial test）。如果s5也触发 → p=0.03125，达到统计显著性阈值。关联 Claim 1: CIVO reproducibility。\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8163}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-24T03:08:56.429Z_

<details><summary>↩ Tool result · `toolu_01HLqVxMMHEadD8dPdx2EtjE`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_059_walker_trained_s5\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T03:08:46.842Z\", \"updated_at\": \"2026-05-24T03:08:56.106Z\", \"hypothesis\": \"Walker CIVO trigger 第5个独立seed验证。当前4/4 seeds触发sustained CIVO（p=0.0625 binomial test）。如果s5也触发 → p=0.03125，达到统计显著性阈值。关联 Claim 1: CIVO reproducibility。\", \"parent\": \"exp_008d_civo_trigger_s3\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7685}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2fe83aea-5863-4eb4-8029-aa58f80fcf56",
  "uuid": "435c2814-6497-4b29-b224-168c3a2aeeab",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"exp_059_walker_trained_s5\\\", \\\"experiment\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T03:08:46.842Z\\\", \\\"updated_at\\\": \\\"2026-05-24T03:08:56.106Z\\\", \\\"hypothesis\\\": \\\"Walker CIVO trigger 第5个独立seed验证。当前4/4 seeds触发sustained CIVO（p=0.0625 binomial test）。如果s5也触发 → p=0.03125，达到统计显著性阈值。关联 Claim 1: CIVO reproducibility。\\\", \\\"parent\\\": \\\"exp_008d_civo_trigger_s3\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.7685}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"exp_059_walker_trained_s5\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T03:08:46.842Z\", \"updated_at\": \"2026-05-24T03:08:56.106Z\", \"hypothesis\": \"Walker CIVO trigger 第5个独立seed验证。当前4/4 seeds触发sustained CIVO（p=0.0625 binomial test）。如果s5也触发 → p=0.03125，达到统计显著性阈值。关联 Claim 1: CIVO reproducibility。\", \"parent\": \"exp_008d_civo_trigger_s3\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7685}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_019dParJbfuugBwgBjjLJm9h`</summary>

```json
{
  "exp_id": "exp_059_walker_trained_s5",
  "field": "status",
  "value": "PENDING",
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2fe83aea-5863-4eb4-8029-aa58f80fcf56",
  "uuid": "c30e060c-518c-4132-b13a-627a0dd176fb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BfYK7fMGNQVEZtDALuu8uw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 875,
      "cache_read_input_tokens": 47919,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 875
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

_source line 38 · 2026-05-24T03:09:00.953Z_

<details><summary>↩ Tool result · `toolu_019dParJbfuugBwgBjjLJm9h`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_059_walker_trained_s5\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T03:08:46.842Z\", \"updated_at\": \"2026-05-24T03:08:59.546Z\", \"hypothesis\": \"Walker CIVO trigger 第5个独立seed验证。当前4/4 seeds触发sustained CIVO（p=0.0625 binomial test）。如果s5也触发 → p=0.03125，达到统计显著性阈值。关联 Claim 1: CIVO reproducibility。\", \"parent\": \"exp_008d_civo_trigger_s3\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.888}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2fe83aea-5863-4eb4-8029-aa58f80fcf56",
  "uuid": "002543e2-956a-4c4e-96db-799dc40bda87",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"exp_059_walker_trained_s5\\\", \\\"experiment\\\": {\\\"status\\\": \\\"PENDING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-24T03:08:46.842Z\\\", \\\"updated_at\\\": \\\"2026-05-24T03:08:59.546Z\\\", \\\"hypothesis\\\": \\\"Walker CIVO trigger 第5个独立seed验证。当前4/4 seeds触发sustained CIVO（p=0.0625 binomial test）。如果s5也触发 → p=0.03125，达到统计显著性阈值。关联 Claim 1: CIVO reproducibility。\\\", \\\"parent\\\": \\\"exp_008d_civo_trigger_s3\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.888}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"exp_059_walker_trained_s5\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-24T03:08:46.842Z\", \"updated_at\": \"2026-05-24T03:08:59.546Z\", \"hypothesis\": \"Walker CIVO trigger 第5个独立seed验证。当前4/4 seeds触发sustained CIVO（p=0.0625 binomial test）。如果s5也触发 → p=0.03125，达到统计显著性阈值。关联 Claim 1: CIVO reproducibility。\", \"parent\": \"exp_008d_civo_trigger_s3\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.888}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 39_

## 完成

**Seed**: 5（seeds 0-4 均已被使用或可能被使用）

**Registry**: `exp_059_walker_trained_s5` 已创建，状态 PENDING，等待审批。

**训练命令**（部署到 bjb1-45299:cuda:1）：

```bash
CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py \
  --configs defaults dmc_proprio \
  --task dmc_walker_walk \
  --gate_enabled True \
  --gate_fixed_dt 2 \
  --gate_subsample_max_dt 2 \
  --gate_subsample_min_dt 1 \
  --imag_horizon 8 \
  --seed 5 \
  --steps 210000 \
  --checkpoint_every 25000 \
  --compile False \
  --device cuda:0 \
  --logdir ./logdir/exp_059_walker_trained_s5
```

**注意**: s3 模板实际跑了 105000 步，你指定了 210000。如果需要与 s3 完全一致应改为 105000。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2fe83aea-5863-4eb4-8029-aa58f80fcf56",
  "uuid": "b78e5313-eb37-4df7-a71b-c1a77941b3f6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JoF5x7PcSF5XXA59geFpN9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 381,
      "cache_read_input_tokens": 48794,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 381
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

_source line 40_

## 完成

**Seed**: 5（seeds 0-4 均已被使用或可能被使用）

**Registry**: `exp_059_walker_trained_s5` 已创建，状态 PENDING，等待审批。

**训练命令**（部署到 bjb1-45299:cuda:1）：

```bash
CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py \
  --configs defaults dmc_proprio \
  --task dmc_walker_walk \
  --gate_enabled True \
  --gate_fixed_dt 2 \
  --gate_subsample_max_dt 2 \
  --gate_subsample_min_dt 1 \
  --imag_horizon 8 \
  --seed 5 \
  --steps 210000 \
  --checkpoint_every 25000 \
  --compile False \
  --device cuda:0 \
  --logdir ./logdir/exp_059_walker_trained_s5
```

**注意**: s3 模板实际跑了 105000 步，你指定了 210000。如果需要与 s3 完全一致应改为 105000。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 114851,
  "duration_api_ms": 119221,
  "num_turns": 13,
  "stop_reason": "end_turn",
  "session_id": "2fe83aea-5863-4eb4-8029-aa58f80fcf56",
  "total_cost_usd": 0.5445130000000001,
  "usage": {
    "input_tokens": 15,
    "cache_creation_input_tokens": 37728,
    "cache_read_input_tokens": 407462,
    "output_tokens": 4137,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 37728,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 360,
        "cache_read_input_tokens": 48794,
        "cache_creation_input_tokens": 381,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 381
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-opus-4-6": {
      "inputTokens": 15,
      "outputTokens": 4137,
      "cacheReadInputTokens": 407462,
      "cacheCreationInputTokens": 37728,
      "webSearchRequests": 0,
      "costUSD": 0.5430310000000002,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    },
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1377,
      "outputTokens": 21,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001482,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "bccc39e3-f46d-4fef-9112-8d46a2bba55f"
}
```

</details>

---
