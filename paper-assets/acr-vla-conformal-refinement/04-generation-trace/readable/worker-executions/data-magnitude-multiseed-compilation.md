# data magnitude multiseed compilation

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 49
- **Recorded user turns:** 1
- **Tool calls:** 14
- **Original source:** `logs/workers/worker_data_magnitude-multiseed-compilation_20260516T221405.log`
- **Structured JSON:** [`ffd37424aa457a5cf525.json`](../../sessions/ff/ffd37424aa457a5cf525.json)

## Before a recorded user message

11 recorded events

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
  "session_id": "17ac476a-dce3-448f-b7ca-396cbd486cca",
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
  "uuid": "951bc7dc-3cf1-4f93-a2ef-87ad2ebd7c1a",
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
    "resetsAt": 1778983200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "85a8c489-afd4-4053-b945-97cc9dc05cd9",
  "session_id": "17ac476a-dce3-448f-b7ca-396cbd486cca"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the registry to get all the experiment data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "17ac476a-dce3-448f-b7ca-396cbd486cca",
  "uuid": "6e9bd076-7374-4ba7-90dd-8710b43b2ff2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012RcrhMRH8S4q8inh5YX4kc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12727,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12727
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01LqCPJbHAz3HcnJTH33GGNa`</summary>

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
  "session_id": "17ac476a-dce3-448f-b7ca-396cbd486cca",
  "uuid": "f00f693a-1182-4769-9092-ecf29ba0cff1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012RcrhMRH8S4q8inh5YX4kc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12727,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12727
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

_source line 6 · 2026-05-16T22:14:15.276Z_

<details><summary>↩ Tool result · `toolu_01LqCPJbHAz3HcnJTH33GGNa`</summary>

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
  "session_id": "17ac476a-dce3-448f-b7ca-396cbd486cca",
  "uuid": "d39fb828-aab2-405c-825e-7e4890ef9119",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_registry"
    ],
    "query": "select:mcp__agent-ml-research__read_registry",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01ShUYWBwXRRQxwj9K26wWys`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
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
  "session_id": "17ac476a-dce3-448f-b7ca-396cbd486cca",
  "uuid": "52814826-d9eb-43a3-9f04-c9431dcc42d9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016XPZAfW8C31rQ7xruQuR7X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 477,
      "cache_read_input_tokens": 24568,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 477
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

_source line 8 · 2026-05-16T22:14:19.313Z_

<details><summary>↩ Tool result · `toolu_01ShUYWBwXRRQxwj9K26wWys`</summary>

```text
Error: result (245,437 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/17ac476a-dce3-448f-b7ca-396cbd486cca/tool-results/mcp-agent-ml-research-read_registry-1778969659294.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/17ac476a-dce3-448f-b7ca-396cbd486cca/tool-results/mcp-agent-ml-research-read_registry-1778969659294.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/17ac476a-dce3-448f-b7ca-396cbd486cca/tool-results/mcp-agent-ml-research-read_registry-1778969659294.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "17ac476a-dce3-448f-b7ca-396cbd486cca",
  "uuid": "c71e5abd-dda2-463a-ab50-29bb0457e5c0",
  "tool_use_result": {
    "content": "Error: result (245,437 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/17ac476a-dce3-448f-b7ca-396cbd486cca/tool-results/mcp-agent-ml-research-read_registry-1778969659294.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/17ac476a-dce3-448f-b7ca-396cbd486cca/tool-results/mcp-agent-ml-research-read_registry-1778969659294.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/17ac476a-dce3-448f-b7ca-396cbd486cca/tool-results/mcp-agent-ml-research-read_registry-1778969659294.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval-argmin-object-seed47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T21:38:21.922Z\", \"updated_at\": \"2026-05-16T21:40:21.037Z\", \"hypothesis\": \"Argmin baseline (reconvla K=10) seed=47 on LIBERO object benchmark. Paired with obs_only seed47 on cuda:0 for direct comparison. Extends argmin multi-seed data for pooled Fisher test.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 47 --K 10 --output_file logs/eval_object_reconvla_seed47.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"322337\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-object-seed47.log\", \"submitted_at\": \"2026-05-16T21:39:10.031Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO object benchmark (10 tasks)\", \"data_count\": 100, \"model_name\": \"reconvla_argmin\", \"seed\": 47}}, \"eval-perdof-object-norm03-seed45-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T21:32:42.117Z\", \"updated_at\": \"2026-05-16T21:36:44.994Z\", \"hypothesis\": \"perdof CRM (ε=0.3) seed=45 on LIBERO object benchmark. Retry after unregistered process conflict. Expected to confirm perdof collapse at high norm (seed42=4%, seed44 running). Supports magnitude curve narrative.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_seed45_r2.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"319463\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm03-seed45-r2.log\", \"submitted_at\": \"2026-05-16T21:33:52.055Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO object benchmark (10 tasks)\", \"data_count\": 100, \"model_name\": \"crm_v3_norm_perdof\", \"seed\": 45}}, \"eval-obs-only-object-norm02-seed47\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T21:32:40.226Z\", \"updated_at\": \"2026-05-16T21:36:41.862Z\", \"hypothesis\": \"obs_only CRM (ε=0.2) seed=47 on LIBERO object benchmark. Extends multi-seed comparison to 6 seeds. If consistent with seeds 42-44 (16-22%), strengthens pooled significance for Narrative A transition.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_seed47.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"319128\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-seed47.log\", \"submitted_at\": \"2026-05-16T21:33:49.282Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO object benchmark (10 tasks)\", \"data_count\": 100, \"model_name\": \"crm_v3_norm_obs_only\", \"seed\": 47}}, \"eval-obs-only-object-norm02-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:44:19.258Z\", \"updated_at\": \"2026-05-16T21:33:38.747Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_seed45.json\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:3\", \"pid\": \"233544\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-seed45.log\", \"submitted_at\": \"2026-05-16T07:44:18.928Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 45, \"model_name\": \"crm_v3_norm_obs_only\", \"hypothesis\": \"obs_only CRM v3-norm norm=0.2 seed=45 on LIBERO object. 4th seed pre-deployed for statistical power.\", \"data_path\": \"LIBERO object benchmark (10 tasks)\", \"data_count\": 100, \"wall_clock_seconds\": 49759.8, \"gpu_hours\": 13.82}, \"reproduce\": {\"finished_at\": \"2026-05-16T21:21:10.527Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T21:21:15.588019+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.16, \"successes\": 16, \"total_rollouts\": 100, \"tasks_completed\": \"10/10\"}, \"checkpoint_path\": \"N/A (eval only)\", \"hypothesis\": \"obs_only CRM (ε=0.2) seed=45 on LIBERO object: if obs_only maintains 16-22% SR range consistent with seeds 42-44, it confirms the method's reliability across random seeds and strengthens pooled statistical test vs argmin.\", \"completed_at\": \"2026-05-16T21:33:38.747Z\"}, \"eval-scalar-object-seed44-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:11:59.390Z\", \"updated_at\": \"2026-05-16T21:29:49.586Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_scalar_seed44_r2.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"226878\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-scalar-object-seed44-r2.log\", \"submitted_at\": \"2026-05-16T07:11:59.066Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_v3_norm_scalar_unc\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 51470.5, \"gpu_hours\": 14.3}, \"reproduce\": {\"finished_at\": \"2026-05-16T21:11:40.494Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T21:11:48.900516+00:00\"}]}, \"hypothesis\": \"Scalar CRM seed=44 on LIBERO object benchmark. Retry of failed eval-scalar-object-seed44. Expects scalar variant underperforms obs_only but may match argmin baseline.\", \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.06, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-16T21:29:49.586Z\"}, \"eval-obs-only-object-default-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:13:41.913Z\", \"updated_at\": \"2026-05-16T20:38:56.577Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_default_seed44.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"229751\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-default-seed44.log\", \"submitted_at\": \"2026-05-16T07:13:41.570Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_v3_norm_obs_only\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 48315.0, \"gpu_hours\": 13.42}, \"reproduce\": {\"finished_at\": \"2026-05-16T20:36:24.235Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T20:36:28.363366+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.16, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-default-seed44.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"completed_at\": \"2026-05-16T20:38:56.577Z\"}, \"eval-perdof-object-default-seed45\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T20:21:08.043Z\", \"updated_at\": \"2026-05-16T20:21:22.126Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_object_perdof_default_seed45.json\", \"server\": \"bjb1-32546\", \"gpu_id\": 4, \"model_name\": \"crm_perdof_default\", \"seed\": 45, \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark\", \"hypothesis\": \"perdof CRM default norm (~1.42) seed=45 on LIBERO object. Confirms catastrophic collapse (seed42=0%, seed44=running). Multi-seed evidence for paper figure.\", \"pid\": 310477}}, \"eval-perdof-object-norm01-seed45\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T20:21:06.341Z\", \"updated_at\": \"2026-05-16T20:21:19.670Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_perdof_norm01_seed45.json\", \"server\": \"bjb1-32546\", \"gpu_id\": 2, \"model_name\": \"crm_perdof_norm01\", \"seed\": 45, \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark\", \"hypothesis\": \"perdof CRM norm=0.1 seed=45 on LIBERO object. Multi-seed magnitude curve: seed42=11%, seed44=deploying. 3rd seed for perdof low-norm baseline.\", \"pid\": 309151}}, \"eval-perdof-object-norm01-seed44\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T20:21:04.937Z\", \"updated_at\": \"2026-05-16T20:21:16.499Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_perdof_norm01_seed44.json\", \"server\": \"bjb1-18228\", \"gpu_id\": 1, \"model_name\": \"crm_perdof_norm01\", \"seed\": 44, \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark\", \"hypothesis\": \"perdof CRM norm=0.1 seed=44 on LIBERO object. Multi-seed magnitude curve: seed42=11%, expecting similar. Fills the biggest gap in perdof magnitude data (norm=0.1 only has 1 seed).\", \"pid\": 531963}}, \"eval-perdof-object-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T04:56:22.235Z\", \"updated_at\": \"2026-05-16T19:45:27.956Z\", \"hypothesis\": \"perdof CRM v3-norm seed=44 on LIBERO object benchmark. Completes seed=44 four-way comparison. seed42=11%, seed43=12%. Expected to confirm perdof < argmin.\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-16T04:57:04.525Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --benchmark object --mode crm_perdof --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1 --K 10 --seed 44 --n_rollouts 10 --output_file logs/eval_object_perdof_seed44.json\\\"\", \"finished_at\": \"2026-05-16T18:13:35.112Z\", \"training_hours\": 13.28}, \"spec\": {\"data_path\": \"LIBERO_object\", \"data_count\": 100, \"model_name\": \"crm_perdof\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO_object_10tasks_10rollouts\"}, \"pid\": \"452982\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-seed44.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T18:13:38.573783+00:00\"}]}, \"metrics\": {\"overall_sr\": 0.08, \"total_success\": 8, \"total_rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"completed_at\": \"2026-05-16T19:45:27.956Z\"}, \"eval-obs-only-object-norm01-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:12:01.937Z\", \"updated_at\": \"2026-05-16T19:45:26.774Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_obs_only_norm01_seed44.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"227086\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm01-seed44.log\", \"submitted_at\": \"2026-05-16T07:12:01.614Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_v3_norm_obs_only\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 45205.2, \"gpu_hours\": 12.56}, \"reproduce\": {\"finished_at\": \"2026-05-16T19:42:10.387Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T19:42:13.494105+00:00\"}]}, \"metrics\": {\"overall_sr\": 0.16, \"total_success\": 16, \"total_rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"completed_at\": \"2026-05-16T19:45:26.774Z\"}, \"eval-obs-only-object-norm03-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T06:05:51.470Z\", \"updated_at\": \"2026-05-16T19:37:12.898Z\", \"hypothesis\": \"obs_only CRM v3-norm at norm=0.3 seed=44 on LIBERO object benchmark. Multi-seed magnitude curve coverage. seed42 norm=0.3 object still running on bjb2-28827. Pairs with seed44 norm=0.2 for norm sensitivity across seeds.\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-32546\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-16T06:06:08.369Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03_seed44.json\\\"\", \"finished_at\": \"2026-05-16T19:34:37.134Z\", \"training_hours\": 13.47}, \"spec\": {\"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_obs_only (327198 params)\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\"}, \"pid\": \"220777\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm03-seed44.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T19:34:40.416412+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.18, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"completed_at\": \"2026-05-16T19:37:12.898Z\"}, \"eval-argmin-object-seed46\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T18:39:23.017Z\", \"updated_at\": \"2026-05-16T18:55:11.951Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 46 --K 10 --output_file logs/eval_object_reconvla_seed46.json\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:1\", \"seed\": 46, \"model_name\": \"reconvla\", \"hypothesis\": \"argmin baseline K=10 seed=46 on LIBERO object. 5th seed for Fisher test. Pairs with eval-obs-only-object-norm02-seed46 (bjb1-18228:cuda:3).\", \"data_path\": \"\", \"data_count\": 0, \"checkpoint_source\": \"\", \"eval_data\": \"object\", \"pid\": 295478, \"log_path\": \"logs/eval_argmin_object_seed46.log\"}}, \"eval-vla-mean-object-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T04:58:30.713Z\", \"updated_at\": \"2026-05-16T18:36:08.965Z\", \"hypothesis\": \"VLA-mean baseline (K=10, mean aggregation) seed=44 on LIBERO object benchmark. Completes seed=44 six-way comparison. seed42=12%, seed43=15%.\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-32546\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-16T04:58:47.863Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode mean --n_rollouts 10 --K 10 --seed 44 --output_file logs/eval_object_vla_mean_seed44.json\\\"\", \"finished_at\": \"2026-05-16T18:33:19.875Z\", \"training_hours\": 13.58}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode mean --n_rollouts 10 --K 10 --seed 44 --output_file logs/eval_object_vla_mean_seed44.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"212655\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-mean-object-seed44.log\", \"submitted_at\": \"2026-05-16T04:58:50.101Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 49038.9, \"gpu_hours\": 13.62}, \"pid\": \"212655\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-mean-object-seed44.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T18:33:23.084588+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.1, \"per_task_sr\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.1, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.3, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0.1, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0.1, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 0, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.2, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.2}}, \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed44.json\", \"completed_at\": \"2026-05-16T18:36:08.965Z\"}, \"eval-obs-only-object-norm02-seed46\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T16:04:31.207Z\", \"updated_at\": \"2026-05-16T16:04:39.850Z\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_seed46.json 2>&1 | tee logs/eval_object_obs_only_norm02_seed46.log\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": 510896, \"seed\": 46, \"model_name\": \"crm_obs_only_norm02\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"hypothesis\": \"obs_only CRM v3-norm norm=0.2 seed=46 on LIBERO object. 5th seed for Fisher test statistical power.\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark\", \"log_path\": \"logs/eval_object_obs_only_norm02_seed46.log\"}}, \"eval-perdof-object-norm03-seed44\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T15:24:11.457Z\", \"updated_at\": \"2026-05-16T15:55:56.295Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_seed44.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"505419\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm03-seed44.log\", \"submitted_at\": \"2026-05-16T15:24:11.074Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_id\": \"cuda:2\", \"model_name\": \"crm_perdof_norm03\", \"seed\": 44, \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100}}, \"eval-obs-only-object-norm03-seed45-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T15:24:08.486Z\", \"updated_at\": \"2026-05-16T15:55:53.009Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03_seed45_r2.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"pid\": \"272762\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm03-seed45-r2.log\", \"submitted_at\": \"2026-05-16T15:24:08.144Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_id\": \"cuda:3\", \"model_name\": \"crm_obs_only_norm03\", \"seed\": 45, \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100}}, \"eval-obs-only-object-norm02-seed44-r4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T14:48:54.894Z\", \"updated_at\": \"2026-05-16T15:36:08.207Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_seed44_r4.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"501420\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-seed44-r4.log\", \"submitted_at\": \"2026-05-16T14:49:19.300Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1956.7, \"gpu_hours\": 0.54}, \"hypothesis\": \"P0 retry #4: obs_only CRM v3-norm norm=0.2 seed=44 on LIBERO object. Third seed for Fisher test. seed42=22%, seed43=16%. Previous attempts failed (127/129/killed).\", \"pid\": 501420, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T15:21:56.018Z\", \"failure_reason\": \"r2 data valid (16%), r4 redundant. PID 501420 killed by worker at 2026-05-16T15:09.\"}, \"eval-argmin-object-seed44-r2\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-16T01:32:14.163Z\", \"updated_at\": \"2026-05-16T15:34:00.414Z\", \"hypothesis\": \"Retry of eval-argmin-object-seed44 (EXIT_CODE=127, missing conda activate). argmin baseline K=10 seed=44 on LIBERO object. Third seed for Fisher test. seed42=12%, seed43=17%.\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-18228\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-16T01:32:36.214Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 44 --K 10 --output_file logs/eval_object_reconvla_seed44.json\\\"\", \"finished_at\": \"2026-05-16T15:28:27.588Z\", \"training_hours\": 13.93}, \"completed_at\": \"2026-05-16T01:34:17.696Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"killed\"}, \"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T15:28:32.358640+00:00\"}]}, \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 44 --K 10 --output_file logs/eval_object_reconvla_seed44.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"428117\", \"seed\": 44, \"model_name\": \"reconvla_argmin\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.13, \"successes\": 13, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.5, \"orange_juice\": 0.2}, \"note\": \"EXIT_CODE=129 was SIGHUP after completion, results valid. log: logs/eval_object_reconvla_seed44.json\"}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed44.json\"}, \"eval-obs-only-object-norm02-seed44-r2\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-16T01:32:15.187Z\", \"updated_at\": \"2026-05-16T15:25:14.349Z\", \"hypothesis\": \"Retry of eval-obs-only-object-norm02-seed44 (EXIT_CODE=127, missing conda activate). obs_only CRM norm=0.2 seed=44 on LIBERO object. Third seed for Fisher test. seed42=22% (PROJECT HIGH).\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-18228\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-16T01:32:45.643Z\", \"finished_at\": \"2026-05-16T14:40:32.978Z\", \"training_hours\": 13.13}, \"completed_at\": \"2026-05-16T01:34:19.695Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"killed\"}, \"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T14:40:38.399800+00:00\"}]}, \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_seed44.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"428406\", \"seed\": 44, \"model_name\": \"crm_obs_only_norm02\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100}, \"failure_reason\": null, \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.16, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}, \"checkpoint_path\": \"logs/eval_object_obs_only_norm02_seed44.json\"}, \"eval-vla-only-object-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T08:34:53.953Z\", \"updated_at\": \"2026-05-16T15:22:52.157Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python src/evaluate.py --benchmark object --mode vla_only --K 1 --seed 45 --output_file logs/eval_object_vla_only_seed45.json\", \"server\": \"bjb2-28827\", \"gpu_id\": \"cuda:4\", \"pid\": 221407, \"seed\": 45, \"model_name\": \"smolvla_libero\", \"data_path\": \"LIBERO object\", \"data_count\": 10, \"checkpoint_source\": \"N/A\", \"eval_data\": \"LIBERO object\", \"hypothesis\": \"VLA-only baseline K=1 seed=45 on LIBERO object. Reference for seed45 statistical comparison. seed42=12%, seed43=12%, seed44=10%.\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T14:56:50.174Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T14:56:52.057Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T14:56:54.606880+00:00\"}]}, \"metrics\": {\"overall_sr\": 0.09, \"successes\": 18, \"total\": 200, \"tasks_done\": 10}}, \"eval-obs-only-object-norm01-seed45\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T09:01:52.970Z\", \"updated_at\": \"2026-05-16T14:48:49.862Z\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 python src/evaluate.py --mode crm_obs_only --max_correction_norm 0.1 --k 10 --seed 45 --benchmark object --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_norm01_seed45.json > logs/eval_object_obs_only_norm01_seed45.log 2>&1\", \"server\": \"bjb1-18228\", \"gpu_id\": \"cuda:0\", \"model_name\": \"crm_obs_only\", \"seed\": 45, \"data_path\": \"LIBERO object benchmark\", \"data_count\": -1, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object\", \"hypothesis\": \"obs_only CRM norm=0.1 seed=45 on LIBERO object. Multi-seed magnitude curve data point. seed42=19%.\"}, \"pid\": 474319}, \"eval-obs-only-object-norm03-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T11:14:47.376Z\", \"updated_at\": \"2026-05-16T11:30:59.542Z\", \"spec\": {\"model_name\": \"crm_v3_norm_obs_only\", \"seed\": 45, \"data_path\": \"LIBERO object benchmark (10 tasks)\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03_seed45.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"248860\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm03-seed45.log\", \"submitted_at\": \"2026-05-16T11:14:47Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 972.5, \"gpu_hours\": 0.27}, \"hypothesis\": \"obs_only CRM v3-norm at norm=0.3 seed=45 on LIBERO object benchmark. Multi-seed magnitude curve data point. seed42 norm=0.3=19%, seed44 norm=0.3=running. Extends magnitude robustness evidence to 3rd seed.\", \"conclusion\": \"failed\", \"failure_reason\": \"killed to resolve cuda:3 GPU conflict\", \"completed_at\": \"2026-05-16T11:30:59.542Z\"}, \"eval-mag-perdof-norm03-object-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:26:52.169Z\", \"updated_at\": \"2026-05-16T11:30:53.907Z\", \"spec\": {\"server\": \"bjb2-28827\", \"gpu\": \"cuda:2\", \"pid\": 140759, \"command\": \"python -u src/evaluate.py --mode crm_perdof --benchmark object --seed 42 --K 10 --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_r3.json\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_v3_norm_perdof\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\"}, \"metrics\": {\"overall_sr\": 0.04, \"successes\": 4, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10}, \"reproduce\": {\"finished_at\": \"2026-05-16T11:10:32.044Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T11:10:33.866Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T11:10:39.747200+00:00\"}]}}, \"eval-vla-mean-object-seed45\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T11:14:45.495Z\", \"updated_at\": \"2026-05-16T11:16:06.258Z\", \"spec\": {\"model_name\": \"smolvla_libero_vla_mean\", \"seed\": 45, \"data_path\": \"LIBERO object benchmark (10 tasks)\", \"data_count\": 100, \"checkpoint_source\": \"N/A\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode mean --n_rollouts 10 --K 10 --seed 45 --output_file logs/eval_object_vla_mean_seed45.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"248652\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-mean-object-seed45.log\", \"submitted_at\": \"2026-05-16T11:14:45Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"VLA-mean baseline (K=10, mean aggregation) seed=45 on LIBERO object benchmark. Completes seed=45 six-way comparison. seed42=12%, seed43=15%, seed44=running.\"}, \"eval-obs-only-object-default-seed45\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T11:15:05.583Z\", \"updated_at\": \"2026-05-16T11:15:22.983Z\", \"spec\": {\"command\": \"python src/evaluate.py --mode crm_obs_only --K 10 --seed 45 --benchmark object --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_default_seed45.json\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:3\", \"pid\": 242264, \"data_path\": \"LIBERO object benchmark\", \"data_count\": 10, \"model_name\": \"crm_obs_only\", \"seed\": 45}}, \"eval-mag-perdof-norm02-seed43-object-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:34:16.821Z\", \"updated_at\": \"2026-05-16T10:41:59.362Z\", \"spec\": {\"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_perdof\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed43_r3.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"144504\"}, \"metrics\": {\"overall_sr\": 0.09, \"successes\": 9, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}, \"vs_seed42\": \"-2pp (11% → 9%)\", \"pooled_2seed_perdof_02\": \"10% (20/200)\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T10:39:30.416Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T10:39:33.739829+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"log_path\": \"logs/eval_object_perdof_norm02_seed43_r3.json\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T10:41:59.362Z\"}, \"eval-acr-object-v4-default-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:11:49.844Z\", \"updated_at\": \"2026-05-16T09:00:15.290Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_object_perdof_default_norm_r2.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"390936\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-default-r2.log\", \"submitted_at\": \"2026-05-16T02:11:20Z\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_object\", \"data_count\": 10, \"model_name\": \"crm_perdof_default_norm\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"object\", \"wall_clock_seconds\": 24535.3, \"gpu_hours\": 6.82}, \"hypothesis\": \"v4-default (no magnitude control, norm≈1.42) on object benchmark — ablation to confirm catastrophic failure\", \"parent\": \"eval-acr-object-v4-default\", \"metrics\": {\"overall_sr\": 0, \"successes\": 0, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0, \"bbq_sauce\": 0, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0, \"orange_juice\": 0}, \"note\": \"actual mode=crm_perdof with default norm (~1.42), NOT crm_default. Confirms catastrophic failure at uncontrolled correction magnitude.\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"completed_at\": \"2026-05-16T09:00:15.290Z\"}, \"eval-scalar-object-seed45\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T08:38:01.206Z\", \"updated_at\": \"2026-05-16T08:38:07.795Z\", \"spec\": {\"command\": \"python src/evaluate.py --mode crm_scalar --max_correction_norm 0.1 --K 10 --seed 45 --benchmark object --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --output_file logs/eval_object_scalar_seed45.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"pid\": 224623, \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_v3_scalar_unc\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"eval_data\": \"LIBERO object\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"log_path\": \"logs/eval_object_scalar_seed45.log\"}}, \"eval-mag-perdof-norm005-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:56:58.178Z\", \"updated_at\": \"2026-05-16T08:38:02.524Z\", \"spec\": {\"hypothesis\": \"Object magnitude sweep: perdof CRM v3-norm at norm=0.05 on LIBERO object benchmark. Paired with obs_only norm=0.05 for magnitude comparison figure.\", \"parent\": \"eval-acr-object-v4-perdof\", \"command\": \"python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_perdof_norm005.json\", \"server\": \"bjb2-28827\", \"gpu\": \"1\", \"pid\": 109650, \"data_path\": \"LIBERO object benchmark\", \"data_count\": 10, \"model_name\": \"crm_perdof\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object (10 tasks x 10 rollouts)\", \"log_path\": \"logs/nohup_eval_object_perdof_norm005.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\"}, \"metrics\": {\"overall_sr\": 0.14, \"successes\": 14, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10}, \"reproduce\": {\"finished_at\": \"2026-05-16T08:36:33.616Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T08:36:35.355Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T08:36:40.842032+00:00\"}]}}, \"eval-mag-perdof-norm003-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:47:32.591Z\", \"updated_at\": \"2026-05-16T08:37:12.296Z\", \"hypothesis\": \"Object magnitude sweep: perdof CRM v3-norm at norm=0.03 on LIBERO object benchmark. Paired with obs_only norm=0.03 for magnitude comparison figure. Tests perdof at smallest correction norm on object domain.\", \"spec\": {\"command\": \"python src/evaluate.py --mode crm_perdof --max_correction_norm 0.03 --K 10 --seed 42 --benchmark object\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"pid\": 105938, \"log_path\": \"logs/eval_object_perdof_norm003.json\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_v3_perdof\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object\", \"parent\": \"eval-acr-object-v4-perdof\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"metrics\": {\"overall_success_rate\": 0.14, \"per_task_range\": \"0.0-0.4\"}}, \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.14, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.1}}, \"reproduce\": {\"finished_at\": \"2026-05-16T08:09:00.286Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T08:09:03.327886+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003.json\", \"completed_at\": \"2026-05-16T08:11:39.117Z\"}, \"eval-perdof-object-norm02-seed45\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T08:34:55.059Z\", \"updated_at\": \"2026-05-16T08:35:03.183Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python src/evaluate.py --benchmark object --mode crm_perdof --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --K 10 --seed 45 --output_file logs/eval_object_perdof_norm02_seed45.json\", \"server\": \"bjb2-28827\", \"gpu_id\": \"cuda:1\", \"pid\": 222824, \"seed\": 45, \"model_name\": \"crm_perdof\", \"data_path\": \"LIBERO object\", \"data_count\": 10, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object\", \"hypothesis\": \"Perdof CRM norm=0.2 seed=45 on LIBERO object. Additional perdof data point for cross-seed comparison. Expected ~11% based on seed42 data.\"}}, \"eval-mag-obsonly-norm005-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:29:00.724Z\", \"updated_at\": \"2026-05-16T08:19:41.189Z\", \"spec\": {\"hypothesis\": \"Object magnitude sweep: obs_only CRM v3-norm at norm=0.05 on LIBERO object benchmark. Builds object magnitude curve alongside norm=0.1 (19%) and norm=0.2 (18% partial). Key data for fig3.\", \"parent\": \"eval-acr-object-v4-obs-only\", \"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_obs_only_norm005.json\", \"server\": \"bjb2-28827\", \"data_path\": \"simpler_env object benchmark\", \"data_count\": 10, \"model_name\": \"crm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"object benchmark, max_correction_norm=0.05, K=10, n_rollouts=10\", \"pid\": 101610, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005.log\"}, \"metrics\": {\"overall_sr\": 0.13, \"tasks_completed\": 10, \"total_rollouts\": 100, \"successes\": 13, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"success\", \"checkpoint_path\": \"logs/eval_object_obs_only_norm005.json\", \"completed_at\": \"2026-05-16T08:19:41.189Z\"}, \"eval-obs-only-object-norm02-seed43-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:58:27.783Z\", \"updated_at\": \"2026-05-16T07:46:23.704Z\", \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-seed43-r2.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}, \"hypothesis\": \"D031: obs_only CRM v3-norm norm=0.2 seed=43 on LIBERO object benchmark (r2 retry). P0 critical for statistical significance — seed42=22%, need seed43 pooled to 200 trials. Original crashed after 1 task.\", \"parent\": \"eval-obs-only-object-norm02-seed43\", \"metrics\": {\"overall_sr\": 0.16, \"successes\": 16, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}, \"vs_seed42\": \"-6pp (22% → 16%)\", \"vs_argmin_seed43\": \"-1pp (17% → 16%)\", \"pooled_2seed_obs_only_02\": \"19% (38/200)\", \"pooled_2seed_argmin\": \"14.5% (29/200)\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T07:21:07.838Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T07:21:10.900676+00:00\"}]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T07:23:48.849Z\"}, \"eval-argmin-object-seed45\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:44:23.744Z\", \"updated_at\": \"2026-05-16T07:46:05.948Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 45 --K 10 --output_file logs/eval_object_argmin_seed45.json\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:5\", \"pid\": \"215932\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-object-seed45.log\", \"submitted_at\": \"2026-05-16T07:45:06.846Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 45, \"model_name\": \"reconvla_argmin_baseline\", \"hypothesis\": \"argmin baseline K=10 seed=45 on LIBERO object. 4th seed baseline for Fisher test. Paired with eval-obs-only-object-norm02-seed45.\", \"data_path\": \"LIBERO object benchmark (10 tasks)\", \"data_count\": 100}}, \"eval-mag-obsonly-norm03-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:29:02.155Z\", \"updated_at\": \"2026-05-16T07:42:44.267Z\", \"spec\": {\"hypothesis\": \"Object magnitude sweep: obs_only CRM v3-norm at norm=0.3 on LIBERO object benchmark. Tests degradation at higher correction norm on object domain. Key data for fig3.\", \"parent\": \"eval-acr-object-v4-obs-only\", \"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03.json\", \"server\": \"bjb2-28827\", \"data_path\": \"simpler_env object benchmark\", \"data_count\": 10, \"model_name\": \"crm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"object benchmark, max_correction_norm=0.3, K=10, n_rollouts=10\", \"pid\": 103028, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03.log\"}, \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.19, \"successes\": 19, \"total\": 100}, \"reproduce\": {\"finished_at\": \"2026-05-16T07:35:42.126Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T07:35:43.889Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T07:35:47.235304+00:00\"}]}}, \"eval-perdof-object-default-seed44\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:18:01.200Z\", \"updated_at\": \"2026-05-16T07:19:12.088Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_object_perdof_default_seed44.json\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"316382\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-default-seed44.log\", \"submitted_at\": \"2026-05-16T07:18:00.861Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"crm_v3_norm/perdof\", \"seed\": 44, \"data_path\": \"LIBERO object benchmark\", \"data_count\": 10, \"hypothesis\": \"perdof CRM v3-norm with DEFAULT max_correction_norm (~1.42) seed=44 on LIBERO object. perdof norm=0.1=11%, norm=0.2=11% on object — expected similar or worse at default.\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object\"}}, \"eval-vla-only-object-seed44-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:33:13.916Z\", \"updated_at\": \"2026-05-16T07:13:29.827Z\", \"hypothesis\": \"Retry of eval-vla-only-object-seed44 (r1 EXIT_CODE=127). VLA-only baseline K=1 seed=44 on LIBERO object. Third seed reference. seed42=12%, seed43=12%.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 44 --K 1 --output_file logs/eval_object_vla_only_seed44.json\\\"\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"286989\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-object-seed44-r2.log\", \"submitted_at\": \"2026-05-16T01:33:46.467Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 20383.4, \"gpu_hours\": 5.66}, \"server\": \"bjb2-40593\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb2-40593\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-16T01:33:44.353Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 44 --K 1 --output_file logs/eval_object_vla_only_seed44.json\\\"\", \"code_commit\": \"4b4e03d05161290989b1f19d6e13e077da681a41\", \"finished_at\": \"2026-05-16T04:58:56.451Z\", \"training_hours\": 3.42}, \"pid\": \"286989\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-object-seed44-r2.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T04:59:00.452305+00:00\"}]}, \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.1, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (vla_only baseline)\", \"completed_at\": \"2026-05-16T07:13:29.827Z\"}, \"eval-mag-perdof-norm02-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:07:31.626Z\", \"updated_at\": \"2026-05-16T07:12:35.145Z\", \"spec\": {\"parent\": \"eval-acr-object-v4-perdof\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_perdof\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"object benchmark, max_correction_norm=0.2, K=10, n_rollouts=10\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"127732\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-perdof-norm02-object.log\"}, \"hypothesis\": \"Object magnitude sweep: perdof CRM v3-norm at norm=0.2 on LIBERO object benchmark. Paired with obs_only norm=0.2 (running, 18% at 5/10) for magnitude comparison figure. Tests perdof at moderate correction norm on object domain.\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.11, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}, \"reproduce\": {\"finished_at\": \"2026-05-16T06:04:45.416Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T06:04:48.447852+00:00\"}]}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"completed_at\": \"2026-05-16T07:12:35.145Z\"}, \"eval-acr-object-obs-only-default\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:38:22.125Z\", \"updated_at\": \"2026-05-16T07:09:01.967Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_default_norm.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": 134094, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-obs-only-default.log\", \"submitted_at\": \"2026-05-15T17:38:21.517Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_v3_norm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark\", \"wall_clock_seconds\": 48640.4, \"gpu_hours\": 13.51}, \"hypothesis\": \"obs_only CRM v3-norm with DEFAULT max_correction_norm (~1.42, no magnitude control) on LIBERO object benchmark. Paired with eval-acr-object-v4-default (perdof default). Tests whether obs_only robustness holds even without magnitude capping — if yes, obs_only is fundamentally more robust than perdof regardless of norm setting.\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.17, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.5, \"orange_juice\": 0.3}}, \"reproduce\": {\"finished_at\": \"2026-05-16T06:41:19.269Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T06:41:22.516205+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"completed_at\": \"2026-05-16T07:09:01.967Z\"}, \"eval-scalar-object-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:02:31.432Z\", \"updated_at\": \"2026-05-16T06:04:05.747Z\", \"hypothesis\": \"D031: scalar_unc CRM v3-norm seed=43 on LIBERO object benchmark. Completes seed=43 six-way comparison table. scalar seed=42 was worst at 4% — seed=43 confirms.\", \"parent\": \"eval-acr-object-v4-scalar\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_scalar_seed43.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"114664\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-scalar-object-seed43.log\", \"submitted_at\": \"2026-05-15T16:03:30.400Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_object\", \"data_count\": 10, \"model_name\": \"crm_scalar\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"eval_data\": \"object\", \"wall_clock_seconds\": 50435.3, \"gpu_hours\": 14.01}, \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"avg_sr\": 10, \"per_task_sr\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 30, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 10, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 30, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 30}}, \"reproduce\": {\"finished_at\": \"2026-05-16T06:01:42.952Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T06:01:45.993724+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed43.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed43.json\", \"completed_at\": \"2026-05-16T06:04:05.747Z\"}, \"eval-mag-obsonly-norm003-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:47:31.254Z\", \"updated_at\": \"2026-05-16T05:56:01.541Z\", \"hypothesis\": \"Object magnitude sweep: obs_only CRM v3-norm at norm=0.03 on LIBERO object benchmark. Completes 5-point magnitude curve (0.03/0.05/0.1/0.2/0.3). Tests minimum effective correction magnitude on object domain.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_obs_only_norm003.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": 121325, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm003-object.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"object benchmark, max_correction_norm=0.03, K=10, n_rollouts=10\", \"parent\": \"eval-acr-object-v4-obs-only\"}, \"metrics\": {\"overall_sr\": 0.16, \"tasks_done\": 100, \"tasks_total\": 100, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0.2, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.1, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.4, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_butter_and_place_it_in_the_basket\": 0.1, \"pick_up_the_milk_and_place_it_in_the_basket\": 0.2, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.3, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.3}}, \"reproduce\": {\"finished_at\": \"2026-05-16T05:35:17.752Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T05:35:20.742243+00:00\"}]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T05:56:01.541Z\"}, \"eval-scalar-object-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T05:02:34.914Z\", \"updated_at\": \"2026-05-16T05:25:06.306Z\", \"hypothesis\": \"scalar_unc CRM v3-norm seed=44 on LIBERO object benchmark. Completes seed=44 six-way comparison. scalar seed42=9%, seed43 running (0% at 3/10). Expected worst CRM variant.\", \"server\": \"bjb2-40593\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb2-40593\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-16T05:02:50.780Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_scalar_seed44.json\\\"\", \"code_commit\": \"4b4e03d05161290989b1f19d6e13e077da681a41\", \"finished_at\": \"2026-05-16T05:05:30.084Z\", \"training_hours\": 0.04}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_scalar_seed44.json\\\"\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"310854\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-scalar-object-seed44.log\", \"submitted_at\": \"2026-05-16T05:25:05.983Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"pid\": \"309346\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-scalar-object-seed44.log\", \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-16T05:05:32.021Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T05:05:34.587431+00:00\"}]}}, \"eval-obs-only-object-norm02-seed44-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:34:30.429Z\", \"updated_at\": \"2026-05-16T04:59:20.094Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_seed44.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"431189\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-seed44-r3.log\", \"submitted_at\": \"2026-05-16T01:34:30.132Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 12290.0, \"gpu_hours\": 3.41}, \"hypothesis\": \"Retry of eval-obs-only-object-norm02-seed44 (r1 EXIT_CODE=127, r2 killed by agent). obs_only CRM norm=0.2 seed=44 on LIBERO object. Third seed for Fisher test. seed42=22% (PROJECT HIGH).\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T04:59:20.095Z\"}, \"eval-argmin-object-seed44-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:34:28.047Z\", \"updated_at\": \"2026-05-16T04:59:17.975Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 44 --K 10 --output_file logs/eval_object_reconvla_seed44.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"430985\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-object-seed44-r3.log\", \"submitted_at\": \"2026-05-16T01:34:27.679Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 12290.3, \"gpu_hours\": 3.41}, \"hypothesis\": \"Retry of eval-argmin-object-seed44 (r1 EXIT_CODE=127, r2 killed by agent). argmin baseline K=10 seed=44 on LIBERO object. Third seed for Fisher test. seed42=12%, seed43=17%.\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T04:59:17.975Z\"}, \"eval-vla-mean-object-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:46:28.667Z\", \"updated_at\": \"2026-05-16T04:53:17.141Z\", \"hypothesis\": \"D031: VLA-mean baseline (K=10, mean aggregation) seed=43 on LIBERO object benchmark. Completes seed=43 comparison table. If VLA-mean seed=43 ≈ obs_only seed=43 → CRM correction claim compressed.\", \"parent\": \"eval-vla-mean-object\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode mean --n_rollouts 10 --K 10 --seed 43 --output_file logs/eval_object_vla_mean_seed43.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"111709\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-mean-object-seed43.log\", \"submitted_at\": \"2026-05-15T15:47:37.968Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 43, \"model_name\": \"smolvla\", \"data_path\": \"libero/object\", \"data_count\": 10, \"checkpoint_source\": null, \"eval_data\": \"object\", \"wall_clock_seconds\": 47139.2, \"gpu_hours\": 13.09}, \"metrics\": {\"overall_sr\": 0.15, \"tasks_done\": 10, \"tasks_total\": 10, \"total_success\": 15, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.3, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.1}}, \"reproduce\": {\"finished_at\": \"2026-05-16T04:48:28.380Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T04:48:31.493092+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval-only)\", \"completed_at\": \"2026-05-16T04:53:17.141Z\"}, \"eval-perdof-object-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:19:49.586Z\", \"updated_at\": \"2026-05-16T03:15:39.287Z\", \"hypothesis\": \"D031 supplementary: perdof CRM v3-norm seed=43 on LIBERO object benchmark. Completes three-way comparison (obs_only vs argmin vs perdof) with doubled samples. If perdof seed=43 ≈ argmin seed=43 → confirms obs_only uniquely better.\", \"parent\": \"eval-acr-object-v4-perdof\", \"spec\": {\"command\": \"python evaluate.py --benchmark object --mode crm_perdof --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1 --K 10 --seed 43 --n_rollouts 10 --output_file logs/eval_object_perdof_seed43.json\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"pid\": 365925, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-seed43.log\", \"submitted_at\": \"2026-05-15T13:21:00.347Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 43, \"model_name\": \"crm_perdof\", \"data_path\": \"LIBERO_object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO_object_10tasks_10rollouts\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"wall_clock_seconds\": 50078.9, \"gpu_hours\": 13.91}, \"metrics\": {\"overall_success_rate\": 0.12, \"tasks_done\": 10, \"tasks_total\": 10, \"total_rollouts\": 100, \"total_successes\": 12, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}, \"reproduce\": {\"finished_at\": \"2026-05-16T03:12:36.498Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T03:12:39.589841+00:00\"}]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T03:15:39.287Z\"}, \"eval-vla-only-object-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:29:00.342Z\", \"updated_at\": \"2026-05-16T01:33:29.678Z\", \"hypothesis\": \"D035 follow-up: VLA-only baseline (K=1) seed=44 on LIBERO object benchmark. Third seed reference point. seed42=12%, seed43=12%. Deployed on bjb2-40593.\", \"server\": \"bjb2-40593\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb2-40593\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-16T01:29:36.987Z\", \"command\": \"bash -c \\\"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 44 --K 1 --output_file logs/eval_object_vla_only_seed44.json\\\"\", \"code_commit\": \"4b4e03d05161290989b1f19d6e13e077da681a41\", \"finished_at\": \"2026-05-16T01:30:26.640Z\", \"training_hours\": 0.01}, \"spec\": {\"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"vla_only\", \"seed\": 44, \"checkpoint_source\": \"N/A\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\"}, \"pid\": \"unknown\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-object-seed44.log\", \"failure_reason\": \"EXIT_CODE=127 (command not found) — bash -c wrapping 或环境激活路径错误，bjb2-40593 上系统性问题，三个 seed44 实验全部同样失败\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-16T01:30:33.143Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T01:30:38.635650+00:00\"}]}}, \"eval-obs-only-object-norm02-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:28:59.304Z\", \"updated_at\": \"2026-05-16T01:32:51.127Z\", \"hypothesis\": \"D035 follow-up: obs_only CRM v3-norm norm=0.2 seed=44 on LIBERO object benchmark. Third seed for Fisher exact test. ε=0.2 is PROJECT HIGH config (seed42=22%). Paired with eval-argmin-object-seed44.\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-18228\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-16T01:29:31.218Z\", \"command\": \"bash -c \\\"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_seed44.json\\\"\", \"finished_at\": \"2026-05-16T01:30:14.217Z\", \"training_hours\": 0.01}, \"spec\": {\"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_obs_only (327198 params)\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\"}, \"pid\": \"unknown\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-seed44.log\", \"failure_reason\": \"EXIT_CODE=127: submit command missing conda activation (source /root/miniconda3/etc/profile.d/conda.sh && conda activate base). tmux runs sh, not bash — python not in PATH. Will retry as r2.\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-16T01:30:20.761Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T01:30:23.773246+00:00\"}]}}, \"eval-argmin-object-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:28:58.358Z\", \"updated_at\": \"2026-05-16T01:32:49.190Z\", \"hypothesis\": \"D035 follow-up: argmin baseline (K=10) seed=44 on LIBERO object benchmark. Third seed for Fisher exact test statistical power. Paired with eval-obs-only-object-norm02-seed44. seed42=12%, seed43=17%.\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-18228\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-16T01:29:25.990Z\", \"command\": \"bash -c \\\"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 44 --K 10 --output_file logs/eval_object_reconvla_seed44.json\\\"\", \"finished_at\": \"2026-05-16T01:30:04.115Z\", \"training_hours\": 0.01}, \"spec\": {\"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"ReconVLA (argmin baseline)\", \"seed\": 44, \"checkpoint_source\": \"N/A (no CRM)\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\"}, \"pid\": \"unknown\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-object-seed44.log\", \"failure_reason\": \"EXIT_CODE=127: submit command missing conda activation (source /root/miniconda3/etc/profile.d/conda.sh && conda activate base). tmux runs sh, not bash — python not in PATH. Will retry as r2.\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-16T01:30:06.598Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T01:30:09.864458+00:00\"}]}}, \"eval-obs-only-object-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:58:46.063Z\", \"updated_at\": \"2026-05-16T00:51:14.618Z\", \"hypothesis\": \"D031: obs_only CRM v3-norm seed=43 on LIBERO object benchmark. Doubles sample size for Fisher exact test. seed=42 shows obs_only 16% vs argmin 8% (+8pp, p≈0.19). Combined 200 trials target p < 0.05.\", \"parent\": \"eval-acr-object-v4-obs-only\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_obs_only_seed43.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"356490\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_seed43.json\", \"submitted_at\": \"2026-05-15T12:00:38.618Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_obs_only + SmolVLA\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark (10 tasks x 10 rollouts)\", \"wall_clock_seconds\": 46070.8, \"gpu_hours\": 12.8, \"checkpoint_path\": \"N/A (eval only)\"}, \"metrics\": {\"overall_success_rate\": 0.12, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}, \"vs_argmin_seed43\": {\"obs_only\": 12, \"argmin\": 17, \"diff\": -5}, \"fisher_pooled\": {\"obs_only_total\": \"31/200\", \"argmin_total\": \"29/200\", \"pooled_obs_only_sr\": 0.155, \"pooled_argmin_sr\": 0.145, \"pooled_delta\": 0.01, \"odds_ratio\": 1.08, \"p_value_one_sided\": 0.4444, \"p_value_two_sided\": 0.8888}, \"source\": \"json_file_verified_by_worker\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T00:41:25.212Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T00:42:01.902179+00:00\"}]}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_seed43.json\", \"completed_at\": \"2026-05-16T00:48:29.446Z\"}, \"eval-mag-obsonly-norm003-b2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:20:45.606Z\", \"updated_at\": \"2026-05-16T00:51:03.335Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_mag_obsonly_norm003.json\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"225139\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm003-b2.log\", \"submitted_at\": \"2026-05-15T05:20:45.407Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_spatial\", \"data_count\": 10, \"model_name\": \"crm_v3_norm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"libero_spatial\", \"wall_clock_seconds\": 70039.8, \"gpu_hours\": 19.46}, \"pid\": 227426, \"notes\": \"Ghost PID 211962 killed, b2 now running solo on bjb2-40593 cuda:0. PID 227434 confirmed alive (15min uptime, model loaded, eval executing, GPU 6185MiB/24564MiB, 12% util).\", \"metrics\": {\"overall_sr_10task\": 0.34, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task\": {\"between_plate_and_ramekin\": 0.9, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.8, \"on_stove\": 0, \"next_to_plate\": 0.3, \"on_wooden_cabinet\": 0}}, \"reproduce\": {\"finished_at\": \"2026-05-16T00:42:50.652Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T00:43:27.876843+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_mag_obsonly_norm003.json\", \"completed_at\": \"2026-05-16T00:48:05.254Z\"}, \"eval-mag-obsonly-norm03-b2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:05:41.192Z\", \"updated_at\": \"2026-05-16T00:49:21.141Z\", \"hypothesis\": \"Magnitude sweep: obs_only CRM v3-norm at norm=0.3 on spatial. Retry of eval-mag-obsonly-norm03 (EXIT_CODE=127). Fills obs_only norm=0.3 gap. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade, strong evidence for obs_only robustness.\", \"parent\": \"eval-mag-obsonly-norm03\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_mag_obsonly_norm03_b2.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"130104\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm03-b2.log\", \"submitted_at\": \"2026-05-15T19:11:50.323Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 20250.8, \"gpu_hours\": 5.63}, \"conclusion\": \"failed\", \"notes\": \"Killed: duplicate of eval-mag-obsonly-norm03-r2 on same cuda:0. r2 had 15min more progress. Both wrote same output_file, causing potential corruption.\", \"reproduce\": {\"finished_at\": \"2026-05-15T07:10:36.759Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T07:10:39.645469+00:00\"}]}, \"completed_at\": \"2026-05-16T00:49:21.141Z\"}, \"eval-argmin-object-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:58:46.739Z\", \"updated_at\": \"2026-05-16T00:37:43.289Z\", \"hypothesis\": \"D031: argmin baseline (K=10, scalar Euclidean argmin) seed=43 on LIBERO object benchmark. Paired with eval-obs-only-object-seed43 for Fisher exact test. Need both conditions under same seed for valid comparison.\", \"parent\": \"eval-reconvla-object\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 43 --K 10 --output_file logs/eval_object_reconvla_seed43.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"356696\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-object-seed43.log\", \"submitted_at\": \"2026-05-15T12:00:40.708Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"ReconVLA (reconvla baseline)\", \"seed\": 43, \"checkpoint_source\": \"N/A (no CRM, pure VLA baseline)\", \"eval_data\": \"LIBERO object benchmark (10 tasks x 10 rollouts)\", \"checkpoint_path\": \"N/A\", \"wall_clock_seconds\": 45422.6, \"gpu_hours\": 12.62}, \"metrics\": {\"overall_success_rate\": 0.17, \"total_successes\": 17, \"total_trials\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.3, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}, \"reproduce\": {\"finished_at\": \"2026-05-16T00:35:16.646Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T00:35:19.825582+00:00\"}]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T00:37:43.289Z\"}, \"eval-mag-perdof-norm02-seed43-object-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:19:36.419Z\", \"updated_at\": \"2026-05-15T19:38:38.710Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed43.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"138858\", \"log_path\": \"N/A\", \"submitted_at\": \"2026-05-15T19:19:36.128Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (killed — GPU conflict on cuda:2, replaced by eval-mag-perdof-norm02-seed43-object-r3)\", \"wall_clock_seconds\": 951.1, \"gpu_hours\": 0.26}, \"hypothesis\": \"Object magnitude sweep: perdof CRM v3-norm norm=0.2 seed=43. Moved from bjb2-28827:cuda:3 (GPU conflict with obs_only spatial) to cuda:2. Tests perdof norm sensitivity with second seed.\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:35:27.220Z\"}, \"eval-mag-obsonly-norm03\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:43:48.583Z\", \"updated_at\": \"2026-05-15T19:38:31.587Z\", \"hypothesis\": \"Magnitude sweep: obs_only CRM v3-norm at norm=0.3 on spatial. Fills obs_only norm=0.3 gap. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade at same norm, strong evidence for obs_only robustness.\", \"parent\": \"eval-mag-obsonly-norm02\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_mag_obsonly_norm03.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"unknown\", \"log_path\": \"N/A\", \"submitted_at\": \"2026-05-15T06:44:02.425Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (EXIT_CODE=127, retried as eval-mag-obsonly-norm03-r2)\", \"wall_clock_seconds\": 46287.3, \"gpu_hours\": 12.86}, \"reproduce\": {\"finished_at\": \"2026-05-15T06:44:32.019Z\"}, \"failure_reason\": \"EXIT_CODE=127 (command not found — check bash -c wrapping / env activate)\", \"conclusion\": \"killed\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T06:44:35.317393+00:00\"}]}, \"notes\": \"失败原因: EXIT_CODE=127 — tmux 用 sh 执行命令，python 不在 sh PATH 中。修复: bash -c 包裹。已重试为 eval-mag-obsonly-norm03-r2。\", \"completed_at\": \"2026-05-15T19:35:29.718Z\"}, \"eval-mag-obsonly-norm02-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:26:53.269Z\", \"updated_at\": \"2026-05-15T19:34:07.651Z\", \"spec\": {\"hypothesis\": \"Object magnitude sweep: obs_only CRM v3-norm at norm=0.2 on LIBERO object benchmark. Fills the norm=0.2 gap in 5-point magnitude curve. Previous run reached 18% at 5/10 then stopped.\", \"parent\": \"eval-acr-object-v4-obs-only\", \"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_v2.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": 141024, \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark\", \"checkpoint_path\": \"N/A (duplicate of DONE eval-acr-object-obs-only-norm02, killed to free GPU)\", \"log_path\": \"N/A\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:34:07.651Z\"}, \"eval-mag-obsonly-norm03-b4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:14:01.998Z\", \"updated_at\": \"2026-05-15T19:27:30.465Z\", \"spec\": {\"command\": \"crm_obs_only spatial norm=0.3 (killed)\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"132816\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm03-b4.log\", \"submitted_at\": \"2026-05-15T19:14:01.050Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"spatial\", \"data_count\": 10, \"model_name\": \"crm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"spatial\", \"wall_clock_seconds\": 809.4, \"gpu_hours\": 0.22}, \"conclusion\": \"killed\", \"notes\": \"Redundant: spatial obs_only norm=0.3 already has 10t final data (36%). Killed from cuda:2 GPU contention cleanup on bjb2-28827 (2026-05-16).\", \"completed_at\": \"2026-05-15T19:27:30.465Z\"}, \"eval-mag-obsonly-norm03-b3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:13:38.067Z\", \"updated_at\": \"2026-05-15T19:27:28.479Z\", \"spec\": {\"command\": \"crm_obs_only spatial norm=0.3 (killed)\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"134532\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm03-b3.log\", \"submitted_at\": \"2026-05-15T19:14:52.972Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"spatial\", \"data_count\": 10, \"model_name\": \"crm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"spatial\", \"wall_clock_seconds\": 755.5, \"gpu_hours\": 0.21}, \"hypothesis\": \"Retry of eval-mag-obsonly-norm03-b2 (spatial magnitude sweep obs_only norm=0.3). Submitted on bjb2-28827:cuda:2 instead of bjb1-32546:cuda:3 (cuda:3 occupied by P0 obs-only-norm02-seed43-r2). Director approved.\", \"parent\": \"eval-mag-obsonly-norm03-b2\", \"conclusion\": \"killed\", \"notes\": \"Redundant: spatial obs_only norm=0.3 already has 10t final data (36%). Killed from cuda:2 GPU contention cleanup on bjb2-28827 (2026-05-16).\", \"completed_at\": \"2026-05-15T19:27:28.479Z\"}, \"eval-mag-perdof-norm02-seed43-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:15:19.724Z\", \"updated_at\": \"2026-05-15T19:25:28.957Z\", \"spec\": {\"hypothesis\": \"Object magnitude sweep: perdof CRM v3-norm norm=0.2 seed=43 on LIBERO object benchmark. Paired with obs_only norm=0.2 seed=43 for statistical comparison at the best obs_only norm.\", \"parent\": \"eval-mag-perdof-norm02-object\", \"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed43.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": \"10 rollouts\", \"model_name\": \"crm_v3_norm/perdof\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark\"}, \"conclusion\": \"killed\", \"notes\": \"Killed during cuda:2/3 GPU cleanup on bjb2-28827 (2026-05-16). Was sharing cuda:2 with perdof norm=0.3 r2.\", \"completed_at\": \"2026-05-15T19:25:28.957Z\"}, \"eval-mag-perdof-norm03-object-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:15:16.452Z\", \"updated_at\": \"2026-05-15T19:25:28.055Z\", \"spec\": {\"hypothesis\": \"Object magnitude sweep: perdof CRM v3-norm at norm=0.3 on LIBERO object benchmark. Retry of killed eval-mag-perdof-norm0p3-object. Completes perdof 5-point magnitude curve on object domain.\", \"parent\": \"eval-acr-object-v4-perdof\", \"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_r2.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": \"10 rollouts\", \"model_name\": \"crm_v3_norm/perdof\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark\"}, \"conclusion\": \"killed\", \"notes\": \"GPU contention on cuda:2 (shared with perdof norm=0.2 seed=43). Killed 2026-05-16. Replaced by r3 clean restart.\", \"completed_at\": \"2026-05-15T19:25:28.055Z\"}, \"eval-acr-object-v4-scalar-b2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T02:55:02.698Z\", \"updated_at\": \"2026-05-15T19:17:41.948Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"7017\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-scalar-b2.log\", \"submitted_at\": \"2026-05-15T02:55:02.415Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 58959.5, \"gpu_hours\": 16.38}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:17:41.948Z\"}, \"eval-acr-object-v4-obs-only-b2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T02:55:00.179Z\", \"updated_at\": \"2026-05-15T19:17:40.199Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"pid\": \"6746\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-obs-only-b2.log\", \"submitted_at\": \"2026-05-15T02:54:59.912Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 58960.3, \"gpu_hours\": 16.38}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:17:40.199Z\"}, \"eval-spatial-v4-full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T18:58:07.302Z\", \"updated_at\": \"2026-05-15T19:17:39.068Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl && python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 10 --seed 42 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ 2>&1\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"69379\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-spatial-v4-full.log\", \"submitted_at\": \"2026-05-13T18:58:07.274Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"D015: evaluate.py env_args 缺少 camera_names，SmolVLA 只收到单摄像头输入，结果系统性偏低\", \"wall_clock_seconds\": 173971.8, \"gpu_hours\": 48.33}, \"conclusion\": \"killed\", \"reproduce\": {\"finished_at\": \"2026-05-13T19:36:15.749Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T19:36:19.370112+00:00\"}]}, \"completed_at\": \"2026-05-15T19:17:39.068Z\"}, \"eval-reconvla-spatial-v1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:15:35.450Z\", \"updated_at\": \"2026-05-15T19:17:37.622Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --smolvla_path /root/autodl-tmp/models/smolvla_libero/\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"87787\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-reconvla-spatial-v1.log\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": \"10 tasks x 10 rollouts x 300 steps\", \"model_name\": \"lerobot/smolvla_libero (450M) + ReconVLA argmin selection K=10\", \"seed\": 42, \"hypothesis\": \"ReconVLA (scalar Euclidean nonconformity + argmin) as baseline for ACR-VLA comparison\", \"checkpoint_source\": \"lerobot/smolvla_libero\"}, \"reproduce\": {\"finished_at\": \"2026-05-13T22:59:43.231Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"conclusion\": \"killed\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T20:26:37.521060+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T22:59:44.694612+00:00\"}]}, \"completed_at\": \"2026-05-15T19:17:37.622Z\"}, \"eval-object-v6-full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:28:33.119Z\", \"updated_at\": \"2026-05-15T19:17:36.369Z\", \"spec\": {\"data_path\": \"/root/autodl-tmp/libero_data/ (object)\", \"data_count\": 100, \"model_name\": \"lerobot/smolvla_libero\", \"seed\": 42, \"hypothesis\": \"SmolVLA baseline success rate on libero_object with fixed evaluate.py (env.reset bug removed, 5-step zero-action stabilization)\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"libero_object 10 tasks x 10 rollouts\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:17:36.369Z\"}, \"precompute-v4-shard2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T18:58:14.301Z\", \"updated_at\": \"2026-05-15T19:17:35.000Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 2 --num_shards 3 --seed 42 --K 10 --cache_dir /root/autodl-tmp/crm_cache/ 2>&1\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"69937\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v4-shard2.log\", \"submitted_at\": \"2026-05-13T18:58:14.266Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache/\", \"wall_clock_seconds\": 173960.7, \"gpu_hours\": 48.32}, \"reproduce\": {\"finished_at\": \"2026-05-13T20:09:25.582Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T20:09:26.379476+00:00\"}]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T19:17:35.000Z\"}, \"precompute-v4-shard1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T18:58:12.183Z\", \"updated_at\": \"2026-05-15T19:17:33.288Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 1 --num_shards 3 --seed 42 --K 10 --cache_dir /root/autodl-tmp/crm_cache/ 2>&1\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"69793\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v4-shard1.log\", \"submitted_at\": \"2026-05-13T18:58:12.154Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache/\", \"wall_clock_seconds\": 173961.1, \"gpu_hours\": 48.32}, \"reproduce\": {\"finished_at\": \"2026-05-13T20:04:22.574Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T20:04:23.366356+00:00\"}]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T19:17:33.288Z\"}, \"precompute-v4-shard0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T18:58:09.830Z\", \"updated_at\": \"2026-05-15T19:17:32.128Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 0 --num_shards 3 --seed 42 --K 10 --cache_dir /root/autodl-tmp/crm_cache/ 2>&1\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"69647\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v4-shard0.log\", \"submitted_at\": \"2026-05-13T18:58:09.802Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache/\", \"wall_clock_seconds\": 173962.3, \"gpu_hours\": 48.32}, \"reproduce\": {\"finished_at\": \"2026-05-13T20:04:45.258Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T20:04:50.222546+00:00\"}]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T19:17:32.128Z\"}, \"precompute-v3-shard2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T17:39:04.708Z\", \"updated_at\": \"2026-05-15T19:17:30.541Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 2 --num_shards 3 --seed 42 --K 10 --cache_dir /root/autodl-tmp/crm_cache_v3\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"63218\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v3-shard2.log\", \"submitted_at\": \"2026-05-13T17:39:04.684Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"D014: wrapper 修复版从未部署到服务器，使用旧 buggy 代码运行，产出无效\", \"wall_clock_seconds\": 178705.9, \"gpu_hours\": 49.64}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:17:30.541Z\"}, \"precompute-v3-shard1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T17:39:02.628Z\", \"updated_at\": \"2026-05-15T19:17:29.292Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 1 --num_shards 3 --seed 42 --K 10 --cache_dir /root/autodl-tmp/crm_cache_v3\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"63075\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v3-shard1.log\", \"submitted_at\": \"2026-05-13T17:39:02.603Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"D014: wrapper 修复版从未部署到服务器，使用旧 buggy 代码运行，产出无效\", \"wall_clock_seconds\": 178706.7, \"gpu_hours\": 49.64}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:17:29.293Z\"}, \"precompute-v3-shard0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T17:39:00.259Z\", \"updated_at\": \"2026-05-15T19:17:27.703Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 && rm -rf /root/autodl-tmp/crm_cache_v3 && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 0 --num_shards 3 --seed 42 --K 10 --cache_dir /root/autodl-tmp/crm_cache_v3\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"62930\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v3-shard0.log\", \"submitted_at\": \"2026-05-13T17:39:00.236Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"D014: wrapper 修复版从未部署到服务器，使用旧 buggy 代码运行，产出无效\", \"wall_clock_seconds\": 178707.5, \"gpu_hours\": 49.64}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:17:27.703Z\"}, \"precompute-v2-shard2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T16:11:04.275Z\", \"updated_at\": \"2026-05-15T19:17:26.396Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 2 --num_shards 3 --seed 42 --K 10\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"57846\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v2-shard2.log\", \"submitted_at\": \"2026-05-13T16:11:04.255Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 183982.1, \"gpu_hours\": 51.11}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:17:26.396Z\"}, \"precompute-v2-shard1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T16:11:02.520Z\", \"updated_at\": \"2026-05-15T19:17:25.022Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 1 --num_shards 3 --seed 42 --K 10\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"57706\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v2-shard1.log\", \"submitted_at\": \"2026-05-13T16:11:02.500Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 183982.5, \"gpu_hours\": 51.11}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:17:25.022Z\"}, \"precompute-v2-shard0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T16:11:01.629Z\", \"updated_at\": \"2026-05-15T19:17:23.631Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && rm -rf /root/autodl-tmp/crm_cache/spatial /root/autodl-tmp/crm_cache/object && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 0 --num_shards 3 --seed 42 --K 10\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"57628\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v2-shard0.log\", \"submitted_at\": \"2026-05-13T16:11:01.605Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 183982.0, \"gpu_hours\": 51.11}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:17:23.631Z\"}, \"eval-mag-perdof-norm0p3-object-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:58:30.091Z\", \"updated_at\": \"2026-05-15T19:13:43.549Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_r2.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"127570\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-perdof-norm0p3-object-r2.log\", \"submitted_at\": \"2026-05-15T18:58:29.637Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"libero_object 10 tasks x 10 rollouts\", \"data_path\": \"/root/autodl-tmp/libero_data/ (object)\", \"data_count\": 100, \"model_name\": \"crm_perdof_v3_norm\", \"seed\": 42, \"wall_clock_seconds\": 885.6, \"gpu_hours\": 0.25}, \"hypothesis\": \"Object magnitude sweep: perdof CRM v3-norm at norm=0.3 on LIBERO object benchmark. Migrated from bjb1-32546:cuda:4 (GPU conflict) to bjb2-28827:cuda:2. Paired with obs_only norm=0.3 for magnitude comparison figure.\", \"parent\": \"eval-mag-perdof-norm0p3-object\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:13:15.247Z\", \"failure_reason\": \"Duplicate of eval-mag-perdof-norm03-object (PID 118886 on bjb2-28827:cuda:3, identical params). Killed to free cuda:2.\"}, \"eval-vla-only-object-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:50:14.071Z\", \"updated_at\": \"2026-05-15T19:11:30.342Z\", \"spec\": {\"hypothesis\": \"D031: VLA-only baseline (K=1, single sample, no CRM) seed=43 on LIBERO object benchmark. Completes 7-way seed=43 comparison table. VLA-only seed=42 = 12% = argmin.\", \"parent\": \"eval-vla-only-object\", \"command\": \"CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 43 --K 1 --output_file logs/eval_object_vla_only_seed43.json\", \"server\": \"bjb1-32546\", \"data_path\": \"libero_object\", \"data_count\": 10, \"model_name\": \"vla_only\", \"seed\": 43, \"eval_data\": \"object\"}, \"metrics\": {\"overall_sr\": 0.12, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}, \"source\": \"json_file_verified_by_worker\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T18:46:38.180Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T18:46:39.481Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T18:46:41.461084+00:00\"}]}, \"notes\": \"seed=43 VLA-only 12% = seed=42 12%，baseline 跨 seed 完全一致。per-task 分布略有差异（seed43: chocolate_pudding 40% vs seed42: 20%, bbq_sauce 30% vs 20%），但总 SR 相同。确认 VLA-only 作为稳定 baseline。seed=43 六方对比表第一个完成点。\"}, \"eval-mag-perdof-norm0p3-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:34:52.454Z\", \"updated_at\": \"2026-05-15T18:58:11.790Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"144887\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-perdof-norm0p3-object.log\", \"submitted_at\": \"2026-05-15T18:37:26.089Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1245.7, \"gpu_hours\": 0.35}, \"hypothesis\": \"Retry of eval-mag-perdof-norm03-object (killed by SIGTERM). Object magnitude sweep: perdof CRM v3-norm at norm=0.3 on LIBERO object benchmark. Paired with obs_only norm=0.3 (running) for magnitude comparison figure.\", \"parent\": \"eval-mag-perdof-norm03-object\", \"conclusion\": \"killed\", \"failure_reason\": \"GPU conflict on bjb1-32546:cuda:4 (shared with obs-only-default). Killed lower priority perdof. Migrating to bjb2-28827:cuda:2 as r2.\", \"completed_at\": \"2026-05-15T18:58:11.790Z\"}, \"eval-obs-only-object-norm02-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:38:18.819Z\", \"updated_at\": \"2026-05-15T18:58:10.821Z\", \"hypothesis\": \"D031: obs_only CRM v3-norm norm=0.2 seed=43 on LIBERO object benchmark. norm=0.2 shows strongest signal (18% SR at 5/10 tasks in seed=42). Seed=43 doubling for statistical power on the best-performing configuration.\", \"parent\": \"eval-acr-object-obs-only-norm02\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_seed43.json\", \"server\": \"bjb1-32546\", \"data_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed43.json\", \"data_count\": 10, \"model_name\": \"crm_obs_only\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"object\"}, \"metrics\": {\"pid\": 118214, \"gpu\": 3, \"process_status\": \"alive\", \"log_file\": \"logs/eval_object_obs_only_norm02_seed43.log\"}, \"conclusion\": \"failed\", \"failure_reason\": \"Crashed after 1 task on bjb1-32546:cuda:3 (PID 118214). Reviewer confirmed. Restarting as r2.\", \"completed_at\": \"2026-05-15T18:58:10.821Z\"}, \"eval-acr-object-v4-default\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:18:17.209Z\", \"updated_at\": \"2026-05-15T17:38:37.815Z\", \"hypothesis\": \"Ablation: perdof CRM v3-norm with DEFAULT max_correction_norm (~1.42, no magnitude control) on LIBERO object benchmark. Tests whether magnitude control is essential on object domain too. If v4-default << v4-perdof (norm=0.1) → magnitude control is universally needed. If v4-default ≈ v4-perdof → spatial failure was anomalous.\", \"parent\": \"eval-acr-object-v4-perdof\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_object_perdof_default_norm.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"107658\", \"log_path\": \"logs/eval_object_perdof_default_norm.log\", \"submitted_at\": \"2026-05-16T00:51:00Z\", \"backend\": \"nohup\", \"account\": \"root\", \"data_path\": \"libero_object\", \"data_count\": 10, \"model_name\": \"crm_perdof_default_norm\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"object\"}, \"metrics\": {\"tasks_done\": 3, \"tasks_total\": 10, \"status\": \"DEAD\", \"partial_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0}, \"pid_42311\": \"not_found\", \"needs_restart\": true, \"checked_at\": \"2026-05-16T01:00Z\"}, \"notes\": \"Killed per Director instruction. 3/10 tasks all 0% SR, no magnitude control (norm≈1.42). Conclusion obvious — magnitude control is essential.\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T17:38:37.815Z\"}, \"eval-mag-perdof-norm03-object\": {\"status\": \"DEPLOYED\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:57:00.172Z\", \"updated_at\": \"2026-05-15T17:38:28.909Z\", \"spec\": {\"pid\": 115384, \"gpu_ids\": [2], \"server\": \"bjb2-28827\", \"command\": \"python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03.json\"}, \"server\": \"bjb2-28827\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb2-28827\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-15T17:16:56.760Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03.json\\\"\", \"finished_at\": \"2026-05-15T17:29:42.220Z\", \"training_hours\": 0.21}, \"pid\": 118886, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-perdof-norm03-object.log\", \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T17:29:45.210Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:29:48.614116+00:00\"}]}, \"notes\": \"Restarted on cuda:3 (PID 118886, tmux: eval-mag-perdof-norm03-object) after v4-default killed. Previous run killed by SIGTERM before first rollout.\"}, \"eval-acr-object-obs-only-norm02\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:20:46.639Z\", \"updated_at\": \"2026-05-15T17:37:08.420Z\", \"spec\": {\"hypothesis\": \"obs-only CRM with norm=0.2 on object benchmark. Cross-benchmark norm sensitivity test — paired with eval-mag-obsonly-norm02 on spatial. If obs-only at norm=0.2 > norm=0.1 on both benchmarks → robust 'observation-conditioned correction' story.\", \"parent\": \"eval-acr-object-v4-obs-only\", \"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02.json\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:4\", \"pid\": 44270, \"tmux_session\": \"eval-acr-object-obs-only-norm02\", \"data_path\": \"LIBERO object benchmark (10 tasks)\", \"data_count\": 100, \"model_name\": \"crm_obs_only (327198 params)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark, 10 tasks x 10 rollouts\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-obs-only-norm02.log\"}, \"metrics\": {\"overall_sr\": 0.22, \"total_success\": 22, \"total_rollouts\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.4, \"ketchup\": 0.2, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.6, \"orange_juice\": 0.3}}, \"reproduce\": {\"finished_at\": \"2026-05-15T17:35:34.272Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:35:39.374197+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-obs-only-norm02.log\", \"completed_at\": \"2026-05-15T17:37:08.420Z\"}, \"eval-mag-perdof-norm02\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:16:13.281Z\", \"updated_at\": \"2026-05-15T17:30:15.807Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode acr_vla --max_correction_norm 0.2 --n_rollouts 10 --K 10 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_mag_perdof_norm02.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"SmolVLA + CRM-v3-norm-perdof\", \"seed\": 42, \"checkpoint_source\": \"crm-train-v3-norm-perdof\", \"eval_data\": \"LIBERO spatial\"}, \"gpu\": \"bjb2-28827:cuda:2\", \"pid\": 13728, \"metrics\": {\"tasks_done\": \"6/10\", \"partial_results\": {\"T0_between_plate_ramekin\": \"60%\", \"T1_next_to_ramekin\": \"90%\", \"T2_table_center\": \"0%\", \"T3_on_cookie_box\": \"20%\", \"T4_top_drawer\": \"0%\", \"T5_on_ramekin\": \"0%\"}, \"running_avg_6task\": \"28.3%\", \"snapshot_time\": \"2026-05-15T09:00:00Z\", \"server\": \"bjb2-28827\", \"process_status\": \"alive\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T17:30:14.331Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T17:30:15.807Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:30:23.476790+00:00\"}]}}, \"eval-mag-perdof-norm005\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:16:10.924Z\", \"updated_at\": \"2026-05-15T17:24:59.482Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode acr_vla --max_correction_norm 0.05 --n_rollouts 10 --K 10 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_mag_perdof_norm005.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"SmolVLA + CRM-v3-norm-perdof\", \"seed\": 42, \"checkpoint_source\": \"crm-train-v3-norm-perdof\", \"eval_data\": \"LIBERO spatial\", \"log_path\": \"/root/runs/acr-vla-conformal-refinement/eval-mag-perdof-norm005.log\", \"checkpoint_path\": \"N/A (eval only)\"}, \"gpu\": \"bjb2-28827:cuda:1\", \"pid\": 13456, \"metrics\": {\"T0_between_plate_ramekin\": 50, \"T1_next_to_ramekin\": 100, \"T2_table_center\": 0, \"T3_on_cookie_box\": 30, \"T4_top_drawer\": 0, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 100, \"T7_on_stove\": 0, \"T8_next_to_plate\": 30, \"T9_on_wooden_cabinet\": 0, \"avg_SR_10task\": 31}, \"reproduce\": {\"finished_at\": \"2026-05-15T16:52:50.451Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T16:52:53.898813+00:00\"}]}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-15T17:24:59.482Z\"}, \"eval-mag-obsonly-norm03-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:49:38.786Z\", \"updated_at\": \"2026-05-15T17:22:51.755Z\", \"hypothesis\": \"Retry of eval-mag-obsonly-norm03 (EXIT_CODE=127 fix). Magnitude sweep: obs_only CRM v3-norm at norm=0.3 on spatial. Fills obs_only norm=0.3 gap. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade at same norm, strong evidence for obs_only robustness.\", \"parent\": \"eval-mag-obsonly-norm03\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_mag_obsonly_norm03.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": 325264, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm03-r2.log\", \"submitted_at\": \"2026-05-15T06:50:02.511Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": 100, \"model_name\": \"crm_v3_norm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 37969.2, \"gpu_hours\": 10.55}, \"metrics\": {\"bowl_between\": 0.9, \"next_to_ramekin\": 1, \"table_center\": 0, \"cookie_box\": 0.3, \"top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"stove\": 0, \"next_to_plate\": 0.3, \"wooden_cabinet\": 0, \"overall_SR\": 0.36}, \"reproduce\": {\"finished_at\": \"2026-05-15T17:20:31.567Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:20:34.907634+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm03-r2.log\", \"completed_at\": \"2026-05-15T17:22:51.755Z\"}, \"eval-mag-perdof-norm03\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:16:16.095Z\", \"updated_at\": \"2026-05-15T17:17:49.711Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --smolvla_path /root/autodl-tmp/models/smolvla_libero/\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": 100, \"model_name\": \"crm_v3_norm/perdof\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"log_path\": \"/root/runs/acr-vla-conformal-refinement/eval-mag-perdof-norm03.log\"}, \"gpu\": \"bjb2-28827:cuda:3\", \"pid\": 14260, \"metrics\": {\"overall_sr_10task\": 0.26, \"T0_sr\": 0.7, \"T1_sr\": 0.5, \"T2_sr\": 0.1, \"T3_sr\": 0.1, \"T4_sr\": 0, \"T5_sr\": 0, \"T6_sr\": 0.9, \"T7_sr\": 0.1, \"T8_sr\": 0.2, \"T9_sr\": 0, \"total_successes\": 26, \"total_rollouts\": 100, \"benchmark\": \"spatial\", \"max_correction_norm\": 0.3}, \"reproduce\": {\"finished_at\": \"2026-05-15T16:53:04.031Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T16:53:08.939326+00:00\"}]}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-15T17:17:49.711Z\"}, \"eval-vla-mean-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:31:09.989Z\", \"updated_at\": \"2026-05-15T17:01:25.883Z\", \"spec\": {\"command\": \"python eval_vla.py --benchmark object --mode vla_only --baseline_mode mean --n_rollouts 10 --K 10 --seed 42\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"smolvla_libero\", \"seed\": 42, \"eval_data\": \"LIBERO object\", \"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean.log\"}, \"hypothesis\": \"VLA mean baseline (K=10, mean aggregation) on LIBERO object benchmark. Matches reconvla spatial baseline but on object tasks.\", \"metrics\": {\"benchmark\": \"object\", \"mode\": \"vla_only\", \"baseline_mode\": \"mean\", \"n_rollouts\": 10, \"K\": 10, \"seed\": 42, \"overall_sr\": 12, \"total_success\": 12, \"total_rollouts\": 100, \"tasks_done\": \"10/10\", \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 10, \"bbq_sauce\": 30, \"ketchup\": 10, \"tomato_sauce\": 10, \"butter\": 0, \"milk\": 20, \"chocolate_pudding\": 30, \"orange_juice\": 10}, \"json_output\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean.json\"}, \"conclusion\": \"success\", \"gpu\": \"bjb1-32546:cuda:5\", \"pid\": 18808, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean.log\", \"completed_at\": \"2026-05-15T17:01:25.883Z\"}, \"eval-mag-perdof-norm003\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:16:08.547Z\", \"updated_at\": \"2026-05-15T16:40:16.878Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode acr_vla --max_correction_norm 0.03 --n_rollouts 10 --K 10 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_mag_perdof_norm003.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"SmolVLA + CRM-v3-norm-perdof\", \"seed\": 42, \"checkpoint_source\": \"crm-train-v3-norm-perdof\", \"eval_data\": \"LIBERO spatial\"}, \"gpu\": \"bjb2-28827:cuda:0\", \"pid\": 13185, \"metrics\": {\"benchmark\": \"spatial\", \"mode\": \"acr_vla\", \"max_correction_norm\": 0.03, \"n_rollouts\": 10, \"K\": 10, \"seed\": 42, \"overall_sr\": 30, \"total_success\": 30, \"total_rollouts\": 100, \"tasks_done\": \"10/10\", \"per_task\": {\"T0_between_plate_ramekin\": 60, \"T1_next_to_ramekin\": 100, \"T2_table_center\": 0, \"T3_on_cookie_box\": 30, \"T4_top_drawer\": 10, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 80, \"T7_on_stove\": 0, \"T8_next_to_plate\": 20, \"T9_on_wooden_cabinet\": 0}}, \"reproduce\": {\"finished_at\": \"2026-05-15T16:32:37.390Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T16:32:42.080703+00:00\"}]}, \"log_path\": \"/root/runs/acr-vla-conformal-refinement/eval-mag-perdof-norm003.log\", \"checkpoint_path\": \"N/A (eval-only)\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-15T16:40:16.878Z\"}, \"eval-reconvla-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T01:48:28.744Z\", \"updated_at\": \"2026-05-15T16:25:17.101Z\", \"spec\": {\"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_reconvla.log\", \"json_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_reconvla.json\"}, \"hypothesis\": \"ReconVLA baseline (scalar Euclidean argmin, K=10) on LIBERO object benchmark. Tests whether simple sample selection improves over VLA mean on object manipulation tasks. Provides baseline for CRM comparison on object domain.\", \"metrics\": {\"overall_sr\": 0.12, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}, \"n_rollouts\": 10, \"total_episodes\": 100, \"total_successes\": 12}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T16:25:17.101Z\"}, \"eval-acr-object-v4-obs-only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T02:53:41.689Z\", \"updated_at\": \"2026-05-15T16:23:01.718Z\", \"hypothesis\": \"D021: obs_only CRM v3-norm with max_correction_norm=0.1 on LIBERO object benchmark. Cross-benchmark validation — obs-only leads spatial at 57.5%.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"13797\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-obs-only.log\", \"submitted_at\": \"2026-05-15T02:53:41.526Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 47312.8, \"gpu_hours\": 13.14}, \"metrics\": {\"overall_sr\": \"19.0% (19/100)\", \"total_success\": 19, \"total_rollouts\": 100, \"mode\": \"obs_only\", \"benchmark\": \"object\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"tasks_done\": \"10/10\", \"per_task\": {\"alphabet_soup\": \"0%\", \"cream_cheese\": \"10%\", \"salad_dressing\": \"20%\", \"bbq_sauce\": \"40%\", \"ketchup\": \"10%\", \"tomato_sauce\": \"0%\", \"butter\": \"10%\", \"milk\": \"20%\", \"chocolate_pudding\": \"50%\", \"orange_juice\": \"30%\"}, \"json_output\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T15:59:31.860Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T15:59:34.042176+00:00\"}]}, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-obs-only.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T16:02:14.366Z\"}, \"eval-acr-object-v4-scalar\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T02:53:44.102Z\", \"updated_at\": \"2026-05-15T16:10:02.679Z\", \"hypothesis\": \"D021: scalar_unc CRM v3-norm with max_correction_norm=0.1 on LIBERO object benchmark. Three-way ablation: perdof vs scalar_unc vs obs_only on object.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"14003\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-scalar.log\", \"submitted_at\": \"2026-05-15T02:53:43.910Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 47778.8, \"gpu_hours\": 13.27}, \"metrics\": {\"overall_sr\": 9, \"total_success\": 9, \"total_trials\": 100, \"n_tasks\": 10, \"n_rollouts_per_task\": 10, \"per_task\": {\"alphabet_soup\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"cream_cheese\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"salad_dressing\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"bbq_sauce\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"ketchup\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"tomato_sauce\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"butter\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"milk\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"chocolate_pudding\": {\"sr\": 30, \"success\": 3, \"trials\": 10}, \"orange_juice\": {\"sr\": 20, \"success\": 2, \"trials\": 10}}}, \"reproduce\": {\"finished_at\": \"2026-05-15T16:07:26.276Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T16:07:28.510451+00:00\"}]}, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-scalar.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-15T16:10:02.679Z\"}, \"eval-mag-obsonly-norm02\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:16:21.006Z\", \"updated_at\": \"2026-05-15T16:06:23.063Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --max_correction_norm 0.2 --n_rollouts 10 --K 10 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_mag_obs_only_norm02.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"SmolVLA + CRM-v3-norm-obs_only\", \"seed\": 42, \"checkpoint_source\": \"crm-train-v3-norm-obs_only\", \"eval_data\": \"LIBERO spatial\"}, \"gpu\": \"bjb2-28827:cuda:5\", \"pid\": 15190, \"metrics\": {\"T0_between_plate_ramekin\": 90, \"T1_next_to_ramekin\": 100, \"T2_table_center\": 0, \"T3_on_cookie_box\": 30, \"T4_top_drawer\": 10, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 90, \"T7_on_stove\": 0, \"T8_next_to_plate\": 30, \"T9_on_wooden_cabinet\": 0, \"overall_sr\": 35, \"total_success\": 35, \"total_rollouts\": 100}, \"reproduce\": {\"finished_at\": \"2026-05-15T16:03:26.878Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T16:03:29.305763+00:00\"}]}, \"log_path\": \"/root/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm02.log\", \"conclusion\": \"negative\", \"checkpoint_path\": \"N/A (eval-only experiment)\", \"completed_at\": \"2026-05-15T16:06:23.063Z\"}, \"eval-mag-obsonly-norm005\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:16:18.917Z\", \"updated_at\": \"2026-05-15T16:02:08.945Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --max_correction_norm 0.05 --n_rollouts 10 --K 10 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_mag_obs_only_norm005.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"SmolVLA + CRM-v3-norm-obs_only\", \"seed\": 42, \"checkpoint_source\": \"crm-train-v3-norm-obs_only\", \"eval_data\": \"LIBERO spatial\"}, \"gpu\": \"bjb2-28827:cuda:4\", \"pid\": 14854, \"metrics\": {\"benchmark\": \"spatial\", \"mode\": \"crm_obs_only\", \"max_correction_norm\": 0.05, \"n_rollouts\": 10, \"K\": 10, \"overall_sr\": 35, \"total_success\": 35, \"total_episodes\": 100, \"per_task\": {\"T0_between_plate_ramekin\": 80, \"T1_next_to_ramekin\": 90, \"T2_table_center\": 0, \"T3_on_cookie_box\": 40, \"T4_top_drawer\": 10, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 80, \"T7_on_stove\": 0, \"T8_next_to_plate\": 50, \"T9_on_wooden_cabinet\": 0}}, \"reproduce\": {\"finished_at\": \"2026-05-15T16:00:02.717Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T16:00:09.569232+00:00\"}]}, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm005.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T16:02:08.945Z\"}, \"eval-acr-object-v4-perdof\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T02:49:13.626Z\", \"updated_at\": \"2026-05-15T15:45:38.531Z\", \"hypothesis\": \"D021: ACR-VLA perdof CRM v3-norm with max_correction_norm=0.1 on LIBERO object benchmark. Cross-benchmark validation of spatial findings.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode acr_vla --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1\", \"server\": \"bjb1-32546\", \"gpu_ids\": [\"cuda:1\"], \"pid\": \"11116\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v3-norm perdof, max_correction_norm=0.1, object)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\", \"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-perdof.log\"}, \"metrics\": {\"overall_sr\": \"11.0% (11/100)\", \"total_success\": 11, \"total_rollouts\": 100, \"mode\": \"perdof\", \"benchmark\": \"object\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"alphabet_soup\": \"0%\", \"cream_cheese\": \"0%\", \"salad_dressing\": \"20%\", \"bbq_sauce\": \"30%\", \"ketchup\": \"0%\", \"tomato_sauce\": \"0%\", \"butter\": \"10%\", \"milk\": \"0%\", \"chocolate_pudding\": \"20%\", \"orange_juice\": \"30%\"}, \"note\": \"perdof object 11% vs argmin ~7% (partial). obs_only leads at ~14% (8/10). Confirms perdof not competitive on object.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T15:45:38.531Z\"}, \"eval-acr-spatial-v4-scalar-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:14:04.283Z\", \"updated_at\": \"2026-05-15T13:18:27.852Z\", \"hypothesis\": \"Restart from T3. scalar_unc CRM v3-norm with max_correction_norm=0.1 on spatial. Three-way ablation: perdof vs scalar_unc vs obs_only.\", \"parent\": \"eval-acr-spatial-v4-scalar\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_scalar --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1 --start_task 3\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": 311881, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-scalar-r2.log\", \"submitted_at\": \"2026-05-15T05:14:33.525Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO spatial\", \"data_count\": 70, \"model_name\": \"ACR-VLA CRM scalar_unc v3-norm (restart from T3)\", \"seed\": 42, \"eval_data\": \"LIBERO spatial tasks 3-9\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"checkpoint_path\": \"N/A (eval-only)\", \"wall_clock_seconds\": 29034.3, \"gpu_hours\": 8.07}, \"metrics\": {\"overall_sr\": \"32.0% (32/100)\", \"total_success\": 32, \"total_rollouts\": 100, \"mode\": \"scalar_unc\", \"benchmark\": \"spatial\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"T0\": \"60%\", \"T1\": \"100%\", \"T2\": \"10%\", \"T3\": \"40%\", \"T4\": \"0%\", \"T5\": \"0%\", \"T6\": \"90%\", \"T7\": \"0%\", \"T8\": \"10%\", \"T9\": \"10%\"}, \"note\": \"D030 confirmed: scalar_unc spatial 32% vs argmin 34% = -2pp. T0-T2 from original eval-acr-spatial-v4-scalar, T3-T9 from r2 restart. All CRM variants dead on spatial.\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T13:15:46.765Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T13:15:49.226583+00:00\"}]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T13:18:27.853Z\"}, \"eval-acr-spatial-v4-obs-only-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:14:05.934Z\", \"updated_at\": \"2026-05-15T11:15:11.801Z\", \"hypothesis\": \"Restart from T6. obs_only CRM v3-norm with max_correction_norm=0.1 on spatial. If obs_only >= perdof, conformal features need restructuring.\", \"parent\": \"eval-acr-spatial-v4-obs-only-r2\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --start_task 6\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": 312420, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-obs-only-r3.log\", \"submitted_at\": \"2026-05-15T05:14:38.600Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO spatial\", \"data_count\": 40, \"model_name\": \"ACR-VLA CRM obs_only v3-norm (restart from T6)\", \"seed\": 42, \"eval_data\": \"LIBERO spatial tasks 6-9\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"wall_clock_seconds\": 21633.2, \"gpu_hours\": 6.01}, \"metrics\": {\"overall_sr\": \"35.0% (35/100)\", \"total_success\": 35, \"total_rollouts\": 100, \"mode\": \"crm_obs_only\", \"benchmark\": \"spatial\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"T0\": \"90%\", \"T1\": \"100%\", \"T2\": \"0%\", \"T3\": \"40%\", \"T4\": \"10%\", \"T5\": \"0%\", \"T6\": \"90%\", \"T7\": \"0%\", \"T8\": \"20%\", \"T9\": \"0%\"}, \"r3_subset_T6_T9\": \"27.5% (11/40)\", \"note\": \"D030: obs_only spatial 10-task = 35%. vs argmin 34% = +1pp. Scenario C threshold (>=39%) NOT MET. Earlier T0-T5 advantage (+5pp) wiped out by T6-T9.\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T10:15:39.276Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T10:15:44.340640+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-obs-only-r3.log\", \"completed_at\": \"2026-05-15T11:15:11.801Z\"}, \"eval-obs-only-spatial-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T09:09:04.411Z\", \"updated_at\": \"2026-05-15T10:01:21.065Z\", \"hypothesis\": \"D029: obs_only seed=43 复现实验。obs_only 是项目唯一存活路径。seed=42 如果确认 +5pp over argmin，seed=43 增加统计力（200 vs 200 样本下 Fisher exact p ~0.12，配合 object benchmark 独立验证有望通过）。\", \"parent\": \"eval-acr-spatial-v4-obs-only-r3\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_obs_only_spatial_seed43.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"341873\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-spatial-seed43.log\", \"submitted_at\": \"2026-05-15T09:09:23.712Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": 100, \"model_name\": \"crm_v3_norm_obs_only\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO spatial (10 tasks x 10 rollouts)\", \"wall_clock_seconds\": 3117.4, \"gpu_hours\": 0.87}, \"notes\": \"D029: perdof spatial 35% vs argmin 34% = +1pp, kill criterion triggered. Per-DOF claim dead on spatial. obs_only 是唯一存活路径，seed=43 用于增加统计力。\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T10:01:21.065Z\"}, \"eval-acr-spatial-v4-small-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:14:05.220Z\", \"updated_at\": \"2026-05-15T09:10:21.153Z\", \"hypothesis\": \"Restart from T7. ACR-VLA perdof CRM v3-norm with max_correction_norm=0.1 on spatial. Full per-DOF uncertainty pipeline.\", \"parent\": \"eval-acr-spatial-v4-small\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/crm_best.pt --max_correction_norm 0.1 --start_task 7\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": 312150, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-small-r2.log\", \"submitted_at\": \"2026-05-15T05:14:36.298Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO spatial\", \"data_count\": 30, \"model_name\": \"ACR-VLA CRM perdof v3-norm (restart from T7)\", \"seed\": 42, \"eval_data\": \"LIBERO spatial tasks 7-9\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/crm_best.pt\", \"wall_clock_seconds\": 14053.7, \"gpu_hours\": 3.9}, \"notes\": \"[D027] Framing 暂不裁决。Scenario A/B/C 取决于 magnitude sweep + object benchmark 结果。spatial matched-task perdof=argmin (0pp) 意味着 Scenario A 在 spatial 上不可能。\", \"metrics\": {\"overall_sr\": \"35.0% (35/100)\", \"total_success\": 35, \"total_rollouts\": 100, \"mode\": \"perdof\", \"benchmark\": \"spatial\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"T0\": \"60%\", \"T1\": \"100%\", \"T2\": \"10%\", \"T3\": \"40%\", \"T4\": \"0%\", \"T5\": \"0%\", \"T6\": \"90%\", \"T7\": \"10%\", \"T8\": \"40%\", \"T9\": \"0%\"}, \"note\": \"D029: perdof spatial complete 10-task = 35%. vs argmin 34% = +1pp. Kill criterion triggered — per-DOF claim dead on spatial.\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T09:05:27.552Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T09:05:31.321347+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/crm_best.pt\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-small-r2.log\", \"completed_at\": \"2026-05-15T09:08:50.017Z\"}, \"eval-mag-obsonly-norm-0.3-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:10:44.647Z\", \"updated_at\": \"2026-05-15T07:19:12.632Z\", \"hypothesis\": \"Magnitude sweep: obs_only CRM v3-norm at max_correction_norm=0.3 on spatial. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade at same norm, strong evidence for obs_only robustness over perdof.\", \"parent\": \"eval-mag-obsonly-norm02\", \"spec\": {\"command\": \"N/A (stale duplicate entry)\", \"server\": \"bjb1-18228\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"N/A\", \"seed\": 0, \"checkpoint_source\": \"N/A\", \"eval_data\": \"N/A\"}, \"conclusion\": \"killed\", \"checkpoint_path\": \"N/A (stale duplicate entry, never ran)\", \"log_path\": \"N/A\", \"notes\": \"Stale duplicate entry with dots in name. Actual experiment is eval-mag-obsonly-norm-0p3-r3 (also killed). Real running experiment is eval-mag-obsonly-norm03-r2.\", \"completed_at\": \"2026-05-15T07:19:12.632Z\"}, \"eval-mag-obsonly-norm-0p3-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:11:06.381Z\", \"updated_at\": \"2026-05-15T07:17:16.300Z\", \"hypothesis\": \"Magnitude sweep: obs_only CRM v3-norm at max_correction_norm=0.3 on spatial. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade at same norm, strong evidence for obs_only robustness over perdof.\", \"parent\": \"eval-mag-obsonly-norm02\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_mag_obsonly_norm_0p3.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"329871\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm-0p3-r3.log\", \"submitted_at\": \"2026-05-15T07:11:15.690Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": 100, \"model_name\": \"crm_obs_only_v3_norm\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO spatial (10 tasks x 10 rollouts)\", \"wall_clock_seconds\": 360.6, \"gpu_hours\": 0.1}, \"conclusion\": \"killed\", \"notes\": \"Director 撤销部署指令。r2 (PID 325264) 实际未被误杀，r3 是基于信息差的重复部署。立即 kill r3 保留 r2。\", \"checkpoint_path\": \"N/A (killed before completion)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm-0p3-r3.log\", \"completed_at\": \"2026-05-15T07:17:16.300Z\"}, \"eval-argmin-only-spatial-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:14:03.322Z\", \"updated_at\": \"2026-05-15T06:39:37.926Z\", \"hypothesis\": \"Restart from T9. ReconVLA baseline (scalar Euclidean argmin, K=10) on spatial. Isolate argmin base action selection from CRM correction.\", \"parent\": \"eval-argmin-only-spatial\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --start_task 9\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": 311609, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-only-spatial-r2.log\", \"submitted_at\": \"2026-05-15T05:14:30.112Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO spatial\", \"data_count\": 10, \"model_name\": \"ReconVLA argmin K=10 (restart from T9)\", \"seed\": 42, \"eval_data\": \"LIBERO spatial task 9 only\", \"checkpoint_source\": \"N/A (reconvla mode, no CRM)\", \"wall_clock_seconds\": 5107.8, \"gpu_hours\": 1.42}, \"reproduce\": {\"finished_at\": \"2026-05-15T06:35:00.746Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T06:35:02.954210+00:00\"}]}, \"metrics\": {\"overall_success_rate\": 0.34, \"total_successes\": 34, \"total_trials\": 100, \"per_task\": {\"T0_between_plate_and_ramekin\": 0.6, \"T1_next_to_ramekin\": 1, \"T2_from_table_center\": 0, \"T3_on_cookie_box\": 0.3, \"T4_in_top_drawer\": 0.1, \"T5_on_ramekin\": 0.1, \"T6_next_to_cookie_box\": 0.9, \"T7_on_stove\": 0, \"T8_next_to_plate\": 0.3, \"T9_on_wooden_cabinet\": 0.1}, \"note\": \"T0-T8 from original run (eval-argmin-only-spatial), T9 from r2 restart. Combined 10-task result.\"}, \"conclusion\": \"success\", \"notes\": \"10-task complete. T9 (wooden_cabinet) = 10%. Overall 34% (34/100). T0-T8 from original run, T9 from r2 restart. Clean exit. bjb1-18228 cuda:0 now FREE.\", \"checkpoint_path\": \"N/A (eval-only, no checkpoint output)\", \"completed_at\": \"2026-05-15T06:39:37.926Z\"}, \"eval-mag-obsonly-norm003\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:21:24.009Z\", \"updated_at\": \"2026-05-15T05:32:12.897Z\", \"hypothesis\": \"Magnitude sweep: obs_only CRM v3-norm at norm=0.03 on spatial. Completes obs_only norm curve (have 0.05, 0.2; adding 0.03).\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --max_correction_norm 0.03 --n_rollouts 10 --K 10 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_mag_obsonly_norm003.json\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": 225144, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm003-b2.log\", \"submitted_at\": \"2026-05-15T05:20:45Z\", \"submitted_via\": \"tmux (manual)\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"SmolVLA + CRM-v3-norm-obs_only\", \"seed\": 42, \"checkpoint_source\": \"crm-train-v3-norm-obs_only\", \"eval_data\": \"LIBERO spatial\", \"wall_clock_seconds\": 686.0, \"gpu_hours\": 0.19}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T05:32:10.962Z\", \"notes\": \"Duplicate experiment on same GPU. pid 225144 was actually the child python process of eval-mag-obsonly-norm003-b2's wrapper (pid 225139). Not a separate experiment. Killed, restarted b2 with new pid 227426.\"}, \"eval-vla-only-object-k1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:11:14.165Z\", \"updated_at\": \"2026-05-15T05:18:17.853Z\", \"hypothesis\": \"VLA-only baseline (K=1, single sample, no CRM) on LIBERO object benchmark. Lowest-bar baseline for object domain.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode vla_only --baseline_mode single --benchmark object --n_rollouts 10 --seed 42 --K 1 --output_file logs/eval_object_vla_only_k1.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"39397\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-object-k1.log\", \"submitted_at\": \"2026-05-15T05:11:22.634Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"SmolVLA (VLA-only K=1 single sample)\", \"seed\": 42, \"eval_data\": \"LIBERO object\", \"checkpoint_source\": \"N/A (no CRM, single VLA sample)\", \"wall_clock_seconds\": 311.9, \"gpu_hours\": 0.09}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T05:16:34.574Z\", \"notes\": \"Duplicate of eval-vla-only-object (already DONE at 12% SR). Process killed to free bjb1-32546 cuda:4.\"}, \"eval-acr-spatial-v4-obs-only-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:16:06.636Z\", \"updated_at\": \"2026-05-15T05:05:21.600Z\", \"hypothesis\": \"D020: obs_only CRM v3-norm (val_loss 0.0165) with max_correction_norm=0.1. If obs_only >= v4-small (perdof) → Claim 1 needs restructuring. If obs_only < v4-small → conformal features have unique value under distribution shift.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"270097\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-obs-only-r2.log\", \"submitted_at\": \"2026-05-14T22:21:35.775Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_ids\": [\"cuda:0\"], \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v3-norm obs_only, max_correction_norm=0.1)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 24161.7, \"gpu_hours\": 6.71}, \"metrics\": {\"tasks_done\": \"6/10\", \"partial_results\": {\"between_plate_and_ramekin\": \"90.0% (9/10)\", \"next_to_ramekin\": \"100.0% (10/10)\", \"from_table_center\": \"0.0% (0/10)\", \"on_cookie_box\": \"40.0% (4/10)\", \"in_top_drawer\": \"10.0% (1/10)\", \"on_ramekin\": \"0.0% (0/10)\"}, \"running_avg_6tasks\": \"40.0% (24/60)\", \"snapshot_time\": \"2026-05-15T12:00:00Z\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:0\", \"pid\": 270097}, \"notes\": \"[2026-05-15 corrected] 之前误判为 env hang，实际是被 kill-restart Worker SIGTERM kill。日志无 error/traceback，符合 SIGTERM 特征。6/10 tasks 完成 + task 7 部分（5/10 rollouts），40.0% SR (24/60)。需重跑。\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T05:04:17.448Z\", \"failure_reason\": \"被 kill-restart Worker SIGTERM（Director 撤销 kill 指令前已执行）。完成 6/10 tasks，第 7 个 task (next_to_cookie_box) rollout 5/10 时被 kill。\"}, \"eval-acr-spatial-v4-small\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:09:00.358Z\", \"updated_at\": \"2026-05-15T05:05:19.028Z\", \"hypothesis\": \"D018: Normalization + moderate correction scaling (max_correction_norm=0.1, 14x smaller than default). If v4-small > v4-default → magnitude control needed on top of normalization.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1\", \"server\": \"bjb1-18228\", \"gpu_ids\": [\"cuda:3\"], \"pid\": 253085, \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v3-norm per-DOF, max_correction_norm=0.1)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"log_path\": \"/root/autodl-tmp/logs/eval_acr_spatial_v4_small.log\"}, \"metrics\": {\"tasks_done\": \"7/10\", \"partial_results\": {\"between_plate_and_ramekin\": \"60.0% (6/10)\", \"next_to_ramekin\": \"100.0% (10/10)\", \"from_table_center\": \"10.0% (1/10)\", \"on_cookie_box\": \"40.0% (4/10)\", \"in_top_drawer\": \"0.0% (0/10)\", \"on_ramekin\": \"0.0% (0/10)\", \"next_to_cookie_box\": \"90.0% (9/10)\"}, \"running_avg_7tasks\": \"42.9% (30/70)\", \"snapshot_time\": \"2026-05-15T12:00:00Z\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:3\", \"pid\": 253085}, \"notes\": \"[2026-05-15 corrected] 之前误判为 env init hang，实际是被 kill-restart Worker SIGTERM kill。日志无 error/traceback，符合 SIGTERM 特征。7/10 tasks 完成，42.9% SR (30/70)。需重跑 tasks 8-10（或全部重跑）。\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T05:04:16.712Z\", \"failure_reason\": \"被 kill-restart Worker SIGTERM（Director 撤销 kill 指令前已执行）。完成 7/10 tasks 后在 task 8 启动前被 kill。\"}, \"eval-acr-spatial-v4-scalar\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:15:49.209Z\", \"updated_at\": \"2026-05-15T05:02:30.518Z\", \"hypothesis\": \"D020: scalar_unc CRM (val_loss 0.0374) with max_correction_norm=0.1. Three-way ablation: perdof vs scalar_unc vs obs_only under identical correction magnitude.\", \"spec\": {\"hypothesis\": \"D020 三路消融：scalar_unc CRM v3-norm (val_loss 0.0374) with max_correction_norm=0.1. 与 perdof (cuda:3) 和 obs_only (cuda:0) 同条件对比，判断 per-DOF vs scalar conformal features 的增益\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v3-norm scalar_unc, max_correction_norm=0.1)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"command\": \"python -u src/evaluate.py --mode crm_scalar --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": 288939, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-scalar.log\", \"gpu_ids\": [\"cuda:2\"]}, \"metrics\": {\"tasks_done\": \"3/10\", \"partial_results\": {\"between_plate_and_ramekin\": \"60.0% (6/10)\", \"next_to_ramekin\": \"100.0% (10/10)\", \"from_table_center\": \"10.0% (1/10)\"}, \"running_avg_3tasks\": \"56.7% (17/30)\", \"snapshot_time\": \"2026-05-15T12:00:00Z\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:2\", \"pid\": 288939}, \"notes\": \"[2026-05-15] HUNG: 3/10 tasks done (56.7%, 17/30), stuck on task 4 env init for 8+ hours. Process alive (pid 288939, GPU 1450 MiB) but zero log progress. Needs kill+restart.\", \"reproduce\": {\"finished_at\": \"2026-05-15T04:57:54.647Z\"}, \"failure_reason\": \"Kill-restart Worker 在 Director 撤销 kill 指令前已执行 SIGTERM (EXIT_CODE=143)。D026 kill 指令已被撤销但来不及阻止。\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T04:57:55.887Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T04:57:57.857060+00:00\"}]}}, \"eval-argmin-only-spatial\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:47:58.683Z\", \"updated_at\": \"2026-05-15T05:02:29.518Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark spatial --n_rollouts 10 --seed 42 --K 10\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"231421\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-only-spatial.log\", \"submitted_at\": \"2026-05-14T17:47:58.583Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_ids\": [\"cuda:1\"], \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"SmolVLA K=10 argmin selection (no CRM correction)\", \"seed\": 42, \"hypothesis\": \"Isolate argmin base action selection from CRM correction. If argmin-only ≈ VLA mean (40%), CRM delta is the sole culprit. If argmin-only << VLA mean, argmin selection itself is problematic.\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 40187.5, \"gpu_hours\": 11.16}, \"metrics\": {\"tasks_done\": \"9/10\", \"partial_results\": {\"between_plate_and_ramekin\": \"60.0% (6/10)\", \"next_to_ramekin\": \"100.0% (10/10)\", \"from_table_center\": \"0.0% (0/10)\", \"on_cookie_box\": \"30.0% (3/10)\", \"in_top_drawer\": \"10.0% (1/10)\", \"on_ramekin\": \"10.0% (1/10)\", \"next_to_cookie_box\": \"90.0% (9/10)\", \"on_stove\": \"0.0% (0/10)\", \"next_to_plate\": \"30.0% (3/10)\"}, \"running_avg_9tasks\": \"36.7% (33/90)\", \"snapshot_time\": \"2026-05-15T12:00:00Z\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"pid\": 231421}, \"notes\": \"[2026-05-15] HUNG: 9/10 tasks done (36.7%, 33/90), stuck on task 10 env init for 8+ hours. Process alive (pid 231426, GPU 1414 MiB) but zero log progress. Needs kill+restart.\", \"reproduce\": {\"finished_at\": \"2026-05-15T04:57:45.148Z\"}, \"failure_reason\": \"Kill-restart Worker 在 Director 撤销 kill 指令前已执行 SIGTERM (EXIT_CODE=143)。D026 kill 指令已被撤销但来不及阻止。\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T04:57:46.099Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T04:57:50.175181+00:00\"}]}}, \"eval-vla-only-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T02:54:57.323Z\", \"updated_at\": \"2026-05-15T04:47:47.959Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode single --n_rollouts 10 --K 1 --output_file logs/eval_object_vla_only.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"SmolVLA (VLA-only baseline)\", \"seed\": 42, \"eval_data\": \"LIBERO object\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only.log\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only.json\"}, \"conclusion\": \"success\", \"hypothesis\": \"VLA-only baseline (K=1, no mean, no CRM) on LIBERO object benchmark. Single sample from flow-matching VLA.\", \"metrics\": {\"overall_sr\": 0.12, \"total_success\": 12, \"total_trials\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"gpu\": \"bjb1-32546:cuda:4\", \"pid\": 17222, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only.log\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only.json\", \"completed_at\": \"2026-05-15T04:42:20.025Z\"}, \"eval-acr-spatial-v4-default-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T01:48:09.734Z\", \"updated_at\": \"2026-05-15T03:30:05.911Z\", \"hypothesis\": \"D018-D019 验证: perdof CRM v3-norm with DEFAULT max_correction_norm (~1.42). 如果 v4-default << v4-small (max_norm=0.1) → magnitude control 是必要的。如果 v4-default ≈ baseline → normalization 独自不够。补全 bjb1 上两次失败的实验。\", \"parent\": \"eval-acr-spatial-v4-default-r2\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\\\"\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"212685\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-default-r3.log\", \"submitted_at\": \"2026-05-15T01:49:35.076Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v3-norm perdof, default max_correction_norm)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 6030.8, \"gpu_hours\": 1.68}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T03:30:05.911Z\"}, \"eval-tiny-correction-spatial\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:48:35.421Z\", \"updated_at\": \"2026-05-15T01:45:12.897Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v2/perdof/crm_best.pt --max_correction_norm 0.05\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"232815\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-tiny-correction-spatial.log\", \"submitted_at\": \"2026-05-14T17:48:35.317Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_ids\": [\"cuda:2\"], \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"ACR-VLA per-DOF CRM v2 with tiny correction (max_norm=0.05, 28x smaller than default 1.42)\", \"seed\": 42, \"hypothesis\": \"Extreme correction clipping (0.05 vs 1.42) tests whether compounding error from large CRM deltas is the primary failure mode. If tiny-correction >> full-correction, correction magnitude is the problem.\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v2/perdof/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 27771.0, \"gpu_hours\": 7.71}, \"metrics\": {\"tasks_done\": \"7/10\", \"partial_results\": {\"T1_between_plate_ramekin\": \"70% (7/10)\", \"T2_next_to_ramekin\": \"90% (9/10)\", \"T3_from_table_center\": \"0% (0/10)\", \"T4_on_cookie_box\": \"30% (3/10)\", \"T5_in_top_drawer\": \"0% (0/10)\", \"T6_on_ramekin\": \"0% (0/10)\", \"T7_next_to_cookie_box\": \"90% (9/10)\"}, \"running_avg_7tasks\": \"40% (28/70)\", \"process_status\": \"ACTUALLY ALIVE - bash wrapper PID 232815 dead but python child PID 232820 still running (07:48h, 139% CPU, 9.1GB RSS, GPU2)\", \"status_correction\": \"Registry incorrectly marked DONE, process is still completing remaining 3 tasks\", \"snapshot_time\": \"2026-05-15T09:40Z\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T01:31:26.353Z\", \"failure_reason\": \"D021: v2 checkpoint invalidated by crm_cache_v5 retraining. Replaced by eval-acr-spatial-v4-scalar on bjb1:2.\"}, \"eval-vla-mean-spatial-t10\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:20:02.901Z\", \"updated_at\": \"2026-05-15T01:45:11.590Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --baseline_mode mean --benchmark spatial --n_rollouts 10 --seed 42 --start_task 9 --output_file /root/autodl-tmp/eval_results/eval-vla-mean-spatial-t10.json\", \"server\": \"bjb2-40593\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 10, \"model_name\": \"smolvla_libero\", \"seed\": 42}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T01:32:23.773Z\", \"metrics\": {\"T10_on_wooden_shelf\": \"10% (1/10)\", \"note\": \"Only ran task 9 (start_task=9). T10 = wooden shelf task.\"}, \"log_path\": \"/root/autodl-tmp/eval_results/eval-vla-mean-spatial-t10.json\", \"checkpoint_path\": \"N/A (eval only)\"}, \"eval-vla-mean-spatial\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T03:10:44.114Z\", \"updated_at\": \"2026-05-15T01:35:18.092Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode vla_only --baseline_mode mean --benchmark spatial --n_rollouts 10 --seed 42\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"143106\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"SmolVLA K=10 mean action (no conformal)\", \"seed\": 42, \"hypothesis\": \"K=10 mean baseline isolates multi-sampling averaging contribution vs conformal correction. Expected between vla_only K=1 (30%) and ACR-VLA.\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"log_path\": \"/root/autodl-tmp/eval_results/eval-vla-mean-spatial.log\"}, \"metrics\": {\"overall_success_rate_10tasks\": 0.32, \"total_successes\": 32, \"total_trials\": 100, \"T1\": 0.7, \"T2\": 1, \"T3\": 0, \"T4\": 0.3, \"T5\": 0, \"T6\": 0, \"T7\": 0.8, \"T8\": 0, \"T9\": 0.3, \"T10\": 0.1}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T22:12:39.100Z\", \"log_path\": \"/root/autodl-tmp/eval_results/eval-vla-mean-spatial.log\", \"checkpoint_path\": \"N/A (eval experiment)\"}, \"eval-acr-spatial-v4-default-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:17:37.194Z\", \"updated_at\": \"2026-05-14T22:40:00.000Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\\\"\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"203217\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-default-r2.log\", \"submitted_at\": \"2026-05-14T22:29:03.489Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"D018 retry: Normalization alone fixes CRM correction degradation. v3-norm per-DOF checkpoint with default max_correction_norm (~1.42). If >30% baseline → normalization was the main fix. If still < 30% → magnitude control also needed (compare with v4-small at 0.1).\", \"parent\": \"eval-acr-spatial-v4-default\", \"conclusion\": \"killed\", \"failure_reason\": \"Superseded by D020 plan. Default norm=1.42 already proven to degrade (v4-default: 0/5). Not needed. Process killed on bjb2 (PID 203222 confirmed dead).\", \"completed_at\": \"2026-05-14T22:40:00.000Z\"}, \"eval-acr-spatial-v4-obs-only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:08:53.421Z\", \"updated_at\": \"2026-05-14T22:16:05.788Z\", \"hypothesis\": \"D020: obs_only CRM (val_loss 0.0165, 54% better than perdof 0.0358) with max_correction_norm=0.1. If obs_only >= v4-small (perdof) → Claim 1 needs restructuring. If obs_only < v4-small → conformal features have unique value under distribution shift.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3/obs_only/crm_best.pt\", \"server\": \"bjb2-40593\", \"gpu_ids\": [\"cuda:0\"], \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v3 obs_only, default max_correction_norm=1.42)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"log_path\": \"/root/autodl-tmp/logs/eval-acr-spatial-v4-obs-only.log\", \"tmux_session\": \"eval-acr-spatial-v4-obs-only\", \"pid\": 199257}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T22:16:04.414Z\", \"failure_reason\": \"Wrong checkpoint (crm_v3 not crm_v3_norm) + wrong max_correction_norm (1.42 not 0.1). Killed and replaced by eval-acr-spatial-v4-obs-only-r2.\"}, \"eval-acr-spatial-v4-default\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:08:59.906Z\", \"updated_at\": \"2026-05-14T22:08:58.490Z\", \"hypothesis\": \"D018: Input normalization alone fixes CRM correction degradation. v3-norm checkpoint with default max_correction_norm=1.42. If >30% baseline → normalization was the main fix.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"server\": \"bjb1-18228\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v3-norm per-DOF, default correction)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\"}, \"metrics\": {\"tasks_done\": \"0/10\", \"status_alert\": \"NO PROCESS FOUND - registry says RUNNING but no matching PID or tmux session on bjb1-18228. GPU 0 occupied by stale eval-acr-spatial-v3 tmux + crm-train-obs-only. NEEDS RESTART.\", \"snapshot_time\": \"2026-05-15T05:26Z\"}, \"conclusion\": \"failed\", \"failure_reason\": \"Process died. D019: 0/5 on task 1 confirmed default norm=1.42 still degrades. Replaced by eval-acr-spatial-v4-obs-only on cuda:0.\", \"completed_at\": \"2026-05-14T22:08:58.490Z\"}, \"crm-train-v3-norm-scalar-unc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:09:01.250Z\", \"updated_at\": \"2026-05-14T22:05:42.608Z\", \"hypothesis\": \"Ablation: scalar_unc input mode (scalar uncertainty only) with normalization. Tests per-DOF vs scalar uncertainty contribution with proper normalization.\", \"spec\": {\"command\": \"python -u src/train_crm.py --benchmark spatial --cache_dir /root/autodl-tmp/crm_cache_v5 --output_dir /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/ --K 10 --epochs 50 --batch_size 512 --lr 0.016 --input_mode scalar_unc --seed 42\", \"server\": \"bjb1-18228\", \"data_path\": \"/root/autodl-tmp/crm_cache_v5/spatial/\", \"data_count\": 12167, \"model_name\": \"CRM-MLP-Normalized (scalar_unc)\", \"seed\": 42}, \"metrics\": {\"best_epoch\": 46, \"best_val_loss\": 0.037354, \"final_train_loss\": 0.053422, \"final_val_loss\": 0.03737}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"log_path\": \"/tmp/crm_train_scalar_unc.log\", \"completed_at\": \"2026-05-14T22:05:42.608Z\"}, \"crm-train-v3-norm-obs-only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:09:00.829Z\", \"updated_at\": \"2026-05-14T22:05:28.289Z\", \"hypothesis\": \"Ablation: obs_only input mode (no uncertainty features) with normalization. Isolates contribution of obs features vs conformal features.\", \"spec\": {\"command\": \"python -u src/train_crm.py --benchmark spatial --cache_dir /root/autodl-tmp/crm_cache_v5 --output_dir /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/ --K 10 --epochs 50 --batch_size 512 --lr 0.016 --input_mode obs_only --seed 42\", \"server\": \"bjb1-18228\", \"data_path\": \"/root/autodl-tmp/crm_cache_v5/spatial/\", \"data_count\": 12167, \"model_name\": \"CRM-MLP-Normalized (obs_only)\", \"seed\": 42}, \"metrics\": {\"best_epoch\": 48, \"best_val_loss\": 0.01645, \"final_train_loss\": 0.025576, \"final_val_loss\": 0.01645, \"total_epochs\": 50}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"/tmp/crm_train_obs_only.log\", \"completed_at\": \"2026-05-14T22:05:28.289Z\"}, \"eval-acr-object-v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:17:13.095Z\", \"updated_at\": \"2026-05-14T20:48:42.308Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode acr_vla --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v2/perdof/crm_best.pt\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"197803\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v3.log\", \"submitted_at\": \"2026-05-14T12:17:13.006Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/ (object benchmark)\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v2 per-DOF + SmolVLA K=10)\", \"seed\": 42, \"hypothesis\": \"Per-DOF conformal correction generalizes from spatial to object benchmark — cross-benchmark validation of ACR-VLA.\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v2/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 28901.2, \"gpu_hours\": 8.03}, \"metrics\": {\"tasks_done\": \"4/10\", \"overall_success_rate\": 0, \"total_successes\": 0, \"total_rollouts\": 40, \"per_task_partial\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0, \"bbq_sauce\": 0}, \"snapshot_time\": \"2026-05-14T18:15Z\"}, \"conclusion\": \"failed\", \"reproduce\": {\"finished_at\": \"2026-05-14T20:18:53.408Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-14T20:18:54.185Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T20:18:55.466058+00:00\"}]}}, \"eval-acr-spatial-v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:17:06.073Z\", \"updated_at\": \"2026-05-14T20:48:41.643Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v2/perdof/crm_best.pt\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"197057\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v3.log\", \"submitted_at\": \"2026-05-14T12:17:05.974Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial benchmark)\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v2 per-DOF + SmolVLA K=10)\", \"seed\": 42, \"hypothesis\": \"Per-DOF conformal correction (ACR-VLA with D016 4-bug fix) outperforms VLA K=1 (30%) and SampleConsensus (34%) on LIBERO spatial. CORE CLAIM experiment.\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v2/perdof/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 28899.4, \"gpu_hours\": 8.03}, \"metrics\": {\"tasks_done\": \"4/10\", \"overall_success_rate\": 0.025, \"total_successes\": 1, \"total_rollouts\": 40, \"per_task_partial\": {\"pick_up_black_bowl_between_plate_and_ramekin\": 0.1, \"pick_up_black_bowl_next_to_ramekin\": 0, \"pick_up_black_bowl_from_table_center\": 0, \"pick_up_black_bowl_on_cookie_box\": 0}, \"snapshot_time\": \"2026-05-14T18:15Z\"}, \"conclusion\": \"failed\", \"reproduce\": {\"finished_at\": \"2026-05-14T20:18:44.725Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-14T20:18:45.380Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T20:18:46.631294+00:00\"}]}}, \"crm-train-v3-norm\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:45:12.565Z\", \"updated_at\": \"2026-05-14T20:05:22.677Z\", \"hypothesis\": \"D018: Input normalization fixes 1500x scale imbalance in CRM inputs, enabling proper gradient flow and meaningful per-DOF correction learning\", \"parent\": \"crm-train-v3-perdof\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/train_crm.py --benchmark spatial --cache_dir /root/autodl-tmp/crm_cache_v5 --output_dir /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/ --K 10 --epochs 50 --batch_size 512 --lr 0.016 --input_mode full --seed 42\", \"server\": \"bjb1-18228\", \"data_path\": \"/root/autodl-tmp/crm_cache_v5/spatial/\", \"data_count\": 12167, \"model_name\": \"CRM-MLP-337K-Normalized\", \"seed\": 42, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"N/A (training experiment)\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"log_path\": \"no log file (tee failed, output was in tmux pane only)\", \"completed_at\": \"2026-05-14T20:05:20.181Z\", \"results\": {\"best_epoch\": 47, \"best_val_loss\": 0.03578, \"final_train_loss\": 0.04992, \"final_val_loss\": 0.03578, \"total_epochs\": 50, \"normalization\": \"per-feature input normalization (mean/std stored in crm_best.pt as input_mean/input_std tensors)\"}}, \"crm-train-v3-scalar-unc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:05:00.968Z\", \"updated_at\": \"2026-05-14T18:37:14.400Z\", \"spec\": {\"command\": \"python -u src/train_crm.py --benchmark spatial --cache_dir /root/autodl-tmp/crm_cache/ --output_dir /root/autodl-tmp/checkpoints/crm_v3/scalar_unc/ --K 10 --epochs 50 --batch_size 512 --lr 0.016 --input_mode scalar_unc --seed 42 --norm_stats /root/autodl-tmp/checkpoints/crm_v3/norm_stats.pt\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"181896\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-train-v3-scalar-unc.log\", \"submitted_at\": \"2026-05-14T18:05:00.862Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/crm_cache/\", \"data_count\": 0, \"model_name\": \"CRM-MLP-337K\", \"seed\": 42, \"wall_clock_seconds\": 1917.7, \"gpu_hours\": 0.53}, \"reproduce\": {\"finished_at\": \"2026-05-14T18:27:15.107Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T18:27:19.071535+00:00\"}]}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T18:36:58.566Z\", \"metrics\": {\"invalidation_reason\": \"Trained on bjb2 crm_cache v4 (6D state, pre-D016). Must retrain on bjb1 crm_cache_v5 (8D state).\", \"original_val_loss\": 1.195}}, \"crm-train-v3-obs-only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:05:02.939Z\", \"updated_at\": \"2026-05-14T18:37:04.316Z\", \"spec\": {\"command\": \"python -u src/train_crm.py --benchmark spatial --cache_dir /root/autodl-tmp/crm_cache/ --output_dir /root/autodl-tmp/checkpoints/crm_v3/obs_only/ --K 10 --epochs 50 --batch_size 512 --lr 0.016 --input_mode obs_only --seed 42 --norm_stats /root/autodl-tmp/checkpoints/crm_v3/norm_stats.pt\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"181973\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-train-v3-obs-only.log\", \"submitted_at\": \"2026-05-14T18:05:02.833Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/crm_cache/spatial\", \"data_count\": 2402, \"model_name\": \"CRM-MLP-337K\", \"seed\": 42, \"wall_clock_seconds\": 1802.8, \"gpu_hours\": 0.5}, \"reproduce\": {\"finished_at\": \"2026-05-14T18:27:22.983Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T18:27:25.410071+00:00\"}]}, \"conclusion\": \"killed\", \"metrics\": {\"invalidation_reason\": \"Trained on bjb2 crm_cache v4 (6D state, pre-D016). Must retrain on bjb1 crm_cache_v5 (8D state).\", \"original_val_loss\": 1.193424}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3/obs_only/crm_best.pt\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-train-v3-obs-only.log\", \"completed_at\": \"2026-05-14T18:35:05.626Z\"}, \"crm-train-v3-perdof\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:04:54.552Z\", \"updated_at\": \"2026-05-14T18:37:02.631Z\", \"spec\": {\"command\": \"python -u src/train_crm.py --benchmark spatial --cache_dir /root/autodl-tmp/crm_cache/ --output_dir /root/autodl-tmp/checkpoints/crm_v3/perdof/ --K 10 --epochs 50 --batch_size 512 --lr 0.016 --input_mode full --seed 42 --norm_stats /root/autodl-tmp/checkpoints/crm_v3/norm_stats.pt\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"181668\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-train-v3-perdof.log\", \"submitted_at\": \"2026-05-14T18:04:54.446Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/crm_cache/\", \"data_count\": 0, \"model_name\": \"CRM-MLP-337K\", \"seed\": 42, \"wall_clock_seconds\": 1510.3, \"gpu_hours\": 0.42}, \"reproduce\": {\"finished_at\": \"2026-05-14T18:27:11.506Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T18:27:13.038696+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3/perdof/crm_best.pt\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-train-v3-perdof.log\", \"metrics\": {\"invalidation_reason\": \"Trained on bjb2 crm_cache v4 (6D state, pre-D016). Must retrain on bjb1 crm_cache_v5 (8D state).\", \"original_val_loss\": 1.191387}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T18:30:04.713Z\"}, \"eval-obs-only-spatial-v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:49:43.787Z\", \"updated_at\": \"2026-05-14T17:47:54.523Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v2/obs_only/crm_best.pt\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"211961\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-spatial-v3.log\", \"submitted_at\": \"2026-05-14T12:49:43.691Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"CRM obs_only v2 (990D, no conformal features)\", \"seed\": 42, \"hypothesis\": \"obs_only CRM ablation — CRM without conformal features tests whether per-DOF conformal intervals are necessary\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v2/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"parent\": \"crm-train-v2-obs-only\", \"conclusion_note\": \"Director order: 0/30 after 3 tasks, no diagnostic value. Freed bjb1:2 for eval-tiny-correction-spatial.\", \"metrics\": {\"tasks_completed\": 3, \"total_tasks\": 10, \"success_rate\": 0, \"successes\": 0, \"rollouts\": 30}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v2/obs_only/crm_best.pt\", \"wall_clock_seconds\": 17890.8, \"gpu_hours\": 4.97}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T17:47:54.523Z\"}, \"eval-scalar-unc-spatial-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:17:08.413Z\", \"updated_at\": \"2026-05-14T17:47:53.188Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode crm_scalar --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v2/scalar_unc/crm_best.pt\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"197324\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-scalar-unc-spatial-v2.log\", \"submitted_at\": \"2026-05-14T12:17:08.325Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial benchmark)\", \"data_count\": 100, \"model_name\": \"CRM v2 scalar-uncertainty + SmolVLA K=10\", \"seed\": 42, \"hypothesis\": \"Scalar uncertainty CRM ablation — tests whether per-DOF conformal is superior to scalar aggregated uncertainty for action correction.\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v2/scalar_unc/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"conclusion_note\": \"Director order: 0/30 after 3 tasks, no diagnostic value. Freed bjb1:1 for eval-argmin-only-spatial.\", \"metrics\": {\"tasks_completed\": 3, \"total_tasks\": 10, \"success_rate\": 0, \"successes\": 0, \"rollouts\": 30}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v2/scalar_unc/crm_best.pt\", \"wall_clock_seconds\": 19844.9, \"gpu_hours\": 5.51}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T17:47:53.188Z\"}, \"eval-obs-only-spatial-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:43:42.283Z\", \"updated_at\": \"2026-05-14T12:46:47.663Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v2/obs_only/crm_best.pt\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"203968\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-spatial-v2.log\", \"submitted_at\": \"2026-05-14T12:43:42.188Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"CRM obs_only v2 (990D, no conformal features)\", \"seed\": 42, \"hypothesis\": \"obs_only CRM ablation — CRM without conformal features tests whether per-DOF conformal intervals are necessary for effective correction\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v2/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"parent\": \"crm-train-v2-obs-only\", \"failure_reason\": \"Bug: evaluate.py line 266 CRM load condition missing crm_obs_only, CRM was None throughout eval, all rollouts 0%. Replaced by eval-obs-only-spatial-v3.\", \"wall_clock_seconds\": 185.5, \"gpu_hours\": 0.05}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T12:46:47.663Z\"}, \"eval-obs-only-spatial\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:17:10.843Z\", \"updated_at\": \"2026-05-14T12:40:23.205Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v2/obs_only/crm_best.pt\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"197596\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-spatial.log\", \"submitted_at\": \"2026-05-14T12:17:10.754Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"CRM obs_only v2 (990D input, no conformal features)\", \"seed\": 42, \"hypothesis\": \"obs_only CRM ablation — CRM without conformal features\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v2/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"failure_reason\": \"evaluate.py has no crm_obs_only mode. --mode acr_vla loads CRM expecting 1030D input but obs_only checkpoint has 990D (no conformal features). Replaced by eval-obs-only-spatial-v2.\", \"wall_clock_seconds\": 1392.5, \"gpu_hours\": 0.39}, \"conclusion\": \"failed\", \"metrics\": {\"error\": \"size mismatch: obs_only CRM net.0.weight [256,990] vs acr_vla expects [256,1030] — no crm_obs_only mode in evaluate.py\"}, \"completed_at\": \"2026-05-14T12:40:23.205Z\"}, \"crm-train-v2-obs-only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T09:41:35.819Z\", \"updated_at\": \"2026-05-14T12:17:42.122Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 python -u src/train_crm.py --benchmark spatial object --cache_dir /root/autodl-tmp/crm_cache_v5/ --output_dir /root/autodl-tmp/checkpoints/crm_v2/obs_only/ --K 10 --epochs 50 --batch_size 512 --lr 0.016 --input_mode obs_only --seed 42\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"187913\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-train-v2-obs-only.log\", \"submitted_at\": \"2026-05-14T09:41:35.736Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/crm_cache_v5/\", \"data_count\": 26737, \"model_name\": \"CRM obs_only v2\", \"seed\": 42, \"wall_clock_seconds\": 9366.4, \"gpu_hours\": 2.6}, \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.050501, \"best_epoch\": 50, \"total_epochs\": 50, \"final_train_loss\": 0.074839, \"comparison_vs_old\": \"old_6D_buggy=0.018312, new=0.050501 (loss metric changed with v2 fix)\"}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v2/obs_only/crm_best.pt\", \"log_path\": \"/root/runs/acr-vla-conformal-refinement/crm-train-v2-obs-only.log\", \"completed_at\": \"2026-05-14T12:17:42.122Z\"}, \"crm-train-v2-scalar-unc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T09:30:43.696Z\", \"updated_at\": \"2026-05-14T12:17:01.093Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=1 python -u src/train_crm.py --benchmark spatial object --cache_dir /root/autodl-tmp/crm_cache_v5/ --output_dir /root/autodl-tmp/checkpoints/crm_v2/scalar_unc/ --K 10 --epochs 50 --batch_size 512 --lr 0.016 --input_mode scalar_unc --seed 42\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"186964\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-train-v2-scalar-unc.log\", \"submitted_at\": \"2026-05-14T09:30:43.616Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/crm_cache_v5/\", \"data_count\": 26737, \"model_name\": \"CRM scalar-unc v2 (327K params, 8D state fix)\", \"seed\": 42, \"hypothesis\": \"Scalar CRM v2 ablation — per-DOF expected to outperform on task success rate despite similar val_loss\", \"wall_clock_seconds\": 9977.5, \"gpu_hours\": 2.77}, \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.047202, \"best_epoch\": 48, \"total_epochs\": 50, \"final_train_loss\": 0.069679, \"comparison_vs_old\": \"old_6D_buggy=0.008379, new=0.047202 (loss metric changed with v2 fix)\"}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v2/scalar_unc/crm_best.pt\", \"log_path\": \"/root/runs/acr-vla-conformal-refinement/crm-train-v2-scalar-unc.log\", \"completed_at\": \"2026-05-14T12:17:01.093Z\"}, \"crm-train-v2-perdof\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T09:30:40.796Z\", \"updated_at\": \"2026-05-14T12:17:00.195Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 python -u src/train_crm.py --benchmark spatial object --cache_dir /root/autodl-tmp/crm_cache_v5/ --output_dir /root/autodl-tmp/checkpoints/crm_v2/perdof/ --K 10 --epochs 50 --batch_size 512 --lr 0.016 --input_mode full --seed 42\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"186823\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-train-v2-perdof.log\", \"submitted_at\": \"2026-05-14T09:30:40.716Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/crm_cache_v5/\", \"data_count\": 26737, \"model_name\": \"CRM per-DOF v2 (337K params, 8D state fix, argmin base, L2 clip)\", \"seed\": 42, \"hypothesis\": \"Per-DOF CRM v2 with D016 fixes (8D state, argmin base, alpha=0.5, L2 clipping) improves over pre-fix version\", \"wall_clock_seconds\": 9979.5, \"gpu_hours\": 2.77}, \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.051684, \"best_epoch\": 48, \"total_epochs\": 50, \"final_train_loss\": 0.076748, \"comparison_vs_old\": \"old_6D_buggy=0.009046, new=0.051684 (loss metric changed with v2 fix)\"}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v2/perdof/crm_best.pt\", \"log_path\": \"/root/runs/acr-vla-conformal-refinement/crm-train-v2-perdof.log\", \"completed_at\": \"2026-05-14T12:17:00.195Z\"}, \"eval-reconvla-spatial-v3\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-13T23:04:34.297Z\", \"updated_at\": \"2026-05-14T11:10:55.009Z\", \"reproduce\": {\"finished_at\": \"2026-05-14T11:07:49.901Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-13T23:34:14.141Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:34:15.524386+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T11:07:51.915540+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode reconvla --benchmark spatial --n_rollouts 10 --seed 42 --K 10\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"118108\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"SampleConsensus (scalar Euclidean argmin)\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/eval_results/eval-reconvla-spatial-v3.log\", \"hypothesis\": \"SampleConsensus scalar baseline for ACR-VLA comparison\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\"}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.34, \"total_successes\": 34, \"total_rollouts\": 100, \"per_task\": {\"pick_up_black_bowl_between_plate_and_ramekin\": 0.6, \"pick_up_black_bowl_next_to_ramekin\": 1, \"pick_up_black_bowl_from_table_center\": 0, \"pick_up_black_bowl_on_cookie_box\": 0.3, \"pick_up_black_bowl_in_top_drawer\": 0.1, \"pick_up_black_bowl_on_ramekin\": 0.1, \"pick_up_black_bowl_next_to_cookie_box\": 0.9, \"pick_up_black_bowl_on_stove\": 0, \"pick_up_black_bowl_next_to_plate\": 0.4, \"pick_up_black_bowl_on_wooden_cabinet\": 0}}, \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"/root/autodl-tmp/eval_results/eval-reconvla-spatial-v3.log\"}, \"precompute-v5-shard2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:55:02.277Z\", \"updated_at\": \"2026-05-14T09:28:09.308Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 python -u src/train_crm.py --precompute --benchmark spatial object --cache_dir /root/autodl-tmp/crm_cache_v5/ --K 10 --shard_id 2 --num_shards 3 --max_demos_per_task 10 --precompute_batch_size 4 --save_every 500\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"180480\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v5-shard2.log\", \"submitted_at\": \"2026-05-14T07:56:37.531Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial + object)\", \"data_count\": \"~8900 samples (shard 2 of 3)\", \"model_name\": \"SmolVLA 450M (precompute K=10 features)\", \"seed\": 42, \"hypothesis\": \"Phase 2 precompute with 8D state fix (C1) for per-DOF CRM retraining\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache_v5/\", \"wall_clock_seconds\": 5491.8, \"gpu_hours\": 1.53}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T09:28:09.308Z\"}, \"precompute-v5-shard1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:55:00.276Z\", \"updated_at\": \"2026-05-14T09:28:07.934Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=1 python -u src/train_crm.py --precompute --benchmark spatial object --cache_dir /root/autodl-tmp/crm_cache_v5/ --K 10 --shard_id 1 --num_shards 3 --max_demos_per_task 10 --precompute_batch_size 4 --save_every 500\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"180400\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v5-shard1.log\", \"submitted_at\": \"2026-05-14T07:56:35.789Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial + object)\", \"data_count\": \"~8900 samples (shard 1 of 3)\", \"model_name\": \"SmolVLA 450M (precompute K=10 features)\", \"seed\": 42, \"hypothesis\": \"Phase 2 precompute with 8D state fix (C1) for per-DOF CRM retraining\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache_v5/\", \"wall_clock_seconds\": 5492.1, \"gpu_hours\": 1.53}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T09:28:07.934Z\"}, \"precompute-v5-shard0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:54:59.383Z\", \"updated_at\": \"2026-05-14T09:28:06.626Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 python -u src/train_crm.py --precompute --benchmark spatial object --cache_dir /root/autodl-tmp/crm_cache_v5/ --K 10 --shard_id 0 --num_shards 3 --max_demos_per_task 10 --precompute_batch_size 4 --save_every 500\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"180251\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v5-shard0.log\", \"submitted_at\": \"2026-05-14T07:56:33.414Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial + object)\", \"data_count\": \"~8900 samples (shard 0 of 3)\", \"model_name\": \"SmolVLA 450M (precompute K=10 features)\", \"seed\": 42, \"hypothesis\": \"Phase 2 precompute with 8D state fix (C1) for per-DOF CRM retraining\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache_v5/\", \"wall_clock_seconds\": 5493.2, \"gpu_hours\": 1.53}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T09:28:06.626Z\"}, \"crm-train-a4-scalar-unc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:48:40.837Z\", \"updated_at\": \"2026-05-14T07:59:32.676Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/train_crm.py --benchmark spatial object --epochs 50 --batch_size 32 --lr 0.001 --K 10 --seed 42 --input_mode scalar_unc --output_dir /root/autodl-tmp/checkpoints/crm/scalar_unc/\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"121984\", \"data_path\": \"/root/autodl-tmp/crm_cache/\", \"data_count\": 26737, \"model_name\": \"CRM-scalar_unc (3D scalar uncertainty)\", \"seed\": 42, \"hypothesis\": \"CRM with scalar Euclidean uncertainty (3D) performs worse than per-DOF (40D), validating per-DOF advantage. Ablation A4, hyperparams matched to plan_001 (bs=32/lr=1e-3).\", \"log_path\": \"/root/autodl-tmp/checkpoints/crm/scalar_unc/train.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm/scalar_unc/crm_best.pt\", \"conclusion_note\": \"Training converged. scalar val_loss 0.008379 < per-DOF 0.009046 — original hypothesis (scalar worse) NOT confirmed on val_loss. Hypothesis pending eval-scalar-unc-spatial task success rate validation.\"}, \"conclusion\": \"killed\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm/scalar_unc/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/checkpoints/crm/scalar_unc/train.log\", \"metrics\": {\"best_val_loss\": 0.008379, \"best_epoch\": 48, \"total_epochs\": 50, \"final_val_loss\": 0.008384, \"final_train_loss\": 0.012959}, \"completed_at\": \"2026-05-14T02:21:00.891Z\", \"conclusion_note\": \"invalidated by D016 C1 fix, 6D state mismatch — checkpoint trained on wrong features\"}, \"crm-train-a3-obs-only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:56:28.643Z\", \"updated_at\": \"2026-05-14T07:59:31.277Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/train_crm.py --benchmark spatial object --epochs 50 --batch_size 512 --lr 0.016 --K 10 --seed 42 --input_mode obs_only --output_dir /root/autodl-tmp/checkpoints/crm/obs_only/\", \"server\": \"bjb1-18228\", \"data_path\": \"/root/autodl-tmp/crm_cache/\", \"data_count\": 26737, \"model_name\": \"CRM-obs_only\", \"seed\": 42, \"hypothesis\": \"CRM without conformal features (obs_only, 990D input) performs significantly worse than full CRM (1030D), validating that per-DOF conformal features are necessary for effective correction\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm/obs_only/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/checkpoints/crm/obs_only/train.log\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T23:43:51.534Z\", \"metrics\": {\"best_val_loss\": 0.018312, \"best_epoch\": 4, \"early_stopped_at_epoch\": \"~15-20\", \"early_stop_reason\": \"val_loss plateau at 0.018 for 10+ epochs (full CRM: 0.009, 2x gap confirms conformal features are critical)\", \"input_dim\": 990, \"params\": 327966}, \"conclusion_note\": \"invalidated by D016 C1 fix, 6D state mismatch — checkpoint trained on wrong features\"}, \"crm-train-v1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:10:36.535Z\", \"updated_at\": \"2026-05-14T07:59:30.290Z\", \"spec\": {\"command\": \"python -u src/train_crm.py --benchmark spatial object --epochs 50 --batch_size 32 --lr 1e-3 --K 10 --seed 42\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"78520\", \"log_path\": \"/root/runs/acr-vla-conformal-refinement/crm-train-v1.log\", \"data_path\": \"/root/autodl-tmp/crm_cache/ (spatial: 12167 + object: 14570 = 26737 samples)\", \"data_count\": 26737, \"model_name\": \"CRM MLP (337K params, 1030D→256→256→30D)\", \"seed\": 42, \"hypothesis\": \"CRM with per-DOF conformal features (1030D input) learns dimension-selective correction, achieving lower action MSE than scalar/no-uncertainty ablations\", \"checkpoint_source\": \"precompute-v4 (spatial+object)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm/\"}, \"reproduce\": {\"finished_at\": \"2026-05-13T22:40:27.930Z\"}, \"failure_reason\": \"RESOLVED: EXIT_CODE=129 was SIGHUP after training completed (50/50 epochs). Not a real failure.\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T22:40:28.559Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T22:40:29.429643+00:00\"}]}, \"metrics\": {\"best_val_loss\": 0.009046, \"best_epoch\": 50, \"total_epochs\": 50, \"checkpoint\": \"crm_best.pt\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm/crm_best.pt\", \"exit_code_note\": \"129 was false alarm - SIGHUP after training completed\"}, \"conclusion_note\": \"invalidated by D016 C1 fix, 6D state mismatch — checkpoint trained on wrong features\"}, \"crm-train-k5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T01:42:55.911Z\", \"updated_at\": \"2026-05-14T07:59:29.396Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/train_crm.py --benchmark spatial object --epochs 50 --batch_size 32 --lr 0.001 --K 5 --seed 42 --cache_dir /root/autodl-tmp/crm_cache_k5/ --output_dir /root/autodl-tmp/checkpoints/crm/k5/\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"139839\", \"data_path\": \"/root/autodl-tmp/crm_cache_k5/\", \"data_count\": 26737, \"model_name\": \"CRM (K=5, 337K params)\", \"seed\": 42, \"hypothesis\": \"CRM with K=5 conformal samples for K sensitivity ablation (K=10 baseline val_loss=0.009046)\", \"log_path\": \"/root/autodl-tmp/checkpoints/crm/k5/train.log\", \"checkpoint_source\": \"from_scratch\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm/k5/crm_best.pt\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T04:12:42.247Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T04:12:44.286094+00:00\"}]}, \"conclusion\": \"killed\", \"metrics\": {\"best_val_loss\": 0.008996, \"best_epoch\": 50, \"total_epochs\": 50, \"comparison\": \"K=5 val_loss 0.008996 ≈ K=10 val_loss 0.009046, near identical\"}, \"completed_at\": \"2026-05-14T07:21:32.072Z\", \"conclusion_note\": \"invalidated by D016 C1 fix, 6D state mismatch — checkpoint trained on wrong features\"}, \"eval-scalar-unc-spatial\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:54:30.549Z\", \"updated_at\": \"2026-05-14T07:52:44.766Z\", \"spec\": {\"hypothesis\": \"Scalar CRM (3D unc) vs per-DOF CRM (40D unc) on spatial task success rate. Val_loss favored scalar (0.008 vs 0.009) but per-DOF expected to win on task success via dimension-selective correction.\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"CRM-scalar_unc (3D scalar uncertainty, 327K params)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm/scalar_unc/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode crm_scalar --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm/scalar_unc/crm_best.pt\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"143206\", \"log_path\": \"/root/autodl-tmp/eval_results/eval-scalar-unc-spatial.log\", \"failure_reason\": \"D016: C1 (state 6D→8D mismatch). Scalar CRM trained on wrong features. Replaced by eval-scalar-unc-spatial-v2.\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T07:52:15.933Z\", \"conclusion_note\": \"invalidated by D016 C1 bug, pre-fix data collected\"}, \"eval-acr-spatial-v2\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-13T23:04:32.138Z\", \"updated_at\": \"2026-05-14T07:52:43.327Z\", \"reproduce\": {\"finished_at\": \"2026-05-13T23:31:30.005Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-13T23:31:31.129Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:31:32.734610+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm/crm_best.pt\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"117814\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"ACR-VLA (SmolVLA + CRM per-DOF)\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/eval_results/eval-acr-spatial-v2.log\", \"hypothesis\": \"ACR-VLA per-DOF correction improves over SmolVLA baseline on spatial\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"failure_reason\": \"D016: C1 (state 6D→8D mismatch) + W3 (alpha 0.1→0.5). CRM trained on wrong features + CGS quantile wrong. Replaced by eval-acr-spatial-v3.\"}, \"conclusion\": \"killed\", \"conclusion_note\": \"invalidated by D016 C1 bug, pre-fix data collected\"}, \"eval-k5-spatial\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T04:14:23.092Z\", \"updated_at\": \"2026-05-14T07:52:43.134Z\", \"spec\": {\"command\": \"MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 5 --crm_checkpoint /root/autodl-tmp/checkpoints/crm/k5/crm_best.pt\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"154189\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"ACR-VLA K=5 (CRM 337K + SmolVLA 450M)\", \"seed\": 42, \"hypothesis\": \"K=5 vs K=10 ACR-VLA on task success rate.\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm/k5/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"log_path\": \"/root/autodl-tmp/eval_results/eval-k5-spatial.log\", \"failure_reason\": \"D016: C1 (state 6D→8D mismatch) + W3 (alpha 0.1→0.5). CRM K=5 trained on wrong features. Replaced by eval-k5-spatial-v2.\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T07:52:14.685Z\", \"conclusion_note\": \"invalidated by D016 C1 bug, pre-fix data collected\"}, \"eval-object-v8-full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T00:05:25.647Z\", \"updated_at\": \"2026-05-14T03:10:30.457Z\", \"spec\": {\"hypothesis\": \"SmolVLA baseline on libero_object with K=1 fix (vla_only single inference)\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\", \"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 42\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"125830\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_object/\", \"data_count\": 100, \"model_name\": \"smolvla_libero\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/eval_results/eval-object-v6.log\"}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13, \"total_successes\": 13, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}, \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-14T03:10:30.457Z\"}, \"eval-spatial-v7-full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T00:05:16.510Z\", \"updated_at\": \"2026-05-14T01:45:58.391Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 10 --seed 42\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"123761\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"lerobot/smolvla_libero\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/eval_results/eval-spatial-v7.log\", \"hypothesis\": \"SmolVLA baseline on libero_spatial with K=1 fix (vla_only single inference)\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\"}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.3, \"total_successes\": 30, \"total_episodes\": 100, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"pick_up_black_bowl_between_plate_and_ramekin\": 0.6, \"pick_up_black_bowl_next_to_ramekin\": 1, \"pick_up_black_bowl_from_table_center\": 0, \"pick_up_black_bowl_on_cookie_box\": 0.2, \"pick_up_black_bowl_in_top_drawer\": 0, \"pick_up_black_bowl_on_ramekin\": 0, \"pick_up_black_bowl_next_to_cookie_box\": 0.9, \"pick_up_black_bowl_on_stove\": 0, \"pick_up_black_bowl_next_to_plate\": 0.3, \"pick_up_black_bowl_on_wooden_cabinet\": 0}}, \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-14T01:45:58.391Z\"}, \"eval-object-v7-full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T00:03:35.642Z\", \"updated_at\": \"2026-05-14T01:45:48.892Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 42\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"125830\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_object/\", \"data_count\": 100, \"model_name\": \"smolvla_libero\", \"seed\": 42, \"hypothesis\": \"SmolVLA baseline on libero_object with K=1 fix (single inference per step)\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\", \"log_path\": \"/root/autodl-tmp/eval_results/eval-object-v6.log\", \"failure_reason\": \"Duplicate entry — same PID 125830 tracked by eval-object-v8-full. Cleaning up.\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T01:45:48.892Z\"}, \"eval-spatial-v6-full\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-13T23:04:28.766Z\", \"updated_at\": \"2026-05-14T00:05:22.619Z\", \"reproduce\": {\"finished_at\": \"2026-05-14T00:03:28.470Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-13T23:34:09.898Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:34:11.481851+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T00:03:30.351859+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 10 --seed 42\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"117486\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"lerobot/smolvla_libero\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/eval_results/eval-spatial-v6-full.log\", \"hypothesis\": \"SmolVLA baseline on libero_spatial with fixed evaluate.py (reset→set_init_state→zero-action)\", \"failure_reason\": \"vla_only mode running K=10 instead of K=1, wasting GPU. Killed and restarted with K=1 fix.\"}, \"conclusion\": \"killed\"}, \"eval-object-v5-full\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-13T23:17:35.776Z\", \"updated_at\": \"2026-05-14T00:04:26.792Z\", \"reproduce\": {\"finished_at\": \"2026-05-13T23:43:52.899Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-13T23:43:53.809Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:43:56.187212+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 42 --smolvla_path /root/autodl-tmp/models/smolvla_libero/\", \"server\": \"bjb2-40593\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_object/\", \"data_count\": 100, \"model_name\": \"smolvla_libero\", \"seed\": 42, \"pid\": 117697, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-object-v5-full.log\", \"gpu\": \"cuda:0\", \"note\": \"restored from false DONE/failed — cron misdetected tmux pipe buffering as process exit\", \"failure_reason\": \"vla_only mode running K=10 multi-sampling (should be K=1). Killed by Director order, replaced by eval-object-v7-full with K=1 fix.\"}, \"conclusion\": \"killed\"}, \"eval-acr-vla-spatial-v1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:56:40.287Z\", \"updated_at\": \"2026-05-13T23:14:22.561Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm/crm_best.pt --output_file /root/autodl-tmp/eval_results/acr_vla_spatial_v1.json\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO spatial benchmark (10 tasks)\", \"data_count\": 100, \"model_name\": \"ACR-VLA (SmolVLA + CRM perdof)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm/crm_best.pt\", \"eval_data\": \"LIBERO spatial, 10 tasks x 10 rollouts\", \"parent\": \"train-crm-v1\", \"failure_reason\": \"P0 bug: evaluate.py env.reset() 覆盖 set_init_state 的 demo 初始状态，结果不可信。已被 eval-acr-spatial-v2 替代\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T23:13:00.422Z\"}, \"eval-acr-spatial-v1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:54:28.535Z\", \"updated_at\": \"2026-05-13T23:12:11.315Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm/crm_best.pt --output_file /root/autodl-tmp/eval_results/eval-acr-spatial-v1.json\", \"server\": \"bjb1-18228\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"ACR-VLA (SmolVLA + CRM)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm/crm_best.pt\", \"eval_data\": \"LIBERO spatial (10 tasks x 10 rollouts)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/eval_results/eval-acr-spatial-v1.log\", \"failure_reason\": \"P0 bug: evaluate.py env.reset() 覆盖 set_init_state 的 demo 初始状态，结果不可信\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T23:09:38.077Z\"}, \"eval-reconvla-spatial-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:29:41.730Z\", \"updated_at\": \"2026-05-13T23:12:10.958Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark spatial --n_rollouts 10 --seed 42 --K 10\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"87787\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-reconvla-spatial-v1.log\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"smolvla_libero + ReconVLA argmin\", \"seed\": 42, \"hypothesis\": \"ReconVLA (scalar Euclidean nonconformity + argmin) as baseline for ACR-VLA comparison\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"libero_spatial 10 tasks\", \"failure_reason\": \"P0 bug: evaluate.py env.reset() 覆盖 set_init_state 的 demo 初始状态，结果不可信\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T23:09:40.252Z\"}, \"eval-object-v4-full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T19:13:26.341Z\", \"updated_at\": \"2026-05-13T23:12:10.037Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 42\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"103768\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-object-v4-full.log\", \"data_path\": \"/root/autodl-tmp/libero_data/ (object)\", \"data_count\": 100, \"model_name\": \"lerobot/smolvla_libero\", \"seed\": 42, \"hypothesis\": \"SmolVLA with verified-deployed wrapper achieves meaningful success rate on libero_object\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"libero_object 10 tasks\", \"failure_reason\": \"P0 bug: evaluate.py env.reset() 覆盖 set_init_state 的 demo 初始状态，结果不可信\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T23:09:39.017Z\"}, \"eval-spatial-v5-full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T19:16:58.052Z\", \"updated_at\": \"2026-05-13T23:12:09.066Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 10 --seed 42\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"73756\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-spatial-v5-full.log\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"lerobot/smolvla_libero\", \"seed\": 42, \"hypothesis\": \"SmolVLA with verified wrapper + dual camera (agentview + eye_in_hand) achieves >50% on libero_spatial\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"libero_spatial 10 tasks\", \"failure_reason\": \"P0 bug: evaluate.py env.reset() 覆盖 set_init_state 的 demo 初始状态，结果不可信\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T23:09:39.445Z\"}, \"precompute-k5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:15:37.603Z\", \"updated_at\": \"2026-05-13T22:12:39.543Z\", \"spec\": {\"command\": \"python -u src/train_crm.py --precompute --benchmark spatial object --K 5 --cache_dir /root/autodl-tmp/crm_cache_k5/\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"79517\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-k5.log\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 26737, \"model_name\": \"smolvla_libero\", \"seed\": 42, \"hypothesis\": \"K=5 precompute for K sensitivity ablation (plan_015)\"}, \"reproduce\": {\"finished_at\": \"2026-05-13T22:09:33.445Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T22:09:34.396952+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache_k5/\", \"metrics\": {\"spatial_samples\": 12167, \"object_samples\": 14570, \"total_samples\": 26737, \"spatial_cache_mb\": 106, \"object_cache_mb\": 127, \"total_cache_mb\": 233, \"runtime_min\": 107}, \"completed_at\": \"2026-05-13T22:12:39.543Z\"}, \"mvp-point-reaching\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T01:22:10.415Z\", \"updated_at\": \"2026-05-13T22:06:11.073Z\", \"spec\": {\"hypothesis\": \"Per-DOF uncertainty features carry more actionable information than scalar uncertainty summaries, enabling dimension-selective correction\", \"description\": \"3D point-reaching MVP: 3 MLP variants (scalar/per-DOF/no uncertainty) x 6 groups (3 anisotropy ratios x 2 uncertainty sources)\", \"server\": \"bjb2-40593\", \"gpu\": \"cuda:0\", \"data_count\": 20000, \"model_name\": \"CorrectionMLP(2-layer, 64-hidden)\", \"seed\": 42, \"command\": \"python -u run_mvp.py\", \"data_path\": \"synthetic (generated in-script)\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/mvp/\", \"log_path\": \"/root/acr-vla-conformal-refinement/mvp/mvp_results.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T01:44:00.055Z\", \"metrics\": {\"group1_oracle\": {\"A_scalar\": {\"mse_x\": 0.180218, \"mse_y\": 0.02497, \"mse_z\": 0.024232, \"total\": 0.076473}, \"B_perDOF\": {\"mse_x\": 0.172652, \"mse_y\": 0.015544, \"mse_z\": 0.01561, \"total\": 0.067935}, \"C_none\": {\"mse_x\": 0.22706, \"mse_y\": 0.025542, \"mse_z\": 0.024753, \"total\": 0.092451}}, \"group2_oracle\": {\"A_scalar\": {\"mse_x\": 0.064642, \"mse_y\": 0.023836, \"mse_z\": 0.022967, \"total\": 0.037148}, \"B_perDOF\": {\"mse_x\": 0.053403, \"mse_y\": 0.015695, \"mse_z\": 0.01573, \"total\": 0.028276}, \"C_none\": {\"mse_x\": 0.084178, \"mse_y\": 0.025427, \"mse_z\": 0.024798, \"total\": 0.044801}}, \"group3_oracle\": {\"A_scalar\": {\"mse_x\": 0.042948, \"mse_y\": 0.023218, \"mse_z\": 0.022365, \"total\": 0.02951}, \"B_perDOF\": {\"mse_x\": 0.033008, \"mse_y\": 0.015621, \"mse_z\": 0.015647, \"total\": 0.021425}, \"C_none\": {\"mse_x\": 0.053043, \"mse_y\": 0.025523, \"mse_z\": 0.024741, \"total\": 0.034436}}, \"group4_K10\": {\"A_scalar\": {\"mse_x\": 0.187418, \"mse_y\": 0.024701, \"mse_z\": 0.024277, \"total\": 0.078799}, \"B_perDOF\": {\"mse_x\": 0.182888, \"mse_y\": 0.019072, \"mse_z\": 0.018475, \"total\": 0.073478}, \"C_none\": {\"mse_x\": 0.21507, \"mse_y\": 0.02496, \"mse_z\": 0.024637, \"total\": 0.088223}}, \"group5_K10\": {\"A_scalar\": {\"mse_x\": 0.064895, \"mse_y\": 0.02386, \"mse_z\": 0.023596, \"total\": 0.037451}, \"B_perDOF\": {\"mse_x\": 0.05851, \"mse_y\": 0.018868, \"mse_z\": 0.018471, \"total\": 0.03195}, \"C_none\": {\"mse_x\": 0.077047, \"mse_y\": 0.024825, \"mse_z\": 0.02464, \"total\": 0.042171}}, \"group6_K10\": {\"A_scalar\": {\"mse_x\": 0.041848, \"mse_y\": 0.02344, \"mse_z\": 0.023207, \"total\": 0.029498}, \"B_perDOF\": {\"mse_x\": 0.036348, \"mse_y\": 0.018736, \"mse_z\": 0.018453, \"total\": 0.024512}, \"C_none\": {\"mse_x\": 0.048365, \"mse_y\": 0.024827, \"mse_z\": 0.024577, \"total\": 0.03259}}, \"pass_criteria\": {\"group1\": \"PASS\", \"group4\": \"PASS\", \"overall\": \"SUCCESS\"}, \"summary_pct_improvements\": {\"reference_group\": \"group4_K10 (sigma=0.5/0.1/0.1, K=10 estimated uncertainty)\", \"perDOF_vs_scalar_total\": 6.75, \"perDOF_vs_none_total\": 16.71, \"perDOF_vs_scalar_y_axis\": 22.79, \"perDOF_vs_scalar_z_axis\": 23.9, \"paper_claims\": {\"6.7_pct_over_scalar\": \"group4 total: (0.078799-0.073478)/0.078799 = 6.75%\", \"16.7_pct_over_none\": \"group4 total: (0.088223-0.073478)/0.088223 = 16.71%\", \"22_24_pct_per_axis\": \"group4 y: 22.79%, z: 23.90%\"}}}}, \"eval-spatial-v3-full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T17:38:57.194Z\", \"updated_at\": \"2026-05-13T19:09:00.612Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl && python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 10 --seed 42 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ 2>&1\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"62654\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-spatial-v3-full.log\", \"submitted_at\": \"2026-05-13T17:38:57.172Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": \"10 tasks x 10 rollouts x 300 steps\", \"model_name\": \"lerobot/smolvla_libero (450M, rewritten wrapper aligned with lerobot pipeline)\", \"seed\": 42, \"hypothesis\": \"Rewritten wrapper (fully aligned with lerobot SmolVLAPolicy) achieves >50% on libero_spatial with 10 rollouts\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"failure_reason\": \"D014: wrapper 修复版从未部署到服务器，使用旧 buggy 代码运行，产出无效\", \"wall_clock_seconds\": 5403.4, \"gpu_hours\": 1.5}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T19:09:00.612Z\"}, \"eval-spatial-reeval-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T16:08:51.171Z\", \"updated_at\": \"2026-05-13T16:14:40.934Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 3 --seed 42 --smolvla_path /root/autodl-tmp/models/smolvla_libero/\", \"server\": \"autodl-4090x4\", \"gpu\": [\"cuda:0\"], \"pid\": \"87385\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": \"10 tasks x 3 rollouts x 300 steps\", \"model_name\": \"lerobot/smolvla_libero (450M, full fine-tuned)\", \"seed\": 42, \"hypothesis\": \"Fixed wrapper (7 bugs) achieves >50% on libero_spatial\", \"log_path\": \"/tmp/eval_spatial.log\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"failure_reason\": \"Killed by Director - wrapper not fully fixed, 55.6% result unreliable. Redirected to full wrapper rewrite aligned with lerobot pipeline.\", \"checkpoint_path\": \"N/A\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T16:14:40.934Z\"}, \"eval-smolvla-libero-spatial\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T11:35:16.236Z\", \"updated_at\": \"2026-05-13T15:45:51.082Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 3 --seed 42\", \"server\": \"autodl-4090x4\", \"gpu\": [\"cuda:0\"], \"pid\": \"43809\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": \"10 tasks x 3 rollouts x 300 steps\", \"model_name\": \"lerobot/smolvla_libero (450M, full fine-tuned on libero_spatial)\", \"seed\": 42, \"hypothesis\": \"Validate smolvla_libero checkpoint with fixed wrapper (correct state repr, 256x256 images, 7D action) achieves >50% success on libero_spatial\", \"log_path\": \"/tmp/eval_spatial_full.log\", \"checkpoint_source\": \"lerobot/smolvla_libero (HuggingFace community checkpoint)\", \"failure_reason\": \"smolvla_libero 0% on spatial - 6 wrapper bugs: image flip/size/normalization, state 6D→8D, state normalization, action denormalization all missing\", \"checkpoint_path\": \"N/A\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T15:45:51.082Z\"}, \"precompute-shard2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T11:57:48.056Z\", \"updated_at\": \"2026-05-13T15:26:07.463Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 2 --num_shards 3 --seed 42 --K 10\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"47186\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-shard2.log\", \"submitted_at\": \"2026-05-13T11:57:48.042Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache/\", \"wall_clock_seconds\": 12499.4, \"gpu_hours\": 3.47}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T15:26:07.463Z\"}, \"precompute-shard1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T11:57:46.669Z\", \"updated_at\": \"2026-05-13T15:26:06.485Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 1 --num_shards 3 --seed 42 --K 10\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"47044\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-shard1.log\", \"submitted_at\": \"2026-05-13T11:57:46.654Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache/\", \"wall_clock_seconds\": 12499.8, \"gpu_hours\": 3.47}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T15:26:06.485Z\"}, \"precompute-shard0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T11:57:45.284Z\", \"updated_at\": \"2026-05-13T15:26:05.433Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 0 --num_shards 3 --seed 42 --K 10\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"46966\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-shard0.log\", \"submitted_at\": \"2026-05-13T11:57:45.270Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache/\", \"wall_clock_seconds\": 12500.2, \"gpu_hours\": 3.47}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T15:26:05.433Z\"}, \"plan_014-reconvla-baseline\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-13T06:56:12.892Z\", \"updated_at\": \"2026-05-13T11:07:20.019Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark spatial object --n_rollouts 20 --seed 42\", \"server\": \"autodl-4090\", \"gpu\": [\"cuda:0\"], \"pid\": \"50790\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/plan_014-reconvla-baseline.log\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial + object)\", \"data_count\": \"20 tasks x 20 rollouts = 400 episodes\", \"model_name\": \"SmolVLA (450M) + ReconVLA argmin selection\", \"seed\": 42, \"hypothesis\": \"ReconVLA (scalar Euclidean nonconformity + argmin selection) as baseline for ACR-VLA comparison\", \"fixes_applied\": [\"BDDL path: use benchmark_instance.get_task_bddl_file_path()\", \"LIBERO assets copied from GitHub repo\"]}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T11:07:20.019Z\"}, \"plan_001-crm-smolvla\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T03:01:07.682Z\", \"updated_at\": \"2026-05-13T05:44:07.131Z\", \"spec\": {\"command\": \"python -u src/train_crm.py --auto --benchmark spatial object --epochs 50 --batch_size 32 --lr 1e-3 --seed 42 --K 10\", \"server\": \"autodl-4090\", \"gpu\": [\"cuda:0\"], \"pid\": \"32811\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/plan_001-crm-smolvla.log\", \"submitted_at\": \"2026-05-13T04:54:14.975Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial + object)\", \"data_count\": 1000, \"model_name\": \"CRM (337K) + SmolVLA (450M)\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm/\", \"hypothesis\": \"Per-DOF conformal features enable dimension-selective action correction on LIBERO\", \"wall_clock_seconds\": 2992.2, \"gpu_hours\": 0.83}, \"conclusion\": \"failed\", \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"completed_at\": \"2026-05-13T05:44:07.131Z\"}}, \"count\": 161, \"total\": 161, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4282}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 9_

数据量太大，用子代理处理。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "17ac476a-dce3-448f-b7ca-396cbd486cca",
  "uuid": "331a42b0-eb74-44ce-af38-5a834f4f55e5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tyk58bDV1hxZM9ZJJsycmm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 625,
      "cache_read_input_tokens": 25045,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 625
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

_source line 10_

<details open><summary>🔧 Tool call — Agent · `toolu_017jeRjGwGz5FwezgA7fQo6P`</summary>

```json
{
  "description": "Extract magnitude sweep data",
  "prompt": "I need you to extract experiment data from a large JSON registry file and produce a structured summary.\n\nThe file is at: `/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/17ac476a-dce3-448f-b7ca-396cbd486cca/tool-results/mcp-agent-ml-research-read_registry-1778969659294.txt`\n\nThe file is JSON with schema: `{result: string}` — the `result` field is itself a JSON string that needs to be parsed.\n\n**What I need:**\n\nExtract all experiments whose `exp_id` matches the \"object benchmark\" magnitude sweep pattern. The naming conventions are:\n- `eval-obs-only-object-norm{NN}-seed{XX}` (norm02=0.2, norm01=0.1, norm005=0.05, norm003=0.03, norm03=0.3)\n- `eval-perdof-object-norm{NN}-seed{XX}`\n- `eval-argmin-object-seed{XX}`\n- `eval-scalar-object-seed{XX}`\n- `eval-vla-mean-object-seed{XX}`\n- `eval-vla-only-object-seed{XX}`\n- `eval-obs-only-object-default-seed{XX}` (norm=default≈1.42)\n- `eval-perdof-object-default-seed{XX}`\n\nFor each matching experiment, extract:\n1. `exp_id`\n2. `status` (DONE, RUNNING, FAILED, etc.)\n3. `metrics` — specifically `overall_sr` (overall success rate)\n4. Any progress info if RUNNING\n\n**Output format:**\nPrint a Python-parseable list of dicts, one per experiment, with keys: `exp_id`, `method`, `norm`, `seed`, `status`, `overall_sr`, `progress_info`\n\nWhere:\n- `method`: one of obs_only, perdof, argmin, scalar, vla_mean, vla_only\n- `norm`: float value (0.03, 0.05, 0.10, 0.20, 0.30, 1.42 for default) or None for methods without norm\n- `seed`: integer\n- `overall_sr`: float or None if not available\n- `progress_info`: string or None\n\nUse jq or python to parse the file. The file may be very large so work efficiently. Print the final structured output so I can use it."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "17ac476a-dce3-448f-b7ca-396cbd486cca",
  "uuid": "409eca22-7d99-4150-bafa-0caf641f59bd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tyk58bDV1hxZM9ZJJsycmm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 625,
      "cache_read_input_tokens": 25045,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 625
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

_source line 11_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a58b6d9515d921b8d",
  "tool_use_id": "toolu_017jeRjGwGz5FwezgA7fQo6P",
  "description": "Extract magnitude sweep data",
  "task_type": "local_agent",
  "prompt": "I need you to extract experiment data from a large JSON registry file and produce a structured summary.\n\nThe file is at: `/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/17ac476a-dce3-448f-b7ca-396cbd486cca/tool-results/mcp-agent-ml-research-read_registry-1778969659294.txt`\n\nThe file is JSON with schema: `{result: string}` — the `result` field is itself a JSON string that needs to be parsed.\n\n**What I need:**\n\nExtract all experiments whose `exp_id` matches the \"object benchmark\" magnitude sweep pattern. The naming conventions are:\n- `eval-obs-only-object-norm{NN}-seed{XX}` (norm02=0.2, norm01=0.1, norm005=0.05, norm003=0.03, norm03=0.3)\n- `eval-perdof-object-norm{NN}-seed{XX}`\n- `eval-argmin-object-seed{XX}`\n- `eval-scalar-object-seed{XX}`\n- `eval-vla-mean-object-seed{XX}`\n- `eval-vla-only-object-seed{XX}`\n- `eval-obs-only-object-default-seed{XX}` (norm=default≈1.42)\n- `eval-perdof-object-default-seed{XX}`\n\nFor each matching experiment, extract:\n1. `exp_id`\n2. `status` (DONE, RUNNING, FAILED, etc.)\n3. `metrics` — specifically `overall_sr` (overall success rate)\n4. Any progress info if RUNNING\n\n**Output format:**\nPrint a Python-parseable list of dicts, one per experiment, with keys: `exp_id`, `method`, `norm`, `seed`, `status`, `overall_sr`, `progress_info`\n\nWhere:\n- `method`: one of obs_only, perdof, argmin, scalar, vla_mean, vla_only\n- `norm`: float value (0.03, 0.05, 0.10, 0.20, 0.30, 1.42 for default) or None for methods without norm\n- `seed`: integer\n- `overall_sr`: float or None if not available\n- `progress_info`: string or None\n\nUse jq or python to parse the file. The file may be very large so work efficiently. Print the final structured output so I can use it.",
  "uuid": "90ff3b03-109e-446e-a766-ff7f48b4e932",
  "session_id": "17ac476a-dce3-448f-b7ca-396cbd486cca"
}
```

---

## Round 1

38 recorded events

### User

_source line 12 · 2026-05-16T22:14:31.828Z_

I need you to extract experiment data from a large JSON registry file and produce a structured summary.

The file is at: `/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/17ac476a-dce3-448f-b7ca-396cbd486cca/tool-results/mcp-agent-ml-research-read_registry-1778969659294.txt`

The file is JSON with schema: `{result: string}` — the `result` field is itself a JSON string that needs to be parsed.

**What I need:**

Extract all experiments whose `exp_id` matches the "object benchmark" magnitude sweep pattern. The naming conventions are:
- `eval-obs-only-object-norm{NN}-seed{XX}` (norm02=0.2, norm01=0.1, norm005=0.05, norm003=0.03, norm03=0.3)
- `eval-perdof-object-norm{NN}-seed{XX}`
- `eval-argmin-object-seed{XX}`
- `eval-scalar-object-seed{XX}`
- `eval-vla-mean-object-seed{XX}`
- `eval-vla-only-object-seed{XX}`
- `eval-obs-only-object-default-seed{XX}` (norm=default≈1.42)
- `eval-perdof-object-default-seed{XX}`

For each matching experiment, extract:
1. `exp_id`
2. `status` (DONE, RUNNING, FAILED, etc.)
3. `metrics` — specifically `overall_sr` (overall success rate)
4. Any progress info if RUNNING

**Output format:**
Print a Python-parseable list of dicts, one per experiment, with keys: `exp_id`, `method`, `norm`, `seed`, `status`, `overall_sr`, `progress_info`

Where:
- `method`: one of obs_only, perdof, argmin, scalar, vla_mean, vla_only
- `norm`: float value (0.03, 0.05, 0.10, 0.20, 0.30, 1.42 for default) or None for methods without norm
- `seed`: integer
- `overall_sr`: float or None if not available
- `progress_info`: string or None

Use jq or python to parse the file. The file may be very large so work efficiently. Print the final structured output so I can use it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_017jeRjGwGz5FwezgA7fQo6P",
  "session_id": "17ac476a-dce3-448f-b7ca-396cbd486cca",
  "uuid": "aedbe4d4-7a42-4bf8-89a4-2feadbc0f1b9"
}
```

</details>

---

### System

_source line 13_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a58b6d9515d921b8d",
  "tool_use_id": "toolu_017jeRjGwGz5FwezgA7fQo6P",
  "description": "Running Check file size",
  "usage": {
    "total_tokens": 16044,
    "tool_uses": 1,
    "duration_ms": 3825
  },
  "last_tool_name": "Bash",
  "uuid": "6dfecd15-7fc7-4463-8d55-20b78c46c489",
  "session_id": "17ac476a-dce3-448f-b7ca-396cbd486cca"
}
```

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Bash · `toolu_01MtGZbAbnqy5FzyoJkRYeNX`</summary>

```json
{
  "command": "wc -c /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/17ac476a-dce3-448f-b7ca-396cbd486cca/tool-results/mcp-agent-ml-research-read_registry-1778969659294.txt",
  "description": "Check file size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_017jeRjGwGz5FwezgA7fQo6P",
  "session_id": "17ac476a-dce3-448f-b7ca-396cbd486cca",
  "uuid": "6a26c4e3-33fe-4a23-b75e-0c551bfcd188",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011hRBBk4p6Sy2eV8XnH4GQ9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15983,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15983,
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

_source line 15 · 2026-05-16T22:14:35.814Z_

<details><summary>↩ Tool result · `toolu_01MtGZbAbnqy5FzyoJkRYeNX`</summary>

```text
246786 /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/17ac476a-dce3-448f-b7ca-396cbd486cca/tool-results/mcp-agent-ml-research-read_registry-1778969659294.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_017jeRjGwGz5FwezgA7fQo6P",
  "session_id": "17ac476a-dce3-448f-b7ca-396cbd486cca",
  "uuid": "c136eaa2-c1bd-47c8-bc48-57cc23aba042"
}
```

</details>

---

### System

_source line 16_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a58b6d9515d921b8d",
  "tool_use_id": "toolu_017jeRjGwGz5FwezgA7fQo6P",
  "description": "Running Parse registry JSON and extract object benchmark magnitude sweep experiments",
  "usage": {
    "total_tokens": 17207,
    "tool_uses": 2,
    "duration_ms": 24477
  },
  "last_tool_name": "Bash",
  "uuid": "8b6889d2-4cdb-4c27-87df-dd762361c44f",
  "session_id": "17ac476a-dce3-448f-b7ca-396cbd486cca"
}
```

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Bash · `toolu_0113Ynvug9uVvAqmmxHjvjED`</summary>

```json
{
  "command": "python3 << 'EOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/17ac476a-dce3-448f-b7ca-396cbd486cca/tool-results/mcp-agent-ml-research-read_registry-1778969659294.txt\"\n\nwith open(filepath, 'r') as f:\n    outer = json.loads(f.read())\n\n# The result field is itself a JSON string\nregistry = json.loads(outer['result'])\n\n# Patterns to match\nimport re\n\npatterns = [\n    r'^eval-obs-only-object-norm\\d+-seed\\d+$',\n    r'^eval-perdof-object-norm\\d+-seed\\d+$',\n    r'^eval-argmin-object-seed\\d+$',\n    r'^eval-scalar-object-seed\\d+$',\n    r'^eval-vla-mean-object-seed\\d+$',\n    r'^eval-vla-only-object-seed\\d+$',\n    r'^eval-obs-only-object-default-seed\\d+$',\n    r'^eval-perdof-object-default-seed\\d+$',\n]\n\ncombined_pattern = '|'.join(patterns)\n\ndef parse_method_norm_seed(exp_id):\n    # obs_only with norm\n    m = re.match(r'^eval-obs-only-object-norm(\\d+)-seed(\\d+)$', exp_id)\n    if m:\n        norm_str = m.group(1)\n        seed = int(m.group(2))\n        norm_map = {'02': 0.2, '01': 0.1, '005': 0.05, '003': 0.03, '03': 0.3}\n        norm = norm_map.get(norm_str, float('0.' + norm_str))\n        return 'obs_only', norm, seed\n\n    # obs_only default\n    m = re.match(r'^eval-obs-only-object-default-seed(\\d+)$', exp_id)\n    if m:\n        return 'obs_only', 1.42, int(m.group(1))\n\n    # perdof with norm\n    m = re.match(r'^eval-perdof-object-norm(\\d+)-seed(\\d+)$', exp_id)\n    if m:\n        norm_str = m.group(1)\n        seed = int(m.group(2))\n        norm_map = {'02': 0.2, '01': 0.1, '005': 0.05, '003': 0.03, '03': 0.3}\n        norm = norm_map.get(norm_str, float('0.' + norm_str))\n        return 'perdof', norm, seed\n\n    # perdof default\n    m = re.match(r'^eval-perdof-object-default-seed(\\d+)$', exp_id)\n    if m:\n        return 'perdof', 1.42, int(m.group(1))\n\n    # argmin\n    m = re.match(r'^eval-argmin-object-seed(\\d+)$', exp_id)\n    if m:\n        return 'argmin', None, int(m.group(1))\n\n    # scalar\n    m = re.match(r'^eval-scalar-object-seed(\\d+)$', exp_id)\n    if m:\n        return 'scalar', None, int(m.group(1))\n\n    # vla_mean\n    m = re.match(r'^eval-vla-mean-object-seed(\\d+)$', exp_id)\n    if m:\n        return 'vla_mean', None, int(m.group(1))\n\n    # vla_only\n    m = re.match(r'^eval-vla-only-object-seed(\\d+)$', exp_id)\n    if m:\n        return 'vla_only', None, int(m.group(1))\n\n    return None, None, None\n\n# Find matching experiments\nresults = []\n\n# registry could be a dict with 'experiments' key or a list\nif isinstance(registry, dict):\n    experiments = registry.get('experiments', registry)\n    if isinstance(experiments, dict):\n        exp_list = list(experiments.values()) if not all(isinstance(v, dict) and 'exp_id' in v for v in experiments.values()) else list(experiments.values())\n        # Try treating keys as exp_ids\n        exp_items = []\n        for k, v in experiments.items():\n            if isinstance(v, dict):\n                if 'exp_id' not in v:\n                    v['exp_id'] = k\n                exp_items.append(v)\n        experiments = exp_items\n    elif isinstance(experiments, list):\n        pass\nelse:\n    experiments = registry\n\nfor exp in experiments:\n    if not isinstance(exp, dict):\n        continue\n    exp_id = exp.get('exp_id', '')\n    if re.match(combined_pattern, exp_id):\n        method, norm, seed = parse_method_norm_seed(exp_id)\n        status = exp.get('status', None)\n        metrics = exp.get('metrics', {}) or {}\n        overall_sr = metrics.get('overall_sr', None)\n        progress_info = exp.get('progress', None) or exp.get('progress_info', None)\n        if progress_info and isinstance(progress_info, dict):\n            progress_info = str(progress_info)\n        results.append({\n            'exp_id': exp_id,\n            'method': method,\n            'norm': norm,\n            'seed': seed,\n            'status': status,\n            'overall_sr': overall_sr,\n            'progress_info': progress_info,\n        })\n\n# Sort by method, norm, seed\ndef sort_key(x):\n    method_order = {'obs_only': 0, 'perdof': 1, 'argmin': 2, 'scalar': 3, 'vla_mean': 4, 'vla_only': 5}\n    return (method_order.get(x['method'], 99), x['norm'] or 0, x['seed'])\n\nresults.sort(key=sort_key)\n\nprint(f\"# Found {len(results)} matching experiments\\n\")\n# Print as Python list\nimport pprint\npprint.pprint(results)\nEOF",
  "description": "Parse registry JSON and extract object benchmark magnitude sweep experiments",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_017jeRjGwGz5FwezgA7fQo6P",
  "session_id": "17ac476a-dce3-448f-b7ca-396cbd486cca",
  "uuid": "36a9b404-78dc-4e4e-8a71-7c30aaaa0e6c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JyiCFu7fkDUhKKLAgURVMB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1113,
      "cache_read_input_tokens": 15983,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1113,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 52,
      "service_tier": "standard",
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

_source line 18 · 2026-05-16T22:14:56.445Z_

<details><summary>↩ Tool result · `toolu_0113Ynvug9uVvAqmmxHjvjED`</summary>

```text
# Found 0 matching experiments

[]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_017jeRjGwGz5FwezgA7fQo6P",
  "session_id": "17ac476a-dce3-448f-b7ca-396cbd486cca",
  "uuid": "034607d4-d11d-425b-888d-ac38702113bf"
}
```

</details>

---

### System

_source line 19_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a58b6d9515d921b8d",
  "tool_use_id": "toolu_017jeRjGwGz5FwezgA7fQo6P",
  "description": "Running Inspect registry structure",
  "usage": {
    "total_tokens": 18922,
    "tool_uses": 3,
    "duration_ms": 30890
  },
  "last_tool_name": "Bash",
  "uuid": "e36130e8-8c45-46e3-b403-d75e5876f19e",
  "session_id": "17ac476a-dce3-448f-b7ca-396cbd486cca"
}
```

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Bash · `toolu_016z1p9GBJkKq9xFARiVNX5z`</summary>

```json
{
  "command": "python3 << 'EOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/17ac476a-dce3-448f-b7ca-396cbd486cca/tool-results/mcp-agent-ml-research-read_registry-1778969659294.txt\"\n\nwith open(filepath, 'r') as f:\n    outer = json.loads(f.read())\n\n# The result field is itself a JSON string\nregistry = json.loads(outer['result'])\n\nprint(\"Type of registry:\", type(registry))\nif isinstance(registry, dict):\n    print(\"Top-level keys:\", list(registry.keys())[:20])\n    # Check first few entries\n    for i, (k, v) in enumerate(registry.items()):\n        if i < 3:\n            print(f\"\\nKey: {k}\")\n            print(f\"Value type: {type(v)}\")\n            if isinstance(v, dict):\n                print(f\"Value keys: {list(v.keys())[:10]}\")\nelif isinstance(registry, list):\n    print(f\"List length: {len(registry)}\")\n    if registry:\n        print(\"First item:\", registry[0])\nEOF",
  "description": "Inspect registry structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_017jeRjGwGz5FwezgA7fQo6P",
  "session_id": "17ac476a-dce3-448f-b7ca-396cbd486cca",
  "uuid": "2ca8ac59-6890-4e01-8c7c-31f4b4f6493e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012jyhUMakrUn5dtrRpWvmaD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1713,
      "cache_read_input_tokens": 17096,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1713,
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

_source line 21 · 2026-05-16T22:15:02.856Z_

<details><summary>↩ Tool result · `toolu_016z1p9GBJkKq9xFARiVNX5z`</summary>

```text
Type of registry: &lt;class 'dict'>
Top-level keys: ['success', 'data', 'error', 'metadata']

Key: success
Value type: &lt;class 'bool'>

Key: data
Value type: &lt;class 'dict'>
Value keys: ['experiments', 'count', 'total', 'baseline']

Key: error
Value type: &lt;class 'NoneType'>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_017jeRjGwGz5FwezgA7fQo6P",
  "session_id": "17ac476a-dce3-448f-b7ca-396cbd486cca",
  "uuid": "2c10d8d4-071f-4240-90fe-6ed3f6305cf4"
}
```

</details>

---

### System

_source line 22_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a58b6d9515d921b8d",
  "tool_use_id": "toolu_017jeRjGwGz5FwezgA7fQo6P",
  "description": "Running Inspect experiments structure",
  "usage": {
    "total_tokens": 19507,
    "tool_uses": 4,
    "duration_ms": 37226
  },
  "last_tool_name": "Bash",
  "uuid": "b62c4e1d-aa68-4b3f-afe1-9baedec7d26a",
  "session_id": "17ac476a-dce3-448f-b7ca-396cbd486cca"
}
```

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Bash · `toolu_01PSVL2aB7sSsgnEdnVuVhQQ`</summary>

```json
{
  "command": "python3 << 'EOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/17ac476a-dce3-448f-b7ca-396cbd486cca/tool-results/mcp-agent-ml-research-read_registry-1778969659294.txt\"\n\nwith open(filepath, 'r') as f:\n    outer = json.loads(f.read())\n\nregistry = json.loads(outer['result'])\ndata = registry['data']\nexperiments = data['experiments']\n\nprint(f\"Type of experiments: {type(experiments)}\")\nprint(f\"Count: {data.get('count')}, Total: {data.get('total')}\")\n\nif isinstance(experiments, dict):\n    keys = list(experiments.keys())\n    print(f\"\\nNumber of experiment keys: {len(keys)}\")\n    print(\"First 20 keys:\", keys[:20])\n    # Show one example\n    first_key = keys[0]\n    print(f\"\\nExample entry '{first_key}':\")\n    print(json.dumps(experiments[first_key], indent=2)[:1000])\nelif isinstance(experiments, list):\n    print(f\"List length: {len(experiments)}\")\n    print(\"First item:\", json.dumps(experiments[0], indent=2)[:500])\nEOF",
  "description": "Inspect experiments structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_017jeRjGwGz5FwezgA7fQo6P",
  "session_id": "17ac476a-dce3-448f-b7ca-396cbd486cca",
  "uuid": "569e56ec-56ae-4813-809d-db63921e6ca1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QzMyQm5rB3U6nq4nKSrnTn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 513,
      "cache_read_input_tokens": 18809,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 513,
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

_source line 24 · 2026-05-16T22:15:09.147Z_

<details><summary>↩ Tool result · `toolu_01PSVL2aB7sSsgnEdnVuVhQQ`</summary>

```text
Type of experiments: &lt;class 'dict'>
Count: 161, Total: 161

Number of experiment keys: 161
First 20 keys: ['eval-argmin-object-seed47', 'eval-perdof-object-norm03-seed45-r2', 'eval-obs-only-object-norm02-seed47', 'eval-obs-only-object-norm02-seed45', 'eval-scalar-object-seed44-r2', 'eval-obs-only-object-default-seed44', 'eval-perdof-object-default-seed45', 'eval-perdof-object-norm01-seed45', 'eval-perdof-object-norm01-seed44', 'eval-perdof-object-seed44', 'eval-obs-only-object-norm01-seed44', 'eval-obs-only-object-norm03-seed44', 'eval-argmin-object-seed46', 'eval-vla-mean-object-seed44', 'eval-obs-only-object-norm02-seed46', 'eval-perdof-object-norm03-seed44', 'eval-obs-only-object-norm03-seed45-r2', 'eval-obs-only-object-norm02-seed44-r4', 'eval-argmin-object-seed44-r2', 'eval-obs-only-object-norm02-seed44-r2']

Example entry 'eval-argmin-object-seed47':
{
  "status": "RUNNING",
  "retry_count": 0,
  "created_at": "2026-05-16T21:38:21.922Z",
  "updated_at": "2026-05-16T21:40:21.037Z",
  "hypothesis": "Argmin baseline (reconvla K=10) seed=47 on LIBERO object benchmark. Paired with obs_only seed47 on cuda:0 for direct comparison. Extends argmin multi-seed data for pooled Fisher test.",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 47 --K 10 --output_file logs/eval_object_reconvla_seed47.json\"",
    "server": "bjb1-32546",
    "gpu": [
      "cuda:3"
    ],
    "pid": "322337",
    "log_path": "~/runs/acr-vla-conformal-refinement/eval-argmin-object-seed47.log",
    "submitted_at": "2026-05-16T21:39:10.031Z",
    "submitted_via": "submit_trai
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_017jeRjGwGz5FwezgA7fQo6P",
  "session_id": "17ac476a-dce3-448f-b7ca-396cbd486cca",
  "uuid": "199aa8b5-943d-487c-b2d2-43105f2ceeba"
}
```

</details>

---

### System

_source line 25_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a58b6d9515d921b8d",
  "tool_use_id": "toolu_017jeRjGwGz5FwezgA7fQo6P",
  "description": "Running List all object-related experiment keys",
  "usage": {
    "total_tokens": 20772,
    "tool_uses": 5,
    "duration_ms": 48693
  },
  "last_tool_name": "Bash",
  "uuid": "95fe7d18-5574-4f62-b756-798c85493202",
  "session_id": "17ac476a-dce3-448f-b7ca-396cbd486cca"
}
```

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — Bash · `toolu_018YVQF7aN9fse57FTS776q5`</summary>

```json
{
  "command": "python3 << 'EOF'\nimport json\nimport re\n\nfilepath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/17ac476a-dce3-448f-b7ca-396cbd486cca/tool-results/mcp-agent-ml-research-read_registry-1778969659294.txt\"\n\nwith open(filepath, 'r') as f:\n    outer = json.loads(f.read())\n\nregistry = json.loads(outer['result'])\nexperiments = registry['data']['experiments']\n\n# Now let's look at naming patterns more carefully - there are also \"-r2\", \"-r3\" suffixes\n# Let's see all keys that contain \"object\"\nobject_keys = [k for k in experiments.keys() if 'object' in k]\nprint(f\"Total object keys: {len(object_keys)}\")\nfor k in sorted(object_keys):\n    print(k)\nEOF",
  "description": "List all object-related experiment keys"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_017jeRjGwGz5FwezgA7fQo6P",
  "session_id": "17ac476a-dce3-448f-b7ca-396cbd486cca",
  "uuid": "a5d3180e-3d37-4329-8e41-2f9e2ae332f7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015qLoC9ZF9b8JA7YUSeEBxV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1192,
      "cache_read_input_tokens": 19322,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1192,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 73,
      "service_tier": "standard",
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

_source line 27 · 2026-05-16T22:15:20.680Z_

<details><summary>↩ Tool result · `toolu_018YVQF7aN9fse57FTS776q5`</summary>

```text
Total object keys: 78
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
eval-argmin-object-seed43
eval-argmin-object-seed44
eval-argmin-object-seed44-r2
eval-argmin-object-seed44-r3
eval-argmin-object-seed45
eval-argmin-object-seed46
eval-argmin-object-seed47
eval-mag-obsonly-norm003-object
eval-mag-obsonly-norm005-object
eval-mag-obsonly-norm02-object
eval-mag-obsonly-norm03-object
eval-mag-perdof-norm003-object
eval-mag-perdof-norm005-object
eval-mag-perdof-norm02-object
eval-mag-perdof-norm02-seed43-object
eval-mag-perdof-norm02-seed43-object-r2
eval-mag-perdof-norm02-seed43-object-r3
eval-mag-perdof-norm03-object
eval-mag-perdof-norm03-object-r2
eval-mag-perdof-norm03-object-r3
eval-mag-perdof-norm0p3-object
eval-mag-perdof-norm0p3-object-r2
eval-object-v4-full
eval-object-v5-full
eval-object-v6-full
eval-object-v7-full
eval-object-v8-full
eval-obs-only-object-default-seed44
eval-obs-only-object-default-seed45
eval-obs-only-object-norm01-seed44
eval-obs-only-object-norm01-seed45
eval-obs-only-object-norm02-seed43
eval-obs-only-object-norm02-seed43-r2
eval-obs-only-object-norm02-seed44
eval-obs-only-object-norm02-seed44-r2
eval-obs-only-object-norm02-seed44-r3
eval-obs-only-object-norm02-seed44-r4
eval-obs-only-object-norm02-seed45
eval-obs-only-object-norm02-seed46
eval-obs-only-object-norm02-seed47
eval-obs-only-object-norm03-seed44
eval-obs-only-object-norm03-seed45
eval-obs-only-object-norm03-seed45-r2
eval-obs-only-object-seed43
eval-perdof-object-default-seed44
eval-perdof-object-default-seed45
eval-perdof-object-norm01-seed44
eval-perdof-object-norm01-seed45
eval-perdof-object-norm02-seed45
eval-perdof-object-norm03-seed44
eval-perdof-object-norm03-seed45-r2
eval-perdof-object-seed43
eval-perdof-object-seed44
eval-reconvla-object
eval-scalar-object-seed43
eval-scalar-object-seed44
eval-scalar-object-seed44-r2
eval-scalar-object-seed45
eval-vla-mean-object
eval-vla-mean-object-seed43
eval-vla-mean-object-seed44
eval-vla-mean-object-seed45
eval-vla-only-object
eval-vla-only-object-k1
eval-vla-only-object-seed43
eval-vla-only-object-seed44
eval-vla-only-object-seed44-r2
eval-vla-only-object-seed45
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_017jeRjGwGz5FwezgA7fQo6P",
  "session_id": "17ac476a-dce3-448f-b7ca-396cbd486cca",
  "uuid": "59c0aa29-a31f-42d5-8b0b-a389da7fca7c"
}
```

</details>

---

### System

_source line 28_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a58b6d9515d921b8d",
  "tool_use_id": "toolu_017jeRjGwGz5FwezgA7fQo6P",
  "description": "Running Parse all object benchmark magnitude sweep experiments with broader matching",
  "usage": {
    "total_tokens": 22163,
    "tool_uses": 6,
    "duration_ms": 83193
  },
  "last_tool_name": "Bash",
  "uuid": "3aa3838e-aa69-404a-bdca-6476f51bcad8",
  "session_id": "17ac476a-dce3-448f-b7ca-396cbd486cca"
}
```

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Bash · `toolu_01KdXpPECkTr7pPLGBbpoky3`</summary>

```json
{
  "command": "python3 << 'EOF'\nimport json\nimport re\nimport pprint\n\nfilepath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/17ac476a-dce3-448f-b7ca-396cbd486cca/tool-results/mcp-agent-ml-research-read_registry-1778969659294.txt\"\n\nwith open(filepath, 'r') as f:\n    outer = json.loads(f.read())\n\nregistry = json.loads(outer['result'])\nexperiments = registry['data']['experiments']\n\n# Updated patterns to include retry suffixes (-r2, -r3, -r4) and also the legacy \"eval-mag-*\" pattern\n# and entries without seed or with different naming\n# Let me be comprehensive and match ALL object benchmark magnitude sweep experiments\n\n# The patterns requested:\n# eval-obs-only-object-norm{NN}-seed{XX}(-rN)?\n# eval-perdof-object-norm{NN}-seed{XX}(-rN)?\n# eval-argmin-object-seed{XX}(-rN)?\n# eval-scalar-object-seed{XX}(-rN)?\n# eval-vla-mean-object-seed{XX}(-rN)?\n# eval-vla-only-object-seed{XX}(-rN)?\n# eval-obs-only-object-default-seed{XX}(-rN)?\n# eval-perdof-object-default-seed{XX}(-rN)?\n# Also: eval-obs-only-object-seed{XX} (no norm specified)\n# Also: eval-perdof-object-seed{XX} (no norm specified)\n# Also: eval-mag-obsonly-norm{NN}-object, eval-mag-perdof-norm{NN}-object (earlier naming)\n\npatterns_with_captures = [\n    # obs_only with explicit norm and seed\n    (r'^eval-obs-only-object-norm(\\d+p?\\d*)-seed(\\d+)(-r\\d+)?$', 'obs_only', True, True),\n    # obs_only default with seed\n    (r'^eval-obs-only-object-default-seed(\\d+)(-r\\d+)?$', 'obs_only', False, True),\n    # obs_only with seed only (no norm keyword)\n    (r'^eval-obs-only-object-seed(\\d+)(-r\\d+)?$', 'obs_only', False, True),\n    # perdof with explicit norm and seed\n    (r'^eval-perdof-object-norm(\\d+p?\\d*)-seed(\\d+)(-r\\d+)?$', 'perdof', True, True),\n    # perdof default with seed\n    (r'^eval-perdof-object-default-seed(\\d+)(-r\\d+)?$', 'perdof', False, True),\n    # perdof with seed only (no norm keyword)\n    (r'^eval-perdof-object-seed(\\d+)(-r\\d+)?$', 'perdof', False, True),\n    # argmin with seed\n    (r'^eval-argmin-object-seed(\\d+)(-r\\d+)?$', 'argmin', False, True),\n    # scalar with seed\n    (r'^eval-scalar-object-seed(\\d+)(-r\\d+)?$', 'scalar', False, True),\n    # vla_mean with seed\n    (r'^eval-vla-mean-object-seed(\\d+)(-r\\d+)?$', 'vla_mean', False, True),\n    # vla_only with seed\n    (r'^eval-vla-only-object-seed(\\d+)(-r\\d+)?$', 'vla_only', False, True),\n    # Legacy mag patterns\n    (r'^eval-mag-obsonly-norm(\\d+p?\\d*)-object(-r\\d+)?$', 'obs_only', True, False),\n    (r'^eval-mag-obsonly-norm(\\d+p?\\d*)-seed(\\d+)-object(-r\\d+)?$', 'obs_only', True, True),\n    (r'^eval-mag-perdof-norm(\\d+p?\\d*)-object(-r\\d+)?$', 'perdof', True, False),\n    (r'^eval-mag-perdof-norm(\\d+p?\\d*)-seed(\\d+)-object(-r\\d+)?$', 'perdof', True, True),\n    # Also seedless versions\n    (r'^eval-vla-mean-object(-r\\d+)?$', 'vla_mean', False, False),\n    (r'^eval-vla-only-object(-r\\d+)?$', 'vla_only', False, False),\n    (r'^eval-perdof-object-norm(\\d+p?\\d*)-seed(\\d+)(-r\\d+)?$', 'perdof', True, True),\n]\n\nnorm_map = {'02': 0.2, '01': 0.1, '005': 0.05, '003': 0.03, '03': 0.3, '0p3': 0.3}\n\ndef parse_norm(norm_str):\n    if norm_str in norm_map:\n        return norm_map[norm_str]\n    # Try parsing as \"0p3\" -> 0.3\n    if 'p' in norm_str:\n        return float(norm_str.replace('p', '.'))\n    # fallback: interpret as 0.{digits}\n    return float('0.' + norm_str)\n\ndef parse_experiment(exp_id):\n    \"\"\"Returns (method, norm, seed) or None if no match\"\"\"\n    \n    # obs_only with explicit norm and seed\n    m = re.match(r'^eval-obs-only-object-norm(\\d+p?\\d*)-seed(\\d+)(-r\\d+)?$', exp_id)\n    if m:\n        return 'obs_only', parse_norm(m.group(1)), int(m.group(2))\n    \n    # obs_only default with seed\n    m = re.match(r'^eval-obs-only-object-default-seed(\\d+)(-r\\d+)?$', exp_id)\n    if m:\n        return 'obs_only', 1.42, int(m.group(1))\n    \n    # obs_only with seed only (no norm)\n    m = re.match(r'^eval-obs-only-object-seed(\\d+)(-r\\d+)?$', exp_id)\n    if m:\n        return 'obs_only', None, int(m.group(1))\n    \n    # perdof with explicit norm and seed\n    m = re.match(r'^eval-perdof-object-norm(\\d+p?\\d*)-seed(\\d+)(-r\\d+)?$', exp_id)\n    if m:\n        return 'perdof', parse_norm(m.group(1)), int(m.group(2))\n    \n    # perdof default with seed\n    m = re.match(r'^eval-perdof-object-default-seed(\\d+)(-r\\d+)?$', exp_id)\n    if m:\n        return 'perdof', 1.42, int(m.group(1))\n    \n    # perdof with seed only\n    m = re.match(r'^eval-perdof-object-seed(\\d+)(-r\\d+)?$', exp_id)\n    if m:\n        return 'perdof', None, int(m.group(1))\n    \n    # argmin with seed\n    m = re.match(r'^eval-argmin-object-seed(\\d+)(-r\\d+)?$', exp_id)\n    if m:\n        return 'argmin', None, int(m.group(1))\n    \n    # scalar with seed\n    m = re.match(r'^eval-scalar-object-seed(\\d+)(-r\\d+)?$', exp_id)\n    if m:\n        return 'scalar', None, int(m.group(1))\n    \n    # vla_mean with seed\n    m = re.match(r'^eval-vla-mean-object-seed(\\d+)(-r\\d+)?$', exp_id)\n    if m:\n        return 'vla_mean', None, int(m.group(1))\n    \n    # vla_mean without seed\n    m = re.match(r'^eval-vla-mean-object(-r\\d+)?$', exp_id)\n    if m:\n        return 'vla_mean', None, None\n    \n    # vla_only with seed\n    m = re.match(r'^eval-vla-only-object-seed(\\d+)(-r\\d+)?$', exp_id)\n    if m:\n        return 'vla_only', None, int(m.group(1))\n    \n    # vla_only without seed\n    m = re.match(r'^eval-vla-only-object(-r\\d+)?$', exp_id)\n    if m:\n        return 'vla_only', None, None\n\n    # Legacy: eval-mag-obsonly-norm{NN}-object\n    m = re.match(r'^eval-mag-obsonly-norm(\\d+p?\\d*)-object(-r\\d+)?$', exp_id)\n    if m:\n        return 'obs_only', parse_norm(m.group(1)), None\n    \n    # Legacy: eval-mag-obsonly-norm{NN}-seed{XX}-object\n    m = re.match(r'^eval-mag-obsonly-norm(\\d+p?\\d*)-seed(\\d+)-object(-r\\d+)?$', exp_id)\n    if m:\n        return 'obs_only', parse_norm(m.group(1)), int(m.group(2))\n    \n    # Legacy: eval-mag-perdof-norm{NN}-object\n    m = re.match(r'^eval-mag-perdof-norm(\\d+p?\\d*)-object(-r\\d+)?$', exp_id)\n    if m:\n        return 'perdof', parse_norm(m.group(1)), None\n    \n    # Legacy: eval-mag-perdof-norm{NN}-seed{XX}-object\n    m = re.match(r'^eval-mag-perdof-norm(\\d+p?\\d*)-seed(\\d+)-object(-r\\d+)?$', exp_id)\n    if m:\n        return 'perdof', parse_norm(m.group(1)), int(m.group(2))\n    \n    return None\n\n# Process all object experiments\nresults = []\nfor exp_id in sorted(experiments.keys()):\n    if 'object' not in exp_id:\n        continue\n    parsed = parse_experiment(exp_id)\n    if parsed is None:\n        continue\n    method, norm, seed = parsed\n    \n    exp = experiments[exp_id]\n    status = exp.get('status', None)\n    metrics = exp.get('metrics', {}) or {}\n    overall_sr = metrics.get('overall_sr', None)\n    \n    # Check for progress info\n    progress_info = None\n    if exp.get('progress'):\n        progress_info = str(exp['progress'])\n    elif exp.get('progress_info'):\n        progress_info = str(exp['progress_info'])\n    # Also check spec for progress-like info\n    if status == 'RUNNING' and not progress_info:\n        # Maybe check latest log snippet\n        if exp.get('last_check'):\n            progress_info = str(exp['last_check'])\n    \n    results.append({\n        'exp_id': exp_id,\n        'method': method,\n        'norm': norm,\n        'seed': seed,\n        'status': status,\n        'overall_sr': overall_sr,\n        'progress_info': progress_info,\n    })\n\n# Sort by method, norm, seed\ndef sort_key(x):\n    method_order = {'obs_only': 0, 'perdof': 1, 'argmin': 2, 'scalar': 3, 'vla_mean': 4, 'vla_only': 5}\n    return (method_order.get(x['method'], 99), x['norm'] if x['norm'] is not None else -1, x['seed'] if x['seed'] is not None else -1, x['exp_id'])\n\nresults.sort(key=sort_key)\n\nprint(f\"# Found {len(results)} matching experiments\\n\")\npprint.pprint(results)\nEOF",
  "description": "Parse all object benchmark magnitude sweep experiments with broader matching",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_017jeRjGwGz5FwezgA7fQo6P",
  "session_id": "17ac476a-dce3-448f-b7ca-396cbd486cca",
  "uuid": "526f8b4d-c564-4e42-9a8e-901022a5f6f7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Bkyz2CVApdcfmkw6qUbzD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1329,
      "cache_read_input_tokens": 20514,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1329,
        "ephemeral_1h_input_tokens": 0
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

_source line 30 · 2026-05-16T22:15:55.139Z_

<details><summary>↩ Tool result · `toolu_01KdXpPECkTr7pPLGBbpoky3`</summary>

```text
# Found 61 matching experiments

[{'exp_id': 'eval-obs-only-object-seed43',
  'method': 'obs_only',
  'norm': None,
  'overall_sr': None,
  'progress_info': None,
  'seed': 43,
  'status': 'DONE'},
 {'exp_id': 'eval-mag-obsonly-norm003-object',
  'method': 'obs_only',
  'norm': 0.03,
  'overall_sr': 0.16,
  'progress_info': None,
  'seed': None,
  'status': 'DONE'},
 {'exp_id': 'eval-mag-obsonly-norm005-object',
  'method': 'obs_only',
  'norm': 0.05,
  'overall_sr': 0.13,
  'progress_info': None,
  'seed': None,
  'status': 'DONE'},
 {'exp_id': 'eval-obs-only-object-norm01-seed44',
  'method': 'obs_only',
  'norm': 0.1,
  'overall_sr': 0.16,
  'progress_info': None,
  'seed': 44,
  'status': 'DONE'},
 {'exp_id': 'eval-obs-only-object-norm01-seed45',
  'method': 'obs_only',
  'norm': 0.1,
  'overall_sr': None,
  'progress_info': None,
  'seed': 45,
  'status': 'RUNNING'},
 {'exp_id': 'eval-mag-obsonly-norm02-object',
  'method': 'obs_only',
  'norm': 0.2,
  'overall_sr': None,
  'progress_info': None,
  'seed': None,
  'status': 'DONE'},
 {'exp_id': 'eval-obs-only-object-norm02-seed43',
  'method': 'obs_only',
  'norm': 0.2,
  'overall_sr': None,
  'progress_info': None,
  'seed': 43,
  'status': 'DONE'},
 {'exp_id': 'eval-obs-only-object-norm02-seed43-r2',
  'method': 'obs_only',
  'norm': 0.2,
  'overall_sr': 0.16,
  'progress_info': None,
  'seed': 43,
  'status': 'DONE'},
 {'exp_id': 'eval-obs-only-object-norm02-seed44',
  'method': 'obs_only',
  'norm': 0.2,
  'overall_sr': None,
  'progress_info': None,
  'seed': 44,
  'status': 'DONE'},
 {'exp_id': 'eval-obs-only-object-norm02-seed44-r2',
  'method': 'obs_only',
  'norm': 0.2,
  'overall_sr': 0.16,
  'progress_info': None,
  'seed': 44,
  'status': 'DONE'},
 {'exp_id': 'eval-obs-only-object-norm02-seed44-r3',
  'method': 'obs_only',
  'norm': 0.2,
  'overall_sr': None,
  'progress_info': None,
  'seed': 44,
  'status': 'DONE'},
 {'exp_id': 'eval-obs-only-object-norm02-seed44-r4',
  'method': 'obs_only',
  'norm': 0.2,
  'overall_sr': None,
  'progress_info': None,
  'seed': 44,
  'status': 'DONE'},
 {'exp_id': 'eval-obs-only-object-norm02-seed45',
  'method': 'obs_only',
  'norm': 0.2,
  'overall_sr': 0.16,
  'progress_info': None,
  'seed': 45,
  'status': 'DONE'},
 {'exp_id': 'eval-obs-only-object-norm02-seed46',
  'method': 'obs_only',
  'norm': 0.2,
  'overall_sr': None,
  'progress_info': None,
  'seed': 46,
  'status': 'RUNNING'},
 {'exp_id': 'eval-obs-only-object-norm02-seed47',
  'method': 'obs_only',
  'norm': 0.2,
  'overall_sr': None,
  'progress_info': None,
  'seed': 47,
  'status': 'RUNNING'},
 {'exp_id': 'eval-mag-obsonly-norm03-object',
  'method': 'obs_only',
  'norm': 0.3,
  'overall_sr': 0.19,
  'progress_info': None,
  'seed': None,
  'status': 'DONE'},
 {'exp_id': 'eval-obs-only-object-norm03-seed44',
  'method': 'obs_only',
  'norm': 0.3,
  'overall_sr': 0.18,
  'progress_info': None,
  'seed': 44,
  'status': 'DONE'},
 {'exp_id': 'eval-obs-only-object-norm03-seed45',
  'method': 'obs_only',
  'norm': 0.3,
  'overall_sr': None,
  'progress_info': None,
  'seed': 45,
  'status': 'DONE'},
 {'exp_id': 'eval-obs-only-object-norm03-seed45-r2',
  'method': 'obs_only',
  'norm': 0.3,
  'overall_sr': None,
  'progress_info': None,
  'seed': 45,
  'status': 'RUNNING'},
 {'exp_id': 'eval-obs-only-object-default-seed44',
  'method': 'obs_only',
  'norm': 1.42,
  'overall_sr': 0.16,
  'progress_info': None,
  'seed': 44,
  'status': 'DONE'},
 {'exp_id': 'eval-obs-only-object-default-seed45',
  'method': 'obs_only',
  'norm': 1.42,
  'overall_sr': None,
  'progress_info': None,
  'seed': 45,
  'status': 'RUNNING'},
 {'exp_id': 'eval-perdof-object-seed43',
  'method': 'perdof',
  'norm': None,
  'overall_sr': None,
  'progress_info': None,
  'seed': 43,
  'status': 'DONE'},
 {'exp_id': 'eval-perdof-object-seed44',
  'method': 'perdof',
  'norm': None,
  'overall_sr': 0.08,
  'progress_info': None,
  'seed': 44,
  'status': 'DONE'},
 {'exp_id': 'eval-mag-perdof-norm003-object',
  'method': 'perdof',
  'norm': 0.03,
  'overall_sr': 0.14,
  'progress_info': None,
  'seed': None,
  'status': 'DONE'},
 {'exp_id': 'eval-mag-perdof-norm005-object',
  'method': 'perdof',
  'norm': 0.05,
  'overall_sr': 0.14,
  'progress_info': None,
  'seed': None,
  'status': 'DONE'},
 {'exp_id': 'eval-perdof-object-norm01-seed44',
  'method': 'perdof',
  'norm': 0.1,
  'overall_sr': None,
  'progress_info': None,
  'seed': 44,
  'status': 'RUNNING'},
 {'exp_id': 'eval-perdof-object-norm01-seed45',
  'method': 'perdof',
  'norm': 0.1,
  'overall_sr': None,
  'progress_info': None,
  'seed': 45,
  'status': 'RUNNING'},
 {'exp_id': 'eval-mag-perdof-norm02-object',
  'method': 'perdof',
  'norm': 0.2,
  'overall_sr': 0.11,
  'progress_info': None,
  'seed': None,
  'status': 'DONE'},
 {'exp_id': 'eval-mag-perdof-norm02-seed43-object',
  'method': 'perdof',
  'norm': 0.2,
  'overall_sr': None,
  'progress_info': None,
  'seed': 43,
  'status': 'DONE'},
 {'exp_id': 'eval-mag-perdof-norm02-seed43-object-r2',
  'method': 'perdof',
  'norm': 0.2,
  'overall_sr': None,
  'progress_info': None,
  'seed': 43,
  'status': 'DONE'},
 {'exp_id': 'eval-mag-perdof-norm02-seed43-object-r3',
  'method': 'perdof',
  'norm': 0.2,
  'overall_sr': 0.09,
  'progress_info': None,
  'seed': 43,
  'status': 'DONE'},
 {'exp_id': 'eval-perdof-object-norm02-seed45',
  'method': 'perdof',
  'norm': 0.2,
  'overall_sr': None,
  'progress_info': None,
  'seed': 45,
  'status': 'RUNNING'},
 {'exp_id': 'eval-mag-perdof-norm03-object',
  'method': 'perdof',
  'norm': 0.3,
  'overall_sr': None,
  'progress_info': None,
  'seed': None,
  'status': 'DEPLOYED'},
 {'exp_id': 'eval-mag-perdof-norm03-object-r2',
  'method': 'perdof',
  'norm': 0.3,
  'overall_sr': None,
  'progress_info': None,
  'seed': None,
  'status': 'DONE'},
 {'exp_id': 'eval-mag-perdof-norm03-object-r3',
  'method': 'perdof',
  'norm': 0.3,
  'overall_sr': 0.04,
  'progress_info': None,
  'seed': None,
  'status': 'DONE'},
 {'exp_id': 'eval-mag-perdof-norm0p3-object',
  'method': 'perdof',
  'norm': 0.3,
  'overall_sr': None,
  'progress_info': None,
  'seed': None,
  'status': 'DONE'},
 {'exp_id': 'eval-mag-perdof-norm0p3-object-r2',
  'method': 'perdof',
  'norm': 0.3,
  'overall_sr': None,
  'progress_info': None,
  'seed': None,
  'status': 'DONE'},
 {'exp_id': 'eval-perdof-object-norm03-seed44',
  'method': 'perdof',
  'norm': 0.3,
  'overall_sr': None,
  'progress_info': None,
  'seed': 44,
  'status': 'RUNNING'},
 {'exp_id': 'eval-perdof-object-norm03-seed45-r2',
  'method': 'perdof',
  'norm': 0.3,
  'overall_sr': None,
  'progress_info': None,
  'seed': 45,
  'status': 'RUNNING'},
 {'exp_id': 'eval-perdof-object-default-seed44',
  'method': 'perdof',
  'norm': 1.42,
  'overall_sr': None,
  'progress_info': None,
  'seed': 44,
  'status': 'RUNNING'},
 {'exp_id': 'eval-perdof-object-default-seed45',
  'method': 'perdof',
  'norm': 1.42,
  'overall_sr': None,
  'progress_info': None,
  'seed': 45,
  'status': 'RUNNING'},
 {'exp_id': 'eval-argmin-object-seed43',
  'method': 'argmin',
  'norm': None,
  'overall_sr': None,
  'progress_info': None,
  'seed': 43,
  'status': 'DONE'},
 {'exp_id': 'eval-argmin-object-seed44',
  'method': 'argmin',
  'norm': None,
  'overall_sr': None,
  'progress_info': None,
  'seed': 44,
  'status': 'DONE'},
 {'exp_id': 'eval-argmin-object-seed44-r2',
  'method': 'argmin',
  'norm': None,
  'overall_sr': 0.13,
  'progress_info': None,
  'seed': 44,
  'status': 'DONE'},
 {'exp_id': 'eval-argmin-object-seed44-r3',
  'method': 'argmin',
  'norm': None,
  'overall_sr': None,
  'progress_info': None,
  'seed': 44,
  'status': 'DONE'},
 {'exp_id': 'eval-argmin-object-seed45',
  'method': 'argmin',
  'norm': None,
  'overall_sr': None,
  'progress_info': None,
  'seed': 45,
  'status': 'RUNNING'},
 {'exp_id': 'eval-argmin-object-seed46',
  'method': 'argmin',
  'norm': None,
  'overall_sr': None,
  'progress_info': None,
  'seed': 46,
  'status': 'RUNNING'},
 {'exp_id': 'eval-argmin-object-seed47',
  'method': 'argmin',
  'norm': None,
  'overall_sr': None,
  'progress_info': None,
  'seed': 47,
  'status': 'RUNNING'},
 {'exp_id': 'eval-scalar-object-seed43',
  'method': 'scalar',
  'norm': None,
  'overall_sr': None,
  'progress_info': None,
  'seed': 43,
  'status': 'DONE'},
 {'exp_id': 'eval-scalar-object-seed44',
  'method': 'scalar',
  'norm': None,
  'overall_sr': None,
  'progress_info': None,
  'seed': 44,
  'status': 'DONE'},
 {'exp_id': 'eval-scalar-object-seed44-r2',
  'method': 'scalar',
  'norm': None,
  'overall_sr': 0.06,
  'progress_info': None,
  'seed': 44,
  'status': 'DONE'},
 {'exp_id': 'eval-scalar-object-seed45',
  'method': 'scalar',
  'norm': None,
  'overall_sr': None,
  'progress_info': None,
  'seed': 45,
  'status': 'RUNNING'},
 {'exp_id': 'eval-vla-mean-object',
  'method': 'vla_mean',
  'norm': None,
  'overall_sr': 12,
  'progress_info': None,
  'seed': None,
  'status': 'DONE'},
 {'exp_id': 'eval-vla-mean-object-seed43',
  'method': 'vla_mean',
  'norm': None,
  'overall_sr': 0.15,
  'progress_info': None,
  'seed': 43,
  'status': 'DONE'},
 {'exp_id': 'eval-vla-mean-object-seed44',
  'method': 'vla_mean',
  'norm': None,
  'overall_sr': 0.1,
  'progress_info': None,
  'seed': 44,
  'status': 'DONE'},
 {'exp_id': 'eval-vla-mean-object-seed45',
  'method': 'vla_mean',
  'norm': None,
  'overall_sr': None,
  'progress_info': None,
  'seed': 45,
  'status': 'RUNNING'},
 {'exp_id': 'eval-vla-only-object',
  'method': 'vla_only',
  'norm': None,
  'overall_sr': 0.12,
  'progress_info': None,
  'seed': None,
  'status': 'DONE'},
 {'exp_id': 'eval-vla-only-object-seed43',
  'method': 'vla_only',
  'norm': None,
  'overall_sr': 0.12,
  'progress_info': None,
  'seed': 43,
  'status': 'DONE'},
 {'exp_id': 'eval-vla-only-object-seed44',
  'method': 'vla_only',
  'norm': None,
  'overall_sr': None,
  'progress_info': None,
  'seed': 44,
  'status': 'DONE'},
 {'exp_id': 'eval-vla-only-object-seed44-r2',
  'method': 'vla_only',
  'norm': None,
  'overall_sr': 0.1,
  'progress_info': None,
  'seed': 44,
  'status': 'DONE'},
 {'exp_id': 'eval-vla-only-object-seed45',
  'method': 'vla_only',
  'norm': None,
  'overall_sr': 0.09,
  'progress_info': None,
  'seed': 45,
  'status': 'DONE'}]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_017jeRjGwGz5FwezgA7fQo6P",
  "session_id": "17ac476a-dce3-448f-b7ca-396cbd486cca",
  "uuid": "7897860c-b031-4ad2-955f-869326648143"
}
```

</details>

---

### System

_source line 31_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a58b6d9515d921b8d",
  "tool_use_id": "toolu_017jeRjGwGz5FwezgA7fQo6P",
  "description": "Running Check DONE experiments with missing overall_sr for alternative metric storage",
  "usage": {
    "total_tokens": 30168,
    "tool_uses": 7,
    "duration_ms": 96001
  },
  "last_tool_name": "Bash",
  "uuid": "c2e7ad10-1b4a-409c-93a5-87bddb9cbd11",
  "session_id": "17ac476a-dce3-448f-b7ca-396cbd486cca"
}
```

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — Bash · `toolu_01PdGvrU8o6Jdzqge3WajLgZ`</summary>

```json
{
  "command": "python3 << 'EOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/17ac476a-dce3-448f-b7ca-396cbd486cca/tool-results/mcp-agent-ml-research-read_registry-1778969659294.txt\"\n\nwith open(filepath, 'r') as f:\n    outer = json.loads(f.read())\n\nregistry = json.loads(outer['result'])\nexperiments = registry['data']['experiments']\n\n# Check a few DONE experiments with no overall_sr to see what metrics they have\ncheck_ids = [\n    'eval-obs-only-object-seed43',\n    'eval-obs-only-object-norm02-seed43',\n    'eval-obs-only-object-norm02-seed44',\n    'eval-argmin-object-seed43',\n    'eval-argmin-object-seed44',\n    'eval-scalar-object-seed43',\n    'eval-scalar-object-seed44',\n]\n\nfor eid in check_ids:\n    if eid in experiments:\n        exp = experiments[eid]\n        print(f\"\\n=== {eid} (status={exp.get('status')}) ===\")\n        print(f\"  metrics: {exp.get('metrics')}\")\n        # Check if there's a results field\n        if 'results' in exp:\n            print(f\"  results keys: {list(exp['results'].keys()) if isinstance(exp['results'], dict) else exp['results']}\")\n        if 'output' in exp:\n            print(f\"  output: {str(exp['output'])[:200]}\")\n        if 'notes' in exp:\n            print(f\"  notes: {exp['notes'][:200]}\")\nEOF",
  "description": "Check DONE experiments with missing overall_sr for alternative metric storage"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_017jeRjGwGz5FwezgA7fQo6P",
  "session_id": "17ac476a-dce3-448f-b7ca-396cbd486cca",
  "uuid": "2553f268-2486-49c5-99f7-872df907e901",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012hqFzSPri4FmbhXq3m9sXc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8003,
      "cache_read_input_tokens": 21843,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8003,
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

_source line 33 · 2026-05-16T22:16:07.920Z_

<details><summary>↩ Tool result · `toolu_01PdGvrU8o6Jdzqge3WajLgZ`</summary>

```text
=== eval-obs-only-object-seed43 (status=DONE) ===
  metrics: {'overall_success_rate': 0.12, 'tasks_done': 10, 'tasks_total': 10, 'per_task': {'alphabet_soup': 0, 'cream_cheese': 0.1, 'salad_dressing': 0.1, 'bbq_sauce': 0.3, 'ketchup': 0, 'tomato_sauce': 0, 'butter': 0, 'milk': 0.1, 'chocolate_pudding': 0.4, 'orange_juice': 0.2}, 'vs_argmin_seed43': {'obs_only': 12, 'argmin': 17, 'diff': -5}, 'fisher_pooled': {'obs_only_total': '31/200', 'argmin_total': '29/200', 'pooled_obs_only_sr': 0.155, 'pooled_argmin_sr': 0.145, 'pooled_delta': 0.01, 'odds_ratio': 1.08, 'p_value_one_sided': 0.4444, 'p_value_two_sided': 0.8888}, 'source': 'json_file_verified_by_worker'}

=== eval-obs-only-object-norm02-seed43 (status=DONE) ===
  metrics: {'pid': 118214, 'gpu': 3, 'process_status': 'alive', 'log_file': 'logs/eval_object_obs_only_norm02_seed43.log'}

=== eval-obs-only-object-norm02-seed44 (status=DONE) ===
  metrics: None

=== eval-argmin-object-seed43 (status=DONE) ===
  metrics: {'overall_success_rate': 0.17, 'total_successes': 17, 'total_trials': 100, 'per_task': {'alphabet_soup': 0, 'cream_cheese': 0, 'salad_dressing': 0.2, 'bbq_sauce': 0.2, 'ketchup': 0.1, 'tomato_sauce': 0.1, 'butter': 0.2, 'milk': 0.3, 'chocolate_pudding': 0.4, 'orange_juice': 0.2}}

=== eval-argmin-object-seed44 (status=DONE) ===
  metrics: None

=== eval-scalar-object-seed43 (status=DONE) ===
  metrics: {'tasks_done': 10, 'tasks_total': 10, 'avg_sr': 10, 'per_task_sr': {'pick_up_the_alphabet_soup_and_place_it_in_the_basket': 0, 'pick_up_the_cream_cheese_and_place_it_in_the_basket': 0, 'pick_up_the_salad_dressing_and_place_it_in_the_basket': 0, 'pick_up_the_bbq_sauce_and_place_it_in_the_basket': 30, 'pick_up_the_ketchup_and_place_it_in_the_basket': 0, 'pick_up_the_tomato_sauce_and_place_it_in_the_basket': 0, 'pick_up_the_butter_and_place_it_in_the_basket': 0, 'pick_up_the_milk_and_place_it_in_the_basket': 10, 'pick_up_the_chocolate_pudding_and_place_it_in_the_basket': 30, 'pick_up_the_orange_juice_and_place_it_in_the_basket': 30}}

=== eval-scalar-object-seed44 (status=DONE) ===
  metrics: None
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_017jeRjGwGz5FwezgA7fQo6P",
  "session_id": "17ac476a-dce3-448f-b7ca-396cbd486cca",
  "uuid": "a5faafbf-aaa2-41c6-952d-8797d658741a"
}
```

</details>

---

### System

_source line 34_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a58b6d9515d921b8d",
  "tool_use_id": "toolu_017jeRjGwGz5FwezgA7fQo6P",
  "description": "Running Final extraction with normalized overall_sr across all metric key variants",
  "usage": {
    "total_tokens": 31728,
    "tool_uses": 8,
    "duration_ms": 131938
  },
  "last_tool_name": "Bash",
  "uuid": "b55b14c3-40f1-48aa-8ac7-62075c65d9fc",
  "session_id": "17ac476a-dce3-448f-b7ca-396cbd486cca"
}
```

---

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — Bash · `toolu_01DbvDHppodQ39vTPHLT6uSb`</summary>

```json
{
  "command": "python3 << 'EOF'\nimport json\nimport re\nimport pprint\n\nfilepath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/17ac476a-dce3-448f-b7ca-396cbd486cca/tool-results/mcp-agent-ml-research-read_registry-1778969659294.txt\"\n\nwith open(filepath, 'r') as f:\n    outer = json.loads(f.read())\n\nregistry = json.loads(outer['result'])\nexperiments = registry['data']['experiments']\n\nnorm_map = {'02': 0.2, '01': 0.1, '005': 0.05, '003': 0.03, '03': 0.3, '0p3': 0.3}\n\ndef parse_norm(norm_str):\n    if norm_str in norm_map:\n        return norm_map[norm_str]\n    if 'p' in norm_str:\n        return float(norm_str.replace('p', '.'))\n    return float('0.' + norm_str)\n\ndef parse_experiment(exp_id):\n    \"\"\"Returns (method, norm, seed) or None if no match\"\"\"\n    m = re.match(r'^eval-obs-only-object-norm(\\d+p?\\d*)-seed(\\d+)(-r\\d+)?$', exp_id)\n    if m: return 'obs_only', parse_norm(m.group(1)), int(m.group(2))\n    m = re.match(r'^eval-obs-only-object-default-seed(\\d+)(-r\\d+)?$', exp_id)\n    if m: return 'obs_only', 1.42, int(m.group(1))\n    m = re.match(r'^eval-obs-only-object-seed(\\d+)(-r\\d+)?$', exp_id)\n    if m: return 'obs_only', None, int(m.group(1))\n    m = re.match(r'^eval-perdof-object-norm(\\d+p?\\d*)-seed(\\d+)(-r\\d+)?$', exp_id)\n    if m: return 'perdof', parse_norm(m.group(1)), int(m.group(2))\n    m = re.match(r'^eval-perdof-object-default-seed(\\d+)(-r\\d+)?$', exp_id)\n    if m: return 'perdof', 1.42, int(m.group(1))\n    m = re.match(r'^eval-perdof-object-seed(\\d+)(-r\\d+)?$', exp_id)\n    if m: return 'perdof', None, int(m.group(1))\n    m = re.match(r'^eval-argmin-object-seed(\\d+)(-r\\d+)?$', exp_id)\n    if m: return 'argmin', None, int(m.group(1))\n    m = re.match(r'^eval-scalar-object-seed(\\d+)(-r\\d+)?$', exp_id)\n    if m: return 'scalar', None, int(m.group(1))\n    m = re.match(r'^eval-vla-mean-object-seed(\\d+)(-r\\d+)?$', exp_id)\n    if m: return 'vla_mean', None, int(m.group(1))\n    m = re.match(r'^eval-vla-mean-object(-r\\d+)?$', exp_id)\n    if m: return 'vla_mean', None, None\n    m = re.match(r'^eval-vla-only-object-seed(\\d+)(-r\\d+)?$', exp_id)\n    if m: return 'vla_only', None, int(m.group(1))\n    m = re.match(r'^eval-vla-only-object(-r\\d+)?$', exp_id)\n    if m: return 'vla_only', None, None\n    m = re.match(r'^eval-mag-obsonly-norm(\\d+p?\\d*)-object(-r\\d+)?$', exp_id)\n    if m: return 'obs_only', parse_norm(m.group(1)), None\n    m = re.match(r'^eval-mag-obsonly-norm(\\d+p?\\d*)-seed(\\d+)-object(-r\\d+)?$', exp_id)\n    if m: return 'obs_only', parse_norm(m.group(1)), int(m.group(2))\n    m = re.match(r'^eval-mag-perdof-norm(\\d+p?\\d*)-object(-r\\d+)?$', exp_id)\n    if m: return 'perdof', parse_norm(m.group(1)), None\n    m = re.match(r'^eval-mag-perdof-norm(\\d+p?\\d*)-seed(\\d+)-object(-r\\d+)?$', exp_id)\n    if m: return 'perdof', parse_norm(m.group(1)), int(m.group(2))\n    return None\n\ndef extract_overall_sr(metrics):\n    \"\"\"Extract overall success rate, normalizing to 0-1 scale\"\"\"\n    if not metrics or not isinstance(metrics, dict):\n        return None\n    # Try different key names\n    sr = metrics.get('overall_sr')\n    if sr is None:\n        sr = metrics.get('overall_success_rate')\n    if sr is None:\n        sr = metrics.get('avg_sr')\n    if sr is None:\n        # Try computing from total_successes/total_trials\n        succ = metrics.get('total_successes')\n        trials = metrics.get('total_trials')\n        if succ is not None and trials is not None and trials > 0:\n            sr = succ / trials\n    if sr is None:\n        return None\n    # Normalize: if > 1, assume percentage scale (0-100) -> convert to 0-1\n    if isinstance(sr, (int, float)) and sr > 1:\n        sr = sr / 100.0\n    return round(sr, 4) if sr is not None else None\n\n# Process all object experiments\nresults = []\nfor exp_id in sorted(experiments.keys()):\n    if 'object' not in exp_id:\n        continue\n    parsed = parse_experiment(exp_id)\n    if parsed is None:\n        continue\n    method, norm, seed = parsed\n    \n    exp = experiments[exp_id]\n    status = exp.get('status', None)\n    metrics = exp.get('metrics', {}) or {}\n    overall_sr = extract_overall_sr(metrics)\n    \n    # Progress info\n    progress_info = None\n    if exp.get('progress'):\n        progress_info = str(exp['progress'])\n    elif exp.get('progress_info'):\n        progress_info = str(exp['progress_info'])\n    \n    results.append({\n        'exp_id': exp_id,\n        'method': method,\n        'norm': norm,\n        'seed': seed,\n        'status': status,\n        'overall_sr': overall_sr,\n        'progress_info': progress_info,\n    })\n\n# Sort\ndef sort_key(x):\n    method_order = {'obs_only': 0, 'perdof': 1, 'argmin': 2, 'scalar': 3, 'vla_mean': 4, 'vla_only': 5}\n    return (method_order.get(x['method'], 99), x['norm'] if x['norm'] is not None else -1, x['seed'] if x['seed'] is not None else -1, x['exp_id'])\n\nresults.sort(key=sort_key)\n\nprint(f\"# Found {len(results)} matching experiments\")\nprint(f\"# Status breakdown: DONE={sum(1 for r in results if r['status']=='DONE')}, RUNNING={sum(1 for r in results if r['status']=='RUNNING')}, other={sum(1 for r in results if r['status'] not in ('DONE','RUNNING'))}\")\nprint(f\"# With overall_sr: {sum(1 for r in results if r['overall_sr'] is not None)}\")\nprint()\nprint(\"results = \\\\\")\npprint.pprint(results)\nEOF",
  "description": "Final extraction with normalized overall_sr across all metric key variants",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_017jeRjGwGz5FwezgA7fQo6P",
  "session_id": "17ac476a-dce3-448f-b7ca-396cbd486cca",
  "uuid": "eabf900f-52fe-4829-b52b-99cf57d7a84e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018zByrBmBKWjD9VW7oXFyaW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1558,
      "cache_read_input_tokens": 29846,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1558,
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

_source line 36 · 2026-05-16T22:16:43.932Z_

<details><summary>↩ Tool result · `toolu_01DbvDHppodQ39vTPHLT6uSb`</summary>

```text
# Found 61 matching experiments
# Status breakdown: DONE=43, RUNNING=17, other=1
# With overall_sr: 28

results = \
[{'exp_id': 'eval-obs-only-object-seed43',
  'method': 'obs_only',
  'norm': None,
  'overall_sr': 0.12,
  'progress_info': None,
  'seed': 43,
  'status': 'DONE'},
 {'exp_id': 'eval-mag-obsonly-norm003-object',
  'method': 'obs_only',
  'norm': 0.03,
  'overall_sr': 0.16,
  'progress_info': None,
  'seed': None,
  'status': 'DONE'},
 {'exp_id': 'eval-mag-obsonly-norm005-object',
  'method': 'obs_only',
  'norm': 0.05,
  'overall_sr': 0.13,
  'progress_info': None,
  'seed': None,
  'status': 'DONE'},
 {'exp_id': 'eval-obs-only-object-norm01-seed44',
  'method': 'obs_only',
  'norm': 0.1,
  'overall_sr': 0.16,
  'progress_info': None,
  'seed': 44,
  'status': 'DONE'},
 {'exp_id': 'eval-obs-only-object-norm01-seed45',
  'method': 'obs_only',
  'norm': 0.1,
  'overall_sr': None,
  'progress_info': None,
  'seed': 45,
  'status': 'RUNNING'},
 {'exp_id': 'eval-mag-obsonly-norm02-object',
  'method': 'obs_only',
  'norm': 0.2,
  'overall_sr': None,
  'progress_info': None,
  'seed': None,
  'status': 'DONE'},
 {'exp_id': 'eval-obs-only-object-norm02-seed43',
  'method': 'obs_only',
  'norm': 0.2,
  'overall_sr': None,
  'progress_info': None,
  'seed': 43,
  'status': 'DONE'},
 {'exp_id': 'eval-obs-only-object-norm02-seed43-r2',
  'method': 'obs_only',
  'norm': 0.2,
  'overall_sr': 0.16,
  'progress_info': None,
  'seed': 43,
  'status': 'DONE'},
 {'exp_id': 'eval-obs-only-object-norm02-seed44',
  'method': 'obs_only',
  'norm': 0.2,
  'overall_sr': None,
  'progress_info': None,
  'seed': 44,
  'status': 'DONE'},
 {'exp_id': 'eval-obs-only-object-norm02-seed44-r2',
  'method': 'obs_only',
  'norm': 0.2,
  'overall_sr': 0.16,
  'progress_info': None,
  'seed': 44,
  'status': 'DONE'},
 {'exp_id': 'eval-obs-only-object-norm02-seed44-r3',
  'method': 'obs_only',
  'norm': 0.2,
  'overall_sr': None,
  'progress_info': None,
  'seed': 44,
  'status': 'DONE'},
 {'exp_id': 'eval-obs-only-object-norm02-seed44-r4',
  'method': 'obs_only',
  'norm': 0.2,
  'overall_sr': None,
  'progress_info': None,
  'seed': 44,
  'status': 'DONE'},
 {'exp_id': 'eval-obs-only-object-norm02-seed45',
  'method': 'obs_only',
  'norm': 0.2,
  'overall_sr': 0.16,
  'progress_info': None,
  'seed': 45,
  'status': 'DONE'},
 {'exp_id': 'eval-obs-only-object-norm02-seed46',
  'method': 'obs_only',
  'norm': 0.2,
  'overall_sr': None,
  'progress_info': None,
  'seed': 46,
  'status': 'RUNNING'},
 {'exp_id': 'eval-obs-only-object-norm02-seed47',
  'method': 'obs_only',
  'norm': 0.2,
  'overall_sr': None,
  'progress_info': None,
  'seed': 47,
  'status': 'RUNNING'},
 {'exp_id': 'eval-mag-obsonly-norm03-object',
  'method': 'obs_only',
  'norm': 0.3,
  'overall_sr': 0.19,
  'progress_info': None,
  'seed': None,
  'status': 'DONE'},
 {'exp_id': 'eval-obs-only-object-norm03-seed44',
  'method': 'obs_only',
  'norm': 0.3,
  'overall_sr': 0.18,
  'progress_info': None,
  'seed': 44,
  'status': 'DONE'},
 {'exp_id': 'eval-obs-only-object-norm03-seed45',
  'method': 'obs_only',
  'norm': 0.3,
  'overall_sr': None,
  'progress_info': None,
  'seed': 45,
  'status': 'DONE'},
 {'exp_id': 'eval-obs-only-object-norm03-seed45-r2',
  'method': 'obs_only',
  'norm': 0.3,
  'overall_sr': None,
  'progress_info': None,
  'seed': 45,
  'status': 'RUNNING'},
 {'exp_id': 'eval-obs-only-object-default-seed44',
  'method': 'obs_only',
  'norm': 1.42,
  'overall_sr': 0.16,
  'progress_info': None,
  'seed': 44,
  'status': 'DONE'},
 {'exp_id': 'eval-obs-only-object-default-seed45',
  'method': 'obs_only',
  'norm': 1.42,
  'overall_sr': None,
  'progress_info': None,
  'seed': 45,
  'status': 'RUNNING'},
 {'exp_id': 'eval-perdof-object-seed43',
  'method': 'perdof',
  'norm': None,
  'overall_sr': 0.12,
  'progress_info': None,
  'seed': 43,
  'status': 'DONE'},
 {'exp_id': 'eval-perdof-object-seed44',
  'method': 'perdof',
  'norm': None,
  'overall_sr': 0.08,
  'progress_info': None,
  'seed': 44,
  'status': 'DONE'},
 {'exp_id': 'eval-mag-perdof-norm003-object',
  'method': 'perdof',
  'norm': 0.03,
  'overall_sr': 0.14,
  'progress_info': None,
  'seed': None,
  'status': 'DONE'},
 {'exp_id': 'eval-mag-perdof-norm005-object',
  'method': 'perdof',
  'norm': 0.05,
  'overall_sr': 0.14,
  'progress_info': None,
  'seed': None,
  'status': 'DONE'},
 {'exp_id': 'eval-perdof-object-norm01-seed44',
  'method': 'perdof',
  'norm': 0.1,
  'overall_sr': None,
  'progress_info': None,
  'seed': 44,
  'status': 'RUNNING'},
 {'exp_id': 'eval-perdof-object-norm01-seed45',
  'method': 'perdof',
  'norm': 0.1,
  'overall_sr': None,
  'progress_info': None,
  'seed': 45,
  'status': 'RUNNING'},
 {'exp_id': 'eval-mag-perdof-norm02-object',
  'method': 'perdof',
  'norm': 0.2,
  'overall_sr': 0.11,
  'progress_info': None,
  'seed': None,
  'status': 'DONE'},
 {'exp_id': 'eval-mag-perdof-norm02-seed43-object',
  'method': 'perdof',
  'norm': 0.2,
  'overall_sr': None,
  'progress_info': None,
  'seed': 43,
  'status': 'DONE'},
 {'exp_id': 'eval-mag-perdof-norm02-seed43-object-r2',
  'method': 'perdof',
  'norm': 0.2,
  'overall_sr': None,
  'progress_info': None,
  'seed': 43,
  'status': 'DONE'},
 {'exp_id': 'eval-mag-perdof-norm02-seed43-object-r3',
  'method': 'perdof',
  'norm': 0.2,
  'overall_sr': 0.09,
  'progress_info': None,
  'seed': 43,
  'status': 'DONE'},
 {'exp_id': 'eval-perdof-object-norm02-seed45',
  'method': 'perdof',
  'norm': 0.2,
  'overall_sr': None,
  'progress_info': None,
  'seed': 45,
  'status': 'RUNNING'},
 {'exp_id': 'eval-mag-perdof-norm03-object',
  'method': 'perdof',
  'norm': 0.3,
  'overall_sr': None,
  'progress_info': None,
  'seed': None,
  'status': 'DEPLOYED'},
 {'exp_id': 'eval-mag-perdof-norm03-object-r2',
  'method': 'perdof',
  'norm': 0.3,
  'overall_sr': None,
  'progress_info': None,
  'seed': None,
  'status': 'DONE'},
 {'exp_id': 'eval-mag-perdof-norm03-object-r3',
  'method': 'perdof',
  'norm': 0.3,
  'overall_sr': 0.04,
  'progress_info': None,
  'seed': None,
  'status': 'DONE'},
 {'exp_id': 'eval-mag-perdof-norm0p3-object',
  'method': 'perdof',
  'norm': 0.3,
  'overall_sr': None,
  'progress_info': None,
  'seed': None,
  'status': 'DONE'},
 {'exp_id': 'eval-mag-perdof-norm0p3-object-r2',
  'method': 'perdof',
  'norm': 0.3,
  'overall_sr': None,
  'progress_info': None,
  'seed': None,
  'status': 'DONE'},
 {'exp_id': 'eval-perdof-object-norm03-seed44',
  'method': 'perdof',
  'norm': 0.3,
  'overall_sr': None,
  'progress_info': None,
  'seed': 44,
  'status': 'RUNNING'},
 {'exp_id': 'eval-perdof-object-norm03-seed45-r2',
  'method': 'perdof',
  'norm': 0.3,
  'overall_sr': None,
  'progress_info': None,
  'seed': 45,
  'status': 'RUNNING'},
 {'exp_id': 'eval-perdof-object-default-seed44',
  'method': 'perdof',
  'norm': 1.42,
  'overall_sr': None,
  'progress_info': None,
  'seed': 44,
  'status': 'RUNNING'},
 {'exp_id': 'eval-perdof-object-default-seed45',
  'method': 'perdof',
  'norm': 1.42,
  'overall_sr': None,
  'progress_info': None,
  'seed': 45,
  'status': 'RUNNING'},
 {'exp_id': 'eval-argmin-object-seed43',
  'method': 'argmin',
  'norm': None,
  'overall_sr': 0.17,
  'progress_info': None,
  'seed': 43,
  'status': 'DONE'},
 {'exp_id': 'eval-argmin-object-seed44',
  'method': 'argmin',
  'norm': None,
  'overall_sr': None,
  'progress_info': None,
  'seed': 44,
  'status': 'DONE'},
 {'exp_id': 'eval-argmin-object-seed44-r2',
  'method': 'argmin',
  'norm': None,
  'overall_sr': 0.13,
  'progress_info': None,
  'seed': 44,
  'status': 'DONE'},
 {'exp_id': 'eval-argmin-object-seed44-r3',
  'method': 'argmin',
  'norm': None,
  'overall_sr': None,
  'progress_info': None,
  'seed': 44,
  'status': 'DONE'},
 {'exp_id': 'eval-argmin-object-seed45',
  'method': 'argmin',
  'norm': None,
  'overall_sr': None,
  'progress_info': None,
  'seed': 45,
  'status': 'RUNNING'},
 {'exp_id': 'eval-argmin-object-seed46',
  'method': 'argmin',
  'norm': None,
  'overall_sr': None,
  'progress_info': None,
  'seed': 46,
  'status': 'RUNNING'},
 {'exp_id': 'eval-argmin-object-seed47',
  'method': 'argmin',
  'norm': None,
  'overall_sr': None,
  'progress_info': None,
  'seed': 47,
  'status': 'RUNNING'},
 {'exp_id': 'eval-scalar-object-seed43',
  'method': 'scalar',
  'norm': None,
  'overall_sr': 0.1,
  'progress_info': None,
  'seed': 43,
  'status': 'DONE'},
 {'exp_id': 'eval-scalar-object-seed44',
  'method': 'scalar',
  'norm': None,
  'overall_sr': None,
  'progress_info': None,
  'seed': 44,
  'status': 'DONE'},
 {'exp_id': 'eval-scalar-object-seed44-r2',
  'method': 'scalar',
  'norm': None,
  'overall_sr': 0.06,
  'progress_info': None,
  'seed': 44,
  'status': 'DONE'},
 {'exp_id': 'eval-scalar-object-seed45',
  'method': 'scalar',
  'norm': None,
  'overall_sr': None,
  'progress_info': None,
  'seed': 45,
  'status': 'RUNNING'},
 {'exp_id': 'eval-vla-mean-object',
  'method': 'vla_mean',
  'norm': None,
  'overall_sr': 0.12,
  'progress_info': None,
  'seed': None,
  'status': 'DONE'},
 {'exp_id': 'eval-vla-mean-object-seed43',
  'method': 'vla_mean',
  'norm': None,
  'overall_sr': 0.15,
  'progress_info': None,
  'seed': 43,
  'status': 'DONE'},
 {'exp_id': 'eval-vla-mean-object-seed44',
  'method': 'vla_mean',
  'norm': None,
  'overall_sr': 0.1,
  'progress_info': None,
  'seed': 44,
  'status': 'DONE'},
 {'exp_id': 'eval-vla-mean-object-seed45',
  'method': 'vla_mean',
  'norm': None,
  'overall_sr': None,
  'progress_info': None,
  'seed': 45,
  'status': 'RUNNING'},
 {'exp_id': 'eval-vla-only-object',
  'method': 'vla_only',
  'norm': None,
  'overall_sr': 0.12,
  'progress_info': None,
  'seed': None,
  'status': 'DONE'},
 {'exp_id': 'eval-vla-only-object-seed43',
  'method': 'vla_only',
  'norm': None,
  'overall_sr': 0.12,
  'progress_info': None,
  'seed': 43,
  'status': 'DONE'},
 {'exp_id': 'eval-vla-only-object-seed44',
  'method': 'vla_only',
  'norm': None,
  'overall_sr': None,
  'progress_info': None,
  'seed': 44,
  'status': 'DONE'},
 {'exp_id': 'eval-vla-only-object-seed44-r2',
  'method': 'vla_only',
  'norm': None,
  'overall_sr': 0.1,
  'progress_info': None,
  'seed': 44,
  'status': 'DONE'},
 {'exp_id': 'eval-vla-only-object-seed45',
  'method': 'vla_only',
  'norm': None,
  'overall_sr': 0.09,
  'progress_info': None,
  'seed': 45,
  'status': 'DONE'}]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_017jeRjGwGz5FwezgA7fQo6P",
  "session_id": "17ac476a-dce3-448f-b7ca-396cbd486cca",
  "uuid": "029da623-615b-4ff9-a9ad-172eaf171967"
}
```

</details>

---

### System

_source line 37_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a58b6d9515d921b8d",
  "tool_use_id": "toolu_017jeRjGwGz5FwezgA7fQo6P",
  "status": "completed",
  "output_file": "",
  "summary": "Extract magnitude sweep data",
  "usage": {
    "total_tokens": 38789,
    "tool_uses": 8,
    "duration_ms": 176154
  },
  "uuid": "1cade60a-b668-4d1e-867b-d40da8e4f903",
  "session_id": "17ac476a-dce3-448f-b7ca-396cbd486cca"
}
```

---

### Tool result

_source line 38 · 2026-05-16T22:17:27.988Z_

<details><summary>↩ Tool result · `toolu_017jeRjGwGz5FwezgA7fQo6P`</summary>

````text
Here is the complete structured extraction. **61 experiments** matched the object benchmark magnitude sweep patterns.

```python
results = [
 {'exp_id': 'eval-obs-only-object-seed43', 'method': 'obs_only', 'norm': None, 'seed': 43, 'status': 'DONE', 'overall_sr': 0.12, 'progress_info': None},
 {'exp_id': 'eval-mag-obsonly-norm003-object', 'method': 'obs_only', 'norm': 0.03, 'seed': None, 'status': 'DONE', 'overall_sr': 0.16, 'progress_info': None},
 {'exp_id': 'eval-mag-obsonly-norm005-object', 'method': 'obs_only', 'norm': 0.05, 'seed': None, 'status': 'DONE', 'overall_sr': 0.13, 'progress_info': None},
 {'exp_id': 'eval-obs-only-object-norm01-seed44', 'method': 'obs_only', 'norm': 0.1, 'seed': 44, 'status': 'DONE', 'overall_sr': 0.16, 'progress_info': None},
 {'exp_id': 'eval-obs-only-object-norm01-seed45', 'method': 'obs_only', 'norm': 0.1, 'seed': 45, 'status': 'RUNNING', 'overall_sr': None, 'progress_info': None},
 {'exp_id': 'eval-mag-obsonly-norm02-object', 'method': 'obs_only', 'norm': 0.2, 'seed': None, 'status': 'DONE', 'overall_sr': None, 'progress_info': None},
 {'exp_id': 'eval-obs-only-object-norm02-seed43', 'method': 'obs_only', 'norm': 0.2, 'seed': 43, 'status': 'DONE', 'overall_sr': None, 'progress_info': None},
 {'exp_id': 'eval-obs-only-object-norm02-seed43-r2', 'method': 'obs_only', 'norm': 0.2, 'seed': 43, 'status': 'DONE', 'overall_sr': 0.16, 'progress_info': None},
 {'exp_id': 'eval-obs-only-object-norm02-seed44', 'method': 'obs_only', 'norm': 0.2, 'seed': 44, 'status': 'DONE', 'overall_sr': None, 'progress_info': None},
 {'exp_id': 'eval-obs-only-object-norm02-seed44-r2', 'method': 'obs_only', 'norm': 0.2, 'seed': 44, 'status': 'DONE', 'overall_sr': 0.16, 'progress_info': None},
 {'exp_id': 'eval-obs-only-object-norm02-seed44-r3', 'method': 'obs_only', 'norm': 0.2, 'seed': 44, 'status': 'DONE', 'overall_sr': None, 'progress_info': None},
 {'exp_id': 'eval-obs-only-object-norm02-seed44-r4', 'method': 'obs_only', 'norm': 0.2, 'seed': 44, 'status': 'DONE', 'overall_sr': None, 'progress_info': None},
 {'exp_id': 'eval-obs-only-object-norm02-seed45', 'method': 'obs_only', 'norm': 0.2, 'seed': 45, 'status': 'DONE', 'overall_sr': 0.16, 'progress_info': None},
 {'exp_id': 'eval-obs-only-object-norm02-seed46', 'method': 'obs_only', 'norm': 0.2, 'seed': 46, 'status': 'RUNNING', 'overall_sr': None, 'progress_info': None},
 {'exp_id': 'eval-obs-only-object-norm02-seed47', 'method': 'obs_only', 'norm': 0.2, 'seed': 47, 'status': 'RUNNING', 'overall_sr': None, 'progress_info': None},
 {'exp_id': 'eval-mag-obsonly-norm03-object', 'method': 'obs_only', 'norm': 0.3, 'seed': None, 'status': 'DONE', 'overall_sr': 0.19, 'progress_info': None},
 {'exp_id': 'eval-obs-only-object-norm03-seed44', 'method': 'obs_only', 'norm': 0.3, 'seed': 44, 'status': 'DONE', 'overall_sr': 0.18, 'progress_info': None},
 {'exp_id': 'eval-obs-only-object-norm03-seed45', 'method': 'obs_only', 'norm': 0.3, 'seed': 45, 'status': 'DONE', 'overall_sr': None, 'progress_info': None},
 {'exp_id': 'eval-obs-only-object-norm03-seed45-r2', 'method': 'obs_only', 'norm': 0.3, 'seed': 45, 'status': 'RUNNING', 'overall_sr': None, 'progress_info': None},
 {'exp_id': 'eval-obs-only-object-default-seed44', 'method': 'obs_only', 'norm': 1.42, 'seed': 44, 'status': 'DONE', 'overall_sr': 0.16, 'progress_info': None},
 {'exp_id': 'eval-obs-only-object-default-seed45', 'method': 'obs_only', 'norm': 1.42, 'seed': 45, 'status': 'RUNNING', 'overall_sr': None, 'progress_info': None},
 {'exp_id': 'eval-perdof-object-seed43', 'method': 'perdof', 'norm': None, 'seed': 43, 'status': 'DONE', 'overall_sr': 0.12, 'progress_info': None},
 {'exp_id': 'eval-perdof-object-seed44', 'method': 'perdof', 'norm': None, 'seed': 44, 'status': 'DONE', 'overall_sr': 0.08, 'progress_info': None},
 {'exp_id': 'eval-mag-perdof-norm003-object', 'method': 'perdof', 'norm': 0.03, 'seed': None, 'status': 'DONE', 'overall_sr': 0.14, 'progress_info': None},
 {'exp_id': 'eval-mag-perdof-norm005-object', 'method': 'perdof', 'norm': 0.05, 'seed': None, 'status': 'DONE', 'overall_sr': 0.14, 'progress_info': None},
 {'exp_id': 'eval-perdof-object-norm01-seed44', 'method': 'perdof', 'norm': 0.1, 'seed': 44, 'status': 'RUNNING', 'overall_sr': None, 'progress_info': None},
 {'exp_id': 'eval-perdof-object-norm01-seed45', 'method': 'perdof', 'norm': 0.1, 'seed': 45, 'status': 'RUNNING', 'overall_sr': None, 'progress_info': None},
 {'exp_id': 'eval-mag-perdof-norm02-object', 'method': 'perdof', 'norm': 0.2, 'seed': None, 'status': 'DONE', 'overall_sr': 0.11, 'progress_info': None},
 {'exp_id': 'eval-mag-perdof-norm02-seed43-object', 'method': 'perdof', 'norm': 0.2, 'seed': 43, 'status': 'DONE', 'overall_sr': None, 'progress_info': None},
 {'exp_id': 'eval-mag-perdof-norm02-seed43-object-r2', 'method': 'perdof', 'norm': 0.2, 'seed': 43, 'status': 'DONE', 'overall_sr': None, 'progress_info': None},
 {'exp_id': 'eval-mag-perdof-norm02-seed43-object-r3', 'method': 'perdof', 'norm': 0.2, 'seed': 43, 'status': 'DONE', 'overall_sr': 0.09, 'progress_info': None},
 {'exp_id': 'eval-perdof-object-norm02-seed45', 'method': 'perdof', 'norm': 0.2, 'seed': 45, 'status': 'RUNNING', 'overall_sr': None, 'progress_info': None},
 {'exp_id': 'eval-mag-perdof-norm03-object', 'method': 'perdof', 'norm': 0.3, 'seed': None, 'status': 'DEPLOYED', 'overall_sr': None, 'progress_info': None},
 {'exp_id': 'eval-mag-perdof-norm03-object-r2', 'method': 'perdof', 'norm': 0.3, 'seed': None, 'status': 'DONE', 'overall_sr': None, 'progress_info': None},
 {'exp_id': 'eval-mag-perdof-norm03-object-r3', 'method': 'perdof', 'norm': 0.3, 'seed': None, 'status': 'DONE', 'overall_sr': 0.04, 'progress_info': None},
 {'exp_id': 'eval-mag-perdof-norm0p3-object', 'method': 'perdof', 'norm': 0.3, 'seed': None, 'status': 'DONE', 'overall_sr': None, 'progress_info': None},
 {'exp_id': 'eval-mag-perdof-norm0p3-object-r2', 'method': 'perdof', 'norm': 0.3, 'seed': None, 'status': 'DONE', 'overall_sr': None, 'progress_info': None},
 {'exp_id': 'eval-perdof-object-norm03-seed44', 'method': 'perdof', 'norm': 0.3, 'seed': 44, 'status': 'RUNNING', 'overall_sr': None, 'progress_info': None},
 {'exp_id': 'eval-perdof-object-norm03-seed45-r2', 'method': 'perdof', 'norm': 0.3, 'seed': 45, 'status': 'RUNNING', 'overall_sr': None, 'progress_info': None},
 {'exp_id': 'eval-perdof-object-default-seed44', 'method': 'perdof', 'norm': 1.42, 'seed': 44, 'status': 'RUNNING', 'overall_sr': None, 'progress_info': None},
 {'exp_id': 'eval-perdof-object-default-seed45', 'method': 'perdof', 'norm': 1.42, 'seed': 45, 'status': 'RUNNING', 'overall_sr': None, 'progress_info': None},
 {'exp_id': 'eval-argmin-object-seed43', 'method': 'argmin', 'norm': None, 'seed': 43, 'status': 'DONE', 'overall_sr': 0.17, 'progress_info': None},
 {'exp_id': 'eval-argmin-object-seed44', 'method': 'argmin', 'norm': None, 'seed': 44, 'status': 'DONE', 'overall_sr': None, 'progress_info': None},
 {'exp_id': 'eval-argmin-object-seed44-r2', 'method': 'argmin', 'norm': None, 'seed': 44, 'status': 'DONE', 'overall_sr': 0.13, 'progress_info': None},
 {'exp_id': 'eval-argmin-object-seed44-r3', 'method': 'argmin', 'norm': None, 'seed': 44, 'status': 'DONE', 'overall_sr': None, 'progress_info': None},
 {'exp_id': 'eval-argmin-object-seed45', 'method': 'argmin', 'norm': None, 'seed': 45, 'status': 'RUNNING', 'overall_sr': None, 'progress_info': None},
 {'exp_id': 'eval-argmin-object-seed46', 'method': 'argmin', 'norm': None, 'seed': 46, 'status': 'RUNNING', 'overall_sr': None, 'progress_info': None},
 {'exp_id': 'eval-argmin-object-seed47', 'method': 'argmin', 'norm': None, 'seed': 47, 'status': 'RUNNING', 'overall_sr': None, 'progress_info': None},
 {'exp_id': 'eval-scalar-object-seed43', 'method': 'scalar', 'norm': None, 'seed': 43, 'status': 'DONE', 'overall_sr': 0.1, 'progress_info': None},
 {'exp_id': 'eval-scalar-object-seed44', 'method': 'scalar', 'norm': None, 'seed': 44, 'status': 'DONE', 'overall_sr': None, 'progress_info': None},
 {'exp_id': 'eval-scalar-object-seed44-r2', 'method': 'scalar', 'norm': None, 'seed': 44, 'status': 'DONE', 'overall_sr': 0.06, 'progress_info': None},
 {'exp_id': 'eval-scalar-object-seed45', 'method': 'scalar', 'norm': None, 'seed': 45, 'status': 'RUNNING', 'overall_sr': None, 'progress_info': None},
 {'exp_id': 'eval-vla-mean-object', 'method': 'vla_mean', 'norm': None, 'seed': None, 'status': 'DONE', 'overall_sr': 0.12, 'progress_info': None},
 {'exp_id': 'eval-vla-mean-object-seed43', 'method': 'vla_mean', 'norm': None, 'seed': 43, 'status': 'DONE', 'overall_sr': 0.15, 'progress_info': None},
 {'exp_id': 'eval-vla-mean-object-seed44', 'method': 'vla_mean', 'norm': None, 'seed': 44, 'status': 'DONE', 'overall_sr': 0.1, 'progress_info': None},
 {'exp_id': 'eval-vla-mean-object-seed45', 'method': 'vla_mean', 'norm': None, 'seed': 45, 'status': 'RUNNING', 'overall_sr': None, 'progress_info': None},
 {'exp_id': 'eval-vla-only-object', 'method': 'vla_only', 'norm': None, 'seed': None, 'status': 'DONE', 'overall_sr': 0.12, 'progress_info': None},
 {'exp_id': 'eval-vla-only-object-seed43', 'method': 'vla_only', 'norm': None, 'seed': 43, 'status': 'DONE', 'overall_sr': 0.12, 'progress_info': None},
 {'exp_id': 'eval-vla-only-object-seed44', 'method': 'vla_only', 'norm': None, 'seed': 44, 'status': 'DONE', 'overall_sr': None, 'progress_info': None},
 {'exp_id': 'eval-vla-only-object-seed44-r2', 'method': 'vla_only', 'norm': None, 'seed': 44, 'status': 'DONE', 'overall_sr': 0.1, 'progress_info': None},
 {'exp_id': 'eval-vla-only-object-seed45', 'method': 'vla_only', 'norm': None, 'seed': 45, 'status': 'DONE', 'overall_sr': 0.09, 'progress_info': None},
]
```

**Summary:**
- **61 total** matching experiments
- **43 DONE**, **17 RUNNING**, **1 DEPLOYED**
- **28** have `overall_sr` values (normalized to 0-1 scale; the raw registry used a mix of `overall_sr`, `overall_success_rate`, and `avg_sr` keys, some in percentage 0-100 format)
- No `progress_info` was stored in any experiment entry
- Retries (`-r2`, `-r3`, `-r4`) are included as separate entries; for each (method, norm, seed) group, typically the latest retry has metrics recorded
- The `eval-mag-*` prefix is the legacy naming convention (single-seed runs without explicit seed in name); `eval-{method}-object-norm{NN}-seed{XX}` is the newer multi-seed naming

agentId: a58b6d9515d921b8d (use SendMessage with to: 'a58b6d9515d921b8d' to continue this agent)
&lt;usage>total_tokens: 43122
tool_uses: 8
duration_ms: 176158&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "17ac476a-dce3-448f-b7ca-396cbd486cca",
  "uuid": "0811cc5b-dbad-4720-99d7-922ecd861efe",
  "tool_use_result": {
    "status": "completed",
    "prompt": "I need you to extract experiment data from a large JSON registry file and produce a structured summary.\n\nThe file is at: `/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/17ac476a-dce3-448f-b7ca-396cbd486cca/tool-results/mcp-agent-ml-research-read_registry-1778969659294.txt`\n\nThe file is JSON with schema: `{result: string}` — the `result` field is itself a JSON string that needs to be parsed.\n\n**What I need:**\n\nExtract all experiments whose `exp_id` matches the \"object benchmark\" magnitude sweep pattern. The naming conventions are:\n- `eval-obs-only-object-norm{NN}-seed{XX}` (norm02=0.2, norm01=0.1, norm005=0.05, norm003=0.03, norm03=0.3)\n- `eval-perdof-object-norm{NN}-seed{XX}`\n- `eval-argmin-object-seed{XX}`\n- `eval-scalar-object-seed{XX}`\n- `eval-vla-mean-object-seed{XX}`\n- `eval-vla-only-object-seed{XX}`\n- `eval-obs-only-object-default-seed{XX}` (norm=default≈1.42)\n- `eval-perdof-object-default-seed{XX}`\n\nFor each matching experiment, extract:\n1. `exp_id`\n2. `status` (DONE, RUNNING, FAILED, etc.)\n3. `metrics` — specifically `overall_sr` (overall success rate)\n4. Any progress info if RUNNING\n\n**Output format:**\nPrint a Python-parseable list of dicts, one per experiment, with keys: `exp_id`, `method`, `norm`, `seed`, `status`, `overall_sr`, `progress_info`\n\nWhere:\n- `method`: one of obs_only, perdof, argmin, scalar, vla_mean, vla_only\n- `norm`: float value (0.03, 0.05, 0.10, 0.20, 0.30, 1.42 for default) or None for methods without norm\n- `seed`: integer\n- `overall_sr`: float or None if not available\n- `progress_info`: string or None\n\nUse jq or python to parse the file. The file may be very large so work efficiently. Print the final structured output so I can use it.",
    "agentId": "a58b6d9515d921b8d",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is the complete structured extraction. **61 experiments** matched the object benchmark magnitude sweep patterns.\n\n```python\nresults = [\n {'exp_id': 'eval-obs-only-object-seed43', 'method': 'obs_only', 'norm': None, 'seed': 43, 'status': 'DONE', 'overall_sr': 0.12, 'progress_info': None},\n {'exp_id': 'eval-mag-obsonly-norm003-object', 'method': 'obs_only', 'norm': 0.03, 'seed': None, 'status': 'DONE', 'overall_sr': 0.16, 'progress_info': None},\n {'exp_id': 'eval-mag-obsonly-norm005-object', 'method': 'obs_only', 'norm': 0.05, 'seed': None, 'status': 'DONE', 'overall_sr': 0.13, 'progress_info': None},\n {'exp_id': 'eval-obs-only-object-norm01-seed44', 'method': 'obs_only', 'norm': 0.1, 'seed': 44, 'status': 'DONE', 'overall_sr': 0.16, 'progress_info': None},\n {'exp_id': 'eval-obs-only-object-norm01-seed45', 'method': 'obs_only', 'norm': 0.1, 'seed': 45, 'status': 'RUNNING', 'overall_sr': None, 'progress_info': None},\n {'exp_id': 'eval-mag-obsonly-norm02-object', 'method': 'obs_only', 'norm': 0.2, 'seed': None, 'status': 'DONE', 'overall_sr': None, 'progress_info': None},\n {'exp_id': 'eval-obs-only-object-norm02-seed43', 'method': 'obs_only', 'norm': 0.2, 'seed': 43, 'status': 'DONE', 'overall_sr': None, 'progress_info': None},\n {'exp_id': 'eval-obs-only-object-norm02-seed43-r2', 'method': 'obs_only', 'norm': 0.2, 'seed': 43, 'status': 'DONE', 'overall_sr': 0.16, 'progress_info': None},\n {'exp_id': 'eval-obs-only-object-norm02-seed44', 'method': 'obs_only', 'norm': 0.2, 'seed': 44, 'status': 'DONE', 'overall_sr': None, 'progress_info': None},\n {'exp_id': 'eval-obs-only-object-norm02-seed44-r2', 'method': 'obs_only', 'norm': 0.2, 'seed': 44, 'status': 'DONE', 'overall_sr': 0.16, 'progress_info': None},\n {'exp_id': 'eval-obs-only-object-norm02-seed44-r3', 'method': 'obs_only', 'norm': 0.2, 'seed': 44, 'status': 'DONE', 'overall_sr': None, 'progress_info': None},\n {'exp_id': 'eval-obs-only-object-norm02-seed44-r4', 'method': 'obs_only', 'norm': 0.2, 'seed': 44, 'status': 'DONE', 'overall_sr': None, 'progress_info': None},\n {'exp_id': 'eval-obs-only-object-norm02-seed45', 'method': 'obs_only', 'norm': 0.2, 'seed': 45, 'status': 'DONE', 'overall_sr': 0.16, 'progress_info': None},\n {'exp_id': 'eval-obs-only-object-norm02-seed46', 'method': 'obs_only', 'norm': 0.2, 'seed': 46, 'status': 'RUNNING', 'overall_sr': None, 'progress_info': None},\n {'exp_id': 'eval-obs-only-object-norm02-seed47', 'method': 'obs_only', 'norm': 0.2, 'seed': 47, 'status': 'RUNNING', 'overall_sr': None, 'progress_info': None},\n {'exp_id': 'eval-mag-obsonly-norm03-object', 'method': 'obs_only', 'norm': 0.3, 'seed': None, 'status': 'DONE', 'overall_sr': 0.19, 'progress_info': None},\n {'exp_id': 'eval-obs-only-object-norm03-seed44', 'method': 'obs_only', 'norm': 0.3, 'seed': 44, 'status': 'DONE', 'overall_sr': 0.18, 'progress_info': None},\n {'exp_id': 'eval-obs-only-object-norm03-seed45', 'method': 'obs_only', 'norm': 0.3, 'seed': 45, 'status': 'DONE', 'overall_sr': None, 'progress_info': None},\n {'exp_id': 'eval-obs-only-object-norm03-seed45-r2', 'method': 'obs_only', 'norm': 0.3, 'seed': 45, 'status': 'RUNNING', 'overall_sr': None, 'progress_info': None},\n {'exp_id': 'eval-obs-only-object-default-seed44', 'method': 'obs_only', 'norm': 1.42, 'seed': 44, 'status': 'DONE', 'overall_sr': 0.16, 'progress_info': None},\n {'exp_id': 'eval-obs-only-object-default-seed45', 'method': 'obs_only', 'norm': 1.42, 'seed': 45, 'status': 'RUNNING', 'overall_sr': None, 'progress_info': None},\n {'exp_id': 'eval-perdof-object-seed43', 'method': 'perdof', 'norm': None, 'seed': 43, 'status': 'DONE', 'overall_sr': 0.12, 'progress_info': None},\n {'exp_id': 'eval-perdof-object-seed44', 'method': 'perdof', 'norm': None, 'seed': 44, 'status': 'DONE', 'overall_sr': 0.08, 'progress_info': None},\n {'exp_id': 'eval-mag-perdof-norm003-object', 'method': 'perdof', 'norm': 0.03, 'seed': None, 'status': 'DONE', 'overall_sr': 0.14, 'progress_info': None},\n {'exp_id': 'eval-mag-perdof-norm005-object', 'method': 'perdof', 'norm': 0.05, 'seed': None, 'status': 'DONE', 'overall_sr': 0.14, 'progress_info': None},\n {'exp_id': 'eval-perdof-object-norm01-seed44', 'method': 'perdof', 'norm': 0.1, 'seed': 44, 'status': 'RUNNING', 'overall_sr': None, 'progress_info': None},\n {'exp_id': 'eval-perdof-object-norm01-seed45', 'method': 'perdof', 'norm': 0.1, 'seed': 45, 'status': 'RUNNING', 'overall_sr': None, 'progress_info': None},\n {'exp_id': 'eval-mag-perdof-norm02-object', 'method': 'perdof', 'norm': 0.2, 'seed': None, 'status': 'DONE', 'overall_sr': 0.11, 'progress_info': None},\n {'exp_id': 'eval-mag-perdof-norm02-seed43-object', 'method': 'perdof', 'norm': 0.2, 'seed': 43, 'status': 'DONE', 'overall_sr': None, 'progress_info': None},\n {'exp_id': 'eval-mag-perdof-norm02-seed43-object-r2', 'method': 'perdof', 'norm': 0.2, 'seed': 43, 'status': 'DONE', 'overall_sr': None, 'progress_info': None},\n {'exp_id': 'eval-mag-perdof-norm02-seed43-object-r3', 'method': 'perdof', 'norm': 0.2, 'seed': 43, 'status': 'DONE', 'overall_sr': 0.09, 'progress_info': None},\n {'exp_id': 'eval-perdof-object-norm02-seed45', 'method': 'perdof', 'norm': 0.2, 'seed': 45, 'status': 'RUNNING', 'overall_sr': None, 'progress_info': None},\n {'exp_id': 'eval-mag-perdof-norm03-object', 'method': 'perdof', 'norm': 0.3, 'seed': None, 'status': 'DEPLOYED', 'overall_sr': None, 'progress_info': None},\n {'exp_id': 'eval-mag-perdof-norm03-object-r2', 'method': 'perdof', 'norm': 0.3, 'seed': None, 'status': 'DONE', 'overall_sr': None, 'progress_info': None},\n {'exp_id': 'eval-mag-perdof-norm03-object-r3', 'method': 'perdof', 'norm': 0.3, 'seed': None, 'status': 'DONE', 'overall_sr': 0.04, 'progress_info': None},\n {'exp_id': 'eval-mag-perdof-norm0p3-object', 'method': 'perdof', 'norm': 0.3, 'seed': None, 'status': 'DONE', 'overall_sr': None, 'progress_info': None},\n {'exp_id': 'eval-mag-perdof-norm0p3-object-r2', 'method': 'perdof', 'norm': 0.3, 'seed': None, 'status': 'DONE', 'overall_sr': None, 'progress_info': None},\n {'exp_id': 'eval-perdof-object-norm03-seed44', 'method': 'perdof', 'norm': 0.3, 'seed': 44, 'status': 'RUNNING', 'overall_sr': None, 'progress_info': None},\n {'exp_id': 'eval-perdof-object-norm03-seed45-r2', 'method': 'perdof', 'norm': 0.3, 'seed': 45, 'status': 'RUNNING', 'overall_sr': None, 'progress_info': None},\n {'exp_id': 'eval-perdof-object-default-seed44', 'method': 'perdof', 'norm': 1.42, 'seed': 44, 'status': 'RUNNING', 'overall_sr': None, 'progress_info': None},\n {'exp_id': 'eval-perdof-object-default-seed45', 'method': 'perdof', 'norm': 1.42, 'seed': 45, 'status': 'RUNNING', 'overall_sr': None, 'progress_info': None},\n {'exp_id': 'eval-argmin-object-seed43', 'method': 'argmin', 'norm': None, 'seed': 43, 'status': 'DONE', 'overall_sr': 0.17, 'progress_info': None},\n {'exp_id': 'eval-argmin-object-seed44', 'method': 'argmin', 'norm': None, 'seed': 44, 'status': 'DONE', 'overall_sr': None, 'progress_info': None},\n {'exp_id': 'eval-argmin-object-seed44-r2', 'method': 'argmin', 'norm': None, 'seed': 44, 'status': 'DONE', 'overall_sr': 0.13, 'progress_info': None},\n {'exp_id': 'eval-argmin-object-seed44-r3', 'method': 'argmin', 'norm': None, 'seed': 44, 'status': 'DONE', 'overall_sr': None, 'progress_info': None},\n {'exp_id': 'eval-argmin-object-seed45', 'method': 'argmin', 'norm': None, 'seed': 45, 'status': 'RUNNING', 'overall_sr': None, 'progress_info': None},\n {'exp_id': 'eval-argmin-object-seed46', 'method': 'argmin', 'norm': None, 'seed': 46, 'status': 'RUNNING', 'overall_sr': None, 'progress_info': None},\n {'exp_id': 'eval-argmin-object-seed47', 'method': 'argmin', 'norm': None, 'seed': 47, 'status': 'RUNNING', 'overall_sr': None, 'progress_info': None},\n {'exp_id': 'eval-scalar-object-seed43', 'method': 'scalar', 'norm': None, 'seed': 43, 'status': 'DONE', 'overall_sr': 0.1, 'progress_info': None},\n {'exp_id': 'eval-scalar-object-seed44', 'method': 'scalar', 'norm': None, 'seed': 44, 'status': 'DONE', 'overall_sr': None, 'progress_info': None},\n {'exp_id': 'eval-scalar-object-seed44-r2', 'method': 'scalar', 'norm': None, 'seed': 44, 'status': 'DONE', 'overall_sr': 0.06, 'progress_info': None},\n {'exp_id': 'eval-scalar-object-seed45', 'method': 'scalar', 'norm': None, 'seed': 45, 'status': 'RUNNING', 'overall_sr': None, 'progress_info': None},\n {'exp_id': 'eval-vla-mean-object', 'method': 'vla_mean', 'norm': None, 'seed': None, 'status': 'DONE', 'overall_sr': 0.12, 'progress_info': None},\n {'exp_id': 'eval-vla-mean-object-seed43', 'method': 'vla_mean', 'norm': None, 'seed': 43, 'status': 'DONE', 'overall_sr': 0.15, 'progress_info': None},\n {'exp_id': 'eval-vla-mean-object-seed44', 'method': 'vla_mean', 'norm': None, 'seed': 44, 'status': 'DONE', 'overall_sr': 0.1, 'progress_info': None},\n {'exp_id': 'eval-vla-mean-object-seed45', 'method': 'vla_mean', 'norm': None, 'seed': 45, 'status': 'RUNNING', 'overall_sr': None, 'progress_info': None},\n {'exp_id': 'eval-vla-only-object', 'method': 'vla_only', 'norm': None, 'seed': None, 'status': 'DONE', 'overall_sr': 0.12, 'progress_info': None},\n {'exp_id': 'eval-vla-only-object-seed43', 'method': 'vla_only', 'norm': None, 'seed': 43, 'status': 'DONE', 'overall_sr': 0.12, 'progress_info': None},\n {'exp_id': 'eval-vla-only-object-seed44', 'method': 'vla_only', 'norm': None, 'seed': 44, 'status': 'DONE', 'overall_sr': None, 'progress_info': None},\n {'exp_id': 'eval-vla-only-object-seed44-r2', 'method': 'vla_only', 'norm': None, 'seed': 44, 'status': 'DONE', 'overall_sr': 0.1, 'progress_info': None},\n {'exp_id': 'eval-vla-only-object-seed45', 'method': 'vla_only', 'norm': None, 'seed': 45, 'status': 'DONE', 'overall_sr': 0.09, 'progress_info': None},\n]\n```\n\n**Summary:**\n- **61 total** matching experiments\n- **43 DONE**, **17 RUNNING**, **1 DEPLOYED**\n- **28** have `overall_sr` values (normalized to 0-1 scale; the raw registry used a mix of `overall_sr`, `overall_success_rate`, and `avg_sr` keys, some in percentage 0-100 format)\n- No `progress_info` was stored in any experiment entry\n- Retries (`-r2`, `-r3`, `-r4`) are included as separate entries; for each (method, norm, seed) group, typically the latest retry has metrics recorded\n- The `eval-mag-*` prefix is the legacy naming convention (single-seed runs without explicit seed in name); `eval-{method}-object-norm{NN}-seed{XX}` is the newer multi-seed naming"
      }
    ],
    "totalDurationMs": 176158,
    "totalTokens": 43122,
    "totalToolUseCount": 8,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7060,
      "cache_read_input_tokens": 31404,
      "output_tokens": 4657,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7060
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4657,
          "cache_read_input_tokens": 31404,
          "cache_creation_input_tokens": 7060,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7060,
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
      "bashCount": 8,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  }
}
````

</details>

---

### Assistant

_source line 39_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data. Let me also check if there are any experiments with the original seed (seed 42) that might be the `eval-mag-*` ones without explicit seed in name. Let me also look for the original magnitude sweep experiments that might have seed=42 as default.

Looking at the data:
- `eval-mag-obsonly-norm003-object` — no seed, likely seed=42 (default)
- `eval-mag-obsonly-norm005-object` — no seed, likely seed=42
- `eval-mag-obsonly-norm02-object` — no seed, likely seed=42


- `eval-mag-obsonly-norm03-object` — no seed, likely seed=42
- `eval-mag-perdof-norm003-object` — no seed, likely seed=42
- `eval-mag-perdof-norm005-object` — no seed, likely seed=42
- `eval-mag-perdof-norm02-object` — no seed, likely seed=42
- `eval-mag-perdof-norm03-object` (and retries) — no seed, likely seed=42
- `eval-vla-mean-object` — no seed, likely seed=42
- `eval-vla-only-` (appears to be cut off)

Then there are the explicitly seeded runs, and I'm noticing `eval-obs-only-object-seed43` doesn't follow the standard naming pattern — it's missing the norm specification, which is unusual. Looking at the overall_sr=0.12 for this run, I'm trying to figure out whether this uses the default norm or something else entirely. I'm trying to figure out what norm value these unnamed experiments used by comparing their performance metrics against the known magnitude sweep results, but the values don't align cleanly with any particular norm setting—they might be from an earlier naming convention before the standardization, possibly norm=0.1. I'm going to assign the unnamed experiments to their most likely defaults: `eval-obs-only-object-seed43` probably used norm=0.1 since that was the standard setup, and the `eval-mag-*` experiments without explicit seeds likely used seed=42. Now I'll organize everything into a matrix to see the full picture. Let me think about what needs to go in:

**Methods with norm dimension**: obs_only, perdof
**Methods without norm**: argmin, scalar, vla_mean, vla_only

For obs_only × norm × seed:
- norm 0.03: seed 42 (0.16)
- norm 0.05: seed 42 (0.13)
- norm 0.10: seed 43 (0.12?), seed 44 (0.16), seed 45 (RUNNING)
- norm 0.20: seed 42 (legacy, no sr), seed 43 (0.16 from r2), seed 44 (0.16 from r2), seed 45 (0.16), seed 46 (RUNNING), seed 47 (RUNNING)
- norm 0.30: seed 42 (0.19), seed 44 (0.18), seed 45 (RUNNING r2)
- norm 1.42 (default): seed 44 (0.16), seed 45 (RUNNING)

I'm noticing that some experiment runs have multiple retries, and only the latest one contains valid metrics. I need to identify which entries correspond to which norm values — for instance, `eval-obs-only-object-seed43` with no explicit norm parameter and overall_sr=0.12 should map to the norm=0.1 seed 43 entry. I'll track the latest valid results for each configuration going forward. result for each (method, norm, seed) combination.

Let me now carefully build the matrix. First let me map:

**obs_only:**
- norm=0.03, seed=42: 0.16
- norm=0.05, seed=42: 0.13
- norm=0.10, seed=42: — (no data)
- norm=0.10, seed=43: 0.12 (from eval-obs-only-object-seed43, assuming this is norm=0.1)
- norm=0.10, seed=44: 0.16
- norm=0.10, seed=45: RUNNING
- norm=0.20, seed=42: — (eval-mag-obsonly-norm02-object has no SR)
  Actually wait, eval-mag-obsonly-norm02-object is DONE with overall_sr=None. That's odd.
- norm=0.20, seed=43: 0.16
- norm=0.20, seed=44: 0.16
- norm=0.20, seed=45: 0.16
- norm=0.20, seed=46: RUNNING
- norm=0.20, seed=47: RUNNING
- norm=0.30, seed=42: 0.19
- norm=0.30, seed=44: 0.18
- norm=0.30, seed=45: RUNNING
- norm=1.42, seed=42: — (no data)
- norm=1.42, seed=44: 0.16
- norm=1.42, seed=45: RUNNING

**perdof:**
- norm=0.03, seed=42: 0.14
- norm=0.05, seed=42: 0.14
- norm=0.10, seed=42: —
- norm=0.10, seed=43: 0.12 (from eval-perdof-object-seed43, assuming norm=0.1)
- norm=0.10, seed=44: RUNNING (eval-perdof-object-norm01-seed44)

But wait, there's also `eval-perdof-object-seed44` with overall_sr=0.08. If this is norm=0.1 then we have conflict with `eval-perdof-object-norm01-seed44` which is RUNNING.

Actually maybe `eval-perdof-object-seed43` and `eval-perdof-object-seed44` are NOT norm=0.1. Maybe they're the default norm (1.42)? Let me reconsider the naming convention for default is `eval-perdof-object-default`.

I'm working through the naming conventions to figure out which norm values these experiments actually used, since some entries don't have explicit norm labels in their names. I'm seeing that `eval-perdof-object-seed44` and `eval-perdof-object-norm01-seed44` are both running with the same configuration, which suggests the latter might be a re-run since the original result showed a low success rate. My approach will be to take the most recent valid result for each unique combination of method, norm, and seed, while flagging any currently running experiments for the same parameters. Let me construct the output matrix now with what I have.

Looking at the magnitude sweep experiments, I'm noticing the naming pattern across the obs_only and perdof methods with various norm values at seed 42, which gives me another set of baseline results to incorporate into the matrix. I'm looking at the results for the vla_mean and vla_only methods across different seeds, with most showing scores in the 0.09-0.15 range and a few still running. Now I'm ready to compile everything together.

I need to clarify how to present these success rate values—the subagent normalized everything to a 0-1 scale, so I'll display them as percentages by multiplying by 100 for readability. Let me organize the complete data matrix with the obs_only dimension first.

Generating markdown table... Generating performance metrics table... Looking at the remaining results for vla_mean and vla_only, I can see the pattern of completion rates across different seeds. Now I'm calculating the overall coverage and statistics across all methods—the norm-dependent ones have 36 cells each while the norm-independent methods have 6 seeds each, giving me a total of 72 cells to account for. I'm tracking the completion status across different methods—scalar and vla_mean are done, and vla_only is finished with four cells. That brings the total to 28 completed cells. Now I'm looking at what's still running: obs_only has five cells in progress, perdof has seven, argmin has three more to go, and scalar just started on s45.

So that's 17 cells currently running, which means 51 cells haven't started yet out of the 96 total. I'm noticing there might be some overlap with the perdof norm=0.10 seed=44 case—there's a completed result with sr=0.08, but also a running version that could be a re-run, so I should use the finished one as the value. Now I'm calculating means and standard deviations for methods with enough data points, starting with obs_only norm=0.20 where seeds 43, 44, and 45 all show 0.16.

Continuing with the remaining methods: obs_only norm=0.10 gives me a mean of 0.14 with a standard deviation of 0.028 across seeds 43 and 44, while vla_only across seeds 42 through 45 averages to about 0.1075 with a standard deviation of 0.014. I'll convert these to percentages for the output and then write out the artifact file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "17ac476a-dce3-448f-b7ca-396cbd486cca",
  "uuid": "367ccbec-c3dd-4df2-ab98-719a5b187734",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S9NtRokM2Sqqevf5SdRUfM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5431,
      "cache_read_input_tokens": 25670,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5431
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

Now I have all the data. Let me organize it into the matrix format and write the artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "17ac476a-dce3-448f-b7ca-396cbd486cca",
  "uuid": "63baa264-cbc9-426f-be4a-64eb3f6bb06d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S9NtRokM2Sqqevf5SdRUfM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5431,
      "cache_read_input_tokens": 25670,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5431
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_018tXzBYcXyd8n4eDywGPnRt`</summary>

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
  "session_id": "17ac476a-dce3-448f-b7ca-396cbd486cca",
  "uuid": "91ef13c3-892f-4230-afa1-24b1d586c33f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S9NtRokM2Sqqevf5SdRUfM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5431,
      "cache_read_input_tokens": 25670,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5431
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

_source line 42 · 2026-05-16T22:18:48.748Z_

<details><summary>↩ Tool result · `toolu_018tXzBYcXyd8n4eDywGPnRt`</summary>

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
  "session_id": "17ac476a-dce3-448f-b7ca-396cbd486cca",
  "uuid": "d0fe0915-d799-4645-bef4-463637012098",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Assistant

_source line 43_

<details><summary>Logged reasoning block</summary>

```text
Now let me write the artifact file with all the organized data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "17ac476a-dce3-448f-b7ca-396cbd486cca",
  "uuid": "01d772ef-162d-453b-a98c-88e954893b71",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017KucpffjGP4cFtYYVyeZi8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6075,
      "cache_read_input_tokens": 31101,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6075
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

_source line 44_

<details open><summary>🔧 Tool call — Write · `toolu_013cyPTEZuCriSRBxEVe5cyd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/magnitude_multiseed_data.md",
  "content": "# Magnitude Multi-Seed Data Matrix (Object Benchmark)\n\n> Generated: 2026-05-16\n> Source: experiment registry (acr-vla-conformal-refinement)\n\n## 注意事项\n\n- SR 值为 0-1 scale（即 0.16 = 16% success rate）\n- `eval-mag-*` 命名的实验视为 seed=42（原始 magnitude sweep）\n- `eval-{method}-object-seed{XX}` 无 norm 标注的视为 norm=0.10（标准配置）\n- 有 retry（-r2/-r3）的取最新有效结果\n- perdof norm=0.10 seed=44: 旧实验 sr=0.08，新命名实验 RUNNING 中（疑似 re-run）\n\n---\n\n## 1. obs_only (norm × seed)\n\n| norm | seed 42 | seed 43 | seed 44 | seed 45 | seed 46 | seed 47 |\n|------|---------|---------|---------|---------|---------|---------|\n| 0.03 | **0.16** | — | — | — | — | — |\n| 0.05 | **0.13** | — | — | — | — | — |\n| 0.10 | — | **0.12** | **0.16** | RUNNING | — | — |\n| 0.20 | *(no SR)* | **0.16** | **0.16** | **0.16** | RUNNING | RUNNING |\n| 0.30 | **0.19** | — | **0.18** | RUNNING | — | — |\n| 1.42 | — | — | **0.16** | RUNNING | — | — |\n\n## 2. perdof (norm × seed)\n\n| norm | seed 42 | seed 43 | seed 44 | seed 45 | seed 46 | seed 47 |\n|------|---------|---------|---------|---------|---------|---------|\n| 0.03 | **0.14** | — | — | — | — | — |\n| 0.05 | **0.14** | — | — | — | — | — |\n| 0.10 | — | **0.12** | **0.08** | RUNNING | — | — |\n| 0.20 | **0.11** | **0.09** | — | RUNNING | — | — |\n| 0.30 | **0.04** | — | RUNNING | RUNNING | — | — |\n| 1.42 | — | — | RUNNING | RUNNING | — | — |\n\n## 3. argmin (no norm dimension)\n\n| seed 42 | seed 43 | seed 44 | seed 45 | seed 46 | seed 47 |\n|---------|---------|---------|---------|---------|---------|\n| — | **0.17** | **0.13** | RUNNING | RUNNING | RUNNING |\n\n## 4. scalar (no norm dimension)\n\n| seed 42 | seed 43 | seed 44 | seed 45 | seed 46 | seed 47 |\n|---------|---------|---------|---------|---------|---------|\n| — | **0.10** | **0.06** | RUNNING | — | — |\n\n## 5. vla_mean (no norm dimension)\n\n| seed 42 | seed 43 | seed 44 | seed 45 | seed 46 | seed 47 |\n|---------|---------|---------|---------|---------|---------|\n| **0.12** | **0.15** | **0.10** | RUNNING | — | — |\n\n## 6. vla_only (no norm dimension)\n\n| seed 42 | seed 43 | seed 44 | seed 45 | seed 46 | seed 47 |\n|---------|---------|---------|---------|---------|---------|\n| **0.12** | **0.12** | **0.10** | **0.09** | — | — |\n\n---\n\n## 覆盖率统计\n\n| 类别 | 总 cells | 已完成 | RUNNING | 未部署 | 完成率 |\n|------|----------|--------|---------|--------|--------|\n| obs_only (6 norms × 6 seeds) | 36 | 10 | 5 | 21 | 28% |\n| perdof (6 norms × 6 seeds) | 36 | 7 | 7 | 22 | 19% |\n| argmin (6 seeds) | 6 | 2 | 3 | 1 | 33% |\n| scalar (6 seeds) | 6 | 2 | 1 | 3 | 33% |\n| vla_mean (6 seeds) | 6 | 3 | 1 | 2 | 50% |\n| vla_only (6 seeds) | 6 | 4 | 0 | 2 | 67% |\n| **总计** | **96** | **28** | **17** | **51** | **29%** |\n\n---\n\n## Mean ± Std（≥2 seeds 完成的组合）\n\n### obs_only by norm\n\n| norm | n_seeds | mean | std | seeds used |\n|------|---------|------|-----|------------|\n| 0.10 | 2 | 0.140 | 0.028 | 43, 44 |\n| 0.20 | 3 | 0.160 | 0.000 | 43, 44, 45 |\n| 0.30 | 2 | 0.185 | 0.007 | 42, 44 |\n\n### perdof by norm\n\n| norm | n_seeds | mean | std | seeds used |\n|------|---------|------|-----|------------|\n| 0.10 | 2 | 0.100 | 0.028 | 43, 44 |\n| 0.20 | 2 | 0.100 | 0.014 | 42, 43 |\n\n### Methods without norm\n\n| method | n_seeds | mean | std | seeds used |\n|--------|---------|------|-----|------------|\n| argmin | 2 | 0.150 | 0.028 | 43, 44 |\n| scalar | 2 | 0.080 | 0.028 | 43, 44 |\n| vla_mean | 3 | 0.123 | 0.025 | 42, 43, 44 |\n| vla_only | 4 | 0.108 | 0.014 | 42, 43, 44, 45 |\n\n---\n\n## 缺失数据清单\n\n### 高优先级（有部分 seed 完成，需补齐 error bar）\n\n**obs_only norm=0.20** — 最接近完整，缺 seed 42 结果（实验存在但无 SR）, seed 46/47 RUNNING\n**obs_only norm=0.10** — 缺 seed 42, 45(RUNNING), 46, 47\n**obs_only norm=0.30** — 缺 seed 43, 45(RUNNING), 46, 47\n**vla_only** — 缺 seed 46, 47（4 seeds 已完成，可能足够）\n**vla_mean** — 缺 seed 45(RUNNING), 46, 47\n**argmin** — 缺 seed 42, 45/46/47(RUNNING)\n\n### 中优先级（只有 1-2 个 seed）\n\n**obs_only norm=0.03** — 仅 seed 42\n**obs_only norm=0.05** — 仅 seed 42\n**obs_only norm=1.42** — 仅 seed 44, seed 45 RUNNING\n**perdof norm=0.03** — 仅 seed 42\n**perdof norm=0.05** — 仅 seed 42\n**perdof norm=0.30** — 仅 seed 42 (sr=0.04), seed 44/45 RUNNING\n**perdof norm=1.42** — 无完成，seed 44/45 RUNNING\n**scalar** — 仅 seed 43/44\n\n### 未部署（完全没有实验）\n\n| method | norm | missing seeds |\n|--------|------|---------------|\n| obs_only | 0.03 | 43, 44, 45, 46, 47 |\n| obs_only | 0.05 | 43, 44, 45, 46, 47 |\n| obs_only | 0.10 | 42, 46, 47 |\n| obs_only | 0.20 | — (全部已有或 RUNNING) |\n| obs_only | 0.30 | 43, 46, 47 |\n| obs_only | 1.42 | 42, 43, 46, 47 |\n| perdof | 0.03 | 43, 44, 45, 46, 47 |\n| perdof | 0.05 | 43, 44, 45, 46, 47 |\n| perdof | 0.10 | 42, 46, 47 |\n| perdof | 0.20 | 44, 46, 47 |\n| perdof | 0.30 | 43, 46, 47 |\n| perdof | 1.42 | 42, 43, 46, 47 |\n| argmin | — | 42 |\n| scalar | — | 42, 46, 47 |\n| vla_mean | — | 46, 47 |\n| vla_only | — | 46, 47 |\n\n---\n\n## 实验 ID 到结果映射（完整参考）\n\n### obs_only\n| exp_id | norm | seed | status | overall_sr |\n|--------|------|------|--------|------------|\n| eval-mag-obsonly-norm003-object | 0.03 | 42 | DONE | 0.16 |\n| eval-mag-obsonly-norm005-object | 0.05 | 42 | DONE | 0.13 |\n| eval-obs-only-object-seed43 | 0.10 | 43 | DONE | 0.12 |\n| eval-obs-only-object-norm01-seed44 | 0.10 | 44 | DONE | 0.16 |\n| eval-obs-only-object-norm01-seed45 | 0.10 | 45 | RUNNING | — |\n| eval-mag-obsonly-norm02-object | 0.20 | 42 | DONE | *(no SR)* |\n| eval-obs-only-object-norm02-seed43-r2 | 0.20 | 43 | DONE | 0.16 |\n| eval-obs-only-object-norm02-seed44-r2 | 0.20 | 44 | DONE | 0.16 |\n| eval-obs-only-object-norm02-seed45 | 0.20 | 45 | DONE | 0.16 |\n| eval-obs-only-object-norm02-seed46 | 0.20 | 46 | RUNNING | — |\n| eval-obs-only-object-norm02-seed47 | 0.20 | 47 | RUNNING | — |\n| eval-mag-obsonly-norm03-object | 0.30 | 42 | DONE | 0.19 |\n| eval-obs-only-object-norm03-seed44 | 0.30 | 44 | DONE | 0.18 |\n| eval-obs-only-object-norm03-seed45-r2 | 0.30 | 45 | RUNNING | — |\n| eval-obs-only-object-default-seed44 | 1.42 | 44 | DONE | 0.16 |\n| eval-obs-only-object-default-seed45 | 1.42 | 45 | RUNNING | — |\n\n### perdof\n| exp_id | norm | seed | status | overall_sr |\n|--------|------|------|--------|------------|\n| eval-mag-perdof-norm003-object | 0.03 | 42 | DONE | 0.14 |\n| eval-mag-perdof-norm005-object | 0.05 | 42 | DONE | 0.14 |\n| eval-perdof-object-seed43 | 0.10 | 43 | DONE | 0.12 |\n| eval-perdof-object-seed44 | 0.10 | 44 | DONE | 0.08 |\n| eval-perdof-object-norm01-seed44 | 0.10 | 44 | RUNNING | — |\n| eval-perdof-object-norm01-seed45 | 0.10 | 45 | RUNNING | — |\n| eval-mag-perdof-norm02-object | 0.20 | 42 | DONE | 0.11 |\n| eval-mag-perdof-norm02-seed43-object-r3 | 0.20 | 43 | DONE | 0.09 |\n| eval-perdof-object-norm02-seed45 | 0.20 | 45 | RUNNING | — |\n| eval-mag-perdof-norm03-object-r3 | 0.30 | 42 | DONE | 0.04 |\n| eval-perdof-object-norm03-seed44 | 0.30 | 44 | RUNNING | — |\n| eval-perdof-object-norm03-seed45-r2 | 0.30 | 45 | RUNNING | — |\n| eval-perdof-object-default-seed44 | 1.42 | 44 | RUNNING | — |\n| eval-perdof-object-default-seed45 | 1.42 | 45 | RUNNING | — |\n\n### argmin\n| exp_id | seed | status | overall_sr |\n|--------|------|--------|------------|\n| eval-argmin-object-seed43 | 43 | DONE | 0.17 |\n| eval-argmin-object-seed44-r2 | 44 | DONE | 0.13 |\n| eval-argmin-object-seed45 | 45 | RUNNING | — |\n| eval-argmin-object-seed46 | 46 | RUNNING | — |\n| eval-argmin-object-seed47 | 47 | RUNNING | — |\n\n### scalar\n| exp_id | seed | status | overall_sr |\n|--------|------|--------|------------|\n| eval-scalar-object-seed43 | 43 | DONE | 0.10 |\n| eval-scalar-object-seed44-r2 | 44 | DONE | 0.06 |\n| eval-scalar-object-seed45 | 45 | RUNNING | — |\n\n### vla_mean\n| exp_id | seed | status | overall_sr |\n|--------|------|--------|------------|\n| eval-vla-mean-object | 42 | DONE | 0.12 |\n| eval-vla-mean-object-seed43 | 43 | DONE | 0.15 |\n| eval-vla-mean-object-seed44 | 44 | DONE | 0.10 |\n| eval-vla-mean-object-seed45 | 45 | RUNNING | — |\n\n### vla_only\n| exp_id | seed | status | overall_sr |\n|--------|------|--------|------------|\n| eval-vla-only-object | 42 | DONE | 0.12 |\n| eval-vla-only-object-seed43 | 43 | DONE | 0.12 |\n| eval-vla-only-object-seed44-r2 | 44 | DONE | 0.10 |\n| eval-vla-only-object-seed45 | 45 | DONE | 0.09 |\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "17ac476a-dce3-448f-b7ca-396cbd486cca",
  "uuid": "c89536d2-f262-4389-b80c-683bf711263e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017KucpffjGP4cFtYYVyeZi8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6075,
      "cache_read_input_tokens": 31101,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6075
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

_source line 45 · 2026-05-16T22:19:40.413Z_

<details><summary>↩ Tool result · `toolu_013cyPTEZuCriSRBxEVe5cyd`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/magnitude_multiseed_data.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "17ac476a-dce3-448f-b7ca-396cbd486cca",
  "uuid": "772e2ffa-6ca6-4dca-b685-00dc7948d739",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/magnitude_multiseed_data.md",
    "content": "# Magnitude Multi-Seed Data Matrix (Object Benchmark)\n\n> Generated: 2026-05-16\n> Source: experiment registry (acr-vla-conformal-refinement)\n\n## 注意事项\n\n- SR 值为 0-1 scale（即 0.16 = 16% success rate）\n- `eval-mag-*` 命名的实验视为 seed=42（原始 magnitude sweep）\n- `eval-{method}-object-seed{XX}` 无 norm 标注的视为 norm=0.10（标准配置）\n- 有 retry（-r2/-r3）的取最新有效结果\n- perdof norm=0.10 seed=44: 旧实验 sr=0.08，新命名实验 RUNNING 中（疑似 re-run）\n\n---\n\n## 1. obs_only (norm × seed)\n\n| norm | seed 42 | seed 43 | seed 44 | seed 45 | seed 46 | seed 47 |\n|------|---------|---------|---------|---------|---------|---------|\n| 0.03 | **0.16** | — | — | — | — | — |\n| 0.05 | **0.13** | — | — | — | — | — |\n| 0.10 | — | **0.12** | **0.16** | RUNNING | — | — |\n| 0.20 | *(no SR)* | **0.16** | **0.16** | **0.16** | RUNNING | RUNNING |\n| 0.30 | **0.19** | — | **0.18** | RUNNING | — | — |\n| 1.42 | — | — | **0.16** | RUNNING | — | — |\n\n## 2. perdof (norm × seed)\n\n| norm | seed 42 | seed 43 | seed 44 | seed 45 | seed 46 | seed 47 |\n|------|---------|---------|---------|---------|---------|---------|\n| 0.03 | **0.14** | — | — | — | — | — |\n| 0.05 | **0.14** | — | — | — | — | — |\n| 0.10 | — | **0.12** | **0.08** | RUNNING | — | — |\n| 0.20 | **0.11** | **0.09** | — | RUNNING | — | — |\n| 0.30 | **0.04** | — | RUNNING | RUNNING | — | — |\n| 1.42 | — | — | RUNNING | RUNNING | — | — |\n\n## 3. argmin (no norm dimension)\n\n| seed 42 | seed 43 | seed 44 | seed 45 | seed 46 | seed 47 |\n|---------|---------|---------|---------|---------|---------|\n| — | **0.17** | **0.13** | RUNNING | RUNNING | RUNNING |\n\n## 4. scalar (no norm dimension)\n\n| seed 42 | seed 43 | seed 44 | seed 45 | seed 46 | seed 47 |\n|---------|---------|---------|---------|---------|---------|\n| — | **0.10** | **0.06** | RUNNING | — | — |\n\n## 5. vla_mean (no norm dimension)\n\n| seed 42 | seed 43 | seed 44 | seed 45 | seed 46 | seed 47 |\n|---------|---------|---------|---------|---------|---------|\n| **0.12** | **0.15** | **0.10** | RUNNING | — | — |\n\n## 6. vla_only (no norm dimension)\n\n| seed 42 | seed 43 | seed 44 | seed 45 | seed 46 | seed 47 |\n|---------|---------|---------|---------|---------|---------|\n| **0.12** | **0.12** | **0.10** | **0.09** | — | — |\n\n---\n\n## 覆盖率统计\n\n| 类别 | 总 cells | 已完成 | RUNNING | 未部署 | 完成率 |\n|------|----------|--------|---------|--------|--------|\n| obs_only (6 norms × 6 seeds) | 36 | 10 | 5 | 21 | 28% |\n| perdof (6 norms × 6 seeds) | 36 | 7 | 7 | 22 | 19% |\n| argmin (6 seeds) | 6 | 2 | 3 | 1 | 33% |\n| scalar (6 seeds) | 6 | 2 | 1 | 3 | 33% |\n| vla_mean (6 seeds) | 6 | 3 | 1 | 2 | 50% |\n| vla_only (6 seeds) | 6 | 4 | 0 | 2 | 67% |\n| **总计** | **96** | **28** | **17** | **51** | **29%** |\n\n---\n\n## Mean ± Std（≥2 seeds 完成的组合）\n\n### obs_only by norm\n\n| norm | n_seeds | mean | std | seeds used |\n|------|---------|------|-----|------------|\n| 0.10 | 2 | 0.140 | 0.028 | 43, 44 |\n| 0.20 | 3 | 0.160 | 0.000 | 43, 44, 45 |\n| 0.30 | 2 | 0.185 | 0.007 | 42, 44 |\n\n### perdof by norm\n\n| norm | n_seeds | mean | std | seeds used |\n|------|---------|------|-----|------------|\n| 0.10 | 2 | 0.100 | 0.028 | 43, 44 |\n| 0.20 | 2 | 0.100 | 0.014 | 42, 43 |\n\n### Methods without norm\n\n| method | n_seeds | mean | std | seeds used |\n|--------|---------|------|-----|------------|\n| argmin | 2 | 0.150 | 0.028 | 43, 44 |\n| scalar | 2 | 0.080 | 0.028 | 43, 44 |\n| vla_mean | 3 | 0.123 | 0.025 | 42, 43, 44 |\n| vla_only | 4 | 0.108 | 0.014 | 42, 43, 44, 45 |\n\n---\n\n## 缺失数据清单\n\n### 高优先级（有部分 seed 完成，需补齐 error bar）\n\n**obs_only norm=0.20** — 最接近完整，缺 seed 42 结果（实验存在但无 SR）, seed 46/47 RUNNING\n**obs_only norm=0.10** — 缺 seed 42, 45(RUNNING), 46, 47\n**obs_only norm=0.30** — 缺 seed 43, 45(RUNNING), 46, 47\n**vla_only** — 缺 seed 46, 47（4 seeds 已完成，可能足够）\n**vla_mean** — 缺 seed 45(RUNNING), 46, 47\n**argmin** — 缺 seed 42, 45/46/47(RUNNING)\n\n### 中优先级（只有 1-2 个 seed）\n\n**obs_only norm=0.03** — 仅 seed 42\n**obs_only norm=0.05** — 仅 seed 42\n**obs_only norm=1.42** — 仅 seed 44, seed 45 RUNNING\n**perdof norm=0.03** — 仅 seed 42\n**perdof norm=0.05** — 仅 seed 42\n**perdof norm=0.30** — 仅 seed 42 (sr=0.04), seed 44/45 RUNNING\n**perdof norm=1.42** — 无完成，seed 44/45 RUNNING\n**scalar** — 仅 seed 43/44\n\n### 未部署（完全没有实验）\n\n| method | norm | missing seeds |\n|--------|------|---------------|\n| obs_only | 0.03 | 43, 44, 45, 46, 47 |\n| obs_only | 0.05 | 43, 44, 45, 46, 47 |\n| obs_only | 0.10 | 42, 46, 47 |\n| obs_only | 0.20 | — (全部已有或 RUNNING) |\n| obs_only | 0.30 | 43, 46, 47 |\n| obs_only | 1.42 | 42, 43, 46, 47 |\n| perdof | 0.03 | 43, 44, 45, 46, 47 |\n| perdof | 0.05 | 43, 44, 45, 46, 47 |\n| perdof | 0.10 | 42, 46, 47 |\n| perdof | 0.20 | 44, 46, 47 |\n| perdof | 0.30 | 43, 46, 47 |\n| perdof | 1.42 | 42, 43, 46, 47 |\n| argmin | — | 42 |\n| scalar | — | 42, 46, 47 |\n| vla_mean | — | 46, 47 |\n| vla_only | — | 46, 47 |\n\n---\n\n## 实验 ID 到结果映射（完整参考）\n\n### obs_only\n| exp_id | norm | seed | status | overall_sr |\n|--------|------|------|--------|------------|\n| eval-mag-obsonly-norm003-object | 0.03 | 42 | DONE | 0.16 |\n| eval-mag-obsonly-norm005-object | 0.05 | 42 | DONE | 0.13 |\n| eval-obs-only-object-seed43 | 0.10 | 43 | DONE | 0.12 |\n| eval-obs-only-object-norm01-seed44 | 0.10 | 44 | DONE | 0.16 |\n| eval-obs-only-object-norm01-seed45 | 0.10 | 45 | RUNNING | — |\n| eval-mag-obsonly-norm02-object | 0.20 | 42 | DONE | *(no SR)* |\n| eval-obs-only-object-norm02-seed43-r2 | 0.20 | 43 | DONE | 0.16 |\n| eval-obs-only-object-norm02-seed44-r2 | 0.20 | 44 | DONE | 0.16 |\n| eval-obs-only-object-norm02-seed45 | 0.20 | 45 | DONE | 0.16 |\n| eval-obs-only-object-norm02-seed46 | 0.20 | 46 | RUNNING | — |\n| eval-obs-only-object-norm02-seed47 | 0.20 | 47 | RUNNING | — |\n| eval-mag-obsonly-norm03-object | 0.30 | 42 | DONE | 0.19 |\n| eval-obs-only-object-norm03-seed44 | 0.30 | 44 | DONE | 0.18 |\n| eval-obs-only-object-norm03-seed45-r2 | 0.30 | 45 | RUNNING | — |\n| eval-obs-only-object-default-seed44 | 1.42 | 44 | DONE | 0.16 |\n| eval-obs-only-object-default-seed45 | 1.42 | 45 | RUNNING | — |\n\n### perdof\n| exp_id | norm | seed | status | overall_sr |\n|--------|------|------|--------|------------|\n| eval-mag-perdof-norm003-object | 0.03 | 42 | DONE | 0.14 |\n| eval-mag-perdof-norm005-object | 0.05 | 42 | DONE | 0.14 |\n| eval-perdof-object-seed43 | 0.10 | 43 | DONE | 0.12 |\n| eval-perdof-object-seed44 | 0.10 | 44 | DONE | 0.08 |\n| eval-perdof-object-norm01-seed44 | 0.10 | 44 | RUNNING | — |\n| eval-perdof-object-norm01-seed45 | 0.10 | 45 | RUNNING | — |\n| eval-mag-perdof-norm02-object | 0.20 | 42 | DONE | 0.11 |\n| eval-mag-perdof-norm02-seed43-object-r3 | 0.20 | 43 | DONE | 0.09 |\n| eval-perdof-object-norm02-seed45 | 0.20 | 45 | RUNNING | — |\n| eval-mag-perdof-norm03-object-r3 | 0.30 | 42 | DONE | 0.04 |\n| eval-perdof-object-norm03-seed44 | 0.30 | 44 | RUNNING | — |\n| eval-perdof-object-norm03-seed45-r2 | 0.30 | 45 | RUNNING | — |\n| eval-perdof-object-default-seed44 | 1.42 | 44 | RUNNING | — |\n| eval-perdof-object-default-seed45 | 1.42 | 45 | RUNNING | — |\n\n### argmin\n| exp_id | seed | status | overall_sr |\n|--------|------|--------|------------|\n| eval-argmin-object-seed43 | 43 | DONE | 0.17 |\n| eval-argmin-object-seed44-r2 | 44 | DONE | 0.13 |\n| eval-argmin-object-seed45 | 45 | RUNNING | — |\n| eval-argmin-object-seed46 | 46 | RUNNING | — |\n| eval-argmin-object-seed47 | 47 | RUNNING | — |\n\n### scalar\n| exp_id | seed | status | overall_sr |\n|--------|------|--------|------------|\n| eval-scalar-object-seed43 | 43 | DONE | 0.10 |\n| eval-scalar-object-seed44-r2 | 44 | DONE | 0.06 |\n| eval-scalar-object-seed45 | 45 | RUNNING | — |\n\n### vla_mean\n| exp_id | seed | status | overall_sr |\n|--------|------|--------|------------|\n| eval-vla-mean-object | 42 | DONE | 0.12 |\n| eval-vla-mean-object-seed43 | 43 | DONE | 0.15 |\n| eval-vla-mean-object-seed44 | 44 | DONE | 0.10 |\n| eval-vla-mean-object-seed45 | 45 | RUNNING | — |\n\n### vla_only\n| exp_id | seed | status | overall_sr |\n|--------|------|--------|------------|\n| eval-vla-only-object | 42 | DONE | 0.12 |\n| eval-vla-only-object-seed43 | 43 | DONE | 0.12 |\n| eval-vla-only-object-seed44-r2 | 44 | DONE | 0.10 |\n| eval-vla-only-object-seed45 | 45 | DONE | 0.09 |\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 46_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01S8hBvko71XVpiXFXkjY1T7`</summary>

```json
{
  "name": "magnitude_multiseed_data",
  "type": "data",
  "description": "Object benchmark magnitude sweep 跨 seed 数据矩阵 (norm × seed × method)，含覆盖率统计、mean±std、缺失数据清单",
  "project": "acr-vla-conformal-refinement",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/magnitude_multiseed_data.md",
  "tags": [
    "magnitude",
    "multiseed",
    "object-benchmark",
    "error-bars"
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
  "session_id": "17ac476a-dce3-448f-b7ca-396cbd486cca",
  "uuid": "d9ba9b2f-5f88-4757-8570-4fa5fbff174c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015KkN5u3XnZM3aC1Nqn7LTn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4307,
      "cache_read_input_tokens": 37176,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4307
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

_source line 47 · 2026-05-16T22:19:47.451Z_

<details><summary>↩ Tool result · `toolu_01S8hBvko71XVpiXFXkjY1T7`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_030619\", \"name\": \"magnitude_multiseed_data\", \"type\": \"data\", \"description\": \"Object benchmark magnitude sweep 跨 seed 数据矩阵 (norm × seed × method)，含覆盖率统计、mean±std、缺失数据清单\", \"path\": \"projects/acr-vla-conformal-refinement/artifacts/_project/data/magnitude_multiseed_data.md\", \"url\": null, \"project\": \"acr-vla-conformal-refinement\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T22:19:47.126887+00:00\", \"tags\": [\"magnitude\", \"multiseed\", \"object-benchmark\", \"error-bars\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "17ac476a-dce3-448f-b7ca-396cbd486cca",
  "uuid": "b47b3fe5-db2a-4985-b80d-327759859264",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260516_030619\\\", \\\"name\\\": \\\"magnitude_multiseed_data\\\", \\\"type\\\": \\\"data\\\", \\\"description\\\": \\\"Object benchmark magnitude sweep 跨 seed 数据矩阵 (norm × seed × method)，含覆盖率统计、mean±std、缺失数据清单\\\", \\\"path\\\": \\\"projects/acr-vla-conformal-refinement/artifacts/_project/data/magnitude_multiseed_data.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"acr-vla-conformal-refinement\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-16T22:19:47.126887+00:00\\\", \\\"tags\\\": [\\\"magnitude\\\", \\\"multiseed\\\", \\\"object-benchmark\\\", \\\"error-bars\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_030619\", \"name\": \"magnitude_multiseed_data\", \"type\": \"data\", \"description\": \"Object benchmark magnitude sweep 跨 seed 数据矩阵 (norm × seed × method)，含覆盖率统计、mean±std、缺失数据清单\", \"path\": \"projects/acr-vla-conformal-refinement/artifacts/_project/data/magnitude_multiseed_data.md\", \"url\": null, \"project\": \"acr-vla-conformal-refinement\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T22:19:47.126887+00:00\", \"tags\": [\"magnitude\", \"multiseed\", \"object-benchmark\", \"error-bars\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 48_

完成。数据已写入 `artifacts/magnitude_multiseed_data.md` 并注册。

**关键数字：**
- 总计 96 个 cells，28 已完成 (29%)，17 RUNNING，51 未部署
- 目前可算 error bar 的组合：obs_only norm=0.20 (3 seeds, mean=0.16, std=0)、vla_only (4 seeds, mean=0.108, std=0.014)、vla_mean (3 seeds, mean=0.123, std=0.025)
- obs_only/perdof 的 norm=0.03 和 0.05 最缺数据（都只有 seed 42）
- norm=0.20 的 obs_only 覆盖最好，seed 46/47 正在跑

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "17ac476a-dce3-448f-b7ca-396cbd486cca",
  "uuid": "a131b7e3-8efa-4273-92e7-43d66c00c3b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Sri3qQRcEorEtrEodn1ym",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 580,
      "cache_read_input_tokens": 41483,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 580
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

_source line 49_

完成。数据已写入 `artifacts/magnitude_multiseed_data.md` 并注册。

**关键数字：**
- 总计 96 个 cells，28 已完成 (29%)，17 RUNNING，51 未部署
- 目前可算 error bar 的组合：obs_only norm=0.20 (3 seeds, mean=0.16, std=0)、vla_only (4 seeds, mean=0.108, std=0.014)、vla_mean (3 seeds, mean=0.123, std=0.025)
- obs_only/perdof 的 norm=0.03 和 0.05 最缺数据（都只有 seed 42）
- norm=0.20 的 obs_only 覆盖最好，seed 46/47 正在跑

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 342631,
  "duration_api_ms": 341641,
  "num_turns": 7,
  "stop_reason": "end_turn",
  "session_id": "17ac476a-dce3-448f-b7ca-396cbd486cca",
  "total_cost_usd": 1.235722,
  "usage": {
    "input_tokens": 13,
    "cache_creation_input_tokens": 30222,
    "cache_read_input_tokens": 196884,
    "output_tokens": 11108,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 30222,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 221,
        "cache_read_input_tokens": 41483,
        "cache_creation_input_tokens": 580,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 580
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1264,
      "outputTokens": 15,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001339,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 24,
      "outputTokens": 24765,
      "cacheReadInputTokens": 371701,
      "cacheCreationInputTokens": 68686,
      "webSearchRequests": 0,
      "costUSD": 1.234383,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "39360404-d9d8-4c9d-86b5-49f8e5e2aa3f"
}
```

</details>

---
