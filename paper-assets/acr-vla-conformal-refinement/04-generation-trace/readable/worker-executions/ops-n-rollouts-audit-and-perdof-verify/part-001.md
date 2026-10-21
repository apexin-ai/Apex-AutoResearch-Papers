# ops n rollouts audit and perdof verify — Part 1 of 2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

[Transcript overview](../ops-n-rollouts-audit-and-perdof-verify.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/30/30a985f0f9b92136022c.json)

## Before a recorded user message

## Before a recorded user message

16 recorded events


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
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
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
  "uuid": "c899edae-263b-441b-a131-706d5025467e",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/memory/"
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
    "resetsAt": 1779118800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "559dc1df-d1db-47c2-88bb-15dea6f6a76d",
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d"
}
```

---


### Assistant

_source line 4_

I'll start by reading the project configuration and registry to understand the experiment setup, then SSH to servers to verify the data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "c48896c9-ad9f-416a-959f-0c31d4aefe8f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TQJsRzAxqJAjwB1jtA1pfk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13685,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13685
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_015XHkYDZuXS1LXnNS6PF1W9`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only",
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
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "f0adb3ad-490e-4eb2-84b0-6e2a9416a261",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TQJsRzAxqJAjwB1jtA1pfk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13685,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13685
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

_source line 6 · 2026-05-18T10:42:59.391Z_

<details><summary>↩ Tool result · `toolu_015XHkYDZuXS1LXnNS6PF1W9`</summary>

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
  "tool_name": "mcp__agent-ml-research__ssh_execute"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_read_only"
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
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "b310e336-cf4f-4b7c-b0c5-b2f914c2e054",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__ssh_read_only"
    ],
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only",
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
Let me start by reading the registry to find all relevant experiments, and also check the existing data files in the project.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "f25c11d6-64dd-4050-88a9-c3cc35992e9c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S9ujVFna7AfzKXXLUD7uKB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1044,
      "cache_read_input_tokens": 25526,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1044
      },
      "output_tokens": 26,
      "service_tier": "standard",
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

_source line 8_

Let me start by reading the registry and checking existing data files in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "e5eb5592-0cee-4959-852c-d524c2ff120f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S9ujVFna7AfzKXXLUD7uKB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1044,
      "cache_read_input_tokens": 25526,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1044
      },
      "output_tokens": 26,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_016mHEzU7xURReT8XBUX2SM2`</summary>

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
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "c3fdc541-70da-4c7d-871e-ccfa398724ee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S9ujVFna7AfzKXXLUD7uKB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1044,
      "cache_read_input_tokens": 25526,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1044
      },
      "output_tokens": 26,
      "service_tier": "standard",
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

_source line 10 · 2026-05-18T10:43:04.765Z_

<details><summary>↩ Tool result · `toolu_016mHEzU7xURReT8XBUX2SM2`</summary>

```text
Error: result (364,316 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/c1bdccab-16c6-497c-9d30-0feab97d927d/tool-results/mcp-agent-ml-research-read_registry-1779100984736.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/c1bdccab-16c6-497c-9d30-0feab97d927d/tool-results/mcp-agent-ml-research-read_registry-1779100984736.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/c1bdccab-16c6-497c-9d30-0feab97d927d/tool-results/mcp-agent-ml-research-read_registry-1779100984736.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "21fe8ab3-7d80-4013-a09e-f67c49043b54",
  "tool_use_result": {
    "content": "Error: result (364,316 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/c1bdccab-16c6-497c-9d30-0feab97d927d/tool-results/mcp-agent-ml-research-read_registry-1779100984736.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/c1bdccab-16c6-497c-9d30-0feab97d927d/tool-results/mcp-agent-ml-research-read_registry-1779100984736.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/c1bdccab-16c6-497c-9d30-0feab97d927d/tool-results/mcp-agent-ml-research-read_registry-1779100984736.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval-perdof-object-norm02-seed45-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T23:09:08.601Z\", \"updated_at\": \"2026-05-18T10:42:06.788Z\", \"hypothesis\": \"perdof CRM (ε=0.2) seed45 on LIBERO-Object. r3 重试。补充 perdof magnitude curve ε=0.2 数据。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed45_r3.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": 749547, \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_perdof\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed45_r3.json\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\"}, \"metrics\": {\"overall_success_rate\": 0.12, \"tasks_completed\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T10:28:49.451Z\"}, \"eval-perdof-object-norm005-seed44\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-17T23:31:56.813Z\", \"updated_at\": \"2026-05-18T10:37:09.805Z\", \"spec\": {\"command\": \"crm_perdof --seed 44 --K 10 --max_correction_norm 0.05\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"553052\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm005-seed44.log\", \"submitted_at\": \"2026-05-17T23:31:56.266Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_perdof\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}, \"hypothesis\": \"perdof CRM (ε=0.05) seed44 on LIBERO-Object. 补充 Figure 2 低 norm 段 perdof 数据。与 obs_only norm005 seed44 配对对比。\"}, \"eval-random-selection-object-seed44\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T02:25:56.030Z\", \"updated_at\": \"2026-05-18T10:37:07.439Z\", \"spec\": {\"command\": \"random_selection --seed 44 --K 10\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"pid\": \"514350\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-random-selection-object-seed44.log\", \"submitted_at\": \"2026-05-18T02:25:55.477Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"random_selection\", \"seed\": 44, \"eval_data\": \"LIBERO-Object\"}, \"hypothesis\": \"Random selection baseline (K=10 随机选一个 action) seed44 on LIBERO-Object. 第三个 seed 验证 random selection ≈ VLA-only。\"}, \"eval-obs-only-object-norm02-seed48-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T10:33:11.557Z\", \"updated_at\": \"2026-05-18T10:34:35.629Z\", \"hypothesis\": \"obs_only CRM (ε=0.2) seed48 on LIBERO-Object. Retry after killed previous attempt. Supplements primary result (seed42-47 done, this extends to seed48).\", \"spec\": {\"command\": \"crm_obs_only --seed 48 --K 10 --max_correction_norm 0.2\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"796900\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 48, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}}, \"eval-obs-only-object-norm01-seed46-r3\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T10:33:39.698Z\", \"updated_at\": \"2026-05-18T10:34:33.777Z\", \"hypothesis\": \"obs_only CRM (ε=0.1) seed46 on LIBERO-Object. Retry r3. Supplements magnitude curve ε=0.1 data. seed42=19%, seed43=12%, seed44=16%, seed45=14%.\", \"spec\": {\"command\": \"crm_obs_only --seed 46 --K 10 --max_correction_norm 0.1\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"562396\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}}, \"eval-obs-only-object-norm005-seed45\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T10:33:08.510Z\", \"updated_at\": \"2026-05-18T10:34:31.217Z\", \"hypothesis\": \"obs_only CRM (ε=0.05) seed45 on LIBERO-Object. Supplements magnitude curve low-norm data. seed42=13%, seed43=14%.\", \"spec\": {\"command\": \"crm_obs_only --seed 45 --K 10 --max_correction_norm 0.05\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"565173\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}}, \"eval-perdof-object-norm01-seed43\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T01:29:55.249Z\", \"updated_at\": \"2026-05-18T10:32:48.246Z\", \"spec\": {\"command\": \"crm_perdof --seed 43 --K 10 --max_correction_norm 0.1\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"571010\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm01-seed43.log\", \"submitted_at\": \"2026-05-18T01:29:54.691Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_perdof\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}}, \"eval-perdof-object-norm02-seed43\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:36:46.839Z\", \"updated_at\": \"2026-05-18T10:32:46.245Z\", \"hypothesis\": \"perdof CRM ε=0.2 seed43 on LIBERO-Object. 补充 perdof magnitude curve ε=0.2 数据（seed42=11%, seed43 之前仅 spatial 数据 9%）。与 obs_only ε=0.2 seed43=16% 配对对比。\", \"spec\": {\"command\": \"crm_perdof --seed 43 --K 10 --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"535595\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_perdof\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}}, \"eval-obs-only-object-norm005-seed44\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-17T23:10:56.103Z\", \"updated_at\": \"2026-05-18T10:32:41.861Z\", \"spec\": {\"command\": \"crm_obs_only --seed 44 --K 10 --max_correction_norm 0.05\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"549432\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm005-seed44.log\", \"submitted_at\": \"2026-05-17T23:10:55.072Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}, \"hypothesis\": \"obs_only CRM (ε=0.05) seed44 on LIBERO-Object. 补充 Figure 2 低 norm 段数据。seed42=13%, seed43 running。\"}, \"eval-perdof-object-norm02-seed48\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-17T23:05:24.390Z\", \"updated_at\": \"2026-05-18T10:32:39.509Z\", \"spec\": {\"command\": \"crm_perdof --seed 48 --K 10 --max_correction_norm 0.2\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:5\"], \"pid\": \"488665\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm02-seed48.log\", \"submitted_at\": \"2026-05-17T23:05:23.874Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_perdof\", \"seed\": 48, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}, \"hypothesis\": \"perdof CRM (ε=0.2) seed48 on LIBERO-Object. 补充 magnitude curve ε=0.2 数据，扩展 error bars。\"}, \"eval-random-selection-object-seed43\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-17T23:10:52.130Z\", \"updated_at\": \"2026-05-18T10:32:34.784Z\", \"spec\": {\"command\": \"random_selection --seed 43 --K 10\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"pid\": \"492545\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-random-selection-object-seed43.log\", \"submitted_at\": \"2026-05-17T23:15:07.123Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"random_selection\", \"seed\": 43, \"eval_data\": \"LIBERO-Object\"}, \"hypothesis\": \"Random selection baseline (K=10 随机选一个 action) seed43 on LIBERO-Object. 多 seed 验证 CRM selection > random。seed42 RUNNING 中。\"}, \"eval-perdof-object-default-seed43\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T06:17:50.362Z\", \"updated_at\": \"2026-05-18T10:31:11.231Z\", \"hypothesis\": \"Perdof CRM without norm clipping (uncapped, actual norm ~1.42) causes catastrophic collapse on LIBERO-Object. seed42=0%, seed46=0%, seed44=0% (partial). seed43 confirms cross-seed consistency of collapse.\", \"spec\": {\"command\": \"bash -c \\\"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_object_perdof_default_seed43.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"832702\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-default-seed43.log\", \"submitted_at\": \"2026-05-18T10:31:01.993Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_perdof\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\"}}, \"eval-obs-only-object-norm02-k5-seed44\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T10:27:12.596Z\", \"updated_at\": \"2026-05-18T10:27:15.044Z\", \"hypothesis\": \"obs_only CRM K=5 ε=0.2 seed44. Third seed for K-value curve (seed42=14%, seed43 RUNNING). Strengthens K=5 data point statistics.\"}, \"eval-perdof-object-norm01-seed46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T06:51:19.181Z\", \"updated_at\": \"2026-05-18T07:05:38.605Z\", \"hypothesis\": \"perdof CRM (ε=0.1) seed=46 on LIBERO Object. Extends perdof low-norm data (seed42=11%, seed44/45 running). At ε=0.1 perdof is in its \\\"safe zone\\\" (tight bound masks noisy corrections). Paired with obs_only seed46 for direct comparison at same seed.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_perdof_norm01_seed46.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"393633\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed46.json\", \"submitted_at\": \"2026-05-17T06:51:36.171Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_perdof_v3_norm\", \"seed\": 46, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"checkpoint_path\": \"N/A\", \"wall_clock_seconds\": 87240.0, \"gpu_hours\": 24.23}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-18T07:05:36.145Z\", \"metrics\": {\"overall_success_rate\": 0.1}}, \"eval-obs-only-object-norm01-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T09:01:52.970Z\", \"updated_at\": \"2026-05-18T07:05:03.603Z\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 python src/evaluate.py --mode crm_obs_only --max_correction_norm 0.1 --k 10 --seed 45 --benchmark object --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_norm01_seed45.json > logs/eval_object_obs_only_norm01_seed45.log 2>&1\", \"server\": \"bjb1-18228\", \"gpu_id\": \"cuda:0\", \"model_name\": \"crm_obs_only\", \"seed\": 45, \"data_path\": \"LIBERO object benchmark\", \"data_count\": -1, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object\", \"hypothesis\": \"obs_only CRM norm=0.1 seed=45 on LIBERO object. Multi-seed magnitude curve data point. seed42=19%.\"}, \"pid\": 474319, \"hypothesis\": \"obs_only CRM (ε=0.1) seed=45 on LIBERO Object. 验证 obs_only 在低 norm (0.1) 的稳定性。seed42 在 0.1 为 19%，如果一致则确认 obs_only 全 norm 范围鲁棒。\", \"conclusion\": \"success\", \"notes\": \"PID 474319 died, GPU idle 28h+. Ghost experiment — process dead but registry not updated.\", \"completed_at\": \"2026-05-17T13:31:33.316Z\", \"metrics\": {\"overall_success_rate\": 0.14}}, \"eval-obs-only-object-norm02-k5-seed42\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-17T13:34:40.971Z\", \"updated_at\": \"2026-05-18T07:05:02.646Z\", \"hypothesis\": \"obs_only CRM (ε=0.2, K=5) seed42 on LIBERO-Object. K sweep 实验：K=5 vs K=10 (22%) 比较，验证 sample count 对 selection quality 的影响。若 K=5 显著低于 K=10，说明足够的 candidate 多样性对 CRM selection 关键。\", \"reproduce\": {\"finished_at\": \"2026-05-17T18:32:21.424Z\"}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"completed_at\": \"2026-05-17T18:32:28.770Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T18:32:40.928533+00:00\"}], \"previous_failure\": {\"conclusion\": \"killed\"}}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 5 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_k5_seed42.json\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only_v3_norm\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\"}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.14}}, \"eval-perdof-object-default-seed46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:21:54.338Z\", \"updated_at\": \"2026-05-18T07:05:01.672Z\", \"hypothesis\": \"perdof CRM (default norm, 无裁剪) seed46 on LIBERO-Object. 验证 perdof 在 uncapped norm 下的灾难性崩溃（seed42=0%）是否跨 seed 一致。支撑 obs_only > perdof claim。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_object_perdof_default_seed46.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": 423767, \"seed\": 46, \"model_name\": \"SmolVLA+CRM_perdof\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_seed46.json\", \"checkpoint_path\": \"N/A\", \"metrics\": {\"overall_sr\": 0, \"per_task_sr\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 0, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0}}}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-18T01:27:04.768Z\", \"metrics\": {\"overall_success_rate\": 0}}, \"eval-perdof-object-default-seed44\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-16T07:18:01.200Z\", \"updated_at\": \"2026-05-18T06:19:59.229Z\", \"hypothesis\": \"perdof CRM (default norm ~1.42) seed=44 on LIBERO Object. 验证 perdof 在 uncapped norm 下的 catastrophic collapse（seed42=0%）。为 magnitude curve 提供第二个 seed 的 default 数据点。\", \"reproduce\": {\"finished_at\": \"2026-05-17T07:20:12.857Z\"}, \"failure_reason\": \"EXIT_CODE=124 (timeout — exceeded timeout_hours)\", \"completed_at\": \"2026-05-17T07:20:15.008Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T07:20:19.307187+00:00\"}], \"previous_failure\": {\"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0, \"total_successes\": 0, \"total_rollouts\": 90, \"tasks_completed\": 9, \"note\": \"Task 10 not started due to 24h timeout. 0/90 rollouts succeeded. Catastrophic collapse at unclipped norm.\", \"seed\": 44, \"mode\": \"crm_perdof\", \"benchmark\": \"object\", \"max_correction_norm\": \"default (~1.42)\"}, \"notes\": \"Timeout (EXIT_CODE=124, 24h) but partial results conclusive: 0/90 rollouts = 0% SR across 9/10 tasks. Task 10 not started. Confirms catastrophic collapse at unclipped norm, consistent with seed42=0%. Every rollout hit max_steps=300 (agent unable to complete any task), causing the timeout.\"}}, \"notes\": \"Timeout (EXIT_CODE=124, 24h) but partial results conclusive: 0/90 rollouts = 0% SR across 9/10 tasks. Task 10 not started. Confirms catastrophic collapse at unclipped norm, consistent with seed42=0%. Every rollout hit max_steps=300 (agent unable to complete any task), causing the timeout.\", \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0, \"total_successes\": 0, \"total_rollouts\": 90, \"tasks_completed\": 9, \"note\": \"Partial 9/10 tasks, 0/90 rollouts. Accepted as collapse evidence per Director decision 2026-05-18.\"}, \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"partial results from previous run, 0/90 rollouts across 9/10 tasks\", \"server\": \"autodl-4090 (previous run)\", \"command\": \"python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"model_name\": \"crm_perdof\", \"seed\": 44, \"data_path\": \"LIBERO-Object\", \"data_count\": 90}}, \"eval-perdof-object-default-seed45\": {\"status\": \"PREPARING\", \"retry_count\": 1, \"created_at\": \"2026-05-16T20:21:08.043Z\", \"updated_at\": \"2026-05-18T06:17:54.050Z\", \"completed_at\": \"2026-05-17T02:54:38.157Z\", \"hypothesis\": \"Per-DoF CRM with default norm on LIBERO-Object seed=45 validates cross-seed consistency of per-DoF correction — paired with seed42/43/44 to assess variance of correction-based methods vs baseline\", \"parent\": \"crm-train-v2-perdof\", \"extra\": {\"previous_failure\": {\"conclusion\": \"killed\", \"metrics\": {\"kill_reason\": \"Sacrificed for P0 direct-correction experiment (no free GPU). Was at task 5/10 after 6h. Expected result: 0% (confirmed by seed42=0%, seed44 running on autodl-4090).\", \"partial_progress\": \"5/10 tasks, bbq_sauce 0% success\"}}}}, \"eval-mag-perdof-norm02\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:16:13.281Z\", \"updated_at\": \"2026-05-18T05:54:22.364Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode acr_vla --max_correction_norm 0.2 --n_rollouts 10 --K 10 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_mag_perdof_norm02.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"SmolVLA + CRM-v3-norm-perdof\", \"seed\": 42, \"checkpoint_source\": \"crm-train-v3-norm-perdof\", \"eval_data\": \"LIBERO spatial\"}, \"gpu\": \"bjb2-28827:cuda:2\", \"pid\": 13728, \"metrics\": {\"tasks_done\": \"6/10\", \"partial_results\": {\"T0_between_plate_ramekin\": \"60%\", \"T1_next_to_ramekin\": \"90%\", \"T2_table_center\": \"0%\", \"T3_on_cookie_box\": \"20%\", \"T4_top_drawer\": \"0%\", \"T5_on_ramekin\": \"0%\"}, \"running_avg_6task\": \"28.3%\", \"snapshot_time\": \"2026-05-15T09:00:00Z\", \"server\": \"bjb2-28827\", \"process_status\": \"alive\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T17:30:14.331Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T17:30:15.807Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:30:23.476790+00:00\"}]}, \"hypothesis\": \"Per-DoF CRM with max_correction_norm=0.2 on LIBERO-Spatial achieves optimal balance between correction magnitude and stability — norm=0.2 is hypothesized sweet spot from obs-only results\", \"parent\": \"eval-acr-spatial-v3\"}, \"eval-acr-spatial-v4-scalar\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:15:49.209Z\", \"updated_at\": \"2026-05-18T05:54:21.341Z\", \"hypothesis\": \"D020: scalar_unc CRM (val_loss 0.0374) with max_correction_norm=0.1. Three-way ablation: perdof vs scalar_unc vs obs_only under identical correction magnitude.\", \"spec\": {\"hypothesis\": \"D020 三路消融：scalar_unc CRM v3-norm (val_loss 0.0374) with max_correction_norm=0.1. 与 perdof (cuda:3) 和 obs_only (cuda:0) 同条件对比，判断 per-DOF vs scalar conformal features 的增益\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v3-norm scalar_unc, max_correction_norm=0.1)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"command\": \"python -u src/evaluate.py --mode crm_scalar --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": 288939, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-scalar.log\", \"gpu_ids\": [\"cuda:2\"]}, \"metrics\": {\"tasks_done\": \"3/10\", \"partial_results\": {\"between_plate_and_ramekin\": \"60.0% (6/10)\", \"next_to_ramekin\": \"100.0% (10/10)\", \"from_table_center\": \"10.0% (1/10)\"}, \"running_avg_3tasks\": \"56.7% (17/30)\", \"snapshot_time\": \"2026-05-15T12:00:00Z\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:2\", \"pid\": 288939}, \"notes\": \"[2026-05-15] HUNG: 3/10 tasks done (56.7%, 17/30), stuck on task 4 env init for 8+ hours. Process alive (pid 288939, GPU 1450 MiB) but zero log progress. Needs kill+restart.\", \"reproduce\": {\"finished_at\": \"2026-05-15T04:57:54.647Z\"}, \"failure_reason\": \"Kill-restart Worker 在 Director 撤销 kill 指令前已执行 SIGTERM (EXIT_CODE=143)。D026 kill 指令已被撤销但来不及阻止。\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T04:57:55.887Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T04:57:57.857060+00:00\"}]}}, \"eval-acr-spatial-v4-small\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:09:00.358Z\", \"updated_at\": \"2026-05-18T05:54:20.300Z\", \"hypothesis\": \"D018: Normalization + moderate correction scaling (max_correction_norm=0.1, 14x smaller than default). If v4-small > v4-default → magnitude control needed on top of normalization.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1\", \"server\": \"bjb1-18228\", \"gpu_ids\": [\"cuda:3\"], \"pid\": 253085, \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v3-norm per-DOF, max_correction_norm=0.1)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"log_path\": \"/root/autodl-tmp/logs/eval_acr_spatial_v4_small.log\"}, \"metrics\": {\"tasks_done\": \"7/10\", \"partial_results\": {\"between_plate_and_ramekin\": \"60.0% (6/10)\", \"next_to_ramekin\": \"100.0% (10/10)\", \"from_table_center\": \"10.0% (1/10)\", \"on_cookie_box\": \"40.0% (4/10)\", \"in_top_drawer\": \"0.0% (0/10)\", \"on_ramekin\": \"0.0% (0/10)\", \"next_to_cookie_box\": \"90.0% (9/10)\"}, \"running_avg_7tasks\": \"42.9% (30/70)\", \"snapshot_time\": \"2026-05-15T12:00:00Z\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:3\", \"pid\": 253085}, \"notes\": \"[2026-05-15 corrected] 之前误判为 env init hang，实际是被 kill-restart Worker SIGTERM kill。日志无 error/traceback，符合 SIGTERM 特征。7/10 tasks 完成，42.9% SR (30/70)。需重跑 tasks 8-10（或全部重跑）。\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T05:04:16.712Z\", \"failure_reason\": \"被 kill-restart Worker SIGTERM（Director 撤销 kill 指令前已执行）。完成 7/10 tasks 后在 task 8 启动前被 kill。\"}, \"eval-acr-spatial-v4-obs-only-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:16:06.636Z\", \"updated_at\": \"2026-05-18T05:54:19.300Z\", \"hypothesis\": \"D020: obs_only CRM v3-norm (val_loss 0.0165) with max_correction_norm=0.1. If obs_only >= v4-small (perdof) → Claim 1 needs restructuring. If obs_only < v4-small → conformal features have unique value under distribution shift.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"270097\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-obs-only-r2.log\", \"submitted_at\": \"2026-05-14T22:21:35.775Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_ids\": [\"cuda:0\"], \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v3-norm obs_only, max_correction_norm=0.1)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 24161.7, \"gpu_hours\": 6.71}, \"metrics\": {\"tasks_done\": \"6/10\", \"partial_results\": {\"between_plate_and_ramekin\": \"90.0% (9/10)\", \"next_to_ramekin\": \"100.0% (10/10)\", \"from_table_center\": \"0.0% (0/10)\", \"on_cookie_box\": \"40.0% (4/10)\", \"in_top_drawer\": \"10.0% (1/10)\", \"on_ramekin\": \"0.0% (0/10)\"}, \"running_avg_6tasks\": \"40.0% (24/60)\", \"snapshot_time\": \"2026-05-15T12:00:00Z\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:0\", \"pid\": 270097}, \"notes\": \"[2026-05-15 corrected] 之前误判为 env hang，实际是被 kill-restart Worker SIGTERM kill。日志无 error/traceback，符合 SIGTERM 特征。6/10 tasks 完成 + task 7 部分（5/10 rollouts），40.0% SR (24/60)。需重跑。\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T05:04:17.448Z\", \"failure_reason\": \"被 kill-restart Worker SIGTERM（Director 撤销 kill 指令前已执行）。完成 6/10 tasks，第 7 个 task (next_to_cookie_box) rollout 5/10 时被 kill。\"}, \"eval-argmin-only-spatial\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:47:58.683Z\", \"updated_at\": \"2026-05-18T05:54:18.227Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark spatial --n_rollouts 10 --seed 42 --K 10\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"231421\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-only-spatial.log\", \"submitted_at\": \"2026-05-14T17:47:58.583Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_ids\": [\"cuda:1\"], \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"SmolVLA K=10 argmin selection (no CRM correction)\", \"seed\": 42, \"hypothesis\": \"Isolate argmin base action selection from CRM correction. If argmin-only ≈ VLA mean (40%), CRM delta is the sole culprit. If argmin-only << VLA mean, argmin selection itself is problematic.\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 40187.5, \"gpu_hours\": 11.16}, \"metrics\": {\"tasks_done\": \"9/10\", \"partial_results\": {\"between_plate_and_ramekin\": \"60.0% (6/10)\", \"next_to_ramekin\": \"100.0% (10/10)\", \"from_table_center\": \"0.0% (0/10)\", \"on_cookie_box\": \"30.0% (3/10)\", \"in_top_drawer\": \"10.0% (1/10)\", \"on_ramekin\": \"10.0% (1/10)\", \"next_to_cookie_box\": \"90.0% (9/10)\", \"on_stove\": \"0.0% (0/10)\", \"next_to_plate\": \"30.0% (3/10)\"}, \"running_avg_9tasks\": \"36.7% (33/90)\", \"snapshot_time\": \"2026-05-15T12:00:00Z\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"pid\": 231421}, \"notes\": \"[2026-05-15] HUNG: 9/10 tasks done (36.7%, 33/90), stuck on task 10 env init for 8+ hours. Process alive (pid 231426, GPU 1414 MiB) but zero log progress. Needs kill+restart.\", \"reproduce\": {\"finished_at\": \"2026-05-15T04:57:45.148Z\"}, \"failure_reason\": \"Kill-restart Worker 在 Director 撤销 kill 指令前已执行 SIGTERM (EXIT_CODE=143)。D026 kill 指令已被撤销但来不及阻止。\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T04:57:46.099Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T04:57:50.175181+00:00\"}]}, \"hypothesis\": \"Argmin-only selection (K=10, pick lowest CRM score without correction) on LIBERO-Spatial tests whether selection alone provides benefit — isolating the selection mechanism from the correction mechanism\", \"parent\": \"eval-reconvla-spatial-v3\"}, \"eval-acr-spatial-v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:17:06.073Z\", \"updated_at\": \"2026-05-18T05:54:17.209Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v2/perdof/crm_best.pt\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"197057\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v3.log\", \"submitted_at\": \"2026-05-14T12:17:05.974Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial benchmark)\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v2 per-DOF + SmolVLA K=10)\", \"seed\": 42, \"hypothesis\": \"Per-DOF conformal correction (ACR-VLA with D016 4-bug fix) outperforms VLA K=1 (30%) and SampleConsensus (34%) on LIBERO spatial. CORE CLAIM experiment.\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v2/perdof/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 28899.4, \"gpu_hours\": 8.03}, \"metrics\": {\"tasks_done\": \"4/10\", \"overall_success_rate\": 0.025, \"total_successes\": 1, \"total_rollouts\": 40, \"per_task_partial\": {\"pick_up_black_bowl_between_plate_and_ramekin\": 0.1, \"pick_up_black_bowl_next_to_ramekin\": 0, \"pick_up_black_bowl_from_table_center\": 0, \"pick_up_black_bowl_on_cookie_box\": 0}, \"snapshot_time\": \"2026-05-14T18:15Z\"}, \"conclusion\": \"success\", \"reproduce\": {\"finished_at\": \"2026-05-14T20:18:44.725Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-14T20:18:45.380Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T20:18:46.631294+00:00\"}]}, \"hypothesis\": \"ACR pipeline v3 (K=10 conformal selection) on LIBERO-Spatial improves over VLA-only baseline, validating that conformal selection generalizes across spatial reasoning tasks\", \"parent\": \"crm-train-v2-perdof\"}, \"eval-acr-object-v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:17:13.095Z\", \"updated_at\": \"2026-05-18T05:54:16.171Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode acr_vla --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v2/perdof/crm_best.pt\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"197803\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v3.log\", \"submitted_at\": \"2026-05-14T12:17:13.006Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/ (object benchmark)\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v2 per-DOF + SmolVLA K=10)\", \"seed\": 42, \"hypothesis\": \"Per-DOF conformal correction generalizes from spatial to object benchmark — cross-benchmark validation of ACR-VLA.\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v2/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 28901.2, \"gpu_hours\": 8.03}, \"metrics\": {\"tasks_done\": \"4/10\", \"overall_success_rate\": 0, \"total_successes\": 0, \"total_rollouts\": 40, \"per_task_partial\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0, \"bbq_sauce\": 0}, \"snapshot_time\": \"2026-05-14T18:15Z\"}, \"conclusion\": \"negative\", \"reproduce\": {\"finished_at\": \"2026-05-14T20:18:53.408Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-14T20:18:54.185Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T20:18:55.466058+00:00\"}]}, \"hypothesis\": \"ACR pipeline v3 (K=10 conformal selection with scalar uncertainty) on LIBERO-Object improves over VLA-only baseline by selecting highest-confidence action from candidate set\", \"parent\": \"crm-train-v2-perdof\"}, \"eval-openvla-object-vla-only-seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T15:56:51.046Z\", \"updated_at\": \"2026-05-18T05:54:15.084Z\", \"spec\": {\"command\": \"python -u src/openvla_eval.py --mode vla_only --benchmark object --n_rollouts 10 --seed 42 --K 1 --gpu 0 --model_path /root/autodl-tmp/models/openvla-libero-object\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"667642\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-openvla-object-vla-only-seed42.log\", \"submitted_at\": \"2026-05-17T15:57:37.232Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"OpenVLA-7B-libero-object\", \"seed\": 42, \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"checkpoint_source\": \"/root/autodl-tmp/models/openvla-libero-object\", \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 7512.0, \"gpu_hours\": 2.09}, \"hypothesis\": \"OpenVLA 7B VLA-only baseline on LIBERO-Object. 0% SR due to transformers 5.8 DynamicCache bug. Fix: use official repo eval code with transformers 4.40.1 in isolated conda env. Dry-run verified 80% SR on libero_spatial. Awaiting GPU for full LIBERO-Object eval.\", \"reproduce\": {\"finished_at\": \"2026-05-17T18:01:16.139Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T18:01:26.464150+00:00\"}]}, \"conclusion\": \"negative\", \"metrics\": {\"overall_success_rate\": 0, \"total_successes\": 0, \"total_rollouts\": 100, \"avg_inference_time_ms\": 178, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 0, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0}}, \"completed_at\": \"2026-05-17T18:02:49.250Z\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-openvla-object-vla-only-seed42.log\", \"notes\": \"NEEDS INVESTIGATION: 0% success rate vs OpenVLA paper 88.4% (LIBERO-Object). 100% confirmed code bug. Suspected action tokenization/detokenization or unnormalize issue. Do NOT treat as valid baseline.\"}, \"eval-obs-only-object-norm02-k5-seed43\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T04:37:18.401Z\", \"updated_at\": \"2026-05-18T04:37:38.252Z\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 43 --K 5 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_k5_seed43.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"527465\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-k5-seed43.log\", \"submitted_at\": \"2026-05-18T04:37:17.870Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 43, \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}, \"hypothesis\": \"obs_only CRM K=5 ε=0.2 seed43. Second seed for K-value curve (seed42=14%). Director highest priority.\"}, \"eval-perdof-object-norm02-seed47\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T13:32:28.585Z\", \"updated_at\": \"2026-05-18T04:37:10.886Z\", \"hypothesis\": \"perdof CRM with ε=0.2 on LIBERO-Object seed47. Magnitude curve data point for perdof at primary comparison norm.\", \"spec\": {\"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"404983\", \"command\": \"/root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed47.json\", \"model_name\": \"SmolVLA+CRM_perdof\", \"seed\": 47, \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed47.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T04:37:04.589Z\", \"metrics\": {\"overall_sr\": 0.11, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}}, \"eval-obs-only-object-norm02-seed48\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T23:05:21.870Z\", \"updated_at\": \"2026-05-18T03:04:35.124Z\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 48 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_seed48.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"796895\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-seed48.log\", \"submitted_at\": \"2026-05-18T03:04:34.555Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"obs_only CRM ε=0.2 seed48. Key data point at primary comparison norm.\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-17T23:12:19.723Z\"}, \"eval-obs-only-object-default-seed46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:21:52.326Z\", \"updated_at\": \"2026-05-18T03:03:50.286Z\", \"hypothesis\": \"obs_only CRM without norm constraint (uncapped correction magnitude) on LIBERO-Object seed46. Tests whether obs_only maintains performance without explicit correction capping.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_default_seed46.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": 422357, \"seed\": 46, \"model_name\": \"SmolVLA+CRM_obs_only\", \"data_path\": \"LIBERO-Object 10 tasks\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed46.json\", \"checkpoint_path\": \"N/A\"}, \"reproduce\": {\"finished_at\": \"2026-05-18T00:20:44.089Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T00:20:46.904Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T00:20:52.370655+00:00\"}]}, \"metrics\": {\"overall_sr\": 0.15, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}}, \"eval-perdof-object-norm01-seed42-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T02:32:26.297Z\", \"updated_at\": \"2026-05-18T02:33:07.050Z\", \"hypothesis\": \"perdof CRM with max_correction_norm=0.1 on LIBERO-Object seed42. Rerun of failed eval-perdof-object-norm01-seed42. PID 497642 on cuda:3, started 07:52 UTC.\", \"parent\": \"eval-perdof-object-norm01-seed42\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_perdof_norm01_seed42.json\", \"server\": \"bjb2-28827\", \"data_path\": \"/root/acr-vla-conformal-refinement/src/evaluate.py\", \"data_count\": \"10 rollouts x 10 tasks\", \"model_name\": \"crm_perdof\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}}, \"eval-obs-only-object-norm01-seed42-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T02:32:25.342Z\", \"updated_at\": \"2026-05-18T02:33:03.686Z\", \"hypothesis\": \"obs_only CRM with max_correction_norm=0.1 on LIBERO-Object seed42. Rerun of failed eval-obs-only-object-norm01-seed42. PID 497445 on cuda:1, started 07:52 UTC.\", \"parent\": \"eval-obs-only-object-norm01-seed42\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_obs_only_norm01_seed42.json\", \"server\": \"bjb2-28827\", \"data_path\": \"/root/acr-vla-conformal-refinement/src/evaluate.py\", \"data_count\": \"10 rollouts x 10 tasks\", \"model_name\": \"crm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}}, \"eval-perdof-object-norm01-seed42\": {\"status\": \"DEPLOYED\", \"retry_count\": 0, \"created_at\": \"2026-05-17T23:53:01.705Z\", \"updated_at\": \"2026-05-18T02:31:45.337Z\", \"hypothesis\": \"perdof CRM with ε=0.1 on LIBERO-Object seed42. Magnitude curve comparison point for perdof variant.\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_perdof_norm01_seed42.json\", \"server\": \"bjb2-28827\", \"data_path\": \"/root/acr-vla-conformal-refinement/src/evaluate.py\", \"data_count\": \"10 rollouts x 10 tasks\", \"model_name\": \"crm_perdof\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-18T02:11:22.573Z\"}, \"eval-obs-only-object-norm01-seed42\": {\"status\": \"DEPLOYED\", \"retry_count\": 0, \"created_at\": \"2026-05-17T23:53:00.645Z\", \"updated_at\": \"2026-05-18T02:31:42.546Z\", \"hypothesis\": \"obs_only CRM with ε=0.1 on LIBERO-Object seed42. Intermediate norm point for magnitude curve.\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_obs_only_norm01_seed42.json\", \"server\": \"bjb2-28827\", \"data_path\": \"/root/acr-vla-conformal-refinement/src/evaluate.py\", \"data_count\": \"10 rollouts x 10 tasks\", \"model_name\": \"crm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-18T02:11:19.115Z\"}, \"eval-perdof-object-norm02-seed46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T10:54:38.275Z\", \"updated_at\": \"2026-05-18T02:24:22.787Z\", \"hypothesis\": \"perdof CRM with ε=0.2 on LIBERO-Object seed46. Magnitude curve data point for perdof variant at primary comparison norm.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed46.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"pid\": 389051, \"seed\": 46, \"model_name\": \"SmolVLA+CRM_perdof\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed46.json\", \"checkpoint_path\": \"N/A\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T02:24:14.354Z\", \"metrics\": {\"overall_sr\": 0.09, \"successes\": 9, \"rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}}, \"eval-obs-only-object-norm01-seed46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T06:51:13.356Z\", \"updated_at\": \"2026-05-18T01:01:03.202Z\", \"hypothesis\": \"obs_only CRM (ε=0.1) seed=46 on LIBERO Object. Extends magnitude curve low-norm segment to 3+ seeds. If consistent with seed42=19% and seed45 (running), strengthens robustness claim that obs_only maintains stable performance across all ε values.\", \"spec\": {\"command\": \"python evaluate.py --benchmark object --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --seed 46 --output_file logs/eval_object_obs_only_norm01_seed46.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"590833\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed46.log\", \"submitted_at\": \"2026-05-17T06:54:14.775Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A\", \"seed\": 46, \"wall_clock_seconds\": 65208.4, \"gpu_hours\": 18.11}, \"conclusion\": \"failed\", \"reproduce\": {\"finished_at\": \"2026-05-18T01:00:59.710Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-18T01:01:03.202Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T01:01:13.372128+00:00\"}]}}, \"eval-obs-only-object-norm005-seed43-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T13:32:27.742Z\", \"updated_at\": \"2026-05-18T00:42:42.174Z\", \"hypothesis\": \"obs_only CRM with ε=0.05 on LIBERO-Object seed43. Retry (r2) for magnitude curve low-norm data point.\", \"spec\": {\"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"433500\", \"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_obs_only_norm005_seed43_r2.json\", \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 43, \"data_path\": \"LIBERO-Object 10 tasks\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed43_r2.json\", \"checkpoint_path\": \"N/A\"}, \"metrics\": {\"overall_sr\": 0.14, \"successes\": 14, \"rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T00:42:42.174Z\"}, \"eval-obs-only-object-norm01-seed46-r2\": {\"status\": \"DEPLOYED\", \"retry_count\": 0, \"created_at\": \"2026-05-17T07:05:18.047Z\", \"updated_at\": \"2026-05-18T00:33:26.447Z\", \"hypothesis\": \"obs_only CRM with ε=0.1 on LIBERO-Object seed46. Retry after previous run was killed at task 5/10.\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_obs_only_norm01_seed46.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": 562396, \"seed\": 46, \"model_name\": \"SmolVLA+CRM_obs_only\", \"data_path\": \"LIBERO-Object 10 tasks\", \"data_count\": 100, \"eval_data\": \"LIBERO-Object\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-17T13:31:53.068Z\", \"notes\": \"Retry #2: relaunched on bjb1-32546 cuda:3, PID 562396, tmux session eval-obs-only-object-norm01-seed46-r2. Previous run killed at task 5/10 on bjb1-18228.\"}, \"mag_obs_only_norm01_seed47\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T18:04:31.864Z\", \"updated_at\": \"2026-05-17T23:47:05.521Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_obs_only_norm01_seed47.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"pid\": \"448773\", \"log_path\": \"N/A (killed as orphan)\", \"submitted_at\": \"2026-05-17T18:04:30.652Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_count\": 100, \"data_path\": \"LIBERO-Object 10tasks×10rollouts\", \"model_name\": \"crm_obs_only + SmolVLA\", \"seed\": 47, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"wall_clock_seconds\": 20554.9, \"gpu_hours\": 5.71}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-17T23:47:05.521Z\"}, \"mag_obs_only_norm01_seed46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T18:04:34.999Z\", \"updated_at\": \"2026-05-17T23:47:03.765Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_obs_only_norm01_seed46.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"449059\", \"log_path\": \"N/A (killed as orphan)\", \"submitted_at\": \"2026-05-17T18:04:34.274Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_count\": 100, \"data_path\": \"LIBERO-Object 10tasks×10rollouts\", \"model_name\": \"crm_obs_only + SmolVLA\", \"seed\": 46, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"wall_clock_seconds\": 20549.5, \"gpu_hours\": 5.71}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-17T23:47:03.765Z\"}, \"eval_obs_only_norm01_seed48\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-17T22:59:51.090Z\", \"updated_at\": \"2026-05-17T23:46:33.880Z\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 48 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_obs_only_norm01_seed48.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"774337\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval_obs_only_norm01_seed48.log\", \"submitted_at\": \"2026-05-17T22:59:50.463Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"eval_obs_only_norm03_seed48\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-17T22:59:53.216Z\", \"updated_at\": \"2026-05-17T23:46:32.828Z\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 48 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03_seed48.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"774538\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval_obs_only_norm03_seed48.log\", \"submitted_at\": \"2026-05-17T22:59:52.629Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"train-crm-k1-accg-object-seed42-full\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-17T15:40:51.279Z\", \"updated_at\": \"2026-05-17T23:44:07.117Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement/src && CUDA_VISIBLE_DEVICES=0 python -u train_crm_k1.py --benchmark object --epochs 50 --batch_size 512 --lr 1e-3 --seed 42 --loss_mode multi --lambda_dir 0.1 --lambda_tri 0.05 --lambda_mag 0.01 --max_correction_norm 0.2 --wandb_project acr-vla-conformal-refinement --wandb_run_name crm-k1-v2-accg-multistage-object --auto 2>&1 | tee /root/acr-vla-conformal-refinement/logs/train_crm_k1_full.log\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"pid\": \"434871\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/train-crm-k1-accg-object-seed42-full.log\", \"submitted_at\": \"2026-05-17T15:40:50.814Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"plan_701-crm-k1-train\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-17T14:04:14.203Z\", \"updated_at\": \"2026-05-17T23:44:06.175Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && mkdir -p /root/autodl-tmp/checkpoints/crm_k1 && CUDA_VISIBLE_DEVICES=1 python -u src/train_crm_k1.py --auto --benchmark spatial --epochs 50 --batch_size 512 --lr 1e-3 --wandb_project acr-vla-conformal-refinement --wandb_run_name crm-k1-train-spatial --precompute_batch_size 4 --output_dir /root/autodl-tmp/checkpoints/crm_k1/ 2>&1 | tee logs/train_crm_k1.log\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"pid\": \"422526\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/plan_701-crm-k1-train.log\", \"submitted_at\": \"2026-05-17T14:04:13.752Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"K=1 CRM 训练：使用多阶段 VLA 特征融合 + 组合损失函数（L2 + contrastive + uncertainty-weighted），训练专门用于 K=1 单采样纠正的 CRM 模型。目标是超越 K=1 VLA-only baseline (10.8%)。\", \"conclusion\": \"killed\"}, \"plan_701-precompute-k1-spatial\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-17T14:11:43.484Z\", \"updated_at\": \"2026-05-17T23:44:05.159Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 python -u src/precompute_k1.py --benchmark spatial --batch_size 4 --cache_dir /root/autodl-tmp/crm_cache_k1/ 2>&1 | tee logs/precompute_k1.log\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"649967\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/plan_701-precompute-k1-spatial.log\", \"submitted_at\": \"2026-05-17T14:11:42.695Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm03-seed46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T10:28:22.831Z\", \"updated_at\": \"2026-05-17T23:30:58.329Z\", \"hypothesis\": \"obs_only CRM at eps=0.3 on seed46 extends magnitude curve high-norm data. seed42=19%, seed44=18%, seed45=14%. 4th seed at this norm.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --seed 46 --benchmark object --n_rollouts 10 --output_file logs/eval_object_obs_only_norm03_seed46.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"416568\", \"seed\": 46, \"model_name\": \"SmolVLA+CRM_obs_only\", \"data_path\": \"LIBERO-Object 10 tasks\", \"data_count\": 100, \"eval_data\": \"LIBERO-Object\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"max_correction_norm\": 0.3, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed46.json\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}, \"metrics\": {\"overall_sr\": 0.17, \"successes\": 17, \"total\": 100}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T23:30:58.329Z\"}, \"eval-obs-only-object-norm005-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T13:32:15.980Z\", \"updated_at\": \"2026-05-17T23:17:56.045Z\", \"hypothesis\": \"obs_only CRM (ε=0.05) seed43 on LIBERO-Object. M006 补救：补充 magnitude curve 低 norm 段多 seed 数据。seed42 ε=0.05=13%。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval-obs-only-object-norm005-seed43.json 2>&1 | tee logs/eval-obs-only-object-norm005-seed43.log\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"631667\", \"log_path\": \"N/A (killed, superseded by r2/r3)\", \"submitted_at\": \"2026-05-17T13:32:57.943Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"wall_clock_seconds\": 35098.1, \"gpu_hours\": 9.75}, \"conclusion\": \"killed\", \"notes\": \"Superseded by eval-obs-only-object-norm005-seed43-r2 (bjb1-32546) and r3 (bjb1-18228)\", \"completed_at\": \"2026-05-17T23:17:56.045Z\"}, \"eval-perdof-object-norm02-seed43-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T12:04:16.681Z\", \"updated_at\": \"2026-05-17T23:17:06.378Z\", \"hypothesis\": \"perdof CRM ε=0.2 seed43 on LIBERO-Object. 第 3 次尝试。补充 perdof magnitude curve ε=0.2 数据（seed42=11%）。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed43_bjb1-32546.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Object\", \"data_count\": 10, \"model_name\": \"crm_v3_norm_perdof\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"log_path\": \"N/A (killed as duplicate)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T23:02:21.019Z\", \"metrics\": {\"overall_sr\": 0.09, \"successes\": 9, \"total\": 100}}, \"mag_perdof_norm02_seed43_r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T18:04:37.024Z\", \"updated_at\": \"2026-05-17T23:10:07.386Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=5 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed43_r3.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:5\"], \"pid\": \"449330\", \"log_path\": \"N/A (killed)\", \"submitted_at\": \"2026-05-17T18:04:36.487Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_count\": 100, \"data_path\": \"LIBERO-Object 10tasks×10rollouts\", \"model_name\": \"crm_perdof + SmolVLA\", \"seed\": 43, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"wall_clock_seconds\": 18330.9, \"gpu_hours\": 5.09}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-17T23:10:07.386Z\"}, \"eval-obs-only-object-norm03-seed48\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-17T23:02:40.444Z\", \"updated_at\": \"2026-05-17T23:02:59.737Z\", \"hypothesis\": \"obs_only CRM (ε=0.3) seed48 on LIBERO-Object. 补充 magnitude curve high-norm 段 seed48 数据。扩展 error bars。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 48 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03_seed48.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": 774538, \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only_v3_norm\", \"seed\": 48, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\"}}, \"eval-obs-only-object-norm01-seed48\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-17T23:02:39.518Z\", \"updated_at\": \"2026-05-17T23:02:57.195Z\", \"hypothesis\": \"obs_only CRM (ε=0.1) seed48 on LIBERO-Object. 补充 magnitude curve low-norm 段 seed48 数据。扩展 error bars。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 48 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_obs_only_norm01_seed48.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": 774337, \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only_v3_norm\", \"seed\": 48, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\"}}, \"eval-perdof-object-norm01-seed47-bjb1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T10:27:16.189Z\", \"updated_at\": \"2026-05-17T23:00:33.671Z\", \"hypothesis\": \"Duplicate of perdof norm=0.1 seed47 on bjb1-32546 (deployed by orphan Worker). Also running on bjb2-40593.\", \"spec\": {\"command\": \"cd /root/autodl-tmp/acr-vla && python evaluate.py --model smolvla --mode crm_perdof --benchmark object --seed 47 --n_rollouts 10 --norm_limit 0.1 --checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": 414817, \"data_path\": \"/root/autodl-tmp/acr-vla/libero/data\", \"data_count\": 100, \"model_name\": \"SmolVLA-450M + CRM-perdof\", \"seed\": 47, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks × 10 rollouts)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed47_r2.json\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\"}, \"metrics\": {\"overall_sr\": 0.14, \"successes\": 14, \"total\": 100}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T23:00:33.671Z\"}, \"eval-openvla-object-vla-only-seed42-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T20:06:55.243Z\", \"updated_at\": \"2026-05-17T22:39:25.302Z\", \"hypothesis\": \"OpenVLA 7B finetuned VLA-only baseline on LIBERO-Object using official eval code (transformers 4.40.1, isolated conda env). v1 failed due to transformers 5.8 DynamicCache bug. Dry-run on libero_spatial confirmed 80% SR. This run uses openvla-libero-object finetuned model with 10 trials/task.\", \"spec\": {\"command\": \"bash -c \\\"source /root/autodl-tmp/conda_envs/openvla/bin/activate && cd /root/autodl-tmp/openvla && MUJOCO_GL=egl python experiments/robot/libero/run_libero_eval.py --model_family openvla --pretrained_checkpoint /root/autodl-tmp/models/openvla-libero-object --task_suite_name libero_object --center_crop True --num_trials_per_task 10 --seed 42 --local_log_dir /root/acr-vla-conformal-refinement/results/eval-openvla-object-vla-only-seed42-v2\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": 747644, \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"openvla-7b-libero-object\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/openvla-libero-object\", \"eval_data\": \"libero_object (10 tasks x 10 trials = 100 rollouts)\", \"log_path\": \"/root/acr-vla-conformal-refinement/results/eval-openvla-object-vla-only-seed42-v2\", \"checkpoint_path\": \"/root/autodl-tmp/models/openvla-libero-object\"}, \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.69, \"n_tasks\": 10, \"n_trials_per_task\": 10, \"total_rollouts\": 100}, \"completed_at\": \"2026-05-17T22:39:25.302Z\"}, \"eval-obs-only-object-norm02-k20-seed42\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-17T13:34:42.612Z\", \"updated_at\": \"2026-05-17T22:37:41.079Z\", \"hypothesis\": \"obs_only CRM (ε=0.2, K=20) seed42 on LIBERO-Object. K sweep 实验：K=20 vs K=10 (22%) 比较，验证增加 candidate 数量是否带来额外增益。若 K=20 ≈ K=10，说明 K=10 已接近饱和。\", \"reproduce\": {\"finished_at\": \"2026-05-17T18:33:08.015Z\"}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"completed_at\": \"2026-05-17T18:33:10.102Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T18:33:36.294183+00:00\"}], \"previous_failure\": {\"conclusion\": \"killed\"}}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_k20_seed42.json\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only_v3_norm\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\"}, \"conclusion\": \"killed\"}, \"eval-k1-crm-multiscale-object-seed44-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T18:40:32.365Z\", \"updated_at\": \"2026-05-17T21:14:35.625Z\", \"hypothesis\": \"K=1 CRM with ACCG (multi-scale 4×960D) on LIBERO-Object seed44. Parallel deployment on bjb1-18228. Parent: train-crm-k1-accg-object-seed42-v2\", \"parent\": \"train-crm-k1-accg-object-seed42-v2\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode crm_k1_accg --benchmark object --n_rollouts 10 --seed 44 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt --max_correction_norm 0.2 --output_file logs/eval_k1_crm_multiscale_object_seed44_bjb1-18228.json\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO-Object\", \"data_count\": 10, \"model_name\": \"crm_k1_multiscale\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt\", \"eval_data\": \"LIBERO-Object\", \"gpu_id\": \"cuda:3\", \"tmux_session\": \"eval-k1-seed44\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt\", \"log_path\": \"logs/eval_k1_crm_multiscale_object_seed44_bjb1-18228.json\"}, \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.1, \"successes\": 10, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}, \"completed_at\": \"2026-05-17T21:14:35.625Z\"}, \"eval-k1-crm-multiscale-object-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T18:34:14.132Z\", \"updated_at\": \"2026-05-17T21:02:09.738Z\", \"hypothesis\": \"K=1 CRM with ACCG (multi-scale 4x960D from layers [3,7,11,15]) on LIBERO-Object seed44. Compare with fallback (single-stage) and VLA-only baseline (10.8%). Multi-scale features enable layer-wise importance weighting for more informative correction signals.\", \"parent\": \"train-crm-k1-accg-object-seed42-v2\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode crm_k1_accg --benchmark object --n_rollouts 10 --seed 44 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_k1/crm_k1_best_multiscale.pt --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:4\", \"pid\": 504682, \"model_name\": \"crm_k1_accg_multiscale\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best_multiscale.pt\", \"eval_data\": \"LIBERO-Object\", \"data_path\": \"LIBERO-Object benchmark (10 tasks)\", \"data_count\": 100, \"seed\": 44, \"log_path\": \"logs/eval_k1_crm_multiscale_object_seed44.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best_multiscale.pt\"}, \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.1, \"successes\": 10, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}, \"completed_at\": \"2026-05-17T21:02:09.738Z\"}, \"eval-k1-crm-multiscale-object-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T18:34:11.800Z\", \"updated_at\": \"2026-05-17T21:02:08.069Z\", \"hypothesis\": \"K=1 CRM with ACCG (multi-scale 4x960D from layers [3,7,11,15]) on LIBERO-Object seed43. Compare with fallback (single-stage) and VLA-only baseline (10.8%). Multi-scale features enable layer-wise importance weighting for more informative correction signals.\", \"parent\": \"train-crm-k1-accg-object-seed42-v2\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --mode crm_k1_accg --benchmark object --n_rollouts 10 --seed 43 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_k1/crm_k1_best_multiscale.pt --max_correction_norm 0.2\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:1\", \"pid\": 503178, \"model_name\": \"crm_k1_accg_multiscale\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best_multiscale.pt\", \"eval_data\": \"LIBERO-Object\", \"data_path\": \"LIBERO-Object benchmark (10 tasks)\", \"data_count\": 100, \"seed\": 43, \"log_path\": \"logs/eval_k1_crm_multiscale_object_seed43.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best_multiscale.pt\"}, \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.09, \"successes\": 9, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.2, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}, \"completed_at\": \"2026-05-17T21:02:08.069Z\"}, \"eval-k1-crm-multiscale-object-seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T18:34:09.846Z\", \"updated_at\": \"2026-05-17T21:02:06.052Z\", \"hypothesis\": \"K=1 CRM with ACCG (multi-scale 4x960D from layers [3,7,11,15]) on LIBERO-Object seed42. Compare with fallback (single-stage) and VLA-only baseline (10.8%). Multi-scale features enable layer-wise importance weighting for more informative correction signals.\", \"parent\": \"train-crm-k1-accg-object-seed42-v2\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode crm_k1_accg --benchmark object --n_rollouts 10 --seed 42 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt --max_correction_norm 0.2\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:0\", \"pid\": 455518, \"model_name\": \"crm_k1_accg_multiscale\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt\", \"eval_data\": \"LIBERO-Object\", \"data_path\": \"LIBERO-Object benchmark (10 tasks)\", \"data_count\": 100, \"seed\": 42, \"log_path\": \"logs/eval_k1_crm_multiscale_object_seed42.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt\"}, \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.12, \"successes\": 12, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.3, \"butter\": 0.1, \"milk\": 0, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.2}}, \"completed_at\": \"2026-05-17T21:02:06.052Z\"}, \"eval-perdof-object-norm01-seed46-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T07:05:32.383Z\", \"updated_at\": \"2026-05-17T21:01:12.153Z\", \"hypothesis\": \"perdof CRM at eps=0.1 on seed46 will show magnitude sensitivity collapse pattern similar to seed42, confirming obs_only robustness advantage\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_perdof --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1 --seed 46 --benchmark object\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": 393646, \"seed\": 46, \"model_name\": \"SmolVLA+CRM_perdof\", \"data_path\": \"LIBERO-Object 10 tasks\", \"data_count\": 100, \"eval_data\": \"LIBERO-Object\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\"}, \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.1, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"log_path\": \"logs/eval_object_perdof_norm01_seed46.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"completed_at\": \"2026-05-17T21:01:12.153Z\"}, \"eval-k1-crm-multiscale-object-seed43-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T18:40:31.417Z\", \"updated_at\": \"2026-05-17T20:55:55.430Z\", \"hypothesis\": \"K=1 CRM with ACCG (multi-scale 4×960D) on LIBERO-Object seed43. Parallel deployment on bjb1-18228. Parent: train-crm-k1-accg-object-seed42-v2\", \"parent\": \"train-crm-k1-accg-object-seed42-v2\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --mode crm_k1_accg --benchmark object --n_rollouts 10 --seed 43 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt --max_correction_norm 0.2 --output_file logs/eval_k1_crm_multiscale_object_seed43_bjb1-18228.json\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO-Object\", \"data_count\": 10, \"model_name\": \"crm_k1_multiscale\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt\", \"eval_data\": \"LIBERO-Object\", \"gpu_id\": \"cuda:1\", \"tmux_session\": \"eval-k1-seed43\"}, \"conclusion\": \"negative\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed43_bjb1-18228.json\", \"metrics\": {\"overall_sr\": 0.09, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.2, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt\", \"completed_at\": \"2026-05-17T20:55:55.430Z\"}, \"eval-obs-only-object-norm01-seed47\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T06:51:15.721Z\", \"updated_at\": \"2026-05-17T19:14:32.736Z\", \"hypothesis\": \"obs_only CRM (ε=0.1) seed=47 on LIBERO Object. 4th seed for magnitude curve low-norm point. Combined with seeds 42/45/46, provides error bar for obs_only at ε=0.1. Supports robustness narrative (obs_only stable across all norms).\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"363210\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm01-seed47.log\", \"submitted_at\": \"2026-05-17T06:54:17.250Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"crm_v3_obs_only\", \"seed\": 47, \"wall_clock_seconds\": 44408.5, \"gpu_hours\": 12.34}, \"conclusion\": \"killed\", \"reproduce\": {\"finished_at\": \"2026-05-17T19:11:17.010Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T19:11:22.018666+00:00\"}]}, \"completed_at\": \"2026-05-17T19:14:25.783Z\", \"failure_reason\": \"Evaluation killed mid-run: only 2/10 tasks completed (task0: 0/10, task1: 1/10). No JSON output saved. EXIT_CODE=0 but incomplete. Previously marked killed in batch cleanup. Data not usable for magnitude curve.\"}, \"eval-perdof-object-norm02-seed45-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T13:32:18.289Z\", \"updated_at\": \"2026-05-17T18:37:21.561Z\", \"hypothesis\": \"perdof CRM (ε=0.2) seed45 on LIBERO-Object. 补充 Figure 2 perdof magnitude curve ε=0.2 数据（seed42=11%, seed43=9%, seed44 running）。\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed45.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"634427\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm02-seed45-r2.log\", \"submitted_at\": \"2026-05-17T13:35:38.103Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 10, \"model_name\": \"crm_perdof\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"wall_clock_seconds\": 17779.9, \"gpu_hours\": 4.94}, \"reproduce\": {\"finished_at\": \"2026-05-17T18:31:54.940Z\"}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-17T18:31:57.991Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T18:32:03.172248+00:00\"}]}}, \"eval-obs-only-object-norm005-seed43-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T13:34:38.488Z\", \"updated_at\": \"2026-05-17T18:37:20.319Z\", \"hypothesis\": \"obs_only CRM (ε=0.05) seed43 on LIBERO-Object. M006 补救重跑。seed42 ε=0.05=13%。\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_obs_only_norm005_seed43_r2.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"633631\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm005-seed43-r3.log\", \"submitted_at\": \"2026-05-17T13:35:14.715Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 10, \"model_name\": \"crm_obs_only\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"wall_clock_seconds\": 17815.3, \"gpu_hours\": 4.95}, \"reproduce\": {\"finished_at\": \"2026-05-17T18:32:06.590Z\"}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-17T18:32:10.053Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T18:32:15.088162+00:00\"}]}}, \"plan_602-latency-profile\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T18:34:20.097Z\", \"updated_at\": \"2026-05-17T18:35:42.842Z\", \"hypothesis\": \"Measure wall-clock latency of ACR-VLA pipeline components: VLA encode, VLA K-sampling (K=1/5/10/20), CGS scoring, CRM forward pass, and full pipeline. Quantify overhead of conformal refinement relative to VLA sampling cost.\", \"spec\": {\"command\": \"python -u src/latency_profile.py\", \"server\": \"bjb2-28827\", \"seed\": 42, \"data_path\": \"/root/acr-vla-conformal-refinement/logs/latency_profile.json\", \"data_count\": 20, \"model_name\": \"SmolVLA+CRM\"}, \"conclusion\": \"success\", \"metrics\": {\"vla_encode_prefix_ms\": 33.5, \"vla_sample_K1_ms\": 192.6, \"vla_sample_K5_ms\": 965.3, \"vla_sample_K10_ms\": 1913.7, \"vla_sample_K20_ms\": 3858.2, \"cgs_ms\": 6.2, \"crm_forward_ms\": 0.3, \"full_pipeline_K10_ms\": 1908.2, \"acr_overhead_pct\": 0.34}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/latency_profile.log\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/latency_profile.json\", \"completed_at\": \"2026-05-17T18:35:42.842Z\"}, \"train-crm-k1-accg-object-seed42-v2\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-17T15:51:14.367Z\", \"updated_at\": \"2026-05-17T18:31:23.291Z\", \"hypothesis\": \"K=1 CRM with ACCG using full multi-scale features (4×960D from SmolVLA layers [3,7,11,15]). Multi-scale should capture richer correction signals than single-stage 960D fallback (val_loss=0.006505). Parent: train-crm-k1-accg-object-seed42-fallback\", \"parent\": \"train-crm-k1-accg-object-seed42-fallback\", \"notes\": \"Retry after W&B API key crash. Added --no_wandb. Precompute cache reused (65,223 samples). Training restarted from scratch (epoch 1/50). PID 447923 on cuda:0, tmux session: train-crm-k1-v2.\", \"reproduce\": {\"finished_at\": \"2026-05-17T18:01:06.354Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T18:01:12.607135+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"HDF5 corruption report was false alarm - all 10 files verified intact (md5 match, h5py OK). Training continued past crash point. Precompute running: 7500/72507, ~75 min remaining. conclusion=failed was set prematurely; training is actually running.\"}}, \"completed_at\": \"2026-05-17T18:01:40.220Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/train-crm-k1-accg-object-seed42-v2.log\"}, \"metrics\": {\"best_val_loss\": 0.007199, \"total_epochs\": 50, \"train_samples\": 65223, \"obs_dim\": \"4x960D\", \"multi_scale\": true}, \"conclusion\": \"success\"}, \"eval-k1-crm-accg-object-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T15:28:01.165Z\", \"updated_at\": \"2026-05-17T18:22:02.272Z\", \"hypothesis\": \"K=1 CRM with ACCG (fallback 960D) on LIBERO-Object seed44. 验证 ACCG correction 是否优于 K=1 VLA-only baseline (mean 10.8%). Parent: train-crm-k1-accg-object-seed42-fallback\", \"parent\": \"train-crm-k1-accg-object-seed42-fallback\", \"spec\": {\"pid\": 460733, \"gpu\": [\"cuda:5\"], \"server\": \"bjb1-32546\", \"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode crm_k1_accg --benchmark object --n_rollouts 10 --seed 44 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt --max_correction_norm 0.2 --output_file logs/eval_k1_crm_accg_object_seed44.json\", \"model_name\": \"crm_k1_accg\", \"seed\": 44, \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k1_crm_accg_object_seed44.json\"}, \"conclusion\": \"negative\", \"metrics\": {\"overall_success_rate\": 0.07, \"n_rollouts\": 100, \"tasks\": {\"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.1}}, \"completed_at\": \"2026-05-17T18:02:47.296Z\"}, \"eval-k1-crm-accg-object-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T15:27:59.825Z\", \"updated_at\": \"2026-05-17T18:22:01.354Z\", \"hypothesis\": \"K=1 CRM with ACCG (fallback 960D) on LIBERO-Object seed43. 验证 ACCG correction 是否优于 K=1 VLA-only baseline (mean 10.8%). Parent: train-crm-k1-accg-object-seed42-fallback\", \"parent\": \"train-crm-k1-accg-object-seed42-fallback\", \"spec\": {\"pid\": 460729, \"gpu\": [\"cuda:4\"], \"server\": \"bjb1-32546\", \"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode crm_k1_accg --benchmark object --n_rollouts 10 --seed 43 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt --max_correction_norm 0.2 --output_file logs/eval_k1_crm_accg_object_seed43.json\", \"model_name\": \"crm_k1_accg\", \"seed\": 43, \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k1_crm_accg_object_seed43.json\"}, \"conclusion\": \"negative\", \"metrics\": {\"overall_success_rate\": 0.12, \"n_rollouts\": 100, \"tasks\": {\"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.2, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.1}}, \"completed_at\": \"2026-05-17T18:02:45.640Z\"}, \"eval-k1-crm-accg-object-seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T15:27:58.213Z\", \"updated_at\": \"2026-05-17T18:22:00.464Z\", \"hypothesis\": \"K=1 CRM with ACCG (fallback 960D) on LIBERO-Object seed42. 验证 ACCG correction 是否优于 K=1 VLA-only baseline (mean 10.8%). Parent: train-crm-k1-accg-object-seed42-fallback\", \"parent\": \"train-crm-k1-accg-object-seed42-fallback\", \"spec\": {\"pid\": 460724, \"gpu\": [\"cuda:1\"], \"server\": \"bjb1-32546\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --mode crm_k1_accg --benchmark object --n_rollouts 10 --seed 42 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt --max_correction_norm 0.2 --output_file logs/eval_k1_crm_accg_object_seed42.json\", \"model_name\": \"crm_k1_accg\", \"seed\": 42, \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt\", \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_k1_crm_accg_object_seed42.json\"}, \"conclusion\": \"negative\", \"metrics\": {\"overall_success_rate\": 0.11, \"n_rollouts\": 100, \"tasks\": {\"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}, \"completed_at\": \"2026-05-17T18:02:43.637Z\"}, \"eval-obs-only-object-default-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T11:15:05.583Z\", \"updated_at\": \"2026-05-17T17:32:15.936Z\", \"spec\": {\"command\": \"python src/evaluate.py --mode crm_obs_only --K 10 --seed 45 --benchmark object --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_default_seed45.json\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:3\", \"pid\": 242264, \"data_path\": \"LIBERO object benchmark\", \"data_count\": 10, \"model_name\": \"crm_obs_only\", \"seed\": 45}, \"hypothesis\": \"obs_only CRM (default norm ~1.42, 无裁剪) seed=45 on LIBERO Object. 验证 obs_only 在 uncapped 大 norm 下仍优于 VLA-only（seed42 在 default 为 17%）。极端 magnitude 鲁棒性测试。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.12, \"tasks\": 10, \"rollouts_per_task\": 20, \"total_successes\": 24, \"total_rollouts\": 200}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed45.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"completed_at\": \"2026-05-17T17:32:15.936Z\"}, \"eval-scalar-object-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T08:38:01.206Z\", \"updated_at\": \"2026-05-17T17:29:34.723Z\", \"spec\": {\"command\": \"python src/evaluate.py --mode crm_scalar --max_correction_norm 0.1 --K 10 --seed 45 --benchmark object --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --output_file logs/eval_object_scalar_seed45.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"pid\": 224623, \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_v3_scalar_unc\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"eval_data\": \"LIBERO object\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"log_path\": \"logs/eval_object_scalar_seed45.log\"}, \"hypothesis\": \"Scalar uncertainty CRM seed=45 on LIBERO Object. 测试 scalar conditioning（单一 std 而非 per-DOF）是否比 obs_only 或 perdof 更优。如果表现介于两者之间，说明 conditioning 信息量与性能正相关。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.09, \"successes\": 18, \"total\": 200, \"best_task\": \"chocolate_pudding_0.25\", \"worst_task\": \"alphabet_soup_0.0\"}, \"completed_at\": \"2026-05-17T17:29:34.723Z\"}, \"eval-perdof-object-norm02-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T08:34:55.059Z\", \"updated_at\": \"2026-05-17T17:03:14.729Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python src/evaluate.py --benchmark object --mode crm_perdof --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --K 10 --seed 45 --output_file logs/eval_object_perdof_norm02_seed45.json\", \"server\": \"bjb2-28827\", \"gpu_id\": \"cuda:1\", \"pid\": 222824, \"seed\": 45, \"model_name\": \"crm_perdof\", \"data_path\": \"LIBERO object\", \"data_count\": 10, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object\", \"hypothesis\": \"Perdof CRM norm=0.2 seed=45 on LIBERO object. Additional perdof data point for cross-seed comparison. Expected ~11% based on seed42 data.\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed45.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\"}, \"hypothesis\": \"perdof CRM (ε=0.2) seed=45 on LIBERO Object. 验证 perdof 在中间 norm (0.2) 的表现（seed42=11%, seed43=9%）。为 magnitude curve 误差估计提供第三个 seed。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.09, \"successes\": 18, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}, \"notes\": \"perdof ε=0.2 seed45: 9% (18/200). Cross-seed: seed42=11%, seed43=9%, seed44=10%, seed45=9%. Mean ~9.75%.\", \"completed_at\": \"2026-05-17T17:03:14.729Z\"}, \"eval-perdof-object-norm02-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T00:37:24.278Z\", \"updated_at\": \"2026-05-17T16:52:17.419Z\", \"hypothesis\": \"perdof CRM (ε=0.2) seed=44 on LIBERO Object benchmark. Adds second seed to perdof norm=0.2 (seed42=11%, seed43=9%). Enables error bar on magnitude curve figure at this norm point.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed44.json\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:5\", \"pid\": \"326081\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm02-seed44.log\", \"submitted_at\": \"2026-05-17T08:36:00Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 44, \"model_name\": \"crm_perdof\", \"data_path\": \"LIBERO object benchmark (10 tasks)\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 29777.4, \"gpu_hours\": 8.27}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.1, \"successes\": 10, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm02-seed44.log\", \"checkpoint_path\": \"logs/eval_object_perdof_norm02_seed44.json\", \"completed_at\": \"2026-05-17T16:52:17.419Z\"}, \"train-crm-k1-accg-object-seed42-fallback\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T15:02:35.790Z\", \"updated_at\": \"2026-05-17T15:19:16.626Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python -u train_crm_k1.py --benchmark object --epochs 50 --batch_size 512 --lr 1e-3 --seed 42 --loss_mode multi --lambda_dir 0.1 --lambda_tri 0.05 --lambda_mag 0.01 --max_correction_norm 0.2 --reuse_k10_cache --k10_cache_dir /root/autodl-tmp/crm_cache_v5/ --auto --no_wandb\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": 456622, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/train_crm_k1_fallback.log\", \"submitted_at\": \"2026-05-17T15:02:35.104Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_id\": \"cuda:4\", \"data_path\": \"/root/autodl-tmp/crm_cache_v5/\", \"data_count\": 4857, \"model_name\": \"crm_k1_accg_fallback\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_k1/\", \"wall_clock_seconds\": 914.9, \"gpu_hours\": 0.25}, \"hypothesis\": \"CRM K=1 with ACCG architecture trained on K=10 single-stage cache (960D fallback) can learn effective corrections for object benchmark, achieving low val_loss comparable to multi-scale approach\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T15:17:49.965Z\", \"metrics\": {\"best_val_loss\": 0.006505, \"best_epoch\": 43, \"total_epochs\": 50, \"train_samples\": 4857, \"obs_dim\": 960, \"multi_scale\": false, \"wall_clock_seconds\": 914.9}}, \"train-crm-k1-accg-object-seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T14:48:22.459Z\", \"updated_at\": \"2026-05-17T14:53:10.162Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement/src && CUDA_VISIBLE_DEVICES=0 python -u train_crm_k1.py --benchmark object --epochs 50 --batch_size 512 --lr 1e-3 --seed 42 --loss_mode multi --lambda_dir 0.1 --lambda_tri 0.05 --lambda_mag 0.01 --max_correction_norm 0.2 --wandb_project acr-vla-conformal-refinement --wandb_run_name crm-k1-v2-accg-object --auto\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"pid\": \"427856\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/train-crm-k1-accg-object-seed42.log\", \"submitted_at\": \"2026-05-17T14:48:21.711Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 42, \"model_name\": \"CRM_K1_ACCG_v2\", \"data_path\": \"LIBERO-Object precomputed K=1 features\", \"data_count\": -1, \"wall_clock_seconds\": 174.4, \"gpu_hours\": 0.05}, \"hypothesis\": \"K=1 CRM 训练（ACCG 架构）：使用 Action-Conditioned Correction Gating 替代 FiLM，多阶段 VLA 特征融合 + 组合损失函数（L2 + directional + triplet + magnitude），训练专用于 K=1 单采样纠正的 CRM。目标超越 K=1 VLA-only baseline (10.8%)。ACCG 用 action 本身计算动态 gate 选择 correction 维度。\", \"reproduce\": {\"finished_at\": \"2026-05-17T14:49:15.593Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T14:49:21.444858+00:00\"}]}, \"conclusion\": \"failed\", \"failure_reason\": \"LIBERO HDF5 demo data missing on bjb2-28827. Precompute requires raw demo trajectories but only K=10 cache exists.\", \"completed_at\": \"2026-05-17T14:51:16.090Z\"}, \"eval-perdof-object-norm02-seed45-deploy\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T13:34:09.564Z\", \"updated_at\": \"2026-05-17T13:52:58.983Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed45.json 2>&1 | tee logs/eval_object_perdof_norm02_seed45.log\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"632156\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm02-seed45-deploy.log\", \"submitted_at\": \"2026-05-17T13:34:09.103Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1025.8, \"gpu_hours\": 0.28}, \"hypothesis\": \"perdof CRM (ε=0.2) seed45 on LIBERO-Object. 补充 Figure 2 perdof magnitude curve ε=0.2 数据（seed42=11%, seed43=9%, seed44 running）。\", \"reproduce\": {\"finished_at\": \"2026-05-17T13:47:18.573Z\"}, \"failure_reason\": \"**根因**: MuJoCo EGL 渲染初始化 segfault（native crash）。\\n\\n**证据**:\\n- tmux 日志和应用日志均在 `[eval] 10 tasks loaded.` 后中断，无 Python traceback、无 segfault handler 输出\\n- 代码中有 SIGSEGV handler 但未被触发，说明崩溃发生在 native code（MuJoCo/EGL）且 handler 未能执行\\n- 同服务器多个实验表现相同模式（eval_object_obs_only_norm03_seed47、eval_object_perdof_norm01_seed47 等均在 \\\"10 tasks loaded\\\" 后死亡）\\n- 非 OOM：系统 RAM 454GB 空闲，GPU VRAM 仅用 5.6GB/24GB\\n- 崩溃点：第一个 rollout_single() → env.reset() 触发 MuJoCo EGL context 创建\\n\\n**关键日志（最后一行有效输出）**:\\n`[eval] 10 tasks loaded.`\\n（之后无任何输出，进程静默死亡）\\n\\n**可能触发因素**: 4 张 GPU 同时运行 4 个 eval 进程，并发 EGL context 初始化存在 driver 层竞争。较早的单卡实验（seed44/45/46）正常完成。\\n\\n**建议**: PID 634438 已在 GPU 0 上重启并处于 Running 状态，等待其完成。若再次失败，考虑串行执行（不并发跑 4 个 EGL 进程）或降低并发数。\", \"conclusion\": \"killed\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T13:47:28.347997+00:00\"}]}, \"completed_at\": \"2026-05-17T13:51:14.936Z\"}, \"eval-obs-only-object-norm003-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T13:33:23.925Z\", \"updated_at\": \"2026-05-17T13:34:01.871Z\", \"hypothesis\": \"obs_only CRM (ε=0.03) seed43 on LIBERO-Object. plan_500 低 norm 补数据：seed42 ε=0.03=16%。多 seed 确认 obs_only 在极低 correction norm 下仍稳定。\", \"conclusion\": \"failed\", \"notes\": \"PID 621127 on bjb1-18228 cuda:1 died. Process not found, GPU idle. Ghost experiment discovered during registration attempt.\", \"spec\": {\"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"621127\", \"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_obs_only_norm003_seed43.json\", \"model_name\": \"SmolVLA+CRM_obs_only\", \"seed\": 43, \"data_path\": \"LIBERO-Object 10 tasks\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object\", \"log_path\": \"logs/eval_object_obs_only_norm003_seed43.log\", \"checkpoint_path\": \"N/A (eval)\"}, \"completed_at\": \"2026-05-17T13:33:52.018Z\"}, \"eval-random-selection-object-seed42\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-17T13:32:30.506Z\", \"updated_at\": \"2026-05-17T13:33:58.460Z\", \"hypothesis\": \"Random selection baseline (K=10 随机选一个 action) on LIBERO-Object seed42. Ablation 验证 CRM uncertainty-guided selection 的价值。\", \"spec\": {\"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"395256\", \"command\": \"python -u src/evaluate.py --mode random_selection --benchmark object --n_rollouts 10 --seed 42 --K 10\", \"model_name\": \"random_selection\", \"seed\": 42, \"data_path\": \"LIBERO-Object 10 tasks\", \"data_count\": 100, \"eval_data\": \"LIBERO-Object\", \"checkpoint_source\": \"N/A (random baseline)\"}}, \"eval-obs-only-object-norm01-seed47-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T07:05:28.139Z\", \"updated_at\": \"2026-05-17T13:31:57.433Z\", \"hypothesis\": \"obs_only CRM at eps=0.1 on seed47 will achieve similar improvement over VLA-only as seen in seed42 (19%), testing seed robustness of the magnitude curve\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --seed 47 --benchmark object\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": 588037, \"seed\": 47, \"model_name\": \"SmolVLA+CRM_obs_only\", \"data_path\": \"LIBERO-Object 10 tasks\", \"data_count\": 100, \"eval_data\": \"LIBERO-Object\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-17T13:31:55.004Z\", \"notes\": \"Worker batch7 误杀, 4/10 tasks 完成\"}, \"eval-perdof-object-norm03-seed45-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T21:32:42.117Z\", \"updated_at\": \"2026-05-17T12:04:17.540Z\", \"hypothesis\": \"perdof CRM (ε=0.3) seed=45 on LIBERO object benchmark. Retry after unregistered process conflict. Expected to confirm perdof collapse at high norm (seed42=4%, seed44 running). Supports magnitude curve narrative.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_seed45_r2.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"319463\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm03-seed45-r2.log\", \"submitted_at\": \"2026-05-16T21:33:52.055Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO object benchmark (10 tasks)\", \"data_count\": 100, \"model_name\": \"crm_v3_norm_perdof\", \"seed\": 45, \"wall_clock_seconds\": 48204.7, \"gpu_hours\": 13.39}, \"reproduce\": {\"finished_at\": \"2026-05-17T10:54:49.175Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T10:54:55.730176+00:00\"}]}, \"checkpoint_path\": \"N/A - eval only\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm03-seed45-r2.log\", \"metrics\": {\"overall_sr\": 0.06, \"successes\": 6, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.1}}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-17T10:57:16.754Z\"}, \"eval-perdof-object-norm03-seed44-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:22:10.412Z\", \"updated_at\": \"2026-05-17T12:00:58.173Z\", \"hypothesis\": \"perdof CRM ε=0.3 seed44 re-run on LIBERO-Object. 原 seed44 已完成(conclusion=negative, SR=4%). 重跑验证跨 seed 一致性。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_seed44_r2.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": 421086, \"seed\": 44, \"model_name\": \"SmolVLA+CRM_perdof\", \"data_path\": \"LIBERO-Object 10 tasks\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\"}, \"conclusion\": \"negative\", \"reproduce\": {\"finished_at\": \"2026-05-17T11:50:26.264Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-17T11:50:20.975Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T11:50:33.595081+00:00\"}]}, \"metrics\": {\"success_rate\": 0.04, \"n_rollouts\": 10, \"total_rollouts\": 100, \"note\": \"JSON result found by diagnostic worker. Matches original seed44=4%. False positive failure due to no sentinel/W&B in evaluate.py.\"}}, \"eval-obs-only-object-norm03-seed47\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:21:56.645Z\", \"updated_at\": \"2026-05-17T11:50:09.879Z\", \"hypothesis\": \"obs_only CRM ε=0.3 seed47 on LIBERO-Object. 5th seed at high norm (seed42=19%, seed44=18%, seed45=14%, seed46 running). 补全 magnitude curve 高 norm 段 error bar。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03_seed47.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": 612853, \"seed\": 47, \"model_name\": \"SmolVLA+CRM_obs_only\", \"data_path\": \"LIBERO-Object 10 tasks\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\"}, \"conclusion\": \"failed\", \"reproduce\": {\"finished_at\": \"2026-05-17T11:50:06.763Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-17T11:50:09.879Z\"}, \"eval-perdof-object-norm03-seed46-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:28:13.840Z\", \"updated_at\": \"2026-05-17T11:36:55.536Z\", \"hypothesis\": \"perdof CRM ε=0.3 seed46 retry on LIBERO-Object. 原 PID 394433 退出，PID 392856 在 bjb2-28827 cuda:2 继续运行。seed42=4%, seed44=4%, seed45=6%。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_seed46.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": 392856, \"seed\": 46, \"model_name\": \"SmolVLA+CRM_perdof\", \"data_path\": \"LIBERO-Object 10 tasks\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"checkpoint_path\": \"N/A\", \"log_path\": \"N/A\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-17T11:36:55.536Z\"}, \"eval-perdof-object-norm03-seed46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:21:58.288Z\", \"updated_at\": \"2026-05-17T11:27:50.618Z\", \"hypothesis\": \"perdof CRM ε=0.3 seed46 on LIBERO-Object. 4th seed at high norm (seed42=4%, seed44=4%, seed45=6%). 验证 perdof 在高 norm 的灾难性崩溃是否跨 seed 一致。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_seed46.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": 392856, \"seed\": 46, \"model_name\": \"SmolVLA+CRM_perdof\", \"data_path\": \"LIBERO-Object 10 tasks\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"note\": \"PID corrected from 394433 to 392856 based on nvidia-smi scan\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-17T11:26:50.317Z\", \"metrics\": {\"failure_reason\": \"Process exited after ~2 min during env loading, no evaluation results produced. No JSON output. Likely OOM or SIGHUP kill (exit code 129).\", \"n_rollouts\": 0}}, \"eval-obs-only-object-norm02-seed47\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T21:32:40.226Z\", \"updated_at\": \"2026-05-17T11:05:43.649Z\", \"hypothesis\": \"obs_only CRM (ε=0.2) seed=47 on LIBERO object benchmark. Extends multi-seed comparison to 6 seeds. If consistent with seeds 42-44 (16-22%), strengthens pooled significance for Narrative A transition.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_seed47.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"319128\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-seed47.log\", \"submitted_at\": \"2026-05-16T21:33:49.282Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO object benchmark (10 tasks)\", \"data_count\": 100, \"model_name\": \"crm_v3_norm_obs_only\", \"seed\": 47, \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed47.json\", \"wall_clock_seconds\": 48714.4, \"gpu_hours\": 13.53}, \"reproduce\": {\"finished_at\": \"2026-05-17T10:48:10.086Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T10:48:15.850144+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.2, \"successes\": 20, \"total\": 100, \"benchmark\": \"object\", \"mode\": \"obs_only\", \"norm\": 0.2, \"seed\": 47}, \"completed_at\": \"2026-05-17T11:05:43.649Z\"}, \"eval-perdof-object-norm01-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T20:21:04.937Z\", \"updated_at\": \"2026-05-17T10:59:11.317Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_perdof_norm01_seed44.json\", \"server\": \"bjb1-18228\", \"gpu_id\": 1, \"model_name\": \"crm_perdof_norm01\", \"seed\": 44, \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark\", \"hypothesis\": \"perdof CRM norm=0.1 seed=44 on LIBERO object. Multi-seed magnitude curve: seed42=11%, expecting similar. Fills the biggest gap in perdof magnitude data (norm=0.1 only has 1 seed).\", \"pid\": 531963}, \"hypothesis\": \"perdof CRM (ε=0.1) seed=44 on LIBERO Object. 验证 perdof 在低 norm 的安全区域（seed42=11%，seed45 running）。多 seed 支撑 magnitude curve 低 norm 段。\", \"reproduce\": {\"finished_at\": \"2026-05-17T10:48:36.650Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-17T10:48:39.951Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T10:48:45.826946+00:00\"}]}, \"notes\": \"失败原因: process dead 5× with no sentinel/W&B — auto-resolved as failed | 诊断中: Worker worker_diagnose_eval-perdof-object-norm01-seed44_20260517T105221 已派发到 bjb1-18228 检查是否为 cron 误判（同配置 seed45 成功，SR=11%）\", \"metrics\": {\"overall_sr\": 0.08, \"total_successes\": 8, \"total_rollouts\": 100, \"seed\": 44, \"mode\": \"crm_perdof\", \"max_correction_norm\": 0.1}}, \"eval-obs-only-object-norm01-seed47-bjb2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T07:07:14.242Z\", \"updated_at\": \"2026-05-17T10:56:41.892Z\", \"hypothesis\": \"Duplicate of seed47 obs_only norm=0.1 on bjb2 (survived GPU conflict cleanup), provides extra seed47 data point\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --seed 47 --benchmark object\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": 363223, \"seed\": 47, \"model_name\": \"SmolVLA+CRM_obs_only\", \"data_path\": \"LIBERO-Object 10 tasks\", \"data_count\": 100, \"eval_data\": \"LIBERO-Object\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"checkpoint_path\": \"N/A (killed duplicate)\", \"log_path\": \"N/A (killed duplicate)\"}, \"conclusion\": \"killed\", \"reproduce\": {\"finished_at\": \"2026-05-17T10:42:47.471Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-17T10:42:49.632Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T10:42:53.924730+00:00\"}]}}, \"eval-obs-only-object-norm02-seed46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T16:04:31.207Z\", \"updated_at\": \"2026-05-17T10:54:36.728Z\", \"spec\": {\"command\": \"cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_seed46.json 2>&1 | tee logs/eval_object_obs_only_norm02_seed46.log\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": 510896, \"seed\": 46, \"model_name\": \"crm_obs_only_norm02\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"hypothesis\": \"obs_only CRM v3-norm norm=0.2 seed=46 on LIBERO object. 5th seed for Fisher test statistical power.\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark\", \"log_path\": \"logs/eval_object_obs_only_norm02_seed46.log\", \"checkpoint_path\": \"N/A (eval only)\"}, \"hypothesis\": \"obs_only CRM ε=0.2 seed46 on LIBERO-Object. Pooled Fisher test 最关键的缺失配对数据（与 argmin seed46=10% 配对）。ε=0.2 是 obs_only 最优区间，seed42=22%。\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.15, \"total_episodes\": 100, \"successes\": 15, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 2, \"bbq_sauce\": 3, \"ketchup\": 0, \"tomato_sauce\": 1, \"butter\": 1, \"milk\": 1, \"chocolate_pudding\": 4, \"orange_juice\": 3}}, \"completed_at\": \"2026-05-17T05:07:55.218Z\"}, \"eval-obs-only-object-norm01-seed46-bjb2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T07:17:00.494Z\", \"updated_at\": \"2026-05-17T10:54:24.948Z\", \"hypothesis\": \"Duplicate of obs_only norm=0.1 seed46 on bjb2 (deployed by batch5 Worker). Extra data point for magnitude curve.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --seed 46 --benchmark object\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"pid\": 365893, \"seed\": 46, \"model_name\": \"SmolVLA+CRM_obs_only\", \"data_path\": \"LIBERO-Object 10 tasks\", \"data_count\": 100, \"eval_data\": \"LIBERO-Object\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}, \"reproduce\": {\"finished_at\": \"2026-05-17T10:43:36.147Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-17T10:43:38.311Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T10:43:46.527772+00:00\"}]}}, \"eval-argmin-object-seed47\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T21:38:21.922Z\", \"updated_at\": \"2026-05-17T10:54:02.629Z\", \"hypothesis\": \"Argmin baseline (reconvla K=10) seed=47 on LIBERO object benchmark. Paired with obs_only seed47 on cuda:0 for direct comparison. Extends argmin multi-seed data for pooled Fisher test.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --seed 47 --benchmark object --n_rollouts 10 --output_file logs/eval_object_reconvla_seed47.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": 322337, \"seed\": 47, \"model_name\": \"SmolVLA_argmin_K10\", \"data_path\": \"LIBERO-Object 10 tasks\", \"data_count\": 100, \"eval_data\": \"LIBERO-Object\", \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-object-seed47.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-17T10:51:45.356Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T10:51:50.389646+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.1, \"total_successes\": 10, \"total_rollouts\": 100, \"n_rollouts_per_task\": 10, \"seed\": 47, \"benchmark\": \"object\", \"K\": 10, \"mode\": \"reconvla\", \"baseline_mode\": \"single\", \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.2}}, \"completed_at\": \"2026-05-17T10:54:02.630Z\"}, \"eval-perdof-object-norm01-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T20:21:06.341Z\", \"updated_at\": \"2026-05-17T10:22:14.183Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_perdof_norm01_seed45.json\", \"server\": \"bjb1-32546\", \"gpu_id\": 2, \"model_name\": \"crm_perdof_norm01\", \"seed\": 45, \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark\", \"hypothesis\": \"perdof CRM norm=0.1 seed=45 on LIBERO object. Multi-seed magnitude curve: seed42=11%, seed44=deploying. 3rd seed for perdof low-norm baseline.\", \"pid\": 309151}, \"hypothesis\": \"perdof CRM (ε=0.1) seed=45 on LIBERO Object. 验证 perdof 在低 norm (0.1) 的安全区域（seed42=11%）。如果与 obs_only 接近，支持\\\"低 norm 两者等效\\\"叙事。\", \"metrics\": {\"overall_sr\": 0.11, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}, \"seed\": 45, \"benchmark\": \"object\", \"mode\": \"crm_perdof\", \"max_correction_norm\": 0.1}, \"conclusion\": \"success\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed45.json\", \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-17T10:22:14.184Z\"}, \"eval-perdof-object-norm01-seed47\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T06:51:20.872Z\", \"updated_at\": \"2026-05-17T10:19:28.338Z\", \"hypothesis\": \"perdof CRM at eps=0.1 on seed47, completes magnitude curve low-norm data for perdof\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode crm_perdof --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1 --seed 47 --benchmark object --n_rollouts 10 --output_file logs/eval_object_perdof_norm01_seed47.json\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"388460\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm01-seed47.log\", \"submitted_at\": \"2026-05-17T06:54:11.992Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 47, \"model_name\": \"SmolVLA+CRM_perdof\", \"data_path\": \"LIBERO-Object 10 tasks\", \"data_count\": 100, \"eval_data\": \"LIBERO-Object\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"checkpoint_path\": \"N/A (killed before completion)\", \"wall_clock_seconds\": 12316.3, \"gpu_hours\": 3.42}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-17T10:19:28.338Z\"}, \"eval-argmin-object-seed46\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T18:39:23.017Z\", \"updated_at\": \"2026-05-17T10:19:26.819Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 46 --K 10 --output_file logs/eval_object_reconvla_seed46.json\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:1\", \"seed\": 46, \"model_name\": \"reconvla\", \"hypothesis\": \"argmin baseline K=10 seed=46 on LIBERO object. 5th seed for Fisher test. Pairs with eval-obs-only-object-norm02-seed46 (bjb1-18228:cuda:3).\", \"data_path\": \"\", \"data_count\": 0, \"checkpoint_source\": \"\", \"eval_data\": \"object\", \"pid\": 295478, \"log_path\": \"logs/eval_argmin_object_seed46.log\", \"checkpoint_path\": \"N/A (eval-only, reconvla baseline)\"}, \"hypothesis\": \"Argmin baseline (conformal selection K=10, 无 learned correction) seed=46 on LIBERO Object. 与 obs_only seed=46 配对，扩展 pooled Fisher test 到 6 seeds。预期 12-17% SR。\", \"metrics\": {\"overall_sr\": 0.1, \"total_successes\": 10, \"total_rollouts\": 100, \"n_rollouts_per_task\": 10, \"seed\": 46, \"benchmark\": \"object\", \"K\": 10, \"mode\": \"reconvla\", \"baseline_mode\": \"single\", \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.1}}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_argmin_object_seed46.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T10:19:26.819Z\"}, \"eval-obs-only-object-norm03-seed45-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T15:24:08.486Z\", \"updated_at\": \"2026-05-17T07:02:49.285Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03_seed45_r2.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:4\"], \"pid\": \"272762\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm03-seed45-r2.log\", \"submitted_at\": \"2026-05-16T15:24:08.144Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_id\": \"cuda:3\", \"model_name\": \"crm_obs_only_norm03\", \"seed\": 45, \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"wall_clock_seconds\": 56321.1, \"gpu_hours\": 15.64}, \"hypothesis\": \"obs_only CRM with max_correction_norm=0.3 on LIBERO Object (seed=45) should show graceful degradation similar to seed42 (19%), providing multi-seed error estimates for the magnitude curve\", \"reproduce\": {\"finished_at\": \"2026-05-17T07:00:25.758Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T07:00:32.829645+00:00\"}]}, \"metrics\": {\"overall_success_rate\": 14, \"total_successes\": 14, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 10, \"bbq_sauce\": 30, \"ketchup\": 10, \"tomato_sauce\": 10, \"butter\": 10, \"milk\": 10, \"chocolate_pudding\": 30, \"orange_juice\": 30}, \"max_correction_norm\": 0.3, \"seed\": 45, \"mode\": \"crm_obs_only\", \"benchmark\": \"object\"}, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm03-seed45-r2.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T07:02:49.285Z\"}, \"eval-vla-mean-object-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T11:14:45.495Z\", \"updated_at\": \"2026-05-17T06:54:28.933Z\", \"spec\": {\"model_name\": \"smolvla_libero_vla_mean\", \"seed\": 45, \"data_path\": \"LIBERO object benchmark (10 tasks)\", \"data_count\": 100, \"checkpoint_source\": \"N/A\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode mean --n_rollouts 10 --K 10 --seed 45 --output_file logs/eval_object_vla_mean_seed45.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"248652\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-mean-object-seed45.log\", \"submitted_at\": \"2026-05-16T11:14:45Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 70783.9, \"gpu_hours\": 19.66}, \"hypothesis\": \"VLA-mean baseline (K=10, mean aggregation) seed=45 on LIBERO object benchmark. Completes seed=45 six-way comparison. seed42=12%, seed43=15%, seed44=running.\", \"reproduce\": {\"finished_at\": \"2026-05-17T03:29:41.019Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T03:29:45.978517+00:00\"}]}, \"metrics\": {\"overall_sr\": 0.13, \"total_success\": 13, \"total_rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}, \"multi_seed_summary\": \"seed42=12%, seed43=15%, seed44=10%, seed45=13%, mean=12.5%\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T06:54:28.933Z\"}, \"eval-argmin-object-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:44:23.744Z\", \"updated_at\": \"2026-05-17T06:53:28.467Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 45 --K 10 --output_file logs/eval_object_argmin_seed45.json\", \"server\": \"bjb2-28827\", \"gpu\": \"cuda:5\", \"pid\": \"215932\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-object-seed45.log\", \"submitted_at\": \"2026-05-16T07:45:06.846Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 45, \"model_name\": \"reconvla_argmin_baseline\", \"hypothesis\": \"argmin baseline K=10 seed=45 on LIBERO object. 4th seed baseline for Fisher test. Paired with eval-obs-only-object-norm02-seed45.\", \"data_path\": \"LIBERO object benchmark (10 tasks)\", \"data_count\": 100, \"wall_clock_seconds\": 60530.4, \"gpu_hours\": 16.81}, \"reproduce\": {\"finished_at\": \"2026-05-17T00:31:27.579Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T00:31:32.330885+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.12, \"successes\": 12, \"total_rollouts\": 100, \"tasks_completed\": \"10/10\"}, \"checkpoint_path\": \"N/A (eval-only)\", \"hypothesis\": \"Argmin baseline (conformal selection K=10, no correction) seed=45 on LIBERO Object. Highest priority: expands argmin multi-seed data from 3 to 4 seeds, balancing against obs_only 5 seeds for symmetric Fisher test. Expected 12-17% SR.\", \"completed_at\": \"2026-05-17T00:33:57.260Z\"}, \"eval-direct-correction-object-seed42-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T03:01:50.937Z\", \"updated_at\": \"2026-05-17T04:48:50.296Z\", \"hypothesis\": \"obs_only CRM 直接纠正单次 VLA 输出（K=1, 跳过 argmin selection），测试 CRM 本身是否有独立纠正价值。如果 SR > VLA-only (~11%)，说明 CRM correction 独立有效；如果 SR ≤ VLA-only，说明 multi-sample selection 是必要前提。Claim 1 (pipeline contribution) 的 ablation。\", \"parent\": \"eval-direct-correction-object-seed42-r2\", \"spec\": {\"command\": \"/root/miniconda3/bin/python -u src/evaluate.py --mode direct_correction --benchmark object --n_rollouts 10 --seed 42 --K 1 --checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/results_direct_correction_object_seed42.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO Object benchmark (10 tasks)\", \"data_count\": \"100 episodes (10 tasks x 10 rollouts)\", \"model_name\": \"obs_only CRM (327K params)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO Object\", \"gpu\": \"cuda:4\", \"pid\": 364076, \"tmux_session\": \"eval-dc-r2\", \"note\": \"Code patched: print every rollout instead of every 5. Root cause of prev failures: workers killed working processes because output interval was 7.5min (5 rollouts x 90s each).\", \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_direct_correction_object_seed42.log\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.14, \"total_episodes\": 100, \"successes\": 14, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 1, \"salad_dressing\": 1, \"bbq_sauce\": 4, \"ketchup\": 0, \"tomato_sauce\": 1, \"butter\": 1, \"milk\": 1, \"chocolate_pudding\": 3, \"orange_juice\": 2}}, \"completed_at\": \"2026-05-17T04:48:50.296Z\"}, \"eval-perdof-object-norm03-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T15:24:11.457Z\", \"updated_at\": \"2026-05-17T04:45:11.458Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_seed44.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"505419\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm03-seed44.log\", \"submitted_at\": \"2026-05-16T15:24:11.074Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_id\": \"cuda:2\", \"model_name\": \"crm_perdof_norm03\", \"seed\": 44, \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 48060.4, \"gpu_hours\": 13.35}, \"hypothesis\": \"perdof CRM (ε=0.3) seed=44 on LIBERO Object. 验证 perdof 在高 norm (0.3) 的退化程度（seed42=4%）。多 seed 确认 perdof progressive collapse 机制。\", \"reproduce\": {\"finished_at\": \"2026-05-17T04:41:11.191Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T04:41:18.547308+00:00\"}]}, \"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0.04, \"total_episodes\": 100, \"successes\": 4, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 1, \"salad_dressing\": 0, \"bbq_sauce\": 1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 1, \"milk\": 0, \"chocolate_pudding\": 1, \"orange_juice\": 0}}, \"completed_at\": \"2026-05-17T04:45:11.458Z\"}, \"eval-mag-perdof-norm02-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:07:31.626Z\", \"updated_at\": \"2026-05-17T03:31:42.118Z\", \"spec\": {\"parent\": \"eval-acr-object-v4-perdof\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_perdof\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"object benchmark, max_correction_norm=0.2, K=10, n_rollouts=10\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"127732\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-perdof-norm02-object.log\"}, \"hypothesis\": \"Object magnitude sweep: perdof CRM v3-norm at norm=0.2 on LIBERO object benchmark. Paired with obs_only norm=0.2 (running, 18% at 5/10) for magnitude comparison figure. Tests perdof at moderate correction norm on object domain.\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.11, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}, \"reproduce\": {\"finished_at\": \"2026-05-16T06:04:45.416Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T06:04:48.447852+00:00\"}]}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"completed_at\": \"2026-05-16T07:12:35.145Z\", \"parent\": \"eval-acr-object-v3\"}, \"eval-acr-object-v4-scalar\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T02:53:44.102Z\", \"updated_at\": \"2026-05-17T03:31:41.215Z\", \"hypothesis\": \"D021: scalar_unc CRM v3-norm with max_correction_norm=0.1 on LIBERO object benchmark. Three-way ablation: perdof vs scalar_unc vs obs_only on object.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:3\"], \"pid\": \"14003\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-scalar.log\", \"submitted_at\": \"2026-05-15T02:53:43.910Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 47778.8, \"gpu_hours\": 13.27}, \"metrics\": {\"overall_sr\": 9, \"total_success\": 9, \"total_trials\": 100, \"n_tasks\": 10, \"n_rollouts_per_task\": 10, \"per_task\": {\"alphabet_soup\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"cream_cheese\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"salad_dressing\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"bbq_sauce\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"ketchup\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"tomato_sauce\": {\"sr\": 0, \"success\": 0, \"trials\": 10}, \"butter\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"milk\": {\"sr\": 10, \"success\": 1, \"trials\": 10}, \"chocolate_pudding\": {\"sr\": 30, \"success\": 3, \"trials\": 10}, \"orange_juice\": {\"sr\": 20, \"success\": 2, \"trials\": 10}}}, \"reproduce\": {\"finished_at\": \"2026-05-15T16:07:26.276Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T16:07:28.510451+00:00\"}]}, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-scalar.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-15T16:10:02.679Z\", \"parent\": \"crm-train-v2-scalar-unc\"}, \"eval-mag-obsonly-norm02\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:16:21.006Z\", \"updated_at\": \"2026-05-17T03:31:40.288Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --max_correction_norm 0.2 --n_rollouts 10 --K 10 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_mag_obs_only_norm02.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"SmolVLA + CRM-v3-norm-obs_only\", \"seed\": 42, \"checkpoint_source\": \"crm-train-v3-norm-obs_only\", \"eval_data\": \"LIBERO spatial\"}, \"gpu\": \"bjb2-28827:cuda:5\", \"pid\": 15190, \"metrics\": {\"T0_between_plate_ramekin\": 90, \"T1_next_to_ramekin\": 100, \"T2_table_center\": 0, \"T3_on_cookie_box\": 30, \"T4_top_drawer\": 10, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 90, \"T7_on_stove\": 0, \"T8_next_to_plate\": 30, \"T9_on_wooden_cabinet\": 0, \"overall_sr\": 35, \"total_success\": 35, \"total_rollouts\": 100}, \"reproduce\": {\"finished_at\": \"2026-05-15T16:03:26.878Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T16:03:29.305763+00:00\"}]}, \"log_path\": \"/root/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm02.log\", \"conclusion\": \"negative\", \"checkpoint_path\": \"N/A (eval-only experiment)\", \"completed_at\": \"2026-05-15T16:06:23.063Z\", \"hypothesis\": \"obs_only CRM (ε=0.2) on LIBERO Spatial benchmark. Spatial benchmark 下 obs_only 最优 norm 是否同样为 0.2。如果 spatial 无明显分离，说明方法效果依赖 action distribution shift 程度。\", \"parent\": \"eval-acr-spatial-v3\"}, \"eval-mag-perdof-norm03\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:16:16.095Z\", \"updated_at\": \"2026-05-17T03:31:39.344Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --smolvla_path /root/autodl-tmp/models/smolvla_libero/\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": 100, \"model_name\": \"crm_v3_norm/perdof\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"log_path\": \"/root/runs/acr-vla-conformal-refinement/eval-mag-perdof-norm03.log\"}, \"gpu\": \"bjb2-28827:cuda:3\", \"pid\": 14260, \"metrics\": {\"overall_sr_10task\": 0.26, \"T0_sr\": 0.7, \"T1_sr\": 0.5, \"T2_sr\": 0.1, \"T3_sr\": 0.1, \"T4_sr\": 0, \"T5_sr\": 0, \"T6_sr\": 0.9, \"T7_sr\": 0.1, \"T8_sr\": 0.2, \"T9_sr\": 0, \"total_successes\": 26, \"total_rollouts\": 100, \"benchmark\": \"spatial\", \"max_correction_norm\": 0.3}, \"reproduce\": {\"finished_at\": \"2026-05-15T16:53:04.031Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T16:53:08.939326+00:00\"}]}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-15T17:17:49.711Z\", \"hypothesis\": \"perdof CRM (ε=0.3) on LIBERO Spatial benchmark. 高 norm 下 perdof 在 spatial 是否也出现退化。如果 spatial 无 collapse（与 obs_only 接近），说明 failure mode 与 task complexity 相关。\", \"parent\": \"eval-acr-spatial-v3\"}, \"eval-mag-perdof-norm005\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:16:10.924Z\", \"updated_at\": \"2026-05-17T03:31:38.448Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode acr_vla --max_correction_norm 0.05 --n_rollouts 10 --K 10 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_mag_perdof_norm005.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"SmolVLA + CRM-v3-norm-perdof\", \"seed\": 42, \"checkpoint_source\": \"crm-train-v3-norm-perdof\", \"eval_data\": \"LIBERO spatial\", \"log_path\": \"/root/runs/acr-vla-conformal-refinement/eval-mag-perdof-norm005.log\", \"checkpoint_path\": \"N/A (eval only)\"}, \"gpu\": \"bjb2-28827:cuda:1\", \"pid\": 13456, \"metrics\": {\"T0_between_plate_ramekin\": 50, \"T1_next_to_ramekin\": 100, \"T2_table_center\": 0, \"T3_on_cookie_box\": 30, \"T4_top_drawer\": 0, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 100, \"T7_on_stove\": 0, \"T8_next_to_plate\": 30, \"T9_on_wooden_cabinet\": 0, \"avg_SR_10task\": 31}, \"reproduce\": {\"finished_at\": \"2026-05-15T16:52:50.451Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T16:52:53.898813+00:00\"}]}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-15T17:24:59.482Z\", \"hypothesis\": \"perdof CRM (ε=0.05) on LIBERO Spatial benchmark. 低 norm 下 perdof 在 spatial 的表现。如果与 obs_only-0.05 一致（35%），说明低 norm 约束消除了 conditioning 差异。\", \"parent\": \"eval-acr-spatial-v3\"}, \"eval-mag-perdof-norm003\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:16:08.547Z\", \"updated_at\": \"2026-05-17T03:31:37.673Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode acr_vla --max_correction_norm 0.03 --n_rollouts 10 --K 10 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_mag_perdof_norm003.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"SmolVLA + CRM-v3-norm-perdof\", \"seed\": 42, \"checkpoint_source\": \"crm-train-v3-norm-perdof\", \"eval_data\": \"LIBERO spatial\"}, \"gpu\": \"bjb2-28827:cuda:0\", \"pid\": 13185, \"metrics\": {\"benchmark\": \"spatial\", \"mode\": \"acr_vla\", \"max_correction_norm\": 0.03, \"n_rollouts\": 10, \"K\": 10, \"seed\": 42, \"overall_sr\": 30, \"total_success\": 30, \"total_rollouts\": 100, \"tasks_done\": \"10/10\", \"per_task\": {\"T0_between_plate_ramekin\": 60, \"T1_next_to_ramekin\": 100, \"T2_table_center\": 0, \"T3_on_cookie_box\": 30, \"T4_top_drawer\": 10, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 80, \"T7_on_stove\": 0, \"T8_next_to_plate\": 20, \"T9_on_wooden_cabinet\": 0}}, \"reproduce\": {\"finished_at\": \"2026-05-15T16:32:37.390Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T16:32:42.080703+00:00\"}]}, \"log_path\": \"/root/runs/acr-vla-conformal-refinement/eval-mag-perdof-norm003.log\", \"checkpoint_path\": \"N/A (eval-only)\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-15T16:40:16.878Z\", \"hypothesis\": \"perdof CRM (ε=0.03) on LIBERO Spatial benchmark. 极低 norm 下 perdof 在 spatial 的表现。与 obs_only-0.03 (34%) 对比，验证低 norm 安全区域。\", \"parent\": \"eval-acr-spatial-v3\"}, \"eval-vla-mean-spatial\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T03:10:44.114Z\", \"updated_at\": \"2026-05-17T03:15:31.664Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode vla_only --baseline_mode mean --benchmark spatial --n_rollouts 10 --seed 42\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"143106\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"SmolVLA K=10 mean action (no conformal)\", \"seed\": 42, \"hypothesis\": \"K=10 mean baseline isolates multi-sampling averaging contribution vs conformal correction. Expected between vla_only K=1 (30%) and ACR-VLA.\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"log_path\": \"/root/autodl-tmp/eval_results/eval-vla-mean-spatial.log\"}, \"metrics\": {\"overall_success_rate_10tasks\": 0.32, \"total_successes\": 32, \"total_trials\": 100, \"T1\": 0.7, \"T2\": 1, \"T3\": 0, \"T4\": 0.3, \"T5\": 0, \"T6\": 0, \"T7\": 0.8, \"T8\": 0, \"T9\": 0.3, \"T10\": 0.1}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T22:12:39.100Z\", \"log_path\": \"/root/autodl-tmp/eval_results/eval-vla-mean-spatial.log\", \"checkpoint_path\": \"N/A (eval experiment)\", \"hypothesis\": \"VLA mean action (average of K=10 samples) on LIBERO-Spatial provides a strong baseline by reducing sampling noise — establishes whether sample averaging alone matches or exceeds single-sample VLA\", \"parent\": \"eval-spatial-v7-full\"}, \"eval-acr-object-obs-only-norm02\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:20:46.639Z\", \"updated_at\": \"2026-05-17T03:15:28.368Z\", \"spec\": {\"hypothesis\": \"obs-only CRM with norm=0.2 on object benchmark. Cross-benchmark norm sensitivity test — paired with eval-mag-obsonly-norm02 on spatial. If obs-only at norm=0.2 > norm=0.1 on both benchmarks → robust 'observation-conditioned correction' story.\", \"parent\": \"eval-acr-object-v4-obs-only\", \"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02.json\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:4\", \"pid\": 44270, \"tmux_session\": \"eval-acr-object-obs-only-norm02\", \"data_path\": \"LIBERO object benchmark (10 tasks)\", \"data_count\": 100, \"model_name\": \"crm_obs_only (327198 params)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark, 10 tasks x 10 rollouts\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-obs-only-norm02.log\"}, \"metrics\": {\"overall_sr\": 0.22, \"total_success\": 22, \"total_rollouts\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.4, \"ketchup\": 0.2, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.6, \"orange_juice\": 0.3}}, \"reproduce\": {\"finished_at\": \"2026-05-15T17:35:34.272Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:35:39.374197+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-obs-only-norm02.log\", \"completed_at\": \"2026-05-15T17:37:08.420Z\", \"hypothesis\": \"ACR with obs-only CRM and max_correction_norm=0.2 on LIBERO-Object achieves meaningful improvement over VLA-only baseline by applying visually-guided corrections without requiring action history\", \"parent\": \"crm-train-v2-obs-only\"}, \"eval-spatial-v7-full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T00:05:16.510Z\", \"updated_at\": \"2026-05-17T03:15:26.392Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 10 --seed 42\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"123761\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"lerobot/smolvla_libero\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/eval_results/eval-spatial-v7.log\", \"hypothesis\": \"SmolVLA baseline on libero_spatial with K=1 fix (vla_only single inference)\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\"}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.3, \"total_successes\": 30, \"total_episodes\": 100, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"pick_up_black_bowl_between_plate_and_ramekin\": 0.6, \"pick_up_black_bowl_next_to_ramekin\": 1, \"pick_up_black_bowl_from_table_center\": 0, \"pick_up_black_bowl_on_cookie_box\": 0.2, \"pick_up_black_bowl_in_top_drawer\": 0, \"pick_up_black_bowl_on_ramekin\": 0, \"pick_up_black_bowl_next_to_cookie_box\": 0.9, \"pick_up_black_bowl_on_stove\": 0, \"pick_up_black_bowl_next_to_plate\": 0.3, \"pick_up_black_bowl_on_wooden_cabinet\": 0}}, \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-14T01:45:58.391Z\", \"hypothesis\": \"Full ACR pipeline v7 (obs-only CRM, conformal selection, norm=0.1) on LIBERO-Spatial achieves improvement over VLA-only baseline (32%), validating the method on spatial reasoning tasks\", \"parent\": \"eval-smolvla-libero-spatial\"}, \"eval-object-v8-full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T00:05:25.647Z\", \"updated_at\": \"2026-05-17T03:15:25.342Z\", \"spec\": {\"hypothesis\": \"SmolVLA baseline on libero_object with K=1 fix (vla_only single inference)\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\", \"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 42\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"125830\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_object/\", \"data_count\": 100, \"model_name\": \"smolvla_libero\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/eval_results/eval-object-v6.log\"}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.13, \"total_successes\": 13, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}, \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-14T03:10:30.457Z\", \"hypothesis\": \"Full ACR pipeline v8 (obs-only CRM, K=10 conformal selection, norm=0.1) on LIBERO-Object achieves consistent improvement over VLA-only baseline (9-12%) across all 10 tasks with optimized hyperparameters\", \"parent\": \"eval-smolvla-libero-spatial\"}, \"precompute-v5-shard2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:55:02.277Z\", \"updated_at\": \"2026-05-17T03:15:19.323Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 python -u src/train_crm.py --precompute --benchmark spatial object --cache_dir /root/autodl-tmp/crm_cache_v5/ --K 10 --shard_id 2 --num_shards 3 --max_demos_per_task 10 --precompute_batch_size 4 --save_every 500\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"180480\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v5-shard2.log\", \"submitted_at\": \"2026-05-14T07:56:37.531Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial + object)\", \"data_count\": \"~8900 samples (shard 2 of 3)\", \"model_name\": \"SmolVLA 450M (precompute K=10 features)\", \"seed\": 42, \"hypothesis\": \"Phase 2 precompute with 8D state fix (C1) for per-DOF CRM retraining\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache_v5/\", \"wall_clock_seconds\": 5491.8, \"gpu_hours\": 1.53}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T09:28:09.308Z\", \"hypothesis\": \"Precompute v5 (shard 2/3) with normalized correction targets and L2-clipped labels — final data version enabling stable CRM v3 training with bounded correction magnitudes\", \"parent\": \"precompute-v4-shard2\"}, \"precompute-v5-shard1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:55:00.276Z\", \"updated_at\": \"2026-05-17T03:15:18.177Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=1 python -u src/train_crm.py --precompute --benchmark spatial object --cache_dir /root/autodl-tmp/crm_cache_v5/ --K 10 --shard_id 1 --num_shards 3 --max_demos_per_task 10 --precompute_batch_size 4 --save_every 500\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"180400\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v5-shard1.log\", \"submitted_at\": \"2026-05-14T07:56:35.789Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial + object)\", \"data_count\": \"~8900 samples (shard 1 of 3)\", \"model_name\": \"SmolVLA 450M (precompute K=10 features)\", \"seed\": 42, \"hypothesis\": \"Phase 2 precompute with 8D state fix (C1) for per-DOF CRM retraining\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache_v5/\", \"wall_clock_seconds\": 5492.1, \"gpu_hours\": 1.53}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T09:28:07.934Z\", \"hypothesis\": \"Precompute v5 (shard 1/3) with normalized correction targets and L2-clipped labels — final data version enabling stable CRM v3 training with bounded correction magnitudes\", \"parent\": \"precompute-v4-shard1\"}, \"precompute-v5-shard0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:54:59.383Z\", \"updated_at\": \"2026-05-17T03:15:17.511Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 python -u src/train_crm.py --precompute --benchmark spatial object --cache_dir /root/autodl-tmp/crm_cache_v5/ --K 10 --shard_id 0 --num_shards 3 --max_demos_per_task 10 --precompute_batch_size 4 --save_every 500\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"180251\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v5-shard0.log\", \"submitted_at\": \"2026-05-14T07:56:33.414Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial + object)\", \"data_count\": \"~8900 samples (shard 0 of 3)\", \"model_name\": \"SmolVLA 450M (precompute K=10 features)\", \"seed\": 42, \"hypothesis\": \"Phase 2 precompute with 8D state fix (C1) for per-DOF CRM retraining\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache_v5/\", \"wall_clock_seconds\": 5493.2, \"gpu_hours\": 1.53}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T09:28:06.626Z\", \"hypothesis\": \"Precompute v5 (shard 0/3) with normalized correction targets and L2-clipped labels — final data version enabling stable CRM v3 training with bounded correction magnitudes\", \"parent\": \"precompute-v4-shard0\"}, \"precompute-v4-shard2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T18:58:14.301Z\", \"updated_at\": \"2026-05-17T03:15:16.391Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 2 --num_shards 3 --seed 42 --K 10 --cache_dir /root/autodl-tmp/crm_cache/ 2>&1\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"69937\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v4-shard2.log\", \"submitted_at\": \"2026-05-13T18:58:14.266Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache/\", \"wall_clock_seconds\": 173960.7, \"gpu_hours\": 48.32}, \"reproduce\": {\"finished_at\": \"2026-05-13T20:09:25.582Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T20:09:26.379476+00:00\"}]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T19:17:35.000Z\", \"hypothesis\": \"Precompute v4 (shard 2/3) with corrected 8D state representation and proper conformal features — fixes data pipeline bugs from v1-v3 that caused downstream CRM training issues\", \"parent\": \"precompute-shard2\"}, \"precompute-v4-shard1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T18:58:12.183Z\", \"updated_at\": \"2026-05-17T03:15:15.362Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 1 --num_shards 3 --seed 42 --K 10 --cache_dir /root/autodl-tmp/crm_cache/ 2>&1\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"69793\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v4-shard1.log\", \"submitted_at\": \"2026-05-13T18:58:12.154Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache/\", \"wall_clock_seconds\": 173961.1, \"gpu_hours\": 48.32}, \"reproduce\": {\"finished_at\": \"2026-05-13T20:04:22.574Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T20:04:23.366356+00:00\"}]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T19:17:33.288Z\", \"hypothesis\": \"Precompute v4 (shard 1/3) with corrected 8D state representation and proper conformal features — fixes data pipeline bugs from v1-v3 that caused downstream CRM training issues\", \"parent\": \"precompute-shard1\"}, \"precompute-v4-shard0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T18:58:09.830Z\", \"updated_at\": \"2026-05-17T03:15:14.415Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 0 --num_shards 3 --seed 42 --K 10 --cache_dir /root/autodl-tmp/crm_cache/ 2>&1\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"69647\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v4-shard0.log\", \"submitted_at\": \"2026-05-13T18:58:09.802Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache/\", \"wall_clock_seconds\": 173962.3, \"gpu_hours\": 48.32}, \"reproduce\": {\"finished_at\": \"2026-05-13T20:04:45.258Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T20:04:50.222546+00:00\"}]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T19:17:32.128Z\", \"hypothesis\": \"Precompute v4 (shard 0/3) with corrected 8D state representation and proper conformal features — fixes data pipeline bugs from v1-v3 that caused downstream CRM training issues\", \"parent\": \"precompute-shard0\"}, \"eval-obs-only-object-norm01-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:12:01.937Z\", \"updated_at\": \"2026-05-17T03:15:05.867Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_obs_only_norm01_seed44.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"227086\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm01-seed44.log\", \"submitted_at\": \"2026-05-16T07:12:01.614Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_v3_norm_obs_only\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 45205.2, \"gpu_hours\": 12.56}, \"reproduce\": {\"finished_at\": \"2026-05-16T19:42:10.387Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T19:42:13.494105+00:00\"}]}, \"metrics\": {\"overall_sr\": 0.16, \"total_success\": 16, \"total_rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"completed_at\": \"2026-05-16T19:45:26.774Z\", \"hypothesis\": \"Obs-only CRM with norm=0.1 on LIBERO-Object seed=44 replicates seed=42 success, confirming that performance gains are robust across random seeds and not artifacts of a single initialization\", \"parent\": \"eval-acr-object-obs-only-norm02\"}, \"eval-vla-only-object-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T08:34:53.953Z\", \"updated_at\": \"2026-05-17T03:15:04.317Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python src/evaluate.py --benchmark object --mode vla_only --K 1 --seed 45 --output_file logs/eval_object_vla_only_seed45.json\", \"server\": \"bjb2-28827\", \"gpu_id\": \"cuda:4\", \"pid\": 221407, \"seed\": 45, \"model_name\": \"smolvla_libero\", \"data_path\": \"LIBERO object\", \"data_count\": 10, \"checkpoint_source\": \"N/A\", \"eval_data\": \"LIBERO object\", \"hypothesis\": \"VLA-only baseline K=1 seed=45 on LIBERO object. Reference for seed45 statistical comparison. seed42=12%, seed43=12%, seed44=10%.\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T14:56:50.174Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T14:56:52.057Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T14:56:54.606880+00:00\"}]}, \"metrics\": {\"overall_sr\": 0.09, \"successes\": 18, \"total\": 200, \"tasks_done\": 10}, \"hypothesis\": \"VLA-only baseline on LIBERO-Object seed=45 provides second additional seed for baseline variance estimation — multi-seed baselines required for statistical significance claims in paper\", \"parent\": \"eval-object-v8-full\"}, \"eval-vla-only-object-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:50:14.071Z\", \"updated_at\": \"2026-05-17T03:15:03.364Z\", \"spec\": {\"hypothesis\": \"D031: VLA-only baseline (K=1, single sample, no CRM) seed=43 on LIBERO object benchmark. Completes 7-way seed=43 comparison table. VLA-only seed=42 = 12% = argmin.\", \"parent\": \"eval-vla-only-object\", \"command\": \"CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 43 --K 1 --output_file logs/eval_object_vla_only_seed43.json\", \"server\": \"bjb1-32546\", \"data_path\": \"libero_object\", \"data_count\": 10, \"model_name\": \"vla_only\", \"seed\": 43, \"eval_data\": \"object\"}, \"metrics\": {\"overall_sr\": 0.12, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}, \"source\": \"json_file_verified_by_worker\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T18:46:38.180Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T18:46:39.481Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T18:46:41.461084+00:00\"}]}, \"notes\": \"seed=43 VLA-only 12% = seed=42 12%，baseline 跨 seed 完全一致。per-task 分布略有差异（seed43: chocolate_pudding 40% vs seed42: 20%, bbq_sauce 30% vs 20%），但总 SR 相同。确认 VLA-only 作为稳定 baseline。seed=43 六方对比表第一个完成点。\", \"hypothesis\": \"VLA-only baseline on LIBERO-Object seed=43 establishes multi-seed baseline variance — needed to determine if ACR improvements are statistically significant above baseline noise\", \"parent\": \"eval-object-v8-full\"}, \"eval-vla-mean-spatial-t10\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:20:02.901Z\", \"updated_at\": \"2026-05-17T03:14:58.588Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --baseline_mode mean --benchmark spatial --n_rollouts 10 --seed 42 --start_task 9 --output_file /root/autodl-tmp/eval_results/eval-vla-mean-spatial-t10.json\", \"server\": \"bjb2-40593\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 10, \"model_name\": \"smolvla_libero\", \"seed\": 42}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T01:32:23.773Z\", \"metrics\": {\"T10_on_wooden_shelf\": \"10% (1/10)\", \"note\": \"Only ran task 9 (start_task=9). T10 = wooden shelf task.\"}, \"log_path\": \"/root/autodl-tmp/eval_results/eval-vla-mean-spatial-t10.json\", \"checkpoint_path\": \"N/A (eval only)\", \"hypothesis\": \"VLA mean action on LIBERO-Spatial task 10 (wooden shelf) specifically — completing the last missing task from the earlier eval-vla-mean-spatial run to have full 10-task baseline numbers\", \"parent\": \"eval-vla-mean-spatial\"}, \"eval-reconvla-spatial-v3\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-13T23:04:34.297Z\", \"updated_at\": \"2026-05-17T03:14:57.896Z\", \"reproduce\": {\"finished_at\": \"2026-05-14T11:07:49.901Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-13T23:34:14.141Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:34:15.524386+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T11:07:51.915540+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode reconvla --benchmark spatial --n_rollouts 10 --seed 42 --K 10\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"118108\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"SampleConsensus (scalar Euclidean argmin)\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/eval_results/eval-reconvla-spatial-v3.log\", \"hypothesis\": \"SampleConsensus scalar baseline for ACR-VLA comparison\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\"}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.34, \"total_successes\": 34, \"total_rollouts\": 100, \"per_task\": {\"pick_up_black_bowl_between_plate_and_ramekin\": 0.6, \"pick_up_black_bowl_next_to_ramekin\": 1, \"pick_up_black_bowl_from_table_center\": 0, \"pick_up_black_bowl_on_cookie_box\": 0.3, \"pick_up_black_bowl_in_top_drawer\": 0.1, \"pick_up_black_bowl_on_ramekin\": 0.1, \"pick_up_black_bowl_next_to_cookie_box\": 0.9, \"pick_up_black_bowl_on_stove\": 0, \"pick_up_black_bowl_next_to_plate\": 0.4, \"pick_up_black_bowl_on_wooden_cabinet\": 0}}, \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"/root/autodl-tmp/eval_results/eval-reconvla-spatial-v3.log\", \"hypothesis\": \"ReconVLA (K=10 sample consensus without CRM) on LIBERO-Spatial establishes upper bound for pure sampling diversity benefit — if high, CRM correction adds value only at lower K; if low, confirms CRM is essential\", \"parent\": \"plan_014-reconvla-baseline\"}, \"eval-obs-only-spatial-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:43:42.283Z\", \"updated_at\": \"2026-05-17T03:14:57.225Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v2/obs_only/crm_best.pt\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"203968\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-spatial-v2.log\", \"submitted_at\": \"2026-05-14T12:43:42.188Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"CRM obs_only v2 (990D, no conformal features)\", \"seed\": 42, \"hypothesis\": \"obs_only CRM ablation — CRM without conformal features tests whether per-DOF conformal intervals are necessary for effective correction\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v2/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"parent\": \"crm-train-v2-obs-only\", \"failure_reason\": \"Bug: evaluate.py line 266 CRM load condition missing crm_obs_only, CRM was None throughout eval, all rollouts 0%. Replaced by eval-obs-only-spatial-v3.\", \"wall_clock_seconds\": 185.5, \"gpu_hours\": 0.05}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T12:46:47.663Z\", \"hypothesis\": \"Obs-only CRM v2 retrained on spatial data resolves the dimension mismatch from v1 and achieves meaningful improvement on LIBERO-Spatial by using benchmark-matched visual features\", \"parent\": \"eval-obs-only-spatial\"}, \"crm-train-v2-scalar-unc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T09:30:43.696Z\", \"updated_at\": \"2026-05-17T03:14:56.290Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=1 python -u src/train_crm.py --benchmark spatial object --cache_dir /root/autodl-tmp/crm_cache_v5/ --output_dir /root/autodl-tmp/checkpoints/crm_v2/scalar_unc/ --K 10 --epochs 50 --batch_size 512 --lr 0.016 --input_mode scalar_unc --seed 42\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"186964\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-train-v2-scalar-unc.log\", \"submitted_at\": \"2026-05-14T09:30:43.616Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/crm_cache_v5/\", \"data_count\": 26737, \"model_name\": \"CRM scalar-unc v2 (327K params, 8D state fix)\", \"seed\": 42, \"hypothesis\": \"Scalar CRM v2 ablation — per-DOF expected to outperform on task success rate despite similar val_loss\", \"wall_clock_seconds\": 9977.5, \"gpu_hours\": 2.77}, \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.047202, \"best_epoch\": 48, \"total_epochs\": 50, \"final_train_loss\": 0.069679, \"comparison_vs_old\": \"old_6D_buggy=0.008379, new=0.047202 (loss metric changed with v2 fix)\"}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v2/scalar_unc/crm_best.pt\", \"log_path\": \"/root/runs/acr-vla-conformal-refinement/crm-train-v2-scalar-unc.log\", \"completed_at\": \"2026-05-14T12:17:01.093Z\", \"hypothesis\": \"Training CRM to predict scalar uncertainty enables confidence-based action selection via conformal prediction, allowing adaptive correction magnitude based on model confidence\", \"parent\": \"plan_001-crm-smolvla\"}, \"crm-train-v2-perdof\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T09:30:40.796Z\", \"updated_at\": \"2026-05-17T03:14:55.328Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 python -u src/train_crm.py --benchmark spatial object --cache_dir /root/autodl-tmp/crm_cache_v5/ --output_dir /root/autodl-tmp/checkpoints/crm_v2/perdof/ --K 10 --epochs 50 --batch_size 512 --lr 0.016 --input_mode full --seed 42\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"186823\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-train-v2-perdof.log\", \"submitted_at\": \"2026-05-14T09:30:40.716Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/crm_cache_v5/\", \"data_count\": 26737, \"model_name\": \"CRM per-DOF v2 (337K params, 8D state fix, argmin base, L2 clip)\", \"seed\": 42, \"hypothesis\": \"Per-DOF CRM v2 with D016 fixes (8D state, argmin base, alpha=0.5, L2 clipping) improves over pre-fix version\", \"wall_clock_seconds\": 9979.5, \"gpu_hours\": 2.77}, \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.051684, \"best_epoch\": 48, \"total_epochs\": 50, \"final_train_loss\": 0.076748, \"comparison_vs_old\": \"old_6D_buggy=0.009046, new=0.051684 (loss metric changed with v2 fix)\"}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v2/perdof/crm_best.pt\", \"log_path\": \"/root/runs/acr-vla-conformal-refinement/crm-train-v2-perdof.log\", \"completed_at\": \"2026-05-14T12:17:00.195Z\", \"hypothesis\": \"Training CRM with per-DoF (per degree-of-freedom) correction output produces more fine-grained corrections than a single scalar, improving downstream task performance on multi-joint manipulation\", \"parent\": \"plan_001-crm-smolvla\"}, \"crm-train-v2-obs-only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T09:41:35.819Z\", \"updated_at\": \"2026-05-17T03:14:53.940Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 python -u src/train_crm.py --benchmark spatial object --cache_dir /root/autodl-tmp/crm_cache_v5/ --output_dir /root/autodl-tmp/checkpoints/crm_v2/obs_only/ --K 10 --epochs 50 --batch_size 512 --lr 0.016 --input_mode obs_only --seed 42\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"187913\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-train-v2-obs-only.log\", \"submitted_at\": \"2026-05-14T09:41:35.736Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/crm_cache_v5/\", \"data_count\": 26737, \"model_name\": \"CRM obs_only v2\", \"seed\": 42, \"wall_clock_seconds\": 9366.4, \"gpu_hours\": 2.6}, \"conclusion\": \"success\", \"metrics\": {\"best_val_loss\": 0.050501, \"best_epoch\": 50, \"total_epochs\": 50, \"final_train_loss\": 0.074839, \"comparison_vs_old\": \"old_6D_buggy=0.018312, new=0.050501 (loss metric changed with v2 fix)\"}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v2/obs_only/crm_best.pt\", \"log_path\": \"/root/runs/acr-vla-conformal-refinement/crm-train-v2-obs-only.log\", \"completed_at\": \"2026-05-14T12:17:42.122Z\", \"hypothesis\": \"Training a CRM with obs-only input (no action/proprio) can learn correction signals purely from visual observation features, enabling correction without access to action space information\", \"parent\": \"plan_001-crm-smolvla\"}, \"precompute-shard2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T11:57:48.056Z\", \"updated_at\": \"2026-05-17T03:13:50.200Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 2 --num_shards 3 --seed 42 --K 10\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"47186\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-shard2.log\", \"submitted_at\": \"2026-05-13T11:57:48.042Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache/\", \"wall_clock_seconds\": 12499.4, \"gpu_hours\": 3.47}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T15:26:07.463Z\", \"hypothesis\": \"Precomputing VLA action caches (shard 2/3) enables offline CRM training without repeated VLA inference — infrastructure prerequisite for scalable CRM training experiments\"}, \"precompute-shard1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T11:57:46.669Z\", \"updated_at\": \"2026-05-17T03:13:49.286Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 1 --num_shards 3 --seed 42 --K 10\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"47044\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-shard1.log\", \"submitted_at\": \"2026-05-13T11:57:46.654Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache/\", \"wall_clock_seconds\": 12499.8, \"gpu_hours\": 3.47}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T15:26:06.485Z\", \"hypothesis\": \"Precomputing VLA action caches (shard 1/3) enables offline CRM training without repeated VLA inference — infrastructure prerequisite for scalable CRM training experiments\"}, \"precompute-shard0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T11:57:45.284Z\", \"updated_at\": \"2026-05-17T03:13:43.682Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 0 --num_shards 3 --seed 42 --K 10\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"46966\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-shard0.log\", \"submitted_at\": \"2026-05-13T11:57:45.270Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache/\", \"wall_clock_seconds\": 12500.2, \"gpu_hours\": 3.47}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T15:26:05.433Z\", \"hypothesis\": \"Precomputing VLA action caches (shard 0/3) enables offline CRM training without repeated VLA inference — infrastructure prerequisite for scalable CRM training experiments\"}, \"precompute-k5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:15:37.603Z\", \"updated_at\": \"2026-05-17T03:13:41.787Z\", \"spec\": {\"command\": \"python -u src/train_crm.py --precompute --benchmark spatial object --K 5 --cache_dir /root/autodl-tmp/crm_cache_k5/\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"79517\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-k5.log\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 26737, \"model_name\": \"smolvla_libero\", \"seed\": 42, \"hypothesis\": \"K=5 precompute for K sensitivity ablation (plan_015)\"}, \"reproduce\": {\"finished_at\": \"2026-05-13T22:09:33.445Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T22:09:34.396952+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/crm_cache_k5/\", \"metrics\": {\"spatial_samples\": 12167, \"object_samples\": 14570, \"total_samples\": 26737, \"spatial_cache_mb\": 106, \"object_cache_mb\": 127, \"total_cache_mb\": 233, \"runtime_min\": 107}, \"completed_at\": \"2026-05-13T22:12:39.543Z\", \"hypothesis\": \"Precomputing K=5 VLA action samples provides sufficient diversity for conformal selection while reducing inference cost by 50% vs K=10 — testing efficiency-performance tradeoff\"}, \"plan_014-reconvla-baseline\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-13T06:56:12.892Z\", \"updated_at\": \"2026-05-17T03:13:39.823Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark spatial object --n_rollouts 20 --seed 42\", \"server\": \"autodl-4090\", \"gpu\": [\"cuda:0\"], \"pid\": \"50790\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/plan_014-reconvla-baseline.log\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial + object)\", \"data_count\": \"20 tasks x 20 rollouts = 400 episodes\", \"model_name\": \"SmolVLA (450M) + ReconVLA argmin selection\", \"seed\": 42, \"hypothesis\": \"ReconVLA (scalar Euclidean nonconformity + argmin selection) as baseline for ACR-VLA comparison\", \"fixes_applied\": [\"BDDL path: use benchmark_instance.get_task_bddl_file_path()\", \"LIBERO assets copied from GitHub repo\"]}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T11:07:20.019Z\", \"hypothesis\": \"ReconVLA baseline implementation validates that sample consensus (K=10 argmin Euclidean) provides meaningful improvement over single-sample VLA, establishing competitive baseline for ACR comparison\"}, \"plan_001-crm-smolvla\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T03:01:07.682Z\", \"updated_at\": \"2026-05-17T03:13:37.890Z\", \"spec\": {\"command\": \"python -u src/train_crm.py --auto --benchmark spatial object --epochs 50 --batch_size 32 --lr 1e-3 --seed 42 --K 10\", \"server\": \"autodl-4090\", \"gpu\": [\"cuda:0\"], \"pid\": \"32811\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/plan_001-crm-smolvla.log\", \"submitted_at\": \"2026-05-13T04:54:14.975Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial + object)\", \"data_count\": 1000, \"model_name\": \"CRM (337K) + SmolVLA (450M)\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm/\", \"hypothesis\": \"Per-DOF conformal features enable dimension-selective action correction on LIBERO\", \"wall_clock_seconds\": 2992.2, \"gpu_hours\": 0.83}, \"conclusion\": \"failed\", \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"completed_at\": \"2026-05-13T05:44:07.131Z\", \"hypothesis\": \"Initial CRM + SmolVLA integration plan validates that conformal residual module can be trained and integrated with a pretrained VLA model for action refinement\"}, \"mvp-point-reaching\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T01:22:10.415Z\", \"updated_at\": \"2026-05-17T03:13:35.534Z\", \"spec\": {\"hypothesis\": \"Per-DOF uncertainty features carry more actionable information than scalar uncertainty summaries, enabling dimension-selective correction\", \"description\": \"3D point-reaching MVP: 3 MLP variants (scalar/per-DOF/no uncertainty) x 6 groups (3 anisotropy ratios x 2 uncertainty sources)\", \"server\": \"bjb2-40593\", \"gpu\": \"cuda:0\", \"data_count\": 20000, \"model_name\": \"CorrectionMLP(2-layer, 64-hidden)\", \"seed\": 42, \"command\": \"python -u run_mvp.py\", \"data_path\": \"synthetic (generated in-script)\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/mvp/\", \"log_path\": \"/root/acr-vla-conformal-refinement/mvp/mvp_results.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T01:44:00.055Z\", \"metrics\": {\"group1_oracle\": {\"A_scalar\": {\"mse_x\": 0.180218, \"mse_y\": 0.02497, \"mse_z\": 0.024232, \"total\": 0.076473}, \"B_perDOF\": {\"mse_x\": 0.172652, \"mse_y\": 0.015544, \"mse_z\": 0.01561, \"total\": 0.067935}, \"C_none\": {\"mse_x\": 0.22706, \"mse_y\": 0.025542, \"mse_z\": 0.024753, \"total\": 0.092451}}, \"group2_oracle\": {\"A_scalar\": {\"mse_x\": 0.064642, \"mse_y\": 0.023836, \"mse_z\": 0.022967, \"total\": 0.037148}, \"B_perDOF\": {\"mse_x\": 0.053403, \"mse_y\": 0.015695, \"mse_z\": 0.01573, \"total\": 0.028276}, \"C_none\": {\"mse_x\": 0.084178, \"mse_y\": 0.025427, \"mse_z\": 0.024798, \"total\": 0.044801}}, \"group3_oracle\": {\"A_scalar\": {\"mse_x\": 0.042948, \"mse_y\": 0.023218, \"mse_z\": 0.022365, \"total\": 0.02951}, \"B_perDOF\": {\"mse_x\": 0.033008, \"mse_y\": 0.015621, \"mse_z\": 0.015647, \"total\": 0.021425}, \"C_none\": {\"mse_x\": 0.053043, \"mse_y\": 0.025523, \"mse_z\": 0.024741, \"total\": 0.034436}}, \"group4_K10\": {\"A_scalar\": {\"mse_x\": 0.187418, \"mse_y\": 0.024701, \"mse_z\": 0.024277, \"total\": 0.078799}, \"B_perDOF\": {\"mse_x\": 0.182888, \"mse_y\": 0.019072, \"mse_z\": 0.018475, \"total\": 0.073478}, \"C_none\": {\"mse_x\": 0.21507, \"mse_y\": 0.02496, \"mse_z\": 0.024637, \"total\": 0.088223}}, \"group5_K10\": {\"A_scalar\": {\"mse_x\": 0.064895, \"mse_y\": 0.02386, \"mse_z\": 0.023596, \"total\": 0.037451}, \"B_perDOF\": {\"mse_x\": 0.05851, \"mse_y\": 0.018868, \"mse_z\": 0.018471, \"total\": 0.03195}, \"C_none\": {\"mse_x\": 0.077047, \"mse_y\": 0.024825, \"mse_z\": 0.02464, \"total\": 0.042171}}, \"group6_K10\": {\"A_scalar\": {\"mse_x\": 0.041848, \"mse_y\": 0.02344, \"mse_z\": 0.023207, \"total\": 0.029498}, \"B_perDOF\": {\"mse_x\": 0.036348, \"mse_y\": 0.018736, \"mse_z\": 0.018453, \"total\": 0.024512}, \"C_none\": {\"mse_x\": 0.048365, \"mse_y\": 0.024827, \"mse_z\": 0.024577, \"total\": 0.03259}}, \"pass_criteria\": {\"group1\": \"PASS\", \"group4\": \"PASS\", \"overall\": \"SUCCESS\"}, \"summary_pct_improvements\": {\"reference_group\": \"group4_K10 (sigma=0.5/0.1/0.1, K=10 estimated uncertainty)\", \"perDOF_vs_scalar_total\": 6.75, \"perDOF_vs_none_total\": 16.71, \"perDOF_vs_scalar_y_axis\": 22.79, \"perDOF_vs_scalar_z_axis\": 23.9, \"paper_claims\": {\"6.7_pct_over_scalar\": \"group4 total: (0.078799-0.073478)/0.078799 = 6.75%\", \"16.7_pct_over_none\": \"group4 total: (0.088223-0.073478)/0.088223 = 16.71%\", \"22_24_pct_per_axis\": \"group4 y: 22.79%, z: 23.90%\"}}}, \"hypothesis\": \"MVP validation: CRM correction signals improve point-reaching accuracy in simplified task — if corrections reliably move end-effector toward targets, the mechanism transfers to full manipulation\"}, \"eval-smolvla-libero-spatial\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T11:35:16.236Z\", \"updated_at\": \"2026-05-17T03:13:33.197Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 3 --seed 42\", \"server\": \"autodl-4090x4\", \"gpu\": [\"cuda:0\"], \"pid\": \"43809\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": \"10 tasks x 3 rollouts x 300 steps\", \"model_name\": \"lerobot/smolvla_libero (450M, full fine-tuned on libero_spatial)\", \"seed\": 42, \"hypothesis\": \"Validate smolvla_libero checkpoint with fixed wrapper (correct state repr, 256x256 images, 7D action) achieves >50% success on libero_spatial\", \"log_path\": \"/tmp/eval_spatial_full.log\", \"checkpoint_source\": \"lerobot/smolvla_libero (HuggingFace community checkpoint)\", \"failure_reason\": \"smolvla_libero 0% on spatial - 6 wrapper bugs: image flip/size/normalization, state 6D→8D, state normalization, action denormalization all missing\", \"checkpoint_path\": \"N/A\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T15:45:51.082Z\", \"hypothesis\": \"SmolVLA pretrained model evaluates directly on LIBERO-Spatial without any CRM or conformal processing — establishing raw VLA capability as absolute floor baseline\"}, \"eval-obs-only-spatial\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:17:10.843Z\", \"updated_at\": \"2026-05-17T03:13:04.533Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v2/obs_only/crm_best.pt\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"197596\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-spatial.log\", \"submitted_at\": \"2026-05-14T12:17:10.754Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"CRM obs_only v2 (990D input, no conformal features)\", \"seed\": 42, \"hypothesis\": \"obs_only CRM ablation — CRM without conformal features\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v2/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"failure_reason\": \"evaluate.py has no crm_obs_only mode. --mode acr_vla loads CRM expecting 1030D input but obs_only checkpoint has 990D (no conformal features). Replaced by eval-obs-only-spatial-v2.\", \"wall_clock_seconds\": 1392.5, \"gpu_hours\": 0.39}, \"conclusion\": \"failed\", \"metrics\": {\"error\": \"size mismatch: obs_only CRM net.0.weight [256,990] vs acr_vla expects [256,1030] — no crm_obs_only mode in evaluate.py\"}, \"completed_at\": \"2026-05-14T12:40:23.205Z\", \"hypothesis\": \"Obs-only CRM trained on object benchmark generalizes to LIBERO-Spatial tasks without retraining — testing cross-benchmark transfer of visual correction signals\"}, \"eval-obs-only-object-default-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:13:41.913Z\", \"updated_at\": \"2026-05-17T03:09:38.443Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_default_seed44.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:5\"], \"pid\": \"229751\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-default-seed44.log\", \"submitted_at\": \"2026-05-16T07:13:41.570Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_v3_norm_obs_only\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 48315.0, \"gpu_hours\": 13.42}, \"reproduce\": {\"finished_at\": \"2026-05-16T20:36:24.235Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T20:36:28.363366+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.16, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-default-seed44.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"completed_at\": \"2026-05-16T20:38:56.577Z\", \"hypothesis\": \"obs_only CRM (default norm ~1.42) seed=44 on LIBERO Object. 验证 obs_only 在 uncapped norm 下的跨 seed 稳定性（seed42=17%）。如果维持 15-20%，确认极端 magnitude 鲁棒性。\"}, \"eval-mag-perdof-norm005-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:56:58.178Z\", \"updated_at\": \"2026-05-17T03:09:30.045Z\", \"spec\": {\"hypothesis\": \"Object magnitude sweep: perdof CRM v3-norm at norm=0.05 on LIBERO object benchmark. Paired with obs_only norm=0.05 for magnitude comparison figure.\", \"parent\": \"eval-acr-object-v4-perdof\", \"command\": \"python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_perdof_norm005.json\", \"server\": \"bjb2-28827\", \"gpu\": \"1\", \"pid\": 109650, \"data_path\": \"LIBERO object benchmark\", \"data_count\": 10, \"model_name\": \"crm_perdof\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object (10 tasks x 10 rollouts)\", \"log_path\": \"logs/nohup_eval_object_perdof_norm005.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\"}, \"metrics\": {\"overall_sr\": 0.14, \"successes\": 14, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10}, \"reproduce\": {\"finished_at\": \"2026-05-16T08:36:33.616Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T08:36:35.355Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T08:36:40.842032+00:00\"}]}, \"hypothesis\": \"perdof CRM (ε=0.05) seed=42 on LIBERO Object. 验证 perdof 在极低 norm 下是否与 obs_only 接近（两者都受限于低 norm 纠正量）。magnitude curve 低端数据点。\"}, \"eval-mag-perdof-norm02-seed43-object-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:34:16.821Z\", \"updated_at\": \"2026-05-17T03:09:27.225Z\", \"spec\": {\"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_perdof\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed43_r3.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"144504\"}, \"metrics\": {\"overall_sr\": 0.09, \"successes\": 9, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}, \"vs_seed42\": \"-2pp (11% → 9%)\", \"pooled_2seed_perdof_02\": \"10% (20/200)\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T10:39:30.416Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T10:39:33.739829+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"log_path\": \"logs/eval_object_perdof_norm02_seed43_r3.json\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T10:41:59.362Z\", \"hypothesis\": \"perdof CRM (ε=0.2) seed=43 on LIBERO Object. 验证 perdof 在 norm=0.2 的多 seed 数据（seed42=11%）。确认 perdof 在中间 norm 的退化幅度具有跨 seed 一致性。\"}, \"eval-mag-perdof-norm03-object-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:26:52.169Z\", \"updated_at\": \"2026-05-17T03:09:17.332Z\", \"spec\": {\"server\": \"bjb2-28827\", \"gpu\": \"cuda:2\", \"pid\": 140759, \"command\": \"python -u src/evaluate.py --mode crm_perdof --benchmark object --seed 42 --K 10 --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_r3.json\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_v3_norm_perdof\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\"}, \"metrics\": {\"overall_sr\": 0.04, \"successes\": 4, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10}, \"reproduce\": {\"finished_at\": \"2026-05-16T11:10:32.044Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T11:10:33.866Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T11:10:39.747200+00:00\"}]}, \"hypothesis\": \"perdof CRM (ε=0.3) seed=42 on LIBERO Object magnitude sweep. 验证 perdof 在 norm=0.3 的 collapse 程度。预期 SR 急剧下降（支持 progressive collapse 叙事）。\"}, \"eval-mag-obsonly-norm005\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:16:18.917Z\", \"updated_at\": \"2026-05-17T03:09:15.263Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --max_correction_norm 0.05 --n_rollouts 10 --K 10 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_mag_obs_only_norm005.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"SmolVLA + CRM-v3-norm-obs_only\", \"seed\": 42, \"checkpoint_source\": \"crm-train-v3-norm-obs_only\", \"eval_data\": \"LIBERO spatial\"}, \"gpu\": \"bjb2-28827:cuda:4\", \"pid\": 14854, \"metrics\": {\"benchmark\": \"spatial\", \"mode\": \"crm_obs_only\", \"max_correction_norm\": 0.05, \"n_rollouts\": 10, \"K\": 10, \"overall_sr\": 35, \"total_success\": 35, \"total_episodes\": 100, \"per_task\": {\"T0_between_plate_ramekin\": 80, \"T1_next_to_ramekin\": 90, \"T2_table_center\": 0, \"T3_on_cookie_box\": 40, \"T4_top_drawer\": 10, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 80, \"T7_on_stove\": 0, \"T8_next_to_plate\": 50, \"T9_on_wooden_cabinet\": 0}}, \"reproduce\": {\"finished_at\": \"2026-05-15T16:00:02.717Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T16:00:09.569232+00:00\"}]}, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm005.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T16:02:08.945Z\", \"hypothesis\": \"obs_only CRM (ε=0.05) on LIBERO Spatial benchmark. 低 norm 在 spatial 上的表现。与 object 的 0.05 数据点对比，检验 benchmark 间一致性。\"}, \"eval-mag-obsonly-norm003-b2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:20:45.606Z\", \"updated_at\": \"2026-05-17T03:09:11.273Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_mag_obsonly_norm003.json\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"225139\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm003-b2.log\", \"submitted_at\": \"2026-05-15T05:20:45.407Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_spatial\", \"data_count\": 10, \"model_name\": \"crm_v3_norm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"libero_spatial\", \"wall_clock_seconds\": 70039.8, \"gpu_hours\": 19.46}, \"pid\": 227426, \"notes\": \"Ghost PID 211962 killed, b2 now running solo on bjb2-40593 cuda:0. PID 227434 confirmed alive (15min uptime, model loaded, eval executing, GPU 6185MiB/24564MiB, 12% util).\", \"metrics\": {\"overall_sr_10task\": 0.34, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task\": {\"between_plate_and_ramekin\": 0.9, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.8, \"on_stove\": 0, \"next_to_plate\": 0.3, \"on_wooden_cabinet\": 0}}, \"reproduce\": {\"finished_at\": \"2026-05-16T00:42:50.652Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T00:43:27.876843+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_mag_obsonly_norm003.json\", \"completed_at\": \"2026-05-16T00:48:05.254Z\", \"hypothesis\": \"obs_only CRM (ε=0.03) on LIBERO Spatial benchmark. 极低 norm 下 obs_only 在 spatial 的表现（10-task SR）。验证 magnitude 效应在不同 benchmark 上的一致性。\"}, \"eval-mag-obsonly-norm03-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:29:02.155Z\", \"updated_at\": \"2026-05-17T03:09:10.586Z\", \"spec\": {\"hypothesis\": \"Object magnitude sweep: obs_only CRM v3-norm at norm=0.3 on LIBERO object benchmark. Tests degradation at higher correction norm on object domain. Key data for fig3.\", \"parent\": \"eval-acr-object-v4-obs-only\", \"command\": \"CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03.json\", \"server\": \"bjb2-28827\", \"data_path\": \"simpler_env object benchmark\", \"data_count\": 10, \"model_name\": \"crm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"object benchmark, max_correction_norm=0.3, K=10, n_rollouts=10\", \"pid\": 103028, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03.log\"}, \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.19, \"successes\": 19, \"total\": 100}, \"reproduce\": {\"finished_at\": \"2026-05-16T07:35:42.126Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T07:35:43.889Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T07:35:47.235304+00:00\"}]}, \"hypothesis\": \"obs_only CRM (ε=0.3) on LIBERO Object magnitude sweep seed=42. 验证高 norm 下 obs_only 是否仍保持 graceful degradation（对比 perdof 在同 norm 的 collapse）。\"}, \"eval-mag-obsonly-norm005-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:29:00.724Z\", \"updated_at\": \"2026-05-17T03:09:06.864Z\", \"spec\": {\"hypothesis\": \"Object magnitude sweep: obs_only CRM v3-norm at norm=0.05 on LIBERO object benchmark. Builds object magnitude curve alongside norm=0.1 (19%) and norm=0.2 (18% partial). Key data for fig3.\", \"parent\": \"eval-acr-object-v4-obs-only\", \"command\": \"CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_obs_only_norm005.json\", \"server\": \"bjb2-28827\", \"data_path\": \"simpler_env object benchmark\", \"data_count\": 10, \"model_name\": \"crm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"object benchmark, max_correction_norm=0.05, K=10, n_rollouts=10\", \"pid\": 101610, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005.log\"}, \"metrics\": {\"overall_sr\": 0.13, \"tasks_completed\": 10, \"total_rollouts\": 100, \"successes\": 13, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"success\", \"checkpoint_path\": \"logs/eval_object_obs_only_norm005.json\", \"completed_at\": \"2026-05-16T08:19:41.189Z\", \"hypothesis\": \"obs_only CRM (ε=0.05) on LIBERO Object magnitude sweep seed=42. 验证极低 norm 下 obs_only 表现。如果 SR 与 VLA-only 相近（12%），说明过低 norm 约束了 CRM 纠正能力。\"}, \"eval-direct-correction-object-seed42-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T02:46:15.008Z\", \"updated_at\": \"2026-05-17T03:04:54.543Z\", \"hypothesis\": \"obs_only CRM 直接纠正单次 VLA 输出（K=1, 跳过 argmin selection），测试 CRM 本身是否有独立纠���价值。如果 SR > VLA-only (~11%)，说明 CRM correction 独立有效；如果 SR ≤ VLA-only，说明 multi-sample selection 是必要前提。Claim 1 (pipeline contribution) 的 ablation。\", \"parent\": \"eval-direct-correction-object-seed42\", \"spec\": {\"command\": \"/root/miniconda3/bin/python -u src/evaluate.py --mode direct_correction --benchmark object --n_rollouts 10 --seed 42 --K 1 --checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/results_direct_correction_object_seed42.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO Object benchmark (10 tasks)\", \"data_count\": \"100 episodes (10 tasks x 10 rollouts)\", \"model_name\": \"obs_only CRM (327K params)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO Object\", \"gpu\": \"cuda:4\", \"pid\": 364076, \"note\": \"Code patched to print every rollout (was every 5). Prev attempts killed working processes due to misinterpreting silence as stuck.\"}, \"reproduce\": {\"finished_at\": \"2026-05-17T02:58:54.670Z\"}, \"failure_reason\": \"Agent误杀：wchar未增长30s被误判为stuck，实际是每5 rollout打印一次（~7.5min间隔）且MuJoCo/CUDA使用memory-mapped I/O不被/proc/PID/io追踪。进程实际正常运行中。\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-17T02:58:57.101Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T02:59:01.101476+00:00\"}]}}, \"eval-direct-correction-object-seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T02:18:02.194Z\", \"updated_at\": \"2026-05-17T02:38:55.611Z\", \"hypothesis\": \"obs_only CRM 直接纠正单次 VLA 输出（跳过 K=10 采样+argmin 选择），测试 obs 特征鲁棒性在简化 pipeline 下是否成立。如果 SR > VLA-only (~11%)，说明 CRM 本身有独立价值；如果 SR < VLA-only，说明 selection 是必要前提。Claim 1 (pipeline contribution) 的 ablation。\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode direct_correction --benchmark object --n_rollouts 10 --seed 42 --K 1 --checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/results_direct_correction_object_seed42.json\", \"server\": \"bjb1-32546\", \"gpu\": \"1\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 10, \"model_name\": \"obs_only CRM v3-norm\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark (10 tasks x 10 rollouts)\", \"pid\": 353384, \"tmux_session\": \"eval-direct-correction-object-seed42\"}, \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-17T02:38:55.611Z\"}, \"eval-obs-only-object-norm02-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:44:19.258Z\", \"updated_at\": \"2026-05-16T21:33:38.747Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_seed45.json\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:3\", \"pid\": \"233544\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-seed45.log\", \"submitted_at\": \"2026-05-16T07:44:18.928Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 45, \"model_name\": \"crm_v3_norm_obs_only\", \"hypothesis\": \"obs_only CRM v3-norm norm=0.2 seed=45 on LIBERO object. 4th seed pre-deployed for statistical power.\", \"data_path\": \"LIBERO object benchmark (10 tasks)\", \"data_count\": 100, \"wall_clock_seconds\": 49759.8, \"gpu_hours\": 13.82}, \"reproduce\": {\"finished_at\": \"2026-05-16T21:21:10.527Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T21:21:15.588019+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.16, \"successes\": 16, \"total_rollouts\": 100, \"tasks_completed\": \"10/10\"}, \"checkpoint_path\": \"N/A (eval only)\", \"hypothesis\": \"obs_only CRM (ε=0.2) seed=45 on LIBERO object: if obs_only maintains 16-22% SR range consistent with seeds 42-44, it confirms the method's reliability across random seeds and strengthens pooled statistical test vs argmin.\", \"completed_at\": \"2026-05-16T21:33:38.747Z\"}, \"eval-scalar-object-seed44-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:11:59.390Z\", \"updated_at\": \"2026-05-16T21:29:49.586Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_scalar_seed44_r2.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": \"226878\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-scalar-object-seed44-r2.log\", \"submitted_at\": \"2026-05-16T07:11:59.066Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_v3_norm_scalar_unc\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 51470.5, \"gpu_hours\": 14.3}, \"reproduce\": {\"finished_at\": \"2026-05-16T21:11:40.494Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T21:11:48.900516+00:00\"}]}, \"hypothesis\": \"Scalar CRM seed=44 on LIBERO object benchmark. Retry of failed eval-scalar-object-seed44. Expects scalar variant underperforms obs_only but may match argmin baseline.\", \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.06, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-16T21:29:49.586Z\"}, \"eval-perdof-object-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T04:56:22.235Z\", \"updated_at\": \"2026-05-16T19:45:27.956Z\", \"hypothesis\": \"perdof CRM v3-norm seed=44 on LIBERO object benchmark. Completes seed=44 four-way comparison. seed42=11%, seed43=12%. Expected to confirm perdof < argmin.\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-16T04:57:04.525Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --benchmark object --mode crm_perdof --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1 --K 10 --seed 44 --n_rollouts 10 --output_file logs/eval_object_perdof_seed44.json\\\"\", \"finished_at\": \"2026-05-16T18:13:35.112Z\", \"training_hours\": 13.28}, \"spec\": {\"data_path\": \"LIBERO_object\", \"data_count\": 100, \"model_name\": \"crm_perdof\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO_object_10tasks_10rollouts\"}, \"pid\": \"452982\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-seed44.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T18:13:38.573783+00:00\"}]}, \"metrics\": {\"overall_sr\": 0.08, \"total_success\": 8, \"total_rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"completed_at\": \"2026-05-16T19:45:27.956Z\"}, \"eval-obs-only-object-norm03-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T06:05:51.470Z\", \"updated_at\": \"2026-05-16T19:37:12.898Z\", \"hypothesis\": \"obs_only CRM v3-norm at norm=0.3 seed=44 on LIBERO object benchmark. Multi-seed magnitude curve coverage. seed42 norm=0.3 object still running on bjb2-28827. Pairs with seed44 norm=0.2 for norm sensitivity across seeds.\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-32546\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-16T06:06:08.369Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03_seed44.json\\\"\", \"finished_at\": \"2026-05-16T19:34:37.134Z\", \"training_hours\": 13.47}, \"spec\": {\"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_obs_only (327198 params)\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\"}, \"pid\": \"220777\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm03-seed44.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T19:34:40.416412+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.18, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"completed_at\": \"2026-05-16T19:37:12.898Z\"}, \"eval-vla-mean-object-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T04:58:30.713Z\", \"updated_at\": \"2026-05-16T18:36:08.965Z\", \"hypothesis\": \"VLA-mean baseline (K=10, mean aggregation) seed=44 on LIBERO object benchmark. Completes seed=44 six-way comparison. seed42=12%, seed43=15%.\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-32546\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-16T04:58:47.863Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode mean --n_rollouts 10 --K 10 --seed 44 --output_file logs/eval_object_vla_mean_seed44.json\\\"\", \"finished_at\": \"2026-05-16T18:33:19.875Z\", \"training_hours\": 13.58}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode mean --n_rollouts 10 --K 10 --seed 44 --output_file logs/eval_object_vla_mean_seed44.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"212655\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-mean-object-seed44.log\", \"submitted_at\": \"2026-05-16T04:58:50.101Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 49038.9, \"gpu_hours\": 13.62}, \"pid\": \"212655\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-mean-object-seed44.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T18:33:23.084588+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.1, \"per_task_sr\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.1, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.3, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0.1, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0.1, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 0, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.2, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.2}}, \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed44.json\", \"completed_at\": \"2026-05-16T18:36:08.965Z\"}, \"eval-obs-only-object-norm02-seed44-r4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T14:48:54.894Z\", \"updated_at\": \"2026-05-16T15:36:08.207Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_seed44_r4.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"501420\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-seed44-r4.log\", \"submitted_at\": \"2026-05-16T14:49:19.300Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1956.7, \"gpu_hours\": 0.54}, \"hypothesis\": \"P0 retry #4: obs_only CRM v3-norm norm=0.2 seed=44 on LIBERO object. Third seed for Fisher test. seed42=22%, seed43=16%. Previous attempts failed (127/129/killed).\", \"pid\": 501420, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T15:21:56.018Z\", \"failure_reason\": \"r2 data valid (16%), r4 redundant. PID 501420 killed by worker at 2026-05-16T15:09.\"}, \"eval-argmin-object-seed44-r2\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-16T01:32:14.163Z\", \"updated_at\": \"2026-05-16T15:34:00.414Z\", \"hypothesis\": \"Retry of eval-argmin-object-seed44 (EXIT_CODE=127, missing conda activate). argmin baseline K=10 seed=44 on LIBERO object. Third seed for Fisher test. seed42=12%, seed43=17%.\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-18228\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-16T01:32:36.214Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 44 --K 10 --output_file logs/eval_object_reconvla_seed44.json\\\"\", \"finished_at\": \"2026-05-16T15:28:27.588Z\", \"training_hours\": 13.93}, \"completed_at\": \"2026-05-16T01:34:17.696Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"killed\"}, \"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T15:28:32.358640+00:00\"}]}, \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 44 --K 10 --output_file logs/eval_object_reconvla_seed44.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"428117\", \"seed\": 44, \"model_name\": \"reconvla_argmin\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.13, \"successes\": 13, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.5, \"orange_juice\": 0.2}, \"note\": \"EXIT_CODE=129 was SIGHUP after completion, results valid. log: logs/eval_object_reconvla_seed44.json\"}, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed44.json\"}, \"eval-obs-only-object-norm02-seed44-r2\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-16T01:32:15.187Z\", \"updated_at\": \"2026-05-16T15:25:14.349Z\", \"hypothesis\": \"Retry of eval-obs-only-object-norm02-seed44 (EXIT_CODE=127, missing conda activate). obs_only CRM norm=0.2 seed=44 on LIBERO object. Third seed for Fisher test. seed42=22% (PROJECT HIGH).\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-18228\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-16T01:32:45.643Z\", \"finished_at\": \"2026-05-16T14:40:32.978Z\", \"training_hours\": 13.13}, \"completed_at\": \"2026-05-16T01:34:19.695Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"killed\"}, \"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T14:40:38.399800+00:00\"}]}, \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_seed44.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"428406\", \"seed\": 44, \"model_name\": \"crm_obs_only_norm02\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100}, \"failure_reason\": null, \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.16, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}, \"checkpoint_path\": \"logs/eval_object_obs_only_norm02_seed44.json\"}, \"eval-obs-only-object-norm03-seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T11:14:47.376Z\", \"updated_at\": \"2026-05-16T11:30:59.542Z\", \"spec\": {\"model_name\": \"crm_v3_norm_obs_only\", \"seed\": 45, \"data_path\": \"LIBERO object benchmark (10 tasks)\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03_seed45.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"248860\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm03-seed45.log\", \"submitted_at\": \"2026-05-16T11:14:47Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 972.5, \"gpu_hours\": 0.27}, \"hypothesis\": \"obs_only CRM v3-norm at norm=0.3 seed=45 on LIBERO object benchmark. Multi-seed magnitude curve data point. seed42 norm=0.3=19%, seed44 norm=0.3=running. Extends magnitude robustness evidence to 3rd seed.\", \"conclusion\": \"failed\", \"failure_reason\": \"killed to resolve cuda:3 GPU conflict\", \"completed_at\": \"2026-05-16T11:30:59.542Z\"}, \"eval-acr-object-v4-default-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:11:49.844Z\", \"updated_at\": \"2026-05-16T09:00:15.290Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_object_perdof_default_norm_r2.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"390936\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-default-r2.log\", \"submitted_at\": \"2026-05-16T02:11:20Z\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_object\", \"data_count\": 10, \"model_name\": \"crm_perdof_default_norm\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"object\", \"wall_clock_seconds\": 24535.3, \"gpu_hours\": 6.82}, \"hypothesis\": \"v4-default (no magnitude control, norm≈1.42) on object benchmark — ablation to confirm catastrophic failure\", \"parent\": \"eval-acr-object-v4-default\", \"metrics\": {\"overall_sr\": 0, \"successes\": 0, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0, \"bbq_sauce\": 0, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0, \"orange_juice\": 0}, \"note\": \"actual mode=crm_perdof with default norm (~1.42), NOT crm_default. Confirms catastrophic failure at uncontrolled correction magnitude.\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"completed_at\": \"2026-05-16T09:00:15.290Z\"}, \"eval-mag-perdof-norm003-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:47:32.591Z\", \"updated_at\": \"2026-05-16T08:37:12.296Z\", \"hypothesis\": \"Object magnitude sweep: perdof CRM v3-norm at norm=0.03 on LIBERO object benchmark. Paired with obs_only norm=0.03 for magnitude comparison figure. Tests perdof at smallest correction norm on object domain.\", \"spec\": {\"command\": \"python src/evaluate.py --mode crm_perdof --max_correction_norm 0.03 --K 10 --seed 42 --benchmark object\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:0\"], \"pid\": 105938, \"log_path\": \"logs/eval_object_perdof_norm003.json\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_v3_perdof\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object\", \"parent\": \"eval-acr-object-v4-perdof\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"metrics\": {\"overall_success_rate\": 0.14, \"per_task_range\": \"0.0-0.4\"}}, \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.14, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.1}}, \"reproduce\": {\"finished_at\": \"2026-05-16T08:09:00.286Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T08:09:03.327886+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003.json\", \"completed_at\": \"2026-05-16T08:11:39.117Z\"}, \"eval-obs-only-object-norm02-seed43-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:58:27.783Z\", \"updated_at\": \"2026-05-16T07:46:23.704Z\", \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-seed43-r2.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\"}, \"hypothesis\": \"D031: obs_only CRM v3-norm norm=0.2 seed=43 on LIBERO object benchmark (r2 retry). P0 critical for statistical significance — seed42=22%, need seed43 pooled to 200 trials. Original crashed after 1 task.\", \"parent\": \"eval-obs-only-object-norm02-seed43\", \"metrics\": {\"overall_sr\": 0.16, \"successes\": 16, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}, \"vs_seed42\": \"-6pp (22% → 16%)\", \"vs_argmin_seed43\": \"-1pp (17% → 16%)\", \"pooled_2seed_obs_only_02\": \"19% (38/200)\", \"pooled_2seed_argmin\": \"14.5% (29/200)\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T07:21:07.838Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T07:21:10.900676+00:00\"}]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T07:23:48.849Z\"}, \"eval-vla-only-object-seed44-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:33:13.916Z\", \"updated_at\": \"2026-05-16T07:13:29.827Z\", \"hypothesis\": \"Retry of eval-vla-only-object-seed44 (r1 EXIT_CODE=127). VLA-only baseline K=1 seed=44 on LIBERO object. Third seed reference. seed42=12%, seed43=12%.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 44 --K 1 --output_file logs/eval_object_vla_only_seed44.json\\\"\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"286989\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-object-seed44-r2.log\", \"submitted_at\": \"2026-05-16T01:33:46.467Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 20383.4, \"gpu_hours\": 5.66}, \"server\": \"bjb2-40593\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb2-40593\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-16T01:33:44.353Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 44 --K 1 --output_file logs/eval_object_vla_only_seed44.json\\\"\", \"code_commit\": \"4b4e03d05161290989b1f19d6e13e077da681a41\", \"finished_at\": \"2026-05-16T04:58:56.451Z\", \"training_hours\": 3.42}, \"pid\": \"286989\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-object-seed44-r2.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T04:59:00.452305+00:00\"}]}, \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.1, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (vla_only baseline)\", \"completed_at\": \"2026-05-16T07:13:29.827Z\"}, \"eval-acr-object-obs-only-default\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:38:22.125Z\", \"updated_at\": \"2026-05-16T07:09:01.967Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_default_norm.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": 134094, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-obs-only-default.log\", \"submitted_at\": \"2026-05-15T17:38:21.517Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_v3_norm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark\", \"wall_clock_seconds\": 48640.4, \"gpu_hours\": 13.51}, \"hypothesis\": \"obs_only CRM v3-norm with DEFAULT max_correction_norm (~1.42, no magnitude control) on LIBERO object benchmark. Paired with eval-acr-object-v4-default (perdof default). Tests whether obs_only robustness holds even without magnitude capping — if yes, obs_only is fundamentally more robust than perdof regardless of norm setting.\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.17, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.5, \"orange_juice\": 0.3}}, \"reproduce\": {\"finished_at\": \"2026-05-16T06:41:19.269Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T06:41:22.516205+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"completed_at\": \"2026-05-16T07:09:01.967Z\"}, \"eval-scalar-object-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:02:31.432Z\", \"updated_at\": \"2026-05-16T06:04:05.747Z\", \"hypothesis\": \"D031: scalar_unc CRM v3-norm seed=43 on LIBERO object benchmark. Completes seed=43 six-way comparison table. scalar seed=42 was worst at 4% — seed=43 confirms.\", \"parent\": \"eval-acr-object-v4-scalar\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_scalar_seed43.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"114664\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-scalar-object-seed43.log\", \"submitted_at\": \"2026-05-15T16:03:30.400Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_object\", \"data_count\": 10, \"model_name\": \"crm_scalar\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"eval_data\": \"object\", \"wall_clock_seconds\": 50435.3, \"gpu_hours\": 14.01}, \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"avg_sr\": 10, \"per_task_sr\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 30, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 10, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 30, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 30}}, \"reproduce\": {\"finished_at\": \"2026-05-16T06:01:42.952Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T06:01:45.993724+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed43.json\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed43.json\", \"completed_at\": \"2026-05-16T06:04:05.747Z\"}, \"eval-mag-obsonly-norm003-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:47:31.254Z\", \"updated_at\": \"2026-05-16T05:56:01.541Z\", \"hypothesis\": \"Object magnitude sweep: obs_only CRM v3-norm at norm=0.03 on LIBERO object benchmark. Completes 5-point magnitude curve (0.03/0.05/0.1/0.2/0.3). Tests minimum effective correction magnitude on object domain.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_obs_only_norm003.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:0\"], \"pid\": 121325, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm003-object.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"object benchmark, max_correction_norm=0.03, K=10, n_rollouts=10\", \"parent\": \"eval-acr-object-v4-obs-only\"}, \"metrics\": {\"overall_sr\": 0.16, \"tasks_done\": 100, \"tasks_total\": 100, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0.2, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.1, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.4, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_butter_and_place_it_in_the_basket\": 0.1, \"pick_up_the_milk_and_place_it_in_the_basket\": 0.2, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.3, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.3}}, \"reproduce\": {\"finished_at\": \"2026-05-16T05:35:17.752Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T05:35:20.742243+00:00\"}]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T05:56:01.541Z\"}, \"eval-scalar-object-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T05:02:34.914Z\", \"updated_at\": \"2026-05-16T05:25:06.306Z\", \"hypothesis\": \"scalar_unc CRM v3-norm seed=44 on LIBERO object benchmark. Completes seed=44 six-way comparison. scalar seed42=9%, seed43 running (0% at 3/10). Expected worst CRM variant.\", \"server\": \"bjb2-40593\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb2-40593\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-16T05:02:50.780Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_scalar_seed44.json\\\"\", \"code_commit\": \"4b4e03d05161290989b1f19d6e13e077da681a41\", \"finished_at\": \"2026-05-16T05:05:30.084Z\", \"training_hours\": 0.04}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_scalar_seed44.json\\\"\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"310854\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-scalar-object-seed44.log\", \"submitted_at\": \"2026-05-16T05:25:05.983Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"pid\": \"309346\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-scalar-object-seed44.log\", \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-16T05:05:32.021Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T05:05:34.587431+00:00\"}]}}, \"eval-obs-only-object-norm02-seed44-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:34:30.429Z\", \"updated_at\": \"2026-05-16T04:59:20.094Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_seed44.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"431189\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-seed44-r3.log\", \"submitted_at\": \"2026-05-16T01:34:30.132Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 12290.0, \"gpu_hours\": 3.41}, \"hypothesis\": \"Retry of eval-obs-only-object-norm02-seed44 (r1 EXIT_CODE=127, r2 killed by agent). obs_only CRM norm=0.2 seed=44 on LIBERO object. Third seed for Fisher test. seed42=22% (PROJECT HIGH).\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T04:59:20.095Z\"}, \"eval-argmin-object-seed44-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:34:28.047Z\", \"updated_at\": \"2026-05-16T04:59:17.975Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 44 --K 10 --output_file logs/eval_object_reconvla_seed44.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"430985\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-object-seed44-r3.log\", \"submitted_at\": \"2026-05-16T01:34:27.679Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 12290.3, \"gpu_hours\": 3.41}, \"hypothesis\": \"Retry of eval-argmin-object-seed44 (r1 EXIT_CODE=127, r2 killed by agent). argmin baseline K=10 seed=44 on LIBERO object. Third seed for Fisher test. seed42=12%, seed43=17%.\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T04:59:17.975Z\"}, \"eval-vla-mean-object-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:46:28.667Z\", \"updated_at\": \"2026-05-16T04:53:17.141Z\", \"hypothesis\": \"D031: VLA-mean baseline (K=10, mean aggregation) seed=43 on LIBERO object benchmark. Completes seed=43 comparison table. If VLA-mean seed=43 ≈ obs_only seed=43 → CRM correction claim compressed.\", \"parent\": \"eval-vla-mean-object\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode mean --n_rollouts 10 --K 10 --seed 43 --output_file logs/eval_object_vla_mean_seed43.json\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:1\"], \"pid\": \"111709\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-mean-object-seed43.log\", \"submitted_at\": \"2026-05-15T15:47:37.968Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 43, \"model_name\": \"smolvla\", \"data_path\": \"libero/object\", \"data_count\": 10, \"checkpoint_source\": null, \"eval_data\": \"object\", \"wall_clock_seconds\": 47139.2, \"gpu_hours\": 13.09}, \"metrics\": {\"overall_sr\": 0.15, \"tasks_done\": 10, \"tasks_total\": 10, \"total_success\": 15, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.3, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.1}}, \"reproduce\": {\"finished_at\": \"2026-05-16T04:48:28.380Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T04:48:31.493092+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval-only)\", \"completed_at\": \"2026-05-16T04:53:17.141Z\"}, \"eval-perdof-object-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:19:49.586Z\", \"updated_at\": \"2026-05-16T03:15:39.287Z\", \"hypothesis\": \"D031 supplementary: perdof CRM v3-norm seed=43 on LIBERO object benchmark. Completes three-way comparison (obs_only vs argmin vs perdof) with doubled samples. If perdof seed=43 ≈ argmin seed=43 → confirms obs_only uniquely better.\", \"parent\": \"eval-acr-object-v4-perdof\", \"spec\": {\"command\": \"python evaluate.py --benchmark object --mode crm_perdof --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1 --K 10 --seed 43 --n_rollouts 10 --output_file logs/eval_object_perdof_seed43.json\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:1\", \"pid\": 365925, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-seed43.log\", \"submitted_at\": \"2026-05-15T13:21:00.347Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 43, \"model_name\": \"crm_perdof\", \"data_path\": \"LIBERO_object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO_object_10tasks_10rollouts\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"wall_clock_seconds\": 50078.9, \"gpu_hours\": 13.91}, \"metrics\": {\"overall_success_rate\": 0.12, \"tasks_done\": 10, \"tasks_total\": 10, \"total_rollouts\": 100, \"total_successes\": 12, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}, \"reproduce\": {\"finished_at\": \"2026-05-16T03:12:36.498Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T03:12:39.589841+00:00\"}]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T03:15:39.287Z\"}, \"eval-vla-only-object-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:29:00.342Z\", \"updated_at\": \"2026-05-16T01:33:29.678Z\", \"hypothesis\": \"D035 follow-up: VLA-only baseline (K=1) seed=44 on LIBERO object benchmark. Third seed reference point. seed42=12%, seed43=12%. Deployed on bjb2-40593.\", \"server\": \"bjb2-40593\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb2-40593\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-16T01:29:36.987Z\", \"command\": \"bash -c \\\"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 44 --K 1 --output_file logs/eval_object_vla_only_seed44.json\\\"\", \"code_commit\": \"4b4e03d05161290989b1f19d6e13e077da681a41\", \"finished_at\": \"2026-05-16T01:30:26.640Z\", \"training_hours\": 0.01}, \"spec\": {\"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"vla_only\", \"seed\": 44, \"checkpoint_source\": \"N/A\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\"}, \"pid\": \"unknown\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-object-seed44.log\", \"failure_reason\": \"EXIT_CODE=127 (command not found) — bash -c wrapping 或环境激活路径错误，bjb2-40593 上系统性问题，三个 seed44 实验全部同样失败\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-16T01:30:33.143Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T01:30:38.635650+00:00\"}]}}, \"eval-obs-only-object-norm02-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:28:59.304Z\", \"updated_at\": \"2026-05-16T01:32:51.127Z\", \"hypothesis\": \"D035 follow-up: obs_only CRM v3-norm norm=0.2 seed=44 on LIBERO object benchmark. Third seed for Fisher exact test. ε=0.2 is PROJECT HIGH config (seed42=22%). Paired with eval-argmin-object-seed44.\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-18228\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-16T01:29:31.218Z\", \"command\": \"bash -c \\\"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_seed44.json\\\"\", \"finished_at\": \"2026-05-16T01:30:14.217Z\", \"training_hours\": 0.01}, \"spec\": {\"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_obs_only (327198 params)\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\"}, \"pid\": \"unknown\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-seed44.log\", \"failure_reason\": \"EXIT_CODE=127: submit command missing conda activation (source /root/miniconda3/etc/profile.d/conda.sh && conda activate base). tmux runs sh, not bash — python not in PATH. Will retry as r2.\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-16T01:30:20.761Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T01:30:23.773246+00:00\"}]}}, \"eval-argmin-object-seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:28:58.358Z\", \"updated_at\": \"2026-05-16T01:32:49.190Z\", \"hypothesis\": \"D035 follow-up: argmin baseline (K=10) seed=44 on LIBERO object benchmark. Third seed for Fisher exact test statistical power. Paired with eval-obs-only-object-norm02-seed44. seed42=12%, seed43=17%.\", \"server\": \"bjb1-18228\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-18228\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-16T01:29:25.990Z\", \"command\": \"bash -c \\\"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 44 --K 10 --output_file logs/eval_object_reconvla_seed44.json\\\"\", \"finished_at\": \"2026-05-16T01:30:04.115Z\", \"training_hours\": 0.01}, \"spec\": {\"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"ReconVLA (argmin baseline)\", \"seed\": 44, \"checkpoint_source\": \"N/A (no CRM)\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\"}, \"pid\": \"unknown\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-object-seed44.log\", \"failure_reason\": \"EXIT_CODE=127: submit command missing conda activation (source /root/miniconda3/etc/profile.d/conda.sh && conda activate base). tmux runs sh, not bash — python not in PATH. Will retry as r2.\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-16T01:30:06.598Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T01:30:09.864458+00:00\"}]}}, \"eval-obs-only-object-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:58:46.063Z\", \"updated_at\": \"2026-05-16T00:51:14.618Z\", \"hypothesis\": \"D031: obs_only CRM v3-norm seed=43 on LIBERO object benchmark. Doubles sample size for Fisher exact test. seed=42 shows obs_only 16% vs argmin 8% (+8pp, p≈0.19). Combined 200 trials target p < 0.05.\", \"parent\": \"eval-acr-object-v4-obs-only\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_obs_only_seed43.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"356490\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_seed43.json\", \"submitted_at\": \"2026-05-15T12:00:38.618Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_obs_only + SmolVLA\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark (10 tasks x 10 rollouts)\", \"wall_clock_seconds\": 46070.8, \"gpu_hours\": 12.8, \"checkpoint_path\": \"N/A (eval only)\"}, \"metrics\": {\"overall_success_rate\": 0.12, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}, \"vs_argmin_seed43\": {\"obs_only\": 12, \"argmin\": 17, \"diff\": -5}, \"fisher_pooled\": {\"obs_only_total\": \"31/200\", \"argmin_total\": \"29/200\", \"pooled_obs_only_sr\": 0.155, \"pooled_argmin_sr\": 0.145, \"pooled_delta\": 0.01, \"odds_ratio\": 1.08, \"p_value_one_sided\": 0.4444, \"p_value_two_sided\": 0.8888}, \"source\": \"json_file_verified_by_worker\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T00:41:25.212Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T00:42:01.902179+00:00\"}]}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_seed43.json\", \"completed_at\": \"2026-05-16T00:48:29.446Z\"}, \"eval-mag-obsonly-norm03-b2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:05:41.192Z\", \"updated_at\": \"2026-05-16T00:49:21.141Z\", \"hypothesis\": \"Magnitude sweep: obs_only CRM v3-norm at norm=0.3 on spatial. Retry of eval-mag-obsonly-norm03 (EXIT_CODE=127). Fills obs_only norm=0.3 gap. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade, strong evidence for obs_only robustness.\", \"parent\": \"eval-mag-obsonly-norm03\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_mag_obsonly_norm03_b2.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"130104\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm03-b2.log\", \"submitted_at\": \"2026-05-15T19:11:50.323Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 20250.8, \"gpu_hours\": 5.63}, \"conclusion\": \"failed\", \"notes\": \"Killed: duplicate of eval-mag-obsonly-norm03-r2 on same cuda:0. r2 had 15min more progress. Both wrote same output_file, causing potential corruption.\", \"reproduce\": {\"finished_at\": \"2026-05-15T07:10:36.759Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T07:10:39.645469+00:00\"}]}, \"completed_at\": \"2026-05-16T00:49:21.141Z\"}, \"eval-argmin-object-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:58:46.739Z\", \"updated_at\": \"2026-05-16T00:37:43.289Z\", \"hypothesis\": \"D031: argmin baseline (K=10, scalar Euclidean argmin) seed=43 on LIBERO object benchmark. Paired with eval-obs-only-object-seed43 for Fisher exact test. Need both conditions under same seed for valid comparison.\", \"parent\": \"eval-reconvla-object\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 43 --K 10 --output_file logs/eval_object_reconvla_seed43.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"356696\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-object-seed43.log\", \"submitted_at\": \"2026-05-15T12:00:40.708Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"ReconVLA (reconvla baseline)\", \"seed\": 43, \"checkpoint_source\": \"N/A (no CRM, pure VLA baseline)\", \"eval_data\": \"LIBERO object benchmark (10 tasks x 10 rollouts)\", \"checkpoint_path\": \"N/A\", \"wall_clock_seconds\": 45422.6, \"gpu_hours\": 12.62}, \"metrics\": {\"overall_success_rate\": 0.17, \"total_successes\": 17, \"total_trials\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.3, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}, \"reproduce\": {\"finished_at\": \"2026-05-16T00:35:16.646Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T00:35:19.825582+00:00\"}]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T00:37:43.289Z\"}, \"eval-mag-perdof-norm02-seed43-object-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:19:36.419Z\", \"updated_at\": \"2026-05-15T19:38:38.710Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed43.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"138858\", \"log_path\": \"N/A\", \"submitted_at\": \"2026-05-15T19:19:36.128Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (killed — GPU conflict on cuda:2, replaced by eval-mag-perdof-norm02-seed43-object-r3)\", \"wall_clock_seconds\": 951.1, \"gpu_hours\": 0.26}, \"hypothesis\": \"Object magnitude sweep: perdof CRM v3-norm norm=0.2 seed=43. Moved from bjb2-28827:cuda:3 (GPU conflict with obs_only spatial) to cuda:2. Tests perdof norm sensitivity with second seed.\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:35:27.220Z\"}, \"eval-mag-obsonly-norm03\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:43:48.583Z\", \"updated_at\": \"2026-05-15T19:38:31.587Z\", \"hypothesis\": \"Magnitude sweep: obs_only CRM v3-norm at norm=0.3 on spatial. Fills obs_only norm=0.3 gap. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade at same norm, strong evidence for obs_only robustness.\", \"parent\": \"eval-mag-obsonly-norm02\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_mag_obsonly_norm03.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"unknown\", \"log_path\": \"N/A\", \"submitted_at\": \"2026-05-15T06:44:02.425Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (EXIT_CODE=127, retried as eval-mag-obsonly-norm03-r2)\", \"wall_clock_seconds\": 46287.3, \"gpu_hours\": 12.86}, \"reproduce\": {\"finished_at\": \"2026-05-15T06:44:32.019Z\"}, \"failure_reason\": \"EXIT_CODE=127 (command not found — check bash -c wrapping / env activate)\", \"conclusion\": \"killed\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T06:44:35.317393+00:00\"}]}, \"notes\": \"失败原因: EXIT_CODE=127 — tmux 用 sh 执行命令，python 不在 sh PATH 中。修复: bash -c 包裹。已重试为 eval-mag-obsonly-norm03-r2。\", \"completed_at\": \"2026-05-15T19:35:29.718Z\"}, \"eval-mag-obsonly-norm02-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:26:53.269Z\", \"updated_at\": \"2026-05-15T19:34:07.651Z\", \"spec\": {\"hypothesis\": \"Object magnitude sweep: obs_only CRM v3-norm at norm=0.2 on LIBERO object benchmark. Fills the norm=0.2 gap in 5-point magnitude curve. Previous run reached 18% at 5/10 then stopped.\", \"parent\": \"eval-acr-object-v4-obs-only\", \"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_v2.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": 141024, \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"crm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark\", \"checkpoint_path\": \"N/A (duplicate of DONE eval-acr-object-obs-only-norm02, killed to free GPU)\", \"log_path\": \"N/A\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:34:07.651Z\"}, \"eval-mag-obsonly-norm03-b4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:14:01.998Z\", \"updated_at\": \"2026-05-15T19:27:30.465Z\", \"spec\": {\"command\": \"crm_obs_only spatial norm=0.3 (killed)\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"132816\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm03-b4.log\", \"submitted_at\": \"2026-05-15T19:14:01.050Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"spatial\", \"data_count\": 10, \"model_name\": \"crm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"spatial\", \"wall_clock_seconds\": 809.4, \"gpu_hours\": 0.22}, \"conclusion\": \"killed\", \"notes\": \"Redundant: spatial obs_only norm=0.3 already has 10t final data (36%). Killed from cuda:2 GPU contention cleanup on bjb2-28827 (2026-05-16).\", \"completed_at\": \"2026-05-15T19:27:30.465Z\"}, \"eval-mag-obsonly-norm03-b3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:13:38.067Z\", \"updated_at\": \"2026-05-15T19:27:28.479Z\", \"spec\": {\"command\": \"crm_obs_only spatial norm=0.3 (killed)\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"134532\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm03-b3.log\", \"submitted_at\": \"2026-05-15T19:14:52.972Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"spatial\", \"data_count\": 10, \"model_name\": \"crm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"spatial\", \"wall_clock_seconds\": 755.5, \"gpu_hours\": 0.21}, \"hypothesis\": \"Retry of eval-mag-obsonly-norm03-b2 (spatial magnitude sweep obs_only norm=0.3). Submitted on bjb2-28827:cuda:2 instead of bjb1-32546:cuda:3 (cuda:3 occupied by P0 obs-only-norm02-seed43-r2). Director approved.\", \"parent\": \"eval-mag-obsonly-norm03-b2\", \"conclusion\": \"killed\", \"notes\": \"Redundant: spatial obs_only norm=0.3 already has 10t final data (36%). Killed from cuda:2 GPU contention cleanup on bjb2-28827 (2026-05-16).\", \"completed_at\": \"2026-05-15T19:27:28.479Z\"}, \"eval-mag-perdof-norm02-seed43-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:15:19.724Z\", \"updated_at\": \"2026-05-15T19:25:28.957Z\", \"spec\": {\"hypothesis\": \"Object magnitude sweep: perdof CRM v3-norm norm=0.2 seed=43 on LIBERO object benchmark. Paired with obs_only norm=0.2 seed=43 for statistical comparison at the best obs_only norm.\", \"parent\": \"eval-mag-perdof-norm02-object\", \"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed43.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": \"10 rollouts\", \"model_name\": \"crm_v3_norm/perdof\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark\"}, \"conclusion\": \"killed\", \"notes\": \"Killed during cuda:2/3 GPU cleanup on bjb2-28827 (2026-05-16). Was sharing cuda:2 with perdof norm=0.3 r2.\", \"completed_at\": \"2026-05-15T19:25:28.957Z\"}, \"eval-mag-perdof-norm03-object-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:15:16.452Z\", \"updated_at\": \"2026-05-15T19:25:28.055Z\", \"spec\": {\"hypothesis\": \"Object magnitude sweep: perdof CRM v3-norm at norm=0.3 on LIBERO object benchmark. Retry of killed eval-mag-perdof-norm0p3-object. Completes perdof 5-point magnitude curve on object domain.\", \"parent\": \"eval-acr-object-v4-perdof\", \"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_r2.json\", \"server\": \"bjb2-28827\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": \"10 rollouts\", \"model_name\": \"crm_v3_norm/perdof\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object benchmark\"}, \"conclusion\": \"killed\", \"notes\": \"GPU contention on cuda:2 (shared with perdof norm=0.2 seed=43). Killed 2026-05-16. Replaced by r3 clean restart.\", \"completed_at\": \"2026-05-15T19:25:28.055Z\"}, \"eval-acr-object-v4-scalar-b2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T02:55:02.698Z\", \"updated_at\": \"2026-05-15T19:17:41.948Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"7017\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-scalar-b2.log\", \"submitted_at\": \"2026-05-15T02:55:02.415Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 58959.5, \"gpu_hours\": 16.38}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:17:41.948Z\"}, \"eval-acr-object-v4-obs-only-b2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T02:55:00.179Z\", \"updated_at\": \"2026-05-15T19:17:40.199Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:1\"], \"pid\": \"6746\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-obs-only-b2.log\", \"submitted_at\": \"2026-05-15T02:54:59.912Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 58960.3, \"gpu_hours\": 16.38}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:17:40.199Z\"}, \"eval-spatial-v4-full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T18:58:07.302Z\", \"updated_at\": \"2026-05-15T19:17:39.068Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl && python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 10 --seed 42 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ 2>&1\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"69379\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-spatial-v4-full.log\", \"submitted_at\": \"2026-05-13T18:58:07.274Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"D015: evaluate.py env_args 缺少 camera_names，SmolVLA 只收到单摄像头输入，结果系统性偏低\", \"wall_clock_seconds\": 173971.8, \"gpu_hours\": 48.33}, \"conclusion\": \"killed\", \"reproduce\": {\"finished_at\": \"2026-05-13T19:36:15.749Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T19:36:19.370112+00:00\"}]}, \"completed_at\": \"2026-05-15T19:17:39.068Z\"}, \"eval-reconvla-spatial-v1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:15:35.450Z\", \"updated_at\": \"2026-05-15T19:17:37.622Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --smolvla_path /root/autodl-tmp/models/smolvla_libero/\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"87787\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-reconvla-spatial-v1.log\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": \"10 tasks x 10 rollouts x 300 steps\", \"model_name\": \"lerobot/smolvla_libero (450M) + ReconVLA argmin selection K=10\", \"seed\": 42, \"hypothesis\": \"ReconVLA (scalar Euclidean nonconformity + argmin) as baseline for ACR-VLA comparison\", \"checkpoint_source\": \"lerobot/smolvla_libero\"}, \"reproduce\": {\"finished_at\": \"2026-05-13T22:59:43.231Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"conclusion\": \"killed\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T20:26:37.521060+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T22:59:44.694612+00:00\"}]}, \"completed_at\": \"2026-05-15T19:17:37.622Z\"}, \"eval-object-v6-full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:28:33.119Z\", \"updated_at\": \"2026-05-15T19:17:36.369Z\", \"spec\": {\"data_path\": \"/root/autodl-tmp/libero_data/ (object)\", \"data_count\": 100, \"model_name\": \"lerobot/smolvla_libero\", \"seed\": 42, \"hypothesis\": \"SmolVLA baseline success rate on libero_object with fixed evaluate.py (env.reset bug removed, 5-step zero-action stabilization)\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"libero_object 10 tasks x 10 rollouts\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:17:36.369Z\"}, \"precompute-v3-shard2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T17:39:04.708Z\", \"updated_at\": \"2026-05-15T19:17:30.541Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 2 --num_shards 3 --seed 42 --K 10 --cache_dir /root/autodl-tmp/crm_cache_v3\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"63218\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v3-shard2.log\", \"submitted_at\": \"2026-05-13T17:39:04.684Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"D014: wrapper 修复版从未部署到服务器，使用旧 buggy 代码运行，产出无效\", \"wall_clock_seconds\": 178705.9, \"gpu_hours\": 49.64}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:17:30.541Z\"}, \"precompute-v3-shard1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T17:39:02.628Z\", \"updated_at\": \"2026-05-15T19:17:29.292Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 1 --num_shards 3 --seed 42 --K 10 --cache_dir /root/autodl-tmp/crm_cache_v3\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"63075\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v3-shard1.log\", \"submitted_at\": \"2026-05-13T17:39:02.603Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"D014: wrapper 修复版从未部署到服务器，使用旧 buggy 代码运行，产出无效\", \"wall_clock_seconds\": 178706.7, \"gpu_hours\": 49.64}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:17:29.293Z\"}, \"precompute-v3-shard0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T17:39:00.259Z\", \"updated_at\": \"2026-05-15T19:17:27.703Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 && rm -rf /root/autodl-tmp/crm_cache_v3 && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 0 --num_shards 3 --seed 42 --K 10 --cache_dir /root/autodl-tmp/crm_cache_v3\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"62930\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v3-shard0.log\", \"submitted_at\": \"2026-05-13T17:39:00.236Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"D014: wrapper 修复版从未部署到服务器，使用旧 buggy 代码运行，产出无效\", \"wall_clock_seconds\": 178707.5, \"gpu_hours\": 49.64}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:17:27.703Z\"}, \"precompute-v2-shard2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T16:11:04.275Z\", \"updated_at\": \"2026-05-15T19:17:26.396Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 2 --num_shards 3 --seed 42 --K 10\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"57846\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v2-shard2.log\", \"submitted_at\": \"2026-05-13T16:11:04.255Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 183982.1, \"gpu_hours\": 51.11}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:17:26.396Z\"}, \"precompute-v2-shard1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T16:11:02.520Z\", \"updated_at\": \"2026-05-15T19:17:25.022Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 1 --num_shards 3 --seed 42 --K 10\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"57706\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v2-shard1.log\", \"submitted_at\": \"2026-05-13T16:11:02.500Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 183982.5, \"gpu_hours\": 51.11}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:17:25.022Z\"}, \"precompute-v2-shard0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T16:11:01.629Z\", \"updated_at\": \"2026-05-15T19:17:23.631Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && rm -rf /root/autodl-tmp/crm_cache/spatial /root/autodl-tmp/crm_cache/object && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id 0 --num_shards 3 --seed 42 --K 10\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"57628\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/precompute-v2-shard0.log\", \"submitted_at\": \"2026-05-13T16:11:01.605Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 183982.0, \"gpu_hours\": 51.11}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:17:23.631Z\"}, \"eval-mag-perdof-norm0p3-object-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:58:30.091Z\", \"updated_at\": \"2026-05-15T19:13:43.549Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_r2.json\\\"\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:2\"], \"pid\": \"127570\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-perdof-norm0p3-object-r2.log\", \"submitted_at\": \"2026-05-15T18:58:29.637Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"libero_object 10 tasks x 10 rollouts\", \"data_path\": \"/root/autodl-tmp/libero_data/ (object)\", \"data_count\": 100, \"model_name\": \"crm_perdof_v3_norm\", \"seed\": 42, \"wall_clock_seconds\": 885.6, \"gpu_hours\": 0.25}, \"hypothesis\": \"Object magnitude sweep: perdof CRM v3-norm at norm=0.3 on LIBERO object benchmark. Migrated from bjb1-32546:cuda:4 (GPU conflict) to bjb2-28827:cuda:2. Paired with obs_only norm=0.3 for magnitude comparison figure.\", \"parent\": \"eval-mag-perdof-norm0p3-object\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:13:15.247Z\", \"failure_reason\": \"Duplicate of eval-mag-perdof-norm03-object (PID 118886 on bjb2-28827:cuda:3, identical params). Killed to free cuda:2.\"}, \"eval-mag-perdof-norm0p3-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:34:52.454Z\", \"updated_at\": \"2026-05-15T18:58:11.790Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"144887\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-perdof-norm0p3-object.log\", \"submitted_at\": \"2026-05-15T18:37:26.089Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1245.7, \"gpu_hours\": 0.35}, \"hypothesis\": \"Retry of eval-mag-perdof-norm03-object (killed by SIGTERM). Object magnitude sweep: perdof CRM v3-norm at norm=0.3 on LIBERO object benchmark. Paired with obs_only norm=0.3 (running) for magnitude comparison figure.\", \"parent\": \"eval-mag-perdof-norm03-object\", \"conclusion\": \"killed\", \"failure_reason\": \"GPU conflict on bjb1-32546:cuda:4 (shared with obs-only-default). Killed lower priority perdof. Migrating to bjb2-28827:cuda:2 as r2.\", \"completed_at\": \"2026-05-15T18:58:11.790Z\"}, \"eval-obs-only-object-norm02-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:38:18.819Z\", \"updated_at\": \"2026-05-15T18:58:10.821Z\", \"hypothesis\": \"D031: obs_only CRM v3-norm norm=0.2 seed=43 on LIBERO object benchmark. norm=0.2 shows strongest signal (18% SR at 5/10 tasks in seed=42). Seed=43 doubling for statistical power on the best-performing configuration.\", \"parent\": \"eval-acr-object-obs-only-norm02\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_seed43.json\", \"server\": \"bjb1-32546\", \"data_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed43.json\", \"data_count\": 10, \"model_name\": \"crm_obs_only\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"object\"}, \"metrics\": {\"pid\": 118214, \"gpu\": 3, \"process_status\": \"alive\", \"log_file\": \"logs/eval_object_obs_only_norm02_seed43.log\"}, \"conclusion\": \"failed\", \"failure_reason\": \"Crashed after 1 task on bjb1-32546:cuda:3 (PID 118214). Reviewer confirmed. Restarting as r2.\", \"completed_at\": \"2026-05-15T18:58:10.821Z\"}, \"eval-acr-object-v4-default\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:18:17.209Z\", \"updated_at\": \"2026-05-15T17:38:37.815Z\", \"hypothesis\": \"Ablation: perdof CRM v3-norm with DEFAULT max_correction_norm (~1.42, no magnitude control) on LIBERO object benchmark. Tests whether magnitude control is essential on object domain too. If v4-default << v4-perdof (norm=0.1) → magnitude control is universally needed. If v4-default ≈ v4-perdof → spatial failure was anomalous.\", \"parent\": \"eval-acr-object-v4-perdof\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --output_file logs/eval_object_perdof_default_norm.json\", \"server\": \"bjb2-28827\", \"gpu\": [\"cuda:3\"], \"pid\": \"107658\", \"log_path\": \"logs/eval_object_perdof_default_norm.log\", \"submitted_at\": \"2026-05-16T00:51:00Z\", \"backend\": \"nohup\", \"account\": \"root\", \"data_path\": \"libero_object\", \"data_count\": 10, \"model_name\": \"crm_perdof_default_norm\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"object\"}, \"metrics\": {\"tasks_done\": 3, \"tasks_total\": 10, \"status\": \"DEAD\", \"partial_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0}, \"pid_42311\": \"not_found\", \"needs_restart\": true, \"checked_at\": \"2026-05-16T01:00Z\"}, \"notes\": \"Killed per Director instruction. 3/10 tasks all 0% SR, no magnitude control (norm≈1.42). Conclusion obvious — magnitude control is essential.\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T17:38:37.815Z\"}, \"eval-mag-perdof-norm03-object\": {\"status\": \"DEPLOYED\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:57:00.172Z\", \"updated_at\": \"2026-05-15T17:38:28.909Z\", \"spec\": {\"pid\": 115384, \"gpu_ids\": [2], \"server\": \"bjb2-28827\", \"command\": \"python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03.json\"}, \"server\": \"bjb2-28827\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb2-28827\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-15T17:16:56.760Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03.json\\\"\", \"finished_at\": \"2026-05-15T17:29:42.220Z\", \"training_hours\": 0.21}, \"pid\": 118886, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-perdof-norm03-object.log\", \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T17:29:45.210Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:29:48.614116+00:00\"}]}, \"notes\": \"Restarted on cuda:3 (PID 118886, tmux: eval-mag-perdof-norm03-object) after v4-default killed. Previous run killed by SIGTERM before first rollout.\"}, \"eval-mag-obsonly-norm03-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:49:38.786Z\", \"updated_at\": \"2026-05-15T17:22:51.755Z\", \"hypothesis\": \"Retry of eval-mag-obsonly-norm03 (EXIT_CODE=127 fix). Magnitude sweep: obs_only CRM v3-norm at norm=0.3 on spatial. Fills obs_only norm=0.3 gap. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade at same norm, strong evidence for obs_only robustness.\", \"parent\": \"eval-mag-obsonly-norm03\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_mag_obsonly_norm03.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": 325264, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm03-r2.log\", \"submitted_at\": \"2026-05-15T06:50:02.511Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": 100, \"model_name\": \"crm_v3_norm_obs_only\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 37969.2, \"gpu_hours\": 10.55}, \"metrics\": {\"bowl_between\": 0.9, \"next_to_ramekin\": 1, \"table_center\": 0, \"cookie_box\": 0.3, \"top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"stove\": 0, \"next_to_plate\": 0.3, \"wooden_cabinet\": 0, \"overall_SR\": 0.36}, \"reproduce\": {\"finished_at\": \"2026-05-15T17:20:31.567Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:20:34.907634+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm03-r2.log\", \"completed_at\": \"2026-05-15T17:22:51.755Z\"}, \"eval-vla-mean-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:31:09.989Z\", \"updated_at\": \"2026-05-15T17:01:25.883Z\", \"spec\": {\"command\": \"python eval_vla.py --benchmark object --mode vla_only --baseline_mode mean --n_rollouts 10 --K 10 --seed 42\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": 100, \"model_name\": \"smolvla_libero\", \"seed\": 42, \"eval_data\": \"LIBERO object\", \"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean.log\"}, \"hypothesis\": \"VLA mean baseline (K=10, mean aggregation) on LIBERO object benchmark. Matches reconvla spatial baseline but on object tasks.\", \"metrics\": {\"benchmark\": \"object\", \"mode\": \"vla_only\", \"baseline_mode\": \"mean\", \"n_rollouts\": 10, \"K\": 10, \"seed\": 42, \"overall_sr\": 12, \"total_success\": 12, \"total_rollouts\": 100, \"tasks_done\": \"10/10\", \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 10, \"bbq_sauce\": 30, \"ketchup\": 10, \"tomato_sauce\": 10, \"butter\": 0, \"milk\": 20, \"chocolate_pudding\": 30, \"orange_juice\": 10}, \"json_output\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean.json\"}, \"conclusion\": \"success\", \"gpu\": \"bjb1-32546:cuda:5\", \"pid\": 18808, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean.log\", \"completed_at\": \"2026-05-15T17:01:25.883Z\"}, \"eval-reconvla-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T01:48:28.744Z\", \"updated_at\": \"2026-05-15T16:25:17.101Z\", \"spec\": {\"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_reconvla.log\", \"json_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_reconvla.json\"}, \"hypothesis\": \"ReconVLA baseline (scalar Euclidean argmin, K=10) on LIBERO object benchmark. Tests whether simple sample selection improves over VLA mean on object manipulation tasks. Provides baseline for CRM comparison on object domain.\", \"metrics\": {\"overall_sr\": 0.12, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}, \"n_rollouts\": 10, \"total_episodes\": 100, \"total_successes\": 12}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T16:25:17.101Z\"}, \"eval-acr-object-v4-obs-only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T02:53:41.689Z\", \"updated_at\": \"2026-05-15T16:23:01.718Z\", \"hypothesis\": \"D021: obs_only CRM v3-norm with max_correction_norm=0.1 on LIBERO object benchmark. Cross-benchmark validation — obs-only leads spatial at 57.5%.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"13797\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-obs-only.log\", \"submitted_at\": \"2026-05-15T02:53:41.526Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 47312.8, \"gpu_hours\": 13.14}, \"metrics\": {\"overall_sr\": \"19.0% (19/100)\", \"total_success\": 19, \"total_rollouts\": 100, \"mode\": \"obs_only\", \"benchmark\": \"object\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"tasks_done\": \"10/10\", \"per_task\": {\"alphabet_soup\": \"0%\", \"cream_cheese\": \"10%\", \"salad_dressing\": \"20%\", \"bbq_sauce\": \"40%\", \"ketchup\": \"10%\", \"tomato_sauce\": \"0%\", \"butter\": \"10%\", \"milk\": \"20%\", \"chocolate_pudding\": \"50%\", \"orange_juice\": \"30%\"}, \"json_output\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T15:59:31.860Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T15:59:34.042176+00:00\"}]}, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-obs-only.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T16:02:14.366Z\"}, \"eval-acr-object-v4-perdof\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T02:49:13.626Z\", \"updated_at\": \"2026-05-15T15:45:38.531Z\", \"hypothesis\": \"D021: ACR-VLA perdof CRM v3-norm with max_correction_norm=0.1 on LIBERO object benchmark. Cross-benchmark validation of spatial findings.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode acr_vla --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1\", \"server\": \"bjb1-32546\", \"gpu_ids\": [\"cuda:1\"], \"pid\": \"11116\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v3-norm perdof, max_correction_norm=0.1, object)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\", \"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-perdof.log\"}, \"metrics\": {\"overall_sr\": \"11.0% (11/100)\", \"total_success\": 11, \"total_rollouts\": 100, \"mode\": \"perdof\", \"benchmark\": \"object\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"alphabet_soup\": \"0%\", \"cream_cheese\": \"0%\", \"salad_dressing\": \"20%\", \"bbq_sauce\": \"30%\", \"ketchup\": \"0%\", \"tomato_sauce\": \"0%\", \"butter\": \"10%\", \"milk\": \"0%\", \"chocolate_pudding\": \"20%\", \"orange_juice\": \"30%\"}, \"note\": \"perdof object 11% vs argmin ~7% (partial). obs_only leads at ~14% (8/10). Confirms perdof not competitive on object.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T15:45:38.531Z\"}, \"eval-acr-spatial-v4-scalar-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:14:04.283Z\", \"updated_at\": \"2026-05-15T13:18:27.852Z\", \"hypothesis\": \"Restart from T3. scalar_unc CRM v3-norm with max_correction_norm=0.1 on spatial. Three-way ablation: perdof vs scalar_unc vs obs_only.\", \"parent\": \"eval-acr-spatial-v4-scalar\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_scalar --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1 --start_task 3\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": 311881, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-scalar-r2.log\", \"submitted_at\": \"2026-05-15T05:14:33.525Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO spatial\", \"data_count\": 70, \"model_name\": \"ACR-VLA CRM scalar_unc v3-norm (restart from T3)\", \"seed\": 42, \"eval_data\": \"LIBERO spatial tasks 3-9\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"checkpoint_path\": \"N/A (eval-only)\", \"wall_clock_seconds\": 29034.3, \"gpu_hours\": 8.07}, \"metrics\": {\"overall_sr\": \"32.0% (32/100)\", \"total_success\": 32, \"total_rollouts\": 100, \"mode\": \"scalar_unc\", \"benchmark\": \"spatial\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"T0\": \"60%\", \"T1\": \"100%\", \"T2\": \"10%\", \"T3\": \"40%\", \"T4\": \"0%\", \"T5\": \"0%\", \"T6\": \"90%\", \"T7\": \"0%\", \"T8\": \"10%\", \"T9\": \"10%\"}, \"note\": \"D030 confirmed: scalar_unc spatial 32% vs argmin 34% = -2pp. T0-T2 from original eval-acr-spatial-v4-scalar, T3-T9 from r2 restart. All CRM variants dead on spatial.\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T13:15:46.765Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T13:15:49.226583+00:00\"}]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T13:18:27.853Z\"}, \"eval-acr-spatial-v4-obs-only-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:14:05.934Z\", \"updated_at\": \"2026-05-15T11:15:11.801Z\", \"hypothesis\": \"Restart from T6. obs_only CRM v3-norm with max_correction_norm=0.1 on spatial. If obs_only >= perdof, conformal features need restructuring.\", \"parent\": \"eval-acr-spatial-v4-obs-only-r2\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --start_task 6\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": 312420, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-obs-only-r3.log\", \"submitted_at\": \"2026-05-15T05:14:38.600Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO spatial\", \"data_count\": 40, \"model_name\": \"ACR-VLA CRM obs_only v3-norm (restart from T6)\", \"seed\": 42, \"eval_data\": \"LIBERO spatial tasks 6-9\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"wall_clock_seconds\": 21633.2, \"gpu_hours\": 6.01}, \"metrics\": {\"overall_sr\": \"35.0% (35/100)\", \"total_success\": 35, \"total_rollouts\": 100, \"mode\": \"crm_obs_only\", \"benchmark\": \"spatial\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"T0\": \"90%\", \"T1\": \"100%\", \"T2\": \"0%\", \"T3\": \"40%\", \"T4\": \"10%\", \"T5\": \"0%\", \"T6\": \"90%\", \"T7\": \"0%\", \"T8\": \"20%\", \"T9\": \"0%\"}, \"r3_subset_T6_T9\": \"27.5% (11/40)\", \"note\": \"D030: obs_only spatial 10-task = 35%. vs argmin 34% = +1pp. Scenario C threshold (>=39%) NOT MET. Earlier T0-T5 advantage (+5pp) wiped out by T6-T9.\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T10:15:39.276Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T10:15:44.340640+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-obs-only-r3.log\", \"completed_at\": \"2026-05-15T11:15:11.801Z\"}, \"eval-obs-only-spatial-seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T09:09:04.411Z\", \"updated_at\": \"2026-05-15T10:01:21.065Z\", \"hypothesis\": \"D029: obs_only seed=43 复现实验。obs_only 是项目唯一存活路径。seed=42 如果确认 +5pp over argmin，seed=43 增加统计力（200 vs 200 样本下 Fisher exact p ~0.12，配合 object benchmark 独立验证有望通过）。\", \"parent\": \"eval-acr-spatial-v4-obs-only-r3\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_obs_only_spatial_seed43.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"341873\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-spatial-seed43.log\", \"submitted_at\": \"2026-05-15T09:09:23.712Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": 100, \"model_name\": \"crm_v3_norm_obs_only\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO spatial (10 tasks x 10 rollouts)\", \"wall_clock_seconds\": 3117.4, \"gpu_hours\": 0.87}, \"notes\": \"D029: perdof spatial 35% vs argmin 34% = +1pp, kill criterion triggered. Per-DOF claim dead on spatial. obs_only 是唯一存活路径，seed=43 用于增加统计力。\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T10:01:21.065Z\"}, \"eval-acr-spatial-v4-small-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:14:05.220Z\", \"updated_at\": \"2026-05-15T09:10:21.153Z\", \"hypothesis\": \"Restart from T7. ACR-VLA perdof CRM v3-norm with max_correction_norm=0.1 on spatial. Full per-DOF uncertainty pipeline.\", \"parent\": \"eval-acr-spatial-v4-small\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/crm_best.pt --max_correction_norm 0.1 --start_task 7\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": 312150, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-small-r2.log\", \"submitted_at\": \"2026-05-15T05:14:36.298Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO spatial\", \"data_count\": 30, \"model_name\": \"ACR-VLA CRM perdof v3-norm (restart from T7)\", \"seed\": 42, \"eval_data\": \"LIBERO spatial tasks 7-9\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/crm_best.pt\", \"wall_clock_seconds\": 14053.7, \"gpu_hours\": 3.9}, \"notes\": \"[D027] Framing 暂不裁决。Scenario A/B/C 取决于 magnitude sweep + object benchmark 结果。spatial matched-task perdof=argmin (0pp) 意味着 Scenario A 在 spatial 上不可能。\", \"metrics\": {\"overall_sr\": \"35.0% (35/100)\", \"total_success\": 35, \"total_rollouts\": 100, \"mode\": \"perdof\", \"benchmark\": \"spatial\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"T0\": \"60%\", \"T1\": \"100%\", \"T2\": \"10%\", \"T3\": \"40%\", \"T4\": \"0%\", \"T5\": \"0%\", \"T6\": \"90%\", \"T7\": \"10%\", \"T8\": \"40%\", \"T9\": \"0%\"}, \"note\": \"D029: perdof spatial complete 10-task = 35%. vs argmin 34% = +1pp. Kill criterion triggered — per-DOF claim dead on spatial.\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T09:05:27.552Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T09:05:31.321347+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/crm_best.pt\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-small-r2.log\", \"completed_at\": \"2026-05-15T09:08:50.017Z\"}, \"eval-mag-obsonly-norm-0.3-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:10:44.647Z\", \"updated_at\": \"2026-05-15T07:19:12.632Z\", \"hypothesis\": \"Magnitude sweep: obs_only CRM v3-norm at max_correction_norm=0.3 on spatial. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade at same norm, strong evidence for obs_only robustness over perdof.\", \"parent\": \"eval-mag-obsonly-norm02\", \"spec\": {\"command\": \"N/A (stale duplicate entry)\", \"server\": \"bjb1-18228\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"N/A\", \"seed\": 0, \"checkpoint_source\": \"N/A\", \"eval_data\": \"N/A\"}, \"conclusion\": \"killed\", \"checkpoint_path\": \"N/A (stale duplicate entry, never ran)\", \"log_path\": \"N/A\", \"notes\": \"Stale duplicate entry with dots in name. Actual experiment is eval-mag-obsonly-norm-0p3-r3 (also killed). Real running experiment is eval-mag-obsonly-norm03-r2.\", \"completed_at\": \"2026-05-15T07:19:12.632Z\"}, \"eval-mag-obsonly-norm-0p3-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:11:06.381Z\", \"updated_at\": \"2026-05-15T07:17:16.300Z\", \"hypothesis\": \"Magnitude sweep: obs_only CRM v3-norm at max_correction_norm=0.3 on spatial. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade at same norm, strong evidence for obs_only robustness over perdof.\", \"parent\": \"eval-mag-obsonly-norm02\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_mag_obsonly_norm_0p3.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"329871\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm-0p3-r3.log\", \"submitted_at\": \"2026-05-15T07:11:15.690Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": 100, \"model_name\": \"crm_obs_only_v3_norm\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO spatial (10 tasks x 10 rollouts)\", \"wall_clock_seconds\": 360.6, \"gpu_hours\": 0.1}, \"conclusion\": \"killed\", \"notes\": \"Director 撤销部署指令。r2 (PID 325264) 实际未被误杀，r3 是基于信息差的重复部署。立即 kill r3 保留 r2。\", \"checkpoint_path\": \"N/A (killed before completion)\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm-0p3-r3.log\", \"completed_at\": \"2026-05-15T07:17:16.300Z\"}, \"eval-argmin-only-spatial-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:14:03.322Z\", \"updated_at\": \"2026-05-15T06:39:37.926Z\", \"hypothesis\": \"Restart from T9. ReconVLA baseline (scalar Euclidean argmin, K=10) on spatial. Isolate argmin base action selection from CRM correction.\", \"parent\": \"eval-argmin-only-spatial\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --start_task 9\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": 311609, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-argmin-only-spatial-r2.log\", \"submitted_at\": \"2026-05-15T05:14:30.112Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO spatial\", \"data_count\": 10, \"model_name\": \"ReconVLA argmin K=10 (restart from T9)\", \"seed\": 42, \"eval_data\": \"LIBERO spatial task 9 only\", \"checkpoint_source\": \"N/A (reconvla mode, no CRM)\", \"wall_clock_seconds\": 5107.8, \"gpu_hours\": 1.42}, \"reproduce\": {\"finished_at\": \"2026-05-15T06:35:00.746Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T06:35:02.954210+00:00\"}]}, \"metrics\": {\"overall_success_rate\": 0.34, \"total_successes\": 34, \"total_trials\": 100, \"per_task\": {\"T0_between_plate_and_ramekin\": 0.6, \"T1_next_to_ramekin\": 1, \"T2_from_table_center\": 0, \"T3_on_cookie_box\": 0.3, \"T4_in_top_drawer\": 0.1, \"T5_on_ramekin\": 0.1, \"T6_next_to_cookie_box\": 0.9, \"T7_on_stove\": 0, \"T8_next_to_plate\": 0.3, \"T9_on_wooden_cabinet\": 0.1}, \"note\": \"T0-T8 from original run (eval-argmin-only-spatial), T9 from r2 restart. Combined 10-task result.\"}, \"conclusion\": \"success\", \"notes\": \"10-task complete. T9 (wooden_cabinet) = 10%. Overall 34% (34/100). T0-T8 from original run, T9 from r2 restart. Clean exit. bjb1-18228 cuda:0 now FREE.\", \"checkpoint_path\": \"N/A (eval-only, no checkpoint output)\", \"completed_at\": \"2026-05-15T06:39:37.926Z\"}, \"eval-mag-obsonly-norm003\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:21:24.009Z\", \"updated_at\": \"2026-05-15T05:32:12.897Z\", \"hypothesis\": \"Magnitude sweep: obs_only CRM v3-norm at norm=0.03 on spatial. Completes obs_only norm curve (have 0.05, 0.2; adding 0.03).\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --max_correction_norm 0.03 --n_rollouts 10 --K 10 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_mag_obsonly_norm003.json\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": 225144, \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm003-b2.log\", \"submitted_at\": \"2026-05-15T05:20:45Z\", \"submitted_via\": \"tmux (manual)\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO spatial benchmark\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"SmolVLA + CRM-v3-norm-obs_only\", \"seed\": 42, \"checkpoint_source\": \"crm-train-v3-norm-obs_only\", \"eval_data\": \"LIBERO spatial\", \"wall_clock_seconds\": 686.0, \"gpu_hours\": 0.19}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T05:32:10.962Z\", \"notes\": \"Duplicate experiment on same GPU. pid 225144 was actually the child python process of eval-mag-obsonly-norm003-b2's wrapper (pid 225139). Not a separate experiment. Killed, restarted b2 with new pid 227426.\"}, \"eval-vla-only-object-k1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:11:14.165Z\", \"updated_at\": \"2026-05-15T05:18:17.853Z\", \"hypothesis\": \"VLA-only baseline (K=1, single sample, no CRM) on LIBERO object benchmark. Lowest-bar baseline for object domain.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode vla_only --baseline_mode single --benchmark object --n_rollouts 10 --seed 42 --K 1 --output_file logs/eval_object_vla_only_k1.json\\\"\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:4\"], \"pid\": \"39397\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-vla-only-object-k1.log\", \"submitted_at\": \"2026-05-15T05:11:22.634Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"SmolVLA (VLA-only K=1 single sample)\", \"seed\": 42, \"eval_data\": \"LIBERO object\", \"checkpoint_source\": \"N/A (no CRM, single VLA sample)\", \"wall_clock_seconds\": 311.9, \"gpu_hours\": 0.09}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T05:16:34.574Z\", \"notes\": \"Duplicate of eval-vla-only-object (already DONE at 12% SR). Process killed to free bjb1-32546 cuda:4.\"}, \"eval-vla-only-object\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T02:54:57.323Z\", \"updated_at\": \"2026-05-15T04:47:47.959Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode single --n_rollouts 10 --K 1 --output_file logs/eval_object_vla_only.json\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO object benchmark\", \"data_count\": \"10 tasks x 10 rollouts\", \"model_name\": \"SmolVLA (VLA-only baseline)\", \"seed\": 42, \"eval_data\": \"LIBERO object\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only.log\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only.json\"}, \"conclusion\": \"success\", \"hypothesis\": \"VLA-only baseline (K=1, no mean, no CRM) on LIBERO object benchmark. Single sample from flow-matching VLA.\", \"metrics\": {\"overall_sr\": 0.12, \"total_success\": 12, \"total_trials\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}, \"gpu\": \"bjb1-32546:cuda:4\", \"pid\": 17222, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only.log\", \"checkpoint_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only.json\", \"completed_at\": \"2026-05-15T04:42:20.025Z\"}, \"eval-acr-spatial-v4-default-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T01:48:09.734Z\", \"updated_at\": \"2026-05-15T03:30:05.911Z\", \"hypothesis\": \"D018-D019 验证: perdof CRM v3-norm with DEFAULT max_correction_norm (~1.42). 如果 v4-default << v4-small (max_norm=0.1) → magnitude control 是必要的。如果 v4-default ≈ baseline → normalization 独自不够。补全 bjb1 上两次失败的实验。\", \"parent\": \"eval-acr-spatial-v4-default-r2\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\\\"\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"212685\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-default-r3.log\", \"submitted_at\": \"2026-05-15T01:49:35.076Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v3-norm perdof, default max_correction_norm)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 6030.8, \"gpu_hours\": 1.68}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T03:30:05.911Z\"}, \"eval-tiny-correction-spatial\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:48:35.421Z\", \"updated_at\": \"2026-05-15T01:45:12.897Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v2/perdof/crm_best.pt --max_correction_norm 0.05\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"232815\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-tiny-correction-spatial.log\", \"submitted_at\": \"2026-05-14T17:48:35.317Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_ids\": [\"cuda:2\"], \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"ACR-VLA per-DOF CRM v2 with tiny correction (max_norm=0.05, 28x smaller than default 1.42)\", \"seed\": 42, \"hypothesis\": \"Extreme correction clipping (0.05 vs 1.42) tests whether compounding error from large CRM deltas is the primary failure mode. If tiny-correction >> full-correction, correction magnitude is the problem.\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v2/perdof/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"wall_clock_seconds\": 27771.0, \"gpu_hours\": 7.71}, \"metrics\": {\"tasks_done\": \"7/10\", \"partial_results\": {\"T1_between_plate_ramekin\": \"70% (7/10)\", \"T2_next_to_ramekin\": \"90% (9/10)\", \"T3_from_table_center\": \"0% (0/10)\", \"T4_on_cookie_box\": \"30% (3/10)\", \"T5_in_top_drawer\": \"0% (0/10)\", \"T6_on_ramekin\": \"0% (0/10)\", \"T7_next_to_cookie_box\": \"90% (9/10)\"}, \"running_avg_7tasks\": \"40% (28/70)\", \"process_status\": \"ACTUALLY ALIVE - bash wrapper PID 232815 dead but python child PID 232820 still running (07:48h, 139% CPU, 9.1GB RSS, GPU2)\", \"status_correction\": \"Registry incorrectly marked DONE, process is still completing remaining 3 tasks\", \"snapshot_time\": \"2026-05-15T09:40Z\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T01:31:26.353Z\", \"failure_reason\": \"D021: v2 checkpoint invalidated by crm_cache_v5 retraining. Replaced by eval-acr-spatial-v4-scalar on bjb1:2.\"}, \"eval-acr-spatial-v4-default-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:17:37.194Z\", \"updated_at\": \"2026-05-14T22:40:00.000Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\\\"\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"203217\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-default-r2.log\", \"submitted_at\": \"2026-05-14T22:29:03.489Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"D018 retry: Normalization alone fixes CRM correction degradation. v3-norm per-DOF checkpoint with default max_correction_norm (~1.42). If >30% baseline → normalization was the main fix. If still < 30% → magnitude control also needed (compare with v4-small at 0.1).\", \"parent\": \"eval-acr-spatial-v4-default\", \"conclusion\": \"killed\", \"failure_reason\": \"Superseded by D020 plan. Default norm=1.42 already proven to degrade (v4-default: 0/5). Not needed. Process killed on bjb2 (PID 203222 confirmed dead).\", \"completed_at\": \"2026-05-14T22:40:00.000Z\"}, \"eval-acr-spatial-v4-obs-only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:08:53.421Z\", \"updated_at\": \"2026-05-14T22:16:05.788Z\", \"hypothesis\": \"D020: obs_only CRM (val_loss 0.0165, 54% better than perdof 0.0358) with max_correction_norm=0.1. If obs_only >= v4-small (perdof) → Claim 1 needs restructuring. If obs_only < v4-small → conformal features have unique value under distribution shift.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3/obs_only/crm_best.pt\", \"server\": \"bjb2-40593\", \"gpu_ids\": [\"cuda:0\"], \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v3 obs_only, default max_correction_norm=1.42)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"log_path\": \"/root/autodl-tmp/logs/eval-acr-spatial-v4-obs-only.log\", \"tmux_session\": \"eval-acr-spatial-v4-obs-only\", \"pid\": 199257}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T22:16:04.414Z\", \"failure_reason\": \"Wrong checkpoint (crm_v3 not crm_v3_norm) + wrong max_correction_norm (1.42 not 0.1). Killed and replaced by eval-acr-spatial-v4-obs-only-r2.\"}, \"eval-acr-spatial-v4-default\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:08:59.906Z\", \"updated_at\": \"2026-05-14T22:08:58.490Z\", \"hypothesis\": \"D018: Input normalization alone fixes CRM correction degradation. v3-norm checkpoint with default max_correction_norm=1.42. If >30% baseline → normalization was the main fix.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"server\": \"bjb1-18228\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"ACR-VLA (CRM v3-norm per-DOF, default correction)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\"}, \"metrics\": {\"tasks_done\": \"0/10\", \"status_alert\": \"NO PROCESS FOUND - registry says RUNNING but no matching PID or tmux session on bjb1-18228. GPU 0 occupied by stale eval-acr-spatial-v3 tmux + crm-train-obs-only. NEEDS RESTART.\", \"snapshot_time\": \"2026-05-15T05:26Z\"}, \"conclusion\": \"failed\", \"failure_reason\": \"Process died. D019: 0/5 on task 1 confirmed default norm=1.42 still degrades. Replaced by eval-acr-spatial-v4-obs-only on cuda:0.\", \"completed_at\": \"2026-05-14T22:08:58.490Z\"}, \"crm-train-v3-norm-scalar-unc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:09:01.250Z\", \"updated_at\": \"2026-05-14T22:05:42.608Z\", \"hypothesis\": \"Ablation: scalar_unc input mode (scalar uncertainty only) with normalization. Tests per-DOF vs scalar uncertainty contribution with proper normalization.\", \"spec\": {\"command\": \"python -u src/train_crm.py --benchmark spatial --cache_dir /root/autodl-tmp/crm_cache_v5 --output_dir /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/ --K 10 --epochs 50 --batch_size 512 --lr 0.016 --input_mode scalar_unc --seed 42\", \"server\": \"bjb1-18228\", \"data_path\": \"/root/autodl-tmp/crm_cache_v5/spatial/\", \"data_count\": 12167, \"model_name\": \"CRM-MLP-Normalized (scalar_unc)\", \"seed\": 42}, \"metrics\": {\"best_epoch\": 46, \"best_val_loss\": 0.037354, \"final_train_loss\": 0.053422, \"final_val_loss\": 0.03737}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"log_path\": \"/tmp/crm_train_scalar_unc.log\", \"completed_at\": \"2026-05-14T22:05:42.608Z\"}, \"crm-train-v3-norm-obs-only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:09:00.829Z\", \"updated_at\": \"2026-05-14T22:05:28.289Z\", \"hypothesis\": \"Ablation: obs_only input mode (no uncertainty features) with normalization. Isolates contribution of obs features vs conformal features.\", \"spec\": {\"command\": \"python -u src/train_crm.py --benchmark spatial --cache_dir /root/autodl-tmp/crm_cache_v5 --output_dir /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/ --K 10 --epochs 50 --batch_size 512 --lr 0.016 --input_mode obs_only --seed 42\", \"server\": \"bjb1-18228\", \"data_path\": \"/root/autodl-tmp/crm_cache_v5/spatial/\", \"data_count\": 12167, \"model_name\": \"CRM-MLP-Normalized (obs_only)\", \"seed\": 42}, \"metrics\": {\"best_epoch\": 48, \"best_val_loss\": 0.01645, \"final_train_loss\": 0.025576, \"final_val_loss\": 0.01645, \"total_epochs\": 50}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"/tmp/crm_train_obs_only.log\", \"completed_at\": \"2026-05-14T22:05:28.289Z\"}, \"crm-train-v3-norm\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:45:12.565Z\", \"updated_at\": \"2026-05-14T20:05:22.677Z\", \"hypothesis\": \"D018: Input normalization fixes 1500x scale imbalance in CRM inputs, enabling proper gradient flow and meaningful per-DOF correction learning\", \"parent\": \"crm-train-v3-perdof\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u src/train_crm.py --benchmark spatial --cache_dir /root/autodl-tmp/crm_cache_v5 --output_dir /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/ --K 10 --epochs 50 --batch_size 512 --lr 0.016 --input_mode full --seed 42\", \"server\": \"bjb1-18228\", \"data_path\": \"/root/autodl-tmp/crm_cache_v5/spatial/\", \"data_count\": 12167, \"model_name\": \"CRM-MLP-337K-Normalized\", \"seed\": 42, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"N/A (training experiment)\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"log_path\": \"no log file (tee failed, output was in tmux pane only)\", \"completed_at\": \"2026-05-14T20:05:20.181Z\", \"results\": {\"best_epoch\": 47, \"best_val_loss\": 0.03578, \"final_train_loss\": 0.04992, \"final_val_loss\": 0.03578, \"total_epochs\": 50, \"normalization\": \"per-feature input normalization (mean/std stored in crm_best.pt as input_mean/input_std tensors)\"}}, \"crm-train-v3-scalar-unc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:05:00.968Z\", \"updated_at\": \"2026-05-14T18:37:14.400Z\", \"spec\": {\"command\": \"python -u src/train_crm.py --benchmark spatial --cache_dir /root/autodl-tmp/crm_cache/ --output_dir /root/autodl-tmp/checkpoints/crm_v3/scalar_unc/ --K 10 --epochs 50 --batch_size 512 --lr 0.016 --input_mode scalar_unc --seed 42 --norm_stats /root/autodl-tmp/checkpoints/crm_v3/norm_stats.pt\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"181896\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-train-v3-scalar-unc.log\", \"submitted_at\": \"2026-05-14T18:05:00.862Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/crm_cache/\", \"data_count\": 0, \"model_name\": \"CRM-MLP-337K\", \"seed\": 42, \"wall_clock_seconds\": 1917.7, \"gpu_hours\": 0.53}, \"reproduce\": {\"finished_at\": \"2026-05-14T18:27:15.107Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T18:27:19.071535+00:00\"}]}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T18:36:58.566Z\", \"metrics\": {\"invalidation_reason\": \"Trained on bjb2 crm_cache v4 (6D state, pre-D016). Must retrain on bjb1 crm_cache_v5 (8D state).\", \"original_val_loss\": 1.195}}, \"crm-train-v3-obs-only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:05:02.939Z\", \"updated_at\": \"2026-05-14T18:37:04.316Z\", \"spec\": {\"command\": \"python -u src/train_crm.py --benchmark spatial --cache_dir /root/autodl-tmp/crm_cache/ --output_dir /root/autodl-tmp/checkpoints/crm_v3/obs_only/ --K 10 --epochs 50 --batch_size 512 --lr 0.016 --input_mode obs_only --seed 42 --norm_stats /root/autodl-tmp/checkpoints/crm_v3/norm_stats.pt\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"181973\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-train-v3-obs-only.log\", \"submitted_at\": \"2026-05-14T18:05:02.833Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/crm_cache/spatial\", \"data_count\": 2402, \"model_name\": \"CRM-MLP-337K\", \"seed\": 42, \"wall_clock_seconds\": 1802.8, \"gpu_hours\": 0.5}, \"reproduce\": {\"finished_at\": \"2026-05-14T18:27:22.983Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T18:27:25.410071+00:00\"}]}, \"conclusion\": \"killed\", \"metrics\": {\"invalidation_reason\": \"Trained on bjb2 crm_cache v4 (6D state, pre-D016). Must retrain on bjb1 crm_cache_v5 (8D state).\", \"original_val_loss\": 1.193424}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3/obs_only/crm_best.pt\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-train-v3-obs-only.log\", \"completed_at\": \"2026-05-14T18:35:05.626Z\"}, \"crm-train-v3-perdof\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:04:54.552Z\", \"updated_at\": \"2026-05-14T18:37:02.631Z\", \"spec\": {\"command\": \"python -u src/train_crm.py --benchmark spatial --cache_dir /root/autodl-tmp/crm_cache/ --output_dir /root/autodl-tmp/checkpoints/crm_v3/perdof/ --K 10 --epochs 50 --batch_size 512 --lr 0.016 --input_mode full --seed 42 --norm_stats /root/autodl-tmp/checkpoints/crm_v3/norm_stats.pt\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"181668\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-train-v3-perdof.log\", \"submitted_at\": \"2026-05-14T18:04:54.446Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/crm_cache/\", \"data_count\": 0, \"model_name\": \"CRM-MLP-337K\", \"seed\": 42, \"wall_clock_seconds\": 1510.3, \"gpu_hours\": 0.42}, \"reproduce\": {\"finished_at\": \"2026-05-14T18:27:11.506Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T18:27:13.038696+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3/perdof/crm_best.pt\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/crm-train-v3-perdof.log\", \"metrics\": {\"invalidation_reason\": \"Trained on bjb2 crm_cache v4 (6D state, pre-D016). Must retrain on bjb1 crm_cache_v5 (8D state).\", \"original_val_loss\": 1.191387}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T18:30:04.713Z\"}, \"eval-obs-only-spatial-v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:49:43.787Z\", \"updated_at\": \"2026-05-14T17:47:54.523Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v2/obs_only/crm_best.pt\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"211961\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-obs-only-spatial-v3.log\", \"submitted_at\": \"2026-05-14T12:49:43.691Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"CRM obs_only v2 (990D, no conformal features)\", \"seed\": 42, \"hypothesis\": \"obs_only CRM ablation — CRM without conformal features tests whether per-DOF conformal intervals are necessary\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v2/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"parent\": \"crm-train-v2-obs-only\", \"conclusion_note\": \"Director order: 0/30 after 3 tasks, no diagnostic value. Freed bjb1:2 for eval-tiny-correction-spatial.\", \"metrics\": {\"tasks_completed\": 3, \"total_tasks\": 10, \"success_rate\": 0, \"successes\": 0, \"rollouts\": 30}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v2/obs_only/crm_best.pt\", \"wall_clock_seconds\": 17890.8, \"gpu_hours\": 4.97}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T17:47:54.523Z\"}, \"eval-scalar-unc-spatial-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:17:08.413Z\", \"updated_at\": \"2026-05-14T17:47:53.188Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode crm_scalar --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v2/scalar_unc/crm_best.pt\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"197324\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-scalar-unc-spatial-v2.log\", \"submitted_at\": \"2026-05-14T12:17:08.325Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial benchmark)\", \"data_count\": 100, \"model_name\": \"CRM v2 scalar-uncertainty + SmolVLA K=10\", \"seed\": 42, \"hypothesis\": \"Scalar uncertainty CRM ablation — tests whether per-DOF conformal is superior to scalar aggregated uncertainty for action correction.\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v2/scalar_unc/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"conclusion_note\": \"Director order: 0/30 after 3 tasks, no diagnostic value. Freed bjb1:1 for eval-argmin-only-spatial.\", \"metrics\": {\"tasks_completed\": 3, \"total_tasks\": 10, \"success_rate\": 0, \"successes\": 0, \"rollouts\": 30}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v2/scalar_unc/crm_best.pt\", \"wall_clock_seconds\": 19844.9, \"gpu_hours\": 5.51}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T17:47:53.188Z\"}, \"crm-train-a4-scalar-unc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:48:40.837Z\", \"updated_at\": \"2026-05-14T07:59:32.676Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/train_crm.py --benchmark spatial object --epochs 50 --batch_size 32 --lr 0.001 --K 10 --seed 42 --input_mode scalar_unc --output_dir /root/autodl-tmp/checkpoints/crm/scalar_unc/\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"121984\", \"data_path\": \"/root/autodl-tmp/crm_cache/\", \"data_count\": 26737, \"model_name\": \"CRM-scalar_unc (3D scalar uncertainty)\", \"seed\": 42, \"hypothesis\": \"CRM with scalar Euclidean uncertainty (3D) performs worse than per-DOF (40D), validating per-DOF advantage. Ablation A4, hyperparams matched to plan_001 (bs=32/lr=1e-3).\", \"log_path\": \"/root/autodl-tmp/checkpoints/crm/scalar_unc/train.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm/scalar_unc/crm_best.pt\", \"conclusion_note\": \"Training converged. scalar val_loss 0.008379 < per-DOF 0.009046 — original hypothesis (scalar worse) NOT confirmed on val_loss. Hypothesis pending eval-scalar-unc-spatial task success rate validation.\"}, \"conclusion\": \"killed\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm/scalar_unc/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/checkpoints/crm/scalar_unc/train.log\", \"metrics\": {\"best_val_loss\": 0.008379, \"best_epoch\": 48, \"total_epochs\": 50, \"final_val_loss\": 0.008384, \"final_train_loss\": 0.012959}, \"completed_at\": \"2026-05-14T02:21:00.891Z\", \"conclusion_note\": \"invalidated by D016 C1 fix, 6D state mismatch — checkpoint trained on wrong features\"}, \"crm-train-a3-obs-only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:56:28.643Z\", \"updated_at\": \"2026-05-14T07:59:31.277Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/train_crm.py --benchmark spatial object --epochs 50 --batch_size 512 --lr 0.016 --K 10 --seed 42 --input_mode obs_only --output_dir /root/autodl-tmp/checkpoints/crm/obs_only/\", \"server\": \"bjb1-18228\", \"data_path\": \"/root/autodl-tmp/crm_cache/\", \"data_count\": 26737, \"model_name\": \"CRM-obs_only\", \"seed\": 42, \"hypothesis\": \"CRM without conformal features (obs_only, 990D input) performs significantly worse than full CRM (1030D), validating that per-DOF conformal features are necessary for effective correction\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm/obs_only/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/checkpoints/crm/obs_only/train.log\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T23:43:51.534Z\", \"metrics\": {\"best_val_loss\": 0.018312, \"best_epoch\": 4, \"early_stopped_at_epoch\": \"~15-20\", \"early_stop_reason\": \"val_loss plateau at 0.018 for 10+ epochs (full CRM: 0.009, 2x gap confirms conformal features are critical)\", \"input_dim\": 990, \"params\": 327966}, \"conclusion_note\": \"invalidated by D016 C1 fix, 6D state mismatch — checkpoint trained on wrong features\"}, \"crm-train-v1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:10:36.535Z\", \"updated_at\": \"2026-05-14T07:59:30.290Z\", \"spec\": {\"command\": \"python -u src/train_crm.py --benchmark spatial object --epochs 50 --batch_size 32 --lr 1e-3 --K 10 --seed 42\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"78520\", \"log_path\": \"/root/runs/acr-vla-conformal-refinement/crm-train-v1.log\", \"data_path\": \"/root/autodl-tmp/crm_cache/ (spatial: 12167 + object: 14570 = 26737 samples)\", \"data_count\": 26737, \"model_name\": \"CRM MLP (337K params, 1030D→256→256→30D)\", \"seed\": 42, \"hypothesis\": \"CRM with per-DOF conformal features (1030D input) learns dimension-selective correction, achieving lower action MSE than scalar/no-uncertainty ablations\", \"checkpoint_source\": \"precompute-v4 (spatial+object)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm/\"}, \"reproduce\": {\"finished_at\": \"2026-05-13T22:40:27.930Z\"}, \"failure_reason\": \"RESOLVED: EXIT_CODE=129 was SIGHUP after training completed (50/50 epochs). Not a real failure.\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T22:40:28.559Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T22:40:29.429643+00:00\"}]}, \"metrics\": {\"best_val_loss\": 0.009046, \"best_epoch\": 50, \"total_epochs\": 50, \"checkpoint\": \"crm_best.pt\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm/crm_best.pt\", \"exit_code_note\": \"129 was false alarm - SIGHUP after training completed\"}, \"conclusion_note\": \"invalidated by D016 C1 fix, 6D state mismatch — checkpoint trained on wrong features\"}, \"crm-train-k5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T01:42:55.911Z\", \"updated_at\": \"2026-05-14T07:59:29.396Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/train_crm.py --benchmark spatial object --epochs 50 --batch_size 32 --lr 0.001 --K 5 --seed 42 --cache_dir /root/autodl-tmp/crm_cache_k5/ --output_dir /root/autodl-tmp/checkpoints/crm/k5/\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"139839\", \"data_path\": \"/root/autodl-tmp/crm_cache_k5/\", \"data_count\": 26737, \"model_name\": \"CRM (K=5, 337K params)\", \"seed\": 42, \"hypothesis\": \"CRM with K=5 conformal samples for K sensitivity ablation (K=10 baseline val_loss=0.009046)\", \"log_path\": \"/root/autodl-tmp/checkpoints/crm/k5/train.log\", \"checkpoint_source\": \"from_scratch\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm/k5/crm_best.pt\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T04:12:42.247Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T04:12:44.286094+00:00\"}]}, \"conclusion\": \"killed\", \"metrics\": {\"best_val_loss\": 0.008996, \"best_epoch\": 50, \"total_epochs\": 50, \"comparison\": \"K=5 val_loss 0.008996 ≈ K=10 val_loss 0.009046, near identical\"}, \"completed_at\": \"2026-05-14T07:21:32.072Z\", \"conclusion_note\": \"invalidated by D016 C1 fix, 6D state mismatch — checkpoint trained on wrong features\"}, \"eval-scalar-unc-spatial\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:54:30.549Z\", \"updated_at\": \"2026-05-14T07:52:44.766Z\", \"spec\": {\"hypothesis\": \"Scalar CRM (3D unc) vs per-DOF CRM (40D unc) on spatial task success rate. Val_loss favored scalar (0.008 vs 0.009) but per-DOF expected to win on task success via dimension-selective correction.\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"CRM-scalar_unc (3D scalar uncertainty, 327K params)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm/scalar_unc/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"command\": \"CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode crm_scalar --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm/scalar_unc/crm_best.pt\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": \"143206\", \"log_path\": \"/root/autodl-tmp/eval_results/eval-scalar-unc-spatial.log\", \"failure_reason\": \"D016: C1 (state 6D→8D mismatch). Scalar CRM trained on wrong features. Replaced by eval-scalar-unc-spatial-v2.\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T07:52:15.933Z\", \"conclusion_note\": \"invalidated by D016 C1 bug, pre-fix data collected\"}, \"eval-acr-spatial-v2\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-13T23:04:32.138Z\", \"updated_at\": \"2026-05-14T07:52:43.327Z\", \"reproduce\": {\"finished_at\": \"2026-05-13T23:31:30.005Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-13T23:31:31.129Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:31:32.734610+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm/crm_best.pt\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:1\"], \"pid\": \"117814\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"ACR-VLA (SmolVLA + CRM per-DOF)\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/eval_results/eval-acr-spatial-v2.log\", \"hypothesis\": \"ACR-VLA per-DOF correction improves over SmolVLA baseline on spatial\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"failure_reason\": \"D016: C1 (state 6D→8D mismatch) + W3 (alpha 0.1→0.5). CRM trained on wrong features + CGS quantile wrong. Replaced by eval-acr-spatial-v3.\"}, \"conclusion\": \"killed\", \"conclusion_note\": \"invalidated by D016 C1 bug, pre-fix data collected\"}, \"eval-k5-spatial\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T04:14:23.092Z\", \"updated_at\": \"2026-05-14T07:52:43.134Z\", \"spec\": {\"command\": \"MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 5 --crm_checkpoint /root/autodl-tmp/checkpoints/crm/k5/crm_best.pt\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"154189\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"ACR-VLA K=5 (CRM 337K + SmolVLA 450M)\", \"seed\": 42, \"hypothesis\": \"K=5 vs K=10 ACR-VLA on task success rate.\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm/k5/crm_best.pt\", \"eval_data\": \"LIBERO spatial 10 tasks x 10 rollouts\", \"log_path\": \"/root/autodl-tmp/eval_results/eval-k5-spatial.log\", \"failure_reason\": \"D016: C1 (state 6D→8D mismatch) + W3 (alpha 0.1→0.5). CRM K=5 trained on wrong features. Replaced by eval-k5-spatial-v2.\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T07:52:14.685Z\", \"conclusion_note\": \"invalidated by D016 C1 bug, pre-fix data collected\"}, \"eval-object-v7-full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T00:03:35.642Z\", \"updated_at\": \"2026-05-14T01:45:48.892Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 42\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"125830\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_object/\", \"data_count\": 100, \"model_name\": \"smolvla_libero\", \"seed\": 42, \"hypothesis\": \"SmolVLA baseline on libero_object with K=1 fix (single inference per step)\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"LIBERO object 10 tasks x 10 rollouts\", \"log_path\": \"/root/autodl-tmp/eval_results/eval-object-v6.log\", \"failure_reason\": \"Duplicate entry — same PID 125830 tracked by eval-object-v8-full. Cleaning up.\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T01:45:48.892Z\"}, \"eval-spatial-v6-full\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-13T23:04:28.766Z\", \"updated_at\": \"2026-05-14T00:05:22.619Z\", \"reproduce\": {\"finished_at\": \"2026-05-14T00:03:28.470Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-13T23:34:09.898Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:34:11.481851+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T00:03:30.351859+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 10 --seed 42\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"117486\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"lerobot/smolvla_libero\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/eval_results/eval-spatial-v6-full.log\", \"hypothesis\": \"SmolVLA baseline on libero_spatial with fixed evaluate.py (reset→set_init_state→zero-action)\", \"failure_reason\": \"vla_only mode running K=10 instead of K=1, wasting GPU. Killed and restarted with K=1 fix.\"}, \"conclusion\": \"killed\"}, \"eval-object-v5-full\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-13T23:17:35.776Z\", \"updated_at\": \"2026-05-14T00:04:26.792Z\", \"reproduce\": {\"finished_at\": \"2026-05-13T23:43:52.899Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-13T23:43:53.809Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:43:56.187212+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 42 --smolvla_path /root/autodl-tmp/models/smolvla_libero/\", \"server\": \"bjb2-40593\", \"data_path\": \"/root/autodl-tmp/libero_data/libero_object/\", \"data_count\": 100, \"model_name\": \"smolvla_libero\", \"seed\": 42, \"pid\": 117697, \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval-object-v5-full.log\", \"gpu\": \"cuda:0\", \"note\": \"restored from false DONE/failed — cron misdetected tmux pipe buffering as process exit\", \"failure_reason\": \"vla_only mode running K=10 multi-sampling (should be K=1). Killed by Director order, replaced by eval-object-v7-full with K=1 fix.\"}, \"conclusion\": \"killed\"}, \"eval-acr-vla-spatial-v1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:56:40.287Z\", \"updated_at\": \"2026-05-13T23:14:22.561Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm/crm_best.pt --output_file /root/autodl-tmp/eval_results/acr_vla_spatial_v1.json\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO spatial benchmark (10 tasks)\", \"data_count\": 100, \"model_name\": \"ACR-VLA (SmolVLA + CRM perdof)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm/crm_best.pt\", \"eval_data\": \"LIBERO spatial, 10 tasks x 10 rollouts\", \"parent\": \"train-crm-v1\", \"failure_reason\": \"P0 bug: evaluate.py env.reset() 覆盖 set_init_state 的 demo 初始状态，结果不可信。已被 eval-acr-spatial-v2 替代\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T23:13:00.422Z\"}, \"eval-acr-spatial-v1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:54:28.535Z\", \"updated_at\": \"2026-05-13T23:12:11.315Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm/crm_best.pt --output_file /root/autodl-tmp/eval_results/eval-acr-spatial-v1.json\", \"server\": \"bjb1-18228\", \"data_path\": \"/root/autodl-tmp/libero_data/\", \"data_count\": 100, \"model_name\": \"ACR-VLA (SmolVLA + CRM)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm/crm_best.pt\", \"eval_data\": \"LIBERO spatial (10 tasks x 10 rollouts)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm/crm_best.pt\", \"log_path\": \"/root/autodl-tmp/eval_results/eval-acr-spatial-v1.log\", \"failure_reason\": \"P0 bug: evaluate.py env.reset() 覆盖 set_init_state 的 demo 初始状态，结果不可信\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T23:09:38.077Z\"}, \"eval-reconvla-spatial-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:29:41.730Z\", \"updated_at\": \"2026-05-13T23:12:10.958Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode reconvla --benchmark spatial --n_rollouts 10 --seed 42 --K 10\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"pid\": \"87787\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-reconvla-spatial-v1.log\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"smolvla_libero + ReconVLA argmin\", \"seed\": 42, \"hypothesis\": \"ReconVLA (scalar Euclidean nonconformity + argmin) as baseline for ACR-VLA comparison\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"libero_spatial 10 tasks\", \"failure_reason\": \"P0 bug: evaluate.py env.reset() 覆盖 set_init_state 的 demo 初始状态，结果不可信\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T23:09:40.252Z\"}, \"eval-object-v4-full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T19:13:26.341Z\", \"updated_at\": \"2026-05-13T23:12:10.037Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 42\", \"server\": \"bjb2-40593\", \"gpu\": [\"cuda:0\"], \"pid\": \"103768\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-object-v4-full.log\", \"data_path\": \"/root/autodl-tmp/libero_data/ (object)\", \"data_count\": 100, \"model_name\": \"lerobot/smolvla_libero\", \"seed\": 42, \"hypothesis\": \"SmolVLA with verified-deployed wrapper achieves meaningful success rate on libero_object\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"libero_object 10 tasks\", \"failure_reason\": \"P0 bug: evaluate.py env.reset() 覆盖 set_init_state 的 demo 初始状态，结果不可信\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T23:09:39.017Z\"}, \"eval-spatial-v5-full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T19:16:58.052Z\", \"updated_at\": \"2026-05-13T23:12:09.066Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 10 --seed 42\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"73756\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-spatial-v5-full.log\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": 100, \"model_name\": \"lerobot/smolvla_libero\", \"seed\": 42, \"hypothesis\": \"SmolVLA with verified wrapper + dual camera (agentview + eye_in_hand) achieves >50% on libero_spatial\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"eval_data\": \"libero_spatial 10 tasks\", \"failure_reason\": \"P0 bug: evaluate.py env.reset() 覆盖 set_init_state 的 demo 初始状态，结果不可信\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T23:09:39.445Z\"}, \"eval-spatial-v3-full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T17:38:57.194Z\", \"updated_at\": \"2026-05-13T19:09:00.612Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl && python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 10 --seed 42 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ 2>&1\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:0\"], \"pid\": \"62654\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-spatial-v3-full.log\", \"submitted_at\": \"2026-05-13T17:38:57.172Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": \"10 tasks x 10 rollouts x 300 steps\", \"model_name\": \"lerobot/smolvla_libero (450M, rewritten wrapper aligned with lerobot pipeline)\", \"seed\": 42, \"hypothesis\": \"Rewritten wrapper (fully aligned with lerobot SmolVLAPolicy) achieves >50% on libero_spatial with 10 rollouts\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"failure_reason\": \"D014: wrapper 修复版从未部署到服务器，使用旧 buggy 代码运行，产出无效\", \"wall_clock_seconds\": 5403.4, \"gpu_hours\": 1.5}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T19:09:00.612Z\"}, \"eval-spatial-reeval-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T16:08:51.171Z\", \"updated_at\": \"2026-05-13T16:14:40.934Z\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 3 --seed 42 --smolvla_path /root/autodl-tmp/models/smolvla_libero/\", \"server\": \"autodl-4090x4\", \"gpu\": [\"cuda:0\"], \"pid\": \"87385\", \"data_path\": \"/root/autodl-tmp/libero_data/ (spatial)\", \"data_count\": \"10 tasks x 3 rollouts x 300 steps\", \"model_name\": \"lerobot/smolvla_libero (450M, full fine-tuned)\", \"seed\": 42, \"hypothesis\": \"Fixed wrapper (7 bugs) achieves >50% on libero_spatial\", \"log_path\": \"/tmp/eval_spatial.log\", \"checkpoint_source\": \"lerobot/smolvla_libero\", \"failure_reason\": \"Killed by Director - wrapper not fully fixed, 55.6% result unreliable. Redirected to full wrapper rewrite aligned with lerobot pipeline.\", \"checkpoint_path\": \"N/A\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-13T16:14:40.934Z\"}}, \"count\": 237, \"total\": 237, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6589}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Glob · `toolu_01TZdeg1ohR5wYYx7o44ak6b`</summary>

```json
{
  "pattern": "**/*.json",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "e7adb8c5-8314-4d7b-9cf9-e0493ce6b1ad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S9ujVFna7AfzKXXLUD7uKB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1044,
      "cache_read_input_tokens": 25526,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1044
      },
      "output_tokens": 26,
      "service_tier": "standard",
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

_source line 12 · 2026-05-18T10:43:05.136Z_

<details><summary>↩ Tool result · `toolu_01TZdeg1ohR5wYYx7o44ak6b`</summary>

```text
artifacts/dream_reports/dream_20260513T015051/best/experiment_data.json
artifacts/dream_reports/dream_20260513T015051/median/experiment_data.json
artifacts/dream_reports/dream_20260513T015051/worst/experiment_data.json
artifacts/dream_reports/dream_20260513T023849/best/experiment_data.json
artifacts/dream_reports/dream_20260513T023849/median/experiment_data.json
artifacts/dream_reports/dream_20260513T023849/worst/experiment_data.json
artifacts/figures/object_benchmark_data.json
artifacts/figures/spatial_final_data.json
artifacts/figures/magnitude_sweep_summary.json
artifacts/argmin_seed44_r2_results.json
artifacts/eval-obs-only-object-norm02-seed44-r2/data/seed44_obs_only_norm02_per_task.json
artifacts/seed44_obs_only_norm02_per_task.json
artifacts/eval-vla-mean-object-seed44/data/results_summary.json
artifacts/eval-vla-mean-object-seed44/data/results_summary_3b7d56.json
artifacts/_project/data/magnitude_curve_data.json
artifacts/_project/data/magnitude_curve_data_fa2562.json
artifacts/_project/data/magnitude_curve_data_8affa6.json
artifacts/_project/data/k_value_curve_data.json
artifacts/_project/data/magnitude_curve_data_9096ae.json
artifacts/k_value_curve_data.json
artifacts/magnitude_curve_data.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "2071919e-2e0f-4ad5-9f53-68864864c766",
  "tool_use_result": {
    "filenames": [
      "artifacts/dream_reports/dream_20260513T015051/best/experiment_data.json",
      "artifacts/dream_reports/dream_20260513T015051/median/experiment_data.json",
      "artifacts/dream_reports/dream_20260513T015051/worst/experiment_data.json",
      "artifacts/dream_reports/dream_20260513T023849/best/experiment_data.json",
      "artifacts/dream_reports/dream_20260513T023849/median/experiment_data.json",
      "artifacts/dream_reports/dream_20260513T023849/worst/experiment_data.json",
      "artifacts/figures/object_benchmark_data.json",
      "artifacts/figures/spatial_final_data.json",
      "artifacts/figures/magnitude_sweep_summary.json",
      "artifacts/argmin_seed44_r2_results.json",
      "artifacts/eval-obs-only-object-norm02-seed44-r2/data/seed44_obs_only_norm02_per_task.json",
      "artifacts/seed44_obs_only_norm02_per_task.json",
      "artifacts/eval-vla-mean-object-seed44/data/results_summary.json",
      "artifacts/eval-vla-mean-object-seed44/data/results_summary_3b7d56.json",
      "artifacts/_project/data/magnitude_curve_data.json",
      "artifacts/_project/data/magnitude_curve_data_fa2562.json",
      "artifacts/_project/data/magnitude_curve_data_8affa6.json",
      "artifacts/_project/data/k_value_curve_data.json",
      "artifacts/_project/data/magnitude_curve_data_9096ae.json",
      "artifacts/k_value_curve_data.json",
      "artifacts/magnitude_curve_data.json"
    ],
    "durationMs": 23,
    "numFiles": 21,
    "truncated": false
  }
}
```

</details>

---


### Assistant

_source line 13_

<details><summary>Logged reasoning block</summary>

```text
The registry is too large. Let me use agents to process this efficiently. I'll need to:

1. Parse the registry to find all relevant experiments
2. SSH to servers to check JSON files

Let me spawn multiple agents to handle this in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "97f795c4-b570-43b9-bd88-5575a5e1d185",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FCKsfR2J66JiHL6mkX8R2U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1235,
      "cache_read_input_tokens": 26570,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1235
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

Registry is large. Let me spawn parallel agents to extract the needed information efficiently.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "ab20cda7-f987-4827-95f0-8e6af7caebfc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FCKsfR2J66JiHL6mkX8R2U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1235,
      "cache_read_input_tokens": 26570,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1235
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

<details open><summary>🔧 Tool call — Agent · `toolu_01LkyHAJXMgM6jYEjtYbJhsT`</summary>

```json
{
  "description": "Registry audit for n_rollouts",
  "prompt": "You have a large JSON registry file at:\n/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/c1bdccab-16c6-497c-9d30-0feab97d927d/tool-results/mcp-agent-ml-research-read_registry-1779100984736.txt\n\nThe file has schema: {result: string} where result is a JSON string.\n\nI need you to extract ALL experiments related to evaluations. Specifically, I need to find experiments matching these categories:\n\n1. **obs_only ε=0.2 (norm02)** - 6 seeds (42-47) - these are the main paper results with K=10\n2. **Argmin baseline** - 6 seeds (42-47)\n3. **VLA-only baseline** - 5 seeds (42-46)\n4. **Magnitude curve obs_only** - various ε values (0.03, 0.05, 0.1, 0.2, 0.5, uncapped)\n5. **Magnitude curve perdof** - various ε values (0.03, 0.05, 0.1, 0.2, 0.5, uncapped)\n6. **Scalar CRM** - 4 seeds (42-45)\n\nFor each experiment, extract:\n- exp_id\n- status\n- server\n- seed (if in config or name)\n- n_rollouts (look in config, command, notes, or any field)\n- success_rate or SR metric\n- Any file paths mentioned (JSON output files)\n- The full command or config that shows n_rollouts\n\nAlso specifically flag ALL experiments where n_rollouts=20 or total_rollouts=200.\n\nUse bash with jq or python to parse the file. The file is JSON with a \"result\" key containing a string. Parse it carefully.\n\nReturn a structured summary organized by category, with exp_id, seed, n_rollouts, server, SR for each.",
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
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "80f11860-29ab-4bb5-a2b3-17ca1ef76455",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FCKsfR2J66JiHL6mkX8R2U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1235,
      "cache_read_input_tokens": 26570,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1235
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


### System

_source line 16_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a5dc54df06c763762",
  "tool_use_id": "toolu_01LkyHAJXMgM6jYEjtYbJhsT",
  "description": "Registry audit for n_rollouts",
  "task_type": "local_agent",
  "prompt": "You have a large JSON registry file at:\n/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/c1bdccab-16c6-497c-9d30-0feab97d927d/tool-results/mcp-agent-ml-research-read_registry-1779100984736.txt\n\nThe file has schema: {result: string} where result is a JSON string.\n\nI need you to extract ALL experiments related to evaluations. Specifically, I need to find experiments matching these categories:\n\n1. **obs_only ε=0.2 (norm02)** - 6 seeds (42-47) - these are the main paper results with K=10\n2. **Argmin baseline** - 6 seeds (42-47)\n3. **VLA-only baseline** - 5 seeds (42-46)\n4. **Magnitude curve obs_only** - various ε values (0.03, 0.05, 0.1, 0.2, 0.5, uncapped)\n5. **Magnitude curve perdof** - various ε values (0.03, 0.05, 0.1, 0.2, 0.5, uncapped)\n6. **Scalar CRM** - 4 seeds (42-45)\n\nFor each experiment, extract:\n- exp_id\n- status\n- server\n- seed (if in config or name)\n- n_rollouts (look in config, command, notes, or any field)\n- success_rate or SR metric\n- Any file paths mentioned (JSON output files)\n- The full command or config that shows n_rollouts\n\nAlso specifically flag ALL experiments where n_rollouts=20 or total_rollouts=200.\n\nUse bash with jq or python to parse the file. The file is JSON with a \"result\" key containing a string. Parse it carefully.\n\nReturn a structured summary organized by category, with exp_id, seed, n_rollouts, server, SR for each.",
  "uuid": "79c6e9af-adce-4b34-b022-e6ca340ce9fb",
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d"
}
```

---


## Round 1

## Round 1

3 recorded events


### User

_source line 17 · 2026-05-18T10:43:18.274Z_

You have a large JSON registry file at:
/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/c1bdccab-16c6-497c-9d30-0feab97d927d/tool-results/mcp-agent-ml-research-read_registry-1779100984736.txt

The file has schema: {result: string} where result is a JSON string.

I need you to extract ALL experiments related to evaluations. Specifically, I need to find experiments matching these categories:

1. **obs_only ε=0.2 (norm02)** - 6 seeds (42-47) - these are the main paper results with K=10
2. **Argmin baseline** - 6 seeds (42-47)
3. **VLA-only baseline** - 5 seeds (42-46)
4. **Magnitude curve obs_only** - various ε values (0.03, 0.05, 0.1, 0.2, 0.5, uncapped)
5. **Magnitude curve perdof** - various ε values (0.03, 0.05, 0.1, 0.2, 0.5, uncapped)
6. **Scalar CRM** - 4 seeds (42-45)

For each experiment, extract:
- exp_id
- status
- server
- seed (if in config or name)
- n_rollouts (look in config, command, notes, or any field)
- success_rate or SR metric
- Any file paths mentioned (JSON output files)
- The full command or config that shows n_rollouts

Also specifically flag ALL experiments where n_rollouts=20 or total_rollouts=200.

Use bash with jq or python to parse the file. The file is JSON with a "result" key containing a string. Parse it carefully.

Return a structured summary organized by category, with exp_id, seed, n_rollouts, server, SR for each.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LkyHAJXMgM6jYEjtYbJhsT",
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "e8ce1650-6ac2-4c71-9e66-8ea48f0cd313"
}
```

</details>

---


### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Agent · `toolu_01T2M7sUsRh3qbz75T18NDYF`</summary>

```json
{
  "description": "Read magnitude curve data",
  "prompt": "Read these JSON data files and report their full contents:\n\n1. /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/magnitude_curve_data.json\n2. /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/magnitude_curve_data.json\n3. /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/figures/magnitude_sweep_summary.json\n4. /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/figures/object_benchmark_data.json\n\nReport the full contents of each file, especially:\n- For magnitude curve data: all epsilon values, seeds, SR values, n_rollouts if present, and source file paths\n- For object benchmark data: all methods, seeds, SR values\n\nBe thorough - report every data point.",
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
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "d228c1f8-95f1-44a6-87b1-4e91f6faf325",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FCKsfR2J66JiHL6mkX8R2U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1235,
      "cache_read_input_tokens": 26570,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1235
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


### System

_source line 19_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a11f7ce8b039566e8",
  "tool_use_id": "toolu_01T2M7sUsRh3qbz75T18NDYF",
  "description": "Read magnitude curve data",
  "task_type": "local_agent",
  "prompt": "Read these JSON data files and report their full contents:\n\n1. /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/magnitude_curve_data.json\n2. /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/magnitude_curve_data.json\n3. /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/figures/magnitude_sweep_summary.json\n4. /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/figures/object_benchmark_data.json\n\nReport the full contents of each file, especially:\n- For magnitude curve data: all epsilon values, seeds, SR values, n_rollouts if present, and source file paths\n- For object benchmark data: all methods, seeds, SR values\n\nBe thorough - report every data point.",
  "uuid": "925a66ba-b016-4f84-8d20-929ba71526a4",
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d"
}
```

---


## Round 2

## Round 2

146 recorded events


### User

_source line 20 · 2026-05-18T10:43:22.115Z_

Read these JSON data files and report their full contents:

1. /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/magnitude_curve_data.json
2. /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/magnitude_curve_data.json
3. /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/figures/magnitude_sweep_summary.json
4. /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/figures/object_benchmark_data.json

Report the full contents of each file, especially:
- For magnitude curve data: all epsilon values, seeds, SR values, n_rollouts if present, and source file paths
- For object benchmark data: all methods, seeds, SR values

Be thorough - report every data point.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01T2M7sUsRh3qbz75T18NDYF",
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "55df6b9b-ea97-42ce-af10-ddc8df2db03b"
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
  "task_id": "a5dc54df06c763762",
  "tool_use_id": "toolu_01LkyHAJXMgM6jYEjtYbJhsT",
  "description": "Running Check file size",
  "usage": {
    "total_tokens": 15887,
    "tool_uses": 1,
    "duration_ms": 5474
  },
  "last_tool_name": "Bash",
  "uuid": "a2c573e4-5f56-4c06-a97c-7be6558448dd",
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d"
}
```

---


### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Bash · `toolu_011JaBnFpDvzWewhUL7jL8Xs`</summary>

```json
{
  "command": "wc -c /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/c1bdccab-16c6-497c-9d30-0feab97d927d/tool-results/mcp-agent-ml-research-read_registry-1779100984736.txt",
  "description": "Check file size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LkyHAJXMgM6jYEjtYbJhsT",
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "b967b62d-0954-43cd-9de0-49d24f15f5d5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XBMLn9oj1gN9Prb6sXictA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15876,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15876,
        "ephemeral_1h_input_tokens": 0
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

_source line 23 · 2026-05-18T10:43:23.899Z_

<details><summary>↩ Tool result · `toolu_011JaBnFpDvzWewhUL7jL8Xs`</summary>

```text
368580 /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/c1bdccab-16c6-497c-9d30-0feab97d927d/tool-results/mcp-agent-ml-research-read_registry-1779100984736.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LkyHAJXMgM6jYEjtYbJhsT",
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "0bfed1b8-edf1-4a05-8b27-96d44ef2e7bc"
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
  "task_id": "a5dc54df06c763762",
  "tool_use_id": "toolu_01LkyHAJXMgM6jYEjtYbJhsT",
  "description": "Running Preview file structure",
  "usage": {
    "total_tokens": 15891,
    "tool_uses": 2,
    "duration_ms": 6538
  },
  "last_tool_name": "Bash",
  "uuid": "a142e59f-a9cf-461c-ad3e-27ea0e1dfa57",
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d"
}
```

---


### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Bash · `toolu_01AFCr7gRQLsstqo1NkSqeXu`</summary>

```json
{
  "command": "head -c 2000 /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/c1bdccab-16c6-497c-9d30-0feab97d927d/tool-results/mcp-agent-ml-research-read_registry-1779100984736.txt",
  "description": "Preview file structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LkyHAJXMgM6jYEjtYbJhsT",
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "3aedf1a8-1d98-4b14-91ac-85fdaeb25bd2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XBMLn9oj1gN9Prb6sXictA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15876,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15876,
        "ephemeral_1h_input_tokens": 0
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

_source line 26 · 2026-05-18T10:43:24.870Z_

<details><summary>↩ Tool result · `toolu_01AFCr7gRQLsstqo1NkSqeXu`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-perdof-object-norm02-seed45-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T23:09:08.601Z\", \"updated_at\": \"2026-05-18T10:42:06.788Z\", \"hypothesis\": \"perdof CRM (ε=0.2) seed45 on LIBERO-Object. r3 重试。补充 perdof magnitude curve ε=0.2 数据。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02_seed45_r3.json\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:3\"], \"pid\": 749547, \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_perdof\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"log_path\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed45_r3.json\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\"}, \"metrics\": {\"overall_success_rate\": 0.12, \"tasks_completed\": 10, \"total_rollouts\": 100}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T10:28:49.451Z\"}, \"eval-perdof-object-norm005-seed44\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-17T23:31:56.813Z\", \"updated_at\": \"2026-05-18T10:37:09.805Z\", \"spec\": {\"command\": \"crm_perdof --seed 44 --K 10 --max_correction_norm 0.05\", \"server\": \"bjb1-32546\", \"gpu\": [\"cuda:2\"], \"pid\": \"553052\", \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm005-seed44.log\", \"submitted_at\": \"2026-05-17T23:31:56.266Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LkyHAJXMgM6jYEjtYbJhsT",
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "be799e6e-4a80-4a5a-908c-9026f393565a"
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
  "task_id": "a11f7ce8b039566e8",
  "tool_use_id": "toolu_01T2M7sUsRh3qbz75T18NDYF",
  "description": "Reading artifacts/_project/data/magnitude_curve_data.json",
  "usage": {
    "total_tokens": 15666,
    "tool_uses": 1,
    "duration_ms": 4002
  },
  "last_tool_name": "Read",
  "uuid": "5d9d1ee7-6061-4020-823e-37c3bf8c9ac8",
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d"
}
```

---


### Tool call

_source line 28_

<details open><summary>🔧 Tool call — Read · `toolu_018jvGpndXAyDGy5JUAAPbSb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/magnitude_curve_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01T2M7sUsRh3qbz75T18NDYF",
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "296e8181-5c06-4e50-b2c1-9d76ee9dfe48",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Nam3BKRY3WAEMTckKNrSL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7394,
      "cache_read_input_tokens": 8255,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7394,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
      "service_tier": "standard",
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

_source line 29 · 2026-05-18T10:43:26.126Z_

<details><summary>↩ Tool result · `toolu_018jvGpndXAyDGy5JUAAPbSb`</summary>

```text
1	{
2	  "metadata": {
3	    "benchmark": "LIBERO Object",
4	    "n_tasks": 10,
5	    "n_rollouts_per_task": 10,
6	    "total_per_seed": 100,
7	    "compiled_date": "2026-05-16"
8	  },
9	  "magnitude_curve": {
10	    "obs_only": [
11	      {"norm": 0.03, "sr": 0.16, "successes": 16, "total": 100, "exp_id": "eval-mag-obsonly-norm003-object", "seed": 42},
12	      {"norm": 0.05, "sr": 0.13, "successes": 13, "total": 100, "exp_id": "eval-mag-obsonly-norm005-object", "seed": 42},
13	      {"norm": 0.10, "sr": 0.19, "successes": 19, "total": 100, "exp_id": "eval-acr-object-v4-obs-only", "seed": 42},
14	      {"norm": 0.20, "sr": 0.22, "successes": 22, "total": 100, "exp_id": "eval-acr-object-obs-only-norm02", "seed": 42},
15	      {"norm": 0.30, "sr": 0.19, "successes": 19, "total": 100, "exp_id": "eval-mag-obsonly-norm03-object", "seed": 42},
16	      {"norm": 1.42, "sr": 0.17, "successes": 17, "total": 100, "exp_id": "eval-acr-object-obs-only-default", "seed": 42, "note": "default norm, no clipping"}
17	    ],
18	    "perdof": [
19	      {"norm": 0.03, "sr": 0.14, "successes": 14, "total": 100, "exp_id": "eval-mag-perdof-norm003-object", "seed": 42},
20	      {"norm": 0.05, "sr": 0.14, "successes": 14, "total": 100, "exp_id": "eval-mag-perdof-norm005-object", "seed": 42},
21	      {"norm": 0.10, "sr": 0.11, "successes": 11, "total": 100, "exp_id": "eval-acr-object-v4-perdof", "seed": 42},
22	      {"norm": 0.20, "sr": 0.11, "successes": 11, "total": 100, "exp_id": "eval-mag-perdof-norm02-object", "seed": 42},
23	      {"norm": 0.30, "sr": 0.04, "successes": 4, "total": 100, "exp_id": "eval-mag-perdof-norm03-object-r3", "seed": 42},
24	      {"norm": 1.42, "sr": 0.00, "successes": 0, "total": 100, "exp_id": "eval-acr-object-v4-default-r2", "seed": 42, "note": "default norm, catastrophic failure"}
25	    ]
26	  },
27	  "magnitude_curve_spatial": {
28	    "obs_only": [
29	      {"norm": 0.03, "sr": 0.34, "successes": 34, "total": 100, "exp_id": "eval-mag-obsonly-norm003-b2", "seed": 42},
30	      {"norm": 0.05, "sr": 0.35, "successes": 35, "total": 100, "exp_id": "eval-mag-obsonly-norm005", "seed": 42},
31	      {"norm": 0.10, "sr": 0.35, "successes": 35, "total": 100, "exp_id": "eval-acr-spatial-v4-obs-only-r3", "seed": 42},
32	      {"norm": 0.20, "sr": 0.35, "successes": 35, "total": 100, "exp_id": "eval-mag-obsonly-norm02", "seed": 42},
33	      {"norm": 0.30, "sr": 0.36, "successes": 36, "total": 100, "exp_id": "eval-mag-obsonly-norm03-r2", "seed": 42}
34	    ],
35	    "perdof": [
36	      {"norm": 0.03, "sr": 0.30, "successes": 30, "total": 100, "exp_id": "eval-mag-perdof-norm003", "seed": 42},
37	      {"norm": 0.05, "sr": 0.31, "successes": 31, "total": 100, "exp_id": "eval-mag-perdof-norm005", "seed": 42},
38	      {"norm": 0.10, "sr": 0.35, "successes": 35, "total": 100, "exp_id": "eval-acr-spatial-v4-small-r2", "seed": 42},
39	      {"norm": 0.30, "sr": 0.26, "successes": 26, "total": 100, "exp_id": "eval-mag-perdof-norm03", "seed": 42}
40	    ]
41	  },
42	  "baselines": {
43	    "object": {
44	      "argmin_seed42": {"sr": 0.12, "successes": 12, "total": 100, "exp_id": "eval-reconvla-object", "seed": 42},
45	      "vla_only_seed42": {"sr": 0.12, "successes": 12, "total": 100, "exp_id": "eval-vla-only-object", "seed": 42},
46	      "vla_mean_seed42": {"sr": 0.12, "successes": 12, "total": 100, "exp_id": "eval-vla-mean-object", "seed": 42}
47	    },
48	    "spatial": {
49	      "argmin_seed42": {"sr": 0.34, "successes": 34, "total": 100, "exp_id": "eval-argmin-only-spatial-r2", "seed": 42},
50	      "vla_only_seed42": {"sr": 0.30, "successes": 30, "total": 100, "exp_id": "eval-spatial-v7-full", "seed": 42},
51	      "vla_mean_seed42": {"sr": 0.32, "successes": 32, "total": 100, "exp_id": "eval-vla-mean-spatial", "seed": 42}
52	    }
53	  },
54	  "seed_comparison": {
55	    "obs_only_norm02": [
56	      {"seed": 42, "sr": 0.22, "successes": 22, "total": 100, "exp_id": "eval-acr-object-obs-only-norm02"},
57	      {"seed": 43, "sr": 0.16, "successes": 16, "total": 100, "exp_id": "eval-obs-only-object-norm02-seed43-r2"},
58	      {"seed": 44, "sr": 0.16, "successes": 16, "total": 100, "exp_id": "eval-obs-only-object-norm02-seed44-r2"}
59	    ],
60	    "obs_only_norm01": [
61	      {"seed": 42, "sr": 0.19, "successes": 19, "total": 100, "exp_id": "eval-acr-object-v4-obs-only"},
62	      {"seed": 43, "sr": 0.12, "successes": 12, "total": 100, "exp_id": "eval-obs-only-object-seed43"}
63	    ],
64	    "argmin": [
65	      {"seed": 42, "sr": 0.12, "successes": 12, "total": 100, "exp_id": "eval-reconvla-object"},
66	      {"seed": 43, "sr": 0.17, "successes": 17, "total": 100, "exp_id": "eval-argmin-object-seed43"},
67	      {"seed": 44, "sr": 0.13, "successes": 13, "total": 100, "exp_id": "eval-argmin-object-seed44-r2"}
68	    ],
69	    "perdof_norm01": [
70	      {"seed": 42, "sr": 0.11, "successes": 11, "total": 100, "exp_id": "eval-acr-object-v4-perdof"},
71	      {"seed": 43, "sr": 0.12, "successes": 12, "total": 100, "exp_id": "eval-perdof-object-seed43"}
72	    ],
73	    "perdof_norm02": [
74	      {"seed": 42, "sr": 0.11, "successes": 11, "total": 100, "exp_id": "eval-mag-perdof-norm02-object"},
75	      {"seed": 43, "sr": 0.09, "successes": 9, "total": 100, "exp_id": "eval-mag-perdof-norm02-seed43-object-r3"}
76	    ],
77	    "vla_only": [
78	      {"seed": 42, "sr": 0.12, "successes": 12, "total": 100, "exp_id": "eval-vla-only-object"},
79	      {"seed": 43, "sr": 0.12, "successes": 12, "total": 100, "exp_id": "eval-vla-only-object-seed43"},
80	      {"seed": 44, "sr": 0.10, "successes": 10, "total": 100, "exp_id": "eval-vla-only-object-seed44-r2"}
81	    ],
82	    "vla_mean": [
83	      {"seed": 42, "sr": 0.12, "successes": 12, "total": 100, "exp_id": "eval-vla-mean-object"},
84	      {"seed": 43, "sr": 0.15, "successes": 15, "total": 100, "exp_id": "eval-vla-mean-object-seed43"},
85	      {"seed": 44, "sr": 0.10, "successes": 10, "total": 100, "exp_id": "eval-vla-mean-object-seed44"}
86	    ]
87	  }
88	}
89	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01T2M7sUsRh3qbz75T18NDYF",
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "24d0ca9a-e6f6-4cb9-aa56-afc05cea9edd"
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
  "task_id": "a11f7ce8b039566e8",
  "tool_use_id": "toolu_01T2M7sUsRh3qbz75T18NDYF",
  "description": "Reading artifacts/magnitude_curve_data.json",
  "usage": {
    "total_tokens": 15673,
    "tool_uses": 2,
    "duration_ms": 4902
  },
  "last_tool_name": "Read",
  "uuid": "6cf6e795-bf7d-4faa-bff3-81318fc55906",
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d"
}
```

---


### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Read · `toolu_01JQtT2Dxyqr1cRVokEqdiS5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/magnitude_curve_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01T2M7sUsRh3qbz75T18NDYF",
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "312a0664-1c12-410d-bd39-0c550f4780dd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Nam3BKRY3WAEMTckKNrSL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7394,
      "cache_read_input_tokens": 8255,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7394,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
      "service_tier": "standard",
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

_source line 32 · 2026-05-18T10:43:27.026Z_

<details><summary>↩ Tool result · `toolu_01JQtT2Dxyqr1cRVokEqdiS5`</summary>

```text
1	{
2	  "obs_only": {
3	    "0.03": {
4	      "seeds": {
5	        "42": 0.16
6	      },
7	      "mean": 0.16,
8	      "std": 0.0,
9	      "n_seeds": 1
10	    },
11	    "0.05": {
12	      "seeds": {
13	        "42": 0.13,
14	        "43": 0.14
15	      },
16	      "mean": 0.135,
17	      "std": 0.0071,
18	      "n_seeds": 2
19	    },
20	    "0.1": {
21	      "seeds": {
22	        "42": 0.19,
23	        "43": 0.12,
24	        "44": 0.16,
25	        "45": 0.14
26	      },
27	      "mean": 0.1525,
28	      "std": 0.0299,
29	      "n_seeds": 4
30	    },
31	    "0.2": {
32	      "seeds": {
33	        "42": 0.22,
34	        "43": 0.16,
35	        "44": 0.16,
36	        "45": 0.16,
37	        "46": 0.15,
38	        "47": 0.2
39	      },
40	      "mean": 0.175,
41	      "std": 0.0281,
42	      "n_seeds": 6
43	    },
44	    "0.3": {
45	      "seeds": {
46	        "42": 0.19,
47	        "44": 0.18,
48	        "45": 0.14,
49	        "46": 0.17
50	      },
51	      "mean": 0.17,
52	      "std": 0.0216,
53	      "n_seeds": 4
54	    },
55	    "default": {
56	      "seeds": {
57	        "44": 0.16,
58	        "45": 0.12,
59	        "46": 0.15
60	      },
61	      "mean": 0.1433,
62	      "std": 0.0208,
63	      "n_seeds": 3
64	    }
65	  },
66	  "perdof": {
67	    "0.03": {
68	      "seeds": {
69	        "42": 0.14
70	      },
71	      "mean": 0.14,
72	      "std": 0.0,
73	      "n_seeds": 1
74	    },
75	    "0.05": {
76	      "seeds": {
77	        "42": 0.14
78	      },
79	      "mean": 0.14,
80	      "std": 0.0,
81	      "n_seeds": 1
82	    },
83	    "0.1": {
84	      "seeds": {
85	        "42": 0.11,
86	        "43": 0.12,
87	        "44": 0.08,
88	        "45": 0.11,
89	        "46": 0.1,
90	        "47": 0.14
91	      },
92	      "mean": 0.11,
93	      "std": 0.02,
94	      "n_seeds": 6
95	    },
96	    "0.2": {
97	      "seeds": {
98	        "42": 0.11,
99	        "43": 0.09,
100	        "44": 0.1,
101	        "45": 0.09,
102	        "46": 0.09,
103	        "47": 0.11
104	      },
105	      "mean": 0.0983,
106	      "std": 0.0098,
107	      "n_seeds": 6
108	    },
109	    "0.3": {
110	      "seeds": {
111	        "42": 0.04,
112	        "44": 0.04,
113	        "45": 0.06
114	      },
115	      "mean": 0.0467,
116	      "std": 0.0115,
117	      "n_seeds": 3
118	    },
119	    "default": {
120	      "seeds": {
121	        "42": 0.0,
122	        "44": 0.0,
123	        "46": 0.0
124	      },
125	      "mean": 0.0,
126	      "std": 0.0,
127	      "n_seeds": 3,
128	      "notes": {
129	        "42": "eval-perdof-object-default-seed42-r2, full 10/10 tasks",
130	        "44": "partial 9/10 tasks, 0/90 rollouts, timeout EXIT_CODE=124",
131	        "46": "eval-perdof-object-default-seed46, full 10/10 tasks"
132	      }
133	    }
134	  },
135	  "baselines": {
136	    "vla_only": {
137	      "seeds": {
138	        "42": 0.12,
139	        "43": 0.12,
140	        "44": 0.1,
141	        "45": 0.09,
142	        "46": 0.13
143	      },
144	      "mean": 0.112,
145	      "std": 0.0164,
146	      "n_seeds": 5
147	    },
148	    "vla_mean": {
149	      "seeds": {
150	        "42": 0.12,
151	        "43": 0.15,
152	        "44": 0.1,
153	        "45": 0.13
154	      },
155	      "mean": 0.125,
156	      "std": 0.0208,
157	      "n_seeds": 4
158	    },
159	    "reconvla": {
160	      "seeds": {
161	        "42": 0.12,
162	        "43": 0.17,
163	        "44": 0.13,
164	        "46": 0.1,
165	        "47": 0.1
166	      },
167	      "mean": 0.124,
168	      "std": 0.0288,
169	      "n_seeds": 5
170	    },
171	    "argmin": {
172	      "seeds": {
173	        "45": 0.12
174	      },
175	      "mean": 0.12,
176	      "std": 0.0,
177	      "n_seeds": 1
178	    },
179	    "scalar": {
180	      "seeds": {
181	        "42": 0.09,
182	        "43": 0.1,
183	        "44": 0.06,
184	        "45": 0.09
185	      },
186	      "mean": 0.085,
187	      "std": 0.0173,
188	      "n_seeds": 4,
189	      "note_seed42": "eval-acr-object-v4-scalar on bjb1-32546, 10 tasks x 10 rollouts, max_correction_norm=0.1. Previously omitted.",
190	      "note_seed45_rollouts": "seed45 uses 20 rollouts/task (others use 10). SR=9% is correct but sample size differs."
191	    },
192	    "k1_accg": {
193	      "seeds": {
194	        "42": 0.11,
195	        "43": 0.12,
196	        "44": 0.07
197	      },
198	      "mean": 0.1,
199	      "std": 0.0265,
200	      "n_seeds": 3
201	    },
202	    "k1_multiscale": {
203	      "seeds": {
204	        "42": 0.12,
205	        "43": 0.09,
206	        "44": 0.1
207	      },
208	      "mean": 0.1033,
209	      "std": 0.0153,
210	      "n_seeds": 3
211	    }
212	  },
213	  "sources_detail": {
214	    "obs_only": {
215	      "0.03": {
216	        "42": "bjb1-32546:eval_object_obs_only_norm003.json"
217	      },
218	      "0.05": {
219	        "42": "bjb2-28827:eval_object_obs_only_norm005.json",
220	        "43": "bjb1-32546:eval_object_obs_only_norm005_seed43_r2.json"
221	      },
222	      "0.1": {
223	        "42": "bjb1-32546:eval_object_obs_only.json (default name, actual norm=0.1 per log)",
224	        "43": "bjb1-18228:eval_object_obs_only_seed43.json (default name, actual norm=0.1 per log)",
225	        "44": "bjb1-32546:eval_object_obs_only_norm01_seed44.json",
226	        "45": "bjb1-18228:eval_object_obs_only_norm01_seed45.json"
227	      },
228	      "0.2": {
229	        "42": "bjb1-32546:eval_object_obs_only_norm02.json",
230	        "43": "bjb1-32546:eval_object_obs_only_norm02_seed43_r2.json",
231	        "44": "bjb1-18228:eval_object_obs_only_norm02_seed44.json",
232	        "45": "bjb1-32546:eval_object_obs_only_norm02_seed45.json",
233	        "46": "bjb1-18228:eval_object_obs_only_norm02_seed46.json",
234	        "47": "bjb1-32546:eval_object_obs_only_norm02_seed47.json"
235	      },
236	      "0.3": {
237	        "42": "bjb2-28827:eval_object_obs_only_norm03.json",
238	        "44": "bjb1-32546:eval_object_obs_only_norm03_seed44.json",
239	        "45": "bjb2-28827:eval_object_obs_only_norm03_seed45_r2.json",
240	        "46": "bjb1-32546:eval_object_obs_only_norm03_seed46.json"
241	      },
242	      "default": {
243	        "44": "bjb1-32546:eval_object_obs_only_default_seed44.json (verified uncapped)",
244	        "45": "bjb2-28827:eval_object_obs_only_default_seed45.json (verified uncapped)",
245	        "46": "bjb1-32546:eval_object_obs_only_default_seed46.json"
246	      }
247	    },
248	    "perdof": {
249	      "0.03": {
250	        "42": "bjb2-28827:eval_object_perdof_norm003.json"
251	      },
252	      "0.05": {
253	        "42": "bjb2-28827:eval_object_perdof_norm005.json"
254	      },
255	      "0.1": {
256	        "42": "bjb1-32546:eval_object_perdof.json (default name, actual norm=0.1)",
257	        "43": "bjb1-18228:eval_object_perdof_seed43.json (default name, actual norm=0.1)",
258	        "44": "bjb1-18228:eval_object_perdof_norm01_seed44.json",
259	        "45": "bjb1-32546:eval_object_perdof_norm01_seed45.json",
260	        "46": "bjb1-32546:eval_object_perdof_norm01_seed46.json",
261	        "47": "bjb1-32546:eval_object_perdof_norm01_seed47_r2.json"
262	      },
263	      "0.2": {
264	        "42": "bjb1-32546:eval_object_perdof_norm02.json",
265	        "43": "bjb2-28827:eval_object_perdof_norm02_seed43_r3.json",
266	        "44": "bjb2-28827:eval_object_perdof_norm02_seed44.json",
267	        "45": "bjb2-28827:eval_object_perdof_norm02_seed45.json",
268	        "46": "bjb2-28827:eval_object_perdof_norm02_seed46.json",
269	        "47": "bjb2-28827:eval_object_perdof_norm02_seed47.json"
270	      },
271	      "0.3": {
272	        "42": "bjb2-28827:eval_object_perdof_norm03_r3.json",
273	        "44": "bjb1-18228:eval_object_perdof_norm03_seed44.json",
274	        "45": "bjb1-32546:eval_object_perdof_norm03_seed45_r2.json"
275	      },
276	      "default": {
277	        "42": "bjb1-18228:eval_object_perdof_default_norm_r2.json",
278	        "44": "partial (9/10 tasks, 0/90 rollouts, timeout)",
279	        "46": "bjb1-32546:eval_object_perdof_default_seed46.json"
280	      }
281	    }
282	  },
283	  "collected_at": "2026-05-18T05:55:00.000000",
284	  "servers_checked": [
285	    "bjb2-28827",
286	    "bjb1-32546",
287	    "bjb1-18228",
288	    "bjb2-40593"
289	  ],
290	  "notes": {
291	    "obs_only_default_seed42_reclassified": "eval_object_obs_only.json (SR=0.19) reclassified to epsilon=0.1 per log verification. Reviewer Report #22.",
292	    "obs_only_default_seed43_reclassified": "eval_object_obs_only_seed43.json (SR=0.12) reclassified to epsilon=0.1 per log verification. Reviewer Report #22.",
293	    "perdof_default_seed46_zero": "eval_object_perdof_default_seed46.json on bjb1-32546 had 0.00 SR. Completed all 10 tasks x 10 rollouts with zero successes. Included as legitimate negative result.",
294	    "perdof_default_seed42_r2_included": "eval_object_perdof_default_norm_r2.json on bjb1-18228 had 0.00 SR. Previously excluded as retry, now INCLUDED per Reviewer Report #21 as valid uncapped data point.",
295	    "excluded_spatial": "eval_mag_obsonly_norm03.json and eval_mag_obsonly_norm003.json are spatial benchmark, excluded.",
296	    "excluded_openvla": "eval_openvla_object_vla_only_seed42.json (OpenVLA model, 0% SR) excluded as different model.",
297	    "k5_variant": "eval_object_obs_only_norm02_k5_seed42.json on bjb1-18228 (SR=0.14, K=5) excluded from main curve (different K parameter).",
298	    "bjb2_40593_duplicate": "eval_object_obs_only.json on bjb2-40593 (SR=0.19) is duplicate of seed42 on bjb1-32546, not counted twice.",
299	    "perdof_default_reclassified_20260518": "CRITICAL FIX: perdof 'default' seed42/43/44 reclassified to epsilon=0.1. Reviewer Report #20. perdof uncapped now has seed42-r2=0%, seed44=0%(partial), seed46=0% (n=3).",
300	    "obs_only_default_reclassified_20260518": "CRITICAL FIX: obs_only 'default' seed42/43 reclassified to epsilon=0.1 per log verification. Reviewer Report #22. seed44/45 pending log verification."
301	  }
302	}
303	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01T2M7sUsRh3qbz75T18NDYF",
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "25c7854d-c048-4b9a-bbbe-5eb003be3da5"
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
  "task_id": "a11f7ce8b039566e8",
  "tool_use_id": "toolu_01T2M7sUsRh3qbz75T18NDYF",
  "description": "Reading artifacts/figures/magnitude_sweep_summary.json",
  "usage": {
    "total_tokens": 15680,
    "tool_uses": 3,
    "duration_ms": 5426
  },
  "last_tool_name": "Read",
  "uuid": "21c6fbfd-e8da-4f84-8123-1f6a976f7776",
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d"
}
```

---


### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Read · `toolu_01MussZUgXQGJr6YRbnxXkMD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/figures/magnitude_sweep_summary.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01T2M7sUsRh3qbz75T18NDYF",
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "41ef55c6-6c0f-452d-afd4-9dc4f8d33747",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Nam3BKRY3WAEMTckKNrSL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7394,
      "cache_read_input_tokens": 8255,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7394,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
      "service_tier": "standard",
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

_source line 35 · 2026-05-18T10:43:27.547Z_

<details><summary>↩ Tool result · `toolu_01MussZUgXQGJr6YRbnxXkMD`</summary>

```text
1	{
2	  "baselines": {
3	    "argmin": 0.34,
4	    "vla_only": 0.3,
5	    "vla_mean": 0.32
6	  },
7	  "perdof": {},
8	  "obs_only": {}
9	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01T2M7sUsRh3qbz75T18NDYF",
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "9ebbf453-2cfa-42a3-8b6b-42386e7731c7"
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
  "task_id": "a11f7ce8b039566e8",
  "tool_use_id": "toolu_01T2M7sUsRh3qbz75T18NDYF",
  "description": "Reading artifacts/figures/object_benchmark_data.json",
  "usage": {
    "total_tokens": 15687,
    "tool_uses": 4,
    "duration_ms": 5710
  },
  "last_tool_name": "Read",
  "uuid": "9fa40b82-3825-41ae-95ec-b8868380af00",
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d"
}
```

---


### Tool call

_source line 37_

<details open><summary>🔧 Tool call — Read · `toolu_01YVt16JX5EER2n46cXeCJHE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/figures/object_benchmark_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01T2M7sUsRh3qbz75T18NDYF",
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "636286ee-9205-47e7-9a6b-64190f711ae0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Nam3BKRY3WAEMTckKNrSL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7394,
      "cache_read_input_tokens": 8255,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7394,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
      "service_tier": "standard",
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

_source line 38 · 2026-05-18T10:43:27.831Z_

<details><summary>↩ Tool result · `toolu_01YVt16JX5EER2n46cXeCJHE`</summary>

```text
1	{
2	  "VLA-only": {
3	    "per_task": {
4	      "alphabet_soup": 0.0,
5	      "cream_cheese": 10.0,
6	      "salad_dressing": 20.0,
7	      "bbq_sauce": 20.0,
8	      "ketchup": 0.0,
9	      "tomato_sauce": 10.0,
10	      "butter": 0.0,
11	      "milk": 10.0,
12	      "chocolate_pudding": 20.0,
13	      "orange_juice": 30.0
14	    },
15	    "overall_sr": 12.0,
16	    "n_tasks_completed": 10,
17	    "exp_id": "eval-vla-only-object",
18	    "status": "DONE"
19	  },
20	  "VLA-mean": {
21	    "per_task": {
22	      "alphabet_soup": 0.0,
23	      "cream_cheese": 0.0,
24	      "salad_dressing": 10.0,
25	      "bbq_sauce": 30.0,
26	      "ketchup": 10.0,
27	      "tomato_sauce": 10.0,
28	      "butter": 0.0,
29	      "milk": 20.0,
30	      "chocolate_pudding": 30.0,
31	      "orange_juice": 10.0
32	    },
33	    "overall_sr": 12.0,
34	    "n_tasks_completed": 10,
35	    "exp_id": "eval-vla-mean-object",
36	    "status": "DONE"
37	  },
38	  "ReconVLA": {
39	    "per_task": {
40	      "alphabet_soup": 0.0,
41	      "cream_cheese": 0.0,
42	      "salad_dressing": 10.0,
43	      "bbq_sauce": 30.0,
44	      "ketchup": 0.0,
45	      "tomato_sauce": 0.0,
46	      "butter": 10.0,
47	      "milk": 10.0,
48	      "chocolate_pudding": 30.0,
49	      "orange_juice": 30.0
50	    },
51	    "overall_sr": 12.0,
52	    "n_tasks_completed": 10,
53	    "exp_id": "eval-reconvla-object",
54	    "status": "DONE"
55	  },
56	  "ACR per-DOF": {
57	    "per_task": {
58	      "alphabet_soup": 0.0,
59	      "cream_cheese": 0.0,
60	      "salad_dressing": 20.0,
61	      "bbq_sauce": 30.0,
62	      "ketchup": 0.0,
63	      "tomato_sauce": 0.0,
64	      "butter": 10.0,
65	      "milk": 0.0,
66	      "chocolate_pudding": 20.0,
67	      "orange_juice": 30.0
68	    },
69	    "overall_sr": 11.0,
70	    "n_tasks_completed": 10,
71	    "exp_id": "eval-acr-object-v4-perdof",
72	    "status": "DONE"
73	  },
74	  "ACR obs-only": {
75	    "per_task": {
76	      "alphabet_soup": 0.0,
77	      "cream_cheese": 10.0,
78	      "salad_dressing": 20.0,
79	      "bbq_sauce": 40.0,
80	      "ketchup": 10.0,
81	      "tomato_sauce": 0.0,
82	      "butter": 10.0,
83	      "milk": 20.0,
84	      "chocolate_pudding": 50.0,
85	      "orange_juice": 30.0
86	    },
87	    "overall_sr": 19.0,
88	    "n_tasks_completed": 10,
89	    "exp_id": "eval-acr-object-v4-obs-only",
90	    "status": "DONE"
91	  },
92	  "ACR scalar": {
93	    "per_task": {
94	      "alphabet_soup": 0.0,
95	      "cream_cheese": 0.0,
96	      "salad_dressing": 10.0,
97	      "bbq_sauce": 10.0,
98	      "ketchup": 0.0,
99	      "tomato_sauce": 0.0,
100	      "butter": 10.0,
101	      "milk": 10.0,
102	      "chocolate_pudding": 30.0,
103	      "orange_juice": 20.0
104	    },
105	    "overall_sr": 9.0,
106	    "n_tasks_completed": 10,
107	    "exp_id": "eval-acr-object-v4-scalar",
108	    "status": "DONE"
109	  },
110	  "ACR obs-only-0.2": {
111	    "per_task": {
112	      "alphabet_soup": 0.0,
113	      "cream_cheese": 0.0,
114	      "salad_dressing": 30.0,
115	      "bbq_sauce": 40.0,
116	      "ketchup": 20.0,
117	      "tomato_sauce": 10.0,
118	      "butter": 10.0,
119	      "milk": 20.0,
120	      "chocolate_pudding": 60.0,
121	      "orange_juice": 30.0
122	    },
123	    "overall_sr": 22.0,
124	    "n_tasks_completed": 10,
125	    "exp_id": "eval-acr-object-obs-only-norm02",
126	    "status": "DONE"
127	  }
128	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01T2M7sUsRh3qbz75T18NDYF",
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "c57f98d5-f360-4f61-8fd2-2bf9e7f72b53"
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
  "task_id": "a5dc54df06c763762",
  "tool_use_id": "toolu_01LkyHAJXMgM6jYEjtYbJhsT",
  "description": "Running Parse registry JSON and categorize all eval experiments",
  "usage": {
    "total_tokens": 18087,
    "tool_uses": 3,
    "duration_ms": 54346
  },
  "last_tool_name": "Bash",
  "uuid": "3fe9e85a-2f32-4524-8669-b410925aca42",
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d"
}
```

---


### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Bash · `toolu_01Su6BwoXFh2J5uVit8W3YcU`</summary>

```json
{
  "command": "cat << 'PYEOF' > /tmp/parse_registry.py\nimport json\nimport sys\nimport re\n\nREGISTRY_FILE = \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/c1bdccab-16c6-497c-9d30-0feab97d927d/tool-results/mcp-agent-ml-research-read_registry-1779100984736.txt\"\n\nwith open(REGISTRY_FILE, 'r') as f:\n    raw = json.load(f)\n\ndata = json.loads(raw[\"result\"])\nexperiments = data[\"data\"][\"experiments\"]\n\nprint(f\"Total experiments in registry: {len(experiments)}\\n\")\n\n# Categorize experiments\ncategories = {\n    \"obs_only_norm02\": [],       # obs_only ε=0.2 (norm02), 6 seeds\n    \"argmin_baseline\": [],        # argmin baseline\n    \"vla_only_baseline\": [],      # VLA-only baseline\n    \"magnitude_obs_only\": [],     # magnitude curve obs_only various ε\n    \"magnitude_perdof\": [],       # magnitude curve perdof various ε\n    \"scalar_crm\": [],             # scalar CRM\n    \"other_eval\": [],             # other evals\n}\n\ndef extract_seed(exp_id, spec, exp):\n    \"\"\"Extract seed from various locations\"\"\"\n    # From spec\n    if spec.get(\"seed\") is not None:\n        return spec[\"seed\"]\n    # From command\n    cmd = spec.get(\"command\", \"\")\n    m = re.search(r'--seed\\s+(\\d+)', cmd)\n    if m:\n        return int(m.group(1))\n    # From exp_id\n    m = re.search(r'seed(\\d+)', exp_id)\n    if m:\n        return int(m.group(1))\n    # From config\n    config = spec.get(\"config\", {})\n    if isinstance(config, dict) and config.get(\"seed\"):\n        return config[\"seed\"]\n    return None\n\ndef extract_n_rollouts(exp_id, spec, exp):\n    \"\"\"Extract n_rollouts from various locations\"\"\"\n    cmd = spec.get(\"command\", \"\")\n    m = re.search(r'--n_rollouts\\s+(\\d+)', cmd)\n    if m:\n        return int(m.group(1))\n    # From spec fields\n    if spec.get(\"n_rollouts\"):\n        return spec[\"n_rollouts\"]\n    # From eval_data\n    eval_data = spec.get(\"eval_data\", \"\")\n    m = re.search(r'(\\d+)\\s*rollouts', eval_data)\n    if m:\n        return int(m.group(1))\n    # From config\n    config = spec.get(\"config\", {})\n    if isinstance(config, dict) and config.get(\"n_rollouts\"):\n        return config[\"n_rollouts\"]\n    return None\n\ndef extract_total_rollouts(exp):\n    \"\"\"Extract total_rollouts from metrics\"\"\"\n    metrics = exp.get(\"metrics\", {})\n    if isinstance(metrics, dict):\n        return metrics.get(\"total_rollouts\")\n    return None\n\ndef extract_sr(exp):\n    \"\"\"Extract success rate\"\"\"\n    metrics = exp.get(\"metrics\", {})\n    if isinstance(metrics, dict):\n        sr = metrics.get(\"overall_success_rate\")\n        if sr is not None:\n            return sr\n        sr = metrics.get(\"success_rate\")\n        if sr is not None:\n            return sr\n    return None\n\ndef extract_files(exp_id, spec, exp):\n    \"\"\"Extract file paths\"\"\"\n    files = []\n    cmd = spec.get(\"command\", \"\")\n    m = re.search(r'--output_file\\s+(\\S+)', cmd)\n    if m:\n        files.append(m.group(1))\n    if spec.get(\"log_path\"):\n        files.append(spec[\"log_path\"])\n    if spec.get(\"output_file\"):\n        files.append(spec[\"output_file\"])\n    return list(set(files))\n\ndef extract_epsilon(exp_id, spec):\n    \"\"\"Extract epsilon / max_correction_norm\"\"\"\n    cmd = spec.get(\"command\", \"\")\n    m = re.search(r'--max_correction_norm\\s+([\\d.]+)', cmd)\n    if m:\n        return float(m.group(1))\n    # from exp_id\n    norm_map = {\n        \"norm003\": 0.03, \"norm005\": 0.05, \"norm01\": 0.1,\n        \"norm02\": 0.2, \"norm05\": 0.5, \"uncapped\": \"uncapped\"\n    }\n    for k, v in norm_map.items():\n        if k in exp_id:\n            return v\n    return None\n\ndef categorize(exp_id, exp):\n    spec = exp.get(\"spec\", {})\n    cmd = spec.get(\"command\", \"\") or \"\"\n    hypothesis = exp.get(\"hypothesis\", \"\") or \"\"\n    \n    # Only look at eval experiments\n    if not exp_id.startswith(\"eval\"):\n        return None\n    \n    mode = \"\"\n    if \"--mode crm_obs_only\" in cmd or \"crm_obs_only\" in cmd or \"mode crm_obs_only\" in cmd:\n        mode = \"obs_only\"\n    elif \"--mode crm_perdof\" in cmd or \"crm_perdof\" in cmd or \"mode crm_perdof\" in cmd:\n        mode = \"perdof\"\n    elif \"--mode argmin\" in cmd or \"argmin\" in cmd:\n        mode = \"argmin\"\n    elif \"--mode vla_only\" in cmd or \"vla_only\" in cmd or \"vla-only\" in exp_id:\n        mode = \"vla_only\"\n    elif \"--mode crm_scalar\" in cmd or \"scalar\" in exp_id:\n        mode = \"scalar\"\n    \n    # Also check exp_id for mode hints\n    if \"obs-only\" in exp_id or \"obsonly\" in exp_id:\n        mode = \"obs_only\"\n    if \"perdof\" in exp_id:\n        mode = \"perdof\"\n    if \"argmin\" in exp_id:\n        mode = \"argmin\"\n    if \"vla-only\" in exp_id or \"vlaonly\" in exp_id:\n        mode = \"vla_only\"\n    if \"scalar\" in exp_id:\n        mode = \"scalar\"\n    \n    epsilon = extract_epsilon(exp_id, spec)\n    \n    # Categorize\n    if mode == \"argmin\":\n        return \"argmin_baseline\"\n    elif mode == \"vla_only\":\n        return \"vla_only_baseline\"\n    elif mode == \"scalar\":\n        return \"scalar_crm\"\n    elif mode == \"obs_only\":\n        if epsilon == 0.2 or \"norm02\" in exp_id:\n            # Check if it's part of magnitude curve or main results\n            if \"magnitude\" in exp_id or \"mag\" in exp_id or \"curve\" in exp_id:\n                return \"magnitude_obs_only\"\n            # If epsilon is exactly 0.2 and has a seed, it could be main results or magnitude curve\n            # Main results = 6 seeds with norm02\n            return \"obs_only_norm02\"\n        elif epsilon is not None or \"uncapped\" in exp_id:\n            return \"magnitude_obs_only\"\n        else:\n            return \"obs_only_norm02\"  # default obs_only to norm02 category\n    elif mode == \"perdof\":\n        if epsilon == 0.2 or \"norm02\" in exp_id:\n            # perdof magnitude curve includes ε=0.2\n            return \"magnitude_perdof\"\n        elif epsilon is not None or \"uncapped\" in exp_id:\n            return \"magnitude_perdof\"\n        else:\n            return \"magnitude_perdof\"\n    \n    return \"other_eval\"\n\n# Process all experiments\nfor exp_id, exp in sorted(experiments.items()):\n    if not exp_id.startswith(\"eval\"):\n        continue\n    \n    spec = exp.get(\"spec\", {})\n    cat = categorize(exp_id, exp)\n    if cat is None:\n        continue\n    \n    entry = {\n        \"exp_id\": exp_id,\n        \"status\": exp.get(\"status\"),\n        \"server\": spec.get(\"server\"),\n        \"seed\": extract_seed(exp_id, spec, exp),\n        \"n_rollouts\": extract_n_rollouts(exp_id, spec, exp),\n        \"total_rollouts\": extract_total_rollouts(exp),\n        \"sr\": extract_sr(exp),\n        \"epsilon\": extract_epsilon(exp_id, spec),\n        \"files\": extract_files(exp_id, spec, exp),\n        \"command\": spec.get(\"command\", \"\"),\n        \"conclusion\": exp.get(\"conclusion\"),\n        \"hypothesis\": exp.get(\"hypothesis\", \"\"),\n    }\n    categories[cat].append(entry)\n\n# Print results\ndef print_category(name, entries, show_epsilon=False):\n    print(f\"\\n{'='*100}\")\n    print(f\"  {name}  ({len(entries)} experiments)\")\n    print(f\"{'='*100}\")\n    \n    # Sort by seed, then epsilon, then exp_id\n    entries.sort(key=lambda e: (e.get(\"seed\") or 999, str(e.get(\"epsilon\") or \"\"), e[\"exp_id\"]))\n    \n    for e in entries:\n        flag = \"\"\n        if e[\"n_rollouts\"] == 20:\n            flag = \" *** n_rollouts=20 ***\"\n        if e[\"total_rollouts\"] == 200:\n            flag += \" *** total_rollouts=200 ***\"\n        \n        eps_str = f\"  ε={e['epsilon']}\" if show_epsilon and e['epsilon'] is not None else \"\"\n        sr_str = f\"  SR={e['sr']}\" if e['sr'] is not None else \"  SR=N/A\"\n        seed_str = f\"  seed={e['seed']}\" if e['seed'] is not None else \"\"\n        \n        print(f\"\\n  exp_id: {e['exp_id']}\")\n        print(f\"    status={e['status']}  server={e['server']}{seed_str}{eps_str}\")\n        print(f\"    n_rollouts={e['n_rollouts']}  total_rollouts={e['total_rollouts']}{sr_str}\")\n        print(f\"    conclusion={e['conclusion']}{flag}\")\n        if e['files']:\n            print(f\"    files: {e['files']}\")\n        if e['command']:\n            # Truncate long commands\n            cmd = e['command']\n            if len(cmd) > 200:\n                cmd = cmd[:200] + \"...\"\n            print(f\"    cmd: {cmd}\")\n        if e['hypothesis']:\n            hyp = e['hypothesis'][:150]\n            print(f\"    hypothesis: {hyp}\")\n\nprint_category(\"1. OBS_ONLY ε=0.2 (norm02) — Main Paper Results K=10\", categories[\"obs_only_norm02\"], show_epsilon=True)\nprint_category(\"2. ARGMIN BASELINE\", categories[\"argmin_baseline\"])\nprint_category(\"3. VLA-ONLY BASELINE\", categories[\"vla_only_baseline\"])\nprint_category(\"4. MAGNITUDE CURVE OBS_ONLY — Various ε\", categories[\"magnitude_obs_only\"], show_epsilon=True)\nprint_category(\"5. MAGNITUDE CURVE PERDOF — Various ε\", categories[\"magnitude_perdof\"], show_epsilon=True)\nprint_category(\"6. SCALAR CRM\", categories[\"scalar_crm\"])\nprint_category(\"7. OTHER EVAL (uncategorized)\", categories[\"other_eval\"], show_epsilon=True)\n\n# Summary of n_rollouts=20 or total_rollouts=200 flagged experiments\nprint(f\"\\n{'='*100}\")\nprint(f\"  FLAGGED: n_rollouts=20 or total_rollouts=200\")\nprint(f\"{'='*100}\")\nflagged = []\nfor cat, entries in categories.items():\n    for e in entries:\n        if e[\"n_rollouts\"] == 20 or e[\"total_rollouts\"] == 200:\n            flagged.append((cat, e))\n\nif flagged:\n    for cat, e in flagged:\n        print(f\"\\n  [{cat}] {e['exp_id']}\")\n        print(f\"    n_rollouts={e['n_rollouts']}  total_rollouts={e['total_rollouts']}  seed={e['seed']}  SR={e['sr']}  status={e['status']}\")\n        if e['command']:\n            print(f\"    cmd: {e['command'][:200]}\")\nelse:\n    print(\"  None found.\")\n\n# Per-category seed coverage summary\nprint(f\"\\n{'='*100}\")\nprint(f\"  SEED COVERAGE SUMMARY\")\nprint(f\"{'='*100}\")\nfor cat_name, display_name in [\n    (\"obs_only_norm02\", \"obs_only ε=0.2\"),\n    (\"argmin_baseline\", \"argmin\"),\n    (\"vla_only_baseline\", \"vla_only\"),\n    (\"scalar_crm\", \"scalar CRM\"),\n]:\n    seeds = sorted(set(e[\"seed\"] for e in categories[cat_name] if e[\"seed\"] is not None))\n    done_seeds = sorted(set(e[\"seed\"] for e in categories[cat_name] if e[\"seed\"] is not None and e[\"status\"] == \"DONE\"))\n    print(f\"  {display_name}: all seeds={seeds}, DONE seeds={done_seeds}\")\n\nprint(f\"\\n  Magnitude obs_only epsilons:\")\neps_set = sorted(set(str(e[\"epsilon\"]) for e in categories[\"magnitude_obs_only\"] if e[\"epsilon\"] is not None))\nprint(f\"    ε values present: {eps_set}\")\nfor eps in eps_set:\n    exps = [e for e in categories[\"magnitude_obs_only\"] if str(e[\"epsilon\"]) == eps]\n    seeds = sorted(set(e[\"seed\"] for e in exps if e[\"seed\"] is not None))\n    done = [e for e in exps if e[\"status\"] == \"DONE\"]\n    print(f\"    ε={eps}: {len(exps)} exps, seeds={seeds}, {len(done)} DONE\")\n\nprint(f\"\\n  Magnitude perdof epsilons:\")\neps_set = sorted(set(str(e[\"epsilon\"]) for e in categories[\"magnitude_perdof\"] if e[\"epsilon\"] is not None))\nprint(f\"    ε values present: {eps_set}\")\nfor eps in eps_set:\n    exps = [e for e in categories[\"magnitude_perdof\"] if str(e[\"epsilon\"]) == eps]\n    seeds = sorted(set(e[\"seed\"] for e in exps if e[\"seed\"] is not None))\n    done = [e for e in exps if e[\"status\"] == \"DONE\"]\n    print(f\"    ε={eps}: {len(exps)} exps, seeds={seeds}, {len(done)} DONE\")\n\nPYEOF\npython3 /tmp/parse_registry.py",
  "description": "Parse registry JSON and categorize all eval experiments",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LkyHAJXMgM6jYEjtYbJhsT",
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "f3d4a12b-a0af-44dc-94c6-48ad954c9131",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HMLGPDbrCxWrdsfgHmbfuE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2196,
      "cache_read_input_tokens": 15876,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2196,
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

_source line 41 · 2026-05-18T10:44:12.976Z_

<details><summary>↩ Tool result · `toolu_01Su6BwoXFh2J5uVit8W3YcU`</summary>

```text
&lt;persisted-output>
Output too large (112.1KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/c1bdccab-16c6-497c-9d30-0feab97d927d/tool-results/bkoeg1h8a.txt

Preview (first 2KB):
Total experiments in registry: 237


====================================================================================================
  1. OBS_ONLY ε=0.2 (norm02) — Main Paper Results K=10  (28 experiments)
====================================================================================================

  exp_id: eval-acr-object-obs-only-default
    status=DONE  server=bjb1-32546  seed=42
    n_rollouts=10  total_rollouts=None  SR=N/A
    conclusion=success
    files: ['logs/eval_object_obs_only_default_norm.json', '~/runs/acr-vla-conformal-refinement/eval-acr-object-obs-only-default.log']
    cmd: python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval...
    hypothesis: obs_only CRM v3-norm with DEFAULT max_correction_norm (~1.42, no magnitude control) on LIBERO object benchmark. Paired with eval-acr-object-v4-default

  exp_id: eval-acr-spatial-v4-obs-only
    status=DONE  server=bjb2-40593  seed=42
    n_rollouts=10  total_rollouts=None  SR=N/A
    conclusion=failed
    files: ['/root/autodl-tmp/logs/eval-acr-spatial-v4-obs-only.log']
    cmd: python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3/obs_only/crm_best.pt
    hypothesis: D020: obs_only CRM (val_loss 0.0165, 54% better than perdof 0.0358) with max_correction_norm=0.1. If obs_only >= v4-small (perdof) → Claim 1 needs res

  exp_id: eval-mag-obsonly-norm03-b3
    status=DONE  server=bjb2-28827  seed=42
    n_rollouts=None  total_rollouts=None  SR=N/A
    conclusion=killed
    files: ['~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm03-b3.log']
    cmd: crm_obs_only spatial norm=0.3 (killed)
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LkyHAJXMgM6jYEjtYbJhsT",
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "53a3a176-57ba-44eb-8af9-d401abef3d7b"
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
  "task_id": "a5dc54df06c763762",
  "tool_use_id": "toolu_01LkyHAJXMgM6jYEjtYbJhsT",
  "description": "Reading ~/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/c1bdccab-16c6-497c-9d30-0feab97d927d/tool-results/bkoeg1h8a.txt",
  "usage": {
    "total_tokens": 22783,
    "tool_uses": 4,
    "duration_ms": 59342
  },
  "last_tool_name": "Read",
  "uuid": "8224c4c7-3869-4a11-b3b7-cd74fe24ce01",
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d"
}
```

---


### Tool call

_source line 43_

<details open><summary>🔧 Tool call — Read · `toolu_01PAFEJPfbUVhSFo7FMQ1mQp`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/c1bdccab-16c6-497c-9d30-0feab97d927d/tool-results/bkoeg1h8a.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LkyHAJXMgM6jYEjtYbJhsT",
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "9c57e7bc-dd1b-48f6-8406-9b11296231d3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TiV5aiV3n1hdGfZuGBKTgb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4694,
      "cache_read_input_tokens": 18072,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4694,
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

_source line 44 · 2026-05-18T10:44:17.872Z_

<details><summary>↩ Tool result · reported error · `toolu_01PAFEJPfbUVhSFo7FMQ1mQp`</summary>

```text
File content (44453 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LkyHAJXMgM6jYEjtYbJhsT",
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "d91204af-7cce-46b7-b8ba-6ed979b2ae2c",
  "tool_use_result": "Error: File content (44453 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
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
  "task_id": "a5dc54df06c763762",
  "tool_use_id": "toolu_01LkyHAJXMgM6jYEjtYbJhsT",
  "description": "Reading ~/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/c1bdccab-16c6-497c-9d30-0feab97d927d/tool-results/bkoeg1h8a.txt",
  "usage": {
    "total_tokens": 23066,
    "tool_uses": 5,
    "duration_ms": 63137
  },
  "last_tool_name": "Read",
  "uuid": "3a988828-974e-4dba-a628-9ce3760e58bf",
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d"
}
```

---


### Tool call

_source line 46_

<details open><summary>🔧 Tool call — Read · `toolu_01Wt1N6ESEEaxQf7PSAV2XgB`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/c1bdccab-16c6-497c-9d30-0feab97d927d/tool-results/bkoeg1h8a.txt",
  "limit": 500,
  "offset": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LkyHAJXMgM6jYEjtYbJhsT",
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "c76b7ac3-15a2-4199-a176-92f58ca5b497",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U9xRxd6QEA8yUDpoz6y5QJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 211,
      "cache_read_input_tokens": 22766,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 211,
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

_source line 47 · 2026-05-18T10:44:21.656Z_

<details><summary>↩ Tool result · `toolu_01Wt1N6ESEEaxQf7PSAV2XgB`</summary>

```text
0	Total experiments in registry: 237
1	
2	
3	====================================================================================================
4	  1. OBS_ONLY ε=0.2 (norm02) — Main Paper Results K=10  (28 experiments)
5	====================================================================================================
6	
7	  exp_id: eval-acr-object-obs-only-default
8	    status=DONE  server=bjb1-32546  seed=42
9	    n_rollouts=10  total_rollouts=None  SR=N/A
10	    conclusion=success
11	    files: ['logs/eval_object_obs_only_default_norm.json', '~/runs/acr-vla-conformal-refinement/eval-acr-object-obs-only-default.log']
12	    cmd: python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval...
13	    hypothesis: obs_only CRM v3-norm with DEFAULT max_correction_norm (~1.42, no magnitude control) on LIBERO object benchmark. Paired with eval-acr-object-v4-default
14	
15	  exp_id: eval-acr-spatial-v4-obs-only
16	    status=DONE  server=bjb2-40593  seed=42
17	    n_rollouts=10  total_rollouts=None  SR=N/A
18	    conclusion=failed
19	    files: ['/root/autodl-tmp/logs/eval-acr-spatial-v4-obs-only.log']
20	    cmd: python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3/obs_only/crm_best.pt
21	    hypothesis: D020: obs_only CRM (val_loss 0.0165, 54% better than perdof 0.0358) with max_correction_norm=0.1. If obs_only >= v4-small (perdof) → Claim 1 needs res
22	
23	  exp_id: eval-mag-obsonly-norm03-b3
24	    status=DONE  server=bjb2-28827  seed=42
25	    n_rollouts=None  total_rollouts=None  SR=N/A
26	    conclusion=killed
27	    files: ['~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm03-b3.log']
28	    cmd: crm_obs_only spatial norm=0.3 (killed)
29	    hypothesis: Retry of eval-mag-obsonly-norm03-b2 (spatial magnitude sweep obs_only norm=0.3). Submitted on bjb2-28827:cuda:2 instead of bjb1-32546:cuda:3 (cuda:3 o
30	
31	  exp_id: eval-mag-obsonly-norm03-b4
32	    status=DONE  server=bjb2-28827  seed=42
33	    n_rollouts=None  total_rollouts=None  SR=N/A
34	    conclusion=killed
35	    files: ['~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm03-b4.log']
36	    cmd: crm_obs_only spatial norm=0.3 (killed)
37	
38	  exp_id: eval-obs-only-spatial
39	    status=DONE  server=bjb1-18228  seed=42
40	    n_rollouts=10  total_rollouts=None  SR=N/A
41	    conclusion=failed
42	    files: ['~/runs/acr-vla-conformal-refinement/eval-obs-only-spatial.log']
43	    cmd: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/eva...
44	    hypothesis: Obs-only CRM trained on object benchmark generalizes to LIBERO-Spatial tasks without retraining — testing cross-benchmark transfer of visual correctio
45	
46	  exp_id: eval-obs-only-spatial-v2
47	    status=DONE  server=bjb1-18228  seed=42
48	    n_rollouts=10  total_rollouts=None  SR=N/A
49	    conclusion=failed
50	    files: ['~/runs/acr-vla-conformal-refinement/eval-obs-only-spatial-v2.log']
51	    cmd: python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v2/obs_only/crm_best.pt
52	    hypothesis: Obs-only CRM v2 retrained on spatial data resolves the dimension mismatch from v1 and achieves meaningful improvement on LIBERO-Spatial by using bench
53	
54	  exp_id: eval-obs-only-spatial-v3
55	    status=DONE  server=bjb1-18228  seed=42
56	    n_rollouts=10  total_rollouts=None  SR=N/A
57	    conclusion=killed
58	    files: ['~/runs/acr-vla-conformal-refinement/eval-obs-only-spatial-v3.log']
59	    cmd: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/eva...
60	
61	  exp_id: eval-acr-object-obs-only-norm02
62	    status=DONE  server=bjb1-32546  seed=42  ε=0.2
63	    n_rollouts=10  total_rollouts=100  SR=N/A
64	    conclusion=success
65	    files: ['~/runs/acr-vla-conformal-refinement/eval-acr-object-obs-only-norm02.log', 'logs/eval_object_obs_only_norm02.json']
66	    cmd: python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0...
67	    hypothesis: ACR with obs-only CRM and max_correction_norm=0.2 on LIBERO-Object achieves meaningful improvement over VLA-only baseline by applying visually-guided 
68	
69	  exp_id: eval-obs-only-object-norm02-k20-seed42
70	    status=DONE  server=bjb1-18228  seed=42  ε=0.2
71	    n_rollouts=10  total_rollouts=None  SR=N/A
72	    conclusion=killed
73	    files: ['logs/eval_object_obs_only_norm02_k20_seed42.json']
74	    cmd: CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt ...
75	    hypothesis: obs_only CRM (ε=0.2, K=20) seed42 on LIBERO-Object. K sweep 实验：K=20 vs K=10 (22%) 比较，验证增加 candidate 数量是否带来额外增益。若 K=20 ≈ K=10，说明 K=10 已接近饱和。
76	
77	  exp_id: eval-obs-only-object-norm02-k5-seed42
78	    status=DONE  server=bjb1-18228  seed=42  ε=0.2
79	    n_rollouts=10  total_rollouts=None  SR=0.14
80	    conclusion=success
81	    files: ['logs/eval_object_obs_only_norm02_k5_seed42.json']
82	    cmd: CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 5 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt -...
83	    hypothesis: obs_only CRM (ε=0.2, K=5) seed42 on LIBERO-Object. K sweep 实验：K=5 vs K=10 (22%) 比较，验证 sample count 对 selection quality 的影响。若 K=5 显著低于 K=10，说明足够的 candi
84	
85	  exp_id: eval-obs-only-object-norm02-k5-seed43
86	    status=RUNNING  server=bjb2-28827  seed=43  ε=0.2
87	    n_rollouts=10  total_rollouts=None  SR=N/A
88	    conclusion=None
89	    files: ['logs/eval_object_obs_only_norm02_k5_seed43.json', '~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-k5-seed43.log']
90	    cmd: cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 43 --K 5 --crm_checkpoint /root/autodl-tmp/check...
91	    hypothesis: obs_only CRM K=5 ε=0.2 seed43. Second seed for K-value curve (seed42=14%). Director highest priority.
92	
93	  exp_id: eval-obs-only-object-norm02-seed43
94	    status=DONE  server=bjb1-32546  seed=43  ε=0.2
95	    n_rollouts=10  total_rollouts=None  SR=N/A
96	    conclusion=failed
97	    files: ['logs/eval_object_obs_only_norm02_seed43.json']
98	    cmd: CUDA_VISIBLE_DEVICES=3 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed ...
99	    hypothesis: D031: obs_only CRM v3-norm norm=0.2 seed=43 on LIBERO object benchmark. norm=0.2 shows strongest signal (18% SR at 5/10 tasks in seed=42). Seed=43 dou
100	
101	  exp_id: eval-obs-only-object-norm02-seed43-r2
102	    status=DONE  server=None  seed=43  ε=0.2
103	    n_rollouts=None  total_rollouts=None  SR=N/A
104	    conclusion=success
105	    files: ['~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-seed43-r2.log']
106	    hypothesis: D031: obs_only CRM v3-norm norm=0.2 seed=43 on LIBERO object benchmark (r2 retry). P0 critical for statistical significance — seed42=22%, need seed43 
107	
108	  exp_id: eval-obs-only-object-default-seed44
109	    status=DONE  server=bjb1-32546  seed=44
110	    n_rollouts=10  total_rollouts=None  SR=N/A
111	    conclusion=success
112	    files: ['logs/eval_object_obs_only_default_seed44.json"', '~/runs/acr-vla-conformal-refinement/eval-obs-only-object-default-seed44.log']
113	    cmd: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MU...
114	    hypothesis: obs_only CRM (default norm ~1.42) seed=44 on LIBERO Object. 验证 obs_only 在 uncapped norm 下的跨 seed 稳定性（seed42=17%）。如果维持 15-20%，确认极端 magnitude 鲁棒性。
115	
116	  exp_id: eval-obs-only-object-norm03-seed44
117	    status=DONE  server=None  seed=44
118	    n_rollouts=10  total_rollouts=100  SR=N/A
119	    conclusion=success
120	    hypothesis: obs_only CRM v3-norm at norm=0.3 seed=44 on LIBERO object benchmark. Multi-seed magnitude curve coverage. seed42 norm=0.3 object still running on bjb2
121	
122	  exp_id: eval-obs-only-object-norm02-k5-seed44
123	    status=PREPARING  server=None  seed=44  ε=0.2
124	    n_rollouts=None  total_rollouts=None  SR=N/A
125	    conclusion=None
126	    hypothesis: obs_only CRM K=5 ε=0.2 seed44. Third seed for K-value curve (seed42=14%, seed43 RUNNING). Strengthens K=5 data point statistics.
127	
128	  exp_id: eval-obs-only-object-norm02-seed44
129	    status=DONE  server=None  seed=44  ε=0.2
130	    n_rollouts=10  total_rollouts=None  SR=N/A
131	    conclusion=failed
132	    hypothesis: D035 follow-up: obs_only CRM v3-norm norm=0.2 seed=44 on LIBERO object benchmark. Third seed for Fisher exact test. ε=0.2 is PROJECT HIGH config (seed
133	
134	  exp_id: eval-obs-only-object-norm02-seed44-r2
135	    status=DONE  server=bjb1-18228  seed=44  ε=0.2
136	    n_rollouts=10  total_rollouts=None  SR=N/A
137	    conclusion=success
138	    files: ['logs/eval_object_obs_only_norm02_seed44.json']
139	    cmd: source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --see...
140	    hypothesis: Retry of eval-obs-only-object-norm02-seed44 (EXIT_CODE=127, missing conda activate). obs_only CRM norm=0.2 seed=44 on LIBERO object. Third seed for Fi
141	
142	  exp_id: eval-obs-only-object-norm02-seed44-r3
143	    status=DONE  server=bjb1-18228  seed=44  ε=0.2
144	    n_rollouts=10  total_rollouts=None  SR=N/A
145	    conclusion=killed
146	    files: ['logs/eval_object_obs_only_norm02_seed44.json"', '~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-seed44-r3.log']
147	    cmd: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MU...
148	    hypothesis: Retry of eval-obs-only-object-norm02-seed44 (r1 EXIT_CODE=127, r2 killed by agent). obs_only CRM norm=0.2 seed=44 on LIBERO object. Third seed for Fis
149	
150	  exp_id: eval-obs-only-object-norm02-seed44-r4
151	    status=DONE  server=bjb1-18228  seed=44  ε=0.2
152	    n_rollouts=10  total_rollouts=None  SR=N/A
153	    conclusion=killed
154	    files: ['logs/eval_object_obs_only_norm02_seed44_r4.json"', '~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-seed44-r4.log']
155	    cmd: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MU...
156	    hypothesis: P0 retry #4: obs_only CRM v3-norm norm=0.2 seed=44 on LIBERO object. Third seed for Fisher test. seed42=22%, seed43=16%. Previous attempts failed (127
157	
158	  exp_id: eval-obs-only-object-default-seed45
159	    status=DONE  server=bjb2-28827  seed=45
160	    n_rollouts=None  total_rollouts=200  SR=0.12
161	    conclusion=success *** total_rollouts=200 ***
162	    files: ['logs/eval_object_obs_only_default_seed45.json']
163	    cmd: python src/evaluate.py --mode crm_obs_only --K 10 --seed 45 --benchmark object --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_de...
164	    hypothesis: obs_only CRM (default norm ~1.42, 无裁剪) seed=45 on LIBERO Object. 验证 obs_only 在 uncapped 大 norm 下仍优于 VLA-only（seed42 在 default 为 17%）。极端 magnitude 鲁棒性测
165	
166	  exp_id: eval-obs-only-object-norm02-seed45
167	    status=DONE  server=bjb1-32546  seed=45  ε=0.2
168	    n_rollouts=10  total_rollouts=100  SR=N/A
169	    conclusion=success
170	    files: ['~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-seed45.log', 'logs/eval_object_obs_only_norm02_seed45.json']
171	    cmd: python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0...
172	    hypothesis: obs_only CRM (ε=0.2) seed=45 on LIBERO object: if obs_only maintains 16-22% SR range consistent with seeds 42-44, it confirms the method's reliability
173	
174	  exp_id: eval-obs-only-object-default-seed46
175	    status=DONE  server=bjb1-32546  seed=46
176	    n_rollouts=10  total_rollouts=None  SR=N/A
177	    conclusion=success
178	    files: ['/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed46.json', 'logs/eval_object_obs_only_default_seed46.json']
179	    cmd: CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt ...
180	    hypothesis: obs_only CRM without norm constraint (uncapped correction magnitude) on LIBERO-Object seed46. Tests whether obs_only maintains performance without exp
181	
182	  exp_id: eval-obs-only-object-norm02-seed46
183	    status=DONE  server=bjb1-18228  seed=46  ε=0.2
184	    n_rollouts=10  total_rollouts=None  SR=0.15
185	    conclusion=success
186	    files: ['logs/eval_object_obs_only_norm02_seed46.log', 'logs/eval_object_obs_only_norm02_seed46.json']
187	    cmd: cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode crm_obs_only -...
188	    hypothesis: obs_only CRM ε=0.2 seed46 on LIBERO-Object. Pooled Fisher test 最关键的缺失配对数据（与 argmin seed46=10% 配对）。ε=0.2 是 obs_only 最优区间，seed42=22%。
189	
190	  exp_id: eval-obs-only-object-norm02-seed47
191	    status=DONE  server=bjb1-32546  seed=47  ε=0.2
192	    n_rollouts=10  total_rollouts=None  SR=0.2
193	    conclusion=success
194	    files: ['logs/eval_object_obs_only_norm02_seed47.json"', '~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-seed47.log']
195	    cmd: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MU...
196	    hypothesis: obs_only CRM (ε=0.2) seed=47 on LIBERO object benchmark. Extends multi-seed comparison to 6 seeds. If consistent with seeds 42-44 (16-22%), strengthen
197	
198	  exp_id: eval-obs-only-object-norm02-seed48
199	    status=DONE  server=bjb1-18228  seed=48  ε=0.2
200	    n_rollouts=10  total_rollouts=None  SR=N/A
201	    conclusion=killed
202	    files: ['logs/eval_object_obs_only_norm02_seed48.json', '~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-seed48.log']
203	    cmd: cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 48 --K 10 --crm_checkpoint ...
204	    hypothesis: obs_only CRM ε=0.2 seed48. Key data point at primary comparison norm.
205	
206	  exp_id: eval-obs-only-object-norm02-seed48-r2
207	    status=RUNNING  server=bjb1-18228  seed=48  ε=0.2
208	    n_rollouts=None  total_rollouts=None  SR=N/A
209	    conclusion=None
210	    cmd: crm_obs_only --seed 48 --K 10 --max_correction_norm 0.2
211	    hypothesis: obs_only CRM (ε=0.2) seed48 on LIBERO-Object. Retry after killed previous attempt. Supplements primary result (seed42-47 done, this extends to seed48)
212	
213	  exp_id: eval-mag-obsonly-norm-0.3-r3
214	    status=DONE  server=bjb1-18228  seed=0
215	    n_rollouts=None  total_rollouts=None  SR=N/A
216	    conclusion=killed
217	    cmd: N/A (stale duplicate entry)
218	    hypothesis: Magnitude sweep: obs_only CRM v3-norm at max_correction_norm=0.3 on spatial. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade at sam
219	
220	====================================================================================================
221	  2. ARGMIN BASELINE  (9 experiments)
222	====================================================================================================
223	
224	  exp_id: eval-argmin-only-spatial
225	    status=DONE  server=bjb1-18228  seed=42
226	    n_rollouts=10  total_rollouts=None  SR=N/A
227	    conclusion=killed
228	    files: ['~/runs/acr-vla-conformal-refinement/eval-argmin-only-spatial.log']
229	    cmd: python -u src/evaluate.py --mode reconvla --benchmark spatial --n_rollouts 10 --seed 42 --K 10
230	    hypothesis: Argmin-only selection (K=10, pick lowest CRM score without correction) on LIBERO-Spatial tests whether selection alone provides benefit — isolating th
231	
232	  exp_id: eval-argmin-only-spatial-r2
233	    status=DONE  server=bjb1-18228  seed=42
234	    n_rollouts=10  total_rollouts=None  SR=0.34
235	    conclusion=success
236	    files: ['~/runs/acr-vla-conformal-refinement/eval-argmin-only-spatial-r2.log']
237	    cmd: python -u src/evaluate.py --mode reconvla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --start_task 9
238	    hypothesis: Restart from T9. ReconVLA baseline (scalar Euclidean argmin, K=10) on spatial. Isolate argmin base action selection from CRM correction.
239	
240	  exp_id: eval-argmin-object-seed43
241	    status=DONE  server=bjb1-18228  seed=43
242	    n_rollouts=10  total_rollouts=None  SR=0.17
243	    conclusion=success
244	    files: ['logs/eval_object_reconvla_seed43.json', '~/runs/acr-vla-conformal-refinement/eval-argmin-object-seed43.log']
245	    cmd: python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 43 --K 10 --output_file logs/eval_object_reconvla_seed43.json
246	    hypothesis: D031: argmin baseline (K=10, scalar Euclidean argmin) seed=43 on LIBERO object benchmark. Paired with eval-obs-only-object-seed43 for Fisher exact tes
247	
248	  exp_id: eval-argmin-object-seed44
249	    status=DONE  server=None  seed=44
250	    n_rollouts=10  total_rollouts=None  SR=N/A
251	    conclusion=failed
252	    hypothesis: D035 follow-up: argmin baseline (K=10) seed=44 on LIBERO object benchmark. Third seed for Fisher exact test statistical power. Paired with eval-obs-on
253	
254	  exp_id: eval-argmin-object-seed44-r2
255	    status=DONE  server=bjb1-18228  seed=44
256	    n_rollouts=10  total_rollouts=None  SR=N/A
257	    conclusion=success
258	    files: ['logs/eval_object_reconvla_seed44.json']
259	    cmd: source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 44...
260	    hypothesis: Retry of eval-argmin-object-seed44 (EXIT_CODE=127, missing conda activate). argmin baseline K=10 seed=44 on LIBERO object. Third seed for Fisher test.
261	
262	  exp_id: eval-argmin-object-seed44-r3
263	    status=DONE  server=bjb1-18228  seed=44
264	    n_rollouts=10  total_rollouts=None  SR=N/A
265	    conclusion=killed
266	    files: ['logs/eval_object_reconvla_seed44.json"', '~/runs/acr-vla-conformal-refinement/eval-argmin-object-seed44-r3.log']
267	    cmd: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MU...
268	    hypothesis: Retry of eval-argmin-object-seed44 (r1 EXIT_CODE=127, r2 killed by agent). argmin baseline K=10 seed=44 on LIBERO object. Third seed for Fisher test. 
269	
270	  exp_id: eval-argmin-object-seed45
271	    status=DONE  server=bjb2-28827  seed=45
272	    n_rollouts=10  total_rollouts=100  SR=N/A
273	    conclusion=success
274	    files: ['logs/eval_object_argmin_seed45.json', '~/runs/acr-vla-conformal-refinement/eval-argmin-object-seed45.log']
275	    cmd: python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 45 --K 10 --output_file logs/eval_object_argmin_seed45.json
276	    hypothesis: Argmin baseline (conformal selection K=10, no correction) seed=45 on LIBERO Object. Highest priority: expands argmin multi-seed data from 3 to 4 seeds
277	
278	  exp_id: eval-argmin-object-seed46
279	    status=DONE  server=bjb1-32546  seed=46
280	    n_rollouts=10  total_rollouts=100  SR=N/A
281	    conclusion=success
282	    files: ['logs/eval_object_reconvla_seed46.json', 'logs/eval_argmin_object_seed46.log']
283	    cmd: python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 46 --K 10 --output_file logs/eval_object_reconvla_seed46.json
284	    hypothesis: Argmin baseline (conformal selection K=10, 无 learned correction) seed=46 on LIBERO Object. 与 obs_only seed=46 配对，扩展 pooled Fisher test 到 6 seeds。预期 12
285	
286	  exp_id: eval-argmin-object-seed47
287	    status=DONE  server=bjb1-32546  seed=47
288	    n_rollouts=10  total_rollouts=100  SR=N/A
289	    conclusion=success
290	    files: ['logs/eval_object_reconvla_seed47.json', '~/runs/acr-vla-conformal-refinement/eval-argmin-object-seed47.log']
291	    cmd: python -u src/evaluate.py --mode reconvla --seed 47 --benchmark object --n_rollouts 10 --output_file logs/eval_object_reconvla_seed47.json
292	    hypothesis: Argmin baseline (reconvla K=10) seed=47 on LIBERO object benchmark. Paired with obs_only seed47 on cuda:0 for direct comparison. Extends argmin multi-
293	
294	====================================================================================================
295	  3. VLA-ONLY BASELINE  (25 experiments)
296	====================================================================================================
297	
298	  exp_id: eval-object-v4-full
299	    status=DONE  server=bjb2-40593  seed=42
300	    n_rollouts=10  total_rollouts=None  SR=N/A
301	    conclusion=killed
302	    files: ['~/runs/acr-vla-conformal-refinement/eval-object-v4-full.log']
303	    cmd: python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 42
304	
305	  exp_id: eval-object-v5-full
306	    status=DONE  server=bjb2-40593  seed=42
307	    n_rollouts=10  total_rollouts=None  SR=N/A
308	    conclusion=killed
309	    files: ['/root/acr-vla-conformal-refinement/logs/eval-object-v5-full.log']
310	    cmd: CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 42 --smolvla_path /root/autodl-tmp/models/smolvla_libero...
311	
312	  exp_id: eval-object-v7-full
313	    status=DONE  server=bjb2-40593  seed=42
314	    n_rollouts=10  total_rollouts=None  SR=N/A
315	    conclusion=killed
316	    files: ['/root/autodl-tmp/eval_results/eval-object-v6.log']
317	    cmd: CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 42
318	
319	  exp_id: eval-object-v8-full
320	    status=DONE  server=bjb2-40593  seed=42
321	    n_rollouts=10  total_rollouts=100  SR=0.13
322	    conclusion=success
323	    files: ['/root/autodl-tmp/eval_results/eval-object-v6.log']
324	    cmd: CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 42
325	    hypothesis: Full ACR pipeline v8 (obs-only CRM, K=10 conformal selection, norm=0.1) on LIBERO-Object achieves consistent improvement over VLA-only baseline (9-12%
326	
327	  exp_id: eval-openvla-object-vla-only-seed42
328	    status=DONE  server=bjb1-18228  seed=42
329	    n_rollouts=10  total_rollouts=100  SR=0
330	    conclusion=negative
331	    files: ['~/runs/acr-vla-conformal-refinement/eval-openvla-object-vla-only-seed42.log']
332	    cmd: python -u src/openvla_eval.py --mode vla_only --benchmark object --n_rollouts 10 --seed 42 --K 1 --gpu 0 --model_path /root/autodl-tmp/models/openvla-libero-object
333	    hypothesis: OpenVLA 7B VLA-only baseline on LIBERO-Object. 0% SR due to transformers 5.8 DynamicCache bug. Fix: use official repo eval code with transformers 4.40
334	
335	  exp_id: eval-openvla-object-vla-only-seed42-v2
336	    status=DONE  server=bjb1-18228  seed=42
337	    n_rollouts=100  total_rollouts=100  SR=N/A
338	    conclusion=success
339	    files: ['/root/acr-vla-conformal-refinement/results/eval-openvla-object-vla-only-seed42-v2']
340	    cmd: bash -c "source /root/autodl-tmp/conda_envs/openvla/bin/activate && cd /root/autodl-tmp/openvla && MUJOCO_GL=egl python experiments/robot/libero/run_libero_eval.py --model_family openvla --pretrained_...
341	    hypothesis: OpenVLA 7B finetuned VLA-only baseline on LIBERO-Object using official eval code (transformers 4.40.1, isolated conda env). v1 failed due to transform
342	
343	  exp_id: eval-smolvla-libero-spatial
344	    status=DONE  server=autodl-4090x4  seed=42
345	    n_rollouts=3  total_rollouts=None  SR=N/A
346	    conclusion=failed
347	    files: ['/tmp/eval_spatial_full.log']
348	    cmd: python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 3 --seed 42
349	    hypothesis: SmolVLA pretrained model evaluates directly on LIBERO-Spatial without any CRM or conformal processing — establishing raw VLA capability as absolute fl
350	
351	  exp_id: eval-spatial-reeval-v2
352	    status=DONE  server=autodl-4090x4  seed=42
353	    n_rollouts=3  total_rollouts=None  SR=N/A
354	    conclusion=killed
355	    files: ['/tmp/eval_spatial.log']
356	    cmd: python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 3 --seed 42 --smolvla_path /root/autodl-tmp/models/smolvla_libero/
357	
358	  exp_id: eval-spatial-v3-full
359	    status=DONE  server=bjb1-18228  seed=42
360	    n_rollouts=10  total_rollouts=None  SR=N/A
361	    conclusion=killed
362	    files: ['~/runs/acr-vla-conformal-refinement/eval-spatial-v3-full.log']
363	    cmd: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl && python -u src...
364	
365	  exp_id: eval-spatial-v4-full
366	    status=DONE  server=bjb1-18228  seed=42
367	    n_rollouts=10  total_rollouts=None  SR=N/A
368	    conclusion=killed
369	    files: ['~/runs/acr-vla-conformal-refinement/eval-spatial-v4-full.log']
370	    cmd: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl && python -u src...
371	
372	  exp_id: eval-spatial-v5-full
373	    status=DONE  server=bjb1-18228  seed=42
374	    n_rollouts=10  total_rollouts=None  SR=N/A
375	    conclusion=killed
376	    files: ['~/runs/acr-vla-conformal-refinement/eval-spatial-v5-full.log']
377	    cmd: python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 10 --seed 42
378	
379	  exp_id: eval-spatial-v6-full
380	    status=DONE  server=bjb1-18228  seed=42
381	    n_rollouts=10  total_rollouts=None  SR=N/A
382	    conclusion=killed
383	    files: ['/root/autodl-tmp/eval_results/eval-spatial-v6-full.log']
384	    cmd: CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 10 --seed 42
385	
386	  exp_id: eval-spatial-v7-full
387	    status=DONE  server=bjb1-18228  seed=42
388	    n_rollouts=10  total_rollouts=None  SR=0.3
389	    conclusion=success
390	    files: ['/root/autodl-tmp/eval_results/eval-spatial-v7.log']
391	    cmd: CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 10 --seed 42
392	    hypothesis: Full ACR pipeline v7 (obs-only CRM, conformal selection, norm=0.1) on LIBERO-Spatial achieves improvement over VLA-only baseline (32%), validating the
393	
394	  exp_id: eval-vla-mean-object
395	    status=DONE  server=bjb1-32546  seed=42
396	    n_rollouts=10  total_rollouts=100  SR=N/A
397	    conclusion=success
398	    files: ['/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean.log']
399	    cmd: python eval_vla.py --benchmark object --mode vla_only --baseline_mode mean --n_rollouts 10 --K 10 --seed 42
400	    hypothesis: VLA mean baseline (K=10, mean aggregation) on LIBERO object benchmark. Matches reconvla spatial baseline but on object tasks.
401	
402	  exp_id: eval-vla-mean-spatial
403	    status=DONE  server=bjb2-40593  seed=42
404	    n_rollouts=10  total_rollouts=None  SR=N/A
405	    conclusion=success
406	    files: ['/root/autodl-tmp/eval_results/eval-vla-mean-spatial.log']
407	    cmd: CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode vla_only --baseline_mode mean --benchmark spatial --n_rollouts 10 --seed 42
408	    hypothesis: VLA mean action (average of K=10 samples) on LIBERO-Spatial provides a strong baseline by reducing sampling noise — establishes whether sample averagi
409	
410	  exp_id: eval-vla-mean-spatial-t10
411	    status=DONE  server=bjb2-40593  seed=42
412	    n_rollouts=10  total_rollouts=None  SR=N/A
413	    conclusion=success
414	    files: ['/root/autodl-tmp/eval_results/eval-vla-mean-spatial-t10.json']
415	    cmd: python -u src/evaluate.py --mode vla_only --baseline_mode mean --benchmark spatial --n_rollouts 10 --seed 42 --start_task 9 --output_file /root/autodl-tmp/eval_results/eval-vla-mean-spatial-t10.json
416	    hypothesis: VLA mean action on LIBERO-Spatial task 10 (wooden shelf) specifically — completing the last missing task from the earlier eval-vla-mean-spatial run to
417	
418	  exp_id: eval-vla-only-object
419	    status=DONE  server=bjb1-32546  seed=42
420	    n_rollouts=10  total_rollouts=None  SR=N/A
421	    conclusion=success
422	    files: ['/root/acr-vla-conformal-refinement/logs/eval_object_vla_only.log', 'logs/eval_object_vla_only.json']
423	    cmd: python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode single --n_rollouts 10 --K 1 --output_file logs/eval_object_vla_only.json
424	    hypothesis: VLA-only baseline (K=1, no mean, no CRM) on LIBERO object benchmark. Single sample from flow-matching VLA.
425	
426	  exp_id: eval-vla-only-object-k1
427	    status=DONE  server=bjb1-32546  seed=42
428	    n_rollouts=10  total_rollouts=None  SR=N/A
429	    conclusion=failed
430	    files: ['logs/eval_object_vla_only_k1.json"', '~/runs/acr-vla-conformal-refinement/eval-vla-only-object-k1.log']
431	    cmd: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MU...
432	    hypothesis: VLA-only baseline (K=1, single sample, no CRM) on LIBERO object benchmark. Lowest-bar baseline for object domain.
433	
434	  exp_id: eval-vla-mean-object-seed43
435	    status=DONE  server=bjb1-32546  seed=43
436	    n_rollouts=10  total_rollouts=100  SR=N/A
437	    conclusion=success
438	    files: ['logs/eval_object_vla_mean_seed43.json', '~/runs/acr-vla-conformal-refinement/eval-vla-mean-object-seed43.log']
439	    cmd: python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode mean --n_rollouts 10 --K 10 --seed 43 --output_file logs/eval_object_vla_mean_seed43.json
440	    hypothesis: D031: VLA-mean baseline (K=10, mean aggregation) seed=43 on LIBERO object benchmark. Completes seed=43 comparison table. If VLA-mean seed=43 ≈ obs_onl
441	
442	  exp_id: eval-vla-only-object-seed43
443	    status=DONE  server=bjb1-32546  seed=43
444	    n_rollouts=10  total_rollouts=None  SR=N/A
445	    conclusion=success
446	    files: ['logs/eval_object_vla_only_seed43.json']
447	    cmd: CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 43 -...
448	    hypothesis: VLA-only baseline on LIBERO-Object seed=43 establishes multi-seed baseline variance — needed to determine if ACR improvements are statistically signif
449	
450	  exp_id: eval-vla-mean-object-seed44
451	    status=DONE  server=bjb1-32546  seed=44
452	    n_rollouts=10  total_rollouts=None  SR=N/A
453	    conclusion=success
454	    files: ['~/runs/acr-vla-conformal-refinement/eval-vla-mean-object-seed44.log', 'logs/eval_object_vla_mean_seed44.json"']
455	    cmd: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MU...
456	    hypothesis: VLA-mean baseline (K=10, mean aggregation) seed=44 on LIBERO object benchmark. Completes seed=44 six-way comparison. seed42=12%, seed43=15%.
457	
458	  exp_id: eval-vla-only-object-seed44
459	    status=DONE  server=None  seed=44
460	    n_rollouts=10  total_rollouts=None  SR=N/A
461	    conclusion=failed
462	    hypothesis: D035 follow-up: VLA-only baseline (K=1) seed=44 on LIBERO object benchmark. Third seed reference point. seed42=12%, seed43=12%. Deployed on bjb2-40593
463	
464	  exp_id: eval-vla-only-object-seed44-r2
465	    status=DONE  server=bjb2-40593  seed=44
466	    n_rollouts=10  total_rollouts=None  SR=N/A
467	    conclusion=success
468	    files: ['logs/eval_object_vla_only_seed44.json"', '~/runs/acr-vla-conformal-refinement/eval-vla-only-object-seed44-r2.log']
469	    cmd: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MU...
470	    hypothesis: Retry of eval-vla-only-object-seed44 (r1 EXIT_CODE=127). VLA-only baseline K=1 seed=44 on LIBERO object. Third seed reference. seed42=12%, seed43=12%.
471	
472	  exp_id: eval-vla-mean-object-seed45
473	    status=DONE  server=bjb2-28827  seed=45
474	    n_rollouts=10  total_rollouts=100  SR=N/A
475	    conclusion=success
476	    files: ['logs/eval_object_vla_mean_seed45.json"', '~/runs/acr-vla-conformal-refinement/eval-vla-mean-object-seed45.log']
477	    cmd: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MU...
478	    hypothesis: VLA-mean baseline (K=10, mean aggregation) seed=45 on LIBERO object benchmark. Completes seed=45 six-way comparison. seed42=12%, seed43=15%, seed44=ru
479	
480	  exp_id: eval-vla-only-object-seed45
481	    status=DONE  server=bjb2-28827  seed=45
482	    n_rollouts=None  total_rollouts=None  SR=N/A
483	    conclusion=success
484	    files: ['logs/eval_object_vla_only_seed45.json']
485	    cmd: CUDA_VISIBLE_DEVICES=4 python src/evaluate.py --benchmark object --mode vla_only --K 1 --seed 45 --output_file logs/eval_object_vla_only_seed45.json
486	    hypothesis: VLA-only baseline on LIBERO-Object seed=45 provides second additional seed for baseline variance estimation — multi-seed baselines required for statis
487	
488	====================================================================================================
489	  4. MAGNITUDE CURVE OBS_ONLY — Various ε  (43 experiments)
490	====================================================================================================
491	
492	  exp_id: eval-mag-obsonly-norm003
493	    status=DONE  server=bjb2-40593  seed=42  ε=0.03
494	    n_rollouts=10  total_rollouts=None  SR=N/A
495	    conclusion=killed
496	    files: ['~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm003-b2.log', 'logs/eval_mag_obsonly_norm003.json']
497	    cmd: python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --max_correction_norm 0.03 --n_rollouts 10 --K 10 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ --crm_checkpoint /root/autodl...
498	    hypothesis: Magnitude sweep: obs_only CRM v3-norm at norm=0.03 on spatial. Completes obs_only norm curve (have 0.05, 0.2; adding 0.03).
499	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LkyHAJXMgM6jYEjtYbJhsT",
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "04570627-b04f-45d6-ab0b-0e29f39b3dd8"
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
  "task_id": "a5dc54df06c763762",
  "tool_use_id": "toolu_01LkyHAJXMgM6jYEjtYbJhsT",
  "description": "Reading ~/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/c1bdccab-16c6-497c-9d30-0feab97d927d/tool-results/bkoeg1h8a.txt",
  "usage": {
    "total_tokens": 23138,
    "tool_uses": 6,
    "duration_ms": 64219
  },
  "last_tool_name": "Read",
  "uuid": "e03d674f-5d3a-45a9-b243-dba402dab5a8",
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d"
}
```

---


### Tool call

_source line 49_

<details open><summary>🔧 Tool call — Read · `toolu_01Vhf7o9G5642Zf1XEuTTN7Q`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/c1bdccab-16c6-497c-9d30-0feab97d927d/tool-results/bkoeg1h8a.txt",
  "limit": 500,
  "offset": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LkyHAJXMgM6jYEjtYbJhsT",
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "e027263d-dcc3-47c8-95c3-42d75c76a749",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U9xRxd6QEA8yUDpoz6y5QJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 211,
      "cache_read_input_tokens": 22766,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 211,
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

_source line 50 · 2026-05-18T10:44:22.750Z_

<details><summary>↩ Tool result · `toolu_01Vhf7o9G5642Zf1XEuTTN7Q`</summary>

```text
500	
501	  exp_id: eval-mag-obsonly-norm003-b2
502	    status=DONE  server=bjb2-40593  seed=42  ε=0.03
503	    n_rollouts=10  total_rollouts=None  SR=N/A
504	    conclusion=success
505	    files: ['~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm003-b2.log', 'logs/eval_mag_obsonly_norm003.json']
506	    cmd: python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm ...
507	    hypothesis: obs_only CRM (ε=0.03) on LIBERO Spatial benchmark. 极低 norm 下 obs_only 在 spatial 的表现（10-task SR）。验证 magnitude 效应在不同 benchmark 上的一致性。
508	
509	  exp_id: eval-mag-obsonly-norm003-object
510	    status=DONE  server=bjb1-32546  seed=42  ε=0.03
511	    n_rollouts=10  total_rollouts=None  SR=N/A
512	    conclusion=success
513	    files: ['logs/eval_object_obs_only_norm003.json"', '~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm003-object.log']
514	    cmd: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts...
515	    hypothesis: Object magnitude sweep: obs_only CRM v3-norm at norm=0.03 on LIBERO object benchmark. Completes 5-point magnitude curve (0.03/0.05/0.1/0.2/0.3). Tests
516	
517	  exp_id: eval-mag-obsonly-norm005
518	    status=DONE  server=bjb2-28827  seed=42  ε=0.05
519	    n_rollouts=10  total_rollouts=None  SR=N/A
520	    conclusion=success
521	    files: ['logs/eval_mag_obs_only_norm005.json']
522	    cmd: python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --max_correction_norm 0.05 --n_rollouts 10 --K 10 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ --crm_checkpoint /root/autodl...
523	    hypothesis: obs_only CRM (ε=0.05) on LIBERO Spatial benchmark. 低 norm 在 spatial 上的表现。与 object 的 0.05 数据点对比，检验 benchmark 间一致性。
524	
525	  exp_id: eval-mag-obsonly-norm005-object
526	    status=DONE  server=bjb2-28827  seed=42  ε=0.05
527	    n_rollouts=10  total_rollouts=100  SR=N/A
528	    conclusion=success
529	    files: ['logs/eval_object_obs_only_norm005.json', '/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005.log']
530	    cmd: CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt ...
531	    hypothesis: obs_only CRM (ε=0.05) on LIBERO Object magnitude sweep seed=42. 验证极低 norm 下 obs_only 表现。如果 SR 与 VLA-only 相近（12%），说明过低 norm 约束了 CRM 纠正能力。
532	
533	  exp_id: eval-acr-object-v4-obs-only
534	    status=DONE  server=bjb1-32546  seed=42  ε=0.1
535	    n_rollouts=10  total_rollouts=100  SR=N/A
536	    conclusion=success
537	    files: ['~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-obs-only.log']
538	    cmd: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MU...
539	    hypothesis: D021: obs_only CRM v3-norm with max_correction_norm=0.1 on LIBERO object benchmark. Cross-benchmark validation — obs-only leads spatial at 57.5%.
540	
541	  exp_id: eval-acr-object-v4-obs-only-b2
542	    status=DONE  server=bjb2-28827  seed=42  ε=0.1
543	    n_rollouts=10  total_rollouts=None  SR=N/A
544	    conclusion=killed
545	    files: ['~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-obs-only-b2.log']
546	    cmd: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MU...
547	
548	  exp_id: eval-acr-spatial-v4-obs-only-r2
549	    status=DONE  server=bjb1-18228  seed=42  ε=0.1
550	    n_rollouts=10  total_rollouts=None  SR=N/A
551	    conclusion=killed
552	    files: ['~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-obs-only-r2.log']
553	    cmd: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate....
554	    hypothesis: D020: obs_only CRM v3-norm (val_loss 0.0165) with max_correction_norm=0.1. If obs_only >= v4-small (perdof) → Claim 1 needs restructuring. If obs_only
555	
556	  exp_id: eval-acr-spatial-v4-obs-only-r3
557	    status=DONE  server=bjb1-18228  seed=42  ε=0.1
558	    n_rollouts=10  total_rollouts=100  SR=N/A
559	    conclusion=success
560	    files: ['~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-obs-only-r3.log']
561	    cmd: python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm ...
562	    hypothesis: Restart from T6. obs_only CRM v3-norm with max_correction_norm=0.1 on spatial. If obs_only >= perdof, conformal features need restructuring.
563	
564	  exp_id: eval-obs-only-object-norm01-seed42
565	    status=DEPLOYED  server=bjb2-28827  seed=42  ε=0.1
566	    n_rollouts=10  total_rollouts=None  SR=N/A
567	    conclusion=failed
568	    files: ['logs/eval_object_obs_only_norm01_seed42.json']
569	    cmd: cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint ...
570	    hypothesis: obs_only CRM with ε=0.1 on LIBERO-Object seed42. Intermediate norm point for magnitude curve.
571	
572	  exp_id: eval-obs-only-object-norm01-seed42-r2
573	    status=RUNNING  server=bjb2-28827  seed=42  ε=0.1
574	    n_rollouts=10  total_rollouts=None  SR=N/A
575	    conclusion=None
576	    files: ['logs/eval_object_obs_only_norm01_seed42.json']
577	    cmd: cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint ...
578	    hypothesis: obs_only CRM with max_correction_norm=0.1 on LIBERO-Object seed42. Rerun of failed eval-obs-only-object-norm01-seed42. PID 497445 on cuda:1, started 0
579	
580	  exp_id: eval-mag-obsonly-norm02
581	    status=DONE  server=bjb2-28827  seed=42  ε=0.2
582	    n_rollouts=10  total_rollouts=100  SR=N/A
583	    conclusion=negative
584	    files: ['logs/eval_mag_obs_only_norm02.json']
585	    cmd: python -u src/evaluate.py --benchmark spatial --mode crm_obs_only --max_correction_norm 0.2 --n_rollouts 10 --K 10 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ --crm_checkpoint /root/autodl-...
586	    hypothesis: obs_only CRM (ε=0.2) on LIBERO Spatial benchmark. Spatial benchmark 下 obs_only 最优 norm 是否同样为 0.2。如果 spatial 无明显分离，说明方法效果依赖 action distribution shift 程
587	
588	  exp_id: eval-mag-obsonly-norm02-object
589	    status=DONE  server=bjb2-28827  seed=42  ε=0.2
590	    n_rollouts=10  total_rollouts=None  SR=N/A
591	    conclusion=killed
592	    files: ['logs/eval_object_obs_only_norm02_v2.json', 'N/A']
593	    cmd: CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt ...
594	
595	  exp_id: eval-mag-obsonly-norm-0p3-r3
596	    status=DONE  server=bjb1-18228  seed=42  ε=0.3
597	    n_rollouts=10  total_rollouts=None  SR=N/A
598	    conclusion=killed
599	    files: ['~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm-0p3-r3.log', 'logs/eval_mag_obsonly_norm_0p3.json"']
600	    cmd: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollout...
601	    hypothesis: Magnitude sweep: obs_only CRM v3-norm at max_correction_norm=0.3 on spatial. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't degrade at sam
602	
603	  exp_id: eval-mag-obsonly-norm03
604	    status=DONE  server=bjb1-18228  seed=42  ε=0.3
605	    n_rollouts=10  total_rollouts=None  SR=N/A
606	    conclusion=killed
607	    files: ['logs/eval_mag_obsonly_norm03.json', 'N/A']
608	    cmd: python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm ...
609	    hypothesis: Magnitude sweep: obs_only CRM v3-norm at norm=0.3 on spatial. Fills obs_only norm=0.3 gap. perdof norm=0.3 shows T1 drop to 50% — if obs_only doesn't 
610	
611	  exp_id: eval-mag-obsonly-norm03-b2
612	    status=DONE  server=bjb2-28827  seed=42  ε=0.3
613	    n_rollouts=10  total_rollouts=None  SR=N/A
614	    conclusion=failed
615	    files: ['logs/eval_mag_obsonly_norm03_b2.json"', '~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm03-b2.log']
616	    cmd: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MU...
617	    hypothesis: Magnitude sweep: obs_only CRM v3-norm at norm=0.3 on spatial. Retry of eval-mag-obsonly-norm03 (EXIT_CODE=127). Fills obs_only norm=0.3 gap. perdof no
618	
619	  exp_id: eval-mag-obsonly-norm03-object
620	    status=DONE  server=bjb2-28827  seed=42  ε=0.3
621	    n_rollouts=10  total_rollouts=None  SR=N/A
622	    conclusion=success
623	    files: ['logs/eval_object_obs_only_norm03.json', '/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03.log']
624	    cmd: CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt ...
625	    hypothesis: obs_only CRM (ε=0.3) on LIBERO Object magnitude sweep seed=42. 验证高 norm 下 obs_only 是否仍保持 graceful degradation（对比 perdof 在同 norm 的 collapse）。
626	
627	  exp_id: eval-mag-obsonly-norm03-r2
628	    status=DONE  server=bjb1-18228  seed=42  ε=0.3
629	    n_rollouts=10  total_rollouts=None  SR=N/A
630	    conclusion=success
631	    files: ['logs/eval_mag_obsonly_norm03.json"', '~/runs/acr-vla-conformal-refinement/eval-mag-obsonly-norm03-r2.log']
632	    cmd: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollout...
633	    hypothesis: Retry of eval-mag-obsonly-norm03 (EXIT_CODE=127 fix). Magnitude sweep: obs_only CRM v3-norm at norm=0.3 on spatial. Fills obs_only norm=0.3 gap. perdo
634	
635	  exp_id: eval-obs-only-object-norm003-seed43
636	    status=DONE  server=bjb1-18228  seed=43  ε=0.03
637	    n_rollouts=10  total_rollouts=None  SR=N/A
638	    conclusion=failed
639	    files: ['logs/eval_object_obs_only_norm003_seed43.json', 'logs/eval_object_obs_only_norm003_seed43.log']
640	    cmd: python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0...
641	    hypothesis: obs_only CRM (ε=0.03) seed43 on LIBERO-Object. plan_500 低 norm 补数据：seed42 ε=0.03=16%。多 seed 确认 obs_only 在极低 correction norm 下仍稳定。
642	
643	  exp_id: eval-obs-only-object-norm005-seed43
644	    status=DONE  server=bjb1-18228  seed=43  ε=0.05
645	    n_rollouts=10  total_rollouts=None  SR=N/A
646	    conclusion=killed
647	    files: ['logs/eval-obs-only-object-norm005-seed43.json', 'N/A (killed, superseded by r2/r3)']
648	    cmd: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MU...
649	    hypothesis: obs_only CRM (ε=0.05) seed43 on LIBERO-Object. M006 补救：补充 magnitude curve 低 norm 段多 seed 数据。seed42 ε=0.05=13%。
650	
651	  exp_id: eval-obs-only-object-norm005-seed43-r2
652	    status=DONE  server=bjb1-32546  seed=43  ε=0.05
653	    n_rollouts=10  total_rollouts=None  SR=N/A
654	    conclusion=success
655	    files: ['logs/eval_object_obs_only_norm005_seed43_r2.json', '/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed43_r2.json']
656	    cmd: python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0...
657	    hypothesis: obs_only CRM with ε=0.05 on LIBERO-Object seed43. Retry (r2) for magnitude curve low-norm data point.
658	
659	  exp_id: eval-obs-only-object-norm005-seed43-r3
660	    status=DONE  server=bjb1-18228  seed=43  ε=0.05
661	    n_rollouts=10  total_rollouts=None  SR=N/A
662	    conclusion=killed
663	    files: ['~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm005-seed43-r3.log', 'logs/eval_object_obs_only_norm005_seed43_r2.json']
664	    cmd: python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0...
665	    hypothesis: obs_only CRM (ε=0.05) seed43 on LIBERO-Object. M006 补救重跑。seed42 ε=0.05=13%。
666	
667	  exp_id: eval-obs-only-object-seed43
668	    status=DONE  server=bjb1-18228  seed=43  ε=0.1
669	    n_rollouts=10  total_rollouts=None  SR=0.12
670	    conclusion=negative
671	    files: ['logs/eval_object_obs_only_seed43.json', '/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_seed43.json']
672	    cmd: python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0...
673	    hypothesis: D031: obs_only CRM v3-norm seed=43 on LIBERO object benchmark. Doubles sample size for Fisher exact test. seed=42 shows obs_only 16% vs argmin 8% (+8p
674	
675	  exp_id: eval-obs-only-spatial-seed43
676	    status=DONE  server=bjb1-18228  seed=43  ε=0.1
677	    n_rollouts=10  total_rollouts=None  SR=N/A
678	    conclusion=failed
679	    files: ['~/runs/acr-vla-conformal-refinement/eval-obs-only-spatial-seed43.log', 'logs/eval_obs_only_spatial_seed43.json"']
680	    cmd: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollout...
681	    hypothesis: D029: obs_only seed=43 复现实验。obs_only 是项目唯一存活路径。seed=42 如果确认 +5pp over argmin，seed=43 增加统计力（200 vs 200 样本下 Fisher exact p ~0.12，配合 object benchmark 独立验
682	
683	  exp_id: eval-obs-only-object-norm005-seed44
684	    status=RUNNING  server=bjb1-32546  seed=44  ε=0.05
685	    n_rollouts=None  total_rollouts=None  SR=N/A
686	    conclusion=None
687	    files: ['~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm005-seed44.log']
688	    cmd: crm_obs_only --seed 44 --K 10 --max_correction_norm 0.05
689	    hypothesis: obs_only CRM (ε=0.05) seed44 on LIBERO-Object. 补充 Figure 2 低 norm 段数据。seed42=13%, seed43 running。
690	
691	  exp_id: eval-obs-only-object-norm01-seed44
692	    status=DONE  server=bjb1-32546  seed=44  ε=0.1
693	    n_rollouts=10  total_rollouts=100  SR=N/A
694	    conclusion=success
695	    files: ['logs/eval_object_obs_only_norm01_seed44.json"', '~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm01-seed44.log']
696	    cmd: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MU...
697	    hypothesis: Obs-only CRM with norm=0.1 on LIBERO-Object seed=44 replicates seed=42 success, confirming that performance gains are robust across random seeds and n
698	
699	  exp_id: eval-obs-only-object-norm005-seed45
700	    status=RUNNING  server=bjb1-32546  seed=45  ε=0.05
701	    n_rollouts=None  total_rollouts=None  SR=N/A
702	    conclusion=None
703	    cmd: crm_obs_only --seed 45 --K 10 --max_correction_norm 0.05
704	    hypothesis: obs_only CRM (ε=0.05) seed45 on LIBERO-Object. Supplements magnitude curve low-norm data. seed42=13%, seed43=14%.
705	
706	  exp_id: eval-obs-only-object-norm01-seed45
707	    status=DONE  server=bjb1-18228  seed=45  ε=0.1
708	    n_rollouts=None  total_rollouts=None  SR=0.14
709	    conclusion=success
710	    files: ['logs/eval_object_obs_only_norm01_seed45.json']
711	    cmd: source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 python src/evaluate.py --mode crm_obs_only --max_correction_nor...
712	    hypothesis: obs_only CRM (ε=0.1) seed=45 on LIBERO Object. 验证 obs_only 在低 norm (0.1) 的稳定性。seed42 在 0.1 为 19%，如果一致则确认 obs_only 全 norm 范围鲁棒。
713	
714	  exp_id: eval-obs-only-object-norm03-seed45
715	    status=DONE  server=bjb2-28827  seed=45  ε=0.3
716	    n_rollouts=10  total_rollouts=None  SR=N/A
717	    conclusion=failed
718	    files: ['logs/eval_object_obs_only_norm03_seed45.json"', '~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm03-seed45.log']
719	    cmd: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MU...
720	    hypothesis: obs_only CRM v3-norm at norm=0.3 seed=45 on LIBERO object benchmark. Multi-seed magnitude curve data point. seed42 norm=0.3=19%, seed44 norm=0.3=runni
721	
722	  exp_id: eval-obs-only-object-norm03-seed45-r2
723	    status=DONE  server=bjb2-28827  seed=45  ε=0.3
724	    n_rollouts=10  total_rollouts=100  SR=14
725	    conclusion=success
726	    files: ['~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm03-seed45-r2.log', 'logs/eval_object_obs_only_norm03_seed45_r2.json"']
727	    cmd: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MU...
728	    hypothesis: obs_only CRM with max_correction_norm=0.3 on LIBERO Object (seed=45) should show graceful degradation similar to seed42 (19%), providing multi-seed er
729	
730	  exp_id: eval-obs-only-object-norm01-seed46
731	    status=DONE  server=bjb1-18228  seed=46  ε=0.1
732	    n_rollouts=None  total_rollouts=None  SR=N/A
733	    conclusion=failed
734	    files: ['/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed46.log', 'logs/eval_object_obs_only_norm01_seed46.json']
735	    cmd: python evaluate.py --benchmark object --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --seed 46 --output_file logs/eval_obj...
736	    hypothesis: obs_only CRM (ε=0.1) seed=46 on LIBERO Object. Extends magnitude curve low-norm segment to 3+ seeds. If consistent with seed42=19% and seed45 (running
737	
738	  exp_id: eval-obs-only-object-norm01-seed46-bjb2
739	    status=DONE  server=bjb2-28827  seed=46  ε=0.1
740	    n_rollouts=None  total_rollouts=None  SR=N/A
741	    conclusion=killed
742	    cmd: python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --seed 46 --benchmark object
743	    hypothesis: Duplicate of obs_only norm=0.1 seed46 on bjb2 (deployed by batch5 Worker). Extra data point for magnitude curve.
744	
745	  exp_id: eval-obs-only-object-norm01-seed46-r2
746	    status=DEPLOYED  server=bjb1-32546  seed=46  ε=0.1
747	    n_rollouts=10  total_rollouts=None  SR=N/A
748	    conclusion=killed
749	    files: ['logs/eval_object_obs_only_norm01_seed46.json']
750	    cmd: cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/chec...
751	    hypothesis: obs_only CRM with ε=0.1 on LIBERO-Object seed46. Retry after previous run was killed at task 5/10.
752	
753	  exp_id: eval-obs-only-object-norm01-seed46-r3
754	    status=RUNNING  server=bjb1-32546  seed=46  ε=0.1
755	    n_rollouts=None  total_rollouts=None  SR=N/A
756	    conclusion=None
757	    cmd: crm_obs_only --seed 46 --K 10 --max_correction_norm 0.1
758	    hypothesis: obs_only CRM (ε=0.1) seed46 on LIBERO-Object. Retry r3. Supplements magnitude curve ε=0.1 data. seed42=19%, seed43=12%, seed44=16%, seed45=14%.
759	
760	  exp_id: eval-obs-only-object-norm03-seed46
761	    status=DONE  server=bjb1-32546  seed=46  ε=0.3
762	    n_rollouts=10  total_rollouts=None  SR=N/A
763	    conclusion=success
764	    files: ['logs/eval_object_obs_only_norm03_seed46.json', '/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed46.json']
765	    cmd: CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --seed 46 --benchmark obje...
766	    hypothesis: obs_only CRM at eps=0.3 on seed46 extends magnitude curve high-norm data. seed42=19%, seed44=18%, seed45=14%. 4th seed at this norm.
767	
768	  exp_id: eval-obs-only-object-norm01-seed47
769	    status=DONE  server=bjb2-28827  seed=47  ε=0.1
770	    n_rollouts=10  total_rollouts=None  SR=N/A
771	    conclusion=killed
772	    files: ['~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm01-seed47.log']
773	    cmd: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts...
774	    hypothesis: obs_only CRM (ε=0.1) seed=47 on LIBERO Object. 4th seed for magnitude curve low-norm point. Combined with seeds 42/45/46, provides error bar for obs_o
775	
776	  exp_id: eval-obs-only-object-norm01-seed47-bjb2
777	    status=DONE  server=bjb2-28827  seed=47  ε=0.1
778	    n_rollouts=None  total_rollouts=None  SR=N/A
779	    conclusion=killed
780	    files: ['N/A (killed duplicate)']
781	    cmd: python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --seed 47 --benchmark object
782	    hypothesis: Duplicate of seed47 obs_only norm=0.1 on bjb2 (survived GPU conflict cleanup), provides extra seed47 data point
783	
784	  exp_id: eval-obs-only-object-norm01-seed47-r2
785	    status=DONE  server=bjb1-18228  seed=47  ε=0.1
786	    n_rollouts=None  total_rollouts=None  SR=N/A
787	    conclusion=killed
788	    cmd: python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --seed 47 --benchmark object
789	    hypothesis: obs_only CRM at eps=0.1 on seed47 will achieve similar improvement over VLA-only as seen in seed42 (19%), testing seed robustness of the magnitude cur
790	
791	  exp_id: eval-obs-only-object-norm03-seed47
792	    status=DONE  server=bjb1-18228  seed=47  ε=0.3
793	    n_rollouts=10  total_rollouts=None  SR=N/A
794	    conclusion=failed
795	    files: ['logs/eval_object_obs_only_norm03_seed47.json']
796	    cmd: CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt ...
797	    hypothesis: obs_only CRM ε=0.3 seed47 on LIBERO-Object. 5th seed at high norm (seed42=19%, seed44=18%, seed45=14%, seed46 running). 补全 magnitude curve 高 norm 段 er
798	
799	  exp_id: eval-obs-only-object-norm01-seed48
800	    status=RUNNING  server=bjb1-18228  seed=48  ε=0.1
801	    n_rollouts=10  total_rollouts=None  SR=N/A
802	    conclusion=None
803	    files: ['logs/eval_object_obs_only_norm01_seed48.json']
804	    cmd: CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 48 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/...
805	    hypothesis: obs_only CRM (ε=0.1) seed48 on LIBERO-Object. 补充 magnitude curve low-norm 段 seed48 数据。扩展 error bars。
806	
807	  exp_id: eval_obs_only_norm01_seed48
808	    status=PREPARING  server=bjb1-18228  seed=48  ε=0.1
809	    n_rollouts=10  total_rollouts=None  SR=N/A
810	    conclusion=killed
811	    files: ['logs/eval_object_obs_only_norm01_seed48.json', '~/runs/acr-vla-conformal-refinement/eval_obs_only_norm01_seed48.log']
812	    cmd: cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 48 --K 10 --crm_checkpoint /root/autodl-tmp/checkp...
813	
814	  exp_id: eval-obs-only-object-norm03-seed48
815	    status=RUNNING  server=bjb1-18228  seed=48  ε=0.3
816	    n_rollouts=10  total_rollouts=None  SR=N/A
817	    conclusion=None
818	    files: ['logs/eval_object_obs_only_norm03_seed48.json']
819	    cmd: CUDA_VISIBLE_DEVICES=2 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 48 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/...
820	    hypothesis: obs_only CRM (ε=0.3) seed48 on LIBERO-Object. 补充 magnitude curve high-norm 段 seed48 数据。扩展 error bars。
821	
822	  exp_id: eval_obs_only_norm03_seed48
823	    status=PREPARING  server=bjb1-18228  seed=48  ε=0.3
824	    n_rollouts=10  total_rollouts=None  SR=N/A
825	    conclusion=killed
826	    files: ['logs/eval_object_obs_only_norm03_seed48.json', '~/runs/acr-vla-conformal-refinement/eval_obs_only_norm03_seed48.log']
827	    cmd: cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 48 --K 10 --crm_checkpoint /root/autodl-tmp/checkp...
828	
829	====================================================================================================
830	  5. MAGNITUDE CURVE PERDOF — Various ε  (49 experiments)
831	====================================================================================================
832	
833	  exp_id: eval-acr-object-v4-default
834	    status=DONE  server=bjb2-28827  seed=42
835	    n_rollouts=10  total_rollouts=None  SR=N/A
836	    conclusion=killed
837	    files: ['logs/eval_object_perdof_default_norm.log', 'logs/eval_object_perdof_default_norm.json']
838	    cmd: CUDA_VISIBLE_DEVICES=3 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42...
839	    hypothesis: Ablation: perdof CRM v3-norm with DEFAULT max_correction_norm (~1.42, no magnitude control) on LIBERO object benchmark. Tests whether magnitude contro
840	
841	  exp_id: eval-acr-object-v4-default-r2
842	    status=DONE  server=bjb1-18228  seed=42
843	    n_rollouts=10  total_rollouts=None  SR=N/A
844	    conclusion=success
845	    files: ['~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-default-r2.log', 'logs/eval_object_perdof_default_norm_r2.json']
846	    cmd: CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42...
847	    hypothesis: v4-default (no magnitude control, norm≈1.42) on object benchmark — ablation to confirm catastrophic failure
848	
849	  exp_id: eval-mag-perdof-norm003
850	    status=DONE  server=bjb2-28827  seed=42  ε=0.03
851	    n_rollouts=10  total_rollouts=100  SR=N/A
852	    conclusion=negative
853	    files: ['logs/eval_mag_perdof_norm003.json']
854	    cmd: python -u src/evaluate.py --benchmark spatial --mode acr_vla --max_correction_norm 0.03 --n_rollouts 10 --K 10 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ --crm_checkpoint /root/autodl-tmp/...
855	    hypothesis: perdof CRM (ε=0.03) on LIBERO Spatial benchmark. 极低 norm 下 perdof 在 spatial 的表现。与 obs_only-0.03 (34%) 对比，验证低 norm 安全区域。
856	
857	  exp_id: eval-mag-perdof-norm003-object
858	    status=DONE  server=bjb2-28827  seed=42  ε=0.03
859	    n_rollouts=None  total_rollouts=None  SR=N/A
860	    conclusion=success
861	    files: ['logs/eval_object_perdof_norm003.json']
862	    cmd: python src/evaluate.py --mode crm_perdof --max_correction_norm 0.03 --K 10 --seed 42 --benchmark object
863	    hypothesis: Object magnitude sweep: perdof CRM v3-norm at norm=0.03 on LIBERO object benchmark. Paired with obs_only norm=0.03 for magnitude comparison figure. Te
864	
865	  exp_id: eval-mag-perdof-norm005
866	    status=DONE  server=bjb2-28827  seed=42  ε=0.05
867	    n_rollouts=10  total_rollouts=None  SR=N/A
868	    conclusion=negative
869	    files: ['/root/runs/acr-vla-conformal-refinement/eval-mag-perdof-norm005.log', 'logs/eval_mag_perdof_norm005.json']
870	    cmd: python -u src/evaluate.py --benchmark spatial --mode acr_vla --max_correction_norm 0.05 --n_rollouts 10 --K 10 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ --crm_checkpoint /root/autodl-tmp/...
871	    hypothesis: perdof CRM (ε=0.05) on LIBERO Spatial benchmark. 低 norm 下 perdof 在 spatial 的表现。如果与 obs_only-0.05 一致（35%），说明低 norm 约束消除了 conditioning 差异。
872	
873	  exp_id: eval-mag-perdof-norm005-object
874	    status=DONE  server=bjb2-28827  seed=42  ε=0.05
875	    n_rollouts=10  total_rollouts=None  SR=N/A
876	    conclusion=success
877	    files: ['logs/eval_object_perdof_norm005.json', 'logs/nohup_eval_object_perdof_norm005.log']
878	    cmd: python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.05 ...
879	    hypothesis: perdof CRM (ε=0.05) seed=42 on LIBERO Object. 验证 perdof 在极低 norm 下是否与 obs_only 接近（两者都受限于低 norm 纠正量）。magnitude curve 低端数据点。
880	
881	  exp_id: eval-acr-object-v4-perdof
882	    status=DONE  server=bjb1-32546  seed=42  ε=0.1
883	    n_rollouts=10  total_rollouts=100  SR=N/A
884	    conclusion=success
885	    files: ['~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-perdof.log']
886	    cmd: python -u src/evaluate.py --mode acr_vla --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1
887	    hypothesis: D021: ACR-VLA perdof CRM v3-norm with max_correction_norm=0.1 on LIBERO object benchmark. Cross-benchmark validation of spatial findings.
888	
889	  exp_id: eval-perdof-object-norm01-seed42
890	    status=DEPLOYED  server=bjb2-28827  seed=42  ε=0.1
891	    n_rollouts=10  total_rollouts=None  SR=N/A
892	    conclusion=failed
893	    files: ['logs/eval_object_perdof_norm01_seed42.json']
894	    cmd: cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /r...
895	    hypothesis: perdof CRM with ε=0.1 on LIBERO-Object seed42. Magnitude curve comparison point for perdof variant.
896	
897	  exp_id: eval-perdof-object-norm01-seed42-r2
898	    status=RUNNING  server=bjb2-28827  seed=42  ε=0.1
899	    n_rollouts=10  total_rollouts=None  SR=N/A
900	    conclusion=None
901	    files: ['logs/eval_object_perdof_norm01_seed42.json']
902	    cmd: cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /r...
903	    hypothesis: perdof CRM with max_correction_norm=0.1 on LIBERO-Object seed42. Rerun of failed eval-perdof-object-norm01-seed42. PID 497642 on cuda:3, started 07:52
904	
905	  exp_id: eval-mag-perdof-norm02
906	    status=DONE  server=bjb2-28827  seed=42  ε=0.2
907	    n_rollouts=10  total_rollouts=None  SR=N/A
908	    conclusion=killed
909	    files: ['logs/eval_mag_perdof_norm02.json']
910	    cmd: python -u src/evaluate.py --benchmark spatial --mode acr_vla --max_correction_norm 0.2 --n_rollouts 10 --K 10 --smolvla_path /root/autodl-tmp/models/smolvla_libero/ --crm_checkpoint /root/autodl-tmp/c...
911	    hypothesis: Per-DoF CRM with max_correction_norm=0.2 on LIBERO-Spatial achieves optimal balance between correction magnitude and stability — norm=0.2 is hypothesi
912	
913	  exp_id: eval-mag-perdof-norm02-object
914	    status=DONE  server=bjb1-32546  seed=42  ε=0.2
915	    n_rollouts=10  total_rollouts=None  SR=N/A
916	    conclusion=negative
917	    files: ['logs/eval_object_perdof_norm02.json"', '~/runs/acr-vla-conformal-refinement/eval-mag-perdof-norm02-object.log']
918	    cmd: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 1...
919	    hypothesis: Object magnitude sweep: perdof CRM v3-norm at norm=0.2 on LIBERO object benchmark. Paired with obs_only norm=0.2 (running, 18% at 5/10) for magnitude 
920	
921	  exp_id: eval-mag-perdof-norm03
922	    status=DONE  server=bjb2-28827  seed=42  ε=0.3
923	    n_rollouts=10  total_rollouts=100  SR=N/A
924	    conclusion=negative
925	    files: ['/root/runs/acr-vla-conformal-refinement/eval-mag-perdof-norm03.log']
926	    cmd: python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --s...
927	    hypothesis: perdof CRM (ε=0.3) on LIBERO Spatial benchmark. 高 norm 下 perdof 在 spatial 是否也出现退化。如果 spatial 无 collapse（与 obs_only 接近），说明 failure mode 与 task complexi
928	
929	  exp_id: eval-mag-perdof-norm03-object
930	    status=DEPLOYED  server=bjb2-28827  seed=42  ε=0.3
931	    n_rollouts=10  total_rollouts=None  SR=N/A
932	    conclusion=killed
933	    files: ['logs/eval_object_perdof_norm03.json']
934	    cmd: python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 -...
935	
936	  exp_id: eval-mag-perdof-norm03-object-r2
937	    status=DONE  server=bjb2-28827  seed=42  ε=0.3
938	    n_rollouts=10  total_rollouts=None  SR=N/A
939	    conclusion=killed
940	    files: ['logs/eval_object_perdof_norm03_r2.json']
941	    cmd: CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --ma...
942	
943	  exp_id: eval-mag-perdof-norm03-object-r3
944	    status=DONE  server=bjb2-28827  seed=42  ε=0.3
945	    n_rollouts=10  total_rollouts=None  SR=N/A
946	    conclusion=success
947	    files: ['logs/eval_object_perdof_norm03_r3.json']
948	    cmd: python -u src/evaluate.py --mode crm_perdof --benchmark object --seed 42 --K 10 --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_r3.json
949	    hypothesis: perdof CRM (ε=0.3) seed=42 on LIBERO Object magnitude sweep. 验证 perdof 在 norm=0.3 的 collapse 程度。预期 SR 急剧下降（支持 progressive collapse 叙事）。
950	
951	  exp_id: eval-mag-perdof-norm0p3-object
952	    status=DONE  server=bjb1-32546  seed=42  ε=0.3
953	    n_rollouts=10  total_rollouts=None  SR=N/A
954	    conclusion=killed
955	    files: ['~/runs/acr-vla-conformal-refinement/eval-mag-perdof-norm0p3-object.log', 'logs/eval_object_perdof_norm03.json"']
956	    cmd: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --m...
957	    hypothesis: Retry of eval-mag-perdof-norm03-object (killed by SIGTERM). Object magnitude sweep: perdof CRM v3-norm at norm=0.3 on LIBERO object benchmark. Paired 
958	
959	  exp_id: eval-mag-perdof-norm0p3-object-r2
960	    status=DONE  server=bjb2-28827  seed=42  ε=0.3
961	    n_rollouts=10  total_rollouts=None  SR=N/A
962	    conclusion=killed
963	    files: ['logs/eval_object_perdof_norm03_r2.json"', '~/runs/acr-vla-conformal-refinement/eval-mag-perdof-norm0p3-object-r2.log']
964	    cmd: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MU...
965	    hypothesis: Object magnitude sweep: perdof CRM v3-norm at norm=0.3 on LIBERO object benchmark. Migrated from bjb1-32546:cuda:4 (GPU conflict) to bjb2-28827:cuda:2
966	
967	  exp_id: eval-perdof-object-default-seed43
968	    status=RUNNING  server=bjb1-18228  seed=43
969	    n_rollouts=10  total_rollouts=None  SR=N/A
970	    conclusion=None
971	    files: ['logs/eval_object_perdof_default_seed43.json"', '~/runs/acr-vla-conformal-refinement/eval-perdof-object-default-seed43.log']
972	    cmd: bash -c "cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp...
973	    hypothesis: Perdof CRM without norm clipping (uncapped, actual norm ~1.42) causes catastrophic collapse on LIBERO-Object. seed42=0%, seed46=0%, seed44=0% (partial
974	
975	  exp_id: eval-perdof-object-norm01-seed43
976	    status=RUNNING  server=bjb1-32546  seed=43  ε=0.1
977	    n_rollouts=None  total_rollouts=None  SR=N/A
978	    conclusion=None
979	    files: ['~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm01-seed43.log']
980	    cmd: crm_perdof --seed 43 --K 10 --max_correction_norm 0.1
981	
982	  exp_id: eval-perdof-object-seed43
983	    status=DONE  server=bjb1-18228  seed=43  ε=0.1
984	    n_rollouts=10  total_rollouts=100  SR=0.12
985	    conclusion=success
986	    files: ['logs/eval_object_perdof_seed43.json', '~/runs/acr-vla-conformal-refinement/eval-perdof-object-seed43.log']
987	    cmd: python evaluate.py --benchmark object --mode crm_perdof --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1 --K 10 --seed 43 --n_rollouts 10 --output...
988	    hypothesis: D031 supplementary: perdof CRM v3-norm seed=43 on LIBERO object benchmark. Completes three-way comparison (obs_only vs argmin vs perdof) with doubled 
989	
990	  exp_id: eval-mag-perdof-norm02-seed43-object
991	    status=DONE  server=bjb2-28827  seed=43  ε=0.2
992	    n_rollouts=10  total_rollouts=None  SR=N/A
993	    conclusion=killed
994	    files: ['logs/eval_object_perdof_norm02_seed43.json']
995	    cmd: CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --ma...
996	
997	  exp_id: eval-mag-perdof-norm02-seed43-object-r2
998	    status=DONE  server=bjb2-28827  seed=43  ε=0.2
999	    n_rollouts=10  total_rollouts=None  SR=N/A
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LkyHAJXMgM6jYEjtYbJhsT",
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "3a463580-1698-49b2-875c-f88404fccb53"
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
  "task_id": "a5dc54df06c763762",
  "tool_use_id": "toolu_01LkyHAJXMgM6jYEjtYbJhsT",
  "description": "Reading ~/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/c1bdccab-16c6-497c-9d30-0feab97d927d/tool-results/bkoeg1h8a.txt",
  "usage": {
    "total_tokens": 53756,
    "tool_uses": 7,
    "duration_ms": 70348
  },
  "last_tool_name": "Read",
  "uuid": "c1775f00-1a40-455e-b5de-1c786423416e",
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d"
}
```

---


### Tool call

_source line 52_

<details open><summary>🔧 Tool call — Read · `toolu_016pzwN83BFYMUSC8NS2LMgC`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/c1bdccab-16c6-497c-9d30-0feab97d927d/tool-results/bkoeg1h8a.txt",
  "limit": 500,
  "offset": 999
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LkyHAJXMgM6jYEjtYbJhsT",
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "b486ec76-8bc7-44a1-b52a-4cc17aed9c5b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VVx4rDbpfeNBPqSVKmEqAJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 30580,
      "cache_read_input_tokens": 22977,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30580,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
      "service_tier": "standard",
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

_source line 53 · 2026-05-18T10:44:28.892Z_

<details><summary>↩ Tool result · `toolu_016pzwN83BFYMUSC8NS2LMgC`</summary>

```text
999	    n_rollouts=10  total_rollouts=None  SR=N/A
1000	    conclusion=killed
1001	    files: ['logs/eval_object_perdof_norm02_seed43.json"', 'N/A']
1002	    cmd: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MU...
1003	    hypothesis: Object magnitude sweep: perdof CRM v3-norm norm=0.2 seed=43. Moved from bjb2-28827:cuda:3 (GPU conflict with obs_only spatial) to cuda:2. Tests perdof
1004	
1005	  exp_id: eval-mag-perdof-norm02-seed43-object-r3
1006	    status=DONE  server=bjb2-28827  seed=43  ε=0.2
1007	    n_rollouts=10  total_rollouts=None  SR=N/A
1008	    conclusion=success
1009	    files: ['logs/eval_object_perdof_norm02_seed43_r3.json"']
1010	    cmd: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MU...
1011	    hypothesis: perdof CRM (ε=0.2) seed=43 on LIBERO Object. 验证 perdof 在 norm=0.2 的多 seed 数据（seed42=11%）。确认 perdof 在中间 norm 的退化幅度具有跨 seed 一致性。
1012	
1013	  exp_id: eval-perdof-object-norm02-seed43
1014	    status=RUNNING  server=bjb1-32546  seed=43  ε=0.2
1015	    n_rollouts=None  total_rollouts=None  SR=N/A
1016	    conclusion=None
1017	    cmd: crm_perdof --seed 43 --K 10 --max_correction_norm 0.2
1018	    hypothesis: perdof CRM ε=0.2 seed43 on LIBERO-Object. 补充 perdof magnitude curve ε=0.2 数据（seed42=11%, seed43 之前仅 spatial 数据 9%）。与 obs_only ε=0.2 seed43=16% 配对对比。
1019	
1020	  exp_id: eval-perdof-object-norm02-seed43-r3
1021	    status=DONE  server=bjb1-32546  seed=43  ε=0.2
1022	    n_rollouts=10  total_rollouts=None  SR=N/A
1023	    conclusion=success
1024	    files: ['N/A (killed as duplicate)', 'logs/eval_object_perdof_norm02_seed43_bjb1-32546.json']
1025	    cmd: CUDA_VISIBLE_DEVICES=4 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 43...
1026	    hypothesis: perdof CRM ε=0.2 seed43 on LIBERO-Object. 第 3 次尝试。补充 perdof magnitude curve ε=0.2 数据（seed42=11%）。
1027	
1028	  exp_id: eval-perdof-object-default-seed44
1029	    status=DONE  server=autodl-4090 (previous run)  seed=44
1030	    n_rollouts=10  total_rollouts=90  SR=N/A
1031	    conclusion=negative
1032	    files: ['partial results from previous run, 0/90 rollouts across 9/10 tasks']
1033	    cmd: python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt
1034	    hypothesis: perdof CRM (default norm ~1.42) seed=44 on LIBERO Object. 验证 perdof 在 uncapped norm 下的 catastrophic collapse（seed42=0%）。为 magnitude curve 提供第二个 seed 的
1035	
1036	  exp_id: eval-perdof-object-seed44
1037	    status=DONE  server=None  seed=44
1038	    n_rollouts=10  total_rollouts=100  SR=N/A
1039	    conclusion=negative
1040	    hypothesis: perdof CRM v3-norm seed=44 on LIBERO object benchmark. Completes seed=44 four-way comparison. seed42=11%, seed43=12%. Expected to confirm perdof < arg
1041	
1042	  exp_id: eval-perdof-object-norm005-seed44
1043	    status=RUNNING  server=bjb1-32546  seed=44  ε=0.05
1044	    n_rollouts=None  total_rollouts=None  SR=N/A
1045	    conclusion=None
1046	    files: ['~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm005-seed44.log']
1047	    cmd: crm_perdof --seed 44 --K 10 --max_correction_norm 0.05
1048	    hypothesis: perdof CRM (ε=0.05) seed44 on LIBERO-Object. 补充 Figure 2 低 norm 段 perdof 数据。与 obs_only norm005 seed44 配对对比。
1049	
1050	  exp_id: eval-perdof-object-norm01-seed44
1051	    status=DONE  server=bjb1-18228  seed=44  ε=0.1
1052	    n_rollouts=10  total_rollouts=100  SR=N/A
1053	    conclusion=negative
1054	    files: ['logs/eval_object_perdof_norm01_seed44.json']
1055	    cmd: python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1 -...
1056	    hypothesis: perdof CRM (ε=0.1) seed=44 on LIBERO Object. 验证 perdof 在低 norm 的安全区域（seed42=11%，seed45 running）。多 seed 支撑 magnitude curve 低 norm 段。
1057	
1058	  exp_id: eval-perdof-object-norm02-seed44
1059	    status=DONE  server=bjb2-28827  seed=44  ε=0.2
1060	    n_rollouts=10  total_rollouts=None  SR=0.1
1061	    conclusion=success
1062	    files: ['logs/eval_object_perdof_norm02_seed44.json', '~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm02-seed44.log']
1063	    cmd: CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --ma...
1064	    hypothesis: perdof CRM (ε=0.2) seed=44 on LIBERO Object benchmark. Adds second seed to perdof norm=0.2 (seed42=11%, seed43=9%). Enables error bar on magnitude cur
1065	
1066	  exp_id: eval-perdof-object-norm03-seed44
1067	    status=DONE  server=bjb1-18228  seed=44  ε=0.3
1068	    n_rollouts=10  total_rollouts=None  SR=0.04
1069	    conclusion=negative
1070	    files: ['logs/eval_object_perdof_norm03_seed44.json"', '~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm03-seed44.log']
1071	    cmd: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MU...
1072	    hypothesis: perdof CRM (ε=0.3) seed=44 on LIBERO Object. 验证 perdof 在高 norm (0.3) 的退化程度（seed42=4%）。多 seed 确认 perdof progressive collapse 机制。
1073	
1074	  exp_id: eval-perdof-object-norm03-seed44-r2
1075	    status=DONE  server=bjb1-32546  seed=44  ε=0.3
1076	    n_rollouts=10  total_rollouts=100  SR=0.04
1077	    conclusion=negative
1078	    files: ['logs/eval_object_perdof_norm03_seed44_r2.json']
1079	    cmd: CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 44 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --ma...
1080	    hypothesis: perdof CRM ε=0.3 seed44 re-run on LIBERO-Object. 原 seed44 已完成(conclusion=negative, SR=4%). 重跑验证跨 seed 一致性。
1081	
1082	  exp_id: eval-perdof-object-default-seed45
1083	    status=PREPARING  server=None  seed=45
1084	    n_rollouts=None  total_rollouts=None  SR=N/A
1085	    conclusion=None
1086	    hypothesis: Per-DoF CRM with default norm on LIBERO-Object seed=45 validates cross-seed consistency of per-DoF correction — paired with seed42/43/44 to assess var
1087	
1088	  exp_id: eval-perdof-object-norm01-seed45
1089	    status=DONE  server=bjb1-32546  seed=45  ε=0.1
1090	    n_rollouts=10  total_rollouts=None  SR=N/A
1091	    conclusion=success
1092	    files: ['logs/eval_object_perdof_norm01_seed45.json']
1093	    cmd: python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1 -...
1094	    hypothesis: perdof CRM (ε=0.1) seed=45 on LIBERO Object. 验证 perdof 在低 norm (0.1) 的安全区域（seed42=11%）。如果与 obs_only 接近，支持"低 norm 两者等效"叙事。
1095	
1096	  exp_id: eval-perdof-object-norm02-seed45
1097	    status=DONE  server=bjb2-28827  seed=45  ε=0.2
1098	    n_rollouts=None  total_rollouts=None  SR=0.09
1099	    conclusion=success
1100	    files: ['/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed45.log', 'logs/eval_object_perdof_norm02_seed45.json']
1101	    cmd: CUDA_VISIBLE_DEVICES=1 python src/evaluate.py --benchmark object --mode crm_perdof --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 --K 10 --seed ...
1102	    hypothesis: perdof CRM (ε=0.2) seed=45 on LIBERO Object. 验证 perdof 在中间 norm (0.2) 的表现（seed42=11%, seed43=9%）。为 magnitude curve 误差估计提供第三个 seed。
1103	
1104	  exp_id: eval-perdof-object-norm02-seed45-deploy
1105	    status=DONE  server=bjb1-18228  seed=45  ε=0.2
1106	    n_rollouts=10  total_rollouts=None  SR=N/A
1107	    conclusion=killed
1108	    files: ['~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm02-seed45-deploy.log', 'logs/eval_object_perdof_norm02_seed45.json']
1109	    cmd: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MU...
1110	    hypothesis: perdof CRM (ε=0.2) seed45 on LIBERO-Object. 补充 Figure 2 perdof magnitude curve ε=0.2 数据（seed42=11%, seed43=9%, seed44 running）。
1111	
1112	  exp_id: eval-perdof-object-norm02-seed45-r2
1113	    status=DONE  server=bjb1-18228  seed=45  ε=0.2
1114	    n_rollouts=10  total_rollouts=None  SR=N/A
1115	    conclusion=killed
1116	    files: ['~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm02-seed45-r2.log', 'logs/eval_object_perdof_norm02_seed45.json']
1117	    cmd: python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.2 -...
1118	    hypothesis: perdof CRM (ε=0.2) seed45 on LIBERO-Object. 补充 Figure 2 perdof magnitude curve ε=0.2 数据（seed42=11%, seed43=9%, seed44 running）。
1119	
1120	  exp_id: eval-perdof-object-norm02-seed45-r3
1121	    status=DONE  server=bjb1-18228  seed=45  ε=0.2
1122	    n_rollouts=10  total_rollouts=100  SR=0.12
1123	    conclusion=success
1124	    files: ['/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed45_r3.json', 'logs/eval_object_perdof_norm02_seed45_r3.json']
1125	    cmd: CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/pe...
1126	    hypothesis: perdof CRM (ε=0.2) seed45 on LIBERO-Object. r3 重试。补充 perdof magnitude curve ε=0.2 数据。
1127	
1128	  exp_id: eval-perdof-object-norm03-seed45-r2
1129	    status=DONE  server=bjb1-32546  seed=45  ε=0.3
1130	    n_rollouts=10  total_rollouts=None  SR=N/A
1131	    conclusion=negative
1132	    files: ['logs/eval_object_perdof_norm03_seed45_r2.json"', '~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm03-seed45-r2.log']
1133	    cmd: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MU...
1134	    hypothesis: perdof CRM (ε=0.3) seed=45 on LIBERO object benchmark. Retry after unregistered process conflict. Expected to confirm perdof collapse at high norm (se
1135	
1136	  exp_id: eval-perdof-object-default-seed46
1137	    status=DONE  server=bjb1-32546  seed=46
1138	    n_rollouts=10  total_rollouts=None  SR=0
1139	    conclusion=negative
1140	    files: ['/root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_seed46.json', 'logs/eval_object_perdof_default_seed46.json']
1141	    cmd: CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --ou...
1142	    hypothesis: perdof CRM (default norm, 无裁剪) seed46 on LIBERO-Object. 验证 perdof 在 uncapped norm 下的灾难性崩溃（seed42=0%）是否跨 seed 一致。支撑 obs_only > perdof claim。
1143	
1144	  exp_id: eval-perdof-object-norm01-seed46
1145	    status=DONE  server=bjb1-32546  seed=46  ε=0.1
1146	    n_rollouts=10  total_rollouts=None  SR=0.1
1147	    conclusion=negative
1148	    files: ['logs/eval_object_perdof_norm01_seed46.json', '/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed46.json']
1149	    cmd: python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1 -...
1150	    hypothesis: perdof CRM (ε=0.1) seed=46 on LIBERO Object. Extends perdof low-norm data (seed42=11%, seed44/45 running). At ε=0.1 perdof is in its "safe zone" (tigh
1151	
1152	  exp_id: eval-perdof-object-norm01-seed46-r2
1153	    status=DONE  server=bjb1-32546  seed=46  ε=0.1
1154	    n_rollouts=None  total_rollouts=None  SR=N/A
1155	    conclusion=success
1156	    cmd: python -u src/evaluate.py --mode crm_perdof --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1 --seed 46 --benchmark object
1157	    hypothesis: perdof CRM at eps=0.1 on seed46 will show magnitude sensitivity collapse pattern similar to seed42, confirming obs_only robustness advantage
1158	
1159	  exp_id: eval-perdof-object-norm02-seed46
1160	    status=DONE  server=bjb2-28827  seed=46  ε=0.2
1161	    n_rollouts=10  total_rollouts=None  SR=N/A
1162	    conclusion=success
1163	    files: ['logs/eval_object_perdof_norm02_seed46.json', '/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed46.json']
1164	    cmd: CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --ma...
1165	    hypothesis: perdof CRM with ε=0.2 on LIBERO-Object seed46. Magnitude curve data point for perdof variant at primary comparison norm.
1166	
1167	  exp_id: eval-perdof-object-norm03-seed46
1168	    status=DONE  server=bjb2-28827  seed=46  ε=0.3
1169	    n_rollouts=10  total_rollouts=None  SR=N/A
1170	    conclusion=failed
1171	    files: ['logs/eval_object_perdof_norm03_seed46.json']
1172	    cmd: CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --ma...
1173	    hypothesis: perdof CRM ε=0.3 seed46 on LIBERO-Object. 4th seed at high norm (seed42=4%, seed44=4%, seed45=6%). 验证 perdof 在高 norm 的灾难性崩溃是否跨 seed 一致。
1174	
1175	  exp_id: eval-perdof-object-norm03-seed46-r2
1176	    status=DONE  server=bjb2-28827  seed=46  ε=0.3
1177	    n_rollouts=10  total_rollouts=None  SR=N/A
1178	    conclusion=killed
1179	    files: ['logs/eval_object_perdof_norm03_seed46.json', 'N/A']
1180	    cmd: CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --ma...
1181	    hypothesis: perdof CRM ε=0.3 seed46 retry on LIBERO-Object. 原 PID 394433 退出，PID 392856 在 bjb2-28827 cuda:2 继续运行。seed42=4%, seed44=4%, seed45=6%。
1182	
1183	  exp_id: eval-perdof-object-norm01-seed47
1184	    status=DONE  server=bjb2-40593  seed=47  ε=0.1
1185	    n_rollouts=10  total_rollouts=None  SR=N/A
1186	    conclusion=killed
1187	    files: ['~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm01-seed47.log', 'logs/eval_object_perdof_norm01_seed47.json']
1188	    cmd: CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode crm_perdof --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1 --seed 47 --benchmark object -...
1189	    hypothesis: perdof CRM at eps=0.1 on seed47, completes magnitude curve low-norm data for perdof
1190	
1191	  exp_id: eval-perdof-object-norm01-seed47-bjb1
1192	    status=DONE  server=bjb1-32546  seed=47  ε=0.1
1193	    n_rollouts=10  total_rollouts=None  SR=N/A
1194	    conclusion=success
1195	    files: ['/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed47_r2.json']
1196	    cmd: cd /root/autodl-tmp/acr-vla && python evaluate.py --model smolvla --mode crm_perdof --benchmark object --seed 47 --n_rollouts 10 --norm_limit 0.1 --checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/...
1197	    hypothesis: Duplicate of perdof norm=0.1 seed47 on bjb1-32546 (deployed by orphan Worker). Also running on bjb2-40593.
1198	
1199	  exp_id: eval-perdof-object-norm02-seed47
1200	    status=DONE  server=bjb2-28827  seed=47  ε=0.2
1201	    n_rollouts=10  total_rollouts=None  SR=N/A
1202	    conclusion=success
1203	    files: ['/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed47.json', 'logs/eval_object_perdof_norm02_seed47.json']
1204	    cmd: /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_...
1205	    hypothesis: perdof CRM with ε=0.2 on LIBERO-Object seed47. Magnitude curve data point for perdof at primary comparison norm.
1206	
1207	  exp_id: eval-perdof-object-norm02-seed48
1208	    status=RUNNING  server=bjb2-28827  seed=48  ε=0.2
1209	    n_rollouts=None  total_rollouts=None  SR=N/A
1210	    conclusion=None
1211	    files: ['~/runs/acr-vla-conformal-refinement/eval-perdof-object-norm02-seed48.log']
1212	    cmd: crm_perdof --seed 48 --K 10 --max_correction_norm 0.2
1213	    hypothesis: perdof CRM (ε=0.2) seed48 on LIBERO-Object. 补充 magnitude curve ε=0.2 数据，扩展 error bars。
1214	
1215	====================================================================================================
1216	  6. SCALAR CRM  (10 experiments)
1217	====================================================================================================
1218	
1219	  exp_id: eval-scalar-unc-spatial
1220	    status=DONE  server=bjb1-18228  seed=42
1221	    n_rollouts=10  total_rollouts=None  SR=N/A
1222	    conclusion=killed
1223	    files: ['/root/autodl-tmp/eval_results/eval-scalar-unc-spatial.log']
1224	    cmd: CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode crm_scalar --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm/scalar_unc/crm_best.pt
1225	
1226	  exp_id: eval-scalar-unc-spatial-v2
1227	    status=DONE  server=bjb1-18228  seed=42
1228	    n_rollouts=10  total_rollouts=None  SR=N/A
1229	    conclusion=killed
1230	    files: ['~/runs/acr-vla-conformal-refinement/eval-scalar-unc-spatial-v2.log']
1231	    cmd: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/eva...
1232	
1233	  exp_id: eval-acr-object-v4-scalar
1234	    status=DONE  server=bjb1-32546  seed=42
1235	    n_rollouts=10  total_rollouts=None  SR=N/A
1236	    conclusion=negative
1237	    files: ['~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-scalar.log']
1238	    cmd: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MU...
1239	    hypothesis: D021: scalar_unc CRM v3-norm with max_correction_norm=0.1 on LIBERO object benchmark. Three-way ablation: perdof vs scalar_unc vs obs_only on object.
1240	
1241	  exp_id: eval-acr-object-v4-scalar-b2
1242	    status=DONE  server=bjb2-28827  seed=42
1243	    n_rollouts=10  total_rollouts=None  SR=N/A
1244	    conclusion=killed
1245	    files: ['~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-scalar-b2.log']
1246	    cmd: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MU...
1247	
1248	  exp_id: eval-acr-spatial-v4-scalar
1249	    status=DONE  server=bjb1-18228  seed=42
1250	    n_rollouts=10  total_rollouts=None  SR=N/A
1251	    conclusion=killed
1252	    files: ['~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-scalar.log']
1253	    cmd: python -u src/evaluate.py --mode crm_scalar --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm ...
1254	    hypothesis: D020: scalar_unc CRM (val_loss 0.0374) with max_correction_norm=0.1. Three-way ablation: perdof vs scalar_unc vs obs_only under identical correction m
1255	
1256	  exp_id: eval-acr-spatial-v4-scalar-r2
1257	    status=DONE  server=bjb1-18228  seed=42
1258	    n_rollouts=10  total_rollouts=100  SR=N/A
1259	    conclusion=success
1260	    files: ['~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-scalar-r2.log']
1261	    cmd: python -u src/evaluate.py --mode crm_scalar --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm ...
1262	    hypothesis: Restart from T3. scalar_unc CRM v3-norm with max_correction_norm=0.1 on spatial. Three-way ablation: perdof vs scalar_unc vs obs_only.
1263	
1264	  exp_id: eval-scalar-object-seed43
1265	    status=DONE  server=bjb1-32546  seed=43
1266	    n_rollouts=10  total_rollouts=None  SR=N/A
1267	    conclusion=success
1268	    files: ['logs/eval_object_scalar_seed43.json', '~/runs/acr-vla-conformal-refinement/eval-scalar-object-seed43.log']
1269	    cmd: python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 43 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0...
1270	    hypothesis: D031: scalar_unc CRM v3-norm seed=43 on LIBERO object benchmark. Completes seed=43 six-way comparison table. scalar seed=42 was worst at 4% — seed=43 
1271	
1272	  exp_id: eval-scalar-object-seed44
1273	    status=DONE  server=bjb2-40593  seed=44
1274	    n_rollouts=10  total_rollouts=None  SR=N/A
1275	    conclusion=failed
1276	    files: ['logs/eval_object_scalar_seed44.json"', '~/runs/acr-vla-conformal-refinement/eval-scalar-object-seed44.log']
1277	    cmd: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MU...
1278	    hypothesis: scalar_unc CRM v3-norm seed=44 on LIBERO object benchmark. Completes seed=44 six-way comparison. scalar seed42=9%, seed43 running (0% at 3/10). Expect
1279	
1280	  exp_id: eval-scalar-object-seed44-r2
1281	    status=DONE  server=bjb1-32546  seed=44
1282	    n_rollouts=10  total_rollouts=None  SR=N/A
1283	    conclusion=negative
1284	    files: ['logs/eval_object_scalar_seed44_r2.json"', '~/runs/acr-vla-conformal-refinement/eval-scalar-object-seed44-r2.log']
1285	    cmd: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MU...
1286	    hypothesis: Scalar CRM seed=44 on LIBERO object benchmark. Retry of failed eval-scalar-object-seed44. Expects scalar variant underperforms obs_only but may match 
1287	
1288	  exp_id: eval-scalar-object-seed45
1289	    status=DONE  server=bjb2-28827  seed=45
1290	    n_rollouts=None  total_rollouts=None  SR=0.09
1291	    conclusion=success
1292	    files: ['logs/eval_object_scalar_seed45.json', 'logs/eval_object_scalar_seed45.log']
1293	    cmd: python src/evaluate.py --mode crm_scalar --max_correction_norm 0.1 --K 10 --seed 45 --benchmark object --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --output_file lo...
1294	    hypothesis: Scalar uncertainty CRM seed=45 on LIBERO Object. 测试 scalar conditioning（单一 std 而非 per-DOF）是否比 obs_only 或 perdof 更优。如果表现介于两者之间，说明 conditioning 信息量与性能正相
1295	
1296	====================================================================================================
1297	  7. OTHER EVAL (uncategorized)  (31 experiments)
1298	====================================================================================================
1299	
1300	  exp_id: eval-acr-object-v3
1301	    status=DONE  server=bjb1-18228  seed=42
1302	    n_rollouts=10  total_rollouts=40  SR=0
1303	    conclusion=negative
1304	    files: ['~/runs/acr-vla-conformal-refinement/eval-acr-object-v3.log']
1305	    cmd: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/eva...
1306	    hypothesis: ACR pipeline v3 (K=10 conformal selection with scalar uncertainty) on LIBERO-Object improves over VLA-only baseline by selecting highest-confidence ac
1307	
1308	  exp_id: eval-acr-spatial-v1
1309	    status=DONE  server=bjb1-18228  seed=42
1310	    n_rollouts=10  total_rollouts=None  SR=N/A
1311	    conclusion=killed
1312	    files: ['/root/autodl-tmp/eval_results/eval-acr-spatial-v1.json', '/root/autodl-tmp/eval_results/eval-acr-spatial-v1.log']
1313	    cmd: CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/...
1314	
1315	  exp_id: eval-acr-spatial-v2
1316	    status=DONE  server=bjb1-18228  seed=42
1317	    n_rollouts=10  total_rollouts=None  SR=N/A
1318	    conclusion=killed
1319	    files: ['/root/autodl-tmp/eval_results/eval-acr-spatial-v2.log']
1320	    cmd: CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/...
1321	
1322	  exp_id: eval-acr-spatial-v3
1323	    status=DONE  server=bjb1-18228  seed=42
1324	    n_rollouts=10  total_rollouts=40  SR=0.025
1325	    conclusion=success
1326	    files: ['~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v3.log']
1327	    cmd: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/eva...
1328	    hypothesis: ACR pipeline v3 (K=10 conformal selection) on LIBERO-Spatial improves over VLA-only baseline, validating that conformal selection generalizes across s
1329	
1330	  exp_id: eval-acr-spatial-v4-default
1331	    status=DONE  server=bjb1-18228  seed=42
1332	    n_rollouts=10  total_rollouts=None  SR=N/A
1333	    conclusion=failed
1334	    cmd: CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/...
1335	    hypothesis: D018: Input normalization alone fixes CRM correction degradation. v3-norm checkpoint with default max_correction_norm=1.42. If >30% baseline → normali
1336	
1337	  exp_id: eval-acr-spatial-v4-default-r2
1338	    status=DONE  server=bjb2-40593  seed=42
1339	    n_rollouts=10  total_rollouts=None  SR=N/A
1340	    conclusion=killed
1341	    files: ['~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-default-r2.log']
1342	    cmd: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u src/evaluate....
1343	    hypothesis: D018 retry: Normalization alone fixes CRM correction degradation. v3-norm per-DOF checkpoint with default max_correction_norm (~1.42). If >30% baselin
1344	
1345	  exp_id: eval-acr-spatial-v4-default-r3
1346	    status=DONE  server=bjb2-40593  seed=42
1347	    n_rollouts=10  total_rollouts=None  SR=N/A
1348	    conclusion=killed
1349	    files: ['~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-default-r3.log']
1350	    cmd: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl ...
1351	    hypothesis: D018-D019 验证: perdof CRM v3-norm with DEFAULT max_correction_norm (~1.42). 如果 v4-default << v4-small (max_norm=0.1) → magnitude control 是必要的。如果 v4-def
1352	
1353	  exp_id: eval-acr-vla-spatial-v1
1354	    status=DONE  server=bjb1-18228  seed=42
1355	    n_rollouts=10  total_rollouts=None  SR=N/A
1356	    conclusion=killed
1357	    files: ['/root/autodl-tmp/eval_results/acr_vla_spatial_v1.json']
1358	    cmd: python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm/crm_best.pt --output_file /root/autodl-tmp/eval_results/...
1359	
1360	  exp_id: eval-k5-spatial
1361	    status=DONE  server=bjb1-18228  seed=42
1362	    n_rollouts=10  total_rollouts=None  SR=N/A
1363	    conclusion=killed
1364	    files: ['/root/autodl-tmp/eval_results/eval-k5-spatial.log']
1365	    cmd: MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 5 --crm_checkpoint /root/autodl-tmp/checkpoints/crm/k5/crm_best.pt
1366	
1367	  exp_id: eval-object-v6-full
1368	    status=DONE  server=None  seed=42
1369	    n_rollouts=10  total_rollouts=None  SR=N/A
1370	    conclusion=killed
1371	
1372	  exp_id: eval-random-selection-object-seed42
1373	    status=RUNNING  server=bjb2-40593  seed=42
1374	    n_rollouts=10  total_rollouts=None  SR=N/A
1375	    conclusion=None
1376	    cmd: python -u src/evaluate.py --mode random_selection --benchmark object --n_rollouts 10 --seed 42 --K 10
1377	    hypothesis: Random selection baseline (K=10 随机选一个 action) on LIBERO-Object seed42. Ablation 验证 CRM uncertainty-guided selection 的价值。
1378	
1379	  exp_id: eval-reconvla-spatial-v1
1380	    status=DONE  server=bjb1-18228  seed=42
1381	    n_rollouts=10  total_rollouts=None  SR=N/A
1382	    conclusion=killed
1383	    files: ['~/runs/acr-vla-conformal-refinement/eval-reconvla-spatial-v1.log']
1384	    cmd: python -u src/evaluate.py --mode reconvla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --smolvla_path /root/autodl-tmp/models/smolvla_libero/
1385	
1386	  exp_id: eval-reconvla-spatial-v2
1387	    status=DONE  server=bjb1-18228  seed=42
1388	    n_rollouts=10  total_rollouts=None  SR=N/A
1389	    conclusion=killed
1390	    files: ['~/runs/acr-vla-conformal-refinement/eval-reconvla-spatial-v1.log']
1391	    cmd: python -u src/evaluate.py --mode reconvla --benchmark spatial --n_rollouts 10 --seed 42 --K 10
1392	
1393	  exp_id: eval-reconvla-spatial-v3
1394	    status=DONE  server=bjb1-18228  seed=42
1395	    n_rollouts=10  total_rollouts=100  SR=0.34
1396	    conclusion=success
1397	    files: ['/root/autodl-tmp/eval_results/eval-reconvla-spatial-v3.log']
1398	    cmd: CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode reconvla --benchmark spatial --n_rollouts 10 --seed 42 --K 10
1399	    hypothesis: ReconVLA (K=10 sample consensus without CRM) on LIBERO-Spatial establishes upper bound for pure sampling diversity benefit — if high, CRM correction a
1400	
1401	  exp_id: eval-tiny-correction-spatial
1402	    status=DONE  server=bjb1-18228  seed=42  ε=0.05
1403	    n_rollouts=10  total_rollouts=None  SR=N/A
1404	    conclusion=killed
1405	    files: ['~/runs/acr-vla-conformal-refinement/eval-tiny-correction-spatial.log']
1406	    cmd: python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v2/perdof/crm_best.pt --max_correction_norm 0.05
1407	
1408	  exp_id: eval-acr-spatial-v4-small
1409	    status=DONE  server=bjb1-18228  seed=42  ε=0.1
1410	    n_rollouts=10  total_rollouts=None  SR=N/A
1411	    conclusion=killed
1412	    files: ['/root/autodl-tmp/logs/eval_acr_spatial_v4_small.log']
1413	    cmd: python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.1
1414	    hypothesis: D018: Normalization + moderate correction scaling (max_correction_norm=0.1, 14x smaller than default). If v4-small > v4-default → magnitude control ne
1415	
1416	  exp_id: eval-acr-spatial-v4-small-r2
1417	    status=DONE  server=bjb1-18228  seed=42  ε=0.1
1418	    n_rollouts=10  total_rollouts=100  SR=N/A
1419	    conclusion=success
1420	    files: ['~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-small-r2.log']
1421	    cmd: python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/crm_best.pt --max_correction_norm 0.1 --start_ta...
1422	    hypothesis: Restart from T7. ACR-VLA perdof CRM v3-norm with max_correction_norm=0.1 on spatial. Full per-DOF uncertainty pipeline.
1423	
1424	  exp_id: eval-direct-correction-object-seed42
1425	    status=DONE  server=bjb1-32546  seed=42  ε=0.2
1426	    n_rollouts=10  total_rollouts=None  SR=N/A
1427	    conclusion=failed
1428	    files: ['logs/results_direct_correction_object_seed42.json']
1429	    cmd: python -u src/evaluate.py --mode direct_correction --benchmark object --n_rollouts 10 --seed 42 --K 1 --checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0...
1430	    hypothesis: obs_only CRM 直接纠正单次 VLA 输出（跳过 K=10 采样+argmin 选择），测试 obs 特征鲁棒性在简化 pipeline 下是否成立。如果 SR > VLA-only (~11%)，说明 CRM 本身有独立价值；如果 SR < VLA-only，说明 selection 是
1431	
1432	  exp_id: eval-direct-correction-object-seed42-r2
1433	    status=DONE  server=bjb1-32546  seed=42  ε=0.2
1434	    n_rollouts=10  total_rollouts=None  SR=N/A
1435	    conclusion=failed
1436	    files: ['logs/results_direct_correction_object_seed42.json']
1437	    cmd: /root/miniconda3/bin/python -u src/evaluate.py --mode direct_correction --benchmark object --n_rollouts 10 --seed 42 --K 1 --checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --...
1438	    hypothesis: obs_only CRM 直接纠正单次 VLA 输出（K=1, 跳过 argmin selection），测试 CRM 本身是否有独立纠���价值。如果 SR > VLA-only (~11%)，说明 CRM correction 独立有效；如果 SR ≤ VLA-only，说明 multi-sam
1439	
1440	  exp_id: eval-direct-correction-object-seed42-r3
1441	    status=DONE  server=bjb1-32546  seed=42  ε=0.2
1442	    n_rollouts=10  total_rollouts=None  SR=0.14
1443	    conclusion=success
1444	    files: ['/root/acr-vla-conformal-refinement/logs/eval_direct_correction_object_seed42.log', 'logs/results_direct_correction_object_seed42.json']
1445	    cmd: /root/miniconda3/bin/python -u src/evaluate.py --mode direct_correction --benchmark object --n_rollouts 10 --seed 42 --K 1 --checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --...
1446	    hypothesis: obs_only CRM 直接纠正单次 VLA 输出（K=1, 跳过 argmin selection），测试 CRM 本身是否有独立纠正价值。如果 SR > VLA-only (~11%)，说明 CRM correction 独立有效；如果 SR ≤ VLA-only，说明 multi-sampl
1447	
1448	  exp_id: eval-k1-crm-accg-object-seed42
1449	    status=DONE  server=bjb1-32546  seed=42  ε=0.2
1450	    n_rollouts=10  total_rollouts=None  SR=0.11
1451	    conclusion=negative
1452	    files: ['/root/acr-vla-conformal-refinement/logs/eval_k1_crm_accg_object_seed42.json', 'logs/eval_k1_crm_accg_object_seed42.json']
1453	    cmd: CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --mode crm_k1_accg --benchmark object --n_rollouts 10 --seed 42 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt --max_correction_no...
1454	    hypothesis: K=1 CRM with ACCG (fallback 960D) on LIBERO-Object seed42. 验证 ACCG correction 是否优于 K=1 VLA-only baseline (mean 10.8%). Parent: train-crm-k1-accg-objec
1455	
1456	  exp_id: eval-k1-crm-multiscale-object-seed42
1457	    status=DONE  server=bjb2-28827  seed=42  ε=0.2
1458	    n_rollouts=10  total_rollouts=None  SR=N/A
1459	    conclusion=negative
1460	    files: ['logs/eval_k1_crm_multiscale_object_seed42.log']
1461	    cmd: CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode crm_k1_accg --benchmark object --n_rollouts 10 --seed 42 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt --max_correction_no...
1462	    hypothesis: K=1 CRM with ACCG (multi-scale 4x960D from layers [3,7,11,15]) on LIBERO-Object seed42. Compare with fallback (single-stage) and VLA-only baseline (10
1463	
1464	  exp_id: eval-random-selection-object-seed43
1465	    status=RUNNING  server=bjb2-28827  seed=43
1466	    n_rollouts=None  total_rollouts=None  SR=N/A
1467	    conclusion=None
1468	    files: ['~/runs/acr-vla-conformal-refinement/eval-random-selection-object-seed43.log']
1469	    cmd: random_selection --seed 43 --K 10
1470	    hypothesis: Random selection baseline (K=10 随机选一个 action) seed43 on LIBERO-Object. 多 seed 验证 CRM selection > random。seed42 RUNNING 中。
1471	
1472	  exp_id: eval-k1-crm-accg-object-seed43
1473	    status=DONE  server=bjb1-32546  seed=43  ε=0.2
1474	    n_rollouts=10  total_rollouts=None  SR=0.12
1475	    conclusion=negative
1476	    files: ['/root/acr-vla-conformal-refinement/logs/eval_k1_crm_accg_object_seed43.json', 'logs/eval_k1_crm_accg_object_seed43.json']
1477	    cmd: CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode crm_k1_accg --benchmark object --n_rollouts 10 --seed 43 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt --max_correction_no...
1478	    hypothesis: K=1 CRM with ACCG (fallback 960D) on LIBERO-Object seed43. 验证 ACCG correction 是否优于 K=1 VLA-only baseline (mean 10.8%). Parent: train-crm-k1-accg-objec
1479	
1480	  exp_id: eval-k1-crm-multiscale-object-seed43
1481	    status=DONE  server=bjb1-32546  seed=43  ε=0.2
1482	    n_rollouts=10  total_rollouts=None  SR=N/A
1483	    conclusion=negative
1484	    files: ['logs/eval_k1_crm_multiscale_object_seed43.log']
1485	    cmd: CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --mode crm_k1_accg --benchmark object --n_rollouts 10 --seed 43 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_k1/crm_k1_best_multiscale.pt --max_co...
1486	    hypothesis: K=1 CRM with ACCG (multi-scale 4x960D from layers [3,7,11,15]) on LIBERO-Object seed43. Compare with fallback (single-stage) and VLA-only baseline (10
1487	
1488	  exp_id: eval-k1-crm-multiscale-object-seed43-r2
1489	    status=DONE  server=bjb1-18228  seed=43  ε=0.2
1490	    n_rollouts=10  total_rollouts=None  SR=N/A
1491	    conclusion=negative
1492	    files: ['logs/eval_k1_crm_multiscale_object_seed43_bjb1-18228.json']
1493	    cmd: CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --mode crm_k1_accg --benchmark object --n_rollouts 10 --seed 43 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt --max_correction_no...
1494	    hypothesis: K=1 CRM with ACCG (multi-scale 4×960D) on LIBERO-Object seed43. Parallel deployment on bjb1-18228. Parent: train-crm-k1-accg-object-seed42-v2
1495	
1496	  exp_id: eval-random-selection-object-seed44
1497	    status=RUNNING  server=bjb2-28827  seed=44
1498	    n_rollouts=None  total_rollouts=None  SR=N/A
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LkyHAJXMgM6jYEjtYbJhsT",
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "26dd2a3d-dd72-4933-adce-b10c030fe8a2"
}
```

</details>

---


### System

_source line 54_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a11f7ce8b039566e8",
  "tool_use_id": "toolu_01T2M7sUsRh3qbz75T18NDYF",
  "status": "completed",
  "output_file": "",
  "summary": "Read magnitude curve data",
  "usage": {
    "total_tokens": 25915,
    "tool_uses": 4,
    "duration_ms": 78821
  },
  "uuid": "4fa0c74e-ce82-4e23-a2bb-955c8055e30a",
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d"
}
```

---


### Tool result

_source line 55 · 2026-05-18T10:44:40.941Z_

<details><summary>↩ Tool result · `toolu_01T2M7sUsRh3qbz75T18NDYF`</summary>

````text
Here are the full contents of all four files.

---

## File 1: `_project/data/magnitude_curve_data.json`

**Metadata:**
- Benchmark: LIBERO Object
- n_tasks: 10, n_rollouts_per_task: 10, total_per_seed: 100
- Compiled date: 2026-05-16

**magnitude_curve (Object benchmark):**

| Mode | norm | SR | successes | total | exp_id | seed | note |
|------|------|----|-----------|-------|--------|------|------|
| obs_only | 0.03 | 0.16 | 16 | 100 | eval-mag-obsonly-norm003-object | 42 | |
| obs_only | 0.05 | 0.13 | 13 | 100 | eval-mag-obsonly-norm005-object | 42 | |
| obs_only | 0.10 | 0.19 | 19 | 100 | eval-acr-object-v4-obs-only | 42 | |
| obs_only | 0.20 | 0.22 | 22 | 100 | eval-acr-object-obs-only-norm02 | 42 | |
| obs_only | 0.30 | 0.19 | 19 | 100 | eval-mag-obsonly-norm03-object | 42 | |
| obs_only | 1.42 | 0.17 | 17 | 100 | eval-acr-object-obs-only-default | 42 | default norm, no clipping |
| perdof | 0.03 | 0.14 | 14 | 100 | eval-mag-perdof-norm003-object | 42 | |
| perdof | 0.05 | 0.14 | 14 | 100 | eval-mag-perdof-norm005-object | 42 | |
| perdof | 0.10 | 0.11 | 11 | 100 | eval-acr-object-v4-perdof | 42 | |
| perdof | 0.20 | 0.11 | 11 | 100 | eval-mag-perdof-norm02-object | 42 | |
| perdof | 0.30 | 0.04 | 4 | 100 | eval-mag-perdof-norm03-object-r3 | 42 | |
| perdof | 1.42 | 0.00 | 0 | 100 | eval-acr-object-v4-default-r2 | 42 | default norm, catastrophic failure |

**magnitude_curve_spatial:**

| Mode | norm | SR | successes | total | exp_id | seed |
|------|------|----|-----------|-------|--------|------|
| obs_only | 0.03 | 0.34 | 34 | 100 | eval-mag-obsonly-norm003-b2 | 42 |
| obs_only | 0.05 | 0.35 | 35 | 100 | eval-mag-obsonly-norm005 | 42 |
| obs_only | 0.10 | 0.35 | 35 | 100 | eval-acr-spatial-v4-obs-only-r3 | 42 |
| obs_only | 0.20 | 0.35 | 35 | 100 | eval-mag-obsonly-norm02 | 42 |
| obs_only | 0.30 | 0.36 | 36 | 100 | eval-mag-obsonly-norm03-r2 | 42 |
| perdof | 0.03 | 0.30 | 30 | 100 | eval-mag-perdof-norm003 | 42 |
| perdof | 0.05 | 0.31 | 31 | 100 | eval-mag-perdof-norm005 | 42 |
| perdof | 0.10 | 0.35 | 35 | 100 | eval-acr-spatial-v4-small-r2 | 42 |
| perdof | 0.30 | 0.26 | 26 | 100 | eval-mag-perdof-norm03 | 42 |

**baselines:**

Object baselines:
- argmin (seed 42): SR=0.12, 12/100, exp_id=eval-reconvla-object
- vla_only (seed 42): SR=0.12, 12/100, exp_id=eval-vla-only-object
- vla_mean (seed 42): SR=0.12, 12/100, exp_id=eval-vla-mean-object

Spatial baselines:
- argmin (seed 42): SR=0.34, 34/100, exp_id=eval-argmin-only-spatial-r2
- vla_only (seed 42): SR=0.30, 30/100, exp_id=eval-spatial-v7-full
- vla_mean (seed 42): SR=0.32, 32/100, exp_id=eval-vla-mean-spatial

**seed_comparison:**

obs_only_norm02:
- seed 42: SR=0.22, 22/100 (eval-acr-object-obs-only-norm02)
- seed 43: SR=0.16, 16/100 (eval-obs-only-object-norm02-seed43-r2)
- seed 44: SR=0.16, 16/100 (eval-obs-only-object-norm02-seed44-r2)

obs_only_norm01:
- seed 42: SR=0.19, 19/100 (eval-acr-object-v4-obs-only)
- seed 43: SR=0.12, 12/100 (eval-obs-only-object-seed43)

argmin:
- seed 42: SR=0.12, 12/100 (eval-reconvla-object)
- seed 43: SR=0.17, 17/100 (eval-argmin-object-seed43)
- seed 44: SR=0.13, 13/100 (eval-argmin-object-seed44-r2)

perdof_norm01:
- seed 42: SR=0.11, 11/100 (eval-acr-object-v4-perdof)
- seed 43: SR=0.12, 12/100 (eval-perdof-object-seed43)

perdof_norm02:
- seed 42: SR=0.11, 11/100 (eval-mag-perdof-norm02-object)
- seed 43: SR=0.09, 9/100 (eval-mag-perdof-norm02-seed43-object-r3)

vla_only:
- seed 42: SR=0.12, 12/100 (eval-vla-only-object)
- seed 43: SR=0.12, 12/100 (eval-vla-only-object-seed43)
- seed 44: SR=0.10, 10/100 (eval-vla-only-object-seed44-r2)

vla_mean:
- seed 42: SR=0.12, 12/100 (eval-vla-mean-object)
- seed 43: SR=0.15, 15/100 (eval-vla-mean-object-seed43)
- seed 44: SR=0.10, 10/100 (eval-vla-mean-object-seed44)

---

## File 2: `artifacts/magnitude_curve_data.json`

This is the most comprehensive file, with multi-seed data and source file paths. Collected at `2026-05-18T05:55:00`, from servers: bjb2-28827, bjb1-32546, bjb1-18228, bjb2-40593.

**obs_only:**

| epsilon | seed | SR |
|---------|------|----|
| 0.03 | 42 | 0.16 |
| 0.05 | 42 | 0.13 |
| 0.05 | 43 | 0.14 |
| 0.1 | 42 | 0.19 |
| 0.1 | 43 | 0.12 |
| 0.1 | 44 | 0.16 |
| 0.1 | 45 | 0.14 |
| 0.2 | 42 | 0.22 |
| 0.2 | 43 | 0.16 |
| 0.2 | 44 | 0.16 |
| 0.2 | 45 | 0.16 |
| 0.2 | 46 | 0.15 |
| 0.2 | 47 | 0.20 |
| 0.3 | 42 | 0.19 |
| 0.3 | 44 | 0.18 |
| 0.3 | 45 | 0.14 |
| 0.3 | 46 | 0.17 |
| default | 44 | 0.16 |
| default | 45 | 0.12 |
| default | 46 | 0.15 |

Aggregated stats:
- 0.03: mean=0.16, std=0.0, n=1
- 0.05: mean=0.135, std=0.0071, n=2
- 0.1: mean=0.1525, std=0.0299, n=4
- 0.2: mean=0.175, std=0.0281, n=6
- 0.3: mean=0.17, std=0.0216, n=4
- default: mean=0.1433, std=0.0208, n=3

**perdof:**

| epsilon | seed | SR |
|---------|------|----|
| 0.03 | 42 | 0.14 |
| 0.05 | 42 | 0.14 |
| 0.1 | 42 | 0.11 |
| 0.1 | 43 | 0.12 |
| 0.1 | 44 | 0.08 |
| 0.1 | 45 | 0.11 |
| 0.1 | 46 | 0.10 |
| 0.1 | 47 | 0.14 |
| 0.2 | 42 | 0.11 |
| 0.2 | 43 | 0.09 |
| 0.2 | 44 | 0.10 |
| 0.2 | 45 | 0.09 |
| 0.2 | 46 | 0.09 |
| 0.2 | 47 | 0.11 |
| 0.3 | 42 | 0.04 |
| 0.3 | 44 | 0.04 |
| 0.3 | 45 | 0.06 |
| default | 42 | 0.00 |
| default | 44 | 0.00 |
| default | 46 | 0.00 |

Aggregated stats:
- 0.03: mean=0.14, std=0.0, n=1
- 0.05: mean=0.14, std=0.0, n=1
- 0.1: mean=0.11, std=0.02, n=6
- 0.2: mean=0.0983, std=0.0098, n=6
- 0.3: mean=0.0467, std=0.0115, n=3
- default: mean=0.0, std=0.0, n=3 (notes: seed42 from eval-perdof-object-default-seed42-r2, full 10/10 tasks; seed44 partial 9/10 tasks, 0/90 rollouts, timeout EXIT_CODE=124; seed46 from eval-perdof-object-default-seed46, full 10/10 tasks)

**baselines:**

| Method | seed | SR |
|--------|------|----|
| vla_only | 42 | 0.12 |
| vla_only | 43 | 0.12 |
| vla_only | 44 | 0.10 |
| vla_only | 45 | 0.09 |
| vla_only | 46 | 0.13 |
| vla_mean | 42 | 0.12 |
| vla_mean | 43 | 0.15 |
| vla_mean | 44 | 0.10 |
| vla_mean | 45 | 0.13 |
| reconvla | 42 | 0.12 |
| reconvla | 43 | 0.17 |
| reconvla | 44 | 0.13 |
| reconvla | 46 | 0.10 |
| reconvla | 47 | 0.10 |
| argmin | 45 | 0.12 |
| scalar | 42 | 0.09 |
| scalar | 43 | 0.10 |
| scalar | 44 | 0.06 |
| scalar | 45 | 0.09 |
| k1_accg | 42 | 0.11 |
| k1_accg | 43 | 0.12 |
| k1_accg | 44 | 0.07 |
| k1_multiscale | 42 | 0.12 |
| k1_multiscale | 43 | 0.09 |
| k1_multiscale | 44 | 0.10 |

Baseline aggregated stats:
- vla_only: mean=0.112, std=0.0164, n=5
- vla_mean: mean=0.125, std=0.0208, n=4
- reconvla: mean=0.124, std=0.0288, n=5
- argmin: mean=0.12, std=0.0, n=1
- scalar: mean=0.085, std=0.0173, n=4 (note: seed42 from eval-acr-object-v4-scalar on bjb1-32546, max_correction_norm=0.1; seed45 uses 20 rollouts/task instead of 10)
- k1_accg: mean=0.1, std=0.0265, n=3
- k1_multiscale: mean=0.1033, std=0.0153, n=3

**sources_detail** (source file paths per seed per epsilon):

obs_only:
- 0.03/42: bjb1-32546:eval_object_obs_only_norm003.json
- 0.05/42: bjb2-28827:eval_object_obs_only_norm005.json
- 0.05/43: bjb1-32546:eval_object_obs_only_norm005_seed43_r2.json
- 0.1/42: bjb1-32546:eval_object_obs_only.json (actual norm=0.1 per log)
- 0.1/43: bjb1-18228:eval_object_obs_only_seed43.json (actual norm=0.1 per log)
- 0.1/44: bjb1-32546:eval_object_obs_only_norm01_seed44.json
- 0.1/45: bjb1-18228:eval_object_obs_only_norm01_seed45.json
- 0.2/42: bjb1-32546:eval_object_obs_only_norm02.json
- 0.2/43: bjb1-32546:eval_object_obs_only_norm02_seed43_r2.json
- 0.2/44: bjb1-18228:eval_object_obs_only_norm02_seed44.json
- 0.2/45: bjb1-32546:eval_object_obs_only_norm02_seed45.json
- 0.2/46: bjb1-18228:eval_object_obs_only_norm02_seed46.json
- 0.2/47: bjb1-32546:eval_object_obs_only_norm02_seed47.json
- 0.3/42: bjb2-28827:eval_object_obs_only_norm03.json
- 0.3/44: bjb1-32546:eval_object_obs_only_norm03_seed44.json
- 0.3/45: bjb2-28827:eval_object_obs_only_norm03_seed45_r2.json
- 0.3/46: bjb1-32546:eval_object_obs_only_norm03_seed46.json
- default/44: bjb1-32546:eval_object_obs_only_default_seed44.json (verified uncapped)
- default/45: bjb2-28827:eval_object_obs_only_default_seed45.json (verified uncapped)
- default/46: bjb1-32546:eval_object_obs_only_default_seed46.json

perdof:
- 0.03/42: bjb2-28827:eval_object_perdof_norm003.json
- 0.05/42: bjb2-28827:eval_object_perdof_norm005.json
- 0.1/42: bjb1-32546:eval_object_perdof.json (actual norm=0.1)
- 0.1/43: bjb1-18228:eval_object_perdof_seed43.json (actual norm=0.1)
- 0.1/44: bjb1-18228:eval_object_perdof_norm01_seed44.json
- 0.1/45: bjb1-32546:eval_object_perdof_norm01_seed45.json
- 0.1/46: bjb1-32546:eval_object_perdof_norm01_seed46.json
- 0.1/47: bjb1-32546:eval_object_perdof_norm01_seed47_r2.json
- 0.2/42: bjb1-32546:eval_object_perdof_norm02.json
- 0.2/43: bjb2-28827:eval_object_perdof_norm02_seed43_r3.json
- 0.2/44: bjb2-28827:eval_object_perdof_norm02_seed44.json
- 0.2/45: bjb2-28827:eval_object_perdof_norm02_seed45.json
- 0.2/46: bjb2-28827:eval_object_perdof_norm02_seed46.json
- 0.2/47: bjb2-28827:eval_object_perdof_norm02_seed47.json
- 0.3/42: bjb2-28827:eval_object_perdof_norm03_r3.json
- 0.3/44: bjb1-18228:eval_object_perdof_norm03_seed44.json
- 0.3/45: bjb1-32546:eval_object_perdof_norm03_seed45_r2.json
- default/42: bjb1-18228:eval_object_perdof_default_norm_r2.json
- default/44: partial (9/10 tasks, 0/90 rollouts, timeout)
- default/46: bjb1-32546:eval_object_perdof_default_seed46.json

**Key notes from the file:**
- obs_only "default" seed42/43 were reclassified to epsilon=0.1 per log verification (Reviewer Report #22)
- perdof "default" seed42/43/44 were reclassified to epsilon=0.1 (Reviewer Report #20); perdof uncapped now has seed42-r2=0%, seed44=0%(partial), seed46=0% (n=3)
- eval_openvla_object_vla_only_seed42.json (OpenVLA model, 0% SR) excluded as different model
- K=5 variant (eval_object_obs_only_norm02_k5_seed42.json, SR=0.14) excluded from main curve
- bjb2-40593 duplicate of seed42 on bjb1-32546, not counted twice

---

## File 3: `artifacts/figures/magnitude_sweep_summary.json`

This file is minimal and contains only spatial baselines with empty sweep data:

```json
{
  "baselines": {
    "argmin": 0.34,
    "vla_only": 0.3,
    "vla_mean": 0.32
  },
  "perdof": {},
  "obs_only": {}
}
```

The `perdof` and `obs_only` dictionaries are empty. Only three spatial baselines are recorded.

---

## File 4: `artifacts/figures/object_benchmark_data.json`

Per-task success rates (in %) and overall SR for 7 methods on 10 LIBERO Object tasks, all seed 42:

| Method | alphabet_soup | cream_cheese | salad_dressing | bbq_sauce | ketchup | tomato_sauce | butter | milk | chocolate_pudding | orange_juice | Overall SR | exp_id |
|--------|--------------|--------------|----------------|-----------|---------|--------------|--------|------|-------------------|--------------|------------|--------|
| VLA-only | 0 | 10 | 20 | 20 | 0 | 10 | 0 | 10 | 20 | 30 | 12.0 | eval-vla-only-object |
| VLA-mean | 0 | 0 | 10 | 30 | 10 | 10 | 0 | 20 | 30 | 10 | 12.0 | eval-vla-mean-object |
| ReconVLA | 0 | 0 | 10 | 30 | 0 | 0 | 10 | 10 | 30 | 30 | 12.0 | eval-reconvla-object |
| ACR per-DOF | 0 | 0 | 20 | 30 | 0 | 0 | 10 | 0 | 20 | 30 | 11.0 | eval-acr-object-v4-perdof |
| ACR obs-only | 0 | 10 | 20 | 40 | 10 | 0 | 10 | 20 | 50 | 30 | 19.0 | eval-acr-object-v4-obs-only |
| ACR scalar | 0 | 0 | 10 | 10 | 0 | 0 | 10 | 10 | 30 | 20 | 9.0 | eval-acr-object-v4-scalar |
| ACR obs-only-0.2 | 0 | 0 | 30 | 40 | 20 | 10 | 10 | 20 | 60 | 30 | 22.0 | eval-acr-object-obs-only-norm02 |

All methods have n_tasks_completed=10 and status=DONE. These are single-seed (seed 42) results. The best performer is ACR obs-only-0.2 at 22% SR, followed by ACR obs-only at 19%. The three baselines (VLA-only, VLA-mean, ReconVLA) all achieved 12%. ACR scalar performed worst at 9%.

agentId: a11f7ce8b039566e8 (use SendMessage with to: 'a11f7ce8b039566e8' to continue this agent)
&lt;usage>total_tokens: 31907
tool_uses: 4
duration_ms: 78823&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "f0069e31-8001-4c06-84ad-8d16a76b7479",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Read these JSON data files and report their full contents:\n\n1. /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/data/magnitude_curve_data.json\n2. /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/magnitude_curve_data.json\n3. /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/figures/magnitude_sweep_summary.json\n4. /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/figures/object_benchmark_data.json\n\nReport the full contents of each file, especially:\n- For magnitude curve data: all epsilon values, seeds, SR values, n_rollouts if present, and source file paths\n- For object benchmark data: all methods, seeds, SR values\n\nBe thorough - report every data point.",
    "agentId": "a11f7ce8b039566e8",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are the full contents of all four files.\n\n---\n\n## File 1: `_project/data/magnitude_curve_data.json`\n\n**Metadata:**\n- Benchmark: LIBERO Object\n- n_tasks: 10, n_rollouts_per_task: 10, total_per_seed: 100\n- Compiled date: 2026-05-16\n\n**magnitude_curve (Object benchmark):**\n\n| Mode | norm | SR | successes | total | exp_id | seed | note |\n|------|------|----|-----------|-------|--------|------|------|\n| obs_only | 0.03 | 0.16 | 16 | 100 | eval-mag-obsonly-norm003-object | 42 | |\n| obs_only | 0.05 | 0.13 | 13 | 100 | eval-mag-obsonly-norm005-object | 42 | |\n| obs_only | 0.10 | 0.19 | 19 | 100 | eval-acr-object-v4-obs-only | 42 | |\n| obs_only | 0.20 | 0.22 | 22 | 100 | eval-acr-object-obs-only-norm02 | 42 | |\n| obs_only | 0.30 | 0.19 | 19 | 100 | eval-mag-obsonly-norm03-object | 42 | |\n| obs_only | 1.42 | 0.17 | 17 | 100 | eval-acr-object-obs-only-default | 42 | default norm, no clipping |\n| perdof | 0.03 | 0.14 | 14 | 100 | eval-mag-perdof-norm003-object | 42 | |\n| perdof | 0.05 | 0.14 | 14 | 100 | eval-mag-perdof-norm005-object | 42 | |\n| perdof | 0.10 | 0.11 | 11 | 100 | eval-acr-object-v4-perdof | 42 | |\n| perdof | 0.20 | 0.11 | 11 | 100 | eval-mag-perdof-norm02-object | 42 | |\n| perdof | 0.30 | 0.04 | 4 | 100 | eval-mag-perdof-norm03-object-r3 | 42 | |\n| perdof | 1.42 | 0.00 | 0 | 100 | eval-acr-object-v4-default-r2 | 42 | default norm, catastrophic failure |\n\n**magnitude_curve_spatial:**\n\n| Mode | norm | SR | successes | total | exp_id | seed |\n|------|------|----|-----------|-------|--------|------|\n| obs_only | 0.03 | 0.34 | 34 | 100 | eval-mag-obsonly-norm003-b2 | 42 |\n| obs_only | 0.05 | 0.35 | 35 | 100 | eval-mag-obsonly-norm005 | 42 |\n| obs_only | 0.10 | 0.35 | 35 | 100 | eval-acr-spatial-v4-obs-only-r3 | 42 |\n| obs_only | 0.20 | 0.35 | 35 | 100 | eval-mag-obsonly-norm02 | 42 |\n| obs_only | 0.30 | 0.36 | 36 | 100 | eval-mag-obsonly-norm03-r2 | 42 |\n| perdof | 0.03 | 0.30 | 30 | 100 | eval-mag-perdof-norm003 | 42 |\n| perdof | 0.05 | 0.31 | 31 | 100 | eval-mag-perdof-norm005 | 42 |\n| perdof | 0.10 | 0.35 | 35 | 100 | eval-acr-spatial-v4-small-r2 | 42 |\n| perdof | 0.30 | 0.26 | 26 | 100 | eval-mag-perdof-norm03 | 42 |\n\n**baselines:**\n\nObject baselines:\n- argmin (seed 42): SR=0.12, 12/100, exp_id=eval-reconvla-object\n- vla_only (seed 42): SR=0.12, 12/100, exp_id=eval-vla-only-object\n- vla_mean (seed 42): SR=0.12, 12/100, exp_id=eval-vla-mean-object\n\nSpatial baselines:\n- argmin (seed 42): SR=0.34, 34/100, exp_id=eval-argmin-only-spatial-r2\n- vla_only (seed 42): SR=0.30, 30/100, exp_id=eval-spatial-v7-full\n- vla_mean (seed 42): SR=0.32, 32/100, exp_id=eval-vla-mean-spatial\n\n**seed_comparison:**\n\nobs_only_norm02:\n- seed 42: SR=0.22, 22/100 (eval-acr-object-obs-only-norm02)\n- seed 43: SR=0.16, 16/100 (eval-obs-only-object-norm02-seed43-r2)\n- seed 44: SR=0.16, 16/100 (eval-obs-only-object-norm02-seed44-r2)\n\nobs_only_norm01:\n- seed 42: SR=0.19, 19/100 (eval-acr-object-v4-obs-only)\n- seed 43: SR=0.12, 12/100 (eval-obs-only-object-seed43)\n\nargmin:\n- seed 42: SR=0.12, 12/100 (eval-reconvla-object)\n- seed 43: SR=0.17, 17/100 (eval-argmin-object-seed43)\n- seed 44: SR=0.13, 13/100 (eval-argmin-object-seed44-r2)\n\nperdof_norm01:\n- seed 42: SR=0.11, 11/100 (eval-acr-object-v4-perdof)\n- seed 43: SR=0.12, 12/100 (eval-perdof-object-seed43)\n\nperdof_norm02:\n- seed 42: SR=0.11, 11/100 (eval-mag-perdof-norm02-object)\n- seed 43: SR=0.09, 9/100 (eval-mag-perdof-norm02-seed43-object-r3)\n\nvla_only:\n- seed 42: SR=0.12, 12/100 (eval-vla-only-object)\n- seed 43: SR=0.12, 12/100 (eval-vla-only-object-seed43)\n- seed 44: SR=0.10, 10/100 (eval-vla-only-object-seed44-r2)\n\nvla_mean:\n- seed 42: SR=0.12, 12/100 (eval-vla-mean-object)\n- seed 43: SR=0.15, 15/100 (eval-vla-mean-object-seed43)\n- seed 44: SR=0.10, 10/100 (eval-vla-mean-object-seed44)\n\n---\n\n## File 2: `artifacts/magnitude_curve_data.json`\n\nThis is the most comprehensive file, with multi-seed data and source file paths. Collected at `2026-05-18T05:55:00`, from servers: bjb2-28827, bjb1-32546, bjb1-18228, bjb2-40593.\n\n**obs_only:**\n\n| epsilon | seed | SR |\n|---------|------|----|\n| 0.03 | 42 | 0.16 |\n| 0.05 | 42 | 0.13 |\n| 0.05 | 43 | 0.14 |\n| 0.1 | 42 | 0.19 |\n| 0.1 | 43 | 0.12 |\n| 0.1 | 44 | 0.16 |\n| 0.1 | 45 | 0.14 |\n| 0.2 | 42 | 0.22 |\n| 0.2 | 43 | 0.16 |\n| 0.2 | 44 | 0.16 |\n| 0.2 | 45 | 0.16 |\n| 0.2 | 46 | 0.15 |\n| 0.2 | 47 | 0.20 |\n| 0.3 | 42 | 0.19 |\n| 0.3 | 44 | 0.18 |\n| 0.3 | 45 | 0.14 |\n| 0.3 | 46 | 0.17 |\n| default | 44 | 0.16 |\n| default | 45 | 0.12 |\n| default | 46 | 0.15 |\n\nAggregated stats:\n- 0.03: mean=0.16, std=0.0, n=1\n- 0.05: mean=0.135, std=0.0071, n=2\n- 0.1: mean=0.1525, std=0.0299, n=4\n- 0.2: mean=0.175, std=0.0281, n=6\n- 0.3: mean=0.17, std=0.0216, n=4\n- default: mean=0.1433, std=0.0208, n=3\n\n**perdof:**\n\n| epsilon | seed | SR |\n|---------|------|----|\n| 0.03 | 42 | 0.14 |\n| 0.05 | 42 | 0.14 |\n| 0.1 | 42 | 0.11 |\n| 0.1 | 43 | 0.12 |\n| 0.1 | 44 | 0.08 |\n| 0.1 | 45 | 0.11 |\n| 0.1 | 46 | 0.10 |\n| 0.1 | 47 | 0.14 |\n| 0.2 | 42 | 0.11 |\n| 0.2 | 43 | 0.09 |\n| 0.2 | 44 | 0.10 |\n| 0.2 | 45 | 0.09 |\n| 0.2 | 46 | 0.09 |\n| 0.2 | 47 | 0.11 |\n| 0.3 | 42 | 0.04 |\n| 0.3 | 44 | 0.04 |\n| 0.3 | 45 | 0.06 |\n| default | 42 | 0.00 |\n| default | 44 | 0.00 |\n| default | 46 | 0.00 |\n\nAggregated stats:\n- 0.03: mean=0.14, std=0.0, n=1\n- 0.05: mean=0.14, std=0.0, n=1\n- 0.1: mean=0.11, std=0.02, n=6\n- 0.2: mean=0.0983, std=0.0098, n=6\n- 0.3: mean=0.0467, std=0.0115, n=3\n- default: mean=0.0, std=0.0, n=3 (notes: seed42 from eval-perdof-object-default-seed42-r2, full 10/10 tasks; seed44 partial 9/10 tasks, 0/90 rollouts, timeout EXIT_CODE=124; seed46 from eval-perdof-object-default-seed46, full 10/10 tasks)\n\n**baselines:**\n\n| Method | seed | SR |\n|--------|------|----|\n| vla_only | 42 | 0.12 |\n| vla_only | 43 | 0.12 |\n| vla_only | 44 | 0.10 |\n| vla_only | 45 | 0.09 |\n| vla_only | 46 | 0.13 |\n| vla_mean | 42 | 0.12 |\n| vla_mean | 43 | 0.15 |\n| vla_mean | 44 | 0.10 |\n| vla_mean | 45 | 0.13 |\n| reconvla | 42 | 0.12 |\n| reconvla | 43 | 0.17 |\n| reconvla | 44 | 0.13 |\n| reconvla | 46 | 0.10 |\n| reconvla | 47 | 0.10 |\n| argmin | 45 | 0.12 |\n| scalar | 42 | 0.09 |\n| scalar | 43 | 0.10 |\n| scalar | 44 | 0.06 |\n| scalar | 45 | 0.09 |\n| k1_accg | 42 | 0.11 |\n| k1_accg | 43 | 0.12 |\n| k1_accg | 44 | 0.07 |\n| k1_multiscale | 42 | 0.12 |\n| k1_multiscale | 43 | 0.09 |\n| k1_multiscale | 44 | 0.10 |\n\nBaseline aggregated stats:\n- vla_only: mean=0.112, std=0.0164, n=5\n- vla_mean: mean=0.125, std=0.0208, n=4\n- reconvla: mean=0.124, std=0.0288, n=5\n- argmin: mean=0.12, std=0.0, n=1\n- scalar: mean=0.085, std=0.0173, n=4 (note: seed42 from eval-acr-object-v4-scalar on bjb1-32546, max_correction_norm=0.1; seed45 uses 20 rollouts/task instead of 10)\n- k1_accg: mean=0.1, std=0.0265, n=3\n- k1_multiscale: mean=0.1033, std=0.0153, n=3\n\n**sources_detail** (source file paths per seed per epsilon):\n\nobs_only:\n- 0.03/42: bjb1-32546:eval_object_obs_only_norm003.json\n- 0.05/42: bjb2-28827:eval_object_obs_only_norm005.json\n- 0.05/43: bjb1-32546:eval_object_obs_only_norm005_seed43_r2.json\n- 0.1/42: bjb1-32546:eval_object_obs_only.json (actual norm=0.1 per log)\n- 0.1/43: bjb1-18228:eval_object_obs_only_seed43.json (actual norm=0.1 per log)\n- 0.1/44: bjb1-32546:eval_object_obs_only_norm01_seed44.json\n- 0.1/45: bjb1-18228:eval_object_obs_only_norm01_seed45.json\n- 0.2/42: bjb1-32546:eval_object_obs_only_norm02.json\n- 0.2/43: bjb1-32546:eval_object_obs_only_norm02_seed43_r2.json\n- 0.2/44: bjb1-18228:eval_object_obs_only_norm02_seed44.json\n- 0.2/45: bjb1-32546:eval_object_obs_only_norm02_seed45.json\n- 0.2/46: bjb1-18228:eval_object_obs_only_norm02_seed46.json\n- 0.2/47: bjb1-32546:eval_object_obs_only_norm02_seed47.json\n- 0.3/42: bjb2-28827:eval_object_obs_only_norm03.json\n- 0.3/44: bjb1-32546:eval_object_obs_only_norm03_seed44.json\n- 0.3/45: bjb2-28827:eval_object_obs_only_norm03_seed45_r2.json\n- 0.3/46: bjb1-32546:eval_object_obs_only_norm03_seed46.json\n- default/44: bjb1-32546:eval_object_obs_only_default_seed44.json (verified uncapped)\n- default/45: bjb2-28827:eval_object_obs_only_default_seed45.json (verified uncapped)\n- default/46: bjb1-32546:eval_object_obs_only_default_seed46.json\n\nperdof:\n- 0.03/42: bjb2-28827:eval_object_perdof_norm003.json\n- 0.05/42: bjb2-28827:eval_object_perdof_norm005.json\n- 0.1/42: bjb1-32546:eval_object_perdof.json (actual norm=0.1)\n- 0.1/43: bjb1-18228:eval_object_perdof_seed43.json (actual norm=0.1)\n- 0.1/44: bjb1-18228:eval_object_perdof_norm01_seed44.json\n- 0.1/45: bjb1-32546:eval_object_perdof_norm01_seed45.json\n- 0.1/46: bjb1-32546:eval_object_perdof_norm01_seed46.json\n- 0.1/47: bjb1-32546:eval_object_perdof_norm01_seed47_r2.json\n- 0.2/42: bjb1-32546:eval_object_perdof_norm02.json\n- 0.2/43: bjb2-28827:eval_object_perdof_norm02_seed43_r3.json\n- 0.2/44: bjb2-28827:eval_object_perdof_norm02_seed44.json\n- 0.2/45: bjb2-28827:eval_object_perdof_norm02_seed45.json\n- 0.2/46: bjb2-28827:eval_object_perdof_norm02_seed46.json\n- 0.2/47: bjb2-28827:eval_object_perdof_norm02_seed47.json\n- 0.3/42: bjb2-28827:eval_object_perdof_norm03_r3.json\n- 0.3/44: bjb1-18228:eval_object_perdof_norm03_seed44.json\n- 0.3/45: bjb1-32546:eval_object_perdof_norm03_seed45_r2.json\n- default/42: bjb1-18228:eval_object_perdof_default_norm_r2.json\n- default/44: partial (9/10 tasks, 0/90 rollouts, timeout)\n- default/46: bjb1-32546:eval_object_perdof_default_seed46.json\n\n**Key notes from the file:**\n- obs_only \"default\" seed42/43 were reclassified to epsilon=0.1 per log verification (Reviewer Report #22)\n- perdof \"default\" seed42/43/44 were reclassified to epsilon=0.1 (Reviewer Report #20); perdof uncapped now has seed42-r2=0%, seed44=0%(partial), seed46=0% (n=3)\n- eval_openvla_object_vla_only_seed42.json (OpenVLA model, 0% SR) excluded as different model\n- K=5 variant (eval_object_obs_only_norm02_k5_seed42.json, SR=0.14) excluded from main curve\n- bjb2-40593 duplicate of seed42 on bjb1-32546, not counted twice\n\n---\n\n## File 3: `artifacts/figures/magnitude_sweep_summary.json`\n\nThis file is minimal and contains only spatial baselines with empty sweep data:\n\n```json\n{\n  \"baselines\": {\n    \"argmin\": 0.34,\n    \"vla_only\": 0.3,\n    \"vla_mean\": 0.32\n  },\n  \"perdof\": {},\n  \"obs_only\": {}\n}\n```\n\nThe `perdof` and `obs_only` dictionaries are empty. Only three spatial baselines are recorded.\n\n---\n\n## File 4: `artifacts/figures/object_benchmark_data.json`\n\nPer-task success rates (in %) and overall SR for 7 methods on 10 LIBERO Object tasks, all seed 42:\n\n| Method | alphabet_soup | cream_cheese | salad_dressing | bbq_sauce | ketchup | tomato_sauce | butter | milk | chocolate_pudding | orange_juice | Overall SR | exp_id |\n|--------|--------------|--------------|----------------|-----------|---------|--------------|--------|------|-------------------|--------------|------------|--------|\n| VLA-only | 0 | 10 | 20 | 20 | 0 | 10 | 0 | 10 | 20 | 30 | 12.0 | eval-vla-only-object |\n| VLA-mean | 0 | 0 | 10 | 30 | 10 | 10 | 0 | 20 | 30 | 10 | 12.0 | eval-vla-mean-object |\n| ReconVLA | 0 | 0 | 10 | 30 | 0 | 0 | 10 | 10 | 30 | 30 | 12.0 | eval-reconvla-object |\n| ACR per-DOF | 0 | 0 | 20 | 30 | 0 | 0 | 10 | 0 | 20 | 30 | 11.0 | eval-acr-object-v4-perdof |\n| ACR obs-only | 0 | 10 | 20 | 40 | 10 | 0 | 10 | 20 | 50 | 30 | 19.0 | eval-acr-object-v4-obs-only |\n| ACR scalar | 0 | 0 | 10 | 10 | 0 | 0 | 10 | 10 | 30 | 20 | 9.0 | eval-acr-object-v4-scalar |\n| ACR obs-only-0.2 | 0 | 0 | 30 | 40 | 20 | 10 | 10 | 20 | 60 | 30 | 22.0 | eval-acr-object-obs-only-norm02 |\n\nAll methods have n_tasks_completed=10 and status=DONE. These are single-seed (seed 42) results. The best performer is ACR obs-only-0.2 at 22% SR, followed by ACR obs-only at 19%. The three baselines (VLA-only, VLA-mean, ReconVLA) all achieved 12%. ACR scalar performed worst at 9%."
      }
    ],
    "totalDurationMs": 78823,
    "totalTokens": 31907,
    "totalToolUseCount": 4,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10229,
      "cache_read_input_tokens": 15649,
      "output_tokens": 6028,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10229
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6028,
          "cache_read_input_tokens": 15649,
          "cache_creation_input_tokens": 10229,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10229,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 4,
      "searchCount": 0,
      "bashCount": 0,
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


### System

_source line 56_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5dc54df06c763762",
  "tool_use_id": "toolu_01LkyHAJXMgM6jYEjtYbJhsT",
  "description": "Running Extract and categorize all eval experiments with structured summary",
  "usage": {
    "total_tokens": 70203,
    "tool_uses": 8,
    "duration_ms": 172067
  },
  "last_tool_name": "Bash",
  "uuid": "d0c17ead-54dd-4025-a99e-b5290b3739ee",
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d"
}
```

---


### Tool call

_source line 57_

<details open><summary>🔧 Tool call — Bash · `toolu_015QEEfooZ8QyBhWXbc4Xnt2`</summary>

```json
{
  "command": "cat << 'PYEOF' > /tmp/extract_final.py\nimport json\nimport re\n\nREGISTRY_FILE = \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/c1bdccab-16c6-497c-9d30-0feab97d927d/tool-results/mcp-agent-ml-research-read_registry-1779100984736.txt\"\n\nwith open(REGISTRY_FILE, 'r') as f:\n    raw = json.load(f)\n\ndata = json.loads(raw[\"result\"])\nexperiments = data[\"data\"][\"experiments\"]\n\ndef get(exp, *keys, default=None):\n    \"\"\"Nested get\"\"\"\n    obj = exp\n    for k in keys:\n        if isinstance(obj, dict):\n            obj = obj.get(k, default)\n        else:\n            return default\n    return obj\n\ndef extract_from_cmd(cmd, flag):\n    if not cmd: return None\n    m = re.search(rf'{flag}\\s+(\\S+)', cmd)\n    return m.group(1) if m else None\n\ndef get_seed(eid, exp):\n    s = get(exp, 'spec', 'seed')\n    if s is not None: return int(s)\n    cmd = get(exp, 'spec', 'command', default='')\n    v = extract_from_cmd(cmd, '--seed')\n    if v: return int(v)\n    m = re.search(r'seed(\\d+)', eid)\n    if m: return int(m.group(1))\n    return None\n\ndef get_nrollouts(eid, exp):\n    cmd = get(exp, 'spec', 'command', default='')\n    v = extract_from_cmd(cmd, '--n_rollouts')\n    if v: return int(v)\n    ed = get(exp, 'spec', 'eval_data', default='')\n    m = re.search(r'(\\d+)\\s*rollouts', ed)\n    if m: return int(m.group(1))\n    return None\n\ndef get_eps(eid, exp):\n    cmd = get(exp, 'spec', 'command', default='')\n    v = extract_from_cmd(cmd, '--max_correction_norm')\n    if v:\n        try: return float(v)\n        except: pass\n    norm_map = {\"norm003\": 0.03, \"norm005\": 0.05, \"norm01\": 0.1, \"norm02\": 0.2, \"norm03\": 0.3, \"norm0p3\": 0.3, \"norm05\": 0.5}\n    for k, val in norm_map.items():\n        if k in eid: return val\n    if \"default\" in eid or \"uncapped\" in eid: return \"uncapped\"\n    return None\n\ndef get_sr(exp):\n    sr = get(exp, 'metrics', 'overall_success_rate')\n    if sr is not None: return sr\n    sr = get(exp, 'metrics', 'success_rate')\n    if sr is not None: return sr\n    return None\n\ndef get_total_rollouts(exp):\n    return get(exp, 'metrics', 'total_rollouts')\n\ndef get_mode(eid, exp):\n    cmd = get(exp, 'spec', 'command', default='')\n    if '--mode crm_obs_only' in cmd or 'crm_obs_only' in cmd:\n        return 'obs_only'\n    if '--mode crm_perdof' in cmd or 'crm_perdof' in cmd:\n        return 'perdof'\n    if '--mode reconvla' in cmd or 'reconvla' in cmd:\n        return 'argmin'\n    if '--mode vla_only' in cmd or 'vla_only' in cmd:\n        return 'vla_only'\n    if '--mode crm_scalar' in cmd or 'crm_scalar' in cmd:\n        return 'scalar'\n    if '--mode acr_vla' in cmd:\n        return 'perdof'  # acr_vla = perdof pipeline\n    # From exp_id\n    if 'obs-only' in eid or 'obsonly' in eid: return 'obs_only'\n    if 'perdof' in eid: return 'perdof'\n    if 'argmin' in eid: return 'argmin'\n    if 'vla-only' in eid or 'vla-mean' in eid: return 'vla_only'\n    if 'scalar' in eid: return 'scalar'\n    if 'reconvla' in eid: return 'argmin'\n    return None\n\ndef get_benchmark(eid, exp):\n    cmd = get(exp, 'spec', 'command', default='')\n    if '--benchmark object' in cmd: return 'object'\n    if '--benchmark spatial' in cmd: return 'spatial'\n    if 'object' in eid: return 'object'\n    if 'spatial' in eid: return 'spatial'\n    return None\n\ndef get_files(eid, exp):\n    files = []\n    cmd = get(exp, 'spec', 'command', default='')\n    v = extract_from_cmd(cmd, '--output_file')\n    if v: files.append(v)\n    lp = get(exp, 'spec', 'log_path')\n    if lp: files.append(lp)\n    return files\n\n# ======================================================================\n# CATEGORY 1: obs_only ε=0.2 (norm02) — Main paper results K=10\n# Seeds 42-47, benchmark=object, mode=obs_only, ε=0.2\n# ======================================================================\nprint(\"=\" * 110)\nprint(\"  CATEGORY 1: obs_only ε=0.2 (norm02) — Main Paper Results K=10\")\nprint(\"  Expected: 6 seeds (42-47), benchmark=object, mode=crm_obs_only, --max_correction_norm 0.2, --K 10\")\nprint(\"=\" * 110)\n\ncat1 = []\nfor eid, exp in sorted(experiments.items()):\n    if not eid.startswith('eval'): continue\n    mode = get_mode(eid, exp)\n    if mode != 'obs_only': continue\n    eps = get_eps(eid, exp)\n    if eps != 0.2: continue\n    bm = get_benchmark(eid, exp)\n    if bm != 'object': continue\n    seed = get_seed(eid, exp)\n    if seed is None or seed < 42 or seed > 47: continue\n    # Exclude K=5 and K=20 experiments\n    cmd = get(exp, 'spec', 'command', default='')\n    if '--K 5' in cmd or '--K 20' in cmd or 'k5' in eid or 'k20' in eid: continue\n    \n    status = exp.get('status')\n    conclusion = exp.get('conclusion')\n    server = get(exp, 'spec', 'server')\n    nr = get_nrollouts(eid, exp)\n    tr = get_total_rollouts(exp)\n    sr = get_sr(exp)\n    \n    flag = \"\"\n    if nr == 20: flag += \" **n_rollouts=20**\"\n    if tr == 200: flag += \" **total_rollouts=200**\"\n    \n    cat1.append({\n        'eid': eid, 'seed': seed, 'status': status, 'conclusion': conclusion,\n        'server': server, 'nr': nr, 'tr': tr, 'sr': sr, 'flag': flag,\n        'files': get_files(eid, exp), 'cmd': cmd[:200] if cmd else ''\n    })\n\ncat1.sort(key=lambda x: (x['seed'], x['eid']))\nfor e in cat1:\n    sr_s = f\"{e['sr']}\" if e['sr'] is not None else \"N/A\"\n    print(f\"\\n  {e['eid']}\")\n    print(f\"    seed={e['seed']}  status={e['status']}  conclusion={e['conclusion']}  server={e['server']}\")\n    print(f\"    n_rollouts={e['nr']}  total_rollouts={e['tr']}  SR={sr_s}{e['flag']}\")\n    if e['files']: print(f\"    files: {e['files']}\")\n\n# ======================================================================\n# CATEGORY 2: Argmin baseline — seeds 42-47, benchmark=object\n# ======================================================================\nprint(\"\\n\\n\" + \"=\" * 110)\nprint(\"  CATEGORY 2: Argmin Baseline (reconvla mode)\")\nprint(\"  Expected: 6 seeds (42-47), benchmark=object, mode=reconvla, K=10\")\nprint(\"=\" * 110)\n\ncat2 = []\nfor eid, exp in sorted(experiments.items()):\n    if not eid.startswith('eval'): continue\n    mode = get_mode(eid, exp)\n    if mode != 'argmin': continue\n    bm = get_benchmark(eid, exp)\n    if bm != 'object': continue\n    seed = get_seed(eid, exp)\n    if seed is None or seed < 42 or seed > 47: continue\n    \n    status = exp.get('status')\n    conclusion = exp.get('conclusion')\n    server = get(exp, 'spec', 'server')\n    nr = get_nrollouts(eid, exp)\n    tr = get_total_rollouts(exp)\n    sr = get_sr(exp)\n    cmd = get(exp, 'spec', 'command', default='')\n    \n    flag = \"\"\n    if nr == 20: flag += \" **n_rollouts=20**\"\n    if tr == 200: flag += \" **total_rollouts=200**\"\n    \n    cat2.append({\n        'eid': eid, 'seed': seed, 'status': status, 'conclusion': conclusion,\n        'server': server, 'nr': nr, 'tr': tr, 'sr': sr, 'flag': flag,\n        'files': get_files(eid, exp), 'cmd': cmd[:200] if cmd else ''\n    })\n\n# Also look for argmin-only-spatial seed42 since it matches the pattern\nfor eid, exp in sorted(experiments.items()):\n    if not eid.startswith('eval'): continue\n    if 'argmin' not in eid: continue\n    if eid in [e['eid'] for e in cat2]: continue\n    mode = get_mode(eid, exp)\n    seed = get_seed(eid, exp)\n    status = exp.get('status')\n    conclusion = exp.get('conclusion')\n    server = get(exp, 'spec', 'server')\n    nr = get_nrollouts(eid, exp)\n    tr = get_total_rollouts(exp)\n    sr = get_sr(exp)\n    cmd = get(exp, 'spec', 'command', default='')\n    bm = get_benchmark(eid, exp)\n    flag = \"\"\n    if nr == 20: flag += \" **n_rollouts=20**\"\n    if tr == 200: flag += \" **total_rollouts=200**\"\n    cat2.append({\n        'eid': eid, 'seed': seed, 'status': status, 'conclusion': conclusion,\n        'server': server, 'nr': nr, 'tr': tr, 'sr': sr, 'flag': flag,\n        'benchmark': bm,\n        'files': get_files(eid, exp), 'cmd': cmd[:200] if cmd else ''\n    })\n\ncat2.sort(key=lambda x: (x['seed'] or 0, x['eid']))\nfor e in cat2:\n    sr_s = f\"{e['sr']}\" if e['sr'] is not None else \"N/A\"\n    bm_s = f\"  benchmark={e.get('benchmark','object')}\" if e.get('benchmark') != 'object' else \"\"\n    print(f\"\\n  {e['eid']}\")\n    print(f\"    seed={e['seed']}  status={e['status']}  conclusion={e['conclusion']}  server={e['server']}{bm_s}\")\n    print(f\"    n_rollouts={e['nr']}  total_rollouts={e['tr']}  SR={sr_s}{e['flag']}\")\n    if e['files']: print(f\"    files: {e['files']}\")\n\n# ======================================================================\n# CATEGORY 3: VLA-only baseline — seeds 42-46, benchmark=object\n# ======================================================================\nprint(\"\\n\\n\" + \"=\" * 110)\nprint(\"  CATEGORY 3: VLA-Only Baseline\")\nprint(\"  Expected: 5 seeds (42-46), benchmark=object, mode=vla_only\")\nprint(\"=\" * 110)\n\ncat3 = []\nfor eid, exp in sorted(experiments.items()):\n    if not eid.startswith('eval'): continue\n    mode = get_mode(eid, exp)\n    if mode != 'vla_only': continue\n    seed = get_seed(eid, exp)\n    bm = get_benchmark(eid, exp)\n    status = exp.get('status')\n    conclusion = exp.get('conclusion')\n    server = get(exp, 'spec', 'server')\n    nr = get_nrollouts(eid, exp)\n    tr = get_total_rollouts(exp)\n    sr = get_sr(exp)\n    cmd = get(exp, 'spec', 'command', default='')\n    \n    flag = \"\"\n    if nr == 20: flag += \" **n_rollouts=20**\"\n    if tr == 200: flag += \" **total_rollouts=200**\"\n    \n    cat3.append({\n        'eid': eid, 'seed': seed, 'status': status, 'conclusion': conclusion,\n        'server': server, 'nr': nr, 'tr': tr, 'sr': sr, 'flag': flag,\n        'benchmark': bm, 'mode_detail': '',\n        'files': get_files(eid, exp), 'cmd': cmd[:200] if cmd else ''\n    })\n    # Detect vla_mean vs vla_only\n    if '--baseline_mode mean' in cmd or 'vla-mean' in eid or 'vla_mean' in eid:\n        cat3[-1]['mode_detail'] = 'vla_mean(K=10)'\n    elif '--K 1' in cmd or 'k1' in eid:\n        cat3[-1]['mode_detail'] = 'vla_only(K=1)'\n    else:\n        cat3[-1]['mode_detail'] = 'vla_only'\n\ncat3.sort(key=lambda x: (x['seed'] or 0, x.get('benchmark',''), x['eid']))\nfor e in cat3:\n    sr_s = f\"{e['sr']}\" if e['sr'] is not None else \"N/A\"\n    print(f\"\\n  {e['eid']}\")\n    print(f\"    seed={e['seed']}  benchmark={e.get('benchmark','?')}  sub={e['mode_detail']}  status={e['status']}  conclusion={e['conclusion']}  server={e['server']}\")\n    print(f\"    n_rollouts={e['nr']}  total_rollouts={e['tr']}  SR={sr_s}{e['flag']}\")\n    if e['files']: print(f\"    files: {e['files']}\")\n\n# ======================================================================\n# CATEGORY 4: Magnitude curve obs_only — various ε, benchmark=object\n# ======================================================================\nprint(\"\\n\\n\" + \"=\" * 110)\nprint(\"  CATEGORY 4: Magnitude Curve obs_only — Various ε (benchmark=object, DONE+success only)\")\nprint(\"=\" * 110)\n\ncat4 = []\nfor eid, exp in sorted(experiments.items()):\n    if not eid.startswith('eval'): continue\n    mode = get_mode(eid, exp)\n    if mode != 'obs_only': continue\n    bm = get_benchmark(eid, exp)\n    if bm != 'object': continue\n    eps = get_eps(eid, exp)\n    seed = get_seed(eid, exp)\n    status = exp.get('status')\n    conclusion = exp.get('conclusion')\n    server = get(exp, 'spec', 'server')\n    nr = get_nrollouts(eid, exp)\n    tr = get_total_rollouts(exp)\n    sr = get_sr(exp)\n    cmd = get(exp, 'spec', 'command', default='')\n    # Skip K!=10\n    if '--K 5' in cmd or '--K 20' in cmd or 'k5' in eid or 'k20' in eid: continue\n    \n    flag = \"\"\n    if nr == 20: flag += \" **n_rollouts=20**\"\n    if tr == 200: flag += \" **total_rollouts=200**\"\n    \n    cat4.append({\n        'eid': eid, 'seed': seed, 'eps': eps, 'status': status, 'conclusion': conclusion,\n        'server': server, 'nr': nr, 'tr': tr, 'sr': sr, 'flag': flag,\n        'files': get_files(eid, exp)\n    })\n\ncat4.sort(key=lambda x: (str(x['eps'] or ''), x['seed'] or 0, x['eid']))\ncurrent_eps = None\nfor e in cat4:\n    if e['eps'] != current_eps:\n        current_eps = e['eps']\n        print(f\"\\n  --- ε = {current_eps} ---\")\n    sr_s = f\"{e['sr']}\" if e['sr'] is not None else \"N/A\"\n    done_mark = \"✓\" if e['status'] == 'DONE' and e['conclusion'] == 'success' else (\"✗\" if e['conclusion'] in ('killed','failed') else \"◎\" if e['status'] in ('RUNNING','DEPLOYED') else \"?\")\n    print(f\"    [{done_mark}] {e['eid']}  seed={e['seed']}  status={e['status']}  conclusion={e['conclusion']}  SR={sr_s}  n_rollouts={e['nr']}  tr={e['tr']}{e['flag']}\")\n\n# ======================================================================\n# CATEGORY 5: Magnitude curve perdof — various ε, benchmark=object\n# ======================================================================\nprint(\"\\n\\n\" + \"=\" * 110)\nprint(\"  CATEGORY 5: Magnitude Curve perdof — Various ε (benchmark=object)\")\nprint(\"=\" * 110)\n\ncat5 = []\nfor eid, exp in sorted(experiments.items()):\n    if not eid.startswith('eval'): continue\n    mode = get_mode(eid, exp)\n    if mode != 'perdof': continue\n    bm = get_benchmark(eid, exp)\n    if bm != 'object': continue\n    eps = get_eps(eid, exp)\n    seed = get_seed(eid, exp)\n    status = exp.get('status')\n    conclusion = exp.get('conclusion')\n    server = get(exp, 'spec', 'server')\n    nr = get_nrollouts(eid, exp)\n    tr = get_total_rollouts(exp)\n    sr = get_sr(exp)\n    cmd = get(exp, 'spec', 'command', default='')\n    \n    flag = \"\"\n    if nr == 20: flag += \" **n_rollouts=20**\"\n    if tr == 200: flag += \" **total_rollouts=200**\"\n    \n    cat5.append({\n        'eid': eid, 'seed': seed, 'eps': eps, 'status': status, 'conclusion': conclusion,\n        'server': server, 'nr': nr, 'tr': tr, 'sr': sr, 'flag': flag,\n        'files': get_files(eid, exp)\n    })\n\ncat5.sort(key=lambda x: (str(x['eps'] or ''), x['seed'] or 0, x['eid']))\ncurrent_eps = None\nfor e in cat5:\n    if e['eps'] != current_eps:\n        current_eps = e['eps']\n        print(f\"\\n  --- ε = {current_eps} ---\")\n    sr_s = f\"{e['sr']}\" if e['sr'] is not None else \"N/A\"\n    done_mark = \"✓\" if e['status'] == 'DONE' and e['conclusion'] in ('success','negative') else (\"✗\" if e['conclusion'] in ('killed','failed') else \"◎\" if e['status'] in ('RUNNING','DEPLOYED') else \"?\")\n    print(f\"    [{done_mark}] {e['eid']}  seed={e['seed']}  status={e['status']}  conclusion={e['conclusion']}  SR={sr_s}  n_rollouts={e['nr']}  tr={e['tr']}{e['flag']}\")\n\n# ======================================================================\n# CATEGORY 6: Scalar CRM — seeds 42-45\n# ======================================================================\nprint(\"\\n\\n\" + \"=\" * 110)\nprint(\"  CATEGORY 6: Scalar CRM\")\nprint(\"  Expected: 4 seeds (42-45)\")\nprint(\"=\" * 110)\n\ncat6 = []\nfor eid, exp in sorted(experiments.items()):\n    if not eid.startswith('eval'): continue\n    mode = get_mode(eid, exp)\n    if mode != 'scalar': continue\n    seed = get_seed(eid, exp)\n    status = exp.get('status')\n    conclusion = exp.get('conclusion')\n    server = get(exp, 'spec', 'server')\n    nr = get_nrollouts(eid, exp)\n    tr = get_total_rollouts(exp)\n    sr = get_sr(exp)\n    bm = get_benchmark(eid, exp)\n    cmd = get(exp, 'spec', 'command', default='')\n    \n    flag = \"\"\n    if nr == 20: flag += \" **n_rollouts=20**\"\n    if tr == 200: flag += \" **total_rollouts=200**\"\n    \n    cat6.append({\n        'eid': eid, 'seed': seed, 'status': status, 'conclusion': conclusion,\n        'server': server, 'nr': nr, 'tr': tr, 'sr': sr, 'flag': flag,\n        'benchmark': bm, 'files': get_files(eid, exp),\n        'cmd': cmd[:200] if cmd else ''\n    })\n\ncat6.sort(key=lambda x: (x['seed'] or 0, x['eid']))\nfor e in cat6:\n    sr_s = f\"{e['sr']}\" if e['sr'] is not None else \"N/A\"\n    print(f\"\\n  {e['eid']}\")\n    print(f\"    seed={e['seed']}  benchmark={e.get('benchmark','?')}  status={e['status']}  conclusion={e['conclusion']}  server={e['server']}\")\n    print(f\"    n_rollouts={e['nr']}  total_rollouts={e['tr']}  SR={sr_s}{e['flag']}\")\n    if e['files']: print(f\"    files: {e['files']}\")\n\n# ======================================================================\n# FLAGGED: n_rollouts=20 or total_rollouts=200\n# ======================================================================\nprint(\"\\n\\n\" + \"=\" * 110)\nprint(\"  FLAGGED EXPERIMENTS: n_rollouts=20 or total_rollouts=200\")\nprint(\"=\" * 110)\n\nflagged = []\nfor eid, exp in sorted(experiments.items()):\n    if not eid.startswith('eval'): continue\n    nr = get_nrollouts(eid, exp)\n    tr = get_total_rollouts(exp)\n    if nr == 20 or tr == 200:\n        seed = get_seed(eid, exp)\n        sr = get_sr(exp)\n        status = exp.get('status')\n        mode = get_mode(eid, exp)\n        bm = get_benchmark(eid, exp)\n        server = get(exp, 'spec', 'server')\n        cmd = get(exp, 'spec', 'command', default='')\n        flagged.append({\n            'eid': eid, 'seed': seed, 'nr': nr, 'tr': tr, 'sr': sr,\n            'status': status, 'mode': mode, 'benchmark': bm, 'server': server,\n            'cmd': cmd[:250] if cmd else ''\n        })\n\nif flagged:\n    for e in flagged:\n        print(f\"\\n  {e['eid']}\")\n        print(f\"    mode={e['mode']}  benchmark={e['benchmark']}  seed={e['seed']}  server={e['server']}\")\n        print(f\"    n_rollouts={e['nr']}  total_rollouts={e['tr']}  SR={e['sr']}  status={e['status']}\")\n        if e['cmd']: print(f\"    cmd: {e['cmd']}\")\nelse:\n    print(\"  None found.\")\n\n# ======================================================================\n# CLEAN SUMMARY TABLE: best run per (category, seed) for usable results\n# ======================================================================\nprint(\"\\n\\n\" + \"=\" * 110)\nprint(\"  CLEAN SUMMARY: Best DONE+success run per seed (benchmark=object only)\")\nprint(\"=\" * 110)\n\ndef best_run(entries, target_seeds):\n    \"\"\"Pick the best (latest retry) DONE+success run per seed\"\"\"\n    by_seed = {}\n    for e in entries:\n        s = e['seed']\n        if s not in target_seeds: continue\n        # Prefer DONE+success with SR available\n        if s not in by_seed:\n            by_seed[s] = e\n        else:\n            prev = by_seed[s]\n            # Prefer success over others\n            if e['conclusion'] == 'success' and prev['conclusion'] != 'success':\n                by_seed[s] = e\n            elif e['conclusion'] == 'success' and prev['conclusion'] == 'success':\n                # Prefer one with SR\n                if e['sr'] is not None and prev['sr'] is None:\n                    by_seed[s] = e\n    return by_seed\n\nprint(\"\\n  obs_only ε=0.2 (K=10, object):\")\nprint(f\"  {'Seed':<6} {'exp_id':<55} {'Status':<10} {'SR':<8} {'n_rollouts':<12} {'total_roll':<12} {'Server'}\")\nbest1 = best_run(cat1, [42,43,44,45,46,47])\nfor s in [42,43,44,45,46,47]:\n    if s in best1:\n        e = best1[s]\n        sr_s = f\"{e['sr']}\" if e['sr'] is not None else \"N/A\"\n        print(f\"  {s:<6} {e['eid']:<55} {e['status']:<10} {sr_s:<8} {e['nr']!s:<12} {e['tr']!s:<12} {e['server']}\")\n    else:\n        print(f\"  {s:<6} {'MISSING':<55}\")\n\nprint(\"\\n  Argmin baseline (K=10, object):\")\nprint(f\"  {'Seed':<6} {'exp_id':<55} {'Status':<10} {'SR':<8} {'n_rollouts':<12} {'total_roll':<12} {'Server'}\")\n# Filter cat2 to object only\ncat2_obj = [e for e in cat2 if e.get('benchmark','object') == 'object']\nbest2 = best_run(cat2_obj, [42,43,44,45,46,47])\nfor s in [42,43,44,45,46,47]:\n    if s in best2:\n        e = best2[s]\n        sr_s = f\"{e['sr']}\" if e['sr'] is not None else \"N/A\"\n        print(f\"  {s:<6} {e['eid']:<55} {e['status']:<10} {sr_s:<8} {e['nr']!s:<12} {e['tr']!s:<12} {e['server']}\")\n    else:\n        print(f\"  {s:<6} {'MISSING / no successful run':<55}\")\n\nprint(\"\\n  VLA-only baseline (K=1, object):\")\nprint(f\"  {'Seed':<6} {'exp_id':<55} {'Sub-mode':<16} {'Status':<10} {'SR':<8} {'n_rollouts':<12} {'total_roll':<12} {'Server'}\")\ncat3_obj_k1 = [e for e in cat3 if e.get('benchmark') == 'object' and ('K=1' in e['mode_detail'] or 'vla_only' in e['mode_detail'])]\nbest3 = best_run(cat3_obj_k1, [42,43,44,45,46])\nfor s in [42,43,44,45,46]:\n    if s in best3:\n        e = best3[s]\n        sr_s = f\"{e['sr']}\" if e['sr'] is not None else \"N/A\"\n        print(f\"  {s:<6} {e['eid']:<55} {e['mode_detail']:<16} {e['status']:<10} {sr_s:<8} {e['nr']!s:<12} {e['tr']!s:<12} {e['server']}\")\n    else:\n        print(f\"  {s:<6} {'MISSING / no successful run':<55}\")\n\nprint(\"\\n  Scalar CRM (object, ε=0.1):\")\nprint(f\"  {'Seed':<6} {'exp_id':<55} {'Status':<10} {'SR':<8} {'n_rollouts':<12} {'total_roll':<12} {'Server'}\")\ncat6_obj = [e for e in cat6 if e.get('benchmark') == 'object']\nbest6 = best_run(cat6_obj, [42,43,44,45])\nfor s in [42,43,44,45]:\n    if s in best6:\n        e = best6[s]\n        sr_s = f\"{e['sr']}\" if e['sr'] is not None else \"N/A\"\n        print(f\"  {s:<6} {e['eid']:<55} {e['status']:<10} {sr_s:<8} {e['nr']!s:<12} {e['tr']!s:<12} {e['server']}\")\n    else:\n        print(f\"  {s:<6} {'MISSING / no successful run':<55}\")\n\n# Magnitude curve summary\nprint(\"\\n  Magnitude curve obs_only (object, DONE+success/negative only):\")\nprint(f\"  {'ε':<10} {'Seeds with usable data':<50} {'SRs'}\")\neps_vals = sorted(set(e['eps'] for e in cat4 if e['eps'] is not None and e['eps'] != 0.2), key=lambda x: (str(type(x)), x))\neps_vals_all = [0.03, 0.05, 0.1, 0.2, 0.3, \"uncapped\"]\nfor ev in eps_vals_all:\n    matching = [e for e in cat4 if e['eps'] == ev and e['status'] == 'DONE' and e['conclusion'] in ('success','negative')]\n    seeds = sorted(set(e['seed'] for e in matching if e['seed'] is not None))\n    srs = {e['seed']: e['sr'] for e in matching if e['sr'] is not None}\n    print(f\"  {str(ev):<10} seeds={seeds}  SRs={srs}\")\n\nprint(\"\\n  Magnitude curve perdof (object, DONE+success/negative only):\")\nprint(f\"  {'ε':<10} {'Seeds with usable data':<50} {'SRs'}\")\neps_vals_all_p = [0.03, 0.05, 0.1, 0.2, 0.3, \"uncapped\"]\nfor ev in eps_vals_all_p:\n    matching = [e for e in cat5 if e['eps'] == ev and e['status'] == 'DONE' and e['conclusion'] in ('success','negative')]\n    seeds = sorted(set(e['seed'] for e in matching if e['seed'] is not None))\n    srs = {e['seed']: e['sr'] for e in matching if e['sr'] is not None}\n    print(f\"  {str(ev):<10} seeds={seeds}  SRs={srs}\")\n\nPYEOF\npython3 /tmp/extract_final.py 2>&1",
  "description": "Extract and categorize all eval experiments with structured summary",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LkyHAJXMgM6jYEjtYbJhsT",
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "13b25dc9-c43c-44b6-b7cc-530b69f2b66a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D6njrkG5jAaw9ekJK9gomV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16445,
      "cache_read_input_tokens": 53557,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16445,
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

_source line 58 · 2026-05-18T10:46:10.536Z_

<details><summary>↩ Tool result · `toolu_015QEEfooZ8QyBhWXbc4Xnt2`</summary>

```text
&lt;persisted-output>
Output too large (31.4KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/c1bdccab-16c6-497c-9d30-0feab97d927d/tool-results/btng1tze4.txt

Preview (first 2KB):
==============================================================================================================
  CATEGORY 1: obs_only ε=0.2 (norm02) — Main Paper Results K=10
  Expected: 6 seeds (42-47), benchmark=object, mode=crm_obs_only, --max_correction_norm 0.2, --K 10
==============================================================================================================

  eval-acr-object-obs-only-norm02
    seed=42  status=DONE  conclusion=success  server=bjb1-32546
    n_rollouts=10  total_rollouts=100  SR=N/A
    files: ['logs/eval_object_obs_only_norm02.json', '~/runs/acr-vla-conformal-refinement/eval-acr-object-obs-only-norm02.log']

  eval-mag-obsonly-norm02-object
    seed=42  status=DONE  conclusion=killed  server=bjb2-28827
    n_rollouts=10  total_rollouts=None  SR=N/A
    files: ['logs/eval_object_obs_only_norm02_v2.json', 'N/A']

  eval-obs-only-object-norm02-seed43
    seed=43  status=DONE  conclusion=failed  server=bjb1-32546
    n_rollouts=10  total_rollouts=None  SR=N/A
    files: ['logs/eval_object_obs_only_norm02_seed43.json']

  eval-obs-only-object-norm02-seed43-r2
    seed=43  status=DONE  conclusion=success  server=None
    n_rollouts=None  total_rollouts=None  SR=N/A
    files: ['~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-seed43-r2.log']

  eval-obs-only-object-norm02-seed44
    seed=44  status=DONE  conclusion=failed  server=None
    n_rollouts=10  total_rollouts=None  SR=N/A

  eval-obs-only-object-norm02-seed44-r2
    seed=44  status=DONE  conclusion=success  server=bjb1-18228
    n_rollouts=10  total_rollouts=None  SR=N/A
    files: ['logs/eval_object_obs_only_norm02_seed44.json']

  eval-obs-only-object-norm02-seed44-r3
    seed=44  status=DONE  conclusion=killed  server=bjb1-18228
    n_rollouts=10  total_rollouts=None  SR=N/A
    files: ['logs/eval_object_obs_only_norm02_seed44.json"', '~/runs/acr-vla-conformal-refinement/eval-obs-only-object-norm02-seed44-r3.log']

...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LkyHAJXMgM6jYEjtYbJhsT",
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "4b99180d-8a5f-4748-bd69-185f8588d541"
}
```

</details>

---


### System

_source line 59_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5dc54df06c763762",
  "tool_use_id": "toolu_01LkyHAJXMgM6jYEjtYbJhsT",
  "description": "Reading ~/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/c1bdccab-16c6-497c-9d30-0feab97d927d/tool-results/btng1tze4.txt",
  "usage": {
    "total_tokens": 79500,
    "tool_uses": 9,
    "duration_ms": 176511
  },
  "last_tool_name": "Read",
  "uuid": "14d02bc8-6c0b-48ec-a70e-71b6ce73c16e",
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d"
}
```

---


### Tool call

_source line 60_

<details open><summary>🔧 Tool call — Read · `toolu_01A56ojUMghTYntxxyCVUMS8`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/c1bdccab-16c6-497c-9d30-0feab97d927d/tool-results/btng1tze4.txt",
  "offset": 540,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LkyHAJXMgM6jYEjtYbJhsT",
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "f1d14fae-4956-4d44-9dc6-2656bd1ac3ef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TgdRuVxjuZwJQ3cPzegEWF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9295,
      "cache_read_input_tokens": 70002,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9295,
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

_source line 61 · 2026-05-18T10:46:14.792Z_

<details><summary>↩ Tool result · `toolu_01A56ojUMghTYntxxyCVUMS8`</summary>

```text
&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (540). The file has 490 lines.&lt;/system-reminder>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LkyHAJXMgM6jYEjtYbJhsT",
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "12c7b971-d422-4a62-a583-7fa864724e10"
}
```

</details>

---


### System

_source line 62_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5dc54df06c763762",
  "tool_use_id": "toolu_01LkyHAJXMgM6jYEjtYbJhsT",
  "description": "Reading ~/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/c1bdccab-16c6-497c-9d30-0feab97d927d/tool-results/btng1tze4.txt",
  "usage": {
    "total_tokens": 79795,
    "tool_uses": 10,
    "duration_ms": 180304
  },
  "last_tool_name": "Read",
  "uuid": "b3b15668-2fee-4b44-8e1c-561fcf0df211",
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d"
}
```

---


### Tool call

_source line 63_

<details open><summary>🔧 Tool call — Read · `toolu_01XYSFSWaqweBbLKRynJaYhV`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/c1bdccab-16c6-497c-9d30-0feab97d927d/tool-results/btng1tze4.txt",
  "offset": 350,
  "limit": 140
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01LkyHAJXMgM6jYEjtYbJhsT",
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "4f3fe1bc-3d70-42ae-9452-c0a544ff295c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ra4osJu3xQzqEGpHde2M9d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 223,
      "cache_read_input_tokens": 79297,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 223,
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

_source line 64 · 2026-05-18T10:46:18.583Z_

<details><summary>↩ Tool result · `toolu_01XYSFSWaqweBbLKRynJaYhV`</summary>

```text
350	    [✗] eval-mag-perdof-norm03-object  seed=42  status=DEPLOYED  conclusion=killed  SR=N/A  n_rollouts=10  tr=None
351	    [✗] eval-mag-perdof-norm03-object-r2  seed=42  status=DONE  conclusion=killed  SR=N/A  n_rollouts=10  tr=None
352	    [✓] eval-mag-perdof-norm03-object-r3  seed=42  status=DONE  conclusion=success  SR=N/A  n_rollouts=10  tr=None
353	    [✗] eval-mag-perdof-norm0p3-object  seed=42  status=DONE  conclusion=killed  SR=N/A  n_rollouts=10  tr=None
354	    [✗] eval-mag-perdof-norm0p3-object-r2  seed=42  status=DONE  conclusion=killed  SR=N/A  n_rollouts=10  tr=None
355	    [✓] eval-perdof-object-norm03-seed44  seed=44  status=DONE  conclusion=negative  SR=0.04  n_rollouts=10  tr=None
356	    [✓] eval-perdof-object-norm03-seed44-r2  seed=44  status=DONE  conclusion=negative  SR=0.04  n_rollouts=10  tr=100
357	    [✓] eval-perdof-object-norm03-seed45-r2  seed=45  status=DONE  conclusion=negative  SR=N/A  n_rollouts=10  tr=None
358	    [✗] eval-perdof-object-norm03-seed46  seed=46  status=DONE  conclusion=failed  SR=N/A  n_rollouts=10  tr=None
359	    [✗] eval-perdof-object-norm03-seed46-r2  seed=46  status=DONE  conclusion=killed  SR=N/A  n_rollouts=10  tr=None
360	
361	  --- ε = uncapped ---
362	    [✗] eval-acr-object-v4-default  seed=42  status=DONE  conclusion=killed  SR=N/A  n_rollouts=10  tr=None
363	    [✓] eval-acr-object-v4-default-r2  seed=42  status=DONE  conclusion=success  SR=N/A  n_rollouts=10  tr=None
364	    [◎] eval-perdof-object-default-seed43  seed=43  status=RUNNING  conclusion=None  SR=N/A  n_rollouts=10  tr=None
365	    [✓] eval-perdof-object-default-seed44  seed=44  status=DONE  conclusion=negative  SR=N/A  n_rollouts=10  tr=90
366	    [?] eval-perdof-object-default-seed45  seed=45  status=PREPARING  conclusion=None  SR=N/A  n_rollouts=None  tr=None
367	    [✓] eval-perdof-object-default-seed46  seed=46  status=DONE  conclusion=negative  SR=0  n_rollouts=10  tr=None
368	
369	
370	==============================================================================================================
371	  CATEGORY 6: Scalar CRM
372	  Expected: 4 seeds (42-45)
373	==============================================================================================================
374	
375	  eval-acr-object-v4-scalar
376	    seed=42  benchmark=object  status=DONE  conclusion=negative  server=bjb1-32546
377	    n_rollouts=10  total_rollouts=None  SR=N/A
378	    files: ['~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-scalar.log']
379	
380	  eval-acr-object-v4-scalar-b2
381	    seed=42  benchmark=object  status=DONE  conclusion=killed  server=bjb2-28827
382	    n_rollouts=10  total_rollouts=None  SR=N/A
383	    files: ['~/runs/acr-vla-conformal-refinement/eval-acr-object-v4-scalar-b2.log']
384	
385	  eval-acr-spatial-v4-scalar
386	    seed=42  benchmark=spatial  status=DONE  conclusion=killed  server=bjb1-18228
387	    n_rollouts=10  total_rollouts=None  SR=N/A
388	    files: ['~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-scalar.log']
389	
390	  eval-acr-spatial-v4-scalar-r2
391	    seed=42  benchmark=spatial  status=DONE  conclusion=success  server=bjb1-18228
392	    n_rollouts=10  total_rollouts=100  SR=N/A
393	    files: ['~/runs/acr-vla-conformal-refinement/eval-acr-spatial-v4-scalar-r2.log']
394	
395	  eval-scalar-unc-spatial
396	    seed=42  benchmark=spatial  status=DONE  conclusion=killed  server=bjb1-18228
397	    n_rollouts=10  total_rollouts=None  SR=N/A
398	    files: ['/root/autodl-tmp/eval_results/eval-scalar-unc-spatial.log']
399	
400	  eval-scalar-unc-spatial-v2
401	    seed=42  benchmark=spatial  status=DONE  conclusion=killed  server=bjb1-18228
402	    n_rollouts=10  total_rollouts=None  SR=N/A
403	    files: ['~/runs/acr-vla-conformal-refinement/eval-scalar-unc-spatial-v2.log']
404	
405	  eval-scalar-object-seed43
406	    seed=43  benchmark=object  status=DONE  conclusion=success  server=bjb1-32546
407	    n_rollouts=10  total_rollouts=None  SR=N/A
408	    files: ['logs/eval_object_scalar_seed43.json', '~/runs/acr-vla-conformal-refinement/eval-scalar-object-seed43.log']
409	
410	  eval-scalar-object-seed44
411	    seed=44  benchmark=object  status=DONE  conclusion=failed  server=bjb2-40593
412	    n_rollouts=10  total_rollouts=None  SR=N/A
413	    files: ['logs/eval_object_scalar_seed44.json"', '~/runs/acr-vla-conformal-refinement/eval-scalar-object-seed44.log']
414	
415	  eval-scalar-object-seed44-r2
416	    seed=44  benchmark=object  status=DONE  conclusion=negative  server=bjb1-32546
417	    n_rollouts=10  total_rollouts=None  SR=N/A
418	    files: ['logs/eval_object_scalar_seed44_r2.json"', '~/runs/acr-vla-conformal-refinement/eval-scalar-object-seed44-r2.log']
419	
420	  eval-scalar-object-seed45
421	    seed=45  benchmark=object  status=DONE  conclusion=success  server=bjb2-28827
422	    n_rollouts=None  total_rollouts=None  SR=0.09
423	    files: ['logs/eval_object_scalar_seed45.json', 'logs/eval_object_scalar_seed45.log']
424	
425	
426	==============================================================================================================
427	  FLAGGED EXPERIMENTS: n_rollouts=20 or total_rollouts=200
428	==============================================================================================================
429	
430	  eval-obs-only-object-default-seed45
431	    mode=obs_only  benchmark=object  seed=45  server=bjb2-28827
432	    n_rollouts=None  total_rollouts=200  SR=0.12  status=DONE
433	    cmd: python src/evaluate.py --mode crm_obs_only --K 10 --seed 45 --benchmark object --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_default_seed45.json
434	
435	
436	==============================================================================================================
437	  CLEAN SUMMARY: Best DONE+success run per seed (benchmark=object only)
438	==============================================================================================================
439	
440	  obs_only ε=0.2 (K=10, object):
441	  Seed   exp_id                                                  Status     SR       n_rollouts   total_roll   Server
442	  42     eval-acr-object-obs-only-norm02                         DONE       N/A      10           100          bjb1-32546
443	  43     eval-obs-only-object-norm02-seed43-r2                   DONE       N/A      None         None         None
444	  44     eval-obs-only-object-norm02-seed44-r2                   DONE       N/A      10           None         bjb1-18228
445	  45     eval-obs-only-object-norm02-seed45                      DONE       N/A      10           100          bjb1-32546
446	  46     eval-obs-only-object-norm02-seed46                      DONE       0.15     10           None         bjb1-18228
447	  47     eval-obs-only-object-norm02-seed47                      DONE       0.2      10           None         bjb1-32546
448	
449	  Argmin baseline (K=10, object):
450	  Seed   exp_id                                                  Status     SR       n_rollouts   total_roll   Server
451	  42     MISSING / no successful run                            
452	  43     eval-argmin-object-seed43                               DONE       0.17     10           None         bjb1-18228
453	  44     eval-argmin-object-seed44-r2                            DONE       N/A      10           None         bjb1-18228
454	  45     eval-argmin-object-seed45                               DONE       N/A      10           100          bjb2-28827
455	  46     eval-argmin-object-seed46                               DONE       N/A      10           100          bjb1-32546
456	  47     eval-argmin-object-seed47                               DONE       N/A      10           100          bjb1-32546
457	
458	  VLA-only baseline (K=1, object):
459	  Seed   exp_id                                                  Sub-mode         Status     SR       n_rollouts   total_roll   Server
460	  42     eval-object-v8-full                                     vla_only         DONE       0.13     10           100          bjb2-40593
461	  43     eval-vla-mean-object-seed43                             vla_mean(K=10)   DONE       N/A      10           100          bjb1-32546
462	  44     eval-vla-mean-object-seed44                             vla_mean(K=10)   DONE       N/A      10           None         bjb1-32546
463	  45     eval-vla-mean-object-seed45                             vla_mean(K=10)   DONE       N/A      10           100          bjb2-28827
464	  46     MISSING / no successful run                            
465	
466	  Scalar CRM (object, ε=0.1):
467	  Seed   exp_id                                                  Status     SR       n_rollouts   total_roll   Server
468	  42     eval-acr-object-v4-scalar                               DONE       N/A      10           None         bjb1-32546
469	  43     eval-scalar-object-seed43                               DONE       N/A      10           None         bjb1-32546
470	  44     eval-scalar-object-seed44                               DONE       N/A      10           None         bjb2-40593
471	  45     eval-scalar-object-seed45                               DONE       0.09     None         None         bjb2-28827
472	
473	  Magnitude curve obs_only (object, DONE+success/negative only):
474	  ε          Seeds with usable data                             SRs
475	  0.03       seeds=[42]  SRs={}
476	  0.05       seeds=[42, 43]  SRs={}
477	  0.1        seeds=[43, 44, 45]  SRs={43: 0.12, 45: 0.14}
478	  0.2        seeds=[42, 43, 44, 45, 46, 47]  SRs={46: 0.15, 47: 0.2}
479	  0.3        seeds=[42, 44, 45, 46]  SRs={45: 14}
480	  uncapped   seeds=[42, 44, 45, 46]  SRs={45: 0.12}
481	
482	  Magnitude curve perdof (object, DONE+success/negative only):
483	  ε          Seeds with usable data                             SRs
484	  0.03       seeds=[42]  SRs={}
485	  0.05       seeds=[42]  SRs={}
486	  0.1        seeds=[42, 43, 44, 45, 46, 47]  SRs={43: 0.12, 46: 0.1}
487	  0.2        seeds=[42, 43, 44, 45, 46, 47]  SRs={44: 0.1, 45: 0.12}
488	  0.3        seeds=[42, 44, 45]  SRs={44: 0.04}
489	  uncapped   seeds=[42, 44, 46]  SRs={46: 0}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01LkyHAJXMgM6jYEjtYbJhsT",
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "a91438ea-5f43-4929-8f8a-b56a7bb00fcb"
}
```

</details>

---


### System

_source line 65_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a5dc54df06c763762",
  "tool_use_id": "toolu_01LkyHAJXMgM6jYEjtYbJhsT",
  "status": "completed",
  "output_file": "",
  "summary": "Registry audit for n_rollouts",
  "usage": {
    "total_tokens": 83584,
    "tool_uses": 10,
    "duration_ms": 223344
  },
  "uuid": "453e35a4-7172-4429-a901-7c7858f7d158",
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d"
}
```

---


### Tool result

_source line 66 · 2026-05-18T10:47:01.622Z_

<details><summary>↩ Tool result · `toolu_01LkyHAJXMgM6jYEjtYbJhsT`</summary>

```text
Here is the complete structured summary of all evaluation experiments.

---

## CATEGORY 1: obs_only ε=0.2 (norm02) — Main Paper Results K=10

**Best DONE+success run per seed (benchmark=object):**

| Seed | exp_id | Status | SR | n_rollouts | total_rollouts | Server |
|------|--------|--------|----|------------|----------------|--------|
| 42 | `eval-acr-object-obs-only-norm02` | DONE | N/A (in JSON) | 10 | 100 | bjb1-32546 |
| 43 | `eval-obs-only-object-norm02-seed43-r2` | DONE | N/A | None | None | None |
| 44 | `eval-obs-only-object-norm02-seed44-r2` | DONE | N/A | 10 | None | bjb1-18228 |
| 45 | `eval-obs-only-object-norm02-seed45` | DONE | N/A (in JSON) | 10 | 100 | bjb1-32546 |
| 46 | `eval-obs-only-object-norm02-seed46` | DONE | 0.15 | 10 | None | bjb1-18228 |
| 47 | `eval-obs-only-object-norm02-seed47` | DONE | 0.20 | 10 | None | bjb1-32546 |

All 6 seeds have a DONE+success run. Additional experiments exist per seed (retries, killed attempts), plus seed48 has a RUNNING r2 attempt. SRs for seeds 42-45 are stored in JSON output files but not recorded in registry metrics. Key JSON files: `logs/eval_object_obs_only_norm02.json`, `logs/eval_object_obs_only_norm02_seed43.json` (from r2 log), `logs/eval_object_obs_only_norm02_seed44.json`, `logs/eval_object_obs_only_norm02_seed45.json`, `logs/eval_object_obs_only_norm02_seed46.json`.

Also present: K=5 sweep experiments (seed42 DONE SR=0.14, seed43 RUNNING, seed44 PREPARING) and a K=20 experiment (seed42 killed).

---

## CATEGORY 2: Argmin Baseline (reconvla mode, K=10)

**Best DONE+success/completed run per seed (benchmark=object):**

| Seed | exp_id | Status | SR | n_rollouts | total_rollouts | Server |
|------|--------|--------|----|------------|----------------|--------|
| 42 | **MISSING** (only spatial runs: `eval-argmin-only-spatial-r2` SR=0.34) | - | - | - | - | - |
| 43 | `eval-argmin-object-seed43` | DONE | 0.17 | 10 | None | bjb1-18228 |
| 44 | `eval-argmin-object-seed44-r2` | DONE | N/A (in JSON) | 10 | None | bjb1-18228 |
| 45 | `eval-argmin-object-seed45` | DONE | N/A | 10 | 100 | bjb2-28827 |
| 46 | `eval-argmin-object-seed46` | DONE | N/A | 10 | 100 | bjb1-32546 |
| 47 | `eval-argmin-object-seed47` | DONE | N/A | 10 | 100 | bjb1-32546 |

Note: Seed 42 argmin on object benchmark is missing. There's no `eval-argmin-object-seed42` entry. The `eval-argmin-only-spatial` and `eval-argmin-only-spatial-r2` are spatial benchmark only. Key JSON files: `logs/eval_object_reconvla_seed43.json`, `logs/eval_object_reconvla_seed44.json`, `logs/eval_object_argmin_seed45.json`, `logs/eval_object_reconvla_seed46.json`, `logs/eval_object_reconvla_seed47.json`.

---

## CATEGORY 3: VLA-Only Baseline

**Best run per seed (benchmark=object):**

| Seed | exp_id | Sub-mode | Status | SR | n_rollouts | Server |
|------|--------|----------|--------|----|------------|--------|
| 42 | `eval-object-v8-full` | vla_only | DONE | 0.13 | 10 | bjb2-40593 |
| 42 | `eval-vla-only-object` | vla_only(K=1) | DONE | N/A | 10 | bjb1-32546 |
| 43 | `eval-vla-only-object-seed43` | vla_only(K=1) | DONE | N/A | 10 | bjb1-32546 |
| 43 | `eval-vla-mean-object-seed43` | vla_mean(K=10) | DONE | N/A | 10 | bjb1-32546 |
| 44 | `eval-vla-only-object-seed44-r2` | vla_only(K=1) | DONE | N/A | 10 | bjb2-40593 |
| 44 | `eval-vla-mean-object-seed44` | vla_mean(K=10) | DONE | N/A | 10 | bjb1-32546 |
| 45 | `eval-vla-only-object-seed45` | vla_only | DONE | N/A | None | bjb2-28827 |
| 45 | `eval-vla-mean-object-seed45` | vla_mean(K=10) | DONE | N/A | 10 | bjb2-28827 |
| 46 | **MISSING** for object | - | - | - | - | - |

Two sub-types exist: `vla_only` (K=1, single sample) and `vla_mean` (K=10, mean aggregation). Seed 46 has no object-benchmark VLA-only run. Spatial benchmarks exist for seed42 only. Also includes an OpenVLA experiment (`eval-openvla-object-vla-only-seed42-v2`, n_rollouts=**100**).

---

## CATEGORY 4: Magnitude Curve obs_only (benchmark=object)

**Usable data (DONE + success/negative) per ε:**

| ε | Seeds with usable data | Known SRs |
|---|----------------------|-----------|
| 0.03 | [42] | {} (SR in JSON file) |
| 0.05 | [42, 43] | {} |
| 0.1 | [43, 44, 45] | {43: 0.12, 45: 0.14} |
| 0.2 | [42, 43, 44, 45, 46, 47] | {46: 0.15, 47: 0.20} |
| 0.3 | [42, 44, 45, 46] | {45: 14 (likely 0.14)} |
| uncapped | [42, 44, 45, 46] | {45: 0.12} |

RUNNING: ε=0.05 seed44, ε=0.05 seed45, ε=0.1 seed42-r2, ε=0.1 seed46-r3, ε=0.1 seed48, ε=0.3 seed48.

---

## CATEGORY 5: Magnitude Curve perdof (benchmark=object)

**Usable data (DONE + success/negative) per ε:**

| ε | Seeds with usable data | Known SRs |
|---|----------------------|-----------|
| 0.03 | [42] | {} |
| 0.05 | [42] | {} |
| 0.1 | [42, 43, 44, 45, 46, 47] | {43: 0.12, 46: 0.10} |
| 0.2 | [42, 43, 44, 45, 46, 47] | {44: 0.10, 45: 0.12} |
| 0.3 | [42, 44, 45] | {44: 0.04} |
| uncapped | [42, 44, 46] | {46: 0.00} |

RUNNING: ε=0.05 seed44, ε=0.1 seed42-r2, ε=0.1 seed43, ε=0.2 seed43, ε=0.2 seed48, uncapped seed43.

---

## CATEGORY 6: Scalar CRM

| Seed | exp_id | Benchmark | Status | SR | n_rollouts | Server |
|------|--------|-----------|--------|----|------------|--------|
| 42 | `eval-acr-object-v4-scalar` | object | DONE | N/A | 10 | bjb1-32546 |
| 42 | `eval-acr-spatial-v4-scalar-r2` | spatial | DONE | N/A | 10 | bjb1-18228 |
| 43 | `eval-scalar-object-seed43` | object | DONE | N/A | 10 | bjb1-32546 |
| 44 | `eval-scalar-object-seed44-r2` | object | DONE | N/A | 10 | bjb1-32546 |
| 45 | `eval-scalar-object-seed45` | object | DONE | 0.09 | None | bjb2-28827 |

All 4 object seeds (42-45) have completed runs. seed42 conclusion=negative, seed43 conclusion=success, seed44 conclusion=negative, seed45 conclusion=success (SR=0.09).

---

## FLAGGED: n_rollouts=20 or total_rollouts=200

**Only 1 experiment flagged:**

- **`eval-obs-only-object-default-seed45`** — mode=obs_only, benchmark=object, seed=45, server=bjb2-28827
  - n_rollouts=None (not in command), **total_rollouts=200**, SR=0.12, status=DONE
  - Command: `python src/evaluate.py --mode crm_obs_only --K 10 --seed 45 --benchmark object --crm_checkpoint .../obs_only/crm_best.pt --output_file logs/eval_object_obs_only_default_seed45.json`
  - This is an uncapped/default norm experiment. The 200 total_rollouts suggests it ran 20 rollouts per task (10 tasks x 20 = 200), not the standard 10.

Also notable: `eval-openvla-object-vla-only-seed42-v2` has n_rollouts=**100** in command (using OpenVLA official eval code with different rollout structure), total_rollouts=100.

---

## Key Observations

1. **Many SRs are N/A in registry metrics** — the actual results are stored in the JSON output files on the remote servers, not captured in the registry.
2. **Argmin seed42 on object is missing** — no `eval-argmin-object-seed42` experiment exists.
3. **VLA-only seed46 on object is missing**.
4. **The only total_rollouts=200 experiment** is `eval-obs-only-object-default-seed45` (uncapped norm, not the norm02 main result).
5. All standard experiments use n_rollouts=10 with 10 tasks = 100 total rollouts.

agentId: a5dc54df06c763762 (use SendMessage with to: 'a5dc54df06c763762' to continue this agent)
&lt;usage>total_tokens: 86289
tool_uses: 10
duration_ms: 223346&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "29494824-6cdf-46e3-a2c1-3d42942194b4",
  "tool_use_result": {
    "status": "completed",
    "prompt": "You have a large JSON registry file at:\n/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/c1bdccab-16c6-497c-9d30-0feab97d927d/tool-results/mcp-agent-ml-research-read_registry-1779100984736.txt\n\nThe file has schema: {result: string} where result is a JSON string.\n\nI need you to extract ALL experiments related to evaluations. Specifically, I need to find experiments matching these categories:\n\n1. **obs_only ε=0.2 (norm02)** - 6 seeds (42-47) - these are the main paper results with K=10\n2. **Argmin baseline** - 6 seeds (42-47)\n3. **VLA-only baseline** - 5 seeds (42-46)\n4. **Magnitude curve obs_only** - various ε values (0.03, 0.05, 0.1, 0.2, 0.5, uncapped)\n5. **Magnitude curve perdof** - various ε values (0.03, 0.05, 0.1, 0.2, 0.5, uncapped)\n6. **Scalar CRM** - 4 seeds (42-45)\n\nFor each experiment, extract:\n- exp_id\n- status\n- server\n- seed (if in config or name)\n- n_rollouts (look in config, command, notes, or any field)\n- success_rate or SR metric\n- Any file paths mentioned (JSON output files)\n- The full command or config that shows n_rollouts\n\nAlso specifically flag ALL experiments where n_rollouts=20 or total_rollouts=200.\n\nUse bash with jq or python to parse the file. The file is JSON with a \"result\" key containing a string. Parse it carefully.\n\nReturn a structured summary organized by category, with exp_id, seed, n_rollouts, server, SR for each.",
    "agentId": "a5dc54df06c763762",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is the complete structured summary of all evaluation experiments.\n\n---\n\n## CATEGORY 1: obs_only ε=0.2 (norm02) — Main Paper Results K=10\n\n**Best DONE+success run per seed (benchmark=object):**\n\n| Seed | exp_id | Status | SR | n_rollouts | total_rollouts | Server |\n|------|--------|--------|----|------------|----------------|--------|\n| 42 | `eval-acr-object-obs-only-norm02` | DONE | N/A (in JSON) | 10 | 100 | bjb1-32546 |\n| 43 | `eval-obs-only-object-norm02-seed43-r2` | DONE | N/A | None | None | None |\n| 44 | `eval-obs-only-object-norm02-seed44-r2` | DONE | N/A | 10 | None | bjb1-18228 |\n| 45 | `eval-obs-only-object-norm02-seed45` | DONE | N/A (in JSON) | 10 | 100 | bjb1-32546 |\n| 46 | `eval-obs-only-object-norm02-seed46` | DONE | 0.15 | 10 | None | bjb1-18228 |\n| 47 | `eval-obs-only-object-norm02-seed47` | DONE | 0.20 | 10 | None | bjb1-32546 |\n\nAll 6 seeds have a DONE+success run. Additional experiments exist per seed (retries, killed attempts), plus seed48 has a RUNNING r2 attempt. SRs for seeds 42-45 are stored in JSON output files but not recorded in registry metrics. Key JSON files: `logs/eval_object_obs_only_norm02.json`, `logs/eval_object_obs_only_norm02_seed43.json` (from r2 log), `logs/eval_object_obs_only_norm02_seed44.json`, `logs/eval_object_obs_only_norm02_seed45.json`, `logs/eval_object_obs_only_norm02_seed46.json`.\n\nAlso present: K=5 sweep experiments (seed42 DONE SR=0.14, seed43 RUNNING, seed44 PREPARING) and a K=20 experiment (seed42 killed).\n\n---\n\n## CATEGORY 2: Argmin Baseline (reconvla mode, K=10)\n\n**Best DONE+success/completed run per seed (benchmark=object):**\n\n| Seed | exp_id | Status | SR | n_rollouts | total_rollouts | Server |\n|------|--------|--------|----|------------|----------------|--------|\n| 42 | **MISSING** (only spatial runs: `eval-argmin-only-spatial-r2` SR=0.34) | - | - | - | - | - |\n| 43 | `eval-argmin-object-seed43` | DONE | 0.17 | 10 | None | bjb1-18228 |\n| 44 | `eval-argmin-object-seed44-r2` | DONE | N/A (in JSON) | 10 | None | bjb1-18228 |\n| 45 | `eval-argmin-object-seed45` | DONE | N/A | 10 | 100 | bjb2-28827 |\n| 46 | `eval-argmin-object-seed46` | DONE | N/A | 10 | 100 | bjb1-32546 |\n| 47 | `eval-argmin-object-seed47` | DONE | N/A | 10 | 100 | bjb1-32546 |\n\nNote: Seed 42 argmin on object benchmark is missing. There's no `eval-argmin-object-seed42` entry. The `eval-argmin-only-spatial` and `eval-argmin-only-spatial-r2` are spatial benchmark only. Key JSON files: `logs/eval_object_reconvla_seed43.json`, `logs/eval_object_reconvla_seed44.json`, `logs/eval_object_argmin_seed45.json`, `logs/eval_object_reconvla_seed46.json`, `logs/eval_object_reconvla_seed47.json`.\n\n---\n\n## CATEGORY 3: VLA-Only Baseline\n\n**Best run per seed (benchmark=object):**\n\n| Seed | exp_id | Sub-mode | Status | SR | n_rollouts | Server |\n|------|--------|----------|--------|----|------------|--------|\n| 42 | `eval-object-v8-full` | vla_only | DONE | 0.13 | 10 | bjb2-40593 |\n| 42 | `eval-vla-only-object` | vla_only(K=1) | DONE | N/A | 10 | bjb1-32546 |\n| 43 | `eval-vla-only-object-seed43` | vla_only(K=1) | DONE | N/A | 10 | bjb1-32546 |\n| 43 | `eval-vla-mean-object-seed43` | vla_mean(K=10) | DONE | N/A | 10 | bjb1-32546 |\n| 44 | `eval-vla-only-object-seed44-r2` | vla_only(K=1) | DONE | N/A | 10 | bjb2-40593 |\n| 44 | `eval-vla-mean-object-seed44` | vla_mean(K=10) | DONE | N/A | 10 | bjb1-32546 |\n| 45 | `eval-vla-only-object-seed45` | vla_only | DONE | N/A | None | bjb2-28827 |\n| 45 | `eval-vla-mean-object-seed45` | vla_mean(K=10) | DONE | N/A | 10 | bjb2-28827 |\n| 46 | **MISSING** for object | - | - | - | - | - |\n\nTwo sub-types exist: `vla_only` (K=1, single sample) and `vla_mean` (K=10, mean aggregation). Seed 46 has no object-benchmark VLA-only run. Spatial benchmarks exist for seed42 only. Also includes an OpenVLA experiment (`eval-openvla-object-vla-only-seed42-v2`, n_rollouts=**100**).\n\n---\n\n## CATEGORY 4: Magnitude Curve obs_only (benchmark=object)\n\n**Usable data (DONE + success/negative) per ε:**\n\n| ε | Seeds with usable data | Known SRs |\n|---|----------------------|-----------|\n| 0.03 | [42] | {} (SR in JSON file) |\n| 0.05 | [42, 43] | {} |\n| 0.1 | [43, 44, 45] | {43: 0.12, 45: 0.14} |\n| 0.2 | [42, 43, 44, 45, 46, 47] | {46: 0.15, 47: 0.20} |\n| 0.3 | [42, 44, 45, 46] | {45: 14 (likely 0.14)} |\n| uncapped | [42, 44, 45, 46] | {45: 0.12} |\n\nRUNNING: ε=0.05 seed44, ε=0.05 seed45, ε=0.1 seed42-r2, ε=0.1 seed46-r3, ε=0.1 seed48, ε=0.3 seed48.\n\n---\n\n## CATEGORY 5: Magnitude Curve perdof (benchmark=object)\n\n**Usable data (DONE + success/negative) per ε:**\n\n| ε | Seeds with usable data | Known SRs |\n|---|----------------------|-----------|\n| 0.03 | [42] | {} |\n| 0.05 | [42] | {} |\n| 0.1 | [42, 43, 44, 45, 46, 47] | {43: 0.12, 46: 0.10} |\n| 0.2 | [42, 43, 44, 45, 46, 47] | {44: 0.10, 45: 0.12} |\n| 0.3 | [42, 44, 45] | {44: 0.04} |\n| uncapped | [42, 44, 46] | {46: 0.00} |\n\nRUNNING: ε=0.05 seed44, ε=0.1 seed42-r2, ε=0.1 seed43, ε=0.2 seed43, ε=0.2 seed48, uncapped seed43.\n\n---\n\n## CATEGORY 6: Scalar CRM\n\n| Seed | exp_id | Benchmark | Status | SR | n_rollouts | Server |\n|------|--------|-----------|--------|----|------------|--------|\n| 42 | `eval-acr-object-v4-scalar` | object | DONE | N/A | 10 | bjb1-32546 |\n| 42 | `eval-acr-spatial-v4-scalar-r2` | spatial | DONE | N/A | 10 | bjb1-18228 |\n| 43 | `eval-scalar-object-seed43` | object | DONE | N/A | 10 | bjb1-32546 |\n| 44 | `eval-scalar-object-seed44-r2` | object | DONE | N/A | 10 | bjb1-32546 |\n| 45 | `eval-scalar-object-seed45` | object | DONE | 0.09 | None | bjb2-28827 |\n\nAll 4 object seeds (42-45) have completed runs. seed42 conclusion=negative, seed43 conclusion=success, seed44 conclusion=negative, seed45 conclusion=success (SR=0.09).\n\n---\n\n## FLAGGED: n_rollouts=20 or total_rollouts=200\n\n**Only 1 experiment flagged:**\n\n- **`eval-obs-only-object-default-seed45`** — mode=obs_only, benchmark=object, seed=45, server=bjb2-28827\n  - n_rollouts=None (not in command), **total_rollouts=200**, SR=0.12, status=DONE\n  - Command: `python src/evaluate.py --mode crm_obs_only --K 10 --seed 45 --benchmark object --crm_checkpoint .../obs_only/crm_best.pt --output_file logs/eval_object_obs_only_default_seed45.json`\n  - This is an uncapped/default norm experiment. The 200 total_rollouts suggests it ran 20 rollouts per task (10 tasks x 20 = 200), not the standard 10.\n\nAlso notable: `eval-openvla-object-vla-only-seed42-v2` has n_rollouts=**100** in command (using OpenVLA official eval code with different rollout structure), total_rollouts=100.\n\n---\n\n## Key Observations\n\n1. **Many SRs are N/A in registry metrics** — the actual results are stored in the JSON output files on the remote servers, not captured in the registry.\n2. **Argmin seed42 on object is missing** — no `eval-argmin-object-seed42` experiment exists.\n3. **VLA-only seed46 on object is missing**.\n4. **The only total_rollouts=200 experiment** is `eval-obs-only-object-default-seed45` (uncapped norm, not the norm02 main result).\n5. All standard experiments use n_rollouts=10 with 10 tasks = 100 total rollouts."
      }
    ],
    "totalDurationMs": 223346,
    "totalTokens": 86289,
    "totalToolUseCount": 10,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3788,
      "cache_read_input_tokens": 79520,
      "output_tokens": 2980,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3788
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2980,
          "cache_read_input_tokens": 79520,
          "cache_creation_input_tokens": 3788,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3788,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 6,
      "searchCount": 0,
      "bashCount": 4,
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

_source line 67_

<details><summary>Logged reasoning block</summary>

```text
Now I have a good overview. Let me now SSH to the servers to verify the actual JSON files. I need to:

1. Check n_rollouts in the JSON files for all core data points
2. Specifically check seed45 experiments
3. Check perdof ε=0.2 all seeds

Let me identify the key files I need to check:

**obs_only ε=0.2 (6 seeds):**
- seed42: bjb1-32546:eval_object_obs_only_norm02.json
- seed43: bjb1-32546:eval_object_obs_only_norm02_seed43_r2.json


- seed44: bjb1-18228:eval_object_obs_only_norm02_seed44.json
- seed45: bjb1-32546:eval_object_obs_only_norm02_seed45.json
- seed46: bjb1-18228:eval_object_obs_only_norm02_seed46.json
- seed47: bjb1-32546:eval_object_obs_only_norm02_seed47.json

**Argmin baseline (6 seeds):**
- seed42: eval-reconvla-object → bjb1-32546 (need to find file)
- seed43: bjb1-18228

:eval_object_reconvla_seed43.json
- seed44: bjb1-18228:eval_object_reconvla_seed44.json
- seed45: bjb2-28827:eval_object_argmin_seed45.json
- seed46: bjb1-32546:eval_object_reconvla_seed46.json
- seed47: bjb1-32546:eval_object_reconvla_seed47.json

**VLA-only baseline (5 seeds):**
- seed42: bjb1-32546:eval_vla_only_object.json
- seed43: bjb1-32546
- seed44: bjb2-40593
- seed45: bjb2-28827
- seed46: ?

**Scalar CRM (4 seeds):**
- seed42: bjb1-32546
- seed43: bjb1-32546
- seed44: bjb1-32546
- seed45: bjb2-28827

Now I'm tracking down the remaining evaluation files across different baselines and seeds, noting which ones are still missing or need verification. Now I'm checking the JSON files across the servers to verify the n_rollouts and success rates for those experiments—particularly the ones the reviewer mentioned with n_rollouts=20, since only one was clearly flagged in the registry. I'll SSH into all four servers in parallel to pull the actual data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "eb434226-c352-47f6-8ffc-d82c4d1c18ec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0137LRxwoxMonVKcc8MYnWHX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6132,
      "cache_creation_input_tokens": 4090,
      "cache_read_input_tokens": 27805,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4090
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

_source line 68_

Good overview from the registry. Now I need to SSH to the servers to verify n_rollouts directly from the JSON files. Let me check all 4 servers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "ada16203-f4a4-4f31-95b5-54363ee85ef3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0137LRxwoxMonVKcc8MYnWHX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6132,
      "cache_creation_input_tokens": 4090,
      "cache_read_input_tokens": 27805,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4090
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

_source line 69_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01TzXfSAMTGRy5QvSHa7iW3X`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/acr-vla-conformal-refinement/logs /root/runs/acr-vla-conformal-refinement -name \"*.json\" -type f 2>/dev/null",
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
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "d57760e2-a68e-43d0-9c8f-ae85e05a4c09",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0137LRxwoxMonVKcc8MYnWHX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6132,
      "cache_creation_input_tokens": 4090,
      "cache_read_input_tokens": 27805,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4090
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

_source line 70 · 2026-05-18T10:47:21.132Z_

<details><summary>↩ Tool result · `toolu_01TzXfSAMTGRy5QvSHa7iW3X`</summary>

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
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "62e6661b-6439-42b2-b11e-79a951f5543f",
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


### Tool call

_source line 71_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01RXzWaw1Y58SYB7UPGoh3g8`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "find /root/acr-vla-conformal-refinement/logs /root/runs/acr-vla-conformal-refinement -name \"*.json\" -type f 2>/dev/null",
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
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "ce02a60d-08ec-4ee8-b8a2-8975a1fb74ee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0137LRxwoxMonVKcc8MYnWHX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6132,
      "cache_creation_input_tokens": 4090,
      "cache_read_input_tokens": 27805,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4090
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

_source line 72 · 2026-05-18T10:47:22.064Z_

<details><summary>↩ Tool result · `toolu_01RXzWaw1Y58SYB7UPGoh3g8`</summary>

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
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "4ed00691-11e9-4d08-9151-77ee4eb8dc12",
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


### Tool call

_source line 73_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01EYJLHVbukEd3KmfrfCT8oj`</summary>

```json
{
  "server": "bjb1-18228",
  "command": "find /root/acr-vla-conformal-refinement/logs /root/runs/acr-vla-conformal-refinement -name \"*.json\" -type f 2>/dev/null",
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
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "4c3e27d7-ef8f-4263-809e-a30f246b9399",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0137LRxwoxMonVKcc8MYnWHX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6132,
      "cache_creation_input_tokens": 4090,
      "cache_read_input_tokens": 27805,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4090
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

_source line 74 · 2026-05-18T10:47:23.025Z_

<details><summary>↩ Tool result · `toolu_01EYJLHVbukEd3KmfrfCT8oj`</summary>

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
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "f6d0e2b2-9f98-482a-bf5e-7b9a3a9d2b10",
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


### Tool call

_source line 75_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Detrmu9d1eTgNvjeNpGcS5`</summary>

```json
{
  "server": "bjb2-40593",
  "command": "find /root/acr-vla-conformal-refinement/logs /root/runs/acr-vla-conformal-refinement -name \"*.json\" -type f 2>/dev/null",
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
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "239e713c-b4d7-417d-9df9-04a4a2d88d1b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0137LRxwoxMonVKcc8MYnWHX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6132,
      "cache_creation_input_tokens": 4090,
      "cache_read_input_tokens": 27805,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4090
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

_source line 76 · 2026-05-18T10:47:23.830Z_

<details><summary>↩ Tool result · `toolu_01Detrmu9d1eTgNvjeNpGcS5`</summary>

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
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "7dc99f73-680f-4b96-bb63-be26504ee2c8",
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

_source line 77_

<details><summary>Logged reasoning block</summary>

```text
The `2>/dev/null` redirect is causing the block. Let me remove the redirect.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "12849334-447f-421b-af3d-c2aec6fba3bd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QKkcB2awJj2ckmxBoekosw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8281,
      "cache_read_input_tokens": 31895,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8281
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

_source line 78_

The `2>/dev/null` redirect is blocked. Let me fix that.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "2f818c9f-3e55-461e-ac0a-32576c94476d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QKkcB2awJj2ckmxBoekosw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8281,
      "cache_read_input_tokens": 31895,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8281
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

_source line 79_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01UaQPaxXbNd74gZNbP5MM4i`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/acr-vla-conformal-refinement/logs -name \"*.json\" -type f",
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
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "be3dab31-570a-43c2-8720-d05e7a3b7e86",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QKkcB2awJj2ckmxBoekosw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8281,
      "cache_read_input_tokens": 31895,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8281
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

_source line 80_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01E4KnDzk8i4At9LzirrtUuu`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "find /root/acr-vla-conformal-refinement/logs -name \"*.json\" -type f",
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
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "85a33be0-f120-4e23-9485-9f2fdcfb56e6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QKkcB2awJj2ckmxBoekosw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8281,
      "cache_read_input_tokens": 31895,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8281
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

_source line 81 · 2026-05-18T10:47:29.214Z_

<details><summary>↩ Tool result · `toolu_01UaQPaxXbNd74gZNbP5MM4i`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_norm.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed43_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed44_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed45.json\\n/root/acr-vla-conformal-refinement/logs/results_direct_correction_object_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_seed45_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_k1_crm_accg_object_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_k1_crm_accg_object_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_k1_crm_accg_object_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed47_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed43_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed43_bjb1-32546.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.02}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "aa6ddd1f-c568-4eee-b776-50ddd649980b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_norm.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed43_r2.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed44_r2.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/results_direct_correction_object_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed47.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed47.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_seed45_r2.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_k1_crm_accg_object_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_k1_crm_accg_object_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_k1_crm_accg_object_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed47_r2.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed43_r2.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed43_bjb1-32546.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.02}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_norm.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed43_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed44_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed45.json\\n/root/acr-vla-conformal-refinement/logs/results_direct_correction_object_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed47.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_seed45_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_k1_crm_accg_object_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_k1_crm_accg_object_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_k1_crm_accg_object_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed47_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed43_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed43_bjb1-32546.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.02}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 82_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01AXXmMav4QVW8ijcb82oV2q`</summary>

```json
{
  "server": "bjb1-18228",
  "command": "find /root/acr-vla-conformal-refinement/logs -name \"*.json\" -type f",
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
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "c9f0d2c7-6abe-477d-b077-3c61018bbdc7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QKkcB2awJj2ckmxBoekosw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8281,
      "cache_read_input_tokens": 31895,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8281
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

_source line 83_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01DBqvyLELrznZLbzmjhH8VV`</summary>

```json
{
  "server": "bjb2-40593",
  "command": "find /root/acr-vla-conformal-refinement/logs -name \"*.json\" -type f",
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
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "6c000c7e-7556-4920-984d-e97bc0d4a4a8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QKkcB2awJj2ckmxBoekosw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8281,
      "cache_read_input_tokens": 31895,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8281
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

_source line 84 · 2026-05-18T10:47:30.170Z_

<details><summary>↩ Tool result · `toolu_01E4KnDzk8i4At9LzirrtUuu`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed43_r3.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_r3.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_argmin_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed45_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed45.json\\n/root/acr-vla-conformal-refinement/logs/latency_profile.json\\n/root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed47.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.94}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "f3c27f34-c839-42bd-ab64-1209c8cbf763",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed43_r3.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_r3.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_argmin_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed45_r2.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/latency_profile.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed47.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.94}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed43_r3.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_r3.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_argmin_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed45_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed45.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed45.json\\n/root/acr-vla-conformal-refinement/logs/latency_profile.json\\n/root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed47.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.94}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 85 · 2026-05-18T10:47:31.283Z_

<details><summary>↩ Tool result · `toolu_01AXXmMav4QVW8ijcb82oV2q`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_reconvla_spatial_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_mag_obsonly_norm03.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_norm_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed45.json\\n/root/acr-vla-conformal-refinement/logs/openvla_single_test.json\\n/root/acr-vla-conformal-refinement/logs/eval_openvla_object_vla_only_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed43_bjb1-18228.json\\n/root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed44_bjb1-18228.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed45_r3.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.09}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "d717e866-97da-4ab6-9a07-9c1cc2d12dd7",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_reconvla_spatial_r2.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_mag_obsonly_norm03.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_seed43.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_norm_r2.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed46.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed44.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed45.json\\\\n/root/acr-vla-conformal-refinement/logs/openvla_single_test.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_openvla_object_vla_only_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed43_bjb1-18228.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed44_bjb1-18228.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed42.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed45_r3.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.09}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_reconvla_spatial_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_mag_obsonly_norm03.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_seed43.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_norm_r2.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed46.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed44.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed45.json\\n/root/acr-vla-conformal-refinement/logs/openvla_single_test.json\\n/root/acr-vla-conformal-refinement/logs/eval_openvla_object_vla_only_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed43_bjb1-18228.json\\n/root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed44_bjb1-18228.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_k5_seed42.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed45_r3.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.09}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 86 · 2026-05-18T10:47:32.221Z_

<details><summary>↩ Tool result · `toolu_01DBqvyLELrznZLbzmjhH8VV`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json\\n/root/acr-vla-conformal-refinement/logs/eval_mag_obsonly_norm003.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "27e9e816-5dcd-4d4e-a6ee-bb8eac45d0e9",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_mag_obsonly_norm003.json\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.9}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json\\n/root/acr-vla-conformal-refinement/logs/eval_mag_obsonly_norm003.json\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 87_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the JSON file listings. Let me now read the key files to check n_rollouts. I need to use python -c to extract the total_rollouts from each JSON file.

Key files I need to check for Part A:

**obs_only ε=0.2 (6 seeds):**
- seed42: bjb1-32546: /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02.json
- seed43: bjb1-32546: /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed43_r2.json


- seed44: bjb1-18228: /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed44.json
- seed45: bjb1-32546: /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed45.json
- seed46: bjb1-18228: /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed46.json
- seed47: bjb1-32546: /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed47.json

I'm also tracking the argmin/reconvla baseline results across six seeds, pulling from various job IDs and log files in the same directory structure. Now I'm tracking down the VLA-only baseline results across the remaining seeds—seed44 through seed46 are scattered across different job IDs. For the Scalar CRM experiments, I'm noticing seed42 is missing from the file listings, and I only have results for seeds 43-45 so far.

Looking at the perdof ε=0.2 results, I've got a more complete picture with seeds 42-47 spread across the servers, though seed47 appears to be cut off mid-listing.

Now I need to check the n_rollouts in each file to understand the scale of these experiments. I'll write a quick script to extract the summary information from each JSON file and see what structure they contain.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "a9106755-4e09-4230-9597-c3d8a71df7b4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017zGdN2iPb7fsR1RYxsM3q6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3473,
      "cache_read_input_tokens": 40176,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3473
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

_source line 88_

Good, I have all file listings. Now let me check the JSON file structure and extract n_rollouts from key files. Let me start by reading one example file and then batch the rest.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "2ddd7945-f4eb-4b20-b384-22b0e94104c8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017zGdN2iPb7fsR1RYxsM3q6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3473,
      "cache_read_input_tokens": 40176,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3473
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

_source line 89_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_0119bnrAy157TJe6AToMXZYS`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "python3 -c \"import json; d=json.load(open('/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02.json')); print(json.dumps({k:v for k,v in d.items() if k!='tasks'}, indent=2))\"",
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
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "3a92891d-a49e-4eab-b085-07b1323500b2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017zGdN2iPb7fsR1RYxsM3q6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3473,
      "cache_read_input_tokens": 40176,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3473
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

_source line 90 · 2026-05-18T10:47:54.241Z_

<details><summary>↩ Tool result · `toolu_0119bnrAy157TJe6AToMXZYS`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "bbaafcf0-1e7b-48b6-b18a-34874d439b15",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 91_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01JdjVKQnsd7eVPQkvXEg5t4`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "python3 -c \"import json; d=json.load(open('/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed45.json')); print(json.dumps({k:v for k,v in d.items() if k!='tasks'}, indent=2))\"",
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
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "fd51b848-b016-4f45-9eb7-45928551c11e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017zGdN2iPb7fsR1RYxsM3q6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3473,
      "cache_read_input_tokens": 40176,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3473
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

_source line 92 · 2026-05-18T10:47:55.447Z_

<details><summary>↩ Tool result · `toolu_01JdjVKQnsd7eVPQkvXEg5t4`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "e544ba93-3396-43b4-93c3-da959789b7e8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 93_

<details><summary>Logged reasoning block</summary>

```text
The semicolons in the python -c command are blocked. Let me use `grep` or `head` to read the files instead, or use `ssh_execute` for python commands.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "def4afa9-6a60-45f2-90f0-6513d88d9bd5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QKWo3kiF7PSsGL6Z9erDPZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1970,
      "cache_read_input_tokens": 43649,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1970
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

_source line 94_

Need to use ssh_execute for python commands, or use grep to extract fields. Let me use grep for the key fields from JSON files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "df0f5a45-2bbc-44e7-9897-97e653d19032",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QKWo3kiF7PSsGL6Z9erDPZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1970,
      "cache_read_input_tokens": 43649,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1970
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

_source line 95_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01AqWN188rurC99EyA4sAQ8f`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "head -30 /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02.json",
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
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "090045cd-52d1-446d-b88e-30ebb5dcc34c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QKWo3kiF7PSsGL6Z9erDPZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1970,
      "cache_read_input_tokens": 43649,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1970
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

_source line 96 · 2026-05-18T10:48:01.526Z_

<details><summary>↩ Tool result · `toolu_01AqWN188rurC99EyA4sAQ8f`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"crm_obs_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 10,\\n  \\\"overall_success_rate\\\": 0.22,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.4,\\n      \\\"successes\\\": 4,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.2,\\n      \\\"successes\\\": 2,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "2cf61b53-ce87-4f31-beef-6733ac5c5111",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"mode\\\\\\\": \\\\\\\"crm_obs_only\\\\\\\",\\\\n  \\\\\\\"baseline_mode\\\\\\\": \\\\\\\"single\\\\\\\",\\\\n  \\\\\\\"benchmark\\\\\\\": \\\\\\\"object\\\\\\\",\\\\n  \\\\\\\"n_rollouts\\\\\\\": 10,\\\\n  \\\\\\\"overall_success_rate\\\\\\\": 0.22,\\\\n  \\\\\\\"per_task\\\\\\\": {\\\\n    \\\\\\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n      \\\\\\\"successes\\\\\\\": 0,\\\\n      \\\\\\\"total\\\\\\\": 10\\\\n    },\\\\n    \\\\\\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n      \\\\\\\"successes\\\\\\\": 0,\\\\n      \\\\\\\"total\\\\\\\": 10\\\\n    },\\\\n    \\\\\\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.3,\\\\n      \\\\\\\"successes\\\\\\\": 3,\\\\n      \\\\\\\"total\\\\\\\": 10\\\\n    },\\\\n    \\\\\\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.4,\\\\n      \\\\\\\"successes\\\\\\\": 4,\\\\n      \\\\\\\"total\\\\\\\": 10\\\\n    },\\\\n    \\\\\\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.2,\\\\n      \\\\\\\"successes\\\\\\\": 2,\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"crm_obs_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 10,\\n  \\\"overall_success_rate\\\": 0.22,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.4,\\n      \\\"successes\\\": 4,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.2,\\n      \\\"successes\\\": 2,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 97_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01VXKT75UYju6V8aQviZxW6p`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "head -30 /root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed45.json",
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
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "e115699e-c3e6-4a28-bd1d-e07afd1620bb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QKWo3kiF7PSsGL6Z9erDPZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1970,
      "cache_read_input_tokens": 43649,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1970
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

_source line 98 · 2026-05-18T10:48:02.028Z_

<details><summary>↩ Tool result · `toolu_01VXKT75UYju6V8aQviZxW6p`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"crm_scalar\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.09,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 2,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.05,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.15,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.05,\\n      \\\"successes\\\": 1,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "5619b42f-ce66-48db-9b37-16a0b458b742",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"mode\\\\\\\": \\\\\\\"crm_scalar\\\\\\\",\\\\n  \\\\\\\"baseline_mode\\\\\\\": \\\\\\\"single\\\\\\\",\\\\n  \\\\\\\"benchmark\\\\\\\": \\\\\\\"object\\\\\\\",\\\\n  \\\\\\\"n_rollouts\\\\\\\": 20,\\\\n  \\\\\\\"overall_success_rate\\\\\\\": 0.09,\\\\n  \\\\\\\"per_task\\\\\\\": {\\\\n    \\\\\\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n      \\\\\\\"successes\\\\\\\": 0,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n      \\\\\\\"successes\\\\\\\": 2,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.05,\\\\n      \\\\\\\"successes\\\\\\\": 1,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.15,\\\\n      \\\\\\\"successes\\\\\\\": 3,\\\\n      \\\\\\\"total\\\\\\\": 20\\\\n    },\\\\n    \\\\\\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.05,\\\\n      \\\\\\\"successes\\\\\\\": 1,\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.31}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"crm_scalar\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 20,\\n  \\\"overall_success_rate\\\": 0.09,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 2,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.05,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.15,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 20\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.05,\\n      \\\"successes\\\": 1,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 99_

<details><summary>Logged reasoning block</summary>

```text
I can see the structure. The JSON files have:
- `n_rollouts` field directly
- `overall_success_rate`
- `per_task` with each task having `total` per task

So for seed42 obs_only norm02: n_rollouts=10, SR=0.22 ✅
For scalar seed45: n_rollouts=20, SR=0.09 — confirmed!

Now I need to batch check all the core data points. Let me use grep to extract n_rollouts from multiple files at once on each server.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "231b2517-82cf-4027-8d60-8cd2b2388470",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RGEddjQU1R8h4yZ7aXKmxs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1616,
      "cache_read_input_tokens": 45619,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1616
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

_source line 100_

Confirmed: scalar seed45 has n_rollouts=20. Now let me batch-check all core data files across all servers. I'll use grep to extract n_rollouts from each file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "e9c37ef3-b8d1-4267-bff6-d64939b6f3cc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RGEddjQU1R8h4yZ7aXKmxs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1616,
      "cache_read_input_tokens": 45619,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1616
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

_source line 101_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01GWyb1M3NsRsUSkz7pPd6mr`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "grep -H \"n_rollouts\" /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02.json /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed43_r2.json /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed45.json /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed47.json /root/acr-vla-conformal-refinement/logs/eval_object_reconvla.json /root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed46.json /root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed47.json /root/acr-vla-conformal-refinement/logs/eval_object_vla_only.json /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed43.json /root/acr-vla-conformal-refinement/logs/eval_object_vla_mean.json /root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed43.json /root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed44.json /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02.json /root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed43.json /root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed44_r2.json",
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
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "07d6a091-d51f-4556-91f3-41fd1e79de26",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RGEddjQU1R8h4yZ7aXKmxs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1616,
      "cache_read_input_tokens": 45619,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1616
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

_source line 102 · 2026-05-18T10:48:12.240Z_

<details><summary>↩ Tool result · `toolu_01GWyb1M3NsRsUSkz7pPd6mr`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed43_r2.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed45.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed47.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed46.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed47.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed43.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed43.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed44.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed43.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed44_r2.json:  \\\"n_rollouts\\\": 10,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "9cb3687e-14a7-4748-8aac-958bd0290629",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02.json:  \\\\\\\"n_rollouts\\\\\\\": 10,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed43_r2.json:  \\\\\\\"n_rollouts\\\\\\\": 10,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed45.json:  \\\\\\\"n_rollouts\\\\\\\": 10,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed47.json:  \\\\\\\"n_rollouts\\\\\\\": 10,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla.json:  \\\\\\\"n_rollouts\\\\\\\": 10,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed46.json:  \\\\\\\"n_rollouts\\\\\\\": 10,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed47.json:  \\\\\\\"n_rollouts\\\\\\\": 10,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only.json:  \\\\\\\"n_rollouts\\\\\\\": 10,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed43.json:  \\\\\\\"n_rollouts\\\\\\\": 10,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean.json:  \\\\\\\"n_rollouts\\\\\\\": 10,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed43.json:  \\\\\\\"n_rollouts\\\\\\\": 10,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed44.json:  \\\\\\\"n_rollouts\\\\\\\": 10,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02.json:  \\\\\\\"n_rollouts\\\\\\\": 10,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed43.json:  \\\\\\\"n_rollouts\\\\\\\": 10,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed44_r2.json:  \\\\\\\"n_rollouts\\\\\\\": 10,\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed43_r2.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed45.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed47.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed46.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed47.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed43.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed43.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed44.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed43.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed44_r2.json:  \\\"n_rollouts\\\": 10,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 103_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Q8k7griZtVGV42gDATktmU`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "grep -H \"n_rollouts\" /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed43_r3.json /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed44.json /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed45.json /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed46.json /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed47.json /root/acr-vla-conformal-refinement/logs/eval_object_argmin_seed45.json /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed45.json /root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed45.json /root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed45.json /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed45.json /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed45_r2.json",
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
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "136b6159-e012-437f-9d64-d0d6f8a961fb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RGEddjQU1R8h4yZ7aXKmxs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1616,
      "cache_read_input_tokens": 45619,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1616
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

_source line 104 · 2026-05-18T10:48:15.966Z_

<details><summary>↩ Tool result · `toolu_01Q8k7griZtVGV42gDATktmU`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed43_r3.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed44.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed45.json:  \\\"n_rollouts\\\": 20,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed46.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed47.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_argmin_seed45.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed45.json:  \\\"n_rollouts\\\": 20,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed45.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed45.json:  \\\"n_rollouts\\\": 20,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed45.json:  \\\"n_rollouts\\\": 20,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed45_r2.json:  \\\"n_rollouts\\\": 10,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "d94341b8-d62f-485c-813d-39b27468d08b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed43_r3.json:  \\\\\\\"n_rollouts\\\\\\\": 10,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed44.json:  \\\\\\\"n_rollouts\\\\\\\": 10,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed45.json:  \\\\\\\"n_rollouts\\\\\\\": 20,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed46.json:  \\\\\\\"n_rollouts\\\\\\\": 10,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed47.json:  \\\\\\\"n_rollouts\\\\\\\": 10,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_argmin_seed45.json:  \\\\\\\"n_rollouts\\\\\\\": 10,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed45.json:  \\\\\\\"n_rollouts\\\\\\\": 20,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed45.json:  \\\\\\\"n_rollouts\\\\\\\": 10,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed45.json:  \\\\\\\"n_rollouts\\\\\\\": 20,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed45.json:  \\\\\\\"n_rollouts\\\\\\\": 20,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed45_r2.json:  \\\\\\\"n_rollouts\\\\\\\": 10,\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.31}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed43_r3.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed44.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed45.json:  \\\"n_rollouts\\\": 20,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed46.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed47.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_argmin_seed45.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed45.json:  \\\"n_rollouts\\\": 20,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed45.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed45.json:  \\\"n_rollouts\\\": 20,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed45.json:  \\\"n_rollouts\\\": 20,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed45_r2.json:  \\\"n_rollouts\\\": 10,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 105_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01GcZWZvPTrkegb1WFNQMauc`</summary>

```json
{
  "server": "bjb1-18228",
  "command": "grep -H \"n_rollouts\" /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed44.json /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed46.json /root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed43.json /root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed44.json /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed46.json /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_seed43.json /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed45_r3.json /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed45.json /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed44.json",
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
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "cf8380e3-889b-4320-8195-15c9a667e7be",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RGEddjQU1R8h4yZ7aXKmxs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1616,
      "cache_read_input_tokens": 45619,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1616
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

_source line 106 · 2026-05-18T10:48:18.855Z_

<details><summary>↩ Tool result · `toolu_01GcZWZvPTrkegb1WFNQMauc`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed44.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed46.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed43.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed44.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed46.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_seed43.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed45_r3.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed45.json:  \\\"n_rollouts\\\": 20,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed44.json:  \\\"n_rollouts\\\": 10,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "803edfe0-3d24-487c-95f3-f9fd05add5ac",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed44.json:  \\\\\\\"n_rollouts\\\\\\\": 10,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed46.json:  \\\\\\\"n_rollouts\\\\\\\": 10,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed43.json:  \\\\\\\"n_rollouts\\\\\\\": 10,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed44.json:  \\\\\\\"n_rollouts\\\\\\\": 10,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed46.json:  \\\\\\\"n_rollouts\\\\\\\": 10,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_seed43.json:  \\\\\\\"n_rollouts\\\\\\\": 10,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed45_r3.json:  \\\\\\\"n_rollouts\\\\\\\": 10,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed45.json:  \\\\\\\"n_rollouts\\\\\\\": 20,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed44.json:  \\\\\\\"n_rollouts\\\\\\\": 10,\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed44.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed46.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed43.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed44.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed46.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_seed43.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed45_r3.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed45.json:  \\\"n_rollouts\\\": 20,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed44.json:  \\\"n_rollouts\\\": 10,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 107_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01RS41q1uN6fRXtqKrywfpq5`</summary>

```json
{
  "server": "bjb2-40593",
  "command": "grep -H \"n_rollouts\" /root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json",
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
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "5b71d8b6-6adf-405f-84ea-36f4a87a08fd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RGEddjQU1R8h4yZ7aXKmxs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1616,
      "cache_read_input_tokens": 45619,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1616
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

_source line 108 · 2026-05-18T10:48:19.991Z_

<details><summary>↩ Tool result · `toolu_01RS41q1uN6fRXtqKrywfpq5`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json:  \\\"n_rollouts\\\": 10,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "a237da11-4bb7-4281-b45b-e1eb15fc0a1f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json:  \\\\\\\"n_rollouts\\\\\\\": 10,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json:  \\\\\\\"n_rollouts\\\\\\\": 10,\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.32}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json:  \\\"n_rollouts\\\": 10,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 109_

<details><summary>Logged reasoning block</summary>

```text
Excellent! Now I have a comprehensive picture. Let me also get the SR values for these files. Let me also check a few more files I missed and get the SR for the ones I'm interested in.

Key findings so far on n_rollouts:

**n_rollouts=20 files found:**
1. bjb2-28827: eval_object_perdof_norm02_seed45.json — n_rollouts=20 ⚠️ **THIS IS IN CORE DATA**
2. bjb2-28827: eval_object_vla_only_seed45.json — n_rollouts=20 ⚠️ **THIS IS IN CORE DATA** 


3. bjb2-28827: eval_object_scalar_seed45.json — n_rollouts=20 ⚠️ **THIS IS IN CORE DATA**
4. bjb2-28827: eval_object_obs_only_default_seed45.json — n_rollouts=20 (uncapped, in magnitude curve)
5. bjb1-18228: eval_object_obs_only_norm01_seed45.json — n_rollouts=20 ⚠️ (in magnitude curve)

All n_rollouts=10 variants are the obs_only ε=0.2 seeds.

I'm seeing a clear pattern across all the other configurations — reconvla, argmin, vla_mean, scalar, and perdof norm02 variants all have n_rollouts=10 across their seed ranges. But seed45 consistently shows up with n_rollouts=10 in the obs_only ε=0.2 case, which suggests this is a systematic issue specific to that seed rather than a configuration problem. I'm noticing a critical inconsistency in the perdof ε=0.2 data — the original seed45 run used n_rollouts=20 and achieved SR=9%, while the r3 version with n_rollouts=10 got SR=12%, so I need to swap in the r3 version to keep the rollout counts consistent across my comparisons. I should also verify the success rates for all the files I'm tracking and check the magnitude curve files for the other epsilon values in obs_only.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "fb50d710-4415-4a83-b0ff-7de1c376a43a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VR8HhUyvVkAokRm3x2ZvPh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3838,
      "cache_read_input_tokens": 47235,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3838
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

_source line 110_

Critical findings emerging. seed45 has systematic n_rollouts=20 on bjb2-28827. Let me now get SR values and check remaining magnitude curve files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "f0f2188c-2e6c-4816-a14e-f53b1a307e0f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VR8HhUyvVkAokRm3x2ZvPh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3838,
      "cache_read_input_tokens": 47235,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3838
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

_source line 111_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01DTD6FomPqFdZysRK2vQqaw`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "grep \"overall_success_rate\" /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed45.json /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed45.json /root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed45.json /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed45.json /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed43_r3.json /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed44.json /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed46.json /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed47.json /root/acr-vla-conformal-refinement/logs/eval_object_argmin_seed45.json /root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed45.json /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed45_r2.json",
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
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "998e9661-3330-424f-aa0e-c0d688888680",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VR8HhUyvVkAokRm3x2ZvPh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3838,
      "cache_read_input_tokens": 47235,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3838
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

_source line 112 · 2026-05-18T10:48:44.397Z_

<details><summary>↩ Tool result · `toolu_01DTD6FomPqFdZysRK2vQqaw`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed45.json:  \\\"overall_success_rate\\\": 0.09,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed45.json:  \\\"overall_success_rate\\\": 0.09,\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed45.json:  \\\"overall_success_rate\\\": 0.09,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed45.json:  \\\"overall_success_rate\\\": 0.12,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed43_r3.json:  \\\"overall_success_rate\\\": 0.09,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed44.json:  \\\"overall_success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed46.json:  \\\"overall_success_rate\\\": 0.09,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed47.json:  \\\"overall_success_rate\\\": 0.11,\\n/root/acr-vla-conformal-refinement/logs/eval_object_argmin_seed45.json:  \\\"overall_success_rate\\\": 0.12,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed45.json:  \\\"overall_success_rate\\\": 0.13,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed45_r2.json:  \\\"overall_success_rate\\\": 0.14,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "34507854-c970-4fcb-aed1-20a929c542df",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed45.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.09,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed45.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.09,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed45.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.09,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed45.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.12,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed43_r3.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.09,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed44.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed46.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.09,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed47.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.11,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_argmin_seed45.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.12,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed45.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.13,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed45_r2.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.14,\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.31}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed45.json:  \\\"overall_success_rate\\\": 0.09,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed45.json:  \\\"overall_success_rate\\\": 0.09,\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed45.json:  \\\"overall_success_rate\\\": 0.09,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed45.json:  \\\"overall_success_rate\\\": 0.12,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed43_r3.json:  \\\"overall_success_rate\\\": 0.09,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed44.json:  \\\"overall_success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed46.json:  \\\"overall_success_rate\\\": 0.09,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed47.json:  \\\"overall_success_rate\\\": 0.11,\\n/root/acr-vla-conformal-refinement/logs/eval_object_argmin_seed45.json:  \\\"overall_success_rate\\\": 0.12,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean_seed45.json:  \\\"overall_success_rate\\\": 0.13,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed45_r2.json:  \\\"overall_success_rate\\\": 0.14,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 113_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Cfy1LFQBka25WoEcsiHjXQ`</summary>

```json
{
  "server": "bjb1-18228",
  "command": "grep \"overall_success_rate\" /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed45_r3.json /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed45.json /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed46.json",
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
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "43ea7f13-f658-42f0-9277-f275eb9afb0b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VR8HhUyvVkAokRm3x2ZvPh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3838,
      "cache_read_input_tokens": 47235,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3838
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

_source line 114 · 2026-05-18T10:48:46.181Z_

<details><summary>↩ Tool result · `toolu_01Cfy1LFQBka25WoEcsiHjXQ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed45_r3.json:  \\\"overall_success_rate\\\": 0.12,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed45.json:  \\\"overall_success_rate\\\": 0.14,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed46.json:  \\\"overall_success_rate\\\": 0.13,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "a48b641a-0ae0-4bf0-890b-ab87761ac38d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed45_r3.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.12,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed45.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.14,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed46.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.13,\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02_seed45_r3.json:  \\\"overall_success_rate\\\": 0.12,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed45.json:  \\\"overall_success_rate\\\": 0.14,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed46.json:  \\\"overall_success_rate\\\": 0.13,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 115_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_016okhRGSiMyDHLukhyaL35g`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "grep -H \"overall_success_rate\" /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02.json /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed43_r2.json /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed45.json /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed47.json /root/acr-vla-conformal-refinement/logs/eval_object_reconvla.json /root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed46.json /root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed47.json /root/acr-vla-conformal-refinement/logs/eval_object_vla_only.json /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed43.json /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02.json /root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed43.json /root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed44_r2.json",
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
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "15f9b0a2-8669-402d-b927-28d2e3d44d07",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VR8HhUyvVkAokRm3x2ZvPh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3838,
      "cache_read_input_tokens": 47235,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3838
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

_source line 116 · 2026-05-18T10:48:49.649Z_

<details><summary>↩ Tool result · `toolu_016okhRGSiMyDHLukhyaL35g`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02.json:  \\\"overall_success_rate\\\": 0.22,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed43_r2.json:  \\\"overall_success_rate\\\": 0.16,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed45.json:  \\\"overall_success_rate\\\": 0.16,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed47.json:  \\\"overall_success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla.json:  \\\"overall_success_rate\\\": 0.12,\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed46.json:  \\\"overall_success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed47.json:  \\\"overall_success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only.json:  \\\"overall_success_rate\\\": 0.12,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed43.json:  \\\"overall_success_rate\\\": 0.12,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02.json:  \\\"overall_success_rate\\\": 0.11,\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed43.json:  \\\"overall_success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed44_r2.json:  \\\"overall_success_rate\\\": 0.06,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "5af2af51-dc7d-4bba-b29a-3a4e22c38375",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.22,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed43_r2.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.16,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed45.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.16,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed47.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.2,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.12,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed46.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed47.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.12,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed43.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.12,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.11,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed43.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.1,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed44_r2.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.06,\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02.json:  \\\"overall_success_rate\\\": 0.22,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed43_r2.json:  \\\"overall_success_rate\\\": 0.16,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed45.json:  \\\"overall_success_rate\\\": 0.16,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02_seed47.json:  \\\"overall_success_rate\\\": 0.2,\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla.json:  \\\"overall_success_rate\\\": 0.12,\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed46.json:  \\\"overall_success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_reconvla_seed47.json:  \\\"overall_success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only.json:  \\\"overall_success_rate\\\": 0.12,\\n/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed43.json:  \\\"overall_success_rate\\\": 0.12,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm02.json:  \\\"overall_success_rate\\\": 0.11,\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed43.json:  \\\"overall_success_rate\\\": 0.1,\\n/root/acr-vla-conformal-refinement/logs/eval_object_scalar_seed44_r2.json:  \\\"overall_success_rate\\\": 0.06,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 117_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_013RCCYnyzvudwUh21WeoYH3`</summary>

```json
{
  "server": "bjb2-40593",
  "command": "grep -H \"overall_success_rate\" /root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json",
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
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "7a11add6-4b77-42f2-a936-904b7e77ef3a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VR8HhUyvVkAokRm3x2ZvPh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3838,
      "cache_read_input_tokens": 47235,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3838
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

_source line 118 · 2026-05-18T10:48:50.472Z_

<details><summary>↩ Tool result · `toolu_013RCCYnyzvudwUh21WeoYH3`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json:  \\\"overall_success_rate\\\": 0.1,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "539a6d0f-3eb5-40bc-86da-35b10839baa1",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json:  \\\\\\\"overall_success_rate\\\\\\\": 0.1,\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.32}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_only_seed44.json:  \\\"overall_success_rate\\\": 0.1,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 119_

<details><summary>Logged reasoning block</summary>

```text
Now let me also check the remaining magnitude curve files. I need to verify:
1. obs_only ε=0.1 seed45 — on bjb1-18228, n_rollouts=20, SR=0.14 — IN MAGNITUDE CURVE
2. obs_only default seed45 — on bjb2-28827, n_rollouts=20, SR=0.12 — IN MAGNITUDE CURVE

And the remaining magnitude curve files I haven't checked yet. Let me also check:
- obs_only ε=0.03 seed42 on bjb1-32546


- obs_only ε=0.05 seed42 on bjb2-28827
- obs_only ε=0.05 seed43 on bjb1-32546
- obs_only ε=0.1 seed42 on bjb1-32546
- obs_only ε=0.1 seed43 on bjb1-18228
- obs_only ε=0.1 seed44 on bjb1-32546
- obs_only ε=0.3 seed42 on bjb2-28827
- obs_only ε=0.3 seed44 on bjb1-32546
- obs_only ε=0.3 seed46 on bjb1-32546
- obs_only default seed44 on bjb1-32546
- obs_only default seed46 on bjb1-32546

I'm also tracking the perdof experiments with various epsilon values and seeds across the same cluster nodes, ranging from ε=0.03 up to ε=0.3.

For the baselines, I need to locate the scalar seed42 file—the registry shows it's eval-acr-object-v4-scalar. I'm also verifying the argmin baseline with seed42, which corresponds to eval-reconvla-object on bjb1-32546 with n_rollouts=10 and SR=0.12. The VLA-only seed45 on bjb2-28827 has n_rollouts=20 and SR=0.09, which is what's currently in the paper.

Now I need to check the remaining magnitude curve configurations and track down that scalar seed42 file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "6a9f7e06-cc4b-4377-b675-a0268aecfa20",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Zyx6DeHW7b18PZJVkPyrF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4127,
      "cache_read_input_tokens": 51073,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4127
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

_source line 120_

Now let me check the remaining magnitude curve files and find the scalar seed42 source.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "a7dac315-1340-4532-b557-ceffaab20bcb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Zyx6DeHW7b18PZJVkPyrF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4127,
      "cache_read_input_tokens": 51073,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4127
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

_source line 121_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01TyaeHsP247CXi7HYuZpexn`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "grep -H \"n_rollouts\" /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003.json /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed44.json /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed44.json /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed46.json /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed44.json /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_norm.json /root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json /root/acr-vla-conformal-refinement/logs/eval_object_perdof.json /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed45.json /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed46.json /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed47_r2.json /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_seed45_r2.json /root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_seed46.json /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed43_r2.json",
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
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "e778fd0d-84be-46c4-89f7-c733da711472",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Zyx6DeHW7b18PZJVkPyrF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4127,
      "cache_read_input_tokens": 51073,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4127
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

_source line 122 · 2026-05-18T10:49:10.499Z_

<details><summary>↩ Tool result · `toolu_01TyaeHsP247CXi7HYuZpexn`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed44.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed44.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed46.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed44.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_norm.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed45.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed46.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed47_r2.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_seed45_r2.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_seed46.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed43_r2.json:  \\\"n_rollouts\\\": 10,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "d2d1bccf-2132-4cc5-86cf-0534525e274d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003.json:  \\\\\\\"n_rollouts\\\\\\\": 10,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed44.json:  \\\\\\\"n_rollouts\\\\\\\": 10,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed44.json:  \\\\\\\"n_rollouts\\\\\\\": 10,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed46.json:  \\\\\\\"n_rollouts\\\\\\\": 10,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed44.json:  \\\\\\\"n_rollouts\\\\\\\": 10,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_norm.json:  \\\\\\\"n_rollouts\\\\\\\": 10,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json:  \\\\\\\"n_rollouts\\\\\\\": 10,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof.json:  \\\\\\\"n_rollouts\\\\\\\": 10,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed45.json:  \\\\\\\"n_rollouts\\\\\\\": 10,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed46.json:  \\\\\\\"n_rollouts\\\\\\\": 10,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed47_r2.json:  \\\\\\\"n_rollouts\\\\\\\": 10,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_seed45_r2.json:  \\\\\\\"n_rollouts\\\\\\\": 10,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_seed46.json:  \\\\\\\"n_rollouts\\\\\\\": 10,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed43_r2.json:  \\\\\\\"n_rollouts\\\\\\\": 10,\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm003.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm01_seed44.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed44.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03_seed46.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed44.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_norm.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed45.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed46.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm01_seed47_r2.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_seed45_r2.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_seed46.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005_seed43_r2.json:  \\\"n_rollouts\\\": 10,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 123_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_0149R5obTRsUcmTvvrDgFb8W`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "grep -H \"n_rollouts\" /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03.json /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005.json /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003.json /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005.json /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_r3.json /root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed42.json",
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
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "7b609865-897a-43f2-a61d-38534c0ecddb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Zyx6DeHW7b18PZJVkPyrF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4127,
      "cache_read_input_tokens": 51073,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4127
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

_source line 124 · 2026-05-18T10:49:13.297Z_

<details><summary>↩ Tool result · `toolu_0149R5obTRsUcmTvvrDgFb8W`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_r3.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed42.json:  \\\"n_rollouts\\\": 10,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.33}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "7c110139-ed7b-446c-9dca-7782f1356f9c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03.json:  \\\\\\\"n_rollouts\\\\\\\": 10,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005.json:  \\\\\\\"n_rollouts\\\\\\\": 10,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003.json:  \\\\\\\"n_rollouts\\\\\\\": 10,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005.json:  \\\\\\\"n_rollouts\\\\\\\": 10,\\\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_r3.json:  \\\\\\\"n_rollouts\\\\\\\": 10,\\\\n/root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed42.json:  \\\\\\\"n_rollouts\\\\\\\": 10,\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.33}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm03.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm005.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm003.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm005.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_r3.json:  \\\"n_rollouts\\\": 10,\\n/root/acr-vla-conformal-refinement/logs/eval_k1_crm_multiscale_object_seed42.json:  \\\"n_rollouts\\\": 10,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.33}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 125_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01JqtNDjDz9kMrWxxVETsYfH`</summary>

```json
{
  "server": "bjb1-18228",
  "command": "grep -H \"n_rollouts\" /root/acr-vla-conformal-refinement/logs/eval_object_obs_only_seed43.json /root/acr-vla-conformal-refinement/logs/eval_object_perdof_seed43.json /root/acr-vla-conformal-refinement/logs/eval_object_perdof_seed44.json /root/acr-vla-conformal-refinement/logs/eval_object_perdof_norm03_seed44.json /root/acr-vla-conformal-refinement/logs/eval_object_perdof_default_norm_r2.json",
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
  "session_id": "c1bdccab-16c6-497c-9d30-0feab97d927d",
  "uuid": "f38f10fe-e9d6-4f1d-9562-67951b4a34d2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Zyx6DeHW7b18PZJVkPyrF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4127,
      "cache_read_input_tokens": 51073,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4127
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
