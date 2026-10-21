# analysis magnitude curve data

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 79
- **Recorded user turns:** 1
- **Tool calls:** 23
- **Original source:** `logs/workers/worker_analysis_magnitude-curve-data_20260516T185620.log`
- **Structured JSON:** [`4741ba08b444505241e9.json`](../../sessions/47/4741ba08b444505241e9.json)

## Before a recorded user message

13 recorded events

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
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
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
    "mcp__agent-ml-research__append_idea",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__save_project_file",
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
  "uuid": "0008c9ed-5e31-41e0-8ce5-35509e4f883c",
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
    "status": "allowed",
    "resetsAt": 1778964000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "9484664d-2f29-4db7-a874-d7d37364c296",
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the registry to get all relevant experiment data, then compile the magnitude curve data and write the Fisher test script.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "55ff9547-81f3-46e8-9b32-7bd60c346a19",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018vdstxS41L9NWwo3VjXupt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11916,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11916
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

### Assistant

_source line 5_

I'll read the registry to get all relevant experiment data, then compile the magnitude curve JSON and write the Fisher test script.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "d1e3aa68-5e26-4c32-9163-231e35fc0bc0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018vdstxS41L9NWwo3VjXupt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11916,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11916
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

_source line 6_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01FqitYjxJ6DMf2TTbZzW8xj`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
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
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "2b34172b-6a8d-4755-a7fc-e99643a17c06",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018vdstxS41L9NWwo3VjXupt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11916,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11916
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

_source line 7 · 2026-05-16T18:56:30.113Z_

<details><summary>↩ Tool result · `toolu_01FqitYjxJ6DMf2TTbZzW8xj`</summary>

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
  "tool_name": "mcp__agent-ml-research__register_artifact"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
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
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "ca7b7ea2-e945-466f-ba23-60c0f0c77c7b",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Assistant

_source line 8_

<details><summary>Logged reasoning block</summary>

```text
Let me read the registry to get all relevant experiments. I'll filter for DONE experiments first.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "814b9ebc-d7c6-4dff-8939-fbaeffbddae2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FG21MdiP76R8Vgc5gdcNw6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 23757,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1392
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_015ggQQ3mBGnQpuCgEor3YDL`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": {
    "status": "DONE"
  },
  "limit": 0,
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
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "9048e32e-498b-4a76-a2fe-96e355d887aa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FG21MdiP76R8Vgc5gdcNw6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 23757,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1392
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

_source line 10 · 2026-05-16T18:56:38.226Z_

<details><summary>↩ Tool result · `toolu_015ggQQ3mBGnQpuCgEor3YDL`</summary>

```text
Error: result (213,771 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/18137809-ea2c-4289-a326-73c48f2a7d35/tool-results/mcp-agent-ml-research-read_registry-1778957798211.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/18137809-ea2c-4289-a326-73c48f2a7d35/tool-results/mcp-agent-ml-research-read_registry-1778957798211.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/18137809-ea2c-4289-a326-73c48f2a7d35/tool-results/mcp-agent-ml-research-read_registry-1778957798211.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "541553c3-cadb-471a-a13a-f44894390f08",
  "tool_use_result": {
    "content": "Error: result (213,771 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/18137809-ea2c-4289-a326-73c48f2a7d35/tool-results/mcp-agent-ml-research-read_registry-1778957798211.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/18137809-ea2c-4289-a326-73c48f2a7d35/tool-results/mcp-agent-ml-research-read_registry-1778957798211.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/18137809-ea2c-4289-a326-73c48f2a7d35/tool-results/mcp-agent-ml-research-read_registry-1778957798211.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval-vla-mean-object-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T04:58:30.713Z\", \"updated_at\": \"2026-05-16T18:36:08.965Z\", \"hypothesis\": \"VLA-mean baseline (K=10, mean aggregation) seed=44 on LIBERO object benchmark. Completes seed=44 six-way comparison. seed42=12%, seed43=15%.\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-32546\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-16T04:58:47.863Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode mean --n_rollouts 10 --K 10 --seed 44 --output_file logs/eval_object_vla_mean_seed44.json\\\"\", \"finished_at\": \"2026-05-16T18:33:19.875Z\", \"training_hours\": 13.58}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode mean --n_rollouts 10 --K 10 --seed 44 --output_file logs/eval_object_vla_mean_seed44.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"212655\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-mean-object-seed44.log\", \"submitted_at\": \"2026-05-16T04:58:50.101Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 49038.9, \"gpu_hours\": 13.62}, \"pid\": \"212655\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-mean-object-seed44.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T18:33:23.084588+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.1, \"per_task_sr\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.1, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.3, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0.1, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0.1, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 0, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.2, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.2}}, \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed44.json\", \"completed_at\": \"2026-05-16T18:36:08.965Z\"}, \"eval-obs-only-object-norm02-seed44-r4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T14:48:54.894Z\", \"updated_at\": \"2026-05-16T15:36:08.207Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_seed44_r4.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"501420\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-seed44-r4.log\", \"submitted_at\": \"2026-05-16T14:49:19.300Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1956.7, \"gpu_hours\": 0.54}, \"hypothesis\": \"P0 retry #4: obs_only CRM v3-norm norm=0.2 seed=44 on LIBERO object. Third seed for Fisher test. seed42=22%, seed43=16%. Previous attempts failed (127/129/killed).\", \"pid\": 501420, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T15:21:56.018Z\", \"failure_reason\": \"r2 data valid (16%), r4 redundant. PID 501420 killed by worker at 2026-05-16T15:09.\"}, \"eval-argmin-object-seed44-r2\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-16T01:32:14.163Z\", \"updated_at\": \"2026-05-16T15:34:00.414Z\", \"hypothesis\": \"Retry of eval-argmin-object-seed44 (EXIT_CODE=127, missing conda activate). argmin baseline K=10 seed=44 on LIBERO object. Third seed for Fisher test. seed42=12%, seed43=17%.\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-18228\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-16T01:32:36.214Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 44 --K 10 --output_file logs/eval_object_reconvla_seed44.json\\\"\", \"finished_at\": \"2026-05-16T15:28:27.588Z\", \"training_hours\": 13.93}, \"completed_at\": \"2026-05-16T01:34:17.696Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"killed\"}, \"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T15:28:32.358640+00:00\"}]}, \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 44 --K 10 --output_file logs/eval_object_reconvla_seed44.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"428117\", \"seed\": 44, \"model_name\": \"reconvla_argmin\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.13, \"successes\": 13, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.5, \"orange_juice\": 0.2}, \"note\": \"EXIT_CODE=129 was SIGHUP after completion, results valid. log: logs/eval_object_reconvla_seed44.json\"}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed44.json\"}, \"eval-obs-only-object-norm02-seed44-r2\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-16T01:32:15.187Z\", \"updated_at\": \"2026-05-16T15:25:14.349Z\", \"hypothesis\": \"Retry of eval-obs-only-object-norm02-seed44 (EXIT_CODE=127, missing conda activate). obs_only CRM norm=0.2 seed=44 on LIBERO object. Third seed for Fisher test. seed42=22% (PROJECT HIGH).\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-18228\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-16T01:32:45.643Z\", \"finished_at\": \"2026-05-16T14:40:32.978Z\", \"training_hours\": 13.13}, \"completed_at\": \"2026-05-16T01:34:19.695Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"killed\"}, \"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T14:40:38.399800+00:00\"}]}, \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_seed44.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"428406\", \"seed\": 44, \"model_name\": \"crm_obs_only_norm02\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100}, \"failure_reason\": null, \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.16, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}, \"checkpoint_path\": \"logs/eval_object_obs_only_norm02_seed44.json\"}, \"eval-vla-only-object-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T08:34:53.953Z\", \"updated_at\": \"2026-05-16T15:22:52.157Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python src/evaluate.py --benchmark object --mode vla_only --K 1 --seed 45 --output_file logs/eval_object_vla_only_seed45.json\", \"server\": \"bjb2-28827\", \"gpu_id\": \"cuda:4\", \"pid\": 221407, \"seed\": 45, \"model_name\": \"smolvla_libero\", \"data_path\": \"LIBERO object\", \"data_count\": 10, \"checkpoint_source\": \"N/A\", \"eval_data\": \"LIBERO object\", \"hypothesis\": \"VLA-only baseline K=1 seed=45 on LIBERO object. Reference for seed45 statistical comparison. seed42=12%, seed43=12%, seed44=10%.\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T14:56:50.174Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T14:56:52.057Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T14:56:54.606880+00:00\"}]}, \"metrics\": {\"overall_sr\": 0.09, \"successes\": 18, \"total\": 200, \"tasks_done\": 10}}, \"eval-obs-only-object-norm03-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T11:14:47.376Z\", \"updated_at\": \"2026-05-16T11:30:59.542Z\", \"spec\": {\"model_name\": \"crm_v3_norm_obs_only\", \"seed\": 45, \"data_path\": \"LIBERO object benchmark (10 tasks)\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03_seed45.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"248860\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm03-seed45.log\", \"submitted_at\": \"2026-05-16T11:14:47Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 972.5, \"gpu_hours\": 0.27}, \"hypothesis\": \"obs_only CRM v3-norm at norm=0.3 seed=45 on LIBERO object benchmark. Multi-seed magnitude curve data point. seed42 norm=0.3=19%, seed44 norm=0.3=running. Extends magnitude robustness evidence to 3rd seed.\", \"conclusion\": \"failed\", \"failure_reason\": \"killed to resolve cuda:3 GPU conflict\", \"completed_at\": \"2026-05-16T11:30:59.542Z\"}, \"eval-mag-perdof-norm03-object-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:26:52.169Z\", \"updated_at\": \"2026-05-16T11:30:53.907Z\", \"spec\": {\"server\": \"bjb2-28827\", \"gpu\": \"cuda:2\", \"pid\": 140759, \"command\": \"python -u src/evaluate.py --mode crm_perdof --benchmark object --seed 42 --K 10 --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_r3.json\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_v3_norm_perdof\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\"}, \"metrics\": {\"overall_sr\": 0.04, \"successes\": 4, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10}, \"reproduce\": {\"finished_at\": \"2026-05-16T11:10:32.044Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T11:10:33.866Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T11:10:39.747200+00:00\"}]}}, \"eval-mag-perdof-norm02-seed43-object-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:34:16.821Z\", \"updated_at\": \"2026-05-16T10:41:59.362Z\", \"spec\": {\"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_perdof\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed43_r3.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"144504\"}, \"metrics\": {\"overall_sr\": 0.09, \"successes\": 9, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}, \"vs_seed42\": \"-2pp (11% → 9%)\", \"pooled_2seed_perdof_02\": \"10% (20/200)\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T10:39:30.416Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T10:39:33.739829+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"log_path\": \"logs/eval_object_perdof_norm02_seed43_r3.json\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T10:41:59.362Z\"}, \"eval-acr-object-v4-default-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:11:49.844Z\", \"updated_at\": \"2026-05-16T09:00:15.290Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_object_perdof_default_norm_r2.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"390936\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-default-r2.log\", \"submitted_at\": \"2026-05-16T02:11:20Z\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_object\", \"data_count\": 10, \"model_name\": \"crm_perdof_default_norm\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"object\", \"wall_clock_seconds\": 24535.3, \"gpu_hours\": 6.82}, \"hypothesis\": \"v4-default (no magnitude control, norm≈1.42) on object benchmark — ablation to confirm catastrophic failure\", \"parent\": \"eval-acr-object-v4-default\", \"metrics\": {\"overall_sr\": 0, \"successes\": 0, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0, \"bbq_sauce\": 0, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0, \"orange_juice\": 0}, \"note\": \"actual mode=crm_perdof with default norm (~1.42), NOT crm_default. Confirms catastrophic failure at uncontrolled correction magnitude.\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"completed_at\": \"2026-05-16T09:00:15.290Z\"}, \"eval-mag-perdof-norm005-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:56:58.178Z\", \"updated_at\": \"2026-05-16T08:38:02.524Z\", \"spec\": {\"hypothesis\": \"Object magnitude sweep: perdof CRM v3-norm at norm=0.05 on LIBERO object benchmark. Paired with obs_only norm=0.05 for magnitude comparison figure.\", \"parent\": \"eval-acr-object-v4-perdof\", \"command\": \"python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_perdof_norm005.json\", \"server\": \"bjb2-28827\", \"gpu\": \"1\", \"pid\": 109650, \"data_path\": \"LIBERO object benchmark\", \"data_count\": 10, \"model_name\": \"crm_perdof\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object (10 tasks x 10 rollouts)\", \"log_path\": \"logs/nohup_eval_object_perdof_norm005.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\"}, \"metrics\": {\"overall_sr\": 0.14, \"successes\": 14, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10}, \"reproduce\": {\"finished_at\": \"2026-05-16T08:36:33.616Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T08:36:35.355Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T08:36:40.842032+00:00\"}]}}, \"eval-mag-perdof-norm003-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:47:32.591Z\", \"updated_at\": \"2026-05-16T08:37:12.296Z\", \"hypothesis\": \"Object magnitude sweep: perdof CRM v3-norm at norm=0.03 on LIBERO object benchmark. Paired with obs_only norm=0.03 for magnitude comparison figure. Tests perdof at smallest correction norm on object domain.\", \"spec\": {\"command\": \"python src/evaluate.py --mode crm_perdof --max_correction_norm 0.03 --K 10 --seed 42 --benchmark object\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"pid\": 105938, \"log_path\": \"logs/eval_object_perdof_norm003.json\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_v3_perdof\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object\", \"parent\": \"eval-acr-object-v4-perdof\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"metrics\": {\"overall_success_rate\": 0.14, \"per_task_range\": \"0.0-0.4\"}}, \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.14, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.1}}, \"reproduce\": {\"finished_at\": \"2026-05-16T08:09:00.286Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T08:09:03.327886+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003.json\", \"completed_at\": \"2026-05-16T08:11:39.117Z\"}, \"eval-mag-obsonly-norm005-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:29:00.724Z\", \"updated_at\": \"2026-05-16T08:19:41.189Z\", \"spec\": {\"hypothesis\": \"Object magnitude sweep: obs_only CRM v3-norm at norm=0.05 on LIBERO object benchmark. Builds object magnitude curve alongside norm=0.1 (19%) and norm=0.2 (18% partial). Key data for fig3.\", \"parent\": \"eval-acr-object-v4-obs-only\", \"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_obs_only_norm005.json\", \"server\": \"bjb2-28827\", \"data_path\": \"simpler_env object benchmark\", \"data_count\": 10, \"model_name\": \"crm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"object benchmark, max_correction_norm=0.05, K=10, n_rollouts=10\", \"pid\": 101610, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005.log\"}, \"metrics\": {\"overall_sr\": 0.13, \"tasks_completed\": 10, \"total_rollouts\": 100, \"successes\": 13, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"success\", \"checkpoint_path\": \"logs/eval_object_obs_only_norm005.json\", \"completed_at\": \"2026-05-16T08:19:41.189Z\"}, \"eval-obs-only-object-norm02-seed43-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:58:27.783Z\", \"updated_at\": \"2026-05-16T07:46:23.704Z\", \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-seed43-r2.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}, \"hypothesis\": \"D031: obs_only CRM v3-norm norm=0.2 seed=43 on LIBERO object benchmark (r2 retry). P0 critical for statistical significance — seed42=22%, need seed43 pooled to 200 trials. Original crashed after 1 task.\", \"parent\": \"eval-obs-only-object-norm02-seed43\", \"metrics\": {\"overall_sr\": 0.16, \"successes\": 16, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}, \"vs_seed42\": \"-6pp (22% → 16%)\", \"vs_argmin_seed43\": \"-1pp (17% → 16%)\", \"pooled_2seed_obs_only_02\": \"19% (38/200)\", \"pooled_2seed_argmin\": \"14.5% (29/200)\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T07:21:07.838Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T07:21:10.900676+00:00\"}]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T07:23:48.849Z\"}, \"eval-mag-obsonly-norm03-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:29:02.155Z\", \"updated_at\": \"2026-05-16T07:42:44.267Z\", \"spec\": {\"hypothesis\": \"Object magnitude sweep: obs_only CRM v3-norm at norm=0.3 on LIBERO object benchmark. Tests degradation at higher correction norm on object domain. Key data for fig3.\", \"parent\": \"eval-acr-object-v4-obs-only\", \"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03.json\", \"server\": \"bjb2-28827\", \"data_path\": \"simpler_env object benchmark\", \"data_count\": 10, \"model_name\": \"crm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"object benchmark, max_correction_norm=0.3, K=10, n_rollouts=10\", \"pid\": 103028, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03.log\"}, \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.19, \"successes\": 19, \"total\": 100}, \"reproduce\": {\"finished_at\": \"2026-05-16T07:35:42.126Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T07:35:43.889Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T07:35:47.235304+00:00\"}]}}, \"eval-vla-only-object-seed44-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:33:13.916Z\", \"updated_at\": \"2026-05-16T07:13:29.827Z\", \"hypothesis\": \"Retry of eval-vla-only-object-seed44 (r1 EXIT_CODE=127). VLA-only baseline K=1 seed=44 on LIBERO object. Third seed reference. seed42=12%, seed43=12%.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 44 --K 1 --output_file logs/eval_object_vla_only_seed44.json\\\"\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"286989\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-object-seed44-r2.log\", \"submitted_at\": \"2026-05-16T01:33:46.467Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 20383.4, \"gpu_hours\": 5.66}, \"server\": \"bjb2-40593\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb2-40593\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-16T01:33:44.353Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 44 --K 1 --output_file logs/eval_object_vla_only_seed44.json\\\"\", \"code_commit\": \"4b4e03d05161290989b1f19d6e13e077da681a41\", \"finished_at\": \"2026-05-16T04:58:56.451Z\", \"training_hours\": 3.42}, \"pid\": \"286989\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-object-seed44-r2.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T04:59:00.452305+00:00\"}]}, \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.1, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (vla_only baseline)\", \"completed_at\": \"2026-05-16T07:13:29.827Z\"}, \"eval-mag-perdof-norm02-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:07:31.626Z\", \"updated_at\": \"2026-05-16T07:12:35.145Z\", \"spec\": {\"parent\": \"eval-acr-object-v4-perdof\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_perdof\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"object benchmark, max_correction_norm=0.2, K=10, n_rollouts=10\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"127732\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-perdof-norm02-object.log\"}, \"hypothesis\": \"Object magnitude sweep: perdof CRM v3-norm at norm=0.2 on LIBERO object benchmark. Paired with obs_only norm=0.2 (running, 18% at 5/10) for magnitude comparison figure. Tests perdof at moderate correction norm on object domain.\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.11, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}, \"reproduce\": {\"finished_at\": \"2026-05-16T06:04:45.416Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T06:04:48.447852+00:00\"}]}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"completed_at\": \"2026-05-16T07:12:35.145Z\"}, \"eval-acr-object-obs-only-default\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:38:22.125Z\", \"updated_at\": \"2026-05-16T07:09:01.967Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_default_norm.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": 134094, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-obs-only-default.log\", \"submitted_at\": \"2026-05-15T17:38:21.517Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_v3_norm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark\", \"wall_clock_seconds\": 48640.4, \"gpu_hours\": 13.51}, \"hypothesis\": \"obs_only CRM v3-norm with DEFAULT max_correction_norm (~1.42, no magnitude control) on LIBERO object benchmark. Paired with eval-acr-object-v4-default (perdof default). Tests whether obs_only robustness holds even without magnitude capping — if yes, obs_only is fundamentally more robust than perdof regardless of norm setting.\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.17, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.5, \"orange_juice\": 0.3}}, \"reproduce\": {\"finished_at\": \"2026-05-16T06:41:19.269Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T06:41:22.516205+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"completed_at\": \"2026-05-16T07:09:01.967Z\"}, \"eval-scalar-object-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:02:31.432Z\", \"updated_at\": \"2026-05-16T06:04:05.747Z\", \"hypothesis\": \"D031: scalar_unc CRM v3-norm seed=43 on LIBERO object benchmark. Completes seed=43 six-way comparison table. scalar seed=42 was worst at 4% — seed=43 confirms.\", \"parent\": \"eval-acr-object-v4-scalar\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_scalar_seed43.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"114664\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-scalar-object-seed43.log\", \"submitted_at\": \"2026-05-15T16:03:30.400Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_object\", \"data_count\": 10, \"model_name\": \"crm_scalar\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"eval_data\": \"object\", \"wall_clock_seconds\": 50435.3, \"gpu_hours\": 14.01}, \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"avg_sr\": 10, \"per_task_sr\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 30, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 10, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 30, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 30}}, \"reproduce\": {\"finished_at\": \"2026-05-16T06:01:42.952Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T06:01:45.993724+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed43.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed43.json\", \"completed_at\": \"2026-05-16T06:04:05.747Z\"}, \"eval-mag-obsonly-norm003-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:47:31.254Z\", \"updated_at\": \"2026-05-16T05:56:01.541Z\", \"hypothesis\": \"Object magnitude sweep: obs_only CRM v3-norm at norm=0.03 on LIBERO object benchmark. Completes 5-point magnitude curve (0.03/0.05/0.1/0.2/0.3). Tests minimum effective correction magnitude on object domain.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_obs_only_norm003.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": 121325, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm003-object.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"object benchmark, max_correction_norm=0.03, K=10, n_rollouts=10\", \"parent\": \"eval-acr-object-v4-obs-only\"}, \"metrics\": {\"overall_sr\": 0.16, \"tasks_done\": 100, \"tasks_total\": 100, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0.2, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.1, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.4, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_butter_and_place_it_in_the_basket\": 0.1, \"pick_up_the_milk_and_place_it_in_the_basket\": 0.2, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.3, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.3}}, \"reproduce\": {\"finished_at\": \"2026-05-16T05:35:17.752Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T05:35:20.742243+00:00\"}]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T05:56:01.541Z\"}, \"eval-scalar-object-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T05:02:34.914Z\", \"updated_at\": \"2026-05-16T05:25:06.306Z\", \"hypothesis\": \"scalar_unc CRM v3-norm seed=44 on LIBERO object benchmark. Completes seed=44 six-way comparison. scalar seed42=9%, seed43 running (0% at 3/10). Expected worst CRM variant.\", \"server\": \"bjb2-40593\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb2-40593\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-16T05:02:50.780Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_scalar_seed44.json\\\"\", \"code_commit\": \"4b4e03d05161290989b1f19d6e13e077da681a41\", \"finished_at\": \"2026-05-16T05:05:30.084Z\", \"training_hours\": 0.04}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_scalar_seed44.json\\\"\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"310854\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-scalar-object-seed44.log\", \"submitted_at\": \"2026-05-16T05:25:05.983Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"pid\": \"309346\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-scalar-object-seed44.log\", \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-16T05:05:32.021Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T05:05:34.587431+00:00\"}]}}, \"eval-obs-only-object-norm02-seed44-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:34:30.429Z\", \"updated_at\": \"2026-05-16T04:59:20.094Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_seed44.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"431189\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-seed44-r3.log\", \"submitted_at\": \"2026-05-16T01:34:30.132Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 12290.0, \"gpu_hours\": 3.41}, \"hypothesis\": \"Retry of eval-obs-only-object-norm02-seed44 (r1 EXIT_CODE=127, r2 killed by agent). obs_only CRM norm=0.2 seed=44 on LIBERO object. Third seed for Fisher test. seed42=22% (PROJECT HIGH).\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T04:59:20.095Z\"}, \"eval-argmin-object-seed44-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:34:28.047Z\", \"updated_at\": \"2026-05-16T04:59:17.975Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 44 --K 10 --output_file logs/eval_object_reconvla_seed44.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"430985\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-object-seed44-r3.log\", \"submitted_at\": \"2026-05-16T01:34:27.679Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 12290.3, \"gpu_hours\": 3.41}, \"hypothesis\": \"Retry of eval-argmin-object-seed44 (r1 EXIT_CODE=127, r2 killed by agent). argmin baseline K=10 seed=44 on LIBERO object. Third seed for Fisher test. seed42=12%, seed43=17%.\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T04:59:17.975Z\"}, \"eval-vla-mean-object-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:46:28.667Z\", \"updated_at\": \"2026-05-16T04:53:17.141Z\", \"hypothesis\": \"D031: VLA-mean baseline (K=10, mean aggregation) seed=43 on LIBERO object benchmark. Completes seed=43 comparison table. If VLA-mean seed=43 ≈ obs_only seed=43 → CRM correction claim compressed.\", \"parent\": \"eval-vla-mean-object\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode mean --n_rollouts 10 --K 10 --seed 43 --output_file logs/eval_object_vla_mean_seed43.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"111709\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-mean-object-seed43.log\", \"submitted_at\": \"2026-05-15T15:47:37.968Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 43, \"model_name\": \"smolvla\", \"data_path\": \"libero/object\", \"data_count\": 10, \"checkpoint_source\": null, \"eval_data\": \"object\", \"wall_clock_seconds\": 47139.2, \"gpu_hours\": 13.09}, \"metrics\": {\"overall_sr\": 0.15, \"tasks_done\": 10, \"tasks_total\": 10, \"total_success\": 15, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.3, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.1}}, \"reproduce\": {\"finished_at\": \"2026-05-16T04:48:28.380Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T04:48:31.493092+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval-only)\", \"completed_at\": \"2026-05-16T04:53:17.141Z\"}, \"eval-perdof-object-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:19:49.586Z\", \"updated_at\": \"2026-05-16T03:15:39.287Z\", \"hypothesis\": \"D031 supplementary: perdof CRM v3-norm seed=43 on LIBERO object benchmark. Completes three-way comparison (obs_only vs argmin vs perdof) with doubled samples. If perdof seed=43 ≈ argmin seed=43 → confirms obs_only uniquely better.\", \"parent\": \"eval-acr-object-v4-perdof\", \"spec\": {\"command\": \"python evaluate.py --benchmark object --mode crm_perdof --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1 --K 10 --seed 43 --n_rollouts 10 --output_file logs/eval_object_perdof_seed43.json\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"pid\": 365925, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-seed43.log\", \"submitted_at\": \"2026-05-15T13:21:00.347Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 43, \"model_name\": \"crm_perdof\", \"data_path\": \"LIBERO_object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO_object_10tasks_10rollouts\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"wall_clock_seconds\": 50078.9, \"gpu_hours\": 13.91}, \"metrics\": {\"overall_success_rate\": 0.12, \"tasks_done\": 10, \"tasks_total\": 10, \"total_rollouts\": 100, \"total_successes\": 12, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}, \"reproduce\": {\"finished_at\": \"2026-05-16T03:12:36.498Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T03:12:39.589841+00:00\"}]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T03:15:39.287Z\"}, \"eval-vla-only-object-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:29:00.342Z\", \"updated_at\": \"2026-05-16T01:33:29.678Z\", \"hypothesis\": \"D035 follow-up: VLA-only baseline (K=1) seed=44 on LIBERO object benchmark. Third seed reference point. seed42=12%, seed43=12%. Deployed on bjb2-40593.\", \"server\": \"bjb2-40593\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb2-40593\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-16T01:29:36.987Z\", \"command\": \"bash -c \\\"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 44 --K 1 --output_file logs/eval_object_vla_only_seed44.json\\\"\", \"code_commit\": \"4b4e03d05161290989b1f19d6e13e077da681a41\", \"finished_at\": \"2026-05-16T01:30:26.640Z\", \"training_hours\": 0.01}, \"spec\": {\"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"vla_only\", \"seed\": 44, \"checkpoint_source\": \"N/A\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\"}, \"pid\": \"unknown\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-object-seed44.log\", \"failure_reason\": \"EXIT_CODE=127 (command not found) — bash -c wrapping 或环境激活路径错误，bjb2-40593 上系统性问题，三个 seed44 实验全部同样失败\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-16T01:30:33.143Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T01:30:38.635650+00:00\"}]}}, \"eval-obs-only-object-norm02-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:28:59.304Z\", \"updated_at\": \"2026-05-16T01:32:51.127Z\", \"hypothesis\": \"D035 follow-up: obs_only CRM v3-norm norm=0.2 seed=44 on LIBERO object benchmark. Third seed for Fisher exact test. ε=0.2 is PROJECT HIGH config (seed42=22%). Paired with eval-argmin-object-seed44.\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-18228\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-16T01:29:31.218Z\", \"command\": \"bash -c \\\"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_seed44.json\\\"\", \"finished_at\": \"2026-05-16T01:30:14.217Z\", \"training_hours\": 0.01}, \"spec\": {\"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_obs_only (327198 params)\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\"}, \"pid\": \"unknown\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-seed44.log\", \"failure_reason\": \"EXIT_CODE=127: submit command missing conda activation (source /root/miniconda3/etc/profile.d/conda.sh && conda activate base). tmux runs sh, not bash — python not in PATH. Will retry as r2.\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-16T01:30:20.761Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T01:30:23.773246+00:00\"}]}}, \"eval-argmin-object-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:28:58.358Z\", \"updated_at\": \"2026-05-16T01:32:49.190Z\", \"hypothesis\": \"D035 follow-up: argmin baseline (K=10) seed=44 on LIBERO object benchmark. Third seed for Fisher exact test statistical power. Paired with eval-obs-only-object-norm02-seed44. seed42=12%, seed43=17%.\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-18228\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-16T01:29:25.990Z\", \"command\": \"bash -c \\\"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 44 --K 10 --output_file logs/eval_object_reconvla_seed44.json\\\"\", \"finished_at\": \"2026-05-16T01:30:04.115Z\", \"training_hours\": 0.01}, \"spec\": {\"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"ReconVLA (argmin baseline)\", \"seed\": 44, \"checkpoint_source\": \"N/A (no CRM)\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\"}, \"pid\": \"unknown\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-object-seed44.log\", \"failure_reason\": \"EXIT_CODE=127: submit command missing conda activation (source /root/miniconda3/etc/profile.d/conda.sh && conda activate base). tmux runs sh, not bash — python not in PATH. Will retry as r2.\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-16T01:30:06.598Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T01:30:09.864458+00:00\"}]}}, \"eval-obs-only-object-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:58:46.063Z\", \"updated_at\": \"2026-05-16T00:51:14.618Z\", \"hypothesis\": \"D031: obs_only CRM v3-norm seed=43 on LIBERO object benchmark. Doubles sample size for Fisher exact test. seed=42 shows obs_only 16% vs argmin 8% (+8pp, p≈0.19). Combined 200 trials target p < 0.05.\", \"parent\": \"eval-acr-object-v4-obs-only\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_obs_only_seed43.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"356490\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_seed43.json\", \"submitted_at\": \"2026-05-15T12:00:38.618Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_obs_only + SmolVLA\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark (10 tasks x 10 rollouts)\", \"wall_clock_seconds\": 46070.8, \"gpu_hours\": 12.8, \"checkpoint_path\": \"N/A (eval only)\"}, \"metrics\": {\"overall_success_rate\": 0.12, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}, \"vs_argmin_seed43\": {\"obs_only\": 12, \"argmin\": 17, \"diff\": -5}, \"fisher_pooled\": {\"obs_only_total\": \"31/200\", \"argmin_total\": \"29/200\", \"pooled_obs_only_sr\": 0.155, \"pooled_argmin_sr\": 0.145, \"pooled_delta\": 0.01, \"odds_ratio\": 1.08, \"p_value_one_sided\": 0.4444, \"p_value_two_sided\": 0.8888}, \"source\": \"json_file_verified_by_worker\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T00:41:25.212Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T00:42:01.902179+00:00\"}]}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_seed43.json\", \"completed_at\": \"2026-05-16T00:48:29.446Z\"}, \"eval-mag-obsonly-norm003-b2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:20:45.606Z\", \"updated_at\": \"2026-05-16T00:51:03.335Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_mag_obsonly_norm003.json\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"225139\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm003-b2.log\", \"submitted_at\": \"2026-05-15T05:20:45.407Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_spatial\", \"data_count\": 10, \"model_name\": \"crm_v3_norm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"libero_spatial\", \"wall_clock_seconds\": 70039.8, \"gpu_hours\": 19.46}, \"pid\": 227426, \"notes\": \"Ghost PID 211962 killed, b2 now running solo on bjb2-40593 cuda:0. PID 227434 confirmed alive (15min uptime, model loaded, eval executing, GPU 6185MiB/24564MiB, 12% util).\", \"metrics\": {\"overall_sr_10task\": 0.34, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task\": {\"between_plate_and_ramekin\": 0.9, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.8, \"on_stove\": 0, \"next_to_plate\": 0.3, \"on_wooden_cabinet\": 0}}, \"reproduce\": {\"finished_at\": \"2026-05-16T00:42:50.652Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T00:43:27.876843+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_mag_obsonly_norm003.json\", \"completed_at\": \"2026-05-16T00:48:05.254Z\"}, \"eval-mag-obsonly-norm03-b2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:05:41.192Z\", \"updated_at\": \"2026-05-16T00:49:21.141Z\", \"hypothesis\": \"Magnitude sweep: obs_only CRM v3-norm at norm=0.3 on spatial. Retry of eval-mag-obsonly-norm03 (EXIT_CODE=127). Fills obs_only norm=0.3 gap. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade, strong evidence for obs_only robustness.\", \"parent\": \"eval-mag-obsonly-norm03\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_mag_obsonly_norm03_b2.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"130104\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm03-b2.log\", \"submitted_at\": \"2026-05-15T19:11:50.323Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 20250.8, \"gpu_hours\": 5.63}, \"conclusion\": \"failed\", \"notes\": \"Killed: duplicate of eval-mag-obsonly-norm03-r2 on same cuda:0. r2 had 15min more progress. Both wrote same output_file, causing potential corruption.\", \"reproduce\": {\"finished_at\": \"2026-05-15T07:10:36.759Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T07:10:39.645469+00:00\"}]}, \"completed_at\": \"2026-05-16T00:49:21.141Z\"}, \"eval-argmin-object-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:58:46.739Z\", \"updated_at\": \"2026-05-16T00:37:43.289Z\", \"hypothesis\": \"D031: argmin baseline (K=10, scalar Euclidean argmin) seed=43 on LIBERO object benchmark. Paired with eval-obs-only-object-seed43 for Fisher exact test. Need both conditions under same seed for valid comparison.\", \"parent\": \"eval-reconvla-object\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 43 --K 10 --output_file logs/eval_object_reconvla_seed43.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"356696\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-object-seed43.log\", \"submitted_at\": \"2026-05-15T12:00:40.708Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"ReconVLA (reconvla baseline)\", \"seed\": 43, \"checkpoint_source\": \"N/A (no CRM, pure VLA baseline)\", \"eval_data\": \"LIBERO object benchmark (10 tasks x 10 rollouts)\", \"checkpoint_path\": \"N/A\", \"wall_clock_seconds\": 45422.6, \"gpu_hours\": 12.62}, \"metrics\": {\"overall_success_rate\": 0.17, \"total_successes\": 17, \"total_trials\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.3, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}, \"reproduce\": {\"finished_at\": \"2026-05-16T00:35:16.646Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T00:35:19.825582+00:00\"}]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T00:37:43.289Z\"}, \"eval-mag-perdof-norm02-seed43-object-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:19:36.419Z\", \"updated_at\": \"2026-05-15T19:38:38.710Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed43.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"138858\", \"log_path\": \"N/A\", \"submitted_at\": \"2026-05-15T19:19:36.128Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (killed — GPU conflict on cuda:2, replaced by eval-mag-perdof-norm02-seed43-object-r3)\", \"wall_clock_seconds\": 951.1, \"gpu_hours\": 0.26}, \"hypothesis\": \"Object magnitude sweep: perdof CRM v3-norm norm=0.2 seed=43. Moved from bjb2-28827:cuda:3 (GPU conflict with obs_only spatial) to cuda:2. Tests perdof norm sensitivity with second seed.\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:35:27.220Z\"}, \"eval-mag-obsonly-norm03\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:43:48.583Z\", \"updated_at\": \"2026-05-15T19:38:31.587Z\", \"hypothesis\": \"Magnitude sweep: obs_only CRM v3-norm at norm=0.3 on spatial. Fills obs_only norm=0.3 gap. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade at same norm, strong evidence for obs_only robustness.\", \"parent\": \"eval-mag-obsonly-norm02\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_mag_obsonly_norm03.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"unknown\", \"log_path\": \"N/A\", \"submitted_at\": \"2026-05-15T06:44:02.425Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (EXIT_CODE=127, retried as eval-mag-obsonly-norm03-r2)\", \"wall_clock_seconds\": 46287.3, \"gpu_hours\": 12.86}, \"reproduce\": {\"finished_at\": \"2026-05-15T06:44:32.019Z\"}, \"failure_reason\": \"EXIT_CODE=127 (command not found — check bash -c wrapping / env activate)\", \"conclusion\": \"killed\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T06:44:35.317393+00:00\"}]}, \"notes\": \"失败原因: EXIT_CODE=127 — tmux 用 sh 执行命令，python 不在 sh PATH 中。修复: bash -c 包裹。已重试为 eval-mag-obsonly-norm03-r2。\", \"completed_at\": \"2026-05-15T19:35:29.718Z\"}, \"eval-mag-obsonly-norm02-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:26:53.269Z\", \"updated_at\": \"2026-05-15T19:34:07.651Z\", \"spec\": {\"hypothesis\": \"Object magnitude sweep: obs_only CRM v3-norm at norm=0.2 on LIBERO object benchmark. Fills the norm=0.2 gap in 5-point magnitude curve. Previous run reached 18% at 5/10 then stopped.\", \"parent\": \"eval-acr-object-v4-obs-only\", \"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_v2.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": 141024, \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark\", \"checkpoint_path\": \"N/A (duplicate of DONE eval-acr-object-obs-only-norm02, killed to free GPU)\", \"log_path\": \"N/A\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:34:07.651Z\"}, \"eval-mag-obsonly-norm03-b4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:14:01.998Z\", \"updated_at\": \"2026-05-15T19:27:30.465Z\", \"spec\": {\"command\": \"crm_obs_only spatial norm=0.3 (killed)\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"132816\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm03-b4.log\", \"submitted_at\": \"2026-05-15T19:14:01.050Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"spatial\", \"data_count\": 10, \"model_name\": \"crm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"spatial\", \"wall_clock_seconds\": 809.4, \"gpu_hours\": 0.22}, \"conclusion\": \"killed\", \"notes\": \"Redundant: spatial obs_only norm=0.3 already has 10t final data (36%). Killed from cuda:2 GPU contention cleanup on bjb2-28827 (2026-05-16).\", \"completed_at\": \"2026-05-15T19:27:30.465Z\"}, \"eval-mag-obsonly-norm03-b3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:13:38.067Z\", \"updated_at\": \"2026-05-15T19:27:28.479Z\", \"spec\": {\"command\": \"crm_obs_only spatial norm=0.3 (killed)\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"134532\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm03-b3.log\", \"submitted_at\": \"2026-05-15T19:14:52.972Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"spatial\", \"data_count\": 10, \"model_name\": \"crm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"spatial\", \"wall_clock_seconds\": 755.5, \"gpu_hours\": 0.21}, \"hypothesis\": \"Retry of eval-mag-obsonly-norm03-b2 (spatial magnitude sweep obs_only norm=0.3). Submitted on bjb2-28827:cuda:2 instead of bjb1-32546:cuda:3 (cuda:3 occupied by P0 obs-only-norm02-seed43-r2). Director approved.\", \"parent\": \"eval-mag-obsonly-norm03-b2\", \"conclusion\": \"killed\", \"notes\": \"Redundant: spatial obs_only norm=0.3 already has 10t final data (36%). Killed from cuda:2 GPU contention cleanup on bjb2-28827 (2026-05-16).\", \"completed_at\": \"2026-05-15T19:27:28.479Z\"}, \"eval-mag-perdof-norm02-seed43-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:15:19.724Z\", \"updated_at\": \"2026-05-15T19:25:28.957Z\", \"spec\": {\"hypothesis\": \"Object magnitude sweep: perdof CRM v3-norm norm=0.2 seed=43 on LIBERO object benchmark. Paired with obs_only norm=0.2 seed=43 for statistical comparison at the best obs_only norm.\", \"parent\": \"eval-mag-perdof-norm02-object\", \"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed43.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": \"10 rollouts\", \"model_name\": \"crm_v3_norm/perdof\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark\"}, \"conclusion\": \"killed\", \"notes\": \"Killed during cuda:2/3 GPU cleanup on bjb2-28827 (2026-05-16). Was sharing cuda:2 with perdof norm=0.3 r2.\", \"completed_at\": \"2026-05-15T19:25:28.957Z\"}, \"eval-mag-perdof-norm03-object-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:15:16.452Z\", \"updated_at\": \"2026-05-15T19:25:28.055Z\", \"spec\": {\"hypothesis\": \"Object magnitude sweep: perdof CRM v3-norm at norm=0.3 on LIBERO object benchmark. Retry of killed eval-mag-perdof-norm0p3-object. Completes perdof 5-point magnitude curve on object domain.\", \"parent\": \"eval-acr-object-v4-perdof\", \"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_r2.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": \"10 rollouts\", \"model_name\": \"crm_v3_norm/perdof\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark\"}, \"conclusion\": \"killed\", \"notes\": \"GPU contention on cuda:2 (shared with perdof norm=0.2 seed=43). Killed 2026-05-16. Replaced by r3 clean restart.\", \"completed_at\": \"2026-05-15T19:25:28.055Z\"}, \"eval-acr-object-v4-scalar-b2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T02:55:02.698Z\", \"updated_at\": \"2026-05-15T19:17:41.948Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"7017\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-scalar-b2.log\", \"submitted_at\": \"2026-05-15T02:55:02.415Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 58959.5, \"gpu_hours\": 16.38}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:17:41.948Z\"}, \"eval-acr-object-v4-obs-only-b2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T02:55:00.179Z\", \"updated_at\": \"2026-05-15T19:17:40.199Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"pid\": \"6746\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-obs-only-b2.log\", \"submitted_at\": \"2026-05-15T02:54:59.912Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 58960.3, \"gpu_hours\": 16.38}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:17:40.199Z\"}, \"eval-spatial-v4-full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T18:58:07.302Z\", \"updated_at\": \"2026-05-15T19:17:39.068Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl && python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 10 --seed 42 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ 2>&1\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"69379\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-spatial-v4-full.log\", \"submitted_at\": \"2026-05-13T18:58:07.274Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"D015: evaluate.py env_args 缺少 camera_names，SmolVLA 只收到单摄像头输入，结果系统性偏低\", \"wall_clock_seconds\": 173971.8, \"gpu_hours\": 48.33}, \"conclusion\": \"killed\", \"reproduce\": {\"finished_at\": \"2026-05-13T19:36:15.749Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T19:36:19.370112+00:00\"}]}, \"completed_at\": \"2026-05-15T19:17:39.068Z\"}, \"eval-reconvla-spatial-v1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:15:35.450Z\", \"updated_at\": \"2026-05-15T19:17:37.622Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --smolvla_path /root/autodl-tmp/models/smolvla_libero/\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"87787\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-reconvla-spatial-v1.log\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": \"10 tasks x 10 rollouts x 300 steps\", \"model_name\": \"lerobot/smolvla_libero (450M) + ReconVLA argmin selection K=10\", \"seed\": 42, \"hypothesis\": \"ReconVLA (scalar Euclidean nonconformity + argmin) as baseline for ACR-VLA comparison\", \"checkpoint_source\": \"lerobot/smolvla_libero\"}, \"reproduce\": {\"finished_at\": \"2026-05-13T22:59:43.231Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"conclusion\": \"killed\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T20:26:37.521060+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T22:59:44.694612+00:00\"}]}, \"completed_at\": \"2026-05-15T19:17:37.622Z\"}, \"eval-object-v6-full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:28:33.119Z\", \"updated_at\": \"2026-05-15T19:17:36.369Z\", \"spec\": {\"data_path\": \"/root/autodl-tmp/libero_data/ (object)\", \"data_count\": 100, \"model_name\": \"lerobot/smolvla_libero\", \"seed\": 42, \"hypothesis\": \"SmolVLA baseline success rate on libero_object with fixed evaluate.py (env.reset bug removed, 5-step zero-action stabilization)\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"libero_object 10 tasks x 10 rollouts\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:17:36.369Z\"}, \"precompute-v4-shard2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T18:58:14.301Z\", \"updated_at\": \"2026-05-15T19:17:35.000Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 2 --num_shards 3 --seed 42 --K 10 --cache_dir /root/autodl-tmp/crm_cache/ 2>&1\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"69937\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v4-shard2.log\", \"submitted_at\": \"2026-05-13T18:58:14.266Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache/\", \"wall_clock_seconds\": 173960.7, \"gpu_hours\": 48.32}, \"reproduce\": {\"finished_at\": \"2026-05-13T20:09:25.582Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T20:09:26.379476+00:00\"}]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T19:17:35.000Z\"}, \"precompute-v4-shard1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T18:58:12.183Z\", \"updated_at\": \"2026-05-15T19:17:33.288Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 1 --num_shards 3 --seed 42 --K 10 --cache_dir /root/autodl-tmp/crm_cache/ 2>&1\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"69793\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v4-shard1.log\", \"submitted_at\": \"2026-05-13T18:58:12.154Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache/\", \"wall_clock_seconds\": 173961.1, \"gpu_hours\": 48.32}, \"reproduce\": {\"finished_at\": \"2026-05-13T20:04:22.574Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T20:04:23.366356+00:00\"}]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T19:17:33.288Z\"}, \"precompute-v4-shard0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T18:58:09.830Z\", \"updated_at\": \"2026-05-15T19:17:32.128Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 0 --num_shards 3 --seed 42 --K 10 --cache_dir /root/autodl-tmp/crm_cache/ 2>&1\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"69647\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v4-shard0.log\", \"submitted_at\": \"2026-05-13T18:58:09.802Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache/\", \"wall_clock_seconds\": 173962.3, \"gpu_hours\": 48.32}, \"reproduce\": {\"finished_at\": \"2026-05-13T20:04:45.258Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T20:04:50.222546+00:00\"}]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T19:17:32.128Z\"}, \"precompute-v3-shard2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T17:39:04.708Z\", \"updated_at\": \"2026-05-15T19:17:30.541Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 2 --num_shards 3 --seed 42 --K 10 --cache_dir /root/autodl-tmp/crm_cache_v3\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"63218\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v3-shard2.log\", \"submitted_at\": \"2026-05-13T17:39:04.684Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"D014: wrapper 修复版从未部署到服务器，使用旧 buggy 代码运行，产出无效\", \"wall_clock_seconds\": 178705.9, \"gpu_hours\": 49.64}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:17:30.541Z\"}, \"precompute-v3-shard1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T17:39:02.628Z\", \"updated_at\": \"2026-05-15T19:17:29.292Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 1 --num_shards 3 --seed 42 --K 10 --cache_dir /root/autodl-tmp/crm_cache_v3\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"63075\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v3-shard1.log\", \"submitted_at\": \"2026-05-13T17:39:02.603Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"D014: wrapper 修复版从未部署到服务器，使用旧 buggy 代码运行，产出无效\", \"wall_clock_seconds\": 178706.7, \"gpu_hours\": 49.64}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:17:29.293Z\"}, \"precompute-v3-shard0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T17:39:00.259Z\", \"updated_at\": \"2026-05-15T19:17:27.703Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 && rm -rf /root/autodl-tmp/crm_cache_v3 && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 0 --num_shards 3 --seed 42 --K 10 --cache_dir /root/autodl-tmp/crm_cache_v3\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"62930\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v3-shard0.log\", \"submitted_at\": \"2026-05-13T17:39:00.236Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"D014: wrapper 修复版从未部署到服务器，使用旧 buggy 代码运行，产出无效\", \"wall_clock_seconds\": 178707.5, \"gpu_hours\": 49.64}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:17:27.703Z\"}, \"precompute-v2-shard2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T16:11:04.275Z\", \"updated_at\": \"2026-05-15T19:17:26.396Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 2 --num_shards 3 --seed 42 --K 10\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"57846\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v2-shard2.log\", \"submitted_at\": \"2026-05-13T16:11:04.255Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 183982.1, \"gpu_hours\": 51.11}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:17:26.396Z\"}, \"precompute-v2-shard1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T16:11:02.520Z\", \"updated_at\": \"2026-05-15T19:17:25.022Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 1 --num_shards 3 --seed 42 --K 10\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"57706\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v2-shard1.log\", \"submitted_at\": \"2026-05-13T16:11:02.500Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 183982.5, \"gpu_hours\": 51.11}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:17:25.022Z\"}, \"precompute-v2-shard0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T16:11:01.629Z\", \"updated_at\": \"2026-05-15T19:17:23.631Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && rm -rf /root/autodl-tmp/crm_cache/spatial /root/autodl-tmp/crm_cache/object && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 0 --num_shards 3 --seed 42 --K 10\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"57628\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v2-shard0.log\", \"submitted_at\": \"2026-05-13T16:11:01.605Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 183982.0, \"gpu_hours\": 51.11}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:17:23.631Z\"}, \"eval-mag-perdof-norm0p3-object-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:58:30.091Z\", \"updated_at\": \"2026-05-15T19:13:43.549Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_r2.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"127570\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-perdof-norm0p3-object-r2.log\", \"submitted_at\": \"2026-05-15T18:58:29.637Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"libero_object 10 tasks x 10 rollouts\", \"data_path\": \"/root/autodl-tmp/libero_data/ (object)\", \"data_count\": 100, \"model_name\": \"crm_perdof_v3_norm\", \"seed\": 42, \"wall_clock_seconds\": 885.6, \"gpu_hours\": 0.25}, \"hypothesis\": \"Object magnitude sweep: perdof CRM v3-norm at norm=0.3 on LIBERO object benchmark. Migrated from bjb1-32546:cuda:4 (GPU conflict) to bjb2-28827:cuda:2. Paired with obs_only norm=0.3 for magnitude comparison figure.\", \"parent\": \"eval-mag-perdof-norm0p3-object\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:13:15.247Z\", \"failure_reason\": \"Duplicate of eval-mag-perdof-norm03-object (PID 118886 on bjb2-28827:cuda:3, identical params). Killed to free cuda:2.\"}, \"eval-vla-only-object-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:50:14.071Z\", \"updated_at\": \"2026-05-15T19:11:30.342Z\", \"spec\": {\"hypothesis\": \"D031: VLA-only baseline (K=1, single sample, no CRM) seed=43 on LIBERO object benchmark. Completes 7-way seed=43 comparison table. VLA-only seed=42 = 12% = argmin.\", \"parent\": \"eval-vla-only-object\", \"command\": \"CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 43 --K 1 --output_file logs/eval_object_vla_only_seed43.json\", \"server\": \"bjb1-32546\", \"data_path\": \"libero_object\", \"data_count\": 10, \"model_name\": \"vla_only\", \"seed\": 43, \"eval_data\": \"object\"}, \"metrics\": {\"overall_sr\": 0.12, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}, \"source\": \"json_file_verified_by_worker\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T18:46:38.180Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T18:46:39.481Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T18:46:41.461084+00:00\"}]}, \"notes\": \"seed=43 VLA-only 12% = seed=42 12%，baseline 跨 seed 完全一致。per-task 分布略有差异（seed43: chocolate_pudding 40% vs seed42: 20%, bbq_sauce 30% vs 20%），但总 SR 相同。确认 VLA-only 作为稳定 baseline。seed=43 六方对比表第一个完成点。\"}, \"eval-mag-perdof-norm0p3-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:34:52.454Z\", \"updated_at\": \"2026-05-15T18:58:11.790Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"144887\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-perdof-norm0p3-object.log\", \"submitted_at\": \"2026-05-15T18:37:26.089Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1245.7, \"gpu_hours\": 0.35}, \"hypothesis\": \"Retry of eval-mag-perdof-norm03-object (killed by SIGTERM). Object magnitude sweep: perdof CRM v3-norm at norm=0.3 on LIBERO object benchmark. Paired with obs_only norm=0.3 (running) for magnitude comparison figure.\", \"parent\": \"eval-mag-perdof-norm03-object\", \"conclusion\": \"killed\", \"failure_reason\": \"GPU conflict on bjb1-32546:cuda:4 (shared with obs-only-default). Killed lower priority perdof. Migrating to bjb2-28827:cuda:2 as r2.\", \"completed_at\": \"2026-05-15T18:58:11.790Z\"}, \"eval-obs-only-object-norm02-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:38:18.819Z\", \"updated_at\": \"2026-05-15T18:58:10.821Z\", \"hypothesis\": \"D031: obs_only CRM v3-norm norm=0.2 seed=43 on LIBERO object benchmark. norm=0.2 shows strongest signal (18% SR at 5/10 tasks in seed=42). Seed=43 doubling for statistical power on the best-performing configuration.\", \"parent\": \"eval-acr-object-obs-only-norm02\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_seed43.json\", \"server\": \"bjb1-32546\", \"data_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed43.json\", \"data_count\": 10, \"model_name\": \"crm_obs_only\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"object\"}, \"metrics\": {\"pid\": 118214, \"gpu\": 3, \"process_status\": \"alive\", \"log_file\": \"logs/eval_object_obs_only_norm02_seed43.log\"}, \"conclusion\": \"failed\", \"failure_reason\": \"Crashed after 1 task on bjb1-32546:cuda:3 (PID 118214). Reviewer confirmed. Restarting as r2.\", \"completed_at\": \"2026-05-15T18:58:10.821Z\"}, \"eval-acr-object-v4-default\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:18:17.209Z\", \"updated_at\": \"2026-05-15T17:38:37.815Z\", \"hypothesis\": \"Ablation: perdof CRM v3-norm with DEFAULT max_correction_norm (~1.42, no magnitude control) on LIBERO object benchmark. Tests whether magnitude control is essential on object domain too. If v4-default << v4-perdof (norm=0.1) → magnitude control is universally needed. If v4-default ≈ v4-perdof → spatial failure was anomalous.\", \"parent\": \"eval-acr-object-v4-perdof\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_object_perdof_default_norm.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"107658\", \"log_path\": \"logs/eval_object_perdof_default_norm.log\", \"submitted_at\": \"2026-05-16T00:51:00Z\", \"backend\": \"nohup\", \"account\": \"root\", \"data_path\": \"libero_object\", \"data_count\": 10, \"model_name\": \"crm_perdof_default_norm\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"object\"}, \"metrics\": {\"tasks_done\": 3, \"tasks_total\": 10, \"status\": \"DEAD\", \"partial_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0}, \"pid_42311\": \"not_found\", \"needs_restart\": true, \"checked_at\": \"2026-05-16T01:00Z\"}, \"notes\": \"Killed per Director instruction. 3/10 tasks all 0% SR, no magnitude control (norm≈1.42). Conclusion obvious — magnitude control is essential.\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T17:38:37.815Z\"}, \"eval-acr-object-obs-only-norm02\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:20:46.639Z\", \"updated_at\": \"2026-05-15T17:37:08.420Z\", \"spec\": {\"hypothesis\": \"obs-only CRM with norm=0.2 on object benchmark. Cross-benchmark norm sensitivity test — paired with eval-mag-obsonly-norm02 on spatial. If obs-only at norm=0.2 > norm=0.1 on both benchmarks → robust 'observation-conditioned correction' story.\", \"parent\": \"eval-acr-object-v4-obs-only\", \"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02.json\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:4\", \"pid\": 44270, \"tmux_session\": \"eval-acr-object-obs-only-norm02\", \"data_path\": \"LIBERO object benchmark (10 tasks)\", \"data_count\": 100, \"model_name\": \"crm_obs_only (327198 params)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark, 10 tasks x 10 rollouts\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-obs-only-norm02.log\"}, \"metrics\": {\"overall_sr\": 0.22, \"total_success\": 22, \"total_rollouts\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.4, \"ketchup\": 0.2, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.6, \"orange_juice\": 0.3}}, \"reproduce\": {\"finished_at\": \"2026-05-15T17:35:34.272Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:35:39.374197+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-obs-only-norm02.log\", \"completed_at\": \"2026-05-15T17:37:08.420Z\"}, \"eval-mag-perdof-norm02\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:16:13.281Z\", \"updated_at\": \"2026-05-15T17:30:15.807Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode acr_vla --max_correction_norm 0.2 --n_rollouts 10 --K 10 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_mag_perdof_norm02.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"SmolVLA + CRM-v3-norm-perdof\", \"seed\": 42, \"checkpoint_source\": \"crm-train-v3-norm-perdof\", \"eval_data\": \"LIBERO spatial\"}, \"gpu\": \"bjb2-28827:cuda:2\", \"pid\": 13728, \"metrics\": {\"tasks_done\": \"6/10\", \"partial_results\": {\"T0_between_plate_ramekin\": \"60%\", \"T1_next_to_ramekin\": \"90%\", \"T2_table_center\": \"0%\", \"T3_on_cookie_box\": \"20%\", \"T4_top_drawer\": \"0%\", \"T5_on_ramekin\": \"0%\"}, \"running_avg_6task\": \"28.3%\", \"snapshot_time\": \"2026-05-15T09:00:00Z\", \"server\": \"bjb2-28827\", \"process_status\": \"alive\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T17:30:14.331Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T17:30:15.807Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:30:23.476790+00:00\"}]}}, \"eval-mag-perdof-norm005\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:16:10.924Z\", \"updated_at\": \"2026-05-15T17:24:59.482Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode acr_vla --max_correction_norm 0.05 --n_rollouts 10 --K 10 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_mag_perdof_norm005.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"SmolVLA + CRM-v3-norm-perdof\", \"seed\": 42, \"checkpoint_source\": \"crm-train-v3-norm-perdof\", \"eval_data\": \"LIBERO spatial\", \"log_path\": \"/root/runs/acr-vla-conformal-refinement/eval-mag-perdof-norm005.log\", \"checkpoint_path\": \"N/A (eval only)\"}, \"gpu\": \"bjb2-28827:cuda:1\", \"pid\": 13456, \"metrics\": {\"T0_between_plate_ramekin\": 50, \"T1_next_to_ramekin\": 100, \"T2_table_center\": 0, \"T3_on_cookie_box\": 30, \"T4_top_drawer\": 0, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 100, \"T7_on_stove\": 0, \"T8_next_to_plate\": 30, \"T9_on_wooden_cabinet\": 0, \"avg_SR_10task\": 31}, \"reproduce\": {\"finished_at\": \"2026-05-15T16:52:50.451Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T16:52:53.898813+00:00\"}]}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-15T17:24:59.482Z\"}, \"eval-mag-obsonly-norm03-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:49:38.786Z\", \"updated_at\": \"2026-05-15T17:22:51.755Z\", \"hypothesis\": \"Retry of eval-mag-obsonly-norm03 (EXIT_CODE=127 fix). Magnitude sweep: obs_only CRM v3-norm at norm=0.3 on spatial. Fills obs_only norm=0.3 gap. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade at same norm, strong evidence for obs_only robustness.\", \"parent\": \"eval-mag-obsonly-norm03\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_mag_obsonly_norm03.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": 325264, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm03-r2.log\", \"submitted_at\": \"2026-05-15T06:50:02.511Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": 100, \"model_name\": \"crm_v3_norm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 37969.2, \"gpu_hours\": 10.55}, \"metrics\": {\"bowl_between\": 0.9, \"next_to_ramekin\": 1, \"table_center\": 0, \"cookie_box\": 0.3, \"top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"stove\": 0, \"next_to_plate\": 0.3, \"wooden_cabinet\": 0, \"overall_SR\": 0.36}, \"reproduce\": {\"finished_at\": \"2026-05-15T17:20:31.567Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:20:34.907634+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm03-r2.log\", \"completed_at\": \"2026-05-15T17:22:51.755Z\"}, \"eval-mag-perdof-norm03\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:16:16.095Z\", \"updated_at\": \"2026-05-15T17:17:49.711Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --smolvla_path /root/autodl-tmp/models/smolvla_libero/\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": 100, \"model_name\": \"crm_v3_norm/perdof\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"log_path\": \"/root/runs/acr-vla-conformal-refinement/eval-mag-perdof-norm03.log\"}, \"gpu\": \"bjb2-28827:cuda:3\", \"pid\": 14260, \"metrics\": {\"overall_sr_10task\": 0.26, \"T0_sr\": 0.7, \"T1_sr\": 0.5, \"T2_sr\": 0.1, \"T3_sr\": 0.1, \"T4_sr\": 0, \"T5_sr\": 0, \"T6_sr\": 0.9, \"T7_sr\": 0.1, \"T8_sr\": 0.2, \"T9_sr\": 0, \"total_successes\": 26, \"total_rollouts\": 100, \"benchmark\": \"spatial\", \"max_correction_norm\": 0.3}, \"reproduce\": {\"finished_at\": \"2026-05-15T16:53:04.031Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T16:53:08.939326+00:00\"}]}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-15T17:17:49.711Z\"}, \"eval-vla-mean-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:31:09.989Z\", \"updated_at\": \"2026-05-15T17:01:25.883Z\", \"spec\": {\"command\": \"python eval_vla.py --benchmark object --mode vla_only --baseline_mode mean --n_rollouts 10 --K 10 --seed 42\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"smolvla_libero\", \"seed\": 42, \"eval_data\": \"LIBERO object\", \"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean.log\"}, \"hypothesis\": \"VLA mean baseline (K=10, mean aggregation) on LIBERO object benchmark. Matches reconvla spatial baseline but on object tasks.\", \"metrics\": {\"benchmark\": \"object\", \"mode\": \"vla_only\", \"baseline_mode\": \"mean\", \"n_rollouts\": 10, \"K\": 10, \"seed\": 42, \"overall_sr\": 12, \"total_success\": 12, \"total_rollouts\": 100, \"tasks_done\": \"10/10\", \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 10, \"bbq_sauce\": 30, \"ketchup\": 10, \"tomato_sauce\": 10, \"butter\": 0, \"milk\": 20, \"chocolate_pudding\": 30, \"orange_juice\": 10}, \"json_output\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean.json\"}, \"conclusion\": \"success\", \"gpu\": \"bjb1-32546:cuda:5\", \"pid\": 18808, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean.log\", \"completed_at\": \"2026-05-15T17:01:25.883Z\"}, \"eval-mag-perdof-norm003\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:16:08.547Z\", \"updated_at\": \"2026-05-15T16:40:16.878Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode acr_vla --max_correction_norm 0.03 --n_rollouts 10 --K 10 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_mag_perdof_norm003.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"SmolVLA + CRM-v3-norm-perdof\", \"seed\": 42, \"checkpoint_source\": \"crm-train-v3-norm-perdof\", \"eval_data\": \"LIBERO spatial\"}, \"gpu\": \"bjb2-28827:cuda:0\", \"pid\": 13185, \"metrics\": {\"benchmark\": \"spatial\", \"mode\": \"acr_vla\", \"max_correction_norm\": 0.03, \"n_rollouts\": 10, \"K\": 10, \"seed\": 42, \"overall_sr\": 30, \"total_success\": 30, \"total_rollouts\": 100, \"tasks_done\": \"10/10\", \"per_task\": {\"T0_between_plate_ramekin\": 60, \"T1_next_to_ramekin\": 100, \"T2_table_center\": 0, \"T3_on_cookie_box\": 30, \"T4_top_drawer\": 10, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 80, \"T7_on_stove\": 0, \"T8_next_to_plate\": 20, \"T9_on_wooden_cabinet\": 0}}, \"reproduce\": {\"finished_at\": \"2026-05-15T16:32:37.390Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T16:32:42.080703+00:00\"}]}, \"log_path\": \"/root/runs/acr-vla-conformal-refinement/eval-mag-perdof-norm003.log\", \"checkpoint_path\": \"N/A (eval-only)\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-15T16:40:16.878Z\"}, \"eval-reconvla-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T01:48:28.744Z\", \"updated_at\": \"2026-05-15T16:25:17.101Z\", \"spec\": {\"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_reconvla.log\", \"json_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_reconvla.json\"}, \"hypothesis\": \"ReconVLA baseline (scalar Euclidean argmin, K=10) on LIBERO object benchmark. Tests whether simple sample selection improves over VLA mean on object manipulation tasks. Provides baseline for CRM comparison on object domain.\", \"metrics\": {\"overall_sr\": 0.12, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}, \"n_rollouts\": 10, \"total_episodes\": 100, \"total_successes\": 12}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T16:25:17.101Z\"}, \"eval-acr-object-v4-obs-only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T02:53:41.689Z\", \"updated_at\": \"2026-05-15T16:23:01.718Z\", \"hypothesis\": \"D021: obs_only CRM v3-norm with max_correction_norm=0.1 on LIBERO object benchmark. Cross-benchmark validation — obs-only leads spatial at 57.5%.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"13797\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-obs-only.log\", \"submitted_at\": \"2026-05-15T02:53:41.526Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 47312.8, \"gpu_hours\": 13.14}, \"metrics\": {\"overall_sr\": \"19.0% (19/100)\", \"total_success\": 19, \"total_rollouts\": 100, \"mode\": \"obs_only\", \"benchmark\": \"object\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"tasks_done\": \"10/10\", \"per_task\": {\"alphabet_soup\": \"0%\", \"cream_cheese\": \"10%\", \"salad_dressing\": \"20%\", \"bbq_sauce\": \"40%\", \"ketchup\": \"10%\", \"tomato_sauce\": \"0%\", \"butter\": \"10%\", \"milk\": \"20%\", \"chocolate_pudding\": \"50%\", \"orange_juice\": \"30%\"}, \"json_output\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T15:59:31.860Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T15:59:34.042176+00:00\"}]}, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-obs-only.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T16:02:14.366Z\"}, \"eval-acr-object-v4-scalar\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T02:53:44.102Z\", \"updated_at\": \"2026-05-15T16:10:02.679Z\", \"hypothesis\": \"D021: scalar_unc CRM v3-norm with max_correction_norm=0.1 on LIBERO object benchmark. Three-way ablation: perdof vs scalar_unc vs obs_only on object.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"14003\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-scalar.log\", \"submitted_at\": \"2026-05-15T02:53:43.910Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 47778.8, \"gpu_hours\": 13.27}, \"metrics\": {\"overall_sr\": 9, \"total_success\": 9, \"total_trials\": 100, \"n_tasks\": 10, \"n_rollouts_per_task\": 10, \"per_task\": {\"alphabet_soup\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"cream_cheese\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"salad_dressing\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"bbq_sauce\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"ketchup\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"tomato_sauce\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"butter\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"milk\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"chocolate_pudding\": {\"sr\": 30, \"success\": 3, \"trials\": 10}, \"orange_juice\": {\"sr\": 20, \"success\": 2, \"trials\": 10}}}, \"reproduce\": {\"finished_at\": \"2026-05-15T16:07:26.276Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T16:07:28.510451+00:00\"}]}, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-scalar.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-15T16:10:02.679Z\"}, \"eval-mag-obsonly-norm02\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:16:21.006Z\", \"updated_at\": \"2026-05-15T16:06:23.063Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --max_correction_norm 0.2 --n_rollouts 10 --K 10 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_mag_obs_only_norm02.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"SmolVLA + CRM-v3-norm-obs_only\", \"seed\": 42, \"checkpoint_source\": \"crm-train-v3-norm-obs_only\", \"eval_data\": \"LIBERO spatial\"}, \"gpu\": \"bjb2-28827:cuda:5\", \"pid\": 15190, \"metrics\": {\"T0_between_plate_ramekin\": 90, \"T1_next_to_ramekin\": 100, \"T2_table_center\": 0, \"T3_on_cookie_box\": 30, \"T4_top_drawer\": 10, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 90, \"T7_on_stove\": 0, \"T8_next_to_plate\": 30, \"T9_on_wooden_cabinet\": 0, \"overall_sr\": 35, \"total_success\": 35, \"total_rollouts\": 100}, \"reproduce\": {\"finished_at\": \"2026-05-15T16:03:26.878Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T16:03:29.305763+00:00\"}]}, \"log_path\": \"/root/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm02.log\", \"conclusion\": \"negative\", \"checkpoint_path\": \"N/A (eval-only experiment)\", \"completed_at\": \"2026-05-15T16:06:23.063Z\"}, \"eval-mag-obsonly-norm005\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:16:18.917Z\", \"updated_at\": \"2026-05-15T16:02:08.945Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --max_correction_norm 0.05 --n_rollouts 10 --K 10 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_mag_obs_only_norm005.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"SmolVLA + CRM-v3-norm-obs_only\", \"seed\": 42, \"checkpoint_source\": \"crm-train-v3-norm-obs_only\", \"eval_data\": \"LIBERO spatial\"}, \"gpu\": \"bjb2-28827:cuda:4\", \"pid\": 14854, \"metrics\": {\"benchmark\": \"spatial\", \"mode\": \"crm_obs_only\", \"max_correction_norm\": 0.05, \"n_rollouts\": 10, \"K\": 10, \"overall_sr\": 35, \"total_success\": 35, \"total_episodes\": 100, \"per_task\": {\"T0_between_plate_ramekin\": 80, \"T1_next_to_ramekin\": 90, \"T2_table_center\": 0, \"T3_on_cookie_box\": 40, \"T4_top_drawer\": 10, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 80, \"T7_on_stove\": 0, \"T8_next_to_plate\": 50, \"T9_on_wooden_cabinet\": 0}}, \"reproduce\": {\"finished_at\": \"2026-05-15T16:00:02.717Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T16:00:09.569232+00:00\"}]}, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm005.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T16:02:08.945Z\"}, \"eval-acr-object-v4-perdof\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T02:49:13.626Z\", \"updated_at\": \"2026-05-15T15:45:38.531Z\", \"hypothesis\": \"D021: ACR-VLA perdof CRM v3-norm with max_correction_norm=0.1 on LIBERO object benchmark. Cross-benchmark validation of spatial findings.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode acr_vla --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1\", \"server\": \"bjb1-32546\", \"gpu_ids\": [\"cuda:1\"], \"pid\": \"11116\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v3-norm perdof, max_correction_norm=0.1, object)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\", \"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-perdof.log\"}, \"metrics\": {\"overall_sr\": \"11.0% (11/100)\", \"total_success\": 11, \"total_rollouts\": 100, \"mode\": \"perdof\", \"benchmark\": \"object\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"alphabet_soup\": \"0%\", \"cream_cheese\": \"0%\", \"salad_dressing\": \"20%\", \"bbq_sauce\": \"30%\", \"ketchup\": \"0%\", \"tomato_sauce\": \"0%\", \"butter\": \"10%\", \"milk\": \"0%\", \"chocolate_pudding\": \"20%\", \"orange_juice\": \"30%\"}, \"note\": \"perdof object 11% vs argmin ~7% (partial). obs_only leads at ~14% (8/10). Confirms perdof not competitive on object.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T15:45:38.531Z\"}, \"eval-acr-spatial-v4-scalar-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:14:04.283Z\", \"updated_at\": \"2026-05-15T13:18:27.852Z\", \"hypothesis\": \"Restart from T3. scalar_unc CRM v3-norm with max_correction_norm=0.1 on spatial. Three-way ablation: perdof vs scalar_unc vs obs_only.\", \"parent\": \"eval-acr-spatial-v4-scalar\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_scalar --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1 --start_task 3\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": 311881, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-scalar-r2.log\", \"submitted_at\": \"2026-05-15T05:14:33.525Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO spatial\", \"data_count\": 70, \"model_name\": \"ACR-VLA CRM scalar_unc v3-norm (restart from T3)\", \"seed\": 42, \"eval_data\": \"LIBERO spatial tasks 3-9\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"checkpoint_path\": \"N/A (eval-only)\", \"wall_clock_seconds\": 29034.3, \"gpu_hours\": 8.07}, \"metrics\": {\"overall_sr\": \"32.0% (32/100)\", \"total_success\": 32, \"total_rollouts\": 100, \"mode\": \"scalar_unc\", \"benchmark\": \"spatial\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"T0\": \"60%\", \"T1\": \"100%\", \"T2\": \"10%\", \"T3\": \"40%\", \"T4\": \"0%\", \"T5\": \"0%\", \"T6\": \"90%\", \"T7\": \"0%\", \"T8\": \"10%\", \"T9\": \"10%\"}, \"note\": \"D030 confirmed: scalar_unc spatial 32% vs argmin 34% = -2pp. T0-T2 from original eval-acr-spatial-v4-scalar, T3-T9 from r2 restart. All CRM variants dead on spatial.\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T13:15:46.765Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T13:15:49.226583+00:00\"}]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T13:18:27.853Z\"}, \"eval-acr-spatial-v4-obs-only-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:14:05.934Z\", \"updated_at\": \"2026-05-15T11:15:11.801Z\", \"hypothesis\": \"Restart from T6. obs_only CRM v3-norm with max_correction_norm=0.1 on spatial. If obs_only >= perdof, conformal features need restructuring.\", \"parent\": \"eval-acr-spatial-v4-obs-only-r2\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --start_task 6\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": 312420, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-obs-only-r3.log\", \"submitted_at\": \"2026-05-15T05:14:38.600Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO spatial\", \"data_count\": 40, \"model_name\": \"ACR-VLA CRM obs_only v3-norm (restart from T6)\", \"seed\": 42, \"eval_data\": \"LIBERO spatial tasks 6-9\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"wall_clock_seconds\": 21633.2, \"gpu_hours\": 6.01}, \"metrics\": {\"overall_sr\": \"35.0% (35/100)\", \"total_success\": 35, \"total_rollouts\": 100, \"mode\": \"crm_obs_only\", \"benchmark\": \"spatial\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"T0\": \"90%\", \"T1\": \"100%\", \"T2\": \"0%\", \"T3\": \"40%\", \"T4\": \"10%\", \"T5\": \"0%\", \"T6\": \"90%\", \"T7\": \"0%\", \"T8\": \"20%\", \"T9\": \"0%\"}, \"r3_subset_T6_T9\": \"27.5% (11/40)\", \"note\": \"D030: obs_only spatial 10-task = 35%. vs argmin 34% = +1pp. Scenario C threshold (>=39%) NOT MET. Earlier T0-T5 advantage (+5pp) wiped out by T6-T9.\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T10:15:39.276Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T10:15:44.340640+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-obs-only-r3.log\", \"completed_at\": \"2026-05-15T11:15:11.801Z\"}, \"eval-obs-only-spatial-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T09:09:04.411Z\", \"updated_at\": \"2026-05-15T10:01:21.065Z\", \"hypothesis\": \"D029: obs_only seed=43 复现实验。obs_only 是项目唯一存活路径。seed=42 如果确认 +5pp over argmin，seed=43 增加统计力（200 vs 200 样本下 Fisher exact p ~0.12，配合 object benchmark 独立验证有望通过）。\", \"parent\": \"eval-acr-spatial-v4-obs-only-r3\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_obs_only_spatial_seed43.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"341873\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-spatial-seed43.log\", \"submitted_at\": \"2026-05-15T09:09:23.712Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": 100, \"model_name\": \"crm_v3_norm_obs_only\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO spatial (10 tasks x 10 rollouts)\", \"wall_clock_seconds\": 3117.4, \"gpu_hours\": 0.87}, \"notes\": \"D029: perdof spatial 35% vs argmin 34% = +1pp, kill criterion triggered. Per-DOF claim dead on spatial. obs_only 是唯一存活路径，seed=43 用于增加统计力。\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T10:01:21.065Z\"}, \"eval-acr-spatial-v4-small-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:14:05.220Z\", \"updated_at\": \"2026-05-15T09:10:21.153Z\", \"hypothesis\": \"Restart from T7. ACR-VLA perdof CRM v3-norm with max_correction_norm=0.1 on spatial. Full per-DOF uncertainty pipeline.\", \"parent\": \"eval-acr-spatial-v4-small\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/crm_best.pt --max_correction_norm 0.1 --start_task 7\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": 312150, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-small-r2.log\", \"submitted_at\": \"2026-05-15T05:14:36.298Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO spatial\", \"data_count\": 30, \"model_name\": \"ACR-VLA CRM perdof v3-norm (restart from T7)\", \"seed\": 42, \"eval_data\": \"LIBERO spatial tasks 7-9\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/crm_best.pt\", \"wall_clock_seconds\": 14053.7, \"gpu_hours\": 3.9}, \"notes\": \"[D027] Framing 暂不裁决。Scenario A/B/C 取决于 magnitude sweep + object benchmark 结果。spatial matched-task perdof=argmin (0pp) 意味着 Scenario A 在 spatial 上不可能。\", \"metrics\": {\"overall_sr\": \"35.0% (35/100)\", \"total_success\": 35, \"total_rollouts\": 100, \"mode\": \"perdof\", \"benchmark\": \"spatial\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"T0\": \"60%\", \"T1\": \"100%\", \"T2\": \"10%\", \"T3\": \"40%\", \"T4\": \"0%\", \"T5\": \"0%\", \"T6\": \"90%\", \"T7\": \"10%\", \"T8\": \"40%\", \"T9\": \"0%\"}, \"note\": \"D029: perdof spatial complete 10-task = 35%. vs argmin 34% = +1pp. Kill criterion triggered — per-DOF claim dead on spatial.\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T09:05:27.552Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T09:05:31.321347+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/crm_best.pt\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-small-r2.log\", \"completed_at\": \"2026-05-15T09:08:50.017Z\"}, \"eval-mag-obsonly-norm-0.3-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:10:44.647Z\", \"updated_at\": \"2026-05-15T07:19:12.632Z\", \"hypothesis\": \"Magnitude sweep: obs_only CRM v3-norm at max_correction_norm=0.3 on spatial. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade at same norm, strong evidence for obs_only robustness over perdof.\", \"parent\": \"eval-mag-obsonly-norm02\", \"spec\": {\"command\": \"N/A (stale duplicate entry)\", \"server\": \"bjb1-18228\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"N/A\", \"seed\": 0, \"checkpoint_source\": \"N/A\", \"eval_data\": \"N/A\"}, \"conclusion\": \"killed\", \"checkpoint_path\": \"N/A (stale duplicate entry, never ran)\", \"log_path\": \"N/A\", \"notes\": \"Stale duplicate entry with dots in name. Actual experiment is eval-mag-obsonly-norm-0p3-r3 (also killed). Real running experiment is eval-mag-obsonly-norm03-r2.\", \"completed_at\": \"2026-05-15T07:19:12.632Z\"}, \"eval-mag-obsonly-norm-0p3-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:11:06.381Z\", \"updated_at\": \"2026-05-15T07:17:16.300Z\", \"hypothesis\": \"Magnitude sweep: obs_only CRM v3-norm at max_correction_norm=0.3 on spatial. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade at same norm, strong evidence for obs_only robustness over perdof.\", \"parent\": \"eval-mag-obsonly-norm02\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_mag_obsonly_norm_0p3.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"329871\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm-0p3-r3.log\", \"submitted_at\": \"2026-05-15T07:11:15.690Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": 100, \"model_name\": \"crm_obs_only_v3_norm\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO spatial (10 tasks x 10 rollouts)\", \"wall_clock_seconds\": 360.6, \"gpu_hours\": 0.1}, \"conclusion\": \"killed\", \"notes\": \"Director 撤销部署指令。r2 (PID 325264) 实际未被误杀，r3 是基于信息差的重复部署。立即 kill r3 保留 r2。\", \"checkpoint_path\": \"N/A (killed before completion)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm-0p3-r3.log\", \"completed_at\": \"2026-05-15T07:17:16.300Z\"}, \"eval-argmin-only-spatial-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:14:03.322Z\", \"updated_at\": \"2026-05-15T06:39:37.926Z\", \"hypothesis\": \"Restart from T9. ReconVLA baseline (scalar Euclidean argmin, K=10) on spatial. Isolate argmin base action selection from CRM correction.\", \"parent\": \"eval-argmin-only-spatial\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --start_task 9\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": 311609, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-only-spatial-r2.log\", \"submitted_at\": \"2026-05-15T05:14:30.112Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO spatial\", \"data_count\": 10, \"model_name\": \"ReconVLA argmin K=10 (restart from T9)\", \"seed\": 42, \"eval_data\": \"LIBERO spatial task 9 only\", \"checkpoint_source\": \"N/A (reconvla mode, no CRM)\", \"wall_clock_seconds\": 5107.8, \"gpu_hours\": 1.42}, \"reproduce\": {\"finished_at\": \"2026-05-15T06:35:00.746Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T06:35:02.954210+00:00\"}]}, \"metrics\": {\"overall_success_rate\": 0.34, \"total_successes\": 34, \"total_trials\": 100, \"per_task\": {\"T0_between_plate_and_ramekin\": 0.6, \"T1_next_to_ramekin\": 1, \"T2_from_table_center\": 0, \"T3_on_cookie_box\": 0.3, \"T4_in_top_drawer\": 0.1, \"T5_on_ramekin\": 0.1, \"T6_next_to_cookie_box\": 0.9, \"T7_on_stove\": 0, \"T8_next_to_plate\": 0.3, \"T9_on_wooden_cabinet\": 0.1}, \"note\": \"T0-T8 from original run (eval-argmin-only-spatial), T9 from r2 restart. Combined 10-task result.\"}, \"conclusion\": \"success\", \"notes\": \"10-task complete. T9 (wooden_cabinet) = 10%. Overall 34% (34/100). T0-T8 from original run, T9 from r2 restart. Clean exit. bjb1-18228 cuda:0 now FREE.\", \"checkpoint_path\": \"N/A (eval-only, no checkpoint output)\", \"completed_at\": \"2026-05-15T06:39:37.926Z\"}, \"eval-mag-obsonly-norm003\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:21:24.009Z\", \"updated_at\": \"2026-05-15T05:32:12.897Z\", \"hypothesis\": \"Magnitude sweep: obs_only CRM v3-norm at norm=0.03 on spatial. Completes obs_only norm curve (have 0.05, 0.2; adding 0.03).\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --max_correction_norm 0.03 --n_rollouts 10 --K 10 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_mag_obsonly_norm003.json\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": 225144, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm003-b2.log\", \"submitted_at\": \"2026-05-15T05:20:45Z\", \"submitted_via\": \"tmux (manual)\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"SmolVLA + CRM-v3-norm-obs_only\", \"seed\": 42, \"checkpoint_source\": \"crm-train-v3-norm-obs_only\", \"eval_data\": \"LIBERO spatial\", \"wall_clock_seconds\": 686.0, \"gpu_hours\": 0.19}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T05:32:10.962Z\", \"notes\": \"Duplicate experiment on same GPU. pid 225144 was actually the child python process of eval-mag-obsonly-norm003-b2's wrapper (pid 225139). Not a separate experiment. Killed, restarted b2 with new pid 227426.\"}, \"eval-vla-only-object-k1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:11:14.165Z\", \"updated_at\": \"2026-05-15T05:18:17.853Z\", \"hypothesis\": \"VLA-only baseline (K=1, single sample, no CRM) on LIBERO object benchmark. Lowest-bar baseline for object domain.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode vla_only --baseline_mode single --benchmark object --n_rollouts 10 --seed 42 --K 1 --output_file logs/eval_object_vla_only_k1.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"39397\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-object-k1.log\", \"submitted_at\": \"2026-05-15T05:11:22.634Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"SmolVLA (VLA-only K=1 single sample)\", \"seed\": 42, \"eval_data\": \"LIBERO object\", \"checkpoint_source\": \"N/A (no CRM, single VLA sample)\", \"wall_clock_seconds\": 311.9, \"gpu_hours\": 0.09}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T05:16:34.574Z\", \"notes\": \"Duplicate of eval-vla-only-object (already DONE at 12% SR). Process killed to free bjb1-32546 cuda:4.\"}, \"eval-acr-spatial-v4-obs-only-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:16:06.636Z\", \"updated_at\": \"2026-05-15T05:05:21.600Z\", \"hypothesis\": \"D020: obs_only CRM v3-norm (val_loss 0.0165) with max_correction_norm=0.1. If obs_only >= v4-small (perdof) → Claim 1 needs restructuring. If obs_only < v4-small → conformal features have unique value under distribution shift.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"270097\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-obs-only-r2.log\", \"submitted_at\": \"2026-05-14T22:21:35.775Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_ids\": [\"cuda:0\"], \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v3-norm obs_only, max_correction_norm=0.1)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 24161.7, \"gpu_hours\": 6.71}, \"metrics\": {\"tasks_done\": \"6/10\", \"partial_results\": {\"between_plate_and_ramekin\": \"90.0% (9/10)\", \"next_to_ramekin\": \"100.0% (10/10)\", \"from_table_center\": \"0.0% (0/10)\", \"on_cookie_box\": \"40.0% (4/10)\", \"in_top_drawer\": \"10.0% (1/10)\", \"on_ramekin\": \"0.0% (0/10)\"}, \"running_avg_6tasks\": \"40.0% (24/60)\", \"snapshot_time\": \"2026-05-15T12:00:00Z\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:0\", \"pid\": 270097}, \"notes\": \"[2026-05-15 corrected] 之前误判为 env hang，实际是被 kill-restart Worker SIGTERM kill。日志无 error/traceback，符合 SIGTERM 特征。6/10 tasks 完成 + task 7 部分（5/10 rollouts），40.0% SR (24/60)。需重跑。\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T05:04:17.448Z\", \"failure_reason\": \"被 kill-restart Worker SIGTERM（Director 撤销 kill 指令前已执行）。完成 6/10 tasks，第 7 个 task (next_to_cookie_box) rollout 5/10 时被 kill。\"}, \"eval-acr-spatial-v4-small\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:09:00.358Z\", \"updated_at\": \"2026-05-15T05:05:19.028Z\", \"hypothesis\": \"D018: Normalization + moderate correction scaling (max_correction_norm=0.1, 14x smaller than default). If v4-small > v4-default → magnitude control needed on top of normalization.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1\", \"server\": \"bjb1-18228\", \"gpu_ids\": [\"cuda:3\"], \"pid\": 253085, \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v3-norm per-DOF, max_correction_norm=0.1)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"log_path\": \"/root/autodl-tmp/logs/eval_acr_spatial_v4_small.log\"}, \"metrics\": {\"tasks_done\": \"7/10\", \"partial_results\": {\"between_plate_and_ramekin\": \"60.0% (6/10)\", \"next_to_ramekin\": \"100.0% (10/10)\", \"from_table_center\": \"10.0% (1/10)\", \"on_cookie_box\": \"40.0% (4/10)\", \"in_top_drawer\": \"0.0% (0/10)\", \"on_ramekin\": \"0.0% (0/10)\", \"next_to_cookie_box\": \"90.0% (9/10)\"}, \"running_avg_7tasks\": \"42.9% (30/70)\", \"snapshot_time\": \"2026-05-15T12:00:00Z\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:3\", \"pid\": 253085}, \"notes\": \"[2026-05-15 corrected] 之前误判为 env init hang，实际是被 kill-restart Worker SIGTERM kill。日志无 error/traceback，符合 SIGTERM 特征。7/10 tasks 完成，42.9% SR (30/70)。需重跑 tasks 8-10（或全部重跑）。\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T05:04:16.712Z\", \"failure_reason\": \"被 kill-restart Worker SIGTERM（Director 撤销 kill 指令前已执行）。完成 7/10 tasks 后在 task 8 启动前被 kill。\"}, \"eval-acr-spatial-v4-scalar\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:15:49.209Z\", \"updated_at\": \"2026-05-15T05:02:30.518Z\", \"hypothesis\": \"D020: scalar_unc CRM (val_loss 0.0374) with max_correction_norm=0.1. Three-way ablation: perdof vs scalar_unc vs obs_only under identical correction magnitude.\", \"spec\": {\"hypothesis\": \"D020 三路消融：scalar_unc CRM v3-norm (val_loss 0.0374) with max_correction_norm=0.1. 与 perdof (cuda:3) 和 obs_only (cuda:0) 同条件对比，判断 per-DOF vs scalar conformal features 的增益\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v3-norm scalar_unc, max_correction_norm=0.1)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"command\": \"python -u src/evaluate.py --mode crm_scalar --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": 288939, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-scalar.log\", \"gpu_ids\": [\"cuda:2\"]}, \"metrics\": {\"tasks_done\": \"3/10\", \"partial_results\": {\"between_plate_and_ramekin\": \"60.0% (6/10)\", \"next_to_ramekin\": \"100.0% (10/10)\", \"from_table_center\": \"10.0% (1/10)\"}, \"running_avg_3tasks\": \"56.7% (17/30)\", \"snapshot_time\": \"2026-05-15T12:00:00Z\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:2\", \"pid\": 288939}, \"notes\": \"[2026-05-15] HUNG: 3/10 tasks done (56.7%, 17/30), stuck on task 4 env init for 8+ hours. Process alive (pid 288939, GPU 1450 MiB) but zero log progress. Needs kill+restart.\", \"reproduce\": {\"finished_at\": \"2026-05-15T04:57:54.647Z\"}, \"failure_reason\": \"Kill-restart Worker 在 Director 撤销 kill 指令前已执行 SIGTERM (EXIT_CODE=143)。D026 kill 指令已被撤销但来不及阻止。\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T04:57:55.887Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T04:57:57.857060+00:00\"}]}}, \"eval-argmin-only-spatial\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:47:58.683Z\", \"updated_at\": \"2026-05-15T05:02:29.518Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark spatial --n_rollouts 10 --seed 42 --K 10\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"231421\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-only-spatial.log\", \"submitted_at\": \"2026-05-14T17:47:58.583Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_ids\": [\"cuda:1\"], \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"SmolVLA K=10 argmin selection (no CRM correction)\", \"seed\": 42, \"hypothesis\": \"Isolate argmin base action selection from CRM correction. If argmin-only ≈ VLA mean (40%), CRM delta is the sole culprit. If argmin-only << VLA mean, argmin selection itself is problematic.\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 40187.5, \"gpu_hours\": 11.16}, \"metrics\": {\"tasks_done\": \"9/10\", \"partial_results\": {\"between_plate_and_ramekin\": \"60.0% (6/10)\", \"next_to_ramekin\": \"100.0% (10/10)\", \"from_table_center\": \"0.0% (0/10)\", \"on_cookie_box\": \"30.0% (3/10)\", \"in_top_drawer\": \"10.0% (1/10)\", \"on_ramekin\": \"10.0% (1/10)\", \"next_to_cookie_box\": \"90.0% (9/10)\", \"on_stove\": \"0.0% (0/10)\", \"next_to_plate\": \"30.0% (3/10)\"}, \"running_avg_9tasks\": \"36.7% (33/90)\", \"snapshot_time\": \"2026-05-15T12:00:00Z\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"pid\": 231421}, \"notes\": \"[2026-05-15] HUNG: 9/10 tasks done (36.7%, 33/90), stuck on task 10 env init for 8+ hours. Process alive (pid 231426, GPU 1414 MiB) but zero log progress. Needs kill+restart.\", \"reproduce\": {\"finished_at\": \"2026-05-15T04:57:45.148Z\"}, \"failure_reason\": \"Kill-restart Worker 在 Director 撤销 kill 指令前已执行 SIGTERM (EXIT_CODE=143)。D026 kill 指令已被撤销但来不及阻止。\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T04:57:46.099Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T04:57:50.175181+00:00\"}]}}, \"eval-vla-only-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T02:54:57.323Z\", \"updated_at\": \"2026-05-15T04:47:47.959Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode single --n_rollouts 10 --K 1 --output_file logs/eval_object_vla_only.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"SmolVLA (VLA-only baseline)\", \"seed\": 42, \"eval_data\": \"LIBERO object\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only.log\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only.json\"}, \"conclusion\": \"success\", \"hypothesis\": \"VLA-only baseline (K=1, no mean, no CRM) on LIBERO object benchmark. Single sample from flow-matching VLA.\", \"metrics\": {\"overall_sr\": 0.12, \"total_success\": 12, \"total_trials\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"gpu\": \"bjb1-32546:cuda:4\", \"pid\": 17222, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only.log\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only.json\", \"completed_at\": \"2026-05-15T04:42:20.025Z\"}, \"eval-acr-spatial-v4-default-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T01:48:09.734Z\", \"updated_at\": \"2026-05-15T03:30:05.911Z\", \"hypothesis\": \"D018-D019 验证: perdof CRM v3-norm with DEFAULT max_correction_norm (~1.42). 如果 v4-default << v4-small (max_norm=0.1) → magnitude control 是必要的。如果 v4-default ≈ baseline → normalization 独自不够。补全 bjb1 上两次失败的实验。\", \"parent\": \"eval-acr-spatial-v4-default-r2\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\\\"\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"212685\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-default-r3.log\", \"submitted_at\": \"2026-05-15T01:49:35.076Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v3-norm perdof, default max_correction_norm)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 6030.8, \"gpu_hours\": 1.68}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T03:30:05.911Z\"}, \"eval-tiny-correction-spatial\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:48:35.421Z\", \"updated_at\": \"2026-05-15T01:45:12.897Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v2/perdof/crm_best.pt --max_correction_norm 0.05\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"232815\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-tiny-correction-spatial.log\", \"submitted_at\": \"2026-05-14T17:48:35.317Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_ids\": [\"cuda:2\"], \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"ACR-VLA per-DOF CRM v2 with tiny correction (max_norm=0.05, 28x smaller than default 1.42)\", \"seed\": 42, \"hypothesis\": \"Extreme correction clipping (0.05 vs 1.42) tests whether compounding error from large CRM deltas is the primary failure mode. If tiny-correction >> full-correction, correction magnitude is the problem.\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v2/perdof/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 27771.0, \"gpu_hours\": 7.71}, \"metrics\": {\"tasks_done\": \"7/10\", \"partial_results\": {\"T1_between_plate_ramekin\": \"70% (7/10)\", \"T2_next_to_ramekin\": \"90% (9/10)\", \"T3_from_table_center\": \"0% (0/10)\", \"T4_on_cookie_box\": \"30% (3/10)\", \"T5_in_top_drawer\": \"0% (0/10)\", \"T6_on_ramekin\": \"0% (0/10)\", \"T7_next_to_cookie_box\": \"90% (9/10)\"}, \"running_avg_7tasks\": \"40% (28/70)\", \"process_status\": \"ACTUALLY ALIVE - bash wrapper PID 232815 dead but python child PID 232820 still running (07:48h, 139% CPU, 9.1GB RSS, GPU2)\", \"status_correction\": \"Registry incorrectly marked DONE, process is still completing remaining 3 tasks\", \"snapshot_time\": \"2026-05-15T09:40Z\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T01:31:26.353Z\", \"failure_reason\": \"D021: v2 checkpoint invalidated by crm_cache_v5 retraining. Replaced by eval-acr-spatial-v4-scalar on bjb1:2.\"}, \"eval-vla-mean-spatial-t10\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:20:02.901Z\", \"updated_at\": \"2026-05-15T01:45:11.590Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --baseline_mode mean --benchmark spatial --n_rollouts 10 --seed 42 --start_task 9 --output_file /root/autodl-tmp/eval_results/eval-vla-mean-spatial-t10.json\", \"server\": \"bjb2-40593\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 10, \"model_name\": \"smolvla_libero\", \"seed\": 42}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T01:32:23.773Z\", \"metrics\": {\"T10_on_wooden_shelf\": \"10% (1/10)\", \"note\": \"Only ran task 9 (start_task=9). T10 = wooden shelf task.\"}, \"log_path\": \"/root/autodl-tmp/eval_results/eval-vla-mean-spatial-t10.json\", \"checkpoint_path\": \"N/A (eval only)\"}, \"eval-vla-mean-spatial\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T03:10:44.114Z\", \"updated_at\": \"2026-05-15T01:35:18.092Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode vla_only --baseline_mode mean --benchmark spatial --n_rollouts 10 --seed 42\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"143106\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"SmolVLA K=10 mean action (no conformal)\", \"seed\": 42, \"hypothesis\": \"K=10 mean baseline isolates multi-sampling averaging contribution vs conformal correction. Expected between vla_only K=1 (30%) and ACR-VLA.\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"log_path\": \"/root/autodl-tmp/eval_results/eval-vla-mean-spatial.log\"}, \"metrics\": {\"overall_success_rate_10tasks\": 0.32, \"total_successes\": 32, \"total_trials\": 100, \"T1\": 0.7, \"T2\": 1, \"T3\": 0, \"T4\": 0.3, \"T5\": 0, \"T6\": 0, \"T7\": 0.8, \"T8\": 0, \"T9\": 0.3, \"T10\": 0.1}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T22:12:39.100Z\", \"log_path\": \"/root/autodl-tmp/eval_results/eval-vla-mean-spatial.log\", \"checkpoint_path\": \"N/A (eval experiment)\"}, \"eval-acr-spatial-v4-default-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:17:37.194Z\", \"updated_at\": \"2026-05-14T22:40:00.000Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\\\"\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"203217\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-default-r2.log\", \"submitted_at\": \"2026-05-14T22:29:03.489Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"D018 retry: Normalization alone fixes CRM correction degradation. v3-norm per-DOF checkpoint with default max_correction_norm (~1.42). If >30% baseline → normalization was the main fix. If still < 30% → magnitude control also needed (compare with v4-small at 0.1).\", \"parent\": \"eval-acr-spatial-v4-default\", \"conclusion\": \"killed\", \"failure_reason\": \"Superseded by D020 plan. Default norm=1.42 already proven to degrade (v4-default: 0/5). Not needed. Process killed on bjb2 (PID 203222 confirmed dead).\", \"completed_at\": \"2026-05-14T22:40:00.000Z\"}, \"eval-acr-spatial-v4-obs-only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:08:53.421Z\", \"updated_at\": \"2026-05-14T22:16:05.788Z\", \"hypothesis\": \"D020: obs_only CRM (val_loss 0.0165, 54% better than perdof 0.0358) with max_correction_norm=0.1. If obs_only >= v4-small (perdof) → Claim 1 needs restructuring. If obs_only < v4-small → conformal features have unique value under distribution shift.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3/obs_only/crm_best.pt\", \"server\": \"bjb2-40593\", \"gpu_ids\": [\"cuda:0\"], \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v3 obs_only, default max_correction_norm=1.42)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"log_path\": \"/root/autodl-tmp/logs/eval-acr-spatial-v4-obs-only.log\", \"tmux_session\": \"eval-acr-spatial-v4-obs-only\", \"pid\": 199257}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T22:16:04.414Z\", \"failure_reason\": \"Wrong checkpoint (crm_v3 not crm_v3_norm) + wrong max_correction_norm (1.42 not 0.1). Killed and replaced by eval-acr-spatial-v4-obs-only-r2.\"}, \"eval-acr-spatial-v4-default\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:08:59.906Z\", \"updated_at\": \"2026-05-14T22:08:58.490Z\", \"hypothesis\": \"D018: Input normalization alone fixes CRM correction degradation. v3-norm checkpoint with default max_correction_norm=1.42. If >30% baseline → normalization was the main fix.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"server\": \"bjb1-18228\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v3-norm per-DOF, default correction)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\"}, \"metrics\": {\"tasks_done\": \"0/10\", \"status_alert\": \"NO PROCESS FOUND - registry says RUNNING but no matching PID or tmux session on bjb1-18228. GPU 0 occupied by stale eval-acr-spatial-v3 tmux + crm-train-obs-only. NEEDS RESTART.\", \"snapshot_time\": \"2026-05-15T05:26Z\"}, \"conclusion\": \"failed\", \"failure_reason\": \"Process died. D019: 0/5 on task 1 confirmed default norm=1.42 still degrades. Replaced by eval-acr-spatial-v4-obs-only on cuda:0.\", \"completed_at\": \"2026-05-14T22:08:58.490Z\"}, \"crm-train-v3-norm-scalar-unc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:09:01.250Z\", \"updated_at\": \"2026-05-14T22:05:42.608Z\", \"hypothesis\": \"Ablation: scalar_unc input mode (scalar uncertainty only) with normalization. Tests per-DOF vs scalar uncertainty contribution with proper normalization.\", \"spec\": {\"command\": \"python -u src/train_crm.py --benchmark spatial --cache_dir /root/autodl-tmp/crm_cache_v5 --output_dir /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/ --K 10 --epochs 50 --batch_size 512 --lr 0.016 --input_mode scalar_unc --seed 42\", \"server\": \"bjb1-18228\", \"data_path\": \"/root/autodl-tmp/crm_cache_v5/spatial/\", \"data_count\": 12167, \"model_name\": \"CRM-MLP-Normalized (scalar_unc)\", \"seed\": 42}, \"metrics\": {\"best_epoch\": 46, \"best_val_loss\": 0.037354, \"final_train_loss\": 0.053422, \"final_val_loss\": 0.03737}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"log_path\": \"/tmp/crm_train_scalar_unc.log\", \"completed_at\": \"2026-05-14T22:05:42.608Z\"}, \"crm-train-v3-norm-obs-only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:09:00.829Z\", \"updated_at\": \"2026-05-14T22:05:28.289Z\", \"hypothesis\": \"Ablation: obs_only input mode (no uncertainty features) with normalization. Isolates contribution of obs features vs conformal features.\", \"spec\": {\"command\": \"python -u src/train_crm.py --benchmark spatial --cache_dir /root/autodl-tmp/crm_cache_v5 --output_dir /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/ --K 10 --epochs 50 --batch_size 512 --lr 0.016 --input_mode obs_only --seed 42\", \"server\": \"bjb1-18228\", \"data_path\": \"/root/autodl-tmp/crm_cache_v5/spatial/\", \"data_count\": 12167, \"model_name\": \"CRM-MLP-Normalized (obs_only)\", \"seed\": 42}, \"metrics\": {\"best_epoch\": 48, \"best_val_loss\": 0.01645, \"final_train_loss\": 0.025576, \"final_val_loss\": 0.01645, \"total_epochs\": 50}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"/tmp/crm_train_obs_only.log\", \"completed_at\": \"2026-05-14T22:05:28.289Z\"}, \"eval-acr-object-v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:17:13.095Z\", \"updated_at\": \"2026-05-14T20:48:42.308Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode acr_vla --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v2/perdof/crm_best.pt\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"197803\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v3.log\", \"submitted_at\": \"2026-05-14T12:17:13.006Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/ (object benchmark)\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v2 per-DOF + SmolVLA K=10)\", \"seed\": 42, \"hypothesis\": \"Per-DOF conformal correction generalizes from spatial to object benchmark — cross-benchmark validation of ACR-VLA.\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v2/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 28901.2, \"gpu_hours\": 8.03}, \"metrics\": {\"tasks_done\": \"4/10\", \"overall_success_rate\": 0, \"total_successes\": 0, \"total_rollouts\": 40, \"per_task_partial\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0, \"bbq_sauce\": 0}, \"snapshot_time\": \"2026-05-14T18:15Z\"}, \"conclusion\": \"failed\", \"reproduce\": {\"finished_at\": \"2026-05-14T20:18:53.408Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-14T20:18:54.185Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T20:18:55.466058+00:00\"}]}}, \"eval-acr-spatial-v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:17:06.073Z\", \"updated_at\": \"2026-05-14T20:48:41.643Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v2/perdof/crm_best.pt\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"197057\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v3.log\", \"submitted_at\": \"2026-05-14T12:17:05.974Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial benchmark)\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v2 per-DOF + SmolVLA K=10)\", \"seed\": 42, \"hypothesis\": \"Per-DOF conformal correction (ACR-VLA with D016 4-bug fix) outperforms VLA K=1 (30%) and SampleConsensus (34%) on LIBERO spatial. CORE CLAIM experiment.\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v2/perdof/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 28899.4, \"gpu_hours\": 8.03}, \"metrics\": {\"tasks_done\": \"4/10\", \"overall_success_rate\": 0.025, \"total_successes\": 1, \"total_rollouts\": 40, \"per_task_partial\": {\"pick_up_black_bowl_between_plate_and_ramekin\": 0.1, \"pick_up_black_bowl_next_to_ramekin\": 0, \"pick_up_black_bowl_from_table_center\": 0, \"pick_up_black_bowl_on_cookie_box\": 0}, \"snapshot_time\": \"2026-05-14T18:15Z\"}, \"conclusion\": \"failed\", \"reproduce\": {\"finished_at\": \"2026-05-14T20:18:44.725Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-14T20:18:45.380Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T20:18:46.631294+00:00\"}]}}, \"crm-train-v3-norm\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:45:12.565Z\", \"updated_at\": \"2026-05-14T20:05:22.677Z\", \"hypothesis\": \"D018: Input normalization fixes 1500x scale imbalance in CRM inputs, enabling proper gradient flow and meaningful per-DOF correction learning\", \"parent\": \"crm-train-v3-perdof\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/train_crm.py --benchmark spatial --cache_dir /root/autodl-tmp/crm_cache_v5 --output_dir /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/ --K 10 --epochs 50 --batch_size 512 --lr 0.016 --input_mode full --seed 42\", \"server\": \"bjb1-18228\", \"data_path\": \"/root/autodl-tmp/crm_cache_v5/spatial/\", \"data_count\": 12167, \"model_name\": \"CRM-MLP-337K-Normalized\", \"seed\": 42, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"N/A (training experiment)\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"log_path\": \"no log file (tee failed, output was in tmux pane only)\", \"completed_at\": \"2026-05-14T20:05:20.181Z\", \"results\": {\"best_epoch\": 47, \"best_val_loss\": 0.03578, \"final_train_loss\": 0.04992, \"final_val_loss\": 0.03578, \"total_epochs\": 50, \"normalization\": \"per-feature input normalization (mean/std stored in crm_best.pt as input_mean/input_std tensors)\"}}, \"crm-train-v3-scalar-unc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:05:00.968Z\", \"updated_at\": \"2026-05-14T18:37:14.400Z\", \"spec\": {\"command\": \"python -u src/train_crm.py --benchmark spatial --cache_dir /root/autodl-tmp/crm_cache/ --output_dir /root/autodl-tmp/checkpoints/crm_v3/scalar_unc/ --K 10 --epochs 50 --batch_size 512 --lr 0.016 --input_mode scalar_unc --seed 42 --norm_stats /root/autodl-tmp/checkpoints/crm_v3/norm_stats.pt\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"181896\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-train-v3-scalar-unc.log\", \"submitted_at\": \"2026-05-14T18:05:00.862Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/crm_cache/\", \"data_count\": 0, \"model_name\": \"CRM-MLP-337K\", \"seed\": 42, \"wall_clock_seconds\": 1917.7, \"gpu_hours\": 0.53}, \"reproduce\": {\"finished_at\": \"2026-05-14T18:27:15.107Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T18:27:19.071535+00:00\"}]}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T18:36:58.566Z\", \"metrics\": {\"invalidation_reason\": \"Trained on bjb2 crm_cache v4 (6D state, pre-D016). Must retrain on bjb1 crm_cache_v5 (8D state).\", \"original_val_loss\": 1.195}}, \"crm-train-v3-obs-only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:05:02.939Z\", \"updated_at\": \"2026-05-14T18:37:04.316Z\", \"spec\": {\"command\": \"python -u src/train_crm.py --benchmark spatial --cache_dir /root/autodl-tmp/crm_cache/ --output_dir /root/autodl-tmp/checkpoints/crm_v3/obs_only/ --K 10 --epochs 50 --batch_size 512 --lr 0.016 --input_mode obs_only --seed 42 --norm_stats /root/autodl-tmp/checkpoints/crm_v3/norm_stats.pt\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"181973\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-train-v3-obs-only.log\", \"submitted_at\": \"2026-05-14T18:05:02.833Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/crm_cache/spatial\", \"data_count\": 2402, \"model_name\": \"CRM-MLP-337K\", \"seed\": 42, \"wall_clock_seconds\": 1802.8, \"gpu_hours\": 0.5}, \"reproduce\": {\"finished_at\": \"2026-05-14T18:27:22.983Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T18:27:25.410071+00:00\"}]}, \"conclusion\": \"killed\", \"metrics\": {\"invalidation_reason\": \"Trained on bjb2 crm_cache v4 (6D state, pre-D016). Must retrain on bjb1 crm_cache_v5 (8D state).\", \"original_val_loss\": 1.193424}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3/obs_only/crm_best.pt\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-train-v3-obs-only.log\", \"completed_at\": \"2026-05-14T18:35:05.626Z\"}, \"crm-train-v3-perdof\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:04:54.552Z\", \"updated_at\": \"2026-05-14T18:37:02.631Z\", \"spec\": {\"command\": \"python -u src/train_crm.py --benchmark spatial --cache_dir /root/autodl-tmp/crm_cache/ --output_dir /root/autodl-tmp/checkpoints/crm_v3/perdof/ --K 10 --epochs 50 --batch_size 512 --lr 0.016 --input_mode full --seed 42 --norm_stats /root/autodl-tmp/checkpoints/crm_v3/norm_stats.pt\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"181668\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-train-v3-perdof.log\", \"submitted_at\": \"2026-05-14T18:04:54.446Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/crm_cache/\", \"data_count\": 0, \"model_name\": \"CRM-MLP-337K\", \"seed\": 42, \"wall_clock_seconds\": 1510.3, \"gpu_hours\": 0.42}, \"reproduce\": {\"finished_at\": \"2026-05-14T18:27:11.506Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T18:27:13.038696+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3/perdof/crm_best.pt\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-train-v3-perdof.log\", \"metrics\": {\"invalidation_reason\": \"Trained on bjb2 crm_cache v4 (6D state, pre-D016). Must retrain on bjb1 crm_cache_v5 (8D state).\", \"original_val_loss\": 1.191387}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T18:30:04.713Z\"}, \"eval-obs-only-spatial-v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:49:43.787Z\", \"updated_at\": \"2026-05-14T17:47:54.523Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v2/obs_only/crm_best.pt\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"211961\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-spatial-v3.log\", \"submitted_at\": \"2026-05-14T12:49:43.691Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"CRM obs_only v2 (990D, no conformal features)\", \"seed\": 42, \"hypothesis\": \"obs_only CRM ablation — CRM without conformal features tests whether per-DOF conformal intervals are necessary\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v2/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"parent\": \"crm-train-v2-obs-only\", \"conclusion_note\": \"Director order: 0/30 after 3 tasks, no diagnostic value. Freed bjb1:2 for eval-tiny-correction-spatial.\", \"metrics\": {\"tasks_completed\": 3, \"total_tasks\": 10, \"success_rate\": 0, \"successes\": 0, \"rollouts\": 30}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v2/obs_only/crm_best.pt\", \"wall_clock_seconds\": 17890.8, \"gpu_hours\": 4.97}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T17:47:54.523Z\"}, \"eval-scalar-unc-spatial-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:17:08.413Z\", \"updated_at\": \"2026-05-14T17:47:53.188Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode crm_scalar --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v2/scalar_unc/crm_best.pt\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"197324\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-scalar-unc-spatial-v2.log\", \"submitted_at\": \"2026-05-14T12:17:08.325Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial benchmark)\", \"data_count\": 100, \"model_name\": \"CRM v2 scalar-uncertainty + SmolVLA K=10\", \"seed\": 42, \"hypothesis\": \"Scalar uncertainty CRM ablation — tests whether per-DOF conformal is superior to scalar aggregated uncertainty for action correction.\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v2/scalar_unc/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"conclusion_note\": \"Director order: 0/30 after 3 tasks, no diagnostic value. Freed bjb1:1 for eval-argmin-only-spatial.\", \"metrics\": {\"tasks_completed\": 3, \"total_tasks\": 10, \"success_rate\": 0, \"successes\": 0, \"rollouts\": 30}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v2/scalar_unc/crm_best.pt\", \"wall_clock_seconds\": 19844.9, \"gpu_hours\": 5.51}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T17:47:53.188Z\"}, \"eval-obs-only-spatial-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:43:42.283Z\", \"updated_at\": \"2026-05-14T12:46:47.663Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v2/obs_only/crm_best.pt\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"203968\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-spatial-v2.log\", \"submitted_at\": \"2026-05-14T12:43:42.188Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"CRM obs_only v2 (990D, no conformal features)\", \"seed\": 42, \"hypothesis\": \"obs_only CRM ablation — CRM without conformal features tests whether per-DOF conformal intervals are necessary for effective correction\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v2/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"parent\": \"crm-train-v2-obs-only\", \"failure_reason\": \"Bug: evaluate.py line 266 CRM load condition missing crm_obs_only, CRM was None throughout eval, all rollouts 0%. Replaced by eval-obs-only-spatial-v3.\", \"wall_clock_seconds\": 185.5, \"gpu_hours\": 0.05}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T12:46:47.663Z\"}, \"eval-obs-only-spatial\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:17:10.843Z\", \"updated_at\": \"2026-05-14T12:40:23.205Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v2/obs_only/crm_best.pt\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"197596\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-spatial.log\", \"submitted_at\": \"2026-05-14T12:17:10.754Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"CRM obs_only v2 (990D input, no conformal features)\", \"seed\": 42, \"hypothesis\": \"obs_only CRM ablation — CRM without conformal features\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v2/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"failure_reason\": \"evaluate.py has no crm_obs_only mode. --mode acr_vla loads CRM expecting 1030D input but obs_only checkpoint has 990D (no conformal features). Replaced by eval-obs-only-spatial-v2.\", \"wall_clock_seconds\": 1392.5, \"gpu_hours\": 0.39}, \"conclusion\": \"failed\", \"metrics\": {\"error\": \"size mismatch: obs_only CRM net.0.weight [256,990] vs acr_vla expects [256,1030] — no crm_obs_only mode in evaluate.py\"}, \"completed_at\": \"2026-05-14T12:40:23.205Z\"}, \"crm-train-v2-obs-only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T09:41:35.819Z\", \"updated_at\": \"2026-05-14T12:17:42.122Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 python -u src/train_crm.py --benchmark spatial object --cache_dir /root/autodl-tmp/crm_cache_v5/ --output_dir /root/autodl-tmp/checkpoints/crm_v2/obs_only/ --K 10 --epochs 50 --batch_size 512 --lr 0.016 --input_mode obs_only --seed 42\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"187913\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-train-v2-obs-only.log\", \"submitted_at\": \"2026-05-14T09:41:35.736Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/crm_cache_v5/\", \"data_count\": 26737, \"model_name\": \"CRM obs_only v2\", \"seed\": 42, \"wall_clock_seconds\": 9366.4, \"gpu_hours\": 2.6}, \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.050501, \"best_epoch\": 50, \"total_epochs\": 50, \"final_train_loss\": 0.074839, \"comparison_vs_old\": \"old_6D_buggy=0.018312, new=0.050501 (loss metric changed with v2 fix)\"}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v2/obs_only/crm_best.pt\", \"log_path\": \"/root/runs/acr-vla-conformal-refinement/crm-train-v2-obs-only.log\", \"completed_at\": \"2026-05-14T12:17:42.122Z\"}, \"crm-train-v2-scalar-unc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T09:30:43.696Z\", \"updated_at\": \"2026-05-14T12:17:01.093Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=1 python -u src/train_crm.py --benchmark spatial object --cache_dir /root/autodl-tmp/crm_cache_v5/ --output_dir /root/autodl-tmp/checkpoints/crm_v2/scalar_unc/ --K 10 --epochs 50 --batch_size 512 --lr 0.016 --input_mode scalar_unc --seed 42\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"186964\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-train-v2-scalar-unc.log\", \"submitted_at\": \"2026-05-14T09:30:43.616Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/crm_cache_v5/\", \"data_count\": 26737, \"model_name\": \"CRM scalar-unc v2 (327K params, 8D state fix)\", \"seed\": 42, \"hypothesis\": \"Scalar CRM v2 ablation — per-DOF expected to outperform on task success rate despite similar val_loss\", \"wall_clock_seconds\": 9977.5, \"gpu_hours\": 2.77}, \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.047202, \"best_epoch\": 48, \"total_epochs\": 50, \"final_train_loss\": 0.069679, \"comparison_vs_old\": \"old_6D_buggy=0.008379, new=0.047202 (loss metric changed with v2 fix)\"}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v2/scalar_unc/crm_best.pt\", \"log_path\": \"/root/runs/acr-vla-conformal-refinement/crm-train-v2-scalar-unc.log\", \"completed_at\": \"2026-05-14T12:17:01.093Z\"}, \"crm-train-v2-perdof\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T09:30:40.796Z\", \"updated_at\": \"2026-05-14T12:17:00.195Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 python -u src/train_crm.py --benchmark spatial object --cache_dir /root/autodl-tmp/crm_cache_v5/ --output_dir /root/autodl-tmp/checkpoints/crm_v2/perdof/ --K 10 --epochs 50 --batch_size 512 --lr 0.016 --input_mode full --seed 42\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"186823\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-train-v2-perdof.log\", \"submitted_at\": \"2026-05-14T09:30:40.716Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/crm_cache_v5/\", \"data_count\": 26737, \"model_name\": \"CRM per-DOF v2 (337K params, 8D state fix, argmin base, L2 clip)\", \"seed\": 42, \"hypothesis\": \"Per-DOF CRM v2 with D016 fixes (8D state, argmin base, alpha=0.5, L2 clipping) improves over pre-fix version\", \"wall_clock_seconds\": 9979.5, \"gpu_hours\": 2.77}, \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.051684, \"best_epoch\": 48, \"total_epochs\": 50, \"final_train_loss\": 0.076748, \"comparison_vs_old\": \"old_6D_buggy=0.009046, new=0.051684 (loss metric changed with v2 fix)\"}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v2/perdof/crm_best.pt\", \"log_path\": \"/root/runs/acr-vla-conformal-refinement/crm-train-v2-perdof.log\", \"completed_at\": \"2026-05-14T12:17:00.195Z\"}, \"eval-reconvla-spatial-v3\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-13T23:04:34.297Z\", \"updated_at\": \"2026-05-14T11:10:55.009Z\", \"reproduce\": {\"finished_at\": \"2026-05-14T11:07:49.901Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-13T23:34:14.141Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:34:15.524386+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T11:07:51.915540+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode reconvla --benchmark spatial --n_rollouts 10 --seed 42 --K 10\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"118108\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"SampleConsensus (scalar Euclidean argmin)\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/eval_results/eval-reconvla-spatial-v3.log\", \"hypothesis\": \"SampleConsensus scalar baseline for ACR-VLA comparison\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\"}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.34, \"total_successes\": 34, \"total_rollouts\": 100, \"per_task\": {\"pick_up_black_bowl_between_plate_and_ramekin\": 0.6, \"pick_up_black_bowl_next_to_ramekin\": 1, \"pick_up_black_bowl_from_table_center\": 0, \"pick_up_black_bowl_on_cookie_box\": 0.3, \"pick_up_black_bowl_in_top_drawer\": 0.1, \"pick_up_black_bowl_on_ramekin\": 0.1, \"pick_up_black_bowl_next_to_cookie_box\": 0.9, \"pick_up_black_bowl_on_stove\": 0, \"pick_up_black_bowl_next_to_plate\": 0.4, \"pick_up_black_bowl_on_wooden_cabinet\": 0}}, \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"/root/autodl-tmp/eval_results/eval-reconvla-spatial-v3.log\"}, \"precompute-v5-shard2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:55:02.277Z\", \"updated_at\": \"2026-05-14T09:28:09.308Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 python -u src/train_crm.py --precompute --benchmark spatial object --cache_dir /root/autodl-tmp/crm_cache_v5/ --K 10 --shard_id 2 --num_shards 3 --max_demos_per_task 10 --precompute_batch_size 4 --save_every 500\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"180480\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v5-shard2.log\", \"submitted_at\": \"2026-05-14T07:56:37.531Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial + object)\", \"data_count\": \"~8900 samples (shard 2 of 3)\", \"model_name\": \"SmolVLA 450M (precompute K=10 features)\", \"seed\": 42, \"hypothesis\": \"Phase 2 precompute with 8D state fix (C1) for per-DOF CRM retraining\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache_v5/\", \"wall_clock_seconds\": 5491.8, \"gpu_hours\": 1.53}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T09:28:09.308Z\"}, \"precompute-v5-shard1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:55:00.276Z\", \"updated_at\": \"2026-05-14T09:28:07.934Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=1 python -u src/train_crm.py --precompute --benchmark spatial object --cache_dir /root/autodl-tmp/crm_cache_v5/ --K 10 --shard_id 1 --num_shards 3 --max_demos_per_task 10 --precompute_batch_size 4 --save_every 500\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"180400\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v5-shard1.log\", \"submitted_at\": \"2026-05-14T07:56:35.789Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial + object)\", \"data_count\": \"~8900 samples (shard 1 of 3)\", \"model_name\": \"SmolVLA 450M (precompute K=10 features)\", \"seed\": 42, \"hypothesis\": \"Phase 2 precompute with 8D state fix (C1) for per-DOF CRM retraining\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache_v5/\", \"wall_clock_seconds\": 5492.1, \"gpu_hours\": 1.53}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T09:28:07.934Z\"}, \"precompute-v5-shard0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:54:59.383Z\", \"updated_at\": \"2026-05-14T09:28:06.626Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 python -u src/train_crm.py --precompute --benchmark spatial object --cache_dir /root/autodl-tmp/crm_cache_v5/ --K 10 --shard_id 0 --num_shards 3 --max_demos_per_task 10 --precompute_batch_size 4 --save_every 500\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"180251\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v5-shard0.log\", \"submitted_at\": \"2026-05-14T07:56:33.414Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial + object)\", \"data_count\": \"~8900 samples (shard 0 of 3)\", \"model_name\": \"SmolVLA 450M (precompute K=10 features)\", \"seed\": 42, \"hypothesis\": \"Phase 2 precompute with 8D state fix (C1) for per-DOF CRM retraining\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache_v5/\", \"wall_clock_seconds\": 5493.2, \"gpu_hours\": 1.53}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T09:28:06.626Z\"}, \"crm-train-a4-scalar-unc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:48:40.837Z\", \"updated_at\": \"2026-05-14T07:59:32.676Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/train_crm.py --benchmark spatial object --epochs 50 --batch_size 32 --lr 0.001 --K 10 --seed 42 --input_mode scalar_unc --output_dir /root/autodl-tmp/checkpoints/crm/scalar_unc/\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"121984\", \"data_path\": \"/root/autodl-tmp/crm_cache/\", \"data_count\": 26737, \"model_name\": \"CRM-scalar_unc (3D scalar uncertainty)\", \"seed\": 42, \"hypothesis\": \"CRM with scalar Euclidean uncertainty (3D) performs worse than per-DOF (40D), validating per-DOF advantage. Ablation A4, hyperparams matched to plan_001 (bs=32/lr=1e-3).\", \"log_path\": \"/root/autodl-tmp/checkpoints/crm/scalar_unc/train.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm/scalar_unc/crm_best.pt\", \"conclusion_note\": \"Training converged. scalar val_loss 0.008379 < per-DOF 0.009046 — original hypothesis (scalar worse) NOT confirmed on val_loss. Hypothesis pending eval-scalar-unc-spatial task success rate validation.\"}, \"conclusion\": \"killed\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm/scalar_unc/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/checkpoints/crm/scalar_unc/train.log\", \"metrics\": {\"best_val_loss\": 0.008379, \"best_epoch\": 48, \"total_epochs\": 50, \"final_val_loss\": 0.008384, \"final_train_loss\": 0.012959}, \"completed_at\": \"2026-05-14T02:21:00.891Z\", \"conclusion_note\": \"invalidated by D016 C1 fix, 6D state mismatch — checkpoint trained on wrong features\"}, \"crm-train-a3-obs-only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:56:28.643Z\", \"updated_at\": \"2026-05-14T07:59:31.277Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/train_crm.py --benchmark spatial object --epochs 50 --batch_size 512 --lr 0.016 --K 10 --seed 42 --input_mode obs_only --output_dir /root/autodl-tmp/checkpoints/crm/obs_only/\", \"server\": \"bjb1-18228\", \"data_path\": \"/root/autodl-tmp/crm_cache/\", \"data_count\": 26737, \"model_name\": \"CRM-obs_only\", \"seed\": 42, \"hypothesis\": \"CRM without conformal features (obs_only, 990D input) performs significantly worse than full CRM (1030D), validating that per-DOF conformal features are necessary for effective correction\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm/obs_only/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/checkpoints/crm/obs_only/train.log\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T23:43:51.534Z\", \"metrics\": {\"best_val_loss\": 0.018312, \"best_epoch\": 4, \"early_stopped_at_epoch\": \"~15-20\", \"early_stop_reason\": \"val_loss plateau at 0.018 for 10+ epochs (full CRM: 0.009, 2x gap confirms conformal features are critical)\", \"input_dim\": 990, \"params\": 327966}, \"conclusion_note\": \"invalidated by D016 C1 fix, 6D state mismatch — checkpoint trained on wrong features\"}, \"crm-train-v1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:10:36.535Z\", \"updated_at\": \"2026-05-14T07:59:30.290Z\", \"spec\": {\"command\": \"python -u src/train_crm.py --benchmark spatial object --epochs 50 --batch_size 32 --lr 1e-3 --K 10 --seed 42\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"78520\", \"log_path\": \"/root/runs/acr-vla-conformal-refinement/crm-train-v1.log\", \"data_path\": \"/root/autodl-tmp/crm_cache/ (spatial: 12167 + object: 14570 = 26737 samples)\", \"data_count\": 26737, \"model_name\": \"CRM MLP (337K params, 1030D→256→256→30D)\", \"seed\": 42, \"hypothesis\": \"CRM with per-DOF conformal features (1030D input) learns dimension-selective correction, achieving lower action MSE than scalar/no-uncertainty ablations\", \"checkpoint_source\": \"precompute-v4 (spatial+object)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm/\"}, \"reproduce\": {\"finished_at\": \"2026-05-13T22:40:27.930Z\"}, \"failure_reason\": \"RESOLVED: EXIT_CODE=129 was SIGHUP after training completed (50/50 epochs). Not a real failure.\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T22:40:28.559Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T22:40:29.429643+00:00\"}]}, \"metrics\": {\"best_val_loss\": 0.009046, \"best_epoch\": 50, \"total_epochs\": 50, \"checkpoint\": \"crm_best.pt\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm/crm_best.pt\", \"exit_code_note\": \"129 was false alarm - SIGHUP after training completed\"}, \"conclusion_note\": \"invalidated by D016 C1 fix, 6D state mismatch — checkpoint trained on wrong features\"}, \"crm-train-k5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T01:42:55.911Z\", \"updated_at\": \"2026-05-14T07:59:29.396Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/train_crm.py --benchmark spatial object --epochs 50 --batch_size 32 --lr 0.001 --K 5 --seed 42 --cache_dir /root/autodl-tmp/crm_cache_k5/ --output_dir /root/autodl-tmp/checkpoints/crm/k5/\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"139839\", \"data_path\": \"/root/autodl-tmp/crm_cache_k5/\", \"data_count\": 26737, \"model_name\": \"CRM (K=5, 337K params)\", \"seed\": 42, \"hypothesis\": \"CRM with K=5 conformal samples for K sensitivity ablation (K=10 baseline val_loss=0.009046)\", \"log_path\": \"/root/autodl-tmp/checkpoints/crm/k5/train.log\", \"checkpoint_source\": \"from_scratch\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm/k5/crm_best.pt\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T04:12:42.247Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T04:12:44.286094+00:00\"}]}, \"conclusion\": \"killed\", \"metrics\": {\"best_val_loss\": 0.008996, \"best_epoch\": 50, \"total_epochs\": 50, \"comparison\": \"K=5 val_loss 0.008996 ≈ K=10 val_loss 0.009046, near identical\"}, \"completed_at\": \"2026-05-14T07:21:32.072Z\", \"conclusion_note\": \"invalidated by D016 C1 fix, 6D state mismatch — checkpoint trained on wrong features\"}, \"eval-scalar-unc-spatial\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:54:30.549Z\", \"updated_at\": \"2026-05-14T07:52:44.766Z\", \"spec\": {\"hypothesis\": \"Scalar CRM (3D unc) vs per-DOF CRM (40D unc) on spatial task success rate. Val_loss favored scalar (0.008 vs 0.009) but per-DOF expected to win on task success via dimension-selective correction.\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"CRM-scalar_unc (3D scalar uncertainty, 327K params)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm/scalar_unc/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode crm_scalar --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm/scalar_unc/crm_best.pt\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"143206\", \"log_path\": \"/root/autodl-tmp/eval_results/eval-scalar-unc-spatial.log\", \"failure_reason\": \"D016: C1 (state 6D→8D mismatch). Scalar CRM trained on wrong features. Replaced by eval-scalar-unc-spatial-v2.\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T07:52:15.933Z\", \"conclusion_note\": \"invalidated by D016 C1 bug, pre-fix data collected\"}, \"eval-acr-spatial-v2\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-13T23:04:32.138Z\", \"updated_at\": \"2026-05-14T07:52:43.327Z\", \"reproduce\": {\"finished_at\": \"2026-05-13T23:31:30.005Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-13T23:31:31.129Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:31:32.734610+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm/crm_best.pt\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"117814\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"ACR-VLA (SmolVLA + CRM per-DOF)\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/eval_results/eval-acr-spatial-v2.log\", \"hypothesis\": \"ACR-VLA per-DOF correction improves over SmolVLA baseline on spatial\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"failure_reason\": \"D016: C1 (state 6D→8D mismatch) + W3 (alpha 0.1→0.5). CRM trained on wrong features + CGS quantile wrong. Replaced by eval-acr-spatial-v3.\"}, \"conclusion\": \"killed\", \"conclusion_note\": \"invalidated by D016 C1 bug, pre-fix data collected\"}, \"eval-k5-spatial\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T04:14:23.092Z\", \"updated_at\": \"2026-05-14T07:52:43.134Z\", \"spec\": {\"command\": \"MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 5 --crm_checkpoint /root/autodl-tmp/checkpoints/crm/k5/crm_best.pt\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"154189\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"ACR-VLA K=5 (CRM 337K + SmolVLA 450M)\", \"seed\": 42, \"hypothesis\": \"K=5 vs K=10 ACR-VLA on task success rate.\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm/k5/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"log_path\": \"/root/autodl-tmp/eval_results/eval-k5-spatial.log\", \"failure_reason\": \"D016: C1 (state 6D→8D mismatch) + W3 (alpha 0.1→0.5). CRM K=5 trained on wrong features. Replaced by eval-k5-spatial-v2.\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T07:52:14.685Z\", \"conclusion_note\": \"invalidated by D016 C1 bug, pre-fix data collected\"}, \"eval-object-v8-full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T00:05:25.647Z\", \"updated_at\": \"2026-05-14T03:10:30.457Z\", \"spec\": {\"hypothesis\": \"SmolVLA baseline on libero_object with K=1 fix (vla_only single inference)\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\", \"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 42\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"125830\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_object/\", \"data_count\": 100, \"model_name\": \"smolvla_libero\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/eval_results/eval-object-v6.log\"}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13, \"total_successes\": 13, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}, \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-14T03:10:30.457Z\"}, \"eval-spatial-v7-full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T00:05:16.510Z\", \"updated_at\": \"2026-05-14T01:45:58.391Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 10 --seed 42\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"123761\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"lerobot/smolvla_libero\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/eval_results/eval-spatial-v7.log\", \"hypothesis\": \"SmolVLA baseline on libero_spatial with K=1 fix (vla_only single inference)\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\"}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.3, \"total_successes\": 30, \"total_episodes\": 100, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"pick_up_black_bowl_between_plate_and_ramekin\": 0.6, \"pick_up_black_bowl_next_to_ramekin\": 1, \"pick_up_black_bowl_from_table_center\": 0, \"pick_up_black_bowl_on_cookie_box\": 0.2, \"pick_up_black_bowl_in_top_drawer\": 0, \"pick_up_black_bowl_on_ramekin\": 0, \"pick_up_black_bowl_next_to_cookie_box\": 0.9, \"pick_up_black_bowl_on_stove\": 0, \"pick_up_black_bowl_next_to_plate\": 0.3, \"pick_up_black_bowl_on_wooden_cabinet\": 0}}, \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-14T01:45:58.391Z\"}, \"eval-object-v7-full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T00:03:35.642Z\", \"updated_at\": \"2026-05-14T01:45:48.892Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 42\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"125830\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_object/\", \"data_count\": 100, \"model_name\": \"smolvla_libero\", \"seed\": 42, \"hypothesis\": \"SmolVLA baseline on libero_object with K=1 fix (single inference per step)\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\", \"log_path\": \"/root/autodl-tmp/eval_results/eval-object-v6.log\", \"failure_reason\": \"Duplicate entry — same PID 125830 tracked by eval-object-v8-full. Cleaning up.\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T01:45:48.892Z\"}, \"eval-spatial-v6-full\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-13T23:04:28.766Z\", \"updated_at\": \"2026-05-14T00:05:22.619Z\", \"reproduce\": {\"finished_at\": \"2026-05-14T00:03:28.470Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-13T23:34:09.898Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:34:11.481851+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T00:03:30.351859+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 10 --seed 42\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"117486\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"lerobot/smolvla_libero\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/eval_results/eval-spatial-v6-full.log\", \"hypothesis\": \"SmolVLA baseline on libero_spatial with fixed evaluate.py (reset→set_init_state→zero-action)\", \"failure_reason\": \"vla_only mode running K=10 instead of K=1, wasting GPU. Killed and restarted with K=1 fix.\"}, \"conclusion\": \"killed\"}, \"eval-object-v5-full\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-13T23:17:35.776Z\", \"updated_at\": \"2026-05-14T00:04:26.792Z\", \"reproduce\": {\"finished_at\": \"2026-05-13T23:43:52.899Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-13T23:43:53.809Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:43:56.187212+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 42 --smolvla_path /root/autodl-tmp/models/smolvla_libero/\", \"server\": \"bjb2-40593\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_object/\", \"data_count\": 100, \"model_name\": \"smolvla_libero\", \"seed\": 42, \"pid\": 117697, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-object-v5-full.log\", \"gpu\": \"cuda:0\", \"note\": \"restored from false DONE/failed — cron misdetected tmux pipe buffering as process exit\", \"failure_reason\": \"vla_only mode running K=10 multi-sampling (should be K=1). Killed by Director order, replaced by eval-object-v7-full with K=1 fix.\"}, \"conclusion\": \"killed\"}, \"eval-acr-vla-spatial-v1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:56:40.287Z\", \"updated_at\": \"2026-05-13T23:14:22.561Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm/crm_best.pt --output_file /root/autodl-tmp/eval_results/acr_vla_spatial_v1.json\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO spatial benchmark (10 tasks)\", \"data_count\": 100, \"model_name\": \"ACR-VLA (SmolVLA + CRM perdof)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm/crm_best.pt\", \"eval_data\": \"LIBERO spatial, 10 tasks x 10 rollouts\", \"parent\": \"train-crm-v1\", \"failure_reason\": \"P0 bug: evaluate.py env.reset() 覆盖 set_init_state 的 demo 初始状态，结果不可信。已被 eval-acr-spatial-v2 替代\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T23:13:00.422Z\"}, \"eval-acr-spatial-v1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:54:28.535Z\", \"updated_at\": \"2026-05-13T23:12:11.315Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm/crm_best.pt --output_file /root/autodl-tmp/eval_results/eval-acr-spatial-v1.json\", \"server\": \"bjb1-18228\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"ACR-VLA (SmolVLA + CRM)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm/crm_best.pt\", \"eval_data\": \"LIBERO spatial (10 tasks x 10 rollouts)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/eval_results/eval-acr-spatial-v1.log\", \"failure_reason\": \"P0 bug: evaluate.py env.reset() 覆盖 set_init_state 的 demo 初始状态，结果不可信\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T23:09:38.077Z\"}, \"eval-reconvla-spatial-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:29:41.730Z\", \"updated_at\": \"2026-05-13T23:12:10.958Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark spatial --n_rollouts 10 --seed 42 --K 10\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"87787\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-reconvla-spatial-v1.log\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"smolvla_libero + ReconVLA argmin\", \"seed\": 42, \"hypothesis\": \"ReconVLA (scalar Euclidean nonconformity + argmin) as baseline for ACR-VLA comparison\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"libero_spatial 10 tasks\", \"failure_reason\": \"P0 bug: evaluate.py env.reset() 覆盖 set_init_state 的 demo 初始状态，结果不可信\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T23:09:40.252Z\"}, \"eval-object-v4-full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T19:13:26.341Z\", \"updated_at\": \"2026-05-13T23:12:10.037Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 42\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"103768\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-object-v4-full.log\", \"data_path\": \"/root/autodl-tmp/libero_data/ (object)\", \"data_count\": 100, \"model_name\": \"lerobot/smolvla_libero\", \"seed\": 42, \"hypothesis\": \"SmolVLA with verified-deployed wrapper achieves meaningful success rate on libero_object\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"libero_object 10 tasks\", \"failure_reason\": \"P0 bug: evaluate.py env.reset() 覆盖 set_init_state 的 demo 初始状态，结果不可信\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T23:09:39.017Z\"}, \"eval-spatial-v5-full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T19:16:58.052Z\", \"updated_at\": \"2026-05-13T23:12:09.066Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 10 --seed 42\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"73756\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-spatial-v5-full.log\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"lerobot/smolvla_libero\", \"seed\": 42, \"hypothesis\": \"SmolVLA with verified wrapper + dual camera (agentview + eye_in_hand) achieves >50% on libero_spatial\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"libero_spatial 10 tasks\", \"failure_reason\": \"P0 bug: evaluate.py env.reset() 覆盖 set_init_state 的 demo 初始状态，结果不可信\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T23:09:39.445Z\"}, \"precompute-k5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:15:37.603Z\", \"updated_at\": \"2026-05-13T22:12:39.543Z\", \"spec\": {\"command\": \"python -u src/train_crm.py --precompute --benchmark spatial object --K 5 --cache_dir /root/autodl-tmp/crm_cache_k5/\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"79517\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-k5.log\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 26737, \"model_name\": \"smolvla_libero\", \"seed\": 42, \"hypothesis\": \"K=5 precompute for K sensitivity ablation (plan_015)\"}, \"reproduce\": {\"finished_at\": \"2026-05-13T22:09:33.445Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T22:09:34.396952+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache_k5/\", \"metrics\": {\"spatial_samples\": 12167, \"object_samples\": 14570, \"total_samples\": 26737, \"spatial_cache_mb\": 106, \"object_cache_mb\": 127, \"total_cache_mb\": 233, \"runtime_min\": 107}, \"completed_at\": \"2026-05-13T22:12:39.543Z\"}, \"mvp-point-reaching\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T01:22:10.415Z\", \"updated_at\": \"2026-05-13T22:06:11.073Z\", \"spec\": {\"hypothesis\": \"Per-DOF uncertainty features carry more actionable information than scalar uncertainty summaries, enabling dimension-selective correction\", \"description\": \"3D point-reaching MVP: 3 MLP variants (scalar/per-DOF/no uncertainty) x 6 groups (3 anisotropy ratios x 2 uncertainty sources)\", \"server\": \"bjb2-40593\", \"gpu\": \"cuda:0\", \"data_count\": 20000, \"model_name\": \"CorrectionMLP(2-layer, 64-hidden)\", \"seed\": 42, \"command\": \"python -u run_mvp.py\", \"data_path\": \"synthetic (generated in-script)\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/mvp/\", \"log_path\": \"/root/acr-vla-conformal-refinement/mvp/mvp_results.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T01:44:00.055Z\", \"metrics\": {\"group1_oracle\": {\"A_scalar\": {\"mse_x\": 0.180218, \"mse_y\": 0.02497, \"mse_z\": 0.024232, \"total\": 0.076473}, \"B_perDOF\": {\"mse_x\": 0.172652, \"mse_y\": 0.015544, \"mse_z\": 0.01561, \"total\": 0.067935}, \"C_none\": {\"mse_x\": 0.22706, \"mse_y\": 0.025542, \"mse_z\": 0.024753, \"total\": 0.092451}}, \"group2_oracle\": {\"A_scalar\": {\"mse_x\": 0.064642, \"mse_y\": 0.023836, \"mse_z\": 0.022967, \"total\": 0.037148}, \"B_perDOF\": {\"mse_x\": 0.053403, \"mse_y\": 0.015695, \"mse_z\": 0.01573, \"total\": 0.028276}, \"C_none\": {\"mse_x\": 0.084178, \"mse_y\": 0.025427, \"mse_z\": 0.024798, \"total\": 0.044801}}, \"group3_oracle\": {\"A_scalar\": {\"mse_x\": 0.042948, \"mse_y\": 0.023218, \"mse_z\": 0.022365, \"total\": 0.02951}, \"B_perDOF\": {\"mse_x\": 0.033008, \"mse_y\": 0.015621, \"mse_z\": 0.015647, \"total\": 0.021425}, \"C_none\": {\"mse_x\": 0.053043, \"mse_y\": 0.025523, \"mse_z\": 0.024741, \"total\": 0.034436}}, \"group4_K10\": {\"A_scalar\": {\"mse_x\": 0.187418, \"mse_y\": 0.024701, \"mse_z\": 0.024277, \"total\": 0.078799}, \"B_perDOF\": {\"mse_x\": 0.182888, \"mse_y\": 0.019072, \"mse_z\": 0.018475, \"total\": 0.073478}, \"C_none\": {\"mse_x\": 0.21507, \"mse_y\": 0.02496, \"mse_z\": 0.024637, \"total\": 0.088223}}, \"group5_K10\": {\"A_scalar\": {\"mse_x\": 0.064895, \"mse_y\": 0.02386, \"mse_z\": 0.023596, \"total\": 0.037451}, \"B_perDOF\": {\"mse_x\": 0.05851, \"mse_y\": 0.018868, \"mse_z\": 0.018471, \"total\": 0.03195}, \"C_none\": {\"mse_x\": 0.077047, \"mse_y\": 0.024825, \"mse_z\": 0.02464, \"total\": 0.042171}}, \"group6_K10\": {\"A_scalar\": {\"mse_x\": 0.041848, \"mse_y\": 0.02344, \"mse_z\": 0.023207, \"total\": 0.029498}, \"B_perDOF\": {\"mse_x\": 0.036348, \"mse_y\": 0.018736, \"mse_z\": 0.018453, \"total\": 0.024512}, \"C_none\": {\"mse_x\": 0.048365, \"mse_y\": 0.024827, \"mse_z\": 0.024577, \"total\": 0.03259}}, \"pass_criteria\": {\"group1\": \"PASS\", \"group4\": \"PASS\", \"overall\": \"SUCCESS\"}, \"summary_pct_improvements\": {\"reference_group\": \"group4_K10 (sigma=0.5/0.1/0.1, K=10 estimated uncertainty)\", \"perDOF_vs_scalar_total\": 6.75, \"perDOF_vs_none_total\": 16.71, \"perDOF_vs_scalar_y_axis\": 22.79, \"perDOF_vs_scalar_z_axis\": 23.9, \"paper_claims\": {\"6.7_pct_over_scalar\": \"group4 total: (0.078799-0.073478)/0.078799 = 6.75%\", \"16.7_pct_over_none\": \"group4 total: (0.088223-0.073478)/0.088223 = 16.71%\", \"22_24_pct_per_axis\": \"group4 y: 22.79%, z: 23.90%\"}}}}, \"eval-spatial-v3-full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T17:38:57.194Z\", \"updated_at\": \"2026-05-13T19:09:00.612Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl && python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 10 --seed 42 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ 2>&1\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"62654\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-spatial-v3-full.log\", \"submitted_at\": \"2026-05-13T17:38:57.172Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": \"10 tasks x 10 rollouts x 300 steps\", \"model_name\": \"lerobot/smolvla_libero (450M, rewritten wrapper aligned with lerobot pipeline)\", \"seed\": 42, \"hypothesis\": \"Rewritten wrapper (fully aligned with lerobot SmolVLAPolicy) achieves >50% on libero_spatial with 10 rollouts\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"failure_reason\": \"D014: wrapper 修复版从未部署到服务器，使用旧 buggy 代码运行，产出无效\", \"wall_clock_seconds\": 5403.4, \"gpu_hours\": 1.5}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T19:09:00.612Z\"}, \"eval-spatial-reeval-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T16:08:51.171Z\", \"updated_at\": \"2026-05-13T16:14:40.934Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 3 --seed 42 --smolvla_path /root/autodl-tmp/models/smolvla_libero/\", \"server\": \"autodl-4090x4\", \"gpu\": [\"cuda:0\"], \"pid\": \"87385\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": \"10 tasks x 3 rollouts x 300 steps\", \"model_name\": \"lerobot/smolvla_libero (450M, full fine-tuned)\", \"seed\": 42, \"hypothesis\": \"Fixed wrapper (7 bugs) achieves >50% on libero_spatial\", \"log_path\": \"/tmp/eval_spatial.log\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"failure_reason\": \"Killed by Director - wrapper not fully fixed, 55.6% result unreliable. Redirected to full wrapper rewrite aligned with lerobot pipeline.\", \"checkpoint_path\": \"N/A\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T16:14:40.934Z\"}, \"eval-smolvla-libero-spatial\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T11:35:16.236Z\", \"updated_at\": \"2026-05-13T15:45:51.082Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 3 --seed 42\", \"server\": \"autodl-4090x4\", \"gpu\": [\"cuda:0\"], \"pid\": \"43809\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": \"10 tasks x 3 rollouts x 300 steps\", \"model_name\": \"lerobot/smolvla_libero (450M, full fine-tuned on libero_spatial)\", \"seed\": 42, \"hypothesis\": \"Validate smolvla_libero checkpoint with fixed wrapper (correct state repr, 256x256 images, 7D action) achieves >50% success on libero_spatial\", \"log_path\": \"/tmp/eval_spatial_full.log\", \"checkpoint_source\": \"lerobot/smolvla_libero (HuggingFace community checkpoint)\", \"failure_reason\": \"smolvla_libero 0% on spatial - 6 wrapper bugs: image flip/size/normalization, state 6D→8D, state normalization, action denormalization all missing\", \"checkpoint_path\": \"N/A\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T15:45:51.082Z\"}, \"precompute-shard2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T11:57:48.056Z\", \"updated_at\": \"2026-05-13T15:26:07.463Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 2 --num_shards 3 --seed 42 --K 10\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"47186\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-shard2.log\", \"submitted_at\": \"2026-05-13T11:57:48.042Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache/\", \"wall_clock_seconds\": 12499.4, \"gpu_hours\": 3.47}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T15:26:07.463Z\"}, \"precompute-shard1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T11:57:46.669Z\", \"updated_at\": \"2026-05-13T15:26:06.485Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 1 --num_shards 3 --seed 42 --K 10\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"47044\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-shard1.log\", \"submitted_at\": \"2026-05-13T11:57:46.654Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache/\", \"wall_clock_seconds\": 12499.8, \"gpu_hours\": 3.47}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T15:26:06.485Z\"}, \"precompute-shard0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T11:57:45.284Z\", \"updated_at\": \"2026-05-13T15:26:05.433Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 0 --num_shards 3 --seed 42 --K 10\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"46966\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-shard0.log\", \"submitted_at\": \"2026-05-13T11:57:45.270Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache/\", \"wall_clock_seconds\": 12500.2, \"gpu_hours\": 3.47}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T15:26:05.433Z\"}, \"plan_014-reconvla-baseline\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-13T06:56:12.892Z\", \"updated_at\": \"2026-05-13T11:07:20.019Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark spatial object --n_rollouts 20 --seed 42\", \"server\": \"autodl-4090\", \"gpu\": [\"cuda:0\"], \"pid\": \"50790\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/plan_014-reconvla-baseline.log\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial + object)\", \"data_count\": \"20 tasks x 20 rollouts = 400 episodes\", \"model_name\": \"SmolVLA (450M) + ReconVLA argmin selection\", \"seed\": 42, \"hypothesis\": \"ReconVLA (scalar Euclidean nonconformity + argmin selection) as baseline for ACR-VLA comparison\", \"fixes_applied\": [\"BDDL path: use benchmark_instance.get_task_bddl_file_path()\", \"LIBERO assets copied from GitHub repo\"]}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T11:07:20.019Z\"}, \"plan_001-crm-smolvla\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T03:01:07.682Z\", \"updated_at\": \"2026-05-13T05:44:07.131Z\", \"spec\": {\"command\": \"python -u src/train_crm.py --auto --benchmark spatial object --epochs 50 --batch_size 32 --lr 1e-3 --seed 42 --K 10\", \"server\": \"autodl-4090\", \"gpu\": [\"cuda:0\"], \"pid\": \"32811\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/plan_001-crm-smolvla.log\", \"submitted_at\": \"2026-05-13T04:54:14.975Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial + object)\", \"data_count\": 1000, \"model_name\": \"CRM (337K) + SmolVLA (450M)\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm/\", \"hypothesis\": \"Per-DOF conformal features enable dimension-selective action correction on LIBERO\", \"wall_clock_seconds\": 2992.2, \"gpu_hours\": 0.83}, \"conclusion\": \"failed\", \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"completed_at\": \"2026-05-13T05:44:07.131Z\"}}, \"count\": 137, \"total\": 137, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7602}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 11_

Registry output is too large for direct context. Let me use a subagent to extract the relevant magnitude curve and seed comparison data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "34989fa3-9ada-42d0-a97b-642b78165ff8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013r6wURTjuBbqs4TEfJrMtN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 688,
      "cache_read_input_tokens": 25149,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 688
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

_source line 12_

<details open><summary>🔧 Tool call — Agent · `toolu_01NvDCriszJntJmm1x8xpQz3`</summary>

```json
{
  "description": "Extract magnitude curve data from registry",
  "prompt": "I need to extract specific experiment data from a large JSON registry file. The file is at:\n/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/18137809-ea2c-4289-a326-73c48f2a7d35/tool-results/mcp-agent-ml-research-read_registry-1778957798211.txt\n\nThe file has schema: {result: string} where result is a JSON string containing experiment data.\n\nI need you to:\n1. First probe the structure (jq type, length, keys)\n2. Then extract ALL experiments that are relevant to the \"magnitude curve\" analysis. These are experiments that involve:\n   - obs_only strategy with various norm levels (0.03, 0.05, 0.10, 0.20, 0.30, and default ~1.42)\n   - perdof strategy with same norm levels\n   - argmin strategy experiments\n   - Any multi-seed experiments (seed42, seed43, seed44, seed45, seed46)\n\nFor each relevant experiment, I need:\n- exp_id\n- The strategy/method (obs_only, perdof, argmin)\n- The norm value used\n- The seed\n- Success rate (SR)\n- Number of successes and total trials\n- Any relevant metrics\n\nPlease output a structured summary with ALL data points organized by:\nA) Magnitude curve (seed42): obs_only and perdof at each norm level\nB) Seed comparison: obs_only_norm02 across seeds, argmin across seeds, perdof across seeds\n\nBe thorough - extract every single data point. Quote exp_ids exactly.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "180634b5-df2c-48c9-a157-c8bcfe2e5269",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013r6wURTjuBbqs4TEfJrMtN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 688,
      "cache_read_input_tokens": 25149,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 688
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

### System

_source line 13_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a6eebf2158cc00587",
  "tool_use_id": "toolu_01NvDCriszJntJmm1x8xpQz3",
  "description": "Extract magnitude curve data from registry",
  "task_type": "local_agent",
  "prompt": "I need to extract specific experiment data from a large JSON registry file. The file is at:\n/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/18137809-ea2c-4289-a326-73c48f2a7d35/tool-results/mcp-agent-ml-research-read_registry-1778957798211.txt\n\nThe file has schema: {result: string} where result is a JSON string containing experiment data.\n\nI need you to:\n1. First probe the structure (jq type, length, keys)\n2. Then extract ALL experiments that are relevant to the \"magnitude curve\" analysis. These are experiments that involve:\n   - obs_only strategy with various norm levels (0.03, 0.05, 0.10, 0.20, 0.30, and default ~1.42)\n   - perdof strategy with same norm levels\n   - argmin strategy experiments\n   - Any multi-seed experiments (seed42, seed43, seed44, seed45, seed46)\n\nFor each relevant experiment, I need:\n- exp_id\n- The strategy/method (obs_only, perdof, argmin)\n- The norm value used\n- The seed\n- Success rate (SR)\n- Number of successes and total trials\n- Any relevant metrics\n\nPlease output a structured summary with ALL data points organized by:\nA) Magnitude curve (seed42): obs_only and perdof at each norm level\nB) Seed comparison: obs_only_norm02 across seeds, argmin across seeds, perdof across seeds\n\nBe thorough - extract every single data point. Quote exp_ids exactly.",
  "uuid": "4732729c-8630-4977-94fe-04771140cb9d",
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35"
}
```

---

## Round 1

66 recorded events

### User

_source line 14 · 2026-05-16T18:56:50.088Z_

I need to extract specific experiment data from a large JSON registry file. The file is at:
/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/18137809-ea2c-4289-a326-73c48f2a7d35/tool-results/mcp-agent-ml-research-read_registry-1778957798211.txt

The file has schema: {result: string} where result is a JSON string containing experiment data.

I need you to:
1. First probe the structure (jq type, length, keys)
2. Then extract ALL experiments that are relevant to the "magnitude curve" analysis. These are experiments that involve:
   - obs_only strategy with various norm levels (0.03, 0.05, 0.10, 0.20, 0.30, and default ~1.42)
   - perdof strategy with same norm levels
   - argmin strategy experiments
   - Any multi-seed experiments (seed42, seed43, seed44, seed45, seed46)

For each relevant experiment, I need:
- exp_id
- The strategy/method (obs_only, perdof, argmin)
- The norm value used
- The seed
- Success rate (SR)
- Number of successes and total trials
- Any relevant metrics

Please output a structured summary with ALL data points organized by:
A) Magnitude curve (seed42): obs_only and perdof at each norm level
B) Seed comparison: obs_only_norm02 across seeds, argmin across seeds, perdof across seeds

Be thorough - extract every single data point. Quote exp_ids exactly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01NvDCriszJntJmm1x8xpQz3",
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "40ef9f3d-6376-40c4-af09-beb5f1609889"
}
```

</details>

---

### System

_source line 15_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a6eebf2158cc00587",
  "tool_use_id": "toolu_01NvDCriszJntJmm1x8xpQz3",
  "description": "Running Check file size",
  "usage": {
    "total_tokens": 14577,
    "tool_uses": 1,
    "duration_ms": 3206
  },
  "last_tool_name": "Bash",
  "uuid": "3bfa39cf-411e-4fd8-9a47-1d06f1e1d89f",
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35"
}
```

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Bash · `toolu_01CZ1wEQtx7hasmufnHcAhrP`</summary>

```json
{
  "command": "wc -c /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/18137809-ea2c-4289-a326-73c48f2a7d35/tool-results/mcp-agent-ml-research-read_registry-1778957798211.txt",
  "description": "Check file size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01NvDCriszJntJmm1x8xpQz3",
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "c2b65159-cb66-4a7c-978b-6041dbbcf0ce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MLspfNokrFDUzcWnKbr8nj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14516,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14516,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 58,
      "service_tier": "standard",
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

_source line 17 · 2026-05-16T18:56:53.451Z_

<details><summary>↩ Tool result · `toolu_01CZ1wEQtx7hasmufnHcAhrP`</summary>

```text
215113 /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/18137809-ea2c-4289-a326-73c48f2a7d35/tool-results/mcp-agent-ml-research-read_registry-1778957798211.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01NvDCriszJntJmm1x8xpQz3",
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "cdb8b291-cd65-4d18-a992-062317f5b838"
}
```

</details>

---

### System

_source line 18_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a6eebf2158cc00587",
  "tool_use_id": "toolu_01NvDCriszJntJmm1x8xpQz3",
  "description": "Running Probe JSON structure",
  "usage": {
    "total_tokens": 15764,
    "tool_uses": 2,
    "duration_ms": 9751
  },
  "last_tool_name": "Bash",
  "uuid": "d5977216-1073-4ab8-a361-70ffe1466ac3",
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35"
}
```

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Bash · `toolu_01W2Uzz9DUXtV1ChXerZ1MBE`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/18137809-ea2c-4289-a326-73c48f2a7d35/tool-results && cat mcp-agent-ml-research-read_registry-1778957798211.txt | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\nprint('Top-level keys:', list(raw.keys()))\nprint('Type of result:', type(raw.get('result')))\nresult_str = raw['result']\nprint('result length:', len(result_str))\n# Parse the inner JSON\ndata = json.loads(result_str)\nprint('Inner type:', type(data))\nif isinstance(data, dict):\n    print('Inner keys:', list(data.keys())[:20])\n    print('Total keys:', len(data.keys()))\nelif isinstance(data, list):\n    print('Inner length:', len(data))\n    if len(data) > 0:\n        print('First item type:', type(data[0]))\n        if isinstance(data[0], dict):\n            print('First item keys:', list(data[0].keys()))\n\"\n",
  "description": "Probe JSON structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01NvDCriszJntJmm1x8xpQz3",
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "6d855cc3-3929-42e1-ae39-a0908be29031",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CsK6e3Pzmc4nJyAQH3a1cN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1117,
      "cache_read_input_tokens": 14516,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1117,
        "ephemeral_1h_input_tokens": 0
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

_source line 20 · 2026-05-16T18:56:59.986Z_

<details><summary>↩ Tool result · `toolu_01W2Uzz9DUXtV1ChXerZ1MBE`</summary>

```text
Top-level keys: ['result']
Type of result: &lt;class 'str'>
result length: 198596
Inner type: &lt;class 'dict'>
Inner keys: ['success', 'data', 'error', 'metadata']
Total keys: 4
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01NvDCriszJntJmm1x8xpQz3",
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "547e5599-1c73-4d5d-b8ff-1aba7f5636a9"
}
```

</details>

---

### System

_source line 21_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a6eebf2158cc00587",
  "tool_use_id": "toolu_01NvDCriszJntJmm1x8xpQz3",
  "description": "Running Probe inner data structure",
  "usage": {
    "total_tokens": 16288,
    "tool_uses": 3,
    "duration_ms": 14749
  },
  "last_tool_name": "Bash",
  "uuid": "8d242e10-e2fd-4d0e-8a50-4a125ba0fb12",
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35"
}
```

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Bash · `toolu_01VriVg6YGLMxBQ2TeTEbgSJ`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/18137809-ea2c-4289-a326-73c48f2a7d35/tool-results && cat mcp-agent-ml-research-read_registry-1778957798211.txt | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\ndata = json.loads(raw['result'])\nprint('success:', data['success'])\nprint('error:', data['error'])\nprint('metadata:', data['metadata'])\ninner_data = data['data']\nprint('data type:', type(inner_data))\nif isinstance(inner_data, dict):\n    print('data keys:', list(inner_data.keys())[:30])\n    print('total data keys:', len(inner_data.keys()))\nelif isinstance(inner_data, list):\n    print('data length:', len(inner_data))\n\"\n",
  "description": "Probe inner data structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01NvDCriszJntJmm1x8xpQz3",
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "8587eed1-cae3-4ff2-868a-3e2dc692cf51",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J6NJvFA2kDuMUtKYG7AnZe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 452,
      "cache_read_input_tokens": 15633,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 452,
        "ephemeral_1h_input_tokens": 0
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

_source line 23 · 2026-05-16T18:57:04.932Z_

<details><summary>↩ Tool result · `toolu_01VriVg6YGLMxBQ2TeTEbgSJ`</summary>

```text
success: True
error: None
metadata: {'elapsed_seconds': 0.7602}
data type: &lt;class 'dict'>
data keys: ['experiments', 'count', 'total', 'baseline']
total data keys: 4
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01NvDCriszJntJmm1x8xpQz3",
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "de93ac2f-f372-4fa2-8af3-c6ff66514cfc"
}
```

</details>

---

### System

_source line 24_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a6eebf2158cc00587",
  "tool_use_id": "toolu_01NvDCriszJntJmm1x8xpQz3",
  "description": "Running Probe experiments structure",
  "usage": {
    "total_tokens": 16749,
    "tool_uses": 4,
    "duration_ms": 22046
  },
  "last_tool_name": "Bash",
  "uuid": "3f3e0ab2-bc1c-484f-a62c-b318f865ba2a",
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35"
}
```

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Bash · `toolu_012znPVXyhbHSKcjo7As5ArU`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/18137809-ea2c-4289-a326-73c48f2a7d35/tool-results && cat mcp-agent-ml-research-read_registry-1778957798211.txt | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\ndata = json.loads(raw['result'])\ninner = data['data']\nprint('count:', inner['count'])\nprint('total:', inner['total'])\nprint('baseline:', inner['baseline'])\nexps = inner['experiments']\nprint('experiments type:', type(exps))\nif isinstance(exps, list):\n    print('num experiments:', len(exps))\n    if len(exps) > 0:\n        print('first exp keys:', list(exps[0].keys()))\n        print()\n        print('First experiment:')\n        print(json.dumps(exps[0], indent=2)[:2000])\nelif isinstance(exps, dict):\n    print('num experiments:', len(exps))\n    first_key = list(exps.keys())[0]\n    print('first key:', first_key)\n    print('first value keys:', list(exps[first_key].keys()))\n\"\n",
  "description": "Probe experiments structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01NvDCriszJntJmm1x8xpQz3",
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "59713755-dce3-4f66-9ecb-febfe26fb3fb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012BGb2gJMQjWJ2gmbEpxaMN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 389,
      "cache_read_input_tokens": 16085,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 389,
        "ephemeral_1h_input_tokens": 0
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

_source line 26 · 2026-05-16T18:57:12.278Z_

<details><summary>↩ Tool result · `toolu_012znPVXyhbHSKcjo7As5ArU`</summary>

```text
count: 137
total: 137
baseline: None
experiments type: &lt;class 'dict'>
num experiments: 137
first key: eval-vla-mean-object-seed44
first value keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'server', 'gpu', 'account', 'reproduce', 'spec', 'pid', 'log_path', 'extra', 'conclusion', 'metrics', 'checkpoint_path', 'completed_at']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01NvDCriszJntJmm1x8xpQz3",
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "c00bbf1e-5925-4916-977c-5e1b7b048149"
}
```

</details>

---

### System

_source line 27_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a6eebf2158cc00587",
  "tool_use_id": "toolu_01NvDCriszJntJmm1x8xpQz3",
  "description": "Running List all experiment IDs",
  "usage": {
    "total_tokens": 17368,
    "tool_uses": 5,
    "duration_ms": 28528
  },
  "last_tool_name": "Bash",
  "uuid": "704b363e-efac-42ad-9790-9e3c8d234820",
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35"
}
```

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — Bash · `toolu_014U3wVDK3qyTExWNsSZgXeg`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/18137809-ea2c-4289-a326-73c48f2a7d35/tool-results && cat mcp-agent-ml-research-read_registry-1778957798211.txt | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\ndata = json.loads(raw['result'])\nexps = data['data']['experiments']\n\n# Print all experiment IDs\nfor k in sorted(exps.keys()):\n    print(k)\n\" | head -150\n",
  "description": "List all experiment IDs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01NvDCriszJntJmm1x8xpQz3",
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "79dc5618-8879-48bd-96c0-a2a817f2a3f4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UefVpFKgJx1YLqBL1b1sVR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 547,
      "cache_read_input_tokens": 16474,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 547,
        "ephemeral_1h_input_tokens": 0
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

_source line 29 · 2026-05-16T18:57:18.702Z_

<details><summary>↩ Tool result · `toolu_014U3wVDK3qyTExWNsSZgXeg`</summary>

```text
crm-train-a3-obs-only
crm-train-a4-scalar-unc
crm-train-k5
crm-train-v1
crm-train-v2-obs-only
crm-train-v2-perdof
crm-train-v2-scalar-unc
crm-train-v3-norm
crm-train-v3-norm-obs-only
crm-train-v3-norm-scalar-unc
crm-train-v3-obs-only
crm-train-v3-perdof
crm-train-v3-scalar-unc
eval-acr-object-obs-only-default
eval-acr-object-obs-only-norm02
eval-acr-object-v3
eval-acr-object-v4-default
eval-acr-object-v4-default-r2
eval-acr-object-v4-obs-only
eval-acr-object-v4-obs-only-b2
eval-acr-object-v4-perdof
eval-acr-object-v4-scalar
eval-acr-object-v4-scalar-b2
eval-acr-spatial-v1
eval-acr-spatial-v2
eval-acr-spatial-v3
eval-acr-spatial-v4-default
eval-acr-spatial-v4-default-r2
eval-acr-spatial-v4-default-r3
eval-acr-spatial-v4-obs-only
eval-acr-spatial-v4-obs-only-r2
eval-acr-spatial-v4-obs-only-r3
eval-acr-spatial-v4-scalar
eval-acr-spatial-v4-scalar-r2
eval-acr-spatial-v4-small
eval-acr-spatial-v4-small-r2
eval-acr-vla-spatial-v1
eval-argmin-object-seed43
eval-argmin-object-seed44
eval-argmin-object-seed44-r2
eval-argmin-object-seed44-r3
eval-argmin-only-spatial
eval-argmin-only-spatial-r2
eval-k5-spatial
eval-mag-obsonly-norm-0.3-r3
eval-mag-obsonly-norm-0p3-r3
eval-mag-obsonly-norm003
eval-mag-obsonly-norm003-b2
eval-mag-obsonly-norm003-object
eval-mag-obsonly-norm005
eval-mag-obsonly-norm005-object
eval-mag-obsonly-norm02
eval-mag-obsonly-norm02-object
eval-mag-obsonly-norm03
eval-mag-obsonly-norm03-b2
eval-mag-obsonly-norm03-b3
eval-mag-obsonly-norm03-b4
eval-mag-obsonly-norm03-object
eval-mag-obsonly-norm03-r2
eval-mag-perdof-norm003
eval-mag-perdof-norm003-object
eval-mag-perdof-norm005
eval-mag-perdof-norm005-object
eval-mag-perdof-norm02
eval-mag-perdof-norm02-object
eval-mag-perdof-norm02-seed43-object
eval-mag-perdof-norm02-seed43-object-r2
eval-mag-perdof-norm02-seed43-object-r3
eval-mag-perdof-norm03
eval-mag-perdof-norm03-object-r2
eval-mag-perdof-norm03-object-r3
eval-mag-perdof-norm0p3-object
eval-mag-perdof-norm0p3-object-r2
eval-object-v4-full
eval-object-v5-full
eval-object-v6-full
eval-object-v7-full
eval-object-v8-full
eval-obs-only-object-norm02-seed43
eval-obs-only-object-norm02-seed43-r2
eval-obs-only-object-norm02-seed44
eval-obs-only-object-norm02-seed44-r2
eval-obs-only-object-norm02-seed44-r3
eval-obs-only-object-norm02-seed44-r4
eval-obs-only-object-norm03-seed45
eval-obs-only-object-seed43
eval-obs-only-spatial
eval-obs-only-spatial-seed43
eval-obs-only-spatial-v2
eval-obs-only-spatial-v3
eval-perdof-object-seed43
eval-reconvla-object
eval-reconvla-spatial-v1
eval-reconvla-spatial-v2
eval-reconvla-spatial-v3
eval-scalar-object-seed43
eval-scalar-object-seed44
eval-scalar-unc-spatial
eval-scalar-unc-spatial-v2
eval-smolvla-libero-spatial
eval-spatial-reeval-v2
eval-spatial-v3-full
eval-spatial-v4-full
eval-spatial-v5-full
eval-spatial-v6-full
eval-spatial-v7-full
eval-tiny-correction-spatial
eval-vla-mean-object
eval-vla-mean-object-seed43
eval-vla-mean-object-seed44
eval-vla-mean-spatial
eval-vla-mean-spatial-t10
eval-vla-only-object
eval-vla-only-object-k1
eval-vla-only-object-seed43
eval-vla-only-object-seed44
eval-vla-only-object-seed44-r2
eval-vla-only-object-seed45
mvp-point-reaching
plan_001-crm-smolvla
plan_014-reconvla-baseline
precompute-k5
precompute-shard0
precompute-shard1
precompute-shard2
precompute-v2-shard0
precompute-v2-shard1
precompute-v2-shard2
precompute-v3-shard0
precompute-v3-shard1
precompute-v3-shard2
precompute-v4-shard0
precompute-v4-shard1
precompute-v4-shard2
precompute-v5-shard0
precompute-v5-shard1
precompute-v5-shard2
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01NvDCriszJntJmm1x8xpQz3",
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "b16cd24c-599a-4f5f-a484-18728a865747"
}
```

</details>

---

### System

_source line 30_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a6eebf2158cc00587",
  "tool_use_id": "toolu_01NvDCriszJntJmm1x8xpQz3",
  "description": "Running Extract magnitude curve experiments",
  "usage": {
    "total_tokens": 19234,
    "tool_uses": 6,
    "duration_ms": 37720
  },
  "last_tool_name": "Bash",
  "uuid": "875cc14c-7153-476f-96ef-ea34a1163032",
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35"
}
```

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Bash · `toolu_019LBC2eu2yYoK3egTKDRZ48`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/18137809-ea2c-4289-a326-73c48f2a7d35/tool-results && cat mcp-agent-ml-research-read_registry-1778957798211.txt | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\ndata = json.loads(raw['result'])\nexps = data['data']['experiments']\n\n# Filter relevant experiments\nrelevant_prefixes = ['eval-mag-', 'eval-obs-only-object-norm', 'eval-argmin-object-', 'eval-perdof-object-']\nrelevant_keys = []\nfor k in sorted(exps.keys()):\n    for prefix in relevant_prefixes:\n        if k.startswith(prefix):\n            relevant_keys.append(k)\n            break\n\n# Also include obs-only default and vla-only baselines for context\nfor k in sorted(exps.keys()):\n    if 'obs-only' in k and 'norm' not in k and 'object' in k:\n        if k not in relevant_keys:\n            relevant_keys.append(k)\n\nprint(f'Found {len(relevant_keys)} relevant experiments')\nprint()\nfor k in sorted(relevant_keys):\n    exp = exps[k]\n    print(f'=== {k} ===')\n    print(f'  status: {exp[\\\"status\\\"]}')\n    print(f'  metrics: {json.dumps(exp.get(\\\"metrics\\\"), indent=4)}')\n    print(f'  spec: {json.dumps(exp.get(\\\"spec\\\"), indent=4) if exp.get(\\\"spec\\\") else None}')\n    print(f'  conclusion: {exp.get(\\\"conclusion\\\", \\\"\\\")[:200]}')\n    print()\n\" 2>&1 | head -500\n",
  "description": "Extract magnitude curve experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01NvDCriszJntJmm1x8xpQz3",
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "db743fd9-1d19-4714-ac23-fdd58ff9ca10",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016xHCA32TbKc2Th8QCWLd3v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1864,
      "cache_read_input_tokens": 17021,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1864,
        "ephemeral_1h_input_tokens": 0
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

_source line 32 · 2026-05-16T18:57:27.904Z_

<details><summary>↩ Tool result · `toolu_019LBC2eu2yYoK3egTKDRZ48`</summary>

```text
Found 45 relevant experiments

=== eval-acr-object-obs-only-default ===
  status: DONE
  metrics: {
    "tasks_done": 10,
    "tasks_total": 10,
    "overall_sr": 0.17,
    "per_task_sr": {
        "alphabet_soup": 0,
        "cream_cheese": 0,
        "salad_dressing": 0.2,
        "bbq_sauce": 0.4,
        "ketchup": 0,
        "tomato_sauce": 0.1,
        "butter": 0.1,
        "milk": 0.1,
        "chocolate_pudding": 0.5,
        "orange_juice": 0.3
    }
}
  spec: {
    "command": "python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_default_norm.json",
    "server": "bjb1-32546",
    "gpu": [
        "cuda:4"
    ],
    "pid": 134094,
    "log_path": "~/runs/acr-vla-conformal-refinement/eval-acr-object-obs-only-default.log",
    "submitted_at": "2026-05-15T17:38:21.517Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "LIBERO object benchmark",
    "data_count": 100,
    "model_name": "crm_v3_norm_obs_only",
    "seed": 42,
    "checkpoint_source": "/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt",
    "eval_data": "LIBERO object benchmark",
    "wall_clock_seconds": 48640.4,
    "gpu_hours": 13.51
}
  conclusion: success

=== eval-acr-object-v4-obs-only ===
  status: DONE
  metrics: {
    "overall_sr": "19.0% (19/100)",
    "total_success": 19,
    "total_rollouts": 100,
    "mode": "obs_only",
    "benchmark": "object",
    "max_correction_norm": 0.1,
    "seed": 42,
    "K": 10,
    "tasks_done": "10/10",
    "per_task": {
        "alphabet_soup": "0%",
        "cream_cheese": "10%",
        "salad_dressing": "20%",
        "bbq_sauce": "40%",
        "ketchup": "10%",
        "tomato_sauce": "0%",
        "butter": "10%",
        "milk": "20%",
        "chocolate_pudding": "50%",
        "orange_juice": "30%"
    },
    "json_output": "/root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json"
}
  spec: {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1\"",
    "server": "bjb1-32546",
    "gpu": [
        "cuda:2"
    ],
    "pid": "13797",
    "log_path": "~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-obs-only.log",
    "submitted_at": "2026-05-15T02:53:41.526Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "wall_clock_seconds": 47312.8,
    "gpu_hours": 13.14
}
  conclusion: success

=== eval-acr-object-v4-obs-only-b2 ===
  status: DONE
  metrics: null
  spec: {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1\"",
    "server": "bjb2-28827",
    "gpu": [
        "cuda:1"
    ],
    "pid": "6746",
    "log_path": "~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-obs-only-b2.log",
    "submitted_at": "2026-05-15T02:54:59.912Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "wall_clock_seconds": 58960.3,
    "gpu_hours": 16.38
}
  conclusion: killed

=== eval-argmin-object-seed43 ===
  status: DONE
  metrics: {
    "overall_success_rate": 0.17,
    "total_successes": 17,
    "total_trials": 100,
    "per_task": {
        "alphabet_soup": 0,
        "cream_cheese": 0,
        "salad_dressing": 0.2,
        "bbq_sauce": 0.2,
        "ketchup": 0.1,
        "tomato_sauce": 0.1,
        "butter": 0.2,
        "milk": 0.3,
        "chocolate_pudding": 0.4,
        "orange_juice": 0.2
    }
}
  spec: {
    "command": "python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 43 --K 10 --output_file logs/eval_object_reconvla_seed43.json",
    "server": "bjb1-18228",
    "gpu": [
        "cuda:3"
    ],
    "pid": "356696",
    "log_path": "~/runs/acr-vla-conformal-refinement/eval-argmin-object-seed43.log",
    "submitted_at": "2026-05-15T12:00:40.708Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "LIBERO object benchmark",
    "data_count": 100,
    "model_name": "ReconVLA (reconvla baseline)",
    "seed": 43,
    "checkpoint_source": "N/A (no CRM, pure VLA baseline)",
    "eval_data": "LIBERO object benchmark (10 tasks x 10 rollouts)",
    "checkpoint_path": "N/A",
    "wall_clock_seconds": 45422.6,
    "gpu_hours": 12.62
}
  conclusion: success

=== eval-argmin-object-seed44 ===
  status: DONE
  metrics: null
  spec: {
    "data_path": "LIBERO object benchmark",
    "data_count": 100,
    "model_name": "ReconVLA (argmin baseline)",
    "seed": 44,
    "checkpoint_source": "N/A (no CRM)",
    "eval_data": "LIBERO object 10 tasks x 10 rollouts"
}
  conclusion: failed

=== eval-argmin-object-seed44-r2 ===
  status: DONE
  metrics: {
    "overall_sr": 0.13,
    "successes": 13,
    "total": 100,
    "tasks_done": 10,
    "tasks_total": 10,
    "per_task_sr": {
        "alphabet_soup": 0,
        "cream_cheese": 0,
        "salad_dressing": 0.1,
        "bbq_sauce": 0.2,
        "ketchup": 0.1,
        "tomato_sauce": 0.1,
        "butter": 0,
        "milk": 0.1,
        "chocolate_pudding": 0.5,
        "orange_juice": 0.2
    },
    "note": "EXIT_CODE=129 was SIGHUP after completion, results valid. log: logs/eval_object_reconvla_seed44.json"
}
  spec: {
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 44 --K 10 --output_file logs/eval_object_reconvla_seed44.json",
    "server": "bjb1-18228",
    "gpu": [
        "cuda:3"
    ],
    "pid": "428117",
    "seed": 44,
    "model_name": "reconvla_argmin",
    "data_path": "LIBERO object benchmark",
    "data_count": 100
}
  conclusion: success

=== eval-argmin-object-seed44-r3 ===
  status: DONE
  metrics: null
  spec: {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 44 --K 10 --output_file logs/eval_object_reconvla_seed44.json\"",
    "server": "bjb1-18228",
    "gpu": [
        "cuda:3"
    ],
    "pid": "430985",
    "log_path": "~/runs/acr-vla-conformal-refinement/eval-argmin-object-seed44-r3.log",
    "submitted_at": "2026-05-16T01:34:27.679Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "wall_clock_seconds": 12290.3,
    "gpu_hours": 3.41
}
  conclusion: killed

=== eval-mag-obsonly-norm-0.3-r3 ===
  status: DONE
  metrics: null
  spec: {
    "command": "N/A (stale duplicate entry)",
    "server": "bjb1-18228",
    "data_path": "N/A",
    "data_count": 0,
    "model_name": "N/A",
    "seed": 0,
    "checkpoint_source": "N/A",
    "eval_data": "N/A"
}
  conclusion: killed

=== eval-mag-obsonly-norm-0p3-r3 ===
  status: DONE
  metrics: null
  spec: {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_mag_obsonly_norm_0p3.json\"",
    "server": "bjb1-18228",
    "gpu": [
        "cuda:0"
    ],
    "pid": "329871",
    "log_path": "~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm-0p3-r3.log",
    "submitted_at": "2026-05-15T07:11:15.690Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "LIBERO spatial benchmark",
    "data_count": 100,
    "model_name": "crm_obs_only_v3_norm",
    "seed": 42,
    "checkpoint_source": "/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt",
    "eval_data": "LIBERO spatial (10 tasks x 10 rollouts)",
    "wall_clock_seconds": 360.6,
    "gpu_hours": 0.1
}
  conclusion: killed

=== eval-mag-obsonly-norm003 ===
  status: DONE
  metrics: null
  spec: {
    "command": "python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --max_correction_norm 0.03 --n_rollouts 10 --K 10 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_mag_obsonly_norm003.json",
    "server": "bjb2-40593",
    "gpu": [
        "cuda:0"
    ],
    "pid": 225144,
    "log_path": "~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm003-b2.log",
    "submitted_at": "2026-05-15T05:20:45Z",
    "submitted_via": "tmux (manual)",
    "backend": "tmux",
    "account": "root",
    "data_path": "LIBERO spatial benchmark",
    "data_count": "10 tasks x 10 rollouts",
    "model_name": "SmolVLA + CRM-v3-norm-obs_only",
    "seed": 42,
    "checkpoint_source": "crm-train-v3-norm-obs_only",
    "eval_data": "LIBERO spatial",
    "wall_clock_seconds": 686.0,
    "gpu_hours": 0.19
}
  conclusion: killed

=== eval-mag-obsonly-norm003-b2 ===
  status: DONE
  metrics: {
    "overall_sr_10task": 0.34,
    "tasks_done": 10,
    "tasks_total": 10,
    "per_task": {
        "between_plate_and_ramekin": 0.9,
        "next_to_ramekin": 1,
        "from_table_center": 0,
        "on_cookie_box": 0.3,
        "in_top_drawer": 0.1,
        "on_ramekin": 0,
        "next_to_cookie_box": 0.8,
        "on_stove": 0,
        "next_to_plate": 0.3,
        "on_wooden_cabinet": 0
    }
}
  spec: {
    "command": "python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_mag_obsonly_norm003.json",
    "server": "bjb2-40593",
    "gpu": [
        "cuda:0"
    ],
    "pid": "225139",
    "log_path": "~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm003-b2.log",
    "submitted_at": "2026-05-15T05:20:45.407Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "/root/autodl-tmp/libero_data/libero_spatial",
    "data_count": 10,
    "model_name": "crm_v3_norm_obs_only",
    "seed": 42,
    "checkpoint_source": "/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt",
    "eval_data": "libero_spatial",
    "wall_clock_seconds": 70039.8,
    "gpu_hours": 19.46
}
  conclusion: success

=== eval-mag-obsonly-norm003-object ===
  status: DONE
  metrics: {
    "overall_sr": 0.16,
    "tasks_done": 100,
    "tasks_total": 100,
    "per_task": {
        "pick_up_the_alphabet_soup_and_place_it_in_the_basket": 0,
        "pick_up_the_cream_cheese_and_place_it_in_the_basket": 0.2,
        "pick_up_the_salad_dressing_and_place_it_in_the_basket": 0.1,
        "pick_up_the_bbq_sauce_and_place_it_in_the_basket": 0.4,
        "pick_up_the_ketchup_and_place_it_in_the_basket": 0,
        "pick_up_the_tomato_sauce_and_place_it_in_the_basket": 0,
        "pick_up_the_butter_and_place_it_in_the_basket": 0.1,
        "pick_up_the_milk_and_place_it_in_the_basket": 0.2,
        "pick_up_the_chocolate_pudding_and_place_it_in_the_basket": 0.3,
        "pick_up_the_orange_juice_and_place_it_in_the_basket": 0.3
    }
}
  spec: {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_obs_only_norm003.json\"",
    "server": "bjb1-32546",
    "gpu": [
        "cuda:0"
    ],
    "pid": 121325,
    "log_path": "~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm003-object.log",
    "checkpoint_path": "/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt",
    "data_path": "LIBERO object benchmark",
    "data_count": 100,
    "model_name": "crm_obs_only",
    "seed": 42,
    "checkpoint_source": "/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt",
    "eval_data": "object benchmark, max_correction_norm=0.03, K=10, n_rollouts=10",
    "parent": "eval-acr-object-v4-obs-only"
}
  conclusion: success

=== eval-mag-obsonly-norm005 ===
  status: DONE
  metrics: {
    "benchmark": "spatial",
    "mode": "crm_obs_only",
    "max_correction_norm": 0.05,
    "n_rollouts": 10,
    "K": 10,
    "overall_sr": 35,
    "total_success": 35,
    "total_episodes": 100,
    "per_task": {
        "T0_between_plate_ramekin": 80,
        "T1_next_to_ramekin": 90,
        "T2_table_center": 0,
        "T3_on_cookie_box": 40,
        "T4_top_drawer": 10,
        "T5_on_ramekin": 0,
        "T6_next_to_cookie_box": 80,
        "T7_on_stove": 0,
        "T8_next_to_plate": 50,
        "T9_on_wooden_cabinet": 0
    }
}
  spec: {
    "command": "python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --max_correction_norm 0.05 --n_rollouts 10 --K 10 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_mag_obs_only_norm005.json",
    "server": "bjb2-28827",
    "data_path": "LIBERO spatial benchmark",
    "data_count": "10 tasks x 10 rollouts",
    "model_name": "SmolVLA + CRM-v3-norm-obs_only",
    "seed": 42,
    "checkpoint_source": "crm-train-v3-norm-obs_only",
    "eval_data": "LIBERO spatial"
}
  conclusion: success

=== eval-mag-obsonly-norm005-object ===
  status: DONE
  metrics: {
    "overall_sr": 0.13,
    "tasks_completed": 10,
    "total_rollouts": 100,
    "successes": 13,
    "per_task_sr": {
        "alphabet_soup": 0,
        "cream_cheese": 0,
        "salad_dressing": 0.1,
        "bbq_sauce": 0.3,
        "ketchup": 0,
        "tomato_sauce": 0.1,
        "butter": 0.1,
        "milk": 0.2,
        "chocolate_pudding": 0.2,
        "orange_juice": 0.3
    }
}
  spec: {
    "hypothesis": "Object magnitude sweep: obs_only CRM v3-norm at norm=0.05 on LIBERO object benchmark. Builds object magnitude curve alongside norm=0.1 (19%) and norm=0.2 (18% partial). Key data for fig3.",
    "parent": "eval-acr-object-v4-obs-only",
    "command": "CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_obs_only_norm005.json",
    "server": "bjb2-28827",
    "data_path": "simpler_env object benchmark",
    "data_count": 10,
    "model_name": "crm_obs_only",
    "seed": 42,
    "checkpoint_source": "/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt",
    "eval_data": "object benchmark, max_correction_norm=0.05, K=10, n_rollouts=10",
    "pid": 101610,
    "log_path": "/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005.log"
}
  conclusion: success

=== eval-mag-obsonly-norm02 ===
  status: DONE
  metrics: {
    "T0_between_plate_ramekin": 90,
    "T1_next_to_ramekin": 100,
    "T2_table_center": 0,
    "T3_on_cookie_box": 30,
    "T4_top_drawer": 10,
    "T5_on_ramekin": 0,
    "T6_next_to_cookie_box": 90,
    "T7_on_stove": 0,
    "T8_next_to_plate": 30,
    "T9_on_wooden_cabinet": 0,
    "overall_sr": 35,
    "total_success": 35,
    "total_rollouts": 100
}
  spec: {
    "command": "python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --max_correction_norm 0.2 --n_rollouts 10 --K 10 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_mag_obs_only_norm02.json",
    "server": "bjb2-28827",
    "data_path": "LIBERO spatial benchmark",
    "data_count": "10 tasks x 10 rollouts",
    "model_name": "SmolVLA + CRM-v3-norm-obs_only",
    "seed": 42,
    "checkpoint_source": "crm-train-v3-norm-obs_only",
    "eval_data": "LIBERO spatial"
}
  conclusion: negative

=== eval-mag-obsonly-norm02-object ===
  status: DONE
  metrics: null
  spec: {
    "hypothesis": "Object magnitude sweep: obs_only CRM v3-norm at norm=0.2 on LIBERO object benchmark. Fills the norm=0.2 gap in 5-point magnitude curve. Previous run reached 18% at 5/10 then stopped.",
    "parent": "eval-acr-object-v4-obs-only",
    "command": "CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_v2.json",
    "server": "bjb2-28827",
    "gpu": [
        "cuda:3"
    ],
    "pid": 141024,
    "data_path": "LIBERO object benchmark",
    "data_count": 100,
    "model_name": "crm_obs_only",
    "seed": 42,
    "checkpoint_source": "/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt",
    "eval_data": "LIBERO object benchmark",
    "checkpoint_path": "N/A (duplicate of DONE eval-acr-object-obs-only-norm02, killed to free GPU)",
    "log_path": "N/A"
}
  conclusion: killed

=== eval-mag-obsonly-norm03 ===
  status: DONE
  metrics: null
  spec: {
    "command": "python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_mag_obsonly_norm03.json",
    "server": "bjb1-18228",
    "gpu": [
        "cuda:0"
    ],
    "pid": "unknown",
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01NvDCriszJntJmm1x8xpQz3",
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "1decb284-74d2-45bf-b749-3c92a5a2dc6a"
}
```

</details>

---

### System

_source line 33_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a6eebf2158cc00587",
  "tool_use_id": "toolu_01NvDCriszJntJmm1x8xpQz3",
  "description": "Running Extract obs_only norm03, perdof, and seed experiments",
  "usage": {
    "total_tokens": 27453,
    "tool_uses": 7,
    "duration_ms": 50231
  },
  "last_tool_name": "Bash",
  "uuid": "4ba9ec40-2cc3-4ffc-9e46-1772ff0c9888",
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35"
}
```

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Bash · `toolu_012LSL6pS6VxRVR6bpVeDKBf`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/18137809-ea2c-4289-a326-73c48f2a7d35/tool-results && cat mcp-agent-ml-research-read_registry-1778957798211.txt | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\ndata = json.loads(raw['result'])\nexps = data['data']['experiments']\n\n# Continue printing the rest\nrelevant_keys = [k for k in sorted(exps.keys()) if any(p in k for p in ['eval-mag-obsonly-norm03', 'eval-mag-perdof', 'eval-obs-only-object-norm', 'eval-perdof-object', 'eval-acr-object-obs-only-norm'])]\n\nfor k in sorted(relevant_keys):\n    exp = exps[k]\n    print(f'=== {k} ===')\n    print(f'  status: {exp[\\\"status\\\"]}')\n    print(f'  metrics: {json.dumps(exp.get(\\\"metrics\\\"), indent=4)}')\n    if exp.get('spec'):\n        spec = exp['spec']\n        seed = spec.get('seed', 'N/A')\n        norm = None\n        cmd = spec.get('command', '')\n        if '--max_correction_norm' in cmd:\n            parts = cmd.split('--max_correction_norm')\n            if len(parts) > 1:\n                norm = parts[1].strip().split()[0]\n        print(f'  seed: {seed}, norm_from_cmd: {norm}')\n        print(f'  server: {spec.get(\\\"server\\\")}')\n    print(f'  conclusion: {exp.get(\\\"conclusion\\\", \\\"\\\")[:200]}')\n    print()\n\" 2>&1",
  "description": "Extract obs_only norm03, perdof, and seed experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01NvDCriszJntJmm1x8xpQz3",
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "b8b72d38-c739-4d5a-b94f-316354300c4c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Addi2dRi4iwHDXuzJ8ScZq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8184,
      "cache_read_input_tokens": 18885,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8184,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
      "service_tier": "standard",
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

_source line 35 · 2026-05-16T18:57:40.418Z_

<details><summary>↩ Tool result · `toolu_012LSL6pS6VxRVR6bpVeDKBf`</summary>

```text
=== eval-acr-object-obs-only-norm02 ===
  status: DONE
  metrics: {
    "overall_sr": 0.22,
    "total_success": 22,
    "total_rollouts": 100,
    "tasks_done": 10,
    "tasks_total": 10,
    "per_task": {
        "alphabet_soup": 0,
        "cream_cheese": 0,
        "salad_dressing": 0.3,
        "bbq_sauce": 0.4,
        "ketchup": 0.2,
        "tomato_sauce": 0.1,
        "butter": 0.1,
        "milk": 0.2,
        "chocolate_pudding": 0.6,
        "orange_juice": 0.3
    }
}
  seed: 42, norm_from_cmd: 0.2
  server: bjb1-32546
  conclusion: success

=== eval-mag-obsonly-norm03 ===
  status: DONE
  metrics: null
  seed: N/A, norm_from_cmd: 0.3
  server: bjb1-18228
  conclusion: killed

=== eval-mag-obsonly-norm03-b2 ===
  status: DONE
  metrics: null
  seed: N/A, norm_from_cmd: 0.3
  server: bjb2-28827
  conclusion: failed

=== eval-mag-obsonly-norm03-b3 ===
  status: DONE
  metrics: null
  seed: 42, norm_from_cmd: None
  server: bjb2-28827
  conclusion: killed

=== eval-mag-obsonly-norm03-b4 ===
  status: DONE
  metrics: null
  seed: 42, norm_from_cmd: None
  server: bjb2-28827
  conclusion: killed

=== eval-mag-obsonly-norm03-object ===
  status: DONE
  metrics: {
    "tasks_done": 10,
    "tasks_total": 10,
    "overall_sr": 0.19,
    "successes": 19,
    "total": 100
}
  seed: 42, norm_from_cmd: 0.3
  server: bjb2-28827
  conclusion: success

=== eval-mag-obsonly-norm03-r2 ===
  status: DONE
  metrics: {
    "bowl_between": 0.9,
    "next_to_ramekin": 1,
    "table_center": 0,
    "cookie_box": 0.3,
    "top_drawer": 0.1,
    "on_ramekin": 0,
    "next_to_cookie_box": 1,
    "stove": 0,
    "next_to_plate": 0.3,
    "wooden_cabinet": 0,
    "overall_SR": 0.36
}
  seed: 42, norm_from_cmd: 0.3
  server: bjb1-18228
  conclusion: success

=== eval-mag-perdof-norm003 ===
  status: DONE
  metrics: {
    "benchmark": "spatial",
    "mode": "acr_vla",
    "max_correction_norm": 0.03,
    "n_rollouts": 10,
    "K": 10,
    "seed": 42,
    "overall_sr": 30,
    "total_success": 30,
    "total_rollouts": 100,
    "tasks_done": "10/10",
    "per_task": {
        "T0_between_plate_ramekin": 60,
        "T1_next_to_ramekin": 100,
        "T2_table_center": 0,
        "T3_on_cookie_box": 30,
        "T4_top_drawer": 10,
        "T5_on_ramekin": 0,
        "T6_next_to_cookie_box": 80,
        "T7_on_stove": 0,
        "T8_next_to_plate": 20,
        "T9_on_wooden_cabinet": 0
    }
}
  seed: 42, norm_from_cmd: 0.03
  server: bjb2-28827
  conclusion: negative

=== eval-mag-perdof-norm003-object ===
  status: DONE
  metrics: {
    "tasks_done": 10,
    "tasks_total": 10,
    "overall_sr": 0.14,
    "per_task_sr": {
        "alphabet_soup": 0,
        "cream_cheese": 0,
        "salad_dressing": 0.2,
        "bbq_sauce": 0.2,
        "ketchup": 0.1,
        "tomato_sauce": 0.1,
        "butter": 0.2,
        "milk": 0.1,
        "chocolate_pudding": 0.4,
        "orange_juice": 0.1
    }
}
  seed: 42, norm_from_cmd: 0.03
  server: bjb2-28827
  conclusion: success

=== eval-mag-perdof-norm005 ===
  status: DONE
  metrics: {
    "T0_between_plate_ramekin": 50,
    "T1_next_to_ramekin": 100,
    "T2_table_center": 0,
    "T3_on_cookie_box": 30,
    "T4_top_drawer": 0,
    "T5_on_ramekin": 0,
    "T6_next_to_cookie_box": 100,
    "T7_on_stove": 0,
    "T8_next_to_plate": 30,
    "T9_on_wooden_cabinet": 0,
    "avg_SR_10task": 31
}
  seed: 42, norm_from_cmd: 0.05
  server: bjb2-28827
  conclusion: negative

=== eval-mag-perdof-norm005-object ===
  status: DONE
  metrics: {
    "overall_sr": 0.14,
    "successes": 14,
    "total": 100,
    "tasks_done": 10,
    "tasks_total": 10
}
  seed: 42, norm_from_cmd: 0.05
  server: bjb2-28827
  conclusion: success

=== eval-mag-perdof-norm02 ===
  status: DONE
  metrics: {
    "tasks_done": "6/10",
    "partial_results": {
        "T0_between_plate_ramekin": "60%",
        "T1_next_to_ramekin": "90%",
        "T2_table_center": "0%",
        "T3_on_cookie_box": "20%",
        "T4_top_drawer": "0%",
        "T5_on_ramekin": "0%"
    },
    "running_avg_6task": "28.3%",
    "snapshot_time": "2026-05-15T09:00:00Z",
    "server": "bjb2-28827",
    "process_status": "alive"
}
  seed: 42, norm_from_cmd: 0.2
  server: bjb2-28827
  conclusion: failed

=== eval-mag-perdof-norm02-object ===
  status: DONE
  metrics: {
    "tasks_done": 10,
    "tasks_total": 10,
    "overall_sr": 0.11,
    "per_task_sr": {
        "alphabet_soup": 0,
        "cream_cheese": 0.1,
        "salad_dressing": 0.1,
        "bbq_sauce": 0.1,
        "ketchup": 0,
        "tomato_sauce": 0,
        "butter": 0.1,
        "milk": 0.1,
        "chocolate_pudding": 0.4,
        "orange_juice": 0.2
    }
}
  seed: 42, norm_from_cmd: 0.2
  server: bjb1-32546
  conclusion: negative

=== eval-mag-perdof-norm02-seed43-object ===
  status: DONE
  metrics: null
  seed: 43, norm_from_cmd: 0.2
  server: bjb2-28827
  conclusion: killed

=== eval-mag-perdof-norm02-seed43-object-r2 ===
  status: DONE
  metrics: null
  seed: N/A, norm_from_cmd: 0.2
  server: bjb2-28827
  conclusion: killed

=== eval-mag-perdof-norm02-seed43-object-r3 ===
  status: DONE
  metrics: {
    "overall_sr": 0.09,
    "successes": 9,
    "total": 100,
    "tasks_done": 10,
    "tasks_total": 10,
    "per_task_sr": {
        "alphabet_soup": 0,
        "cream_cheese": 0,
        "salad_dressing": 0.1,
        "bbq_sauce": 0.1,
        "ketchup": 0,
        "tomato_sauce": 0,
        "butter": 0,
        "milk": 0,
        "chocolate_pudding": 0.4,
        "orange_juice": 0.3
    },
    "vs_seed42": "-2pp (11% \u2192 9%)",
    "pooled_2seed_perdof_02": "10% (20/200)"
}
  seed: 43, norm_from_cmd: 0.2
  server: bjb2-28827
  conclusion: success

=== eval-mag-perdof-norm03 ===
  status: DONE
  metrics: {
    "overall_sr_10task": 0.26,
    "T0_sr": 0.7,
    "T1_sr": 0.5,
    "T2_sr": 0.1,
    "T3_sr": 0.1,
    "T4_sr": 0,
    "T5_sr": 0,
    "T6_sr": 0.9,
    "T7_sr": 0.1,
    "T8_sr": 0.2,
    "T9_sr": 0,
    "total_successes": 26,
    "total_rollouts": 100,
    "benchmark": "spatial",
    "max_correction_norm": 0.3
}
  seed: 42, norm_from_cmd: 0.3
  server: bjb2-28827
  conclusion: negative

=== eval-mag-perdof-norm03-object-r2 ===
  status: DONE
  metrics: null
  seed: 42, norm_from_cmd: 0.3
  server: bjb2-28827
  conclusion: killed

=== eval-mag-perdof-norm03-object-r3 ===
  status: DONE
  metrics: {
    "overall_sr": 0.04,
    "successes": 4,
    "total": 100,
    "tasks_done": 10,
    "tasks_total": 10
}
  seed: 42, norm_from_cmd: 0.3
  server: bjb2-28827
  conclusion: success

=== eval-mag-perdof-norm0p3-object ===
  status: DONE
  metrics: null
  seed: N/A, norm_from_cmd: 0.3
  server: bjb1-32546
  conclusion: killed

=== eval-mag-perdof-norm0p3-object-r2 ===
  status: DONE
  metrics: null
  seed: 42, norm_from_cmd: 0.3
  server: bjb2-28827
  conclusion: killed

=== eval-obs-only-object-norm02-seed43 ===
  status: DONE
  metrics: {
    "pid": 118214,
    "gpu": 3,
    "process_status": "alive",
    "log_file": "logs/eval_object_obs_only_norm02_seed43.log"
}
  seed: 43, norm_from_cmd: 0.2
  server: bjb1-32546
  conclusion: failed

=== eval-obs-only-object-norm02-seed43-r2 ===
  status: DONE
  metrics: {
    "overall_sr": 0.16,
    "successes": 16,
    "total": 100,
    "per_task": {
        "alphabet_soup": 0,
        "cream_cheese": 0.1,
        "salad_dressing": 0.2,
        "bbq_sauce": 0.4,
        "ketchup": 0,
        "tomato_sauce": 0.1,
        "butter": 0.1,
        "milk": 0.1,
        "chocolate_pudding": 0.4,
        "orange_juice": 0.2
    },
    "vs_seed42": "-6pp (22% \u2192 16%)",
    "vs_argmin_seed43": "-1pp (17% \u2192 16%)",
    "pooled_2seed_obs_only_02": "19% (38/200)",
    "pooled_2seed_argmin": "14.5% (29/200)"
}
  seed: N/A, norm_from_cmd: None
  server: None
  conclusion: success

=== eval-obs-only-object-norm02-seed44 ===
  status: DONE
  metrics: null
  seed: 44, norm_from_cmd: None
  server: None
  conclusion: failed

=== eval-obs-only-object-norm02-seed44-r2 ===
  status: DONE
  metrics: {
    "overall_sr": 0.16,
    "per_task_sr": {
        "alphabet_soup": 0,
        "cream_cheese": 0.1,
        "salad_dressing": 0.2,
        "bbq_sauce": 0.2,
        "ketchup": 0.1,
        "tomato_sauce": 0.1,
        "butter": 0.2,
        "milk": 0.1,
        "chocolate_pudding": 0.3,
        "orange_juice": 0.3
    }
}
  seed: 44, norm_from_cmd: 0.2
  server: bjb1-18228
  conclusion: success

=== eval-obs-only-object-norm02-seed44-r3 ===
  status: DONE
  metrics: null
  seed: N/A, norm_from_cmd: 0.2
  server: bjb1-18228
  conclusion: killed

=== eval-obs-only-object-norm02-seed44-r4 ===
  status: DONE
  metrics: null
  seed: N/A, norm_from_cmd: 0.2
  server: bjb1-18228
  conclusion: killed

=== eval-obs-only-object-norm03-seed45 ===
  status: DONE
  metrics: null
  seed: 45, norm_from_cmd: 0.3
  server: bjb2-28827
  conclusion: failed

=== eval-perdof-object-seed43 ===
  status: DONE
  metrics: {
    "overall_success_rate": 0.12,
    "tasks_done": 10,
    "tasks_total": 10,
    "total_rollouts": 100,
    "total_successes": 12,
    "per_task": {
        "alphabet_soup": 0,
        "cream_cheese": 0,
        "salad_dressing": 0.2,
        "bbq_sauce": 0.3,
        "ketchup": 0,
        "tomato_sauce": 0,
        "butter": 0,
        "milk": 0,
        "chocolate_pudding": 0.4,
        "orange_juice": 0.3
    }
}
  seed: 43, norm_from_cmd: 0.1
  server: bjb1-18228
  conclusion: success
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01NvDCriszJntJmm1x8xpQz3",
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "c6912d39-5573-40a7-94db-beb5998018cf"
}
```

</details>

---

### System

_source line 36_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a6eebf2158cc00587",
  "tool_use_id": "toolu_01NvDCriszJntJmm1x8xpQz3",
  "description": "Running Extract baseline and additional seed experiments",
  "usage": {
    "total_tokens": 32258,
    "tool_uses": 8,
    "duration_ms": 66891
  },
  "last_tool_name": "Bash",
  "uuid": "89ce6196-a7da-4948-8a29-f94bed55c29c",
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35"
}
```

---

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — Bash · `toolu_012n3BoDR1B87XzkRNHrHGhB`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/18137809-ea2c-4289-a326-73c48f2a7d35/tool-results && cat mcp-agent-ml-research-read_registry-1778957798211.txt | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\ndata = json.loads(raw['result'])\nexps = data['data']['experiments']\n\n# Get obs-only default (norm ~1.42), obs-only-spatial, and any remaining seed experiments\n# Also look for eval-vla-only (baseline without CRM) and argmin-only\nrelevant_keys = ['eval-acr-object-obs-only-default', 'eval-acr-object-v4-obs-only', \n                 'eval-obs-only-spatial', 'eval-obs-only-spatial-seed43', 'eval-obs-only-spatial-v2', 'eval-obs-only-spatial-v3',\n                 'eval-obs-only-object-seed43',\n                 'eval-vla-only-object', 'eval-vla-only-object-seed43', 'eval-vla-only-object-seed44', 'eval-vla-only-object-seed44-r2', 'eval-vla-only-object-seed45',\n                 'eval-vla-only-object-k1',\n                 'eval-argmin-only-spatial', 'eval-argmin-only-spatial-r2',\n                 'eval-reconvla-object']\n\nfor k in sorted(relevant_keys):\n    if k not in exps:\n        print(f'=== {k} === NOT FOUND')\n        continue\n    exp = exps[k]\n    print(f'=== {k} ===')\n    print(f'  status: {exp[\\\"status\\\"]}')\n    print(f'  metrics: {json.dumps(exp.get(\\\"metrics\\\"), indent=4)}')\n    if exp.get('spec'):\n        spec = exp['spec']\n        seed = spec.get('seed', 'N/A')\n        norm = None\n        cmd = spec.get('command', '')\n        if '--max_correction_norm' in cmd:\n            parts = cmd.split('--max_correction_norm')\n            if len(parts) > 1:\n                norm = parts[1].strip().split()[0]\n        mode = spec.get('model_name', '')\n        print(f'  seed: {seed}, norm_from_cmd: {norm}, model: {mode}')\n    print(f'  conclusion: {exp.get(\\\"conclusion\\\", \\\"\\\")[:200]}')\n    print()\n\" 2>&1",
  "description": "Extract baseline and additional seed experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01NvDCriszJntJmm1x8xpQz3",
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "31ba775f-3e39-4f9a-a7ae-44202dcf2c82",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01No4JHFsBwf3ULhSVB7kXBZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4770,
      "cache_read_input_tokens": 27069,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4770,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
      "service_tier": "standard",
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

_source line 38 · 2026-05-16T18:57:57.068Z_

<details><summary>↩ Tool result · `toolu_012n3BoDR1B87XzkRNHrHGhB`</summary>

```text
=== eval-acr-object-obs-only-default ===
  status: DONE
  metrics: {
    "tasks_done": 10,
    "tasks_total": 10,
    "overall_sr": 0.17,
    "per_task_sr": {
        "alphabet_soup": 0,
        "cream_cheese": 0,
        "salad_dressing": 0.2,
        "bbq_sauce": 0.4,
        "ketchup": 0,
        "tomato_sauce": 0.1,
        "butter": 0.1,
        "milk": 0.1,
        "chocolate_pudding": 0.5,
        "orange_juice": 0.3
    }
}
  seed: 42, norm_from_cmd: None, model: crm_v3_norm_obs_only
  conclusion: success

=== eval-acr-object-v4-obs-only ===
  status: DONE
  metrics: {
    "overall_sr": "19.0% (19/100)",
    "total_success": 19,
    "total_rollouts": 100,
    "mode": "obs_only",
    "benchmark": "object",
    "max_correction_norm": 0.1,
    "seed": 42,
    "K": 10,
    "tasks_done": "10/10",
    "per_task": {
        "alphabet_soup": "0%",
        "cream_cheese": "10%",
        "salad_dressing": "20%",
        "bbq_sauce": "40%",
        "ketchup": "10%",
        "tomato_sauce": "0%",
        "butter": "10%",
        "milk": "20%",
        "chocolate_pudding": "50%",
        "orange_juice": "30%"
    },
    "json_output": "/root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json"
}
  seed: N/A, norm_from_cmd: 0.1", model: 
  conclusion: success

=== eval-argmin-only-spatial ===
  status: DONE
  metrics: {
    "tasks_done": "9/10",
    "partial_results": {
        "between_plate_and_ramekin": "60.0% (6/10)",
        "next_to_ramekin": "100.0% (10/10)",
        "from_table_center": "0.0% (0/10)",
        "on_cookie_box": "30.0% (3/10)",
        "in_top_drawer": "10.0% (1/10)",
        "on_ramekin": "10.0% (1/10)",
        "next_to_cookie_box": "90.0% (9/10)",
        "on_stove": "0.0% (0/10)",
        "next_to_plate": "30.0% (3/10)"
    },
    "running_avg_9tasks": "36.7% (33/90)",
    "snapshot_time": "2026-05-15T12:00:00Z",
    "server": "bjb1-18228",
    "gpu": "cuda:1",
    "pid": 231421
}
  seed: 42, norm_from_cmd: None, model: SmolVLA K=10 argmin selection (no CRM correction)
  conclusion: failed

=== eval-argmin-only-spatial-r2 ===
  status: DONE
  metrics: {
    "overall_success_rate": 0.34,
    "total_successes": 34,
    "total_trials": 100,
    "per_task": {
        "T0_between_plate_and_ramekin": 0.6,
        "T1_next_to_ramekin": 1,
        "T2_from_table_center": 0,
        "T3_on_cookie_box": 0.3,
        "T4_in_top_drawer": 0.1,
        "T5_on_ramekin": 0.1,
        "T6_next_to_cookie_box": 0.9,
        "T7_on_stove": 0,
        "T8_next_to_plate": 0.3,
        "T9_on_wooden_cabinet": 0.1
    },
    "note": "T0-T8 from original run (eval-argmin-only-spatial), T9 from r2 restart. Combined 10-task result."
}
  seed: 42, norm_from_cmd: None, model: ReconVLA argmin K=10 (restart from T9)
  conclusion: success

=== eval-obs-only-object-seed43 ===
  status: DONE
  metrics: {
    "overall_success_rate": 0.12,
    "tasks_done": 10,
    "tasks_total": 10,
    "per_task": {
        "alphabet_soup": 0,
        "cream_cheese": 0.1,
        "salad_dressing": 0.1,
        "bbq_sauce": 0.3,
        "ketchup": 0,
        "tomato_sauce": 0,
        "butter": 0,
        "milk": 0.1,
        "chocolate_pudding": 0.4,
        "orange_juice": 0.2
    },
    "vs_argmin_seed43": {
        "obs_only": 12,
        "argmin": 17,
        "diff": -5
    },
    "fisher_pooled": {
        "obs_only_total": "31/200",
        "argmin_total": "29/200",
        "pooled_obs_only_sr": 0.155,
        "pooled_argmin_sr": 0.145,
        "pooled_delta": 0.01,
        "odds_ratio": 1.08,
        "p_value_one_sided": 0.4444,
        "p_value_two_sided": 0.8888
    },
    "source": "json_file_verified_by_worker"
}
  seed: 43, norm_from_cmd: 0.1, model: crm_obs_only + SmolVLA
  conclusion: negative

=== eval-obs-only-spatial ===
  status: DONE
  metrics: {
    "error": "size mismatch: obs_only CRM net.0.weight [256,990] vs acr_vla expects [256,1030] \u2014 no crm_obs_only mode in evaluate.py"
}
  seed: 42, norm_from_cmd: None, model: CRM obs_only v2 (990D input, no conformal features)
  conclusion: failed

=== eval-obs-only-spatial-seed43 ===
  status: DONE
  metrics: null
  seed: 43, norm_from_cmd: 0.1, model: crm_v3_norm_obs_only
  conclusion: failed

=== eval-obs-only-spatial-v2 ===
  status: DONE
  metrics: null
  seed: 42, norm_from_cmd: None, model: CRM obs_only v2 (990D, no conformal features)
  conclusion: failed

=== eval-obs-only-spatial-v3 ===
  status: DONE
  metrics: null
  seed: 42, norm_from_cmd: None, model: CRM obs_only v2 (990D, no conformal features)
  conclusion: killed

=== eval-reconvla-object ===
  status: DONE
  metrics: {
    "overall_sr": 0.12,
    "per_task": {
        "alphabet_soup": 0,
        "cream_cheese": 0,
        "salad_dressing": 0.1,
        "bbq_sauce": 0.3,
        "ketchup": 0,
        "tomato_sauce": 0,
        "butter": 0.1,
        "milk": 0.1,
        "chocolate_pudding": 0.3,
        "orange_juice": 0.3
    },
    "n_rollouts": 10,
    "total_episodes": 100,
    "total_successes": 12
}
  seed: N/A, norm_from_cmd: None, model: 
  conclusion: success

=== eval-vla-only-object ===
  status: DONE
  metrics: {
    "overall_sr": 0.12,
    "total_success": 12,
    "total_trials": 100,
    "per_task": {
        "alphabet_soup": 0,
        "cream_cheese": 0.1,
        "salad_dressing": 0.2,
        "bbq_sauce": 0.2,
        "ketchup": 0,
        "tomato_sauce": 0.1,
        "butter": 0,
        "milk": 0.1,
        "chocolate_pudding": 0.2,
        "orange_juice": 0.3
    }
}
  seed: 42, norm_from_cmd: None, model: SmolVLA (VLA-only baseline)
  conclusion: success

=== eval-vla-only-object-k1 ===
  status: DONE
  metrics: null
  seed: 42, norm_from_cmd: None, model: SmolVLA (VLA-only K=1 single sample)
  conclusion: failed

=== eval-vla-only-object-seed43 ===
  status: DONE
  metrics: {
    "overall_sr": 0.12,
    "tasks_done": 10,
    "tasks_total": 10,
    "per_task_sr": {
        "alphabet_soup": 0,
        "cream_cheese": 0.1,
        "salad_dressing": 0.1,
        "bbq_sauce": 0.3,
        "ketchup": 0,
        "tomato_sauce": 0,
        "butter": 0,
        "milk": 0.1,
        "chocolate_pudding": 0.4,
        "orange_juice": 0.2
    },
    "source": "json_file_verified_by_worker"
}
  seed: 43, norm_from_cmd: None, model: vla_only
  conclusion: success

=== eval-vla-only-object-seed44 ===
  status: DONE
  metrics: null
  seed: 44, norm_from_cmd: None, model: vla_only
  conclusion: failed

=== eval-vla-only-object-seed44-r2 ===
  status: DONE
  metrics: {
    "tasks_done": 10,
    "tasks_total": 10,
    "overall_sr": 0.1,
    "per_task_sr": {
        "alphabet_soup": 0,
        "cream_cheese": 0.1,
        "salad_dressing": 0.2,
        "bbq_sauce": 0.2,
        "ketchup": 0,
        "tomato_sauce": 0,
        "butter": 0,
        "milk": 0.1,
        "chocolate_pudding": 0.2,
        "orange_juice": 0.2
    }
}
  seed: N/A, norm_from_cmd: None, model: 
  conclusion: success

=== eval-vla-only-object-seed45 ===
  status: DONE
  metrics: {
    "overall_sr": 0.09,
    "successes": 18,
    "total": 200,
    "tasks_done": 10
}
  seed: 45, norm_from_cmd: None, model: smolvla_libero
  conclusion: success
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01NvDCriszJntJmm1x8xpQz3",
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "b9e60ac4-7215-4e9e-81d8-18f8fdb242c5"
}
```

</details>

---

### System

_source line 39_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a6eebf2158cc00587",
  "tool_use_id": "toolu_01NvDCriszJntJmm1x8xpQz3",
  "description": "Running Get additional detail for specific experiments",
  "usage": {
    "total_tokens": 36125,
    "tool_uses": 9,
    "duration_ms": 75313
  },
  "last_tool_name": "Bash",
  "uuid": "d59281fa-38b4-40e1-8664-3f941252a692",
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35"
}
```

---

### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Bash · `toolu_01SEkTMjx9mEFEv9rXtYgjGK`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/18137809-ea2c-4289-a326-73c48f2a7d35/tool-results && cat mcp-agent-ml-research-read_registry-1778957798211.txt | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\ndata = json.loads(raw['result'])\nexps = data['data']['experiments']\n\n# Now get more detail on: eval-mag-obsonly-norm03-object (per_task data)\n# and the obs_only default norm (~1.42) spatial metrics\n# Also get eval-acr-object-v4-perdof for perdof norm=0.1 baseline\n# And eval-mag-perdof-norm03 spatial\nkeys_detail = ['eval-mag-obsonly-norm03-object', 'eval-acr-object-v4-perdof',\n               'eval-mag-perdof-norm03-object-r3', 'eval-mag-perdof-norm005-object',\n               'eval-vla-only-object-seed45']\n\nfor k in keys_detail:\n    if k not in exps:\n        print(f'=== {k} === NOT FOUND')\n        continue\n    exp = exps[k]\n    print(f'=== {k} ===')\n    print(f'  full entry: {json.dumps(exp, indent=2)[:3000]}')\n    print()\n\" 2>&1",
  "description": "Get additional detail for specific experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01NvDCriszJntJmm1x8xpQz3",
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "098c95f7-63c8-4be3-9171-99bfc61ebceb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01USZRs38UZtpj4wjtKLNSzY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3795,
      "cache_read_input_tokens": 31839,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3795,
        "ephemeral_1h_input_tokens": 0
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

_source line 41 · 2026-05-16T18:58:05.515Z_

<details><summary>↩ Tool result · `toolu_01SEkTMjx9mEFEv9rXtYgjGK`</summary>

```text
=== eval-mag-obsonly-norm03-object ===
  full entry: {
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-15T16:29:02.155Z",
  "updated_at": "2026-05-16T07:42:44.267Z",
  "spec": {
    "hypothesis": "Object magnitude sweep: obs_only CRM v3-norm at norm=0.3 on LIBERO object benchmark. Tests degradation at higher correction norm on object domain. Key data for fig3.",
    "parent": "eval-acr-object-v4-obs-only",
    "command": "CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03.json",
    "server": "bjb2-28827",
    "data_path": "simpler_env object benchmark",
    "data_count": 10,
    "model_name": "crm_obs_only",
    "seed": 42,
    "checkpoint_source": "/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt",
    "eval_data": "object benchmark, max_correction_norm=0.3, K=10, n_rollouts=10",
    "pid": 103028,
    "log_path": "/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03.log"
  },
  "metrics": {
    "tasks_done": 10,
    "tasks_total": 10,
    "overall_sr": 0.19,
    "successes": 19,
    "total": 100
  },
  "reproduce": {
    "finished_at": "2026-05-16T07:35:42.126Z"
  },
  "failure_reason": "",
  "conclusion": "success",
  "completed_at": "2026-05-16T07:35:43.889Z",
  "extra": {
    "hook_events": [
      {
        "event": "on_failed",
        "action": "agent",
        "ts": "2026-05-16T07:35:47.235304+00:00"
      }
    ]
  }
}

=== eval-acr-object-v4-perdof ===
  full entry: {
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-15T02:49:13.626Z",
  "updated_at": "2026-05-15T15:45:38.531Z",
  "hypothesis": "D021: ACR-VLA perdof CRM v3-norm with max_correction_norm=0.1 on LIBERO object benchmark. Cross-benchmark validation of spatial findings.",
  "spec": {
    "command": "python -u src/evaluate.py --mode acr_vla --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1",
    "server": "bjb1-32546",
    "gpu_ids": [
      "cuda:1"
    ],
    "pid": "11116",
    "data_path": "/root/autodl-tmp/libero_data/",
    "data_count": 100,
    "model_name": "ACR-VLA (CRM v3-norm perdof, max_correction_norm=0.1, object)",
    "seed": 42,
    "checkpoint_source": "/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt",
    "eval_data": "LIBERO object 10 tasks x 10 rollouts",
    "checkpoint_path": "N/A (eval-only)",
    "log_path": "~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-perdof.log"
  },
  "metrics": {
    "overall_sr": "11.0% (11/100)",
    "total_success": 11,
    "total_rollouts": 100,
    "mode": "perdof",
    "benchmark": "object",
    "max_correction_norm": 0.1,
    "seed": 42,
    "K": 10,
    "per_task": {
      "alphabet_soup": "0%",
      "cream_cheese": "0%",
      "salad_dressing": "20%",
      "bbq_sauce": "30%",
      "ketchup": "0%",
      "tomato_sauce": "0%",
      "butter": "10%",
      "milk": "0%",
      "chocolate_pudding": "20%",
      "orange_juice": "30%"
    },
    "note": "perdof object 11% vs argmin ~7% (partial). obs_only leads at ~14% (8/10). Confirms perdof not competitive on object."
  },
  "conclusion": "success",
  "completed_at": "2026-05-15T15:45:38.531Z"
}

=== eval-mag-perdof-norm03-object-r3 ===
  full entry: {
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-15T19:26:52.169Z",
  "updated_at": "2026-05-16T11:30:53.907Z",
  "spec": {
    "server": "bjb2-28827",
    "gpu": "cuda:2",
    "pid": 140759,
    "command": "python -u src/evaluate.py --mode crm_perdof --benchmark object --seed 42 --K 10 --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_r3.json",
    "data_path": "LIBERO object benchmark",
    "data_count": 100,
    "model_name": "crm_v3_norm_perdof",
    "seed": 42,
    "checkpoint_source": "/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt",
    "eval_data": "LIBERO object 10 tasks x 10 rollouts"
  },
  "metrics": {
    "overall_sr": 0.04,
    "successes": 4,
    "total": 100,
    "tasks_done": 10,
    "tasks_total": 10
  },
  "reproduce": {
    "finished_at": "2026-05-16T11:10:32.044Z"
  },
  "failure_reason": "",
  "conclusion": "success",
  "completed_at": "2026-05-16T11:10:33.866Z",
  "extra": {
    "hook_events": [
      {
        "event": "on_failed",
        "action": "agent",
        "ts": "2026-05-16T11:10:39.747200+00:00"
      }
    ]
  }
}

=== eval-mag-perdof-norm005-object ===
  full entry: {
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-15T16:56:58.178Z",
  "updated_at": "2026-05-16T08:38:02.524Z",
  "spec": {
    "hypothesis": "Object magnitude sweep: perdof CRM v3-norm at norm=0.05 on LIBERO object benchmark. Paired with obs_only norm=0.05 for magnitude comparison figure.",
    "parent": "eval-acr-object-v4-perdof",
    "command": "python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_perdof_norm005.json",
    "server": "bjb2-28827",
    "gpu": "1",
    "pid": 109650,
    "data_path": "LIBERO object benchmark",
    "data_count": 10,
    "model_name": "crm_perdof",
    "seed": 42,
    "checkpoint_source": "/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt",
    "eval_data": "LIBERO object (10 tasks x 10 rollouts)",
    "log_path": "logs/nohup_eval_object_perdof_norm005.log",
    "checkpoint_path": "/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt"
  },
  "metrics": {
    "overall_sr": 0.14,
    "successes": 14,
    "total": 100,
    "tasks_done": 10,
    "tasks_total": 10
  },
  "reproduce": {
    "finished_at": "2026-05-16T08:36:33.616Z"
  },
  "failure_reason": "",
  "conclusion": "success",
  "completed_at": "2026-05-16T08:36:35.355Z",
  "extra": {
    "hook_events": [
      {
        "event": "on_failed",
        "action": "agent",
        "ts": "2026-05-16T08:36:40.842032+00:00"
      }
    ]
  }
}

=== eval-vla-only-object-seed45 ===
  full entry: {
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-16T08:34:53.953Z",
  "updated_at": "2026-05-16T15:22:52.157Z",
  "spec": {
    "command": "CUDA_VISIBLE_DEVICES=4 python src/evaluate.py --benchmark object --mode vla_only --K 1 --seed 45 --output_file logs/eval_object_vla_only_seed45.json",
    "server": "bjb2-28827",
    "gpu_id": "cuda:4",
    "pid": 221407,
    "seed": 45,
    "model_name": "smolvla_libero",
    "data_path": "LIBERO object",
    "data_count": 10,
    "checkpoint_source": "N/A",
    "eval_data": "LIBERO object",
    "hypothesis": "VLA-only baseline K=1 seed=45 on LIBERO object. Reference for seed45 statistical comparison. seed42=12%, seed43=12%, seed44=10%."
  },
  "reproduce": {
    "finished_at": "2026-05-16T14:56:50.174Z"
  },
  "failure_reason": "process dead 5\u00d7 with no sentinel/W&B \u2014 auto-resolved as failed",
  "conclusion": "success",
  "completed_at": "2026-05-16T14:56:52.057Z",
  "extra": {
    "hook_events": [
      {
        "event": "on_failed",
        "action": "agent",
        "ts": "2026-05-16T14:56:54.606880+00:00"
      }
    ]
  },
  "metrics": {
    "overall_sr": 0.09,
    "successes": 18,
    "total": 200,
    "tasks_done": 10
  }
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01NvDCriszJntJmm1x8xpQz3",
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "31f975a8-23e8-4be6-bf46-0ec101b978c9"
}
```

</details>

---

### System

_source line 42_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a6eebf2158cc00587",
  "tool_use_id": "toolu_01NvDCriszJntJmm1x8xpQz3",
  "description": "Running Get spatial magnitude curve and argmin baselines",
  "usage": {
    "total_tokens": 39808,
    "tool_uses": 10,
    "duration_ms": 84846
  },
  "last_tool_name": "Bash",
  "uuid": "954fcf69-cb82-4d07-b118-d150ba1aa985",
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35"
}
```

---

### Tool call

_source line 43_

<details open><summary>🔧 Tool call — Bash · `toolu_01Mr7kre949Pos93w661YD6E`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/18137809-ea2c-4289-a326-73c48f2a7d35/tool-results && cat mcp-agent-ml-research-read_registry-1778957798211.txt | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\ndata = json.loads(raw['result'])\nexps = data['data']['experiments']\n\n# Get the reconvla/argmin seed42 baseline  \n# And spatial benchmark data for magnitude curve\nkeys = ['eval-reconvla-object', 'eval-vla-mean-object', 'eval-vla-mean-object-seed43', 'eval-vla-mean-object-seed44',\n        'eval-mag-obsonly-norm005', 'eval-mag-obsonly-norm003-b2', 'eval-mag-obsonly-norm02', 'eval-mag-obsonly-norm03-r2',\n        'eval-mag-perdof-norm003', 'eval-mag-perdof-norm005', 'eval-mag-perdof-norm03']\n\nfor k in keys:\n    if k not in exps:\n        print(f'=== {k} === NOT FOUND')\n        continue\n    exp = exps[k]\n    spec = exp.get('spec', {})\n    print(f'=== {k} ===')\n    print(f'  seed: {spec.get(\\\"seed\\\", \\\"N/A\\\")}')\n    cmd = spec.get('command', '')\n    norm = None\n    if '--max_correction_norm' in cmd:\n        parts = cmd.split('--max_correction_norm')\n        if len(parts) > 1:\n            norm = parts[1].strip().split()[0]\n    print(f'  norm: {norm}')\n    print(f'  metrics: {json.dumps(exp.get(\\\"metrics\\\"))}')\n    print(f'  conclusion: {exp.get(\\\"conclusion\\\")}')\n    print()\n\" 2>&1",
  "description": "Get spatial magnitude curve and argmin baselines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01NvDCriszJntJmm1x8xpQz3",
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "7df29ed5-ff3d-4fe7-a83c-f78416a735d1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XGCSts92jgbpze3Liz58nU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3611,
      "cache_read_input_tokens": 35634,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3611,
        "ephemeral_1h_input_tokens": 0
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

_source line 44 · 2026-05-16T18:58:15.035Z_

<details><summary>↩ Tool result · `toolu_01Mr7kre949Pos93w661YD6E`</summary>

```text
=== eval-reconvla-object ===
  seed: N/A
  norm: None
  metrics: {"overall_sr": 0.12, "per_task": {"alphabet_soup": 0, "cream_cheese": 0, "salad_dressing": 0.1, "bbq_sauce": 0.3, "ketchup": 0, "tomato_sauce": 0, "butter": 0.1, "milk": 0.1, "chocolate_pudding": 0.3, "orange_juice": 0.3}, "n_rollouts": 10, "total_episodes": 100, "total_successes": 12}
  conclusion: success

=== eval-vla-mean-object ===
  seed: 42
  norm: None
  metrics: {"benchmark": "object", "mode": "vla_only", "baseline_mode": "mean", "n_rollouts": 10, "K": 10, "seed": 42, "overall_sr": 12, "total_success": 12, "total_rollouts": 100, "tasks_done": "10/10", "per_task": {"alphabet_soup": 0, "cream_cheese": 0, "salad_dressing": 10, "bbq_sauce": 30, "ketchup": 10, "tomato_sauce": 10, "butter": 0, "milk": 20, "chocolate_pudding": 30, "orange_juice": 10}, "json_output": "/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean.json"}
  conclusion: success

=== eval-vla-mean-object-seed43 ===
  seed: 43
  norm: None
  metrics: {"overall_sr": 0.15, "tasks_done": 10, "tasks_total": 10, "total_success": 15, "total_rollouts": 100, "per_task": {"alphabet_soup": 0, "cream_cheese": 0, "salad_dressing": 0.2, "bbq_sauce": 0.3, "ketchup": 0.1, "tomato_sauce": 0.1, "butter": 0.1, "milk": 0.3, "chocolate_pudding": 0.3, "orange_juice": 0.1}}
  conclusion: success

=== eval-vla-mean-object-seed44 ===
  seed: N/A
  norm: None
  metrics: {"overall_sr": 0.1, "per_task_sr": {"pick_up_the_alphabet_soup_and_place_it_in_the_basket": 0, "pick_up_the_cream_cheese_and_place_it_in_the_basket": 0, "pick_up_the_salad_dressing_and_place_it_in_the_basket": 0.1, "pick_up_the_bbq_sauce_and_place_it_in_the_basket": 0.3, "pick_up_the_ketchup_and_place_it_in_the_basket": 0.1, "pick_up_the_tomato_sauce_and_place_it_in_the_basket": 0.1, "pick_up_the_butter_and_place_it_in_the_basket": 0, "pick_up_the_milk_and_place_it_in_the_basket": 0, "pick_up_the_chocolate_pudding_and_place_it_in_the_basket": 0.2, "pick_up_the_orange_juice_and_place_it_in_the_basket": 0.2}}
  conclusion: success

=== eval-mag-obsonly-norm005 ===
  seed: 42
  norm: 0.05
  metrics: {"benchmark": "spatial", "mode": "crm_obs_only", "max_correction_norm": 0.05, "n_rollouts": 10, "K": 10, "overall_sr": 35, "total_success": 35, "total_episodes": 100, "per_task": {"T0_between_plate_ramekin": 80, "T1_next_to_ramekin": 90, "T2_table_center": 0, "T3_on_cookie_box": 40, "T4_top_drawer": 10, "T5_on_ramekin": 0, "T6_next_to_cookie_box": 80, "T7_on_stove": 0, "T8_next_to_plate": 50, "T9_on_wooden_cabinet": 0}}
  conclusion: success

=== eval-mag-obsonly-norm003-b2 ===
  seed: 42
  norm: 0.03
  metrics: {"overall_sr_10task": 0.34, "tasks_done": 10, "tasks_total": 10, "per_task": {"between_plate_and_ramekin": 0.9, "next_to_ramekin": 1, "from_table_center": 0, "on_cookie_box": 0.3, "in_top_drawer": 0.1, "on_ramekin": 0, "next_to_cookie_box": 0.8, "on_stove": 0, "next_to_plate": 0.3, "on_wooden_cabinet": 0}}
  conclusion: success

=== eval-mag-obsonly-norm02 ===
  seed: 42
  norm: 0.2
  metrics: {"T0_between_plate_ramekin": 90, "T1_next_to_ramekin": 100, "T2_table_center": 0, "T3_on_cookie_box": 30, "T4_top_drawer": 10, "T5_on_ramekin": 0, "T6_next_to_cookie_box": 90, "T7_on_stove": 0, "T8_next_to_plate": 30, "T9_on_wooden_cabinet": 0, "overall_sr": 35, "total_success": 35, "total_rollouts": 100}
  conclusion: negative

=== eval-mag-obsonly-norm03-r2 ===
  seed: 42
  norm: 0.3
  metrics: {"bowl_between": 0.9, "next_to_ramekin": 1, "table_center": 0, "cookie_box": 0.3, "top_drawer": 0.1, "on_ramekin": 0, "next_to_cookie_box": 1, "stove": 0, "next_to_plate": 0.3, "wooden_cabinet": 0, "overall_SR": 0.36}
  conclusion: success

=== eval-mag-perdof-norm003 ===
  seed: 42
  norm: 0.03
  metrics: {"benchmark": "spatial", "mode": "acr_vla", "max_correction_norm": 0.03, "n_rollouts": 10, "K": 10, "seed": 42, "overall_sr": 30, "total_success": 30, "total_rollouts": 100, "tasks_done": "10/10", "per_task": {"T0_between_plate_ramekin": 60, "T1_next_to_ramekin": 100, "T2_table_center": 0, "T3_on_cookie_box": 30, "T4_top_drawer": 10, "T5_on_ramekin": 0, "T6_next_to_cookie_box": 80, "T7_on_stove": 0, "T8_next_to_plate": 20, "T9_on_wooden_cabinet": 0}}
  conclusion: negative

=== eval-mag-perdof-norm005 ===
  seed: 42
  norm: 0.05
  metrics: {"T0_between_plate_ramekin": 50, "T1_next_to_ramekin": 100, "T2_table_center": 0, "T3_on_cookie_box": 30, "T4_top_drawer": 0, "T5_on_ramekin": 0, "T6_next_to_cookie_box": 100, "T7_on_stove": 0, "T8_next_to_plate": 30, "T9_on_wooden_cabinet": 0, "avg_SR_10task": 31}
  conclusion: negative

=== eval-mag-perdof-norm03 ===
  seed: 42
  norm: 0.3
  metrics: {"overall_sr_10task": 0.26, "T0_sr": 0.7, "T1_sr": 0.5, "T2_sr": 0.1, "T3_sr": 0.1, "T4_sr": 0, "T5_sr": 0, "T6_sr": 0.9, "T7_sr": 0.1, "T8_sr": 0.2, "T9_sr": 0, "total_successes": 26, "total_rollouts": 100, "benchmark": "spatial", "max_correction_norm": 0.3}
  conclusion: negative
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01NvDCriszJntJmm1x8xpQz3",
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "08eeca66-5d37-4c46-b467-bb86710ec00c"
}
```

</details>

---

### System

_source line 45_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a6eebf2158cc00587",
  "tool_use_id": "toolu_01NvDCriszJntJmm1x8xpQz3",
  "description": "Running Get spatial v4 data for obs_only norm=0.1",
  "usage": {
    "total_tokens": 42817,
    "tool_uses": 11,
    "duration_ms": 94000
  },
  "last_tool_name": "Bash",
  "uuid": "0d891a1b-a182-4de2-a201-6dcf2b639ac9",
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35"
}
```

---

### Tool call

_source line 46_

<details open><summary>🔧 Tool call — Bash · `toolu_01FCD1Nfg6RxNDDHVp8ERQE1`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/18137809-ea2c-4289-a326-73c48f2a7d35/tool-results && cat mcp-agent-ml-research-read_registry-1778957798211.txt | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\ndata = json.loads(raw['result'])\nexps = data['data']['experiments']\n\n# Get the perdof norm=0.1 spatial and obs_only norm=0.1 spatial\n# Also need: default norm obs_only spatial, perdof spatial default, argmin spatial\nkeys = ['eval-acr-spatial-v4-obs-only', 'eval-acr-spatial-v4-default', 'eval-acr-spatial-v4-scalar',\n        'eval-acr-spatial-v4-obs-only-r2', 'eval-acr-spatial-v4-obs-only-r3',\n        'eval-acr-spatial-v4-default-r2', 'eval-acr-spatial-v4-default-r3']\n\nfor k in keys:\n    if k not in exps:\n        print(f'=== {k} === NOT FOUND')\n        continue\n    exp = exps[k]\n    spec = exp.get('spec', {})\n    print(f'=== {k} ===')\n    print(f'  seed: {spec.get(\\\"seed\\\", \\\"N/A\\\")}')\n    cmd = spec.get('command', '')\n    norm = None\n    if '--max_correction_norm' in cmd:\n        parts = cmd.split('--max_correction_norm')\n        if len(parts) > 1:\n            norm = parts[1].strip().split()[0]\n    mode = ''\n    if '--mode' in cmd:\n        parts = cmd.split('--mode')\n        if len(parts) > 1:\n            mode = parts[1].strip().split()[0]\n    print(f'  norm: {norm}, mode: {mode}')\n    print(f'  metrics: {json.dumps(exp.get(\\\"metrics\\\"))}')\n    print(f'  conclusion: {exp.get(\\\"conclusion\\\")}')\n    print()\n\" 2>&1",
  "description": "Get spatial v4 data for obs_only norm=0.1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01NvDCriszJntJmm1x8xpQz3",
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "aab5f272-5535-4344-a7ff-948d880310ad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017MFV6xDJh8yGt4CTgJNkXH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2937,
      "cache_read_input_tokens": 39245,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2937,
        "ephemeral_1h_input_tokens": 0
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

_source line 47 · 2026-05-16T18:58:24.174Z_

<details><summary>↩ Tool result · `toolu_01FCD1Nfg6RxNDDHVp8ERQE1`</summary>

```text
=== eval-acr-spatial-v4-obs-only ===
  seed: 42
  norm: None, mode: crm_obs_only
  metrics: null
  conclusion: failed

=== eval-acr-spatial-v4-default ===
  seed: 42
  norm: None, mode: acr_vla
  metrics: {"tasks_done": "0/10", "status_alert": "NO PROCESS FOUND - registry says RUNNING but no matching PID or tmux session on bjb1-18228. GPU 0 occupied by stale eval-acr-spatial-v3 tmux + crm-train-obs-only. NEEDS RESTART.", "snapshot_time": "2026-05-15T05:26Z"}
  conclusion: failed

=== eval-acr-spatial-v4-scalar ===
  seed: 42
  norm: 0.1, mode: crm_scalar
  metrics: {"tasks_done": "3/10", "partial_results": {"between_plate_and_ramekin": "60.0% (6/10)", "next_to_ramekin": "100.0% (10/10)", "from_table_center": "10.0% (1/10)"}, "running_avg_3tasks": "56.7% (17/30)", "snapshot_time": "2026-05-15T12:00:00Z", "server": "bjb1-18228", "gpu": "cuda:2", "pid": 288939}
  conclusion: failed

=== eval-acr-spatial-v4-obs-only-r2 ===
  seed: 42
  norm: 0.1", mode: crm_obs_only
  metrics: {"tasks_done": "6/10", "partial_results": {"between_plate_and_ramekin": "90.0% (9/10)", "next_to_ramekin": "100.0% (10/10)", "from_table_center": "0.0% (0/10)", "on_cookie_box": "40.0% (4/10)", "in_top_drawer": "10.0% (1/10)", "on_ramekin": "0.0% (0/10)"}, "running_avg_6tasks": "40.0% (24/60)", "snapshot_time": "2026-05-15T12:00:00Z", "server": "bjb1-18228", "gpu": "cuda:0", "pid": 270097}
  conclusion: failed

=== eval-acr-spatial-v4-obs-only-r3 ===
  seed: 42
  norm: 0.1, mode: crm_obs_only
  metrics: {"overall_sr": "35.0% (35/100)", "total_success": 35, "total_rollouts": 100, "mode": "crm_obs_only", "benchmark": "spatial", "max_correction_norm": 0.1, "seed": 42, "K": 10, "per_task": {"T0": "90%", "T1": "100%", "T2": "0%", "T3": "40%", "T4": "10%", "T5": "0%", "T6": "90%", "T7": "0%", "T8": "20%", "T9": "0%"}, "r3_subset_T6_T9": "27.5% (11/40)", "note": "D030: obs_only spatial 10-task = 35%. vs argmin 34% = +1pp. Scenario C threshold (>=39%) NOT MET. Earlier T0-T5 advantage (+5pp) wiped out by T6-T9."}
  conclusion: success

=== eval-acr-spatial-v4-default-r2 ===
  seed: N/A
  norm: None, mode: acr_vla
  metrics: null
  conclusion: killed

=== eval-acr-spatial-v4-default-r3 ===
  seed: 42
  norm: None, mode: acr_vla
  metrics: null
  conclusion: killed
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01NvDCriszJntJmm1x8xpQz3",
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "867871be-9553-4483-b106-e8427988b7a4"
}
```

</details>

---

### System

_source line 48_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a6eebf2158cc00587",
  "tool_use_id": "toolu_01NvDCriszJntJmm1x8xpQz3",
  "description": "Running Get spatial full evaluations and perdof norm02 details",
  "usage": {
    "total_tokens": 44581,
    "tool_uses": 12,
    "duration_ms": 102822
  },
  "last_tool_name": "Bash",
  "uuid": "d92de56f-5320-4b2e-a0b9-fd383b5ff411",
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35"
}
```

---

### Tool call

_source line 49_

<details open><summary>🔧 Tool call — Bash · `toolu_012a1xPQWYsoYWjuMC6JU6ZP`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/18137809-ea2c-4289-a326-73c48f2a7d35/tool-results && cat mcp-agent-ml-research-read_registry-1778957798211.txt | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\ndata = json.loads(raw['result'])\nexps = data['data']['experiments']\n\n# Get the perdof spatial norm=0.1 and norm=0.2 complete data\n# Also get eval-mag-perdof-norm02 partial spatial results\nkeys = ['eval-spatial-v4-full', 'eval-spatial-v5-full', 'eval-spatial-v6-full', 'eval-spatial-v7-full']\nfor k in keys:\n    if k not in exps:\n        print(f'=== {k} === NOT FOUND')\n        continue\n    exp = exps[k]\n    spec = exp.get('spec', {})\n    print(f'=== {k} ===')\n    cmd = spec.get('command', '')\n    mode = ''\n    if '--mode' in cmd:\n        parts = cmd.split('--mode')\n        if len(parts) > 1:\n            mode = parts[1].strip().split()[0]\n    norm = None\n    if '--max_correction_norm' in cmd:\n        parts = cmd.split('--max_correction_norm')\n        if len(parts) > 1:\n            norm = parts[1].strip().split()[0]\n    print(f'  mode: {mode}, norm: {norm}, seed: {spec.get(\\\"seed\\\")}')\n    print(f'  metrics: {json.dumps(exp.get(\\\"metrics\\\"))}')\n    print(f'  conclusion: {exp.get(\\\"conclusion\\\")}')\n    print()\n\n# Also check eval-mag-perdof-norm02 full entry for partial spatial data\nk = 'eval-mag-perdof-norm02'\nexp = exps[k]\nprint(f'=== {k} (full spec) ===')\nprint(json.dumps(exp.get('spec'), indent=2))\n\" 2>&1",
  "description": "Get spatial full evaluations and perdof norm02 details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01NvDCriszJntJmm1x8xpQz3",
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "0cd4b2ac-69a6-448f-b415-e1180eb67fee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HyPb3cG8jsKjzrD3AwAbaT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1692,
      "cache_read_input_tokens": 42182,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1692,
        "ephemeral_1h_input_tokens": 0
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

_source line 50 · 2026-05-16T18:58:33.010Z_

<details><summary>↩ Tool result · `toolu_012a1xPQWYsoYWjuMC6JU6ZP`</summary>

```text
=== eval-spatial-v4-full ===
  mode: vla_only, norm: None, seed: None
  metrics: null
  conclusion: killed

=== eval-spatial-v5-full ===
  mode: vla_only, norm: None, seed: 42
  metrics: null
  conclusion: killed

=== eval-spatial-v6-full ===
  mode: vla_only, norm: None, seed: 42
  metrics: null
  conclusion: killed

=== eval-spatial-v7-full ===
  mode: vla_only, norm: None, seed: 42
  metrics: {"overall_success_rate": 0.3, "total_successes": 30, "total_episodes": 100, "n_tasks": 10, "n_rollouts": 10, "per_task": {"pick_up_black_bowl_between_plate_and_ramekin": 0.6, "pick_up_black_bowl_next_to_ramekin": 1, "pick_up_black_bowl_from_table_center": 0, "pick_up_black_bowl_on_cookie_box": 0.2, "pick_up_black_bowl_in_top_drawer": 0, "pick_up_black_bowl_on_ramekin": 0, "pick_up_black_bowl_next_to_cookie_box": 0.9, "pick_up_black_bowl_on_stove": 0, "pick_up_black_bowl_next_to_plate": 0.3, "pick_up_black_bowl_on_wooden_cabinet": 0}}
  conclusion: success

=== eval-mag-perdof-norm02 (full spec) ===
{
  "command": "python -u src/evaluate.py --benchmark spatial --mode acr_vla --max_correction_norm 0.2 --n_rollouts 10 --K 10 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_mag_perdof_norm02.json",
  "server": "bjb2-28827",
  "data_path": "LIBERO spatial benchmark",
  "data_count": "10 tasks x 10 rollouts",
  "model_name": "SmolVLA + CRM-v3-norm-perdof",
  "seed": 42,
  "checkpoint_source": "crm-train-v3-norm-perdof",
  "eval_data": "LIBERO spatial"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01NvDCriszJntJmm1x8xpQz3",
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "d258a52b-40c7-400f-8f6e-976c5d6258cc"
}
```

</details>

---

### System

_source line 51_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a6eebf2158cc00587",
  "tool_use_id": "toolu_01NvDCriszJntJmm1x8xpQz3",
  "description": "Running Search for perdof spatial norm=0.1",
  "usage": {
    "total_tokens": 45973,
    "tool_uses": 13,
    "duration_ms": 115744
  },
  "last_tool_name": "Bash",
  "uuid": "e85e4728-ce41-42a5-98aa-310f9c0d0de5",
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35"
}
```

---

### Tool call

_source line 52_

<details open><summary>🔧 Tool call — Bash · `toolu_01UWsS8Z1SiEdTYrkyGzbTcp`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/18137809-ea2c-4289-a326-73c48f2a7d35/tool-results && cat mcp-agent-ml-research-read_registry-1778957798211.txt | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\ndata = json.loads(raw['result'])\nexps = data['data']['experiments']\n\n# Get perdof spatial norm=0.1 (should be in eval-acr-spatial-v4-default or similar perdof spatial exp)\n# Let me search for any perdof spatial at 0.1\nfor k in sorted(exps.keys()):\n    exp = exps[k]\n    spec = exp.get('spec', {})\n    cmd = spec.get('command', '')\n    if 'perdof' in cmd and 'spatial' in cmd and '0.1' in cmd and exp.get('metrics'):\n        print(f'{k}: metrics={json.dumps(exp.get(\\\"metrics\\\"))}')\n        print()\n\n# Also get the obs_only default norm spatial (should be somewhere)\nprint('--- obs_only default norm spatial ---')\nk = 'eval-acr-object-obs-only-default'\nexp = exps[k]\nspec = exp.get('spec', {})\ncmd = spec.get('command', '')\nprint(f'  command: {cmd}')\nprint()\n\n# check for perdof spatial norm=0.1\nprint('--- Searching for perdof spatial norm=0.1 with metrics ---')\nfor k in sorted(exps.keys()):\n    exp = exps[k]\n    spec = exp.get('spec', {})\n    cmd = spec.get('command', '')\n    model = spec.get('model_name', '')\n    if ('perdof' in k or 'perdof' in cmd or 'perdof' in model) and 'spatial' in (cmd + k):\n        if exp.get('metrics') and exp['status'] == 'DONE' and exp.get('conclusion') in ['success', 'negative']:\n            print(f'{k}: conclusion={exp[\\\"conclusion\\\"]} metrics={json.dumps(exp.get(\\\"metrics\\\"))}')\n            print()\n\" 2>&1",
  "description": "Search for perdof spatial norm=0.1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01NvDCriszJntJmm1x8xpQz3",
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "1aaf4159-1b3e-4724-9e2e-e49613dcb394",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019BCkeeRkn5mxe8vgANaVdM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1320,
      "cache_read_input_tokens": 43874,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1320,
        "ephemeral_1h_input_tokens": 0
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

_source line 53 · 2026-05-16T18:58:45.928Z_

<details><summary>↩ Tool result · `toolu_01UWsS8Z1SiEdTYrkyGzbTcp`</summary>

```text
eval-acr-spatial-v4-small: metrics={"tasks_done": "7/10", "partial_results": {"between_plate_and_ramekin": "60.0% (6/10)", "next_to_ramekin": "100.0% (10/10)", "from_table_center": "10.0% (1/10)", "on_cookie_box": "40.0% (4/10)", "in_top_drawer": "0.0% (0/10)", "on_ramekin": "0.0% (0/10)", "next_to_cookie_box": "90.0% (9/10)"}, "running_avg_7tasks": "42.9% (30/70)", "snapshot_time": "2026-05-15T12:00:00Z", "server": "bjb1-18228", "gpu": "cuda:3", "pid": 253085}

--- obs_only default norm spatial ---
  command: python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_default_norm.json

--- Searching for perdof spatial norm=0.1 with metrics ---
crm-train-v2-perdof: conclusion=success metrics={"best_val_loss": 0.051684, "best_epoch": 48, "total_epochs": 50, "final_train_loss": 0.076748, "comparison_vs_old": "old_6D_buggy=0.009046, new=0.051684 (loss metric changed with v2 fix)"}

eval-acr-spatial-v4-small-r2: conclusion=success metrics={"overall_sr": "35.0% (35/100)", "total_success": 35, "total_rollouts": 100, "mode": "perdof", "benchmark": "spatial", "max_correction_norm": 0.1, "seed": 42, "K": 10, "per_task": {"T0": "60%", "T1": "100%", "T2": "10%", "T3": "40%", "T4": "0%", "T5": "0%", "T6": "90%", "T7": "10%", "T8": "40%", "T9": "0%"}, "note": "D029: perdof spatial complete 10-task = 35%. vs argmin 34% = +1pp. Kill criterion triggered \u2014 per-DOF claim dead on spatial."}

eval-mag-perdof-norm003: conclusion=negative metrics={"benchmark": "spatial", "mode": "acr_vla", "max_correction_norm": 0.03, "n_rollouts": 10, "K": 10, "seed": 42, "overall_sr": 30, "total_success": 30, "total_rollouts": 100, "tasks_done": "10/10", "per_task": {"T0_between_plate_ramekin": 60, "T1_next_to_ramekin": 100, "T2_table_center": 0, "T3_on_cookie_box": 30, "T4_top_drawer": 10, "T5_on_ramekin": 0, "T6_next_to_cookie_box": 80, "T7_on_stove": 0, "T8_next_to_plate": 20, "T9_on_wooden_cabinet": 0}}

eval-mag-perdof-norm005: conclusion=negative metrics={"T0_between_plate_ramekin": 50, "T1_next_to_ramekin": 100, "T2_table_center": 0, "T3_on_cookie_box": 30, "T4_top_drawer": 0, "T5_on_ramekin": 0, "T6_next_to_cookie_box": 100, "T7_on_stove": 0, "T8_next_to_plate": 30, "T9_on_wooden_cabinet": 0, "avg_SR_10task": 31}

eval-mag-perdof-norm03: conclusion=negative metrics={"overall_sr_10task": 0.26, "T0_sr": 0.7, "T1_sr": 0.5, "T2_sr": 0.1, "T3_sr": 0.1, "T4_sr": 0, "T5_sr": 0, "T6_sr": 0.9, "T7_sr": 0.1, "T8_sr": 0.2, "T9_sr": 0, "total_successes": 26, "total_rollouts": 100, "benchmark": "spatial", "max_correction_norm": 0.3}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01NvDCriszJntJmm1x8xpQz3",
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "1da77d52-4d88-46fc-860a-cba5ff7bce6f"
}
```

</details>

---

### System

_source line 54_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a6eebf2158cc00587",
  "tool_use_id": "toolu_01NvDCriszJntJmm1x8xpQz3",
  "description": "Running Get default norm spatial obs_only and argmin spatial data",
  "usage": {
    "total_tokens": 47945,
    "tool_uses": 14,
    "duration_ms": 125363
  },
  "last_tool_name": "Bash",
  "uuid": "d42b0d5a-95c3-4cea-b1e1-a3fda8ad2cb0",
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35"
}
```

---

### Tool call

_source line 55_

<details open><summary>🔧 Tool call — Bash · `toolu_01MUf7wkMPFGGsqWyC1WLrD2`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/18137809-ea2c-4289-a326-73c48f2a7d35/tool-results && cat mcp-agent-ml-research-read_registry-1778957798211.txt | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\ndata = json.loads(raw['result'])\nexps = data['data']['experiments']\n\n# Get obs_only spatial default norm (no norm clipping)\n# This should be eval-acr-spatial-v4-obs-only series. The r3 has metrics with norm=0.1 \n# But what about the default norm (no max_correction_norm) for spatial obs_only?\n# Let's search for it\nprint('--- obs_only spatial with default/unclamped norm ---')\nfor k in sorted(exps.keys()):\n    exp = exps[k]\n    spec = exp.get('spec', {})\n    cmd = spec.get('command', '')\n    if 'obs_only' in cmd and 'spatial' in cmd and '--max_correction_norm' not in cmd:\n        if exp.get('metrics') and exp['status'] == 'DONE':\n            print(f'{k}: metrics={json.dumps(exp.get(\\\"metrics\\\"))}')\n            print()\n\n# Also look at eval-mag-perdof-norm02 for partial spatial data\nprint()\nprint('--- perdof norm=0.2 spatial (partial) ---')\nk = 'eval-mag-perdof-norm02'\nexp = exps[k]\nprint(f'{k}: metrics={json.dumps(exp.get(\\\"metrics\\\"))}')\n\n# Also get argmin-only-spatial-r2 details\nprint()\nprint('--- argmin only spatial ---')\nk = 'eval-argmin-only-spatial-r2'\nexp = exps[k]\nspec = exp.get('spec', {})\ncmd = spec.get('command', '')\nprint(f'{k}: seed={spec.get(\\\"seed\\\")}, metrics={json.dumps(exp.get(\\\"metrics\\\"))}')\n\" 2>&1",
  "description": "Get default norm spatial obs_only and argmin spatial data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01NvDCriszJntJmm1x8xpQz3",
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "64450416-e939-4f42-a3af-27f1f8da76df",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JpJj7e3baB5U2jdg5sZYKY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1900,
      "cache_read_input_tokens": 45194,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1900,
        "ephemeral_1h_input_tokens": 0
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

_source line 56 · 2026-05-16T18:58:55.539Z_

<details><summary>↩ Tool result · `toolu_01MUf7wkMPFGGsqWyC1WLrD2`</summary>

```text
--- obs_only spatial with default/unclamped norm ---
crm-train-a3-obs-only: metrics={"best_val_loss": 0.018312, "best_epoch": 4, "early_stopped_at_epoch": "~15-20", "early_stop_reason": "val_loss plateau at 0.018 for 10+ epochs (full CRM: 0.009, 2x gap confirms conformal features are critical)", "input_dim": 990, "params": 327966}

crm-train-v2-obs-only: metrics={"best_val_loss": 0.050501, "best_epoch": 50, "total_epochs": 50, "final_train_loss": 0.074839, "comparison_vs_old": "old_6D_buggy=0.018312, new=0.050501 (loss metric changed with v2 fix)"}

crm-train-v3-norm-obs-only: metrics={"best_epoch": 48, "best_val_loss": 0.01645, "final_train_loss": 0.025576, "final_val_loss": 0.01645, "total_epochs": 50}

crm-train-v3-obs-only: metrics={"invalidation_reason": "Trained on bjb2 crm_cache v4 (6D state, pre-D016). Must retrain on bjb1 crm_cache_v5 (8D state).", "original_val_loss": 1.193424}

eval-obs-only-spatial: metrics={"error": "size mismatch: obs_only CRM net.0.weight [256,990] vs acr_vla expects [256,1030] \u2014 no crm_obs_only mode in evaluate.py"}


--- perdof norm=0.2 spatial (partial) ---
eval-mag-perdof-norm02: metrics={"tasks_done": "6/10", "partial_results": {"T0_between_plate_ramekin": "60%", "T1_next_to_ramekin": "90%", "T2_table_center": "0%", "T3_on_cookie_box": "20%", "T4_top_drawer": "0%", "T5_on_ramekin": "0%"}, "running_avg_6task": "28.3%", "snapshot_time": "2026-05-15T09:00:00Z", "server": "bjb2-28827", "process_status": "alive"}

--- argmin only spatial ---
eval-argmin-only-spatial-r2: seed=42, metrics={"overall_success_rate": 0.34, "total_successes": 34, "total_trials": 100, "per_task": {"T0_between_plate_and_ramekin": 0.6, "T1_next_to_ramekin": 1, "T2_from_table_center": 0, "T3_on_cookie_box": 0.3, "T4_in_top_drawer": 0.1, "T5_on_ramekin": 0.1, "T6_next_to_cookie_box": 0.9, "T7_on_stove": 0, "T8_next_to_plate": 0.3, "T9_on_wooden_cabinet": 0.1}, "note": "T0-T8 from original run (eval-argmin-only-spatial), T9 from r2 restart. Combined 10-task result."}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01NvDCriszJntJmm1x8xpQz3",
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "e6b1c76f-3ced-4874-9132-ce1058bd63a5"
}
```

</details>

---

### System

_source line 57_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a6eebf2158cc00587",
  "tool_use_id": "toolu_01NvDCriszJntJmm1x8xpQz3",
  "description": "Running Find default norm experiments and perdof seed43 details",
  "usage": {
    "total_tokens": 49533,
    "tool_uses": 15,
    "duration_ms": 134757
  },
  "last_tool_name": "Bash",
  "uuid": "bd77a3eb-03d7-424a-ace9-0ea3d82bed9f",
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35"
}
```

---

### Tool call

_source line 58_

<details open><summary>🔧 Tool call — Bash · `toolu_01MG7DbuoFkRiTX1Yv4yg3gv`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/18137809-ea2c-4289-a326-73c48f2a7d35/tool-results && cat mcp-agent-ml-research-read_registry-1778957798211.txt | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\ndata = json.loads(raw['result'])\nexps = data['data']['experiments']\n\n# Get obs_only spatial default norm from eval-acr-object-obs-only-default - that's actually object\n# What about spatial obs_only with default (no --max_correction_norm)?\n# The r3 experiment shows 35% with norm=0.1. The default norm would be the model's natural output\n# Let's check hypothesis/extra for default norm value\n\n# Find all obs_only with 'default' in key name\nfor k in sorted(exps.keys()):\n    if 'default' in k.lower() and 'obs' in k.lower():\n        exp = exps[k]\n        print(f'{k}: status={exp[\\\"status\\\"]}, conclusion={exp.get(\\\"conclusion\\\")}, metrics={json.dumps(exp.get(\\\"metrics\\\"))}')\n        print()\n\n# Also check perdof object seed43\nk = 'eval-perdof-object-seed43'\nexp = exps[k]\nspec = exp.get('spec', {})\nprint(f'=== {k} ===')\nprint(f'  seed: {spec.get(\\\"seed\\\")}')\ncmd = spec.get('command', '')\nnorm = None\nif '--max_correction_norm' in cmd:\n    parts = cmd.split('--max_correction_norm')\n    if len(parts) > 1:\n        norm = parts[1].strip().split()[0]\nprint(f'  norm: {norm}')\nprint(f'  full metrics: {json.dumps(exp.get(\\\"metrics\\\"), indent=2)}')\nprint(f'  conclusion: {exp.get(\\\"conclusion\\\")}')\n\" 2>&1",
  "description": "Find default norm experiments and perdof seed43 details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01NvDCriszJntJmm1x8xpQz3",
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "1e43c530-556d-45cb-8cce-8b9b36169cb9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NF7TkFCfoTVvxG6GGWpyAi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1516,
      "cache_read_input_tokens": 47094,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1516,
        "ephemeral_1h_input_tokens": 0
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

_source line 59 · 2026-05-16T18:59:05.002Z_

<details><summary>↩ Tool result · `toolu_01MG7DbuoFkRiTX1Yv4yg3gv`</summary>

```text
eval-acr-object-obs-only-default: status=DONE, conclusion=success, metrics={"tasks_done": 10, "tasks_total": 10, "overall_sr": 0.17, "per_task_sr": {"alphabet_soup": 0, "cream_cheese": 0, "salad_dressing": 0.2, "bbq_sauce": 0.4, "ketchup": 0, "tomato_sauce": 0.1, "butter": 0.1, "milk": 0.1, "chocolate_pudding": 0.5, "orange_juice": 0.3}}

=== eval-perdof-object-seed43 ===
  seed: 43
  norm: 0.1
  full metrics: {
  "overall_success_rate": 0.12,
  "tasks_done": 10,
  "tasks_total": 10,
  "total_rollouts": 100,
  "total_successes": 12,
  "per_task": {
    "alphabet_soup": 0,
    "cream_cheese": 0,
    "salad_dressing": 0.2,
    "bbq_sauce": 0.3,
    "ketchup": 0,
    "tomato_sauce": 0,
    "butter": 0,
    "milk": 0,
    "chocolate_pudding": 0.4,
    "orange_juice": 0.3
  }
}
  conclusion: success
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01NvDCriszJntJmm1x8xpQz3",
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "d386600d-b37c-4b1d-a6d9-b0fe88f09b3f"
}
```

</details>

---

### System

_source line 60_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a6eebf2158cc00587",
  "tool_use_id": "toolu_01NvDCriszJntJmm1x8xpQz3",
  "status": "completed",
  "output_file": "",
  "summary": "Extract magnitude curve data from registry",
  "usage": {
    "total_tokens": 50528,
    "tool_uses": 15,
    "duration_ms": 168337
  },
  "uuid": "f2d8dec4-bb9d-4ef4-9901-c47444c6d2ca",
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35"
}
```

---

### Tool result

_source line 61 · 2026-05-16T18:59:38.428Z_

<details><summary>↩ Tool result · `toolu_01NvDCriszJntJmm1x8xpQz3`</summary>

```text
Now I have all the data. Let me compile the complete structured summary.

Here is the complete structured extraction of all magnitude curve experiment data:

---

## A) MAGNITUDE CURVE (seed=42): obs_only and perdof at each norm level

### OBJECT Benchmark (LIBERO Object, 10 tasks x 10 rollouts = 100 trials)

| Norm | obs_only exp_id | obs_only SR | perdof exp_id | perdof SR |
|------|-----------------|-------------|---------------|-----------|
| 0.03 | `eval-mag-obsonly-norm003-object` | 16% (16/100) | `eval-mag-perdof-norm003-object` | 14% (14/100) |
| 0.05 | `eval-mag-obsonly-norm005-object` | 13% (13/100) | `eval-mag-perdof-norm005-object` | 14% (14/100) |
| 0.10 | `eval-acr-object-v4-obs-only` | 19% (19/100) | `eval-acr-object-v4-perdof` | 11% (11/100) |
| 0.20 | `eval-acr-object-obs-only-norm02` | 22% (22/100) | `eval-mag-perdof-norm02-object` | 11% (11/100) |
| 0.30 | `eval-mag-obsonly-norm03-object` | 19% (19/100) | `eval-mag-perdof-norm03-object-r3` | 4% (4/100) |
| default (~1.42, no clamp) | `eval-acr-object-obs-only-default` | 17% (17/100) | -- | -- |

### SPATIAL Benchmark (LIBERO Spatial, 10 tasks x 10 rollouts = 100 trials)

| Norm | obs_only exp_id | obs_only SR | perdof exp_id | perdof SR |
|------|-----------------|-------------|---------------|-----------|
| 0.03 | `eval-mag-obsonly-norm003-b2` | 34% (34/100) | `eval-mag-perdof-norm003` | 30% (30/100) |
| 0.05 | `eval-mag-obsonly-norm005` | 35% (35/100) | `eval-mag-perdof-norm005` | 31% (31/100) |
| 0.10 | `eval-acr-spatial-v4-obs-only-r3` | 35% (35/100) | `eval-acr-spatial-v4-small-r2` | 35% (35/100) |
| 0.20 | `eval-mag-obsonly-norm02` | 35% (35/100) | `eval-mag-perdof-norm02` | ~28.3% (partial 6/10 tasks, FAILED) |
| 0.30 | `eval-mag-obsonly-norm03-r2` | 36% (36/100) | `eval-mag-perdof-norm03` | 26% (26/100) |

**Baselines (Spatial):**
- Argmin (no CRM): `eval-argmin-only-spatial-r2` = 34% (34/100), seed=42
- VLA-only (no correction): `eval-spatial-v7-full` = 30% (30/100), seed=42

---

## B) SEED COMPARISON (LIBERO Object benchmark, 100 trials each)

### obs_only norm=0.2 across seeds

| Seed | exp_id | SR | Successes/Total |
|------|--------|----|-----------------|
| 42 | `eval-acr-object-obs-only-norm02` | 22% | 22/100 |
| 43 | `eval-obs-only-object-norm02-seed43-r2` | 16% | 16/100 |
| 44 | `eval-obs-only-object-norm02-seed44-r2` | 16% | 16/100 |

Pooled 2-seed (42+43): 19% (38/200)

### obs_only norm=0.1 across seeds

| Seed | exp_id | SR | Successes/Total |
|------|--------|----|-----------------|
| 42 | `eval-acr-object-v4-obs-only` | 19% | 19/100 |
| 43 | `eval-obs-only-object-seed43` | 12% | 12/100 |

Fisher pooled (seed42+43): 15.5% (31/200)

### argmin (reconvla, no CRM) across seeds

| Seed | exp_id | SR | Successes/Total |
|------|--------|----|-----------------|
| 42 | `eval-reconvla-object` | 12% | 12/100 |
| 43 | `eval-argmin-object-seed43` | 17% | 17/100 |
| 44 | `eval-argmin-object-seed44-r2` | 13% | 13/100 |

Pooled 2-seed (42+43): 14.5% (29/200)

### perdof norm=0.1 across seeds

| Seed | exp_id | SR | Successes/Total |
|------|--------|----|-----------------|
| 42 | `eval-acr-object-v4-perdof` | 11% | 11/100 |
| 43 | `eval-perdof-object-seed43` | 12% | 12/100 |

### perdof norm=0.2 across seeds

| Seed | exp_id | SR | Successes/Total |
|------|--------|----|-----------------|
| 42 | `eval-mag-perdof-norm02-object` | 11% | 11/100 |
| 43 | `eval-mag-perdof-norm02-seed43-object-r3` | 9% | 9/100 |

Pooled 2-seed: 10% (20/200)

### VLA-only (no CRM, no correction) across seeds

| Seed | exp_id | SR | Successes/Total |
|------|--------|----|-----------------|
| 42 | `eval-vla-only-object` | 12% | 12/100 |
| 43 | `eval-vla-only-object-seed43` | 12% | 12/100 |
| 44 | `eval-vla-only-object-seed44-r2` | 10% | 10/100 |
| 45 | `eval-vla-only-object-seed45` | 9% | 18/200 |

### VLA-mean (K=10 mean selection) across seeds

| Seed | exp_id | SR | Successes/Total |
|------|--------|----|-----------------|
| 42 | `eval-vla-mean-object` | 12% | 12/100 |
| 43 | `eval-vla-mean-object-seed43` | 15% | 15/100 |
| 44 | `eval-vla-mean-object-seed44` | 10% | 10/100 |

---

## Key Observations from the Data

1. **obs_only Object magnitude curve peaks at norm=0.2** (22%) then slightly drops at norm=0.3 (19%) and default (17%).
2. **perdof Object degrades sharply at higher norms**: 14% at low norms, 11% at 0.1-0.2, catastrophic 4% at 0.3.
3. **Spatial obs_only is flat across norms** (34-36%), essentially norm-insensitive on spatial.
4. **Spatial perdof degrades at high norm**: 30-35% at low norms, drops to 26% at 0.3.
5. **obs_only norm=0.2 seed variance**: 22%, 16%, 16% across seeds (high variance, seed42 is an outlier).
6. **Failed/killed experiments** (no usable metrics): `eval-mag-obsonly-norm03` (killed), `eval-mag-obsonly-norm03-b2` (failed), `eval-mag-obsonly-norm03-b3/b4` (killed), `eval-obs-only-object-norm02-seed44-r3/r4` (killed), `eval-obs-only-object-norm03-seed45` (failed), `eval-mag-perdof-norm02-seed43-object` and `-r2` (killed).

agentId: a6eebf2158cc00587 (use SendMessage with to: 'a6eebf2158cc00587' to continue this agent)
&lt;usage>total_tokens: 51765
tool_uses: 15
duration_ms: 168339&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "28d44abc-5dd3-41db-a70a-7639a4ad58d6",
  "tool_use_result": {
    "status": "completed",
    "prompt": "I need to extract specific experiment data from a large JSON registry file. The file is at:\n/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/18137809-ea2c-4289-a326-73c48f2a7d35/tool-results/mcp-agent-ml-research-read_registry-1778957798211.txt\n\nThe file has schema: {result: string} where result is a JSON string containing experiment data.\n\nI need you to:\n1. First probe the structure (jq type, length, keys)\n2. Then extract ALL experiments that are relevant to the \"magnitude curve\" analysis. These are experiments that involve:\n   - obs_only strategy with various norm levels (0.03, 0.05, 0.10, 0.20, 0.30, and default ~1.42)\n   - perdof strategy with same norm levels\n   - argmin strategy experiments\n   - Any multi-seed experiments (seed42, seed43, seed44, seed45, seed46)\n\nFor each relevant experiment, I need:\n- exp_id\n- The strategy/method (obs_only, perdof, argmin)\n- The norm value used\n- The seed\n- Success rate (SR)\n- Number of successes and total trials\n- Any relevant metrics\n\nPlease output a structured summary with ALL data points organized by:\nA) Magnitude curve (seed42): obs_only and perdof at each norm level\nB) Seed comparison: obs_only_norm02 across seeds, argmin across seeds, perdof across seeds\n\nBe thorough - extract every single data point. Quote exp_ids exactly.",
    "agentId": "a6eebf2158cc00587",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have all the data. Let me compile the complete structured summary.\n\nHere is the complete structured extraction of all magnitude curve experiment data:\n\n---\n\n## A) MAGNITUDE CURVE (seed=42): obs_only and perdof at each norm level\n\n### OBJECT Benchmark (LIBERO Object, 10 tasks x 10 rollouts = 100 trials)\n\n| Norm | obs_only exp_id | obs_only SR | perdof exp_id | perdof SR |\n|------|-----------------|-------------|---------------|-----------|\n| 0.03 | `eval-mag-obsonly-norm003-object` | 16% (16/100) | `eval-mag-perdof-norm003-object` | 14% (14/100) |\n| 0.05 | `eval-mag-obsonly-norm005-object` | 13% (13/100) | `eval-mag-perdof-norm005-object` | 14% (14/100) |\n| 0.10 | `eval-acr-object-v4-obs-only` | 19% (19/100) | `eval-acr-object-v4-perdof` | 11% (11/100) |\n| 0.20 | `eval-acr-object-obs-only-norm02` | 22% (22/100) | `eval-mag-perdof-norm02-object` | 11% (11/100) |\n| 0.30 | `eval-mag-obsonly-norm03-object` | 19% (19/100) | `eval-mag-perdof-norm03-object-r3` | 4% (4/100) |\n| default (~1.42, no clamp) | `eval-acr-object-obs-only-default` | 17% (17/100) | -- | -- |\n\n### SPATIAL Benchmark (LIBERO Spatial, 10 tasks x 10 rollouts = 100 trials)\n\n| Norm | obs_only exp_id | obs_only SR | perdof exp_id | perdof SR |\n|------|-----------------|-------------|---------------|-----------|\n| 0.03 | `eval-mag-obsonly-norm003-b2` | 34% (34/100) | `eval-mag-perdof-norm003` | 30% (30/100) |\n| 0.05 | `eval-mag-obsonly-norm005` | 35% (35/100) | `eval-mag-perdof-norm005` | 31% (31/100) |\n| 0.10 | `eval-acr-spatial-v4-obs-only-r3` | 35% (35/100) | `eval-acr-spatial-v4-small-r2` | 35% (35/100) |\n| 0.20 | `eval-mag-obsonly-norm02` | 35% (35/100) | `eval-mag-perdof-norm02` | ~28.3% (partial 6/10 tasks, FAILED) |\n| 0.30 | `eval-mag-obsonly-norm03-r2` | 36% (36/100) | `eval-mag-perdof-norm03` | 26% (26/100) |\n\n**Baselines (Spatial):**\n- Argmin (no CRM): `eval-argmin-only-spatial-r2` = 34% (34/100), seed=42\n- VLA-only (no correction): `eval-spatial-v7-full` = 30% (30/100), seed=42\n\n---\n\n## B) SEED COMPARISON (LIBERO Object benchmark, 100 trials each)\n\n### obs_only norm=0.2 across seeds\n\n| Seed | exp_id | SR | Successes/Total |\n|------|--------|----|-----------------|\n| 42 | `eval-acr-object-obs-only-norm02` | 22% | 22/100 |\n| 43 | `eval-obs-only-object-norm02-seed43-r2` | 16% | 16/100 |\n| 44 | `eval-obs-only-object-norm02-seed44-r2` | 16% | 16/100 |\n\nPooled 2-seed (42+43): 19% (38/200)\n\n### obs_only norm=0.1 across seeds\n\n| Seed | exp_id | SR | Successes/Total |\n|------|--------|----|-----------------|\n| 42 | `eval-acr-object-v4-obs-only` | 19% | 19/100 |\n| 43 | `eval-obs-only-object-seed43` | 12% | 12/100 |\n\nFisher pooled (seed42+43): 15.5% (31/200)\n\n### argmin (reconvla, no CRM) across seeds\n\n| Seed | exp_id | SR | Successes/Total |\n|------|--------|----|-----------------|\n| 42 | `eval-reconvla-object` | 12% | 12/100 |\n| 43 | `eval-argmin-object-seed43` | 17% | 17/100 |\n| 44 | `eval-argmin-object-seed44-r2` | 13% | 13/100 |\n\nPooled 2-seed (42+43): 14.5% (29/200)\n\n### perdof norm=0.1 across seeds\n\n| Seed | exp_id | SR | Successes/Total |\n|------|--------|----|-----------------|\n| 42 | `eval-acr-object-v4-perdof` | 11% | 11/100 |\n| 43 | `eval-perdof-object-seed43` | 12% | 12/100 |\n\n### perdof norm=0.2 across seeds\n\n| Seed | exp_id | SR | Successes/Total |\n|------|--------|----|-----------------|\n| 42 | `eval-mag-perdof-norm02-object` | 11% | 11/100 |\n| 43 | `eval-mag-perdof-norm02-seed43-object-r3` | 9% | 9/100 |\n\nPooled 2-seed: 10% (20/200)\n\n### VLA-only (no CRM, no correction) across seeds\n\n| Seed | exp_id | SR | Successes/Total |\n|------|--------|----|-----------------|\n| 42 | `eval-vla-only-object` | 12% | 12/100 |\n| 43 | `eval-vla-only-object-seed43` | 12% | 12/100 |\n| 44 | `eval-vla-only-object-seed44-r2` | 10% | 10/100 |\n| 45 | `eval-vla-only-object-seed45` | 9% | 18/200 |\n\n### VLA-mean (K=10 mean selection) across seeds\n\n| Seed | exp_id | SR | Successes/Total |\n|------|--------|----|-----------------|\n| 42 | `eval-vla-mean-object` | 12% | 12/100 |\n| 43 | `eval-vla-mean-object-seed43` | 15% | 15/100 |\n| 44 | `eval-vla-mean-object-seed44` | 10% | 10/100 |\n\n---\n\n## Key Observations from the Data\n\n1. **obs_only Object magnitude curve peaks at norm=0.2** (22%) then slightly drops at norm=0.3 (19%) and default (17%).\n2. **perdof Object degrades sharply at higher norms**: 14% at low norms, 11% at 0.1-0.2, catastrophic 4% at 0.3.\n3. **Spatial obs_only is flat across norms** (34-36%), essentially norm-insensitive on spatial.\n4. **Spatial perdof degrades at high norm**: 30-35% at low norms, drops to 26% at 0.3.\n5. **obs_only norm=0.2 seed variance**: 22%, 16%, 16% across seeds (high variance, seed42 is an outlier).\n6. **Failed/killed experiments** (no usable metrics): `eval-mag-obsonly-norm03` (killed), `eval-mag-obsonly-norm03-b2` (failed), `eval-mag-obsonly-norm03-b3/b4` (killed), `eval-obs-only-object-norm02-seed44-r3/r4` (killed), `eval-obs-only-object-norm03-seed45` (failed), `eval-mag-perdof-norm02-seed43-object` and `-r2` (killed)."
      }
    ],
    "totalDurationMs": 168339,
    "totalTokens": 51765,
    "totalToolUseCount": 15,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 994,
      "cache_read_input_tokens": 48610,
      "output_tokens": 2160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 994
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2160,
          "cache_read_input_tokens": 48610,
          "cache_creation_input_tokens": 994,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 994,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 15,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
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
Excellent! Now I have all the data. Let me also check if there's a "default" perdof entry. The data shows "--" for perdof at default norm. Let me also check the note about perdof default. It seems like there's no perdof default experiment. The user's table shows perdof default = 0%, let me check if there's data for that.

Looking at the user's table:
| default(~1.42) | 17% | 0% |

So perdof at default should be 0%. Let me check if there's an experiment for that. The agent didn't find one with exp_id. Let me check for a perdof default experiment.


Actually, looking more carefully at the task description, the user provided obs_only default = 17% and perdof default = 0%, and I found the obs_only experiment in the registry, but the perdof default experiment might not be there yet. The user also mentioned seed45/46 are about to complete, so those may not be in the registry yet. Let me proceed with what I have and look for the perdof default experiment.

Since the user's table shows 0%, there must be an experiment for it somewhere. Let me query for it specifically.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "fd35b3ac-5f1e-46cb-9f62-e5562f35217e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xrwu9AGkkAS9krvdfvqarn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2762,
      "cache_read_input_tokens": 25837,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2762
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

_source line 63_

Good data. Let me check for the perdof default experiment that the user's table shows as 0%.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "d4cf3125-f2d4-44fb-87c8-466926c60adc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xrwu9AGkkAS9krvdfvqarn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2762,
      "cache_read_input_tokens": 25837,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2762
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

_source line 64_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01YBEnn3JL3yckqBEHNT8JNy`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": {
    "status": "DONE"
  },
  "limit": 0,
  "fields": [
    "exp_id",
    "metrics",
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
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "97319039-6702-4c4d-8730-5318daf4210c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xrwu9AGkkAS9krvdfvqarn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2762,
      "cache_read_input_tokens": 25837,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2762
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

_source line 65 · 2026-05-16T18:59:49.873Z_

<details><summary>↩ Tool result · `toolu_01YBEnn3JL3yckqBEHNT8JNy`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-vla-mean-object-seed44\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.1, \"per_task_sr\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.1, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.3, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0.1, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0.1, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 0, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.2, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.2}}}, \"eval-obs-only-object-norm02-seed44-r4\": {\"conclusion\": \"killed\"}, \"eval-argmin-object-seed44-r2\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.13, \"successes\": 13, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.5, \"orange_juice\": 0.2}, \"note\": \"EXIT_CODE=129 was SIGHUP after completion, results valid. log: logs/eval_object_reconvla_seed44.json\"}}, \"eval-obs-only-object-norm02-seed44-r2\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.16, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}}, \"eval-vla-only-object-seed45\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.09, \"successes\": 18, \"total\": 200, \"tasks_done\": 10}}, \"eval-obs-only-object-norm03-seed45\": {\"conclusion\": \"failed\"}, \"eval-mag-perdof-norm03-object-r3\": {\"metrics\": {\"overall_sr\": 0.04, \"successes\": 4, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10}, \"conclusion\": \"success\"}, \"eval-mag-perdof-norm02-seed43-object-r3\": {\"metrics\": {\"overall_sr\": 0.09, \"successes\": 9, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}, \"vs_seed42\": \"-2pp (11% → 9%)\", \"pooled_2seed_perdof_02\": \"10% (20/200)\"}, \"conclusion\": \"success\"}, \"eval-acr-object-v4-default-r2\": {\"metrics\": {\"overall_sr\": 0, \"successes\": 0, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0, \"bbq_sauce\": 0, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0, \"orange_juice\": 0}, \"note\": \"actual mode=crm_perdof with default norm (~1.42), NOT crm_default. Confirms catastrophic failure at uncontrolled correction magnitude.\"}, \"conclusion\": \"success\"}, \"eval-mag-perdof-norm005-object\": {\"metrics\": {\"overall_sr\": 0.14, \"successes\": 14, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10}, \"conclusion\": \"success\"}, \"eval-mag-perdof-norm003-object\": {\"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.14, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.1}}, \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm005-object\": {\"metrics\": {\"overall_sr\": 0.13, \"tasks_completed\": 10, \"total_rollouts\": 100, \"successes\": 13, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed43-r2\": {\"metrics\": {\"overall_sr\": 0.16, \"successes\": 16, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}, \"vs_seed42\": \"-6pp (22% → 16%)\", \"vs_argmin_seed43\": \"-1pp (17% → 16%)\", \"pooled_2seed_obs_only_02\": \"19% (38/200)\", \"pooled_2seed_argmin\": \"14.5% (29/200)\"}, \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm03-object\": {\"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.19, \"successes\": 19, \"total\": 100}, \"conclusion\": \"success\"}, \"eval-vla-only-object-seed44-r2\": {\"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.1, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}, \"conclusion\": \"success\"}, \"eval-mag-perdof-norm02-object\": {\"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.11, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}, \"conclusion\": \"negative\"}, \"eval-acr-object-obs-only-default\": {\"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.17, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.5, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-scalar-object-seed43\": {\"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"avg_sr\": 10, \"per_task_sr\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 30, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 10, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 30, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 30}}, \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm003-object\": {\"metrics\": {\"overall_sr\": 0.16, \"tasks_done\": 100, \"tasks_total\": 100, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0.2, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.1, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.4, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_butter_and_place_it_in_the_basket\": 0.1, \"pick_up_the_milk_and_place_it_in_the_basket\": 0.2, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.3, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.3}}, \"conclusion\": \"success\"}, \"eval-scalar-object-seed44\": {\"conclusion\": \"failed\"}, \"eval-obs-only-object-norm02-seed44-r3\": {\"conclusion\": \"killed\"}, \"eval-argmin-object-seed44-r3\": {\"conclusion\": \"killed\"}, \"eval-vla-mean-object-seed43\": {\"metrics\": {\"overall_sr\": 0.15, \"tasks_done\": 10, \"tasks_total\": 10, \"total_success\": 15, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.3, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.1}}, \"conclusion\": \"success\"}, \"eval-perdof-object-seed43\": {\"metrics\": {\"overall_success_rate\": 0.12, \"tasks_done\": 10, \"tasks_total\": 10, \"total_rollouts\": 100, \"total_successes\": 12, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-vla-only-object-seed44\": {\"conclusion\": \"failed\"}, \"eval-obs-only-object-norm02-seed44\": {\"conclusion\": \"failed\"}, \"eval-argmin-object-seed44\": {\"conclusion\": \"failed\"}, \"eval-obs-only-object-seed43\": {\"metrics\": {\"overall_success_rate\": 0.12, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}, \"vs_argmin_seed43\": {\"obs_only\": 12, \"argmin\": 17, \"diff\": -5}, \"fisher_pooled\": {\"obs_only_total\": \"31/200\", \"argmin_total\": \"29/200\", \"pooled_obs_only_sr\": 0.155, \"pooled_argmin_sr\": 0.145, \"pooled_delta\": 0.01, \"odds_ratio\": 1.08, \"p_value_one_sided\": 0.4444, \"p_value_two_sided\": 0.8888}, \"source\": \"json_file_verified_by_worker\"}, \"conclusion\": \"negative\"}, \"eval-mag-obsonly-norm003-b2\": {\"metrics\": {\"overall_sr_10task\": 0.34, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task\": {\"between_plate_and_ramekin\": 0.9, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.8, \"on_stove\": 0, \"next_to_plate\": 0.3, \"on_wooden_cabinet\": 0}}, \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm03-b2\": {\"conclusion\": \"failed\"}, \"eval-argmin-object-seed43\": {\"metrics\": {\"overall_success_rate\": 0.17, \"total_successes\": 17, \"total_trials\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.3, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}, \"conclusion\": \"success\"}, \"eval-mag-perdof-norm02-seed43-object-r2\": {\"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm03\": {\"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm02-object\": {\"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm03-b4\": {\"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm03-b3\": {\"conclusion\": \"killed\"}, \"eval-mag-perdof-norm02-seed43-object\": {\"conclusion\": \"killed\"}, \"eval-mag-perdof-norm03-object-r2\": {\"conclusion\": \"killed\"}, \"eval-acr-object-v4-scalar-b2\": {\"conclusion\": \"killed\"}, \"eval-acr-object-v4-obs-only-b2\": {\"conclusion\": \"killed\"}, \"eval-spatial-v4-full\": {\"conclusion\": \"killed\"}, \"eval-reconvla-spatial-v1\": {\"conclusion\": \"killed\"}, \"eval-object-v6-full\": {\"conclusion\": \"killed\"}, \"precompute-v4-shard2\": {\"conclusion\": \"success\"}, \"precompute-v4-shard1\": {\"conclusion\": \"success\"}, \"precompute-v4-shard0\": {\"conclusion\": \"success\"}, \"precompute-v3-shard2\": {\"conclusion\": \"killed\"}, \"precompute-v3-shard1\": {\"conclusion\": \"killed\"}, \"precompute-v3-shard0\": {\"conclusion\": \"killed\"}, \"precompute-v2-shard2\": {\"conclusion\": \"killed\"}, \"precompute-v2-shard1\": {\"conclusion\": \"killed\"}, \"precompute-v2-shard0\": {\"conclusion\": \"killed\"}, \"eval-mag-perdof-norm0p3-object-r2\": {\"conclusion\": \"killed\"}, \"eval-vla-only-object-seed43\": {\"metrics\": {\"overall_sr\": 0.12, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}, \"source\": \"json_file_verified_by_worker\"}, \"conclusion\": \"success\"}, \"eval-mag-perdof-norm0p3-object\": {\"conclusion\": \"killed\"}, \"eval-obs-only-object-norm02-seed43\": {\"metrics\": {\"pid\": 118214, \"gpu\": 3, \"process_status\": \"alive\", \"log_file\": \"logs/eval_object_obs_only_norm02_seed43.log\"}, \"conclusion\": \"failed\"}, \"eval-acr-object-v4-default\": {\"metrics\": {\"tasks_done\": 3, \"tasks_total\": 10, \"status\": \"DEAD\", \"partial_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0}, \"pid_42311\": \"not_found\", \"needs_restart\": true, \"checked_at\": \"2026-05-16T01:00Z\"}, \"conclusion\": \"killed\"}, \"eval-acr-object-obs-only-norm02\": {\"metrics\": {\"overall_sr\": 0.22, \"total_success\": 22, \"total_rollouts\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.4, \"ketchup\": 0.2, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.6, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-mag-perdof-norm02\": {\"metrics\": {\"tasks_done\": \"6/10\", \"partial_results\": {\"T0_between_plate_ramekin\": \"60%\", \"T1_next_to_ramekin\": \"90%\", \"T2_table_center\": \"0%\", \"T3_on_cookie_box\": \"20%\", \"T4_top_drawer\": \"0%\", \"T5_on_ramekin\": \"0%\"}, \"running_avg_6task\": \"28.3%\", \"snapshot_time\": \"2026-05-15T09:00:00Z\", \"server\": \"bjb2-28827\", \"process_status\": \"alive\"}, \"conclusion\": \"failed\"}, \"eval-mag-perdof-norm005\": {\"metrics\": {\"T0_between_plate_ramekin\": 50, \"T1_next_to_ramekin\": 100, \"T2_table_center\": 0, \"T3_on_cookie_box\": 30, \"T4_top_drawer\": 0, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 100, \"T7_on_stove\": 0, \"T8_next_to_plate\": 30, \"T9_on_wooden_cabinet\": 0, \"avg_SR_10task\": 31}, \"conclusion\": \"negative\"}, \"eval-mag-obsonly-norm03-r2\": {\"metrics\": {\"bowl_between\": 0.9, \"next_to_ramekin\": 1, \"table_center\": 0, \"cookie_box\": 0.3, \"top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"stove\": 0, \"next_to_plate\": 0.3, \"wooden_cabinet\": 0, \"overall_SR\": 0.36}, \"conclusion\": \"success\"}, \"eval-mag-perdof-norm03\": {\"metrics\": {\"overall_sr_10task\": 0.26, \"T0_sr\": 0.7, \"T1_sr\": 0.5, \"T2_sr\": 0.1, \"T3_sr\": 0.1, \"T4_sr\": 0, \"T5_sr\": 0, \"T6_sr\": 0.9, \"T7_sr\": 0.1, \"T8_sr\": 0.2, \"T9_sr\": 0, \"total_successes\": 26, \"total_rollouts\": 100, \"benchmark\": \"spatial\", \"max_correction_norm\": 0.3}, \"conclusion\": \"negative\"}, \"eval-vla-mean-object\": {\"metrics\": {\"benchmark\": \"object\", \"mode\": \"vla_only\", \"baseline_mode\": \"mean\", \"n_rollouts\": 10, \"K\": 10, \"seed\": 42, \"overall_sr\": 12, \"total_success\": 12, \"total_rollouts\": 100, \"tasks_done\": \"10/10\", \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 10, \"bbq_sauce\": 30, \"ketchup\": 10, \"tomato_sauce\": 10, \"butter\": 0, \"milk\": 20, \"chocolate_pudding\": 30, \"orange_juice\": 10}, \"json_output\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean.json\"}, \"conclusion\": \"success\"}, \"eval-mag-perdof-norm003\": {\"metrics\": {\"benchmark\": \"spatial\", \"mode\": \"acr_vla\", \"max_correction_norm\": 0.03, \"n_rollouts\": 10, \"K\": 10, \"seed\": 42, \"overall_sr\": 30, \"total_success\": 30, \"total_rollouts\": 100, \"tasks_done\": \"10/10\", \"per_task\": {\"T0_between_plate_ramekin\": 60, \"T1_next_to_ramekin\": 100, \"T2_table_center\": 0, \"T3_on_cookie_box\": 30, \"T4_top_drawer\": 10, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 80, \"T7_on_stove\": 0, \"T8_next_to_plate\": 20, \"T9_on_wooden_cabinet\": 0}}, \"conclusion\": \"negative\"}, \"eval-reconvla-object\": {\"metrics\": {\"overall_sr\": 0.12, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}, \"n_rollouts\": 10, \"total_episodes\": 100, \"total_successes\": 12}, \"conclusion\": \"success\"}, \"eval-acr-object-v4-obs-only\": {\"metrics\": {\"overall_sr\": \"19.0% (19/100)\", \"total_success\": 19, \"total_rollouts\": 100, \"mode\": \"obs_only\", \"benchmark\": \"object\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"tasks_done\": \"10/10\", \"per_task\": {\"alphabet_soup\": \"0%\", \"cream_cheese\": \"10%\", \"salad_dressing\": \"20%\", \"bbq_sauce\": \"40%\", \"ketchup\": \"10%\", \"tomato_sauce\": \"0%\", \"butter\": \"10%\", \"milk\": \"20%\", \"chocolate_pudding\": \"50%\", \"orange_juice\": \"30%\"}, \"json_output\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json\"}, \"conclusion\": \"success\"}, \"eval-acr-object-v4-scalar\": {\"metrics\": {\"overall_sr\": 9, \"total_success\": 9, \"total_trials\": 100, \"n_tasks\": 10, \"n_rollouts_per_task\": 10, \"per_task\": {\"alphabet_soup\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"cream_cheese\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"salad_dressing\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"bbq_sauce\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"ketchup\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"tomato_sauce\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"butter\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"milk\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"chocolate_pudding\": {\"sr\": 30, \"success\": 3, \"trials\": 10}, \"orange_juice\": {\"sr\": 20, \"success\": 2, \"trials\": 10}}}, \"conclusion\": \"negative\"}, \"eval-mag-obsonly-norm02\": {\"metrics\": {\"T0_between_plate_ramekin\": 90, \"T1_next_to_ramekin\": 100, \"T2_table_center\": 0, \"T3_on_cookie_box\": 30, \"T4_top_drawer\": 10, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 90, \"T7_on_stove\": 0, \"T8_next_to_plate\": 30, \"T9_on_wooden_cabinet\": 0, \"overall_sr\": 35, \"total_success\": 35, \"total_rollouts\": 100}, \"conclusion\": \"negative\"}, \"eval-mag-obsonly-norm005\": {\"metrics\": {\"benchmark\": \"spatial\", \"mode\": \"crm_obs_only\", \"max_correction_norm\": 0.05, \"n_rollouts\": 10, \"K\": 10, \"overall_sr\": 35, \"total_success\": 35, \"total_episodes\": 100, \"per_task\": {\"T0_between_plate_ramekin\": 80, \"T1_next_to_ramekin\": 90, \"T2_table_center\": 0, \"T3_on_cookie_box\": 40, \"T4_top_drawer\": 10, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 80, \"T7_on_stove\": 0, \"T8_next_to_plate\": 50, \"T9_on_wooden_cabinet\": 0}}, \"conclusion\": \"success\"}, \"eval-acr-object-v4-perdof\": {\"metrics\": {\"overall_sr\": \"11.0% (11/100)\", \"total_success\": 11, \"total_rollouts\": 100, \"mode\": \"perdof\", \"benchmark\": \"object\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"alphabet_soup\": \"0%\", \"cream_cheese\": \"0%\", \"salad_dressing\": \"20%\", \"bbq_sauce\": \"30%\", \"ketchup\": \"0%\", \"tomato_sauce\": \"0%\", \"butter\": \"10%\", \"milk\": \"0%\", \"chocolate_pudding\": \"20%\", \"orange_juice\": \"30%\"}, \"note\": \"perdof object 11% vs argmin ~7% (partial). obs_only leads at ~14% (8/10). Confirms perdof not competitive on object.\"}, \"conclusion\": \"success\"}, \"eval-acr-spatial-v4-scalar-r2\": {\"metrics\": {\"overall_sr\": \"32.0% (32/100)\", \"total_success\": 32, \"total_rollouts\": 100, \"mode\": \"scalar_unc\", \"benchmark\": \"spatial\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"T0\": \"60%\", \"T1\": \"100%\", \"T2\": \"10%\", \"T3\": \"40%\", \"T4\": \"0%\", \"T5\": \"0%\", \"T6\": \"90%\", \"T7\": \"0%\", \"T8\": \"10%\", \"T9\": \"10%\"}, \"note\": \"D030 confirmed: scalar_unc spatial 32% vs argmin 34% = -2pp. T0-T2 from original eval-acr-spatial-v4-scalar, T3-T9 from r2 restart. All CRM variants dead on spatial.\"}, \"conclusion\": \"success\"}, \"eval-acr-spatial-v4-obs-only-r3\": {\"metrics\": {\"overall_sr\": \"35.0% (35/100)\", \"total_success\": 35, \"total_rollouts\": 100, \"mode\": \"crm_obs_only\", \"benchmark\": \"spatial\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"T0\": \"90%\", \"T1\": \"100%\", \"T2\": \"0%\", \"T3\": \"40%\", \"T4\": \"10%\", \"T5\": \"0%\", \"T6\": \"90%\", \"T7\": \"0%\", \"T8\": \"20%\", \"T9\": \"0%\"}, \"r3_subset_T6_T9\": \"27.5% (11/40)\", \"note\": \"D030: obs_only spatial 10-task = 35%. vs argmin 34% = +1pp. Scenario C threshold (>=39%) NOT MET. Earlier T0-T5 advantage (+5pp) wiped out by T6-T9.\"}, \"conclusion\": \"success\"}, \"eval-obs-only-spatial-seed43\": {\"conclusion\": \"failed\"}, \"eval-acr-spatial-v4-small-r2\": {\"metrics\": {\"overall_sr\": \"35.0% (35/100)\", \"total_success\": 35, \"total_rollouts\": 100, \"mode\": \"perdof\", \"benchmark\": \"spatial\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"T0\": \"60%\", \"T1\": \"100%\", \"T2\": \"10%\", \"T3\": \"40%\", \"T4\": \"0%\", \"T5\": \"0%\", \"T6\": \"90%\", \"T7\": \"10%\", \"T8\": \"40%\", \"T9\": \"0%\"}, \"note\": \"D029: perdof spatial complete 10-task = 35%. vs argmin 34% = +1pp. Kill criterion triggered — per-DOF claim dead on spatial.\"}, \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm-0.3-r3\": {\"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm-0p3-r3\": {\"conclusion\": \"killed\"}, \"eval-argmin-only-spatial-r2\": {\"metrics\": {\"overall_success_rate\": 0.34, \"total_successes\": 34, \"total_trials\": 100, \"per_task\": {\"T0_between_plate_and_ramekin\": 0.6, \"T1_next_to_ramekin\": 1, \"T2_from_table_center\": 0, \"T3_on_cookie_box\": 0.3, \"T4_in_top_drawer\": 0.1, \"T5_on_ramekin\": 0.1, \"T6_next_to_cookie_box\": 0.9, \"T7_on_stove\": 0, \"T8_next_to_plate\": 0.3, \"T9_on_wooden_cabinet\": 0.1}, \"note\": \"T0-T8 from original run (eval-argmin-only-spatial), T9 from r2 restart. Combined 10-task result.\"}, \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm003\": {\"conclusion\": \"killed\"}, \"eval-vla-only-object-k1\": {\"conclusion\": \"failed\"}, \"eval-acr-spatial-v4-obs-only-r2\": {\"metrics\": {\"tasks_done\": \"6/10\", \"partial_results\": {\"between_plate_and_ramekin\": \"90.0% (9/10)\", \"next_to_ramekin\": \"100.0% (10/10)\", \"from_table_center\": \"0.0% (0/10)\", \"on_cookie_box\": \"40.0% (4/10)\", \"in_top_drawer\": \"10.0% (1/10)\", \"on_ramekin\": \"0.0% (0/10)\"}, \"running_avg_6tasks\": \"40.0% (24/60)\", \"snapshot_time\": \"2026-05-15T12:00:00Z\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:0\", \"pid\": 270097}, \"conclusion\": \"failed\"}, \"eval-acr-spatial-v4-small\": {\"metrics\": {\"tasks_done\": \"7/10\", \"partial_results\": {\"between_plate_and_ramekin\": \"60.0% (6/10)\", \"next_to_ramekin\": \"100.0% (10/10)\", \"from_table_center\": \"10.0% (1/10)\", \"on_cookie_box\": \"40.0% (4/10)\", \"in_top_drawer\": \"0.0% (0/10)\", \"on_ramekin\": \"0.0% (0/10)\", \"next_to_cookie_box\": \"90.0% (9/10)\"}, \"running_avg_7tasks\": \"42.9% (30/70)\", \"snapshot_time\": \"2026-05-15T12:00:00Z\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:3\", \"pid\": 253085}, \"conclusion\": \"failed\"}, \"eval-acr-spatial-v4-scalar\": {\"metrics\": {\"tasks_done\": \"3/10\", \"partial_results\": {\"between_plate_and_ramekin\": \"60.0% (6/10)\", \"next_to_ramekin\": \"100.0% (10/10)\", \"from_table_center\": \"10.0% (1/10)\"}, \"running_avg_3tasks\": \"56.7% (17/30)\", \"snapshot_time\": \"2026-05-15T12:00:00Z\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:2\", \"pid\": 288939}, \"conclusion\": \"failed\"}, \"eval-argmin-only-spatial\": {\"metrics\": {\"tasks_done\": \"9/10\", \"partial_results\": {\"between_plate_and_ramekin\": \"60.0% (6/10)\", \"next_to_ramekin\": \"100.0% (10/10)\", \"from_table_center\": \"0.0% (0/10)\", \"on_cookie_box\": \"30.0% (3/10)\", \"in_top_drawer\": \"10.0% (1/10)\", \"on_ramekin\": \"10.0% (1/10)\", \"next_to_cookie_box\": \"90.0% (9/10)\", \"on_stove\": \"0.0% (0/10)\", \"next_to_plate\": \"30.0% (3/10)\"}, \"running_avg_9tasks\": \"36.7% (33/90)\", \"snapshot_time\": \"2026-05-15T12:00:00Z\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"pid\": 231421}, \"conclusion\": \"failed\"}, \"eval-vla-only-object\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.12, \"total_success\": 12, \"total_trials\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}}, \"eval-acr-spatial-v4-default-r3\": {\"conclusion\": \"killed\"}, \"eval-tiny-correction-spatial\": {\"metrics\": {\"tasks_done\": \"7/10\", \"partial_results\": {\"T1_between_plate_ramekin\": \"70% (7/10)\", \"T2_next_to_ramekin\": \"90% (9/10)\", \"T3_from_table_center\": \"0% (0/10)\", \"T4_on_cookie_box\": \"30% (3/10)\", \"T5_in_top_drawer\": \"0% (0/10)\", \"T6_on_ramekin\": \"0% (0/10)\", \"T7_next_to_cookie_box\": \"90% (9/10)\"}, \"running_avg_7tasks\": \"40% (28/70)\", \"process_status\": \"ACTUALLY ALIVE - bash wrapper PID 232815 dead but python child PID 232820 still running (07:48h, 139% CPU, 9.1GB RSS, GPU2)\", \"status_correction\": \"Registry incorrectly marked DONE, process is still completing remaining 3 tasks\", \"snapshot_time\": \"2026-05-15T09:40Z\"}, \"conclusion\": \"killed\"}, \"eval-vla-mean-spatial-t10\": {\"conclusion\": \"success\", \"metrics\": {\"T10_on_wooden_shelf\": \"10% (1/10)\", \"note\": \"Only ran task 9 (start_task=9). T10 = wooden shelf task.\"}}, \"eval-vla-mean-spatial\": {\"metrics\": {\"overall_success_rate_10tasks\": 0.32, \"total_successes\": 32, \"total_trials\": 100, \"T1\": 0.7, \"T2\": 1, \"T3\": 0, \"T4\": 0.3, \"T5\": 0, \"T6\": 0, \"T7\": 0.8, \"T8\": 0, \"T9\": 0.3, \"T10\": 0.1}, \"conclusion\": \"success\"}, \"eval-acr-spatial-v4-default-r2\": {\"conclusion\": \"killed\"}, \"eval-acr-spatial-v4-obs-only\": {\"conclusion\": \"failed\"}, \"eval-acr-spatial-v4-default\": {\"metrics\": {\"tasks_done\": \"0/10\", \"status_alert\": \"NO PROCESS FOUND - registry says RUNNING but no matching PID or tmux session on bjb1-18228. GPU 0 occupied by stale eval-acr-spatial-v3 tmux + crm-train-obs-only. NEEDS RESTART.\", \"snapshot_time\": \"2026-05-15T05:26Z\"}, \"conclusion\": \"failed\"}, \"crm-train-v3-norm-scalar-unc\": {\"metrics\": {\"best_epoch\": 46, \"best_val_loss\": 0.037354, \"final_train_loss\": 0.053422, \"final_val_loss\": 0.03737}, \"conclusion\": \"success\"}, \"crm-train-v3-norm-obs-only\": {\"metrics\": {\"best_epoch\": 48, \"best_val_loss\": 0.01645, \"final_train_loss\": 0.025576, \"final_val_loss\": 0.01645, \"total_epochs\": 50}, \"conclusion\": \"success\"}, \"eval-acr-object-v3\": {\"metrics\": {\"tasks_done\": \"4/10\", \"overall_success_rate\": 0, \"total_successes\": 0, \"total_rollouts\": 40, \"per_task_partial\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0, \"bbq_sauce\": 0}, \"snapshot_time\": \"2026-05-14T18:15Z\"}, \"conclusion\": \"failed\"}, \"eval-acr-spatial-v3\": {\"metrics\": {\"tasks_done\": \"4/10\", \"overall_success_rate\": 0.025, \"total_successes\": 1, \"total_rollouts\": 40, \"per_task_partial\": {\"pick_up_black_bowl_between_plate_and_ramekin\": 0.1, \"pick_up_black_bowl_next_to_ramekin\": 0, \"pick_up_black_bowl_from_table_center\": 0, \"pick_up_black_bowl_on_cookie_box\": 0}, \"snapshot_time\": \"2026-05-14T18:15Z\"}, \"conclusion\": \"failed\"}, \"crm-train-v3-norm\": {\"conclusion\": \"success\"}, \"crm-train-v3-scalar-unc\": {\"conclusion\": \"killed\", \"metrics\": {\"invalidation_reason\": \"Trained on bjb2 crm_cache v4 (6D state, pre-D016). Must retrain on bjb1 crm_cache_v5 (8D state).\", \"original_val_loss\": 1.195}}, \"crm-train-v3-obs-only\": {\"conclusion\": \"killed\", \"metrics\": {\"invalidation_reason\": \"Trained on bjb2 crm_cache v4 (6D state, pre-D016). Must retrain on bjb1 crm_cache_v5 (8D state).\", \"original_val_loss\": 1.193424}}, \"crm-train-v3-perdof\": {\"metrics\": {\"invalidation_reason\": \"Trained on bjb2 crm_cache v4 (6D state, pre-D016). Must retrain on bjb1 crm_cache_v5 (8D state).\", \"original_val_loss\": 1.191387}, \"conclusion\": \"killed\"}, \"eval-obs-only-spatial-v3\": {\"conclusion\": \"killed\"}, \"eval-scalar-unc-spatial-v2\": {\"conclusion\": \"killed\"}, \"eval-obs-only-spatial-v2\": {\"conclusion\": \"failed\"}, \"eval-obs-only-spatial\": {\"conclusion\": \"failed\", \"metrics\": {\"error\": \"size mismatch: obs_only CRM net.0.weight [256,990] vs acr_vla expects [256,1030] — no crm_obs_only mode in evaluate.py\"}}, \"crm-train-v2-obs-only\": {\"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.050501, \"best_epoch\": 50, \"total_epochs\": 50, \"final_train_loss\": 0.074839, \"comparison_vs_old\": \"old_6D_buggy=0.018312, new=0.050501 (loss metric changed with v2 fix)\"}}, \"crm-train-v2-scalar-unc\": {\"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.047202, \"best_epoch\": 48, \"total_epochs\": 50, \"final_train_loss\": 0.069679, \"comparison_vs_old\": \"old_6D_buggy=0.008379, new=0.047202 (loss metric changed with v2 fix)\"}}, \"crm-train-v2-perdof\": {\"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.051684, \"best_epoch\": 48, \"total_epochs\": 50, \"final_train_loss\": 0.076748, \"comparison_vs_old\": \"old_6D_buggy=0.009046, new=0.051684 (loss metric changed with v2 fix)\"}}, \"eval-reconvla-spatial-v3\": {\"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.34, \"total_successes\": 34, \"total_rollouts\": 100, \"per_task\": {\"pick_up_black_bowl_between_plate_and_ramekin\": 0.6, \"pick_up_black_bowl_next_to_ramekin\": 1, \"pick_up_black_bowl_from_table_center\": 0, \"pick_up_black_bowl_on_cookie_box\": 0.3, \"pick_up_black_bowl_in_top_drawer\": 0.1, \"pick_up_black_bowl_on_ramekin\": 0.1, \"pick_up_black_bowl_next_to_cookie_box\": 0.9, \"pick_up_black_bowl_on_stove\": 0, \"pick_up_black_bowl_next_to_plate\": 0.4, \"pick_up_black_bowl_on_wooden_cabinet\": 0}}}, \"precompute-v5-shard2\": {\"conclusion\": \"success\"}, \"precompute-v5-shard1\": {\"conclusion\": \"success\"}, \"precompute-v5-shard0\": {\"conclusion\": \"success\"}, \"crm-train-a4-scalar-unc\": {\"conclusion\": \"killed\", \"metrics\": {\"best_val_loss\": 0.008379, \"best_epoch\": 48, \"total_epochs\": 50, \"final_val_loss\": 0.008384, \"final_train_loss\": 0.012959}}, \"crm-train-a3-obs-only\": {\"conclusion\": \"killed\", \"metrics\": {\"best_val_loss\": 0.018312, \"best_epoch\": 4, \"early_stopped_at_epoch\": \"~15-20\", \"early_stop_reason\": \"val_loss plateau at 0.018 for 10+ epochs (full CRM: 0.009, 2x gap confirms conformal features are critical)\", \"input_dim\": 990, \"params\": 327966}}, \"crm-train-v1\": {\"conclusion\": \"killed\", \"metrics\": {\"best_val_loss\": 0.009046, \"best_epoch\": 50, \"total_epochs\": 50, \"checkpoint\": \"crm_best.pt\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm/crm_best.pt\", \"exit_code_note\": \"129 was false alarm - SIGHUP after training completed\"}}, \"crm-train-k5\": {\"conclusion\": \"killed\", \"metrics\": {\"best_val_loss\": 0.008996, \"best_epoch\": 50, \"total_epochs\": 50, \"comparison\": \"K=5 val_loss 0.008996 ≈ K=10 val_loss 0.009046, near identical\"}}, \"eval-scalar-unc-spatial\": {\"conclusion\": \"killed\"}, \"eval-acr-spatial-v2\": {\"conclusion\": \"killed\"}, \"eval-k5-spatial\": {\"conclusion\": \"killed\"}, \"eval-object-v8-full\": {\"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13, \"total_successes\": 13, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}}, \"eval-spatial-v7-full\": {\"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.3, \"total_successes\": 30, \"total_episodes\": 100, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"pick_up_black_bowl_between_plate_and_ramekin\": 0.6, \"pick_up_black_bowl_next_to_ramekin\": 1, \"pick_up_black_bowl_from_table_center\": 0, \"pick_up_black_bowl_on_cookie_box\": 0.2, \"pick_up_black_bowl_in_top_drawer\": 0, \"pick_up_black_bowl_on_ramekin\": 0, \"pick_up_black_bowl_next_to_cookie_box\": 0.9, \"pick_up_black_bowl_on_stove\": 0, \"pick_up_black_bowl_next_to_plate\": 0.3, \"pick_up_black_bowl_on_wooden_cabinet\": 0}}}, \"eval-object-v7-full\": {\"conclusion\": \"killed\"}, \"eval-spatial-v6-full\": {\"conclusion\": \"killed\"}, \"eval-object-v5-full\": {\"conclusion\": \"killed\"}, \"eval-acr-vla-spatial-v1\": {\"conclusion\": \"killed\"}, \"eval-acr-spatial-v1\": {\"conclusion\": \"killed\"}, \"eval-reconvla-spatial-v2\": {\"conclusion\": \"killed\"}, \"eval-object-v4-full\": {\"conclusion\": \"killed\"}, \"eval-spatial-v5-full\": {\"conclusion\": \"killed\"}, \"precompute-k5\": {\"conclusion\": \"success\", \"metrics\": {\"spatial_samples\": 12167, \"object_samples\": 14570, \"total_samples\": 26737, \"spatial_cache_mb\": 106, \"object_cache_mb\": 127, \"total_cache_mb\": 233, \"runtime_min\": 107}}, \"mvp-point-reaching\": {\"conclusion\": \"success\", \"metrics\": {\"group1_oracle\": {\"A_scalar\": {\"mse_x\": 0.180218, \"mse_y\": 0.02497, \"mse_z\": 0.024232, \"total\": 0.076473}, \"B_perDOF\": {\"mse_x\": 0.172652, \"mse_y\": 0.015544, \"mse_z\": 0.01561, \"total\": 0.067935}, \"C_none\": {\"mse_x\": 0.22706, \"mse_y\": 0.025542, \"mse_z\": 0.024753, \"total\": 0.092451}}, \"group2_oracle\": {\"A_scalar\": {\"mse_x\": 0.064642, \"mse_y\": 0.023836, \"mse_z\": 0.022967, \"total\": 0.037148}, \"B_perDOF\": {\"mse_x\": 0.053403, \"mse_y\": 0.015695, \"mse_z\": 0.01573, \"total\": 0.028276}, \"C_none\": {\"mse_x\": 0.084178, \"mse_y\": 0.025427, \"mse_z\": 0.024798, \"total\": 0.044801}}, \"group3_oracle\": {\"A_scalar\": {\"mse_x\": 0.042948, \"mse_y\": 0.023218, \"mse_z\": 0.022365, \"total\": 0.02951}, \"B_perDOF\": {\"mse_x\": 0.033008, \"mse_y\": 0.015621, \"mse_z\": 0.015647, \"total\": 0.021425}, \"C_none\": {\"mse_x\": 0.053043, \"mse_y\": 0.025523, \"mse_z\": 0.024741, \"total\": 0.034436}}, \"group4_K10\": {\"A_scalar\": {\"mse_x\": 0.187418, \"mse_y\": 0.024701, \"mse_z\": 0.024277, \"total\": 0.078799}, \"B_perDOF\": {\"mse_x\": 0.182888, \"mse_y\": 0.019072, \"mse_z\": 0.018475, \"total\": 0.073478}, \"C_none\": {\"mse_x\": 0.21507, \"mse_y\": 0.02496, \"mse_z\": 0.024637, \"total\": 0.088223}}, \"group5_K10\": {\"A_scalar\": {\"mse_x\": 0.064895, \"mse_y\": 0.02386, \"mse_z\": 0.023596, \"total\": 0.037451}, \"B_perDOF\": {\"mse_x\": 0.05851, \"mse_y\": 0.018868, \"mse_z\": 0.018471, \"total\": 0.03195}, \"C_none\": {\"mse_x\": 0.077047, \"mse_y\": 0.024825, \"mse_z\": 0.02464, \"total\": 0.042171}}, \"group6_K10\": {\"A_scalar\": {\"mse_x\": 0.041848, \"mse_y\": 0.02344, \"mse_z\": 0.023207, \"total\": 0.029498}, \"B_perDOF\": {\"mse_x\": 0.036348, \"mse_y\": 0.018736, \"mse_z\": 0.018453, \"total\": 0.024512}, \"C_none\": {\"mse_x\": 0.048365, \"mse_y\": 0.024827, \"mse_z\": 0.024577, \"total\": 0.03259}}, \"pass_criteria\": {\"group1\": \"PASS\", \"group4\": \"PASS\", \"overall\": \"SUCCESS\"}, \"summary_pct_improvements\": {\"reference_group\": \"group4_K10 (sigma=0.5/0.1/0.1, K=10 estimated uncertainty)\", \"perDOF_vs_scalar_total\": 6.75, \"perDOF_vs_none_total\": 16.71, \"perDOF_vs_scalar_y_axis\": 22.79, \"perDOF_vs_scalar_z_axis\": 23.9, \"paper_claims\": {\"6.7_pct_over_scalar\": \"group4 total: (0.078799-0.073478)/0.078799 = 6.75%\", \"16.7_pct_over_none\": \"group4 total: (0.088223-0.073478)/0.088223 = 16.71%\", \"22_24_pct_per_axis\": \"group4 y: 22.79%, z: 23.90%\"}}}}, \"eval-spatial-v3-full\": {\"conclusion\": \"killed\"}, \"eval-spatial-reeval-v2\": {\"conclusion\": \"killed\"}, \"eval-smolvla-libero-spatial\": {\"conclusion\": \"failed\"}, \"precompute-shard2\": {\"conclusion\": \"success\"}, \"precompute-shard1\": {\"conclusion\": \"success\"}, \"precompute-shard0\": {\"conclusion\": \"success\"}, \"plan_014-reconvla-baseline\": {\"conclusion\": \"failed\"}, \"plan_001-crm-smolvla\": {\"conclusion\": \"failed\"}}, \"count\": 137, \"total\": 137, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.366}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "e8924493-92f2-45ae-b70c-acb027ed0413",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"eval-vla-mean-object-seed44\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.1, \\\"per_task_sr\\\": {\\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": 0, \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": 0, \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": 0.1, \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": 0.3, \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": 0.1, \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": 0.1, \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": 0, \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": 0, \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": 0.2, \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": 0.2}}}, \\\"eval-obs-only-object-norm02-seed44-r4\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-argmin-object-seed44-r2\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.13, \\\"successes\\\": 13, \\\"total\\\": 100, \\\"tasks_done\\\": 10, \\\"tasks_total\\\": 10, \\\"per_task_sr\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0, \\\"salad_dressing\\\": 0.1, \\\"bbq_sauce\\\": 0.2, \\\"ketchup\\\": 0.1, \\\"tomato_sauce\\\": 0.1, \\\"butter\\\": 0, \\\"milk\\\": 0.1, \\\"chocolate_pudding\\\": 0.5, \\\"orange_juice\\\": 0.2}, \\\"note\\\": \\\"EXIT_CODE=129 was SIGHUP after completion, results valid. log: logs/eval_object_reconvla_seed44.json\\\"}}, \\\"eval-obs-only-object-norm02-seed44-r2\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.16, \\\"per_task_sr\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0.1, \\\"salad_dressing\\\": 0.2, \\\"bbq_sauce\\\": 0.2, \\\"ketchup\\\": 0.1, \\\"tomato_sauce\\\": 0.1, \\\"butter\\\": 0.2, \\\"milk\\\": 0.1, \\\"chocolate_pudding\\\": 0.3, \\\"orange_juice\\\": 0.3}}}, \\\"eval-vla-only-object-seed45\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.09, \\\"successes\\\": 18, \\\"total\\\": 200, \\\"tasks_done\\\": 10}}, \\\"eval-obs-only-object-norm03-seed45\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-mag-perdof-norm03-object-r3\\\": {\\\"metrics\\\": {\\\"overall_sr\\\": 0.04, \\\"successes\\\": 4, \\\"total\\\": 100, \\\"tasks_done\\\": 10, \\\"tasks_total\\\": 10}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-mag-perdof-norm02-seed43-object-r3\\\": {\\\"metrics\\\": {\\\"overall_sr\\\": 0.09, \\\"successes\\\": 9, \\\"total\\\": 100, \\\"tasks_done\\\": 10, \\\"tasks_total\\\": 10, \\\"per_task_sr\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0, \\\"salad_dressing\\\": 0.1, \\\"bbq_sauce\\\": 0.1, \\\"ketchup\\\": 0, \\\"tomato_sauce\\\": 0, \\\"butter\\\": 0, \\\"milk\\\": 0, \\\"chocolate_pudding\\\": 0.4, \\\"orange_juice\\\": 0.3}, \\\"vs_seed42\\\": \\\"-2pp (11% → 9%)\\\", \\\"pooled_2seed_perdof_02\\\": \\\"10% (20/200)\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-acr-object-v4-default-r2\\\": {\\\"metrics\\\": {\\\"overall_sr\\\": 0, \\\"successes\\\": 0, \\\"total\\\": 100, \\\"tasks_done\\\": 10, \\\"tasks_total\\\": 10, \\\"per_task_sr\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0, \\\"salad_dressing\\\": 0, \\\"bbq_sauce\\\": 0, \\\"ketchup\\\": 0, \\\"tomato_sauce\\\": 0, \\\"butter\\\": 0, \\\"milk\\\": 0, \\\"chocolate_pudding\\\": 0, \\\"orange_juice\\\": 0}, \\\"note\\\": \\\"actual mode=crm_perdof with default norm (~1.42), NOT crm_default. Confirms catastrophic failure at uncontrolled correction magnitude.\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-mag-perdof-norm005-object\\\": {\\\"metrics\\\": {\\\"overall_sr\\\": 0.14, \\\"successes\\\": 14, \\\"total\\\": 100, \\\"tasks_done\\\": 10, \\\"tasks_total\\\": 10}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-mag-perdof-norm003-object\\\": {\\\"metrics\\\": {\\\"tasks_done\\\": 10, \\\"tasks_total\\\": 10, \\\"overall_sr\\\": 0.14, \\\"per_task_sr\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0, \\\"salad_dressing\\\": 0.2, \\\"bbq_sauce\\\": 0.2, \\\"ketchup\\\": 0.1, \\\"tomato_sauce\\\": 0.1, \\\"butter\\\": 0.2, \\\"milk\\\": 0.1, \\\"chocolate_pudding\\\": 0.4, \\\"orange_juice\\\": 0.1}}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-mag-obsonly-norm005-object\\\": {\\\"metrics\\\": {\\\"overall_sr\\\": 0.13, \\\"tasks_completed\\\": 10, \\\"total_rollouts\\\": 100, \\\"successes\\\": 13, \\\"per_task_sr\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0, \\\"salad_dressing\\\": 0.1, \\\"bbq_sauce\\\": 0.3, \\\"ketchup\\\": 0, \\\"tomato_sauce\\\": 0.1, \\\"butter\\\": 0.1, \\\"milk\\\": 0.2, \\\"chocolate_pudding\\\": 0.2, \\\"orange_juice\\\": 0.3}}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-object-norm02-seed43-r2\\\": {\\\"metrics\\\": {\\\"overall_sr\\\": 0.16, \\\"successes\\\": 16, \\\"total\\\": 100, \\\"per_task\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0.1, \\\"salad_dressing\\\": 0.2, \\\"bbq_sauce\\\": 0.4, \\\"ketchup\\\": 0, \\\"tomato_sauce\\\": 0.1, \\\"butter\\\": 0.1, \\\"milk\\\": 0.1, \\\"chocolate_pudding\\\": 0.4, \\\"orange_juice\\\": 0.2}, \\\"vs_seed42\\\": \\\"-6pp (22% → 16%)\\\", \\\"vs_argmin_seed43\\\": \\\"-1pp (17% → 16%)\\\", \\\"pooled_2seed_obs_only_02\\\": \\\"19% (38/200)\\\", \\\"pooled_2seed_argmin\\\": \\\"14.5% (29/200)\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-mag-obsonly-norm03-object\\\": {\\\"metrics\\\": {\\\"tasks_done\\\": 10, \\\"tasks_total\\\": 10, \\\"overall_sr\\\": 0.19, \\\"successes\\\": 19, \\\"total\\\": 100}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-vla-only-object-seed44-r2\\\": {\\\"metrics\\\": {\\\"tasks_done\\\": 10, \\\"tasks_total\\\": 10, \\\"overall_sr\\\": 0.1, \\\"per_task_sr\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0.1, \\\"salad_dressing\\\": 0.2, \\\"bbq_sauce\\\": 0.2, \\\"ketchup\\\": 0, \\\"tomato_sauce\\\": 0, \\\"butter\\\": 0, \\\"milk\\\": 0.1, \\\"chocolate_pudding\\\": 0.2, \\\"orange_juice\\\": 0.2}}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-mag-perdof-norm02-object\\\": {\\\"metrics\\\": {\\\"tasks_done\\\": 10, \\\"tasks_total\\\": 10, \\\"overall_sr\\\": 0.11, \\\"per_task_sr\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0.1, \\\"salad_dressing\\\": 0.1, \\\"bbq_sauce\\\": 0.1, \\\"ketchup\\\": 0, \\\"tomato_sauce\\\": 0, \\\"butter\\\": 0.1, \\\"milk\\\": 0.1, \\\"chocolate_pudding\\\": 0.4, \\\"orange_juice\\\": 0.2}}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-acr-object-obs-only-default\\\": {\\\"metrics\\\": {\\\"tasks_done\\\": 10, \\\"tasks_total\\\": 10, \\\"overall_sr\\\": 0.17, \\\"per_task_sr\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0, \\\"salad_dressing\\\": 0.2, \\\"bbq_sauce\\\": 0.4, \\\"ketchup\\\": 0, \\\"tomato_sauce\\\": 0.1, \\\"butter\\\": 0.1, \\\"milk\\\": 0.1, \\\"chocolate_pudding\\\": 0.5, \\\"orange_juice\\\": 0.3}}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-scalar-object-seed43\\\": {\\\"metrics\\\": {\\\"tasks_done\\\": 10, \\\"tasks_total\\\": 10, \\\"avg_sr\\\": 10, \\\"per_task_sr\\\": {\\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": 0, \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": 0, \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": 0, \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": 30, \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": 0, \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": 0, \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": 0, \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": 10, \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": 30, \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": 30}}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-mag-obsonly-norm003-object\\\": {\\\"metrics\\\": {\\\"overall_sr\\\": 0.16, \\\"tasks_done\\\": 100, \\\"tasks_total\\\": 100, \\\"per_task\\\": {\\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": 0, \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": 0.2, \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": 0.1, \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": 0.4, \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": 0, \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": 0, \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": 0.1, \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": 0.2, \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": 0.3, \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": 0.3}}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-scalar-object-seed44\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-obs-only-object-norm02-seed44-r3\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-argmin-object-seed44-r3\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-vla-mean-object-seed43\\\": {\\\"metrics\\\": {\\\"overall_sr\\\": 0.15, \\\"tasks_done\\\": 10, \\\"tasks_total\\\": 10, \\\"total_success\\\": 15, \\\"total_rollouts\\\": 100, \\\"per_task\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0, \\\"salad_dressing\\\": 0.2, \\\"bbq_sauce\\\": 0.3, \\\"ketchup\\\": 0.1, \\\"tomato_sauce\\\": 0.1, \\\"butter\\\": 0.1, \\\"milk\\\": 0.3, \\\"chocolate_pudding\\\": 0.3, \\\"orange_juice\\\": 0.1}}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-perdof-object-seed43\\\": {\\\"metrics\\\": {\\\"overall_success_rate\\\": 0.12, \\\"tasks_done\\\": 10, \\\"tasks_total\\\": 10, \\\"total_rollouts\\\": 100, \\\"total_successes\\\": 12, \\\"per_task\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0, \\\"salad_dressing\\\": 0.2, \\\"bbq_sauce\\\": 0.3, \\\"ketchup\\\": 0, \\\"tomato_sauce\\\": 0, \\\"butter\\\": 0, \\\"milk\\\": 0, \\\"chocolate_pudding\\\": 0.4, \\\"orange_juice\\\": 0.3}}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-vla-only-object-seed44\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-obs-only-object-norm02-seed44\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-argmin-object-seed44\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-obs-only-object-seed43\\\": {\\\"metrics\\\": {\\\"overall_success_rate\\\": 0.12, \\\"tasks_done\\\": 10, \\\"tasks_total\\\": 10, \\\"per_task\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0.1, \\\"salad_dressing\\\": 0.1, \\\"bbq_sauce\\\": 0.3, \\\"ketchup\\\": 0, \\\"tomato_sauce\\\": 0, \\\"butter\\\": 0, \\\"milk\\\": 0.1, \\\"chocolate_pudding\\\": 0.4, \\\"orange_juice\\\": 0.2}, \\\"vs_argmin_seed43\\\": {\\\"obs_only\\\": 12, \\\"argmin\\\": 17, \\\"diff\\\": -5}, \\\"fisher_pooled\\\": {\\\"obs_only_total\\\": \\\"31/200\\\", \\\"argmin_total\\\": \\\"29/200\\\", \\\"pooled_obs_only_sr\\\": 0.155, \\\"pooled_argmin_sr\\\": 0.145, \\\"pooled_delta\\\": 0.01, \\\"odds_ratio\\\": 1.08, \\\"p_value_one_sided\\\": 0.4444, \\\"p_value_two_sided\\\": 0.8888}, \\\"source\\\": \\\"json_file_verified_by_worker\\\"}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-mag-obsonly-norm003-b2\\\": {\\\"metrics\\\": {\\\"overall_sr_10task\\\": 0.34, \\\"tasks_done\\\": 10, \\\"tasks_total\\\": 10, \\\"per_task\\\": {\\\"between_plate_and_ramekin\\\": 0.9, \\\"next_to_ramekin\\\": 1, \\\"from_table_center\\\": 0, \\\"on_cookie_box\\\": 0.3, \\\"in_top_drawer\\\": 0.1, \\\"on_ramekin\\\": 0, \\\"next_to_cookie_box\\\": 0.8, \\\"on_stove\\\": 0, \\\"next_to_plate\\\": 0.3, \\\"on_wooden_cabinet\\\": 0}}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-mag-obsonly-norm03-b2\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-argmin-object-seed43\\\": {\\\"metrics\\\": {\\\"overall_success_rate\\\": 0.17, \\\"total_successes\\\": 17, \\\"total_trials\\\": 100, \\\"per_task\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0, \\\"salad_dressing\\\": 0.2, \\\"bbq_sauce\\\": 0.2, \\\"ketchup\\\": 0.1, \\\"tomato_sauce\\\": 0.1, \\\"butter\\\": 0.2, \\\"milk\\\": 0.3, \\\"chocolate_pudding\\\": 0.4, \\\"orange_juice\\\": 0.2}}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-mag-perdof-norm02-seed43-object-r2\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-mag-obsonly-norm03\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-mag-obsonly-norm02-object\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-mag-obsonly-norm03-b4\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-mag-obsonly-norm03-b3\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-mag-perdof-norm02-seed43-object\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-mag-perdof-norm03-object-r2\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-acr-object-v4-scalar-b2\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-acr-object-v4-obs-only-b2\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-spatial-v4-full\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-reconvla-spatial-v1\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-object-v6-full\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"precompute-v4-shard2\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"precompute-v4-shard1\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"precompute-v4-shard0\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"precompute-v3-shard2\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"precompute-v3-shard1\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"precompute-v3-shard0\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"precompute-v2-shard2\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"precompute-v2-shard1\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"precompute-v2-shard0\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-mag-perdof-norm0p3-object-r2\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-vla-only-object-seed43\\\": {\\\"metrics\\\": {\\\"overall_sr\\\": 0.12, \\\"tasks_done\\\": 10, \\\"tasks_total\\\": 10, \\\"per_task_sr\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0.1, \\\"salad_dressing\\\": 0.1, \\\"bbq_sauce\\\": 0.3, \\\"ketchup\\\": 0, \\\"tomato_sauce\\\": 0, \\\"butter\\\": 0, \\\"milk\\\": 0.1, \\\"chocolate_pudding\\\": 0.4, \\\"orange_juice\\\": 0.2}, \\\"source\\\": \\\"json_file_verified_by_worker\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-mag-perdof-norm0p3-object\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-obs-only-object-norm02-seed43\\\": {\\\"metrics\\\": {\\\"pid\\\": 118214, \\\"gpu\\\": 3, \\\"process_status\\\": \\\"alive\\\", \\\"log_file\\\": \\\"logs/eval_object_obs_only_norm02_seed43.log\\\"}, \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-acr-object-v4-default\\\": {\\\"metrics\\\": {\\\"tasks_done\\\": 3, \\\"tasks_total\\\": 10, \\\"status\\\": \\\"DEAD\\\", \\\"partial_sr\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0, \\\"salad_dressing\\\": 0}, \\\"pid_42311\\\": \\\"not_found\\\", \\\"needs_restart\\\": true, \\\"checked_at\\\": \\\"2026-05-16T01:00Z\\\"}, \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-acr-object-obs-only-norm02\\\": {\\\"metrics\\\": {\\\"overall_sr\\\": 0.22, \\\"total_success\\\": 22, \\\"total_rollouts\\\": 100, \\\"tasks_done\\\": 10, \\\"tasks_total\\\": 10, \\\"per_task\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0, \\\"salad_dressing\\\": 0.3, \\\"bbq_sauce\\\": 0.4, \\\"ketchup\\\": 0.2, \\\"tomato_sauce\\\": 0.1, \\\"butter\\\": 0.1, \\\"milk\\\": 0.2, \\\"chocolate_pudding\\\": 0.6, \\\"orange_juice\\\": 0.3}}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-mag-perdof-norm02\\\": {\\\"metrics\\\": {\\\"tasks_done\\\": \\\"6/10\\\", \\\"partial_results\\\": {\\\"T0_between_plate_ramekin\\\": \\\"60%\\\", \\\"T1_next_to_ramekin\\\": \\\"90%\\\", \\\"T2_table_center\\\": \\\"0%\\\", \\\"T3_on_cookie_box\\\": \\\"20%\\\", \\\"T4_top_drawer\\\": \\\"0%\\\", \\\"T5_on_ramekin\\\": \\\"0%\\\"}, \\\"running_avg_6task\\\": \\\"28.3%\\\", \\\"snapshot_time\\\": \\\"2026-05-15T09:00:00Z\\\", \\\"server\\\": \\\"bjb2-28827\\\", \\\"process_status\\\": \\\"alive\\\"}, \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-mag-perdof-norm005\\\": {\\\"metrics\\\": {\\\"T0_between_plate_ramekin\\\": 50, \\\"T1_next_to_ramekin\\\": 100, \\\"T2_table_center\\\": 0, \\\"T3_on_cookie_box\\\": 30, \\\"T4_top_drawer\\\": 0, \\\"T5_on_ramekin\\\": 0, \\\"T6_next_to_cookie_box\\\": 100, \\\"T7_on_stove\\\": 0, \\\"T8_next_to_plate\\\": 30, \\\"T9_on_wooden_cabinet\\\": 0, \\\"avg_SR_10task\\\": 31}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-mag-obsonly-norm03-r2\\\": {\\\"metrics\\\": {\\\"bowl_between\\\": 0.9, \\\"next_to_ramekin\\\": 1, \\\"table_center\\\": 0, \\\"cookie_box\\\": 0.3, \\\"top_drawer\\\": 0.1, \\\"on_ramekin\\\": 0, \\\"next_to_cookie_box\\\": 1, \\\"stove\\\": 0, \\\"next_to_plate\\\": 0.3, \\\"wooden_cabinet\\\": 0, \\\"overall_SR\\\": 0.36}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-mag-perdof-norm03\\\": {\\\"metrics\\\": {\\\"overall_sr_10task\\\": 0.26, \\\"T0_sr\\\": 0.7, \\\"T1_sr\\\": 0.5, \\\"T2_sr\\\": 0.1, \\\"T3_sr\\\": 0.1, \\\"T4_sr\\\": 0, \\\"T5_sr\\\": 0, \\\"T6_sr\\\": 0.9, \\\"T7_sr\\\": 0.1, \\\"T8_sr\\\": 0.2, \\\"T9_sr\\\": 0, \\\"total_successes\\\": 26, \\\"total_rollouts\\\": 100, \\\"benchmark\\\": \\\"spatial\\\", \\\"max_correction_norm\\\": 0.3}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-vla-mean-object\\\": {\\\"metrics\\\": {\\\"benchmark\\\": \\\"object\\\", \\\"mode\\\": \\\"vla_only\\\", \\\"baseline_mode\\\": \\\"mean\\\", \\\"n_rollouts\\\": 10, \\\"K\\\": 10, \\\"seed\\\": 42, \\\"overall_sr\\\": 12, \\\"total_success\\\": 12, \\\"total_rollouts\\\": 100, \\\"tasks_done\\\": \\\"10/10\\\", \\\"per_task\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0, \\\"salad_dressing\\\": 10, \\\"bbq_sauce\\\": 30, \\\"ketchup\\\": 10, \\\"tomato_sauce\\\": 10, \\\"butter\\\": 0, \\\"milk\\\": 20, \\\"chocolate_pudding\\\": 30, \\\"orange_juice\\\": 10}, \\\"json_output\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean.json\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-mag-perdof-norm003\\\": {\\\"metrics\\\": {\\\"benchmark\\\": \\\"spatial\\\", \\\"mode\\\": \\\"acr_vla\\\", \\\"max_correction_norm\\\": 0.03, \\\"n_rollouts\\\": 10, \\\"K\\\": 10, \\\"seed\\\": 42, \\\"overall_sr\\\": 30, \\\"total_success\\\": 30, \\\"total_rollouts\\\": 100, \\\"tasks_done\\\": \\\"10/10\\\", \\\"per_task\\\": {\\\"T0_between_plate_ramekin\\\": 60, \\\"T1_next_to_ramekin\\\": 100, \\\"T2_table_center\\\": 0, \\\"T3_on_cookie_box\\\": 30, \\\"T4_top_drawer\\\": 10, \\\"T5_on_ramekin\\\": 0, \\\"T6_next_to_cookie_box\\\": 80, \\\"T7_on_stove\\\": 0, \\\"T8_next_to_plate\\\": 20, \\\"T9_on_wooden_cabinet\\\": 0}}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-reconvla-object\\\": {\\\"metrics\\\": {\\\"overall_sr\\\": 0.12, \\\"per_task\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0, \\\"salad_dressing\\\": 0.1, \\\"bbq_sauce\\\": 0.3, \\\"ketchup\\\": 0, \\\"tomato_sauce\\\": 0, \\\"butter\\\": 0.1, \\\"milk\\\": 0.1, \\\"chocolate_pudding\\\": 0.3, \\\"orange_juice\\\": 0.3}, \\\"n_rollouts\\\": 10, \\\"total_episodes\\\": 100, \\\"total_successes\\\": 12}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-acr-object-v4-obs-only\\\": {\\\"metrics\\\": {\\\"overall_sr\\\": \\\"19.0% (19/100)\\\", \\\"total_success\\\": 19, \\\"total_rollouts\\\": 100, \\\"mode\\\": \\\"obs_only\\\", \\\"benchmark\\\": \\\"object\\\", \\\"max_correction_norm\\\": 0.1, \\\"seed\\\": 42, \\\"K\\\": 10, \\\"tasks_done\\\": \\\"10/10\\\", \\\"per_task\\\": {\\\"alphabet_soup\\\": \\\"0%\\\", \\\"cream_cheese\\\": \\\"10%\\\", \\\"salad_dressing\\\": \\\"20%\\\", \\\"bbq_sauce\\\": \\\"40%\\\", \\\"ketchup\\\": \\\"10%\\\", \\\"tomato_sauce\\\": \\\"0%\\\", \\\"butter\\\": \\\"10%\\\", \\\"milk\\\": \\\"20%\\\", \\\"chocolate_pudding\\\": \\\"50%\\\", \\\"orange_juice\\\": \\\"30%\\\"}, \\\"json_output\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-acr-object-v4-scalar\\\": {\\\"metrics\\\": {\\\"overall_sr\\\": 9, \\\"total_success\\\": 9, \\\"total_trials\\\": 100, \\\"n_tasks\\\": 10, \\\"n_rollouts_per_task\\\": 10, \\\"per_task\\\": {\\\"alphabet_soup\\\": {\\\"sr\\\": 0, \\\"success\\\": 0, \\\"trials\\\": 10}, \\\"cream_cheese\\\": {\\\"sr\\\": 0, \\\"success\\\": 0, \\\"trials\\\": 10}, \\\"salad_dressing\\\": {\\\"sr\\\": 10, \\\"success\\\": 1, \\\"trials\\\": 10}, \\\"bbq_sauce\\\": {\\\"sr\\\": 10, \\\"success\\\": 1, \\\"trials\\\": 10}, \\\"ketchup\\\": {\\\"sr\\\": 0, \\\"success\\\": 0, \\\"trials\\\": 10}, \\\"tomato_sauce\\\": {\\\"sr\\\": 0, \\\"success\\\": 0, \\\"trials\\\": 10}, \\\"butter\\\": {\\\"sr\\\": 10, \\\"success\\\": 1, \\\"trials\\\": 10}, \\\"milk\\\": {\\\"sr\\\": 10, \\\"success\\\": 1, \\\"trials\\\": 10}, \\\"chocolate_pudding\\\": {\\\"sr\\\": 30, \\\"success\\\": 3, \\\"trials\\\": 10}, \\\"orange_juice\\\": {\\\"sr\\\": 20, \\\"success\\\": 2, \\\"trials\\\": 10}}}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-mag-obsonly-norm02\\\": {\\\"metrics\\\": {\\\"T0_between_plate_ramekin\\\": 90, \\\"T1_next_to_ramekin\\\": 100, \\\"T2_table_center\\\": 0, \\\"T3_on_cookie_box\\\": 30, \\\"T4_top_drawer\\\": 10, \\\"T5_on_ramekin\\\": 0, \\\"T6_next_to_cookie_box\\\": 90, \\\"T7_on_stove\\\": 0, \\\"T8_next_to_plate\\\": 30, \\\"T9_on_wooden_cabinet\\\": 0, \\\"overall_sr\\\": 35, \\\"total_success\\\": 35, \\\"total_rollouts\\\": 100}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval-mag-obsonly-norm005\\\": {\\\"metrics\\\": {\\\"benchmark\\\": \\\"spatial\\\", \\\"mode\\\": \\\"crm_obs_only\\\", \\\"max_correction_norm\\\": 0.05, \\\"n_rollouts\\\": 10, \\\"K\\\": 10, \\\"overall_sr\\\": 35, \\\"total_success\\\": 35, \\\"total_episodes\\\": 100, \\\"per_task\\\": {\\\"T0_between_plate_ramekin\\\": 80, \\\"T1_next_to_ramekin\\\": 90, \\\"T2_table_center\\\": 0, \\\"T3_on_cookie_box\\\": 40, \\\"T4_top_drawer\\\": 10, \\\"T5_on_ramekin\\\": 0, \\\"T6_next_to_cookie_box\\\": 80, \\\"T7_on_stove\\\": 0, \\\"T8_next_to_plate\\\": 50, \\\"T9_on_wooden_cabinet\\\": 0}}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-acr-object-v4-perdof\\\": {\\\"metrics\\\": {\\\"overall_sr\\\": \\\"11.0% (11/100)\\\", \\\"total_success\\\": 11, \\\"total_rollouts\\\": 100, \\\"mode\\\": \\\"perdof\\\", \\\"benchmark\\\": \\\"object\\\", \\\"max_correction_norm\\\": 0.1, \\\"seed\\\": 42, \\\"K\\\": 10, \\\"per_task\\\": {\\\"alphabet_soup\\\": \\\"0%\\\", \\\"cream_cheese\\\": \\\"0%\\\", \\\"salad_dressing\\\": \\\"20%\\\", \\\"bbq_sauce\\\": \\\"30%\\\", \\\"ketchup\\\": \\\"0%\\\", \\\"tomato_sauce\\\": \\\"0%\\\", \\\"butter\\\": \\\"10%\\\", \\\"milk\\\": \\\"0%\\\", \\\"chocolate_pudding\\\": \\\"20%\\\", \\\"orange_juice\\\": \\\"30%\\\"}, \\\"note\\\": \\\"perdof object 11% vs argmin ~7% (partial). obs_only leads at ~14% (8/10). Confirms perdof not competitive on object.\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-acr-spatial-v4-scalar-r2\\\": {\\\"metrics\\\": {\\\"overall_sr\\\": \\\"32.0% (32/100)\\\", \\\"total_success\\\": 32, \\\"total_rollouts\\\": 100, \\\"mode\\\": \\\"scalar_unc\\\", \\\"benchmark\\\": \\\"spatial\\\", \\\"max_correction_norm\\\": 0.1, \\\"seed\\\": 42, \\\"K\\\": 10, \\\"per_task\\\": {\\\"T0\\\": \\\"60%\\\", \\\"T1\\\": \\\"100%\\\", \\\"T2\\\": \\\"10%\\\", \\\"T3\\\": \\\"40%\\\", \\\"T4\\\": \\\"0%\\\", \\\"T5\\\": \\\"0%\\\", \\\"T6\\\": \\\"90%\\\", \\\"T7\\\": \\\"0%\\\", \\\"T8\\\": \\\"10%\\\", \\\"T9\\\": \\\"10%\\\"}, \\\"note\\\": \\\"D030 confirmed: scalar_unc spatial 32% vs argmin 34% = -2pp. T0-T2 from original eval-acr-spatial-v4-scalar, T3-T9 from r2 restart. All CRM variants dead on spatial.\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-acr-spatial-v4-obs-only-r3\\\": {\\\"metrics\\\": {\\\"overall_sr\\\": \\\"35.0% (35/100)\\\", \\\"total_success\\\": 35, \\\"total_rollouts\\\": 100, \\\"mode\\\": \\\"crm_obs_only\\\", \\\"benchmark\\\": \\\"spatial\\\", \\\"max_correction_norm\\\": 0.1, \\\"seed\\\": 42, \\\"K\\\": 10, \\\"per_task\\\": {\\\"T0\\\": \\\"90%\\\", \\\"T1\\\": \\\"100%\\\", \\\"T2\\\": \\\"0%\\\", \\\"T3\\\": \\\"40%\\\", \\\"T4\\\": \\\"10%\\\", \\\"T5\\\": \\\"0%\\\", \\\"T6\\\": \\\"90%\\\", \\\"T7\\\": \\\"0%\\\", \\\"T8\\\": \\\"20%\\\", \\\"T9\\\": \\\"0%\\\"}, \\\"r3_subset_T6_T9\\\": \\\"27.5% (11/40)\\\", \\\"note\\\": \\\"D030: obs_only spatial 10-task = 35%. vs argmin 34% = +1pp. Scenario C threshold (>=39%) NOT MET. Earlier T0-T5 advantage (+5pp) wiped out by T6-T9.\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-obs-only-spatial-seed43\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-acr-spatial-v4-small-r2\\\": {\\\"metrics\\\": {\\\"overall_sr\\\": \\\"35.0% (35/100)\\\", \\\"total_success\\\": 35, \\\"total_rollouts\\\": 100, \\\"mode\\\": \\\"perdof\\\", \\\"benchmark\\\": \\\"spatial\\\", \\\"max_correction_norm\\\": 0.1, \\\"seed\\\": 42, \\\"K\\\": 10, \\\"per_task\\\": {\\\"T0\\\": \\\"60%\\\", \\\"T1\\\": \\\"100%\\\", \\\"T2\\\": \\\"10%\\\", \\\"T3\\\": \\\"40%\\\", \\\"T4\\\": \\\"0%\\\", \\\"T5\\\": \\\"0%\\\", \\\"T6\\\": \\\"90%\\\", \\\"T7\\\": \\\"10%\\\", \\\"T8\\\": \\\"40%\\\", \\\"T9\\\": \\\"0%\\\"}, \\\"note\\\": \\\"D029: perdof spatial complete 10-task = 35%. vs argmin 34% = +1pp. Kill criterion triggered — per-DOF claim dead on spatial.\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-mag-obsonly-norm-0.3-r3\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-mag-obsonly-norm-0p3-r3\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-argmin-only-spatial-r2\\\": {\\\"metrics\\\": {\\\"overall_success_rate\\\": 0.34, \\\"total_successes\\\": 34, \\\"total_trials\\\": 100, \\\"per_task\\\": {\\\"T0_between_plate_and_ramekin\\\": 0.6, \\\"T1_next_to_ramekin\\\": 1, \\\"T2_from_table_center\\\": 0, \\\"T3_on_cookie_box\\\": 0.3, \\\"T4_in_top_drawer\\\": 0.1, \\\"T5_on_ramekin\\\": 0.1, \\\"T6_next_to_cookie_box\\\": 0.9, \\\"T7_on_stove\\\": 0, \\\"T8_next_to_plate\\\": 0.3, \\\"T9_on_wooden_cabinet\\\": 0.1}, \\\"note\\\": \\\"T0-T8 from original run (eval-argmin-only-spatial), T9 from r2 restart. Combined 10-task result.\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-mag-obsonly-norm003\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-vla-only-object-k1\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-acr-spatial-v4-obs-only-r2\\\": {\\\"metrics\\\": {\\\"tasks_done\\\": \\\"6/10\\\", \\\"partial_results\\\": {\\\"between_plate_and_ramekin\\\": \\\"90.0% (9/10)\\\", \\\"next_to_ramekin\\\": \\\"100.0% (10/10)\\\", \\\"from_table_center\\\": \\\"0.0% (0/10)\\\", \\\"on_cookie_box\\\": \\\"40.0% (4/10)\\\", \\\"in_top_drawer\\\": \\\"10.0% (1/10)\\\", \\\"on_ramekin\\\": \\\"0.0% (0/10)\\\"}, \\\"running_avg_6tasks\\\": \\\"40.0% (24/60)\\\", \\\"snapshot_time\\\": \\\"2026-05-15T12:00:00Z\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": 270097}, \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-acr-spatial-v4-small\\\": {\\\"metrics\\\": {\\\"tasks_done\\\": \\\"7/10\\\", \\\"partial_results\\\": {\\\"between_plate_and_ramekin\\\": \\\"60.0% (6/10)\\\", \\\"next_to_ramekin\\\": \\\"100.0% (10/10)\\\", \\\"from_table_center\\\": \\\"10.0% (1/10)\\\", \\\"on_cookie_box\\\": \\\"40.0% (4/10)\\\", \\\"in_top_drawer\\\": \\\"0.0% (0/10)\\\", \\\"on_ramekin\\\": \\\"0.0% (0/10)\\\", \\\"next_to_cookie_box\\\": \\\"90.0% (9/10)\\\"}, \\\"running_avg_7tasks\\\": \\\"42.9% (30/70)\\\", \\\"snapshot_time\\\": \\\"2026-05-15T12:00:00Z\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"gpu\\\": \\\"cuda:3\\\", \\\"pid\\\": 253085}, \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-acr-spatial-v4-scalar\\\": {\\\"metrics\\\": {\\\"tasks_done\\\": \\\"3/10\\\", \\\"partial_results\\\": {\\\"between_plate_and_ramekin\\\": \\\"60.0% (6/10)\\\", \\\"next_to_ramekin\\\": \\\"100.0% (10/10)\\\", \\\"from_table_center\\\": \\\"10.0% (1/10)\\\"}, \\\"running_avg_3tasks\\\": \\\"56.7% (17/30)\\\", \\\"snapshot_time\\\": \\\"2026-05-15T12:00:00Z\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"gpu\\\": \\\"cuda:2\\\", \\\"pid\\\": 288939}, \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-argmin-only-spatial\\\": {\\\"metrics\\\": {\\\"tasks_done\\\": \\\"9/10\\\", \\\"partial_results\\\": {\\\"between_plate_and_ramekin\\\": \\\"60.0% (6/10)\\\", \\\"next_to_ramekin\\\": \\\"100.0% (10/10)\\\", \\\"from_table_center\\\": \\\"0.0% (0/10)\\\", \\\"on_cookie_box\\\": \\\"30.0% (3/10)\\\", \\\"in_top_drawer\\\": \\\"10.0% (1/10)\\\", \\\"on_ramekin\\\": \\\"10.0% (1/10)\\\", \\\"next_to_cookie_box\\\": \\\"90.0% (9/10)\\\", \\\"on_stove\\\": \\\"0.0% (0/10)\\\", \\\"next_to_plate\\\": \\\"30.0% (3/10)\\\"}, \\\"running_avg_9tasks\\\": \\\"36.7% (33/90)\\\", \\\"snapshot_time\\\": \\\"2026-05-15T12:00:00Z\\\", \\\"server\\\": \\\"bjb1-18228\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"pid\\\": 231421}, \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-vla-only-object\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 0.12, \\\"total_success\\\": 12, \\\"total_trials\\\": 100, \\\"per_task\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0.1, \\\"salad_dressing\\\": 0.2, \\\"bbq_sauce\\\": 0.2, \\\"ketchup\\\": 0, \\\"tomato_sauce\\\": 0.1, \\\"butter\\\": 0, \\\"milk\\\": 0.1, \\\"chocolate_pudding\\\": 0.2, \\\"orange_juice\\\": 0.3}}}, \\\"eval-acr-spatial-v4-default-r3\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-tiny-correction-spatial\\\": {\\\"metrics\\\": {\\\"tasks_done\\\": \\\"7/10\\\", \\\"partial_results\\\": {\\\"T1_between_plate_ramekin\\\": \\\"70% (7/10)\\\", \\\"T2_next_to_ramekin\\\": \\\"90% (9/10)\\\", \\\"T3_from_table_center\\\": \\\"0% (0/10)\\\", \\\"T4_on_cookie_box\\\": \\\"30% (3/10)\\\", \\\"T5_in_top_drawer\\\": \\\"0% (0/10)\\\", \\\"T6_on_ramekin\\\": \\\"0% (0/10)\\\", \\\"T7_next_to_cookie_box\\\": \\\"90% (9/10)\\\"}, \\\"running_avg_7tasks\\\": \\\"40% (28/70)\\\", \\\"process_status\\\": \\\"ACTUALLY ALIVE - bash wrapper PID 232815 dead but python child PID 232820 still running (07:48h, 139% CPU, 9.1GB RSS, GPU2)\\\", \\\"status_correction\\\": \\\"Registry incorrectly marked DONE, process is still completing remaining 3 tasks\\\", \\\"snapshot_time\\\": \\\"2026-05-15T09:40Z\\\"}, \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-vla-mean-spatial-t10\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"T10_on_wooden_shelf\\\": \\\"10% (1/10)\\\", \\\"note\\\": \\\"Only ran task 9 (start_task=9). T10 = wooden shelf task.\\\"}}, \\\"eval-vla-mean-spatial\\\": {\\\"metrics\\\": {\\\"overall_success_rate_10tasks\\\": 0.32, \\\"total_successes\\\": 32, \\\"total_trials\\\": 100, \\\"T1\\\": 0.7, \\\"T2\\\": 1, \\\"T3\\\": 0, \\\"T4\\\": 0.3, \\\"T5\\\": 0, \\\"T6\\\": 0, \\\"T7\\\": 0.8, \\\"T8\\\": 0, \\\"T9\\\": 0.3, \\\"T10\\\": 0.1}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-acr-spatial-v4-default-r2\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-acr-spatial-v4-obs-only\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-acr-spatial-v4-default\\\": {\\\"metrics\\\": {\\\"tasks_done\\\": \\\"0/10\\\", \\\"status_alert\\\": \\\"NO PROCESS FOUND - registry says RUNNING but no matching PID or tmux session on bjb1-18228. GPU 0 occupied by stale eval-acr-spatial-v3 tmux + crm-train-obs-only. NEEDS RESTART.\\\", \\\"snapshot_time\\\": \\\"2026-05-15T05:26Z\\\"}, \\\"conclusion\\\": \\\"failed\\\"}, \\\"crm-train-v3-norm-scalar-unc\\\": {\\\"metrics\\\": {\\\"best_epoch\\\": 46, \\\"best_val_loss\\\": 0.037354, \\\"final_train_loss\\\": 0.053422, \\\"final_val_loss\\\": 0.03737}, \\\"conclusion\\\": \\\"success\\\"}, \\\"crm-train-v3-norm-obs-only\\\": {\\\"metrics\\\": {\\\"best_epoch\\\": 48, \\\"best_val_loss\\\": 0.01645, \\\"final_train_loss\\\": 0.025576, \\\"final_val_loss\\\": 0.01645, \\\"total_epochs\\\": 50}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval-acr-object-v3\\\": {\\\"metrics\\\": {\\\"tasks_done\\\": \\\"4/10\\\", \\\"overall_success_rate\\\": 0, \\\"total_successes\\\": 0, \\\"total_rollouts\\\": 40, \\\"per_task_partial\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0, \\\"salad_dressing\\\": 0, \\\"bbq_sauce\\\": 0}, \\\"snapshot_time\\\": \\\"2026-05-14T18:15Z\\\"}, \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-acr-spatial-v3\\\": {\\\"metrics\\\": {\\\"tasks_done\\\": \\\"4/10\\\", \\\"overall_success_rate\\\": 0.025, \\\"total_successes\\\": 1, \\\"total_rollouts\\\": 40, \\\"per_task_partial\\\": {\\\"pick_up_black_bowl_between_plate_and_ramekin\\\": 0.1, \\\"pick_up_black_bowl_next_to_ramekin\\\": 0, \\\"pick_up_black_bowl_from_table_center\\\": 0, \\\"pick_up_black_bowl_on_cookie_box\\\": 0}, \\\"snapshot_time\\\": \\\"2026-05-14T18:15Z\\\"}, \\\"conclusion\\\": \\\"failed\\\"}, \\\"crm-train-v3-norm\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"crm-train-v3-scalar-unc\\\": {\\\"conclusion\\\": \\\"killed\\\", \\\"metrics\\\": {\\\"invalidation_reason\\\": \\\"Trained on bjb2 crm_cache v4 (6D state, pre-D016). Must retrain on bjb1 crm_cache_v5 (8D state).\\\", \\\"original_val_loss\\\": 1.195}}, \\\"crm-train-v3-obs-only\\\": {\\\"conclusion\\\": \\\"killed\\\", \\\"metrics\\\": {\\\"invalidation_reason\\\": \\\"Trained on bjb2 crm_cache v4 (6D state, pre-D016). Must retrain on bjb1 crm_cache_v5 (8D state).\\\", \\\"original_val_loss\\\": 1.193424}}, \\\"crm-train-v3-perdof\\\": {\\\"metrics\\\": {\\\"invalidation_reason\\\": \\\"Trained on bjb2 crm_cache v4 (6D state, pre-D016). Must retrain on bjb1 crm_cache_v5 (8D state).\\\", \\\"original_val_loss\\\": 1.191387}, \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-obs-only-spatial-v3\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-scalar-unc-spatial-v2\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-obs-only-spatial-v2\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"eval-obs-only-spatial\\\": {\\\"conclusion\\\": \\\"failed\\\", \\\"metrics\\\": {\\\"error\\\": \\\"size mismatch: obs_only CRM net.0.weight [256,990] vs acr_vla expects [256,1030] — no crm_obs_only mode in evaluate.py\\\"}}, \\\"crm-train-v2-obs-only\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"best_val_loss\\\": 0.050501, \\\"best_epoch\\\": 50, \\\"total_epochs\\\": 50, \\\"final_train_loss\\\": 0.074839, \\\"comparison_vs_old\\\": \\\"old_6D_buggy=0.018312, new=0.050501 (loss metric changed with v2 fix)\\\"}}, \\\"crm-train-v2-scalar-unc\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"best_val_loss\\\": 0.047202, \\\"best_epoch\\\": 48, \\\"total_epochs\\\": 50, \\\"final_train_loss\\\": 0.069679, \\\"comparison_vs_old\\\": \\\"old_6D_buggy=0.008379, new=0.047202 (loss metric changed with v2 fix)\\\"}}, \\\"crm-train-v2-perdof\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"best_val_loss\\\": 0.051684, \\\"best_epoch\\\": 48, \\\"total_epochs\\\": 50, \\\"final_train_loss\\\": 0.076748, \\\"comparison_vs_old\\\": \\\"old_6D_buggy=0.009046, new=0.051684 (loss metric changed with v2 fix)\\\"}}, \\\"eval-reconvla-spatial-v3\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.34, \\\"total_successes\\\": 34, \\\"total_rollouts\\\": 100, \\\"per_task\\\": {\\\"pick_up_black_bowl_between_plate_and_ramekin\\\": 0.6, \\\"pick_up_black_bowl_next_to_ramekin\\\": 1, \\\"pick_up_black_bowl_from_table_center\\\": 0, \\\"pick_up_black_bowl_on_cookie_box\\\": 0.3, \\\"pick_up_black_bowl_in_top_drawer\\\": 0.1, \\\"pick_up_black_bowl_on_ramekin\\\": 0.1, \\\"pick_up_black_bowl_next_to_cookie_box\\\": 0.9, \\\"pick_up_black_bowl_on_stove\\\": 0, \\\"pick_up_black_bowl_next_to_plate\\\": 0.4, \\\"pick_up_black_bowl_on_wooden_cabinet\\\": 0}}}, \\\"precompute-v5-shard2\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"precompute-v5-shard1\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"precompute-v5-shard0\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"crm-train-a4-scalar-unc\\\": {\\\"conclusion\\\": \\\"killed\\\", \\\"metrics\\\": {\\\"best_val_loss\\\": 0.008379, \\\"best_epoch\\\": 48, \\\"total_epochs\\\": 50, \\\"final_val_loss\\\": 0.008384, \\\"final_train_loss\\\": 0.012959}}, \\\"crm-train-a3-obs-only\\\": {\\\"conclusion\\\": \\\"killed\\\", \\\"metrics\\\": {\\\"best_val_loss\\\": 0.018312, \\\"best_epoch\\\": 4, \\\"early_stopped_at_epoch\\\": \\\"~15-20\\\", \\\"early_stop_reason\\\": \\\"val_loss plateau at 0.018 for 10+ epochs (full CRM: 0.009, 2x gap confirms conformal features are critical)\\\", \\\"input_dim\\\": 990, \\\"params\\\": 327966}}, \\\"crm-train-v1\\\": {\\\"conclusion\\\": \\\"killed\\\", \\\"metrics\\\": {\\\"best_val_loss\\\": 0.009046, \\\"best_epoch\\\": 50, \\\"total_epochs\\\": 50, \\\"checkpoint\\\": \\\"crm_best.pt\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/crm/crm_best.pt\\\", \\\"exit_code_note\\\": \\\"129 was false alarm - SIGHUP after training completed\\\"}}, \\\"crm-train-k5\\\": {\\\"conclusion\\\": \\\"killed\\\", \\\"metrics\\\": {\\\"best_val_loss\\\": 0.008996, \\\"best_epoch\\\": 50, \\\"total_epochs\\\": 50, \\\"comparison\\\": \\\"K=5 val_loss 0.008996 ≈ K=10 val_loss 0.009046, near identical\\\"}}, \\\"eval-scalar-unc-spatial\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-acr-spatial-v2\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-k5-spatial\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-object-v8-full\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.13, \\\"total_successes\\\": 13, \\\"total_rollouts\\\": 100, \\\"per_task\\\": {\\\"alphabet_soup\\\": 0, \\\"cream_cheese\\\": 0, \\\"salad_dressing\\\": 0.2, \\\"bbq_sauce\\\": 0.3, \\\"ketchup\\\": 0, \\\"tomato_sauce\\\": 0.1, \\\"butter\\\": 0.1, \\\"milk\\\": 0.2, \\\"chocolate_pudding\\\": 0.2, \\\"orange_juice\\\": 0.2}}}, \\\"eval-spatial-v7-full\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"overall_success_rate\\\": 0.3, \\\"total_successes\\\": 30, \\\"total_episodes\\\": 100, \\\"n_tasks\\\": 10, \\\"n_rollouts\\\": 10, \\\"per_task\\\": {\\\"pick_up_black_bowl_between_plate_and_ramekin\\\": 0.6, \\\"pick_up_black_bowl_next_to_ramekin\\\": 1, \\\"pick_up_black_bowl_from_table_center\\\": 0, \\\"pick_up_black_bowl_on_cookie_box\\\": 0.2, \\\"pick_up_black_bowl_in_top_drawer\\\": 0, \\\"pick_up_black_bowl_on_ramekin\\\": 0, \\\"pick_up_black_bowl_next_to_cookie_box\\\": 0.9, \\\"pick_up_black_bowl_on_stove\\\": 0, \\\"pick_up_black_bowl_next_to_plate\\\": 0.3, \\\"pick_up_black_bowl_on_wooden_cabinet\\\": 0}}}, \\\"eval-object-v7-full\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-spatial-v6-full\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-object-v5-full\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-acr-vla-spatial-v1\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-acr-spatial-v1\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-reconvla-spatial-v2\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-object-v4-full\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-spatial-v5-full\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"precompute-k5\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"spatial_samples\\\": 12167, \\\"object_samples\\\": 14570, \\\"total_samples\\\": 26737, \\\"spatial_cache_mb\\\": 106, \\\"object_cache_mb\\\": 127, \\\"total_cache_mb\\\": 233, \\\"runtime_min\\\": 107}}, \\\"mvp-point-reaching\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"group1_oracle\\\": {\\\"A_scalar\\\": {\\\"mse_x\\\": 0.180218, \\\"mse_y\\\": 0.02497, \\\"mse_z\\\": 0.024232, \\\"total\\\": 0.076473}, \\\"B_perDOF\\\": {\\\"mse_x\\\": 0.172652, \\\"mse_y\\\": 0.015544, \\\"mse_z\\\": 0.01561, \\\"total\\\": 0.067935}, \\\"C_none\\\": {\\\"mse_x\\\": 0.22706, \\\"mse_y\\\": 0.025542, \\\"mse_z\\\": 0.024753, \\\"total\\\": 0.092451}}, \\\"group2_oracle\\\": {\\\"A_scalar\\\": {\\\"mse_x\\\": 0.064642, \\\"mse_y\\\": 0.023836, \\\"mse_z\\\": 0.022967, \\\"total\\\": 0.037148}, \\\"B_perDOF\\\": {\\\"mse_x\\\": 0.053403, \\\"mse_y\\\": 0.015695, \\\"mse_z\\\": 0.01573, \\\"total\\\": 0.028276}, \\\"C_none\\\": {\\\"mse_x\\\": 0.084178, \\\"mse_y\\\": 0.025427, \\\"mse_z\\\": 0.024798, \\\"total\\\": 0.044801}}, \\\"group3_oracle\\\": {\\\"A_scalar\\\": {\\\"mse_x\\\": 0.042948, \\\"mse_y\\\": 0.023218, \\\"mse_z\\\": 0.022365, \\\"total\\\": 0.02951}, \\\"B_perDOF\\\": {\\\"mse_x\\\": 0.033008, \\\"mse_y\\\": 0.015621, \\\"mse_z\\\": 0.015647, \\\"total\\\": 0.021425}, \\\"C_none\\\": {\\\"mse_x\\\": 0.053043, \\\"mse_y\\\": 0.025523, \\\"mse_z\\\": 0.024741, \\\"total\\\": 0.034436}}, \\\"group4_K10\\\": {\\\"A_scalar\\\": {\\\"mse_x\\\": 0.187418, \\\"mse_y\\\": 0.024701, \\\"mse_z\\\": 0.024277, \\\"total\\\": 0.078799}, \\\"B_perDOF\\\": {\\\"mse_x\\\": 0.182888, \\\"mse_y\\\": 0.019072, \\\"mse_z\\\": 0.018475, \\\"total\\\": 0.073478}, \\\"C_none\\\": {\\\"mse_x\\\": 0.21507, \\\"mse_y\\\": 0.02496, \\\"mse_z\\\": 0.024637, \\\"total\\\": 0.088223}}, \\\"group5_K10\\\": {\\\"A_scalar\\\": {\\\"mse_x\\\": 0.064895, \\\"mse_y\\\": 0.02386, \\\"mse_z\\\": 0.023596, \\\"total\\\": 0.037451}, \\\"B_perDOF\\\": {\\\"mse_x\\\": 0.05851, \\\"mse_y\\\": 0.018868, \\\"mse_z\\\": 0.018471, \\\"total\\\": 0.03195}, \\\"C_none\\\": {\\\"mse_x\\\": 0.077047, \\\"mse_y\\\": 0.024825, \\\"mse_z\\\": 0.02464, \\\"total\\\": 0.042171}}, \\\"group6_K10\\\": {\\\"A_scalar\\\": {\\\"mse_x\\\": 0.041848, \\\"mse_y\\\": 0.02344, \\\"mse_z\\\": 0.023207, \\\"total\\\": 0.029498}, \\\"B_perDOF\\\": {\\\"mse_x\\\": 0.036348, \\\"mse_y\\\": 0.018736, \\\"mse_z\\\": 0.018453, \\\"total\\\": 0.024512}, \\\"C_none\\\": {\\\"mse_x\\\": 0.048365, \\\"mse_y\\\": 0.024827, \\\"mse_z\\\": 0.024577, \\\"total\\\": 0.03259}}, \\\"pass_criteria\\\": {\\\"group1\\\": \\\"PASS\\\", \\\"group4\\\": \\\"PASS\\\", \\\"overall\\\": \\\"SUCCESS\\\"}, \\\"summary_pct_improvements\\\": {\\\"reference_group\\\": \\\"group4_K10 (sigma=0.5/0.1/0.1, K=10 estimated uncertainty)\\\", \\\"perDOF_vs_scalar_total\\\": 6.75, \\\"perDOF_vs_none_total\\\": 16.71, \\\"perDOF_vs_scalar_y_axis\\\": 22.79, \\\"perDOF_vs_scalar_z_axis\\\": 23.9, \\\"paper_claims\\\": {\\\"6.7_pct_over_scalar\\\": \\\"group4 total: (0.078799-0.073478)/0.078799 = 6.75%\\\", \\\"16.7_pct_over_none\\\": \\\"group4 total: (0.088223-0.073478)/0.088223 = 16.71%\\\", \\\"22_24_pct_per_axis\\\": \\\"group4 y: 22.79%, z: 23.90%\\\"}}}}, \\\"eval-spatial-v3-full\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-spatial-reeval-v2\\\": {\\\"conclusion\\\": \\\"killed\\\"}, \\\"eval-smolvla-libero-spatial\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"precompute-shard2\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"precompute-shard1\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"precompute-shard0\\\": {\\\"conclusion\\\": \\\"success\\\"}, \\\"plan_014-reconvla-baseline\\\": {\\\"conclusion\\\": \\\"failed\\\"}, \\\"plan_001-crm-smolvla\\\": {\\\"conclusion\\\": \\\"failed\\\"}}, \\\"count\\\": 137, \\\"total\\\": 137, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.366}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval-vla-mean-object-seed44\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.1, \"per_task_sr\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.1, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.3, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0.1, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0.1, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 0, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.2, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.2}}}, \"eval-obs-only-object-norm02-seed44-r4\": {\"conclusion\": \"killed\"}, \"eval-argmin-object-seed44-r2\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.13, \"successes\": 13, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.5, \"orange_juice\": 0.2}, \"note\": \"EXIT_CODE=129 was SIGHUP after completion, results valid. log: logs/eval_object_reconvla_seed44.json\"}}, \"eval-obs-only-object-norm02-seed44-r2\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.16, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}}, \"eval-vla-only-object-seed45\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.09, \"successes\": 18, \"total\": 200, \"tasks_done\": 10}}, \"eval-obs-only-object-norm03-seed45\": {\"conclusion\": \"failed\"}, \"eval-mag-perdof-norm03-object-r3\": {\"metrics\": {\"overall_sr\": 0.04, \"successes\": 4, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10}, \"conclusion\": \"success\"}, \"eval-mag-perdof-norm02-seed43-object-r3\": {\"metrics\": {\"overall_sr\": 0.09, \"successes\": 9, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}, \"vs_seed42\": \"-2pp (11% → 9%)\", \"pooled_2seed_perdof_02\": \"10% (20/200)\"}, \"conclusion\": \"success\"}, \"eval-acr-object-v4-default-r2\": {\"metrics\": {\"overall_sr\": 0, \"successes\": 0, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0, \"bbq_sauce\": 0, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0, \"orange_juice\": 0}, \"note\": \"actual mode=crm_perdof with default norm (~1.42), NOT crm_default. Confirms catastrophic failure at uncontrolled correction magnitude.\"}, \"conclusion\": \"success\"}, \"eval-mag-perdof-norm005-object\": {\"metrics\": {\"overall_sr\": 0.14, \"successes\": 14, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10}, \"conclusion\": \"success\"}, \"eval-mag-perdof-norm003-object\": {\"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.14, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.1}}, \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm005-object\": {\"metrics\": {\"overall_sr\": 0.13, \"tasks_completed\": 10, \"total_rollouts\": 100, \"successes\": 13, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-obs-only-object-norm02-seed43-r2\": {\"metrics\": {\"overall_sr\": 0.16, \"successes\": 16, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}, \"vs_seed42\": \"-6pp (22% → 16%)\", \"vs_argmin_seed43\": \"-1pp (17% → 16%)\", \"pooled_2seed_obs_only_02\": \"19% (38/200)\", \"pooled_2seed_argmin\": \"14.5% (29/200)\"}, \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm03-object\": {\"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.19, \"successes\": 19, \"total\": 100}, \"conclusion\": \"success\"}, \"eval-vla-only-object-seed44-r2\": {\"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.1, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}, \"conclusion\": \"success\"}, \"eval-mag-perdof-norm02-object\": {\"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.11, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}, \"conclusion\": \"negative\"}, \"eval-acr-object-obs-only-default\": {\"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.17, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.5, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-scalar-object-seed43\": {\"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"avg_sr\": 10, \"per_task_sr\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 30, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 10, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 30, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 30}}, \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm003-object\": {\"metrics\": {\"overall_sr\": 0.16, \"tasks_done\": 100, \"tasks_total\": 100, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0.2, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.1, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.4, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_butter_and_place_it_in_the_basket\": 0.1, \"pick_up_the_milk_and_place_it_in_the_basket\": 0.2, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.3, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.3}}, \"conclusion\": \"success\"}, \"eval-scalar-object-seed44\": {\"conclusion\": \"failed\"}, \"eval-obs-only-object-norm02-seed44-r3\": {\"conclusion\": \"killed\"}, \"eval-argmin-object-seed44-r3\": {\"conclusion\": \"killed\"}, \"eval-vla-mean-object-seed43\": {\"metrics\": {\"overall_sr\": 0.15, \"tasks_done\": 10, \"tasks_total\": 10, \"total_success\": 15, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.3, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.1}}, \"conclusion\": \"success\"}, \"eval-perdof-object-seed43\": {\"metrics\": {\"overall_success_rate\": 0.12, \"tasks_done\": 10, \"tasks_total\": 10, \"total_rollouts\": 100, \"total_successes\": 12, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-vla-only-object-seed44\": {\"conclusion\": \"failed\"}, \"eval-obs-only-object-norm02-seed44\": {\"conclusion\": \"failed\"}, \"eval-argmin-object-seed44\": {\"conclusion\": \"failed\"}, \"eval-obs-only-object-seed43\": {\"metrics\": {\"overall_success_rate\": 0.12, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}, \"vs_argmin_seed43\": {\"obs_only\": 12, \"argmin\": 17, \"diff\": -5}, \"fisher_pooled\": {\"obs_only_total\": \"31/200\", \"argmin_total\": \"29/200\", \"pooled_obs_only_sr\": 0.155, \"pooled_argmin_sr\": 0.145, \"pooled_delta\": 0.01, \"odds_ratio\": 1.08, \"p_value_one_sided\": 0.4444, \"p_value_two_sided\": 0.8888}, \"source\": \"json_file_verified_by_worker\"}, \"conclusion\": \"negative\"}, \"eval-mag-obsonly-norm003-b2\": {\"metrics\": {\"overall_sr_10task\": 0.34, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task\": {\"between_plate_and_ramekin\": 0.9, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.8, \"on_stove\": 0, \"next_to_plate\": 0.3, \"on_wooden_cabinet\": 0}}, \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm03-b2\": {\"conclusion\": \"failed\"}, \"eval-argmin-object-seed43\": {\"metrics\": {\"overall_success_rate\": 0.17, \"total_successes\": 17, \"total_trials\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.3, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}, \"conclusion\": \"success\"}, \"eval-mag-perdof-norm02-seed43-object-r2\": {\"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm03\": {\"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm02-object\": {\"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm03-b4\": {\"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm03-b3\": {\"conclusion\": \"killed\"}, \"eval-mag-perdof-norm02-seed43-object\": {\"conclusion\": \"killed\"}, \"eval-mag-perdof-norm03-object-r2\": {\"conclusion\": \"killed\"}, \"eval-acr-object-v4-scalar-b2\": {\"conclusion\": \"killed\"}, \"eval-acr-object-v4-obs-only-b2\": {\"conclusion\": \"killed\"}, \"eval-spatial-v4-full\": {\"conclusion\": \"killed\"}, \"eval-reconvla-spatial-v1\": {\"conclusion\": \"killed\"}, \"eval-object-v6-full\": {\"conclusion\": \"killed\"}, \"precompute-v4-shard2\": {\"conclusion\": \"success\"}, \"precompute-v4-shard1\": {\"conclusion\": \"success\"}, \"precompute-v4-shard0\": {\"conclusion\": \"success\"}, \"precompute-v3-shard2\": {\"conclusion\": \"killed\"}, \"precompute-v3-shard1\": {\"conclusion\": \"killed\"}, \"precompute-v3-shard0\": {\"conclusion\": \"killed\"}, \"precompute-v2-shard2\": {\"conclusion\": \"killed\"}, \"precompute-v2-shard1\": {\"conclusion\": \"killed\"}, \"precompute-v2-shard0\": {\"conclusion\": \"killed\"}, \"eval-mag-perdof-norm0p3-object-r2\": {\"conclusion\": \"killed\"}, \"eval-vla-only-object-seed43\": {\"metrics\": {\"overall_sr\": 0.12, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}, \"source\": \"json_file_verified_by_worker\"}, \"conclusion\": \"success\"}, \"eval-mag-perdof-norm0p3-object\": {\"conclusion\": \"killed\"}, \"eval-obs-only-object-norm02-seed43\": {\"metrics\": {\"pid\": 118214, \"gpu\": 3, \"process_status\": \"alive\", \"log_file\": \"logs/eval_object_obs_only_norm02_seed43.log\"}, \"conclusion\": \"failed\"}, \"eval-acr-object-v4-default\": {\"metrics\": {\"tasks_done\": 3, \"tasks_total\": 10, \"status\": \"DEAD\", \"partial_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0}, \"pid_42311\": \"not_found\", \"needs_restart\": true, \"checked_at\": \"2026-05-16T01:00Z\"}, \"conclusion\": \"killed\"}, \"eval-acr-object-obs-only-norm02\": {\"metrics\": {\"overall_sr\": 0.22, \"total_success\": 22, \"total_rollouts\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.4, \"ketchup\": 0.2, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.6, \"orange_juice\": 0.3}}, \"conclusion\": \"success\"}, \"eval-mag-perdof-norm02\": {\"metrics\": {\"tasks_done\": \"6/10\", \"partial_results\": {\"T0_between_plate_ramekin\": \"60%\", \"T1_next_to_ramekin\": \"90%\", \"T2_table_center\": \"0%\", \"T3_on_cookie_box\": \"20%\", \"T4_top_drawer\": \"0%\", \"T5_on_ramekin\": \"0%\"}, \"running_avg_6task\": \"28.3%\", \"snapshot_time\": \"2026-05-15T09:00:00Z\", \"server\": \"bjb2-28827\", \"process_status\": \"alive\"}, \"conclusion\": \"failed\"}, \"eval-mag-perdof-norm005\": {\"metrics\": {\"T0_between_plate_ramekin\": 50, \"T1_next_to_ramekin\": 100, \"T2_table_center\": 0, \"T3_on_cookie_box\": 30, \"T4_top_drawer\": 0, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 100, \"T7_on_stove\": 0, \"T8_next_to_plate\": 30, \"T9_on_wooden_cabinet\": 0, \"avg_SR_10task\": 31}, \"conclusion\": \"negative\"}, \"eval-mag-obsonly-norm03-r2\": {\"metrics\": {\"bowl_between\": 0.9, \"next_to_ramekin\": 1, \"table_center\": 0, \"cookie_box\": 0.3, \"top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"stove\": 0, \"next_to_plate\": 0.3, \"wooden_cabinet\": 0, \"overall_SR\": 0.36}, \"conclusion\": \"success\"}, \"eval-mag-perdof-norm03\": {\"metrics\": {\"overall_sr_10task\": 0.26, \"T0_sr\": 0.7, \"T1_sr\": 0.5, \"T2_sr\": 0.1, \"T3_sr\": 0.1, \"T4_sr\": 0, \"T5_sr\": 0, \"T6_sr\": 0.9, \"T7_sr\": 0.1, \"T8_sr\": 0.2, \"T9_sr\": 0, \"total_successes\": 26, \"total_rollouts\": 100, \"benchmark\": \"spatial\", \"max_correction_norm\": 0.3}, \"conclusion\": \"negative\"}, \"eval-vla-mean-object\": {\"metrics\": {\"benchmark\": \"object\", \"mode\": \"vla_only\", \"baseline_mode\": \"mean\", \"n_rollouts\": 10, \"K\": 10, \"seed\": 42, \"overall_sr\": 12, \"total_success\": 12, \"total_rollouts\": 100, \"tasks_done\": \"10/10\", \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 10, \"bbq_sauce\": 30, \"ketchup\": 10, \"tomato_sauce\": 10, \"butter\": 0, \"milk\": 20, \"chocolate_pudding\": 30, \"orange_juice\": 10}, \"json_output\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean.json\"}, \"conclusion\": \"success\"}, \"eval-mag-perdof-norm003\": {\"metrics\": {\"benchmark\": \"spatial\", \"mode\": \"acr_vla\", \"max_correction_norm\": 0.03, \"n_rollouts\": 10, \"K\": 10, \"seed\": 42, \"overall_sr\": 30, \"total_success\": 30, \"total_rollouts\": 100, \"tasks_done\": \"10/10\", \"per_task\": {\"T0_between_plate_ramekin\": 60, \"T1_next_to_ramekin\": 100, \"T2_table_center\": 0, \"T3_on_cookie_box\": 30, \"T4_top_drawer\": 10, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 80, \"T7_on_stove\": 0, \"T8_next_to_plate\": 20, \"T9_on_wooden_cabinet\": 0}}, \"conclusion\": \"negative\"}, \"eval-reconvla-object\": {\"metrics\": {\"overall_sr\": 0.12, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}, \"n_rollouts\": 10, \"total_episodes\": 100, \"total_successes\": 12}, \"conclusion\": \"success\"}, \"eval-acr-object-v4-obs-only\": {\"metrics\": {\"overall_sr\": \"19.0% (19/100)\", \"total_success\": 19, \"total_rollouts\": 100, \"mode\": \"obs_only\", \"benchmark\": \"object\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"tasks_done\": \"10/10\", \"per_task\": {\"alphabet_soup\": \"0%\", \"cream_cheese\": \"10%\", \"salad_dressing\": \"20%\", \"bbq_sauce\": \"40%\", \"ketchup\": \"10%\", \"tomato_sauce\": \"0%\", \"butter\": \"10%\", \"milk\": \"20%\", \"chocolate_pudding\": \"50%\", \"orange_juice\": \"30%\"}, \"json_output\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json\"}, \"conclusion\": \"success\"}, \"eval-acr-object-v4-scalar\": {\"metrics\": {\"overall_sr\": 9, \"total_success\": 9, \"total_trials\": 100, \"n_tasks\": 10, \"n_rollouts_per_task\": 10, \"per_task\": {\"alphabet_soup\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"cream_cheese\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"salad_dressing\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"bbq_sauce\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"ketchup\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"tomato_sauce\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"butter\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"milk\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"chocolate_pudding\": {\"sr\": 30, \"success\": 3, \"trials\": 10}, \"orange_juice\": {\"sr\": 20, \"success\": 2, \"trials\": 10}}}, \"conclusion\": \"negative\"}, \"eval-mag-obsonly-norm02\": {\"metrics\": {\"T0_between_plate_ramekin\": 90, \"T1_next_to_ramekin\": 100, \"T2_table_center\": 0, \"T3_on_cookie_box\": 30, \"T4_top_drawer\": 10, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 90, \"T7_on_stove\": 0, \"T8_next_to_plate\": 30, \"T9_on_wooden_cabinet\": 0, \"overall_sr\": 35, \"total_success\": 35, \"total_rollouts\": 100}, \"conclusion\": \"negative\"}, \"eval-mag-obsonly-norm005\": {\"metrics\": {\"benchmark\": \"spatial\", \"mode\": \"crm_obs_only\", \"max_correction_norm\": 0.05, \"n_rollouts\": 10, \"K\": 10, \"overall_sr\": 35, \"total_success\": 35, \"total_episodes\": 100, \"per_task\": {\"T0_between_plate_ramekin\": 80, \"T1_next_to_ramekin\": 90, \"T2_table_center\": 0, \"T3_on_cookie_box\": 40, \"T4_top_drawer\": 10, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 80, \"T7_on_stove\": 0, \"T8_next_to_plate\": 50, \"T9_on_wooden_cabinet\": 0}}, \"conclusion\": \"success\"}, \"eval-acr-object-v4-perdof\": {\"metrics\": {\"overall_sr\": \"11.0% (11/100)\", \"total_success\": 11, \"total_rollouts\": 100, \"mode\": \"perdof\", \"benchmark\": \"object\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"alphabet_soup\": \"0%\", \"cream_cheese\": \"0%\", \"salad_dressing\": \"20%\", \"bbq_sauce\": \"30%\", \"ketchup\": \"0%\", \"tomato_sauce\": \"0%\", \"butter\": \"10%\", \"milk\": \"0%\", \"chocolate_pudding\": \"20%\", \"orange_juice\": \"30%\"}, \"note\": \"perdof object 11% vs argmin ~7% (partial). obs_only leads at ~14% (8/10). Confirms perdof not competitive on object.\"}, \"conclusion\": \"success\"}, \"eval-acr-spatial-v4-scalar-r2\": {\"metrics\": {\"overall_sr\": \"32.0% (32/100)\", \"total_success\": 32, \"total_rollouts\": 100, \"mode\": \"scalar_unc\", \"benchmark\": \"spatial\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"T0\": \"60%\", \"T1\": \"100%\", \"T2\": \"10%\", \"T3\": \"40%\", \"T4\": \"0%\", \"T5\": \"0%\", \"T6\": \"90%\", \"T7\": \"0%\", \"T8\": \"10%\", \"T9\": \"10%\"}, \"note\": \"D030 confirmed: scalar_unc spatial 32% vs argmin 34% = -2pp. T0-T2 from original eval-acr-spatial-v4-scalar, T3-T9 from r2 restart. All CRM variants dead on spatial.\"}, \"conclusion\": \"success\"}, \"eval-acr-spatial-v4-obs-only-r3\": {\"metrics\": {\"overall_sr\": \"35.0% (35/100)\", \"total_success\": 35, \"total_rollouts\": 100, \"mode\": \"crm_obs_only\", \"benchmark\": \"spatial\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"T0\": \"90%\", \"T1\": \"100%\", \"T2\": \"0%\", \"T3\": \"40%\", \"T4\": \"10%\", \"T5\": \"0%\", \"T6\": \"90%\", \"T7\": \"0%\", \"T8\": \"20%\", \"T9\": \"0%\"}, \"r3_subset_T6_T9\": \"27.5% (11/40)\", \"note\": \"D030: obs_only spatial 10-task = 35%. vs argmin 34% = +1pp. Scenario C threshold (>=39%) NOT MET. Earlier T0-T5 advantage (+5pp) wiped out by T6-T9.\"}, \"conclusion\": \"success\"}, \"eval-obs-only-spatial-seed43\": {\"conclusion\": \"failed\"}, \"eval-acr-spatial-v4-small-r2\": {\"metrics\": {\"overall_sr\": \"35.0% (35/100)\", \"total_success\": 35, \"total_rollouts\": 100, \"mode\": \"perdof\", \"benchmark\": \"spatial\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"T0\": \"60%\", \"T1\": \"100%\", \"T2\": \"10%\", \"T3\": \"40%\", \"T4\": \"0%\", \"T5\": \"0%\", \"T6\": \"90%\", \"T7\": \"10%\", \"T8\": \"40%\", \"T9\": \"0%\"}, \"note\": \"D029: perdof spatial complete 10-task = 35%. vs argmin 34% = +1pp. Kill criterion triggered — per-DOF claim dead on spatial.\"}, \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm-0.3-r3\": {\"conclusion\": \"killed\"}, \"eval-mag-obsonly-norm-0p3-r3\": {\"conclusion\": \"killed\"}, \"eval-argmin-only-spatial-r2\": {\"metrics\": {\"overall_success_rate\": 0.34, \"total_successes\": 34, \"total_trials\": 100, \"per_task\": {\"T0_between_plate_and_ramekin\": 0.6, \"T1_next_to_ramekin\": 1, \"T2_from_table_center\": 0, \"T3_on_cookie_box\": 0.3, \"T4_in_top_drawer\": 0.1, \"T5_on_ramekin\": 0.1, \"T6_next_to_cookie_box\": 0.9, \"T7_on_stove\": 0, \"T8_next_to_plate\": 0.3, \"T9_on_wooden_cabinet\": 0.1}, \"note\": \"T0-T8 from original run (eval-argmin-only-spatial), T9 from r2 restart. Combined 10-task result.\"}, \"conclusion\": \"success\"}, \"eval-mag-obsonly-norm003\": {\"conclusion\": \"killed\"}, \"eval-vla-only-object-k1\": {\"conclusion\": \"failed\"}, \"eval-acr-spatial-v4-obs-only-r2\": {\"metrics\": {\"tasks_done\": \"6/10\", \"partial_results\": {\"between_plate_and_ramekin\": \"90.0% (9/10)\", \"next_to_ramekin\": \"100.0% (10/10)\", \"from_table_center\": \"0.0% (0/10)\", \"on_cookie_box\": \"40.0% (4/10)\", \"in_top_drawer\": \"10.0% (1/10)\", \"on_ramekin\": \"0.0% (0/10)\"}, \"running_avg_6tasks\": \"40.0% (24/60)\", \"snapshot_time\": \"2026-05-15T12:00:00Z\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:0\", \"pid\": 270097}, \"conclusion\": \"failed\"}, \"eval-acr-spatial-v4-small\": {\"metrics\": {\"tasks_done\": \"7/10\", \"partial_results\": {\"between_plate_and_ramekin\": \"60.0% (6/10)\", \"next_to_ramekin\": \"100.0% (10/10)\", \"from_table_center\": \"10.0% (1/10)\", \"on_cookie_box\": \"40.0% (4/10)\", \"in_top_drawer\": \"0.0% (0/10)\", \"on_ramekin\": \"0.0% (0/10)\", \"next_to_cookie_box\": \"90.0% (9/10)\"}, \"running_avg_7tasks\": \"42.9% (30/70)\", \"snapshot_time\": \"2026-05-15T12:00:00Z\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:3\", \"pid\": 253085}, \"conclusion\": \"failed\"}, \"eval-acr-spatial-v4-scalar\": {\"metrics\": {\"tasks_done\": \"3/10\", \"partial_results\": {\"between_plate_and_ramekin\": \"60.0% (6/10)\", \"next_to_ramekin\": \"100.0% (10/10)\", \"from_table_center\": \"10.0% (1/10)\"}, \"running_avg_3tasks\": \"56.7% (17/30)\", \"snapshot_time\": \"2026-05-15T12:00:00Z\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:2\", \"pid\": 288939}, \"conclusion\": \"failed\"}, \"eval-argmin-only-spatial\": {\"metrics\": {\"tasks_done\": \"9/10\", \"partial_results\": {\"between_plate_and_ramekin\": \"60.0% (6/10)\", \"next_to_ramekin\": \"100.0% (10/10)\", \"from_table_center\": \"0.0% (0/10)\", \"on_cookie_box\": \"30.0% (3/10)\", \"in_top_drawer\": \"10.0% (1/10)\", \"on_ramekin\": \"10.0% (1/10)\", \"next_to_cookie_box\": \"90.0% (9/10)\", \"on_stove\": \"0.0% (0/10)\", \"next_to_plate\": \"30.0% (3/10)\"}, \"running_avg_9tasks\": \"36.7% (33/90)\", \"snapshot_time\": \"2026-05-15T12:00:00Z\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"pid\": 231421}, \"conclusion\": \"failed\"}, \"eval-vla-only-object\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.12, \"total_success\": 12, \"total_trials\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}}, \"eval-acr-spatial-v4-default-r3\": {\"conclusion\": \"killed\"}, \"eval-tiny-correction-spatial\": {\"metrics\": {\"tasks_done\": \"7/10\", \"partial_results\": {\"T1_between_plate_ramekin\": \"70% (7/10)\", \"T2_next_to_ramekin\": \"90% (9/10)\", \"T3_from_table_center\": \"0% (0/10)\", \"T4_on_cookie_box\": \"30% (3/10)\", \"T5_in_top_drawer\": \"0% (0/10)\", \"T6_on_ramekin\": \"0% (0/10)\", \"T7_next_to_cookie_box\": \"90% (9/10)\"}, \"running_avg_7tasks\": \"40% (28/70)\", \"process_status\": \"ACTUALLY ALIVE - bash wrapper PID 232815 dead but python child PID 232820 still running (07:48h, 139% CPU, 9.1GB RSS, GPU2)\", \"status_correction\": \"Registry incorrectly marked DONE, process is still completing remaining 3 tasks\", \"snapshot_time\": \"2026-05-15T09:40Z\"}, \"conclusion\": \"killed\"}, \"eval-vla-mean-spatial-t10\": {\"conclusion\": \"success\", \"metrics\": {\"T10_on_wooden_shelf\": \"10% (1/10)\", \"note\": \"Only ran task 9 (start_task=9). T10 = wooden shelf task.\"}}, \"eval-vla-mean-spatial\": {\"metrics\": {\"overall_success_rate_10tasks\": 0.32, \"total_successes\": 32, \"total_trials\": 100, \"T1\": 0.7, \"T2\": 1, \"T3\": 0, \"T4\": 0.3, \"T5\": 0, \"T6\": 0, \"T7\": 0.8, \"T8\": 0, \"T9\": 0.3, \"T10\": 0.1}, \"conclusion\": \"success\"}, \"eval-acr-spatial-v4-default-r2\": {\"conclusion\": \"killed\"}, \"eval-acr-spatial-v4-obs-only\": {\"conclusion\": \"failed\"}, \"eval-acr-spatial-v4-default\": {\"metrics\": {\"tasks_done\": \"0/10\", \"status_alert\": \"NO PROCESS FOUND - registry says RUNNING but no matching PID or tmux session on bjb1-18228. GPU 0 occupied by stale eval-acr-spatial-v3 tmux + crm-train-obs-only. NEEDS RESTART.\", \"snapshot_time\": \"2026-05-15T05:26Z\"}, \"conclusion\": \"failed\"}, \"crm-train-v3-norm-scalar-unc\": {\"metrics\": {\"best_epoch\": 46, \"best_val_loss\": 0.037354, \"final_train_loss\": 0.053422, \"final_val_loss\": 0.03737}, \"conclusion\": \"success\"}, \"crm-train-v3-norm-obs-only\": {\"metrics\": {\"best_epoch\": 48, \"best_val_loss\": 0.01645, \"final_train_loss\": 0.025576, \"final_val_loss\": 0.01645, \"total_epochs\": 50}, \"conclusion\": \"success\"}, \"eval-acr-object-v3\": {\"metrics\": {\"tasks_done\": \"4/10\", \"overall_success_rate\": 0, \"total_successes\": 0, \"total_rollouts\": 40, \"per_task_partial\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0, \"bbq_sauce\": 0}, \"snapshot_time\": \"2026-05-14T18:15Z\"}, \"conclusion\": \"failed\"}, \"eval-acr-spatial-v3\": {\"metrics\": {\"tasks_done\": \"4/10\", \"overall_success_rate\": 0.025, \"total_successes\": 1, \"total_rollouts\": 40, \"per_task_partial\": {\"pick_up_black_bowl_between_plate_and_ramekin\": 0.1, \"pick_up_black_bowl_next_to_ramekin\": 0, \"pick_up_black_bowl_from_table_center\": 0, \"pick_up_black_bowl_on_cookie_box\": 0}, \"snapshot_time\": \"2026-05-14T18:15Z\"}, \"conclusion\": \"failed\"}, \"crm-train-v3-norm\": {\"conclusion\": \"success\"}, \"crm-train-v3-scalar-unc\": {\"conclusion\": \"killed\", \"metrics\": {\"invalidation_reason\": \"Trained on bjb2 crm_cache v4 (6D state, pre-D016). Must retrain on bjb1 crm_cache_v5 (8D state).\", \"original_val_loss\": 1.195}}, \"crm-train-v3-obs-only\": {\"conclusion\": \"killed\", \"metrics\": {\"invalidation_reason\": \"Trained on bjb2 crm_cache v4 (6D state, pre-D016). Must retrain on bjb1 crm_cache_v5 (8D state).\", \"original_val_loss\": 1.193424}}, \"crm-train-v3-perdof\": {\"metrics\": {\"invalidation_reason\": \"Trained on bjb2 crm_cache v4 (6D state, pre-D016). Must retrain on bjb1 crm_cache_v5 (8D state).\", \"original_val_loss\": 1.191387}, \"conclusion\": \"killed\"}, \"eval-obs-only-spatial-v3\": {\"conclusion\": \"killed\"}, \"eval-scalar-unc-spatial-v2\": {\"conclusion\": \"killed\"}, \"eval-obs-only-spatial-v2\": {\"conclusion\": \"failed\"}, \"eval-obs-only-spatial\": {\"conclusion\": \"failed\", \"metrics\": {\"error\": \"size mismatch: obs_only CRM net.0.weight [256,990] vs acr_vla expects [256,1030] — no crm_obs_only mode in evaluate.py\"}}, \"crm-train-v2-obs-only\": {\"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.050501, \"best_epoch\": 50, \"total_epochs\": 50, \"final_train_loss\": 0.074839, \"comparison_vs_old\": \"old_6D_buggy=0.018312, new=0.050501 (loss metric changed with v2 fix)\"}}, \"crm-train-v2-scalar-unc\": {\"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.047202, \"best_epoch\": 48, \"total_epochs\": 50, \"final_train_loss\": 0.069679, \"comparison_vs_old\": \"old_6D_buggy=0.008379, new=0.047202 (loss metric changed with v2 fix)\"}}, \"crm-train-v2-perdof\": {\"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.051684, \"best_epoch\": 48, \"total_epochs\": 50, \"final_train_loss\": 0.076748, \"comparison_vs_old\": \"old_6D_buggy=0.009046, new=0.051684 (loss metric changed with v2 fix)\"}}, \"eval-reconvla-spatial-v3\": {\"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.34, \"total_successes\": 34, \"total_rollouts\": 100, \"per_task\": {\"pick_up_black_bowl_between_plate_and_ramekin\": 0.6, \"pick_up_black_bowl_next_to_ramekin\": 1, \"pick_up_black_bowl_from_table_center\": 0, \"pick_up_black_bowl_on_cookie_box\": 0.3, \"pick_up_black_bowl_in_top_drawer\": 0.1, \"pick_up_black_bowl_on_ramekin\": 0.1, \"pick_up_black_bowl_next_to_cookie_box\": 0.9, \"pick_up_black_bowl_on_stove\": 0, \"pick_up_black_bowl_next_to_plate\": 0.4, \"pick_up_black_bowl_on_wooden_cabinet\": 0}}}, \"precompute-v5-shard2\": {\"conclusion\": \"success\"}, \"precompute-v5-shard1\": {\"conclusion\": \"success\"}, \"precompute-v5-shard0\": {\"conclusion\": \"success\"}, \"crm-train-a4-scalar-unc\": {\"conclusion\": \"killed\", \"metrics\": {\"best_val_loss\": 0.008379, \"best_epoch\": 48, \"total_epochs\": 50, \"final_val_loss\": 0.008384, \"final_train_loss\": 0.012959}}, \"crm-train-a3-obs-only\": {\"conclusion\": \"killed\", \"metrics\": {\"best_val_loss\": 0.018312, \"best_epoch\": 4, \"early_stopped_at_epoch\": \"~15-20\", \"early_stop_reason\": \"val_loss plateau at 0.018 for 10+ epochs (full CRM: 0.009, 2x gap confirms conformal features are critical)\", \"input_dim\": 990, \"params\": 327966}}, \"crm-train-v1\": {\"conclusion\": \"killed\", \"metrics\": {\"best_val_loss\": 0.009046, \"best_epoch\": 50, \"total_epochs\": 50, \"checkpoint\": \"crm_best.pt\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm/crm_best.pt\", \"exit_code_note\": \"129 was false alarm - SIGHUP after training completed\"}}, \"crm-train-k5\": {\"conclusion\": \"killed\", \"metrics\": {\"best_val_loss\": 0.008996, \"best_epoch\": 50, \"total_epochs\": 50, \"comparison\": \"K=5 val_loss 0.008996 ≈ K=10 val_loss 0.009046, near identical\"}}, \"eval-scalar-unc-spatial\": {\"conclusion\": \"killed\"}, \"eval-acr-spatial-v2\": {\"conclusion\": \"killed\"}, \"eval-k5-spatial\": {\"conclusion\": \"killed\"}, \"eval-object-v8-full\": {\"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13, \"total_successes\": 13, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}}, \"eval-spatial-v7-full\": {\"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.3, \"total_successes\": 30, \"total_episodes\": 100, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"pick_up_black_bowl_between_plate_and_ramekin\": 0.6, \"pick_up_black_bowl_next_to_ramekin\": 1, \"pick_up_black_bowl_from_table_center\": 0, \"pick_up_black_bowl_on_cookie_box\": 0.2, \"pick_up_black_bowl_in_top_drawer\": 0, \"pick_up_black_bowl_on_ramekin\": 0, \"pick_up_black_bowl_next_to_cookie_box\": 0.9, \"pick_up_black_bowl_on_stove\": 0, \"pick_up_black_bowl_next_to_plate\": 0.3, \"pick_up_black_bowl_on_wooden_cabinet\": 0}}}, \"eval-object-v7-full\": {\"conclusion\": \"killed\"}, \"eval-spatial-v6-full\": {\"conclusion\": \"killed\"}, \"eval-object-v5-full\": {\"conclusion\": \"killed\"}, \"eval-acr-vla-spatial-v1\": {\"conclusion\": \"killed\"}, \"eval-acr-spatial-v1\": {\"conclusion\": \"killed\"}, \"eval-reconvla-spatial-v2\": {\"conclusion\": \"killed\"}, \"eval-object-v4-full\": {\"conclusion\": \"killed\"}, \"eval-spatial-v5-full\": {\"conclusion\": \"killed\"}, \"precompute-k5\": {\"conclusion\": \"success\", \"metrics\": {\"spatial_samples\": 12167, \"object_samples\": 14570, \"total_samples\": 26737, \"spatial_cache_mb\": 106, \"object_cache_mb\": 127, \"total_cache_mb\": 233, \"runtime_min\": 107}}, \"mvp-point-reaching\": {\"conclusion\": \"success\", \"metrics\": {\"group1_oracle\": {\"A_scalar\": {\"mse_x\": 0.180218, \"mse_y\": 0.02497, \"mse_z\": 0.024232, \"total\": 0.076473}, \"B_perDOF\": {\"mse_x\": 0.172652, \"mse_y\": 0.015544, \"mse_z\": 0.01561, \"total\": 0.067935}, \"C_none\": {\"mse_x\": 0.22706, \"mse_y\": 0.025542, \"mse_z\": 0.024753, \"total\": 0.092451}}, \"group2_oracle\": {\"A_scalar\": {\"mse_x\": 0.064642, \"mse_y\": 0.023836, \"mse_z\": 0.022967, \"total\": 0.037148}, \"B_perDOF\": {\"mse_x\": 0.053403, \"mse_y\": 0.015695, \"mse_z\": 0.01573, \"total\": 0.028276}, \"C_none\": {\"mse_x\": 0.084178, \"mse_y\": 0.025427, \"mse_z\": 0.024798, \"total\": 0.044801}}, \"group3_oracle\": {\"A_scalar\": {\"mse_x\": 0.042948, \"mse_y\": 0.023218, \"mse_z\": 0.022365, \"total\": 0.02951}, \"B_perDOF\": {\"mse_x\": 0.033008, \"mse_y\": 0.015621, \"mse_z\": 0.015647, \"total\": 0.021425}, \"C_none\": {\"mse_x\": 0.053043, \"mse_y\": 0.025523, \"mse_z\": 0.024741, \"total\": 0.034436}}, \"group4_K10\": {\"A_scalar\": {\"mse_x\": 0.187418, \"mse_y\": 0.024701, \"mse_z\": 0.024277, \"total\": 0.078799}, \"B_perDOF\": {\"mse_x\": 0.182888, \"mse_y\": 0.019072, \"mse_z\": 0.018475, \"total\": 0.073478}, \"C_none\": {\"mse_x\": 0.21507, \"mse_y\": 0.02496, \"mse_z\": 0.024637, \"total\": 0.088223}}, \"group5_K10\": {\"A_scalar\": {\"mse_x\": 0.064895, \"mse_y\": 0.02386, \"mse_z\": 0.023596, \"total\": 0.037451}, \"B_perDOF\": {\"mse_x\": 0.05851, \"mse_y\": 0.018868, \"mse_z\": 0.018471, \"total\": 0.03195}, \"C_none\": {\"mse_x\": 0.077047, \"mse_y\": 0.024825, \"mse_z\": 0.02464, \"total\": 0.042171}}, \"group6_K10\": {\"A_scalar\": {\"mse_x\": 0.041848, \"mse_y\": 0.02344, \"mse_z\": 0.023207, \"total\": 0.029498}, \"B_perDOF\": {\"mse_x\": 0.036348, \"mse_y\": 0.018736, \"mse_z\": 0.018453, \"total\": 0.024512}, \"C_none\": {\"mse_x\": 0.048365, \"mse_y\": 0.024827, \"mse_z\": 0.024577, \"total\": 0.03259}}, \"pass_criteria\": {\"group1\": \"PASS\", \"group4\": \"PASS\", \"overall\": \"SUCCESS\"}, \"summary_pct_improvements\": {\"reference_group\": \"group4_K10 (sigma=0.5/0.1/0.1, K=10 estimated uncertainty)\", \"perDOF_vs_scalar_total\": 6.75, \"perDOF_vs_none_total\": 16.71, \"perDOF_vs_scalar_y_axis\": 22.79, \"perDOF_vs_scalar_z_axis\": 23.9, \"paper_claims\": {\"6.7_pct_over_scalar\": \"group4 total: (0.078799-0.073478)/0.078799 = 6.75%\", \"16.7_pct_over_none\": \"group4 total: (0.088223-0.073478)/0.088223 = 16.71%\", \"22_24_pct_per_axis\": \"group4 y: 22.79%, z: 23.90%\"}}}}, \"eval-spatial-v3-full\": {\"conclusion\": \"killed\"}, \"eval-spatial-reeval-v2\": {\"conclusion\": \"killed\"}, \"eval-smolvla-libero-spatial\": {\"conclusion\": \"failed\"}, \"precompute-shard2\": {\"conclusion\": \"success\"}, \"precompute-shard1\": {\"conclusion\": \"success\"}, \"precompute-shard0\": {\"conclusion\": \"success\"}, \"plan_014-reconvla-baseline\": {\"conclusion\": \"failed\"}, \"plan_001-crm-smolvla\": {\"conclusion\": \"failed\"}}, \"count\": 137, \"total\": 137, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.366}}"
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
Now I have all the data I need. Let me compile the magnitude curve JSON. I found:

**Object Benchmark (seed=42) - Magnitude Curve:**

obs_only:
- norm 0.03: `eval-mag-obsonly-norm003-object` → 16% (16/100)
- norm 0.05: `eval-mag-obsonly-norm005-object` → 13% (13/100)
- norm 0.10: `eval-acr-object-v4-obs-only` → 19% (19/100)
- norm 0.20: `eval-acr-object-obs-only-norm02` → 22% (22/100)


- norm 0.30: `eval-mag-obsonly-norm03-object` → 19% (19/100)
- default (~1.42): `eval-acr-object-obs-only-default` → 17% (17/100)

perdof:
- norm 0.03: `eval-mag-perdof-norm003-object` → 14% (14/100)
- norm 0.05: `eval-mag-perdof-norm005-object` → 14% (14/100)
- norm 0.10: `eval-acr-object-v4-perdof` → 11% (11/100)
- norm 0.20: `eval-mag-perdof-norm02-object` → 11% (11/100)
- norm 0.30: `eval-mag-perdof-norm03-object-r3` → 4% (4/100)
- default (~1.42): `eval-acr-object-v4-default-r2` → 0% (0/100)

Now I'm looking at how different seeds affect performance with the obs_only norm=0.2 configuration, where seed42 achieves 22% compared to seeds 43 and 44 at 16% each. I'm also comparing this against argmin approaches without CRM, which show notably lower performance around 12%.

Checking the obs_only norm=0.1 and perdof norm=0.1 variants across seeds, I see seed42 consistently performs better or comparably to the other seeds, with most configurations landing in the 11-19% range.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "bf6b68ef-9dc3-476d-8cff-fbfc84a88f45",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XkXdJ9cn24UMaScsmCfCzu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16652,
      "cache_read_input_tokens": 28599,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16652
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

_source line 67_

I have all the data. Now I'll write both artifacts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "ef5ef186-d78f-4e7e-8026-2ded3ecd80f6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XkXdJ9cn24UMaScsmCfCzu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16652,
      "cache_read_input_tokens": 28599,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16652
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

_source line 68_

<details open><summary>🔧 Tool call — Write · `toolu_01AJWYpK9A853zX58JJxkCmC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/magnitude_curve_data.json",
  "content": "{\n  \"metadata\": {\n    \"benchmark\": \"LIBERO Object\",\n    \"n_tasks\": 10,\n    \"n_rollouts_per_task\": 10,\n    \"total_per_seed\": 100,\n    \"compiled_date\": \"2026-05-16\"\n  },\n  \"magnitude_curve\": {\n    \"obs_only\": [\n      {\"norm\": 0.03, \"sr\": 0.16, \"successes\": 16, \"total\": 100, \"exp_id\": \"eval-mag-obsonly-norm003-object\", \"seed\": 42},\n      {\"norm\": 0.05, \"sr\": 0.13, \"successes\": 13, \"total\": 100, \"exp_id\": \"eval-mag-obsonly-norm005-object\", \"seed\": 42},\n      {\"norm\": 0.10, \"sr\": 0.19, \"successes\": 19, \"total\": 100, \"exp_id\": \"eval-acr-object-v4-obs-only\", \"seed\": 42},\n      {\"norm\": 0.20, \"sr\": 0.22, \"successes\": 22, \"total\": 100, \"exp_id\": \"eval-acr-object-obs-only-norm02\", \"seed\": 42},\n      {\"norm\": 0.30, \"sr\": 0.19, \"successes\": 19, \"total\": 100, \"exp_id\": \"eval-mag-obsonly-norm03-object\", \"seed\": 42},\n      {\"norm\": 1.42, \"sr\": 0.17, \"successes\": 17, \"total\": 100, \"exp_id\": \"eval-acr-object-obs-only-default\", \"seed\": 42, \"note\": \"default norm, no clipping\"}\n    ],\n    \"perdof\": [\n      {\"norm\": 0.03, \"sr\": 0.14, \"successes\": 14, \"total\": 100, \"exp_id\": \"eval-mag-perdof-norm003-object\", \"seed\": 42},\n      {\"norm\": 0.05, \"sr\": 0.14, \"successes\": 14, \"total\": 100, \"exp_id\": \"eval-mag-perdof-norm005-object\", \"seed\": 42},\n      {\"norm\": 0.10, \"sr\": 0.11, \"successes\": 11, \"total\": 100, \"exp_id\": \"eval-acr-object-v4-perdof\", \"seed\": 42},\n      {\"norm\": 0.20, \"sr\": 0.11, \"successes\": 11, \"total\": 100, \"exp_id\": \"eval-mag-perdof-norm02-object\", \"seed\": 42},\n      {\"norm\": 0.30, \"sr\": 0.04, \"successes\": 4, \"total\": 100, \"exp_id\": \"eval-mag-perdof-norm03-object-r3\", \"seed\": 42},\n      {\"norm\": 1.42, \"sr\": 0.00, \"successes\": 0, \"total\": 100, \"exp_id\": \"eval-acr-object-v4-default-r2\", \"seed\": 42, \"note\": \"default norm, catastrophic failure\"}\n    ]\n  },\n  \"magnitude_curve_spatial\": {\n    \"obs_only\": [\n      {\"norm\": 0.03, \"sr\": 0.34, \"successes\": 34, \"total\": 100, \"exp_id\": \"eval-mag-obsonly-norm003-b2\", \"seed\": 42},\n      {\"norm\": 0.05, \"sr\": 0.35, \"successes\": 35, \"total\": 100, \"exp_id\": \"eval-mag-obsonly-norm005\", \"seed\": 42},\n      {\"norm\": 0.10, \"sr\": 0.35, \"successes\": 35, \"total\": 100, \"exp_id\": \"eval-acr-spatial-v4-obs-only-r3\", \"seed\": 42},\n      {\"norm\": 0.20, \"sr\": 0.35, \"successes\": 35, \"total\": 100, \"exp_id\": \"eval-mag-obsonly-norm02\", \"seed\": 42},\n      {\"norm\": 0.30, \"sr\": 0.36, \"successes\": 36, \"total\": 100, \"exp_id\": \"eval-mag-obsonly-norm03-r2\", \"seed\": 42}\n    ],\n    \"perdof\": [\n      {\"norm\": 0.03, \"sr\": 0.30, \"successes\": 30, \"total\": 100, \"exp_id\": \"eval-mag-perdof-norm003\", \"seed\": 42},\n      {\"norm\": 0.05, \"sr\": 0.31, \"successes\": 31, \"total\": 100, \"exp_id\": \"eval-mag-perdof-norm005\", \"seed\": 42},\n      {\"norm\": 0.10, \"sr\": 0.35, \"successes\": 35, \"total\": 100, \"exp_id\": \"eval-acr-spatial-v4-small-r2\", \"seed\": 42},\n      {\"norm\": 0.30, \"sr\": 0.26, \"successes\": 26, \"total\": 100, \"exp_id\": \"eval-mag-perdof-norm03\", \"seed\": 42}\n    ]\n  },\n  \"baselines\": {\n    \"object\": {\n      \"argmin_seed42\": {\"sr\": 0.12, \"successes\": 12, \"total\": 100, \"exp_id\": \"eval-reconvla-object\", \"seed\": 42},\n      \"vla_only_seed42\": {\"sr\": 0.12, \"successes\": 12, \"total\": 100, \"exp_id\": \"eval-vla-only-object\", \"seed\": 42},\n      \"vla_mean_seed42\": {\"sr\": 0.12, \"successes\": 12, \"total\": 100, \"exp_id\": \"eval-vla-mean-object\", \"seed\": 42}\n    },\n    \"spatial\": {\n      \"argmin_seed42\": {\"sr\": 0.34, \"successes\": 34, \"total\": 100, \"exp_id\": \"eval-argmin-only-spatial-r2\", \"seed\": 42},\n      \"vla_only_seed42\": {\"sr\": 0.30, \"successes\": 30, \"total\": 100, \"exp_id\": \"eval-spatial-v7-full\", \"seed\": 42},\n      \"vla_mean_seed42\": {\"sr\": 0.32, \"successes\": 32, \"total\": 100, \"exp_id\": \"eval-vla-mean-spatial\", \"seed\": 42}\n    }\n  },\n  \"seed_comparison\": {\n    \"obs_only_norm02\": [\n      {\"seed\": 42, \"sr\": 0.22, \"successes\": 22, \"total\": 100, \"exp_id\": \"eval-acr-object-obs-only-norm02\"},\n      {\"seed\": 43, \"sr\": 0.16, \"successes\": 16, \"total\": 100, \"exp_id\": \"eval-obs-only-object-norm02-seed43-r2\"},\n      {\"seed\": 44, \"sr\": 0.16, \"successes\": 16, \"total\": 100, \"exp_id\": \"eval-obs-only-object-norm02-seed44-r2\"}\n    ],\n    \"obs_only_norm01\": [\n      {\"seed\": 42, \"sr\": 0.19, \"successes\": 19, \"total\": 100, \"exp_id\": \"eval-acr-object-v4-obs-only\"},\n      {\"seed\": 43, \"sr\": 0.12, \"successes\": 12, \"total\": 100, \"exp_id\": \"eval-obs-only-object-seed43\"}\n    ],\n    \"argmin\": [\n      {\"seed\": 42, \"sr\": 0.12, \"successes\": 12, \"total\": 100, \"exp_id\": \"eval-reconvla-object\"},\n      {\"seed\": 43, \"sr\": 0.17, \"successes\": 17, \"total\": 100, \"exp_id\": \"eval-argmin-object-seed43\"},\n      {\"seed\": 44, \"sr\": 0.13, \"successes\": 13, \"total\": 100, \"exp_id\": \"eval-argmin-object-seed44-r2\"}\n    ],\n    \"perdof_norm01\": [\n      {\"seed\": 42, \"sr\": 0.11, \"successes\": 11, \"total\": 100, \"exp_id\": \"eval-acr-object-v4-perdof\"},\n      {\"seed\": 43, \"sr\": 0.12, \"successes\": 12, \"total\": 100, \"exp_id\": \"eval-perdof-object-seed43\"}\n    ],\n    \"perdof_norm02\": [\n      {\"seed\": 42, \"sr\": 0.11, \"successes\": 11, \"total\": 100, \"exp_id\": \"eval-mag-perdof-norm02-object\"},\n      {\"seed\": 43, \"sr\": 0.09, \"successes\": 9, \"total\": 100, \"exp_id\": \"eval-mag-perdof-norm02-seed43-object-r3\"}\n    ],\n    \"vla_only\": [\n      {\"seed\": 42, \"sr\": 0.12, \"successes\": 12, \"total\": 100, \"exp_id\": \"eval-vla-only-object\"},\n      {\"seed\": 43, \"sr\": 0.12, \"successes\": 12, \"total\": 100, \"exp_id\": \"eval-vla-only-object-seed43\"},\n      {\"seed\": 44, \"sr\": 0.10, \"successes\": 10, \"total\": 100, \"exp_id\": \"eval-vla-only-object-seed44-r2\"}\n    ],\n    \"vla_mean\": [\n      {\"seed\": 42, \"sr\": 0.12, \"successes\": 12, \"total\": 100, \"exp_id\": \"eval-vla-mean-object\"},\n      {\"seed\": 43, \"sr\": 0.15, \"successes\": 15, \"total\": 100, \"exp_id\": \"eval-vla-mean-object-seed43\"},\n      {\"seed\": 44, \"sr\": 0.10, \"successes\": 10, \"total\": 100, \"exp_id\": \"eval-vla-mean-object-seed44\"}\n    ]\n  }\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "ac244f6b-7238-479f-a1d2-abca1ef09f77",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XkXdJ9cn24UMaScsmCfCzu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16652,
      "cache_read_input_tokens": 28599,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16652
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

_source line 69 · 2026-05-16T19:00:31.225Z_

<details><summary>↩ Tool result · `toolu_01AJWYpK9A853zX58JJxkCmC`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/magnitude_curve_data.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "4aa07976-9b76-449d-92c7-3e5c4f24ab9d",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/magnitude_curve_data.json",
    "content": "{\n  \"metadata\": {\n    \"benchmark\": \"LIBERO Object\",\n    \"n_tasks\": 10,\n    \"n_rollouts_per_task\": 10,\n    \"total_per_seed\": 100,\n    \"compiled_date\": \"2026-05-16\"\n  },\n  \"magnitude_curve\": {\n    \"obs_only\": [\n      {\"norm\": 0.03, \"sr\": 0.16, \"successes\": 16, \"total\": 100, \"exp_id\": \"eval-mag-obsonly-norm003-object\", \"seed\": 42},\n      {\"norm\": 0.05, \"sr\": 0.13, \"successes\": 13, \"total\": 100, \"exp_id\": \"eval-mag-obsonly-norm005-object\", \"seed\": 42},\n      {\"norm\": 0.10, \"sr\": 0.19, \"successes\": 19, \"total\": 100, \"exp_id\": \"eval-acr-object-v4-obs-only\", \"seed\": 42},\n      {\"norm\": 0.20, \"sr\": 0.22, \"successes\": 22, \"total\": 100, \"exp_id\": \"eval-acr-object-obs-only-norm02\", \"seed\": 42},\n      {\"norm\": 0.30, \"sr\": 0.19, \"successes\": 19, \"total\": 100, \"exp_id\": \"eval-mag-obsonly-norm03-object\", \"seed\": 42},\n      {\"norm\": 1.42, \"sr\": 0.17, \"successes\": 17, \"total\": 100, \"exp_id\": \"eval-acr-object-obs-only-default\", \"seed\": 42, \"note\": \"default norm, no clipping\"}\n    ],\n    \"perdof\": [\n      {\"norm\": 0.03, \"sr\": 0.14, \"successes\": 14, \"total\": 100, \"exp_id\": \"eval-mag-perdof-norm003-object\", \"seed\": 42},\n      {\"norm\": 0.05, \"sr\": 0.14, \"successes\": 14, \"total\": 100, \"exp_id\": \"eval-mag-perdof-norm005-object\", \"seed\": 42},\n      {\"norm\": 0.10, \"sr\": 0.11, \"successes\": 11, \"total\": 100, \"exp_id\": \"eval-acr-object-v4-perdof\", \"seed\": 42},\n      {\"norm\": 0.20, \"sr\": 0.11, \"successes\": 11, \"total\": 100, \"exp_id\": \"eval-mag-perdof-norm02-object\", \"seed\": 42},\n      {\"norm\": 0.30, \"sr\": 0.04, \"successes\": 4, \"total\": 100, \"exp_id\": \"eval-mag-perdof-norm03-object-r3\", \"seed\": 42},\n      {\"norm\": 1.42, \"sr\": 0.00, \"successes\": 0, \"total\": 100, \"exp_id\": \"eval-acr-object-v4-default-r2\", \"seed\": 42, \"note\": \"default norm, catastrophic failure\"}\n    ]\n  },\n  \"magnitude_curve_spatial\": {\n    \"obs_only\": [\n      {\"norm\": 0.03, \"sr\": 0.34, \"successes\": 34, \"total\": 100, \"exp_id\": \"eval-mag-obsonly-norm003-b2\", \"seed\": 42},\n      {\"norm\": 0.05, \"sr\": 0.35, \"successes\": 35, \"total\": 100, \"exp_id\": \"eval-mag-obsonly-norm005\", \"seed\": 42},\n      {\"norm\": 0.10, \"sr\": 0.35, \"successes\": 35, \"total\": 100, \"exp_id\": \"eval-acr-spatial-v4-obs-only-r3\", \"seed\": 42},\n      {\"norm\": 0.20, \"sr\": 0.35, \"successes\": 35, \"total\": 100, \"exp_id\": \"eval-mag-obsonly-norm02\", \"seed\": 42},\n      {\"norm\": 0.30, \"sr\": 0.36, \"successes\": 36, \"total\": 100, \"exp_id\": \"eval-mag-obsonly-norm03-r2\", \"seed\": 42}\n    ],\n    \"perdof\": [\n      {\"norm\": 0.03, \"sr\": 0.30, \"successes\": 30, \"total\": 100, \"exp_id\": \"eval-mag-perdof-norm003\", \"seed\": 42},\n      {\"norm\": 0.05, \"sr\": 0.31, \"successes\": 31, \"total\": 100, \"exp_id\": \"eval-mag-perdof-norm005\", \"seed\": 42},\n      {\"norm\": 0.10, \"sr\": 0.35, \"successes\": 35, \"total\": 100, \"exp_id\": \"eval-acr-spatial-v4-small-r2\", \"seed\": 42},\n      {\"norm\": 0.30, \"sr\": 0.26, \"successes\": 26, \"total\": 100, \"exp_id\": \"eval-mag-perdof-norm03\", \"seed\": 42}\n    ]\n  },\n  \"baselines\": {\n    \"object\": {\n      \"argmin_seed42\": {\"sr\": 0.12, \"successes\": 12, \"total\": 100, \"exp_id\": \"eval-reconvla-object\", \"seed\": 42},\n      \"vla_only_seed42\": {\"sr\": 0.12, \"successes\": 12, \"total\": 100, \"exp_id\": \"eval-vla-only-object\", \"seed\": 42},\n      \"vla_mean_seed42\": {\"sr\": 0.12, \"successes\": 12, \"total\": 100, \"exp_id\": \"eval-vla-mean-object\", \"seed\": 42}\n    },\n    \"spatial\": {\n      \"argmin_seed42\": {\"sr\": 0.34, \"successes\": 34, \"total\": 100, \"exp_id\": \"eval-argmin-only-spatial-r2\", \"seed\": 42},\n      \"vla_only_seed42\": {\"sr\": 0.30, \"successes\": 30, \"total\": 100, \"exp_id\": \"eval-spatial-v7-full\", \"seed\": 42},\n      \"vla_mean_seed42\": {\"sr\": 0.32, \"successes\": 32, \"total\": 100, \"exp_id\": \"eval-vla-mean-spatial\", \"seed\": 42}\n    }\n  },\n  \"seed_comparison\": {\n    \"obs_only_norm02\": [\n      {\"seed\": 42, \"sr\": 0.22, \"successes\": 22, \"total\": 100, \"exp_id\": \"eval-acr-object-obs-only-norm02\"},\n      {\"seed\": 43, \"sr\": 0.16, \"successes\": 16, \"total\": 100, \"exp_id\": \"eval-obs-only-object-norm02-seed43-r2\"},\n      {\"seed\": 44, \"sr\": 0.16, \"successes\": 16, \"total\": 100, \"exp_id\": \"eval-obs-only-object-norm02-seed44-r2\"}\n    ],\n    \"obs_only_norm01\": [\n      {\"seed\": 42, \"sr\": 0.19, \"successes\": 19, \"total\": 100, \"exp_id\": \"eval-acr-object-v4-obs-only\"},\n      {\"seed\": 43, \"sr\": 0.12, \"successes\": 12, \"total\": 100, \"exp_id\": \"eval-obs-only-object-seed43\"}\n    ],\n    \"argmin\": [\n      {\"seed\": 42, \"sr\": 0.12, \"successes\": 12, \"total\": 100, \"exp_id\": \"eval-reconvla-object\"},\n      {\"seed\": 43, \"sr\": 0.17, \"successes\": 17, \"total\": 100, \"exp_id\": \"eval-argmin-object-seed43\"},\n      {\"seed\": 44, \"sr\": 0.13, \"successes\": 13, \"total\": 100, \"exp_id\": \"eval-argmin-object-seed44-r2\"}\n    ],\n    \"perdof_norm01\": [\n      {\"seed\": 42, \"sr\": 0.11, \"successes\": 11, \"total\": 100, \"exp_id\": \"eval-acr-object-v4-perdof\"},\n      {\"seed\": 43, \"sr\": 0.12, \"successes\": 12, \"total\": 100, \"exp_id\": \"eval-perdof-object-seed43\"}\n    ],\n    \"perdof_norm02\": [\n      {\"seed\": 42, \"sr\": 0.11, \"successes\": 11, \"total\": 100, \"exp_id\": \"eval-mag-perdof-norm02-object\"},\n      {\"seed\": 43, \"sr\": 0.09, \"successes\": 9, \"total\": 100, \"exp_id\": \"eval-mag-perdof-norm02-seed43-object-r3\"}\n    ],\n    \"vla_only\": [\n      {\"seed\": 42, \"sr\": 0.12, \"successes\": 12, \"total\": 100, \"exp_id\": \"eval-vla-only-object\"},\n      {\"seed\": 43, \"sr\": 0.12, \"successes\": 12, \"total\": 100, \"exp_id\": \"eval-vla-only-object-seed43\"},\n      {\"seed\": 44, \"sr\": 0.10, \"successes\": 10, \"total\": 100, \"exp_id\": \"eval-vla-only-object-seed44-r2\"}\n    ],\n    \"vla_mean\": [\n      {\"seed\": 42, \"sr\": 0.12, \"successes\": 12, \"total\": 100, \"exp_id\": \"eval-vla-mean-object\"},\n      {\"seed\": 43, \"sr\": 0.15, \"successes\": 15, \"total\": 100, \"exp_id\": \"eval-vla-mean-object-seed43\"},\n      {\"seed\": 44, \"sr\": 0.10, \"successes\": 10, \"total\": 100, \"exp_id\": \"eval-vla-mean-object-seed44\"}\n    ]\n  }\n}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 70_

<details open><summary>🔧 Tool call — Write · `toolu_01K8Q3eeED4zfD3nGgka43bM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/pooled_fisher_test_v2.py",
  "content": "#!/usr/bin/env python3\n\"\"\"Pooled Fisher exact test for multi-seed comparisons.\n\nReads actual counts from magnitude_curve_data.json — never hardcodes n_rollouts.\nSupports 2/3/4/5 seed pooled analysis via --seeds argument.\n\nUsage:\n    python pooled_fisher_test_v2.py --data magnitude_curve_data.json --method1 obs_only_norm02 --method2 argmin\n    python pooled_fisher_test_v2.py --data magnitude_curve_data.json --method1 obs_only_norm02 --method2 argmin --seeds 42 43 44\n\"\"\"\n\nimport argparse\nimport json\nimport sys\nfrom scipy.stats import fisher_exact\nimport numpy as np\n\n\ndef load_data(json_path: str) -> dict:\n    with open(json_path) as f:\n        return json.load(f)\n\n\ndef get_method_data(data: dict, method_key: str) -> list[dict]:\n    \"\"\"Get seed-level data for a method from seed_comparison section.\"\"\"\n    seed_comp = data.get(\"seed_comparison\", {})\n    if method_key not in seed_comp:\n        available = list(seed_comp.keys())\n        print(f\"Error: method '{method_key}' not found. Available: {available}\", file=sys.stderr)\n        sys.exit(1)\n    return seed_comp[method_key]\n\n\ndef pool_counts(entries: list[dict], seeds: list[int] | None = None) -> tuple[int, int]:\n    \"\"\"Pool successes and totals across specified seeds.\"\"\"\n    filtered = entries\n    if seeds is not None:\n        filtered = [e for e in entries if e[\"seed\"] in seeds]\n        found_seeds = {e[\"seed\"] for e in filtered}\n        missing = set(seeds) - found_seeds\n        if missing:\n            print(f\"Warning: seeds {missing} not found in data (available: {[e['seed'] for e in entries]})\", file=sys.stderr)\n    total_successes = sum(e[\"successes\"] for e in filtered)\n    total_trials = sum(e[\"total\"] for e in filtered)\n    return total_successes, total_trials\n\n\ndef fisher_test_pooled(s1: int, n1: int, s2: int, n2: int) -> dict:\n    \"\"\"Run Fisher exact test on pooled 2x2 contingency table.\n\n    Table:\n              success  failure\n    method1:    s1     n1 - s1\n    method2:    s2     n2 - s2\n    \"\"\"\n    table = np.array([[s1, n1 - s1], [s2, n2 - s2]])\n    or_two, p_two = fisher_exact(table, alternative='two-sided')\n    or_greater, p_greater = fisher_exact(table, alternative='greater')\n    or_less, p_less = fisher_exact(table, alternative='less')\n    return {\n        \"contingency_table\": table.tolist(),\n        \"method1_sr\": s1 / n1 if n1 > 0 else 0,\n        \"method2_sr\": s2 / n2 if n2 > 0 else 0,\n        \"delta_pp\": (s1 / n1 - s2 / n2) * 100 if n1 > 0 and n2 > 0 else 0,\n        \"odds_ratio\": or_two,\n        \"p_two_sided\": p_two,\n        \"p_greater\": p_greater,\n        \"p_less\": p_less,\n    }\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"Pooled Fisher exact test from JSON data\")\n    parser.add_argument(\"--data\", required=True, help=\"Path to magnitude_curve_data.json\")\n    parser.add_argument(\"--method1\", required=True, help=\"First method key in seed_comparison\")\n    parser.add_argument(\"--method2\", required=True, help=\"Second method key in seed_comparison\")\n    parser.add_argument(\"--seeds\", nargs=\"+\", type=int, default=None,\n                        help=\"Which seeds to include (default: all available)\")\n    args = parser.parse_args()\n\n    data = load_data(args.data)\n    entries1 = get_method_data(data, args.method1)\n    entries2 = get_method_data(data, args.method2)\n\n    s1, n1 = pool_counts(entries1, args.seeds)\n    s2, n2 = pool_counts(entries2, args.seeds)\n\n    seeds_used = args.seeds if args.seeds else sorted({e[\"seed\"] for e in entries1})\n    n_seeds = len(seeds_used)\n\n    print(f\"{'='*60}\")\n    print(f\"Pooled Fisher Exact Test ({n_seeds}-seed)\")\n    print(f\"{'='*60}\")\n    print(f\"Method 1: {args.method1}\")\n    print(f\"  Seeds: {seeds_used}\")\n    print(f\"  Pooled: {s1}/{n1} = {s1/n1:.1%}\")\n    for e in entries1:\n        if args.seeds is None or e[\"seed\"] in args.seeds:\n            print(f\"    seed{e['seed']}: {e['successes']}/{e['total']} ({e['exp_id']})\")\n    print(f\"Method 2: {args.method2}\")\n    print(f\"  Seeds: {sorted({e['seed'] for e in entries2 if args.seeds is None or e['seed'] in args.seeds})}\")\n    print(f\"  Pooled: {s2}/{n2} = {s2/n2:.1%}\")\n    for e in entries2:\n        if args.seeds is None or e[\"seed\"] in args.seeds:\n            print(f\"    seed{e['seed']}: {e['successes']}/{e['total']} ({e['exp_id']})\")\n    print()\n\n    result = fisher_test_pooled(s1, n1, s2, n2)\n\n    print(f\"Contingency table:\")\n    print(f\"              success  failure\")\n    print(f\"  {args.method1:20s}  {s1:>5d}  {n1-s1:>5d}\")\n    print(f\"  {args.method2:20s}  {s2:>5d}  {n2-s2:>5d}\")\n    print()\n    print(f\"Delta: {result['delta_pp']:+.1f} pp ({args.method1} - {args.method2})\")\n    print(f\"Odds ratio: {result['odds_ratio']:.4f}\")\n    print(f\"p (two-sided): {result['p_two_sided']:.4f}\")\n    print(f\"p (method1 > method2): {result['p_greater']:.4f}\")\n    print(f\"p (method1 < method2): {result['p_less']:.4f}\")\n    print()\n\n    alpha = 0.05\n    sig = \"SIGNIFICANT\" if result['p_two_sided'] < alpha else \"NOT significant\"\n    print(f\"At alpha={alpha}: {sig}\")\n    print(f\"{'='*60}\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "706e8b95-7214-438f-901e-e2b2464e0683",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XkXdJ9cn24UMaScsmCfCzu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16652,
      "cache_read_input_tokens": 28599,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16652
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

_source line 71 · 2026-05-16T19:00:54.360Z_

<details><summary>↩ Tool result · `toolu_01K8Q3eeED4zfD3nGgka43bM`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/pooled_fisher_test_v2.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "ce600d97-9571-40bb-b7db-7e949e6ec27d",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/pooled_fisher_test_v2.py",
    "content": "#!/usr/bin/env python3\n\"\"\"Pooled Fisher exact test for multi-seed comparisons.\n\nReads actual counts from magnitude_curve_data.json — never hardcodes n_rollouts.\nSupports 2/3/4/5 seed pooled analysis via --seeds argument.\n\nUsage:\n    python pooled_fisher_test_v2.py --data magnitude_curve_data.json --method1 obs_only_norm02 --method2 argmin\n    python pooled_fisher_test_v2.py --data magnitude_curve_data.json --method1 obs_only_norm02 --method2 argmin --seeds 42 43 44\n\"\"\"\n\nimport argparse\nimport json\nimport sys\nfrom scipy.stats import fisher_exact\nimport numpy as np\n\n\ndef load_data(json_path: str) -> dict:\n    with open(json_path) as f:\n        return json.load(f)\n\n\ndef get_method_data(data: dict, method_key: str) -> list[dict]:\n    \"\"\"Get seed-level data for a method from seed_comparison section.\"\"\"\n    seed_comp = data.get(\"seed_comparison\", {})\n    if method_key not in seed_comp:\n        available = list(seed_comp.keys())\n        print(f\"Error: method '{method_key}' not found. Available: {available}\", file=sys.stderr)\n        sys.exit(1)\n    return seed_comp[method_key]\n\n\ndef pool_counts(entries: list[dict], seeds: list[int] | None = None) -> tuple[int, int]:\n    \"\"\"Pool successes and totals across specified seeds.\"\"\"\n    filtered = entries\n    if seeds is not None:\n        filtered = [e for e in entries if e[\"seed\"] in seeds]\n        found_seeds = {e[\"seed\"] for e in filtered}\n        missing = set(seeds) - found_seeds\n        if missing:\n            print(f\"Warning: seeds {missing} not found in data (available: {[e['seed'] for e in entries]})\", file=sys.stderr)\n    total_successes = sum(e[\"successes\"] for e in filtered)\n    total_trials = sum(e[\"total\"] for e in filtered)\n    return total_successes, total_trials\n\n\ndef fisher_test_pooled(s1: int, n1: int, s2: int, n2: int) -> dict:\n    \"\"\"Run Fisher exact test on pooled 2x2 contingency table.\n\n    Table:\n              success  failure\n    method1:    s1     n1 - s1\n    method2:    s2     n2 - s2\n    \"\"\"\n    table = np.array([[s1, n1 - s1], [s2, n2 - s2]])\n    or_two, p_two = fisher_exact(table, alternative='two-sided')\n    or_greater, p_greater = fisher_exact(table, alternative='greater')\n    or_less, p_less = fisher_exact(table, alternative='less')\n    return {\n        \"contingency_table\": table.tolist(),\n        \"method1_sr\": s1 / n1 if n1 > 0 else 0,\n        \"method2_sr\": s2 / n2 if n2 > 0 else 0,\n        \"delta_pp\": (s1 / n1 - s2 / n2) * 100 if n1 > 0 and n2 > 0 else 0,\n        \"odds_ratio\": or_two,\n        \"p_two_sided\": p_two,\n        \"p_greater\": p_greater,\n        \"p_less\": p_less,\n    }\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"Pooled Fisher exact test from JSON data\")\n    parser.add_argument(\"--data\", required=True, help=\"Path to magnitude_curve_data.json\")\n    parser.add_argument(\"--method1\", required=True, help=\"First method key in seed_comparison\")\n    parser.add_argument(\"--method2\", required=True, help=\"Second method key in seed_comparison\")\n    parser.add_argument(\"--seeds\", nargs=\"+\", type=int, default=None,\n                        help=\"Which seeds to include (default: all available)\")\n    args = parser.parse_args()\n\n    data = load_data(args.data)\n    entries1 = get_method_data(data, args.method1)\n    entries2 = get_method_data(data, args.method2)\n\n    s1, n1 = pool_counts(entries1, args.seeds)\n    s2, n2 = pool_counts(entries2, args.seeds)\n\n    seeds_used = args.seeds if args.seeds else sorted({e[\"seed\"] for e in entries1})\n    n_seeds = len(seeds_used)\n\n    print(f\"{'='*60}\")\n    print(f\"Pooled Fisher Exact Test ({n_seeds}-seed)\")\n    print(f\"{'='*60}\")\n    print(f\"Method 1: {args.method1}\")\n    print(f\"  Seeds: {seeds_used}\")\n    print(f\"  Pooled: {s1}/{n1} = {s1/n1:.1%}\")\n    for e in entries1:\n        if args.seeds is None or e[\"seed\"] in args.seeds:\n            print(f\"    seed{e['seed']}: {e['successes']}/{e['total']} ({e['exp_id']})\")\n    print(f\"Method 2: {args.method2}\")\n    print(f\"  Seeds: {sorted({e['seed'] for e in entries2 if args.seeds is None or e['seed'] in args.seeds})}\")\n    print(f\"  Pooled: {s2}/{n2} = {s2/n2:.1%}\")\n    for e in entries2:\n        if args.seeds is None or e[\"seed\"] in args.seeds:\n            print(f\"    seed{e['seed']}: {e['successes']}/{e['total']} ({e['exp_id']})\")\n    print()\n\n    result = fisher_test_pooled(s1, n1, s2, n2)\n\n    print(f\"Contingency table:\")\n    print(f\"              success  failure\")\n    print(f\"  {args.method1:20s}  {s1:>5d}  {n1-s1:>5d}\")\n    print(f\"  {args.method2:20s}  {s2:>5d}  {n2-s2:>5d}\")\n    print()\n    print(f\"Delta: {result['delta_pp']:+.1f} pp ({args.method1} - {args.method2})\")\n    print(f\"Odds ratio: {result['odds_ratio']:.4f}\")\n    print(f\"p (two-sided): {result['p_two_sided']:.4f}\")\n    print(f\"p (method1 > method2): {result['p_greater']:.4f}\")\n    print(f\"p (method1 < method2): {result['p_less']:.4f}\")\n    print()\n\n    alpha = 0.05\n    sig = \"SIGNIFICANT\" if result['p_two_sided'] < alpha else \"NOT significant\"\n    print(f\"At alpha={alpha}: {sig}\")\n    print(f\"{'='*60}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 72_

<details><summary>Logged reasoning block</summary>

```text
Now let me register both artifacts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "25e37775-f73a-47b7-806f-f88a9adddc77",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012mJzeCpYaMYCbXCXz1yVM9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5801,
      "cache_read_input_tokens": 45251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5801
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

_source line 73_

Now registering both artifacts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "f8ca8488-16dd-4d2e-a4ec-f4f73ebfb8f2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012mJzeCpYaMYCbXCXz1yVM9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5801,
      "cache_read_input_tokens": 45251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5801
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

_source line 74_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01LrMHgnPMXqwEXDWKrX6zL3`</summary>

```json
{
  "name": "magnitude_curve_data",
  "type": "data",
  "description": "Compiled magnitude curve data (obs_only vs perdof SR at 6 norm levels) + multi-seed comparison data for Fisher tests. All counts from registry with exp_id traceability.",
  "project": "acr-vla-conformal-refinement",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/magnitude_curve_data.json",
  "tags": [
    "corl2026",
    "magnitude-curve",
    "fisher-test",
    "object-benchmark"
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
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "e544adc1-85f3-4d7e-882d-d37c117a23ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012mJzeCpYaMYCbXCXz1yVM9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5801,
      "cache_read_input_tokens": 45251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5801
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

_source line 75 · 2026-05-16T19:01:01.983Z_

<details><summary>↩ Tool result · `toolu_01LrMHgnPMXqwEXDWKrX6zL3`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_c48d4c\", \"name\": \"magnitude_curve_data\", \"type\": \"data\", \"description\": \"Compiled magnitude curve data (obs_only vs perdof SR at 6 norm levels) + multi-seed comparison data for Fisher tests. All counts from registry with exp_id traceability.\", \"path\": \"projects/acr-vla-conformal-refinement/artifacts/_project/data/magnitude_curve_data.json\", \"url\": null, \"project\": \"acr-vla-conformal-refinement\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T19:01:01.862529+00:00\", \"tags\": [\"corl2026\", \"magnitude-curve\", \"fisher-test\", \"object-benchmark\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "6c1ce02a-dd55-41c6-a458-0bf11c1cc564",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260516_c48d4c\\\", \\\"name\\\": \\\"magnitude_curve_data\\\", \\\"type\\\": \\\"data\\\", \\\"description\\\": \\\"Compiled magnitude curve data (obs_only vs perdof SR at 6 norm levels) + multi-seed comparison data for Fisher tests. All counts from registry with exp_id traceability.\\\", \\\"path\\\": \\\"projects/acr-vla-conformal-refinement/artifacts/_project/data/magnitude_curve_data.json\\\", \\\"url\\\": null, \\\"project\\\": \\\"acr-vla-conformal-refinement\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-16T19:01:01.862529+00:00\\\", \\\"tags\\\": [\\\"corl2026\\\", \\\"magnitude-curve\\\", \\\"fisher-test\\\", \\\"object-benchmark\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_c48d4c\", \"name\": \"magnitude_curve_data\", \"type\": \"data\", \"description\": \"Compiled magnitude curve data (obs_only vs perdof SR at 6 norm levels) + multi-seed comparison data for Fisher tests. All counts from registry with exp_id traceability.\", \"path\": \"projects/acr-vla-conformal-refinement/artifacts/_project/data/magnitude_curve_data.json\", \"url\": null, \"project\": \"acr-vla-conformal-refinement\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T19:01:01.862529+00:00\", \"tags\": [\"corl2026\", \"magnitude-curve\", \"fisher-test\", \"object-benchmark\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 76_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01TFFwAM3QLwpMrTdVpXBbTT`</summary>

```json
{
  "name": "pooled_fisher_test_v2",
  "type": "data",
  "description": "Fixed Fisher exact test script. Reads actual counts from JSON (no hardcoded n_rollouts). Supports --seeds flag for 2/3/4/5 seed pooled analysis. Fixes v1 bug that doubled counts.",
  "project": "acr-vla-conformal-refinement",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/pooled_fisher_test_v2.py",
  "tags": [
    "corl2026",
    "fisher-test",
    "statistics",
    "multi-seed"
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
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "9ce55205-e20b-4813-9e80-78c2b356f3b6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012mJzeCpYaMYCbXCXz1yVM9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5801,
      "cache_read_input_tokens": 45251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5801
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

_source line 77 · 2026-05-16T19:01:04.745Z_

<details><summary>↩ Tool result · `toolu_01TFFwAM3QLwpMrTdVpXBbTT`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_b3c36b\", \"name\": \"pooled_fisher_test_v2\", \"type\": \"data\", \"description\": \"Fixed Fisher exact test script. Reads actual counts from JSON (no hardcoded n_rollouts). Supports --seeds flag for 2/3/4/5 seed pooled analysis. Fixes v1 bug that doubled counts.\", \"path\": \"projects/acr-vla-conformal-refinement/artifacts/_project/data/pooled_fisher_test_v2.py\", \"url\": null, \"project\": \"acr-vla-conformal-refinement\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T19:01:04.629226+00:00\", \"tags\": [\"corl2026\", \"fisher-test\", \"statistics\", \"multi-seed\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "2c926bd0-3816-4cbc-9e24-7d83b6eca3aa",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260516_b3c36b\\\", \\\"name\\\": \\\"pooled_fisher_test_v2\\\", \\\"type\\\": \\\"data\\\", \\\"description\\\": \\\"Fixed Fisher exact test script. Reads actual counts from JSON (no hardcoded n_rollouts). Supports --seeds flag for 2/3/4/5 seed pooled analysis. Fixes v1 bug that doubled counts.\\\", \\\"path\\\": \\\"projects/acr-vla-conformal-refinement/artifacts/_project/data/pooled_fisher_test_v2.py\\\", \\\"url\\\": null, \\\"project\\\": \\\"acr-vla-conformal-refinement\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-16T19:01:04.629226+00:00\\\", \\\"tags\\\": [\\\"corl2026\\\", \\\"fisher-test\\\", \\\"statistics\\\", \\\"multi-seed\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_b3c36b\", \"name\": \"pooled_fisher_test_v2\", \"type\": \"data\", \"description\": \"Fixed Fisher exact test script. Reads actual counts from JSON (no hardcoded n_rollouts). Supports --seeds flag for 2/3/4/5 seed pooled analysis. Fixes v1 bug that doubled counts.\", \"path\": \"projects/acr-vla-conformal-refinement/artifacts/_project/data/pooled_fisher_test_v2.py\", \"url\": null, \"project\": \"acr-vla-conformal-refinement\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T19:01:04.629226+00:00\", \"tags\": [\"corl2026\", \"fisher-test\", \"statistics\", \"multi-seed\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 78_

两个产出已完成并注册：

**1. `magnitude_curve_data.json`** — 包含：
- Object benchmark magnitude curve（seed42，6 norm 级别 × obs_only + perdof）
- Spatial benchmark magnitude curve（seed42）
- 所有 baselines（argmin / vla_only / vla_mean）
- `seed_comparison` 区段：obs_only_norm02 (3 seeds), obs_only_norm01 (2 seeds), argmin (3 seeds), perdof_norm01/02 (2 seeds), vla_only (3 seeds), vla_mean (3 seeds)
- 每个数据点含 exp_id 追溯

**2. `pooled_fisher_test_v2.py`** — 修正版脚本：
- 从 JSON 读 `successes`/`total`（不硬编码）
- `--seeds 42 43 44` 指定包含哪些 seeds
- 输出 pooled Fisher p-value（双边 + 单边）
- 用法示例：`python pooled_fisher_test_v2.py --data magnitude_curve_data.json --method1 obs_only_norm02 --method2 argmin --seeds 42 43 44`

seed45/46 完成后只需在 JSON 的 `seed_comparison` 各 method 下追加条目即可直接跑 5-seed pooled test。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "uuid": "161decac-aa50-48ee-8222-02bca8eae62c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LF2rXbUNTSicNWLbtj39gT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1247,
      "cache_read_input_tokens": 51052,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1247
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

_source line 79_

两个产出已完成并注册：

**1. `magnitude_curve_data.json`** — 包含：
- Object benchmark magnitude curve（seed42，6 norm 级别 × obs_only + perdof）
- Spatial benchmark magnitude curve（seed42）
- 所有 baselines（argmin / vla_only / vla_mean）
- `seed_comparison` 区段：obs_only_norm02 (3 seeds), obs_only_norm01 (2 seeds), argmin (3 seeds), perdof_norm01/02 (2 seeds), vla_only (3 seeds), vla_mean (3 seeds)
- 每个数据点含 exp_id 追溯

**2. `pooled_fisher_test_v2.py`** — 修正版脚本：
- 从 JSON 读 `successes`/`total`（不硬编码）
- `--seeds 42 43 44` 指定包含哪些 seeds
- 输出 pooled Fisher p-value（双边 + 单边）
- 用法示例：`python pooled_fisher_test_v2.py --data magnitude_curve_data.json --method1 obs_only_norm02 --method2 argmin --seeds 42 43 44`

seed45/46 完成后只需在 JSON 的 `seed_comparison` 各 method 下追加条目即可直接跑 5-seed pooled test。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 289294,
  "duration_api_ms": 287955,
  "num_turns": 9,
  "stop_reason": "end_turn",
  "session_id": "18137809-ea2c-4289-a326-73c48f2a7d35",
  "total_cost_usd": 1.344595,
  "usage": {
    "input_tokens": 10,
    "cache_creation_input_tokens": 40458,
    "cache_read_input_tokens": 211486,
    "output_tokens": 7866,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 40458,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 377,
        "cache_read_input_tokens": 51052,
        "cache_creation_input_tokens": 1247,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1247
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1712,
      "outputTokens": 17,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001797,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 28,
      "outputTokens": 17774,
      "cacheReadInputTokens": 670841,
      "cacheCreationInputTokens": 90062,
      "webSearchRequests": 0,
      "costUSD": 1.342798,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "af416b8a-dc5f-4b8a-81dc-7d0c712b43c9"
}
```

</details>

---
