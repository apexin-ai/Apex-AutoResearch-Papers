# analysis cross scale summary

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/workers/worker_analysis_cross_scale_summary_20260516T142615.log`
- **Structured JSON:** [`d7ead506b7fe12784ea8.json`](../../sessions/d7/d7ead506b7fe12784ea8.json)

## Before a recorded user message

35 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "session_id": "6cf6c7bc-54c9-45a8-b5e6-b498a2a84d18",
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
  "uuid": "8328f6c2-c8f7-4291-a653-39634fb71ba2",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/memory/"
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
    "resetsAt": 1778957400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "626fdc73-5554-4983-aee4-74007c0542e2",
  "session_id": "6cf6c7bc-54c9-45a8-b5e6-b498a2a84d18"
}
```

---

### Assistant

_source line 4_

I'll start by reading the registry to get all experiment data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6cf6c7bc-54c9-45a8-b5e6-b498a2a84d18",
  "uuid": "4f35daae-553f-4916-bbc8-ccacd3a8d639",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018UMtNDXUnKfVEL4GFDroZq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11682,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11682
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

_source line 5_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01QzukYCwGEFJj9UaSjvkebM`</summary>

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
  "session_id": "6cf6c7bc-54c9-45a8-b5e6-b498a2a84d18",
  "uuid": "334e4947-650b-4df8-a729-7a5ac416f138",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018UMtNDXUnKfVEL4GFDroZq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11682,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11682
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

_source line 6 · 2026-05-16T14:26:24.908Z_

<details><summary>↩ Tool result · `toolu_01QzukYCwGEFJj9UaSjvkebM`</summary>

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
  "session_id": "6cf6c7bc-54c9-45a8-b5e6-b498a2a84d18",
  "uuid": "e8885628-90ee-4acf-a147-0b21c607916d",
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

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Let me read the registry to get all experiment data for the trace-verdict-study project.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6cf6c7bc-54c9-45a8-b5e6-b498a2a84d18",
  "uuid": "d826ede9-751d-40fd-9076-16dfa4221354",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ScJGR986YGegcFCufyErrn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1339,
      "cache_read_input_tokens": 23523,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1339
      },
      "output_tokens": 43,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_0189F6P5FigWgP6B82F8dW9K`</summary>

```json
{
  "project": "trace-verdict-study",
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
  "session_id": "6cf6c7bc-54c9-45a8-b5e6-b498a2a84d18",
  "uuid": "4159d920-6671-4083-8e10-eae8686e2685",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ScJGR986YGegcFCufyErrn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1339,
      "cache_read_input_tokens": 23523,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1339
      },
      "output_tokens": 43,
      "service_tier": "standard",
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

_source line 9 · 2026-05-16T14:26:28.881Z_

<details><summary>↩ Tool result · `toolu_0189F6P5FigWgP6B82F8dW9K`</summary>

```text
Error: result (125,349 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/6cf6c7bc-54c9-45a8-b5e6-b498a2a84d18/tool-results/mcp-agent-ml-research-read_registry-1778941588866.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/6cf6c7bc-54c9-45a8-b5e6-b498a2a84d18/tool-results/mcp-agent-ml-research-read_registry-1778941588866.txt in sequential chunks until 100% of the content has been read.
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
  "session_id": "6cf6c7bc-54c9-45a8-b5e6-b498a2a84d18",
  "uuid": "1c990629-8613-4d3d-9024-bfbe0525f2a4",
  "tool_use_result": {
    "content": "Error: result (125,349 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/6cf6c7bc-54c9-45a8-b5e6-b498a2a84d18/tool-results/mcp-agent-ml-research-read_registry-1778941588866.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/6cf6c7bc-54c9-45a8-b5e6-b498a2a84d18/tool-results/mcp-agent-ml-research-read_registry-1778941588866.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"codellama13b_vota_seed42\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:47:21.632Z\", \"updated_at\": \"2026-05-16T14:23:10.565Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition vota --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_vota_seed42 --wandb_project trace-verdict-study --wandb_run_name codellama13b_vota_seed42 && python eval/evaluate.py --condition vota --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_vota_seed42/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_vota_seed42/final/eval_results.json --save_predictions\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"279473\", \"log_path\": \"~/runs/trace-verdict-study/codellama13b_vota_seed42.log\", \"submitted_at\": \"2026-05-16T14:23:09.712Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"pid\": \"279473\", \"log_path\": \"~/runs/trace-verdict-study/codellama13b_vota_seed42.log\", \"wandb_run_id\": \"codellama13b_vota_seed42\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition vota --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_vota_seed42 --wandb_project trace-verdict-study --wandb_run_name codellama13b_vota_seed42 && python eval/evaluate.py --condition vota --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_vota_seed42/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_vota_seed42/final/eval_results.json --save_predictions\\\"\", \"wandb_run_id\": \"codellama13b_vota_seed42\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\"}}, \"codellama13b_no_trace_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:47:20.182Z\", \"updated_at\": \"2026-05-16T14:22:58.643Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition no_trace --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_no_trace_seed42 --wandb_project trace-verdict-study --wandb_run_name codellama13b_no_trace_seed42 && python eval/evaluate.py --condition no_trace --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_no_trace_seed42/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_no_trace_seed42/final/eval_results.json --save_predictions\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"277044\", \"log_path\": \"~/runs/trace-verdict-study/codellama13b_no_trace_seed42.log\", \"submitted_at\": \"2026-05-16T13:42:06.812Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 2451.8, \"gpu_hours\": 0.68}, \"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"pid\": \"277044\", \"log_path\": \"~/runs/trace-verdict-study/codellama13b_no_trace_seed42.log\", \"wandb_run_id\": \"codellama13b_no_trace_seed42\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition no_trace --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_no_trace_seed42 --wandb_project trace-verdict-study --wandb_run_name codellama13b_no_trace_seed42 && python eval/evaluate.py --condition no_trace --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_no_trace_seed42/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_no_trace_seed42/final/eval_results.json --save_predictions\\\"\", \"wandb_run_id\": \"codellama13b_no_trace_seed42\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\", \"finished_at\": \"2026-05-16T14:19:42.177Z\"}, \"gpu_ids\": [\"cuda:1\"], \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T14:19:44.574583+00:00\"}]}, \"metrics\": {\"accuracy\": 0.765, \"n\": 1190, \"majority_baseline\": 0.7151, \"lift\": 0.05, \"pass_precision\": 0.84, \"pass_recall\": 0.83, \"pass_f1\": 0.84, \"fail_precision\": 0.59, \"fail_recall\": 0.59, \"fail_f1\": 0.59, \"accuracy_ci\": [0.738, 0.787]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_no_trace_seed42/final\", \"completed_at\": \"2026-05-16T14:22:58.643Z\"}, \"loop_only_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T06:03:36.673Z\", \"updated_at\": \"2026-05-16T13:43:23.144Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition loop_only --gradient_checkpointing --gpu 0 --seed 456 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/loop_only_seed456 --wandb_project trace-verdict-study --wandb_run_name loop_only_seed456 && python eval/evaluate.py --condition loop_only --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/loop_only_seed456/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/loop_only_seed456/final/eval_results.json --save_predictions\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"269723\", \"log_path\": \"~/runs/trace-verdict-study/loop_only_seed456.log\", \"submitted_at\": \"2026-05-16T11:31:50.484Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 7892.7, \"gpu_hours\": 2.19}, \"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"pid\": \"269723\", \"log_path\": \"~/runs/trace-verdict-study/loop_only_seed456.log\", \"wandb_run_id\": \"loop_only_seed456\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition loop_only --gradient_checkpointing --gpu 0 --seed 456 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/loop_only_seed456 --wandb_project trace-verdict-study --wandb_run_name loop_only_seed456 && python eval/evaluate.py --condition loop_only --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/loop_only_seed456/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/loop_only_seed456/final/eval_results.json --save_predictions\\\"\", \"wandb_run_id\": \"loop_only_seed456\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\", \"finished_at\": \"2026-05-16T13:39:35.472Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T13:39:37.576842+00:00\"}]}, \"metrics\": {\"accuracy\": 0.8664, \"n\": 1190, \"pass_precision\": 0.9179, \"pass_recall\": 0.8931, \"pass_f1\": 0.9053, \"fail_precision\": 0.7486, \"fail_recall\": 0.7994, \"fail_f1\": 0.7732, \"accuracy_ci\": [0.847, 0.884]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/loop_only_seed456/final\", \"completed_at\": \"2026-05-16T13:43:23.144Z\"}, \"qwen15b_full_trace_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T09:22:03.743Z\", \"updated_at\": \"2026-05-16T12:03:49.820Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition full_trace --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_seed42 --wandb_project trace-verdict-study --wandb_run_name qwen15b_full_trace_seed42 && python eval/evaluate.py --condition full_trace --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_seed42/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_seed42/final/eval_results.json --save_predictions\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"267886\", \"log_path\": \"~/runs/trace-verdict-study/qwen15b_full_trace_seed42.log\", \"submitted_at\": \"2026-05-16T11:10:01.431Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 3228.4, \"gpu_hours\": 0.9}, \"server\": \"westd-11235\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"pid\": \"267886\", \"log_path\": \"~/runs/trace-verdict-study/qwen15b_full_trace_seed42.log\", \"wandb_run_id\": \"qwen15b_full_trace_seed42\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition full_trace --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_seed42 --wandb_project trace-verdict-study --wandb_run_name qwen15b_full_trace_seed42 && python eval/evaluate.py --condition full_trace --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_seed42/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_seed42/final/eval_results.json --save_predictions\\\"\", \"wandb_run_id\": \"qwen15b_full_trace_seed42\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\", \"finished_at\": \"2026-05-16T12:00:28.907Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T12:00:31.043272+00:00\"}]}, \"metrics\": {\"accuracy\": 0.7706, \"n\": 1190}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_seed42/final\", \"completed_at\": \"2026-05-16T12:03:49.820Z\"}, \"codellama13b_exception_only_seed42\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:47:18.896Z\", \"updated_at\": \"2026-05-16T12:03:39.369Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition exception_only --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_exception_only_seed42 --wandb_project trace-verdict-study --wandb_run_name codellama13b_exception_only_seed42 && python eval/evaluate.py --condition exception_only --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_exception_only_seed42/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_exception_only_seed42/final/eval_results.json --save_predictions\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"271776\", \"log_path\": \"~/runs/trace-verdict-study/codellama13b_exception_only_seed42.log\", \"submitted_at\": \"2026-05-16T12:03:38.585Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"server\": \"westd-11235\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"pid\": \"271776\", \"log_path\": \"~/runs/trace-verdict-study/codellama13b_exception_only_seed42.log\", \"wandb_run_id\": \"codellama13b_exception_only_seed42\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition exception_only --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_exception_only_seed42 --wandb_project trace-verdict-study --wandb_run_name codellama13b_exception_only_seed42 && python eval/evaluate.py --condition exception_only --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_exception_only_seed42/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_exception_only_seed42/final/eval_results.json --save_predictions\\\"\", \"wandb_run_id\": \"codellama13b_exception_only_seed42\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\"}}, \"loop_only_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T06:03:35.196Z\", \"updated_at\": \"2026-05-16T11:39:45.684Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition loop_only --gradient_checkpointing --gpu 0 --seed 123 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/loop_only_seed123 --wandb_project trace-verdict-study --wandb_run_name loop_only_seed123 && python eval/evaluate.py --condition loop_only --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/loop_only_seed123/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/loop_only_seed123/final/eval_results.json --save_predictions\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"261213\", \"log_path\": \"~/runs/trace-verdict-study/loop_only_seed123.log\", \"submitted_at\": \"2026-05-16T09:21:29.194Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/loop_only_seed123/final\", \"wall_clock_seconds\": 7779.8, \"gpu_hours\": 2.16}, \"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"pid\": \"261213\", \"log_path\": \"~/runs/trace-verdict-study/loop_only_seed123.log\", \"wandb_run_id\": \"loop_only_seed123\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition loop_only --gradient_checkpointing --gpu 0 --seed 123 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/loop_only_seed123 --wandb_project trace-verdict-study --wandb_run_name loop_only_seed123 && python eval/evaluate.py --condition loop_only --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/loop_only_seed123/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/loop_only_seed123/final/eval_results.json --save_predictions\\\"\", \"wandb_run_id\": \"loop_only_seed123\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\", \"finished_at\": \"2026-05-16T11:28:44.218Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T11:28:46.379629+00:00\"}]}, \"metrics\": {\"accuracy\": 0.8588, \"majority_baseline\": 0.7151, \"lift\": 0.1437, \"n\": 1190, \"pass_precision\": 0.9129, \"pass_recall\": 0.8872, \"pass_f1\": 0.8999, \"fail_precision\": 0.7355, \"fail_recall\": 0.7876, \"fail_f1\": 0.7607, \"accuracy_ci\": [0.8403, 0.8773]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T11:31:09.027Z\"}, \"codellama_vota_seed42\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:27:43.769Z\", \"updated_at\": \"2026-05-16T11:37:31.737Z\", \"spec\": {\"hypothesis\": \"Multi-family validation: VOTA on CodeLlama-7B-Instruct.\", \"model_name\": \"CodeLlama-7b-Instruct-hf\", \"seed\": 42, \"condition\": \"vota\"}, \"conclusion\": \"killed\", \"failure_reason\": \"user approved 13B not 7B\"}, \"codellama_no_trace_seed42\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:27:42.805Z\", \"updated_at\": \"2026-05-16T11:37:31.087Z\", \"spec\": {\"hypothesis\": \"Multi-family baseline: no_trace on CodeLlama-7B-Instruct.\", \"model_name\": \"CodeLlama-7b-Instruct-hf\", \"seed\": 42, \"condition\": \"no_trace\"}, \"conclusion\": \"killed\", \"failure_reason\": \"user approved 13B not 7B\"}, \"codellama_exception_only_seed42\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:27:41.475Z\", \"updated_at\": \"2026-05-16T11:37:30.170Z\", \"spec\": {\"hypothesis\": \"Multi-family validation: exception_only on CodeLlama-7B-Instruct. Tests if exception dominance generalizes to LLaMA family.\", \"model_name\": \"CodeLlama-7b-Instruct-hf\", \"seed\": 42, \"condition\": \"exception_only\"}, \"conclusion\": \"killed\", \"failure_reason\": \"user approved 13B not 7B\"}, \"qwen1.5b_full_trace_seed42\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:27:39.587Z\", \"updated_at\": \"2026-05-16T11:36:49.302Z\", \"spec\": {\"hypothesis\": \"Multi-scale validation: full_trace on Qwen-2.5-Coder-1.5B.\", \"model_name\": \"Qwen2.5-Coder-1.5B-Instruct\", \"seed\": 42, \"condition\": \"full_trace\"}, \"conclusion\": \"killed\", \"failure_reason\": \"replaced by qwen15b_* entries (dot in exp_id incompatible with submit_on_allocated)\"}, \"qwen1.5b_vota_seed42\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:27:38.134Z\", \"updated_at\": \"2026-05-16T11:36:48.754Z\", \"spec\": {\"hypothesis\": \"Multi-scale validation: VOTA on Qwen-2.5-Coder-1.5B.\", \"model_name\": \"Qwen2.5-Coder-1.5B-Instruct\", \"seed\": 42, \"condition\": \"vota\"}, \"conclusion\": \"killed\", \"failure_reason\": \"replaced by qwen15b_* entries (dot in exp_id incompatible with submit_on_allocated)\"}, \"qwen1.5b_no_trace_seed42\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:27:36.233Z\", \"updated_at\": \"2026-05-16T11:36:47.343Z\", \"spec\": {\"hypothesis\": \"Multi-scale baseline: no_trace on Qwen-2.5-Coder-1.5B.\", \"model_name\": \"Qwen2.5-Coder-1.5B-Instruct\", \"seed\": 42, \"condition\": \"no_trace\"}, \"conclusion\": \"killed\", \"failure_reason\": \"replaced by qwen15b_* entries (dot in exp_id incompatible with submit_on_allocated)\"}, \"qwen1.5b_exception_only_seed42\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:27:34.741Z\", \"updated_at\": \"2026-05-16T11:36:46.424Z\", \"spec\": {\"hypothesis\": \"Multi-scale validation: exception_only on Qwen-2.5-Coder-1.5B. Tests if exception dominance holds at smaller scale.\", \"model_name\": \"Qwen2.5-Coder-1.5B-Instruct\", \"seed\": 42, \"condition\": \"exception_only\", \"server\": \"westd-11235\", \"gpu\": \"cuda:0\", \"account\": \"root\"}, \"conclusion\": \"killed\", \"failure_reason\": \"replaced by qwen15b_* entries (dot in exp_id incompatible with submit_on_allocated)\"}, \"qwen15b_vota_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T09:22:02.463Z\", \"updated_at\": \"2026-05-16T11:09:39.319Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition vota --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_vota_seed42 --wandb_project trace-verdict-study --wandb_run_name qwen15b_vota_seed42 && python eval/evaluate.py --condition vota --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_vota_seed42/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_vota_seed42/final/eval_results.json --save_predictions\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"265006\", \"log_path\": \"~/runs/trace-verdict-study/qwen15b_vota_seed42.log\", \"submitted_at\": \"2026-05-16T10:15:27.340Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_vota_seed42/final\", \"wall_clock_seconds\": 3252.0, \"gpu_hours\": 0.9}, \"server\": \"westd-11235\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"pid\": \"265006\", \"log_path\": \"~/runs/trace-verdict-study/qwen15b_vota_seed42.log\", \"wandb_run_id\": \"qwen15b_vota_seed42\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition vota --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_vota_seed42 --wandb_project trace-verdict-study --wandb_run_name qwen15b_vota_seed42 && python eval/evaluate.py --condition vota --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_vota_seed42/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_vota_seed42/final/eval_results.json --save_predictions\\\"\", \"wandb_run_id\": \"qwen15b_vota_seed42\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\", \"finished_at\": \"2026-05-16T11:07:13.230Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T11:07:15.416174+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.9958, \"n\": 1190, \"pass_recall\": 0.9976, \"fail_recall\": 0.9912, \"pass_f1\": 0.9971, \"fail_f1\": 0.9926, \"training_time_sec\": 2922}, \"completed_at\": \"2026-05-16T11:09:39.319Z\"}, \"qwen15b_no_trace_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T09:22:01.028Z\", \"updated_at\": \"2026-05-16T10:15:10.017Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition no_trace --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_no_trace_seed42 --wandb_project trace-verdict-study --wandb_run_name qwen15b_no_trace_seed42 && python eval/evaluate.py --condition no_trace --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_no_trace_seed42/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_no_trace_seed42/final/eval_results.json --save_predictions\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"263569\", \"log_path\": \"~/runs/trace-verdict-study/qwen15b_no_trace_seed42.log\", \"submitted_at\": \"2026-05-16T09:56:11.214Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_no_trace_seed42/final\", \"wall_clock_seconds\": 1138.8, \"gpu_hours\": 0.32}, \"server\": \"westd-11235\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"pid\": \"263569\", \"log_path\": \"~/runs/trace-verdict-study/qwen15b_no_trace_seed42.log\", \"wandb_run_id\": \"qwen15b_no_trace_seed42\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition no_trace --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_no_trace_seed42 --wandb_project trace-verdict-study --wandb_run_name qwen15b_no_trace_seed42 && python eval/evaluate.py --condition no_trace --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_no_trace_seed42/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_no_trace_seed42/final/eval_results.json --save_predictions\\\"\", \"wandb_run_id\": \"qwen15b_no_trace_seed42\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\", \"finished_at\": \"2026-05-16T10:13:02.700Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T10:13:04.620520+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.6731, \"n\": 1190, \"pass_f1\": 0.7527, \"fail_f1\": 0.518, \"lift_over_majority\": -0.042, \"training_time_sec\": 851}, \"completed_at\": \"2026-05-16T10:15:10.018Z\"}, \"qwen15b_exception_only_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T09:22:13.547Z\", \"updated_at\": \"2026-05-16T09:55:51.757Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition exception_only --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_exception_only_seed42 --wandb_project trace-verdict-study --wandb_run_name qwen15b_exception_only_seed42 && python eval/evaluate.py --condition exception_only --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_exception_only_seed42/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_exception_only_seed42/final/eval_results.json --save_predictions\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"261588\", \"log_path\": \"~/runs/trace-verdict-study/qwen15b_exception_only_seed42.log\", \"submitted_at\": \"2026-05-16T09:22:34.937Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_exception_only_seed42/final\", \"wall_clock_seconds\": 1990.3, \"gpu_hours\": 0.55}, \"server\": \"westd-11235\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"pid\": \"261588\", \"log_path\": \"~/runs/trace-verdict-study/qwen15b_exception_only_seed42.log\", \"wandb_run_id\": \"qwen15b_exception_only_seed42\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition exception_only --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_exception_only_seed42 --wandb_project trace-verdict-study --wandb_run_name qwen15b_exception_only_seed42 && python eval/evaluate.py --condition exception_only --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_exception_only_seed42/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_exception_only_seed42/final/eval_results.json --save_predictions\\\"\", \"wandb_run_id\": \"qwen15b_exception_only_seed42\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\", \"finished_at\": \"2026-05-16T09:53:32.293Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T09:53:34.556600+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.9983, \"accuracy_ci_lower\": 0.9958, \"accuracy_ci_upper\": 1, \"majority_baseline\": 0.7151, \"lift\": 0.283, \"n\": 1190, \"pass_precision\": 1, \"pass_recall\": 0.9976, \"pass_f1\": 0.9988, \"fail_precision\": 0.9941, \"fail_recall\": 1, \"fail_f1\": 0.9971, \"train_loss\": 0.1347, \"eval_loss\": 0.5761, \"wall_clock_seconds\": 1762}, \"completed_at\": \"2026-05-16T09:55:45.253Z\"}, \"label_only_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T04:40:19.669Z\", \"updated_at\": \"2026-05-16T09:22:46.929Z\", \"hypothesis\": \"Seed robustness: label_only (full_trace + label-only loss) with seed=456 on Qwen-2.5-Coder-7B. Verifies label_only 86.22% stability across seeds.\", \"parent\": \"full_trace_label_only_seed42\", \"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-16T05:31:03.019Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition full_trace --label_only_loss --gradient_checkpointing --gpu 0 --seed 456 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_label_only_seed456 --wandb_project trace-verdict-study --wandb_run_name label_only_seed456 && python eval/evaluate.py --condition full_trace --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_label_only_seed456/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_label_only_seed456/final/eval_results.json --save_predictions\\\"\", \"wandb_run_id\": \"label_only_seed456\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\", \"finished_at\": \"2026-05-16T09:01:08.445Z\", \"training_hours\": 3.5}, \"spec\": {\"command\": \"python train/train_sft.py --condition full_trace --label_only_loss --gradient_checkpointing --gpu 0 --seed 456 + evaluate.py\", \"server\": \"westd-11235\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/full_trace_{train,test}.jsonl\", \"data_count\": 5910, \"model_name\": \"Qwen/Qwen2.5-Coder-7B-Instruct\", \"seed\": 456, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_label_only_seed456/final\", \"log_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_label_only_seed456/final/eval_results.json\"}, \"pid\": \"249616\", \"log_path\": \"~/runs/trace-verdict-study/label_only_seed456.log\", \"wandb_run_id\": \"label_only_seed456\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T09:01:14.180779+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.859, \"n\": 1190, \"pass_recall\": 0.938, \"fail_recall\": 0.661, \"pass_f1\": 0.905, \"fail_f1\": 0.727}, \"completed_at\": \"2026-05-16T09:22:46.929Z\"}, \"label_only_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T04:40:18.683Z\", \"updated_at\": \"2026-05-16T09:01:41.007Z\", \"hypothesis\": \"Seed robustness: label_only (full_trace + label-only loss) with seed=123 on Qwen-2.5-Coder-7B. Verifies label_only 86.22% stability across seeds.\", \"parent\": \"full_trace_label_only_seed42\", \"server\": \"westd-11235\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-11235\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-16T05:31:02.488Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition full_trace --label_only_loss --gradient_checkpointing --gpu 0 --seed 123 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_label_only_seed123 --wandb_project trace-verdict-study --wandb_run_name label_only_seed123 && python eval/evaluate.py --condition full_trace --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_label_only_seed123/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_label_only_seed123/final/eval_results.json --save_predictions\\\"\", \"wandb_run_id\": \"label_only_seed123\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\", \"finished_at\": \"2026-05-16T08:58:33.644Z\", \"training_hours\": 3.46}, \"spec\": {\"command\": \"python train/train_sft.py --condition full_trace --label_only_loss --gradient_checkpointing --gpu 0 --seed 123 + evaluate.py\", \"server\": \"westd-11235\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/full_trace_{train,test}.jsonl\", \"data_count\": 5910, \"model_name\": \"Qwen/Qwen2.5-Coder-7B-Instruct\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_label_only_seed123/final\", \"log_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_label_only_seed123/final/eval_results.json\"}, \"pid\": \"249124\", \"log_path\": \"~/runs/trace-verdict-study/label_only_seed123.log\", \"wandb_run_id\": \"label_only_seed123\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T08:58:35.632418+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.8706, \"n\": 1190, \"pass_recall\": 0.974, \"fail_recall\": 0.611, \"pass_f1\": 0.915, \"fail_f1\": 0.729}, \"completed_at\": \"2026-05-16T09:01:41.007Z\"}, \"exception_only_nomarker_seed456\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:12:12.683Z\", \"updated_at\": \"2026-05-16T07:49:12.477Z\", \"spec\": {\"hypothesis\": \"Task G: Format marker ablation — seed=456. Remove [No exception data in trace] marker from exception_only and retrain. Tests whether format marker affects model judgment.\", \"parent\": \"exception_only_seed42\", \"plan_id\": \"round5_task_g\"}}, \"exception_only_nomarker_seed123\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:12:11.533Z\", \"updated_at\": \"2026-05-16T07:49:11.150Z\", \"spec\": {\"hypothesis\": \"Task G: Format marker ablation — seed=123. Remove [No exception data in trace] marker from exception_only and retrain. Tests whether format marker affects model judgment.\", \"parent\": \"exception_only_seed42\", \"plan_id\": \"round5_task_g\"}}, \"exception_only_nomarker_seed42\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-16T06:03:33.324Z\", \"updated_at\": \"2026-05-16T07:49:09.923Z\", \"spec\": {\"hypothesis\": \"Task G: Format marker ablation — remove [TRACE_START]/[EXCEPTION]/etc markers from exception_only condition and retrain. Tests whether SFT relies on format markers or actual exception content.\", \"parent\": \"exception_only_seed42\", \"plan_id\": \"round5_task_g\"}}, \"ae_only_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T03:41:51.316Z\", \"updated_at\": \"2026-05-16T06:48:30.962Z\", \"hypothesis\": \"Seed robustness: ae_only with seed=456 on Qwen-2.5-Coder-7B. Verifies ae_only 99.92% is stable across seeds (Reviewer P0 requirement).\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition ae_only --gradient_checkpointing --gpu 0 --seed 456 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/ae_only_seed456 --wandb_project trace-verdict-study --wandb_run_name ae_only_seed456 && python eval/evaluate.py --condition ae_only --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/ae_only_seed456/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/ae_only_seed456/final/eval_results.json --save_predictions\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/ae_only_{train,test}.jsonl\", \"data_count\": 4720, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 456, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/ae_only_seed456/final\", \"log_path\": \"/tmp/ae_only_seed456.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T06:26:31.454Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T06:26:32.421Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T06:26:34.050811+00:00\"}]}, \"metrics\": {\"accuracy\": 0.9992, \"n\": 1190, \"majority_baseline\": 0.7151, \"lift\": 0.2841, \"seed_comparison\": {\"seed42_accuracy\": 0.9992, \"seed123_accuracy\": 0.9908, \"seed456_accuracy\": 0.9992, \"mean_accuracy\": 0.9964, \"std\": 0.0049, \"note\": \"2/3 seeds = 99.92%, seed123 = 99.08%. Mean = 99.64% ± 0.49\"}}}, \"ae_only_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T03:41:50.753Z\", \"updated_at\": \"2026-05-16T06:48:29.943Z\", \"hypothesis\": \"Seed robustness: ae_only with seed=123 on Qwen-2.5-Coder-7B. Verifies ae_only 99.92% is stable across seeds (Reviewer P0 requirement).\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition ae_only --gradient_checkpointing --gpu 0 --seed 123 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/ae_only_seed123 --wandb_project trace-verdict-study --wandb_run_name ae_only_seed123 && python eval/evaluate.py --condition ae_only --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/ae_only_seed123/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/ae_only_seed123/final/eval_results.json --save_predictions\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/ae_only_{train,test}.jsonl\", \"data_count\": 4720, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/ae_only_seed123\", \"log_path\": \"/tmp/ae_only_seed123.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T06:16:31.845Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T06:16:33.018Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T06:16:35.841653+00:00\"}]}, \"metrics\": {\"accuracy\": 0.9908, \"n\": 1190, \"pass_recall\": 0.987, \"fail_recall\": 1, \"majority_baseline\": 0.7151, \"lift\": 0.2757}, \"notes\": \"Cron 误判为 failed（进程死亡 5× 无 sentinel/W&B），Reviewer 独立核实训练+eval 均成功完成。accuracy=99.08% 低于 seed42/456 (99.92%)，ae_only 3-seed mean=99.64% ± 0.49。\"}, \"regex_baseline_analysis\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T03:43:17.799Z\", \"updated_at\": \"2026-05-16T04:08:29.402Z\", \"hypothesis\": \"Regex/heuristic baselines on exception_only test data. Tests if simple pattern matching can match SFT performance (Reviewer critical concern).\", \"conclusion\": \"success\", \"metrics\": {\"regex_B1_ERROR_presence\": 0.9345, \"regex_B2_Traceback\": 0.7151, \"regex_B3_any_keyword\": 0.9345, \"regex_B4_exception_type\": 0.9361, \"regex_B5_format_marker\": 0.9933, \"regex_B6_error_count_ge2\": 0.9202, \"sft_exception_only\": 0.9983, \"best_regex_gap_vs_sft\": -0.0622, \"B5_mcnemar_p\": 0.041, \"n\": 1190}, \"spec\": {\"checkpoint_path\": \"N/A (CPU analysis, no model)\", \"log_path\": \"N/A (CPU analysis)\"}, \"checkpoint_path\": \"N/A (analysis-only, no training)\", \"log_path\": \"N/A (analysis-only, no training)\", \"completed_at\": \"2026-05-16T04:08:09.296Z\"}, \"full_trace_2048tok_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:27:19.848Z\", \"updated_at\": \"2026-05-16T04:08:09.868Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition full_trace --data_dir /root/autodl-tmp/trace-verdict-study-data/ --model_path /root/trace-verdict-study/models/Qwen2.5-Coder-7B-Instruct --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_2048tok --max_trace_tokens 2048 --seed 42 --wandb_run_name full_trace_2048tok_seed42 --gradient_checkpointing && python eval/evaluate.py --condition full_trace --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_2048tok/final --gpu 0 --save_predictions --output /root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_2048tok/final/eval_results.json\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"220276\", \"log_path\": \"~/runs/trace-verdict-study/full_trace_2048tok_seed42.log\", \"submitted_at\": \"2026-05-16T01:35:43.979Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 9136.0, \"gpu_hours\": 2.54}, \"conclusion\": \"killed\", \"notes\": \"Director 取消：max_trace_tokens=2048 经 chat template overhead 后有效 trace ~1970 tok，与 no_limit (max_length=2048 封顶) 几乎一致。Token length ablation 最终设计改为 256/512/1024/no_limit 四点。\", \"completed_at\": \"2026-05-16T04:07:59.930Z\"}, \"deepseek_vota_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:13:39.391Z\", \"updated_at\": \"2026-05-16T02:45:56.773Z\", \"hypothesis\": \"Multi-model validation: VOTA on DeepSeek-Coder-6.7B-Instruct (plan_004). Tests if VOTA's verdict accuracy advantage generalizes beyond Qwen2.5-Coder to DCSH's same base model.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition vota --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_vota --gradient_checkpointing --gpu 0 --seed 42 --wandb_project trace-verdict-study --wandb_run_name deepseek_vota_seed42 && python eval/evaluate.py --condition vota --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_vota/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_vota/final/eval_results.json\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"93484\", \"log_path\": \"~/runs/trace-verdict-study/deepseek_vota_seed42.log\", \"submitted_at\": \"2026-05-15T10:45:36.891Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/vota_{train,test}.jsonl\", \"data_count\": 4720, \"model_name\": \"deepseek-ai/deepseek-coder-6.7b-instruct\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_vota/final\", \"wall_clock_seconds\": 8839.9, \"gpu_hours\": 2.46}, \"reproduce\": {\"finished_at\": \"2026-05-15T13:06:46.525Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T13:06:47.175122+00:00\"}]}, \"metrics\": {\"accuracy\": 0.8445, \"majority_baseline\": 0.7151, \"lift\": 0.1294, \"accuracy_ci\": [0.826, 0.864], \"pass_precision\": 0.821, \"pass_recall\": 1, \"pass_f1\": 0.902, \"fail_precision\": 1, \"fail_recall\": 0.454, \"fail_f1\": 0.625, \"eval_loss_epoch1\": 0.0679, \"eval_loss_epoch2\": 0.095, \"eval_loss_epoch3\": 0.1121, \"final_train_loss\": 0.0522, \"epoch1_checkpoint_eval\": {\"accuracy\": 0.7815, \"accuracy_ci\": [0.76, 0.803], \"fail_recall\": 0.233, \"fail_precision\": 1, \"pass_recall\": 1, \"pass_precision\": 0.766, \"fail_f1\": 0.378, \"pass_f1\": 0.867, \"conclusion\": \"epoch3_final_is_better\"}, \"reeval_with_fixed_script\": {\"accuracy\": 0.16, \"accuracy_ci\": [0.139, 0.18], \"fail_f1\": 0.61, \"fail_precision\": 0.9, \"fail_recall\": 0.47, \"pass_f1\": 0.07, \"pass_precision\": 1, \"pass_recall\": 0.04, \"note\": \"CATASTROPHIC: re-eval with corrected evaluate.py shows 16% (vs original 84.45%). Model predicts fail for almost everything. Previous 84.45% may have been from buggy eval. NEEDS INVESTIGATION.\"}, \"group_analysis\": {\"train_truncated\": {\"n\": 1091, \"accuracy\": 0.8304, \"ci_95\": [0.8075, 0.8524], \"correct\": 906, \"incorrect\": 185, \"pass_accuracy\": 1, \"pass_n\": 822, \"fail_accuracy\": 0.3123, \"fail_n\": 269}, \"train_intact\": {\"n\": 99, \"accuracy\": 1, \"ci_95\": [1, 1], \"correct\": 99, \"incorrect\": 0, \"pass_accuracy\": 1, \"pass_n\": 29, \"fail_accuracy\": 1, \"fail_n\": 70}, \"fisher_exact\": {\"odds_ratio\": 0, \"p_value\": 0}, \"overall_accuracy\": 0.8445, \"max_length\": 2048, \"note\": \"Grouped by whether training sample content exceeded token budget (DeepSeek tokenizer, max_length=2048). Inference used full-length input (no truncation). All 185 errors from truncated group's fail class (fail_recall=31.2%). Intact group: 100% accuracy.\"}}, \"conclusion\": \"success\", \"log_path\": \"/root/runs/trace-verdict-study/deepseek_vota_seed42.log\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_vota/final\", \"completed_at\": \"2026-05-15T13:12:56.838Z\", \"notes\": \"DeepSeek VOTA: 84.45% confirmed with max_length=16384 (re-verified 2026-05-16, exact match). max_length=2048 gives 16% due to evaluate.py front-truncation removing \\\"Answer: \\\" suffix from 91.7% of inputs. Training-time eval used old script (no truncation). exception_only/no_trace unaffected (short inputs). Systematic audit 2026-05-16: adapter base_model=DeepSeek confirmed, no model mixup possible.\"}, \"deepseek_full_trace_seed42_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:40:07.877Z\", \"updated_at\": \"2026-05-16T02:37:10.773Z\", \"hypothesis\": \"DeepSeek full_trace v3: retrain with label-preserving truncation fix in to_chat_text(). v1/v2 collapsed due to DeepSeek tokenizer producing >2048 tokens → SFTTrainer right-truncated labels. Tests if full_trace shows intermediate performance on DeepSeek (plan_004, 4th condition).\", \"parent\": \"\", \"notes\": \"DeepSeek full_trace v3: label-preserving truncation fix. 79.16% confirmed with max_length=2048 (matches training). eval_results.json has stale 28.49% from max_length=16384 run; correct value in eval_results_maxlen2048.json. predictions.jsonl overwritten 2026-05-16 with maxlen2048 results (reliable). Systematic audit 2026-05-16 confirmed: adapter base_model=DeepSeek, no model mixup possible (dimension mismatch would crash).\", \"spec\": {\"command\": \"python train_sft.py --condition full_trace --model deepseek-coder-6.7b --max_length 2048 --seed 42\", \"server\": \"westd-11235\", \"data_path\": \"/root/trace-verdict-study/data\", \"data_count\": 5910, \"model_name\": \"deepseek-ai/deepseek-coder-6.7b-instruct\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace_seed42_v3\", \"log_path\": \"/root/trace-verdict-study/logs/deepseek_full_trace_seed42_v3\"}, \"gpu\": \"cuda:1\", \"metrics\": {\"accuracy\": 0.7916, \"majority_baseline\": 0.7151, \"lift\": 0.0765, \"n\": 1190, \"pass_precision\": 0.857, \"pass_recall\": 0.851, \"pass_f1\": 0.854, \"fail_precision\": 0.632, \"fail_recall\": 0.643, \"fail_f1\": 0.637, \"accuracy_ci\": [0.768, 0.813], \"train_loss\": 0.0547, \"train_runtime_seconds\": 8891, \"epochs\": 3, \"reeval_discrepancy\": {\"reeval_accuracy\": 0.285, \"reeval_note\": \"RESOLVED: 28.5% was caused by eval max_length=16384 (OOD). Re-eval with max_length=2048 reproduces 79.16%. predictions.jsonl updated to maxlen2048 results.\", \"status\": \"RESOLVED\"}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T23:27:54.219Z\", \"log_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace_seed42_v3.log\"}, \"eval_missing_predictions_batch_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:41:02.286Z\", \"updated_at\": \"2026-05-16T02:12:47.505Z\", \"spec\": {\"command\": \"bash run_missing_predictions.sh 1\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"221213\", \"log_path\": \"~/runs/trace-verdict-study/eval_missing_predictions_batch_v2.log\", \"submitted_at\": \"2026-05-16T01:41:02.047Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"deepseek_full_trace_v3 + debugbench_vota predictions\", \"data_count\": 1616, \"model_name\": \"DeepSeek-Coder-6.7B + Qwen-2.5-Coder-7B\", \"seed\": 42, \"wall_clock_seconds\": 1905.5, \"gpu_hours\": 0.53}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval-only batch)\", \"completed_at\": \"2026-05-16T02:12:47.505Z\"}, \"debugbench_vota_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T23:33:57.931Z\", \"updated_at\": \"2026-05-16T01:58:42.269Z\", \"spec\": {\"hypothesis\": \"plan_005: VOTA on DebugBench (bug detection). Tests if VOTA's structured trace analysis provides additional signal beyond exception_only on a logic-error-dominated benchmark.\", \"model_name\": \"Qwen/Qwen2.5-Coder-7B-Instruct\", \"seed\": 42, \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/debugbench_vota_{train,test}.jsonl\", \"data_count\": {\"train\": 1622, \"test\": 426}, \"plan_id\": \"plan_005\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && ... && python train/train_sft.py --condition debugbench_vota --gradient_checkpointing --gpu 0 --seed 42 --output_dir .../debugbench_vota --wandb_project trace-verdict-study --wandb_run_name debugbench_vota_seed42 && python eval/evaluate.py --condition debugbench_vota --checkpoint_dir .../debugbench_vota/final --gpu 0\\\"\", \"server\": \"westd-11235\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_vota\", \"log_path\": \"~/runs/trace-verdict-study/debugbench_vota_seed42.log\"}, \"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-16T00:01:37.634Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition debugbench_vota --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_vota --wandb_project trace-verdict-study --wandb_run_name debugbench_vota_seed42 && python eval/evaluate.py --condition debugbench_vota --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_vota/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_vota/final/eval_results.json\\\"\", \"wandb_run_id\": \"debugbench_vota_seed42\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\", \"finished_at\": \"2026-05-16T00:55:26.974Z\", \"training_hours\": 0.9}, \"pid\": \"211253\", \"log_path\": \"~/runs/trace-verdict-study/debugbench_vota_seed42.log\", \"wandb_run_id\": \"debugbench_vota_seed42\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T00:55:28.620314+00:00\"}]}, \"metrics\": {\"accuracy\": 0.9977, \"majority_baseline\": 0.5141, \"lift\": 0.4836, \"n\": 426, \"pass_precision\": 1, \"pass_recall\": 1, \"pass_f1\": 1, \"fail_precision\": 1, \"fail_recall\": 1, \"fail_f1\": 1, \"accuracy_ci\": [0.993, 1], \"train_loss\": 0.098, \"eval_loss\": 0.1179, \"eval_mean_token_accuracy\": 0.9737, \"errors\": 1}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T00:58:14.197Z\", \"notes\": \"predictions.jsonl generated (426 lines). Accuracy=99.77%, matches registry. Path: /root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_vota/final/predictions.jsonl\"}, \"eval_missing_predictions_batch\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:33:51.923Z\", \"updated_at\": \"2026-05-16T01:58:38.428Z\", \"spec\": {\"command\": \"python eval/evaluate.py --save_predictions\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"219832\", \"log_path\": \"~/runs/trace-verdict-study/eval_missing_predictions_batch.log\", \"submitted_at\": \"2026-05-16T01:33:51.795Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/\", \"data_count\": 1616, \"model_name\": \"DeepSeek-Coder-6.7B + Qwen2.5-Coder-7B\", \"seed\": 42, \"wall_clock_seconds\": 1480.2, \"gpu_hours\": 0.41}, \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"/tmp/deepseek_eval_preds.log, /tmp/debugbench_vota_eval_preds.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T01:58:31.993Z\", \"notes\": \"predictions.jsonl generated for both experiments. deepseek_full_trace_seed42_v3: 1190 lines, accuracy=28.5% (NOT 79.16% as expected — model predicts all fail, same result with max_length=16384). debugbench_vota_seed42: 426 lines, accuracy=99.77% (matches registry). Paths: /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace_seed42_v3/final/predictions.jsonl, /root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_vota/final/predictions.jsonl\"}, \"full_trace_1024tok_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:27:17.607Z\", \"updated_at\": \"2026-05-16T01:57:18.837Z\", \"spec\": {\"hypothesis\": \"plan_006: trace length ablation - 1024 tokens. Tests if medium-length trace preserves enough signal to match or exceed untruncated full_trace (81.8%).\", \"model_name\": \"Qwen/Qwen2.5-Coder-7B-Instruct\", \"seed\": 42, \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/full_trace_{train,test}.jsonl\", \"data_count\": 4720, \"max_trace_tokens\": 1024, \"plan_id\": \"plan_006\", \"command\": \"train_sft.py --condition full_trace --max_trace_tokens 1024 + evaluate.py\", \"server\": \"westd-11235\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_1024tok\", \"log_path\": \"~/runs/trace-verdict-study/full_trace_1024tok_seed42.log\"}, \"server\": \"westd-11235\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-11235\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-16T00:15:42.746Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition full_trace --max_trace_tokens 1024 --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_1024tok --wandb_project trace-verdict-study --wandb_run_name full_trace_1024tok_seed42 && python eval/evaluate.py --condition full_trace --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_1024tok/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_1024tok/final/eval_results.json\\\"\", \"wandb_run_id\": \"full_trace_1024tok_seed42\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\", \"finished_at\": \"2026-05-16T01:54:26.200Z\", \"training_hours\": 1.65}, \"pid\": \"212643\", \"log_path\": \"~/runs/trace-verdict-study/full_trace_1024tok_seed42.log\", \"wandb_run_id\": \"full_trace_1024tok_seed42\", \"gpu_id\": \"cuda:0\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T01:54:27.781595+00:00\"}]}, \"metrics\": {\"accuracy\": 0.7723, \"majority_baseline\": 0.7151, \"lift\": 0.0571, \"n\": 1190, \"accuracy_ci\": [0.7487, 0.7958], \"pass_precision\": 0.9006, \"pass_recall\": 0.7662, \"pass_f1\": 0.8279, \"fail_precision\": 0.573, \"fail_recall\": 0.7876, \"fail_f1\": 0.6634, \"train_loss\": 0.0634, \"train_runtime_sec\": 5553, \"epochs\": 3}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-16T01:56:53.352Z\"}, \"debugbench_exception_only_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T23:33:52.790Z\", \"updated_at\": \"2026-05-16T01:35:56.671Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition debugbench_exception_only --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_exception_only --wandb_project trace-verdict-study --wandb_run_name debugbench_exception_only_seed42 && python eval/evaluate.py --condition debugbench_exception_only --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_exception_only/final --gpu 0 --save_predictions --output /root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_exception_only/final/eval_results.json\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"216806\", \"log_path\": \"~/runs/trace-verdict-study/debugbench_exception_only_seed42.log\", \"submitted_at\": \"2026-05-16T01:11:57.937Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1255.3, \"gpu_hours\": 0.35}, \"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"pid\": \"216806\", \"log_path\": \"~/runs/trace-verdict-study/debugbench_exception_only_seed42.log\", \"wandb_run_id\": \"debugbench_exception_only_seed42\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition debugbench_exception_only --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_exception_only --wandb_project trace-verdict-study --wandb_run_name debugbench_exception_only_seed42 && python eval/evaluate.py --condition debugbench_exception_only --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_exception_only/final --gpu 0 --save_predictions --output /root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_exception_only/final/eval_results.json\\\"\", \"wandb_run_id\": \"debugbench_exception_only_seed42\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\", \"finished_at\": \"2026-05-16T01:27:40.798Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T01:27:43.171585+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 1, \"majority_baseline\": 0.5141, \"lift\": 0.4859, \"n\": 426, \"pass_precision\": 1, \"pass_recall\": 1, \"pass_f1\": 1, \"fail_precision\": 1, \"fail_recall\": 1, \"fail_f1\": 1, \"accuracy_ci_wilson\": [0.9914, 1], \"accuracy_ci_bootstrap\": [1, 1], \"train_loss\": 0.2435, \"eval_loss\": 0.4157, \"train_runtime_sec\": 837}, \"notes\": \"100.0% accuracy (426/426 完美预测)。exception_only 在 DebugBench 上超越 VOTA (99.77%) 和 no_trace (96.71%)。Checkpoint: /root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_exception_only/final/。Predictions: predictions.jsonl (426条)。\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_exception_only/final/\", \"completed_at\": \"2026-05-16T01:32:53.272Z\", \"predictions_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_exception_only/final/predictions.jsonl\"}, \"deepseek_exception_only_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:19:31.586Z\", \"updated_at\": \"2026-05-16T01:16:41.387Z\", \"hypothesis\": \"Cross-model seed robustness: exception_only seed=456 on DeepSeek-Coder-6.7B. Third seed to determine if seed42 (99.83%) is outlier or seed123 (91.09%) is outlier.\", \"parent\": \"deepseek_exception_only_seed123\", \"spec\": {\"command\": \"python train/train_sft.py --condition exception_only --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_exception_only_seed456 --gradient_checkpointing --gpu 0 --seed 456 --wandb_project trace-verdict-study --wandb_run_name deepseek_exception_only_seed456\", \"server\": \"westd-11235\", \"model_name\": \"deepseek-ai/deepseek-coder-6.7b-instruct\", \"seed\": 456, \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/exception_only_{train,test}.jsonl\", \"data_count\": 4720, \"checkpoint_source\": \"N/A - training run\", \"eval_data\": \"N/A - training run\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T22:08:34.111Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T22:08:35.359157+00:00\"}]}, \"metrics\": {\"accuracy\": 0.9933, \"majority_baseline\": 0.7151, \"lift\": 0.2782, \"n\": 1190, \"pass_precision\": 1, \"pass_recall\": 0.9906, \"pass_f1\": 0.9953, \"fail_precision\": 0.9769, \"fail_recall\": 1, \"fail_f1\": 0.9883, \"accuracy_ci\": [0.9882, 0.9975], \"train_loss\": 0.1225, \"eval_loss\": 0.4824, \"train_runtime_sec\": 6246, \"seed_comparison\": {\"seed42_accuracy\": 0.9933, \"seed456_accuracy\": 0.9933, \"seed123_accuracy\": 0.9109, \"note\": \"seed42 and seed456 identical (99.33%); seed123 outlier (91.09%). 2/3 seeds robust.\"}, \"epoch1_checkpoint_eval\": {\"accuracy\": 0.993, \"accuracy_ci\": [0.988, 0.997], \"fail_f1\": 0.99, \"fail_precision\": 0.98, \"fail_recall\": 1, \"pass_f1\": 1, \"pass_precision\": 1, \"pass_recall\": 0.99, \"conclusion\": \"epoch1 (99.3%) ≈ epoch3 (99.33%), 1 epoch convergence confirmed\"}}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_exception_only_seed456/final\", \"log_path\": \"/root/runs/trace-verdict-study/deepseek_exception_only_seed456.log\", \"conclusion\": \"success\", \"notes\": \"seed456 accuracy 99.33% = seed42 99.33%（完全一致）。seed123 (91.09%) 是离群值——2/3 seeds 在 DeepSeek 上稳定。Epoch1 checkpoint (checkpoint-148) 可用于 epoch1 eval。Eval 由 on_complete hook 的 eval 脚本 (PID 166680) 自动运行，结果写入 final/eval_results.json。\", \"completed_at\": \"2026-05-15T22:13:38.554Z\", \"outputs\": {\"predictions_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_exception_only_seed456/checkpoint-148/predictions.jsonl\"}}, \"deepseek_exception_only_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:31:02.686Z\", \"updated_at\": \"2026-05-16T01:16:41.099Z\", \"spec\": {\"command\": \"bash -c \\\"... train_sft.py --condition exception_only --seed 123 + evaluate.py\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"144507\", \"log_path\": \"~/runs/trace-verdict-study/deepseek_exception_only_seed123.log\", \"submitted_at\": \"2026-05-15T18:14:56.180Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"plan_id\": \"plan_008\", \"model_name\": \"deepseek-ai/deepseek-coder-6.7b-instruct\", \"seed\": 123, \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/exception_only_{train,test}.jsonl\", \"data_count\": 4720, \"wall_clock_seconds\": 6785.9, \"gpu_hours\": 1.88}, \"hypothesis\": \"Cross-model seed robustness: exception_only with seed=123 on DeepSeek-Coder-6.7B (plan_008). Further validates exception signal cross-model generalization (99.33% seed42).\", \"reproduce\": {\"finished_at\": \"2026-05-15T20:04:43.247Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T20:04:44.489564+00:00\"}]}, \"metrics\": {\"accuracy\": 0.9109, \"pass_precision\": 1, \"pass_recall\": 0.993, \"pass_f1\": 0.996, \"fail_precision\": 0.976, \"fail_recall\": 0.705, \"fail_f1\": 0.818, \"ci_95\": [0.894, 0.926], \"train_loss\": 0.122, \"train_runtime_sec\": 6384}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_exception_only_seed123/final\", \"log_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_exception_only_seed123/final/predictions.jsonl\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-15T20:08:02.101Z\", \"notes\": \"NEGATIVE: accuracy 91.09% vs seed42 99.83% (-8.74pp). fail_recall=0.705, train_loss=0.122 偏高。DeepSeek exception_only 对 seed 不鲁棒，seed42 的 99.83% 可能是 LoRA 初始化运气。Exception signal 仍有效（+19.6pp over baseline）但跨模型稳定性不成立。\", \"outputs\": {\"predictions_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_exception_only_seed123/checkpoint-148/predictions.jsonl\"}}, \"deepseek_exception_only_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:17:07.674Z\", \"updated_at\": \"2026-05-16T01:16:38.239Z\", \"hypothesis\": \"Multi-model validation: exception_only on DeepSeek-Coder-6.7B-Instruct (plan_004). Tests if exception dominance (99.83% on Qwen) generalizes across models — the most valuable cross-model evidence.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition exception_only --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_exception_only --gradient_checkpointing --gpu 0 --seed 42 --wandb_project trace-verdict-study --wandb_run_name deepseek_exception_only_seed42 && python eval/evaluate.py --condition exception_only --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_exception_only/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_exception_only/final/eval_results.json\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"107188\", \"log_path\": \"~/runs/trace-verdict-study/deepseek_exception_only_seed42.log\", \"submitted_at\": \"2026-05-15T13:10:32.405Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/exception_only_{train,test}.jsonl\", \"data_count\": 4720, \"model_name\": \"deepseek-ai/deepseek-coder-6.7b-instruct\", \"seed\": 42, \"wall_clock_seconds\": 7358.8, \"gpu_hours\": 2.04}, \"reproduce\": {\"finished_at\": \"2026-05-15T15:06:51.643Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T15:06:52.877301+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_exception_only/final\", \"metrics\": {\"accuracy\": 0.9933, \"majority_baseline\": 0.7151, \"lift\": 0.2782, \"n\": 1190, \"pass_precision\": 1, \"pass_recall\": 0.9906, \"pass_f1\": 0.9953, \"fail_precision\": 0.9769, \"fail_recall\": 1, \"fail_f1\": 0.9883, \"epoch1_checkpoint_eval\": {\"accuracy\": 0.9983, \"fail_recall\": 1, \"fail_precision\": 0.9941, \"pass_recall\": 0.9976, \"conclusion\": \"epoch1_better_by_0.50pp\"}}, \"completed_at\": \"2026-05-15T15:13:11.215Z\", \"notes\": \"epoch 1 (step 148) accuracy = 99.83%，高于 final (epoch 3) 的 99.33%。eval_loss epoch 2→3 从 0.413 涨到 0.476 (+15%)。continued training 导致 token-level 过拟合，verdict accuracy 从 99.83% 降到 99.33% (-0.50pp)。这是 eval_loss/accuracy 解耦的又一例证——但此处 eval_loss 上升确实伴随 accuracy 下降，与 DeepSeek VOTA 的趋势相反。Epoch 1 的 99.83% 与 Qwen exception_only (99.83%) 完全一致——跨模型 gap = 0pp（在最佳 checkpoint 下）。\", \"outputs\": {\"predictions_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_exception_only/checkpoint-148/predictions.jsonl\"}}, \"deepseek_no_trace_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:13:40.004Z\", \"updated_at\": \"2026-05-16T01:16:37.143Z\", \"hypothesis\": \"Multi-model baseline: no-trace verdict prediction on DeepSeek-Coder-6.7B-Instruct (plan_004). Establishes DeepSeek baseline for comparison with VOTA and full_trace conditions.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition no_trace --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_no_trace --gradient_checkpointing --gpu 0 --seed 42 --wandb_project trace-verdict-study --wandb_run_name deepseek_no_trace_seed42 && python eval/evaluate.py --condition no_trace --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_no_trace/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_no_trace/final/eval_results.json\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"106822\", \"log_path\": \"~/runs/trace-verdict-study/deepseek_no_trace_seed42.log\", \"submitted_at\": \"2026-05-15T13:09:35.611Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/no_trace_{train,test}.jsonl\", \"data_count\": 4720, \"model_name\": \"deepseek-ai/deepseek-coder-6.7b-instruct\", \"seed\": 42, \"wall_clock_seconds\": 1791.4, \"gpu_hours\": 0.5}, \"reproduce\": {\"finished_at\": \"2026-05-15T13:37:07.125Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T13:37:08.315605+00:00\"}]}, \"conclusion\": \"negative\", \"metrics\": {\"accuracy\": 0.7336, \"majority_baseline\": 0.7151, \"lift\": 0.0185, \"n\": 1190, \"pass_precision\": 0.817, \"pass_recall\": 0.808, \"pass_f1\": 0.813, \"fail_precision\": 0.532, \"fail_recall\": 0.546, \"fail_f1\": 0.539, \"accuracy_ci\": [0.708, 0.757], \"lift_ci\": [-0.009, 0.046]}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_no_trace/final\", \"log_path\": \"~/runs/trace-verdict-study/deepseek_no_trace_seed42.log\", \"completed_at\": \"2026-05-15T13:39:27.031Z\", \"notes\": \"Negative: lift +1.85pp over majority, 95% CI [-0.93, +4.63] crosses 0. DeepSeek-Coder-6.7B no-trace verdict prediction is not statistically different from majority baseline. Within-model VOTA lift: +11.09pp (84.45% - 73.36%).\", \"outputs\": {\"predictions_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_no_trace/final/predictions.jsonl\"}}, \"debugbench_no_trace_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T23:33:55.756Z\", \"updated_at\": \"2026-05-16T01:12:05.904Z\", \"spec\": {\"hypothesis\": \"plan_005: No-trace baseline on DebugBench. Establishes baseline for VOTA/exception_only comparison on bug detection task.\", \"model_name\": \"Qwen/Qwen2.5-Coder-7B-Instruct\", \"seed\": 42, \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/debugbench_no_trace_{train,test}.jsonl\", \"data_count\": {\"train\": 1622, \"test\": 426}, \"plan_id\": \"plan_005\", \"server\": \"westd-11235\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_no_trace\", \"log_path\": \"~/runs/trace-verdict-study/debugbench_no_trace_seed42.log\"}, \"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-16T00:58:18.036Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition debugbench_no_trace --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_no_trace --wandb_project trace-verdict-study --wandb_run_name debugbench_no_trace_seed42 && python eval/evaluate.py --condition debugbench_no_trace --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_no_trace/final --gpu 0 --save_predictions --output /root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_no_trace/final/eval_results.json\\\"\", \"wandb_run_id\": \"debugbench_no_trace_seed42\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\", \"finished_at\": \"2026-05-16T01:09:14.222Z\", \"training_hours\": 0.18}, \"pid\": \"215223\", \"log_path\": \"~/runs/trace-verdict-study/debugbench_no_trace_seed42.log\", \"wandb_run_id\": \"debugbench_no_trace_seed42\", \"gpu_id\": \"cuda:1\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T01:09:16.070113+00:00\"}]}, \"metrics\": {\"accuracy\": 0.9671, \"majority_baseline\": 0.5141, \"lift\": 0.4531, \"pass_precision\": 1, \"pass_recall\": 0.936, \"pass_f1\": 0.967, \"fail_precision\": 0.937, \"fail_recall\": 1, \"fail_f1\": 0.967, \"accuracy_ci\": [0.948, 0.984], \"train_loss\": 0.249, \"eval_loss\": 0.532}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T01:12:05.904Z\"}, \"full_trace_512tok_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:27:16.130Z\", \"updated_at\": \"2026-05-16T00:18:25.627Z\", \"spec\": {\"hypothesis\": \"plan_006: trace length ablation - 512 tokens. Tests accuracy with moderate trace length.\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/full_trace_{train,test}.jsonl\", \"data_count\": 4720, \"model_name\": \"Qwen/Qwen2.5-Coder-7B-Instruct\", \"seed\": 42, \"max_trace_tokens\": 512, \"plan_id\": \"plan_006\", \"command\": \"train_sft.py --condition full_trace --max_trace_tokens 512 --gradient_checkpointing --gpu 0 --seed 42 + evaluate.py\", \"server\": \"westd-11235\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_512tok/final\", \"log_path\": \"~/runs/trace-verdict-study/full_trace_512tok_seed42.log\"}, \"reproduce\": {\"pid\": 197608, \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-15T23:16:13Z\", \"wandb_run_name\": \"full_trace_512tok_seed42\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\"}, \"metrics\": {\"accuracy\": 0.8042, \"majority_baseline\": 0.7151, \"lift\": 0.0891, \"pass_precision\": 0.8705, \"pass_recall\": 0.8531, \"pass_f1\": 0.8617, \"fail_precision\": 0.6489, \"fail_recall\": 0.6814, \"fail_f1\": 0.6647, \"n\": 1190, \"accuracy_ci\": [0.7815, 0.8261]}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-16T00:14:32.967Z\"}, \"full_trace_256tok_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:27:14.119Z\", \"updated_at\": \"2026-05-16T00:03:55.505Z\", \"spec\": {\"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/full_trace_{train,test}.jsonl\", \"data_count\": 4720, \"model_name\": \"Qwen/Qwen2.5-Coder-7B-Instruct\", \"seed\": 42, \"max_trace_tokens\": 256}, \"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-15T23:05:57.749Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition full_trace --max_trace_tokens 256 --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_256tok --wandb_project trace-verdict-study --wandb_run_name full_trace_256tok_seed42 && python eval/evaluate.py --condition full_trace --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_256tok/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_256tok/final/eval_results.json\\\"\", \"wandb_run_id\": \"full_trace_256tok_seed42\", \"code_commit\": \"0836dd49526be55ab8571a3f716512d4ccd72312\", \"finished_at\": \"2026-05-16T00:01:15.610Z\", \"training_hours\": 0.92}, \"pid\": \"187860\", \"log_path\": \"~/runs/trace-verdict-study/full_trace_256tok_seed42.log\", \"wandb_run_id\": \"full_trace_256tok_seed42\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T00:01:17.060104+00:00\"}]}, \"metrics\": {\"accuracy\": 0.7882, \"majority_baseline\": 0.7151, \"lift\": 0.0731, \"n\": 1190, \"pass_precision\": 0.903, \"pass_recall\": 0.788, \"pass_f1\": 0.842, \"fail_precision\": 0.597, \"fail_recall\": 0.788, \"fail_f1\": 0.679, \"accuracy_ci\": [0.764, 0.81], \"train_loss\": 0.1094, \"train_runtime_sec\": 3047, \"epochs\": 3}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_256tok/final\", \"completed_at\": \"2026-05-16T00:03:55.505Z\"}, \"debugbench_exception_bug_fix\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T23:14:24.382Z\", \"updated_at\": \"2026-05-15T23:26:16.029Z\", \"spec\": {\"command\": \"python data/debugbench_format_data.py\", \"server\": \"westd-11235\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/debugbench/raw_traces.jsonl\", \"data_count\": 2048, \"model_name\": \"data_processing\", \"seed\": 42, \"checkpoint_path\": \"/root/trace-verdict-study/data/debugbench_format_data.py\", \"log_path\": \"/tmp/debugbench_format.log\"}, \"conclusion\": \"success\", \"hypothesis\": \"BUG FIX: compress_exception_only() only checked trace_raw events, missing 625/1006 empty-trace fails (syntax errors) + 5 event-capped samples. Fix: fallback to test_results.error. Exception signal 376→1006/1006, upper bound 69.2%→100%. DebugBench 30.5% empty trace rate confirmed.\", \"completed_at\": \"2026-05-15T23:26:16.029Z\"}, \"vota_seed456_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:39:05.494Z\", \"updated_at\": \"2026-05-15T21:04:28.008Z\", \"hypothesis\": \"Seed robustness: VOTA with seed=456, retry with --gradient_checkpointing (v1 OOM). Verifies VOTA 99.2% accuracy stable across seeds.\", \"notes\": \"Auto-retried from vota_seed456 (OOM). PID 146592, cuda:1, --gradient_checkpointing enabled. Started 18:31 UTC, ~2h to complete. Low priority per Director (VOTA not primary claim).\", \"parent\": \"vota_seed456\", \"spec\": {\"command\": \"python train/train_sft.py --condition vota --gradient_checkpointing --gpu 0 --seed 456 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/vota_seed456 --wandb_project trace-verdict-study --wandb_run_name vota_seed456_v2\", \"server\": \"westd-11235\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/vota_{train,test}.jsonl\", \"data_count\": 4720, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 456, \"checkpoint_source\": \"N/A (training, not eval)\", \"eval_data\": \"N/A (training, not eval)\"}, \"metrics\": {\"accuracy\": 0.9908, \"pass_precision\": 1, \"pass_recall\": 0.987, \"pass_f1\": 0.993, \"fail_precision\": 0.969, \"fail_recall\": 1, \"fail_f1\": 0.984, \"ci_95\": [0.985, 0.996]}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/vota_seed456/final\", \"log_path\": \"/root/runs/trace-verdict-study/vota_seed456.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T21:04:28.008Z\"}, \"no_trace_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:58:31.125Z\", \"updated_at\": \"2026-05-15T19:53:26.153Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export WANDB_API_KEY=[REDACTED] /root/.wandb_api_key 2>/dev/null || echo '') && cd /root/trace-verdict-study && python train/train_sft.py --condition no_trace --gpu 0 --wandb_project trace-verdict-study --wandb_run_name no_trace_seed42\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"709277\", \"log_path\": \"~/runs/trace-verdict-study/no_trace_seed42.log\", \"submitted_at\": \"2026-05-14T17:58:31.124Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 93295.0, \"gpu_hours\": 25.92}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:53:26.153Z\"}, \"no_trace_seed42_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:59:53.488Z\", \"updated_at\": \"2026-05-15T19:53:25.181Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export WANDB_API_KEY=[REDACTED] /root/.wandb_api_key 2>/dev/null || echo '') && cd /root/trace-verdict-study && python train/train_sft.py --condition no_trace --gpu 0 --wandb_project trace-verdict-study --wandb_run_name no_trace_seed42\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"709781\", \"log_path\": \"~/runs/trace-verdict-study/no_trace_seed42_v2.log\", \"submitted_at\": \"2026-05-14T17:59:53.485Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 93211.7, \"gpu_hours\": 25.89}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:53:25.181Z\"}, \"vota_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:58:32.967Z\", \"updated_at\": \"2026-05-15T19:53:23.979Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export WANDB_API_KEY=[REDACTED] /root/.wandb_api_key 2>/dev/null || echo '') && cd /root/trace-verdict-study && python train/train_sft.py --condition vota --gpu 1 --wandb_project trace-verdict-study --wandb_run_name vota_seed42\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"709357\", \"log_path\": \"~/runs/trace-verdict-study/vota_seed42.log\", \"submitted_at\": \"2026-05-14T17:58:32.964Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 93291.0, \"gpu_hours\": 25.91}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:53:23.979Z\"}, \"vota_seed42_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:59:55.517Z\", \"updated_at\": \"2026-05-15T19:53:22.853Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export WANDB_API_KEY=[REDACTED] /root/.wandb_api_key 2>/dev/null || echo '') && cd /root/trace-verdict-study && python train/train_sft.py --condition vota --gpu 1 --wandb_project trace-verdict-study --wandb_run_name vota_seed42\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"709863\", \"log_path\": \"~/runs/trace-verdict-study/vota_seed42_v2.log\", \"submitted_at\": \"2026-05-14T17:59:55.513Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 93207.3, \"gpu_hours\": 25.89}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:53:22.853Z\"}, \"vota_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T12:38:51.823Z\", \"updated_at\": \"2026-05-15T18:38:53.768Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition vota --gradient_checkpointing --gpu 0 --seed 456 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/vota_seed456 --wandb_project trace-verdict-study --wandb_run_name vota_seed456_v2 && python eval/evaluate.py --condition vota --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/vota_seed456/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/vota_seed456/final/eval_results.json --save_predictions --max_length 2048\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"146582\", \"log_path\": \"~/runs/trace-verdict-study/vota_seed456.log\", \"submitted_at\": \"2026-05-15T18:31:33.049Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 87.5, \"gpu_hours\": 0.02}, \"hypothesis\": \"Seed robustness: VOTA with seed=456 (plan_008). Verifies VOTA 99.2% accuracy is stable across random seeds.\", \"notes\": \"Original PID 145908 OOM'd ~3min after start. Auto-retried as v2 (PID 146592) with --gradient_checkpointing on cuda:1. Step 15/444 (3.4%) at 18:37 UTC, ~2h to complete. W&B run: vota_seed456_v2. Director 决策: 低优先级，exception_only seed robustness 优先。\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T18:33:00.592Z\"}, \"deepseek_full_trace_seed42_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:13:29.181Z\", \"updated_at\": \"2026-05-15T18:27:46.453Z\", \"hypothesis\": \"DeepSeek full_trace v2: retrain with v5 code (chat-template-aware truncation preserving labels). v1 collapsed to 28.49% due to label truncation during training.\", \"spec\": {\"plan_id\": \"plan_004\", \"model_name\": \"deepseek-ai/deepseek-coder-6.7b-instruct\", \"seed\": 42, \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/full_trace_{train,test}.jsonl\", \"data_count\": 4720, \"server\": \"westd-11235\", \"command\": \"train_sft.py --condition full_trace + evaluate.py\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace_v2\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T18:27:40.446Z\", \"notes\": \"Killed by worker_ops_kill_and_submit_vota_seed456 to free cuda:1 for vota_seed456. Training incomplete — needs re-run after GPU available. PID 144864 killed at ~18:24 UTC.\"}, \"deepseek_full_trace_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:13:40.756Z\", \"updated_at\": \"2026-05-15T18:23:42.993Z\", \"hypothesis\": \"Multi-model comparison: full-trace verdict prediction on DeepSeek-Coder-6.7B-Instruct (plan_004). Tests if full_trace also shows intermediate performance on DeepSeek-Coder.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition full_trace --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace --gradient_checkpointing --gpu 0 --seed 42 --wandb_project trace-verdict-study --wandb_run_name deepseek_full_trace_seed42 && python eval/evaluate.py --condition full_trace --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace/final/eval_results.json\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"112289\", \"log_path\": \"~/runs/trace-verdict-study/deepseek_full_trace_seed42.log\", \"submitted_at\": \"2026-05-15T13:47:47.241Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/full_trace_{train,test}.jsonl\", \"data_count\": 4720, \"model_name\": \"deepseek-ai/deepseek-coder-6.7b-instruct\", \"seed\": 42, \"wall_clock_seconds\": 10254.4, \"gpu_hours\": 2.85}, \"notes\": \"INVALIDATED: train-eval truncation mismatch。旧 eval (无截断): 28.49% (all predict fail)。修复后 eval (截断到 2048): 10.59% (模型输出垃圾 token: '{', 'execution', '{}', 'assert' 等, 从未输出 'pass')。结论：LoRA 本身训练失败，不仅是 eval 问题。truncation fix 暴露了更深层问题——训练时 label 被截断导致 LoRA 未学到有效分类行为。v2 重训已提交 (deepseek_full_trace_seed42_v2)。\", \"reproduce\": {\"finished_at\": \"2026-05-15T16:36:17.857Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T16:36:19.211594+00:00\"}]}, \"metrics\": {\"accuracy_no_truncation\": 0.2849, \"accuracy_with_truncation_fix\": 0.1059, \"accuracy_with_truncation_fix_ci\": [0.089, 0.123], \"majority_baseline\": 0.7151, \"n\": 1190, \"note\": \"Both evals show model failure. No-truncation: all predict fail. With-truncation: garbage tokens. LoRA training itself failed due to label truncation during training.\"}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace/final\", \"log_path\": \"~/runs/trace-verdict-study/deepseek_full_trace_seed42.log\", \"completed_at\": \"2026-05-15T16:38:41.604Z\"}, \"exception_only_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:31:01.555Z\", \"updated_at\": \"2026-05-15T18:03:37.166Z\", \"spec\": {\"plan_id\": \"plan_008a\", \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 123, \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/exception_only_{train,test}.jsonl\", \"data_count\": 4720, \"server\": \"westd-11235\"}, \"hypothesis\": \"Seed robustness: exception_only with seed=123 on Qwen-2.5-Coder-7B (plan_008). Verifies headline result 99.83% is stable across seeds.\", \"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-15T15:54:06.157Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition exception_only --gradient_checkpointing --gpu 0 --seed 123 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_seed123 --wandb_project trace-verdict-study --wandb_run_name exception_only_seed123 && python eval/evaluate.py --condition exception_only --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_seed123/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_seed123/final/eval_results.json\\\"\", \"wandb_run_id\": \"exception_only_seed123\", \"finished_at\": \"2026-05-15T18:00:50.835Z\", \"training_hours\": 2.11}, \"pid\": \"124197\", \"log_path\": \"~/runs/trace-verdict-study/exception_only_seed123.log\", \"wandb_run_id\": \"exception_only_seed123\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T18:00:52.169672+00:00\"}]}, \"notes\": \"Seed robustness 结论: exception_only 99.83% ± 0.00 (seeds 42/123/456), 每 seed 恰好 2/1190 errors。极大概率同一组 irreducible 样本。\", \"metrics\": {\"accuracy\": 0.9983, \"accuracy_ci\": [0.9958, 1], \"majority_baseline\": 0.7151, \"lift\": 0.2832, \"n\": 1190, \"pass_precision\": 1, \"pass_recall\": 0.9976, \"pass_f1\": 0.9988, \"fail_precision\": 0.9941, \"fail_recall\": 1, \"fail_f1\": 0.9971, \"train_loss\": 0.1096, \"train_runtime_sec\": 7507, \"epochs\": 3, \"seed_comparison\": {\"seed42_accuracy\": 0.9983, \"seed456_accuracy\": 0.9983, \"seed123_accuracy\": 0.9983, \"max_diff\": 0, \"note\": \"identical accuracy to 4 decimal places across all 3 seeds (42/456/123); each has exactly 2/1190 errors; exception_only fully seed-robust\"}}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_seed123/final\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T18:03:37.166Z\"}, \"exception_only_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:31:02.005Z\", \"updated_at\": \"2026-05-15T18:02:52.070Z\", \"spec\": {\"plan_id\": \"plan_008a\", \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 456, \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/exception_only_{train,test}.jsonl\", \"data_count\": 4720, \"server\": \"westd-11235\"}, \"hypothesis\": \"Seed robustness: exception_only with seed=456 on Qwen-2.5-Coder-7B (plan_008). Verifies headline result 99.83% is stable across seeds.\", \"server\": \"westd-11235\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-11235\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-15T16:38:44.142Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition exception_only --gradient_checkpointing --gpu 0 --seed 456 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_seed456 --wandb_project trace-verdict-study --wandb_run_name exception_only_seed456 && python eval/evaluate.py --condition exception_only --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_seed456/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_seed456/final/eval_results.json\\\"\", \"wandb_run_id\": \"exception_only_seed456\", \"finished_at\": \"2026-05-15T17:56:16.196Z\", \"training_hours\": 1.29}, \"pid\": \"129476\", \"log_path\": \"~/runs/trace-verdict-study/exception_only_seed456.log\", \"wandb_run_id\": \"exception_only_seed456\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:56:17.874949+00:00\"}]}, \"metrics\": {\"accuracy\": 0.9983, \"accuracy_ci\": [0.9958, 1], \"majority_baseline\": 0.7151, \"lift\": 0.2832, \"n\": 1190, \"pass_precision\": 1, \"pass_recall\": 0.9976, \"pass_f1\": 0.9988, \"fail_precision\": 0.9941, \"fail_recall\": 1, \"fail_f1\": 0.9971, \"vs_seed42\": {\"seed42_accuracy\": 0.9983, \"seed456_accuracy\": 0.9983, \"diff\": 0, \"note\": \"identical accuracy to 4 decimal places; no predictions.jsonl for paired bootstrap\"}, \"train_loss\": 0.1087, \"eval_loss\": 0.4629, \"train_runtime_sec\": 4541, \"epochs\": 3}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_seed456/final\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T17:58:25.389Z\", \"notes\": \"Seed robustness 结论: exception_only 99.83% ± 0.00 (seeds 42/123/456), 每 seed 恰好 2/1190 errors。极大概率同一组 irreducible 样本。\"}, \"vota_exception_only_seed42_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:16:14.602Z\", \"updated_at\": \"2026-05-15T18:02:36.534Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition exception_only --gradient_checkpointing --gpu 1 --seed 42 --wandb_project trace-verdict-study --wandb_run_name vota_exception_only_seed42_v2 && python eval/evaluate.py --condition exception_only --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/exception_only/final --gpu 1 --output /root/autodl-tmp/trace-verdict-study-checkpoints/exception_only/final/eval_results.json\\\"\", \"server\": \"westd-11235\", \"data_path\": \"exception_only\", \"data_count\": 4720, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 42, \"pid\": \"79633\", \"gpu\": [\"cuda:1\"], \"submitted_at\": \"2026-05-15T15:15:14Z\", \"log_path\": \"~/runs/trace-verdict-study/vota_exception_only_seed42_v2.log\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/exception_only/final\"}, \"hypothesis\": \"VOTA component ablation: exception_only condition — retry with --gradient_checkpointing (v1 OOM at step 8). Tests if [ERROR] events are the primary driver of VOTA's 99.2% accuracy (plan_003 sub-b)\", \"metrics\": {\"accuracy\": 0.9983, \"majority_baseline\": 0.7151, \"lift\": 0.2832, \"n\": 1190, \"pass_precision\": 1, \"pass_recall\": 0.998, \"pass_f1\": 0.999, \"fail_precision\": 0.994, \"fail_recall\": 1, \"fail_f1\": 0.997, \"lift_vs_notrace\": 0.2471, \"lift_vs_notrace_ci_lower\": 0.2227, \"lift_vs_notrace_ci_upper\": 0.2714, \"lift_vs_fulltrace\": 0.1807, \"lift_vs_fulltrace_ci_lower\": 0.1588, \"lift_vs_fulltrace_ci_upper\": 0.2034, \"lift_vs_vota\": 0.0067, \"lift_vs_vota_ci_lower\": 0.0017, \"lift_vs_vota_ci_upper\": 0.0126, \"lift_vs_vota_pvalue\": 0.01}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T09:35:01.676Z\", \"notes\": \"Seed robustness confirmed: exception_only 99.83% ± 0.00 across seeds 42/123/456. Each seed has exactly 2/1190 errors. High probability same irreducible samples. [re-eval] 修复后 evaluate.py 重跑 Δ=0。\"}, \"vota_seed123\": {\"status\": \"DONE\", \"retry_count\": 2, \"created_at\": \"2026-05-15T12:38:48.954Z\", \"updated_at\": \"2026-05-15T16:58:40.507Z\", \"hypothesis\": \"Seed robustness: VOTA with seed=123 (plan_008). Verifies VOTA 99.2% accuracy is stable across random seeds.\", \"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-15T12:39:38.117Z\", \"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition vota --gradient_checkpointing --gpu 0 --seed 123 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/vota_seed123 --wandb_project trace-verdict-study --wandb_run_name vota_seed123_v2 && python eval/evaluate.py --condition vota --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/vota_seed123/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/vota_seed123/final/eval_results.json\\\"\", \"finished_at\": \"2026-05-15T12:59:09.843Z\", \"training_hours\": 0.33, \"wandb_run_id\": \"vota_seed123_v2\"}, \"failure_reason\": \"CUDA OOM: CUDA out of memory. Tried to allocate 4.64 GiB. GPU 0 has a total capacity of 94.97 GiB of which 614.25 MiB is free. Process 93494 has 21.86 GiB memory in use. Including non-PyTorch memory, this process has 24.48 GiB memory in use. Of the allocated m\", \"completed_at\": \"2026-05-15T12:42:01.260Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T12:42:02.205055+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T12:59:14.689674+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"conclusion\": \"failed\", \"spec\": {\"plan_id\": \"plan_008b\", \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 123, \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/vota_{train,test}.jsonl\", \"data_count\": 4720, \"server\": \"westd-11235\"}}, \"full_trace_label_only_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T04:01:29.625Z\", \"updated_at\": \"2026-05-15T16:36:05.917Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_label_only/final\", \"log_path\": \"~/runs/trace-verdict-study/full_trace_label_only_seed42.log\"}, \"hypothesis\": \"Label-only loss on full_trace fixes gradient dilution collapse (plan_002: loss only on pass/fail token, not trace tokens)\", \"reproduce\": {\"finished_at\": \"2026-05-15T07:15:28.991Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T07:15:30.057513+00:00\"}]}, \"metrics\": {\"accuracy\": 0.8622, \"accuracy_ci_lower\": 0.8437, \"accuracy_ci_upper\": 0.8807, \"majority_baseline\": 0.7151, \"lift\": 0.1471, \"n\": 1190, \"pass_precision\": 0.8821, \"pass_recall\": 0.9318, \"pass_f1\": 0.9063, \"fail_precision\": 0.8007, \"fail_recall\": 0.6873, \"fail_f1\": 0.7397, \"train_loss\": 0.2505, \"eval_loss\": 0.3205, \"lift_vs_notrace\": 0.1109, \"lift_vs_notrace_ci_lower\": 0.0849, \"lift_vs_notrace_ci_upper\": 0.137, \"lift_vs_standard_fulltrace\": 0.0445, \"lift_vs_standard_fulltrace_ci_lower\": 0.0235, \"lift_vs_standard_fulltrace_ci_upper\": 0.0655, \"lift_vs_standard_fulltrace_pvalue\": 0}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T07:23:57.111Z\", \"notes\": \"Label-only loss 将 full_trace 从 81.8% 提升到 86.2% (+4.4pp)，确认 gradient dilution 是 full_trace 性能受限的部分原因。但 86.2% vs VOTA 99.2% 仍有 13pp gap，说明 gradient dilution 只是部分解释——trace 信息密度（VOTA 的 decision-relevant compression）才是主因。[2026-05-15 re-eval] 用修复后 evaluate.py + --condition full_trace 重跑，accuracy 不变 (86.22% → 86.22%, Δ=0)，predictions.jsonl 1190行已生成。训练确认使用 full_trace 格式数据，label_only 仅改变 loss mask。\"}, \"vota_no_ae_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T04:21:27.279Z\", \"updated_at\": \"2026-05-15T16:25:20.610Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition vota_no_ae --gpu 1 --seed 42 --wandb_project trace-verdict-study --wandb_run_name vota_no_ae_seed42\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"953133\", \"log_path\": \"~/runs/trace-verdict-study/vota_no_ae_seed42.log\", \"submitted_at\": \"2026-05-15T04:21:27.215Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/vota_no_ae_train.jsonl\", \"data_count\": 4720, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/vota_no_ae/final\", \"wall_clock_seconds\": 6902.4, \"gpu_hours\": 1.92}, \"hypothesis\": \"VOTA without actual/expected values: tests if VOTA's accuracy comes from genuine behavioral understanding vs trivial string comparison (plan_001)\", \"reproduce\": {\"finished_at\": \"2026-05-15T06:10:18.839Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T06:10:19.847891+00:00\"}]}, \"metrics\": {\"accuracy\": 0.994, \"majority_baseline\": 0.7151, \"lift\": 0.279, \"n\": 1190, \"pass_f1\": 0.996, \"fail_f1\": 0.989, \"accuracy_ci_lower\": 0.989, \"accuracy_ci_upper\": 0.998, \"lift_vs_notrace\": 0.243, \"lift_vs_notrace_ci_lower\": 0.218, \"lift_vs_notrace_ci_upper\": 0.268, \"train_loss\": 0.0908, \"eval_loss\": 0.2215, \"wall_clock_seconds\": 6397.88}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T06:16:29.587Z\", \"notes\": \"✅ Eval verified: accuracy 99.4% [98.9, 99.8] confirmed by evaluate.py + bootstrap. 去掉 actual/expected 后性能不降（vs VOTA v5 99.2%），证明 VOTA 效果来自 trace 行为模式理解而非 trivial string comparison。Claim 1 走 full positive framing。[2026-05-15 re-eval] 用修复后 evaluate.py 重跑，accuracy 不变 (99.41% → 99.41%, Δ=0)，predictions.jsonl 1190行已生成。\"}, \"vota_loop_only_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:02:41.201Z\", \"updated_at\": \"2026-05-15T16:25:16.352Z\", \"hypothesis\": \"VOTA component ablation: loop_only condition — only loop compression summaries, no actual/expected or exception. Tests loop behavioral pattern contribution to VOTA 99.2% accuracy (plan_003 sub-c)\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition loop_only --gradient_checkpointing --gpu 0 --seed 42 --wandb_project trace-verdict-study --wandb_run_name vota_loop_only_seed42 && python eval/evaluate.py --condition loop_only --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/loop_only/final --gpu 0\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"82362\", \"log_path\": \"~/runs/trace-verdict-study/vota_loop_only_seed42.log\", \"submitted_at\": \"2026-05-15T07:58:06.023Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/loop_only_{train,test}.jsonl\", \"data_count\": 4720, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 42, \"wall_clock_seconds\": 7952.5, \"gpu_hours\": 2.21}, \"reproduce\": {\"finished_at\": \"2026-05-15T10:04:53.052Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T10:04:54.341040+00:00\"}]}, \"metrics\": {\"accuracy\": 0.8563, \"majority_baseline\": 0.7151, \"lift\": 0.1412, \"n\": 1190, \"pass_precision\": 0.9239, \"pass_recall\": 0.8707, \"pass_f1\": 0.8966, \"fail_precision\": 0.7165, \"fail_recall\": 0.8201, \"fail_f1\": 0.7648, \"accuracy_ci\": [0.8353, 0.8756], \"bootstrap_vs_no_trace\": {\"diff\": 0.105, \"ci\": [0.0824, 0.1286], \"significant\": true}, \"bootstrap_vs_vota\": {\"diff\": -0.1378, \"ci\": [-0.1571, -0.1185], \"significant\": true}, \"bootstrap_vs_full_trace\": {\"diff\": 0.0387, \"ci\": [0.0185, 0.0597], \"significant\": true}, \"train_loss\": 0.0718, \"wall_clock_seconds\": 7425.65}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/loop_only/final/\", \"log_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/loop_only/final/eval_results.json\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T10:10:38.549Z\", \"notes\": \"[2026-05-15 re-eval] 用修复后 evaluate.py 重跑，accuracy 不变 (85.63% → 85.63%, Δ=0)，predictions.jsonl 1190行已生成。\"}, \"vota_ae_only_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:11:44.999Z\", \"updated_at\": \"2026-05-15T16:25:14.973Z\", \"hypothesis\": \"VOTA component ablation: ae_only condition — only actual/expected values, no exception/loop compression (plan_003 sub-a)\", \"notes\": \"ae_only accuracy 99.92% [99.75%, 100%]。与 exception_only (99.83%) 统计等价，均为 Tier 1 diagnostic-moment signals。88% 样本含 fallback locals 行（无信息量的模块命名空间导入），85% 样本含 [ASSERT] 行的 actual/expected 对比（合法诊断信息）。Reviewer 核实 fallback locals 不含 verdict 信号，不构成 data leakage（D013 裁定）。Train: 3 epochs, 444 steps, final train_loss=0.022, eval_loss=0.166, eval_token_acc=96.76%。[2026-05-15 re-eval] 用修复后 evaluate.py 重跑，accuracy 不变 (99.92% → 99.92%, Δ=0)，predictions.jsonl 1190行已生成。\", \"spec\": {\"command\": \"python train/train_sft.py --condition ae_only --gradient_checkpointing --gpu 1 --seed 42 --wandb_project trace-verdict-study --wandb_run_name vota_ae_only_seed42 && python eval/evaluate.py --condition ae_only --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/ae_only/final --gpu 1 --output /root/autodl-tmp/trace-verdict-study-checkpoints/ae_only/final/eval_results.json\", \"server\": \"westd-11235\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/ae_only_train.jsonl\", \"data_count\": 4720, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 42}, \"reproduce\": {\"finished_at\": \"2026-05-15T12:13:36.539Z\"}, \"failure_reason\": \"N/A — cron 误判。实际已完成，eval_results.json 已生成。process dead 5x 是因为训练+eval 正常结束后进程退出，cron 无 W&B/sentinel 检测通道。\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T12:13:36.813Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T12:13:37.756005+00:00\"}]}, \"metrics\": {\"accuracy\": 0.9992, \"accuracy_ci\": [0.9975, 1], \"bootstrap_pairwise\": {\"ae_only_vs_no_trace\": {\"diff\": 0.2479, \"ci\": [0.2235, 0.2731], \"p_value\": 0, \"significant\": true}, \"ae_only_vs_exception_only\": {\"diff\": 0.0008, \"ci\": [-0.0017, 0.0034], \"p_value\": 0.8002, \"significant\": false}, \"ae_only_vs_vota\": {\"diff\": 0.005, \"ci\": [0.0017, 0.0092], \"p_value\": 0.0046, \"significant\": true}}, \"config\": {\"n_bootstrap\": 10000, \"seed\": 42, \"method\": \"paired_bootstrap\"}}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/ae_only/final\", \"log_path\": \"~/runs/trace-verdict-study/vota_ae_only_seed42.log\"}, \"full_trace_seed42_v5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T01:46:03.068Z\", \"updated_at\": \"2026-05-15T15:50:39.179Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/full_trace/final/\", \"log_path\": \"~/runs/trace-verdict-study/full_trace_seed42_v5.log\", \"wall_clock_seconds\": 7852, \"gpu_hours\": 2.18}, \"hypothesis\": \"Full execution trace with chat-template-aware truncation provides verdict accuracy lift vs no-trace baseline (v5: fixed chat template overhead)\", \"reproduce\": {\"finished_at\": \"2026-05-15T03:58:14.030Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T03:58:14.897249+00:00\"}]}, \"metrics\": {\"accuracy\": 0.8176, \"majority_baseline\": 0.7151, \"lift\": 0.1025, \"n\": 1190, \"pass_precision\": 0.8774, \"pass_recall\": 0.866, \"pass_f1\": 0.8717, \"fail_precision\": 0.6743, \"fail_recall\": 0.6962, \"fail_f1\": 0.6851, \"accuracy_ci_lower\": 0.797, \"accuracy_ci_upper\": 0.839, \"lift_vs_notrace\": 0.0664, \"lift_vs_notrace_ci_lower\": 0.0437, \"lift_vs_notrace_ci_upper\": 0.0899, \"train_loss\": 0.05, \"eval_loss\": 0.0867, \"wall_clock_seconds\": 7852, \"epoch_level\": {\"epoch1_accuracy\": 0.8303, \"epoch2_accuracy\": 0.763, \"final_accuracy\": 0.8176, \"trend\": \"non_monotonic_epoch1_best_epoch2_collapse\"}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T04:06:20.880Z\", \"notes\": \"✅ Paired bootstrap CI (2026-05-15): lift vs no_trace = +6.6pp [4.4, 9.0]pp (significant, N=10000). lift_ci in registry [7.4, 13.2] was vs majority, not vs no_trace — now corrected.\"}, \"no_trace_seed42_v5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T01:46:17.948Z\", \"updated_at\": \"2026-05-15T15:50:35.449Z\", \"hypothesis\": \"Baseline: verdict accuracy without execution trace (v5: same code version as vota_v5/full_trace_v5 for fair comparison)\", \"conclusion\": \"success\", \"spec\": {\"command\": \"python train/train_sft.py --condition no_trace --gpu 1 --seed 42 --wandb_project trace-verdict-study --wandb_run_name no_trace_seed42_v5\", \"server\": \"westd-11235\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/no_trace_train.jsonl\", \"data_count\": 4720, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/no_trace/final\", \"log_path\": \"~/runs/trace-verdict-study/no_trace_seed42_v5.log\"}, \"completed_at\": \"2026-05-15T06:45:11.265Z\", \"metrics\": {\"accuracy\": 0.7513, \"accuracy_ci_lower\": 0.7277, \"accuracy_ci_upper\": 0.7748, \"majority_baseline\": 0.7151, \"lift\": 0.0361, \"lift_ci_lower\": 0.0042, \"lift_ci_upper\": 0.0706, \"n\": 1190, \"pass_precision\": 0.8776, \"pass_recall\": 0.7579, \"pass_f1\": 0.8134, \"fail_precision\": 0.5473, \"fail_recall\": 0.7345, \"fail_f1\": 0.6272, \"epoch_level\": {\"epoch1_accuracy\": 0.7429, \"epoch2_accuracy\": 0.763, \"final_accuracy\": 0.7513, \"trend\": \"non_monotonic_epoch2_best\"}}}, \"vota_seed42_v5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T01:46:04.015Z\", \"updated_at\": \"2026-05-15T15:50:32.123Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition vota --gpu 1 --wandb_project trace-verdict-study --wandb_run_name vota_seed42_v5\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"940786\", \"log_path\": \"~/runs/trace-verdict-study/vota_seed42_v5.log\", \"submitted_at\": \"2026-05-15T01:46:03.990Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/vota_train.jsonl\", \"data_count\": 4720, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/vota/final/\", \"wall_clock_seconds\": 8443, \"gpu_hours\": 2.35}, \"hypothesis\": \"VOTA trace provides verdict accuracy lift over no-trace baseline (v5: fixed chat template overhead, all labels preserved)\", \"reproduce\": {\"finished_at\": \"2026-05-15T04:08:40.446Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T04:08:41.358997+00:00\"}]}, \"metrics\": {\"accuracy\": 0.9941, \"majority_baseline\": 0.7151, \"lift\": 0.279, \"n\": 1190, \"pass_precision\": 1, \"pass_recall\": 0.9882, \"pass_f1\": 0.9941, \"fail_precision\": 0.9714, \"fail_recall\": 1, \"fail_f1\": 0.9855, \"lift_vs_notrace\": 0.2428, \"lift_vs_notrace_ci_lower\": 0.2185, \"lift_vs_notrace_ci_upper\": 0.2681, \"accuracy_ci_lower\": 0.9882, \"accuracy_ci_upper\": 0.9983, \"train_loss\": 0.05, \"eval_loss\": 0.0867, \"eval_mean_token_accuracy\": 0.9828, \"wall_clock_seconds\": 8443, \"epoch_level\": {\"epoch1_accuracy\": 0.9933, \"epoch2_accuracy\": 0.9941, \"final_accuracy\": 0.9941, \"trend\": \"monotonic_increasing_then_stable\"}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T04:21:27.059Z\"}, \"calibration_analysis_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T12:27:04.073Z\", \"updated_at\": \"2026-05-15T13:09:52.711Z\", \"spec\": {\"plan_id\": \"plan_007\", \"command\": \"python eval/calibration_analysis.py\", \"server\": \"westd-11235\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/\", \"data_count\": 1190, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 42}, \"hypothesis\": \"Calibration analysis: ECE + reliability diagrams for VOTA/exception_only/full_trace/no_trace. Tests whether VOTA's compressed traces improve model calibration beyond accuracy (plan_007).\", \"conclusion\": \"success\", \"metrics\": {\"no_trace\": {\"ece\": 0.171476, \"mce\": 0.475643, \"brier_score\": 0.197152, \"accuracy\": 0.751261, \"n_samples\": 1190}, \"full_trace\": {\"ece\": 0.095817, \"mce\": 0.249061, \"brier_score\": 0.143924, \"accuracy\": 0.817647, \"n_samples\": 1190}, \"label_only\": {\"ece\": 0.110686, \"mce\": 0.417124, \"brier_score\": 0.120144, \"accuracy\": 0.862185, \"n_samples\": 1190}, \"loop_only\": {\"ece\": 0.083085, \"mce\": 0.183406, \"brier_score\": 0.118335, \"accuracy\": 0.856303, \"n_samples\": 1190}, \"ae_only\": {\"ece\": 0.000415, \"mce\": 0.000415, \"brier_score\": 0.000847, \"accuracy\": 0.99916, \"n_samples\": 1190}, \"exception_only\": {\"ece\": 0.002717, \"mce\": 0.835484, \"brier_score\": 0.001311, \"accuracy\": 0.998319, \"n_samples\": 1190}, \"vota\": {\"ece\": 0.00541, \"mce\": 0.622459, \"brier_score\": 0.005234, \"accuracy\": 0.994118, \"n_samples\": 1190}}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/calibration/\", \"log_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/calibration/calibration_metrics.json\", \"completed_at\": \"2026-05-15T12:36:49.992Z\"}, \"vota_exception_only_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:02:39.821Z\", \"updated_at\": \"2026-05-15T07:16:20.123Z\", \"hypothesis\": \"VOTA component ablation: exception_only condition — only exception summaries, no actual/expected or loop compression. Tests if [ERROR] events are the primary driver of VOTA's 99.2% accuracy (plan_003 sub-b)\", \"spec\": {\"command\": \"python train/train_sft.py --condition exception_only --gpu 1 --seed 42 --wandb_project trace-verdict-study --wandb_run_name vota_exception_only_seed42 && python eval/evaluate.py --condition exception_only --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/exception_only/final --gpu 1\", \"server\": \"westd-11235\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/exception_only_{train,test}.jsonl\", \"data_count\": {\"train\": 4720, \"test\": 1190}, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"log_path\": \"~/runs/trace-verdict-study/vota_exception_only_seed42.log\", \"failure_reason\": \"OOM at step 8/444 — missing --gradient_checkpointing flag\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T07:16:20.123Z\"}, \"vota_seed42_v4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:12:38.660Z\", \"updated_at\": \"2026-05-15T01:37:13.355Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/vota/final/\", \"log_path\": \"~/runs/trace-verdict-study/vota_seed42_v4.log\", \"wall_clock_seconds\": 8160, \"gpu_hours\": 2.27}, \"hypothesis\": \"VOTA trace provides verdict accuracy lift over no-trace baseline (v4: removed match leakage + fixed label truncation)\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.9563, \"majority_baseline\": 0.7151, \"lift\": 0.2412, \"n\": 1190, \"pass_precision\": 0.944, \"pass_recall\": 0.998, \"pass_f1\": 0.97, \"fail_precision\": 0.993, \"fail_recall\": 0.853, \"fail_f1\": 0.917, \"lift_vs_notrace\": 0.205, \"lift_vs_notrace_ci_lower\": 0.177, \"lift_vs_notrace_ci_upper\": 0.234, \"train_loss\": 0.046, \"eval_loss\": 0.0842}, \"completed_at\": \"2026-05-15T01:10:45.307Z\"}, \"full_trace_seed42_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:12:46.333Z\", \"updated_at\": \"2026-05-15T01:10:45.707Z\", \"hypothesis\": \"Full execution trace with smart truncation (label preserved) provides verdict accuracy lift vs no-trace baseline\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/full_trace/final/\", \"log_path\": \"~/runs/trace-verdict-study/full_trace_seed42_v2.log\", \"wall_clock_seconds\": 7860, \"gpu_hours\": 2.18}, \"metrics\": {\"accuracy\": 0.284, \"majority_baseline\": 0.7151, \"lift\": -0.4311, \"n\": 1190, \"pass_precision\": 0.923, \"pass_recall\": 0.085, \"pass_f1\": 0.155, \"fail_precision\": 0.445, \"fail_recall\": 0.785, \"fail_f1\": 0.568, \"train_loss\": 0.0373, \"eval_loss\": 0.082, \"eval_mean_token_accuracy\": 0.984}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-15T01:10:45.708Z\"}, \"no_trace_seed42_v4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:12:37.755Z\", \"updated_at\": \"2026-05-14T22:39:32.197Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/no_trace/final/\", \"log_path\": \"~/runs/trace-verdict-study/no_trace_seed42_v4.log\", \"wall_clock_seconds\": 1274.7, \"gpu_hours\": 0.35}, \"hypothesis\": \"Baseline: verdict accuracy without execution trace (v4: fixed label truncation)\", \"reproduce\": {\"finished_at\": \"2026-05-14T22:34:36.523Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T22:34:37.283133+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.7513, \"majority_baseline\": 0.7151, \"lift\": 0.0361, \"pass_precision\": 0.8776, \"pass_recall\": 0.7579, \"pass_f1\": 0.8134, \"fail_precision\": 0.5473, \"fail_recall\": 0.7345, \"fail_f1\": 0.6272, \"train_loss\": 0.18, \"eval_loss\": 0.6454, \"eval_mean_token_accuracy\": 0.8897}, \"completed_at\": \"2026-05-14T22:39:12.249Z\"}, \"full_trace_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:38:06.325Z\", \"updated_at\": \"2026-05-14T22:12:18.859Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition full_trace --gpu 0 --wandb_project trace-verdict-study --wandb_run_name full_trace_seed42\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"712469\", \"log_path\": \"~/runs/trace-verdict-study/full_trace_seed42.log\", \"submitted_at\": \"2026-05-14T18:38:06.317Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/full_trace_train.jsonl\", \"data_count\": 4720, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 42, \"hypothesis\": \"Full execution trace (line-by-line Scratchpad format) provides verdict accuracy lift vs no-trace baseline\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/full_trace/final/\", \"wall_clock_seconds\": 11247.5, \"gpu_hours\": 3.12}, \"conclusion\": \"killed\", \"metrics\": {\"train_loss\": 0.037, \"eval_loss\": 0.084, \"eval_mean_token_accuracy\": 0.984, \"accuracy\": 0.284, \"majority_baseline\": 0.7151, \"lift\": -0.431, \"pass_precision\": 0.88, \"pass_recall\": 0.08, \"pass_f1\": 0.16, \"fail_precision\": 0.31, \"fail_recall\": 0.97, \"fail_f1\": 0.57}, \"completed_at\": \"2026-05-14T21:45:33.847Z\"}, \"no_trace_seed42_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:01:02.647Z\", \"updated_at\": \"2026-05-14T22:12:18.583Z\", \"spec\": {\"command\": \"python train/train_sft.py --condition no_trace --gpu 0\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"710523\", \"log_path\": \"~/runs/trace-verdict-study/no_trace_seed42_v3.log\", \"submitted_at\": \"2026-05-14T18:01:02.641Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/no_trace_train.jsonl\", \"data_count\": 4720, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 42, \"hypothesis\": \"Baseline: verdict accuracy without execution trace\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/no_trace/final/\", \"wall_clock_seconds\": 4617.5, \"gpu_hours\": 1.28}, \"conclusion\": \"killed\", \"metrics\": {\"train_loss\": 0.18, \"eval_loss\": 0.645, \"eval_mean_token_accuracy\": 0.89, \"accuracy\": 0.7513, \"majority_baseline\": 0.7151, \"lift\": 0.0361, \"pass_precision\": 0.8776, \"pass_recall\": 0.7579, \"pass_f1\": 0.8134, \"fail_precision\": 0.5473, \"fail_recall\": 0.7345, \"fail_f1\": 0.6272}, \"completed_at\": \"2026-05-14T19:18:00.158Z\"}, \"vota_seed42_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:01:04.345Z\", \"updated_at\": \"2026-05-14T21:51:40.917Z\", \"spec\": {\"command\": \"python train/train_sft.py --condition vota --gpu 1\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"710601\", \"log_path\": \"~/runs/trace-verdict-study/vota_seed42_v3.log\", \"submitted_at\": \"2026-05-14T18:01:04.338Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/vota_train.jsonl\", \"data_count\": 4720, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 42, \"hypothesis\": \"VOTA trace provides significant verdict accuracy lift over no-trace baseline\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/vota/final/\", \"wall_clock_seconds\": 13468.8, \"gpu_hours\": 3.74}, \"conclusion\": \"killed\", \"metrics\": {\"train_loss\": 0.046, \"eval_loss\": 0.085, \"eval_mean_token_accuracy\": 0.983, \"accuracy\": 0.992, \"majority_baseline\": 0.7151, \"lift\": 0.276, \"pass_precision\": 0.99, \"pass_recall\": 0.99, \"pass_f1\": 0.99, \"fail_precision\": 0.99, \"fail_recall\": 0.99, \"fail_f1\": 0.99}, \"completed_at\": \"2026-05-14T21:45:33.135Z\"}}, \"count\": 67, \"total\": 67, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2383}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 10_

<details><summary>Logged reasoning block</summary>

```text
The result is too large. Let me read it in chunks to get all the data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6cf6c7bc-54c9-45a8-b5e6-b498a2a84d18",
  "uuid": "cfba0136-479e-4d7c-bf93-cffa1e639d9d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GSFF2HopRmXtVPFLNK6zZZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 512,
      "cache_read_input_tokens": 24862,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 512
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

_source line 11_

Large registry. Let me read it in chunks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6cf6c7bc-54c9-45a8-b5e6-b498a2a84d18",
  "uuid": "f8251bc8-0cb5-4ed5-b770-be90ed2e8e04",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GSFF2HopRmXtVPFLNK6zZZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 512,
      "cache_read_input_tokens": 24862,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 512
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

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_01QqrzQPt7TdmwbgeLTFBxYt`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/6cf6c7bc-54c9-45a8-b5e6-b498a2a84d18/tool-results/mcp-agent-ml-research-read_registry-1778941588866.txt",
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6cf6c7bc-54c9-45a8-b5e6-b498a2a84d18",
  "uuid": "f933d8ba-7b8d-40c3-bdd5-7b8e7b5bf80b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GSFF2HopRmXtVPFLNK6zZZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 512,
      "cache_read_input_tokens": 24862,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 512
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

_source line 13 · 2026-05-16T14:26:32.648Z_

<details><summary>↩ Tool result · reported error · `toolu_01QqrzQPt7TdmwbgeLTFBxYt`</summary>

```text
File content (50552 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6cf6c7bc-54c9-45a8-b5e6-b498a2a84d18",
  "uuid": "90db69b8-3fab-42b4-b6c0-a224619f2155",
  "tool_use_result": "Error: File content (50552 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Read · `toolu_01W6tYzxYYwcQUTFsdVf3azr`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/6cf6c7bc-54c9-45a8-b5e6-b498a2a84d18/tool-results/mcp-agent-ml-research-read_registry-1778941588866.txt",
  "limit": 150,
  "offset": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6cf6c7bc-54c9-45a8-b5e6-b498a2a84d18",
  "uuid": "14602c0f-9f85-448b-85b5-0efbb27af815",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GxfQ79zBXPk4dVaq3VBjmV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 267,
      "cache_read_input_tokens": 25374,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 267
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

_source line 15 · 2026-05-16T14:26:36.211Z_

<details><summary>↩ Tool result · reported error · `toolu_01W6tYzxYYwcQUTFsdVf3azr`</summary>

```text
File content (50552 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6cf6c7bc-54c9-45a8-b5e6-b498a2a84d18",
  "uuid": "7deec30d-bfab-45ad-a581-0cd28774c192",
  "tool_use_result": "Error: File content (50552 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Bash · `toolu_01LSpK8E7MXeoioRZCoaLutR`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/6cf6c7bc-54c9-45a8-b5e6-b498a2a84d18/tool-results/mcp-agent-ml-research-read_registry-1778941588866.txt | python3 -c \"\nimport json, sys\n\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\n\n# Extract key fields for all experiments\nfor exp in result:\n    eid = exp.get('exp_id','?')\n    status = exp.get('status','?')\n    conclusion = exp.get('conclusion','')\n    metrics = exp.get('metrics', {})\n    hypothesis = exp.get('hypothesis','')\n    name = exp.get('name','')\n    config = exp.get('config', {})\n    \n    print(f'=== {eid} ===')\n    print(f'  name: {name}')\n    print(f'  status: {status}')\n    print(f'  conclusion: {conclusion}')\n    print(f'  metrics: {json.dumps(metrics)}')\n    # Extract model info from config or name\n    model = config.get('model','')\n    seed = config.get('seed','')\n    condition = config.get('condition','')\n    print(f'  model: {model}, seed: {seed}, condition: {condition}')\n    print()\n\" 2>&1 | head -800\n",
  "description": "Parse registry JSON and extract key experiment fields",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6cf6c7bc-54c9-45a8-b5e6-b498a2a84d18",
  "uuid": "81a8e248-1389-41c9-81a6-8452bbf1a0c1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011gsZypxGGEZHd2SGAK2wmb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 240,
      "cache_read_input_tokens": 25641,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 240
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

_source line 17 · 2026-05-16T14:26:45.597Z_

<details><summary>↩ Tool result · `toolu_01LSpK8E7MXeoioRZCoaLutR`</summary>

```text
Traceback (most recent call last):
  File "&lt;string>", line 9, in &lt;module>
    eid = exp.get('exp_id','?')
          ^^^^^^^
AttributeError: 'str' object has no attribute 'get'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6cf6c7bc-54c9-45a8-b5e6-b498a2a84d18",
  "uuid": "03e00131-ff81-4ff5-aa8a-4fe4c1e358f0",
  "tool_use_result": {
    "stdout": "Traceback (most recent call last):\n  File \"&lt;string>\", line 9, in &lt;module>\n    eid = exp.get('exp_id','?')\n          ^^^^^^^\nAttributeError: 'str' object has no attribute 'get'",
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

_source line 18_

<details open><summary>🔧 Tool call — Bash · `toolu_01PZyLWq1Njo9D9aHchb2Q6g`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/6cf6c7bc-54c9-45a8-b5e6-b498a2a84d18/tool-results/mcp-agent-ml-research-read_registry-1778941588866.txt | python3 -c \"\nimport json, sys\n\ndata = json.load(sys.stdin)\nresult_str = data['result']\n# Check what type result is\nprint(type(result_str))\nprint(result_str[:500])\n\" 2>&1\n",
  "description": "Inspect registry result structure",
  "timeout": 15000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6cf6c7bc-54c9-45a8-b5e6-b498a2a84d18",
  "uuid": "7a596d8b-142e-4cc3-8b3e-93d7c785476b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MWN9A4jbCb4x6QA2viSNwB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 546,
      "cache_read_input_tokens": 25881,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 546
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

_source line 19 · 2026-05-16T14:26:49.813Z_

<details><summary>↩ Tool result · `toolu_01PZyLWq1Njo9D9aHchb2Q6g`</summary>

```text
&lt;class 'str'>
{"success": true, "data": {"experiments": {"codellama13b_vota_seed42": {"status": "RUNNING", "retry_count": 0, "created_at": "2026-05-16T07:47:21.632Z", "updated_at": "2026-05-16T14:23:10.565Z", "spec": {"command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition vota --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf --gradient_checkpo
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6cf6c7bc-54c9-45a8-b5e6-b498a2a84d18",
  "uuid": "0ec8863a-091a-4676-956d-acf7f55b1ca1",
  "tool_use_result": {
    "stdout": "&lt;class 'str'>\n{\"success\": true, \"data\": {\"experiments\": {\"codellama13b_vota_seed42\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:47:21.632Z\", \"updated_at\": \"2026-05-16T14:23:10.565Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition vota --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf --gradient_checkpo",
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

<details open><summary>🔧 Tool call — Bash · `toolu_013WMPb5LugtX7pgm5SVWka7`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/6cf6c7bc-54c9-45a8-b5e6-b498a2a84d18/tool-results/mcp-agent-ml-research-read_registry-1778941588866.txt | python3 -c \"\nimport json, sys\n\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\nfor eid, exp in experiments.items():\n    status = exp.get('status','?')\n    metrics = exp.get('metrics', {})\n    conclusion = exp.get('conclusion','')\n    config = exp.get('config', {})\n    \n    # Try to extract accuracy from metrics\n    acc = metrics.get('accuracy', metrics.get('acc', ''))\n    ci = metrics.get('ci_95', metrics.get('confidence_interval', ''))\n    \n    print(f'{eid}')\n    print(f'  status={status}')\n    if metrics:\n        print(f'  metrics={json.dumps(metrics)}')\n    if conclusion:\n        print(f'  conclusion={conclusion[:200]}')\n    if config:\n        print(f'  config_keys={list(config.keys())}')\n    print()\n\" 2>&1 | head -1000\n",
  "description": "Parse registry experiments with metrics",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6cf6c7bc-54c9-45a8-b5e6-b498a2a84d18",
  "uuid": "f5651953-a766-424e-833c-a062ec0556ab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0176hz7JUyhXMRBVA93YNTTd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 457,
      "cache_read_input_tokens": 26427,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 457
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

_source line 21 · 2026-05-16T14:26:55.886Z_

<details><summary>↩ Tool result · `toolu_013WMPb5LugtX7pgm5SVWka7`</summary>

```text
codellama13b_vota_seed42
  status=RUNNING

codellama13b_no_trace_seed42
  status=DONE
  metrics={"accuracy": 0.765, "n": 1190, "majority_baseline": 0.7151, "lift": 0.05, "pass_precision": 0.84, "pass_recall": 0.83, "pass_f1": 0.84, "fail_precision": 0.59, "fail_recall": 0.59, "fail_f1": 0.59, "accuracy_ci": [0.738, 0.787]}
  conclusion=success

loop_only_seed456
  status=DONE
  metrics={"accuracy": 0.8664, "n": 1190, "pass_precision": 0.9179, "pass_recall": 0.8931, "pass_f1": 0.9053, "fail_precision": 0.7486, "fail_recall": 0.7994, "fail_f1": 0.7732, "accuracy_ci": [0.847, 0.884]}
  conclusion=success

qwen15b_full_trace_seed42
  status=DONE
  metrics={"accuracy": 0.7706, "n": 1190}
  conclusion=success

codellama13b_exception_only_seed42
  status=RUNNING

loop_only_seed123
  status=DONE
  metrics={"accuracy": 0.8588, "majority_baseline": 0.7151, "lift": 0.1437, "n": 1190, "pass_precision": 0.9129, "pass_recall": 0.8872, "pass_f1": 0.8999, "fail_precision": 0.7355, "fail_recall": 0.7876, "fail_f1": 0.7607, "accuracy_ci": [0.8403, 0.8773]}
  conclusion=success

codellama_vota_seed42
  status=QUEUED
  conclusion=killed

codellama_no_trace_seed42
  status=QUEUED
  conclusion=killed

codellama_exception_only_seed42
  status=QUEUED
  conclusion=killed

qwen1.5b_full_trace_seed42
  status=QUEUED
  conclusion=killed

qwen1.5b_vota_seed42
  status=QUEUED
  conclusion=killed

qwen1.5b_no_trace_seed42
  status=QUEUED
  conclusion=killed

qwen1.5b_exception_only_seed42
  status=QUEUED
  conclusion=killed

qwen15b_vota_seed42
  status=DONE
  metrics={"accuracy": 0.9958, "n": 1190, "pass_recall": 0.9976, "fail_recall": 0.9912, "pass_f1": 0.9971, "fail_f1": 0.9926, "training_time_sec": 2922}
  conclusion=success

qwen15b_no_trace_seed42
  status=DONE
  metrics={"accuracy": 0.6731, "n": 1190, "pass_f1": 0.7527, "fail_f1": 0.518, "lift_over_majority": -0.042, "training_time_sec": 851}
  conclusion=success

qwen15b_exception_only_seed42
  status=DONE
  metrics={"accuracy": 0.9983, "accuracy_ci_lower": 0.9958, "accuracy_ci_upper": 1, "majority_baseline": 0.7151, "lift": 0.283, "n": 1190, "pass_precision": 1, "pass_recall": 0.9976, "pass_f1": 0.9988, "fail_precision": 0.9941, "fail_recall": 1, "fail_f1": 0.9971, "train_loss": 0.1347, "eval_loss": 0.5761, "wall_clock_seconds": 1762}
  conclusion=success

label_only_seed456
  status=DONE
  metrics={"accuracy": 0.859, "n": 1190, "pass_recall": 0.938, "fail_recall": 0.661, "pass_f1": 0.905, "fail_f1": 0.727}
  conclusion=success

label_only_seed123
  status=DONE
  metrics={"accuracy": 0.8706, "n": 1190, "pass_recall": 0.974, "fail_recall": 0.611, "pass_f1": 0.915, "fail_f1": 0.729}
  conclusion=success

exception_only_nomarker_seed456
  status=QUEUED

exception_only_nomarker_seed123
  status=QUEUED

exception_only_nomarker_seed42
  status=QUEUED

ae_only_seed456
  status=DONE
  metrics={"accuracy": 0.9992, "n": 1190, "majority_baseline": 0.7151, "lift": 0.2841, "seed_comparison": {"seed42_accuracy": 0.9992, "seed123_accuracy": 0.9908, "seed456_accuracy": 0.9992, "mean_accuracy": 0.9964, "std": 0.0049, "note": "2/3 seeds = 99.92%, seed123 = 99.08%. Mean = 99.64% \u00b1 0.49"}}
  conclusion=success

ae_only_seed123
  status=DONE
  metrics={"accuracy": 0.9908, "n": 1190, "pass_recall": 0.987, "fail_recall": 1, "majority_baseline": 0.7151, "lift": 0.2757}
  conclusion=success

regex_baseline_analysis
  status=DONE
  metrics={"regex_B1_ERROR_presence": 0.9345, "regex_B2_Traceback": 0.7151, "regex_B3_any_keyword": 0.9345, "regex_B4_exception_type": 0.9361, "regex_B5_format_marker": 0.9933, "regex_B6_error_count_ge2": 0.9202, "sft_exception_only": 0.9983, "best_regex_gap_vs_sft": -0.0622, "B5_mcnemar_p": 0.041, "n": 1190}
  conclusion=success

full_trace_2048tok_seed42
  status=DONE
  conclusion=killed

deepseek_vota_seed42
  status=DONE
  metrics={"accuracy": 0.8445, "majority_baseline": 0.7151, "lift": 0.1294, "accuracy_ci": [0.826, 0.864], "pass_precision": 0.821, "pass_recall": 1, "pass_f1": 0.902, "fail_precision": 1, "fail_recall": 0.454, "fail_f1": 0.625, "eval_loss_epoch1": 0.0679, "eval_loss_epoch2": 0.095, "eval_loss_epoch3": 0.1121, "final_train_loss": 0.0522, "epoch1_checkpoint_eval": {"accuracy": 0.7815, "accuracy_ci": [0.76, 0.803], "fail_recall": 0.233, "fail_precision": 1, "pass_recall": 1, "pass_precision": 0.766, "fail_f1": 0.378, "pass_f1": 0.867, "conclusion": "epoch3_final_is_better"}, "reeval_with_fixed_script": {"accuracy": 0.16, "accuracy_ci": [0.139, 0.18], "fail_f1": 0.61, "fail_precision": 0.9, "fail_recall": 0.47, "pass_f1": 0.07, "pass_precision": 1, "pass_recall": 0.04, "note": "CATASTROPHIC: re-eval with corrected evaluate.py shows 16% (vs original 84.45%). Model predicts fail for almost everything. Previous 84.45% may have been from buggy eval. NEEDS INVESTIGATION."}, "group_analysis": {"train_truncated": {"n": 1091, "accuracy": 0.8304, "ci_95": [0.8075, 0.8524], "correct": 906, "incorrect": 185, "pass_accuracy": 1, "pass_n": 822, "fail_accuracy": 0.3123, "fail_n": 269}, "train_intact": {"n": 99, "accuracy": 1, "ci_95": [1, 1], "correct": 99, "incorrect": 0, "pass_accuracy": 1, "pass_n": 29, "fail_accuracy": 1, "fail_n": 70}, "fisher_exact": {"odds_ratio": 0, "p_value": 0}, "overall_accuracy": 0.8445, "max_length": 2048, "note": "Grouped by whether training sample content exceeded token budget (DeepSeek tokenizer, max_length=2048). Inference used full-length input (no truncation). All 185 errors from truncated group's fail class (fail_recall=31.2%). Intact group: 100% accuracy."}}
  conclusion=success

deepseek_full_trace_seed42_v3
  status=DONE
  metrics={"accuracy": 0.7916, "majority_baseline": 0.7151, "lift": 0.0765, "n": 1190, "pass_precision": 0.857, "pass_recall": 0.851, "pass_f1": 0.854, "fail_precision": 0.632, "fail_recall": 0.643, "fail_f1": 0.637, "accuracy_ci": [0.768, 0.813], "train_loss": 0.0547, "train_runtime_seconds": 8891, "epochs": 3, "reeval_discrepancy": {"reeval_accuracy": 0.285, "reeval_note": "RESOLVED: 28.5% was caused by eval max_length=16384 (OOD). Re-eval with max_length=2048 reproduces 79.16%. predictions.jsonl updated to maxlen2048 results.", "status": "RESOLVED"}}
  conclusion=success

eval_missing_predictions_batch_v2
  status=DONE
  conclusion=success

debugbench_vota_seed42
  status=DONE
  metrics={"accuracy": 0.9977, "majority_baseline": 0.5141, "lift": 0.4836, "n": 426, "pass_precision": 1, "pass_recall": 1, "pass_f1": 1, "fail_precision": 1, "fail_recall": 1, "fail_f1": 1, "accuracy_ci": [0.993, 1], "train_loss": 0.098, "eval_loss": 0.1179, "eval_mean_token_accuracy": 0.9737, "errors": 1}
  conclusion=success

eval_missing_predictions_batch
  status=DONE
  conclusion=success

full_trace_1024tok_seed42
  status=DONE
  metrics={"accuracy": 0.7723, "majority_baseline": 0.7151, "lift": 0.0571, "n": 1190, "accuracy_ci": [0.7487, 0.7958], "pass_precision": 0.9006, "pass_recall": 0.7662, "pass_f1": 0.8279, "fail_precision": 0.573, "fail_recall": 0.7876, "fail_f1": 0.6634, "train_loss": 0.0634, "train_runtime_sec": 5553, "epochs": 3}
  conclusion=negative

debugbench_exception_only_seed42
  status=DONE
  metrics={"accuracy": 1, "majority_baseline": 0.5141, "lift": 0.4859, "n": 426, "pass_precision": 1, "pass_recall": 1, "pass_f1": 1, "fail_precision": 1, "fail_recall": 1, "fail_f1": 1, "accuracy_ci_wilson": [0.9914, 1], "accuracy_ci_bootstrap": [1, 1], "train_loss": 0.2435, "eval_loss": 0.4157, "train_runtime_sec": 837}
  conclusion=success

deepseek_exception_only_seed456
  status=DONE
  metrics={"accuracy": 0.9933, "majority_baseline": 0.7151, "lift": 0.2782, "n": 1190, "pass_precision": 1, "pass_recall": 0.9906, "pass_f1": 0.9953, "fail_precision": 0.9769, "fail_recall": 1, "fail_f1": 0.9883, "accuracy_ci": [0.9882, 0.9975], "train_loss": 0.1225, "eval_loss": 0.4824, "train_runtime_sec": 6246, "seed_comparison": {"seed42_accuracy": 0.9933, "seed456_accuracy": 0.9933, "seed123_accuracy": 0.9109, "note": "seed42 and seed456 identical (99.33%); seed123 outlier (91.09%). 2/3 seeds robust."}, "epoch1_checkpoint_eval": {"accuracy": 0.993, "accuracy_ci": [0.988, 0.997], "fail_f1": 0.99, "fail_precision": 0.98, "fail_recall": 1, "pass_f1": 1, "pass_precision": 1, "pass_recall": 0.99, "conclusion": "epoch1 (99.3%) \u2248 epoch3 (99.33%), 1 epoch convergence confirmed"}}
  conclusion=success

deepseek_exception_only_seed123
  status=DONE
  metrics={"accuracy": 0.9109, "pass_precision": 1, "pass_recall": 0.993, "pass_f1": 0.996, "fail_precision": 0.976, "fail_recall": 0.705, "fail_f1": 0.818, "ci_95": [0.894, 0.926], "train_loss": 0.122, "train_runtime_sec": 6384}
  conclusion=negative

deepseek_exception_only_seed42
  status=DONE
  metrics={"accuracy": 0.9933, "majority_baseline": 0.7151, "lift": 0.2782, "n": 1190, "pass_precision": 1, "pass_recall": 0.9906, "pass_f1": 0.9953, "fail_precision": 0.9769, "fail_recall": 1, "fail_f1": 0.9883, "epoch1_checkpoint_eval": {"accuracy": 0.9983, "fail_recall": 1, "fail_precision": 0.9941, "pass_recall": 0.9976, "conclusion": "epoch1_better_by_0.50pp"}}
  conclusion=success

deepseek_no_trace_seed42
  status=DONE
  metrics={"accuracy": 0.7336, "majority_baseline": 0.7151, "lift": 0.0185, "n": 1190, "pass_precision": 0.817, "pass_recall": 0.808, "pass_f1": 0.813, "fail_precision": 0.532, "fail_recall": 0.546, "fail_f1": 0.539, "accuracy_ci": [0.708, 0.757], "lift_ci": [-0.009, 0.046]}
  conclusion=negative

debugbench_no_trace_seed42
  status=DONE
  metrics={"accuracy": 0.9671, "majority_baseline": 0.5141, "lift": 0.4531, "pass_precision": 1, "pass_recall": 0.936, "pass_f1": 0.967, "fail_precision": 0.937, "fail_recall": 1, "fail_f1": 0.967, "accuracy_ci": [0.948, 0.984], "train_loss": 0.249, "eval_loss": 0.532}
  conclusion=success

full_trace_512tok_seed42
  status=DONE
  metrics={"accuracy": 0.8042, "majority_baseline": 0.7151, "lift": 0.0891, "pass_precision": 0.8705, "pass_recall": 0.8531, "pass_f1": 0.8617, "fail_precision": 0.6489, "fail_recall": 0.6814, "fail_f1": 0.6647, "n": 1190, "accuracy_ci": [0.7815, 0.8261]}
  conclusion=negative

full_trace_256tok_seed42
  status=DONE
  metrics={"accuracy": 0.7882, "majority_baseline": 0.7151, "lift": 0.0731, "n": 1190, "pass_precision": 0.903, "pass_recall": 0.788, "pass_f1": 0.842, "fail_precision": 0.597, "fail_recall": 0.788, "fail_f1": 0.679, "accuracy_ci": [0.764, 0.81], "train_loss": 0.1094, "train_runtime_sec": 3047, "epochs": 3}
  conclusion=negative

debugbench_exception_bug_fix
  status=DONE
  conclusion=success

vota_seed456_v2
  status=DONE
  metrics={"accuracy": 0.9908, "pass_precision": 1, "pass_recall": 0.987, "pass_f1": 0.993, "fail_precision": 0.969, "fail_recall": 1, "fail_f1": 0.984, "ci_95": [0.985, 0.996]}
  conclusion=success

no_trace_seed42
  status=DONE
  conclusion=killed

no_trace_seed42_v2
  status=DONE
  conclusion=killed

vota_seed42
  status=DONE
  conclusion=killed

vota_seed42_v2
  status=DONE
  conclusion=killed

vota_seed456
  status=DONE
  conclusion=failed

deepseek_full_trace_seed42_v2
  status=DONE
  conclusion=killed

deepseek_full_trace_seed42
  status=DONE
  metrics={"accuracy_no_truncation": 0.2849, "accuracy_with_truncation_fix": 0.1059, "accuracy_with_truncation_fix_ci": [0.089, 0.123], "majority_baseline": 0.7151, "n": 1190, "note": "Both evals show model failure. No-truncation: all predict fail. With-truncation: garbage tokens. LoRA training itself failed due to label truncation during training."}
  conclusion=negative

exception_only_seed123
  status=DONE
  metrics={"accuracy": 0.9983, "accuracy_ci": [0.9958, 1], "majority_baseline": 0.7151, "lift": 0.2832, "n": 1190, "pass_precision": 1, "pass_recall": 0.9976, "pass_f1": 0.9988, "fail_precision": 0.9941, "fail_recall": 1, "fail_f1": 0.9971, "train_loss": 0.1096, "train_runtime_sec": 7507, "epochs": 3, "seed_comparison": {"seed42_accuracy": 0.9983, "seed456_accuracy": 0.9983, "seed123_accuracy": 0.9983, "max_diff": 0, "note": "identical accuracy to 4 decimal places across all 3 seeds (42/456/123); each has exactly 2/1190 errors; exception_only fully seed-robust"}}
  conclusion=success

exception_only_seed456
  status=DONE
  metrics={"accuracy": 0.9983, "accuracy_ci": [0.9958, 1], "majority_baseline": 0.7151, "lift": 0.2832, "n": 1190, "pass_precision": 1, "pass_recall": 0.9976, "pass_f1": 0.9988, "fail_precision": 0.9941, "fail_recall": 1, "fail_f1": 0.9971, "vs_seed42": {"seed42_accuracy": 0.9983, "seed456_accuracy": 0.9983, "diff": 0, "note": "identical accuracy to 4 decimal places; no predictions.jsonl for paired bootstrap"}, "train_loss": 0.1087, "eval_loss": 0.4629, "train_runtime_sec": 4541, "epochs": 3}
  conclusion=success

vota_exception_only_seed42_v2
  status=DONE
  metrics={"accuracy": 0.9983, "majority_baseline": 0.7151, "lift": 0.2832, "n": 1190, "pass_precision": 1, "pass_recall": 0.998, "pass_f1": 0.999, "fail_precision": 0.994, "fail_recall": 1, "fail_f1": 0.997, "lift_vs_notrace": 0.2471, "lift_vs_notrace_ci_lower": 0.2227, "lift_vs_notrace_ci_upper": 0.2714, "lift_vs_fulltrace": 0.1807, "lift_vs_fulltrace_ci_lower": 0.1588, "lift_vs_fulltrace_ci_upper": 0.2034, "lift_vs_vota": 0.0067, "lift_vs_vota_ci_lower": 0.0017, "lift_vs_vota_ci_upper": 0.0126, "lift_vs_vota_pvalue": 0.01}
  conclusion=success

vota_seed123
  status=DONE
  conclusion=failed

full_trace_label_only_seed42
  status=DONE
  metrics={"accuracy": 0.8622, "accuracy_ci_lower": 0.8437, "accuracy_ci_upper": 0.8807, "majority_baseline": 0.7151, "lift": 0.1471, "n": 1190, "pass_precision": 0.8821, "pass_recall": 0.9318, "pass_f1": 0.9063, "fail_precision": 0.8007, "fail_recall": 0.6873, "fail_f1": 0.7397, "train_loss": 0.2505, "eval_loss": 0.3205, "lift_vs_notrace": 0.1109, "lift_vs_notrace_ci_lower": 0.0849, "lift_vs_notrace_ci_upper": 0.137, "lift_vs_standard_fulltrace": 0.0445, "lift_vs_standard_fulltrace_ci_lower": 0.0235, "lift_vs_standard_fulltrace_ci_upper": 0.0655, "lift_vs_standard_fulltrace_pvalue": 0}
  conclusion=success

vota_no_ae_seed42
  status=DONE
  metrics={"accuracy": 0.994, "majority_baseline": 0.7151, "lift": 0.279, "n": 1190, "pass_f1": 0.996, "fail_f1": 0.989, "accuracy_ci_lower": 0.989, "accuracy_ci_upper": 0.998, "lift_vs_notrace": 0.243, "lift_vs_notrace_ci_lower": 0.218, "lift_vs_notrace_ci_upper": 0.268, "train_loss": 0.0908, "eval_loss": 0.2215, "wall_clock_seconds": 6397.88}
  conclusion=success

vota_loop_only_seed42
  status=DONE
  metrics={"accuracy": 0.8563, "majority_baseline": 0.7151, "lift": 0.1412, "n": 1190, "pass_precision": 0.9239, "pass_recall": 0.8707, "pass_f1": 0.8966, "fail_precision": 0.7165, "fail_recall": 0.8201, "fail_f1": 0.7648, "accuracy_ci": [0.8353, 0.8756], "bootstrap_vs_no_trace": {"diff": 0.105, "ci": [0.0824, 0.1286], "significant": true}, "bootstrap_vs_vota": {"diff": -0.1378, "ci": [-0.1571, -0.1185], "significant": true}, "bootstrap_vs_full_trace": {"diff": 0.0387, "ci": [0.0185, 0.0597], "significant": true}, "train_loss": 0.0718, "wall_clock_seconds": 7425.65}
  conclusion=success

vota_ae_only_seed42
  status=DONE
  metrics={"accuracy": 0.9992, "accuracy_ci": [0.9975, 1], "bootstrap_pairwise": {"ae_only_vs_no_trace": {"diff": 0.2479, "ci": [0.2235, 0.2731], "p_value": 0, "significant": true}, "ae_only_vs_exception_only": {"diff": 0.0008, "ci": [-0.0017, 0.0034], "p_value": 0.8002, "significant": false}, "ae_only_vs_vota": {"diff": 0.005, "ci": [0.0017, 0.0092], "p_value": 0.0046, "significant": true}}, "config": {"n_bootstrap": 10000, "seed": 42, "method": "paired_bootstrap"}}
  conclusion=success

full_trace_seed42_v5
  status=DONE
  metrics={"accuracy": 0.8176, "majority_baseline": 0.7151, "lift": 0.1025, "n": 1190, "pass_precision": 0.8774, "pass_recall": 0.866, "pass_f1": 0.8717, "fail_precision": 0.6743, "fail_recall": 0.6962, "fail_f1": 0.6851, "accuracy_ci_lower": 0.797, "accuracy_ci_upper": 0.839, "lift_vs_notrace": 0.0664, "lift_vs_notrace_ci_lower": 0.0437, "lift_vs_notrace_ci_upper": 0.0899, "train_loss": 0.05, "eval_loss": 0.0867, "wall_clock_seconds": 7852, "epoch_level": {"epoch1_accuracy": 0.8303, "epoch2_accuracy": 0.763, "final_accuracy": 0.8176, "trend": "non_monotonic_epoch1_best_epoch2_collapse"}}
  conclusion=success

no_trace_seed42_v5
  status=DONE
  metrics={"accuracy": 0.7513, "accuracy_ci_lower": 0.7277, "accuracy_ci_upper": 0.7748, "majority_baseline": 0.7151, "lift": 0.0361, "lift_ci_lower": 0.0042, "lift_ci_upper": 0.0706, "n": 1190, "pass_precision": 0.8776, "pass_recall": 0.7579, "pass_f1": 0.8134, "fail_precision": 0.5473, "fail_recall": 0.7345, "fail_f1": 0.6272, "epoch_level": {"epoch1_accuracy": 0.7429, "epoch2_accuracy": 0.763, "final_accuracy": 0.7513, "trend": "non_monotonic_epoch2_best"}}
  conclusion=success

vota_seed42_v5
  status=DONE
  metrics={"accuracy": 0.9941, "majority_baseline": 0.7151, "lift": 0.279, "n": 1190, "pass_precision": 1, "pass_recall": 0.9882, "pass_f1": 0.9941, "fail_precision": 0.9714, "fail_recall": 1, "fail_f1": 0.9855, "lift_vs_notrace": 0.2428, "lift_vs_notrace_ci_lower": 0.2185, "lift_vs_notrace_ci_upper": 0.2681, "accuracy_ci_lower": 0.9882, "accuracy_ci_upper": 0.9983, "train_loss": 0.05, "eval_loss": 0.0867, "eval_mean_token_accuracy": 0.9828, "wall_clock_seconds": 8443, "epoch_level": {"epoch1_accuracy": 0.9933, "epoch2_accuracy": 0.9941, "final_accuracy": 0.9941, "trend": "monotonic_increasing_then_stable"}}
  conclusion=success

calibration_analysis_seed42
  status=DONE
  metrics={"no_trace": {"ece": 0.171476, "mce": 0.475643, "brier_score": 0.197152, "accuracy": 0.751261, "n_samples": 1190}, "full_trace": {"ece": 0.095817, "mce": 0.249061, "brier_score": 0.143924, "accuracy": 0.817647, "n_samples": 1190}, "label_only": {"ece": 0.110686, "mce": 0.417124, "brier_score": 0.120144, "accuracy": 0.862185, "n_samples": 1190}, "loop_only": {"ece": 0.083085, "mce": 0.183406, "brier_score": 0.118335, "accuracy": 0.856303, "n_samples": 1190}, "ae_only": {"ece": 0.000415, "mce": 0.000415, "brier_score": 0.000847, "accuracy": 0.99916, "n_samples": 1190}, "exception_only": {"ece": 0.002717, "mce": 0.835484, "brier_score": 0.001311, "accuracy": 0.998319, "n_samples": 1190}, "vota": {"ece": 0.00541, "mce": 0.622459, "brier_score": 0.005234, "accuracy": 0.994118, "n_samples": 1190}}
  conclusion=success

vota_exception_only_seed42
  status=DONE
  conclusion=failed

vota_seed42_v4
  status=DONE
  metrics={"accuracy": 0.9563, "majority_baseline": 0.7151, "lift": 0.2412, "n": 1190, "pass_precision": 0.944, "pass_recall": 0.998, "pass_f1": 0.97, "fail_precision": 0.993, "fail_recall": 0.853, "fail_f1": 0.917, "lift_vs_notrace": 0.205, "lift_vs_notrace_ci_lower": 0.177, "lift_vs_notrace_ci_upper": 0.234, "train_loss": 0.046, "eval_loss": 0.0842}
  conclusion=success

full_trace_seed42_v2
  status=DONE
  metrics={"accuracy": 0.284, "majority_baseline": 0.7151, "lift": -0.4311, "n": 1190, "pass_precision": 0.923, "pass_recall": 0.085, "pass_f1": 0.155, "fail_precision": 0.445, "fail_recall": 0.785, "fail_f1": 0.568, "train_loss": 0.0373, "eval_loss": 0.082, "eval_mean_token_accuracy": 0.984}
  conclusion=negative

no_trace_seed42_v4
  status=DONE
  metrics={"accuracy": 0.7513, "majority_baseline": 0.7151, "lift": 0.0361, "pass_precision": 0.8776, "pass_recall": 0.7579, "pass_f1": 0.8134, "fail_precision": 0.5473, "fail_recall": 0.7345, "fail_f1": 0.6272, "train_loss": 0.18, "eval_loss": 0.6454, "eval_mean_token_accuracy": 0.8897}
  conclusion=success

full_trace_seed42
  status=DONE
  metrics={"train_loss": 0.037, "eval_loss": 0.084, "eval_mean_token_accuracy": 0.984, "accuracy": 0.284, "majority_baseline": 0.7151, "lift": -0.431, "pass_precision": 0.88, "pass_recall": 0.08, "pass_f1": 0.16, "fail_precision": 0.31, "fail_recall": 0.97, "fail_f1": 0.57}
  conclusion=killed

no_trace_seed42_v3
  status=DONE
  metrics={"train_loss": 0.18, "eval_loss": 0.645, "eval_mean_token_accuracy": 0.89, "accuracy": 0.7513, "majority_baseline": 0.7151, "lift": 0.0361, "pass_precision": 0.8776, "pass_recall": 0.7579, "pass_f1": 0.8134, "fail_precision": 0.5473, "fail_recall": 0.7345, "fail_f1": 0.6272}
  conclusion=killed

vota_seed42_v3
  status=DONE
  metrics={"train_loss": 0.046, "eval_loss": 0.085, "eval_mean_token_accuracy": 0.983, "accuracy": 0.992, "majority_baseline": 0.7151, "lift": 0.276, "pass_precision": 0.99, "pass_recall": 0.99, "pass_f1": 0.99, "fail_precision": 0.99, "fail_recall": 0.99, "fail_f1": 0.99}
  conclusion=killed
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6cf6c7bc-54c9-45a8-b5e6-b498a2a84d18",
  "uuid": "8051ea07-277f-4f79-9f37-03c69cb1e10b",
  "tool_use_result": {
    "stdout": "codellama13b_vota_seed42\n  status=RUNNING\n\ncodellama13b_no_trace_seed42\n  status=DONE\n  metrics={\"accuracy\": 0.765, \"n\": 1190, \"majority_baseline\": 0.7151, \"lift\": 0.05, \"pass_precision\": 0.84, \"pass_recall\": 0.83, \"pass_f1\": 0.84, \"fail_precision\": 0.59, \"fail_recall\": 0.59, \"fail_f1\": 0.59, \"accuracy_ci\": [0.738, 0.787]}\n  conclusion=success\n\nloop_only_seed456\n  status=DONE\n  metrics={\"accuracy\": 0.8664, \"n\": 1190, \"pass_precision\": 0.9179, \"pass_recall\": 0.8931, \"pass_f1\": 0.9053, \"fail_precision\": 0.7486, \"fail_recall\": 0.7994, \"fail_f1\": 0.7732, \"accuracy_ci\": [0.847, 0.884]}\n  conclusion=success\n\nqwen15b_full_trace_seed42\n  status=DONE\n  metrics={\"accuracy\": 0.7706, \"n\": 1190}\n  conclusion=success\n\ncodellama13b_exception_only_seed42\n  status=RUNNING\n\nloop_only_seed123\n  status=DONE\n  metrics={\"accuracy\": 0.8588, \"majority_baseline\": 0.7151, \"lift\": 0.1437, \"n\": 1190, \"pass_precision\": 0.9129, \"pass_recall\": 0.8872, \"pass_f1\": 0.8999, \"fail_precision\": 0.7355, \"fail_recall\": 0.7876, \"fail_f1\": 0.7607, \"accuracy_ci\": [0.8403, 0.8773]}\n  conclusion=success\n\ncodellama_vota_seed42\n  status=QUEUED\n  conclusion=killed\n\ncodellama_no_trace_seed42\n  status=QUEUED\n  conclusion=killed\n\ncodellama_exception_only_seed42\n  status=QUEUED\n  conclusion=killed\n\nqwen1.5b_full_trace_seed42\n  status=QUEUED\n  conclusion=killed\n\nqwen1.5b_vota_seed42\n  status=QUEUED\n  conclusion=killed\n\nqwen1.5b_no_trace_seed42\n  status=QUEUED\n  conclusion=killed\n\nqwen1.5b_exception_only_seed42\n  status=QUEUED\n  conclusion=killed\n\nqwen15b_vota_seed42\n  status=DONE\n  metrics={\"accuracy\": 0.9958, \"n\": 1190, \"pass_recall\": 0.9976, \"fail_recall\": 0.9912, \"pass_f1\": 0.9971, \"fail_f1\": 0.9926, \"training_time_sec\": 2922}\n  conclusion=success\n\nqwen15b_no_trace_seed42\n  status=DONE\n  metrics={\"accuracy\": 0.6731, \"n\": 1190, \"pass_f1\": 0.7527, \"fail_f1\": 0.518, \"lift_over_majority\": -0.042, \"training_time_sec\": 851}\n  conclusion=success\n\nqwen15b_exception_only_seed42\n  status=DONE\n  metrics={\"accuracy\": 0.9983, \"accuracy_ci_lower\": 0.9958, \"accuracy_ci_upper\": 1, \"majority_baseline\": 0.7151, \"lift\": 0.283, \"n\": 1190, \"pass_precision\": 1, \"pass_recall\": 0.9976, \"pass_f1\": 0.9988, \"fail_precision\": 0.9941, \"fail_recall\": 1, \"fail_f1\": 0.9971, \"train_loss\": 0.1347, \"eval_loss\": 0.5761, \"wall_clock_seconds\": 1762}\n  conclusion=success\n\nlabel_only_seed456\n  status=DONE\n  metrics={\"accuracy\": 0.859, \"n\": 1190, \"pass_recall\": 0.938, \"fail_recall\": 0.661, \"pass_f1\": 0.905, \"fail_f1\": 0.727}\n  conclusion=success\n\nlabel_only_seed123\n  status=DONE\n  metrics={\"accuracy\": 0.8706, \"n\": 1190, \"pass_recall\": 0.974, \"fail_recall\": 0.611, \"pass_f1\": 0.915, \"fail_f1\": 0.729}\n  conclusion=success\n\nexception_only_nomarker_seed456\n  status=QUEUED\n\nexception_only_nomarker_seed123\n  status=QUEUED\n\nexception_only_nomarker_seed42\n  status=QUEUED\n\nae_only_seed456\n  status=DONE\n  metrics={\"accuracy\": 0.9992, \"n\": 1190, \"majority_baseline\": 0.7151, \"lift\": 0.2841, \"seed_comparison\": {\"seed42_accuracy\": 0.9992, \"seed123_accuracy\": 0.9908, \"seed456_accuracy\": 0.9992, \"mean_accuracy\": 0.9964, \"std\": 0.0049, \"note\": \"2/3 seeds = 99.92%, seed123 = 99.08%. Mean = 99.64% \\u00b1 0.49\"}}\n  conclusion=success\n\nae_only_seed123\n  status=DONE\n  metrics={\"accuracy\": 0.9908, \"n\": 1190, \"pass_recall\": 0.987, \"fail_recall\": 1, \"majority_baseline\": 0.7151, \"lift\": 0.2757}\n  conclusion=success\n\nregex_baseline_analysis\n  status=DONE\n  metrics={\"regex_B1_ERROR_presence\": 0.9345, \"regex_B2_Traceback\": 0.7151, \"regex_B3_any_keyword\": 0.9345, \"regex_B4_exception_type\": 0.9361, \"regex_B5_format_marker\": 0.9933, \"regex_B6_error_count_ge2\": 0.9202, \"sft_exception_only\": 0.9983, \"best_regex_gap_vs_sft\": -0.0622, \"B5_mcnemar_p\": 0.041, \"n\": 1190}\n  conclusion=success\n\nfull_trace_2048tok_seed42\n  status=DONE\n  conclusion=killed\n\ndeepseek_vota_seed42\n  status=DONE\n  metrics={\"accuracy\": 0.8445, \"majority_baseline\": 0.7151, \"lift\": 0.1294, \"accuracy_ci\": [0.826, 0.864], \"pass_precision\": 0.821, \"pass_recall\": 1, \"pass_f1\": 0.902, \"fail_precision\": 1, \"fail_recall\": 0.454, \"fail_f1\": 0.625, \"eval_loss_epoch1\": 0.0679, \"eval_loss_epoch2\": 0.095, \"eval_loss_epoch3\": 0.1121, \"final_train_loss\": 0.0522, \"epoch1_checkpoint_eval\": {\"accuracy\": 0.7815, \"accuracy_ci\": [0.76, 0.803], \"fail_recall\": 0.233, \"fail_precision\": 1, \"pass_recall\": 1, \"pass_precision\": 0.766, \"fail_f1\": 0.378, \"pass_f1\": 0.867, \"conclusion\": \"epoch3_final_is_better\"}, \"reeval_with_fixed_script\": {\"accuracy\": 0.16, \"accuracy_ci\": [0.139, 0.18], \"fail_f1\": 0.61, \"fail_precision\": 0.9, \"fail_recall\": 0.47, \"pass_f1\": 0.07, \"pass_precision\": 1, \"pass_recall\": 0.04, \"note\": \"CATASTROPHIC: re-eval with corrected evaluate.py shows 16% (vs original 84.45%). Model predicts fail for almost everything. Previous 84.45% may have been from buggy eval. NEEDS INVESTIGATION.\"}, \"group_analysis\": {\"train_truncated\": {\"n\": 1091, \"accuracy\": 0.8304, \"ci_95\": [0.8075, 0.8524], \"correct\": 906, \"incorrect\": 185, \"pass_accuracy\": 1, \"pass_n\": 822, \"fail_accuracy\": 0.3123, \"fail_n\": 269}, \"train_intact\": {\"n\": 99, \"accuracy\": 1, \"ci_95\": [1, 1], \"correct\": 99, \"incorrect\": 0, \"pass_accuracy\": 1, \"pass_n\": 29, \"fail_accuracy\": 1, \"fail_n\": 70}, \"fisher_exact\": {\"odds_ratio\": 0, \"p_value\": 0}, \"overall_accuracy\": 0.8445, \"max_length\": 2048, \"note\": \"Grouped by whether training sample content exceeded token budget (DeepSeek tokenizer, max_length=2048). Inference used full-length input (no truncation). All 185 errors from truncated group's fail class (fail_recall=31.2%). Intact group: 100% accuracy.\"}}\n  conclusion=success\n\ndeepseek_full_trace_seed42_v3\n  status=DONE\n  metrics={\"accuracy\": 0.7916, \"majority_baseline\": 0.7151, \"lift\": 0.0765, \"n\": 1190, \"pass_precision\": 0.857, \"pass_recall\": 0.851, \"pass_f1\": 0.854, \"fail_precision\": 0.632, \"fail_recall\": 0.643, \"fail_f1\": 0.637, \"accuracy_ci\": [0.768, 0.813], \"train_loss\": 0.0547, \"train_runtime_seconds\": 8891, \"epochs\": 3, \"reeval_discrepancy\": {\"reeval_accuracy\": 0.285, \"reeval_note\": \"RESOLVED: 28.5% was caused by eval max_length=16384 (OOD). Re-eval with max_length=2048 reproduces 79.16%. predictions.jsonl updated to maxlen2048 results.\", \"status\": \"RESOLVED\"}}\n  conclusion=success\n\neval_missing_predictions_batch_v2\n  status=DONE\n  conclusion=success\n\ndebugbench_vota_seed42\n  status=DONE\n  metrics={\"accuracy\": 0.9977, \"majority_baseline\": 0.5141, \"lift\": 0.4836, \"n\": 426, \"pass_precision\": 1, \"pass_recall\": 1, \"pass_f1\": 1, \"fail_precision\": 1, \"fail_recall\": 1, \"fail_f1\": 1, \"accuracy_ci\": [0.993, 1], \"train_loss\": 0.098, \"eval_loss\": 0.1179, \"eval_mean_token_accuracy\": 0.9737, \"errors\": 1}\n  conclusion=success\n\neval_missing_predictions_batch\n  status=DONE\n  conclusion=success\n\nfull_trace_1024tok_seed42\n  status=DONE\n  metrics={\"accuracy\": 0.7723, \"majority_baseline\": 0.7151, \"lift\": 0.0571, \"n\": 1190, \"accuracy_ci\": [0.7487, 0.7958], \"pass_precision\": 0.9006, \"pass_recall\": 0.7662, \"pass_f1\": 0.8279, \"fail_precision\": 0.573, \"fail_recall\": 0.7876, \"fail_f1\": 0.6634, \"train_loss\": 0.0634, \"train_runtime_sec\": 5553, \"epochs\": 3}\n  conclusion=negative\n\ndebugbench_exception_only_seed42\n  status=DONE\n  metrics={\"accuracy\": 1, \"majority_baseline\": 0.5141, \"lift\": 0.4859, \"n\": 426, \"pass_precision\": 1, \"pass_recall\": 1, \"pass_f1\": 1, \"fail_precision\": 1, \"fail_recall\": 1, \"fail_f1\": 1, \"accuracy_ci_wilson\": [0.9914, 1], \"accuracy_ci_bootstrap\": [1, 1], \"train_loss\": 0.2435, \"eval_loss\": 0.4157, \"train_runtime_sec\": 837}\n  conclusion=success\n\ndeepseek_exception_only_seed456\n  status=DONE\n  metrics={\"accuracy\": 0.9933, \"majority_baseline\": 0.7151, \"lift\": 0.2782, \"n\": 1190, \"pass_precision\": 1, \"pass_recall\": 0.9906, \"pass_f1\": 0.9953, \"fail_precision\": 0.9769, \"fail_recall\": 1, \"fail_f1\": 0.9883, \"accuracy_ci\": [0.9882, 0.9975], \"train_loss\": 0.1225, \"eval_loss\": 0.4824, \"train_runtime_sec\": 6246, \"seed_comparison\": {\"seed42_accuracy\": 0.9933, \"seed456_accuracy\": 0.9933, \"seed123_accuracy\": 0.9109, \"note\": \"seed42 and seed456 identical (99.33%); seed123 outlier (91.09%). 2/3 seeds robust.\"}, \"epoch1_checkpoint_eval\": {\"accuracy\": 0.993, \"accuracy_ci\": [0.988, 0.997], \"fail_f1\": 0.99, \"fail_precision\": 0.98, \"fail_recall\": 1, \"pass_f1\": 1, \"pass_precision\": 1, \"pass_recall\": 0.99, \"conclusion\": \"epoch1 (99.3%) \\u2248 epoch3 (99.33%), 1 epoch convergence confirmed\"}}\n  conclusion=success\n\ndeepseek_exception_only_seed123\n  status=DONE\n  metrics={\"accuracy\": 0.9109, \"pass_precision\": 1, \"pass_recall\": 0.993, \"pass_f1\": 0.996, \"fail_precision\": 0.976, \"fail_recall\": 0.705, \"fail_f1\": 0.818, \"ci_95\": [0.894, 0.926], \"train_loss\": 0.122, \"train_runtime_sec\": 6384}\n  conclusion=negative\n\ndeepseek_exception_only_seed42\n  status=DONE\n  metrics={\"accuracy\": 0.9933, \"majority_baseline\": 0.7151, \"lift\": 0.2782, \"n\": 1190, \"pass_precision\": 1, \"pass_recall\": 0.9906, \"pass_f1\": 0.9953, \"fail_precision\": 0.9769, \"fail_recall\": 1, \"fail_f1\": 0.9883, \"epoch1_checkpoint_eval\": {\"accuracy\": 0.9983, \"fail_recall\": 1, \"fail_precision\": 0.9941, \"pass_recall\": 0.9976, \"conclusion\": \"epoch1_better_by_0.50pp\"}}\n  conclusion=success\n\ndeepseek_no_trace_seed42\n  status=DONE\n  metrics={\"accuracy\": 0.7336, \"majority_baseline\": 0.7151, \"lift\": 0.0185, \"n\": 1190, \"pass_precision\": 0.817, \"pass_recall\": 0.808, \"pass_f1\": 0.813, \"fail_precision\": 0.532, \"fail_recall\": 0.546, \"fail_f1\": 0.539, \"accuracy_ci\": [0.708, 0.757], \"lift_ci\": [-0.009, 0.046]}\n  conclusion=negative\n\ndebugbench_no_trace_seed42\n  status=DONE\n  metrics={\"accuracy\": 0.9671, \"majority_baseline\": 0.5141, \"lift\": 0.4531, \"pass_precision\": 1, \"pass_recall\": 0.936, \"pass_f1\": 0.967, \"fail_precision\": 0.937, \"fail_recall\": 1, \"fail_f1\": 0.967, \"accuracy_ci\": [0.948, 0.984], \"train_loss\": 0.249, \"eval_loss\": 0.532}\n  conclusion=success\n\nfull_trace_512tok_seed42\n  status=DONE\n  metrics={\"accuracy\": 0.8042, \"majority_baseline\": 0.7151, \"lift\": 0.0891, \"pass_precision\": 0.8705, \"pass_recall\": 0.8531, \"pass_f1\": 0.8617, \"fail_precision\": 0.6489, \"fail_recall\": 0.6814, \"fail_f1\": 0.6647, \"n\": 1190, \"accuracy_ci\": [0.7815, 0.8261]}\n  conclusion=negative\n\nfull_trace_256tok_seed42\n  status=DONE\n  metrics={\"accuracy\": 0.7882, \"majority_baseline\": 0.7151, \"lift\": 0.0731, \"n\": 1190, \"pass_precision\": 0.903, \"pass_recall\": 0.788, \"pass_f1\": 0.842, \"fail_precision\": 0.597, \"fail_recall\": 0.788, \"fail_f1\": 0.679, \"accuracy_ci\": [0.764, 0.81], \"train_loss\": 0.1094, \"train_runtime_sec\": 3047, \"epochs\": 3}\n  conclusion=negative\n\ndebugbench_exception_bug_fix\n  status=DONE\n  conclusion=success\n\nvota_seed456_v2\n  status=DONE\n  metrics={\"accuracy\": 0.9908, \"pass_precision\": 1, \"pass_recall\": 0.987, \"pass_f1\": 0.993, \"fail_precision\": 0.969, \"fail_recall\": 1, \"fail_f1\": 0.984, \"ci_95\": [0.985, 0.996]}\n  conclusion=success\n\nno_trace_seed42\n  status=DONE\n  conclusion=killed\n\nno_trace_seed42_v2\n  status=DONE\n  conclusion=killed\n\nvota_seed42\n  status=DONE\n  conclusion=killed\n\nvota_seed42_v2\n  status=DONE\n  conclusion=killed\n\nvota_seed456\n  status=DONE\n  conclusion=failed\n\ndeepseek_full_trace_seed42_v2\n  status=DONE\n  conclusion=killed\n\ndeepseek_full_trace_seed42\n  status=DONE\n  metrics={\"accuracy_no_truncation\": 0.2849, \"accuracy_with_truncation_fix\": 0.1059, \"accuracy_with_truncation_fix_ci\": [0.089, 0.123], \"majority_baseline\": 0.7151, \"n\": 1190, \"note\": \"Both evals show model failure. No-truncation: all predict fail. With-truncation: garbage tokens. LoRA training itself failed due to label truncation during training.\"}\n  conclusion=negative\n\nexception_only_seed123\n  status=DONE\n  metrics={\"accuracy\": 0.9983, \"accuracy_ci\": [0.9958, 1], \"majority_baseline\": 0.7151, \"lift\": 0.2832, \"n\": 1190, \"pass_precision\": 1, \"pass_recall\": 0.9976, \"pass_f1\": 0.9988, \"fail_precision\": 0.9941, \"fail_recall\": 1, \"fail_f1\": 0.9971, \"train_loss\": 0.1096, \"train_runtime_sec\": 7507, \"epochs\": 3, \"seed_comparison\": {\"seed42_accuracy\": 0.9983, \"seed456_accuracy\": 0.9983, \"seed123_accuracy\": 0.9983, \"max_diff\": 0, \"note\": \"identical accuracy to 4 decimal places across all 3 seeds (42/456/123); each has exactly 2/1190 errors; exception_only fully seed-robust\"}}\n  conclusion=success\n\nexception_only_seed456\n  status=DONE\n  metrics={\"accuracy\": 0.9983, \"accuracy_ci\": [0.9958, 1], \"majority_baseline\": 0.7151, \"lift\": 0.2832, \"n\": 1190, \"pass_precision\": 1, \"pass_recall\": 0.9976, \"pass_f1\": 0.9988, \"fail_precision\": 0.9941, \"fail_recall\": 1, \"fail_f1\": 0.9971, \"vs_seed42\": {\"seed42_accuracy\": 0.9983, \"seed456_accuracy\": 0.9983, \"diff\": 0, \"note\": \"identical accuracy to 4 decimal places; no predictions.jsonl for paired bootstrap\"}, \"train_loss\": 0.1087, \"eval_loss\": 0.4629, \"train_runtime_sec\": 4541, \"epochs\": 3}\n  conclusion=success\n\nvota_exception_only_seed42_v2\n  status=DONE\n  metrics={\"accuracy\": 0.9983, \"majority_baseline\": 0.7151, \"lift\": 0.2832, \"n\": 1190, \"pass_precision\": 1, \"pass_recall\": 0.998, \"pass_f1\": 0.999, \"fail_precision\": 0.994, \"fail_recall\": 1, \"fail_f1\": 0.997, \"lift_vs_notrace\": 0.2471, \"lift_vs_notrace_ci_lower\": 0.2227, \"lift_vs_notrace_ci_upper\": 0.2714, \"lift_vs_fulltrace\": 0.1807, \"lift_vs_fulltrace_ci_lower\": 0.1588, \"lift_vs_fulltrace_ci_upper\": 0.2034, \"lift_vs_vota\": 0.0067, \"lift_vs_vota_ci_lower\": 0.0017, \"lift_vs_vota_ci_upper\": 0.0126, \"lift_vs_vota_pvalue\": 0.01}\n  conclusion=success\n\nvota_seed123\n  status=DONE\n  conclusion=failed\n\nfull_trace_label_only_seed42\n  status=DONE\n  metrics={\"accuracy\": 0.8622, \"accuracy_ci_lower\": 0.8437, \"accuracy_ci_upper\": 0.8807, \"majority_baseline\": 0.7151, \"lift\": 0.1471, \"n\": 1190, \"pass_precision\": 0.8821, \"pass_recall\": 0.9318, \"pass_f1\": 0.9063, \"fail_precision\": 0.8007, \"fail_recall\": 0.6873, \"fail_f1\": 0.7397, \"train_loss\": 0.2505, \"eval_loss\": 0.3205, \"lift_vs_notrace\": 0.1109, \"lift_vs_notrace_ci_lower\": 0.0849, \"lift_vs_notrace_ci_upper\": 0.137, \"lift_vs_standard_fulltrace\": 0.0445, \"lift_vs_standard_fulltrace_ci_lower\": 0.0235, \"lift_vs_standard_fulltrace_ci_upper\": 0.0655, \"lift_vs_standard_fulltrace_pvalue\": 0}\n  conclusion=success\n\nvota_no_ae_seed42\n  status=DONE\n  metrics={\"accuracy\": 0.994, \"majority_baseline\": 0.7151, \"lift\": 0.279, \"n\": 1190, \"pass_f1\": 0.996, \"fail_f1\": 0.989, \"accuracy_ci_lower\": 0.989, \"accuracy_ci_upper\": 0.998, \"lift_vs_notrace\": 0.243, \"lift_vs_notrace_ci_lower\": 0.218, \"lift_vs_notrace_ci_upper\": 0.268, \"train_loss\": 0.0908, \"eval_loss\": 0.2215, \"wall_clock_seconds\": 6397.88}\n  conclusion=success\n\nvota_loop_only_seed42\n  status=DONE\n  metrics={\"accuracy\": 0.8563, \"majority_baseline\": 0.7151, \"lift\": 0.1412, \"n\": 1190, \"pass_precision\": 0.9239, \"pass_recall\": 0.8707, \"pass_f1\": 0.8966, \"fail_precision\": 0.7165, \"fail_recall\": 0.8201, \"fail_f1\": 0.7648, \"accuracy_ci\": [0.8353, 0.8756], \"bootstrap_vs_no_trace\": {\"diff\": 0.105, \"ci\": [0.0824, 0.1286], \"significant\": true}, \"bootstrap_vs_vota\": {\"diff\": -0.1378, \"ci\": [-0.1571, -0.1185], \"significant\": true}, \"bootstrap_vs_full_trace\": {\"diff\": 0.0387, \"ci\": [0.0185, 0.0597], \"significant\": true}, \"train_loss\": 0.0718, \"wall_clock_seconds\": 7425.65}\n  conclusion=success\n\nvota_ae_only_seed42\n  status=DONE\n  metrics={\"accuracy\": 0.9992, \"accuracy_ci\": [0.9975, 1], \"bootstrap_pairwise\": {\"ae_only_vs_no_trace\": {\"diff\": 0.2479, \"ci\": [0.2235, 0.2731], \"p_value\": 0, \"significant\": true}, \"ae_only_vs_exception_only\": {\"diff\": 0.0008, \"ci\": [-0.0017, 0.0034], \"p_value\": 0.8002, \"significant\": false}, \"ae_only_vs_vota\": {\"diff\": 0.005, \"ci\": [0.0017, 0.0092], \"p_value\": 0.0046, \"significant\": true}}, \"config\": {\"n_bootstrap\": 10000, \"seed\": 42, \"method\": \"paired_bootstrap\"}}\n  conclusion=success\n\nfull_trace_seed42_v5\n  status=DONE\n  metrics={\"accuracy\": 0.8176, \"majority_baseline\": 0.7151, \"lift\": 0.1025, \"n\": 1190, \"pass_precision\": 0.8774, \"pass_recall\": 0.866, \"pass_f1\": 0.8717, \"fail_precision\": 0.6743, \"fail_recall\": 0.6962, \"fail_f1\": 0.6851, \"accuracy_ci_lower\": 0.797, \"accuracy_ci_upper\": 0.839, \"lift_vs_notrace\": 0.0664, \"lift_vs_notrace_ci_lower\": 0.0437, \"lift_vs_notrace_ci_upper\": 0.0899, \"train_loss\": 0.05, \"eval_loss\": 0.0867, \"wall_clock_seconds\": 7852, \"epoch_level\": {\"epoch1_accuracy\": 0.8303, \"epoch2_accuracy\": 0.763, \"final_accuracy\": 0.8176, \"trend\": \"non_monotonic_epoch1_best_epoch2_collapse\"}}\n  conclusion=success\n\nno_trace_seed42_v5\n  status=DONE\n  metrics={\"accuracy\": 0.7513, \"accuracy_ci_lower\": 0.7277, \"accuracy_ci_upper\": 0.7748, \"majority_baseline\": 0.7151, \"lift\": 0.0361, \"lift_ci_lower\": 0.0042, \"lift_ci_upper\": 0.0706, \"n\": 1190, \"pass_precision\": 0.8776, \"pass_recall\": 0.7579, \"pass_f1\": 0.8134, \"fail_precision\": 0.5473, \"fail_recall\": 0.7345, \"fail_f1\": 0.6272, \"epoch_level\": {\"epoch1_accuracy\": 0.7429, \"epoch2_accuracy\": 0.763, \"final_accuracy\": 0.7513, \"trend\": \"non_monotonic_epoch2_best\"}}\n  conclusion=success\n\nvota_seed42_v5\n  status=DONE\n  metrics={\"accuracy\": 0.9941, \"majority_baseline\": 0.7151, \"lift\": 0.279, \"n\": 1190, \"pass_precision\": 1, \"pass_recall\": 0.9882, \"pass_f1\": 0.9941, \"fail_precision\": 0.9714, \"fail_recall\": 1, \"fail_f1\": 0.9855, \"lift_vs_notrace\": 0.2428, \"lift_vs_notrace_ci_lower\": 0.2185, \"lift_vs_notrace_ci_upper\": 0.2681, \"accuracy_ci_lower\": 0.9882, \"accuracy_ci_upper\": 0.9983, \"train_loss\": 0.05, \"eval_loss\": 0.0867, \"eval_mean_token_accuracy\": 0.9828, \"wall_clock_seconds\": 8443, \"epoch_level\": {\"epoch1_accuracy\": 0.9933, \"epoch2_accuracy\": 0.9941, \"final_accuracy\": 0.9941, \"trend\": \"monotonic_increasing_then_stable\"}}\n  conclusion=success\n\ncalibration_analysis_seed42\n  status=DONE\n  metrics={\"no_trace\": {\"ece\": 0.171476, \"mce\": 0.475643, \"brier_score\": 0.197152, \"accuracy\": 0.751261, \"n_samples\": 1190}, \"full_trace\": {\"ece\": 0.095817, \"mce\": 0.249061, \"brier_score\": 0.143924, \"accuracy\": 0.817647, \"n_samples\": 1190}, \"label_only\": {\"ece\": 0.110686, \"mce\": 0.417124, \"brier_score\": 0.120144, \"accuracy\": 0.862185, \"n_samples\": 1190}, \"loop_only\": {\"ece\": 0.083085, \"mce\": 0.183406, \"brier_score\": 0.118335, \"accuracy\": 0.856303, \"n_samples\": 1190}, \"ae_only\": {\"ece\": 0.000415, \"mce\": 0.000415, \"brier_score\": 0.000847, \"accuracy\": 0.99916, \"n_samples\": 1190}, \"exception_only\": {\"ece\": 0.002717, \"mce\": 0.835484, \"brier_score\": 0.001311, \"accuracy\": 0.998319, \"n_samples\": 1190}, \"vota\": {\"ece\": 0.00541, \"mce\": 0.622459, \"brier_score\": 0.005234, \"accuracy\": 0.994118, \"n_samples\": 1190}}\n  conclusion=success\n\nvota_exception_only_seed42\n  status=DONE\n  conclusion=failed\n\nvota_seed42_v4\n  status=DONE\n  metrics={\"accuracy\": 0.9563, \"majority_baseline\": 0.7151, \"lift\": 0.2412, \"n\": 1190, \"pass_precision\": 0.944, \"pass_recall\": 0.998, \"pass_f1\": 0.97, \"fail_precision\": 0.993, \"fail_recall\": 0.853, \"fail_f1\": 0.917, \"lift_vs_notrace\": 0.205, \"lift_vs_notrace_ci_lower\": 0.177, \"lift_vs_notrace_ci_upper\": 0.234, \"train_loss\": 0.046, \"eval_loss\": 0.0842}\n  conclusion=success\n\nfull_trace_seed42_v2\n  status=DONE\n  metrics={\"accuracy\": 0.284, \"majority_baseline\": 0.7151, \"lift\": -0.4311, \"n\": 1190, \"pass_precision\": 0.923, \"pass_recall\": 0.085, \"pass_f1\": 0.155, \"fail_precision\": 0.445, \"fail_recall\": 0.785, \"fail_f1\": 0.568, \"train_loss\": 0.0373, \"eval_loss\": 0.082, \"eval_mean_token_accuracy\": 0.984}\n  conclusion=negative\n\nno_trace_seed42_v4\n  status=DONE\n  metrics={\"accuracy\": 0.7513, \"majority_baseline\": 0.7151, \"lift\": 0.0361, \"pass_precision\": 0.8776, \"pass_recall\": 0.7579, \"pass_f1\": 0.8134, \"fail_precision\": 0.5473, \"fail_recall\": 0.7345, \"fail_f1\": 0.6272, \"train_loss\": 0.18, \"eval_loss\": 0.6454, \"eval_mean_token_accuracy\": 0.8897}\n  conclusion=success\n\nfull_trace_seed42\n  status=DONE\n  metrics={\"train_loss\": 0.037, \"eval_loss\": 0.084, \"eval_mean_token_accuracy\": 0.984, \"accuracy\": 0.284, \"majority_baseline\": 0.7151, \"lift\": -0.431, \"pass_precision\": 0.88, \"pass_recall\": 0.08, \"pass_f1\": 0.16, \"fail_precision\": 0.31, \"fail_recall\": 0.97, \"fail_f1\": 0.57}\n  conclusion=killed\n\nno_trace_seed42_v3\n  status=DONE\n  metrics={\"train_loss\": 0.18, \"eval_loss\": 0.645, \"eval_mean_token_accuracy\": 0.89, \"accuracy\": 0.7513, \"majority_baseline\": 0.7151, \"lift\": 0.0361, \"pass_precision\": 0.8776, \"pass_recall\": 0.7579, \"pass_f1\": 0.8134, \"fail_precision\": 0.5473, \"fail_recall\": 0.7345, \"fail_f1\": 0.6272}\n  conclusion=killed\n\nvota_seed42_v3\n  status=DONE\n  metrics={\"train_loss\": 0.046, \"eval_loss\": 0.085, \"eval_mean_token_accuracy\": 0.983, \"accuracy\": 0.992, \"majority_baseline\": 0.7151, \"lift\": 0.276, \"pass_precision\": 0.99, \"pass_recall\": 0.99, \"pass_f1\": 0.99, \"fail_precision\": 0.99, \"fail_recall\": 0.99, \"fail_f1\": 0.99}\n  conclusion=killed",
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

_source line 22_

<details open><summary>🔧 Tool call — Bash · `toolu_01MpWvNCSGbsuL2VNz3KyvEw`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/6cf6c7bc-54c9-45a8-b5e6-b498a2a84d18/tool-results/mcp-agent-ml-research-read_registry-1778941588866.txt | python3 -c \"\nimport json, sys\n\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\n# Continue listing remaining experiments\nseen = set()\nfor eid, exp in experiments.items():\n    status = exp.get('status','?')\n    metrics = exp.get('metrics', {})\n    conclusion = exp.get('conclusion','')\n    \n    if eid.startswith(('exception_only_seed42', 'vota_seed123_v', 'ae_only_seed42', 'loop_only_seed42', 'label_only_seed42', 'full_trace_seed42_v3', 'full_trace_seed42_v4', 'deepseek_no_trace_seed')):\n        print(f'{eid}')\n        print(f'  status={status}')\n        if metrics:\n            print(f'  metrics={json.dumps(metrics)}')\n        if conclusion:\n            print(f'  conclusion={conclusion[:200]}')\n        print()\n\" 2>&1\n",
  "description": "Find remaining experiments not yet seen",
  "timeout": 15000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6cf6c7bc-54c9-45a8-b5e6-b498a2a84d18",
  "uuid": "4cef2716-19da-4bf8-91ff-aafbf6f52651",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rv1mPNdXG5tpuYv5Ba3G5K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9334,
      "cache_read_input_tokens": 26884,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9334
      },
      "output_tokens": 37,
      "service_tier": "standard",
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

_source line 23 · 2026-05-16T14:27:08.301Z_

<details><summary>↩ Tool result · `toolu_01MpWvNCSGbsuL2VNz3KyvEw`</summary>

```text
deepseek_no_trace_seed42
  status=DONE
  metrics={"accuracy": 0.7336, "majority_baseline": 0.7151, "lift": 0.0185, "n": 1190, "pass_precision": 0.817, "pass_recall": 0.808, "pass_f1": 0.813, "fail_precision": 0.532, "fail_recall": 0.546, "fail_f1": 0.539, "accuracy_ci": [0.708, 0.757], "lift_ci": [-0.009, 0.046]}
  conclusion=negative
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6cf6c7bc-54c9-45a8-b5e6-b498a2a84d18",
  "uuid": "e07324ad-2bb7-4cc2-95df-dbee2dd6a4f7",
  "tool_use_result": {
    "stdout": "deepseek_no_trace_seed42\n  status=DONE\n  metrics={\"accuracy\": 0.7336, \"majority_baseline\": 0.7151, \"lift\": 0.0185, \"n\": 1190, \"pass_precision\": 0.817, \"pass_recall\": 0.808, \"pass_f1\": 0.813, \"fail_precision\": 0.532, \"fail_recall\": 0.546, \"fail_f1\": 0.539, \"accuracy_ci\": [0.708, 0.757], \"lift_ci\": [-0.009, 0.046]}\n  conclusion=negative",
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

_source line 24_

<details open><summary>🔧 Tool call — Bash · `toolu_012YC7hNoXvvFqzSqxEp4cBg`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/6cf6c7bc-54c9-45a8-b5e6-b498a2a84d18/tool-results/mcp-agent-ml-research-read_registry-1778941588866.txt | python3 -c \"\nimport json, sys\n\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\n# Get all exp IDs and check for ones with exception_only_seed42, ae_only_seed42, loop_only_seed42, label_only_seed42\nfor eid in sorted(experiments.keys()):\n    exp = experiments[eid]\n    status = exp.get('status','?')\n    conclusion = exp.get('conclusion','')\n    metrics = exp.get('metrics', {})\n    acc = metrics.get('accuracy', 'N/A')\n    print(f'{eid}: status={status}, conclusion={conclusion}, acc={acc}')\n\" 2>&1\n",
  "description": "List all experiment IDs with status and accuracy",
  "timeout": 15000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6cf6c7bc-54c9-45a8-b5e6-b498a2a84d18",
  "uuid": "5fb4dd66-9d9b-42d2-8c68-e8a1c9c89c2f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FgQJNv2Sq4ecaXLkKjVKaH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 719,
      "cache_read_input_tokens": 36218,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 719
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

_source line 25 · 2026-05-16T14:27:13.608Z_

<details><summary>↩ Tool result · `toolu_012YC7hNoXvvFqzSqxEp4cBg`</summary>

```text
ae_only_seed123: status=DONE, conclusion=success, acc=0.9908
ae_only_seed456: status=DONE, conclusion=success, acc=0.9992
calibration_analysis_seed42: status=DONE, conclusion=success, acc=N/A
codellama13b_exception_only_seed42: status=RUNNING, conclusion=, acc=N/A
codellama13b_no_trace_seed42: status=DONE, conclusion=success, acc=0.765
codellama13b_vota_seed42: status=RUNNING, conclusion=, acc=N/A
codellama_exception_only_seed42: status=QUEUED, conclusion=killed, acc=N/A
codellama_no_trace_seed42: status=QUEUED, conclusion=killed, acc=N/A
codellama_vota_seed42: status=QUEUED, conclusion=killed, acc=N/A
debugbench_exception_bug_fix: status=DONE, conclusion=success, acc=N/A
debugbench_exception_only_seed42: status=DONE, conclusion=success, acc=1
debugbench_no_trace_seed42: status=DONE, conclusion=success, acc=0.9671
debugbench_vota_seed42: status=DONE, conclusion=success, acc=0.9977
deepseek_exception_only_seed123: status=DONE, conclusion=negative, acc=0.9109
deepseek_exception_only_seed42: status=DONE, conclusion=success, acc=0.9933
deepseek_exception_only_seed456: status=DONE, conclusion=success, acc=0.9933
deepseek_full_trace_seed42: status=DONE, conclusion=negative, acc=N/A
deepseek_full_trace_seed42_v2: status=DONE, conclusion=killed, acc=N/A
deepseek_full_trace_seed42_v3: status=DONE, conclusion=success, acc=0.7916
deepseek_no_trace_seed42: status=DONE, conclusion=negative, acc=0.7336
deepseek_vota_seed42: status=DONE, conclusion=success, acc=0.8445
eval_missing_predictions_batch: status=DONE, conclusion=success, acc=N/A
eval_missing_predictions_batch_v2: status=DONE, conclusion=success, acc=N/A
exception_only_nomarker_seed123: status=QUEUED, conclusion=, acc=N/A
exception_only_nomarker_seed42: status=QUEUED, conclusion=, acc=N/A
exception_only_nomarker_seed456: status=QUEUED, conclusion=, acc=N/A
exception_only_seed123: status=DONE, conclusion=success, acc=0.9983
exception_only_seed456: status=DONE, conclusion=success, acc=0.9983
full_trace_1024tok_seed42: status=DONE, conclusion=negative, acc=0.7723
full_trace_2048tok_seed42: status=DONE, conclusion=killed, acc=N/A
full_trace_256tok_seed42: status=DONE, conclusion=negative, acc=0.7882
full_trace_512tok_seed42: status=DONE, conclusion=negative, acc=0.8042
full_trace_label_only_seed42: status=DONE, conclusion=success, acc=0.8622
full_trace_seed42: status=DONE, conclusion=killed, acc=0.284
full_trace_seed42_v2: status=DONE, conclusion=negative, acc=0.284
full_trace_seed42_v5: status=DONE, conclusion=success, acc=0.8176
label_only_seed123: status=DONE, conclusion=success, acc=0.8706
label_only_seed456: status=DONE, conclusion=success, acc=0.859
loop_only_seed123: status=DONE, conclusion=success, acc=0.8588
loop_only_seed456: status=DONE, conclusion=success, acc=0.8664
no_trace_seed42: status=DONE, conclusion=killed, acc=N/A
no_trace_seed42_v2: status=DONE, conclusion=killed, acc=N/A
no_trace_seed42_v3: status=DONE, conclusion=killed, acc=0.7513
no_trace_seed42_v4: status=DONE, conclusion=success, acc=0.7513
no_trace_seed42_v5: status=DONE, conclusion=success, acc=0.7513
qwen1.5b_exception_only_seed42: status=QUEUED, conclusion=killed, acc=N/A
qwen1.5b_full_trace_seed42: status=QUEUED, conclusion=killed, acc=N/A
qwen1.5b_no_trace_seed42: status=QUEUED, conclusion=killed, acc=N/A
qwen1.5b_vota_seed42: status=QUEUED, conclusion=killed, acc=N/A
qwen15b_exception_only_seed42: status=DONE, conclusion=success, acc=0.9983
qwen15b_full_trace_seed42: status=DONE, conclusion=success, acc=0.7706
qwen15b_no_trace_seed42: status=DONE, conclusion=success, acc=0.6731
qwen15b_vota_seed42: status=DONE, conclusion=success, acc=0.9958
regex_baseline_analysis: status=DONE, conclusion=success, acc=N/A
vota_ae_only_seed42: status=DONE, conclusion=success, acc=0.9992
vota_exception_only_seed42: status=DONE, conclusion=failed, acc=N/A
vota_exception_only_seed42_v2: status=DONE, conclusion=success, acc=0.9983
vota_loop_only_seed42: status=DONE, conclusion=success, acc=0.8563
vota_no_ae_seed42: status=DONE, conclusion=success, acc=0.994
vota_seed123: status=DONE, conclusion=failed, acc=N/A
vota_seed42: status=DONE, conclusion=killed, acc=N/A
vota_seed42_v2: status=DONE, conclusion=killed, acc=N/A
vota_seed42_v3: status=DONE, conclusion=killed, acc=0.992
vota_seed42_v4: status=DONE, conclusion=success, acc=0.9563
vota_seed42_v5: status=DONE, conclusion=success, acc=0.9941
vota_seed456: status=DONE, conclusion=failed, acc=N/A
vota_seed456_v2: status=DONE, conclusion=success, acc=0.9908
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6cf6c7bc-54c9-45a8-b5e6-b498a2a84d18",
  "uuid": "e9d2acb1-f43e-4808-b5bf-d0f34a9144b0",
  "tool_use_result": {
    "stdout": "ae_only_seed123: status=DONE, conclusion=success, acc=0.9908\nae_only_seed456: status=DONE, conclusion=success, acc=0.9992\ncalibration_analysis_seed42: status=DONE, conclusion=success, acc=N/A\ncodellama13b_exception_only_seed42: status=RUNNING, conclusion=, acc=N/A\ncodellama13b_no_trace_seed42: status=DONE, conclusion=success, acc=0.765\ncodellama13b_vota_seed42: status=RUNNING, conclusion=, acc=N/A\ncodellama_exception_only_seed42: status=QUEUED, conclusion=killed, acc=N/A\ncodellama_no_trace_seed42: status=QUEUED, conclusion=killed, acc=N/A\ncodellama_vota_seed42: status=QUEUED, conclusion=killed, acc=N/A\ndebugbench_exception_bug_fix: status=DONE, conclusion=success, acc=N/A\ndebugbench_exception_only_seed42: status=DONE, conclusion=success, acc=1\ndebugbench_no_trace_seed42: status=DONE, conclusion=success, acc=0.9671\ndebugbench_vota_seed42: status=DONE, conclusion=success, acc=0.9977\ndeepseek_exception_only_seed123: status=DONE, conclusion=negative, acc=0.9109\ndeepseek_exception_only_seed42: status=DONE, conclusion=success, acc=0.9933\ndeepseek_exception_only_seed456: status=DONE, conclusion=success, acc=0.9933\ndeepseek_full_trace_seed42: status=DONE, conclusion=negative, acc=N/A\ndeepseek_full_trace_seed42_v2: status=DONE, conclusion=killed, acc=N/A\ndeepseek_full_trace_seed42_v3: status=DONE, conclusion=success, acc=0.7916\ndeepseek_no_trace_seed42: status=DONE, conclusion=negative, acc=0.7336\ndeepseek_vota_seed42: status=DONE, conclusion=success, acc=0.8445\neval_missing_predictions_batch: status=DONE, conclusion=success, acc=N/A\neval_missing_predictions_batch_v2: status=DONE, conclusion=success, acc=N/A\nexception_only_nomarker_seed123: status=QUEUED, conclusion=, acc=N/A\nexception_only_nomarker_seed42: status=QUEUED, conclusion=, acc=N/A\nexception_only_nomarker_seed456: status=QUEUED, conclusion=, acc=N/A\nexception_only_seed123: status=DONE, conclusion=success, acc=0.9983\nexception_only_seed456: status=DONE, conclusion=success, acc=0.9983\nfull_trace_1024tok_seed42: status=DONE, conclusion=negative, acc=0.7723\nfull_trace_2048tok_seed42: status=DONE, conclusion=killed, acc=N/A\nfull_trace_256tok_seed42: status=DONE, conclusion=negative, acc=0.7882\nfull_trace_512tok_seed42: status=DONE, conclusion=negative, acc=0.8042\nfull_trace_label_only_seed42: status=DONE, conclusion=success, acc=0.8622\nfull_trace_seed42: status=DONE, conclusion=killed, acc=0.284\nfull_trace_seed42_v2: status=DONE, conclusion=negative, acc=0.284\nfull_trace_seed42_v5: status=DONE, conclusion=success, acc=0.8176\nlabel_only_seed123: status=DONE, conclusion=success, acc=0.8706\nlabel_only_seed456: status=DONE, conclusion=success, acc=0.859\nloop_only_seed123: status=DONE, conclusion=success, acc=0.8588\nloop_only_seed456: status=DONE, conclusion=success, acc=0.8664\nno_trace_seed42: status=DONE, conclusion=killed, acc=N/A\nno_trace_seed42_v2: status=DONE, conclusion=killed, acc=N/A\nno_trace_seed42_v3: status=DONE, conclusion=killed, acc=0.7513\nno_trace_seed42_v4: status=DONE, conclusion=success, acc=0.7513\nno_trace_seed42_v5: status=DONE, conclusion=success, acc=0.7513\nqwen1.5b_exception_only_seed42: status=QUEUED, conclusion=killed, acc=N/A\nqwen1.5b_full_trace_seed42: status=QUEUED, conclusion=killed, acc=N/A\nqwen1.5b_no_trace_seed42: status=QUEUED, conclusion=killed, acc=N/A\nqwen1.5b_vota_seed42: status=QUEUED, conclusion=killed, acc=N/A\nqwen15b_exception_only_seed42: status=DONE, conclusion=success, acc=0.9983\nqwen15b_full_trace_seed42: status=DONE, conclusion=success, acc=0.7706\nqwen15b_no_trace_seed42: status=DONE, conclusion=success, acc=0.6731\nqwen15b_vota_seed42: status=DONE, conclusion=success, acc=0.9958\nregex_baseline_analysis: status=DONE, conclusion=success, acc=N/A\nvota_ae_only_seed42: status=DONE, conclusion=success, acc=0.9992\nvota_exception_only_seed42: status=DONE, conclusion=failed, acc=N/A\nvota_exception_only_seed42_v2: status=DONE, conclusion=success, acc=0.9983\nvota_loop_only_seed42: status=DONE, conclusion=success, acc=0.8563\nvota_no_ae_seed42: status=DONE, conclusion=success, acc=0.994\nvota_seed123: status=DONE, conclusion=failed, acc=N/A\nvota_seed42: status=DONE, conclusion=killed, acc=N/A\nvota_seed42_v2: status=DONE, conclusion=killed, acc=N/A\nvota_seed42_v3: status=DONE, conclusion=killed, acc=0.992\nvota_seed42_v4: status=DONE, conclusion=success, acc=0.9563\nvota_seed42_v5: status=DONE, conclusion=success, acc=0.9941\nvota_seed456: status=DONE, conclusion=failed, acc=N/A\nvota_seed456_v2: status=DONE, conclusion=success, acc=0.9908",
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
Now I have a comprehensive view of all experiments. Let me organize the data carefully.

Key observations about which experiments to use (selecting the best/canonical version for each):

**Qwen-2.5-Coder-7B (default model):**
- no_trace: no_trace_seed42_v5 → 0.7513 [0.7277, 0.7748]
- full_trace: full_trace_seed42_v5 → 0.8176 [0.797, 0.839]


- VOTA: vota_seed42_v5 → 0.9941 [0.9882, 0.9983]
- exception_only: vota_exception_only_seed42_v2 → 0.9983 [0.9958, 1.0], with consistent results across different seeds
- ae_only: vota_ae_only_seed42 → 0.9992 [0.9958, 1.0]
- loop_only: vota_loop_only_seed42 → 0.8563 [0.8353, 0.8756], with seed123 and seed456 showing similar performance around 0.86
- label_only: full_trace_label_only_seed42 → 0.8622 [0.8437, 0.8807], with seed123 at 0.8706 and seed456 at 0.859

The ae_only and exception_only variants are performing significantly better than the loop_only and label_only approaches, suggesting those mechanisms are more effective for this task. So for label_only, the canonical seed42 run is full_trace_label_only_seed42 at 0.8622, with multi-seed runs showing 0.8706 and 0.859. There's also vota_no_ae_seed42 as a special ablation variant at 0.994. Now I'm looking at the results across different model sizes—Qwen-2.5-Coder-1.5B shows a clear progression from 0.6731 without tracing up to 0.9958 with VOTA, and exception_only matches that at 0.9983. DeepSeek-Coder-6.7B results are starting to come in as well.

For DeepSeek, the no_trace baseline is around 0.7336 with confidence intervals, full_trace improves to 0.7916, and VOTA reaches 0.8445—though there's a re-evaluation issue flagged here. Exception_only performs much stronger at 0.9933 across multiple seeds, though seed123 drops to 0.9109. I'm noticing the VOTA result has a critical note about a catastrophic re-evaluation discrepancy when using corrected evaluation code, showing a significant 16% drop. The reeval with the corrected script shows 16% accuracy for the VOTA model, which contradicts the original 84.45%, but the group analysis breakdown suggests the 84.45% is actually correct when trained with max_length=2048—the discrepancy might stem from the evaluation setup rather than the model itself. I should use the 84.45% figure but note this unresolved inconsistency.

Now I'm reviewing the results across the other models: CodeLlama-13B's no_trace variant achieved 76.5% accuracy, while DebugBench shows strong performance across all conditions, with the exception_only and VOTA variants both reaching near-perfect scores above 99%.

I'm also looking at how the regex baselines compare—the format marker baseline performs best at 99.33%, and I'm examining the trace length ablation for Qwen-7B to see how context window size affects performance, with the full trace version reaching 81.76% accuracy.

Now I'm checking the calibration metrics across different configurations, and the results show that using only the exception type achieves remarkably low error rates, while the VOTA ensemble approach maintains strong performance around 99.4% across different random seeds. Now I'm compiling the seed robustness metrics across all approaches and models, calculating the performance variations and mean scores for each configuration. Looking at the comparative lifts between exception_only and the baseline no_trace approach to quantify the improvements each method provides. Looking at the performance differences across model sizes and conditions, I'm seeing a clear pattern emerge: approaches that leverage exception and assertion information cluster around 99.4-99.9% accuracy, while those relying only on structural trace data fall significantly lower at 75-86%. The signal-rich methods average 99.7% compared to just 82.2% for signal-poor approaches, suggesting that semantic information about program behavior is far more valuable than raw execution traces.

Now I'm ready to compile the comprehensive report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6cf6c7bc-54c9-45a8-b5e6-b498a2a84d18",
  "uuid": "83d4705f-e67b-445c-b14a-7b5191e40065",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CPHtao7YfRJosCH9W5skXU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2095,
      "cache_read_input_tokens": 36937,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2095
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

_source line 27_

All data collected. Now I'll compile the summary report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6cf6c7bc-54c9-45a8-b5e6-b498a2a84d18",
  "uuid": "182d9a66-60df-4f64-afe3-a0e0d7151405",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CPHtao7YfRJosCH9W5skXU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2095,
      "cache_read_input_tokens": 36937,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2095
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

_source line 28_

<details open><summary>🔧 Tool call — Bash · `toolu_01DWrdCfeiNpt7LEp7LvyFGU`</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/cross_scale_summary",
  "description": "Create output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6cf6c7bc-54c9-45a8-b5e6-b498a2a84d18",
  "uuid": "84845eab-5538-48a2-a467-d35779176000",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CPHtao7YfRJosCH9W5skXU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2095,
      "cache_read_input_tokens": 36937,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2095
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

_source line 29 · 2026-05-16T14:28:03.487Z_

<details><summary>↩ Tool result · `toolu_01DWrdCfeiNpt7LEp7LvyFGU`</summary>

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
  "session_id": "6cf6c7bc-54c9-45a8-b5e6-b498a2a84d18",
  "uuid": "9484ee4d-3166-438a-8638-44722b9c762e",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  }
}
```

</details>

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — Write · `toolu_014uWatZYkc8N9extxdQLbL9`</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/cross_scale_summary/results_summary.md",
  "content": "# Cross-Model / Cross-Scale Experiment Results Summary\n\nGenerated: 2026-05-16\n\n---\n\n## Table A: Main Results (per Model x Condition)\n\nAll accuracy values on test set (n=1190 unless noted). CI = 95% Wilson confidence interval.\n\n### Qwen-2.5-Coder-7B (primary model)\n\n| Condition | Accuracy | CI 95% | exp_id |\n|-----------|----------|--------|--------|\n| no_trace | 0.7513 | [0.728, 0.775] | no_trace_seed42_v5 |\n| full_trace | 0.8176 | [0.797, 0.839] | full_trace_seed42_v5 |\n| label_only | 0.8622 | [0.844, 0.881] | full_trace_label_only_seed42 |\n| loop_only | 0.8563 | [0.835, 0.876] | vota_loop_only_seed42 |\n| VOTA | 0.9941 | [0.988, 0.998] | vota_seed42_v5 |\n| ae_only | 0.9992 | [0.998, 1.000] | vota_ae_only_seed42 |\n| exception_only | 0.9983 | [0.996, 1.000] | vota_exception_only_seed42_v2 |\n\n### Qwen-2.5-Coder-1.5B\n\n| Condition | Accuracy | CI 95% | exp_id |\n|-----------|----------|--------|--------|\n| no_trace | 0.6731 | — | qwen15b_no_trace_seed42 |\n| full_trace | 0.7706 | — | qwen15b_full_trace_seed42 |\n| VOTA | 0.9958 | — | qwen15b_vota_seed42 |\n| exception_only | 0.9983 | [0.996, 1.000] | qwen15b_exception_only_seed42 |\n\n### DeepSeek-Coder-6.7B\n\n| Condition | Accuracy | CI 95% | exp_id |\n|-----------|----------|--------|--------|\n| no_trace | 0.7336 | [0.708, 0.757] | deepseek_no_trace_seed42 |\n| full_trace | 0.7916 | [0.768, 0.813] | deepseek_full_trace_seed42_v3 |\n| VOTA | 0.8445* | [0.826, 0.864] | deepseek_vota_seed42 |\n| exception_only | 0.9933 | [0.988, 0.998] | deepseek_exception_only_seed42 |\n\n*VOTA re-eval with fixed script showed 16% — discrepancy under investigation. The 84.45% value is from max_length=2048 eval; group analysis shows 100% accuracy on non-truncated training samples, 31.2% fail_recall on truncated samples.\n\n### CodeLlama-13B-Instruct\n\n| Condition | Accuracy | CI 95% | exp_id |\n|-----------|----------|--------|--------|\n| no_trace | 0.7650 | [0.738, 0.787] | codellama13b_no_trace_seed42 |\n| exception_only | RUNNING | — | codellama13b_exception_only_seed42 |\n| VOTA | RUNNING | — | codellama13b_vota_seed42 |\n\n---\n\n## Table B: Seed Robustness Summary\n\n### Qwen-2.5-Coder-7B\n\n| Condition | seed42 | seed123 | seed456 | Mean | σ | exp_ids |\n|-----------|--------|---------|---------|------|---|---------|\n| exception_only | 0.9983 | 0.9983 | 0.9983 | 0.9983 | 0.0000 | vota_exception_only_seed42_v2, exception_only_seed123, exception_only_seed456 |\n| ae_only | 0.9992 | 0.9908 | 0.9992 | 0.9964 | 0.0049 | vota_ae_only_seed42, ae_only_seed123, ae_only_seed456 |\n| VOTA | 0.9941 | — | 0.9908 | 0.9925 | 0.0023 | vota_seed42_v5, vota_seed456_v2 (seed123 failed) |\n| loop_only | 0.8563 | 0.8588 | 0.8664 | 0.8605 | 0.0053 | vota_loop_only_seed42, loop_only_seed123, loop_only_seed456 |\n| label_only | 0.8622 | 0.8706 | 0.8590 | 0.8639 | 0.0060 | full_trace_label_only_seed42, label_only_seed123, label_only_seed456 |\n\n### DeepSeek-Coder-6.7B\n\n| Condition | seed42 | seed123 | seed456 | Mean | σ | exp_ids |\n|-----------|--------|---------|---------|------|---|---------|\n| exception_only | 0.9933 | 0.9109 | 0.9933 | 0.9658 | 0.0476 | deepseek_exception_only_seed42, deepseek_exception_only_seed123, deepseek_exception_only_seed456 |\n\nNote: DeepSeek seed123 is an outlier (91.09% vs 99.33% for seed42/456). 2/3 seeds robust.\n\n---\n\n## Table C: Cross-Task Generalization (DebugBench)\n\nDefectDetection task, n=426, majority_baseline=0.5141.\n\n| Condition | Accuracy | CI 95% | Lift vs majority | exp_id |\n|-----------|----------|--------|------------------|--------|\n| no_trace | 0.9671 | [0.948, 0.984] | +0.4531 | debugbench_no_trace_seed42 |\n| VOTA | 0.9977 | [0.993, 1.000] | +0.4836 | debugbench_vota_seed42 |\n| exception_only | 1.0000 | [0.991, 1.000] | +0.4859 | debugbench_exception_only_seed42 |\n\n---\n\n## Table D: Regex Baselines (Qwen-7B test set, n=1190)\n\n| Baseline | Rule | Accuracy | exp_id |\n|----------|------|----------|--------|\n| B1 | ERROR keyword presence | 0.9345 | regex_baseline_analysis |\n| B2 | Traceback presence | 0.7151 | regex_baseline_analysis |\n| B3 | Any error keyword | 0.9345 | regex_baseline_analysis |\n| B4 | Exception type extraction | 0.9361 | regex_baseline_analysis |\n| B5 | Format marker | 0.9933 | regex_baseline_analysis |\n| B6 | Error count >= 2 | 0.9202 | regex_baseline_analysis |\n| SFT exception_only | — | 0.9983 | vota_exception_only_seed42_v2 |\n\nBest regex (B5) vs SFT gap: -0.0050 (McNemar p=0.041, significant).\n\n---\n\n## Table E: Full Trace Length Ablation (Qwen-7B, seed42)\n\n| Max tokens | Accuracy | CI 95% | exp_id |\n|------------|----------|--------|--------|\n| 256 | 0.7882 | [0.764, 0.810] | full_trace_256tok_seed42 |\n| 512 | 0.8042 | [0.782, 0.826] | full_trace_512tok_seed42 |\n| 1024 | 0.7723 | [0.749, 0.796] | full_trace_1024tok_seed42 |\n| full (2048) | 0.8176 | [0.797, 0.839] | full_trace_seed42_v5 |\n\nNon-monotonic: 512 > 1024 (information loss from mid-truncation). Best at full length but only +1.3pp over 512.\n\n---\n\n## Table F: Calibration (Qwen-7B, seed42)\n\n| Condition | ECE | MCE | Brier Score | exp_id |\n|-----------|-----|-----|-------------|--------|\n| no_trace | 0.1715 | 0.4756 | 0.1972 | calibration_analysis_seed42 |\n| full_trace | 0.0958 | 0.2491 | 0.1439 | calibration_analysis_seed42 |\n| label_only | 0.1107 | 0.4171 | 0.1201 | calibration_analysis_seed42 |\n| loop_only | 0.0831 | 0.1834 | 0.1183 | calibration_analysis_seed42 |\n| ae_only | 0.0004 | 0.0004 | 0.0008 | calibration_analysis_seed42 |\n| exception_only | 0.0027 | 0.8355 | 0.0013 | calibration_analysis_seed42 |\n| VOTA | 0.0054 | 0.6225 | 0.0052 | calibration_analysis_seed42 |\n\n---\n\n## Key Comparisons\n\n### 1. exception_only vs no_trace lift (per model)\n\n| Model | no_trace | exception_only | Δ (abs) | Δ (rel%) |\n|-------|----------|----------------|---------|----------|\n| Qwen-7B | 0.7513 | 0.9983 | +0.2470 | +32.9% |\n| Qwen-1.5B | 0.6731 | 0.9983 | +0.3252 | +48.3% |\n| DeepSeek-6.7B | 0.7336 | 0.9933 | +0.2597 | +35.4% |\n| CodeLlama-13B | 0.7650 | RUNNING | — | — |\n\nConsistent +24.7 to +32.5pp lift across all completed models.\n\n### 2. exception_only vs VOTA (per model)\n\n| Model | VOTA | exception_only | Δ | Note |\n|-------|------|----------------|---|------|\n| Qwen-7B | 0.9941 | 0.9983 | +0.0042 | p=0.01 (vota_exception_only_seed42_v2) |\n| Qwen-1.5B | 0.9958 | 0.9983 | +0.0025 | — |\n| DeepSeek-6.7B | 0.8445* | 0.9933 | +0.1488 | VOTA compromised by truncation |\n\nexception_only >= VOTA in all models. On Qwen-7B the difference is small but statistically significant.\n\n### 3. Scale comparison: 1.5B vs 7B\n\n| Condition | 1.5B | 7B | Δ (7B - 1.5B) |\n|-----------|------|----|----|\n| no_trace | 0.6731 | 0.7513 | +0.0782 |\n| full_trace | 0.7706 | 0.8176 | +0.0470 |\n| VOTA | 0.9958 | 0.9941 | -0.0017 |\n| exception_only | 0.9983 | 0.9983 | 0.0000 |\n\nPattern: scale matters for weak signals (no_trace, full_trace) but is irrelevant for strong signals (exception_only, VOTA). The 1.5B model matches or exceeds 7B when given structured trace information.\n\n### 4. Signal-Rich vs Signal-Poor Grouping (Qwen-7B)\n\n**Signal-rich** (contains exception/assertion error info):\n- ae_only: 0.9992\n- exception_only: 0.9983\n- VOTA: 0.9941\n- Mean: **0.9972**\n\n**Signal-poor** (structural/positional info only):\n- label_only: 0.8622\n- loop_only: 0.8563\n- full_trace (raw): 0.8176\n- no_trace: 0.7513\n- Mean: **0.8219**\n\nGap: **+0.1753** (signal-rich vs signal-poor).\n\nThe assertion/exception content is the critical signal. Structural trace elements (loop counts, labels, raw output) provide moderate improvement over no_trace but plateau around 85-86%.\n\n### 5. Ablation Component Hierarchy (Qwen-7B, seed42)\n\n```\nae_only      0.9992  ████████████████████████████████████████  (+24.8pp vs no_trace)\nexcept_only  0.9983  ████████████████████████████████████████  (+24.7pp)\nVOTA         0.9941  ███████████████████████████████████████   (+24.3pp)\nvota_no_ae   0.9940  ███████████████████████████████████████   (+24.3pp)\nlabel_only   0.8622  ██████████████████████████████████        (+11.1pp)\nloop_only    0.8563  █████████████████████████████████         (+10.5pp)\nfull_trace   0.8176  ██████████████████████████████            (+6.6pp)\nno_trace     0.7513  █████████████████████████████             (baseline)\nmajority     0.7151  ████████████████████████████              (chance)\n```\n\n---\n\n## Experiment Status Summary\n\n| Status | Count | Notes |\n|--------|-------|-------|\n| DONE (usable) | 35+ | Core experiments with valid metrics |\n| RUNNING | 2 | codellama13b_exception_only_seed42, codellama13b_vota_seed42 |\n| QUEUED/killed | ~12 | Superseded by v2-v5 reruns or killed early |\n| Failed | 3 | vota_seed123, vota_seed456, vota_exception_only_seed42 |\n\n---\n\n## Notes\n\n1. **Qwen-7B canonical versions**: v5 for no_trace/full_trace/VOTA (unified eval pipeline). Earlier versions (v1-v4) had eval bugs or were killed.\n2. **DeepSeek VOTA caveat**: The 84.45% accuracy may be inflated — re-eval with corrected script showed 16%. The group analysis confirms the model fails on truncated training samples. Use with asterisk.\n3. **DeepSeek full_trace reeval**: Resolved — 28.5% re-eval was caused by eval max_length=16384 (OOD). Re-eval with max_length=2048 reproduces 79.16%.\n4. **CodeLlama-13B**: Only no_trace complete (76.5%). exception_only and VOTA still running.\n5. **DebugBench**: All three conditions near-ceiling (96.7%–100%), suggesting the DefectDetection task is easier than the main CodeNet verdict task.\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6cf6c7bc-54c9-45a8-b5e6-b498a2a84d18",
  "uuid": "3e405b1d-72df-448e-a2e1-747677a19445",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KxTRfLWSQ79L1ZYA5ZsWSh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3269,
      "cache_read_input_tokens": 39032,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3269
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

_source line 31 · 2026-05-16T14:28:58.925Z_

<details><summary>↩ Tool result · `toolu_014uWatZYkc8N9extxdQLbL9`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/cross_scale_summary/results_summary.md
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6cf6c7bc-54c9-45a8-b5e6-b498a2a84d18",
  "uuid": "56b9bc07-ea4e-49cf-b90e-eca9fa38911f",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/cross_scale_summary/results_summary.md",
    "content": "# Cross-Model / Cross-Scale Experiment Results Summary\n\nGenerated: 2026-05-16\n\n---\n\n## Table A: Main Results (per Model x Condition)\n\nAll accuracy values on test set (n=1190 unless noted). CI = 95% Wilson confidence interval.\n\n### Qwen-2.5-Coder-7B (primary model)\n\n| Condition | Accuracy | CI 95% | exp_id |\n|-----------|----------|--------|--------|\n| no_trace | 0.7513 | [0.728, 0.775] | no_trace_seed42_v5 |\n| full_trace | 0.8176 | [0.797, 0.839] | full_trace_seed42_v5 |\n| label_only | 0.8622 | [0.844, 0.881] | full_trace_label_only_seed42 |\n| loop_only | 0.8563 | [0.835, 0.876] | vota_loop_only_seed42 |\n| VOTA | 0.9941 | [0.988, 0.998] | vota_seed42_v5 |\n| ae_only | 0.9992 | [0.998, 1.000] | vota_ae_only_seed42 |\n| exception_only | 0.9983 | [0.996, 1.000] | vota_exception_only_seed42_v2 |\n\n### Qwen-2.5-Coder-1.5B\n\n| Condition | Accuracy | CI 95% | exp_id |\n|-----------|----------|--------|--------|\n| no_trace | 0.6731 | — | qwen15b_no_trace_seed42 |\n| full_trace | 0.7706 | — | qwen15b_full_trace_seed42 |\n| VOTA | 0.9958 | — | qwen15b_vota_seed42 |\n| exception_only | 0.9983 | [0.996, 1.000] | qwen15b_exception_only_seed42 |\n\n### DeepSeek-Coder-6.7B\n\n| Condition | Accuracy | CI 95% | exp_id |\n|-----------|----------|--------|--------|\n| no_trace | 0.7336 | [0.708, 0.757] | deepseek_no_trace_seed42 |\n| full_trace | 0.7916 | [0.768, 0.813] | deepseek_full_trace_seed42_v3 |\n| VOTA | 0.8445* | [0.826, 0.864] | deepseek_vota_seed42 |\n| exception_only | 0.9933 | [0.988, 0.998] | deepseek_exception_only_seed42 |\n\n*VOTA re-eval with fixed script showed 16% — discrepancy under investigation. The 84.45% value is from max_length=2048 eval; group analysis shows 100% accuracy on non-truncated training samples, 31.2% fail_recall on truncated samples.\n\n### CodeLlama-13B-Instruct\n\n| Condition | Accuracy | CI 95% | exp_id |\n|-----------|----------|--------|--------|\n| no_trace | 0.7650 | [0.738, 0.787] | codellama13b_no_trace_seed42 |\n| exception_only | RUNNING | — | codellama13b_exception_only_seed42 |\n| VOTA | RUNNING | — | codellama13b_vota_seed42 |\n\n---\n\n## Table B: Seed Robustness Summary\n\n### Qwen-2.5-Coder-7B\n\n| Condition | seed42 | seed123 | seed456 | Mean | σ | exp_ids |\n|-----------|--------|---------|---------|------|---|---------|\n| exception_only | 0.9983 | 0.9983 | 0.9983 | 0.9983 | 0.0000 | vota_exception_only_seed42_v2, exception_only_seed123, exception_only_seed456 |\n| ae_only | 0.9992 | 0.9908 | 0.9992 | 0.9964 | 0.0049 | vota_ae_only_seed42, ae_only_seed123, ae_only_seed456 |\n| VOTA | 0.9941 | — | 0.9908 | 0.9925 | 0.0023 | vota_seed42_v5, vota_seed456_v2 (seed123 failed) |\n| loop_only | 0.8563 | 0.8588 | 0.8664 | 0.8605 | 0.0053 | vota_loop_only_seed42, loop_only_seed123, loop_only_seed456 |\n| label_only | 0.8622 | 0.8706 | 0.8590 | 0.8639 | 0.0060 | full_trace_label_only_seed42, label_only_seed123, label_only_seed456 |\n\n### DeepSeek-Coder-6.7B\n\n| Condition | seed42 | seed123 | seed456 | Mean | σ | exp_ids |\n|-----------|--------|---------|---------|------|---|---------|\n| exception_only | 0.9933 | 0.9109 | 0.9933 | 0.9658 | 0.0476 | deepseek_exception_only_seed42, deepseek_exception_only_seed123, deepseek_exception_only_seed456 |\n\nNote: DeepSeek seed123 is an outlier (91.09% vs 99.33% for seed42/456). 2/3 seeds robust.\n\n---\n\n## Table C: Cross-Task Generalization (DebugBench)\n\nDefectDetection task, n=426, majority_baseline=0.5141.\n\n| Condition | Accuracy | CI 95% | Lift vs majority | exp_id |\n|-----------|----------|--------|------------------|--------|\n| no_trace | 0.9671 | [0.948, 0.984] | +0.4531 | debugbench_no_trace_seed42 |\n| VOTA | 0.9977 | [0.993, 1.000] | +0.4836 | debugbench_vota_seed42 |\n| exception_only | 1.0000 | [0.991, 1.000] | +0.4859 | debugbench_exception_only_seed42 |\n\n---\n\n## Table D: Regex Baselines (Qwen-7B test set, n=1190)\n\n| Baseline | Rule | Accuracy | exp_id |\n|----------|------|----------|--------|\n| B1 | ERROR keyword presence | 0.9345 | regex_baseline_analysis |\n| B2 | Traceback presence | 0.7151 | regex_baseline_analysis |\n| B3 | Any error keyword | 0.9345 | regex_baseline_analysis |\n| B4 | Exception type extraction | 0.9361 | regex_baseline_analysis |\n| B5 | Format marker | 0.9933 | regex_baseline_analysis |\n| B6 | Error count >= 2 | 0.9202 | regex_baseline_analysis |\n| SFT exception_only | — | 0.9983 | vota_exception_only_seed42_v2 |\n\nBest regex (B5) vs SFT gap: -0.0050 (McNemar p=0.041, significant).\n\n---\n\n## Table E: Full Trace Length Ablation (Qwen-7B, seed42)\n\n| Max tokens | Accuracy | CI 95% | exp_id |\n|------------|----------|--------|--------|\n| 256 | 0.7882 | [0.764, 0.810] | full_trace_256tok_seed42 |\n| 512 | 0.8042 | [0.782, 0.826] | full_trace_512tok_seed42 |\n| 1024 | 0.7723 | [0.749, 0.796] | full_trace_1024tok_seed42 |\n| full (2048) | 0.8176 | [0.797, 0.839] | full_trace_seed42_v5 |\n\nNon-monotonic: 512 > 1024 (information loss from mid-truncation). Best at full length but only +1.3pp over 512.\n\n---\n\n## Table F: Calibration (Qwen-7B, seed42)\n\n| Condition | ECE | MCE | Brier Score | exp_id |\n|-----------|-----|-----|-------------|--------|\n| no_trace | 0.1715 | 0.4756 | 0.1972 | calibration_analysis_seed42 |\n| full_trace | 0.0958 | 0.2491 | 0.1439 | calibration_analysis_seed42 |\n| label_only | 0.1107 | 0.4171 | 0.1201 | calibration_analysis_seed42 |\n| loop_only | 0.0831 | 0.1834 | 0.1183 | calibration_analysis_seed42 |\n| ae_only | 0.0004 | 0.0004 | 0.0008 | calibration_analysis_seed42 |\n| exception_only | 0.0027 | 0.8355 | 0.0013 | calibration_analysis_seed42 |\n| VOTA | 0.0054 | 0.6225 | 0.0052 | calibration_analysis_seed42 |\n\n---\n\n## Key Comparisons\n\n### 1. exception_only vs no_trace lift (per model)\n\n| Model | no_trace | exception_only | Δ (abs) | Δ (rel%) |\n|-------|----------|----------------|---------|----------|\n| Qwen-7B | 0.7513 | 0.9983 | +0.2470 | +32.9% |\n| Qwen-1.5B | 0.6731 | 0.9983 | +0.3252 | +48.3% |\n| DeepSeek-6.7B | 0.7336 | 0.9933 | +0.2597 | +35.4% |\n| CodeLlama-13B | 0.7650 | RUNNING | — | — |\n\nConsistent +24.7 to +32.5pp lift across all completed models.\n\n### 2. exception_only vs VOTA (per model)\n\n| Model | VOTA | exception_only | Δ | Note |\n|-------|------|----------------|---|------|\n| Qwen-7B | 0.9941 | 0.9983 | +0.0042 | p=0.01 (vota_exception_only_seed42_v2) |\n| Qwen-1.5B | 0.9958 | 0.9983 | +0.0025 | — |\n| DeepSeek-6.7B | 0.8445* | 0.9933 | +0.1488 | VOTA compromised by truncation |\n\nexception_only >= VOTA in all models. On Qwen-7B the difference is small but statistically significant.\n\n### 3. Scale comparison: 1.5B vs 7B\n\n| Condition | 1.5B | 7B | Δ (7B - 1.5B) |\n|-----------|------|----|----|\n| no_trace | 0.6731 | 0.7513 | +0.0782 |\n| full_trace | 0.7706 | 0.8176 | +0.0470 |\n| VOTA | 0.9958 | 0.9941 | -0.0017 |\n| exception_only | 0.9983 | 0.9983 | 0.0000 |\n\nPattern: scale matters for weak signals (no_trace, full_trace) but is irrelevant for strong signals (exception_only, VOTA). The 1.5B model matches or exceeds 7B when given structured trace information.\n\n### 4. Signal-Rich vs Signal-Poor Grouping (Qwen-7B)\n\n**Signal-rich** (contains exception/assertion error info):\n- ae_only: 0.9992\n- exception_only: 0.9983\n- VOTA: 0.9941\n- Mean: **0.9972**\n\n**Signal-poor** (structural/positional info only):\n- label_only: 0.8622\n- loop_only: 0.8563\n- full_trace (raw): 0.8176\n- no_trace: 0.7513\n- Mean: **0.8219**\n\nGap: **+0.1753** (signal-rich vs signal-poor).\n\nThe assertion/exception content is the critical signal. Structural trace elements (loop counts, labels, raw output) provide moderate improvement over no_trace but plateau around 85-86%.\n\n### 5. Ablation Component Hierarchy (Qwen-7B, seed42)\n\n```\nae_only      0.9992  ████████████████████████████████████████  (+24.8pp vs no_trace)\nexcept_only  0.9983  ████████████████████████████████████████  (+24.7pp)\nVOTA         0.9941  ███████████████████████████████████████   (+24.3pp)\nvota_no_ae   0.9940  ███████████████████████████████████████   (+24.3pp)\nlabel_only   0.8622  ██████████████████████████████████        (+11.1pp)\nloop_only    0.8563  █████████████████████████████████         (+10.5pp)\nfull_trace   0.8176  ██████████████████████████████            (+6.6pp)\nno_trace     0.7513  █████████████████████████████             (baseline)\nmajority     0.7151  ████████████████████████████              (chance)\n```\n\n---\n\n## Experiment Status Summary\n\n| Status | Count | Notes |\n|--------|-------|-------|\n| DONE (usable) | 35+ | Core experiments with valid metrics |\n| RUNNING | 2 | codellama13b_exception_only_seed42, codellama13b_vota_seed42 |\n| QUEUED/killed | ~12 | Superseded by v2-v5 reruns or killed early |\n| Failed | 3 | vota_seed123, vota_seed456, vota_exception_only_seed42 |\n\n---\n\n## Notes\n\n1. **Qwen-7B canonical versions**: v5 for no_trace/full_trace/VOTA (unified eval pipeline). Earlier versions (v1-v4) had eval bugs or were killed.\n2. **DeepSeek VOTA caveat**: The 84.45% accuracy may be inflated — re-eval with corrected script showed 16%. The group analysis confirms the model fails on truncated training samples. Use with asterisk.\n3. **DeepSeek full_trace reeval**: Resolved — 28.5% re-eval was caused by eval max_length=16384 (OOD). Re-eval with max_length=2048 reproduces 79.16%.\n4. **CodeLlama-13B**: Only no_trace complete (76.5%). exception_only and VOTA still running.\n5. **DebugBench**: All three conditions near-ceiling (96.7%–100%), suggesting the DefectDetection task is easier than the main CodeNet verdict task.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
````

</details>

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_011m1cbuk96zUx6v4yshdaBg`</summary>

```json
{
  "name": "cross_scale_results_summary",
  "type": "report",
  "description": "Complete cross-model/cross-scale experiment results summary with 6 tables (Main Results, Seed Robustness, DebugBench, Regex Baselines, Length Ablation, Calibration) and 5 key comparison analyses. All numbers annotated with exp_id source.",
  "project": "trace-verdict-study",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/cross_scale_summary/results_summary.md",
  "tags": [
    "results",
    "summary",
    "cross-model",
    "cross-scale",
    "paper-table"
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
  "session_id": "6cf6c7bc-54c9-45a8-b5e6-b498a2a84d18",
  "uuid": "2ed9a5c6-244b-4cd2-865f-7fad3f9bce7e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0151BXTNxRYMzFAVHfU43RSG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4129,
      "cache_read_input_tokens": 42301,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4129
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

_source line 33 · 2026-05-16T14:29:04.284Z_

<details><summary>↩ Tool result · `toolu_011m1cbuk96zUx6v4yshdaBg`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_3affa6\", \"name\": \"cross_scale_results_summary\", \"type\": \"report\", \"description\": \"Complete cross-model/cross-scale experiment results summary with 6 tables (Main Results, Seed Robustness, DebugBench, Regex Baselines, Length Ablation, Calibration) and 5 key comparison analyses. All numbers annotated with exp_id source.\", \"path\": \"projects/trace-verdict-study/artifacts/_project/report/results_summary.md\", \"url\": null, \"project\": \"trace-verdict-study\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T14:29:04.176974+00:00\", \"tags\": [\"results\", \"summary\", \"cross-model\", \"cross-scale\", \"paper-table\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6cf6c7bc-54c9-45a8-b5e6-b498a2a84d18",
  "uuid": "32f8ee36-d814-4071-9216-998130883606",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260516_3affa6\\\", \\\"name\\\": \\\"cross_scale_results_summary\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Complete cross-model/cross-scale experiment results summary with 6 tables (Main Results, Seed Robustness, DebugBench, Regex Baselines, Length Ablation, Calibration) and 5 key comparison analyses. All numbers annotated with exp_id source.\\\", \\\"path\\\": \\\"projects/trace-verdict-study/artifacts/_project/report/results_summary.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"trace-verdict-study\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-16T14:29:04.176974+00:00\\\", \\\"tags\\\": [\\\"results\\\", \\\"summary\\\", \\\"cross-model\\\", \\\"cross-scale\\\", \\\"paper-table\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_3affa6\", \"name\": \"cross_scale_results_summary\", \"type\": \"report\", \"description\": \"Complete cross-model/cross-scale experiment results summary with 6 tables (Main Results, Seed Robustness, DebugBench, Regex Baselines, Length Ablation, Calibration) and 5 key comparison analyses. All numbers annotated with exp_id source.\", \"path\": \"projects/trace-verdict-study/artifacts/_project/report/results_summary.md\", \"url\": null, \"project\": \"trace-verdict-study\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T14:29:04.176974+00:00\", \"tags\": [\"results\", \"summary\", \"cross-model\", \"cross-scale\", \"paper-table\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 34_

报告已写入并注册。核心发现：

**6 张表**：Main Results (4 models)、Seed Robustness、DebugBench、Regex Baselines、Length Ablation、Calibration。

**关键结论**：
- **exception_only 跨模型一致性强**：Qwen-7B/1.5B/DeepSeek 均达 99.3%+，vs no_trace 提升 +24.7 到 +32.5pp
- **exception_only >= VOTA**：所有模型上 exception_only 持平或优于 VOTA（Qwen-7B 上 p=0.01）
- **Scale 对强信号无关**：1.5B 在 exception_only/VOTA 上与 7B 持平，仅在 no_trace/full_trace 上落后 5-8pp
- **Signal-rich vs signal-poor 分界清晰**：含异常/断言信息的条件均值 99.7%，仅含结构信息的条件均值 82.2%，gap=17.5pp
- **Seed 鲁棒性**：exception_only (Qwen-7B) 三 seed 完全一致 (99.83%)；ae_only σ=0.49%；DeepSeek seed123 是 outlier (91.1% vs 99.3%)
- **待补数据**：CodeLlama-13B exception_only 和 VOTA 仍在 RUNNING

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6cf6c7bc-54c9-45a8-b5e6-b498a2a84d18",
  "uuid": "558e806c-8d59-4be1-83e4-6e6c7750650b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RPzkAQftgKh8dJHJYB8nUW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 597,
      "cache_read_input_tokens": 46430,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 597
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

_source line 35_

报告已写入并注册。核心发现：

**6 张表**：Main Results (4 models)、Seed Robustness、DebugBench、Regex Baselines、Length Ablation、Calibration。

**关键结论**：
- **exception_only 跨模型一致性强**：Qwen-7B/1.5B/DeepSeek 均达 99.3%+，vs no_trace 提升 +24.7 到 +32.5pp
- **exception_only >= VOTA**：所有模型上 exception_only 持平或优于 VOTA（Qwen-7B 上 p=0.01）
- **Scale 对强信号无关**：1.5B 在 exception_only/VOTA 上与 7B 持平，仅在 no_trace/full_trace 上落后 5-8pp
- **Signal-rich vs signal-poor 分界清晰**：含异常/断言信息的条件均值 99.7%，仅含结构信息的条件均值 82.2%，gap=17.5pp
- **Seed 鲁棒性**：exception_only (Qwen-7B) 三 seed 完全一致 (99.83%)；ae_only σ=0.49%；DeepSeek seed123 是 outlier (91.1% vs 99.3%)
- **待补数据**：CodeLlama-13B exception_only 和 VOTA 仍在 RUNNING

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 176316,
  "duration_api_ms": 175160,
  "num_turns": 13,
  "stop_reason": "end_turn",
  "session_id": "6cf6c7bc-54c9-45a8-b5e6-b498a2a84d18",
  "total_cost_usd": 0.683501,
  "usage": {
    "input_tokens": 17,
    "cache_creation_input_tokens": 35186,
    "cache_read_input_tokens": 391351,
    "output_tokens": 10649,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 35186,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 403,
        "cache_read_input_tokens": 46430,
        "cache_creation_input_tokens": 597,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 597
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1513,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001603,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 17,
      "outputTokens": 10649,
      "cacheReadInputTokens": 391351,
      "cacheCreationInputTokens": 35186,
      "webSearchRequests": 0,
      "costUSD": 0.681898,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "b271586f-a3ef-4956-b915-86b0a8f95bf4"
}
```

</details>

---
