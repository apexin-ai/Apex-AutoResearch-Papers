# analysis comprehensive results table

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 40
- **Recorded user turns:** 0
- **Tool calls:** 14
- **Original source:** `logs/workers/worker_analysis_comprehensive-results-table_20260516T175236.log`
- **Structured JSON:** [`2024bf16677c7099f12c.json`](../../sessions/20/2024bf16677c7099f12c.json)

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "session_id": "4a270429-54da-4381-97e3-905a06c925c1",
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
  "uuid": "98de1f77-6c1d-4f75-9bca-9204d1178328",
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
  "uuid": "ebef6950-5ddc-4103-af56-78098c933ccb",
  "session_id": "4a270429-54da-4381-97e3-905a06c925c1"
}
```

---

### Assistant

_source line 4_

I'll read the registry to get all experiment data, then compile the results tables.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a270429-54da-4381-97e3-905a06c925c1",
  "uuid": "fe3eb219-197f-41de-aafe-b0c9ddc9c89e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012SsAFMDphxScN9qtmhCCxt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12047,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12047
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01NuQpAddg2unBEv3jvPKNFq`</summary>

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
  "session_id": "4a270429-54da-4381-97e3-905a06c925c1",
  "uuid": "33b2a842-1a21-4d72-a78d-b26a5f0dfb02",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012SsAFMDphxScN9qtmhCCxt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12047,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12047
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

_source line 6 · 2026-05-16T17:52:45.444Z_

<details><summary>↩ Tool result · `toolu_01NuQpAddg2unBEv3jvPKNFq`</summary>

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
  "session_id": "4a270429-54da-4381-97e3-905a06c925c1",
  "uuid": "b9f0c5ce-c005-4fbf-8256-f120267d1769",
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

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Let me read the registry to get all experiments with status DONE and conclusion success.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a270429-54da-4381-97e3-905a06c925c1",
  "uuid": "4c4c9b05-c562-467c-9593-8b5b71323e9e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013fyKap47LV9gmPWksdhxoQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 466,
      "cache_read_input_tokens": 23888,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 466
      },
      "output_tokens": 49,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_018H9G6xFwPEVsAmoDwPTMZE`</summary>

```json
{
  "project": "trace-verdict-study",
  "filters": {
    "status": "DONE",
    "conclusion": "success"
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
  "session_id": "4a270429-54da-4381-97e3-905a06c925c1",
  "uuid": "a9c7e7e5-48fa-4b34-b5db-a885b835dbcc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013fyKap47LV9gmPWksdhxoQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 466,
      "cache_read_input_tokens": 23888,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 466
      },
      "output_tokens": 49,
      "service_tier": "standard",
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

_source line 9 · 2026-05-16T17:52:49.518Z_

<details><summary>↩ Tool result · `toolu_018H9G6xFwPEVsAmoDwPTMZE`</summary>

```text
Error: result (91,017 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/4a270429-54da-4381-97e3-905a06c925c1/tool-results/mcp-agent-ml-research-read_registry-1778953969502.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/4a270429-54da-4381-97e3-905a06c925c1/tool-results/mcp-agent-ml-research-read_registry-1778953969502.txt in sequential chunks until 100% of the content has been read.
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
  "session_id": "4a270429-54da-4381-97e3-905a06c925c1",
  "uuid": "d25c402d-a2df-49a6-a206-ce6785667a50",
  "tool_use_result": {
    "content": "Error: result (91,017 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/4a270429-54da-4381-97e3-905a06c925c1/tool-results/mcp-agent-ml-research-read_registry-1778953969502.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/4a270429-54da-4381-97e3-905a06c925c1/tool-results/mcp-agent-ml-research-read_registry-1778953969502.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"qwen15b_nomarker_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T17:29:18.046Z\", \"updated_at\": \"2026-05-16T17:47:36.397Z\", \"spec\": {\"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"account\": \"root\", \"command\": \"cd /root/trace-verdict-study && /root/miniconda3/bin/python train/train_sft.py --condition exception_only_nomarker --model_path /root/trace-verdict-study/models/Qwen2.5-Coder-1.5B-Instruct --gradient_checkpointing --gpu 0 --seed 42\", \"pid\": \"292150\", \"log_path\": \"/tmp/qwen15b_nomarker_seed42.log\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/exception_only_nomarker_train.jsonl\", \"data_count\": 4720, \"model_name\": \"Qwen2.5-Coder-1.5B-Instruct\", \"seed\": 42}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_nomarker/final/\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.978, \"n\": 1190, \"accuracy_ci\": [0.97, 0.986], \"majority_baseline\": 0.715, \"lift\": 0.263, \"pass_precision\": 0.97, \"pass_recall\": 1, \"pass_f1\": 0.98, \"fail_precision\": 1, \"fail_recall\": 0.92, \"fail_f1\": 0.96}, \"completed_at\": \"2026-05-16T17:47:36.397Z\"}, \"exception_only_nomarker_seed42\": {\"status\": \"DONE\", \"retry_count\": 2, \"created_at\": \"2026-05-16T06:03:33.324Z\", \"updated_at\": \"2026-05-16T17:09:23.981Z\", \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"reproduce\": {\"finished_at\": \"2026-05-16T17:06:14.692Z\"}, \"completed_at\": \"2026-05-16T15:50:22.017Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T15:50:23.894246+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T17:06:17.875239+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"python train/train_sft.py --condition exception_only_nomarker --model_path models/Qwen2.5-Coder-7B-Instruct --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_nomarker_seed42 --wandb_run_name exception_only_nomarker_seed42 --gradient_checkpointing && python eval/evaluate.py --condition exception_only_nomarker --checkpoint_dir .../exception_only_nomarker_seed42/final --save_predictions\", \"server\": \"westd-11235\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/exception_only_nomarker_{train,test}.jsonl\", \"data_count\": 5910, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_nomarker_seed42\", \"log_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_nomarker_seed42_train.log\", \"gpu\": \"cuda:0\", \"tmux_session\": \"nomarker_seed42\", \"description\": \"R1-N1 control: exception_only with ALL bracket format markers removed\", \"markers_removed\": [\"[No exception data in trace]\", \"[ERROR] prefix\", \"[No trace available]\", \"[...trace truncated...]\"], \"train_samples\": 4720, \"test_samples\": 1190}, \"wandb_run_id\": \"exception_only_nomarker_seed42\", \"pid\": 287933, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.9655, \"n\": 1190, \"accuracy_ci\": [0.955, 0.976]}}, \"codellama13b_exception_only_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:47:18.896Z\", \"updated_at\": \"2026-05-16T14:48:23.848Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition exception_only --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_exception_only_seed42 --wandb_project trace-verdict-study --wandb_run_name codellama13b_exception_only_seed42 && python eval/evaluate.py --condition exception_only --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_exception_only_seed42/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_exception_only_seed42/final/eval_results.json --save_predictions\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"271776\", \"log_path\": \"~/runs/trace-verdict-study/codellama13b_exception_only_seed42.log\", \"submitted_at\": \"2026-05-16T12:03:38.585Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 9885.3, \"gpu_hours\": 2.75}, \"server\": \"westd-11235\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"pid\": \"271776\", \"log_path\": \"~/runs/trace-verdict-study/codellama13b_exception_only_seed42.log\", \"wandb_run_id\": \"codellama13b_exception_only_seed42\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition exception_only --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_exception_only_seed42 --wandb_project trace-verdict-study --wandb_run_name codellama13b_exception_only_seed42 && python eval/evaluate.py --condition exception_only --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_exception_only_seed42/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_exception_only_seed42/final/eval_results.json --save_predictions\\\"\", \"wandb_run_id\": \"codellama13b_exception_only_seed42\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\", \"finished_at\": \"2026-05-16T14:45:17.342Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T14:45:19.404390+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_exception_only_seed42/final/\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.9983, \"n\": 1190, \"errors\": 2}, \"completed_at\": \"2026-05-16T14:48:23.848Z\"}, \"loop_only_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T06:03:36.673Z\", \"updated_at\": \"2026-05-16T14:26:30.516Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition loop_only --gradient_checkpointing --gpu 0 --seed 456 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/loop_only_seed456 --wandb_project trace-verdict-study --wandb_run_name loop_only_seed456 && python eval/evaluate.py --condition loop_only --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/loop_only_seed456/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/loop_only_seed456/final/eval_results.json --save_predictions\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"269723\", \"log_path\": \"~/runs/trace-verdict-study/loop_only_seed456.log\", \"submitted_at\": \"2026-05-16T11:31:50.484Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 7892.7, \"gpu_hours\": 2.19}, \"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"pid\": \"269723\", \"log_path\": \"~/runs/trace-verdict-study/loop_only_seed456.log\", \"wandb_run_id\": \"loop_only_seed456\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition loop_only --gradient_checkpointing --gpu 0 --seed 456 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/loop_only_seed456 --wandb_project trace-verdict-study --wandb_run_name loop_only_seed456 && python eval/evaluate.py --condition loop_only --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/loop_only_seed456/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/loop_only_seed456/final/eval_results.json --save_predictions\\\"\", \"wandb_run_id\": \"loop_only_seed456\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\", \"finished_at\": \"2026-05-16T13:39:35.472Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T13:39:37.576842+00:00\"}]}, \"metrics\": {\"accuracy\": 0.8664, \"n\": 1190, \"pass_precision\": 0.9179, \"pass_recall\": 0.8931, \"pass_f1\": 0.9053, \"fail_precision\": 0.7486, \"fail_recall\": 0.7994, \"fail_f1\": 0.7732, \"accuracy_ci\": [0.847, 0.884]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/loop_only_seed456/final\", \"completed_at\": \"2026-05-16T13:43:23.144Z\", \"notes\": \"Loop_only seed robustness 完成: seed42=85.63%, seed123=85.88%, seed456=86.64%. Mean=86.05% ± 0.43. 稳定。\"}, \"loop_only_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T06:03:35.196Z\", \"updated_at\": \"2026-05-16T14:26:29.406Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition loop_only --gradient_checkpointing --gpu 0 --seed 123 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/loop_only_seed123 --wandb_project trace-verdict-study --wandb_run_name loop_only_seed123 && python eval/evaluate.py --condition loop_only --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/loop_only_seed123/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/loop_only_seed123/final/eval_results.json --save_predictions\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"261213\", \"log_path\": \"~/runs/trace-verdict-study/loop_only_seed123.log\", \"submitted_at\": \"2026-05-16T09:21:29.194Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/loop_only_seed123/final\", \"wall_clock_seconds\": 7779.8, \"gpu_hours\": 2.16}, \"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"pid\": \"261213\", \"log_path\": \"~/runs/trace-verdict-study/loop_only_seed123.log\", \"wandb_run_id\": \"loop_only_seed123\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition loop_only --gradient_checkpointing --gpu 0 --seed 123 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/loop_only_seed123 --wandb_project trace-verdict-study --wandb_run_name loop_only_seed123 && python eval/evaluate.py --condition loop_only --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/loop_only_seed123/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/loop_only_seed123/final/eval_results.json --save_predictions\\\"\", \"wandb_run_id\": \"loop_only_seed123\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\", \"finished_at\": \"2026-05-16T11:28:44.218Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T11:28:46.379629+00:00\"}]}, \"metrics\": {\"accuracy\": 0.8588, \"majority_baseline\": 0.7151, \"lift\": 0.1437, \"n\": 1190, \"pass_precision\": 0.9129, \"pass_recall\": 0.8872, \"pass_f1\": 0.8999, \"fail_precision\": 0.7355, \"fail_recall\": 0.7876, \"fail_f1\": 0.7607, \"accuracy_ci\": [0.8403, 0.8773]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T11:31:09.027Z\", \"notes\": \"Loop_only seed robustness 完成: seed42=85.63%, seed123=85.88%, seed456=86.64%. Mean=86.05% ± 0.43. 稳定。\"}, \"codellama13b_no_trace_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:47:20.182Z\", \"updated_at\": \"2026-05-16T14:22:58.643Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition no_trace --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_no_trace_seed42 --wandb_project trace-verdict-study --wandb_run_name codellama13b_no_trace_seed42 && python eval/evaluate.py --condition no_trace --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_no_trace_seed42/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_no_trace_seed42/final/eval_results.json --save_predictions\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"277044\", \"log_path\": \"~/runs/trace-verdict-study/codellama13b_no_trace_seed42.log\", \"submitted_at\": \"2026-05-16T13:42:06.812Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 2451.8, \"gpu_hours\": 0.68}, \"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"pid\": \"277044\", \"log_path\": \"~/runs/trace-verdict-study/codellama13b_no_trace_seed42.log\", \"wandb_run_id\": \"codellama13b_no_trace_seed42\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition no_trace --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_no_trace_seed42 --wandb_project trace-verdict-study --wandb_run_name codellama13b_no_trace_seed42 && python eval/evaluate.py --condition no_trace --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_no_trace_seed42/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_no_trace_seed42/final/eval_results.json --save_predictions\\\"\", \"wandb_run_id\": \"codellama13b_no_trace_seed42\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\", \"finished_at\": \"2026-05-16T14:19:42.177Z\"}, \"gpu_ids\": [\"cuda:1\"], \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T14:19:44.574583+00:00\"}]}, \"metrics\": {\"accuracy\": 0.765, \"n\": 1190, \"majority_baseline\": 0.7151, \"lift\": 0.05, \"pass_precision\": 0.84, \"pass_recall\": 0.83, \"pass_f1\": 0.84, \"fail_precision\": 0.59, \"fail_recall\": 0.59, \"fail_f1\": 0.59, \"accuracy_ci\": [0.738, 0.787]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_no_trace_seed42/final\", \"completed_at\": \"2026-05-16T14:22:58.643Z\"}, \"qwen15b_full_trace_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T09:22:03.743Z\", \"updated_at\": \"2026-05-16T12:03:49.820Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition full_trace --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_seed42 --wandb_project trace-verdict-study --wandb_run_name qwen15b_full_trace_seed42 && python eval/evaluate.py --condition full_trace --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_seed42/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_seed42/final/eval_results.json --save_predictions\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"267886\", \"log_path\": \"~/runs/trace-verdict-study/qwen15b_full_trace_seed42.log\", \"submitted_at\": \"2026-05-16T11:10:01.431Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 3228.4, \"gpu_hours\": 0.9}, \"server\": \"westd-11235\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"pid\": \"267886\", \"log_path\": \"~/runs/trace-verdict-study/qwen15b_full_trace_seed42.log\", \"wandb_run_id\": \"qwen15b_full_trace_seed42\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition full_trace --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_seed42 --wandb_project trace-verdict-study --wandb_run_name qwen15b_full_trace_seed42 && python eval/evaluate.py --condition full_trace --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_seed42/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_seed42/final/eval_results.json --save_predictions\\\"\", \"wandb_run_id\": \"qwen15b_full_trace_seed42\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\", \"finished_at\": \"2026-05-16T12:00:28.907Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T12:00:31.043272+00:00\"}]}, \"metrics\": {\"accuracy\": 0.7706, \"n\": 1190}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_seed42/final\", \"completed_at\": \"2026-05-16T12:03:49.820Z\"}, \"qwen15b_vota_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T09:22:02.463Z\", \"updated_at\": \"2026-05-16T11:09:39.319Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition vota --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_vota_seed42 --wandb_project trace-verdict-study --wandb_run_name qwen15b_vota_seed42 && python eval/evaluate.py --condition vota --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_vota_seed42/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_vota_seed42/final/eval_results.json --save_predictions\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"265006\", \"log_path\": \"~/runs/trace-verdict-study/qwen15b_vota_seed42.log\", \"submitted_at\": \"2026-05-16T10:15:27.340Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_vota_seed42/final\", \"wall_clock_seconds\": 3252.0, \"gpu_hours\": 0.9}, \"server\": \"westd-11235\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"pid\": \"265006\", \"log_path\": \"~/runs/trace-verdict-study/qwen15b_vota_seed42.log\", \"wandb_run_id\": \"qwen15b_vota_seed42\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition vota --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_vota_seed42 --wandb_project trace-verdict-study --wandb_run_name qwen15b_vota_seed42 && python eval/evaluate.py --condition vota --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_vota_seed42/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_vota_seed42/final/eval_results.json --save_predictions\\\"\", \"wandb_run_id\": \"qwen15b_vota_seed42\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\", \"finished_at\": \"2026-05-16T11:07:13.230Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T11:07:15.416174+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.9958, \"n\": 1190, \"pass_recall\": 0.9976, \"fail_recall\": 0.9912, \"pass_f1\": 0.9971, \"fail_f1\": 0.9926, \"training_time_sec\": 2922}, \"completed_at\": \"2026-05-16T11:09:39.319Z\"}, \"qwen15b_no_trace_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T09:22:01.028Z\", \"updated_at\": \"2026-05-16T10:15:10.017Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition no_trace --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_no_trace_seed42 --wandb_project trace-verdict-study --wandb_run_name qwen15b_no_trace_seed42 && python eval/evaluate.py --condition no_trace --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_no_trace_seed42/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_no_trace_seed42/final/eval_results.json --save_predictions\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"263569\", \"log_path\": \"~/runs/trace-verdict-study/qwen15b_no_trace_seed42.log\", \"submitted_at\": \"2026-05-16T09:56:11.214Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_no_trace_seed42/final\", \"wall_clock_seconds\": 1138.8, \"gpu_hours\": 0.32}, \"server\": \"westd-11235\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"pid\": \"263569\", \"log_path\": \"~/runs/trace-verdict-study/qwen15b_no_trace_seed42.log\", \"wandb_run_id\": \"qwen15b_no_trace_seed42\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition no_trace --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_no_trace_seed42 --wandb_project trace-verdict-study --wandb_run_name qwen15b_no_trace_seed42 && python eval/evaluate.py --condition no_trace --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_no_trace_seed42/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_no_trace_seed42/final/eval_results.json --save_predictions\\\"\", \"wandb_run_id\": \"qwen15b_no_trace_seed42\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\", \"finished_at\": \"2026-05-16T10:13:02.700Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T10:13:04.620520+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.6731, \"n\": 1190, \"pass_f1\": 0.7527, \"fail_f1\": 0.518, \"lift_over_majority\": -0.042, \"training_time_sec\": 851}, \"completed_at\": \"2026-05-16T10:15:10.018Z\"}, \"qwen15b_exception_only_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T09:22:13.547Z\", \"updated_at\": \"2026-05-16T09:55:51.757Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition exception_only --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_exception_only_seed42 --wandb_project trace-verdict-study --wandb_run_name qwen15b_exception_only_seed42 && python eval/evaluate.py --condition exception_only --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_exception_only_seed42/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_exception_only_seed42/final/eval_results.json --save_predictions\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"261588\", \"log_path\": \"~/runs/trace-verdict-study/qwen15b_exception_only_seed42.log\", \"submitted_at\": \"2026-05-16T09:22:34.937Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_exception_only_seed42/final\", \"wall_clock_seconds\": 1990.3, \"gpu_hours\": 0.55}, \"server\": \"westd-11235\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"pid\": \"261588\", \"log_path\": \"~/runs/trace-verdict-study/qwen15b_exception_only_seed42.log\", \"wandb_run_id\": \"qwen15b_exception_only_seed42\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition exception_only --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_exception_only_seed42 --wandb_project trace-verdict-study --wandb_run_name qwen15b_exception_only_seed42 && python eval/evaluate.py --condition exception_only --model_path /root/autodl-tmp/models/Qwen2.5-Coder-1.5B-Instruct --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_exception_only_seed42/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_exception_only_seed42/final/eval_results.json --save_predictions\\\"\", \"wandb_run_id\": \"qwen15b_exception_only_seed42\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\", \"finished_at\": \"2026-05-16T09:53:32.293Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T09:53:34.556600+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.9983, \"accuracy_ci_lower\": 0.9958, \"accuracy_ci_upper\": 1, \"majority_baseline\": 0.7151, \"lift\": 0.283, \"n\": 1190, \"pass_precision\": 1, \"pass_recall\": 0.9976, \"pass_f1\": 0.9988, \"fail_precision\": 0.9941, \"fail_recall\": 1, \"fail_f1\": 0.9971, \"train_loss\": 0.1347, \"eval_loss\": 0.5761, \"wall_clock_seconds\": 1762}, \"completed_at\": \"2026-05-16T09:55:45.253Z\"}, \"label_only_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T04:40:19.669Z\", \"updated_at\": \"2026-05-16T09:22:46.929Z\", \"hypothesis\": \"Seed robustness: label_only (full_trace + label-only loss) with seed=456 on Qwen-2.5-Coder-7B. Verifies label_only 86.22% stability across seeds.\", \"parent\": \"full_trace_label_only_seed42\", \"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-16T05:31:03.019Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition full_trace --label_only_loss --gradient_checkpointing --gpu 0 --seed 456 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_label_only_seed456 --wandb_project trace-verdict-study --wandb_run_name label_only_seed456 && python eval/evaluate.py --condition full_trace --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_label_only_seed456/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_label_only_seed456/final/eval_results.json --save_predictions\\\"\", \"wandb_run_id\": \"label_only_seed456\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\", \"finished_at\": \"2026-05-16T09:01:08.445Z\", \"training_hours\": 3.5}, \"spec\": {\"command\": \"python train/train_sft.py --condition full_trace --label_only_loss --gradient_checkpointing --gpu 0 --seed 456 + evaluate.py\", \"server\": \"westd-11235\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/full_trace_{train,test}.jsonl\", \"data_count\": 5910, \"model_name\": \"Qwen/Qwen2.5-Coder-7B-Instruct\", \"seed\": 456, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_label_only_seed456/final\", \"log_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_label_only_seed456/final/eval_results.json\"}, \"pid\": \"249616\", \"log_path\": \"~/runs/trace-verdict-study/label_only_seed456.log\", \"wandb_run_id\": \"label_only_seed456\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T09:01:14.180779+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.859, \"n\": 1190, \"pass_recall\": 0.938, \"fail_recall\": 0.661, \"pass_f1\": 0.905, \"fail_f1\": 0.727}, \"completed_at\": \"2026-05-16T09:22:46.929Z\"}, \"label_only_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T04:40:18.683Z\", \"updated_at\": \"2026-05-16T09:01:41.007Z\", \"hypothesis\": \"Seed robustness: label_only (full_trace + label-only loss) with seed=123 on Qwen-2.5-Coder-7B. Verifies label_only 86.22% stability across seeds.\", \"parent\": \"full_trace_label_only_seed42\", \"server\": \"westd-11235\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-11235\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-16T05:31:02.488Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition full_trace --label_only_loss --gradient_checkpointing --gpu 0 --seed 123 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_label_only_seed123 --wandb_project trace-verdict-study --wandb_run_name label_only_seed123 && python eval/evaluate.py --condition full_trace --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_label_only_seed123/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_label_only_seed123/final/eval_results.json --save_predictions\\\"\", \"wandb_run_id\": \"label_only_seed123\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\", \"finished_at\": \"2026-05-16T08:58:33.644Z\", \"training_hours\": 3.46}, \"spec\": {\"command\": \"python train/train_sft.py --condition full_trace --label_only_loss --gradient_checkpointing --gpu 0 --seed 123 + evaluate.py\", \"server\": \"westd-11235\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/full_trace_{train,test}.jsonl\", \"data_count\": 5910, \"model_name\": \"Qwen/Qwen2.5-Coder-7B-Instruct\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_label_only_seed123/final\", \"log_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_label_only_seed123/final/eval_results.json\"}, \"pid\": \"249124\", \"log_path\": \"~/runs/trace-verdict-study/label_only_seed123.log\", \"wandb_run_id\": \"label_only_seed123\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T08:58:35.632418+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.8706, \"n\": 1190, \"pass_recall\": 0.974, \"fail_recall\": 0.611, \"pass_f1\": 0.915, \"fail_f1\": 0.729}, \"completed_at\": \"2026-05-16T09:01:41.007Z\"}, \"ae_only_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T03:41:51.316Z\", \"updated_at\": \"2026-05-16T06:48:30.962Z\", \"hypothesis\": \"Seed robustness: ae_only with seed=456 on Qwen-2.5-Coder-7B. Verifies ae_only 99.92% is stable across seeds (Reviewer P0 requirement).\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition ae_only --gradient_checkpointing --gpu 0 --seed 456 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/ae_only_seed456 --wandb_project trace-verdict-study --wandb_run_name ae_only_seed456 && python eval/evaluate.py --condition ae_only --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/ae_only_seed456/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/ae_only_seed456/final/eval_results.json --save_predictions\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/ae_only_{train,test}.jsonl\", \"data_count\": 4720, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 456, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/ae_only_seed456/final\", \"log_path\": \"/tmp/ae_only_seed456.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T06:26:31.454Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T06:26:32.421Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T06:26:34.050811+00:00\"}]}, \"metrics\": {\"accuracy\": 0.9992, \"n\": 1190, \"majority_baseline\": 0.7151, \"lift\": 0.2841, \"seed_comparison\": {\"seed42_accuracy\": 0.9992, \"seed123_accuracy\": 0.9908, \"seed456_accuracy\": 0.9992, \"mean_accuracy\": 0.9964, \"std\": 0.0049, \"note\": \"2/3 seeds = 99.92%, seed123 = 99.08%. Mean = 99.64% ± 0.49\"}}}, \"ae_only_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T03:41:50.753Z\", \"updated_at\": \"2026-05-16T06:48:29.943Z\", \"hypothesis\": \"Seed robustness: ae_only with seed=123 on Qwen-2.5-Coder-7B. Verifies ae_only 99.92% is stable across seeds (Reviewer P0 requirement).\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition ae_only --gradient_checkpointing --gpu 0 --seed 123 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/ae_only_seed123 --wandb_project trace-verdict-study --wandb_run_name ae_only_seed123 && python eval/evaluate.py --condition ae_only --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/ae_only_seed123/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/ae_only_seed123/final/eval_results.json --save_predictions\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/ae_only_{train,test}.jsonl\", \"data_count\": 4720, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/ae_only_seed123\", \"log_path\": \"/tmp/ae_only_seed123.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T06:16:31.845Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T06:16:33.018Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T06:16:35.841653+00:00\"}]}, \"metrics\": {\"accuracy\": 0.9908, \"n\": 1190, \"pass_recall\": 0.987, \"fail_recall\": 1, \"majority_baseline\": 0.7151, \"lift\": 0.2757}, \"notes\": \"Cron 误判为 failed（进程死亡 5× 无 sentinel/W&B），Reviewer 独立核实训练+eval 均成功完成。accuracy=99.08% 低于 seed42/456 (99.92%)，ae_only 3-seed mean=99.64% ± 0.49。\"}, \"regex_baseline_analysis\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T03:43:17.799Z\", \"updated_at\": \"2026-05-16T04:08:29.402Z\", \"hypothesis\": \"Regex/heuristic baselines on exception_only test data. Tests if simple pattern matching can match SFT performance (Reviewer critical concern).\", \"conclusion\": \"success\", \"metrics\": {\"regex_B1_ERROR_presence\": 0.9345, \"regex_B2_Traceback\": 0.7151, \"regex_B3_any_keyword\": 0.9345, \"regex_B4_exception_type\": 0.9361, \"regex_B5_format_marker\": 0.9933, \"regex_B6_error_count_ge2\": 0.9202, \"sft_exception_only\": 0.9983, \"best_regex_gap_vs_sft\": -0.0622, \"B5_mcnemar_p\": 0.041, \"n\": 1190}, \"spec\": {\"checkpoint_path\": \"N/A (CPU analysis, no model)\", \"log_path\": \"N/A (CPU analysis)\"}, \"checkpoint_path\": \"N/A (analysis-only, no training)\", \"log_path\": \"N/A (analysis-only, no training)\", \"completed_at\": \"2026-05-16T04:08:09.296Z\"}, \"deepseek_vota_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:13:39.391Z\", \"updated_at\": \"2026-05-16T02:45:56.773Z\", \"hypothesis\": \"Multi-model validation: VOTA on DeepSeek-Coder-6.7B-Instruct (plan_004). Tests if VOTA's verdict accuracy advantage generalizes beyond Qwen2.5-Coder to DCSH's same base model.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition vota --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_vota --gradient_checkpointing --gpu 0 --seed 42 --wandb_project trace-verdict-study --wandb_run_name deepseek_vota_seed42 && python eval/evaluate.py --condition vota --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_vota/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_vota/final/eval_results.json\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"93484\", \"log_path\": \"~/runs/trace-verdict-study/deepseek_vota_seed42.log\", \"submitted_at\": \"2026-05-15T10:45:36.891Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/vota_{train,test}.jsonl\", \"data_count\": 4720, \"model_name\": \"deepseek-ai/deepseek-coder-6.7b-instruct\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_vota/final\", \"wall_clock_seconds\": 8839.9, \"gpu_hours\": 2.46}, \"reproduce\": {\"finished_at\": \"2026-05-15T13:06:46.525Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T13:06:47.175122+00:00\"}]}, \"metrics\": {\"accuracy\": 0.8445, \"majority_baseline\": 0.7151, \"lift\": 0.1294, \"accuracy_ci\": [0.826, 0.864], \"pass_precision\": 0.821, \"pass_recall\": 1, \"pass_f1\": 0.902, \"fail_precision\": 1, \"fail_recall\": 0.454, \"fail_f1\": 0.625, \"eval_loss_epoch1\": 0.0679, \"eval_loss_epoch2\": 0.095, \"eval_loss_epoch3\": 0.1121, \"final_train_loss\": 0.0522, \"epoch1_checkpoint_eval\": {\"accuracy\": 0.7815, \"accuracy_ci\": [0.76, 0.803], \"fail_recall\": 0.233, \"fail_precision\": 1, \"pass_recall\": 1, \"pass_precision\": 0.766, \"fail_f1\": 0.378, \"pass_f1\": 0.867, \"conclusion\": \"epoch3_final_is_better\"}, \"reeval_with_fixed_script\": {\"accuracy\": 0.16, \"accuracy_ci\": [0.139, 0.18], \"fail_f1\": 0.61, \"fail_precision\": 0.9, \"fail_recall\": 0.47, \"pass_f1\": 0.07, \"pass_precision\": 1, \"pass_recall\": 0.04, \"note\": \"CATASTROPHIC: re-eval with corrected evaluate.py shows 16% (vs original 84.45%). Model predicts fail for almost everything. Previous 84.45% may have been from buggy eval. NEEDS INVESTIGATION.\"}, \"group_analysis\": {\"train_truncated\": {\"n\": 1091, \"accuracy\": 0.8304, \"ci_95\": [0.8075, 0.8524], \"correct\": 906, \"incorrect\": 185, \"pass_accuracy\": 1, \"pass_n\": 822, \"fail_accuracy\": 0.3123, \"fail_n\": 269}, \"train_intact\": {\"n\": 99, \"accuracy\": 1, \"ci_95\": [1, 1], \"correct\": 99, \"incorrect\": 0, \"pass_accuracy\": 1, \"pass_n\": 29, \"fail_accuracy\": 1, \"fail_n\": 70}, \"fisher_exact\": {\"odds_ratio\": 0, \"p_value\": 0}, \"overall_accuracy\": 0.8445, \"max_length\": 2048, \"note\": \"Grouped by whether training sample content exceeded token budget (DeepSeek tokenizer, max_length=2048). Inference used full-length input (no truncation). All 185 errors from truncated group's fail class (fail_recall=31.2%). Intact group: 100% accuracy.\"}}, \"conclusion\": \"success\", \"log_path\": \"/root/runs/trace-verdict-study/deepseek_vota_seed42.log\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_vota/final\", \"completed_at\": \"2026-05-15T13:12:56.838Z\", \"notes\": \"DeepSeek VOTA: 84.45% confirmed with max_length=16384 (re-verified 2026-05-16, exact match). max_length=2048 gives 16% due to evaluate.py front-truncation removing \\\"Answer: \\\" suffix from 91.7% of inputs. Training-time eval used old script (no truncation). exception_only/no_trace unaffected (short inputs). Systematic audit 2026-05-16: adapter base_model=DeepSeek confirmed, no model mixup possible.\"}, \"deepseek_full_trace_seed42_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:40:07.877Z\", \"updated_at\": \"2026-05-16T02:37:10.773Z\", \"hypothesis\": \"DeepSeek full_trace v3: retrain with label-preserving truncation fix in to_chat_text(). v1/v2 collapsed due to DeepSeek tokenizer producing >2048 tokens → SFTTrainer right-truncated labels. Tests if full_trace shows intermediate performance on DeepSeek (plan_004, 4th condition).\", \"parent\": \"\", \"notes\": \"DeepSeek full_trace v3: label-preserving truncation fix. 79.16% confirmed with max_length=2048 (matches training). eval_results.json has stale 28.49% from max_length=16384 run; correct value in eval_results_maxlen2048.json. predictions.jsonl overwritten 2026-05-16 with maxlen2048 results (reliable). Systematic audit 2026-05-16 confirmed: adapter base_model=DeepSeek, no model mixup possible (dimension mismatch would crash).\", \"spec\": {\"command\": \"python train_sft.py --condition full_trace --model deepseek-coder-6.7b --max_length 2048 --seed 42\", \"server\": \"westd-11235\", \"data_path\": \"/root/trace-verdict-study/data\", \"data_count\": 5910, \"model_name\": \"deepseek-ai/deepseek-coder-6.7b-instruct\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace_seed42_v3\", \"log_path\": \"/root/trace-verdict-study/logs/deepseek_full_trace_seed42_v3\"}, \"gpu\": \"cuda:1\", \"metrics\": {\"accuracy\": 0.7916, \"majority_baseline\": 0.7151, \"lift\": 0.0765, \"n\": 1190, \"pass_precision\": 0.857, \"pass_recall\": 0.851, \"pass_f1\": 0.854, \"fail_precision\": 0.632, \"fail_recall\": 0.643, \"fail_f1\": 0.637, \"accuracy_ci\": [0.768, 0.813], \"train_loss\": 0.0547, \"train_runtime_seconds\": 8891, \"epochs\": 3, \"reeval_discrepancy\": {\"reeval_accuracy\": 0.285, \"reeval_note\": \"RESOLVED: 28.5% was caused by eval max_length=16384 (OOD). Re-eval with max_length=2048 reproduces 79.16%. predictions.jsonl updated to maxlen2048 results.\", \"status\": \"RESOLVED\"}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T23:27:54.219Z\", \"log_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace_seed42_v3.log\"}, \"eval_missing_predictions_batch_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:41:02.286Z\", \"updated_at\": \"2026-05-16T02:12:47.505Z\", \"spec\": {\"command\": \"bash run_missing_predictions.sh 1\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"221213\", \"log_path\": \"~/runs/trace-verdict-study/eval_missing_predictions_batch_v2.log\", \"submitted_at\": \"2026-05-16T01:41:02.047Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"deepseek_full_trace_v3 + debugbench_vota predictions\", \"data_count\": 1616, \"model_name\": \"DeepSeek-Coder-6.7B + Qwen-2.5-Coder-7B\", \"seed\": 42, \"wall_clock_seconds\": 1905.5, \"gpu_hours\": 0.53}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval-only batch)\", \"completed_at\": \"2026-05-16T02:12:47.505Z\"}, \"debugbench_vota_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T23:33:57.931Z\", \"updated_at\": \"2026-05-16T01:58:42.269Z\", \"spec\": {\"hypothesis\": \"plan_005: VOTA on DebugBench (bug detection). Tests if VOTA's structured trace analysis provides additional signal beyond exception_only on a logic-error-dominated benchmark.\", \"model_name\": \"Qwen/Qwen2.5-Coder-7B-Instruct\", \"seed\": 42, \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/debugbench_vota_{train,test}.jsonl\", \"data_count\": {\"train\": 1622, \"test\": 426}, \"plan_id\": \"plan_005\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && ... && python train/train_sft.py --condition debugbench_vota --gradient_checkpointing --gpu 0 --seed 42 --output_dir .../debugbench_vota --wandb_project trace-verdict-study --wandb_run_name debugbench_vota_seed42 && python eval/evaluate.py --condition debugbench_vota --checkpoint_dir .../debugbench_vota/final --gpu 0\\\"\", \"server\": \"westd-11235\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_vota\", \"log_path\": \"~/runs/trace-verdict-study/debugbench_vota_seed42.log\"}, \"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-16T00:01:37.634Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition debugbench_vota --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_vota --wandb_project trace-verdict-study --wandb_run_name debugbench_vota_seed42 && python eval/evaluate.py --condition debugbench_vota --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_vota/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_vota/final/eval_results.json\\\"\", \"wandb_run_id\": \"debugbench_vota_seed42\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\", \"finished_at\": \"2026-05-16T00:55:26.974Z\", \"training_hours\": 0.9}, \"pid\": \"211253\", \"log_path\": \"~/runs/trace-verdict-study/debugbench_vota_seed42.log\", \"wandb_run_id\": \"debugbench_vota_seed42\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T00:55:28.620314+00:00\"}]}, \"metrics\": {\"accuracy\": 0.9977, \"majority_baseline\": 0.5141, \"lift\": 0.4836, \"n\": 426, \"pass_precision\": 1, \"pass_recall\": 1, \"pass_f1\": 1, \"fail_precision\": 1, \"fail_recall\": 1, \"fail_f1\": 1, \"accuracy_ci\": [0.993, 1], \"train_loss\": 0.098, \"eval_loss\": 0.1179, \"eval_mean_token_accuracy\": 0.9737, \"errors\": 1}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T00:58:14.197Z\", \"notes\": \"predictions.jsonl generated (426 lines). Accuracy=99.77%, matches registry. Path: /root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_vota/final/predictions.jsonl\"}, \"eval_missing_predictions_batch\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:33:51.923Z\", \"updated_at\": \"2026-05-16T01:58:38.428Z\", \"spec\": {\"command\": \"python eval/evaluate.py --save_predictions\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"219832\", \"log_path\": \"~/runs/trace-verdict-study/eval_missing_predictions_batch.log\", \"submitted_at\": \"2026-05-16T01:33:51.795Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/\", \"data_count\": 1616, \"model_name\": \"DeepSeek-Coder-6.7B + Qwen2.5-Coder-7B\", \"seed\": 42, \"wall_clock_seconds\": 1480.2, \"gpu_hours\": 0.41}, \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"/tmp/deepseek_eval_preds.log, /tmp/debugbench_vota_eval_preds.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T01:58:31.993Z\", \"notes\": \"predictions.jsonl generated for both experiments. deepseek_full_trace_seed42_v3: 1190 lines, accuracy=28.5% (NOT 79.16% as expected — model predicts all fail, same result with max_length=16384). debugbench_vota_seed42: 426 lines, accuracy=99.77% (matches registry). Paths: /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace_seed42_v3/final/predictions.jsonl, /root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_vota/final/predictions.jsonl\"}, \"debugbench_exception_only_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T23:33:52.790Z\", \"updated_at\": \"2026-05-16T01:35:56.671Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition debugbench_exception_only --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_exception_only --wandb_project trace-verdict-study --wandb_run_name debugbench_exception_only_seed42 && python eval/evaluate.py --condition debugbench_exception_only --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_exception_only/final --gpu 0 --save_predictions --output /root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_exception_only/final/eval_results.json\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"216806\", \"log_path\": \"~/runs/trace-verdict-study/debugbench_exception_only_seed42.log\", \"submitted_at\": \"2026-05-16T01:11:57.937Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1255.3, \"gpu_hours\": 0.35}, \"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"pid\": \"216806\", \"log_path\": \"~/runs/trace-verdict-study/debugbench_exception_only_seed42.log\", \"wandb_run_id\": \"debugbench_exception_only_seed42\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition debugbench_exception_only --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_exception_only --wandb_project trace-verdict-study --wandb_run_name debugbench_exception_only_seed42 && python eval/evaluate.py --condition debugbench_exception_only --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_exception_only/final --gpu 0 --save_predictions --output /root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_exception_only/final/eval_results.json\\\"\", \"wandb_run_id\": \"debugbench_exception_only_seed42\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\", \"finished_at\": \"2026-05-16T01:27:40.798Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T01:27:43.171585+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 1, \"majority_baseline\": 0.5141, \"lift\": 0.4859, \"n\": 426, \"pass_precision\": 1, \"pass_recall\": 1, \"pass_f1\": 1, \"fail_precision\": 1, \"fail_recall\": 1, \"fail_f1\": 1, \"accuracy_ci_wilson\": [0.9914, 1], \"accuracy_ci_bootstrap\": [1, 1], \"train_loss\": 0.2435, \"eval_loss\": 0.4157, \"train_runtime_sec\": 837}, \"notes\": \"100.0% accuracy (426/426 完美预测)。exception_only 在 DebugBench 上超越 VOTA (99.77%) 和 no_trace (96.71%)。Checkpoint: /root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_exception_only/final/。Predictions: predictions.jsonl (426条)。\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_exception_only/final/\", \"completed_at\": \"2026-05-16T01:32:53.272Z\", \"predictions_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_exception_only/final/predictions.jsonl\"}, \"deepseek_exception_only_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:19:31.586Z\", \"updated_at\": \"2026-05-16T01:16:41.387Z\", \"hypothesis\": \"Cross-model seed robustness: exception_only seed=456 on DeepSeek-Coder-6.7B. Third seed to determine if seed42 (99.83%) is outlier or seed123 (91.09%) is outlier.\", \"parent\": \"deepseek_exception_only_seed123\", \"spec\": {\"command\": \"python train/train_sft.py --condition exception_only --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_exception_only_seed456 --gradient_checkpointing --gpu 0 --seed 456 --wandb_project trace-verdict-study --wandb_run_name deepseek_exception_only_seed456\", \"server\": \"westd-11235\", \"model_name\": \"deepseek-ai/deepseek-coder-6.7b-instruct\", \"seed\": 456, \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/exception_only_{train,test}.jsonl\", \"data_count\": 4720, \"checkpoint_source\": \"N/A - training run\", \"eval_data\": \"N/A - training run\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T22:08:34.111Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T22:08:35.359157+00:00\"}]}, \"metrics\": {\"accuracy\": 0.9933, \"majority_baseline\": 0.7151, \"lift\": 0.2782, \"n\": 1190, \"pass_precision\": 1, \"pass_recall\": 0.9906, \"pass_f1\": 0.9953, \"fail_precision\": 0.9769, \"fail_recall\": 1, \"fail_f1\": 0.9883, \"accuracy_ci\": [0.9882, 0.9975], \"train_loss\": 0.1225, \"eval_loss\": 0.4824, \"train_runtime_sec\": 6246, \"seed_comparison\": {\"seed42_accuracy\": 0.9933, \"seed456_accuracy\": 0.9933, \"seed123_accuracy\": 0.9109, \"note\": \"seed42 and seed456 identical (99.33%); seed123 outlier (91.09%). 2/3 seeds robust.\"}, \"epoch1_checkpoint_eval\": {\"accuracy\": 0.993, \"accuracy_ci\": [0.988, 0.997], \"fail_f1\": 0.99, \"fail_precision\": 0.98, \"fail_recall\": 1, \"pass_f1\": 1, \"pass_precision\": 1, \"pass_recall\": 0.99, \"conclusion\": \"epoch1 (99.3%) ≈ epoch3 (99.33%), 1 epoch convergence confirmed\"}}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_exception_only_seed456/final\", \"log_path\": \"/root/runs/trace-verdict-study/deepseek_exception_only_seed456.log\", \"conclusion\": \"success\", \"notes\": \"seed456 accuracy 99.33% = seed42 99.33%（完全一致）。seed123 (91.09%) 是离群值——2/3 seeds 在 DeepSeek 上稳定。Epoch1 checkpoint (checkpoint-148) 可用于 epoch1 eval。Eval 由 on_complete hook 的 eval 脚本 (PID 166680) 自动运行，结果写入 final/eval_results.json。\", \"completed_at\": \"2026-05-15T22:13:38.554Z\", \"outputs\": {\"predictions_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_exception_only_seed456/checkpoint-148/predictions.jsonl\"}}, \"deepseek_exception_only_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:17:07.674Z\", \"updated_at\": \"2026-05-16T01:16:38.239Z\", \"hypothesis\": \"Multi-model validation: exception_only on DeepSeek-Coder-6.7B-Instruct (plan_004). Tests if exception dominance (99.83% on Qwen) generalizes across models — the most valuable cross-model evidence.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition exception_only --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_exception_only --gradient_checkpointing --gpu 0 --seed 42 --wandb_project trace-verdict-study --wandb_run_name deepseek_exception_only_seed42 && python eval/evaluate.py --condition exception_only --model_path /root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_exception_only/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_exception_only/final/eval_results.json\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"107188\", \"log_path\": \"~/runs/trace-verdict-study/deepseek_exception_only_seed42.log\", \"submitted_at\": \"2026-05-15T13:10:32.405Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/exception_only_{train,test}.jsonl\", \"data_count\": 4720, \"model_name\": \"deepseek-ai/deepseek-coder-6.7b-instruct\", \"seed\": 42, \"wall_clock_seconds\": 7358.8, \"gpu_hours\": 2.04}, \"reproduce\": {\"finished_at\": \"2026-05-15T15:06:51.643Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T15:06:52.877301+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_exception_only/final\", \"metrics\": {\"accuracy\": 0.9933, \"majority_baseline\": 0.7151, \"lift\": 0.2782, \"n\": 1190, \"pass_precision\": 1, \"pass_recall\": 0.9906, \"pass_f1\": 0.9953, \"fail_precision\": 0.9769, \"fail_recall\": 1, \"fail_f1\": 0.9883, \"epoch1_checkpoint_eval\": {\"accuracy\": 0.9983, \"fail_recall\": 1, \"fail_precision\": 0.9941, \"pass_recall\": 0.9976, \"conclusion\": \"epoch1_better_by_0.50pp\"}}, \"completed_at\": \"2026-05-15T15:13:11.215Z\", \"notes\": \"epoch 1 (step 148) accuracy = 99.83%，高于 final (epoch 3) 的 99.33%。eval_loss epoch 2→3 从 0.413 涨到 0.476 (+15%)。continued training 导致 token-level 过拟合，verdict accuracy 从 99.83% 降到 99.33% (-0.50pp)。这是 eval_loss/accuracy 解耦的又一例证——但此处 eval_loss 上升确实伴随 accuracy 下降，与 DeepSeek VOTA 的趋势相反。Epoch 1 的 99.83% 与 Qwen exception_only (99.83%) 完全一致——跨模型 gap = 0pp（在最佳 checkpoint 下）。\", \"outputs\": {\"predictions_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_exception_only/checkpoint-148/predictions.jsonl\"}}, \"debugbench_no_trace_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T23:33:55.756Z\", \"updated_at\": \"2026-05-16T01:12:05.904Z\", \"spec\": {\"hypothesis\": \"plan_005: No-trace baseline on DebugBench. Establishes baseline for VOTA/exception_only comparison on bug detection task.\", \"model_name\": \"Qwen/Qwen2.5-Coder-7B-Instruct\", \"seed\": 42, \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/debugbench_no_trace_{train,test}.jsonl\", \"data_count\": {\"train\": 1622, \"test\": 426}, \"plan_id\": \"plan_005\", \"server\": \"westd-11235\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_no_trace\", \"log_path\": \"~/runs/trace-verdict-study/debugbench_no_trace_seed42.log\"}, \"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-16T00:58:18.036Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition debugbench_no_trace --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_no_trace --wandb_project trace-verdict-study --wandb_run_name debugbench_no_trace_seed42 && python eval/evaluate.py --condition debugbench_no_trace --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_no_trace/final --gpu 0 --save_predictions --output /root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_no_trace/final/eval_results.json\\\"\", \"wandb_run_id\": \"debugbench_no_trace_seed42\", \"code_commit\": \"e404237ccc765768e267d4d6fd3c89549dcf41a4\", \"finished_at\": \"2026-05-16T01:09:14.222Z\", \"training_hours\": 0.18}, \"pid\": \"215223\", \"log_path\": \"~/runs/trace-verdict-study/debugbench_no_trace_seed42.log\", \"wandb_run_id\": \"debugbench_no_trace_seed42\", \"gpu_id\": \"cuda:1\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T01:09:16.070113+00:00\"}]}, \"metrics\": {\"accuracy\": 0.9671, \"majority_baseline\": 0.5141, \"lift\": 0.4531, \"pass_precision\": 1, \"pass_recall\": 0.936, \"pass_f1\": 0.967, \"fail_precision\": 0.937, \"fail_recall\": 1, \"fail_f1\": 0.967, \"accuracy_ci\": [0.948, 0.984], \"train_loss\": 0.249, \"eval_loss\": 0.532}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T01:12:05.904Z\"}, \"debugbench_exception_bug_fix\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T23:14:24.382Z\", \"updated_at\": \"2026-05-15T23:26:16.029Z\", \"spec\": {\"command\": \"python data/debugbench_format_data.py\", \"server\": \"westd-11235\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/debugbench/raw_traces.jsonl\", \"data_count\": 2048, \"model_name\": \"data_processing\", \"seed\": 42, \"checkpoint_path\": \"/root/trace-verdict-study/data/debugbench_format_data.py\", \"log_path\": \"/tmp/debugbench_format.log\"}, \"conclusion\": \"success\", \"hypothesis\": \"BUG FIX: compress_exception_only() only checked trace_raw events, missing 625/1006 empty-trace fails (syntax errors) + 5 event-capped samples. Fix: fallback to test_results.error. Exception signal 376→1006/1006, upper bound 69.2%→100%. DebugBench 30.5% empty trace rate confirmed.\", \"completed_at\": \"2026-05-15T23:26:16.029Z\"}, \"vota_seed456_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:39:05.494Z\", \"updated_at\": \"2026-05-15T21:04:28.008Z\", \"hypothesis\": \"Seed robustness: VOTA with seed=456, retry with --gradient_checkpointing (v1 OOM). Verifies VOTA 99.2% accuracy stable across seeds.\", \"notes\": \"Auto-retried from vota_seed456 (OOM). PID 146592, cuda:1, --gradient_checkpointing enabled. Started 18:31 UTC, ~2h to complete. Low priority per Director (VOTA not primary claim).\", \"parent\": \"vota_seed456\", \"spec\": {\"command\": \"python train/train_sft.py --condition vota --gradient_checkpointing --gpu 0 --seed 456 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/vota_seed456 --wandb_project trace-verdict-study --wandb_run_name vota_seed456_v2\", \"server\": \"westd-11235\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/vota_{train,test}.jsonl\", \"data_count\": 4720, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 456, \"checkpoint_source\": \"N/A (training, not eval)\", \"eval_data\": \"N/A (training, not eval)\"}, \"metrics\": {\"accuracy\": 0.9908, \"pass_precision\": 1, \"pass_recall\": 0.987, \"pass_f1\": 0.993, \"fail_precision\": 0.969, \"fail_recall\": 1, \"fail_f1\": 0.984, \"ci_95\": [0.985, 0.996]}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/vota_seed456/final\", \"log_path\": \"/root/runs/trace-verdict-study/vota_seed456.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T21:04:28.008Z\"}, \"exception_only_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:31:01.555Z\", \"updated_at\": \"2026-05-15T18:03:37.166Z\", \"spec\": {\"plan_id\": \"plan_008a\", \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 123, \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/exception_only_{train,test}.jsonl\", \"data_count\": 4720, \"server\": \"westd-11235\"}, \"hypothesis\": \"Seed robustness: exception_only with seed=123 on Qwen-2.5-Coder-7B (plan_008). Verifies headline result 99.83% is stable across seeds.\", \"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-11235\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-15T15:54:06.157Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition exception_only --gradient_checkpointing --gpu 0 --seed 123 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_seed123 --wandb_project trace-verdict-study --wandb_run_name exception_only_seed123 && python eval/evaluate.py --condition exception_only --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_seed123/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_seed123/final/eval_results.json\\\"\", \"wandb_run_id\": \"exception_only_seed123\", \"finished_at\": \"2026-05-15T18:00:50.835Z\", \"training_hours\": 2.11}, \"pid\": \"124197\", \"log_path\": \"~/runs/trace-verdict-study/exception_only_seed123.log\", \"wandb_run_id\": \"exception_only_seed123\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T18:00:52.169672+00:00\"}]}, \"notes\": \"Seed robustness 结论: exception_only 99.83% ± 0.00 (seeds 42/123/456), 每 seed 恰好 2/1190 errors。极大概率同一组 irreducible 样本。\", \"metrics\": {\"accuracy\": 0.9983, \"accuracy_ci\": [0.9958, 1], \"majority_baseline\": 0.7151, \"lift\": 0.2832, \"n\": 1190, \"pass_precision\": 1, \"pass_recall\": 0.9976, \"pass_f1\": 0.9988, \"fail_precision\": 0.9941, \"fail_recall\": 1, \"fail_f1\": 0.9971, \"train_loss\": 0.1096, \"train_runtime_sec\": 7507, \"epochs\": 3, \"seed_comparison\": {\"seed42_accuracy\": 0.9983, \"seed456_accuracy\": 0.9983, \"seed123_accuracy\": 0.9983, \"max_diff\": 0, \"note\": \"identical accuracy to 4 decimal places across all 3 seeds (42/456/123); each has exactly 2/1190 errors; exception_only fully seed-robust\"}}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_seed123/final\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T18:03:37.166Z\"}, \"exception_only_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:31:02.005Z\", \"updated_at\": \"2026-05-15T18:02:52.070Z\", \"spec\": {\"plan_id\": \"plan_008a\", \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 456, \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/exception_only_{train,test}.jsonl\", \"data_count\": 4720, \"server\": \"westd-11235\"}, \"hypothesis\": \"Seed robustness: exception_only with seed=456 on Qwen-2.5-Coder-7B (plan_008). Verifies headline result 99.83% is stable across seeds.\", \"server\": \"westd-11235\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-11235\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-15T16:38:44.142Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition exception_only --gradient_checkpointing --gpu 0 --seed 456 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_seed456 --wandb_project trace-verdict-study --wandb_run_name exception_only_seed456 && python eval/evaluate.py --condition exception_only --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_seed456/final --gpu 0 --output /root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_seed456/final/eval_results.json\\\"\", \"wandb_run_id\": \"exception_only_seed456\", \"finished_at\": \"2026-05-15T17:56:16.196Z\", \"training_hours\": 1.29}, \"pid\": \"129476\", \"log_path\": \"~/runs/trace-verdict-study/exception_only_seed456.log\", \"wandb_run_id\": \"exception_only_seed456\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:56:17.874949+00:00\"}]}, \"metrics\": {\"accuracy\": 0.9983, \"accuracy_ci\": [0.9958, 1], \"majority_baseline\": 0.7151, \"lift\": 0.2832, \"n\": 1190, \"pass_precision\": 1, \"pass_recall\": 0.9976, \"pass_f1\": 0.9988, \"fail_precision\": 0.9941, \"fail_recall\": 1, \"fail_f1\": 0.9971, \"vs_seed42\": {\"seed42_accuracy\": 0.9983, \"seed456_accuracy\": 0.9983, \"diff\": 0, \"note\": \"identical accuracy to 4 decimal places; no predictions.jsonl for paired bootstrap\"}, \"train_loss\": 0.1087, \"eval_loss\": 0.4629, \"train_runtime_sec\": 4541, \"epochs\": 3}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_seed456/final\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T17:58:25.389Z\", \"notes\": \"Seed robustness 结论: exception_only 99.83% ± 0.00 (seeds 42/123/456), 每 seed 恰好 2/1190 errors。极大概率同一组 irreducible 样本。\"}, \"vota_exception_only_seed42_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:16:14.602Z\", \"updated_at\": \"2026-05-15T18:02:36.534Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition exception_only --gradient_checkpointing --gpu 1 --seed 42 --wandb_project trace-verdict-study --wandb_run_name vota_exception_only_seed42_v2 && python eval/evaluate.py --condition exception_only --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/exception_only/final --gpu 1 --output /root/autodl-tmp/trace-verdict-study-checkpoints/exception_only/final/eval_results.json\\\"\", \"server\": \"westd-11235\", \"data_path\": \"exception_only\", \"data_count\": 4720, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 42, \"pid\": \"79633\", \"gpu\": [\"cuda:1\"], \"submitted_at\": \"2026-05-15T15:15:14Z\", \"log_path\": \"~/runs/trace-verdict-study/vota_exception_only_seed42_v2.log\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/exception_only/final\"}, \"hypothesis\": \"VOTA component ablation: exception_only condition — retry with --gradient_checkpointing (v1 OOM at step 8). Tests if [ERROR] events are the primary driver of VOTA's 99.2% accuracy (plan_003 sub-b)\", \"metrics\": {\"accuracy\": 0.9983, \"majority_baseline\": 0.7151, \"lift\": 0.2832, \"n\": 1190, \"pass_precision\": 1, \"pass_recall\": 0.998, \"pass_f1\": 0.999, \"fail_precision\": 0.994, \"fail_recall\": 1, \"fail_f1\": 0.997, \"lift_vs_notrace\": 0.2471, \"lift_vs_notrace_ci_lower\": 0.2227, \"lift_vs_notrace_ci_upper\": 0.2714, \"lift_vs_fulltrace\": 0.1807, \"lift_vs_fulltrace_ci_lower\": 0.1588, \"lift_vs_fulltrace_ci_upper\": 0.2034, \"lift_vs_vota\": 0.0067, \"lift_vs_vota_ci_lower\": 0.0017, \"lift_vs_vota_ci_upper\": 0.0126, \"lift_vs_vota_pvalue\": 0.01}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T09:35:01.676Z\", \"notes\": \"Seed robustness confirmed: exception_only 99.83% ± 0.00 across seeds 42/123/456. Each seed has exactly 2/1190 errors. High probability same irreducible samples. [re-eval] 修复后 evaluate.py 重跑 Δ=0。\"}, \"full_trace_label_only_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T04:01:29.625Z\", \"updated_at\": \"2026-05-15T16:36:05.917Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_label_only/final\", \"log_path\": \"~/runs/trace-verdict-study/full_trace_label_only_seed42.log\"}, \"hypothesis\": \"Label-only loss on full_trace fixes gradient dilution collapse (plan_002: loss only on pass/fail token, not trace tokens)\", \"reproduce\": {\"finished_at\": \"2026-05-15T07:15:28.991Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T07:15:30.057513+00:00\"}]}, \"metrics\": {\"accuracy\": 0.8622, \"accuracy_ci_lower\": 0.8437, \"accuracy_ci_upper\": 0.8807, \"majority_baseline\": 0.7151, \"lift\": 0.1471, \"n\": 1190, \"pass_precision\": 0.8821, \"pass_recall\": 0.9318, \"pass_f1\": 0.9063, \"fail_precision\": 0.8007, \"fail_recall\": 0.6873, \"fail_f1\": 0.7397, \"train_loss\": 0.2505, \"eval_loss\": 0.3205, \"lift_vs_notrace\": 0.1109, \"lift_vs_notrace_ci_lower\": 0.0849, \"lift_vs_notrace_ci_upper\": 0.137, \"lift_vs_standard_fulltrace\": 0.0445, \"lift_vs_standard_fulltrace_ci_lower\": 0.0235, \"lift_vs_standard_fulltrace_ci_upper\": 0.0655, \"lift_vs_standard_fulltrace_pvalue\": 0}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T07:23:57.111Z\", \"notes\": \"Label-only loss 将 full_trace 从 81.8% 提升到 86.2% (+4.4pp)，确认 gradient dilution 是 full_trace 性能受限的部分原因。但 86.2% vs VOTA 99.2% 仍有 13pp gap，说明 gradient dilution 只是部分解释——trace 信息密度（VOTA 的 decision-relevant compression）才是主因。[2026-05-15 re-eval] 用修复后 evaluate.py + --condition full_trace 重跑，accuracy 不变 (86.22% → 86.22%, Δ=0)，predictions.jsonl 1190行已生成。训练确认使用 full_trace 格式数据，label_only 仅改变 loss mask。\"}, \"vota_no_ae_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T04:21:27.279Z\", \"updated_at\": \"2026-05-15T16:25:20.610Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition vota_no_ae --gpu 1 --seed 42 --wandb_project trace-verdict-study --wandb_run_name vota_no_ae_seed42\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"953133\", \"log_path\": \"~/runs/trace-verdict-study/vota_no_ae_seed42.log\", \"submitted_at\": \"2026-05-15T04:21:27.215Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/vota_no_ae_train.jsonl\", \"data_count\": 4720, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/vota_no_ae/final\", \"wall_clock_seconds\": 6902.4, \"gpu_hours\": 1.92}, \"hypothesis\": \"VOTA without actual/expected values: tests if VOTA's accuracy comes from genuine behavioral understanding vs trivial string comparison (plan_001)\", \"reproduce\": {\"finished_at\": \"2026-05-15T06:10:18.839Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T06:10:19.847891+00:00\"}]}, \"metrics\": {\"accuracy\": 0.994, \"majority_baseline\": 0.7151, \"lift\": 0.279, \"n\": 1190, \"pass_f1\": 0.996, \"fail_f1\": 0.989, \"accuracy_ci_lower\": 0.989, \"accuracy_ci_upper\": 0.998, \"lift_vs_notrace\": 0.243, \"lift_vs_notrace_ci_lower\": 0.218, \"lift_vs_notrace_ci_upper\": 0.268, \"train_loss\": 0.0908, \"eval_loss\": 0.2215, \"wall_clock_seconds\": 6397.88}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T06:16:29.587Z\", \"notes\": \"✅ Eval verified: accuracy 99.4% [98.9, 99.8] confirmed by evaluate.py + bootstrap. 去掉 actual/expected 后性能不降（vs VOTA v5 99.2%），证明 VOTA 效果来自 trace 行为模式理解而非 trivial string comparison。Claim 1 走 full positive framing。[2026-05-15 re-eval] 用修复后 evaluate.py 重跑，accuracy 不变 (99.41% → 99.41%, Δ=0)，predictions.jsonl 1190行已生成。\"}, \"vota_loop_only_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:02:41.201Z\", \"updated_at\": \"2026-05-15T16:25:16.352Z\", \"hypothesis\": \"VOTA component ablation: loop_only condition — only loop compression summaries, no actual/expected or exception. Tests loop behavioral pattern contribution to VOTA 99.2% accuracy (plan_003 sub-c)\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition loop_only --gradient_checkpointing --gpu 0 --seed 42 --wandb_project trace-verdict-study --wandb_run_name vota_loop_only_seed42 && python eval/evaluate.py --condition loop_only --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/loop_only/final --gpu 0\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:0\"], \"pid\": \"82362\", \"log_path\": \"~/runs/trace-verdict-study/vota_loop_only_seed42.log\", \"submitted_at\": \"2026-05-15T07:58:06.023Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/loop_only_{train,test}.jsonl\", \"data_count\": 4720, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 42, \"wall_clock_seconds\": 7952.5, \"gpu_hours\": 2.21}, \"reproduce\": {\"finished_at\": \"2026-05-15T10:04:53.052Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T10:04:54.341040+00:00\"}]}, \"metrics\": {\"accuracy\": 0.8563, \"majority_baseline\": 0.7151, \"lift\": 0.1412, \"n\": 1190, \"pass_precision\": 0.9239, \"pass_recall\": 0.8707, \"pass_f1\": 0.8966, \"fail_precision\": 0.7165, \"fail_recall\": 0.8201, \"fail_f1\": 0.7648, \"accuracy_ci\": [0.8353, 0.8756], \"bootstrap_vs_no_trace\": {\"diff\": 0.105, \"ci\": [0.0824, 0.1286], \"significant\": true}, \"bootstrap_vs_vota\": {\"diff\": -0.1378, \"ci\": [-0.1571, -0.1185], \"significant\": true}, \"bootstrap_vs_full_trace\": {\"diff\": 0.0387, \"ci\": [0.0185, 0.0597], \"significant\": true}, \"train_loss\": 0.0718, \"wall_clock_seconds\": 7425.65}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/loop_only/final/\", \"log_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/loop_only/final/eval_results.json\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T10:10:38.549Z\", \"notes\": \"[2026-05-15 re-eval] 用修复后 evaluate.py 重跑，accuracy 不变 (85.63% → 85.63%, Δ=0)，predictions.jsonl 1190行已生成。\"}, \"vota_ae_only_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:11:44.999Z\", \"updated_at\": \"2026-05-15T16:25:14.973Z\", \"hypothesis\": \"VOTA component ablation: ae_only condition — only actual/expected values, no exception/loop compression (plan_003 sub-a)\", \"notes\": \"ae_only accuracy 99.92% [99.75%, 100%]。与 exception_only (99.83%) 统计等价，均为 Tier 1 diagnostic-moment signals。88% 样本含 fallback locals 行（无信息量的模块命名空间导入），85% 样本含 [ASSERT] 行的 actual/expected 对比（合法诊断信息）。Reviewer 核实 fallback locals 不含 verdict 信号，不构成 data leakage（D013 裁定）。Train: 3 epochs, 444 steps, final train_loss=0.022, eval_loss=0.166, eval_token_acc=96.76%。[2026-05-15 re-eval] 用修复后 evaluate.py 重跑，accuracy 不变 (99.92% → 99.92%, Δ=0)，predictions.jsonl 1190行已生成。\", \"spec\": {\"command\": \"python train/train_sft.py --condition ae_only --gradient_checkpointing --gpu 1 --seed 42 --wandb_project trace-verdict-study --wandb_run_name vota_ae_only_seed42 && python eval/evaluate.py --condition ae_only --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/ae_only/final --gpu 1 --output /root/autodl-tmp/trace-verdict-study-checkpoints/ae_only/final/eval_results.json\", \"server\": \"westd-11235\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/ae_only_train.jsonl\", \"data_count\": 4720, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 42}, \"reproduce\": {\"finished_at\": \"2026-05-15T12:13:36.539Z\"}, \"failure_reason\": \"N/A — cron 误判。实际已完成，eval_results.json 已生成。process dead 5x 是因为训练+eval 正常结束后进程退出，cron 无 W&B/sentinel 检测通道。\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T12:13:36.813Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T12:13:37.756005+00:00\"}]}, \"metrics\": {\"accuracy\": 0.9992, \"accuracy_ci\": [0.9975, 1], \"bootstrap_pairwise\": {\"ae_only_vs_no_trace\": {\"diff\": 0.2479, \"ci\": [0.2235, 0.2731], \"p_value\": 0, \"significant\": true}, \"ae_only_vs_exception_only\": {\"diff\": 0.0008, \"ci\": [-0.0017, 0.0034], \"p_value\": 0.8002, \"significant\": false}, \"ae_only_vs_vota\": {\"diff\": 0.005, \"ci\": [0.0017, 0.0092], \"p_value\": 0.0046, \"significant\": true}}, \"config\": {\"n_bootstrap\": 10000, \"seed\": 42, \"method\": \"paired_bootstrap\"}}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/ae_only/final\", \"log_path\": \"~/runs/trace-verdict-study/vota_ae_only_seed42.log\"}, \"full_trace_seed42_v5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T01:46:03.068Z\", \"updated_at\": \"2026-05-15T15:50:39.179Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/full_trace/final/\", \"log_path\": \"~/runs/trace-verdict-study/full_trace_seed42_v5.log\", \"wall_clock_seconds\": 7852, \"gpu_hours\": 2.18}, \"hypothesis\": \"Full execution trace with chat-template-aware truncation provides verdict accuracy lift vs no-trace baseline (v5: fixed chat template overhead)\", \"reproduce\": {\"finished_at\": \"2026-05-15T03:58:14.030Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T03:58:14.897249+00:00\"}]}, \"metrics\": {\"accuracy\": 0.8176, \"majority_baseline\": 0.7151, \"lift\": 0.1025, \"n\": 1190, \"pass_precision\": 0.8774, \"pass_recall\": 0.866, \"pass_f1\": 0.8717, \"fail_precision\": 0.6743, \"fail_recall\": 0.6962, \"fail_f1\": 0.6851, \"accuracy_ci_lower\": 0.797, \"accuracy_ci_upper\": 0.839, \"lift_vs_notrace\": 0.0664, \"lift_vs_notrace_ci_lower\": 0.0437, \"lift_vs_notrace_ci_upper\": 0.0899, \"train_loss\": 0.05, \"eval_loss\": 0.0867, \"wall_clock_seconds\": 7852, \"epoch_level\": {\"epoch1_accuracy\": 0.8303, \"epoch2_accuracy\": 0.763, \"final_accuracy\": 0.8176, \"trend\": \"non_monotonic_epoch1_best_epoch2_collapse\"}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T04:06:20.880Z\", \"notes\": \"✅ Paired bootstrap CI (2026-05-15): lift vs no_trace = +6.6pp [4.4, 9.0]pp (significant, N=10000). lift_ci in registry [7.4, 13.2] was vs majority, not vs no_trace — now corrected.\"}, \"no_trace_seed42_v5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T01:46:17.948Z\", \"updated_at\": \"2026-05-15T15:50:35.449Z\", \"hypothesis\": \"Baseline: verdict accuracy without execution trace (v5: same code version as vota_v5/full_trace_v5 for fair comparison)\", \"conclusion\": \"success\", \"spec\": {\"command\": \"python train/train_sft.py --condition no_trace --gpu 1 --seed 42 --wandb_project trace-verdict-study --wandb_run_name no_trace_seed42_v5\", \"server\": \"westd-11235\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/no_trace_train.jsonl\", \"data_count\": 4720, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/no_trace/final\", \"log_path\": \"~/runs/trace-verdict-study/no_trace_seed42_v5.log\"}, \"completed_at\": \"2026-05-15T06:45:11.265Z\", \"metrics\": {\"accuracy\": 0.7513, \"accuracy_ci_lower\": 0.7277, \"accuracy_ci_upper\": 0.7748, \"majority_baseline\": 0.7151, \"lift\": 0.0361, \"lift_ci_lower\": 0.0042, \"lift_ci_upper\": 0.0706, \"n\": 1190, \"pass_precision\": 0.8776, \"pass_recall\": 0.7579, \"pass_f1\": 0.8134, \"fail_precision\": 0.5473, \"fail_recall\": 0.7345, \"fail_f1\": 0.6272, \"epoch_level\": {\"epoch1_accuracy\": 0.7429, \"epoch2_accuracy\": 0.763, \"final_accuracy\": 0.7513, \"trend\": \"non_monotonic_epoch2_best\"}}}, \"vota_seed42_v5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T01:46:04.015Z\", \"updated_at\": \"2026-05-15T15:50:32.123Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/trace-verdict-study && python train/train_sft.py --condition vota --gpu 1 --wandb_project trace-verdict-study --wandb_run_name vota_seed42_v5\\\"\", \"server\": \"westd-11235\", \"gpu\": [\"cuda:1\"], \"pid\": \"940786\", \"log_path\": \"~/runs/trace-verdict-study/vota_seed42_v5.log\", \"submitted_at\": \"2026-05-15T01:46:03.990Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/vota_train.jsonl\", \"data_count\": 4720, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/vota/final/\", \"wall_clock_seconds\": 8443, \"gpu_hours\": 2.35}, \"hypothesis\": \"VOTA trace provides verdict accuracy lift over no-trace baseline (v5: fixed chat template overhead, all labels preserved)\", \"reproduce\": {\"finished_at\": \"2026-05-15T04:08:40.446Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T04:08:41.358997+00:00\"}]}, \"metrics\": {\"accuracy\": 0.9941, \"majority_baseline\": 0.7151, \"lift\": 0.279, \"n\": 1190, \"pass_precision\": 1, \"pass_recall\": 0.9882, \"pass_f1\": 0.9941, \"fail_precision\": 0.9714, \"fail_recall\": 1, \"fail_f1\": 0.9855, \"lift_vs_notrace\": 0.2428, \"lift_vs_notrace_ci_lower\": 0.2185, \"lift_vs_notrace_ci_upper\": 0.2681, \"accuracy_ci_lower\": 0.9882, \"accuracy_ci_upper\": 0.9983, \"train_loss\": 0.05, \"eval_loss\": 0.0867, \"eval_mean_token_accuracy\": 0.9828, \"wall_clock_seconds\": 8443, \"epoch_level\": {\"epoch1_accuracy\": 0.9933, \"epoch2_accuracy\": 0.9941, \"final_accuracy\": 0.9941, \"trend\": \"monotonic_increasing_then_stable\"}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T04:21:27.059Z\"}, \"calibration_analysis_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T12:27:04.073Z\", \"updated_at\": \"2026-05-15T13:09:52.711Z\", \"spec\": {\"plan_id\": \"plan_007\", \"command\": \"python eval/calibration_analysis.py\", \"server\": \"westd-11235\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/\", \"data_count\": 1190, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 42}, \"hypothesis\": \"Calibration analysis: ECE + reliability diagrams for VOTA/exception_only/full_trace/no_trace. Tests whether VOTA's compressed traces improve model calibration beyond accuracy (plan_007).\", \"conclusion\": \"success\", \"metrics\": {\"no_trace\": {\"ece\": 0.171476, \"mce\": 0.475643, \"brier_score\": 0.197152, \"accuracy\": 0.751261, \"n_samples\": 1190}, \"full_trace\": {\"ece\": 0.095817, \"mce\": 0.249061, \"brier_score\": 0.143924, \"accuracy\": 0.817647, \"n_samples\": 1190}, \"label_only\": {\"ece\": 0.110686, \"mce\": 0.417124, \"brier_score\": 0.120144, \"accuracy\": 0.862185, \"n_samples\": 1190}, \"loop_only\": {\"ece\": 0.083085, \"mce\": 0.183406, \"brier_score\": 0.118335, \"accuracy\": 0.856303, \"n_samples\": 1190}, \"ae_only\": {\"ece\": 0.000415, \"mce\": 0.000415, \"brier_score\": 0.000847, \"accuracy\": 0.99916, \"n_samples\": 1190}, \"exception_only\": {\"ece\": 0.002717, \"mce\": 0.835484, \"brier_score\": 0.001311, \"accuracy\": 0.998319, \"n_samples\": 1190}, \"vota\": {\"ece\": 0.00541, \"mce\": 0.622459, \"brier_score\": 0.005234, \"accuracy\": 0.994118, \"n_samples\": 1190}}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/calibration/\", \"log_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/calibration/calibration_metrics.json\", \"completed_at\": \"2026-05-15T12:36:49.992Z\"}, \"vota_seed42_v4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:12:38.660Z\", \"updated_at\": \"2026-05-15T01:37:13.355Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/vota/final/\", \"log_path\": \"~/runs/trace-verdict-study/vota_seed42_v4.log\", \"wall_clock_seconds\": 8160, \"gpu_hours\": 2.27}, \"hypothesis\": \"VOTA trace provides verdict accuracy lift over no-trace baseline (v4: removed match leakage + fixed label truncation)\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.9563, \"majority_baseline\": 0.7151, \"lift\": 0.2412, \"n\": 1190, \"pass_precision\": 0.944, \"pass_recall\": 0.998, \"pass_f1\": 0.97, \"fail_precision\": 0.993, \"fail_recall\": 0.853, \"fail_f1\": 0.917, \"lift_vs_notrace\": 0.205, \"lift_vs_notrace_ci_lower\": 0.177, \"lift_vs_notrace_ci_upper\": 0.234, \"train_loss\": 0.046, \"eval_loss\": 0.0842}, \"completed_at\": \"2026-05-15T01:10:45.307Z\"}, \"no_trace_seed42_v4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:12:37.755Z\", \"updated_at\": \"2026-05-14T22:39:32.197Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/no_trace/final/\", \"log_path\": \"~/runs/trace-verdict-study/no_trace_seed42_v4.log\", \"wall_clock_seconds\": 1274.7, \"gpu_hours\": 0.35}, \"hypothesis\": \"Baseline: verdict accuracy without execution trace (v4: fixed label truncation)\", \"reproduce\": {\"finished_at\": \"2026-05-14T22:34:36.523Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T22:34:37.283133+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.7513, \"majority_baseline\": 0.7151, \"lift\": 0.0361, \"pass_precision\": 0.8776, \"pass_recall\": 0.7579, \"pass_f1\": 0.8134, \"fail_precision\": 0.5473, \"fail_recall\": 0.7345, \"fail_f1\": 0.6272, \"train_loss\": 0.18, \"eval_loss\": 0.6454, \"eval_mean_token_accuracy\": 0.8897}, \"completed_at\": \"2026-05-14T22:39:12.249Z\"}}, \"count\": 39, \"total\": 39, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2323}}"
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
The result is too large to fit in one response. Let me read it in chunks to extract all the experiment data I need.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a270429-54da-4381-97e3-905a06c925c1",
  "uuid": "a164b7c4-7129-42b7-a240-9f24237fcacd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xk3mAV4dhxaY27RcAnm8mz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 527,
      "cache_read_input_tokens": 24354,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 527
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

Large registry. Let me read it in chunks to extract all experiment metrics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a270429-54da-4381-97e3-905a06c925c1",
  "uuid": "85eeb039-52ba-4663-8ecb-01989759b038",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xk3mAV4dhxaY27RcAnm8mz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 527,
      "cache_read_input_tokens": 24354,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 527
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

<details open><summary>🔧 Tool call — Bash · `toolu_01WWyAsfbBwLQ2boevq3NcZi`</summary>

```json
{
  "command": "wc -l /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/4a270429-54da-4381-97e3-905a06c925c1/tool-results/mcp-agent-ml-research-read_registry-1778953969502.txt",
  "description": "Count lines in registry dump"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a270429-54da-4381-97e3-905a06c925c1",
  "uuid": "592ddec6-73ed-4b73-a80d-c5751d704dc1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xk3mAV4dhxaY27RcAnm8mz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 527,
      "cache_read_input_tokens": 24354,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 527
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

_source line 13 · 2026-05-16T17:52:53.549Z_

<details><summary>↩ Tool result · `toolu_01WWyAsfbBwLQ2boevq3NcZi`</summary>

```text
0 /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/4a270429-54da-4381-97e3-905a06c925c1/tool-results/mcp-agent-ml-research-read_registry-1778953969502.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4a270429-54da-4381-97e3-905a06c925c1",
  "uuid": "0dcc5daf-d8f5-4488-900f-fd4b77c2364f",
  "tool_use_result": {
    "stdout": "0 /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/4a270429-54da-4381-97e3-905a06c925c1/tool-results/mcp-agent-ml-research-read_registry-1778953969502.txt",
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

_source line 14_

<details open><summary>🔧 Tool call — Bash · `toolu_01C8C9WjTv5wEnLM6GTuciut`</summary>

```json
{
  "command": "wc -c /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/4a270429-54da-4381-97e3-905a06c925c1/tool-results/mcp-agent-ml-research-read_registry-1778953969502.txt",
  "description": "Count bytes in registry dump"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a270429-54da-4381-97e3-905a06c925c1",
  "uuid": "695eca75-f2dd-4015-9d70-6acc263ddd44",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014bj1ART8wNMGxLMoE1Ecur",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 321,
      "cache_read_input_tokens": 24881,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 321
      },
      "output_tokens": 57,
      "service_tier": "standard",
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

_source line 15 · 2026-05-16T17:52:57.009Z_

<details><summary>↩ Tool result · `toolu_01C8C9WjTv5wEnLM6GTuciut`</summary>

```text
91938 /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/4a270429-54da-4381-97e3-905a06c925c1/tool-results/mcp-agent-ml-research-read_registry-1778953969502.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4a270429-54da-4381-97e3-905a06c925c1",
  "uuid": "4cde4640-6b2e-46f4-b205-0c9ee517f82b",
  "tool_use_result": {
    "stdout": "91938 /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/4a270429-54da-4381-97e3-905a06c925c1/tool-results/mcp-agent-ml-research-read_registry-1778953969502.txt",
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

_source line 16_

<details open><summary>🔧 Tool call — Bash · `toolu_01Q1TT71M1PAMK4fB8PWrJfh`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/4a270429-54da-4381-97e3-905a06c925c1/tool-results/mcp-agent-ml-research-read_registry-1778953969502.txt | python3 -c \"\nimport json, sys\n\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\n\n# Extract key info from each experiment\nfor exp in result:\n    name = exp.get('name', 'unknown')\n    metrics = exp.get('metrics', {})\n    if metrics:\n        print(f'=== {name} ===')\n        for k, v in metrics.items():\n            print(f'  {k}: {v}')\n        print()\n\"",
  "description": "Extract experiment names and metrics from registry JSON"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a270429-54da-4381-97e3-905a06c925c1",
  "uuid": "670b8aed-b4e5-40bf-8274-0f11a9a7e814",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RU6R9969JFZZAieuKmCcTp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 265,
      "cache_read_input_tokens": 25202,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 265
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

_source line 17 · 2026-05-16T17:53:01.806Z_

<details><summary>↩ Tool result · reported error · `toolu_01Q1TT71M1PAMK4fB8PWrJfh`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 9, in &lt;module>
    name = exp.get('name', 'unknown')
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
  "session_id": "4a270429-54da-4381-97e3-905a06c925c1",
  "uuid": "a948fdce-50b1-488f-8c01-06568b5b0095",
  "tool_use_result": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 9, in &lt;module>\n    name = exp.get('name', 'unknown')\n           ^^^^^^^\nAttributeError: 'str' object has no attribute 'get'"
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Bash · `toolu_01HcGRyy5vR64D9RCWKFrNyb`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/4a270429-54da-4381-97e3-905a06c925c1/tool-results/mcp-agent-ml-research-read_registry-1778953969502.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = data['result']\n# Check structure\nif isinstance(result, str):\n    result = json.loads(result)\nprint(type(result))\nif isinstance(result, list):\n    print(f'Count: {len(result)}')\n    print(f'First item type: {type(result[0])}')\n    if isinstance(result[0], str):\n        print(f'First item: {result[0][:200]}')\n    elif isinstance(result[0], dict):\n        print(f'First item keys: {list(result[0].keys())}')\nelif isinstance(result, dict):\n    print(f'Keys: {list(result.keys())[:20]}')\n\"",
  "description": "Inspect registry JSON structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a270429-54da-4381-97e3-905a06c925c1",
  "uuid": "18357ed3-905a-4ad5-a799-2259c8ea39a7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012DEiErqdaLmWycWySdGMPG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 371,
      "cache_read_input_tokens": 25467,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 371
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

_source line 19 · 2026-05-16T17:53:07.407Z_

<details><summary>↩ Tool result · `toolu_01HcGRyy5vR64D9RCWKFrNyb`</summary>

```text
&lt;class 'dict'>
Keys: ['success', 'data', 'error', 'metadata']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4a270429-54da-4381-97e3-905a06c925c1",
  "uuid": "a6f81c1e-eafa-46fe-950d-fd2ab55d3cd2",
  "tool_use_result": {
    "stdout": "&lt;class 'dict'>\nKeys: ['success', 'data', 'error', 'metadata']",
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

<details open><summary>🔧 Tool call — Bash · `toolu_01WGvnqe2rEanspSjeXAximV`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/4a270429-54da-4381-97e3-905a06c925c1/tool-results/mcp-agent-ml-research-read_registry-1778953969502.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = data['result']\nif isinstance(result, str):\n    result = json.loads(result)\nexperiments = result['data']\nprint(f'Total experiments: {len(experiments)}')\nfor exp in experiments:\n    name = exp.get('name', 'unknown')\n    metrics = exp.get('metrics', {})\n    print(f'=== {name} ===')\n    if metrics:\n        for k, v in metrics.items():\n            print(f'  {k}: {v}')\n    else:\n        print('  (no metrics)')\n    print()\n\" 2>&1",
  "description": "Extract all experiment names and metrics",
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
  "session_id": "4a270429-54da-4381-97e3-905a06c925c1",
  "uuid": "d8bcdbad-14f5-46e5-b12c-229816c005a2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V2zwLiWrTvGRC7TU9hNY2R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 385,
      "cache_read_input_tokens": 25838,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 385
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

_source line 21 · 2026-05-16T17:53:12.544Z_

<details><summary>↩ Tool result · reported error · `toolu_01WGvnqe2rEanspSjeXAximV`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 10, in &lt;module>
    name = exp.get('name', 'unknown')
           ^^^^^^^
AttributeError: 'str' object has no attribute 'get'
Total experiments: 4
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4a270429-54da-4381-97e3-905a06c925c1",
  "uuid": "5593cb80-32ad-4178-a9fa-8ad5afde2aca",
  "tool_use_result": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 10, in &lt;module>\n    name = exp.get('name', 'unknown')\n           ^^^^^^^\nAttributeError: 'str' object has no attribute 'get'\nTotal experiments: 4"
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Bash · `toolu_01FRB4LJgNXtdNPGpSW2TF5A`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/4a270429-54da-4381-97e3-905a06c925c1/tool-results/mcp-agent-ml-research-read_registry-1778953969502.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = data['result']\nif isinstance(result, str):\n    result = json.loads(result)\nexperiments = result['data']\nprint(f'Total: {len(experiments)}')\nfor i, exp in enumerate(experiments):\n    print(f'Item {i}: type={type(exp).__name__}')\n    if isinstance(exp, str):\n        print(f'  value: {exp[:200]}')\n    elif isinstance(exp, dict):\n        print(f'  keys: {list(exp.keys())[:10]}')\n\"",
  "description": "Check data item types"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a270429-54da-4381-97e3-905a06c925c1",
  "uuid": "b1582213-e698-4410-b9cb-4b862e4d8ac8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FuXmCwUxrsr18kUxkVfzga",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 437,
      "cache_read_input_tokens": 26223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 437
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

_source line 23 · 2026-05-16T17:53:17.280Z_

<details><summary>↩ Tool result · `toolu_01FRB4LJgNXtdNPGpSW2TF5A`</summary>

```text
Total: 4
Item 0: type=str
  value: experiments
Item 1: type=str
  value: count
Item 2: type=str
  value: total
Item 3: type=str
  value: baseline
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4a270429-54da-4381-97e3-905a06c925c1",
  "uuid": "41fefde2-ad07-46b1-bc99-56facf06c9d4",
  "tool_use_result": {
    "stdout": "Total: 4\nItem 0: type=str\n  value: experiments\nItem 1: type=str\n  value: count\nItem 2: type=str\n  value: total\nItem 3: type=str\n  value: baseline",
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

<details open><summary>🔧 Tool call — Bash · `toolu_01Rkoo1cpAie4FtTZUrZauyD`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/4a270429-54da-4381-97e3-905a06c925c1/tool-results/mcp-agent-ml-research-read_registry-1778953969502.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = data['result']\nif isinstance(result, str):\n    result = json.loads(result)\n# It's a dict with key names as items\nfor key in result['data']:\n    val = result['data'][key]\n    if isinstance(val, list):\n        print(f'{key}: list of {len(val)} items')\n    elif isinstance(val, dict):\n        print(f'{key}: dict with {len(val)} keys')\n    else:\n        print(f'{key}: {val}')\n\"",
  "description": "Inspect data structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a270429-54da-4381-97e3-905a06c925c1",
  "uuid": "96c40ed6-e8bb-44f8-9986-e5abacd382d7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y7RseJDCqC2uym45QxH1yS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 483,
      "cache_read_input_tokens": 26660,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 483
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

_source line 25 · 2026-05-16T17:53:22.254Z_

<details><summary>↩ Tool result · `toolu_01Rkoo1cpAie4FtTZUrZauyD`</summary>

```text
experiments: dict with 39 keys
count: 39
total: 39
baseline: None
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4a270429-54da-4381-97e3-905a06c925c1",
  "uuid": "b4ad4981-cb74-4f98-9d5c-a8c6af27dd0c",
  "tool_use_result": {
    "stdout": "experiments: dict with 39 keys\ncount: 39\ntotal: 39\nbaseline: None",
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

_source line 26_

<details open><summary>🔧 Tool call — Bash · `toolu_01MBYXAuhZQ94MZQJz9Kp1Yt`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/4a270429-54da-4381-97e3-905a06c925c1/tool-results/mcp-agent-ml-research-read_registry-1778953969502.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = data['result']\nif isinstance(result, str):\n    result = json.loads(result)\nexperiments = result['data']['experiments']\nfor name, exp in experiments.items():\n    metrics = exp.get('metrics', {})\n    print(f'=== {name} ===')\n    if metrics:\n        for k, v in metrics.items():\n            print(f'  {k}: {v}')\n    else:\n        print('  (no metrics)')\n    print()\n\"",
  "description": "Extract all experiment names and metrics",
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
  "session_id": "4a270429-54da-4381-97e3-905a06c925c1",
  "uuid": "111d3667-9fbb-4f32-964d-bffc187cacf8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015zvdAWAygy2FUQ3mqLPWjf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 340,
      "cache_read_input_tokens": 27143,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 340
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

_source line 27 · 2026-05-16T17:53:26.690Z_

<details><summary>↩ Tool result · `toolu_01MBYXAuhZQ94MZQJz9Kp1Yt`</summary>

```text
=== qwen15b_nomarker_seed42 ===
  accuracy: 0.978
  n: 1190
  accuracy_ci: [0.97, 0.986]
  majority_baseline: 0.715
  lift: 0.263
  pass_precision: 0.97
  pass_recall: 1
  pass_f1: 0.98
  fail_precision: 1
  fail_recall: 0.92
  fail_f1: 0.96

=== exception_only_nomarker_seed42 ===
  accuracy: 0.9655
  n: 1190
  accuracy_ci: [0.955, 0.976]

=== codellama13b_exception_only_seed42 ===
  accuracy: 0.9983
  n: 1190
  errors: 2

=== loop_only_seed456 ===
  accuracy: 0.8664
  n: 1190
  pass_precision: 0.9179
  pass_recall: 0.8931
  pass_f1: 0.9053
  fail_precision: 0.7486
  fail_recall: 0.7994
  fail_f1: 0.7732
  accuracy_ci: [0.847, 0.884]

=== loop_only_seed123 ===
  accuracy: 0.8588
  majority_baseline: 0.7151
  lift: 0.1437
  n: 1190
  pass_precision: 0.9129
  pass_recall: 0.8872
  pass_f1: 0.8999
  fail_precision: 0.7355
  fail_recall: 0.7876
  fail_f1: 0.7607
  accuracy_ci: [0.8403, 0.8773]

=== codellama13b_no_trace_seed42 ===
  accuracy: 0.765
  n: 1190
  majority_baseline: 0.7151
  lift: 0.05
  pass_precision: 0.84
  pass_recall: 0.83
  pass_f1: 0.84
  fail_precision: 0.59
  fail_recall: 0.59
  fail_f1: 0.59
  accuracy_ci: [0.738, 0.787]

=== qwen15b_full_trace_seed42 ===
  accuracy: 0.7706
  n: 1190

=== qwen15b_vota_seed42 ===
  accuracy: 0.9958
  n: 1190
  pass_recall: 0.9976
  fail_recall: 0.9912
  pass_f1: 0.9971
  fail_f1: 0.9926
  training_time_sec: 2922

=== qwen15b_no_trace_seed42 ===
  accuracy: 0.6731
  n: 1190
  pass_f1: 0.7527
  fail_f1: 0.518
  lift_over_majority: -0.042
  training_time_sec: 851

=== qwen15b_exception_only_seed42 ===
  accuracy: 0.9983
  accuracy_ci_lower: 0.9958
  accuracy_ci_upper: 1
  majority_baseline: 0.7151
  lift: 0.283
  n: 1190
  pass_precision: 1
  pass_recall: 0.9976
  pass_f1: 0.9988
  fail_precision: 0.9941
  fail_recall: 1
  fail_f1: 0.9971
  train_loss: 0.1347
  eval_loss: 0.5761
  wall_clock_seconds: 1762

=== label_only_seed456 ===
  accuracy: 0.859
  n: 1190
  pass_recall: 0.938
  fail_recall: 0.661
  pass_f1: 0.905
  fail_f1: 0.727

=== label_only_seed123 ===
  accuracy: 0.8706
  n: 1190
  pass_recall: 0.974
  fail_recall: 0.611
  pass_f1: 0.915
  fail_f1: 0.729

=== ae_only_seed456 ===
  accuracy: 0.9992
  n: 1190
  majority_baseline: 0.7151
  lift: 0.2841
  seed_comparison: {'seed42_accuracy': 0.9992, 'seed123_accuracy': 0.9908, 'seed456_accuracy': 0.9992, 'mean_accuracy': 0.9964, 'std': 0.0049, 'note': '2/3 seeds = 99.92%, seed123 = 99.08%. Mean = 99.64% ± 0.49'}

=== ae_only_seed123 ===
  accuracy: 0.9908
  n: 1190
  pass_recall: 0.987
  fail_recall: 1
  majority_baseline: 0.7151
  lift: 0.2757

=== regex_baseline_analysis ===
  regex_B1_ERROR_presence: 0.9345
  regex_B2_Traceback: 0.7151
  regex_B3_any_keyword: 0.9345
  regex_B4_exception_type: 0.9361
  regex_B5_format_marker: 0.9933
  regex_B6_error_count_ge2: 0.9202
  sft_exception_only: 0.9983
  best_regex_gap_vs_sft: -0.0622
  B5_mcnemar_p: 0.041
  n: 1190

=== deepseek_vota_seed42 ===
  accuracy: 0.8445
  majority_baseline: 0.7151
  lift: 0.1294
  accuracy_ci: [0.826, 0.864]
  pass_precision: 0.821
  pass_recall: 1
  pass_f1: 0.902
  fail_precision: 1
  fail_recall: 0.454
  fail_f1: 0.625
  eval_loss_epoch1: 0.0679
  eval_loss_epoch2: 0.095
  eval_loss_epoch3: 0.1121
  final_train_loss: 0.0522
  epoch1_checkpoint_eval: {'accuracy': 0.7815, 'accuracy_ci': [0.76, 0.803], 'fail_recall': 0.233, 'fail_precision': 1, 'pass_recall': 1, 'pass_precision': 0.766, 'fail_f1': 0.378, 'pass_f1': 0.867, 'conclusion': 'epoch3_final_is_better'}
  reeval_with_fixed_script: {'accuracy': 0.16, 'accuracy_ci': [0.139, 0.18], 'fail_f1': 0.61, 'fail_precision': 0.9, 'fail_recall': 0.47, 'pass_f1': 0.07, 'pass_precision': 1, 'pass_recall': 0.04, 'note': 'CATASTROPHIC: re-eval with corrected evaluate.py shows 16% (vs original 84.45%). Model predicts fail for almost everything. Previous 84.45% may have been from buggy eval. NEEDS INVESTIGATION.'}
  group_analysis: {'train_truncated': {'n': 1091, 'accuracy': 0.8304, 'ci_95': [0.8075, 0.8524], 'correct': 906, 'incorrect': 185, 'pass_accuracy': 1, 'pass_n': 822, 'fail_accuracy': 0.3123, 'fail_n': 269}, 'train_intact': {'n': 99, 'accuracy': 1, 'ci_95': [1, 1], 'correct': 99, 'incorrect': 0, 'pass_accuracy': 1, 'pass_n': 29, 'fail_accuracy': 1, 'fail_n': 70}, 'fisher_exact': {'odds_ratio': 0, 'p_value': 0}, 'overall_accuracy': 0.8445, 'max_length': 2048, 'note': "Grouped by whether training sample content exceeded token budget (DeepSeek tokenizer, max_length=2048). Inference used full-length input (no truncation). All 185 errors from truncated group's fail class (fail_recall=31.2%). Intact group: 100% accuracy."}

=== deepseek_full_trace_seed42_v3 ===
  accuracy: 0.7916
  majority_baseline: 0.7151
  lift: 0.0765
  n: 1190
  pass_precision: 0.857
  pass_recall: 0.851
  pass_f1: 0.854
  fail_precision: 0.632
  fail_recall: 0.643
  fail_f1: 0.637
  accuracy_ci: [0.768, 0.813]
  train_loss: 0.0547
  train_runtime_seconds: 8891
  epochs: 3
  reeval_discrepancy: {'reeval_accuracy': 0.285, 'reeval_note': 'RESOLVED: 28.5% was caused by eval max_length=16384 (OOD). Re-eval with max_length=2048 reproduces 79.16%. predictions.jsonl updated to maxlen2048 results.', 'status': 'RESOLVED'}

=== eval_missing_predictions_batch_v2 ===
  (no metrics)

=== debugbench_vota_seed42 ===
  accuracy: 0.9977
  majority_baseline: 0.5141
  lift: 0.4836
  n: 426
  pass_precision: 1
  pass_recall: 1
  pass_f1: 1
  fail_precision: 1
  fail_recall: 1
  fail_f1: 1
  accuracy_ci: [0.993, 1]
  train_loss: 0.098
  eval_loss: 0.1179
  eval_mean_token_accuracy: 0.9737
  errors: 1

=== eval_missing_predictions_batch ===
  (no metrics)

=== debugbench_exception_only_seed42 ===
  accuracy: 1
  majority_baseline: 0.5141
  lift: 0.4859
  n: 426
  pass_precision: 1
  pass_recall: 1
  pass_f1: 1
  fail_precision: 1
  fail_recall: 1
  fail_f1: 1
  accuracy_ci_wilson: [0.9914, 1]
  accuracy_ci_bootstrap: [1, 1]
  train_loss: 0.2435
  eval_loss: 0.4157
  train_runtime_sec: 837

=== deepseek_exception_only_seed456 ===
  accuracy: 0.9933
  majority_baseline: 0.7151
  lift: 0.2782
  n: 1190
  pass_precision: 1
  pass_recall: 0.9906
  pass_f1: 0.9953
  fail_precision: 0.9769
  fail_recall: 1
  fail_f1: 0.9883
  accuracy_ci: [0.9882, 0.9975]
  train_loss: 0.1225
  eval_loss: 0.4824
  train_runtime_sec: 6246
  seed_comparison: {'seed42_accuracy': 0.9933, 'seed456_accuracy': 0.9933, 'seed123_accuracy': 0.9109, 'note': 'seed42 and seed456 identical (99.33%); seed123 outlier (91.09%). 2/3 seeds robust.'}
  epoch1_checkpoint_eval: {'accuracy': 0.993, 'accuracy_ci': [0.988, 0.997], 'fail_f1': 0.99, 'fail_precision': 0.98, 'fail_recall': 1, 'pass_f1': 1, 'pass_precision': 1, 'pass_recall': 0.99, 'conclusion': 'epoch1 (99.3%) ≈ epoch3 (99.33%), 1 epoch convergence confirmed'}

=== deepseek_exception_only_seed42 ===
  accuracy: 0.9933
  majority_baseline: 0.7151
  lift: 0.2782
  n: 1190
  pass_precision: 1
  pass_recall: 0.9906
  pass_f1: 0.9953
  fail_precision: 0.9769
  fail_recall: 1
  fail_f1: 0.9883
  epoch1_checkpoint_eval: {'accuracy': 0.9983, 'fail_recall': 1, 'fail_precision': 0.9941, 'pass_recall': 0.9976, 'conclusion': 'epoch1_better_by_0.50pp'}

=== debugbench_no_trace_seed42 ===
  accuracy: 0.9671
  majority_baseline: 0.5141
  lift: 0.4531
  pass_precision: 1
  pass_recall: 0.936
  pass_f1: 0.967
  fail_precision: 0.937
  fail_recall: 1
  fail_f1: 0.967
  accuracy_ci: [0.948, 0.984]
  train_loss: 0.249
  eval_loss: 0.532

=== debugbench_exception_bug_fix ===
  (no metrics)

=== vota_seed456_v2 ===
  accuracy: 0.9908
  pass_precision: 1
  pass_recall: 0.987
  pass_f1: 0.993
  fail_precision: 0.969
  fail_recall: 1
  fail_f1: 0.984
  ci_95: [0.985, 0.996]

=== exception_only_seed123 ===
  accuracy: 0.9983
  accuracy_ci: [0.9958, 1]
  majority_baseline: 0.7151
  lift: 0.2832
  n: 1190
  pass_precision: 1
  pass_recall: 0.9976
  pass_f1: 0.9988
  fail_precision: 0.9941
  fail_recall: 1
  fail_f1: 0.9971
  train_loss: 0.1096
  train_runtime_sec: 7507
  epochs: 3
  seed_comparison: {'seed42_accuracy': 0.9983, 'seed456_accuracy': 0.9983, 'seed123_accuracy': 0.9983, 'max_diff': 0, 'note': 'identical accuracy to 4 decimal places across all 3 seeds (42/456/123); each has exactly 2/1190 errors; exception_only fully seed-robust'}

=== exception_only_seed456 ===
  accuracy: 0.9983
  accuracy_ci: [0.9958, 1]
  majority_baseline: 0.7151
  lift: 0.2832
  n: 1190
  pass_precision: 1
  pass_recall: 0.9976
  pass_f1: 0.9988
  fail_precision: 0.9941
  fail_recall: 1
  fail_f1: 0.9971
  vs_seed42: {'seed42_accuracy': 0.9983, 'seed456_accuracy': 0.9983, 'diff': 0, 'note': 'identical accuracy to 4 decimal places; no predictions.jsonl for paired bootstrap'}
  train_loss: 0.1087
  eval_loss: 0.4629
  train_runtime_sec: 4541
  epochs: 3

=== vota_exception_only_seed42_v2 ===
  accuracy: 0.9983
  majority_baseline: 0.7151
  lift: 0.2832
  n: 1190
  pass_precision: 1
  pass_recall: 0.998
  pass_f1: 0.999
  fail_precision: 0.994
  fail_recall: 1
  fail_f1: 0.997
  lift_vs_notrace: 0.2471
  lift_vs_notrace_ci_lower: 0.2227
  lift_vs_notrace_ci_upper: 0.2714
  lift_vs_fulltrace: 0.1807
  lift_vs_fulltrace_ci_lower: 0.1588
  lift_vs_fulltrace_ci_upper: 0.2034
  lift_vs_vota: 0.0067
  lift_vs_vota_ci_lower: 0.0017
  lift_vs_vota_ci_upper: 0.0126
  lift_vs_vota_pvalue: 0.01

=== full_trace_label_only_seed42 ===
  accuracy: 0.8622
  accuracy_ci_lower: 0.8437
  accuracy_ci_upper: 0.8807
  majority_baseline: 0.7151
  lift: 0.1471
  n: 1190
  pass_precision: 0.8821
  pass_recall: 0.9318
  pass_f1: 0.9063
  fail_precision: 0.8007
  fail_recall: 0.6873
  fail_f1: 0.7397
  train_loss: 0.2505
  eval_loss: 0.3205
  lift_vs_notrace: 0.1109
  lift_vs_notrace_ci_lower: 0.0849
  lift_vs_notrace_ci_upper: 0.137
  lift_vs_standard_fulltrace: 0.0445
  lift_vs_standard_fulltrace_ci_lower: 0.0235
  lift_vs_standard_fulltrace_ci_upper: 0.0655
  lift_vs_standard_fulltrace_pvalue: 0

=== vota_no_ae_seed42 ===
  accuracy: 0.994
  majority_baseline: 0.7151
  lift: 0.279
  n: 1190
  pass_f1: 0.996
  fail_f1: 0.989
  accuracy_ci_lower: 0.989
  accuracy_ci_upper: 0.998
  lift_vs_notrace: 0.243
  lift_vs_notrace_ci_lower: 0.218
  lift_vs_notrace_ci_upper: 0.268
  train_loss: 0.0908
  eval_loss: 0.2215
  wall_clock_seconds: 6397.88

=== vota_loop_only_seed42 ===
  accuracy: 0.8563
  majority_baseline: 0.7151
  lift: 0.1412
  n: 1190
  pass_precision: 0.9239
  pass_recall: 0.8707
  pass_f1: 0.8966
  fail_precision: 0.7165
  fail_recall: 0.8201
  fail_f1: 0.7648
  accuracy_ci: [0.8353, 0.8756]
  bootstrap_vs_no_trace: {'diff': 0.105, 'ci': [0.0824, 0.1286], 'significant': True}
  bootstrap_vs_vota: {'diff': -0.1378, 'ci': [-0.1571, -0.1185], 'significant': True}
  bootstrap_vs_full_trace: {'diff': 0.0387, 'ci': [0.0185, 0.0597], 'significant': True}
  train_loss: 0.0718
  wall_clock_seconds: 7425.65

=== vota_ae_only_seed42 ===
  accuracy: 0.9992
  accuracy_ci: [0.9975, 1]
  bootstrap_pairwise: {'ae_only_vs_no_trace': {'diff': 0.2479, 'ci': [0.2235, 0.2731], 'p_value': 0, 'significant': True}, 'ae_only_vs_exception_only': {'diff': 0.0008, 'ci': [-0.0017, 0.0034], 'p_value': 0.8002, 'significant': False}, 'ae_only_vs_vota': {'diff': 0.005, 'ci': [0.0017, 0.0092], 'p_value': 0.0046, 'significant': True}}
  config: {'n_bootstrap': 10000, 'seed': 42, 'method': 'paired_bootstrap'}

=== full_trace_seed42_v5 ===
  accuracy: 0.8176
  majority_baseline: 0.7151
  lift: 0.1025
  n: 1190
  pass_precision: 0.8774
  pass_recall: 0.866
  pass_f1: 0.8717
  fail_precision: 0.6743
  fail_recall: 0.6962
  fail_f1: 0.6851
  accuracy_ci_lower: 0.797
  accuracy_ci_upper: 0.839
  lift_vs_notrace: 0.0664
  lift_vs_notrace_ci_lower: 0.0437
  lift_vs_notrace_ci_upper: 0.0899
  train_loss: 0.05
  eval_loss: 0.0867
  wall_clock_seconds: 7852
  epoch_level: {'epoch1_accuracy': 0.8303, 'epoch2_accuracy': 0.763, 'final_accuracy': 0.8176, 'trend': 'non_monotonic_epoch1_best_epoch2_collapse'}

=== no_trace_seed42_v5 ===
  accuracy: 0.7513
  accuracy_ci_lower: 0.7277
  accuracy_ci_upper: 0.7748
  majority_baseline: 0.7151
  lift: 0.0361
  lift_ci_lower: 0.0042
  lift_ci_upper: 0.0706
  n: 1190
  pass_precision: 0.8776
  pass_recall: 0.7579
  pass_f1: 0.8134
  fail_precision: 0.5473
  fail_recall: 0.7345
  fail_f1: 0.6272
  epoch_level: {'epoch1_accuracy': 0.7429, 'epoch2_accuracy': 0.763, 'final_accuracy': 0.7513, 'trend': 'non_monotonic_epoch2_best'}

=== vota_seed42_v5 ===
  accuracy: 0.9941
  majority_baseline: 0.7151
  lift: 0.279
  n: 1190
  pass_precision: 1
  pass_recall: 0.9882
  pass_f1: 0.9941
  fail_precision: 0.9714
  fail_recall: 1
  fail_f1: 0.9855
  lift_vs_notrace: 0.2428
  lift_vs_notrace_ci_lower: 0.2185
  lift_vs_notrace_ci_upper: 0.2681
  accuracy_ci_lower: 0.9882
  accuracy_ci_upper: 0.9983
  train_loss: 0.05
  eval_loss: 0.0867
  eval_mean_token_accuracy: 0.9828
  wall_clock_seconds: 8443
  epoch_level: {'epoch1_accuracy': 0.9933, 'epoch2_accuracy': 0.9941, 'final_accuracy': 0.9941, 'trend': 'monotonic_increasing_then_stable'}

=== calibration_analysis_seed42 ===
  no_trace: {'ece': 0.171476, 'mce': 0.475643, 'brier_score': 0.197152, 'accuracy': 0.751261, 'n_samples': 1190}
  full_trace: {'ece': 0.095817, 'mce': 0.249061, 'brier_score': 0.143924, 'accuracy': 0.817647, 'n_samples': 1190}
  label_only: {'ece': 0.110686, 'mce': 0.417124, 'brier_score': 0.120144, 'accuracy': 0.862185, 'n_samples': 1190}
  loop_only: {'ece': 0.083085, 'mce': 0.183406, 'brier_score': 0.118335, 'accuracy': 0.856303, 'n_samples': 1190}
  ae_only: {'ece': 0.000415, 'mce': 0.000415, 'brier_score': 0.000847, 'accuracy': 0.99916, 'n_samples': 1190}
  exception_only: {'ece': 0.002717, 'mce': 0.835484, 'brier_score': 0.001311, 'accuracy': 0.998319, 'n_samples': 1190}
  vota: {'ece': 0.00541, 'mce': 0.622459, 'brier_score': 0.005234, 'accuracy': 0.994118, 'n_samples': 1190}

=== vota_seed42_v4 ===
  accuracy: 0.9563
  majority_baseline: 0.7151
  lift: 0.2412
  n: 1190
  pass_precision: 0.944
  pass_recall: 0.998
  pass_f1: 0.97
  fail_precision: 0.993
  fail_recall: 0.853
  fail_f1: 0.917
  lift_vs_notrace: 0.205
  lift_vs_notrace_ci_lower: 0.177
  lift_vs_notrace_ci_upper: 0.234
  train_loss: 0.046
  eval_loss: 0.0842

=== no_trace_seed42_v4 ===
  accuracy: 0.7513
  majority_baseline: 0.7151
  lift: 0.0361
  pass_precision: 0.8776
  pass_recall: 0.7579
  pass_f1: 0.8134
  fail_precision: 0.5473
  fail_recall: 0.7345
  fail_f1: 0.6272
  train_loss: 0.18
  eval_loss: 0.6454
  eval_mean_token_accuracy: 0.8897
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4a270429-54da-4381-97e3-905a06c925c1",
  "uuid": "f38564af-76d0-481d-b50e-655a6cfa87f8",
  "tool_use_result": {
    "stdout": "=== qwen15b_nomarker_seed42 ===\n  accuracy: 0.978\n  n: 1190\n  accuracy_ci: [0.97, 0.986]\n  majority_baseline: 0.715\n  lift: 0.263\n  pass_precision: 0.97\n  pass_recall: 1\n  pass_f1: 0.98\n  fail_precision: 1\n  fail_recall: 0.92\n  fail_f1: 0.96\n\n=== exception_only_nomarker_seed42 ===\n  accuracy: 0.9655\n  n: 1190\n  accuracy_ci: [0.955, 0.976]\n\n=== codellama13b_exception_only_seed42 ===\n  accuracy: 0.9983\n  n: 1190\n  errors: 2\n\n=== loop_only_seed456 ===\n  accuracy: 0.8664\n  n: 1190\n  pass_precision: 0.9179\n  pass_recall: 0.8931\n  pass_f1: 0.9053\n  fail_precision: 0.7486\n  fail_recall: 0.7994\n  fail_f1: 0.7732\n  accuracy_ci: [0.847, 0.884]\n\n=== loop_only_seed123 ===\n  accuracy: 0.8588\n  majority_baseline: 0.7151\n  lift: 0.1437\n  n: 1190\n  pass_precision: 0.9129\n  pass_recall: 0.8872\n  pass_f1: 0.8999\n  fail_precision: 0.7355\n  fail_recall: 0.7876\n  fail_f1: 0.7607\n  accuracy_ci: [0.8403, 0.8773]\n\n=== codellama13b_no_trace_seed42 ===\n  accuracy: 0.765\n  n: 1190\n  majority_baseline: 0.7151\n  lift: 0.05\n  pass_precision: 0.84\n  pass_recall: 0.83\n  pass_f1: 0.84\n  fail_precision: 0.59\n  fail_recall: 0.59\n  fail_f1: 0.59\n  accuracy_ci: [0.738, 0.787]\n\n=== qwen15b_full_trace_seed42 ===\n  accuracy: 0.7706\n  n: 1190\n\n=== qwen15b_vota_seed42 ===\n  accuracy: 0.9958\n  n: 1190\n  pass_recall: 0.9976\n  fail_recall: 0.9912\n  pass_f1: 0.9971\n  fail_f1: 0.9926\n  training_time_sec: 2922\n\n=== qwen15b_no_trace_seed42 ===\n  accuracy: 0.6731\n  n: 1190\n  pass_f1: 0.7527\n  fail_f1: 0.518\n  lift_over_majority: -0.042\n  training_time_sec: 851\n\n=== qwen15b_exception_only_seed42 ===\n  accuracy: 0.9983\n  accuracy_ci_lower: 0.9958\n  accuracy_ci_upper: 1\n  majority_baseline: 0.7151\n  lift: 0.283\n  n: 1190\n  pass_precision: 1\n  pass_recall: 0.9976\n  pass_f1: 0.9988\n  fail_precision: 0.9941\n  fail_recall: 1\n  fail_f1: 0.9971\n  train_loss: 0.1347\n  eval_loss: 0.5761\n  wall_clock_seconds: 1762\n\n=== label_only_seed456 ===\n  accuracy: 0.859\n  n: 1190\n  pass_recall: 0.938\n  fail_recall: 0.661\n  pass_f1: 0.905\n  fail_f1: 0.727\n\n=== label_only_seed123 ===\n  accuracy: 0.8706\n  n: 1190\n  pass_recall: 0.974\n  fail_recall: 0.611\n  pass_f1: 0.915\n  fail_f1: 0.729\n\n=== ae_only_seed456 ===\n  accuracy: 0.9992\n  n: 1190\n  majority_baseline: 0.7151\n  lift: 0.2841\n  seed_comparison: {'seed42_accuracy': 0.9992, 'seed123_accuracy': 0.9908, 'seed456_accuracy': 0.9992, 'mean_accuracy': 0.9964, 'std': 0.0049, 'note': '2/3 seeds = 99.92%, seed123 = 99.08%. Mean = 99.64% ± 0.49'}\n\n=== ae_only_seed123 ===\n  accuracy: 0.9908\n  n: 1190\n  pass_recall: 0.987\n  fail_recall: 1\n  majority_baseline: 0.7151\n  lift: 0.2757\n\n=== regex_baseline_analysis ===\n  regex_B1_ERROR_presence: 0.9345\n  regex_B2_Traceback: 0.7151\n  regex_B3_any_keyword: 0.9345\n  regex_B4_exception_type: 0.9361\n  regex_B5_format_marker: 0.9933\n  regex_B6_error_count_ge2: 0.9202\n  sft_exception_only: 0.9983\n  best_regex_gap_vs_sft: -0.0622\n  B5_mcnemar_p: 0.041\n  n: 1190\n\n=== deepseek_vota_seed42 ===\n  accuracy: 0.8445\n  majority_baseline: 0.7151\n  lift: 0.1294\n  accuracy_ci: [0.826, 0.864]\n  pass_precision: 0.821\n  pass_recall: 1\n  pass_f1: 0.902\n  fail_precision: 1\n  fail_recall: 0.454\n  fail_f1: 0.625\n  eval_loss_epoch1: 0.0679\n  eval_loss_epoch2: 0.095\n  eval_loss_epoch3: 0.1121\n  final_train_loss: 0.0522\n  epoch1_checkpoint_eval: {'accuracy': 0.7815, 'accuracy_ci': [0.76, 0.803], 'fail_recall': 0.233, 'fail_precision': 1, 'pass_recall': 1, 'pass_precision': 0.766, 'fail_f1': 0.378, 'pass_f1': 0.867, 'conclusion': 'epoch3_final_is_better'}\n  reeval_with_fixed_script: {'accuracy': 0.16, 'accuracy_ci': [0.139, 0.18], 'fail_f1': 0.61, 'fail_precision': 0.9, 'fail_recall': 0.47, 'pass_f1': 0.07, 'pass_precision': 1, 'pass_recall': 0.04, 'note': 'CATASTROPHIC: re-eval with corrected evaluate.py shows 16% (vs original 84.45%). Model predicts fail for almost everything. Previous 84.45% may have been from buggy eval. NEEDS INVESTIGATION.'}\n  group_analysis: {'train_truncated': {'n': 1091, 'accuracy': 0.8304, 'ci_95': [0.8075, 0.8524], 'correct': 906, 'incorrect': 185, 'pass_accuracy': 1, 'pass_n': 822, 'fail_accuracy': 0.3123, 'fail_n': 269}, 'train_intact': {'n': 99, 'accuracy': 1, 'ci_95': [1, 1], 'correct': 99, 'incorrect': 0, 'pass_accuracy': 1, 'pass_n': 29, 'fail_accuracy': 1, 'fail_n': 70}, 'fisher_exact': {'odds_ratio': 0, 'p_value': 0}, 'overall_accuracy': 0.8445, 'max_length': 2048, 'note': \"Grouped by whether training sample content exceeded token budget (DeepSeek tokenizer, max_length=2048). Inference used full-length input (no truncation). All 185 errors from truncated group's fail class (fail_recall=31.2%). Intact group: 100% accuracy.\"}\n\n=== deepseek_full_trace_seed42_v3 ===\n  accuracy: 0.7916\n  majority_baseline: 0.7151\n  lift: 0.0765\n  n: 1190\n  pass_precision: 0.857\n  pass_recall: 0.851\n  pass_f1: 0.854\n  fail_precision: 0.632\n  fail_recall: 0.643\n  fail_f1: 0.637\n  accuracy_ci: [0.768, 0.813]\n  train_loss: 0.0547\n  train_runtime_seconds: 8891\n  epochs: 3\n  reeval_discrepancy: {'reeval_accuracy': 0.285, 'reeval_note': 'RESOLVED: 28.5% was caused by eval max_length=16384 (OOD). Re-eval with max_length=2048 reproduces 79.16%. predictions.jsonl updated to maxlen2048 results.', 'status': 'RESOLVED'}\n\n=== eval_missing_predictions_batch_v2 ===\n  (no metrics)\n\n=== debugbench_vota_seed42 ===\n  accuracy: 0.9977\n  majority_baseline: 0.5141\n  lift: 0.4836\n  n: 426\n  pass_precision: 1\n  pass_recall: 1\n  pass_f1: 1\n  fail_precision: 1\n  fail_recall: 1\n  fail_f1: 1\n  accuracy_ci: [0.993, 1]\n  train_loss: 0.098\n  eval_loss: 0.1179\n  eval_mean_token_accuracy: 0.9737\n  errors: 1\n\n=== eval_missing_predictions_batch ===\n  (no metrics)\n\n=== debugbench_exception_only_seed42 ===\n  accuracy: 1\n  majority_baseline: 0.5141\n  lift: 0.4859\n  n: 426\n  pass_precision: 1\n  pass_recall: 1\n  pass_f1: 1\n  fail_precision: 1\n  fail_recall: 1\n  fail_f1: 1\n  accuracy_ci_wilson: [0.9914, 1]\n  accuracy_ci_bootstrap: [1, 1]\n  train_loss: 0.2435\n  eval_loss: 0.4157\n  train_runtime_sec: 837\n\n=== deepseek_exception_only_seed456 ===\n  accuracy: 0.9933\n  majority_baseline: 0.7151\n  lift: 0.2782\n  n: 1190\n  pass_precision: 1\n  pass_recall: 0.9906\n  pass_f1: 0.9953\n  fail_precision: 0.9769\n  fail_recall: 1\n  fail_f1: 0.9883\n  accuracy_ci: [0.9882, 0.9975]\n  train_loss: 0.1225\n  eval_loss: 0.4824\n  train_runtime_sec: 6246\n  seed_comparison: {'seed42_accuracy': 0.9933, 'seed456_accuracy': 0.9933, 'seed123_accuracy': 0.9109, 'note': 'seed42 and seed456 identical (99.33%); seed123 outlier (91.09%). 2/3 seeds robust.'}\n  epoch1_checkpoint_eval: {'accuracy': 0.993, 'accuracy_ci': [0.988, 0.997], 'fail_f1': 0.99, 'fail_precision': 0.98, 'fail_recall': 1, 'pass_f1': 1, 'pass_precision': 1, 'pass_recall': 0.99, 'conclusion': 'epoch1 (99.3%) ≈ epoch3 (99.33%), 1 epoch convergence confirmed'}\n\n=== deepseek_exception_only_seed42 ===\n  accuracy: 0.9933\n  majority_baseline: 0.7151\n  lift: 0.2782\n  n: 1190\n  pass_precision: 1\n  pass_recall: 0.9906\n  pass_f1: 0.9953\n  fail_precision: 0.9769\n  fail_recall: 1\n  fail_f1: 0.9883\n  epoch1_checkpoint_eval: {'accuracy': 0.9983, 'fail_recall': 1, 'fail_precision': 0.9941, 'pass_recall': 0.9976, 'conclusion': 'epoch1_better_by_0.50pp'}\n\n=== debugbench_no_trace_seed42 ===\n  accuracy: 0.9671\n  majority_baseline: 0.5141\n  lift: 0.4531\n  pass_precision: 1\n  pass_recall: 0.936\n  pass_f1: 0.967\n  fail_precision: 0.937\n  fail_recall: 1\n  fail_f1: 0.967\n  accuracy_ci: [0.948, 0.984]\n  train_loss: 0.249\n  eval_loss: 0.532\n\n=== debugbench_exception_bug_fix ===\n  (no metrics)\n\n=== vota_seed456_v2 ===\n  accuracy: 0.9908\n  pass_precision: 1\n  pass_recall: 0.987\n  pass_f1: 0.993\n  fail_precision: 0.969\n  fail_recall: 1\n  fail_f1: 0.984\n  ci_95: [0.985, 0.996]\n\n=== exception_only_seed123 ===\n  accuracy: 0.9983\n  accuracy_ci: [0.9958, 1]\n  majority_baseline: 0.7151\n  lift: 0.2832\n  n: 1190\n  pass_precision: 1\n  pass_recall: 0.9976\n  pass_f1: 0.9988\n  fail_precision: 0.9941\n  fail_recall: 1\n  fail_f1: 0.9971\n  train_loss: 0.1096\n  train_runtime_sec: 7507\n  epochs: 3\n  seed_comparison: {'seed42_accuracy': 0.9983, 'seed456_accuracy': 0.9983, 'seed123_accuracy': 0.9983, 'max_diff': 0, 'note': 'identical accuracy to 4 decimal places across all 3 seeds (42/456/123); each has exactly 2/1190 errors; exception_only fully seed-robust'}\n\n=== exception_only_seed456 ===\n  accuracy: 0.9983\n  accuracy_ci: [0.9958, 1]\n  majority_baseline: 0.7151\n  lift: 0.2832\n  n: 1190\n  pass_precision: 1\n  pass_recall: 0.9976\n  pass_f1: 0.9988\n  fail_precision: 0.9941\n  fail_recall: 1\n  fail_f1: 0.9971\n  vs_seed42: {'seed42_accuracy': 0.9983, 'seed456_accuracy': 0.9983, 'diff': 0, 'note': 'identical accuracy to 4 decimal places; no predictions.jsonl for paired bootstrap'}\n  train_loss: 0.1087\n  eval_loss: 0.4629\n  train_runtime_sec: 4541\n  epochs: 3\n\n=== vota_exception_only_seed42_v2 ===\n  accuracy: 0.9983\n  majority_baseline: 0.7151\n  lift: 0.2832\n  n: 1190\n  pass_precision: 1\n  pass_recall: 0.998\n  pass_f1: 0.999\n  fail_precision: 0.994\n  fail_recall: 1\n  fail_f1: 0.997\n  lift_vs_notrace: 0.2471\n  lift_vs_notrace_ci_lower: 0.2227\n  lift_vs_notrace_ci_upper: 0.2714\n  lift_vs_fulltrace: 0.1807\n  lift_vs_fulltrace_ci_lower: 0.1588\n  lift_vs_fulltrace_ci_upper: 0.2034\n  lift_vs_vota: 0.0067\n  lift_vs_vota_ci_lower: 0.0017\n  lift_vs_vota_ci_upper: 0.0126\n  lift_vs_vota_pvalue: 0.01\n\n=== full_trace_label_only_seed42 ===\n  accuracy: 0.8622\n  accuracy_ci_lower: 0.8437\n  accuracy_ci_upper: 0.8807\n  majority_baseline: 0.7151\n  lift: 0.1471\n  n: 1190\n  pass_precision: 0.8821\n  pass_recall: 0.9318\n  pass_f1: 0.9063\n  fail_precision: 0.8007\n  fail_recall: 0.6873\n  fail_f1: 0.7397\n  train_loss: 0.2505\n  eval_loss: 0.3205\n  lift_vs_notrace: 0.1109\n  lift_vs_notrace_ci_lower: 0.0849\n  lift_vs_notrace_ci_upper: 0.137\n  lift_vs_standard_fulltrace: 0.0445\n  lift_vs_standard_fulltrace_ci_lower: 0.0235\n  lift_vs_standard_fulltrace_ci_upper: 0.0655\n  lift_vs_standard_fulltrace_pvalue: 0\n\n=== vota_no_ae_seed42 ===\n  accuracy: 0.994\n  majority_baseline: 0.7151\n  lift: 0.279\n  n: 1190\n  pass_f1: 0.996\n  fail_f1: 0.989\n  accuracy_ci_lower: 0.989\n  accuracy_ci_upper: 0.998\n  lift_vs_notrace: 0.243\n  lift_vs_notrace_ci_lower: 0.218\n  lift_vs_notrace_ci_upper: 0.268\n  train_loss: 0.0908\n  eval_loss: 0.2215\n  wall_clock_seconds: 6397.88\n\n=== vota_loop_only_seed42 ===\n  accuracy: 0.8563\n  majority_baseline: 0.7151\n  lift: 0.1412\n  n: 1190\n  pass_precision: 0.9239\n  pass_recall: 0.8707\n  pass_f1: 0.8966\n  fail_precision: 0.7165\n  fail_recall: 0.8201\n  fail_f1: 0.7648\n  accuracy_ci: [0.8353, 0.8756]\n  bootstrap_vs_no_trace: {'diff': 0.105, 'ci': [0.0824, 0.1286], 'significant': True}\n  bootstrap_vs_vota: {'diff': -0.1378, 'ci': [-0.1571, -0.1185], 'significant': True}\n  bootstrap_vs_full_trace: {'diff': 0.0387, 'ci': [0.0185, 0.0597], 'significant': True}\n  train_loss: 0.0718\n  wall_clock_seconds: 7425.65\n\n=== vota_ae_only_seed42 ===\n  accuracy: 0.9992\n  accuracy_ci: [0.9975, 1]\n  bootstrap_pairwise: {'ae_only_vs_no_trace': {'diff': 0.2479, 'ci': [0.2235, 0.2731], 'p_value': 0, 'significant': True}, 'ae_only_vs_exception_only': {'diff': 0.0008, 'ci': [-0.0017, 0.0034], 'p_value': 0.8002, 'significant': False}, 'ae_only_vs_vota': {'diff': 0.005, 'ci': [0.0017, 0.0092], 'p_value': 0.0046, 'significant': True}}\n  config: {'n_bootstrap': 10000, 'seed': 42, 'method': 'paired_bootstrap'}\n\n=== full_trace_seed42_v5 ===\n  accuracy: 0.8176\n  majority_baseline: 0.7151\n  lift: 0.1025\n  n: 1190\n  pass_precision: 0.8774\n  pass_recall: 0.866\n  pass_f1: 0.8717\n  fail_precision: 0.6743\n  fail_recall: 0.6962\n  fail_f1: 0.6851\n  accuracy_ci_lower: 0.797\n  accuracy_ci_upper: 0.839\n  lift_vs_notrace: 0.0664\n  lift_vs_notrace_ci_lower: 0.0437\n  lift_vs_notrace_ci_upper: 0.0899\n  train_loss: 0.05\n  eval_loss: 0.0867\n  wall_clock_seconds: 7852\n  epoch_level: {'epoch1_accuracy': 0.8303, 'epoch2_accuracy': 0.763, 'final_accuracy': 0.8176, 'trend': 'non_monotonic_epoch1_best_epoch2_collapse'}\n\n=== no_trace_seed42_v5 ===\n  accuracy: 0.7513\n  accuracy_ci_lower: 0.7277\n  accuracy_ci_upper: 0.7748\n  majority_baseline: 0.7151\n  lift: 0.0361\n  lift_ci_lower: 0.0042\n  lift_ci_upper: 0.0706\n  n: 1190\n  pass_precision: 0.8776\n  pass_recall: 0.7579\n  pass_f1: 0.8134\n  fail_precision: 0.5473\n  fail_recall: 0.7345\n  fail_f1: 0.6272\n  epoch_level: {'epoch1_accuracy': 0.7429, 'epoch2_accuracy': 0.763, 'final_accuracy': 0.7513, 'trend': 'non_monotonic_epoch2_best'}\n\n=== vota_seed42_v5 ===\n  accuracy: 0.9941\n  majority_baseline: 0.7151\n  lift: 0.279\n  n: 1190\n  pass_precision: 1\n  pass_recall: 0.9882\n  pass_f1: 0.9941\n  fail_precision: 0.9714\n  fail_recall: 1\n  fail_f1: 0.9855\n  lift_vs_notrace: 0.2428\n  lift_vs_notrace_ci_lower: 0.2185\n  lift_vs_notrace_ci_upper: 0.2681\n  accuracy_ci_lower: 0.9882\n  accuracy_ci_upper: 0.9983\n  train_loss: 0.05\n  eval_loss: 0.0867\n  eval_mean_token_accuracy: 0.9828\n  wall_clock_seconds: 8443\n  epoch_level: {'epoch1_accuracy': 0.9933, 'epoch2_accuracy': 0.9941, 'final_accuracy': 0.9941, 'trend': 'monotonic_increasing_then_stable'}\n\n=== calibration_analysis_seed42 ===\n  no_trace: {'ece': 0.171476, 'mce': 0.475643, 'brier_score': 0.197152, 'accuracy': 0.751261, 'n_samples': 1190}\n  full_trace: {'ece': 0.095817, 'mce': 0.249061, 'brier_score': 0.143924, 'accuracy': 0.817647, 'n_samples': 1190}\n  label_only: {'ece': 0.110686, 'mce': 0.417124, 'brier_score': 0.120144, 'accuracy': 0.862185, 'n_samples': 1190}\n  loop_only: {'ece': 0.083085, 'mce': 0.183406, 'brier_score': 0.118335, 'accuracy': 0.856303, 'n_samples': 1190}\n  ae_only: {'ece': 0.000415, 'mce': 0.000415, 'brier_score': 0.000847, 'accuracy': 0.99916, 'n_samples': 1190}\n  exception_only: {'ece': 0.002717, 'mce': 0.835484, 'brier_score': 0.001311, 'accuracy': 0.998319, 'n_samples': 1190}\n  vota: {'ece': 0.00541, 'mce': 0.622459, 'brier_score': 0.005234, 'accuracy': 0.994118, 'n_samples': 1190}\n\n=== vota_seed42_v4 ===\n  accuracy: 0.9563\n  majority_baseline: 0.7151\n  lift: 0.2412\n  n: 1190\n  pass_precision: 0.944\n  pass_recall: 0.998\n  pass_f1: 0.97\n  fail_precision: 0.993\n  fail_recall: 0.853\n  fail_f1: 0.917\n  lift_vs_notrace: 0.205\n  lift_vs_notrace_ci_lower: 0.177\n  lift_vs_notrace_ci_upper: 0.234\n  train_loss: 0.046\n  eval_loss: 0.0842\n\n=== no_trace_seed42_v4 ===\n  accuracy: 0.7513\n  majority_baseline: 0.7151\n  lift: 0.0361\n  pass_precision: 0.8776\n  pass_recall: 0.7579\n  pass_f1: 0.8134\n  fail_precision: 0.5473\n  fail_recall: 0.7345\n  fail_f1: 0.6272\n  train_loss: 0.18\n  eval_loss: 0.6454\n  eval_mean_token_accuracy: 0.8897",
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

_source line 28_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data. Let me also check if there are more experiments I need, particularly for deepseek_exception_only_seed123, deepseek_no_trace_seed42, codellama13b entries, etc. Let me also look for any additional experiments I might have missed.

Let me compile all the data needed:

**Table 1 — Model × Condition (7B default = Qwen-2.5-Coder-7B)**

For Qwen-2.5-Coder-7B (main model):


I'm pulling together the performance metrics for each condition—no trace, full trace, loop only, exception only, and the combined VOTA approach—with their respective confidence intervals across the seed42 experiments. Now I'm looking at the remaining results for DeepSeek-Coder-6.7B and CodeLlama-13B, checking which experiments completed successfully. I notice the DeepSeek no_trace experiment doesn't appear in the data, so I'll mark that as incomplete. The CodeLlama results are starting to come through with the no_trace baseline at 76.50%.

I'm also compiling a seed robustness table to see how consistent the exception_only and ae_only approaches are across different random seeds. The exception_only method shows perfect consistency at 99.83% across all three seeds, while ae_only is showing some variation between seed42 at 99.92% and seed123 at 99.08%.

Now I'm working through the loop_only results across the three seeds and calculating the mean performance and standard deviation to quantify the variability.

Continuing with the label_only configuration, I'm computing the same statistics across its three seed runs, which shows slightly higher mean performance at 86.39% with comparable variance. For the VOTA model, I'm starting to compile results but notice some data points are missing from the dataset. as "—"
- seed456: vota_seed456_v2 → 99.08%
- Wait, I see seed42 and seed456. Let me check for seed123... I don't see a vota_seed123 experiment. 
  - Actually let me check vota_seed456_v2 accuracy: 99.08%
  - Mean of 2 seeds: (99.41 + 99.08)/2 = 99.25% but this is only 2 seeds.

Hmm, let me reconsider. The task says:
- Seed Robustness table: rows = conditions (exception_only, ae_only, loop_only, label_only, VOTA)
- Columns = seed42, seed123, seed456, Mean ± σ

For VOTA:
- seed42: 99.41%
- seed456: 99.08%
- seed123 isn't available, so I'm working with just two seeds for the mean.

Now I'm looking at the cross-dataset results on DebugBench. The no_trace baseline gets 96.71%, exception_only jumps to 100%, and VOTA lands at 99.77%, all notably higher than the MBPPplus baseline. I'm also checking the marker ablation for Qwen-7B where exception_only with markers reaches 99.83% but drops to 96.55% without them. Now I'm looking at the regex baseline results and comparing each approach against the SFT model's 99.83% performance. The format marker baseline (B5) comes closest at 99.33%, creating only a 0.5 percentage point gap, while the traceback-only approach (B2) performs worst at 71.51%, leaving a 28.32 point deficit.

I'm also tracking which experiments have confidence intervals and which don't—the exception_only approach across models consistently shows strong performance with explicit CI ranges, while some other variants like the no_trace and full_trace results for Qwen are missing their confidence bounds. Let me continue checking what CI data I have for the remaining models.

For the DeepSeek seed robustness, I'm seeing that seed42 and seed456 both hit 99.33%, but I need to verify the seed123 result—it looks like there's a seed_comparison field embedded in one of the results that shows seed123 achieved 91.09%, which is notably lower than the other seeds. I'm realizing the seed robustness table should only include Qwen-7B experiments, and I'm seeing a pattern across the exception_only, ae_only, and loop_only variants where each has three seed versions (42, 123, 456).

Now I need to verify the accuracy calculations for the ae_only experiments and compute the mean and standard deviation across those seeds. I'm finishing the ae_only calculation, then moving through the remaining conditions. For loop_only, the mean is 86.05% with a standard deviation of 0.53%, and label_only shows a mean of 86.39% with 0.60% variation. Now I'm looking at the VOTA results.

For VOTA, I only have two seed values available (99.41 and 99.08), giving a mean of 99.25% with a standard deviation of 0.23%. Now I need to compile the confidence intervals for Table 1, starting with the Qwen-7B results where no_trace is 75.13% with bounds of [72.77, 77.48], and I'm working through the full_trace values next. Now I'm looking at the performance metrics for the remaining models and realizing I need to compute Wilson confidence intervals for all the cells to match the table format requirement, rather than leaving some blank. Generating the confidence intervals...

Now I'm noticing the task specifies Δ as the difference between the with_markers and without_markers conditions. For Qwen-7B that's a 3.28 percentage point drop, and for Qwen-1.5B it's 2.03 percentage points. I have everything I need to compile the full results table.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a270429-54da-4381-97e3-905a06c925c1",
  "uuid": "acfacc39-4a4b-451d-9ac8-e0f860b0b3ce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0116iz6hm5kdhxhDjG3Kv6AZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7298,
      "cache_read_input_tokens": 27483,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7298
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

_source line 29_

Got all 39 experiments. Let me compute missing CIs and compile the tables.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a270429-54da-4381-97e3-905a06c925c1",
  "uuid": "f45c1b6c-0477-4808-a054-ede16ccee0bf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0116iz6hm5kdhxhDjG3Kv6AZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7298,
      "cache_read_input_tokens": 27483,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7298
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

_source line 30_

<details open><summary>🔧 Tool call — Bash · `toolu_01AtdvtqLRGodAEsfJVVSqFW`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport math\n\ndef wilson_ci(p, n, z=1.96):\n    denom = 1 + z**2/n\n    center = (p + z**2/(2*n)) / denom\n    margin = z * math.sqrt(p*(1-p)/n + z**2/(4*n**2)) / denom\n    lo = max(0, center - margin)\n    hi = min(1, center + margin)\n    return (round(lo*100, 2), round(hi*100, 2))\n\n# Missing CIs\ncases = {\n    \"qwen15b_no_trace\": (0.6731, 1190),\n    \"qwen15b_full_trace\": (0.7706, 1190),\n    \"qwen15b_vota\": (0.9958, 1190),\n    \"deepseek_exception_only\": (0.9933, 1190),\n    \"codellama_exception_only\": (0.9983, 1190),\n    \"debugbench_no_trace\": (0.9671, 426),\n    \"debugbench_vota\": (0.9977, 426),\n}\n\nfor name, (p, n) in cases.items():\n    lo, hi = wilson_ci(p, n)\n    print(f\"{name}: {p*100:.2f}% [{lo:.2f}, {hi:.2f}]\")\n\n# Seed robustness stats\nimport statistics\nprint(\"\\n=== Seed Robustness ===\")\nseeds = {\n    \"exception_only\": [99.83, 99.83, 99.83],\n    \"ae_only\": [99.92, 99.08, 99.92],\n    \"loop_only\": [85.63, 85.88, 86.64],\n    \"label_only\": [86.22, 87.06, 85.90],\n    \"VOTA\": [99.41, None, 99.08],  # seed123 missing\n}\nfor name, vals in seeds.items():\n    clean = [v for v in vals if v is not None]\n    mean = statistics.mean(clean)\n    if len(clean) > 1:\n        std = statistics.stdev(clean)\n    else:\n        std = 0\n    print(f\"{name}: mean={mean:.2f}, std={std:.2f} (n={len(clean)})\")\n\nPYEOF",
  "description": "Compute missing Wilson CIs and seed stats"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a270429-54da-4381-97e3-905a06c925c1",
  "uuid": "9852460f-3e9a-437f-ad64-41c1017c8a9b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0116iz6hm5kdhxhDjG3Kv6AZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7298,
      "cache_read_input_tokens": 27483,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7298
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

_source line 31 · 2026-05-16T17:54:51.091Z_

<details><summary>↩ Tool result · `toolu_01AtdvtqLRGodAEsfJVVSqFW`</summary>

```text
qwen15b_no_trace: 67.31% [64.59, 69.92]
qwen15b_full_trace: 77.06% [74.59, 79.36]
qwen15b_vota: 99.58% [99.02, 99.82]
deepseek_exception_only: 99.33% [98.68, 99.66]
codellama_exception_only: 99.83% [99.39, 99.95]
debugbench_no_trace: 96.71% [94.56, 98.03]
debugbench_vota: 99.77% [98.69, 99.96]

=== Seed Robustness ===
exception_only: mean=99.83, std=0.00 (n=3)
ae_only: mean=99.64, std=0.48 (n=3)
loop_only: mean=86.05, std=0.53 (n=3)
label_only: mean=86.39, std=0.60 (n=3)
VOTA: mean=99.25, std=0.23 (n=2)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4a270429-54da-4381-97e3-905a06c925c1",
  "uuid": "83b7574a-b319-420b-99ae-5c84ef3234e7",
  "tool_use_result": {
    "stdout": "qwen15b_no_trace: 67.31% [64.59, 69.92]\nqwen15b_full_trace: 77.06% [74.59, 79.36]\nqwen15b_vota: 99.58% [99.02, 99.82]\ndeepseek_exception_only: 99.33% [98.68, 99.66]\ncodellama_exception_only: 99.83% [99.39, 99.95]\ndebugbench_no_trace: 96.71% [94.56, 98.03]\ndebugbench_vota: 99.77% [98.69, 99.96]\n\n=== Seed Robustness ===\nexception_only: mean=99.83, std=0.00 (n=3)\nae_only: mean=99.64, std=0.48 (n=3)\nloop_only: mean=86.05, std=0.53 (n=3)\nlabel_only: mean=86.39, std=0.60 (n=3)\nVOTA: mean=99.25, std=0.23 (n=2)",
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

_source line 32_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01DmaxpCyRJ25qWJes3k4rxz`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
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
  "session_id": "4a270429-54da-4381-97e3-905a06c925c1",
  "uuid": "aa3593fe-9626-47bc-a088-5560311fc60a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M2W6BzxhxEv8B1783LjvBh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5906,
      "cache_read_input_tokens": 34781,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5906
      },
      "output_tokens": 40,
      "service_tier": "standard",
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

_source line 33 · 2026-05-16T17:54:54.620Z_

<details><summary>↩ Tool result · `toolu_01DmaxpCyRJ25qWJes3k4rxz`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
}
```

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
  "session_id": "4a270429-54da-4381-97e3-905a06c925c1",
  "uuid": "768ffb26-7c03-4e90-97ac-0e6c469bbdad",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Assistant

_source line 34_

Now let me write the comprehensive results table.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a270429-54da-4381-97e3-905a06c925c1",
  "uuid": "d77cf307-e0c3-4ddf-8cfc-e2b7ce4560e9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BsosBS7AiRjcqXSjYq53Ja",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 976,
      "cache_read_input_tokens": 40687,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 976
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

_source line 35_

<details open><summary>🔧 Tool call — Write · `toolu_01HPTRtcF1NCnpwKvPPX59hL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/comprehensive_results_table.md",
  "content": "# Comprehensive Experiment Results — Trace-Verdict Study\n\n> Compiled: 2026-05-16 | All results from registry (status=DONE, conclusion=success)\n> Dataset: MBPP+ (n=1190) unless noted | Metric: accuracy % [95% Wilson CI]\n\n---\n\n## Table 1 — Model × Condition (Primary Results)\n\n| Model | no_trace | full_trace | label_only | loop_only | exception_only | ae_only | VOTA |\n|:------|:--------:|:----------:|:----------:|:---------:|:--------------:|:-------:|:----:|\n| **Qwen-2.5-Coder-7B** | 75.13 [72.77, 77.48] | 81.76 [79.70, 83.90] | 86.22 [84.37, 88.07] | 85.63 [83.53, 87.56] | 99.83 [99.58, 100.00] | 99.92 [99.75, 100.00] | 99.41 [98.82, 99.83] |\n| **Qwen-2.5-Coder-1.5B** | 67.31 [64.59, 69.92] | 77.06 [74.59, 79.36] | — | — | 99.83 [99.58, 100.00] | — | 99.58 [99.02, 99.82] |\n| **DeepSeek-Coder-6.7B** | — | 79.16 [76.80, 81.30] | — | — | 99.33 [98.68, 99.66] | — | 84.45 [82.60, 86.40] |\n| **CodeLlama-13B** | 76.50 [73.80, 78.70] | — | — | — | 99.83 [99.39, 99.95] | — | — |\n\n**Key observations:**\n- exception_only achieves ≥99.33% across all 4 models\n- VOTA degraded on DeepSeek (84.45%) due to max_length=2048 truncation (verified)\n- DeepSeek full_trace also impacted by truncation (79.16%)\n\n---\n\n## Table 2 — Seed Robustness (Qwen-2.5-Coder-7B, MBPP+)\n\n| Condition | seed42 | seed123 | seed456 | Mean ± σ |\n|:----------|:------:|:-------:|:-------:|:--------:|\n| **exception_only** | 99.83 | 99.83 | 99.83 | 99.83 ± 0.00 |\n| **ae_only** | 99.92 | 99.08 | 99.92 | 99.64 ± 0.48 |\n| **VOTA** | 99.41 | — | 99.08 | 99.25 ± 0.23 |\n| **label_only** | 86.22 | 87.06 | 85.90 | 86.39 ± 0.60 |\n| **loop_only** | 85.63 | 85.88 | 86.64 | 86.05 ± 0.53 |\n\n**Key observations:**\n- exception_only: perfectly seed-robust (identical 99.83% across 3 seeds, each with exactly 2/1190 errors)\n- ae_only: near-perfect; seed123 slightly lower (99.08%) but still >99%\n- loop_only and label_only: stable within ~1pp\n\n---\n\n## Table 3 — Cross-Dataset Generalization (DebugBench, n=426)\n\n| Condition | DebugBench Acc | n | MBPP+ Acc | Δ (DB − MBPP+) |\n|:----------|:--------------:|:---:|:---------:|:---------------:|\n| **no_trace** | 96.71 [94.56, 98.03] | 426 | 75.13 | +21.58 |\n| **exception_only** | 100.00 [99.14, 100.00] | 426 | 99.83 | +0.17 |\n| **VOTA** | 99.77 [98.69, 99.96] | 426 | 99.41 | +0.36 |\n\n**Key observations:**\n- DebugBench has balanced labels (majority baseline 51.41% vs MBPP+ 71.51%), making no_trace much easier\n- exception_only and VOTA both transfer perfectly (≥99.77%)\n\n---\n\n## Table 4 — Format Marker Ablation (Nomarker)\n\n| Model | with_markers | without_markers | Δ |\n|:------|:------------:|:---------------:|:---:|\n| **Qwen-2.5-Coder-7B** | 99.83 | 96.55 [95.50, 97.60] | −3.28 |\n| **Qwen-2.5-Coder-1.5B** | 99.83 | 97.80 [97.00, 98.60] | −2.03 |\n\n**Key observations:**\n- Removing format markers costs 2–3pp; models still achieve >96% without them\n- Smaller model (1.5B) is less affected by marker removal\n\n---\n\n## Table 5 — Regex Baseline Comparison (MBPP+, n=1190)\n\n| Baseline | Accuracy | vs SFT Gap |\n|:---------|:--------:|:----------:|\n| B1: ERROR keyword presence | 93.45 | −6.38 |\n| B2: Traceback presence | 71.51 | −28.32 |\n| B3: Any error keyword | 93.45 | −6.38 |\n| B4: Exception type match | 93.61 | −6.22 |\n| B5: Format marker match | 99.33 | −0.50 |\n| B6: Error count ≥ 2 | 92.02 | −7.81 |\n| **SFT (exception_only)** | **99.83** | **ref** |\n\n**Key observations:**\n- Best regex (B5: format marker) reaches 99.33% — only 0.50pp below SFT\n- B5 vs SFT: McNemar p = 0.041 (significant at α=0.05)\n- B2 (Traceback presence) equals majority baseline (71.51%), providing no discriminative value\n\n---\n\n## Supplementary: DeepSeek Seed Comparison (exception_only)\n\n| Seed | Accuracy | Note |\n|:-----|:--------:|:-----|\n| seed42 | 99.33 | |\n| seed123 | 91.09 | outlier |\n| seed456 | 99.33 | |\n| **Mean ± σ** | **96.58 ± 4.76** | 2/3 seeds robust; seed123 anomalous |\n\n---\n\n## Supplementary: Per-Condition Lift vs no_trace (Qwen-7B)\n\n| Condition | Accuracy | Lift vs no_trace | 95% CI of lift |\n|:----------|:--------:|:----------------:|:--------------:|\n| no_trace | 75.13 | ref | — |\n| full_trace | 81.76 | +6.64 | [4.37, 8.99] |\n| label_only | 86.22 | +11.09 | [8.49, 13.70] |\n| loop_only | 85.63 | +10.50 | [8.24, 12.86] |\n| VOTA | 99.41 | +24.28 | [21.85, 26.81] |\n| ae_only | 99.92 | +24.79 | [22.35, 27.31] |\n| exception_only | 99.83 | +24.71 | [22.27, 27.14] |\n\n---\n\n## Supplementary: Calibration (Qwen-7B, seed42)\n\n| Condition | ECE ↓ | MCE ↓ | Brier ↓ |\n|:----------|:-----:|:-----:|:-------:|\n| no_trace | 0.1715 | 0.4756 | 0.1972 |\n| full_trace | 0.0958 | 0.2491 | 0.1439 |\n| label_only | 0.1107 | 0.4171 | 0.1201 |\n| loop_only | 0.0831 | 0.1834 | 0.1183 |\n| exception_only | 0.0027 | 0.8355 | 0.0013 |\n| ae_only | 0.0004 | 0.0004 | 0.0008 |\n| VOTA | 0.0054 | 0.6225 | 0.0052 |\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a270429-54da-4381-97e3-905a06c925c1",
  "uuid": "4e6f3b64-a810-48a9-af7f-74dac87de765",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BsosBS7AiRjcqXSjYq53Ja",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 976,
      "cache_read_input_tokens": 40687,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 976
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

_source line 36 · 2026-05-16T17:55:34.235Z_

<details><summary>↩ Tool result · `toolu_01HPTRtcF1NCnpwKvPPX59hL`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/comprehensive_results_table.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4a270429-54da-4381-97e3-905a06c925c1",
  "uuid": "725fbd04-57af-486c-bdd1-c5c5fc0c8490",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/comprehensive_results_table.md",
    "content": "# Comprehensive Experiment Results — Trace-Verdict Study\n\n> Compiled: 2026-05-16 | All results from registry (status=DONE, conclusion=success)\n> Dataset: MBPP+ (n=1190) unless noted | Metric: accuracy % [95% Wilson CI]\n\n---\n\n## Table 1 — Model × Condition (Primary Results)\n\n| Model | no_trace | full_trace | label_only | loop_only | exception_only | ae_only | VOTA |\n|:------|:--------:|:----------:|:----------:|:---------:|:--------------:|:-------:|:----:|\n| **Qwen-2.5-Coder-7B** | 75.13 [72.77, 77.48] | 81.76 [79.70, 83.90] | 86.22 [84.37, 88.07] | 85.63 [83.53, 87.56] | 99.83 [99.58, 100.00] | 99.92 [99.75, 100.00] | 99.41 [98.82, 99.83] |\n| **Qwen-2.5-Coder-1.5B** | 67.31 [64.59, 69.92] | 77.06 [74.59, 79.36] | — | — | 99.83 [99.58, 100.00] | — | 99.58 [99.02, 99.82] |\n| **DeepSeek-Coder-6.7B** | — | 79.16 [76.80, 81.30] | — | — | 99.33 [98.68, 99.66] | — | 84.45 [82.60, 86.40] |\n| **CodeLlama-13B** | 76.50 [73.80, 78.70] | — | — | — | 99.83 [99.39, 99.95] | — | — |\n\n**Key observations:**\n- exception_only achieves ≥99.33% across all 4 models\n- VOTA degraded on DeepSeek (84.45%) due to max_length=2048 truncation (verified)\n- DeepSeek full_trace also impacted by truncation (79.16%)\n\n---\n\n## Table 2 — Seed Robustness (Qwen-2.5-Coder-7B, MBPP+)\n\n| Condition | seed42 | seed123 | seed456 | Mean ± σ |\n|:----------|:------:|:-------:|:-------:|:--------:|\n| **exception_only** | 99.83 | 99.83 | 99.83 | 99.83 ± 0.00 |\n| **ae_only** | 99.92 | 99.08 | 99.92 | 99.64 ± 0.48 |\n| **VOTA** | 99.41 | — | 99.08 | 99.25 ± 0.23 |\n| **label_only** | 86.22 | 87.06 | 85.90 | 86.39 ± 0.60 |\n| **loop_only** | 85.63 | 85.88 | 86.64 | 86.05 ± 0.53 |\n\n**Key observations:**\n- exception_only: perfectly seed-robust (identical 99.83% across 3 seeds, each with exactly 2/1190 errors)\n- ae_only: near-perfect; seed123 slightly lower (99.08%) but still >99%\n- loop_only and label_only: stable within ~1pp\n\n---\n\n## Table 3 — Cross-Dataset Generalization (DebugBench, n=426)\n\n| Condition | DebugBench Acc | n | MBPP+ Acc | Δ (DB − MBPP+) |\n|:----------|:--------------:|:---:|:---------:|:---------------:|\n| **no_trace** | 96.71 [94.56, 98.03] | 426 | 75.13 | +21.58 |\n| **exception_only** | 100.00 [99.14, 100.00] | 426 | 99.83 | +0.17 |\n| **VOTA** | 99.77 [98.69, 99.96] | 426 | 99.41 | +0.36 |\n\n**Key observations:**\n- DebugBench has balanced labels (majority baseline 51.41% vs MBPP+ 71.51%), making no_trace much easier\n- exception_only and VOTA both transfer perfectly (≥99.77%)\n\n---\n\n## Table 4 — Format Marker Ablation (Nomarker)\n\n| Model | with_markers | without_markers | Δ |\n|:------|:------------:|:---------------:|:---:|\n| **Qwen-2.5-Coder-7B** | 99.83 | 96.55 [95.50, 97.60] | −3.28 |\n| **Qwen-2.5-Coder-1.5B** | 99.83 | 97.80 [97.00, 98.60] | −2.03 |\n\n**Key observations:**\n- Removing format markers costs 2–3pp; models still achieve >96% without them\n- Smaller model (1.5B) is less affected by marker removal\n\n---\n\n## Table 5 — Regex Baseline Comparison (MBPP+, n=1190)\n\n| Baseline | Accuracy | vs SFT Gap |\n|:---------|:--------:|:----------:|\n| B1: ERROR keyword presence | 93.45 | −6.38 |\n| B2: Traceback presence | 71.51 | −28.32 |\n| B3: Any error keyword | 93.45 | −6.38 |\n| B4: Exception type match | 93.61 | −6.22 |\n| B5: Format marker match | 99.33 | −0.50 |\n| B6: Error count ≥ 2 | 92.02 | −7.81 |\n| **SFT (exception_only)** | **99.83** | **ref** |\n\n**Key observations:**\n- Best regex (B5: format marker) reaches 99.33% — only 0.50pp below SFT\n- B5 vs SFT: McNemar p = 0.041 (significant at α=0.05)\n- B2 (Traceback presence) equals majority baseline (71.51%), providing no discriminative value\n\n---\n\n## Supplementary: DeepSeek Seed Comparison (exception_only)\n\n| Seed | Accuracy | Note |\n|:-----|:--------:|:-----|\n| seed42 | 99.33 | |\n| seed123 | 91.09 | outlier |\n| seed456 | 99.33 | |\n| **Mean ± σ** | **96.58 ± 4.76** | 2/3 seeds robust; seed123 anomalous |\n\n---\n\n## Supplementary: Per-Condition Lift vs no_trace (Qwen-7B)\n\n| Condition | Accuracy | Lift vs no_trace | 95% CI of lift |\n|:----------|:--------:|:----------------:|:--------------:|\n| no_trace | 75.13 | ref | — |\n| full_trace | 81.76 | +6.64 | [4.37, 8.99] |\n| label_only | 86.22 | +11.09 | [8.49, 13.70] |\n| loop_only | 85.63 | +10.50 | [8.24, 12.86] |\n| VOTA | 99.41 | +24.28 | [21.85, 26.81] |\n| ae_only | 99.92 | +24.79 | [22.35, 27.31] |\n| exception_only | 99.83 | +24.71 | [22.27, 27.14] |\n\n---\n\n## Supplementary: Calibration (Qwen-7B, seed42)\n\n| Condition | ECE ↓ | MCE ↓ | Brier ↓ |\n|:----------|:-----:|:-----:|:-------:|\n| no_trace | 0.1715 | 0.4756 | 0.1972 |\n| full_trace | 0.0958 | 0.2491 | 0.1439 |\n| label_only | 0.1107 | 0.4171 | 0.1201 |\n| loop_only | 0.0831 | 0.1834 | 0.1183 |\n| exception_only | 0.0027 | 0.8355 | 0.0013 |\n| ae_only | 0.0004 | 0.0004 | 0.0008 |\n| VOTA | 0.0054 | 0.6225 | 0.0052 |\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01GhQqzSZmHZtcHb35zeXm4r`</summary>

```json
{
  "name": "comprehensive_results_table",
  "type": "report",
  "description": "Full experiment results compilation: Table 1 (Model×Condition), Seed Robustness, DebugBench cross-dataset, Nomarker ablation, Regex baselines, Lift analysis, Calibration. 39 experiments, all DONE/success.",
  "project": "trace-verdict-study",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/comprehensive_results_table.md",
  "tags": [
    "results",
    "paper",
    "table1",
    "comprehensive"
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
  "session_id": "4a270429-54da-4381-97e3-905a06c925c1",
  "uuid": "57aede11-d962-402f-a9a5-e08f116b950c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YBnH988VWiTRWceJcz2Xg5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2451,
      "cache_read_input_tokens": 41663,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2451
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

_source line 38 · 2026-05-16T17:55:39.918Z_

<details><summary>↩ Tool result · `toolu_01GhQqzSZmHZtcHb35zeXm4r`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_e87c5a\", \"name\": \"comprehensive_results_table\", \"type\": \"report\", \"description\": \"Full experiment results compilation: Table 1 (Model×Condition), Seed Robustness, DebugBench cross-dataset, Nomarker ablation, Regex baselines, Lift analysis, Calibration. 39 experiments, all DONE/success.\", \"path\": \"projects/trace-verdict-study/artifacts/_project/report/comprehensive_results_table.md\", \"url\": null, \"project\": \"trace-verdict-study\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T17:55:39.804716+00:00\", \"tags\": [\"results\", \"paper\", \"table1\", \"comprehensive\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4a270429-54da-4381-97e3-905a06c925c1",
  "uuid": "ee3eafc1-e0f9-4563-be17-bd4ced630dee",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260516_e87c5a\\\", \\\"name\\\": \\\"comprehensive_results_table\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Full experiment results compilation: Table 1 (Model×Condition), Seed Robustness, DebugBench cross-dataset, Nomarker ablation, Regex baselines, Lift analysis, Calibration. 39 experiments, all DONE/success.\\\", \\\"path\\\": \\\"projects/trace-verdict-study/artifacts/_project/report/comprehensive_results_table.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"trace-verdict-study\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-16T17:55:39.804716+00:00\\\", \\\"tags\\\": [\\\"results\\\", \\\"paper\\\", \\\"table1\\\", \\\"comprehensive\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_e87c5a\", \"name\": \"comprehensive_results_table\", \"type\": \"report\", \"description\": \"Full experiment results compilation: Table 1 (Model×Condition), Seed Robustness, DebugBench cross-dataset, Nomarker ablation, Regex baselines, Lift analysis, Calibration. 39 experiments, all DONE/success.\", \"path\": \"projects/trace-verdict-study/artifacts/_project/report/comprehensive_results_table.md\", \"url\": null, \"project\": \"trace-verdict-study\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T17:55:39.804716+00:00\", \"tags\": [\"results\", \"paper\", \"table1\", \"comprehensive\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 39_

已写入并注册 `comprehensive_results_table.md` (art_20260516_e87c5a)。

包含 7 张表：
1. **Table 1** — 4 模型 × 7 条件，exception_only 全模型 ≥99.33%
2. **Seed Robustness** — exception_only 完美稳定 (σ=0.00)，loop_only/label_only σ<1pp
3. **DebugBench 跨数据集** — exception_only 100%，VOTA 99.77%
4. **Nomarker 消融** — 去 markers 损失 2–3pp
5. **Regex Baselines** — 最佳 regex (B5) 99.33%，与 SFT 差 0.50pp (p=0.041)
6. **Lift vs no_trace** — 含 bootstrap CI
7. **Calibration** — ae_only ECE 最低 (0.0004)

空缺格标 "—"，所有数字 2 位小数，CI 用 Wilson 区间补齐。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a270429-54da-4381-97e3-905a06c925c1",
  "uuid": "575f6bcd-603d-45d2-aeae-a7793e8362c9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017F3sKJfuDAuUr1HU9KY6J4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 567,
      "cache_read_input_tokens": 44114,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 567
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

已写入并注册 `comprehensive_results_table.md` (art_20260516_e87c5a)。

包含 7 张表：
1. **Table 1** — 4 模型 × 7 条件，exception_only 全模型 ≥99.33%
2. **Seed Robustness** — exception_only 完美稳定 (σ=0.00)，loop_only/label_only σ<1pp
3. **DebugBench 跨数据集** — exception_only 100%，VOTA 99.77%
4. **Nomarker 消融** — 去 markers 损失 2–3pp
5. **Regex Baselines** — 最佳 regex (B5) 99.33%，与 SFT 差 0.50pp (p=0.041)
6. **Lift vs no_trace** — 含 bootstrap CI
7. **Calibration** — ae_only ECE 最低 (0.0004)

空缺格标 "—"，所有数字 2 位小数，CI 用 Wilson 区间补齐。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 185438,
  "duration_api_ms": 185266,
  "num_turns": 15,
  "stop_reason": "end_turn",
  "session_id": "4a270429-54da-4381-97e3-905a06c925c1",
  "total_cost_usd": 0.7036454999999999,
  "usage": {
    "input_tokens": 21,
    "cache_creation_input_tokens": 32840,
    "cache_read_input_tokens": 430225,
    "output_tokens": 11249,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 32840,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 300,
        "cache_read_input_tokens": 44114,
        "cache_creation_input_tokens": 567,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 567
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1878,
      "outputTokens": 15,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0019529999999999999,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 21,
      "outputTokens": 11249,
      "cacheReadInputTokens": 430225,
      "cacheCreationInputTokens": 32840,
      "webSearchRequests": 0,
      "costUSD": 0.7016924999999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "ee769393-3c86-4487-8988-d3dd11b32244"
}
```

</details>

---
