# research scienceworld registry history

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 87
- **Recorded user turns:** 2
- **Tool calls:** 25
- **Original source:** `logs/workers/worker_research_scienceworld_registry_history_20260522T033549.log`
- **Structured JSON:** [`63a69fccd40b215ac32e.json`](../../sessions/63/63a69fccd40b215ac32e.json)

## Before a recorded user message

25 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
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
  "uuid": "d14250d3-77e3-47a3-9836-f9fe9d24aed1",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-1-projects-cost-verify-agent-rl/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Assistant

_source line 3_

<details><summary>Logged reasoning block</summary>

```text
Let me start by loading the MCP tools I need, then gather information from multiple sources in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "55e1223b-71ce-409d-9d31-00989be02a52",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013NzmUJj4DWWnv1De5XL4XL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12550,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12550
      },
      "output_tokens": 20,
      "service_tier": "standard",
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

Let我先加载需要的 MCP 工具，然后并行收集信息。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "00c0ca99-8e72-4fcf-b2f7-2d1355bb3378",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013NzmUJj4DWWnv1De5XL4XL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12550,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12550
      },
      "output_tokens": 20,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01KK5b7LUuEPQ2vPkQidreeX`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file",
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
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "8fed65a2-4af2-41ad-a163-4c332f8a1516",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013NzmUJj4DWWnv1De5XL4XL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12550,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12550
      },
      "output_tokens": 20,
      "service_tier": "standard",
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

_source line 6 · 2026-05-22T03:36:02.228Z_

<details><summary>↩ Tool result · `toolu_01KK5b7LUuEPQ2vPkQidreeX`</summary>

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
  "tool_name": "mcp__agent-ml-research__read_project_file"
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
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "e09f09fd-f398-4c75-a1d7-024352d7722e",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Runtime record

_source line 7_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1779438600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "99b22612-e601-4e6f-a3fb-920ccf697f03",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb"
}
```

---

### Assistant

_source line 8_

<details><summary>Logged reasoning block</summary>

```text
Now let me gather information from multiple sources in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "6e4e5119-e4fa-40cc-91e8-85f2bacc3a1f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QQZd1sWwcKS9LP7FXrQnW1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 842,
      "cache_read_input_tokens": 24391,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 842
      },
      "output_tokens": 32,
      "service_tier": "standard",
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

_source line 9_

并行收集所有相关信息。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "0c28f282-255a-4ba6-8704-0d5a87f02084",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QQZd1sWwcKS9LP7FXrQnW1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 842,
      "cache_read_input_tokens": 24391,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 842
      },
      "output_tokens": 32,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01RGNr1VRd6SFTjSJiBXYyuV`</summary>

```json
{
  "project": "cost-verify-agent-rl",
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
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "399b0325-b2d3-4895-9eee-6a741af46cee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QQZd1sWwcKS9LP7FXrQnW1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 842,
      "cache_read_input_tokens": 24391,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 842
      },
      "output_tokens": 32,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01TjeMFVvP7m1kvPWE89mCZv`</summary>

```json
{
  "project": "cost-verify-agent-rl",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "8c86d514-4ee0-42f8-a0e3-54e0ebac4f20",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QQZd1sWwcKS9LP7FXrQnW1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 842,
      "cache_read_input_tokens": 24391,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 842
      },
      "output_tokens": 32,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01NzDd8teyKzcjuWqQ8S1QN1`</summary>

```json
{
  "project": "cost-verify-agent-rl",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "2079e271-3fcb-42b5-8d7c-31ab79c8d2b9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QQZd1sWwcKS9LP7FXrQnW1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 842,
      "cache_read_input_tokens": 24391,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 842
      },
      "output_tokens": 32,
      "service_tier": "standard",
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

_source line 13 · 2026-05-22T03:36:07.348Z_

<details><summary>↩ Tool result · `toolu_01RGNr1VRd6SFTjSJiBXYyuV`</summary>

```text
Error: result (271,315 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-1-projects-cost-verify-agent-rl/54b94781-146b-4013-9381-11e3737077cb/tool-results/mcp-agent-ml-research-read_registry-1779420967332.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-1-projects-cost-verify-agent-rl/54b94781-146b-4013-9381-11e3737077cb/tool-results/mcp-agent-ml-research-read_registry-1779420967332.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-1-projects-cost-verify-agent-rl/54b94781-146b-4013-9381-11e3737077cb/tool-results/mcp-agent-ml-research-read_registry-1779420967332.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "dcd90077-bc18-43e1-b2f2-e2c320db3a68",
  "tool_use_result": {
    "content": "Error: result (271,315 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-1-projects-cost-verify-agent-rl/54b94781-146b-4013-9381-11e3737077cb/tool-results/mcp-agent-ml-research-read_registry-1779420967332.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-1-projects-cost-verify-agent-rl/54b94781-146b-4013-9381-11e3737077cb/tool-results/mcp-agent-ml-research-read_registry-1779420967332.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-1-projects-cost-verify-agent-rl/54b94781-146b-4013-9381-11e3737077cb/tool-results/mcp-agent-ml-research-read_registry-1779420967332.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"exp029_seed6_step15_ood\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T01:59:56.936Z\", \"updated_at\": \"2026-05-22T03:24:27.048Z\", \"spec\": {\"command\": \"cd /root/cost-verify-agent-rl && CUDA_VISIBLE_DEVICES=1 python RAGEN/eval/eval_ood.py --checkpoint_path /root/autodl-tmp/checkpoints/qwen_seed6_step15_hf --max_turn 50 --num_episodes 134 --temperature 0.4\", \"server\": \"bjb1-17606\", \"gpu\": [\"cuda:1\"], \"pid\": \"383485\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp029_seed6_step15_ood.log\", \"submitted_at\": \"2026-05-22T01:59:56.545Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"ALFWorld OOD 134 tasks\", \"data_count\": 134, \"model_name\": \"Qwen3-1.5B (seed6 step15)\", \"seed\": 6, \"checkpoint_source\": \"exp029_seed6 global_step_15_hf (SCP from westd)\", \"eval_data\": \"ALFWorld OOD 134 tasks\"}, \"hypothesis\": \"OOD eval for seed 6 step 15 checkpoint. Seed 6 exhibited collapse behavior. OOD success rate shows generalization impact of seed collapse, contributing to paper Table 1.\"}, \"exp029_seed5_step10_ood\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T01:59:30.305Z\", \"updated_at\": \"2026-05-22T03:24:24.882Z\", \"spec\": {\"command\": \"cd /root/cost-verify-agent-rl && CUDA_VISIBLE_DEVICES=0 python RAGEN/eval/eval_ood.py --checkpoint_path /root/autodl-tmp/checkpoints/qwen_seed5_step10_hf --max_turn 50 --num_episodes 134 --temperature 0.4\", \"server\": \"bjb1-17606\", \"gpu\": [\"cuda:0\"], \"pid\": \"382718\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp029_seed5_step10_ood.log\", \"submitted_at\": \"2026-05-22T02:06:30.360Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"ALFWorld OOD 134 tasks\", \"data_count\": 134, \"model_name\": \"Qwen3-1.5B (seed5 step10)\", \"seed\": 5, \"checkpoint_source\": \"exp029_seed5 global_step_10_hf (SCP from westd)\", \"eval_data\": \"ALFWorld OOD 134 tasks\"}, \"hypothesis\": \"OOD eval for seed 5 step 10 checkpoint. Seed 5 is a stable (non-collapsed) seed. OOD success rate establishes the generalization baseline for healthy seeds at step 10, contributing to paper Table 1.\"}, \"exp029_c_prime_resume_mt50_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T02:28:34.487Z\", \"updated_at\": \"2026-05-22T03:23:39.029Z\", \"hypothesis\": \"C' resume from step 5 with max_turn=50, optimizer_offload=false. Retry of exp029_c_prime_resume_mt50 which crashed due to optimizer_offload device mismatch. If step 6-7 train_success recovers >15%, trajectory cap approach is salvageable. If <10%, max_turn=25 training damage is irreversible.\", \"parent\": \"exp029_intervention_c_prime\", \"spec\": {\"command\": \"cd /root/cost-verify-agent-rl && CUDA_VISIBLE_DEVICES=0,1 RAY_TMPDIR=/root/autodl-tmp/ray_tmp python train.py --config-name _alfworld_c_prime_resume_mt50\", \"server\": \"bjb1\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"376153\", \"data_path\": \"ALFWorld episode-level\", \"data_count\": 134, \"model_name\": \"Qwen3-1.5B\", \"seed\": 999, \"checkpoint_source\": \"exp029_intervention_c_prime global_step_5\", \"eval_data\": \"ALFWorld valid_unseen 32 episodes\", \"wandb_run_id\": \"u6jn1njs\", \"resume_from\": \"/root/autodl-tmp/checkpoints/exp029_intervention_c_prime/global_step_5/\", \"optimizer_offload\": false, \"max_turn\": 50, \"total_training_steps\": 7, \"save_freq\": 5, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/exp029_intervention_c_prime/global_step_7/\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp029_c_prime_resume_mt50.log\"}, \"failure_reason\": \"Cron misreported as failed (wrong server name bjb1 vs bjb1-17606). Training actually completed successfully (EXIT_CODE=0). Conclusion is negative: val_success declined 21.875%→18.75%, response length inflation continued (rollout 11440→13304). max_turn=25 training error caused irreversible damage.\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-22T02:40:21.815Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T02:40:27.125663+00:00\"}]}, \"metrics\": {\"step6_train_success\": 31.25, \"step7_train_success\": 16.41, \"step5_val_success\": 21.875, \"step7_val_success\": 18.75, \"step6_rollout_response_length\": 11440, \"step7_rollout_response_length\": 13304, \"step7_val_response_length\": 7020, \"step6_action_is_valid\": 0.712, \"step7_action_is_valid\": 0.704}}, \"exp029_c_prime_resume_mt50\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T01:37:52.570Z\", \"updated_at\": \"2026-05-22T02:10:03.387Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/cost-verify-agent-rl/RAGEN && RAY_TMPDIR=/root/autodl-tmp/ray_tmp python train.py --config-name _alfworld_c_prime_resume_mt50\\\"\", \"server\": \"bjb1-17606\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"376153\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp029_c_prime_resume_mt50.log\", \"submitted_at\": \"2026-05-22T02:10:02.678Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"C' resume from step 5 with max_turn=50 (fixing design error of max_turn=25). If step 6-7 train_success recovers >15%, trajectory cap approach is salvageable with correct max_turn. If <10%, the damage from 5 steps of max_turn=25 training is irreversible.\", \"parent\": \"exp029_intervention_c_prime\", \"reproduce\": {\"finished_at\": \"2026-05-22T02:04:52.751Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-22T02:04:54.915Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T02:04:58.971260+00:00\"}]}}, \"exp029_new_seed_2048\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T01:57:22.267Z\", \"updated_at\": \"2026-05-22T02:01:21.488Z\", \"spec\": {\"command\": \"python train.py --config-name _alfworld_new_seed_2048\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:2\", \"cuda:3\"], \"pid\": \"79754\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp029_new_seed_2048.log\", \"submitted_at\": \"2026-05-22T01:57:21.879Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"ALFWorld episode-level\", \"data_count\": 134, \"model_name\": \"Qwen3-1.5B\", \"seed\": 2048, \"checkpoint_source\": \"qwen3_exp021_ragen_sft_v4 (SFT base)\", \"eval_data\": \"ALFWorld valid_unseen 32 episodes\"}, \"hypothesis\": \"New seed (2048) episode-level GRPO with max_turn=50, 5 steps only. Provides stable-seed step-5 checkpoint for OOD eval as paper Table 1 control — establishing step-5 OOD baseline without any intervention or collapse.\"}, \"exp029_c_prime_resume\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T01:19:33.287Z\", \"updated_at\": \"2026-05-22T01:19:33.287Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/cost-verify-agent-rl/RAGEN && RAY_TMPDIR=/root/autodl-tmp/ray_tmp python train.py --config-name _alfworld_c_prime_resume_step5\\\"\", \"server\": \"bjb1-17606\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"362509\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp029_c_prime_resume.log\", \"submitted_at\": \"2026-05-22T01:19:32.885Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"seed7_high_kl_step5_ood_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T23:56:31.101Z\", \"updated_at\": \"2026-05-22T01:15:40.622Z\", \"hypothesis\": \"Seed 7 with high-KL intervention at step 5 (mid-training) OOD eval. Retry of seed7_high_kl_step5_ood which failed on first attempt (Ray/ALFWorld init failure).\", \"parent\": \"exp029_seed7_high_kl\", \"spec\": {\"command\": \"python train.py --config-name _alfworld_seed7_kl_step5_ood_eval\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:3\"], \"pid\": \"968497\", \"data_path\": \"ALFWorld OOD 134 episodes\", \"data_count\": 134, \"model_name\": \"Qwen3-1.5B (seed7 high-KL step 5)\", \"seed\": 789, \"checkpoint_source\": \"qwen_exp029_seed7_high_kl_step5_hf\", \"eval_data\": \"ALFWorld OOD 134 episodes\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T00:22:46.063Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T00:22:48.104Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T00:22:51.922018+00:00\"}]}, \"notes\": \"OOD success 9.70% (13/134 episodes). Seed 7 high-KL intervention step 5 (mid-training). Consistent with other intervention variants producing 10-15% OOD — policy-constraining interventions limit generalization.\", \"metrics\": {\"ood_success_rate\": 0.097, \"eval_tasks\": 134, \"wandb_run_id\": \"ej3afpel\"}}, \"c_prime_step5_ood_bjb1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T00:38:37.400Z\", \"updated_at\": \"2026-05-22T01:08:37.950Z\", \"spec\": {\"command\": \"python train.py --config-name _alfworld_c_prime_step5_ood_eval\", \"server\": \"bjb1-17606\", \"gpu\": [\"cuda:0\"], \"pid\": \"357552\", \"log_path\": \"~/runs/cost-verify-agent-rl/c_prime_step5_ood_bjb1.log\", \"submitted_at\": \"2026-05-22T00:38:37.000Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen3-1.7B (C' step5 HF)\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/qwen_c_prime_step5_hf\", \"eval_data\": \"AlfworldSG_OOD (134 valid_unseen tasks)\", \"data_count\": 134, \"seed\": 999, \"data_path\": \"AlfworldSG_OOD\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/qwen_c_prime_step5_hf\", \"wall_clock_seconds\": 1801.0, \"gpu_hours\": 0.5}, \"reproduce\": {\"finished_at\": \"2026-05-22T01:04:27.269Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T01:04:32.707139+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"ood_success_rate\": 0, \"ood_pass_at_1\": 0, \"ood_action_is_valid\": 0.9757, \"ood_action_is_effective\": 1, \"ood_num_actions\": 50, \"ood_avg_episode_return\": 0, \"ood_raw_reward\": 0, \"ood_response_length\": 4250.31, \"ood_reward_mean_at_134\": 0, \"total_tasks\": 134, \"successful_tasks\": 0, \"wandb_run_id\": \"tf8ute5n\"}, \"hypothesis\": \"C' (trajectory-level cap 12000) step 5 OOD eval on bjb1 — retry of westd OOM run. If C' step5 achieved 21.875% val success, OOD generalization should be comparable to other interventions (10-15%).\", \"notes\": \"OOD success 0.0% (0/134 episodes) — catastrophic OOD failure. Model hit max actions (50) on every episode, action_is_valid=97.6%, action_is_effective=100% — syntactically correct but never completes any task. response_length=4250 (much shorter than val 8327). Compared to: SFT baseline 5.97%, Seed 1 23.88%, Seed 4 30.60%, Intervention C step5 10.45%, C step7 14.93%. C' step5 is the worst OOD result across all checkpoints. W&B run: tf8ute5n (entity: xiaoyucorynne-).\", \"completed_at\": \"2026-05-22T01:08:37.950Z\"}, \"exp029_intervention_c_prime\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T21:36:15.938Z\", \"updated_at\": \"2026-05-22T00:55:47.445Z\", \"hypothesis\": \"Trajectory-level token cap (12000 tokens across all turns) will reduce cost per trajectory while maintaining task success rate, because most successful ALFWorld episodes complete within 12 turns (~12K tokens) and the cap only truncates inefficient long-running failures.\", \"parent\": \"exp029_seed7\", \"spec\": {\"command\": \"python train.py --config-name _alfworld_intervention_c_prime\", \"server\": \"bjb1-17606\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"347250\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp029_intervention_c_prime.log\", \"submitted_at\": \"2026-05-21T22:02:36.943Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"ALFWorld episode-level\", \"data_count\": 134, \"model_name\": \"Qwen3-1.5B\", \"seed\": 999, \"checkpoint_source\": \"qwen3_exp021_ragen_sft_v4 (SFT base)\", \"eval_data\": \"ALFWorld valid_unseen 32 episodes\", \"checkpoint_path\": \"unknown - crashed during checkpoint save (disk full)\", \"wall_clock_seconds\": 7072.1, \"gpu_hours\": 3.93}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-22T00:00:29.004Z\", \"notes\": \"All 7 training steps completed. Crash during final checkpoint save (disk full /tmp/ray). W&B run: zndyygbn. CRITICAL FINDING: trajectory cap (12000) was NEVER triggered — aborted_ratio=0 throughout all 7 steps. response_length/mean=8198 (final), response_length/max=13322 (includes env tokens, model tokens ≈9600 < 12000 cap). Step 5 metrics: response_length/mean=8327, val≈21.9% success. Step 5 checkpoint intact and converted to HF (on both bjb1 and westd). The 12000 cap was not restrictive enough — this run is functionally equivalent to uncapped training with max_turn=25.\"}, \"c_prime_step5_ood\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T23:59:02.288Z\", \"updated_at\": \"2026-05-22T00:37:41.817Z\", \"spec\": {\"command\": \"python train.py --config-name _alfworld_c_prime_step5_ood_eval\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\"], \"pid\": \"995987\", \"log_path\": \"~/runs/cost-verify-agent-rl/c_prime_step5_ood.log\", \"submitted_at\": \"2026-05-21T23:59:01.912Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"ALFWorld OOD 134 episodes\", \"data_count\": 134, \"model_name\": \"Qwen3-1.5B (C' trajectory cap step 5)\", \"seed\": 789, \"checkpoint_source\": \"qwen_c_prime_step5_hf (from exp029_intervention_c_prime global_step_5)\", \"eval_data\": \"ALFWorld OOD 134 episodes\", \"wall_clock_seconds\": 2319.9, \"gpu_hours\": 0.64}, \"hypothesis\": \"C' (trajectory cap 12000) step 5 OOD eval — if train metrics are positive at step 5, OOD generalization confirms trajectory cap preserves learning\", \"parent\": \"exp029_intervention_c_prime\", \"reproduce\": {\"finished_at\": \"2026-05-22T00:37:39.757Z\"}, \"failure_reason\": \"EXIT_CODE=137 (SIGKILL — OOM killer or manual kill)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-22T00:37:41.817Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T00:37:45.810471+00:00\"}]}}, \"c_prime_step5_ood_eval\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T00:36:42.807Z\", \"updated_at\": \"2026-05-22T00:36:42.807Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/cost-verify-agent-rl/RAGEN && python train.py --config-name _alfworld_c_prime_step5_ood_eval\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\"], \"pid\": \"57960\", \"log_path\": \"~/runs/cost-verify-agent-rl/c_prime_step5_ood_eval.log\", \"submitted_at\": \"2026-05-22T00:36:42.387Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"seed7_high_kl_step5_ood\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T23:09:57.949Z\", \"updated_at\": \"2026-05-21T23:55:51.948Z\", \"spec\": {\"command\": \"python train.py --config-name _alfworld_seed7_high_kl_step5_ood_eval\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:3\"], \"pid\": \"968497\", \"log_path\": \"~/runs/cost-verify-agent-rl/seed7_high_kl_step5_ood.log\", \"submitted_at\": \"2026-05-21T23:48:37.258Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"ALFWorld OOD 134 episodes\", \"data_count\": 134, \"model_name\": \"Qwen3-1.5B (seed7 high KL step 5)\", \"seed\": 789, \"checkpoint_source\": \"qwen_exp029_seed7_high_kl_step5_hf\", \"eval_data\": \"ALFWorld OOD 134 episodes\", \"wall_clock_seconds\": 434.7, \"gpu_hours\": 0.12}, \"hypothesis\": \"Seed 7 with high-KL intervention at step 5 (mid-training, before final degradation) OOD eval — provides pre-collapse data point for bimodal analysis.\", \"parent\": \"exp029_seed7_high_kl\", \"notes\": \"First attempt failed: Ray started but ALFWorld env never initialized (silent failure, log path was None). Restarted by Worker at ~23:50 UTC with same checkpoint /root/autodl-tmp/checkpoints/qwen_exp029_seed7_high_kl_step5_hf/. Second attempt running.\", \"reproduce\": {\"finished_at\": \"2026-05-21T23:55:49.905Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-21T23:55:51.948Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-21T23:55:58.612344+00:00\"}]}}, \"intervention_c_step7_ood\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T22:54:26.515Z\", \"updated_at\": \"2026-05-21T23:45:01.965Z\", \"spec\": {\"command\": \"python train.py --config-name _alfworld_intervention_c_ood_eval\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\"], \"pid\": \"895615\", \"log_path\": \"~/runs/cost-verify-agent-rl/intervention_c_step7_ood.log\", \"submitted_at\": \"2026-05-21T22:54:26.154Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"eval_out_of_distribution\", \"data_count\": 134, \"model_name\": \"qwen_intervention_c_hard_cap_step7_hf\", \"seed\": 789, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/qwen_intervention_c_hard_cap_step7_hf\", \"eval_data\": \"AlfworldSG_OOD (134 tasks)\", \"wall_clock_seconds\": 1787.9, \"gpu_hours\": 0.5}, \"hypothesis\": \"Intervention-C (hard cap: 512 tokens/turn + 20 turns) step 7 (final, collapsed) achieves low OOD generalization, consistent with other collapsed seeds showing low OOD despite some train success.\", \"parent\": \"intervention-c-hard-cap\", \"reproduce\": {\"finished_at\": \"2026-05-21T23:18:29.604Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-21T23:18:32.894345+00:00\"}]}, \"metrics\": {\"ood_pass_at_1\": 0.1493, \"ood_action_is_valid\": 0.663, \"ood_num_actions\": 43.67, \"ood_response_length\": 6365.6, \"ood_action_is_effective\": 1, \"ood_reward_mean\": 1.493, \"eval_tasks\": 134, \"eval_time_seconds\": 1370}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/qwen_intervention_c_hard_cap_step7_hf\", \"log_path\": \"/root/runs/cost-verify-agent-rl/intervention_c_step7_ood.log\", \"conclusion\": \"success\", \"notes\": \"Intervention C (hard cap 512/20) step 7 final checkpoint OOD = 14.93%. Comparable OOD despite collapse, confounded by training steps (only 7 steps vs Seed 4's 15 steps). Hard cap collapse produces lower OOD than natural collapse (Seed 4 30.6%), suggesting policy-constraining interventions limit generalization.\", \"completed_at\": \"2026-05-21T23:24:14.052Z\"}, \"seed7_high_kl_step7_ood\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T23:07:29.560Z\", \"updated_at\": \"2026-05-21T23:40:01.125Z\", \"spec\": {\"command\": \"python train.py --config-name _alfworld_seed7_high_kl_step7_ood_eval\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:2\"], \"pid\": \"924058\", \"log_path\": \"~/runs/cost-verify-agent-rl/seed7_high_kl_step7_ood.log\", \"submitted_at\": \"2026-05-21T23:07:29.164Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"alfworld/eval_out_of_distribution\", \"data_count\": 134, \"model_name\": \"qwen_exp029_seed7_high_kl_step7_hf\", \"seed\": 999, \"checkpoint_source\": \"exp029_seed7_high_kl/global_step_7_hf\", \"eval_data\": \"alfworld eval_out_of_distribution (134 tasks)\", \"wall_clock_seconds\": 1952.0, \"gpu_hours\": 0.54}, \"hypothesis\": \"Seed 7 with high-KL intervention (step 7, final) OOD performance — high KL was applied to prevent collapse but experiment still ended with poor train_success. OOD should be low, confirming collapse correlation.\", \"parent\": \"exp029_seed7_high_kl\", \"reproduce\": {\"finished_at\": \"2026-05-21T23:34:19.100Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-21T23:34:22.299914+00:00\"}]}, \"metrics\": {\"ood_success_rate\": 0.1343, \"ood_pass_at_1\": 0.1343, \"ood_action_is_valid\": 0.7253, \"ood_action_is_effective\": 0.9928, \"ood_num_actions\": 44.1, \"ood_response_length\": 7885.16, \"ood_manager_invalid_action\": 0.0072, \"eval_tasks\": 134, \"eval_split\": \"eval_out_of_distribution\"}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/exp029-seed7-high-kl/global_step_7_hf\", \"log_path\": \"~/runs/cost-verify-agent-rl/seed7_high_kl_step7_ood.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T23:40:01.126Z\"}, \"intervention_c_step5_ood\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T22:55:42.545Z\", \"updated_at\": \"2026-05-21T23:24:51.302Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/cost-verify-agent-rl/RAGEN && export WANDB_PROJECT=cost-verify-agent-rl && export CUDA_VISIBLE_DEVICES=1 && python train.py --config-name _alfworld_intervention_c_step5_ood_eval\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:1\"], \"pid\": \"903154\", \"log_path\": \"~/runs/cost-verify-agent-rl/intervention_c_step5_ood.log\", \"submitted_at\": \"2026-05-21T22:55:41.851Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/cost-verify-agent-rl/RAGEN\", \"data_count\": 134, \"model_name\": \"qwen_intervention_c_hard_cap_step5_hf\", \"seed\": 321, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/qwen_intervention_c_hard_cap_step5_hf\", \"eval_data\": \"AlfworldSG_OOD (134 episodes)\", \"wall_clock_seconds\": 1749.5, \"gpu_hours\": 0.49}, \"hypothesis\": \"Intervention-C (hard cap) step 5 (pre-collapse, train_success~38%) OOD eval provides a pre-collapse data point for bimodal analysis comparison.\", \"parent\": \"intervention-c-hard-cap\", \"reproduce\": {\"finished_at\": \"2026-05-21T23:20:59.937Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-21T23:21:03.338466+00:00\"}]}, \"metrics\": {\"ood_success_rate\": 0.1045, \"ood_pass_at_1\": 0.1045, \"val_reward_mean\": 1.045, \"val_response_length\": 6266.3, \"val_num_actions\": 45.02, \"val_action_is_valid\": 0.637, \"val_action_is_effective\": 0.99, \"ood_episodes\": 134, \"wandb_run_id\": \"fxodsn98\", \"wandb_run_name\": \"intervention-c-step5-ood-eval\"}, \"log_path\": \"~/runs/cost-verify-agent-rl/intervention_c_step5_ood.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/qwen_intervention_c_hard_cap_step5_hf\", \"conclusion\": \"negative\", \"notes\": \"OOD success 10.45% (14/134 episodes) — below 15% threshold. Response length 6266 tokens (already inflated vs base). action_is_valid only 63.7% indicating format degradation. This pre-collapse step 5 checkpoint (train_success~38%) already shows poor OOD generalization, consistent with intervention-c-hard-cap being negative overall — hard cap did not prevent response inflation or preserve OOD transfer.\", \"completed_at\": \"2026-05-21T23:24:51.302Z\"}, \"intervention-c-hard-cap\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T21:12:57.442Z\", \"updated_at\": \"2026-05-21T22:27:43.521Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/cost-verify-agent-rl/RAGEN && RAY_ADDRESS=local CUDA_VISIBLE_DEVICES=0,1 python train.py --config-name _alfworld_intervention_c_hard_cap\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"788147\", \"log_path\": \"~/runs/cost-verify-agent-rl/intervention-c-hard-cap.log\", \"submitted_at\": \"2026-05-21T21:12:56.719Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"ALFWorld episode-level\", \"data_count\": 134, \"model_name\": \"Qwen3-1.5B (qwen3_exp021_ragen_sft_v4)\", \"seed\": 999, \"checkpoint_source\": \"qwen3_exp021_ragen_sft_v4 (SFT base)\", \"eval_data\": \"N/A (training)\", \"hyperparams\": {\"response_length\": 512, \"max_turn\": 20, \"kl_loss_coef\": 0.01, \"total_steps\": 7}, \"checkpoint_path\": \"N/A (negative result)\", \"wall_clock_seconds\": 4486.8, \"gpu_hours\": 2.49}, \"hypothesis\": \"Generation hard cap (per-turn 512 tokens + max 20 turns) physically prevents response_length explosion that caused 50% seed collapse. Same seed=999 as Seed 7 which collapsed at step 7. If step 7 resp_len < 2000 and success > 30%, hard cap is effective mitigation.\", \"parent\": \"exp029_seed7\", \"notes\": \"Completed 7/7 steps, EXIT_CODE=0. Hard cap (512 tokens/turn, 20 turns) FAILED to prevent response length explosion. Model compensated by using more turns — response_length/mean went from 4662 (step 6) to 7170 (step 7). Train success peaked at 38.28% (step 6) then crashed to 15.625% (step 7). Final val_success=9.375%, barely above baseline 6.25%. All 3 interventions (A: len_penalty, B: high_kl, C: hard_cap) are negative. W&B: https://wandb.ai/xiaoyucorynne-/cost-verify-agent-rl/runs/hszaa3vc\", \"reproduce\": {\"finished_at\": \"2026-05-21T22:22:23.182Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-21T22:22:27.354282+00:00\"}]}, \"conclusion\": \"negative\", \"metrics\": {\"step7_train_success\": 0.15625, \"step7_val_success\": 0.09375, \"step7_train_resp_len\": 870.25, \"step7_val_resp_len\": 927.44, \"step7_response_length_mean\": 7170.41, \"step7_aborted_ratio\": 0, \"step7_pg_loss\": 6.72e-05, \"step7_kl_loss\": 0.0204, \"step7_grad_norm\": 1.31, \"step6_train_success\": 0.3828, \"step6_train_resp_len\": 745, \"step6_response_length_mean\": 4662.21, \"step0_val_success\": 0.0625, \"step0_val_resp_len\": 974.78}, \"completed_at\": \"2026-05-21T22:27:43.522Z\"}, \"exp029_seed4_ood_eval_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T21:10:07.966Z\", \"updated_at\": \"2026-05-21T22:20:19.400Z\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/cost-verify-agent-rl/RAGEN && RAY_ADDRESS=local CUDA_VISIBLE_DEVICES=2 python train.py --config-name _alfworld_exp029_seed4_ood_eval'\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:2\"], \"pid\": \"779407\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp029_seed4_ood_eval_v2.log\", \"submitted_at\": \"2026-05-21T21:10:07.557Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"AlfworldSG_OOD\", \"data_count\": 134, \"model_name\": \"Qwen2.5-1.5B (exp029_seed4_step15)\", \"seed\": 42, \"checkpoint_source\": \"exp029_seed4_v2 step 15 (FSDP->HF)\", \"eval_data\": \"AlfworldSG_OOD valid_unseen 134 tasks\", \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 4211.8, \"gpu_hours\": 1.17}, \"hypothesis\": \"Episode-level GRPO seed=42 (collapse seed, step 15) achieves meaningful OOD generalization despite response_length explosion during training\", \"parent\": \"exp029_seed4_v2\", \"reproduce\": {\"finished_at\": \"2026-05-21T22:16:40.786Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-21T22:16:45.668835+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"ood_success_rate\": 0.306, \"ood_pass_at_1\": 0.306, \"ood_action_is_valid\": 0.6367, \"ood_response_length\": 7212, \"ood_num_actions\": 44, \"eval_tasks\": 134}, \"completed_at\": \"2026-05-21T22:20:19.400Z\"}, \"exp029_seed8_ood_precollapse\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T21:12:56.344Z\", \"updated_at\": \"2026-05-21T21:48:34.209Z\", \"hypothesis\": \"Seed 8 (collapse seed) pre-collapse checkpoint (step 5) retains OOD generalization ability before response_length explosion, testing whether early GRPO training generalizes to unseen ALFWorld tasks\", \"parent\": \"exp029_seed8\", \"spec\": {\"checkpoint_path\": \"N/A (eval-only experiment, no checkpoint produced)\", \"log_path\": \"/root/autodl-tmp/ray_tmp/ray/session_2026-05-22_05-18-18_722190_801623/logs/worker-343a9768a58fc9783e78784154b6596ece79d3591fd07873619f72cb-01000000-808429.out\"}, \"conclusion\": \"success\", \"metrics\": {\"ood_success_rate\": 0.1194, \"ood_pass_at_1\": 0.1194, \"ood_num_actions\": 44.92, \"ood_action_is_valid\": 0.5754, \"ood_action_is_effective\": 1, \"ood_response_length\": 6503.04, \"eval_tasks\": 134, \"eval_time_seconds\": 1430.88}, \"notes\": \"Seed 8 pre-collapse (step 5) OOD eval completed. OOD success rate: 11.94% (134 tasks). Log found in Ray worker output (worker-343a9768...808429.out), not in dedicated log file. Wandb run: bpmk7i8r. No tmux session remaining.\", \"completed_at\": \"2026-05-21T21:48:34.209Z\"}, \"exp029_seed7_ood_precollapse\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T21:12:54.573Z\", \"updated_at\": \"2026-05-21T21:33:13.466Z\", \"hypothesis\": \"Seed 7 (collapse seed, step 5 = pre-collapse checkpoint) retains OOD generalization ability before response_length explosion. Comparing pre-collapse OOD vs post-collapse OOD reveals whether collapse destroys learned generalization or the model never generalized.\", \"parent\": \"exp029_seed7\", \"conclusion\": \"killed\", \"notes\": \"Checkpoint deleted during westd disk cleanup. Cannot perform OOD eval.\"}, \"exp029_seed7_high_kl\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T16:15:26.386Z\", \"updated_at\": \"2026-05-21T21:01:59.701Z\", \"hypothesis\": \"Higher KL coefficient (0.1 vs 0.01, 10x increase) constrains policy drift enough to prevent response_length explosion that caused ~43% seed collapse. Same seed=999 as original Seed 7. No code change, config-only intervention. If step 7 response_length < 2000 and success > 30%, higher KL is effective.\", \"parent\": \"exp029_seed7\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/cost-verify-agent-rl/RAGEN && RAY_ADDRESS=local CUDA_VISIBLE_DEVICES=0,1 WANDB_PROJECT=cost-verify-agent-rl python train.py --config-name _alfworld_exp029_seed7_high_kl\\\"\", \"server\": \"bjb1-17606\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"334159\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp029_seed7_high_kl.log\", \"submitted_at\": \"2026-05-21T17:01:50Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"ALFWorld episode-level\", \"data_count\": \"134 tasks\", \"model_name\": \"Qwen3-1.5B (qwen3_exp021_ragen_sft_v4)\", \"seed\": 999, \"kl_loss_coef\": 0.1, \"total_steps\": 7, \"checkpoint_source\": \"qwen3_exp021_ragen_sft_v4 (SFT base)\", \"eval_data\": \"N/A (training experiment)\", \"note\": \"3rd submit: 1st stuck on disk full, 2nd crashed on Ray node kill. GPU now clean.\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/exp029-seed7-high-kl/\", \"wall_clock_seconds\": 14409.7, \"gpu_hours\": 8.01}, \"metrics\": {\"val_success_step0\": 0.15625, \"val_success_final\": 0.3125, \"val_response_length_step0\": 5575.47, \"val_response_length_final\": 6045.84, \"val_reward_mean_step0\": 1.5625, \"val_reward_mean_final\": 3.125, \"train_response_length_step1\": 5601.36, \"train_response_length_final\": 12849.99, \"actor_kl_loss_step1\": 0.00128, \"actor_kl_coef\": 0.1, \"actor_ppo_kl_step1\": 2.71e-05, \"total_steps\": 7, \"total_time_s\": 13197, \"exit_code\": 0}, \"log_path\": \"~/runs/cost-verify-agent-rl/exp029_seed7_high_kl.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/exp029-seed7-high-kl/global_step_7/\", \"conclusion\": \"negative\", \"failure_reason\": \"KL 10x (0.01→0.1) cannot prevent response inflation: train_resp_len 5601→12849, val_success ~28-31% (SFT baseline level). Config-level KL regularization insufficient.\", \"completed_at\": \"2026-05-21T21:01:59.701Z\"}, \"exp029_seed8\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T15:49:23.647Z\", \"updated_at\": \"2026-05-21T20:57:49.435Z\", \"hypothesis\": \"Episode-level GRPO (seed=1024) avoids collapse and learns consistently. 6th seed for cross-seed robustness evidence. RAY_ADDRESS=local isolation enforced. Runs on westd cuda:2,3, isolated from Seed 7 on cuda:0,1.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/cost-verify-agent-rl/RAGEN && RAY_ADDRESS=local CUDA_VISIBLE_DEVICES=2,3 WANDB_PROJECT=cost-verify-agent-rl python train.py --config-name _alfworld_exp029_seed8_episode\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:2\", \"cuda:3\"], \"pid\": \"462991\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp029_seed8.log\", \"submitted_at\": \"2026-05-21T15:53:08.498Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"ALFWorld episode-level\", \"data_count\": \"134 tasks\", \"model_name\": \"Qwen3-1.5B (qwen3_exp021_ragen_sft_v4)\", \"seed\": 1024, \"wandb_run_id\": \"c0l6e7vd\", \"wall_clock_seconds\": 18181.2, \"gpu_hours\": 10.1}, \"metrics\": {\"val_success_step0\": 0.3125, \"val_success_step5\": 0.2813, \"val_resp_len_step0\": 2469, \"val_resp_len_step5\": 3162, \"train_success_step1\": 0.359, \"train_success_step9\": 0.109, \"train_resp_len_step1\": 1784, \"train_resp_len_step9\": 11569, \"rollout_resp_len_step9\": 14869, \"collapse_type\": \"response_inflation\", \"collapse_detected_at_step\": 9, \"steps_completed_so_far\": 9}, \"reproduce\": {\"finished_at\": \"2026-05-21T20:56:07.072Z\"}, \"failure_reason\": \"Response inflation collapse at step 9. train_resp_len: 1784→11569, rollout_resp_len: 14869, train_success: 35.9%→10.9%. Same collapse pattern as Seed 7 (step 7) and Seed 4 v2. Hypothesis falsified: seed=1024 does NOT avoid collapse.\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-21T20:56:09.668Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-21T20:56:13.212077+00:00\"}]}}, \"exp029_seed4_ood_eval\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T20:50:32.599Z\", \"updated_at\": \"2026-05-21T20:50:32.599Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/cost-verify-agent-rl/RAGEN && RAY_ADDRESS=local CUDA_VISIBLE_DEVICES=0 WANDB_PROJECT=cost-verify-agent-rl python train.py --config-name _alfworld_exp029_seed4_ood_eval\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\"], \"pid\": \"762273\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp029_seed4_ood_eval.log\", \"submitted_at\": \"2026-05-21T20:50:32.213Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"exp029_seed7_len_penalty\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T16:15:24.107Z\", \"updated_at\": \"2026-05-21T20:40:18.140Z\", \"hypothesis\": \"Response length penalty (threshold=1000, coef=0.5) prevents response_length explosion that caused ~43% seed collapse in episode-level GRPO. Same seed=999 as original Seed 7 which collapsed at step 7. If step 7 response_length < 2000 and success > 30%, penalty is effective.\", \"parent\": \"exp029_seed7\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/cost-verify-agent-rl/RAGEN && RAY_ADDRESS=local CUDA_VISIBLE_DEVICES=0,1 WANDB_PROJECT=cost-verify-agent-rl python train.py --config-name _alfworld_exp029_seed7_len_penalty\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"495138\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp029_seed7_len_penalty.log\", \"submitted_at\": \"2026-05-21T16:19:03.754Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"ALFWorld episode-level\", \"data_count\": \"134 tasks\", \"model_name\": \"Qwen3-1.5B (qwen3_exp021_ragen_sft_v4)\", \"seed\": 999, \"response_length_penalty_coef\": 0.5, \"response_length_penalty_threshold\": 1000, \"total_steps\": 7, \"checkpoint_source\": \"qwen3_exp021_ragen_sft_v4 (SFT base)\", \"eval_data\": \"N/A (training experiment)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/exp029-seed7-len-penalty/\", \"wall_clock_seconds\": 15672.0, \"gpu_hours\": 8.71}, \"conclusion\": \"negative\", \"metrics\": {\"val_success_step0\": 0.0625, \"val_success_step7\": 0.2813, \"val_resp_len_step0\": 8600, \"val_resp_len_step7\": 7598, \"train_success_step1\": 0.3125, \"train_resp_len_step1\": 1992, \"rollout_resp_len_step1\": 10319, \"rollout_resp_len_step7\": 14284, \"steps_completed\": 7, \"intervention\": \"response_length_penalty\", \"penalty_coef\": 0.5, \"penalty_threshold\": 1000, \"criteria_met\": false, \"criteria_resp_len\": \"7598 >> 2000 FAIL\", \"criteria_success\": \"28.13% < 30% FAIL\"}, \"completed_at\": \"2026-05-21T20:40:15.779Z\", \"failure_reason\": \"Length penalty (coef=0.5, threshold=1000) insufficient. val resp_len only reduced 8600→7598 (far from 2000 target). val success=28.13% (below 30% threshold). Penalty only affected train resp_len (1992) but rollout resp_len continued inflating to 14284.\"}, \"exp029_seed4_v2\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-21T07:41:09.516Z\", \"updated_at\": \"2026-05-21T16:34:48.956Z\", \"hypothesis\": \"Episode-level GRPO (seed=123) avoids collapse and learns consistently. Retry of seed4 with disk cleaned and save_freq=5.\", \"reproduce\": {\"finished_at\": \"2026-05-21T16:10:28.120Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-21T08:52:14.261Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-21T08:52:17.832069+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-21T16:10:32.176442+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/cost-verify-agent-rl/RAGEN && CUDA_VISIBLE_DEVICES=0,1 WANDB_PROJECT=cost-verify-agent-rl python train.py --config-name _alfworld_exp029_seed4_episode\\\"\", \"server\": \"bjb1-17606\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"302056\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp029_seed4_v2.log\", \"submitted_at\": \"2026-05-21T08:42:11.524Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wandb_run_id\": \"fb1o765g\", \"data_path\": \"ALFWorld episode-level\", \"data_count\": \"134 tasks\", \"model_name\": \"Qwen3-1.5B (qwen3_exp021_ragen_sft_v4)\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/exp029-seed4/global_step_15/\", \"wall_clock_seconds\": 28357.4, \"gpu_hours\": 15.75}, \"conclusion\": \"negative\", \"metrics\": {\"val_pass_at_1\": 0.4375, \"val_pass_at_8\": 0.988, \"train_success_step13\": 0.3828, \"response_length\": 4850, \"kl_loss\": 0.119, \"entropy\": 0.035, \"collapse_type\": \"response_inflation\", \"steps_completed\": 15}}, \"exp029_seed7\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T12:20:06.906Z\", \"updated_at\": \"2026-05-21T16:08:56.968Z\", \"hypothesis\": \"Episode-level GRPO (seed=999) avoids collapse and learns consistently. Sixth seed for cross-seed robustness evidence. Replaces Seed 5 v2 (lost to M043 OOM at step 12). RAY_ADDRESS=local isolation enforced.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/cost-verify-agent-rl/RAGEN && RAY_ADDRESS=local CUDA_VISIBLE_DEVICES=0,1 WANDB_PROJECT=cost-verify-agent-rl python train.py --config-name _alfworld_exp029_seed7_episode\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"226699\", \"data_path\": \"ALFWorld episode-level\", \"data_count\": \"134 tasks\", \"model_name\": \"Qwen3-1.5B (qwen3_exp021_ragen_sft_v4)\", \"seed\": 999, \"wandb_run_id\": \"p6vwsrfk\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp029_seed7.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/exp029-seed7/global_step_5/\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-21T16:08:54.276Z\", \"failure_reason\": \"response_length explosion at step 7 (8803 tokens). Director ordered kill. Same collapse pattern as ~43% of seeds.\", \"metrics\": {\"response_length_step7\": 8803, \"train_success_step6\": 0.523, \"collapse_type\": \"response_length_explosion\", \"steps_completed\": 7, \"killed_at_step\": 7}}, \"exp029_seed6_ood_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T13:07:07.533Z\", \"updated_at\": \"2026-05-21T16:02:38.737Z\", \"hypothesis\": \"Evaluate exp029_seed6_v3 final checkpoint (global_step_15, episode-level GRPO seed=789, val=28.1%) on 134 OOD tasks (valid_unseen, τ=0.4). Cross-seed OOD evidence for paper Table 1.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/cost-verify-agent-rl/RAGEN && RAY_ADDRESS=local CUDA_VISIBLE_DEVICES=2 WANDB_PROJECT=cost-verify-agent-rl python train.py --config-name _alfworld_exp029_seed6_ood_eval\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:2\"], \"pid\": \"291159\", \"data_path\": \"AlfworldSG_OOD (134 valid_unseen tasks)\", \"data_count\": 134, \"model_name\": \"Qwen3-1.5B (episode GRPO seed=789, step 15)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/exp029-seed6/global_step_15_hf\", \"eval_data\": \"AlfworldSG_OOD 134 tasks, τ=0.4\"}, \"metrics\": {\"failure_reason\": \"ValueError: Unsupported model: /root/autodl-tmp/checkpoints/exp029-seed6/global_step_15_hf — get_special_tokens() in ctx_manager.py does not recognize the RL checkpoint name_or_path\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-21T13:36:19.727Z\"}, \"sft_baseline_ood_eval_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T13:25:37.537Z\", \"updated_at\": \"2026-05-21T16:02:35.804Z\", \"hypothesis\": \"1.7B SFT baseline (qwen3_exp021_ragen_sft_v4) OOD performance on 134 valid_unseen tasks (τ=0.4). Fills Table 1 SFT baseline row. Retry of failed sft_baseline_ood_eval (M043 Ray leak).\", \"spec\": {\"checkpoint_path\": \"N/A (val_only eval)\", \"log_path\": \"/tmp/eval_sft_baseline_ood.log\", \"model_name\": \"Qwen3-1.5B SFT (qwen3_exp021_ragen_sft_v4)\"}, \"reproduce\": {\"finished_at\": \"2026-05-21T13:45:24.568Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T13:45:26.298Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-21T13:45:30.088937+00:00\"}]}, \"metrics\": {\"ood_success_rate\": 0.0597, \"pass_at_1\": 0.0597, \"response_length\": 7640.93, \"tasks_evaluated\": 134, \"temperature\": 0.4}}, \"exp029_seed5_ood_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T14:00:13.239Z\", \"updated_at\": \"2026-05-21T16:02:34.383Z\", \"hypothesis\": \"Evaluate exp029_seed5_v2 partial checkpoint (global_step_10, episode-level GRPO seed=456, training OOM at step 12) on 134 OOD tasks (valid_unseen, τ=0.4). Supplementary cross-seed variance data point despite incomplete training.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/cost-verify-agent-rl/RAGEN && RAY_ADDRESS=local CUDA_VISIBLE_DEVICES=3 WANDB_PROJECT=cost-verify-agent-rl python train.py --config-name _alfworld_exp029_seed5_ood_eval\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:3\"], \"pid\": \"375913\", \"data_path\": \"AlfworldSG_OOD (134 valid_unseen tasks)\", \"data_count\": 134, \"model_name\": \"Qwen3-1.5B (episode GRPO seed=456, step 10, partial training)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/qwen_exp029_seed5_step10_hf (symlink to global_step_10_hf)\", \"eval_data\": \"AlfworldSG_OOD 134 tasks, τ=0.4\", \"log_path\": \"/tmp/exp029_seed5_ood_eval.log\", \"wandb_run_id\": \"u4zste0d\", \"note\": \"Started via ssh_execute before submit_training_job mandate, no cron monitoring\", \"checkpoint_path\": \"N/A (val_only eval)\"}, \"metrics\": {\"ood_success_rate\": 0.291, \"ood_pass_at_1\": 0.291, \"ood_num_actions\": 38.54, \"ood_action_is_effective\": 0.9999, \"ood_action_is_valid\": 0.7266, \"ood_response_length\": 6632, \"ood_tasks\": 134, \"temperature\": 0.4, \"checkpoint\": \"qwen_exp029_seed5_step10_hf\", \"checkpoint_md5\": \"35c3860dff645f9d4d9e28c898d20729\", \"verification_status\": \"VERIFIED - different weights, different per-task distribution, statistical coincidence\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T15:06:47.104Z\"}, \"exp029_seed6_ood_eval_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T13:57:41.031Z\", \"updated_at\": \"2026-05-21T16:02:30.675Z\", \"hypothesis\": \"Evaluate exp029_seed6_v3 final checkpoint (global_step_15, episode-level GRPO seed=789, val=28.1%) on 134 OOD tasks (valid_unseen, τ=0.4). Retry after v1 failed due to get_special_tokens() path mismatch. Fixed via qwen symlink.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/cost-verify-agent-rl/RAGEN && RAY_ADDRESS=local CUDA_VISIBLE_DEVICES=2 WANDB_PROJECT=cost-verify-agent-rl python train.py --config-name _alfworld_exp029_seed6_ood_eval\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:2\"], \"pid\": \"342378\", \"data_path\": \"AlfworldSG_OOD (134 valid_unseen tasks)\", \"data_count\": 134, \"model_name\": \"Qwen3-1.5B (episode GRPO seed=789, step 15)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/qwen_exp029_seed6_step15_hf (symlink to global_step_15_hf)\", \"eval_data\": \"AlfworldSG_OOD 134 tasks, τ=0.4\", \"log_path\": \"/tmp/exp029_seed6_ood_eval_v2.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-21T14:09:04.581Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T14:09:06.456Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-21T14:09:10.091639+00:00\"}]}, \"metrics\": {\"ood_success_rate\": 0.291, \"ood_pass_at_1\": 0.291, \"ood_num_actions\": 36.57, \"ood_action_is_effective\": 0.973, \"ood_action_is_valid\": 0.632, \"ood_manager_invalid_action\": 0.027, \"ood_tasks\": 134, \"ood_env\": \"AlfworldSG_OOD\", \"temperature\": 0.4, \"checkpoint\": \"qwen_exp029_seed6_step15_hf\"}, \"checkpoint_path\": \"N/A (val_only eval)\"}, \"exp029_seed6_v3\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-21T08:08:09.482Z\", \"updated_at\": \"2026-05-21T16:02:21.684Z\", \"hypothesis\": \"Episode-level GRPO (seed=789) avoids collapse and learns consistently. Full retrain after M040 checkpoint loss. CUDA_VISIBLE_DEVICES=2,3 enforced.\", \"reproduce\": {\"finished_at\": \"2026-05-21T12:58:52.192Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-21T08:22:34.606Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-21T08:22:38.791277+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-21T12:58:56.169629+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/cost-verify-agent-rl/RAGEN && RAY_ADDRESS=local CUDA_VISIBLE_DEVICES=2,3 WANDB_PROJECT=cost-verify-agent-rl python train.py --config-name _alfworld_exp029_seed6_episode\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:2\", \"cuda:3\"], \"pid\": \"920749\", \"wandb_run_id\": \"2bbyvsdr\", \"data_path\": \"ALFWorld episode-level\", \"data_count\": \"134 tasks\", \"model_name\": \"Qwen3-1.5B (qwen3_exp021_ragen_sft_v4)\", \"seed\": 789}, \"metrics\": {\"val_success_step0\": 0.094, \"val_success_step5\": 0.219, \"val_success_step10\": 0.281, \"val_success_step15\": 0.281, \"train_reward_final\": 8.91, \"response_length_initial\": 14910, \"response_length_final\": 3329, \"kl_max\": 0.008, \"steps_completed\": 15}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/exp029-seed6/global_step_15/actor/\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp029_seed6_v3.log\", \"conclusion\": \"success\"}, \"exp029_seed5_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T07:41:06.806Z\", \"updated_at\": \"2026-05-21T16:02:19.518Z\", \"hypothesis\": \"Episode-level GRPO (seed=456) avoids collapse and learns consistently. Retry of seed5 with correct CUDA_VISIBLE_DEVICES isolation and save_freq=5.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/cost-verify-agent-rl/RAGEN && CUDA_VISIBLE_DEVICES=0,1 WANDB_PROJECT=cost-verify-agent-rl python train.py --config-name _alfworld_exp029_seed5_episode\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"879704\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp029_seed5_v2.log\", \"submitted_at\": \"2026-05-21T08:08:23.448Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wandb_run_id\": \"yyoghk1f\", \"data_path\": \"ALFWorld episode-level\", \"data_count\": \"134 tasks\", \"model_name\": \"Qwen3-1.5B (qwen3_exp021_ragen_sft_v4)\", \"seed\": 456, \"wall_clock_seconds\": 14348.5, \"gpu_hours\": 7.97}, \"reproduce\": {\"finished_at\": \"2026-05-21T12:07:29.557Z\"}, \"failure_reason\": \"OOM at step 12 due to SFT eval Ray worker GPU leak (M043). Process 196655 (eval) consumed 17.13GB on GPU 0, leaving only 3.88GB free for Seed 5 training.\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-21T12:07:31.932Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-21T12:07:35.698763+00:00\"}]}}, \"sft_baseline_ood_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T10:55:22.862Z\", \"updated_at\": \"2026-05-21T12:17:06.640Z\", \"hypothesis\": \"1.7B SFT baseline (qwen3_exp021_ragen_sft_v4) OOD performance on 134 valid_unseen tasks. Fills Table 1 '---' cell. Expected low OOD (~5-10%) as SFT lacks GRPO generalization.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/cost-verify-agent-rl/RAGEN && CUDA_VISIBLE_DEVICES=2 python train.py --config-name _alfworld_sft_baseline_ood_eval\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:2\"], \"pid\": \"156291\", \"log_path\": \"~/runs/cost-verify-agent-rl/sft_baseline_ood_eval.log\", \"submitted_at\": \"2026-05-21T11:57:07.885Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wandb_run_id\": \"bdnhzq9u\", \"data_path\": \"ALFWorld valid_unseen 134 OOD tasks\", \"data_count\": 134, \"model_name\": \"qwen3_exp021_ragen_sft_v4 (1.7B SFT)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4/\", \"eval_data\": \"AlfworldSG_OOD 134 tasks, τ=0.4\", \"wall_clock_seconds\": 1198.8, \"gpu_hours\": 0.33}, \"conclusion\": \"failed\", \"failure_reason\": \"Ray worker leaked to GPU 0 (M043), killed to protect Seed 5 training. Same root cause as M041: Ray cluster sharing.\", \"completed_at\": \"2026-05-21T12:17:06.641Z\"}, \"exp029_seed6_episode\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:52:52.029Z\", \"updated_at\": \"2026-05-21T08:07:53.647Z\", \"hypothesis\": \"Episode-level GRPO (seed=789) avoids collapse and learns consistently, providing fifth seed for cross-seed robustness. Existing: Seed 1 OOD=23.88%, Seed 3 OOD=10.45%, Seeds 4/5 training.\", \"parent\": null, \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/cost-verify-agent-rl/RAGEN && python train.py --config config/_alfworld_exp029_seed6_episode.yaml\", \"server\": \"westd-47453\", \"gpu_ids\": [0, 1], \"pid\": 697721, \"data_path\": \"ALFWorld train split (3553 games)\", \"data_count\": 3553, \"model_name\": \"qwen3-1.7B (exp021 SFT v4)\", \"seed\": \"train=789, val=321\", \"wandb_run_id\": \"nagp1pi4\", \"tmux_session\": \"exp029_seed6\", \"note\": \"CUDA_VISIBLE_DEVICES was NOT set, Ray workers leaked to GPU 0,1 instead of intended 2,3\"}, \"metrics\": {\"val_success_step0\": 0.09375, \"val_success_step10\": 0.40625, \"train_success_step14\": 0.789, \"steps_completed\": 15, \"failure_reason\": \"disk full during step 15 checkpoint save\"}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/exp029-seed6/exp029-seed6-episode-level/global_step_10 (intact); global_step_15 model weights possibly usable but optimizer corrupted\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp029_seed6_episode.log\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-21T07:36:47.026Z\"}, \"exp029_seed6_v2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T07:41:08.261Z\", \"updated_at\": \"2026-05-21T07:42:18.148Z\", \"hypothesis\": \"Episode-level GRPO (seed=789) avoids collapse and learns consistently. Retry of seed6 with correct CUDA_VISIBLE_DEVICES isolation and save_freq=5.\"}, \"exp029_seed5_episode\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:45:02.042Z\", \"updated_at\": \"2026-05-21T07:39:52.851Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export TMPDIR=/root/autodl-tmp/tmp && export WANDB_DIR=/root/autodl-tmp/wandb && export WANDB_TMPDIR=/root/autodl-tmp/tmp && cd /root/autodl-tmp/cost-verify-agent-rl/RAGEN && CUDA_VISIBLE_DEVICES=0,1 WANDB_PROJECT=cost-verify-agent-rl python train.py --config-name _alfworld_exp029_seed5_episode\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"683267\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp029_seed5_episode.log\", \"submitted_at\": \"2026-05-21T02:45:01.624Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"AlfworldSG (16 env_groups x 8 group_size)\", \"data_count\": 128, \"model_name\": \"Qwen3-1.7B (exp021 SFT v4)\", \"seed\": 456, \"checkpoint_source\": \"qwen3_exp021_ragen_sft_v4\", \"eval_data\": \"AlfworldSG 32 val tasks (in-distribution)\", \"wall_clock_seconds\": 17691.2, \"gpu_hours\": 9.83}, \"hypothesis\": \"Episode-level GRPO (seed=456) avoids collapse and learns consistently, providing fourth seed for cross-seed robustness. Seed 1 val~43%/OOD=23.88%, Seed 3 val~40.6%/OOD=10.45%.\", \"parent\": \"exp029_seed3_v2\", \"metrics\": {\"failure_reason\": \"CUDA OOM during loss.backward - Seed 6 process (no CUDA_VISIBLE_DEVICES) leaked onto GPU 0,1, consuming 37.7GB\", \"exit_code\": 1}, \"checkpoint_path\": \"none - OOM crash, no checkpoint saved\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-21T07:39:52.851Z\"}, \"exp029_seed4_episode\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:40:45.734Z\", \"updated_at\": \"2026-05-21T07:39:51.644Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export TMPDIR=/root/autodl-tmp/tmp && mkdir -p /root/autodl-tmp/tmp && cd /root/cost-verify-agent-rl/RAGEN && CUDA_VISIBLE_DEVICES=0,1 WANDB_PROJECT=cost-verify-agent-rl python train.py --config-name _alfworld_exp029_seed4_episode\\\"\", \"server\": \"bjb1-17606\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"283470\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp029_seed4_episode.log\", \"submitted_at\": \"2026-05-21T02:40:45.415Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"AlfworldSG (built-in)\", \"data_count\": \"128 episodes/step (8 env_groups x 8 group_size train, 32 val)\", \"model_name\": \"Qwen3-1.7B (SFT v4)\", \"seed\": \"train=123, val=456\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4\", \"eval_data\": \"AlfworldSG val 32 episodes\", \"wall_clock_seconds\": 17946.2, \"gpu_hours\": 9.97}, \"hypothesis\": \"Episode-level GRPO (seed=123) avoids collapse and learns consistently, providing third seed for cross-seed robustness evidence. Seed 1 val~43%, Seed 3 val~40.6%.\", \"parent\": \"exp029_seed3_v2\", \"metrics\": {\"failure_reason\": \"bjb1 disk full at step 8, save_freq=999 means no checkpoint saved\", \"steps_completed\": 8, \"exit_code\": 1}, \"checkpoint_path\": \"none - save_freq=999, no checkpoint saved before crash\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-21T07:39:51.644Z\"}, \"scienceworld_grpo_cell_c_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T18:23:30.854Z\", \"updated_at\": \"2026-05-21T02:44:56.368Z\", \"hypothesis\": \"ScienceWorld 环境下 episode-level GRPO 能避免 collapse 并学到有效策略，验证 episode-level credit 作为 fix 的跨环境泛化性（v3: 磁盘清理后重启）\", \"parent\": \"scienceworld_grpo_cell_c_v2\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/cost-verify-agent-rl/RAGEN && WANDB_PROJECT=cost-verify-agent-rl python train.py --config-name _scienceworld_cell_c_grpo\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:2\", \"cuda:3\"], \"pid\": \"88226\", \"log_path\": \"~/runs/cost-verify-agent-rl/scienceworld_grpo_cell_c_v3.log\", \"submitted_at\": \"2026-05-20T18:23:38.661Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"ScienceWorldSG (30 task types)\", \"data_count\": 128, \"model_name\": \"Qwen3-1.7B (ScienceWorld SFT checkpoint)\", \"seed\": 10000, \"checkpoint_source\": \"qwen3_scienceworld_sft\", \"eval_data\": \"ScienceWorldSG 30 task types (dev split)\", \"checkpoint_path\": \"N/A (negative, no useful checkpoint)\", \"wall_clock_seconds\": 30077.7, \"gpu_hours\": 16.71}, \"conclusion\": \"negative\", \"notes\": \"D109 止损：step 3 success=0%, action_is_valid=9.4%(<20% 阈值), score 从 2.71 降至 0.96, reward 从 0.5 降至 0.153。趋势恶化，释放 GPU。\", \"completed_at\": \"2026-05-21T02:44:56.370Z\"}, \"exp029_seed3_ood_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T00:39:28.222Z\", \"updated_at\": \"2026-05-21T02:39:55.650Z\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/cost-verify-agent-rl/RAGEN && CUDA_VISIBLE_DEVICES=0,1 WANDB_PROJECT=cost-verify-agent-rl python train.py --config-name _alfworld_exp029_seed3_ood_final'\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"530289\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp029_seed3_ood_v2.log\", \"submitted_at\": \"2026-05-21T00:39:27.902Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"AlfworldSG_OOD (134 valid_unseen tasks)\", \"data_count\": 134, \"model_name\": \"qwen3_exp021_ragen_sft_v4\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/exp029-seed3/global_step_15\", \"eval_data\": \"AlfworldSG_OOD\", \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 7227.7, \"gpu_hours\": 4.02}, \"conclusion\": \"success\", \"metrics\": {\"ood_success_rate\": 0.1045, \"ood_tasks\": 134, \"temperature\": 0.4, \"checkpoint\": \"global_step_15\", \"seed\": \"42/123\"}, \"hypothesis\": \"Evaluate exp029_seed3_v2 final checkpoint (global_step_15, episode-level GRPO seed=42) on 134 OOD tasks (valid_unseen). Cross-seed OOD evidence for paper. Seed 1 OOD=23.88%.\", \"completed_at\": \"2026-05-21T02:39:55.650Z\"}, \"exp029_seed3_ood_final\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T23:00:23.413Z\", \"updated_at\": \"2026-05-21T00:36:31.725Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/cost-verify-agent-rl/RAGEN && CUDA_VISIBLE_DEVICES=0,1 WANDB_PROJECT=cost-verify-agent-rl python train.py --config-name _alfworld_exp029_seed3_ood_final\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"417862\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp029_seed3_ood_final.log\", \"submitted_at\": \"2026-05-20T23:00:23.049Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"Evaluate exp029_seed3_v2 final checkpoint (global_step_15, episode-level GRPO seed=42) on 134 OOD tasks. Cross-seed OOD evidence. Seed 1 OOD=23.88%.\", \"parent\": \"exp029_seed3_v2\", \"conclusion\": \"failed\"}, \"exp029_seed3_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:09:19.834Z\", \"updated_at\": \"2026-05-20T23:01:27.840Z\", \"hypothesis\": \"Episode-level GRPO avoids collapse and learns consistently across seeds, confirming robustness of the credit assignment fix (seed 3 replication of exp029)\", \"parent\": \"exp029_seed3_episode\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export TMPDIR=/root/autodl-tmp/tmp && export WANDB_DIR=/root/autodl-tmp/wandb && export WANDB_TMPDIR=/root/autodl-tmp/tmp && cd /root/cost-verify-agent-rl/RAGEN && WANDB_PROJECT=cost-verify-agent-rl python train.py --config-name _alfworld_exp029_episode_level seed.train=42 seed.val=123 trainer.total_training_steps=15 trainer.experiment_name=exp029-seed3-episode-level trainer.local_log_dir=/root/autodl-tmp/checkpoints/exp029-seed3/ trainer.default_local_dir=/root/autodl-tmp/checkpoints/exp029-seed3/\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"991448\", \"log_path\": \"/root/runs/cost-verify-agent-rl/exp029_seed3_v2.log\", \"submitted_at\": \"2026-05-20T17:09:29.872Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"AlfworldSG (16 train groups x 8, 32 val groups x 1)\", \"data_count\": 128, \"model_name\": \"Qwen3-1.7B SFT (qwen3_exp021_ragen_sft_v4)\", \"seed\": \"42/123\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4\", \"eval_data\": \"AlfworldSG 32 val episodes\", \"wall_clock_seconds\": 20809.1, \"gpu_hours\": 11.56, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/exp029-seed3/global_step_15/\"}, \"reproduce\": {\"finished_at\": \"2026-05-20T22:56:16.783Z\"}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T22:56:18.986Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T22:56:22.163545+00:00\"}]}, \"notes\": \"训练实际完成 15/15 步。EXIT_CODE=129 是 W&B teardown BrokenPipeError 导致的误报。Checkpoint 已保存至 /root/autodl-tmp/checkpoints/exp029-seed3/global_step_15/。初步 metrics: val-core/reward/mean@32=4.0625 (~40.6% success), first_turn_valid_rate=0.977, pass@1(non-zero)=1.0, best@4=8.49, best@8=9.72\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/exp029-seed3/global_step_15/\"}, \"exp029_seed3_ood\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T19:57:11.789Z\", \"updated_at\": \"2026-05-20T21:09:53.849Z\", \"spec\": {\"command\": \"bash -c \\\"... python train.py --config-name _alfworld_exp029_seed3_ood\\\"\", \"server\": \"bjb1-17606\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"265901\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp029_seed3_ood.log\", \"submitted_at\": \"2026-05-20T19:57:11.483Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"qwen3_exp021_ragen_sft_v4\", \"seed\": 3, \"data_path\": \"AlfworldSG_OOD (134 valid_unseen)\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/exp029-seed3/global_step_5\", \"eval_data\": \"AlfworldSG_OOD (134 valid_unseen tasks)\", \"data_count\": 134, \"checkpoint_path\": \"N/A (eval failed)\", \"failure_reason\": \"RuntimeError: FSDP checkpoint device mismatch - optimizer step found tensors on cuda:0 and cpu. RAGEN train.py runs optimizer step during eval flow, incompatible with FSDP 2-GPU checkpoint loaded on different topology.\", \"wall_clock_seconds\": 4362.4, \"gpu_hours\": 2.42}, \"hypothesis\": \"Evaluate exp029_seed3_v2 checkpoint (global_step_5) on 134 OOD tasks (valid_unseen) to provide cross-seed OOD generalization evidence. Seed 1 OOD=23.88% at step 15.\", \"parent\": \"exp029_seed3_v2\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-20T21:09:53.850Z\"}, \"exp029_seed2_ood_step15\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T10:37:25.028Z\", \"updated_at\": \"2026-05-20T19:14:37.390Z\", \"hypothesis\": \"Evaluate exp029_seed2 global_step_15 checkpoint on 134 OOD tasks (valid_unseen). Step 15 is the bjb1 checkpoint before westd resume (step 30 checkpoint lost in disk cleanup M019). Provides cross-seed OOD number for paper table (seed1 OOD=23.88%). Step 15 val was near peak (~25-28%), OOD number expected similar to seed1.\", \"parent\": \"exp029_episode_level_seed2\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export TMPDIR=/root/autodl-tmp/tmp && mkdir -p /root/autodl-tmp/tmp && cd /root/cost-verify-agent-rl/RAGEN && CUDA_VISIBLE_DEVICES=0 python train.py --config-name _alfworld_exp029_seed2_ood_step15\\\"\", \"server\": \"bjb1-17606\", \"gpu\": [\"cuda:0\"], \"pid\": \"259263\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp029_seed2_ood_step15.log\", \"submitted_at\": \"2026-05-20T19:14:37.088Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"notes\": \"全部 seed2 checkpoint 已丢失（M019）。Director 确认取消，论文只用 seed1 OOD 数据。\", \"conclusion\": \"killed\"}, \"sw_info_loss_bjb1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T16:38:54.097Z\", \"updated_at\": \"2026-05-20T19:10:24.938Z\", \"hypothesis\": \"ScienceWorld SFT model under h=2 windowing shows significant performance degradation vs full context (T=0 deterministic), quantifying information loss (M1) cross-environment on bjb1\", \"parent\": \"scienceworld_sft_eval_v2\", \"spec\": {\"command\": \"python eval_scienceworld_info_loss.py --checkpoint /root/autodl-tmp/checkpoints/scienceworld_sft/huggingface --history_length {-1,2} --temperature 0 --max_variations 3 --tensor_parallel_size 2\", \"server\": \"bjb1-17606\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"229078\", \"log_path\": \"~/runs/cost-verify-agent-rl/sw_info_loss_bjb1.log\", \"submitted_at\": \"2026-05-20T16:39:02.613Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"scienceworld dev split\", \"data_count\": \"30 task types x 3 variations = 90 episodes per condition\", \"model_name\": \"qwen3_scienceworld_sft\", \"seed\": \"deterministic (T=0)\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/scienceworld_sft/huggingface\", \"eval_data\": \"scienceworld dev split, 3 variations per task\", \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 9082.3, \"gpu_hours\": 5.05}, \"reproduce\": {\"finished_at\": \"2026-05-20T19:07:34.749Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T19:07:38.508523+00:00\"}]}, \"metrics\": {\"full_context_success\": 0.348, \"h2_success\": 0.045, \"info_loss_delta_pp\": 30.3, \"full_episodes\": 89, \"h2_episodes\": 89, \"full_avg_score\": 26.7, \"h2_avg_score\": 17.4, \"temperature\": 0, \"notable\": \"find-animal/find-living-thing/lifespan-longest+shortest: 100% full → 0% h=2\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T19:10:24.938Z\"}, \"scienceworld_grpo_cell_c_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T15:41:04.991Z\", \"updated_at\": \"2026-05-20T18:23:54.294Z\", \"hypothesis\": \"ScienceWorld 环境下 episode-level GRPO 能避免 collapse 并学到有效策略，验证 episode-level credit 作为 fix 的跨环境泛化性（v2: 加固 JVM 通信——增大堆至 4g + py4j 断连自动重建 JVM + step 崩溃优雅降级）\", \"parent\": \"scienceworld_grpo_cell_c\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/cost-verify-agent-rl/RAGEN && WANDB_PROJECT=cost-verify-agent-rl JAVA_TOOL_OPTIONS='-Xmx4g' python train.py --config-name _scienceworld_cell_c_grpo\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:2\", \"cuda:3\"], \"pid\": \"920065\", \"log_path\": \"~/runs/cost-verify-agent-rl/scienceworld_grpo_cell_c_v2.log\", \"submitted_at\": \"2026-05-20T15:41:18.991Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_ids\": [\"cuda:2\", \"cuda:3\"], \"data_path\": \"scienceworld (30 tasks)\", \"data_count\": 128, \"model_name\": \"qwen3_scienceworld_sft\", \"seed\": 10000, \"checkpoint_source\": \"qwen3_scienceworld_sft\", \"eval_data\": \"scienceworld dev split\", \"wall_clock_seconds\": 9746.5, \"gpu_hours\": 5.41}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-20T18:23:45.449Z\", \"metrics\": {\"note\": \"Stalled at step 2 due to disk full (99%), Ray object spilling blocked. GPU 0% util for >1h50min. Killed and restarted as v3.\"}}, \"exp029_seed3_episode\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T16:52:11.263Z\", \"updated_at\": \"2026-05-20T17:07:41.079Z\", \"hypothesis\": \"Episode-level GRPO avoids collapse and learns consistently across seeds, confirming robustness of the credit assignment fix (seed 3 replication of exp029)\", \"parent\": \"exp029_episode_level\", \"spec\": {\"command\": \"python train.py --config-name _alfworld_exp029_episode_level seed=42 trainer.total_training_steps=15\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"980051\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp029_seed3_episode.log\", \"submitted_at\": \"2026-05-20T17:03:22.094Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"AlfworldSG (16 train groups x 8, 32 val groups x 1)\", \"data_count\": 128, \"model_name\": \"Qwen3-1.7B SFT (qwen3_exp021_ragen_sft_v4)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4\", \"eval_data\": \"AlfworldSG 32 val episodes\", \"wall_clock_seconds\": 242.6, \"gpu_hours\": 0.13}, \"reproduce\": {\"finished_at\": \"2026-05-20T17:07:21.936Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-20T17:07:24.724Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T17:07:28.775428+00:00\"}]}}, \"scienceworld_grpo_cell_c\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:24:51.574Z\", \"updated_at\": \"2026-05-20T15:32:10.728Z\", \"hypothesis\": \"ScienceWorld 环境下 episode-level GRPO 能避免 collapse 并学到有效策略，验证 episode-level credit 作为 fix 的跨环境泛化性\", \"parent\": \"scienceworld_sft\", \"spec\": {\"command\": \"cd /root/cost-verify-agent-rl/RAGEN && WANDB_PROJECT=cost-verify-agent-rl python train.py --config-name _scienceworld_cell_c_grpo\", \"server\": \"westd-47453\", \"gpu\": \"cuda:2,3\", \"pid\": 766820, \"wandb_run_id\": \"sx7h864t\", \"data_path\": \"ScienceWorldSG\", \"data_count\": 30, \"model_name\": \"Qwen3-1.7B (ScienceWorld SFT checkpoint)\", \"seed\": 42, \"checkpoint_source\": \"scienceworld_sft\", \"eval_data\": \"ScienceWorldSG 30 task types (dev split)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/scienceworld_cell_c/\", \"log_path\": \"/root/runs/cost-verify-agent-rl/scienceworld_cell_c.log\", \"hyperparams\": {\"total_training_steps\": 15, \"context_window_mode\": \"full\", \"env_groups\": 16, \"group_size\": 8, \"ppo_mini_batch_size\": 8, \"ppo_max_token_len_per_gpu\": 16384, \"optimizer_offload\": true, \"lr\": 1e-06, \"n_gpus_per_node\": 2}, \"notes\": \"ScienceWorld Cell C: episode-level full context. Expected to learn without collapse, proving fix generalizes.\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-20T15:32:04.012Z\", \"metrics\": {\"step_1_success\": 0, \"step_1_pass_at_8\": 0, \"step_1_score\": 2.74, \"step_1_final_score\": 5.44, \"step_1_action_valid\": 0.44, \"completed_steps\": \"1/15\", \"failure_reason\": \"ScienceWorld Java environment communication error: Exception while sending command\"}}, \"scienceworld_info_loss_h2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T14:21:16.640Z\", \"updated_at\": \"2026-05-20T14:36:43.490Z\", \"hypothesis\": \"ScienceWorld SFT model with h=2 sliding window at T=0 shows degraded performance vs full context, confirming information loss generalizes beyond ALFWorld\", \"parent\": \"8b_det_eval_h2\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-20T14:36:43.490Z\"}, \"sw_info_loss_full_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T14:34:18.334Z\", \"updated_at\": \"2026-05-20T14:36:34.122Z\", \"hypothesis\": \"ScienceWorld SFT model with full context at T=0 achieves significantly higher success rate than h=2, quantifying information loss (Mechanism 1) in a second environment beyond ALFWorld\", \"parent\": \"scienceworld_sft_eval_v2\", \"spec\": {\"command\": \"python eval_scienceworld_info_loss.py --checkpoint qwen3_scienceworld_sft --temperature 0 --history_length -1 --tensor_parallel_size 2 --max_model_len 16384\", \"server\": \"westd-47453\", \"data_path\": \"ScienceWorldSG dev split\", \"data_count\": \"89 episodes\", \"model_name\": \"qwen3_scienceworld_sft\", \"seed\": 0, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/qwen3_scienceworld_sft/huggingface\", \"eval_data\": \"ScienceWorldSG dev, max_variations=3, T=0, full context\", \"gpu\": \"cuda:0,1\", \"pid\": 875971}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-20T14:36:34.123Z\"}, \"scienceworld_info_loss_full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T14:21:15.269Z\", \"updated_at\": \"2026-05-20T14:33:44.987Z\", \"hypothesis\": \"ScienceWorld SFT model with full context at T=0 achieves significantly higher success rate than h=2, quantifying information loss (Mechanism 1) in a second environment beyond ALFWorld\", \"parent\": \"8b_det_eval_full\", \"spec\": {\"command\": \"python3 eval_scienceworld_info_loss.py --temperature 0 --history_length -1 --max_variations 3 --tensor_parallel_size 2\", \"server\": \"westd-47453\", \"data_path\": \"ScienceWorldSG dev split\", \"data_count\": \"~90 episodes\", \"model_name\": \"qwen3_scienceworld_sft\", \"seed\": 0, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/qwen3_scienceworld_sft/huggingface\", \"eval_data\": \"ScienceWorldSG dev, max_variations=3\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-20T14:33:44.987Z\"}, \"scienceworld_sft_eval_v2\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-19T18:50:45.230Z\", \"updated_at\": \"2026-05-20T14:15:37.390Z\", \"hypothesis\": \"SFT-trained model on ScienceWorld can achieve meaningful task completion rates across diverse science tasks, establishing a baseline for subsequent RL fine-tuning comparison.\", \"parent\": \"scienceworld_sft_eval\", \"reproduce\": {\"finished_at\": \"2026-05-19T23:59:52.638Z\"}, \"failure_reason\": null, \"completed_at\": \"2026-05-19T23:59:54.217Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T23:59:57.500015+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"metrics\": {\"episodes_completed\": 409, \"episodes_total\": 1796, \"progress_pct\": 22.8, \"success_count\": 158, \"success_rate\": 0.386, \"speed_ep_per_min\": 1.56}}}, \"spec\": {\"command\": \"python /root/cost-verify-agent-rl/eval_scienceworld.py --temperature 0.4 --resume --episode_timeout 300\", \"server\": \"bjb1-17606\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"195853\", \"data_path\": \"scienceworld dev split\", \"data_count\": 1796, \"model_name\": \"Qwen3-1.7B (ScienceWorld SFT)\", \"seed\": 42, \"log_path\": \"/tmp/eval_scienceworld_v2_resumed.log\", \"checkpoint_source\": \"scienceworld_sft/global_step_448\", \"eval_data\": \"ScienceWorld dev split, 1796 episodes, 30 task types\", \"checkpoint_path\": \"N/A (eval only)\"}, \"metrics\": {\"total_episodes\": 1796, \"success_count\": 540, \"overall_success_rate\": 0.301, \"timeouts\": 0, \"errors\": 0, \"avg_score\": 20.9, \"avg_steps_per_episode\": 28.7, \"total_time_seconds\": 51462, \"split\": \"dev\", \"temperature\": 0.4, \"per_task_type\": {\"boil\": {\"n\": 7, \"succ\": 0, \"rate\": 0}, \"change-the-state-of-matter-of\": {\"n\": 7, \"succ\": 1, \"rate\": 0.143}, \"chemistry-mix\": {\"n\": 8, \"succ\": 0, \"rate\": 0}, \"chemistry-mix-paint-secondary-color\": {\"n\": 9, \"succ\": 2, \"rate\": 0.222}, \"chemistry-mix-paint-tertiary-color\": {\"n\": 9, \"succ\": 0, \"rate\": 0}, \"find-animal\": {\"n\": 75, \"succ\": 37, \"rate\": 0.493}, \"find-living-thing\": {\"n\": 75, \"succ\": 49, \"rate\": 0.653}, \"find-non-living-thing\": {\"n\": 75, \"succ\": 58, \"rate\": 0.773}, \"find-plant\": {\"n\": 75, \"succ\": 9, \"rate\": 0.12}, \"freeze\": {\"n\": 7, \"succ\": 0, \"rate\": 0}, \"grow-fruit\": {\"n\": 31, \"succ\": 2, \"rate\": 0.065}, \"grow-plant\": {\"n\": 31, \"succ\": 0, \"rate\": 0}, \"identify-life-stages-1\": {\"n\": 3, \"succ\": 0, \"rate\": 0}, \"identify-life-stages-2\": {\"n\": 2, \"succ\": 0, \"rate\": 0}, \"inclined-plane-determine-angle\": {\"n\": 42, \"succ\": 7, \"rate\": 0.167}, \"inclined-plane-friction-named-surfaces\": {\"n\": 346, \"succ\": 83, \"rate\": 0.24}, \"inclined-plane-friction-unnamed-surfaces\": {\"n\": 40, \"succ\": 10, \"rate\": 0.25}, \"lifespan-longest-lived\": {\"n\": 31, \"succ\": 28, \"rate\": 0.903}, \"lifespan-longest-lived-then-shortest-lived\": {\"n\": 31, \"succ\": 28, \"rate\": 0.903}, \"lifespan-shortest-lived\": {\"n\": 31, \"succ\": 21, \"rate\": 0.677}, \"measure-melting-point-known-substance\": {\"n\": 109, \"succ\": 25, \"rate\": 0.229}, \"measure-melting-point-unknown-substance\": {\"n\": 75, \"succ\": 27, \"rate\": 0.36}, \"melt\": {\"n\": 7, \"succ\": 1, \"rate\": 0.143}, \"mendelian-genetics-known-plant\": {\"n\": 30, \"succ\": 8, \"rate\": 0.267}, \"mendelian-genetics-unknown-plant\": {\"n\": 120, \"succ\": 35, \"rate\": 0.292}, \"power-component\": {\"n\": 5, \"succ\": 3, \"rate\": 0.6}, \"power-component-renewable-vs-nonrenewable-energy\": {\"n\": 5, \"succ\": 0, \"rate\": 0}, \"test-conductivity\": {\"n\": 225, \"succ\": 35, \"rate\": 0.156}, \"test-conductivity-of-unknown-substances\": {\"n\": 150, \"succ\": 44, \"rate\": 0.293}, \"use-thermometer\": {\"n\": 135, \"succ\": 27, \"rate\": 0.2}}, \"results_json_path\": \"/root/autodl-tmp/checkpoints/scienceworld_sft/eval_results_dev_v2.json\"}, \"conclusion\": \"success\"}, \"scienceworld_grpo_cell_a\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:24:49.171Z\", \"updated_at\": \"2026-05-20T13:54:57.116Z\", \"hypothesis\": \"ScienceWorld 环境下 step-independent GRPO (h=2) 也会出现 policy collapse，验证 ALFWorld 观察到的 collapse 是 step-independent credit assignment 的固有问题而非环境特异性\", \"parent\": \"scienceworld_sft\", \"spec\": {\"command\": \"cd /root/cost-verify-agent-rl/RAGEN && WANDB_PROJECT=cost-verify-agent-rl python train.py --config-name _scienceworld_cell_a_grpo\", \"server\": \"westd-47453\", \"gpu\": \"cuda:0,1\", \"pid\": 759987, \"wandb_run_id\": \"f1c4g6dk\", \"data_path\": \"ScienceWorldSG\", \"data_count\": 30, \"model_name\": \"Qwen3-1.7B (ScienceWorld SFT checkpoint)\", \"seed\": 42, \"checkpoint_source\": \"scienceworld_sft\", \"eval_data\": \"ScienceWorldSG 30 task types (dev split)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/scienceworld-cell-a/global_step_15\", \"log_path\": \"/root/cost-verify-agent-rl/RAGEN/wandb/run-20260520_204440-f1c4g6dk/files/output.log\", \"hyperparams\": {\"total_training_steps\": 15, \"context_window_mode\": \"step_independent\", \"step_independent_history_length\": 2, \"env_groups\": 16, \"group_size\": 8, \"ppo_mini_batch_size\": 8, \"ppo_max_token_len_per_gpu\": 16384, \"optimizer_offload\": true, \"lr\": 1e-06, \"n_gpus_per_node\": 2}, \"notes\": \"ScienceWorld Cell A: step-independent h=2. Expected to show collapse, proving it generalizes beyond ALFWorld.\"}, \"conclusion\": \"negative\", \"metrics\": {\"steps_completed\": 14, \"success_rate\": 0, \"final_score_train\": -100, \"final_score_val\": 1, \"reward_mean_start\": 0.6, \"reward_mean_end\": 0.1, \"entropy_start\": 0.283, \"entropy_end\": 0.52, \"kl_start\": 1.606, \"kl_end\": 0.03, \"exit_mode\": \"abnormal (log truncated at step 15 start)\", \"note\": \"collapse confirmed - success rate 0% throughout, matches ALFWorld Cell A pattern\"}, \"completed_at\": \"2026-05-20T13:54:57.117Z\"}, \"8b_v9d_ood_eval_v5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:25:24.932Z\", \"updated_at\": \"2026-05-20T11:20:18.763Z\", \"hypothesis\": \"Evaluate 8B Cell C episode-level GRPO model (v9d step 10, val_before_train 96.875%) on 134 OOD ALFWorld tasks. Paper's key data point: 8B model OOD generalization under episode-level GRPO. Fix: val.env_groups 234→134 to match val.n_groups=[134].\", \"parent\": \"8b_cell_c_episode_v9d\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && sed -i 's/env_groups: 234/env_groups: 134/' /root/cost-verify-agent-rl/RAGEN/config/_alfworld_8b_v9d_ood_eval.yaml && echo '=== env_groups/n_groups after sed fix ===' && grep -n -E 'env_groups|n_groups' /root/cost-verify-agent-rl/RAGEN/config/_alfworld_8b_v9d_ood_eval.yaml && cd /root/cost-verify-agent-rl/RAGEN && export WANDB_PROJECT=cost-verify-agent-rl && python train.py --config-name _alfworld_8b_v9d_ood_eval\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\", \"cuda:1\", \"cuda:2\", \"cuda:3\"], \"pid\": \"737225\", \"log_path\": \"~/runs/cost-verify-agent-rl/8b_v9d_ood_eval_v5.log\", \"submitted_at\": \"2026-05-20T10:26:02.004Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 3256.8, \"gpu_hours\": 3.62}, \"conclusion\": \"success\", \"metrics\": {\"pass_at_1\": 90.3, \"action_valid_rate\": 98.7, \"n_tasks\": 134, \"temperature\": 0.4, \"model\": \"8B Cell C v9d step 10\"}, \"completed_at\": \"2026-05-20T11:20:18.763Z\"}, \"8b_v9d_ood_eval_v4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:14:46.445Z\", \"updated_at\": \"2026-05-20T10:20:38.588Z\", \"hypothesis\": \"Evaluate 8B Cell C episode-level GRPO model (v9d step 10, val_before_train 96.875%) on 134 OOD ALFWorld tasks. Paper's key data point. Config fix: ppo_mini_batch_size=4, env_groups=2, n_groups=[2].\", \"parent\": \"8b_cell_c_episode_v9d\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && echo aW1wb3J0IHJlCnBhdGggPSAnL3Jvb3QvY29zdC12ZXJpZnktYWdlbnQtcmwvUkFHRU4vY29uZmlnL19hbGZ3b3JsZF84Yl92OWRfb29kX2V2YWwueWFtbCcKdGV4dCA9IG9wZW4ocGF0aCkucmVhZCgpCnRleHQgPSByZS5zdWIocidwcG9fbWluaV9iYXRjaF9zaXplOlxzKlxkKycsICdwcG9fbWluaV9iYXRjaF9zaXplOiA0JywgdGV4dCkKdGV4dCA9IHJlLnN1YihyJ2Vudl9ncm91cHM6XHMqXGQrJywgJ2Vudl9ncm91cHM6IDInLCB0ZXh0LCBjb3VudD0xKQpuZXcgPSByZS5zdWIocicobl9ncm91cHM6XHMqXFspXGQrKFxdKScsIGxhbWJkYSBtOiBtLmdyb3VwKDEpICsgJzInICsgbS5ncm91cCgyKSwgdGV4dCwgY291bnQ9MSkKaWYgbmV3ID09IHRleHQ6CiAgICBuZXcgPSByZS5zdWIocicobl9ncm91cHM6W15cbl0qXG5ccyotXHMqKVxkKycsIGxhbWJkYSBtOiBtLmdyb3VwKDEpICsgJzInLCB0ZXh0LCBjb3VudD0xKQp0ZXh0ID0gbmV3Cm9wZW4ocGF0aCwgJ3cnKS53cml0ZSh0ZXh0KQpwcmludCgnRklYRUQnKQo= | base64 -d > /tmp/fix_ood.py && python3 /tmp/fix_ood.py && grep -n -E 'ppo_mini_batch_size|env_groups|group_size|n_groups' /root/cost-verify-agent-rl/RAGEN/config/_alfworld_8b_v9d_ood_eval.yaml && cd /root/cost-verify-agent-rl/RAGEN && export WANDB_PROJECT=cost-verify-agent-rl && python train.py --config-name _alfworld_8b_v9d_ood_eval\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\", \"cuda:1\", \"cuda:2\", \"cuda:3\"], \"pid\": \"728499\", \"log_path\": \"~/runs/cost-verify-agent-rl/8b_v9d_ood_eval_v4.log\", \"submitted_at\": \"2026-05-20T10:15:20.931Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 144.6, \"gpu_hours\": 0.16}, \"reproduce\": {\"finished_at\": \"2026-05-20T10:17:43.415Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-20T10:17:45.530Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T10:17:49.059040+00:00\"}]}}, \"8b_v9d_ood_eval_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:13:27.671Z\", \"updated_at\": \"2026-05-20T10:14:40.807Z\", \"hypothesis\": \"Evaluate 8B Cell C episode-level GRPO model (v9d step 10, val_before_train 96.875%) on 134 OOD ALFWorld tasks. Paper's key data point. Config fix via base64-encoded script: ppo_mini_batch_size=4, env_groups=2, n_groups=[2].\", \"parent\": \"8b_cell_c_episode_v9d\", \"spec\": {\"command\": \"bash -c \\\"echo aW1wb3J0IHJlCnBhdGggPSAnL3Jvb3QvY29zdC12ZXJpZnktYWdlbnQtcmwvUkFHRU4vY29uZmlnL19hbGZ3b3JsZF84Yl92OWRfb29kX2V2YWwueWFtbCcKdGV4dCA9IG9wZW4ocGF0aCkucmVhZCgpCnRleHQgPSByZS5zdWIocidwcG9fbWluaV9iYXRjaF9zaXplOlxzKlxkKycsICdwcG9fbWluaV9iYXRjaF9zaXplOiA0JywgdGV4dCkKdGV4dCA9IHJlLnN1YihyJ2Vudl9ncm91cHM6XHMqXGQrJywgJ2Vudl9ncm91cHM6IDInLCB0ZXh0LCBjb3VudD0xKQpuZXcgPSByZS5zdWIocicobl9ncm91cHM6XHMqXFspXGQrKFxdKScsIGxhbWJkYSBtOiBtLmdyb3VwKDEpICsgJzInICsgbS5ncm91cCgyKSwgdGV4dCwgY291bnQ9MSkKaWYgbmV3ID09IHRleHQ6CiAgICBuZXcgPSByZS5zdWIocicobl9ncm91cHM6W15cbl0qXG5ccyotXHMqKVxkKycsIGxhbWJkYSBtOiBtLmdyb3VwKDEpICsgJzInLCB0ZXh0LCBjb3VudD0xKQp0ZXh0ID0gbmV3Cm9wZW4ocGF0aCwgJ3cnKS53cml0ZSh0ZXh0KQpwcmludCgnRklYRUQnKQo= | base64 -d > /tmp/fix_ood.py && python3 /tmp/fix_ood.py && grep -n -E 'ppo_mini_batch_size|env_groups|group_size|n_groups' /root/cost-verify-agent-rl/RAGEN/config/_alfworld_8b_v9d_ood_eval.yaml && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/cost-verify-agent-rl/RAGEN && export WANDB_PROJECT=cost-verify-agent-rl && python train.py --config-name _alfworld_8b_v9d_ood_eval\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\", \"cuda:1\", \"cuda:2\", \"cuda:3\"], \"pid\": \"unknown\", \"log_path\": \"~/runs/cost-verify-agent-rl/8b_v9d_ood_eval_v3.log\", \"submitted_at\": \"2026-05-20T10:14:11.326Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 29.5, \"gpu_hours\": 0.03}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-20T10:14:40.807Z\"}, \"8b_v9d_ood_eval_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:12:05.992Z\", \"updated_at\": \"2026-05-20T10:13:16.252Z\", \"hypothesis\": \"Evaluate 8B Cell C episode-level GRPO model (v9d step 10, val_before_train 96.875%) on 134 OOD ALFWorld tasks (valid_unseen). Step 10 is effective final model (reward saturated at step 12, zero gradients). This is the paper's key data point: 8B model OOD generalization under episode-level GRPO. Retry of 8b_v9d_ood_eval with fixed config (ppo_mini_batch_size=4, env_groups=2, n_groups=[2]).\", \"parent\": \"8b_cell_c_episode_v9d\", \"spec\": {\"command\": \"bash -c \\\"cat > /tmp/fix_ood.py <<'PYEOF'\\nimport re\\npath = '/root/cost-verify-agent-rl/RAGEN/config/_alfworld_8b_v9d_ood_eval.yaml'\\ntext = open(path).read()\\ntext = re.sub(r'ppo_mini_batch_size:\\\\s*\\\\d+', 'ppo_mini_batch_size: 4', text)\\ntext = re.sub(r'env_groups:\\\\s*\\\\d+', 'env_groups: 2', text, count=1)\\nnew = re.sub(r'(n_groups:\\\\s*\\\\[)\\\\d+(\\\\])', lambda m: m.group(1) + '2' + m.group(2), text, count=1)\\nif new == text:\\n    new = re.sub(r'(n_groups:[^\\\\n]*\\\\n\\\\s*-\\\\s*)\\\\d+', lambda m: m.group(1) + '2', text, count=1)\\ntext = new\\nopen(path, 'w').write(text)\\nprint('FIXED')\\nPYEOF\\npython3 /tmp/fix_ood.py && grep -n -E 'ppo_mini_batch_size|env_groups|group_size|n_groups' /root/cost-verify-agent-rl/RAGEN/config/_alfworld_8b_v9d_ood_eval.yaml && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/cost-verify-agent-rl/RAGEN && export WANDB_PROJECT=cost-verify-agent-rl && python train.py --config-name _alfworld_8b_v9d_ood_eval\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\", \"cuda:1\", \"cuda:2\", \"cuda:3\"], \"pid\": \"unknown\", \"log_path\": \"~/runs/cost-verify-agent-rl/8b_v9d_ood_eval_v2.log\", \"submitted_at\": \"2026-05-20T10:12:41.132Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 35.1, \"gpu_hours\": 0.04}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-20T10:13:16.252Z\"}, \"8b_v9d_ood_eval\": {\"status\": \"DONE\", \"retry_count\": 3, \"created_at\": \"2026-05-20T09:37:39.568Z\", \"updated_at\": \"2026-05-20T10:11:53.284Z\", \"hypothesis\": \"Evaluate 8B Cell C episode-level GRPO model (v9d step 10, val_before_train 96.875%) on 134 OOD ALFWorld tasks (valid_unseen). Step 10 is effective final model (reward saturated at step 12, zero gradients). This is the paper's key data point: 8B model OOD generalization under episode-level GRPO.\", \"parent\": \"8b_cell_c_episode_v9d\", \"reproduce\": {\"finished_at\": \"2026-05-20T10:06:59.965Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-20T09:55:39.605Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T09:55:44.782123+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T10:02:54.140859+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T10:07:05.599655+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"bash -c \\\"sed -i 's/ppo_mini_batch_size: 2/ppo_mini_batch_size: 4/' /root/cost-verify-agent-rl/RAGEN/config/_alfworld_8b_v9d_ood_eval.yaml && sed -i 's/env_groups: 1/env_groups: 2/' /root/cost-verify-agent-rl/RAGEN/config/_alfworld_8b_v9d_ood_eval.yaml && grep -E 'ppo_mini_batch_size|env_groups|group_size' /root/cost-verify-agent-rl/RAGEN/config/_alfworld_8b_v9d_ood_eval.yaml && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/cost-verify-agent-rl/RAGEN && export WANDB_PROJECT=cost-verify-agent-rl && python train.py --config-name _alfworld_8b_v9d_ood_eval\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\", \"cuda:1\", \"cuda:2\", \"cuda:3\"], \"pid\": \"719730\", \"log_path\": \"~/runs/cost-verify-agent-rl/8b_v9d_ood_eval.log\", \"submitted_at\": \"2026-05-20T10:04:30.975Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 151.1, \"gpu_hours\": 0.17}, \"conclusion\": \"failed\"}, \"8b_cell_c_episode_v9d\": {\"status\": \"DONE\", \"retry_count\": 3, \"created_at\": \"2026-05-19T23:13:25.570Z\", \"updated_at\": \"2026-05-20T09:32:19.245Z\", \"hypothesis\": \"FSDP2 + CPUOffloadPolicy 8B Cell C episode-level GRPO。v9c 证明训练有效（2步 success 40%→64%），但 step 3 因 max_prompt_length==max_model_len 溢出。v9d 修复：max_prompt_length 16384→15360，留 1024 token headroom。从头训练（无 checkpoint）。\", \"parent\": \"8b_cell_c_episode_v9c\", \"reproduce\": {\"finished_at\": \"2026-05-20T07:55:47.277Z\"}, \"failure_reason\": \"EXIT_CODE=129 (SIGHUP) at step 7/30. Training was healthy: train_success 91.4%, entropy 0.047, disk 91GB. Not algorithmic — signal kill. 3rd operational crash (disk full → deleted model → SIGHUP). Worker dispatched to diagnose + restart.\", \"completed_at\": \"2026-05-20T02:20:48.275Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T02:20:51.818939+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T05:13:00.335716+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T07:55:52.509825+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"metrics\": {\"step\": 7, \"steps_total\": 30, \"step_time_s\": 1300, \"eta_hours\": 8, \"train_success_step6\": 0.852, \"train_success_step7\": 0.914, \"pass_at_8\": 1, \"entropy_step7\": 0.0473, \"kl_step7\": -0.034, \"grad_norm_step7\": 0.573, \"pg_loss_step7\": 0.00096, \"disk_available_gb\": 91, \"disk_risk\": \"step 5 ckpt still 92GB (pre-config-change). step 10 ckpt must be ~33GB or disk crash. Need verification.\", \"wandb_run_id\": \"4x8hludk\", \"gpu_util\": \"75%/61%/82%/100%\", \"gpu_mem_gb\": \"24/98 per card\"}, \"notes\": \"SIGHUP 诊断 (2026-05-20): 无 EXIT_CODE=129。v9d 实际到达 step 10（checkpoint 存在 92GB），之前 metrics 仅更新到 step 7。v9c 根因: vLLM prompt 16384 = max_model_len 溢出 (EXIT_CODE=1)。v9d 已重启 (15:56 UTC)，从 step 10 恢复，wandb: aeml21w9。SFT checkpoint 通过 symlink→Qwen3-8B 修复。剩余 20 步。风险: prompt 长度崩溃仍可能重现。\"}}, \"notes\": \"SIGHUP 诊断 (2026-05-20): 无 EXIT_CODE=129。v9d 实际到达 step 10（checkpoint 存在 92GB），之前 metrics 仅更新到 step 7。v9c 根因: vLLM prompt 16384 = max_model_len 溢出 (EXIT_CODE=1)。v9d 已重启 (15:56 UTC)，从 step 10 恢复，wandb: aeml21w9。SFT checkpoint 通过 symlink→Qwen3-8B 修复。剩余 20 步。风险: prompt 长度崩溃仍可能重现。\", \"spec\": {\"command\": \"bash -c \\\"ln -sf /root/autodl-tmp/models/Qwen3-8B /root/autodl-tmp/checkpoints/qwen3_8b_sft_v1/checkpoint-231 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/cost-verify-agent-rl/RAGEN && export WANDB_PROJECT=cost-verify-agent-rl && python train.py --config-name _alfworld_8b_cell_c_v9\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\", \"cuda:1\", \"cuda:2\", \"cuda:3\"], \"pid\": \"652262\", \"data_path\": \"/root/autodl-tmp/data/alfworld/train/\", \"data_count\": 8810, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"log_path\": \"/root/runs/cost-verify-agent-rl/8b_cell_c_episode_v9d.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/8b-cell-c-v9/global_step_10/\", \"checkpoint_source\": \"step 10 checkpoint + Qwen3-8B base model symlink\", \"eval_data\": \"N/A - training experiment\", \"save_contents\": [\"model\", \"extra\"], \"note\": \"6th start: resume from step 10 with fixed save_contents yaml (actor_rollout_ref.actor.checkpoint).\"}, \"metrics\": {\"step\": 15, \"steps_total\": 30, \"stopped_reason\": \"reward_saturation_and_nccl_hang\", \"train_success_step12\": 1, \"pg_loss_step12\": 0, \"advantage_step12\": 0, \"val_before_train_step10\": 0.96875, \"train_success_step7\": 0.914, \"train_success_step11\": 0.9375, \"effective_final_step\": 10, \"wandb_run_id\": \"aeml21w9\", \"note\": \"Reward saturated at step 12 (100% success, zero gradients). NCCL hang at step 15. Step 10 checkpoint is effective final model.\"}, \"conclusion\": \"success\"}, \"8b_cell_c_episode_v9c\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T19:08:11.566Z\", \"updated_at\": \"2026-05-19T23:10:39.477Z\", \"hypothesis\": \"FSDP2 + CPUOffloadPolicy 解决 8B Cell C backward OOM。v9b 因 _fsdp_wrapped_module (FSDP1 专属属性) 在 compute_log_prob 崩溃。v9c 全量修复 5 个文件 10 处 FSDP1-specific 模式（_fsdp_wrapped_module→getattr 兼容, summon_full_params→isinstance 守卫）。预期无 FSDP1/2 兼容性问题。\", \"parent\": \"8b_cell_c_episode_v9b\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/cost-verify-agent-rl/RAGEN && export WANDB_PROJECT=cost-verify-agent-rl && python train.py --config-name _alfworld_8b_cell_c_v9\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\", \"cuda:1\", \"cuda:2\", \"cuda:3\"], \"pid\": \"178115\", \"log_path\": \"~/runs/cost-verify-agent-rl/8b_cell_c_episode_v9c.log\", \"submitted_at\": \"2026-05-19T19:08:33.403Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/alfworld/train/\", \"data_count\": 8810, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/8b-cell-c-v9/\", \"checkpoint_source\": \"Qwen3-8B base (no SFT)\", \"eval_data\": \"N/A - training experiment, parent is derivation chain not eval source\", \"wall_clock_seconds\": 14526.1, \"gpu_hours\": 16.14}, \"metrics\": {\"step\": 1, \"val_reward_mean_at_32\": 4.06, \"gpu_mem_peak_gb\": 83, \"step_time_min\": 31.5}, \"conclusion\": \"failed\", \"failure_reason\": \"vLLM prompt length overflow: max_prompt_length (16384) == max_model_len (16384), no room for generation output. Crashed at step 3/30 during rollout. Fix: lower max_prompt_length to 15360.\", \"completed_at\": \"2026-05-19T23:10:39.477Z\"}, \"8b_cell_c_episode_v9b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T18:36:02.652Z\", \"updated_at\": \"2026-05-19T18:58:19.550Z\", \"hypothesis\": \"FSDP2 + CPUOffloadPolicy 解决 8B Cell C backward OOM（v7 缺口 3.7 GiB）。v9 失败于 NotImplementedError（train.py 不识别 fsdp2 strategy），已修复：train.py 接受 fsdp2 + critic.strategy=fsdp2。重试。\", \"parent\": \"8b_cell_c_episode_v9\", \"server\": \"westd-47453\", \"gpu\": \"cuda:0,cuda:1,cuda:2,cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-47453\", \"gpu\": \"cuda:0,cuda:1,cuda:2,cuda:3\", \"started_at\": \"2026-05-19T18:36:15.510Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/cost-verify-agent-rl/RAGEN && export WANDB_PROJECT=cost-verify-agent-rl && export CUDA_VISIBLE_DEVICES=0,1,2,3 && python train.py --config-name _alfworld_8b_cell_c_v9\\\"\", \"finished_at\": \"2026-05-19T18:56:35.614Z\", \"training_hours\": 0.34}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/cost-verify-agent-rl/RAGEN && export WANDB_PROJECT=cost-verify-agent-rl && export CUDA_VISIBLE_DEVICES=0,1,2,3 && python train.py --config-name _alfworld_8b_cell_c_v9\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\", \"cuda:1\", \"cuda:2\", \"cuda:3\"], \"pid\": \"157729\", \"data_count\": 8810, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"wandb_run_id\": \"7xfef8p6\", \"log_path\": \"~/runs/cost-verify-agent-rl/8b_cell_c_episode_v9b.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/8b-cell-c-v9/\", \"hyperparams\": {\"strategy\": \"fsdp2\", \"offload_policy\": true, \"activation_offload\": true, \"ppo_mini_batch_size\": 4, \"gpu_memory_utilization\": 0.25, \"max_model_len\": 16384, \"use_ref\": false, \"reward\": \"episode-level\"}}, \"pid\": \"157729\", \"log_path\": \"~/runs/cost-verify-agent-rl/8b_cell_c_episode_v9b.log\", \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-19T18:56:37.556Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T18:56:40.574889+00:00\"}]}}, \"scienceworld_sft_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T18:11:10.597Z\", \"updated_at\": \"2026-05-19T18:46:33.866Z\", \"hypothesis\": \"Evaluate ScienceWorld SFT checkpoint on dev split (1796 episodes, 30 task types). Establishes SFT baseline success rate for ScienceWorld before GRPO experiments.\", \"parent\": \"scienceworld_sft\", \"spec\": {\"command\": \"python /root/cost-verify-agent-rl/eval_scienceworld.py --temperature 0.4\", \"server\": \"bjb1-17606\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"183712\", \"data_path\": \"scienceworld dev split\", \"data_count\": 1796, \"model_name\": \"Qwen3-1.7B (ScienceWorld SFT)\", \"seed\": 42, \"log_path\": \"/tmp/eval_scienceworld.log\", \"checkpoint_source\": \"scienceworld_sft/global_step_448\", \"eval_data\": \"ScienceWorld dev split, 1796 episodes, 30 task types\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-19T18:46:33.866Z\"}, \"8b_cell_c_episode_v9\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T18:12:32.644Z\", \"updated_at\": \"2026-05-19T18:35:55.002Z\", \"hypothesis\": \"FSDP2 + CPUOffloadPolicy 解决 8B Cell C backward OOM（v7 缺口 3.7 GiB）。CPU offload 将参数和 optimizer states 按 layer 搬运，GPU 峰值从 ~55-65GB 降至 ~26-36GB。验证 8B 模型 episode-level GRPO 训练可行性。\", \"parent\": \"8b_cell_c_episode_v8\", \"server\": \"westd-47453\", \"gpu\": \"cuda:0,cuda:1,cuda:2,cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-47453\", \"gpu\": \"cuda:0,cuda:1,cuda:2,cuda:3\", \"started_at\": \"2026-05-19T18:13:33.083Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/cost-verify-agent-rl/RAGEN && export WANDB_PROJECT=cost-verify-agent-rl && export CUDA_VISIBLE_DEVICES=0,1,2,3 && python train.py --config-name _alfworld_8b_cell_c_v9\\\"\", \"finished_at\": \"2026-05-19T18:16:07.543Z\", \"training_hours\": 0.04}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/cost-verify-agent-rl/RAGEN && export WANDB_PROJECT=cost-verify-agent-rl && export CUDA_VISIBLE_DEVICES=0,1,2,3 && python train.py --config-name _alfworld_8b_cell_c_v9\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\", \"cuda:1\", \"cuda:2\", \"cuda:3\"], \"pid\": \"148894\", \"log_path\": \"~/runs/cost-verify-agent-rl/8b_cell_c_episode_v9.log\", \"submitted_at\": \"2026-05-19T18:13:35.317Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 154.1, \"gpu_hours\": 0.17}, \"pid\": \"148894\", \"log_path\": \"~/runs/cost-verify-agent-rl/8b_cell_c_episode_v9.log\", \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-19T18:16:09.400Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T18:16:12.439790+00:00\"}]}, \"notes\": \"失败原因: NotImplementedError at train.py:245 — TaskRunner.run() 中 FSDP2+CPUOffload 代码路径未实现。策略配置 strategy=fsdp 但 run() 方法对应分支 raise NotImplementedError。运行仅 154s，初始化阶段即崩溃。 | 已有成果: 无（未进入训练） | 建议: 需在 train.py 中实现 FSDP2+CPUOffloadPolicy 的 run 逻辑\", \"metrics\": {\"failure_reason\": \"NotImplementedError in train.py:245 - FSDP2 strategy not handled in if-else\", \"fix\": \"Added fsdp2 to strategy check + critic.strategy=fsdp2 in config\"}}, \"scienceworld_sft\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T14:35:00.255Z\", \"updated_at\": \"2026-05-19T17:50:12.565Z\", \"hypothesis\": \"ScienceWorld 1.7B SFT 训练，为后续 GRPO 实验提供 base checkpoint。验证 SFT 训练 pipeline 可泛化到第二个交互环境（ALFWorld 之外），支撑跨环境 RL 训练失败机制对比（Cell A vs Cell C）。数据：3592 train / 1796 val expert trajectories。\", \"spec\": {\"command\": \"bash /root/cost-verify-agent-rl/RAGEN/scripts/run_scienceworld_sft.sh\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\", \"cuda:1\", \"cuda:2\", \"cuda:3\"], \"pid\": \"120838\", \"data_path\": \"/root/autodl-tmp/expert_sft/scienceworld_sft_train.jsonl\", \"data_count\": 3592, \"model_name\": \"Qwen3-1.7B\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/wandb/\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/scienceworld_sft/\", \"hyperparams\": {\"lr\": \"5e-6\", \"epochs\": 2, \"batch_size\": 16, \"max_length\": 16384, \"fsdp\": \"fsdp2\"}, \"wandb_run_id\": \"dqoxg94e\", \"notes\": \"原始 wrapper PID 120827 已退出，实际 torchrun PID 120838，workers 120904-120907\"}, \"conclusion\": \"success\", \"metrics\": {\"train_loss_final\": 0.00318, \"val_loss_final\": 0.01098, \"total_steps\": 448, \"epochs\": 2, \"total_train_time_s\": 9319.4, \"checkpoint\": \"global_step_448\"}, \"completed_at\": \"2026-05-19T17:50:12.566Z\"}, \"exp029_per_task_t04_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T14:40:00.807Z\", \"updated_at\": \"2026-05-19T15:24:57.755Z\", \"hypothesis\": \"Per-task-type OOD eval with T=0.4 (paper protocol D092) will show similar task-type ranking pattern as T=0.0 but with higher overall success rate (~23.88% vs 16.4%). Multi-step tasks (heat/cool/two_obj) expected to remain worst. Rerun after v1 vLLM crash.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0,1 python eval_per_task_type.py 2>&1 | tee /root/autodl-tmp/tmp/exp029_per_task_t04.log\", \"server\": \"bjb1-17606\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"171794\", \"data_path\": \"ALFWorld valid_unseen 134 OOD tasks\", \"data_count\": 134, \"model_name\": \"exp029_seed1_global_step_15\", \"seed\": 1, \"checkpoint_source\": \"exp029_episode_level global_step_15\", \"eval_data\": \"ALFWorld valid_unseen 134 OOD tasks, T=0.4, do_sample=True\", \"log_path\": \"/root/autodl-tmp/tmp/exp029_per_task_t04.log\", \"checkpoint_path\": \"/root/autodl-tmp/tmp/exp029_per_task_type_breakdown_t04.json\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T15:06:52.270Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T15:06:53.812Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T15:06:56.750401+00:00\"}]}, \"metrics\": {\"temperature\": 0.4, \"total_success_rate\": 0.194, \"total_success\": 26, \"total_tasks\": 134, \"pick_and_place_simple\": {\"count\": 24, \"success\": 4, \"rate\": 0.167}, \"pick_clean_then_place_in_recep\": {\"count\": 31, \"success\": 8, \"rate\": 0.258}, \"pick_heat_then_place_in_recep\": {\"count\": 23, \"success\": 4, \"rate\": 0.174}, \"pick_cool_then_place_in_recep\": {\"count\": 21, \"success\": 5, \"rate\": 0.238}, \"look_at_obj_in_light\": {\"count\": 18, \"success\": 5, \"rate\": 0.278}, \"pick_two_obj_and_place\": {\"count\": 17, \"success\": 0, \"rate\": 0}}, \"notes\": \"独立 eval script T=0.4 得 19.4% (26/134)，vs RAGEN 内置 eval 23.88% (32/134)。差 4.48pp，需排查 pipeline 差异（任务 B）。结果文件：/root/autodl-tmp/tmp/exp029_per_task_type_breakdown_t04.json。Cron 误标 failed，实际成功完成。\"}, \"exp029_per_task_t04\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T14:17:41.710Z\", \"updated_at\": \"2026-05-19T14:31:42.043Z\", \"hypothesis\": \"Per-task-type OOD eval with T=0.4 (paper protocol D092) will show similar task-type ranking pattern as T=0.0 but with higher overall success rate (~23.88% vs 16.4%). Multi-step tasks (heat/cool/two_obj) expected to remain worst.\", \"parent\": \"exp029_per_task_breakdown\", \"spec\": {\"command\": \"python eval_per_task_type.py\", \"server\": \"bjb1-17606\", \"model_name\": \"exp029_hf (Qwen3-based)\", \"seed\": 1, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/exp029_hf\", \"eval_data\": \"alfworld eval_out_of_distribution (134 tasks)\", \"data_count\": 134, \"data_path\": \"/root/autodl-tmp/alfworld\"}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-19T14:31:42.043Z\"}, \"8b_cell_c_episode_v8\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T14:10:15.655Z\", \"updated_at\": \"2026-05-19T14:16:13.413Z\", \"hypothesis\": \"Reducing ppo_mini_batch_size 4→2 halves backward activation memory (~3.7 GiB freed), and lowering gpu_memory_utilization 0.25→0.22 returns ~2.88 GiB/GPU to PyTorch allocator. Together these resolve the backward OOM that killed v7 (needed 3.7 GiB, had 0). D094 final attempt — if fails, 8B Cell C abandoned.\", \"parent\": \"8b_cell_c_episode_v7\", \"spec\": {\"command\": \"bash -c 'cd /root/cost-verify-agent-rl/RAGEN/config && sed ... && python train.py --config-name _alfworld_8b_cell_c'\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\", \"cuda:1\", \"cuda:2\", \"cuda:3\"], \"pid\": \"113992\", \"log_path\": \"~/runs/cost-verify-agent-rl/8b_cell_c_episode_v8.log\", \"submitted_at\": \"2026-05-19T14:13:14.349Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 31.4, \"gpu_hours\": 0.03, \"data_path\": \"ALFWorld\", \"data_count\": 3553, \"model_name\": \"Qwen3-8B\", \"seed\": 1, \"checkpoint_path\": \"N/A - failed on config validation\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T14:13:43.897Z\"}, \"failure_reason\": \"Traceback → h_size, \\\\ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ AssertionError: actor ppo_micro_batch_size_per_gpu * n_gpus_per_node (4) must be less than or equal to ppo_mini_batch_size (2)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-19T14:13:45.704Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T14:13:49.206647+00:00\"}]}, \"notes\": \"失败原因: 配置约束违反 — ppo_mini_batch_size=2 但 ppo_micro_batch_size_per_gpu(1)*n_gpus(4)=4 > 2。4 GPU 下 mini_batch 最小为 4。| 根因: v7 已证明 mini_batch=4 时 backward 需 8.94 GiB 仅剩 3.83 GiB，无法进一步缩小 mini_batch。8B Cell C episode-level 在 4×96GB 上内存死锁 — FSDP+actor+optimizer+vLLM KV cache 占满显存，backward 无余量。| D094 已标记为最后尝试，8 次连续失败(v1→v8)，覆盖了所有可行参数组合(use_ref, gpu_mem_util, max_model_len, mini_batch_size)。| 建议: 放弃 8B Cell C，用 1.7B Cell C (exp029, 已 success) 作为论文正面对照\"}, \"exp029_per_task_breakdown\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T12:22:29.035Z\", \"updated_at\": \"2026-05-19T14:15:04.649Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python eval_per_task_type.py\\\"\", \"server\": \"bjb1-17606\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"169264\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp029_per_task_breakdown.log\", \"submitted_at\": \"2026-05-19T13:22:17.722Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"ALFWorld valid_unseen 134 tasks grouped by task type\", \"data_count\": 134, \"model_name\": \"exp029_seed1_global_step_15\", \"seed\": 1, \"checkpoint_source\": \"exp029_episode_level global_step_15\", \"eval_data\": \"ALFWorld valid_unseen 134 OOD tasks\", \"checkpoint_path\": \"/root/autodl-tmp/tmp/exp029_per_task_type_breakdown.json\", \"wall_clock_seconds\": 3166.9, \"gpu_hours\": 1.76}, \"hypothesis\": \"Per-task-type OOD eval of exp029 seed1 (Cell C, episode-level + full context) will reveal which ALFWorld task types benefit most from RL training, providing granular analysis for paper Results section. Checkpoint: global_step_15, 134 OOD tasks grouped by task type.\", \"parent\": \"exp029_episode_level\", \"reproduce\": {\"finished_at\": \"2026-05-19T14:06:22.115Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T14:06:24.846177+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"temperature\": 0, \"total_success_rate\": 0.164, \"pick_and_place_simple\": {\"count\": 24, \"success\": 5, \"rate\": 0.208}, \"pick_clean_then_place_in_recep\": {\"count\": 31, \"success\": 8, \"rate\": 0.258}, \"pick_heat_then_place_in_recep\": {\"count\": 23, \"success\": 1, \"rate\": 0.043}, \"pick_cool_then_place_in_recep\": {\"count\": 21, \"success\": 2, \"rate\": 0.095}, \"look_at_obj_in_light\": {\"count\": 18, \"success\": 5, \"rate\": 0.278}, \"pick_two_obj_and_place\": {\"count\": 17, \"success\": 1, \"rate\": 0.059}}, \"completed_at\": \"2026-05-19T14:15:04.649Z\"}, \"8b_cell_c_episode_v7\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T13:45:33.729Z\", \"updated_at\": \"2026-05-19T14:06:53.506Z\", \"hypothesis\": \"8B Cell C episode-level with gpu_memory_utilization=0.25 (up from 0.20, giving 6.24 GiB KV cache vs needed 2.25 GiB) and max_model_len=16384. v5 solved OOM (use_ref=False), v6 failed on insufficient KV cache (1.44 GiB < 2.25 GiB needed). D093 math: 0.25 gives 2.8x headroom. No expandable_segments (vLLM incompatible).\", \"parent\": \"8b_cell_c_episode_v6\", \"spec\": {\"command\": \"bash -c 'cd /root/cost-verify-agent-rl/RAGEN/config && sed ... && python train.py --config-name _alfworld_8b_cell_c'\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\", \"cuda:1\", \"cuda:2\", \"cuda:3\"], \"pid\": \"93170\", \"log_path\": \"~/runs/cost-verify-agent-rl/8b_cell_c_episode_v7.log\", \"submitted_at\": \"2026-05-19T13:45:56.063Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"ALFWorld train 140 games\", \"data_count\": 140, \"model_name\": \"qwen3_8b_sft_v1/checkpoint-231\", \"seed\": 42, \"checkpoint_source\": \"7b_sft_v1\", \"eval_data\": \"ALFWorld train 140 + val 32 (in-training eval)\", \"wall_clock_seconds\": 1257.4, \"gpu_hours\": 1.4}, \"reproduce\": {\"finished_at\": \"2026-05-19T14:06:51.627Z\"}, \"failure_reason\": \"CUDA OOM: CUDA out of memory. Tried to allocate 8.94 GiB. GPU 0 has a total capacity of 94.97 GiB of which 3.83 GiB is free. Including non-PyTorch memory, this process has 91.13 GiB memory in use. Of the allocated memory 110.14 GiB is allocated by PyTorch, wit\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-19T14:06:53.506Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T14:06:59.873595+00:00\"}]}}, \"8b_cell_c_episode_v6\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T13:23:28.445Z\", \"updated_at\": \"2026-05-19T13:46:13.860Z\", \"hypothesis\": \"8B Cell C episode-level with use_ref=False, max_model_len=16384 (up from 8192 which was too short for some prompts), no expandable_segments (incompatible with vLLM CuMemAllocator). v5 proved OOM is solved and VLLM inits successfully; v6 fixes the remaining prompt length issue. If backward pass succeeds, Cell C at 8B scale provides the positive control for scale-invariant information loss analysis.\", \"parent\": \"8b_cell_c_episode_v5\", \"spec\": {\"command\": \"bash -c 'cd /root/cost-verify-agent-rl/RAGEN/config && sed -i \\\"s/max_model_len: 8192/max_model_len: 16384/g\\\" _alfworld_8b_cell_c.yaml && echo \\\"=== Config verification ===\\\" && grep -E \\\"max_model_len|use_ref|use_kl_loss|gpu_memory_utilization|ppo_mini_batch_size\\\" _alfworld_8b_cell_c.yaml && echo \\\"=== Starting training ===\\\" && cd /root/cost-verify-agent-rl/RAGEN && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && mkdir -p /root/autodl-tmp/checkpoints/8b-cell-c /root/autodl-tmp/tmp && export TMPDIR=/root/autodl-tmp/tmp && export RAY_TMPDIR=/root/autodl-tmp/ray_tmp && export WANDB_PROJECT=cost-verify-agent-rl && CUDA_VISIBLE_DEVICES=0,1,2,3 python train.py --config-name _alfworld_8b_cell_c'\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\", \"cuda:1\", \"cuda:2\", \"cuda:3\"], \"pid\": \"84321\", \"log_path\": \"~/runs/cost-verify-agent-rl/8b_cell_c_episode_v6.log\", \"submitted_at\": \"2026-05-19T13:24:02.584Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1180.4, \"gpu_hours\": 1.31}, \"reproduce\": {\"finished_at\": \"2026-05-19T13:43:41.216Z\"}, \"failure_reason\": \"vLLM KV cache OOM: max_model_len=16384 needs 2.25 GiB KV cache but only 1.44 GiB available (gpu_memory_utilization=0.20). Estimated max supported length: 10480. Fix: reduce max_model_len to 10240 or increase gpu_memory_utilization to ~0.30.\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-19T13:43:43.030Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T13:43:46.122639+00:00\"}]}, \"notes\": \"失败原因: vLLM KV cache 内存不足 — max_model_len=16384 需 2.25 GiB，gpu_memory_utilization=0.20 仅提供 1.44 GiB (estimated max len=10480) | v5→v6 progression: v5 证明 use_ref=False + util=0.20 解决了 FSDP OOM 和 vLLM init 问题，但 max_model_len=8192 太短；v6 增到 16384 又超了 KV cache 预算 | 建议: v7 用 max_model_len=10240 (在 1.44 GiB 预算内) 或 gpu_memory_utilization=0.25-0.30 给更多 KV cache 空间\"}, \"8b_cell_c_episode_v5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T13:11:45.033Z\", \"updated_at\": \"2026-05-19T13:18:55.955Z\", \"hypothesis\": \"8B Cell C episode-level with use_ref=False (releasing ~8 GiB/GPU from ref model) and gpu_memory_utilization=0.20 will resolve the Catch-22 OOM: FSDP+ref baseline ~90 GiB/GPU leaves no room for VLLM. Removing ref model is the only viable fix since batch/token params were already minimized in v1-v3 and gpu_memory_utilization=0.15 was too low for VLLM init in v4.\", \"parent\": \"8b_cell_c_episode_v2\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/cost-verify-agent-rl/RAGEN && CUDA_VISIBLE_DEVICES=0,1,2,3 PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True python train.py --config-name _alfworld_8b_cell_c'\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\", \"cuda:1\", \"cuda:2\", \"cuda:3\"], \"pid\": \"75042\", \"log_path\": \"~/runs/cost-verify-agent-rl/8b_cell_c_episode_v5.log\", \"submitted_at\": \"2026-05-19T13:16:02.004Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"ALFWorld train 140 games\", \"data_count\": 140, \"model_name\": \"qwen3_8b_sft_v1/checkpoint-231\", \"seed\": 42, \"checkpoint_source\": \"7b_sft_v1\", \"eval_data\": \"ALFWorld train 140 + val 32 (in-training eval)\", \"checkpoint_path\": \"N/A (failed before first step)\", \"wall_clock_seconds\": 174.0, \"gpu_hours\": 0.19}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-19T13:18:55.955Z\"}, \"8b_cell_c_episode_v4\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T12:49:54.545Z\", \"updated_at\": \"2026-05-19T12:49:54.545Z\", \"spec\": {\"command\": \"bash -c 'export TMPDIR=/root/autodl-tmp/tmp && mkdir -p /root/autodl-tmp/tmp && export RAY_TMPDIR=/root/autodl-tmp/ray_tmp && mkdir -p /root/autodl-tmp/ray_tmp && export TMUX_TMPDIR=/root/autodl-tmp/tmux && mkdir -p /root/autodl-tmp/tmux && export TORCH_COMPILE_DISABLE=1 && export PYTHONUNBUFFERED=1 && export WANDB_PROJECT=cost-verify-agent-rl && export WANDB_DIR=/root/autodl-tmp/wandb && export WANDB_TMPDIR=/root/autodl-tmp/tmp && export CUDA_VISIBLE_DEVICES=0,1,2,3 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/cost-verify-agent-rl/RAGEN && python train.py --config-name _alfworld_8b_cell_c'\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\", \"cuda:1\", \"cuda:2\", \"cuda:3\"], \"pid\": \"58153\", \"log_path\": \"~/runs/cost-verify-agent-rl/8b_cell_c_episode_v4.log\", \"submitted_at\": \"2026-05-19T12:49:54.289Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"8b_cell_c_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T12:14:42.678Z\", \"updated_at\": \"2026-05-19T12:47:42.902Z\", \"spec\": {\"command\": \"python train.py --config-name _alfworld_8b_cell_c (ppo_mini_batch_size=4)\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\", \"cuda:1\", \"cuda:2\", \"cuda:3\"], \"pid\": \"36872\", \"log_path\": \"~/runs/cost-verify-agent-rl/8b_cell_c_v3.log\", \"submitted_at\": \"2026-05-19T12:19:12.602Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"ALFWorld 32 in-dist tasks\", \"data_count\": 32, \"model_name\": \"qwen3_8b_sft_v1/checkpoint-231\", \"seed\": 42, \"checkpoint_source\": \"qwen3_8b_sft_v1/checkpoint-231\", \"eval_data\": \"32 in-dist ALFWorld val tasks\", \"checkpoint_path\": \"N/A (OOM before first step)\", \"wall_clock_seconds\": 1710.3, \"gpu_hours\": 1.9}, \"hypothesis\": \"8B Cell C (episode-level, full context) with ppo_mini_batch_size=4 can pass backward without OOM. Positive control for scale analysis: if 8B Cell C maintains/improves from SFT baseline while Cell A collapses, confirms scale-invariant information loss mechanism.\", \"parent\": \"8b_cell_c_episode_v2\", \"conclusion\": \"failed\", \"failure_reason\": \"CUDA OOM at loss.backward() (dp_actor.py:468). Tried to allocate 8.76 GiB, GPU had 118.48 GiB allocated across FSDP shards with only ~5-6 GiB free. ppo_mini_batch_size=4 insufficient — same OOM pattern as v1 and v2. Third consecutive backward-pass OOM.\", \"completed_at\": \"2026-05-19T12:47:42.902Z\"}, \"8b_det_eval_h2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T11:54:36.334Z\", \"updated_at\": \"2026-05-19T12:32:42.763Z\", \"spec\": {\"command\": \"python train.py --config-name _alfworld_8b_det_eval_h2\", \"server\": \"bjb1-17606\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"160160\", \"log_path\": \"~/runs/cost-verify-agent-rl/8b_det_eval_h2.log\", \"submitted_at\": \"2026-05-19T11:54:36.028Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"32 in-dist ALFWorld val tasks\", \"data_count\": 32, \"model_name\": \"qwen3_8b_sft_v1/checkpoint-231\", \"seed\": 123, \"checkpoint_source\": \"qwen3_8b_sft_v1/checkpoint-231\", \"eval_data\": \"32 in-dist tasks, T=0, greedy, h=2 windowing\", \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 2286.7, \"gpu_hours\": 1.27}, \"hypothesis\": \"h=2 windowing at T=0 deterministic eval will show substantial information loss compared to full-context T=0 eval on same 32 in-dist tasks. The gap quantifies pure information loss without sampling variance confound. Expected significant degradation from full-context baseline.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.3125, \"num_actions\": 37.59, \"action_is_valid\": 0.9188, \"pass_at_1\": 0.3125, \"eval_tasks\": 32, \"temperature\": 0, \"do_sample\": false, \"wandb_run\": \"qtxhh5ak\", \"information_loss_pp\": 37.5, \"information_loss_relative\": 0.545}, \"completed_at\": \"2026-05-19T12:32:42.763Z\"}, \"8b_det_eval_full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T11:49:48.132Z\", \"updated_at\": \"2026-05-19T12:32:41.705Z\", \"spec\": {\"command\": \"python train.py --config-name _alfworld_8b_det_eval_full\", \"server\": \"bjb1-17606\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"155887\", \"log_path\": \"~/runs/cost-verify-agent-rl/8b_det_eval_full.log\", \"submitted_at\": \"2026-05-19T11:49:47.504Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"32 in-dist ALFWorld val tasks\", \"data_count\": 32, \"model_name\": \"qwen3_8b_sft_v1/checkpoint-231\", \"seed\": 123, \"checkpoint_source\": \"qwen3_8b_sft_v1/checkpoint-231\", \"eval_data\": \"32 in-dist tasks, T=0, greedy decoding\", \"checkpoint_path\": \"N/A (eval only)\", \"wall_clock_seconds\": 2574.2, \"gpu_hours\": 1.43}, \"hypothesis\": \"Full-context deterministic eval (T=0) of 8B SFT checkpoint provides the true baseline success rate on 32 in-dist tasks, eliminating sampling variance. Expected ~70-80% given 80.6% OOD performance. This number is the denominator for quantifying information loss from h=2 windowing.\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.6875, \"num_actions\": 24.22, \"action_is_valid\": 0.926, \"pass_at_1\": 0.6875, \"eval_tasks\": 32, \"temperature\": 0, \"do_sample\": false, \"wandb_run\": \"mb005ir1\"}, \"completed_at\": \"2026-05-19T12:32:41.705Z\"}, \"8b_cell_c_episode_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T11:47:08.586Z\", \"updated_at\": \"2026-05-19T12:14:02.446Z\", \"spec\": {\"command\": \"python train.py --config-name _alfworld_8b_cell_c\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\", \"cuda:1\", \"cuda:2\", \"cuda:3\"], \"pid\": \"7176\", \"log_path\": \"~/runs/cost-verify-agent-rl/8b_cell_c_episode_v2.log\", \"submitted_at\": \"2026-05-19T11:49:06.817Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen3-8B-SFT (checkpoint-231)\", \"data_path\": \"ALFWorld train 140 games\", \"data_count\": 140, \"seed\": 42, \"checkpoint_source\": \"7b_sft_v1\", \"eval_data\": \"ALFWorld train 140 + val 32 (in-training eval)\", \"hyperparams\": {\"lr\": 5e-07, \"context_window_mode\": \"episode_level\", \"total_training_steps\": 30, \"n_gpus\": 4, \"gradient_checkpointing\": true, \"optimizer_offload\": true, \"enable_think\": false, \"save_freq\": 999, \"ppo_max_token_len_per_gpu\": 16384, \"log_prob_max_token_len_per_gpu\": 16384, \"PYTORCH_CUDA_ALLOC_CONF\": \"expandable_segments:True\"}, \"wall_clock_seconds\": 1302.8, \"gpu_hours\": 1.45}, \"hypothesis\": \"8B Cell C v2: episode-level RL with full context from 80.6% SFT baseline. Same as 8b_cell_c_episode but with OOM fix (ppo_max_token_len_per_gpu 32768→16384, PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True). Positive control for scale analysis. Core comparison vs Cell A: Cell A collapse + Cell C stability = scale-invariant mechanism confirmation. lr=5e-7.\", \"parent\": \"7b_sft_v1\", \"reproduce\": {\"finished_at\": \"2026-05-19T12:10:47.882Z\"}, \"failure_reason\": \"CUDA OOM: CUDA out of memory. Tried to allocate 8.76 GiB. GPU 0 has a total capacity of 94.97 GiB of which 4.94 GiB is free. Including non-PyTorch memory, this process has 89.98 GiB memory in use. Of the allocated memory 118.48 GiB is allocated by PyTorch, wit\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-19T12:10:49.641Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T12:10:52.542394+00:00\"}]}, \"notes\": \"Second OOM at backward(). ppo_max_token_len_per_gpu 32768→16384 无效（内存数字与 v1 完全一致：tried to alloc 8.76GiB, 4.94GiB free）。瓶颈是 backward pass 同时处理的序列数，不是总 token 数。Fix: ppo_mini_batch_size 16→4。Retrying as 8b_cell_c_v3.\"}, \"8b_cell_c_episode\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T10:08:01.438Z\", \"updated_at\": \"2026-05-19T11:46:47.187Z\", \"hypothesis\": \"8B Cell C: episode-level RL with full context from 80.6% SFT baseline. Positive control for scale analysis. At 1.7B Cell C reached ~28-31% OOD. If 8B Cell C maintains/improves from 80.6%, confirms episode-level advantage is robust across model scales. Core comparison vs Cell A: Cell A collapse (28.1%→12.5% step 1) + Cell C stability = scale-invariant mechanism confirmation. lr=5e-7.\", \"parent\": \"7b_sft_v1\", \"spec\": {\"command\": \"python train.py --config-name _alfworld_8b_cell_c\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\", \"cuda:1\", \"cuda:2\", \"cuda:3\"], \"pid\": \"977400\", \"log_path\": \"~/runs/cost-verify-agent-rl/8b_cell_c_episode.log\", \"submitted_at\": \"2026-05-19T11:19:34.673Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen3-8B-SFT (checkpoint-231)\", \"data_path\": \"ALFWorld train 140 games\", \"data_count\": 140, \"seed\": 42, \"checkpoint_source\": \"7b_sft_v1\", \"eval_data\": \"ALFWorld train 140 + val 32 (in-training eval)\", \"hyperparams\": {\"lr\": 5e-07, \"context_window_mode\": \"episode_level\", \"total_training_steps\": 30, \"n_gpus\": 4, \"gradient_checkpointing\": true, \"optimizer_offload\": true, \"enable_think\": false, \"save_freq\": 999}, \"wall_clock_seconds\": 1394.0, \"gpu_hours\": 1.55}, \"reproduce\": {\"finished_at\": \"2026-05-19T11:42:46.841Z\"}, \"failure_reason\": \"CUDA OOM: CUDA out of memory. Tried to allocate 8.76 GiB. GPU 0 has a total capacity of 94.97 GiB of which 4.94 GiB is free. Including non-PyTorch memory, this process has 89.98 GiB memory in use. Of the allocated memory 118.48 GiB is allocated by PyTorch, wit\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-19T11:42:48.678Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T11:42:51.496326+00:00\"}]}, \"notes\": \"OOM at backward(): full context avg 1464 tokens (~2.6x longer than h=2) exceeded 96GB. Fix: ppo_max_token_len_per_gpu 32768→16384 + PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True. Retrying as 8b_cell_c_episode_v2.\"}, \"8b_sft_clean_eval_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T11:18:59.182Z\", \"updated_at\": \"2026-05-19T11:24:37.814Z\", \"hypothesis\": \"8B SFT checkpoint full-context eval on 32 in-dist val tasks. Provides clean comparison baseline: current 80.6% is OOD 134 tasks, need full-context in-dist number to quantify information loss from h=2 windowing on the SAME eval set (Cell A used 32 in-dist). Required for paper: cannot claim \\\"52pp loss\\\" when comparing different eval sets.\", \"parent\": \"7b_sft_v1\", \"spec\": {\"command\": \"bash -c '... && cd /root/cost-verify-agent-rl/RAGEN && python train.py --config-name _alfworld_8b_sft_clean_eval'\", \"server\": \"bjb1-17606\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"model_name\": \"Qwen3-8B-SFT (checkpoint-231)\", \"data_path\": \"ALFWorld val 32 in-dist tasks\", \"data_count\": 32, \"seed\": 42, \"checkpoint_source\": \"7b_sft_v1\", \"eval_data\": \"ALFWorld val 32 in-dist (full context)\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.71875, \"num_actions\": 23.4375, \"action_is_effective\": 1, \"action_is_valid\": 0.9595, \"pass@1\": 0.71875, \"response_length\": 1731, \"reward_mean@32\": 7.1875, \"reward_std@32\": 4.496, \"best@32_mean\": 10, \"worst@32_mean\": 0, \"eval_episodes\": 32, \"eval_split\": \"eval_in_distribution\", \"eval_context\": \"full\"}, \"log_path\": \"~/runs/cost-verify-agent-rl/8b_sft_clean_eval.log\", \"checkpoint_path\": \"N/A (eval-only)\", \"completed_at\": \"2026-05-19T11:24:08.493Z\", \"notes\": \"8B SFT full-context in-dist eval: 71.875% success (23/32 tasks). Key comparison: Cell A h=2 in-dist val_before_train = 28.1% → information loss from h=2 windowing = 43.7pp on same eval set. OOD (134 tasks) = 80.6%. W&B: h4cupinr. PID was 149409 on bjb1.\"}, \"7b_cell_a_h2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T07:48:29.054Z\", \"updated_at\": \"2026-05-19T11:24:24.790Z\", \"hypothesis\": \"7B (Qwen3-8B) Cell A: step-independent RL with h=2 from 80.6% SFT baseline. Tests whether information loss + sign misattribution mechanisms are scale-invariant. At 1.7B, Cell A collapsed to 0%/3.73%. If 8B Cell A also degrades (drop to &lt;70% or training instability/collapse), confirms the mechanisms are fundamental to step-independent RL regardless of model capacity. Core comparison: Cell A degradation vs Cell C stability, direction should match 1.7B findings. lr=5e-7 (conservative, strong baseline).\", \"parent\": \"7b_sft_v1\", \"spec\": {\"command\": \"python train.py --config-name _alfworld_8b_cell_a\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\", \"cuda:1\", \"cuda:2\", \"cuda:3\"], \"pid\": 849089, \"log_path\": \"~/runs/cost-verify-agent-rl/7b_cell_a_h2.log\", \"submitted_at\": \"2026-05-19T08:01:29.531Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen3-8B-SFT (checkpoint-231)\", \"data_path\": \"ALFWorld train 140 games\", \"data_count\": 140, \"seed\": 42, \"checkpoint_source\": \"7b_sft_v1\", \"eval_data\": \"ALFWorld train 140 + val 32 (in-training eval)\", \"wandb_run\": \"irxgmlm2\", \"hyperparams\": {\"lr\": 5e-07, \"h\": 2, \"context_window_mode\": \"step_independent\", \"total_training_steps\": 15, \"n_gpus\": 4, \"gradient_checkpointing\": true, \"optimizer_offload\": true, \"enable_think\": false}, \"wall_clock_seconds\": 11694.4, \"gpu_hours\": 12.99}, \"notes\": \"D085: killed at step 2. Q4 confirmed (complete collapse). Step 1: train=12.5%, entropy=0.115 (collapse), KL=1.917. Step 2: train=1.56%, entropy=0.605 (rebound from collapse), KL=-1.885 (negative, policy pushed away from own behavior). Entropy collapse→rebound + negative KL = sign misattribution destruction mechanism. If 1.7B shows same pattern → scale-invariant evidence for paper.\", \"metrics\": {\"val_before_train_success\": 0.281, \"step1_train_success\": 0.125, \"step1_kl\": 1.917, \"step1_entropy\": 0.115, \"step1_grad_norm\": 2.29, \"step1_num_actions\": 47.7, \"step1_pass_at_8\": 0.5, \"step1_pg_clipfrac\": 0.109, \"step1_response_length\": 567.5, \"step1_duration_sec\": 5076, \"step2_train_success\": 0.015625, \"step2_entropy\": 0.605, \"step2_ppo_kl\": -1.885, \"step2_num_actions\": 49.7, \"collapse_pattern\": \"Q4 confirmed: step 0 val=28.1% → step 1 train=12.5% (entropy collapse 0.115) → step 2 train=1.56% (entropy rebound 0.605, negative KL -1.885). Complete collapse in 2 steps.\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-19T11:16:23.905Z\"}, \"8b_sft_clean_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T10:07:58.491Z\", \"updated_at\": \"2026-05-19T11:16:10.623Z\", \"hypothesis\": \"8B SFT checkpoint full-context eval on 32 in-dist val tasks. Provides clean comparison baseline: current 80.6% is OOD 134 tasks, 28.1% is in-dist 32 tasks with h=2 windowing. Need full-context in-dist number to quantify information loss from h=2 windowing on the SAME eval set. Required for paper: cannot write \\\"52pp loss\\\" when comparing different eval sets.\", \"parent\": \"7b_sft_v1\", \"spec\": {\"command\": \"bash -c 'export TMPDIR=/root/autodl-tmp/tmp && mkdir -p /root/autodl-tmp/tmp && export RAY_TMPDIR=/root/autodl-tmp/ray_tmp && mkdir -p /root/autodl-tmp/ray_tmp && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/cost-verify-agent-rl/RAGEN && python train.py --config-name _alfworld_8b_sft_clean_eval'\", \"server\": \"bjb1-17606\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"146168\", \"log_path\": \"~/runs/cost-verify-agent-rl/8b_sft_clean_eval.log\", \"submitted_at\": \"2026-05-19T11:16:10.400Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T10:41:32.774Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-19T10:41:34.291Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T10:41:37.189538+00:00\"}]}}, \"exp029_seed2_ood_reeval_v4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T07:39:29.323Z\", \"updated_at\": \"2026-05-19T10:35:20.219Z\", \"hypothesis\": \"Evaluate exp029_seed2 step 30 checkpoint (val peak 31.25%) on 134 OOD tasks (valid_unseen) for cross-seed OOD comparison. Paper table requires seed2 OOD number (seed1=23.88%). Previous v1/v2/v3 all crashed due to root partition overflow (M017), now fixed with TMPDIR redirect.\", \"parent\": \"exp029_seed2_westd_resume\", \"spec\": {\"command\": \"bash -c \\\"export TMPDIR=/root/autodl-tmp/tmp && mkdir -p $TMPDIR && export RAY_TMPDIR=/root/autodl-tmp/ray_tmp && mkdir -p $RAY_TMPDIR && export TMUX_TMPDIR=/root/autodl-tmp/tmux && mkdir -p $TMUX_TMPDIR && export WANDB_DIR=/root/autodl-tmp/wandb && export WANDB_TMPDIR=/root/autodl-tmp/tmp && export WANDB_PROJECT=cost-verify-agent-rl && export CUDA_VISIBLE_DEVICES=0,1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/cost-verify-agent-rl/RAGEN && python -m verl.trainer.main_ppo --config-path /root/autodl-tmp/cost-verify-agent-rl/RAGEN/config --config-name _alfworld_exp029_seed2_reeval_ood_v4\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"828607\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp029_seed2_ood_reeval_v4.log\", \"submitted_at\": \"2026-05-19T07:46:33.081Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 8413.6, \"gpu_hours\": 4.67}, \"notes\": \"D084: westd 上 exp029-seed2/ checkpoint (62G) 在磁盘清理时被删除。bjb1 上只有 global_step_15（原始训练崩溃点），无 global_step_30。OOD eval 阻塞。\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-19T10:06:46.679Z\"}, \"hsweep_h20_seed1\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-18T18:04:42.684Z\", \"updated_at\": \"2026-05-19T10:33:39.352Z\", \"hypothesis\": \"h=20 with step_independent generation provides 20-step observation windows. Key data point for fig5 cliff figure: with h=10 and h=5 both collapsing, h=20 tests whether 20 steps of context is sufficient for recovery. If h=20 recovers (val > 0% at step 5+), the cliff is between h=10 and h=20. If still collapsed, the minimum viable context window is larger than 20 steps.\", \"parent\": \"hsweep_h10_seed1\", \"reproduce\": {\"finished_at\": \"2026-05-18T18:38:42.494Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-18T18:38:43.732Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T18:38:46.246660+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"诊断中: worker_diagnose_hsweep_h20_seed1_20260518T184044 正在 SSH 深查失败原因。日志尾部无 Traceback，疑似系统级 kill (OOM/磁盘)。\"}}, \"notes\": \"D084 确认: 只需 step 5 val 数据做 cliff figure (in-dist val success vs h-value), 不需要 checkpoint, 不做 h=20 OOD eval。Step 5 val 出来后立即 kill, 释放 bjb1 GPU 给 exp029_seed2 OOD eval + 8b_sft_clean_eval。\", \"spec\": {\"command\": \"source /root/miniconda3/bin/activate && cd /root/cost-verify-agent-rl/RAGEN && export RAY_OBJECT_STORE_MEMORY=16000000000 && PYTHONUNBUFFERED=1 python train.py --config-name _alfworld_hsweep_h20 seed.train=10000 trainer.experiment_name=hsweep-h20-seed1\", \"server\": \"bjb1-17606\", \"gpu\": \"0,1\", \"pid\": 77613, \"log_path\": \"/root/runs/cost-verify-agent-rl/hsweep_h20_seed1.log\", \"submitted_at\": \"2026-05-18T19:10:38.966Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wandb_run_id\": \"qi8g4f86\", \"data_path\": \"ALFWorld\", \"data_count\": 3553, \"model_name\": \"Qwen3-1.7B (SFT v4)\", \"seed\": 10000, \"checkpoint_source\": \"qwen3_exp021_ragen_sft_v4\", \"eval_data\": \"ALFWorld val 32 tasks\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/hsweep-h20/\", \"hyperparams\": {\"total_training_steps\": 15, \"h\": 20, \"max_actor_ckpt_to_keep\": 3, \"val_before_train\": false, \"optimizer_offload\": false, \"ray_object_store_memory\": \"16GB\"}, \"wall_clock_seconds\": 55380.4, \"gpu_hours\": 15.38}, \"metrics\": {\"step1_train\": 0.203, \"step2_train\": 0.133, \"step4_train\": 0.281, \"val_step5_success\": 0.15625}, \"conclusion\": \"success\"}, \"7b_sft_eval_ood\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T07:39:26.088Z\", \"updated_at\": \"2026-05-19T07:43:55.586Z\", \"hypothesis\": \"Evaluate Qwen3-8B SFT checkpoint (7b_sft_v1, loss=0.0355, acc=98.56%) on ALFWorld OOD 134 tasks. Establishes 8B SFT baseline for subsequent RL experiments (Cell A vs Cell C). If success rate significantly higher than 1.7B SFT baseline (~6.25%), confirms model scale advantage for SFT; if similar, the 1.7B findings generalize.\", \"parent\": \"7b_sft_v1\", \"spec\": {\"command\": \"RAGEN eval val_only=true on ALFWorld OOD 134 tasks, Qwen3-8B SFT checkpoint-231\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:2\", \"cuda:3\"], \"model_name\": \"Qwen3-8B-SFT (checkpoint-231)\", \"data_path\": \"ALFWorld valid_unseen 134 tasks\", \"data_count\": 134, \"seed\": 42, \"checkpoint_source\": \"7b_sft_v1\", \"eval_data\": \"ALFWorld valid_unseen OOD 134 tasks\", \"wandb_run\": \"8v6iysv3\", \"pid\": 807986, \"log_path\": \"/root/autodl-tmp/logs/7b_sft_eval_ood.log\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.806, \"pass_at_1\": 0.806, \"num_actions\": 20.18, \"action_is_valid\": 0.963, \"action_is_effective\": 1, \"reward_mean_at_134\": 8.06, \"response_length\": 1987.9, \"best_at_2_mean\": 9.53, \"best_at_4_mean\": 9.98, \"best_at_8_mean\": 10, \"worst_at_2_mean\": 6.55, \"worst_at_4_mean\": 4.11, \"worst_at_8_mean\": 1.93}, \"notes\": \"Eval completed successfully. OOD 134 tasks success rate 80.6%. W&B data missing due to BrokenPipeError during wandb teardown (asyncio stream close), but all metrics logged to file. GPU cuda:2,3 released.\", \"checkpoint_path\": \"N/A (eval-only, source checkpoint from 7b_sft_v1)\", \"completed_at\": \"2026-05-19T07:43:55.586Z\"}, \"7b_sft_v1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T06:09:08.447Z\", \"updated_at\": \"2026-05-19T07:38:58.545Z\", \"hypothesis\": \"SFT Qwen3-8B on ALFWorld expert data (2460 examples) to create 8B SFT checkpoint for subsequent RL training (Cell A vs C). Also tests westd stability with non-Ray workload (torchrun). SFT is mandatory for fair comparison with 1.7B experiments (same pipeline: base → SFT → RL).\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0,1,2,3 torchrun --nproc_per_node=4 scripts/sft_train_8b.py\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\", \"cuda:1\", \"cuda:2\", \"cuda:3\"], \"model_name\": \"Qwen3-8B\", \"data_path\": \"/root/autodl-tmp/expert_sft/expert_sft_train.jsonl\", \"data_count\": 2460, \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/qwen3_8b_sft_v1\", \"log_path\": \"/root/autodl-tmp/sft_8b.log\", \"hyperparams\": {\"lr\": 1e-05, \"epochs\": 3, \"per_device_batch\": 2, \"grad_accum\": 4, \"max_seq\": 4096, \"total_steps\": 231, \"fsdp\": \"full_shard\", \"bf16\": true}}, \"conclusion\": \"success\", \"notes\": \"Final: loss=0.0355, token_accuracy=98.56%, 231/231 steps, 3 epochs. FSDP full_shard 4xRTX PRO 6000. DDP OOM → FSDP resolved. TMPDIR fix (M017) prevented root partition overflow. Checkpoint saving 7 shards to /root/autodl-tmp/checkpoints/qwen3_8b_sft_v1/.\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/qwen3_8b_sft_v1/\", \"log_path\": \"/root/autodl-tmp/checkpoints/qwen3_8b_sft_v1/training.log\", \"completed_at\": \"2026-05-19T07:38:58.545Z\"}, \"7b_zeroshot_eval_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:43:38.265Z\", \"updated_at\": \"2026-05-19T06:05:28.518Z\", \"hypothesis\": \"Zero-shot evaluation of Qwen3-8B on ALFWorld OOD 134 tasks. If success rate > 30%, can skip SFT and go directly to RL. If < 10%, SFT is mandatory. Establishes 8B baseline for model-agnostic claim.\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/cost-verify-agent-rl/RAGEN && CUDA_VISIBLE_DEVICES=2,3 python train.py --config-name _alfworld_7b_zeroshot_eval\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:2\", \"cuda:3\"], \"pid\": \"790377\", \"wandb_run_id\": \"w56o6f11\", \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"data_path\": \"AlfworldSG_OOD (eval_out_of_distribution)\", \"data_count\": 134, \"eval_data\": \"alfworld_valid_unseen_134\", \"log_path\": \"/root/runs/cost-verify-agent-rl/7b_zeroshot_eval_v2.log\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-19T06:05:20.447Z\", \"failure_reason\": \"Process died on westd (2nd crash). Same pattern as OOD eval: all tmux sessions gone, all processes dead, system healthy. Suspected container restart. Moving to bjb1 per Director instruction.\"}, \"exp029_seed2_ood_reeval_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:22:37.809Z\", \"updated_at\": \"2026-05-19T06:05:27.014Z\", \"hypothesis\": \"Retry of exp029_seed2_ood_reeval (crashed twice). Evaluate exp029_seed2 step 30 checkpoint (val peak 31.25%) on 134 OOD tasks (valid_unseen) for cross-seed OOD comparison. Paper table requires seed2 OOD number (seed1=23.88%).\", \"parent\": \"exp029_seed2_ood_reeval\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/cost-verify-agent-rl/RAGEN && CUDA_VISIBLE_DEVICES=0,1 python train.py --config-name _alfworld_exp029_seed2_reeval_ood\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"786931\", \"wandb_run_id\": \"ypt94m3v\", \"model_name\": \"Qwen3-1.7B (SFT v4)\", \"seed\": 43, \"data_path\": \"AlfworldSG_OOD (eval_out_of_distribution)\", \"data_count\": 134, \"checkpoint_source\": \"exp029_seed2_westd_resume global_step_30\", \"eval_data\": \"alfworld_valid_unseen_134\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/exp029-seed2/global_step_30/\", \"log_path\": \"/root/autodl-tmp/exp029_seed2_ood_v3.log\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-19T06:05:19.664Z\", \"failure_reason\": \"Process died again on westd (4th total crash). System diagnostics show westd is healthy (memory 969Gi free, no Ray, no OOM in logs). All tmux sessions disappeared. Suspected: container restart or SSH session management issue killing all processes. Moving to bjb1 per Director instruction.\"}, \"exp029_seed2_ood_reeval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T02:38:28.552Z\", \"updated_at\": \"2026-05-19T05:02:51.662Z\", \"hypothesis\": \"Evaluate exp029_seed2 step 30 checkpoint (val peak 31.25%) on 134 OOD tasks (valid_unseen) to get cross-seed OOD comparison with seed1 (23.88%). Paper table requires both seeds.\", \"parent\": \"exp029_seed2_westd_resume\", \"spec\": {\"command\": \"python train.py --config-name _alfworld_exp029_seed2_reeval_ood\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"725711\", \"wandb_run_id\": \"l0zohzt5\", \"model_name\": \"Qwen3-1.7B (SFT v4)\", \"seed\": 43, \"data_path\": \"AlfworldSG_OOD (eval_out_of_distribution)\", \"data_count\": 134, \"checkpoint_source\": \"exp029_seed2_westd_resume global_step_30\", \"eval_data\": \"alfworld_valid_unseen_134\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/exp029-seed2/global_step_30/\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-19T05:02:46.918Z\", \"failure_reason\": \"Process crashed silently on westd cuda:0,1. No W&B metrics, no log residue. Likely killed by system or Ray conflict. Third attempt needed.\"}, \"hsweep_h10_seed1\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-17T17:30:46.964Z\", \"updated_at\": \"2026-05-19T02:45:40.356Z\", \"hypothesis\": \"h=10 with step_independent generation provides 10-step observation windows. Key data point for fig5 cliff figure: if h=10 shows recovery (val > 0%), the cliff is between h=5 and h=10. If still collapsed, cliff is between h=10 and full context (h=28).\", \"parent\": \"hsweep_h2_seed1\", \"reproduce\": {\"finished_at\": \"2026-05-18T03:09:23.490Z\"}, \"failure_reason\": \"Intentionally killed by ops worker (kill-h10-dual-reeval-restart) to free bjb1 cuda:0,1 for exp029 reeval + hsweep_h2_seed2 reeval sequence. Will be restarted after reevals complete.\", \"completed_at\": \"2026-05-18T03:09:24.711Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T03:09:28.621330+00:00\"}], \"previous_failure\": {\"conclusion\": \"killed\", \"notes\": \"Director 批准临时 kill（刚启动几分钟，无进度损失）以释放 bjb1 cuda:0,1 跑 exp029 + hsweep_h2_seed2 双 reeval。Reeval 完成后重启。原由 auto_next_hsweep.sh 自动启动，未经正式审批。\"}}, \"notes\": \"Director ordered kill: h=10 fully collapsed (train=0% from step 2, val=SFT baseline at step 5). Ray cluster占全部4 GPU（idle worker锁定cuda:0,1各40GB）。M015教训：必须显式设CUDA_VISIBLE_DEVICES。\", \"spec\": {\"command\": \"python train.py --config-name _alfworld_hsweep_h10 seed.train=10000 trainer.experiment_name=hsweep-h10-seed1\", \"server\": \"westd-47453\", \"gpu\": \"2,3\", \"pid\": 34193, \"wandb_run_id\": \"x09p5xd0\", \"data_path\": \"/root/autodl-tmp/cost-verify-agent-rl/data/alfworld\", \"data_count\": 3553, \"model_name\": \"Qwen3-1.7B (SFT v4) — registry曾误记为Qwen2.5-3B，config验证确认是Qwen3\", \"seed\": 10000, \"checkpoint_source\": \"qwen3_exp021_ragen_sft_v4\", \"eval_data\": \"ALFWorld val 32 tasks\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/hsweep-h10/\", \"log_path\": \"/root/autodl-tmp/cost-verify-agent-rl/logs/hsweep_h10_seed1.log\"}, \"conclusion\": \"killed\", \"metrics\": {\"step2_train_success\": 0, \"step5_val_success\": \"SFT_baseline\", \"collapse_onset\": \"step 2\", \"verdict\": \"complete collapse, h=10 insufficient context\"}}, \"exp029_seed2_westd_resume\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:50:04.399Z\", \"updated_at\": \"2026-05-19T02:20:31.354Z\", \"hypothesis\": \"Resume exp029_seed2 (Cell C full_context + episode-level advantage, seed=43) from step 15 on westd. Target step 40, confirm stable learning trajectory.\", \"parent\": \"exp029_episode_level_seed2\", \"conclusion\": \"killed\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export TMPDIR=/root/autodl-tmp/tmp && mkdir -p $TMPDIR && export TORCH_COMPILE_DISABLE=1 && export PYTHONUNBUFFERED=1 && export WANDB_PROJECT=cost-verify-agent-rl && export WANDB_DIR=/root/autodl-tmp/wandb && export WANDB_TMPDIR=/root/autodl-tmp/tmp && cd /root/autodl-tmp/cost-verify-agent-rl/RAGEN && CUDA_VISIBLE_DEVICES=0,1 python train.py --config-name _alfworld_exp029_episode_level_seed2'\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"414163\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp029_seed2_westd_resume.log\", \"submitted_at\": \"2026-05-18T22:58:56.941Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wandb_run_id\": \"9xs5vfbe\", \"data_path\": \"/root/autodl-tmp/cost-verify-agent-rl/data/alfworld\", \"data_count\": 3553, \"model_name\": \"Qwen3-1.7B (SFT v4)\", \"seed\": 43, \"checkpoint_source\": \"exp029_seed2_bjb1_step15 (symlinked)\", \"eval_data\": \"alfworld_valid_unseen_134\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/exp029-seed2/\", \"hyperparams\": {\"total_training_steps\": 40, \"resume_from_step\": 15, \"optimizer_offload\": false, \"max_actor_ckpt_to_keep\": 3, \"h\": \"full_context\", \"advantage\": \"episode-level\"}, \"wall_clock_seconds\": 12080.0, \"gpu_hours\": 6.71}, \"metrics\": {\"step15_val_success\": 0.25, \"step15_manager_invalid\": 0.008, \"step15_num_actions\": 40.1, \"step20_val_success\": 0.125, \"step20_manager_invalid\": 0.343, \"step25_val_success\": 0.156, \"step25_manager_invalid\": 0.51, \"step30_val_success\": 0.3125, \"step30_manager_invalid\": 0.467, \"step35_val_success\": 0.28125, \"step35_manager_invalid\": 0.591, \"step40_val_success\": 0.28125, \"step40_manager_invalid\": 0.584, \"step40_train_success\": 0.0625, \"step40_train_manager_invalid\": 0.801, \"step40_ppo_kl\": 0.1735, \"step40_grad_norm\": 8.47, \"step40_num_actions\": 8.2}, \"completed_at\": \"2026-05-19T02:20:16.905Z\"}, \"factorial_h2_episodeadv_seed2\": {\"status\": \"DONE\", \"retry_count\": 4, \"created_at\": \"2026-05-18T04:48:02.228Z\", \"updated_at\": \"2026-05-18T22:47:00.000Z\", \"conclusion\": \"success\", \"metrics\": {\"step15_train_success\": 0.555, \"step15_val_ood_success\": 0.0075, \"step15_val_ood_action_valid\": 0.173, \"step15_kl\": 0.618, \"step15_train_pass8\": 0.875}, \"completed_at\": \"2026-05-18T10:52:19.155Z\", \"hypothesis\": \"Replicate factorial experiment (step-independent + episode-level advantage) with different seed to confirm that sign misattribution elimination is robust, not single-seed artifact. Same config, different seed, 15 steps.\", \"parent\": \"factorial_h2_episodeadv_seed1\", \"failure_reason\": \"Worker 546362 (TaskRunner) 在 val_before_train 初始评估阶段被信号杀死 (SYSTEM_ERROR, connection error code 2 / EOF)。GCS 报告可能原因: OOM killer / SIGSEGV。134 个 ALFWorld eval 环境并行启动约 12 分钟后进程崩溃，无 Python traceback。0/15 训练步完成，无 checkpoint。\", \"reproduce\": {\"finished_at\": \"2026-05-18T10:52:18.239Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T10:52:21.813105+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"cd /root/autodl-tmp/cost-verify-agent-rl/RAGEN && TMPDIR=/root/autodl-tmp/tmp TORCH_COMPILE_DISABLE=1 PYTHONUNBUFFERED=1 CUDA_VISIBLE_DEVICES=0,1 python train.py --config-name _alfworld_factorial_h2_episode_adv_seed2\", \"server\": \"westd-47453\", \"gpu\": \"0,1\", \"pid\": \"576727\", \"wandb_run_id\": \"6rqnrlr7\", \"data_path\": \"/root/autodl-tmp/cost-verify-agent-rl/data/alfworld\", \"data_count\": 3553, \"model_name\": \"Qwen3-1.7B (SFT v4)\", \"seed\": 43, \"checkpoint_source\": \"qwen3_exp021_ragen_sft_v4\", \"eval_data\": \"alfworld_valid_unseen_134\", \"log_path\": \"/root/autodl-tmp/cost-verify-agent-rl/logs/factorial_seed2_v4.log\", \"val_before_train\": false, \"retry_v4\": true}}, \"exp029_episode_level_seed2\": {\"status\": \"DONE\", \"retry_count\": 3, \"created_at\": \"2026-05-18T04:48:01.826Z\", \"updated_at\": \"2026-05-18T18:25:16.249Z\", \"hypothesis\": \"Replicate exp029 episode-level result (23.88% OOD) with different seed to confirm statistical robustness. P0 priority: core positive claim built on single seed is desk-reject risk. Same SFT checkpoint, same config, seed=43, 15 steps, AlfworldSG_OOD 134 tasks eval.\", \"parent\": \"exp029_episode_level\", \"reproduce\": {\"finished_at\": \"2026-05-18T17:27:12.433Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-18T05:41:19.165Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T05:41:22.770723+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T06:18:18.594301+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T07:41:53.887922+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T09:53:02.637445+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T10:29:27.034216+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T15:00:41.979643+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T15:20:52.909936+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T17:27:16.338465+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"cd /root/cost-verify-agent-rl/RAGEN && CUDA_VISIBLE_DEVICES=0,1 python train.py --config-name _alfworld_exp029_episode_level_seed2\", \"server\": \"bjb1-17606\", \"gpu\": \"cuda:0,1\", \"pid\": 66897, \"wandb_run_id\": \"25d60jf4\", \"data_path\": \"ALFWorld\", \"data_count\": 134, \"model_name\": \"Qwen3-1.7B (SFT v4 checkpoint)\", \"seed\": 43, \"checkpoint_source\": \"exp021_ragen_sft_v4\", \"eval_data\": \"AlfworldSG_OOD 134 tasks\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/exp029-seed2/\", \"log_path\": \"/root/runs/cost-verify-agent-rl/exp029_seed2_resume_step15.log\", \"hyperparams\": {\"total_training_steps\": 100, \"enable_gradient_checkpointing\": true, \"ppo_mini_batch_size\": 8, \"ppo_max_token_len_per_gpu\": 16384, \"env_groups\": 8, \"group_size\": 8, \"optimizer_offload\": false, \"max_actor_ckpt_to_keep\": 3}, \"notes\": \"Resume from step 15 after disk full crash. step_25 corrupted (truncated optimizer files). Deleted step_5/10/20/25 ckpts. max_actor_ckpt_to_keep=3. optimizer_offload=false. Using conda base env.\"}, \"conclusion\": \"killed\", \"notes\": \"Director 止损 kill。bjb1 累计 10+ 次失败。step 15 val=21.875% (32 tasks)，数据保留在 /root/autodl-tmp/checkpoints/exp029-seed2/。计划转移到 westd cuda:0,1 继续（factorial 完成后）。\"}, \"gsweep_g100_h5_seed1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T13:56:58.033Z\", \"updated_at\": \"2026-05-18T17:36:39.529Z\", \"hypothesis\": \"γ=1.0 (no discount) tests whether collapse in h=5 is caused by sign misattribution from magnitude decay. If γ=1.0 also collapses, sign misattribution is not solely from discount-induced magnitude decay.\", \"parent\": \"gsweep_g095_h5_seed1\", \"spec\": {\"command\": \"python train.py --config-name _alfworld_gamma_sweep_g100_h5\", \"server\": \"westd-47453\", \"gpu\": \"2,3\", \"pid\": \"714093\", \"wandb_run_id\": \"da7701tk\", \"data_path\": \"/root/autodl-tmp/cost-verify-agent-rl/data/alfworld\", \"data_count\": 3553, \"model_name\": \"Qwen/Qwen2.5-3B\", \"seed\": 10000, \"checkpoint_source\": \"Qwen2.5-3B base\", \"eval_data\": \"ALFWorld val 32 tasks\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/gsweep-g100-h5/\", \"log_path\": \"/root/autodl-tmp/cost-verify-agent-rl/logs/gsweep_g100_seed1.log\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-18T17:35:40.356Z\", \"metrics\": {\"conclusion_reason\": \"collapsed, γ=1.0 also collapses confirming sign misattribution not solely from magnitude decay\"}}, \"gsweep_g095_h5_seed1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T13:56:55.994Z\", \"updated_at\": \"2026-05-18T13:11:09.941Z\", \"hypothesis\": \"γ=0.95 with h=5 is the control condition matching hsweep_h5. Early windows retain γ^9 ≈ 0.95^9 ≈ 63% of terminal return. Expected to reproduce h5 behavior from h-sweep.\", \"parent\": \"hsweep_h2_seed1\", \"spec\": {\"command\": \"bash launch_gsweep.sh g095 \\\"2,3\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:2\", \"cuda:3\"], \"pid\": 416289, \"data_path\": \"ALFWorld\", \"data_count\": \"134 train tasks\", \"model_name\": \"Qwen3-1.7B\", \"seed\": 10000, \"wandb_run_id\": \"d3irreww\", \"checkpoint_source\": \"Qwen3-1.7B base\", \"eval_data\": \"ALFWorld val 32 tasks\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/gsweep-g095-h5-seed1/\", \"log_path\": \"/root/autodl-tmp/cost-verify-agent-rl/RAGEN/outputs/\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-18T13:09:34.521Z\", \"metrics\": {\"val_success_step5\": 0, \"conclusion_reason\": \"collapsed at step 5, val=0%\"}}, \"factorial_h2_episodeadv_seed1\": {\"status\": \"DONE\", \"retry_count\": 2, \"created_at\": \"2026-05-17T18:17:23.327Z\", \"updated_at\": \"2026-05-18T10:22:36.071Z\", \"hypothesis\": \"Step_independent generation (h=2) with episode-level advantage eliminates sign misattribution while preserving truncated-context inference. If success >> h=2 step-level (0%), information loss alone does not cause collapse — sign misattribution is the primary driver. If success ≈ 0%, information loss is sufficient to cause collapse regardless of advantage computation. This is the key factorial experiment separating the two mechanisms.\", \"parent\": \"hsweep_h2_seed1\", \"server\": \"westd-47453\", \"gpu\": \"cuda:0,cuda:1\", \"reproduce\": {\"command\": \"bash -c \\\"export TORCH_COMPILE_DISABLE=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/cost-verify-agent-rl/RAGEN && ALFWORLD_DATA=/root/autodl-tmp/alfworld CUDA_VISIBLE_DEVICES=0,1 python train.py --config-name _alfworld_factorial_h2_episode_adv\\\"\", \"finished_at\": \"2026-05-18T10:16:37.005Z\"}, \"failure_reason\": \"False positive: W&B atexit BrokenPipeError during cleanup. Training completed all 15/15 steps normally.\", \"completed_at\": \"2026-05-17T19:23:42.236Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T19:23:44.970401+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T20:06:00.076942+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T10:16:44.344646+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"bash -c \\\"export TMPDIR=/root/autodl-tmp/tmp && mkdir -p $TMPDIR && export TORCH_COMPILE_DISABLE=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/cost-verify-agent-rl/RAGEN && ALFWORLD_DATA=/root/autodl-tmp/alfworld CUDA_VISIBLE_DEVICES=0,1 python train.py --config-name _alfworld_factorial_h2_episode_adv\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": 475745, \"wandb_run_id\": \"jsrvwcfd\", \"model_name\": \"Qwen3-1.7B-SFT (exp021)\", \"seed\": 42, \"data_path\": \"ALFWorld valid_unseen\", \"data_count\": \"3553 train + 134 OOD eval\", \"log_path\": \"~/runs/cost-verify-agent-rl/factorial_h2_episodeadv_seed1.log\", \"env\": \"TMPDIR=/root/autodl-tmp/tmp TORCH_COMPILE_DISABLE=1\", \"checkpoint_source\": \"Qwen3-1.7B-SFT exp021\", \"eval_data\": \"ALFWorld valid_unseen 134 tasks (OOD)\"}, \"metrics\": {\"completed_steps\": \"15/15\", \"wandb_run_id\": \"6liw7fm1\", \"val_step5\": {\"success\": 0.0597, \"dataset\": \"AlfworldOOD_134tasks\"}, \"val_step15\": {\"success\": 0.0075}, \"kl_loss_trajectory\": {\"step1\": 0.238, \"step5\": 0.735, \"step10\": 1.029, \"step15\": 2.845}, \"ppo_kl_range\": \"0.025-0.096\", \"best_checkpoint\": \"global_step_5\", \"best_val_success\": 0.0597, \"train_step1\": {\"success\": 0.203, \"pass_at_8\": 0.688}, \"train_step6\": {\"success\": 0.258, \"pass_at_8\": 0.813}, \"checkpoint_paths\": {\"step5\": \"/root/autodl-tmp/checkpoints/factorial-h2-episode-adv/global_step_5/\", \"step10\": \"/root/autodl-tmp/checkpoints/factorial-h2-episode-adv/global_step_10/\", \"step15\": \"/root/autodl-tmp/checkpoints/factorial-h2-episode-adv/global_step_15/\"}, \"exit_cause\": \"W&B atexit BrokenPipeError (false positive)\", \"kl_issue\": \"kl_loss_coef=0.01 too low, policy drifted after step 5\", \"status_note\": \"COMPLETED. Best val OOD 5.97% at step 5. Degraded to 0.75% by step 15 due to KL drift. Sign misattribution elimination confirmed: 5.97% vs 0% (step-level h=2).\"}, \"notes\": \"W&B 深度分析确认：sign misattribution 是 collapse 的 primary driver。关键证据：step 3→4 hsweep action_valid 91.3%→43.1% (catastrophic collapse) vs factorial 保�� 79-85% (无崩溃)。V-shaped recovery (20.3%→3.1%→15.63%) 是探索期波动非不可逆退化。3-cell 贡献：sign misattribution ~6pp (0%→5.97% val), information loss ~22pp (5.97%→28.1% val)。Sign misattribution pp 贡献较小但是 catastrophic collapse 的质变 trigger。\", \"conclusion\": \"success\"}, \"gsweep_g080_h5_seed1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T13:56:53.634Z\", \"updated_at\": \"2026-05-18T09:35:23.404Z\", \"hypothesis\": \"γ=0.8 with h=5 represents an intermediate decay rate where early windows retain γ^9 ≈ 0.8^9 ≈ 13% of terminal return, potentially showing delayed but still present collapse compared to γ=0.95 (39%).\", \"parent\": \"hsweep_h2_seed1\", \"spec\": {\"command\": \"python train.py --config-name _alfworld_gamma_sweep_g080_h5 seed.train=10000 trainer.experiment_name=gsweep-g080-h5-seed1\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:2\", \"cuda:3\"], \"pid\": 955007, \"model_name\": \"Qwen3-1.7B\", \"seed\": 10000, \"data_path\": \"ALFWorld\", \"data_count\": \"134 train tasks\", \"log_path\": \"~/runs/cost-verify-agent-rl/gsweep_g080_h5_seed1.log\", \"env\": \"TORCH_COMPILE_DISABLE=1\", \"checkpoint_source\": \"Qwen3-1.7B base\", \"eval_data\": \"ALFWorld val 32 tasks\"}, \"metrics\": {\"step5_val_success\": \"3.125%\", \"step5_entropy\": 0.185, \"subsequent_steps\": \"all 0%\", \"conclusion_note\": \"Complete collapse confirmed. γ=0.80 with h=5 shows catastrophic failure — killed early by Director as no new information expected. Supports hypothesis that lower gamma accelerates collapse.\"}, \"reproduce\": {\"finished_at\": \"2026-05-18T09:21:28.503Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-18T09:21:28.848Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T09:21:35.022554+00:00\"}]}}, \"hsweep_h2_seed2_reeval_ood\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T04:12:03.656Z\", \"updated_at\": \"2026-05-18T05:13:33.875Z\", \"hypothesis\": \"Evaluate hsweep_h2_seed2 checkpoint (step 15) on OOD 134 tasks to get comparable metric with exp029 reeval (23.88%). If val success remains low (~9% in-distribution), confirms collapse is real even with late recovery.\", \"parent\": \"hsweep_h2_seed2\", \"spec\": {\"command\": \"python train.py --config-name _alfworld_hsweep_h2_seed2_reeval_ood\", \"server\": \"bjb1-17606\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"model_name\": \"Qwen3-1.7B (hsweep-h2 step 15, seed2)\", \"data_path\": \"ALFWorld valid_unseen\", \"data_count\": \"134 OOD tasks\", \"seed\": 10001, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/hsweep-h2/global_step_15\", \"eval_data\": \"AlfworldSG_OOD 134 tasks\", \"log_path\": \"/root/runs/cost-verify-agent-rl/hsweep-h2-seed2-reeval-ood.log\", \"checkpoint_path\": \"N/A (eval only)\"}, \"metrics\": {\"success\": 0.0373, \"action_is_valid\": 0.994, \"action_is_effective\": 1, \"pass_at_1\": 0.0373, \"num_actions\": 48.53, \"response_length\": 8501, \"dataset\": \"AlfworldSG_OOD_134tasks\", \"date\": \"2026-05-18\", \"note\": \"Valid actions (99.4%) but cannot complete tasks - generates long ineffective sequences\"}, \"conclusion\": \"success\", \"reproduce\": {\"finished_at\": \"2026-05-18T05:09:58.763Z\"}, \"failure_reason\": \"N/A - completed successfully. OOD success=3.73%. Process exit was expected (eval-only run).\", \"completed_at\": \"2026-05-18T05:09:59.965Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T05:10:04.087054+00:00\"}]}}, \"exp029_episode_level\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T08:49:53.280Z\", \"updated_at\": \"2026-05-18T04:11:39.305Z\", \"hypothesis\": \"Episode-level 训练（context_window_mode: full）解决 step_independent h=2 的信用分配缺陷，模型能学到跨步规划策略，val success 不再停滞于 baseline。\", \"parent\": \"exp028c_selfguide_recipe\", \"notes\": \"Director 决策 early-stop at step 15（val success 28.125%, pass@8=92.9%）释放 GPU 给 h-sweep。MVP 已通过（step 5 val=25%, 2x baseline）。Episode-level 训练假设确认：从 12.5% baseline 提升到 28.125%，而 step-independent 崩塌到 0%。Checkpoint: global_step_15。\", \"server\": \"bjb1-17606\", \"gpu\": \"cuda:0,cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-17606\", \"gpu\": \"cuda:0,cuda:1\", \"started_at\": \"2026-05-16T09:49:15.902Z\", \"finished_at\": \"2026-05-16T19:20:32.435Z\", \"training_hours\": 9.52}, \"failure_reason\": null, \"completed_at\": null, \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T16:10:47.902736+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T18:24:49.059842+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T19:09:41.491953+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T19:20:35.794556+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"metrics\": {\"step_0_val\": {\"success\": 12.5, \"pass_at_1\": 12.5, \"action_is_valid\": 78.3, \"episodes\": 32, \"note\": \"当前 run (W&B 6d4oml60) val_before_train\"}, \"step_1_train\": {\"success\": 17.97, \"pass_at_8\": 56.25, \"action_is_valid\": 68.24, \"action_is_effective\": 99.47, \"num_actions\": 42.03, \"entropy\": 0.02775, \"kl_loss\": 0.000915, \"pg_loss\": -4.59e-05, \"grad_norm\": 1.267, \"score_mean\": 1.797, \"response_length\": 7112, \"response_length_max\": 16381, \"time_s\": 1810, \"note\": \"当前 run。success 17.97% > baseline 12.5%。entropy/grad_norm 正常（full mode token-mean 量纲）\"}}, \"notes\": \"当前运行: PID 889859, W&B 6d4oml60。正确日志: /root/autodl-tmp/exp029_restart.log。Step 1 完成(30m10s/step)，step 2 进行中。TMPDIR=/root/autodl-tmp/tmp, WANDB_DIR=/root/autodl-tmp/wandb。val env_groups=32。ETA 全部 100 steps ≈ 50h。\"}}, \"conclusion\": \"success\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export TMPDIR=/root/autodl-tmp/tmp && export WANDB_DIR=/root/autodl-tmp/wandb && export WANDB_TMPDIR=/root/autodl-tmp/tmp && cd /root/cost-verify-agent-rl/RAGEN && python train.py --config-name _alfworld_exp029_episode_level\\\"\", \"server\": \"bjb1-17606\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"902342\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp029_episode_level.log\", \"submitted_at\": \"2026-05-16T20:12:30.835Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/exp029/global_step_15/actor/huggingface\", \"wall_clock_seconds\": 30261.8, \"gpu_hours\": 16.81}, \"metrics\": {\"reeval_ood_134tasks\": {\"success\": 0.2388, \"action_is_valid\": 0.5683, \"action_is_effective\": 0.916, \"manager_invalid_action\": 0.0839, \"reward_mean\": 2.388, \"best_at_8\": 8.88, \"dataset\": \"AlfworldSG_OOD_134tasks\", \"date\": \"2026-05-18\"}}}, \"gsweep_g050_h5_seed1\": {\"status\": \"DONE\", \"retry_count\": 2, \"created_at\": \"2026-05-17T13:56:51.277Z\", \"updated_at\": \"2026-05-18T02:56:21.234Z\", \"hypothesis\": \"γ=0.5 with h=5 will show accelerated collapse compared to default γ=0.95, because γ^k decay compounds: early windows receive only γ^(N-1) ≈ 0.5^9 ≈ 0.2% of terminal return, making sign misattribution maximally severe.\", \"parent\": \"hsweep_h2_seed1\", \"reproduce\": {\"finished_at\": \"2026-05-18T02:55:47.955Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T14:42:45.029228+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T02:55:56.282433+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"metrics\": {\"training_steps_completed\": 0, \"wandb_run_id\": null, \"checkpoint_path\": null, \"log_path\": \"/root/runs/cost-verify-agent-rl/gsweep_g050_h5_seed1.log\", \"crash_reason\": \"AssertionError: duplicate template name in torch._inductor/select_algorithm.py — vLLM/PyTorch incompatibility during rollout module init\", \"crash_stage\": \"initialization (before any training step)\", \"collapse_onset_step\": null, \"total_training_steps\": 0, \"elapsed_hours\": 0, \"server\": \"westd-47453\", \"gpu\": \"cuda:2,3\", \"gamma\": 0.5, \"h\": 5}, \"notes\": \"Infrastructure failure: experiment crashed during vLLM rollout module initialization with 'AssertionError: duplicate template name' in torch._inductor/select_algorithm.py. This is a vLLM/PyTorch version incompatibility on westd-47453. Zero training steps completed, no W&B data, no checkpoint. Hypothesis (γ=0.5 accelerates collapse vs γ=0.95) was never tested. Needs environment fix (likely vLLM or PyTorch version mismatch) before retry.\"}}, \"completed_at\": \"2026-05-17T14:44:36.785Z\", \"notes\": \"Director 批准 early kill (step 12/15)。Hypothesis 完全确认：γ=0.5 加速 collapse，从 step 1 起 train success 基本为 0%，val step 5/10 全零，KL step 8 spike 到 0.209。step 10 checkpoint 已保存。数据足够用于论文 gamma sweep figure。Watchdog 预期自动启动 g080。\", \"spec\": {\"command\": \"python train.py --config-name _alfworld_gamma_sweep_g050_h5 seed.train=10000 trainer.experiment_name=gsweep-g050-h5-seed1\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:2\", \"cuda:3\"], \"pid\": \"85798\", \"model_name\": \"Qwen3-1.7B\", \"seed\": 10000, \"data_path\": \"ALFWorld\", \"data_count\": \"134 train tasks\", \"log_path\": \"~/runs/cost-verify-agent-rl/gsweep_g050_h5_seed1.log\", \"env\": \"TORCH_COMPILE_DISABLE=1\", \"checkpoint_source\": \"Qwen3-1.7B base (not from parent checkpoint, parent field is for derivation tracking)\", \"eval_data\": \"ALFWorld val 32 tasks\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/gsweep-g050-h5/global_step_10\"}, \"metrics\": {\"current_step\": \"12/15\", \"train_success_collapsed_at\": \"step 1\", \"train_success_all_steps\": \"0-2.3% (effectively 0%)\", \"val_step0\": {\"success\": 0.094}, \"val_step5\": {\"success\": 0, \"reward\": 0}, \"val_step10\": {\"success\": 0, \"reward\": 0, \"response_length\": 1412}, \"kl_sequence\": [0.019, 0.025, 0.018, 0.014, 0.01, 0.009, 0.009, 0.209, 0.018], \"kl_spike_step8\": 0.209, \"checkpoint\": \"global_step_10\", \"eta\": \"~5h from 02:46 UTC\", \"status_note\": \"COMPLETELY COLLAPSED. Train success 0% from step 1. KL spike 20x at step 8. Val all zeros. Remaining 3 steps waste GPU. Recommend early kill.\"}, \"conclusion\": \"killed\", \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\"}, \"hsweep_h2_seed2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T14:37:14.817Z\", \"updated_at\": \"2026-05-18T02:55:38.705Z\", \"hypothesis\": \"h=2 seed 2 replicates seed 1 catastrophic collapse (step 3-4 onset, 0% by step 9+), confirming collapse is robust not single-run artifact. Additionally LOG_PER_SAMPLE_ADV=1 collects per-window advantage data for plan_004 sign misattribution empirical verification.\", \"parent\": \"hsweep_h2_seed1\", \"spec\": {\"command\": \"python train.py --config-name _alfworld_hsweep_h2 seed.train=20000 trainer.experiment_name=hsweep-h2-seed2\", \"server\": \"bjb1-17606\", \"gpu\": \"cuda:0,1\", \"pid\": 945877, \"wandb_run_id\": \"jhwyg4tc\", \"model_name\": \"Qwen3-1.7B\", \"seed\": 20000, \"data_path\": \"ALFWorld\", \"data_count\": \"134 train tasks\", \"checkpoint_source\": \"Qwen3-1.7B base (same as hsweep_h2_seed1, not from parent checkpoint)\", \"eval_data\": \"ALFWorld val 16 tasks\", \"log_path\": \"~/runs/cost-verify-agent-rl/hsweep_h2_s2.log\", \"notes\": \"auto_next triggered from hsweep_h2_seed1 completion. LOG_PER_SAMPLE_ADV=1 for plan_004 advantage logging.\", \"env\": \"LOG_PER_SAMPLE_ADV=1\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/hsweep-h2/global_step_15/\"}, \"metrics\": {\"current_step\": \"15/15\", \"completed\": true, \"val_step5\": {\"success\": 0}, \"val_step10\": {\"success\": 0}, \"val_step15\": {\"success\": 0.09375}, \"train_step14\": {\"success\": 0.2656, \"pass_at_8\": 0.6875}, \"train_step15\": {\"success\": 0.2812, \"pass_at_8\": 0.625, \"entropy\": 0.401, \"ppo_kl\": 0.006}, \"train_success_peak\": {\"step\": 15, \"value\": 0.2812}, \"adv_log_lines\": 3000, \"adv_episodes\": {\"total\": 128, \"success\": 65, \"fail\": 63}, \"adv_analysis\": {\"sign_outcome_agreement\": 0.5207, \"point_biserial_r\": 0.068, \"p_adv_pos_given_success\": 0.3706, \"p_adv_pos_given_failure\": 0.306, \"magnitude_decay_gamma\": 0.9426, \"distribution_overlap\": 0.878, \"verdict\": \"52% agreement confirms advantage signal nearly uninformative about episode outcome = sign misattribution\"}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/hsweep-h2/global_step_15/\", \"checkpoint_warning\": \"seed2 overwrote seed1 step15 checkpoint in same directory\", \"status_note\": \"COMPLETED 15/15. Late recovery at step 14-15 (train 26-28%). Val 9.375% on 16 in-dist tasks. ADV: 52% sign agreement = near-random.\"}, \"conclusion\": \"success\", \"notes\": \"15/15 步正常完成 + final val。Hypothesis NOT confirmed：seed2 未复现 seed1 的 catastrophic collapse。关键差异：(1) action_is_valid 始终 88-100%（seed1 崩至 0.06%）(2) val step 15 恢复到 9.375%（seed1 终值 0%）(3) train step 15 success=28.1%（seed1 终值 0%）。Val step 0/5/10 确实为 0%，说明 h=2 确实造成学习困难，但不是 seed1 那样的不可逆 catastrophic collapse。Collapse 行为是 seed-dependent 的，不是 robust finding。ADV log 3000 行可用于 sign misattribution 分析。注意：checkpoint 写入 hsweep-h2/ 目录（与 seed1 共享，global_step_15 被覆盖）。\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/hsweep-h2/global_step_15\", \"log_path\": \"/root/runs/cost-verify-agent-rl/hsweep-h2-seed2.log\", \"completed_at\": \"2026-05-18T02:52:28.352Z\"}, \"gae_baseline_seed1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T14:05:31.533Z\", \"updated_at\": \"2026-05-17T19:19:48.391Z\", \"hypothesis\": \"REINFORCE++ (running-mean baseline, no critic) provides modest improvement over episode-level GRPO due to per-token advantage normalization. Fallback from GAE due to TRL 1.1.0 removing AutoModelForCausalLMWithValueHead (critic head unavailable).\", \"parent\": \"exp029_episode_level\", \"spec\": {\"command\": \"python train.py --config-name _alfworld_reinforce_pp_baseline\", \"server\": \"westd-47453\", \"gpu\": \"cuda:0,1\", \"pid\": 40267, \"wandb_run_id\": \"dt79qyd9\", \"model_name\": \"Qwen3-1.7B\", \"seed\": 42, \"data_path\": \"ALFWorld\", \"data_count\": \"134 train tasks\", \"val_episodes\": 32, \"checkpoint_path\": \"N/A (killed at step 11/15)\", \"log_path\": \"~/runs/cost-verify-agent-rl/gae_baseline_seed1.log\"}, \"metrics\": {\"wandb_run_id\": \"dt79qyd9\", \"pid\": 40267, \"val_step0\": {\"success\": 0.0625, \"action_is_valid\": 0.7796}, \"val_step5\": {\"success\": 0.125, \"action_is_valid\": 0.6926}, \"val_step10\": {\"success\": 0.125, \"pass_at_1\": 0.125, \"reward_mean\": 1.25}, \"train_step9\": {\"success\": 0.0313, \"action_is_valid\": 0.6033, \"pass_at_8\": 0.25}, \"server\": \"westd-47453\", \"gpu\": \"cuda:0,1\", \"method\": \"reinforce_plus_plus\", \"fallback_reason\": \"TRL 1.1.0 removed AutoModelForCausalLMWithValueHead\", \"current_step\": \"11/15\"}, \"notes\": \"实际运行 REINFORCE++ (adv_estimator=reinforce_plus_plus_baseline)，非 GAE。GAE 因 TRL 1.1.0 移除 AutoModelForCausalLMWithValueHead 不可用 (D060)。\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-17T19:19:48.391Z\"}, \"hsweep_h2_seed1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T04:37:11.061Z\", \"updated_at\": \"2026-05-17T14:36:40.246Z\", \"hypothesis\": \"Step-independent GRPO with h=2 (minimal context, N=25 windows per episode) will catastrophically collapse due to advantage sign misattribution: early windows retain only γ^24=0.95^24≈29% of terminal return, and all windows in failed episodes receive undifferentiated negative advantage regardless of action quality\", \"parent\": \"exp029_episode_level\", \"spec\": {\"command\": \"bash /root/cost-verify-agent-rl/scripts/launch_hsweep.sh 2 1\", \"server\": \"bjb1-17606\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"920380\", \"model_name\": \"Qwen3-1.7B (SFT checkpoint: /root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4)\", \"data_path\": \"RAGEN expert data (same as exp029)\", \"data_count\": \"16 train tasks / 128 val tasks\", \"seed\": 10000, \"log_path\": \"~/runs/cost-verify-agent-rl/hsweep_h2_s1.log\", \"algorithm\": \"GRPO + step_independent (h=2)\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4\", \"eval_data\": \"N/A (training experiment, not eval)\", \"key_params\": {\"context_window_mode\": \"step_independent\", \"step_independent_history_length\": 2, \"total_training_steps\": 15, \"test_freq\": 5, \"save_freq\": 5, \"gamma\": 0.95, \"kl_loss_coef\": 0.01, \"group_size\": 8}}, \"metrics\": {\"train_step\": 15, \"total_steps\": 15, \"wandb_run_id\": \"7o9bjszm\", \"step1\": {\"success\": 0.1875, \"pass_at_8\": 0.4375, \"invalid_action\": 0.027}, \"step2\": {\"success\": 0.1484, \"pass_at_8\": 0.5, \"invalid_action\": 0.02}, \"step3\": {\"success\": 0.1875, \"pass_at_8\": 0.625, \"invalid_action\": 0.028}, \"step4\": {\"success\": 0.0547, \"pass_at_8\": 0.25, \"invalid_action\": 0.264}, \"step5\": {\"success\": 0.0156, \"pass_at_8\": 0.0625, \"invalid_action\": 0.369}, \"step6\": {\"success\": 0.0313, \"pass_at_8\": 0.25, \"invalid_action\": 0.471}, \"step7\": {\"success\": 0.0469, \"pass_at_8\": 0.1875, \"invalid_action\": 0.502}, \"step8\": {\"success\": 0.0156, \"pass_at_8\": 0.125, \"invalid_action\": 0.542}, \"step9\": {\"success\": 0, \"pass_at_8\": 0, \"invalid_action\": 0.641}, \"step10\": {\"success\": 0.0234}, \"step11_15\": {\"success\": 0, \"invalid_action\": 0.972}, \"val_final\": {\"success\": 0, \"invalid_action\": 0.999, \"action_is_valid\": 0.0006}, \"checkpoint\": \"global_step_5,10,15\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/hsweep-h2/\", \"log_path\": \"~/runs/cost-verify-agent-rl/hsweep_h2_s1.log\", \"gpu_util\": \"95-100%\", \"collapse_onset\": \"step3→step4\", \"elapsed_hours\": 10.04, \"step15_entropy\": 0.342, \"step15_kl_loss\": 0.777, \"step15_grad_norm\": 1.611, \"auto_next_triggered\": true, \"seed2_pid\": 945877, \"seed2_wandb\": \"jhwyg4tc\"}, \"plan_id\": \"plan_002\", \"conclusion\": \"success\", \"notes\": \"15 steps 完成。Hypothesis 验证：h=2 step_independent 确实灾难性崩溃（step 3→4 onset, step 9 归零, step 11-15 持续为零）。Final val: success=0%, invalid_action=99.9%, action_is_valid=0.06%。模型彻底退化到几乎只输出无效动作。\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/hsweep-h2/global_step_15\", \"log_path\": \"/root/runs/cost-verify-agent-rl/hsweep-h2-seed1.log\", \"completed_at\": \"2026-05-17T14:35:27.052Z\"}, \"exp025c\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T08:09:29.393Z\", \"updated_at\": \"2026-05-17T10:53:00.425Z\", \"spec\": {\"name\": \"verl-agent ALFWorld GRPO baseline — single GPU, thread-safe config\", \"hypothesis\": \"verl-agent GRPO with Qwen3-1.7B on single GPU (TP=1, enforce_eager, thread-limited) can train ALFWorld within cgroup pids.max=20480 limit. Degraded dry run validated: PIDs stable at 6575/20480 (32%). Target: success ≥20%.\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate /root/autodl-tmp/conda-envs/verl-agent && cd /root/autodl-tmp/verl-agent && bash examples/grpo_trainer/run_alfworld_exp025c.sh\\\"\", \"server\": \"bjb1-17606\", \"data_path\": \"$HOME/data/verl-agent/text/train.parquet\", \"data_count\": \"16 train / 128 val\", \"model_name\": \"Qwen3-1.7B (local: /root/autodl-tmp/models/Qwen/Qwen3-1___7B/)\", \"seed\": 0, \"framework\": \"verl-agent v0.3.1.dev\", \"algorithm\": \"GRPO\", \"gpus\": \"cuda:0 (1x RTX PRO 6000 Blackwell 98GB)\", \"key_params\": {\"train_batch_size\": 16, \"val_batch_size\": 128, \"group_size\": 8, \"lr\": 1e-06, \"total_epochs\": 150, \"max_steps\": 50, \"kl_loss_coef\": 0.01, \"invalid_action_penalty_coef\": 0.1, \"tensor_model_parallel_size\": 1, \"test_freq\": 5, \"val_before_train\": true, \"save_freq\": 25, \"enforce_eager\": true, \"env_rollout_n\": 2, \"ray_init_num_cpus\": 8, \"vllm_attention_backend\": \"FLASH_ATTN\", \"thread_limit\": \"OMP/MKL/OPENBLAS/NUMEXPR=1\"}}, \"notes\": \"项目已 pivot 到 h-sweep + sign misattribution 诊断方向（D054/D057）。exp025c 属于 pivot 前的实验设计，不在当前 experiment_plan.yaml 中，与论文核心 claims 无关联。GPU 资源优先用于 h-sweep 和 GAE baseline。\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-17T10:52:59.475Z\"}, \"exp026_step_independent_grpo\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-15T09:34:33.675Z\", \"updated_at\": \"2026-05-17T03:14:31.315Z\", \"server\": \"bjb1-17606\", \"gpu\": \"cuda:0,cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-17606\", \"gpu\": \"cuda:0,cuda:1\", \"started_at\": \"2026-05-15T09:35:34.249Z\", \"finished_at\": \"2026-05-15T11:07:27.171Z\", \"training_hours\": 1.53}, \"notes\": \"exp026 negative: step-independent GRPO 在 step 2 达峰 train success=32.81% 后连续崩塌至 step 4 的 0%。Step 5 val eval 未完成即被 kill（val 生成阶段启动后进程被终止），无法对比 step 0 vs step 5 val。无 checkpoint（save_freq=25 未触发）。根因分析（Reviewer）：sparse reward + 小 env_groups(4=64 rollouts) 导致全零 batch 概率高，advantage 只有负信号把策略推回 reference。action_is_valid 在 step 2-4 保持 ~72% 但 success 归零，模型学会了\\\"看起来合理\\\"的 action 但丧失任务完成能力。教训：(1) save_freq 必须 ≤5 捕获早期峰值 (2) env_groups 需 ≥8 降低全零 batch 概率 (3) WANDB_MODE=disabled 导致 cron 误判 (4) cron 应监控 Ray TaskRunner PID 而非 shell wrapper PID。\", \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-15T11:07:28.010Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T11:07:29.450586+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"metrics\": {\"val_before_train_success\": 0.0625, \"val_before_train_action_is_valid\": 0.631, \"val_before_train_action_is_effective\": 0.879, \"val_before_train_episodes\": 16, \"val_before_train_pass_at_1\": 0.0625, \"truncation_count_val\": 25, \"train_step1_success\": 0.2188, \"train_step1_action_is_valid\": 0.686, \"train_step1_entropy\": 0.2672, \"train_step1_pg_loss\": 0.00732, \"train_step1_kl_loss\": 0.1797, \"train_step1_ppo_kl\": 0.067, \"train_step1_grad_norm\": 14.43, \"train_step1_reward_mean\": 1.218, \"train_step1_pass_at_16\": 1, \"train_step2_success\": 0.3281, \"train_step2_action_is_valid\": 0.603, \"train_step2_entropy\": 0.317, \"train_step2_pg_loss\": 0.00571, \"train_step2_kl_loss\": 0.0974, \"train_step2_ppo_kl\": 0.0267, \"train_step2_grad_norm\": 15.62, \"train_step2_reward_mean\": 1.62, \"train_step2_pass_at_16\": 1}, \"notes\": \"⚠️ D029: CRON 误判 DONE(failed)，进程实际仍在运行。Train step 1-2 指标突破性：success 6.25% → 21.88% → 32.81%（已超 MVP 20%），entropy 0.267→0.317（无 collapse），grad_norm 14-16（稳定）。指标来源：Ray worker stdout logs。Step 5 val 是首个正式验证点。早停标准维持。后续实验硬规则：禁止 WANDB_MODE=disabled。\"}}, \"spec\": {\"command\": \"bash -c \\\"ray stop --force; pkill -9 -f ray; pkill -9 -f vllm; sleep 3; rm -rf /tmp/ray/session_*; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/cost-verify-agent-rl && bash scripts/run_exp026_step_independent_grpo.sh\\\"\", \"server\": \"bjb1-17606\", \"gpu\": \"cuda:0,cuda:1\", \"pid\": 781795, \"log_path\": \"/root/autodl-tmp/tmp/ray/session_2026-05-15_18-38-45_487055_778562/logs/worker-f5a9c771de63c207b8db019edc7dedd89a425c2fe97314a2669cdd43-01000000-781795.out\", \"data_path\": \"RAGEN expert data (same as exp021)\", \"data_count\": \"16 train tasks / 128 val tasks per epoch\", \"model_name\": \"Qwen3-1.7B (SFT checkpoint: /root/autodl-tmp/checkpoints/exp021_ragen_sft_v4/final/)\", \"seed\": 0, \"framework\": \"RAGEN + cherry-picked step-independent rollout\", \"algorithm\": \"GRPO + step-independent rollout + discounted returns\", \"key_params\": {\"context_window_mode\": \"step_independent\", \"step_independent_history_length\": 5, \"kl_loss_coef\": 0.01, \"kl_loss_type\": \"low_var_kl\", \"lr\": 1e-06, \"group_size\": 8, \"gamma\": 0.95, \"invalid_action_penalty_coef\": 0.1, \"max_turn\": 50, \"total_training_steps\": 150, \"test_freq\": 5, \"save_freq\": 25, \"val_before_train\": true, \"use_turn_scores\": true}}, \"metrics\": {\"val_before_train_success\": 0.0625, \"val_before_train_action_is_valid\": 0.631, \"val_before_train_episodes\": 16, \"train_step1_success\": 0.2188, \"train_step1_action_is_valid\": 0.686, \"train_step1_entropy\": 0.2672, \"train_step1_kl_loss\": 0.1797, \"train_step1_grad_norm\": 14.43, \"train_step1_reward_mean\": 1.218, \"train_step1_pass_at_16\": 1, \"train_step2_success\": 0.3281, \"train_step2_action_is_valid\": 0.603, \"train_step2_entropy\": 0.317, \"train_step2_kl_loss\": 0.0974, \"train_step2_grad_norm\": 15.62, \"train_step2_reward_mean\": 1.62, \"train_step2_pass_at_16\": 1, \"train_step3_success\": 0.1719, \"train_step3_action_is_valid\": 0.641, \"train_step3_entropy\": 0.387, \"train_step3_kl_loss\": 0.2617, \"train_step3_grad_norm\": 15.65, \"train_step3_reward_mean\": 1.079, \"train_step3_pass_at_16\": 0.75, \"train_step4_success\": 0, \"train_step4_action_is_valid\": 0.717, \"train_step4_entropy\": 0.387, \"train_step4_kl_loss\": 0.054, \"train_step4_grad_norm\": 13.81, \"train_step4_pass_at_16\": 0}, \"conclusion\": \"negative\", \"log_path\": \"/root/autodl-tmp/tmp/ray/session_2026-05-15_18-38-45_487055_778562/logs/worker-*-781795.out\", \"checkpoint_path\": \"N/A (crashed at step 4, no checkpoint saved)\", \"hypothesis\": \"Step-independent GRPO（每步独立优化、不建模跨步依赖）能在ALFWorld多步任务中学到有效策略，因为每步的local reward信号足以引导正确行为选择\", \"parent\": \"exp021_ragen_sft_v4\"}, \"exp019b_expert_sft_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:30:00.085Z\", \"updated_at\": \"2026-05-17T03:14:30.703Z\", \"spec\": {\"command\": \"nohup bash /root/cost-verify-agent-rl/scripts/run_exp019b.sh > /tmp/exp019b.log 2>&1\", \"server\": \"bjb1-17606\", \"gpu\": [\"cuda:0\"], \"pid\": \"379367\", \"log_path\": \"/tmp/exp019b.log\", \"submitted_at\": \"2026-05-14T20:54:00.000Z\", \"submitted_via\": \"nohup\", \"backend\": \"nohup\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/expert_sft_v3/expert_sft_train.jsonl\", \"data_count\": 2546, \"model_name\": \"Qwen3-1.7B (from exp008_sft/final)\", \"seed\": 42, \"wall_clock_seconds\": 2964.6, \"gpu_hours\": 0.82}, \"server\": \"bjb1-17606\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"pid\": \"379367\", \"log_path\": \"/tmp/exp019b.log\", \"hypothesis\": \"Two-stage Expert SFT: exp008_sft checkpoint + v3 data (original move actions + admissible actions). LR=5e-6, 2 epochs, batch=4, grad_accum=4, max_seq=4096. Pass: success>=10%, format_ok>=90%, action_is_valid>=85%.\", \"notes\": \"训练成功完成 320/320 steps (2 epochs, 47:49)。Cron 多次误报 failed（监控错误 PID / 无法区分正常退出与崩溃）。Checkpoint: /root/autodl-tmp/checkpoints/exp019b_expert_sft_v3/final/\", \"reproduce\": {\"finished_at\": \"2026-05-14T21:43:23.788Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T21:43:24.618Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T21:43:25.640262+00:00\"}]}, \"metrics\": {\"train_loss\": 0.0718, \"eval_loss\": 0.0428, \"eval_mean_token_accuracy\": 0.9869, \"train_runtime_seconds\": 2869.8, \"steps\": 320, \"epochs\": 2, \"eval_success_rate\": 0.2, \"eval_format_ok\": 1, \"eval_action_is_valid\": 0.8533, \"eval_episodes\": 20, \"eval_avg_steps\": 25.4, \"eval_time_seconds\": 146}, \"parent\": \"exp008_sft\"}, \"exp013f\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T09:21:46.227Z\", \"updated_at\": \"2026-05-17T03:14:29.725Z\", \"hypothesis\": \"Dense reward shaping(valid_action_bonus=0.15)为全失败GRPO group提供非零方差梯度信号，使模型在避免梯度collapse的同时学到task success而非仅优化bonus\", \"parent\": \"exp013e\", \"spec\": {\"command\": \"bash /root/cost-verify-agent-rl/scripts/run_exp013f.sh\", \"server\": \"bjb1-17606\", \"data_path\": \"AlfworldSG_Dense (3553 train games)\", \"data_count\": 3553, \"model_name\": \"Qwen3-1.7B SFT (exp008_sft/final)\", \"seed\": 10000, \"pid\": 313810, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/exp013f/\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp013f.log\", \"description\": \"Dense reward GRPO with full Director fixes: RAY_memory_monitor_refresh_ms=0, RAY_SYSTEM_MEMORY=210GB, val env_groups 16→4, HYDRA_FULL_ERROR=1, Ray log auto-backup on crash. object_store_memory=30GB. From step 5 checkpoint.\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/exp008_grpo/global_step_5\", \"eval_data\": \"N/A - training experiment\"}, \"metrics\": {\"step\": 30, \"total_steps\": 30, \"completed\": true, \"exit_code\": 0, \"training_time_s\": 10683, \"step6_success\": 0.0156, \"step7_success\": 0.0781, \"step10_success\": 0, \"step17_success\": 0.0156, \"final_val_success\": 0, \"final_val_action_is_valid\": 0.975, \"final_val_action_is_effective\": 1, \"final_val_reward_mean_at4\": 4.388, \"final_val_reward_std_at4\": 0.195, \"final_val_reward_best_at4\": 4.499, \"final_val_pass_at1\": 0, \"action_is_valid_trend\": \"60%→65.9%→77.1%→97.5%\", \"success_trend\": \"0%→1.56%→7.81%→0%→1.56%→0%\", \"grad_norm_range\": \"1.7-2.9 (no collapse)\", \"conclusion_reason\": \"Dense reward gaming: model optimized valid_action_bonus (action_is_valid 60%→97.5%) but success stayed 0%. Reward ratio 1:67 too weak — cumulative valid_action_bonus (4.5) dominated learning signal vs sparse success_reward (10.0). GRPO collapse prevented but task completion not learned.\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T12:33:28.313Z\", \"notes\": \"30/30 步完成，EXIT_CODE=0。Dense reward shaping 成功解决了 exp012b 的 catastrophic collapse（grad_norm 稳定 1.7-2.9），但产生 reward gaming：模型最大化 valid_action_bonus 而非 success_reward。action_is_valid 60%→97.5%（学会合法命令），success 始终 0-8%（未学会完成任务）。final_val reward/mean@4=4.388 ≈ 29 valid_actions × 0.15，几乎无 success_reward 贡献。Disk warning: /root/autodl-tmp 95% full (4.1GB remaining)。Ray log 备份失败（脚本执行时 session 已清理）。Checkpoint: global_step_30 已保存。\"}, \"exp028_prereq_zeroshot\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T21:11:06.120Z\", \"updated_at\": \"2026-05-17T03:14:28.598Z\", \"conclusion\": \"negative\", \"checkpoint_path\": \"N/A (zero-shot eval, no checkpoint)\", \"log_path\": \"wandb:qdvv09da\", \"completed_at\": \"2026-05-15T21:11:32.780Z\", \"wandb_run_id\": \"qdvv09da\", \"metrics\": {\"success\": 0, \"action_is_valid\": 0.75, \"num_actions\": 50, \"pass_at_1\": 0, \"response_length\": 75.07}, \"notes\": \"Qwen3-1.7B（本身就是 instruct 模型）零样本 ALFWorld eval = 0% success。证明 SFT 从 0%→6.25% 是有益的，D044 '不做SFT' 假设不成立。W&B run: qdvv09da\", \"hypothesis\": \"Qwen3-1.7B base模型具备ALFWorld零样本能力(success>0%)，无需SFT即可作为GRPO冷启动点——如成立则SFT引入的分布偏差可能反而有害\"}, \"exp008_sft\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T03:04:47.496Z\", \"updated_at\": \"2026-05-17T03:14:25.946Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python /root/cost-verify-agent-rl/scripts/sft_train.py\", \"server\": \"bjb1-17606\", \"gpu\": [\"cuda:0\"], \"pid\": \"192546\", \"log_path\": \"/root/autodl-tmp/exp008_sft_v2.log\", \"submitted_at\": \"2026-05-14T03:21:15.615Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"hypothesis\": \"SFT warmup on ALFWorld trajectories teaches Qwen3-1.7B valid command semantics\", \"model_name\": \"Qwen3-1.7B\", \"data_path\": \"/root/autodl-tmp/sft_data/alfworld_sft_ragen.jsonl\", \"data_count\": 1200, \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/exp008_sft/final\", \"wall_clock_seconds\": 990.8, \"gpu_hours\": 0.28}, \"notes\": \"SFT 转换脚本修复后重跑成功。Eval 方法: 独立脚本 eval_sft_model.py, 4 episodes (seed=0,1,2,3), HF generate() + AlfredTXTEnv, cuda:1, max_steps=50。action_is_valid=90% (180/200 actions), format_ok=100%, success_rate=0%。完整 50-episode eval 未完成（为 GRPO 让出 GPU）。\", \"conclusion\": \"success\", \"metrics\": {\"action_is_valid\": 0.9, \"format_ok\": 1, \"success_rate\": 0, \"final_loss\": 0.069, \"final_token_accuracy\": 0.973, \"data_count\": 1200, \"epochs\": 3, \"total_steps\": 225, \"training_time_s\": 576}, \"completed_at\": \"2026-05-14T03:37:46.382Z\", \"hypothesis\": \"基础格式SFT使Qwen3-1.7B学会ALFWorld动作格式和有效动作选择(format_ok+action_is_valid)，建立可训练基线，为后续expert SFT和GRPO提供非随机起点\"}, \"exp028c_selfguide_recipe\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T21:38:48.089Z\", \"updated_at\": \"2026-05-16T08:29:53.723Z\", \"wandb_run_id\": \"4yu6qz1m\", \"spec\": {\"command\": \"bash scripts/run_exp028c_selfguide_recipe.sh\", \"server\": \"bjb1-17606\", \"data_path\": \"AlfworldSG (env_configs)\", \"data_count\": 128, \"model_name\": \"qwen3_exp021_ragen_sft_v4 (SFT checkpoint)\", \"seed\": 10000}, \"notes\": \"D052 终止。step_independent h=2 导致灾难性过拟合：step_5_val best@128=10.0 → step_10_val best@800=0.0。train success 波动上升(peak 21.88%)=局部动作过拟合，但无法泛化到新 game。根因：(1) step_independent 破坏长程信用分配 (2) self-guidance reward 缺失 (3) val 仅 16 episodes。参见 selfguide_setup_audit.md。\", \"metrics\": {\"step_0_val\": {\"success\": 6.25, \"pass_at_1\": 6.25, \"action_is_valid\": 74.5, \"score_mean\": 0.119}, \"step_1_train\": {\"success\": 13.28, \"pass_at_8\": 37.5, \"action_is_valid\": 76.4, \"action_is_effective\": 96.37, \"entropy\": 0.2634, \"kl_loss\": 0.0128, \"ppo_kl\": 0.019, \"grad_norm\": 16.88, \"score_mean\": 0.843, \"time_s\": 3252, \"note\": \"三方交叉验证通过\"}, \"step_2_train\": {\"success\": 6.25, \"pass_at_8\": 25, \"action_is_valid\": 83.2, \"entropy\": 0.247, \"kl_loss\": 0.1706, \"pg_loss\": 0.007, \"grad_norm\": 17.3, \"score_mean\": 0.274, \"time_s\": 3120}, \"step_3_train\": {\"success\": 15.63, \"pass_at_8\": 68.75, \"action_is_valid\": 85.9, \"entropy\": 0.2488, \"kl_loss\": 0.1118, \"grad_norm\": 12.57, \"score_mean\": 0.661, \"time_s\": 2760}, \"step_4_train\": {\"success\": 18.75, \"pass_at_8\": 62.5, \"action_is_valid\": 87.94, \"entropy\": 0.234, \"kl_loss\": 0.031, \"ppo_kl\": 0.015}, \"step_5_train\": {\"success\": 9.4, \"pass_at_8\": 37.5, \"action_is_valid\": 89.6, \"entropy\": 0.236, \"kl_loss\": 0.824, \"grad_norm\": 13.1}, \"step_5_val\": {\"success\": 6.25, \"pass_at_1\": 6.25, \"action_is_valid\": 96.5, \"action_is_effective\": 100, \"num_actions\": 49.4, \"score_mean\": 0.518}, \"step_6_train\": {\"success\": 10.94, \"action_is_valid\": 90.4, \"entropy\": 0.234, \"kl_loss\": 0.098, \"grad_norm\": 12.54}, \"step_7_train\": {\"success\": 21.88, \"pass_at_8\": 56.25, \"action_is_valid\": 91.8, \"entropy\": 0.224, \"kl_loss\": 0.046}, \"step_8_train\": {\"success\": 15.6, \"pass_at_8\": 50, \"action_is_valid\": 92.7, \"kl_loss\": 0.039, \"entropy\": 0.204}, \"step_9_train\": {\"success\": 18, \"pass_at_8\": 56.3, \"action_is_valid\": 93.6, \"kl_loss\": 0.047, \"entropy\": 0.204}, \"step_10_train\": {\"success\": 18.75, \"action_is_valid\": 90.7, \"kl_loss\": 0.197}, \"step_10_val\": {\"success\": 0, \"pass_at_1\": 0, \"best_at_128\": 0, \"best_at_800\": 0, \"action_is_valid\": 93.6, \"num_actions\": 49.8, \"reward_mean\": 0, \"note\": \"灾难性崩溃，模型完全遗忘\"}}, \"conclusion\": \"failed\", \"reproduce\": {\"finished_at\": \"2026-05-16T08:18:35.556Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-16T08:18:36.285Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T08:18:38.177731+00:00\"}]}}, \"exp028a_recipe_fix\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T21:08:53.131Z\", \"updated_at\": \"2026-05-15T21:25:46.006Z\", \"hypothesis\": \"invalid_action_penalty (-0.1) 为全失败 GRPO group 提供非零方差梯度信号。从 exp021 SFT checkpoint (6.25% success) 出发，仅增加 invalid_action_penalty_coef=0.1，其余参数与 exp027 完全一致。预期：penalty 让失败 trajectory 间有区分（invalid action 多=reward更低），解决 ~43% group 零梯度问题。Pass: success ≥20%（稳定，非瞬时 peak）。\", \"parent\": \"exp027_stable_grpo\", \"wandb_run_id\": \"lu42su82\", \"spec\": {\"command\": \"bash scripts/run_exp028a_recipe_fix.sh\", \"server\": \"bjb1-17606\", \"model_name\": \"qwen3_exp021_ragen_sft_v4\", \"seed\": 10000, \"data_path\": \"AlfworldSG\", \"data_count\": 128, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4\", \"eval_data\": \"AlfworldSG val 16 episodes\"}, \"conclusion\": \"killed\", \"notes\": \"与 exp027 功能等价（penalty getattr 默认值=0.1 在 exp027 中已生效）。Director 指令停止。\", \"completed_at\": \"2026-05-15T21:25:46.007Z\"}, \"exp028_prereq_zeroshot_instruct\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:59:57.529Z\", \"updated_at\": \"2026-05-15T21:06:09.982Z\", \"hypothesis\": \"Qwen3-1.7B-Instruct 零样本 ALFWorld eval，验证\\\"SFT是毒药\\\"假设。如果 Instruct ≥15% success（vs SFT checkpoint 6.25%），则确认 SFT 起点有害，exp028a 可跳过 SFT 直接 GRPO。\", \"parent\": \"exp027_stable_grpo\", \"notes\": \"Qwen3-1.7B 确认就是 instruct 模型（无独立 Instruct 变体）。零样本 eval 0% success / 0.75% valid（与之前结果一致）。关键结论：\\\"SFT是毒药\\\"假设(D044)不成立——SFT 实际提升了 0%→6.25%。62pp gap 根因排除 SFT，聚焦于 binary reward 零梯度 + mini-batch 过小 + 训练步数不足。\"}, \"exp027_stable_grpo\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:04:13.123Z\", \"updated_at\": \"2026-05-15T20:44:26.582Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/cost-verify-agent-rl && bash scripts/run_exp027_stable_grpo.sh\\\"\", \"server\": \"bjb1-17606\", \"gpu\": \"cuda:0,cuda:1\", \"pid\": 789790, \"log_path\": \"~/runs/cost-verify-agent-rl/exp027_stable_grpo.log\", \"submitted_at\": \"2026-05-15T14:33:03.633Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"RAGEN expert data (same as exp021/026)\", \"data_count\": \"16 train / 128 val per epoch, env_groups=8: 128 rollouts per train step\", \"model_name\": \"Qwen3-1.7B (SFT checkpoint: /root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4)\", \"seed\": 0, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4\", \"eval_data\": \"ALFWorld train+val environments (RAGEN format, val env_groups=16, C003-compliant)\", \"framework\": \"RAGEN + cherry-picked step-independent rollout\", \"algorithm\": \"GRPO + step-independent rollout + discounted returns\", \"key_params\": {\"lr\": 5e-07, \"kl_loss_coef\": 0.005, \"entropy_coeff\": 0.01, \"save_freq\": 5, \"total_training_steps\": 50, \"test_freq\": 5, \"env_groups_train\": 8, \"env_groups_val\": 16, \"max_actor_ckpt_to_keep\": 10, \"context_window_mode\": \"step_independent\", \"step_independent_history_length\": 5, \"gamma\": 0.95, \"group_size\": 16, \"invalid_action_penalty_coef\": 0.1, \"max_turn\": 50, \"WANDB_MODE\": \"enabled\"}, \"wall_clock_seconds\": 22179.3, \"gpu_hours\": 6.16}, \"notes\": \"进程退出原因：Ray raylet 被异常终止（ActorUnavailableError: RPC error: Socket closed rpc_code: 14）。Raylet termination unexpected — 可能 SIGKILL by OOM killer 或内存访问错误。退出发生在 step 4 完成后、step 5 开始前。EXIT_CODE=1。D045 已判定 MVP 未通过（train success 13.28% < 20% 阈值）。Recipe Gap 诊断三大根因：(1) SFT 起点反效果 (2) Binary reward 零梯度 (3) Mini-batch 8× 过小。exp028 配置准备中（5 个 Worker 活跃）。\", \"hypothesis\": \"Stabilized step-independent GRPO: 针对 exp026 死亡螺旋根因（sparse reward + 小 env_groups 导致全零 batch），增加 rollouts（env_groups 4→8, 128 trajectories）、降低 LR（1e-6→5e-7）、降低 KL（0.01→0.005）、新增 entropy bonus（0.01）、save_freq 5 捕获峰值。50 步快速验证。Pass: success ≥20% 且无连续 2 步归零。\", \"parent\": \"exp026_step_independent_grpo\", \"wandb_run_id\": \"y7jiibqk\", \"metrics\": {\"step_0_val_before_train\": {\"success\": 6.25, \"action_is_valid\": 63.125, \"action_is_effective\": 87.875, \"num_actions\": 42.375, \"response_length\": 114.67, \"reward_mean\": 0.3226, \"val_generation_time_s\": 502.57}, \"step_1_train\": {\"success\": 35.94, \"kl_loss\": 0.058, \"batch_size\": 5152, \"training_time_s\": 4342}, \"step_2_train\": {\"success\": 10.16, \"kl_loss\": 0.413, \"batch_size\": 6144, \"training_time_s\": 5886}, \"step_3_train\": {\"success\": 10.16, \"kl_loss\": 0.248, \"entropy\": 0.385, \"pass_at_16\": 0.5, \"grad_norm\": 21.31, \"reward_mean\": 0.483, \"batch_size\": 6048, \"training_time_s\": 4689}, \"step_4_train\": {\"success\": 13.28, \"pass_at_16\": 0.375, \"note\": \"Director判定: 趋势确认, MVP未通过\"}}, \"conclusion\": \"failed\", \"reproduce\": {\"finished_at\": \"2026-05-15T20:42:41.686Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-15T20:42:42.920Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T20:42:44.371995+00:00\"}]}}, \"exp025b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:34:34.283Z\", \"updated_at\": \"2026-05-15T07:44:26.903Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate /root/autodl-tmp/conda-envs/verl-agent && cd /root/autodl-tmp/verl-agent && bash examples/grpo_trainer/run_alfworld_exp025.sh\\\"\", \"server\": \"bjb1-17606\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"615550\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp025b.log\", \"submitted_at\": \"2026-05-15T07:41:46.859Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"parent\": \"exp025\", \"notes\": \"三次提交均失败。第三次：pre-flight 清理后 Ray 主进程启动成功、数据加载成功（8810 train / 494 val），但 AlfworldWorker 进程初始化时线程创建失败（Resource temporarily unavailable, EAGAIN）。36+ 次 system:11 错误，43+ 次 Fatal Python error: Aborted。jemalloc arena background thread creation failed。根因：系统 nproc/线程上限不足，8 个 AlfworldWorker + Ray 内部线程总数超限。需排查 ulimit -u 和 /proc/sys/kernel/threads-max。\", \"server\": \"bjb1-17606\", \"gpu\": \"cuda:0,cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-17606\", \"gpu\": \"cuda:0,cuda:1\", \"started_at\": \"2026-05-15T07:35:49.952Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate /root/autodl-tmp/conda-envs/verl-agent && cd /root/autodl-tmp/verl-agent && bash examples/grpo_trainer/run_alfworld_exp025.sh\\\"\", \"finished_at\": \"2026-05-15T07:38:59.743Z\", \"training_hours\": 0.05}, \"pid\": \"614229\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp025b.log\", \"conclusion\": \"failed\", \"failure_reason\": \"Traceback → /resource_tracker.py\\\", line 89, in _stop File \\\"/root/autodl-tmp/conda-envs/verl-agent/lib/python3.12/site-packages/multiprocess/resource_tracker.py\\\", line 102, in _stop_locked AttributeError: '_thread.RLock' object has no attribute '_recursion_count'\", \"completed_at\": \"2026-05-15T07:39:01.024Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T07:39:02.902074+00:00\"}]}}, \"exp025\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:52:48.190Z\", \"updated_at\": \"2026-05-15T07:34:25.374Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/verl-agent && bash examples/grpo_trainer/run_alfworld_exp025.sh\\\"\", \"server\": \"bjb1-17606\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"555182\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp025.log\", \"submitted_at\": \"2026-05-15T07:13:01.394Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 143.1, \"gpu_hours\": 0.08}, \"notes\": \"崩溃原因：(1) conda activate base 错误，应用 /root/autodl-tmp/conda-envs/verl-agent 环境 (2) save_freq=-1 未修改为 25。ModuleNotFoundError — base 环境缺 verl-agent 依赖。教训：提交前必须验证 which python 指向正确环境 + 关键参数在 config 中与预期一致。\", \"server\": \"bjb1-17606\", \"gpu\": \"cuda:0,cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-17606\", \"gpu\": \"cuda:0,cuda:1\", \"started_at\": \"2026-05-15T07:11:50.984Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/verl-agent && bash examples/grpo_trainer/run_alfworld_exp025.sh\\\"\", \"finished_at\": \"2026-05-15T07:15:22.435Z\", \"training_hours\": 0.06}, \"pid\": \"555182\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp025.log\", \"failure_reason\": \"ModuleNotFoundError in ray::TaskRunner.run() — verl-agent ALFWorld 训练进程异常退出，缺少模块。诊断 Worker 已派出分析具体缺失模块。\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T07:15:24.448Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T07:15:25.976397+00:00\"}]}}, \"exp021_ragen_sft_v4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T02:09:31.719Z\", \"updated_at\": \"2026-05-15T06:24:16.570Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/cost-verify-agent-rl && CUDA_VISIBLE_DEVICES=0 python scripts/sft_train_v2.py --model_path /root/autodl-tmp/checkpoints/exp008_sft/final --data_path /root/autodl-tmp/expert_sft_v4/expert_sft_train.jsonl --val_path /root/autodl-tmp/expert_sft_v4/expert_sft_val.jsonl --output_dir /root/autodl-tmp/checkpoints/exp021_ragen_sft_v4 --learning_rate 5e-6 --num_train_epochs 2 --per_device_train_batch_size 4 --gradient_accumulation_steps 4 --max_seq_length 4096 --warmup_ratio 0.1 2>&1 | tee /root/runs/cost-verify-agent-rl/exp021_ragen_sft_v4.log\\\"\", \"server\": \"bjb1-17606\", \"gpu\": [\"cuda:0\"], \"pid\": \"406279\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp021_ragen_sft_v4.log\", \"submitted_at\": \"2026-05-15T02:09:31.617Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/expert_sft_v4/expert_sft_train.jsonl\", \"data_count\": 2546, \"model_name\": \"Qwen3-1.7B (exp008_sft checkpoint)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/exp008_sft/final\", \"eval_data\": \"RAGEN val_before_train (ALFWorld val environments, >=16 episodes)\", \"hyperparams\": {\"lr\": 5e-06, \"epochs\": 2, \"batch_size\": 4, \"grad_accum\": 4, \"max_seq_length\": 4096, \"warmup_ratio\": 0.1}, \"wall_clock_seconds\": 3938.7, \"gpu_hours\": 1.09}, \"hypothesis\": \"Two-stage SFT with RAGEN-format data (v4). From exp008_sft checkpoint, fine-tune with v4 data (RAGEN Turn/State/Reward structure, fixed system prompt with consistent &lt;answer&gt; tag instruction). LR=5e-6, 2 epochs. Validate via RAGEN val_before_train (not eval_sft_fast). Pass: RAGEN val success >= 10%, action_is_valid >= 85%.\", \"parent\": \"exp019b_expert_sft_v3\", \"reproduce\": {\"finished_at\": \"2026-05-15T02:57:51.981Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T02:57:53.576860+00:00\"}]}, \"conclusion\": \"negative\", \"metrics\": {\"train_loss_final\": 0.038, \"train_token_accuracy\": 0.988, \"train_steps\": 320, \"train_epochs\": 2, \"train_time_min\": 47.8, \"ragen_val_success\": 0.25, \"ragen_val_action_is_valid\": 0.875, \"eval_sft_fast_success\": 0, \"eval_sft_fast_format_ok\": 1, \"eval_sft_fast_action_is_valid\": 0.71, \"checkpoint_size_gb\": 3.3, \"ragen_val_success_16ep\": 0.0625, \"ragen_val_action_is_valid_16ep\": 0.6875}, \"notes\": \"D024: conclusion 降级为 negative (原 success)。16ep eval 数据: success=6.25%, action_is_valid=68.75%。原 4ep eval 的 25%/87.5% 为 unreliable_small_sample，不作为决策依据。Registry 无 inconclusive 选项，用 negative 代替。\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/exp021_ragen_sft_v4/final/\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp021_ragen_sft_v4.log\", \"completed_at\": \"2026-05-15T03:15:10.310Z\"}, \"exp024_success_gated_grpo\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:03:10.298Z\", \"updated_at\": \"2026-05-15T06:04:06.454Z\", \"hypothesis\": \"Success-gated GRPO from exp021 checkpoint. D026 终止 RAGEN GRPO 后不再适用，success-gated 不解决 context 爆炸根因。关联 D027。\", \"spec\": {\"command\": \"success-gated GRPO (never actually ran, killed before start)\", \"server\": \"bjb1-17606\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"Qwen3-1.7B (exp021 checkpoint)\", \"seed\": 42}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T06:04:05.148Z\", \"notes\": \"D027: Kill exp024 — D026 终止 RAGEN GRPO 后 success-gated 变体不再适用，不解决 context 爆炸根因。关联 D025/D026/D027。\"}, \"exp023c_grpo_serial\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T04:20:22.909Z\", \"updated_at\": \"2026-05-15T05:11:22.083Z\", \"hypothesis\": \"GRPO from exp021 RAGEN-format SFT checkpoint. Serial mode (parallel_friendly=false, max_workers=1) to avoid tatsu race. reward scale=10.0, kl_loss_coef=0.5, LR=5e-7, val env_groups=16, gpu_memory_utilization=0.6, 30 steps. Pass: success ≥ 25%, step time baseline comparison with exp022 (~208s/step).\", \"parent\": \"exp023_grpo_parallel\", \"spec\": {\"command\": \"python train.py --config-name _alfworld_exp023_grpo_parallel (serial mode: parallel_friendly=false, max_workers=1)\", \"server\": \"bjb1-17606\", \"data_path\": \"/root/autodl-tmp/expert_sft_v4/\", \"data_count\": 2546, \"model_name\": \"Qwen3-1.7B (exp021 RAGEN SFT v4 checkpoint)\", \"seed\": 0, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4\", \"eval_data\": \"ALFWorld train+val environments (RAGEN format, val env_groups=16)\", \"hyperparams\": {\"lr\": 5e-07, \"kl_loss_coef\": 0.5, \"max_grad_norm\": 1, \"total_steps\": 30, \"reward_scale\": 10, \"gpu_memory_utilization\": 0.6, \"parallel_friendly\": false, \"max_workers\": 1, \"format_penalty\": 0}}, \"metrics\": {\"val_step0_success\": 0.0625, \"val_step0_action_is_valid\": 0.6875, \"val_step0_episodes\": 16, \"train_step1_success\": 0.297, \"train_step1_action_is_valid\": 0.791, \"train_step1_entropy\": 0.0652, \"train_step1_pass16\": 0.75, \"train_step1_kl\": 0.000156, \"train_step8_success\": 0.234, \"train_step8_action_is_valid\": 0.779, \"train_step8_entropy\": 0.0555, \"train_step8_pass16\": 0.5, \"train_step8_kl\": 0.000475, \"steps_completed\": 8, \"steps_planned\": 30, \"step_time_seconds_start\": 240, \"step_time_seconds_end\": 365}, \"notes\": \"磁盘满崩溃 (step 9, /root/autodl-tmp 94% 233G/250G, OSError Errno 28)。但 8 步 metrics 趋势已显示退化：train success 29.7%→23.4%↓, pass@16 75%→50%↓, entropy 0.065→0.056↓, KL 0.00016→0.00048↑, step time 240s→365s↓。GRPO 未能在 SFT baseline 上产生改善，反而在退化。注意 step 0 val success=6.25% 与 train step 1 success=29.7% 差异大（val 用不同 game set + 16 episodes vs train 64 trajectories）。Checkpoint: global_step_5 only (save_freq=5, 第二次保存在 step 10 未到)。\", \"conclusion\": \"failed\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/exp023c/global_step_5\", \"log_path\": \"/root/autodl-tmp/checkpoints/exp023c/train.log\", \"completed_at\": \"2026-05-15T05:09:48.692Z\"}, \"exp023_grpo_parallel\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T04:06:02.056Z\", \"updated_at\": \"2026-05-15T04:12:41.878Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && ... && python train.py --config-name _alfworld_exp023_grpo_parallel ...\\\"\", \"server\": \"bjb1-17606\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"442593\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp023_grpo_parallel.log\", \"submitted_at\": \"2026-05-15T04:06:01.924Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/expert_sft_v4/\", \"data_count\": 2546, \"model_name\": \"Qwen3-1.7B (exp021 RAGEN SFT v4 checkpoint)\", \"seed\": 0, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4\", \"eval_data\": \"ALFWorld train+val environments (RAGEN format, val env_groups=16, n_groups=[16])\", \"hyperparams\": {\"lr\": 5e-07, \"kl_loss_coef\": 0.5, \"max_grad_norm\": 1, \"total_steps\": 30, \"reward_scale\": 1, \"gpu_memory_utilization\": 0.6, \"parallel_friendly\": true, \"max_workers\": 4, \"format_penalty\": 0}, \"wall_clock_seconds\": 287.6, \"gpu_hours\": 0.16}, \"hypothesis\": \"GRPO from exp021 RAGEN-format SFT checkpoint with 3 key fixes: (1) reward scale 10.0→1.0 (align with Self-Guide paper binary reward), (2) parallel rollout (max_workers=4, thread-safe env), (3) val env_groups=16 for reliable eval. kl_loss_coef=0.5, LR=5e-7, 30 steps. Pass: success ≥ 25% (maintain SFT baseline), step time < 200s (vs exp022 ~208s serial).\", \"parent\": \"exp022_grpo_from_sft_v4\", \"reproduce\": {\"finished_at\": \"2026-05-15T04:10:48.550Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T04:10:49.531Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T04:10:50.770477+00:00\"}]}, \"notes\": \"失败原因: textworld PDDL parser (tatsu) 在 val env reset 时崩溃 — tatsu.exceptions.FailedToken: expecting 'action', got template :: \\\"take {o} from {r}\\\". val env_groups=16 加载了更多 game files，触发了某个 game file 与当前 tatsu 版本不兼容的 PDDL grammar. | 已有成果: 无（val_before_train 阶段即崩溃，未开始训练） | 建议: 诊断具体哪个 game file 有问题，降低 val env_groups 或修复 game file/tatsu 兼容性\"}, \"exp022_grpo_from_sft_v4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:17:34.035Z\", \"updated_at\": \"2026-05-15T03:52:55.267Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export TMPDIR=/root/autodl-tmp/tmp/ && mkdir -p /root/autodl-tmp/tmp/ && export ALFWORLD_DATA=/root/autodl-tmp/alfworld && export RAY_memory_monitor_refresh_ms=0 && export RAY_SYSTEM_MEMORY=210000000000 && export HYDRA_FULL_ERROR=1 && mkdir -p /root/autodl-tmp/checkpoints/exp022/ && cd /root/cost-verify-agent-rl/RAGEN && sed -i 's/kl_loss_coef: 0.1/kl_loss_coef: 0.5/g' config/_alfworld_exp022_grpo_from_sft_v4.yaml && python train.py --config-name _alfworld_exp022_grpo_from_sft_v4 model_path=/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4 trainer.experiment_name=exp022-alfworld-grpo-from-sft-v4 trainer.local_log_dir=/root/autodl-tmp/checkpoints/exp022/ trainer.default_local_dir=/root/autodl-tmp/checkpoints/exp022/ es_manager.val.env_groups=8 'es_manager.val.env_configs.n_groups=[8]'\\\"\", \"server\": \"bjb1-17606\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"434853\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp022_grpo_from_sft_v4.log\", \"submitted_at\": \"2026-05-15T03:17:33.945Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/expert_sft_v4/\", \"data_count\": 2546, \"model_name\": \"Qwen3-1.7B (exp021 RAGEN SFT checkpoint)\", \"seed\": 0, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4\", \"eval_data\": \"ALFWorld train+val environments (RAGEN format, val env_groups=8)\", \"hyperparams\": {\"lr\": 5e-07, \"kl_loss_coef\": 0.5, \"max_grad_norm\": 1, \"total_steps\": 30, \"format_penalty\": 0, \"success_reward\": 10}, \"wall_clock_seconds\": 2121.3, \"gpu_hours\": 1.18}, \"hypothesis\": \"GRPO from exp021 RAGEN-format SFT checkpoint (25% RAGEN val success baseline). Sparse reward (won=10.0), LR=5e-7, kl_loss_coef=0.5 (5x stronger than exp020b to prevent entropy collapse), max_grad_norm=1.0, 30 steps, val env_groups=8. Pass: success ≥ 25% (maintain SFT baseline).\", \"parent\": \"exp021_ragen_sft_v4\", \"notes\": \"Step 0 val: success=12.5% (1/8), action_is_valid=48.75%。Step 1 完成后 kill。action_is_valid 远低于 SFT eval 结果（87.5%/68.75%），说明 RAGEN GRPO 框架中模型表现显著退化。kl_loss_coef=0.5, env_groups=8 均已确认生效。训练速度 ~208s/step。Checkpoint: global_step_1 可能已保存。\", \"conclusion\": \"killed\", \"metrics\": {\"steps_completed\": 1, \"steps_planned\": 30, \"val_step0_success\": 0.125, \"val_step0_action_is_valid\": 0.4875, \"val_step0_action_is_effective\": 1, \"val_step0_reward_mean\": 1.25, \"val_step0_reward_best\": 6.61, \"val_step0_episodes\": 8, \"step_time_seconds\": 208}, \"completed_at\": \"2026-05-15T03:52:55.268Z\"}, \"exp021_sft_ragen_format\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:35:48.559Z\", \"updated_at\": \"2026-05-15T02:11:46.204Z\", \"hypothesis\": \"Two-stage SFT with RAGEN-format data (v4). From exp008_sft checkpoint, fine-tune with v4 data (RAGEN Turn/State/Reward structure, fixed system prompt with consistent &lt;answer> tag instruction). LR=5e-6, 2 epochs. Validate via RAGEN val_before_train (not eval_sft_fast). Pass: RAGEN val success >= 10%, action_is_valid >= 85%.\", \"parent\": \"exp019b_expert_sft_v3\", \"notes\": \"被 exp021_ragen_sft_v4 取代。\", \"conclusion\": \"killed\"}, \"exp020d_grpo_from_sft\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:19:30.993Z\", \"updated_at\": \"2026-05-15T02:01:10.192Z\", \"hypothesis\": \"GRPO from exp019b SFT checkpoint (20% success baseline). Sparse reward only (won=10.0), LR=5e-7, kl_loss_coef=0.1, max_grad_norm=1.0, 30 steps. Pass: success ≥ 20%. Symlink fix for response_mask assertion (proven in exp020b). exp020c failed: Hydra key path wrong.\", \"parent\": \"exp019b_expert_sft_v3\", \"spec\": {\"command\": \"bash -c \\\"ray stop --force 2>/dev/null; sleep 5; ln -sfn /root/autodl-tmp/checkpoints/exp019b_expert_sft_v3/final /root/autodl-tmp/checkpoints/qwen3_exp019b_sft && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export TMPDIR=/root/autodl-tmp/tmp/ && mkdir -p /root/autodl-tmp/tmp/ && export ALFWORLD_DATA=/root/autodl-tmp/alfworld && export RAY_memory_monitor_refresh_ms=0 && export RAY_SYSTEM_MEMORY=210000000000 && export HYDRA_FULL_ERROR=1 && mkdir -p /root/autodl-tmp/checkpoints/exp020d/ && cd /root/cost-verify-agent-rl/RAGEN && python train.py --config-name _alfworld_exp018_sft_grpo model_path=/root/autodl-tmp/checkpoints/qwen3_exp019b_sft trainer.experiment_name=exp020d-alfworld-sft-grpo trainer.local_log_dir=/root/autodl-tmp/checkpoints/exp020d/ trainer.default_local_dir=/root/autodl-tmp/checkpoints/exp020d/ es_manager.val.env_groups=4 'es_manager.val.env_configs.n_groups=[4]'\\\"\", \"server\": \"bjb1-17606\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"390605\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp020d_grpo_from_sft.log\", \"submitted_at\": \"2026-05-14T22:19:42.442Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"failed\", \"notes\": \"D022 废弃。exp020b 确认 GRPO from SFT 因 RAGEN 格式不兼容导致 val success = 0%。exp020c/d 同样会遇到此问题。改走 exp021（RAGEN 格式 SFT 数据重训）。\"}, \"exp020c_grpo_from_sft\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:15:37.659Z\", \"updated_at\": \"2026-05-15T02:01:08.768Z\", \"hypothesis\": \"GRPO from exp019b SFT checkpoint (20% success baseline). Sparse reward only (won=10.0), LR=5e-7, kl_loss_coef=0.1, max_grad_norm=1.0, 30 steps. Pass: success ≥ 20%. Fix: symlink + enable_response_mask=false (exp020/020b crashed on response_mask assertion).\", \"parent\": \"exp019b_expert_sft_v3\", \"spec\": {\"command\": \"bash -c \\\"ln -sfn /root/autodl-tmp/checkpoints/exp019b_expert_sft_v3/final /root/autodl-tmp/checkpoints/qwen3_exp019b_sft && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export TMPDIR=/root/autodl-tmp/tmp/ && mkdir -p /root/autodl-tmp/tmp/ && export ALFWORLD_DATA=/root/autodl-tmp/alfworld && export RAY_memory_monitor_refresh_ms=0 && export RAY_SYSTEM_MEMORY=210000000000 && export HYDRA_FULL_ERROR=1 && mkdir -p /root/autodl-tmp/checkpoints/exp020c/ && cd /root/cost-verify-agent-rl/RAGEN && python train.py --config-name _alfworld_exp018_sft_grpo model_path=/root/autodl-tmp/checkpoints/qwen3_exp019b_sft trainer.experiment_name=exp020c-alfworld-sft-grpo trainer.local_log_dir=/root/autodl-tmp/checkpoints/exp020c/ trainer.default_local_dir=/root/autodl-tmp/checkpoints/exp020c/ actor_rollout_ref.model.enable_response_mask=false es_manager.val.env_groups=4 'es_manager.val.env_configs.n_groups=[4]'\\\"\", \"server\": \"bjb1-17606\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"389983\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp020c_grpo_from_sft.log\", \"submitted_at\": \"2026-05-14T22:15:49.190Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"failed\", \"notes\": \"D022 废弃。exp020b 确认 GRPO from SFT 因 RAGEN 格式不兼容导致 val success = 0%。exp020c/d 同样会遇到此问题。改走 exp021（RAGEN 格式 SFT 数据重训）。\"}, \"exp020b_grpo_from_sft\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:12:38.928Z\", \"updated_at\": \"2026-05-15T02:00:56.016Z\", \"hypothesis\": \"GRPO from exp019b SFT checkpoint (20% success baseline). Sparse reward only (won=10.0), LR=5e-7, kl_loss_coef=0.1, max_grad_norm=1.0, 30 steps. Pass: success ≥ 20%. Fix: symlink with \\\"qwen\\\" in path to pass response_mask assertion (exp020 crashed on this).\", \"parent\": \"exp019b_expert_sft_v3\", \"spec\": {\"command\": \"python train.py --config-name _alfworld_exp018_sft_grpo\", \"server\": \"bjb1-17606\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"385977\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp020b_grpo_from_sft.log\", \"submitted_at\": \"2026-05-14T22:12:49.413Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/expert_sft_v3/\", \"data_count\": 2460, \"model_name\": \"Qwen3-1.7B (exp019b SFT checkpoint)\", \"seed\": 0, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/qwen3_exp019b_sft\", \"eval_data\": \"ALFWorld train+val environments\", \"wall_clock_seconds\": 10144.0, \"gpu_hours\": 5.64}, \"conclusion\": \"negative\", \"metrics\": {\"steps_completed\": 22, \"steps_planned\": 30, \"hung_at_step\": 23, \"step1_train_success\": 0.1875, \"step10_train_success\": 0.1875, \"step20_train_success\": 0.125, \"step22_train_success\": 0.0469, \"val_success_step0\": 0, \"val_success_step20\": 0, \"entropy_initial\": 0.107, \"entropy_final\": 0.042, \"grad_norm_initial\": 2.78, \"grad_norm_step20\": 5.58, \"ppo_kl_final\": 0.00918, \"pass_at_16_step1\": 0.75, \"pass_at_16_step22\": 0.25, \"checkpoint_latest\": \"global_step_20\", \"training_status\": \"hung_at_step23_rollout\"}, \"notes\": \"Negative 结论：GRPO from SFT 导致策略坍缩。训练 22/30 步后卡死在 step 23 rollout（环境交互死锁，GPU 0% 利用率但显存仍占 40GB×2）。关键指标全线恶化：train success 18.75%→4.69%（远低于 SFT baseline 20%），val success 始终 0%，entropy 0.107→0.042（坍缩 61%），pass@16 从 75%降到 25%。GRPO 不仅未提升 SFT 性能，反而严重退化。根因分析：sparse reward（won=10.0）学习信号不足以维持 SFT 学到的 task knowledge，KL coef=0.1 不足以约束策略偏移。Checkpoint: /root/autodl-tmp/checkpoints/exp020b/global_step_20/\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/exp020b/global_step_20/\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp020b_grpo_from_sft.log\", \"completed_at\": \"2026-05-15T01:01:53.408Z\"}, \"exp020_grpo_from_sft\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:07:16.290Z\", \"updated_at\": \"2026-05-14T22:11:05.341Z\", \"hypothesis\": \"GRPO from exp019b SFT checkpoint (20% success baseline) can maintain or improve success rate. Sparse reward only (won=10.0), LR=5e-7, kl_loss_coef=0.1, max_grad_norm=1.0, 30 steps. Pass: success ≥ 20%.\", \"parent\": \"exp019b_expert_sft_v3\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export TMPDIR=/root/autodl-tmp/tmp/ && mkdir -p \\\\$TMPDIR && export ALFWORLD_DATA=/root/autodl-tmp/alfworld && export RAY_memory_monitor_refresh_ms=0 && export RAY_SYSTEM_MEMORY=210000000000 && export HYDRA_FULL_ERROR=1 && export CUDA_VISIBLE_DEVICES=0,1 && mkdir -p /root/autodl-tmp/checkpoints/exp020/ && cd /root/cost-verify-agent-rl/RAGEN && python train.py --config-name _alfworld_exp018_sft_grpo model_path=/root/autodl-tmp/checkpoints/exp019b_expert_sft_v3/final trainer.experiment_name=exp020-alfworld-sft-grpo trainer.local_log_dir=/root/autodl-tmp/checkpoints/exp020/ trainer.default_local_dir=/root/autodl-tmp/checkpoints/exp020/ es_manager.val.env_groups=4 'es_manager.val.env_configs.n_groups=[4]'\\\"\", \"server\": \"bjb1-17606\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"385383\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp020_grpo_from_sft.log\", \"submitted_at\": \"2026-05-14T22:08:41.040Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 41.7, \"gpu_hours\": 0.02}, \"reproduce\": {\"finished_at\": \"2026-05-14T22:09:21.956Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T22:09:22.710Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T22:09:23.776796+00:00\"}]}, \"notes\": \"失败原因: AssertionError at train.py:137 — model_path=/root/autodl-tmp/checkpoints/exp019b_expert_sft_v3/final 不含 \\\"qwen\\\" 字符串，enable_response_mask=true 断言失败。模型实际是 Qwen3-1.7B 微调 checkpoint，路径命名问题。error_type=infrastructure | 建议: 创建含 \\\"qwen\\\" 的 symlink 或添加 enable_response_mask=false override 后重提交\"}, \"exp019c_expert_sft_v3\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:03:02.685Z\", \"updated_at\": \"2026-05-14T21:05:37.494Z\", \"hypothesis\": \"Two-stage Expert SFT（重试）: 从 exp008_sft checkpoint 出发，用 v3 数据（保留原始 move actions + admissible actions augmentation）微调。LR=5e-6, 2 epochs, batch=4, grad_accum=4, max_seq=4096。Pass: success ≥ 10%, format_ok ≥ 90%, action_is_valid ≥ 85%。\", \"parent\": \"exp019b_expert_sft_v3\", \"spec\": {\"command\": \"bash -c \\\"rm -rf /root/autodl-tmp/checkpoints/exp019b_expert_sft_v3 && > /root/runs/cost-verify-agent-rl/exp019b_expert_sft_v3.log && cd /root/cost-verify-agent-rl && bash scripts/run_exp019b.sh\\\"\", \"server\": \"bjb1-17606\", \"gpu\": [\"cuda:0\"], \"pid\": \"unknown\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp019c_expert_sft_v3.log\", \"submitted_at\": \"2026-05-14T21:03:15.877Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"notes\": \"废弃。submit_training_job 因 GPU 被占（exp019b nohup 进程仍在跑）EXIT_CODE=1 退出。实际训练由 exp019b 的 nohup 进程完成。\", \"conclusion\": \"killed\"}, \"exp019_expert_sft_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T16:38:05.515Z\", \"updated_at\": \"2026-05-14T17:11:09.024Z\", \"spec\": {\"hypothesis\": \"两阶段 SFT：从 exp008_sft checkpoint（format_ok=100%, action_is_valid=90%）出发，用格式修复后的 expert trajectory 数据微调。降低 LR=5e-6（防遗忘 format），2 epochs。目标：success ≥ 10% 且 format_ok ≥ 90%。\", \"parent\": \"exp008_sft\", \"model_name\": \"Qwen3-1.7B\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/exp008_sft/final\", \"command\": \"bash scripts/run_exp019.sh\", \"server\": \"bjb1-17606\", \"data_path\": \"/root/autodl-tmp/expert_sft_v2/expert_sft_train.jsonl\", \"data_count\": 2460, \"seed\": 42, \"description\": \"D018: B+C 方案 — move→put 修复 + 从 exp008_sft checkpoint 微调, LR=5e-6, 2 epochs\"}, \"server\": \"bjb1-17606\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-17606\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-14T16:47:11.532Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/cost-verify-agent-rl && bash scripts/run_exp019.sh\\\"\", \"finished_at\": \"2026-05-14T16:57:30.058Z\", \"training_hours\": 0.17}, \"pid\": \"366040\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp019_expert_sft_v2.log\", \"conclusion\": \"killed\", \"notes\": \"D019 kill：move→put 替换方向错误。ALFWorld admissible_commands 包含 move X to Y，不含 put。用 put 替换的数据会使 action_is_valid 更差。改用原始 expert data（保留 move）+ admissible actions augmentation。\", \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-14T16:57:30.447Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T16:57:31.467540+00:00\"}]}, \"checkpoint_path\": \"INVALID — move→put 错误数据训练，已标记 _INVALID\"}, \"exp019b_expert_sft_v2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T16:49:30.246Z\", \"updated_at\": \"2026-05-14T16:49:30.246Z\", \"spec\": {\"hypothesis\": \"两阶段 SFT：从 exp008_sft checkpoint（format_ok=100%, action_is_valid=90%）出发，用原始 expert data（保留 move X to Y）+ admissible actions augmentation 微调。LR=5e-6, 2 epochs。目标：success ≥ 10% 且 format_ok ≥ 90%。\", \"parent\": \"exp008_sft\", \"model_name\": \"Qwen3-1.7B\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/exp008_sft/final\", \"description\": \"D019: 修正版 — 原始 expert data (保留 move) + admissible actions + 从 exp008_sft checkpoint 微调\"}}, \"exp018_sft_grpo\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:43:08.545Z\", \"updated_at\": \"2026-05-14T16:45:33.314Z\", \"hypothesis\": \"Expert SFT → Sparse GRPO：从 exp017 SFT checkpoint 开始纯 sparse GRPO 训练。SFT 提升 baseline success rate（≥10%），使 GRPO 有足够非零 reward group 产生有效梯度。LR=5e-7, kl_loss_coef=0.1, max_grad_norm=1.0, won=10.0, 无 bonus/penalty, GRPO 30 步。Pass: success ≥ 20%。\", \"parent\": \"exp017_expert_sft\", \"conclusion\": \"killed\", \"notes\": \"D018 取消：exp017 eval 5% success 与 base 4.7% 差异太小，GRPO 大概率重蹈覆辙。等 exp019 v2 SFT（修复 move→put + admissible actions 数据增强）后再考虑 GRPO。\"}, \"exp017_expert_sft\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:36:28.291Z\", \"updated_at\": \"2026-05-14T16:36:17.637Z\", \"hypothesis\": \"Expert SFT: 用 PDDL expert trajectory 数据 SFT Qwen3-1.7B instruct 模型，提升 ALFWorld baseline success rate，为后续 GRPO 提供更好的冷启动点。LR=2e-5, 3 epochs, batch_size=4, grad_accum=4。Pass 标准: success ≥ 10%。\", \"parent\": \"exp008_sft\", \"spec\": {\"command\": \"bash scripts/run_expert_sft.sh\", \"server\": \"bjb1-17606\", \"data_path\": \"/root/autodl-tmp/expert_trajectories/sft_data/train.jsonl\", \"data_count\": 2460, \"model_name\": \"Qwen3-1.7B\", \"seed\": 42, \"checkpoint_source\": \"Qwen/Qwen3-1.7B (original instruct)\", \"eval_data\": \"ALFWorld 134 tasks eval after SFT\"}, \"conclusion\": \"success\", \"metrics\": {\"final_train_loss\": 0.1434, \"final_step_loss\": 0.04, \"final_token_accuracy\": 0.983, \"epochs\": 3, \"total_steps\": 462, \"training_time_min\": 26, \"data_count_train\": 2460, \"data_count_val\": 129, \"checkpoint_size_gb\": 3.44, \"eval_success_rate\": 0.05, \"eval_success\": \"1/20\", \"eval_action_is_valid\": 0.638, \"eval_format_ok\": 0.75, \"eval_avg_steps\": 22, \"eval_time_s\": 149.6, \"eval_per_task\": {\"put\": \"0/10\", \"clean\": \"0/4\", \"cool\": \"1/3\", \"heat\": \"0/2\", \"examine\": \"0/1\"}, \"eval_parse_failures\": \"5/20 episodes (EP 7/12/16/17/18)\"}, \"notes\": \"训练成功完成。Expert PDDL trajectory 2460 条 SFT Qwen3-1.7B，3 epochs 462 steps 26 min。Final loss=0.1434。Checkpoint: /root/autodl-tmp/checkpoints/exp017_expert_sft/final/ (3.44GB)。\\n\\nEval 结果（20 episodes, vLLM 推理, max_steps=30）：success=5% (1/20), action_is_valid=63.8%, format_ok=75%。唯一成功是 1 个 cool 任务（EP 8, 15 步）。5/20 episodes parse 失败（1 步即退出）。put 任务 0/10 全失败。\\n\\n对比 exp008_sft（1200 条普通 SFT）：action_is_valid 90%→63.8%（下降！）, format_ok 100%→75%（下降！）, success 0%→5%（略升）。Expert data SFT 提升了 success 但 format/valid 反而退步，可能因为 expert trajectory 格式与 RAGEN 的 &lt;think>/&lt;answer> 格式不完全匹配。\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/exp017_expert_sft/final/\", \"log_path\": \"/root/runs/cost-verify-agent-rl/exp017_expert_sft.log\", \"reproduce\": {\"finished_at\": \"2026-05-14T16:13:13.399Z\"}, \"failure_reason\": \"\", \"completed_at\": \"2026-05-14T16:13:13.805Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T16:13:17.574000+00:00\"}]}}, \"exp016\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:44:58.883Z\", \"updated_at\": \"2026-05-14T15:36:27.432Z\", \"hypothesis\": \"LR 折中方案：LR=5e-7（exp012b 1e-6 collapse vs exp015 1e-7 零梯度的中间值）。kl_loss_coef=0.1, max_grad_norm=1.0 保持。纯 sparse reward（won=10.0，无 bonus，无 format_penalty）。从 exp015/global_step_5 checkpoint 恢复，GRPO 30 步。\", \"parent\": \"exp015\", \"server\": \"bjb1-17606\", \"gpu\": \"cuda:0,cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-17606\", \"gpu\": \"cuda:0,cuda:1\", \"started_at\": \"2026-05-14T13:52:42.492Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && bash /root/cost-verify-agent-rl/scripts/run_exp016.sh\\\"\", \"finished_at\": \"2026-05-14T15:04:04.459Z\", \"training_hours\": 1.19}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && bash /root/cost-verify-agent-rl/scripts/run_exp016.sh\\\"\", \"server\": \"bjb1-17606\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"343927\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp016.log\", \"submitted_at\": \"2026-05-14T13:53:45.002Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 4219.8, \"gpu_hours\": 2.34}, \"pid\": \"343927\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp016.log\", \"metrics\": {\"step\": 12, \"total_steps\": 30, \"elapsed_min\": 51, \"step6_success\": 0, \"step6_action_is_valid\": 0.521, \"step6_pg_loss\": 0, \"step6_grad_norm\": 0.841, \"step7_success\": 0.047, \"step7_pass_at16\": 0.5, \"step7_action_is_valid\": 0.655, \"step10_success\": 0, \"step10_action_is_valid\": 0.664, \"step10_pg_loss\": 0, \"step10_grad_norm\": 0.856, \"step10_entropy\": 0.1046, \"step10_ppo_kl\": -9.1e-05, \"all_raw_rewards\": 0, \"all_advantages\": 0, \"all_returns\": 0, \"reward_signal\": \"BROKEN — success episodes get reward=0\", \"action_is_valid_trend\": \"52.1%→65.5%→66.4%\", \"manager_invalid_action_trend\": \"13.5%→11.2%→9.6%\"}, \"conclusion\": \"failed\", \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-14T15:04:04.809Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T15:04:05.813843+00:00\"}]}, \"notes\": \"D015 kill。训练 12 步，pg_loss 恒为 0。原因：base success ~4.7%（仅 val，train temperature=1.0 下接近 0%），纯 sparse reward 下 GRPO 无有效学习信号。raw_reward=0 是日志 artifact（info dict 缺 raw_reward 字段），实际训练 reward pipeline 正常（critic/score 正确传递，step 7 score/mean=0.46875=3/64×10.0）。NaiveRewardManager 是 pass-through，不覆盖 env reward。LR=5e-7 本身无问题，根因是 sparse reward 冷启动。\"}, \"exp015\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:48:38.065Z\", \"updated_at\": \"2026-05-14T13:44:57.940Z\", \"hypothesis\": \"Sparse GRPO + 训练稳定性修复。纯 sparse reward（won=10.0，无 valid_action_bonus，无 format_penalty）。针对 exp012b 的 step 7 catastrophic collapse（grad_norm 1.48→0.094），三项修复：LR 1e-7（降 10 倍防单步更新过激）、kl_loss_coef 0.1（增 10 倍约束策略偏移）、max_grad_norm=1.0（梯度裁剪）。从 exp008 step 5 checkpoint 恢复，GRPO 30 步。\", \"parent\": \"exp012b\", \"notes\": \"D014 kill。Steps 3-5 连续零梯度（pg_loss=0, grad_norm~0），LR=1e-7 过保守导致无有效学习。Step 0 val: action_is_valid=85.8%, success=0%。训练稳定性修复验证成功（无 catastrophic collapse），但学习率不足以产生有意义的 policy update。Checkpoint: global_step_5 已保存，供 exp016 恢复。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && bash /root/cost-verify-agent-rl/scripts/run_exp015.sh\\\"\", \"server\": \"bjb1-17606\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"334692\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp015.log\", \"submitted_at\": \"2026-05-14T12:57:59.726Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 2818.2, \"gpu_hours\": 1.57}, \"server\": \"bjb1-17606\", \"gpu\": \"cuda:0,cuda:1\", \"pid\": \"334692\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp015.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && bash /root/cost-verify-agent-rl/scripts/run_exp015.sh\\\"\", \"code_commit\": \"a6d0501af3c3936f11932b3735a7c9c85d2bc9ee\"}, \"metrics\": {\"step\": 1, \"total_steps\": 30, \"val_step0_success\": 0, \"val_step0_action_is_valid\": 0.858, \"val_step0_pass_at1\": 0, \"val_step0_episodic_return\": 0, \"val_step0_response_length\": 2797.5, \"val_train_transition\": \"passed\", \"estimated_total_time_min\": 163, \"time_per_step_min\": 5.6}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T13:44:57.940Z\"}, \"exp014b\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:45:27.876Z\", \"updated_at\": \"2026-05-14T12:48:37.433Z\", \"hypothesis\": \"极低 Dense Reward: valid_action_bonus=0.01（1:1000 比例），测试极弱 bonus 能否防 collapse 又不引发 gaming。如果 bonus 弱到不影响 GRPO reward ranking，模型不会被诱导走捷径。success_reward=10.0, format_penalty=0, 从 exp008 step 5 checkpoint 恢复, GRPO 30 步。\", \"parent\": \"exp013f\", \"conclusion\": \"killed\", \"notes\": \"D013 撤销：Director 修订决策，改为 exp015。exp014b 等 exp015 结果后再决定。\"}, \"exp014a\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:45:27.347Z\", \"updated_at\": \"2026-05-14T12:48:35.102Z\", \"hypothesis\": \"Success-Gated Dense Reward: valid_action_bonus=0.15 只在 group 内至少一条 trajectory success 时才给。消除 reward gaming 的独立最大化路径——没有 success 就没有 bonus，模型必须探索 success。success_reward=10.0, format_penalty=0, 从 exp008 step 5 checkpoint 恢复, GRPO 30 步。\", \"parent\": \"exp013f\", \"conclusion\": \"killed\", \"notes\": \"D013 撤销：Director 修订决策，success-gated bonus 有 bootstrap 问题（初始 success=0 时 bonus 永远为 0，退化为 sparse reward），改为 exp015 纯 sparse GRPO + 训练稳定性修复。\"}, \"exp014c\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:45:21.231Z\", \"updated_at\": \"2026-05-14T12:45:25.025Z\", \"hypothesis\": \"Success-gated valid_action_bonus：bonus 仅在 episode 成功时累加到 reward，消除独立最大化路径。valid_action_bonus=0.15, success_reward=10.0。解决 exp013f reward gaming（unconditional bonus 导致 agent 放弃 success 追求 valid action）。从 step 5 checkpoint 恢复 GRPO 30 步。\", \"parent\": \"exp013f\"}, \"exp013e\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T09:02:52.837Z\", \"updated_at\": \"2026-05-14T09:21:08.911Z\", \"hypothesis\": \"exp013d 基础设施修复重试。Ray object_store_memory 改用 Hydra config override (ray_kwargs.ray_init.object_store_memory=32212254720) 替代无效的环境变量。其余同 exp013d: dense reward shaping (valid_action_bonus=0.15, kl_loss_coef=0.01, success_reward=10.0), env_groups=4, 从 step 5 checkpoint 恢复。\", \"parent\": \"exp013d\", \"spec\": {\"command\": \"python train.py --config-name _alfworld_exp013b_dense_reward trainer.experiment_name=exp013e-alfworld-dense-reward trainer.local_log_dir=/root/autodl-tmp/checkpoints/exp013e/ trainer.default_local_dir=/root/autodl-tmp/checkpoints/exp013e/\", \"server\": \"bjb1-17606\", \"data_path\": \"AlfworldSG_Dense (3553 train games)\", \"data_count\": 3553, \"model_name\": \"Qwen3-1.7B SFT (exp008_sft/final)\", \"seed\": 10000, \"pid\": 298696, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/exp013e/\", \"log_path\": \"/tmp/exp013e.log\", \"description\": \"Dense reward GRPO with Ray object_store_memory fix (30GB). Resume from exp008_grpo step 5. valid_action_bonus=0.15, kl_loss_coef=0.01, format_penalty=0, env_groups=4.\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/exp008_grpo/global_step_5\", \"eval_data\": \"N/A - training experiment\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T09:19:20.818Z\", \"notes\": \"ActorUnavailableError: RPC error: Socket closed rpc_code: 14。validation step 5 完成后向 training step 6 过渡时崩溃。诊断排除: cgroup OOM (oom_kill=0)、系统 OOM (dmesg 无记录)、CUDA OOM (无日志)、磁盘满 (118GB剩余)。Ray worker 日志被 ray stop --force 清除，最可能原因: vLLM worker 在 val→train 切换时的内存峰值或内部错误。object_store_memory=30GB 设置正确(train.py:203)。validation 指标: success=0, action_is_valid=0.656, reward_mean=2.953, reward_std=1.608。结论: 瞬态崩溃，可安全重提交。建议加 HYDRA_FULL_ERROR=1。\"}, \"exp013d\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:34:37.036Z\", \"updated_at\": \"2026-05-14T08:52:25.371Z\", \"hypothesis\": \"exp013b/c 内存修复重试。Dense reward shaping (valid_action_bonus=0.15) 已验证有效 (reward_std=1.608>0)。修复: env_groups 8→4 (64并发, 峰值~158GB < 220GB cgroup限制) + RAY_object_store_memory=30GB。\", \"parent\": \"exp013c\", \"notes\": \"RAY_object_store_memory env var 未生效，Ray 仍分配 70.36GB object store（默认值）。env_groups=4 生效但不够。Raylet 被 cgroup OOM killer SIGKILL。修复: 用 Hydra config override ray_kwargs.ray_init.object_store_memory=32212254720 显式传给 ray.init()。\", \"server\": \"bjb1-17606\", \"gpu\": \"cuda:0,cuda:1\", \"account\": \"root\", \"spec\": {\"command\": \"python train.py --config-name _alfworld_exp013b_dense_reward\", \"server\": \"bjb1-17606\", \"gpu\": \"cuda:0,cuda:1\", \"data_path\": \"/root/autodl-tmp/alfworld/\", \"data_count\": 3553, \"model_name\": \"Qwen3-1.7B (SFT warmup, resumed from GRPO step 5)\", \"seed\": 10000, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/exp008_grpo/global_step_5/\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp013d.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/exp013b_grpo/\", \"config\": \"_alfworld_exp013b_dense_reward.yaml\", \"hyperparams\": {\"valid_action_bonus\": 0.15, \"success_reward\": 10, \"format_penalty\": 0, \"kl_loss_coef\": 0.01, \"lr\": 1e-06, \"group_size\": 16, \"train_env_groups\": 4, \"RAY_object_store_memory\": \"30GB\"}}, \"pid\": \"272157\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp013d.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export TMPDIR=/root/autodl-tmp/tmp/ && mkdir -p \\\\$TMPDIR && export ALFWORLD_DATA=/root/autodl-tmp/alfworld && export RAY_object_store_memory=30000000000 && cd /root/cost-verify-agent-rl/RAGEN && python train.py --config-name _alfworld_exp013b_dense_reward\\\"\", \"finished_at\": \"2026-05-14T08:37:22.538Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T08:37:23.463Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T08:37:24.501932+00:00\"}]}}, \"exp013c\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:30:44.623Z\", \"updated_at\": \"2026-05-14T08:34:10.517Z\", \"hypothesis\": \"exp013b 基础设施重试。Dense reward shaping (valid_action_bonus=0.15 + success=10.0) 已验证有效 (reward_std=1.608>0)。exp013b 因 OOM/Ray 崩溃，非算法问题。\", \"parent\": \"exp013b\", \"notes\": \"预防性kill。诊断确认 exp013b 崩溃根因: cgroup 内存限制 220GB, Ray object_store 70GB + memory 164GB = 234GB 超限。128并发ALFWorld游戏(8 env_groups × 16 group_size)在 step 6 rollout 触发 Plasma mmap ENOMEM。exp013c 同配置会重现。修复: env_groups 8→4 + RAY_object_store_memory=30GB。\", \"server\": \"bjb1-17606\", \"gpu\": \"cuda:0,cuda:1\", \"account\": \"root\", \"spec\": {\"command\": \"python train.py --config-name _alfworld_exp013b_dense_reward\", \"server\": \"bjb1-17606\", \"gpu\": \"cuda:0,cuda:1\", \"data_path\": \"/root/autodl-tmp/alfworld/\", \"data_count\": 3553, \"model_name\": \"Qwen3-1.7B (SFT warmup, resumed from GRPO step 5)\", \"seed\": 10000, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/exp008_grpo/global_step_5/\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp013c.log\", \"checkpoint_path\": \"none\", \"config\": \"_alfworld_exp013b_dense_reward.yaml\", \"hyperparams\": {\"valid_action_bonus\": 0.15, \"success_reward\": 10, \"format_penalty\": 0, \"kl_loss_coef\": 0.01, \"lr\": 1e-06, \"group_size\": 16}}, \"pid\": \"264217\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp013c.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export TMPDIR=/root/autodl-tmp/tmp/ && mkdir -p \\\\$TMPDIR && export ALFWORLD_DATA=/root/autodl-tmp/alfworld && cd /root/cost-verify-agent-rl/RAGEN && python train.py --config-name _alfworld_exp013b_dense_reward\\\"\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T08:34:10.517Z\"}, \"exp013b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:15:44.247Z\", \"updated_at\": \"2026-05-14T08:27:21.850Z\", \"hypothesis\": \"Dense reward shaping: valid_action_bonus=0.15 per valid action + success_reward=10.0 + kl_loss_coef=0.01。每步有效动作获得 0.15 奖励提供持续 GRPO 学习信号（30步累计上限4.5 vs 终局10.0），KL 约束防止 policy 过激更新。format_penalty=0，从 step 5 checkpoint 恢复 GRPO 30 步。\", \"parent\": \"exp013\", \"notes\": \"Dense reward shaping 有效性已确认：val reward_mean=2.953, reward_std=1.608 (>0)。崩溃是基础设施问题（OOM/Ray），非算法问题。清理后重试。超参: valid_action_bonus=0.15, kl_loss_coef=0.01, success_reward=10.0, format_penalty=0, group_size=16。\", \"server\": \"bjb1-17606\", \"gpu\": \"cuda:0,cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-17606\", \"gpu\": \"cuda:0,cuda:1\", \"started_at\": \"2026-05-14T08:17:09.149Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export TMPDIR=/root/autodl-tmp/tmp/ && mkdir -p \\\\$TMPDIR && export ALFWORLD_DATA=/root/autodl-tmp/alfworld && cd /root/cost-verify-agent-rl/RAGEN && python train.py --config-name _alfworld_exp013b_dense_reward\\\"\", \"finished_at\": \"2026-05-14T08:24:45.209Z\", \"training_hours\": 0.13}, \"spec\": {\"command\": \"python train.py --config-name _alfworld_exp013b_dense_reward\", \"server\": \"bjb1-17606\", \"gpu\": \"cuda:0,cuda:1\", \"data_path\": \"/root/autodl-tmp/alfworld/\", \"data_count\": 3553, \"model_name\": \"Qwen3-1.7B (SFT warmup, resumed from GRPO step 5)\", \"seed\": 10000, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/exp008_grpo/global_step_5/\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp013b.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/exp013b_grpo/\", \"config\": \"_alfworld_exp013b_dense_reward.yaml\", \"hyperparams\": {\"valid_action_bonus\": 0.15, \"success_reward\": 10, \"format_penalty\": 0, \"kl_loss_coef\": 0.01, \"lr\": 1e-06, \"group_size\": 16}}, \"pid\": \"258987\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp013b.log\", \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T08:24:46.177Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T08:24:47.218414+00:00\"}]}}, \"exp013\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:02:52.275Z\", \"updated_at\": \"2026-05-14T08:04:35.100Z\", \"hypothesis\": \"Dense reward shaping (valid_action_bonus=0.5 + success_reward=10.0) 解决 sparse binary reward 冷启动死锁。每步有效动作获得 0.5 奖励提供持续学习信号，终局 success 保留 10.0 大奖引导任务完成。\", \"parent\": \"exp012b\", \"notes\": \"D011驳回纯KL方案。Director要求dense reward shaping: valid_action_bonus=0.5 + success_reward=10.0 (1:20比值)。需改reward function代码（env.py或es_manager.py），不只是yaml config。format_penalty=0保持，从step 5恢复。\", \"conclusion\": \"killed\", \"spec\": {\"checkpoint_path\": \"none\", \"log_path\": \"none\"}, \"completed_at\": \"2026-05-14T08:04:35.100Z\"}, \"exp012b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T06:44:22.570Z\", \"updated_at\": \"2026-05-14T07:57:46.417Z\", \"hypothesis\": \"format_penalty=0 + group_size=16，从 step 5 checkpoint 恢复 GRPO 训练。纯 A2 实验（D010）：隔离 format penalty 对 success 崩塌的影响。exp012 的基础设施修复重试（vLLM 参数兼容已修复）。\", \"parent\": \"exp012\", \"notes\": \"D011 kill。step 6 success=8.59%（优于 exp010 的 4.7%），但 step 7 catastrophic collapse: success→0%, grad_norm 1.48→0.09, pg_loss→0。根因：GRPO 单步 policy update 过激，跳出有 success 的分布区域。Reward fix (format_penalty=0) 延缓了 1 步但未解决根因。下一步 exp013: 降 LR 1e-6 + kl_coef 0.05 稳定训练。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export TMPDIR=/root/autodl-tmp/tmp/ && mkdir -p \\\\$TMPDIR && export ALFWORLD_DATA=/root/autodl-tmp/alfworld && cd /root/cost-verify-agent-rl/RAGEN && python train.py --config-name _alfworld_exp012_reward_fix\\\"\", \"server\": \"bjb1-17606\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"233689\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp012b.log\", \"submitted_at\": \"2026-05-14T06:45:43.279Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/exp012_grpo/\", \"wall_clock_seconds\": 4293.6, \"gpu_hours\": 2.39}, \"server\": \"bjb1-17606\", \"gpu\": \"cuda:0,cuda:1\", \"account\": \"root\", \"pid\": \"233689\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp012b.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export TMPDIR=/root/autodl-tmp/tmp/ && mkdir -p \\\\$TMPDIR && export ALFWORLD_DATA=/root/autodl-tmp/alfworld && cd /root/cost-verify-agent-rl/RAGEN && python train.py --config-name _alfworld_exp012_reward_fix\\\"\", \"code_commit\": \"20daedc47558e000f7de912b060646bf2e8026bd\"}, \"metrics\": {\"step\": 8, \"total_steps\": 30, \"step6_success\": 0.0859, \"step6_action_is_valid\": 0.613, \"step6_pass_at_16\": 0.5, \"step6_ppo_kl\": 0.0039, \"step6_entropy\": 0.1006, \"step6_grad_norm\": 1.477, \"step7_success\": 0, \"step7_action_is_valid\": 0.685, \"step7_pass_at_16\": 0, \"step7_pg_loss\": 0, \"step7_ppo_kl\": 0.00439, \"step7_entropy\": 0.0904, \"step7_grad_norm\": 0.094, \"trend\": \"success 8.6%→0% collapse at step 7 (same pattern as exp010, delayed 1 step). grad_norm 1.477→0.094, pg_loss→0. Reward fix delayed but did not prevent collapse.\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T07:57:16.833Z\"}, \"exp012\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T06:24:24.322Z\", \"updated_at\": \"2026-05-14T06:32:18.431Z\", \"hypothesis\": \"format_penalty=0 + group_size=16 解决 exp010/011 中 format penalty 劫持 GRPO 梯度导致 success 崩塌的问题。从 step 5 checkpoint 恢复，预期 success rate 能持续上升而非崩塌。\", \"parent\": \"exp011\", \"notes\": \"D010指令：纯A2实验，隔离变量。format_penalty=0（非-0.01），不含valid-action bonus，env.py保持原始二值reward（won=10.0/otherwise 0）。group_size=16, resume from step 5。\\n\\n失败原因: vLLM 版本兼容问题。agent_proxy.py:69 传 `disable_mm_preprocessor_cache` 给 vLLM LLM()，但服务器安装的 vLLM 版本不支持此参数。TypeError at EngineArgs.__init__()。启动即崩溃，无训练数据。\\n\\n诊断 Worker: worker_diagnose_exp012_20260514T063149 正在修复。error_type=infrastructure。\", \"server\": \"bjb1-17606\", \"gpu\": \"cuda:0,cuda:1\", \"account\": \"root\", \"spec\": {\"command\": \"python -m ragen.llm_agent.agent_proxy --config-name _alfworld_exp012_reward_fix\", \"server\": \"bjb1-17606\", \"gpu\": \"cuda:0,cuda:1\", \"data_path\": \"/root/autodl-tmp/alfworld/\", \"data_count\": 3553, \"model_name\": \"Qwen3-1.7B (SFT warmup, resumed from GRPO step 5)\", \"seed\": 10000, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/exp008_grpo/global_step_5/\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp012.log\", \"checkpoint_path\": \"none\", \"config\": \"_alfworld_exp012_reward_fix.yaml\", \"changes_from_parent\": \"format_penalty: -0.1→0, group_size: 8→16, resume from step 5 instead of step 10\"}, \"pid\": \"221683\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp012.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export TMPDIR=/root/autodl-tmp/tmp/ && mkdir -p \\\\$TMPDIR && export ALFWORLD_DATA=/root/autodl-tmp/alfworld && cd /root/cost-verify-agent-rl/RAGEN && python -m ragen.llm_agent.agent_proxy --config-name _alfworld_exp012_reward_fix\\\"\", \"finished_at\": \"2026-05-14T06:30:05.818Z\"}, \"failure_reason\": \"Traceback →  = LLM( ^^^^ File \\\"/root/miniconda3/lib/python3.12/site-packages/vllm/entrypoints/llm.py\\\", line 342, in __init__ engine_args = EngineArgs( ^^^^^^^^^^^ TypeError: EngineArgs.__init__() got an unexpected keyword argument 'disable_mm_preprocessor_cache'\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T06:30:06.373Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T06:30:07.545912+00:00\"}]}}, \"exp011\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:16:54.748Z\", \"updated_at\": \"2026-05-14T06:26:41.225Z\", \"spec\": {\"command\": \"python train.py --config-name=_alfworld_exp008_sft_grpo trainer.resume_mode=resume_path trainer.resume_from_path=/root/autodl-tmp/checkpoints/exp008_grpo/global_step_10 trainer.default_local_dir=/root/autodl-tmp/checkpoints/exp011_grpo/ trainer.local_log_dir=/root/autodl-tmp/checkpoints/exp011_grpo/ trainer.experiment_name=exp011-alfworld-sft-grpo-resume\", \"server\": \"bjb1-17606\", \"data_path\": \"/root/autodl-tmp/alfworld/\", \"data_count\": 3553, \"model_name\": \"Qwen3-1.7B (SFT warmup, resumed from step 10)\", \"seed\": 10000, \"hypothesis\": \"Resume GRPO from step 10 checkpoint with /tmp fix. Same hypothesis as exp010: GRPO with SFT-warmed Qwen3-1.7B achieves success_rate >= 76% on ALFWorld\", \"parent\": \"exp010\", \"log_path\": \"/root/autodl-tmp/exp011_grpo.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/exp011_grpo/\", \"gpu\": \"cuda:0, cuda:1\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T05:56:45.332Z\", \"notes\": \"D007决定kill: reward shaping问题导致success崩塌(format penalty劫持GRPO梯度)。D008确认A2(降format_penalty)为P0。下一步: exp012修改reward function后从step 5 checkpoint恢复。\"}, \"exp010\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T03:45:56.628Z\", \"updated_at\": \"2026-05-14T05:28:54.984Z\", \"spec\": {\"command\": \"python train.py --config-name=_alfworld_exp008_sft_grpo\", \"server\": \"bjb1-17606\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"199389\", \"log_path\": \"/root/autodl-tmp/exp010_grpo.log\", \"submitted_at\": \"2026-05-14T03:45:56.604Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"hypothesis\": \"GRPO with SFT-warmed Qwen3-1.7B can learn ALFWorld task-solving strategy from environment reward, achieving success_rate >= 76%\", \"model_name\": \"Qwen3-1.7B (SFT warmup)\", \"description\": \"Phase A GRPO with SFT checkpoint. Config: _alfworld_exp008_sft_grpo.yaml, symlink qwen3_sft_final, save_freq=5, RAY_TMPDIR explicit.\", \"decision\": \"D006\", \"data_path\": \"/root/autodl-tmp/alfworld/\", \"data_count\": 3553, \"seed\": 10000, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/exp008_grpo/\", \"wall_clock_seconds\": 4825.2, \"gpu_hours\": 2.68}, \"metrics\": {\"step\": 11, \"total_steps\": 30, \"crash_reason\": \"/tmp disk full (fast_downward libdownward.so)\", \"initial_val_action_is_valid\": 0.652, \"initial_val_success\": 0, \"step1_success\": 0.047, \"step1_pass_at_8\": 0.375, \"step1_action_is_valid\": 0.588, \"step10_success\": 0, \"step10_pass_at_8\": 0, \"step10_action_is_valid\": 0.683, \"step5_ppo_kl\": 0.00158, \"step5_entropy\": 0.1, \"trend\": \"action_is_valid improving (58.8%→68.3%) but success collapsing (4.7%→0%)\", \"checkpoint_saved\": \"global_step_10\"}, \"notes\": \"Step 11 崩溃: /tmp磁盘满(fast_downward libdownward.so, 与exp007相同根因)。TMPDIR已修复。关键问题: success 4.7%→0%, pass@8 37.5%→0% (学习信号问题), 但action_is_valid 58.8%→68.3% (模型在学合法命令但非任务完成)。Director要求先分析reward shaping再决定是否恢复训练。\", \"reproduce\": {\"finished_at\": \"2026-05-14T05:06:20.766Z\"}, \"failure_reason\": \"OSError: No space left on device - fast_downward copies libdownward.so to /tmp (root partition full, 30GB). Same root cause as exp007 but different trigger path. Fix: set TMPDIR=/root/autodl-tmp/tmp\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T05:06:21.848Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T05:06:22.885741+00:00\"}]}}, \"exp009\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-14T03:35:13.150Z\", \"updated_at\": \"2026-05-14T04:28:35.845Z\", \"reproduce\": {\"finished_at\": \"2026-05-14T03:39:35.514Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T03:39:36.501130+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"metrics\": {\"status\": \"training_never_started\", \"completed_steps\": 0, \"total_steps\": 30, \"error\": \"AssertionError: enable_response_mask path check failed for SFT checkpoint path\"}, \"notes\": \"第1次启动即失败: AssertionError response mask only supported for qwen/llama-3 — SFT checkpoint 路径 .../exp008_sft/final 不含 \\\"qwen\\\"。修复: 创建 symlink /root/autodl-tmp/checkpoints/qwen3_sft_final → final，保留 response_mask。\"}}, \"notes\": \"第1次: 启动即失败(response_mask断言)。第2次: 与exp010资源冲突(双GRPO同时跑cuda:0+1, 写同一checkpoint目录), 手动终止保留exp010。\", \"completed_at\": \"2026-05-14T03:42:46.557Z\", \"spec\": {\"hypothesis\": \"GRPO with SFT-warmed Qwen3-1.7B can learn ALFWorld task-solving strategy from environment reward, achieving success_rate >= 76%\", \"model_name\": \"Qwen3-1.7B (SFT warmup)\", \"description\": \"Phase A GRPO retry: symlink fix for response_mask, RAY_TMPDIR explicit in command, save_freq=5\", \"decision\": \"D006\", \"command\": \"python train.py --config-name=_alfworld_exp008_sft_grpo\", \"server\": \"bjb1-17606\", \"data_path\": \"/root/autodl-tmp/alfworld/\", \"data_count\": 3553, \"seed\": 10000, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/exp008_grpo/\", \"log_path\": \"/root/autodl-tmp/exp009_grpo.log\"}, \"conclusion\": \"failed\"}, \"exp008\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T03:01:53.741Z\", \"updated_at\": \"2026-05-14T03:04:43.138Z\", \"spec\": {\"hypothesis\": \"SFT warmup on ALFWorld trajectories teaches Qwen3-1.7B valid command semantics, enabling GRPO to bootstrap from non-sparse reward\", \"parent\": \"exp007\", \"model_name\": \"Qwen3-1.7B\", \"description\": \"Phase A retry: SFT warmup (public dataset, format conversion) → GRPO training. Two stages: (1) SFT on ALFWorld trajectories to learn command format+semantics, (2) GRPO with SFT checkpoint\"}, \"conclusion\": \"killed\", \"notes\": \"Director 撤回：LR 5e-6 方案不对，问题是命令语义缺失。改为 SFT warmup (D006)\"}, \"exp007\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T00:12:06.008Z\", \"updated_at\": \"2026-05-14T03:00:29.952Z\", \"spec\": {\"hypothesis\": \"Parser fix + prompt enhancement + speed optimization (collapse_detection off) enables GRPO learning signal with <50% invalid_action\", \"model_name\": \"Qwen3-1.7B\", \"server\": \"bjb1-17606\", \"data_path\": \"ALFWorld train split (3553 games)\", \"data_count\": 3553, \"seed\": 10000, \"description\": \"Phase A fixed: parser adapts Qwen3 format (fallback regex) + prompt enhancement (direct ALFWorld commands) + collapse_detection off + 30 steps + 64 traj/step + 30 max_turns\", \"parent\": \"exp003\", \"command\": \"python train.py (GRPO, Qwen3-1.7B, ALFWorld)\", \"checkpoint_path\": \"N/A (no checkpoint saved)\", \"log_path\": \"/root/autodl-tmp/exp007_formal.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T02:51:31.895Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T02:51:33.256865+00:00\"}]}, \"conclusion\": \"failed\", \"metrics\": {\"steps_completed\": 10, \"steps_planned\": 30, \"crash_reason\": \"OSError: No space left on device (/tmp)\", \"final_success_rate\": 0.0625, \"final_action_is_valid\": 0.0835, \"final_manager_invalid_action\": 0.0156, \"final_pass_at_8\": 0.375, \"final_pg_loss\": 0.00117, \"final_ppo_kl\": 0.00127, \"final_entropy\": 0.057, \"final_score_mean\": 0.578, \"dryrun_action_is_valid\": 0.054, \"dryrun_invalid_action\": 0.065, \"training_time_s\": 6739}, \"completed_at\": \"2026-05-14T02:58:07.012Z\", \"notes\": \"失败原因: (1) 基础设施: step 10时/tmp磁盘满(Ray session文件占满30GB根分区) (2) 学习信号: action_is_valid 8.4% < 10% kill阈值, GRPO无法从稀疏reward bootstrap有效ALFWorld命令 | 已有成果: parser fix验证成功(invalid_action 95%→1.6%), 速度优化验证成功(95min→12min/step) | 建议: SFT warmup教模型ALFWorld命令语义后再接GRPO\"}, \"exp007_dryrun\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T00:19:04.596Z\", \"updated_at\": \"2026-05-14T00:19:04.596Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export ALFWORLD_DATA=/root/autodl-tmp/alfworld && cd /root/cost-verify-agent-rl/RAGEN && python train.py --config-name=_alfworld_exp007_dryrun 2>&1 | tee /root/autodl-tmp/exp007_dryrun.log\\\"\", \"server\": \"bjb1-17606\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"172463\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp007_dryrun.log\", \"submitted_at\": \"2026-05-14T00:19:04.582Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"exp003\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T21:39:20.081Z\", \"updated_at\": \"2026-05-14T00:08:23.334Z\", \"spec\": {\"hypothesis\": \"Always-on self-guidance via GRPO can achieve >=76% on ALFWorld with prompt truncation\", \"model_name\": \"Qwen3-1.7B\", \"server\": \"bjb1-17606\", \"data_path\": \"/root/autodl-tmp/alfworld/\", \"data_count\": \"3553 (train split)\", \"seed\": {\"train\": 10000, \"val\": 123}, \"description\": \"Phase A v3: prompt truncation + 128 traj/step + 100 steps + 50 max_turns\", \"command\": \"python train.py --config-name=_alfworld_exp003\", \"failure_reason\": \"Bootstrap failure: Qwen3-1.7B base不生成&lt;answer>标签，原生格式为&lt;think>...&lt;/think>+直接文本。RAGEN正则&lt;think>(.*?)&lt;/think>\\\\s*&lt;answer>(.*?)&lt;/answer>匹配失败→actions=[]→invalid_action=95.3%, pg_loss≈0。32/32样本确认。\", \"checkpoint_path\": \"N/A\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp003.log\", \"diagnosis_report\": \"artifacts/exp003/report/exp003_invalid_action_diagnosis.md\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T00:08:23.334Z\"}, \"exp005\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:23:20.655Z\", \"updated_at\": \"2026-05-13T23:23:20.655Z\", \"spec\": {\"hypothesis\": \"Fast config (30 steps, 64 traj/step, 30 max_turns) can show learning trend in ~12-20h\", \"model_name\": \"Qwen3-1.7B\", \"server\": \"bjb1-17606\", \"data_path\": \"/root/autodl-tmp/alfworld/\", \"data_count\": \"3553 (train split)\", \"seed\": {\"train\": 10000, \"val\": 123}, \"parent\": \"exp003\", \"description\": \"Phase A fast: reduced config for quicker iteration\"}}, \"exp_003\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-13T21:01:51.727Z\", \"updated_at\": \"2026-05-13T22:04:11.399Z\", \"spec\": {\"hypothesis\": \"Always-on self-guidance via GRPO can achieve ≥76% on ALFWorld with proper prompt truncation (max_prompt_length=4096)\", \"model_name\": \"Qwen3-1.7B\", \"server\": \"bjb1-17606\", \"data_path\": \"/root/autodl-tmp/alfworld/\", \"data_count\": 8810, \"seed\": 42, \"parent\": \"exp_002\", \"description\": \"Phase A v3: add prompt truncation (max_prompt_length=4096) matching Self-Guide paper\"}, \"conclusion\": \"failed\"}, \"exp_003_dryrun\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-13T21:07:02.905Z\", \"updated_at\": \"2026-05-13T21:44:30.297Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export ALFWORLD_DATA=/root/autodl-tmp/alfworld && cd /root/cost-verify-agent-rl/RAGEN && python train.py --config-name=_alfworld_exp003_dryrun 2>&1 | tee /root/autodl-tmp/exp003_dryrun.log\\\"\", \"server\": \"bjb1-17606\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"132166\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp_003_dryrun.log\", \"submitted_at\": \"2026-05-13T21:09:26.351Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"failed\"}, \"exp_003_dryrun2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-13T21:22:01.436Z\", \"updated_at\": \"2026-05-13T21:44:29.827Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export ALFWORLD_DATA=/root/autodl-tmp/alfworld && export RAY_DISABLE_DASHBOARD_AGENT=1 && cd /root/cost-verify-agent-rl/RAGEN && python train.py --config-name=_alfworld_exp003_dryrun 2>&1 | tee /root/autodl-tmp/exp003_dryrun2.log\\\"\", \"server\": \"bjb1-17606\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"137760\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp_003_dryrun2.log\", \"submitted_at\": \"2026-05-13T21:22:01.428Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"failed\"}, \"exp003_dryrun3\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-13T21:26:41.066Z\", \"updated_at\": \"2026-05-13T21:44:28.884Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export ALFWORLD_DATA=/root/autodl-tmp/alfworld && cd /root/cost-verify-agent-rl/RAGEN && python train.py --config-name=_alfworld_exp003_dryrun\\\"\", \"server\": \"bjb1-17606\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"149365\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp003_dryrun3.log\", \"submitted_at\": \"2026-05-13T21:26:41.056Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"failed\"}, \"exp_003_dryrun3\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-13T21:27:05.011Z\", \"updated_at\": \"2026-05-13T21:44:27.949Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export ALFWORLD_DATA=/root/autodl-tmp/alfworld && export RAY_DISABLE_DASHBOARD_AGENT=1 && cd /root/cost-verify-agent-rl/RAGEN && python train.py --config-name=_alfworld_exp003_dryrun 2>&1 | tee /root/autodl-tmp/exp003_dryrun3.log\\\"\", \"server\": \"bjb1-17606\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"152820\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp_003_dryrun3.log\", \"submitted_at\": \"2026-05-13T21:27:05.002Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"failed\"}, \"exp_002\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T19:28:16.342Z\", \"updated_at\": \"2026-05-13T21:22:13.213Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/cost-verify-agent-rl/RAGEN && ALFWORLD_DATA=/root/autodl-tmp/alfworld CUDA_VISIBLE_DEVICES=0,1 python train.py --config-name _alfworld_exp002\\\"\", \"server\": \"bjb1-17606\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"138870\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp_002.log\", \"submitted_at\": \"2026-05-13T21:22:13.205Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T21:01:03.160Z\"}, \"exp_001b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T19:14:10.718Z\", \"updated_at\": \"2026-05-13T19:29:05.714Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/cost-verify-agent-rl/RAGEN && ALFWORLD_DATA=/root/autodl-tmp/alfworld CUDA_VISIBLE_DEVICES=0,1 python train.py --config-name _alfworld_exp001b\\\"\", \"server\": \"bjb1-17606\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"93789\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp_001b.log\", \"submitted_at\": \"2026-05-13T19:15:38.523Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"Same bootstrap failure as exp_001: base model (Qwen3-1.7B) cannot produce &lt;think>/&lt;answer> format. pg_loss≈0, KL=0, 95.6% invalid actions. Killed at step 4/50.\", \"checkpoint_path\": \"N/A\", \"wall_clock_seconds\": 807.2, \"gpu_hours\": 0.45}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T19:29:05.714Z\"}, \"exp_001\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T18:26:40.715Z\", \"updated_at\": \"2026-05-13T19:13:39.086Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/cost-verify-agent-rl/RAGEN && ALFWORLD_DATA=/root/autodl-tmp/alfworld CUDA_VISIBLE_DEVICES=0,1 python train.py --config-name _alfworld_exp001\\\"\", \"server\": \"bjb1-17606\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"87845\", \"log_path\": \"~/runs/cost-verify-agent-rl/exp_001.log\", \"submitted_at\": \"2026-05-13T18:34:53.576Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A\", \"failure_reason\": \"ValueError: decoder prompt (4096 tokens) + output tokens > max_model_len (4096). Multi-turn rollout prompt exceeded limit at step 7.\", \"wall_clock_seconds\": 2325.5, \"gpu_hours\": 1.29}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T19:13:39.086Z\"}}, \"count\": 154, \"total\": 154, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5725}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-22T03:36:07.361Z_

<details><summary>↩ Tool result · `toolu_01TjeMFVvP7m1kvPWE89mCZv`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/memory.md\", \"content\": \"# Project Memory — cost-verify-agent-rl\\n\\n## 经验教训\\n\\n### max_prompt_length 必须严格小于 max_model_len (2026-05-19)\\nv9c 在 step 3/30 崩溃：`max_prompt_length: 16384 == max_model_len: 16384`，prompt 填满后 vLLM 报 \\\"prompt + requested output tokens > max_model_len\\\"。修复：`max_prompt_length = max_model_len - response_length`（15360 = 16384 - 1024）。写 config 时永远预留 generation headroom。\\n\\n### save_freq 不应设为 999 (2026-05-19)\\nv9c 崩溃后无 checkpoint 可恢复（save_freq: 999 = 实际不保存）。30 步训练建议 save_freq: 5~10，代价是少量磁盘但能从中间恢复。\\n\\n### FSDP2 兼容性修复模式 (2026-05-19)\\n- `_fsdp_wrapped_module` → `getattr(model, \\\"_fsdp_wrapped_module\\\", model)`\\n- `FSDP.summon_full_params(model)` → `FSDP.summon_full_params(model) if isinstance(model, FSDP) else nullcontext()`\\n- FSDP2 用 `fully_shard` composable API，不 wrap 模型，不存在 `_fsdp_wrapped_module`\\n\\n### save_contents 的 yaml 路径必须正确 (2026-05-20)\\nverl checkpoint 的 `save_contents` 必须放在 `actor_rollout_ref.actor.checkpoint` 下，不是 `trainer` 下。错误路径导致保存完整 optimizer state（92GB），正确路径只保存 actor weights（33GB）。\\n\\n### FSDP2 checkpoint 是 rank shards 不是 HF 格式 (2026-05-20)\\nFSDP2 保存的 checkpoint 是 `world_size_N` 目录下的 per-rank shards（`__0_0.distcp` 等），不是 HF safetensors。部署/评估前必须用 `convert_fsdp_to_hf.py` 合并为标准 HF 格式。\\n\\n### NCCL deadlock hang 的模式识别 (2026-05-20)\\nv9d step 15 出现 NCCL deadlock：GPU utilization 0% 但显存仍占 ~60GB，进程不退出也不报错。这是典型的 collective 通信死锁（某 rank 未到达同步点）。发现后应直接 kill 进程，不要等待恢复。长训练建议设 `NCCL_TIMEOUT`。\\n\\n### 8B episode-level GRPO reward 饱和极快 (2026-05-20)\\nv9d 训练曲线：40.6%(baseline) → 81.25%(step 5) → 96.875%(step 10) → 100%(step 12)。Step 12 后 advantage=0, pg_loss=0, grad_norm→0，完全无学习信号。教训：8B 模型在简单任务上 episode-level GRPO ≤15 steps 即可饱和，必须提前规划 OOD eval 和 early stopping，否则后续 steps 浪费算力且有 hang 风险。\\n\\n### ScienceWorld eval valid_action_rate bug (2026-05-19)\\n`action_is_valid` 必须对比完整 `valid_actions` 列表，不能对比截断的 `shown[:50]`（前 50 个几乎全是 `connect X to Y` 格式，模型输出的自然语言动作全被误判）。\\n\\n### exp029 标准 config response_length 是 1024 不是 400 (2026-05-21)\\nIntervention C Worker 确认 Seed 7 原始 config `response_length=1024`。之前 handoff 说 400 是错误信息。\\n\\n## 决策原因\\n\\n### 8B Cell C 用 FSDP2 + CPUOffloadPolicy (2026-05-19)\\nFSDP1 峰值 ~91 GB/GPU → OOM（v5-v8 全部失败）。FSDP2 CPUOffloadPolicy 将参数和优化器按 layer 搬到 CPU，峰值降至 ~83 GB/GPU，余量 ~12 GB。不需要租卡。\\n\\n### ScienceWorld GRPO reward 是 continuous sparse (2026-05-19)\\n公式：`reward = (score/100) * 10.0`，范围 0-10，仅 episode 结束发放。Cell A（step-level）预期失败：中间步 reward=0，最后一步有 continuous reward 但 step-level credit assignment 无法利用。Cell C（episode-level）自然兼容。\\n\\n### 崩溃 seed OOD 泛化最强 — 关键 narrative 发现 (2026-05-21)\\nSeed 4（collapse seed, step 15）OOD = 30.60%，超过所有 success seeds（max 29.10%）。response_length inflation（7212 tokens）在 OOD 场景充当\\\"暴力搜索\\\"——更长的探索覆盖更多动作组合。崩溃不是纯粹有害的：训练集上是退化，OOD 上是更好的探索性。Bimodal behavior 是 \\\"efficient learner vs over-explorer\\\" 的权衡，不是简单的 \\\"success vs failure\\\"。\\n\\n### max_response_length 在 RAGEN 代码中无原生实现 (2026-05-21)\\n`config/base.yaml` 中 `data.max_response_length` 仅通过 OmegaConf 插值映射到 per-turn `rollout.response_length`，无 trajectory-level 截断逻辑。C' 实验在 bjb1 `agent_proxy.py` 中手动实现了 cumulative token 计数器（L253-339），此改动只在 bjb1 上，westd 代码未改。\\n\\n## 约束\\n\\n### westd GPU 内存紧张 (2026-05-19)\\n8B FSDP2+CPUOffload 训练时 GPU 占用 ~83/95.6 GB (87%)。不要增加 batch size 或 max_model_len，无余量。\\n\", \"total_chars\": 3137, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "963abddc-300c-4e26-a177-ac85bc75281a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/memory.md\\\", \\\"content\\\": \\\"# Project Memory — cost-verify-agent-rl\\\\n\\\\n## 经验教训\\\\n\\\\n### max_prompt_length 必须严格小于 max_model_len (2026-05-19)\\\\nv9c 在 step 3/30 崩溃：`max_prompt_length: 16384 == max_model_len: 16384`，prompt 填满后 vLLM 报 \\\\\\\"prompt + requested output tokens > max_model_len\\\\\\\"。修复：`max_prompt_length = max_model_len - response_length`（15360 = 16384 - 1024）。写 config 时永远预留 generation headroom。\\\\n\\\\n### save_freq 不应设为 999 (2026-05-19)\\\\nv9c 崩溃后无 checkpoint 可恢复（save_freq: 999 = 实际不保存）。30 步训练建议 save_freq: 5~10，代价是少量磁盘但能从中间恢复。\\\\n\\\\n### FSDP2 兼容性修复模式 (2026-05-19)\\\\n- `_fsdp_wrapped_module` → `getattr(model, \\\\\\\"_fsdp_wrapped_module\\\\\\\", model)`\\\\n- `FSDP.summon_full_params(model)` → `FSDP.summon_full_params(model) if isinstance(model, FSDP) else nullcontext()`\\\\n- FSDP2 用 `fully_shard` composable API，不 wrap 模型，不存在 `_fsdp_wrapped_module`\\\\n\\\\n### save_contents 的 yaml 路径必须正确 (2026-05-20)\\\\nverl checkpoint 的 `save_contents` 必须放在 `actor_rollout_ref.actor.checkpoint` 下，不是 `trainer` 下。错误路径导致保存完整 optimizer state（92GB），正确路径只保存 actor weights（33GB）。\\\\n\\\\n### FSDP2 checkpoint 是 rank shards 不是 HF 格式 (2026-05-20)\\\\nFSDP2 保存的 checkpoint 是 `world_size_N` 目录下的 per-rank shards（`__0_0.distcp` 等），不是 HF safetensors。部署/评估前必须用 `convert_fsdp_to_hf.py` 合并为标准 HF 格式。\\\\n\\\\n### NCCL deadlock hang 的模式识别 (2026-05-20)\\\\nv9d step 15 出现 NCCL deadlock：GPU utilization 0% 但显存仍占 ~60GB，进程不退出也不报错。这是典型的 collective 通信死锁（某 rank 未到达同步点）。发现后应直接 kill 进程，不要等待恢复。长训练建议设 `NCCL_TIMEOUT`。\\\\n\\\\n### 8B episode-level GRPO reward 饱和极快 (2026-05-20)\\\\nv9d 训练曲线：40.6%(baseline) → 81.25%(step 5) → 96.875%(step 10) → 100%(step 12)。Step 12 后 advantage=0, pg_loss=0, grad_norm→0，完全无学习信号。教训：8B 模型在简单任务上 episode-level GRPO ≤15 steps 即可饱和，必须提前规划 OOD eval 和 early stopping，否则后续 steps 浪费算力且有 hang 风险。\\\\n\\\\n### ScienceWorld eval valid_action_rate bug (2026-05-19)\\\\n`action_is_valid` 必须对比完整 `valid_actions` 列表，不能对比截断的 `shown[:50]`（前 50 个几乎全是 `connect X to Y` 格式，模型输出的自然语言动作全被误判）。\\\\n\\\\n### exp029 标准 config response_length 是 1024 不是 400 (2026-05-21)\\\\nIntervention C Worker 确认 Seed 7 原始 config `response_length=1024`。之前 handoff 说 400 是错误信息。\\\\n\\\\n## 决策原因\\\\n\\\\n### 8B Cell C 用 FSDP2 + CPUOffloadPolicy (2026-05-19)\\\\nFSDP1 峰值 ~91 GB/GPU → OOM（v5-v8 全部失败）。FSDP2 CPUOffloadPolicy 将参数和优化器按 layer 搬到 CPU，峰值降至 ~83 GB/GPU，余量 ~12 GB。不需要租卡。\\\\n\\\\n### ScienceWorld GRPO reward 是 continuous sparse (2026-05-19)\\\\n公式：`reward = (score/100) * 10.0`，范围 0-10，仅 episode 结束发放。Cell A（step-level）预期失败：中间步 reward=0，最后一步有 continuous reward 但 step-level credit assignment 无法利用。Cell C（episode-level）自然兼容。\\\\n\\\\n### 崩溃 seed OOD 泛化最强 — 关键 narrative 发现 (2026-05-21)\\\\nSeed 4（collapse seed, step 15）OOD = 30.60%，超过所有 success seeds（max 29.10%）。response_length inflation（7212 tokens）在 OOD 场景充当\\\\\\\"暴力搜索\\\\\\\"——更长的探索覆盖更多动作组合。崩溃不是纯粹有害的：训练集上是退化，OOD 上是更好的探索性。Bimodal behavior 是 \\\\\\\"efficient learner vs over-explorer\\\\\\\" 的权衡，不是简单的 \\\\\\\"success vs failure\\\\\\\"。\\\\n\\\\n### max_response_length 在 RAGEN 代码中无原生实现 (2026-05-21)\\\\n`config/base.yaml` 中 `data.max_response_length` 仅通过 OmegaConf 插值映射到 per-turn `rollout.response_length`，无 trajectory-level 截断逻辑。C' 实验在 bjb1 `agent_proxy.py` 中手动实现了 cumulative token 计数器（L253-339），此改动只在 bjb1 上，westd 代码未改。\\\\n\\\\n## 约束\\\\n\\\\n### westd GPU 内存紧张 (2026-05-19)\\\\n8B FSDP2+CPUOffload 训练时 GPU 占用 ~83/95.6 GB (87%)。不要增加 batch size 或 max_model_len，无余量。\\\\n\\\", \\\"total_chars\\\": 3137, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/memory.md\", \"content\": \"# Project Memory — cost-verify-agent-rl\\n\\n## 经验教训\\n\\n### max_prompt_length 必须严格小于 max_model_len (2026-05-19)\\nv9c 在 step 3/30 崩溃：`max_prompt_length: 16384 == max_model_len: 16384`，prompt 填满后 vLLM 报 \\\"prompt + requested output tokens > max_model_len\\\"。修复：`max_prompt_length = max_model_len - response_length`（15360 = 16384 - 1024）。写 config 时永远预留 generation headroom。\\n\\n### save_freq 不应设为 999 (2026-05-19)\\nv9c 崩溃后无 checkpoint 可恢复（save_freq: 999 = 实际不保存）。30 步训练建议 save_freq: 5~10，代价是少量磁盘但能从中间恢复。\\n\\n### FSDP2 兼容性修复模式 (2026-05-19)\\n- `_fsdp_wrapped_module` → `getattr(model, \\\"_fsdp_wrapped_module\\\", model)`\\n- `FSDP.summon_full_params(model)` → `FSDP.summon_full_params(model) if isinstance(model, FSDP) else nullcontext()`\\n- FSDP2 用 `fully_shard` composable API，不 wrap 模型，不存在 `_fsdp_wrapped_module`\\n\\n### save_contents 的 yaml 路径必须正确 (2026-05-20)\\nverl checkpoint 的 `save_contents` 必须放在 `actor_rollout_ref.actor.checkpoint` 下，不是 `trainer` 下。错误路径导致保存完整 optimizer state（92GB），正确路径只保存 actor weights（33GB）。\\n\\n### FSDP2 checkpoint 是 rank shards 不是 HF 格式 (2026-05-20)\\nFSDP2 保存的 checkpoint 是 `world_size_N` 目录下的 per-rank shards（`__0_0.distcp` 等），不是 HF safetensors。部署/评估前必须用 `convert_fsdp_to_hf.py` 合并为标准 HF 格式。\\n\\n### NCCL deadlock hang 的模式识别 (2026-05-20)\\nv9d step 15 出现 NCCL deadlock：GPU utilization 0% 但显存仍占 ~60GB，进程不退出也不报错。这是典型的 collective 通信死锁（某 rank 未到达同步点）。发现后应直接 kill 进程，不要等待恢复。长训练建议设 `NCCL_TIMEOUT`。\\n\\n### 8B episode-level GRPO reward 饱和极快 (2026-05-20)\\nv9d 训练曲线：40.6%(baseline) → 81.25%(step 5) → 96.875%(step 10) → 100%(step 12)。Step 12 后 advantage=0, pg_loss=0, grad_norm→0，完全无学习信号。教训：8B 模型在简单任务上 episode-level GRPO ≤15 steps 即可饱和，必须提前规划 OOD eval 和 early stopping，否则后续 steps 浪费算力且有 hang 风险。\\n\\n### ScienceWorld eval valid_action_rate bug (2026-05-19)\\n`action_is_valid` 必须对比完整 `valid_actions` 列表，不能对比截断的 `shown[:50]`（前 50 个几乎全是 `connect X to Y` 格式，模型输出的自然语言动作全被误判）。\\n\\n### exp029 标准 config response_length 是 1024 不是 400 (2026-05-21)\\nIntervention C Worker 确认 Seed 7 原始 config `response_length=1024`。之前 handoff 说 400 是错误信息。\\n\\n## 决策原因\\n\\n### 8B Cell C 用 FSDP2 + CPUOffloadPolicy (2026-05-19)\\nFSDP1 峰值 ~91 GB/GPU → OOM（v5-v8 全部失败）。FSDP2 CPUOffloadPolicy 将参数和优化器按 layer 搬到 CPU，峰值降至 ~83 GB/GPU，余量 ~12 GB。不需要租卡。\\n\\n### ScienceWorld GRPO reward 是 continuous sparse (2026-05-19)\\n公式：`reward = (score/100) * 10.0`，范围 0-10，仅 episode 结束发放。Cell A（step-level）预期失败：中间步 reward=0，最后一步有 continuous reward 但 step-level credit assignment 无法利用。Cell C（episode-level）自然兼容。\\n\\n### 崩溃 seed OOD 泛化最强 — 关键 narrative 发现 (2026-05-21)\\nSeed 4（collapse seed, step 15）OOD = 30.60%，超过所有 success seeds（max 29.10%）。response_length inflation（7212 tokens）在 OOD 场景充当\\\"暴力搜索\\\"——更长的探索覆盖更多动作组合。崩溃不是纯粹有害的：训练集上是退化，OOD 上是更好的探索性。Bimodal behavior 是 \\\"efficient learner vs over-explorer\\\" 的权衡，不是简单的 \\\"success vs failure\\\"。\\n\\n### max_response_length 在 RAGEN 代码中无原生实现 (2026-05-21)\\n`config/base.yaml` 中 `data.max_response_length` 仅通过 OmegaConf 插值映射到 per-turn `rollout.response_length`，无 trajectory-level 截断逻辑。C' 实验在 bjb1 `agent_proxy.py` 中手动实现了 cumulative token 计数器（L253-339），此改动只在 bjb1 上，westd 代码未改。\\n\\n## 约束\\n\\n### westd GPU 内存紧张 (2026-05-19)\\n8B FSDP2+CPUOffload 训练时 GPU 占用 ~83/95.6 GB (87%)。不要增加 batch size 或 max_model_len，无余量。\\n\", \"total_chars\": 3137, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-22T03:36:07.375Z_

<details><summary>↩ Tool result · `toolu_01NzDd8teyKzcjuWqQ8S1QN1`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/literature_map.yaml\", \"content\": \"# B-IAVR Literature Map\\n# Updated: 2026-05-17\\n# Categories: direct-competitor, method-component, background, evaluation\\n# Roles: predecessor, competitor, baseline, evaluation, background\\n\\npapers:\\n\\n  # ============================================================\\n  # Direction 1: Self-Verification / Self-Correction in LLM Agents\\n  # ============================================================\\n\\n  - id: kamoi2024self-correction-survey\\n    title: \\\"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs\\\"\\n    authors: \\\"Kamoi et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2024\\n    arxiv_id: \\\"2406.01297\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Foundational survey establishing that pure intrinsic self-correction is unreliable.\\n      Validates B-IAVR's use of grounded verification (environment re-observation) over prompted self-feedback.\\n\\n  - id: tie2025correctbench\\n    title: \\\"Can LLMs Correct Themselves? A Benchmark of Self-Correction in LLMs\\\"\\n    authors: \\\"Tie et al.\\\"\\n    venue: \\\"NeurIPS 2025 Datasets & Benchmarks\\\"\\n    year: 2025\\n    arxiv_id: \\\"2510.16062\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Benchmark showing self-correction has diminishing returns when applied uniformly.\\n      Supports B-IAVR's selective verification design over blanket correction.\\n\\n  - id: self-verification-dilemma-2026\\n    title: \\\"Self-Verification Dilemma: Experience-Driven Suppression of Overused Checking in LLM Reasoning\\\"\\n    authors: \\\"Long et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2602.03485\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Empirically validates that >90% of self-verification is confirmatory, ~2% corrective.\\n      Directly supports B-IAVR's core thesis that verification should be selective.\\n      Their experience-pool approach is complementary to B-IAVR's action-change signal.\\n\\n  - id: zhang2025incentivize-self-verify\\n    title: \\\"Incentivizing LLMs to Self-Verify Their Answers\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2506.01369\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Unifies answer generation and verification via single RL training process.\\n      Parallel to B-IAVR: they train verification into generation; B-IAVR trains when to trigger separate verification.\\n\\n  - id: mar2025\\n    title: \\\"MAR: Multi-Agent Reflexion Improves Reasoning Abilities in LLMs\\\"\\n    authors: \\\"Ozer et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2512.20845\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Multi-agent self-correction with diverse critic personas.\\n      Complementary: MAR improves correction quality; B-IAVR decides when to trigger correction.\\n\\n  - id: ssr2025\\n    title: \\\"SSR: Socratic Self-Refine for Large Language Model Reasoning\\\"\\n    authors: \\\"Shi et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2511.10621\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Structured Socratic questioning for self-refinement.\\n      Complementary: improves correction step quality; B-IAVR focuses on when to invoke correction.\\n\\n  - id: verifiagent2025\\n    title: \\\"VerifiAgent: a Unified Verification Agent in Language Model Reasoning\\\"\\n    authors: \\\"Han et al.\\\"\\n    venue: \\\"EMNLP 2025 Findings\\\"\\n    year: 2025\\n    arxiv_id: \\\"2504.00406\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Unified verification agent with meta-verification + tool-based adaptive verification.\\n      Focuses on how to verify (tool selection); B-IAVR focuses on when to verify (policy learning).\\n      Complementary: VerifiAgent's verification quality could enhance B-IAVR's verification step.\\n\\n  # ============================================================\\n  # Direction 2: Agent RL Training\\n  # ============================================================\\n\\n  - id: feng2025gigpo\\n    title: \\\"GiGPO: Group-in-Group Policy Optimization for LLM Agent Training\\\"\\n    authors: \\\"Feng et al.\\\"\\n    venue: \\\"NeurIPS 2025\\\"\\n    year: 2025\\n    arxiv_id: \\\"2505.10978\\\"\\n    category: method-component\\n    role: predecessor\\n    relevance_note: >\\n      Core training algorithm for B-IAVR. Nested group structure provides step-level credit\\n      assignment without learned critic. >12% over GRPO on ALFWorld, >9% on WebShop.\\n\\n  - id: selfguide2026\\n    title: \\\"Co-Evolution of Policy and Internal Reward for Language Agents (Self-Guide)\\\"\\n    authors: \\\"Wang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2604.03098\\\"\\n    category: method-component\\n    role: predecessor\\n    relevance_note: >\\n      Direct predecessor. B-IAVR extends Self-Guide's co-evolving internal reward.\\n      The self-guidance signal is the foundation for action-change detection triggering verification.\\n      8% improvement over env-reward-only on ALFWorld with Qwen3-1.7B/4B.\\n\\n  - id: spear2025\\n    title: \\\"Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning\\\"\\n    authors: \\\"Qin et al.\\\"\\n    venue: \\\"ICLR 2026\\\"\\n    year: 2025\\n    arxiv_id: \\\"2509.22601\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      Curriculum-based self-imitation for sparse-reward agent tasks.\\n      Up to +16.1% on ALFWorld over GRPO. Self-imitation curriculum could augment B-IAVR training.\\n\\n  - id: wei2025webagent-r1\\n    title: \\\"WebAgent-R1: Training Web Agents via End-to-End Multi-Turn RL\\\"\\n    authors: \\\"Wei et al.\\\"\\n    venue: \\\"EMNLP 2025\\\"\\n    year: 2025\\n    arxiv_id: \\\"2505.16421\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Extends GRPO to multi-turn (M-GRPO) with dynamic context compression.\\n      Qwen-2.5-3B: 6.1% to 33.9% on WebArena-Lite. M-GRPO multi-turn extension relevant to B-IAVR.\\n\\n  - id: dapo2025\\n    title: \\\"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\\\"\\n    authors: \\\"Yu et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2503.14476\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      RL training stabilization techniques (Clip-Higher, Dynamic Sampling).\\n      Applicable to B-IAVR's RL training to prevent entropy collapse.\\n\\n  - id: digiRL2024\\n    title: \\\"DigiRL: Training In-The-Wild Device-Control Agents with Autonomous RL\\\"\\n    authors: \\\"Bai et al.\\\"\\n    venue: \\\"NeurIPS 2024\\\"\\n    year: 2024\\n    arxiv_id: \\\"2406.11896\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Online RL for device control agents. Demonstrates online RL viability for interactive agents.\\n      49.5% absolute improvement over SFT. Parallel approach to B-IAVR in text-based setting.\\n\\n  - id: li2025sorl\\n    title: \\\"SORL: Stabilizing Off-Policy RL for Long-Horizon Agent Training\\\"\\n    authors: \\\"Li et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2511.20718\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      Turn-level importance sampling + clipping-triggered normalization for stable multi-turn agent RL.\\n      Directly applicable to B-IAVR's multi-turn ALFWorld training stability.\\n\\n  - id: agentic-rl-survey-2025\\n    title: \\\"The Landscape of Agentic Reinforcement Learning for LLMs: A Survey\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    venue: \\\"TMLR 2026\\\"\\n    year: 2025\\n    arxiv_id: \\\"2509.02547\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Comprehensive survey formalizing agentic RL. Contextualizes B-IAVR as training agents\\n      to make meta-decisions (when to verify) via RL within the POMDP framework.\\n\\n  - id: skillmaster2026\\n    title: \\\"SkillMaster: Toward Autonomous Skill Mastery in LLM Agents\\\"\\n    authors: \\\"Yang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2605.08693\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      DualAdv-GRPO: separately estimates advantages for task-solving and skill-editing decisions.\\n      +8.8% on ALFWorld, +9.3% on WebShop. DualAdv structure could inform B-IAVR's\\n      separation of action and verification advantages.\\n\\n  - id: t2po2026\\n    title: \\\"T2PO: Uncertainty-Guided Exploration Control for Stable Multi-Turn Agentic RL\\\"\\n    authors: \\\"Wang et al.\\\"\\n    venue: \\\"ICML 2026 Spotlight\\\"\\n    year: 2026\\n    arxiv_id: \\\"2605.02178\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      Token- and turn-level uncertainty monitoring for stable multi-turn agent RL.\\n      Triggers thinking intervention when marginal uncertainty change drops below threshold.\\n      Evaluated on ALFWorld and WebShop. Conceptually related: uncertainty-based trigger vs\\n      B-IAVR's action-change trigger, but T2PO targets training stability, not deployment verification.\\n\\n  - id: gvpo2026\\n    title: \\\"GVPO: Group Verification-based Policy Optimization for Interactive Coding Agents\\\"\\n    authors: \\\"Dai et al.\\\"\\n    venue: \\\"ICLR 2026\\\"\\n    year: 2026\\n    arxiv_id: null  # no arXiv preprint; OpenReview ID: RY47Tq0VsV\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      Advantage shaping with outcome-verifiable + process-verifiable signals.\\n      +12.7% over o1 on AppWorld. Integrates intermediate execution feedback as step-level\\n      verification signals. Different focus: uses verification for credit assignment during\\n      training; B-IAVR learns when to invoke verification at deployment.\\n\\n  - id: agentv-rl2026\\n    title: \\\"AgentV-RL: Scaling Reward Modeling with Agentic Verifier\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2604.16004\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      Bidirectional forward/backward agentic verifier for reward modeling in RL.\\n      4B model surpasses SOTA ORMs by 25.2%. Addresses verification quality in reward modeling;\\n      B-IAVR addresses verification timing in agent deployment. Complementary.\\n\\n  - id: pa-moe2026\\n    title: \\\"PA-MoE: Phase-Aware Mixture of Experts for Agentic Reinforcement Learning\\\"\\n    authors: \\\"Li et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2602.17038\\\"\\n    category: evaluation\\n    role: baseline\\n    relevance_note: >\\n      [NEW-0516] Lightweight phase router learns latent phase boundaries from RL objective.\\n      PA-MoE+GiGPO with Qwen2.5-1.5B achieves 93.8% on ALFWorld (+7.7 over GiGPO 86.1%).\\n      1.5B outperforms vanilla 7B GiGPO (90.2%). New small-model SOTA on ALFWorld.\\n      Orthogonal architecture innovation; important baseline to cite.\\n\\n  - id: sdar2026\\n    title: \\\"SDAR: Self-Distilled Agentic Reinforcement Learning\\\"\\n    authors: \\\"Lu et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2605.15155\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] On-policy self-distillation as gated auxiliary objective during RL training.\\n      Token-level gate decides supervision intensity. +9.4% over GRPO on ALFWorld.\\n      Complementary: SDAR improves RL training; B-IAVR learns verification policy.\\n\\n  - id: hcapo2026\\n    title: \\\"HCAPO: Hindsight Credit Assignment for Long-Horizon LLM Agents\\\"\\n    authors: \\\"Tan et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2603.08754\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] LLM-as-critic refines step-level Q-values via hindsight reasoning +\\n      multi-scale advantage for critical decision states.\\n      +13.8% on ALFWorld, +7.7% on WebShop over GRPO (Qwen2.5-7B).\\n      Could improve B-IAVR's reward signal for verification decision steps.\\n\\n  - id: act2026\\n    title: \\\"ACT: Agentic Critical Training\\\"\\n    authors: \\\"Liu et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2603.08706\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] Trains agents to judge action quality via critical comparison reward.\\n      +5.07 over IL, +4.62 over RL. Different axis: ACT improves reflection quality;\\n      B-IAVR decides when to reflect.\\n\\n  - id: rwml2026\\n    title: \\\"RWML: Reinforcement World Model Learning for LLM-based Agents\\\"\\n    authors: \\\"Yu et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2602.05842\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] Self-supervised world model via sim-to-real gap rewards in embedding space.\\n      +6.9 on ALFWorld over task-success-only RL. Matches expert-data training.\\n      Orthogonal: improves internal world model; B-IAVR adds selective verification.\\n\\n  - id: skill0-2026\\n    title: \\\"SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization\\\"\\n    authors: \\\"Lu et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2604.02268\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] Training-time curriculum progressively withdraws skill context until zero-shot.\\n      +9.7% on ALFWorld over GRPO, <0.5k tokens per step.\\n      Complementary: SKILL0 internalizes skills; B-IAVR adds selective verification.\\n\\n  - id: fission-grpo2026\\n    title: \\\"Fission-GRPO: Robust Tool Use via Learning to Recover from Execution Errors\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2601.15625\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] Fissions failed trajectories into recovery training instances.\\n      +4% overall accuracy on BFCL v4 Multi-Turn over GRPO.\\n      Related: error recovery after failure vs B-IAVR's proactive verification.\\n\\n  - id: selfbudgeter2026\\n    title: \\\"SelfBudgeter: Adaptive Token Allocation for Efficient LLM Reasoning\\\"\\n    authors: \\\"Li et al.\\\"\\n    venue: \\\"ICLR 2026 (under review)\\\"\\n    year: 2025\\n    arxiv_id: \\\"2505.11274\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] Self-estimated token budgets + budget-guided GRPO. 61% token reduction.\\n      Parallel concept: SelfBudgeter allocates computation budget;\\n      B-IAVR makes binary verify/not-verify decision. Both use RL for adaptive compute.\\n\\n  - id: cove2026\\n    title: \\\"CoVe: Training Interactive Tool-Use Agents via Constraint-Guided Verification\\\"\\n    authors: \\\"Chen et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2603.01940\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] Task constraints guide trajectory generation and serve as deterministic verifiers.\\n      Different: CoVe uses verification for data synthesis; B-IAVR learns when to verify at inference.\\n\\n  # ============================================================\\n  # Direction 3: Selective Verification / Adaptive Computation\\n  # ============================================================\\n\\n  - id: wan2025derailer-rerailer\\n    title: \\\"Derailer-Rerailer: Adaptive Verification for Efficient and Reliable LM Reasoning\\\"\\n    authors: \\\"Wan et al.\\\"\\n    venue: \\\"ACL 2025 Findings\\\"\\n    year: 2025\\n    arxiv_id: \\\"2408.13940\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      Most directly related competitor. Both do selective verification with binary trigger.\\n      Key difference: operates on reasoning chains (single-turn); B-IAVR on agent trajectories (multi-turn).\\n      Uses heuristic instability signal; B-IAVR uses RL-trained action-change signal.\\n      8-11% accuracy gain, 2-3x efficiency over uniform verification.\\n\\n  - id: sherlock2025\\n    title: \\\"Sherlock: Reliable and Efficient Agentic Workflow Execution\\\"\\n    authors: \\\"Microsoft\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2511.00330\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      Selective verification for agentic workflows via offline counterfactual analysis + speculative execution.\\n      Different scope: workflow DAG level (offline); B-IAVR is step-level (online RL).\\n      18.3% accuracy gain, 26% cost reduction, 48.7% latency reduction.\\n\\n  - id: singhi2025when-to-verify\\n    title: \\\"When To Solve, When To Verify: Compute-Optimal Verification for LLM Reasoning\\\"\\n    authors: \\\"Singhi et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2504.01005\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Derives inference scaling laws for solve-vs-verify tradeoff.\\n      Finding that over-verification is suboptimal directly supports B-IAVR's selective approach.\\n      B-IAVR learns this allocation via RL rather than analytically.\\n\\n  - id: yang2026ares\\n    title: \\\"ARES: Adaptive Reasoning Effort Selection for Efficient LLM Agents\\\"\\n    authors: \\\"Yang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2603.07915\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      Closest competitor in agent domain. Both train learned per-step compute allocation.\\n      ARES uses SFT-initialized router further refined via GRPO with outcome + token efficiency reward;\\n      B-IAVR trains binary verify/not-verify via RL with action-change signal.\\n      Key differences: (1) reward signal — ARES optimizes token efficiency, B-IAVR uses action-change\\n      as verification trigger; (2) data requirement — ARES needs difficulty-annotated training data\\n      to bootstrap the router, B-IAVR learns from environment interaction alone.\\n      Reduces reasoning tokens by up to 52.7%.\\n\\n  - id: tu2025autothink\\n    title: \\\"Learning When to Think: Shaping Adaptive Reasoning in R1-Style Models via Multi-Stage RL\\\"\\n    authors: \\\"Tu et al.\\\"\\n    venue: \\\"NeurIPS 2025\\\"\\n    year: 2025\\n    arxiv_id: \\\"2505.10832\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      Analogous idea in reasoning domain: RL-trained adaptive computation trigger.\\n      Operates on single-turn reasoning; B-IAVR on multi-turn agent trajectories.\\n      +6.4% accuracy, -52% tokens on DeepSeek-R1-Distill-Qwen-1.5B.\\n\\n  - id: du2025thinkless\\n    title: \\\"Thinkless: LLM Learns When to Think\\\"\\n    authors: \\\"Fang et al.\\\"\\n    venue: \\\"NeurIPS 2025\\\"\\n    year: 2025\\n    arxiv_id: \\\"2505.13379\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      RL-trained control token to decide when to invoke extended thinking.\\n      Methodologically closest to B-IAVR in reasoning domain; B-IAVR applies to interactive agent trajectories.\\n\\n  - id: wang2025efficient-agents\\n    title: \\\"Efficient Agents: Building Effective Agents While Reducing Cost\\\"\\n    authors: \\\"Wang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2508.02694\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      First systematic study of agent efficiency-effectiveness tradeoff.\\n      Framework-level cost reduction; B-IAVR addresses cost at verification-policy level.\\n      Retains 96.7% performance with 28.4% cost-of-pass improvement.\\n\\n  - id: venktesh2025trust-but-verify\\n    title: \\\"Trust but Verify! A Survey on Verification Design for Test-time Scaling\\\"\\n    authors: \\\"Venktesh et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2508.16665\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Survey of verification approaches for test-time compute scaling.\\n      Identifies verification timing as key open problem. B-IAVR provides concrete solution for agent setting.\\n\\n  - id: agent-omit2026\\n    title: \\\"Agent-Omit: Training Efficient LLM Agents for Adaptive Thought and Observation Omission via Agentic RL\\\"\\n    authors: \\\"Ning et al.\\\"\\n    venue: \\\"ICML 2026\\\"\\n    year: 2026\\n    arxiv_id: \\\"2602.04284\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      RL-trained policy for adaptive omission of redundant thoughts and observations.\\n      Agent-Omit-8B matches frontier agents with best efficiency tradeoff on 5 benchmarks.\\n      Both use RL to learn cost-efficient agent behavior. Key difference: Agent-Omit subtracts\\n      (omits unnecessary context); B-IAVR selectively adds (verification steps).\\n      Opposite but complementary approaches to cost-efficiency. Potentially combinable.\\n\\n  - id: ava2026\\n    title: \\\"Anytime Verified Agents: Adaptive Compute Allocation for Reliable LLM Reasoning under Budget Constraints\\\"\\n    authors: \\\"Patel\\\"\\n    venue: \\\"TMLR 2026\\\"\\n    year: 2026\\n    arxiv_id: null  # no arXiv preprint; OpenReview ID: JMDCMf7mlF\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      Dynamic compute allocation across search, sampling, and verification under budget.\\n      Uses calibrated uncertainty + value-of-information for selective verification cascades.\\n      Evaluated on GSM8K/MATH/HotpotQA/HumanEval (reasoning), not interactive agents.\\n      Key difference: analytical/heuristic allocation vs B-IAVR's RL-learned policy;\\n      single-turn reasoning vs multi-turn agent trajectories.\\n\\n  - id: cast2026\\n    title: \\\"CAST: Case-Based Calibration of Adaptive Reasoning and Execution for LLM Tool Use\\\"\\n    authors: \\\"Pang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2605.15041\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Historical execution cases calibrate reasoning depth for tool use.\\n      Reduces reasoning length 26% with +5.85% accuracy on BFCLv2/ToolBench.\\n      Related: adaptive reasoning depth; different: case-based calibration vs RL-learned policy.\\n\\n  - id: marginal-token-allocators2026\\n    title: \\\"Agentic AI Systems Should Be Designed as Marginal Token Allocators\\\"\\n    authors: \\\"Zhu\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2605.01214\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Position paper framing agent cost-efficiency as marginal token allocation economics.\\n      Identifies under-verification as systematic failure mode. Supports B-IAVR's framing\\n      that verification decisions should reflect marginal cost-benefit analysis.\\n\\n  - id: argos2025\\n    title: \\\"Argos: Multimodal RL with Adaptive Verifier for AI Agents\\\"\\n    authors: \\\"Tan et al.\\\"\\n    venue: \\\"arXiv (revised April 2026)\\\"\\n    year: 2025\\n    arxiv_id: \\\"2512.03438\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Agentic verifier that adaptively selects scoring functions for multimodal RL training.\\n      Different domain (multimodal/robotics). The adaptive verifier selection concept is\\n      complementary: Argos adapts how to verify; B-IAVR adapts when to verify.\\n\\n  # ============================================================\\n  # Direction 4: ALFWorld / Interactive Environment Benchmarks\\n  # ============================================================\\n\\n  - id: kim2025reflact\\n    title: \\\"ReflAct: World-Grounded Decision Making in LLM Agents via Goal-State Reflection\\\"\\n    authors: \\\"Kim et al.\\\"\\n    venue: \\\"EMNLP 2025\\\"\\n    year: 2025\\n    arxiv_id: \\\"2505.15182\\\"\\n    category: evaluation\\n    role: baseline\\n    relevance_note: >\\n      Prompting SOTA on ALFWorld at 93.3%. Replaces ReAct's next-action thinking with state-goal reflection.\\n      B-IAVR addresses different axis (cost-efficiency) since ALFWorld accuracy is near saturation.\\n\\n  - id: choudhury2025agentprm\\n    title: \\\"Process Reward Models for LLM Agents: Practical Framework and Directions\\\"\\n    authors: \\\"Choudhury\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2502.10325\\\"\\n    category: evaluation\\n    role: baseline\\n    relevance_note: >\\n      Monte Carlo rollout-based process reward for agent training. 3B models achieve 91% on ALFWorld.\\n      Validates RL training approach; AgentPRM could serve as reward model for B-IAVR.\\n\\n  - id: xi2025agentprm\\n    title: \\\"AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress\\\"\\n    authors: \\\"Xi et al.\\\"\\n    venue: \\\"ACM Web Conference 2026\\\"\\n    year: 2025\\n    arxiv_id: \\\"2511.08325\\\"\\n    category: evaluation\\n    role: baseline\\n    relevance_note: >\\n      Independent work from Choudhury et al., using TD-based estimation with GAE for scalable\\n      PRM data labeling. 8x more compute-efficient than baselines with robust test-time scaling.\\n      Different approach: Choudhury uses MC rollouts; Xi uses TD+GAE for step-wise promise and progress.\\n\\n  - id: xiang2024retrospex\\n    title: \\\"Retrospex: Language Agent Meets Offline RL Critic\\\"\\n    authors: \\\"Xiang et al.\\\"\\n    venue: \\\"EMNLP 2024\\\"\\n    year: 2024\\n    arxiv_id: \\\"2505.11807\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Offline RL Critic augments LLM agent action selection via dynamic rescoring.\\n      Similar architecture could inform B-IAVR's verification value estimation.\\n\\n  - id: cfgm2025\\n    title: \\\"CFGM: Coarse-to-Fine Grounded Memory for LLM Agent Planning\\\"\\n    authors: \\\"Yang et al.\\\"\\n    venue: \\\"EMNLP 2025\\\"\\n    year: 2025\\n    arxiv_id: \\\"2508.15305\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Memory-augmented agent planning with episodic grounding.\\n      ALFWorld +10.40%, WebShop +20%. Complementary to B-IAVR's verification approach.\\n\\n  - id: respact2024\\n    title: \\\"ReSpAct: Harmonizing Reasoning, Speaking, and Acting\\\"\\n    authors: \\\"Dongre et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2024\\n    arxiv_id: \\\"2411.00927\\\"\\n    category: evaluation\\n    role: baseline\\n    relevance_note: >\\n      Integrates dialogue/reasoning/acting. +6% over ReAct on ALFWorld.\\n      Reduces invalid actions from 13% to 3%; B-IAVR's verification achieves error prevention differently.\\n\\n  # ============================================================\\n  # Direction 5: Multi-Turn Credit Assignment (Direct Competitors)\\n  # ============================================================\\n\\n  - id: turn-ppo2025\\n    title: \\\"Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs\\\"\\n    authors: \\\"Li et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2512.17008\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      [NEW-0517] Most direct competitor. Identifies \\\"uniform advantage\\\" problem in\\n      step-independent GRPO (subset of our \\\"sign misattribution\\\"). Proposes turn-level\\n      MDP + learned value function. Our differences: (1) more precise formalization\\n      (sign misattribution + gamma decay quantification), (2) contrarian solution\\n      (episode-level coarser credit vs their finer turn-level credit).\\n\\n  - id: gagpo2026\\n    title: \\\"GAGPO: Generalized Advantage Grouped Policy Optimization\\\"\\n    authors: \\\"Zhu et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2605.13217\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      [NEW-0517] Critic-free step-aligned credit via non-parametric grouped value proxy +\\n      TD/GAE-style temporal advantages. ALFWorld 93.5% (1.5B), 95.6% (7B).\\n      Pursues finer-grained credit to improve performance; our work diagnoses why\\n      step-independent fails (sign misattribution) and shows coarser episode-level suffices.\\n      Different contribution axis: performance optimization vs mechanism diagnosis.\\n\\n  - id: mt-grpo2025\\n    title: \\\"Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Reward Design\\\"\\n    authors: \\\"Wei et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2505.11821\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      [NEW-0517] Proposes MT-GRPO with turn-level reward design for multi-turn RL.\\n      Evaluated on QA search tasks (NQ, TriviaQA, HotpotQA), not ALFWorld.\\n      Qwen2.5-7B. Same direction as Turn-PPO (finer turn-level credit);\\n      our contrarian shows coarser episode-level eliminates sign misattribution.\\n\\n  - id: istar2025\\n    title: \\\"Agentic Reinforcement Learning with Implicit Step Rewards\\\"\\n    authors: \\\"Liu et al.\\\"\\n    venue: \\\"ICLR 2026\\\"\\n    year: 2025\\n    arxiv_id: \\\"2509.19199\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      [NEW-0517] Implicit PRM + dual advantage (step + episode level) for agentic RL.\\n      WebShop 86.5%, VisualSokoban 91.7%. ICLR 2026 published.\\n      Learns step-level credit via implicit rewards without explicit labels;\\n      our work shows episode-level alone suffices when sign misattribution is the bottleneck.\\n      Validates that step-level credit helps, but doesn't diagnose when it hurts.\\n\\n  - id: archer2024\\n    title: \\\"ArCHer: Training Language Model Agents via Hierarchical Multi-Turn RL\\\"\\n    authors: \\\"Zhou, Zanette, Pan, Levine, Kumar\\\"\\n    venue: \\\"ICML 2024\\\"\\n    year: 2024\\n    arxiv_id: \\\"2402.19446\\\"\\n    category: method-component\\n    role: predecessor\\n    relevance_note: >\\n      [NEW-0517] Foundational hierarchical multi-turn RL framework (ICML 2024).\\n      High-level off-policy value RL (utterance-level) + low-level token policy.\\n      ~100x sample efficiency. Establishes that multi-turn RL needs hierarchical structure;\\n      our work specifically diagnoses why flat step-independent approaches fail.\\n\\n  - id: ca-survey2026\\n    title: \\\"From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models\\\"\\n    authors: \\\"Zhang\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2604.09459\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      [NEW-0517] Comprehensive survey of 47 CA methods (2024-2026). Two-dimensional\\n      taxonomy: granularity (token/segment/step/turn/multi-agent) x methodology\\n      (MC/TD/model-based/game-theoretic/information-theoretic). Contextualizes our\\n      sign misattribution diagnosis within the broader CA landscape.\\n\\n  - id: hiper2026\\n    title: \\\"HiPER: Hierarchical Reinforcement Learning with Explicit Credit Assignment for Large Language Model Agents\\\"\\n    authors: \\\"Peng et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2602.16165\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      [NEW-0517] Hierarchical Plan-Execute RL. ALFWorld 97.4% (7B), 95.3% (1.5B).\\n      GRPO baseline: 71.1% (1.5B), 85.4% (7B). 2.8x training efficiency gain.\\n      Pursues SOTA performance via hierarchical plan-execute architecture;\\n      our work does mechanism diagnosis of why step-independent GRPO fails.\\n      Different contribution dimension: not comparable on performance axis.\\n\", \"total_chars\": 29932, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "275cbfdc-1995-4234-8cbe-f7128f56169c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/literature_map.yaml\\\", \\\"content\\\": \\\"# B-IAVR Literature Map\\\\n# Updated: 2026-05-17\\\\n# Categories: direct-competitor, method-component, background, evaluation\\\\n# Roles: predecessor, competitor, baseline, evaluation, background\\\\n\\\\npapers:\\\\n\\\\n  # ============================================================\\\\n  # Direction 1: Self-Verification / Self-Correction in LLM Agents\\\\n  # ============================================================\\\\n\\\\n  - id: kamoi2024self-correction-survey\\\\n    title: \\\\\\\"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs\\\\\\\"\\\\n    authors: \\\\\\\"Kamoi et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2024\\\\n    arxiv_id: \\\\\\\"2406.01297\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      Foundational survey establishing that pure intrinsic self-correction is unreliable.\\\\n      Validates B-IAVR's use of grounded verification (environment re-observation) over prompted self-feedback.\\\\n\\\\n  - id: tie2025correctbench\\\\n    title: \\\\\\\"Can LLMs Correct Themselves? A Benchmark of Self-Correction in LLMs\\\\\\\"\\\\n    authors: \\\\\\\"Tie et al.\\\\\\\"\\\\n    venue: \\\\\\\"NeurIPS 2025 Datasets & Benchmarks\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2510.16062\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      Benchmark showing self-correction has diminishing returns when applied uniformly.\\\\n      Supports B-IAVR's selective verification design over blanket correction.\\\\n\\\\n  - id: self-verification-dilemma-2026\\\\n    title: \\\\\\\"Self-Verification Dilemma: Experience-Driven Suppression of Overused Checking in LLM Reasoning\\\\\\\"\\\\n    authors: \\\\\\\"Long et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: \\\\\\\"2602.03485\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      Empirically validates that >90% of self-verification is confirmatory, ~2% corrective.\\\\n      Directly supports B-IAVR's core thesis that verification should be selective.\\\\n      Their experience-pool approach is complementary to B-IAVR's action-change signal.\\\\n\\\\n  - id: zhang2025incentivize-self-verify\\\\n    title: \\\\\\\"Incentivizing LLMs to Self-Verify Their Answers\\\\\\\"\\\\n    authors: \\\\\\\"Zhang et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2506.01369\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      Unifies answer generation and verification via single RL training process.\\\\n      Parallel to B-IAVR: they train verification into generation; B-IAVR trains when to trigger separate verification.\\\\n\\\\n  - id: mar2025\\\\n    title: \\\\\\\"MAR: Multi-Agent Reflexion Improves Reasoning Abilities in LLMs\\\\\\\"\\\\n    authors: \\\\\\\"Ozer et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2512.20845\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      Multi-agent self-correction with diverse critic personas.\\\\n      Complementary: MAR improves correction quality; B-IAVR decides when to trigger correction.\\\\n\\\\n  - id: ssr2025\\\\n    title: \\\\\\\"SSR: Socratic Self-Refine for Large Language Model Reasoning\\\\\\\"\\\\n    authors: \\\\\\\"Shi et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2511.10621\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      Structured Socratic questioning for self-refinement.\\\\n      Complementary: improves correction step quality; B-IAVR focuses on when to invoke correction.\\\\n\\\\n  - id: verifiagent2025\\\\n    title: \\\\\\\"VerifiAgent: a Unified Verification Agent in Language Model Reasoning\\\\\\\"\\\\n    authors: \\\\\\\"Han et al.\\\\\\\"\\\\n    venue: \\\\\\\"EMNLP 2025 Findings\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2504.00406\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      Unified verification agent with meta-verification + tool-based adaptive verification.\\\\n      Focuses on how to verify (tool selection); B-IAVR focuses on when to verify (policy learning).\\\\n      Complementary: VerifiAgent's verification quality could enhance B-IAVR's verification step.\\\\n\\\\n  # ============================================================\\\\n  # Direction 2: Agent RL Training\\\\n  # ============================================================\\\\n\\\\n  - id: feng2025gigpo\\\\n    title: \\\\\\\"GiGPO: Group-in-Group Policy Optimization for LLM Agent Training\\\\\\\"\\\\n    authors: \\\\\\\"Feng et al.\\\\\\\"\\\\n    venue: \\\\\\\"NeurIPS 2025\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2505.10978\\\\\\\"\\\\n    category: method-component\\\\n    role: predecessor\\\\n    relevance_note: >\\\\n      Core training algorithm for B-IAVR. Nested group structure provides step-level credit\\\\n      assignment without learned critic. >12% over GRPO on ALFWorld, >9% on WebShop.\\\\n\\\\n  - id: selfguide2026\\\\n    title: \\\\\\\"Co-Evolution of Policy and Internal Reward for Language Agents (Self-Guide)\\\\\\\"\\\\n    authors: \\\\\\\"Wang et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: \\\\\\\"2604.03098\\\\\\\"\\\\n    category: method-component\\\\n    role: predecessor\\\\n    relevance_note: >\\\\n      Direct predecessor. B-IAVR extends Self-Guide's co-evolving internal reward.\\\\n      The self-guidance signal is the foundation for action-change detection triggering verification.\\\\n      8% improvement over env-reward-only on ALFWorld with Qwen3-1.7B/4B.\\\\n\\\\n  - id: spear2025\\\\n    title: \\\\\\\"Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning\\\\\\\"\\\\n    authors: \\\\\\\"Qin et al.\\\\\\\"\\\\n    venue: \\\\\\\"ICLR 2026\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2509.22601\\\\\\\"\\\\n    category: method-component\\\\n    role: background\\\\n    relevance_note: >\\\\n      Curriculum-based self-imitation for sparse-reward agent tasks.\\\\n      Up to +16.1% on ALFWorld over GRPO. Self-imitation curriculum could augment B-IAVR training.\\\\n\\\\n  - id: wei2025webagent-r1\\\\n    title: \\\\\\\"WebAgent-R1: Training Web Agents via End-to-End Multi-Turn RL\\\\\\\"\\\\n    authors: \\\\\\\"Wei et al.\\\\\\\"\\\\n    venue: \\\\\\\"EMNLP 2025\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2505.16421\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      Extends GRPO to multi-turn (M-GRPO) with dynamic context compression.\\\\n      Qwen-2.5-3B: 6.1% to 33.9% on WebArena-Lite. M-GRPO multi-turn extension relevant to B-IAVR.\\\\n\\\\n  - id: dapo2025\\\\n    title: \\\\\\\"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\\\\\\\"\\\\n    authors: \\\\\\\"Yu et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2503.14476\\\\\\\"\\\\n    category: method-component\\\\n    role: background\\\\n    relevance_note: >\\\\n      RL training stabilization techniques (Clip-Higher, Dynamic Sampling).\\\\n      Applicable to B-IAVR's RL training to prevent entropy collapse.\\\\n\\\\n  - id: digiRL2024\\\\n    title: \\\\\\\"DigiRL: Training In-The-Wild Device-Control Agents with Autonomous RL\\\\\\\"\\\\n    authors: \\\\\\\"Bai et al.\\\\\\\"\\\\n    venue: \\\\\\\"NeurIPS 2024\\\\\\\"\\\\n    year: 2024\\\\n    arxiv_id: \\\\\\\"2406.11896\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      Online RL for device control agents. Demonstrates online RL viability for interactive agents.\\\\n      49.5% absolute improvement over SFT. Parallel approach to B-IAVR in text-based setting.\\\\n\\\\n  - id: li2025sorl\\\\n    title: \\\\\\\"SORL: Stabilizing Off-Policy RL for Long-Horizon Agent Training\\\\\\\"\\\\n    authors: \\\\\\\"Li et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2511.20718\\\\\\\"\\\\n    category: method-component\\\\n    role: background\\\\n    relevance_note: >\\\\n      Turn-level importance sampling + clipping-triggered normalization for stable multi-turn agent RL.\\\\n      Directly applicable to B-IAVR's multi-turn ALFWorld training stability.\\\\n\\\\n  - id: agentic-rl-survey-2025\\\\n    title: \\\\\\\"The Landscape of Agentic Reinforcement Learning for LLMs: A Survey\\\\\\\"\\\\n    authors: \\\\\\\"Zhang et al.\\\\\\\"\\\\n    venue: \\\\\\\"TMLR 2026\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2509.02547\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      Comprehensive survey formalizing agentic RL. Contextualizes B-IAVR as training agents\\\\n      to make meta-decisions (when to verify) via RL within the POMDP framework.\\\\n\\\\n  - id: skillmaster2026\\\\n    title: \\\\\\\"SkillMaster: Toward Autonomous Skill Mastery in LLM Agents\\\\\\\"\\\\n    authors: \\\\\\\"Yang et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: \\\\\\\"2605.08693\\\\\\\"\\\\n    category: method-component\\\\n    role: background\\\\n    relevance_note: >\\\\n      DualAdv-GRPO: separately estimates advantages for task-solving and skill-editing decisions.\\\\n      +8.8% on ALFWorld, +9.3% on WebShop. DualAdv structure could inform B-IAVR's\\\\n      separation of action and verification advantages.\\\\n\\\\n  - id: t2po2026\\\\n    title: \\\\\\\"T2PO: Uncertainty-Guided Exploration Control for Stable Multi-Turn Agentic RL\\\\\\\"\\\\n    authors: \\\\\\\"Wang et al.\\\\\\\"\\\\n    venue: \\\\\\\"ICML 2026 Spotlight\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: \\\\\\\"2605.02178\\\\\\\"\\\\n    category: method-component\\\\n    role: background\\\\n    relevance_note: >\\\\n      Token- and turn-level uncertainty monitoring for stable multi-turn agent RL.\\\\n      Triggers thinking intervention when marginal uncertainty change drops below threshold.\\\\n      Evaluated on ALFWorld and WebShop. Conceptually related: uncertainty-based trigger vs\\\\n      B-IAVR's action-change trigger, but T2PO targets training stability, not deployment verification.\\\\n\\\\n  - id: gvpo2026\\\\n    title: \\\\\\\"GVPO: Group Verification-based Policy Optimization for Interactive Coding Agents\\\\\\\"\\\\n    authors: \\\\\\\"Dai et al.\\\\\\\"\\\\n    venue: \\\\\\\"ICLR 2026\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: null  # no arXiv preprint; OpenReview ID: RY47Tq0VsV\\\\n    category: method-component\\\\n    role: background\\\\n    relevance_note: >\\\\n      Advantage shaping with outcome-verifiable + process-verifiable signals.\\\\n      +12.7% over o1 on AppWorld. Integrates intermediate execution feedback as step-level\\\\n      verification signals. Different focus: uses verification for credit assignment during\\\\n      training; B-IAVR learns when to invoke verification at deployment.\\\\n\\\\n  - id: agentv-rl2026\\\\n    title: \\\\\\\"AgentV-RL: Scaling Reward Modeling with Agentic Verifier\\\\\\\"\\\\n    authors: \\\\\\\"Zhang et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: \\\\\\\"2604.16004\\\\\\\"\\\\n    category: method-component\\\\n    role: background\\\\n    relevance_note: >\\\\n      Bidirectional forward/backward agentic verifier for reward modeling in RL.\\\\n      4B model surpasses SOTA ORMs by 25.2%. Addresses verification quality in reward modeling;\\\\n      B-IAVR addresses verification timing in agent deployment. Complementary.\\\\n\\\\n  - id: pa-moe2026\\\\n    title: \\\\\\\"PA-MoE: Phase-Aware Mixture of Experts for Agentic Reinforcement Learning\\\\\\\"\\\\n    authors: \\\\\\\"Li et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: \\\\\\\"2602.17038\\\\\\\"\\\\n    category: evaluation\\\\n    role: baseline\\\\n    relevance_note: >\\\\n      [NEW-0516] Lightweight phase router learns latent phase boundaries from RL objective.\\\\n      PA-MoE+GiGPO with Qwen2.5-1.5B achieves 93.8% on ALFWorld (+7.7 over GiGPO 86.1%).\\\\n      1.5B outperforms vanilla 7B GiGPO (90.2%). New small-model SOTA on ALFWorld.\\\\n      Orthogonal architecture innovation; important baseline to cite.\\\\n\\\\n  - id: sdar2026\\\\n    title: \\\\\\\"SDAR: Self-Distilled Agentic Reinforcement Learning\\\\\\\"\\\\n    authors: \\\\\\\"Lu et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: \\\\\\\"2605.15155\\\\\\\"\\\\n    category: method-component\\\\n    role: background\\\\n    relevance_note: >\\\\n      [NEW-0516] On-policy self-distillation as gated auxiliary objective during RL training.\\\\n      Token-level gate decides supervision intensity. +9.4% over GRPO on ALFWorld.\\\\n      Complementary: SDAR improves RL training; B-IAVR learns verification policy.\\\\n\\\\n  - id: hcapo2026\\\\n    title: \\\\\\\"HCAPO: Hindsight Credit Assignment for Long-Horizon LLM Agents\\\\\\\"\\\\n    authors: \\\\\\\"Tan et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: \\\\\\\"2603.08754\\\\\\\"\\\\n    category: method-component\\\\n    role: background\\\\n    relevance_note: >\\\\n      [NEW-0516] LLM-as-critic refines step-level Q-values via hindsight reasoning +\\\\n      multi-scale advantage for critical decision states.\\\\n      +13.8% on ALFWorld, +7.7% on WebShop over GRPO (Qwen2.5-7B).\\\\n      Could improve B-IAVR's reward signal for verification decision steps.\\\\n\\\\n  - id: act2026\\\\n    title: \\\\\\\"ACT: Agentic Critical Training\\\\\\\"\\\\n    authors: \\\\\\\"Liu et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: \\\\\\\"2603.08706\\\\\\\"\\\\n    category: method-component\\\\n    role: background\\\\n    relevance_note: >\\\\n      [NEW-0516] Trains agents to judge action quality via critical comparison reward.\\\\n      +5.07 over IL, +4.62 over RL. Different axis: ACT improves reflection quality;\\\\n      B-IAVR decides when to reflect.\\\\n\\\\n  - id: rwml2026\\\\n    title: \\\\\\\"RWML: Reinforcement World Model Learning for LLM-based Agents\\\\\\\"\\\\n    authors: \\\\\\\"Yu et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: \\\\\\\"2602.05842\\\\\\\"\\\\n    category: method-component\\\\n    role: background\\\\n    relevance_note: >\\\\n      [NEW-0516] Self-supervised world model via sim-to-real gap rewards in embedding space.\\\\n      +6.9 on ALFWorld over task-success-only RL. Matches expert-data training.\\\\n      Orthogonal: improves internal world model; B-IAVR adds selective verification.\\\\n\\\\n  - id: skill0-2026\\\\n    title: \\\\\\\"SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization\\\\\\\"\\\\n    authors: \\\\\\\"Lu et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: \\\\\\\"2604.02268\\\\\\\"\\\\n    category: method-component\\\\n    role: background\\\\n    relevance_note: >\\\\n      [NEW-0516] Training-time curriculum progressively withdraws skill context until zero-shot.\\\\n      +9.7% on ALFWorld over GRPO, <0.5k tokens per step.\\\\n      Complementary: SKILL0 internalizes skills; B-IAVR adds selective verification.\\\\n\\\\n  - id: fission-grpo2026\\\\n    title: \\\\\\\"Fission-GRPO: Robust Tool Use via Learning to Recover from Execution Errors\\\\\\\"\\\\n    authors: \\\\\\\"Zhang et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: \\\\\\\"2601.15625\\\\\\\"\\\\n    category: method-component\\\\n    role: background\\\\n    relevance_note: >\\\\n      [NEW-0516] Fissions failed trajectories into recovery training instances.\\\\n      +4% overall accuracy on BFCL v4 Multi-Turn over GRPO.\\\\n      Related: error recovery after failure vs B-IAVR's proactive verification.\\\\n\\\\n  - id: selfbudgeter2026\\\\n    title: \\\\\\\"SelfBudgeter: Adaptive Token Allocation for Efficient LLM Reasoning\\\\\\\"\\\\n    authors: \\\\\\\"Li et al.\\\\\\\"\\\\n    venue: \\\\\\\"ICLR 2026 (under review)\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2505.11274\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      [NEW-0516] Self-estimated token budgets + budget-guided GRPO. 61% token reduction.\\\\n      Parallel concept: SelfBudgeter allocates computation budget;\\\\n      B-IAVR makes binary verify/not-verify decision. Both use RL for adaptive compute.\\\\n\\\\n  - id: cove2026\\\\n    title: \\\\\\\"CoVe: Training Interactive Tool-Use Agents via Constraint-Guided Verification\\\\\\\"\\\\n    authors: \\\\\\\"Chen et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: \\\\\\\"2603.01940\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      [NEW-0516] Task constraints guide trajectory generation and serve as deterministic verifiers.\\\\n      Different: CoVe uses verification for data synthesis; B-IAVR learns when to verify at inference.\\\\n\\\\n  # ============================================================\\\\n  # Direction 3: Selective Verification / Adaptive Computation\\\\n  # ============================================================\\\\n\\\\n  - id: wan2025derailer-rerailer\\\\n    title: \\\\\\\"Derailer-Rerailer: Adaptive Verification for Efficient and Reliable LM Reasoning\\\\\\\"\\\\n    authors: \\\\\\\"Wan et al.\\\\\\\"\\\\n    venue: \\\\\\\"ACL 2025 Findings\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2408.13940\\\\\\\"\\\\n    category: direct-competitor\\\\n    role: competitor\\\\n    relevance_note: >\\\\n      Most directly related competitor. Both do selective verification with binary trigger.\\\\n      Key difference: operates on reasoning chains (single-turn); B-IAVR on agent trajectories (multi-turn).\\\\n      Uses heuristic instability signal; B-IAVR uses RL-trained action-change signal.\\\\n      8-11% accuracy gain, 2-3x efficiency over uniform verification.\\\\n\\\\n  - id: sherlock2025\\\\n    title: \\\\\\\"Sherlock: Reliable and Efficient Agentic Workflow Execution\\\\\\\"\\\\n    authors: \\\\\\\"Microsoft\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2511.00330\\\\\\\"\\\\n    category: direct-competitor\\\\n    role: competitor\\\\n    relevance_note: >\\\\n      Selective verification for agentic workflows via offline counterfactual analysis + speculative execution.\\\\n      Different scope: workflow DAG level (offline); B-IAVR is step-level (online RL).\\\\n      18.3% accuracy gain, 26% cost reduction, 48.7% latency reduction.\\\\n\\\\n  - id: singhi2025when-to-verify\\\\n    title: \\\\\\\"When To Solve, When To Verify: Compute-Optimal Verification for LLM Reasoning\\\\\\\"\\\\n    authors: \\\\\\\"Singhi et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2504.01005\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      Derives inference scaling laws for solve-vs-verify tradeoff.\\\\n      Finding that over-verification is suboptimal directly supports B-IAVR's selective approach.\\\\n      B-IAVR learns this allocation via RL rather than analytically.\\\\n\\\\n  - id: yang2026ares\\\\n    title: \\\\\\\"ARES: Adaptive Reasoning Effort Selection for Efficient LLM Agents\\\\\\\"\\\\n    authors: \\\\\\\"Yang et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: \\\\\\\"2603.07915\\\\\\\"\\\\n    category: direct-competitor\\\\n    role: competitor\\\\n    relevance_note: >\\\\n      Closest competitor in agent domain. Both train learned per-step compute allocation.\\\\n      ARES uses SFT-initialized router further refined via GRPO with outcome + token efficiency reward;\\\\n      B-IAVR trains binary verify/not-verify via RL with action-change signal.\\\\n      Key differences: (1) reward signal — ARES optimizes token efficiency, B-IAVR uses action-change\\\\n      as verification trigger; (2) data requirement — ARES needs difficulty-annotated training data\\\\n      to bootstrap the router, B-IAVR learns from environment interaction alone.\\\\n      Reduces reasoning tokens by up to 52.7%.\\\\n\\\\n  - id: tu2025autothink\\\\n    title: \\\\\\\"Learning When to Think: Shaping Adaptive Reasoning in R1-Style Models via Multi-Stage RL\\\\\\\"\\\\n    authors: \\\\\\\"Tu et al.\\\\\\\"\\\\n    venue: \\\\\\\"NeurIPS 2025\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2505.10832\\\\\\\"\\\\n    category: direct-competitor\\\\n    role: competitor\\\\n    relevance_note: >\\\\n      Analogous idea in reasoning domain: RL-trained adaptive computation trigger.\\\\n      Operates on single-turn reasoning; B-IAVR on multi-turn agent trajectories.\\\\n      +6.4% accuracy, -52% tokens on DeepSeek-R1-Distill-Qwen-1.5B.\\\\n\\\\n  - id: du2025thinkless\\\\n    title: \\\\\\\"Thinkless: LLM Learns When to Think\\\\\\\"\\\\n    authors: \\\\\\\"Fang et al.\\\\\\\"\\\\n    venue: \\\\\\\"NeurIPS 2025\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2505.13379\\\\\\\"\\\\n    category: direct-competitor\\\\n    role: competitor\\\\n    relevance_note: >\\\\n      RL-trained control token to decide when to invoke extended thinking.\\\\n      Methodologically closest to B-IAVR in reasoning domain; B-IAVR applies to interactive agent trajectories.\\\\n\\\\n  - id: wang2025efficient-agents\\\\n    title: \\\\\\\"Efficient Agents: Building Effective Agents While Reducing Cost\\\\\\\"\\\\n    authors: \\\\\\\"Wang et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2508.02694\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      First systematic study of agent efficiency-effectiveness tradeoff.\\\\n      Framework-level cost reduction; B-IAVR addresses cost at verification-policy level.\\\\n      Retains 96.7% performance with 28.4% cost-of-pass improvement.\\\\n\\\\n  - id: venktesh2025trust-but-verify\\\\n    title: \\\\\\\"Trust but Verify! A Survey on Verification Design for Test-time Scaling\\\\\\\"\\\\n    authors: \\\\\\\"Venktesh et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2508.16665\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      Survey of verification approaches for test-time compute scaling.\\\\n      Identifies verification timing as key open problem. B-IAVR provides concrete solution for agent setting.\\\\n\\\\n  - id: agent-omit2026\\\\n    title: \\\\\\\"Agent-Omit: Training Efficient LLM Agents for Adaptive Thought and Observation Omission via Agentic RL\\\\\\\"\\\\n    authors: \\\\\\\"Ning et al.\\\\\\\"\\\\n    venue: \\\\\\\"ICML 2026\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: \\\\\\\"2602.04284\\\\\\\"\\\\n    category: direct-competitor\\\\n    role: competitor\\\\n    relevance_note: >\\\\n      RL-trained policy for adaptive omission of redundant thoughts and observations.\\\\n      Agent-Omit-8B matches frontier agents with best efficiency tradeoff on 5 benchmarks.\\\\n      Both use RL to learn cost-efficient agent behavior. Key difference: Agent-Omit subtracts\\\\n      (omits unnecessary context); B-IAVR selectively adds (verification steps).\\\\n      Opposite but complementary approaches to cost-efficiency. Potentially combinable.\\\\n\\\\n  - id: ava2026\\\\n    title: \\\\\\\"Anytime Verified Agents: Adaptive Compute Allocation for Reliable LLM Reasoning under Budget Constraints\\\\\\\"\\\\n    authors: \\\\\\\"Patel\\\\\\\"\\\\n    venue: \\\\\\\"TMLR 2026\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: null  # no arXiv preprint; OpenReview ID: JMDCMf7mlF\\\\n    category: direct-competitor\\\\n    role: competitor\\\\n    relevance_note: >\\\\n      Dynamic compute allocation across search, sampling, and verification under budget.\\\\n      Uses calibrated uncertainty + value-of-information for selective verification cascades.\\\\n      Evaluated on GSM8K/MATH/HotpotQA/HumanEval (reasoning), not interactive agents.\\\\n      Key difference: analytical/heuristic allocation vs B-IAVR's RL-learned policy;\\\\n      single-turn reasoning vs multi-turn agent trajectories.\\\\n\\\\n  - id: cast2026\\\\n    title: \\\\\\\"CAST: Case-Based Calibration of Adaptive Reasoning and Execution for LLM Tool Use\\\\\\\"\\\\n    authors: \\\\\\\"Pang et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: \\\\\\\"2605.15041\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      Historical execution cases calibrate reasoning depth for tool use.\\\\n      Reduces reasoning length 26% with +5.85% accuracy on BFCLv2/ToolBench.\\\\n      Related: adaptive reasoning depth; different: case-based calibration vs RL-learned policy.\\\\n\\\\n  - id: marginal-token-allocators2026\\\\n    title: \\\\\\\"Agentic AI Systems Should Be Designed as Marginal Token Allocators\\\\\\\"\\\\n    authors: \\\\\\\"Zhu\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: \\\\\\\"2605.01214\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      Position paper framing agent cost-efficiency as marginal token allocation economics.\\\\n      Identifies under-verification as systematic failure mode. Supports B-IAVR's framing\\\\n      that verification decisions should reflect marginal cost-benefit analysis.\\\\n\\\\n  - id: argos2025\\\\n    title: \\\\\\\"Argos: Multimodal RL with Adaptive Verifier for AI Agents\\\\\\\"\\\\n    authors: \\\\\\\"Tan et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv (revised April 2026)\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2512.03438\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      Agentic verifier that adaptively selects scoring functions for multimodal RL training.\\\\n      Different domain (multimodal/robotics). The adaptive verifier selection concept is\\\\n      complementary: Argos adapts how to verify; B-IAVR adapts when to verify.\\\\n\\\\n  # ============================================================\\\\n  # Direction 4: ALFWorld / Interactive Environment Benchmarks\\\\n  # ============================================================\\\\n\\\\n  - id: kim2025reflact\\\\n    title: \\\\\\\"ReflAct: World-Grounded Decision Making in LLM Agents via Goal-State Reflection\\\\\\\"\\\\n    authors: \\\\\\\"Kim et al.\\\\\\\"\\\\n    venue: \\\\\\\"EMNLP 2025\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2505.15182\\\\\\\"\\\\n    category: evaluation\\\\n    role: baseline\\\\n    relevance_note: >\\\\n      Prompting SOTA on ALFWorld at 93.3%. Replaces ReAct's next-action thinking with state-goal reflection.\\\\n      B-IAVR addresses different axis (cost-efficiency) since ALFWorld accuracy is near saturation.\\\\n\\\\n  - id: choudhury2025agentprm\\\\n    title: \\\\\\\"Process Reward Models for LLM Agents: Practical Framework and Directions\\\\\\\"\\\\n    authors: \\\\\\\"Choudhury\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2502.10325\\\\\\\"\\\\n    category: evaluation\\\\n    role: baseline\\\\n    relevance_note: >\\\\n      Monte Carlo rollout-based process reward for agent training. 3B models achieve 91% on ALFWorld.\\\\n      Validates RL training approach; AgentPRM could serve as reward model for B-IAVR.\\\\n\\\\n  - id: xi2025agentprm\\\\n    title: \\\\\\\"AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress\\\\\\\"\\\\n    authors: \\\\\\\"Xi et al.\\\\\\\"\\\\n    venue: \\\\\\\"ACM Web Conference 2026\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2511.08325\\\\\\\"\\\\n    category: evaluation\\\\n    role: baseline\\\\n    relevance_note: >\\\\n      Independent work from Choudhury et al., using TD-based estimation with GAE for scalable\\\\n      PRM data labeling. 8x more compute-efficient than baselines with robust test-time scaling.\\\\n      Different approach: Choudhury uses MC rollouts; Xi uses TD+GAE for step-wise promise and progress.\\\\n\\\\n  - id: xiang2024retrospex\\\\n    title: \\\\\\\"Retrospex: Language Agent Meets Offline RL Critic\\\\\\\"\\\\n    authors: \\\\\\\"Xiang et al.\\\\\\\"\\\\n    venue: \\\\\\\"EMNLP 2024\\\\\\\"\\\\n    year: 2024\\\\n    arxiv_id: \\\\\\\"2505.11807\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      Offline RL Critic augments LLM agent action selection via dynamic rescoring.\\\\n      Similar architecture could inform B-IAVR's verification value estimation.\\\\n\\\\n  - id: cfgm2025\\\\n    title: \\\\\\\"CFGM: Coarse-to-Fine Grounded Memory for LLM Agent Planning\\\\\\\"\\\\n    authors: \\\\\\\"Yang et al.\\\\\\\"\\\\n    venue: \\\\\\\"EMNLP 2025\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2508.15305\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      Memory-augmented agent planning with episodic grounding.\\\\n      ALFWorld +10.40%, WebShop +20%. Complementary to B-IAVR's verification approach.\\\\n\\\\n  - id: respact2024\\\\n    title: \\\\\\\"ReSpAct: Harmonizing Reasoning, Speaking, and Acting\\\\\\\"\\\\n    authors: \\\\\\\"Dongre et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2024\\\\n    arxiv_id: \\\\\\\"2411.00927\\\\\\\"\\\\n    category: evaluation\\\\n    role: baseline\\\\n    relevance_note: >\\\\n      Integrates dialogue/reasoning/acting. +6% over ReAct on ALFWorld.\\\\n      Reduces invalid actions from 13% to 3%; B-IAVR's verification achieves error prevention differently.\\\\n\\\\n  # ============================================================\\\\n  # Direction 5: Multi-Turn Credit Assignment (Direct Competitors)\\\\n  # ============================================================\\\\n\\\\n  - id: turn-ppo2025\\\\n    title: \\\\\\\"Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs\\\\\\\"\\\\n    authors: \\\\\\\"Li et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2512.17008\\\\\\\"\\\\n    category: direct-competitor\\\\n    role: competitor\\\\n    relevance_note: >\\\\n      [NEW-0517] Most direct competitor. Identifies \\\\\\\"uniform advantage\\\\\\\" problem in\\\\n      step-independent GRPO (subset of our \\\\\\\"sign misattribution\\\\\\\"). Proposes turn-level\\\\n      MDP + learned value function. Our differences: (1) more precise formalization\\\\n      (sign misattribution + gamma decay quantification), (2) contrarian solution\\\\n      (episode-level coarser credit vs their finer turn-level credit).\\\\n\\\\n  - id: gagpo2026\\\\n    title: \\\\\\\"GAGPO: Generalized Advantage Grouped Policy Optimization\\\\\\\"\\\\n    authors: \\\\\\\"Zhu et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: \\\\\\\"2605.13217\\\\\\\"\\\\n    category: direct-competitor\\\\n    role: competitor\\\\n    relevance_note: >\\\\n      [NEW-0517] Critic-free step-aligned credit via non-parametric grouped value proxy +\\\\n      TD/GAE-style temporal advantages. ALFWorld 93.5% (1.5B), 95.6% (7B).\\\\n      Pursues finer-grained credit to improve performance; our work diagnoses why\\\\n      step-independent fails (sign misattribution) and shows coarser episode-level suffices.\\\\n      Different contribution axis: performance optimization vs mechanism diagnosis.\\\\n\\\\n  - id: mt-grpo2025\\\\n    title: \\\\\\\"Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Reward Design\\\\\\\"\\\\n    authors: \\\\\\\"Wei et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2505.11821\\\\\\\"\\\\n    category: direct-competitor\\\\n    role: competitor\\\\n    relevance_note: >\\\\n      [NEW-0517] Proposes MT-GRPO with turn-level reward design for multi-turn RL.\\\\n      Evaluated on QA search tasks (NQ, TriviaQA, HotpotQA), not ALFWorld.\\\\n      Qwen2.5-7B. Same direction as Turn-PPO (finer turn-level credit);\\\\n      our contrarian shows coarser episode-level eliminates sign misattribution.\\\\n\\\\n  - id: istar2025\\\\n    title: \\\\\\\"Agentic Reinforcement Learning with Implicit Step Rewards\\\\\\\"\\\\n    authors: \\\\\\\"Liu et al.\\\\\\\"\\\\n    venue: \\\\\\\"ICLR 2026\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2509.19199\\\\\\\"\\\\n    category: direct-competitor\\\\n    role: competitor\\\\n    relevance_note: >\\\\n      [NEW-0517] Implicit PRM + dual advantage (step + episode level) for agentic RL.\\\\n      WebShop 86.5%, VisualSokoban 91.7%. ICLR 2026 published.\\\\n      Learns step-level credit via implicit rewards without explicit labels;\\\\n      our work shows episode-level alone suffices when sign misattribution is the bottleneck.\\\\n      Validates that step-level credit helps, but doesn't diagnose when it hurts.\\\\n\\\\n  - id: archer2024\\\\n    title: \\\\\\\"ArCHer: Training Language Model Agents via Hierarchical Multi-Turn RL\\\\\\\"\\\\n    authors: \\\\\\\"Zhou, Zanette, Pan, Levine, Kumar\\\\\\\"\\\\n    venue: \\\\\\\"ICML 2024\\\\\\\"\\\\n    year: 2024\\\\n    arxiv_id: \\\\\\\"2402.19446\\\\\\\"\\\\n    category: method-component\\\\n    role: predecessor\\\\n    relevance_note: >\\\\n      [NEW-0517] Foundational hierarchical multi-turn RL framework (ICML 2024).\\\\n      High-level off-policy value RL (utterance-level) + low-level token policy.\\\\n      ~100x sample efficiency. Establishes that multi-turn RL needs hierarchical structure;\\\\n      our work specifically diagnoses why flat step-independent approaches fail.\\\\n\\\\n  - id: ca-survey2026\\\\n    title: \\\\\\\"From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models\\\\\\\"\\\\n    authors: \\\\\\\"Zhang\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: \\\\\\\"2604.09459\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      [NEW-0517] Comprehensive survey of 47 CA methods (2024-2026). Two-dimensional\\\\n      taxonomy: granularity (token/segment/step/turn/multi-agent) x methodology\\\\n      (MC/TD/model-based/game-theoretic/information-theoretic). Contextualizes our\\\\n      sign misattribution diagnosis within the broader CA landscape.\\\\n\\\\n  - id: hiper2026\\\\n    title: \\\\\\\"HiPER: Hierarchical Reinforcement Learning with Explicit Credit Assignment for Large Language Model Agents\\\\\\\"\\\\n    authors: \\\\\\\"Peng et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: \\\\\\\"2602.16165\\\\\\\"\\\\n    category: method-component\\\\n    role: background\\\\n    relevance_note: >\\\\n      [NEW-0517] Hierarchical Plan-Execute RL. ALFWorld 97.4% (7B), 95.3% (1.5B).\\\\n      GRPO baseline: 71.1% (1.5B), 85.4% (7B). 2.8x training efficiency gain.\\\\n      Pursues SOTA performance via hierarchical plan-execute architecture;\\\\n      our work does mechanism diagnosis of why step-independent GRPO fails.\\\\n      Different contribution dimension: not comparable on performance axis.\\\\n\\\", \\\"total_chars\\\": 29932, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/literature_map.yaml\", \"content\": \"# B-IAVR Literature Map\\n# Updated: 2026-05-17\\n# Categories: direct-competitor, method-component, background, evaluation\\n# Roles: predecessor, competitor, baseline, evaluation, background\\n\\npapers:\\n\\n  # ============================================================\\n  # Direction 1: Self-Verification / Self-Correction in LLM Agents\\n  # ============================================================\\n\\n  - id: kamoi2024self-correction-survey\\n    title: \\\"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs\\\"\\n    authors: \\\"Kamoi et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2024\\n    arxiv_id: \\\"2406.01297\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Foundational survey establishing that pure intrinsic self-correction is unreliable.\\n      Validates B-IAVR's use of grounded verification (environment re-observation) over prompted self-feedback.\\n\\n  - id: tie2025correctbench\\n    title: \\\"Can LLMs Correct Themselves? A Benchmark of Self-Correction in LLMs\\\"\\n    authors: \\\"Tie et al.\\\"\\n    venue: \\\"NeurIPS 2025 Datasets & Benchmarks\\\"\\n    year: 2025\\n    arxiv_id: \\\"2510.16062\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Benchmark showing self-correction has diminishing returns when applied uniformly.\\n      Supports B-IAVR's selective verification design over blanket correction.\\n\\n  - id: self-verification-dilemma-2026\\n    title: \\\"Self-Verification Dilemma: Experience-Driven Suppression of Overused Checking in LLM Reasoning\\\"\\n    authors: \\\"Long et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2602.03485\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Empirically validates that >90% of self-verification is confirmatory, ~2% corrective.\\n      Directly supports B-IAVR's core thesis that verification should be selective.\\n      Their experience-pool approach is complementary to B-IAVR's action-change signal.\\n\\n  - id: zhang2025incentivize-self-verify\\n    title: \\\"Incentivizing LLMs to Self-Verify Their Answers\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2506.01369\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Unifies answer generation and verification via single RL training process.\\n      Parallel to B-IAVR: they train verification into generation; B-IAVR trains when to trigger separate verification.\\n\\n  - id: mar2025\\n    title: \\\"MAR: Multi-Agent Reflexion Improves Reasoning Abilities in LLMs\\\"\\n    authors: \\\"Ozer et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2512.20845\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Multi-agent self-correction with diverse critic personas.\\n      Complementary: MAR improves correction quality; B-IAVR decides when to trigger correction.\\n\\n  - id: ssr2025\\n    title: \\\"SSR: Socratic Self-Refine for Large Language Model Reasoning\\\"\\n    authors: \\\"Shi et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2511.10621\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Structured Socratic questioning for self-refinement.\\n      Complementary: improves correction step quality; B-IAVR focuses on when to invoke correction.\\n\\n  - id: verifiagent2025\\n    title: \\\"VerifiAgent: a Unified Verification Agent in Language Model Reasoning\\\"\\n    authors: \\\"Han et al.\\\"\\n    venue: \\\"EMNLP 2025 Findings\\\"\\n    year: 2025\\n    arxiv_id: \\\"2504.00406\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Unified verification agent with meta-verification + tool-based adaptive verification.\\n      Focuses on how to verify (tool selection); B-IAVR focuses on when to verify (policy learning).\\n      Complementary: VerifiAgent's verification quality could enhance B-IAVR's verification step.\\n\\n  # ============================================================\\n  # Direction 2: Agent RL Training\\n  # ============================================================\\n\\n  - id: feng2025gigpo\\n    title: \\\"GiGPO: Group-in-Group Policy Optimization for LLM Agent Training\\\"\\n    authors: \\\"Feng et al.\\\"\\n    venue: \\\"NeurIPS 2025\\\"\\n    year: 2025\\n    arxiv_id: \\\"2505.10978\\\"\\n    category: method-component\\n    role: predecessor\\n    relevance_note: >\\n      Core training algorithm for B-IAVR. Nested group structure provides step-level credit\\n      assignment without learned critic. >12% over GRPO on ALFWorld, >9% on WebShop.\\n\\n  - id: selfguide2026\\n    title: \\\"Co-Evolution of Policy and Internal Reward for Language Agents (Self-Guide)\\\"\\n    authors: \\\"Wang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2604.03098\\\"\\n    category: method-component\\n    role: predecessor\\n    relevance_note: >\\n      Direct predecessor. B-IAVR extends Self-Guide's co-evolving internal reward.\\n      The self-guidance signal is the foundation for action-change detection triggering verification.\\n      8% improvement over env-reward-only on ALFWorld with Qwen3-1.7B/4B.\\n\\n  - id: spear2025\\n    title: \\\"Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning\\\"\\n    authors: \\\"Qin et al.\\\"\\n    venue: \\\"ICLR 2026\\\"\\n    year: 2025\\n    arxiv_id: \\\"2509.22601\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      Curriculum-based self-imitation for sparse-reward agent tasks.\\n      Up to +16.1% on ALFWorld over GRPO. Self-imitation curriculum could augment B-IAVR training.\\n\\n  - id: wei2025webagent-r1\\n    title: \\\"WebAgent-R1: Training Web Agents via End-to-End Multi-Turn RL\\\"\\n    authors: \\\"Wei et al.\\\"\\n    venue: \\\"EMNLP 2025\\\"\\n    year: 2025\\n    arxiv_id: \\\"2505.16421\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Extends GRPO to multi-turn (M-GRPO) with dynamic context compression.\\n      Qwen-2.5-3B: 6.1% to 33.9% on WebArena-Lite. M-GRPO multi-turn extension relevant to B-IAVR.\\n\\n  - id: dapo2025\\n    title: \\\"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\\\"\\n    authors: \\\"Yu et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2503.14476\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      RL training stabilization techniques (Clip-Higher, Dynamic Sampling).\\n      Applicable to B-IAVR's RL training to prevent entropy collapse.\\n\\n  - id: digiRL2024\\n    title: \\\"DigiRL: Training In-The-Wild Device-Control Agents with Autonomous RL\\\"\\n    authors: \\\"Bai et al.\\\"\\n    venue: \\\"NeurIPS 2024\\\"\\n    year: 2024\\n    arxiv_id: \\\"2406.11896\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Online RL for device control agents. Demonstrates online RL viability for interactive agents.\\n      49.5% absolute improvement over SFT. Parallel approach to B-IAVR in text-based setting.\\n\\n  - id: li2025sorl\\n    title: \\\"SORL: Stabilizing Off-Policy RL for Long-Horizon Agent Training\\\"\\n    authors: \\\"Li et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2511.20718\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      Turn-level importance sampling + clipping-triggered normalization for stable multi-turn agent RL.\\n      Directly applicable to B-IAVR's multi-turn ALFWorld training stability.\\n\\n  - id: agentic-rl-survey-2025\\n    title: \\\"The Landscape of Agentic Reinforcement Learning for LLMs: A Survey\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    venue: \\\"TMLR 2026\\\"\\n    year: 2025\\n    arxiv_id: \\\"2509.02547\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Comprehensive survey formalizing agentic RL. Contextualizes B-IAVR as training agents\\n      to make meta-decisions (when to verify) via RL within the POMDP framework.\\n\\n  - id: skillmaster2026\\n    title: \\\"SkillMaster: Toward Autonomous Skill Mastery in LLM Agents\\\"\\n    authors: \\\"Yang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2605.08693\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      DualAdv-GRPO: separately estimates advantages for task-solving and skill-editing decisions.\\n      +8.8% on ALFWorld, +9.3% on WebShop. DualAdv structure could inform B-IAVR's\\n      separation of action and verification advantages.\\n\\n  - id: t2po2026\\n    title: \\\"T2PO: Uncertainty-Guided Exploration Control for Stable Multi-Turn Agentic RL\\\"\\n    authors: \\\"Wang et al.\\\"\\n    venue: \\\"ICML 2026 Spotlight\\\"\\n    year: 2026\\n    arxiv_id: \\\"2605.02178\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      Token- and turn-level uncertainty monitoring for stable multi-turn agent RL.\\n      Triggers thinking intervention when marginal uncertainty change drops below threshold.\\n      Evaluated on ALFWorld and WebShop. Conceptually related: uncertainty-based trigger vs\\n      B-IAVR's action-change trigger, but T2PO targets training stability, not deployment verification.\\n\\n  - id: gvpo2026\\n    title: \\\"GVPO: Group Verification-based Policy Optimization for Interactive Coding Agents\\\"\\n    authors: \\\"Dai et al.\\\"\\n    venue: \\\"ICLR 2026\\\"\\n    year: 2026\\n    arxiv_id: null  # no arXiv preprint; OpenReview ID: RY47Tq0VsV\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      Advantage shaping with outcome-verifiable + process-verifiable signals.\\n      +12.7% over o1 on AppWorld. Integrates intermediate execution feedback as step-level\\n      verification signals. Different focus: uses verification for credit assignment during\\n      training; B-IAVR learns when to invoke verification at deployment.\\n\\n  - id: agentv-rl2026\\n    title: \\\"AgentV-RL: Scaling Reward Modeling with Agentic Verifier\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2604.16004\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      Bidirectional forward/backward agentic verifier for reward modeling in RL.\\n      4B model surpasses SOTA ORMs by 25.2%. Addresses verification quality in reward modeling;\\n      B-IAVR addresses verification timing in agent deployment. Complementary.\\n\\n  - id: pa-moe2026\\n    title: \\\"PA-MoE: Phase-Aware Mixture of Experts for Agentic Reinforcement Learning\\\"\\n    authors: \\\"Li et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2602.17038\\\"\\n    category: evaluation\\n    role: baseline\\n    relevance_note: >\\n      [NEW-0516] Lightweight phase router learns latent phase boundaries from RL objective.\\n      PA-MoE+GiGPO with Qwen2.5-1.5B achieves 93.8% on ALFWorld (+7.7 over GiGPO 86.1%).\\n      1.5B outperforms vanilla 7B GiGPO (90.2%). New small-model SOTA on ALFWorld.\\n      Orthogonal architecture innovation; important baseline to cite.\\n\\n  - id: sdar2026\\n    title: \\\"SDAR: Self-Distilled Agentic Reinforcement Learning\\\"\\n    authors: \\\"Lu et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2605.15155\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] On-policy self-distillation as gated auxiliary objective during RL training.\\n      Token-level gate decides supervision intensity. +9.4% over GRPO on ALFWorld.\\n      Complementary: SDAR improves RL training; B-IAVR learns verification policy.\\n\\n  - id: hcapo2026\\n    title: \\\"HCAPO: Hindsight Credit Assignment for Long-Horizon LLM Agents\\\"\\n    authors: \\\"Tan et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2603.08754\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] LLM-as-critic refines step-level Q-values via hindsight reasoning +\\n      multi-scale advantage for critical decision states.\\n      +13.8% on ALFWorld, +7.7% on WebShop over GRPO (Qwen2.5-7B).\\n      Could improve B-IAVR's reward signal for verification decision steps.\\n\\n  - id: act2026\\n    title: \\\"ACT: Agentic Critical Training\\\"\\n    authors: \\\"Liu et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2603.08706\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] Trains agents to judge action quality via critical comparison reward.\\n      +5.07 over IL, +4.62 over RL. Different axis: ACT improves reflection quality;\\n      B-IAVR decides when to reflect.\\n\\n  - id: rwml2026\\n    title: \\\"RWML: Reinforcement World Model Learning for LLM-based Agents\\\"\\n    authors: \\\"Yu et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2602.05842\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] Self-supervised world model via sim-to-real gap rewards in embedding space.\\n      +6.9 on ALFWorld over task-success-only RL. Matches expert-data training.\\n      Orthogonal: improves internal world model; B-IAVR adds selective verification.\\n\\n  - id: skill0-2026\\n    title: \\\"SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization\\\"\\n    authors: \\\"Lu et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2604.02268\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] Training-time curriculum progressively withdraws skill context until zero-shot.\\n      +9.7% on ALFWorld over GRPO, <0.5k tokens per step.\\n      Complementary: SKILL0 internalizes skills; B-IAVR adds selective verification.\\n\\n  - id: fission-grpo2026\\n    title: \\\"Fission-GRPO: Robust Tool Use via Learning to Recover from Execution Errors\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2601.15625\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] Fissions failed trajectories into recovery training instances.\\n      +4% overall accuracy on BFCL v4 Multi-Turn over GRPO.\\n      Related: error recovery after failure vs B-IAVR's proactive verification.\\n\\n  - id: selfbudgeter2026\\n    title: \\\"SelfBudgeter: Adaptive Token Allocation for Efficient LLM Reasoning\\\"\\n    authors: \\\"Li et al.\\\"\\n    venue: \\\"ICLR 2026 (under review)\\\"\\n    year: 2025\\n    arxiv_id: \\\"2505.11274\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] Self-estimated token budgets + budget-guided GRPO. 61% token reduction.\\n      Parallel concept: SelfBudgeter allocates computation budget;\\n      B-IAVR makes binary verify/not-verify decision. Both use RL for adaptive compute.\\n\\n  - id: cove2026\\n    title: \\\"CoVe: Training Interactive Tool-Use Agents via Constraint-Guided Verification\\\"\\n    authors: \\\"Chen et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2603.01940\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] Task constraints guide trajectory generation and serve as deterministic verifiers.\\n      Different: CoVe uses verification for data synthesis; B-IAVR learns when to verify at inference.\\n\\n  # ============================================================\\n  # Direction 3: Selective Verification / Adaptive Computation\\n  # ============================================================\\n\\n  - id: wan2025derailer-rerailer\\n    title: \\\"Derailer-Rerailer: Adaptive Verification for Efficient and Reliable LM Reasoning\\\"\\n    authors: \\\"Wan et al.\\\"\\n    venue: \\\"ACL 2025 Findings\\\"\\n    year: 2025\\n    arxiv_id: \\\"2408.13940\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      Most directly related competitor. Both do selective verification with binary trigger.\\n      Key difference: operates on reasoning chains (single-turn); B-IAVR on agent trajectories (multi-turn).\\n      Uses heuristic instability signal; B-IAVR uses RL-trained action-change signal.\\n      8-11% accuracy gain, 2-3x efficiency over uniform verification.\\n\\n  - id: sherlock2025\\n    title: \\\"Sherlock: Reliable and Efficient Agentic Workflow Execution\\\"\\n    authors: \\\"Microsoft\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2511.00330\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      Selective verification for agentic workflows via offline counterfactual analysis + speculative execution.\\n      Different scope: workflow DAG level (offline); B-IAVR is step-level (online RL).\\n      18.3% accuracy gain, 26% cost reduction, 48.7% latency reduction.\\n\\n  - id: singhi2025when-to-verify\\n    title: \\\"When To Solve, When To Verify: Compute-Optimal Verification for LLM Reasoning\\\"\\n    authors: \\\"Singhi et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2504.01005\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Derives inference scaling laws for solve-vs-verify tradeoff.\\n      Finding that over-verification is suboptimal directly supports B-IAVR's selective approach.\\n      B-IAVR learns this allocation via RL rather than analytically.\\n\\n  - id: yang2026ares\\n    title: \\\"ARES: Adaptive Reasoning Effort Selection for Efficient LLM Agents\\\"\\n    authors: \\\"Yang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2603.07915\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      Closest competitor in agent domain. Both train learned per-step compute allocation.\\n      ARES uses SFT-initialized router further refined via GRPO with outcome + token efficiency reward;\\n      B-IAVR trains binary verify/not-verify via RL with action-change signal.\\n      Key differences: (1) reward signal — ARES optimizes token efficiency, B-IAVR uses action-change\\n      as verification trigger; (2) data requirement — ARES needs difficulty-annotated training data\\n      to bootstrap the router, B-IAVR learns from environment interaction alone.\\n      Reduces reasoning tokens by up to 52.7%.\\n\\n  - id: tu2025autothink\\n    title: \\\"Learning When to Think: Shaping Adaptive Reasoning in R1-Style Models via Multi-Stage RL\\\"\\n    authors: \\\"Tu et al.\\\"\\n    venue: \\\"NeurIPS 2025\\\"\\n    year: 2025\\n    arxiv_id: \\\"2505.10832\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      Analogous idea in reasoning domain: RL-trained adaptive computation trigger.\\n      Operates on single-turn reasoning; B-IAVR on multi-turn agent trajectories.\\n      +6.4% accuracy, -52% tokens on DeepSeek-R1-Distill-Qwen-1.5B.\\n\\n  - id: du2025thinkless\\n    title: \\\"Thinkless: LLM Learns When to Think\\\"\\n    authors: \\\"Fang et al.\\\"\\n    venue: \\\"NeurIPS 2025\\\"\\n    year: 2025\\n    arxiv_id: \\\"2505.13379\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      RL-trained control token to decide when to invoke extended thinking.\\n      Methodologically closest to B-IAVR in reasoning domain; B-IAVR applies to interactive agent trajectories.\\n\\n  - id: wang2025efficient-agents\\n    title: \\\"Efficient Agents: Building Effective Agents While Reducing Cost\\\"\\n    authors: \\\"Wang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2508.02694\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      First systematic study of agent efficiency-effectiveness tradeoff.\\n      Framework-level cost reduction; B-IAVR addresses cost at verification-policy level.\\n      Retains 96.7% performance with 28.4% cost-of-pass improvement.\\n\\n  - id: venktesh2025trust-but-verify\\n    title: \\\"Trust but Verify! A Survey on Verification Design for Test-time Scaling\\\"\\n    authors: \\\"Venktesh et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2508.16665\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Survey of verification approaches for test-time compute scaling.\\n      Identifies verification timing as key open problem. B-IAVR provides concrete solution for agent setting.\\n\\n  - id: agent-omit2026\\n    title: \\\"Agent-Omit: Training Efficient LLM Agents for Adaptive Thought and Observation Omission via Agentic RL\\\"\\n    authors: \\\"Ning et al.\\\"\\n    venue: \\\"ICML 2026\\\"\\n    year: 2026\\n    arxiv_id: \\\"2602.04284\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      RL-trained policy for adaptive omission of redundant thoughts and observations.\\n      Agent-Omit-8B matches frontier agents with best efficiency tradeoff on 5 benchmarks.\\n      Both use RL to learn cost-efficient agent behavior. Key difference: Agent-Omit subtracts\\n      (omits unnecessary context); B-IAVR selectively adds (verification steps).\\n      Opposite but complementary approaches to cost-efficiency. Potentially combinable.\\n\\n  - id: ava2026\\n    title: \\\"Anytime Verified Agents: Adaptive Compute Allocation for Reliable LLM Reasoning under Budget Constraints\\\"\\n    authors: \\\"Patel\\\"\\n    venue: \\\"TMLR 2026\\\"\\n    year: 2026\\n    arxiv_id: null  # no arXiv preprint; OpenReview ID: JMDCMf7mlF\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      Dynamic compute allocation across search, sampling, and verification under budget.\\n      Uses calibrated uncertainty + value-of-information for selective verification cascades.\\n      Evaluated on GSM8K/MATH/HotpotQA/HumanEval (reasoning), not interactive agents.\\n      Key difference: analytical/heuristic allocation vs B-IAVR's RL-learned policy;\\n      single-turn reasoning vs multi-turn agent trajectories.\\n\\n  - id: cast2026\\n    title: \\\"CAST: Case-Based Calibration of Adaptive Reasoning and Execution for LLM Tool Use\\\"\\n    authors: \\\"Pang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2605.15041\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Historical execution cases calibrate reasoning depth for tool use.\\n      Reduces reasoning length 26% with +5.85% accuracy on BFCLv2/ToolBench.\\n      Related: adaptive reasoning depth; different: case-based calibration vs RL-learned policy.\\n\\n  - id: marginal-token-allocators2026\\n    title: \\\"Agentic AI Systems Should Be Designed as Marginal Token Allocators\\\"\\n    authors: \\\"Zhu\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2605.01214\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Position paper framing agent cost-efficiency as marginal token allocation economics.\\n      Identifies under-verification as systematic failure mode. Supports B-IAVR's framing\\n      that verification decisions should reflect marginal cost-benefit analysis.\\n\\n  - id: argos2025\\n    title: \\\"Argos: Multimodal RL with Adaptive Verifier for AI Agents\\\"\\n    authors: \\\"Tan et al.\\\"\\n    venue: \\\"arXiv (revised April 2026)\\\"\\n    year: 2025\\n    arxiv_id: \\\"2512.03438\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Agentic verifier that adaptively selects scoring functions for multimodal RL training.\\n      Different domain (multimodal/robotics). The adaptive verifier selection concept is\\n      complementary: Argos adapts how to verify; B-IAVR adapts when to verify.\\n\\n  # ============================================================\\n  # Direction 4: ALFWorld / Interactive Environment Benchmarks\\n  # ============================================================\\n\\n  - id: kim2025reflact\\n    title: \\\"ReflAct: World-Grounded Decision Making in LLM Agents via Goal-State Reflection\\\"\\n    authors: \\\"Kim et al.\\\"\\n    venue: \\\"EMNLP 2025\\\"\\n    year: 2025\\n    arxiv_id: \\\"2505.15182\\\"\\n    category: evaluation\\n    role: baseline\\n    relevance_note: >\\n      Prompting SOTA on ALFWorld at 93.3%. Replaces ReAct's next-action thinking with state-goal reflection.\\n      B-IAVR addresses different axis (cost-efficiency) since ALFWorld accuracy is near saturation.\\n\\n  - id: choudhury2025agentprm\\n    title: \\\"Process Reward Models for LLM Agents: Practical Framework and Directions\\\"\\n    authors: \\\"Choudhury\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2502.10325\\\"\\n    category: evaluation\\n    role: baseline\\n    relevance_note: >\\n      Monte Carlo rollout-based process reward for agent training. 3B models achieve 91% on ALFWorld.\\n      Validates RL training approach; AgentPRM could serve as reward model for B-IAVR.\\n\\n  - id: xi2025agentprm\\n    title: \\\"AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress\\\"\\n    authors: \\\"Xi et al.\\\"\\n    venue: \\\"ACM Web Conference 2026\\\"\\n    year: 2025\\n    arxiv_id: \\\"2511.08325\\\"\\n    category: evaluation\\n    role: baseline\\n    relevance_note: >\\n      Independent work from Choudhury et al., using TD-based estimation with GAE for scalable\\n      PRM data labeling. 8x more compute-efficient than baselines with robust test-time scaling.\\n      Different approach: Choudhury uses MC rollouts; Xi uses TD+GAE for step-wise promise and progress.\\n\\n  - id: xiang2024retrospex\\n    title: \\\"Retrospex: Language Agent Meets Offline RL Critic\\\"\\n    authors: \\\"Xiang et al.\\\"\\n    venue: \\\"EMNLP 2024\\\"\\n    year: 2024\\n    arxiv_id: \\\"2505.11807\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Offline RL Critic augments LLM agent action selection via dynamic rescoring.\\n      Similar architecture could inform B-IAVR's verification value estimation.\\n\\n  - id: cfgm2025\\n    title: \\\"CFGM: Coarse-to-Fine Grounded Memory for LLM Agent Planning\\\"\\n    authors: \\\"Yang et al.\\\"\\n    venue: \\\"EMNLP 2025\\\"\\n    year: 2025\\n    arxiv_id: \\\"2508.15305\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Memory-augmented agent planning with episodic grounding.\\n      ALFWorld +10.40%, WebShop +20%. Complementary to B-IAVR's verification approach.\\n\\n  - id: respact2024\\n    title: \\\"ReSpAct: Harmonizing Reasoning, Speaking, and Acting\\\"\\n    authors: \\\"Dongre et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2024\\n    arxiv_id: \\\"2411.00927\\\"\\n    category: evaluation\\n    role: baseline\\n    relevance_note: >\\n      Integrates dialogue/reasoning/acting. +6% over ReAct on ALFWorld.\\n      Reduces invalid actions from 13% to 3%; B-IAVR's verification achieves error prevention differently.\\n\\n  # ============================================================\\n  # Direction 5: Multi-Turn Credit Assignment (Direct Competitors)\\n  # ============================================================\\n\\n  - id: turn-ppo2025\\n    title: \\\"Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs\\\"\\n    authors: \\\"Li et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2512.17008\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      [NEW-0517] Most direct competitor. Identifies \\\"uniform advantage\\\" problem in\\n      step-independent GRPO (subset of our \\\"sign misattribution\\\"). Proposes turn-level\\n      MDP + learned value function. Our differences: (1) more precise formalization\\n      (sign misattribution + gamma decay quantification), (2) contrarian solution\\n      (episode-level coarser credit vs their finer turn-level credit).\\n\\n  - id: gagpo2026\\n    title: \\\"GAGPO: Generalized Advantage Grouped Policy Optimization\\\"\\n    authors: \\\"Zhu et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2605.13217\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      [NEW-0517] Critic-free step-aligned credit via non-parametric grouped value proxy +\\n      TD/GAE-style temporal advantages. ALFWorld 93.5% (1.5B), 95.6% (7B).\\n      Pursues finer-grained credit to improve performance; our work diagnoses why\\n      step-independent fails (sign misattribution) and shows coarser episode-level suffices.\\n      Different contribution axis: performance optimization vs mechanism diagnosis.\\n\\n  - id: mt-grpo2025\\n    title: \\\"Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Reward Design\\\"\\n    authors: \\\"Wei et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2505.11821\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      [NEW-0517] Proposes MT-GRPO with turn-level reward design for multi-turn RL.\\n      Evaluated on QA search tasks (NQ, TriviaQA, HotpotQA), not ALFWorld.\\n      Qwen2.5-7B. Same direction as Turn-PPO (finer turn-level credit);\\n      our contrarian shows coarser episode-level eliminates sign misattribution.\\n\\n  - id: istar2025\\n    title: \\\"Agentic Reinforcement Learning with Implicit Step Rewards\\\"\\n    authors: \\\"Liu et al.\\\"\\n    venue: \\\"ICLR 2026\\\"\\n    year: 2025\\n    arxiv_id: \\\"2509.19199\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      [NEW-0517] Implicit PRM + dual advantage (step + episode level) for agentic RL.\\n      WebShop 86.5%, VisualSokoban 91.7%. ICLR 2026 published.\\n      Learns step-level credit via implicit rewards without explicit labels;\\n      our work shows episode-level alone suffices when sign misattribution is the bottleneck.\\n      Validates that step-level credit helps, but doesn't diagnose when it hurts.\\n\\n  - id: archer2024\\n    title: \\\"ArCHer: Training Language Model Agents via Hierarchical Multi-Turn RL\\\"\\n    authors: \\\"Zhou, Zanette, Pan, Levine, Kumar\\\"\\n    venue: \\\"ICML 2024\\\"\\n    year: 2024\\n    arxiv_id: \\\"2402.19446\\\"\\n    category: method-component\\n    role: predecessor\\n    relevance_note: >\\n      [NEW-0517] Foundational hierarchical multi-turn RL framework (ICML 2024).\\n      High-level off-policy value RL (utterance-level) + low-level token policy.\\n      ~100x sample efficiency. Establishes that multi-turn RL needs hierarchical structure;\\n      our work specifically diagnoses why flat step-independent approaches fail.\\n\\n  - id: ca-survey2026\\n    title: \\\"From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models\\\"\\n    authors: \\\"Zhang\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2604.09459\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      [NEW-0517] Comprehensive survey of 47 CA methods (2024-2026). Two-dimensional\\n      taxonomy: granularity (token/segment/step/turn/multi-agent) x methodology\\n      (MC/TD/model-based/game-theoretic/information-theoretic). Contextualizes our\\n      sign misattribution diagnosis within the broader CA landscape.\\n\\n  - id: hiper2026\\n    title: \\\"HiPER: Hierarchical Reinforcement Learning with Explicit Credit Assignment for Large Language Model Agents\\\"\\n    authors: \\\"Peng et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2602.16165\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      [NEW-0517] Hierarchical Plan-Execute RL. ALFWorld 97.4% (7B), 95.3% (1.5B).\\n      GRPO baseline: 71.1% (1.5B), 85.4% (7B). 2.8x training efficiency gain.\\n      Pursues SOTA performance via hierarchical plan-execute architecture;\\n      our work does mechanism diagnosis of why step-independent GRPO fails.\\n      Different contribution dimension: not comparable on performance axis.\\n\", \"total_chars\": 29932, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
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
The registry output was too large and was saved to a file. Let me use jq to extract ScienceWorld-related experiments from it. Let me also read the experiment plan.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "f25a2f45-8b83-46fb-b453-51328b2452b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H5zw5a5KSnE5RVniXHjM13",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13785,
      "cache_read_input_tokens": 25233,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13785
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

_source line 17_

Registry 输出过大，用 jq 提取 ScienceWorld 相关实验。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "836455b1-ed59-4c74-8e44-d07db230702a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H5zw5a5KSnE5RVniXHjM13",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13785,
      "cache_read_input_tokens": 25233,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13785
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

_source line 18_

<details open><summary>🔧 Tool call — Bash · `toolu_0179tYanS3i5AxFzZJs6Fqma`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-1-projects-cost-verify-agent-rl/54b94781-146b-4013-9381-11e3737077cb/tool-results/mcp-agent-ml-research-read_registry-1779420967332.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result if isinstance(result, list) else result.get('experiments', result.get('data', []))\nif isinstance(exps, dict):\n    exps = list(exps.values())\n# Filter for ScienceWorld related\nsw_exps = []\nfor exp in exps:\n    exp_id = exp.get('exp_id', '') or ''\n    hypothesis = exp.get('hypothesis', '') or ''\n    spec = json.dumps(exp.get('spec', {})) if exp.get('spec') else ''\n    conclusion = exp.get('conclusion', '') or ''\n    tags = json.dumps(exp.get('tags', [])) if exp.get('tags') else ''\n    all_text = (exp_id + hypothesis + spec + conclusion + tags).lower()\n    if 'scienceworld' in all_text or 'science_world' in all_text or 'science-world' in all_text or 'sw_' in exp_id.lower() or '_sw' in exp_id.lower():\n        sw_exps.append(exp)\nprint(f'Found {len(sw_exps)} ScienceWorld experiments out of {len(exps)} total')\nprint(json.dumps(sw_exps, indent=2, ensure_ascii=False))\n\" 2>&1 | head -500",
  "description": "Extract ScienceWorld experiments from registry JSON"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "f7b032cf-b91f-4c25-88e0-3584718aed24",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H5zw5a5KSnE5RVniXHjM13",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13785,
      "cache_read_input_tokens": 25233,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13785
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

_source line 19 · 2026-05-22T03:36:22.163Z_

<details><summary>↩ Tool result · `toolu_0179tYanS3i5AxFzZJs6Fqma`</summary>

```text
Traceback (most recent call last):
  File "&lt;string>", line 11, in &lt;module>
    exp_id = exp.get('exp_id', '') or ''
             ^^^^^^^
AttributeError: 'int' object has no attribute 'get'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "4c8a4ce3-477b-4ab9-b5e4-9c8b50734b03",
  "tool_use_result": {
    "stdout": "Traceback (most recent call last):\n  File \"&lt;string>\", line 11, in &lt;module>\n    exp_id = exp.get('exp_id', '') or ''\n             ^^^^^^^\nAttributeError: 'int' object has no attribute 'get'",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0199BbSoffAhkbzuHXeBk9Ea`</summary>

```json
{
  "project": "cost-verify-agent-rl",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "76138802-66d9-4bfd-b1ca-8f0afd1d48ff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H5zw5a5KSnE5RVniXHjM13",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13785,
      "cache_read_input_tokens": 25233,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13785
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

_source line 21 · 2026-05-22T03:36:22.568Z_

<details><summary>↩ Tool result · `toolu_0199BbSoffAhkbzuHXeBk9Ea`</summary>

```text
Error: result (96,899 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-1-projects-cost-verify-agent-rl/54b94781-146b-4013-9381-11e3737077cb/tool-results/mcp-agent-ml-research-read_project_file-1779420982565.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-1-projects-cost-verify-agent-rl/54b94781-146b-4013-9381-11e3737077cb/tool-results/mcp-agent-ml-research-read_project_file-1779420982565.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-1-projects-cost-verify-agent-rl/54b94781-146b-4013-9381-11e3737077cb/tool-results/mcp-agent-ml-research-read_project_file-1779420982565.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "0a5eb309-7eaf-459e-b866-d5e3930a973f",
  "tool_use_result": {
    "content": "Error: result (96,899 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-1-projects-cost-verify-agent-rl/54b94781-146b-4013-9381-11e3737077cb/tool-results/mcp-agent-ml-research-read_project_file-1779420982565.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-1-projects-cost-verify-agent-rl/54b94781-146b-4013-9381-11e3737077cb/tool-results/mcp-agent-ml-research-read_project_file-1779420982565.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-1-projects-cost-verify-agent-rl/54b94781-146b-4013-9381-11e3737077cb/tool-results/mcp-agent-ml-research-read_project_file-1779420982565.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/decisions.yaml\", \"content\": \"_next_id: 121\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 17:33 UTC\\n  summary: MVP 选择 ALFWorld + Qwen3-1.7B 单环境验证 B-IAVR 核心假设\\n  rationale: ALFWorld 离散动作空间使 action_changed 信号最清晰，semantic canonicalization 简单（verb,object,receptacle三元组）。Qwen3-1.7B\\n    有充分 headroom（+8.6pp on ALFWorld）。MVP 只需验证\\\"agent 能学会选择性验证\\\"这一核心假设，不需要跨环境/跨模型。2×GPU\\n    足够 1.7B+LoRA 训练。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 18:39 UTC\\n  summary: Phase A 使用全量微调（非 LoRA），匹配 Self-Guide 原始论文设置\\n  rationale: Self-Guide 原文用全量微调 GRPO。1.7B 模型在 94GB VRAM 下全量微调显存仅 38.5GB，完全可行。匹配 baseline\\n    设置确保公平对比。IDEA_BRIEF 提及 LoRA 是基于 H100 80GB 的资源估算，RTX PRO 6000 94GB 无需节省。\\n  related_experiments:\\n  - exp_id: exp_001\\n    role: Phase A baseline\\n    result: running\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 23:55 UTC\\n  summary: Kill exp003，Phase A bootstrap 失败确认，等待 invalid action 根因诊断后决定修复方向\\n  rationale: 'exp003 step 1: invalid_action=95.3%, pg_loss≈0, 每步 1.6h（100步=160h）。GRPO\\n    从 0.125% valid action 中无法获得有效学习信号。Qwen3 无独立 Instruct 版，Plan B 失效。需先诊断 invalid\\n    action 根因（格式冲突 / token 问题 / prompt 不兼容）再选修复路径。'\\n  related_experiments:\\n  - exp_id: exp003\\n    role: primary\\n    result: failed - bootstrap failure, 95% invalid actions, pg_loss≈0\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 00:10 UTC\\n  summary: 采用方案 A（修改解析器适配 Qwen3 格式）+ prompt 增强 + 速度优化，解决 bootstrap 失败\\n  rationale: 根因确认：Qwen3-1.7B 原生输出 &lt;think>...&lt;/think> 后直接跟自然语言，不生成 &lt;answer> 标签。RAGEN\\n    解析器正则要求 &lt;answer> 导致 95% invalid。方案 A 最快（1-2h 改代码）、最低风险（不换模型不加训练阶段），同时优化速度（关闭 collapse\\n    multi_turn 省 35% 步耗时 + 减 traj/step）。\\n  related_experiments:\\n  - exp_id: exp003\\n    role: diagnostic\\n    result: '32/32 samples confirm: no &lt;answer> tag in Qwen3 output'\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-14 02:56 UTC\\n  summary: exp007 borderline 但不 pivot SFT，提高 LR 到 5e-6 重跑 GRPO\\n  rationale: exp007 step 10 action_is_valid=8.35%，技术上触发预设 kill 条件（<10%），但：(1) 趋势明确上升\\n    4.01%→8.35%（+0.48pp/step），线性外推 ~step 14 即突破 10%；(2) success 从 0%→6.25%，GRPO 确实在学习；(3)\\n    manager_invalid 6.46%→1.56%，解析器修复有效；(4) 崩溃是 /tmp 磁盘满（基础设施），非算法失败；(5) SFT warmup\\n    需额外收集 expert trajectories + 训练周期，开销大。因此override kill 条件，选择提高 LR（1e-6→5e-6）重跑 GRPO\\n    30 步，save_freq=5，同时修复所有基础设施问题（RAY_TMPDIR、/tmp 清理）。新 kill 条件：step 10 action_is_valid\\n    < 15%（因 LR 提高 5x，预期收敛更快）。\\n  related_experiments:\\n  - exp_id: exp007\\n    role: evidence\\n    result: step 10 action_is_valid=8.35%, success=6.25%, 因磁盘满崩溃于 step 11, checkpoint\\n      全部丢失\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-14 03:02 UTC\\n  summary: 撤回 exp008 (LR 5e-6)，改用 SFT warmup 再接 GRPO\\n  rationale: Agent 正确指出 action_is_valid 低的根因不是 LR 不够高，而是 Qwen3-1.7B 缺乏 ALFWorld 命令语义知识——92%\\n    的动作语法正确但语义无效（不是合法 ALFWorld 命令）。提高 LR 只能加速已有信号的收敛，无法从根本解决命令词汇缺失。SFT warmup 直接教模型\\n    ALFWorld 命令格式和语义，GRPO 再优化策略，是更高效的路径。SFT 计划已就绪（artifacts/sft_warmup_plan.md），总成本\\n    ~8h（SFT 2h + GRPO 6h），可接受。\\n  related_experiments:\\n  - exp_id: exp007\\n    role: evidence\\n    result: 10 步 action_is_valid 仅 8.35%，语法正确但语义无效，指向命令知识缺失而非学习速度问题\\n  depends_on:\\n  - D005\\n- id: D007\\n  date: 2026-05-14 05:40 UTC\\n  summary: Kill exp011，改 reward function（连续score+降format penalty+group_size 16），从\\n    step 5 checkpoint 恢复\\n  rationale: Reward 分析确认：format_penalty(-0.1/turn)在零成功 group 中劫持 GRPO 梯度，模型只学格式不学任务（action_is_valid\\n    68% + success 0%）。A1 连续 score 给部分完成的轨迹提供梯度信号；A2 降 format_penalty 到 -0.01 避免淹没任务信号；B1\\n    group_size 8→16 提高正信号 group 比例（32%→53%）。从 step 5 恢复因其仍有 1.6% success 残余。\\n  related_experiments:\\n  - exp_id: exp010\\n    role: evidence\\n    result: failed - reward analysis revealed format penalty hijacking GRPO gradient\\n  - exp_id: exp011\\n    role: killed\\n    result: same reward config as exp010, will repeat collapse pattern\\n  depends_on:\\n  - D006\\n- id: D008\\n  date: 2026-05-14 05:41 UTC\\n  summary: Reviewer 确认 exp010 reward shaping 分析正确；A2(降 format_penalty)为 P0，A1(进度奖励)需先验证\\n    infos[\\\"score\\\"] 粒度\\n  rationale: Reviewer 独立验证了代码引用和根因诊断。新发现：env.py:137 未请求 score=True，AlfWorld 不同任务类型的\\n    score 粒度未知。A2（format_penalty→0 或 -0.01）风险最低——KL loss 已提供格式压力（SFT 模型 90% valid），penalty\\n    冗余且有害。exp011 从 step 10 恢复无 reward 修改=浪费算力，已在 D007 中 kill。\\n  related_experiments:\\n  - exp_id: exp010\\n    role: analysis_source\\n    result: failed\\n  - exp_id: exp011\\n    role: killed\\n    result: wasteful_resume_from_step10\\n  depends_on: []\\n- id: D009\\n  date: 2026-05-14 06:34 UTC\\n  summary: 强制 pre-flight checklist：每次实验提交前必须验证入口点、磁盘、参数兼容性、checkpoint 路径\\n  rationale: 18 个实验仅 1 成功，多数失败为可避免的工程问题（错误入口点、磁盘满、格式不兼容）。exp012 再次因用错入口点（agent_proxy\\n    vs train.py）失败。引入 pre-flight checklist 防止此类重复失败。\\n  related_experiments:\\n  - exp_id: exp012\\n    role: trigger\\n    result: failed - wrong entry point\\n  - exp_id: exp007\\n    role: prior failure\\n    result: failed - disk full\\n  - exp_id: exp003\\n    role: prior failure\\n    result: failed - format incompatibility\\n  depends_on:\\n  - D006\\n  - D008\\n- id: D010\\n  date: 2026-05-14 07:41 UTC\\n  summary: Kill exp012b（零梯度死锁），引入 dense reward shaping 设计 exp013，下调 MVP pass 标准至 success\\n    ≥ 20%\\n  rationale: 两位 Reviewer 独立确认：exp012b step 6-7 pg_loss=0, success=0%, pass@16=0%,\\n    advantages 全零。format_penalty=0 消除了组内 reward 方差，GRPO 无梯度信号。继续跑浪费 ~10.6 GPU-hours。核心问题是\\n    sparse binary reward + 弱基础模型 + GRPO 方差依赖 = 冷启动死锁。方向（SFT→GRPO）未被证伪，但需要 reward shaping\\n    打破死锁。76% MVP 标准不现实（Self-Guide 是非 RL 方法），下调至 20% 证明 GRPO 能学到有意义策略。\\n  related_experiments:\\n  - exp_id: exp012b\\n    role: trigger\\n    result: zero gradient deadlock - pg_loss=0, success=0%\\n  - exp_id: exp010\\n    role: comparison\\n    result: format_penalty=-0.1 had success=4.7% but gradient hijacking\\n  - exp_id: exp008_sft\\n    role: baseline\\n    result: SFT taught format compliance but not task strategy\\n  depends_on:\\n  - D008\\n  - D009\\n- id: D011\\n  date: 2026-05-14 07:41 UTC\\n  summary: Kill exp012b（零梯度死锁确认），引入 dense reward shaping，下调 MVP pass 标准至 success ≥\\n    20%\\n  rationale: Reviewer critical 确认：format_penalty=0 + binary reward + 0% success =\\n    零梯度死锁（pg_loss=0.0），模型完全不更新。exp010 的 format_penalty=-0.1 至少创造了 reward 方差但方向错误。根本问题是\\n    ALFWorld sparse binary reward + GRPO 在基础模型太弱时无法工作。解决方案：加 step-level dense reward\\n    shaping（子目标奖励），方向正确且创造梯度信号。76% 目标来自 Self-Guide 论文的非 RL 方法，30 步 GRPO 不可达，MVP pass\\n    下调至 success ≥ 20% + 明确上升趋势。\\n  related_experiments:\\n  - exp_id: exp012b\\n    role: trigger\\n    result: step 6-7 train success=0%, pg_loss=0.0, 零梯度\\n  - exp_id: exp010\\n    role: 对照\\n    result: format_penalty=-0.1 时 step 1 success=4.7% 但后续崩塌\\n  - exp_id: exp008_sft\\n    role: 基础\\n    result: SFT warmup 成功，action_is_valid 68-72%\\n  depends_on:\\n  - D008\\n  - D009\\n- id: D012\\n  date: 2026-05-14 12:40 UTC\\n  summary: 'exp013f negative: dense reward gaming — 下一步 success-gated bonus + 降低 bonus\\n    比例'\\n  rationale: exp013f 完成 30 步，dense reward (valid_action_bonus=0.15) 解决了 collapse（grad_norm\\n    稳定 1.7-8.15）但引发 reward gaming：action_is_valid 60%→97.5% 而 success 归零，score_max\\n    从 10+ 塌缩到 4.5。模型学会独立最大化 dense reward（29步×0.15=4.35）放弃高风险 success（10.0）。核心问题：dense\\n    reward 可被独立最大化。修复方向：(1) success-gated bonus 消除独立最大化路径 (2) 降低 bonus 到 0.01 测试弱信号是否足够\\n    (3) 前 N 步 warmup 后撤掉 bonus。优先级 exp014c > exp014a > exp014b。\\n  related_experiments:\\n  - exp_id: exp013f\\n    role: primary\\n    result: negative - reward gaming\\n  - exp_id: exp012b\\n    role: baseline\\n    result: negative - catastrophic collapse\\n  depends_on:\\n  - D011\\n- id: D013\\n  date: 2026-05-14 12:47 UTC\\n  summary: D012 修订：放弃 success-gated bonus（bootstrap 问题），改走 sparse GRPO + 训练稳定性修复\\n  rationale: Success-gated bonus 在 success≈0% 时退化为 sparse reward，无法解决冷启动。而 exp012b\\n    step 6 success=8.59% 证明 sparse GRPO 有信号，collapse（grad_norm 1.48→0.09）可能是 LR 过高\\n    / KL 过低导致的单步更新过激，不是 reward sparsity。方案 B（sparse GRPO + 极低 LR 1e-7 + KL 0.1 + gradient\\n    clipping）直接解决 collapse 且不引入新 reward hacking 风险。\\n  related_experiments:\\n  - exp_id: exp012b\\n    role: evidence\\n    result: step 6 success=8.59% proves sparse signal exists; collapse at step 7 was\\n      training instability\\n  - exp_id: exp013f\\n    role: evidence\\n    result: dense reward gaming confirms reward shaping risks\\n  depends_on:\\n  - D012\\n- id: D014\\n  date: 2026-05-14 13:44 UTC\\n  summary: Kill exp015（LR 1e-7 过保守，连续 3 步零梯度），启动 exp016 LR=5e-7 折中方案\\n  rationale: exp015 step 1-2 有梯度信号（pg_loss>0, success 3-5%），验证了 D013 的 collapse 修复。但\\n    step 3-5 连续零梯度，LR=1e-7 的参数更新量约 5e-12，模型行为无可观测变化。Kill 条件已满足。LR=1e-6（exp012b）collapse，LR=1e-7（exp015）不学习，取折中\\n    LR=5e-7 + 保留 KL=0.1 + grad_clip=1.0。从 exp015 step 5 checkpoint 恢复（保留 step 1-2\\n    的微小更新）。\\n  related_experiments:\\n  - exp_id: exp015\\n    role: primary\\n    result: kill - LR too conservative, 3 consecutive zero-gradient steps\\n  - exp_id: exp012b\\n    role: reference\\n    result: LR 1e-6 collapsed at step 7\\n  depends_on:\\n  - D013\\n- id: D015\\n  date: 2026-05-14 14:55 UTC\\n  summary: Kill exp016 — reward function 完全失效，12 步零 reward 信号，GPU 空转\\n  rationale: exp016 step 12/30，所有 step 的 raw_reward/advantages/returns 均为 0。Step 7\\n    出现 4.7% success 但 reward 仍为 0，说明 reward function 未正确将 success 映射到 reward。grad_norm\\n    ~0.85 仅来自 entropy loss，模型无 policy gradient 信号。疑似 checkpoint resume 后 reward config\\n    丢失。继续运行浪费 GPU。\\n  related_experiments:\\n  - exp_id: exp016\\n    role: subject\\n    result: killed — reward function broken\\n  depends_on:\\n  - D014\\n- id: D016\\n  date: 2026-05-14 14:57 UTC\\n  summary: Pivot to Expert SFT warmup — GRPO 在 base success ~1-2% 下无法工作，LR 搜索区间穷尽\\n  rationale: Reviewer critical 分析确认：exp016 step 7 pg_loss=0.000151 证明 reward function\\n    本身可用，但 7 步中仅 1 步有 success（14%），步骤 8-12 连续 5 步零梯度。反推 base success rate ~1-2%，GRPO\\n    在此 sparsity 下无法产生有效学习。LR 搜索已覆盖 1e-6（collapse）→ 5e-7（无效学习）→ 1e-7（零梯度），区间穷尽。Pivot\\n    到 expert SFT：用 ALFWorld HandCodedTWAgent 收集的 expert trajectories（当前 ~61-70%）做\\n    SFT warmup，将 base success 提升到 10-15% 后再上 sparse GRPO。\\n  related_experiments:\\n  - exp_id: exp016\\n    role: evidence\\n    result: 6/7 steps zero gradient, base success ~1-2%\\n  - exp_id: exp015\\n    role: evidence\\n    result: LR=1e-7 zero gradients after step 3\\n  - exp_id: exp012b\\n    role: evidence\\n    result: LR=1e-6 catastrophic collapse\\n  depends_on:\\n  - D015\\n  - D014\\n  - D013\\n- id: D017\\n  date: 2026-05-14 15:20 UTC\\n  summary: D015 误诊纠正 — reward pipeline 正常，exp016 失败原因是 base success 太稀疏（1/8 步有信号）\\n  rationale: Reviewer 逐行核实 exp016.log：Step 7 critic/score/mean=0.46875（= 3/64 × 10.0）、critic/score/max=10.0、pg_loss=0.000151、grad_norm=2.0，reward\\n    function 完全正确。Agent 报告的 raw_reward=0 来自 es_manager 的 info.get('raw_reward', 0.0)\\n    日志 artifact，ALFWorld env info 不含此 key。NaiveRewardManager 检测到 rm_scores 后 pass-through，agent_trainer.py:779\\n    不是覆写。D016 Expert SFT pivot 仍成立，理由修正为 base success ~4.7%（仅 1/8 步有 success）太稀疏。\\n  related_experiments:\\n  - exp_id: exp016\\n    role: evidence\\n    result: reward pipeline confirmed working; killed due to sparse success, not bug\\n  depends_on:\\n  - D015\\n  - D016\\n- id: D018\\n  date: 2026-05-14 16:37 UTC\\n  summary: exp017 eval 5% success（低于 10% 阈值），采用方案 B+C：修复数据格式 + 从 exp008_sft checkpoint\\n    继续微调\\n  rationale: 'exp017 SFT eval: 5% success (1/20)，format_ok 从 100% 降至 75%，action_is_valid\\n    从 90% 降至 63.8%。25% episodes parse 失败（1 步退出）。expert trajectory 格式与 RAGEN &lt;think>/&lt;answer>\\n    不完全匹配，SFT 学到任务知识但破坏了 format 合规性。方案：(1) 修复 expert data 格式对齐 RAGEN template (2)\\n    从 exp008_sft checkpoint 开始微调（已有 100% format_ok），用较低 LR 防止遗忘 format。预计 ~1.5h。方案\\n    A（直接 GRPO）信号改善极小（5% vs 4.7%），方案 D 工程量太大。'\\n  related_experiments:\\n  - exp_id: exp017_expert_sft\\n    role: evidence\\n    result: 5% success, format_ok 75%, below 10% threshold\\n  - exp_id: exp008_sft\\n    role: baseline\\n    result: 0% success but 100% format_ok, 90% action_is_valid\\n  depends_on:\\n  - D016\\n  - D017\\n- id: D019\\n  date: 2026-05-14 16:48 UTC\\n  summary: Kill exp019 — move→put 替换方向错误，admissible_commands 中是 move 不是 put\\n  rationale: Reviewer critical 确认：ALFWorld handcoded expert 代码 5 种任务类型全部用 \\\"move {}\\n    to {}\\\" 检查 admissible_commands，RAGEN env.py action_is_available 检查 action in admissible_commands。fix_expert_sft_format.py\\n    将 2157 条正确的 \\\"move\\\" 替换为 \\\"put in/on\\\"，教模型产生不在 admissible_commands 中的动作，会进一步恶化 action_is_valid。正确修复方向：保留\\n    \\\"move\\\" 原样，在 observation 中添加 admissible actions 列表后缀。\\n  related_experiments:\\n  - exp_id: exp019_expert_sft_v2\\n    role: subject\\n    result: killed — trained on incorrectly modified data (move→put)\\n  depends_on:\\n  - D018\\n- id: D020\\n  date: 2026-05-14 21:53 UTC\\n  summary: exp019b SFT eval 通过（20% success），启动 GRPO 训练\\n  rationale: exp019b 三项指标全部达标：success=20%, format_ok=100%, action_is_valid=85.3%。admissible\\n    actions augmentation 是关键因素（exp017 无→5%, exp019b 有→20%）。SFT checkpoint 已提供足够 base\\n    success rate，GRPO 应有足够非零 reward groups 产生有效梯度。从 exp019b checkpoint 启动 sparse GRPO\\n    是 MVP gate 最后一步。\\n  related_experiments:\\n  - exp_id: exp019b_expert_sft_v3\\n    role: evidence\\n    result: success=20%, format_ok=100%, action_is_valid=85.3%\\n  - exp_id: exp017_expert_sft\\n    role: baseline\\n    result: success=5%, format_ok=75% (无 admissible actions)\\n  depends_on:\\n  - D018\\n  - D019\\n- id: D021\\n  date: 2026-05-14 22:34 UTC\\n  summary: exp020 系列 0% success 根因确认：SFT 训练格式与 RAGEN 格式不匹配，走方案 B 重训\\n  rationale: 同一 checkpoint 在 eval_sft_fast 中 20% success，在 RAGEN 中 0%。根因三个：(1) system\\n    prompt 矛盾（RAGEN 说不要标签又说要标签）(2) observation 格式完全不同（RAGEN 有 Turn N/State/Reward\\n    包装，SFT 数据没有）(3) temperature 差异。RAGEN 的多轮结构是 GRPO rollout 必需的，不能去掉。正确方案是将 SFT 数据转换为\\n    RAGEN 格式重训，而非改 RAGEN 适配 SFT。\\n  related_experiments:\\n  - exp_id: exp020_grpo_from_sft\\n    role: evidence\\n    result: AssertionError, 未运行\\n  - exp_id: exp020b_grpo_from_sft\\n    role: evidence\\n    result: val_before_train success=0%, action_is_valid=16.7%\\n  - exp_id: exp020c_grpo_from_sft\\n    role: evidence\\n    result: hydra config error\\n  - exp_id: exp020d_grpo_from_sft\\n    role: evidence\\n    result: killed, 同 exp020b 配置\\n  depends_on:\\n  - D020\\n- id: D022\\n  date: 2026-05-15 01:07 UTC\\n  summary: exp020b GRPO 失败，确认 eval mismatch 是根因，恢复 D021 RAGEN 格式重训路线\\n  rationale: exp020b 30步中跑了22步，train success从18.75%降到4.69%，val success始终0%，entropy坍缩61%。核心问题不是GRPO算法，而是SFT模型在RAGEN多轮框架下表现与eval_sft_fast完全不同（0%\\n    vs 20%）。之前Reviewer修正认为\\\"0%是样本量问题\\\"是错误的——22步训练确认了系统性不一致。D021（将SFT数据转换为RAGEN格式重训）是正确方向，恢复执行。\\n  related_experiments:\\n  - exp_id: exp020b_grpo_from_sft\\n    role: evidence\\n    result: train success 18.75%→4.69%, val success=0%, entropy collapse\\n  - exp_id: exp019b_expert_sft_v3\\n    role: baseline\\n    result: eval_sft_fast 20% but RAGEN val 0%\\n  depends_on:\\n  - D020\\n  - D021\\n- id: D023\\n  date: 2026-05-15 03:16 UTC\\n  summary: exp021 RAGEN 格式 SFT 验证通过（25% success），批准 exp022 GRPO\\n  rationale: exp021 在 RAGEN val 中 success=25%, action_is_valid=87.5%，全部达标。对比 exp019b\\n    在 RAGEN val 中 0% success，证明格式对齐是根因且修复生效。25% baseline 是目前最强起点，配合加强的 KL 约束（0.1→0.5）应能避免\\n    exp020b 的 entropy 坍缩。\\n  related_experiments:\\n  - exp_id: exp021_ragen_sft_v4\\n    role: evidence\\n    result: RAGEN val success=25%, action_is_valid=87.5%\\n  - exp_id: exp019b_expert_sft_v3\\n    role: baseline\\n    result: RAGEN val success=0%\\n  - exp_id: exp020b_grpo_from_sft\\n    role: negative\\n    result: train success 18.75%→4.69%, entropy collapse\\n  depends_on:\\n  - D021\\n  - D022\\n- id: D024\\n  date: 2026-05-15 03:21 UTC\\n  summary: exp021 结论降级为 inconclusive，exp022 暂不 kill 等 step 0 val 确认\\n  rationale: exp021 两次独立 eval 严重矛盾：4-episode val_before_train 25% success vs ~16-episode\\n    eval 6.25% success。4-episode 估计方差过大不可靠，25% 结果很可能是高方差幸运值。exp022 基于该不可靠数据启动，但已在运行中——让\\n    step 0 val_before_train 给出更可靠的 baseline 数字再决定是否 kill，避免白白浪费已投入的启动时间。同时 Reviewer\\n    指出 exp022 的 val env_groups=8 override 可能未生效（config dump 显示 4），需立即验证。\\n  related_experiments:\\n  - exp_id: exp021_ragen_sft_v4\\n    role: trigger\\n    result: inconclusive — 4-ep 25% vs 16-ep 6.25%\\n  - exp_id: exp022_grpo_from_sft_v4\\n    role: at_risk\\n    result: running, awaiting step 0 val confirmation\\n  depends_on:\\n  - D023\\n- id: D025\\n  date: 2026-05-15 05:14 UTC\\n  summary: Sparse binary GRPO 路线终止。三次一致退化（exp020b/exp022/exp023c），KL 仅 0.0005 时 success\\n    已退化，算法与稀疏 reward 结构性不匹配。Pivot 到两条并行路线：(1) success-gated dense reward GRPO，(2)\\n    GiGPO cherry-pick\\n  rationale: '三次 GRPO 实验（exp020b kl=0.1, exp022 kl=0.5, exp023c kl=0.5 serial）均呈现同一模式：entropy\\n    收缩 + success 退化 + KL 极低（策略几乎未移动就已退化）。根因：sparse binary reward（0/10）下绝大多数 GRPO group\\n    全零 reward → advantage≈0 → 有效梯度来自极少数成功 episode → 不足以引导策略改进。kl_loss_coef 从 0.1 到\\n    0.5 仅减缓退化速度未改变方向。这是算法-任务结构性不匹配，非超参问题。\\n\\n\\n    两条 pivot 路线：\\n\\n    (1) Success-gated dense reward：从 exp021 checkpoint（25% success）出发，给 valid_action\\n    加 bonus 但仅在 episode 成功时给。exp013f 失败原因是 unconditional bonus → reward gaming；success-gating\\n    消除独立最大化路径。代码改动小，可当天启动。\\n\\n    (2) GiGPO cherry-pick：step-level advantage estimation 提供更密集的信号，解决 credit assignment。已有迁移方案（3-5天），作为更彻底的解决方案。'\\n  related_experiments:\\n  - exp_id: exp020b_grpo_from_sft\\n    role: evidence\\n    result: 'failed: entropy collapse 61%, success→0%'\\n  - exp_id: exp022_grpo_from_sft_v4\\n    role: evidence\\n    result: 'killed: step 0 action_is_valid 48.75%'\\n  - exp_id: exp023c_grpo_serial\\n    role: evidence\\n    result: 'failed: 8 steps success 29.7%→23.4%, disk full crash'\\n  - exp_id: exp013f\\n    role: lesson\\n    result: unconditional dense reward → gaming\\n  depends_on:\\n  - D022\\n  - D023\\n  - D024\\n- id: D026\\n  date: 2026-05-15 05:15 UTC\\n  summary: GRPO in RAGEN 确认失败（3/3），pivot 到 verl-agent GiGPO cherry-pick（Plan C）\\n  rationale: 三次 GRPO 实验（exp020b/exp022/exp023c）一致表现为 entropy 坍缩 + success 退化。但 Self-Guide\\n    论文证明 GRPO 在 ALFWorld 上可以达到 72.7%（verl-agent 框架），说明问题不是 GRPO+sparse reward 本身，而是\\n    RAGEN 框架。RAGEN 的 full-history concatenation 导致 context 随步数爆炸，1.7B 模型在长 context\\n    下推理质量退化。verl-agent 的 step-independent rollout 保持 context 恒定。IDEA_BRIEF 原始设计也指定\\n    verl-agent。采用 Plan C（cherry-pick GiGPO + 核心 rollout 机制，3-5 天），避免 Plan A/B 的 2-4\\n    周全量迁移风险。\\n  related_experiments:\\n  - exp_id: exp020b_grpo_from_sft\\n    role: evidence\\n    result: 'failed: entropy collapse, success 18.75%→4.69%'\\n  - exp_id: exp022_grpo_from_sft_v4\\n    role: evidence\\n    result: 'killed: step 0 action_is_valid 48.75%'\\n  - exp_id: exp023c_grpo_serial\\n    role: evidence\\n    result: 'failed: step 9 disk full, 8 steps showed success 29.7%→23.4%, entropy\\n      shrinking'\\n  depends_on:\\n  - D022\\n  - D023\\n  - D024\\n- id: D027\\n  date: 2026-05-15 05:25 UTC\\n  summary: Kill exp024 (success-gated GRPO) — D026 已终止 RAGEN GRPO 路线，success-gated\\n    不解决 context 爆炸根因\\n  rationale: Reviewer 审查报告指出决策链冲突：D026 已明确 pivot 到 verl-agent GiGPO 并终止 RAGEN GRPO\\n    路线，但 exp024 仍是 RAGEN GRPO（仅改 reward 为 success-gated）。三点判断：(1) success-gated reward\\n    不解决 RAGEN full-history concatenation 导致的 context 爆炸——这是 exp020b/022/023c 三次退化的共因；(2)\\n    D013 之前已因 bootstrap 问题否决 success-gated（success≈0% 退化为 sparse），当前 baseline 6.25%\\n    仍然很低；(3) 3/3 RAGEN GRPO 退化 pattern 下第 4 次仅改 reward 极不可能成功。GPU 应腾出用于 verl-agent\\n    GiGPO cherry-pick 准备。\\n  related_experiments:\\n  - exp_id: exp024\\n    role: killed\\n    result: D026后应终止，step 0/30 刚启动\\n  - exp_id: exp020b_grpo_from_sft\\n    role: evidence\\n    result: RAGEN GRPO 退化 1/3\\n  - exp_id: exp022_grpo_from_sft_v4\\n    role: evidence\\n    result: RAGEN GRPO 退化 2/3\\n  - exp_id: exp023c_grpo_serial\\n    role: evidence\\n    result: RAGEN GRPO 退化 3/3\\n  depends_on:\\n  - D026\\n  - D025\\n- id: D028\\n  date: 2026-05-15 08:32 UTC\\n  summary: 终止 verl-agent 直接运行尝试，全力转向 Track B cherry-pick（步独立 rollout + GiGPO 整合到 RAGEN）\\n  rationale: 'verl-agent 在 bjb1-17606 上 6 次启动失败（exp025→exp025b×3→dry run v7/v8/threadopt），根因是\\n    AutoDL 容器 cgroup pids.max=20480 限制。Ray 集群 + FSDP + vLLM TP 的线程总数超过此限制，即使单 GPU\\n    降级配置也在训练阶段崩溃。AutoDL 无法调整 pids.max，暂无非容器化服务器可用。继续在同一配置重试无意义。\\n\\n\\n    Track B cherry-pick 是可行路径：将 step-independent rollout + GiGPO 算法整合到 RAGEN 代码库（不依赖\\n    Ray，已验证可在此服务器运行）。Track B 分析报告已完成（gigpo_cherry_pick_plan.md），方案明确（~480 行新增 + ~200\\n    行修改，8 文件，3-5 天）。\\n\\n\\n    附带收获：verl-agent val_before_train 产出了 Qwen3-1.7B raw baseline（success=6.2%，与 RAGEN\\n    SFT 后的 6.25% 接近），确认模型基础能力跨框架一致，训练算法是关键差异。'\\n  related_experiments:\\n  - exp_id: exp025\\n    role: evidence\\n    result: 'failed: conda env 错误'\\n  - exp_id: exp025b\\n    role: evidence\\n    result: 'failed: 3次启动失败（vllm模块/Ray GCS/EAGAIN）'\\n  - exp_id: exp025c\\n    role: evidence\\n    result: 未提交，threadopt dryrun 训练阶段崩溃\\n  depends_on:\\n  - D026\\n  - D027\\n- id: D029\\n  date: 2026-05-15 11:14 UTC\\n  summary: exp026 registry 被 cron 误标 DONE(failed)，实际训练仍在运行；速度修正为 30-60min/step（总计\\n    75-150h）\\n  rationale: Cron 5 次检查因 WANDB_MODE=disabled 无法读取指标，自动判定进程死亡并标记 failed。但 PID 存活、GPU\\n    双卡 100% 利用率、日志持续写入。DONE→RUNNING 转换被 registry 禁止，需在训练真正完成后手动更新 conclusion。速度估算从之前的\\n    21min/step 修正为 30-60min/step（step 0 含 val_before_train 耗时 ~40min），150 steps 预计\\n    3-6 天完成。教训：后续实验必须启用 W&B 或 sentinel file 避免 cron 误判。\\n  related_experiments:\\n  - exp_id: exp026_step_independent_grpo\\n    role: subject\\n    result: running (registry incorrectly shows failed)\\n  depends_on:\\n  - D028\\n- id: D030\\n  date: 2026-05-15 11:50 UTC\\n  summary: exp026 等待期并行实现 B-IAVR 核心机制代码（action-change gating），不再空等 baseline 结果\\n  rationale: Reviewer 战略审查指出：50 个实验全在 pipeline debugging，核心 B-IAVR 选择性验证机制零实现。即使 exp026\\n    成功（weak story），真正的论文实验（有/无 selective verification ablation）还没开始。利用 3-6 天训练等待期提前铺核心代码，exp026\\n    出结果后可直接进入核心实验阶段，压缩整体时间线。\\n  related_experiments:\\n  - exp_id: exp026_step_independent_grpo\\n    role: baseline\\n    result: running\\n  - exp_id: exp020b_grpo_from_sft\\n    role: evidence\\n    result: failed - entropy collapse\\n  - exp_id: exp022_grpo_from_sft_v4\\n    role: evidence\\n    result: failed - entropy collapse\\n  - exp_id: exp023c_grpo_serial\\n    role: evidence\\n    result: failed - entropy collapse\\n  depends_on:\\n  - D029\\n  - D028\\n- id: D031\\n  date: 2026-05-15 12:13 UTC\\n  summary: B-IAVR 代码审查通过（Reviewer info），Phase B 前必须解决两个 warning：&lt;VERIFY> special token\\n    注册 + a_pre 推理开销量化\\n  rationale: Reviewer 审查 B-IAVR 核心代码：reward 公式/Lagrangian 更新/模块化设计/52 个测试全通过，与 IDEA_BRIEF\\n    一致。但 &lt;VERIFY> 若被 tokenizer 拆为 8 个子 token 会显著增加学习难度（必须注册为 special token）；a_pre\\n    每次 verify step 额外一次 greedy decode 可能增加 15-30% 步耗时（需 dry run 量化）。这两项是 Phase B 集成前的硬性前置。\\n  related_experiments:\\n  - exp_id: exp026_step_independent_grpo\\n    role: baseline_for_phase_b\\n    result: running\\n  depends_on:\\n  - D030\\n- id: D032\\n  date: 2026-05-15 12:33 UTC\\n  summary: exp026 前 2 步训练指标强正向（success 6.25%→32.81%，entropy 未 collapse），等 step 5 val\\n    做 MVP 判定\\n  rationale: 从 Ray worker stdout logs 提取到训练指标，解决了之前的盲飞问题。Step 1 train success 21.88%\\n    已超 MVP 目标（20%），但 train ≠ val，需等 step 5 val（test_freq=5）确认。Entropy 上升（0.267→0.317）而非\\n    collapse，与之前 3 次 RAGEN GRPO 失败形成鲜明对比，确认 step-independent context + step-level\\n    credit assignment 是关键因素。MVP 判定标准：val success ≥ 20% → complete_mvp()。\\n  related_experiments:\\n  - exp_id: exp026_step_independent_grpo\\n    role: subject\\n    result: train success 32.81% at step 2, awaiting step 5 val\\n  depends_on:\\n  - D029\\n  - D030\\n- id: D033\\n  date: 2026-05-15 13:02 UTC\\n  summary: exp026 registry 误判修复：cron 因 WANDB_MODE=disabled + 监控错误 PID 误标 DONE(failed)，实际训练正常运行（PID\\n    781795）。已重置 RUNNING 并修正监控。后续实验硬规则：禁止 WANDB_MODE=disabled\\n  rationale: 两个根因：(1) WANDB_MODE=disabled 导致 cron 无 sentinel/metrics 可检测；(2) 监控了 shell\\n    wrapper PID 778562 而非实际训练进程 PID 781795。Reviewer 交叉验证确认 step 1-2 指标真实。修复后 cron\\n    间隔 300s 监控正确 PID + log_path。教训沉淀：所有实验必须启用 W&B 以确保 cron 可监控。\\n  related_experiments:\\n  - exp_id: exp026_step_independent_grpo\\n    role: affected\\n    result: registry reset to RUNNING, actual training healthy\\n  depends_on:\\n  - D029\\n  - D032\\n- id: D034\\n  date: 2026-05-15 13:38 UTC\\n  summary: 建立两级阈值：MVP=20% val（训练可行性 checkpoint），论文 baseline 最低要求=50% val（B-IAVR 的\\n    always-on baseline 需与 Self-Guide 72.7% 可比才有说服力）\\n  rationale: Reviewer 独立评估指出：Self-Guide 在 ALFWorld 上 Qwen3-1.7B GRPO baseline 已达 72.7%，20%\\n    val 处于所有已发表 baseline 底部。step-independent rollout 是 verl-agent cherry-pick 不算本项目贡献，论文贡献必须来自\\n    B-IAVR。在弱 agent（20%）上证明选择性验证的 cost-efficiency 没有说服力——需要 baseline 至少 50-60% 才能让\\n    B-IAVR 的 Pareto efficiency claim 有意义。MVP 阈值保持 20% 不变（证明 GRPO 在 RAGEN 能跑），但内部明确论文可行性需要\\n    val 收敛到更高水平。Reviewer 估计 150 步训练后 val 可达 60-70%，与 Self-Guide no-SG baseline 可比。\\n  related_experiments:\\n  - exp_id: exp026_step_independent_grpo\\n    role: baseline\\n    result: train 32.81% @ step 2, val pending\\n  depends_on:\\n  - D032\\n  - D033\\n- id: D035\\n  date: 2026-05-15 14:01 UTC\\n  summary: exp026 训练不稳定（step 2 峰值 32.81% → step 4 归零），准备 exp027 调参重跑；save_freq 必须降至\\n    5\\n  rationale: Step 4 success=0%, pass@16=0。非 entropy collapse（entropy 稳定 0.387），而是\\n    step 3 负梯度过度纠正导致保守退化（KL 回落至 0.054，action_is_valid 反升至 71.7%）。LR=1e-6 对 step-level\\n    reward 的高方差梯度过大。save_freq=25 导致 step 2 的 32.81% 峰值无 checkpoint 可恢复——这是最大损失。exp027\\n    方向：降 LR（→5e-7）、升 KL coef（0.01→0.04）、save_freq=5。等 step 5 val 确认后正式切换。\\n  related_experiments:\\n  - exp_id: exp026_step_independent_grpo\\n    role: evidence\\n    result: 'training unstable: peak 32.81% at step 2, collapsed to 0% at step 4'\\n  depends_on:\\n  - D032\\n- id: D036\\n  date: 2026-05-15 14:07 UTC\\n  summary: Reviewer critical 确认 exp026 GRPO 死亡螺旋：step 4 success=0%，KL→0.0025 策略回退到\\n    reference，exp027 需针对性解决稀疏奖励崩塌\\n  rationale: Reviewer 独立核实训练指标：step 2 峰值 32.81% 后单调下降，step 4 完全崩塌（64 rollout 全失败）。KL\\n    单调递减说明策略不是发散而是回退到 reference，固定 KL penalty 无效。exp027 必须引入 dynamic sampling（过滤零奖励\\n    batch）+ 调整 clip ratio + 可能加 entropy bonus 维持探索。已向 Agent 发送 exp027 设计修正指令。\\n  related_experiments:\\n  - exp_id: exp026_step_independent_grpo\\n    role: primary\\n    result: collapsing\\n  - exp_id: exp027_stable_grpo\\n    role: next\\n    result: preparing\\n  depends_on:\\n  - D035\\n- id: D037\\n  date: 2026-05-15 15:17 UTC\\n  summary: exp027 val 判定阈值：<20% fail、20-25% weak (=SFT)、30%+ proceed Phase B。Reviewer\\n    指出 GRPO 从未在 val 超越 SFT baseline，train-val gap 是系统性风险。\\n  rationale: 'Reviewer pass/fail 评估揭示关键事实：51 个实验中所有 GRPO 的 val success 均为 0-12.5%，而\\n    SFT (exp019b) 已达 20%。exp026 的 32.81% 是 train success，已知 train-val 差距巨大（exp023c:\\n    train 29.7% vs val 6.25%）。因此 exp027 的判定必须基于 val success：(1) val<20% → MVP 失败，需\\n    pivot（换服务器跑 verl-agent 原版 or 重评项目）；(2) val 20-25% → GRPO 仅匹配 SFT，RL 训练贡献为零，需重新评估\\n    Phase B 是否建在 SFT 上；(3) val≥30% → GRPO 首次超越 SFT，Phase B 有意义的 baseline，proceed。A\\n    类会议需 val≥40% + 第二环境 + 模型规模实验，预估 500-800 GPU-h。'\\n  related_experiments:\\n  - exp_id: exp027_stable_grpo\\n    role: 被判定对象\\n    result: running\\n  - exp_id: exp026_step_independent_grpo\\n    role: 前置实验\\n    result: negative\\n  - exp_id: exp019b_expert_sft_v3\\n    role: SFT baseline对照\\n    result: success\\n  depends_on:\\n  - D036\\n  - D034\\n- id: D038\\n  date: 2026-05-15 15:17 UTC\\n  summary: Reviewer 评估 exp027 pass/fail 论文可行性：修正 claim 强度阈值，确认 val success 是唯一判定标准\\n  rationale: 'Reviewer 指出关键事实：GRPO 从未在 val 上超越 SFT baseline（RAGEN 框架内 6.25%）。exp026\\n    的 32.81% 是 train success 不是 val success，train-val 差距系统性存在（exp023c: train 29.7%\\n    vs val 6.25%）。但 Reviewer 混淆了两个 eval 框架：exp019b 的 20% 是 eval_sft_fast（非 RAGEN eval），RAGEN\\n    框架内 SFT baseline 是 6.25%（exp021 C003-compliant 16ep eval）。因此 exp027 val ≥ 20%\\n    = 3.2× SFT baseline，仍是有意义的 RL 贡献，不是\\\"仅匹配 SFT\\\"。但 Reviewer 对 A 类会议的要求评估（Phase B +\\n    ablation + 第二环境 + scaling = 500-800 GPU-h）是合理的。结论：val success 是唯一判定标准，train success\\n    仅作 training dynamics 参考；MVP 20% 的门槛在 RAGEN eval 框架下仍然有效且有意义。'\\n  related_experiments:\\n  - exp_id: exp027_stable_grpo\\n    role: subject\\n    result: running\\n  - exp_id: exp026_step_independent_grpo\\n    role: evidence\\n    result: negative\\n  - exp_id: exp021_ragen_sft_v4\\n    role: baseline\\n    result: negative\\n  - exp_id: exp019b_expert_sft_v3\\n    role: baseline\\n    result: success\\n  depends_on:\\n  - D036\\n  - D034\\n- id: D039\\n  date: 2026-05-15 16:57 UTC\\n  summary: 论文 framing 方向锁定：cost-efficiency story，不走 performance story；ARES 为主要竞争对标\\n  rationale: Related work survey + Reviewer 评估揭示：ALFWorld SOTA 88-93%，我们最好 6.25%，即使\\n    exp027 达 40% 仍是 bottom tier，performance story 死路。唯一可行路径是 cost-efficiency framing——\\\"在接近\\n    Self-Guide 性能的前提下，通过 RL-trained selective verification 减少 verification 开销\\\"。ARES\\n    (arXiv 2603.07915) 是最近竞争者（per-step adaptive computation），差异化点：(1) binary verify/not-verify\\n    决策更简洁可解释 vs ARES 连续 effort selection，(2) action-change 作为 environment-grounded\\n    reward signal vs ARES 的 SFT router，(3) interactive agent 场景 vs general reasoning。前提条件：baseline\\n    必须 ≥50%（接近 Self-Guide 72.7%），否则 cost-efficiency claim 无意义。\\n  related_experiments:\\n  - exp_id: exp027_stable_grpo\\n    role: MVP gating\\n    result: running\\n  - exp_id: exp026_step_independent_grpo\\n    role: evidence for step-independent approach\\n    result: negative (peak 32.81% then collapsed)\\n  - exp_id: exp021_ragen_sft_v4\\n    role: SFT baseline\\n    result: 6.25% success\\n  depends_on:\\n  - D038\\n  - D037\\n- id: D040\\n  date: 2026-05-15 18:27 UTC\\n  summary: 修正 exp027 step 3 判定框架为三层阈值，Plan B kl_coef 上调至 0.015-0.02，中期评估 adaptive\\n    KL\\n  rationale: Reviewer 独立评估确认 step 2 KL 0.058→0.413 (7x) 为强警告信号，kl_coef=0.005 约束过弱。exp026(KL\\n    collapse)+exp027(KL spike) 揭示固定 kl_coef 的 Goldilocks zone 极窄。修正：(1) 三层判定——绿(success≥10%+KL<0.3)、黄(success≥6.25%+KL\\n    0.3-0.6，准备 Plan B)、红(success<6.25%或KL>0.6，终止)；(2) Plan B kl_coef 从 0.01-0.02 收窄至\\n    0.015-0.02（0.01 在 exp026 已失败）；(3) 增加 entropy(<0.15=collapse)/pass@16(<0.5=零批次风险)/grad_norm(>25=不稳定)\\n    三个辅助监控维度；(4) 中期评估 adaptive KL 实现成本。\\n  related_experiments:\\n  - exp_id: exp027_stable_grpo\\n    role: primary\\n    result: step2 KL spike 0.413, success drop to 10.16%\\n  - exp_id: exp026_step_independent_grpo\\n    role: reference\\n    result: 'symmetric failure: KL collapse to 0.0025'\\n  depends_on:\\n  - D037\\n- id: D041\\n  date: 2026-05-15 19:50 UTC\\n  summary: exp027 瓶颈诊断为 sparse reward 学习信号不足而非 KL 不稳定；Plan B(adaptive KL) 降级，Plan\\n    D(GiGPO/step-level credit) 升为首选备选路线\\n  rationale: Reviewer 独立评估：(1) train success 连续两步 10.16%=plateau，pass@16 从 100%→50%\\n    说明仅 4/8 env groups 有学习信号；(2) exp026(太激进crash)+exp027(太保守plateau)构成稳定性-效率 dilemma，纯超参调整无法解决；(3)\\n    adaptive KL 解决的是 KL 振荡，但 KL 已自修正（0.413→0.248），不是当前瓶颈；(4) Self-Guide 同模型同环境达 72.7%，差异在\\n    step-level dense reward vs binary sparse reward；(5) GiGPO/step-level credit 打破\\n    plateau 概率 40-70% vs 当前 recipe 15-25%。决策：exp027 跑到 step 10（早停条件 train≤12%），并行准备\\n    Plan D。\\n  related_experiments:\\n  - exp_id: exp027_stable_grpo\\n    role: primary\\n    result: step2-3 train success plateau at 10.16%, pass@16 declining\\n  - exp_id: exp026_step_independent_grpo\\n    role: reference\\n    result: aggressive config crashed, complementary failure mode\\n  depends_on:\\n  - D040\\n  - D037\\n- id: D042\\n  date: 2026-05-15 19:50 UTC\\n  summary: 采纳 Reviewer 建议：exp027 跑到 step 10 评估，同时并行准备 Plan D（GiGPO/step-level credit\\n    assignment），不再把 adaptive KL 作为首选 Plan B\\n  rationale: Reviewer 独立评估 exp027 中期趋势：train success 连续两步 10.16% plateau，pass@16 从\\n    100%→50% 持续下滑，50 步内 val 突破 20% 概率 <10%。核心瓶颈已从 KL 不稳定（已自修正）转为学习信号密度不足——sparse binary\\n    reward + GRPO 在 8 env groups 下信号太稀疏。Adaptive KL 只解决 KL 振荡不解决信号密度问题。Self-Guide\\n    论文用同模型同环境达 72.7%，差异在 co-evolving internal reward（step-level dense reward）。Plan\\n    D（GiGPO/step-level credit）估计 40-55% 概率达 20% val，远高于当前 recipe 的 15-25%。决策：(1) exp027\\n    继续到 step 10（~12h），如 train success ≤12% 终止；(2) 立即并行准备 Plan D 代码和方案；(3) Adaptive\\n    KL 降级为 Plan D 的辅助选项而非独立方案。\\n  related_experiments:\\n  - exp_id: exp027_stable_grpo\\n    role: primary\\n    result: step 3 绿区但 plateau at 10.16%, pass@16 下滑\\n  - exp_id: exp026_step_independent_grpo\\n    role: reference\\n    result: 对称失败模式：KL collapse vs KL spike\\n  depends_on:\\n  - D040\\n  - D037\\n- id: D043\\n  date: 2026-05-15 20:15 UTC\\n  summary: Reviewer 发现 recipe gap 是根本问题：参考论文 GRPO baseline 72-73% vs 我们 10%，GiGPO\\n    集成继续但新增 recipe gap 诊断为最高优先级\\n  rationale: GiGPO 论文 Qwen2.5-1.5B GRPO=72.8%, Self-Guide 论文 Qwen3-1.7B GRPO=72.7%,\\n    我们 exp027 Qwen3-1.7B=10.16%@step3。62pp 的 baseline gap 说明瓶颈不在 RL 算法（GRPO vs GiGPO）而在训练\\n    recipe（SFT 起点质量/训练迭代数/环境配置/LR等）。GiGPO 改善 credit assignment 但不解决 recipe gap。必须系统对比训练配置找出差异根因。GiGPO\\n    集成继续（低成本），但预期从\\\"突破 40%+\\\"下调为\\\"增量未知\\\"。\\n  related_experiments:\\n  - exp_id: exp027_stable_grpo\\n    role: primary\\n    result: step3 train success 10.16%, baseline gap 62pp vs reference papers\\n  - exp_id: exp021_ragen_sft_v4\\n    role: reference\\n    result: SFT baseline 6.25%\\n  depends_on:\\n  - D041\\n- id: D044\\n  date: 2026-05-15 20:28 UTC\\n  summary: Recipe Gap 确认三大根因：SFT 毒药 + binary reward 零梯度 + mini-batch 过小；Phase A 策略：Instruct\\n    冷启动 + invalid_action_penalty 最小变更验证\\n  rationale: Recipe Gap 六维对比发现参考论文（Self-Guide 72.7%, GiGPO）均从 Instruct 冷启动而非 SFT，且使用\\n    invalid_action_penalty 区分失败轨迹。我们的 SFT 破坏了 instruction-following 能力（baseline 6.25%），导致\\n    GRPO 零梯度。Phase A 只改两个变量隔离根因验证，GiGPO 算法切换暂缓（先修 recipe 再评估算法）。前置 zero-shot eval\\n    建立 Instruct 真实 baseline。\\n  related_experiments:\\n  - exp_id: exp027_stable_grpo\\n    role: evidence\\n    result: step 1→3 success 35.9%→10.2%, 确认 sparse reward 零梯度\\n  - exp_id: exp026_step_independent_grpo\\n    role: evidence\\n    result: negative, 死亡螺旋\\n  depends_on:\\n  - D043\\n  - D041\\n  - D042\\n- id: D045\\n  date: 2026-05-15 20:39 UTC\\n  summary: exp027 判定 MVP 未通过：train success 13.28%（step 4），pass@16 持续下降至 37.5%，模型特化而非泛化。Step\\n    5 未执行（进程异常终止）。\\n  rationale: 'Step 1→4 趋势：success 35.9%→10.2%→10.2%→13.28%（微升但远低于 20% MVP 阈值），pass@16\\n    100%→62.5%→50%→37.5%（单调下降=探索能力丧失）。历史 train-val gap（exp023c: train 29.7% vs val\\n    6.25%）表明 val 不可能达 20%。D044 recipe gap 分析确认根因为 SFT 毒药 + binary reward 零梯度。进程在 step\\n    4 后异常终止（earlystop worker 可能误杀或自然崩溃），step 5 val 和 checkpoint 均未生成。基于充分的 train 证据直接判定，不补跑\\n    val。'\\n  related_experiments:\\n  - exp_id: exp027_stable_grpo\\n    role: primary\\n    result: MVP 未通过, train success 13.28%, pass@16 37.5%\\n  depends_on:\\n  - D044\\n  - D040\\n  - D037\\n- id: D046\\n  date: 2026-05-15 21:05 UTC\\n  summary: 继续 Phase A：exp028a Instruct 冷启动 + invalid_action_penalty 路线。零样本 eval ≥15%\\n    则直接提交；<15% 则重评项目\\n  rationale: D044 recipe gap 诊断是 52 个实验以来最具证据支撑的根因分析——参考论文（Self-Guide 72.7%, GiGPO\\n    72.8%）均从 Instruct 冷启动且使用 invalid_action_penalty，我们的 SFT 路线破坏了 instruction-following\\n    能力（baseline 6.25%）。exp028a 只改两个变量（Instruct 起点 + invalid_action_penalty），隔离验证 recipe\\n    gap 假设，成本低（预计 <50 GPU-h）。如果修复 recipe 后仍无法达到 20% val，说明瓶颈在 RAGEN 框架层面而非训练 recipe，项目需重评。零样本\\n    eval 阈值 15% 作为 Instruct 模型 baseline 下限——低于此说明模型本身能力不足，recipe gap 不是唯一问题。\\n  related_experiments:\\n  - exp_id: exp027_stable_grpo\\n    role: MVP failed\\n    result: train success 13.28%, pass@16 37.5%\\n  - exp_id: exp028_prereq_zeroshot_instruct\\n    role: 前置验证\\n    result: running\\n  - exp_id: exp028a\\n    role: 下一实验\\n    result: preparing\\n  depends_on:\\n  - D044\\n  - D045\\n- id: D047\\n  date: 2026-05-15 21:06 UTC\\n  summary: 暂停 exp028a 最终定参，等零样本 eval 确认 Qwen3-1.7B base 能力后再决定 model_path 和训练起点\\n  rationale: 发现 Qwen3-1.7B 可能不存在独立 Instruct 变体（base/instruct 同权重，chat template 切换）。如果零样本确实\\n    ≈0%，D044 的\\\"SFT 毒药\\\"假设不成立——SFT 是从 0% 提升到 6.25% 的必要步骤，而非有害步骤。exp028a 的 model_path\\n    选择（base vs SFT checkpoint）完全取决于这个结果。penalty 修复可继续，但训练提交 hold 到零样本结论出来。\\n  related_experiments:\\n  - exp_id: exp028a\\n    role: blocked_by_diagnostic\\n    result: pending\\n  - exp_id: exp027_stable_grpo\\n    role: predecessor\\n    result: negative\\n  - exp_id: exp028_prereq_zeroshot_instruct\\n    role: diagnostic\\n    result: running\\n  depends_on:\\n  - D044\\n  - D045\\n- id: D048\\n  date: 2026-05-15 21:08 UTC\\n  summary: exp028a 采用 SFT checkpoint + invalid_action_penalty 最小变更方案，放弃 \\\"SFT是毒药\\\" 假设\\n  rationale: Qwen3-1.7B 本身就是 instruct 模型，不存在独立 -Instruct 版本。零样本 0%→SFT 6.25% 证明 SFT\\n    有益非有害。真正差距在 GRPO recipe（零梯度/binary reward/batch size）。MVP 阶段隔离单一变量：只加 invalid_action_penalty=-0.1\\n    解决零梯度问题，保留 SFT checkpoint 作为更好起点。Pass 阈值 ≥20%。Option 2（全面 recipe 对齐）变量过多，作为后备。\\n  related_experiments:\\n  - exp_id: exp028_prereq\\n    role: evidence\\n    result: Qwen3-1.7B 零样本 0%，确认即 instruct 模型\\n  - exp_id: exp021\\n    role: baseline\\n    result: SFT val 6.25%\\n  - exp_id: exp027\\n    role: evidence\\n    result: GRPO peak 35.9% → collapse 10-13%，零梯度问题\\n  depends_on: []\\n- id: D049\\n  date: 2026-05-15 21:08 UTC\\n  summary: 'D046: SFT必要性确认 + 下一步双GPU并行策略（D诊断→A+C并行）'\\n  rationale: 零样本0% vs SFT 6.25% vs SFT+GRPO 35.94%证明SFT是必要正效果，根因#1(SFT毒药)证伪。剩余根因#2(零梯度)和#3(mini-batch过小)需修复。策略：先跑5min诊断(enable_thinking=False零样本)排除格式干扰；penalty代码就绪后双GPU并行——一卡跑penalty+mb8，一卡跑penalty+mb32，同时验证根因#2和#3。\\n  related_experiments:\\n  - exp_id: exp021\\n    role: evidence\\n    result: SFT 0%→6.25% success, 0.75%→68.75% action_is_valid\\n  - exp_id: exp027\\n    role: evidence\\n    result: SFT+GRPO step1 35.94% success\\n  - exp_id: D046\\n    role: diagnostic\\n    result: 零样本=0%确认instruct模型\\n  depends_on: []\\n- id: D050\\n  date: 2026-05-15 21:24 UTC\\n  summary: '停止 exp028a（确认与 exp027 功能等价），根因 #2 也被否定，下一步全面对齐 Self-Guide recipe'\\n  rationale: Reviewer 三次报告确认：exp027 代码默认 invalid_action_penalty_coef=0.1 已生效（step_rewards.py\\n    在 exp027 启动前已存在，advantage/min 出现负值）。exp028a 显式设 0.1 = 重复 exp027。三大根因状态：#1 SFT毒药\\n    ❌(D047)、#2 零梯度 ❌(penalty 已生效但仍 10-13%)、#3 mini-batch 过小 ✅未验证。单变量策略连续两次未命中，MVP\\n    需要正面信号——改为对齐 Self-Guide recipe（mini-batch + steps + LR 同时调整），成功后再做 ablation 分解归因。\\n  related_experiments:\\n  - exp_id: exp027\\n    role: evidence\\n    result: penalty=0.1 已默认生效，仍 collapse 到 10-13%\\n  - exp_id: exp028a\\n    role: cancelled\\n    result: 确认与 exp027 功能等价，停止\\n  depends_on: []\\n- id: D051\\n  date: 2026-05-16 03:22 UTC\\n  summary: Setup 审计发现 exp028c 非 Self-Guide 有效复现：step-independent 训练破坏信用分配 + self-guidance\\n    reward 缺失 + val 仅 16 episodes\\n  rationale: Agent 完成 6 维度审计，发现 5 个根本差异。最大嫌疑：RAGEN history_length=2 切断 episode-level\\n    训练导致长程信用分配失效（gamma^49=7.7%），完美解释 train success 波动但 val 不动。Self-guidance ±0.1 step\\n    reward（贡献 8%）完全未实现。Val 16 episodes 分辨率仅 6.25%。决策：exp028c 继续到 step 10 作 baseline\\n    数据点，同时开始 P0/P1 代码修复，修复后启动 exp029 作为真正复现。\\n  related_experiments:\\n  - exp_id: exp028c_selfguide_recipe\\n    role: 触发审计\\n    result: val success 6.25% = baseline after 5 steps\\n  - exp_id: exp027_stable_grpo\\n    role: 同类失败\\n    result: 相同 failure mode\\n  - exp_id: exp026_step_independent_grpo\\n    role: 同类失败\\n    result: 相同 failure mode\\n  depends_on:\\n  - D050\\n  - D045\\n  - D044\\n- id: D052\\n  date: 2026-05-16 07:54 UTC\\n  summary: exp028c 终止：step 10 val success=0%（灾难性崩溃），MVP 确认失败。根因：step_independent h=2\\n    导致过拟合 train distribution + 灾难性遗忘 val。下一步 exp029 episode-level 训练。\\n  rationale: step_5_val best@128=10.0（满分）→ step_10_val best@800=0.0（完全归零）。模型在 train\\n    distribution 上仍有 10-22% success 但 val 从 6.25% 崩到 0%。D051 分析确认的结构性缺陷（step_independent\\n    h=2）获得最强实验证据：模型过拟合 train 局部 pattern 且灾难性遗忘 val 能力。继续训练浪费 GPU（已用 8.5h，剩余 68h）。立即终止释放\\n    GPU 给 exp029。\\n  related_experiments:\\n  - exp_id: exp028c_selfguide_recipe\\n    role: 终止\\n    result: step_10_val success=0%, catastrophic forgetting\\n  - exp_id: exp027_stable_grpo\\n    role: 同类失败\\n    result: train 13.28% peak, val 未测\\n  - exp_id: exp026_step_independent_grpo\\n    role: 同类失败\\n    result: 相同 failure mode\\n  depends_on:\\n  - D051\\n  - D050\\n  - D037\\n- id: D053\\n  date: 2026-05-16 23:45 UTC\\n  summary: MVP 通过：episode-level GRPO step 5 val=25%（2x baseline），complete_mvp() 进入\\n    research 阶段\\n  rationale: Step 5 val success 25% 远超 15% 阈值（也超过了 step 10 的 25% 门槛）。对比 exp028c step_independent\\n    模式 step_5_val=6.25%，episode-level context window 证明解决了信用分配缺陷。训练稳定（grad_norm 1.0-1.7，无\\n    OOM），pass@8 峰值 75% 证明策略有潜力。KL 上升趋势需关注但不阻碍 MVP 判定。\\n  related_experiments:\\n  - exp_id: exp029_episode_level\\n    role: MVP validation\\n    result: step_5_val=25%, train_peak=35.2%\\n  - exp_id: exp028c_selfguide_recipe\\n    role: negative control (step_independent)\\n    result: step_5_val=6.25%, step_10_val=0%\\n  depends_on:\\n  - D051\\n  - D052\\n- id: D054\\n  date: 2026-05-16 23:53 UTC\\n  summary: 'Post-MVP framing pivot: dual contribution (episode-level training methodology\\n    + selective verification)'\\n  rationale: 'MVP 结果 (exp029 25% vs exp028c 0%) 证明 episode-level credit assignment\\n    本身是强贡献。原 D039 纯 cost-efficiency framing 依赖 baseline ≥50%（当前远未达到），风险过高。新 framing:\\n    Claim 1 (training methodology, already established) 为 primary, Claims 2-3 (selective\\n    verification) 为 conditional secondary。如果收敛后 <40%, Plan A 退到 pure methodology paper。'\\n  related_experiments:\\n  - exp_id: exp029_episode_level\\n    role: primary_evidence\\n    result: step5_val=25%_2x_baseline\\n  - exp_id: exp028c_selfguide_recipe\\n    role: negative_evidence\\n    result: step10_val=0%_catastrophic_collapse\\n  depends_on:\\n  - D053\\n  - D051\\n  - D039\\n- id: D055\\n  date: 2026-05-17 00:48 UTC\\n  summary: Dream Review (weak reject) 响应：修正理论框架（γ decay → dual mechanism），加 GAE baseline，升\\n    seeds 至 5\\n  rationale: Dream simulate 返回 weak reject，核心问题：(1) γ^(T-h) 理论与 GRPO 不匹配（GRPO 无显式\\n    γ），(2) novelty 不足（episode-level 是 REINFORCE default），(3) 统计 power 不足，(4) 缺 GAE\\n    baseline。修正：理论改为 \\\"information bottleneck + gradient signal dilution\\\" 双机制；加 GAE(λ=0.95)\\n    baseline；multi-seed 升至 5；h-sweep 每个 h 3 seeds。总 GPU 预算 P0 从 268h 升至 438h。确认 dual\\n    contribution framing 保持（不退到纯 methodology）。\\n  related_experiments:\\n  - exp_id: exp029_episode_level\\n    role: basis\\n    result: step5_val=25%\\n  - exp_id: exp028c_selfguide_recipe\\n    role: basis\\n    result: step10_val=0%\\n  depends_on:\\n  - D054\\n  - D053\\n- id: D056\\n  date: 2026-05-17 03:32 UTC\\n  summary: Negative 复盘发现：episode-level + valid_action_bonus 可能安全（exp013f gaming 是\\n    step_independent 特有），加入 h-sweep 批次验证\\n  rationale: exp013f 证伪了 \\\"dense reward shaping 帮助 GRPO\\\"，但其 gaming 行为（action_is_valid\\n    97% + task success 0%）是 step_independent 特有的：每步独立优化允许只最大化 per-step bonus。Episode-level\\n    下模型必须优化 trajectory-level total reward，无法独立 game。当前 exp029 的 action_is_valid=55.9%\\n    且在下降，加小 bonus 可能提供额外信号打破 23-25% plateau。这是从 negative 推导的假设，有明确的 parent 链。\\n  related_experiments:\\n  - exp_id: exp013f\\n    role: parent_negative\\n    result: reward gaming under step_independent\\n  - exp_id: exp029_episode_level\\n    role: target\\n    result: plateau at 23-25%, action_is_valid declining\\n  depends_on:\\n  - D055\\n  - D051\\n- id: D057\\n  date: 2026-05-17 04:16 UTC\\n  summary: Early-stop exp029 at step 15 (val=28%, pass@8=92.9%), release GPUs for\\n    h-sweep (plan_002, paper core figure)\\n  rationale: 'Step 15 val=28.125% (marginal +3pp over step 5-10), action_is_valid\\n    degrading (78→55%), action_is_effective dropped to 77%. Continuing has low ROI:\\n    pass@8=92.9% already proves capability exists, main problem is consistency which\\n    current config won''t fix. h-sweep (plan_002) is P0 for paper — shows the cliff\\n    mechanism, directly addresses Dream C1/C2 reviewer concerns. Checkpoint preserved\\n    for future resume. Plan_003c (bonus variant) included in h-sweep batch.'\\n  related_experiments:\\n  - exp_id: exp029_episode_level\\n    role: early_stopped\\n    result: step15_val=28.125%_pass@8=92.9%\\n  - exp_id: exp028c_selfguide_recipe\\n    role: comparison\\n    result: step10_val=0%\\n  depends_on:\\n  - D056\\n  - D055\\n- id: D058\\n  date: 2026-05-17 06:22 UTC\\n  summary: 'Theory correction: \\\"flat advantage\\\" → \\\"γ-attenuated credit + undifferentiated\\n    failure\\\" based on source code verification'\\n  rationale: Agent 源码审计发现 RAGEN step_independent 实现中 compute_step_discounted_returns()\\n    使用 γ-discount，per-window return 不同（非 flat）。实际机制：成功 episode 早期 window 获 γ^k 衰减\\n    return（γ^{N-1}=γ^24≈29%, where N=⌈T/h⌉=25），失败 episode 所有 window 获相同近零 advantage。这比之前的\\n    \\\"identical advantage\\\" 假设更精确，也比最初的 \\\"GRPO has γ\\\" 更 nuanced（γ 在实现层非算法层）。批准 h=2 seed\\n    2 启用 per-window advantage logging 收集实证。\\n  related_experiments:\\n  - exp_id: hsweep_h2_seed1\\n    role: ongoing\\n    result: source code audit during run\\n  - exp_id: exp029\\n    role: baseline\\n    result: episode-level comparison\\n  depends_on:\\n  - D055\\n  - D056\\n- id: D059\\n  date: 2026-05-17 08:11 UTC\\n  summary: h-sweep val 用 post-hoc full-context eval 替代 truncated val，不重启训练\\n  rationale: Reviewer 发现 hsweep val 也受 context_window_mode 影响（h=2 val step 0 = 0%），无法作为纯\\n    credit assignment 崩溃证据。解决方案：训练继续（收集 train metrics），完成后对所有 checkpoint 用 full context\\n    做 post-hoc val eval。这样 cliff figure 的 val 曲线只反映 training credit assignment 效果，不混入\\n    inference context 限制。不重启当前 seed 1（已跑 3h，train metrics 仍有价值）。\\n  related_experiments:\\n  - exp_id: hsweep_h2_seed1\\n    role: trigger\\n    result: val step 0 = 0% due to context truncation\\n  - exp_id: exp028c\\n    role: reference\\n    result: val uses full context, valid collapse evidence 6.25%→0%\\n  depends_on:\\n  - D057\\n- id: D060\\n  date: 2026-05-17 14:10 UTC\\n  summary: 'GAE baseline fallback to REINFORCE++: TRL 1.1.0 移除 ValueHead，改用 REINFORCE++\\n    (running-mean baseline) 作为标准 RL 对照'\\n  rationale: plan_003b 已预留 fallback（\\\"如果实现成本过高，可用 REINFORCE baseline 替代\\\"）。论文核心是 step-independent\\n    vs episode-level credit assignment，不是 critic vs no-critic。REINFORCE++ 作为无 critic\\n    的标准 baseline 足以回答 Dream C4 的 baseline 要求。从头实现 GAE value head 工程成本高且不在论文贡献范围内。\\n  related_experiments:\\n  - exp_id: gae_baseline_seed1\\n    role: primary\\n    result: fallback to REINFORCE++\\n  depends_on:\\n  - D054\\n- id: D061\\n  date: 2026-05-17 16:11 UTC\\n  summary: Selective verification 从核心贡献降级为 proposed future application，论文聚焦双贡献：(1)\\n    sign misattribution 诊断 (2) episode-level 解决方案分析\\n  rationale: Phase B 实验未实现，Reviewer 指出 \\\"贡献承诺与交付不一致\\\"（C2/W4）。论文当前实验证据只支撑诊断和 episode-level\\n    方案，不支撑 selective verification claim。保持诚实定位，将其明确为 future work。\\n  related_experiments:\\n  - exp_id: exp029_episode_level\\n    role: primary\\n    result: success\\n  - exp_id: hsweep_h2_seed1\\n    role: supporting\\n    result: success (collapse confirmed)\\n  depends_on:\\n  - D054\\n  - D060\\n- id: D062\\n  date: 2026-05-17 17:22 UTC\\n  summary: Dream review 分析：放弃 \\\"contrarian\\\" framing，加 factorial experiment (plan_018)，暂不因\\n    r=0.640 pivot\\n  rationale: Dream dream_20260517T133129 (full review) 三档评分 best=3.5, median=3.0,\\n    worst=2.5。跨档一致的结构性问题：(1) 缺 factorial experiment 分离 info loss vs sign misattribution\\n    — 加 plan_018; (2) \\\"contrarian\\\" framing 被 GAGPO 93.5% 直接反驳 — reframe 为 diagnostic\\n    contribution; (3) Turn-PPO 差异化不足 — 需 empirical comparison; (4) related work 不够。同时\\n    Agent 报告 r(adv,step_return)=0.640 contradicts sign misattribution 但分析需要更多诊断（已发\\n    4 个 diagnostic questions），暂不 pivot，γ=1.0 是终极判别器。\\n  related_experiments:\\n  - exp_id: dream_20260517T133129\\n    role: dream_review\\n    result: best=3.5/median=3.0/worst=2.5\\n  - exp_id: plan_018\\n    role: new_experiment\\n    result: planned\\n  - exp_id: plan_019\\n    role: new_experiment\\n    result: planned\\n  depends_on: []\\n- id: D063\\n  date: 2026-05-17 17:40 UTC\\n  summary: r=0.640 解析：sign misattribution 成立但机制比 binary 假设更复杂（Type C evidence）\\n  rationale: Reviewer 独立核实 800 条 ADV log，发现三类 window：(A) 成功+正adv=正确信号 20条; (B) 有penalty失败+负adv=format\\n    signal 748条; (C) 零penalty失败+正adv=sign misattribution直接证据 32条(4%)。Type C 证明 sign\\n    misattribution 存在：episode 失败但因 group mean 被 penalty windows 拉负，无penalty的失败 window\\n    反而获得正 advantage 被强化。r=0.640 由 penalty 驱动的真实变异（区分 format 不区分 task），不是纯 artifact\\n    也不是反驳。Proposition 2 的 binary 假设需修正为包含 penalty 影响的版本。Worker 2 \\\"假说不成立\\\"过强，Worker\\n    1 \\\"纯伪影\\\"也不完全准确。\\n  related_experiments:\\n  - exp_id: hsweep_h2_seed2\\n    role: data_source\\n    result: 800 ADV log records analyzed\\n  - exp_id: plan_004\\n    role: verification\\n    result: partially complete - mechanism confirmed with nuance\\n  - exp_id: plan_018\\n    role: next_step\\n    result: still needed for relative contribution\\n  depends_on:\\n  - D062\\n- id: D064\\n  date: 2026-05-17 17:57 UTC\\n  summary: Eval 切换到 valid_unseen(134) 对齐文献标准 + re-eval exp029 checkpoint 做校准\\n  rationale: Worker 发现当前所有实验 val 使用 valid_seen(ID, 140 tasks 的 32-subset)，但 ALFWorld\\n    文献标准（Self-Guide, RAGEN 等）使用 valid_unseen(OOD, 134 tasks)。论文提交必须与文献可比。选 Option\\n    A：未来实验统一 valid_unseen(134)。已完成的 h-sweep 内部相对比较仍有效（同 eval 下对比），但 exp029 需要在 valid_unseen\\n    上重新 eval 一次做绝对值校准。不选 Option C（两个都跑）因为 eval 时间翻倍且审稿人只看一套数字。\\n  related_experiments:\\n  - exp_id: plan_019\\n    role: trigger\\n    result: eval expansion feasibility confirmed\\n  - exp_id: exp029_episode_level\\n    role: needs_reeval\\n    result: checkpoint needs valid_unseen eval\\n  depends_on:\\n  - D062\\n- id: D065\\n  date: 2026-05-17 18:06 UTC\\n  summary: gae_baseline_seed1 (REINFORCE++) step 10 early-stop 阈值：success < 10% 且无上升趋势则\\n    kill，释放 westd cuda:0,1\\n  rationale: Step 7 success=7.81%, entropy=0.03（近确定性策略但表现差）。对比 exp029 episode-level\\n    GRPO step 5 已达 25%。REINFORCE++ 作为 baseline 已提供有价值数据点（per-token baseline 不解决 credit\\n    assignment），继续跑下去 GPU 时间投入回报递减。释放的 cuda:0,1 可用于 plan_018 factorial 或 gsweep 后续。\\n  related_experiments:\\n  - exp_id: gae_baseline_seed1\\n    role: subject\\n    result: step7 success=7.81% entropy=0.03\\n  - exp_id: exp029_episode_level\\n    role: comparison\\n    result: step5 success=25%\\n  depends_on:\\n  - D063\\n- id: D066\\n  date: 2026-05-18 01:24 UTC\\n  summary: factorial step 5 反弹确认 sign misattribution 是 collapse 主因，information loss\\n    限制上限但不致 collapse。Claim 升级为 dual mechanism factorial separation。\\n  rationale: factorial step 5 train success 从 3.13% 反弹到 15.63%，val 从 2.24% 升至 5.97%，entropy\\n    健康(0.70)，action_valid 稳定(80%)。对比 hsweep_h2 同期 catastrophic collapse (0% val, 0.06%\\n    action_valid)。step 1-4 的下降是 RL 早期波动非趋势。episode-level advantage 在 truncated context\\n    下确实能学习，sign misattribution 消除是关键。\\n  related_experiments:\\n  - exp_id: factorial_h2_episodeadv_seed1\\n    role: primary\\n    result: step5 train=15.63% val=5.97% V-shaped recovery\\n  - exp_id: hsweep_h2_seed1\\n    role: control\\n    result: step5 catastrophic collapse 0% val\\n  - exp_id: exp029_episode_level\\n    role: comparison\\n    result: 28.1% val (full context upper bound)\\n  depends_on:\\n  - D062\\n  - D063\\n- id: D067\\n  date: 2026-05-18 03:03 UTC\\n  summary: 'Narrative pivot: \\\"catastrophic collapse\\\" → \\\"training fragility/instability\\\"\\n    based on seed divergence evidence'\\n  rationale: 'hsweep_h2_seed2 val=9.375% at step 15 disproves universal catastrophic\\n    collapse. seed1 collapses (0%), seed2 shows delayed generalization (0%→9.375%).\\n    ADV 52% sign agreement proves mechanism (near-random gradient signal) regardless\\n    of seed outcome. New narrative: sign misattribution makes step-independent training\\n    fragile and unreliable — some seeds collapse, others learn slowly with much lower\\n    ceiling. More honest and still strong: \\\"fragile/unreliable training\\\" is an equally\\n    important negative finding for practitioners, with stronger evidence support than\\n    \\\"always collapses\\\".'\\n  related_experiments:\\n  - exp_id: hsweep_h2_seed1\\n    role: evidence\\n    result: catastrophic collapse (val=0%)\\n  - exp_id: hsweep_h2_seed2\\n    role: evidence\\n    result: delayed generalization (val=9.375% at step 15)\\n  - exp_id: factorial_h2_episodeadv_seed1\\n    role: evidence\\n    result: V-shaped recovery (25.78%), stable learning under episode-level advantage\\n  - exp_id: exp029_episode_level\\n    role: baseline\\n    result: 28.1% with full context + episode-level\\n  depends_on:\\n  - D062\\n  - D063\\n  - D066\\n- id: D068\\n  date: 2026-05-18 03:52 UTC\\n  summary: 'exp029 OOD reeval: 23.88% on 134 tasks. Information loss preliminary estimate\\n    17.9pp, action_is_valid insight confirms mechanism'\\n  rationale: 'exp029 step 15 on AlfworldOOD 134 tasks: success=23.88% (vs 28.1% on\\n    in-dist 32 tasks, -4pp as expected). Preliminary decomposition on unified OOD\\n    set: information loss (B→C) = 23.88% - 5.97% = 17.9pp. Sign misattribution (A→B)\\n    still missing Cell A OOD data (hsweep_h2 reeval pending). Key insight: action_is_valid\\n    nearly identical between factorial (57.65%) and exp029 (56.84%) despite 18pp success\\n    gap — full context advantage is in decision quality not action legality, supporting\\n    information loss mechanism narrative. Caveat: factorial only at step 5 (step mismatch)\\n    and KL inflating (0.24→1.77), final decomposition needs factorial step 15.'\\n  related_experiments:\\n  - exp_id: exp029_episode_level\\n    role: primary\\n    result: 23.88% OOD success\\n  - exp_id: factorial_h2_episodeadv_seed1\\n    role: comparison\\n    result: 5.97% OOD at step 5, KL inflating\\n  - exp_id: hsweep_h2_seed2\\n    role: pending\\n    result: OOD reeval needed for Cell A\\n  depends_on:\\n  - D066\\n  - D067\\n- id: D069\\n  date: 2026-05-18 04:47 UTC\\n  summary: 'GPU priority shift: exp029 seed 2 + factorial seed 2 > h10 restart. Statistical\\n    power is P0 risk.'\\n  rationale: 'Reviewer assessment of Dream Review 6 Criticals concludes C3 (statistical\\n    power) is the only desk-reject-level risk. Core causal claim (factorial) and core\\n    positive result (exp029) both rest on single seeds. Reprioritize: (1) bjb1 after\\n    reeval → exp029 seed 2 instead of h10 restart; (2) westd cuda:0,1 after factorial\\n    seed 1 → factorial seed 2. h10 deferred — it contributes to cliff figure (nice-to-have)\\n    but doesn''t address P0 risk. The 2 extra seeds directly address \\\"how do you know\\n    this isn''t noise from one seed\\\" concern.'\\n  related_experiments:\\n  - exp_id: exp029_episode_level\\n    role: needs_replication\\n    result: 23.88% OOD single seed\\n  - exp_id: factorial_h2_episodeadv_seed1\\n    role: needs_replication\\n    result: running step 8/15, 1 seed\\n  depends_on:\\n  - D067\\n  - D068\\n- id: D070\\n  date: 2026-05-18 04:58 UTC\\n  summary: '3-cell decomposition: information loss 89% (17.9pp) >> sign misattribution\\n    11% (2.2pp). Narrative rebalance needed.'\\n  rationale: 'OOD 134 tasks unified decomposition: Cell A (step-indep + step-level)\\n    3.73%, Cell B (step-indep + episode-level) 5.97%, Cell C (full context + episode-level)\\n    23.88%. Sign misattribution effect (A→B) = 2.24pp; information loss effect (B→C)\\n    = 17.91pp. Ratio ~1:8. Paper cannot claim sign misattribution as primary driver\\n    of performance loss. However, sign misattribution still matters for training STABILITY\\n    (seed1 collapse vs seed2 delayed recovery, 52% sign agreement = noisy gradient).\\n    Two mechanisms damage training in orthogonal dimensions: information loss limits\\n    WHAT you can learn (ceiling), sign misattribution determines WHETHER you learn\\n    (stability). CAVEAT: Cell B is step 5 only; factorial step 10-15 may change this\\n    ratio significantly. Step mismatch makes current decomposition preliminary.'\\n  related_experiments:\\n  - exp_id: hsweep_h2_seed2\\n    role: Cell A\\n    result: 3.73% OOD at step 15\\n  - exp_id: factorial_h2_episodeadv_seed1\\n    role: Cell B\\n    result: 5.97% OOD at step 5 (preliminary)\\n  - exp_id: exp029_episode_level\\n    role: Cell C\\n    result: 23.88% OOD at step 15\\n  depends_on:\\n  - D067\\n  - D068\\n- id: D071\\n  date: 2026-05-18 05:44 UTC\\n  summary: 'Factorial step 10 val=5.22%: sign misattribution 量化贡献降至 1.49pp (7.4%),\\n    接近噪声。Framing 调整方向：sign misattribution 价值在机制解释力（训练不稳定性），不在量化性能贡献。等 step 15 确认后最终定稿。'\\n  rationale: 'Step 10 3-cell 分解: Cell A 3.73%, Cell B 5.22%, Cell C 23.88%。Cell B-A\\n    差距 1.49pp ≈ 2/134 tasks, Fisher exact p >> 0.05。但 factorial 训练过程中 step 6 达 25.8%\\n    success（Cell A 从未超过 0%），证明消除 sign misattribution 后模型能开始学习，只是 info loss ceiling\\n    + KL 膨胀限制了最终 val 表现。Sign misattribution 的贡献从\\\"量化性能\\\"转向\\\"机制解释\\\"：解释 seed 间 0% vs 9.375%\\n    的随机性、52% sign agreement 的噪声特征。'\\n  related_experiments:\\n  - exp_id: factorial_h2_episodeadv_seed1\\n    role: primary\\n    result: step 10 val=5.22%, train peak step 6=25.8%, KL inflation 0.735→1.029\\n  - exp_id: hsweep_h2_seed2\\n    role: baseline_cell_a\\n    result: OOD 3.73%\\n  - exp_id: exp029_episode_level\\n    role: baseline_cell_c\\n    result: OOD 23.88%\\n  depends_on:\\n  - D070\\n  - D067\\n- id: D072\\n  date: 2026-05-18 09:14 UTC\\n  summary: Kill g080 (已确认坍缩) 释放 westd cuda:2,3 给 g095。Negative 结果（g050/g080 坍缩、factorial\\n    振荡、seed 间 variance）作为论文 diagnostic 贡献的核心内容，不当废数据处理。\\n  rationale: g080 step 5 val=3.125%（低于 SFT baseline 9.38%），entropy=0.185，action_valid=98.2%，完全坍缩且不可逆。继续跑无新信息，GPU\\n    应释放给 g095 定位 γ-cliff 临界点。同时确认叙事方向：diagnostic paper 的贡献恰恰是 failure mode 分析，negative\\n    结果（g050/g080 坍缩曲线、factorial 振荡 vs monotonic collapse 对比、seed 间 variance）直接变成论文\\n    figure/table。\\n  related_experiments:\\n  - exp_id: gsweep_g080_h5_seed1\\n    role: killed_for_resource\\n    result: val 3.125%, entropy collapse confirmed\\n  - exp_id: gsweep_g095_h5_seed1\\n    role: next_launch\\n    result: config ready, dry-run passed\\n  - exp_id: factorial_h2_episodeadv_seed1\\n    role: narrative_source\\n    result: oscillation pattern vs Cell A monotonic collapse\\n  depends_on:\\n  - D071\\n  - D070\\n- id: D073\\n  date: 2026-05-18 10:22 UTC\\n  summary: 3-cell 定量分解在 step 15 失效（Cell B=0.75% < Cell A=3.73%）。放弃 \\\"X% info loss +\\n    Y% sign misattribution\\\" 加法分解，转向定性双机制诊断：sign misattribution 杀死学习能力（Cell A 单调坍缩），info\\n    loss 杀死泛化能力（Cell B 能学但 OOD 崩溃），两者共同作用才导致 step-independent 失败。\\n  rationale: 'Factorial step 15: Cell B val OOD=0.75%, KL=2.845, val action_valid=11%。Train\\n    success=16.41% 但 OOD 完全崩溃，说明 truncated context 下模型 overfit 训练分布但无法泛化。3-cell 加法分解高度依赖\\n    checkpoint 选择（step 5: B>A, step 10: B≈A, step 15: B&lt;A），定量分解不可靠有 cherry-picking\\n    风险。但定性发现更丰富：(1) Cell A 单调坍缩到 0%（sign misattribution 完全阻止学习），(2) Cell B 高方差振荡后\\n    overfit 崩溃（episode advantage 恢复学习信号但 info loss 阻止泛化），(3) Cell C 稳定到 23.88%（两者都解决后正常学习）。这比简单的百分比分解更有洞察力。'\\n  related_experiments:\\n  - exp_id: factorial_h2_episodeadv_seed1\\n    role: primary\\n    result: step 15 val OOD=0.75%, train=16.41%, KL=2.845, 3-cell decomposition breaks\\n  - exp_id: hsweep_h2_seed2\\n    role: cell_a\\n    result: OOD 3.73%\\n  - exp_id: exp029_episode_level\\n    role: cell_c\\n    result: OOD 23.88%\\n  depends_on:\\n  - D071\\n  - D070\\n- id: D074\\n  date: 2026-05-18 13:06 UTC\\n  summary: g095 step 5 val=0% 完全坍缩。γ-cliff 不在 0.80-0.95（之前假设错误），在 γ>0.95。Kill g095\\n    释放 westd cuda:2,3 给 g100（γ=1.0），g100 现在是 γ-sweep 叙事的决定性数据点。\\n  rationale: γ-sweep 全系列：g050 instant collapse, g080 val=3.125%, g095 val=0.0%。三个\\n    γ 值全部坍缩，且 g095(γ=0.95) 比 g080(γ=0.80) 更差。说明 step-independent + step-level advantage\\n    的 collapse 不仅仅是 γ magnitude decay 问题——即使 γ=0.95 保留 63% 信号，sign misattribution\\n    仍然致命。g100(γ=1.0, 无折扣) 是唯一剩余的数据点：如果 g100 也 collapse，则问题完全来自 step-independent windowing\\n    本身；如果 g100 不 collapse，则 γ 确实有贡献但 cliff 极陡（只在 γ=1.0 时消失）。\\n  related_experiments:\\n  - exp_id: gsweep_g095_h5_seed1\\n    role: primary\\n    result: step 5 val=0.0%, entropy collapse 0.341→~0, complete failure\\n  - exp_id: gsweep_g080_h5_seed1\\n    role: comparison\\n    result: step 5 val=3.125%, also collapsed\\n  - exp_id: gsweep_g050_h5_seed1\\n    role: comparison\\n    result: instant collapse from step 1\\n  depends_on:\\n  - D072\\n  - D073\\n- id: D075\\n  date: 2026-05-18 16:29 UTC\\n  summary: g100 (γ=1.0) 坍缩确认。γ-sweep 全系列（0.50/0.80/0.95/1.0）全部坍缩，sign misattribution\\n    是 windowing + group norm 的固有属性，非 magnitude decay\\n  rationale: g100 前 4 步：entropy 0.341→0.148 持续下降，success <1%，与 g095 轨迹几乎一致仅慢 1 步。step\\n    2 response_length spike (700 tokens) 随即坍缩回 43 tokens。γ=1.0 无折扣仍坍缩 → magnitude\\n    decay 不是根因。论文叙事从\\\"γ-cliff\\\"转为\\\"step-independent windowing 的根本不兼容性\\\"（Reviewer 情景 1）。等\\n    step 5 val 最终确认后 kill g100，释放 GPU 给 h-sweep。\\n  related_experiments:\\n  - exp_id: gsweep_g100_h5_seed1\\n    role: decisive\\n    result: collapsing (entropy 0.148 at step 4)\\n  - exp_id: gsweep_g095_h5_seed1\\n    role: comparison\\n    result: collapsed val=0%\\n  - exp_id: gsweep_g080_h5_seed1\\n    role: comparison\\n    result: collapsed val=3.125%\\n  - exp_id: gsweep_g050_h5_seed1\\n    role: comparison\\n    result: instant collapse\\n  depends_on:\\n  - D074\\n- id: D076\\n  date: 2026-05-18 16:29 UTC\\n  summary: factorial_seed2 step 5 P0 跨 seed 验证通过。Cell B \\\"能学不能泛化\\\" 跨 seed 可复现，D073 定性分析确认\\n  rationale: 'seed2 step 5: val OOD 2.24% (vs seed1 5.97%)，train 31.25% (vs seed1\\n    ~16.6%)。OOD 值有方差（2-6% range）但定性结论一致：Cell B 能学但 info loss 阻止泛化。seed2 kl_loss 1.528\\n    已偏高，可能更快发散。继续跑到 step 15 获取完整轨迹。'\\n  related_experiments:\\n  - exp_id: factorial_h2_episodeadv_seed2\\n    role: primary\\n    result: val OOD 2.24%, train 31.25%\\n  - exp_id: factorial_h2_episodeadv_seed1\\n    role: comparison\\n    result: val OOD 5.97% at step 5\\n  depends_on:\\n  - D073\\n- id: D077\\n  date: 2026-05-18 17:47 UTC\\n  summary: 彻底放弃 bjb1 跑 exp029_seed2，转移到 westd。bjb1 转部署 h=20。现有 step 0-20 数据保留\\n  rationale: exp029_seed2 在 bjb1 累计 10+ 次失败：初始 OOM (3次)、存储 I/O crash、FSDP optimizer_offload\\n    bug、磁盘满 crash、vLLM stall (3.5h 空转)。每次修复后出现新问题，bjb1 对 episode-level 训练系统性不可靠。现有数据\\n    step 0-20 (val 37.5% at step 20) 已证明 Cell C seed2 学习能力，完整训练转移到 westd（factorial\\n    完成后释放 cuda:0,1）。bjb1 转部署 step_independent h=20（已验证 h=2 系列在 bjb1 上稳定）。\\n  related_experiments:\\n  - exp_id: exp029_episode_level_seed2\\n    role: primary\\n    result: 10+ failures on bjb1, val 37.5% at step 20\\n  - exp_id: hsweep_h20_seed1\\n    role: replacement\\n    result: pending deployment on bjb1\\n  depends_on:\\n  - D075\\n  - D076\\n- id: D078\\n  date: 2026-05-18 22:47 UTC\\n  summary: factorial_seed2 step 15 完成：两个 seed val OOD 完全一致 (0.75%)，Cell B 跨 seed 验证最终确认。Train\\n    success 差异大 (20% vs 55.5%) 但 OOD 泛化同样崩溃，information loss 结论稳固。\\n  rationale: seed1 和 seed2 在 step 15 的 val OOD 完全一致（0.75% = 1/134），尽管 train success\\n    差距极大。这证明 information loss (M1) 对 OOD 泛化的破坏是确定性的、与 seed 无关的。D076 从 step 5 的定性一致升级为\\n    step 15 的定量一致。\\n  related_experiments:\\n  - exp_id: factorial_h2_episodeadv_seed2\\n    role: primary\\n    result: val OOD 0.75% at step 15, train 55.5%\\n  - exp_id: factorial_h2_episodeadv_seed1\\n    role: comparison\\n    result: val OOD 0.75% at step 15, train ~20%\\n  depends_on:\\n  - D076\\n  - D073\\n- id: D079\\n  date: 2026-05-19 00:45 UTC\\n  summary: h=10 step 5 确认无学习（val=SFT baseline 6.25%, train=0%）。Cliff 边界 h>10。h=2/5/10\\n    全部失败，step-independent 在 h≤10 完全不可行。\\n  rationale: h=10 提供 10 步观察窗口，但 step_independent 模式下仍然完全无法学习（train success=0%, critic\\n    score=0）。结合 h=2 崩溃、h=5(γ-sweep) 全崩溃，cliff figure 的边界至少在 h>10。如果 h=20 也失败，则 step-independent\\n    windowing 在任何非 full context 下都不可行，叙事从 \\\"small h fails\\\" 升级为 \\\"step-independent fundamentally\\n    fails\\\"。\\n  related_experiments:\\n  - exp_id: hsweep_h10_seed1\\n    role: primary\\n    result: step 5 val=6.25% (SFT baseline), train=0%\\n  - exp_id: hsweep_h2_seed1\\n    role: comparison\\n    result: collapse\\n  - exp_id: gsweep_g050_h5_seed1\\n    role: comparison\\n    result: collapse (h=5)\\n  depends_on:\\n  - D075\\n- id: D080\\n  date: 2026-05-19 02:16 UTC\\n  summary: exp029_seed2 完成：val 峰值 31.25% (step 30)，稳定 28.1% (step 35-40)。Cell C 跨\\n    seed 确认——两 seed 均 ~28-31%，与 Cell A 崩溃和 Cell B 0.75% 形成清晰对比。Step 40 后训练已崩溃（train\\n    6.25%, invalid 80%），但 val 保持。Kill 释放 GPU。\\n  rationale: seed1 28.1%@step15, seed2 31.25%@step30, 稳定在 28.1%@step35-40。两 seed 收敛到同一量级，支撑\\n    \\\"Cell C enables non-trivial learning\\\" claim。格式退化（manager_invalid 0.8%→58%）是已知的\\n    extended training 问题，不影响核心 claim。继续跑无增量收益，kill 释放 westd cuda:0,1。\\n  related_experiments:\\n  - exp_id: exp029_episode_level_seed2\\n    role: primary\\n    result: val peak 31.25% (step 30), stable 28.1% (step 35-40)\\n  - exp_id: exp029_episode_level\\n    role: comparison\\n    result: seed1 val 28.1% (step 15), OOD 23.88%\\n  depends_on:\\n  - D078\\n- id: D081\\n  date: 2026-05-19 03:34 UTC\\n  summary: 启动 7B (Qwen3-8B) + ScienceWorld 两条并行实验线。7B 立即用 westd cuda:2,3 下载+零样本 eval；ScienceWorld\\n    先做 CPU 工程适配。用户明确要求\\\"把条件性加分也做掉\\\"。\\n  rationale: 用户要求做全部条件性加分实验（7B 验证 + ScienceWorld）。7B 用 Qwen3-8B（同家族，8B 参数），westd RTX\\n    PRO 6000 96GB 显存充裕。ScienceWorld Reviewer 要求必须用 episode total return 做 GRPO advantage，不用\\n    step-level intermediate reward。两条线可并行：7B 占 GPU，ScienceWorld 工程适配仅 CPU。\\n  related_experiments:\\n  - exp_id: plan_015\\n    role: target\\n    result: starting\\n  - exp_id: plan_014\\n    role: target\\n    result: starting\\n  depends_on:\\n  - D080\\n  - D078\\n- id: D082\\n  date: 2026-05-19 06:12 UTC\\n  summary: westd 反复崩溃根因确认：根分区 overlay 30G 仅剩 3G，Ray/tmux temp 吃满导致连锁崩溃。必须清理 provenance_weight_training\\n    (13G) + 重定向 TMPDIR/RAY_TMPDIR/TMUX_TMPDIR 到数据盘后才能继续使用 westd。\\n  rationale: 'OOD eval 3次 + 7B zeroshot 1次 = 4次崩溃均由根分区满导致。tmux socket 在 /tmp，/tmp\\n    满后 tmux server 死亡，所有子进程收 SIGHUP 被杀。进程死后 temp 文件释放，表面看系统正常但问题会反复出现。Reviewer severity:\\n    critical。'\\n  related_experiments:\\n  - exp_id: exp029_seed2_ood_reeval\\n    role: affected\\n    result: 3x crash\\n  - exp_id: plan_015\\n    role: affected\\n    result: 7B zeroshot crash\\n  depends_on:\\n  - D081\\n- id: D083\\n  date: 2026-05-19 07:45 UTC\\n  summary: Qwen3-8B SFT baseline 80.6% OOD success（vs 1.7B 的 6.25%）。7B RL 实验 hypothesis\\n    从\\\"RL 大幅提升\\\"调整为\\\"step-independent 是否仍导致退化\\\"。核心看 Cell A 是否从 80.6% 下降 + Cell C 是否维持/小幅提升。\\n  rationale: SFT baseline 已 80.6%，RL 提升空间有限。但如果 step-independent 在强 baseline 上仍导致退化，反而是更有力的跨规模证据——sign\\n    misattribution 在任何模型规模下都是结构性问题。实验设计从\\\"who improves more\\\"转为\\\"does step-independent\\n    still harm even strong models\\\"。\\n  related_experiments:\\n  - exp_id: plan_015\\n    role: target\\n    result: hypothesis adjusted\\n  - exp_id: 7b_sft_v1\\n    role: evidence\\n    result: 80.6% OOD success\\n  depends_on:\\n  - D081\\n- id: D084\\n  date: 2026-05-19 10:32 UTC\\n  summary: h=20 step 5 val=15.625% 确认 cliff 在 h=10 和 h=20 之间。Kill h=20 释放 bjb1 GPU，转\\n    exp029_seed2 OOD eval + clean comparison eval。\\n  rationale: Cliff figure 数据完整：h=2(0%), h=5(0%), h=10(6.25%=baseline), h=20(15.625%),\\n    h=full(28-31%)。h=20 继续跑到 15 步需 85h 不值得，step 5 val 数据足够画 cliff figure。bjb1 GPU\\n    转给更紧急的 exp029_seed2 OOD eval（论文表格缺失数据）和 8B SFT clean comparison eval（解决 eval set\\n    confound）。\\n  related_experiments:\\n  - exp_id: hsweep_h20_seed1\\n    role: completed\\n    result: val 15.625% step 5\\n  - exp_id: exp029_seed2_ood_reeval\\n    role: next\\n    result: pending\\n  - exp_id: 8b_sft_clean_eval\\n    role: next\\n    result: pending\\n  depends_on:\\n  - D082\\n- id: D085\\n  date: 2026-05-19 11:14 UTC\\n  summary: Kill 8B Cell A at step 1, 立即启动 8B Cell C (episode-level)。Step 1 三重 collapse\\n    信号已足够支撑 scale-invariance claim。\\n  rationale: 8B Cell A step 1 数据：success 28.1%→12.5% 腰斩, entropy 0.115 ≈ 0, num_actions\\n    47.7/50 max out。三重 collapse 信号与 1.7B 完全一致。继续跑 4-5h 到 step 5 预期 val≈0%，边际信息增量极低。Cell\\n    C (episode-level 正控制) 是论文更缺的数据——同一 8B 模型、同一 80.6% SFT baseline，不同训练模式的对比远比 Cell\\n    A 多跑几步更有论文价值。4 GPU × 4-5h 机会成本应投入 Cell C。\\n  related_experiments:\\n  - exp_id: 7b_cell_a_h2\\n    role: killed\\n    result: 'step1 collapse: 28.1%→12.5%, entropy=0.115, scale-invariant'\\n  - exp_id: 8b_cell_c_episode\\n    role: next\\n    result: pending\\n  depends_on:\\n  - D083\\n  - D084\\n- id: D086\\n  date: 2026-05-19 11:17 UTC\\n  summary: 确认 exp029_seed2 所有 checkpoint 全部丢失（bjb1 + westd），论文 seed2 列只有 in-dist 31.25%，无\\n    OOD。\\n  rationale: bjb1 seed2 目录在磁盘满事故后被清理，westd seed2 在 M019 磁盘危机中删除。bjb1 上 /root/autodl-tmp/checkpoints/exp029/global_step_15/\\n    实际是 seed1 checkpoint。论文用 seed1 OOD 23.88% 作为主要数字，seed2 in-dist 31.25% 作为双 seed\\n    学习确认。两 seed 都学习是 claim 核心，OOD 单 seed 不影响 claim 强度。\\n  related_experiments:\\n  - exp_id: exp029_seed2_ood_step15\\n    role: killed\\n    result: checkpoint lost, cannot execute\\n  - exp_id: exp029_episode_level\\n    role: primary\\n    result: seed1 OOD 23.88%\\n  depends_on:\\n  - D084\\n  - D080\\n- id: D087\\n  date: 2026-05-19 11:28 UTC\\n  summary: 43.75pp information loss 数字 confounded（跨 server eval variance），改用同 server\\n    12.5pp + 安排 temperature=0 deterministic eval 获取可靠数字\\n  rationale: 同一 8B SFT checkpoint 在 bjb1 2GPU 跑 71.875%、westd 4GPU 跑 40.625%，差 31pp。temperature=1.0\\n    + n=32 + FSDP GPU 数差异导致 eval variance 极大。论文不能用跨 server 数字做对比。同 server (westd 4GPU)\\n    对比：full=40.625% vs h=2=28.125% = 12.5pp。安排 bjb1 上 temperature=0 deterministic\\n    eval (full vs h=2) 获取可靠数字。\\n  related_experiments:\\n  - exp_id: 8b_sft_clean_eval\\n    role: confounded\\n    result: 71.875% bjb1, not comparable to westd\\n  - exp_id: 7b_cell_a_h2\\n    role: baseline\\n    result: step 0 val 28.125% westd\\n  - exp_id: 8b_cell_c_episode\\n    role: baseline\\n    result: step 0 val 40.625% westd\\n  depends_on:\\n  - D085\\n- id: D088\\n  date: 2026-05-19 11:46 UTC\\n  summary: Sign misattribution 机制精确化：跨尺度一致 + 概率性触发。1.7B seed1 完整复现 8B 的 entropy oscillation\\n    + negative KL 路径，seed2 正常学习。\\n  rationale: 1.7B seed1 (7o9bjszm) 展示 3 阶段 entropy oscillation + 3 次 negative KL →\\n    15 步崩溃到 0%，与 8B 2 步崩溃同一路径。1.7B seed2 (jhwyg4tc) 同一配置下正常学习。论文 claim 从 \\\"scale-invariant\\n    collapse\\\" 精确化为 \\\"scale-invariant mechanism, stochastic trigger\\\"——更准确且解释了社区为何未普遍注意到问题。与\\n    D067 \\\"unstable/fragile\\\" framing 完美对齐。\\n  related_experiments:\\n  - exp_id: 7b_cell_a_h2\\n    role: 8B evidence\\n    result: entropy collapse→rebound + neg KL, 2-step collapse\\n  - exp_id: hsweep_h2_seed1\\n    role: 1.7B seed1 evidence\\n    result: same pathway, 15-step collapse\\n  - exp_id: hsweep_h2_seed2\\n    role: 1.7B seed2 control\\n    result: normal learning, no anomaly\\n  depends_on:\\n  - D085\\n- id: D089\\n  date: 2026-05-19 11:51 UTC\\n  summary: 启动 ScienceWorld 实验线：用 1.7B 跑 Cell A vs Cell C 对比，解决单环境短板。mendelian-genetics\\n    排除。\\n  rationale: ScienceWorld SFT 数据 2989+ score=100 episodes（79% quality），远超 500 条阈值。mendelian-genetics\\n    2 个 task type 全部失败（gold path 质量问题，非模型问题），排除。ScienceWorld 用 1.7B 即可（解决单环境问题，不需要\\n    8B），可用 bjb1 2卡跑。8B ALFWorld Cell C 用 westd 4卡并行。Cell A vs Cell C on ScienceWorld\\n    是审稿人 \\\"single environment\\\" concern (#5) 的直接回应。\\n  related_experiments:\\n  - exp_id: 8b_cell_c_episode_v2\\n    role: parallel\\n    result: running on westd\\n  - exp_id: scienceworld_sft\\n    role: next\\n    result: planned for bjb1\\n  depends_on:\\n  - D085\\n  - D087\\n- id: D090\\n  date: 2026-05-19 12:54 UTC\\n  summary: 'Cell C v5: use_ref=False 释放 ref model 内存，解决 Catch-22（gpu_mem_util 0.35\\n    backward OOM vs 0.15 VLLM 初始化失败）'\\n  rationale: 4 次 OOM/失败证明 8B FSDP + optimizer + ref model 基础占用 ~90 GiB/GPU，无法在 gpu_memory_utilization\\n    0.15-0.35 间找到平衡点。use_ref=False 释放 ~8 GiB/GPU，允许 gpu_memory_utilization=0.20 同时满足\\n    VLLM 初始化和 backward 空间。代价是无 KL 约束，但验证 \\\"episode-level 8B 能否训练\\\" 比 KL 约束更重要。论文注明 limitation。\\n  related_experiments:\\n  - exp_id: 8b_cell_c_episode\\n    role: v1\\n    result: OOM backward\\n  - exp_id: 8b_cell_c_episode_v2\\n    role: v2\\n    result: OOM backward (token_len no-op)\\n  - exp_id: 8b_cell_c_v3\\n    role: v3\\n    result: OOM backward (mini_batch no effect)\\n  - exp_id: 8b_cell_c_episode_v4\\n    role: v4\\n    result: VLLM init fail (gpu_mem_util too low)\\n  - exp_id: 8b_cell_c_episode_v5\\n    role: v5\\n    result: 'planned: use_ref=False + gpu_mem_util=0.20'\\n  depends_on:\\n  - D085\\n  - D089\\n- id: D091\\n  date: 2026-05-19 13:22 UTC\\n  summary: 'Cell C v6: max_model_len=16384 + 移除 PYTORCH_CUDA_ALLOC_CONF。OOM 已解决（use_ref=False），v5\\n    新错误是 max_model_len=8192 太小（prompt 8450 tokens）+ expandable_segments 与 vLLM 不兼容'\\n  rationale: v5 验证了 use_ref=False + gpu_memory_utilization=0.20 组合可行（VLLM 初始化成功，FSDP\\n    加载正常）。max_model_len=8192 是 v4 为省 KV cache 内存降的，但 Cell C full-context mode 的 prompt\\n    可达 8450+ tokens。16384 匹配 max_prompt_length 配置且在 19.6 GiB VLLM 预算内可行（8B GQA 头减少了\\n    KV cache 需求）。PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True 与 vLLM CuMemAllocator\\n    冲突，必须移除。\\n  related_experiments:\\n  - exp_id: 8b_cell_c_episode_v5\\n    role: parent\\n    result: 'failed: max_model_len too small + CUDA_ALLOC incompatible'\\n  depends_on:\\n  - D090\\n- id: D092\\n  date: 2026-05-19 13:24 UTC\\n  summary: 论文 eval 协议统一为 T=0.4 (do_sample=True)。23.88% 为正确的 exp029 OOD 数字。独立 eval\\n    的 16.4% 是 T=0.0 greedy 的结果，差异来自温度参数而非 checkpoint 或评估错误\\n  rationale: Reviewer 确认根因：RAGEN 内置 eval 用 T=0.4 (do_sample=True) 得 23.88%，独立 eval\\n    脚本用 T=0.0 (greedy) 得 16.4%。Agent 环境中 mild sampling 有助于避免 greedy decoding 的重复循环陷阱，T=0.4\\n    更贴近实际应用场景且与训练 eval 协议一致。论文主表用 T=0.4，per-task breakdown 需用 T=0.4 重跑以保持一致，论文 Experiments\\n    节必须明确标注 temperature 和 sampling 设置。\\n  related_experiments:\\n  - exp_id: exp029_per_task_breakdown\\n    role: evidence\\n    result: 16.4% at T=0.0 vs 23.88% at T=0.4\\n  depends_on: []\\n- id: D093\\n  date: 2026-05-19 13:45 UTC\\n  summary: 'Cell C v7: gpu_memory_utilization=0.25 + max_model_len=16384。0.20 下 KV\\n    cache 仅 1.44 GiB（需 2.25 GiB），增到 0.25 后 KV cache ≈ 6.24 GiB（2.8x 余量）。vs 原 OOM 配置(0.35+ref)净释放\\n    17.6 GiB，backward 空间充足'\\n  rationale: KV cache 计算：gpu_mem_util=0.20 → VLLM 总 19.2 GiB，模型权重占 17.76 GiB，KV cache\\n    仅 1.44 GiB。gpu_mem_util=0.25 → VLLM 总 24 GiB，KV cache = 24 - 17.76 = 6.24 GiB，远超\\n    max_model_len=16384 所需的 2.25 GiB。Backward 空间：相比原失败配置（0.35 + ref model），0.25 少占\\n    9.6 GiB + ref 释放 8 GiB = 净多 17.6 GiB，backward 应无问题。不选 0.30（多给 VLLM 4.8 GiB 无必要），不选方案\\n    A（10240 可能在训练中遇到更长 prompt 再次失败）。\\n  related_experiments:\\n  - exp_id: 8b_cell_c_episode_v5\\n    role: parent\\n    result: 'failed: max_model_len=16384 needs 2.25 GiB KV cache, gpu_mem_util=0.20\\n      only provides 1.44 GiB'\\n  depends_on:\\n  - D091\\n  - D090\\n- id: D094\\n  date: 2026-05-19 14:09 UTC\\n  summary: 'Cell C v8（最后尝试）: ppo_mini_batch_size=2 + gpu_memory_utilization=0.22。v7\\n    backward OOM 缺 3.7 GiB。batch 4→2 约省一半激活内存，util 0.25→0.22 释放 2.88 GiB。如果 v8 仍 OOM，接受\\n    1.7B-only Cell C 数据，不再尝试'\\n  rationale: v7 数据：allocated 110.14 GiB，backward 需 8.94 GiB，可用 5.21 GiB，缺 3.7 GiB。ppo_mini_batch_size\\n    从 4 降到 2，backward 激活内存大约减半（~4.5 GiB）。gpu_memory_utilization 从 0.25 降到 0.22，释放\\n    (0.25-0.22)×96=2.88 GiB，KV cache 从 6.24 降到 3.36 GiB（仍 > 需要的 2.25 GiB）。组合后：可用 ~8.1\\n    GiB，需 ~4.5 GiB，余量 ~3.5 GiB。8B Cell C 连续 8 次失败已消耗大量 GPU 时间，这是最后一次尝试。论文有完整 1.7B\\n    Cell C 数据 + 8B Cell A collapse + 8B info loss，足够支撑 claim。\\n  related_experiments:\\n  - exp_id: 8b_cell_c_episode_v7\\n    role: parent\\n    result: 'failed: backward OOM, 110.14 GiB allocated, need 8.94 GiB, only 5.21\\n      GiB free'\\n  depends_on:\\n  - D093\\n- id: D095\\n  date: 2026-05-19 14:14 UTC\\n  summary: 正式放弃 8B Cell C：4×96GB 硬件不足以容纳 8B FSDP + VLLM + full-context backward（差\\n    ~4 GiB 无可调参数弥补）。论文 8B 验证限于 Cell A collapse + info loss 37.5pp。1.7B Cell C 数据完整充分\\n  rationale: 9 次连续失败穷尽所有配置空间。v8 暴露最后一个约束：ppo_mini_batch_size ≥ micro_batch_per_gpu(1)\\n    × n_gpus(4) = 4，不可再降。gpu_mem_util 0.25→0.22 仅省 2.93 GiB < 缺口 3.73 GiB。8B FSDP\\n    模型 + optimizer + VLLM 基线占用 ~110 GiB / 4GPU，backward 需 ~9 GiB，可用仅 ~5 GiB。根本矛盾：full-context\\n    episode 的长序列 backward 激活在 96GB GPU 上装不下。论文有 1.7B Cell C 完整数据（23.88% OOD, 双 seed）+\\n    8B Cell A collapse + 8B info loss 37.5pp + stochastic-triggered mechanism，scale\\n    invariance claim 已充分支撑。8B Cell C 缺失在 Limitations 说明。\\n  related_experiments:\\n  - exp_id: 8b_cell_c_episode_v7\\n    role: evidence\\n    result: 'backward OOM: 110.14 GiB allocated, need 8.94, free 5.21'\\n  - exp_id: 8b_cell_c_episode_v5\\n    role: evidence\\n    result: VLLM init + val_before_train passed but backward OOM\\n  depends_on:\\n  - D094\\n  - D093\\n  - D090\\n- id: D096\\n  date: 2026-05-19 14:27 UTC\\n  summary: 'D096: 尝试 FSDP CPU Offload 解决 8B Cell C backward OOM'\\n  rationale: 用户批准\\\"试一下，不行再加卡\\\"。v7 backward OOM 缺口 3.7 GiB，CPU Offload 可省 ~8 GiB/卡，理论上绰绰有余。改动最小（只需修改\\n    FSDP config 加 CPUOffload），不需要改 RAGEN 代码。如果失败，用户同意租更多 GPU。\\n  related_experiments:\\n  - exp_id: 8b_cell_c_episode_v7\\n    role: predecessor\\n    result: backward OOM, gap 3.7 GiB\\n  - exp_id: 8b_cell_c_episode_v8\\n    role: predecessor\\n    result: config constraint violation\\n  depends_on:\\n  - D095\\n- id: D097\\n  date: 2026-05-19 18:17 UTC\\n  summary: 'D097: 8B Cell C v9 (FSDP2 CPUOffload) 失败——RAGEN GRPO train.py 不支持 FSDP2'\\n  rationale: 'v9 启动后立即 NotImplementedError: RAGEN TaskRunner.run() 未实现 FSDP2 strategy。SFT\\n    能用 FSDP2 是因为走 verl 原生 fsdp_sft_trainer，但 GRPO 走 RAGEN 自有代码。D096 的前提（只需改 config）不成立。回到用户决策：加卡还是接受\\n    1.7B-only。'\\n  related_experiments:\\n  - exp_id: 8b_cell_c_v9\\n    role: failed\\n    result: 'NotImplementedError: RAGEN GRPO 不支持 FSDP2'\\n  depends_on:\\n  - D096\\n  - D095\\n- id: D098\\n  date: 2026-05-19 18:34 UTC\\n  summary: 'D098: 让 Agent 修改 RAGEN train.py 支持 FSDP2 + CPUOffload，而非租卡'\\n  rationale: 用户（曹晓玉）建议让 AI 改代码而非租卡。RAGEN train.py 需要 4 处改动（TaskRunner.run FSDP2 分支、update_actor\\n    DTensor 适配、rollout↔training 参数搬运、checkpoint 格式）。Agent 改代码分钟级，westd 4 卡空闲可即时验证。成功则省租卡费用，失败再回退到租卡方案。\\n  related_experiments:\\n  - exp_id: 8b_cell_c_v9\\n    role: predecessor\\n    result: 'NotImplementedError: RAGEN 不支持 FSDP2'\\n  depends_on:\\n  - D097\\n- id: D099\\n  date: 2026-05-19 20:13 UTC\\n  summary: 'D099: 8B Cell C v9c backward pass 成功——FSDP2+CPUOffload 方案可行，8B Cell C\\n    解锁'\\n  rationale: v9c 完成 step 1/30 backward pass 无 OOM。FSDP2+CPUOffload 将峰值显存从 91 GB 降至\\n    83 GB/卡（余量 12 GB），10 次修复（5 文件 10 处 FSDP1→FSDP2 兼容）全部生效。预计 15-16h 完成 30 steps 训练。不需要租卡。\\n  related_experiments:\\n  - exp_id: 8b_cell_c_v9c\\n    role: running\\n    result: step 1/30 完成, backward pass 无 OOM, 83 GB/卡\\n  depends_on:\\n  - D098\\n  - D097\\n  - D096\\n- id: D100\\n  date: 2026-05-19 23:22 UTC\\n  summary: 停止 v9d 修改 save_freq=5 后重启——15h FSDP2 首次完整训练不能无 checkpoint\\n  rationale: v9d 在 step 0（val_before_train 刚完成），save_freq=999 意味着 30 步 15h 训练无中间保存。FSDP2+CPUOffload\\n    在 8B 上是首次完整运行，稳定性未验证；v9c 已在 step 3 崩溃过。Reviewer warning + M029 教训。停下改 config 损失\\n    < 5 分钟，但能保护后续 15h 的中间结果。save_freq=5 每 ~2.5h 存一次 checkpoint。\\n  related_experiments:\\n  - exp_id: 8b_cell_c_episode_v9d\\n    role: target\\n    result: 修改 save_freq 后重启\\n  depends_on:\\n  - D099\\n- id: D101\\n  date: 2026-05-20 05:09 UTC\\n  summary: v9d save_contents 去掉 optimizer——checkpoint 从 92GB 降至 ~33GB，彻底解决磁盘问题\\n  rationale: Reviewer 核实 step 5 checkpoint 实际 92GB（含 4×16.38GB optimizer state），远超估算的\\n    37GB。52GB 可用空间下 step 10 必崩（先写后删需 92GB）。去掉 optimizer 后 checkpoint ~33GB，两个 checkpoint\\n    仅 66GB，加 base ~107GB = 173GB << 250GB，永远安全。load_contents 已确认不含 optimizer，save\\n    端对齐即可。代价：停止当前 step 6 + resume from step 5，损失 ~28min。\\n  related_experiments:\\n  - exp_id: 8b_cell_c_episode_v9d\\n    role: target\\n    result: step 5 healthy, disk crisis\\n  depends_on:\\n  - D100\\n- id: D102\\n  date: 2026-05-20 08:05 UTC\\n  summary: v9d 暂停训练，转向 step 10 OOD eval——8+ 次崩溃指向系统性不稳定，step 10 val=96.875% 数据已足够强\\n  rationale: v9d 从 step 5 到 step 11 训练正常（success 81→97%），但 8+ 次崩溃覆盖磁盘满/model_path\\n    误删/vLLM OOM/SIGHUP/静默死亡多种 failure mode，指向 FSDP2+CPUOffload+4卡 8B 在 westd 上的系统性不稳定。继续重启大概率继续崩。step\\n    10 val=96.875% vs Cell A 1.5% 的对比已足够支撑跨尺度 claim。先做 OOD eval 拿论文数据，同时诊断根因决定是否值得继续训练到\\n    step 30。\\n  related_experiments:\\n  - exp_id: 8b_cell_c_episode_v9d\\n    role: target\\n    result: step 10 val 96.875%, 8+ crashes\\n  depends_on:\\n  - D101\\n- id: D103\\n  date: 2026-05-20 09:24 UTC\\n  summary: v9d step 15 后停止训练——step 12 起 GRPO reward 饱和（100% success, pg_loss=0），继续训练无信号。转向\\n    OOD eval\\n  rationale: Step 12 完整 metrics：train success 1.0，critic score 全 10.0，advantages 全\\n    0，pg_loss=0，grad_norm 0.022。GRPO 依赖 group 内 reward 差异，全组成功则 advantage normalization\\n    为零。Step 12→30 模型权重不会变化（除 entropy drift），等效 GPU 空转。OOD eval 是论文关键数据，step 10/15\\n    checkpoint 已可评估。停训练后释放 westd 4×GPU 用于 OOD eval + 可能的 ScienceWorld GRPO。\\n  related_experiments:\\n  - exp_id: 8b_cell_c_episode_v9d\\n    role: target\\n    result: step 12 reward saturation, 100% in-dist success\\n  depends_on:\\n  - D102\\n- id: D104\\n  date: 2026-05-20 12:14 UTC\\n  summary: Claim 1 升级：从 \\\"unstable/fragile\\\" 升级为 \\\"systematic failure mechanism, scale-invariant\\\"\\n    + \\\"necessary minimum fix\\\"。不用 \\\"catastrophic\\\"（1.7B seed2 学了 9.375%）\\n  rationale: Reviewer 独立评估：8B Cell C 90.3% + Cell A 1.5% 跨尺度对比、γ-sweep 全坍缩、factorial\\n    2×2 全部验证——证据强度已超出 D067 降级时的 \\\"unstable/fragile\\\"。新表述：systematic + scale-invariant\\n    failure mechanism，episode-level 是 necessary minimum fix（不 claim optimal，承认 GAGPO\\n    等更优）。保留 stochastically triggered 解释社区为何未普遍注意。最大风险：R1(trivial fix)+R2(无 fine-grained\\n    baseline) 组合攻击——Practitioner Decision Tree 在 Discussion 中可部分缓解。\\n  related_experiments:\\n  - exp_id: 8b_cell_c_episode_v9d\\n    role: key_evidence\\n    result: 90.3% OOD\\n  - exp_id: 7b_cell_a_h2\\n    role: key_evidence\\n    result: 1.5% collapse\\n  - exp_id: gsweep_g100_h5_seed1\\n    role: supporting\\n    result: γ=1.0 collapse\\n  depends_on:\\n  - D067\\n  - D103\\n- id: D105\\n  date: 2026-05-20 13:26 UTC\\n  summary: ScienceWorld GRPO 三场景预案：(1) Cell A collapse + Cell C learns = 最强; (2) 两者都不学\\n    = diagnosis 仍成立，fix 加限定语; (3) Cell A 不 collapse = 可解释为 \\\"nothing to destroy at\\n    0% baseline\\\"。核心结论：ScienceWorld 是 bonus，不是 load-bearing\\n  rationale: Reviewer 独立评估：三个场景概率 40%/35%/25%。无论哪个场景，ALFWorld 的跨尺度证据（1.7B + 8B）+ factorial\\n    + γ-sweep 已足够 EMNLP ≥ 4.0。ScienceWorld Cell A val_before_train = 0% 使场景 3 有合理解释（sign\\n    misattribution 破坏的是 existing capability，0% baseline 无东西可破坏）。关键诊断指标不仅是 pass@1，还有\\n    entropy/KL 轨迹（区分 active destruction vs no signal）。场景 2 需提前准备 Limitations 段 \\\"capacity\\n    vs credit\\\" 讨论。\\n  related_experiments:\\n  - exp_id: scienceworld_grpo_cell_a\\n    role: pending\\n    result: running\\n  - exp_id: scienceworld_grpo_cell_c\\n    role: pending\\n    result: running\\n  depends_on:\\n  - D104\\n- id: D106\\n  date: 2026-05-20 13:49 UTC\\n  summary: ScienceWorld Cell A 崩溃确认：final_score 6.0→-100.0，比 ALFWorld 更极端。D105 场景\\n    1 上半部成立——failure mechanism 跨环境验证完成\\n  rationale: Cell A (step-independent h=2) 在 ScienceWorld 15 步全程 0% success，final_score\\n    降至 -100.0（ALFWorld 不会负分）。entropy 上升+KL 崩塌模式与 ALFWorld 一致。ScienceWorld 任务结构（科学推理、长\\n    horizon）与 ALFWorld（家务）完全不同，排除环境特异性。等 Cell C 结果完成场景 1 判断。Reviewer 风险 R3 (single\\n    env) 基本解决。\\n  related_experiments:\\n  - exp_id: scienceworld_grpo_cell_a\\n    role: key_evidence\\n    result: collapse confirmed, final_score -100.0\\n  - exp_id: scienceworld_grpo_cell_c\\n    role: pending\\n    result: 1/15 steps, ~7h\\n  depends_on:\\n  - D105\\n- id: D107\\n  date: 2026-05-20 15:34 UTC\\n  summary: ScienceWorld Cell C 崩溃（第3次 Java 异常）：最后重试一次加固版，不阻塞论文压缩\\n  rationale: ScienceWorld Java 环境三次崩溃（Info Loss Eval ×2 + Cell C ×1），root cause 是\\n    Java IPC 通信异常。Cell A collapse 已确认（D106），跨环境 failure 证据充分。Cell C（episode-level\\n    fix 跨环境验证）是 nice-to-have 而非 must-have——论文核心 claim 不依赖它。策略：(1) 最后重试一次，Agent 先调查\\n    Java 异常并加固；(2) Paper Agent 立即推进 16→8 页压缩，不等 Cell C；(3) 若再次崩溃则接受现有数据，Limitations\\n    如实说明。\\n  related_experiments:\\n  - exp_id: scienceworld_grpo_cell_c\\n    role: subject\\n    result: DONE(failed) — Java IPC crash after step 1\\n  - exp_id: scienceworld_grpo_cell_a\\n    role: evidence\\n    result: DONE(negative) — collapse confirmed, cross-env failure validated\\n  depends_on:\\n  - D105\\n  - D106\\n- id: D108\\n  date: 2026-05-21 01:48 UTC\\n  summary: Seed 3 OOD 10.45% (vs Seed 1 23.88%)：Table 1 报 mean[range]，Limitations\\n    加 seed variance 说明。Cell C v3 ScienceWorld episode-level 坍塌：继续观察到 step 5，不影响当前\\n    claim（论文只 claim collapse generalizes，不 claim fix generalizes）\\n  rationale: Seed 3 OOD 差异统计显著 (z=2.91, p<0.005)，但均值 17.2% 仍高于 SFT baseline 12.5%，核心\\n    claim \\\"episode-level avoids collapse and enables learning\\\" 两 seed 都成立。Cell C v3\\n    step 2 reward saturation（128 trajectories 全零 reward），与 Section 3 reward saturation\\n    分析一致——ScienceWorld 更难，episode-level 不能解决 reward saturation。论文已谨慎措辞，只需加 Limitations。\\n  related_experiments:\\n  - exp_id: exp029_seed3_ood_v2\\n    role: seed3 OOD eval\\n    result: 10.45% (14/134)\\n  - exp_id: exp029_episode_level\\n    role: seed1 OOD baseline\\n    result: 23.88% (32/134)\\n  - exp_id: scienceworld_grpo_cell_c_v3\\n    role: SW episode-level fix\\n    result: collapsing at step 2\\n  depends_on:\\n  - D104\\n  - D106\\n- id: D109\\n  date: 2026-05-21 02:41 UTC\\n  summary: Cell C v3 提前终止（step 3），释放 westd cuda:2,3；启动 seed 5 并行训练（westd cuda:0,1）\\n  rationale: Cell C v3 step 3 已满足止损条件（success=0%, action_is_valid=9.4%<20%），且趋势持续恶化（score\\n    2.71→0.96, reward 0.5→0.153），等 step 5 只浪费 ~10 GPU-hours。论文 Limitations 段用 step\\n    3 数据即可。释放的 GPU 加上已空闲的 cuda:0,1，启动 seed 5 并行训练——与 bjb1 seed 4 同时跑，最终 4 个 seed 的\\n    OOD 数据统计可靠性远优于 3 个。当前 2-seed OOD variance 大（10.4% vs 23.9%），4 seeds 可报 mean±std，审稿人信服度显著提升。\\n  related_experiments:\\n  - exp_id: scienceworld_grpo_cell_c_v3\\n    role: terminated\\n    result: 'negative: 3 steps 0% success, collapse confirmed'\\n  - exp_id: exp029_seed4\\n    role: parallel_seed\\n    result: training on bjb1\\n  depends_on:\\n  - D107\\n  - D108\\n- id: D110\\n  date: 2026-05-21 12:09 UTC\\n  summary: 'Seed 5 性能恶化（step 11: 16.4%）但不中止，跑完 15 步；论文 claim 措辞从 \\\"consistently\\\" 调整为\\n    \\\"on average outperforms\\\" + 报告 mean±std'\\n  rationale: Seed 5 train success 从峰值 73.4% 跌到 16.4%（step 11），ppo_kl=0.0059 远高于 Seed\\n    6 的 0.0007。但未 collapse（entropy=0.073>0, pass@8=0.625）。只剩 4 步（~70min），重启不划算。核心\\n    claim 是 \\\"episode-level 不 collapse\\\"（step-level 每 seed 都崩到 0%），Seed 5 虽然性能差但没 collapse，仍支撑\\n    claim。同时 Seed 6 step 11 达 82% train success，表现极强。5-seed mean±std 会有较大方差（OOD 预计\\n    5-25% range），论文需诚实报告并弱化 \\\"consistently\\\" 措辞。\\n  related_experiments:\\n  - exp_id: exp029_seed5_v2\\n    role: primary\\n    result: degrading (16.4% at step 11)\\n  - exp_id: exp029_seed6_v3\\n    role: contrast\\n    result: strong (82.0% at step 11)\\n  - exp_id: exp029_seed4_v2\\n    role: ongoing\\n    result: normal (25.0% at step 5)\\n  depends_on:\\n  - D108\\n- id: D111\\n  date: 2026-05-21 12:15 UTC\\n  summary: Seed 5 因 SFT eval Ray 泄漏 OOM 死亡（step 12）；不重启 seed=456（已退化），改启新 Seed 7 (seed=999)\\n    填满 westd cuda:0,1\\n  rationale: 'SFT eval 配置 CUDA_VISIBLE_DEVICES=1 但 Ray worker 泄漏到 GPU 0，占用 17.13GB\\n    导致 Seed 5 backward pass OOM。同类 bug 见 M041（Ray 集群共享致 GPU 越界）。Seed 5 在 OOM 前已严重退化（step\\n    11: 16.4% success, ppo_kl=0.0059, response_length=4536），重启 seed=456 大概率复现退化。改用新\\n    seed=999 (Seed 7)，westd cuda:0,1 不能空着。Step 10 checkpoint 保留作 supplementary eval\\n    数据点。'\\n  related_experiments:\\n  - exp_id: exp029_seed5_v2\\n    role: failed\\n    result: OOM at step 12 due to SFT eval Ray worker GPU leak\\n  - exp_id: sft_baseline_ood_eval\\n    role: cause\\n    result: Ray worker leaked from GPU 1 to GPU 0\\n  depends_on:\\n  - D110\\n- id: D112\\n  date: 2026-05-21 13:07 UTC\\n  summary: 跨 seed 鲁棒性风险已知但不改方向：5 个完成/进行中的 seed 中无一 true collapse（vs step-level 100%\\n    collapse），方差大但 claim 仍成立，等全部数据到手再调整 claim 措辞\\n  rationale: 'Reviewer 警告 Seed 4 退化（step 7: 12.5%）、Seed 5 OOM 前已退化，成功率似乎仅 1/3。但完整数据含\\n    Seed 1 (23.88% OOD) 和 Seed 3 (10.45% OOD) 均成功完成。核心 claim 是 \\\"episode-level 不 collapse\\\"（step-level\\n    每 seed 崩到 0%），即使退化的 episode-level seed 也在 10%+，区分成立。Response_length 双峰分布（成功 seed\\n    ~500-800 tokens vs 失败 seed ~4500+ tokens）可写入论文作为 analysis 贡献。Seed 7 是关键变量——如果也退化，claim\\n    需弱化为 \\\"enables learning in a subset of seeds\\\"；如果成功，3/5+ seeds 有意义学习。暂不改方向，等数据到齐。'\\n  related_experiments:\\n  - exp_id: exp029_seed4_v2\\n    role: degrading\\n    result: 'step 7: 12.5% success, response_length 7547'\\n  - exp_id: exp029_seed6_v3\\n    role: success\\n    result: 89.06% train success, completed\\n  - exp_id: exp029_seed7\\n    role: pending\\n    result: just started\\n  depends_on:\\n  - D111\\n  - D110\\n- id: D113\\n  date: 2026-05-21 15:59 UTC\\n  summary: 跨 seed 崩溃率 43-50%：论文 claim 从 \\\"avoids collapse\\\" 调整为 \\\"enables learning where\\n    step-level cannot\\\" + response_length 双峰分析作为新贡献\\n  rationale: 7 个已完成/进行中 seed 中 3 个崩溃（Seed 2/4/7），Seed 5 OOM 前也在退化。Episode-level 不能可靠防止崩溃，但有两个关键区分：(1)\\n    step-level 100% collapse vs episode-level ~50%，改善幅度显著；(2) 崩溃机制不同——step-level 是\\n    entropy→0 的 true collapse（M1/M2 病理），episode-level 是 response_length 爆炸导致的性能退化，entropy\\n    保持 >0。论文 framing 应调整为：episode-level 修复了 M1/M2 机制性问题，使学习成为可能（step-level 做不到），但暴露了新的失败模式（response\\n    inflation）。崩溃 vs 成功 seed 的双峰分析（response_length 简洁 vs 膨胀）本身是有价值的分析贡献。等 Seed 8 数据确认后最终定调。\\n  related_experiments:\\n  - exp_id: exp029_seed7\\n    role: collapsed\\n    result: 'step 7: 20.3% success, response_length 8803'\\n  - exp_id: exp029_seed4_v2\\n    role: collapsed\\n    result: 'step 14: 20.3%, unstable throughout'\\n  - exp_id: exp029_seed6_v3\\n    role: success\\n    result: 89% train, 29.1% OOD\\n  - exp_id: exp029_seed8\\n    role: pending\\n    result: just started\\n  depends_on:\\n  - D112\\n- id: D114\\n  date: 2026-05-21 20:41 UTC\\n  summary: Intervention A (response length penalty) 失败：penalty 仅影响 training gradient\\n    不影响 inference 生成行为；Intervention B (KL 10x) 初步有效，val resp_len 稳定，等最终结果\\n  rationale: len_penalty 在 agent_trainer.py 加了 per-sample reward penalty，但 penalty\\n    只在 compute_advantage 时生效——inference 时模型仍按原策略生成，导致 rollout resp_len=14284（vs training\\n    1992）。这说明纯 reward shaping 不够，需要约束策略本身。high_kl (kl_loss_coef 0.01→0.1) 直接在 actor\\n    loss 中约束策略偏移，val resp_len 5353 稳定且 val success 28.13% 上升中，step 5/7 趋势健康。Seed 8\\n    step 9 确认崩溃（train success 11%，resp_len 11569），跨 seed 崩溃率升至 4/8 = 50%。\\n  related_experiments:\\n  - exp_id: exp029_seed7_len_penalty\\n    role: intervention_a\\n    result: 'NEGATIVE: val resp_len=7598, success=28.13%'\\n  - exp_id: exp029_seed7_high_kl\\n    role: intervention_b\\n    result: 'IN PROGRESS: val resp_len=5353 stable, success=28.13%'\\n  - exp_id: exp029_seed8\\n    role: collapsing\\n    result: 'step 9: train success 11%, resp_len 11569'\\n  depends_on:\\n  - D113\\n- id: D115\\n  date: 2026-05-21 20:56 UTC\\n  summary: Kill Seed 8 (confirmed collapse) + 启动 Intervention C (response length hard\\n    cap) 作为第三种不同类型的崩溃修复尝试\\n  rationale: 'Seed 8 step 9 resp_len=11569, train_success 35.9%→10.9%, 与 Seeds 4/7\\n    相同的 response inflation 模式，无恢复可能。Kill 释放 westd cuda:2,3。\\n\\n\\n    Intervention A (len_penalty, reward 层面) 和 B (high_kl, 正则化层面) 均为 config-level 同类干预。即使\\n    B 也失败，按 method-improvement 框架仍不满足\\\"2-3 种不同类型\\\"的 pivot 前提。\\n\\n\\n    Intervention C: 在 rollout 生成时硬限 per-turn max_new_tokens (~800 tokens)，物理阻断 response\\n    inflation 的正反馈循环。这是 generation-level 约束，与 reward penalty (A) 和 KL regularization\\n    (B) 是不同类型的干预。成功 seed per-turn ~500-800 tokens，崩溃 seed 4500-8800+。cap 在 800 不影响简洁策略，但阻止冗长策略获得\\n    reward。\\n\\n\\n    用户要求\\\"先尝试挽回\\\"，这是最后一种合理的干预类型。如果 C 也失败 → 三种不同类型干预全部无效 → 满足 method→analysis 切换三前提中的\\n    (a)。'\\n  related_experiments:\\n  - exp_id: exp029_seed8\\n    role: killed\\n    result: 'collapse confirmed: resp_len 11569, train_success 10.9%'\\n  - exp_id: exp029_seed7_len_penalty\\n    role: evidence\\n    result: negative - Intervention A (reward penalty) failed\\n  - exp_id: exp029_seed7_high_kl\\n    role: evidence\\n    result: running - Intervention B (KL regularization), likely negative\\n  depends_on:\\n  - D114\\n  - D113\\n- id: D116\\n  date: 2026-05-21 21:37 UTC\\n  summary: Intervention C' (trajectory-level cap) 在 bjb1 并行测试：response_length=1024\\n    不变 + max_response_length=12000 + max_turn=25\\n  rationale: 'westd 的 Intervention C (512/20) 是 aggressive stress test。C'' 测试更温和的假设：保持原始\\n    per-turn 自由度，只限 trajectory 总量。两个并行结果组合可区分\\\"需要强约束\\\"vs\\\"温和约束够用\\\"vs\\\"generation constraint\\n    整体无效\\\"。\\n\\n\\n    Reviewer 指出原计划 8000 仅比 SFT baseline (7640) 高 4.7%，RL 探索几乎无空间。调整为 12000（57% headroom），成功\\n    seed 6000-8000 不受影响，崩溃 seed 14000-15000 被限到 12000（20% 削减）。'\\n  related_experiments:\\n  - exp_id: exp029_intervention_c_prime\\n    role: primary\\n    result: preparing\\n  depends_on:\\n  - D115\\n- id: D117\\n  date: 2026-05-21 22:26 UTC\\n  summary: Intervention C (per-turn 512/20) 确认失败：mode shift 证明 collapse 是 trajectory-level\\n    行为。三种 config/reward-level 干预全部无效。\\n  rationale: Step 7 train success 15.6%, val 9.375% (=SFT baseline)。模型在 per-turn cap\\n    下转为增加 turn 数补偿（num_actions 18.14/20），trajectory resp_len 从 3754→7170（+91%）。与原始\\n    Seed 7 崩溃时机完全一致（step 7）。结合 A (reward penalty) 和 B (KL 10x) 失败，三种不同层级干预全部无效。但 mode\\n    shift 本身是重要发现：per-turn constraint ≠ trajectory-level control，证明 response inflation\\n    是 emergent trajectory-level 行为。C' (trajectory cap 12000) 在 bjb1 运行中，是最后一个干预维度。\\n  related_experiments:\\n  - exp_id: intervention-c-hard-cap\\n    role: primary\\n    result: negative\\n  - exp_id: exp029_seed7_len_penalty\\n    role: context\\n    result: negative\\n  - exp_id: exp029_seed7_high_kl\\n    role: context\\n    result: negative\\n  - exp_id: exp029_intervention_c_prime\\n    role: next\\n    result: running\\n  depends_on:\\n  - D115\\n  - D114\\n- id: D118\\n  date: 2026-05-22 01:38 UTC\\n  summary: C' step 5 OOD=0% 双服务器确认：max_turn=25 导致严重过拟合训练分布，cap 从未触发（无效实验）\\n  rationale: bjb1 和 westd 均输出 0/134 OOD，排除了 FSDP→HF 转换错误的可能。action_is_valid 97.6%\\n    但每集撞满 50 步上限，说明模型无法在 50-turn eval 中完成任务。C' 训练 max_turn=25（其他实验均 50），且 trajectory\\n    cap 12000 从未触发（max model tokens ~9600）。C' 实际测的是 max_turn=25 而非 trajectory cap，结论无效。需用\\n    max_turn=50 重做才能验证 trajectory cap 假设。\\n  related_experiments:\\n  - exp_id: c_prime_step5_ood_bjb1\\n    role: confirmation\\n    result: OOD=0.0%\\n  - exp_id: c_prime_step5_ood\\n    role: initial_detection\\n    result: OOD=0.0% (westd)\\n  - exp_id: exp029_intervention_c_prime\\n    role: parent_training\\n    result: negative, cap never triggered\\n  depends_on:\\n  - D116\\n  - D117\\n- id: D119\\n  date: 2026-05-22 03:24 UTC\\n  summary: C' mt50 诊断确认：(1) collapse 在 max_turn=50 下复现，排除 max_turn 为主因；(2) trajectory\\n    cap 12000 实质失效（resp_len=13304 超 cap 但 aborted_ratio=0）；(3) 四种干预全部失败/无效，转向诊断论文叙事\\n  rationale: C' resume_mt50_v2 step 6→7 完全复现经典 collapse（peak 31.25% → crash 16.41%，resp_len\\n    11440→13304）。关键：step 7 resp_len=13304 超过 12000 cap 但 aborted_ratio=0，说明 trajectory\\n    cap 代码实现本身有问题（可能只是 per-turn 限制而非 trajectory 总长）。至此四种干预方向：A(reward penalty)失败、B(KL\\n    10x)失败、C(per-turn cap)mode shift 失败、C'(trajectory cap)实现无效+collapse 复现。用户指示\\\"先尝试挽回，不行再调整叙事\\\"——已穷举四种方向，应执行叙事调整。\\n  related_experiments:\\n  - exp_id: exp029_c_prime_resume_mt50_v2\\n    role: diagnostic\\n    result: collapse reproduced, cap never triggered despite exceeding 12000\\n  - exp_id: exp029_intervention_c_prime\\n    role: parent\\n    result: negative\\n  - exp_id: intervention-c-hard-cap\\n    role: comparison\\n    result: mode shift\\n  - exp_id: exp029_seed7_len_penalty\\n    role: comparison\\n    result: failed\\n  - exp_id: exp029_seed7_high_kl\\n    role: comparison\\n    result: failed\\n  depends_on:\\n  - D118\\n  - D117\\n- id: D120\\n  date: 2026-05-22 03:34 UTC\\n  summary: 接受 Reviewer 叙事建议：干预实验降级为 Discussion，核心 claim 聚焦双机制诊断 + factorial + 8B scale；ScienceWorld\\n    跨环境验证升为 P0\\n  rationale: Reviewer 审查结论：(1) Claim 1（双机制诊断）证据 VERY STRONG，足够支撑核心贡献；(2) 干预失败/response\\n    inflation/mode shift 证据不足作 core claim（N=1、训练步数混杂、C' 实现 bug）；(3) 无 ScienceWorld\\n    预估 3.0-3.5（Findings），补齐后 3.5-4.0（Conference）。ScienceWorld 是达到 EMNLP 2026 Overall\\n    ≥4 的关键门槛。干预实验放 Discussion/Observations，不稀释核心贡献。seed_2048 step 1-2 即崩溃（resp_len\\n    15511, success 0.78%），无法提供 healthy baseline，但更新 collapse rate 至 4/7=57%。\\n  related_experiments:\\n  - exp_id: exp029_new_seed_2048\\n    role: observation\\n    result: collapsing at step 1-2, resp_len=15865, cannot serve as healthy baseline\\n  - exp_id: exp029_c_prime_resume_mt50_v2\\n    role: parent\\n    result: negative, cap ineffective\\n  depends_on:\\n  - D119\\n\", \"total_chars\": 91759, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 22_

<details><summary>Logged reasoning block</summary>

```text
Let me first probe the structure of the registry JSON, then fix my extraction. Also need to handle the decisions.yaml file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "58905ce6-10f3-478d-831f-4f649a582691",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rjtua6vzA4JTHgzfxF2b32",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1318,
      "cache_read_input_tokens": 39018,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1318
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

需要先探测 JSON 结构。让我用 agent 并行处理这两个大文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "78924da0-fc23-4296-be20-707063ea7cc7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rjtua6vzA4JTHgzfxF2b32",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1318,
      "cache_read_input_tokens": 39018,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1318
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

<details open><summary>🔧 Tool call — Agent · `toolu_01N2zJUo1dnEGhGjTPYb6p2w`</summary>

```json
{
  "description": "Extract ScienceWorld experiments from registry",
  "prompt": "I need to extract all ScienceWorld-related experiments from a large registry JSON file. \n\nThe file is at: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-1-projects-cost-verify-agent-rl/54b94781-146b-4013-9381-11e3737077cb/tool-results/mcp-agent-ml-research-read_registry-1779420967332.txt\n\nIt's JSON with schema: {result: string}. The `result` field is itself a JSON string that needs to be parsed.\n\nSteps:\n1. Probe the structure with python to understand the nesting (type, length, keys of the parsed result)\n2. Find all experiments where exp_id, hypothesis, spec, conclusion, tags, or any text field contains \"scienceworld\", \"science_world\", \"science-world\", \"sw_\", \"_sw\", or \"ScienceWorld\"\n3. For each matching experiment, output ALL fields verbatim — especially: exp_id, status, created_at, updated_at, hypothesis, spec (including hyperparameters), conclusion, failure_reason, metrics, tags\n\nReturn the complete data for all matching experiments. Do NOT summarize — I need the raw data."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "a8503a38-2581-4337-a700-84b2aad08e35",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rjtua6vzA4JTHgzfxF2b32",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1318,
      "cache_read_input_tokens": 39018,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1318
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

_source line 25_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a81374730ba0416fe",
  "tool_use_id": "toolu_01N2zJUo1dnEGhGjTPYb6p2w",
  "description": "Extract ScienceWorld experiments from registry",
  "task_type": "local_agent",
  "prompt": "I need to extract all ScienceWorld-related experiments from a large registry JSON file. \n\nThe file is at: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-1-projects-cost-verify-agent-rl/54b94781-146b-4013-9381-11e3737077cb/tool-results/mcp-agent-ml-research-read_registry-1779420967332.txt\n\nIt's JSON with schema: {result: string}. The `result` field is itself a JSON string that needs to be parsed.\n\nSteps:\n1. Probe the structure with python to understand the nesting (type, length, keys of the parsed result)\n2. Find all experiments where exp_id, hypothesis, spec, conclusion, tags, or any text field contains \"scienceworld\", \"science_world\", \"science-world\", \"sw_\", \"_sw\", or \"ScienceWorld\"\n3. For each matching experiment, output ALL fields verbatim — especially: exp_id, status, created_at, updated_at, hypothesis, spec (including hyperparameters), conclusion, failure_reason, metrics, tags\n\nReturn the complete data for all matching experiments. Do NOT summarize — I need the raw data.",
  "uuid": "899b3159-e48f-483a-aec0-53c899132ea8",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb"
}
```

---

## Round 1

3 recorded events

### User

_source line 26 · 2026-05-22T03:36:35.401Z_

I need to extract all ScienceWorld-related experiments from a large registry JSON file. 

The file is at: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-1-projects-cost-verify-agent-rl/54b94781-146b-4013-9381-11e3737077cb/tool-results/mcp-agent-ml-research-read_registry-1779420967332.txt

It's JSON with schema: {result: string}. The `result` field is itself a JSON string that needs to be parsed.

Steps:
1. Probe the structure with python to understand the nesting (type, length, keys of the parsed result)
2. Find all experiments where exp_id, hypothesis, spec, conclusion, tags, or any text field contains "scienceworld", "science_world", "science-world", "sw_", "_sw", or "ScienceWorld"
3. For each matching experiment, output ALL fields verbatim — especially: exp_id, status, created_at, updated_at, hypothesis, spec (including hyperparameters), conclusion, failure_reason, metrics, tags

Return the complete data for all matching experiments. Do NOT summarize — I need the raw data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01N2zJUo1dnEGhGjTPYb6p2w",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "7071ce8c-6cac-49b8-8976-340b9518344a"
}
```

</details>

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Agent · `toolu_01UvN5LYeDV9iSrVapRBHaFQ`</summary>

```json
{
  "description": "Extract ScienceWorld info from decisions.yaml",
  "prompt": "I need to extract all ScienceWorld-related content from a large decisions.yaml file.\n\nThe file is at: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-1-projects-cost-verify-agent-rl/54b94781-146b-4013-9381-11e3737077cb/tool-results/mcp-agent-ml-research-read_project_file-1779420982565.txt\n\nIt's JSON with schema: {result: string}. The `result` field is itself a JSON string containing the YAML content.\n\nSteps:\n1. Parse the JSON to get the YAML content string\n2. Search through the content for any mentions of \"ScienceWorld\", \"scienceworld\", \"science_world\", \"sw_\", \"Cell A\", \"Cell C\" (these are experiment cells that may involve ScienceWorld)\n3. Extract all relevant sections/decisions verbatim\n\nReturn all matching content verbatim. I need the full context around each mention."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "beb78591-d91b-4aee-81a5-1a53c422d8b3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rjtua6vzA4JTHgzfxF2b32",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1318,
      "cache_read_input_tokens": 39018,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1318
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

_source line 28_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "ad21c2477dd6123aa",
  "tool_use_id": "toolu_01UvN5LYeDV9iSrVapRBHaFQ",
  "description": "Extract ScienceWorld info from decisions.yaml",
  "task_type": "local_agent",
  "prompt": "I need to extract all ScienceWorld-related content from a large decisions.yaml file.\n\nThe file is at: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-1-projects-cost-verify-agent-rl/54b94781-146b-4013-9381-11e3737077cb/tool-results/mcp-agent-ml-research-read_project_file-1779420982565.txt\n\nIt's JSON with schema: {result: string}. The `result` field is itself a JSON string containing the YAML content.\n\nSteps:\n1. Parse the JSON to get the YAML content string\n2. Search through the content for any mentions of \"ScienceWorld\", \"scienceworld\", \"science_world\", \"sw_\", \"Cell A\", \"Cell C\" (these are experiment cells that may involve ScienceWorld)\n3. Extract all relevant sections/decisions verbatim\n\nReturn all matching content verbatim. I need the full context around each mention.",
  "uuid": "cb7f85df-ec60-482f-868b-c6eef9a5cc67",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb"
}
```

---

## Round 2

59 recorded events

### User

_source line 29 · 2026-05-22T03:36:39.549Z_

I need to extract all ScienceWorld-related content from a large decisions.yaml file.

The file is at: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-1-projects-cost-verify-agent-rl/54b94781-146b-4013-9381-11e3737077cb/tool-results/mcp-agent-ml-research-read_project_file-1779420982565.txt

It's JSON with schema: {result: string}. The `result` field is itself a JSON string containing the YAML content.

Steps:
1. Parse the JSON to get the YAML content string
2. Search through the content for any mentions of "ScienceWorld", "scienceworld", "science_world", "sw_", "Cell A", "Cell C" (these are experiment cells that may involve ScienceWorld)
3. Extract all relevant sections/decisions verbatim

Return all matching content verbatim. I need the full context around each mention.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UvN5LYeDV9iSrVapRBHaFQ",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "ccf1d025-77f9-46fe-ba7d-eedace7203ac"
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
  "task_id": "a81374730ba0416fe",
  "tool_use_id": "toolu_01N2zJUo1dnEGhGjTPYb6p2w",
  "description": "Running Probe the JSON file structure",
  "usage": {
    "total_tokens": 14973,
    "tool_uses": 1,
    "duration_ms": 6944
  },
  "last_tool_name": "Bash",
  "uuid": "eb0b0ec0-7dd3-4701-9496-e69e29ffa72a",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb"
}
```

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Bash · `toolu_013ZAeTC53cKCTuicCtnK7tK`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-1-projects-cost-verify-agent-rl/54b94781-146b-4013-9381-11e3737077cb/tool-results/mcp-agent-ml-research-read_registry-1779420967332.txt') as f:\n    raw = json.load(f)\n\nprint('Top-level type:', type(raw))\nprint('Top-level keys:', list(raw.keys()) if isinstance(raw, dict) else 'N/A')\nresult = json.loads(raw['result'])\nprint('Result type:', type(result))\nif isinstance(result, dict):\n    print('Result keys:', list(result.keys()))\n    for k, v in result.items():\n        print(f'  {k}: type={type(v).__name__}, ', end='')\n        if isinstance(v, list):\n            print(f'len={len(v)}')\n        elif isinstance(v, dict):\n            print(f'keys={list(v.keys())[:5]}...' if len(v) > 5 else f'keys={list(v.keys())}')\n        else:\n            print(f'value={str(v)[:100]}')\n\"\n",
  "description": "Probe the JSON file structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01N2zJUo1dnEGhGjTPYb6p2w",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "1b344742-3bed-43a4-8108-749715587fab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0156avLTdLiCTqcpGGHZH1wS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14966,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14966,
        "ephemeral_1h_input_tokens": 0
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

_source line 32 · 2026-05-22T03:36:42.452Z_

<details><summary>↩ Tool result · `toolu_013ZAeTC53cKCTuicCtnK7tK`</summary>

```text
Top-level type: &lt;class 'dict'>
Top-level keys: ['result']
Result type: &lt;class 'dict'>
Result keys: ['success', 'data', 'error', 'metadata']
  success: type=bool, value=True
  data: type=dict, keys=['experiments', 'count', 'total', 'baseline']
  error: type=NoneType, value=None
  metadata: type=dict, keys=['elapsed_seconds']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01N2zJUo1dnEGhGjTPYb6p2w",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "37ae5801-6a08-467d-bf92-1d6562c641b1"
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
  "task_id": "ad21c2477dd6123aa",
  "tool_use_id": "toolu_01UvN5LYeDV9iSrVapRBHaFQ",
  "description": "Reading ~/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-1-projects-cost-verify-agent-rl/54b94781-146b-4013-9381-11e3737077cb/tool-results/mcp-agent-ml-research-read_project_file-1779420982565.txt",
  "usage": {
    "total_tokens": 14921,
    "tool_uses": 1,
    "duration_ms": 6100
  },
  "last_tool_name": "Read",
  "uuid": "91a918ea-ecdb-42df-a67a-c5bd71780a32",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb"
}
```

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Read · `toolu_01T5AsBdGGoTPDPNxxxdsWLC`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-1-projects-cost-verify-agent-rl/54b94781-146b-4013-9381-11e3737077cb/tool-results/mcp-agent-ml-research-read_project_file-1779420982565.txt",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UvN5LYeDV9iSrVapRBHaFQ",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "a89f9742-e88b-4384-9616-774d106211a9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015hiP4z14MmByzxJbRVjBfc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6662,
      "cache_read_input_tokens": 8252,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6662,
        "ephemeral_1h_input_tokens": 0
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

_source line 35 · 2026-05-22T03:36:45.947Z_

<details><summary>↩ Tool result · reported error · `toolu_01T5AsBdGGoTPDPNxxxdsWLC`</summary>

```text
File content (48610 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UvN5LYeDV9iSrVapRBHaFQ",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "dd8656b4-6f78-47d9-9833-1c23716c92be",
  "tool_use_result": "Error: File content (48610 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
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
  "task_id": "a81374730ba0416fe",
  "tool_use_id": "toolu_01N2zJUo1dnEGhGjTPYb6p2w",
  "description": "Running Check experiments structure and count",
  "usage": {
    "total_tokens": 16386,
    "tool_uses": 2,
    "duration_ms": 14364
  },
  "last_tool_name": "Bash",
  "uuid": "4138d3b8-02f4-4e41-93c9-d829e058a316",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb"
}
```

---

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — Bash · `toolu_01BbURnRTCLjrYWxagCHz6PE`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-1-projects-cost-verify-agent-rl/54b94781-146b-4013-9381-11e3737077cb/tool-results/mcp-agent-ml-research-read_registry-1779420967332.txt') as f:\n    raw = json.load(f)\n\nresult = json.loads(raw['result'])\ndata = result['data']\nexperiments = data['experiments']\nprint('Total experiments:', len(experiments))\nprint('First experiment keys:', list(experiments[0].keys()) if experiments else 'empty')\nif experiments:\n    print('Sample exp_id:', experiments[0].get('exp_id'))\n\"\n",
  "description": "Check experiments structure and count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01N2zJUo1dnEGhGjTPYb6p2w",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "8e958660-5737-41df-892b-c77901c8611a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011wjz1JAx6aL81cmThjrtRy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1373,
      "cache_read_input_tokens": 14966,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1373,
        "ephemeral_1h_input_tokens": 0
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

_source line 38 · 2026-05-22T03:36:49.979Z_

<details><summary>↩ Tool result · reported error · `toolu_01BbURnRTCLjrYWxagCHz6PE`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 11, in &lt;module>
    print('First experiment keys:', list(experiments[0].keys()) if experiments else 'empty')
                                         ~~~~~~~~~~~^^^
KeyError: 0
Total experiments: 154
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01N2zJUo1dnEGhGjTPYb6p2w",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "0a2d45d6-79b7-4bb2-9c54-c16810acb2b2",
  "tool_use_result": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 11, in &lt;module>\n    print('First experiment keys:', list(experiments[0].keys()) if experiments else 'empty')\n                                         ~~~~~~~~~~~^^^\nKeyError: 0\nTotal experiments: 154"
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
  "task_id": "ad21c2477dd6123aa",
  "tool_use_id": "toolu_01UvN5LYeDV9iSrVapRBHaFQ",
  "description": "Searching for ScienceWorld|scienceworld|science_world|sw_",
  "usage": {
    "total_tokens": 15996,
    "tool_uses": 2,
    "duration_ms": 13855
  },
  "last_tool_name": "Grep",
  "uuid": "ac4cf748-eb07-40d5-8ff0-27a034938124",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb"
}
```

---

### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Grep · `toolu_01UmHzugsmGoUuEx2D1dY9Z1`</summary>

```json
{
  "pattern": "ScienceWorld|scienceworld|science_world|sw_",
  "path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-1-projects-cost-verify-agent-rl/54b94781-146b-4013-9381-11e3737077cb/tool-results/mcp-agent-ml-research-read_project_file-1779420982565.txt",
  "output_mode": "content",
  "-n": true,
  "head_limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UvN5LYeDV9iSrVapRBHaFQ",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "6b1a1972-a5e2-4899-b86e-897fe673cba0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JzHWmFz99j7JX2H5g1enSg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1075,
      "cache_read_input_tokens": 14914,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1075,
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

_source line 41 · 2026-05-22T03:36:53.438Z_

<details><summary>↩ Tool result · `toolu_01UmHzugsmGoUuEx2D1dY9Z1`</summary>

```text
1:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UvN5LYeDV9iSrVapRBHaFQ",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "7bcdd996-0c04-4a62-ad96-ebf83dd367be"
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
  "task_id": "ad21c2477dd6123aa",
  "tool_use_id": "toolu_01UvN5LYeDV9iSrVapRBHaFQ",
  "description": "Searching for Cell A|Cell C",
  "usage": {
    "total_tokens": 15997,
    "tool_uses": 3,
    "duration_ms": 15240
  },
  "last_tool_name": "Grep",
  "uuid": "a7443614-f218-4247-b72a-17e2d440f627",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb"
}
```

---

### Tool call

_source line 43_

<details open><summary>🔧 Tool call — Grep · `toolu_011tqX8wvdAUTwQ7NbZhR9yh`</summary>

```json
{
  "pattern": "Cell A|Cell C",
  "path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-1-projects-cost-verify-agent-rl/54b94781-146b-4013-9381-11e3737077cb/tool-results/mcp-agent-ml-research-read_project_file-1779420982565.txt",
  "output_mode": "content",
  "-n": true,
  "head_limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UvN5LYeDV9iSrVapRBHaFQ",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "574f1e84-6a63-41ef-a328-db6783c290b1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JzHWmFz99j7JX2H5g1enSg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1075,
      "cache_read_input_tokens": 14914,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1075,
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

_source line 44 · 2026-05-22T03:36:54.800Z_

<details><summary>↩ Tool result · `toolu_011tqX8wvdAUTwQ7NbZhR9yh`</summary>

```text
1:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UvN5LYeDV9iSrVapRBHaFQ",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "1a914370-5821-4c05-9f70-696b92ac1e80"
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
  "task_id": "a81374730ba0416fe",
  "tool_use_id": "toolu_01N2zJUo1dnEGhGjTPYb6p2w",
  "description": "Running Check experiments dict structure",
  "usage": {
    "total_tokens": 16820,
    "tool_uses": 3,
    "duration_ms": 20521
  },
  "last_tool_name": "Bash",
  "uuid": "a5fa7cf9-f007-4114-b93a-5d7cc79113d6",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb"
}
```

---

### Tool call

_source line 46_

<details open><summary>🔧 Tool call — Bash · `toolu_0162tZMmHqA1DnXYdJw5jfjo`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-1-projects-cost-verify-agent-rl/54b94781-146b-4013-9381-11e3737077cb/tool-results/mcp-agent-ml-research-read_registry-1779420967332.txt') as f:\n    raw = json.load(f)\n\nresult = json.loads(raw['result'])\ndata = result['data']\nexperiments = data['experiments']\nprint('Experiments type:', type(experiments))\nif isinstance(experiments, dict):\n    keys = list(experiments.keys())\n    print('First 3 keys:', keys[:3])\n    first_key = keys[0]\n    first_exp = experiments[first_key]\n    print('First exp type:', type(first_exp))\n    if isinstance(first_exp, dict):\n        print('First exp keys:', list(first_exp.keys()))\n\"\n",
  "description": "Check experiments dict structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01N2zJUo1dnEGhGjTPYb6p2w",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "6a96d2bd-3c06-499a-8235-c16339e03e24",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WAbjHPXrkWoGF68yo9n2Qs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 361,
      "cache_read_input_tokens": 16339,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 361,
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

_source line 47 · 2026-05-22T03:36:56.027Z_

<details><summary>↩ Tool result · `toolu_0162tZMmHqA1DnXYdJw5jfjo`</summary>

```text
Experiments type: &lt;class 'dict'>
First 3 keys: ['exp029_seed6_step15_ood', 'exp029_seed5_step10_ood', 'exp029_c_prime_resume_mt50_v2']
First exp type: &lt;class 'dict'>
First exp keys: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'hypothesis']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01N2zJUo1dnEGhGjTPYb6p2w",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "6e28c860-f3d5-4248-9175-0a5d22af7fb2"
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
  "task_id": "ad21c2477dd6123aa",
  "tool_use_id": "toolu_01UvN5LYeDV9iSrVapRBHaFQ",
  "description": "Reading ~/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-1-projects-cost-verify-agent-rl/54b94781-146b-4013-9381-11e3737077cb/tool-results/mcp-agent-ml-research-read_project_file-1779420982565.txt",
  "usage": {
    "total_tokens": 16523,
    "tool_uses": 4,
    "duration_ms": 20690
  },
  "last_tool_name": "Read",
  "uuid": "cc3aae34-ee02-44dd-9e36-6aabd2b75744",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb"
}
```

---

### Tool call

_source line 49_

<details open><summary>🔧 Tool call — Read · `toolu_01AJ97JKfLC5rWt4a3A8tCL4`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-1-projects-cost-verify-agent-rl/54b94781-146b-4013-9381-11e3737077cb/tool-results/mcp-agent-ml-research-read_project_file-1779420982565.txt",
  "limit": 1,
  "offset": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UvN5LYeDV9iSrVapRBHaFQ",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "36db4e4a-8734-46b3-aa79-76f03156f361",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XtX5LrqJTH4F8it7uDT1xN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 524,
      "cache_read_input_tokens": 15989,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 524,
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

_source line 50 · 2026-05-22T03:37:00.555Z_

<details><summary>↩ Tool result · reported error · `toolu_01AJ97JKfLC5rWt4a3A8tCL4`</summary>

```text
File content (48610 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UvN5LYeDV9iSrVapRBHaFQ",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "89511927-61a2-4804-aa6a-a77365b2986d",
  "tool_use_result": "Error: File content (48610 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
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
  "task_id": "a81374730ba0416fe",
  "tool_use_id": "toolu_01N2zJUo1dnEGhGjTPYb6p2w",
  "description": "Running Search for all ScienceWorld-related experiments and output full data",
  "usage": {
    "total_tokens": 17259,
    "tool_uses": 4,
    "duration_ms": 29146
  },
  "last_tool_name": "Bash",
  "uuid": "7264d5d3-c711-45ba-b054-8c83d4fe1bec",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb"
}
```

---

### Tool call

_source line 52_

<details open><summary>🔧 Tool call — Bash · `toolu_011o5ZH5H7ACpHcTSAUC6jGb`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json, re\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-1-projects-cost-verify-agent-rl/54b94781-146b-4013-9381-11e3737077cb/tool-results/mcp-agent-ml-research-read_registry-1779420967332.txt') as f:\n    raw = json.load(f)\n\nresult = json.loads(raw['result'])\nexperiments = result['data']['experiments']\n\n# Patterns to search for\npatterns = re.compile(r'scienceworld|science_world|science-world|sw_|_sw|ScienceWorld', re.IGNORECASE)\n\nmatching = {}\nfor exp_id, exp_data in experiments.items():\n    # Serialize the entire experiment to string and search\n    full_text = json.dumps(exp_data) + \" \" + exp_id\n    if patterns.search(full_text):\n        matching[exp_id] = exp_data\n\nprint(f\"Found {len(matching)} matching experiments out of {len(experiments)} total\\n\")\nprint(\"=\"*120)\n\nfor exp_id, exp_data in sorted(matching.items()):\n    print(f\"\\n{'='*120}\")\n    print(f\"EXP_ID: {exp_id}\")\n    print(f\"{'='*120}\")\n    print(json.dumps(exp_data, indent=2, ensure_ascii=False))\n\nPYEOF\n",
  "description": "Search for all ScienceWorld-related experiments and output full data",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01N2zJUo1dnEGhGjTPYb6p2w",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "102a1fbe-8947-4f4a-8d9a-59f3de6a418d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013k3DPJvo6KdphZRzwUYwef",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 437,
      "cache_read_input_tokens": 16700,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 437,
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

_source line 53 · 2026-05-22T03:37:04.664Z_

<details><summary>↩ Tool result · `toolu_011o5ZH5H7ACpHcTSAUC6jGb`</summary>

```text
Found 14 matching experiments out of 154 total

========================================================================================================================

========================================================================================================================
EXP_ID: gsweep_g050_h5_seed1
========================================================================================================================
{
  "status": "DONE",
  "retry_count": 2,
  "created_at": "2026-05-17T13:56:51.277Z",
  "updated_at": "2026-05-18T02:56:21.234Z",
  "hypothesis": "γ=0.5 with h=5 will show accelerated collapse compared to default γ=0.95, because γ^k decay compounds: early windows receive only γ^(N-1) ≈ 0.5^9 ≈ 0.2% of terminal return, making sign misattribution maximally severe.",
  "parent": "hsweep_h2_seed1",
  "reproduce": {
    "finished_at": "2026-05-18T02:55:47.955Z"
  },
  "extra": {
    "hook_events": [
      {
        "event": "on_complete",
        "action": "agent",
        "ts": "2026-05-17T14:42:45.029228+00:00"
      },
      {
        "event": "on_failed",
        "action": "agent",
        "ts": "2026-05-18T02:55:56.282433+00:00"
      }
    ],
    "previous_failure": {
      "conclusion": "failed",
      "metrics": {
        "training_steps_completed": 0,
        "wandb_run_id": null,
        "checkpoint_path": null,
        "log_path": "/root/runs/cost-verify-agent-rl/gsweep_g050_h5_seed1.log",
        "crash_reason": "AssertionError: duplicate template name in torch._inductor/select_algorithm.py — vLLM/PyTorch incompatibility during rollout module init",
        "crash_stage": "initialization (before any training step)",
        "collapse_onset_step": null,
        "total_training_steps": 0,
        "elapsed_hours": 0,
        "server": "westd-47453",
        "gpu": "cuda:2,3",
        "gamma": 0.5,
        "h": 5
      },
      "notes": "Infrastructure failure: experiment crashed during vLLM rollout module initialization with 'AssertionError: duplicate template name' in torch._inductor/select_algorithm.py. This is a vLLM/PyTorch version incompatibility on westd-47453. Zero training steps completed, no W&B data, no checkpoint. Hypothesis (γ=0.5 accelerates collapse vs γ=0.95) was never tested. Needs environment fix (likely vLLM or PyTorch version mismatch) before retry."
    }
  },
  "completed_at": "2026-05-17T14:44:36.785Z",
  "notes": "Director 批准 early kill (step 12/15)。Hypothesis 完全确认：γ=0.5 加速 collapse，从 step 1 起 train success 基本为 0%，val step 5/10 全零，KL step 8 spike 到 0.209。step 10 checkpoint 已保存。数据足够用于论文 gamma sweep figure。Watchdog 预期自动启动 g080。",
  "spec": {
    "command": "python train.py --config-name _alfworld_gamma_sweep_g050_h5 seed.train=10000 trainer.experiment_name=gsweep-g050-h5-seed1",
    "server": "westd-47453",
    "gpu": [
      "cuda:2",
      "cuda:3"
    ],
    "pid": "85798",
    "model_name": "Qwen3-1.7B",
    "seed": 10000,
    "data_path": "ALFWorld",
    "data_count": "134 train tasks",
    "log_path": "~/runs/cost-verify-agent-rl/gsweep_g050_h5_seed1.log",
    "env": "TORCH_COMPILE_DISABLE=1",
    "checkpoint_source": "Qwen3-1.7B base (not from parent checkpoint, parent field is for derivation tracking)",
    "eval_data": "ALFWorld val 32 tasks",
    "checkpoint_path": "/root/autodl-tmp/checkpoints/gsweep-g050-h5/global_step_10"
  },
  "metrics": {
    "current_step": "12/15",
    "train_success_collapsed_at": "step 1",
    "train_success_all_steps": "0-2.3% (effectively 0%)",
    "val_step0": {
      "success": 0.094
    },
    "val_step5": {
      "success": 0,
      "reward": 0
    },
    "val_step10": {
      "success": 0,
      "reward": 0,
      "response_length": 1412
    },
    "kl_sequence": [
      0.019,
      0.025,
      0.018,
      0.014,
      0.01,
      0.009,
      0.009,
      0.209,
      0.018
    ],
    "kl_spike_step8": 0.209,
    "checkpoint": "global_step_10",
    "eta": "~5h from 02:46 UTC",
    "status_note": "COMPLETELY COLLAPSED. Train success 0% from step 1. KL spike 20x at step 8. Val all zeros. Remaining 3 steps waste GPU. Recommend early kill."
  },
  "conclusion": "killed",
  "failure_reason": "process dead 5× with no sentinel/W&B — auto-resolved as failed"
}

========================================================================================================================
EXP_ID: gsweep_g080_h5_seed1
========================================================================================================================
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-17T13:56:53.634Z",
  "updated_at": "2026-05-18T09:35:23.404Z",
  "hypothesis": "γ=0.8 with h=5 represents an intermediate decay rate where early windows retain γ^9 ≈ 0.8^9 ≈ 13% of terminal return, potentially showing delayed but still present collapse compared to γ=0.95 (39%).",
  "parent": "hsweep_h2_seed1",
  "spec": {
    "command": "python train.py --config-name _alfworld_gamma_sweep_g080_h5 seed.train=10000 trainer.experiment_name=gsweep-g080-h5-seed1",
    "server": "westd-47453",
    "gpu": [
      "cuda:2",
      "cuda:3"
    ],
    "pid": 955007,
    "model_name": "Qwen3-1.7B",
    "seed": 10000,
    "data_path": "ALFWorld",
    "data_count": "134 train tasks",
    "log_path": "~/runs/cost-verify-agent-rl/gsweep_g080_h5_seed1.log",
    "env": "TORCH_COMPILE_DISABLE=1",
    "checkpoint_source": "Qwen3-1.7B base",
    "eval_data": "ALFWorld val 32 tasks"
  },
  "metrics": {
    "step5_val_success": "3.125%",
    "step5_entropy": 0.185,
    "subsequent_steps": "all 0%",
    "conclusion_note": "Complete collapse confirmed. γ=0.80 with h=5 shows catastrophic failure — killed early by Director as no new information expected. Supports hypothesis that lower gamma accelerates collapse."
  },
  "reproduce": {
    "finished_at": "2026-05-18T09:21:28.503Z"
  },
  "failure_reason": "process dead 5× with no sentinel/W&B — auto-resolved as failed",
  "conclusion": "negative",
  "completed_at": "2026-05-18T09:21:28.848Z",
  "extra": {
    "hook_events": [
      {
        "event": "on_failed",
        "action": "agent",
        "ts": "2026-05-18T09:21:35.022554+00:00"
      }
    ]
  }
}

========================================================================================================================
EXP_ID: gsweep_g100_h5_seed1
========================================================================================================================
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-17T13:56:58.033Z",
  "updated_at": "2026-05-18T17:36:39.529Z",
  "hypothesis": "γ=1.0 (no discount) tests whether collapse in h=5 is caused by sign misattribution from magnitude decay. If γ=1.0 also collapses, sign misattribution is not solely from discount-induced magnitude decay.",
  "parent": "gsweep_g095_h5_seed1",
  "spec": {
    "command": "python train.py --config-name _alfworld_gamma_sweep_g100_h5",
    "server": "westd-47453",
    "gpu": "2,3",
    "pid": "714093",
    "wandb_run_id": "da7701tk",
    "data_path": "/root/autodl-tmp/cost-verify-agent-rl/data/alfworld",
    "data_count": 3553,
    "model_name": "Qwen/Qwen2.5-3B",
    "seed": 10000,
    "checkpoint_source": "Qwen2.5-3B base",
    "eval_data": "ALFWorld val 32 tasks",
    "checkpoint_path": "/root/autodl-tmp/checkpoints/gsweep-g100-h5/",
    "log_path": "/root/autodl-tmp/cost-verify-agent-rl/logs/gsweep_g100_seed1.log"
  },
  "conclusion": "negative",
  "completed_at": "2026-05-18T17:35:40.356Z",
  "metrics": {
    "conclusion_reason": "collapsed, γ=1.0 also collapses confirming sign misattribution not solely from magnitude decay"
  }
}

========================================================================================================================
EXP_ID: scienceworld_grpo_cell_a
========================================================================================================================
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-20T11:24:49.171Z",
  "updated_at": "2026-05-20T13:54:57.116Z",
  "hypothesis": "ScienceWorld 环境下 step-independent GRPO (h=2) 也会出现 policy collapse，验证 ALFWorld 观察到的 collapse 是 step-independent credit assignment 的固有问题而非环境特异性",
  "parent": "scienceworld_sft",
  "spec": {
    "command": "cd /root/cost-verify-agent-rl/RAGEN && WANDB_PROJECT=cost-verify-agent-rl python train.py --config-name _scienceworld_cell_a_grpo",
    "server": "westd-47453",
    "gpu": "cuda:0,1",
    "pid": 759987,
    "wandb_run_id": "f1c4g6dk",
    "data_path": "ScienceWorldSG",
    "data_count": 30,
    "model_name": "Qwen3-1.7B (ScienceWorld SFT checkpoint)",
    "seed": 42,
    "checkpoint_source": "scienceworld_sft",
    "eval_data": "ScienceWorldSG 30 task types (dev split)",
    "checkpoint_path": "/root/autodl-tmp/checkpoints/scienceworld-cell-a/global_step_15",
    "log_path": "/root/cost-verify-agent-rl/RAGEN/wandb/run-20260520_204440-f1c4g6dk/files/output.log",
    "hyperparams": {
      "total_training_steps": 15,
      "context_window_mode": "step_independent",
      "step_independent_history_length": 2,
      "env_groups": 16,
      "group_size": 8,
      "ppo_mini_batch_size": 8,
      "ppo_max_token_len_per_gpu": 16384,
      "optimizer_offload": true,
      "lr": 1e-06,
      "n_gpus_per_node": 2
    },
    "notes": "ScienceWorld Cell A: step-independent h=2. Expected to show collapse, proving it generalizes beyond ALFWorld."
  },
  "conclusion": "negative",
  "metrics": {
    "steps_completed": 14,
    "success_rate": 0,
    "final_score_train": -100,
    "final_score_val": 1,
    "reward_mean_start": 0.6,
    "reward_mean_end": 0.1,
    "entropy_start": 0.283,
    "entropy_end": 0.52,
    "kl_start": 1.606,
    "kl_end": 0.03,
    "exit_mode": "abnormal (log truncated at step 15 start)",
    "note": "collapse confirmed - success rate 0% throughout, matches ALFWorld Cell A pattern"
  },
  "completed_at": "2026-05-20T13:54:57.117Z"
}

========================================================================================================================
EXP_ID: scienceworld_grpo_cell_c
========================================================================================================================
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-20T11:24:51.574Z",
  "updated_at": "2026-05-20T15:32:10.728Z",
  "hypothesis": "ScienceWorld 环境下 episode-level GRPO 能避免 collapse 并学到有效策略，验证 episode-level credit 作为 fix 的跨环境泛化性",
  "parent": "scienceworld_sft",
  "spec": {
    "command": "cd /root/cost-verify-agent-rl/RAGEN && WANDB_PROJECT=cost-verify-agent-rl python train.py --config-name _scienceworld_cell_c_grpo",
    "server": "westd-47453",
    "gpu": "cuda:2,3",
    "pid": 766820,
    "wandb_run_id": "sx7h864t",
    "data_path": "ScienceWorldSG",
    "data_count": 30,
    "model_name": "Qwen3-1.7B (ScienceWorld SFT checkpoint)",
    "seed": 42,
    "checkpoint_source": "scienceworld_sft",
    "eval_data": "ScienceWorldSG 30 task types (dev split)",
    "checkpoint_path": "/root/autodl-tmp/checkpoints/scienceworld_cell_c/",
    "log_path": "/root/runs/cost-verify-agent-rl/scienceworld_cell_c.log",
    "hyperparams": {
      "total_training_steps": 15,
      "context_window_mode": "full",
      "env_groups": 16,
      "group_size": 8,
      "ppo_mini_batch_size": 8,
      "ppo_max_token_len_per_gpu": 16384,
      "optimizer_offload": true,
      "lr": 1e-06,
      "n_gpus_per_node": 2
    },
    "notes": "ScienceWorld Cell C: episode-level full context. Expected to learn without collapse, proving fix generalizes."
  },
  "conclusion": "failed",
  "completed_at": "2026-05-20T15:32:04.012Z",
  "metrics": {
    "step_1_success": 0,
    "step_1_pass_at_8": 0,
    "step_1_score": 2.74,
    "step_1_final_score": 5.44,
    "step_1_action_valid": 0.44,
    "completed_steps": "1/15",
    "failure_reason": "ScienceWorld Java environment communication error: Exception while sending command"
  }
}

========================================================================================================================
EXP_ID: scienceworld_grpo_cell_c_v2
========================================================================================================================
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-20T15:41:04.991Z",
  "updated_at": "2026-05-20T18:23:54.294Z",
  "hypothesis": "ScienceWorld 环境下 episode-level GRPO 能避免 collapse 并学到有效策略，验证 episode-level credit 作为 fix 的跨环境泛化性（v2: 加固 JVM 通信——增大堆至 4g + py4j 断连自动重建 JVM + step 崩溃优雅降级）",
  "parent": "scienceworld_grpo_cell_c",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/cost-verify-agent-rl/RAGEN && WANDB_PROJECT=cost-verify-agent-rl JAVA_TOOL_OPTIONS='-Xmx4g' python train.py --config-name _scienceworld_cell_c_grpo\"",
    "server": "westd-47453",
    "gpu": [
      "cuda:2",
      "cuda:3"
    ],
    "pid": "920065",
    "log_path": "~/runs/cost-verify-agent-rl/scienceworld_grpo_cell_c_v2.log",
    "submitted_at": "2026-05-20T15:41:18.991Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "gpu_ids": [
      "cuda:2",
      "cuda:3"
    ],
    "data_path": "scienceworld (30 tasks)",
    "data_count": 128,
    "model_name": "qwen3_scienceworld_sft",
    "seed": 10000,
    "checkpoint_source": "qwen3_scienceworld_sft",
    "eval_data": "scienceworld dev split",
    "wall_clock_seconds": 9746.5,
    "gpu_hours": 5.41
  },
  "conclusion": "failed",
  "completed_at": "2026-05-20T18:23:45.449Z",
  "metrics": {
    "note": "Stalled at step 2 due to disk full (99%), Ray object spilling blocked. GPU 0% util for >1h50min. Killed and restarted as v3."
  }
}

========================================================================================================================
EXP_ID: scienceworld_grpo_cell_c_v3
========================================================================================================================
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-20T18:23:30.854Z",
  "updated_at": "2026-05-21T02:44:56.368Z",
  "hypothesis": "ScienceWorld 环境下 episode-level GRPO 能避免 collapse 并学到有效策略，验证 episode-level credit 作为 fix 的跨环境泛化性（v3: 磁盘清理后重启）",
  "parent": "scienceworld_grpo_cell_c_v2",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/cost-verify-agent-rl/RAGEN && WANDB_PROJECT=cost-verify-agent-rl python train.py --config-name _scienceworld_cell_c_grpo\"",
    "server": "westd-47453",
    "gpu": [
      "cuda:2",
      "cuda:3"
    ],
    "pid": "88226",
    "log_path": "~/runs/cost-verify-agent-rl/scienceworld_grpo_cell_c_v3.log",
    "submitted_at": "2026-05-20T18:23:38.661Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "ScienceWorldSG (30 task types)",
    "data_count": 128,
    "model_name": "Qwen3-1.7B (ScienceWorld SFT checkpoint)",
    "seed": 10000,
    "checkpoint_source": "qwen3_scienceworld_sft",
    "eval_data": "ScienceWorldSG 30 task types (dev split)",
    "checkpoint_path": "N/A (negative, no useful checkpoint)",
    "wall_clock_seconds": 30077.7,
    "gpu_hours": 16.71
  },
  "conclusion": "negative",
  "notes": "D109 止损：step 3 success=0%, action_is_valid=9.4%(<20% 阈值), score 从 2.71 降至 0.96, reward 从 0.5 降至 0.153。趋势恶化，释放 GPU。",
  "completed_at": "2026-05-21T02:44:56.370Z"
}

========================================================================================================================
EXP_ID: scienceworld_info_loss_full
========================================================================================================================
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-20T14:21:15.269Z",
  "updated_at": "2026-05-20T14:33:44.987Z",
  "hypothesis": "ScienceWorld SFT model with full context at T=0 achieves significantly higher success rate than h=2, quantifying information loss (Mechanism 1) in a second environment beyond ALFWorld",
  "parent": "8b_det_eval_full",
  "spec": {
    "command": "python3 eval_scienceworld_info_loss.py --temperature 0 --history_length -1 --max_variations 3 --tensor_parallel_size 2",
    "server": "westd-47453",
    "data_path": "ScienceWorldSG dev split",
    "data_count": "~90 episodes",
    "model_name": "qwen3_scienceworld_sft",
    "seed": 0,
    "checkpoint_source": "/root/autodl-tmp/checkpoints/qwen3_scienceworld_sft/huggingface",
    "eval_data": "ScienceWorldSG dev, max_variations=3"
  },
  "conclusion": "failed",
  "completed_at": "2026-05-20T14:33:44.987Z"
}

========================================================================================================================
EXP_ID: scienceworld_info_loss_h2
========================================================================================================================
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-20T14:21:16.640Z",
  "updated_at": "2026-05-20T14:36:43.490Z",
  "hypothesis": "ScienceWorld SFT model with h=2 sliding window at T=0 shows degraded performance vs full context, confirming information loss generalizes beyond ALFWorld",
  "parent": "8b_det_eval_h2",
  "conclusion": "killed",
  "completed_at": "2026-05-20T14:36:43.490Z"
}

========================================================================================================================
EXP_ID: scienceworld_sft
========================================================================================================================
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-19T14:35:00.255Z",
  "updated_at": "2026-05-19T17:50:12.565Z",
  "hypothesis": "ScienceWorld 1.7B SFT 训练，为后续 GRPO 实验提供 base checkpoint。验证 SFT 训练 pipeline 可泛化到第二个交互环境（ALFWorld 之外），支撑跨环境 RL 训练失败机制对比（Cell A vs Cell C）。数据：3592 train / 1796 val expert trajectories。",
  "spec": {
    "command": "bash /root/cost-verify-agent-rl/RAGEN/scripts/run_scienceworld_sft.sh",
    "server": "westd-47453",
    "gpu": [
      "cuda:0",
      "cuda:1",
      "cuda:2",
      "cuda:3"
    ],
    "pid": "120838",
    "data_path": "/root/autodl-tmp/expert_sft/scienceworld_sft_train.jsonl",
    "data_count": 3592,
    "model_name": "Qwen3-1.7B",
    "seed": 42,
    "log_path": "/root/autodl-tmp/wandb/",
    "checkpoint_path": "/root/autodl-tmp/checkpoints/scienceworld_sft/",
    "hyperparams": {
      "lr": "5e-6",
      "epochs": 2,
      "batch_size": 16,
      "max_length": 16384,
      "fsdp": "fsdp2"
    },
    "wandb_run_id": "dqoxg94e",
    "notes": "原始 wrapper PID 120827 已退出，实际 torchrun PID 120838，workers 120904-120907"
  },
  "conclusion": "success",
  "metrics": {
    "train_loss_final": 0.00318,
    "val_loss_final": 0.01098,
    "total_steps": 448,
    "epochs": 2,
    "total_train_time_s": 9319.4,
    "checkpoint": "global_step_448"
  },
  "completed_at": "2026-05-19T17:50:12.566Z"
}

========================================================================================================================
EXP_ID: scienceworld_sft_eval
========================================================================================================================
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-19T18:11:10.597Z",
  "updated_at": "2026-05-19T18:46:33.866Z",
  "hypothesis": "Evaluate ScienceWorld SFT checkpoint on dev split (1796 episodes, 30 task types). Establishes SFT baseline success rate for ScienceWorld before GRPO experiments.",
  "parent": "scienceworld_sft",
  "spec": {
    "command": "python /root/cost-verify-agent-rl/eval_scienceworld.py --temperature 0.4",
    "server": "bjb1-17606",
    "gpu": [
      "cuda:0",
      "cuda:1"
    ],
    "pid": "183712",
    "data_path": "scienceworld dev split",
    "data_count": 1796,
    "model_name": "Qwen3-1.7B (ScienceWorld SFT)",
    "seed": 42,
    "log_path": "/tmp/eval_scienceworld.log",
    "checkpoint_source": "scienceworld_sft/global_step_448",
    "eval_data": "ScienceWorld dev split, 1796 episodes, 30 task types"
  },
  "conclusion": "killed",
  "completed_at": "2026-05-19T18:46:33.866Z"
}

========================================================================================================================
EXP_ID: scienceworld_sft_eval_v2
========================================================================================================================
{
  "status": "DONE",
  "retry_count": 1,
  "created_at": "2026-05-19T18:50:45.230Z",
  "updated_at": "2026-05-20T14:15:37.390Z",
  "hypothesis": "SFT-trained model on ScienceWorld can achieve meaningful task completion rates across diverse science tasks, establishing a baseline for subsequent RL fine-tuning comparison.",
  "parent": "scienceworld_sft_eval",
  "reproduce": {
    "finished_at": "2026-05-19T23:59:52.638Z"
  },
  "failure_reason": null,
  "completed_at": "2026-05-19T23:59:54.217Z",
  "extra": {
    "hook_events": [
      {
        "event": "on_failed",
        "action": "agent",
        "ts": "2026-05-19T23:59:57.500015+00:00"
      }
    ],
    "previous_failure": {
      "conclusion": "failed",
      "metrics": {
        "episodes_completed": 409,
        "episodes_total": 1796,
        "progress_pct": 22.8,
        "success_count": 158,
        "success_rate": 0.386,
        "speed_ep_per_min": 1.56
      }
    }
  },
  "spec": {
    "command": "python /root/cost-verify-agent-rl/eval_scienceworld.py --temperature 0.4 --resume --episode_timeout 300",
    "server": "bjb1-17606",
    "gpu": [
      "cuda:0",
      "cuda:1"
    ],
    "pid": "195853",
    "data_path": "scienceworld dev split",
    "data_count": 1796,
    "model_name": "Qwen3-1.7B (ScienceWorld SFT)",
    "seed": 42,
    "log_path": "/tmp/eval_scienceworld_v2_resumed.log",
    "checkpoint_source": "scienceworld_sft/global_step_448",
    "eval_data": "ScienceWorld dev split, 1796 episodes, 30 task types",
    "checkpoint_path": "N/A (eval only)"
  },
  "metrics": {
    "total_episodes": 1796,
    "success_count": 540,
    "overall_success_rate": 0.301,
    "timeouts": 0,
    "errors": 0,
    "avg_score": 20.9,
    "avg_steps_per_episode": 28.7,
    "total_time_seconds": 51462,
    "split": "dev",
    "temperature": 0.4,
    "per_task_type": {
      "boil": {
        "n": 7,
        "succ": 0,
        "rate": 0
      },
      "change-the-state-of-matter-of": {
        "n": 7,
        "succ": 1,
        "rate": 0.143
      },
      "chemistry-mix": {
        "n": 8,
        "succ": 0,
        "rate": 0
      },
      "chemistry-mix-paint-secondary-color": {
        "n": 9,
        "succ": 2,
        "rate": 0.222
      },
      "chemistry-mix-paint-tertiary-color": {
        "n": 9,
        "succ": 0,
        "rate": 0
      },
      "find-animal": {
        "n": 75,
        "succ": 37,
        "rate": 0.493
      },
      "find-living-thing": {
        "n": 75,
        "succ": 49,
        "rate": 0.653
      },
      "find-non-living-thing": {
        "n": 75,
        "succ": 58,
        "rate": 0.773
      },
      "find-plant": {
        "n": 75,
        "succ": 9,
        "rate": 0.12
      },
      "freeze": {
        "n": 7,
        "succ": 0,
        "rate": 0
      },
      "grow-fruit": {
        "n": 31,
        "succ": 2,
        "rate": 0.065
      },
      "grow-plant": {
        "n": 31,
        "succ": 0,
        "rate": 0
      },
      "identify-life-stages-1": {
        "n": 3,
        "succ": 0,
        "rate": 0
      },
      "identify-life-stages-2": {
        "n": 2,
        "succ": 0,
        "rate": 0
      },
      "inclined-plane-determine-angle": {
        "n": 42,
        "succ": 7,
        "rate": 0.167
      },
      "inclined-plane-friction-named-surfaces": {
        "n": 346,
        "succ": 83,
        "rate": 0.24
      },
      "inclined-plane-friction-unnamed-surfaces": {
        "n": 40,
        "succ": 10,
        "rate": 0.25
      },
      "lifespan-longest-lived": {
        "n": 31,
        "succ": 28,
        "rate": 0.903
      },
      "lifespan-longest-lived-then-shortest-lived": {
        "n": 31,
        "succ": 28,
        "rate": 0.903
      },
      "lifespan-shortest-lived": {
        "n": 31,
        "succ": 21,
        "rate": 0.677
      },
      "measure-melting-point-known-substance": {
        "n": 109,
        "succ": 25,
        "rate": 0.229
      },
      "measure-melting-point-unknown-substance": {
        "n": 75,
        "succ": 27,
        "rate": 0.36
      },
      "melt": {
        "n": 7,
        "succ": 1,
        "rate": 0.143
      },
      "mendelian-genetics-known-plant": {
        "n": 30,
        "succ": 8,
        "rate": 0.267
      },
      "mendelian-genetics-unknown-plant": {
        "n": 120,
        "succ": 35,
        "rate": 0.292
      },
      "power-component": {
        "n": 5,
        "succ": 3,
        "rate": 0.6
      },
      "power-component-renewable-vs-nonrenewable-energy": {
        "n": 5,
        "succ": 0,
        "rate": 0
      },
      "test-conductivity": {
        "n": 225,
        "succ": 35,
        "rate": 0.156
      },
      "test-conductivity-of-unknown-substances": {
        "n": 150,
        "succ": 44,
        "rate": 0.293
      },
      "use-thermometer": {
        "n": 135,
        "succ": 27,
        "rate": 0.2
      }
    },
    "results_json_path": "/root/autodl-tmp/checkpoints/scienceworld_sft/eval_results_dev_v2.json"
  },
  "conclusion": "success"
}

========================================================================================================================
EXP_ID: sw_info_loss_bjb1
========================================================================================================================
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-20T16:38:54.097Z",
  "updated_at": "2026-05-20T19:10:24.938Z",
  "hypothesis": "ScienceWorld SFT model under h=2 windowing shows significant performance degradation vs full context (T=0 deterministic), quantifying information loss (M1) cross-environment on bjb1",
  "parent": "scienceworld_sft_eval_v2",
  "spec": {
    "command": "python eval_scienceworld_info_loss.py --checkpoint /root/autodl-tmp/checkpoints/scienceworld_sft/huggingface --history_length {-1,2} --temperature 0 --max_variations 3 --tensor_parallel_size 2",
    "server": "bjb1-17606",
    "gpu": [
      "cuda:0",
      "cuda:1"
    ],
    "pid": "229078",
    "log_path": "~/runs/cost-verify-agent-rl/sw_info_loss_bjb1.log",
    "submitted_at": "2026-05-20T16:39:02.613Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "scienceworld dev split",
    "data_count": "30 task types x 3 variations = 90 episodes per condition",
    "model_name": "qwen3_scienceworld_sft",
    "seed": "deterministic (T=0)",
    "checkpoint_source": "/root/autodl-tmp/checkpoints/scienceworld_sft/huggingface",
    "eval_data": "scienceworld dev split, 3 variations per task",
    "checkpoint_path": "N/A (eval only)",
    "wall_clock_seconds": 9082.3,
    "gpu_hours": 5.05
  },
  "reproduce": {
    "finished_at": "2026-05-20T19:07:34.749Z"
  },
  "extra": {
    "hook_events": [
      {
        "event": "on_complete",
        "action": "agent",
        "ts": "2026-05-20T19:07:38.508523+00:00"
      }
    ]
  },
  "metrics": {
    "full_context_success": 0.348,
    "h2_success": 0.045,
    "info_loss_delta_pp": 30.3,
    "full_episodes": 89,
    "h2_episodes": 89,
    "full_avg_score": 26.7,
    "h2_avg_score": 17.4,
    "temperature": 0,
    "notable": "find-animal/find-living-thing/lifespan-longest+shortest: 100% full → 0% h=2"
  },
  "conclusion": "success",
  "completed_at": "2026-05-20T19:10:24.938Z"
}

========================================================================================================================
EXP_ID: sw_info_loss_full_v2
========================================================================================================================
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-20T14:34:18.334Z",
  "updated_at": "2026-05-20T14:36:34.122Z",
  "hypothesis": "ScienceWorld SFT model with full context at T=0 achieves significantly higher success rate than h=2, quantifying information loss (Mechanism 1) in a second environment beyond ALFWorld",
  "parent": "scienceworld_sft_eval_v2",
  "spec": {
    "command": "python eval_scienceworld_info_loss.py --checkpoint qwen3_scienceworld_sft --temperature 0 --history_length -1 --tensor_parallel_size 2 --max_model_len 16384",
    "server": "westd-47453",
    "data_path": "ScienceWorldSG dev split",
    "data_count": "89 episodes",
    "model_name": "qwen3_scienceworld_sft",
    "seed": 0,
    "checkpoint_source": "/root/autodl-tmp/checkpoints/qwen3_scienceworld_sft/huggingface",
    "eval_data": "ScienceWorldSG dev, max_variations=3, T=0, full context",
    "gpu": "cuda:0,1",
    "pid": 875971
  },
  "conclusion": "failed",
  "completed_at": "2026-05-20T14:36:34.123Z"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01N2zJUo1dnEGhGjTPYb6p2w",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "fc47b157-85c7-4b05-af9c-b68e8f73a3d6"
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
  "task_id": "ad21c2477dd6123aa",
  "tool_use_id": "toolu_01UvN5LYeDV9iSrVapRBHaFQ",
  "description": "Running Parse JSON and extract YAML content to temp file",
  "usage": {
    "total_tokens": 16794,
    "tool_uses": 5,
    "duration_ms": 27189
  },
  "last_tool_name": "Bash",
  "uuid": "bdca1c27-cb8a-49d1-920f-d53993210c1f",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb"
}
```

---

### Tool call

_source line 55_

<details open><summary>🔧 Tool call — Bash · `toolu_01AV2todD2NfH4A9WyRxHS61`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-1-projects-cost-verify-agent-rl/54b94781-146b-4013-9381-11e3737077cb/tool-results && python3 -c \"\nimport json\n\nwith open('mcp-agent-ml-research-read_project_file-1779420982565.txt', 'r') as f:\n    data = json.load(f)\n\n# The result field contains the YAML as a string\nyaml_content = data['result']\n\n# Write YAML to a temp file for easier processing\nwith open('/tmp/decisions_yaml.txt', 'w') as f:\n    f.write(yaml_content)\n\nprint(f'YAML content length: {len(yaml_content)} chars')\nprint(f'First 200 chars: {yaml_content[:200]}')\n\"\n",
  "description": "Parse JSON and extract YAML content to temp file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UvN5LYeDV9iSrVapRBHaFQ",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "a7feafb6-df59-4a85-8aa2-651b6c6d208b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RYR59iHnnioJUk7EEd73bS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 269,
      "cache_read_input_tokens": 16513,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 269,
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

_source line 56 · 2026-05-22T03:37:06.818Z_

<details><summary>↩ Tool result · `toolu_01AV2todD2NfH4A9WyRxHS61`</summary>

```text
YAML content length: 94350 chars
First 200 chars: {"success": true, "data": {"path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/decisions.yaml", "content": "_next_id: 121\ndecisions:\n- id: D001\n  date: 2026-05-13
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UvN5LYeDV9iSrVapRBHaFQ",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "d2829c56-af70-4f2a-a446-d58b940ba31b"
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
  "task_id": "ad21c2477dd6123aa",
  "tool_use_id": "toolu_01UvN5LYeDV9iSrVapRBHaFQ",
  "description": "Running Extract nested YAML content to temp file",
  "usage": {
    "total_tokens": 17240,
    "tool_uses": 6,
    "duration_ms": 32596
  },
  "last_tool_name": "Bash",
  "uuid": "b7d39eb4-3f3f-4e1c-856f-cef6ad369f6d",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb"
}
```

---

### Tool call

_source line 58_

<details open><summary>🔧 Tool call — Bash · `toolu_01JHxvSXJwsF2s1paCj6mq7U`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-1-projects-cost-verify-agent-rl/54b94781-146b-4013-9381-11e3737077cb/tool-results/mcp-agent-ml-research-read_project_file-1779420982565.txt', 'r') as f:\n    data = json.load(f)\n\ninner = json.loads(data['result'])\nyaml_content = inner['data']['content']\n\nwith open('/tmp/decisions_yaml.txt', 'w') as f:\n    f.write(yaml_content)\n\nprint(f'YAML content length: {len(yaml_content)} chars')\nprint(f'Total lines: {yaml_content.count(chr(10))}')\n\"\n",
  "description": "Extract nested YAML content to temp file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UvN5LYeDV9iSrVapRBHaFQ",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "8fc04824-b124-44f2-bd79-e00055016d7e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BSxdpxGNUGdftGwR3XUBZ3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 444,
      "cache_read_input_tokens": 16782,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 444,
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

_source line 59 · 2026-05-22T03:37:12.227Z_

<details><summary>↩ Tool result · `toolu_01JHxvSXJwsF2s1paCj6mq7U`</summary>

```text
YAML content length: 91759 chars
Total lines: 2228
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UvN5LYeDV9iSrVapRBHaFQ",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "3e647c07-7dbd-41e0-a8f1-1007946f87ba"
}
```

</details>

---

### System

_source line 60_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad21c2477dd6123aa",
  "tool_use_id": "toolu_01UvN5LYeDV9iSrVapRBHaFQ",
  "description": "Running Find all lines matching ScienceWorld-related patterns",
  "usage": {
    "total_tokens": 17690,
    "tool_uses": 7,
    "duration_ms": 39525
  },
  "last_tool_name": "Bash",
  "uuid": "fe70b910-3c3c-4441-99aa-a5aeb2142158",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb"
}
```

---

### Tool call

_source line 61_

<details open><summary>🔧 Tool call — Bash · `toolu_013RuuNns9qFV9QoABiA8Mv6`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport re\n\nwith open('/tmp/decisions_yaml.txt', 'r') as f:\n    lines = f.readlines()\n\n# Search patterns\npatterns = [\n    re.compile(r'ScienceWorld', re.IGNORECASE),\n    re.compile(r'science_world', re.IGNORECASE),\n    re.compile(r'sw_'),\n    re.compile(r'Cell A[^-a-zA-Z]|Cell C[^-a-zA-Z]|\"Cell A\"|\"Cell C\"'),\n]\n\n# Find all line numbers that match\nmatching_lines = set()\nfor i, line in enumerate(lines):\n    for p in patterns:\n        if p.search(line):\n            matching_lines.add(i)\n\nprint(f\"Total matching lines: {len(matching_lines)}\")\nprint(f\"Line numbers: {sorted(matching_lines)}\")\nPYEOF\n",
  "description": "Find all lines matching ScienceWorld-related patterns"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UvN5LYeDV9iSrVapRBHaFQ",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "1c3ef1dc-0e7a-4c5f-81b0-d6559510d984",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019bdEZhmQwkzNnAujrM9dER",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 448,
      "cache_read_input_tokens": 17226,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 448,
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

_source line 62 · 2026-05-22T03:37:19.209Z_

<details><summary>↩ Tool result · `toolu_013RuuNns9qFV9QoABiA8Mv6`</summary>

```text
Total matching lines: 77
Line numbers: [1228, 1242, 1271, 1272, 1283, 1289, 1298, 1300, 1333, 1339, 1340, 1345, 1346, 1425, 1476, 1477, 1480, 1493, 1495, 1496, 1497, 1527, 1562, 1564, 1567, 1637, 1639, 1640, 1641, 1647, 1655, 1681, 1684, 1709, 1727, 1729, 1733, 1734, 1744, 1745, 1749, 1750, 1751, 1765, 1779, 1803, 1845, 1860, 1871, 1891, 1892, 1893, 1895, 1900, 1903, 1910, 1912, 1913, 1914, 1917, 1920, 1927, 1928, 1929, 1931, 1934, 1937, 1946, 1949, 1951, 1959, 1967, 1968, 1973, 2212, 2215, 2216]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UvN5LYeDV9iSrVapRBHaFQ",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "62ddb12a-8de3-4936-83de-5ccba26ce64a"
}
```

</details>

---

### System

_source line 63_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a81374730ba0416fe",
  "tool_use_id": "toolu_01N2zJUo1dnEGhGjTPYb6p2w",
  "description": "Running Check which patterns matched for gamma sweep experiments (likely false positives)",
  "usage": {
    "total_tokens": 28372,
    "tool_uses": 5,
    "duration_ms": 47974
  },
  "last_tool_name": "Bash",
  "uuid": "97cf7013-387f-47a0-96a0-9acbe15d1446",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb"
}
```

---

### Tool call

_source line 64_

<details open><summary>🔧 Tool call — Bash · `toolu_01UkXdxsmZSgtRbWDbWTH3Va`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json, re\n\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-1-projects-cost-verify-agent-rl/54b94781-146b-4013-9381-11e3737077cb/tool-results/mcp-agent-ml-research-read_registry-1779420967332.txt') as f:\n    raw = json.load(f)\n\nresult = json.loads(raw['result'])\nexperiments = result['data']['experiments']\n\n# Check which pattern matched for the gamma sweep experiments\nfor exp_id in ['gsweep_g050_h5_seed1', 'gsweep_g080_h5_seed1', 'gsweep_g100_h5_seed1']:\n    full_text = json.dumps(experiments[exp_id]) + \" \" + exp_id\n    patterns = [\n        ('scienceworld', re.compile(r'scienceworld', re.IGNORECASE)),\n        ('science_world', re.compile(r'science_world', re.IGNORECASE)),\n        ('science-world', re.compile(r'science-world', re.IGNORECASE)),\n        ('sw_', re.compile(r'sw_')),\n        ('_sw', re.compile(r'_sw')),\n        ('ScienceWorld', re.compile(r'ScienceWorld')),\n    ]\n    for name, pat in patterns:\n        matches = pat.findall(full_text)\n        if matches:\n            # Find context\n            for m in pat.finditer(full_text):\n                start = max(0, m.start()-30)\n                end = min(len(full_text), m.end()+30)\n                print(f\"  {exp_id} matched '{name}': ...{full_text[start:end]}...\")\nPYEOF\n",
  "description": "Check which patterns matched for gamma sweep experiments (likely false positives)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01N2zJUo1dnEGhGjTPYb6p2w",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "b84f5b98-97e7-4d29-869e-e1bce978c5d4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gp6G3pFhKBYMoGZGAjb9Az",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11111,
      "cache_read_input_tokens": 17137,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11111,
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

_source line 65 · 2026-05-22T03:37:23.507Z_

<details><summary>↩ Tool result · `toolu_01UkXdxsmZSgtRbWDbWTH3Va`</summary>

```text
  gsweep_g050_h5_seed1 matched '_sw': ... --config-name _alfworld_gamma_sweep_g050_h5 seed.train=10000 t...
  gsweep_g080_h5_seed1 matched '_sw': ... --config-name _alfworld_gamma_sweep_g080_h5 seed.train=10000 t...
  gsweep_g100_h5_seed1 matched '_sw': ... --config-name _alfworld_gamma_sweep_g100_h5", "server": "westd...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01N2zJUo1dnEGhGjTPYb6p2w",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "d44ddc21-aaee-4229-8ca2-638f1c225c20"
}
```

</details>

---

### System

_source line 66_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad21c2477dd6123aa",
  "tool_use_id": "toolu_01UvN5LYeDV9iSrVapRBHaFQ",
  "description": "Running Extract complete decision blocks containing ScienceWorld references",
  "usage": {
    "total_tokens": 18348,
    "tool_uses": 8,
    "duration_ms": 55996
  },
  "last_tool_name": "Bash",
  "uuid": "8c77dfb4-fb55-4eb4-8fef-b15452511e1e",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb"
}
```

---

### Tool call

_source line 67_

<details open><summary>🔧 Tool call — Bash · `toolu_012ugacEHsvD72bsvqgvaoDQ`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport re\n\nwith open('/tmp/decisions_yaml.txt', 'r') as f:\n    lines = f.readlines()\n\n# Search patterns\npatterns = [\n    re.compile(r'ScienceWorld', re.IGNORECASE),\n    re.compile(r'science_world', re.IGNORECASE),\n    re.compile(r'sw_'),\n    re.compile(r'Cell A(?![a-zA-Z-])|Cell C(?![a-zA-Z-])'),\n]\n\n# Find all line numbers that match\nmatching_lines = set()\nfor i, line in enumerate(lines):\n    for p in patterns:\n        if p.search(line):\n            matching_lines.add(i)\n\n# Find decision block boundaries (lines starting with \"- id: D\")\ndecision_starts = []\nfor i, line in enumerate(lines):\n    if re.match(r'^- id: D\\d+', line):\n        decision_starts.append(i)\n\n# Also find the header line\nheader_end = 0\nfor i, line in enumerate(lines):\n    if line.strip().startswith('decisions:'):\n        header_end = i + 1\n        break\n\n# For each matching line, find which decision block it belongs to\nmatching_decisions = set()\nfor ml in matching_lines:\n    # Find the decision start that is <= ml\n    best = None\n    for ds in decision_starts:\n        if ds <= ml:\n            best = ds\n        else:\n            break\n    if best is not None:\n        matching_decisions.add(best)\n\n# Extract each matching decision block\nprint(f\"Found {len(matching_decisions)} decision blocks containing ScienceWorld-related content\\n\")\nprint(\"=\" * 80)\n\nfor ds in sorted(matching_decisions):\n    # Find the end of this block (next decision start or EOF)\n    end = len(lines)\n    for next_ds in decision_starts:\n        if next_ds > ds:\n            end = next_ds\n            break\n    \n    block = ''.join(lines[ds:end])\n    print(f\"\\n[Lines {ds+1}-{end}]\")\n    print(block)\n    print(\"=\" * 80)\n\nPYEOF\n",
  "description": "Extract complete decision blocks containing ScienceWorld references",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UvN5LYeDV9iSrVapRBHaFQ",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "8b4e27ec-afb3-4328-8aaf-f8fb0c53a220",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M72Wdi5PjXwkbpnqNddYAB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 654,
      "cache_read_input_tokens": 17674,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 654,
        "ephemeral_1h_input_tokens": 0
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

_source line 68 · 2026-05-22T03:37:35.631Z_

<details><summary>↩ Tool result · `toolu_012ugacEHsvD72bsvqgvaoDQ`</summary>

```text
&lt;persisted-output>
Output too large (29.9KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-1-projects-cost-verify-agent-rl/54b94781-146b-4013-9381-11e3737077cb/tool-results/blomixe5q.txt

Preview (first 2KB):
Found 28 decision blocks containing ScienceWorld-related content

================================================================================

[Lines 1222-1246]
- id: D068
  date: 2026-05-18 03:52 UTC
  summary: 'exp029 OOD reeval: 23.88% on 134 tasks. Information loss preliminary estimate
    17.9pp, action_is_valid insight confirms mechanism'
  rationale: 'exp029 step 15 on AlfworldOOD 134 tasks: success=23.88% (vs 28.1% on
    in-dist 32 tasks, -4pp as expected). Preliminary decomposition on unified OOD
    set: information loss (B→C) = 23.88% - 5.97% = 17.9pp. Sign misattribution (A→B)
    still missing Cell A OOD data (hsweep_h2 reeval pending). Key insight: action_is_valid
    nearly identical between factorial (57.65%) and exp029 (56.84%) despite 18pp success
    gap — full context advantage is in decision quality not action legality, supporting
    information loss mechanism narrative. Caveat: factorial only at step 5 (step mismatch)
    and KL inflating (0.24→1.77), final decomposition needs factorial step 15.'
  related_experiments:
  - exp_id: exp029_episode_level
    role: primary
    result: 23.88% OOD success
  - exp_id: factorial_h2_episodeadv_seed1
    role: comparison
    result: 5.97% OOD at step 5, KL inflating
  - exp_id: hsweep_h2_seed2
    role: pending
    result: OOD reeval needed for Cell A
  depends_on:
  - D066
  - D067

================================================================================

[Lines 1268-1294]
- id: D070
  date: 2026-05-18 04:58 UTC
  summary: '3-cell decomposition: information loss 89% (17.9pp) >> sign misattribution
    11% (2.2pp). Narrative rebalance needed.'
  rationale: 'OOD 134 tasks unified decomposition: Cell A (step-indep + step-level)
    3.73%, Cell B (step-indep + episode-level) 5.97%, Cell C (full context + episode-level)
    23.88%. Sign misattribution effect (A→B) = 2.24pp; information loss effect (B→C)
    = 17.91pp. Ratio ~1:8. Paper cannot claim sign misattribution as primary driver
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UvN5LYeDV9iSrVapRBHaFQ",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "f6ae513c-f664-4fee-be41-516f6b9bbbf7"
}
```

</details>

---

### System

_source line 69_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad21c2477dd6123aa",
  "tool_use_id": "toolu_01UvN5LYeDV9iSrVapRBHaFQ",
  "description": "Reading ~/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-1-projects-cost-verify-agent-rl/54b94781-146b-4013-9381-11e3737077cb/tool-results/blomixe5q.txt",
  "usage": {
    "total_tokens": 19872,
    "tool_uses": 9,
    "duration_ms": 61651
  },
  "last_tool_name": "Read",
  "uuid": "f1532372-5a36-49df-be47-85b111b394d4",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb"
}
```

---

### Tool call

_source line 70_

<details open><summary>🔧 Tool call — Read · `toolu_011SrrP8BMVY9XxXdQUgL3mL`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-1-projects-cost-verify-agent-rl/54b94781-146b-4013-9381-11e3737077cb/tool-results/blomixe5q.txt",
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
  "parent_tool_use_id": "toolu_01UvN5LYeDV9iSrVapRBHaFQ",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "35c01c64-5c20-4eb5-b9f8-f0929bf7c97e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014TErNop6aVTmzgif2ymZMD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1455,
      "cache_read_input_tokens": 18328,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1455,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 69,
      "service_tier": "standard",
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

_source line 71 · 2026-05-22T03:37:41.207Z_

<details><summary>↩ Tool result · `toolu_011SrrP8BMVY9XxXdQUgL3mL`</summary>

```text
0	Found 28 decision blocks containing ScienceWorld-related content
1	
2	================================================================================
3	
4	[Lines 1222-1246]
5	- id: D068
6	  date: 2026-05-18 03:52 UTC
7	  summary: 'exp029 OOD reeval: 23.88% on 134 tasks. Information loss preliminary estimate
8	    17.9pp, action_is_valid insight confirms mechanism'
9	  rationale: 'exp029 step 15 on AlfworldOOD 134 tasks: success=23.88% (vs 28.1% on
10	    in-dist 32 tasks, -4pp as expected). Preliminary decomposition on unified OOD
11	    set: information loss (B→C) = 23.88% - 5.97% = 17.9pp. Sign misattribution (A→B)
12	    still missing Cell A OOD data (hsweep_h2 reeval pending). Key insight: action_is_valid
13	    nearly identical between factorial (57.65%) and exp029 (56.84%) despite 18pp success
14	    gap — full context advantage is in decision quality not action legality, supporting
15	    information loss mechanism narrative. Caveat: factorial only at step 5 (step mismatch)
16	    and KL inflating (0.24→1.77), final decomposition needs factorial step 15.'
17	  related_experiments:
18	  - exp_id: exp029_episode_level
19	    role: primary
20	    result: 23.88% OOD success
21	  - exp_id: factorial_h2_episodeadv_seed1
22	    role: comparison
23	    result: 5.97% OOD at step 5, KL inflating
24	  - exp_id: hsweep_h2_seed2
25	    role: pending
26	    result: OOD reeval needed for Cell A
27	  depends_on:
28	  - D066
29	  - D067
30	
31	================================================================================
32	
33	[Lines 1268-1294]
34	- id: D070
35	  date: 2026-05-18 04:58 UTC
36	  summary: '3-cell decomposition: information loss 89% (17.9pp) >> sign misattribution
37	    11% (2.2pp). Narrative rebalance needed.'
38	  rationale: 'OOD 134 tasks unified decomposition: Cell A (step-indep + step-level)
39	    3.73%, Cell B (step-indep + episode-level) 5.97%, Cell C (full context + episode-level)
40	    23.88%. Sign misattribution effect (A→B) = 2.24pp; information loss effect (B→C)
41	    = 17.91pp. Ratio ~1:8. Paper cannot claim sign misattribution as primary driver
42	    of performance loss. However, sign misattribution still matters for training STABILITY
43	    (seed1 collapse vs seed2 delayed recovery, 52% sign agreement = noisy gradient).
44	    Two mechanisms damage training in orthogonal dimensions: information loss limits
45	    WHAT you can learn (ceiling), sign misattribution determines WHETHER you learn
46	    (stability). CAVEAT: Cell B is step 5 only; factorial step 10-15 may change this
47	    ratio significantly. Step mismatch makes current decomposition preliminary.'
48	  related_experiments:
49	  - exp_id: hsweep_h2_seed2
50	    role: Cell A
51	    result: 3.73% OOD at step 15
52	  - exp_id: factorial_h2_episodeadv_seed1
53	    role: Cell B
54	    result: 5.97% OOD at step 5 (preliminary)
55	  - exp_id: exp029_episode_level
56	    role: Cell C
57	    result: 23.88% OOD at step 15
58	  depends_on:
59	  - D067
60	  - D068
61	
62	================================================================================
63	
64	[Lines 1295-1316]
65	- id: D071
66	  date: 2026-05-18 05:44 UTC
67	  summary: 'Factorial step 10 val=5.22%: sign misattribution 量化贡献降至 1.49pp (7.4%),
68	    接近噪声。Framing 调整方向：sign misattribution 价值在机制解释力（训练不稳定性），不在量化性能贡献。等 step 15 确认后最终定稿。'
69	  rationale: 'Step 10 3-cell 分解: Cell A 3.73%, Cell B 5.22%, Cell C 23.88%。Cell B-A
70	    差距 1.49pp ≈ 2/134 tasks, Fisher exact p >> 0.05。但 factorial 训练过程中 step 6 达 25.8%
71	    success（Cell A 从未超过 0%），证明消除 sign misattribution 后模型能开始学习，只是 info loss ceiling
72	    + KL 膨胀限制了最终 val 表现。Sign misattribution 的贡献从"量化性能"转向"机制解释"：解释 seed 间 0% vs 9.375%
73	    的随机性、52% sign agreement 的噪声特征。'
74	  related_experiments:
75	  - exp_id: factorial_h2_episodeadv_seed1
76	    role: primary
77	    result: step 10 val=5.22%, train peak step 6=25.8%, KL inflation 0.735→1.029
78	  - exp_id: hsweep_h2_seed2
79	    role: baseline_cell_a
80	    result: OOD 3.73%
81	  - exp_id: exp029_episode_level
82	    role: baseline_cell_c
83	    result: OOD 23.88%
84	  depends_on:
85	  - D070
86	  - D067
87	
88	================================================================================
89	
90	[Lines 1317-1337]
91	- id: D072
92	  date: 2026-05-18 09:14 UTC
93	  summary: Kill g080 (已确认坍缩) 释放 westd cuda:2,3 给 g095。Negative 结果（g050/g080 坍缩、factorial
94	    振荡、seed 间 variance）作为论文 diagnostic 贡献的核心内容，不当废数据处理。
95	  rationale: g080 step 5 val=3.125%（低于 SFT baseline 9.38%），entropy=0.185，action_valid=98.2%，完全坍缩且不可逆。继续跑无新信息，GPU
96	    应释放给 g095 定位 γ-cliff 临界点。同时确认叙事方向：diagnostic paper 的贡献恰恰是 failure mode 分析，negative
97	    结果（g050/g080 坍缩曲线、factorial 振荡 vs monotonic collapse 对比、seed 间 variance）直接变成论文
98	    figure/table。
99	  related_experiments:
100	  - exp_id: gsweep_g080_h5_seed1
101	    role: killed_for_resource
102	    result: val 3.125%, entropy collapse confirmed
103	  - exp_id: gsweep_g095_h5_seed1
104	    role: next_launch
105	    result: config ready, dry-run passed
106	  - exp_id: factorial_h2_episodeadv_seed1
107	    role: narrative_source
108	    result: oscillation pattern vs Cell A monotonic collapse
109	  depends_on:
110	  - D071
111	  - D070
112	
113	================================================================================
114	
115	[Lines 1338-1360]
116	- id: D073
117	  date: 2026-05-18 10:22 UTC
118	  summary: 3-cell 定量分解在 step 15 失效（Cell B=0.75% < Cell A=3.73%）。放弃 "X% info loss +
119	    Y% sign misattribution" 加法分解，转向定性双机制诊断：sign misattribution 杀死学习能力（Cell A 单调坍缩），info
120	    loss 杀死泛化能力（Cell B 能学但 OOD 崩溃），两者共同作用才导致 step-independent 失败。
121	  rationale: 'Factorial step 15: Cell B val OOD=0.75%, KL=2.845, val action_valid=11%。Train
122	    success=16.41% 但 OOD 完全崩溃，说明 truncated context 下模型 overfit 训练分布但无法泛化。3-cell 加法分解高度依赖
123	    checkpoint 选择（step 5: B>A, step 10: B≈A, step 15: B&lt;A），定量分解不可靠有 cherry-picking
124	    风险。但定性发现更丰富：(1) Cell A 单调坍缩到 0%（sign misattribution 完全阻止学习），(2) Cell B 高方差振荡后
125	    overfit 崩溃（episode advantage 恢复学习信号但 info loss 阻止泛化），(3) Cell C 稳定到 23.88%（两者都解决后正常学习）。这比简单的百分比分解更有洞察力。'
126	  related_experiments:
127	  - exp_id: factorial_h2_episodeadv_seed1
128	    role: primary
129	    result: step 15 val OOD=0.75%, train=16.41%, KL=2.845, 3-cell decomposition breaks
130	  - exp_id: hsweep_h2_seed2
131	    role: cell_a
132	    result: OOD 3.73%
133	  - exp_id: exp029_episode_level
134	    role: cell_c
135	    result: OOD 23.88%
136	  depends_on:
137	  - D071
138	  - D070
139	
140	================================================================================
141	
142	[Lines 1421-1437]
143	- id: D077
144	  date: 2026-05-18 17:47 UTC
145	  summary: 彻底放弃 bjb1 跑 exp029_seed2，转移到 westd。bjb1 转部署 h=20。现有 step 0-20 数据保留
146	  rationale: exp029_seed2 在 bjb1 累计 10+ 次失败：初始 OOM (3次)、存储 I/O crash、FSDP optimizer_offload
147	    bug、磁盘满 crash、vLLM stall (3.5h 空转)。每次修复后出现新问题，bjb1 对 episode-level 训练系统性不可靠。现有数据
148	    step 0-20 (val 37.5% at step 20) 已证明 Cell C seed2 学习能力，完整训练转移到 westd（factorial
149	    完成后释放 cuda:0,1）。bjb1 转部署 step_independent h=20（已验证 h=2 系列在 bjb1 上稳定）。
150	  related_experiments:
151	  - exp_id: exp029_episode_level_seed2
152	    role: primary
153	    result: 10+ failures on bjb1, val 37.5% at step 20
154	  - exp_id: hsweep_h20_seed1
155	    role: replacement
156	    result: pending deployment on bjb1
157	  depends_on:
158	  - D075
159	  - D076
160	
161	================================================================================
162	
163	[Lines 1475-1491]
164	- id: D080
165	  date: 2026-05-19 02:16 UTC
166	  summary: exp029_seed2 完成：val 峰值 31.25% (step 30)，稳定 28.1% (step 35-40)。Cell C 跨
167	    seed 确认——两 seed 均 ~28-31%，与 Cell A 崩溃和 Cell B 0.75% 形成清晰对比。Step 40 后训练已崩溃（train
168	    6.25%, invalid 80%），但 val 保持。Kill 释放 GPU。
169	  rationale: seed1 28.1%@step15, seed2 31.25%@step30, 稳定在 28.1%@step35-40。两 seed 收敛到同一量级，支撑
170	    "Cell C enables non-trivial learning" claim。格式退化（manager_invalid 0.8%→58%）是已知的
171	    extended training 问题，不影响核心 claim。继续跑无增量收益，kill 释放 westd cuda:0,1。
172	  related_experiments:
173	  - exp_id: exp029_episode_level_seed2
174	    role: primary
175	    result: val peak 31.25% (step 30), stable 28.1% (step 35-40)
176	  - exp_id: exp029_episode_level
177	    role: comparison
178	    result: seed1 val 28.1% (step 15), OOD 23.88%
179	  depends_on:
180	  - D078
181	
182	================================================================================
183	
184	[Lines 1492-1508]
185	- id: D081
186	  date: 2026-05-19 03:34 UTC
187	  summary: 启动 7B (Qwen3-8B) + ScienceWorld 两条并行实验线。7B 立即用 westd cuda:2,3 下载+零样本 eval；ScienceWorld
188	    先做 CPU 工程适配。用户明确要求"把条件性加分也做掉"。
189	  rationale: 用户要求做全部条件性加分实验（7B 验证 + ScienceWorld）。7B 用 Qwen3-8B（同家族，8B 参数），westd RTX
190	    PRO 6000 96GB 显存充裕。ScienceWorld Reviewer 要求必须用 episode total return 做 GRPO advantage，不用
191	    step-level intermediate reward。两条线可并行：7B 占 GPU，ScienceWorld 工程适配仅 CPU。
192	  related_experiments:
193	  - exp_id: plan_015
194	    role: target
195	    result: starting
196	  - exp_id: plan_014
197	    role: target
198	    result: starting
199	  depends_on:
200	  - D080
201	  - D078
202	
203	================================================================================
204	
205	[Lines 1525-1540]
206	- id: D083
207	  date: 2026-05-19 07:45 UTC
208	  summary: Qwen3-8B SFT baseline 80.6% OOD success（vs 1.7B 的 6.25%）。7B RL 实验 hypothesis
209	    从"RL 大幅提升"调整为"step-independent 是否仍导致退化"。核心看 Cell A 是否从 80.6% 下降 + Cell C 是否维持/小幅提升。
210	  rationale: SFT baseline 已 80.6%，RL 提升空间有限。但如果 step-independent 在强 baseline 上仍导致退化，反而是更有力的跨规模证据——sign
211	    misattribution 在任何模型规模下都是结构性问题。实验设计从"who improves more"转为"does step-independent
212	    still harm even strong models"。
213	  related_experiments:
214	  - exp_id: plan_015
215	    role: target
216	    result: hypothesis adjusted
217	  - exp_id: 7b_sft_v1
218	    role: evidence
219	    result: 80.6% OOD success
220	  depends_on:
221	  - D081
222	
223	================================================================================
224	
225	[Lines 1561-1578]
226	- id: D085
227	  date: 2026-05-19 11:14 UTC
228	  summary: Kill 8B Cell A at step 1, 立即启动 8B Cell C (episode-level)。Step 1 三重 collapse
229	    信号已足够支撑 scale-invariance claim。
230	  rationale: 8B Cell A step 1 数据：success 28.1%→12.5% 腰斩, entropy 0.115 ≈ 0, num_actions
231	    47.7/50 max out。三重 collapse 信号与 1.7B 完全一致。继续跑 4-5h 到 step 5 预期 val≈0%，边际信息增量极低。Cell
232	    C (episode-level 正控制) 是论文更缺的数据——同一 8B 模型、同一 80.6% SFT baseline，不同训练模式的对比远比 Cell
233	    A 多跑几步更有论文价值。4 GPU × 4-5h 机会成本应投入 Cell C。
234	  related_experiments:
235	  - exp_id: 7b_cell_a_h2
236	    role: killed
237	    result: 'step1 collapse: 28.1%→12.5%, entropy=0.115, scale-invariant'
238	  - exp_id: 8b_cell_c_episode
239	    role: next
240	    result: pending
241	  depends_on:
242	  - D083
243	  - D084
244	
245	================================================================================
246	
247	[Lines 1636-1653]
248	- id: D089
249	  date: 2026-05-19 11:51 UTC
250	  summary: 启动 ScienceWorld 实验线：用 1.7B 跑 Cell A vs Cell C 对比，解决单环境短板。mendelian-genetics
251	    排除。
252	  rationale: ScienceWorld SFT 数据 2989+ score=100 episodes（79% quality），远超 500 条阈值。mendelian-genetics
253	    2 个 task type 全部失败（gold path 质量问题，非模型问题），排除。ScienceWorld 用 1.7B 即可（解决单环境问题，不需要
254	    8B），可用 bjb1 2卡跑。8B ALFWorld Cell C 用 westd 4卡并行。Cell A vs Cell C on ScienceWorld
255	    是审稿人 "single environment" concern (#5) 的直接回应。
256	  related_experiments:
257	  - exp_id: 8b_cell_c_episode_v2
258	    role: parallel
259	    result: running on westd
260	  - exp_id: scienceworld_sft
261	    role: next
262	    result: planned for bjb1
263	  depends_on:
264	  - D085
265	  - D087
266	
267	================================================================================
268	
269	[Lines 1654-1679]
270	- id: D090
271	  date: 2026-05-19 12:54 UTC
272	  summary: 'Cell C v5: use_ref=False 释放 ref model 内存，解决 Catch-22（gpu_mem_util 0.35
273	    backward OOM vs 0.15 VLLM 初始化失败）'
274	  rationale: 4 次 OOM/失败证明 8B FSDP + optimizer + ref model 基础占用 ~90 GiB/GPU，无法在 gpu_memory_utilization
275	    0.15-0.35 间找到平衡点。use_ref=False 释放 ~8 GiB/GPU，允许 gpu_memory_utilization=0.20 同时满足
276	    VLLM 初始化和 backward 空间。代价是无 KL 约束，但验证 "episode-level 8B 能否训练" 比 KL 约束更重要。论文注明 limitation。
277	  related_experiments:
278	  - exp_id: 8b_cell_c_episode
279	    role: v1
280	    result: OOM backward
281	  - exp_id: 8b_cell_c_episode_v2
282	    role: v2
283	    result: OOM backward (token_len no-op)
284	  - exp_id: 8b_cell_c_v3
285	    role: v3
286	    result: OOM backward (mini_batch no effect)
287	  - exp_id: 8b_cell_c_episode_v4
288	    role: v4
289	    result: VLLM init fail (gpu_mem_util too low)
290	  - exp_id: 8b_cell_c_episode_v5
291	    role: v5
292	    result: 'planned: use_ref=False + gpu_mem_util=0.20'
293	  depends_on:
294	  - D085
295	  - D089
296	
297	================================================================================
298	
299	[Lines 1680-1694]
300	- id: D091
301	  date: 2026-05-19 13:22 UTC
302	  summary: 'Cell C v6: max_model_len=16384 + 移除 PYTORCH_CUDA_ALLOC_CONF。OOM 已解决（use_ref=False），v5
303	    新错误是 max_model_len=8192 太小（prompt 8450 tokens）+ expandable_segments 与 vLLM 不兼容'
304	  rationale: v5 验证了 use_ref=False + gpu_memory_utilization=0.20 组合可行（VLLM 初始化成功，FSDP
305	    加载正常）。max_model_len=8192 是 v4 为省 KV cache 内存降的，但 Cell C full-context mode 的 prompt
306	    可达 8450+ tokens。16384 匹配 max_prompt_length 配置且在 19.6 GiB VLLM 预算内可行（8B GQA 头减少了
307	    KV cache 需求）。PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True 与 vLLM CuMemAllocator
308	    冲突，必须移除。
309	  related_experiments:
310	  - exp_id: 8b_cell_c_episode_v5
311	    role: parent
312	    result: 'failed: max_model_len too small + CUDA_ALLOC incompatible'
313	  depends_on:
314	  - D090
315	
316	================================================================================
317	
318	[Lines 1708-1725]
319	- id: D093
320	  date: 2026-05-19 13:45 UTC
321	  summary: 'Cell C v7: gpu_memory_utilization=0.25 + max_model_len=16384。0.20 下 KV
322	    cache 仅 1.44 GiB（需 2.25 GiB），增到 0.25 后 KV cache ≈ 6.24 GiB（2.8x 余量）。vs 原 OOM 配置(0.35+ref)净释放
323	    17.6 GiB，backward 空间充足'
324	  rationale: KV cache 计算：gpu_mem_util=0.20 → VLLM 总 19.2 GiB，模型权重占 17.76 GiB，KV cache
325	    仅 1.44 GiB。gpu_mem_util=0.25 → VLLM 总 24 GiB，KV cache = 24 - 17.76 = 6.24 GiB，远超
326	    max_model_len=16384 所需的 2.25 GiB。Backward 空间：相比原失败配置（0.35 + ref model），0.25 少占
327	    9.6 GiB + ref 释放 8 GiB = 净多 17.6 GiB，backward 应无问题。不选 0.30（多给 VLLM 4.8 GiB 无必要），不选方案
328	    A（10240 可能在训练中遇到更长 prompt 再次失败）。
329	  related_experiments:
330	  - exp_id: 8b_cell_c_episode_v5
331	    role: parent
332	    result: 'failed: max_model_len=16384 needs 2.25 GiB KV cache, gpu_mem_util=0.20
333	      only provides 1.44 GiB'
334	  depends_on:
335	  - D091
336	  - D090
337	
338	================================================================================
339	
340	[Lines 1726-1742]
341	- id: D094
342	  date: 2026-05-19 14:09 UTC
343	  summary: 'Cell C v8（最后尝试）: ppo_mini_batch_size=2 + gpu_memory_utilization=0.22。v7
344	    backward OOM 缺 3.7 GiB。batch 4→2 约省一半激活内存，util 0.25→0.22 释放 2.88 GiB。如果 v8 仍 OOM，接受
345	    1.7B-only Cell C 数据，不再尝试'
346	  rationale: v7 数据：allocated 110.14 GiB，backward 需 8.94 GiB，可用 5.21 GiB，缺 3.7 GiB。ppo_mini_batch_size
347	    从 4 降到 2，backward 激活内存大约减半（~4.5 GiB）。gpu_memory_utilization 从 0.25 降到 0.22，释放
348	    (0.25-0.22)×96=2.88 GiB，KV cache 从 6.24 降到 3.36 GiB（仍 > 需要的 2.25 GiB）。组合后：可用 ~8.1
349	    GiB，需 ~4.5 GiB，余量 ~3.5 GiB。8B Cell C 连续 8 次失败已消耗大量 GPU 时间，这是最后一次尝试。论文有完整 1.7B
350	    Cell C 数据 + 8B Cell A collapse + 8B info loss，足够支撑 claim。
351	  related_experiments:
352	  - exp_id: 8b_cell_c_episode_v7
353	    role: parent
354	    result: 'failed: backward OOM, 110.14 GiB allocated, need 8.94 GiB, only 5.21
355	      GiB free'
356	  depends_on:
357	  - D093
358	
359	================================================================================
360	
361	[Lines 1743-1763]
362	- id: D095
363	  date: 2026-05-19 14:14 UTC
364	  summary: 正式放弃 8B Cell C：4×96GB 硬件不足以容纳 8B FSDP + VLLM + full-context backward（差
365	    ~4 GiB 无可调参数弥补）。论文 8B 验证限于 Cell A collapse + info loss 37.5pp。1.7B Cell C 数据完整充分
366	  rationale: 9 次连续失败穷尽所有配置空间。v8 暴露最后一个约束：ppo_mini_batch_size ≥ micro_batch_per_gpu(1)
367	    × n_gpus(4) = 4，不可再降。gpu_mem_util 0.25→0.22 仅省 2.93 GiB < 缺口 3.73 GiB。8B FSDP
368	    模型 + optimizer + VLLM 基线占用 ~110 GiB / 4GPU，backward 需 ~9 GiB，可用仅 ~5 GiB。根本矛盾：full-context
369	    episode 的长序列 backward 激活在 96GB GPU 上装不下。论文有 1.7B Cell C 完整数据（23.88% OOD, 双 seed）+
370	    8B Cell A collapse + 8B info loss 37.5pp + stochastic-triggered mechanism，scale
371	    invariance claim 已充分支撑。8B Cell C 缺失在 Limitations 说明。
372	  related_experiments:
373	  - exp_id: 8b_cell_c_episode_v7
374	    role: evidence
375	    result: 'backward OOM: 110.14 GiB allocated, need 8.94, free 5.21'
376	  - exp_id: 8b_cell_c_episode_v5
377	    role: evidence
378	    result: VLLM init + val_before_train passed but backward OOM
379	  depends_on:
380	  - D094
381	  - D093
382	  - D090
383	
384	================================================================================
385	
386	[Lines 1764-1777]
387	- id: D096
388	  date: 2026-05-19 14:27 UTC
389	  summary: 'D096: 尝试 FSDP CPU Offload 解决 8B Cell C backward OOM'
390	  rationale: 用户批准"试一下，不行再加卡"。v7 backward OOM 缺口 3.7 GiB，CPU Offload 可省 ~8 GiB/卡，理论上绰绰有余。改动最小（只需修改
391	    FSDP config 加 CPUOffload），不需要改 RAGEN 代码。如果失败，用户同意租更多 GPU。
392	  related_experiments:
393	  - exp_id: 8b_cell_c_episode_v7
394	    role: predecessor
395	    result: backward OOM, gap 3.7 GiB
396	  - exp_id: 8b_cell_c_episode_v8
397	    role: predecessor
398	    result: config constraint violation
399	  depends_on:
400	  - D095
401	
402	================================================================================
403	
404	[Lines 1778-1790]
405	- id: D097
406	  date: 2026-05-19 18:17 UTC
407	  summary: 'D097: 8B Cell C v9 (FSDP2 CPUOffload) 失败——RAGEN GRPO train.py 不支持 FSDP2'
408	  rationale: 'v9 启动后立即 NotImplementedError: RAGEN TaskRunner.run() 未实现 FSDP2 strategy。SFT
409	    能用 FSDP2 是因为走 verl 原生 fsdp_sft_trainer，但 GRPO 走 RAGEN 自有代码。D096 的前提（只需改 config）不成立。回到用户决策：加卡还是接受
410	    1.7B-only。'
411	  related_experiments:
412	  - exp_id: 8b_cell_c_v9
413	    role: failed
414	    result: 'NotImplementedError: RAGEN GRPO 不支持 FSDP2'
415	  depends_on:
416	  - D096
417	  - D095
418	
419	================================================================================
420	
421	[Lines 1802-1815]
422	- id: D099
423	  date: 2026-05-19 20:13 UTC
424	  summary: 'D099: 8B Cell C v9c backward pass 成功——FSDP2+CPUOffload 方案可行，8B Cell C
425	    解锁'
426	  rationale: v9c 完成 step 1/30 backward pass 无 OOM。FSDP2+CPUOffload 将峰值显存从 91 GB 降至
427	    83 GB/卡（余量 12 GB），10 次修复（5 文件 10 处 FSDP1→FSDP2 兼容）全部生效。预计 15-16h 完成 30 steps 训练。不需要租卡。
428	  related_experiments:
429	  - exp_id: 8b_cell_c_v9c
430	    role: running
431	    result: step 1/30 完成, backward pass 无 OOM, 83 GB/卡
432	  depends_on:
433	  - D098
434	  - D097
435	  - D096
436	
437	================================================================================
438	
439	[Lines 1841-1853]
440	- id: D102
441	  date: 2026-05-20 08:05 UTC
442	  summary: v9d 暂停训练，转向 step 10 OOD eval——8+ 次崩溃指向系统性不稳定，step 10 val=96.875% 数据已足够强
443	  rationale: v9d 从 step 5 到 step 11 训练正常（success 81→97%），但 8+ 次崩溃覆盖磁盘满/model_path
444	    误删/vLLM OOM/SIGHUP/静默死亡多种 failure mode，指向 FSDP2+CPUOffload+4卡 8B 在 westd 上的系统性不稳定。继续重启大概率继续崩。step
445	    10 val=96.875% vs Cell A 1.5% 的对比已足够支撑跨尺度 claim。先做 OOD eval 拿论文数据，同时诊断根因决定是否值得继续训练到
446	    step 30。
447	  related_experiments:
448	  - exp_id: 8b_cell_c_episode_v9d
449	    role: target
450	    result: step 10 val 96.875%, 8+ crashes
451	  depends_on:
452	  - D101
453	
454	================================================================================
455	
456	[Lines 1854-1867]
457	- id: D103
458	  date: 2026-05-20 09:24 UTC
459	  summary: v9d step 15 后停止训练——step 12 起 GRPO reward 饱和（100% success, pg_loss=0），继续训练无信号。转向
460	    OOD eval
461	  rationale: Step 12 完整 metrics：train success 1.0，critic score 全 10.0，advantages 全
462	    0，pg_loss=0，grad_norm 0.022。GRPO 依赖 group 内 reward 差异，全组成功则 advantage normalization
463	    为零。Step 12→30 模型权重不会变化（除 entropy drift），等效 GPU 空转。OOD eval 是论文关键数据，step 10/15
464	    checkpoint 已可评估。停训练后释放 westd 4×GPU 用于 OOD eval + 可能的 ScienceWorld GRPO。
465	  related_experiments:
466	  - exp_id: 8b_cell_c_episode_v9d
467	    role: target
468	    result: step 12 reward saturation, 100% in-dist success
469	  depends_on:
470	  - D102
471	
472	================================================================================
473	
474	[Lines 1868-1889]
475	- id: D104
476	  date: 2026-05-20 12:14 UTC
477	  summary: Claim 1 升级：从 "unstable/fragile" 升级为 "systematic failure mechanism, scale-invariant"
478	    + "necessary minimum fix"。不用 "catastrophic"（1.7B seed2 学了 9.375%）
479	  rationale: Reviewer 独立评估：8B Cell C 90.3% + Cell A 1.5% 跨尺度对比、γ-sweep 全坍缩、factorial
480	    2×2 全部验证——证据强度已超出 D067 降级时的 "unstable/fragile"。新表述：systematic + scale-invariant
481	    failure mechanism，episode-level 是 necessary minimum fix（不 claim optimal，承认 GAGPO
482	    等更优）。保留 stochastically triggered 解释社区为何未普遍注意。最大风险：R1(trivial fix)+R2(无 fine-grained
483	    baseline) 组合攻击——Practitioner Decision Tree 在 Discussion 中可部分缓解。
484	  related_experiments:
485	  - exp_id: 8b_cell_c_episode_v9d
486	    role: key_evidence
487	    result: 90.3% OOD
488	  - exp_id: 7b_cell_a_h2
489	    role: key_evidence
490	    result: 1.5% collapse
491	  - exp_id: gsweep_g100_h5_seed1
492	    role: supporting
493	    result: γ=1.0 collapse
494	  depends_on:
495	  - D067
496	  - D103
497	
498	================================================================================
499	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UvN5LYeDV9iSrVapRBHaFQ",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "b0cb1b33-afcf-46a6-95ed-ecb10cbf20f4"
}
```

</details>

---

### System

_source line 72_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad21c2477dd6123aa",
  "tool_use_id": "toolu_01UvN5LYeDV9iSrVapRBHaFQ",
  "description": "Reading ~/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-1-projects-cost-verify-agent-rl/54b94781-146b-4013-9381-11e3737077cb/tool-results/blomixe5q.txt",
  "usage": {
    "total_tokens": 30363,
    "tool_uses": 10,
    "duration_ms": 67785
  },
  "last_tool_name": "Read",
  "uuid": "4881c9a8-d1e7-4e42-b53f-a630f7bd6a74",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb"
}
```

---

### Tool call

_source line 73_

<details open><summary>🔧 Tool call — Read · `toolu_01BNQk1QXCWC26hkHjS5GXQk`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-1-projects-cost-verify-agent-rl/54b94781-146b-4013-9381-11e3737077cb/tool-results/blomixe5q.txt",
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
  "parent_tool_use_id": "toolu_01UvN5LYeDV9iSrVapRBHaFQ",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "f3817960-f230-493c-aa1e-d27b01ee34cf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JXqMDDUaVSmfFnLHhnJMzn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10453,
      "cache_read_input_tokens": 19783,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10453,
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

_source line 74 · 2026-05-22T03:37:47.354Z_

<details><summary>↩ Tool result · `toolu_01BNQk1QXCWC26hkHjS5GXQk`</summary>

```text
500	
501	[Lines 1890-1908]
502	- id: D105
503	  date: 2026-05-20 13:26 UTC
504	  summary: ScienceWorld GRPO 三场景预案：(1) Cell A collapse + Cell C learns = 最强; (2) 两者都不学
505	    = diagnosis 仍成立，fix 加限定语; (3) Cell A 不 collapse = 可解释为 "nothing to destroy at
506	    0% baseline"。核心结论：ScienceWorld 是 bonus，不是 load-bearing
507	  rationale: Reviewer 独立评估：三个场景概率 40%/35%/25%。无论哪个场景，ALFWorld 的跨尺度证据（1.7B + 8B）+ factorial
508	    + γ-sweep 已足够 EMNLP ≥ 4.0。ScienceWorld Cell A val_before_train = 0% 使场景 3 有合理解释（sign
509	    misattribution 破坏的是 existing capability，0% baseline 无东西可破坏）。关键诊断指标不仅是 pass@1，还有
510	    entropy/KL 轨迹（区分 active destruction vs no signal）。场景 2 需提前准备 Limitations 段 "capacity
511	    vs credit" 讨论。
512	  related_experiments:
513	  - exp_id: scienceworld_grpo_cell_a
514	    role: pending
515	    result: running
516	  - exp_id: scienceworld_grpo_cell_c
517	    role: pending
518	    result: running
519	  depends_on:
520	  - D104
521	
522	================================================================================
523	
524	[Lines 1909-1925]
525	- id: D106
526	  date: 2026-05-20 13:49 UTC
527	  summary: ScienceWorld Cell A 崩溃确认：final_score 6.0→-100.0，比 ALFWorld 更极端。D105 场景
528	    1 上半部成立——failure mechanism 跨环境验证完成
529	  rationale: Cell A (step-independent h=2) 在 ScienceWorld 15 步全程 0% success，final_score
530	    降至 -100.0（ALFWorld 不会负分）。entropy 上升+KL 崩塌模式与 ALFWorld 一致。ScienceWorld 任务结构（科学推理、长
531	    horizon）与 ALFWorld（家务）完全不同，排除环境特异性。等 Cell C 结果完成场景 1 判断。Reviewer 风险 R3 (single
532	    env) 基本解决。
533	  related_experiments:
534	  - exp_id: scienceworld_grpo_cell_a
535	    role: key_evidence
536	    result: collapse confirmed, final_score -100.0
537	  - exp_id: scienceworld_grpo_cell_c
538	    role: pending
539	    result: 1/15 steps, ~7h
540	  depends_on:
541	  - D105
542	
543	================================================================================
544	
545	[Lines 1926-1943]
546	- id: D107
547	  date: 2026-05-20 15:34 UTC
548	  summary: ScienceWorld Cell C 崩溃（第3次 Java 异常）：最后重试一次加固版，不阻塞论文压缩
549	  rationale: ScienceWorld Java 环境三次崩溃（Info Loss Eval ×2 + Cell C ×1），root cause 是
550	    Java IPC 通信异常。Cell A collapse 已确认（D106），跨环境 failure 证据充分。Cell C（episode-level
551	    fix 跨环境验证）是 nice-to-have 而非 must-have——论文核心 claim 不依赖它。策略：(1) 最后重试一次，Agent 先调查
552	    Java 异常并加固；(2) Paper Agent 立即推进 16→8 页压缩，不等 Cell C；(3) 若再次崩溃则接受现有数据，Limitations
553	    如实说明。
554	  related_experiments:
555	  - exp_id: scienceworld_grpo_cell_c
556	    role: subject
557	    result: DONE(failed) — Java IPC crash after step 1
558	  - exp_id: scienceworld_grpo_cell_a
559	    role: evidence
560	    result: DONE(negative) — collapse confirmed, cross-env failure validated
561	  depends_on:
562	  - D105
563	  - D106
564	
565	================================================================================
566	
567	[Lines 1944-1965]
568	- id: D108
569	  date: 2026-05-21 01:48 UTC
570	  summary: Seed 3 OOD 10.45% (vs Seed 1 23.88%)：Table 1 报 mean[range]，Limitations
571	    加 seed variance 说明。Cell C v3 ScienceWorld episode-level 坍塌：继续观察到 step 5，不影响当前
572	    claim（论文只 claim collapse generalizes，不 claim fix generalizes）
573	  rationale: Seed 3 OOD 差异统计显著 (z=2.91, p<0.005)，但均值 17.2% 仍高于 SFT baseline 12.5%，核心
574	    claim "episode-level avoids collapse and enables learning" 两 seed 都成立。Cell C v3
575	    step 2 reward saturation（128 trajectories 全零 reward），与 Section 3 reward saturation
576	    分析一致——ScienceWorld 更难，episode-level 不能解决 reward saturation。论文已谨慎措辞，只需加 Limitations。
577	  related_experiments:
578	  - exp_id: exp029_seed3_ood_v2
579	    role: seed3 OOD eval
580	    result: 10.45% (14/134)
581	  - exp_id: exp029_episode_level
582	    role: seed1 OOD baseline
583	    result: 23.88% (32/134)
584	  - exp_id: scienceworld_grpo_cell_c_v3
585	    role: SW episode-level fix
586	    result: collapsing at step 2
587	  depends_on:
588	  - D104
589	  - D106
590	
591	================================================================================
592	
593	[Lines 1966-1982]
594	- id: D109
595	  date: 2026-05-21 02:41 UTC
596	  summary: Cell C v3 提前终止（step 3），释放 westd cuda:2,3；启动 seed 5 并行训练（westd cuda:0,1）
597	  rationale: Cell C v3 step 3 已满足止损条件（success=0%, action_is_valid=9.4%<20%），且趋势持续恶化（score
598	    2.71→0.96, reward 0.5→0.153），等 step 5 只浪费 ~10 GPU-hours。论文 Limitations 段用 step
599	    3 数据即可。释放的 GPU 加上已空闲的 cuda:0,1，启动 seed 5 并行训练——与 bjb1 seed 4 同时跑，最终 4 个 seed 的
600	    OOD 数据统计可靠性远优于 3 个。当前 2-seed OOD variance 大（10.4% vs 23.9%），4 seeds 可报 mean±std，审稿人信服度显著提升。
601	  related_experiments:
602	  - exp_id: scienceworld_grpo_cell_c_v3
603	    role: terminated
604	    result: 'negative: 3 steps 0% success, collapse confirmed'
605	  - exp_id: exp029_seed4
606	    role: parallel_seed
607	    result: training on bjb1
608	  depends_on:
609	  - D107
610	  - D108
611	
612	================================================================================
613	
614	[Lines 2211-2228]
615	- id: D120
616	  date: 2026-05-22 03:34 UTC
617	  summary: 接受 Reviewer 叙事建议：干预实验降级为 Discussion，核心 claim 聚焦双机制诊断 + factorial + 8B scale；ScienceWorld
618	    跨环境验证升为 P0
619	  rationale: Reviewer 审查结论：(1) Claim 1（双机制诊断）证据 VERY STRONG，足够支撑核心贡献；(2) 干预失败/response
620	    inflation/mode shift 证据不足作 core claim（N=1、训练步数混杂、C' 实现 bug）；(3) 无 ScienceWorld
621	    预估 3.0-3.5（Findings），补齐后 3.5-4.0（Conference）。ScienceWorld 是达到 EMNLP 2026 Overall
622	    ≥4 的关键门槛。干预实验放 Discussion/Observations，不稀释核心贡献。seed_2048 step 1-2 即崩溃（resp_len
623	    15511, success 0.78%），无法提供 healthy baseline，但更新 collapse rate 至 4/7=57%。
624	  related_experiments:
625	  - exp_id: exp029_new_seed_2048
626	    role: observation
627	    result: collapsing at step 1-2, resp_len=15865, cannot serve as healthy baseline
628	  - exp_id: exp029_c_prime_resume_mt50_v2
629	    role: parent
630	    result: negative, cap ineffective
631	  depends_on:
632	  - D119
633	
634	================================================================================
635	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UvN5LYeDV9iSrVapRBHaFQ",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "abec4a0a-9956-4898-a396-17948bb25f87"
}
```

</details>

---

### System

_source line 75_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad21c2477dd6123aa",
  "tool_use_id": "toolu_01UvN5LYeDV9iSrVapRBHaFQ",
  "description": "Searching for scienceworld|science.world",
  "usage": {
    "total_tokens": 33298,
    "tool_uses": 11,
    "duration_ms": 72768
  },
  "last_tool_name": "Grep",
  "uuid": "4c1597f9-5506-45ae-b540-2eb78c48e296",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb"
}
```

---

### Tool call

_source line 76_

<details open><summary>🔧 Tool call — Grep · `toolu_01X4UoRKAe9WtXehywDwxBgN`</summary>

```json
{
  "pattern": "scienceworld|science.world",
  "path": "/tmp/decisions_yaml.txt",
  "output_mode": "content",
  "-i": true,
  "-n": true,
  "head_limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UvN5LYeDV9iSrVapRBHaFQ",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "6c19ec64-cb4a-4675-8bfc-7c93fa8aae34",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nf4FinswBPPUfJiBKZCQTc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2931,
      "cache_read_input_tokens": 30236,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2931,
        "ephemeral_1h_input_tokens": 0
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

_source line 77 · 2026-05-22T03:37:52.335Z_

<details><summary>↩ Tool result · `toolu_01X4UoRKAe9WtXehywDwxBgN`</summary>

```text
1494:  summary: 启动 7B (Qwen3-8B) + ScienceWorld 两条并行实验线。7B 立即用 westd cuda:2,3 下载+零样本 eval；ScienceWorld
1496:  rationale: 用户要求做全部条件性加分实验（7B 验证 + ScienceWorld）。7B 用 Qwen3-8B（同家族，8B 参数），westd RTX
1497:    PRO 6000 96GB 显存充裕。ScienceWorld Reviewer 要求必须用 episode total return 做 GRPO advantage，不用
1498:    step-level intermediate reward。两条线可并行：7B 占 GPU，ScienceWorld 工程适配仅 CPU。
1638:  summary: 启动 ScienceWorld 实验线：用 1.7B 跑 Cell A vs Cell C 对比，解决单环境短板。mendelian-genetics
1640:  rationale: ScienceWorld SFT 数据 2989+ score=100 episodes（79% quality），远超 500 条阈值。mendelian-genetics
1641:    2 个 task type 全部失败（gold path 质量问题，非模型问题），排除。ScienceWorld 用 1.7B 即可（解决单环境问题，不需要
1642:    8B），可用 bjb1 2卡跑。8B ALFWorld Cell C 用 westd 4卡并行。Cell A vs Cell C on ScienceWorld
1648:  - exp_id: scienceworld_sft
1861:    checkpoint 已可评估。停训练后释放 westd 4×GPU 用于 OOD eval + 可能的 ScienceWorld GRPO。
1892:  summary: ScienceWorld GRPO 三场景预案：(1) Cell A collapse + Cell C learns = 最强; (2) 两者都不学
1894:    0% baseline"。核心结论：ScienceWorld 是 bonus，不是 load-bearing
1896:    + γ-sweep 已足够 EMNLP ≥ 4.0。ScienceWorld Cell A val_before_train = 0% 使场景 3 有合理解释（sign
1901:  - exp_id: scienceworld_grpo_cell_a
1904:  - exp_id: scienceworld_grpo_cell_c
1911:  summary: ScienceWorld Cell A 崩溃确认：final_score 6.0→-100.0，比 ALFWorld 更极端。D105 场景
1913:  rationale: Cell A (step-independent h=2) 在 ScienceWorld 15 步全程 0% success，final_score
1914:    降至 -100.0（ALFWorld 不会负分）。entropy 上升+KL 崩塌模式与 ALFWorld 一致。ScienceWorld 任务结构（科学推理、长
1918:  - exp_id: scienceworld_grpo_cell_a
1921:  - exp_id: scienceworld_grpo_cell_c
1928:  summary: ScienceWorld Cell C 崩溃（第3次 Java 异常）：最后重试一次加固版，不阻塞论文压缩
1929:  rationale: ScienceWorld Java 环境三次崩溃（Info Loss Eval ×2 + Cell C ×1），root cause 是
1935:  - exp_id: scienceworld_grpo_cell_c
1938:  - exp_id: scienceworld_grpo_cell_a
1947:    加 seed variance 说明。Cell C v3 ScienceWorld episode-level 坍塌：继续观察到 step 5，不影响当前
1952:    分析一致——ScienceWorld 更难，episode-level 不能解决 reward saturation。论文已谨慎措辞，只需加 Limitations。
1960:  - exp_id: scienceworld_grpo_cell_c_v3
1974:  - exp_id: scienceworld_grpo_cell_c_v3
2213:  summary: 接受 Reviewer 叙事建议：干预实验降级为 Discussion，核心 claim 聚焦双机制诊断 + factorial + 8B scale；ScienceWorld
2216:    inflation/mode shift 证据不足作 core claim（N=1、训练步数混杂、C' 实现 bug）；(3) 无 ScienceWorld
2217:    预估 3.0-3.5（Findings），补齐后 3.5-4.0（Conference）。ScienceWorld 是达到 EMNLP 2026 Overall
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UvN5LYeDV9iSrVapRBHaFQ",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "a37fb779-b892-49d1-965b-7ca6ffe8c78b"
}
```

</details>

---

### System

_source line 78_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad21c2477dd6123aa",
  "tool_use_id": "toolu_01UvN5LYeDV9iSrVapRBHaFQ",
  "description": "Running Verify all Cell A/C mentions are captured",
  "usage": {
    "total_tokens": 34777,
    "tool_uses": 12,
    "duration_ms": 87846
  },
  "last_tool_name": "Bash",
  "uuid": "f97c5344-86fc-47fb-832e-91abf4c0d9ec",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb"
}
```

---

### Tool call

_source line 79_

<details open><summary>🔧 Tool call — Bash · `toolu_01Tc89h52eyGKxu4mym48s6E`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport re\n\nwith open('/tmp/decisions_yaml.txt', 'r') as f:\n    lines = f.readlines()\n\n# Check for any Cell A/Cell C mentions NOT in the already-found blocks\n# The found decision blocks start at these lines (0-indexed):\nfound_starts = [1221, 1267, 1294, 1316, 1337, 1420, 1474, 1491, 1524, 1560, 1635, 1653, 1679, 1707, 1725, 1742, 1763, 1777, 1801, 1840, 1853, 1867, 1889, 1908, 1925, 1943, 1965, 2210]\n\n# Find decision boundaries\ndecision_starts = []\nfor i, line in enumerate(lines):\n    if re.match(r'^- id: D\\d+', line):\n        decision_starts.append(i)\n\n# Cell A / Cell C pattern - but exclude Cell Agent, Cell Adapter etc.\ncell_pattern = re.compile(r'Cell [AC](?!\\w)')\nmatching = set()\nfor i, line in enumerate(lines):\n    if cell_pattern.search(line):\n        # find which decision block\n        best = None\n        for ds in decision_starts:\n            if ds <= i:\n                best = ds\n            else:\n                break\n        if best is not None:\n            matching.add(best)\n\nnot_found = matching - set(found_starts)\nif not_found:\n    print(f\"Additional Cell A/C blocks not in ScienceWorld set: {sorted(not_found)}\")\n    for ds in sorted(not_found):\n        end = len(lines)\n        for next_ds in decision_starts:\n            if next_ds > ds:\n                end = next_ds\n                break\n        # Print the ID line\n        print(f\"  {lines[ds].strip()}\")\nelse:\n    print(\"All Cell A/C mentions are already captured in the extracted blocks.\")\nPYEOF\n",
  "description": "Verify all Cell A/C mentions are captured"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UvN5LYeDV9iSrVapRBHaFQ",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "66eae0fa-3ab9-4f73-93c0-82b89e30e4ab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EHXxWZouccL27VgnukqEfh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1477,
      "cache_read_input_tokens": 33167,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1477,
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

_source line 80 · 2026-05-22T03:38:07.488Z_

<details><summary>↩ Tool result · `toolu_01Tc89h52eyGKxu4mym48s6E`</summary>

```text
All Cell A/C mentions are already captured in the extracted blocks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UvN5LYeDV9iSrVapRBHaFQ",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "d0e540c4-377f-4245-9415-e54236b94f8d"
}
```

</details>

---

### System

_source line 81_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a81374730ba0416fe",
  "tool_use_id": "toolu_01N2zJUo1dnEGhGjTPYb6p2w",
  "status": "completed",
  "output_file": "",
  "summary": "Extract ScienceWorld experiments from registry",
  "usage": {
    "total_tokens": 29283,
    "tool_uses": 5,
    "duration_ms": 145517
  },
  "uuid": "b6655676-8b79-4f7c-be0d-67522146c752",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb"
}
```

---

### Tool result

_source line 82 · 2026-05-22T03:39:00.922Z_

<details><summary>↩ Tool result · `toolu_01N2zJUo1dnEGhGjTPYb6p2w`</summary>

```text
Confirmed: the 3 gamma sweep experiments are false positives — they matched `_sw` in `_alfworld_gamma_sweep_*`. The actual ScienceWorld experiments are the remaining 11.

Here are all 11 genuine ScienceWorld experiments with full verbatim data:

---

### 1. `scienceworld_sft`
- **Status:** DONE
- **Conclusion:** success
- **Created:** 2026-05-19T14:35:00.255Z
- **Updated:** 2026-05-19T17:50:12.565Z
- **Hypothesis:** ScienceWorld 1.7B SFT 训练，为后续 GRPO 实验提供 base checkpoint。验证 SFT 训练 pipeline 可泛化到第二个交互环境（ALFWorld 之外），支撑跨环境 RL 训练失败机制对比（Cell A vs Cell C）。数据：3592 train / 1796 val expert trajectories。
- **Spec:**
  - command: `bash /root/cost-verify-agent-rl/RAGEN/scripts/run_scienceworld_sft.sh`
  - server: westd-47453
  - gpu: [cuda:0, cuda:1, cuda:2, cuda:3]
  - pid: 120838
  - data_path: /root/autodl-tmp/expert_sft/scienceworld_sft_train.jsonl
  - data_count: 3592
  - model_name: Qwen3-1.7B
  - seed: 42
  - log_path: /root/autodl-tmp/wandb/
  - checkpoint_path: /root/autodl-tmp/checkpoints/scienceworld_sft/
  - hyperparams: {lr: 5e-6, epochs: 2, batch_size: 16, max_length: 16384, fsdp: fsdp2}
  - wandb_run_id: dqoxg94e
- **Metrics:** train_loss_final: 0.00318, val_loss_final: 0.01098, total_steps: 448, epochs: 2, total_train_time_s: 9319.4, checkpoint: global_step_448
- **Completed:** 2026-05-19T17:50:12.566Z

---

### 2. `scienceworld_sft_eval`
- **Status:** DONE
- **Conclusion:** killed
- **Created:** 2026-05-19T18:11:10.597Z
- **Updated:** 2026-05-19T18:46:33.866Z
- **Hypothesis:** Evaluate ScienceWorld SFT checkpoint on dev split (1796 episodes, 30 task types). Establishes SFT baseline success rate for ScienceWorld before GRPO experiments.
- **Parent:** scienceworld_sft
- **Spec:**
  - command: `python /root/cost-verify-agent-rl/eval_scienceworld.py --temperature 0.4`
  - server: bjb1-17606
  - gpu: [cuda:0, cuda:1]
  - pid: 183712
  - data_path: scienceworld dev split
  - data_count: 1796
  - model_name: Qwen3-1.7B (ScienceWorld SFT)
  - seed: 42
  - checkpoint_source: scienceworld_sft/global_step_448
  - eval_data: ScienceWorld dev split, 1796 episodes, 30 task types
- **Completed:** 2026-05-19T18:46:33.866Z

---

### 3. `scienceworld_sft_eval_v2`
- **Status:** DONE
- **Conclusion:** success
- **Retry count:** 1
- **Created:** 2026-05-19T18:50:45.230Z
- **Updated:** 2026-05-20T14:15:37.390Z
- **Hypothesis:** SFT-trained model on ScienceWorld can achieve meaningful task completion rates across diverse science tasks, establishing a baseline for subsequent RL fine-tuning comparison.
- **Parent:** scienceworld_sft_eval
- **Spec:**
  - command: `python /root/cost-verify-agent-rl/eval_scienceworld.py --temperature 0.4 --resume --episode_timeout 300`
  - server: bjb1-17606
  - gpu: [cuda:0, cuda:1]
  - pid: 195853
  - data_path: scienceworld dev split
  - data_count: 1796
  - model_name: Qwen3-1.7B (ScienceWorld SFT)
  - seed: 42
  - checkpoint_source: scienceworld_sft/global_step_448
  - eval_data: ScienceWorld dev split, 1796 episodes, 30 task types
  - checkpoint_path: N/A (eval only)
- **Metrics:**
  - total_episodes: 1796, success_count: 540, overall_success_rate: 0.301, timeouts: 0, errors: 0
  - avg_score: 20.9, avg_steps_per_episode: 28.7, total_time_seconds: 51462
  - Per-task breakdown (30 task types):
    - boil: 0/7 (0%), change-the-state-of-matter-of: 1/7 (14.3%), chemistry-mix: 0/8 (0%)
    - chemistry-mix-paint-secondary-color: 2/9 (22.2%), chemistry-mix-paint-tertiary-color: 0/9 (0%)
    - find-animal: 37/75 (49.3%), find-living-thing: 49/75 (65.3%), find-non-living-thing: 58/75 (77.3%)
    - find-plant: 9/75 (12%), freeze: 0/7 (0%), grow-fruit: 2/31 (6.5%), grow-plant: 0/31 (0%)
    - identify-life-stages-1: 0/3 (0%), identify-life-stages-2: 0/2 (0%)
    - inclined-plane-determine-angle: 7/42 (16.7%), inclined-plane-friction-named-surfaces: 83/346 (24%)
    - inclined-plane-friction-unnamed-surfaces: 10/40 (25%), lifespan-longest-lived: 28/31 (90.3%)
    - lifespan-longest-lived-then-shortest-lived: 28/31 (90.3%), lifespan-shortest-lived: 21/31 (67.7%)
    - measure-melting-point-known-substance: 25/109 (22.9%), measure-melting-point-unknown-substance: 27/75 (36%)
    - melt: 1/7 (14.3%), mendelian-genetics-known-plant: 8/30 (26.7%), mendelian-genetics-unknown-plant: 35/120 (29.2%)
    - power-component: 3/5 (60%), power-component-renewable-vs-nonrenewable-energy: 0/5 (0%)
    - test-conductivity: 35/225 (15.6%), test-conductivity-of-unknown-substances: 44/150 (29.3%), use-thermometer: 27/135 (20%)
  - results_json_path: /root/autodl-tmp/checkpoints/scienceworld_sft/eval_results_dev_v2.json
- **Previous failure:** 409/1796 episodes completed (22.8%), success_rate 0.386 at that point
- **Completed:** 2026-05-19T23:59:54.217Z

---

### 4. `scienceworld_grpo_cell_a`
- **Status:** DONE
- **Conclusion:** negative
- **Created:** 2026-05-20T11:24:49.171Z
- **Updated:** 2026-05-20T13:54:57.116Z
- **Hypothesis:** ScienceWorld 环境下 step-independent GRPO (h=2) 也会出现 policy collapse，验证 ALFWorld 观察到的 collapse 是 step-independent credit assignment 的固有问题而非环境特异性
- **Parent:** scienceworld_sft
- **Spec:**
  - command: `cd /root/cost-verify-agent-rl/RAGEN && WANDB_PROJECT=cost-verify-agent-rl python train.py --config-name _scienceworld_cell_a_grpo`
  - server: westd-47453, gpu: cuda:0,1, pid: 759987
  - wandb_run_id: f1c4g6dk
  - data_path: ScienceWorldSG, data_count: 30
  - model_name: Qwen3-1.7B (ScienceWorld SFT checkpoint), seed: 42
  - checkpoint_source: scienceworld_sft
  - eval_data: ScienceWorldSG 30 task types (dev split)
  - checkpoint_path: /root/autodl-tmp/checkpoints/scienceworld-cell-a/global_step_15
  - hyperparams: {total_training_steps: 15, context_window_mode: step_independent, step_independent_history_length: 2, env_groups: 16, group_size: 8, ppo_mini_batch_size: 8, ppo_max_token_len_per_gpu: 16384, optimizer_offload: true, lr: 1e-06, n_gpus_per_node: 2}
- **Metrics:** steps_completed: 14, success_rate: 0, final_score_train: -100, final_score_val: 1, reward_mean_start: 0.6, reward_mean_end: 0.1, entropy_start: 0.283, entropy_end: 0.52, kl_start: 1.606, kl_end: 0.03, exit_mode: abnormal (log truncated at step 15 start), note: "collapse confirmed - success rate 0% throughout, matches ALFWorld Cell A pattern"
- **Completed:** 2026-05-20T13:54:57.117Z

---

### 5. `scienceworld_grpo_cell_c`
- **Status:** DONE
- **Conclusion:** failed
- **Created:** 2026-05-20T11:24:51.574Z
- **Updated:** 2026-05-20T15:32:10.728Z
- **Hypothesis:** ScienceWorld 环境下 episode-level GRPO 能避免 collapse 并学到有效策略，验证 episode-level credit 作为 fix 的跨环境泛化性
- **Parent:** scienceworld_sft
- **Spec:**
  - command: `cd /root/cost-verify-agent-rl/RAGEN && WANDB_PROJECT=cost-verify-agent-rl python train.py --config-name _scienceworld_cell_c_grpo`
  - server: westd-47453, gpu: cuda:2,3, pid: 766820
  - wandb_run_id: sx7h864t
  - data_path: ScienceWorldSG, data_count: 30
  - model_name: Qwen3-1.7B (ScienceWorld SFT checkpoint), seed: 42
  - checkpoint_source: scienceworld_sft
  - eval_data: ScienceWorldSG 30 task types (dev split)
  - checkpoint_path: /root/autodl-tmp/checkpoints/scienceworld_cell_c/
  - hyperparams: {total_training_steps: 15, context_window_mode: full, env_groups: 16, group_size: 8, ppo_mini_batch_size: 8, ppo_max_token_len_per_gpu: 16384, optimizer_offload: true, lr: 1e-06, n_gpus_per_node: 2}
- **Metrics:** step_1_success: 0, step_1_pass_at_8: 0, step_1_score: 2.74, step_1_final_score: 5.44, step_1_action_valid: 0.44, completed_steps: 1/15, failure_reason: "ScienceWorld Java environment communication error: Exception while sending command"
- **Completed:** 2026-05-20T15:32:04.012Z

---

### 6. `scienceworld_grpo_cell_c_v2`
- **Status:** DONE
- **Conclusion:** failed
- **Created:** 2026-05-20T15:41:04.991Z
- **Updated:** 2026-05-20T18:23:54.294Z
- **Hypothesis:** ScienceWorld 环境下 episode-level GRPO 能避免 collapse 并学到有效策略（v2: JVM 通信加固）
- **Parent:** scienceworld_grpo_cell_c
- **Spec:**
  - command: `bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/cost-verify-agent-rl/RAGEN && WANDB_PROJECT=cost-verify-agent-rl JAVA_TOOL_OPTIONS='-Xmx4g' python train.py --config-name _scienceworld_cell_c_grpo"`
  - server: westd-47453, gpu: [cuda:2, cuda:3], pid: 920065
  - wall_clock_seconds: 9746.5, gpu_hours: 5.41
  - data_path: scienceworld (30 tasks), data_count: 128
  - model_name: qwen3_scienceworld_sft, seed: 10000
  - checkpoint_source: qwen3_scienceworld_sft
- **Metrics:** note: "Stalled at step 2 due to disk full (99%), Ray object spilling blocked. GPU 0% util for >1h50min. Killed and restarted as v3."
- **Completed:** 2026-05-20T18:23:45.449Z

---

### 7. `scienceworld_grpo_cell_c_v3`
- **Status:** DONE
- **Conclusion:** negative
- **Created:** 2026-05-20T18:23:30.854Z
- **Updated:** 2026-05-21T02:44:56.368Z
- **Hypothesis:** ScienceWorld 环境下 episode-level GRPO 能避免 collapse（v3: 磁盘清理后重启）
- **Parent:** scienceworld_grpo_cell_c_v2
- **Spec:**
  - command: `bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/cost-verify-agent-rl/RAGEN && WANDB_PROJECT=cost-verify-agent-rl python train.py --config-name _scienceworld_cell_c_grpo"`
  - server: westd-47453, gpu: [cuda:2, cuda:3], pid: 88226
  - wall_clock_seconds: 30077.7, gpu_hours: 16.71
  - data_path: ScienceWorldSG (30 task types), data_count: 128
  - model_name: Qwen3-1.7B (ScienceWorld SFT checkpoint), seed: 10000
  - checkpoint_source: qwen3_scienceworld_sft
  - checkpoint_path: N/A (negative, no useful checkpoint)
- **Notes:** D109 止损：step 3 success=0%, action_is_valid=9.4%(<20% 阈值), score 从 2.71 降至 0.96, reward 从 0.5 降至 0.153。趋势恶化，释放 GPU。
- **Completed:** 2026-05-21T02:44:56.370Z

---

### 8. `scienceworld_info_loss_full`
- **Status:** DONE
- **Conclusion:** failed
- **Created:** 2026-05-20T14:21:15.269Z
- **Updated:** 2026-05-20T14:33:44.987Z
- **Hypothesis:** ScienceWorld SFT model with full context at T=0 achieves significantly higher success rate than h=2, quantifying information loss (Mechanism 1) in a second environment beyond ALFWorld
- **Parent:** 8b_det_eval_full
- **Spec:**
  - command: `python3 eval_scienceworld_info_loss.py --temperature 0 --history_length -1 --max_variations 3 --tensor_parallel_size 2`
  - server: westd-47453
  - data_path: ScienceWorldSG dev split, data_count: ~90 episodes
  - model_name: qwen3_scienceworld_sft, seed: 0
  - checkpoint_source: /root/autodl-tmp/checkpoints/qwen3_scienceworld_sft/huggingface
- **Completed:** 2026-05-20T14:33:44.987Z

---

### 9. `scienceworld_info_loss_h2`
- **Status:** DONE
- **Conclusion:** killed
- **Created:** 2026-05-20T14:21:16.640Z
- **Updated:** 2026-05-20T14:36:43.490Z
- **Hypothesis:** ScienceWorld SFT model with h=2 sliding window at T=0 shows degraded performance vs full context, confirming information loss generalizes beyond ALFWorld
- **Parent:** 8b_det_eval_h2
- **Completed:** 2026-05-20T14:36:43.490Z

---

### 10. `sw_info_loss_bjb1`
- **Status:** DONE
- **Conclusion:** success
- **Created:** 2026-05-20T16:38:54.097Z
- **Updated:** 2026-05-20T19:10:24.938Z
- **Hypothesis:** ScienceWorld SFT model under h=2 windowing shows significant performance degradation vs full context (T=0 deterministic), quantifying information loss (M1) cross-environment on bjb1
- **Parent:** scienceworld_sft_eval_v2
- **Spec:**
  - command: `python eval_scienceworld_info_loss.py --checkpoint /root/autodl-tmp/checkpoints/scienceworld_sft/huggingface --history_length {-1,2} --temperature 0 --max_variations 3 --tensor_parallel_size 2`
  - server: bjb1-17606, gpu: [cuda:0, cuda:1], pid: 229078
  - wall_clock_seconds: 9082.3, gpu_hours: 5.05
  - data_path: scienceworld dev split
  - data_count: 30 task types x 3 variations = 90 episodes per condition
  - model_name: qwen3_scienceworld_sft, seed: deterministic (T=0)
  - checkpoint_source: /root/autodl-tmp/checkpoints/scienceworld_sft/huggingface
- **Metrics:** full_context_success: 0.348, h2_success: 0.045, info_loss_delta_pp: 30.3, full_episodes: 89, h2_episodes: 89, full_avg_score: 26.7, h2_avg_score: 17.4, temperature: 0, notable: "find-animal/find-living-thing/lifespan-longest+shortest: 100% full -> 0% h=2"
- **Completed:** 2026-05-20T19:10:24.938Z

---

### 11. `sw_info_loss_full_v2`
- **Status:** DONE
- **Conclusion:** failed
- **Created:** 2026-05-20T14:34:18.334Z
- **Updated:** 2026-05-20T14:36:34.122Z
- **Hypothesis:** ScienceWorld SFT model with full context at T=0 achieves significantly higher success rate than h=2, quantifying information loss (Mechanism 1) in a second environment beyond ALFWorld
- **Parent:** scienceworld_sft_eval_v2
- **Spec:**
  - command: `python eval_scienceworld_info_loss.py --checkpoint qwen3_scienceworld_sft --temperature 0 --history_length -1 --tensor_parallel_size 2 --max_model_len 16384`
  - server: westd-47453
  - data_path: ScienceWorldSG dev split, data_count: 89 episodes
  - model_name: qwen3_scienceworld_sft, seed: 0
  - checkpoint_source: /root/autodl-tmp/checkpoints/qwen3_scienceworld_sft/huggingface
  - gpu: cuda:0,1, pid: 875971
- **Completed:** 2026-05-20T14:36:34.123Z

---

**Summary:** 14 initial matches, 3 false positives (gamma sweep ALFWorld experiments matching `_sw` in `_alfworld_gamma_sweep`). 11 genuine ScienceWorld experiments:
- 2 successes: `scienceworld_sft` (SFT training), `scienceworld_sft_eval_v2` (SFT eval, 30.1% success), `sw_info_loss_bjb1` (info loss: full=34.8% vs h2=4.5%)
- 2 negative: `scienceworld_grpo_cell_a` (collapse confirmed at h=2), `scienceworld_grpo_cell_c_v3` (episode-level also collapsed)
- 4 failed: `scienceworld_grpo_cell_c` (Java error), `scienceworld_grpo_cell_c_v2` (disk full), `scienceworld_info_loss_full` (failed), `sw_info_loss_full_v2` (failed)
- 2 killed: `scienceworld_sft_eval` (killed), `scienceworld_info_loss_h2` (killed)

agentId: a81374730ba0416fe (use SendMessage with to: 'a81374730ba0416fe' to continue this agent)
&lt;usage>total_tokens: 34828
tool_uses: 5
duration_ms: 145532&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "416e4f6e-75f5-422f-b417-957d7ad15ff0",
  "tool_use_result": {
    "status": "completed",
    "prompt": "I need to extract all ScienceWorld-related experiments from a large registry JSON file. \n\nThe file is at: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-1-projects-cost-verify-agent-rl/54b94781-146b-4013-9381-11e3737077cb/tool-results/mcp-agent-ml-research-read_registry-1779420967332.txt\n\nIt's JSON with schema: {result: string}. The `result` field is itself a JSON string that needs to be parsed.\n\nSteps:\n1. Probe the structure with python to understand the nesting (type, length, keys of the parsed result)\n2. Find all experiments where exp_id, hypothesis, spec, conclusion, tags, or any text field contains \"scienceworld\", \"science_world\", \"science-world\", \"sw_\", \"_sw\", or \"ScienceWorld\"\n3. For each matching experiment, output ALL fields verbatim — especially: exp_id, status, created_at, updated_at, hypothesis, spec (including hyperparameters), conclusion, failure_reason, metrics, tags\n\nReturn the complete data for all matching experiments. Do NOT summarize — I need the raw data.",
    "agentId": "a81374730ba0416fe",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Confirmed: the 3 gamma sweep experiments are false positives — they matched `_sw` in `_alfworld_gamma_sweep_*`. The actual ScienceWorld experiments are the remaining 11.\n\nHere are all 11 genuine ScienceWorld experiments with full verbatim data:\n\n---\n\n### 1. `scienceworld_sft`\n- **Status:** DONE\n- **Conclusion:** success\n- **Created:** 2026-05-19T14:35:00.255Z\n- **Updated:** 2026-05-19T17:50:12.565Z\n- **Hypothesis:** ScienceWorld 1.7B SFT 训练，为后续 GRPO 实验提供 base checkpoint。验证 SFT 训练 pipeline 可泛化到第二个交互环境（ALFWorld 之外），支撑跨环境 RL 训练失败机制对比（Cell A vs Cell C）。数据：3592 train / 1796 val expert trajectories。\n- **Spec:**\n  - command: `bash /root/cost-verify-agent-rl/RAGEN/scripts/run_scienceworld_sft.sh`\n  - server: westd-47453\n  - gpu: [cuda:0, cuda:1, cuda:2, cuda:3]\n  - pid: 120838\n  - data_path: /root/autodl-tmp/expert_sft/scienceworld_sft_train.jsonl\n  - data_count: 3592\n  - model_name: Qwen3-1.7B\n  - seed: 42\n  - log_path: /root/autodl-tmp/wandb/\n  - checkpoint_path: /root/autodl-tmp/checkpoints/scienceworld_sft/\n  - hyperparams: {lr: 5e-6, epochs: 2, batch_size: 16, max_length: 16384, fsdp: fsdp2}\n  - wandb_run_id: dqoxg94e\n- **Metrics:** train_loss_final: 0.00318, val_loss_final: 0.01098, total_steps: 448, epochs: 2, total_train_time_s: 9319.4, checkpoint: global_step_448\n- **Completed:** 2026-05-19T17:50:12.566Z\n\n---\n\n### 2. `scienceworld_sft_eval`\n- **Status:** DONE\n- **Conclusion:** killed\n- **Created:** 2026-05-19T18:11:10.597Z\n- **Updated:** 2026-05-19T18:46:33.866Z\n- **Hypothesis:** Evaluate ScienceWorld SFT checkpoint on dev split (1796 episodes, 30 task types). Establishes SFT baseline success rate for ScienceWorld before GRPO experiments.\n- **Parent:** scienceworld_sft\n- **Spec:**\n  - command: `python /root/cost-verify-agent-rl/eval_scienceworld.py --temperature 0.4`\n  - server: bjb1-17606\n  - gpu: [cuda:0, cuda:1]\n  - pid: 183712\n  - data_path: scienceworld dev split\n  - data_count: 1796\n  - model_name: Qwen3-1.7B (ScienceWorld SFT)\n  - seed: 42\n  - checkpoint_source: scienceworld_sft/global_step_448\n  - eval_data: ScienceWorld dev split, 1796 episodes, 30 task types\n- **Completed:** 2026-05-19T18:46:33.866Z\n\n---\n\n### 3. `scienceworld_sft_eval_v2`\n- **Status:** DONE\n- **Conclusion:** success\n- **Retry count:** 1\n- **Created:** 2026-05-19T18:50:45.230Z\n- **Updated:** 2026-05-20T14:15:37.390Z\n- **Hypothesis:** SFT-trained model on ScienceWorld can achieve meaningful task completion rates across diverse science tasks, establishing a baseline for subsequent RL fine-tuning comparison.\n- **Parent:** scienceworld_sft_eval\n- **Spec:**\n  - command: `python /root/cost-verify-agent-rl/eval_scienceworld.py --temperature 0.4 --resume --episode_timeout 300`\n  - server: bjb1-17606\n  - gpu: [cuda:0, cuda:1]\n  - pid: 195853\n  - data_path: scienceworld dev split\n  - data_count: 1796\n  - model_name: Qwen3-1.7B (ScienceWorld SFT)\n  - seed: 42\n  - checkpoint_source: scienceworld_sft/global_step_448\n  - eval_data: ScienceWorld dev split, 1796 episodes, 30 task types\n  - checkpoint_path: N/A (eval only)\n- **Metrics:**\n  - total_episodes: 1796, success_count: 540, overall_success_rate: 0.301, timeouts: 0, errors: 0\n  - avg_score: 20.9, avg_steps_per_episode: 28.7, total_time_seconds: 51462\n  - Per-task breakdown (30 task types):\n    - boil: 0/7 (0%), change-the-state-of-matter-of: 1/7 (14.3%), chemistry-mix: 0/8 (0%)\n    - chemistry-mix-paint-secondary-color: 2/9 (22.2%), chemistry-mix-paint-tertiary-color: 0/9 (0%)\n    - find-animal: 37/75 (49.3%), find-living-thing: 49/75 (65.3%), find-non-living-thing: 58/75 (77.3%)\n    - find-plant: 9/75 (12%), freeze: 0/7 (0%), grow-fruit: 2/31 (6.5%), grow-plant: 0/31 (0%)\n    - identify-life-stages-1: 0/3 (0%), identify-life-stages-2: 0/2 (0%)\n    - inclined-plane-determine-angle: 7/42 (16.7%), inclined-plane-friction-named-surfaces: 83/346 (24%)\n    - inclined-plane-friction-unnamed-surfaces: 10/40 (25%), lifespan-longest-lived: 28/31 (90.3%)\n    - lifespan-longest-lived-then-shortest-lived: 28/31 (90.3%), lifespan-shortest-lived: 21/31 (67.7%)\n    - measure-melting-point-known-substance: 25/109 (22.9%), measure-melting-point-unknown-substance: 27/75 (36%)\n    - melt: 1/7 (14.3%), mendelian-genetics-known-plant: 8/30 (26.7%), mendelian-genetics-unknown-plant: 35/120 (29.2%)\n    - power-component: 3/5 (60%), power-component-renewable-vs-nonrenewable-energy: 0/5 (0%)\n    - test-conductivity: 35/225 (15.6%), test-conductivity-of-unknown-substances: 44/150 (29.3%), use-thermometer: 27/135 (20%)\n  - results_json_path: /root/autodl-tmp/checkpoints/scienceworld_sft/eval_results_dev_v2.json\n- **Previous failure:** 409/1796 episodes completed (22.8%), success_rate 0.386 at that point\n- **Completed:** 2026-05-19T23:59:54.217Z\n\n---\n\n### 4. `scienceworld_grpo_cell_a`\n- **Status:** DONE\n- **Conclusion:** negative\n- **Created:** 2026-05-20T11:24:49.171Z\n- **Updated:** 2026-05-20T13:54:57.116Z\n- **Hypothesis:** ScienceWorld 环境下 step-independent GRPO (h=2) 也会出现 policy collapse，验证 ALFWorld 观察到的 collapse 是 step-independent credit assignment 的固有问题而非环境特异性\n- **Parent:** scienceworld_sft\n- **Spec:**\n  - command: `cd /root/cost-verify-agent-rl/RAGEN && WANDB_PROJECT=cost-verify-agent-rl python train.py --config-name _scienceworld_cell_a_grpo`\n  - server: westd-47453, gpu: cuda:0,1, pid: 759987\n  - wandb_run_id: f1c4g6dk\n  - data_path: ScienceWorldSG, data_count: 30\n  - model_name: Qwen3-1.7B (ScienceWorld SFT checkpoint), seed: 42\n  - checkpoint_source: scienceworld_sft\n  - eval_data: ScienceWorldSG 30 task types (dev split)\n  - checkpoint_path: /root/autodl-tmp/checkpoints/scienceworld-cell-a/global_step_15\n  - hyperparams: {total_training_steps: 15, context_window_mode: step_independent, step_independent_history_length: 2, env_groups: 16, group_size: 8, ppo_mini_batch_size: 8, ppo_max_token_len_per_gpu: 16384, optimizer_offload: true, lr: 1e-06, n_gpus_per_node: 2}\n- **Metrics:** steps_completed: 14, success_rate: 0, final_score_train: -100, final_score_val: 1, reward_mean_start: 0.6, reward_mean_end: 0.1, entropy_start: 0.283, entropy_end: 0.52, kl_start: 1.606, kl_end: 0.03, exit_mode: abnormal (log truncated at step 15 start), note: \"collapse confirmed - success rate 0% throughout, matches ALFWorld Cell A pattern\"\n- **Completed:** 2026-05-20T13:54:57.117Z\n\n---\n\n### 5. `scienceworld_grpo_cell_c`\n- **Status:** DONE\n- **Conclusion:** failed\n- **Created:** 2026-05-20T11:24:51.574Z\n- **Updated:** 2026-05-20T15:32:10.728Z\n- **Hypothesis:** ScienceWorld 环境下 episode-level GRPO 能避免 collapse 并学到有效策略，验证 episode-level credit 作为 fix 的跨环境泛化性\n- **Parent:** scienceworld_sft\n- **Spec:**\n  - command: `cd /root/cost-verify-agent-rl/RAGEN && WANDB_PROJECT=cost-verify-agent-rl python train.py --config-name _scienceworld_cell_c_grpo`\n  - server: westd-47453, gpu: cuda:2,3, pid: 766820\n  - wandb_run_id: sx7h864t\n  - data_path: ScienceWorldSG, data_count: 30\n  - model_name: Qwen3-1.7B (ScienceWorld SFT checkpoint), seed: 42\n  - checkpoint_source: scienceworld_sft\n  - eval_data: ScienceWorldSG 30 task types (dev split)\n  - checkpoint_path: /root/autodl-tmp/checkpoints/scienceworld_cell_c/\n  - hyperparams: {total_training_steps: 15, context_window_mode: full, env_groups: 16, group_size: 8, ppo_mini_batch_size: 8, ppo_max_token_len_per_gpu: 16384, optimizer_offload: true, lr: 1e-06, n_gpus_per_node: 2}\n- **Metrics:** step_1_success: 0, step_1_pass_at_8: 0, step_1_score: 2.74, step_1_final_score: 5.44, step_1_action_valid: 0.44, completed_steps: 1/15, failure_reason: \"ScienceWorld Java environment communication error: Exception while sending command\"\n- **Completed:** 2026-05-20T15:32:04.012Z\n\n---\n\n### 6. `scienceworld_grpo_cell_c_v2`\n- **Status:** DONE\n- **Conclusion:** failed\n- **Created:** 2026-05-20T15:41:04.991Z\n- **Updated:** 2026-05-20T18:23:54.294Z\n- **Hypothesis:** ScienceWorld 环境下 episode-level GRPO 能避免 collapse 并学到有效策略（v2: JVM 通信加固）\n- **Parent:** scienceworld_grpo_cell_c\n- **Spec:**\n  - command: `bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/cost-verify-agent-rl/RAGEN && WANDB_PROJECT=cost-verify-agent-rl JAVA_TOOL_OPTIONS='-Xmx4g' python train.py --config-name _scienceworld_cell_c_grpo\"`\n  - server: westd-47453, gpu: [cuda:2, cuda:3], pid: 920065\n  - wall_clock_seconds: 9746.5, gpu_hours: 5.41\n  - data_path: scienceworld (30 tasks), data_count: 128\n  - model_name: qwen3_scienceworld_sft, seed: 10000\n  - checkpoint_source: qwen3_scienceworld_sft\n- **Metrics:** note: \"Stalled at step 2 due to disk full (99%), Ray object spilling blocked. GPU 0% util for >1h50min. Killed and restarted as v3.\"\n- **Completed:** 2026-05-20T18:23:45.449Z\n\n---\n\n### 7. `scienceworld_grpo_cell_c_v3`\n- **Status:** DONE\n- **Conclusion:** negative\n- **Created:** 2026-05-20T18:23:30.854Z\n- **Updated:** 2026-05-21T02:44:56.368Z\n- **Hypothesis:** ScienceWorld 环境下 episode-level GRPO 能避免 collapse（v3: 磁盘清理后重启）\n- **Parent:** scienceworld_grpo_cell_c_v2\n- **Spec:**\n  - command: `bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/cost-verify-agent-rl/RAGEN && WANDB_PROJECT=cost-verify-agent-rl python train.py --config-name _scienceworld_cell_c_grpo\"`\n  - server: westd-47453, gpu: [cuda:2, cuda:3], pid: 88226\n  - wall_clock_seconds: 30077.7, gpu_hours: 16.71\n  - data_path: ScienceWorldSG (30 task types), data_count: 128\n  - model_name: Qwen3-1.7B (ScienceWorld SFT checkpoint), seed: 10000\n  - checkpoint_source: qwen3_scienceworld_sft\n  - checkpoint_path: N/A (negative, no useful checkpoint)\n- **Notes:** D109 止损：step 3 success=0%, action_is_valid=9.4%(<20% 阈值), score 从 2.71 降至 0.96, reward 从 0.5 降至 0.153。趋势恶化，释放 GPU。\n- **Completed:** 2026-05-21T02:44:56.370Z\n\n---\n\n### 8. `scienceworld_info_loss_full`\n- **Status:** DONE\n- **Conclusion:** failed\n- **Created:** 2026-05-20T14:21:15.269Z\n- **Updated:** 2026-05-20T14:33:44.987Z\n- **Hypothesis:** ScienceWorld SFT model with full context at T=0 achieves significantly higher success rate than h=2, quantifying information loss (Mechanism 1) in a second environment beyond ALFWorld\n- **Parent:** 8b_det_eval_full\n- **Spec:**\n  - command: `python3 eval_scienceworld_info_loss.py --temperature 0 --history_length -1 --max_variations 3 --tensor_parallel_size 2`\n  - server: westd-47453\n  - data_path: ScienceWorldSG dev split, data_count: ~90 episodes\n  - model_name: qwen3_scienceworld_sft, seed: 0\n  - checkpoint_source: /root/autodl-tmp/checkpoints/qwen3_scienceworld_sft/huggingface\n- **Completed:** 2026-05-20T14:33:44.987Z\n\n---\n\n### 9. `scienceworld_info_loss_h2`\n- **Status:** DONE\n- **Conclusion:** killed\n- **Created:** 2026-05-20T14:21:16.640Z\n- **Updated:** 2026-05-20T14:36:43.490Z\n- **Hypothesis:** ScienceWorld SFT model with h=2 sliding window at T=0 shows degraded performance vs full context, confirming information loss generalizes beyond ALFWorld\n- **Parent:** 8b_det_eval_h2\n- **Completed:** 2026-05-20T14:36:43.490Z\n\n---\n\n### 10. `sw_info_loss_bjb1`\n- **Status:** DONE\n- **Conclusion:** success\n- **Created:** 2026-05-20T16:38:54.097Z\n- **Updated:** 2026-05-20T19:10:24.938Z\n- **Hypothesis:** ScienceWorld SFT model under h=2 windowing shows significant performance degradation vs full context (T=0 deterministic), quantifying information loss (M1) cross-environment on bjb1\n- **Parent:** scienceworld_sft_eval_v2\n- **Spec:**\n  - command: `python eval_scienceworld_info_loss.py --checkpoint /root/autodl-tmp/checkpoints/scienceworld_sft/huggingface --history_length {-1,2} --temperature 0 --max_variations 3 --tensor_parallel_size 2`\n  - server: bjb1-17606, gpu: [cuda:0, cuda:1], pid: 229078\n  - wall_clock_seconds: 9082.3, gpu_hours: 5.05\n  - data_path: scienceworld dev split\n  - data_count: 30 task types x 3 variations = 90 episodes per condition\n  - model_name: qwen3_scienceworld_sft, seed: deterministic (T=0)\n  - checkpoint_source: /root/autodl-tmp/checkpoints/scienceworld_sft/huggingface\n- **Metrics:** full_context_success: 0.348, h2_success: 0.045, info_loss_delta_pp: 30.3, full_episodes: 89, h2_episodes: 89, full_avg_score: 26.7, h2_avg_score: 17.4, temperature: 0, notable: \"find-animal/find-living-thing/lifespan-longest+shortest: 100% full -> 0% h=2\"\n- **Completed:** 2026-05-20T19:10:24.938Z\n\n---\n\n### 11. `sw_info_loss_full_v2`\n- **Status:** DONE\n- **Conclusion:** failed\n- **Created:** 2026-05-20T14:34:18.334Z\n- **Updated:** 2026-05-20T14:36:34.122Z\n- **Hypothesis:** ScienceWorld SFT model with full context at T=0 achieves significantly higher success rate than h=2, quantifying information loss (Mechanism 1) in a second environment beyond ALFWorld\n- **Parent:** scienceworld_sft_eval_v2\n- **Spec:**\n  - command: `python eval_scienceworld_info_loss.py --checkpoint qwen3_scienceworld_sft --temperature 0 --history_length -1 --tensor_parallel_size 2 --max_model_len 16384`\n  - server: westd-47453\n  - data_path: ScienceWorldSG dev split, data_count: 89 episodes\n  - model_name: qwen3_scienceworld_sft, seed: 0\n  - checkpoint_source: /root/autodl-tmp/checkpoints/qwen3_scienceworld_sft/huggingface\n  - gpu: cuda:0,1, pid: 875971\n- **Completed:** 2026-05-20T14:36:34.123Z\n\n---\n\n**Summary:** 14 initial matches, 3 false positives (gamma sweep ALFWorld experiments matching `_sw` in `_alfworld_gamma_sweep`). 11 genuine ScienceWorld experiments:\n- 2 successes: `scienceworld_sft` (SFT training), `scienceworld_sft_eval_v2` (SFT eval, 30.1% success), `sw_info_loss_bjb1` (info loss: full=34.8% vs h2=4.5%)\n- 2 negative: `scienceworld_grpo_cell_a` (collapse confirmed at h=2), `scienceworld_grpo_cell_c_v3` (episode-level also collapsed)\n- 4 failed: `scienceworld_grpo_cell_c` (Java error), `scienceworld_grpo_cell_c_v2` (disk full), `scienceworld_info_loss_full` (failed), `sw_info_loss_full_v2` (failed)\n- 2 killed: `scienceworld_sft_eval` (killed), `scienceworld_info_loss_h2` (killed)"
      }
    ],
    "totalDurationMs": 145532,
    "totalTokens": 34828,
    "totalToolUseCount": 5,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 909,
      "cache_read_input_tokens": 28248,
      "output_tokens": 5670,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 909
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5670,
          "cache_read_input_tokens": 28248,
          "cache_creation_input_tokens": 909,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 909,
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
      "bashCount": 5,
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

### System

_source line 83_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "ad21c2477dd6123aa",
  "tool_use_id": "toolu_01UvN5LYeDV9iSrVapRBHaFQ",
  "status": "completed",
  "output_file": "",
  "summary": "Extract ScienceWorld info from decisions.yaml",
  "usage": {
    "total_tokens": 35538,
    "tool_uses": 12,
    "duration_ms": 374869
  },
  "uuid": "db7ab4ed-9829-45ba-aeee-0d3fcdbfa729",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb"
}
```

---

### Tool result

_source line 84 · 2026-05-22T03:42:54.421Z_

<details><summary>↩ Tool result · `toolu_01UvN5LYeDV9iSrVapRBHaFQ`</summary>

````text
All matches are captured. Here are all 28 decision blocks from `decisions.yaml` containing ScienceWorld-related content (including Cell A/Cell C references), extracted verbatim:

---

**D068** (2026-05-18 03:52 UTC)
```yaml
- id: D068
  date: 2026-05-18 03:52 UTC
  summary: 'exp029 OOD reeval: 23.88% on 134 tasks. Information loss preliminary estimate
    17.9pp, action_is_valid insight confirms mechanism'
  rationale: 'exp029 step 15 on AlfworldOOD 134 tasks: success=23.88% (vs 28.1% on
    in-dist 32 tasks, -4pp as expected). Preliminary decomposition on unified OOD
    set: information loss (B→C) = 23.88% - 5.97% = 17.9pp. Sign misattribution (A→B)
    still missing Cell A OOD data (hsweep_h2 reeval pending). Key insight: action_is_valid
    nearly identical between factorial (57.65%) and exp029 (56.84%) despite 18pp success
    gap — full context advantage is in decision quality not action legality, supporting
    information loss mechanism narrative. Caveat: factorial only at step 5 (step mismatch)
    and KL inflating (0.24→1.77), final decomposition needs factorial step 15.'
  related_experiments:
  - exp_id: exp029_episode_level
    role: primary
    result: 23.88% OOD success
  - exp_id: factorial_h2_episodeadv_seed1
    role: comparison
    result: 5.97% OOD at step 5, KL inflating
  - exp_id: hsweep_h2_seed2
    role: pending
    result: OOD reeval needed for Cell A
  depends_on:
  - D066
  - D067
```

**D070** (2026-05-18 04:58 UTC)
```yaml
- id: D070
  date: 2026-05-18 04:58 UTC
  summary: '3-cell decomposition: information loss 89% (17.9pp) >> sign misattribution
    11% (2.2pp). Narrative rebalance needed.'
  rationale: 'OOD 134 tasks unified decomposition: Cell A (step-indep + step-level)
    3.73%, Cell B (step-indep + episode-level) 5.97%, Cell C (full context + episode-level)
    23.88%. Sign misattribution effect (A→B) = 2.24pp; information loss effect (B→C)
    = 17.91pp. Ratio ~1:8. Paper cannot claim sign misattribution as primary driver
    of performance loss. However, sign misattribution still matters for training STABILITY
    (seed1 collapse vs seed2 delayed recovery, 52% sign agreement = noisy gradient).
    Two mechanisms damage training in orthogonal dimensions: information loss limits
    WHAT you can learn (ceiling), sign misattribution determines WHETHER you learn
    (stability). CAVEAT: Cell B is step 5 only; factorial step 10-15 may change this
    ratio significantly. Step mismatch makes current decomposition preliminary.'
  related_experiments:
  - exp_id: hsweep_h2_seed2
    role: Cell A
    result: 3.73% OOD at step 15
  - exp_id: factorial_h2_episodeadv_seed1
    role: Cell B
    result: 5.97% OOD at step 5 (preliminary)
  - exp_id: exp029_episode_level
    role: Cell C
    result: 23.88% OOD at step 15
  depends_on:
  - D067
  - D068
```

**D071** (2026-05-18 05:44 UTC)
```yaml
- id: D071
  date: 2026-05-18 05:44 UTC
  summary: 'Factorial step 10 val=5.22%: sign misattribution 量化贡献降至 1.49pp (7.4%),
    接近噪声。Framing 调整方向：sign misattribution 价值在机制解释力（训练不稳定性），不在量化性能贡献。等 step 15 确认后最终定稿。'
  rationale: 'Step 10 3-cell 分解: Cell A 3.73%, Cell B 5.22%, Cell C 23.88%。Cell B-A
    差距 1.49pp ≈ 2/134 tasks, Fisher exact p >> 0.05。但 factorial 训练过程中 step 6 达 25.8%
    success（Cell A 从未超过 0%），证明消除 sign misattribution 后模型能开始学习，只是 info loss ceiling
    + KL 膨胀限制了最终 val 表现。Sign misattribution 的贡献从"量化性能"转向"机制解释"：解释 seed 间 0% vs 9.375%
    的随机性、52% sign agreement 的噪声特征。'
  related_experiments:
  - exp_id: factorial_h2_episodeadv_seed1
    role: primary
    result: step 10 val=5.22%, train peak step 6=25.8%, KL inflation 0.735→1.029
  - exp_id: hsweep_h2_seed2
    role: baseline_cell_a
    result: OOD 3.73%
  - exp_id: exp029_episode_level
    role: baseline_cell_c
    result: OOD 23.88%
  depends_on:
  - D070
  - D067
```

**D072** (2026-05-18 09:14 UTC)
```yaml
- id: D072
  date: 2026-05-18 09:14 UTC
  summary: Kill g080 (已确认坍缩) 释放 westd cuda:2,3 给 g095。Negative 结果（g050/g080 坍缩、factorial
    振荡、seed 间 variance）作为论文 diagnostic 贡献的核心内容，不当废数据处理。
  rationale: g080 step 5 val=3.125%（低于 SFT baseline 9.38%），entropy=0.185，action_valid=98.2%，完全坍缩且不可逆。继续跑无新信息，GPU
    应释放给 g095 定位 γ-cliff 临界点。同时确认叙事方向：diagnostic paper 的贡献恰恰是 failure mode 分析，negative
    结果（g050/g080 坍缩曲线、factorial 振荡 vs monotonic collapse 对比、seed 间 variance）直接变成论文
    figure/table。
  related_experiments:
  - exp_id: gsweep_g080_h5_seed1
    role: killed_for_resource
    result: val 3.125%, entropy collapse confirmed
  - exp_id: gsweep_g095_h5_seed1
    role: next_launch
    result: config ready, dry-run passed
  - exp_id: factorial_h2_episodeadv_seed1
    role: narrative_source
    result: oscillation pattern vs Cell A monotonic collapse
  depends_on:
  - D071
  - D070
```

**D073** (2026-05-18 10:22 UTC)
```yaml
- id: D073
  date: 2026-05-18 10:22 UTC
  summary: 3-cell 定量分解在 step 15 失效（Cell B=0.75% < Cell A=3.73%）。放弃 "X% info loss +
    Y% sign misattribution" 加法分解，转向定性双机制诊断：sign misattribution 杀死学习能力（Cell A 单调坍缩），info
    loss 杀死泛化能力（Cell B 能学但 OOD 崩溃），两者共同作用才导致 step-independent 失败。
  rationale: 'Factorial step 15: Cell B val OOD=0.75%, KL=2.845, val action_valid=11%。Train
    success=16.41% 但 OOD 完全崩溃，说明 truncated context 下模型 overfit 训练分布但无法泛化。3-cell 加法分解高度依赖
    checkpoint 选择（step 5: B>A, step 10: B≈A, step 15: B&lt;A），定量分解不可靠有 cherry-picking
    风险。但定性发现更丰富：(1) Cell A 单调坍缩到 0%（sign misattribution 完全阻止学习），(2) Cell B 高方差振荡后
    overfit 崩溃（episode advantage 恢复学习信号但 info loss 阻止泛化），(3) Cell C 稳定到 23.88%（两者都解决后正常学习）。这比简单的百分比分解更有洞察力。'
  related_experiments:
  - exp_id: factorial_h2_episodeadv_seed1
    role: primary
    result: step 15 val OOD=0.75%, train=16.41%, KL=2.845, 3-cell decomposition breaks
  - exp_id: hsweep_h2_seed2
    role: cell_a
    result: OOD 3.73%
  - exp_id: exp029_episode_level
    role: cell_c
    result: OOD 23.88%
  depends_on:
  - D071
  - D070
```

**D077** (2026-05-18 17:47 UTC)
```yaml
- id: D077
  date: 2026-05-18 17:47 UTC
  summary: 彻底放弃 bjb1 跑 exp029_seed2，转移到 westd。bjb1 转部署 h=20。现有 step 0-20 数据保留
  rationale: exp029_seed2 在 bjb1 累计 10+ 次失败：初始 OOM (3次)、存储 I/O crash、FSDP optimizer_offload
    bug、磁盘满 crash、vLLM stall (3.5h 空转)。每次修复后出现新问题，bjb1 对 episode-level 训练系统性不可靠。现有数据
    step 0-20 (val 37.5% at step 20) 已证明 Cell C seed2 学习能力，完整训练转移到 westd（factorial
    完成后释放 cuda:0,1）。bjb1 转部署 step_independent h=20（已验证 h=2 系列在 bjb1 上稳定）。
  related_experiments:
  - exp_id: exp029_episode_level_seed2
    role: primary
    result: 10+ failures on bjb1, val 37.5% at step 20
  - exp_id: hsweep_h20_seed1
    role: replacement
    result: pending deployment on bjb1
  depends_on:
  - D075
  - D076
```

**D080** (2026-05-19 02:16 UTC)
```yaml
- id: D080
  date: 2026-05-19 02:16 UTC
  summary: exp029_seed2 完成：val 峰值 31.25% (step 30)，稳定 28.1% (step 35-40)。Cell C 跨
    seed 确认——两 seed 均 ~28-31%，与 Cell A 崩溃和 Cell B 0.75% 形成清晰对比。Step 40 后训练已崩溃（train
    6.25%, invalid 80%），但 val 保持。Kill 释放 GPU。
  rationale: seed1 28.1%@step15, seed2 31.25%@step30, 稳定在 28.1%@step35-40。两 seed 收敛到同一量级，支撑
    "Cell C enables non-trivial learning" claim。格式退化（manager_invalid 0.8%→58%）是已知的
    extended training 问题，不影响核心 claim。继续跑无增量收益，kill 释放 westd cuda:0,1。
  related_experiments:
  - exp_id: exp029_episode_level_seed2
    role: primary
    result: val peak 31.25% (step 30), stable 28.1% (step 35-40)
  - exp_id: exp029_episode_level
    role: comparison
    result: seed1 val 28.1% (step 15), OOD 23.88%
  depends_on:
  - D078
```

**D081** (2026-05-19 03:34 UTC) -- **Key ScienceWorld decision: launch**
```yaml
- id: D081
  date: 2026-05-19 03:34 UTC
  summary: 启动 7B (Qwen3-8B) + ScienceWorld 两条并行实验线。7B 立即用 westd cuda:2,3 下载+零样本 eval；ScienceWorld
    先做 CPU 工程适配。用户明确要求"把条件性加分也做掉"。
  rationale: 用户要求做全部条件性加分实验（7B 验证 + ScienceWorld）。7B 用 Qwen3-8B（同家族，8B 参数），westd RTX
    PRO 6000 96GB 显存充裕。ScienceWorld Reviewer 要求必须用 episode total return 做 GRPO advantage，不用
    step-level intermediate reward。两条线可并行：7B 占 GPU，ScienceWorld 工程适配仅 CPU。
  related_experiments:
  - exp_id: plan_015
    role: target
    result: starting
  - exp_id: plan_014
    role: target
    result: starting
  depends_on:
  - D080
  - D078
```

**D083** (2026-05-19 07:45 UTC)
```yaml
- id: D083
  date: 2026-05-19 07:45 UTC
  summary: Qwen3-8B SFT baseline 80.6% OOD success（vs 1.7B 的 6.25%）。7B RL 实验 hypothesis
    从"RL 大幅提升"调整为"step-independent 是否仍导致退化"。核心看 Cell A 是否从 80.6% 下降 + Cell C 是否维持/小幅提升。
  rationale: SFT baseline 已 80.6%，RL 提升空间有限。但如果 step-independent 在强 baseline 上仍导致退化，反而是更有力的跨规模证据——sign
    misattribution 在任何模型规模下都是结构性问题。实验设计从"who improves more"转为"does step-independent
    still harm even strong models"。
  related_experiments:
  - exp_id: plan_015
    role: target
    result: hypothesis adjusted
  - exp_id: 7b_sft_v1
    role: evidence
    result: 80.6% OOD success
  depends_on:
  - D081
```

**D085** (2026-05-19 11:14 UTC)
```yaml
- id: D085
  date: 2026-05-19 11:14 UTC
  summary: Kill 8B Cell A at step 1, 立即启动 8B Cell C (episode-level)。Step 1 三重 collapse
    信号已足够支撑 scale-invariance claim。
  rationale: 8B Cell A step 1 数据：success 28.1%→12.5% 腰斩, entropy 0.115 ≈ 0, num_actions
    47.7/50 max out。三重 collapse 信号与 1.7B 完全一致。继续跑 4-5h 到 step 5 预期 val≈0%，边际信息增量极低。Cell
    C (episode-level 正控制) 是论文更缺的数据——同一 8B 模型、同一 80.6% SFT baseline，不同训练模式的对比远比 Cell
    A 多跑几步更有论文价值。4 GPU × 4-5h 机会成本应投入 Cell C。
  related_experiments:
  - exp_id: 7b_cell_a_h2
    role: killed
    result: 'step1 collapse: 28.1%→12.5%, entropy=0.115, scale-invariant'
  - exp_id: 8b_cell_c_episode
    role: next
    result: pending
  depends_on:
  - D083
  - D084
```

**D089** (2026-05-19 11:51 UTC) -- **Key ScienceWorld decision: experiment design**
```yaml
- id: D089
  date: 2026-05-19 11:51 UTC
  summary: 启动 ScienceWorld 实验线：用 1.7B 跑 Cell A vs Cell C 对比，解决单环境短板。mendelian-genetics
    排除。
  rationale: ScienceWorld SFT 数据 2989+ score=100 episodes（79% quality），远超 500 条阈值。mendelian-genetics
    2 个 task type 全部失败（gold path 质量问题，非模型问题），排除。ScienceWorld 用 1.7B 即可（解决单环境问题，不需要
    8B），可用 bjb1 2卡跑。8B ALFWorld Cell C 用 westd 4卡并行。Cell A vs Cell C on ScienceWorld
    是审稿人 "single environment" concern (#5) 的直接回应。
  related_experiments:
  - exp_id: 8b_cell_c_episode_v2
    role: parallel
    result: running on westd
  - exp_id: scienceworld_sft
    role: next
    result: planned for bjb1
  depends_on:
  - D085
  - D087
```

**D090** (2026-05-19 12:54 UTC)
```yaml
- id: D090
  date: 2026-05-19 12:54 UTC
  summary: 'Cell C v5: use_ref=False 释放 ref model 内存，解决 Catch-22（gpu_mem_util 0.35
    backward OOM vs 0.15 VLLM 初始化失败）'
  rationale: 4 次 OOM/失败证明 8B FSDP + optimizer + ref model 基础占用 ~90 GiB/GPU，无法在 gpu_memory_utilization
    0.15-0.35 间找到平衡点。use_ref=False 释放 ~8 GiB/GPU，允许 gpu_memory_utilization=0.20 同时满足
    VLLM 初始化和 backward 空间。代价是无 KL 约束，但验证 "episode-level 8B 能否训练" 比 KL 约束更重要。论文注明 limitation。
  related_experiments:
  - exp_id: 8b_cell_c_episode
    role: v1
    result: OOM backward
  - exp_id: 8b_cell_c_episode_v2
    role: v2
    result: OOM backward (token_len no-op)
  - exp_id: 8b_cell_c_v3
    role: v3
    result: OOM backward (mini_batch no effect)
  - exp_id: 8b_cell_c_episode_v4
    role: v4
    result: VLLM init fail (gpu_mem_util too low)
  - exp_id: 8b_cell_c_episode_v5
    role: v5
    result: 'planned: use_ref=False + gpu_mem_util=0.20'
  depends_on:
  - D085
  - D089
```

**D091** (2026-05-19 13:22 UTC)
```yaml
- id: D091
  date: 2026-05-19 13:22 UTC
  summary: 'Cell C v6: max_model_len=16384 + 移除 PYTORCH_CUDA_ALLOC_CONF。OOM 已解决（use_ref=False），v5
    新错误是 max_model_len=8192 太小（prompt 8450 tokens）+ expandable_segments 与 vLLM 不兼容'
  rationale: v5 验证了 use_ref=False + gpu_memory_utilization=0.20 组合可行（VLLM 初始化成功，FSDP
    加载正常）。max_model_len=8192 是 v4 为省 KV cache 内存降的，但 Cell C full-context mode 的 prompt
    可达 8450+ tokens。16384 匹配 max_prompt_length 配置且在 19.6 GiB VLLM 预算内可行（8B GQA 头减少了
    KV cache 需求）。PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True 与 vLLM CuMemAllocator
    冲突，必须移除。
  related_experiments:
  - exp_id: 8b_cell_c_episode_v5
    role: parent
    result: 'failed: max_model_len too small + CUDA_ALLOC incompatible'
  depends_on:
  - D090
```

**D093** (2026-05-19 13:45 UTC)
```yaml
- id: D093
  date: 2026-05-19 13:45 UTC
  summary: 'Cell C v7: gpu_memory_utilization=0.25 + max_model_len=16384。0.20 下 KV
    cache 仅 1.44 GiB（需 2.25 GiB），增到 0.25 后 KV cache ≈ 6.24 GiB（2.8x 余量）。vs 原 OOM 配置(0.35+ref)净释放
    17.6 GiB，backward 空间充足'
  rationale: KV cache 计算：gpu_mem_util=0.20 → VLLM 总 19.2 GiB，模型权重占 17.76 GiB，KV cache
    仅 1.44 GiB。gpu_mem_util=0.25 → VLLM 总 24 GiB，KV cache = 24 - 17.76 = 6.24 GiB，远超
    max_model_len=16384 所需的 2.25 GiB。Backward 空间：相比原失败配置（0.35 + ref model），0.25 少占
    9.6 GiB + ref 释放 8 GiB = 净多 17.6 GiB，backward 应无问题。不选 0.30（多给 VLLM 4.8 GiB 无必要），不选方案
    A（10240 可能在训练中遇到更长 prompt 再次失败）。
  related_experiments:
  - exp_id: 8b_cell_c_episode_v5
    role: parent
    result: 'failed: max_model_len=16384 needs 2.25 GiB KV cache, gpu_mem_util=0.20
      only provides 1.44 GiB'
  depends_on:
  - D091
  - D090
```

**D094** (2026-05-19 14:09 UTC)
```yaml
- id: D094
  date: 2026-05-19 14:09 UTC
  summary: 'Cell C v8（最后尝试）: ppo_mini_batch_size=2 + gpu_memory_utilization=0.22。v7
    backward OOM 缺 3.7 GiB。batch 4→2 约省一半激活内存，util 0.25→0.22 释放 2.88 GiB。如果 v8 仍 OOM，接受
    1.7B-only Cell C 数据，不再尝试'
  rationale: v7 数据：allocated 110.14 GiB，backward 需 8.94 GiB，可用 5.21 GiB，缺 3.7 GiB。ppo_mini_batch_size
    从 4 降到 2，backward 激活内存大约减半（~4.5 GiB）。gpu_memory_utilization 从 0.25 降到 0.22，释放
    (0.25-0.22)×96=2.88 GiB，KV cache 从 6.24 降到 3.36 GiB（仍 > 需要的 2.25 GiB）。组合后：可用 ~8.1
    GiB，需 ~4.5 GiB，余量 ~3.5 GiB。8B Cell C 连续 8 次失败已消耗大量 GPU 时间，这是最后一次尝试。论文有完整 1.7B
    Cell C 数据 + 8B Cell A collapse + 8B info loss，足够支撑 claim。
  related_experiments:
  - exp_id: 8b_cell_c_episode_v7
    role: parent
    result: 'failed: backward OOM, 110.14 GiB allocated, need 8.94 GiB, only 5.21
      GiB free'
  depends_on:
  - D093
```

**D095** (2026-05-19 14:14 UTC)
```yaml
- id: D095
  date: 2026-05-19 14:14 UTC
  summary: 正式放弃 8B Cell C：4×96GB 硬件不足以容纳 8B FSDP + VLLM + full-context backward（差
    ~4 GiB 无可调参数弥补）。论文 8B 验证限于 Cell A collapse + info loss 37.5pp。1.7B Cell C 数据完整充分
  rationale: 9 次连续失败穷尽所有配置空间。v8 暴露最后一个约束：ppo_mini_batch_size ≥ micro_batch_per_gpu(1)
    × n_gpus(4) = 4，不可再降。gpu_mem_util 0.25→0.22 仅省 2.93 GiB < 缺口 3.73 GiB。8B FSDP
    模型 + optimizer + VLLM 基线占用 ~110 GiB / 4GPU，backward 需 ~9 GiB，可用仅 ~5 GiB。根本矛盾：full-context
    episode 的长序列 backward 激活在 96GB GPU 上装不下。论文有 1.7B Cell C 完整数据（23.88% OOD, 双 seed）+
    8B Cell A collapse + 8B info loss 37.5pp + stochastic-triggered mechanism，scale
    invariance claim 已充分支撑。8B Cell C 缺失在 Limitations 说明。
  related_experiments:
  - exp_id: 8b_cell_c_episode_v7
    role: evidence
    result: 'backward OOM: 110.14 GiB allocated, need 8.94, free 5.21'
  - exp_id: 8b_cell_c_episode_v5
    role: evidence
    result: VLLM init + val_before_train passed but backward OOM
  depends_on:
  - D094
  - D093
  - D090
```

**D096** (2026-05-19 14:27 UTC)
```yaml
- id: D096
  date: 2026-05-19 14:27 UTC
  summary: 'D096: 尝试 FSDP CPU Offload 解决 8B Cell C backward OOM'
  rationale: 用户批准"试一下，不行再加卡"。v7 backward OOM 缺口 3.7 GiB，CPU Offload 可省 ~8 GiB/卡，理论上绰绰有余。改动最小（只需修改
    FSDP config 加 CPUOffload），不需要改 RAGEN 代码。如果失败，用户同意租更多 GPU。
  related_experiments:
  - exp_id: 8b_cell_c_episode_v7
    role: predecessor
    result: backward OOM, gap 3.7 GiB
  - exp_id: 8b_cell_c_episode_v8
    role: predecessor
    result: config constraint violation
  depends_on:
  - D095
```

**D097** (2026-05-19 18:17 UTC)
```yaml
- id: D097
  date: 2026-05-19 18:17 UTC
  summary: 'D097: 8B Cell C v9 (FSDP2 CPUOffload) 失败——RAGEN GRPO train.py 不支持 FSDP2'
  rationale: 'v9 启动后立即 NotImplementedError: RAGEN TaskRunner.run() 未实现 FSDP2 strategy。SFT
    能用 FSDP2 是因为走 verl 原生 fsdp_sft_trainer，但 GRPO 走 RAGEN 自有代码。D096 的前提（只需改 config）不成立。回到用户决策：加卡还是接受
    1.7B-only。'
  related_experiments:
  - exp_id: 8b_cell_c_v9
    role: failed
    result: 'NotImplementedError: RAGEN GRPO 不支持 FSDP2'
  depends_on:
  - D096
  - D095
```

**D099** (2026-05-19 20:13 UTC)
```yaml
- id: D099
  date: 2026-05-19 20:13 UTC
  summary: 'D099: 8B Cell C v9c backward pass 成功——FSDP2+CPUOffload 方案可行，8B Cell C
    解锁'
  rationale: v9c 完成 step 1/30 backward pass 无 OOM。FSDP2+CPUOffload 将峰值显存从 91 GB 降至
    83 GB/卡（余量 12 GB），10 次修复（5 文件 10 处 FSDP1→FSDP2 兼容）全部生效。预计 15-16h 完成 30 steps 训练。不需要租卡。
  related_experiments:
  - exp_id: 8b_cell_c_v9c
    role: running
    result: step 1/30 完成, backward pass 无 OOM, 83 GB/卡
  depends_on:
  - D098
  - D097
  - D096
```

**D102** (2026-05-20 08:05 UTC)
```yaml
- id: D102
  date: 2026-05-20 08:05 UTC
  summary: v9d 暂停训练，转向 step 10 OOD eval——8+ 次崩溃指向系统性不稳定，step 10 val=96.875% 数据已足够强
  rationale: v9d 从 step 5 到 step 11 训练正常（success 81→97%），但 8+ 次崩溃覆盖磁盘满/model_path
    误删/vLLM OOM/SIGHUP/静默死亡多种 failure mode，指向 FSDP2+CPUOffload+4卡 8B 在 westd 上的系统性不稳定。继续重启大概率继续崩。step
    10 val=96.875% vs Cell A 1.5% 的对比已足够支撑跨尺度 claim。先做 OOD eval 拿论文数据，同时诊断根因决定是否值得继续训练到
    step 30。
  related_experiments:
  - exp_id: 8b_cell_c_episode_v9d
    role: target
    result: step 10 val 96.875%, 8+ crashes
  depends_on:
  - D101
```

**D103** (2026-05-20 09:24 UTC)
```yaml
- id: D103
  date: 2026-05-20 09:24 UTC
  summary: v9d step 15 后停止训练——step 12 起 GRPO reward 饱和（100% success, pg_loss=0），继续训练无信号。转向
    OOD eval
  rationale: Step 12 完整 metrics：train success 1.0，critic score 全 10.0，advantages 全
    0，pg_loss=0，grad_norm 0.022。GRPO 依赖 group 内 reward 差异，全组成功则 advantage normalization
    为零。Step 12→30 模型权重不会变化（除 entropy drift），等效 GPU 空转。OOD eval 是论文关键数据，step 10/15
    checkpoint 已可评估。停训练后释放 westd 4×GPU 用于 OOD eval + 可能的 ScienceWorld GRPO。
  related_experiments:
  - exp_id: 8b_cell_c_episode_v9d
    role: target
    result: step 12 reward saturation, 100% in-dist success
  depends_on:
  - D102
```

**D104** (2026-05-20 12:14 UTC)
```yaml
- id: D104
  date: 2026-05-20 12:14 UTC
  summary: Claim 1 升级：从 "unstable/fragile" 升级为 "systematic failure mechanism, scale-invariant"
    + "necessary minimum fix"。不用 "catastrophic"（1.7B seed2 学了 9.375%）
  rationale: Reviewer 独立评估：8B Cell C 90.3% + Cell A 1.5% 跨尺度对比、γ-sweep 全坍缩、factorial
    2×2 全部验证——证据强度已超出 D067 降级时的 "unstable/fragile"。新表述：systematic + scale-invariant
    failure mechanism，episode-level 是 necessary minimum fix（不 claim optimal，承认 GAGPO
    等更优）。保留 stochastically triggered 解释社区为何未普遍注意。最大风险：R1(trivial fix)+R2(无 fine-grained
    baseline) 组合攻击——Practitioner Decision Tree 在 Discussion 中可部分缓解。
  related_experiments:
  - exp_id: 8b_cell_c_episode_v9d
    role: key_evidence
    result: 90.3% OOD
  - exp_id: 7b_cell_a_h2
    role: key_evidence
    result: 1.5% collapse
  - exp_id: gsweep_g100_h5_seed1
    role: supporting
    result: γ=1.0 collapse
  depends_on:
  - D067
  - D103
```

**D105** (2026-05-20 13:26 UTC) -- **Key ScienceWorld decision: scenario planning**
```yaml
- id: D105
  date: 2026-05-20 13:26 UTC
  summary: ScienceWorld GRPO 三场景预案：(1) Cell A collapse + Cell C learns = 最强; (2) 两者都不学
    = diagnosis 仍成立，fix 加限定语; (3) Cell A 不 collapse = 可解释为 "nothing to destroy at
    0% baseline"。核心结论：ScienceWorld 是 bonus，不是 load-bearing
  rationale: Reviewer 独立评估：三个场景概率 40%/35%/25%。无论哪个场景，ALFWorld 的跨尺度证据（1.7B + 8B）+ factorial
    + γ-sweep 已足够 EMNLP ≥ 4.0。ScienceWorld Cell A val_before_train = 0% 使场景 3 有合理解释（sign
    misattribution 破坏的是 existing capability，0% baseline 无东西可破坏）。关键诊断指标不仅是 pass@1，还有
    entropy/KL 轨迹（区分 active destruction vs no signal）。场景 2 需提前准备 Limitations 段 "capacity
    vs credit" 讨论。
  related_experiments:
  - exp_id: scienceworld_grpo_cell_a
    role: pending
    result: running
  - exp_id: scienceworld_grpo_cell_c
    role: pending
    result: running
  depends_on:
  - D104
```

**D106** (2026-05-20 13:49 UTC) -- **Key ScienceWorld result: Cell A collapse confirmed**
```yaml
- id: D106
  date: 2026-05-20 13:49 UTC
  summary: ScienceWorld Cell A 崩溃确认：final_score 6.0→-100.0，比 ALFWorld 更极端。D105 场景
    1 上半部成立——failure mechanism 跨环境验证完成
  rationale: Cell A (step-independent h=2) 在 ScienceWorld 15 步全程 0% success，final_score
    降至 -100.0（ALFWorld 不会负分）。entropy 上升+KL 崩塌模式与 ALFWorld 一致。ScienceWorld 任务结构（科学推理、长
    horizon）与 ALFWorld（家务）完全不同，排除环境特异性。等 Cell C 结果完成场景 1 判断。Reviewer 风险 R3 (single
    env) 基本解决。
  related_experiments:
  - exp_id: scienceworld_grpo_cell_a
    role: key_evidence
    result: collapse confirmed, final_score -100.0
  - exp_id: scienceworld_grpo_cell_c
    role: pending
    result: 1/15 steps, ~7h
  depends_on:
  - D105
```

**D107** (2026-05-20 15:34 UTC) -- **ScienceWorld Cell C Java crashes**
```yaml
- id: D107
  date: 2026-05-20 15:34 UTC
  summary: ScienceWorld Cell C 崩溃（第3次 Java 异常）：最后重试一次加固版，不阻塞论文压缩
  rationale: ScienceWorld Java 环境三次崩溃（Info Loss Eval ×2 + Cell C ×1），root cause 是
    Java IPC 通信异常。Cell A collapse 已确认（D106），跨环境 failure 证据充分。Cell C（episode-level
    fix 跨环境验证）是 nice-to-have 而非 must-have——论文核心 claim 不依赖它。策略：(1) 最后重试一次，Agent 先调查
    Java 异常并加固；(2) Paper Agent 立即推进 16→8 页压缩，不等 Cell C；(3) 若再次崩溃则接受现有数据，Limitations
    如实说明。
  related_experiments:
  - exp_id: scienceworld_grpo_cell_c
    role: subject
    result: DONE(failed) — Java IPC crash after step 1
  - exp_id: scienceworld_grpo_cell_a
    role: evidence
    result: DONE(negative) — collapse confirmed, cross-env failure validated
  depends_on:
  - D105
  - D106
```

**D108** (2026-05-21 01:48 UTC) -- **ScienceWorld Cell C v3 also collapses**
```yaml
- id: D108
  date: 2026-05-21 01:48 UTC
  summary: Seed 3 OOD 10.45% (vs Seed 1 23.88%)：Table 1 报 mean[range]，Limitations
    加 seed variance 说明。Cell C v3 ScienceWorld episode-level 坍塌：继续观察到 step 5，不影响当前
    claim（论文只 claim collapse generalizes，不 claim fix generalizes）
  rationale: Seed 3 OOD 差异统计显著 (z=2.91, p<0.005)，但均值 17.2% 仍高于 SFT baseline 12.5%，核心
    claim "episode-level avoids collapse and enables learning" 两 seed 都成立。Cell C v3
    step 2 reward saturation（128 trajectories 全零 reward），与 Section 3 reward saturation
    分析一致——ScienceWorld 更难，episode-level 不能解决 reward saturation。论文已谨慎措辞，只需加 Limitations。
  related_experiments:
  - exp_id: exp029_seed3_ood_v2
    role: seed3 OOD eval
    result: 10.45% (14/134)
  - exp_id: exp029_episode_level
    role: seed1 OOD baseline
    result: 23.88% (32/134)
  - exp_id: scienceworld_grpo_cell_c_v3
    role: SW episode-level fix
    result: collapsing at step 2
  depends_on:
  - D104
  - D106
```

**D109** (2026-05-21 02:41 UTC) -- **ScienceWorld Cell C terminated**
```yaml
- id: D109
  date: 2026-05-21 02:41 UTC
  summary: Cell C v3 提前终止（step 3），释放 westd cuda:2,3；启动 seed 5 并行训练（westd cuda:0,1）
  rationale: Cell C v3 step 3 已满足止损条件（success=0%, action_is_valid=9.4%<20%），且趋势持续恶化（score
    2.71→0.96, reward 0.5→0.153），等 step 5 只浪费 ~10 GPU-hours。论文 Limitations 段用 step
    3 数据即可。释放的 GPU 加上已空闲的 cuda:0,1，启动 seed 5 并行训练——与 bjb1 seed 4 同时跑，最终 4 个 seed 的
    OOD 数据统计可靠性远优于 3 个。当前 2-seed OOD variance 大（10.4% vs 23.9%），4 seeds 可报 mean±std，审稿人信服度显著提升。
  related_experiments:
  - exp_id: scienceworld_grpo_cell_c_v3
    role: terminated
    result: 'negative: 3 steps 0% success, collapse confirmed'
  - exp_id: exp029_seed4
    role: parallel_seed
    result: training on bjb1
  depends_on:
  - D107
  - D108
```

**D120** (2026-05-22 03:34 UTC) -- **ScienceWorld elevated to P0**
```yaml
- id: D120
  date: 2026-05-22 03:34 UTC
  summary: 接受 Reviewer 叙事建议：干预实验降级为 Discussion，核心 claim 聚焦双机制诊断 + factorial + 8B scale；ScienceWorld
    跨环境验证升为 P0
  rationale: Reviewer 审查结论：(1) Claim 1（双机制诊断）证据 VERY STRONG，足够支撑核心贡献；(2) 干预失败/response
    inflation/mode shift 证据不足作 core claim（N=1、训练步数混杂、C' 实现 bug）；(3) 无 ScienceWorld
    预估 3.0-3.5（Findings），补齐后 3.5-4.0（Conference）。ScienceWorld 是达到 EMNLP 2026 Overall
    ≥4 的关键门槛。干预实验放 Discussion/Observations，不稀释核心贡献。seed_2048 step 1-2 即崩溃（resp_len
    15511, success 0.78%），无法提供 healthy baseline，但更新 collapse rate 至 4/7=57%。
  related_experiments:
  - exp_id: exp029_new_seed_2048
    role: observation
    result: collapsing at step 1-2, resp_len=15865, cannot serve as healthy baseline
  - exp_id: exp029_c_prime_resume_mt50_v2
    role: parent
    result: negative, cap ineffective
  depends_on:
  - D119
```

---

**Summary of all 28 decision blocks**: D068, D070, D071, D072, D073, D077, D080, D081, D083, D085, D089, D090, D091, D093, D094, D095, D096, D097, D099, D102, D103, D104, D105, D106, D107, D108, D109, D120.

The **directly ScienceWorld-focused** decisions are: D081 (launch), D089 (experiment design), D105 (scenario planning), D106 (Cell A collapse confirmed), D107 (Cell C Java crashes), D108 (Cell C v3 collapses), D109 (Cell C terminated), D120 (ScienceWorld elevated to P0). The remaining decisions reference Cell A/Cell C in the ALFWorld/8B context.

agentId: ad21c2477dd6123aa (use SendMessage with to: 'ad21c2477dd6123aa' to continue this agent)
&lt;usage>total_tokens: 47749
tool_uses: 12
duration_ms: 374870&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "b4d613de-50fc-4986-909e-02d97eb6bc8e",
  "tool_use_result": {
    "status": "completed",
    "prompt": "I need to extract all ScienceWorld-related content from a large decisions.yaml file.\n\nThe file is at: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-1-projects-cost-verify-agent-rl/54b94781-146b-4013-9381-11e3737077cb/tool-results/mcp-agent-ml-research-read_project_file-1779420982565.txt\n\nIt's JSON with schema: {result: string}. The `result` field is itself a JSON string containing the YAML content.\n\nSteps:\n1. Parse the JSON to get the YAML content string\n2. Search through the content for any mentions of \"ScienceWorld\", \"scienceworld\", \"science_world\", \"sw_\", \"Cell A\", \"Cell C\" (these are experiment cells that may involve ScienceWorld)\n3. Extract all relevant sections/decisions verbatim\n\nReturn all matching content verbatim. I need the full context around each mention.",
    "agentId": "ad21c2477dd6123aa",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "All matches are captured. Here are all 28 decision blocks from `decisions.yaml` containing ScienceWorld-related content (including Cell A/Cell C references), extracted verbatim:\n\n---\n\n**D068** (2026-05-18 03:52 UTC)\n```yaml\n- id: D068\n  date: 2026-05-18 03:52 UTC\n  summary: 'exp029 OOD reeval: 23.88% on 134 tasks. Information loss preliminary estimate\n    17.9pp, action_is_valid insight confirms mechanism'\n  rationale: 'exp029 step 15 on AlfworldOOD 134 tasks: success=23.88% (vs 28.1% on\n    in-dist 32 tasks, -4pp as expected). Preliminary decomposition on unified OOD\n    set: information loss (B→C) = 23.88% - 5.97% = 17.9pp. Sign misattribution (A→B)\n    still missing Cell A OOD data (hsweep_h2 reeval pending). Key insight: action_is_valid\n    nearly identical between factorial (57.65%) and exp029 (56.84%) despite 18pp success\n    gap — full context advantage is in decision quality not action legality, supporting\n    information loss mechanism narrative. Caveat: factorial only at step 5 (step mismatch)\n    and KL inflating (0.24→1.77), final decomposition needs factorial step 15.'\n  related_experiments:\n  - exp_id: exp029_episode_level\n    role: primary\n    result: 23.88% OOD success\n  - exp_id: factorial_h2_episodeadv_seed1\n    role: comparison\n    result: 5.97% OOD at step 5, KL inflating\n  - exp_id: hsweep_h2_seed2\n    role: pending\n    result: OOD reeval needed for Cell A\n  depends_on:\n  - D066\n  - D067\n```\n\n**D070** (2026-05-18 04:58 UTC)\n```yaml\n- id: D070\n  date: 2026-05-18 04:58 UTC\n  summary: '3-cell decomposition: information loss 89% (17.9pp) >> sign misattribution\n    11% (2.2pp). Narrative rebalance needed.'\n  rationale: 'OOD 134 tasks unified decomposition: Cell A (step-indep + step-level)\n    3.73%, Cell B (step-indep + episode-level) 5.97%, Cell C (full context + episode-level)\n    23.88%. Sign misattribution effect (A→B) = 2.24pp; information loss effect (B→C)\n    = 17.91pp. Ratio ~1:8. Paper cannot claim sign misattribution as primary driver\n    of performance loss. However, sign misattribution still matters for training STABILITY\n    (seed1 collapse vs seed2 delayed recovery, 52% sign agreement = noisy gradient).\n    Two mechanisms damage training in orthogonal dimensions: information loss limits\n    WHAT you can learn (ceiling), sign misattribution determines WHETHER you learn\n    (stability). CAVEAT: Cell B is step 5 only; factorial step 10-15 may change this\n    ratio significantly. Step mismatch makes current decomposition preliminary.'\n  related_experiments:\n  - exp_id: hsweep_h2_seed2\n    role: Cell A\n    result: 3.73% OOD at step 15\n  - exp_id: factorial_h2_episodeadv_seed1\n    role: Cell B\n    result: 5.97% OOD at step 5 (preliminary)\n  - exp_id: exp029_episode_level\n    role: Cell C\n    result: 23.88% OOD at step 15\n  depends_on:\n  - D067\n  - D068\n```\n\n**D071** (2026-05-18 05:44 UTC)\n```yaml\n- id: D071\n  date: 2026-05-18 05:44 UTC\n  summary: 'Factorial step 10 val=5.22%: sign misattribution 量化贡献降至 1.49pp (7.4%),\n    接近噪声。Framing 调整方向：sign misattribution 价值在机制解释力（训练不稳定性），不在量化性能贡献。等 step 15 确认后最终定稿。'\n  rationale: 'Step 10 3-cell 分解: Cell A 3.73%, Cell B 5.22%, Cell C 23.88%。Cell B-A\n    差距 1.49pp ≈ 2/134 tasks, Fisher exact p >> 0.05。但 factorial 训练过程中 step 6 达 25.8%\n    success（Cell A 从未超过 0%），证明消除 sign misattribution 后模型能开始学习，只是 info loss ceiling\n    + KL 膨胀限制了最终 val 表现。Sign misattribution 的贡献从\"量化性能\"转向\"机制解释\"：解释 seed 间 0% vs 9.375%\n    的随机性、52% sign agreement 的噪声特征。'\n  related_experiments:\n  - exp_id: factorial_h2_episodeadv_seed1\n    role: primary\n    result: step 10 val=5.22%, train peak step 6=25.8%, KL inflation 0.735→1.029\n  - exp_id: hsweep_h2_seed2\n    role: baseline_cell_a\n    result: OOD 3.73%\n  - exp_id: exp029_episode_level\n    role: baseline_cell_c\n    result: OOD 23.88%\n  depends_on:\n  - D070\n  - D067\n```\n\n**D072** (2026-05-18 09:14 UTC)\n```yaml\n- id: D072\n  date: 2026-05-18 09:14 UTC\n  summary: Kill g080 (已确认坍缩) 释放 westd cuda:2,3 给 g095。Negative 结果（g050/g080 坍缩、factorial\n    振荡、seed 间 variance）作为论文 diagnostic 贡献的核心内容，不当废数据处理。\n  rationale: g080 step 5 val=3.125%（低于 SFT baseline 9.38%），entropy=0.185，action_valid=98.2%，完全坍缩且不可逆。继续跑无新信息，GPU\n    应释放给 g095 定位 γ-cliff 临界点。同时确认叙事方向：diagnostic paper 的贡献恰恰是 failure mode 分析，negative\n    结果（g050/g080 坍缩曲线、factorial 振荡 vs monotonic collapse 对比、seed 间 variance）直接变成论文\n    figure/table。\n  related_experiments:\n  - exp_id: gsweep_g080_h5_seed1\n    role: killed_for_resource\n    result: val 3.125%, entropy collapse confirmed\n  - exp_id: gsweep_g095_h5_seed1\n    role: next_launch\n    result: config ready, dry-run passed\n  - exp_id: factorial_h2_episodeadv_seed1\n    role: narrative_source\n    result: oscillation pattern vs Cell A monotonic collapse\n  depends_on:\n  - D071\n  - D070\n```\n\n**D073** (2026-05-18 10:22 UTC)\n```yaml\n- id: D073\n  date: 2026-05-18 10:22 UTC\n  summary: 3-cell 定量分解在 step 15 失效（Cell B=0.75% < Cell A=3.73%）。放弃 \"X% info loss +\n    Y% sign misattribution\" 加法分解，转向定性双机制诊断：sign misattribution 杀死学习能力（Cell A 单调坍缩），info\n    loss 杀死泛化能力（Cell B 能学但 OOD 崩溃），两者共同作用才导致 step-independent 失败。\n  rationale: 'Factorial step 15: Cell B val OOD=0.75%, KL=2.845, val action_valid=11%。Train\n    success=16.41% 但 OOD 完全崩溃，说明 truncated context 下模型 overfit 训练分布但无法泛化。3-cell 加法分解高度依赖\n    checkpoint 选择（step 5: B>A, step 10: B≈A, step 15: B&lt;A），定量分解不可靠有 cherry-picking\n    风险。但定性发现更丰富：(1) Cell A 单调坍缩到 0%（sign misattribution 完全阻止学习），(2) Cell B 高方差振荡后\n    overfit 崩溃（episode advantage 恢复学习信号但 info loss 阻止泛化），(3) Cell C 稳定到 23.88%（两者都解决后正常学习）。这比简单的百分比分解更有洞察力。'\n  related_experiments:\n  - exp_id: factorial_h2_episodeadv_seed1\n    role: primary\n    result: step 15 val OOD=0.75%, train=16.41%, KL=2.845, 3-cell decomposition breaks\n  - exp_id: hsweep_h2_seed2\n    role: cell_a\n    result: OOD 3.73%\n  - exp_id: exp029_episode_level\n    role: cell_c\n    result: OOD 23.88%\n  depends_on:\n  - D071\n  - D070\n```\n\n**D077** (2026-05-18 17:47 UTC)\n```yaml\n- id: D077\n  date: 2026-05-18 17:47 UTC\n  summary: 彻底放弃 bjb1 跑 exp029_seed2，转移到 westd。bjb1 转部署 h=20。现有 step 0-20 数据保留\n  rationale: exp029_seed2 在 bjb1 累计 10+ 次失败：初始 OOM (3次)、存储 I/O crash、FSDP optimizer_offload\n    bug、磁盘满 crash、vLLM stall (3.5h 空转)。每次修复后出现新问题，bjb1 对 episode-level 训练系统性不可靠。现有数据\n    step 0-20 (val 37.5% at step 20) 已证明 Cell C seed2 学习能力，完整训练转移到 westd（factorial\n    完成后释放 cuda:0,1）。bjb1 转部署 step_independent h=20（已验证 h=2 系列在 bjb1 上稳定）。\n  related_experiments:\n  - exp_id: exp029_episode_level_seed2\n    role: primary\n    result: 10+ failures on bjb1, val 37.5% at step 20\n  - exp_id: hsweep_h20_seed1\n    role: replacement\n    result: pending deployment on bjb1\n  depends_on:\n  - D075\n  - D076\n```\n\n**D080** (2026-05-19 02:16 UTC)\n```yaml\n- id: D080\n  date: 2026-05-19 02:16 UTC\n  summary: exp029_seed2 完成：val 峰值 31.25% (step 30)，稳定 28.1% (step 35-40)。Cell C 跨\n    seed 确认——两 seed 均 ~28-31%，与 Cell A 崩溃和 Cell B 0.75% 形成清晰对比。Step 40 后训练已崩溃（train\n    6.25%, invalid 80%），但 val 保持。Kill 释放 GPU。\n  rationale: seed1 28.1%@step15, seed2 31.25%@step30, 稳定在 28.1%@step35-40。两 seed 收敛到同一量级，支撑\n    \"Cell C enables non-trivial learning\" claim。格式退化（manager_invalid 0.8%→58%）是已知的\n    extended training 问题，不影响核心 claim。继续跑无增量收益，kill 释放 westd cuda:0,1。\n  related_experiments:\n  - exp_id: exp029_episode_level_seed2\n    role: primary\n    result: val peak 31.25% (step 30), stable 28.1% (step 35-40)\n  - exp_id: exp029_episode_level\n    role: comparison\n    result: seed1 val 28.1% (step 15), OOD 23.88%\n  depends_on:\n  - D078\n```\n\n**D081** (2026-05-19 03:34 UTC) -- **Key ScienceWorld decision: launch**\n```yaml\n- id: D081\n  date: 2026-05-19 03:34 UTC\n  summary: 启动 7B (Qwen3-8B) + ScienceWorld 两条并行实验线。7B 立即用 westd cuda:2,3 下载+零样本 eval；ScienceWorld\n    先做 CPU 工程适配。用户明确要求\"把条件性加分也做掉\"。\n  rationale: 用户要求做全部条件性加分实验（7B 验证 + ScienceWorld）。7B 用 Qwen3-8B（同家族，8B 参数），westd RTX\n    PRO 6000 96GB 显存充裕。ScienceWorld Reviewer 要求必须用 episode total return 做 GRPO advantage，不用\n    step-level intermediate reward。两条线可并行：7B 占 GPU，ScienceWorld 工程适配仅 CPU。\n  related_experiments:\n  - exp_id: plan_015\n    role: target\n    result: starting\n  - exp_id: plan_014\n    role: target\n    result: starting\n  depends_on:\n  - D080\n  - D078\n```\n\n**D083** (2026-05-19 07:45 UTC)\n```yaml\n- id: D083\n  date: 2026-05-19 07:45 UTC\n  summary: Qwen3-8B SFT baseline 80.6% OOD success（vs 1.7B 的 6.25%）。7B RL 实验 hypothesis\n    从\"RL 大幅提升\"调整为\"step-independent 是否仍导致退化\"。核心看 Cell A 是否从 80.6% 下降 + Cell C 是否维持/小幅提升。\n  rationale: SFT baseline 已 80.6%，RL 提升空间有限。但如果 step-independent 在强 baseline 上仍导致退化，反而是更有力的跨规模证据——sign\n    misattribution 在任何模型规模下都是结构性问题。实验设计从\"who improves more\"转为\"does step-independent\n    still harm even strong models\"。\n  related_experiments:\n  - exp_id: plan_015\n    role: target\n    result: hypothesis adjusted\n  - exp_id: 7b_sft_v1\n    role: evidence\n    result: 80.6% OOD success\n  depends_on:\n  - D081\n```\n\n**D085** (2026-05-19 11:14 UTC)\n```yaml\n- id: D085\n  date: 2026-05-19 11:14 UTC\n  summary: Kill 8B Cell A at step 1, 立即启动 8B Cell C (episode-level)。Step 1 三重 collapse\n    信号已足够支撑 scale-invariance claim。\n  rationale: 8B Cell A step 1 数据：success 28.1%→12.5% 腰斩, entropy 0.115 ≈ 0, num_actions\n    47.7/50 max out。三重 collapse 信号与 1.7B 完全一致。继续跑 4-5h 到 step 5 预期 val≈0%，边际信息增量极低。Cell\n    C (episode-level 正控制) 是论文更缺的数据——同一 8B 模型、同一 80.6% SFT baseline，不同训练模式的对比远比 Cell\n    A 多跑几步更有论文价值。4 GPU × 4-5h 机会成本应投入 Cell C。\n  related_experiments:\n  - exp_id: 7b_cell_a_h2\n    role: killed\n    result: 'step1 collapse: 28.1%→12.5%, entropy=0.115, scale-invariant'\n  - exp_id: 8b_cell_c_episode\n    role: next\n    result: pending\n  depends_on:\n  - D083\n  - D084\n```\n\n**D089** (2026-05-19 11:51 UTC) -- **Key ScienceWorld decision: experiment design**\n```yaml\n- id: D089\n  date: 2026-05-19 11:51 UTC\n  summary: 启动 ScienceWorld 实验线：用 1.7B 跑 Cell A vs Cell C 对比，解决单环境短板。mendelian-genetics\n    排除。\n  rationale: ScienceWorld SFT 数据 2989+ score=100 episodes（79% quality），远超 500 条阈值。mendelian-genetics\n    2 个 task type 全部失败（gold path 质量问题，非模型问题），排除。ScienceWorld 用 1.7B 即可（解决单环境问题，不需要\n    8B），可用 bjb1 2卡跑。8B ALFWorld Cell C 用 westd 4卡并行。Cell A vs Cell C on ScienceWorld\n    是审稿人 \"single environment\" concern (#5) 的直接回应。\n  related_experiments:\n  - exp_id: 8b_cell_c_episode_v2\n    role: parallel\n    result: running on westd\n  - exp_id: scienceworld_sft\n    role: next\n    result: planned for bjb1\n  depends_on:\n  - D085\n  - D087\n```\n\n**D090** (2026-05-19 12:54 UTC)\n```yaml\n- id: D090\n  date: 2026-05-19 12:54 UTC\n  summary: 'Cell C v5: use_ref=False 释放 ref model 内存，解决 Catch-22（gpu_mem_util 0.35\n    backward OOM vs 0.15 VLLM 初始化失败）'\n  rationale: 4 次 OOM/失败证明 8B FSDP + optimizer + ref model 基础占用 ~90 GiB/GPU，无法在 gpu_memory_utilization\n    0.15-0.35 间找到平衡点。use_ref=False 释放 ~8 GiB/GPU，允许 gpu_memory_utilization=0.20 同时满足\n    VLLM 初始化和 backward 空间。代价是无 KL 约束，但验证 \"episode-level 8B 能否训练\" 比 KL 约束更重要。论文注明 limitation。\n  related_experiments:\n  - exp_id: 8b_cell_c_episode\n    role: v1\n    result: OOM backward\n  - exp_id: 8b_cell_c_episode_v2\n    role: v2\n    result: OOM backward (token_len no-op)\n  - exp_id: 8b_cell_c_v3\n    role: v3\n    result: OOM backward (mini_batch no effect)\n  - exp_id: 8b_cell_c_episode_v4\n    role: v4\n    result: VLLM init fail (gpu_mem_util too low)\n  - exp_id: 8b_cell_c_episode_v5\n    role: v5\n    result: 'planned: use_ref=False + gpu_mem_util=0.20'\n  depends_on:\n  - D085\n  - D089\n```\n\n**D091** (2026-05-19 13:22 UTC)\n```yaml\n- id: D091\n  date: 2026-05-19 13:22 UTC\n  summary: 'Cell C v6: max_model_len=16384 + 移除 PYTORCH_CUDA_ALLOC_CONF。OOM 已解决（use_ref=False），v5\n    新错误是 max_model_len=8192 太小（prompt 8450 tokens）+ expandable_segments 与 vLLM 不兼容'\n  rationale: v5 验证了 use_ref=False + gpu_memory_utilization=0.20 组合可行（VLLM 初始化成功，FSDP\n    加载正常）。max_model_len=8192 是 v4 为省 KV cache 内存降的，但 Cell C full-context mode 的 prompt\n    可达 8450+ tokens。16384 匹配 max_prompt_length 配置且在 19.6 GiB VLLM 预算内可行（8B GQA 头减少了\n    KV cache 需求）。PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True 与 vLLM CuMemAllocator\n    冲突，必须移除。\n  related_experiments:\n  - exp_id: 8b_cell_c_episode_v5\n    role: parent\n    result: 'failed: max_model_len too small + CUDA_ALLOC incompatible'\n  depends_on:\n  - D090\n```\n\n**D093** (2026-05-19 13:45 UTC)\n```yaml\n- id: D093\n  date: 2026-05-19 13:45 UTC\n  summary: 'Cell C v7: gpu_memory_utilization=0.25 + max_model_len=16384。0.20 下 KV\n    cache 仅 1.44 GiB（需 2.25 GiB），增到 0.25 后 KV cache ≈ 6.24 GiB（2.8x 余量）。vs 原 OOM 配置(0.35+ref)净释放\n    17.6 GiB，backward 空间充足'\n  rationale: KV cache 计算：gpu_mem_util=0.20 → VLLM 总 19.2 GiB，模型权重占 17.76 GiB，KV cache\n    仅 1.44 GiB。gpu_mem_util=0.25 → VLLM 总 24 GiB，KV cache = 24 - 17.76 = 6.24 GiB，远超\n    max_model_len=16384 所需的 2.25 GiB。Backward 空间：相比原失败配置（0.35 + ref model），0.25 少占\n    9.6 GiB + ref 释放 8 GiB = 净多 17.6 GiB，backward 应无问题。不选 0.30（多给 VLLM 4.8 GiB 无必要），不选方案\n    A（10240 可能在训练中遇到更长 prompt 再次失败）。\n  related_experiments:\n  - exp_id: 8b_cell_c_episode_v5\n    role: parent\n    result: 'failed: max_model_len=16384 needs 2.25 GiB KV cache, gpu_mem_util=0.20\n      only provides 1.44 GiB'\n  depends_on:\n  - D091\n  - D090\n```\n\n**D094** (2026-05-19 14:09 UTC)\n```yaml\n- id: D094\n  date: 2026-05-19 14:09 UTC\n  summary: 'Cell C v8（最后尝试）: ppo_mini_batch_size=2 + gpu_memory_utilization=0.22。v7\n    backward OOM 缺 3.7 GiB。batch 4→2 约省一半激活内存，util 0.25→0.22 释放 2.88 GiB。如果 v8 仍 OOM，接受\n    1.7B-only Cell C 数据，不再尝试'\n  rationale: v7 数据：allocated 110.14 GiB，backward 需 8.94 GiB，可用 5.21 GiB，缺 3.7 GiB。ppo_mini_batch_size\n    从 4 降到 2，backward 激活内存大约减半（~4.5 GiB）。gpu_memory_utilization 从 0.25 降到 0.22，释放\n    (0.25-0.22)×96=2.88 GiB，KV cache 从 6.24 降到 3.36 GiB（仍 > 需要的 2.25 GiB）。组合后：可用 ~8.1\n    GiB，需 ~4.5 GiB，余量 ~3.5 GiB。8B Cell C 连续 8 次失败已消耗大量 GPU 时间，这是最后一次尝试。论文有完整 1.7B\n    Cell C 数据 + 8B Cell A collapse + 8B info loss，足够支撑 claim。\n  related_experiments:\n  - exp_id: 8b_cell_c_episode_v7\n    role: parent\n    result: 'failed: backward OOM, 110.14 GiB allocated, need 8.94 GiB, only 5.21\n      GiB free'\n  depends_on:\n  - D093\n```\n\n**D095** (2026-05-19 14:14 UTC)\n```yaml\n- id: D095\n  date: 2026-05-19 14:14 UTC\n  summary: 正式放弃 8B Cell C：4×96GB 硬件不足以容纳 8B FSDP + VLLM + full-context backward（差\n    ~4 GiB 无可调参数弥补）。论文 8B 验证限于 Cell A collapse + info loss 37.5pp。1.7B Cell C 数据完整充分\n  rationale: 9 次连续失败穷尽所有配置空间。v8 暴露最后一个约束：ppo_mini_batch_size ≥ micro_batch_per_gpu(1)\n    × n_gpus(4) = 4，不可再降。gpu_mem_util 0.25→0.22 仅省 2.93 GiB < 缺口 3.73 GiB。8B FSDP\n    模型 + optimizer + VLLM 基线占用 ~110 GiB / 4GPU，backward 需 ~9 GiB，可用仅 ~5 GiB。根本矛盾：full-context\n    episode 的长序列 backward 激活在 96GB GPU 上装不下。论文有 1.7B Cell C 完整数据（23.88% OOD, 双 seed）+\n    8B Cell A collapse + 8B info loss 37.5pp + stochastic-triggered mechanism，scale\n    invariance claim 已充分支撑。8B Cell C 缺失在 Limitations 说明。\n  related_experiments:\n  - exp_id: 8b_cell_c_episode_v7\n    role: evidence\n    result: 'backward OOM: 110.14 GiB allocated, need 8.94, free 5.21'\n  - exp_id: 8b_cell_c_episode_v5\n    role: evidence\n    result: VLLM init + val_before_train passed but backward OOM\n  depends_on:\n  - D094\n  - D093\n  - D090\n```\n\n**D096** (2026-05-19 14:27 UTC)\n```yaml\n- id: D096\n  date: 2026-05-19 14:27 UTC\n  summary: 'D096: 尝试 FSDP CPU Offload 解决 8B Cell C backward OOM'\n  rationale: 用户批准\"试一下，不行再加卡\"。v7 backward OOM 缺口 3.7 GiB，CPU Offload 可省 ~8 GiB/卡，理论上绰绰有余。改动最小（只需修改\n    FSDP config 加 CPUOffload），不需要改 RAGEN 代码。如果失败，用户同意租更多 GPU。\n  related_experiments:\n  - exp_id: 8b_cell_c_episode_v7\n    role: predecessor\n    result: backward OOM, gap 3.7 GiB\n  - exp_id: 8b_cell_c_episode_v8\n    role: predecessor\n    result: config constraint violation\n  depends_on:\n  - D095\n```\n\n**D097** (2026-05-19 18:17 UTC)\n```yaml\n- id: D097\n  date: 2026-05-19 18:17 UTC\n  summary: 'D097: 8B Cell C v9 (FSDP2 CPUOffload) 失败——RAGEN GRPO train.py 不支持 FSDP2'\n  rationale: 'v9 启动后立即 NotImplementedError: RAGEN TaskRunner.run() 未实现 FSDP2 strategy。SFT\n    能用 FSDP2 是因为走 verl 原生 fsdp_sft_trainer，但 GRPO 走 RAGEN 自有代码。D096 的前提（只需改 config）不成立。回到用户决策：加卡还是接受\n    1.7B-only。'\n  related_experiments:\n  - exp_id: 8b_cell_c_v9\n    role: failed\n    result: 'NotImplementedError: RAGEN GRPO 不支持 FSDP2'\n  depends_on:\n  - D096\n  - D095\n```\n\n**D099** (2026-05-19 20:13 UTC)\n```yaml\n- id: D099\n  date: 2026-05-19 20:13 UTC\n  summary: 'D099: 8B Cell C v9c backward pass 成功——FSDP2+CPUOffload 方案可行，8B Cell C\n    解锁'\n  rationale: v9c 完成 step 1/30 backward pass 无 OOM。FSDP2+CPUOffload 将峰值显存从 91 GB 降至\n    83 GB/卡（余量 12 GB），10 次修复（5 文件 10 处 FSDP1→FSDP2 兼容）全部生效。预计 15-16h 完成 30 steps 训练。不需要租卡。\n  related_experiments:\n  - exp_id: 8b_cell_c_v9c\n    role: running\n    result: step 1/30 完成, backward pass 无 OOM, 83 GB/卡\n  depends_on:\n  - D098\n  - D097\n  - D096\n```\n\n**D102** (2026-05-20 08:05 UTC)\n```yaml\n- id: D102\n  date: 2026-05-20 08:05 UTC\n  summary: v9d 暂停训练，转向 step 10 OOD eval——8+ 次崩溃指向系统性不稳定，step 10 val=96.875% 数据已足够强\n  rationale: v9d 从 step 5 到 step 11 训练正常（success 81→97%），但 8+ 次崩溃覆盖磁盘满/model_path\n    误删/vLLM OOM/SIGHUP/静默死亡多种 failure mode，指向 FSDP2+CPUOffload+4卡 8B 在 westd 上的系统性不稳定。继续重启大概率继续崩。step\n    10 val=96.875% vs Cell A 1.5% 的对比已足够支撑跨尺度 claim。先做 OOD eval 拿论文数据，同时诊断根因决定是否值得继续训练到\n    step 30。\n  related_experiments:\n  - exp_id: 8b_cell_c_episode_v9d\n    role: target\n    result: step 10 val 96.875%, 8+ crashes\n  depends_on:\n  - D101\n```\n\n**D103** (2026-05-20 09:24 UTC)\n```yaml\n- id: D103\n  date: 2026-05-20 09:24 UTC\n  summary: v9d step 15 后停止训练——step 12 起 GRPO reward 饱和（100% success, pg_loss=0），继续训练无信号。转向\n    OOD eval\n  rationale: Step 12 完整 metrics：train success 1.0，critic score 全 10.0，advantages 全\n    0，pg_loss=0，grad_norm 0.022。GRPO 依赖 group 内 reward 差异，全组成功则 advantage normalization\n    为零。Step 12→30 模型权重不会变化（除 entropy drift），等效 GPU 空转。OOD eval 是论文关键数据，step 10/15\n    checkpoint 已可评估。停训练后释放 westd 4×GPU 用于 OOD eval + 可能的 ScienceWorld GRPO。\n  related_experiments:\n  - exp_id: 8b_cell_c_episode_v9d\n    role: target\n    result: step 12 reward saturation, 100% in-dist success\n  depends_on:\n  - D102\n```\n\n**D104** (2026-05-20 12:14 UTC)\n```yaml\n- id: D104\n  date: 2026-05-20 12:14 UTC\n  summary: Claim 1 升级：从 \"unstable/fragile\" 升级为 \"systematic failure mechanism, scale-invariant\"\n    + \"necessary minimum fix\"。不用 \"catastrophic\"（1.7B seed2 学了 9.375%）\n  rationale: Reviewer 独立评估：8B Cell C 90.3% + Cell A 1.5% 跨尺度对比、γ-sweep 全坍缩、factorial\n    2×2 全部验证——证据强度已超出 D067 降级时的 \"unstable/fragile\"。新表述：systematic + scale-invariant\n    failure mechanism，episode-level 是 necessary minimum fix（不 claim optimal，承认 GAGPO\n    等更优）。保留 stochastically triggered 解释社区为何未普遍注意。最大风险：R1(trivial fix)+R2(无 fine-grained\n    baseline) 组合攻击——Practitioner Decision Tree 在 Discussion 中可部分缓解。\n  related_experiments:\n  - exp_id: 8b_cell_c_episode_v9d\n    role: key_evidence\n    result: 90.3% OOD\n  - exp_id: 7b_cell_a_h2\n    role: key_evidence\n    result: 1.5% collapse\n  - exp_id: gsweep_g100_h5_seed1\n    role: supporting\n    result: γ=1.0 collapse\n  depends_on:\n  - D067\n  - D103\n```\n\n**D105** (2026-05-20 13:26 UTC) -- **Key ScienceWorld decision: scenario planning**\n```yaml\n- id: D105\n  date: 2026-05-20 13:26 UTC\n  summary: ScienceWorld GRPO 三场景预案：(1) Cell A collapse + Cell C learns = 最强; (2) 两者都不学\n    = diagnosis 仍成立，fix 加限定语; (3) Cell A 不 collapse = 可解释为 \"nothing to destroy at\n    0% baseline\"。核心结论：ScienceWorld 是 bonus，不是 load-bearing\n  rationale: Reviewer 独立评估：三个场景概率 40%/35%/25%。无论哪个场景，ALFWorld 的跨尺度证据（1.7B + 8B）+ factorial\n    + γ-sweep 已足够 EMNLP ≥ 4.0。ScienceWorld Cell A val_before_train = 0% 使场景 3 有合理解释（sign\n    misattribution 破坏的是 existing capability，0% baseline 无东西可破坏）。关键诊断指标不仅是 pass@1，还有\n    entropy/KL 轨迹（区分 active destruction vs no signal）。场景 2 需提前准备 Limitations 段 \"capacity\n    vs credit\" 讨论。\n  related_experiments:\n  - exp_id: scienceworld_grpo_cell_a\n    role: pending\n    result: running\n  - exp_id: scienceworld_grpo_cell_c\n    role: pending\n    result: running\n  depends_on:\n  - D104\n```\n\n**D106** (2026-05-20 13:49 UTC) -- **Key ScienceWorld result: Cell A collapse confirmed**\n```yaml\n- id: D106\n  date: 2026-05-20 13:49 UTC\n  summary: ScienceWorld Cell A 崩溃确认：final_score 6.0→-100.0，比 ALFWorld 更极端。D105 场景\n    1 上半部成立——failure mechanism 跨环境验证完成\n  rationale: Cell A (step-independent h=2) 在 ScienceWorld 15 步全程 0% success，final_score\n    降至 -100.0（ALFWorld 不会负分）。entropy 上升+KL 崩塌模式与 ALFWorld 一致。ScienceWorld 任务结构（科学推理、长\n    horizon）与 ALFWorld（家务）完全不同，排除环境特异性。等 Cell C 结果完成场景 1 判断。Reviewer 风险 R3 (single\n    env) 基本解决。\n  related_experiments:\n  - exp_id: scienceworld_grpo_cell_a\n    role: key_evidence\n    result: collapse confirmed, final_score -100.0\n  - exp_id: scienceworld_grpo_cell_c\n    role: pending\n    result: 1/15 steps, ~7h\n  depends_on:\n  - D105\n```\n\n**D107** (2026-05-20 15:34 UTC) -- **ScienceWorld Cell C Java crashes**\n```yaml\n- id: D107\n  date: 2026-05-20 15:34 UTC\n  summary: ScienceWorld Cell C 崩溃（第3次 Java 异常）：最后重试一次加固版，不阻塞论文压缩\n  rationale: ScienceWorld Java 环境三次崩溃（Info Loss Eval ×2 + Cell C ×1），root cause 是\n    Java IPC 通信异常。Cell A collapse 已确认（D106），跨环境 failure 证据充分。Cell C（episode-level\n    fix 跨环境验证）是 nice-to-have 而非 must-have——论文核心 claim 不依赖它。策略：(1) 最后重试一次，Agent 先调查\n    Java 异常并加固；(2) Paper Agent 立即推进 16→8 页压缩，不等 Cell C；(3) 若再次崩溃则接受现有数据，Limitations\n    如实说明。\n  related_experiments:\n  - exp_id: scienceworld_grpo_cell_c\n    role: subject\n    result: DONE(failed) — Java IPC crash after step 1\n  - exp_id: scienceworld_grpo_cell_a\n    role: evidence\n    result: DONE(negative) — collapse confirmed, cross-env failure validated\n  depends_on:\n  - D105\n  - D106\n```\n\n**D108** (2026-05-21 01:48 UTC) -- **ScienceWorld Cell C v3 also collapses**\n```yaml\n- id: D108\n  date: 2026-05-21 01:48 UTC\n  summary: Seed 3 OOD 10.45% (vs Seed 1 23.88%)：Table 1 报 mean[range]，Limitations\n    加 seed variance 说明。Cell C v3 ScienceWorld episode-level 坍塌：继续观察到 step 5，不影响当前\n    claim（论文只 claim collapse generalizes，不 claim fix generalizes）\n  rationale: Seed 3 OOD 差异统计显著 (z=2.91, p<0.005)，但均值 17.2% 仍高于 SFT baseline 12.5%，核心\n    claim \"episode-level avoids collapse and enables learning\" 两 seed 都成立。Cell C v3\n    step 2 reward saturation（128 trajectories 全零 reward），与 Section 3 reward saturation\n    分析一致——ScienceWorld 更难，episode-level 不能解决 reward saturation。论文已谨慎措辞，只需加 Limitations。\n  related_experiments:\n  - exp_id: exp029_seed3_ood_v2\n    role: seed3 OOD eval\n    result: 10.45% (14/134)\n  - exp_id: exp029_episode_level\n    role: seed1 OOD baseline\n    result: 23.88% (32/134)\n  - exp_id: scienceworld_grpo_cell_c_v3\n    role: SW episode-level fix\n    result: collapsing at step 2\n  depends_on:\n  - D104\n  - D106\n```\n\n**D109** (2026-05-21 02:41 UTC) -- **ScienceWorld Cell C terminated**\n```yaml\n- id: D109\n  date: 2026-05-21 02:41 UTC\n  summary: Cell C v3 提前终止（step 3），释放 westd cuda:2,3；启动 seed 5 并行训练（westd cuda:0,1）\n  rationale: Cell C v3 step 3 已满足止损条件（success=0%, action_is_valid=9.4%<20%），且趋势持续恶化（score\n    2.71→0.96, reward 0.5→0.153），等 step 5 只浪费 ~10 GPU-hours。论文 Limitations 段用 step\n    3 数据即可。释放的 GPU 加上已空闲的 cuda:0,1，启动 seed 5 并行训练——与 bjb1 seed 4 同时跑，最终 4 个 seed 的\n    OOD 数据统计可靠性远优于 3 个。当前 2-seed OOD variance 大（10.4% vs 23.9%），4 seeds 可报 mean±std，审稿人信服度显著提升。\n  related_experiments:\n  - exp_id: scienceworld_grpo_cell_c_v3\n    role: terminated\n    result: 'negative: 3 steps 0% success, collapse confirmed'\n  - exp_id: exp029_seed4\n    role: parallel_seed\n    result: training on bjb1\n  depends_on:\n  - D107\n  - D108\n```\n\n**D120** (2026-05-22 03:34 UTC) -- **ScienceWorld elevated to P0**\n```yaml\n- id: D120\n  date: 2026-05-22 03:34 UTC\n  summary: 接受 Reviewer 叙事建议：干预实验降级为 Discussion，核心 claim 聚焦双机制诊断 + factorial + 8B scale；ScienceWorld\n    跨环境验证升为 P0\n  rationale: Reviewer 审查结论：(1) Claim 1（双机制诊断）证据 VERY STRONG，足够支撑核心贡献；(2) 干预失败/response\n    inflation/mode shift 证据不足作 core claim（N=1、训练步数混杂、C' 实现 bug）；(3) 无 ScienceWorld\n    预估 3.0-3.5（Findings），补齐后 3.5-4.0（Conference）。ScienceWorld 是达到 EMNLP 2026 Overall\n    ≥4 的关键门槛。干预实验放 Discussion/Observations，不稀释核心贡献。seed_2048 step 1-2 即崩溃（resp_len\n    15511, success 0.78%），无法提供 healthy baseline，但更新 collapse rate 至 4/7=57%。\n  related_experiments:\n  - exp_id: exp029_new_seed_2048\n    role: observation\n    result: collapsing at step 1-2, resp_len=15865, cannot serve as healthy baseline\n  - exp_id: exp029_c_prime_resume_mt50_v2\n    role: parent\n    result: negative, cap ineffective\n  depends_on:\n  - D119\n```\n\n---\n\n**Summary of all 28 decision blocks**: D068, D070, D071, D072, D073, D077, D080, D081, D083, D085, D089, D090, D091, D093, D094, D095, D096, D097, D099, D102, D103, D104, D105, D106, D107, D108, D109, D120.\n\nThe **directly ScienceWorld-focused** decisions are: D081 (launch), D089 (experiment design), D105 (scenario planning), D106 (Cell A collapse confirmed), D107 (Cell C Java crashes), D108 (Cell C v3 collapses), D109 (Cell C terminated), D120 (ScienceWorld elevated to P0). The remaining decisions reference Cell A/Cell C in the ALFWorld/8B context."
      }
    ],
    "totalDurationMs": 374870,
    "totalTokens": 47749,
    "totalToolUseCount": 12,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 760,
      "cache_read_input_tokens": 34644,
      "output_tokens": 12344,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 760
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12344,
          "cache_read_input_tokens": 34644,
          "cache_creation_input_tokens": 760,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 760,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 4,
      "searchCount": 3,
      "bashCount": 5,
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

_source line 85_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive data from all sources. Let me compile the final report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "8942c0a7-6825-41d2-a667-5e23fcab5e2f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DHU6nuWpCP1KYeys3eVKHL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19052,
      "cache_read_input_tokens": 40336,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19052
      },
      "output_tokens": 23,
      "service_tier": "standard",
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

_source line 86_

## ScienceWorld 实验汇总报告

---

### 1. 实验时间线

| exp_id | 创建时间 | 状态 | 结论 | 说明 |
|--------|---------|------|------|------|
| `scienceworld_sft` | 05-19 14:35 | DONE | **success** | 1.7B SFT 训练，448 steps，train_loss 0.003 |
| `scienceworld_sft_eval` | 05-19 18:11 | DONE | killed | 首次 eval，中途 killed |
| `scienceworld_sft_eval_v2` | 05-19 18:50 | DONE | **success** | SFT baseline: **30.1% success, avg_score 20.9** |
| `scienceworld_info_loss_full` | 05-20 14:21 | DONE | failed | westd 上 info loss 实验，失败 |
| `sw_info_loss_full_v2` | 05-20 14:34 | DONE | failed | 同上重试，再次失败 |
| `scienceworld_info_loss_h2` | 05-20 14:21 | DONE | killed | h=2 info loss 实验，killed |
| `sw_info_loss_bjb1` | 05-20 16:38 | DONE | **success** | **info loss 结果: full=34.8% vs h2=4.5%, delta=30.3pp** |
| `scienceworld_grpo_cell_a` | 05-20 11:24 | DONE | **negative** | **Cell A collapse 确认: 15步全程 0% success, score→-100** |
| `scienceworld_grpo_cell_c` | 05-20 11:24 | DONE | **failed** | Cell C v1: Java IPC 通信异常，step 1 后崩溃 |
| `scienceworld_grpo_cell_c_v2` | 05-20 15:41 | DONE | **failed** | Cell C v2: 磁盘满(99%)，Ray object spilling 阻塞，stall 1h50m |
| `scienceworld_grpo_cell_c_v3` | 05-20 18:23 | DONE | **negative** | Cell C v3: **3步后止损，0% success, action_valid=9.4%, collapse** |

---

### 2. 每次失败的具体原因

**Cell C v1 (Java crash)**
- failure_reason: `ScienceWorld Java environment communication error: Exception while sending command`
- 仅完成 1/15 steps，step 1 score=5.44, action_valid=0.44
- Root cause: ScienceWorld 底层 Java IPC 通信不稳定

**Cell C v2 (磁盘满)**
- 在 step 2 stall，磁盘使用率 99%
- Ray object spilling 被阻塞，GPU utilization 0% 持续 1h50min
- 花费 5.41 GPU-hours 后 killed

**Cell C v3 (训练崩溃/止损)**
- 不是基础设施故障，而是**训练本身 collapse**
- step 1→3: score 2.71→0.96, reward 0.5→0.153, action_valid=9.4%
- 128 trajectories 全零 reward（reward saturation）
- D109 判定：满足止损条件（success=0%, action_valid<20%），趋势持续恶化，释放 GPU

**Cell A (负面结果，非"失败")**
- 15步全程 0% success，final_score -100.0（比 ALFWorld 更极端）
- entropy 上升 + KL 崩塌，模式与 ALFWorld Cell A 一致
- 这是**预期结果**，用于跨环境验证 step-independent collapse

---

### 3. SFT Baseline 结果

- **整体**: 540/1796 episodes 成功，**success rate 30.1%，avg_score 20.9**
- **高分任务**: lifespan-longest-lived 90.3%, find-non-living-thing 77.3%, find-living-thing 65.3%
- **零分任务**: boil 0%, chemistry-mix 0%, freeze 0%, grow-plant 0%, identify-life-stages 0%
- **Info loss**: full context 34.8% vs h=2 window 4.5%，delta 30.3pp（某些任务从 100%→0%）

---

### 4. 实验设计和超参数

**SFT 训练**:
- model: Qwen3-1.7B, data: 3592 train / 1796 val, lr: 5e-6, epochs: 2, batch: 16, max_length: 16384, FSDP2

**Cell A (step-independent GRPO)**:
- steps: 15, context_window_mode: step_independent, history_length: 2
- env_groups: 16, group_size: 8, ppo_mini_batch_size: 8, lr: 1e-6, n_gpus: 2
- server: westd, gpu: cuda:0,1

**Cell C (episode-level GRPO)**:
- steps: 15, context_window_mode: full
- env_groups: 16, group_size: 8, ppo_mini_batch_size: 8, lr: 1e-6, n_gpus: 2
- server: westd, gpu: cuda:2,3
- seed: 10000（v2/v3）

---

### 5. 基于失败历史的 GRPO 配置建议

Cell C 三次失败暴露三个独立问题：

1. **Java IPC 不稳定** → 需要 JVM 加固（`JAVA_TOOL_OPTIONS=-Xmx4g`、超时重试、进程隔离）。v2 已做但未解决根本问题。考虑在 ScienceWorld env wrapper 层加 try/retry + env reset 逻辑。

2. **磁盘空间** → v2 因 99% 磁盘满导致 Ray spilling 失败。训练前必须确保 ≥50GB 可用空间，设置 `RAY_object_spilling_config` 指向数据盘。

3. **Reward saturation / 任务太难** → 这是最根本的问题。128 trajectories 全零 reward 意味着模型在 GRPO group 内无任何成功样本，advantage 全为零，训练信号消失。SFT baseline 仅 30.1%（ALFWorld SFT 是 ~50-80%），大量任务类型 success=0%。

**配置方向建议**：
- **过滤训练任务**：排除 SFT success=0% 的任务类型（boil, chemistry-mix, freeze, grow-plant 等），只用 SFT 有基础能力的任务（find-*, lifespan-*, test-conductivity 等）
- **增大 group_size**：从 8 提到 16-32，增加组内至少有 1 个成功样本的概率
- **增大 env_groups**：增加每步训练样本量
- **提高 lr**：当前 1e-6 可能过低，可尝试 5e-6（与 SFT 一致）
- **考虑 curriculum**：先从高成功率任务开始，逐步引入难任务
- **JVM 稳定性**：每个 episode 后强制 env.reset()，通信超时设 30s，失败后重建 Java 进程而非整个训练崩溃

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "uuid": "599a8be4-7d08-4923-8072-fa17728309e2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DHU6nuWpCP1KYeys3eVKHL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19052,
      "cache_read_input_tokens": 40336,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19052
      },
      "output_tokens": 23,
      "service_tier": "standard",
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

_source line 87_

## ScienceWorld 实验汇总报告

---

### 1. 实验时间线

| exp_id | 创建时间 | 状态 | 结论 | 说明 |
|--------|---------|------|------|------|
| `scienceworld_sft` | 05-19 14:35 | DONE | **success** | 1.7B SFT 训练，448 steps，train_loss 0.003 |
| `scienceworld_sft_eval` | 05-19 18:11 | DONE | killed | 首次 eval，中途 killed |
| `scienceworld_sft_eval_v2` | 05-19 18:50 | DONE | **success** | SFT baseline: **30.1% success, avg_score 20.9** |
| `scienceworld_info_loss_full` | 05-20 14:21 | DONE | failed | westd 上 info loss 实验，失败 |
| `sw_info_loss_full_v2` | 05-20 14:34 | DONE | failed | 同上重试，再次失败 |
| `scienceworld_info_loss_h2` | 05-20 14:21 | DONE | killed | h=2 info loss 实验，killed |
| `sw_info_loss_bjb1` | 05-20 16:38 | DONE | **success** | **info loss 结果: full=34.8% vs h2=4.5%, delta=30.3pp** |
| `scienceworld_grpo_cell_a` | 05-20 11:24 | DONE | **negative** | **Cell A collapse 确认: 15步全程 0% success, score→-100** |
| `scienceworld_grpo_cell_c` | 05-20 11:24 | DONE | **failed** | Cell C v1: Java IPC 通信异常，step 1 后崩溃 |
| `scienceworld_grpo_cell_c_v2` | 05-20 15:41 | DONE | **failed** | Cell C v2: 磁盘满(99%)，Ray object spilling 阻塞，stall 1h50m |
| `scienceworld_grpo_cell_c_v3` | 05-20 18:23 | DONE | **negative** | Cell C v3: **3步后止损，0% success, action_valid=9.4%, collapse** |

---

### 2. 每次失败的具体原因

**Cell C v1 (Java crash)**
- failure_reason: `ScienceWorld Java environment communication error: Exception while sending command`
- 仅完成 1/15 steps，step 1 score=5.44, action_valid=0.44
- Root cause: ScienceWorld 底层 Java IPC 通信不稳定

**Cell C v2 (磁盘满)**
- 在 step 2 stall，磁盘使用率 99%
- Ray object spilling 被阻塞，GPU utilization 0% 持续 1h50min
- 花费 5.41 GPU-hours 后 killed

**Cell C v3 (训练崩溃/止损)**
- 不是基础设施故障，而是**训练本身 collapse**
- step 1→3: score 2.71→0.96, reward 0.5→0.153, action_valid=9.4%
- 128 trajectories 全零 reward（reward saturation）
- D109 判定：满足止损条件（success=0%, action_valid<20%），趋势持续恶化，释放 GPU

**Cell A (负面结果，非"失败")**
- 15步全程 0% success，final_score -100.0（比 ALFWorld 更极端）
- entropy 上升 + KL 崩塌，模式与 ALFWorld Cell A 一致
- 这是**预期结果**，用于跨环境验证 step-independent collapse

---

### 3. SFT Baseline 结果

- **整体**: 540/1796 episodes 成功，**success rate 30.1%，avg_score 20.9**
- **高分任务**: lifespan-longest-lived 90.3%, find-non-living-thing 77.3%, find-living-thing 65.3%
- **零分任务**: boil 0%, chemistry-mix 0%, freeze 0%, grow-plant 0%, identify-life-stages 0%
- **Info loss**: full context 34.8% vs h=2 window 4.5%，delta 30.3pp（某些任务从 100%→0%）

---

### 4. 实验设计和超参数

**SFT 训练**:
- model: Qwen3-1.7B, data: 3592 train / 1796 val, lr: 5e-6, epochs: 2, batch: 16, max_length: 16384, FSDP2

**Cell A (step-independent GRPO)**:
- steps: 15, context_window_mode: step_independent, history_length: 2
- env_groups: 16, group_size: 8, ppo_mini_batch_size: 8, lr: 1e-6, n_gpus: 2
- server: westd, gpu: cuda:0,1

**Cell C (episode-level GRPO)**:
- steps: 15, context_window_mode: full
- env_groups: 16, group_size: 8, ppo_mini_batch_size: 8, lr: 1e-6, n_gpus: 2
- server: westd, gpu: cuda:2,3
- seed: 10000（v2/v3）

---

### 5. 基于失败历史的 GRPO 配置建议

Cell C 三次失败暴露三个独立问题：

1. **Java IPC 不稳定** → 需要 JVM 加固（`JAVA_TOOL_OPTIONS=-Xmx4g`、超时重试、进程隔离）。v2 已做但未解决根本问题。考虑在 ScienceWorld env wrapper 层加 try/retry + env reset 逻辑。

2. **磁盘空间** → v2 因 99% 磁盘满导致 Ray spilling 失败。训练前必须确保 ≥50GB 可用空间，设置 `RAY_object_spilling_config` 指向数据盘。

3. **Reward saturation / 任务太难** → 这是最根本的问题。128 trajectories 全零 reward 意味着模型在 GRPO group 内无任何成功样本，advantage 全为零，训练信号消失。SFT baseline 仅 30.1%（ALFWorld SFT 是 ~50-80%），大量任务类型 success=0%。

**配置方向建议**：
- **过滤训练任务**：排除 SFT success=0% 的任务类型（boil, chemistry-mix, freeze, grow-plant 等），只用 SFT 有基础能力的任务（find-*, lifespan-*, test-conductivity 等）
- **增大 group_size**：从 8 提到 16-32，增加组内至少有 1 个成功样本的概率
- **增大 env_groups**：增加每步训练样本量
- **提高 lr**：当前 1e-6 可能过低，可尝试 5e-6（与 SFT 一致）
- **考虑 curriculum**：先从高成功率任务开始，逐步引入难任务
- **JVM 稳定性**：每个 episode 后强制 env.reset()，通信超时设 30s，失败后重建 Java 进程而非整个训练崩溃

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 473185,
  "duration_api_ms": 623387,
  "num_turns": 9,
  "stop_reason": "end_turn",
  "session_id": "54b94781-146b-4013-9381-11e3737077cb",
  "total_cost_usd": 1.5883075,
  "usage": {
    "input_tokens": 10,
    "cache_creation_input_tokens": 47547,
    "cache_read_input_tokens": 140819,
    "output_tokens": 4050,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 47547,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 3,
        "output_tokens": 2132,
        "cache_read_input_tokens": 40336,
        "cache_creation_input_tokens": 19052,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 19052
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-opus-4-6": {
      "inputTokens": 32,
      "outputTokens": 27932,
      "cacheReadInputTokens": 477717,
      "cacheCreationInputTokens": 103856,
      "webSearchRequests": 0,
      "costUSD": 1.5864185000000002,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    },
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1794,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001889,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "baaccc6a-b8eb-48e1-8c95-d0bae7ef8643"
}
```

</details>

---
