# analysis exp 003 eval s2 ckpt8000

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 32
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/workers/worker_analysis_exp-003-eval-s2-ckpt8000_20260522T170420.log`
- **Structured JSON:** [`ceaf901e7d3e3aa4391c.json`](../../sessions/ce/ceaf901e7d3e3aa4391c.json)

## Before a recorded user message

32 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "session_id": "26c5ec7a-74bc-48da-96c7-b3a2f055f03a",
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
  "uuid": "38d8af55-b55b-4b42-b4e6-7f20c9881236",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-3-projects-contrastive-entrain-calib/memory/"
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
    "resetsAt": 1779487200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "7e940596-e4a8-4be9-b797-ccaa1c55ea08",
  "session_id": "26c5ec7a-74bc-48da-96c7-b3a2f055f03a"
}
```

---

### Assistant

_source line 4_

I'll read the eval log and check the registry in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26c5ec7a-74bc-48da-96c7-b3a2f055f03a",
  "uuid": "b6ea6e14-0a5b-4e16-befc-2ba617e273ce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LJmHaQ8ncYjun59LNZ59En",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12055,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12055
      },
      "output_tokens": 4,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01PhwJ1yp9XV51NHHgR5k3V7`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__update_registry",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26c5ec7a-74bc-48da-96c7-b3a2f055f03a",
  "uuid": "c5e1f633-5111-4cbe-8f39-c5fb502e83db",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LJmHaQ8ncYjun59LNZ59En",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12055,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12055
      },
      "output_tokens": 4,
      "service_tier": "standard",
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

_source line 6 · 2026-05-22T17:04:31.311Z_

<details><summary>↩ Tool result · `toolu_01PhwJ1yp9XV51NHHgR5k3V7`</summary>

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
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26c5ec7a-74bc-48da-96c7-b3a2f055f03a",
  "uuid": "242c48de-c955-4a54-a35d-a4820a127306",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__update_registry"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__update_registry",
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
Now I'll execute the three parallel operations: read the log, check results directory, and read the registry for seed 1 ckpt-8000.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26c5ec7a-74bc-48da-96c7-b3a2f055f03a",
  "uuid": "1cad7528-24b6-4a14-92fe-5eb5123f8aa4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CQhGxqxYgfSuRvbbfWVgTn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1278,
      "cache_read_input_tokens": 23896,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1278
      },
      "output_tokens": 17,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01SYZAeqRLevPWcW6uva1Wan`</summary>

```json
{
  "server": "westd-29046",
  "command": "cat /root/runs/contrastive_entrain_calib/exp-003-eval-s2-ckpt8000.log",
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
  "session_id": "26c5ec7a-74bc-48da-96c7-b3a2f055f03a",
  "uuid": "3e2cbd54-1427-43d6-908a-b78521fa23b0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CQhGxqxYgfSuRvbbfWVgTn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1278,
      "cache_read_input_tokens": 23896,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1278
      },
      "output_tokens": 17,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01AGcMojZUhD7xrTBTaVhZsH`</summary>

```json
{
  "server": "westd-29046",
  "command": "ls -la /root/contrastive_entrain_calib/results/exp003_d027_eval/",
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
  "session_id": "26c5ec7a-74bc-48da-96c7-b3a2f055f03a",
  "uuid": "aa1eb6e6-e5cc-4a64-a990-c49e2fb4e460",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CQhGxqxYgfSuRvbbfWVgTn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1278,
      "cache_read_input_tokens": 23896,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1278
      },
      "output_tokens": 17,
      "service_tier": "standard",
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

_source line 10 · 2026-05-22T17:04:39.518Z_

<details><summary>↩ Tool result · `toolu_01SYZAeqRLevPWcW6uva1Wan`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-22 23:38:44,503 [INFO] eval_unified_preset: === D027 Unified Preset Eval ===\\n2026-05-22 23:38:44,503 [INFO] eval_unified_preset: model_path: /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B\\n2026-05-22 23:38:44,503 [INFO] eval_unified_preset: lora_path:  /root/autodl-tmp/checkpoints/exp003_r3only_seed2/checkpoint-8000\\n2026-05-22 23:38:44,503 [INFO] eval_unified_preset: data_path:  /root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl\\n2026-05-22 23:38:44,503 [INFO] eval_unified_preset: exp_id:     exp003-s2-ckpt8000\\n2026-05-22 23:38:44,806 [INFO] eval_unified_preset: Loading model...\\n`torch_dtype` is deprecated! Use `dtype` instead!\\n2026-05-22 23:38:45,373 [INFO] accelerate.utils.modeling: We will use 90% of the memory on device 0 for storing the model, and 10% for the buffer to avoid OOM. You can set `max_memory` in to a higher value to use more memory (at your own risk).\\n\\rLoading checkpoint shards:   0%|          | 0/5 [00:00<?, ?it/s]\\rLoading checkpoint shards:  20%|██        | 1/5 [00:00<00:02,  1.42it/s]\\rLoading checkpoint shards:  40%|████      | 2/5 [00:01<00:02,  1.40it/s]\\rLoading checkpoint shards:  60%|██████    | 3/5 [00:02<00:01,  1.07it/s]\\rLoading checkpoint shards:  80%|████████  | 4/5 [00:03<00:00,  1.25it/s]\\rLoading checkpoint shards: 100%|██████████| 5/5 [00:03<00:00,  1.70it/s]\\rLoading checkpoint shards: 100%|██████████| 5/5 [00:03<00:00,  1.46it/s]\\n2026-05-22 23:38:48,948 [INFO] eval_unified_preset: Loading LoRA adapter: /root/autodl-tmp/checkpoints/exp003_r3only_seed2/checkpoint-8000\\n2026-05-22 23:38:50,609 [INFO] eval_unified_preset: Loading NLI model...\\n2026-05-22 23:38:50,830 [INFO] eval_unified_preset: NLI loaded: cross-encoder/nli-deberta-v3-base  id2label={0: 'contradiction', 1: 'entailment', 2: 'neutral'}  ent=1 con=0\\n2026-05-22 23:38:50,833 [INFO] eval_unified_preset: Loaded 362 eval pairs from /root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl\\n2026-05-22 23:38:50,833 [INFO] eval_unified_preset: Running eval on 362 pairs...\\nThe following generation flags are not valid and may be ignored: ['temperature', 'top_p', 'top_k']. Set `TRANSFORMERS_VERBOSITY=info` for more details.\\n2026-05-22 23:48:22,935 [INFO] eval_unified_preset:   Progress: 20/362\\n2026-05-22 23:55:34,434 [INFO] eval_unified_preset:   Progress: 40/362\\n2026-05-23 00:01:06,934 [INFO] eval_unified_preset:   Progress: 60/362\\n2026-05-23 00:05:30,419 [INFO] eval_unified_preset:   Progress: 80/362\\n2026-05-23 00:08:54,146 [INFO] eval_unified_preset:   Progress: 100/362\\n2026-05-23 00:13:40,540 [INFO] eval_unified_preset:   Progress: 120/362\\n2026-05-23 00:17:51,653 [INFO] eval_unified_preset:   Progress: 140/362\\n2026-05-23 00:21:47,555 [INFO] eval_unified_preset:   Progress: 160/362\\n2026-05-23 00:24:27,324 [INFO] eval_unified_preset:   Progress: 180/362\\n2026-05-23 00:27:58,433 [INFO] eval_unified_preset:   Progress: 200/362\\n2026-05-23 00:31:31,244 [INFO] eval_unified_preset:   Progress: 220/362\\n2026-05-23 00:35:51,037 [INFO] eval_unified_preset:   Progress: 240/362\\n2026-05-23 00:40:34,960 [INFO] eval_unified_preset:   Progress: 260/362\\n2026-05-23 00:45:27,735 [INFO] eval_unified_preset:   Progress: 280/362\\n2026-05-23 00:49:31,559 [INFO] eval_unified_preset:   Progress: 300/362\\n2026-05-23 00:53:17,344 [INFO] eval_unified_preset:   Progress: 320/362\\n2026-05-23 00:56:54,443 [INFO] eval_unified_preset:   Progress: 340/362\\n2026-05-23 01:01:49,731 [INFO] eval_unified_preset:   Progress: 360/362\\n2026-05-23 01:02:21,336 [INFO] eval_unified_preset: Detailed results: /root/contrastive_entrain_calib/results/exp003_d027_eval/exp003-s2-ckpt8000_preset_eval.json\\n2026-05-23 01:02:21,337 [INFO] eval_unified_preset: Summary: /root/contrastive_entrain_calib/results/exp003_d027_eval/exp003-s2-ckpt8000_preset_summary.txt\\n\\n==================================================\\n  D027 Preset Eval: exp003-s2-ckpt8000\\n==================================================\\n  ToF        = 0.0663\\n  NoF        = 0.9613\\n  SYCONScore = 0.1240\\n  Samples    = 362 (valid=181, invalid=181)\\n  Time       = 5010s\\n==================================================\\n\\nEXIT_CODE=0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26c5ec7a-74bc-48da-96c7-b3a2f055f03a",
  "uuid": "156a16a1-3d8b-42e2-8b5d-efc94a4bd451",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"2026-05-22 23:38:44,503 [INFO] eval_unified_preset: === D027 Unified Preset Eval ===\\\\n2026-05-22 23:38:44,503 [INFO] eval_unified_preset: model_path: /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B\\\\n2026-05-22 23:38:44,503 [INFO] eval_unified_preset: lora_path:  /root/autodl-tmp/checkpoints/exp003_r3only_seed2/checkpoint-8000\\\\n2026-05-22 23:38:44,503 [INFO] eval_unified_preset: data_path:  /root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl\\\\n2026-05-22 23:38:44,503 [INFO] eval_unified_preset: exp_id:     exp003-s2-ckpt8000\\\\n2026-05-22 23:38:44,806 [INFO] eval_unified_preset: Loading model...\\\\n`torch_dtype` is deprecated! Use `dtype` instead!\\\\n2026-05-22 23:38:45,373 [INFO] accelerate.utils.modeling: We will use 90% of the memory on device 0 for storing the model, and 10% for the buffer to avoid OOM. You can set `max_memory` in to a higher value to use more memory (at your own risk).\\\\n\\\\rLoading checkpoint shards:   0%|          | 0/5 [00:00<?, ?it/s]\\\\rLoading checkpoint shards:  20%|██        | 1/5 [00:00<00:02,  1.42it/s]\\\\rLoading checkpoint shards:  40%|████      | 2/5 [00:01<00:02,  1.40it/s]\\\\rLoading checkpoint shards:  60%|██████    | 3/5 [00:02<00:01,  1.07it/s]\\\\rLoading checkpoint shards:  80%|████████  | 4/5 [00:03<00:00,  1.25it/s]\\\\rLoading checkpoint shards: 100%|██████████| 5/5 [00:03<00:00,  1.70it/s]\\\\rLoading checkpoint shards: 100%|██████████| 5/5 [00:03<00:00,  1.46it/s]\\\\n2026-05-22 23:38:48,948 [INFO] eval_unified_preset: Loading LoRA adapter: /root/autodl-tmp/checkpoints/exp003_r3only_seed2/checkpoint-8000\\\\n2026-05-22 23:38:50,609 [INFO] eval_unified_preset: Loading NLI model...\\\\n2026-05-22 23:38:50,830 [INFO] eval_unified_preset: NLI loaded: cross-encoder/nli-deberta-v3-base  id2label={0: 'contradiction', 1: 'entailment', 2: 'neutral'}  ent=1 con=0\\\\n2026-05-22 23:38:50,833 [INFO] eval_unified_preset: Loaded 362 eval pairs from /root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl\\\\n2026-05-22 23:38:50,833 [INFO] eval_unified_preset: Running eval on 362 pairs...\\\\nThe following generation flags are not valid and may be ignored: ['temperature', 'top_p', 'top_k']. Set `TRANSFORMERS_VERBOSITY=info` for more details.\\\\n2026-05-22 23:48:22,935 [INFO] eval_unified_preset:   Progress: 20/362\\\\n2026-05-22 23:55:34,434 [INFO] eval_unified_preset:   Progress: 40/362\\\\n2026-05-23 00:01:06,934 [INFO] eval_unified_preset:   Progress: 60/362\\\\n2026-05-23 00:05:30,419 [INFO] eval_unified_preset:   Progress: 80/362\\\\n2026-05-23 00:08:54,146 [INFO] eval_unified_preset:   Progress: 100/362\\\\n2026-05-23 00:13:40,540 [INFO] eval_unified_preset:   Progress: 120/362\\\\n2026-05-23 00:17:51,653 [INFO] eval_unified_preset:   Progress: 140/362\\\\n2026-05-23 00:21:47,555 [INFO] eval_unified_preset:   Progress: 160/362\\\\n2026-05-23 00:24:27,324 [INFO] eval_unified_preset:   Progress: 180/362\\\\n2026-05-23 00:27:58,433 [INFO] eval_unified_preset:   Progress: 200/362\\\\n2026-05-23 00:31:31,244 [INFO] eval_unified_preset:   Progress: 220/362\\\\n2026-05-23 00:35:51,037 [INFO] eval_unified_preset:   Progress: 240/362\\\\n2026-05-23 00:40:34,960 [INFO] eval_unified_preset:   Progress: 260/362\\\\n2026-05-23 00:45:27,735 [INFO] eval_unified_preset:   Progress: 280/362\\\\n2026-05-23 00:49:31,559 [INFO] eval_unified_preset:   Progress: 300/362\\\\n2026-05-23 00:53:17,344 [INFO] eval_unified_preset:   Progress: 320/362\\\\n2026-05-23 00:56:54,443 [INFO] eval_unified_preset:   Progress: 340/362\\\\n2026-05-23 01:01:49,731 [INFO] eval_unified_preset:   Progress: 360/362\\\\n2026-05-23 01:02:21,336 [INFO] eval_unified_preset: Detailed results: /root/contrastive_entrain_calib/results/exp003_d027_eval/exp003-s2-ckpt8000_preset_eval.json\\\\n2026-05-23 01:02:21,337 [INFO] eval_unified_preset: Summary: /root/contrastive_entrain_calib/results/exp003_d027_eval/exp003-s2-ckpt8000_preset_summary.txt\\\\n\\\\n==================================================\\\\n  D027 Preset Eval: exp003-s2-ckpt8000\\\\n==================================================\\\\n  ToF        = 0.0663\\\\n  NoF        = 0.9613\\\\n  SYCONScore = 0.1240\\\\n  Samples    = 362 (valid=181, invalid=181)\\\\n  Time       = 5010s\\\\n==================================================\\\\n\\\\nEXIT_CODE=0\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"2026-05-22 23:38:44,503 [INFO] eval_unified_preset: === D027 Unified Preset Eval ===\\n2026-05-22 23:38:44,503 [INFO] eval_unified_preset: model_path: /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B\\n2026-05-22 23:38:44,503 [INFO] eval_unified_preset: lora_path:  /root/autodl-tmp/checkpoints/exp003_r3only_seed2/checkpoint-8000\\n2026-05-22 23:38:44,503 [INFO] eval_unified_preset: data_path:  /root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl\\n2026-05-22 23:38:44,503 [INFO] eval_unified_preset: exp_id:     exp003-s2-ckpt8000\\n2026-05-22 23:38:44,806 [INFO] eval_unified_preset: Loading model...\\n`torch_dtype` is deprecated! Use `dtype` instead!\\n2026-05-22 23:38:45,373 [INFO] accelerate.utils.modeling: We will use 90% of the memory on device 0 for storing the model, and 10% for the buffer to avoid OOM. You can set `max_memory` in to a higher value to use more memory (at your own risk).\\n\\rLoading checkpoint shards:   0%|          | 0/5 [00:00<?, ?it/s]\\rLoading checkpoint shards:  20%|██        | 1/5 [00:00<00:02,  1.42it/s]\\rLoading checkpoint shards:  40%|████      | 2/5 [00:01<00:02,  1.40it/s]\\rLoading checkpoint shards:  60%|██████    | 3/5 [00:02<00:01,  1.07it/s]\\rLoading checkpoint shards:  80%|████████  | 4/5 [00:03<00:00,  1.25it/s]\\rLoading checkpoint shards: 100%|██████████| 5/5 [00:03<00:00,  1.70it/s]\\rLoading checkpoint shards: 100%|██████████| 5/5 [00:03<00:00,  1.46it/s]\\n2026-05-22 23:38:48,948 [INFO] eval_unified_preset: Loading LoRA adapter: /root/autodl-tmp/checkpoints/exp003_r3only_seed2/checkpoint-8000\\n2026-05-22 23:38:50,609 [INFO] eval_unified_preset: Loading NLI model...\\n2026-05-22 23:38:50,830 [INFO] eval_unified_preset: NLI loaded: cross-encoder/nli-deberta-v3-base  id2label={0: 'contradiction', 1: 'entailment', 2: 'neutral'}  ent=1 con=0\\n2026-05-22 23:38:50,833 [INFO] eval_unified_preset: Loaded 362 eval pairs from /root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl\\n2026-05-22 23:38:50,833 [INFO] eval_unified_preset: Running eval on 362 pairs...\\nThe following generation flags are not valid and may be ignored: ['temperature', 'top_p', 'top_k']. Set `TRANSFORMERS_VERBOSITY=info` for more details.\\n2026-05-22 23:48:22,935 [INFO] eval_unified_preset:   Progress: 20/362\\n2026-05-22 23:55:34,434 [INFO] eval_unified_preset:   Progress: 40/362\\n2026-05-23 00:01:06,934 [INFO] eval_unified_preset:   Progress: 60/362\\n2026-05-23 00:05:30,419 [INFO] eval_unified_preset:   Progress: 80/362\\n2026-05-23 00:08:54,146 [INFO] eval_unified_preset:   Progress: 100/362\\n2026-05-23 00:13:40,540 [INFO] eval_unified_preset:   Progress: 120/362\\n2026-05-23 00:17:51,653 [INFO] eval_unified_preset:   Progress: 140/362\\n2026-05-23 00:21:47,555 [INFO] eval_unified_preset:   Progress: 160/362\\n2026-05-23 00:24:27,324 [INFO] eval_unified_preset:   Progress: 180/362\\n2026-05-23 00:27:58,433 [INFO] eval_unified_preset:   Progress: 200/362\\n2026-05-23 00:31:31,244 [INFO] eval_unified_preset:   Progress: 220/362\\n2026-05-23 00:35:51,037 [INFO] eval_unified_preset:   Progress: 240/362\\n2026-05-23 00:40:34,960 [INFO] eval_unified_preset:   Progress: 260/362\\n2026-05-23 00:45:27,735 [INFO] eval_unified_preset:   Progress: 280/362\\n2026-05-23 00:49:31,559 [INFO] eval_unified_preset:   Progress: 300/362\\n2026-05-23 00:53:17,344 [INFO] eval_unified_preset:   Progress: 320/362\\n2026-05-23 00:56:54,443 [INFO] eval_unified_preset:   Progress: 340/362\\n2026-05-23 01:01:49,731 [INFO] eval_unified_preset:   Progress: 360/362\\n2026-05-23 01:02:21,336 [INFO] eval_unified_preset: Detailed results: /root/contrastive_entrain_calib/results/exp003_d027_eval/exp003-s2-ckpt8000_preset_eval.json\\n2026-05-23 01:02:21,337 [INFO] eval_unified_preset: Summary: /root/contrastive_entrain_calib/results/exp003_d027_eval/exp003-s2-ckpt8000_preset_summary.txt\\n\\n==================================================\\n  D027 Preset Eval: exp003-s2-ckpt8000\\n==================================================\\n  ToF        = 0.0663\\n  NoF        = 0.9613\\n  SYCONScore = 0.1240\\n  Samples    = 362 (valid=181, invalid=181)\\n  Time       = 5010s\\n==================================================\\n\\nEXIT_CODE=0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.45}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01CBmHQiA58TWwKszRvgJcQK`</summary>

```json
{
  "filters": {
    "exp_id": "exp-003-eval-ckpt8000"
  },
  "project": "contrastive_entrain_calib",
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
  "session_id": "26c5ec7a-74bc-48da-96c7-b3a2f055f03a",
  "uuid": "bdf81daa-631e-4f7c-8b57-f343cef7e54a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CQhGxqxYgfSuRvbbfWVgTn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1278,
      "cache_read_input_tokens": 23896,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1278
      },
      "output_tokens": 17,
      "service_tier": "standard",
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

_source line 12 · 2026-05-22T17:04:40.039Z_

<details><summary>↩ Tool result · `toolu_01AGcMojZUhD7xrTBTaVhZsH`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 1240\\ndrwxr-xr-x  2 root root   4096 May 23 01:02 .\\ndrwxr-xr-x 13 root root   4096 May 22 10:12 ..\\n-rw-r--r--  1 root root 624212 May 22 11:27 exp003-s2-ckpt4000_preset_eval.json\\n-rw-r--r--  1 root root    369 May 22 11:27 exp003-s2-ckpt4000_preset_summary.txt\\n-rw-r--r--  1 root root 622766 May 23 01:02 exp003-s2-ckpt8000_preset_eval.json\\n-rw-r--r--  1 root root    369 May 23 01:02 exp003-s2-ckpt8000_preset_summary.txt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26c5ec7a-74bc-48da-96c7-b3a2f055f03a",
  "uuid": "68fe6a31-c72e-4772-a0d0-e4c6246fdcea",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"total 1240\\\\ndrwxr-xr-x  2 root root   4096 May 23 01:02 .\\\\ndrwxr-xr-x 13 root root   4096 May 22 10:12 ..\\\\n-rw-r--r--  1 root root 624212 May 22 11:27 exp003-s2-ckpt4000_preset_eval.json\\\\n-rw-r--r--  1 root root    369 May 22 11:27 exp003-s2-ckpt4000_preset_summary.txt\\\\n-rw-r--r--  1 root root 622766 May 23 01:02 exp003-s2-ckpt8000_preset_eval.json\\\\n-rw-r--r--  1 root root    369 May 23 01:02 exp003-s2-ckpt8000_preset_summary.txt\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.51}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"total 1240\\ndrwxr-xr-x  2 root root   4096 May 23 01:02 .\\ndrwxr-xr-x 13 root root   4096 May 22 10:12 ..\\n-rw-r--r--  1 root root 624212 May 22 11:27 exp003-s2-ckpt4000_preset_eval.json\\n-rw-r--r--  1 root root    369 May 22 11:27 exp003-s2-ckpt4000_preset_summary.txt\\n-rw-r--r--  1 root root 622766 May 23 01:02 exp003-s2-ckpt8000_preset_eval.json\\n-rw-r--r--  1 root root    369 May 23 01:02 exp003-s2-ckpt8000_preset_summary.txt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-22T17:04:40.281Z_

<details><summary>↩ Tool result · `toolu_01CBmHQiA58TWwKszRvgJcQK`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2287}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26c5ec7a-74bc-48da-96c7-b3a2f055f03a",
  "uuid": "8933d2fc-cb76-4482-8228-c745e06ec1e2",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.2287}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2287}}"
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
The registry filter by exp_id didn't work as expected. Let me search for the seed 1 ckpt-8000 eval experiment. The filter might need a different approach - let me try searching more broadly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26c5ec7a-74bc-48da-96c7-b3a2f055f03a",
  "uuid": "582572f4-f85e-4187-a55a-819722790a60",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QoxvB2ug7ZykoEAhzQXowP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2734,
      "cache_read_input_tokens": 25174,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2734
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

_source line 15_

Seed 1 的 registry 查询没命中，换个方式查。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26c5ec7a-74bc-48da-96c7-b3a2f055f03a",
  "uuid": "e0a92a22-c679-4856-be39-300b5a999434",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QoxvB2ug7ZykoEAhzQXowP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2734,
      "cache_read_input_tokens": 25174,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2734
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01H1k8tNVXCEZmbseMYFo5Hq`</summary>

```json
{
  "project": "contrastive_entrain_calib",
  "limit": 20,
  "fields": [
    "exp_id",
    "metrics",
    "conclusion",
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
  "session_id": "26c5ec7a-74bc-48da-96c7-b3a2f055f03a",
  "uuid": "baec637b-476a-4403-a272-05b5c4111f2c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QoxvB2ug7ZykoEAhzQXowP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2734,
      "cache_read_input_tokens": 25174,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2734
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

_source line 17 · 2026-05-22T17:04:46.481Z_

<details><summary>↩ Tool result · `toolu_01H1k8tNVXCEZmbseMYFo5Hq`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp-003-eval-s2-ckpt8000\": {\"status\": \"ANALYZING\"}, \"exp-004-s2-eval-ckpt4000\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"SYCONScore\": 0.2061, \"ToF\": 0.116, \"NoF\": 0.9227, \"n_valid\": 181, \"n_total\": 362}}, \"exp-003-len512\": {\"status\": \"PREPARING\", \"conclusion\": \"killed\"}, \"exp-004-reduced-lora\": {\"status\": \"RUNNING\"}, \"exp-004-s2-eval-ckpt3500\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp-003-s3\": {\"status\": \"QUEUED\", \"conclusion\": \"killed\"}, \"exp-002v3-gs8\": {\"status\": \"PREPARING\", \"conclusion\": \"killed\"}, \"exp-004-s2-v2\": {\"status\": \"RUNNING\"}, \"exp-003-gs8\": {\"status\": \"RUNNING\"}, \"exp-003-s2\": {\"status\": \"ANALYZING\", \"conclusion\": \"success\"}, \"exp-003-eval-s2-ckpt7500\": {\"status\": \"RUNNING\"}, \"exp-004-s2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp-004-s2-eval-ckpt2500\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp-004-s2-eval-ckpt2000\": {\"status\": \"DONE\", \"metrics\": {\"sycon_score\": 0.2139, \"tof\": 0.1215, \"nof\": 0.8895, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362}, \"conclusion\": \"success\"}, \"exp-003-eval-s2-ckpt7000\": {\"status\": \"DONE\", \"metrics\": {\"sycon_score\": 0.0945, \"tof\": 0.0497, \"nof\": 0.9503, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362}, \"conclusion\": \"negative\"}, \"exp-004-s2-eval-ckpt1500\": {\"status\": \"DONE\", \"metrics\": {\"sycon_score\": 0.2137, \"tof\": 0.1215, \"nof\": 0.884, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362}, \"conclusion\": \"success\"}, \"exp-004-s2-eval-ckpt1000\": {\"status\": \"DONE\", \"metrics\": {\"sycon_score\": 0.2564, \"tof\": 0.1492, \"nof\": 0.9116, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362}, \"conclusion\": \"success\"}, \"exp-004-s2-eval-ckpt500\": {\"status\": \"DONE\", \"metrics\": {\"sycon_score\": 0.2232, \"tof\": 0.1271, \"nof\": 0.9171, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362}, \"conclusion\": \"success\"}, \"exp-003-eval-s2-ckpt6500\": {\"status\": \"DONE\", \"metrics\": {\"sycon_score\": 0.1046, \"tof\": 0.0552, \"nof\": 0.9779, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362}, \"conclusion\": \"negative\"}, \"exp-003-eval-s2-ckpt6000\": {\"status\": \"DONE\", \"metrics\": {\"sycon_score\": 0.0945, \"tof\": 0.0497, \"nof\": 0.9503, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362}, \"conclusion\": \"success\"}}, \"count\": 20, \"total\": 86, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2384}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26c5ec7a-74bc-48da-96c7-b3a2f055f03a",
  "uuid": "fa64d8f2-c842-4db4-8706-1deaf92c2850",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"exp-003-eval-s2-ckpt8000\\\": {\\\"status\\\": \\\"ANALYZING\\\"}, \\\"exp-004-s2-eval-ckpt4000\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"SYCONScore\\\": 0.2061, \\\"ToF\\\": 0.116, \\\"NoF\\\": 0.9227, \\\"n_valid\\\": 181, \\\"n_total\\\": 362}}, \\\"exp-003-len512\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"exp-004-reduced-lora\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"exp-004-s2-eval-ckpt3500\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp-003-s3\\\": {\\\"status\\\": \\\"QUEUED\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"exp-002v3-gs8\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"exp-004-s2-v2\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"exp-003-gs8\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"exp-003-s2\\\": {\\\"status\\\": \\\"ANALYZING\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-003-eval-s2-ckpt7500\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"exp-004-s2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp-004-s2-eval-ckpt2500\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp-004-s2-eval-ckpt2000\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"sycon_score\\\": 0.2139, \\\"tof\\\": 0.1215, \\\"nof\\\": 0.8895, \\\"n_valid\\\": 181, \\\"n_invalid\\\": 181, \\\"n_total\\\": 362}, \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-003-eval-s2-ckpt7000\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"sycon_score\\\": 0.0945, \\\"tof\\\": 0.0497, \\\"nof\\\": 0.9503, \\\"n_valid\\\": 181, \\\"n_invalid\\\": 181, \\\"n_total\\\": 362}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-004-s2-eval-ckpt1500\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"sycon_score\\\": 0.2137, \\\"tof\\\": 0.1215, \\\"nof\\\": 0.884, \\\"n_valid\\\": 181, \\\"n_invalid\\\": 181, \\\"n_total\\\": 362}, \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-004-s2-eval-ckpt1000\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"sycon_score\\\": 0.2564, \\\"tof\\\": 0.1492, \\\"nof\\\": 0.9116, \\\"n_valid\\\": 181, \\\"n_invalid\\\": 181, \\\"n_total\\\": 362}, \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-004-s2-eval-ckpt500\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"sycon_score\\\": 0.2232, \\\"tof\\\": 0.1271, \\\"nof\\\": 0.9171, \\\"n_valid\\\": 181, \\\"n_invalid\\\": 181, \\\"n_total\\\": 362}, \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-003-eval-s2-ckpt6500\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"sycon_score\\\": 0.1046, \\\"tof\\\": 0.0552, \\\"nof\\\": 0.9779, \\\"n_valid\\\": 181, \\\"n_invalid\\\": 181, \\\"n_total\\\": 362}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-003-eval-s2-ckpt6000\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"sycon_score\\\": 0.0945, \\\"tof\\\": 0.0497, \\\"nof\\\": 0.9503, \\\"n_valid\\\": 181, \\\"n_invalid\\\": 181, \\\"n_total\\\": 362}, \\\"conclusion\\\": \\\"success\\\"}}, \\\"count\\\": 20, \\\"total\\\": 86, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.2384}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"exp-003-eval-s2-ckpt8000\": {\"status\": \"ANALYZING\"}, \"exp-004-s2-eval-ckpt4000\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"SYCONScore\": 0.2061, \"ToF\": 0.116, \"NoF\": 0.9227, \"n_valid\": 181, \"n_total\": 362}}, \"exp-003-len512\": {\"status\": \"PREPARING\", \"conclusion\": \"killed\"}, \"exp-004-reduced-lora\": {\"status\": \"RUNNING\"}, \"exp-004-s2-eval-ckpt3500\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp-003-s3\": {\"status\": \"QUEUED\", \"conclusion\": \"killed\"}, \"exp-002v3-gs8\": {\"status\": \"PREPARING\", \"conclusion\": \"killed\"}, \"exp-004-s2-v2\": {\"status\": \"RUNNING\"}, \"exp-003-gs8\": {\"status\": \"RUNNING\"}, \"exp-003-s2\": {\"status\": \"ANALYZING\", \"conclusion\": \"success\"}, \"exp-003-eval-s2-ckpt7500\": {\"status\": \"RUNNING\"}, \"exp-004-s2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp-004-s2-eval-ckpt2500\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp-004-s2-eval-ckpt2000\": {\"status\": \"DONE\", \"metrics\": {\"sycon_score\": 0.2139, \"tof\": 0.1215, \"nof\": 0.8895, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362}, \"conclusion\": \"success\"}, \"exp-003-eval-s2-ckpt7000\": {\"status\": \"DONE\", \"metrics\": {\"sycon_score\": 0.0945, \"tof\": 0.0497, \"nof\": 0.9503, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362}, \"conclusion\": \"negative\"}, \"exp-004-s2-eval-ckpt1500\": {\"status\": \"DONE\", \"metrics\": {\"sycon_score\": 0.2137, \"tof\": 0.1215, \"nof\": 0.884, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362}, \"conclusion\": \"success\"}, \"exp-004-s2-eval-ckpt1000\": {\"status\": \"DONE\", \"metrics\": {\"sycon_score\": 0.2564, \"tof\": 0.1492, \"nof\": 0.9116, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362}, \"conclusion\": \"success\"}, \"exp-004-s2-eval-ckpt500\": {\"status\": \"DONE\", \"metrics\": {\"sycon_score\": 0.2232, \"tof\": 0.1271, \"nof\": 0.9171, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362}, \"conclusion\": \"success\"}, \"exp-003-eval-s2-ckpt6500\": {\"status\": \"DONE\", \"metrics\": {\"sycon_score\": 0.1046, \"tof\": 0.0552, \"nof\": 0.9779, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362}, \"conclusion\": \"negative\"}, \"exp-003-eval-s2-ckpt6000\": {\"status\": \"DONE\", \"metrics\": {\"sycon_score\": 0.0945, \"tof\": 0.0497, \"nof\": 0.9503, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362}, \"conclusion\": \"success\"}}, \"count\": 20, \"total\": 86, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2384}}"
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
I need to find the seed 1 ckpt-8000 eval. Let me search for it - it might be named differently. Let me look for "exp-003-eval-ckpt8000" or similar.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26c5ec7a-74bc-48da-96c7-b3a2f055f03a",
  "uuid": "4aea96a5-00aa-481c-881a-2f1e039c7fe5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HtHwKbAw4NntJdU1MHoc3V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1409,
      "cache_read_input_tokens": 27908,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1409
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01LP9zhsZ49dDcbwAHiPWf6q`</summary>

```json
{
  "project": "contrastive_entrain_calib",
  "limit": 0,
  "fields": [
    "exp_id",
    "metrics",
    "conclusion",
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
  "session_id": "26c5ec7a-74bc-48da-96c7-b3a2f055f03a",
  "uuid": "e12f174c-3165-4ec4-beec-e8e523d672b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HtHwKbAw4NntJdU1MHoc3V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1409,
      "cache_read_input_tokens": 27908,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1409
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

_source line 20 · 2026-05-22T17:04:51.895Z_

<details><summary>↩ Tool result · `toolu_01LP9zhsZ49dDcbwAHiPWf6q`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp-003-eval-s2-ckpt8000\": {\"status\": \"ANALYZING\"}, \"exp-004-s2-eval-ckpt4000\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"SYCONScore\": 0.2061, \"ToF\": 0.116, \"NoF\": 0.9227, \"n_valid\": 181, \"n_total\": 362}}, \"exp-003-len512\": {\"status\": \"PREPARING\", \"conclusion\": \"killed\"}, \"exp-004-reduced-lora\": {\"status\": \"RUNNING\"}, \"exp-004-s2-eval-ckpt3500\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp-003-s3\": {\"status\": \"QUEUED\", \"conclusion\": \"killed\"}, \"exp-002v3-gs8\": {\"status\": \"PREPARING\", \"conclusion\": \"killed\"}, \"exp-004-s2-v2\": {\"status\": \"RUNNING\"}, \"exp-003-gs8\": {\"status\": \"RUNNING\"}, \"exp-003-s2\": {\"status\": \"ANALYZING\", \"conclusion\": \"success\"}, \"exp-003-eval-s2-ckpt7500\": {\"status\": \"RUNNING\"}, \"exp-004-s2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp-004-s2-eval-ckpt2500\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp-004-s2-eval-ckpt2000\": {\"status\": \"DONE\", \"metrics\": {\"sycon_score\": 0.2139, \"tof\": 0.1215, \"nof\": 0.8895, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362}, \"conclusion\": \"success\"}, \"exp-003-eval-s2-ckpt7000\": {\"status\": \"DONE\", \"metrics\": {\"sycon_score\": 0.0945, \"tof\": 0.0497, \"nof\": 0.9503, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362}, \"conclusion\": \"negative\"}, \"exp-004-s2-eval-ckpt1500\": {\"status\": \"DONE\", \"metrics\": {\"sycon_score\": 0.2137, \"tof\": 0.1215, \"nof\": 0.884, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362}, \"conclusion\": \"success\"}, \"exp-004-s2-eval-ckpt1000\": {\"status\": \"DONE\", \"metrics\": {\"sycon_score\": 0.2564, \"tof\": 0.1492, \"nof\": 0.9116, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362}, \"conclusion\": \"success\"}, \"exp-004-s2-eval-ckpt500\": {\"status\": \"DONE\", \"metrics\": {\"sycon_score\": 0.2232, \"tof\": 0.1271, \"nof\": 0.9171, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362}, \"conclusion\": \"success\"}, \"exp-003-eval-s2-ckpt6500\": {\"status\": \"DONE\", \"metrics\": {\"sycon_score\": 0.1046, \"tof\": 0.0552, \"nof\": 0.9779, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362}, \"conclusion\": \"negative\"}, \"exp-003-eval-s2-ckpt6000\": {\"status\": \"DONE\", \"metrics\": {\"sycon_score\": 0.0945, \"tof\": 0.0497, \"nof\": 0.9503, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362}, \"conclusion\": \"success\"}, \"exp-003-eval-s2-ckpt5500\": {\"status\": \"DONE\", \"metrics\": {\"sycon_score\": 0.1144, \"tof\": 0.0608, \"nof\": 0.9724, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362}, \"conclusion\": \"success\"}, \"exp-003-eval-s2-ckpt5000\": {\"status\": \"DONE\", \"metrics\": {\"sycon_score\": 0.1044, \"tof\": 0.0552, \"nof\": 0.9503, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362}, \"conclusion\": \"success\"}, \"exp-003-eval-s2-ckpt4500\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sycon_score\": 0.1044, \"tof\": 0.0552, \"nof\": 0.9503, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362}}, \"exp-004-eval-ckpt8000-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sycon_score\": 0.3013, \"tof\": 0.1823, \"nof\": 0.8674, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362}}, \"exp-004-eval-ckpt2000-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sycon_score\": 0.255, \"tof\": 0.1492, \"nof\": 0.8785, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362}}, \"exp-004-eval-ckpt500-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sycon_score\": 0.1699, \"tof\": 0.0939, \"nof\": 0.8895, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362}}, \"exp-003-eval-s2-ckpt4000-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sycon_score\": 0.143, \"tof\": 0.0773, \"nof\": 0.9448, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362}}, \"exp-004-eval-ckpt8000\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp-004-eval-ckpt2000\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp-004-eval-ckpt500\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp-003-eval-s2-ckpt4000\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp-003-eval-ckpt8000\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sycon_score\": 0.1433, \"tof\": 0.0773, \"nof\": 0.9724, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362}}, \"exp-003-eval-s2-ckpt3500\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sycon_score\": 0.0744, \"tof\": 0.0387, \"nof\": 0.9724, \"n_valid\": 181, \"n_invalid\": 181}}, \"exp-003-eval-s2-ckpt2500\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sycon_score\": 0.1046, \"tof\": 0.0552, \"nof\": 0.9724}}, \"exp-003-s2-eval-ckpt2000\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp-003-s2-eval-ckpt3000\": {\"status\": \"QUEUED\", \"conclusion\": \"killed\"}, \"exp-003-s2-eval-ckpt2500\": {\"status\": \"QUEUED\", \"conclusion\": \"killed\"}, \"exp-004\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"trend\": \"generally increasing trend with oscillations: early phase ~0.17-0.25, late phase ~0.26-0.30, best=0.301 at ckpt-8000\", \"best_sycon_score\": 0.301, \"best_checkpoint\": \"ckpt-8000\"}}, \"exp-003\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp-003-eval-s2-ckpt2000\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sycon_score\": 0.0846}}, \"exp-003-eval-ckpt7500\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sycon_score\": 0.1046}}, \"exp-003-eval-ckpt7000-v3\": {\"status\": \"DONE\", \"metrics\": {\"sycon_score\": 0.1046}, \"conclusion\": \"success\"}, \"exp-003-eval-s2-ckpt3000\": {\"status\": \"DONE\", \"metrics\": {\"sycon_score\": 0.0945, \"tof\": 0.0497, \"nof\": 0.9503}, \"conclusion\": \"success\"}, \"exp-003-eval-ckpt5000-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sycon_score\": 0.1144, \"tof\": 0.0608, \"nof\": 0.9669}}, \"exp-003-eval-ckpt6500\": {\"status\": \"DONE\", \"metrics\": {\"sycon_score\": 0.1529, \"tof\": 0.0829, \"nof\": 0.9834}, \"conclusion\": \"success\"}, \"exp-003-eval-ckpt6000\": {\"status\": \"DONE\", \"metrics\": {\"sycon_score\": 0.0846, \"tof\": 0.0442, \"nof\": 0.9724}, \"conclusion\": \"success\"}, \"exp-003-eval-ckpt7000-v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp-003-eval-ckpt7000\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp-003-eval-ckpt2000\": {\"status\": \"DONE\", \"metrics\": {\"ToF\": 0.0442, \"NoF\": 0.9834, \"SYCONScore\": 0.0846, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362, \"checkpoint\": \"checkpoint-2000\", \"eval_script\": \"eval_unified_preset.py (D027 standard)\", \"eval_server\": \"westd-28034\", \"vs_vanilla\": \"SYCONScore 0.0846 vs 0.1335 = -36.6%, BELOW baseline\"}, \"conclusion\": \"negative\"}, \"exp-003-eval-ckpt3000\": {\"status\": \"DONE\", \"metrics\": {\"ToF\": 0.0497, \"NoF\": 0.9724, \"SYCONScore\": 0.0946, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362, \"checkpoint\": \"checkpoint-3000\", \"eval_script\": \"eval_unified_preset.py (D027 standard)\", \"eval_server\": \"westd-28034\", \"vs_vanilla\": \"SYCONScore 0.0946 vs 0.1335 = -29.1%, BELOW baseline\"}, \"conclusion\": \"negative\"}, \"exp-009-eval-ckpt500\": {\"status\": \"DONE\", \"metrics\": {\"ToF\": 0.0663, \"NoF\": 0.9337, \"SYCONScore\": 0.1238, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362, \"checkpoint\": \"checkpoint-500\", \"eval_script\": \"eval_unified_preset.py (D027 standard)\", \"eval_server\": \"westd-28034\", \"eval_time_sec\": 7671}, \"conclusion\": \"negative\"}, \"vanilla-d027-reeval\": {\"status\": \"DONE\", \"metrics\": {\"ToF\": 0.0718, \"NoF\": 0.9448, \"SYCONScore\": 0.1335, \"n_total\": 362, \"eval_script\": \"eval_unified_preset.py (D027 standard)\", \"eval_server\": \"westd-28034\", \"note\": \"D027 unified preset baseline. Previous eval_pipeline.py gave ToF=0.1105, NoF=0.9227, SYCONScore=0.1974 — discrepancy due to different eval scripts.\"}, \"conclusion\": \"success\"}, \"exp-003-eval-ckpt4500\": {\"status\": \"DONE\", \"metrics\": {\"ToF\": 0.0718, \"NoF\": 0.9613, \"SYCONScore\": 0.1337, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362, \"checkpoint\": \"checkpoint-4500\", \"eval_script\": \"eval_unified_preset.py (D027 standard)\", \"eval_server\": \"westd-28034\", \"eval_time_sec\": 4280, \"vs_vanilla\": \"SYCONScore 0.1337 vs 0.1335 = +0.1%, essentially EQUAL to baseline\", \"note\": \"Surprising: ckpt-4500 peaks near vanilla baseline (0.1337), HIGHER than ckpt-4000/5000/5500 (0.1144). Non-monotonic trajectory — peak at 4500 then regression.\"}, \"conclusion\": \"negative\"}, \"exp-003-s2-eval-ckpt1500\": {\"status\": \"DONE\", \"metrics\": {\"ToF\": 0.0552, \"NoF\": 0.9503, \"SYCONScore\": 0.1044, \"samples\": 362}, \"conclusion\": \"negative\"}, \"exp-003-s2-eval-ckpt1000\": {\"status\": \"DONE\", \"metrics\": {\"ToF\": 0.0442, \"NoF\": 0.9448, \"SYCONScore\": 0.0844, \"samples\": 362}, \"conclusion\": \"negative\"}, \"exp-003-s2-eval-ckpt500\": {\"status\": \"DONE\", \"metrics\": {\"ToF\": 0.0442, \"NoF\": 0.9503, \"SYCONScore\": 0.0845, \"samples\": 362}, \"conclusion\": \"negative\"}, \"exp-003-eval-ckpt5500\": {\"status\": \"DONE\", \"metrics\": {\"ToF\": 0.0608, \"NoF\": 0.9724, \"SYCONScore\": 0.1144, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362, \"checkpoint\": \"checkpoint-5500\", \"eval_script\": \"eval_unified_preset.py (D027 standard)\", \"eval_server\": \"westd-28034\", \"eval_time_sec\": 4484, \"vs_vanilla\": \"SYCONScore 0.1144 vs 0.1335 = -14.3%, BELOW baseline\", \"note\": \"Identical to ckpt-4000/5000 — plateau confirmed at 3 consecutive checkpoints\"}, \"conclusion\": \"negative\"}, \"exp-004-eval-ckpt5500\": {\"status\": \"DONE\", \"metrics\": {\"ToF\": 0.1381, \"NoF\": 0.8674, \"SYCONScore\": 0.2383, \"n_samples\": 362}, \"conclusion\": \"success\"}, \"exp-004-eval-ckpt4500\": {\"status\": \"DONE\", \"metrics\": {\"ToF\": 0.105, \"NoF\": 0.8785, \"SYCONScore\": 0.1875, \"n_samples\": 362}, \"conclusion\": \"success\"}, \"exp-004-eval-ckpt7500\": {\"status\": \"DONE\", \"metrics\": {\"ToF\": 0.1657, \"NoF\": 0.8453, \"SYCONScore\": 0.2771, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362, \"checkpoint\": \"checkpoint-7500\", \"eval_script\": \"eval_unified_preset.py (D027 standard)\", \"eval_server\": \"westd-28034\", \"vs_vanilla\": \"SYCONScore 0.2771 vs 0.1335 = +107.6%\"}, \"conclusion\": \"success\"}, \"exp-004-eval-ckpt6500\": {\"status\": \"DONE\", \"metrics\": {\"ToF\": 0.1492, \"NoF\": 0.8232, \"SYCONScore\": 0.2526, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362, \"checkpoint\": \"checkpoint-6500\", \"eval_script\": \"eval_unified_preset.py (D027 standard)\", \"eval_server\": \"westd-28034\", \"vs_vanilla\": \"SYCONScore 0.2526 vs 0.1335 = +89.1%\"}, \"conclusion\": \"success\"}, \"exp-009-eval-ckpt1000\": {\"status\": \"DONE\", \"metrics\": {\"ToF\": 0.0608, \"NoF\": 0.9337, \"SYCONScore\": 0.1141, \"n_total\": 362, \"checkpoint\": \"checkpoint-1000\", \"eval_script\": \"eval_unified_preset.py (D027 standard)\", \"eval_server\": \"westd-28034\", \"trend_vs_ckpt500\": \"ToF 0.0663→0.0608 (↓8.3%), SYCONScore 0.1238→0.1141 (↓7.8%)\"}, \"conclusion\": \"negative\"}, \"exp-004-eval-ckpt1500\": {\"status\": \"DONE\", \"metrics\": {\"ToF\": 0.0939, \"NoF\": 0.8895, \"SYCONScore\": 0.1699, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362, \"checkpoint\": \"checkpoint-1500\", \"eval_script\": \"eval_unified_preset.py (D027 standard)\", \"eval_server\": \"westd-28034\", \"eval_time_sec\": 1741, \"vs_vanilla\": \"SYCONScore 0.1699 vs 0.1335 = +27.3%\"}, \"conclusion\": \"success\"}, \"exp-004-eval-ckpt3500\": {\"status\": \"DONE\", \"metrics\": {\"ToF\": 0.1326, \"NoF\": 0.9006, \"SYCONScore\": 0.2312, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362, \"checkpoint\": \"checkpoint-3500\", \"eval_script\": \"eval_unified_preset.py (D027 standard)\", \"eval_server\": \"westd-28034\", \"vs_vanilla\": \"SYCONScore 0.2312 vs 0.1335 = +73.2%\"}, \"conclusion\": \"success\"}, \"exp-004-eval-ckpt2500\": {\"status\": \"DONE\", \"metrics\": {\"ToF\": 0.1381, \"NoF\": 0.884, \"SYCONScore\": 0.2389, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362, \"checkpoint\": \"checkpoint-2500\", \"eval_script\": \"eval_unified_preset.py (D027 standard)\", \"eval_server\": \"westd-28034\", \"vs_vanilla\": \"SYCONScore 0.2389 vs 0.1335 = +78.9%\"}, \"conclusion\": \"success\"}, \"exp-003-eval-ckpt4000\": {\"status\": \"DONE\", \"metrics\": {\"ToF\": 0.0608, \"NoF\": 0.9669, \"SYCONScore\": 0.1144, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362, \"checkpoint\": \"checkpoint-4000\", \"eval_script\": \"eval_unified_preset.py (D027 standard)\", \"eval_server\": \"westd-28034\", \"eval_time_sec\": 4353, \"vs_vanilla\": \"SYCONScore 0.1144 vs 0.1335 = -14.3%, BELOW baseline\", \"note\": \"Identical to ckpt-5000 — model saturated at step 4000\"}, \"conclusion\": \"negative\"}, \"exp-004-eval-ckpt3000\": {\"status\": \"DONE\", \"metrics\": {\"ToF\": 0.116, \"NoF\": 0.9116, \"SYCONScore\": 0.2058, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362, \"checkpoint\": \"checkpoint-3000\", \"eval_script\": \"eval_unified_preset.py (D027 standard)\", \"eval_server\": \"westd-28034\", \"vs_vanilla\": \"SYCONScore 0.2058 vs 0.1335 = +54.2%\"}, \"conclusion\": \"success\"}, \"exp-004-eval-ckpt5000\": {\"status\": \"DONE\", \"metrics\": {\"ToF\": 0.1547, \"NoF\": 0.8785, \"SYCONScore\": 0.2631, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362, \"checkpoint\": \"checkpoint-5000\", \"eval_script\": \"eval_unified_preset.py (D027 standard)\", \"eval_server\": \"westd-28034\", \"eval_time_sec\": 1305, \"vs_vanilla\": \"SYCONScore 0.2631 vs 0.1335 = +97.1%\"}, \"conclusion\": \"success\"}, \"exp-004-eval-ckpt7000\": {\"status\": \"DONE\", \"metrics\": {\"ToF\": 0.1713, \"NoF\": 0.8619, \"SYCONScore\": 0.2858, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362, \"checkpoint\": \"checkpoint-7000\", \"eval_script\": \"eval_unified_preset.py (D027 standard)\", \"eval_server\": \"westd-28034\", \"eval_time_sec\": 1254, \"vs_vanilla\": \"SYCONScore 0.2858 vs 0.1335 = +114.1%\"}, \"conclusion\": \"success\"}, \"exp-004-eval-ckpt1000\": {\"status\": \"DONE\", \"metrics\": {\"ToF\": 0.116, \"NoF\": 0.8729, \"SYCONScore\": 0.2048, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362, \"checkpoint\": \"checkpoint-1000\", \"eval_script\": \"eval_unified_preset.py (D027 standard)\", \"eval_server\": \"westd-28034\", \"eval_time_sec\": 1689, \"vs_vanilla\": \"SYCONScore 0.2048 vs 0.1335 = +53.4%\"}, \"conclusion\": \"success\"}, \"exp-004-eval-ckpt4000\": {\"status\": \"DONE\", \"metrics\": {\"ToF\": 0.1215, \"NoF\": 0.895, \"SYCONScore\": 0.214, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362, \"checkpoint\": \"checkpoint-4000\", \"eval_script\": \"eval_unified_preset.py (D027 standard)\", \"eval_server\": \"westd-28034\", \"vs_vanilla\": \"SYCONScore 0.2140 vs 0.1335 = +60.3%, ABOVE baseline (dip vs ckpt-2000)\"}, \"conclusion\": \"success\"}, \"exp-004-eval-ckpt6000\": {\"status\": \"DONE\", \"metrics\": {\"ToF\": 0.1547, \"NoF\": 0.8508, \"SYCONScore\": 0.2618, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362, \"checkpoint\": \"checkpoint-6000\", \"eval_script\": \"eval_unified_preset.py (D027 standard)\", \"eval_server\": \"westd-28034\", \"vs_vanilla\": \"SYCONScore 0.2618 vs 0.1335 = +96.1%, ABOVE baseline\"}, \"conclusion\": \"success\"}, \"exp-003-eval-ckpt1000\": {\"status\": \"DONE\", \"metrics\": {\"ToF\": 0.0387, \"NoF\": 0.9448, \"SYCONScore\": 0.0743, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362, \"eval_time_s\": 4319, \"checkpoint\": \"checkpoint-1000\", \"eval_script\": \"eval_unified_preset.py (D027 standard)\", \"eval_server\": \"westd-28034\"}, \"conclusion\": \"negative\"}, \"exp-003-eval-ckpt5000\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"ToF\": 0.0608, \"NoF\": 0.9669, \"SYCONScore\": 0.1144, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362, \"checkpoint\": \"checkpoint-5000\", \"eval_script\": \"eval_unified_preset.py (D027 standard)\", \"eval_server\": \"westd-28034\", \"eval_time_sec\": 5146, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/exp003/checkpoint-5000\", \"log_path\": \"/root/autodl-tmp/results/exp003_unified_eval/\", \"vs_vanilla\": \"SYCONScore 0.1144 vs 0.1335 = -14.3%, BELOW baseline\"}}, \"exp-009\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"eval_ckpt500\": {\"ToF\": 0.0663, \"NoF\": 0.9337, \"SYCONScore\": 0.1238}, \"eval_ckpt1000\": {\"ToF\": 0.0608, \"NoF\": 0.9337, \"SYCONScore\": 0.1141}, \"trend\": \"monotonic decline: ckpt-500→ckpt-1000 ToF ↓8.3%, SYCONScore ↓7.8%\", \"vanilla_d027_baseline\": {\"SYCONScore\": 0.1335}, \"kill_reason\": \"D040: all three R1 formulations (cosine/binary/continuous_probability) failed. Completes ALL-formulations-fail argument.\", \"available_checkpoints\": [\"checkpoint-500\", \"checkpoint-1000\"]}}, \"exp-012\": {\"status\": \"DONE\", \"metrics\": {\"cv_auroc_mean\": 0.7793, \"cv_auroc_std\": 0.0189, \"full_auroc\": 0.7779, \"best_layer\": 16, \"style_controlled_auroc\": 0.9227, \"per_layer_auroc_top5\": {\"16\": 0.7793, \"22\": 0.7359, \"25\": 0.7372, \"26\": 0.7374, \"31\": 0.747}, \"domain_auroc\": {\"commonsense\": 0.8444, \"history\": 0.818, \"math\": 0.769, \"science\": 0.7546, \"geography\": 0.7507}, \"evidence_strength_auroc\": {\"strong\": 0.9109, \"medium\": 0.8635, \"weak\": 0.7106}, \"num_pairs\": 181, \"num_samples\": 362, \"layer_range\": [16, 31], \"probe_ablation\": {\"d_syc_best_layer_auroc\": 0.778, \"d_syc_multi_layer_auroc\": 0.813, \"random_direction_auroc_mean\": 0.53, \"random_direction_auroc_std\": 0.054, \"gap_d_syc_minus_random\": 0.248, \"qwen_comparison\": {\"qwen_d_syc\": 0.835, \"qwen_random\": 0.727, \"qwen_gap\": 0.108}, \"finding\": \"Llama gap (+0.248) larger than Qwen (+0.108). Random direction near chance (0.53) on Llama vs 0.73 on Qwen — sycophancy signal more concentrated in specific directions on Llama.\"}}, \"conclusion\": \"success\"}, \"exp-002v3\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"collapse_timeline\": {\"phase1_length_collapse\": \"step 100-300, mean_len 247→80, entropy 0.45→0.10\", \"low_entropy_plateau\": \"step 300-2150, entropy 0.07-0.10\", \"phase2_terminal_collapse\": \"step 2160, entropy 0.056→0.026 in 50 steps, frac_zero_std 0.125→0.419\", \"critical_step\": 2160}, \"entropy_at_kill\": 0.006, \"grad_norm_at_kill\": 0, \"frac_reward_zero_std_peak\": 0.963, \"r3_saturation_step\": 100, \"r3_saturated_value\": 0.9998, \"r1_behavior\": \"mean oscillated -0.46 to +0.41, no sustained positive trend despite 5x scaling\", \"available_checkpoints\": [\"checkpoint-500\", \"checkpoint-1000\", \"checkpoint-1500\", \"checkpoint-2000\"], \"best_checkpoint_before_collapse\": \"checkpoint-2000 (entropy ~0.062, still in plateau)\", \"root_cause\": \"R3 saturated at step 100 → combined reward degenerates to only R1 → cosine R1 signal too noisy (high variance) to provide stable optimization direction. Problem is R1 noise, not R1 magnitude — 5x scaling amplified noise proportionally.\", \"conclusion_reason\": \"GRPO mode collapse: R3 early saturation + cosine R1 high-variance noise = no effective learning signal. Confirms scaled cosine R1 also structurally fails.\"}}, \"exp-008v3\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"preset_eval_ckpt500\": {\"ToF\": 0, \"NoF\": 0.9945, \"SYCONScore\": 0, \"n_total\": 362, \"checkpoint\": \"checkpoint-500\", \"eval_script\": \"eval_unified_preset.py (D027 standard)\", \"eval_server\": \"westd-28034\", \"eval_time_sec\": 6502}, \"preset_eval_ckpt1000\": {\"ToF\": 0.0055, \"NoF\": 0.9945, \"SYCONScore\": 0.011, \"n_total\": 362, \"checkpoint\": \"checkpoint-1000\", \"eval_script\": \"eval_unified_preset.py (D027 standard)\", \"eval_server\": \"westd-28034\", \"eval_time_sec\": 6726}, \"preset_eval_ckpt1500\": {\"ToF\": 0, \"NoF\": 1, \"SYCONScore\": 0, \"eval_server\": \"westd-29046\"}, \"preset_eval_ckpt2000\": {\"ToF\": 0, \"NoF\": 1, \"SYCONScore\": 0, \"eval_server\": \"westd-29046\"}, \"stubbornness_onset\": \"immediate — ToF=0 at ckpt-500, probe reward trap activates within first 500 training steps\", \"trajectory\": \"ckpt-500 ToF=0.000 → ckpt-1000 ToF=0.006 → ckpt-1500 ToF=0.000 → ckpt-2000 ToF=0.000. Stubbornness is not gradual onset but immediate collapse.\"}}, \"exp002v2-recalib\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-016\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"alpha_0.0\": {\"NoF\": 0.6961, \"WRR\": 0.2707}, \"alpha_0.5\": {\"NoF\": 0.6906, \"WRR\": 0.2541}, \"alpha_1.0\": {\"NoF\": 0.7127, \"WRR\": 0.2652}, \"alpha_2.0\": {\"NoF\": 0.6851, \"WRR\": 0.2541}, \"alpha_5.0\": {\"NoF\": 0.7845, \"WRR\": 0.2155}, \"best_alpha\": 5, \"best_NoF_delta\": \"+8.8pp\", \"D027_note\": \"D027 unified eval reversal: alpha=5 SYCONScore=0.054 < vanilla SYCONScore=0.134. ActAdd improves NoF but destroys ToF, net negative under NLI-based SYCONScore.\", \"conclusion_reason\": \"D027 eval reversal: ActAdd alpha=5 SYCONScore 0.054 worse than vanilla 0.134\", \"unified_reeval_D027\": {\"alpha_0.0\": {\"ToF\": 0.0718, \"NoF\": 0.9448, \"SYCONScore\": 0.1335}, \"alpha_0.5\": {\"ToF\": 0.0718, \"NoF\": 0.9392, \"SYCONScore\": 0.1334}, \"alpha_1.0\": {\"ToF\": 0.0442, \"NoF\": 0.9724, \"SYCONScore\": 0.0846}, \"alpha_2.0\": {\"ToF\": 0.0276, \"NoF\": 0.9669, \"SYCONScore\": 0.0537}, \"alpha_5.0\": {\"ToF\": 0.0276, \"NoF\": 0.9613, \"SYCONScore\": 0.0537}, \"eval_server\": \"westd-28034\", \"eval_results_path\": \"/root/contrastive_entrain_calib/results/exp016_unified_reeval/\"}}}, \"exp-014\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"metrics\": {\"preset_eval_ckpt3000\": {\"ToF\": 0.978, \"NoF\": 0.006, \"SYCONScore\": 0.011, \"RC_AUC\": 0.195, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362, \"checkpoint\": \"checkpoint-3000\", \"eval_script\": \"run_exp014_eval.sh (preset, NLI-based)\", \"eval_time_sec\": 1179}, \"diagnosis\": \"mode_collapse: model flips on ALL pressure (valid+invalid), NoF≈0. Consistent with training R3=0.999, entropy=0.025.\"}}, \"vanilla-baseline\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"ToF\": 0.1105, \"NoF\": 0.9227, \"sycon_score\": 0.1974, \"samples\": 362, \"avg_flip_turn_valid\": 1, \"avg_flip_count_invalid\": 0.08, \"eval_script\": \"eval_pipeline.py (28034, missing regex postprocess)\", \"note\": \"28034 version missing regex &lt;think> cleanup, may need re-eval after sync\"}}, \"exp-002v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp-002\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp-008\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp-001\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"cv_auroc_mean\": 0.8269, \"cv_auroc_std\": 0.0278, \"full_auroc\": 0.8159, \"bootstrap_ci_95\": [0.7698, 0.8589], \"best_layer\": 19, \"auroc_weak\": 0.675, \"auroc_medium\": 0.883, \"auroc_strong\": 0.929, \"num_pairs\": 181, \"stop_gate\": \"CONTINUE_REDUCED_R1\"}}}, \"count\": 86, \"total\": 86, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2295}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26c5ec7a-74bc-48da-96c7-b3a2f055f03a",
  "uuid": "10c3a2e3-15ae-4838-a91b-59e392ea45e7",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"exp-003-eval-s2-ckpt8000\\\": {\\\"status\\\": \\\"ANALYZING\\\"}, \\\"exp-004-s2-eval-ckpt4000\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"SYCONScore\\\": 0.2061, \\\"ToF\\\": 0.116, \\\"NoF\\\": 0.9227, \\\"n_valid\\\": 181, \\\"n_total\\\": 362}}, \\\"exp-003-len512\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"exp-004-reduced-lora\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"exp-004-s2-eval-ckpt3500\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp-003-s3\\\": {\\\"status\\\": \\\"QUEUED\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"exp-002v3-gs8\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"exp-004-s2-v2\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"exp-003-gs8\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"exp-003-s2\\\": {\\\"status\\\": \\\"ANALYZING\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-003-eval-s2-ckpt7500\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"exp-004-s2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp-004-s2-eval-ckpt2500\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp-004-s2-eval-ckpt2000\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"sycon_score\\\": 0.2139, \\\"tof\\\": 0.1215, \\\"nof\\\": 0.8895, \\\"n_valid\\\": 181, \\\"n_invalid\\\": 181, \\\"n_total\\\": 362}, \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-003-eval-s2-ckpt7000\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"sycon_score\\\": 0.0945, \\\"tof\\\": 0.0497, \\\"nof\\\": 0.9503, \\\"n_valid\\\": 181, \\\"n_invalid\\\": 181, \\\"n_total\\\": 362}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-004-s2-eval-ckpt1500\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"sycon_score\\\": 0.2137, \\\"tof\\\": 0.1215, \\\"nof\\\": 0.884, \\\"n_valid\\\": 181, \\\"n_invalid\\\": 181, \\\"n_total\\\": 362}, \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-004-s2-eval-ckpt1000\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"sycon_score\\\": 0.2564, \\\"tof\\\": 0.1492, \\\"nof\\\": 0.9116, \\\"n_valid\\\": 181, \\\"n_invalid\\\": 181, \\\"n_total\\\": 362}, \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-004-s2-eval-ckpt500\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"sycon_score\\\": 0.2232, \\\"tof\\\": 0.1271, \\\"nof\\\": 0.9171, \\\"n_valid\\\": 181, \\\"n_invalid\\\": 181, \\\"n_total\\\": 362}, \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-003-eval-s2-ckpt6500\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"sycon_score\\\": 0.1046, \\\"tof\\\": 0.0552, \\\"nof\\\": 0.9779, \\\"n_valid\\\": 181, \\\"n_invalid\\\": 181, \\\"n_total\\\": 362}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-003-eval-s2-ckpt6000\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"sycon_score\\\": 0.0945, \\\"tof\\\": 0.0497, \\\"nof\\\": 0.9503, \\\"n_valid\\\": 181, \\\"n_invalid\\\": 181, \\\"n_total\\\": 362}, \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-003-eval-s2-ckpt5500\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"sycon_score\\\": 0.1144, \\\"tof\\\": 0.0608, \\\"nof\\\": 0.9724, \\\"n_valid\\\": 181, \\\"n_invalid\\\": 181, \\\"n_total\\\": 362}, \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-003-eval-s2-ckpt5000\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"sycon_score\\\": 0.1044, \\\"tof\\\": 0.0552, \\\"nof\\\": 0.9503, \\\"n_valid\\\": 181, \\\"n_invalid\\\": 181, \\\"n_total\\\": 362}, \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-003-eval-s2-ckpt4500\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"sycon_score\\\": 0.1044, \\\"tof\\\": 0.0552, \\\"nof\\\": 0.9503, \\\"n_valid\\\": 181, \\\"n_invalid\\\": 181, \\\"n_total\\\": 362}}, \\\"exp-004-eval-ckpt8000-v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"sycon_score\\\": 0.3013, \\\"tof\\\": 0.1823, \\\"nof\\\": 0.8674, \\\"n_valid\\\": 181, \\\"n_invalid\\\": 181, \\\"n_total\\\": 362}}, \\\"exp-004-eval-ckpt2000-v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"sycon_score\\\": 0.255, \\\"tof\\\": 0.1492, \\\"nof\\\": 0.8785, \\\"n_valid\\\": 181, \\\"n_invalid\\\": 181, \\\"n_total\\\": 362}}, \\\"exp-004-eval-ckpt500-v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"sycon_score\\\": 0.1699, \\\"tof\\\": 0.0939, \\\"nof\\\": 0.8895, \\\"n_valid\\\": 181, \\\"n_invalid\\\": 181, \\\"n_total\\\": 362}}, \\\"exp-003-eval-s2-ckpt4000-v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"sycon_score\\\": 0.143, \\\"tof\\\": 0.0773, \\\"nof\\\": 0.9448, \\\"n_valid\\\": 181, \\\"n_invalid\\\": 181, \\\"n_total\\\": 362}}, \\\"exp-004-eval-ckpt8000\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp-004-eval-ckpt2000\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp-004-eval-ckpt500\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp-003-eval-s2-ckpt4000\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp-003-eval-ckpt8000\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"sycon_score\\\": 0.1433, \\\"tof\\\": 0.0773, \\\"nof\\\": 0.9724, \\\"n_valid\\\": 181, \\\"n_invalid\\\": 181, \\\"n_total\\\": 362}}, \\\"exp-003-eval-s2-ckpt3500\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"sycon_score\\\": 0.0744, \\\"tof\\\": 0.0387, \\\"nof\\\": 0.9724, \\\"n_valid\\\": 181, \\\"n_invalid\\\": 181}}, \\\"exp-003-eval-s2-ckpt2500\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"sycon_score\\\": 0.1046, \\\"tof\\\": 0.0552, \\\"nof\\\": 0.9724}}, \\\"exp-003-s2-eval-ckpt2000\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"exp-003-s2-eval-ckpt3000\\\": {\\\"status\\\": \\\"QUEUED\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"exp-003-s2-eval-ckpt2500\\\": {\\\"status\\\": \\\"QUEUED\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"exp-004\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"trend\\\": \\\"generally increasing trend with oscillations: early phase ~0.17-0.25, late phase ~0.26-0.30, best=0.301 at ckpt-8000\\\", \\\"best_sycon_score\\\": 0.301, \\\"best_checkpoint\\\": \\\"ckpt-8000\\\"}}, \\\"exp-003\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-003-eval-s2-ckpt2000\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"sycon_score\\\": 0.0846}}, \\\"exp-003-eval-ckpt7500\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"sycon_score\\\": 0.1046}}, \\\"exp-003-eval-ckpt7000-v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"sycon_score\\\": 0.1046}, \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-003-eval-s2-ckpt3000\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"sycon_score\\\": 0.0945, \\\"tof\\\": 0.0497, \\\"nof\\\": 0.9503}, \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-003-eval-ckpt5000-v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"sycon_score\\\": 0.1144, \\\"tof\\\": 0.0608, \\\"nof\\\": 0.9669}}, \\\"exp-003-eval-ckpt6500\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"sycon_score\\\": 0.1529, \\\"tof\\\": 0.0829, \\\"nof\\\": 0.9834}, \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-003-eval-ckpt6000\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"sycon_score\\\": 0.0846, \\\"tof\\\": 0.0442, \\\"nof\\\": 0.9724}, \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-003-eval-ckpt7000-v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp-003-eval-ckpt7000\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp-003-eval-ckpt2000\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ToF\\\": 0.0442, \\\"NoF\\\": 0.9834, \\\"SYCONScore\\\": 0.0846, \\\"n_valid\\\": 181, \\\"n_invalid\\\": 181, \\\"n_total\\\": 362, \\\"checkpoint\\\": \\\"checkpoint-2000\\\", \\\"eval_script\\\": \\\"eval_unified_preset.py (D027 standard)\\\", \\\"eval_server\\\": \\\"westd-28034\\\", \\\"vs_vanilla\\\": \\\"SYCONScore 0.0846 vs 0.1335 = -36.6%, BELOW baseline\\\"}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-003-eval-ckpt3000\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ToF\\\": 0.0497, \\\"NoF\\\": 0.9724, \\\"SYCONScore\\\": 0.0946, \\\"n_valid\\\": 181, \\\"n_invalid\\\": 181, \\\"n_total\\\": 362, \\\"checkpoint\\\": \\\"checkpoint-3000\\\", \\\"eval_script\\\": \\\"eval_unified_preset.py (D027 standard)\\\", \\\"eval_server\\\": \\\"westd-28034\\\", \\\"vs_vanilla\\\": \\\"SYCONScore 0.0946 vs 0.1335 = -29.1%, BELOW baseline\\\"}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-009-eval-ckpt500\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ToF\\\": 0.0663, \\\"NoF\\\": 0.9337, \\\"SYCONScore\\\": 0.1238, \\\"n_valid\\\": 181, \\\"n_invalid\\\": 181, \\\"n_total\\\": 362, \\\"checkpoint\\\": \\\"checkpoint-500\\\", \\\"eval_script\\\": \\\"eval_unified_preset.py (D027 standard)\\\", \\\"eval_server\\\": \\\"westd-28034\\\", \\\"eval_time_sec\\\": 7671}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"vanilla-d027-reeval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ToF\\\": 0.0718, \\\"NoF\\\": 0.9448, \\\"SYCONScore\\\": 0.1335, \\\"n_total\\\": 362, \\\"eval_script\\\": \\\"eval_unified_preset.py (D027 standard)\\\", \\\"eval_server\\\": \\\"westd-28034\\\", \\\"note\\\": \\\"D027 unified preset baseline. Previous eval_pipeline.py gave ToF=0.1105, NoF=0.9227, SYCONScore=0.1974 — discrepancy due to different eval scripts.\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-003-eval-ckpt4500\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ToF\\\": 0.0718, \\\"NoF\\\": 0.9613, \\\"SYCONScore\\\": 0.1337, \\\"n_valid\\\": 181, \\\"n_invalid\\\": 181, \\\"n_total\\\": 362, \\\"checkpoint\\\": \\\"checkpoint-4500\\\", \\\"eval_script\\\": \\\"eval_unified_preset.py (D027 standard)\\\", \\\"eval_server\\\": \\\"westd-28034\\\", \\\"eval_time_sec\\\": 4280, \\\"vs_vanilla\\\": \\\"SYCONScore 0.1337 vs 0.1335 = +0.1%, essentially EQUAL to baseline\\\", \\\"note\\\": \\\"Surprising: ckpt-4500 peaks near vanilla baseline (0.1337), HIGHER than ckpt-4000/5000/5500 (0.1144). Non-monotonic trajectory — peak at 4500 then regression.\\\"}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-003-s2-eval-ckpt1500\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ToF\\\": 0.0552, \\\"NoF\\\": 0.9503, \\\"SYCONScore\\\": 0.1044, \\\"samples\\\": 362}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-003-s2-eval-ckpt1000\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ToF\\\": 0.0442, \\\"NoF\\\": 0.9448, \\\"SYCONScore\\\": 0.0844, \\\"samples\\\": 362}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-003-s2-eval-ckpt500\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ToF\\\": 0.0442, \\\"NoF\\\": 0.9503, \\\"SYCONScore\\\": 0.0845, \\\"samples\\\": 362}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-003-eval-ckpt5500\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ToF\\\": 0.0608, \\\"NoF\\\": 0.9724, \\\"SYCONScore\\\": 0.1144, \\\"n_valid\\\": 181, \\\"n_invalid\\\": 181, \\\"n_total\\\": 362, \\\"checkpoint\\\": \\\"checkpoint-5500\\\", \\\"eval_script\\\": \\\"eval_unified_preset.py (D027 standard)\\\", \\\"eval_server\\\": \\\"westd-28034\\\", \\\"eval_time_sec\\\": 4484, \\\"vs_vanilla\\\": \\\"SYCONScore 0.1144 vs 0.1335 = -14.3%, BELOW baseline\\\", \\\"note\\\": \\\"Identical to ckpt-4000/5000 — plateau confirmed at 3 consecutive checkpoints\\\"}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-004-eval-ckpt5500\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ToF\\\": 0.1381, \\\"NoF\\\": 0.8674, \\\"SYCONScore\\\": 0.2383, \\\"n_samples\\\": 362}, \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-004-eval-ckpt4500\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ToF\\\": 0.105, \\\"NoF\\\": 0.8785, \\\"SYCONScore\\\": 0.1875, \\\"n_samples\\\": 362}, \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-004-eval-ckpt7500\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ToF\\\": 0.1657, \\\"NoF\\\": 0.8453, \\\"SYCONScore\\\": 0.2771, \\\"n_valid\\\": 181, \\\"n_invalid\\\": 181, \\\"n_total\\\": 362, \\\"checkpoint\\\": \\\"checkpoint-7500\\\", \\\"eval_script\\\": \\\"eval_unified_preset.py (D027 standard)\\\", \\\"eval_server\\\": \\\"westd-28034\\\", \\\"vs_vanilla\\\": \\\"SYCONScore 0.2771 vs 0.1335 = +107.6%\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-004-eval-ckpt6500\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ToF\\\": 0.1492, \\\"NoF\\\": 0.8232, \\\"SYCONScore\\\": 0.2526, \\\"n_valid\\\": 181, \\\"n_invalid\\\": 181, \\\"n_total\\\": 362, \\\"checkpoint\\\": \\\"checkpoint-6500\\\", \\\"eval_script\\\": \\\"eval_unified_preset.py (D027 standard)\\\", \\\"eval_server\\\": \\\"westd-28034\\\", \\\"vs_vanilla\\\": \\\"SYCONScore 0.2526 vs 0.1335 = +89.1%\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-009-eval-ckpt1000\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ToF\\\": 0.0608, \\\"NoF\\\": 0.9337, \\\"SYCONScore\\\": 0.1141, \\\"n_total\\\": 362, \\\"checkpoint\\\": \\\"checkpoint-1000\\\", \\\"eval_script\\\": \\\"eval_unified_preset.py (D027 standard)\\\", \\\"eval_server\\\": \\\"westd-28034\\\", \\\"trend_vs_ckpt500\\\": \\\"ToF 0.0663→0.0608 (↓8.3%), SYCONScore 0.1238→0.1141 (↓7.8%)\\\"}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-004-eval-ckpt1500\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ToF\\\": 0.0939, \\\"NoF\\\": 0.8895, \\\"SYCONScore\\\": 0.1699, \\\"n_valid\\\": 181, \\\"n_invalid\\\": 181, \\\"n_total\\\": 362, \\\"checkpoint\\\": \\\"checkpoint-1500\\\", \\\"eval_script\\\": \\\"eval_unified_preset.py (D027 standard)\\\", \\\"eval_server\\\": \\\"westd-28034\\\", \\\"eval_time_sec\\\": 1741, \\\"vs_vanilla\\\": \\\"SYCONScore 0.1699 vs 0.1335 = +27.3%\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-004-eval-ckpt3500\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ToF\\\": 0.1326, \\\"NoF\\\": 0.9006, \\\"SYCONScore\\\": 0.2312, \\\"n_valid\\\": 181, \\\"n_invalid\\\": 181, \\\"n_total\\\": 362, \\\"checkpoint\\\": \\\"checkpoint-3500\\\", \\\"eval_script\\\": \\\"eval_unified_preset.py (D027 standard)\\\", \\\"eval_server\\\": \\\"westd-28034\\\", \\\"vs_vanilla\\\": \\\"SYCONScore 0.2312 vs 0.1335 = +73.2%\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-004-eval-ckpt2500\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ToF\\\": 0.1381, \\\"NoF\\\": 0.884, \\\"SYCONScore\\\": 0.2389, \\\"n_valid\\\": 181, \\\"n_invalid\\\": 181, \\\"n_total\\\": 362, \\\"checkpoint\\\": \\\"checkpoint-2500\\\", \\\"eval_script\\\": \\\"eval_unified_preset.py (D027 standard)\\\", \\\"eval_server\\\": \\\"westd-28034\\\", \\\"vs_vanilla\\\": \\\"SYCONScore 0.2389 vs 0.1335 = +78.9%\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-003-eval-ckpt4000\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ToF\\\": 0.0608, \\\"NoF\\\": 0.9669, \\\"SYCONScore\\\": 0.1144, \\\"n_valid\\\": 181, \\\"n_invalid\\\": 181, \\\"n_total\\\": 362, \\\"checkpoint\\\": \\\"checkpoint-4000\\\", \\\"eval_script\\\": \\\"eval_unified_preset.py (D027 standard)\\\", \\\"eval_server\\\": \\\"westd-28034\\\", \\\"eval_time_sec\\\": 4353, \\\"vs_vanilla\\\": \\\"SYCONScore 0.1144 vs 0.1335 = -14.3%, BELOW baseline\\\", \\\"note\\\": \\\"Identical to ckpt-5000 — model saturated at step 4000\\\"}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-004-eval-ckpt3000\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ToF\\\": 0.116, \\\"NoF\\\": 0.9116, \\\"SYCONScore\\\": 0.2058, \\\"n_valid\\\": 181, \\\"n_invalid\\\": 181, \\\"n_total\\\": 362, \\\"checkpoint\\\": \\\"checkpoint-3000\\\", \\\"eval_script\\\": \\\"eval_unified_preset.py (D027 standard)\\\", \\\"eval_server\\\": \\\"westd-28034\\\", \\\"vs_vanilla\\\": \\\"SYCONScore 0.2058 vs 0.1335 = +54.2%\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-004-eval-ckpt5000\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ToF\\\": 0.1547, \\\"NoF\\\": 0.8785, \\\"SYCONScore\\\": 0.2631, \\\"n_valid\\\": 181, \\\"n_invalid\\\": 181, \\\"n_total\\\": 362, \\\"checkpoint\\\": \\\"checkpoint-5000\\\", \\\"eval_script\\\": \\\"eval_unified_preset.py (D027 standard)\\\", \\\"eval_server\\\": \\\"westd-28034\\\", \\\"eval_time_sec\\\": 1305, \\\"vs_vanilla\\\": \\\"SYCONScore 0.2631 vs 0.1335 = +97.1%\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-004-eval-ckpt7000\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ToF\\\": 0.1713, \\\"NoF\\\": 0.8619, \\\"SYCONScore\\\": 0.2858, \\\"n_valid\\\": 181, \\\"n_invalid\\\": 181, \\\"n_total\\\": 362, \\\"checkpoint\\\": \\\"checkpoint-7000\\\", \\\"eval_script\\\": \\\"eval_unified_preset.py (D027 standard)\\\", \\\"eval_server\\\": \\\"westd-28034\\\", \\\"eval_time_sec\\\": 1254, \\\"vs_vanilla\\\": \\\"SYCONScore 0.2858 vs 0.1335 = +114.1%\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-004-eval-ckpt1000\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ToF\\\": 0.116, \\\"NoF\\\": 0.8729, \\\"SYCONScore\\\": 0.2048, \\\"n_valid\\\": 181, \\\"n_invalid\\\": 181, \\\"n_total\\\": 362, \\\"checkpoint\\\": \\\"checkpoint-1000\\\", \\\"eval_script\\\": \\\"eval_unified_preset.py (D027 standard)\\\", \\\"eval_server\\\": \\\"westd-28034\\\", \\\"eval_time_sec\\\": 1689, \\\"vs_vanilla\\\": \\\"SYCONScore 0.2048 vs 0.1335 = +53.4%\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-004-eval-ckpt4000\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ToF\\\": 0.1215, \\\"NoF\\\": 0.895, \\\"SYCONScore\\\": 0.214, \\\"n_valid\\\": 181, \\\"n_invalid\\\": 181, \\\"n_total\\\": 362, \\\"checkpoint\\\": \\\"checkpoint-4000\\\", \\\"eval_script\\\": \\\"eval_unified_preset.py (D027 standard)\\\", \\\"eval_server\\\": \\\"westd-28034\\\", \\\"vs_vanilla\\\": \\\"SYCONScore 0.2140 vs 0.1335 = +60.3%, ABOVE baseline (dip vs ckpt-2000)\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-004-eval-ckpt6000\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ToF\\\": 0.1547, \\\"NoF\\\": 0.8508, \\\"SYCONScore\\\": 0.2618, \\\"n_valid\\\": 181, \\\"n_invalid\\\": 181, \\\"n_total\\\": 362, \\\"checkpoint\\\": \\\"checkpoint-6000\\\", \\\"eval_script\\\": \\\"eval_unified_preset.py (D027 standard)\\\", \\\"eval_server\\\": \\\"westd-28034\\\", \\\"vs_vanilla\\\": \\\"SYCONScore 0.2618 vs 0.1335 = +96.1%, ABOVE baseline\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-003-eval-ckpt1000\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"ToF\\\": 0.0387, \\\"NoF\\\": 0.9448, \\\"SYCONScore\\\": 0.0743, \\\"n_valid\\\": 181, \\\"n_invalid\\\": 181, \\\"n_total\\\": 362, \\\"eval_time_s\\\": 4319, \\\"checkpoint\\\": \\\"checkpoint-1000\\\", \\\"eval_script\\\": \\\"eval_unified_preset.py (D027 standard)\\\", \\\"eval_server\\\": \\\"westd-28034\\\"}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-003-eval-ckpt5000\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"ToF\\\": 0.0608, \\\"NoF\\\": 0.9669, \\\"SYCONScore\\\": 0.1144, \\\"n_valid\\\": 181, \\\"n_invalid\\\": 181, \\\"n_total\\\": 362, \\\"checkpoint\\\": \\\"checkpoint-5000\\\", \\\"eval_script\\\": \\\"eval_unified_preset.py (D027 standard)\\\", \\\"eval_server\\\": \\\"westd-28034\\\", \\\"eval_time_sec\\\": 5146, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/exp003/checkpoint-5000\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/results/exp003_unified_eval/\\\", \\\"vs_vanilla\\\": \\\"SYCONScore 0.1144 vs 0.1335 = -14.3%, BELOW baseline\\\"}}, \\\"exp-009\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"eval_ckpt500\\\": {\\\"ToF\\\": 0.0663, \\\"NoF\\\": 0.9337, \\\"SYCONScore\\\": 0.1238}, \\\"eval_ckpt1000\\\": {\\\"ToF\\\": 0.0608, \\\"NoF\\\": 0.9337, \\\"SYCONScore\\\": 0.1141}, \\\"trend\\\": \\\"monotonic decline: ckpt-500→ckpt-1000 ToF ↓8.3%, SYCONScore ↓7.8%\\\", \\\"vanilla_d027_baseline\\\": {\\\"SYCONScore\\\": 0.1335}, \\\"kill_reason\\\": \\\"D040: all three R1 formulations (cosine/binary/continuous_probability) failed. Completes ALL-formulations-fail argument.\\\", \\\"available_checkpoints\\\": [\\\"checkpoint-500\\\", \\\"checkpoint-1000\\\"]}}, \\\"exp-012\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"cv_auroc_mean\\\": 0.7793, \\\"cv_auroc_std\\\": 0.0189, \\\"full_auroc\\\": 0.7779, \\\"best_layer\\\": 16, \\\"style_controlled_auroc\\\": 0.9227, \\\"per_layer_auroc_top5\\\": {\\\"16\\\": 0.7793, \\\"22\\\": 0.7359, \\\"25\\\": 0.7372, \\\"26\\\": 0.7374, \\\"31\\\": 0.747}, \\\"domain_auroc\\\": {\\\"commonsense\\\": 0.8444, \\\"history\\\": 0.818, \\\"math\\\": 0.769, \\\"science\\\": 0.7546, \\\"geography\\\": 0.7507}, \\\"evidence_strength_auroc\\\": {\\\"strong\\\": 0.9109, \\\"medium\\\": 0.8635, \\\"weak\\\": 0.7106}, \\\"num_pairs\\\": 181, \\\"num_samples\\\": 362, \\\"layer_range\\\": [16, 31], \\\"probe_ablation\\\": {\\\"d_syc_best_layer_auroc\\\": 0.778, \\\"d_syc_multi_layer_auroc\\\": 0.813, \\\"random_direction_auroc_mean\\\": 0.53, \\\"random_direction_auroc_std\\\": 0.054, \\\"gap_d_syc_minus_random\\\": 0.248, \\\"qwen_comparison\\\": {\\\"qwen_d_syc\\\": 0.835, \\\"qwen_random\\\": 0.727, \\\"qwen_gap\\\": 0.108}, \\\"finding\\\": \\\"Llama gap (+0.248) larger than Qwen (+0.108). Random direction near chance (0.53) on Llama vs 0.73 on Qwen — sycophancy signal more concentrated in specific directions on Llama.\\\"}}, \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-002v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"collapse_timeline\\\": {\\\"phase1_length_collapse\\\": \\\"step 100-300, mean_len 247→80, entropy 0.45→0.10\\\", \\\"low_entropy_plateau\\\": \\\"step 300-2150, entropy 0.07-0.10\\\", \\\"phase2_terminal_collapse\\\": \\\"step 2160, entropy 0.056→0.026 in 50 steps, frac_zero_std 0.125→0.419\\\", \\\"critical_step\\\": 2160}, \\\"entropy_at_kill\\\": 0.006, \\\"grad_norm_at_kill\\\": 0, \\\"frac_reward_zero_std_peak\\\": 0.963, \\\"r3_saturation_step\\\": 100, \\\"r3_saturated_value\\\": 0.9998, \\\"r1_behavior\\\": \\\"mean oscillated -0.46 to +0.41, no sustained positive trend despite 5x scaling\\\", \\\"available_checkpoints\\\": [\\\"checkpoint-500\\\", \\\"checkpoint-1000\\\", \\\"checkpoint-1500\\\", \\\"checkpoint-2000\\\"], \\\"best_checkpoint_before_collapse\\\": \\\"checkpoint-2000 (entropy ~0.062, still in plateau)\\\", \\\"root_cause\\\": \\\"R3 saturated at step 100 → combined reward degenerates to only R1 → cosine R1 signal too noisy (high variance) to provide stable optimization direction. Problem is R1 noise, not R1 magnitude — 5x scaling amplified noise proportionally.\\\", \\\"conclusion_reason\\\": \\\"GRPO mode collapse: R3 early saturation + cosine R1 high-variance noise = no effective learning signal. Confirms scaled cosine R1 also structurally fails.\\\"}}, \\\"exp-008v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"preset_eval_ckpt500\\\": {\\\"ToF\\\": 0, \\\"NoF\\\": 0.9945, \\\"SYCONScore\\\": 0, \\\"n_total\\\": 362, \\\"checkpoint\\\": \\\"checkpoint-500\\\", \\\"eval_script\\\": \\\"eval_unified_preset.py (D027 standard)\\\", \\\"eval_server\\\": \\\"westd-28034\\\", \\\"eval_time_sec\\\": 6502}, \\\"preset_eval_ckpt1000\\\": {\\\"ToF\\\": 0.0055, \\\"NoF\\\": 0.9945, \\\"SYCONScore\\\": 0.011, \\\"n_total\\\": 362, \\\"checkpoint\\\": \\\"checkpoint-1000\\\", \\\"eval_script\\\": \\\"eval_unified_preset.py (D027 standard)\\\", \\\"eval_server\\\": \\\"westd-28034\\\", \\\"eval_time_sec\\\": 6726}, \\\"preset_eval_ckpt1500\\\": {\\\"ToF\\\": 0, \\\"NoF\\\": 1, \\\"SYCONScore\\\": 0, \\\"eval_server\\\": \\\"westd-29046\\\"}, \\\"preset_eval_ckpt2000\\\": {\\\"ToF\\\": 0, \\\"NoF\\\": 1, \\\"SYCONScore\\\": 0, \\\"eval_server\\\": \\\"westd-29046\\\"}, \\\"stubbornness_onset\\\": \\\"immediate — ToF=0 at ckpt-500, probe reward trap activates within first 500 training steps\\\", \\\"trajectory\\\": \\\"ckpt-500 ToF=0.000 → ckpt-1000 ToF=0.006 → ckpt-1500 ToF=0.000 → ckpt-2000 ToF=0.000. Stubbornness is not gradual onset but immediate collapse.\\\"}}, \\\"exp002v2-recalib\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp-016\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"alpha_0.0\\\": {\\\"NoF\\\": 0.6961, \\\"WRR\\\": 0.2707}, \\\"alpha_0.5\\\": {\\\"NoF\\\": 0.6906, \\\"WRR\\\": 0.2541}, \\\"alpha_1.0\\\": {\\\"NoF\\\": 0.7127, \\\"WRR\\\": 0.2652}, \\\"alpha_2.0\\\": {\\\"NoF\\\": 0.6851, \\\"WRR\\\": 0.2541}, \\\"alpha_5.0\\\": {\\\"NoF\\\": 0.7845, \\\"WRR\\\": 0.2155}, \\\"best_alpha\\\": 5, \\\"best_NoF_delta\\\": \\\"+8.8pp\\\", \\\"D027_note\\\": \\\"D027 unified eval reversal: alpha=5 SYCONScore=0.054 < vanilla SYCONScore=0.134. ActAdd improves NoF but destroys ToF, net negative under NLI-based SYCONScore.\\\", \\\"conclusion_reason\\\": \\\"D027 eval reversal: ActAdd alpha=5 SYCONScore 0.054 worse than vanilla 0.134\\\", \\\"unified_reeval_D027\\\": {\\\"alpha_0.0\\\": {\\\"ToF\\\": 0.0718, \\\"NoF\\\": 0.9448, \\\"SYCONScore\\\": 0.1335}, \\\"alpha_0.5\\\": {\\\"ToF\\\": 0.0718, \\\"NoF\\\": 0.9392, \\\"SYCONScore\\\": 0.1334}, \\\"alpha_1.0\\\": {\\\"ToF\\\": 0.0442, \\\"NoF\\\": 0.9724, \\\"SYCONScore\\\": 0.0846}, \\\"alpha_2.0\\\": {\\\"ToF\\\": 0.0276, \\\"NoF\\\": 0.9669, \\\"SYCONScore\\\": 0.0537}, \\\"alpha_5.0\\\": {\\\"ToF\\\": 0.0276, \\\"NoF\\\": 0.9613, \\\"SYCONScore\\\": 0.0537}, \\\"eval_server\\\": \\\"westd-28034\\\", \\\"eval_results_path\\\": \\\"/root/contrastive_entrain_calib/results/exp016_unified_reeval/\\\"}}}, \\\"exp-014\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\", \\\"metrics\\\": {\\\"preset_eval_ckpt3000\\\": {\\\"ToF\\\": 0.978, \\\"NoF\\\": 0.006, \\\"SYCONScore\\\": 0.011, \\\"RC_AUC\\\": 0.195, \\\"n_valid\\\": 181, \\\"n_invalid\\\": 181, \\\"n_total\\\": 362, \\\"checkpoint\\\": \\\"checkpoint-3000\\\", \\\"eval_script\\\": \\\"run_exp014_eval.sh (preset, NLI-based)\\\", \\\"eval_time_sec\\\": 1179}, \\\"diagnosis\\\": \\\"mode_collapse: model flips on ALL pressure (valid+invalid), NoF≈0. Consistent with training R3=0.999, entropy=0.025.\\\"}}, \\\"vanilla-baseline\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"ToF\\\": 0.1105, \\\"NoF\\\": 0.9227, \\\"sycon_score\\\": 0.1974, \\\"samples\\\": 362, \\\"avg_flip_turn_valid\\\": 1, \\\"avg_flip_count_invalid\\\": 0.08, \\\"eval_script\\\": \\\"eval_pipeline.py (28034, missing regex postprocess)\\\", \\\"note\\\": \\\"28034 version missing regex &lt;think> cleanup, may need re-eval after sync\\\"}}, \\\"exp-002v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"exp-002\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"exp-008\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"exp-001\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"cv_auroc_mean\\\": 0.8269, \\\"cv_auroc_std\\\": 0.0278, \\\"full_auroc\\\": 0.8159, \\\"bootstrap_ci_95\\\": [0.7698, 0.8589], \\\"best_layer\\\": 19, \\\"auroc_weak\\\": 0.675, \\\"auroc_medium\\\": 0.883, \\\"auroc_strong\\\": 0.929, \\\"num_pairs\\\": 181, \\\"stop_gate\\\": \\\"CONTINUE_REDUCED_R1\\\"}}}, \\\"count\\\": 86, \\\"total\\\": 86, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.2295}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"exp-003-eval-s2-ckpt8000\": {\"status\": \"ANALYZING\"}, \"exp-004-s2-eval-ckpt4000\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"SYCONScore\": 0.2061, \"ToF\": 0.116, \"NoF\": 0.9227, \"n_valid\": 181, \"n_total\": 362}}, \"exp-003-len512\": {\"status\": \"PREPARING\", \"conclusion\": \"killed\"}, \"exp-004-reduced-lora\": {\"status\": \"RUNNING\"}, \"exp-004-s2-eval-ckpt3500\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp-003-s3\": {\"status\": \"QUEUED\", \"conclusion\": \"killed\"}, \"exp-002v3-gs8\": {\"status\": \"PREPARING\", \"conclusion\": \"killed\"}, \"exp-004-s2-v2\": {\"status\": \"RUNNING\"}, \"exp-003-gs8\": {\"status\": \"RUNNING\"}, \"exp-003-s2\": {\"status\": \"ANALYZING\", \"conclusion\": \"success\"}, \"exp-003-eval-s2-ckpt7500\": {\"status\": \"RUNNING\"}, \"exp-004-s2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp-004-s2-eval-ckpt2500\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp-004-s2-eval-ckpt2000\": {\"status\": \"DONE\", \"metrics\": {\"sycon_score\": 0.2139, \"tof\": 0.1215, \"nof\": 0.8895, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362}, \"conclusion\": \"success\"}, \"exp-003-eval-s2-ckpt7000\": {\"status\": \"DONE\", \"metrics\": {\"sycon_score\": 0.0945, \"tof\": 0.0497, \"nof\": 0.9503, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362}, \"conclusion\": \"negative\"}, \"exp-004-s2-eval-ckpt1500\": {\"status\": \"DONE\", \"metrics\": {\"sycon_score\": 0.2137, \"tof\": 0.1215, \"nof\": 0.884, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362}, \"conclusion\": \"success\"}, \"exp-004-s2-eval-ckpt1000\": {\"status\": \"DONE\", \"metrics\": {\"sycon_score\": 0.2564, \"tof\": 0.1492, \"nof\": 0.9116, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362}, \"conclusion\": \"success\"}, \"exp-004-s2-eval-ckpt500\": {\"status\": \"DONE\", \"metrics\": {\"sycon_score\": 0.2232, \"tof\": 0.1271, \"nof\": 0.9171, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362}, \"conclusion\": \"success\"}, \"exp-003-eval-s2-ckpt6500\": {\"status\": \"DONE\", \"metrics\": {\"sycon_score\": 0.1046, \"tof\": 0.0552, \"nof\": 0.9779, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362}, \"conclusion\": \"negative\"}, \"exp-003-eval-s2-ckpt6000\": {\"status\": \"DONE\", \"metrics\": {\"sycon_score\": 0.0945, \"tof\": 0.0497, \"nof\": 0.9503, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362}, \"conclusion\": \"success\"}, \"exp-003-eval-s2-ckpt5500\": {\"status\": \"DONE\", \"metrics\": {\"sycon_score\": 0.1144, \"tof\": 0.0608, \"nof\": 0.9724, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362}, \"conclusion\": \"success\"}, \"exp-003-eval-s2-ckpt5000\": {\"status\": \"DONE\", \"metrics\": {\"sycon_score\": 0.1044, \"tof\": 0.0552, \"nof\": 0.9503, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362}, \"conclusion\": \"success\"}, \"exp-003-eval-s2-ckpt4500\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sycon_score\": 0.1044, \"tof\": 0.0552, \"nof\": 0.9503, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362}}, \"exp-004-eval-ckpt8000-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sycon_score\": 0.3013, \"tof\": 0.1823, \"nof\": 0.8674, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362}}, \"exp-004-eval-ckpt2000-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sycon_score\": 0.255, \"tof\": 0.1492, \"nof\": 0.8785, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362}}, \"exp-004-eval-ckpt500-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sycon_score\": 0.1699, \"tof\": 0.0939, \"nof\": 0.8895, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362}}, \"exp-003-eval-s2-ckpt4000-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sycon_score\": 0.143, \"tof\": 0.0773, \"nof\": 0.9448, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362}}, \"exp-004-eval-ckpt8000\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp-004-eval-ckpt2000\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp-004-eval-ckpt500\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp-003-eval-s2-ckpt4000\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp-003-eval-ckpt8000\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sycon_score\": 0.1433, \"tof\": 0.0773, \"nof\": 0.9724, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362}}, \"exp-003-eval-s2-ckpt3500\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sycon_score\": 0.0744, \"tof\": 0.0387, \"nof\": 0.9724, \"n_valid\": 181, \"n_invalid\": 181}}, \"exp-003-eval-s2-ckpt2500\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sycon_score\": 0.1046, \"tof\": 0.0552, \"nof\": 0.9724}}, \"exp-003-s2-eval-ckpt2000\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp-003-s2-eval-ckpt3000\": {\"status\": \"QUEUED\", \"conclusion\": \"killed\"}, \"exp-003-s2-eval-ckpt2500\": {\"status\": \"QUEUED\", \"conclusion\": \"killed\"}, \"exp-004\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"trend\": \"generally increasing trend with oscillations: early phase ~0.17-0.25, late phase ~0.26-0.30, best=0.301 at ckpt-8000\", \"best_sycon_score\": 0.301, \"best_checkpoint\": \"ckpt-8000\"}}, \"exp-003\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp-003-eval-s2-ckpt2000\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sycon_score\": 0.0846}}, \"exp-003-eval-ckpt7500\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sycon_score\": 0.1046}}, \"exp-003-eval-ckpt7000-v3\": {\"status\": \"DONE\", \"metrics\": {\"sycon_score\": 0.1046}, \"conclusion\": \"success\"}, \"exp-003-eval-s2-ckpt3000\": {\"status\": \"DONE\", \"metrics\": {\"sycon_score\": 0.0945, \"tof\": 0.0497, \"nof\": 0.9503}, \"conclusion\": \"success\"}, \"exp-003-eval-ckpt5000-v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"sycon_score\": 0.1144, \"tof\": 0.0608, \"nof\": 0.9669}}, \"exp-003-eval-ckpt6500\": {\"status\": \"DONE\", \"metrics\": {\"sycon_score\": 0.1529, \"tof\": 0.0829, \"nof\": 0.9834}, \"conclusion\": \"success\"}, \"exp-003-eval-ckpt6000\": {\"status\": \"DONE\", \"metrics\": {\"sycon_score\": 0.0846, \"tof\": 0.0442, \"nof\": 0.9724}, \"conclusion\": \"success\"}, \"exp-003-eval-ckpt7000-v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp-003-eval-ckpt7000\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp-003-eval-ckpt2000\": {\"status\": \"DONE\", \"metrics\": {\"ToF\": 0.0442, \"NoF\": 0.9834, \"SYCONScore\": 0.0846, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362, \"checkpoint\": \"checkpoint-2000\", \"eval_script\": \"eval_unified_preset.py (D027 standard)\", \"eval_server\": \"westd-28034\", \"vs_vanilla\": \"SYCONScore 0.0846 vs 0.1335 = -36.6%, BELOW baseline\"}, \"conclusion\": \"negative\"}, \"exp-003-eval-ckpt3000\": {\"status\": \"DONE\", \"metrics\": {\"ToF\": 0.0497, \"NoF\": 0.9724, \"SYCONScore\": 0.0946, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362, \"checkpoint\": \"checkpoint-3000\", \"eval_script\": \"eval_unified_preset.py (D027 standard)\", \"eval_server\": \"westd-28034\", \"vs_vanilla\": \"SYCONScore 0.0946 vs 0.1335 = -29.1%, BELOW baseline\"}, \"conclusion\": \"negative\"}, \"exp-009-eval-ckpt500\": {\"status\": \"DONE\", \"metrics\": {\"ToF\": 0.0663, \"NoF\": 0.9337, \"SYCONScore\": 0.1238, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362, \"checkpoint\": \"checkpoint-500\", \"eval_script\": \"eval_unified_preset.py (D027 standard)\", \"eval_server\": \"westd-28034\", \"eval_time_sec\": 7671}, \"conclusion\": \"negative\"}, \"vanilla-d027-reeval\": {\"status\": \"DONE\", \"metrics\": {\"ToF\": 0.0718, \"NoF\": 0.9448, \"SYCONScore\": 0.1335, \"n_total\": 362, \"eval_script\": \"eval_unified_preset.py (D027 standard)\", \"eval_server\": \"westd-28034\", \"note\": \"D027 unified preset baseline. Previous eval_pipeline.py gave ToF=0.1105, NoF=0.9227, SYCONScore=0.1974 — discrepancy due to different eval scripts.\"}, \"conclusion\": \"success\"}, \"exp-003-eval-ckpt4500\": {\"status\": \"DONE\", \"metrics\": {\"ToF\": 0.0718, \"NoF\": 0.9613, \"SYCONScore\": 0.1337, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362, \"checkpoint\": \"checkpoint-4500\", \"eval_script\": \"eval_unified_preset.py (D027 standard)\", \"eval_server\": \"westd-28034\", \"eval_time_sec\": 4280, \"vs_vanilla\": \"SYCONScore 0.1337 vs 0.1335 = +0.1%, essentially EQUAL to baseline\", \"note\": \"Surprising: ckpt-4500 peaks near vanilla baseline (0.1337), HIGHER than ckpt-4000/5000/5500 (0.1144). Non-monotonic trajectory — peak at 4500 then regression.\"}, \"conclusion\": \"negative\"}, \"exp-003-s2-eval-ckpt1500\": {\"status\": \"DONE\", \"metrics\": {\"ToF\": 0.0552, \"NoF\": 0.9503, \"SYCONScore\": 0.1044, \"samples\": 362}, \"conclusion\": \"negative\"}, \"exp-003-s2-eval-ckpt1000\": {\"status\": \"DONE\", \"metrics\": {\"ToF\": 0.0442, \"NoF\": 0.9448, \"SYCONScore\": 0.0844, \"samples\": 362}, \"conclusion\": \"negative\"}, \"exp-003-s2-eval-ckpt500\": {\"status\": \"DONE\", \"metrics\": {\"ToF\": 0.0442, \"NoF\": 0.9503, \"SYCONScore\": 0.0845, \"samples\": 362}, \"conclusion\": \"negative\"}, \"exp-003-eval-ckpt5500\": {\"status\": \"DONE\", \"metrics\": {\"ToF\": 0.0608, \"NoF\": 0.9724, \"SYCONScore\": 0.1144, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362, \"checkpoint\": \"checkpoint-5500\", \"eval_script\": \"eval_unified_preset.py (D027 standard)\", \"eval_server\": \"westd-28034\", \"eval_time_sec\": 4484, \"vs_vanilla\": \"SYCONScore 0.1144 vs 0.1335 = -14.3%, BELOW baseline\", \"note\": \"Identical to ckpt-4000/5000 — plateau confirmed at 3 consecutive checkpoints\"}, \"conclusion\": \"negative\"}, \"exp-004-eval-ckpt5500\": {\"status\": \"DONE\", \"metrics\": {\"ToF\": 0.1381, \"NoF\": 0.8674, \"SYCONScore\": 0.2383, \"n_samples\": 362}, \"conclusion\": \"success\"}, \"exp-004-eval-ckpt4500\": {\"status\": \"DONE\", \"metrics\": {\"ToF\": 0.105, \"NoF\": 0.8785, \"SYCONScore\": 0.1875, \"n_samples\": 362}, \"conclusion\": \"success\"}, \"exp-004-eval-ckpt7500\": {\"status\": \"DONE\", \"metrics\": {\"ToF\": 0.1657, \"NoF\": 0.8453, \"SYCONScore\": 0.2771, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362, \"checkpoint\": \"checkpoint-7500\", \"eval_script\": \"eval_unified_preset.py (D027 standard)\", \"eval_server\": \"westd-28034\", \"vs_vanilla\": \"SYCONScore 0.2771 vs 0.1335 = +107.6%\"}, \"conclusion\": \"success\"}, \"exp-004-eval-ckpt6500\": {\"status\": \"DONE\", \"metrics\": {\"ToF\": 0.1492, \"NoF\": 0.8232, \"SYCONScore\": 0.2526, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362, \"checkpoint\": \"checkpoint-6500\", \"eval_script\": \"eval_unified_preset.py (D027 standard)\", \"eval_server\": \"westd-28034\", \"vs_vanilla\": \"SYCONScore 0.2526 vs 0.1335 = +89.1%\"}, \"conclusion\": \"success\"}, \"exp-009-eval-ckpt1000\": {\"status\": \"DONE\", \"metrics\": {\"ToF\": 0.0608, \"NoF\": 0.9337, \"SYCONScore\": 0.1141, \"n_total\": 362, \"checkpoint\": \"checkpoint-1000\", \"eval_script\": \"eval_unified_preset.py (D027 standard)\", \"eval_server\": \"westd-28034\", \"trend_vs_ckpt500\": \"ToF 0.0663→0.0608 (↓8.3%), SYCONScore 0.1238→0.1141 (↓7.8%)\"}, \"conclusion\": \"negative\"}, \"exp-004-eval-ckpt1500\": {\"status\": \"DONE\", \"metrics\": {\"ToF\": 0.0939, \"NoF\": 0.8895, \"SYCONScore\": 0.1699, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362, \"checkpoint\": \"checkpoint-1500\", \"eval_script\": \"eval_unified_preset.py (D027 standard)\", \"eval_server\": \"westd-28034\", \"eval_time_sec\": 1741, \"vs_vanilla\": \"SYCONScore 0.1699 vs 0.1335 = +27.3%\"}, \"conclusion\": \"success\"}, \"exp-004-eval-ckpt3500\": {\"status\": \"DONE\", \"metrics\": {\"ToF\": 0.1326, \"NoF\": 0.9006, \"SYCONScore\": 0.2312, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362, \"checkpoint\": \"checkpoint-3500\", \"eval_script\": \"eval_unified_preset.py (D027 standard)\", \"eval_server\": \"westd-28034\", \"vs_vanilla\": \"SYCONScore 0.2312 vs 0.1335 = +73.2%\"}, \"conclusion\": \"success\"}, \"exp-004-eval-ckpt2500\": {\"status\": \"DONE\", \"metrics\": {\"ToF\": 0.1381, \"NoF\": 0.884, \"SYCONScore\": 0.2389, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362, \"checkpoint\": \"checkpoint-2500\", \"eval_script\": \"eval_unified_preset.py (D027 standard)\", \"eval_server\": \"westd-28034\", \"vs_vanilla\": \"SYCONScore 0.2389 vs 0.1335 = +78.9%\"}, \"conclusion\": \"success\"}, \"exp-003-eval-ckpt4000\": {\"status\": \"DONE\", \"metrics\": {\"ToF\": 0.0608, \"NoF\": 0.9669, \"SYCONScore\": 0.1144, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362, \"checkpoint\": \"checkpoint-4000\", \"eval_script\": \"eval_unified_preset.py (D027 standard)\", \"eval_server\": \"westd-28034\", \"eval_time_sec\": 4353, \"vs_vanilla\": \"SYCONScore 0.1144 vs 0.1335 = -14.3%, BELOW baseline\", \"note\": \"Identical to ckpt-5000 — model saturated at step 4000\"}, \"conclusion\": \"negative\"}, \"exp-004-eval-ckpt3000\": {\"status\": \"DONE\", \"metrics\": {\"ToF\": 0.116, \"NoF\": 0.9116, \"SYCONScore\": 0.2058, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362, \"checkpoint\": \"checkpoint-3000\", \"eval_script\": \"eval_unified_preset.py (D027 standard)\", \"eval_server\": \"westd-28034\", \"vs_vanilla\": \"SYCONScore 0.2058 vs 0.1335 = +54.2%\"}, \"conclusion\": \"success\"}, \"exp-004-eval-ckpt5000\": {\"status\": \"DONE\", \"metrics\": {\"ToF\": 0.1547, \"NoF\": 0.8785, \"SYCONScore\": 0.2631, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362, \"checkpoint\": \"checkpoint-5000\", \"eval_script\": \"eval_unified_preset.py (D027 standard)\", \"eval_server\": \"westd-28034\", \"eval_time_sec\": 1305, \"vs_vanilla\": \"SYCONScore 0.2631 vs 0.1335 = +97.1%\"}, \"conclusion\": \"success\"}, \"exp-004-eval-ckpt7000\": {\"status\": \"DONE\", \"metrics\": {\"ToF\": 0.1713, \"NoF\": 0.8619, \"SYCONScore\": 0.2858, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362, \"checkpoint\": \"checkpoint-7000\", \"eval_script\": \"eval_unified_preset.py (D027 standard)\", \"eval_server\": \"westd-28034\", \"eval_time_sec\": 1254, \"vs_vanilla\": \"SYCONScore 0.2858 vs 0.1335 = +114.1%\"}, \"conclusion\": \"success\"}, \"exp-004-eval-ckpt1000\": {\"status\": \"DONE\", \"metrics\": {\"ToF\": 0.116, \"NoF\": 0.8729, \"SYCONScore\": 0.2048, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362, \"checkpoint\": \"checkpoint-1000\", \"eval_script\": \"eval_unified_preset.py (D027 standard)\", \"eval_server\": \"westd-28034\", \"eval_time_sec\": 1689, \"vs_vanilla\": \"SYCONScore 0.2048 vs 0.1335 = +53.4%\"}, \"conclusion\": \"success\"}, \"exp-004-eval-ckpt4000\": {\"status\": \"DONE\", \"metrics\": {\"ToF\": 0.1215, \"NoF\": 0.895, \"SYCONScore\": 0.214, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362, \"checkpoint\": \"checkpoint-4000\", \"eval_script\": \"eval_unified_preset.py (D027 standard)\", \"eval_server\": \"westd-28034\", \"vs_vanilla\": \"SYCONScore 0.2140 vs 0.1335 = +60.3%, ABOVE baseline (dip vs ckpt-2000)\"}, \"conclusion\": \"success\"}, \"exp-004-eval-ckpt6000\": {\"status\": \"DONE\", \"metrics\": {\"ToF\": 0.1547, \"NoF\": 0.8508, \"SYCONScore\": 0.2618, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362, \"checkpoint\": \"checkpoint-6000\", \"eval_script\": \"eval_unified_preset.py (D027 standard)\", \"eval_server\": \"westd-28034\", \"vs_vanilla\": \"SYCONScore 0.2618 vs 0.1335 = +96.1%, ABOVE baseline\"}, \"conclusion\": \"success\"}, \"exp-003-eval-ckpt1000\": {\"status\": \"DONE\", \"metrics\": {\"ToF\": 0.0387, \"NoF\": 0.9448, \"SYCONScore\": 0.0743, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362, \"eval_time_s\": 4319, \"checkpoint\": \"checkpoint-1000\", \"eval_script\": \"eval_unified_preset.py (D027 standard)\", \"eval_server\": \"westd-28034\"}, \"conclusion\": \"negative\"}, \"exp-003-eval-ckpt5000\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"ToF\": 0.0608, \"NoF\": 0.9669, \"SYCONScore\": 0.1144, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362, \"checkpoint\": \"checkpoint-5000\", \"eval_script\": \"eval_unified_preset.py (D027 standard)\", \"eval_server\": \"westd-28034\", \"eval_time_sec\": 5146, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/exp003/checkpoint-5000\", \"log_path\": \"/root/autodl-tmp/results/exp003_unified_eval/\", \"vs_vanilla\": \"SYCONScore 0.1144 vs 0.1335 = -14.3%, BELOW baseline\"}}, \"exp-009\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"eval_ckpt500\": {\"ToF\": 0.0663, \"NoF\": 0.9337, \"SYCONScore\": 0.1238}, \"eval_ckpt1000\": {\"ToF\": 0.0608, \"NoF\": 0.9337, \"SYCONScore\": 0.1141}, \"trend\": \"monotonic decline: ckpt-500→ckpt-1000 ToF ↓8.3%, SYCONScore ↓7.8%\", \"vanilla_d027_baseline\": {\"SYCONScore\": 0.1335}, \"kill_reason\": \"D040: all three R1 formulations (cosine/binary/continuous_probability) failed. Completes ALL-formulations-fail argument.\", \"available_checkpoints\": [\"checkpoint-500\", \"checkpoint-1000\"]}}, \"exp-012\": {\"status\": \"DONE\", \"metrics\": {\"cv_auroc_mean\": 0.7793, \"cv_auroc_std\": 0.0189, \"full_auroc\": 0.7779, \"best_layer\": 16, \"style_controlled_auroc\": 0.9227, \"per_layer_auroc_top5\": {\"16\": 0.7793, \"22\": 0.7359, \"25\": 0.7372, \"26\": 0.7374, \"31\": 0.747}, \"domain_auroc\": {\"commonsense\": 0.8444, \"history\": 0.818, \"math\": 0.769, \"science\": 0.7546, \"geography\": 0.7507}, \"evidence_strength_auroc\": {\"strong\": 0.9109, \"medium\": 0.8635, \"weak\": 0.7106}, \"num_pairs\": 181, \"num_samples\": 362, \"layer_range\": [16, 31], \"probe_ablation\": {\"d_syc_best_layer_auroc\": 0.778, \"d_syc_multi_layer_auroc\": 0.813, \"random_direction_auroc_mean\": 0.53, \"random_direction_auroc_std\": 0.054, \"gap_d_syc_minus_random\": 0.248, \"qwen_comparison\": {\"qwen_d_syc\": 0.835, \"qwen_random\": 0.727, \"qwen_gap\": 0.108}, \"finding\": \"Llama gap (+0.248) larger than Qwen (+0.108). Random direction near chance (0.53) on Llama vs 0.73 on Qwen — sycophancy signal more concentrated in specific directions on Llama.\"}}, \"conclusion\": \"success\"}, \"exp-002v3\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"collapse_timeline\": {\"phase1_length_collapse\": \"step 100-300, mean_len 247→80, entropy 0.45→0.10\", \"low_entropy_plateau\": \"step 300-2150, entropy 0.07-0.10\", \"phase2_terminal_collapse\": \"step 2160, entropy 0.056→0.026 in 50 steps, frac_zero_std 0.125→0.419\", \"critical_step\": 2160}, \"entropy_at_kill\": 0.006, \"grad_norm_at_kill\": 0, \"frac_reward_zero_std_peak\": 0.963, \"r3_saturation_step\": 100, \"r3_saturated_value\": 0.9998, \"r1_behavior\": \"mean oscillated -0.46 to +0.41, no sustained positive trend despite 5x scaling\", \"available_checkpoints\": [\"checkpoint-500\", \"checkpoint-1000\", \"checkpoint-1500\", \"checkpoint-2000\"], \"best_checkpoint_before_collapse\": \"checkpoint-2000 (entropy ~0.062, still in plateau)\", \"root_cause\": \"R3 saturated at step 100 → combined reward degenerates to only R1 → cosine R1 signal too noisy (high variance) to provide stable optimization direction. Problem is R1 noise, not R1 magnitude — 5x scaling amplified noise proportionally.\", \"conclusion_reason\": \"GRPO mode collapse: R3 early saturation + cosine R1 high-variance noise = no effective learning signal. Confirms scaled cosine R1 also structurally fails.\"}}, \"exp-008v3\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"preset_eval_ckpt500\": {\"ToF\": 0, \"NoF\": 0.9945, \"SYCONScore\": 0, \"n_total\": 362, \"checkpoint\": \"checkpoint-500\", \"eval_script\": \"eval_unified_preset.py (D027 standard)\", \"eval_server\": \"westd-28034\", \"eval_time_sec\": 6502}, \"preset_eval_ckpt1000\": {\"ToF\": 0.0055, \"NoF\": 0.9945, \"SYCONScore\": 0.011, \"n_total\": 362, \"checkpoint\": \"checkpoint-1000\", \"eval_script\": \"eval_unified_preset.py (D027 standard)\", \"eval_server\": \"westd-28034\", \"eval_time_sec\": 6726}, \"preset_eval_ckpt1500\": {\"ToF\": 0, \"NoF\": 1, \"SYCONScore\": 0, \"eval_server\": \"westd-29046\"}, \"preset_eval_ckpt2000\": {\"ToF\": 0, \"NoF\": 1, \"SYCONScore\": 0, \"eval_server\": \"westd-29046\"}, \"stubbornness_onset\": \"immediate — ToF=0 at ckpt-500, probe reward trap activates within first 500 training steps\", \"trajectory\": \"ckpt-500 ToF=0.000 → ckpt-1000 ToF=0.006 → ckpt-1500 ToF=0.000 → ckpt-2000 ToF=0.000. Stubbornness is not gradual onset but immediate collapse.\"}}, \"exp002v2-recalib\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp-016\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"alpha_0.0\": {\"NoF\": 0.6961, \"WRR\": 0.2707}, \"alpha_0.5\": {\"NoF\": 0.6906, \"WRR\": 0.2541}, \"alpha_1.0\": {\"NoF\": 0.7127, \"WRR\": 0.2652}, \"alpha_2.0\": {\"NoF\": 0.6851, \"WRR\": 0.2541}, \"alpha_5.0\": {\"NoF\": 0.7845, \"WRR\": 0.2155}, \"best_alpha\": 5, \"best_NoF_delta\": \"+8.8pp\", \"D027_note\": \"D027 unified eval reversal: alpha=5 SYCONScore=0.054 < vanilla SYCONScore=0.134. ActAdd improves NoF but destroys ToF, net negative under NLI-based SYCONScore.\", \"conclusion_reason\": \"D027 eval reversal: ActAdd alpha=5 SYCONScore 0.054 worse than vanilla 0.134\", \"unified_reeval_D027\": {\"alpha_0.0\": {\"ToF\": 0.0718, \"NoF\": 0.9448, \"SYCONScore\": 0.1335}, \"alpha_0.5\": {\"ToF\": 0.0718, \"NoF\": 0.9392, \"SYCONScore\": 0.1334}, \"alpha_1.0\": {\"ToF\": 0.0442, \"NoF\": 0.9724, \"SYCONScore\": 0.0846}, \"alpha_2.0\": {\"ToF\": 0.0276, \"NoF\": 0.9669, \"SYCONScore\": 0.0537}, \"alpha_5.0\": {\"ToF\": 0.0276, \"NoF\": 0.9613, \"SYCONScore\": 0.0537}, \"eval_server\": \"westd-28034\", \"eval_results_path\": \"/root/contrastive_entrain_calib/results/exp016_unified_reeval/\"}}}, \"exp-014\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"metrics\": {\"preset_eval_ckpt3000\": {\"ToF\": 0.978, \"NoF\": 0.006, \"SYCONScore\": 0.011, \"RC_AUC\": 0.195, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362, \"checkpoint\": \"checkpoint-3000\", \"eval_script\": \"run_exp014_eval.sh (preset, NLI-based)\", \"eval_time_sec\": 1179}, \"diagnosis\": \"mode_collapse: model flips on ALL pressure (valid+invalid), NoF≈0. Consistent with training R3=0.999, entropy=0.025.\"}}, \"vanilla-baseline\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"ToF\": 0.1105, \"NoF\": 0.9227, \"sycon_score\": 0.1974, \"samples\": 362, \"avg_flip_turn_valid\": 1, \"avg_flip_count_invalid\": 0.08, \"eval_script\": \"eval_pipeline.py (28034, missing regex postprocess)\", \"note\": \"28034 version missing regex &lt;think> cleanup, may need re-eval after sync\"}}, \"exp-002v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp-002\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp-008\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp-001\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"cv_auroc_mean\": 0.8269, \"cv_auroc_std\": 0.0278, \"full_auroc\": 0.8159, \"bootstrap_ci_95\": [0.7698, 0.8589], \"best_layer\": 19, \"auroc_weak\": 0.675, \"auroc_medium\": 0.883, \"auroc_strong\": 0.929, \"num_pairs\": 181, \"stop_gate\": \"CONTINUE_REDUCED_R1\"}}}, \"count\": 86, \"total\": 86, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2295}}"
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
I found the seed 1 ckpt-8000 data:

**exp-003-eval-ckpt8000** (seed 1):
- sycon_score: 0.1433
- tof: 0.0773
- nof: 0.9724
- conclusion: success

**exp-003-eval-s2-ckpt8000** (seed 2, from log):
- SYCONScore: 0.1240
- ToF: 0.0663
- NoF: 0.9613


- Samples: 362 (valid=181, invalid=181)

The seed 2 SYCON score of 0.1240 falls below the vanilla baseline of 0.1335, so I need to mark this as negative and update the registry with the metrics, conclusion, and status.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26c5ec7a-74bc-48da-96c7-b3a2f055f03a",
  "uuid": "60caad8d-5c04-44dd-a7ec-1050a1dc3ebd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016G2e7GaRAdvDoKyogkrd7e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10662,
      "cache_read_input_tokens": 29317,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10662
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

_source line 22_

数据已获取。更新 registry。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26c5ec7a-74bc-48da-96c7-b3a2f055f03a",
  "uuid": "7dc1f5c1-68aa-4ad0-b45c-9f34c81f2d37",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016G2e7GaRAdvDoKyogkrd7e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10662,
      "cache_read_input_tokens": 29317,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10662
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_016TdzPNYf4aHSUJR5btPTU5`</summary>

```json
{
  "exp_id": "exp-003-eval-s2-ckpt8000",
  "field": "metrics",
  "value": {
    "SYCONScore": 0.124,
    "ToF": 0.0663,
    "NoF": 0.9613,
    "n_valid": 181,
    "n_invalid": 181,
    "n_total": 362,
    "checkpoint": "checkpoint-8000",
    "eval_script": "eval_unified_preset.py (D027 standard)",
    "eval_server": "westd-29046",
    "eval_time_sec": 5010,
    "vs_vanilla": "SYCONScore 0.1240 vs 0.1335 = -7.1%, BELOW baseline",
    "vs_seed1_ckpt8000": "SYCONScore 0.1240 vs 0.1433 = -13.5%, seed 2 worse than seed 1"
  },
  "project": "contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26c5ec7a-74bc-48da-96c7-b3a2f055f03a",
  "uuid": "983eb83e-139d-4c34-854b-0a9ec589b57e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016G2e7GaRAdvDoKyogkrd7e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10662,
      "cache_read_input_tokens": 29317,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10662
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

_source line 24 · 2026-05-22T17:05:04.017Z_

<details><summary>↩ Tool result · `toolu_016TdzPNYf4aHSUJR5btPTU5`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp-003-eval-s2-ckpt8000\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T15:37:04.686Z\", \"updated_at\": \"2026-05-22T17:05:03.833Z\", \"hypothesis\": \"Eval exp-003-s2 (R3-only seed 2) checkpoint-8000 (final) with D027 unified preset. Last R3-only seed 2 data point. Vanilla baseline SYCONScore=0.1335.\", \"parent\": \"exp-003-s2\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contrastive_entrain_calib && CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python eval/eval_unified_preset.py --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --lora_path /root/autodl-tmp/checkpoints/exp003_r3only_seed2/checkpoint-8000 --data_path /root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl --output_dir /root/contrastive_entrain_calib/results/exp003_d027_eval --exp_id exp003-s2-ckpt8000\\\"\", \"server\": \"westd-29046\", \"gpu\": [\"cuda:1\"], \"pid\": \"517412\", \"log_path\": \"~/runs/contrastive_entrain_calib/exp-003-eval-s2-ckpt8000.log\", \"submitted_at\": \"2026-05-22T15:38:40.535Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T17:03:18.652Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T17:03:22.278890+00:00\"}]}, \"metrics\": {\"SYCONScore\": 0.124, \"ToF\": 0.0663, \"NoF\": 0.9613, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362, \"checkpoint\": \"checkpoint-8000\", \"eval_script\": \"eval_unified_preset.py (D027 standard)\", \"eval_server\": \"westd-29046\", \"eval_time_sec\": 5010, \"vs_vanilla\": \"SYCONScore 0.1240 vs 0.1335 = -7.1%, BELOW baseline\", \"vs_seed1_ckpt8000\": \"SYCONScore 0.1240 vs 0.1433 = -13.5%, seed 2 worse than seed 1\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4329}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26c5ec7a-74bc-48da-96c7-b3a2f055f03a",
  "uuid": "73b214e2-5c95-468a-a133-4dbb425d817f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"exp-003-eval-s2-ckpt8000\\\", \\\"experiment\\\": {\\\"status\\\": \\\"ANALYZING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T15:37:04.686Z\\\", \\\"updated_at\\\": \\\"2026-05-22T17:05:03.833Z\\\", \\\"hypothesis\\\": \\\"Eval exp-003-s2 (R3-only seed 2) checkpoint-8000 (final) with D027 unified preset. Last R3-only seed 2 data point. Vanilla baseline SYCONScore=0.1335.\\\", \\\"parent\\\": \\\"exp-003-s2\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contrastive_entrain_calib && CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python eval/eval_unified_preset.py --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --lora_path /root/autodl-tmp/checkpoints/exp003_r3only_seed2/checkpoint-8000 --data_path /root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl --output_dir /root/contrastive_entrain_calib/results/exp003_d027_eval --exp_id exp003-s2-ckpt8000\\\\\\\"\\\", \\\"server\\\": \\\"westd-29046\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"517412\\\", \\\"log_path\\\": \\\"~/runs/contrastive_entrain_calib/exp-003-eval-s2-ckpt8000.log\\\", \\\"submitted_at\\\": \\\"2026-05-22T15:38:40.535Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-22T17:03:18.652Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-22T17:03:22.278890+00:00\\\"}]}, \\\"metrics\\\": {\\\"SYCONScore\\\": 0.124, \\\"ToF\\\": 0.0663, \\\"NoF\\\": 0.9613, \\\"n_valid\\\": 181, \\\"n_invalid\\\": 181, \\\"n_total\\\": 362, \\\"checkpoint\\\": \\\"checkpoint-8000\\\", \\\"eval_script\\\": \\\"eval_unified_preset.py (D027 standard)\\\", \\\"eval_server\\\": \\\"westd-29046\\\", \\\"eval_time_sec\\\": 5010, \\\"vs_vanilla\\\": \\\"SYCONScore 0.1240 vs 0.1335 = -7.1%, BELOW baseline\\\", \\\"vs_seed1_ckpt8000\\\": \\\"SYCONScore 0.1240 vs 0.1433 = -13.5%, seed 2 worse than seed 1\\\"}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4329}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"exp-003-eval-s2-ckpt8000\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T15:37:04.686Z\", \"updated_at\": \"2026-05-22T17:05:03.833Z\", \"hypothesis\": \"Eval exp-003-s2 (R3-only seed 2) checkpoint-8000 (final) with D027 unified preset. Last R3-only seed 2 data point. Vanilla baseline SYCONScore=0.1335.\", \"parent\": \"exp-003-s2\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contrastive_entrain_calib && CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python eval/eval_unified_preset.py --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --lora_path /root/autodl-tmp/checkpoints/exp003_r3only_seed2/checkpoint-8000 --data_path /root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl --output_dir /root/contrastive_entrain_calib/results/exp003_d027_eval --exp_id exp003-s2-ckpt8000\\\"\", \"server\": \"westd-29046\", \"gpu\": [\"cuda:1\"], \"pid\": \"517412\", \"log_path\": \"~/runs/contrastive_entrain_calib/exp-003-eval-s2-ckpt8000.log\", \"submitted_at\": \"2026-05-22T15:38:40.535Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T17:03:18.652Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T17:03:22.278890+00:00\"}]}, \"metrics\": {\"SYCONScore\": 0.124, \"ToF\": 0.0663, \"NoF\": 0.9613, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362, \"checkpoint\": \"checkpoint-8000\", \"eval_script\": \"eval_unified_preset.py (D027 standard)\", \"eval_server\": \"westd-29046\", \"eval_time_sec\": 5010, \"vs_vanilla\": \"SYCONScore 0.1240 vs 0.1335 = -7.1%, BELOW baseline\", \"vs_seed1_ckpt8000\": \"SYCONScore 0.1240 vs 0.1433 = -13.5%, seed 2 worse than seed 1\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4329}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01N9QawK9znE7fUj36g2m1ZT`</summary>

```json
{
  "exp_id": "exp-003-eval-s2-ckpt8000",
  "field": "conclusion",
  "value": "negative",
  "project": "contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26c5ec7a-74bc-48da-96c7-b3a2f055f03a",
  "uuid": "2f10e9ba-e712-4fec-a15f-5b966dcea040",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016G2e7GaRAdvDoKyogkrd7e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10662,
      "cache_read_input_tokens": 29317,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10662
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

_source line 26 · 2026-05-22T17:05:04.780Z_

<details><summary>↩ Tool result · `toolu_01N9QawK9znE7fUj36g2m1ZT`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp-003-eval-s2-ckpt8000\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T15:37:04.686Z\", \"updated_at\": \"2026-05-22T17:05:04.608Z\", \"hypothesis\": \"Eval exp-003-s2 (R3-only seed 2) checkpoint-8000 (final) with D027 unified preset. Last R3-only seed 2 data point. Vanilla baseline SYCONScore=0.1335.\", \"parent\": \"exp-003-s2\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contrastive_entrain_calib && CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python eval/eval_unified_preset.py --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --lora_path /root/autodl-tmp/checkpoints/exp003_r3only_seed2/checkpoint-8000 --data_path /root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl --output_dir /root/contrastive_entrain_calib/results/exp003_d027_eval --exp_id exp003-s2-ckpt8000\\\"\", \"server\": \"westd-29046\", \"gpu\": [\"cuda:1\"], \"pid\": \"517412\", \"log_path\": \"~/runs/contrastive_entrain_calib/exp-003-eval-s2-ckpt8000.log\", \"submitted_at\": \"2026-05-22T15:38:40.535Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T17:03:18.652Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T17:03:22.278890+00:00\"}]}, \"metrics\": {\"SYCONScore\": 0.124, \"ToF\": 0.0663, \"NoF\": 0.9613, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362, \"checkpoint\": \"checkpoint-8000\", \"eval_script\": \"eval_unified_preset.py (D027 standard)\", \"eval_server\": \"westd-29046\", \"eval_time_sec\": 5010, \"vs_vanilla\": \"SYCONScore 0.1240 vs 0.1335 = -7.1%, BELOW baseline\", \"vs_seed1_ckpt8000\": \"SYCONScore 0.1240 vs 0.1433 = -13.5%, seed 2 worse than seed 1\"}, \"conclusion\": \"negative\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3978}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26c5ec7a-74bc-48da-96c7-b3a2f055f03a",
  "uuid": "ac6171b1-ff45-40d5-9b66-2e09d9ae0c4d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"exp-003-eval-s2-ckpt8000\\\", \\\"experiment\\\": {\\\"status\\\": \\\"ANALYZING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T15:37:04.686Z\\\", \\\"updated_at\\\": \\\"2026-05-22T17:05:04.608Z\\\", \\\"hypothesis\\\": \\\"Eval exp-003-s2 (R3-only seed 2) checkpoint-8000 (final) with D027 unified preset. Last R3-only seed 2 data point. Vanilla baseline SYCONScore=0.1335.\\\", \\\"parent\\\": \\\"exp-003-s2\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contrastive_entrain_calib && CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python eval/eval_unified_preset.py --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --lora_path /root/autodl-tmp/checkpoints/exp003_r3only_seed2/checkpoint-8000 --data_path /root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl --output_dir /root/contrastive_entrain_calib/results/exp003_d027_eval --exp_id exp003-s2-ckpt8000\\\\\\\"\\\", \\\"server\\\": \\\"westd-29046\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"517412\\\", \\\"log_path\\\": \\\"~/runs/contrastive_entrain_calib/exp-003-eval-s2-ckpt8000.log\\\", \\\"submitted_at\\\": \\\"2026-05-22T15:38:40.535Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-22T17:03:18.652Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-22T17:03:22.278890+00:00\\\"}]}, \\\"metrics\\\": {\\\"SYCONScore\\\": 0.124, \\\"ToF\\\": 0.0663, \\\"NoF\\\": 0.9613, \\\"n_valid\\\": 181, \\\"n_invalid\\\": 181, \\\"n_total\\\": 362, \\\"checkpoint\\\": \\\"checkpoint-8000\\\", \\\"eval_script\\\": \\\"eval_unified_preset.py (D027 standard)\\\", \\\"eval_server\\\": \\\"westd-29046\\\", \\\"eval_time_sec\\\": 5010, \\\"vs_vanilla\\\": \\\"SYCONScore 0.1240 vs 0.1335 = -7.1%, BELOW baseline\\\", \\\"vs_seed1_ckpt8000\\\": \\\"SYCONScore 0.1240 vs 0.1433 = -13.5%, seed 2 worse than seed 1\\\"}, \\\"conclusion\\\": \\\"negative\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.3978}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"exp-003-eval-s2-ckpt8000\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T15:37:04.686Z\", \"updated_at\": \"2026-05-22T17:05:04.608Z\", \"hypothesis\": \"Eval exp-003-s2 (R3-only seed 2) checkpoint-8000 (final) with D027 unified preset. Last R3-only seed 2 data point. Vanilla baseline SYCONScore=0.1335.\", \"parent\": \"exp-003-s2\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contrastive_entrain_calib && CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python eval/eval_unified_preset.py --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --lora_path /root/autodl-tmp/checkpoints/exp003_r3only_seed2/checkpoint-8000 --data_path /root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl --output_dir /root/contrastive_entrain_calib/results/exp003_d027_eval --exp_id exp003-s2-ckpt8000\\\"\", \"server\": \"westd-29046\", \"gpu\": [\"cuda:1\"], \"pid\": \"517412\", \"log_path\": \"~/runs/contrastive_entrain_calib/exp-003-eval-s2-ckpt8000.log\", \"submitted_at\": \"2026-05-22T15:38:40.535Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T17:03:18.652Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T17:03:22.278890+00:00\"}]}, \"metrics\": {\"SYCONScore\": 0.124, \"ToF\": 0.0663, \"NoF\": 0.9613, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362, \"checkpoint\": \"checkpoint-8000\", \"eval_script\": \"eval_unified_preset.py (D027 standard)\", \"eval_server\": \"westd-29046\", \"eval_time_sec\": 5010, \"vs_vanilla\": \"SYCONScore 0.1240 vs 0.1335 = -7.1%, BELOW baseline\", \"vs_seed1_ckpt8000\": \"SYCONScore 0.1240 vs 0.1433 = -13.5%, seed 2 worse than seed 1\"}, \"conclusion\": \"negative\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3978}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_017XPXKc176r6o8PnAuT1gQM`</summary>

```json
{
  "exp_id": "exp-003-eval-s2-ckpt8000",
  "field": "status",
  "value": "DONE",
  "project": "contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26c5ec7a-74bc-48da-96c7-b3a2f055f03a",
  "uuid": "d179ffe9-8c80-4af7-993b-05bb9c6f356d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y1FN3Ykgh3JZuBg7TQyDeD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2601,
      "cache_read_input_tokens": 39979,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2601
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

_source line 28 · 2026-05-22T17:05:10.527Z_

<details><summary>↩ Tool result · `toolu_017XPXKc176r6o8PnAuT1gQM`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without output fields: ['checkpoint_path']. Set these fields first or pass them in spec.\", \"metadata\": {\"elapsed_seconds\": 0.2265}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26c5ec7a-74bc-48da-96c7-b3a2f055f03a",
  "uuid": "4cddc454-f3c9-4401-a055-f108f0dd93a6",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"Cannot transition to DONE without output fields: ['checkpoint_path']. Set these fields first or pass them in spec.\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.2265}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without output fields: ['checkpoint_path']. Set these fields first or pass them in spec.\", \"metadata\": {\"elapsed_seconds\": 0.2265}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01CHxidGyd4LzT8qDb9ow2md`</summary>

```json
{
  "exp_id": "exp-003-eval-s2-ckpt8000",
  "field": "status",
  "value": "DONE",
  "project": "contrastive_entrain_calib",
  "spec": {
    "checkpoint_path": "/root/autodl-tmp/checkpoints/exp003_r3only_seed2/checkpoint-8000",
    "log_path": "/root/runs/contrastive_entrain_calib/exp-003-eval-s2-ckpt8000.log"
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
  "session_id": "26c5ec7a-74bc-48da-96c7-b3a2f055f03a",
  "uuid": "a3d4efea-bcee-4ce6-b254-b07beba76400",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KicmxngHHCnDxmtminAvYn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 214,
      "cache_read_input_tokens": 42580,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 214
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

_source line 30 · 2026-05-22T17:05:24.320Z_

<details><summary>↩ Tool result · `toolu_01CHxidGyd4LzT8qDb9ow2md`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp-003-eval-s2-ckpt8000\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T15:37:04.686Z\", \"updated_at\": \"2026-05-22T17:05:23.614Z\", \"hypothesis\": \"Eval exp-003-s2 (R3-only seed 2) checkpoint-8000 (final) with D027 unified preset. Last R3-only seed 2 data point. Vanilla baseline SYCONScore=0.1335.\", \"parent\": \"exp-003-s2\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contrastive_entrain_calib && CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python eval/eval_unified_preset.py --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --lora_path /root/autodl-tmp/checkpoints/exp003_r3only_seed2/checkpoint-8000 --data_path /root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl --output_dir /root/contrastive_entrain_calib/results/exp003_d027_eval --exp_id exp003-s2-ckpt8000\\\"\", \"server\": \"westd-29046\", \"gpu\": [\"cuda:1\"], \"pid\": \"517412\", \"log_path\": \"/root/runs/contrastive_entrain_calib/exp-003-eval-s2-ckpt8000.log\", \"submitted_at\": \"2026-05-22T15:38:40.535Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/exp003_r3only_seed2/checkpoint-8000\", \"wall_clock_seconds\": 5203.1, \"gpu_hours\": 1.45}, \"reproduce\": {\"finished_at\": \"2026-05-22T17:03:18.652Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T17:03:22.278890+00:00\"}]}, \"metrics\": {\"SYCONScore\": 0.124, \"ToF\": 0.0663, \"NoF\": 0.9613, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362, \"checkpoint\": \"checkpoint-8000\", \"eval_script\": \"eval_unified_preset.py (D027 standard)\", \"eval_server\": \"westd-29046\", \"eval_time_sec\": 5010, \"vs_vanilla\": \"SYCONScore 0.1240 vs 0.1335 = -7.1%, BELOW baseline\", \"vs_seed1_ckpt8000\": \"SYCONScore 0.1240 vs 0.1433 = -13.5%, seed 2 worse than seed 1\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-22T17:05:23.614Z\"}, \"hint\": \"💡 建议将本次教训写入 memory.md（什么不 work、为什么）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9959}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "26c5ec7a-74bc-48da-96c7-b3a2f055f03a",
  "uuid": "0fe92b88-eaf8-4366-8e10-cc70441c0f43",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"exp-003-eval-s2-ckpt8000\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T15:37:04.686Z\\\", \\\"updated_at\\\": \\\"2026-05-22T17:05:23.614Z\\\", \\\"hypothesis\\\": \\\"Eval exp-003-s2 (R3-only seed 2) checkpoint-8000 (final) with D027 unified preset. Last R3-only seed 2 data point. Vanilla baseline SYCONScore=0.1335.\\\", \\\"parent\\\": \\\"exp-003-s2\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contrastive_entrain_calib && CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python eval/eval_unified_preset.py --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --lora_path /root/autodl-tmp/checkpoints/exp003_r3only_seed2/checkpoint-8000 --data_path /root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl --output_dir /root/contrastive_entrain_calib/results/exp003_d027_eval --exp_id exp003-s2-ckpt8000\\\\\\\"\\\", \\\"server\\\": \\\"westd-29046\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"517412\\\", \\\"log_path\\\": \\\"/root/runs/contrastive_entrain_calib/exp-003-eval-s2-ckpt8000.log\\\", \\\"submitted_at\\\": \\\"2026-05-22T15:38:40.535Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/exp003_r3only_seed2/checkpoint-8000\\\", \\\"wall_clock_seconds\\\": 5203.1, \\\"gpu_hours\\\": 1.45}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-22T17:03:18.652Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-22T17:03:22.278890+00:00\\\"}]}, \\\"metrics\\\": {\\\"SYCONScore\\\": 0.124, \\\"ToF\\\": 0.0663, \\\"NoF\\\": 0.9613, \\\"n_valid\\\": 181, \\\"n_invalid\\\": 181, \\\"n_total\\\": 362, \\\"checkpoint\\\": \\\"checkpoint-8000\\\", \\\"eval_script\\\": \\\"eval_unified_preset.py (D027 standard)\\\", \\\"eval_server\\\": \\\"westd-29046\\\", \\\"eval_time_sec\\\": 5010, \\\"vs_vanilla\\\": \\\"SYCONScore 0.1240 vs 0.1335 = -7.1%, BELOW baseline\\\", \\\"vs_seed1_ckpt8000\\\": \\\"SYCONScore 0.1240 vs 0.1433 = -13.5%, seed 2 worse than seed 1\\\"}, \\\"conclusion\\\": \\\"negative\\\", \\\"completed_at\\\": \\\"2026-05-22T17:05:23.614Z\\\"}, \\\"hint\\\": \\\"💡 建议将本次教训写入 memory.md（什么不 work、为什么）\\\"}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.9959}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"exp-003-eval-s2-ckpt8000\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T15:37:04.686Z\", \"updated_at\": \"2026-05-22T17:05:23.614Z\", \"hypothesis\": \"Eval exp-003-s2 (R3-only seed 2) checkpoint-8000 (final) with D027 unified preset. Last R3-only seed 2 data point. Vanilla baseline SYCONScore=0.1335.\", \"parent\": \"exp-003-s2\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contrastive_entrain_calib && CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python eval/eval_unified_preset.py --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --lora_path /root/autodl-tmp/checkpoints/exp003_r3only_seed2/checkpoint-8000 --data_path /root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl --output_dir /root/contrastive_entrain_calib/results/exp003_d027_eval --exp_id exp003-s2-ckpt8000\\\"\", \"server\": \"westd-29046\", \"gpu\": [\"cuda:1\"], \"pid\": \"517412\", \"log_path\": \"/root/runs/contrastive_entrain_calib/exp-003-eval-s2-ckpt8000.log\", \"submitted_at\": \"2026-05-22T15:38:40.535Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/exp003_r3only_seed2/checkpoint-8000\", \"wall_clock_seconds\": 5203.1, \"gpu_hours\": 1.45}, \"reproduce\": {\"finished_at\": \"2026-05-22T17:03:18.652Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T17:03:22.278890+00:00\"}]}, \"metrics\": {\"SYCONScore\": 0.124, \"ToF\": 0.0663, \"NoF\": 0.9613, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362, \"checkpoint\": \"checkpoint-8000\", \"eval_script\": \"eval_unified_preset.py (D027 standard)\", \"eval_server\": \"westd-29046\", \"eval_time_sec\": 5010, \"vs_vanilla\": \"SYCONScore 0.1240 vs 0.1335 = -7.1%, BELOW baseline\", \"vs_seed1_ckpt8000\": \"SYCONScore 0.1240 vs 0.1433 = -13.5%, seed 2 worse than seed 1\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-22T17:05:23.614Z\"}, \"hint\": \"💡 建议将本次教训写入 memory.md（什么不 work、为什么）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9959}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 31_

Registry 已更新。结果摘要：

## exp-003-eval-s2-ckpt8000 结果

| 指标 | 值 |
|------|-----|
| **SYCONScore** | **0.1240** |
| ToF | 0.0663 |
| NoF | 0.9613 |
| n_total | 362 (valid=181, invalid=181) |

### 对比

| 对比对象 | SYCONScore | 差值 |
|----------|-----------|------|
| Vanilla baseline | 0.1335 | **-7.1%** (低于 baseline) |
| Seed 1 ckpt-8000 | 0.1433 | **-13.5%** (seed 2 更差) |
| Seed 2 ckpt-7500 | 0.1140 | +8.8% (略有回升但仍低于 baseline) |

### Conclusion: **negative**

R3-only seed 2 全 trajectory 确认失败——从 ckpt-2000 到 ckpt-8000 的 SYCONScore 范围 0.0845~0.1240，始终低于 vanilla baseline 0.1335。Seed 2 表现一致性差于 seed 1（seed 1 ckpt-8000 达到 0.1433，勉强超过 baseline），说明 R3-only 训练的效果不稳定且跨 seed 不可靠。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "26c5ec7a-74bc-48da-96c7-b3a2f055f03a",
  "uuid": "2522f973-997a-4b1e-9d97-f307ce64d0ff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017V2rkpetkP2q9xF82wk6sr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1227,
      "cache_read_input_tokens": 42794,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1227
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

_source line 32_

Registry 已更新。结果摘要：

## exp-003-eval-s2-ckpt8000 结果

| 指标 | 值 |
|------|-----|
| **SYCONScore** | **0.1240** |
| ToF | 0.0663 |
| NoF | 0.9613 |
| n_total | 362 (valid=181, invalid=181) |

### 对比

| 对比对象 | SYCONScore | 差值 |
|----------|-----------|------|
| Vanilla baseline | 0.1335 | **-7.1%** (低于 baseline) |
| Seed 1 ckpt-8000 | 0.1433 | **-13.5%** (seed 2 更差) |
| Seed 2 ckpt-7500 | 0.1140 | +8.8% (略有回升但仍低于 baseline) |

### Conclusion: **negative**

R3-only seed 2 全 trajectory 确认失败——从 ckpt-2000 到 ckpt-8000 的 SYCONScore 范围 0.0845~0.1240，始终低于 vanilla baseline 0.1335。Seed 2 表现一致性差于 seed 1（seed 1 ckpt-8000 达到 0.1433，勉强超过 baseline），说明 R3-only 训练的效果不稳定且跨 seed 不可靠。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 67335,
  "duration_api_ms": 66329,
  "num_turns": 11,
  "stop_reason": "end_turn",
  "session_id": "26c5ec7a-74bc-48da-96c7-b3a2f055f03a",
  "total_cost_usd": 0.38297850000000005,
  "usage": {
    "input_tokens": 11,
    "cache_creation_input_tokens": 32180,
    "cache_read_input_tokens": 243489,
    "output_tokens": 2346,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 32180,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 403,
        "cache_read_input_tokens": 42794,
        "cache_creation_input_tokens": 1227,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1227
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1269,
      "outputTokens": 27,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0014039999999999999,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 11,
      "outputTokens": 2346,
      "cacheReadInputTokens": 243489,
      "cacheCreationInputTokens": 32180,
      "webSearchRequests": 0,
      "costUSD": 0.3815745,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "0c94c208-78c8-49e4-8305-8868a2b62cea"
}
```

</details>

---
