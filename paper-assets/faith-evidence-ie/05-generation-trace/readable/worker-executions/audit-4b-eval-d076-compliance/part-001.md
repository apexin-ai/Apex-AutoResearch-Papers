# audit 4b eval d076 compliance — Part 1 of 2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Worker execution logs

[Transcript overview](../audit-4b-eval-d076-compliance.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/ee/ee9a169c2962b9d90944.json)

## Before a recorded user message

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
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
  "uuid": "c202a496-a3c3-43c9-91cd-e8b9633a5337",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/memory/"
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
    "resetsAt": 1779152400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "53401851-16da-446e-99cd-e2f4ec454444",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0"
}
```

---


### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the registry to get all experiments, then filter for 4B-related ones.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "9e7da629-5087-4972-9daf-dfe3cf6bf5ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WVit5x1Tzy86u5PpyFy451",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14240,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14240
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

读取 registry 并筛选 4B 相关实验。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "9354f3d0-38ea-485e-a8f6-02dac28161c7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WVit5x1Tzy86u5PpyFy451",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14240,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14240
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01KL5WGGvYFkV6SD7W2PhZww`</summary>

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
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "529df9ee-0e2c-4adf-b153-01e3c3a63e70",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WVit5x1Tzy86u5PpyFy451",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14240,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14240
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

_source line 7 · 2026-05-18T22:02:07.699Z_

<details><summary>↩ Tool result · `toolu_01KL5WGGvYFkV6SD7W2PhZww`</summary>

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
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "a6714246-77d2-41e1-95cd-4434330851ba",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_registry"
    ],
    "query": "select:mcp__agent-ml-research__read_registry",
    "total_deferred_tools": 26
  }
}
```

</details>

---


### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01RKy9Ay3nAfmmfZMXnBuJfV`</summary>

```json
{
  "project": "faith-evidence-ie",
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
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "bdae33e1-0c7b-4d5d-a32d-98c416bda16b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0157TYbJsTPg1xE2KeCrG4u9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 504,
      "cache_read_input_tokens": 25687,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 504
      },
      "output_tokens": 60,
      "service_tier": "standard",
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

_source line 9 · 2026-05-18T22:02:12.728Z_

<details><summary>↩ Tool result · `toolu_01RKy9Ay3nAfmmfZMXnBuJfV`</summary>

```text
Error: result (396,849 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/596d8411-63f5-4757-a2a4-2c57b1fcaba0/tool-results/mcp-agent-ml-research-read_registry-1779141732674.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/596d8411-63f5-4757-a2a4-2c57b1fcaba0/tool-results/mcp-agent-ml-research-read_registry-1779141732674.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/596d8411-63f5-4757-a2a4-2c57b1fcaba0/tool-results/mcp-agent-ml-research-read_registry-1779141732674.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "c80b6e70-2c57-47fe-b569-e49ff0053e15",
  "tool_use_result": {
    "content": "Error: result (396,849 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/596d8411-63f5-4757-a2a4-2c57b1fcaba0/tool-results/mcp-agent-ml-research-read_registry-1779141732674.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/596d8411-63f5-4757-a2a4-2c57b1fcaba0/tool-results/mcp-agent-ml-research-read_registry-1779141732674.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/596d8411-63f5-4757-a2a4-2c57b1fcaba0/tool-results/mcp-agent-ml-research-read_registry-1779141732674.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"wave1_sft_4b_s44_eval_r2\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T20:05:57.119Z\", \"updated_at\": \"2026-05-18T21:59:29.645Z\", \"hypothesis\": \"4B SFT seed44 eval r2 (corrected D076 command: --model_path=base --sft_adapter=adapter). Re-run of failed wave1_sft_4b_s44_eval. Expected rel_f1 ~50.5 based on canonical 4B SFT s42.\", \"parent\": \"wave1_sft_4b_s44\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=1 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output_seed44/ --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/wave1_sft_4b_s44_eval_r2\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"571192\", \"log_path\": \"~/runs/faith-evidence-ie/wave1_sft_4b_s44_eval_r2.log\", \"submitted_at\": \"2026-05-18T20:06:13.257Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + SFT-s44\", \"seed\": 42, \"checkpoint_source\": \"wave1_sft_4b_s44\", \"eval_data\": \"DocRED dev\", \"checkpoint_path\": \"/root/autodl-tmp/eval_results/wave1_sft_4b_s44_eval_r2\"}, \"reproduce\": {\"finished_at\": \"2026-05-18T21:59:27.684Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T21:59:33.106103+00:00\"}]}}, \"plan019_8b_sft_s44_eval\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T21:36:26.622Z\", \"updated_at\": \"2026-05-18T21:37:54.518Z\", \"hypothesis\": \"8B SFT s44 eval (D076 protocol): measure SFT baseline for seed44 at 8B scale. Paired with canonical s42 (ign_f1=0.5051) for 2-seed mean±std.\", \"parent\": \"plan019_8b_sft_s44\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen/Qwen3-8B --sft_adapter /root/autodl-tmp/sft_output_qwen3_8b_s44 --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/plan019_8b_sft_s44_eval\", \"server\": \"rtx5090-4x\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": -1, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/sft_output_qwen3_8b_s44\", \"eval_data\": \"docred-dev\"}}, \"wave1_sft_4b_s43_eval_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:29:28.052Z\", \"updated_at\": \"2026-05-18T21:34:25.964Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output_seed43/ --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/wave1_sft_4b_s43_eval_r2\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:2\"], \"pid\": \"568649\", \"log_path\": \"~/runs/faith-evidence-ie/wave1_sft_4b_s43_eval_r2.log\", \"submitted_at\": \"2026-05-18T19:29:27.427Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + SFT-s43\", \"seed\": 42, \"checkpoint_source\": \"wave1_sft_4b_s43\", \"eval_data\": \"DocRED dev\", \"wall_clock_seconds\": 7498.5, \"gpu_hours\": 2.08}, \"hypothesis\": \"4B SFT seed43 eval r2 (corrected D076 command: --model_path=base --sft_adapter=adapter). Re-run of failed wave1_sft_4b_s43_eval. Expected rel_f1 ~50.5 based on canonical 4B SFT s42.\", \"reproduce\": {\"finished_at\": \"2026-05-18T21:31:06.692Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T21:31:13.092816+00:00\"}]}, \"metrics\": {\"ign_f1\": 0.4365, \"rel_f1\": 0.4429, \"evi_f1_joint\": 0.3462, \"evi_f1_tp\": 0.8021, \"edcr\": 0.6827, \"format_compliance_rate\": 1, \"n_truncated\": 318, \"n_predictions\": 17055, \"inference_time_seconds\": 7157.9}, \"checkpoint_path\": \"/root/autodl-tmp/sft_output_seed43/\", \"log_path\": \"~/runs/faith-evidence-ie/wave1_sft_4b_s43_eval_r2.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T21:34:25.964Z\"}, \"plan019_1_7b_sft_s43_eval\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T20:33:55.681Z\", \"updated_at\": \"2026-05-18T20:34:15.653Z\", \"hypothesis\": \"Eval 1.7B SFT seed43 on DocRED dev set to measure RE performance. Paired with s42 for 2-seed mean±std at 1.7B scale.\", \"parent\": \"plan019_1_7b_sft_s43\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen/Qwen3-1.7B --sft_adapter /root/autodl-tmp/sft_output_qwen3_1_7b_bf16_seed43/ --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/plan019_1_7b_sft_s43_eval\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"573657\", \"log_path\": \"~/runs/faith-evidence-ie/plan019_1_7b_sft_s43_eval.log\", \"submitted_at\": \"2026-05-18T20:33:17Z\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"Qwen3-1.7B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/sft_output_qwen3_1_7b_bf16_seed43/\", \"eval_data\": \"docred-dev\"}}, \"plan019_8b_sft_s44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:24:16.330Z\", \"updated_at\": \"2026-05-18T20:32:15.073Z\", \"hypothesis\": \"8B Qwen3 SFT seed44: scaling seeds for statistical robustness. Paired with canonical s42 for 2-seed mean±std at 8B scale. Expected train_loss similar to canonical 8B SFT.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && GPU=0 bash scripts/seed_expansion/sft_8b_s44.sh\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"567982\", \"log_path\": \"~/runs/faith-evidence-ie/plan019_8b_sft_s44.log\", \"submitted_at\": \"2026-05-18T19:24:19.125Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred/train_annotated.json\", \"data_count\": 3027, \"model_name\": \"Qwen3-8B\", \"seed\": 44, \"wall_clock_seconds\": 4067.4, \"gpu_hours\": 1.13}, \"reproduce\": {\"finished_at\": \"2026-05-18T20:28:38.339Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T20:28:43.289104+00:00\"}]}, \"metrics\": {\"train_loss\": 0.5691, \"eval_loss\": 0.7196, \"eval_mean_token_accuracy\": 0.8379, \"eval_entropy\": 0.5579, \"train_runtime_s\": 3823.89, \"epoch\": 3}, \"checkpoint_path\": \"/root/autodl-tmp/sft_output_qwen3_8b_s44\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T20:32:06.560Z\"}, \"plan019_1_7b_sft_s43_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:31:33.003Z\", \"updated_at\": \"2026-05-18T20:21:13.903Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && bash scripts/seed_expansion/sft_1_7b_s43.sh\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:2\"], \"pid\": \"569109\", \"log_path\": \"~/runs/faith-evidence-ie/plan019_1_7b_sft_s43_r2.log\", \"submitted_at\": \"2026-05-18T19:31:32.289Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred/train_annotated.json\", \"data_count\": 3027, \"model_name\": \"Qwen3-1.7B\", \"seed\": 43, \"wall_clock_seconds\": 2981.6, \"gpu_hours\": 0.83}, \"hypothesis\": \"1.7B SFT seed43 r2: third seed for 1.7B scaling robustness. s42 ign_f1=0.4786, s44 ign_f1=0.4321, variance=4.65pp is extreme. Third seed critical to determine if s44 is outlier or s42 is outlier.\", \"reproduce\": {\"finished_at\": \"2026-05-18T20:17:20.369Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T20:17:25.759133+00:00\"}]}, \"metrics\": {\"train_loss\": 0.6881, \"eval_loss\": 0.8029, \"eval_mean_token_accuracy\": 0.8237, \"eval_entropy\": 0.681, \"epochs\": 3, \"runtime_seconds\": 2697}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/sft_output_qwen3_1_7b_bf16_seed43\", \"completed_at\": \"2026-05-18T20:21:13.903Z\"}, \"grpo_bf16_g4_ckpt200_eval\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T20:05:54.201Z\", \"updated_at\": \"2026-05-18T20:09:44.868Z\", \"hypothesis\": \"GRPO bf16 G=4 checkpoint-200 eval (final): compare with ckpt-100 for D106 learning curve. If ckpt-200 > ckpt-100, GRPO is improving. Expected: rel_f1 improvement over ckpt-100.\", \"parent\": \"wave1_grpo_bf16_g4\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=3 python -m freige.eval.inference --model_path /root/autodl-tmp/grpo_bf16_g4/checkpoint-200 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output/ --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/grpo_bf16_g4_ckpt200_eval\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"571115\", \"log_path\": \"~/runs/faith-evidence-ie/grpo_bf16_g4_ckpt200_eval.log\", \"submitted_at\": \"2026-05-18T20:06:10.622Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + SFT + GRPO-bf16-G4-ckpt200\", \"seed\": 42, \"checkpoint_source\": \"wave1_grpo_bf16_g4\", \"eval_data\": \"DocRED dev\", \"checkpoint_path\": \"/root/autodl-tmp/eval_results/grpo_bf16_g4_ckpt200_eval\"}}, \"wave1_grpo_bf16_g4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T12:46:19.740Z\", \"updated_at\": \"2026-05-18T20:09:28.981Z\", \"hypothesis\": \"GRPO bf16 without quantization (G=4): prior GRPO runs used int4 quantization which may have caused training instability. bf16 full precision should provide clean GRPO signal. If GRPO improves over RSFT, validates Claim 2 (decoupling spectrum). Expected: rel_f1 > RSFT baseline (~52pp).\", \"spec\": {\"command\": \"bash /root/autodl-tmp/freige/scripts/d102_next_batch/grpo_bf16_g4.sh\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:2\"], \"pid\": 542121, \"data_path\": \"/root/autodl-tmp/data/docred/train_annotated.json\", \"data_count\": 3027, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"output_dir\": \"/root/autodl-tmp/grpo_bf16_g4\", \"log_path\": \"/root/autodl-tmp/grpo_bf16_g4.log\", \"method\": \"GRPO bf16 no-quantize\", \"num_generations\": 4, \"gradient_accumulation_steps\": 16, \"max_steps\": 200, \"kl_coef\": 0, \"reward_weights\": {\"format\": 0.3, \"f1\": 3, \"ced\": 1}, \"plan_id\": \"plan_015\"}, \"checkpoint_path\": \"/root/autodl-tmp/grpo_bf16_g4\", \"log_path\": \"/root/autodl-tmp/grpo_bf16_g4.log\", \"metrics\": {\"reward_mean\": 1.7646, \"steps_completed\": 200, \"max_steps\": 200}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T20:09:28.981Z\"}, \"random_rsft_k1_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:34:48.815Z\", \"updated_at\": \"2026-05-18T20:08:52.336Z\", \"hypothesis\": \"Random k=1 RSFT eval: if random selection significantly underperforms CED RSFT (gap > 1.5pp in rel_f1), proves CED scoring precision is the key differentiator. CED k=1 mean rel_f1=0.4596, expect random &lt; 0.445.\", \"parent\": \"random_rsft_k1_baseline\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_random_k1/checkpoint-1020 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output/ --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/random_rsft_k1_eval\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"558320\", \"log_path\": \"~/runs/faith-evidence-ie/random_rsft_k1_eval.log\", \"submitted_at\": \"2026-05-18T16:35:12.562Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + SFT + Random-RSFT-k1\", \"seed\": 42, \"checkpoint_source\": \"random_rsft_k1_baseline\", \"eval_data\": \"DocRED dev\", \"checkpoint_path\": \"/root/autodl-tmp/eval_results/random_rsft_k1_eval\", \"wall_clock_seconds\": 12819.8, \"gpu_hours\": 3.56}, \"metrics\": {\"ign_f1\": 0.4114, \"f1\": 0.4198, \"evi_f1\": 0.7964, \"evi_f1_joint\": 0.3216, \"EDCR\": 0.6971, \"format_compliance\": 0.999, \"field_compliance\": 0.7482, \"truncated\": 235, \"n_total\": 985, \"n_predictions\": 16110, \"inference_time_seconds\": 11778.5}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T20:08:52.336Z\"}, \"grpo_bf16_g4_ckpt100_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:34:51.597Z\", \"updated_at\": \"2026-05-18T20:08:50.166Z\", \"hypothesis\": \"GRPO bf16 G=4 checkpoint-100 eval (D106 conditional termination): evaluate mid-training checkpoint to decide whether to continue GRPO training to step 200. If rel_f1 >= RSFT baseline (~52pp), continue. If significantly below, consider early termination.\", \"parent\": \"wave1_grpo_bf16_g4\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=3 python -m freige.eval.inference --model_path /root/autodl-tmp/grpo_bf16_g4/checkpoint-100 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output/ --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/grpo_bf16_g4_ckpt100_eval\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"558467\", \"log_path\": \"~/runs/faith-evidence-ie/grpo_bf16_g4_ckpt100_eval.log\", \"submitted_at\": \"2026-05-18T16:35:15.818Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + SFT + GRPO-bf16-G4-ckpt100\", \"seed\": 42, \"checkpoint_source\": \"wave1_grpo_bf16_g4\", \"eval_data\": \"DocRED dev\", \"checkpoint_path\": \"/root/autodl-tmp/eval_results/grpo_bf16_g4_ckpt100_eval\", \"wall_clock_seconds\": 12814.3, \"gpu_hours\": 3.56}, \"metrics\": {\"ign_f1\": 0.4431, \"f1\": 0.4511, \"evi_f1\": 0.801, \"evi_f1_joint\": 0.3532, \"EDCR\": 0.6453, \"format_compliance\": 0.999, \"field_compliance\": 0.8142, \"truncated\": 182, \"n_total\": 985, \"n_predictions\": 15187, \"inference_time_seconds\": 11458.2}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T20:08:50.166Z\"}, \"plan019_1_7b_sft_s44_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:34:45.563Z\", \"updated_at\": \"2026-05-18T19:27:55.325Z\", \"hypothesis\": \"1.7B SFT seed44 eval (D076 protocol): measure baseline SFT performance for seed44 at 1.7B scale. Paired with canonical s42 for scaling seed robustness. Expected rel_f1 ~49.5 based on canonical 1.7B SFT.\", \"parent\": \"plan019_1_7b_sft_s44\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/eval_results/plan019_1_7b_sft_s44_eval\", \"log_path\": \"~/runs/faith-evidence-ie/plan019_1_7b_sft_s44_eval.log\"}, \"metrics\": {\"ign_f1\": 0.4321, \"f1\": 0.4441, \"evi_f1_tp\": 0.819, \"evi_f1_joint\": 0.3482, \"edcr\": 0.69, \"n_truncated\": 473, \"n_predictions\": 20237, \"n_documents\": 985, \"format_ok_rate\": 1, \"field_compliance_rate\": 0.5198, \"evidence_format_rate\": 0.5198, \"inference_time_seconds\": 6146}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T19:27:55.325Z\"}, \"plan019_1_7b_sft_s44\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T15:22:46.118Z\", \"updated_at\": \"2026-05-18T16:36:03.598Z\", \"hypothesis\": \"1.7B SFT seed44: scaling seeds for statistical robustness. Paired with canonical s42 and s43 for 3-seed mean±std at 1.7B scale. Expected train_loss ~0.70, rel_f1 ~49.5 based on canonical 1.7B SFT.\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/sft_output_qwen3_1_7b_bf16_seed44/\", \"log_path\": \"/root/autodl-tmp/sft_output_qwen3_1_7b_bf16_seed44/training.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-18T16:27:09.983Z\"}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.5783, \"eval_loss\": 0.8037, \"eval_mean_token_accuracy\": 0.8238, \"global_steps\": 570, \"epochs\": 3}}, \"random_rsft_k1_baseline\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T13:32:46.287Z\", \"updated_at\": \"2026-05-18T16:34:56.854Z\", \"hypothesis\": \"Random k=1 RSFT baseline: same candidate pool as CED RSFT but random selection instead of CED scoring. If random RSFT significantly underperforms CED RSFT (rel_f1 gap > 1.5pp), proves CED scoring precision is the key, not just data filtering quantity. CED k=1 mean rel_f1=0.4596, expect random < 0.445.\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/rsft_output_random_k1/\", \"log_path\": \"/root/autodl-tmp/rsft_output_random_k1/training.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-18T16:27:01.706Z\"}, \"metrics\": {\"train_loss\": 0.578, \"mean_token_accuracy\": 0.8552, \"global_steps\": 1020, \"epochs\": 3}, \"conclusion\": \"success\"}, \"plan019_1_7b_sft_s43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T15:22:44.792Z\", \"updated_at\": \"2026-05-18T16:27:07.679Z\", \"hypothesis\": \"1.7B SFT seed43: scaling seeds for statistical robustness. Paired with canonical s42 and s44 for 3-seed mean±std at 1.7B scale. Expected train_loss ~0.70, rel_f1 ~49.5 based on canonical 1.7B SFT.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && GPU=0 bash scripts/seed_expansion/sft_1_7b_s43.sh\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"554962\", \"log_path\": \"~/runs/faith-evidence-ie/plan019_1_7b_sft_s43.log\", \"submitted_at\": \"2026-05-18T15:41:52.784Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred/train_annotated.json\", \"data_count\": 3027, \"model_name\": \"Qwen3-1.7B\", \"seed\": 43, \"wall_clock_seconds\": 2714.9, \"gpu_hours\": 0.75}, \"failure_reason\": \"CUDA OOM: CUDA out of memory. Tried to allocate 20.00 MiB. GPU 0 has a total capacity of 31.36 GiB of which 13.75 MiB is free. Process 553704 has 28.30 GiB memory in use. Including non-PyTorch memory, this process has 3.03 GiB memory in use. Of the allocated m\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-18T16:27:07.680Z\"}, \"wave1_sft_4b_s44_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T14:01:43.597Z\", \"updated_at\": \"2026-05-18T15:43:33.593Z\", \"hypothesis\": \"SFT 4B seed44 eval (D076 protocol): baseline SFT performance for seed44. Paired with s43 for mean±std. Expected rel_f1 ~50.5 based on prior 4B SFT s42 results.\", \"parent\": \"wave1_sft_4b_s44\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.eval.inference --model_path /root/autodl-tmp/sft_output_seed44/ --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/sft_4b_s44_eval\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"548407\", \"log_path\": \"~/runs/faith-evidence-ie/wave1_sft_4b_s44_eval.log\", \"submitted_at\": \"2026-05-18T14:02:17.363Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + SFT-s44\", \"seed\": 42, \"checkpoint_source\": \"wave1_sft_4b_s44\", \"eval_data\": \"DocRED dev\", \"failure_reason\": \"Same inference.py adapter validation bug as s43 eval\", \"wall_clock_seconds\": 6076.2, \"gpu_hours\": 1.69}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-18T15:43:33.594Z\"}, \"wave1_sft_4b_s43_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T14:01:42.261Z\", \"updated_at\": \"2026-05-18T15:43:30.104Z\", \"hypothesis\": \"SFT 4B seed43 eval (D076 protocol): baseline SFT performance for seed43. Paired with s44 for mean±std. Expected rel_f1 ~50.5 based on prior 4B SFT s42 results.\", \"parent\": \"wave1_sft_4b_s43\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.eval.inference --model_path /root/autodl-tmp/sft_output_seed43/ --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/sft_4b_s43_eval\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"548328\", \"log_path\": \"~/runs/faith-evidence-ie/wave1_sft_4b_s43_eval.log\", \"submitted_at\": \"2026-05-18T14:02:15.167Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + SFT-s43\", \"seed\": 42, \"checkpoint_source\": \"wave1_sft_4b_s43\", \"eval_data\": \"DocRED dev\", \"failure_reason\": \"inference.py adapter validation bug: detects LoRA adapter_config.json and requires --sft_adapter, but SFT adapter as model_path should not trigger this. Fix: use --model_path=base_model --sft_adapter=adapter_path\", \"wall_clock_seconds\": 6074.9, \"gpu_hours\": 1.69}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-18T15:43:30.104Z\"}, \"seed_llama_rsft_k1_s43_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T13:30:51.665Z\", \"updated_at\": \"2026-05-18T15:22:14.518Z\", \"hypothesis\": \"LLaMA-8B RSFT k=1 seed43 eval: paired with s42 (rel_f1=0.5839) for seed robustness. If s43 gives similar results (±1.5pp), cross-architecture RSFT k=1 claim is robust. Expected rel_f1 ~0.58±0.015.\", \"parent\": \"rsft_llama_k1_s43_train\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_llama_3_1_8b_k1_s43/checkpoint-1107 --base_model /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B --sft_adapter /root/autodl-tmp/sft_output_llama_3_1_8b --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 43 --no-quantize --output_dir /root/autodl-tmp/eval_results/d102_llama_k1_s43\", \"server\": \"rtx5090-4x\", \"gpu_id\": \"cuda:3\", \"pid\": \"541954\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Meta-Llama-3.1-8B + SFT + RSFT-k1-s43\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/rsft_output_llama_3_1_8b_k1_s43/checkpoint-1107\", \"eval_data\": \"DocRED dev\", \"log_path\": \"/root/autodl-tmp/eval_results/d102_llama_k1_s43.log\", \"checkpoint_path\": \"/root/autodl-tmp/eval_results/d102_llama_k1_s43\", \"ign_f1\": 0.5662, \"f1\": 0.578, \"evi_f1\": 0.4644, \"evi_f1_tp\": 0.8287, \"EDCR\": 0.5783, \"truncated\": 173, \"predictions\": 14967, \"inference_time_s\": 9017}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T15:22:14.518Z\"}, \"wave1_sft_4b_s44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T12:44:43.563Z\", \"updated_at\": \"2026-05-18T14:01:03.605Z\", \"hypothesis\": \"SFT baseline for Qwen3-4B seed44: second seed for SFT baseline. Paired with seed43 for mean±std reporting. Expected rel_f1 similar to seed43 (~50.5±1pp).\", \"spec\": {\"command\": \"bash /root/autodl-tmp/freige/scripts/d102_next_batch/sft_seed44.sh\", \"server\": \"rtx5090-4x\", \"gpu_id\": 1, \"pid\": 540984, \"data_path\": \"/root/autodl-tmp/data/docred/train_annotated.json\", \"data_count\": 3027, \"model_name\": \"Qwen3-4B\", \"seed\": 44, \"plan_id\": \"plan_w3_sft_seeds\", \"checkpoint_source\": \"/root/autodl-tmp/models/Qwen3-4B\", \"log_path\": \"/root/autodl-tmp/sft_output_seed44/training.log\", \"checkpoint_path\": \"/root/autodl-tmp/sft_output_seed44/\", \"train_loss\": 0.7008, \"eval_loss\": 0.7478, \"train_steps\": 144, \"epochs\": 3, \"eval_mean_token_accuracy\": 0.8299}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T14:01:03.605Z\"}, \"wave1_sft_4b_s43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T12:44:52.340Z\", \"updated_at\": \"2026-05-18T14:01:01.015Z\", \"hypothesis\": \"SFT baseline for Qwen3-4B seed43: standard SFT without CED filtering. Paired with RSFT to measure CED filtering gain. Expected rel_f1 ~50.5 based on prior 8B SFT results scaled down.\", \"spec\": {\"command\": \"bash scripts/d102_next_batch/sft_seed43.sh\", \"server\": \"rtx5090-4x\", \"gpu_id\": 0, \"pid\": 540777, \"data_path\": \"/root/autodl-tmp/data/docred/train_annotated.json\", \"data_count\": 3027, \"model_name\": \"Qwen3-4B\", \"seed\": 43, \"output_dir\": \"/root/autodl-tmp/sft_output_seed43\", \"plan_id\": \"plan_w3_sft_seeds\", \"wandb_run_name\": \"sft-4b-seed43\", \"checkpoint_path\": \"/root/autodl-tmp/sft_output_seed43/\", \"log_path\": \"/root/autodl-tmp/sft_output_seed43/training.log\", \"train_loss\": 0.7011, \"eval_loss\": 0.7482, \"train_steps\": 144, \"epochs\": 3, \"eval_mean_token_accuracy\": 0.83}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T14:01:01.015Z\"}, \"d102_llama_rsft_k1_s43_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T13:06:23.193Z\", \"updated_at\": \"2026-05-18T13:59:53.656Z\", \"hypothesis\": \"LLaMA-8B RSFT k=1 seed43 eval: paired with s42 (rel_f1=0.5839) for seed robustness. If s43 gives similar results (±1.5pp), cross-architecture RSFT k=1 claim is robust. Expected rel_f1 ~0.58±0.015.\", \"parent\": \"rsft_llama_k1_s43_train\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_llama_3_1_8b_k1_s43/checkpoint-1107 --base_model /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B --sft_adapter /root/autodl-tmp/sft_output_llama_3_1_8b --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 43 --no-quantize --output_dir /root/autodl-tmp/eval_results/d102_llama_k1_s43\", \"server\": \"rtx5090-4x\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Meta-Llama-3.1-8B + SFT + RSFT-k1-s43\", \"seed\": 43, \"checkpoint_source\": \"rsft_llama_k1_s43_train\", \"eval_data\": \"DocRED dev\", \"checkpoint_path\": \"/root/autodl-tmp/eval_results/d102_llama_k1_s43\", \"log_path\": \"/root/autodl-tmp/eval_results/d102_llama_k1_s43.log\"}, \"conclusion\": \"killed\", \"failure_reason\": \"重复条目，已合并到 seed_llama_rsft_k1_s43_eval（同一进程 PID 541954）\", \"completed_at\": \"2026-05-18T13:59:53.656Z\"}, \"seed_llama_rsft_k1_s43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T12:47:48.554Z\", \"updated_at\": \"2026-05-18T13:01:01.136Z\", \"failure_reason\": \"假阳性：实验仅注册 PREPARING 未提交运行，cron 误判为进程死亡。实际训练由 rsft_llama_k1_s43_train 完成（success）。\", \"conclusion\": \"failed\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T12:47:53.490071+00:00\"}]}, \"spec\": {\"command\": \"N/A - phantom entry, real training done by rsft_llama_k1_s43_train\", \"server\": \"rtx5090-4x\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"N/A\", \"seed\": 43}, \"completed_at\": \"2026-05-18T13:01:01.136Z\"}, \"rsft_llama_k1_s43_train\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T11:42:54.821Z\", \"updated_at\": \"2026-05-18T12:47:09.743Z\", \"spec\": {\"command\": \"GPU=3 bash /root/autodl-tmp/freige/scripts/seed_expansion/train_llama_s43.sh\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"537136\", \"log_path\": \"~/runs/faith-evidence-ie/rsft_llama_k1_s43_train.log\", \"submitted_at\": \"2026-05-18T11:42:54.203Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Meta-Llama-3.1-8B\", \"seed\": 43, \"data_path\": \"/root/autodl-tmp/rsft_scored_llama_3_1_8b_k1/rsft_train.jsonl\", \"data_count\": 2952, \"wall_clock_seconds\": 3855.5, \"gpu_hours\": 1.07}, \"hypothesis\": \"LLaMA-3.1-8B RSFT k=1 seed43: 与 s42 配对验证种子稳定性。k=1 数据（2952 samples），跨架构验证 CED 筛选在 LLaMA 上的效果。\", \"checkpoint_path\": \"/root/autodl-tmp/rsft_output_llama_3_1_8b_k1_s43\", \"log_path\": \"~/runs/faith-evidence-ie/rsft_llama_k1_s43_train.log\", \"conclusion\": \"success\", \"metrics\": {\"train_loss_final\": 0.4447, \"mean_token_accuracy_final\": 0.8912, \"global_steps\": 1107, \"epochs\": 3, \"total_flos\": 386000000000000000}, \"completed_at\": \"2026-05-18T12:47:09.743Z\"}, \"d102_8b_rsft_k1_s43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T05:40:05.983Z\", \"updated_at\": \"2026-05-18T12:18:54.937Z\", \"hypothesis\": \"D102 方法论修正：8B RSFT k=1 seed43，与 s42 配对验证种子稳定性。k=1 数据（3018 samples），超参与 4B canonical 一致。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --sft_adapter /root/autodl-tmp/sft_output_qwen3_8b_bf16 --rsft_data_path /root/autodl-tmp/rsft_scored_qwen3_8b_k1/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output_qwen3_8b_k1_s43 --learning_rate 2e-5 --num_epochs 3 --per_device_batch_size 1 --gradient_accumulation_steps 8 --warmup_steps 100 --save_steps 50 --save_total_limit 2 --max_length 2048 --seed 43 --lora_rank 64 --lora_alpha 128 --bf16 --wandb_project freige-rsft --wandb_run_name rsft_qwen3_8b_k1_s43_resume --resume_from_checkpoint /root/autodl-tmp/rsft_output_qwen3_8b_k1_s43/checkpoint-250\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"516711\", \"log_path\": \"~/runs/faith-evidence-ie/d102_8b_rsft_k1_s43.log\", \"submitted_at\": \"2026-05-18T07:22:33.124Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen3-8B\", \"seed\": 43, \"data_path\": \"/root/autodl-tmp/rsft_scored_qwen3_8b_k1/rsft_train.jsonl\", \"data_count\": 3018, \"checkpoint_path\": \"/root/autodl-tmp/rsft_output_qwen3_8b_k1_s43/checkpoint-1134\", \"wall_clock_seconds\": 5362.4, \"gpu_hours\": 1.49}, \"reproduce\": {\"finished_at\": \"2026-05-18T08:46:56.988Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T08:47:05.756299+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.3862, \"mean_token_accuracy\": 0.8735, \"epochs\": 3, \"global_steps\": 1134, \"runtime_seconds\": 2894.88, \"entropy\": 0.5195, \"data_samples\": 3018}, \"completed_at\": \"2026-05-18T08:51:55.500Z\", \"checkpoint_path\": \"/root/autodl-tmp/rsft_output_qwen3_8b_k1_s43/checkpoint-1134\"}, \"d102_8b_rsft_k1_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T05:40:04.009Z\", \"updated_at\": \"2026-05-18T12:18:53.819Z\", \"hypothesis\": \"D102 方法论修正：8B RSFT 从 k=3 改为 k=1（与论文声明和 4B canonical 一致）。k=1 筛选更严格（3018 samples vs 9041），预期 rel_f1 与 k=3 相当或略有变化，验证 k=1 在 8B 上同样有效。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --sft_adapter /root/autodl-tmp/sft_output_qwen3_8b_bf16 --rsft_data_path /root/autodl-tmp/rsft_scored_qwen3_8b_k1/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output_qwen3_8b_k1 --learning_rate 2e-5 --num_epochs 3 --per_device_batch_size 1 --gradient_accumulation_steps 8 --warmup_steps 100 --save_steps 50 --save_total_limit 2 --max_length 2048 --seed 42 --lora_rank 64 --lora_alpha 128 --bf16 --wandb_project freige-rsft --wandb_run_name rsft_qwen3_8b_k1_s42_resume --resume_from_checkpoint /root/autodl-tmp/rsft_output_qwen3_8b_k1/checkpoint-250\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"516605\", \"log_path\": \"~/runs/faith-evidence-ie/d102_8b_rsft_k1_s42.log\", \"submitted_at\": \"2026-05-18T07:22:29.717Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"data_path\": \"/root/autodl-tmp/rsft_scored_qwen3_8b_k1/rsft_train.jsonl\", \"data_count\": 3018, \"checkpoint_path\": \"/root/autodl-tmp/rsft_output_qwen3_8b_k1/checkpoint-1134\", \"wall_clock_seconds\": 5361.8, \"gpu_hours\": 1.49}, \"reproduce\": {\"finished_at\": \"2026-05-18T08:46:48.141Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T08:46:52.714840+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.3877, \"mean_token_accuracy\": 0.8579, \"epochs\": 3, \"global_steps\": 1134, \"runtime_seconds\": 2915.82, \"entropy\": 0.5847, \"data_samples\": 3018}, \"completed_at\": \"2026-05-18T08:51:51.561Z\", \"checkpoint_path\": \"/root/autodl-tmp/rsft_output_qwen3_8b_k1/checkpoint-1134\"}, \"d102_llama_rsft_k1_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T05:40:08.858Z\", \"updated_at\": \"2026-05-18T08:52:32.145Z\", \"hypothesis\": \"D102 方法论修正：LLaMA-8B RSFT 从 k=3 改为 k=1（与论文声明和 4B canonical 一致）。k=1 筛选更严格（2952 samples vs 8829），跨架构验证 k=1 RSFT 效果。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B --sft_adapter /root/autodl-tmp/sft_output_llama_3_1_8b --rsft_data_path /root/autodl-tmp/rsft_scored_llama_3_1_8b_k1/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output_llama_3_1_8b_k1 --learning_rate 2e-5 --num_epochs 3 --per_device_batch_size 1 --gradient_accumulation_steps 8 --warmup_steps 100 --save_steps 50 --save_total_limit 2 --max_length 2048 --seed 42 --lora_rank 64 --lora_alpha 128 --bf16 --wandb_project freige-rsft --wandb_run_name llama_8b_rsft_ced_k1_resume --resume_from_checkpoint /root/autodl-tmp/rsft_output_llama_3_1_8b_k1/checkpoint-250\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"517259\", \"log_path\": \"~/runs/faith-evidence-ie/d102_llama_rsft_k1_s42.log\", \"submitted_at\": \"2026-05-18T07:22:41.245Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Meta-Llama-3.1-8B\", \"seed\": 42, \"data_path\": \"/root/autodl-tmp/rsft_scored_llama_3_1_8b_k1/rsft_train.jsonl\", \"data_count\": 2952, \"checkpoint_path\": \"/root/autodl-tmp/rsft_output_llama_3_1_8b_k1/checkpoint-1107\", \"wall_clock_seconds\": 5347.6, \"gpu_hours\": 1.49}, \"reproduce\": {\"finished_at\": \"2026-05-18T08:46:39.626Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T08:46:44.372577+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.3698, \"mean_token_accuracy\": 0.8876, \"epochs\": 3, \"global_steps\": 1107, \"runtime_seconds\": 2601.34, \"entropy\": 0.5017, \"data_samples\": 2952}, \"completed_at\": \"2026-05-18T08:51:48.872Z\", \"checkpoint_path\": \"/root/autodl-tmp/rsft_output_llama_3_1_8b_k1/checkpoint-1107\"}, \"d102_1_7b_rsft_k1_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T05:40:07.489Z\", \"updated_at\": \"2026-05-18T08:52:27.461Z\", \"hypothesis\": \"D102 方法论修正：1.7B RSFT 从 k=3 改为 k=1（与论文声明和 4B canonical 一致）。k=1 筛选更严格（3021 samples vs 9042），在最小模型上验证 k=1 RSFT 效果。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen/Qwen3-1.7B --sft_adapter /root/autodl-tmp/sft_output_qwen3_1_7b_bf16 --rsft_data_path /root/autodl-tmp/freige/outputs/rsft_scored_1_7b_k1/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output_qwen3_1_7b_k1 --learning_rate 2e-5 --num_epochs 3 --per_device_batch_size 4 --gradient_accumulation_steps 4 --warmup_steps 100 --save_steps 50 --save_total_limit 2 --max_length 2048 --seed 42 --lora_rank 64 --lora_alpha 128 --bf16 --wandb_project freige-rsft --wandb_run_name rsft_qwen3_1_7b_k1_s42_resume --resume_from_checkpoint /root/autodl-tmp/rsft_output_qwen3_1_7b_k1/checkpoint-250\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:2\"], \"pid\": \"517006\", \"log_path\": \"~/runs/faith-evidence-ie/d102_1_7b_rsft_k1_s42.log\", \"submitted_at\": \"2026-05-18T07:22:37.265Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen3-1.7B\", \"seed\": 42, \"data_path\": \"/root/autodl-tmp/freige/outputs/rsft_scored_1_7b_k1/rsft_train.jsonl\", \"data_count\": 3021, \"checkpoint_path\": \"/root/autodl-tmp/rsft_output_qwen3_1_7b_k1/checkpoint-567\", \"wall_clock_seconds\": 5348.9, \"gpu_hours\": 1.49}, \"reproduce\": {\"finished_at\": \"2026-05-18T08:46:29.889Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T08:46:34.301357+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.3063, \"mean_token_accuracy\": 0.8731, \"epochs\": 3, \"global_steps\": 567, \"runtime_seconds\": 899.39, \"entropy\": 0.5467, \"data_samples\": 3021}, \"completed_at\": \"2026-05-18T08:51:46.141Z\", \"checkpoint_path\": \"/root/autodl-tmp/rsft_output_qwen3_1_7b_k1/checkpoint-567\"}, \"seed_comparison_prep\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T02:35:52.694Z\", \"updated_at\": \"2026-05-17T23:18:37.491Z\", \"notes\": \"## Seed Comparison Pre-Analysis (2026-05-16)\\n\\n### Available Results (3/4 seeds each, s45 pending for both):\\n\\n**flat-NLI RSFT:**\\n- s42: rel_f1=0.4539 (dir: rsft_flat_nli)\\n- s43: rel_f1=0.4523 (dir: rsft_flat_nli_s43_reeval; original rsft_flat_nli_s43 was broken f1=0.002)\\n- s44: rel_f1=0.4615 (dir: rsft_flat_nli_s44; NOTE: only metrics.json, no metrics_v2.json with fixed Ign-F1)\\n- s45: PENDING (empty dir)\\n- Mean: 0.4559 ± 0.0049\\n\\n**CED RSFT:**\\n- s42: rel_f1=0.4504 (dir: rsft_r2b_maxtok1536)\\n- s43: rel_f1=0.4683 (dir: rsft_s43)\\n- s44: rel_f1=0.4655 (dir: rsft_s44)\\n- s45: PENDING (empty dir)\\n- Mean: 0.4614 ± 0.0096\\n\\n### Pre-comparison (N=3):\\n- rel_f1 Delta (fNLI - CED): -0.0055 (CED slightly better)\\n- Paired t-test: t=0.967, p=0.4357 (NOT significant)\\n- 95% CI for delta: [-0.0299, +0.0189] (crosses zero)\\n- Cohen's d: -0.558\\n\\n### seed_comparison.py status: WORKING\\n- Auto-discovers all seeds, handles fallback dirs, filters broken results (f1<0.01)\\n- Outputs to /root/autodl-tmp/eval_results/seed_comparison.{md,json}\\n- Supports --watch mode for polling\", \"conclusion\": \"killed\", \"spec\": {\"checkpoint_path\": \"N/A - killed\", \"log_path\": \"N/A\"}, \"completed_at\": \"2026-05-17T23:18:37.491Z\"}, \"plan006_1_7b_rsft_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T06:10:39.978Z\", \"updated_at\": \"2026-05-17T23:18:35.353Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python3 -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_qwen3_1_7b --base_model /root/autodl-tmp/models/Qwen/Qwen3-1.7B --sft_adapter /root/autodl-tmp/sft_output_qwen3_1_7b_bf16 --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/plan_006_qwen3_1_7b_rsft_eval\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"420013\", \"log_path\": \"N/A\", \"submitted_at\": \"2026-05-17T06:10:39.457Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A - killed\", \"wall_clock_seconds\": 61675.9, \"gpu_hours\": 17.13}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-17T23:18:35.353Z\"}, \"rsft_s43_dev_eval_preds\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T08:35:42.135Z\", \"updated_at\": \"2026-05-17T23:18:03.147Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/freige && python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/rsft_s43_dev_eval_preds\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"431303\", \"log_path\": \"~/runs/faith-evidence-ie/rsft_s43_dev_eval_preds.log\", \"submitted_at\": \"2026-05-17T08:38:45.685Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + SFT + RSFT-s43(CED)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/rsft_output_ced_s43/checkpoint-510\", \"eval_data\": \"docred_dev\", \"checkpoint_path\": \"/root/autodl-tmp/eval_results/rsft_s43_dev_eval_preds\", \"wall_clock_seconds\": 52757.5, \"gpu_hours\": 14.65}, \"hypothesis\": \"Eval RSFT-s43 (CED-scored) on DocRED dev with predictions saved. Prerequisite for Lead 1 CED evidence filtering: per-sentence NLI scoring requires full prediction outputs.\", \"metrics\": {\"ign_f1\": 0.4512, \"f1\": 0.4601, \"evi_f1\": 0.8063, \"edcr\": 0.6542, \"evi_f1_joint\": 0.3605, \"format_compliance_rate\": 1, \"field_compliance_rate\": 0.809, \"n_truncated\": 184, \"inference_time_seconds\": 10982}, \"reproduce\": {\"finished_at\": \"2026-05-17T12:11:12.913Z\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T23:18:03.147Z\"}, \"plan_006_qwen3_1_7b_rsft_eval_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T08:35:45.455Z\", \"updated_at\": \"2026-05-17T23:18:01.212Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/freige && python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_qwen3_1_7b/checkpoint-1698 --base_model /root/autodl-tmp/models/Qwen/Qwen3-1.7B --sft_adapter /root/autodl-tmp/sft_output_qwen3_1_7b_bf16 --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/plan_006_qwen3_1_7b_rsft_eval_r2\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"431380\", \"log_path\": \"~/runs/faith-evidence-ie/plan_006_qwen3_1_7b_rsft_eval_r2.log\", \"submitted_at\": \"2026-05-17T08:38:48.805Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen/Qwen3-1.7B + SFT + RSFT\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/rsft_output_qwen3_1_7b/checkpoint-1698\", \"eval_data\": \"docred_dev\", \"checkpoint_path\": \"/root/autodl-tmp/eval_results/plan_006_qwen3_1_7b_rsft_eval_r2\", \"wall_clock_seconds\": 52752.4, \"gpu_hours\": 14.65}, \"hypothesis\": \"Evaluate 1.7B RSFT model (checkpoint-1698) on DocRED dev. Retry after disk-full crash. Validates CED-filtered RSFT at smallest model scale in scaling study.\", \"parent\": \"plan_006_qwen3_1_7b_rsft_train\", \"metrics\": {\"ign_f1\": 0.505, \"f1\": 0.5219, \"evi_f1\": 0.8309, \"edcr\": 0.6297, \"evi_f1_joint\": 0.4223, \"format_compliance_rate\": 0.999, \"field_compliance_rate\": 0.732, \"n_truncated\": 258, \"inference_time_seconds\": 9464}, \"reproduce\": {\"finished_at\": \"2026-05-17T12:11:16.096Z\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T23:18:01.212Z\"}, \"plan_006_llama_rsft_r3_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T08:35:48.098Z\", \"updated_at\": \"2026-05-17T23:17:59.347Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/freige && python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_llama_3_1_8b_r3/checkpoint-3312 --base_model /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B --sft_adapter /root/autodl-tmp/sft_output_llama_3_1_8b --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/plan_006_llama_rsft_r3_eval\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:2\"], \"pid\": \"432665\", \"log_path\": \"~/runs/faith-evidence-ie/plan_006_llama_rsft_r3_eval.log\", \"submitted_at\": \"2026-05-17T08:40:35.462Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"LLaMA-3.1-8B-Instruct + SFT + RSFT-r3\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/rsft_output_llama_3_1_8b_r3/checkpoint-3312\", \"eval_data\": \"docred_dev\", \"checkpoint_path\": \"/root/autodl-tmp/eval_results/plan_006_llama_rsft_r3_eval\", \"wall_clock_seconds\": 52643.9, \"gpu_hours\": 14.62}, \"hypothesis\": \"Evaluate LLaMA-3.1-8B RSFT r3 (checkpoint-3312, final) on DocRED dev. Cross-architecture validation: if CED-RSFT works on both Qwen and LLaMA, the method is architecture-agnostic.\", \"metrics\": {\"ign_f1\": 0.5563, \"f1\": 0.5674, \"evi_f1\": 0.8255, \"edcr\": 0.5856, \"evi_f1_joint\": 0.4571, \"format_compliance_rate\": 0.997, \"field_compliance_rate\": 0.807, \"n_truncated\": 187, \"inference_time_seconds\": 8650}, \"reproduce\": {\"finished_at\": \"2026-05-17T12:11:19.290Z\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T23:17:59.347Z\"}, \"plan_006_qwen3_8b_rsft_train_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T08:35:51.553Z\", \"updated_at\": \"2026-05-17T23:17:57.426Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/freige && python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --sft_adapter /root/autodl-tmp/sft_output_qwen3_8b_bf16 --rsft_data_path /root/autodl-tmp/rsft_scored_qwen3_8b/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output_qwen3_8b --num_epochs 3 --bf16 --per_device_batch_size 1 --gradient_accumulation_steps 8 --resume_from_checkpoint /root/autodl-tmp/rsft_output_qwen3_8b/checkpoint-750\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"431780\", \"log_path\": \"~/runs/faith-evidence-ie/plan_006_qwen3_8b_rsft_train_r2.log\", \"submitted_at\": \"2026-05-17T08:38:54.918Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/rsft_scored_qwen3_8b/rsft_train.jsonl\", \"data_count\": 9041, \"model_name\": \"Qwen/Qwen3-8B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/sft_output_qwen3_8b_bf16\", \"checkpoint_path\": \"/root/autodl-tmp/rsft_output_qwen3_8b/checkpoint-3393\", \"wall_clock_seconds\": 52742.5, \"gpu_hours\": 14.65}, \"hypothesis\": \"RSFT with CED-scored data (9041 samples) on Qwen3-8B, resume from checkpoint-750 after disk-full crash. At 8B scale, CED-filtered RSFT should achieve highest absolute performance in scaling study.\", \"parent\": \"plan_006_qwen3_8b_rsft_train\", \"metrics\": {\"train_loss\": 0.3008, \"mean_token_accuracy\": 0.9172, \"epochs\": 3, \"runtime_seconds\": 8983}, \"reproduce\": {\"finished_at\": \"2026-05-17T12:11:22.362Z\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T23:17:57.426Z\"}, \"plan_006_qwen3_1_7b_rsft_seed43_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T14:26:15.446Z\", \"updated_at\": \"2026-05-17T19:56:30.167Z\", \"hypothesis\": \"Evaluate 1.7B RSFT seed 43 on DocRED dev. Seed 42 gave rel_f1=0.5219. If seed 43 gives similar result (±1pp, i.e., 0.51-0.53), the 1.7B scaling study datapoint is robust.\", \"parent\": \"plan_006_qwen3_1_7b_rsft_seed43\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_qwen3_1_7b_seed43/checkpoint-1698 --base_model /root/autodl-tmp/models/Qwen/Qwen3-1.7B --sft_adapter /root/autodl-tmp/sft_output_qwen3_1_7b_bf16 --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 43 --no-quantize --output_dir /root/autodl-tmp/eval_results/plan_006_qwen3_1_7b_rsft_seed43_eval\", \"server\": \"rtx5090-4x\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 998, \"model_name\": \"Qwen3-1.7B\", \"seed\": 43, \"checkpoint_source\": \"plan_006_qwen3_1_7b_rsft_seed43\", \"eval_data\": \"docred-dev\", \"pid\": 455632, \"gpu\": \"cuda:2\", \"checkpoint_path\": \"/root/autodl-tmp/eval_results/plan_006_qwen3_1_7b_rsft_seed43_eval\", \"log_path\": \"/root/autodl-tmp/eval_results/plan_006_qwen3_1_7b_rsft_seed43_eval.log\"}, \"conclusion\": \"success\", \"metrics\": {\"f1\": 0.518, \"ign_f1\": 0.5024, \"evi_f1_joint\": 0.4201, \"evi_f1_tp\": 0.8341, \"edcr\": 0.6246, \"precision\": 0.535, \"recall\": 0.5019, \"ign_precision\": 0.5099, \"ign_recall\": 0.4951, \"format_ok\": \"984/985\", \"n_truncated\": 262, \"n_predictions\": 16455}, \"completed_at\": \"2026-05-17T19:56:30.167Z\"}, \"plan_006_qwen3_1_7b_rsft_test\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T16:50:19.779Z\", \"updated_at\": \"2026-05-17T19:56:28.396Z\", \"hypothesis\": \"Generate 1.7B RSFT test set predictions for CodaLab submission. 1.7B RSFT dev rel_f1=0.5219, expect similar performance on test.\", \"parent\": \"plan_006_qwen3_1_7b_rsft_eval_r2\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=2 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_qwen3_1_7b/checkpoint-1698 --base_model /root/autodl-tmp/models/Qwen/Qwen3-1.7B --sft_adapter /root/autodl-tmp/sft_output_qwen3_1_7b_bf16 --data_path /root/autodl-tmp/data/docred --split test --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/plan_006_qwen3_1_7b_rsft_test\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:2\"], \"pid\": \"466508\", \"log_path\": \"~/runs/faith-evidence-ie/plan_006_qwen3_1_7b_rsft_test.log\", \"submitted_at\": \"2026-05-17T16:51:35.716Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": \"1000 (DocRED test)\", \"model_name\": \"Qwen3-1.7B RSFT checkpoint-1698\", \"seed\": 42, \"checkpoint_source\": \"plan_006_qwen3_1_7b_rsft_eval_r2\", \"eval_data\": \"DocRED test\", \"checkpoint_path\": \"/root/autodl-tmp/eval_results/plan_006_qwen3_1_7b_rsft_test\", \"wall_clock_seconds\": 11092.7, \"gpu_hours\": 3.08}, \"reproduce\": {\"finished_at\": \"2026-05-17T19:52:01.502Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T19:52:05.166843+00:00\"}]}, \"metrics\": {\"n_predictions\": 28743, \"n_truncated\": 857, \"format_ok_rate\": 0.999, \"n_docs\": 1000, \"codalab_entries\": 27567}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T19:56:28.396Z\"}, \"plan_006_qwen3_8b_rsft_test\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T15:30:36.092Z\", \"updated_at\": \"2026-05-17T19:01:47.602Z\", \"hypothesis\": \"Generate 8B RSFT test set predictions for CodaLab submission. 8B RSFT dev rel_f1=0.5606, expect similar performance on test.\", \"spec\": {\"command\": \"python inference.py --model_path /root/autodl-tmp/freige/rsft_output_qwen3_8b/checkpoint-3393 --base_model /root/autodl-tmp/models/Qwen3-8B --output_dir /root/autodl-tmp/eval_results/plan_006_qwen3_8b_rsft_test --split test --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize\", \"server\": \"rtx5090-4x\", \"gpu_id\": \"1\", \"pid\": 460585, \"data_path\": \"DocRED test set\", \"model_name\": \"Qwen3-8B RSFT checkpoint-3393\", \"seed\": 42, \"checkpoint_source\": \"plan_006_qwen3_8b_rsft_train_r2\", \"eval_data\": \"DocRED test\", \"checkpoint_path\": \"N/A - test predictions\", \"log_path\": \"/root/autodl-tmp/eval_results/plan_006_qwen3_8b_rsft_test.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T19:01:47.602Z\"}, \"plan_006_llama_rsft_seed43_eval_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T16:03:41.592Z\", \"updated_at\": \"2026-05-17T18:48:55.143Z\", \"hypothesis\": \"Evaluate LLaMA-8B RSFT seed 43 on DocRED dev (retry with correct base_model path). Seed 42 gave rel_f1=0.5674. If seed 43 gives similar result (±1.5pp), the cross-architecture RSFT claim is robust against seed variance.\", \"parent\": \"plan_006_llama_rsft_seed43\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_llama_3_1_8b_seed43/checkpoint-3312 --base_model /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B --sft_adapter /root/autodl-tmp/sft_output_llama_3_1_8b --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 43 --no-quantize --output_dir /root/autodl-tmp/eval_results/plan_006_llama_rsft_seed43_eval_r2\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"463080\", \"log_path\": \"~/runs/faith-evidence-ie/plan_006_llama_rsft_seed43_eval_r2.log\", \"submitted_at\": \"2026-05-17T16:03:52.701Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": \"985 (DocRED dev)\", \"model_name\": \"Meta-Llama-3.1-8B + SFT + RSFT-seed43\", \"seed\": 43, \"checkpoint_source\": \"plan_006_llama_rsft_seed43\", \"eval_data\": \"DocRED dev\", \"checkpoint_path\": \"/root/autodl-tmp/eval_results/plan_006_llama_rsft_seed43_eval_r2\", \"wall_clock_seconds\": 9576.6, \"gpu_hours\": 2.66}, \"reproduce\": {\"finished_at\": \"2026-05-17T18:37:24.160Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T18:37:30.788639+00:00\"}]}, \"metrics\": {\"rel_f1\": 0.5727, \"ign_f1\": 0.5619, \"evi_f1\": 0.8206, \"evi_f1_joint\": 0.4551, \"edcr\": 0.6073, \"format_compliance_rate\": 1, \"n_truncated\": 197}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T18:43:29.317Z\"}, \"plan_006_llama_rsft_test\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T15:30:42.159Z\", \"updated_at\": \"2026-05-17T18:37:51.441Z\", \"hypothesis\": \"Generate LLaMA-8B RSFT test set predictions for CodaLab submission. LLaMA-8B RSFT dev rel_f1=0.5674, expect similar performance on test.\", \"spec\": {\"command\": \"python inference.py --model_path /root/autodl-tmp/freige/rsft_output_llama_3_1_8b_r3/checkpoint-3312 --base_model /root/autodl-tmp/models/Meta-Llama-3.1-8B --output_dir /root/autodl-tmp/eval_results/plan_006_llama_rsft_test --split test --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize\", \"server\": \"rtx5090-4x\", \"gpu_id\": \"3\", \"pid\": 460159, \"data_path\": \"DocRED test set\", \"model_name\": \"LLaMA-3.1-8B RSFT checkpoint-3312\", \"seed\": 42, \"checkpoint_source\": \"plan_006_llama_rsft_r3_train\", \"eval_data\": \"DocRED test\", \"checkpoint_path\": \"N/A - test predictions\", \"log_path\": \"/root/autodl-tmp/eval_results/plan_006_llama_rsft_test.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T18:37:51.441Z\"}, \"plan_006_llama_rsft_seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T13:07:02.215Z\", \"updated_at\": \"2026-05-17T16:48:29.803Z\", \"hypothesis\": \"Validate LLaMA-8B RSFT robustness across seeds. Seed 42 gave rel_f1=0.5674 (+1.6pp over SFT baseline 0.5514). If seed 43 gives similar result, the cross-architecture RSFT claim is robust against seed variance.\", \"parent\": \"plan_016_llama_rsft_train_r3\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B --sft_adapter /root/autodl-tmp/sft_output_llama_3_1_8b --rsft_data_path /root/autodl-tmp/rsft_scored_llama_3_1_8b/rsft_train.jsonl --num_epochs 3 --output_dir /root/autodl-tmp/rsft_output_llama_3_1_8b_seed43 --per_device_batch_size 1 --gradient_accumulation_steps 8 --seed 43 --bf16 --wandb_run_name plan_006_llama_rsft_seed43\", \"server\": \"rtx5090-4x\", \"data_path\": \"/root/autodl-tmp/rsft_scored_llama_3_1_8b/rsft_train.jsonl\", \"data_count\": 8829, \"model_name\": \"Meta-Llama-3.1-8B\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/sft_output_llama_3_1_8b\", \"checkpoint_path\": \"/root/autodl-tmp/rsft_output_llama_3_1_8b_seed43/checkpoint-3312\", \"log_path\": \"~/runs/faith-evidence-ie/plan_006_llama_rsft_seed43.log\", \"gpu\": \"cuda:0\", \"pid\": 450239, \"submitted_at\": \"2026-05-17T21:07:00Z\", \"backend\": \"tmux\", \"account\": \"root\", \"bf16\": true, \"quantize\": false, \"per_device_batch_size\": 1, \"gradient_accumulation_steps\": 8, \"effective_batch_size\": 8, \"total_steps\": 3312, \"eval_data\": \"N/A - training experiment\", \"final_loss\": 0.3715, \"mean_token_accuracy\": 0.9418, \"train_runtime_seconds\": 10136, \"epochs\": 3}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T16:48:29.804Z\"}, \"plan_006_llama_rsft_seed43_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T16:00:04.294Z\", \"updated_at\": \"2026-05-17T16:48:26.809Z\", \"hypothesis\": \"Evaluate LLaMA-8B RSFT seed 43 on DocRED dev. Seed 42 gave rel_f1=0.5674. If seed 43 gives similar result (±1.5pp, i.e., 0.55-0.58), the cross-architecture RSFT claim is robust against seed variance.\", \"parent\": \"plan_006_llama_rsft_seed43\", \"spec\": {\"command\": \"python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_llama_3_1_8b_seed43/checkpoint-3312 --base_model /root/autodl-tmp/models/Meta-Llama-3.1-8B --sft_adapter /root/autodl-tmp/sft_output_llama_3_1_8b --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 43 --no-quantize --output_dir /root/autodl-tmp/eval_results/plan_006_llama_rsft_seed43_eval\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"462707\", \"log_path\": \"~/runs/faith-evidence-ie/plan_006_llama_rsft_seed43_eval.log\", \"submitted_at\": \"2026-05-17T16:00:21.066Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": \"docred-dev-full\", \"model_name\": \"Meta-Llama-3.1-8B + SFT + RSFT-seed43\", \"seed\": 43, \"checkpoint_source\": \"plan_006_llama_rsft_seed43\", \"eval_data\": \"docred-dev\", \"checkpoint_path\": \"N/A (failed)\", \"wall_clock_seconds\": 2885.7, \"gpu_hours\": 0.8}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-17T16:48:26.809Z\"}, \"lead2_ckpt20_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T12:31:32.202Z\", \"updated_at\": \"2026-05-17T15:27:15.598Z\", \"hypothesis\": \"Evaluate GRPO checkpoint-20 from RSFT base (lead2_rsft_grpo_ced_r2) on DocRED dev. If RSFT→GRPO preserves/improves rel_f1 over RSFT baseline (0.4601), it validates the RSFT→GRPO training pipeline as viable.\", \"parent\": \"lead2_rsft_grpo_ced_r2\", \"spec\": {\"server\": \"rtx5090-4x\", \"gpu\": 1, \"command\": \"CUDA_VISIBLE_DEVICES=1 python -m freige.eval.inference --model_path /root/autodl-tmp/grpo_from_rsft_lead2_r2/checkpoint-20 --base_model /root/autodl-tmp/merged_sft_rsft_ced_s43 --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_outputs/lead2_ckpt20_eval\", \"model_name\": \"Qwen3-4B (SFT+RSFT_CED_s43 merged + GRPO ckpt-20)\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/grpo_from_rsft_lead2_r2/checkpoint-20\", \"eval_data\": \"docred_dev\", \"pid\": 446829, \"log_path\": \"/root/autodl-tmp/logs/lead2_ckpt20_eval.log\"}, \"conclusion\": \"success\", \"metrics\": {\"rel_f1\": 0.4617, \"ign_f1\": 0.4533, \"evi_f1\": 0.8103, \"evi_f1_joint\": 0.3642, \"edcr\": 0.6465, \"precision\": 0.476, \"recall\": 0.4482, \"format_ok\": \"985/985\", \"truncated\": \"187/985\", \"predictions\": 14998}, \"checkpoint_path\": \"/root/autodl-tmp/grpo_from_rsft_lead2_r2/checkpoint-20\", \"log_path\": \"/root/autodl-tmp/logs/lead2_ckpt20_eval.log\", \"completed_at\": \"2026-05-17T15:27:15.598Z\"}, \"plan_006_qwen3_8b_rsft_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T12:00:05.493Z\", \"updated_at\": \"2026-05-17T14:59:23.644Z\", \"hypothesis\": \"Evaluate Qwen3-8B RSFT (CED-scored data, 9041 samples) on DocRED dev. At 8B scale with near-zero evidence tax, CED-RSFT should achieve highest absolute Ign-F1 in the scaling study.\", \"parent\": \"plan_006_qwen3_8b_rsft_train_r2\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_qwen3_8b/checkpoint-3393 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --sft_adapter /root/autodl-tmp/sft_output_qwen3_8b_bf16 --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/plan_006_qwen3_8b_rsft_eval\", \"server\": \"rtx5090-4x\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 1000, \"eval_data\": \"DocRED dev\", \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/rsft_output_qwen3_8b/checkpoint-3393\", \"pid\": 442383, \"gpu\": \"cuda:3\"}, \"conclusion\": \"success\", \"metrics\": {\"f1\": 0.5606, \"ign_f1\": 0.5433, \"evi_f1\": 0.8052, \"evi_f1_joint\": 0.4413, \"edcr\": 0.6377, \"precision\": 0.5553, \"recall\": 0.566, \"format_ok\": \"985/985\", \"truncated\": \"267/985\", \"predictions\": 16831}, \"checkpoint_path\": \"/root/autodl-tmp/rsft_output_qwen3_8b/checkpoint-3393\", \"log_path\": \"/root/autodl-tmp/eval_results/plan_006_qwen3_8b_rsft_eval.log\", \"completed_at\": \"2026-05-17T14:59:23.644Z\"}, \"plan_006_qwen3_1_7b_rsft_seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T13:01:14.254Z\", \"updated_at\": \"2026-05-17T14:25:12.839Z\", \"hypothesis\": \"RSFT with seed 43 on Qwen3-1.7B will produce comparable performance to other seeds, validating seed robustness for the scaling study\", \"parent\": \"plan_006_qwen3_1_7b_rsft_eval_r2\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen/Qwen3-1.7B --sft_adapter /root/autodl-tmp/sft_output_qwen3_1_7b_bf16 --rsft_data_path /root/autodl-tmp/freige/outputs/rsft_scored_1_7b/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output_qwen3_1_7b_seed43 --num_epochs 3 --seed 43 --bf16 --wandb_run_name plan_006_qwen3_1_7b_rsft_seed43\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:2\", \"pid\": 449282, \"data_path\": \"/root/autodl-tmp/freige/outputs/rsft_scored_1_7b/rsft_train.jsonl\", \"data_count\": 9042, \"model_name\": \"Qwen/Qwen3-1.7B\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/sft_output_qwen3_1_7b_bf16\", \"eval_data\": \"N/A - training experiment (seed variance replication)\", \"log_path\": \"/root/runs/faith-evidence-ie/plan_006_qwen3_1_7b_rsft_seed43.log\", \"checkpoint_path\": \"/root/autodl-tmp/rsft_output_qwen3_1_7b_seed43\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T14:25:10.190Z\", \"notes\": \"Training completed in 4795.7s (~1h20m). 1698 steps, 3 epochs. Final: train_loss=0.523, mean_token_accuracy=0.879, entropy=0.519. Final checkpoint: checkpoint-1698. Needs eval.\"}, \"post_hoc_bm25_baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T13:01:00.344Z\", \"updated_at\": \"2026-05-17T13:02:03.821Z\", \"hypothesis\": \"Post-hoc BM25 evidence retrieval on SFT-no-evidence predictions: if retrieving evidence after RE produces comparable joint Evi-F1 and EDCR to jointly trained RSFT, then joint generation is unnecessary. Expect RSFT to have better evidence quality (lower EDCR) due to training-time evidence grounding.\", \"parent\": \"plan_014_sft_no_evidence\", \"spec\": {\"command\": \"python -m freige.eval.post_hoc_retrieval --predictions_dir /root/autodl-tmp/eval_results/reeval_sft_baseline_d076 --data_dir /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/eval_results/post_hoc_bm25\", \"server\": \"rtx5090-4x\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"BM25 retrieval on SFT-no-evidence predictions\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/eval_results/post_hoc_bm25/\", \"log_path\": \"/root/autodl-tmp/eval_results/post_hoc_bm25/\", \"checkpoint_source\": \"reeval_sft_baseline_d076\", \"eval_data\": \"docred_dev\"}, \"conclusion\": \"success\", \"metrics\": {\"bm25_entity_k2_rel_f1\": 0.4876, \"bm25_entity_k2_evi_f1_joint\": 0.3473, \"bm25_entity_k2_edcr\": 0.7664, \"bm25_entity_k3_evi_f1_joint\": 0.2989, \"bm25_entity_k3_edcr\": 0.8256, \"bm25_oracle_k_evi_f1_joint\": 0.3834, \"bm25_oracle_k_edcr\": 0.7334, \"rsft_ced_s43_rel_f1\": 0.4601, \"rsft_ced_s43_evi_f1_joint\": 0.3605, \"rsft_ced_s43_edcr\": 0.6542, \"sft_joint_rel_f1\": 0.4049, \"sft_joint_evi_f1_joint\": 0.3147, \"sft_joint_edcr\": 0.6982, \"verdict\": \"RSFT joint generation beats BM25 post-hoc on evi_f1_joint (-1.3pp) and EDCR (-11.2pp). Even oracle-k post-hoc has 7.9pp worse EDCR than RSFT.\"}, \"completed_at\": \"2026-05-17T13:02:03.821Z\"}, \"lead1_ced_evidence_filter\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:54:50.206Z\", \"updated_at\": \"2026-05-17T12:57:03.964Z\", \"spec\": {\"command\": \"python -m eval.ced_evidence_filter --predictions_path /root/autodl-tmp/eval_results/rsft_s43_dev_eval_preds/predictions.json --tau_values 0.3 0.5 0.7 --output_dir /root/autodl-tmp/lead1_ced_filter_results\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"441954\", \"log_path\": \"/root/autodl-tmp/lead1_ced_filter_results/summary.json\", \"submitted_at\": \"2026-05-17T11:54:49.626Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_source\": \"rsft_s43_dev_eval_preds\", \"checkpoint_path\": \"/root/autodl-tmp/lead1_ced_filter_results/\", \"model_name\": \"NLI-filter-on-rsft_s43\", \"data_path\": \"/root/autodl-tmp/eval_results/rsft_s43_dev_eval_preds/predictions.json\", \"data_count\": 14976, \"seed\": 42, \"wall_clock_seconds\": 3664.6, \"gpu_hours\": 1.02}, \"conclusion\": \"negative\", \"hypothesis\": \"Post-hoc CED-based evidence filtering on RSFT predictions: removing low-NLI-score evidence sentences at inference time should improve Evi-F1 and EDCR by eliminating distractor citations, without affecting rel_f1.\", \"completed_at\": \"2026-05-17T12:55:54.239Z\", \"metrics\": {\"baseline_f1\": 0.4601, \"baseline_ign_f1\": 0.4512, \"baseline_evi_f1\": 0.8063, \"baseline_edcr\": 0.6542, \"tau_0.3_evi_f1\": 0.7301, \"tau_0.3_edcr\": 0.5797, \"tau_0.5_evi_f1\": 0.7297, \"tau_0.5_edcr\": 0.5784, \"tau_0.7_evi_f1\": 0.7287, \"tau_0.7_edcr\": 0.5776, \"evidence_kept_pct_tau_0.5\": 61.9, \"verdict\": \"CED filter removes ~38% evidence but drops Evi-F1 by 7.7pp and EDCR by 7.6pp\"}}, \"plan_006_qwen3_8b_rsft_train\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T05:57:56.689Z\", \"updated_at\": \"2026-05-17T08:25:26.201Z\", \"spec\": {\"command\": \"python -m freige.training.rsft_trainer --base_model Qwen3-8B --sft_adapter sft_output_qwen3_8b_bf16 --rsft_data_path rsft_scored_qwen3_8b/rsft_train.jsonl --num_epochs 3 --bf16 --gradient_checkpointing --per_device_batch_size 1 --gradient_accumulation_steps 8\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:3\", \"pid\": 418278, \"log_path\": \"~/runs/faith-evidence-ie/plan_006_qwen3_8b_rsft_train.log\", \"submitted_at\": \"2026-05-17T05:57:56.172Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/rsft_scored_qwen3_8b/rsft_train.jsonl\", \"data_count\": 9041, \"model_name\": \"Qwen/Qwen3-8B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/sft_output_qwen3_8b_bf16\", \"checkpoint_path\": \"/root/autodl-tmp/rsft_output_qwen3_8b/checkpoint-1000\", \"failure_reason\": \"Disk full - RuntimeError unexpected pos at step 1000/3393\", \"wall_clock_seconds\": 8850.0, \"gpu_hours\": 2.46}, \"hypothesis\": \"RSFT with CED-scored data (9041 samples) on Qwen3-8B will improve rel_f1 over SFT baseline. At 8B scale with near-zero evidence tax, CED-filtered RSFT should achieve the highest absolute performance in the model scaling study.\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-17T08:25:26.201Z\"}, \"plan_006_qwen3_1_7b_rsft_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T06:12:11.998Z\", \"updated_at\": \"2026-05-17T08:25:24.429Z\", \"hypothesis\": \"Evaluate 1.7B RSFT model on DocRED dev to measure rel_f1 improvement over SFT baseline. Validates that CED-filtered RSFT generalizes to smallest model scale (1.7B) in the scaling study.\", \"parent\": \"plan_006_qwen3_1_7b_rsft_train\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_qwen3_1_7b --base_model /root/autodl-tmp/models/Qwen/Qwen3-1.7B --sft_adapter /root/autodl-tmp/sft_output_qwen3_1_7b_bf16 --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/plan_006_qwen3_1_7b_rsft_eval\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:1\", \"pid\": 420013, \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen/Qwen3-1.7B + SFT + RSFT\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/rsft_output_qwen3_1_7b\", \"eval_data\": \"docred_dev\", \"checkpoint_path\": \"N/A (eval)\", \"log_path\": \"N/A\", \"failure_reason\": \"Disk full - EXIT_CODE=124 at 74% progress\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-17T08:25:24.429Z\"}, \"rsft_s44_dev_eval_preds\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T05:02:50.832Z\", \"updated_at\": \"2026-05-17T08:25:22.846Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_s44/checkpoint-510 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/rsft_s44_dev_with_preds\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:0\", \"pid\": 414832, \"log_path\": \"~/runs/faith-evidence-ie/rsft_s44_dev_eval_preds.log\", \"submitted_at\": \"2026-05-17T05:02:50.357Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + SFT + RSFT-s44\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/rsft_output_s44/checkpoint-510\", \"eval_data\": \"docred_dev\", \"checkpoint_path\": \"N/A (eval)\", \"failure_reason\": \"Disk full - EXIT_CODE=124 timeout at 97% progress\", \"wall_clock_seconds\": 12152.5, \"gpu_hours\": 3.38}, \"hypothesis\": \"Re-run RSFT s44 dev eval with predictions saved, as prerequisite for CED evidence filtering experiment (线索1: inference-time distractor citation removal). Predictions needed for per-sentence NLI scoring.\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-17T08:25:22.846Z\"}, \"lead2_rsft_grpo_ced_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T06:23:56.474Z\", \"updated_at\": \"2026-05-17T08:25:20.510Z\", \"spec\": {\"command\": \"python -m freige.training.grpo_trainer --model_name merged_sft_rsft_ced_s43 --data_dir /root/autodl-tmp/data/docred --stage 3 --max_steps 50 --lr 1e-6 --G 8 --kl 0.01 --bf16 --ced=1.0 --f1=0.0 --format=0.5 --save_steps 10\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:2\", \"pid\": 421806, \"log_path\": \"~/runs/faith-evidence-ie/lead2_rsft_grpo_ced_r2.log\", \"submitted_at\": \"2026-05-17T06:24:47.600Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 3027, \"model_name\": \"Qwen3-4B (merged SFT+RSFT-s43)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/merged_sft_rsft_ced_s43\", \"eval_data\": \"/root/autodl-tmp/data/docred/dev.json\", \"checkpoint_path\": \"/root/autodl-tmp/grpo_from_rsft_lead2/checkpoint-30\", \"failure_reason\": \"No space left on device at step 30/50 during checkpoint save\", \"wall_clock_seconds\": 7232.9, \"gpu_hours\": 2.01}, \"hypothesis\": \"RSFT→bf16 GRPO two-stage (retry with --data_dir fix): starting from merged RSFT-s43 checkpoint (rel_f1=0.46), short-range GRPO (50 steps, lr=1e-6) with CED-only reward should improve evidence quality (EDCR) while preserving rel_f1.\", \"parent\": \"lead2_rsft_grpo_ced\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-17T08:25:20.510Z\"}, \"plan_016_llama_rsft_train_r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T03:26:03.945Z\", \"updated_at\": \"2026-05-17T06:26:30.916Z\", \"hypothesis\": \"bf16 full-precision training with gradient checkpointing and batch_size=1 will fit within single RTX 5090 32GB VRAM while maintaining training quality comparable to QLoRA, resolving the OOM issues seen in r1/r2 attempts\", \"parent\": \"plan_016_llama_rsft_train_r2\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B --sft_adapter /root/autodl-tmp/sft_output_llama_3_1_8b --rsft_data_path /root/autodl-tmp/rsft_scored_llama_3_1_8b/rsft_train.jsonl --num_epochs 3 --output_dir /root/autodl-tmp/rsft_output_llama_3_1_8b_r3 --per_device_batch_size 1 --gradient_accumulation_steps 8 --seed 42 --bf16 --wandb_run_name plan_016_llama_rsft_train_r3\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:2\", \"pid\": 409565, \"data_path\": \"/root/autodl-tmp/rsft_scored_llama_3_1_8b/rsft_train.jsonl\", \"data_count\": 8829, \"model_name\": \"Meta-Llama-3.1-8B\", \"seed\": 42, \"checkpoint_source\": \"sft_output_llama_3_1_8b (SFT LoRA adapter from plan_016 stage 1)\", \"eval_data\": \"N/A - this is a training experiment (retry of r2 with bf16 instead of QLoRA)\", \"mode\": \"bf16 + gradient_checkpointing\", \"effective_batch_size\": 8, \"total_steps\": 3312, \"log_path\": \"/root/runs/faith-evidence-ie/plan_016_llama_rsft_train_r3.log\", \"bf16\": true, \"gradient_checkpointing\": true, \"quantize\": false, \"checkpoint_path\": \"/root/autodl-tmp/rsft_output_llama_3_1_8b_r3\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T06:26:29.275Z\", \"metrics\": {\"train_loss\": 0.3724, \"mean_token_accuracy\": 0.929, \"total_steps\": 3312, \"epochs\": 3, \"runtime_seconds\": 10231}}, \"lead2_rsft_grpo_ced\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T05:57:53.951Z\", \"updated_at\": \"2026-05-17T06:06:36.130Z\", \"spec\": {\"command\": \"merge_sft_rsft.py then grpo_trainer --model_name merged_sft_rsft_ced_s43 --stage 3 --max_steps 50 --lr 1e-6 --G 8 --kl 0.01 --bf16 --ced=1.0 --f1=0.0 --format=0.5 --save_steps 10\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:1\", \"pid\": 418198, \"log_path\": \"~/runs/faith-evidence-ie/lead2_rsft_grpo_ced.log\", \"submitted_at\": \"2026-05-17T05:57:53.332Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 3027, \"model_name\": \"Qwen3-4B (merged SFT+RSFT-s43)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/merged_sft_rsft_ced_s43\", \"eval_data\": \"/root/autodl-tmp/data/docred/dev.json\", \"checkpoint_path\": \"N/A\", \"failure_reason\": \"docred_processor.py:129 load_dataset('thunlp/docred') failed - server offline\", \"wall_clock_seconds\": 522.8, \"gpu_hours\": 0.15}, \"hypothesis\": \"RSFT→bf16 GRPO two-stage: starting from RSFT best checkpoint (s43, rel_f1=0.46), short-range GRPO (50 steps, lr=1e-6) with CED-only reward should further improve evidence quality (EDCR) while preserving rel_f1, because RSFT provides stable base preventing catastrophic forgetting seen in SFT→GRPO.\", \"parent\": \"mvp2_rsft_train_r1_s43\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-17T06:06:36.130Z\"}, \"plan_006_qwen3_8b_ced_scoring\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T03:27:03.641Z\", \"updated_at\": \"2026-05-17T06:00:52.969Z\", \"hypothesis\": \"CED scoring on Qwen3-8B RSFT candidates (24216 gens from 3027 docs) will produce high-quality filtered training data. At 8B scale with near-zero evidence tax, CED-filtered RSFT should yield further gains over an already strong SFT baseline.\", \"parent\": \"plan_006_qwen3_8b_rsft_candidates_r2\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_score_filter --input_dir /root/autodl-tmp/freige/outputs/rsft_candidates_8b --output_path /root/autodl-tmp/rsft_scored_qwen3_8b --nli_model_path /root/autodl-tmp/.hf_cache/models--cross-encoder--nli-deberta-v3-base/snapshots/6c749ce3425cd33b46d187e45b92bbf96ee12ec7 --nli_device cuda:0 --scoring_mode ced --tau 0.5 --selection_strategy top_k --top_k 3\", \"server\": \"rtx5090-4x\", \"gpu_ids\": [\"cuda:3\"], \"data_path\": \"/root/autodl-tmp/freige/outputs/rsft_candidates_8b\", \"data_count\": 24216, \"model_name\": \"cross-encoder/nli-deberta-v3-base\", \"seed\": 42, \"checkpoint_source\": \"rsft_candidates_8b (Qwen3-8B generations)\", \"eval_data\": \"24216 candidates from 3027 docs\", \"pid\": 411027, \"checkpoint_path\": \"/root/autodl-tmp/rsft_scored_qwen3_8b\", \"log_path\": \"N/A\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T05:59:49.723Z\", \"metrics\": {\"output_samples\": 9041, \"input_candidates\": 24216, \"scoring_mode\": \"ced\", \"tau\": 0.5, \"top_k\": 3}}, \"plan_006_qwen3_1_7b_rsft_train\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T03:03:05.036Z\", \"updated_at\": \"2026-05-17T06:00:51.477Z\", \"hypothesis\": \"RSFT with CED-scored data on Qwen3-1.7B will improve relation extraction F1 over SFT baseline by selectively reinforcing high-quality extraction patterns, similar to gains seen on 4B model\", \"parent\": \"plan_006_qwen3_1_7b_ced_scoring\", \"spec\": {\"command\": \"python -m freige.training.rsft_trainer --base_model Qwen3-1.7B --sft_adapter sft_output_qwen3_1_7b_bf16 --rsft_data_path rsft_scored_1_7b/rsft_train.jsonl --output_dir rsft_output_qwen3_1_7b --num_epochs 3 --seed 42 --bf16\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:1\", \"pid\": 406515, \"data_path\": \"/root/autodl-tmp/freige/outputs/rsft_scored_1_7b/rsft_train.jsonl\", \"data_count\": 9042, \"model_name\": \"Qwen/Qwen3-1.7B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/sft_output_qwen3_1_7b_bf16\", \"eval_data\": \"/root/autodl-tmp/data/docred/dev.json\", \"checkpoint_path\": \"/root/autodl-tmp/rsft_output_qwen3_1_7b\", \"log_path\": \"~/runs/faith-evidence-ie/plan_006_qwen3_1_7b_rsft_train.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T05:59:47.994Z\", \"metrics\": {\"train_loss\": 0.5234, \"eval_loss\": 0.8725, \"eval_mean_token_accuracy\": 0.8185, \"total_steps\": 1698, \"epochs\": 3, \"runtime_hours\": 2.25}}, \"plan_002_test_rsft_s44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T01:05:59.263Z\", \"updated_at\": \"2026-05-17T04:57:25.850Z\", \"hypothesis\": \"RSFT-CED s44 (best dev config, rel_f1=0.4655) maintains improvement over SFT on held-out test set, confirming CED-filtered rejection sampling gains are not dev-set overfitting. Test Ign-F1 should exceed SFT test baseline.\", \"parent\": \"mvp2_rsft_train_r1_s44\", \"spec\": {\"command\": \"python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_s44/checkpoint-510 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split test --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/plan_002_test_rsft_s44\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"396333\", \"log_path\": \"~/runs/faith-evidence-ie/plan_002_test_rsft_s44.log\", \"submitted_at\": \"2026-05-17T01:06:16.686Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 0, \"model_name\": \"Qwen3-4B + SFT + RSFT-s44\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/rsft_output_s44/checkpoint-510\", \"eval_data\": \"docred_test\", \"loading_mode\": \"3-param (base→SFT→RSFT)\", \"checkpoint_path\": \"/root/autodl-tmp/eval_results/plan_002_test_rsft_s44\", \"metrics_note\": \"Test set - no local gold labels. 1000 docs, 26925 predictions, 626 truncated, format_ok=99.6%. Needs CodaLab submission for official scores.\", \"inference_time_s\": 12494, \"wall_clock_seconds\": 13869.2, \"gpu_hours\": 3.85}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T04:57:25.850Z\"}, \"plan_006_qwen3_8b_rsft_candidates_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T01:54:26.118Z\", \"updated_at\": \"2026-05-17T04:08:25.446Z\", \"hypothesis\": \"Resuming 8B candidate generation from idx 2701 will complete the full RSFT candidate set needed for reward-based filtering and RSFT training\", \"parent\": \"plan_006_qwen3_8b_rsft_candidates\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -m freige.training.rsft_generate --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --sft_adapter /root/autodl-tmp/sft_output_qwen3_8b_bf16 --num_generations 8 --temperature 0.7 --batch_size 1 --data_path /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/freige/outputs/rsft_candidates_8b --start_idx 2701\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": 400132, \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 326, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/freige/outputs/rsft_candidates_8b\", \"log_path\": \"/root/runs/faith-evidence-ie/plan_006_qwen3_8b_rsft_candidates_r2.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T04:08:25.446Z\"}, \"plan_016_llama_rsft_train_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T03:10:57.585Z\", \"updated_at\": \"2026-05-17T03:26:02.383Z\", \"hypothesis\": \"LLaMA-3.1-8B RSFT training retry with OOM fix: --no-quantize (bf16) + gradient_checkpointing. R1 OOM due to missing bf16 flag causing fp32 loading on 32GB card. 8829 CED-filtered samples, 3 epochs.\", \"parent\": \"plan_016_llama_rsft_train\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B --sft_adapter /root/autodl-tmp/sft_output_llama_3_1_8b --rsft_data_path /root/autodl-tmp/rsft_scored_llama_3_1_8b/rsft_train.jsonl --num_epochs 3 --output_dir /root/autodl-tmp/rsft_output_llama_3_1_8b --seed 42 --quantize --bf16 --per_device_batch_size 2 --gradient_accumulation_steps 8 --wandb_project faith-evidence-ie --wandb_run_name plan_016_llama_rsft_train_r2\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:2\"], \"pid\": 405397, \"log_path\": \"/root/runs/faith-evidence-ie/plan_016_llama_rsft_train_r2.log\", \"data_path\": \"/root/autodl-tmp/rsft_scored_llama_3_1_8b/rsft_train.jsonl\", \"data_count\": 8829, \"model_name\": \"Meta-Llama-3.1-8B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/sft_output_llama_3_1_8b\", \"eval_data\": \"rsft_scored_llama_3_1_8b\", \"fix\": \"added --quantize --bf16 --per_device_batch_size 2 --gradient_accumulation_steps 8 (R1 OOM due to fp32 loading without quantize flag)\", \"total_steps\": 1656, \"estimated_hours\": 4.4}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-17T03:26:02.383Z\"}, \"plan_016_llama_rsft_train\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T03:03:03.349Z\", \"updated_at\": \"2026-05-17T03:10:51.973Z\", \"hypothesis\": \"LLaMA-3.1-8B RSFT training on CED-filtered candidates (8829 samples, top_k=1) should improve rel_f1 over SFT baseline (0.5514), validating that the CED-RSFT pipeline generalizes across model families (Qwen→LLaMA).\", \"parent\": \"plan_016_llama_ced_scoring\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B --sft_adapter /root/autodl-tmp/sft_output_llama_3_1_8b --rsft_data_path /root/autodl-tmp/rsft_scored_llama_3_1_8b/rsft_train.jsonl --num_epochs 3 --output_dir /root/autodl-tmp/rsft_output_llama_3_1_8b --seed 42 --wandb_run_name plan_016_llama_rsft_train\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:2\"], \"pid\": 404050, \"data_path\": \"/root/autodl-tmp/rsft_scored_llama_3_1_8b\", \"data_count\": 8829, \"model_name\": \"Meta-Llama-3.1-8B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/sft_output_llama_3_1_8b\", \"eval_data\": \"rsft_scored_llama_3_1_8b\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-17T03:10:51.973Z\"}, \"plan_016_llama_ced_scoring\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T01:38:57.773Z\", \"updated_at\": \"2026-05-17T03:05:35.479Z\", \"hypothesis\": \"CED scoring (NLI-based contrastive discrimination) on LLaMA-3.1-8B RSFT candidates will produce filtered training data that improves RSFT quality, consistent with Qwen3-4B CED results.\", \"parent\": \"plan_016_llama_rsft_candidates_r3\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=2 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_score_filter --input_dir /root/autodl-tmp/rsft_candidates_llama_3_1_8b --output_path /root/autodl-tmp/rsft_scored_llama_3_1_8b --nli_model_path cross-encoder/nli-deberta-v3-base --nli_device cuda:0 --scoring_mode ced --tau 0.5 --selection_strategy top_k --top_k 3\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:2\"], \"pid\": \"398949\", \"data_path\": \"/root/autodl-tmp/rsft_candidates_llama_3_1_8b\", \"data_count\": 23704, \"model_name\": \"cross-encoder/nli-deberta-v3-base\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/plan_016_llama_ced_scoring.log\", \"checkpoint_path\": \"/root/autodl-tmp/rsft_scored_llama_3_1_8b\", \"checkpoint_source\": \"/root/autodl-tmp/rsft_candidates_llama_3_1_8b\", \"eval_data\": \"docred_train_candidates_llama_8b\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T03:05:35.479Z\"}, \"plan_006_qwen3_1_7b_ced_scoring\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T00:59:40.455Z\", \"updated_at\": \"2026-05-17T02:59:29.871Z\", \"hypothesis\": \"CED scoring (NLI contrastive discrimination) can effectively filter 1.7B model candidates despite lower generation quality: NLI-based selection should identify high-quality evidence samples even from a capacity-limited generator.\", \"parent\": \"plan_006_qwen3_1_7b_rsft_candidates\", \"spec\": {\"command\": \"python -m freige.training.rsft_score_filter --input_dir /root/autodl-tmp/freige/outputs/rsft_candidates_1_7b --output_path /root/autodl-tmp/freige/outputs/rsft_scored_1_7b --nli_model_path cross-encoder/nli-deberta-v3-base --nli_device cuda:0 --scoring_mode ced --tau 0.5 --selection_strategy top_k --top_k 3\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:0\", \"pid\": 395619, \"data_path\": \"/root/autodl-tmp/freige/outputs/rsft_candidates_1_7b\", \"data_count\": 24216, \"model_name\": \"cross-encoder/nli-deberta-v3-base\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/freige/outputs/rsft_candidates_1_7b\", \"eval_data\": \"docred train candidates\", \"log_path\": \"~/runs/faith-evidence-ie/plan_006_qwen3_1_7b_ced_scoring.log\", \"checkpoint_path\": \"/root/autodl-tmp/freige/outputs/rsft_scored_1_7b\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T02:59:28.237Z\", \"metrics\": {\"total_records\": 24216, \"selected\": 9042, \"unique_docs\": 3021, \"selection_rate\": 0.373, \"mean_f1_reward\": 0.592, \"mean_ced_reward\": 0.559, \"mean_combined_score\": 0.66, \"truncated_count\": 2920, \"truncated_mean_f1\": 0.439, \"non_truncated_mean_f1\": 0.613}}, \"plan_007_redocred_rsft_eval_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T16:25:37.094Z\", \"updated_at\": \"2026-05-17T02:56:32.555Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510 --data_path /root/autodl-tmp/data/re-docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/plan_007_redocred_rsft_eval_r2\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:1\", \"pid\": 363317, \"data_path\": \"/root/autodl-tmp/data/re-docred\", \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/rsft_output_ced_s43/checkpoint-510\", \"eval_data\": \"re-docred/dev\", \"hypothesis\": \"Re-DocRED RSFT eval r2: verify CED-RSFT improvement transfers cross-dataset. Compare vs SFT baseline Ign-F1=0.3659 (D080).\", \"plan_id\": \"plan_007\", \"parent\": \"plan_007_redocred_4b_sft_eval_r2\", \"log_path\": \"/tmp/plan_007_redocred_rsft_eval_r2.log\"}, \"pid\": 363317, \"metrics\": {\"F1\": 0.0025, \"Ign-F1\": 0.0026, \"Evi-F1\": 0.8837, \"EDCR\": 0.9978, \"format_ok\": \"489/493\", \"truncated\": \"117/493\", \"predictions\": 8461}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/eval_results/plan_007_redocred_rsft_eval_r2\", \"completed_at\": \"2026-05-16T17:33:20.838Z\", \"notes\": \"⚠️ NEGATIVE: F1=0.0025 (catastrophic), Evi-F1=0.8837, EDCR=0.9978. SFT baseline on same data = 0.3659 (normal). Framing 调整提案已提交 Director (2026-05-16). 大概率 pipeline bug (adapter loading / prompt format / relation label mapping). Diagnostic Worker dispatched. 等 Director 选 A/B/C narrative 再决定下一步。\", \"hypothesis\": \"CED-RSFT improvements on DocRED should transfer to Re-DocRED: RSFT model should outperform SFT baseline on Re-DocRED Ign-F1, demonstrating cross-dataset generalization of rejection sampling gains.\"}, \"plan_006_qwen3_1_7b_rsft_candidates\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T13:51:15.410Z\", \"updated_at\": \"2026-05-17T02:56:30.210Z\", \"hypothesis\": \"Qwen3-1.7B RSFT candidate generation (N=8, T=0.7). Scale ablation: smallest model RSFT candidates for CED scoring. plan_006 claim=3.\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:0\", \"spec\": {\"model_name\": \"Qwen3-1.7B\", \"sft_adapter\": \"/root/autodl-tmp/sft_output_qwen3_1_7b_bf16\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 3027, \"seed\": 42, \"output_dir\": \"/root/autodl-tmp/freige/outputs/rsft_candidates_1_7b\", \"config\": {\"num_generations\": 8, \"temperature\": 0.7, \"batch_size\": 1, \"split\": \"train\"}, \"command\": \"RSFT candidate generation N=8, T=0.7 for Qwen3-1.7B\", \"server\": \"rtx5090-4x\", \"checkpoint_path\": \"/root/autodl-tmp/freige/outputs/rsft_candidates_1_7b\", \"log_path\": \"~/runs/faith-evidence-ie/plan_006_qwen3_1_7b_rsft_candidates.log\"}, \"conclusion\": \"success\", \"reproduce\": {\"finished_at\": \"2026-05-17T00:59:21.916Z\"}, \"metrics\": {\"docs_completed\": 3027, \"total_generations\": 24216, \"lines\": 24216, \"runtime_h\": 11, \"truncation_rate\": 0.104, \"mean_diversity\": 7.4}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T00:59:26.947779+00:00\"}]}, \"completed_at\": \"2026-05-17T00:59:31.249Z\", \"parent\": \"plan_006_qwen3_1_7b_sft_bf16\"}, \"plan_002_test_eval_s44_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T08:14:36.494Z\", \"updated_at\": \"2026-05-17T02:56:29.283Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_s44/checkpoint-510 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split test --batch_size 4 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/test_rsft_ced_s44 --no-quantize\", \"server\": \"rtx5090-4x\", \"gpu_id\": 1, \"pid\": 319632, \"data_path\": \"/root/autodl-tmp/data/docred/test.json\", \"data_count\": 1000, \"model_name\": \"Qwen3-4B + SFT + RSFT-CED-s44-ckpt510\", \"seed\": 42, \"hypothesis\": \"DocRED test set evaluation with RSFT CED s44 (best config). D076 协议. plan_id=plan_002, claim=1.\", \"parent\": \"mvp2_rsft_train_r1_s44\", \"checkpoint_source\": \"/root/autodl-tmp/rsft_output_s44/checkpoint-510\", \"eval_data\": \"/root/autodl-tmp/data/docred/test.json\", \"log_path\": \"/root/autodl-tmp/eval_results/test_rsft_ced_s44/eval.log\", \"metrics\": {\"n_documents\": 1000, \"n_predictions\": 26925, \"n_codalab_entries\": 25553, \"format_ok_rate\": 0.996, \"n_truncated\": 626, \"inference_time_s\": 13850.5}, \"checkpoint_path\": \"/root/autodl-tmp/eval_results/test_rsft_ced_s44\", \"notes\": \"Test set eval complete. No local F1 (need CodaLab submission). File: codalab_submission.json (25553 entries).\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T12:06:04.702Z\", \"hypothesis\": \"DocRED test set evaluation for RSFT-CED s44 (best dev config). Final benchmark numbers for paper submission; test set performance confirms dev set gains are not overfitting artifacts.\"}, \"plan_006_qwen3_8b_no_evidence_sft\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T09:30:57.988Z\", \"updated_at\": \"2026-05-17T02:56:26.471Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.training.sft_trainer --model_name /root/autodl-tmp/models/Qwen/Qwen3-8B --data_dir /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/sft_output_qwen3_8b_no_evidence --no_evidence --no-quantize --seed 42 --wandb_run_name qwen3_8b_no_evidence_sft\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 3027, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"plan_id\": \"plan_006\", \"hypothesis\": \"8B no-evidence SFT ablation (bf16 LoRA). 与 plan_006_qwen3_8b_sft_bf16 对比量化 evidence generation cost on 8B model. claim=1.\", \"quantize\": \"none (bf16 LoRA)\", \"lora_rank\": 64, \"lora_alpha\": 128, \"output_dir\": \"/root/autodl-tmp/sft_output_qwen3_8b_no_evidence\", \"log_path\": \"/root/autodl-tmp/logs/plan_006_qwen3_8b_no_evidence_sft.log\", \"pid\": 325491, \"wandb_run_name\": \"qwen3_8b_no_evidence_sft\", \"checkpoint_path\": \"/root/autodl-tmp/sft_output_qwen3_8b_no_evidence\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T10:34:35.201Z\", \"metrics\": {\"train_loss\": 0.6509, \"eval_loss\": 0.8153, \"eval_mean_token_accuracy\": 0.8174, \"eval_entropy\": 0.6275, \"train_runtime_sec\": 3656, \"epoch\": 3}, \"hypothesis\": \"Qwen3-8B no-evidence SFT baseline for evidence tax measurement at 8B scale. If 8B no-evi rel_f1 ≈ 8B evidence-SFT rel_f1, confirms that 8B absorbs evidence cost (tax≈0).\"}, \"plan_006_qwen3_1_7b_no_evidence_sft\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:32:23.806Z\", \"updated_at\": \"2026-05-17T02:56:15.512Z\", \"spec\": {\"hypothesis\": \"Qwen3-1.7B no-evidence SFT ablation（复现 plan_014），验证 evidence generation 代价在小模型上是否成立。plan_id=plan_006, claim=1。\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=2 HF_HOME=/root/autodl-tmp/.hf_cache PYTHONUNBUFFERED=1 python -m freige.training.sft_trainer --model_name /root/autodl-tmp/models/Qwen/Qwen3-1.7B --data_dir /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/sft_output_qwen3_1_7b_no_evidence --seed 42 --wandb_run_name qwen3_1_7b_no_evidence_sft --no-quantize --no_evidence\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:2\"], \"account\": \"root\", \"model_name\": \"Qwen3-1.7B\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 3027, \"seed\": 42, \"plan_id\": \"plan_006\", \"lora_rank\": 64, \"lora_alpha\": 128, \"quantize\": \"none (bf16 LoRA)\", \"num_epochs\": 3, \"batch_size\": 1, \"gradient_accumulation_steps\": 16, \"learning_rate\": 0.0002, \"output_dir\": \"/root/autodl-tmp/sft_output_qwen3_1_7b_no_evidence\", \"log_path\": \"~/runs/faith-evidence-ie/plan_006_qwen3_1_7b_no_evidence_sft.log\", \"pid\": \"321094\", \"backend\": \"nohup\", \"notes\": \"r1 (PID 317798) 完成 570 steps，最终模型保存于 16:32:46。r2 (PID 321094/321100) 冗余重复，已 kill 释放 cuda:2\", \"checkpoint_path\": \"/root/autodl-tmp/sft_output_qwen3_1_7b_no_evidence\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T09:05:18.259Z\", \"hypothesis\": \"Qwen3-1.7B no-evidence SFT baseline for evidence tax measurement at 1.7B scale. Paired with evidence-SFT to quantify whether evidence generation constrains or helps small model RE performance.\"}, \"plan_006_qwen3_1_7b_sft_bf16\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T06:36:26.212Z\", \"updated_at\": \"2026-05-17T02:56:13.858Z\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=3 HF_HOME=/root/autodl-tmp/.hf_cache PYTHONUNBUFFERED=1 python -m freige.training.sft_trainer --model_name /root/autodl-tmp/models/Qwen/Qwen3-1.7B --data_dir /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/sft_output_qwen3_1_7b_bf16 --seed 42 --wandb_run_name qwen3_1_7b_sft_bf16 --no-quantize\", \"server\": \"rtx5090-4x\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 3027, \"model_name\": \"Qwen3-1.7B\", \"seed\": 42, \"pid\": \"310381\", \"gpu\": [\"cuda:3\"], \"log_path\": \"~/runs/faith-evidence-ie/plan_006_qwen3_1_7b_sft_bf16.log\", \"backend\": \"tmux\", \"account\": \"root\", \"lora_rank\": 64, \"lora_alpha\": 128, \"target_modules\": 7, \"quantize\": \"none (bf16 LoRA)\", \"trainable_params\": \"69.7M / 1.79B (3.89%)\", \"num_epochs\": 3, \"batch_size\": 1, \"gradient_accumulation_steps\": 16, \"learning_rate\": 0.0002, \"output_dir\": \"/root/autodl-tmp/sft_output_qwen3_1_7b_bf16\", \"hypothesis\": \"Model size ablation: Qwen3-1.7B bf16 LoRA SFT（与 4B 训练 regime 一致），验证 evidence tax 在小模型上的表现。plan_id=plan_006, claim=1。\", \"checkpoint_path\": \"/root/autodl-tmp/sft_output_qwen3_1_7b_bf16/checkpoint-570\"}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.6884, \"eval_loss\": 0.8031, \"eval_mean_token_accuracy\": 0.8238, \"eval_entropy\": 0.682, \"train_runtime_sec\": 2473, \"train_samples_per_second\": 3.672, \"epochs\": 3, \"total_steps\": 570}, \"completed_at\": \"2026-05-16T08:33:12.198Z\", \"hypothesis\": \"Qwen3-1.7B bf16 LoRA SFT training for evidence-grounded DocRE. Scale ablation: smallest model expected to show highest evidence tax due to capacity-constrained multi-task optimization.\"}, \"plan_006_qwen3_8b_sft_bf16\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:50:55.793Z\", \"updated_at\": \"2026-05-17T02:56:12.064Z\", \"spec\": {\"hypothesis\": \"Model size ablation: Qwen3-8B bf16 LoRA SFT（与 4B/1.7B 训练 regime 一致），验证 evidence generation pipeline 在大模型上的表现。plan_id=plan_006, claim=1。\", \"model_name\": \"Qwen3-8B\", \"server\": \"rtx5090-4x\", \"plan_id\": \"plan_006\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=3 HF_HOME=/root/autodl-tmp/.hf_cache PYTHONUNBUFFERED=1 python -m freige.training.sft_trainer --model_name /root/autodl-tmp/models/Qwen/Qwen3-8B --data_dir /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/sft_output_qwen3_8b_bf16 --no-quantize --seed 42 --wandb_run_name qwen3_8b_sft_bf16\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 3027, \"seed\": 42, \"pid\": \"317310\", \"gpu\": [\"cuda:3\"], \"log_path\": \"~/runs/faith-evidence-ie/plan_006_qwen3_8b_sft_bf16.log\", \"backend\": \"tmux\", \"account\": \"root\", \"lora_rank\": 64, \"lora_alpha\": 128, \"target_modules\": 7, \"quantize\": \"none (bf16 LoRA)\", \"trainable_params\": \"174.6M / 8.37B (2.09%)\", \"num_epochs\": 3, \"batch_size\": 1, \"gradient_accumulation_steps\": 16, \"learning_rate\": 0.0002, \"output_dir\": \"/root/autodl-tmp/sft_output_qwen3_8b_bf16\", \"checkpoint_path\": \"N/A\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T09:09:26.703Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T09:09:27.373Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T09:09:32.119544+00:00\"}]}, \"metrics\": {\"train_loss\": 0.5705, \"eval_loss\": 0.7186, \"eval_mean_token_accuracy\": 0.8377, \"eval_entropy\": 0.5614, \"train_runtime_s\": 3932, \"epoch\": 3}, \"notes\": \"训练正常完成，cron 误判(无W&B/sentinel)。Qwen3-8B bf16 LoRA SFT 3ep, train_loss=0.5705, eval_acc=0.8377。checkpoint: /root/autodl-tmp/sft_output_qwen3_8b_bf16。下一步: RSFT + eval。\", \"hypothesis\": \"Qwen3-8B bf16 LoRA SFT training for evidence-grounded DocRE. Scale ablation: larger model should achieve higher rel_f1 than 4B (0.4057) and 1.7B baselines, with lower evidence tax due to greater capacity.\"}, \"reeval_sft_baseline_d076\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T05:26:37.542Z\", \"updated_at\": \"2026-05-17T02:56:09.813Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/sft_baseline_d076_reeval --no-quantize\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"303065\", \"log_path\": \"~/runs/faith-evidence-ie/reeval_sft_baseline_d076.log\", \"submitted_at\": \"2026-05-16T05:26:46.170Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + SFT baseline (no RSFT)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"docred dev (985 docs)\", \"checkpoint_path\": \"/root/autodl-tmp/sft_output\", \"output_dir\": \"/root/autodl-tmp/eval_results/sft_baseline_d076_reeval\", \"wall_clock_seconds\": 11187.5, \"gpu_hours\": 3.11}, \"reproduce\": {\"finished_at\": \"2026-05-16T07:25:48.637Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T07:25:54.520626+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"rel_f1\": 0.4049, \"ign_f1\": 0.3974, \"evi_f1\": 0.7986, \"edcr\": 0.6982, \"evi_f1_joint\": 0.3147, \"format_compliance_rate\": 0.998, \"n_truncated\": 288, \"n_documents\": 985, \"n_predictions\": 16880, \"inference_time_sec\": 7056.5}, \"completed_at\": \"2026-05-16T08:33:13.622Z\", \"hypothesis\": \"Re-eval Qwen3-4B SFT baseline under D076 unified protocol (batch_size=4, no-quantize, max_new_tokens=1024, seed=42). Required as canonical comparison point for all RSFT/GRPO experiments and evidence tax computation.\"}, \"plan_006_qwen3_1_7b_sft_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T08:14:26.923Z\", \"updated_at\": \"2026-05-17T02:56:02.886Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/eval_results/qwen3_1_7b_sft_eval\", \"log_path\": \"~/runs/faith-evidence-ie/plan_006_qwen3_1_7b_sft_eval.log\"}, \"conclusion\": \"success\", \"metrics\": {\"f1\": 0.4945, \"ign_f1\": 0.4786, \"evi_f1\": 0.8316, \"edcr\": 0.6704, \"precision\": 0.5085, \"recall\": 0.4813, \"ign_precision\": 0.483, \"ign_recall\": 0.4743, \"evi_precision\": 0.8203, \"evi_recall\": 0.8432, \"evi_f1_joint\": 0.3958, \"format_compliance_rate\": 1, \"n_predictions\": 17184, \"n_truncated\": 314, \"inference_time_seconds\": 6848.7}, \"completed_at\": \"2026-05-16T10:08:26.496Z\", \"hypothesis\": \"Qwen3-1.7B evidence-SFT eval under D076 protocol. Establishes smallest-scale SFT baseline; evidence tax at 1.7B predicted negative (evidence helps small models by constraining over-prediction).\", \"parent\": \"plan_006_qwen3_1_7b_sft_bf16\"}, \"plan_006_qwen3_8b_sft_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T09:03:35.743Z\", \"updated_at\": \"2026-05-17T02:56:01.221Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen/Qwen3-8B --sft_adapter /root/autodl-tmp/sft_output_qwen3_8b_bf16 --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/qwen3_8b_sft_eval --no-quantize\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 12275, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/sft_output_qwen3_8b_bf16\", \"eval_data\": \"docred-dev\", \"hypothesis\": \"Model size ablation: Qwen3-8B SFT eval on dev set. plan_006 claim=1.\", \"plan_id\": \"plan_006\", \"parent\": \"plan_006_qwen3_8b_sft_bf16\", \"pid\": 322966, \"log_path\": \"/root/autodl-tmp/eval_results/qwen3_8b_sft_eval.log\", \"checkpoint_path\": \"/root/autodl-tmp/sft_output_qwen3_8b_bf16\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T11:05:48.273Z\", \"metrics\": {\"ign_f1\": 0.5051, \"f1\": 0.5262, \"evi_f1\": 0.8188, \"edcr\": 0.651, \"format_ok_rate\": 0.999, \"n_truncated\": 313, \"n_predictions\": 17401, \"inference_time_s\": 7206}, \"hypothesis\": \"Qwen3-8B evidence-SFT eval under D076 unified protocol. Establishes 8B-scale SFT baseline for evidence tax measurement (paired with no-evidence eval) and RSFT improvement quantification.\", \"parent\": \"plan_006_qwen3_8b_sft_bf16\"}, \"plan_016_llama_3_1_8b_no_evidence_sft\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T11:06:47.006Z\", \"updated_at\": \"2026-05-17T02:55:47.936Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.training.sft_trainer --model_name /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B --data_dir /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/sft_output_llama_3_1_8b_no_evidence --no-quantize --no_evidence --seed 42 --wandb_run_name llama_3_1_8b_no_evidence_sft\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 3027, \"model_name\": \"Meta-Llama-3.1-8B\", \"seed\": 42, \"plan_id\": \"plan_016\", \"hypothesis\": \"Cross-family no-evidence SFT: LLaMA-3.1-8B bf16 LoRA. Evidence tax cross-family validation. claim=1.\", \"quantize\": \"none (bf16 LoRA)\", \"lora_rank\": 64, \"lora_alpha\": 128, \"output_dir\": \"/root/autodl-tmp/sft_output_llama_3_1_8b_no_evidence\", \"log_path\": \"/root/autodl-tmp/sft_output_llama_3_1_8b_no_evidence/checkpoint-570/trainer_state.json\", \"pid\": 333911, \"checkpoint_path\": \"/root/autodl-tmp/sft_output_llama_3_1_8b_no_evidence\", \"metrics\": {\"train_loss\": 0.456, \"train_token_accuracy\": 0.8816, \"eval_loss\": 0.8412, \"eval_token_accuracy\": 0.815, \"epochs\": 3, \"total_steps\": 570, \"final_lr\": 3.697e-07}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T12:05:08.263Z\", \"hypothesis\": \"LLaMA-3.1-8B no-evidence SFT baseline for cross-family evidence tax measurement. Paired with evidence-SFT to quantify evidence generation cost on a non-Qwen architecture at 8B scale.\"}, \"plan_016_llama_3_1_8b_sft\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T10:35:41.618Z\", \"updated_at\": \"2026-05-17T02:55:46.226Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.training.sft_trainer --model_name /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B --data_dir /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/sft_output_llama_3_1_8b --no-quantize --seed 42 --wandb_run_name llama_3_1_8b_sft\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 3027, \"model_name\": \"Meta-Llama-3.1-8B\", \"seed\": 42, \"plan_id\": \"plan_016\", \"hypothesis\": \"Cross-family SFT: LLaMA-3.1-8B bf16 LoRA with-evidence SFT. 验证 evidence pipeline 跨模型家族泛化性. claim=1/2.\", \"quantize\": \"none (bf16 LoRA)\", \"lora_rank\": 64, \"lora_alpha\": 128, \"output_dir\": \"/root/autodl-tmp/sft_output_llama_3_1_8b\", \"log_path\": \"/root/autodl-tmp/logs/plan_016_llama_3_1_8b_sft.log\", \"pid\": 331871, \"wandb_run_name\": \"llama_3_1_8b_sft\", \"metrics\": {\"train_loss\": 0.5246, \"eval_loss\": 0.7363, \"token_acc\": 0.8361}, \"checkpoint_path\": \"/root/autodl-tmp/sft_output_llama_3_1_8b\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T11:40:36.505Z\", \"hypothesis\": \"LLaMA-3.1-8B can be SFT-trained for evidence-grounded DocRE with the same pipeline as Qwen3 family, enabling cross-family generalization claims for the FREIGE framework.\"}, \"plan_007_redocred_4b_sft_eval_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T12:36:01.717Z\", \"updated_at\": \"2026-05-17T02:55:43.842Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=0 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/re-docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/plan_007_redocred_4b_sft_eval\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"342711\", \"log_path\": \"~/runs/faith-evidence-ie/plan_007_redocred_4b_sft_eval_r2.log\", \"submitted_at\": \"2026-05-16T12:36:27.149Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 3698.9, \"gpu_hours\": 1.03}, \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:0\", \"pid\": \"342711\", \"log_path\": \"~/runs/faith-evidence-ie/plan_007_redocred_4b_sft_eval_r2.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=0 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/re-docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/plan_007_redocred_4b_sft_eval\\\"\", \"finished_at\": \"2026-05-16T13:31:53.985Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T13:31:58.248381+00:00\"}]}, \"metrics\": {\"ign_f1\": 0.3659, \"f1\": 0.3706, \"evi_f1\": 0.817, \"edcr\": 0.6674, \"format_compliance_rate\": 0.996, \"n_truncated\": 139, \"n_total\": 493, \"inference_time_seconds\": 3281.7, \"precision\": 0.4316, \"recall\": 0.3247, \"ign_precision\": 0.4134, \"ign_recall\": 0.3282, \"evi_precision\": 0.8208, \"evi_recall\": 0.8131, \"n_predictions\": 8191}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/eval_results/plan_007_redocred_4b_sft_eval\", \"completed_at\": \"2026-05-16T13:38:06.043Z\", \"hypothesis\": \"FREIGE SFT model trained on DocRED transfers to Re-DocRED without re-training: if Ign-F1 drop <5pp and Evi-F1 maintains, the learned evidence grounding generalizes across annotation schemes.\", \"parent\": \"reeval_sft_baseline_d076\"}, \"plan_006_qwen3_8b_no_evidence_eval_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T11:17:39.361Z\", \"updated_at\": \"2026-05-17T02:55:34.661Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen/Qwen3-8B --sft_adapter /root/autodl-tmp/sft_output_qwen3_8b_no_evidence --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --no_evidence --output_dir /root/autodl-tmp/eval_results/qwen3_8b_no_evidence_eval_v2\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:2\"], \"pid\": 335357, \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 12275, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/sft_output_qwen3_8b_no_evidence\", \"eval_data\": \"docred-dev\", \"log_path\": \"/root/autodl-tmp/eval_results/qwen3_8b_no_evidence_eval_v2.log\", \"hypothesis\": \"8B no-evidence SFT eval v2 (with --no_evidence flag). Fix v1 prompt mismatch bug. plan_006 claim=1.\", \"plan_id\": \"plan_006\", \"parent\": \"plan_006_qwen3_8b_no_evidence_sft\", \"checkpoint_path\": \"/root/autodl-tmp/sft_output_qwen3_8b_no_evidence\", \"metrics\": {\"ign_f1\": 0.5079, \"rel_f1\": 0.5283, \"evi_f1\": 0, \"edcr\": 0, \"format_compliance_rate\": 0.9949, \"n_total\": 985, \"n_parseable\": 980, \"n_truncated\": 225, \"inference_time_seconds\": 6402.2}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T13:06:41.968Z\", \"hypothesis\": \"8B model capacity absorbs evidence generation cost: no-evidence SFT and evidence-SFT should produce near-identical rel_f1, demonstrating evidence tax≈0 at 8B scale (contrasting with 4B where tax=-7.5pp).\", \"parent\": \"plan_006_qwen3_8b_no_evidence_sft\"}, \"plan_016_llama_3_1_8b_no_evidence_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T12:05:53.861Z\", \"updated_at\": \"2026-05-17T02:55:31.810Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=3 python -m freige.eval.inference --model_path /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B --sft_adapter /root/autodl-tmp/sft_output_llama_3_1_8b_no_evidence --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --no_evidence --output_dir /root/autodl-tmp/eval_results/llama_3_1_8b_no_evidence_eval\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"339687\", \"log_path\": \"~/runs/faith-evidence-ie/plan_016_llama_3_1_8b_no_evidence_eval.log\", \"submitted_at\": \"2026-05-16T12:06:19.840Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 5374.3, \"gpu_hours\": 1.49}, \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:3\", \"pid\": \"339687\", \"log_path\": \"~/runs/faith-evidence-ie/plan_016_llama_3_1_8b_no_evidence_eval.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=3 python -m freige.eval.inference --model_path /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B --sft_adapter /root/autodl-tmp/sft_output_llama_3_1_8b_no_evidence --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --no_evidence --output_dir /root/autodl-tmp/eval_results/llama_3_1_8b_no_evidence_eval\\\"\", \"finished_at\": \"2026-05-16T13:26:57.202Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T13:27:03.265903+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"ign_f1\": 0.5452, \"rel_f1\": 0.5624, \"evi_f1\": 0, \"edcr\": 0}, \"checkpoint_path\": \"/root/autodl-tmp/eval_results/llama_3_1_8b_no_evidence_eval\", \"completed_at\": \"2026-05-16T13:35:54.177Z\", \"hypothesis\": \"LLaMA-3.1-8B no-evidence SFT should achieve similar rel_f1 to evidence-SFT (tax≈0), cross-family validating the 8B-scale evidence absorption pattern observed in Qwen3-8B.\", \"parent\": \"plan_016_llama_3_1_8b_no_evidence_sft\"}, \"plan_006_qwen3_1_7b_no_evidence_eval_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T11:45:02.749Z\", \"updated_at\": \"2026-05-17T02:55:24.084Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen/Qwen3-1.7B --sft_adapter /root/autodl-tmp/sft_output_qwen3_1_7b_no_evidence --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --no_evidence --output_dir /root/autodl-tmp/eval_results/qwen3_1_7b_no_evidence_eval_v3\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 12275, \"model_name\": \"Qwen3-1.7B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/sft_output_qwen3_1_7b_no_evidence\", \"eval_data\": \"docred-dev\", \"hypothesis\": \"Model size ablation: Qwen3-1.7B no-evidence SFT eval (v3, fix bash-c wrapping). plan_006 claim=1.\", \"plan_id\": \"plan_006\", \"parent\": \"plan_006_qwen3_1_7b_no_evidence_sft\", \"pid\": 337839}, \"reproduce\": {\"finished_at\": \"2026-05-16T13:51:46.819Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T13:51:51.769349+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"ign_f1\": 0.3982, \"rel_f1\": 0.4103, \"evi_f1\": 0, \"edcr\": 0, \"precision\": 0.4464, \"recall\": 0.3796, \"format_compliance_rate\": 1, \"n_truncated\": 501, \"inference_time_seconds\": 7465.3, \"evidence_tax\": 0.0804}, \"checkpoint_path\": \"/root/autodl-tmp/eval_results/qwen3_1_7b_no_evidence_eval_v3\", \"log_path\": \"N/A\", \"completed_at\": \"2026-05-16T13:54:19.362Z\", \"hypothesis\": \"1.7B model capacity is insufficient to jointly optimize RE and evidence generation: no-evidence SFT should outperform evidence-SFT on rel_f1, revealing positive evidence tax at small scale (opposite to 8B where tax≈0).\", \"parent\": \"plan_006_qwen3_1_7b_no_evidence_sft\"}, \"plan_016_llama_3_1_8b_sft_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T12:06:49.282Z\", \"updated_at\": \"2026-05-17T02:55:20.475Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=1 python -m freige.eval.inference --model_path /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B --sft_adapter /root/autodl-tmp/sft_output_llama_3_1_8b --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/llama_3_1_8b_sft_eval\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"340111\", \"log_path\": \"~/runs/faith-evidence-ie/plan_016_llama_3_1_8b_sft_eval.log\", \"submitted_at\": \"2026-05-16T12:07:11.141Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 7873.8, \"gpu_hours\": 2.19}, \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:1\", \"pid\": \"340111\", \"log_path\": \"~/runs/faith-evidence-ie/plan_016_llama_3_1_8b_sft_eval.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=1 python -m freige.eval.inference --model_path /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B --sft_adapter /root/autodl-tmp/sft_output_llama_3_1_8b --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/llama_3_1_8b_sft_eval\\\"\", \"finished_at\": \"2026-05-16T14:10:43.158Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T14:10:47.089855+00:00\"}]}, \"metrics\": {\"ign_f1\": 0.5384, \"rel_f1\": 0.5514, \"evi_f1\": 0.8151, \"edcr\": 0.628, \"precision\": 0.5464, \"recall\": 0.5565, \"evi_f1_joint\": 0.4317, \"format_compliance_rate\": 0.9949, \"n_truncated\": 197, \"n_predictions\": 15325, \"inference_time_seconds\": 7331.3, \"evidence_tax_ign_f1\": 0.0068, \"evidence_tax_rel_f1\": 0.011}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/sft_output_llama_3_1_8b\", \"completed_at\": \"2026-05-16T14:18:24.910Z\", \"hypothesis\": \"LLaMA-3.1-8B SFT with evidence generation should achieve comparable rel_f1 to Qwen3-8B SFT, establishing cross-family baseline for evidence tax measurement. Evidence tax at 8B scale predicted near-zero based on Qwen3-8B pattern.\", \"parent\": \"plan_016_llama_3_1_8b_sft\"}, \"plan_016_llama_grpo_qlora\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T13:14:37.199Z\", \"updated_at\": \"2026-05-17T02:55:08.871Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 TRANSFORMERS_OFFLINE=1 python -m freige.training.grpo_trainer --model_name /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B --sft_adapter /root/autodl-tmp/sft_output_llama_3_1_8b --data_dir /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/grpo_output_llama_3_1_8b_qlora --stage 3 --num_generations 4 --lora_rank 64 --per_device_batch_size 1 --gradient_accumulation_steps 16 --max_length 4096 --max_new_tokens 1024 --kl_coef 0 --bf16 --seed 42 --wandb_run_name plan_016_llama_grpo_qlora --nli_model /root/autodl-tmp/.hf_cache/models--cross-encoder--nli-deberta-v3-base/snapshots/6c749ce3425cd33b46d187e45b92bbf96ee12ec7\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:2\", \"pid\": 346621, \"model_name\": \"Meta-Llama-3.1-8B\", \"sft_adapter\": \"/root/autodl-tmp/sft_output_llama_3_1_8b\", \"seed\": 42, \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 3027, \"checkpoint_source\": \"/root/autodl-tmp/sft_output_llama_3_1_8b\", \"output_dir\": \"/root/autodl-tmp/grpo_output_llama_3_1_8b_qlora\", \"hypothesis\": \"LLaMA-3.1-8B GRPO QLoRA (4-bit, G=4, CED reward, kl_coef=0). Cross-family RL decoupling experiment. plan_016 claim=2.\", \"config\": {\"stage\": 3, \"num_generations\": 4, \"lora_rank\": 64, \"quantize\": true, \"kl_coef\": 0, \"per_device_batch_size\": 1, \"gradient_accumulation_steps\": 16, \"max_length\": 4096, \"max_new_tokens\": 1024, \"total_steps\": 757}, \"checkpoint_path\": \"/root/autodl-tmp/grpo_output_llama_3_1_8b_qlora\", \"log_path\": \"~/runs/faith-evidence-ie/plan_016_llama_grpo_qlora.log\"}, \"conclusion\": \"success\", \"metrics\": {\"format_reward\": 1, \"f1_reward\": 0, \"ced_reward\": 0, \"entropy\": 0.28, \"final_step\": 60, \"grad_norm\": 0, \"loss\": 0, \"frac_reward_zero_std\": 1, \"output_length_final\": 172, \"conclusion_note\": \"C2 cross-family validated: LLaMA QLoRA GRPO shows same catastrophic decoupling as Qwen (format gaming, zero IE ability)\"}, \"completed_at\": \"2026-05-16T15:51:16.213Z\", \"hypothesis\": \"QLoRA GRPO catastrophic decoupling (format gaming + zero IE ability) is not Qwen-specific: LLaMA-3.1-8B under identical QLoRA GRPO training should exhibit the same failure mode (grad_norm→0, loss→0, rel_f1→0). Cross-family validation of C2.\", \"parent\": \"mvp2_grpo_ced_lr5e6_r1\"}, \"plan_006_qwen3_8b_rsft_candidates\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T13:49:52.476Z\", \"updated_at\": \"2026-05-17T01:54:20.630Z\", \"hypothesis\": \"Qwen3-8B RSFT candidate generation (N=8, T=0.7). Generates rejection sampling candidates for subsequent CED scoring and filtering. plan_006 claim=3.\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:3\", \"spec\": {\"model_name\": \"Qwen3-8B\", \"sft_adapter\": \"/root/autodl-tmp/sft_output_qwen3_8b_bf16\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 3027, \"seed\": 42, \"output_dir\": \"/root/autodl-tmp/freige/outputs/rsft_candidates_8b\", \"config\": {\"num_generations\": 8, \"temperature\": 0.7, \"batch_size\": 1, \"split\": \"train\"}}, \"pid\": \"349382\", \"log_path\": \"~/runs/faith-evidence-ie/plan_006_qwen3_8b_rsft_candidates.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=3 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_generate --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --sft_adapter /root/autodl-tmp/sft_output_qwen3_8b_bf16 --num_generations 8 --temperature 0.7 --batch_size 1 --data_path /root/autodl-tmp/data/docred --split train --seed 42 --output_dir /root/autodl-tmp/freige/outputs/rsft_candidates_8b\\\"\", \"finished_at\": \"2026-05-17T01:51:04.422Z\"}, \"failure_reason\": \"EXIT_CODE=124 (timeout — exceeded timeout_hours)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-17T01:51:08.747Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T01:51:14.925166+00:00\"}]}}, \"plan_016_llama_rsft_candidates_r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T15:49:40.224Z\", \"updated_at\": \"2026-05-17T01:34:30.186Z\", \"spec\": {\"command\": \"python -m freige.training.rsft_generate --base_model /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B --sft_adapter /root/autodl-tmp/sft_output_llama_3_1_8b --num_generations 8 --temperature 0.7 --batch_size 1 --data_path /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/rsft_candidates_llama_3_1_8b --start_idx 64\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:2\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"model_name\": \"meta-llama/Meta-Llama-3.1-8B\", \"pid\": 360970, \"log_path\": \"~/runs/faith-evidence-ie/plan_016_llama_rsft_candidates_r3.log\", \"checkpoint_path\": \"/root/autodl-tmp/rsft_candidates_llama_3_1_8b\"}, \"hypothesis\": \"LLaMA-3.1-8B RSFT candidate gen r3 (N=8, T=0.7, start_idx=64 resume). Exclusive cuda:2 after GRPO kill.\", \"plan_id\": \"plan_016\", \"parent\": \"plan_016_llama_3_1_8b_sft\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T01:34:30.186Z\"}, \"plan_007_redocred_rsft_eval_r5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T22:04:18.834Z\", \"updated_at\": \"2026-05-17T00:51:25.706Z\", \"hypothesis\": \"CED-RSFT gains transfer to Re-DocRED (r5, correct 3-param loading: base→SFT→RSFT)\", \"parent\": \"plan_007_redocred_rsft_eval_r4\", \"spec\": {\"command\": \"python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/re-docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/plan_007_redocred_rsft_eval_r4\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:1\", \"pid\": 384691, \"data_path\": \"/root/autodl-tmp/data/re-docred\", \"data_count\": -1, \"model_name\": \"Qwen3-4B + SFT + RSFT-CED-s43-ckpt510\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/rsft_output_ced_s43/checkpoint-510\", \"eval_data\": \"re-docred dev\", \"log_path\": \"~/runs/faith-evidence-ie/plan_007_redocred_rsft_eval_r4.log\", \"checkpoint_path\": \"/root/autodl-tmp/rsft_output_ced_s43/checkpoint-510\"}, \"conclusion\": \"success\", \"metrics\": {\"f1\": 0.4234, \"ign_f1\": 0.4145, \"evi_f1\": 0.8182, \"edcr\": 0.621, \"evi_joint_f1\": 0.3306, \"format_compliance\": 1, \"field_compliance\": 0.8134, \"n_documents\": 493, \"n_truncated\": 90, \"inference_time_s\": 5655.5}, \"completed_at\": \"2026-05-17T00:51:25.707Z\"}, \"plan_007_redocred_rsft_eval_r4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T18:00:41.999Z\", \"updated_at\": \"2026-05-16T22:04:01.953Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510 --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/re-docred --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/plan_007_redocred_rsft_eval_r4\", \"server\": \"rtx5090-4x\", \"data_path\": \"/root/autodl-tmp/data/re-docred\", \"data_count\": -1, \"model_name\": \"Qwen3-4B RSFT ced_s43 checkpoint-510\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/rsft_output_ced_s43/checkpoint-510\", \"eval_data\": \"re-docred\", \"pid\": 370793}, \"hypothesis\": \"CED-RSFT gains transfer to Re-DocRED (r4, correct 3-param loading: base→SFT→RSFT)\", \"plan_id\": \"plan_007\", \"parent\": \"plan_007_redocred_4b_sft_eval_r2\", \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-16T21:07:21.170Z\"}, \"plan_002_test_rsft_s43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T17:45:04.744Z\", \"updated_at\": \"2026-05-16T21:07:17.492Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510 --data_path /root/autodl-tmp/data/docred --split test --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/plan_002_test_rsft_s43\", \"server\": \"rtx5090-4x\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": null, \"model_name\": \"Qwen3-4B + RSFT s43 ckpt-510\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/rsft_output_ced_s43/checkpoint-510\", \"eval_data\": \"docred/test.json\", \"parent\": \"rsft_ced_s43\"}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-16T21:07:17.492Z\"}, \"plan_007_redocred_rsft_eval_r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T17:38:09.825Z\", \"updated_at\": \"2026-05-16T21:07:14.348Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510 --data_path /root/autodl-tmp/data/re-docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/redocred_rsft_eval_r3\", \"server\": \"rtx5090-4x\", \"data_path\": \"/root/autodl-tmp/data/re-docred\", \"data_count\": null, \"model_name\": \"Qwen3-4B (CED-RSFT)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/rsft_output_ced_s43/checkpoint-510\", \"eval_data\": \"re-docred-dev\"}, \"hypothesis\": \"Re-DocRED RSFT eval r3 (config fix: model_path=base, sft_adapter=RSFT ckpt). Verify CED-RSFT gains transfer cross-dataset.\", \"plan_id\": \"plan_007\", \"parent\": \"plan_007_redocred_4b_sft_eval_r2\", \"gpu\": \"cuda:1\", \"pid\": 368363, \"conclusion\": \"failed\", \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"completed_at\": \"2026-05-16T21:07:14.348Z\"}, \"plan_007_redocred_rsft_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T14:23:56.999Z\", \"updated_at\": \"2026-05-16T17:49:00.578Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510 --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/re-docred --output_dir /root/autodl-tmp/eval_results/redocred_rsft_eval --batch_size 4 --max_new_tokens 1024 --split dev --seed 42 --no-quantize\", \"server\": \"rtx5090-4x\", \"data_path\": \"/root/autodl-tmp/data/re-docred\", \"data_count\": 500, \"model_name\": \"Qwen3-4B + SFT + CED-RSFT(s43)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/rsft_output_ced_s43/checkpoint-510\", \"eval_data\": \"re-docred/dev\", \"hypothesis\": \"CED-RSFT gains (rel_f1 improvement over SFT) transfer to Re-DocRED cross-dataset eval\", \"parent\": \"plan_007_redocred_4b_sft_eval_r2\", \"plan_id\": \"plan_007\", \"pid\": 352684, \"gpu\": \"cuda:1\", \"log_path\": \"/root/runs/faith-evidence-ie/plan_007_redocred_rsft_eval.log\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-16T14:48:19.318Z\", \"metrics\": {\"failure_reason\": \"OOM + pipeline bug: --model_path and --sft_adapter args in wrong order. RSFT LoRA merged to bare Qwen3-4B without SFT base, causing ontology collapse. Fix: match DocRED eval param ordering.\"}}, \"plan_014_no_evidence_eval_d076\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T14:26:29.748Z\", \"updated_at\": \"2026-05-16T17:37:09.823Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=1 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_no_evidence_output/ --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --no_evidence --output_dir /root/autodl-tmp/eval_results/plan_014_no_evidence_eval_d076\\\"\", \"server\": \"rtx5090-4x\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-4B (no-evidence SFT)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/sft_no_evidence_output/\", \"eval_data\": \"docred-dev\"}, \"hypothesis\": \"4B no-evidence SFT eval under D076 unified protocol (batch_size=4, max_new_tokens=1024, seed=42, no-quantize). Required for clean scaling comparison across 1.7B/4B/8B.\", \"plan_id\": \"plan_014\", \"parent\": \"plan_014_sft_no_evidence\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:1\", \"pid\": 353322, \"metrics\": {\"ign_f1\": 0.4721, \"f1\": 0.4876, \"precision\": 0.4901, \"recall\": 0.4851, \"format_compliance_rate\": 0.9929, \"n_truncated\": 307, \"inference_time_seconds\": 6903.9}, \"checkpoint_path\": \"/root/autodl-tmp/eval_results/plan_014_no_evidence_eval_d076\", \"log_path\": \"/root/runs/faith-evidence-ie/eval_plan_014_no_evidence_r2.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T16:22:20.324Z\"}, \"plan_016_llama_rsft_candidates_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T14:25:55.343Z\", \"updated_at\": \"2026-05-16T14:56:53.198Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -m freige.training.rsft_generate --base_model /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B --sft_adapter /root/autodl-tmp/sft_output_llama_3_1_8b --num_generations 8 --temperature 0.7 --batch_size 1 --data_path /root/autodl-tmp/data/docred --split train --seed 42 --output_dir /root/autodl-tmp/freige/outputs/rsft_candidates_llama_8b\", \"server\": \"rtx5090-4x\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 3027, \"model_name\": \"Meta-Llama-3.1-8B\", \"seed\": 42}, \"hypothesis\": \"LLaMA-3.1-8B RSFT candidate generation (N=8, T=0.7) for cross-family CED-RSFT validation\", \"gpu\": \"cuda:1\", \"pid\": 353179, \"log_path\": \"~/runs/faith-evidence-ie/plan_016_llama_rsft_candidates.log\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-16T14:56:50.729Z\", \"metrics\": {\"docs_completed\": 64, \"docs_total\": 3027, \"lines_generated\": 512, \"output_path\": \"/root/autodl-tmp/freige/outputs/rsft_candidates_llama_8b/generations.jsonl\", \"failure_reason\": \"Process killed externally (no traceback/error in log). Likely OOM on cuda:1. Completed 64/3027 docs (2.1%) in ~23min before termination.\"}}, \"plan_016_llama_rsft_candidates\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T14:15:59.880Z\", \"updated_at\": \"2026-05-16T14:25:29.851Z\", \"spec\": {\"model_name\": \"Meta-Llama-3.1-8B\", \"sft_adapter\": \"/root/autodl-tmp/sft_output_llama_3_1_8b\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 3027, \"seed\": 42, \"n_candidates\": 8, \"temperature\": 0.7, \"output_dir\": \"/root/autodl-tmp/rsft_candidates_llama_3_1_8b\", \"hypothesis\": \"LLaMA-3.1-8B RSFT candidate generation (N=8, T=0.7). Cross-family RSFT pipeline validation. plan_016 claim=1/2.\", \"plan_id\": \"plan_016\", \"parent\": \"plan_016_llama_3_1_8b_sft\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.training.rsft_generate --model_path /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B --sft_adapter /root/autodl-tmp/sft_output_llama_3_1_8b --data_path /root/autodl-tmp/data/docred --n_candidates 8 --temperature 0.7 --no-quantize --output_dir /root/autodl-tmp/rsft_candidates_llama_3_1_8b --seed 42\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"351871\", \"checkpoint_source\": \"/root/autodl-tmp/sft_output_llama_3_1_8b\", \"eval_data\": \"docred-train (generation, not eval)\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-16T14:25:09.831Z\", \"hypothesis\": \"LLaMA-3.1-8B RSFT candidate generation (N=8, T=0.7) for cross-family CED-RSFT validation\", \"pid\": 353179, \"log_path\": \"~/runs/faith-evidence-ie/plan_016_llama_rsft_candidates.log\"}, \"plan_007_redocred_4b_sft_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T12:30:55.473Z\", \"updated_at\": \"2026-05-16T12:34:54.050Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=0 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output_qwen3_4b --data_path /root/autodl-tmp/data/re-docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/plan_007_redocred_4b_sft_eval\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"342069\", \"log_path\": \"~/runs/faith-evidence-ie/plan_007_redocred_4b_sft_eval.log\", \"submitted_at\": \"2026-05-16T12:31:28.959Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 28.3, \"gpu_hours\": 0.01}, \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:0\", \"pid\": \"342069\", \"log_path\": \"~/runs/faith-evidence-ie/plan_007_redocred_4b_sft_eval.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=0 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output_qwen3_4b --data_path /root/autodl-tmp/data/re-docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/plan_007_redocred_4b_sft_eval\\\"\", \"finished_at\": \"2026-05-16T12:31:52.934Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-16T12:31:57.243Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T12:32:01.036672+00:00\"}]}, \"notes\": \"诊断: 两个路径均不存在——(1) 基座模型 /root/autodl-tmp/models/Qwen/Qwen3-4B/ 未下载（服务器只有 Qwen3-1.7B 和 Qwen3-8B）；(2) SFT adapter /root/autodl-tmp/sft_output_qwen3_4b/ 不存在（4B 模型未训练过）。inference.py 加载 tokenizer 时因本地路径不存在回退到 HF Hub 查找，触发 HFValidationError。\\n修复: (1) 先下载 Qwen3-4B 模型到 /root/autodl-tmp/models/Qwen/Qwen3-4B/；(2) 用该模型完成 SFT 训练生成 adapter；(3) 再重新提交 eval。\"}, \"plan_006_qwen3_1_7b_no_evidence_eval_v2r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T12:02:28.162Z\", \"updated_at\": \"2026-05-16T12:28:44.616Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=0 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen/Qwen3-1.7B --sft_adapter /root/autodl-tmp/sft_output_qwen3_1_7b_no_evidence --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --no_evidence --output_dir /root/autodl-tmp/eval_results/qwen3_1_7b_no_evidence_eval_v2\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"339089\", \"log_path\": \"~/runs/faith-evidence-ie/plan_006_qwen3_1_7b_no_evidence_eval_v2r2.log\", \"submitted_at\": \"2026-05-16T12:03:19.347Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 891.3, \"gpu_hours\": 0.25, \"notes\": \"Killed by Director - duplicate of v3 on cuda:1. GPU 释放给其他任务.\", \"checkpoint_path\": \"N/A\"}, \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:0\", \"pid\": \"339089\", \"log_path\": \"~/runs/faith-evidence-ie/plan_006_qwen3_1_7b_no_evidence_eval_v2r2.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=0 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen/Qwen3-1.7B --sft_adapter /root/autodl-tmp/sft_output_qwen3_1_7b_no_evidence --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --no_evidence --output_dir /root/autodl-tmp/eval_results/qwen3_1_7b_no_evidence_eval_v2\\\"\", \"finished_at\": \"2026-05-16T12:18:08.217Z\"}, \"conclusion\": \"failed\", \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-16T12:18:10.679Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T12:18:13.450876+00:00\"}]}}, \"plan_006_qwen3_1_7b_no_evidence_eval_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T11:40:29.706Z\", \"updated_at\": \"2026-05-16T11:44:58.762Z\", \"spec\": {\"command\": \"cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=0 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen/Qwen3-1.7B --sft_adapter /root/autodl-tmp/sft_output_qwen3_1_7b_no_evidence --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --no_evidence --output_dir /root/autodl-tmp/eval_results/qwen3_1_7b_no_evidence_eval_v2\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"unknown\", \"log_path\": \"~/runs/faith-evidence-ie/plan_006_qwen3_1_7b_no_evidence_eval_v2.log\", \"submitted_at\": \"2026-05-16T11:41:21.922Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 14.3, \"gpu_hours\": 0.0}, \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:0\", \"pid\": \"unknown\", \"log_path\": \"~/runs/faith-evidence-ie/plan_006_qwen3_1_7b_no_evidence_eval_v2.log\", \"reproduce\": {\"command\": \"cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=0 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen/Qwen3-1.7B --sft_adapter /root/autodl-tmp/sft_output_qwen3_1_7b_no_evidence --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --no_evidence --output_dir /root/autodl-tmp/eval_results/qwen3_1_7b_no_evidence_eval_v2\", \"finished_at\": \"2026-05-16T11:41:33.375Z\"}, \"failure_reason\": \"EXIT_CODE=127 (command not found — check bash -c wrapping / env activate)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-16T11:41:36.224Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T11:41:40.025368+00:00\"}]}, \"notes\": \"失败原因: tmux 用 sh 执行命令, python 不在 PATH (需 bash -c 包装 conda activate). wall_clock=14s, 未产出任何数据. 已自动重提交为 v3.\"}, \"plan_006_qwen3_1_7b_no_evidence_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T09:25:53.604Z\", \"updated_at\": \"2026-05-16T11:17:18.299Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen/Qwen3-1.7B --sft_adapter /root/autodl-tmp/sft_output_qwen3_1_7b_no_evidence --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/qwen3_1_7b_no_evidence_eval --no-quantize\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:2\"], \"pid\": 324679, \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 12275, \"model_name\": \"Qwen3-1.7B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/sft_output_qwen3_1_7b_no_evidence\", \"eval_data\": \"docred-dev\", \"log_path\": \"/root/autodl-tmp/eval_results/qwen3_1_7b_no_evidence_eval.log\", \"hypothesis\": \"Model size ablation: Qwen3-1.7B no-evidence SFT eval. plan_006 claim=1.\", \"plan_id\": \"plan_006\", \"parent\": \"plan_006_qwen3_1_7b_no_evidence_sft\", \"checkpoint_path\": \"/root/autodl-tmp/sft_output_qwen3_1_7b_no_evidence\", \"notes\": \"INVALID: missing --no_evidence flag in eval, prompt mismatch with training template. Ign-F1=0.3786 is invalid data.\"}, \"conclusion\": \"failed\", \"metrics\": {\"f1\": 0.3884, \"ign_f1\": 0.3786, \"evi_f1\": 0.0007, \"edcr\": 0.9848, \"precision\": 0.4282, \"recall\": 0.3553, \"pred_count\": 27049, \"n_truncated\": 531, \"format_ok_rate\": 0.999}, \"completed_at\": \"2026-05-16T11:11:04.903Z\"}, \"plan_006_qwen3_8b_no_evidence_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T11:12:04.565Z\", \"updated_at\": \"2026-05-16T11:16:54.766Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen/Qwen3-8B --sft_adapter /root/autodl-tmp/sft_output_qwen3_8b_no_evidence --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/qwen3_8b_no_evidence_eval --no-quantize\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:2\"], \"pid\": 334598, \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 12275, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/sft_output_qwen3_8b_no_evidence\", \"eval_data\": \"docred-dev\", \"log_path\": \"/root/autodl-tmp/eval_results/qwen3_8b_no_evidence_eval.log\", \"hypothesis\": \"8B no-evidence SFT eval. 与 plan_006_qwen3_8b_sft_eval (Ign-F1=0.5051) 对比量化 8B evidence tax. plan_006 claim=1.\", \"plan_id\": \"plan_006\", \"parent\": \"plan_006_qwen3_8b_no_evidence_sft\", \"notes\": \"INVALID: same --no_evidence flag bug as 1.7B eval, killed before completion. Prompt mismatch with training template.\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T11:16:54.766Z\"}, \"reeval_flat_nli_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T02:38:03.120Z\", \"updated_at\": \"2026-05-16T10:14:04.270Z\", \"hypothesis\": \"Re-eval flat-NLI RSFT s42 with unified protocol: batch_size=4 + --no-quantize + --sft_adapter + max_new_tokens=1024. 原 eval_plan_001_flat_nli 用了 batch_size=16。Paired t-test 关键路径。\", \"parent\": \"plan_001_rsft_flat_nli\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_flat_nli/checkpoint-507 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/rsft_flat_nli_s42_reeval --no-quantize\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"296732\", \"log_path\": \"/root/autodl-tmp/eval_results/rsft_flat_nli_s42_reeval/metrics.json\", \"submitted_at\": \"2026-05-16T04:16:19.584Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + SFT + flat-NLI RSFT s42\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/rsft_output_flat_nli/checkpoint-507\", \"eval_data\": \"docred dev (985 docs)\", \"checkpoint_path\": \"/root/autodl-tmp/eval_results/rsft_flat_nli_s42_reeval\", \"wall_clock_seconds\": 21464.7, \"gpu_hours\": 5.96}, \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:0\", \"pid\": 296732, \"account\": \"root\", \"log_path\": \"~/runs/faith-evidence-ie/reeval_flat_nli_s42.log\", \"reproduce\": {\"finished_at\": \"2026-05-16T07:59:30.990Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T07:59:34.675689+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"ign_f1\": 0.4448, \"rel_f1\": 0.4535, \"evi_f1\": 0.8039, \"evi_f1_joint\": 0.3558, \"edcr\": 0.6458, \"format_compliance_rate\": 1, \"field_compliance_rate\": 0.7787, \"n_truncated\": 205, \"inference_time_seconds\": 13253.1}, \"completed_at\": \"2026-05-16T10:14:04.270Z\"}, \"reeval_ced_s44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T02:38:00.052Z\", \"updated_at\": \"2026-05-16T10:14:02.479Z\", \"hypothesis\": \"Re-eval CED RSFT s44 with unified protocol: batch_size=4 + --no-quantize + --sft_adapter + max_new_tokens=1024 + seed=44. 原 eval 用了 batch_size≈16 且 seed=42（错误）。Paired t-test 关键路径。\", \"parent\": \"mvp2_rsft_train_r1_s44\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_s44/checkpoint-510 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 44 --output_dir /root/autodl-tmp/eval_results/rsft_ced_s44_reeval --no-quantize\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"297190\", \"log_path\": \"/root/autodl-tmp/eval_results/rsft_ced_s44_reeval/metrics.json\", \"submitted_at\": \"2026-05-16T04:18:28.117Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/eval_results/rsft_ced_s44_reeval\", \"wall_clock_seconds\": 21334.4, \"gpu_hours\": 5.93}, \"notes\": \"正确 checkpoint: /root/autodl-tmp/rsft_output_s44/checkpoint-510。旧 eval 路径一致但可能用了根目录 adapter 而非 checkpoint-510 子目录。\", \"gpu\": \"cuda:0\", \"server\": \"rtx5090-4x\", \"pid\": \"297190\", \"log_path\": \"~/runs/faith-evidence-ie/reeval_ced_s44.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_s44/checkpoint-510 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 44 --output_dir /root/autodl-tmp/eval_results/rsft_ced_s44_reeval --no-quantize\\\"\", \"finished_at\": \"2026-05-16T07:56:51.068Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T07:56:54.613393+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"ign_f1\": 0.4511, \"rel_f1\": 0.4621, \"evi_f1\": 0.805, \"evi_f1_joint\": 0.3677, \"edcr\": 0.635, \"format_compliance_rate\": 1, \"field_compliance_rate\": 0.802, \"n_truncated\": 190, \"inference_time_seconds\": 13077.6}, \"completed_at\": \"2026-05-16T10:14:02.479Z\"}, \"reeval_ced_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T02:37:58.498Z\", \"updated_at\": \"2026-05-16T10:14:00.520Z\", \"hypothesis\": \"Re-eval CED RSFT s42 with unified protocol: batch_size=4 + --no-quantize + --sft_adapter + max_new_tokens=1024. 原 mvp2_eval_rsft_r2b_maxtok1536_r2 用了 batch_size=8 + max_new_tokens=1536。Paired t-test 关键路径。\", \"parent\": \"mvp2_rsft_train_r1\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=2 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output/checkpoint-510 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/rsft_ced_s42_reeval --no-quantize\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:2\"], \"pid\": \"298018\", \"log_path\": \"/root/autodl-tmp/eval_results/rsft_ced_s42_reeval/metrics.json\", \"submitted_at\": \"2026-05-16T04:24:05.849Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/eval_results/rsft_ced_s42_reeval\", \"wall_clock_seconds\": 20994.7, \"gpu_hours\": 5.83}, \"notes\": \"旧 eval (rsft_r2b_maxtok1536_r2) 不仅协议不一致，而且用了错误 checkpoint (rsft_output_r2b: lora_alpha=32, 仅 160 步)。正确 checkpoint: /root/autodl-tmp/rsft_output/checkpoint-510 (seed=42, lora_alpha=128, 510 步，与 s43/s44/s45 配置一致)。\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:2\", \"pid\": \"298018\", \"log_path\": \"~/runs/faith-evidence-ie/reeval_ced_s42.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=2 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output/checkpoint-510 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/rsft_ced_s42_reeval --no-quantize\\\"\", \"finished_at\": \"2026-05-16T07:25:16.570Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T07:25:21.431476+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"ign_f1\": 0.4423, \"rel_f1\": 0.4517, \"evi_f1\": 0.8175, \"evi_f1_joint\": 0.3518, \"edcr\": 0.6569, \"format_compliance_rate\": 1, \"field_compliance_rate\": 0.7756, \"n_truncated\": 214, \"inference_time_seconds\": 10815.5}, \"completed_at\": \"2026-05-16T10:14:00.520Z\"}, \"reeval_flat_nli_s44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T08:56:36.565Z\", \"updated_at\": \"2026-05-16T09:26:04.920Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_flat_nli_s44/checkpoint-507 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 44 --output_dir /root/autodl-tmp/eval_results/rsft_flat_nli_s44_reeval --no-quantize\", \"server\": \"rtx5090-4x\", \"gpu_id\": 0, \"pid\": 322215, \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": null, \"model_name\": \"Qwen3-4B + sft_adapter + rsft_flat_nli_s44/checkpoint-507\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/rsft_output_flat_nli_s44/checkpoint-507\", \"eval_data\": \"docred dev\", \"log_path\": \"/root/autodl-tmp/logs/reeval_flat_nli_s44.log\", \"parent\": \"plan_001_flat_nli_seed44\", \"hypothesis\": \"Re-eval flat-NLI RSFT s44 with D076 unified protocol. 之前 eval_flat_nli_seed44 被 killed。Paired t-test 最后一块拼图。\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T09:26:04.920Z\"}, \"plan_006_qwen3_1_7b_sft\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T06:13:52.388Z\", \"updated_at\": \"2026-05-16T06:33:46.578Z\", \"spec\": {\"hypothesis\": \"Model size ablation: Qwen3-1.7B SFT baseline，验证 evidence tax 和 RSFT 增益在小模型上是否成立。应对 RC4 (scale sensitivity)。plan_id=plan_006, claim=1。\", \"model_name\": \"Qwen3-1.7B\", \"server\": \"rtx5090-4x\", \"plan_id\": \"plan_006\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=3 HF_HOME=/root/autodl-tmp/.hf_cache PYTHONUNBUFFERED=1 python -m freige.training.sft_trainer --model_name /root/autodl-tmp/models/Qwen/Qwen3-1.7B --data_dir /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/sft_output_qwen3_1_7b --seed 42 --wandb_run_name qwen3_1_7b_sft\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 3027, \"seed\": 42, \"pid\": \"308118\", \"gpu\": [\"cuda:3\"], \"log_path\": \"~/runs/faith-evidence-ie/plan_006_qwen3_1_7b_sft.log\", \"backend\": \"tmux\", \"account\": \"root\", \"lora_rank\": 64, \"lora_alpha\": 128, \"target_modules\": 7, \"quantize\": \"4-bit QLoRA\", \"trainable_params\": \"69.7M / 1.79B (3.89%)\", \"num_epochs\": 3, \"batch_size\": 1, \"gradient_accumulation_steps\": 16, \"learning_rate\": 0.0002, \"output_dir\": \"/root/autodl-tmp/sft_output_qwen3_1_7b\", \"kill_reason\": \"QLoRA 4-bit confound: 4B SFT/RSFT 用 bf16 LoRA，1.7B 必须一致\", \"checkpoint_path\": \"N/A\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T06:33:46.578Z\"}, \"reeval_flat_nli_s43_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T02:32:45.507Z\", \"updated_at\": \"2026-05-16T06:10:14.112Z\", \"hypothesis\": \"Re-eval flat-NLI RSFT s43 with unified protocol: batch_size=4 + --no-quantize + --sft_adapter + --max_new_tokens 1024. 原 reeval_flat_nli_s43 用了 batch_size=16 导致协议不一致。C3 paired t-test 关键路径。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=3 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_flat_nli_s43/checkpoint-507 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 43 --output_dir /root/autodl-tmp/eval_results/rsft_flat_nli_s43_reeval_r2 --no-quantize\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"291003\", \"log_path\": \"~/runs/faith-evidence-ie/reeval_flat_nli_s43_r2.log\", \"submitted_at\": \"2026-05-16T03:05:10.815Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 11103.3, \"gpu_hours\": 3.08}, \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:3\", \"pid\": \"291003\", \"log_path\": \"~/runs/faith-evidence-ie/reeval_flat_nli_s43_r2.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=3 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_flat_nli_s43/checkpoint-507 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 43 --output_dir /root/autodl-tmp/eval_results/rsft_flat_nli_s43_reeval_r2 --no-quantize\\\"\", \"finished_at\": \"2026-05-16T06:07:10.034Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T06:07:13.554397+00:00\"}]}, \"metrics\": {\"rel_f1\": 0.4586, \"rel_precision\": 0.4732, \"rel_recall\": 0.4449, \"ign_f1\": 0.4503, \"evi_f1\": 0.8113, \"evi_precision\": 0.8035, \"evi_recall\": 0.8192, \"evi_f1_joint\": 0.358, \"edcr\": 0.6552, \"format_ok_rate\": 0.999, \"n_truncated\": 184, \"n_predictions\": 15015}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/rsft_output_flat_nli_s43/checkpoint-507\", \"completed_at\": \"2026-05-16T06:10:14.112Z\"}, \"eval_rsft_ced_s45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:30:34.036Z\", \"updated_at\": \"2026-05-16T05:43:12.975Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_ced_s45/checkpoint-510 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 45 --output_dir /root/autodl-tmp/eval_results/rsft_ced_s45 --no-quantize\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:2\"], \"pid\": \"283838\", \"log_path\": \"/root/runs/faith-evidence-ie/eval_rsft_ced_s45.log\", \"submitted_at\": \"2026-05-16T01:30:48.081Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 10350.6, \"gpu_hours\": 2.88, \"checkpoint_path\": \"/root/autodl-tmp/rsft_output_ced_s45/checkpoint-510\"}, \"hypothesis\": \"Full dev eval of CED RSFT seed=45 with --sft_adapter + --no-quantize. Paired t-test 关键路径：CED 第 3 个 seed（s42/s44 已有，s43 训练中）。对比 flat-NLI RSFT seeds。plan_id=plan_mvp2_rsft, claim=3。\", \"parent\": \"rsft_ced_s45_train_r4\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"rtx5090-4x\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-16T01:30:45.945Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_ced_s45/checkpoint-510 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 45 --output_dir /root/autodl-tmp/eval_results/rsft_ced_s45 --no-quantize\\\"\", \"finished_at\": \"2026-05-16T04:21:18.743Z\", \"training_hours\": 2.84}, \"pid\": \"283838\", \"log_path\": \"~/runs/faith-evidence-ie/eval_rsft_ced_s45.log\", \"notes\": \"[2026-05-16 02:18 UTC] 69/247 batches (28%), ~2h remaining. ETA ~04:18 UTC. Running normally at ~41s/it avg.\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T04:21:24.317065+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"rel_f1\": 0.4514, \"ign_f1\": 0.4416, \"evi_f1\": 0.8174, \"rel_p\": 0.4718, \"rel_r\": 0.4326, \"edcr\": 0.655, \"evi_f1_joint\": 0.3558, \"n_truncated\": 206, \"format_ok_rate\": 1}, \"checkpoint_path\": \"/root/autodl-tmp/rsft_output_ced_s45/checkpoint-510\", \"completed_at\": \"2026-05-16T04:23:18.660Z\"}, \"eval_rsft_ced_s43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:30:37.978Z\", \"updated_at\": \"2026-05-16T05:18:59.781Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 43 --output_dir /root/autodl-tmp/eval_results/rsft_ced_s43 --no-quantize\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"286587\", \"log_path\": \"~/runs/faith-evidence-ie/eval_rsft_ced_s43.log\", \"submitted_at\": \"2026-05-16T02:13:11.138Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/rsft_output_ced_s43/checkpoint-510\", \"wall_clock_seconds\": 11076.6, \"gpu_hours\": 3.08}, \"hypothesis\": \"Full dev eval of CED RSFT seed=43 with --sft_adapter + --no-quantize. Paired t-test 关键路径：CED 第 4 个 seed。对比 flat-NLI RSFT seeds。plan_id=plan_mvp2_rsft, claim=3。\", \"parent\": \"rsft_ced_s43_train_r3\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"rtx5090-4x\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-16T02:12:19.128Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 43 --output_dir /root/autodl-tmp/eval_results/rsft_ced_s43 --no-quantize\\\"\", \"finished_at\": \"2026-05-16T05:13:49.642Z\", \"training_hours\": 3.03}, \"pid\": \"286587\", \"log_path\": \"~/runs/faith-evidence-ie/eval_rsft_ced_s43.log\", \"notes\": \"[2026-05-16 02:18 UTC] 5/247 batches (2%), ~3h remaining. ETA ~05:19 UTC. Just started, running normally at ~45s/it avg.\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T05:13:52.707434+00:00\"}]}, \"metrics\": {\"rel_f1\": 0.4601, \"ign_f1\": 0.4512, \"precision\": 0.4696, \"recall\": 0.4509, \"evi_f1\": 0.8063, \"evi_precision\": 0.8025, \"evi_recall\": 0.8101, \"edcr\": 0.6542, \"evi_f1_joint\": 0.3605, \"format_ok_rate\": 1, \"n_truncated\": 184, \"n_predictions\": 15051, \"inference_time_seconds\": 10768.2}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T05:17:47.763Z\"}, \"eval_plan_014_no_evidence_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:34:45.302Z\", \"updated_at\": \"2026-05-16T04:20:13.358Z\", \"hypothesis\": \"Retry of eval_plan_014_no_evidence with corrected command: --model_path 传底座 Qwen3-4B, --sft_adapter 传 SFT no-evidence adapter。修复 adapter 检测逻辑冲突。plan_id=plan_014, claim=1。\", \"parent\": \"plan_014_sft_no_evidence\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_no_evidence_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/sft_no_evidence_noquant --no-quantize --no_evidence\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"288109\", \"log_path\": \"~/runs/faith-evidence-ie/eval_plan_014_no_evidence_r2.log\", \"submitted_at\": \"2026-05-16T02:27:53.107Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/sft_no_evidence_output\", \"wall_clock_seconds\": 6547.0, \"gpu_hours\": 1.82}, \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"pid\": \"288109\", \"log_path\": \"~/runs/faith-evidence-ie/eval_plan_014_no_evidence_r2.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_no_evidence_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/sft_no_evidence_noquant --no-quantize --no_evidence\\\"\", \"finished_at\": \"2026-05-16T04:13:27.499Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T04:13:31.947315+00:00\"}]}, \"metrics\": {\"rel_f1\": 0.4876, \"ign_f1\": 0.4721, \"evi_f1\": 0, \"edcr\": 0, \"evi_f1_joint\": 0, \"precision\": 0.4901, \"recall\": 0.4851, \"ign_precision\": 0.4654, \"ign_recall\": 0.4791, \"format_compliance\": 0.993, \"truncation_rate\": 0.312, \"n_predictions\": 21181, \"n_documents\": 985}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T04:17:00.079Z\"}, \"mvp2_ced_reranker_poc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:55:03.414Z\", \"updated_at\": \"2026-05-16T03:49:41.385Z\", \"hypothesis\": \"CED-as-reranker: no fine-tuning, use CED to select best of N=8 SFT candidates at inference time. If rel_f1 > 0.4057 (SFT greedy), CED adds value without training risk. Oracle reranker as upper bound.\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:0\", \"spec\": {\"command\": \"python /root/autodl-tmp/freige/eval/ced_reranker.py (N=8, CED scoring, 985 docs)\", \"server\": \"rtx5090-4x\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + SFT (greedy N=8 + CED reranker)\", \"seed\": 42, \"pid\": \"178050\", \"checkpoint_path\": \"N/A\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_ced_reranker_poc.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T14:47:24.899Z\", \"metrics\": {\"ced_reranker_rel_f1\": 0.486367, \"ced_reranker_ign_f1\": 0.473634, \"ced_reranker_evi_f1\": 0.8188, \"oracle_rel_f1\": 0.623746, \"oracle_ign_f1\": 0.612518, \"random_rel_f1\": 0.453783, \"random_ign_f1\": 0.439677}, \"notes\": \"CED reranker (N=8, no training) rel_f1=0.4864, 超过 SFT greedy (+8.07pp) 和 RSFT 3-seed mean (+2.68pp)。Oracle 上界 rel_f1=0.6237 (+21.8pp vs SFT)，CED reranker 实现了 oracle ceiling 的 37% (0.0807/0.218)。CED-F1 Spearman r=0.3235 (p≈0)，相关性显著但中等——说明 CED 不是完美的 proxy 但有信号。Random baseline rel_f1=0.4538 说明 sampling diversity 本身就有 +4.8pp 收益，CED 在此基础上再加 +3.3pp。EDCR 下降 (0.6156 vs SFT 0.7118)，N=8 sampling 引入更多 distractor citations。推理耗时 5.8h (N=8 生成主导)。结论：CED 作为 inference-time reranker 有明确论文价值——零训练成本超越 RSFT，且 oracle ceiling 表明更好的 reward model 还有大幅空间。\"}, \"eval_flat_nli_seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T23:12:39.186Z\", \"updated_at\": \"2026-05-16T03:49:36.608Z\", \"hypothesis\": \"Full dev eval of flat-NLI RSFT seed=45 checkpoint WITH --sft_adapter。seed45 中间 eval rel_f1=0.4876（待全量确认）。对比 CED RSFT mean (0.4596)。三 seed 全量 eval 出齐后汇报 flat-NLI vs CED RSFT 完整 seed-level 对比。\", \"parent\": \"plan_001_flat_nli_seed45\", \"spec\": {\"command\": \"python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_flat_nli_s45/checkpoint-507 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 45 --output_dir /root/autodl-tmp/eval_results/rsft_flat_nli_s45 --no-quantize\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:3\", \"pid\": 272164, \"log_path\": \"~/runs/faith-evidence-ie/eval_flat_nli_seed45.log\", \"submitted_at\": \"2026-05-15T23:44:54.114Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 12275, \"model_name\": \"Qwen3-4B\", \"seed\": 45, \"checkpoint_source\": \"/root/autodl-tmp/rsft_output_flat_nli_s45/checkpoint-507\", \"eval_data\": \"docred-dev\", \"wall_clock_seconds\": 12094.9, \"gpu_hours\": 3.36}, \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"notes\": \"[2026-05-16 02:18 UTC] 196/247 batches (79%), ~45min remaining. ETA ~03:03 UTC. Running normally at ~47s/it avg.\", \"reproduce\": {\"finished_at\": \"2026-05-16T03:03:01.591Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T03:03:05.615685+00:00\"}]}, \"metrics\": {\"rel_f1\": 0.455052, \"ign_f1\": 0.446181, \"evi_f1\": 0.815399, \"edcr\": 0.652133, \"evi_f1_joint\": 0.355612}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/rsft_output_flat_nli_s45/checkpoint-507\", \"log_path\": \"~/runs/faith-evidence-ie/eval_flat_nli_seed45.log\", \"completed_at\": \"2026-05-16T03:06:29.033Z\"}, \"eval_flat_nli_s44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T23:14:05.010Z\", \"updated_at\": \"2026-05-16T03:49:35.610Z\", \"hypothesis\": \"Full dev eval of flat-NLI RSFT seed=44 with --sft_adapter + --no-quantize. C3 统计显著性数据点 (s42=0.4539, s43 pending, s44 本次, s45 pending)。\", \"parent\": \"plan_001_flat_nli_seed44\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_flat_nli_s44/checkpoint-507 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 44 --output_dir /root/autodl-tmp/eval_results/rsft_flat_nli_s44 --no-quantize\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"270462\", \"log_path\": \"~/runs/faith-evidence-ie/eval_flat_nli_s44.log\", \"submitted_at\": \"2026-05-15T23:27:39.718Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/rsft_output_flat_nli_s44/checkpoint-507\", \"wall_clock_seconds\": 11069.8, \"gpu_hours\": 3.07}, \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"pid\": \"270462\", \"log_path\": \"~/runs/faith-evidence-ie/eval_flat_nli_s44.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_flat_nli_s44/checkpoint-507 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 44 --output_dir /root/autodl-tmp/eval_results/rsft_flat_nli_s44 --no-quantize\\\"\", \"finished_at\": \"2026-05-16T02:24:33.081Z\"}, \"notes\": \"[2026-05-16 02:18 UTC] 238/247 batches (96%), ~7min remaining. ETA ~02:25 UTC. Running normally at ~45s/it avg.\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T02:24:37.198824+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"rel_f1\": 0.461506, \"ign_f1\": 0.452126, \"evi_f1\": 0.813123, \"edcr\": 0.645808, \"evi_f1_joint\": 0.359673}, \"completed_at\": \"2026-05-16T02:32:09.485Z\"}, \"rsft_ced_s45_train_r4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T00:33:12.797Z\", \"updated_at\": \"2026-05-16T02:15:34.043Z\", \"hypothesis\": \"CED RSFT seed=45 训练（r4 重试，r3 因 cuda:2 orphan PID 276148 OOM 失败）。补全 paired t-test 所需的第 3 个 CED seed（现有 s42/s44，s43 在 cuda:1 训练中）。训练数据 2718 samples，3 epochs，~2h。plan_id=plan_mvp2_rsft, claim=3。\", \"parent\": \"\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/rsft_output_ced_s45/checkpoint-510\", \"log_path\": \"/tmp/rsft_ced_s45_r4.log\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/rsft_output_ced_s45/checkpoint-510\", \"log_path\": \"/tmp/rsft_ced_s45_r4.log\", \"metrics\": {\"training_completed\": true, \"checkpoint\": \"checkpoint-510\", \"note\": \"Training metrics not captured (r4 retry after OOM). Eval running as eval_rsft_ced_s45.\"}, \"completed_at\": \"2026-05-16T02:15:34.043Z\"}, \"rsft_ced_s43_train_r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T00:20:57.272Z\", \"updated_at\": \"2026-05-16T02:14:46.064Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/rsft_output_ced_s43/checkpoint-510\", \"log_path\": \"~/runs/faith-evidence-ie/rsft_ced_s43_train_r3.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T02:10:56.984Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T02:11:00.631057+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.6151, \"eval_loss\": 0.7618, \"task_eval_f1\": 0.5026, \"task_eval_ign_f1\": 0.4932, \"task_eval_evi_f1\": 0.7624, \"task_eval_edcr\": 0.6516, \"total_steps\": 510, \"epochs\": 3, \"training_hours\": 1.82}, \"completed_at\": \"2026-05-16T02:14:46.064Z\"}, \"eval_plan_014_no_evidence\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T23:17:32.011Z\", \"updated_at\": \"2026-05-16T01:34:06.402Z\", \"hypothesis\": \"Dev set eval of SFT-no-evidence model (plan_014). 核心目标：对比标准 SFT rel_f1=0.4057 vs 不输出 evidence 的 SFT rel_f1（隔离 evidence generation 代价）。只评估 rel_f1，不评估 evi_f1（输出无 evidence）。plan_id=plan_014, claim=1。\", \"parent\": \"plan_014_sft_no_evidence\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/sft_no_evidence_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/sft_no_evidence_noquant --no-quantize --no_evidence\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:2\"], \"pid\": \"283455\", \"log_path\": \"~/runs/faith-evidence-ie/eval_plan_014_no_evidence.log\", \"submitted_at\": \"2026-05-16T01:27:16.251Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 33.8, \"gpu_hours\": 0.01}, \"conclusion\": \"failed\", \"notes\": \"FAILED: ValueError — model_path 含 adapter_config.json 触发 adapter 检测逻辑，要求 --sft_adapter。诊断(Worker diagnose_eval_plan_014): SFT adapter 本身就是 model_path，不应走 adapter stacking 路径。修复：--model_path 改传底座 Qwen3-4B，--sft_adapter 传 /root/autodl-tmp/sft_no_evidence_output。待 GPU 空闲后以 corrected command 重试。\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"rtx5090-4x\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-16T01:27:14.109Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/sft_no_evidence_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/sft_no_evidence_noquant --no-quantize --no_evidence\\\"\", \"finished_at\": \"2026-05-16T01:27:46.702Z\", \"training_hours\": 0.01}, \"pid\": \"283455\", \"log_path\": \"~/runs/faith-evidence-ie/eval_plan_014_no_evidence.log\", \"failure_reason\": \"Traceback → is a LoRA adapter (adapter_config.json found), but --sft_adapter is not set. RSFT/DPO/GRPO adapters are trained on SFT-merged model and MUST be evaluated with --sft_adapter pointing to the SFT adapter directory. Add: --sft_adapter /path/to/sft_output\", \"completed_at\": \"2026-05-16T01:27:50.023Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T01:27:53.542593+00:00\"}]}}, \"rsft_ced_s45_train_r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T00:21:01.099Z\", \"updated_at\": \"2026-05-16T00:31:23.730Z\", \"spec\": {\"command\": \"python -m freige.training.rsft_trainer --seed 45 --data_path rsft_filtered --output_dir rsft_output_ced_s45 --batch_size 4 --gradient_accumulation_steps 4 --weighted_sampling\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:2\"], \"pid\": \"277407\", \"log_path\": \"~/runs/faith-evidence-ie/rsft_ced_s45_train_r3.log\", \"submitted_at\": \"2026-05-16T00:21:15.972Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"rsft_filtered\", \"data_count\": 2718, \"model_name\": \"sft_base + ced_rsft\", \"seed\": 45, \"wall_clock_seconds\": 368.8, \"gpu_hours\": 0.1, \"notes\": \"CUDA OOM — GPU 2 被 orphan 进程 PID 276148 占用 31.6GB。Worker 正在清理，将创建 r4 重提交。\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-16T00:27:24.802Z\", \"notes\": \"CUDA OOM at launch: cuda:2 occupied by orphan PID 276148 (31.6GB). Need to kill orphan and resubmit as r4.\"}, \"rsft_ced_s45_train_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T00:09:11.100Z\", \"updated_at\": \"2026-05-16T00:25:40.284Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output_ced_s45 --learning_rate 2e-5 --num_epochs 3 --per_device_batch_size 4 --gradient_accumulation_steps 4 --lora_rank 64 --lora_alpha 128 --weighted_sampling --eval_data_dir /root/autodl-tmp/data/docred --eval_max_docs 50 --wandb_run_name rsft-ced-s45-r2 --seed 45\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:2\"], \"pid\": \"276143\", \"log_path\": \"~/runs/faith-evidence-ie/rsft_ced_s45_train_r2.log\", \"submitted_at\": \"2026-05-16T00:16:52.439Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 225.7, \"gpu_hours\": 0.06}, \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"pid\": \"276143\", \"log_path\": \"~/runs/faith-evidence-ie/rsft_ced_s45_train_r2.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output_ced_s45 --learning_rate 2e-5 --num_epochs 3 --per_device_batch_size 4 --gradient_accumulation_steps 4 --lora_rank 64 --lora_alpha 128 --weighted_sampling --eval_data_dir /root/autodl-tmp/data/docred --eval_max_docs 50 --wandb_run_name rsft-ced-s45-r2 --seed 45\\\"\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T00:20:38.182Z\", \"notes\": \"Director 下令终止——错误套用 flat-NLI 超参(batch=1/grad_accum=16)，需用 CED 正确模板(batch=4/grad_accum=4)重跑，已由 r3 替代。\"}, \"rsft_ced_s43_train_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T00:09:34.266Z\", \"updated_at\": \"2026-05-16T00:25:38.818Z\", \"spec\": {\"data_path\": \"/root/autodl-tmp/rsft_filtered/rsft_train.jsonl\", \"data_count\": 2718, \"model_name\": \"Qwen3-4B + LoRA on SFT adapter\", \"seed\": 43, \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"account\": \"root\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output_ced_s43 --lr 2e-5 --epochs 3 --batch 1 --grad_accum 16 --lora_rank 64 --lora_alpha 128 --seed 43 --weighted_sampling\\\"\", \"pid\": 275269, \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"N/A (training, not eval)\", \"log_path\": \"~/runs/faith-evidence-ie/rsft_ced_s43_train_r2.log\", \"output_dir\": \"/root/autodl-tmp/rsft_output_ced_s43\", \"hyperparams\": {\"lr\": \"2e-5\", \"epochs\": 3, \"batch\": 1, \"grad_accum\": 16, \"lora_rank\": 64, \"lora_alpha\": 128, \"bf16\": true, \"weighted_sampling\": true}}, \"hypothesis\": \"CED RSFT seed=43 训练（r2 重试，修正 cwd 错误）。补全 paired t-test 所需的第 3 个 CED seed（现有 s42/s44）。训练数据 2718 samples，3 epochs，~2h。plan_id=plan_mvp2_rsft, claim=3。\", \"parent\": \"rsft_ced_s43_train\", \"reproduce\": {\"finished_at\": \"2026-05-16T00:20:20.177Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-16T00:20:24.299Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T00:20:28.707019+00:00\"}]}, \"notes\": \"Director 下令终止——错误套用 flat-NLI 超参(batch=1/grad_accum=16)，需用 CED 正确模板(batch=4/grad_accum=4)重跑，已由 r3 替代。实际 argparse 无 --batch/--grad_accum 参数，静默忽略后用了默认值(batch=4/grad_accum=4)，实际配置恰好正确，但命令不规范。\"}, \"reeval_rsft_topk3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:00:34.722Z\", \"updated_at\": \"2026-05-16T00:24:22.091Z\", \"hypothesis\": \"Re-eval RSFT top_k=3 WITH --sft_adapter (D064 bug fix). 原 eval_plan_008_rsft_topk3 因缺 --sft_adapter 被 killed。对比 CED RSFT top_k=1 (rel_f1≈0.46) 和 SFT baseline (0.4057)。\", \"parent\": \"plan_008_rsft_topk3\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_topk3_output/checkpoint-1509 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/rsft_topk3_reeval --no-quantize\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:2\"], \"pid\": \"268485\", \"log_path\": \"~/runs/faith-evidence-ie/reeval_rsft_topk3.log\", \"submitted_at\": \"2026-05-15T23:10:49.243Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"RSFT top_k=3 + SFT adapter\", \"seed\": 42, \"checkpoint_source\": \"rsft_topk3_output/checkpoint-1509\", \"eval_data\": \"docred dev\", \"wall_clock_seconds\": 3798.3, \"gpu_hours\": 1.06}, \"reproduce\": {\"finished_at\": \"2026-05-16T00:10:43.871Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T00:10:53.138391+00:00\"}]}, \"metrics\": {\"rel_f1\": 0.4454, \"rel_precision\": 0.4512, \"rel_recall\": 0.4398, \"ign_f1\": 0.4364, \"evi_f1\": 0.8088, \"edcr\": 0.6635, \"format_ok_rate\": 0.999, \"n_truncated\": 214, \"n_predictions\": 16020, \"inference_time_seconds\": 3546.4, \"ign_f1_corrected\": true}, \"conclusion\": \"negative\", \"notes\": \"RSFT top_k=3 rel_f1=0.4454，优于 SFT baseline (0.4057) 但劣于 CED RSFT top_k=1 (~0.46)。top_k=3 引入更多噪声训练样本，反而降低关系抽取精度。evi_f1=0.8088 较好。214/985 truncated。\", \"checkpoint_path\": \"/root/autodl-tmp/rsft_topk3_output/checkpoint-1509\", \"completed_at\": \"2026-05-16T00:14:07.521Z\"}, \"rsft_ced_s43_train\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T00:05:46.635Z\", \"updated_at\": \"2026-05-16T00:10:42.131Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.training.rsft_trainer --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output_ced_s43 --seed 43 --weighted_sampling --eval_data_dir /root/autodl-tmp/data/docred --wandb_run_name rsft_ced_s43 --bf16\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"unknown\", \"log_path\": \"~/runs/faith-evidence-ie/rsft_ced_s43_train.log\", \"submitted_at\": \"2026-05-16T00:06:16.826Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 34.8, \"gpu_hours\": 0.01}, \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"pid\": \"unknown\", \"log_path\": \"~/runs/faith-evidence-ie/rsft_ced_s43_train.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.training.rsft_trainer --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output_ced_s43 --seed 43 --weighted_sampling --eval_data_dir /root/autodl-tmp/data/docred --wandb_run_name rsft_ced_s43 --bf16\\\"\", \"finished_at\": \"2026-05-16T00:06:49.264Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-16T00:06:51.674Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T00:06:55.376318+00:00\"}]}, \"notes\": \"失败原因: No module named freige.training.rsft_trainer — 命令 cd /root/autodl-tmp/freige 导致 cwd 错误。已修正为 cd /root/autodl-tmp，重提交为 rsft_ced_s43_train_r2 (PID=275264)\"}, \"rsft_ced_s45_train\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T00:03:17.851Z\", \"updated_at\": \"2026-05-16T00:05:24.862Z\", \"spec\": {\"hypothesis\": \"CED RSFT seed=45 训练，补全 paired t-test 所需的第 3 个 CED seed（现有 s42/s43/s44）。训练数据 2718 samples，3 epochs，~2h。plan_id=plan_mvp2_rsft, claim=3。\", \"plan_id\": \"plan_mvp2_rsft\", \"model_name\": \"Qwen3-4B + LoRA on SFT adapter\", \"data_path\": \"/root/autodl-tmp/rsft_filtered/rsft_train.jsonl\", \"data_count\": 2718, \"seed\": 45, \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"account\": \"root\", \"checkpoint_path\": \"N/A\", \"log_path\": \"N/A\", \"kill_reason\": \"Director 重排优先级: CED s43 先于 s45, cuda:1 改分配给 rsft_ced_s43_train\"}, \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:1\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T00:05:24.862Z\"}, \"reeval_flat_nli_s43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:00:33.691Z\", \"updated_at\": \"2026-05-15T23:59:33.440Z\", \"hypothesis\": \"Re-eval flat-NLI RSFT seed=43 WITH --sft_adapter (D064 bug fix). 原 eval_plan_001_flat_nli_s43 因缺 --sft_adapter 导致 rel_f1=0.0022 无效。对比 flat-NLI s42 (rel_f1=0.4539) 和 CED RSFT mean (0.4596)。\", \"parent\": \"plan_001_flat_nli_seed43\", \"spec\": {\"command\": \"Re-eval flat-NLI RSFT seed=43 with --sft_adapter (D064 fix)\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:1\", \"pid\": 266178, \"log_path\": \"/root/runs/faith-evidence-ie/reeval_flat_nli_s43.log\", \"submitted_at\": \"2026-05-15T22:57:10.223Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 0, \"model_name\": \"Qwen3-4B + SFT + flat-NLI RSFT s43\", \"seed\": 43, \"checkpoint_source\": \"plan_001_flat_nli_s43\", \"eval_data\": \"docred_dev\", \"checkpoint_path\": \"/root/autodl-tmp/rsft_output_flat_nli_s43/checkpoint-507\", \"eval_output_dir\": \"/root/autodl-tmp/eval_results/rsft_flat_nli_s43_reeval\", \"sft_adapter\": \"/root/autodl-tmp/sft_output\", \"base_model\": \"/root/autodl-tmp/models/Qwen3-4B\", \"wall_clock_seconds\": 3743.2, \"gpu_hours\": 1.04}, \"reproduce\": {\"finished_at\": \"2026-05-15T23:56:41.649Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T23:56:45.572465+00:00\"}]}, \"metrics\": {\"rel_f1\": 0.4523, \"ign_f1\": 0.4523, \"evi_f1\": 0.8158, \"edcr\": 0.6505, \"num_preds\": 15357, \"format_ok\": \"984/985\", \"truncated\": \"211/985\", \"inference_time_s\": 3515.8}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T23:59:33.440Z\"}, \"plan_003_edcr_diagnostic\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T23:12:40.174Z\", \"updated_at\": \"2026-05-15T23:52:05.506Z\", \"hypothesis\": \"EDCR cross-method diagnostic table: 计算所有 evidence-producing 方法（SFT baseline, RSFT-CED best, RSFT-flatNLI best, CED-reranker）的 EDCR，验证 EDCR 作为独立评估指标的诊断能力。plan_id=plan_003, claim=4。GPU 预算 2h。\", \"server\": \"rtx5090-4x\", \"gpu\": null, \"account\": \"root\", \"spec\": {\"gpu\": null, \"server\": \"rtx5090-4x\", \"notes\": \"CPU-only task, GPU allocation removed to free cuda:3\"}, \"conclusion\": \"success\", \"metrics\": {\"methods_evaluated\": 15, \"edcr_vs_rel_f1_spearman\": -0.9648, \"edcr_vs_rel_f1_pvalue\": 0.0001, \"edcr_vs_evi_f1_spearman\": 0.0022, \"edcr_vs_evi_f1_pvalue\": 0.9941, \"edcr_range\": \"0.63-0.99\", \"unique_diagnostic_value\": \"identifies pathological models (GRPO QLoRA) with high evi_f1 but catastrophically low rel_f1\"}, \"checkpoint_path\": \"/root/autodl-tmp/eval_results/edcr_diagnostic.json\", \"log_path\": \"/root/autodl-tmp/eval_results/edcr_diagnostic.tex\", \"completed_at\": \"2026-05-15T23:45:26.064Z\"}, \"eval_flat_nli_seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T23:12:38.199Z\", \"updated_at\": \"2026-05-15T23:48:28.074Z\", \"hypothesis\": \"Full dev eval of flat-NLI RSFT seed=44 with --sft_adapter + --no-quantize. C3 seed-level comparison.\", \"parent\": \"plan_001_flat_nli_seed44\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_flat_nli_s44/checkpoint-507 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 44 --output_dir /root/autodl-tmp/eval_results/rsft_flat_nli_s44 --no-quantize\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"270056\", \"log_path\": \"~/runs/faith-evidence-ie/eval_flat_nli_seed44.log\", \"submitted_at\": \"2026-05-15T23:27:04.263Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1283.8, \"gpu_hours\": 0.36}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T23:48:28.074Z\"}, \"eval_plan_012_dpo_1ep_fixed_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T21:58:52.440Z\", \"updated_at\": \"2026-05-15T23:44:56.586Z\", \"spec\": {\"command\": \"DPO 1ep re-eval with --sft_adapter (D064 fix)\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:3\", \"pid\": 262075, \"log_path\": \"~/runs/faith-evidence-ie/eval_plan_012_dpo_1ep_fixed_r2.log\", \"submitted_at\": \"2026-05-15T21:58:52.150Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 0, \"model_name\": \"Qwen3-4B + SFT + DPO 1ep\", \"seed\": 42, \"checkpoint_source\": \"plan_012_dpo_ced_3ep\", \"eval_data\": \"docred_dev\", \"checkpoint_path\": \"/root/autodl-tmp/dpo_ced_output/checkpoint-167\", \"wall_clock_seconds\": 6197.9, \"gpu_hours\": 1.72}, \"reproduce\": {\"finished_at\": \"2026-05-15T23:36:34.758Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T23:36:37.754401+00:00\"}]}, \"conclusion\": \"negative\", \"metrics\": {\"rel_f1\": 0.4034, \"evi_f1\": 0.8088, \"edcr\": 0.7139, \"format_ok_rate\": 0.999, \"truncated_rate\": 0.343, \"predictions\": 19107, \"ign_f1\": 0.4034, \"precision\": 0.3809, \"recall\": 0.4287, \"vs_sft_delta\": -0.0023, \"note\": \"DPO 1ep matches SFT baseline. 1ep→3ep trajectory shows gradual decoupling (rel_f1↓ evi_f1↑), consistent with GRPO pattern. Ign-F1=F1 exact match needs investigation.\"}, \"completed_at\": \"2026-05-15T23:42:10.085Z\"}, \"plan_001_flat_nli_seed44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T21:38:26.174Z\", \"updated_at\": \"2026-05-15T23:25:30.719Z\", \"spec\": {\"command\": \"rsft train flat_nli seed=44\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:0\", \"pid\": 258503, \"log_path\": \"~/runs/faith-evidence-ie/plan_001_flat_nli_seed44.log\", \"submitted_at\": \"2026-05-15T21:38:25.857Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/rsft_filtered_flat_nli/rsft_train.jsonl\", \"data_count\": 2691, \"model_name\": \"Qwen3-4B + SFT adapter\", \"seed\": 44, \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"checkpoint_path\": \"/root/autodl-tmp/rsft_output_flat_nli_s44\", \"wall_clock_seconds\": 6424.9, \"gpu_hours\": 1.78}, \"reproduce\": {\"finished_at\": \"2026-05-15T23:22:24.600Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T23:22:27.640280+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.6247, \"eval_loss\": 0.7564, \"eval_mean_token_accuracy\": 0.8299, \"task_eval_f1_ep1\": 0.4306, \"task_eval_f1_ep2\": 0.4884, \"task_eval_f1_ep3\": 0.4897, \"task_eval_evi_f1_ep3\": 0.78, \"task_eval_edcr_ep3\": 0.6596, \"task_eval_ign_f1_ep3\": 0.4897, \"train_runtime_sec\": 6197, \"num_epochs\": 3, \"total_steps\": 507}, \"completed_at\": \"2026-05-15T23:25:30.719Z\"}, \"plan_009_dynamics_figure\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T23:17:30.987Z\", \"updated_at\": \"2026-05-15T23:19:12.282Z\", \"hypothesis\": \"GRPO forgetting dynamics 3-panel figure: QLoRA vs BF16 GRPO 的 rel_f1/evi_f1/EDCR 训练轨迹对比。支撑 Claim 3 (task decoupling 是 QLoRA-specific)。plan_id=plan_009。\", \"conclusion\": \"success\", \"spec\": {\"command\": \"GRPO forgetting dynamics figure generation (CPU-only, matplotlib)\", \"server\": \"rtx5090-4x\", \"data_path\": \"W&B metrics + registry checkpoint data\", \"data_count\": 42, \"model_name\": \"N/A (visualization task)\", \"seed\": 0, \"checkpoint_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/plan_009_grpo_forgetting/grpo_forgetting_dynamics_v5.pdf\", \"log_path\": \"N/A\"}, \"completed_at\": \"2026-05-15T23:19:12.282Z\"}, \"plan_001_flat_nli_seed45\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T21:09:05.195Z\", \"updated_at\": \"2026-05-15T23:17:29.971Z\", \"spec\": {\"command\": \"flat-NLI RSFT training seed=45\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:2\", \"pid\": 257187, \"log_path\": \"~/runs/faith-evidence-ie/plan_001_flat_nli_seed45.log\", \"submitted_at\": \"2026-05-15T21:26:10.157Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/rsft_filtered_flat_nli/rsft_train.jsonl\", \"data_count\": 0, \"model_name\": \"Qwen3-4B + SFT adapter\", \"seed\": 45, \"wall_clock_seconds\": 6240.8, \"gpu_hours\": 1.73}, \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"rtx5090-4x\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-15T21:26:08.091Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_data_path /root/autodl-tmp/rsft_filtered_flat_nli/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output_flat_nli_s45 --learning_rate 2e-5 --num_epochs 3 --per_device_batch_size 1 --gradient_accumulation_steps 16 --lora_rank 64 --lora_alpha 128 --eval_data_dir /root/autodl-tmp/data/docred --wandb_run_name plan_001_flat_nli_seed45 --seed 45\\\"\", \"finished_at\": \"2026-05-15T23:07:49.718Z\", \"training_hours\": 1.69}, \"pid\": \"257187\", \"log_path\": \"~/runs/faith-evidence-ie/plan_001_flat_nli_seed45.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T23:07:54.004372+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"task_eval_rel_f1\": 0.4876, \"task_eval_evi_f1\": 0.7927, \"task_eval_edcr\": 0.6517, \"train_loss\": 0.6245, \"runtime_hours\": 1.69, \"note\": \"task-eval on 50 docs only, full dev eval needed\"}, \"checkpoint_path\": \"/root/autodl-tmp/rsft_output_flat_nli_s45/checkpoint-507\", \"completed_at\": \"2026-05-15T23:10:11.004Z\"}, \"plan_011_bf16_g8_step_eval\": {\"status\": \"DONE\", \"retry_count\": 2, \"created_at\": \"2026-05-15T19:04:51.538Z\", \"updated_at\": \"2026-05-15T23:01:09.970Z\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:1\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && bash /root/autodl-tmp/freige/scripts/eval_plan_011_steps.sh\\\"\", \"finished_at\": \"2026-05-15T22:54:30.133Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"completed_at\": \"2026-05-15T19:47:17.272Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T19:47:19.581918+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T19:53:37.646506+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T22:54:32.686556+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"诊断确认：SIGTERM (EXIT_CODE=143)。device_map=\\\"auto\\\" 无 CUDA_VISIBLE_DEVICES 限制，模型加载到 GPU 0（plan_001 占用 16.3GB），双进程共 31.4/32.6GB 后被 kill。两次重试均失败（retry_count=2）。修复：CUDA_VISIBLE_DEVICES=1 重提交到空闲 cuda:1。\"}}, \"notes\": \"诊断确认：SIGTERM (EXIT_CODE=143)。device_map=\\\"auto\\\" 无 CUDA_VISIBLE_DEVICES 限制，模型加载到 GPU 0（plan_001 占用 16.3GB），双进程共 31.4/32.6GB 后被 kill。两次重试均失败（retry_count=2）。修复：CUDA_VISIBLE_DEVICES=1 重提交到空闲 cuda:1。\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/eval_results/grpo_ced_g8_bf16_step30/ + step50/ + step70/\", \"log_path\": \"~/runs/faith-evidence-ie/plan_011_bf16_g8_step_eval.log\"}, \"conclusion\": \"success\", \"metrics\": {\"step_30\": {\"rel_f1\": 0.434, \"evi_f1\": 0.8063, \"edcr\": 0.6807}, \"step_50\": {\"rel_f1\": 0.4276, \"evi_f1\": 0.8024, \"edcr\": 0.6855}, \"step_70\": {\"rel_f1\": 0.4341, \"evi_f1\": 0.8099, \"edcr\": 0.6685}, \"best_step\": \"step_70\", \"trend\": \"non-monotonic, all < ckpt-100 (0.4549)\"}, \"checkpoint_path\": \"N/A (eval-only, source checkpoints at /root/autodl-tmp/grpo_bf16_g8_output/checkpoint-{30,50,70})\"}, \"plan_011_eval_g8_bf16_ckpt100\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:43:24.143Z\", \"updated_at\": \"2026-05-15T22:06:28.981Z\", \"spec\": {\"command\": \"STALE - killed\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"215276\", \"log_path\": \"~/runs/faith-evidence-ie/plan_011_eval_g8_bf16_ckpt100.log\", \"submitted_at\": \"2026-05-15T14:43:23.832Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"grpo_g8_bf16 ckpt100\", \"seed\": 42, \"checkpoint_source\": \"grpo_ced_g8_bf16\", \"eval_data\": \"docred dev\", \"wall_clock_seconds\": 26585.1, \"gpu_hours\": 7.38}, \"conclusion\": \"killed\", \"notes\": \"STALE: 该 eval 已由 eval_grpo_g8_bf16 完成并 success (rel_f1=0.4549)。此条目为残留，不需要执行。\", \"completed_at\": \"2026-05-15T22:06:28.981Z\"}, \"mvp2_eval_rsft_s44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:35:23.934Z\", \"updated_at\": \"2026-05-15T22:06:28.059Z\", \"hypothesis\": \"Full dev eval of RSFT seed=44 checkpoint. First MVP-2 judgement data point. Pass: rel_f1 > 0.4057 AND evi_f1 > 0.798 (SFT baseline).\", \"parent\": \"mvp2_rsft_train_r1_s44\", \"conclusion\": \"killed\", \"notes\": \"STALE: s44 全量 eval 已由 mvp2_eval_rsft_r2b_maxtok1536 等系列完成。s44 rel_f1=0.4655 已入库。此条目为残留。\", \"spec\": {\"command\": \"STALE - killed\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"261617\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_eval_rsft_s44.log\", \"submitted_at\": \"2026-05-15T21:57:22.401Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"RSFT s44\", \"seed\": 44, \"checkpoint_source\": \"rsft_output_s44\", \"eval_data\": \"docred dev\", \"wall_clock_seconds\": 545.7, \"gpu_hours\": 0.15}, \"completed_at\": \"2026-05-15T22:06:28.059Z\"}, \"eval_plan_008_topk3_fixed\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T21:52:00.000Z\", \"retry_count\": 0, \"created_at\": \"2026-05-15T21:39:34.632Z\", \"updated_at\": \"2026-05-15T21:39:34.632Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_topk3_output --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/rsft_topk3_fixed --no-quantize\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"259032\", \"log_path\": \"~/runs/faith-evidence-ie/eval_plan_008_topk3_fixed.log\", \"submitted_at\": \"2026-05-15T21:39:34.183Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval_plan_012_dpo_1ep_fixed\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T21:52:00.000Z\", \"retry_count\": 0, \"created_at\": \"2026-05-15T21:39:31.570Z\", \"updated_at\": \"2026-05-15T21:39:31.570Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/dpo_output_1ep/ --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/dpo_ced_1ep_fixed --no-quantize\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"258955\", \"log_path\": \"~/runs/faith-evidence-ie/eval_plan_012_dpo_1ep_fixed.log\", \"submitted_at\": \"2026-05-15T21:39:31.197Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval_plan_008_rsft_topk3\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T21:38:00.000Z\", \"retry_count\": 0, \"created_at\": \"2026-05-15T21:09:51.464Z\", \"updated_at\": \"2026-05-15T21:38:00.000Z\", \"metrics\": {\"note\": \"INVALID — missing --sft_adapter, killed by Director instruction\"}, \"hypothesis\": \"RSFT top_k=3 dev eval: 对比 top_k=1 RSFT (rel_f1≈0.46) 和 SFT baseline (rel_f1≈0.4057)。验证更多候选是否提升证据质量。\", \"parent\": \"plan_008_rsft_topk3\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_topk3_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/rsft_topk3 --no-quantize\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"255523\", \"log_path\": \"~/runs/faith-evidence-ie/eval_plan_008_rsft_topk3.log\", \"submitted_at\": \"2026-05-15T21:10:11Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"hypothesis\": \"RSFT top_k=3 dev eval: 对比 top_k=5 RSFT (rel_f1≈0.46) 和 SFT baseline (rel_f1=0.4106)。top_k=3 训练 50-doc subset 显示 F1=0.50 但 Evi-F1 下降到 0.68。\", \"parent\": \"plan_008_rsft_topk3\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + SFT + RSFT top_k=3\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/rsft_topk3_output\", \"eval_data\": \"docred-dev (985 docs)\"}}, \"plan_012_dpo_ced\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:54:03.324Z\", \"updated_at\": \"2026-05-15T21:37:44.232Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/dpo_output\", \"data_path\": \"/root/autodl-tmp/dpo_data/dpo_pairs.jsonl\", \"data_count\": 2666, \"model_name\": \"Qwen3-4B + SFT + CED-DPO\", \"seed\": 42, \"beta\": 0.1, \"num_epochs\": 3, \"loss_type\": \"sigmoid\", \"base_model\": \"/root/autodl-tmp/models/Qwen3-4B\", \"sft_adapter\": \"/root/autodl-tmp/sft_output\", \"pairs\": 2666}, \"hypothesis\": \"DPO+CED preference learning: 用 CED 构造 preference pairs (CED top-1 = chosen, CED bottom-1 = rejected)，DPO 训练。验证 offline preference optimization 能否替代 online GRPO 避免 catastrophic forgetting，同时利用 CED 信号。对比 RSFT (rel_f1=0.46) 和 SFT baseline (rel_f1=0.4057)。\", \"reproduce\": {\"finished_at\": \"2026-05-15T17:38:15.433Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:38:17.857458+00:00\"}]}, \"conclusion\": \"negative\", \"notes\": \"⚠️ Reviewer WARNING: 严重过拟合。3 epochs, rewards accuracy=1.0, margins 9x 膨胀, entropy 崩塌。checkpoint-501 是最过拟合版本，结果有 confound。需补 eval checkpoint-400 对比 + 重训 epochs=1。\", \"metrics\": {\"rel_f1\": 0.3429, \"evi_f1\": 0.8403, \"edcr\": 0.7294, \"format_ok_rate\": 0.995, \"checkpoint\": \"checkpoint-501\", \"rewards_accuracy\": 1, \"margins\": 9.01}, \"log_path\": \"~/runs/faith-evidence-ie/plan_012_dpo_ced.log\", \"completed_at\": \"2026-05-15T21:37:44.232Z\"}, \"plan_012_dpo_ced_1ep\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:50:44.852Z\", \"updated_at\": \"2026-05-15T21:36:34.720Z\", \"spec\": {\"hypothesis\": \"DPO+CED 1-epoch 重训：修复 3-epoch 过拟合问题。epochs=1 (~167 steps, <10min)，其余超参不变（β=0.1, lr=5e-7, loss=sigmoid, seed=42, pairs=2666）。让 DPO 数据点可用于论文。\", \"parent\": \"plan_012_dpo_ced\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 WANDB_PROJECT=freige-dpo PYTHONUNBUFFERED=1 python -m freige.training.dpo_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --dpo_data_path /root/autodl-tmp/dpo_data/dpo_pairs.jsonl --output_dir /root/autodl-tmp/dpo_output_1ep --beta 0.1 --num_epochs 1 --seed 42 --loss_type sigmoid --per_device_batch_size 1 --gradient_accumulation_steps 16 --wandb_run_name plan_012_dpo_ced_1ep\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:2\"], \"pid\": \"245103\", \"log_path\": \"~/runs/faith-evidence-ie/plan_012_dpo_ced_1ep.log\", \"submitted_at\": \"2026-05-15T19:43:02.707Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/dpo_data/dpo_pairs.jsonl\", \"data_count\": 2666, \"model_name\": \"Qwen3-4B + SFT + CED-DPO (1ep)\", \"seed\": 42, \"base_model\": \"/root/autodl-tmp/models/Qwen3-4B\", \"sft_adapter\": \"/root/autodl-tmp/sft_output\", \"beta\": 0.1, \"num_epochs\": 1, \"loss_type\": \"sigmoid\", \"checkpoint_path\": \"/root/autodl-tmp/dpo_output_1ep\", \"wall_clock_seconds\": 6812.0, \"gpu_hours\": 1.89}, \"gpu_ids\": [3], \"hypothesis\": \"DPO+CED 1 epoch retraining: plan_012_dpo_ced 3 epochs 严重过拟合 (rewards_accuracy=1.0, margins 9x膨胀, entropy崩塌)。重训 1 epoch 验证 early stopping 是否消除 overfitting confound。对比 plan_012 3ep + RSFT (rel_f1=0.46) + SFT baseline (rel_f1=0.4057)。\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"notes\": \"DPO+CED 完全失败。1ep eval: rel_f1=0.0022 (34 TPs / 19265 preds)，比 3ep (0.3429) 更差。训练指标正常 (accuracy=0.82, margins=0.86)，但模型输出几乎无法匹配正确 relation。evi_f1=0.75 说明模型仍生成 evidence，但 relation extraction 崩溃。358/985 truncated (36%)。DPO 对 evidence-grounded DocRE 完全不适用——不是过拟合问题，是方法本身失效。D061 已关闭 DPO 实验线。\", \"reproduce\": {\"finished_at\": \"2026-05-15T20:17:44.285Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T20:17:46.894275+00:00\"}]}, \"metrics\": {\"rel_f1\": 0.0022, \"evi_f1\": 0.75, \"edcr\": 0.9982, \"format_ok\": \"981/985\", \"truncated\": \"358/985\", \"tp\": 34, \"n_preds\": 19265, \"inference_time_s\": 3643, \"train_loss_final\": 0.59, \"rewards_accuracy\": 0.82, \"rewards_margins\": 0.86, \"total_steps\": 167, \"training_time_min\": 33}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-15T21:36:34.720Z\"}, \"eval_plan_001_flat_nli_s43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:29:54.486Z\", \"updated_at\": \"2026-05-15T21:35:00.000Z\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T21:34:00.000Z\", \"metrics\": {\"rel_f1\": 0.0022, \"ign_f1\": 0.0022, \"evi_f1\": 0.8533, \"edcr\": 0.9982, \"num_preds\": 17285, \"format_ok\": \"981/985\", \"truncated\": \"251/985\", \"tp\": 32, \"note\": \"INVALID — missing --sft_adapter, same bug as DPO 1ep eval\"}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_flat_nli_s43 --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 43 --output_dir /root/autodl-tmp/eval_results/rsft_flat_nli_s43 --no-quantize\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"252179\", \"log_path\": \"~/runs/faith-evidence-ie/eval_plan_001_flat_nli_s43.log\", \"submitted_at\": \"2026-05-15T20:30:26.563Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + flat-NLI RSFT s43 adapter\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/rsft_output_flat_nli_s43\", \"eval_data\": \"docred dev (985 docs)\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T21:33:03.903Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T21:33:07.578617+00:00\"}]}}, \"eval_plan_012_dpo_ced_1ep\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:22:11.752Z\", \"updated_at\": \"2026-05-15T21:27:30.000Z\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-15T21:25:00.000Z\", \"metrics\": {\"rel_f1\": 0.0022, \"ign_f1\": 0.0022, \"evi_f1\": 0.75, \"edcr\": 0.9982, \"num_preds\": 19265, \"format_ok\": \"981/985\", \"truncated\": \"358/985\", \"tp\": 34, \"inference_time_s\": 3643}, \"spec\": {\"command\": \"python -m freige.eval.inference --model_path /root/autodl-tmp/dpo_output_1ep/ --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/dpo_ced_1ep --no-quantize\", \"server\": \"rtx5090-4x\", \"data_path\": \"docred-dev\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + DPO-CED-1ep LoRA\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/dpo_output_1ep/ (final, 167 steps = 1 epoch)\", \"eval_data\": \"docred-dev\", \"gpu_id\": 2, \"parent\": \"plan_012_dpo_ced_1ep\", \"hypothesis\": \"DPO+CED 1ep checkpoint dev set evaluation: 验证 1ep 是否消除 3ep 过拟合 (rewards_acc=1.0, margins=9x), 对比 SFT baseline rel_f1=0.4057\"}}, \"plan_008_rsft_topk3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:01:33.773Z\", \"updated_at\": \"2026-05-15T21:11:35.509Z\", \"spec\": {\"command\": \"python -m freige.train.rsft_train --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/rsft_filtered_topk3/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_topk3_output\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"234489\", \"log_path\": \"/root/runs/faith-evidence-ie/plan_008_rsft_topk3.log\", \"submitted_at\": \"2026-05-15T18:03:03.593Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/rsft_filtered_topk3/rsft_train.jsonl\", \"data_count\": 8037, \"model_name\": \"Qwen3-4B + SFT adapter + RSFT top_k=3\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/rsft_topk3_output\", \"wall_clock_seconds\": 11199.8, \"gpu_hours\": 3.11}, \"reproduce\": {\"finished_at\": \"2026-05-15T21:06:30.938Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T21:06:37.059207+00:00\"}]}, \"hypothesis\": \"RSFT top_k=3 训练：用 CED-filtered 的 top-3 候选进行 rejection sampling fine-tuning，验证更多候选是否比 top_k=1 (rel_f1≈0.46) 带来更好的证据质量。\", \"metrics\": {\"train_loss\": 0.5543, \"eval_loss\": 0.8297, \"eval_mean_token_accuracy\": 0.8228, \"eval_entropy\": 0.6001, \"train_runtime_sec\": 10916, \"total_steps\": 1509, \"epochs\": 3, \"trainable_params_pct\": 3.18, \"rsft_samples\": 8037, \"ced_score_mean\": 0.621, \"task_eval_f1_ep1\": 0.4848, \"task_eval_f1_ep2\": 0.4824, \"task_eval_f1_ep3\": 0.5012, \"task_eval_evi_f1_ep1\": 0.745, \"task_eval_evi_f1_ep2\": 0.6997, \"task_eval_evi_f1_ep3\": 0.6816, \"task_eval_edcr_ep1\": 0.6525, \"task_eval_edcr_ep2\": 0.6529, \"task_eval_edcr_ep3\": 0.5963, \"task_eval_note\": \"50-doc subset, not full dev\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T21:09:43.432Z\", \"notes\": \"RSFT top_k=3 训练正常完成。3 epochs, 1509 steps, 3h02m。8037 RSFT 样本 (CED mean=0.621)。Task eval (50-doc subset): F1 从 ep1=0.4848 升至 ep3=0.5012，但 Evi-F1 从 0.745 降至 0.6816，EDCR 从 0.6525 降至 0.5963，呈现 relation extraction 提升但证据质量下降的 trade-off。与 CED RSFT top_k=5 baseline (rel_f1=0.4596) 相比，subset F1=0.5012 看起来更高，但需 full dev eval 确认。无 W&B run。下一步：提交 eval_plan_008_rsft_topk3 做 full dev eval。\"}, \"plan_001_flat_nli_seed43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:22:55.521Z\", \"updated_at\": \"2026-05-15T20:35:05.452Z\", \"spec\": {\"hypothesis\": \"flat-NLI RSFT seed=43 补跑。验证 seed=42 的 rel_f1=0.4539 是否在噪声范围内（CED RSFT 3-seed mean=0.4596, σ=0.0127）。\", \"parent\": \"plan_001_rsft_flat_nli\", \"command\": \"python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_data_path /root/autodl-tmp/rsft_filtered_flat_nli/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output_flat_nli_s43 --learning_rate 2e-5 --num_epochs 3 --per_device_batch_size 1 --gradient_accumulation_steps 16 --lora_rank 64 --lora_alpha 128 --eval_data_dir /root/autodl-tmp/data/docred --wandb_run_name plan_001_flat_nli_seed43 --seed 43\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"data_path\": \"/root/autodl-tmp/rsft_filtered_flat_nli/rsft_train.jsonl\", \"data_count\": 2691, \"model_name\": \"Qwen3-4B + SFT adapter\", \"seed\": 43, \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"N/A (training)\", \"checkpoint_path\": \"/root/autodl-tmp/rsft_output_flat_nli_s43\", \"log_path\": \"~/runs/faith-evidence-ie/plan_001_flat_nli_seed43.log\", \"pid\": \"236774\", \"submitted_at\": \"2026-05-15T18:22:00Z\", \"submitted_via\": \"worker_direct\", \"backend\": \"nohup\", \"wall_clock_seconds\": 7600.2, \"gpu_hours\": 2.11}, \"reproduce\": {\"finished_at\": \"2026-05-15T20:20:10.574Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T20:20:13.016730+00:00\"}]}, \"metrics\": {\"train_loss_final\": 0.6257, \"train_loss_min\": 0.5895, \"eval_loss_epoch3\": 0.7567, \"eval_accuracy_epoch3\": 0.8298, \"total_steps\": 507, \"epochs\": 3, \"train_runtime_seconds\": 6880, \"task_eval_f1_ep1\": 0.4825, \"task_eval_f1_ep2\": 0.4542, \"task_eval_f1_ep3\": 0.4866, \"task_eval_evi_f1_ep3\": 0.7834, \"task_eval_edcr_ep3\": 0.6402, \"task_eval_note\": \"50-doc subset, not full dev\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/rsft_output_flat_nli_s43\", \"log_path\": \"~/runs/faith-evidence-ie/plan_001_flat_nli_seed43.log\", \"completed_at\": \"2026-05-15T20:28:40.191Z\", \"notes\": \"训练正常完成 (EXIT_CODE=0)。507 steps, 3 epochs, eval_loss 三 epoch 持平 (0.753-0.757) 无过拟合。与 seed42 高度一致 (train_loss 0.6248 vs 0.6238, accuracy ~0.855 vs 0.853)。Checkpoint: /root/autodl-tmp/rsft_output_flat_nli_s43/checkpoint-507。下一步: dev eval 提取 rel_f1/evi_f1。\"}, \"plan_009_flatnli_reward_eval_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:54:58.033Z\", \"updated_at\": \"2026-05-15T20:32:33.464Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -m freige.eval.batch_eval --exp_dir /root/autodl-tmp/grpo_flatnli_r3 --sft_adapter /root/autodl-tmp/sft_output --output_dir /root/autodl-tmp/eval_results/grpo_flatnli_r3 --no-quantize --max_new_tokens 1024\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"246974\", \"log_path\": \"~/runs/faith-evidence-ie/plan_009_flatnli_reward_eval.log\", \"submitted_at\": \"2026-05-16T03:54:00Z\", \"submitted_via\": \"ssh_execute+tmux\", \"backend\": \"tmux\", \"tmux_session\": \"plan_009_flatnli_reward_eval\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + SFT + QLoRA GRPO (flatNLI reward)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/grpo_flatnli_r3 (checkpoints 20,40,60,80,100)\", \"eval_data\": \"docred dev (985 docs, 12275 triples)\", \"checkpoint_path\": \"/root/autodl-tmp/eval_results/grpo_flatnli_r3\", \"parent\": \"plan_009_flatnli_reward_eval\", \"notes\": \"Retry. Batch eval 5 flatNLI-reward GRPO checkpoints (step 20-100) for forgetting dynamics figure.\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T20:32:29.383Z\", \"notes\": \"OOM 失败。--no-quantize + batch_size 16 + max_new_tokens 1024 在单卡 RTX 5090 (32GB) 上 OOM。全部 5 个 checkpoint (20-100) 均未完成 eval。checkpoint-20 仅完成 1/62 batches 即被 kill (-9)。修复方案：降 batch_size 至 4 或 2 后重提交。\"}, \"plan_009_extract_reward_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:04:55.707Z\", \"updated_at\": \"2026-05-15T19:58:37.870Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 bash /root/autodl-tmp/freige/scripts/eval_extract_reward_steps.sh\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"247778\", \"log_path\": \"~/runs/faith-evidence-ie/plan_009_extract_reward_eval.log\", \"submitted_at\": \"2026-05-15T19:55:11.304Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"rtx5090-4x\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-15T19:06:27.578Z\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T19:54:17.758Z\", \"notes\": \"OOM: Worker 提交到了 GPU 0（被 plan_001 占用 16 GiB），而非目标 cuda:1。需在 cuda:0 释放后重提交。\"}, \"eval_sft_baseline_noquant\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:38:33.128Z\", \"updated_at\": \"2026-05-15T19:45:42.147Z\", \"spec\": {\"command\": \"python eval.py --model_path /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/eval_results/sft_baseline_noquant --batch_size 16 --max_new_tokens 1024 --split dev --seed 42\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"237912\", \"log_path\": \"~/runs/faith-evidence-ie/eval_sft_baseline_noquant.log\", \"submitted_at\": \"2026-05-15T18:38:45.042Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + SFT LoRA (no quantization)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"docred/dev (985 docs, 12275 triples)\", \"wall_clock_seconds\": 3916.2, \"gpu_hours\": 1.09, \"checkpoint_path\": \"/root/autodl-tmp/eval_results/sft_baseline_noquant/\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T19:41:54.062Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T19:41:59.716746+00:00\"}]}, \"metrics\": {\"rel_f1\": 0.4106, \"rel_precision\": 0.4198, \"rel_recall\": 0.4019, \"evi_f1\": 0.8013, \"evi_precision\": 0.8005, \"evi_recall\": 0.8022, \"evi_f1_joint\": 0.3216, \"edcr\": 0.7039, \"format_ok_rate\": 0.998, \"field_compliance_rate\": 0.7066, \"n_predictions\": 16774, \"n_truncated\": 288, \"n_documents\": 985, \"inference_time_seconds\": 3677.9}, \"checkpoint_path\": \"/root/autodl-tmp/eval_results/sft_baseline_noquant/metrics.json\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T19:44:01.274Z\", \"notes\": \"[2026-05-16] 无量化 SFT baseline eval 完成。rel_f1=0.4106 vs 量化版 0.4057 (+0.49pp), evi_f1=0.8013 vs 0.7979 (+0.34pp)。差异 <1pp，确认量化 confound 不显著（D058 排除）。所有基于量化 baseline 的对比结论仍然成立。无量化版推理时间 3678s vs 量化版 6139s（快 40%，因无量化用满 GPU 内存）。\"}, \"plan_009_flatnli_reward_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:04:57.991Z\", \"updated_at\": \"2026-05-15T19:39:02.187Z\", \"spec\": {\"hypothesis\": \"FlatNLI reward GRPO checkpoint eval。用已有 checkpoint 补充 forgetting dynamics 图的 flatNLI reward 变体数据，实现三种 reward 对比。\", \"server\": \"rtx5090-4x\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + SFT + QLoRA GRPO (flatNLI reward)\", \"seed\": 42, \"eval_data\": \"docred dev (985 docs)\", \"checkpoint_source\": \"grpo_flatnli_r3/r4/r5/r6 checkpoints\"}, \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"rtx5090-4x\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-15T19:06:33.944Z\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T19:39:02.187Z\"}, \"eval_plan_012_dpo_ced_ckpt400\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:32:55.398Z\", \"updated_at\": \"2026-05-15T19:37:31.477Z\", \"spec\": {\"command\": \"python -m freige.eval.inference --model_path /root/autodl-tmp/dpo_output/checkpoint-400 --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/dpo_ced_ckpt400 --no-quantize\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:3\", \"pid\": 242796, \"log_path\": \"~/runs/faith-evidence-ie/eval_plan_012_dpo_ced_ckpt400.log\", \"submitted_at\": \"2026-05-15T19:32:55.107Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + DPO-CED LoRA (checkpoint-400)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/dpo_output/checkpoint-400\", \"eval_data\": \"docred-dev\", \"log_file\": \"~/runs/faith-evidence-ie/eval_plan_012_dpo_ced_ckpt400.log\", \"parent\": \"plan_012_dpo_ced\", \"wall_clock_seconds\": 248.7, \"gpu_hours\": 0.07}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T19:37:03.842Z\", \"notes\": \"OOM: cuda:3 被 plan_008 占用 19.6 GiB，仅完成 15% batch，结果不可信。需在 cuda:2 重跑。\"}, \"plan_009_forgetting_figure\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:56:56.840Z\", \"updated_at\": \"2026-05-15T18:57:17.531Z\", \"spec\": {\"hypothesis\": \"GRPO forgetting dynamics 可视化：整理 QLoRA vs bf16 GRPO 训练轨迹，绘制论文核心 figure。\", \"server\": \"rtx5090-4x\", \"command\": \"python /root/autodl-tmp/freige/scripts/plot_forgetting_dynamics.py\", \"data_path\": \"trainer_state.json + registry eval metrics\", \"data_count\": 0, \"model_name\": \"N/A (visualization)\", \"seed\": 0, \"checkpoint_path\": \"/root/autodl-tmp/freige/figures/\", \"log_path\": \"N/A\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T18:57:10.563Z\", \"notes\": \"3-panel figure: (a) Training Reward—bf16 1.5-3.0 vs QLoRA 0.1-1.2; (b) Rel-F1—QLoRA暴跌至0.01(lr5e-6)/0.22(lr5e-5), bf16稳定0.45+; (c) Evi-F1—QLoRA lr5e-6反升至0.85, bf16稳定0.81。Artifacts: art_20260515_eace0b (PNG), art_20260515_319233 (PDF)。\"}, \"eval_plan_014_sft_no_evidence\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:20:25.574Z\", \"updated_at\": \"2026-05-15T18:42:46.665Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/eval_results/sft_no_evidence\", \"log_path\": \"~/runs/faith-evidence-ie/eval_plan_014_sft_no_evidence.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T18:29:34.790Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T18:29:37.278008+00:00\"}]}, \"metrics\": {\"rel_f1\": 0.4893, \"rel_ign_f1\": 0.4893, \"rel_precision\": 0.4884, \"rel_recall\": 0.4902, \"evi_f1\": 0, \"evi_precision\": 0, \"evi_recall\": 0, \"edcr\": 0, \"format_ok_rate\": 0.9919, \"n_truncated\": 298, \"n_predictions\": 21064, \"n_documents\": 985, \"n_parseable\": 977, \"inference_time_seconds\": 4103.8}, \"conclusion\": \"success\", \"notes\": \"No-evidence SFT rel_f1=0.4893 vs baseline with-evidence rel_f1=0.4057 (+0.0836, +20.6%). Evidence generation significantly hurts relation extraction. evi_f1=0 as expected. Format compliance 99.2%. 298/985 truncated. Inference 4103.8s.\", \"completed_at\": \"2026-05-15T18:42:46.665Z\"}, \"plan_014_sft_no_evidence\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:55:43.710Z\", \"updated_at\": \"2026-05-15T18:42:28.216Z\", \"hypothesis\": \"SFT-without-evidence ablation: 训练只输出 relation triples（不含 evidence sentences）的 SFT 模型。量化 joint evidence generation 对 extraction 的代价（当前 rel_f1=0.4057 vs 只抽关系的 LMRC 60.7 的 gap 有多少来自 evidence 负担）。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.training.sft_trainer --data_dir /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/sft_no_evidence_output --no_evidence --wandb_run_name plan_014_sft_no_evidence --seed 42\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"222207\", \"log_path\": \"~/runs/faith-evidence-ie/plan_014_sft_no_evidence.log\", \"submitted_at\": \"2026-05-15T15:56:13Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen3-4B (QLoRA 4-bit)\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 3027, \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/sft_no_evidence_output\", \"wall_clock_seconds\": 9975.2, \"gpu_hours\": 2.77}, \"reproduce\": {\"finished_at\": \"2026-05-15T17:01:44.197Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:01:46.586830+00:00\"}]}, \"metrics\": {\"train_loss\": 0.7077, \"eval_loss\": 0.8781, \"eval_token_accuracy\": 0.8086, \"epochs\": 3, \"total_steps\": 570, \"train_runtime_min\": 64, \"samples\": 3027, \"trainable_params\": \"132M/4.15B (3.18%)\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T18:42:28.216Z\"}, \"plan_002_test_eval_s44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:05:47.701Z\", \"updated_at\": \"2026-05-15T18:20:17.405Z\", \"spec\": {\"hypothesis\": \"RSFT s44 checkpoint on DocRED test set should achieve similar or better performance than dev set results, validating generalization of the faithfulness-evidence approach.\", \"task_type\": \"eval\", \"eval_data\": \"docred_test\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 1000, \"model_name\": \"Qwen3-4B + SFT + RSFT-s44\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/rsft_output_s44\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:0\", \"command\": \"python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_s44 --sft_adapter /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split test --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/test_rsft_s44 --no-quantize\", \"log_path\": \"/root/autodl-tmp/eval_results/test_rsft_s44.log\", \"checkpoint_path\": \"/root/autodl-tmp/eval_results/test_rsft_s44\", \"tmux_session\": \"plan_002_test_eval_s44\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T18:20:14.596Z\", \"notes\": \"DocRED test split 无 gold labels，inference.py 不支持 enumerate_all_pairs 模式。推迟到论文终稿阶段（需改造 inference.py + CodaLab submission）。Director 指令标记 failed。\"}, \"plan_001_rsft_flat_nli\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:40:01.021Z\", \"updated_at\": \"2026-05-15T18:04:14.547Z\", \"hypothesis\": \"flat-NLI RSFT ablation: 用 flat-NLI scoring（p_pos 概率，无 contrastive margin）筛选的 2691 样本做 RSFT。对比 CED scoring RSFT（2718 样本）。验证 CED 的对比性 margin 是否是关键因素。如 flat-NLI RSFT ≈ CED RSFT → CED 无增益；如 CED RSFT 显著优于 → contrastive margin 关键。\", \"parent\": \"plan_001_flat_nli_scoring\", \"spec\": {\"gpu\": [\"cuda:0\"], \"command\": \"python rsft_train.py (flat-NLI scoring)\", \"server\": \"rtx5090-4x\", \"data_path\": \"/root/autodl-tmp/rsft_filtered_flat_nli/rsft_train.jsonl\", \"data_count\": 2691, \"model_name\": \"Qwen3-4B + SFT adapter\", \"seed\": null, \"pid\": \"219556\", \"log_path\": \"/root/runs/faith-evidence-ie/plan_001_rsft_flat_nli.log\", \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"N/A (training, not eval)\", \"checkpoint_path\": \"/root/autodl-tmp/rsft_output_flat_nli/\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T16:30:34.306Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T16:30:42.223143+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.6238, \"train_loss_min\": 0.5803, \"mean_token_accuracy\": 0.8528, \"train_runtime_sec\": 2946, \"epochs\": 3, \"total_steps\": 507, \"samples\": 2691}, \"completed_at\": \"2026-05-15T18:04:14.547Z\"}, \"eval_plan_001_flat_nli\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:57:09.693Z\", \"updated_at\": \"2026-05-15T18:04:13.598Z\", \"hypothesis\": \"Dev eval of flat-NLI RSFT (plan_001). 对比 CED RSFT (3-seed mean rel_f1=0.4596). flat-NLI ≈ CED → CED contrastive margin 无增益; CED >> flat-NLI → margin 关键。\", \"parent\": \"plan_001_rsft_flat_nli\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_flat_nli --sft_adapter /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/rsft_flat_nli --no-quantize\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"228508\", \"log_path\": \"~/runs/faith-evidence-ie/eval_plan_001_flat_nli.log\", \"submitted_at\": \"2026-05-15T16:57:46.175Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + SFT + RSFT-flat-NLI\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/rsft_output_flat_nli\", \"eval_data\": \"docred dev (985 docs)\", \"wall_clock_seconds\": 3987.4, \"gpu_hours\": 1.11}, \"reproduce\": {\"finished_at\": \"2026-05-15T17:58:40.529Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:58:48.797356+00:00\"}]}, \"metrics\": {\"rel_f1\": 0.4539, \"ign_f1\": 0.4539, \"evi_f1\": 0.8043, \"edcr\": 0.6431, \"precision\": 0.4671, \"recall\": 0.4414, \"evi_precision\": 0.8143, \"evi_recall\": 0.7945, \"format_ok_rate\": 1, \"n_truncated\": 199, \"n_documents\": 985, \"n_predictions\": 15294, \"inference_time_seconds\": 3631}, \"checkpoint_path\": \"/root/autodl-tmp/eval_results/rsft_flat_nli\", \"log_path\": \"~/runs/faith-evidence-ie/eval_plan_001_flat_nli.log\", \"conclusion\": \"success\", \"notes\": \"flat-NLI RSFT dev eval 完成 (985 docs, EXIT_CODE=0)。rel_f1=0.4539, evi_f1=0.8043, edcr=0.6431。与 CED RSFT 3-seed mean 对比: rel_f1 -0.57pp (0.4539 vs 0.4596), evi_f1 -1.00pp (0.8043 vs 0.8143), edcr 差异极小。flat-NLI 接近但略低于 CED，差异在 CED 3-seed 标准差范围内 (σ=0.0127)。注意此为 single seed (42)，与 CED seed=42 的 0.4449 比反而高 +0.90pp。结论：CED contrastive margin 相对 flat p_pos 的增益极小（<1pp rel_f1），不构成显著优势。论文 claim 应聚焦 CED 的其他价值（reranker、GRPO reward）而非 RSFT filtering 的 contrastive margin。199/985 truncated（高于 CED 的 ~170），format 100% OK。\", \"completed_at\": \"2026-05-15T18:04:13.598Z\"}, \"eval_grpo_g8_bf16\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:41:07.474Z\", \"updated_at\": \"2026-05-15T17:57:46.573Z\", \"spec\": {\"command\": \"python -m freige.eval.batch_eval --exp_dir grpo_ced_g8_bf16 --sft_adapter sft_output --checkpoints 80,90,100 --no-quantize --max_new_tokens 1024\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"214552\", \"log_path\": \"~/runs/faith-evidence-ie/eval_grpo_g8_bf16.log\", \"submitted_at\": \"2026-05-15T14:41:06.626Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + SFT + GRPO-G8-bf16\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/grpo_ced_g8_bf16\", \"eval_data\": \"docred dev (985 docs)\", \"parent\": \"plan_011_grpo_g8_bf16\", \"wall_clock_seconds\": 11785.0, \"gpu_hours\": 3.27}, \"hypothesis\": \"Eval GRPO G=8 bf16 checkpoints 80/90/100 on full dev set (985 docs). 验证 catastrophic forgetting 是否在 bf16 LoRA 下复现。rel_f1>0.30 → forgetting 不复现 (QLoRA-specific); rel_f1<0.05 → 复现 (C2 加强)。对比: SFT rel_f1=0.4057, QLoRA GRPO rel_f1=0.2167 (catastrophic).\", \"metrics\": {\"ckpt80_rel_f1\": 0.4456, \"ckpt80_ign_f1\": 0.4456, \"ckpt80_evi_f1\": 0.8034, \"ckpt80_edcr\": 0.6409, \"ckpt80_format_ok\": \"984/985\", \"ckpt80_truncated\": 50, \"ckpt90_rel_f1\": 0.4523, \"ckpt90_ign_f1\": 0.4523, \"ckpt90_evi_f1\": 0.8052, \"ckpt90_edcr\": 0.6414, \"ckpt90_format_ok\": \"983/985\", \"ckpt90_truncated\": 61, \"ckpt100_rel_f1\": 0.4549, \"ckpt100_ign_f1\": 0.4549, \"ckpt100_evi_f1\": 0.8086, \"ckpt100_edcr\": 0.6318, \"ckpt100_format_ok\": \"985/985\", \"ckpt100_truncated\": 61, \"best_checkpoint\": \"ckpt-100\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T17:55:03.372Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:55:12.125002+00:00\"}]}, \"conclusion\": \"success\", \"notes\": \"3 checkpoints 全部评测完成。rel_f1 单调递增 (0.4456→0.4523→0.4549)，evi_f1 同步上升 (0.8034→0.8052→0.8086)。全部 checkpoint 均大幅超过 SFT baseline (0.4057) 和 QLoRA GRPO (0.2167 catastrophic forgetting)。bf16 LoRA GRPO 无 forgetting，且持续改善至 step 100。Best checkpoint: 100 (rel_f1=0.4549, +12.1% over SFT).\", \"checkpoint_path\": \"/root/autodl-tmp/eval_results/grpo_g8_bf16\", \"completed_at\": \"2026-05-15T17:57:31.658Z\"}, \"plan_015_grpo_g4_bf16_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:27:09.496Z\", \"updated_at\": \"2026-05-15T16:54:54.376Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.training.grpo_trainer --model_name /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_dir /root/autodl-tmp/data/docred --stage 3 --tau_start 0.3 --tau_end 0.5 --output_dir /root/autodl-tmp/grpo_g4_bf16_kl001 --num_generations 4 --reward_device cuda --per_device_batch_size 1 --gradient_accumulation_steps 16 --num_epochs 1 --learning_rate 5e-6 --seed 42 --kl_coef 0.01 --save_steps 20 --save_total_limit 20 --max_steps 200 --format_reward_weight 0.3 --f1_reward_weight 3.0 --ced_reward_weight 1.0 --num_iterations 1 --no-quantize --wandb_run_name plan_015_grpo_g4_bf16_v3\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"226476\", \"log_path\": \"~/runs/faith-evidence-ie/plan_015_grpo_g4_bf16_v3.log\", \"submitted_at\": \"2026-05-15T16:32:42.980Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 3027, \"model_name\": \"Qwen3-4B + SFT adapter\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"N/A (training)\", \"checkpoint_path\": \"/root/autodl-tmp/grpo_g4_bf16_kl001\", \"notes\": \"D052: plan_011 vs mvp2_grpo_ced_kl001_r4 已是 clean ablation。v3 取消，cuda:0 腾给 plan_001 eval。\", \"wall_clock_seconds\": 1331.4, \"gpu_hours\": 0.37}, \"notes\": \"Robustness check, 非 single-variable ablation。lr=5e-6 与对照组 (mvp2_grpo_ced_kl001_r4, lr=5e-5) 不一致。D052 确认 plan_011 (bf16 G=8 kl=0.01 lr=5e-5) vs mvp2_grpo_ced_kl001_r4 (QLoRA G=8 kl=0.01 lr=5e-5) 才是 clean ablation。v3 仅作为额外 robustness data point。\", \"hypothesis\": \"P2 robustness check: bf16 LoRA GRPO G=4, kl=0.01, lr=5e-6。D052 确认 plan_011 vs mvp2_grpo_ced_kl001_r4 已是 clean single-variable quantization ablation (Δ=+23.8pp)。v3 仅为 robustness data point，lr=5e-6 与对照组 lr=5e-5 不一致。\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T16:54:54.376Z\"}, \"plan_015_grpo_g4_bf16_v2\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-15T16:06:43.308Z\", \"updated_at\": \"2026-05-15T16:54:42.310Z\", \"hypothesis\": \"Robustness check: bf16 LoRA GRPO 在 G=4, kl=0, lr=5e-6 条件下是否也防止 catastrophic forgetting。非 single-variable ablation（kl/lr/G 均与 QLoRA 对照组不同）。D052 确认 plan_011 vs mvp2_grpo_ced_kl001_r4 已是 clean quantization ablation。\", \"parent\": \"plan_011_grpo_g8_bf16\", \"completed_at\": \"2026-05-15T16:25:20.634Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"killed\"}}, \"spec\": {\"command\": \"python -m freige.training.grpo_trainer --model_name Qwen3-4B --sft_adapter sft_output --data_dir data/docred --output_dir grpo_g4_bf16_control --stage 3 --num_generations 4 --kl_coef 0 --learning_rate 5e-6 --max_steps 100 --no-quantize --wandb_run_name plan_015_grpo_g4_bf16_v2\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"222942\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 3027, \"model_name\": \"Qwen3-4B + SFT adapter\", \"seed\": 42, \"notes\": \"kl_coef=0 配置错误最终确认 kill。Director 指令以 plan_015_v3 (kl=0.01) 替代。\", \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"N/A (training)\", \"checkpoint_path\": \"/root/autodl-tmp/grpo_g4_bf16_control\", \"log_path\": \"~/runs/faith-evidence-ie/plan_015_grpo_g4_bf16_v2.log\"}, \"conclusion\": \"killed\"}, \"plan_015_grpo_g4_bf16\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:58:43.784Z\", \"updated_at\": \"2026-05-15T16:03:08.279Z\", \"spec\": {\"command\": \"python -m freige.training.grpo_trainer --model_name Qwen3-4B --sft_adapter sft_output --data_dir data/docred --output_dir grpo_ced_g4_bf16 --stage 3 --num_generations 4 --kl_coef 0 --learning_rate 5e-5 --max_steps 100 --no-quantize --wandb_run_name plan_015_grpo_g4_bf16\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"222937\", \"log_path\": \"~/runs/faith-evidence-ie/plan_015_grpo_g4_bf16.log\", \"submitted_at\": \"2026-05-15T15:58:43.532Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 3027, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"wall_clock_seconds\": 264.7, \"gpu_hours\": 0.07}, \"hypothesis\": \"bf16 LoRA GRPO clean control: 与原始 QLoRA GRPO 仅改 quantization（4-bit → bf16），保持 G=4, kl=0, CED reward 不变。验证 catastrophic forgetting 是否由 QLoRA quantization 导致。\", \"conclusion\": \"killed\", \"notes\": \"cuda:0 冲突，与 plan_001_rsft_flat_nli (PID 219556) 冲突。plan_001 先到先得，plan_015 被终止。待 plan_001 完成后重新提交 plan_015。\", \"completed_at\": \"2026-05-15T16:03:08.279Z\"}, \"plan_011_grpo_g8_bf16\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:59:50.014Z\", \"updated_at\": \"2026-05-15T15:55:53.725Z\", \"hypothesis\": \"GRPO G=8 bf16 LoRA: 验证 catastrophic forgetting 是否在 bf16（非 QLoRA 4-bit）下仍复现。CED reward + kl_coef=0.01, 100 steps。如仍 fail → 加强 Claim 3\", \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=3 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 /root/miniconda3/bin/python -m freige.training.grpo_trainer --model_name /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_dir /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/grpo_ced_g8_bf16 --stage 3 --num_generations 8 --kl_coef 0.01 --learning_rate 5e-5 --max_steps 100 --save_steps 10 --save_total_limit 10 --per_device_batch_size 1 --gradient_accumulation_steps 1 --format_reward_weight 0.3 --f1_reward_weight 3.0 --ced_reward_weight 1.0 --num_iterations 1 --no-quantize --wandb_run_name plan_011_grpo_g8_bf16\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"210099\", \"log_path\": \"~/runs/faith-evidence-ie/plan_011_grpo_g8_bf16.log\", \"submitted_at\": \"2026-05-15T14:00:10.122Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 6943.6, \"gpu_hours\": 1.93}, \"log_path\": \"/root/runs/faith-evidence-ie/plan_011_grpo_g8_bf16.log\", \"checkpoint_path\": \"/root/autodl-tmp/grpo_ced_g8_bf16\", \"reproduce\": {\"finished_at\": \"2026-05-15T14:35:19.476Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T14:35:23.573303+00:00\"}]}, \"metrics\": {\"final_step\": 100, \"train_runtime_s\": 554, \"reward_final\": 1.795, \"f1_reward_final\": 1.002, \"ced_reward_final\": 0.494, \"format_reward_final\": 0.3, \"frac_zero_std_final\": 0, \"kl_final\": 0.022, \"best_reward_step\": 85, \"best_reward\": 2.858, \"best_f1_reward\": 1.85, \"mode_collapse\": false, \"lora_config\": \"r=64, alpha=128, dropout=0.05, bf16\", \"checkpoints\": \"10 checkpoints (step 10-100)\"}, \"notes\": \"训练完成 (100/100 steps, EXIT_CODE=0, 554s/9.2min)。无 mode collapse (frac_zero_std=0.0 全程)。KL 极低 (0.005-0.052)。训练 metrics 比 QLoRA 更好 (reward 1.795 vs 1.195, 无 frac_zero_std 升高)。但 QLoRA 训练 metrics 也不差，问题在 eval。必须 eval 才能判断 catastrophic forgetting 是算法层面还是量化问题。\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T15:55:53.725Z\"}, \"plan_011_grpo_g8_bf16_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:43:48.481Z\", \"updated_at\": \"2026-05-15T15:55:52.592Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.eval.inference --model_path /root/autodl-tmp/grpo_ced_g8_bf16/checkpoint-100 --sft_adapter /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/grpo_g8_bf16_ckpt100 --no-quantize\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"216356\", \"log_path\": \"~/runs/faith-evidence-ie/plan_011_grpo_g8_bf16_eval.log\", \"submitted_at\": \"2026-05-15T14:47:35.396Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 4097.2, \"gpu_hours\": 1.14}, \"reproduce\": {\"finished_at\": \"2026-05-15T15:51:35.239Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T15:51:38.162514+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"rel_f1\": 0.4549, \"ign_f1\": 0.4549, \"evi_f1\": 0.8086, \"edcr\": 0.6318, \"format_ok_rate\": 1, \"n_truncated\": 61, \"n_total\": 985, \"n_predictions\": 10701, \"checkpoint\": \"checkpoint-100\", \"model\": \"Qwen3-4B + SFT merged + GRPO bf16 LoRA ckpt-100\", \"inference_time_s\": 3170.3}, \"checkpoint_path\": \"/root/autodl-tmp/eval_results/grpo_g8_bf16_ckpt100\", \"log_path\": \"~/runs/faith-evidence-ie/plan_011_grpo_g8_bf16_eval.log\", \"notes\": \"bf16 GRPO G=8 checkpoint-100 full dev eval (985 docs). F1=0.4549 (+4.92pp vs SFT 0.4057), Evi-F1=0.8086 (+1.07pp vs SFT 0.7979), EDCR=0.6318. Catastrophic forgetting 不复现——bf16 LoRA 下 GRPO 性能甚至超过 SFT baseline。与 QLoRA GRPO (rel_f1=0.2167) 形成鲜明对比。61/985 truncated, 100% format OK. 关键结论: forgetting 是 QLoRA 4-bit 量化导致, 非 GRPO 算法本身问题。但注意此实验同时改了 quantization(bf16 vs 4bit) + group_size(8 vs 4), 需 plan_015 隔离变量。\", \"completed_at\": \"2026-05-15T15:55:52.592Z\"}, \"plan_004_dreeam_baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:47:01.947Z\", \"updated_at\": \"2026-05-15T15:44:24.920Z\", \"hypothesis\": \"Phase A: 复现 DREEAM fully-supervised teacher (RoBERTa-large) DocRED dev Evi-F1≈54.15, RE-F1≈63.49。论文报告的57.34是student model在test set的结果，需4阶段self-training pipeline。\", \"spec\": {\"command\": \"cd /root/autodl-tmp/baselines/dreeam && python run.py --do_train --data_dir dataset/docred --transformer_type roberta --model_name_or_path roberta-large --train_file train_annotated.json --dev_file dev.json --save_path checkpoints/teacher_roberta --train_batch_size 4 --test_batch_size 8 --num_train_epochs 30 --num_class 97 --seed 66\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:2\"], \"pid\": \"213006\", \"log_path\": \"~/runs/faith-evidence-ie/plan_004_dreeam_baseline.log\", \"submitted_at\": \"2026-05-15T14:29:38.364Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"roberta-large\", \"data_path\": \"/root/autodl-tmp/baselines/dreeam/dataset/docred\", \"data_count\": 3053, \"seed\": 66, \"checkpoint_path\": \"/root/autodl-tmp/baselines/dreeam/checkpoints/teacher_roberta/2026-05-15_22:29:42.720935/last.ckpt\", \"wall_clock_seconds\": 4486.6, \"gpu_hours\": 1.25}, \"reproduce\": {\"finished_at\": \"2026-05-15T15:42:51.417Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T15:42:53.896000+00:00\"}]}, \"metrics\": {\"dev_rel_f1\": 63.57, \"dev_rel_ign_f1\": 61.72, \"dev_evi_f1\": 54.01, \"dev_rel_p\": 66.95, \"dev_rel_r\": 60.51, \"dev_evi_p\": 60.53, \"dev_evi_r\": 48.76}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T15:44:24.920Z\"}, \"mvp2_eval_rsft_r2b_maxtok1536_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:54:57.156Z\", \"updated_at\": \"2026-05-15T15:21:13.816Z\", \"hypothesis\": \"Truncation diagnosis: r2b eval with max_new_tokens=1536 (vs default 1024). Retry with correct model stack (Base+SFT+RSFT). If EDCR improves significantly (from 0.6609 toward 0.71+), truncation is the cause. If unchanged, distractor citation is genuine RSFT behavior.\", \"parent\": \"mvp2_eval_rsft_r2b\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"rtx5090-4x\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-15T11:55:17.608Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && rm -rf /root/autodl-tmp/eval_results/rsft_r2b_maxtok1536/* && python -m freige.eval.inference --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --model_path /root/autodl-tmp/rsft_output_r2b --data_path /root/autodl-tmp/data/docred --no-quantize --max_new_tokens 1536 --output_dir /root/autodl-tmp/eval_results/rsft_r2b_maxtok1536\\\"\", \"finished_at\": \"2026-05-15T14:55:32.781Z\", \"training_hours\": 3.0}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && rm -rf /root/autodl-tmp/eval_results/rsft_r2b_maxtok1536/* && python -m freige.eval.inference --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --model_path /root/autodl-tmp/rsft_output_r2b --data_path /root/autodl-tmp/data/docred --no-quantize --max_new_tokens 1536 --output_dir /root/autodl-tmp/eval_results/rsft_r2b_maxtok1536\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"197381\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_eval_rsft_r2b_maxtok1536_r2.log\", \"submitted_at\": \"2026-05-15T11:55:18.697Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 12352.2, \"gpu_hours\": 3.43}, \"pid\": \"197381\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_eval_rsft_r2b_maxtok1536_r2.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T14:55:34.874453+00:00\"}]}, \"metrics\": {\"rel_f1\": 0.4504, \"ign_f1\": 0.4504, \"evi_f1\": 0.8102, \"edcr\": 0.674, \"precision\": 0.4488, \"recall\": 0.4519, \"evi_precision\": 0.8162, \"evi_recall\": 0.8044, \"n_truncated\": 146, \"n_total\": 985, \"n_predictions\": 17188, \"n_distractor_citations\": 19589, \"n_total_citations\": 29063, \"format_ok_rate\": 0.998}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/eval_results/rsft_r2b_maxtok1536/\", \"completed_at\": \"2026-05-15T15:21:10.917Z\", \"notes\": \"max_new_tokens 1536 vs 1024: truncated 179→146 (-33), EDCR 0.6609→0.6740 (+0.0131), rel_f1 0.4493→0.4504, evi_f1 0.8128→0.8102。截断只是 EDCR 偏低的次要因素，distractor citation 是 RSFT 的真实行为。\"}, \"plan_001_flat_nli_scoring\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:36:56.213Z\", \"updated_at\": \"2026-05-15T15:21:03.475Z\", \"hypothesis\": \"flat-NLI scoring 前置步骤：用 flat_nli 模式（p_pos 概率，无 contrastive margin）对 RSFT 生成候选打分并筛选训练数据。\", \"spec\": {\"command\": \"python -m freige.training.rsft_score_filter --scoring_mode flat_nli --top_k 3 --f1_threshold 0.1\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"208155\", \"model_name\": \"DeBERTa-v3-large-mnli-fever-anli-ling-wanli\", \"data_path\": \"/root/autodl-tmp/rsft_generations\", \"data_count\": 21728, \"seed\": 42}, \"reproduce\": {\"finished_at\": \"2026-05-15T15:16:35.698Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T15:16:36.841Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T15:16:38.717977+00:00\"}]}, \"metrics\": {\"total_scored\": 21728, \"selected_samples\": 2691, \"selection_rate\": 0.124, \"selection_strategy\": \"top_k=1\", \"f1_threshold\": 0.1, \"output_path\": \"/root/autodl-tmp/rsft_filtered_flat_nli/rsft_train.jsonl\"}, \"notes\": \"Scoring 实际用 top_k=1（非 spec 中的 top_k=3），与 CED scoring 的 top_k=1 (2718 samples) 公平对比。选出 2691 samples。Cron 误报 failed（假阴性），Reviewer 确认输出完整。\"}, \"mvp2_eval_rsft_s43_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:29:17.551Z\", \"updated_at\": \"2026-05-15T13:54:26.023Z\", \"hypothesis\": \"Full dev eval of RSFT s43 (seed=43). 3rd seed for variance estimation. r1: rel_f1=0.4449, s44: rel_f1=0.4655. Pass: rel_f1 > 0.4057, evi_f1 > 0.798. Retry of mvp2_eval_rsft_s43 (fixed arg names).\", \"parent\": \"mvp2_rsft_train_r1_s43\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_s43 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/eval_results/rsft_s43 --no-quantize\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:2\"], \"pid\": \"194837\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_eval_rsft_s43_r2.log\", \"submitted_at\": \"2026-05-15T11:29:48.250Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 7213.0, \"gpu_hours\": 2.0}, \"pid\": \"194837\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_eval_rsft_s43_r2.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_s43 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/eval_results/rsft_s43 --no-quantize\\\"\", \"finished_at\": \"2026-05-15T13:16:38.318Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T13:16:41.689788+00:00\"}]}, \"metrics\": {\"rel_f1\": 0.4683, \"ign_f1\": 0.4683, \"evi_f1\": 0.8156, \"evi_f1_joint\": 0.3711, \"evi_f1_joint_P\": 0.3747, \"evi_f1_joint_R\": 0.3675, \"edcr\": 0.6388, \"precision\": 0.4817, \"recall\": 0.4556, \"evi_precision\": 0.8142, \"evi_recall\": 0.817, \"n_predictions\": 14970, \"n_truncated\": 171, \"format_ok_rate\": 1, \"inference_time_s\": 6316.7, \"sft_baseline_rel_f1\": 0.4057, \"sft_baseline_evi_f1\": 0.7979, \"delta_rel_f1\": 0.0626, \"delta_evi_f1\": 0.0177, \"delta_evi_f1_joint\": 0.0594, \"mvp2_pass\": true}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/eval_results/rsft_s43\", \"notes\": \"3rd seed PASS. rel_f1=0.4683 (+6.26pp vs SFT), evi_f1=0.8156 (+1.77pp), EDCR=0.6388. 3-seed 完整表: mean rel_f1=0.4596±0.0127, mean evi_f1=0.8143±0.0051. 三个 seed 均稳定超过 SFT baseline。cuda:2 已释放。\", \"completed_at\": \"2026-05-15T13:30:01.258Z\"}, \"mvp2_rsft_ced_scoring_topk3_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T12:12:38.363Z\", \"updated_at\": \"2026-05-15T13:53:08.461Z\", \"hypothesis\": \"CED scoring ablation: top_k=3 (vs top_k=1). More training data (~8000 samples) vs stricter selection (2718 samples). Retry with HF_HUB_OFFLINE=1 (NLI model cached locally).\", \"parent\": \"mvp2_rsft_ced_scoring\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"rtx5090-4x\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-15T12:13:02.778Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && rm -rf /root/autodl-tmp/rsft_filtered_topk3/* && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_score_filter --input_dir /root/autodl-tmp/rsft_generations --output_path /root/autodl-tmp/rsft_filtered_topk3 --nli_model_path cross-encoder/nli-deberta-v3-base --nli_device cuda:0 --selection_strategy top_k --top_k 3 --f1_threshold 0.1 --tau 0.5\\\"\", \"finished_at\": \"2026-05-15T13:19:15.077Z\", \"training_hours\": 1.1}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && rm -rf /root/autodl-tmp/rsft_filtered_topk3/* && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_score_filter --input_dir /root/autodl-tmp/rsft_generations --output_path /root/autodl-tmp/rsft_filtered_topk3 --nli_model_path cross-encoder/nli-deberta-v3-base --nli_device cuda:0 --selection_strategy top_k --top_k 3 --f1_threshold 0.1 --tau 0.5\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"198997\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_rsft_ced_scoring_topk3_r2.log\", \"submitted_at\": \"2026-05-15T12:13:03.900Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 4584.8, \"gpu_hours\": 1.27, \"note\": \"NLI 推理实际跑在 cuda:0 (--nli_device cuda:0)，非 cuda:3。Registry gpu 字段已修正。\"}, \"pid\": \"198997\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_rsft_ced_scoring_topk3_r2.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T13:19:17.812206+00:00\"}]}, \"metrics\": {\"input_generations\": 21728, \"selected_samples\": 8037, \"unique_docs\": 2691, \"selection_rate\": 0.37, \"mean_f1\": 0.5761, \"mean_ced\": 0.6205, \"mean_combined\": 0.6787, \"f1_range_p25\": 0.444, \"f1_range_p75\": 0.717, \"ced_range_p25\": 0.487, \"ced_range_p75\": 0.774, \"truncated_samples\": 1924, \"truncated_pct\": 8.9, \"selection_strategy\": \"top_k=3\", \"f1_threshold\": 0.1, \"topk1_samples\": 2718, \"data_multiplier\": 2.96}, \"conclusion\": \"success\", \"notes\": \"top_k=3 scoring 完成。8037 samples (vs top_k=1 的 2718, 2.96x)。质量下降可控: mean_f1 -0.04, mean_ced -0.048。输出: /root/autodl-tmp/rsft_filtered_topk3/rsft_train.jsonl (24.8MB)。可用于 plan_008 RSFT 训练 ablation。\", \"checkpoint_path\": \"/root/autodl-tmp/rsft_filtered_topk3\", \"completed_at\": \"2026-05-15T13:29:28.749Z\"}, \"mvp2_rsft_train_r1_s44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:36:26.321Z\", \"updated_at\": \"2026-05-15T13:27:38.819Z\", \"hypothesis\": \"RSFT training seed=44 variance estimate. Same params as r1 (bf16 LoRA r=64/α=128, lr=2e-5, 3 epochs, weighted sampling, CED-filtered 2718 samples). Pass: rel_f1 > 0.4057 AND evi_f1 > 0.798.\", \"parent\": \"mvp2_rsft_train_r1\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"rtx5090-4x\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-15T05:38:32.212Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output_s44 --learning_rate 2e-5 --num_epochs 3 --per_device_batch_size 4 --gradient_accumulation_steps 4 --lora_rank 64 --lora_alpha 128 --weighted_sampling --eval_data_dir /root/autodl-tmp/data/docred --eval_max_docs 50 --wandb_run_name rsft-ced-r1-s44 --seed 44\\\"\", \"wandb_run_id\": \"rsft-ced-r1-s44\", \"finished_at\": \"2026-05-15T07:32:40.691Z\", \"training_hours\": 1.9}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output_s44 --learning_rate 2e-5 --num_epochs 3 --per_device_batch_size 4 --gradient_accumulation_steps 4 --lora_rank 64 --lora_alpha 128 --weighted_sampling --eval_data_dir /root/autodl-tmp/data/docred --eval_max_docs 50 --wandb_run_name rsft-ced-r1-s44 --seed 44\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:2\"], \"pid\": \"165672\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_rsft_train_r1_s44.log\", \"submitted_at\": \"2026-05-15T05:39:22.747Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/rsft_output_s44\", \"wall_clock_seconds\": 27283.5, \"gpu_hours\": 7.58}, \"pid\": \"165672\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_rsft_train_r1_s44.log\", \"wandb_run_id\": \"rsft-ced-r1-s44\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T07:32:43.021519+00:00\"}]}, \"metrics\": {\"rel_f1\": 0.4655, \"evi_f1\": 0.8087, \"evi_f1_joint\": 0.3713, \"evi_f1_joint_P\": 0.3775, \"evi_f1_joint_R\": 0.3653, \"edcr\": 0.635, \"sft_baseline_rel_f1\": 0.4057, \"sft_baseline_evi_f1\": 0.7979, \"delta_rel_f1\": 0.0598, \"delta_evi_f1\": 0.0108, \"delta_evi_f1_joint\": 0.0596, \"mvp2_pass\": true}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T13:14:06.295Z\"}, \"mvp2_eval_rsft_r2b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T09:42:58.437Z\", \"updated_at\": \"2026-05-15T13:27:35.580Z\", \"hypothesis\": \"Full dev eval of r2b (1 epoch, alpha=32, lr=1e-5, clean data). Ablation: conservative LoRA scaling vs r2a/r1. Pass: rel_f1 > 0.4057, evi_f1 > 0.798.\", \"parent\": \"mvp2_rsft_r2b\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:3\", \"spec\": {\"command\": \"python -m freige.eval.inference --no-quantize (r2b checkpoint on cuda:3)\", \"server\": \"rtx5090-4x\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + SFT + RSFT r2b\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/rsft_output_r2b\", \"eval_data\": \"/root/autodl-tmp/data/docred/dev.json\", \"pid\": \"189855\"}, \"metrics\": {\"rel_f1\": 0.4493, \"ign_f1\": 0.4493, \"evi_f1\": 0.8128, \"evi_f1_joint\": 0.349, \"evi_f1_joint_P\": 0.3455, \"evi_f1_joint_R\": 0.3526, \"edcr\": 0.6609, \"precision\": 0.4566, \"recall\": 0.4424, \"evi_precision\": 0.8201, \"evi_recall\": 0.8056, \"pred_count\": 14829, \"format_ok\": \"983/985\", \"truncated\": 179, \"inference_time_s\": 5862, \"delta_evi_f1_joint\": 0.0373}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/rsft_output_r2b\", \"log_path\": \"/root/autodl-tmp/eval_results/rsft_r2b/eval.log\", \"completed_at\": \"2026-05-15T11:44:36.428Z\"}, \"mvp2_eval_rsft_r2a\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T09:42:57.684Z\", \"updated_at\": \"2026-05-15T13:27:32.756Z\", \"hypothesis\": \"Full dev eval of r2a (1 epoch, alpha=128, clean data). Ablation: 1 epoch vs 3 epoch (r1). Pass: rel_f1 > 0.4057, evi_f1 > 0.798.\", \"parent\": \"mvp2_rsft_r2a\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:1\", \"spec\": {\"command\": \"python -m freige.eval.inference --no-quantize (r2a checkpoint on cuda:1)\", \"server\": \"rtx5090-4x\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + SFT + RSFT r2a\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/rsft_output_r2a\", \"eval_data\": \"/root/autodl-tmp/data/docred/dev.json\"}, \"conclusion\": \"success\", \"metrics\": {\"rel_f1\": 0.4494, \"ign_f1\": 0.4494, \"evi_f1\": 0.8108, \"evi_f1_joint\": 0.3509, \"evi_f1_joint_P\": 0.3423, \"evi_f1_joint_R\": 0.3599, \"edcr\": 0.6641, \"precision\": 0.4512, \"recall\": 0.4475, \"evi_precision\": 0.8143, \"evi_recall\": 0.8073, \"format_ok_rate\": 1, \"n_predictions\": 15482, \"n_truncated\": 208, \"inference_time_s\": 5967.2, \"delta_evi_f1_joint\": 0.0392}, \"notes\": \"RSFT r2a (1ep, alpha=128/r=64, lr=2e-5, clean 2548 samples). rel_f1=0.4494 (+0.0045 vs r1, +0.0001 vs r2b), evi_f1=0.8108 (-0.0079 vs r1, -0.0020 vs r2b), edcr=0.6641 (+0.0032 vs r2b). 1 epoch with clean data matches r1's 3-epoch rel_f1 while being cheaper. r2a vs r2b (alpha=128 vs 32): nearly identical rel_f1, marginal edcr advantage for higher alpha. All RSFT variants beat SFT baseline on rel_f1/evi_f1 but lose on edcr (0.66-0.66 vs 0.71).\", \"checkpoint_path\": \"/root/autodl-tmp/eval_results/rsft_r2a\", \"log_path\": \"/root/autodl-tmp/eval_results/rsft_r2a/eval.log\", \"completed_at\": \"2026-05-15T11:46:56.410Z\"}, \"mvp2_eval_rsft_r1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T09:40:47.529Z\", \"updated_at\": \"2026-05-15T13:27:31.402Z\", \"hypothesis\": \"Full dev eval of RSFT r1 (seed=42). Same pipeline as s44 eval (985 docs, no-quantize). Need 3-seed data for complete_mvp. s44 PASS: rel_f1=0.4655, evi_f1=0.8087.\", \"parent\": \"mvp2_rsft_train_r1\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:2\", \"spec\": {\"command\": \"python -m freige.eval.inference --no-quantize (r1 checkpoint on cuda:2)\", \"server\": \"rtx5090-4x\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + SFT + RSFT r1\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/rsft_output\", \"eval_data\": \"/root/autodl-tmp/data/docred/dev.json\", \"pid\": \"186329\", \"checkpoint_path\": \"/root/autodl-tmp/rsft_output\", \"log_path\": \"/root/autodl-tmp/eval_results/rsft_r1/eval.log\"}, \"metrics\": {\"rel_f1\": 0.4449, \"evi_f1\": 0.8187, \"evi_f1_joint\": 0.3468, \"evi_f1_joint_P\": 0.3515, \"evi_f1_joint_R\": 0.3423, \"edcr\": 0.6565, \"num_preds\": 15307, \"sft_baseline_rel_f1\": 0.4057, \"sft_baseline_evi_f1\": 0.7979, \"delta_rel_f1\": 0.0392, \"delta_evi_f1\": 0.0208, \"delta_evi_f1_joint\": 0.0351, \"mvp2_pass\": true}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T11:30:26.893Z\"}, \"mvp2_eval_sft_baseline\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-14T21:47:41.356Z\", \"updated_at\": \"2026-05-15T13:27:26.236Z\", \"hypothesis\": \"SFT baseline eval using identical eval protocol as GRPO evals (eval_lr5e6_ckpt20.sh). Required for MVP-2 core comparison: CED_Evi-F1 − SFT_Evi-F1 ≥ 2pp. Prior SFT eval (r3) used different eval path; this ensures apple-to-apple comparison.\", \"parent\": \"mvp2_sft_warmup\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"rtx5090-4x\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-14T21:49:57.466Z\"}, \"notes\": \"[2026-05-15 07:39] Eval 正常完成。结果与 r2/r3 完全一致 (rel_f1=0.4057, evi_f1=0.7979)，apple-to-apple 对比协议复现成功。结果路径: /root/autodl-tmp/sft_baseline_eval_results/metrics.json。cuda:3 已释放。\", \"completed_at\": \"2026-05-14T22:10:34.104Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"[2026-05-15 06:05] RUNNING on cuda:3, PID 104979. Progress: 4/62 batches (6.5%). Shares GPU 3 with mvp2_eval_lr5e6_rp_r2_ckpt20 (PID 103831). ~146s/batch, ETA ~2h20m. Log: tee failed (logs dir missing), output in tmux only. Output dir: /root/autodl-tmp/sft_baseline_eval_results/\"}}, \"spec\": {\"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"account\": \"root\", \"command\": \"python -m freige.eval.inference --model_path /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/sft_baseline_eval_results --quantize\", \"pid\": \"104979\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + SFT LoRA adapter\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"docred dev split\", \"checkpoint_path\": \"/root/autodl-tmp/sft_baseline_eval_results/metrics.json\", \"log_path\": \"N/A - tmux output only\"}, \"conclusion\": \"success\", \"metrics\": {\"rel_f1\": 0.4057, \"evi_f1\": 0.7979, \"evi_f1_joint\": 0.3117, \"evi_f1_joint_P\": 0.3037, \"evi_f1_joint_R\": 0.32, \"edcr\": 0.7118, \"pred_count\": 12234, \"gold_count\": 12151, \"format_ok_rate\": 0.998, \"format_compliance_rate\": 0.998, \"field_compliance_rate\": 0.6264, \"n_truncated\": 367, \"inference_time_seconds\": 6138.5}}, \"mvp2_eval_rsft_r2b_maxtok1536\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:49:48.849Z\", \"updated_at\": \"2026-05-15T13:23:59.642Z\", \"hypothesis\": \"Truncation diagnosis: r2b eval with max_new_tokens=1536 (vs default 1024). If EDCR improves significantly (from 0.6609 toward 0.71+), current EDCR gap is truncation artifact, not model issue. If EDCR unchanged, distractor citation is genuine RSFT behavior.\", \"parent\": \"mvp2_eval_rsft_r2b\", \"spec\": {\"command\": \"python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_r2b --data_path /root/autodl-tmp/data/docred --no-quantize --max_new_tokens 1536 --output_dir /root/autodl-tmp/eval_results/rsft_r2b_maxtok1536\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"196700\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_eval_rsft_r2b_maxtok1536.log\", \"submitted_at\": \"2026-05-15T11:51:37.717Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-4B+SFT+RSFT r2b\", \"checkpoint_source\": \"/root/autodl-tmp/rsft_output_r2b\", \"eval_data\": \"docred dev (985 docs)\", \"seed\": 42, \"purpose\": \"诊断 EDCR 下降是否因 max_new_tokens=1024 截断导致，179/985 docs 被截断，改用 1536 重跑\", \"wall_clock_seconds\": 5541.9, \"gpu_hours\": 1.54}, \"conclusion\": \"killed\", \"notes\": \"Reviewer CRITICAL: 命令缺少 --base_model 和 --sft_adapter，模型 stack 是 Base+RSFT LoRA 而非 Base+SFT+RSFT LoRA，结果不可用。PID 196700 已 kill。重试为 mvp2_eval_rsft_r2b_maxtok1536_r2。\", \"completed_at\": \"2026-05-15T13:23:59.642Z\"}, \"mvp2_rsft_ced_scoring_topk3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:35:23.225Z\", \"updated_at\": \"2026-05-15T13:20:42.443Z\", \"hypothesis\": \"CED scoring ablation: top_k=3 (vs top_k=1). More training data (~8000 samples) vs stricter selection (2718 samples). Answers: does CED filtering strictness affect RSFT training quality?\", \"spec\": {\"command\": \"python -m freige.training.rsft_score_filter --input_dir /root/autodl-tmp/rsft_generations --output_path /root/autodl-tmp/rsft_filtered_topk3 --nli_model_path cross-encoder/nli-deberta-v3-base --nli_device cuda:0 --selection_strategy top_k --top_k 3 --f1_threshold 0.1 --tau 0.5\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"198680\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_rsft_ced_scoring_topk3.log\", \"submitted_at\": \"2026-05-15T12:09:41.690Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/rsft_generations/generations.jsonl\", \"data_count\": 21952, \"model_name\": \"cross-encoder/nli-deberta-v3-base\", \"seed\": 42, \"wall_clock_seconds\": 4260.8, \"gpu_hours\": 1.18}, \"conclusion\": \"killed\", \"notes\": \"NLI 模型加载失败 (HuggingFace Network unreachable)。命令缺少 HF_HOME/HF_HUB_OFFLINE/TRANSFORMERS_OFFLINE 环境变量。重试为 mvp2_rsft_ced_scoring_topk3_r2。\", \"completed_at\": \"2026-05-15T13:20:42.443Z\"}, \"mvp2_rsft_r2b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T08:57:46.813Z\", \"updated_at\": \"2026-05-15T13:14:23.368Z\", \"hypothesis\": \"RSFT r2b: data fix + training dynamics fix (1 epoch + filter truncated + LoRA alpha=32/r=64 scaling 0.5 + lr=1e-5). Isolates: is conservative LoRA scaling the key factor? Pass: rel_f1 > 0.4057, evi_f1 > 0.798.\", \"parent\": \"mvp2_rsft_train_r1\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"rtx5090-4x\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-15T08:58:45.465Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train_clean.jsonl --output_dir /root/autodl-tmp/rsft_output_r2b --learning_rate 1e-5 --num_epochs 1 --per_device_batch_size 4 --gradient_accumulation_steps 4 --lora_rank 64 --lora_alpha 32 --weighted_sampling --save_steps 50 --eval_data_dir /root/autodl-tmp/data/docred --eval_max_docs 50 --wandb_run_name rsft-r2b --seed 42\\\"\", \"wandb_run_id\": \"rsft-r2b\", \"finished_at\": \"2026-05-15T09:35:56.802Z\", \"training_hours\": 0.62}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train_clean.jsonl --output_dir /root/autodl-tmp/rsft_output_r2b --learning_rate 1e-5 --num_epochs 1 --per_device_batch_size 4 --gradient_accumulation_steps 4 --lora_rank 64 --lora_alpha 32 --weighted_sampling --save_steps 50 --eval_data_dir /root/autodl-tmp/data/docred --eval_max_docs 50 --wandb_run_name rsft-r2b --seed 42\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"183587\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_rsft_r2b.log\", \"submitted_at\": \"2026-05-15T09:00:01.270Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/rsft_output_r2b\", \"wall_clock_seconds\": 15262.1, \"gpu_hours\": 4.24}, \"pid\": \"183587\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_rsft_r2b.log\", \"wandb_run_id\": \"rsft-r2b\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T09:35:58.776100+00:00\"}]}, \"notes\": \"训练完成 (160 steps, 33.7min, eval_loss=0.7545)。TaskEvalCallback rel_f1=0.0504 是已知 bug (D038: gold triples 分母不匹配)，不代表真实性能。需全量 dev eval 确认实际指标。\", \"conclusion\": \"success\", \"metrics\": {\"rel_f1\": 0.4493, \"evi_f1\": 0.8128, \"edcr\": 0.6609, \"sft_baseline_rel_f1\": 0.4057, \"sft_baseline_evi_f1\": 0.7979, \"delta_rel_f1\": 0.0436, \"delta_evi_f1\": 0.0149, \"mvp2_pass\": true}, \"completed_at\": \"2026-05-15T13:14:23.368Z\"}, \"mvp2_rsft_r2a\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T08:57:46.140Z\", \"updated_at\": \"2026-05-15T13:14:22.509Z\", \"hypothesis\": \"RSFT r2a: data fix only (1 epoch + filter 170 truncated JSON → 2548 samples). Same LoRA alpha=128/r=64, lr=2e-5 as r1. Isolates: does 1 epoch + clean data alone fix the ontology collapse? Pass: rel_f1 > 0.4057, evi_f1 > 0.798.\", \"parent\": \"mvp2_rsft_train_r1\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"rtx5090-4x\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-15T08:58:44.826Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train_clean.jsonl --output_dir /root/autodl-tmp/rsft_output_r2a --learning_rate 2e-5 --num_epochs 1 --per_device_batch_size 4 --gradient_accumulation_steps 4 --lora_rank 64 --lora_alpha 128 --weighted_sampling --save_steps 50 --eval_data_dir /root/autodl-tmp/data/docred --eval_max_docs 50 --wandb_run_name rsft-r2a --seed 42\\\"\", \"wandb_run_id\": \"rsft-r2a\", \"finished_at\": \"2026-05-15T09:36:15.752Z\", \"training_hours\": 0.63}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train_clean.jsonl --output_dir /root/autodl-tmp/rsft_output_r2a --learning_rate 2e-5 --num_epochs 1 --per_device_batch_size 4 --gradient_accumulation_steps 4 --lora_rank 64 --lora_alpha 128 --weighted_sampling --save_steps 50 --eval_data_dir /root/autodl-tmp/data/docred --eval_max_docs 50 --wandb_run_name rsft-r2a --seed 42\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"183504\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_rsft_r2a.log\", \"submitted_at\": \"2026-05-15T08:59:58.168Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/rsft_output_r2a\", \"wall_clock_seconds\": 15264.3, \"gpu_hours\": 4.24}, \"pid\": \"183504\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_rsft_r2a.log\", \"wandb_run_id\": \"rsft-r2a\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T09:36:20.493042+00:00\"}]}, \"notes\": \"训练完成 (160 steps, 35.5min, eval_loss=0.7547)。TaskEvalCallback rel_f1=0.0509 是已知 bug (D038: gold triples 分母不匹配)，不代表真实性能。需全量 dev eval 确认实际指标。\", \"conclusion\": \"success\", \"metrics\": {\"rel_f1\": 0.4494, \"evi_f1\": 0.8108, \"edcr\": 0.6641, \"sft_baseline_rel_f1\": 0.4057, \"sft_baseline_evi_f1\": 0.7979, \"delta_rel_f1\": 0.0437, \"delta_evi_f1\": 0.0129, \"mvp2_pass\": true}, \"completed_at\": \"2026-05-15T13:14:22.510Z\"}, \"mvp2_rsft_diagnosis\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:55:04.100Z\", \"updated_at\": \"2026-05-15T12:09:32.257Z\", \"hypothesis\": \"RSFT failure root cause: rel_f1=0.0483 vs SFT 0.4057. Diagnose: training data distribution (relation count), step-170 checkpoint output analysis, SFT vs RSFT data comparison.\", \"conclusion\": \"success\", \"metrics\": {\"root_cause\": \"overfitting_plus_sft_knowledge_overwrite\", \"truncated_json_samples\": 170, \"truncated_pct\": 6.3, \"epoch1_eval_loss\": 0.756, \"epoch2_eval_loss\": 0.759, \"lora_scaling\": 2, \"rsft_zero_relation_samples\": 170, \"sft_zero_relation_docs\": 26, \"rsft_mean_relations\": 11.2, \"sft_mean_relations\": 12.5}, \"checkpoint_path\": \"N/A (diagnosis task, no checkpoint)\", \"log_path\": \"N/A (diagnosis task)\", \"completed_at\": \"2026-05-15T12:09:32.257Z\"}, \"mvp2_eval_ced_kl001_r4_last\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:10:05.820Z\", \"updated_at\": \"2026-05-15T12:09:21.004Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && cd /root/autodl-tmp/freige && CUDA_VISIBLE_DEVICES=0 python -m freige.eval.batch_eval --exp_dir /root/autodl-tmp/grpo_ced_kl001 --sft_adapter /root/autodl-tmp/sft_output --output_dir /root/autodl-tmp/eval_results/grpo_ced_kl001 --checkpoints 90,100 --quantize\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"unknown\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_eval_ced_kl001_r4_last.log\", \"submitted_at\": \"2026-05-14T18:10:05.342Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 64755.7, \"gpu_hours\": 17.99}, \"notes\": \"已被拆分为独立 eval：ckpt-90 → mvp2_eval_ced_kl001_r4_ckpt90 (cuda:3)，ckpt-100 → mvp2_eval_ced_kl001_r4_step100 (cuda:0)。此条目作废。\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T12:09:21.004Z\"}, \"mvp2_grpo_ced_kl001_r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:25:06.729Z\", \"updated_at\": \"2026-05-15T12:09:20.252Z\", \"hypothesis\": \"kl_coef=0.01 (vs r5 kl_coef=0.0) prevents CED mode collapse while keeping QLoRA 4-bit compatible — answers whether KL regularization is necessary (retry: fix --lr + bash -c wrapping)\", \"parent\": \"mvp2_grpo_ced_kl001\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.training.grpo_trainer --stage 3 --kl_coef 0.01 --num_iterations 1 --save_steps 20 --save_total_limit 20 --format_reward_weight 0.3 --f1_reward_weight 3.0 --ced_reward_weight 1.0 --learning_rate 5e-5 --gradient_accumulation_steps 16 --num_generations 4\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"65740\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_grpo_ced_kl001_r3.log\", \"submitted_at\": \"2026-05-14T15:25:17.200Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 74643.1, \"gpu_hours\": 20.73}, \"notes\": \"失败原因: datasets 库不支持 thunlp/docred 自定义脚本 (RuntimeError: Dataset scripts are no longer supported)。命令缺少 --data_dir /root/autodl-tmp/data/docred 参数，触发 HF 远程下载失败。需要补全所有必要参数后重新提交。error_type: infrastructure | can_auto_fix: true\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T12:09:20.252Z\"}, \"mvp2_grpo_ced_kl001_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:23:16.518Z\", \"updated_at\": \"2026-05-15T12:09:19.263Z\", \"hypothesis\": \"kl_coef=0.01 (vs r5 kl_coef=0.0) prevents CED mode collapse while keeping QLoRA 4-bit compatible — answers whether KL regularization is necessary (retry: fix --lr → --learning_rate)\", \"parent\": \"mvp2_grpo_ced_kl001\", \"spec\": {\"command\": \"python -m freige.training.grpo_trainer --stage 3 --kl_coef 0.01 --num_iterations 1 --save_steps 20 --save_total_limit 20 --format_reward_weight 0.3 --f1_reward_weight 3.0 --ced_reward_weight 1.0 --learning_rate 5e-5 --gradient_accumulation_steps 16 --num_generations 4\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"unknown\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_grpo_ced_kl001_r2.log\", \"submitted_at\": \"2026-05-14T15:23:31.047Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 74748.2, \"gpu_hours\": 20.76}, \"conclusion\": \"killed\", \"notes\": \"失败原因: 命令未用 bash -c 包裹，tmux 以 sh 执行导致 source 命令失败。error_type: infrastructure | can_auto_fix: true\", \"completed_at\": \"2026-05-15T12:09:19.263Z\"}, \"mvp2_rsft_train_r2_fix\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T08:38:03.815Z\", \"updated_at\": \"2026-05-15T12:09:18.298Z\", \"hypothesis\": \"RSFT r2 fix: 4 fixes based on r1 diagnosis. 1) 1 epoch (vs 3), 2) LoRA alpha=32/r=64 (scaling 0.5 vs 2.0), 3) filtered truncated JSON (~2548 vs 2718 samples), 4) lr=1e-5 (vs 2e-5). Pass: rel_f1 > 0.4057, evi_f1 > 0.798.\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T12:09:18.298Z\"}, \"mvp2_rsft_train_r1_s43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:36:25.275Z\", \"updated_at\": \"2026-05-15T11:31:48.727Z\", \"hypothesis\": \"RSFT training seed=43 variance estimate. Same params as r1 (bf16 LoRA r=64/α=128, lr=2e-5, 3 epochs, weighted sampling, CED-filtered 2718 samples). Pass: rel_f1 > 0.4057 AND evi_f1 > 0.798.\", \"parent\": \"mvp2_rsft_train_r1\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"rtx5090-4x\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-15T05:38:31.664Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output_s43 --learning_rate 2e-5 --num_epochs 3 --per_device_batch_size 4 --gradient_accumulation_steps 4 --lora_rank 64 --lora_alpha 128 --weighted_sampling --eval_data_dir /root/autodl-tmp/data/docred --eval_max_docs 50 --wandb_run_name rsft-ced-r1-s43 --seed 43\\\"\", \"wandb_run_id\": \"rsft-ced-r1-s43\", \"finished_at\": \"2026-05-15T07:37:49.819Z\", \"training_hours\": 1.99}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output_s43 --learning_rate 2e-5 --num_epochs 3 --per_device_batch_size 4 --gradient_accumulation_steps 4 --lora_rank 64 --lora_alpha 128 --weighted_sampling --eval_data_dir /root/autodl-tmp/data/docred --eval_max_docs 50 --wandb_run_name rsft-ced-r1-s43 --seed 43\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"165590\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_rsft_train_r1_s43.log\", \"submitted_at\": \"2026-05-15T05:39:20.307Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 21148.4, \"gpu_hours\": 5.87}, \"pid\": \"165590\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_rsft_train_r1_s43.log\", \"wandb_run_id\": \"rsft-ced-r1-s43\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T07:37:52.173054+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/rsft_output_s43\", \"metrics\": {\"eval_loss\": 0.7622, \"train_loss\": 0.6148, \"eval_entropy\": 0.6724, \"mean_token_accuracy\": 0.8291, \"total_steps\": 510, \"epochs\": 3, \"training_hours\": 1.99}, \"conclusion\": \"success\", \"notes\": \"训练正常完成 (510 steps, 1.99h, eval_loss=0.7622, train_loss=0.6148)。与 s44 (eval_loss=未记录) 和 r1 相近。TaskEvalCallback rel_f1 是已知 bug，需全量 eval。全量 eval 重试 mvp2_eval_rsft_s43_r2 正在运行中。\", \"completed_at\": \"2026-05-15T11:31:48.727Z\"}, \"mvp2_eval_rsft_s43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:25:26.268Z\", \"updated_at\": \"2026-05-15T11:29:11.205Z\", \"hypothesis\": \"Full dev eval of RSFT s43 (seed=43). 3rd seed for variance estimation. r1: rel_f1=0.4449, s44: rel_f1=0.4655. Pass: rel_f1 > 0.4057, evi_f1 > 0.798.\", \"parent\": \"mvp2_rsft_train_r1_s43\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.eval.inference --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_adapter /root/autodl-tmp/rsft_output_s43 --data_dir /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/eval_results/rsft_s43 --no-quantize --gpu 0\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:2\"], \"pid\": \"194296\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_eval_rsft_s43.log\", \"submitted_at\": \"2026-05-15T11:26:15.318Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 18.9, \"gpu_hours\": 0.01}, \"pid\": \"194296\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_eval_rsft_s43.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.eval.inference --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_adapter /root/autodl-tmp/rsft_output_s43 --data_dir /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/eval_results/rsft_s43 --no-quantize --gpu 0\\\"\", \"finished_at\": \"2026-05-15T11:26:32.872Z\"}, \"failure_reason\": \"EXIT_CODE=2 (shell misuse / syntax)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T11:26:34.235Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T11:26:36.157796+00:00\"}]}, \"notes\": \"参数名错误导致失败: --rsft_adapter 应为 --model_path, --data_dir 应为 --data_path, --gpu 0 不存在。重试为 mvp2_eval_rsft_s43_r2。\"}, \"mvp2_rsft_train_r1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:27:39.073Z\", \"updated_at\": \"2026-05-15T09:40:39.078Z\", \"hypothesis\": \"RSFT training on CED-filtered data (2718 samples, mean CED=0.668). SFT warmup baseline: rel_f1=0.4057, evi_f1=0.798. Pass criteria: rel_f1 > 0.4057 AND evi_f1 > 0.798.\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output --learning_rate 2e-5 --num_epochs 3 --per_device_batch_size 4 --gradient_accumulation_steps 4 --lora_rank 64 --lora_alpha 128 --weighted_sampling --eval_data_dir /root/autodl-tmp/data/docred --eval_max_docs 50 --wandb_run_name rsft-ced-r1 --seed 42\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"165130\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_rsft_train_r1.log\", \"submitted_at\": \"2026-05-15T05:37:57.880Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 7210.1, \"gpu_hours\": 2.0}, \"pid\": \"165130\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_rsft_train_r1.log\", \"wandb_run_id\": \"rsft-ced-r1\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output --learning_rate 2e-5 --num_epochs 3 --per_device_batch_size 4 --gradient_accumulation_steps 4 --lora_rank 64 --lora_alpha 128 --weighted_sampling --eval_data_dir /root/autodl-tmp/data/docred --eval_max_docs 50 --wandb_run_name rsft-ced-r1 --seed 42\\\"\", \"wandb_run_id\": \"rsft-ced-r1\", \"finished_at\": \"2026-05-15T07:35:10.628Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T07:35:13.068974+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/rsft_output\", \"metrics\": {\"rel_f1\": 0.0483, \"num_preds\": 848, \"sft_baseline_rel_f1\": 0.4057, \"failure_mode\": \"relation_ontology_collapse_to_freetext\", \"epoch1_eval_loss\": 0.756, \"epoch2_eval_loss\": 0.759}, \"completed_at\": \"2026-05-15T07:38:07.936Z\", \"notes\": \"D037 修正: TaskEvalCallback 的 rel_f1=0.0483 是 eval bug（gold triples 未限制为 eval_max_docs 子集）。全量 eval 待跑。s44 全量 eval 已 PASS: rel_f1=0.4655, evi_f1=0.8087。\"}, \"mvp2_rsft_ced_scoring\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:27:32.788Z\", \"updated_at\": \"2026-05-15T05:33:16.769Z\", \"hypothesis\": \"CED scoring + filtering on 4 shard RSFT generations. top_k=1, f1_threshold=0.1. 21952 → 2718 selected (12.4%).\", \"spec\": {\"command\": \"python -m freige.training.rsft_score_filter --input_dir /root/autodl-tmp/rsft_generations --output_path /root/autodl-tmp/rsft_filtered/rsft_train.jsonl --selection_strategy top_k --top_k 1 --f1_threshold 0.1\", \"server\": \"rtx5090-4x\", \"data_path\": \"/root/autodl-tmp/rsft_generations/\", \"data_count\": 21952, \"model_name\": \"cross-encoder/nli-deberta-v3-base\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/rsft_filtered/rsft_train.jsonl\", \"log_path\": \"/root/autodl-tmp/rsft_filtered/rsft_combined_report.json\"}, \"conclusion\": \"success\", \"metrics\": {\"input_generations\": 21952, \"selected_samples\": 2718, \"unique_docs\": 2691, \"selection_rate\": 0.124, \"mean_f1\": 0.6157, \"mean_ced\": 0.6683, \"f1_range\": [0.1026, 1], \"zero_f1_samples\": 0, \"selection_strategy\": \"top_k=1\", \"f1_threshold\": 0.1}, \"completed_at\": \"2026-05-15T05:33:16.769Z\"}, \"mvp2_rsft_gen_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T01:39:26.572Z\", \"updated_at\": \"2026-05-15T05:21:50.725Z\", \"spec\": {\"pid\": \"135867\"}, \"hypothesis\": \"RSFT generation shard 0/4: N=8 generations at T=0.7 with generation_config override (top_k=0). OOM fix: batch_size=1.\", \"parent\": \"mvp2_sft_warmup\", \"reproduce\": {\"finished_at\": \"2026-05-15T04:54:30.317Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T04:54:31.450Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T04:54:36.643913+00:00\"}]}, \"notes\": \"[2026-05-15 05:01] 生成完成 682/682 docs (100%)。EXIT_CODE=143 是正常完成后的清理 SIGTERM。format_ok 99.6%, truncation_rate 10.1%, diversity 7.6/8。\"}, \"mvp2_rsft_gen_s3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T01:39:34.645Z\", \"updated_at\": \"2026-05-15T05:01:10.955Z\", \"spec\": {\"pid\": \"137985\"}, \"hypothesis\": \"RSFT generation shard 3/4: N=8 generations at T=0.7 with generation_config override (top_k=0). OOM fix: batch_size=1.\", \"parent\": \"mvp2_sft_warmup\", \"reproduce\": {\"finished_at\": \"2026-05-15T04:49:43.444Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T04:49:45.523884+00:00\"}]}, \"conclusion\": \"success\", \"log_path\": \"/root/runs/faith-evidence-ie/mvp2_rsft_gen_s3.log\", \"metrics\": {\"generation_count\": 5288, \"unique_docs\": 659, \"format_compliance\": 0.998, \"diversity_range\": \"7.5-7.8/8\", \"exit_code\": 0}, \"checkpoint_path\": \"/root/autodl-tmp/rsft_generations/shard_3/generations.jsonl\", \"completed_at\": \"2026-05-15T05:00:41.430Z\"}, \"mvp2_rsft_gen_s2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T01:39:32.299Z\", \"updated_at\": \"2026-05-15T04:37:31.632Z\", \"spec\": {\"pid\": \"136649\"}, \"hypothesis\": \"RSFT generation shard 2/4: N=8 generations at T=0.7 with generation_config override (top_k=0). OOM fix: batch_size=1.\", \"parent\": \"mvp2_sft_warmup\", \"reproduce\": {\"finished_at\": \"2026-05-15T04:36:43.615Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T04:36:45.294Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T04:36:48.376664+00:00\"}]}}, \"mvp2_rsft_gen_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T01:39:29.894Z\", \"updated_at\": \"2026-05-15T04:37:14.926Z\", \"spec\": {\"pid\": \"136270\"}, \"hypothesis\": \"RSFT generation shard 1/4: N=8 generations at T=0.7 with generation_config override (top_k=0). OOM fix: batch_size=1.\", \"parent\": \"mvp2_sft_warmup\", \"reproduce\": {\"finished_at\": \"2026-05-15T04:34:07.774Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T04:34:08.880Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T04:34:14.011538+00:00\"}]}}, \"mvp2_rsft_generate\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T00:09:41.289Z\", \"updated_at\": \"2026-05-15T01:32:10.047Z\", \"hypothesis\": \"RSFT generation phase: SFT model generates N=8 candidate outputs per training sample at T=0.7. CED scoring + filtering后作为 RSFT 训练数据。D031 pivot 方向。\", \"parent\": \"mvp2_sft_warmup\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"rtx5090-4x\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-15T00:09:52.157Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/autodl-tmp && python -m freige.training.rsft_generate --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split train_annotated --output_dir /root/autodl-tmp/rsft_generations --num_generations 8 --temperature 0.7 --batch_size 2 --max_new_tokens 1024 --seed 42\\\"\", \"finished_at\": \"2026-05-15T01:32:08.718Z\", \"training_hours\": 1.37}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/autodl-tmp && python -m freige.training.rsft_generate --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split train_annotated --output_dir /root/autodl-tmp/rsft_generations --num_generations 8 --temperature 0.7 --batch_size 2 --max_new_tokens 1024 --seed 42\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"122144\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_rsft_generate.log\", \"submitted_at\": \"2026-05-15T00:09:53.637Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 4936.4, \"gpu_hours\": 1.37}, \"pid\": \"122144\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_rsft_generate.log\", \"failure_reason\": \"EXIT_CODE=137 (SIGKILL — OOM killer or manual kill)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T01:32:10.047Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T01:32:15.807942+00:00\"}]}}, \"mvp2_diversity_probe\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T00:02:19.966Z\", \"updated_at\": \"2026-05-15T01:31:34.495Z\", \"hypothesis\": \"RSFT viability check: SFT model output diversity at T=0.7/1.0 with N=8 generations. Pass criteria: unique triple-sets >= 5/8.\", \"conclusion\": \"success\", \"metrics\": {\"unique_triples_t07\": 5, \"unique_triples_t10\": 8, \"jaccard_t07\": 0.17, \"jaccard_t10\": 0.051, \"format_ok_rate_t07\": 0.5, \"format_ok_rate_t10\": 0.438, \"n_samples\": 3, \"n_generations\": 8, \"note\": \"unique_triples_t07 corrected from 7 to 5.0 (mean). Reviewer: format_ok ~34% after fix, 'diversity' was JSON key name variants not semantic diversity\"}, \"notes\": \"[2026-05-15 01:35] D034 独立验证结果: 200 docs 实际 diversity=7.11/8 (median=8.0), evidence diversity=5.43/8, format parse rate=90.2%。61.5% 文档达到 8/8 完全不同。之前监控报告的 mean_diversity=1.0/8 是监控计算 bug，非生成质量问题。diversity_probe 早期观察(7/8)是准确的。RSFT 前提成立。\", \"spec\": {\"command\": \"python diversity_probe.py (已完成, 状态修正)\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:2\"], \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 3, \"model_name\": \"Qwen3-4B + SFT adapter\", \"seed\": 42, \"checkpoint_path\": \"N/A (probe only)\", \"log_path\": \"N/A (probe only)\"}, \"completed_at\": \"2026-05-15T01:03:18.175Z\", \"checkpoint_path\": \"N/A (validation probe, no checkpoint)\", \"log_path\": \"N/A (validation probe)\"}, \"mvp2_eval_lr5e6_r1_ckpt100\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T23:00:57.035Z\", \"updated_at\": \"2026-05-15T01:30:01.493Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.eval.inference --model_path /root/autodl-tmp/grpo_ced_lr5e6/checkpoint-100 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/lr5e6_r1_ckpt100/checkpoint-100 --quantize\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"117635\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_eval_lr5e6_r1_ckpt100.log\", \"submitted_at\": \"2026-05-14T23:39:51.199Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 6160.9, \"gpu_hours\": 1.71}, \"hypothesis\": \"P0 ckpt-100 eval: lr=5e-6 GRPO at step 100 (halfway point). Checkpoint-100 已保存。与 kl001_r4 的 step-100 (rel_f1=0.217) 形成直接对比。Pass criteria: rel_f1 > 0.30.\", \"parent\": \"mvp2_grpo_ced_lr5e6_r1\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"rtx5090-4x\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-14T23:39:49.461Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.eval.inference --model_path /root/autodl-tmp/grpo_ced_lr5e6/checkpoint-100 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/lr5e6_r1_ckpt100/checkpoint-100 --quantize\\\"\", \"finished_at\": \"2026-05-15T01:19:34.927Z\", \"training_hours\": 1.66}, \"pid\": \"117635\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_eval_lr5e6_r1_ckpt100.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T01:19:36.799167+00:00\"}]}, \"metrics\": {\"rel_f1\": 0.0138, \"rel_precision\": 0.0132, \"rel_recall\": 0.0144, \"ign_f1\": 0.0138, \"evi_f1\": 0.8504, \"evi_precision\": 0.9256, \"evi_recall\": 0.7866, \"edcr\": 0.9876, \"format_ok_rate\": 0.999, \"field_compliance_rate\": 0.8162, \"evidence_format_rate\": 0.8162, \"tp\": 175, \"pred_count\": 13300, \"gold_count\": 12151, \"n_predictions\": 15498, \"n_truncated\": 181, \"n_documents\": 985, \"n_parseable\": 984, \"inference_time_seconds\": 5901.7}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/grpo_ced_lr5e6/checkpoint-100\", \"completed_at\": \"2026-05-15T01:22:32.071Z\"}, \"mvp2_grpo_ced_lr5e6_r1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T19:21:08.231Z\", \"updated_at\": \"2026-05-15T01:29:06.862Z\", \"hypothesis\": \"D030/P0: lr=5e-6 (10x lower than ced_kl001_r4) prevents catastrophic forgetting while maintaining CED reward improvement. Community consensus GRPO+QLoRA lr=5e-6~1e-5. Pass criteria: ckpt-20 rel_f1 > 0.30. Extra monitoring: pred_count + recall trend.\", \"parent\": \"mvp2_grpo_ced_kl001_r4\", \"spec\": {\"command\": \"python -m freige.training.grpo_trainer --model_name /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_dir /root/autodl-tmp/data/docred --stage 3 --tau_start 0.3 --tau_end 0.5 --output_dir /root/autodl-tmp/grpo_ced_lr5e6 --num_generations 8 --reward_device cuda --per_device_batch_size 1 --gradient_accumulation_steps 16 --num_epochs 1 --learning_rate 5e-6 --seed 42 --kl_coef 0.01 --save_steps 20 --save_total_limit 20 --max_steps 200 --format_reward_weight 0.3 --f1_reward_weight 3.0 --ced_reward_weight 1.0 --num_iterations 1 --wandb_run_name grpo-s3-ced-lr5e6-r1\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"90080\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 3053, \"model_name\": \"Qwen3-4B + SFT adapter\", \"seed\": 42, \"hyperparams\": {\"learning_rate\": 5e-06, \"kl_coef\": 0.01, \"num_generations\": 8, \"gradient_accumulation_steps\": 16, \"max_steps\": 200, \"save_steps\": 20, \"format_reward_weight\": 0.3, \"f1_reward_weight\": 3, \"ced_reward_weight\": 1, \"tau_start\": 0.3, \"tau_end\": 0.5}}, \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:0\", \"pid\": \"90080\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_grpo_ced_lr5e6_r1.log\", \"wandb_run_id\": \"grpo-s3-ced-lr5e6-r1\", \"reproduce\": {\"command\": \"bash -c \\\"source /etc/network_turbo && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.training.grpo_trainer --model_name /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_dir /root/autodl-tmp/data/docred --stage 3 --tau_start 0.3 --tau_end 0.5 --output_dir /root/autodl-tmp/grpo_ced_lr5e6 --num_generations 8 --reward_device cuda --per_device_batch_size 1 --gradient_accumulation_steps 16 --num_epochs 1 --learning_rate 5e-6 --seed 42 --kl_coef 0.01 --save_steps 20 --save_total_limit 20 --max_steps 200 --format_reward_weight 0.3 --f1_reward_weight 3.0 --ced_reward_weight 1.0 --num_iterations 1 --wandb_run_name grpo-s3-ced-lr5e6-r1\\\"\", \"wandb_run_id\": \"grpo-s3-ced-lr5e6-r1\"}, \"notes\": \"[2026-05-15 01:08] D032 执行: PID 90080 killed (force_killed=true)。训练 step ~113/200。完整 lr5e-6 轨迹: ckpt-20→40→60→80 rel_f1 = 0.008/0.007/0.009/0.012，无恢复信号。GRPO+QLoRA 方向判死 (D031)，GPU 释放给 RSFT 流水线。\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T01:07:56.366Z\"}, \"mvp2_eval_lr5e6_r1_ckpt80\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:25:45.043Z\", \"updated_at\": \"2026-05-15T01:02:32.508Z\", \"spec\": {\"data_path\": \"/root/autodl-tmp/data/docred/dev.json\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + SFT + GRPO lr5e6 ckpt-80\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/grpo_ced_lr5e6/checkpoint-80\", \"eval_data\": \"/root/autodl-tmp/data/docred/dev.json\", \"command\": \"CUDA_VISIBLE_DEVICES=2 python -m freige.eval.inference --model_path /root/autodl-tmp/grpo_ced_lr5e6/checkpoint-80 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/lr5e6_r1_ckpt80/checkpoint-80 --quantize\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:2\"], \"pid\": \"111731\", \"account\": \"root\", \"log_path\": \"/tmp/eval_lr5e6_ckpt80.log\", \"checkpoint_path\": \"/root/autodl-tmp/eval_results/lr5e6_r1_ckpt80/checkpoint-80/\"}, \"hypothesis\": \"P0 ckpt-80 eval: lr=5e-6 GRPO at step 80. 训练轨迹继续——ckpt-20 FAIL (0.0077), ckpt-40/60 待出. Step 80 reward=0.283 (回升), format_reward=0.249. Pass criteria: rel_f1 > 0.30.\", \"parent\": \"mvp2_grpo_ced_lr5e6_r1\", \"notes\": \"[2026-05-15 08:56] 正常完成。rel_f1=0.0116，延续 ckpt-20/40/60 的平坦趋势 (0.007-0.012)。evi_f1=0.828 继续上升。lr5e6 轨迹: step 20→40→60→80 rel_f1 = 0.008/0.007/0.009/0.012，无恢复信号。cuda:2 已释放。\", \"conclusion\": \"negative\", \"metrics\": {\"rel_f1\": 0.0116, \"ign_f1\": 0.0116, \"precision\": 0.0109, \"recall\": 0.0124, \"evi_f1\": 0.828, \"evi_precision\": 0.928, \"evi_recall\": 0.748, \"edcr\": 0.993, \"format_ok_rate\": 0.999, \"field_compliance_rate\": 0.788, \"pred_count\": 13828, \"gold_count\": 12151, \"n_truncated\": 210, \"inference_time_seconds\": 6099}, \"completed_at\": \"2026-05-15T00:56:43.952Z\"}, \"mvp2_eval_lr5e6_r1_ckpt60_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:27:56.124Z\", \"updated_at\": \"2026-05-15T00:07:56.895Z\", \"hypothesis\": \"P0 ckpt-60 eval retry: 原 submit_on_allocated 失败 (pid=unknown). 手动 SSH 启动 /root/autodl-tmp/scripts/eval_lr5e6_ckpt60.sh. Pass criteria: rel_f1 > 0.30.\", \"parent\": \"mvp2_grpo_ced_lr5e6_r1\", \"spec\": {\"data_path\": \"/root/autodl-tmp/data/docred/dev.json\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + SFT + GRPO lr5e6 ckpt-60\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/grpo_ced_lr5e6/checkpoint-60\", \"eval_data\": \"/root/autodl-tmp/data/docred/dev.json\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python -m freige.eval.inference --model_path /root/autodl-tmp/grpo_ced_lr5e6/checkpoint-60 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/grpo_ced_lr5e6_ckpt60 --quantize\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"108185\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_eval_lr5e6_r1_ckpt60_r2.log\", \"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/eval_results/grpo_ced_lr5e6_ckpt60/metrics.json\"}, \"conclusion\": \"negative\", \"notes\": \"[2026-05-15 08:07] 正常完成。rel_f1=0.0093，与 ckpt-20 (0.0077) / ckpt-40 (0.0071) 同一量级，无恢复信号。evi_f1=0.81 持续上升（ckpt-20: 0.628, ckpt-40: 0.758），证据抽取在改善但关系能力完全崩塌。结果路径: /root/autodl-tmp/eval_results/grpo_ced_lr5e6_ckpt60/metrics.json。cuda:1 已释放。\", \"metrics\": {\"rel_f1\": 0.0093, \"precision\": 0.0085, \"recall\": 0.0103, \"evi_f1\": 0.81, \"edcr\": 0.993, \"format_ok_rate\": 0.998, \"pred_count\": 14626, \"gold_count\": 12151, \"tp\": 125, \"inference_time_seconds\": 6152}, \"completed_at\": \"2026-05-15T00:07:56.895Z\"}, \"mvp2_eval_lr5e6_r1_ckpt60\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-14T22:13:47.936Z\", \"updated_at\": \"2026-05-14T23:25:25.584Z\", \"hypothesis\": \"P0 ckpt-60 eval: lr=5e-6 GRPO at step 60. 训练轨迹数据点——ckpt-20 catastrophic forgetting (rel_f1=0.0077)，需看后续 checkpoint 是否恢复。Pass criteria: rel_f1 > 0.30.\", \"parent\": \"mvp2_grpo_ced_lr5e6_r1\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && python -m freige.eval.batch_eval --exp_dir /root/autodl-tmp/grpo_ced_lr5e6 --sft_adapter /root/autodl-tmp/sft_output --output_dir /root/autodl-tmp/eval_results/lr5e6_r1_ckpt60 --checkpoints 60 --quantize\\\"\", \"finished_at\": \"2026-05-14T22:25:13.602Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-14T22:25:14.773Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T22:25:16.365584+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"[2026-05-15 07:28] 手动 SSH 启动成功. PID=108025, cuda:1, log=/tmp/eval_lr5e6_ckpt60.log\"}}, \"notes\": \"[2026-05-15 07:24] D031 清理: PID 108025 因 cd path 问题从未产出有效结果。已被 _r2 (PID 108185) 取代。标记 failed 关闭。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 bash /root/autodl-tmp/scripts/eval_lr5e6_ckpt60.sh\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"108025\", \"log_path\": \"/tmp/eval_lr5e6_ckpt60.log\", \"submitted_at\": \"2026-05-14T22:29:00Z\", \"submitted_via\": \"manual_ssh\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/grpo_ced_lr5e6\", \"data_count\": 0, \"model_name\": \"grpo_ced_lr5e6_ckpt60\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/grpo_ced_lr5e6/checkpoint-60\", \"eval_data\": \"batch_eval\", \"checkpoint_path\": \"N/A - process had wrong Python path, never produced valid output\", \"log_path_note\": \"PID 108025 had cd path issue, replaced by _r2 (PID 108185)\", \"wall_clock_seconds\": 3385.6, \"gpu_hours\": 0.94}, \"conclusion\": \"failed\"}, \"mvp2_eval_lr5e6_r1_ckpt40_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:41:34.558Z\", \"updated_at\": \"2026-05-14T23:11:56.267Z\", \"hypothesis\": \"Re-tracking orphan PID 101842 for P0 ckpt-40 eval (lr=5e-6 GRPO step 40). Original exp auto-failed due to cron/PID mismatch. Pass criteria: rel_f1 > 0.30.\", \"parent\": \"mvp2_grpo_ced_lr5e6_r1\", \"spec\": {\"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:2\"], \"account\": \"root\", \"command\": \"CUDA_VISIBLE_DEVICES=2 python -m freige.eval.inference\", \"pid\": \"101842\", \"data_path\": \"/root/autodl-tmp/data/docred/dev.json\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + SFT + GRPO lr5e6 ckpt-40\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/grpo_ced_lr5e6/checkpoint-40\", \"eval_data\": \"/root/autodl-tmp/data/docred/dev.json\", \"log_path\": \"/tmp/eval_lr5e6_ckpt40.log\", \"checkpoint_path\": \"/root/autodl-tmp/grpo_ced_lr5e6/checkpoint-40\", \"conclusion\": \"negative\", \"metrics\": {\"f1\": 0.007146887342486364, \"ign_f1\": 0.007146887342486364, \"precision\": 0.0065816821393931, \"recall\": 0.007818286560776891, \"evi_f1\": 0.7583892617449665, \"edcr\": 0.9942045337983383, \"format_ok_rate\": 0.9939086294416244, \"tp\": 95, \"pred_count\": 14434, \"gold_count\": 12151, \"n_truncated\": 424, \"inference_time_seconds\": 6152.4}, \"result_dir\": \"/root/autodl-tmp/eval_results/lr5e6_r1_ckpt40/checkpoint-40\"}, \"notes\": \"[2026-05-15 06:50] 全面状态检查: PID 101842 存活 (Rl, uptime 1:25), GPU 2: 10644 MiB/74% util. tmux mvp2_eval_lr5e6_r1_ckpt40 alive (创建于 05:25 UTC). 按 92s/batch 估算约 55/62 (89%), ETA ~10min (约UTC 07:00).\", \"conclusion\": \"negative\", \"metrics\": {\"rel_f1\": 0.0071, \"precision\": 0.0066, \"recall\": 0.0078, \"evi_f1\": 0.7584, \"evi_precision\": 0.9113, \"evi_recall\": 0.6494, \"edcr\": 0.9942, \"format_ok_rate\": 0.9939, \"field_compliance_rate\": 0.5675, \"pred_count\": 14434, \"gold_count\": 12151, \"tp\": 95, \"n_truncated\": 424, \"inference_time_seconds\": 6152}, \"completed_at\": \"2026-05-14T23:11:48.225Z\"}, \"mvp2_eval_lr5e6_r1_ckpt20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:44:21.167Z\", \"updated_at\": \"2026-05-14T22:12:16.372Z\", \"spec\": {\"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"account\": \"root\", \"command\": \"bash /root/autodl-tmp/scripts/eval_lr5e6_ckpt20.sh\", \"pid\": \"96500\", \"data_path\": \"/root/autodl-tmp/data/docred/dev.json\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + SFT + GRPO lr5e6 ckpt-20\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/grpo_ced_lr5e6/checkpoint-20\", \"eval_data\": \"/root/autodl-tmp/data/docred/dev.json\", \"log_path\": \"/tmp/eval_lr5e6_ckpt20.log\"}, \"hypothesis\": \"P0 ckpt-20 early eval: lr=5e-6 GRPO at step 20. Pass criteria: rel_f1 > 0.30 (no catastrophic forgetting). Key MVP gate for P0.\", \"parent\": \"mvp2_grpo_ced_lr5e6_r1\", \"conclusion\": \"negative\", \"metrics\": {\"rel_f1\": 0.0077, \"rel_precision\": 0.0071, \"rel_recall\": 0.0084, \"evi_f1\": 0.628, \"evi_precision\": 0.855, \"evi_recall\": 0.496, \"edcr\": 0.993, \"format_ok_rate\": 0.991, \"field_compliance_rate\": 0.399, \"pred_count\": 14440, \"gold_count\": 12151, \"tp\": 102, \"n_truncated\": 587, \"inference_time_seconds\": 6370.4}, \"checkpoint_path\": \"/root/autodl-tmp/grpo_ced_lr5e6/checkpoint-20\", \"log_path\": \"/tmp/eval_lr5e6_ckpt20.log\", \"completed_at\": \"2026-05-14T22:12:16.372Z\"}, \"mvp2_eval_lr5e6_rp_r2_ckpt20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:44:56.448Z\", \"updated_at\": \"2026-05-14T22:06:40.812Z\", \"hypothesis\": \"P0+P1 ckpt-20 eval: lr=5e-6 + recall_penalty GRPO at step 20. Director killed rp_r2 training (loss divergence), but ckpt-20 eval needed to close P0+P1 comparison line. Pass criteria: rel_f1 > 0.30 AND pred_count >= 9720.\", \"parent\": \"mvp2_grpo_ced_lr5e6_rp_r2\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python eval rp_r2 ckpt-20\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"103825\", \"data_path\": \"/root/autodl-tmp/data/docred/dev.json\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + SFT + GRPO lr5e6+recall_penalty ckpt-20\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/grpo_ced_lr5e6_rp/checkpoint-20\", \"eval_data\": \"/root/autodl-tmp/data/docred/dev.json\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T22:06:39.146Z\", \"notes\": \"Director 指令 kill: 让 sft_baseline 独占 cuda:3。rp_r2 eval 优先级低，后面补。进度 11/62 (18%)。\"}, \"mvp2_eval_lr5e6_r1_ckpt40\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:25:00.579Z\", \"updated_at\": \"2026-05-14T21:43:33.438Z\", \"spec\": {\"command\": \"bash /root/autodl-tmp/scripts/eval_lr5e6_ckpt40.sh\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:2\"], \"pid\": \"101842\", \"data_path\": \"/root/autodl-tmp/data/docred/dev.json\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + SFT + GRPO lr5e6 ckpt-40\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/grpo_ced_lr5e6/checkpoint-40\", \"eval_data\": \"/root/autodl-tmp/data/docred/dev.json\", \"log_path\": \"/tmp/eval_lr5e6_ckpt40.log\", \"account\": \"root\"}, \"hypothesis\": \"P0 ckpt-40 eval: lr=5e-6 GRPO at step 40 (where f1_reward first rises to 0.038). Director 新判定框架: ckpt-20 FAIL + ckpt-40 PASS → P0 判 PASS。Pass criteria: rel_f1 > 0.30.\", \"parent\": \"mvp2_grpo_ced_lr5e6_r1\", \"reproduce\": {\"finished_at\": \"2026-05-14T21:36:46.425Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T21:36:47.089Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T21:36:48.294849+00:00\"}]}, \"notes\": \"Reviewer 确认 PID 101842 在 cuda:2 正常运行中（inference 5/62, 8%），占用 9710 MiB。原误判原因：kill 旧 PID 100555 后 cron 检测旧 PID 导致 5× dead 误判。实际进程未中断。由 _r2 条目接续追踪。\"}, \"mvp2_grpo_ced_lr5e6_rp_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:04:55.831Z\", \"updated_at\": \"2026-05-14T21:40:50.174Z\", \"hypothesis\": \"D032/P0+P1 retry: lr=5e-6 + --ced_recall_penalty fixes both catastrophic forgetting (lr) and CED recall shortcut (penalty). Pass criteria: ckpt-20 rel_f1 > 0.30 AND pred_count >= 9720 (SFT 80%). Comparing vs P0 (lr5e6_r1) isolates CED shortcut fix contribution. Retry of rp_r1 which failed due to bash quoting.\", \"parent\": \"mvp2_grpo_ced_kl001_r4\", \"spec\": {\"command\": \"python -m freige.training.grpo_trainer --model_name /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_dir /root/autodl-tmp/data/docred --stage 3 --tau_start 0.3 --tau_end 0.5 --output_dir /root/autodl-tmp/grpo_ced_lr5e6_rp --num_generations 8 --reward_device cuda --per_device_batch_size 1 --gradient_accumulation_steps 16 --num_epochs 1 --learning_rate 5e-6 --seed 42 --kl_coef 0.01 --save_steps 20 --save_total_limit 20 --max_steps 200 --format_reward_weight 0.3 --f1_reward_weight 3.0 --ced_reward_weight 1.0 --num_iterations 1 --ced_recall_penalty --wandb_run_name grpo-s3-ced-lr5e6-rp-r2\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"94753\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_grpo_ced_lr5e6_rp_r2.log\", \"submitted_at\": \"2026-05-14T20:05:27.371Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 3053, \"model_name\": \"Qwen3-4B + SFT adapter\", \"seed\": 42, \"checkpoint_source\": \"N/A (training from SFT adapter)\", \"eval_data\": \"/root/autodl-tmp/data/docred/dev.json\", \"hyperparams\": {\"learning_rate\": 5e-06, \"kl_coef\": 0.01, \"num_generations\": 8, \"gradient_accumulation_steps\": 16, \"max_steps\": 200, \"save_steps\": 20, \"format_reward_weight\": 0.3, \"f1_reward_weight\": 3, \"ced_reward_weight\": 1, \"tau_start\": 0.3, \"tau_end\": 0.5, \"ced_recall_penalty\": true}, \"wall_clock_seconds\": 5716.8, \"gpu_hours\": 1.59}, \"wandb_run_id\": \"grpo-s3-ced-lr5e6-rp-r2\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T21:40:44.215Z\", \"notes\": \"Director 决策 kill: loss 持续指数 divergence (step 10: 908 → step 15: 24,650 → step 20: 1.34e7)。根因: recall penalty 产生 5-10x 更强梯度，在 QLoRA 4-bit 下加剧 KL 爆炸，kl_coef=0.01 × KL=1.42e9 = 1.42e7 完全主导 loss。训练 step 39 被 kill。ckpt-20 将用于 eval 关闭 P0+P1 对比线。\"}, \"mvp2_eval_ced_kl001_r4_multi\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:59:22.291Z\", \"updated_at\": \"2026-05-14T21:27:25.338Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -m freige.eval.batch_eval --exp_dir /root/autodl-tmp/grpo_ced_kl001 --sft_adapter /root/autodl-tmp/sft_output --output_dir /root/autodl-tmp/eval_results/grpo_ced_kl001 --checkpoints 10,20,30,40,60,70,80 --quantize --resume\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:2\"], \"pid\": \"78850\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_eval_ced_kl001_r4_multi.log\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": {\"dev\": 985}, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Multi-checkpoint eval of ced_kl001_r4 (steps 10-80) to get full reward→eval correlation and identify best checkpoint for MVP-2 judgment\", \"parent\": \"mvp2_grpo_ced_kl001_r4\", \"checkpoint_source\": \"/root/autodl-tmp/grpo_ced_kl001\", \"eval_data\": \"/root/autodl-tmp/data/docred/dev.json\"}, \"notes\": \"Director 指令: ckpt-30 评完即停。进程在 ckpt-40 推理 3% 时被 kill，非异常崩溃。已完成 6/9 个 ckpt eval: 10,20,30,50,60,90（ckpt-40 中断，ckpt-70/80 未执行）。F1 随 step 单调上升: 0.003→0.009→0.034→0.156→0.147→0.211。best=ckpt-90 (F1=0.211)。Evi-F1 稳定在 0.42-0.72，EDCR 随 step 下降（0.998→0.858）。结果路径: /root/autodl-tmp/eval_results/grpo_ced_kl001/\", \"conclusion\": \"killed\", \"reproduce\": {\"finished_at\": \"2026-05-14T21:18:34.133Z\"}, \"failure_reason\": \"进程在 ckpt-30 eval 完成后继续执行 ckpt-40，推理 3% 时被外部 kill（符合 Director 指令：ckpt-30 评完即停）。监控系统检测 5 次 dead process 后 auto-resolved as failed。非异常崩溃。\", \"completed_at\": \"2026-05-14T21:18:34.860Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T21:18:36.087981+00:00\"}]}, \"metrics\": {\"checkpoint-10\": {\"f1\": 0.003, \"ign_f1\": 0.003, \"evi_f1\": 0.72, \"edcr\": 0.9983, \"format_ok_rate\": 0.999}, \"checkpoint-20\": {\"f1\": 0.0088, \"ign_f1\": 0.0088, \"evi_f1\": 0.423, \"edcr\": 0.9954, \"format_ok_rate\": 0.999}, \"checkpoint-30\": {\"f1\": 0.0338, \"ign_f1\": 0.0338, \"evi_f1\": 0.5889, \"edcr\": 0.9798, \"format_ok_rate\": 1}, \"checkpoint-50\": {\"f1\": 0.1563, \"ign_f1\": 0.1563, \"evi_f1\": 0.5643, \"edcr\": 0.8858, \"format_ok_rate\": 0.999}, \"checkpoint-60\": {\"f1\": 0.1467, \"ign_f1\": 0.1467, \"evi_f1\": 0.5763, \"edcr\": 0.9062, \"format_ok_rate\": 1}, \"checkpoint-90\": {\"f1\": 0.2108, \"ign_f1\": 0.2108, \"evi_f1\": 0.5666, \"edcr\": 0.8584, \"format_ok_rate\": 1}}}, \"mvp2_grpo_ced_lr5e6_rp_r1\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-14T19:44:15.272Z\", \"updated_at\": \"2026-05-14T20:44:07.125Z\", \"hypothesis\": \"D032/P0+P1: lr=5e-6 + --ced_recall_penalty fixes both catastrophic forgetting (lr) and CED recall shortcut (penalty). Pass criteria: ckpt-20 rel_f1 > 0.30 AND pred_count >= 9720 (SFT 80%). Comparing vs P0 isolates CED shortcut fix contribution.\", \"parent\": \"mvp2_grpo_ced_kl001_r4\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"rtx5090-4x\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-14T19:59:16.121Z\", \"command\": \"bash -c \\\"source /etc/network_turbo && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.training.grpo_trainer --model_name /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_dir /root/autodl-tmp/data/docred --stage 3 --tau_start 0.3 --tau_end 0.5 --output_dir /root/autodl-tmp/grpo_ced_lr5e6_rp --num_generations 8 --reward_device cuda --per_device_batch_size 1 --gradient_accumulation_steps 16 --num_epochs 1 --learning_rate 5e-6 --seed 42 --kl_coef 0.01 --save_steps 20 --save_total_limit 20 --max_steps 200 --format_reward_weight 0.3 --f1_reward_weight 3.0 --ced_reward_weight 1.0 --num_iterations 1 --ced_recall_penalty --wandb_run_name grpo-s3-ced-lr5e6-rp-r1\", \"wandb_run_id\": \"grpo-s3-ced-lr5e6-rp-r1\", \"finished_at\": \"2026-05-14T20:44:01.103Z\", \"training_hours\": 0.75}, \"failure_reason\": \"EXIT_CODE=2 (shell misuse / syntax)\", \"completed_at\": \"2026-05-14T19:59:43.146Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T19:59:44.524953+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T20:44:03.547281+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"诊断结果：bash 引号不匹配（unexpected EOF while looking for matching '\\\"'），命令未到达 Python。EXIT_CODE=2。原因：submit_training_job 的 bash -c \\\"...\\\" 外层双引号与命令内部双引号冲突。--ced_recall_penalty 参数在 grpo_trainer.py:406 有定义，参数本身无问题。GPU 1/3 空闲可用。修复方案：用单引号包裹 bash -c '...' 或修复引号转义。需要以 rp_r2 重新提交。\"}}, \"notes\": \"Director D-URGENT: 与 rp_r2 冲突，同 GPU(cuda:3) 同 output_dir(/root/autodl-tmp/grpo_ced_lr5e6_rp/)。PID 94055 killed，保留 rp_r2 (PID 94758) 因其有标准化 submit_training_job 记录。\", \"spec\": {\"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"account\": \"root\", \"pid\": \"94055\", \"command\": \"bash /root/autodl-tmp/scripts/train_ced_lr5e6_rp.sh\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 3053, \"model_name\": \"Qwen3-4B + SFT adapter\", \"seed\": 42, \"checkpoint_source\": \"SFT from scratch (no GRPO checkpoint)\", \"eval_data\": \"N/A - training experiment\"}, \"conclusion\": \"failed\"}, \"mvp2_grpo_ced_lr5e6_p1_r1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T19:28:59.245Z\", \"updated_at\": \"2026-05-14T20:31:06.969Z\", \"hypothesis\": \"D031/P0+P1: lr=5e-6 + --ced_recall_penalty fixes both catastrophic forgetting (lr) and CED recall shortcut (penalty). Pass criteria: ckpt-20 rel_f1 > 0.30 AND pred_count >= 15000 (SFT 80%). Comparing vs P0 isolates CED shortcut fix contribution.\", \"spec\": {\"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"account\": \"root\"}, \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:1\", \"conclusion\": \"killed\", \"notes\": \"Superseded by mvp2_grpo_ced_lr5e6_rp_r1 per Director D032. Never submitted.\", \"completed_at\": \"2026-05-14T20:31:06.969Z\"}, \"mvp2_eval_ced_kl001_r4_step90\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:19:58.623Z\", \"updated_at\": \"2026-05-14T20:01:45.201Z\", \"hypothesis\": \"Eval true best checkpoint (step 90, reward=1.370). Critical after ckpt-50 showed reward hacking (rel_f1 -24.9pp). If step 90 also fails, CED reward design has fundamental issue.\", \"parent\": \"mvp2_grpo_ced_kl001_r4\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && ... && python -m freige.eval.batch_eval --exp_dir /root/autodl-tmp/grpo_ced_kl001 --sft_adapter /root/autodl-tmp/sft_output --output_dir /root/autodl-tmp/eval_results/grpo_ced_kl001 --checkpoints 90 --quantize\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"83207\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + SFT + GRPO ced_kl001 step-90\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/grpo_ced_kl001/checkpoint-90\", \"eval_data\": \"DocRED dev set\", \"checkpoint_path\": \"/root/autodl-tmp/grpo_ced_kl001/checkpoint-90\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_eval_ced_kl001_r4_step90.log\"}, \"notes\": \"2026-05-15 03:20 UTC: ckpt-90 inference 31/62 (50%), ~45 min remaining. Started 02:32 UTC.\", \"reproduce\": {\"finished_at\": \"2026-05-14T19:57:37.435Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T19:57:39.702949+00:00\"}]}, \"metrics\": {\"rel_f1\": 0.2108, \"ign_f1\": 0.2108, \"evi_f1\": 0.5666, \"edcr\": 0.8584, \"pred_count\": 11160, \"n_truncated\": 22, \"format_ok_rate\": 1, \"n_documents\": 985}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T20:01:45.201Z\"}, \"mvp2_eval_ced_kl001_r4_ckpt7080\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T19:50:04.595Z\", \"updated_at\": \"2026-05-14T19:58:46.631Z\", \"hypothesis\": \"Re-run failed ckpt-70/80 eval from crashed high eval (cuda:3 OOM). Completes 10-checkpoint trajectory for paper negative result analysis.\", \"parent\": \"mvp2_grpo_ced_kl001_r4\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"rtx5090-4x\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-14T19:50:27.696Z\", \"command\": \"bash -c \\\"source /etc/network_turbo && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && PYTHONUNBUFFERED=1 python -m freige.eval.batch_eval --exp_dir /root/autodl-tmp/grpo_ced_kl001 --sft_adapter /root/autodl-tmp/sft_output --output_dir /root/autodl-tmp/eval_results/grpo_ced_kl001 --checkpoints 70,80 --quantize --resume\\\"\"}, \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && PYTHONUNBUFFERED=1 python -m freige.eval.batch_eval --exp_dir /root/autodl-tmp/grpo_ced_kl001 --sft_adapter /root/autodl-tmp/sft_output --output_dir /root/autodl-tmp/eval_results/grpo_ced_kl001 --checkpoints 70,80 --quantize --resume\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"91681\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_eval_ced_kl001_r4_ckpt7080.log\", \"submitted_at\": \"2026-05-14T19:50:29.033Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 497.6, \"gpu_hours\": 0.14}, \"pid\": \"91681\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_eval_ced_kl001_r4_ckpt7080.log\", \"conclusion\": \"failed\", \"notes\": \"Process died shortly after start - likely OOM on cuda:3 (same issue as high eval crash during ckpt-70). cuda:3 may have insufficient free VRAM for eval. ckpt-70/80 will be covered by multi eval on cuda:2.\", \"completed_at\": \"2026-05-14T19:58:46.631Z\"}, \"mvp2_eval_ced_kl001_r4_high\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:19:07.637Z\", \"updated_at\": \"2026-05-14T19:47:58.282Z\", \"hypothesis\": \"High-end checkpoint eval (60,70,80,90) on cuda:3, complementing cuda:2 low-end eval. Step 90 is true best checkpoint (reward=1.370). D024 directive.\", \"parent\": \"mvp2_grpo_ced_kl001_r4\", \"spec\": {\"command\": \"python -m freige.eval.batch_eval --exp_dir /root/autodl-tmp/grpo_ced_kl001 --sft_adapter /root/autodl-tmp/sft_output --output_dir /root/autodl-tmp/eval_results/grpo_ced_kl001 --checkpoints 60,70,80,90 --quantize --resume\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"81962\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + SFT + GRPO ced_kl001\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/grpo_ced_kl001\", \"eval_data\": \"DocRED dev set\"}, \"notes\": \"1/4 checkpoints completed (ckpt-60). Process crashed during ckpt-70 inference at 8% - likely OOM or killed. cuda:3 still has 9503 MiB residual. ckpt-90 eval running separately on cuda:1 (mvp2_eval_ced_kl001_r4_step90).\", \"reproduce\": {\"finished_at\": \"2026-05-14T19:45:42.328Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T19:45:43.350Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T19:45:48.432665+00:00\"}]}, \"metrics\": {\"checkpoint_60\": {\"rel_f1\": 0.1467, \"ign_f1\": 0.1467, \"precision\": 0.1909, \"recall\": 0.1192, \"evi_f1\": 0.5763, \"edcr\": 0.9062, \"pred_count\": 10041, \"gold_count\": 12151, \"n_truncated\": 16, \"format_ok_rate\": 1}, \"note\": \"Only ckpt-60 completed. Process died during ckpt-70 inference at 8% (5/62 batch). ckpt-80/90 never started.\"}}, \"mvp2_eval_ced_kl001_r4_step100\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:08:31.821Z\", \"updated_at\": \"2026-05-14T19:41:30.318Z\", \"hypothesis\": \"Eval ced_kl001_r4 last checkpoint (step 100) to compare with best-reward checkpoint (step 50). If best ≠ last, the gap measures training stability under batch_size=1 GRPO variance.\", \"parent\": \"mvp2_grpo_ced_kl001_r4\", \"spec\": {\"command\": \"python -m freige.eval.batch_eval --exp_dir /root/autodl-tmp/grpo_ced_kl001 --sft_adapter /root/autodl-tmp/sft_output --output_dir /root/autodl-tmp/eval_results/grpo_ced_kl001_step100 --checkpoints 100 --quantize\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"80789\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_eval_ced_kl001_r4_step100.log\", \"submitted_at\": \"2026-05-14T18:09:02.064Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"model_name\": \"Qwen3-4B + SFT adapter + GRPO ced_kl001 step-100\", \"checkpoint_source\": \"/root/autodl-tmp/grpo_ced_kl001/checkpoint-100\", \"eval_data\": \"DocRED dev set\", \"data_count\": 998, \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/grpo_ced_kl001/checkpoint-100\", \"wall_clock_seconds\": 5458.4, \"gpu_hours\": 1.52}, \"notes\": \"2026-05-15 03:20 UTC: ckpt-100 inference 48/62 (77%), ~20 min remaining. Started 02:09 UTC.\", \"reproduce\": {\"finished_at\": \"2026-05-14T19:35:23.622Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T19:35:25.057156+00:00\"}]}, \"metrics\": {\"rel_f1\": 0.2167, \"ign_f1\": 0.2167, \"precision\": 0.2849, \"recall\": 0.1749, \"evi_f1\": 0.5746, \"evi_precision\": 0.5244, \"evi_recall\": 0.6353, \"edcr\": 0.8539, \"pred_count\": 7460, \"gold_count\": 12151, \"tp\": 2125, \"n_truncated\": 21, \"format_ok_rate\": 1}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T19:40:00.432Z\"}, \"mvp2_eval_ced_kl001_r4_ckpt90\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:18:13.270Z\", \"updated_at\": \"2026-05-14T19:17:36.777Z\", \"spec\": {\"command\": \"python -m freige.eval.batch_eval --exp_dir /root/autodl-tmp/grpo_ced_kl001 --checkpoints 90 --quantize\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"unknown\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_eval_ced_kl001_r4_ckpt90.log\", \"submitted_at\": \"2026-05-14T18:18:20.407Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-4B + SFT + GRPO ced_kl001 step-90\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/grpo_ced_kl001/checkpoint-90\", \"eval_data\": \"/root/autodl-tmp/data/docred/dev.json\", \"wall_clock_seconds\": 3556.4, \"gpu_hours\": 0.99}, \"hypothesis\": \"Eval ced_kl001_r4 best-reward checkpoint (step 90, reward=1.370, f1=0.720) — this is the primary MVP-2 judgment checkpoint. If evi_f1 ≥ SFT baseline (0.7979) + 2pp = 0.8179, MVP-2 passes.\", \"parent\": \"mvp2_grpo_ced_kl001_r4\", \"conclusion\": \"killed\", \"notes\": \"重复条目，被 mvp2_eval_ced_kl001_r4_step90 (cuda:1, PID 83207, 有 cron 监控) 取代。本条目无 cron、无独立进程。\", \"completed_at\": \"2026-05-14T19:17:36.777Z\"}, \"mvp2_eval_ced_kl001_r4_ckpt10\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:59:08.638Z\", \"updated_at\": \"2026-05-14T19:14:08.763Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -m freige.eval.batch_eval --exp_dir /root/autodl-tmp/grpo_ced_kl001 --sft_adapter /root/autodl-tmp/sft_output --output_dir /root/autodl-tmp/eval_results/grpo_ced_kl001 --checkpoints 10 --quantize\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:2\"], \"pid\": \"78857\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_eval_ced_kl001_r4_ckpt10.log\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": {\"dev\": 985}, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Early checkpoint eval (step 10) of ced_kl001_r4 — part of multi-checkpoint trend analysis for MVP-2 judgment\", \"parent\": \"mvp2_grpo_ced_kl001_r4\", \"checkpoint_source\": \"/root/autodl-tmp/grpo_ced_kl001/checkpoint-10\", \"eval_data\": \"/root/autodl-tmp/data/docred/dev.json\"}, \"notes\": \"Eval 完成（由 multi eval 执行）。ckpt-10 rel_f1=0.003 catastrophic — 模型几乎丧失 relation 抽取能力 (34 TP / 10839 pred)，但 evi_f1=0.72 和 edcr=0.998 反而高。GRPO 训练极早期就严重损害 relation 能力。\", \"conclusion\": \"success\", \"metrics\": {\"rel_f1\": 0.00296, \"rel_precision\": 0.00314, \"rel_recall\": 0.0028, \"evi_f1\": 0.72, \"evi_precision\": 0.6429, \"evi_recall\": 0.8182, \"edcr\": 0.9983, \"n_parseable\": 984, \"n_truncated\": 24, \"n_predictions\": 11621, \"tp\": 34, \"pred_count\": 10839, \"gold_count\": 12151, \"inference_time_seconds\": 5211.4}, \"checkpoint_path\": \"/root/autodl-tmp/eval_results/grpo_ced_kl001/checkpoint-10\", \"log_path\": \"/root/autodl-tmp/eval_results/grpo_ced_kl001/checkpoint-10/metrics.json\", \"completed_at\": \"2026-05-14T19:13:58.921Z\"}, \"mvp2_eval_ced_kl001_r4_early\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:12:53.581Z\", \"updated_at\": \"2026-05-14T18:31:18.065Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -m freige.eval.batch_eval --exp_dir /root/autodl-tmp/grpo_ced_kl001 --sft_adapter /root/autodl-tmp/sft_output --output_dir /root/autodl-tmp/eval_results/grpo_ced_kl001 --checkpoints 50 --quantize\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"75581\", \"log_path\": \"/tmp/eval_ced_kl001_ckpt50.log\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": {\"dev\": 985}, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Early eval of ced_kl001_r4 best-reward checkpoint (step 50, reward=1.1009) to get early signal on CED vs SFT baseline\", \"parent\": \"mvp2_grpo_ced_kl001_r4\", \"checkpoint_source\": \"/root/autodl-tmp/grpo_ced_kl001/checkpoint-50\", \"eval_data\": \"/root/autodl-tmp/data/docred/dev.json\"}, \"notes\": \"**Checkpoint-50 eval 完成，结果极差——MVP-2 双指标均 FAIL：**\\\\n\\\\n- rel_f1: 0.1563 vs SFT 0.4057 (Δ=-24.9pp)，远低于 -5pp 阈值\\\\n- evi_f1: 0.5643 vs SFT 0.7979 (Δ=-23.4pp)，需 +2pp 却暴跌\\\\n- EDCR: 0.8858 vs SFT 0.7118 (Δ=+17.4pp)，唯一改善项\\\\n- recall 崩塌 (0.117 vs gold 12151)，precision 也低 (0.236)\\\\n\\\\n**诊断**: training reward 上升 (1.101) 但 eval F1 崩塌，说明 GRPO 训练在优化 reward proxy 而非实际任务表现。模型学会了高 EDCR（少引用 distractor）但牺牲了大量 recall。pred_count=6032 vs gold=12151，预测数量严重不足。\\\\n\\\\n仍需等待 step-90 (reward=1.37) 的 eval 结果——如果 step-90 也崩塌，则 CED reward 设计需要根本性修改。\", \"conclusion\": \"negative\", \"metrics\": {\"f1\": 0.1563, \"ign_f1\": 0.1563, \"evi_f1\": 0.5643, \"edcr\": 0.8858, \"precision\": 0.2356, \"recall\": 0.1169, \"evi_precision\": 0.4864, \"evi_recall\": 0.6721, \"format_ok_rate\": 0.999, \"n_parseable\": 984, \"n_truncated\": 11, \"n_predictions\": 9250, \"tp\": 1421, \"pred_count\": 6032, \"gold_count\": 12151}, \"checkpoint_path\": \"/root/autodl-tmp/grpo_ced_kl001/checkpoint-50\", \"log_path\": \"/tmp/eval_ced_kl001_ckpt50.log\", \"completed_at\": \"2026-05-14T18:31:06.454Z\"}, \"mvp2_grpo_flatnli_r6\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:25:07.083Z\", \"updated_at\": \"2026-05-14T18:17:52.909Z\", \"hypothesis\": \"Flat-NLI reward with kl_coef=0.01 + num_generations=8 from SFT scratch (not resume). 100-step probe to verify stability. Same D020 config as ced_kl001_r4 (which is healthy). Tests whether flat-NLI reward type works under stable training config.\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && ... && PYTHONUNBUFFERED=1 python -m freige.training.grpo_trainer --stage 2 --kl_coef 0.01 --num_generations 8 --max_steps 100 --wandb_run_name grpo-s2-flatnli-r6\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"76958\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_grpo_flatnli_r6.log\", \"submitted_at\": \"2026-05-14T17:25:30.099Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": {\"train\": 3027, \"dev\": 985}, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"/root/autodl-tmp/data/docred/dev.json\", \"wall_clock_seconds\": 3061.0, \"gpu_hours\": 0.85}, \"parent\": \"mvp2_grpo_flatnli_r5\", \"notes\": \"D020 配置：kl_coef=0.01 + num_generations=8 + save_steps=10 + max_steps=100。从 SFT 全新训练。\\n\\n**D024 Kill — Mode Collapse Confirmed (step 25)**:\\n- frac_zero_std: 0.1→0.4→0.6→0.7→0.9 (单调上升，破 0.8 阈值)\\n- f1_reward=0, flat_nli_reward=0 — 抽取和 NLI 完全死亡\\n- reward 100% format hacking (0.293)\\n- completion_length 缩短 773→586→399\\n- KL step 5 爆炸至 1.23 亿后回落\\n\\n**科学结论**: D020 配置下 flat-NLI reward 信号不足以维持 GRPO 多样性。与 extract_r4 (step 10 collapse) 模式一致。CED 是三种 reward type 中唯一能稳定训练的。\", \"conclusion\": \"negative\", \"metrics\": {\"steps_completed\": 25, \"final_frac_zero_std\": 0.9, \"final_f1_reward\": 0, \"final_flat_nli_reward\": 0, \"final_format_reward\": 0.293, \"collapse_step\": 25}, \"checkpoint_path\": \"N/A (killed at step 25, mode collapse)\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_grpo_flatnli_r6.log\", \"completed_at\": \"2026-05-14T18:16:31.087Z\"}, \"mvp2_grpo_ced_kl001_r4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:32:32.529Z\", \"updated_at\": \"2026-05-14T18:11:53.975Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.training.grpo_trainer --model_name /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_dir /root/autodl-tmp/data/docred --stage 3 --tau_start 0.3 --tau_end 0.5 --output_dir /root/autodl-tmp/grpo_ced_kl001 --num_generations 8 --reward_device cuda --per_device_batch_size 1 --gradient_accumulation_steps 16 --num_epochs 1 --learning_rate 5e-5 --seed 42 --kl_coef 0.01 --save_steps 10 --save_total_limit 20 --max_steps 100 --format_reward_weight 0.3 --f1_reward_weight 3.0 --ced_reward_weight 1.0 --num_iterations 1 --wandb_run_name grpo-s3-ced-kl001-r4\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"68084\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_grpo_ced_kl001_r4.log\", \"submitted_at\": \"2026-05-14T15:32:32.454Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": {\"train\": 3027, \"dev\": 985}, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"kl_coef=0.01 + num_generations=8 prevents mode collapse (vs r5 kl=0/gen=4 which collapsed at step 250). 100-step probe to verify KL stability before full run.\", \"parent\": \"mvp2_grpo_ced_r5\", \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"/root/autodl-tmp/data/docred\", \"hyperparams\": {\"learning_rate\": \"5e-5\", \"kl_coef\": 0.01, \"save_steps\": 10, \"save_total_limit\": 20, \"max_steps\": 100, \"num_iterations\": 1, \"num_generations\": 8, \"format_reward_weight\": 0.3, \"f1_reward_weight\": 3, \"ced_reward_weight\": 1, \"per_device_batch_size\": 1, \"gradient_accumulation_steps\": 16, \"quantization\": \"QLoRA 4-bit NF4\", \"reward_device\": \"cuda\"}, \"wall_clock_seconds\": 9550.2, \"gpu_hours\": 2.65}, \"notes\": \"D020 配置：kl_coef=0.01 + num_generations=8 + save_steps=10 + max_steps=100 探测。✅ F1 门控已包含。\\n\\n**训练完成 (100/100 steps, EXIT_CODE=0, 2h31m)**:\\n- Final (step 100): reward=1.195, f1=0.573, ced=0.328, frac_zero_std=0.2, KL=0.118\\n- **True best: step 90** (reward=1.370, f1=0.720, ced=0.353) — 比 step 50 (1.101) 高 24%\\n- Reward trajectory: 0.22→1.37 (~5x 提升)，batch_size=1 方差大但整体上升\\n- 无 mode collapse（frac_zero_std 从早期 0.3-0.8 降至后半程 0.0-0.2）\\n- KL 稳定（0.10-0.15 range，kl_coef=0.01 控制有效）\\n- 所有 10 个 checkpoint 可用 (10-100)\\n\\n**Eval 覆盖**:\\n- cuda:1: ckpt-50 eval (mvp2_eval_ced_kl001_r4_early)\\n- cuda:2: ckpt 10-80 multi eval (mvp2_eval_ced_kl001_r4_multi)\\n- cuda:0: ckpt 90+100 eval (mvp2_eval_ced_kl001_r4_last)\", \"reproduce\": {\"finished_at\": \"2026-05-14T18:05:49.446Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T18:05:50.777825+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/grpo_ced_kl001/\", \"metrics\": {\"final_step\": 100, \"train_runtime_s\": 9069.88, \"reward_final\": 1.195, \"f1_reward_final\": 0.573, \"ced_reward_final\": 0.328, \"format_reward_final\": 0.293, \"frac_zero_std_final\": 0.2, \"kl_final\": 0.118, \"loss_final\": -0.009, \"grad_norm_final\": 0.14, \"entropy_final\": 0.067, \"completion_length_mean_final\": 520.8, \"best_reward_step\": 90, \"best_reward\": 1.37, \"best_f1_reward\": 0.72, \"best_ced_reward\": 0.353}, \"completed_at\": \"2026-05-14T18:11:42.680Z\"}, \"mvp2_grpo_extract_r4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T16:54:59.403Z\", \"updated_at\": \"2026-05-14T17:40:25.731Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && ... && python -m freige.training.grpo_trainer --stage 1 --kl_coef 0.01 --num_generations 8 --max_steps 100 ...\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:2\"], \"pid\": \"73264\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_grpo_extract_r4.log\", \"submitted_at\": \"2026-05-14T16:55:57.491Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": {\"train\": 3027, \"dev\": 985}, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"/root/autodl-tmp/data/docred\", \"wall_clock_seconds\": 2668.2, \"gpu_hours\": 0.74}, \"hypothesis\": \"Extraction-only reward (format×0.3, f1×3.0, ced=0) with kl_coef=0.01 + num_generations=8 trains stably. 100-step probe parallel ablation with ced_kl001_r4 (CED reward) to compare reward type impact under identical stability config.\", \"parent\": \"mvp2_grpo_extract_r3\", \"notes\": \"D020 配置：kl_coef=0.01 + num_generations=8 + save_steps=10 + max_steps=100 探测。与 ced_kl001_r4 (cuda:0) 构成并行 ablation——相同稳定配置、不同 reward type (extract-only vs CED)。\\n\\n**Mode collapse confirmed → KILLED at step ~30**:\\n- step 5: frac_zero_std=0.2, f1=0.016（初始信号）\\n- step 10-30: frac_zero_std=0.7-0.8, f1_reward=0（完全 collapse）\\n- reward 全部来自 format_reward (~0.29)，模型放弃 extraction\\n- 对比 ced_kl001_r4 同期在 step 20-40 恢复（frac→0.0, f1→0.240），extract_r4 无恢复信号\\n\\n**科学价值**：证明 extraction-only reward（format+f1, 无 CED）在 D020 配置下无法维持 GRPO 多样性。CED reward 通道可能是帮助 ced_kl001_r4 摆脱初期 mode collapse 的关键因素。\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T17:40:25.733Z\"}, \"mvp2_grpo_flatnli_r5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T16:55:02.197Z\", \"updated_at\": \"2026-05-14T17:26:55.692Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && ... && python -m freige.training.grpo_trainer --stage 2 --kl_coef 0.01 --num_generations 8 --max_steps 200 --resume_from_checkpoint /root/autodl-tmp/grpo_flatnli_r3/checkpoint-100 ...\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"73407\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_grpo_flatnli_r5.log\", \"submitted_at\": \"2026-05-14T16:56:01.219Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": {\"train\": 3027, \"dev\": 985}, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"/root/autodl-tmp/data/docred\", \"wall_clock_seconds\": 1854.5, \"gpu_hours\": 0.52}, \"hypothesis\": \"Flat-NLI reward with kl_coef=0.01 + num_generations=8 prevents mode collapse. Resume from flatnli_r3 checkpoint-100 (healthy). 100-step probe (steps 100→200) to verify stability before full run.\", \"parent\": \"mvp2_grpo_flatnli_r4\", \"notes\": \"Director 决策 kill：从 r3 (kl_coef=0) checkpoint-100 恢复后立即崩溃。frac_zero_std: 0.0(r3)→0.9(step 105)→0.7→0.5→0.8(step 120)，0.5-0.9 震荡无收敛。KL 全程 0.44-0.49 高位。根因：kl_coef=0 累积的 policy 漂移 + kl_coef=0.01 penalty 形成对抗。教训：不能从 kl_coef=0 的 checkpoint 恢复加 KL penalty。flatnli_r6 从 SFT 全新训练。\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T17:26:55.692Z\"}, \"mvp2_sft_eval_r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:52:38.174Z\", \"updated_at\": \"2026-05-14T17:06:57.010Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.eval.inference --model_path /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --quantize --output_dir /root/autodl-tmp/sft_eval_r3_results --seed 42\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"62352\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_sft_eval_r3.log\", \"submitted_at\": \"2026-05-14T14:53:52.360Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": {\"dev\": 985}, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"SFT baseline eval with unified eval code (consolidated parse_model_output) for fair comparison with r2\", \"parent\": \"mvp2_sft_warmup\", \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"/root/autodl-tmp/data/docred/dev.json\", \"wall_clock_seconds\": 7718.1, \"gpu_hours\": 2.14}, \"reproduce\": {\"finished_at\": \"2026-05-14T16:42:11.014Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T16:42:12.047698+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"rel_f1\": 0.4057, \"ign_f1\": 0.4057, \"evi_f1\": 0.7979, \"edcr\": 0.7118, \"precision\": 0.4043, \"recall\": 0.407, \"evi_precision\": 0.8035, \"evi_recall\": 0.7924, \"format_ok_rate\": 0.998, \"format_compliance_rate\": 0.626, \"n_parseable\": 617, \"n_truncated\": 367, \"n_predictions\": 18815}, \"checkpoint_path\": \"/root/autodl-tmp/sft_eval_r3_results/\", \"completed_at\": \"2026-05-14T17:02:30.442Z\", \"notes\": \"统一 eval 代码验证：r3 与 r2 所有指标完全一致（差异=0.00pp），含 _repair_truncated_json 的统一 eval 脚本未引入任何偏差。SFT baseline 可靠确认：rel_f1=0.4057, evi_f1=0.7979, edcr=0.7118。983 parseable / 617 field_complete / 367 truncated / 18815 predictions。\"}, \"mvp2_grpo_extract_r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:31:48.781Z\", \"updated_at\": \"2026-05-14T16:59:20.304Z\", \"spec\": {\"command\": \"python -m freige.training.grpo_trainer --stage 1 --kl_coef 0.0 --num_iterations 1 --save_steps 20 --format_reward_weight 0.3 --f1_reward_weight 3.0 --ced_reward_weight 0.0 --lr 5e-5 --gradient_accumulation_steps 16 --num_generations 4\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:2\"], \"pid\": \"53149\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_grpo_extract_r3.log\", \"submitted_at\": \"2026-05-14T12:31:48.738Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": {\"train\": 3027, \"dev\": 985}, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Extraction-only reward (format×0.3, f1×3.0, ced=0) with kl_coef=0 establishes stable GRPO baseline\", \"parent\": \"mvp2_grpo_extract\", \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"/root/autodl-tmp/data/docred\", \"hyperparams\": {\"learning_rate\": \"5e-5\", \"kl_coef\": 0, \"save_steps\": 20, \"num_iterations\": 1, \"format_reward_weight\": 0.3, \"f1_reward_weight\": 3, \"ced_reward_weight\": 0, \"per_device_batch_size\": 1, \"gradient_accumulation_steps\": 16, \"num_generations\": 4, \"quantization\": \"QLoRA 4-bit NF4\"}, \"wall_clock_seconds\": 12041.2, \"gpu_hours\": 3.34}, \"notes\": \"Negative result (756/756 steps completed). 两阶段行为：(1) step 1-520 f1_reward 在 0.02-0.49 波动，completion length ~43 tokens 稳定，看似健康；(2) 实际最后 100+ 步 grad_norm=0, frac_reward_zero_std=1.0, loss=0.0, entropy≈0.005。f1 波动是 SFT 初始化残留，非 GRPO 学习。停滞机制：kl_coef=0 + num_generations=4 → 4 个相同输出 → reward_std=0 → GRPO advantage=0 → 梯度为零。与 ced_r5 的差异：无 CED reward 通道，模型没 drift 到短输出（保持在 SFT 水平），但也完全停止学习。科学价值：证明 num_generations=4 不足以维持 GRPO 多样性，kl_coef=0 下 extraction-only 停滞而 CED collapse 更严重。\", \"reproduce\": {\"finished_at\": \"2026-05-14T15:52:29.058Z\"}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T15:52:29.969Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T15:52:31.006940+00:00\"}]}}, \"mvp2_grpo_flatnli_r4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:32:31.804Z\", \"updated_at\": \"2026-05-14T16:56:12.080Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -m freige.training.grpo_trainer --stage 2 --reward_device cuda --resume_from_checkpoint /root/autodl-tmp/grpo_flatnli_r3/checkpoint-100 --save_total_limit 40 --wandb_run_name grpo-s2-flatnli-r4\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"67050\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_grpo_flatnli_r4.log\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": {\"train\": 3027, \"dev\": 985}, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"resume_from\": \"/root/autodl-tmp/grpo_flatnli_r3/checkpoint-100\", \"hyperparams\": {\"learning_rate\": \"5e-5\", \"kl_coef\": 0, \"num_iterations\": 1, \"format_reward_weight\": 0.3, \"f1_reward_weight\": 3, \"ced_reward_weight\": 1, \"per_device_batch_size\": 1, \"gradient_accumulation_steps\": 16, \"num_generations\": 4, \"reward_device\": \"cuda\", \"quantization\": \"QLoRA 4-bit NF4\"}}, \"pid\": 67050, \"notes\": \"Director 指令 kill: kl=0+gen=4 配置已在 ced_r5/extract_r3/flatnli_r3 三个实验崩塌，统一切到 kl=0.01+gen=8。flatnli_r4 运行 step 104→~130（~30 min），step_time ~34s/step。用 flatnli_r5 从 checkpoint-100 重启。\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T16:54:43.884Z\"}, \"mvp2_grpo_ced_kl001\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:32:53.111Z\", \"updated_at\": \"2026-05-14T15:33:06.208Z\", \"spec\": {\"command\": \"python -m freige.training.grpo_trainer --stage 3 --kl_coef 0.01 --num_iterations 1 --save_steps 20 --save_total_limit 20 --format_reward_weight 0.3 --f1_reward_weight 3.0 --ced_reward_weight 1.0 --lr 5e-5 --gradient_accumulation_steps 16 --num_generations 4\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"64981\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_grpo_ced_kl001.log\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": {\"train\": 3027, \"dev\": 985}, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"kl_coef=0.01 (vs r5 kl_coef=0.0) prevents CED mode collapse while keeping QLoRA 4-bit compatible — answers whether KL regularization is necessary\", \"parent\": \"mvp2_grpo_ced_r5\", \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"/root/autodl-tmp/data/docred\", \"hyperparams\": {\"learning_rate\": \"5e-5\", \"kl_coef\": 0.01, \"save_steps\": 20, \"save_total_limit\": 20, \"num_iterations\": 1, \"format_reward_weight\": 0.3, \"f1_reward_weight\": 3, \"ced_reward_weight\": 1, \"per_device_batch_size\": 1, \"gradient_accumulation_steps\": 16, \"num_generations\": 4, \"quantization\": \"QLoRA 4-bit NF4\"}}, \"notes\": \"三次失败：r1 --lr 不识别 (EXIT_CODE=2)，r2 conda 未激活 python not found (EXIT_CODE=127)，r3 缺 --data_dir。已在 r4 修正所有问题。\", \"hypothesis\": \"kl_coef=0.01 (vs r5 kl_coef=0.0) prevents CED mode collapse while keeping QLoRA 4-bit compatible — answers whether KL regularization is necessary\", \"reproduce\": {\"finished_at\": \"2026-05-14T15:20:19.022Z\"}, \"failure_reason\": \"EXIT_CODE=2 (shell misuse / syntax)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T15:20:19.862Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T15:20:20.950140+00:00\"}]}}, \"mvp2_grpo_ced_r5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:31:45.606Z\", \"updated_at\": \"2026-05-14T15:32:21.817Z\", \"spec\": {\"command\": \"python -m freige.training.grpo_trainer --stage 3 --kl_coef 0.0 --num_iterations 1 --save_steps 20 --format_reward_weight 0.3 --f1_reward_weight 3.0 --ced_reward_weight 1.0 --lr 5e-5 --gradient_accumulation_steps 16 --num_generations 4\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"53071\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_grpo_ced_r5.log\", \"submitted_at\": \"2026-05-14T12:31:45.554Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": {\"train\": 3027, \"dev\": 985}, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"CED reward (format×0.3, f1×3.0, ced×1.0) with kl_coef=0 trains stably and improves Evi-F1 over SFT baseline\", \"parent\": \"mvp2_grpo_ced_r4\", \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"/root/autodl-tmp/data/docred\", \"hyperparams\": {\"learning_rate\": \"5e-5\", \"kl_coef\": 0, \"save_steps\": 20, \"num_iterations\": 1, \"format_reward_weight\": 0.3, \"f1_reward_weight\": 3, \"ced_reward_weight\": 1, \"per_device_batch_size\": 1, \"gradient_accumulation_steps\": 16, \"num_generations\": 4, \"quantization\": \"QLoRA 4-bit NF4\"}, \"wall_clock_seconds\": 9887.5, \"gpu_hours\": 2.75}, \"notes\": \"⚠️ Mode collapse confirmed: step 250+ f1_reward=0, completion length collapsed to fixed 34 tokens, frac_reward_zero_std=0.9-1.0. Model learned to produce short fixed-format output maximizing ced_reward (0.99) + format_reward (0.3) while abandoning relation extraction (f1=0). Early checkpoints (pre-collapse) lost due to save_total_limit=5 — only steps 400-480 remain, all post-collapse. Current checkpoints likely unusable for eval.\", \"conclusion\": \"negative\", \"checkpoint_path\": \"N/A (all checkpoints post-collapse, unusable)\", \"completed_at\": \"2026-05-14T15:29:18.460Z\"}, \"mvp2_grpo_flatnli_r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:31:52.782Z\", \"updated_at\": \"2026-05-14T15:27:55.267Z\", \"spec\": {\"command\": \"python -m freige.training.grpo_trainer --stage 2 --kl_coef 0.0 --num_iterations 1 --save_steps 20 --format_reward_weight 0.3 --f1_reward_weight 3.0 --ced_reward_weight 1.0 --lr 5e-5 --gradient_accumulation_steps 16 --num_generations 4\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"53292\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_grpo_flatnli_r3.log\", \"submitted_at\": \"2026-05-14T12:31:52.703Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": {\"train\": 3027, \"dev\": 985}, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Flat-NLI reward (format×0.3, f1×3.0, ced×1.0) with kl_coef=0 validates non-contrastive evidence baseline\", \"parent\": \"mvp2_grpo_flatnli\", \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"/root/autodl-tmp/data/docred\", \"hyperparams\": {\"learning_rate\": \"5e-5\", \"kl_coef\": 0, \"save_steps\": 20, \"num_iterations\": 1, \"format_reward_weight\": 0.3, \"f1_reward_weight\": 3, \"ced_reward_weight\": 1, \"per_device_batch_size\": 1, \"gradient_accumulation_steps\": 16, \"num_generations\": 4, \"quantization\": \"QLoRA 4-bit NF4\"}, \"wall_clock_seconds\": 9527.7, \"gpu_hours\": 2.65, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_backup/flatnli_r3_healthy/\"}, \"notes\": \"Director 指令 kill：NLI 推理在 CPU 导致 10x 减速（~100-125s/step vs 应有 ~12s/step）。训练本身健康——step 104/756, grad_norm=0.37, f1 从 step 84 起出现, flat_nli_reward=0.52, entropy=0.046。Checkpoint 已备份。修复 --reward_device cuda 后以 flatnli_r4 重启。\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T15:27:48.503Z\"}, \"mvp2_sft_eval_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:45:46.160Z\", \"updated_at\": \"2026-05-14T14:54:07.338Z\", \"spec\": {\"command\": \"python -m freige.eval.inference --model_path /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --quantize --output_dir /root/autodl-tmp/sft_eval_results --seed 42\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"55410\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_sft_eval_r2.log\", \"submitted_at\": \"2026-05-14T12:45:45.981Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": {\"dev\": 985}, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"SFT baseline eval on DocRED dev set (batch_size=16 accelerated)\", \"parent\": \"mvp2_sft_warmup\", \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"/root/autodl-tmp/data/docred/dev.json\", \"wall_clock_seconds\": 7701.4, \"gpu_hours\": 2.14}, \"reproduce\": {\"finished_at\": \"2026-05-14T14:52:20.498Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T14:52:21.560816+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"rel_f1\": 0.4057, \"ign_f1\": 0.4057, \"evi_f1\": 0.7979, \"edcr\": 0.7118, \"precision\": 0.4043, \"recall\": 0.407, \"evi_precision\": 0.8035, \"evi_recall\": 0.7924, \"format_ok_rate\": 0.998, \"format_compliance_rate\": 0.626, \"n_parseable\": 617, \"n_truncated\": 367, \"n_predictions\": 18815, \"inference_time_seconds\": 6484.7}, \"checkpoint_path\": \"/root/autodl-tmp/sft_eval_results/\", \"completed_at\": \"2026-05-14T14:54:07.338Z\"}, \"mvp2_sft_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:10:37.449Z\", \"updated_at\": \"2026-05-14T12:46:04.523Z\", \"spec\": {\"command\": \"python -m freige.eval.inference --model_path sft_output --base_model Qwen3-4B --split dev\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"47293\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_sft_eval.log\", \"submitted_at\": \"2026-05-14T11:48:46.335Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": {\"dev\": 985}, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"SFT baseline eval on DocRED dev set\", \"parent\": \"mvp2_sft_warmup\", \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"/root/autodl-tmp/data/docred/dev.json\", \"wall_clock_seconds\": 3416.3, \"gpu_hours\": 0.95}, \"conclusion\": \"killed\", \"reproduce\": {\"finished_at\": \"2026-05-14T12:45:42.027Z\"}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"completed_at\": \"2026-05-14T12:45:42.659Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T12:45:43.534491+00:00\"}]}, \"notes\": \"Killed intentionally to restart with batch_size=16 (was batch_size=4, ~6h → ~1.5h). Director approved.\"}, \"mvp2_grpo_flatnli_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:10:23.287Z\", \"updated_at\": \"2026-05-14T12:30:08.865Z\", \"spec\": {\"command\": \"python -m freige.training.grpo_trainer --stage 2 --kl_coef 0.0 --num_iterations 1 --save_steps 20 --format_reward_weight 0.3 --f1_reward_weight 3.0 --ced_reward_weight 1.0 --lr 5e-5 --gradient_accumulation_steps 16 --num_generations 4\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"50941\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_grpo_flatnli_r2.log\", \"submitted_at\": \"2026-05-14T12:10:23.256Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": {\"train\": 3027, \"dev\": 985}, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Flat-NLI reward (format×0.3, f1×3.0, ced×1.0) with kl_coef=0 validates non-contrastive evidence baseline\", \"parent\": \"mvp2_grpo_flatnli\", \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"/root/autodl-tmp/data/docred\", \"hyperparams\": {\"learning_rate\": \"5e-5\", \"kl_coef\": 0, \"save_steps\": 20, \"num_iterations\": 1, \"format_reward_weight\": 0.3, \"f1_reward_weight\": 3, \"ced_reward_weight\": 1, \"per_device_batch_size\": 1, \"gradient_accumulation_steps\": 16, \"num_generations\": 4, \"quantization\": \"QLoRA 4-bit NF4\"}, \"wall_clock_seconds\": 1174.2, \"gpu_hours\": 0.33}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T12:29:57.408Z\", \"notes\": \"Killed: Director 指令暂不提交 r2，等原始 flatnli 分析完再决定配置。\"}, \"mvp2_grpo_extract_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:10:19.532Z\", \"updated_at\": \"2026-05-14T12:30:08.099Z\", \"spec\": {\"command\": \"python -m freige.training.grpo_trainer --stage 1 --kl_coef 0.0 --num_iterations 1 --save_steps 20 --format_reward_weight 0.3 --f1_reward_weight 3.0 --ced_reward_weight 0.0 --lr 5e-5 --gradient_accumulation_steps 16 --num_generations 4\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:2\"], \"pid\": \"50670\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_grpo_extract_r2.log\", \"submitted_at\": \"2026-05-14T12:10:19.491Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": {\"train\": 3027, \"dev\": 985}, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Extraction-only reward (format×0.3, f1×3.0, ced=0) with kl_coef=0 establishes stable GRPO baseline\", \"parent\": \"mvp2_grpo_extract\", \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"/root/autodl-tmp/data/docred\", \"hyperparams\": {\"learning_rate\": \"5e-5\", \"kl_coef\": 0, \"save_steps\": 20, \"num_iterations\": 1, \"format_reward_weight\": 0.3, \"f1_reward_weight\": 3, \"ced_reward_weight\": 0, \"per_device_batch_size\": 1, \"gradient_accumulation_steps\": 16, \"num_generations\": 4, \"quantization\": \"QLoRA 4-bit NF4\"}, \"wall_clock_seconds\": 1166.7, \"gpu_hours\": 0.32}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T12:29:46.151Z\", \"notes\": \"Killed: Director 指令暂不提交 r2，等原始 extract 分析完再决定配置。\"}, \"mvp2_grpo_ced_r4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:10:15.698Z\", \"updated_at\": \"2026-05-14T12:30:06.177Z\", \"spec\": {\"command\": \"python -m freige.training.grpo_trainer --stage 3 --kl_coef 0.0 --num_iterations 1 --save_steps 20 --format_reward_weight 0.3 --f1_reward_weight 3.0 --ced_reward_weight 1.0 --lr 5e-5 --gradient_accumulation_steps 16 --num_generations 4\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"50529\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_grpo_ced_r4.log\", \"submitted_at\": \"2026-05-14T12:10:15.624Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": {\"train\": 3027, \"dev\": 985}, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"CED reward (format×0.3, f1×3.0, ced×1.0) with kl_coef=0 (D008 fix) achieves Evi-F1 improvement over SFT baseline\", \"parent\": \"mvp2_grpo_ced_r3\", \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"/root/autodl-tmp/data/docred\", \"hyperparams\": {\"learning_rate\": \"5e-5\", \"kl_coef\": 0, \"save_steps\": 20, \"num_iterations\": 1, \"format_reward_weight\": 0.3, \"f1_reward_weight\": 3, \"ced_reward_weight\": 1, \"per_device_batch_size\": 1, \"gradient_accumulation_steps\": 16, \"num_generations\": 4, \"quantization\": \"QLoRA 4-bit NF4\"}, \"wall_clock_seconds\": 1169.5, \"gpu_hours\": 0.32}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T12:29:45.113Z\", \"notes\": \"Killed: 上一 session 使用 kl_coef=0.0/lr=5e-5 启动，但 Director 要求 D009 配置 (kl_coef=0.5, lr=5e-6, warmup_steps=200)。需等 extract/flatnli 分析完再用正确配置重新提交。\"}, \"mvp2_grpo_extract\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:10:35.796Z\", \"updated_at\": \"2026-05-14T12:25:32.094Z\", \"spec\": {\"command\": \"python -m freige.training.grpo_trainer --stage 1 --ced_reward_weight 0.0 --format_reward_weight 0.3 --f1_reward_weight 3.0 --num_iterations 1 --kl_coef 0.05 --lr 5e-5\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:2\"], \"pid\": \"47561\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_grpo_extract.log\", \"submitted_at\": \"2026-05-14T11:48:50.108Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred/train_annotated.json\", \"data_count\": 3027, \"model_name\": \"Qwen3-4B (QLoRA from SFT warmup)\", \"seed\": 42, \"hypothesis\": \"Extraction-only reward (format+F1, no CED) establishes GRPO baseline\", \"parent\": \"mvp2_sft_warmup\", \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"/root/autodl-tmp/data/docred\", \"hyperparams\": {\"learning_rate\": \"5e-5\", \"kl_coef\": 0.05, \"num_iterations\": 1, \"format_reward_weight\": 0.3, \"f1_reward_weight\": 3, \"ced_reward_weight\": 0}, \"wall_clock_seconds\": 1479.2, \"gpu_hours\": 0.41}, \"hypothesis\": \"Extraction-only reward (format+F1, no CED) establishes GRPO baseline — CED r3 should exceed this on Evi-F1\", \"reproduce\": {\"finished_at\": \"2026-05-14T12:03:50.563Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T12:03:51.381207+00:00\"}]}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T12:13:29.284Z\", \"notes\": \"KL divergence explosion at step 5 due to kl_coef=0.05 + QLoRA 4-bit incompatibility (D008). QLoRA quantization noise makes ref/policy log-prob divergence unreliable, causing KL values to reach 10^8-10^11. Same root cause as r3 and flatnli. Fix: kl_coef=0.0 in r2 retries.\"}, \"mvp2_grpo_flatnli\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:10:33.848Z\", \"updated_at\": \"2026-05-14T12:13:34.747Z\", \"spec\": {\"command\": \"python -m freige.training.grpo_trainer --stage 2 --ced_reward_weight 1.0 --format_reward_weight 0.3 --f1_reward_weight 3.0 --num_iterations 1 --kl_coef 0.05 --lr 5e-5\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:3\"], \"pid\": \"47722\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_grpo_flatnli.log\", \"submitted_at\": \"2026-05-14T11:48:54.086Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": {\"train\": 3027, \"dev\": 985}, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Flat-NLI reward improves Evi-F1 over extraction-only but less than CED\", \"parent\": \"mvp2_sft_warmup\", \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"/root/autodl-tmp/data/docred\", \"hyperparams\": {\"learning_rate\": \"5e-5\", \"kl_coef\": 0.05, \"num_iterations\": 1, \"format_reward_weight\": 0.3, \"f1_reward_weight\": 3, \"ced_reward_weight\": 1}, \"wall_clock_seconds\": 1188.0, \"gpu_hours\": 0.33}, \"hypothesis\": \"Flat-NLI reward (non-contrastive) improves Evi-F1 over extraction-only but less than CED — validates contrastive component's incremental value\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T12:08:42.058Z\", \"notes\": \"KL divergence explosion at step 5 due to kl_coef=0.05 + QLoRA 4-bit incompatibility (D008). QLoRA quantization noise makes ref/policy log-prob divergence unreliable. Same root cause as r3 and extract. Fix: kl_coef=0.0 in r2 retries.\"}, \"mvp2_grpo_ced_r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:47:53.099Z\", \"updated_at\": \"2026-05-14T12:09:23.005Z\", \"spec\": {\"command\": \"python -m freige.training.grpo_trainer --stage 3 --num_iterations 1 --kl_coef 0.05 --save_steps 20 --format_reward_weight 0.3 --f1_reward_weight 3.0 --ced_reward_weight 1.0 --max_kl 100 --lr 5e-5\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"47136\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_grpo_ced_r3.log\", \"submitted_at\": \"2026-05-14T11:48:42.598Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": {\"train\": 3027, \"dev\": 985}, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Reward weighting (format×0.3, f1×3.0, ced×1.0) with stable training (num_iterations=1, KL early stop) improves Evi-F1\", \"parent\": \"mvp2_grpo_ced_r1\", \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"/root/autodl-tmp/data/docred\", \"hyperparams\": {\"learning_rate\": \"5e-5\", \"kl_coef\": 0.05, \"save_steps\": 20, \"num_iterations\": 1, \"format_reward_weight\": 0.3, \"f1_reward_weight\": 3, \"ced_reward_weight\": 1, \"max_kl\": 100}, \"wall_clock_seconds\": 1061.5, \"gpu_hours\": 0.29}, \"hypothesis\": \"CED reward with balanced weights (format×0.3, f1×3.0, ced×1.0) + stable training (num_iterations=1, KL early stop at 100) + kl_coef=0.05 improves Evi-F1 over SFT baseline\", \"reproduce\": {\"finished_at\": \"2026-05-14T12:06:23.600Z\"}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T12:06:24.147Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T12:06:25.189118+00:00\"}]}, \"notes\": \"KL divergence explosion at step 5: first pass KL=4.4M, second pass KL=69.5B (threshold=100). KL early stopping correctly triggered, model saved but no useful training occurred.\\n\\nRoot cause: single-GPU training without --gradient_accumulation_steps (effective batch=1) → extremely noisy gradients → policy diverged from reference in 5 steps. Combined with QLoRA merge rounding amplifying initial policy-reference gap.\\n\\nKey metrics at step 5: loss=269987, kl=4.4M, entropy=0.084 (near 0), format_reward=0.10, f1_reward=0.05, ced_reward=0.15, grad_norm=0.16. EXIT_CODE=129 is artifact of KL early stop exit path.\\n\\nerror_type: hyperparameter | can_auto_fix: false\\nFix options: (1) add --gradient_accumulation_steps 16 for effective batch ~16; (2) reduce lr from 5e-5 to 5e-6; (3) increase kl_coef from 0.05 to 0.5; (4) lr warmup steps\"}, \"mvp2_grpo_ced_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T10:58:11.663Z\", \"updated_at\": \"2026-05-14T11:31:49.724Z\", \"spec\": {\"command\": \"accelerate launch --config_file freige/configs/accelerate_4gpu.yaml -m freige.training.grpo_trainer --model_name Qwen3-4B --learning_rate 2e-5 --kl_coef 0.05 --save_steps 20 --format_reward_weight 0.3 --f1_reward_weight 3.0 --ced_reward_weight 1.0 --num_iterations 2\", \"server\": \"rtx5090-4x\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": {\"train\": 3027, \"dev\": 985}, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"CED reward with balanced weights (format×0.3, f1×3.0, ced×1.0) + KL=0.05 + save_steps=20 + num_iterations=2 prevents mode collapse and improves Evi-F1\", \"parent\": \"mvp2_grpo_ced_r1\", \"hyperparams\": {\"learning_rate\": \"2e-5\", \"kl_coef\": 0.05, \"save_steps\": 20, \"num_iterations\": 2, \"format_reward_weight\": 0.3, \"f1_reward_weight\": 3, \"ced_reward_weight\": 1, \"per_device_batch_size\": 1, \"gradient_accumulation_steps\": 16, \"num_generations\": 4}}, \"reproduce\": {\"finished_at\": \"2026-05-14T11:26:47.993Z\"}, \"failure_reason\": \"EXIT_CODE=137 (SIGKILL — OOM killer or manual kill)\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T11:26:48.502Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T11:26:49.285684+00:00\"}]}}, \"mvp2_grpo_ced_r1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:02:41.858Z\", \"updated_at\": \"2026-05-14T10:37:23.856Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && accelerate launch --config_file freige/configs/accelerate_4gpu.yaml -m freige.training.grpo_trainer --model_name /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_dir /root/autodl-tmp/data/docred --stage 3 --tau_start 0.3 --tau_end 0.5 --output_dir /root/autodl-tmp/grpo_s3 --num_generations 4 --reward_device cpu --per_device_batch_size 1 --gradient_accumulation_steps 16 --num_epochs 1 --learning_rate 5e-5 --seed 42 --wandb_run_name grpo-s3-ced-r1\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\", \"cuda:1\", \"cuda:2\", \"cuda:3\"], \"pid\": \"24122\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_grpo_ced_r1.log\", \"submitted_at\": \"2026-05-14T08:02:41.839Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": {\"train\": 3027, \"dev\": 985}, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"CED reward improves Evi-F1 over flat-NLI and extraction-only baselines\", \"wall_clock_seconds\": 8641.6, \"gpu_hours\": 9.6}, \"conclusion\": \"killed\", \"notes\": \"Mode collapse diagnosed at step 80/189 (F1=0.001, format reward hacking). Root causes and fixes applied to grpo_trainer.py:\\n\\n(A) Checkpoint: save_strategy was \\\"epoch\\\" → now supports --save_steps/--save_total_limit CLI args, defaults to steps-based saving. Validated: checkpoint-1/2 saved in dry-run.\\n\\n(B) Reward weighting: all 3 rewards (format/f1/ced) were equally summed by TRL → added WeightedRewardFn wrapper + --format_reward_weight/--f1_reward_weight/--ced_reward_weight CLI args. Dry-run confirmed weighting works (format raw=0.1 × w=0.3 → 0.03).\\n\\n(C) Clip ratio: num_iterations=1 (default) meant single pass, ratio≡1, clipping never activated → added --num_iterations CLI arg (set to 2 in r2). Also added --max_steps, --kl_coef (beta). Dry-run clip_ratio=0 expected (zero reward variance → zero advantage → no update needed).\\n\\n(D) Added --save_total_limit CLI arg (previously hardcoded to 2, now configurable).\\n\\nDry-run validated: 2 steps completed, checkpoints saved, no OOM with num_iterations=2 on 4xRTX5090. completions/clipped_ratio=1.0 (all hit max_completion_length=1024) — expected for cold-start without warmup.\", \"completed_at\": \"2026-05-14T10:26:43.488Z\"}, \"mvp2_grpo_ced\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:10:31.165Z\", \"updated_at\": \"2026-05-14T08:00:02.874Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && accelerate launch --config_file freige/configs/accelerate_4gpu.yaml -m freige.training.grpo_trainer --model_name /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_dir /root/autodl-tmp/data/docred --stage 3 --tau_start 0.3 --tau_end 0.5 --output_dir /root/autodl-tmp/grpo_s3 --num_generations 4 --reward_device cpu --per_device_batch_size 1 --gradient_accumulation_steps 16 --num_epochs 1 --learning_rate 5e-5 --seed 42 --wandb_run_name grpo-s3-ced\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\", \"cuda:1\", \"cuda:2\", \"cuda:3\"], \"pid\": \"20973\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_grpo_ced.log\", \"submitted_at\": \"2026-05-14T07:19:59.045Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 2189.9, \"gpu_hours\": 2.43}, \"reproduce\": {\"finished_at\": \"2026-05-14T07:56:28.316Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T07:56:28.916Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T07:56:29.797308+00:00\"}]}, \"notes\": \"失败原因: grpo_trainer.py:109 f1_reward_fn 中 p.get(\\\"tail\\\", \\\"\\\").lower() 报 AttributeError: 'NoneType' — 某些 parsed triple 的 \\\"tail\\\" 字段为 None，dict.get 有 key 时不返回 default | 运行 ~36min 后崩溃 | 修复方案: 用 (p.get(\\\"tail\\\") or \\\"\\\") 模式处理 None | error_type: infrastructure | can_auto_fix: true\"}, \"precompute_nli_train\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:05:48.887Z\", \"updated_at\": \"2026-05-14T07:35:24.549Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python precompute_nli.py\\\"\", \"server\": \"gpu-5090-4x-1\", \"gpu\": [\"cuda:0\"], \"pid\": \"19212\", \"log_path\": \"~/runs/faith-evidence-ie/precompute_nli_train.log\", \"submitted_at\": \"2026-05-14T07:05:58.458Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/nli_cache/\", \"wall_clock_seconds\": 1766.1, \"gpu_hours\": 0.49}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T07:35:24.549Z\"}, \"mvp2_sft_warmup\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T06:09:47.819Z\", \"updated_at\": \"2026-05-14T07:10:19.285Z\", \"spec\": {\"command\": \"accelerate launch --config_file freige/configs/accelerate_4gpu.yaml -m freige.training.sft_trainer --model_name /root/autodl-tmp/models/Qwen3-4B --data_dir /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/sft_output --deepspeed freige/configs/deepspeed_zero2.json --num_epochs 3 --per_device_batch_size 1 --gradient_accumulation_steps 16 --learning_rate 2e-4 --max_length 4096 --seed 42\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\", \"cuda:1\", \"cuda:2\", \"cuda:3\"], \"pid\": \"16221\", \"log_path\": \"~/runs/faith-evidence-ie/mvp2_sft_warmup.log\", \"submitted_at\": \"2026-05-14T06:22:10.453Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": {\"train\": 3027, \"dev\": 985}, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"gpu_model\": \"RTX 5090 32GB x4\", \"lora_rank\": 64, \"lora_alpha\": 128, \"quantization\": \"4-bit NF4 QLoRA\", \"deepspeed\": \"ZeRO-2 + CPU offload\", \"effective_batch_size\": 64, \"checkpoint_path\": \"/root/autodl-tmp/sft_output\", \"wall_clock_seconds\": 2888.8, \"gpu_hours\": 3.21}, \"conclusion\": \"success\", \"metrics\": {\"eval_loss\": 0.72, \"accuracy\": 0.835}, \"completed_at\": \"2026-05-14T07:10:19.285Z\"}, \"smoke_test_grpo\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:20:00.970Z\", \"updated_at\": \"2026-05-14T06:09:18.626Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && accelerate launch --num_processes 4 --mixed_precision bf16 -m freige.training.smoke_test\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\", \"cuda:1\", \"cuda:2\", \"cuda:3\"], \"pid\": \"9823\", \"log_path\": \"~/runs/faith-evidence-ie/smoke_test_grpo.log\", \"submitted_at\": \"2026-05-14T05:54:45.178Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (smoke test)\", \"wall_clock_seconds\": 873.4, \"gpu_hours\": 0.97}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T06:09:18.626Z\"}, \"mvp1_ced_signal\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T04:48:46.220Z\", \"updated_at\": \"2026-05-14T05:48:05.545Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES='' python -m freige.analysis.ced_signal_validation --data_dir /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/mvp1_results --split dev --nli_model cross-encoder/nli-deberta-v3-base --tau 0.5 --batch_size 32\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"4491\", \"log_path\": \"~/runs/faith-evidence-ie/mvp1_ced_signal.log\", \"submitted_at\": \"2026-05-14T05:21:30.878Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_count\": 6830, \"model_name\": \"cross-encoder/nli-deberta-v3-base\", \"data_path\": \"/root/autodl-tmp/data/docred/\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/mvp1_results/\", \"wall_clock_seconds\": 1594.7, \"gpu_hours\": 0.44}, \"conclusion\": \"success\", \"metrics\": {\"mean_margin\": 0.48, \"discrimination_accuracy\": 0.815, \"pearson_r_margin_jaccard\": 0.34, \"pass\": true}, \"completed_at\": \"2026-05-14T05:48:05.545Z\"}}, \"count\": 222, \"total\": 222, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.6518}}"
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
The registry data is too large. Let me use a subagent to parse it and extract the 4B-related experiments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "b7a3d7bf-bc37-49ab-8f52-615aac99dee6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VUdQC1qLX54kQBJCaNtkrT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 613,
      "cache_read_input_tokens": 26191,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 613
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

Registry 数据量大，用 subagent 解析筛选 4B 相关实验。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "41c49af5-40ca-42c5-902d-00debc8e5641",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VUdQC1qLX54kQBJCaNtkrT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 613,
      "cache_read_input_tokens": 26191,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 613
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

<details open><summary>🔧 Tool call — Agent · `toolu_01GK9KaSv83WhaAJmvpUVdYs`</summary>

```json
{
  "description": "Parse 4B eval experiments from registry",
  "prompt": "I need you to analyze a large JSON registry file and extract all 4B-related experiments (especially eval experiments).\n\nThe file is at: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/596d8411-63f5-4757-a2a4-2c57b1fcaba0/tool-results/mcp-agent-ml-research-read_registry-1779141732674.txt\n\nIt's JSON with schema: {result: string} where result is a JSON string that needs to be parsed.\n\nSteps:\n1. First probe the structure with jq (type, length, keys)\n2. Parse the nested JSON (result is a JSON string containing the actual data)\n3. Filter for ALL experiments that match ANY of these criteria:\n   - exp_id contains \"4b\" or \"4B\" (case insensitive)\n   - exp_id contains \"wave1_sft\" \n   - exp_id contains \"rsft_ced\" or \"flat_nli\"\n   - Any experiment whose command/spec references \"Qwen3-4B\" or \"qwen3-4b\"\n4. For each matching experiment, extract:\n   - exp_id\n   - status\n   - conclusion (if any)\n   - The full spec.command (the actual shell command used)\n   - Any metrics (especially ign_f1)\n   - created_at / updated_at\n\nOutput ALL of this information verbatim - do not summarize or truncate commands. I need the full command strings to audit eval configurations.\n\nUse python for the parsing since jq may struggle with nested JSON strings."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "9eb37328-b0ce-43ed-a6b0-4ca4885fce94",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VUdQC1qLX54kQBJCaNtkrT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 613,
      "cache_read_input_tokens": 26191,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 613
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

_source line 13_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "aa0dedafabeeb8ab6",
  "tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "description": "Parse 4B eval experiments from registry",
  "task_type": "local_agent",
  "prompt": "I need you to analyze a large JSON registry file and extract all 4B-related experiments (especially eval experiments).\n\nThe file is at: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/596d8411-63f5-4757-a2a4-2c57b1fcaba0/tool-results/mcp-agent-ml-research-read_registry-1779141732674.txt\n\nIt's JSON with schema: {result: string} where result is a JSON string that needs to be parsed.\n\nSteps:\n1. First probe the structure with jq (type, length, keys)\n2. Parse the nested JSON (result is a JSON string containing the actual data)\n3. Filter for ALL experiments that match ANY of these criteria:\n   - exp_id contains \"4b\" or \"4B\" (case insensitive)\n   - exp_id contains \"wave1_sft\" \n   - exp_id contains \"rsft_ced\" or \"flat_nli\"\n   - Any experiment whose command/spec references \"Qwen3-4B\" or \"qwen3-4b\"\n4. For each matching experiment, extract:\n   - exp_id\n   - status\n   - conclusion (if any)\n   - The full spec.command (the actual shell command used)\n   - Any metrics (especially ign_f1)\n   - created_at / updated_at\n\nOutput ALL of this information verbatim - do not summarize or truncate commands. I need the full command strings to audit eval configurations.\n\nUse python for the parsing since jq may struggle with nested JSON strings.",
  "uuid": "c57a9ede-0d55-42f5-a184-0ef14265462d",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0"
}
```

---


## Round 1

## Round 1

67 recorded events


### User

_source line 14 · 2026-05-18T22:02:23.106Z_

I need you to analyze a large JSON registry file and extract all 4B-related experiments (especially eval experiments).

The file is at: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/596d8411-63f5-4757-a2a4-2c57b1fcaba0/tool-results/mcp-agent-ml-research-read_registry-1779141732674.txt

It's JSON with schema: {result: string} where result is a JSON string that needs to be parsed.

Steps:
1. First probe the structure with jq (type, length, keys)
2. Parse the nested JSON (result is a JSON string containing the actual data)
3. Filter for ALL experiments that match ANY of these criteria:
   - exp_id contains "4b" or "4B" (case insensitive)
   - exp_id contains "wave1_sft" 
   - exp_id contains "rsft_ced" or "flat_nli"
   - Any experiment whose command/spec references "Qwen3-4B" or "qwen3-4b"
4. For each matching experiment, extract:
   - exp_id
   - status
   - conclusion (if any)
   - The full spec.command (the actual shell command used)
   - Any metrics (especially ign_f1)
   - created_at / updated_at

Output ALL of this information verbatim - do not summarize or truncate commands. I need the full command strings to audit eval configurations.

Use python for the parsing since jq may struggle with nested JSON strings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "c4928247-4c61-4705-96ff-bec79d8f8a3e"
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
  "task_id": "aa0dedafabeeb8ab6",
  "tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "description": "Running Check file size",
  "usage": {
    "total_tokens": 16039,
    "tool_uses": 1,
    "duration_ms": 4063
  },
  "last_tool_name": "Bash",
  "uuid": "459f45d9-bdb1-4036-8df3-86de5f05c368",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0"
}
```

---


### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Bash · `toolu_01RPC8jZJqNFBdP9WtS5bA9C`</summary>

```json
{
  "command": "wc -c /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/596d8411-63f5-4757-a2a4-2c57b1fcaba0/tool-results/mcp-agent-ml-research-read_registry-1779141732674.txt",
  "description": "Check file size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "92b75a88-3e7a-44c3-b9c7-2931629128f9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Nw3re7636Ta1D7UjkpmRK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16032,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16032,
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

_source line 17 · 2026-05-18T22:02:27.344Z_

<details><summary>↩ Tool result · `toolu_01RPC8jZJqNFBdP9WtS5bA9C`</summary>

```text
405821 /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/596d8411-63f5-4757-a2a4-2c57b1fcaba0/tool-results/mcp-agent-ml-research-read_registry-1779141732674.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "9afe9f41-d7f4-40f0-9f6c-9a7667a94eb7"
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
  "task_id": "aa0dedafabeeb8ab6",
  "tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "description": "Reading ~/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/596d8411-63f5-4757-a2a4-2c57b1fcaba0/tool-results/mcp-agent-ml-research-read_registry-1779141732674.txt",
  "usage": {
    "total_tokens": 16041,
    "tool_uses": 2,
    "duration_ms": 4772
  },
  "last_tool_name": "Read",
  "uuid": "fbb1cc01-c691-4741-8e61-4529005dc6d0",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0"
}
```

---


### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Read · `toolu_01VtueMBXYpan3MQzS1L3ARj`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/596d8411-63f5-4757-a2a4-2c57b1fcaba0/tool-results/mcp-agent-ml-research-read_registry-1779141732674.txt",
  "limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "4591a9be-0c91-4fd5-9682-302b488fd9ec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Nw3re7636Ta1D7UjkpmRK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16032,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16032,
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

_source line 20 · 2026-05-18T22:02:28.392Z_

<details><summary>↩ Tool result · reported error · `toolu_01VtueMBXYpan3MQzS1L3ARj`</summary>

```text
File content (177098 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "464b5902-933e-4835-bd2c-2be5698d45e5",
  "tool_use_result": "Error: File content (177098 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
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
  "task_id": "aa0dedafabeeb8ab6",
  "tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "description": "Running Probe JSON structure of registry file",
  "usage": {
    "total_tokens": 17397,
    "tool_uses": 3,
    "duration_ms": 13891
  },
  "last_tool_name": "Bash",
  "uuid": "bb93f237-2b2e-4745-b056-b40333ec7eb0",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0"
}
```

---


### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Bash · `toolu_01U9cNTtNuNuH1RbP44gUcew`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/596d8411-63f5-4757-a2a4-2c57b1fcaba0/tool-results/mcp-agent-ml-research-read_registry-1779141732674.txt\"\n\nwith open(fpath, 'r') as f:\n    raw = json.load(f)\n\nprint(\"Top-level type:\", type(raw).__name__)\nprint(\"Top-level keys:\", list(raw.keys()) if isinstance(raw, dict) else \"N/A\")\n\n# Parse the nested result string\nresult_str = raw.get(\"result\", \"\")\nprint(\"\\nresult type:\", type(result_str).__name__)\nprint(\"result length:\", len(result_str))\n\ndata = json.loads(result_str)\nprint(\"\\nParsed data type:\", type(data).__name__)\nif isinstance(data, dict):\n    print(\"Parsed data keys:\", list(data.keys()))\n    # Check structure of experiments\n    exps = data.get(\"experiments\", data)\n    if isinstance(exps, dict):\n        print(\"Number of experiments:\", len(exps))\n        # Show first key to understand structure\n        first_key = list(exps.keys())[0]\n        print(\"\\nFirst experiment key:\", first_key)\n        print(\"First experiment structure keys:\", list(exps[first_key].keys()) if isinstance(exps[first_key], dict) else type(exps[first_key]))\n    elif isinstance(exps, list):\n        print(\"Number of experiments:\", len(exps))\n        print(\"First experiment keys:\", list(exps[0].keys()) if exps else \"empty\")\nelif isinstance(data, list):\n    print(\"Number of items:\", len(data))\n    if data:\n        print(\"First item keys:\", list(data[0].keys()) if isinstance(data[0], dict) else type(data[0]))\nPYEOF",
  "description": "Probe JSON structure of registry file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "9e3037fd-b294-450f-9f2a-85dba92001f8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y2ajtfxdrFs3kiQjqHjSiF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1356,
      "cache_read_input_tokens": 16032,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1356,
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

_source line 23 · 2026-05-18T22:02:37.171Z_

<details><summary>↩ Tool result · `toolu_01U9cNTtNuNuH1RbP44gUcew`</summary>

```text
Top-level type: dict
Top-level keys: ['result']

result type: str
result length: 371629

Parsed data type: dict
Parsed data keys: ['success', 'data', 'error', 'metadata']
Number of experiments: 4

First experiment key: success
First experiment structure keys: &lt;class 'bool'>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "4a801884-1554-4b8f-b7c4-aba4196ac385"
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
  "task_id": "aa0dedafabeeb8ab6",
  "tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "description": "Running Explore nested data structure",
  "usage": {
    "total_tokens": 18159,
    "tool_uses": 4,
    "duration_ms": 20038
  },
  "last_tool_name": "Bash",
  "uuid": "51d88b0e-53cf-4b15-b5d0-09db5628817b",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0"
}
```

---


### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Bash · `toolu_01NNmF1bAYtir3Nu529KuunP`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/596d8411-63f5-4757-a2a4-2c57b1fcaba0/tool-results/mcp-agent-ml-research-read_registry-1779141732674.txt\"\n\nwith open(fpath, 'r') as f:\n    raw = json.load(f)\n\ndata = json.loads(raw[\"result\"])\nprint(\"success:\", data[\"success\"])\nprint(\"error:\", data[\"error\"])\nprint(\"metadata:\", data[\"metadata\"])\nprint()\n\ninner = data[\"data\"]\nprint(\"data type:\", type(inner).__name__)\nif isinstance(inner, dict):\n    print(\"data keys:\", list(inner.keys()))\n    # Check experiments\n    for k, v in inner.items():\n        if isinstance(v, (list, dict)):\n            print(f\"  {k}: type={type(v).__name__}, len={len(v)}\")\n        else:\n            print(f\"  {k}: {v}\")\nelif isinstance(inner, list):\n    print(\"data length:\", len(inner))\n    if inner:\n        print(\"first item keys:\", list(inner[0].keys()) if isinstance(inner[0], dict) else type(inner[0]))\nPYEOF",
  "description": "Explore nested data structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "aa6b4e0b-ce78-4b1c-86f7-9f42462fd1d2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013gDHPYY2WMPSAy33o7rEQ7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 689,
      "cache_read_input_tokens": 17388,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 689,
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

_source line 26 · 2026-05-18T22:02:43.251Z_

<details><summary>↩ Tool result · `toolu_01NNmF1bAYtir3Nu529KuunP`</summary>

```text
success: True
error: None
metadata: {'elapsed_seconds': 1.6518}

data type: dict
data keys: ['experiments', 'count', 'total', 'baseline']
  experiments: type=dict, len=222
  count: 222
  total: 222
  baseline: None
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "13abc4af-2af3-419c-b902-15db94b33963"
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
  "task_id": "aa0dedafabeeb8ab6",
  "tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "description": "Running List all experiment IDs",
  "usage": {
    "total_tokens": 18662,
    "tool_uses": 5,
    "duration_ms": 25436
  },
  "last_tool_name": "Bash",
  "uuid": "00ad9f55-3d15-4378-ba19-a544d19d3d13",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0"
}
```

---


### Tool call

_source line 28_

<details open><summary>🔧 Tool call — Bash · `toolu_0153NuwZQerL1BjM7fcEttQn`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/596d8411-63f5-4757-a2a4-2c57b1fcaba0/tool-results/mcp-agent-ml-research-read_registry-1779141732674.txt\"\n\nwith open(fpath, 'r') as f:\n    raw = json.load(f)\n\ndata = json.loads(raw[\"result\"])\nexperiments = data[\"data\"][\"experiments\"]\n\n# First, list ALL exp_ids to understand naming patterns\nall_ids = sorted(experiments.keys())\nprint(\"=== ALL EXPERIMENT IDS ===\")\nfor eid in all_ids:\n    print(f\"  {eid}\")\nprint(f\"\\nTotal: {len(all_ids)}\")\nPYEOF",
  "description": "List all experiment IDs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "28419477-5429-4816-b507-54c8d43e9da6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HxoziHsb9Krwu8xLW8y8Wj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 501,
      "cache_read_input_tokens": 18077,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 501,
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

_source line 29 · 2026-05-18T22:02:48.648Z_

<details><summary>↩ Tool result · `toolu_0153NuwZQerL1BjM7fcEttQn`</summary>

```text
=== ALL EXPERIMENT IDS ===
  d102_1_7b_rsft_k1_s42
  d102_8b_rsft_k1_s42
  d102_8b_rsft_k1_s43
  d102_llama_rsft_k1_s42
  d102_llama_rsft_k1_s43_eval
  eval_flat_nli_s44
  eval_flat_nli_seed44
  eval_flat_nli_seed45
  eval_grpo_g8_bf16
  eval_plan_001_flat_nli
  eval_plan_001_flat_nli_s43
  eval_plan_008_rsft_topk3
  eval_plan_008_topk3_fixed
  eval_plan_012_dpo_1ep_fixed
  eval_plan_012_dpo_1ep_fixed_r2
  eval_plan_012_dpo_ced_1ep
  eval_plan_012_dpo_ced_ckpt400
  eval_plan_014_no_evidence
  eval_plan_014_no_evidence_r2
  eval_plan_014_sft_no_evidence
  eval_rsft_ced_s43
  eval_rsft_ced_s45
  eval_sft_baseline_noquant
  grpo_bf16_g4_ckpt100_eval
  grpo_bf16_g4_ckpt200_eval
  lead1_ced_evidence_filter
  lead2_ckpt20_eval
  lead2_rsft_grpo_ced
  lead2_rsft_grpo_ced_r2
  mvp1_ced_signal
  mvp2_ced_reranker_poc
  mvp2_diversity_probe
  mvp2_eval_ced_kl001_r4_ckpt10
  mvp2_eval_ced_kl001_r4_ckpt7080
  mvp2_eval_ced_kl001_r4_ckpt90
  mvp2_eval_ced_kl001_r4_early
  mvp2_eval_ced_kl001_r4_high
  mvp2_eval_ced_kl001_r4_last
  mvp2_eval_ced_kl001_r4_multi
  mvp2_eval_ced_kl001_r4_step100
  mvp2_eval_ced_kl001_r4_step90
  mvp2_eval_lr5e6_r1_ckpt100
  mvp2_eval_lr5e6_r1_ckpt20
  mvp2_eval_lr5e6_r1_ckpt40
  mvp2_eval_lr5e6_r1_ckpt40_r2
  mvp2_eval_lr5e6_r1_ckpt60
  mvp2_eval_lr5e6_r1_ckpt60_r2
  mvp2_eval_lr5e6_r1_ckpt80
  mvp2_eval_lr5e6_rp_r2_ckpt20
  mvp2_eval_rsft_r1
  mvp2_eval_rsft_r2a
  mvp2_eval_rsft_r2b
  mvp2_eval_rsft_r2b_maxtok1536
  mvp2_eval_rsft_r2b_maxtok1536_r2
  mvp2_eval_rsft_s43
  mvp2_eval_rsft_s43_r2
  mvp2_eval_rsft_s44
  mvp2_eval_sft_baseline
  mvp2_grpo_ced
  mvp2_grpo_ced_kl001
  mvp2_grpo_ced_kl001_r2
  mvp2_grpo_ced_kl001_r3
  mvp2_grpo_ced_kl001_r4
  mvp2_grpo_ced_lr5e6_p1_r1
  mvp2_grpo_ced_lr5e6_r1
  mvp2_grpo_ced_lr5e6_rp_r1
  mvp2_grpo_ced_lr5e6_rp_r2
  mvp2_grpo_ced_r1
  mvp2_grpo_ced_r2
  mvp2_grpo_ced_r3
  mvp2_grpo_ced_r4
  mvp2_grpo_ced_r5
  mvp2_grpo_extract
  mvp2_grpo_extract_r2
  mvp2_grpo_extract_r3
  mvp2_grpo_extract_r4
  mvp2_grpo_flatnli
  mvp2_grpo_flatnli_r2
  mvp2_grpo_flatnli_r3
  mvp2_grpo_flatnli_r4
  mvp2_grpo_flatnli_r5
  mvp2_grpo_flatnli_r6
  mvp2_rsft_ced_scoring
  mvp2_rsft_ced_scoring_topk3
  mvp2_rsft_ced_scoring_topk3_r2
  mvp2_rsft_diagnosis
  mvp2_rsft_gen_s0
  mvp2_rsft_gen_s1
  mvp2_rsft_gen_s2
  mvp2_rsft_gen_s3
  mvp2_rsft_generate
  mvp2_rsft_r2a
  mvp2_rsft_r2b
  mvp2_rsft_train_r1
  mvp2_rsft_train_r1_s43
  mvp2_rsft_train_r1_s44
  mvp2_rsft_train_r2_fix
  mvp2_sft_eval
  mvp2_sft_eval_r2
  mvp2_sft_eval_r3
  mvp2_sft_warmup
  plan006_1_7b_rsft_eval
  plan019_1_7b_sft_s43
  plan019_1_7b_sft_s43_eval
  plan019_1_7b_sft_s43_r2
  plan019_1_7b_sft_s44
  plan019_1_7b_sft_s44_eval
  plan019_8b_sft_s44
  plan019_8b_sft_s44_eval
  plan_001_flat_nli_scoring
  plan_001_flat_nli_seed43
  plan_001_flat_nli_seed44
  plan_001_flat_nli_seed45
  plan_001_rsft_flat_nli
  plan_002_test_eval_s44
  plan_002_test_eval_s44_r2
  plan_002_test_rsft_s43
  plan_002_test_rsft_s44
  plan_003_edcr_diagnostic
  plan_004_dreeam_baseline
  plan_006_llama_rsft_r3_eval
  plan_006_llama_rsft_seed43
  plan_006_llama_rsft_seed43_eval
  plan_006_llama_rsft_seed43_eval_r2
  plan_006_llama_rsft_test
  plan_006_qwen3_1_7b_ced_scoring
  plan_006_qwen3_1_7b_no_evidence_eval
  plan_006_qwen3_1_7b_no_evidence_eval_v2
  plan_006_qwen3_1_7b_no_evidence_eval_v2r2
  plan_006_qwen3_1_7b_no_evidence_eval_v3
  plan_006_qwen3_1_7b_no_evidence_sft
  plan_006_qwen3_1_7b_rsft_candidates
  plan_006_qwen3_1_7b_rsft_eval
  plan_006_qwen3_1_7b_rsft_eval_r2
  plan_006_qwen3_1_7b_rsft_seed43
  plan_006_qwen3_1_7b_rsft_seed43_eval
  plan_006_qwen3_1_7b_rsft_test
  plan_006_qwen3_1_7b_rsft_train
  plan_006_qwen3_1_7b_sft
  plan_006_qwen3_1_7b_sft_bf16
  plan_006_qwen3_1_7b_sft_eval
  plan_006_qwen3_8b_ced_scoring
  plan_006_qwen3_8b_no_evidence_eval
  plan_006_qwen3_8b_no_evidence_eval_v2
  plan_006_qwen3_8b_no_evidence_sft
  plan_006_qwen3_8b_rsft_candidates
  plan_006_qwen3_8b_rsft_candidates_r2
  plan_006_qwen3_8b_rsft_eval
  plan_006_qwen3_8b_rsft_test
  plan_006_qwen3_8b_rsft_train
  plan_006_qwen3_8b_rsft_train_r2
  plan_006_qwen3_8b_sft_bf16
  plan_006_qwen3_8b_sft_eval
  plan_007_redocred_4b_sft_eval
  plan_007_redocred_4b_sft_eval_r2
  plan_007_redocred_rsft_eval
  plan_007_redocred_rsft_eval_r2
  plan_007_redocred_rsft_eval_r3
  plan_007_redocred_rsft_eval_r4
  plan_007_redocred_rsft_eval_r5
  plan_008_rsft_topk3
  plan_009_dynamics_figure
  plan_009_extract_reward_eval
  plan_009_flatnli_reward_eval
  plan_009_flatnli_reward_eval_r2
  plan_009_forgetting_figure
  plan_011_bf16_g8_step_eval
  plan_011_eval_g8_bf16_ckpt100
  plan_011_grpo_g8_bf16
  plan_011_grpo_g8_bf16_eval
  plan_012_dpo_ced
  plan_012_dpo_ced_1ep
  plan_014_no_evidence_eval_d076
  plan_014_sft_no_evidence
  plan_015_grpo_g4_bf16
  plan_015_grpo_g4_bf16_v2
  plan_015_grpo_g4_bf16_v3
  plan_016_llama_3_1_8b_no_evidence_eval
  plan_016_llama_3_1_8b_no_evidence_sft
  plan_016_llama_3_1_8b_sft
  plan_016_llama_3_1_8b_sft_eval
  plan_016_llama_ced_scoring
  plan_016_llama_grpo_qlora
  plan_016_llama_rsft_candidates
  plan_016_llama_rsft_candidates_r2
  plan_016_llama_rsft_candidates_r3
  plan_016_llama_rsft_train
  plan_016_llama_rsft_train_r2
  plan_016_llama_rsft_train_r3
  post_hoc_bm25_baseline
  precompute_nli_train
  random_rsft_k1_baseline
  random_rsft_k1_eval
  reeval_ced_s42
  reeval_ced_s44
  reeval_flat_nli_s42
  reeval_flat_nli_s43
  reeval_flat_nli_s43_r2
  reeval_flat_nli_s44
  reeval_rsft_topk3
  reeval_sft_baseline_d076
  rsft_ced_s43_train
  rsft_ced_s43_train_r2
  rsft_ced_s43_train_r3
  rsft_ced_s45_train
  rsft_ced_s45_train_r2
  rsft_ced_s45_train_r3
  rsft_ced_s45_train_r4
  rsft_llama_k1_s43_train
  rsft_s43_dev_eval_preds
  rsft_s44_dev_eval_preds
  seed_comparison_prep
  seed_llama_rsft_k1_s43
  seed_llama_rsft_k1_s43_eval
  smoke_test_grpo
  wave1_grpo_bf16_g4
  wave1_sft_4b_s43
  wave1_sft_4b_s43_eval
  wave1_sft_4b_s43_eval_r2
  wave1_sft_4b_s44
  wave1_sft_4b_s44_eval
  wave1_sft_4b_s44_eval_r2

Total: 222
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "7d55cf06-559b-42a7-ae23-fc82b130feb4"
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
  "task_id": "aa0dedafabeeb8ab6",
  "tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "description": "Running Filter experiments matching criteria",
  "usage": {
    "total_tokens": 22437,
    "tool_uses": 6,
    "duration_ms": 36424
  },
  "last_tool_name": "Bash",
  "uuid": "9ee30c82-cacd-4653-85fb-dd3dae5faca7",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0"
}
```

---


### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Bash · `toolu_01H7JsdKg9emwLhJrNr2qs7x`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/596d8411-63f5-4757-a2a4-2c57b1fcaba0/tool-results/mcp-agent-ml-research-read_registry-1779141732674.txt\"\n\nwith open(fpath, 'r') as f:\n    raw = json.load(f)\n\ndata = json.loads(raw[\"result\"])\nexperiments = data[\"data\"][\"experiments\"]\n\n# Filter criteria\ndef matches(exp_id, exp_data):\n    eid_lower = exp_id.lower()\n    # Criteria 1: exp_id contains \"4b\"\n    if \"4b\" in eid_lower:\n        return True\n    # Criteria 2: exp_id contains \"wave1_sft\"\n    if \"wave1_sft\" in eid_lower:\n        return True\n    # Criteria 3: exp_id contains \"rsft_ced\" or \"flat_nli\"\n    if \"rsft_ced\" in eid_lower or \"flat_nli\" in eid_lower:\n        return True\n    # Criteria 4: command/spec references \"Qwen3-4B\" or \"qwen3-4b\"\n    spec = exp_data.get(\"spec\", {})\n    if spec:\n        cmd = spec.get(\"command\", \"\") or \"\"\n        spec_str = json.dumps(spec).lower()\n        if \"qwen3-4b\" in spec_str:\n            return True\n    return True  # Actually, let me not do a catch-all\n\n# Redo with proper logic\ndef matches(exp_id, exp_data):\n    eid_lower = exp_id.lower()\n    if \"4b\" in eid_lower:\n        return True\n    if \"wave1_sft\" in eid_lower:\n        return True\n    if \"rsft_ced\" in eid_lower:\n        return True\n    if \"flat_nli\" in eid_lower:\n        return True\n    # Check spec/command for Qwen3-4B\n    spec = exp_data.get(\"spec\", {}) or {}\n    cmd = spec.get(\"command\", \"\") or \"\"\n    spec_str = json.dumps(spec).lower()\n    if \"qwen3-4b\" in spec_str or \"qwen3_4b\" in spec_str:\n        return True\n    return False\n\nmatched = {}\nfor eid, edata in experiments.items():\n    if matches(eid, edata):\n        matched[eid] = edata\n\nprint(f\"Total matched: {len(matched)}\")\nprint(\"\\nMatched exp_ids:\")\nfor eid in sorted(matched.keys()):\n    print(f\"  {eid}\")\nPYEOF",
  "description": "Filter experiments matching criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "5c2a4c04-748e-4d93-a3de-cc463427f465",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VwaGqz8v6saFuywecKF7Uj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3771,
      "cache_read_input_tokens": 18578,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3771,
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

_source line 32 · 2026-05-18T22:02:59.639Z_

<details><summary>↩ Tool result · `toolu_01H7JsdKg9emwLhJrNr2qs7x`</summary>

```text
Total matched: 133

Matched exp_ids:
  eval_flat_nli_s44
  eval_flat_nli_seed44
  eval_flat_nli_seed45
  eval_grpo_g8_bf16
  eval_plan_001_flat_nli
  eval_plan_001_flat_nli_s43
  eval_plan_008_rsft_topk3
  eval_plan_008_topk3_fixed
  eval_plan_012_dpo_1ep_fixed
  eval_plan_012_dpo_1ep_fixed_r2
  eval_plan_012_dpo_ced_1ep
  eval_plan_012_dpo_ced_ckpt400
  eval_plan_014_no_evidence
  eval_plan_014_no_evidence_r2
  eval_rsft_ced_s43
  eval_rsft_ced_s45
  eval_sft_baseline_noquant
  grpo_bf16_g4_ckpt100_eval
  grpo_bf16_g4_ckpt200_eval
  lead2_ckpt20_eval
  lead2_rsft_grpo_ced
  lead2_rsft_grpo_ced_r2
  mvp2_ced_reranker_poc
  mvp2_diversity_probe
  mvp2_eval_ced_kl001_r4_ckpt10
  mvp2_eval_ced_kl001_r4_ckpt90
  mvp2_eval_ced_kl001_r4_early
  mvp2_eval_ced_kl001_r4_high
  mvp2_eval_ced_kl001_r4_multi
  mvp2_eval_ced_kl001_r4_step100
  mvp2_eval_ced_kl001_r4_step90
  mvp2_eval_lr5e6_r1_ckpt100
  mvp2_eval_lr5e6_r1_ckpt20
  mvp2_eval_lr5e6_r1_ckpt40
  mvp2_eval_lr5e6_r1_ckpt40_r2
  mvp2_eval_lr5e6_r1_ckpt60_r2
  mvp2_eval_lr5e6_r1_ckpt80
  mvp2_eval_lr5e6_rp_r2_ckpt20
  mvp2_eval_rsft_r1
  mvp2_eval_rsft_r2a
  mvp2_eval_rsft_r2b
  mvp2_eval_rsft_r2b_maxtok1536
  mvp2_eval_rsft_r2b_maxtok1536_r2
  mvp2_eval_rsft_s43
  mvp2_eval_rsft_s43_r2
  mvp2_eval_sft_baseline
  mvp2_grpo_ced
  mvp2_grpo_ced_kl001
  mvp2_grpo_ced_kl001_r4
  mvp2_grpo_ced_lr5e6_r1
  mvp2_grpo_ced_lr5e6_rp_r1
  mvp2_grpo_ced_lr5e6_rp_r2
  mvp2_grpo_ced_r1
  mvp2_grpo_ced_r2
  mvp2_grpo_ced_r3
  mvp2_grpo_ced_r4
  mvp2_grpo_ced_r5
  mvp2_grpo_extract
  mvp2_grpo_extract_r2
  mvp2_grpo_extract_r3
  mvp2_grpo_extract_r4
  mvp2_grpo_flatnli
  mvp2_grpo_flatnli_r2
  mvp2_grpo_flatnli_r3
  mvp2_grpo_flatnli_r4
  mvp2_grpo_flatnli_r5
  mvp2_grpo_flatnli_r6
  mvp2_rsft_ced_scoring
  mvp2_rsft_ced_scoring_topk3
  mvp2_rsft_ced_scoring_topk3_r2
  mvp2_rsft_generate
  mvp2_rsft_r2a
  mvp2_rsft_r2b
  mvp2_rsft_train_r1
  mvp2_rsft_train_r1_s43
  mvp2_rsft_train_r1_s44
  mvp2_sft_eval
  mvp2_sft_eval_r2
  mvp2_sft_eval_r3
  mvp2_sft_warmup
  plan_001_flat_nli_scoring
  plan_001_flat_nli_seed43
  plan_001_flat_nli_seed44
  plan_001_flat_nli_seed45
  plan_001_rsft_flat_nli
  plan_002_test_eval_s44
  plan_002_test_eval_s44_r2
  plan_002_test_rsft_s43
  plan_002_test_rsft_s44
  plan_007_redocred_4b_sft_eval
  plan_007_redocred_4b_sft_eval_r2
  plan_007_redocred_rsft_eval
  plan_007_redocred_rsft_eval_r2
  plan_007_redocred_rsft_eval_r3
  plan_007_redocred_rsft_eval_r4
  plan_007_redocred_rsft_eval_r5
  plan_008_rsft_topk3
  plan_009_flatnli_reward_eval
  plan_009_flatnli_reward_eval_r2
  plan_011_grpo_g8_bf16
  plan_011_grpo_g8_bf16_eval
  plan_012_dpo_ced
  plan_012_dpo_ced_1ep
  plan_014_no_evidence_eval_d076
  plan_014_sft_no_evidence
  plan_015_grpo_g4_bf16
  plan_015_grpo_g4_bf16_v2
  plan_015_grpo_g4_bf16_v3
  random_rsft_k1_eval
  reeval_ced_s42
  reeval_ced_s44
  reeval_flat_nli_s42
  reeval_flat_nli_s43
  reeval_flat_nli_s43_r2
  reeval_flat_nli_s44
  reeval_rsft_topk3
  reeval_sft_baseline_d076
  rsft_ced_s43_train
  rsft_ced_s43_train_r2
  rsft_ced_s43_train_r3
  rsft_ced_s45_train
  rsft_ced_s45_train_r2
  rsft_ced_s45_train_r3
  rsft_ced_s45_train_r4
  rsft_s43_dev_eval_preds
  rsft_s44_dev_eval_preds
  wave1_grpo_bf16_g4
  wave1_sft_4b_s43
  wave1_sft_4b_s43_eval
  wave1_sft_4b_s43_eval_r2
  wave1_sft_4b_s44
  wave1_sft_4b_s44_eval
  wave1_sft_4b_s44_eval_r2
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "33ff8247-487b-4151-b600-e624d9add932"
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
  "task_id": "aa0dedafabeeb8ab6",
  "tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "description": "Running Identify explicitly 4B-related experiments",
  "usage": {
    "total_tokens": 25342,
    "tool_uses": 7,
    "duration_ms": 45169
  },
  "last_tool_name": "Bash",
  "uuid": "92f6d92e-744e-4e3d-bd8f-16c579b012a9",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0"
}
```

---


### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Bash · `toolu_01MJdGvqbTYFb6jU7uv4MipG`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/596d8411-63f5-4757-a2a4-2c57b1fcaba0/tool-results/mcp-agent-ml-research-read_registry-1779141732674.txt\"\n\nwith open(fpath, 'r') as f:\n    raw = json.load(f)\n\ndata = json.loads(raw[\"result\"])\nexperiments = data[\"data\"][\"experiments\"]\n\n# Let me first check which experiments reference Qwen3-4B in their spec\nprint(\"=== EXPERIMENTS REFERENCING Qwen3-4B IN SPEC ===\")\nfor eid, edata in sorted(experiments.items()):\n    spec = edata.get(\"spec\", {}) or {}\n    spec_str = json.dumps(spec).lower()\n    if \"qwen3-4b\" in spec_str or \"qwen3_4b\" in spec_str:\n        print(f\"  {eid}\")\n\nprint(\"\\n=== EXPERIMENTS WITH '4b' IN EXP_ID ===\")\nfor eid in sorted(experiments.keys()):\n    if \"4b\" in eid.lower():\n        print(f\"  {eid}\")\n\nprint(\"\\n=== EXPERIMENTS WITH 'wave1_sft' IN EXP_ID ===\")\nfor eid in sorted(experiments.keys()):\n    if \"wave1_sft\" in eid.lower():\n        print(f\"  {eid}\")\nPYEOF",
  "description": "Identify explicitly 4B-related experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "1c83df3b-aab4-47ce-80b3-d3859133c177",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LHJe8BZxP57pTKg3PGkzA7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2903,
      "cache_read_input_tokens": 22349,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2903,
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

_source line 35 · 2026-05-18T22:03:08.378Z_

<details><summary>↩ Tool result · `toolu_01MJdGvqbTYFb6jU7uv4MipG`</summary>

```text
=== EXPERIMENTS REFERENCING Qwen3-4B IN SPEC ===
  eval_flat_nli_s44
  eval_flat_nli_seed44
  eval_flat_nli_seed45
  eval_grpo_g8_bf16
  eval_plan_001_flat_nli
  eval_plan_001_flat_nli_s43
  eval_plan_008_rsft_topk3
  eval_plan_008_topk3_fixed
  eval_plan_012_dpo_1ep_fixed
  eval_plan_012_dpo_1ep_fixed_r2
  eval_plan_012_dpo_ced_1ep
  eval_plan_012_dpo_ced_ckpt400
  eval_plan_014_no_evidence
  eval_plan_014_no_evidence_r2
  eval_rsft_ced_s43
  eval_rsft_ced_s45
  eval_sft_baseline_noquant
  grpo_bf16_g4_ckpt100_eval
  grpo_bf16_g4_ckpt200_eval
  lead2_ckpt20_eval
  lead2_rsft_grpo_ced
  lead2_rsft_grpo_ced_r2
  mvp2_ced_reranker_poc
  mvp2_diversity_probe
  mvp2_eval_ced_kl001_r4_ckpt10
  mvp2_eval_ced_kl001_r4_ckpt90
  mvp2_eval_ced_kl001_r4_early
  mvp2_eval_ced_kl001_r4_high
  mvp2_eval_ced_kl001_r4_multi
  mvp2_eval_ced_kl001_r4_step100
  mvp2_eval_ced_kl001_r4_step90
  mvp2_eval_lr5e6_r1_ckpt100
  mvp2_eval_lr5e6_r1_ckpt20
  mvp2_eval_lr5e6_r1_ckpt40
  mvp2_eval_lr5e6_r1_ckpt40_r2
  mvp2_eval_lr5e6_r1_ckpt60_r2
  mvp2_eval_lr5e6_r1_ckpt80
  mvp2_eval_lr5e6_rp_r2_ckpt20
  mvp2_eval_rsft_r1
  mvp2_eval_rsft_r2a
  mvp2_eval_rsft_r2b
  mvp2_eval_rsft_r2b_maxtok1536
  mvp2_eval_rsft_r2b_maxtok1536_r2
  mvp2_eval_rsft_s43
  mvp2_eval_rsft_s43_r2
  mvp2_eval_sft_baseline
  mvp2_grpo_ced
  mvp2_grpo_ced_kl001
  mvp2_grpo_ced_kl001_r4
  mvp2_grpo_ced_lr5e6_r1
  mvp2_grpo_ced_lr5e6_rp_r1
  mvp2_grpo_ced_lr5e6_rp_r2
  mvp2_grpo_ced_r1
  mvp2_grpo_ced_r2
  mvp2_grpo_ced_r3
  mvp2_grpo_ced_r4
  mvp2_grpo_ced_r5
  mvp2_grpo_extract
  mvp2_grpo_extract_r2
  mvp2_grpo_extract_r3
  mvp2_grpo_extract_r4
  mvp2_grpo_flatnli
  mvp2_grpo_flatnli_r2
  mvp2_grpo_flatnli_r3
  mvp2_grpo_flatnli_r4
  mvp2_grpo_flatnli_r5
  mvp2_grpo_flatnli_r6
  mvp2_rsft_generate
  mvp2_rsft_r2a
  mvp2_rsft_r2b
  mvp2_rsft_train_r1
  mvp2_rsft_train_r1_s43
  mvp2_rsft_train_r1_s44
  mvp2_sft_eval
  mvp2_sft_eval_r2
  mvp2_sft_eval_r3
  mvp2_sft_warmup
  plan_001_flat_nli_seed43
  plan_001_flat_nli_seed44
  plan_001_flat_nli_seed45
  plan_001_rsft_flat_nli
  plan_002_test_eval_s44
  plan_002_test_eval_s44_r2
  plan_002_test_rsft_s43
  plan_002_test_rsft_s44
  plan_007_redocred_4b_sft_eval
  plan_007_redocred_4b_sft_eval_r2
  plan_007_redocred_rsft_eval
  plan_007_redocred_rsft_eval_r2
  plan_007_redocred_rsft_eval_r3
  plan_007_redocred_rsft_eval_r4
  plan_007_redocred_rsft_eval_r5
  plan_008_rsft_topk3
  plan_009_flatnli_reward_eval
  plan_009_flatnli_reward_eval_r2
  plan_011_grpo_g8_bf16
  plan_011_grpo_g8_bf16_eval
  plan_012_dpo_ced
  plan_012_dpo_ced_1ep
  plan_014_no_evidence_eval_d076
  plan_014_sft_no_evidence
  plan_015_grpo_g4_bf16
  plan_015_grpo_g4_bf16_v2
  plan_015_grpo_g4_bf16_v3
  random_rsft_k1_eval
  reeval_ced_s42
  reeval_ced_s44
  reeval_flat_nli_s42
  reeval_flat_nli_s43
  reeval_flat_nli_s43_r2
  reeval_flat_nli_s44
  reeval_rsft_topk3
  reeval_sft_baseline_d076
  rsft_ced_s43_train_r2
  rsft_ced_s45_train
  rsft_ced_s45_train_r2
  rsft_s43_dev_eval_preds
  rsft_s44_dev_eval_preds
  wave1_grpo_bf16_g4
  wave1_sft_4b_s43
  wave1_sft_4b_s43_eval
  wave1_sft_4b_s43_eval_r2
  wave1_sft_4b_s44
  wave1_sft_4b_s44_eval
  wave1_sft_4b_s44_eval_r2

=== EXPERIMENTS WITH '4b' IN EXP_ID ===
  plan_007_redocred_4b_sft_eval
  plan_007_redocred_4b_sft_eval_r2
  wave1_sft_4b_s43
  wave1_sft_4b_s43_eval
  wave1_sft_4b_s43_eval_r2
  wave1_sft_4b_s44
  wave1_sft_4b_s44_eval
  wave1_sft_4b_s44_eval_r2

=== EXPERIMENTS WITH 'wave1_sft' IN EXP_ID ===
  wave1_sft_4b_s43
  wave1_sft_4b_s43_eval
  wave1_sft_4b_s43_eval_r2
  wave1_sft_4b_s44
  wave1_sft_4b_s44_eval
  wave1_sft_4b_s44_eval_r2
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "266dba28-0bf5-4283-9de5-b8907e4f49a9"
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
  "task_id": "aa0dedafabeeb8ab6",
  "tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "description": "Running Extract full details for all matching experiments",
  "usage": {
    "total_tokens": 28052,
    "tool_uses": 8,
    "duration_ms": 56916
  },
  "last_tool_name": "Bash",
  "uuid": "1c3100c6-adf0-4b93-b1dd-9d07331baa1d",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0"
}
```

---


### Tool call

_source line 37_

<details open><summary>🔧 Tool call — Bash · `toolu_01Ten53zGvBFx1XsJhQeatun`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/596d8411-63f5-4757-a2a4-2c57b1fcaba0/tool-results/mcp-agent-ml-research-read_registry-1779141732674.txt\"\n\nwith open(fpath, 'r') as f:\n    raw = json.load(f)\n\ndata = json.loads(raw[\"result\"])\nexperiments = data[\"data\"][\"experiments\"]\n\ndef matches(exp_id, exp_data):\n    eid_lower = exp_id.lower()\n    if \"4b\" in eid_lower:\n        return True\n    if \"wave1_sft\" in eid_lower:\n        return True\n    if \"rsft_ced\" in eid_lower:\n        return True\n    if \"flat_nli\" in eid_lower:\n        return True\n    spec = exp_data.get(\"spec\", {}) or {}\n    spec_str = json.dumps(spec).lower()\n    if \"qwen3-4b\" in spec_str or \"qwen3_4b\" in spec_str:\n        return True\n    return False\n\nmatched = {eid: edata for eid, edata in experiments.items() if matches(eid, edata)}\n\n# Write full details to a temp file for easy reading\noutput = []\nfor eid in sorted(matched.keys()):\n    e = matched[eid]\n    output.append(f\"{'='*120}\")\n    output.append(f\"EXP_ID: {eid}\")\n    output.append(f\"STATUS: {e.get('status', 'N/A')}\")\n    output.append(f\"CREATED_AT: {e.get('created_at', 'N/A')}\")\n    output.append(f\"UPDATED_AT: {e.get('updated_at', 'N/A')}\")\n    \n    conclusion = e.get('conclusion', None)\n    if conclusion:\n        output.append(f\"CONCLUSION: {conclusion}\")\n    \n    metrics = e.get('metrics', None)\n    if metrics:\n        output.append(f\"METRICS: {json.dumps(metrics, indent=2)}\")\n    \n    spec = e.get('spec', {}) or {}\n    cmd = spec.get('command', None)\n    if cmd:\n        output.append(f\"COMMAND: {cmd}\")\n    \n    # Also include any other spec fields\n    for k, v in spec.items():\n        if k != 'command' and v is not None:\n            output.append(f\"SPEC.{k}: {v}\")\n    \n    output.append(\"\")\n\ntext = \"\\n\".join(output)\nout_path = \"/tmp/4b_experiments_full.txt\"\nwith open(out_path, 'w') as f:\n    f.write(text)\n\nprint(f\"Written {len(matched)} experiments to {out_path}\")\nprint(f\"File size: {len(text)} chars\")\nPYEOF",
  "description": "Extract full details for all matching experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "a4066504-b805-4db4-a782-654c88599fae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PePnv2ULXMXPmQRqJoDcDt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2708,
      "cache_read_input_tokens": 25252,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2708,
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

_source line 38 · 2026-05-18T22:03:20.409Z_

<details><summary>↩ Tool result · `toolu_01Ten53zGvBFx1XsJhQeatun`</summary>

```text
Written 133 experiments to /tmp/4b_experiments_full.txt
File size: 171063 chars
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "b8ff812b-95c1-4b14-99a2-55988d6d7da7"
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
  "task_id": "aa0dedafabeeb8ab6",
  "tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "description": "Reading /tmp/4b_experiments_full.txt",
  "usage": {
    "total_tokens": 29053,
    "tool_uses": 9,
    "duration_ms": 59559
  },
  "last_tool_name": "Read",
  "uuid": "015f638c-f68e-4139-85ae-b4ca23b2ba1a",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0"
}
```

---


### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Read · `toolu_01G6Dpbt82PqSDjMdCy7t8Rr`</summary>

```json
{
  "file_path": "/tmp/4b_experiments_full.txt",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "a54fa6e4-5440-41eb-a388-61e29a16c845",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XpMf9JoTu39MBTRHBcs8h1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 930,
      "cache_read_input_tokens": 27960,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 930,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 71,
      "service_tier": "standard",
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

_source line 41 · 2026-05-18T22:03:22.688Z_

<details><summary>↩ Tool result · `toolu_01G6Dpbt82PqSDjMdCy7t8Rr`</summary>

```text
1	========================================================================================================================
2	EXP_ID: eval_flat_nli_s44
3	STATUS: DONE
4	CREATED_AT: 2026-05-15T23:14:05.010Z
5	UPDATED_AT: 2026-05-16T03:49:35.610Z
6	CONCLUSION: success
7	METRICS: {
8	  "rel_f1": 0.461506,
9	  "ign_f1": 0.452126,
10	  "evi_f1": 0.813123,
11	  "edcr": 0.645808,
12	  "evi_f1_joint": 0.359673
13	}
14	COMMAND: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_flat_nli_s44/checkpoint-507 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 44 --output_dir /root/autodl-tmp/eval_results/rsft_flat_nli_s44 --no-quantize"
15	SPEC.server: rtx5090-4x
16	SPEC.gpu: ['cuda:0']
17	SPEC.pid: 270462
18	SPEC.log_path: ~/runs/faith-evidence-ie/eval_flat_nli_s44.log
19	SPEC.submitted_at: 2026-05-15T23:27:39.718Z
20	SPEC.submitted_via: submit_training_job
21	SPEC.backend: tmux
22	SPEC.account: root
23	SPEC.checkpoint_path: /root/autodl-tmp/rsft_output_flat_nli_s44/checkpoint-507
24	SPEC.wall_clock_seconds: 11069.8
25	SPEC.gpu_hours: 3.07
26	
27	========================================================================================================================
28	EXP_ID: eval_flat_nli_seed44
29	STATUS: DONE
30	CREATED_AT: 2026-05-15T23:12:38.199Z
31	UPDATED_AT: 2026-05-15T23:48:28.074Z
32	CONCLUSION: killed
33	COMMAND: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_flat_nli_s44/checkpoint-507 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 44 --output_dir /root/autodl-tmp/eval_results/rsft_flat_nli_s44 --no-quantize"
34	SPEC.server: rtx5090-4x
35	SPEC.gpu: ['cuda:0']
36	SPEC.pid: 270056
37	SPEC.log_path: ~/runs/faith-evidence-ie/eval_flat_nli_seed44.log
38	SPEC.submitted_at: 2026-05-15T23:27:04.263Z
39	SPEC.submitted_via: submit_training_job
40	SPEC.backend: tmux
41	SPEC.account: root
42	SPEC.wall_clock_seconds: 1283.8
43	SPEC.gpu_hours: 0.36
44	
45	========================================================================================================================
46	EXP_ID: eval_flat_nli_seed45
47	STATUS: DONE
48	CREATED_AT: 2026-05-15T23:12:39.186Z
49	UPDATED_AT: 2026-05-16T03:49:36.608Z
50	CONCLUSION: success
51	METRICS: {
52	  "rel_f1": 0.455052,
53	  "ign_f1": 0.446181,
54	  "evi_f1": 0.815399,
55	  "edcr": 0.652133,
56	  "evi_f1_joint": 0.355612
57	}
58	COMMAND: python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_flat_nli_s45/checkpoint-507 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 45 --output_dir /root/autodl-tmp/eval_results/rsft_flat_nli_s45 --no-quantize
59	SPEC.server: rtx5090-4x
60	SPEC.gpu: cuda:3
61	SPEC.pid: 272164
62	SPEC.log_path: ~/runs/faith-evidence-ie/eval_flat_nli_seed45.log
63	SPEC.submitted_at: 2026-05-15T23:44:54.114Z
64	SPEC.submitted_via: submit_training_job
65	SPEC.backend: tmux
66	SPEC.account: root
67	SPEC.data_path: /root/autodl-tmp/data/docred
68	SPEC.data_count: 12275
69	SPEC.model_name: Qwen3-4B
70	SPEC.seed: 45
71	SPEC.checkpoint_source: /root/autodl-tmp/rsft_output_flat_nli_s45/checkpoint-507
72	SPEC.eval_data: docred-dev
73	SPEC.wall_clock_seconds: 12094.9
74	SPEC.gpu_hours: 3.36
75	
76	========================================================================================================================
77	EXP_ID: eval_grpo_g8_bf16
78	STATUS: DONE
79	CREATED_AT: 2026-05-15T14:41:07.474Z
80	UPDATED_AT: 2026-05-15T17:57:46.573Z
81	CONCLUSION: success
82	METRICS: {
83	  "ckpt80_rel_f1": 0.4456,
84	  "ckpt80_ign_f1": 0.4456,
85	  "ckpt80_evi_f1": 0.8034,
86	  "ckpt80_edcr": 0.6409,
87	  "ckpt80_format_ok": "984/985",
88	  "ckpt80_truncated": 50,
89	  "ckpt90_rel_f1": 0.4523,
90	  "ckpt90_ign_f1": 0.4523,
91	  "ckpt90_evi_f1": 0.8052,
92	  "ckpt90_edcr": 0.6414,
93	  "ckpt90_format_ok": "983/985",
94	  "ckpt90_truncated": 61,
95	  "ckpt100_rel_f1": 0.4549,
96	  "ckpt100_ign_f1": 0.4549,
97	  "ckpt100_evi_f1": 0.8086,
98	  "ckpt100_edcr": 0.6318,
99	  "ckpt100_format_ok": "985/985",
100	  "ckpt100_truncated": 61,
101	  "best_checkpoint": "ckpt-100"
102	}
103	COMMAND: python -m freige.eval.batch_eval --exp_dir grpo_ced_g8_bf16 --sft_adapter sft_output --checkpoints 80,90,100 --no-quantize --max_new_tokens 1024
104	SPEC.server: rtx5090-4x
105	SPEC.gpu: ['cuda:3']
106	SPEC.pid: 214552
107	SPEC.log_path: ~/runs/faith-evidence-ie/eval_grpo_g8_bf16.log
108	SPEC.submitted_at: 2026-05-15T14:41:06.626Z
109	SPEC.submitted_via: submit_training_job
110	SPEC.backend: tmux
111	SPEC.account: root
112	SPEC.data_path: /root/autodl-tmp/data/docred
113	SPEC.data_count: 985
114	SPEC.model_name: Qwen3-4B + SFT + GRPO-G8-bf16
115	SPEC.seed: 42
116	SPEC.checkpoint_source: /root/autodl-tmp/grpo_ced_g8_bf16
117	SPEC.eval_data: docred dev (985 docs)
118	SPEC.parent: plan_011_grpo_g8_bf16
119	SPEC.wall_clock_seconds: 11785.0
120	SPEC.gpu_hours: 3.27
121	
122	========================================================================================================================
123	EXP_ID: eval_plan_001_flat_nli
124	STATUS: DONE
125	CREATED_AT: 2026-05-15T16:57:09.693Z
126	UPDATED_AT: 2026-05-15T18:04:13.598Z
127	CONCLUSION: success
128	METRICS: {
129	  "rel_f1": 0.4539,
130	  "ign_f1": 0.4539,
131	  "evi_f1": 0.8043,
132	  "edcr": 0.6431,
133	  "precision": 0.4671,
134	  "recall": 0.4414,
135	  "evi_precision": 0.8143,
136	  "evi_recall": 0.7945,
137	  "format_ok_rate": 1,
138	  "n_truncated": 199,
139	  "n_documents": 985,
140	  "n_predictions": 15294,
141	  "inference_time_seconds": 3631
142	}
143	COMMAND: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_flat_nli --sft_adapter /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/rsft_flat_nli --no-quantize"
144	SPEC.server: rtx5090-4x
145	SPEC.gpu: ['cuda:0']
146	SPEC.pid: 228508
147	SPEC.log_path: ~/runs/faith-evidence-ie/eval_plan_001_flat_nli.log
148	SPEC.submitted_at: 2026-05-15T16:57:46.175Z
149	SPEC.submitted_via: submit_training_job
150	SPEC.backend: tmux
151	SPEC.account: root
152	SPEC.data_path: /root/autodl-tmp/data/docred
153	SPEC.data_count: 985
154	SPEC.model_name: Qwen3-4B + SFT + RSFT-flat-NLI
155	SPEC.seed: 42
156	SPEC.checkpoint_source: /root/autodl-tmp/rsft_output_flat_nli
157	SPEC.eval_data: docred dev (985 docs)
158	SPEC.wall_clock_seconds: 3987.4
159	SPEC.gpu_hours: 1.11
160	
161	========================================================================================================================
162	EXP_ID: eval_plan_001_flat_nli_s43
163	STATUS: DONE
164	CREATED_AT: 2026-05-15T20:29:54.486Z
165	UPDATED_AT: 2026-05-15T21:35:00.000Z
166	CONCLUSION: failed
167	METRICS: {
168	  "rel_f1": 0.0022,
169	  "ign_f1": 0.0022,
170	  "evi_f1": 0.8533,
171	  "edcr": 0.9982,
172	  "num_preds": 17285,
173	  "format_ok": "981/985",
174	  "truncated": "251/985",
175	  "tp": 32,
176	  "note": "INVALID \u2014 missing --sft_adapter, same bug as DPO 1ep eval"
177	}
178	COMMAND: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_flat_nli_s43 --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 43 --output_dir /root/autodl-tmp/eval_results/rsft_flat_nli_s43 --no-quantize"
179	SPEC.server: rtx5090-4x
180	SPEC.gpu: ['cuda:0']
181	SPEC.pid: 252179
182	SPEC.log_path: ~/runs/faith-evidence-ie/eval_plan_001_flat_nli_s43.log
183	SPEC.submitted_at: 2026-05-15T20:30:26.563Z
184	SPEC.submitted_via: submit_training_job
185	SPEC.backend: tmux
186	SPEC.account: root
187	SPEC.data_path: /root/autodl-tmp/data/docred
188	SPEC.data_count: 985
189	SPEC.model_name: Qwen3-4B + flat-NLI RSFT s43 adapter
190	SPEC.seed: 43
191	SPEC.checkpoint_source: /root/autodl-tmp/rsft_output_flat_nli_s43
192	SPEC.eval_data: docred dev (985 docs)
193	
194	========================================================================================================================
195	EXP_ID: eval_plan_008_rsft_topk3
196	STATUS: DONE
197	CREATED_AT: 2026-05-15T21:09:51.464Z
198	UPDATED_AT: 2026-05-15T21:38:00.000Z
199	CONCLUSION: killed
200	METRICS: {
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "4e4aecab-290c-442b-9ab6-aeddad2efb7c"
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
  "task_id": "aa0dedafabeeb8ab6",
  "tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "description": "Reading /tmp/4b_experiments_full.txt",
  "usage": {
    "total_tokens": 33359,
    "tool_uses": 10,
    "duration_ms": 62475
  },
  "last_tool_name": "Read",
  "uuid": "783cd34e-bfa2-4e06-bf40-0994dd4c97a6",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0"
}
```

---


### Tool call

_source line 43_

<details open><summary>🔧 Tool call — Read · `toolu_01Bqjnzg9rc5ZutTQdQcdr8W`</summary>

```json
{
  "file_path": "/tmp/4b_experiments_full.txt",
  "offset": 200,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "41b53e19-cd25-4fd1-b759-615bdfad5576",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D3A4cbV9BTHagbLt4rnesZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4268,
      "cache_read_input_tokens": 28890,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4268,
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

_source line 44 · 2026-05-18T22:03:25.602Z_

<details><summary>↩ Tool result · `toolu_01Bqjnzg9rc5ZutTQdQcdr8W`</summary>

```text
200	METRICS: {
201	  "note": "INVALID \u2014 missing --sft_adapter, killed by Director instruction"
202	}
203	COMMAND: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_topk3_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/rsft_topk3 --no-quantize"
204	SPEC.server: rtx5090-4x
205	SPEC.gpu: ['cuda:3']
206	SPEC.pid: 255523
207	SPEC.log_path: ~/runs/faith-evidence-ie/eval_plan_008_rsft_topk3.log
208	SPEC.submitted_at: 2026-05-15T21:10:11Z
209	SPEC.submitted_via: submit_training_job
210	SPEC.backend: tmux
211	SPEC.account: root
212	SPEC.hypothesis: RSFT top_k=3 dev eval: 对比 top_k=5 RSFT (rel_f1≈0.46) 和 SFT baseline (rel_f1=0.4106)。top_k=3 训练 50-doc subset 显示 F1=0.50 但 Evi-F1 下降到 0.68。
213	SPEC.parent: plan_008_rsft_topk3
214	SPEC.data_path: /root/autodl-tmp/data/docred
215	SPEC.data_count: 985
216	SPEC.model_name: Qwen3-4B + SFT + RSFT top_k=3
217	SPEC.seed: 42
218	SPEC.checkpoint_source: /root/autodl-tmp/rsft_topk3_output
219	SPEC.eval_data: docred-dev (985 docs)
220	
221	========================================================================================================================
222	EXP_ID: eval_plan_008_topk3_fixed
223	STATUS: DONE
224	CREATED_AT: 2026-05-15T21:39:34.632Z
225	UPDATED_AT: 2026-05-15T21:39:34.632Z
226	CONCLUSION: killed
227	COMMAND: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_topk3_output --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/rsft_topk3_fixed --no-quantize"
228	SPEC.server: rtx5090-4x
229	SPEC.gpu: ['cuda:3']
230	SPEC.pid: 259032
231	SPEC.log_path: ~/runs/faith-evidence-ie/eval_plan_008_topk3_fixed.log
232	SPEC.submitted_at: 2026-05-15T21:39:34.183Z
233	SPEC.submitted_via: submit_training_job
234	SPEC.backend: tmux
235	SPEC.account: root
236	
237	========================================================================================================================
238	EXP_ID: eval_plan_012_dpo_1ep_fixed
239	STATUS: DONE
240	CREATED_AT: 2026-05-15T21:39:31.570Z
241	UPDATED_AT: 2026-05-15T21:39:31.570Z
242	CONCLUSION: killed
243	COMMAND: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/dpo_output_1ep/ --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/dpo_ced_1ep_fixed --no-quantize"
244	SPEC.server: rtx5090-4x
245	SPEC.gpu: ['cuda:0']
246	SPEC.pid: 258955
247	SPEC.log_path: ~/runs/faith-evidence-ie/eval_plan_012_dpo_1ep_fixed.log
248	SPEC.submitted_at: 2026-05-15T21:39:31.197Z
249	SPEC.submitted_via: submit_training_job
250	SPEC.backend: tmux
251	SPEC.account: root
252	
253	========================================================================================================================
254	EXP_ID: eval_plan_012_dpo_1ep_fixed_r2
255	STATUS: DONE
256	CREATED_AT: 2026-05-15T21:58:52.440Z
257	UPDATED_AT: 2026-05-15T23:44:56.586Z
258	CONCLUSION: negative
259	METRICS: {
260	  "rel_f1": 0.4034,
261	  "evi_f1": 0.8088,
262	  "edcr": 0.7139,
263	  "format_ok_rate": 0.999,
264	  "truncated_rate": 0.343,
265	  "predictions": 19107,
266	  "ign_f1": 0.4034,
267	  "precision": 0.3809,
268	  "recall": 0.4287,
269	  "vs_sft_delta": -0.0023,
270	  "note": "DPO 1ep matches SFT baseline. 1ep\u21923ep trajectory shows gradual decoupling (rel_f1\u2193 evi_f1\u2191), consistent with GRPO pattern. Ign-F1=F1 exact match needs investigation."
271	}
272	COMMAND: DPO 1ep re-eval with --sft_adapter (D064 fix)
273	SPEC.server: rtx5090-4x
274	SPEC.gpu: cuda:3
275	SPEC.pid: 262075
276	SPEC.log_path: ~/runs/faith-evidence-ie/eval_plan_012_dpo_1ep_fixed_r2.log
277	SPEC.submitted_at: 2026-05-15T21:58:52.150Z
278	SPEC.submitted_via: submit_training_job
279	SPEC.backend: tmux
280	SPEC.account: root
281	SPEC.data_path: /root/autodl-tmp/data/docred
282	SPEC.data_count: 0
283	SPEC.model_name: Qwen3-4B + SFT + DPO 1ep
284	SPEC.seed: 42
285	SPEC.checkpoint_source: plan_012_dpo_ced_3ep
286	SPEC.eval_data: docred_dev
287	SPEC.checkpoint_path: /root/autodl-tmp/dpo_ced_output/checkpoint-167
288	SPEC.wall_clock_seconds: 6197.9
289	SPEC.gpu_hours: 1.72
290	
291	========================================================================================================================
292	EXP_ID: eval_plan_012_dpo_ced_1ep
293	STATUS: DONE
294	CREATED_AT: 2026-05-15T20:22:11.752Z
295	UPDATED_AT: 2026-05-15T21:27:30.000Z
296	CONCLUSION: negative
297	METRICS: {
298	  "rel_f1": 0.0022,
299	  "ign_f1": 0.0022,
300	  "evi_f1": 0.75,
301	  "edcr": 0.9982,
302	  "num_preds": 19265,
303	  "format_ok": "981/985",
304	  "truncated": "358/985",
305	  "tp": 34,
306	  "inference_time_s": 3643
307	}
308	COMMAND: python -m freige.eval.inference --model_path /root/autodl-tmp/dpo_output_1ep/ --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/dpo_ced_1ep --no-quantize
309	SPEC.server: rtx5090-4x
310	SPEC.data_path: docred-dev
311	SPEC.data_count: 985
312	SPEC.model_name: Qwen3-4B + DPO-CED-1ep LoRA
313	SPEC.seed: 42
314	SPEC.checkpoint_source: /root/autodl-tmp/dpo_output_1ep/ (final, 167 steps = 1 epoch)
315	SPEC.eval_data: docred-dev
316	SPEC.gpu_id: 2
317	SPEC.parent: plan_012_dpo_ced_1ep
318	SPEC.hypothesis: DPO+CED 1ep checkpoint dev set evaluation: 验证 1ep 是否消除 3ep 过拟合 (rewards_acc=1.0, margins=9x), 对比 SFT baseline rel_f1=0.4057
319	
320	========================================================================================================================
321	EXP_ID: eval_plan_012_dpo_ced_ckpt400
322	STATUS: DONE
323	CREATED_AT: 2026-05-15T19:32:55.398Z
324	UPDATED_AT: 2026-05-15T19:37:31.477Z
325	CONCLUSION: failed
326	COMMAND: python -m freige.eval.inference --model_path /root/autodl-tmp/dpo_output/checkpoint-400 --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/dpo_ced_ckpt400 --no-quantize
327	SPEC.server: rtx5090-4x
328	SPEC.gpu: cuda:3
329	SPEC.pid: 242796
330	SPEC.log_path: ~/runs/faith-evidence-ie/eval_plan_012_dpo_ced_ckpt400.log
331	SPEC.submitted_at: 2026-05-15T19:32:55.107Z
332	SPEC.submitted_via: submit_training_job
333	SPEC.backend: tmux
334	SPEC.account: root
335	SPEC.data_path: /root/autodl-tmp/data/docred
336	SPEC.data_count: 985
337	SPEC.model_name: Qwen3-4B + DPO-CED LoRA (checkpoint-400)
338	SPEC.seed: 42
339	SPEC.checkpoint_source: /root/autodl-tmp/dpo_output/checkpoint-400
340	SPEC.eval_data: docred-dev
341	SPEC.log_file: ~/runs/faith-evidence-ie/eval_plan_012_dpo_ced_ckpt400.log
342	SPEC.parent: plan_012_dpo_ced
343	SPEC.wall_clock_seconds: 248.7
344	SPEC.gpu_hours: 0.07
345	
346	========================================================================================================================
347	EXP_ID: eval_plan_014_no_evidence
348	STATUS: DONE
349	CREATED_AT: 2026-05-15T23:17:32.011Z
350	UPDATED_AT: 2026-05-16T01:34:06.402Z
351	CONCLUSION: failed
352	COMMAND: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/sft_no_evidence_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/sft_no_evidence_noquant --no-quantize --no_evidence"
353	SPEC.server: rtx5090-4x
354	SPEC.gpu: ['cuda:2']
355	SPEC.pid: 283455
356	SPEC.log_path: ~/runs/faith-evidence-ie/eval_plan_014_no_evidence.log
357	SPEC.submitted_at: 2026-05-16T01:27:16.251Z
358	SPEC.submitted_via: submit_training_job
359	SPEC.backend: tmux
360	SPEC.account: root
361	SPEC.wall_clock_seconds: 33.8
362	SPEC.gpu_hours: 0.01
363	
364	========================================================================================================================
365	EXP_ID: eval_plan_014_no_evidence_r2
366	STATUS: DONE
367	CREATED_AT: 2026-05-16T01:34:45.302Z
368	UPDATED_AT: 2026-05-16T04:20:13.358Z
369	CONCLUSION: success
370	METRICS: {
371	  "rel_f1": 0.4876,
372	  "ign_f1": 0.4721,
373	  "evi_f1": 0,
374	  "edcr": 0,
375	  "evi_f1_joint": 0,
376	  "precision": 0.4901,
377	  "recall": 0.4851,
378	  "ign_precision": 0.4654,
379	  "ign_recall": 0.4791,
380	  "format_compliance": 0.993,
381	  "truncation_rate": 0.312,
382	  "n_predictions": 21181,
383	  "n_documents": 985
384	}
385	COMMAND: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_no_evidence_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/sft_no_evidence_noquant --no-quantize --no_evidence"
386	SPEC.server: rtx5090-4x
387	SPEC.gpu: ['cuda:0']
388	SPEC.pid: 288109
389	SPEC.log_path: ~/runs/faith-evidence-ie/eval_plan_014_no_evidence_r2.log
390	SPEC.submitted_at: 2026-05-16T02:27:53.107Z
391	SPEC.submitted_via: submit_training_job
392	SPEC.backend: tmux
393	SPEC.account: root
394	SPEC.checkpoint_path: /root/autodl-tmp/sft_no_evidence_output
395	SPEC.wall_clock_seconds: 6547.0
396	SPEC.gpu_hours: 1.82
397	
398	========================================================================================================================
399	EXP_ID: eval_rsft_ced_s43
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "e9ea2130-9d5c-4db9-9039-89b8c53addd2"
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
  "task_id": "aa0dedafabeeb8ab6",
  "tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "description": "Reading /tmp/4b_experiments_full.txt",
  "usage": {
    "total_tokens": 38038,
    "tool_uses": 11,
    "duration_ms": 65699
  },
  "last_tool_name": "Read",
  "uuid": "df6d3397-cf8d-4e55-a0d2-cc2a77cb5d82",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0"
}
```

---


### Tool call

_source line 46_

<details open><summary>🔧 Tool call — Read · `toolu_01STQA8VniwwuDUfFQNXyoBJ`</summary>

```json
{
  "file_path": "/tmp/4b_experiments_full.txt",
  "offset": 399,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "1417e6aa-8f3b-4b1d-b042-a4f91faf625f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0179LAJZFW4LpGNdxuvSGwDb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8909,
      "cache_read_input_tokens": 28890,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8909,
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

_source line 47 · 2026-05-18T22:03:28.813Z_

<details><summary>↩ Tool result · `toolu_01STQA8VniwwuDUfFQNXyoBJ`</summary>

```text
399	EXP_ID: eval_rsft_ced_s43
400	STATUS: DONE
401	CREATED_AT: 2026-05-16T01:30:37.978Z
402	UPDATED_AT: 2026-05-16T05:18:59.781Z
403	CONCLUSION: success
404	METRICS: {
405	  "rel_f1": 0.4601,
406	  "ign_f1": 0.4512,
407	  "precision": 0.4696,
408	  "recall": 0.4509,
409	  "evi_f1": 0.8063,
410	  "evi_precision": 0.8025,
411	  "evi_recall": 0.8101,
412	  "edcr": 0.6542,
413	  "evi_f1_joint": 0.3605,
414	  "format_ok_rate": 1,
415	  "n_truncated": 184,
416	  "n_predictions": 15051,
417	  "inference_time_seconds": 10768.2
418	}
419	COMMAND: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 43 --output_dir /root/autodl-tmp/eval_results/rsft_ced_s43 --no-quantize"
420	SPEC.server: rtx5090-4x
421	SPEC.gpu: ['cuda:1']
422	SPEC.pid: 286587
423	SPEC.log_path: ~/runs/faith-evidence-ie/eval_rsft_ced_s43.log
424	SPEC.submitted_at: 2026-05-16T02:13:11.138Z
425	SPEC.submitted_via: submit_training_job
426	SPEC.backend: tmux
427	SPEC.account: root
428	SPEC.checkpoint_path: /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510
429	SPEC.wall_clock_seconds: 11076.6
430	SPEC.gpu_hours: 3.08
431	
432	========================================================================================================================
433	EXP_ID: eval_rsft_ced_s45
434	STATUS: DONE
435	CREATED_AT: 2026-05-16T01:30:34.036Z
436	UPDATED_AT: 2026-05-16T05:43:12.975Z
437	CONCLUSION: success
438	METRICS: {
439	  "rel_f1": 0.4514,
440	  "ign_f1": 0.4416,
441	  "evi_f1": 0.8174,
442	  "rel_p": 0.4718,
443	  "rel_r": 0.4326,
444	  "edcr": 0.655,
445	  "evi_f1_joint": 0.3558,
446	  "n_truncated": 206,
447	  "format_ok_rate": 1
448	}
449	COMMAND: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_ced_s45/checkpoint-510 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 45 --output_dir /root/autodl-tmp/eval_results/rsft_ced_s45 --no-quantize"
450	SPEC.server: rtx5090-4x
451	SPEC.gpu: ['cuda:2']
452	SPEC.pid: 283838
453	SPEC.log_path: /root/runs/faith-evidence-ie/eval_rsft_ced_s45.log
454	SPEC.submitted_at: 2026-05-16T01:30:48.081Z
455	SPEC.submitted_via: submit_training_job
456	SPEC.backend: tmux
457	SPEC.account: root
458	SPEC.wall_clock_seconds: 10350.6
459	SPEC.gpu_hours: 2.88
460	SPEC.checkpoint_path: /root/autodl-tmp/rsft_output_ced_s45/checkpoint-510
461	
462	========================================================================================================================
463	EXP_ID: eval_sft_baseline_noquant
464	STATUS: DONE
465	CREATED_AT: 2026-05-15T18:38:33.128Z
466	UPDATED_AT: 2026-05-15T19:45:42.147Z
467	CONCLUSION: success
468	METRICS: {
469	  "rel_f1": 0.4106,
470	  "rel_precision": 0.4198,
471	  "rel_recall": 0.4019,
472	  "evi_f1": 0.8013,
473	  "evi_precision": 0.8005,
474	  "evi_recall": 0.8022,
475	  "evi_f1_joint": 0.3216,
476	  "edcr": 0.7039,
477	  "format_ok_rate": 0.998,
478	  "field_compliance_rate": 0.7066,
479	  "n_predictions": 16774,
480	  "n_truncated": 288,
481	  "n_documents": 985,
482	  "inference_time_seconds": 3677.9
483	}
484	COMMAND: python eval.py --model_path /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/eval_results/sft_baseline_noquant --batch_size 16 --max_new_tokens 1024 --split dev --seed 42
485	SPEC.server: rtx5090-4x
486	SPEC.gpu: ['cuda:1']
487	SPEC.pid: 237912
488	SPEC.log_path: ~/runs/faith-evidence-ie/eval_sft_baseline_noquant.log
489	SPEC.submitted_at: 2026-05-15T18:38:45.042Z
490	SPEC.submitted_via: submit_training_job
491	SPEC.backend: tmux
492	SPEC.account: root
493	SPEC.data_path: /root/autodl-tmp/data/docred
494	SPEC.data_count: 985
495	SPEC.model_name: Qwen3-4B + SFT LoRA (no quantization)
496	SPEC.seed: 42
497	SPEC.checkpoint_source: /root/autodl-tmp/sft_output
498	SPEC.eval_data: docred/dev (985 docs, 12275 triples)
499	SPEC.wall_clock_seconds: 3916.2
500	SPEC.gpu_hours: 1.09
501	SPEC.checkpoint_path: /root/autodl-tmp/eval_results/sft_baseline_noquant/
502	
503	========================================================================================================================
504	EXP_ID: grpo_bf16_g4_ckpt100_eval
505	STATUS: DONE
506	CREATED_AT: 2026-05-18T16:34:51.597Z
507	UPDATED_AT: 2026-05-18T20:08:50.166Z
508	CONCLUSION: success
509	METRICS: {
510	  "ign_f1": 0.4431,
511	  "f1": 0.4511,
512	  "evi_f1": 0.801,
513	  "evi_f1_joint": 0.3532,
514	  "EDCR": 0.6453,
515	  "format_compliance": 0.999,
516	  "field_compliance": 0.8142,
517	  "truncated": 182,
518	  "n_total": 985,
519	  "n_predictions": 15187,
520	  "inference_time_seconds": 11458.2
521	}
522	COMMAND: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=3 python -m freige.eval.inference --model_path /root/autodl-tmp/grpo_bf16_g4/checkpoint-100 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output/ --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/grpo_bf16_g4_ckpt100_eval"
523	SPEC.server: rtx5090-4x
524	SPEC.gpu: ['cuda:3']
525	SPEC.pid: 558467
526	SPEC.log_path: ~/runs/faith-evidence-ie/grpo_bf16_g4_ckpt100_eval.log
527	SPEC.submitted_at: 2026-05-18T16:35:15.818Z
528	SPEC.submitted_via: submit_training_job
529	SPEC.backend: tmux
530	SPEC.account: root
531	SPEC.data_path: /root/autodl-tmp/data/docred
532	SPEC.data_count: 985
533	SPEC.model_name: Qwen3-4B + SFT + GRPO-bf16-G4-ckpt100
534	SPEC.seed: 42
535	SPEC.checkpoint_source: wave1_grpo_bf16_g4
536	SPEC.eval_data: DocRED dev
537	SPEC.checkpoint_path: /root/autodl-tmp/eval_results/grpo_bf16_g4_ckpt100_eval
538	SPEC.wall_clock_seconds: 12814.3
539	SPEC.gpu_hours: 3.56
540	
541	========================================================================================================================
542	EXP_ID: grpo_bf16_g4_ckpt200_eval
543	STATUS: RUNNING
544	CREATED_AT: 2026-05-18T20:05:54.201Z
545	UPDATED_AT: 2026-05-18T20:09:44.868Z
546	COMMAND: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=3 python -m freige.eval.inference --model_path /root/autodl-tmp/grpo_bf16_g4/checkpoint-200 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output/ --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/grpo_bf16_g4_ckpt200_eval"
547	SPEC.server: rtx5090-4x
548	SPEC.gpu: ['cuda:3']
549	SPEC.pid: 571115
550	SPEC.log_path: ~/runs/faith-evidence-ie/grpo_bf16_g4_ckpt200_eval.log
551	SPEC.submitted_at: 2026-05-18T20:06:10.622Z
552	SPEC.submitted_via: submit_training_job
553	SPEC.backend: tmux
554	SPEC.account: root
555	SPEC.data_path: /root/autodl-tmp/data/docred
556	SPEC.data_count: 985
557	SPEC.model_name: Qwen3-4B + SFT + GRPO-bf16-G4-ckpt200
558	SPEC.seed: 42
559	SPEC.checkpoint_source: wave1_grpo_bf16_g4
560	SPEC.eval_data: DocRED dev
561	SPEC.checkpoint_path: /root/autodl-tmp/eval_results/grpo_bf16_g4_ckpt200_eval
562	
563	========================================================================================================================
564	EXP_ID: lead2_ckpt20_eval
565	STATUS: DONE
566	CREATED_AT: 2026-05-17T12:31:32.202Z
567	UPDATED_AT: 2026-05-17T15:27:15.598Z
568	CONCLUSION: success
569	METRICS: {
570	  "rel_f1": 0.4617,
571	  "ign_f1": 0.4533,
572	  "evi_f1": 0.8103,
573	  "evi_f1_joint": 0.3642,
574	  "edcr": 0.6465,
575	  "precision": 0.476,
576	  "recall": 0.4482,
577	  "format_ok": "985/985",
578	  "truncated": "187/985",
579	  "predictions": 14998
580	}
581	COMMAND: CUDA_VISIBLE_DEVICES=1 python -m freige.eval.inference --model_path /root/autodl-tmp/grpo_from_rsft_lead2_r2/checkpoint-20 --base_model /root/autodl-tmp/merged_sft_rsft_ced_s43 --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_outputs/lead2_ckpt20_eval
582	SPEC.server: rtx5090-4x
583	SPEC.gpu: 1
584	SPEC.model_name: Qwen3-4B (SFT+RSFT_CED_s43 merged + GRPO ckpt-20)
585	SPEC.data_path: /root/autodl-tmp/data/docred
586	SPEC.data_count: 985
587	SPEC.seed: 42
588	SPEC.checkpoint_source: /root/autodl-tmp/grpo_from_rsft_lead2_r2/checkpoint-20
589	SPEC.eval_data: docred_dev
590	SPEC.pid: 446829
591	SPEC.log_path: /root/autodl-tmp/logs/lead2_ckpt20_eval.log
592	
593	========================================================================================================================
594	EXP_ID: lead2_rsft_grpo_ced
595	STATUS: DONE
596	CREATED_AT: 2026-05-17T05:57:53.951Z
597	UPDATED_AT: 2026-05-17T06:06:36.130Z
598	CONCLUSION: failed
599	COMMAND: merge_sft_rsft.py then grpo_trainer --model_name merged_sft_rsft_ced_s43 --stage 3 --max_steps 50 --lr 1e-6 --G 8 --kl 0.01 --bf16 --ced=1.0 --f1=0.0 --format=0.5 --save_steps 10
600	SPEC.server: rtx5090-4x
601	SPEC.gpu: cuda:1
602	SPEC.pid: 418198
603	SPEC.log_path: ~/runs/faith-evidence-ie/lead2_rsft_grpo_ced.log
604	SPEC.submitted_at: 2026-05-17T05:57:53.332Z
605	SPEC.submitted_via: submit_training_job
606	SPEC.backend: tmux
607	SPEC.account: root
608	SPEC.data_path: /root/autodl-tmp/data/docred
609	SPEC.data_count: 3027
610	SPEC.model_name: Qwen3-4B (merged SFT+RSFT-s43)
611	SPEC.seed: 42
612	SPEC.checkpoint_source: /root/autodl-tmp/merged_sft_rsft_ced_s43
613	SPEC.eval_data: /root/autodl-tmp/data/docred/dev.json
614	SPEC.checkpoint_path: N/A
615	SPEC.failure_reason: docred_processor.py:129 load_dataset('thunlp/docred') failed - server offline
616	SPEC.wall_clock_seconds: 522.8
617	SPEC.gpu_hours: 0.15
618	
619	========================================================================================================================
620	EXP_ID: lead2_rsft_grpo_ced_r2
621	STATUS: DONE
622	CREATED_AT: 2026-05-17T06:23:56.474Z
623	UPDATED_AT: 2026-05-17T08:25:20.510Z
624	CONCLUSION: failed
625	COMMAND: python -m freige.training.grpo_trainer --model_name merged_sft_rsft_ced_s43 --data_dir /root/autodl-tmp/data/docred --stage 3 --max_steps 50 --lr 1e-6 --G 8 --kl 0.01 --bf16 --ced=1.0 --f1=0.0 --format=0.5 --save_steps 10
626	SPEC.server: rtx5090-4x
627	SPEC.gpu: cuda:2
628	SPEC.pid: 421806
629	SPEC.log_path: ~/runs/faith-evidence-ie/lead2_rsft_grpo_ced_r2.log
630	SPEC.submitted_at: 2026-05-17T06:24:47.600Z
631	SPEC.submitted_via: submit_training_job
632	SPEC.backend: tmux
633	SPEC.account: root
634	SPEC.data_path: /root/autodl-tmp/data/docred
635	SPEC.data_count: 3027
636	SPEC.model_name: Qwen3-4B (merged SFT+RSFT-s43)
637	SPEC.seed: 42
638	SPEC.checkpoint_source: /root/autodl-tmp/merged_sft_rsft_ced_s43
639	SPEC.eval_data: /root/autodl-tmp/data/docred/dev.json
640	SPEC.checkpoint_path: /root/autodl-tmp/grpo_from_rsft_lead2/checkpoint-30
641	SPEC.failure_reason: No space left on device at step 30/50 during checkpoint save
642	SPEC.wall_clock_seconds: 7232.9
643	SPEC.gpu_hours: 2.01
644	
645	========================================================================================================================
646	EXP_ID: mvp2_ced_reranker_poc
647	STATUS: DONE
648	CREATED_AT: 2026-05-15T07:55:03.414Z
649	UPDATED_AT: 2026-05-16T03:49:41.385Z
650	CONCLUSION: success
651	METRICS: {
652	  "ced_reranker_rel_f1": 0.486367,
653	  "ced_reranker_ign_f1": 0.473634,
654	  "ced_reranker_evi_f1": 0.8188,
655	  "oracle_rel_f1": 0.623746,
656	  "oracle_ign_f1": 0.612518,
657	  "random_rel_f1": 0.453783,
658	  "random_ign_f1": 0.439677
659	}
660	COMMAND: python /root/autodl-tmp/freige/eval/ced_reranker.py (N=8, CED scoring, 985 docs)
661	SPEC.server: rtx5090-4x
662	SPEC.data_path: /root/autodl-tmp/data/docred
663	SPEC.data_count: 985
664	SPEC.model_name: Qwen3-4B + SFT (greedy N=8 + CED reranker)
665	SPEC.seed: 42
666	SPEC.pid: 178050
667	SPEC.checkpoint_path: N/A
668	SPEC.log_path: ~/runs/faith-evidence-ie/mvp2_ced_reranker_poc.log
669	
670	========================================================================================================================
671	EXP_ID: mvp2_diversity_probe
672	STATUS: DONE
673	CREATED_AT: 2026-05-15T00:02:19.966Z
674	UPDATED_AT: 2026-05-15T01:31:34.495Z
675	CONCLUSION: success
676	METRICS: {
677	  "unique_triples_t07": 5,
678	  "unique_triples_t10": 8,
679	  "jaccard_t07": 0.17,
680	  "jaccard_t10": 0.051,
681	  "format_ok_rate_t07": 0.5,
682	  "format_ok_rate_t10": 0.438,
683	  "n_samples": 3,
684	  "n_generations": 8,
685	  "note": "unique_triples_t07 corrected from 7 to 5.0 (mean). Reviewer: format_ok ~34% after fix, 'diversity' was JSON key name variants not semantic diversity"
686	}
687	COMMAND: python diversity_probe.py (已完成, 状态修正)
688	SPEC.server: rtx5090-4x
689	SPEC.gpu: ['cuda:2']
690	SPEC.data_path: /root/autodl-tmp/data/docred
691	SPEC.data_count: 3
692	SPEC.model_name: Qwen3-4B + SFT adapter
693	SPEC.seed: 42
694	SPEC.checkpoint_path: N/A (probe only)
695	SPEC.log_path: N/A (probe only)
696	
697	========================================================================================================================
698	EXP_ID: mvp2_eval_ced_kl001_r4_ckpt10
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "81d67e14-c4cf-429d-98ae-c8a64ac7c802"
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
  "task_id": "aa0dedafabeeb8ab6",
  "tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "description": "Reading /tmp/4b_experiments_full.txt",
  "usage": {
    "total_tokens": 44303,
    "tool_uses": 12,
    "duration_ms": 69427
  },
  "last_tool_name": "Read",
  "uuid": "a0dead28-80eb-4f3e-a55f-28409a05b514",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0"
}
```

---


### Tool call

_source line 49_

<details open><summary>🔧 Tool call — Read · `toolu_017VEm1B68kxmQxzJZQ3f9QN`</summary>

```json
{
  "file_path": "/tmp/4b_experiments_full.txt",
  "offset": 698,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "c54ee101-e285-4064-969a-ec1b80b35338",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CsUsnWFeDwyAQsKvJiBeLt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6227,
      "cache_read_input_tokens": 37799,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6227,
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

_source line 50 · 2026-05-18T22:03:32.540Z_

<details><summary>↩ Tool result · `toolu_017VEm1B68kxmQxzJZQ3f9QN`</summary>

```text
698	EXP_ID: mvp2_eval_ced_kl001_r4_ckpt10
699	STATUS: DONE
700	CREATED_AT: 2026-05-14T17:59:08.638Z
701	UPDATED_AT: 2026-05-14T19:14:08.763Z
702	CONCLUSION: success
703	METRICS: {
704	  "rel_f1": 0.00296,
705	  "rel_precision": 0.00314,
706	  "rel_recall": 0.0028,
707	  "evi_f1": 0.72,
708	  "evi_precision": 0.6429,
709	  "evi_recall": 0.8182,
710	  "edcr": 0.9983,
711	  "n_parseable": 984,
712	  "n_truncated": 24,
713	  "n_predictions": 11621,
714	  "tp": 34,
715	  "pred_count": 10839,
716	  "gold_count": 12151,
717	  "inference_time_seconds": 5211.4
718	}
719	COMMAND: CUDA_VISIBLE_DEVICES=2 python -m freige.eval.batch_eval --exp_dir /root/autodl-tmp/grpo_ced_kl001 --sft_adapter /root/autodl-tmp/sft_output --output_dir /root/autodl-tmp/eval_results/grpo_ced_kl001 --checkpoints 10 --quantize
720	SPEC.server: rtx5090-4x
721	SPEC.gpu: ['cuda:2']
722	SPEC.pid: 78857
723	SPEC.log_path: ~/runs/faith-evidence-ie/mvp2_eval_ced_kl001_r4_ckpt10.log
724	SPEC.data_path: /root/autodl-tmp/data/docred
725	SPEC.data_count: {'dev': 985}
726	SPEC.model_name: Qwen3-4B
727	SPEC.seed: 42
728	SPEC.hypothesis: Early checkpoint eval (step 10) of ced_kl001_r4 — part of multi-checkpoint trend analysis for MVP-2 judgment
729	SPEC.parent: mvp2_grpo_ced_kl001_r4
730	SPEC.checkpoint_source: /root/autodl-tmp/grpo_ced_kl001/checkpoint-10
731	SPEC.eval_data: /root/autodl-tmp/data/docred/dev.json
732	
733	========================================================================================================================
734	EXP_ID: mvp2_eval_ced_kl001_r4_ckpt90
735	STATUS: DONE
736	CREATED_AT: 2026-05-14T18:18:13.270Z
737	UPDATED_AT: 2026-05-14T19:17:36.777Z
738	CONCLUSION: killed
739	COMMAND: python -m freige.eval.batch_eval --exp_dir /root/autodl-tmp/grpo_ced_kl001 --checkpoints 90 --quantize
740	SPEC.server: rtx5090-4x
741	SPEC.gpu: ['cuda:3']
742	SPEC.pid: unknown
743	SPEC.log_path: ~/runs/faith-evidence-ie/mvp2_eval_ced_kl001_r4_ckpt90.log
744	SPEC.submitted_at: 2026-05-14T18:18:20.407Z
745	SPEC.submitted_via: submit_training_job
746	SPEC.backend: tmux
747	SPEC.account: root
748	SPEC.data_path: /root/autodl-tmp/data/docred
749	SPEC.data_count: 985
750	SPEC.model_name: Qwen3-4B + SFT + GRPO ced_kl001 step-90
751	SPEC.seed: 42
752	SPEC.checkpoint_source: /root/autodl-tmp/grpo_ced_kl001/checkpoint-90
753	SPEC.eval_data: /root/autodl-tmp/data/docred/dev.json
754	SPEC.wall_clock_seconds: 3556.4
755	SPEC.gpu_hours: 0.99
756	
757	========================================================================================================================
758	EXP_ID: mvp2_eval_ced_kl001_r4_early
759	STATUS: DONE
760	CREATED_AT: 2026-05-14T17:12:53.581Z
761	UPDATED_AT: 2026-05-14T18:31:18.065Z
762	CONCLUSION: negative
763	METRICS: {
764	  "f1": 0.1563,
765	  "ign_f1": 0.1563,
766	  "evi_f1": 0.5643,
767	  "edcr": 0.8858,
768	  "precision": 0.2356,
769	  "recall": 0.1169,
770	  "evi_precision": 0.4864,
771	  "evi_recall": 0.6721,
772	  "format_ok_rate": 0.999,
773	  "n_parseable": 984,
774	  "n_truncated": 11,
775	  "n_predictions": 9250,
776	  "tp": 1421,
777	  "pred_count": 6032,
778	  "gold_count": 12151
779	}
780	COMMAND: CUDA_VISIBLE_DEVICES=1 python -m freige.eval.batch_eval --exp_dir /root/autodl-tmp/grpo_ced_kl001 --sft_adapter /root/autodl-tmp/sft_output --output_dir /root/autodl-tmp/eval_results/grpo_ced_kl001 --checkpoints 50 --quantize
781	SPEC.server: rtx5090-4x
782	SPEC.gpu: ['cuda:1']
783	SPEC.pid: 75581
784	SPEC.log_path: /tmp/eval_ced_kl001_ckpt50.log
785	SPEC.data_path: /root/autodl-tmp/data/docred
786	SPEC.data_count: {'dev': 985}
787	SPEC.model_name: Qwen3-4B
788	SPEC.seed: 42
789	SPEC.hypothesis: Early eval of ced_kl001_r4 best-reward checkpoint (step 50, reward=1.1009) to get early signal on CED vs SFT baseline
790	SPEC.parent: mvp2_grpo_ced_kl001_r4
791	SPEC.checkpoint_source: /root/autodl-tmp/grpo_ced_kl001/checkpoint-50
792	SPEC.eval_data: /root/autodl-tmp/data/docred/dev.json
793	
794	========================================================================================================================
795	EXP_ID: mvp2_eval_ced_kl001_r4_high
796	STATUS: DONE
797	CREATED_AT: 2026-05-14T18:19:07.637Z
798	UPDATED_AT: 2026-05-14T19:47:58.282Z
799	CONCLUSION: failed
800	METRICS: {
801	  "checkpoint_60": {
802	    "rel_f1": 0.1467,
803	    "ign_f1": 0.1467,
804	    "precision": 0.1909,
805	    "recall": 0.1192,
806	    "evi_f1": 0.5763,
807	    "edcr": 0.9062,
808	    "pred_count": 10041,
809	    "gold_count": 12151,
810	    "n_truncated": 16,
811	    "format_ok_rate": 1
812	  },
813	  "note": "Only ckpt-60 completed. Process died during ckpt-70 inference at 8% (5/62 batch). ckpt-80/90 never started."
814	}
815	COMMAND: python -m freige.eval.batch_eval --exp_dir /root/autodl-tmp/grpo_ced_kl001 --sft_adapter /root/autodl-tmp/sft_output --output_dir /root/autodl-tmp/eval_results/grpo_ced_kl001 --checkpoints 60,70,80,90 --quantize --resume
816	SPEC.server: rtx5090-4x
817	SPEC.gpu: ['cuda:3']
818	SPEC.pid: 81962
819	SPEC.data_path: /root/autodl-tmp/data/docred
820	SPEC.data_count: 985
821	SPEC.model_name: Qwen3-4B + SFT + GRPO ced_kl001
822	SPEC.seed: 42
823	SPEC.checkpoint_source: /root/autodl-tmp/grpo_ced_kl001
824	SPEC.eval_data: DocRED dev set
825	
826	========================================================================================================================
827	EXP_ID: mvp2_eval_ced_kl001_r4_multi
828	STATUS: DONE
829	CREATED_AT: 2026-05-14T17:59:22.291Z
830	UPDATED_AT: 2026-05-14T21:27:25.338Z
831	CONCLUSION: killed
832	METRICS: {
833	  "checkpoint-10": {
834	    "f1": 0.003,
835	    "ign_f1": 0.003,
836	    "evi_f1": 0.72,
837	    "edcr": 0.9983,
838	    "format_ok_rate": 0.999
839	  },
840	  "checkpoint-20": {
841	    "f1": 0.0088,
842	    "ign_f1": 0.0088,
843	    "evi_f1": 0.423,
844	    "edcr": 0.9954,
845	    "format_ok_rate": 0.999
846	  },
847	  "checkpoint-30": {
848	    "f1": 0.0338,
849	    "ign_f1": 0.0338,
850	    "evi_f1": 0.5889,
851	    "edcr": 0.9798,
852	    "format_ok_rate": 1
853	  },
854	  "checkpoint-50": {
855	    "f1": 0.1563,
856	    "ign_f1": 0.1563,
857	    "evi_f1": 0.5643,
858	    "edcr": 0.8858,
859	    "format_ok_rate": 0.999
860	  },
861	  "checkpoint-60": {
862	    "f1": 0.1467,
863	    "ign_f1": 0.1467,
864	    "evi_f1": 0.5763,
865	    "edcr": 0.9062,
866	    "format_ok_rate": 1
867	  },
868	  "checkpoint-90": {
869	    "f1": 0.2108,
870	    "ign_f1": 0.2108,
871	    "evi_f1": 0.5666,
872	    "edcr": 0.8584,
873	    "format_ok_rate": 1
874	  }
875	}
876	COMMAND: CUDA_VISIBLE_DEVICES=2 python -m freige.eval.batch_eval --exp_dir /root/autodl-tmp/grpo_ced_kl001 --sft_adapter /root/autodl-tmp/sft_output --output_dir /root/autodl-tmp/eval_results/grpo_ced_kl001 --checkpoints 10,20,30,40,60,70,80 --quantize --resume
877	SPEC.server: rtx5090-4x
878	SPEC.gpu: ['cuda:2']
879	SPEC.pid: 78850
880	SPEC.log_path: ~/runs/faith-evidence-ie/mvp2_eval_ced_kl001_r4_multi.log
881	SPEC.data_path: /root/autodl-tmp/data/docred
882	SPEC.data_count: {'dev': 985}
883	SPEC.model_name: Qwen3-4B
884	SPEC.seed: 42
885	SPEC.hypothesis: Multi-checkpoint eval of ced_kl001_r4 (steps 10-80) to get full reward→eval correlation and identify best checkpoint for MVP-2 judgment
886	SPEC.parent: mvp2_grpo_ced_kl001_r4
887	SPEC.checkpoint_source: /root/autodl-tmp/grpo_ced_kl001
888	SPEC.eval_data: /root/autodl-tmp/data/docred/dev.json
889	
890	========================================================================================================================
891	EXP_ID: mvp2_eval_ced_kl001_r4_step100
892	STATUS: DONE
893	CREATED_AT: 2026-05-14T18:08:31.821Z
894	UPDATED_AT: 2026-05-14T19:41:30.318Z
895	CONCLUSION: negative
896	METRICS: {
897	  "rel_f1": 0.2167,
898	  "ign_f1": 0.2167,
899	  "precision": 0.2849,
900	  "recall": 0.1749,
901	  "evi_f1": 0.5746,
902	  "evi_precision": 0.5244,
903	  "evi_recall": 0.6353,
904	  "edcr": 0.8539,
905	  "pred_count": 7460,
906	  "gold_count": 12151,
907	  "tp": 2125,
908	  "n_truncated": 21,
909	  "format_ok_rate": 1
910	}
911	COMMAND: python -m freige.eval.batch_eval --exp_dir /root/autodl-tmp/grpo_ced_kl001 --sft_adapter /root/autodl-tmp/sft_output --output_dir /root/autodl-tmp/eval_results/grpo_ced_kl001_step100 --checkpoints 100 --quantize
912	SPEC.server: rtx5090-4x
913	SPEC.gpu: ['cuda:0']
914	SPEC.pid: 80789
915	SPEC.log_path: ~/runs/faith-evidence-ie/mvp2_eval_ced_kl001_r4_step100.log
916	SPEC.submitted_at: 2026-05-14T18:09:02.064Z
917	SPEC.submitted_via: submit_training_job
918	SPEC.backend: tmux
919	SPEC.account: root
920	SPEC.data_path: /root/autodl-tmp/data/docred
921	SPEC.model_name: Qwen3-4B + SFT adapter + GRPO ced_kl001 step-100
922	SPEC.checkpoint_source: /root/autodl-tmp/grpo_ced_kl001/checkpoint-100
923	SPEC.eval_data: DocRED dev set
924	SPEC.data_count: 998
925	SPEC.seed: 42
926	SPEC.checkpoint_path: /root/autodl-tmp/grpo_ced_kl001/checkpoint-100
927	SPEC.wall_clock_seconds: 5458.4
928	SPEC.gpu_hours: 1.52
929	
930	========================================================================================================================
931	EXP_ID: mvp2_eval_ced_kl001_r4_step90
932	STATUS: DONE
933	CREATED_AT: 2026-05-14T18:19:58.623Z
934	UPDATED_AT: 2026-05-14T20:01:45.201Z
935	CONCLUSION: negative
936	METRICS: {
937	  "rel_f1": 0.2108,
938	  "ign_f1": 0.2108,
939	  "evi_f1": 0.5666,
940	  "edcr": 0.8584,
941	  "pred_count": 11160,
942	  "n_truncated": 22,
943	  "format_ok_rate": 1,
944	  "n_documents": 985
945	}
946	COMMAND: bash -c "source /etc/network_turbo && ... && python -m freige.eval.batch_eval --exp_dir /root/autodl-tmp/grpo_ced_kl001 --sft_adapter /root/autodl-tmp/sft_output --output_dir /root/autodl-tmp/eval_results/grpo_ced_kl001 --checkpoints 90 --quantize"
947	SPEC.server: rtx5090-4x
948	SPEC.gpu: ['cuda:1']
949	SPEC.pid: 83207
950	SPEC.data_path: /root/autodl-tmp/data/docred
951	SPEC.data_count: 985
952	SPEC.model_name: Qwen3-4B + SFT + GRPO ced_kl001 step-90
953	SPEC.seed: 42
954	SPEC.checkpoint_source: /root/autodl-tmp/grpo_ced_kl001/checkpoint-90
955	SPEC.eval_data: DocRED dev set
956	SPEC.checkpoint_path: /root/autodl-tmp/grpo_ced_kl001/checkpoint-90
957	SPEC.log_path: ~/runs/faith-evidence-ie/mvp2_eval_ced_kl001_r4_step90.log
958	
959	========================================================================================================================
960	EXP_ID: mvp2_eval_lr5e6_r1_ckpt100
961	STATUS: DONE
962	CREATED_AT: 2026-05-14T23:00:57.035Z
963	UPDATED_AT: 2026-05-15T01:30:01.493Z
964	CONCLUSION: negative
965	METRICS: {
966	  "rel_f1": 0.0138,
967	  "rel_precision": 0.0132,
968	  "rel_recall": 0.0144,
969	  "ign_f1": 0.0138,
970	  "evi_f1": 0.8504,
971	  "evi_precision": 0.9256,
972	  "evi_recall": 0.7866,
973	  "edcr": 0.9876,
974	  "format_ok_rate": 0.999,
975	  "field_compliance_rate": 0.8162,
976	  "evidence_format_rate": 0.8162,
977	  "tp": 175,
978	  "pred_count": 13300,
979	  "gold_count": 12151,
980	  "n_predictions": 15498,
981	  "n_truncated": 181,
982	  "n_documents": 985,
983	  "n_parseable": 984,
984	  "inference_time_seconds": 5901.7
985	}
986	COMMAND: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.eval.inference --model_path /root/autodl-tmp/grpo_ced_lr5e6/checkpoint-100 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/lr5e6_r1_ckpt100/checkpoint-100 --quantize"
987	SPEC.server: rtx5090-4x
988	SPEC.gpu: ['cuda:3']
989	SPEC.pid: 117635
990	SPEC.log_path: ~/runs/faith-evidence-ie/mvp2_eval_lr5e6_r1_ckpt100.log
991	SPEC.submitted_at: 2026-05-14T23:39:51.199Z
992	SPEC.submitted_via: submit_training_job
993	SPEC.backend: tmux
994	SPEC.account: root
995	SPEC.wall_clock_seconds: 6160.9
996	SPEC.gpu_hours: 1.71
997	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "df1a297e-9bda-429a-8a19-44fc2dc9b874"
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
  "task_id": "aa0dedafabeeb8ab6",
  "tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "description": "Reading /tmp/4b_experiments_full.txt",
  "usage": {
    "total_tokens": 49901,
    "tool_uses": 13,
    "duration_ms": 74106
  },
  "last_tool_name": "Read",
  "uuid": "6b331c0c-1426-43ac-8605-209fbff4077e",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0"
}
```

---


### Tool call

_source line 52_

<details open><summary>🔧 Tool call — Read · `toolu_01KRN2Jo5rV3u5hhJyiAqiXs`</summary>

```json
{
  "file_path": "/tmp/4b_experiments_full.txt",
  "offset": 997,
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "f14e166c-f424-4a31-8a3b-a7406b208d3f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W4EmPh7oabSkZSku96VnjK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5560,
      "cache_read_input_tokens": 44026,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5560,
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

_source line 53 · 2026-05-18T22:03:37.235Z_

<details><summary>↩ Tool result · `toolu_01KRN2Jo5rV3u5hhJyiAqiXs`</summary>

```text
997	
998	========================================================================================================================
999	EXP_ID: mvp2_eval_lr5e6_r1_ckpt20
1000	STATUS: DONE
1001	CREATED_AT: 2026-05-14T20:44:21.167Z
1002	UPDATED_AT: 2026-05-14T22:12:16.372Z
1003	CONCLUSION: negative
1004	METRICS: {
1005	  "rel_f1": 0.0077,
1006	  "rel_precision": 0.0071,
1007	  "rel_recall": 0.0084,
1008	  "evi_f1": 0.628,
1009	  "evi_precision": 0.855,
1010	  "evi_recall": 0.496,
1011	  "edcr": 0.993,
1012	  "format_ok_rate": 0.991,
1013	  "field_compliance_rate": 0.399,
1014	  "pred_count": 14440,
1015	  "gold_count": 12151,
1016	  "tp": 102,
1017	  "n_truncated": 587,
1018	  "inference_time_seconds": 6370.4
1019	}
1020	COMMAND: bash /root/autodl-tmp/scripts/eval_lr5e6_ckpt20.sh
1021	SPEC.server: rtx5090-4x
1022	SPEC.gpu: ['cuda:1']
1023	SPEC.account: root
1024	SPEC.pid: 96500
1025	SPEC.data_path: /root/autodl-tmp/data/docred/dev.json
1026	SPEC.data_count: 985
1027	SPEC.model_name: Qwen3-4B + SFT + GRPO lr5e6 ckpt-20
1028	SPEC.seed: 42
1029	SPEC.checkpoint_source: /root/autodl-tmp/grpo_ced_lr5e6/checkpoint-20
1030	SPEC.eval_data: /root/autodl-tmp/data/docred/dev.json
1031	SPEC.log_path: /tmp/eval_lr5e6_ckpt20.log
1032	
1033	========================================================================================================================
1034	EXP_ID: mvp2_eval_lr5e6_r1_ckpt40
1035	STATUS: DONE
1036	CREATED_AT: 2026-05-14T21:25:00.579Z
1037	UPDATED_AT: 2026-05-14T21:43:33.438Z
1038	CONCLUSION: failed
1039	COMMAND: bash /root/autodl-tmp/scripts/eval_lr5e6_ckpt40.sh
1040	SPEC.server: rtx5090-4x
1041	SPEC.gpu: ['cuda:2']
1042	SPEC.pid: 101842
1043	SPEC.data_path: /root/autodl-tmp/data/docred/dev.json
1044	SPEC.data_count: 985
1045	SPEC.model_name: Qwen3-4B + SFT + GRPO lr5e6 ckpt-40
1046	SPEC.seed: 42
1047	SPEC.checkpoint_source: /root/autodl-tmp/grpo_ced_lr5e6/checkpoint-40
1048	SPEC.eval_data: /root/autodl-tmp/data/docred/dev.json
1049	SPEC.log_path: /tmp/eval_lr5e6_ckpt40.log
1050	SPEC.account: root
1051	
1052	========================================================================================================================
1053	EXP_ID: mvp2_eval_lr5e6_r1_ckpt40_r2
1054	STATUS: DONE
1055	CREATED_AT: 2026-05-14T21:41:34.558Z
1056	UPDATED_AT: 2026-05-14T23:11:56.267Z
1057	CONCLUSION: negative
1058	METRICS: {
1059	  "rel_f1": 0.0071,
1060	  "precision": 0.0066,
1061	  "recall": 0.0078,
1062	  "evi_f1": 0.7584,
1063	  "evi_precision": 0.9113,
1064	  "evi_recall": 0.6494,
1065	  "edcr": 0.9942,
1066	  "format_ok_rate": 0.9939,
1067	  "field_compliance_rate": 0.5675,
1068	  "pred_count": 14434,
1069	  "gold_count": 12151,
1070	  "tp": 95,
1071	  "n_truncated": 424,
1072	  "inference_time_seconds": 6152
1073	}
1074	COMMAND: CUDA_VISIBLE_DEVICES=2 python -m freige.eval.inference
1075	SPEC.server: rtx5090-4x
1076	SPEC.gpu: ['cuda:2']
1077	SPEC.account: root
1078	SPEC.pid: 101842
1079	SPEC.data_path: /root/autodl-tmp/data/docred/dev.json
1080	SPEC.data_count: 985
1081	SPEC.model_name: Qwen3-4B + SFT + GRPO lr5e6 ckpt-40
1082	SPEC.seed: 42
1083	SPEC.checkpoint_source: /root/autodl-tmp/grpo_ced_lr5e6/checkpoint-40
1084	SPEC.eval_data: /root/autodl-tmp/data/docred/dev.json
1085	SPEC.log_path: /tmp/eval_lr5e6_ckpt40.log
1086	SPEC.checkpoint_path: /root/autodl-tmp/grpo_ced_lr5e6/checkpoint-40
1087	SPEC.conclusion: negative
1088	SPEC.metrics: {'f1': 0.007146887342486364, 'ign_f1': 0.007146887342486364, 'precision': 0.0065816821393931, 'recall': 0.007818286560776891, 'evi_f1': 0.7583892617449665, 'edcr': 0.9942045337983383, 'format_ok_rate': 0.9939086294416244, 'tp': 95, 'pred_count': 14434, 'gold_count': 12151, 'n_truncated': 424, 'inference_time_seconds': 6152.4}
1089	SPEC.result_dir: /root/autodl-tmp/eval_results/lr5e6_r1_ckpt40/checkpoint-40
1090	
1091	========================================================================================================================
1092	EXP_ID: mvp2_eval_lr5e6_r1_ckpt60_r2
1093	STATUS: DONE
1094	CREATED_AT: 2026-05-14T22:27:56.124Z
1095	UPDATED_AT: 2026-05-15T00:07:56.895Z
1096	CONCLUSION: negative
1097	METRICS: {
1098	  "rel_f1": 0.0093,
1099	  "precision": 0.0085,
1100	  "recall": 0.0103,
1101	  "evi_f1": 0.81,
1102	  "edcr": 0.993,
1103	  "format_ok_rate": 0.998,
1104	  "pred_count": 14626,
1105	  "gold_count": 12151,
1106	  "tp": 125,
1107	  "inference_time_seconds": 6152
1108	}
1109	COMMAND: CUDA_VISIBLE_DEVICES=1 python -m freige.eval.inference --model_path /root/autodl-tmp/grpo_ced_lr5e6/checkpoint-60 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/grpo_ced_lr5e6_ckpt60 --quantize
1110	SPEC.data_path: /root/autodl-tmp/data/docred/dev.json
1111	SPEC.data_count: 985
1112	SPEC.model_name: Qwen3-4B + SFT + GRPO lr5e6 ckpt-60
1113	SPEC.seed: 42
1114	SPEC.checkpoint_source: /root/autodl-tmp/grpo_ced_lr5e6/checkpoint-60
1115	SPEC.eval_data: /root/autodl-tmp/data/docred/dev.json
1116	SPEC.server: rtx5090-4x
1117	SPEC.gpu: ['cuda:1']
1118	SPEC.pid: 108185
1119	SPEC.log_path: ~/runs/faith-evidence-ie/mvp2_eval_lr5e6_r1_ckpt60_r2.log
1120	SPEC.account: root
1121	SPEC.backend: tmux
1122	SPEC.checkpoint_path: /root/autodl-tmp/eval_results/grpo_ced_lr5e6_ckpt60/metrics.json
1123	
1124	========================================================================================================================
1125	EXP_ID: mvp2_eval_lr5e6_r1_ckpt80
1126	STATUS: DONE
1127	CREATED_AT: 2026-05-14T22:25:45.043Z
1128	UPDATED_AT: 2026-05-15T01:02:32.508Z
1129	CONCLUSION: negative
1130	METRICS: {
1131	  "rel_f1": 0.0116,
1132	  "ign_f1": 0.0116,
1133	  "precision": 0.0109,
1134	  "recall": 0.0124,
1135	  "evi_f1": 0.828,
1136	  "evi_precision": 0.928,
1137	  "evi_recall": 0.748,
1138	  "edcr": 0.993,
1139	  "format_ok_rate": 0.999,
1140	  "field_compliance_rate": 0.788,
1141	  "pred_count": 13828,
1142	  "gold_count": 12151,
1143	  "n_truncated": 210,
1144	  "inference_time_seconds": 6099
1145	}
1146	COMMAND: CUDA_VISIBLE_DEVICES=2 python -m freige.eval.inference --model_path /root/autodl-tmp/grpo_ced_lr5e6/checkpoint-80 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/lr5e6_r1_ckpt80/checkpoint-80 --quantize
1147	SPEC.data_path: /root/autodl-tmp/data/docred/dev.json
1148	SPEC.data_count: 985
1149	SPEC.model_name: Qwen3-4B + SFT + GRPO lr5e6 ckpt-80
1150	SPEC.seed: 42
1151	SPEC.checkpoint_source: /root/autodl-tmp/grpo_ced_lr5e6/checkpoint-80
1152	SPEC.eval_data: /root/autodl-tmp/data/docred/dev.json
1153	SPEC.server: rtx5090-4x
1154	SPEC.gpu: ['cuda:2']
1155	SPEC.pid: 111731
1156	SPEC.account: root
1157	SPEC.log_path: /tmp/eval_lr5e6_ckpt80.log
1158	SPEC.checkpoint_path: /root/autodl-tmp/eval_results/lr5e6_r1_ckpt80/checkpoint-80/
1159	
1160	========================================================================================================================
1161	EXP_ID: mvp2_eval_lr5e6_rp_r2_ckpt20
1162	STATUS: DONE
1163	CREATED_AT: 2026-05-14T21:44:56.448Z
1164	UPDATED_AT: 2026-05-14T22:06:40.812Z
1165	CONCLUSION: killed
1166	COMMAND: CUDA_VISIBLE_DEVICES=3 python eval rp_r2 ckpt-20
1167	SPEC.server: rtx5090-4x
1168	SPEC.gpu: ['cuda:3']
1169	SPEC.pid: 103825
1170	SPEC.data_path: /root/autodl-tmp/data/docred/dev.json
1171	SPEC.data_count: 985
1172	SPEC.model_name: Qwen3-4B + SFT + GRPO lr5e6+recall_penalty ckpt-20
1173	SPEC.seed: 42
1174	SPEC.checkpoint_source: /root/autodl-tmp/grpo_ced_lr5e6_rp/checkpoint-20
1175	SPEC.eval_data: /root/autodl-tmp/data/docred/dev.json
1176	
1177	========================================================================================================================
1178	EXP_ID: mvp2_eval_rsft_r1
1179	STATUS: DONE
1180	CREATED_AT: 2026-05-15T09:40:47.529Z
1181	UPDATED_AT: 2026-05-15T13:27:31.402Z
1182	CONCLUSION: success
1183	METRICS: {
1184	  "rel_f1": 0.4449,
1185	  "evi_f1": 0.8187,
1186	  "evi_f1_joint": 0.3468,
1187	  "evi_f1_joint_P": 0.3515,
1188	  "evi_f1_joint_R": 0.3423,
1189	  "edcr": 0.6565,
1190	  "num_preds": 15307,
1191	  "sft_baseline_rel_f1": 0.4057,
1192	  "sft_baseline_evi_f1": 0.7979,
1193	  "delta_rel_f1": 0.0392,
1194	  "delta_evi_f1": 0.0208,
1195	  "delta_evi_f1_joint": 0.0351,
1196	  "mvp2_pass": true
1197	}
1198	COMMAND: python -m freige.eval.inference --no-quantize (r1 checkpoint on cuda:2)
1199	SPEC.server: rtx5090-4x
1200	SPEC.data_path: /root/autodl-tmp/data/docred
1201	SPEC.data_count: 985
1202	SPEC.model_name: Qwen3-4B + SFT + RSFT r1
1203	SPEC.seed: 42
1204	SPEC.checkpoint_source: /root/autodl-tmp/rsft_output
1205	SPEC.eval_data: /root/autodl-tmp/data/docred/dev.json
1206	SPEC.pid: 186329
1207	SPEC.checkpoint_path: /root/autodl-tmp/rsft_output
1208	SPEC.log_path: /root/autodl-tmp/eval_results/rsft_r1/eval.log
1209	
1210	========================================================================================================================
1211	EXP_ID: mvp2_eval_rsft_r2a
1212	STATUS: DONE
1213	CREATED_AT: 2026-05-15T09:42:57.684Z
1214	UPDATED_AT: 2026-05-15T13:27:32.756Z
1215	CONCLUSION: success
1216	METRICS: {
1217	  "rel_f1": 0.4494,
1218	  "ign_f1": 0.4494,
1219	  "evi_f1": 0.8108,
1220	  "evi_f1_joint": 0.3509,
1221	  "evi_f1_joint_P": 0.3423,
1222	  "evi_f1_joint_R": 0.3599,
1223	  "edcr": 0.6641,
1224	  "precision": 0.4512,
1225	  "recall": 0.4475,
1226	  "evi_precision": 0.8143,
1227	  "evi_recall": 0.8073,
1228	  "format_ok_rate": 1,
1229	  "n_predictions": 15482,
1230	  "n_truncated": 208,
1231	  "inference_time_s": 5967.2,
1232	  "delta_evi_f1_joint": 0.0392
1233	}
1234	COMMAND: python -m freige.eval.inference --no-quantize (r2a checkpoint on cuda:1)
1235	SPEC.server: rtx5090-4x
1236	SPEC.data_path: /root/autodl-tmp/data/docred
1237	SPEC.data_count: 985
1238	SPEC.model_name: Qwen3-4B + SFT + RSFT r2a
1239	SPEC.seed: 42
1240	SPEC.checkpoint_source: /root/autodl-tmp/rsft_output_r2a
1241	SPEC.eval_data: /root/autodl-tmp/data/docred/dev.json
1242	
1243	========================================================================================================================
1244	EXP_ID: mvp2_eval_rsft_r2b
1245	STATUS: DONE
1246	CREATED_AT: 2026-05-15T09:42:58.437Z
1247	UPDATED_AT: 2026-05-15T13:27:35.580Z
1248	CONCLUSION: success
1249	METRICS: {
1250	  "rel_f1": 0.4493,
1251	  "ign_f1": 0.4493,
1252	  "evi_f1": 0.8128,
1253	  "evi_f1_joint": 0.349,
1254	  "evi_f1_joint_P": 0.3455,
1255	  "evi_f1_joint_R": 0.3526,
1256	  "edcr": 0.6609,
1257	  "precision": 0.4566,
1258	  "recall": 0.4424,
1259	  "evi_precision": 0.8201,
1260	  "evi_recall": 0.8056,
1261	  "pred_count": 14829,
1262	  "format_ok": "983/985",
1263	  "truncated": 179,
1264	  "inference_time_s": 5862,
1265	  "delta_evi_f1_joint": 0.0373
1266	}
1267	COMMAND: python -m freige.eval.inference --no-quantize (r2b checkpoint on cuda:3)
1268	SPEC.server: rtx5090-4x
1269	SPEC.data_path: /root/autodl-tmp/data/docred
1270	SPEC.data_count: 985
1271	SPEC.model_name: Qwen3-4B + SFT + RSFT r2b
1272	SPEC.seed: 42
1273	SPEC.checkpoint_source: /root/autodl-tmp/rsft_output_r2b
1274	SPEC.eval_data: /root/autodl-tmp/data/docred/dev.json
1275	SPEC.pid: 189855
1276	
1277	========================================================================================================================
1278	EXP_ID: mvp2_eval_rsft_r2b_maxtok1536
1279	STATUS: DONE
1280	CREATED_AT: 2026-05-15T11:49:48.849Z
1281	UPDATED_AT: 2026-05-15T13:23:59.642Z
1282	CONCLUSION: killed
1283	COMMAND: python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_r2b --data_path /root/autodl-tmp/data/docred --no-quantize --max_new_tokens 1536 --output_dir /root/autodl-tmp/eval_results/rsft_r2b_maxtok1536
1284	SPEC.server: rtx5090-4x
1285	SPEC.gpu: ['cuda:1']
1286	SPEC.pid: 196700
1287	SPEC.log_path: ~/runs/faith-evidence-ie/mvp2_eval_rsft_r2b_maxtok1536.log
1288	SPEC.submitted_at: 2026-05-15T11:51:37.717Z
1289	SPEC.submitted_via: submit_training_job
1290	SPEC.backend: tmux
1291	SPEC.account: root
1292	SPEC.data_path: /root/autodl-tmp/data/docred
1293	SPEC.data_count: 985
1294	SPEC.model_name: Qwen3-4B+SFT+RSFT r2b
1295	SPEC.checkpoint_source: /root/autodl-tmp/rsft_output_r2b
1296	SPEC.eval_data: docred dev (985 docs)
1297	SPEC.seed: 42
1298	SPEC.purpose: 诊断 EDCR 下降是否因 max_new_tokens=1024 截断导致，179/985 docs 被截断，改用 1536 重跑
1299	SPEC.wall_clock_seconds: 5541.9
1300	SPEC.gpu_hours: 1.54
1301	
1302	========================================================================================================================
1303	EXP_ID: mvp2_eval_rsft_r2b_maxtok1536_r2
1304	STATUS: DONE
1305	CREATED_AT: 2026-05-15T11:54:57.156Z
1306	UPDATED_AT: 2026-05-15T15:21:13.816Z
1307	CONCLUSION: negative
1308	METRICS: {
1309	  "rel_f1": 0.4504,
1310	  "ign_f1": 0.4504,
1311	  "evi_f1": 0.8102,
1312	  "edcr": 0.674,
1313	  "precision": 0.4488,
1314	  "recall": 0.4519,
1315	  "evi_precision": 0.8162,
1316	  "evi_recall": 0.8044,
1317	  "n_truncated": 146,
1318	  "n_total": 985,
1319	  "n_predictions": 17188,
1320	  "n_distractor_citations": 19589,
1321	  "n_total_citations": 29063,
1322	  "format_ok_rate": 0.998
1323	}
1324	COMMAND: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && rm -rf /root/autodl-tmp/eval_results/rsft_r2b_maxtok1536/* && python -m freige.eval.inference --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --model_path /root/autodl-tmp/rsft_output_r2b --data_path /root/autodl-tmp/data/docred --no-quantize --max_new_tokens 1536 --output_dir /root/autodl-tmp/eval_results/rsft_r2b_maxtok1536"
1325	SPEC.server: rtx5090-4x
1326	SPEC.gpu: ['cuda:1']
1327	SPEC.pid: 197381
1328	SPEC.log_path: ~/runs/faith-evidence-ie/mvp2_eval_rsft_r2b_maxtok1536_r2.log
1329	SPEC.submitted_at: 2026-05-15T11:55:18.697Z
1330	SPEC.submitted_via: submit_training_job
1331	SPEC.backend: tmux
1332	SPEC.account: root
1333	SPEC.wall_clock_seconds: 12352.2
1334	SPEC.gpu_hours: 3.43
1335	
1336	========================================================================================================================
1337	EXP_ID: mvp2_eval_rsft_s43
1338	STATUS: DONE
1339	CREATED_AT: 2026-05-15T11:25:26.268Z
1340	UPDATED_AT: 2026-05-15T11:29:11.205Z
1341	CONCLUSION: failed
1342	COMMAND: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.eval.inference --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_adapter /root/autodl-tmp/rsft_output_s43 --data_dir /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/eval_results/rsft_s43 --no-quantize --gpu 0"
1343	SPEC.server: rtx5090-4x
1344	SPEC.gpu: ['cuda:2']
1345	SPEC.pid: 194296
1346	SPEC.log_path: ~/runs/faith-evidence-ie/mvp2_eval_rsft_s43.log
1347	SPEC.submitted_at: 2026-05-15T11:26:15.318Z
1348	SPEC.submitted_via: submit_training_job
1349	SPEC.backend: tmux
1350	SPEC.account: root
1351	SPEC.wall_clock_seconds: 18.9
1352	SPEC.gpu_hours: 0.01
1353	
1354	========================================================================================================================
1355	EXP_ID: mvp2_eval_rsft_s43_r2
1356	STATUS: DONE
1357	CREATED_AT: 2026-05-15T11:29:17.551Z
1358	UPDATED_AT: 2026-05-15T13:54:26.023Z
1359	CONCLUSION: success
1360	METRICS: {
1361	  "rel_f1": 0.4683,
1362	  "ign_f1": 0.4683,
1363	  "evi_f1": 0.8156,
1364	  "evi_f1_joint": 0.3711,
1365	  "evi_f1_joint_P": 0.3747,
1366	  "evi_f1_joint_R": 0.3675,
1367	  "edcr": 0.6388,
1368	  "precision": 0.4817,
1369	  "recall": 0.4556,
1370	  "evi_precision": 0.8142,
1371	  "evi_recall": 0.817,
1372	  "n_predictions": 14970,
1373	  "n_truncated": 171,
1374	  "format_ok_rate": 1,
1375	  "inference_time_s": 6316.7,
1376	  "sft_baseline_rel_f1": 0.4057,
1377	  "sft_baseline_evi_f1": 0.7979,
1378	  "delta_rel_f1": 0.0626,
1379	  "delta_evi_f1": 0.0177,
1380	  "delta_evi_f1_joint": 0.0594,
1381	  "mvp2_pass": true
1382	}
1383	COMMAND: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_s43 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/eval_results/rsft_s43 --no-quantize"
1384	SPEC.server: rtx5090-4x
1385	SPEC.gpu: ['cuda:2']
1386	SPEC.pid: 194837
1387	SPEC.log_path: ~/runs/faith-evidence-ie/mvp2_eval_rsft_s43_r2.log
1388	SPEC.submitted_at: 2026-05-15T11:29:48.250Z
1389	SPEC.submitted_via: submit_training_job
1390	SPEC.backend: tmux
1391	SPEC.account: root
1392	SPEC.wall_clock_seconds: 7213.0
1393	SPEC.gpu_hours: 2.0
1394	
1395	========================================================================================================================
1396	EXP_ID: mvp2_eval_sft_baseline
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "b83bc91e-83d9-47c7-afae-d34de0883744"
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
  "task_id": "aa0dedafabeeb8ab6",
  "tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "description": "Reading /tmp/4b_experiments_full.txt",
  "usage": {
    "total_tokens": 57975,
    "tool_uses": 14,
    "duration_ms": 78962
  },
  "last_tool_name": "Read",
  "uuid": "7c8c231d-7303-4b2f-aca5-ba3e77af7706",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0"
}
```

---


### Tool call

_source line 55_

<details open><summary>🔧 Tool call — Read · `toolu_018en25eyj8nAizVebWvdqef`</summary>

```json
{
  "file_path": "/tmp/4b_experiments_full.txt",
  "offset": 1396,
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "d22cd685-4a57-4057-9c05-0f5c8e169ba6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CaTX38GxyHacvYcKuP9MVW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8036,
      "cache_read_input_tokens": 49586,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8036,
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

_source line 56 · 2026-05-18T22:03:42.075Z_

<details><summary>↩ Tool result · `toolu_018en25eyj8nAizVebWvdqef`</summary>

```text
1396	EXP_ID: mvp2_eval_sft_baseline
1397	STATUS: DONE
1398	CREATED_AT: 2026-05-14T21:47:41.356Z
1399	UPDATED_AT: 2026-05-15T13:27:26.236Z
1400	CONCLUSION: success
1401	METRICS: {
1402	  "rel_f1": 0.4057,
1403	  "evi_f1": 0.7979,
1404	  "evi_f1_joint": 0.3117,
1405	  "evi_f1_joint_P": 0.3037,
1406	  "evi_f1_joint_R": 0.32,
1407	  "edcr": 0.7118,
1408	  "pred_count": 12234,
1409	  "gold_count": 12151,
1410	  "format_ok_rate": 0.998,
1411	  "format_compliance_rate": 0.998,
1412	  "field_compliance_rate": 0.6264,
1413	  "n_truncated": 367,
1414	  "inference_time_seconds": 6138.5
1415	}
1416	COMMAND: python -m freige.eval.inference --model_path /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/sft_baseline_eval_results --quantize
1417	SPEC.server: rtx5090-4x
1418	SPEC.gpu: ['cuda:3']
1419	SPEC.account: root
1420	SPEC.pid: 104979
1421	SPEC.data_path: /root/autodl-tmp/data/docred
1422	SPEC.data_count: 985
1423	SPEC.model_name: Qwen3-4B + SFT LoRA adapter
1424	SPEC.seed: 42
1425	SPEC.checkpoint_source: /root/autodl-tmp/sft_output
1426	SPEC.eval_data: docred dev split
1427	SPEC.checkpoint_path: /root/autodl-tmp/sft_baseline_eval_results/metrics.json
1428	SPEC.log_path: N/A - tmux output only
1429	
1430	========================================================================================================================
1431	EXP_ID: mvp2_grpo_ced
1432	STATUS: DONE
1433	CREATED_AT: 2026-05-14T07:10:31.165Z
1434	UPDATED_AT: 2026-05-14T08:00:02.874Z
1435	CONCLUSION: failed
1436	COMMAND: bash -c "source /etc/network_turbo && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && accelerate launch --config_file freige/configs/accelerate_4gpu.yaml -m freige.training.grpo_trainer --model_name /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_dir /root/autodl-tmp/data/docred --stage 3 --tau_start 0.3 --tau_end 0.5 --output_dir /root/autodl-tmp/grpo_s3 --num_generations 4 --reward_device cpu --per_device_batch_size 1 --gradient_accumulation_steps 16 --num_epochs 1 --learning_rate 5e-5 --seed 42 --wandb_run_name grpo-s3-ced"
1437	SPEC.server: rtx5090-4x
1438	SPEC.gpu: ['cuda:0', 'cuda:1', 'cuda:2', 'cuda:3']
1439	SPEC.pid: 20973
1440	SPEC.log_path: ~/runs/faith-evidence-ie/mvp2_grpo_ced.log
1441	SPEC.submitted_at: 2026-05-14T07:19:59.045Z
1442	SPEC.submitted_via: submit_training_job
1443	SPEC.backend: tmux
1444	SPEC.account: root
1445	SPEC.wall_clock_seconds: 2189.9
1446	SPEC.gpu_hours: 2.43
1447	
1448	========================================================================================================================
1449	EXP_ID: mvp2_grpo_ced_kl001
1450	STATUS: DONE
1451	CREATED_AT: 2026-05-14T12:32:53.111Z
1452	UPDATED_AT: 2026-05-14T15:33:06.208Z
1453	CONCLUSION: failed
1454	COMMAND: python -m freige.training.grpo_trainer --stage 3 --kl_coef 0.01 --num_iterations 1 --save_steps 20 --save_total_limit 20 --format_reward_weight 0.3 --f1_reward_weight 3.0 --ced_reward_weight 1.0 --lr 5e-5 --gradient_accumulation_steps 16 --num_generations 4
1455	SPEC.server: rtx5090-4x
1456	SPEC.gpu: ['cuda:0']
1457	SPEC.pid: 64981
1458	SPEC.log_path: ~/runs/faith-evidence-ie/mvp2_grpo_ced_kl001.log
1459	SPEC.data_path: /root/autodl-tmp/data/docred
1460	SPEC.data_count: {'train': 3027, 'dev': 985}
1461	SPEC.model_name: Qwen3-4B
1462	SPEC.seed: 42
1463	SPEC.hypothesis: kl_coef=0.01 (vs r5 kl_coef=0.0) prevents CED mode collapse while keeping QLoRA 4-bit compatible — answers whether KL regularization is necessary
1464	SPEC.parent: mvp2_grpo_ced_r5
1465	SPEC.checkpoint_source: /root/autodl-tmp/sft_output
1466	SPEC.eval_data: /root/autodl-tmp/data/docred
1467	SPEC.hyperparams: {'learning_rate': '5e-5', 'kl_coef': 0.01, 'save_steps': 20, 'save_total_limit': 20, 'num_iterations': 1, 'format_reward_weight': 0.3, 'f1_reward_weight': 3, 'ced_reward_weight': 1, 'per_device_batch_size': 1, 'gradient_accumulation_steps': 16, 'num_generations': 4, 'quantization': 'QLoRA 4-bit NF4'}
1468	
1469	========================================================================================================================
1470	EXP_ID: mvp2_grpo_ced_kl001_r4
1471	STATUS: DONE
1472	CREATED_AT: 2026-05-14T15:32:32.529Z
1473	UPDATED_AT: 2026-05-14T18:11:53.975Z
1474	CONCLUSION: success
1475	METRICS: {
1476	  "final_step": 100,
1477	  "train_runtime_s": 9069.88,
1478	  "reward_final": 1.195,
1479	  "f1_reward_final": 0.573,
1480	  "ced_reward_final": 0.328,
1481	  "format_reward_final": 0.293,
1482	  "frac_zero_std_final": 0.2,
1483	  "kl_final": 0.118,
1484	  "loss_final": -0.009,
1485	  "grad_norm_final": 0.14,
1486	  "entropy_final": 0.067,
1487	  "completion_length_mean_final": 520.8,
1488	  "best_reward_step": 90,
1489	  "best_reward": 1.37,
1490	  "best_f1_reward": 0.72,
1491	  "best_ced_reward": 0.353
1492	}
1493	COMMAND: bash -c "source /etc/network_turbo && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.training.grpo_trainer --model_name /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_dir /root/autodl-tmp/data/docred --stage 3 --tau_start 0.3 --tau_end 0.5 --output_dir /root/autodl-tmp/grpo_ced_kl001 --num_generations 8 --reward_device cuda --per_device_batch_size 1 --gradient_accumulation_steps 16 --num_epochs 1 --learning_rate 5e-5 --seed 42 --kl_coef 0.01 --save_steps 10 --save_total_limit 20 --max_steps 100 --format_reward_weight 0.3 --f1_reward_weight 3.0 --ced_reward_weight 1.0 --num_iterations 1 --wandb_run_name grpo-s3-ced-kl001-r4"
1494	SPEC.server: rtx5090-4x
1495	SPEC.gpu: ['cuda:0']
1496	SPEC.pid: 68084
1497	SPEC.log_path: ~/runs/faith-evidence-ie/mvp2_grpo_ced_kl001_r4.log
1498	SPEC.submitted_at: 2026-05-14T15:32:32.454Z
1499	SPEC.submitted_via: submit_training_job
1500	SPEC.backend: tmux
1501	SPEC.account: root
1502	SPEC.data_path: /root/autodl-tmp/data/docred
1503	SPEC.data_count: {'train': 3027, 'dev': 985}
1504	SPEC.model_name: Qwen3-4B
1505	SPEC.seed: 42
1506	SPEC.hypothesis: kl_coef=0.01 + num_generations=8 prevents mode collapse (vs r5 kl=0/gen=4 which collapsed at step 250). 100-step probe to verify KL stability before full run.
1507	SPEC.parent: mvp2_grpo_ced_r5
1508	SPEC.checkpoint_source: /root/autodl-tmp/sft_output
1509	SPEC.eval_data: /root/autodl-tmp/data/docred
1510	SPEC.hyperparams: {'learning_rate': '5e-5', 'kl_coef': 0.01, 'save_steps': 10, 'save_total_limit': 20, 'max_steps': 100, 'num_iterations': 1, 'num_generations': 8, 'format_reward_weight': 0.3, 'f1_reward_weight': 3, 'ced_reward_weight': 1, 'per_device_batch_size': 1, 'gradient_accumulation_steps': 16, 'quantization': 'QLoRA 4-bit NF4', 'reward_device': 'cuda'}
1511	SPEC.wall_clock_seconds: 9550.2
1512	SPEC.gpu_hours: 2.65
1513	
1514	========================================================================================================================
1515	EXP_ID: mvp2_grpo_ced_lr5e6_r1
1516	STATUS: DONE
1517	CREATED_AT: 2026-05-14T19:21:08.231Z
1518	UPDATED_AT: 2026-05-15T01:29:06.862Z
1519	CONCLUSION: killed
1520	COMMAND: python -m freige.training.grpo_trainer --model_name /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_dir /root/autodl-tmp/data/docred --stage 3 --tau_start 0.3 --tau_end 0.5 --output_dir /root/autodl-tmp/grpo_ced_lr5e6 --num_generations 8 --reward_device cuda --per_device_batch_size 1 --gradient_accumulation_steps 16 --num_epochs 1 --learning_rate 5e-6 --seed 42 --kl_coef 0.01 --save_steps 20 --save_total_limit 20 --max_steps 200 --format_reward_weight 0.3 --f1_reward_weight 3.0 --ced_reward_weight 1.0 --num_iterations 1 --wandb_run_name grpo-s3-ced-lr5e6-r1
1521	SPEC.server: rtx5090-4x
1522	SPEC.gpu: ['cuda:0']
1523	SPEC.pid: 90080
1524	SPEC.data_path: /root/autodl-tmp/data/docred
1525	SPEC.data_count: 3053
1526	SPEC.model_name: Qwen3-4B + SFT adapter
1527	SPEC.seed: 42
1528	SPEC.hyperparams: {'learning_rate': 5e-06, 'kl_coef': 0.01, 'num_generations': 8, 'gradient_accumulation_steps': 16, 'max_steps': 200, 'save_steps': 20, 'format_reward_weight': 0.3, 'f1_reward_weight': 3, 'ced_reward_weight': 1, 'tau_start': 0.3, 'tau_end': 0.5}
1529	
1530	========================================================================================================================
1531	EXP_ID: mvp2_grpo_ced_lr5e6_rp_r1
1532	STATUS: DONE
1533	CREATED_AT: 2026-05-14T19:44:15.272Z
1534	UPDATED_AT: 2026-05-14T20:44:07.125Z
1535	CONCLUSION: failed
1536	COMMAND: bash /root/autodl-tmp/scripts/train_ced_lr5e6_rp.sh
1537	SPEC.server: rtx5090-4x
1538	SPEC.gpu: ['cuda:3']
1539	SPEC.account: root
1540	SPEC.pid: 94055
1541	SPEC.data_path: /root/autodl-tmp/data/docred
1542	SPEC.data_count: 3053
1543	SPEC.model_name: Qwen3-4B + SFT adapter
1544	SPEC.seed: 42
1545	SPEC.checkpoint_source: SFT from scratch (no GRPO checkpoint)
1546	SPEC.eval_data: N/A - training experiment
1547	
1548	========================================================================================================================
1549	EXP_ID: mvp2_grpo_ced_lr5e6_rp_r2
1550	STATUS: DONE
1551	CREATED_AT: 2026-05-14T20:04:55.831Z
1552	UPDATED_AT: 2026-05-14T21:40:50.174Z
1553	CONCLUSION: killed
1554	COMMAND: python -m freige.training.grpo_trainer --model_name /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_dir /root/autodl-tmp/data/docred --stage 3 --tau_start 0.3 --tau_end 0.5 --output_dir /root/autodl-tmp/grpo_ced_lr5e6_rp --num_generations 8 --reward_device cuda --per_device_batch_size 1 --gradient_accumulation_steps 16 --num_epochs 1 --learning_rate 5e-6 --seed 42 --kl_coef 0.01 --save_steps 20 --save_total_limit 20 --max_steps 200 --format_reward_weight 0.3 --f1_reward_weight 3.0 --ced_reward_weight 1.0 --num_iterations 1 --ced_recall_penalty --wandb_run_name grpo-s3-ced-lr5e6-rp-r2
1555	SPEC.server: rtx5090-4x
1556	SPEC.gpu: ['cuda:3']
1557	SPEC.pid: 94753
1558	SPEC.log_path: ~/runs/faith-evidence-ie/mvp2_grpo_ced_lr5e6_rp_r2.log
1559	SPEC.submitted_at: 2026-05-14T20:05:27.371Z
1560	SPEC.submitted_via: submit_training_job
1561	SPEC.backend: tmux
1562	SPEC.account: root
1563	SPEC.data_path: /root/autodl-tmp/data/docred
1564	SPEC.data_count: 3053
1565	SPEC.model_name: Qwen3-4B + SFT adapter
1566	SPEC.seed: 42
1567	SPEC.checkpoint_source: N/A (training from SFT adapter)
1568	SPEC.eval_data: /root/autodl-tmp/data/docred/dev.json
1569	SPEC.hyperparams: {'learning_rate': 5e-06, 'kl_coef': 0.01, 'num_generations': 8, 'gradient_accumulation_steps': 16, 'max_steps': 200, 'save_steps': 20, 'format_reward_weight': 0.3, 'f1_reward_weight': 3, 'ced_reward_weight': 1, 'tau_start': 0.3, 'tau_end': 0.5, 'ced_recall_penalty': True}
1570	SPEC.wall_clock_seconds: 5716.8
1571	SPEC.gpu_hours: 1.59
1572	
1573	========================================================================================================================
1574	EXP_ID: mvp2_grpo_ced_r1
1575	STATUS: DONE
1576	CREATED_AT: 2026-05-14T08:02:41.858Z
1577	UPDATED_AT: 2026-05-14T10:37:23.856Z
1578	CONCLUSION: killed
1579	COMMAND: bash -c "source /etc/network_turbo && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && accelerate launch --config_file freige/configs/accelerate_4gpu.yaml -m freige.training.grpo_trainer --model_name /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_dir /root/autodl-tmp/data/docred --stage 3 --tau_start 0.3 --tau_end 0.5 --output_dir /root/autodl-tmp/grpo_s3 --num_generations 4 --reward_device cpu --per_device_batch_size 1 --gradient_accumulation_steps 16 --num_epochs 1 --learning_rate 5e-5 --seed 42 --wandb_run_name grpo-s3-ced-r1"
1580	SPEC.server: rtx5090-4x
1581	SPEC.gpu: ['cuda:0', 'cuda:1', 'cuda:2', 'cuda:3']
1582	SPEC.pid: 24122
1583	SPEC.log_path: ~/runs/faith-evidence-ie/mvp2_grpo_ced_r1.log
1584	SPEC.submitted_at: 2026-05-14T08:02:41.839Z
1585	SPEC.submitted_via: submit_training_job
1586	SPEC.backend: tmux
1587	SPEC.account: root
1588	SPEC.data_path: /root/autodl-tmp/data/docred
1589	SPEC.data_count: {'train': 3027, 'dev': 985}
1590	SPEC.model_name: Qwen3-4B
1591	SPEC.seed: 42
1592	SPEC.hypothesis: CED reward improves Evi-F1 over flat-NLI and extraction-only baselines
1593	SPEC.wall_clock_seconds: 8641.6
1594	SPEC.gpu_hours: 9.6
1595	
1596	========================================================================================================================
1597	EXP_ID: mvp2_grpo_ced_r2
1598	STATUS: DONE
1599	CREATED_AT: 2026-05-14T10:58:11.663Z
1600	UPDATED_AT: 2026-05-14T11:31:49.724Z
1601	CONCLUSION: killed
1602	COMMAND: accelerate launch --config_file freige/configs/accelerate_4gpu.yaml -m freige.training.grpo_trainer --model_name Qwen3-4B --learning_rate 2e-5 --kl_coef 0.05 --save_steps 20 --format_reward_weight 0.3 --f1_reward_weight 3.0 --ced_reward_weight 1.0 --num_iterations 2
1603	SPEC.server: rtx5090-4x
1604	SPEC.data_path: /root/autodl-tmp/data/docred
1605	SPEC.data_count: {'train': 3027, 'dev': 985}
1606	SPEC.model_name: Qwen3-4B
1607	SPEC.seed: 42
1608	SPEC.hypothesis: CED reward with balanced weights (format×0.3, f1×3.0, ced×1.0) + KL=0.05 + save_steps=20 + num_iterations=2 prevents mode collapse and improves Evi-F1
1609	SPEC.parent: mvp2_grpo_ced_r1
1610	SPEC.hyperparams: {'learning_rate': '2e-5', 'kl_coef': 0.05, 'save_steps': 20, 'num_iterations': 2, 'format_reward_weight': 0.3, 'f1_reward_weight': 3, 'ced_reward_weight': 1, 'per_device_batch_size': 1, 'gradient_accumulation_steps': 16, 'num_generations': 4}
1611	
1612	========================================================================================================================
1613	EXP_ID: mvp2_grpo_ced_r3
1614	STATUS: DONE
1615	CREATED_AT: 2026-05-14T11:47:53.099Z
1616	UPDATED_AT: 2026-05-14T12:09:23.005Z
1617	CONCLUSION: failed
1618	COMMAND: python -m freige.training.grpo_trainer --stage 3 --num_iterations 1 --kl_coef 0.05 --save_steps 20 --format_reward_weight 0.3 --f1_reward_weight 3.0 --ced_reward_weight 1.0 --max_kl 100 --lr 5e-5
1619	SPEC.server: rtx5090-4x
1620	SPEC.gpu: ['cuda:0']
1621	SPEC.pid: 47136
1622	SPEC.log_path: ~/runs/faith-evidence-ie/mvp2_grpo_ced_r3.log
1623	SPEC.submitted_at: 2026-05-14T11:48:42.598Z
1624	SPEC.submitted_via: submit_training_job
1625	SPEC.backend: tmux
1626	SPEC.account: root
1627	SPEC.data_path: /root/autodl-tmp/data/docred
1628	SPEC.data_count: {'train': 3027, 'dev': 985}
1629	SPEC.model_name: Qwen3-4B
1630	SPEC.seed: 42
1631	SPEC.hypothesis: Reward weighting (format×0.3, f1×3.0, ced×1.0) with stable training (num_iterations=1, KL early stop) improves Evi-F1
1632	SPEC.parent: mvp2_grpo_ced_r1
1633	SPEC.checkpoint_source: /root/autodl-tmp/sft_output
1634	SPEC.eval_data: /root/autodl-tmp/data/docred
1635	SPEC.hyperparams: {'learning_rate': '5e-5', 'kl_coef': 0.05, 'save_steps': 20, 'num_iterations': 1, 'format_reward_weight': 0.3, 'f1_reward_weight': 3, 'ced_reward_weight': 1, 'max_kl': 100}
1636	SPEC.wall_clock_seconds: 1061.5
1637	SPEC.gpu_hours: 0.29
1638	
1639	========================================================================================================================
1640	EXP_ID: mvp2_grpo_ced_r4
1641	STATUS: DONE
1642	CREATED_AT: 2026-05-14T12:10:15.698Z
1643	UPDATED_AT: 2026-05-14T12:30:06.177Z
1644	CONCLUSION: killed
1645	COMMAND: python -m freige.training.grpo_trainer --stage 3 --kl_coef 0.0 --num_iterations 1 --save_steps 20 --format_reward_weight 0.3 --f1_reward_weight 3.0 --ced_reward_weight 1.0 --lr 5e-5 --gradient_accumulation_steps 16 --num_generations 4
1646	SPEC.server: rtx5090-4x
1647	SPEC.gpu: ['cuda:0']
1648	SPEC.pid: 50529
1649	SPEC.log_path: ~/runs/faith-evidence-ie/mvp2_grpo_ced_r4.log
1650	SPEC.submitted_at: 2026-05-14T12:10:15.624Z
1651	SPEC.submitted_via: submit_training_job
1652	SPEC.backend: tmux
1653	SPEC.account: root
1654	SPEC.data_path: /root/autodl-tmp/data/docred
1655	SPEC.data_count: {'train': 3027, 'dev': 985}
1656	SPEC.model_name: Qwen3-4B
1657	SPEC.seed: 42
1658	SPEC.hypothesis: CED reward (format×0.3, f1×3.0, ced×1.0) with kl_coef=0 (D008 fix) achieves Evi-F1 improvement over SFT baseline
1659	SPEC.parent: mvp2_grpo_ced_r3
1660	SPEC.checkpoint_source: /root/autodl-tmp/sft_output
1661	SPEC.eval_data: /root/autodl-tmp/data/docred
1662	SPEC.hyperparams: {'learning_rate': '5e-5', 'kl_coef': 0, 'save_steps': 20, 'num_iterations': 1, 'format_reward_weight': 0.3, 'f1_reward_weight': 3, 'ced_reward_weight': 1, 'per_device_batch_size': 1, 'gradient_accumulation_steps': 16, 'num_generations': 4, 'quantization': 'QLoRA 4-bit NF4'}
1663	SPEC.wall_clock_seconds: 1169.5
1664	SPEC.gpu_hours: 0.32
1665	
1666	========================================================================================================================
1667	EXP_ID: mvp2_grpo_ced_r5
1668	STATUS: DONE
1669	CREATED_AT: 2026-05-14T12:31:45.606Z
1670	UPDATED_AT: 2026-05-14T15:32:21.817Z
1671	CONCLUSION: negative
1672	COMMAND: python -m freige.training.grpo_trainer --stage 3 --kl_coef 0.0 --num_iterations 1 --save_steps 20 --format_reward_weight 0.3 --f1_reward_weight 3.0 --ced_reward_weight 1.0 --lr 5e-5 --gradient_accumulation_steps 16 --num_generations 4
1673	SPEC.server: rtx5090-4x
1674	SPEC.gpu: ['cuda:0']
1675	SPEC.pid: 53071
1676	SPEC.log_path: ~/runs/faith-evidence-ie/mvp2_grpo_ced_r5.log
1677	SPEC.submitted_at: 2026-05-14T12:31:45.554Z
1678	SPEC.submitted_via: submit_training_job
1679	SPEC.backend: tmux
1680	SPEC.account: root
1681	SPEC.data_path: /root/autodl-tmp/data/docred
1682	SPEC.data_count: {'train': 3027, 'dev': 985}
1683	SPEC.model_name: Qwen3-4B
1684	SPEC.seed: 42
1685	SPEC.hypothesis: CED reward (format×0.3, f1×3.0, ced×1.0) with kl_coef=0 trains stably and improves Evi-F1 over SFT baseline
1686	SPEC.parent: mvp2_grpo_ced_r4
1687	SPEC.checkpoint_source: /root/autodl-tmp/sft_output
1688	SPEC.eval_data: /root/autodl-tmp/data/docred
1689	SPEC.hyperparams: {'learning_rate': '5e-5', 'kl_coef': 0, 'save_steps': 20, 'num_iterations': 1, 'format_reward_weight': 0.3, 'f1_reward_weight': 3, 'ced_reward_weight': 1, 'per_device_batch_size': 1, 'gradient_accumulation_steps': 16, 'num_generations': 4, 'quantization': 'QLoRA 4-bit NF4'}
1690	SPEC.wall_clock_seconds: 9887.5
1691	SPEC.gpu_hours: 2.75
1692	
1693	========================================================================================================================
1694	EXP_ID: mvp2_grpo_extract
1695	STATUS: DONE
1696	CREATED_AT: 2026-05-14T07:10:35.796Z
1697	UPDATED_AT: 2026-05-14T12:25:32.094Z
1698	CONCLUSION: failed
1699	COMMAND: python -m freige.training.grpo_trainer --stage 1 --ced_reward_weight 0.0 --format_reward_weight 0.3 --f1_reward_weight 3.0 --num_iterations 1 --kl_coef 0.05 --lr 5e-5
1700	SPEC.server: rtx5090-4x
1701	SPEC.gpu: ['cuda:2']
1702	SPEC.pid: 47561
1703	SPEC.log_path: ~/runs/faith-evidence-ie/mvp2_grpo_extract.log
1704	SPEC.submitted_at: 2026-05-14T11:48:50.108Z
1705	SPEC.submitted_via: submit_training_job
1706	SPEC.backend: tmux
1707	SPEC.account: root
1708	SPEC.data_path: /root/autodl-tmp/data/docred/train_annotated.json
1709	SPEC.data_count: 3027
1710	SPEC.model_name: Qwen3-4B (QLoRA from SFT warmup)
1711	SPEC.seed: 42
1712	SPEC.hypothesis: Extraction-only reward (format+F1, no CED) establishes GRPO baseline
1713	SPEC.parent: mvp2_sft_warmup
1714	SPEC.checkpoint_source: /root/autodl-tmp/sft_output
1715	SPEC.eval_data: /root/autodl-tmp/data/docred
1716	SPEC.hyperparams: {'learning_rate': '5e-5', 'kl_coef': 0.05, 'num_iterations': 1, 'format_reward_weight': 0.3, 'f1_reward_weight': 3, 'ced_reward_weight': 0}
1717	SPEC.wall_clock_seconds: 1479.2
1718	SPEC.gpu_hours: 0.41
1719	
1720	========================================================================================================================
1721	EXP_ID: mvp2_grpo_extract_r2
1722	STATUS: DONE
1723	CREATED_AT: 2026-05-14T12:10:19.532Z
1724	UPDATED_AT: 2026-05-14T12:30:08.099Z
1725	CONCLUSION: killed
1726	COMMAND: python -m freige.training.grpo_trainer --stage 1 --kl_coef 0.0 --num_iterations 1 --save_steps 20 --format_reward_weight 0.3 --f1_reward_weight 3.0 --ced_reward_weight 0.0 --lr 5e-5 --gradient_accumulation_steps 16 --num_generations 4
1727	SPEC.server: rtx5090-4x
1728	SPEC.gpu: ['cuda:2']
1729	SPEC.pid: 50670
1730	SPEC.log_path: ~/runs/faith-evidence-ie/mvp2_grpo_extract_r2.log
1731	SPEC.submitted_at: 2026-05-14T12:10:19.491Z
1732	SPEC.submitted_via: submit_training_job
1733	SPEC.backend: tmux
1734	SPEC.account: root
1735	SPEC.data_path: /root/autodl-tmp/data/docred
1736	SPEC.data_count: {'train': 3027, 'dev': 985}
1737	SPEC.model_name: Qwen3-4B
1738	SPEC.seed: 42
1739	SPEC.hypothesis: Extraction-only reward (format×0.3, f1×3.0, ced=0) with kl_coef=0 establishes stable GRPO baseline
1740	SPEC.parent: mvp2_grpo_extract
1741	SPEC.checkpoint_source: /root/autodl-tmp/sft_output
1742	SPEC.eval_data: /root/autodl-tmp/data/docred
1743	SPEC.hyperparams: {'learning_rate': '5e-5', 'kl_coef': 0, 'save_steps': 20, 'num_iterations': 1, 'format_reward_weight': 0.3, 'f1_reward_weight': 3, 'ced_reward_weight': 0, 'per_device_batch_size': 1, 'gradient_accumulation_steps': 16, 'num_generations': 4, 'quantization': 'QLoRA 4-bit NF4'}
1744	SPEC.wall_clock_seconds: 1166.7
1745	SPEC.gpu_hours: 0.32
1746	
1747	========================================================================================================================
1748	EXP_ID: mvp2_grpo_extract_r3
1749	STATUS: DONE
1750	CREATED_AT: 2026-05-14T12:31:48.781Z
1751	UPDATED_AT: 2026-05-14T16:59:20.304Z
1752	CONCLUSION: negative
1753	COMMAND: python -m freige.training.grpo_trainer --stage 1 --kl_coef 0.0 --num_iterations 1 --save_steps 20 --format_reward_weight 0.3 --f1_reward_weight 3.0 --ced_reward_weight 0.0 --lr 5e-5 --gradient_accumulation_steps 16 --num_generations 4
1754	SPEC.server: rtx5090-4x
1755	SPEC.gpu: ['cuda:2']
1756	SPEC.pid: 53149
1757	SPEC.log_path: ~/runs/faith-evidence-ie/mvp2_grpo_extract_r3.log
1758	SPEC.submitted_at: 2026-05-14T12:31:48.738Z
1759	SPEC.submitted_via: submit_training_job
1760	SPEC.backend: tmux
1761	SPEC.account: root
1762	SPEC.data_path: /root/autodl-tmp/data/docred
1763	SPEC.data_count: {'train': 3027, 'dev': 985}
1764	SPEC.model_name: Qwen3-4B
1765	SPEC.seed: 42
1766	SPEC.hypothesis: Extraction-only reward (format×0.3, f1×3.0, ced=0) with kl_coef=0 establishes stable GRPO baseline
1767	SPEC.parent: mvp2_grpo_extract
1768	SPEC.checkpoint_source: /root/autodl-tmp/sft_output
1769	SPEC.eval_data: /root/autodl-tmp/data/docred
1770	SPEC.hyperparams: {'learning_rate': '5e-5', 'kl_coef': 0, 'save_steps': 20, 'num_iterations': 1, 'format_reward_weight': 0.3, 'f1_reward_weight': 3, 'ced_reward_weight': 0, 'per_device_batch_size': 1, 'gradient_accumulation_steps': 16, 'num_generations': 4, 'quantization': 'QLoRA 4-bit NF4'}
1771	SPEC.wall_clock_seconds: 12041.2
1772	SPEC.gpu_hours: 3.34
1773	
1774	========================================================================================================================
1775	EXP_ID: mvp2_grpo_extract_r4
1776	STATUS: DONE
1777	CREATED_AT: 2026-05-14T16:54:59.403Z
1778	UPDATED_AT: 2026-05-14T17:40:25.731Z
1779	CONCLUSION: killed
1780	COMMAND: bash -c "source /etc/network_turbo && ... && python -m freige.training.grpo_trainer --stage 1 --kl_coef 0.01 --num_generations 8 --max_steps 100 ..."
1781	SPEC.server: rtx5090-4x
1782	SPEC.gpu: ['cuda:2']
1783	SPEC.pid: 73264
1784	SPEC.log_path: ~/runs/faith-evidence-ie/mvp2_grpo_extract_r4.log
1785	SPEC.submitted_at: 2026-05-14T16:55:57.491Z
1786	SPEC.submitted_via: submit_training_job
1787	SPEC.backend: tmux
1788	SPEC.account: root
1789	SPEC.data_path: /root/autodl-tmp/data/docred
1790	SPEC.data_count: {'train': 3027, 'dev': 985}
1791	SPEC.model_name: Qwen3-4B
1792	SPEC.seed: 42
1793	SPEC.checkpoint_source: /root/autodl-tmp/sft_output
1794	SPEC.eval_data: /root/autodl-tmp/data/docred
1795	SPEC.wall_clock_seconds: 2668.2
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "5bde55a7-c7b4-4cb2-97b0-ca6659edd3eb"
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
  "task_id": "aa0dedafabeeb8ab6",
  "tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "description": "Reading /tmp/4b_experiments_full.txt",
  "usage": {
    "total_tokens": 69081,
    "tool_uses": 15,
    "duration_ms": 81938
  },
  "last_tool_name": "Read",
  "uuid": "80ec9907-0048-4f4b-8b6e-662f7cef766b",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0"
}
```

---


### Tool call

_source line 58_

<details open><summary>🔧 Tool call — Read · `toolu_01FySCU1sA5N7QUckQUBcLrQ`</summary>

```json
{
  "file_path": "/tmp/4b_experiments_full.txt",
  "offset": 1795,
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "d8fc3aef-01e8-4cbf-81d2-1786ffdf8d7e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ZUzbUCtSYiopGxv83Lz5z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11068,
      "cache_read_input_tokens": 57622,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11068,
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

_source line 59 · 2026-05-18T22:03:45.051Z_

<details><summary>↩ Tool result · `toolu_01FySCU1sA5N7QUckQUBcLrQ`</summary>

```text
1795	SPEC.wall_clock_seconds: 2668.2
1796	SPEC.gpu_hours: 0.74
1797	
1798	========================================================================================================================
1799	EXP_ID: mvp2_grpo_flatnli
1800	STATUS: DONE
1801	CREATED_AT: 2026-05-14T07:10:33.848Z
1802	UPDATED_AT: 2026-05-14T12:13:34.747Z
1803	CONCLUSION: failed
1804	COMMAND: python -m freige.training.grpo_trainer --stage 2 --ced_reward_weight 1.0 --format_reward_weight 0.3 --f1_reward_weight 3.0 --num_iterations 1 --kl_coef 0.05 --lr 5e-5
1805	SPEC.server: rtx5090-4x
1806	SPEC.gpu: ['cuda:3']
1807	SPEC.pid: 47722
1808	SPEC.log_path: ~/runs/faith-evidence-ie/mvp2_grpo_flatnli.log
1809	SPEC.submitted_at: 2026-05-14T11:48:54.086Z
1810	SPEC.submitted_via: submit_training_job
1811	SPEC.backend: tmux
1812	SPEC.account: root
1813	SPEC.data_path: /root/autodl-tmp/data/docred
1814	SPEC.data_count: {'train': 3027, 'dev': 985}
1815	SPEC.model_name: Qwen3-4B
1816	SPEC.seed: 42
1817	SPEC.hypothesis: Flat-NLI reward improves Evi-F1 over extraction-only but less than CED
1818	SPEC.parent: mvp2_sft_warmup
1819	SPEC.checkpoint_source: /root/autodl-tmp/sft_output
1820	SPEC.eval_data: /root/autodl-tmp/data/docred
1821	SPEC.hyperparams: {'learning_rate': '5e-5', 'kl_coef': 0.05, 'num_iterations': 1, 'format_reward_weight': 0.3, 'f1_reward_weight': 3, 'ced_reward_weight': 1}
1822	SPEC.wall_clock_seconds: 1188.0
1823	SPEC.gpu_hours: 0.33
1824	
1825	========================================================================================================================
1826	EXP_ID: mvp2_grpo_flatnli_r2
1827	STATUS: DONE
1828	CREATED_AT: 2026-05-14T12:10:23.287Z
1829	UPDATED_AT: 2026-05-14T12:30:08.865Z
1830	CONCLUSION: killed
1831	COMMAND: python -m freige.training.grpo_trainer --stage 2 --kl_coef 0.0 --num_iterations 1 --save_steps 20 --format_reward_weight 0.3 --f1_reward_weight 3.0 --ced_reward_weight 1.0 --lr 5e-5 --gradient_accumulation_steps 16 --num_generations 4
1832	SPEC.server: rtx5090-4x
1833	SPEC.gpu: ['cuda:3']
1834	SPEC.pid: 50941
1835	SPEC.log_path: ~/runs/faith-evidence-ie/mvp2_grpo_flatnli_r2.log
1836	SPEC.submitted_at: 2026-05-14T12:10:23.256Z
1837	SPEC.submitted_via: submit_training_job
1838	SPEC.backend: tmux
1839	SPEC.account: root
1840	SPEC.data_path: /root/autodl-tmp/data/docred
1841	SPEC.data_count: {'train': 3027, 'dev': 985}
1842	SPEC.model_name: Qwen3-4B
1843	SPEC.seed: 42
1844	SPEC.hypothesis: Flat-NLI reward (format×0.3, f1×3.0, ced×1.0) with kl_coef=0 validates non-contrastive evidence baseline
1845	SPEC.parent: mvp2_grpo_flatnli
1846	SPEC.checkpoint_source: /root/autodl-tmp/sft_output
1847	SPEC.eval_data: /root/autodl-tmp/data/docred
1848	SPEC.hyperparams: {'learning_rate': '5e-5', 'kl_coef': 0, 'save_steps': 20, 'num_iterations': 1, 'format_reward_weight': 0.3, 'f1_reward_weight': 3, 'ced_reward_weight': 1, 'per_device_batch_size': 1, 'gradient_accumulation_steps': 16, 'num_generations': 4, 'quantization': 'QLoRA 4-bit NF4'}
1849	SPEC.wall_clock_seconds: 1174.2
1850	SPEC.gpu_hours: 0.33
1851	
1852	========================================================================================================================
1853	EXP_ID: mvp2_grpo_flatnli_r3
1854	STATUS: DONE
1855	CREATED_AT: 2026-05-14T12:31:52.782Z
1856	UPDATED_AT: 2026-05-14T15:27:55.267Z
1857	CONCLUSION: killed
1858	COMMAND: python -m freige.training.grpo_trainer --stage 2 --kl_coef 0.0 --num_iterations 1 --save_steps 20 --format_reward_weight 0.3 --f1_reward_weight 3.0 --ced_reward_weight 1.0 --lr 5e-5 --gradient_accumulation_steps 16 --num_generations 4
1859	SPEC.server: rtx5090-4x
1860	SPEC.gpu: ['cuda:3']
1861	SPEC.pid: 53292
1862	SPEC.log_path: ~/runs/faith-evidence-ie/mvp2_grpo_flatnli_r3.log
1863	SPEC.submitted_at: 2026-05-14T12:31:52.703Z
1864	SPEC.submitted_via: submit_training_job
1865	SPEC.backend: tmux
1866	SPEC.account: root
1867	SPEC.data_path: /root/autodl-tmp/data/docred
1868	SPEC.data_count: {'train': 3027, 'dev': 985}
1869	SPEC.model_name: Qwen3-4B
1870	SPEC.seed: 42
1871	SPEC.hypothesis: Flat-NLI reward (format×0.3, f1×3.0, ced×1.0) with kl_coef=0 validates non-contrastive evidence baseline
1872	SPEC.parent: mvp2_grpo_flatnli
1873	SPEC.checkpoint_source: /root/autodl-tmp/sft_output
1874	SPEC.eval_data: /root/autodl-tmp/data/docred
1875	SPEC.hyperparams: {'learning_rate': '5e-5', 'kl_coef': 0, 'save_steps': 20, 'num_iterations': 1, 'format_reward_weight': 0.3, 'f1_reward_weight': 3, 'ced_reward_weight': 1, 'per_device_batch_size': 1, 'gradient_accumulation_steps': 16, 'num_generations': 4, 'quantization': 'QLoRA 4-bit NF4'}
1876	SPEC.wall_clock_seconds: 9527.7
1877	SPEC.gpu_hours: 2.65
1878	SPEC.checkpoint_path: /root/autodl-tmp/checkpoints_backup/flatnli_r3_healthy/
1879	
1880	========================================================================================================================
1881	EXP_ID: mvp2_grpo_flatnli_r4
1882	STATUS: DONE
1883	CREATED_AT: 2026-05-14T15:32:31.804Z
1884	UPDATED_AT: 2026-05-14T16:56:12.080Z
1885	CONCLUSION: killed
1886	COMMAND: CUDA_VISIBLE_DEVICES=3 python -m freige.training.grpo_trainer --stage 2 --reward_device cuda --resume_from_checkpoint /root/autodl-tmp/grpo_flatnli_r3/checkpoint-100 --save_total_limit 40 --wandb_run_name grpo-s2-flatnli-r4
1887	SPEC.server: rtx5090-4x
1888	SPEC.gpu: ['cuda:3']
1889	SPEC.pid: 67050
1890	SPEC.log_path: ~/runs/faith-evidence-ie/mvp2_grpo_flatnli_r4.log
1891	SPEC.data_path: /root/autodl-tmp/data/docred
1892	SPEC.data_count: {'train': 3027, 'dev': 985}
1893	SPEC.model_name: Qwen3-4B
1894	SPEC.seed: 42
1895	SPEC.checkpoint_source: /root/autodl-tmp/sft_output
1896	SPEC.resume_from: /root/autodl-tmp/grpo_flatnli_r3/checkpoint-100
1897	SPEC.hyperparams: {'learning_rate': '5e-5', 'kl_coef': 0, 'num_iterations': 1, 'format_reward_weight': 0.3, 'f1_reward_weight': 3, 'ced_reward_weight': 1, 'per_device_batch_size': 1, 'gradient_accumulation_steps': 16, 'num_generations': 4, 'reward_device': 'cuda', 'quantization': 'QLoRA 4-bit NF4'}
1898	
1899	========================================================================================================================
1900	EXP_ID: mvp2_grpo_flatnli_r5
1901	STATUS: DONE
1902	CREATED_AT: 2026-05-14T16:55:02.197Z
1903	UPDATED_AT: 2026-05-14T17:26:55.692Z
1904	CONCLUSION: killed
1905	COMMAND: bash -c "source /etc/network_turbo && ... && python -m freige.training.grpo_trainer --stage 2 --kl_coef 0.01 --num_generations 8 --max_steps 200 --resume_from_checkpoint /root/autodl-tmp/grpo_flatnli_r3/checkpoint-100 ..."
1906	SPEC.server: rtx5090-4x
1907	SPEC.gpu: ['cuda:3']
1908	SPEC.pid: 73407
1909	SPEC.log_path: ~/runs/faith-evidence-ie/mvp2_grpo_flatnli_r5.log
1910	SPEC.submitted_at: 2026-05-14T16:56:01.219Z
1911	SPEC.submitted_via: submit_training_job
1912	SPEC.backend: tmux
1913	SPEC.account: root
1914	SPEC.data_path: /root/autodl-tmp/data/docred
1915	SPEC.data_count: {'train': 3027, 'dev': 985}
1916	SPEC.model_name: Qwen3-4B
1917	SPEC.seed: 42
1918	SPEC.checkpoint_source: /root/autodl-tmp/sft_output
1919	SPEC.eval_data: /root/autodl-tmp/data/docred
1920	SPEC.wall_clock_seconds: 1854.5
1921	SPEC.gpu_hours: 0.52
1922	
1923	========================================================================================================================
1924	EXP_ID: mvp2_grpo_flatnli_r6
1925	STATUS: DONE
1926	CREATED_AT: 2026-05-14T17:25:07.083Z
1927	UPDATED_AT: 2026-05-14T18:17:52.909Z
1928	CONCLUSION: negative
1929	METRICS: {
1930	  "steps_completed": 25,
1931	  "final_frac_zero_std": 0.9,
1932	  "final_f1_reward": 0,
1933	  "final_flat_nli_reward": 0,
1934	  "final_format_reward": 0.293,
1935	  "collapse_step": 25
1936	}
1937	COMMAND: bash -c "source /etc/network_turbo && ... && PYTHONUNBUFFERED=1 python -m freige.training.grpo_trainer --stage 2 --kl_coef 0.01 --num_generations 8 --max_steps 100 --wandb_run_name grpo-s2-flatnli-r6"
1938	SPEC.server: rtx5090-4x
1939	SPEC.gpu: ['cuda:3']
1940	SPEC.pid: 76958
1941	SPEC.log_path: ~/runs/faith-evidence-ie/mvp2_grpo_flatnli_r6.log
1942	SPEC.submitted_at: 2026-05-14T17:25:30.099Z
1943	SPEC.submitted_via: submit_training_job
1944	SPEC.backend: tmux
1945	SPEC.account: root
1946	SPEC.data_path: /root/autodl-tmp/data/docred
1947	SPEC.data_count: {'train': 3027, 'dev': 985}
1948	SPEC.model_name: Qwen3-4B
1949	SPEC.seed: 42
1950	SPEC.checkpoint_source: /root/autodl-tmp/sft_output
1951	SPEC.eval_data: /root/autodl-tmp/data/docred/dev.json
1952	SPEC.wall_clock_seconds: 3061.0
1953	SPEC.gpu_hours: 0.85
1954	
1955	========================================================================================================================
1956	EXP_ID: mvp2_rsft_ced_scoring
1957	STATUS: DONE
1958	CREATED_AT: 2026-05-15T05:27:32.788Z
1959	UPDATED_AT: 2026-05-15T05:33:16.769Z
1960	CONCLUSION: success
1961	METRICS: {
1962	  "input_generations": 21952,
1963	  "selected_samples": 2718,
1964	  "unique_docs": 2691,
1965	  "selection_rate": 0.124,
1966	  "mean_f1": 0.6157,
1967	  "mean_ced": 0.6683,
1968	  "f1_range": [
1969	    0.1026,
1970	    1
1971	  ],
1972	  "zero_f1_samples": 0,
1973	  "selection_strategy": "top_k=1",
1974	  "f1_threshold": 0.1
1975	}
1976	COMMAND: python -m freige.training.rsft_score_filter --input_dir /root/autodl-tmp/rsft_generations --output_path /root/autodl-tmp/rsft_filtered/rsft_train.jsonl --selection_strategy top_k --top_k 1 --f1_threshold 0.1
1977	SPEC.server: rtx5090-4x
1978	SPEC.data_path: /root/autodl-tmp/rsft_generations/
1979	SPEC.data_count: 21952
1980	SPEC.model_name: cross-encoder/nli-deberta-v3-base
1981	SPEC.seed: 42
1982	SPEC.checkpoint_path: /root/autodl-tmp/rsft_filtered/rsft_train.jsonl
1983	SPEC.log_path: /root/autodl-tmp/rsft_filtered/rsft_combined_report.json
1984	
1985	========================================================================================================================
1986	EXP_ID: mvp2_rsft_ced_scoring_topk3
1987	STATUS: DONE
1988	CREATED_AT: 2026-05-15T07:35:23.225Z
1989	UPDATED_AT: 2026-05-15T13:20:42.443Z
1990	CONCLUSION: killed
1991	COMMAND: python -m freige.training.rsft_score_filter --input_dir /root/autodl-tmp/rsft_generations --output_path /root/autodl-tmp/rsft_filtered_topk3 --nli_model_path cross-encoder/nli-deberta-v3-base --nli_device cuda:0 --selection_strategy top_k --top_k 3 --f1_threshold 0.1 --tau 0.5
1992	SPEC.server: rtx5090-4x
1993	SPEC.gpu: ['cuda:3']
1994	SPEC.pid: 198680
1995	SPEC.log_path: ~/runs/faith-evidence-ie/mvp2_rsft_ced_scoring_topk3.log
1996	SPEC.submitted_at: 2026-05-15T12:09:41.690Z
1997	SPEC.submitted_via: submit_training_job
1998	SPEC.backend: tmux
1999	SPEC.account: root
2000	SPEC.data_path: /root/autodl-tmp/rsft_generations/generations.jsonl
2001	SPEC.data_count: 21952
2002	SPEC.model_name: cross-encoder/nli-deberta-v3-base
2003	SPEC.seed: 42
2004	SPEC.wall_clock_seconds: 4260.8
2005	SPEC.gpu_hours: 1.18
2006	
2007	========================================================================================================================
2008	EXP_ID: mvp2_rsft_ced_scoring_topk3_r2
2009	STATUS: DONE
2010	CREATED_AT: 2026-05-15T12:12:38.363Z
2011	UPDATED_AT: 2026-05-15T13:53:08.461Z
2012	CONCLUSION: success
2013	METRICS: {
2014	  "input_generations": 21728,
2015	  "selected_samples": 8037,
2016	  "unique_docs": 2691,
2017	  "selection_rate": 0.37,
2018	  "mean_f1": 0.5761,
2019	  "mean_ced": 0.6205,
2020	  "mean_combined": 0.6787,
2021	  "f1_range_p25": 0.444,
2022	  "f1_range_p75": 0.717,
2023	  "ced_range_p25": 0.487,
2024	  "ced_range_p75": 0.774,
2025	  "truncated_samples": 1924,
2026	  "truncated_pct": 8.9,
2027	  "selection_strategy": "top_k=3",
2028	  "f1_threshold": 0.1,
2029	  "topk1_samples": 2718,
2030	  "data_multiplier": 2.96
2031	}
2032	COMMAND: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && rm -rf /root/autodl-tmp/rsft_filtered_topk3/* && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_score_filter --input_dir /root/autodl-tmp/rsft_generations --output_path /root/autodl-tmp/rsft_filtered_topk3 --nli_model_path cross-encoder/nli-deberta-v3-base --nli_device cuda:0 --selection_strategy top_k --top_k 3 --f1_threshold 0.1 --tau 0.5"
2033	SPEC.server: rtx5090-4x
2034	SPEC.gpu: ['cuda:0']
2035	SPEC.pid: 198997
2036	SPEC.log_path: ~/runs/faith-evidence-ie/mvp2_rsft_ced_scoring_topk3_r2.log
2037	SPEC.submitted_at: 2026-05-15T12:13:03.900Z
2038	SPEC.submitted_via: submit_training_job
2039	SPEC.backend: tmux
2040	SPEC.account: root
2041	SPEC.wall_clock_seconds: 4584.8
2042	SPEC.gpu_hours: 1.27
2043	SPEC.note: NLI 推理实际跑在 cuda:0 (--nli_device cuda:0)，非 cuda:3。Registry gpu 字段已修正。
2044	
2045	========================================================================================================================
2046	EXP_ID: mvp2_rsft_generate
2047	STATUS: DONE
2048	CREATED_AT: 2026-05-15T00:09:41.289Z
2049	UPDATED_AT: 2026-05-15T01:32:10.047Z
2050	CONCLUSION: failed
2051	COMMAND: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/autodl-tmp && python -m freige.training.rsft_generate --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split train_annotated --output_dir /root/autodl-tmp/rsft_generations --num_generations 8 --temperature 0.7 --batch_size 2 --max_new_tokens 1024 --seed 42"
2052	SPEC.server: rtx5090-4x
2053	SPEC.gpu: ['cuda:1']
2054	SPEC.pid: 122144
2055	SPEC.log_path: ~/runs/faith-evidence-ie/mvp2_rsft_generate.log
2056	SPEC.submitted_at: 2026-05-15T00:09:53.637Z
2057	SPEC.submitted_via: submit_training_job
2058	SPEC.backend: tmux
2059	SPEC.account: root
2060	SPEC.wall_clock_seconds: 4936.4
2061	SPEC.gpu_hours: 1.37
2062	
2063	========================================================================================================================
2064	EXP_ID: mvp2_rsft_r2a
2065	STATUS: DONE
2066	CREATED_AT: 2026-05-15T08:57:46.140Z
2067	UPDATED_AT: 2026-05-15T13:14:22.509Z
2068	CONCLUSION: success
2069	METRICS: {
2070	  "rel_f1": 0.4494,
2071	  "evi_f1": 0.8108,
2072	  "edcr": 0.6641,
2073	  "sft_baseline_rel_f1": 0.4057,
2074	  "sft_baseline_evi_f1": 0.7979,
2075	  "delta_rel_f1": 0.0437,
2076	  "delta_evi_f1": 0.0129,
2077	  "mvp2_pass": true
2078	}
2079	COMMAND: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train_clean.jsonl --output_dir /root/autodl-tmp/rsft_output_r2a --learning_rate 2e-5 --num_epochs 1 --per_device_batch_size 4 --gradient_accumulation_steps 4 --lora_rank 64 --lora_alpha 128 --weighted_sampling --save_steps 50 --eval_data_dir /root/autodl-tmp/data/docred --eval_max_docs 50 --wandb_run_name rsft-r2a --seed 42"
2080	SPEC.server: rtx5090-4x
2081	SPEC.gpu: ['cuda:1']
2082	SPEC.pid: 183504
2083	SPEC.log_path: ~/runs/faith-evidence-ie/mvp2_rsft_r2a.log
2084	SPEC.submitted_at: 2026-05-15T08:59:58.168Z
2085	SPEC.submitted_via: submit_training_job
2086	SPEC.backend: tmux
2087	SPEC.account: root
2088	SPEC.checkpoint_path: /root/autodl-tmp/rsft_output_r2a
2089	SPEC.wall_clock_seconds: 15264.3
2090	SPEC.gpu_hours: 4.24
2091	
2092	========================================================================================================================
2093	EXP_ID: mvp2_rsft_r2b
2094	STATUS: DONE
2095	CREATED_AT: 2026-05-15T08:57:46.813Z
2096	UPDATED_AT: 2026-05-15T13:14:23.368Z
2097	CONCLUSION: success
2098	METRICS: {
2099	  "rel_f1": 0.4493,
2100	  "evi_f1": 0.8128,
2101	  "edcr": 0.6609,
2102	  "sft_baseline_rel_f1": 0.4057,
2103	  "sft_baseline_evi_f1": 0.7979,
2104	  "delta_rel_f1": 0.0436,
2105	  "delta_evi_f1": 0.0149,
2106	  "mvp2_pass": true
2107	}
2108	COMMAND: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train_clean.jsonl --output_dir /root/autodl-tmp/rsft_output_r2b --learning_rate 1e-5 --num_epochs 1 --per_device_batch_size 4 --gradient_accumulation_steps 4 --lora_rank 64 --lora_alpha 32 --weighted_sampling --save_steps 50 --eval_data_dir /root/autodl-tmp/data/docred --eval_max_docs 50 --wandb_run_name rsft-r2b --seed 42"
2109	SPEC.server: rtx5090-4x
2110	SPEC.gpu: ['cuda:3']
2111	SPEC.pid: 183587
2112	SPEC.log_path: ~/runs/faith-evidence-ie/mvp2_rsft_r2b.log
2113	SPEC.submitted_at: 2026-05-15T09:00:01.270Z
2114	SPEC.submitted_via: submit_training_job
2115	SPEC.backend: tmux
2116	SPEC.account: root
2117	SPEC.checkpoint_path: /root/autodl-tmp/rsft_output_r2b
2118	SPEC.wall_clock_seconds: 15262.1
2119	SPEC.gpu_hours: 4.24
2120	
2121	========================================================================================================================
2122	EXP_ID: mvp2_rsft_train_r1
2123	STATUS: DONE
2124	CREATED_AT: 2026-05-15T05:27:39.073Z
2125	UPDATED_AT: 2026-05-15T09:40:39.078Z
2126	CONCLUSION: success
2127	METRICS: {
2128	  "rel_f1": 0.0483,
2129	  "num_preds": 848,
2130	  "sft_baseline_rel_f1": 0.4057,
2131	  "failure_mode": "relation_ontology_collapse_to_freetext",
2132	  "epoch1_eval_loss": 0.756,
2133	  "epoch2_eval_loss": 0.759
2134	}
2135	COMMAND: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output --learning_rate 2e-5 --num_epochs 3 --per_device_batch_size 4 --gradient_accumulation_steps 4 --lora_rank 64 --lora_alpha 128 --weighted_sampling --eval_data_dir /root/autodl-tmp/data/docred --eval_max_docs 50 --wandb_run_name rsft-ced-r1 --seed 42"
2136	SPEC.server: rtx5090-4x
2137	SPEC.gpu: ['cuda:0']
2138	SPEC.pid: 165130
2139	SPEC.log_path: ~/runs/faith-evidence-ie/mvp2_rsft_train_r1.log
2140	SPEC.submitted_at: 2026-05-15T05:37:57.880Z
2141	SPEC.submitted_via: submit_training_job
2142	SPEC.backend: tmux
2143	SPEC.account: root
2144	SPEC.wall_clock_seconds: 7210.1
2145	SPEC.gpu_hours: 2.0
2146	
2147	========================================================================================================================
2148	EXP_ID: mvp2_rsft_train_r1_s43
2149	STATUS: DONE
2150	CREATED_AT: 2026-05-15T05:36:25.275Z
2151	UPDATED_AT: 2026-05-15T11:31:48.727Z
2152	CONCLUSION: success
2153	METRICS: {
2154	  "eval_loss": 0.7622,
2155	  "train_loss": 0.6148,
2156	  "eval_entropy": 0.6724,
2157	  "mean_token_accuracy": 0.8291,
2158	  "total_steps": 510,
2159	  "epochs": 3,
2160	  "training_hours": 1.99
2161	}
2162	COMMAND: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output_s43 --learning_rate 2e-5 --num_epochs 3 --per_device_batch_size 4 --gradient_accumulation_steps 4 --lora_rank 64 --lora_alpha 128 --weighted_sampling --eval_data_dir /root/autodl-tmp/data/docred --eval_max_docs 50 --wandb_run_name rsft-ced-r1-s43 --seed 43"
2163	SPEC.server: rtx5090-4x
2164	SPEC.gpu: ['cuda:1']
2165	SPEC.pid: 165590
2166	SPEC.log_path: ~/runs/faith-evidence-ie/mvp2_rsft_train_r1_s43.log
2167	SPEC.submitted_at: 2026-05-15T05:39:20.307Z
2168	SPEC.submitted_via: submit_training_job
2169	SPEC.backend: tmux
2170	SPEC.account: root
2171	SPEC.wall_clock_seconds: 21148.4
2172	SPEC.gpu_hours: 5.87
2173	
2174	========================================================================================================================
2175	EXP_ID: mvp2_rsft_train_r1_s44
2176	STATUS: DONE
2177	CREATED_AT: 2026-05-15T05:36:26.321Z
2178	UPDATED_AT: 2026-05-15T13:27:38.819Z
2179	CONCLUSION: success
2180	METRICS: {
2181	  "rel_f1": 0.4655,
2182	  "evi_f1": 0.8087,
2183	  "evi_f1_joint": 0.3713,
2184	  "evi_f1_joint_P": 0.3775,
2185	  "evi_f1_joint_R": 0.3653,
2186	  "edcr": 0.635,
2187	  "sft_baseline_rel_f1": 0.4057,
2188	  "sft_baseline_evi_f1": 0.7979,
2189	  "delta_rel_f1": 0.0598,
2190	  "delta_evi_f1": 0.0108,
2191	  "delta_evi_f1_joint": 0.0596,
2192	  "mvp2_pass": true
2193	}
2194	COMMAND: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output_s44 --learning_rate 2e-5 --num_epochs 3 --per_device_batch_size 4 --gradient_accumulation_steps 4 --lora_rank 64 --lora_alpha 128 --weighted_sampling --eval_data_dir /root/autodl-tmp/data/docred --eval_max_docs 50 --wandb_run_name rsft-ced-r1-s44 --seed 44"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "e8fe885f-f3f2-44de-b758-861a96dee82f"
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
  "task_id": "aa0dedafabeeb8ab6",
  "tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "description": "Reading /tmp/4b_experiments_full.txt",
  "usage": {
    "total_tokens": 78739,
    "tool_uses": 16,
    "duration_ms": 85115
  },
  "last_tool_name": "Read",
  "uuid": "7c8c5c2e-5b73-4739-937d-cdb793c89003",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0"
}
```

---


### Tool call

_source line 61_

<details open><summary>🔧 Tool call — Read · `toolu_017rcsYzPhwSTZHatdhsFdWC`</summary>

```json
{
  "file_path": "/tmp/4b_experiments_full.txt",
  "offset": 2194,
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "47afbc02-e4fd-4a2b-b303-e5b6263f94f9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019hnrQAZk9vbNutHbMEP4th",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9620,
      "cache_read_input_tokens": 68690,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9620,
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

_source line 62 · 2026-05-18T22:03:48.226Z_

<details><summary>↩ Tool result · `toolu_017rcsYzPhwSTZHatdhsFdWC`</summary>

```text
2194	COMMAND: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output_s44 --learning_rate 2e-5 --num_epochs 3 --per_device_batch_size 4 --gradient_accumulation_steps 4 --lora_rank 64 --lora_alpha 128 --weighted_sampling --eval_data_dir /root/autodl-tmp/data/docred --eval_max_docs 50 --wandb_run_name rsft-ced-r1-s44 --seed 44"
2195	SPEC.server: rtx5090-4x
2196	SPEC.gpu: ['cuda:2']
2197	SPEC.pid: 165672
2198	SPEC.log_path: ~/runs/faith-evidence-ie/mvp2_rsft_train_r1_s44.log
2199	SPEC.submitted_at: 2026-05-15T05:39:22.747Z
2200	SPEC.submitted_via: submit_training_job
2201	SPEC.backend: tmux
2202	SPEC.account: root
2203	SPEC.checkpoint_path: /root/autodl-tmp/rsft_output_s44
2204	SPEC.wall_clock_seconds: 27283.5
2205	SPEC.gpu_hours: 7.58
2206	
2207	========================================================================================================================
2208	EXP_ID: mvp2_sft_eval
2209	STATUS: DONE
2210	CREATED_AT: 2026-05-14T07:10:37.449Z
2211	UPDATED_AT: 2026-05-14T12:46:04.523Z
2212	CONCLUSION: killed
2213	COMMAND: python -m freige.eval.inference --model_path sft_output --base_model Qwen3-4B --split dev
2214	SPEC.server: rtx5090-4x
2215	SPEC.gpu: ['cuda:1']
2216	SPEC.pid: 47293
2217	SPEC.log_path: ~/runs/faith-evidence-ie/mvp2_sft_eval.log
2218	SPEC.submitted_at: 2026-05-14T11:48:46.335Z
2219	SPEC.submitted_via: submit_training_job
2220	SPEC.backend: tmux
2221	SPEC.account: root
2222	SPEC.data_path: /root/autodl-tmp/data/docred
2223	SPEC.data_count: {'dev': 985}
2224	SPEC.model_name: Qwen3-4B
2225	SPEC.seed: 42
2226	SPEC.hypothesis: SFT baseline eval on DocRED dev set
2227	SPEC.parent: mvp2_sft_warmup
2228	SPEC.checkpoint_source: /root/autodl-tmp/sft_output
2229	SPEC.eval_data: /root/autodl-tmp/data/docred/dev.json
2230	SPEC.wall_clock_seconds: 3416.3
2231	SPEC.gpu_hours: 0.95
2232	
2233	========================================================================================================================
2234	EXP_ID: mvp2_sft_eval_r2
2235	STATUS: DONE
2236	CREATED_AT: 2026-05-14T12:45:46.160Z
2237	UPDATED_AT: 2026-05-14T14:54:07.338Z
2238	CONCLUSION: success
2239	METRICS: {
2240	  "rel_f1": 0.4057,
2241	  "ign_f1": 0.4057,
2242	  "evi_f1": 0.7979,
2243	  "edcr": 0.7118,
2244	  "precision": 0.4043,
2245	  "recall": 0.407,
2246	  "evi_precision": 0.8035,
2247	  "evi_recall": 0.7924,
2248	  "format_ok_rate": 0.998,
2249	  "format_compliance_rate": 0.626,
2250	  "n_parseable": 617,
2251	  "n_truncated": 367,
2252	  "n_predictions": 18815,
2253	  "inference_time_seconds": 6484.7
2254	}
2255	COMMAND: python -m freige.eval.inference --model_path /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --quantize --output_dir /root/autodl-tmp/sft_eval_results --seed 42
2256	SPEC.server: rtx5090-4x
2257	SPEC.gpu: ['cuda:1']
2258	SPEC.pid: 55410
2259	SPEC.log_path: ~/runs/faith-evidence-ie/mvp2_sft_eval_r2.log
2260	SPEC.submitted_at: 2026-05-14T12:45:45.981Z
2261	SPEC.submitted_via: submit_training_job
2262	SPEC.backend: tmux
2263	SPEC.account: root
2264	SPEC.data_path: /root/autodl-tmp/data/docred
2265	SPEC.data_count: {'dev': 985}
2266	SPEC.model_name: Qwen3-4B
2267	SPEC.seed: 42
2268	SPEC.hypothesis: SFT baseline eval on DocRED dev set (batch_size=16 accelerated)
2269	SPEC.parent: mvp2_sft_warmup
2270	SPEC.checkpoint_source: /root/autodl-tmp/sft_output
2271	SPEC.eval_data: /root/autodl-tmp/data/docred/dev.json
2272	SPEC.wall_clock_seconds: 7701.4
2273	SPEC.gpu_hours: 2.14
2274	
2275	========================================================================================================================
2276	EXP_ID: mvp2_sft_eval_r3
2277	STATUS: DONE
2278	CREATED_AT: 2026-05-14T13:52:38.174Z
2279	UPDATED_AT: 2026-05-14T17:06:57.010Z
2280	CONCLUSION: success
2281	METRICS: {
2282	  "rel_f1": 0.4057,
2283	  "ign_f1": 0.4057,
2284	  "evi_f1": 0.7979,
2285	  "edcr": 0.7118,
2286	  "precision": 0.4043,
2287	  "recall": 0.407,
2288	  "evi_precision": 0.8035,
2289	  "evi_recall": 0.7924,
2290	  "format_ok_rate": 0.998,
2291	  "format_compliance_rate": 0.626,
2292	  "n_parseable": 617,
2293	  "n_truncated": 367,
2294	  "n_predictions": 18815
2295	}
2296	COMMAND: bash -c "source /etc/network_turbo && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.eval.inference --model_path /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --quantize --output_dir /root/autodl-tmp/sft_eval_r3_results --seed 42"
2297	SPEC.server: rtx5090-4x
2298	SPEC.gpu: ['cuda:1']
2299	SPEC.pid: 62352
2300	SPEC.log_path: ~/runs/faith-evidence-ie/mvp2_sft_eval_r3.log
2301	SPEC.submitted_at: 2026-05-14T14:53:52.360Z
2302	SPEC.submitted_via: submit_training_job
2303	SPEC.backend: tmux
2304	SPEC.account: root
2305	SPEC.data_path: /root/autodl-tmp/data/docred
2306	SPEC.data_count: {'dev': 985}
2307	SPEC.model_name: Qwen3-4B
2308	SPEC.seed: 42
2309	SPEC.hypothesis: SFT baseline eval with unified eval code (consolidated parse_model_output) for fair comparison with r2
2310	SPEC.parent: mvp2_sft_warmup
2311	SPEC.checkpoint_source: /root/autodl-tmp/sft_output
2312	SPEC.eval_data: /root/autodl-tmp/data/docred/dev.json
2313	SPEC.wall_clock_seconds: 7718.1
2314	SPEC.gpu_hours: 2.14
2315	
2316	========================================================================================================================
2317	EXP_ID: mvp2_sft_warmup
2318	STATUS: DONE
2319	CREATED_AT: 2026-05-14T06:09:47.819Z
2320	UPDATED_AT: 2026-05-14T07:10:19.285Z
2321	CONCLUSION: success
2322	METRICS: {
2323	  "eval_loss": 0.72,
2324	  "accuracy": 0.835
2325	}
2326	COMMAND: accelerate launch --config_file freige/configs/accelerate_4gpu.yaml -m freige.training.sft_trainer --model_name /root/autodl-tmp/models/Qwen3-4B --data_dir /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/sft_output --deepspeed freige/configs/deepspeed_zero2.json --num_epochs 3 --per_device_batch_size 1 --gradient_accumulation_steps 16 --learning_rate 2e-4 --max_length 4096 --seed 42
2327	SPEC.server: rtx5090-4x
2328	SPEC.gpu: ['cuda:0', 'cuda:1', 'cuda:2', 'cuda:3']
2329	SPEC.pid: 16221
2330	SPEC.log_path: ~/runs/faith-evidence-ie/mvp2_sft_warmup.log
2331	SPEC.submitted_at: 2026-05-14T06:22:10.453Z
2332	SPEC.submitted_via: submit_training_job
2333	SPEC.backend: tmux
2334	SPEC.account: root
2335	SPEC.data_path: /root/autodl-tmp/data/docred
2336	SPEC.data_count: {'train': 3027, 'dev': 985}
2337	SPEC.model_name: Qwen3-4B
2338	SPEC.seed: 42
2339	SPEC.gpu_model: RTX 5090 32GB x4
2340	SPEC.lora_rank: 64
2341	SPEC.lora_alpha: 128
2342	SPEC.quantization: 4-bit NF4 QLoRA
2343	SPEC.deepspeed: ZeRO-2 + CPU offload
2344	SPEC.effective_batch_size: 64
2345	SPEC.checkpoint_path: /root/autodl-tmp/sft_output
2346	SPEC.wall_clock_seconds: 2888.8
2347	SPEC.gpu_hours: 3.21
2348	
2349	========================================================================================================================
2350	EXP_ID: plan_001_flat_nli_scoring
2351	STATUS: DONE
2352	CREATED_AT: 2026-05-15T14:36:56.213Z
2353	UPDATED_AT: 2026-05-15T15:21:03.475Z
2354	CONCLUSION: success
2355	METRICS: {
2356	  "total_scored": 21728,
2357	  "selected_samples": 2691,
2358	  "selection_rate": 0.124,
2359	  "selection_strategy": "top_k=1",
2360	  "f1_threshold": 0.1,
2361	  "output_path": "/root/autodl-tmp/rsft_filtered_flat_nli/rsft_train.jsonl"
2362	}
2363	COMMAND: python -m freige.training.rsft_score_filter --scoring_mode flat_nli --top_k 3 --f1_threshold 0.1
2364	SPEC.server: rtx5090-4x
2365	SPEC.gpu: ['cuda:3']
2366	SPEC.pid: 208155
2367	SPEC.model_name: DeBERTa-v3-large-mnli-fever-anli-ling-wanli
2368	SPEC.data_path: /root/autodl-tmp/rsft_generations
2369	SPEC.data_count: 21728
2370	SPEC.seed: 42
2371	
2372	========================================================================================================================
2373	EXP_ID: plan_001_flat_nli_seed43
2374	STATUS: DONE
2375	CREATED_AT: 2026-05-15T18:22:55.521Z
2376	UPDATED_AT: 2026-05-15T20:35:05.452Z
2377	CONCLUSION: success
2378	METRICS: {
2379	  "train_loss_final": 0.6257,
2380	  "train_loss_min": 0.5895,
2381	  "eval_loss_epoch3": 0.7567,
2382	  "eval_accuracy_epoch3": 0.8298,
2383	  "total_steps": 507,
2384	  "epochs": 3,
2385	  "train_runtime_seconds": 6880,
2386	  "task_eval_f1_ep1": 0.4825,
2387	  "task_eval_f1_ep2": 0.4542,
2388	  "task_eval_f1_ep3": 0.4866,
2389	  "task_eval_evi_f1_ep3": 0.7834,
2390	  "task_eval_edcr_ep3": 0.6402,
2391	  "task_eval_note": "50-doc subset, not full dev"
2392	}
2393	COMMAND: python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_data_path /root/autodl-tmp/rsft_filtered_flat_nli/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output_flat_nli_s43 --learning_rate 2e-5 --num_epochs 3 --per_device_batch_size 1 --gradient_accumulation_steps 16 --lora_rank 64 --lora_alpha 128 --eval_data_dir /root/autodl-tmp/data/docred --wandb_run_name plan_001_flat_nli_seed43 --seed 43
2394	SPEC.hypothesis: flat-NLI RSFT seed=43 补跑。验证 seed=42 的 rel_f1=0.4539 是否在噪声范围内（CED RSFT 3-seed mean=0.4596, σ=0.0127）。
2395	SPEC.parent: plan_001_rsft_flat_nli
2396	SPEC.server: rtx5090-4x
2397	SPEC.gpu: ['cuda:0']
2398	SPEC.data_path: /root/autodl-tmp/rsft_filtered_flat_nli/rsft_train.jsonl
2399	SPEC.data_count: 2691
2400	SPEC.model_name: Qwen3-4B + SFT adapter
2401	SPEC.seed: 43
2402	SPEC.checkpoint_source: /root/autodl-tmp/sft_output
2403	SPEC.eval_data: N/A (training)
2404	SPEC.checkpoint_path: /root/autodl-tmp/rsft_output_flat_nli_s43
2405	SPEC.log_path: ~/runs/faith-evidence-ie/plan_001_flat_nli_seed43.log
2406	SPEC.pid: 236774
2407	SPEC.submitted_at: 2026-05-15T18:22:00Z
2408	SPEC.submitted_via: worker_direct
2409	SPEC.backend: nohup
2410	SPEC.wall_clock_seconds: 7600.2
2411	SPEC.gpu_hours: 2.11
2412	
2413	========================================================================================================================
2414	EXP_ID: plan_001_flat_nli_seed44
2415	STATUS: DONE
2416	CREATED_AT: 2026-05-15T21:38:26.174Z
2417	UPDATED_AT: 2026-05-15T23:25:30.719Z
2418	CONCLUSION: success
2419	METRICS: {
2420	  "train_loss": 0.6247,
2421	  "eval_loss": 0.7564,
2422	  "eval_mean_token_accuracy": 0.8299,
2423	  "task_eval_f1_ep1": 0.4306,
2424	  "task_eval_f1_ep2": 0.4884,
2425	  "task_eval_f1_ep3": 0.4897,
2426	  "task_eval_evi_f1_ep3": 0.78,
2427	  "task_eval_edcr_ep3": 0.6596,
2428	  "task_eval_ign_f1_ep3": 0.4897,
2429	  "train_runtime_sec": 6197,
2430	  "num_epochs": 3,
2431	  "total_steps": 507
2432	}
2433	COMMAND: rsft train flat_nli seed=44
2434	SPEC.server: rtx5090-4x
2435	SPEC.gpu: cuda:0
2436	SPEC.pid: 258503
2437	SPEC.log_path: ~/runs/faith-evidence-ie/plan_001_flat_nli_seed44.log
2438	SPEC.submitted_at: 2026-05-15T21:38:25.857Z
2439	SPEC.submitted_via: submit_training_job
2440	SPEC.backend: tmux
2441	SPEC.account: root
2442	SPEC.data_path: /root/autodl-tmp/rsft_filtered_flat_nli/rsft_train.jsonl
2443	SPEC.data_count: 2691
2444	SPEC.model_name: Qwen3-4B + SFT adapter
2445	SPEC.seed: 44
2446	SPEC.checkpoint_source: /root/autodl-tmp/sft_output
2447	SPEC.checkpoint_path: /root/autodl-tmp/rsft_output_flat_nli_s44
2448	SPEC.wall_clock_seconds: 6424.9
2449	SPEC.gpu_hours: 1.78
2450	
2451	========================================================================================================================
2452	EXP_ID: plan_001_flat_nli_seed45
2453	STATUS: DONE
2454	CREATED_AT: 2026-05-15T21:09:05.195Z
2455	UPDATED_AT: 2026-05-15T23:17:29.971Z
2456	CONCLUSION: success
2457	METRICS: {
2458	  "task_eval_rel_f1": 0.4876,
2459	  "task_eval_evi_f1": 0.7927,
2460	  "task_eval_edcr": 0.6517,
2461	  "train_loss": 0.6245,
2462	  "runtime_hours": 1.69,
2463	  "note": "task-eval on 50 docs only, full dev eval needed"
2464	}
2465	COMMAND: flat-NLI RSFT training seed=45
2466	SPEC.server: rtx5090-4x
2467	SPEC.gpu: cuda:2
2468	SPEC.pid: 257187
2469	SPEC.log_path: ~/runs/faith-evidence-ie/plan_001_flat_nli_seed45.log
2470	SPEC.submitted_at: 2026-05-15T21:26:10.157Z
2471	SPEC.submitted_via: submit_training_job
2472	SPEC.backend: tmux
2473	SPEC.account: root
2474	SPEC.data_path: /root/autodl-tmp/rsft_filtered_flat_nli/rsft_train.jsonl
2475	SPEC.data_count: 0
2476	SPEC.model_name: Qwen3-4B + SFT adapter
2477	SPEC.seed: 45
2478	SPEC.wall_clock_seconds: 6240.8
2479	SPEC.gpu_hours: 1.73
2480	
2481	========================================================================================================================
2482	EXP_ID: plan_001_rsft_flat_nli
2483	STATUS: DONE
2484	CREATED_AT: 2026-05-15T15:40:01.021Z
2485	UPDATED_AT: 2026-05-15T18:04:14.547Z
2486	CONCLUSION: success
2487	METRICS: {
2488	  "train_loss": 0.6238,
2489	  "train_loss_min": 0.5803,
2490	  "mean_token_accuracy": 0.8528,
2491	  "train_runtime_sec": 2946,
2492	  "epochs": 3,
2493	  "total_steps": 507,
2494	  "samples": 2691
2495	}
2496	COMMAND: python rsft_train.py (flat-NLI scoring)
2497	SPEC.gpu: ['cuda:0']
2498	SPEC.server: rtx5090-4x
2499	SPEC.data_path: /root/autodl-tmp/rsft_filtered_flat_nli/rsft_train.jsonl
2500	SPEC.data_count: 2691
2501	SPEC.model_name: Qwen3-4B + SFT adapter
2502	SPEC.pid: 219556
2503	SPEC.log_path: /root/runs/faith-evidence-ie/plan_001_rsft_flat_nli.log
2504	SPEC.checkpoint_source: /root/autodl-tmp/sft_output
2505	SPEC.eval_data: N/A (training, not eval)
2506	SPEC.checkpoint_path: /root/autodl-tmp/rsft_output_flat_nli/
2507	
2508	========================================================================================================================
2509	EXP_ID: plan_002_test_eval_s44
2510	STATUS: DONE
2511	CREATED_AT: 2026-05-15T18:05:47.701Z
2512	UPDATED_AT: 2026-05-15T18:20:17.405Z
2513	CONCLUSION: failed
2514	COMMAND: python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_s44 --sft_adapter /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split test --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/test_rsft_s44 --no-quantize
2515	SPEC.hypothesis: RSFT s44 checkpoint on DocRED test set should achieve similar or better performance than dev set results, validating generalization of the faithfulness-evidence approach.
2516	SPEC.task_type: eval
2517	SPEC.eval_data: docred_test
2518	SPEC.data_path: /root/autodl-tmp/data/docred
2519	SPEC.data_count: 1000
2520	SPEC.model_name: Qwen3-4B + SFT + RSFT-s44
2521	SPEC.seed: 42
2522	SPEC.checkpoint_source: /root/autodl-tmp/rsft_output_s44
2523	SPEC.server: rtx5090-4x
2524	SPEC.gpu: cuda:0
2525	SPEC.log_path: /root/autodl-tmp/eval_results/test_rsft_s44.log
2526	SPEC.checkpoint_path: /root/autodl-tmp/eval_results/test_rsft_s44
2527	SPEC.tmux_session: plan_002_test_eval_s44
2528	
2529	========================================================================================================================
2530	EXP_ID: plan_002_test_eval_s44_r2
2531	STATUS: DONE
2532	CREATED_AT: 2026-05-16T08:14:36.494Z
2533	UPDATED_AT: 2026-05-17T02:56:29.283Z
2534	CONCLUSION: success
2535	COMMAND: CUDA_VISIBLE_DEVICES=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_s44/checkpoint-510 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split test --batch_size 4 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/test_rsft_ced_s44 --no-quantize
2536	SPEC.server: rtx5090-4x
2537	SPEC.gpu_id: 1
2538	SPEC.pid: 319632
2539	SPEC.data_path: /root/autodl-tmp/data/docred/test.json
2540	SPEC.data_count: 1000
2541	SPEC.model_name: Qwen3-4B + SFT + RSFT-CED-s44-ckpt510
2542	SPEC.seed: 42
2543	SPEC.hypothesis: DocRED test set evaluation with RSFT CED s44 (best config). D076 协议. plan_id=plan_002, claim=1.
2544	SPEC.parent: mvp2_rsft_train_r1_s44
2545	SPEC.checkpoint_source: /root/autodl-tmp/rsft_output_s44/checkpoint-510
2546	SPEC.eval_data: /root/autodl-tmp/data/docred/test.json
2547	SPEC.log_path: /root/autodl-tmp/eval_results/test_rsft_ced_s44/eval.log
2548	SPEC.metrics: {'n_documents': 1000, 'n_predictions': 26925, 'n_codalab_entries': 25553, 'format_ok_rate': 0.996, 'n_truncated': 626, 'inference_time_s': 13850.5}
2549	SPEC.checkpoint_path: /root/autodl-tmp/eval_results/test_rsft_ced_s44
2550	SPEC.notes: Test set eval complete. No local F1 (need CodaLab submission). File: codalab_submission.json (25553 entries).
2551	
2552	========================================================================================================================
2553	EXP_ID: plan_002_test_rsft_s43
2554	STATUS: DONE
2555	CREATED_AT: 2026-05-16T17:45:04.744Z
2556	UPDATED_AT: 2026-05-16T21:07:17.492Z
2557	CONCLUSION: failed
2558	COMMAND: CUDA_VISIBLE_DEVICES=1 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510 --data_path /root/autodl-tmp/data/docred --split test --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/plan_002_test_rsft_s43
2559	SPEC.server: rtx5090-4x
2560	SPEC.data_path: /root/autodl-tmp/data/docred
2561	SPEC.model_name: Qwen3-4B + RSFT s43 ckpt-510
2562	SPEC.seed: 42
2563	SPEC.checkpoint_source: /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510
2564	SPEC.eval_data: docred/test.json
2565	SPEC.parent: rsft_ced_s43
2566	
2567	========================================================================================================================
2568	EXP_ID: plan_002_test_rsft_s44
2569	STATUS: DONE
2570	CREATED_AT: 2026-05-17T01:05:59.263Z
2571	UPDATED_AT: 2026-05-17T04:57:25.850Z
2572	CONCLUSION: success
2573	COMMAND: python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_s44/checkpoint-510 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split test --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/plan_002_test_rsft_s44
2574	SPEC.server: rtx5090-4x
2575	SPEC.gpu: ['cuda:0']
2576	SPEC.pid: 396333
2577	SPEC.log_path: ~/runs/faith-evidence-ie/plan_002_test_rsft_s44.log
2578	SPEC.submitted_at: 2026-05-17T01:06:16.686Z
2579	SPEC.submitted_via: submit_training_job
2580	SPEC.backend: tmux
2581	SPEC.account: root
2582	SPEC.data_path: /root/autodl-tmp/data/docred
2583	SPEC.data_count: 0
2584	SPEC.model_name: Qwen3-4B + SFT + RSFT-s44
2585	SPEC.seed: 42
2586	SPEC.checkpoint_source: /root/autodl-tmp/rsft_output_s44/checkpoint-510
2587	SPEC.eval_data: docred_test
2588	SPEC.loading_mode: 3-param (base→SFT→RSFT)
2589	SPEC.checkpoint_path: /root/autodl-tmp/eval_results/plan_002_test_rsft_s44
2590	SPEC.metrics_note: Test set - no local gold labels. 1000 docs, 26925 predictions, 626 truncated, format_ok=99.6%. Needs CodaLab submission for official scores.
2591	SPEC.inference_time_s: 12494
2592	SPEC.wall_clock_seconds: 13869.2
2593	SPEC.gpu_hours: 3.85
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "2728e4ef-9598-49e0-8648-6a2b4db9efbd"
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
  "task_id": "aa0dedafabeeb8ab6",
  "tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "description": "Reading /tmp/4b_experiments_full.txt",
  "usage": {
    "total_tokens": 87563,
    "tool_uses": 17,
    "duration_ms": 88388
  },
  "last_tool_name": "Read",
  "uuid": "89270a0f-9d81-490b-8b60-379b6e051ce4",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0"
}
```

---


### Tool call

_source line 64_

<details open><summary>🔧 Tool call — Read · `toolu_01P6AJYdhJ4ATzLT5iBorL2d`</summary>

```json
{
  "file_path": "/tmp/4b_experiments_full.txt",
  "offset": 2593,
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "8fa504ea-5b0b-469f-ad9b-7d419e5cff40",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FsTcNLCF5uHYM3VyekNb2y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8786,
      "cache_read_input_tokens": 78310,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8786,
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

_source line 65 · 2026-05-18T22:03:51.500Z_

<details><summary>↩ Tool result · `toolu_01P6AJYdhJ4ATzLT5iBorL2d`</summary>

```text
2593	SPEC.gpu_hours: 3.85
2594	
2595	========================================================================================================================
2596	EXP_ID: plan_007_redocred_4b_sft_eval
2597	STATUS: DONE
2598	CREATED_AT: 2026-05-16T12:30:55.473Z
2599	UPDATED_AT: 2026-05-16T12:34:54.050Z
2600	CONCLUSION: failed
2601	COMMAND: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=0 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output_qwen3_4b --data_path /root/autodl-tmp/data/re-docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/plan_007_redocred_4b_sft_eval"
2602	SPEC.server: rtx5090-4x
2603	SPEC.gpu: ['cuda:0']
2604	SPEC.pid: 342069
2605	SPEC.log_path: ~/runs/faith-evidence-ie/plan_007_redocred_4b_sft_eval.log
2606	SPEC.submitted_at: 2026-05-16T12:31:28.959Z
2607	SPEC.submitted_via: submit_training_job
2608	SPEC.backend: tmux
2609	SPEC.account: root
2610	SPEC.wall_clock_seconds: 28.3
2611	SPEC.gpu_hours: 0.01
2612	
2613	========================================================================================================================
2614	EXP_ID: plan_007_redocred_4b_sft_eval_r2
2615	STATUS: DONE
2616	CREATED_AT: 2026-05-16T12:36:01.717Z
2617	UPDATED_AT: 2026-05-17T02:55:43.842Z
2618	CONCLUSION: success
2619	METRICS: {
2620	  "ign_f1": 0.3659,
2621	  "f1": 0.3706,
2622	  "evi_f1": 0.817,
2623	  "edcr": 0.6674,
2624	  "format_compliance_rate": 0.996,
2625	  "n_truncated": 139,
2626	  "n_total": 493,
2627	  "inference_time_seconds": 3281.7,
2628	  "precision": 0.4316,
2629	  "recall": 0.3247,
2630	  "ign_precision": 0.4134,
2631	  "ign_recall": 0.3282,
2632	  "evi_precision": 0.8208,
2633	  "evi_recall": 0.8131,
2634	  "n_predictions": 8191
2635	}
2636	COMMAND: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=0 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/re-docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/plan_007_redocred_4b_sft_eval"
2637	SPEC.server: rtx5090-4x
2638	SPEC.gpu: ['cuda:0']
2639	SPEC.pid: 342711
2640	SPEC.log_path: ~/runs/faith-evidence-ie/plan_007_redocred_4b_sft_eval_r2.log
2641	SPEC.submitted_at: 2026-05-16T12:36:27.149Z
2642	SPEC.submitted_via: submit_training_job
2643	SPEC.backend: tmux
2644	SPEC.account: root
2645	SPEC.wall_clock_seconds: 3698.9
2646	SPEC.gpu_hours: 1.03
2647	
2648	========================================================================================================================
2649	EXP_ID: plan_007_redocred_rsft_eval
2650	STATUS: DONE
2651	CREATED_AT: 2026-05-16T14:23:56.999Z
2652	UPDATED_AT: 2026-05-16T17:49:00.578Z
2653	CONCLUSION: failed
2654	METRICS: {
2655	  "failure_reason": "OOM + pipeline bug: --model_path and --sft_adapter args in wrong order. RSFT LoRA merged to bare Qwen3-4B without SFT base, causing ontology collapse. Fix: match DocRED eval param ordering."
2656	}
2657	COMMAND: CUDA_VISIBLE_DEVICES=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510 --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/re-docred --output_dir /root/autodl-tmp/eval_results/redocred_rsft_eval --batch_size 4 --max_new_tokens 1024 --split dev --seed 42 --no-quantize
2658	SPEC.server: rtx5090-4x
2659	SPEC.data_path: /root/autodl-tmp/data/re-docred
2660	SPEC.data_count: 500
2661	SPEC.model_name: Qwen3-4B + SFT + CED-RSFT(s43)
2662	SPEC.seed: 42
2663	SPEC.checkpoint_source: /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510
2664	SPEC.eval_data: re-docred/dev
2665	SPEC.hypothesis: CED-RSFT gains (rel_f1 improvement over SFT) transfer to Re-DocRED cross-dataset eval
2666	SPEC.parent: plan_007_redocred_4b_sft_eval_r2
2667	SPEC.plan_id: plan_007
2668	SPEC.pid: 352684
2669	SPEC.gpu: cuda:1
2670	SPEC.log_path: /root/runs/faith-evidence-ie/plan_007_redocred_rsft_eval.log
2671	
2672	========================================================================================================================
2673	EXP_ID: plan_007_redocred_rsft_eval_r2
2674	STATUS: DONE
2675	CREATED_AT: 2026-05-16T16:25:37.094Z
2676	UPDATED_AT: 2026-05-17T02:56:32.555Z
2677	CONCLUSION: negative
2678	METRICS: {
2679	  "F1": 0.0025,
2680	  "Ign-F1": 0.0026,
2681	  "Evi-F1": 0.8837,
2682	  "EDCR": 0.9978,
2683	  "format_ok": "489/493",
2684	  "truncated": "117/493",
2685	  "predictions": 8461
2686	}
2687	COMMAND: CUDA_VISIBLE_DEVICES=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510 --data_path /root/autodl-tmp/data/re-docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/plan_007_redocred_rsft_eval_r2
2688	SPEC.server: rtx5090-4x
2689	SPEC.gpu: cuda:1
2690	SPEC.pid: 363317
2691	SPEC.data_path: /root/autodl-tmp/data/re-docred
2692	SPEC.model_name: Qwen3-4B
2693	SPEC.seed: 42
2694	SPEC.checkpoint_source: /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510
2695	SPEC.eval_data: re-docred/dev
2696	SPEC.hypothesis: Re-DocRED RSFT eval r2: verify CED-RSFT improvement transfers cross-dataset. Compare vs SFT baseline Ign-F1=0.3659 (D080).
2697	SPEC.plan_id: plan_007
2698	SPEC.parent: plan_007_redocred_4b_sft_eval_r2
2699	SPEC.log_path: /tmp/plan_007_redocred_rsft_eval_r2.log
2700	
2701	========================================================================================================================
2702	EXP_ID: plan_007_redocred_rsft_eval_r3
2703	STATUS: DONE
2704	CREATED_AT: 2026-05-16T17:38:09.825Z
2705	UPDATED_AT: 2026-05-16T21:07:14.348Z
2706	CONCLUSION: failed
2707	COMMAND: CUDA_VISIBLE_DEVICES=1 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510 --data_path /root/autodl-tmp/data/re-docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/redocred_rsft_eval_r3
2708	SPEC.server: rtx5090-4x
2709	SPEC.data_path: /root/autodl-tmp/data/re-docred
2710	SPEC.model_name: Qwen3-4B (CED-RSFT)
2711	SPEC.seed: 42
2712	SPEC.checkpoint_source: /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510
2713	SPEC.eval_data: re-docred-dev
2714	
2715	========================================================================================================================
2716	EXP_ID: plan_007_redocred_rsft_eval_r4
2717	STATUS: DONE
2718	CREATED_AT: 2026-05-16T18:00:41.999Z
2719	UPDATED_AT: 2026-05-16T22:04:01.953Z
2720	CONCLUSION: failed
2721	COMMAND: CUDA_VISIBLE_DEVICES=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510 --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/re-docred --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/plan_007_redocred_rsft_eval_r4
2722	SPEC.server: rtx5090-4x
2723	SPEC.data_path: /root/autodl-tmp/data/re-docred
2724	SPEC.data_count: -1
2725	SPEC.model_name: Qwen3-4B RSFT ced_s43 checkpoint-510
2726	SPEC.seed: 42
2727	SPEC.checkpoint_source: /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510
2728	SPEC.eval_data: re-docred
2729	SPEC.pid: 370793
2730	
2731	========================================================================================================================
2732	EXP_ID: plan_007_redocred_rsft_eval_r5
2733	STATUS: DONE
2734	CREATED_AT: 2026-05-16T22:04:18.834Z
2735	UPDATED_AT: 2026-05-17T00:51:25.706Z
2736	CONCLUSION: success
2737	METRICS: {
2738	  "f1": 0.4234,
2739	  "ign_f1": 0.4145,
2740	  "evi_f1": 0.8182,
2741	  "edcr": 0.621,
2742	  "evi_joint_f1": 0.3306,
2743	  "format_compliance": 1,
2744	  "field_compliance": 0.8134,
2745	  "n_documents": 493,
2746	  "n_truncated": 90,
2747	  "inference_time_s": 5655.5
2748	}
2749	COMMAND: python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/re-docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/plan_007_redocred_rsft_eval_r4
2750	SPEC.server: rtx5090-4x
2751	SPEC.gpu: cuda:1
2752	SPEC.pid: 384691
2753	SPEC.data_path: /root/autodl-tmp/data/re-docred
2754	SPEC.data_count: -1
2755	SPEC.model_name: Qwen3-4B + SFT + RSFT-CED-s43-ckpt510
2756	SPEC.seed: 42
2757	SPEC.checkpoint_source: /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510
2758	SPEC.eval_data: re-docred dev
2759	SPEC.log_path: ~/runs/faith-evidence-ie/plan_007_redocred_rsft_eval_r4.log
2760	SPEC.checkpoint_path: /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510
2761	
2762	========================================================================================================================
2763	EXP_ID: plan_008_rsft_topk3
2764	STATUS: DONE
2765	CREATED_AT: 2026-05-15T18:01:33.773Z
2766	UPDATED_AT: 2026-05-15T21:11:35.509Z
2767	CONCLUSION: success
2768	METRICS: {
2769	  "train_loss": 0.5543,
2770	  "eval_loss": 0.8297,
2771	  "eval_mean_token_accuracy": 0.8228,
2772	  "eval_entropy": 0.6001,
2773	  "train_runtime_sec": 10916,
2774	  "total_steps": 1509,
2775	  "epochs": 3,
2776	  "trainable_params_pct": 3.18,
2777	  "rsft_samples": 8037,
2778	  "ced_score_mean": 0.621,
2779	  "task_eval_f1_ep1": 0.4848,
2780	  "task_eval_f1_ep2": 0.4824,
2781	  "task_eval_f1_ep3": 0.5012,
2782	  "task_eval_evi_f1_ep1": 0.745,
2783	  "task_eval_evi_f1_ep2": 0.6997,
2784	  "task_eval_evi_f1_ep3": 0.6816,
2785	  "task_eval_edcr_ep1": 0.6525,
2786	  "task_eval_edcr_ep2": 0.6529,
2787	  "task_eval_edcr_ep3": 0.5963,
2788	  "task_eval_note": "50-doc subset, not full dev"
2789	}
2790	COMMAND: python -m freige.train.rsft_train --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/rsft_filtered_topk3/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_topk3_output
2791	SPEC.server: rtx5090-4x
2792	SPEC.gpu: ['cuda:3']
2793	SPEC.pid: 234489
2794	SPEC.log_path: /root/runs/faith-evidence-ie/plan_008_rsft_topk3.log
2795	SPEC.submitted_at: 2026-05-15T18:03:03.593Z
2796	SPEC.submitted_via: submit_training_job
2797	SPEC.backend: tmux
2798	SPEC.account: root
2799	SPEC.data_path: /root/autodl-tmp/rsft_filtered_topk3/rsft_train.jsonl
2800	SPEC.data_count: 8037
2801	SPEC.model_name: Qwen3-4B + SFT adapter + RSFT top_k=3
2802	SPEC.seed: 42
2803	SPEC.checkpoint_path: /root/autodl-tmp/rsft_topk3_output
2804	SPEC.wall_clock_seconds: 11199.8
2805	SPEC.gpu_hours: 3.11
2806	
2807	========================================================================================================================
2808	EXP_ID: plan_009_flatnli_reward_eval
2809	STATUS: DONE
2810	CREATED_AT: 2026-05-15T19:04:57.991Z
2811	UPDATED_AT: 2026-05-15T19:39:02.187Z
2812	CONCLUSION: failed
2813	SPEC.hypothesis: FlatNLI reward GRPO checkpoint eval。用已有 checkpoint 补充 forgetting dynamics 图的 flatNLI reward 变体数据，实现三种 reward 对比。
2814	SPEC.server: rtx5090-4x
2815	SPEC.data_path: /root/autodl-tmp/data/docred
2816	SPEC.data_count: 985
2817	SPEC.model_name: Qwen3-4B + SFT + QLoRA GRPO (flatNLI reward)
2818	SPEC.seed: 42
2819	SPEC.eval_data: docred dev (985 docs)
2820	SPEC.checkpoint_source: grpo_flatnli_r3/r4/r5/r6 checkpoints
2821	
2822	========================================================================================================================
2823	EXP_ID: plan_009_flatnli_reward_eval_r2
2824	STATUS: DONE
2825	CREATED_AT: 2026-05-15T19:54:58.033Z
2826	UPDATED_AT: 2026-05-15T20:32:33.464Z
2827	CONCLUSION: failed
2828	COMMAND: CUDA_VISIBLE_DEVICES=1 python -m freige.eval.batch_eval --exp_dir /root/autodl-tmp/grpo_flatnli_r3 --sft_adapter /root/autodl-tmp/sft_output --output_dir /root/autodl-tmp/eval_results/grpo_flatnli_r3 --no-quantize --max_new_tokens 1024
2829	SPEC.server: rtx5090-4x
2830	SPEC.gpu: ['cuda:1']
2831	SPEC.pid: 246974
2832	SPEC.log_path: ~/runs/faith-evidence-ie/plan_009_flatnli_reward_eval.log
2833	SPEC.submitted_at: 2026-05-16T03:54:00Z
2834	SPEC.submitted_via: ssh_execute+tmux
2835	SPEC.backend: tmux
2836	SPEC.tmux_session: plan_009_flatnli_reward_eval
2837	SPEC.account: root
2838	SPEC.data_path: /root/autodl-tmp/data/docred
2839	SPEC.data_count: 985
2840	SPEC.model_name: Qwen3-4B + SFT + QLoRA GRPO (flatNLI reward)
2841	SPEC.seed: 42
2842	SPEC.checkpoint_source: /root/autodl-tmp/grpo_flatnli_r3 (checkpoints 20,40,60,80,100)
2843	SPEC.eval_data: docred dev (985 docs, 12275 triples)
2844	SPEC.checkpoint_path: /root/autodl-tmp/eval_results/grpo_flatnli_r3
2845	SPEC.parent: plan_009_flatnli_reward_eval
2846	SPEC.notes: Retry. Batch eval 5 flatNLI-reward GRPO checkpoints (step 20-100) for forgetting dynamics figure.
2847	
2848	========================================================================================================================
2849	EXP_ID: plan_011_grpo_g8_bf16
2850	STATUS: DONE
2851	CREATED_AT: 2026-05-15T13:59:50.014Z
2852	UPDATED_AT: 2026-05-15T15:55:53.725Z
2853	CONCLUSION: success
2854	METRICS: {
2855	  "final_step": 100,
2856	  "train_runtime_s": 554,
2857	  "reward_final": 1.795,
2858	  "f1_reward_final": 1.002,
2859	  "ced_reward_final": 0.494,
2860	  "format_reward_final": 0.3,
2861	  "frac_zero_std_final": 0,
2862	  "kl_final": 0.022,
2863	  "best_reward_step": 85,
2864	  "best_reward": 2.858,
2865	  "best_f1_reward": 1.85,
2866	  "mode_collapse": false,
2867	  "lora_config": "r=64, alpha=128, dropout=0.05, bf16",
2868	  "checkpoints": "10 checkpoints (step 10-100)"
2869	}
2870	COMMAND: bash -c "cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=3 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 /root/miniconda3/bin/python -m freige.training.grpo_trainer --model_name /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_dir /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/grpo_ced_g8_bf16 --stage 3 --num_generations 8 --kl_coef 0.01 --learning_rate 5e-5 --max_steps 100 --save_steps 10 --save_total_limit 10 --per_device_batch_size 1 --gradient_accumulation_steps 1 --format_reward_weight 0.3 --f1_reward_weight 3.0 --ced_reward_weight 1.0 --num_iterations 1 --no-quantize --wandb_run_name plan_011_grpo_g8_bf16"
2871	SPEC.server: rtx5090-4x
2872	SPEC.gpu: ['cuda:3']
2873	SPEC.pid: 210099
2874	SPEC.log_path: ~/runs/faith-evidence-ie/plan_011_grpo_g8_bf16.log
2875	SPEC.submitted_at: 2026-05-15T14:00:10.122Z
2876	SPEC.submitted_via: submit_training_job
2877	SPEC.backend: tmux
2878	SPEC.account: root
2879	SPEC.wall_clock_seconds: 6943.6
2880	SPEC.gpu_hours: 1.93
2881	
2882	========================================================================================================================
2883	EXP_ID: plan_011_grpo_g8_bf16_eval
2884	STATUS: DONE
2885	CREATED_AT: 2026-05-15T14:43:48.481Z
2886	UPDATED_AT: 2026-05-15T15:55:52.592Z
2887	CONCLUSION: success
2888	METRICS: {
2889	  "rel_f1": 0.4549,
2890	  "ign_f1": 0.4549,
2891	  "evi_f1": 0.8086,
2892	  "edcr": 0.6318,
2893	  "format_ok_rate": 1,
2894	  "n_truncated": 61,
2895	  "n_total": 985,
2896	  "n_predictions": 10701,
2897	  "checkpoint": "checkpoint-100",
2898	  "model": "Qwen3-4B + SFT merged + GRPO bf16 LoRA ckpt-100",
2899	  "inference_time_s": 3170.3
2900	}
2901	COMMAND: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python -m freige.eval.inference --model_path /root/autodl-tmp/grpo_ced_g8_bf16/checkpoint-100 --sft_adapter /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/grpo_g8_bf16_ckpt100 --no-quantize"
2902	SPEC.server: rtx5090-4x
2903	SPEC.gpu: ['cuda:0']
2904	SPEC.pid: 216356
2905	SPEC.log_path: ~/runs/faith-evidence-ie/plan_011_grpo_g8_bf16_eval.log
2906	SPEC.submitted_at: 2026-05-15T14:47:35.396Z
2907	SPEC.submitted_via: submit_training_job
2908	SPEC.backend: tmux
2909	SPEC.account: root
2910	SPEC.wall_clock_seconds: 4097.2
2911	SPEC.gpu_hours: 1.14
2912	
2913	========================================================================================================================
2914	EXP_ID: plan_012_dpo_ced
2915	STATUS: DONE
2916	CREATED_AT: 2026-05-15T15:54:03.324Z
2917	UPDATED_AT: 2026-05-15T21:37:44.232Z
2918	CONCLUSION: negative
2919	METRICS: {
2920	  "rel_f1": 0.3429,
2921	  "evi_f1": 0.8403,
2922	  "edcr": 0.7294,
2923	  "format_ok_rate": 0.995,
2924	  "checkpoint": "checkpoint-501",
2925	  "rewards_accuracy": 1,
2926	  "margins": 9.01
2927	}
2928	SPEC.checkpoint_path: /root/autodl-tmp/dpo_output
2929	SPEC.data_path: /root/autodl-tmp/dpo_data/dpo_pairs.jsonl
2930	SPEC.data_count: 2666
2931	SPEC.model_name: Qwen3-4B + SFT + CED-DPO
2932	SPEC.seed: 42
2933	SPEC.beta: 0.1
2934	SPEC.num_epochs: 3
2935	SPEC.loss_type: sigmoid
2936	SPEC.base_model: /root/autodl-tmp/models/Qwen3-4B
2937	SPEC.sft_adapter: /root/autodl-tmp/sft_output
2938	SPEC.pairs: 2666
2939	
2940	========================================================================================================================
2941	EXP_ID: plan_012_dpo_ced_1ep
2942	STATUS: DONE
2943	CREATED_AT: 2026-05-15T18:50:44.852Z
2944	UPDATED_AT: 2026-05-15T21:36:34.720Z
2945	CONCLUSION: negative
2946	METRICS: {
2947	  "rel_f1": 0.0022,
2948	  "evi_f1": 0.75,
2949	  "edcr": 0.9982,
2950	  "format_ok": "981/985",
2951	  "truncated": "358/985",
2952	  "tp": 34,
2953	  "n_preds": 19265,
2954	  "inference_time_s": 3643,
2955	  "train_loss_final": 0.59,
2956	  "rewards_accuracy": 0.82,
2957	  "rewards_margins": 0.86,
2958	  "total_steps": 167,
2959	  "training_time_min": 33
2960	}
2961	COMMAND: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 WANDB_PROJECT=freige-dpo PYTHONUNBUFFERED=1 python -m freige.training.dpo_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --dpo_data_path /root/autodl-tmp/dpo_data/dpo_pairs.jsonl --output_dir /root/autodl-tmp/dpo_output_1ep --beta 0.1 --num_epochs 1 --seed 42 --loss_type sigmoid --per_device_batch_size 1 --gradient_accumulation_steps 16 --wandb_run_name plan_012_dpo_ced_1ep"
2962	SPEC.hypothesis: DPO+CED 1-epoch 重训：修复 3-epoch 过拟合问题。epochs=1 (~167 steps, <10min)，其余超参不变（β=0.1, lr=5e-7, loss=sigmoid, seed=42, pairs=2666）。让 DPO 数据点可用于论文。
2963	SPEC.parent: plan_012_dpo_ced
2964	SPEC.server: rtx5090-4x
2965	SPEC.gpu: ['cuda:2']
2966	SPEC.pid: 245103
2967	SPEC.log_path: ~/runs/faith-evidence-ie/plan_012_dpo_ced_1ep.log
2968	SPEC.submitted_at: 2026-05-15T19:43:02.707Z
2969	SPEC.submitted_via: submit_training_job
2970	SPEC.backend: tmux
2971	SPEC.account: root
2972	SPEC.data_path: /root/autodl-tmp/dpo_data/dpo_pairs.jsonl
2973	SPEC.data_count: 2666
2974	SPEC.model_name: Qwen3-4B + SFT + CED-DPO (1ep)
2975	SPEC.seed: 42
2976	SPEC.base_model: /root/autodl-tmp/models/Qwen3-4B
2977	SPEC.sft_adapter: /root/autodl-tmp/sft_output
2978	SPEC.beta: 0.1
2979	SPEC.num_epochs: 1
2980	SPEC.loss_type: sigmoid
2981	SPEC.checkpoint_path: /root/autodl-tmp/dpo_output_1ep
2982	SPEC.wall_clock_seconds: 6812.0
2983	SPEC.gpu_hours: 1.89
2984	
2985	========================================================================================================================
2986	EXP_ID: plan_014_no_evidence_eval_d076
2987	STATUS: DONE
2988	CREATED_AT: 2026-05-16T14:26:29.748Z
2989	UPDATED_AT: 2026-05-16T17:37:09.823Z
2990	CONCLUSION: success
2991	METRICS: {
2992	  "ign_f1": 0.4721,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "a4f91953-c362-4023-addd-00c296e45ec4"
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
  "task_id": "aa0dedafabeeb8ab6",
  "tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "description": "Reading /tmp/4b_experiments_full.txt",
  "usage": {
    "total_tokens": 96671,
    "tool_uses": 18,
    "duration_ms": 91689
  },
  "last_tool_name": "Read",
  "uuid": "acd63153-8905-4c8f-9157-796eab3fb1d4",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0"
}
```

---


### Tool call

_source line 67_

<details open><summary>🔧 Tool call — Read · `toolu_01PaTFZ6idnDRSUiHBbWCxd9`</summary>

```json
{
  "file_path": "/tmp/4b_experiments_full.txt",
  "offset": 2992,
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "1bffd532-9613-4200-b74c-64d6b7840276",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H9sZYLHva7sFrpW5Pay87A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9070,
      "cache_read_input_tokens": 87096,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9070,
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

_source line 68 · 2026-05-18T22:03:54.803Z_

<details><summary>↩ Tool result · `toolu_01PaTFZ6idnDRSUiHBbWCxd9`</summary>

```text
2992	  "ign_f1": 0.4721,
2993	  "f1": 0.4876,
2994	  "precision": 0.4901,
2995	  "recall": 0.4851,
2996	  "format_compliance_rate": 0.9929,
2997	  "n_truncated": 307,
2998	  "inference_time_seconds": 6903.9
2999	}
3000	COMMAND: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=1 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_no_evidence_output/ --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --no_evidence --output_dir /root/autodl-tmp/eval_results/plan_014_no_evidence_eval_d076"
3001	SPEC.server: rtx5090-4x
3002	SPEC.data_path: /root/autodl-tmp/data/docred
3003	SPEC.data_count: 985
3004	SPEC.model_name: Qwen3-4B (no-evidence SFT)
3005	SPEC.seed: 42
3006	SPEC.checkpoint_source: /root/autodl-tmp/sft_no_evidence_output/
3007	SPEC.eval_data: docred-dev
3008	
3009	========================================================================================================================
3010	EXP_ID: plan_014_sft_no_evidence
3011	STATUS: DONE
3012	CREATED_AT: 2026-05-15T15:55:43.710Z
3013	UPDATED_AT: 2026-05-15T18:42:28.216Z
3014	CONCLUSION: success
3015	METRICS: {
3016	  "train_loss": 0.7077,
3017	  "eval_loss": 0.8781,
3018	  "eval_token_accuracy": 0.8086,
3019	  "epochs": 3,
3020	  "total_steps": 570,
3021	  "train_runtime_min": 64,
3022	  "samples": 3027,
3023	  "trainable_params": "132M/4.15B (3.18%)"
3024	}
3025	COMMAND: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.training.sft_trainer --data_dir /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/sft_no_evidence_output --no_evidence --wandb_run_name plan_014_sft_no_evidence --seed 42"
3026	SPEC.server: rtx5090-4x
3027	SPEC.gpu: ['cuda:1']
3028	SPEC.pid: 222207
3029	SPEC.log_path: ~/runs/faith-evidence-ie/plan_014_sft_no_evidence.log
3030	SPEC.submitted_at: 2026-05-15T15:56:13Z
3031	SPEC.submitted_via: submit_training_job
3032	SPEC.backend: tmux
3033	SPEC.account: root
3034	SPEC.model_name: Qwen3-4B (QLoRA 4-bit)
3035	SPEC.data_path: /root/autodl-tmp/data/docred
3036	SPEC.data_count: 3027
3037	SPEC.seed: 42
3038	SPEC.checkpoint_path: /root/autodl-tmp/sft_no_evidence_output
3039	SPEC.wall_clock_seconds: 9975.2
3040	SPEC.gpu_hours: 2.77
3041	
3042	========================================================================================================================
3043	EXP_ID: plan_015_grpo_g4_bf16
3044	STATUS: DONE
3045	CREATED_AT: 2026-05-15T15:58:43.784Z
3046	UPDATED_AT: 2026-05-15T16:03:08.279Z
3047	CONCLUSION: killed
3048	COMMAND: python -m freige.training.grpo_trainer --model_name Qwen3-4B --sft_adapter sft_output --data_dir data/docred --output_dir grpo_ced_g4_bf16 --stage 3 --num_generations 4 --kl_coef 0 --learning_rate 5e-5 --max_steps 100 --no-quantize --wandb_run_name plan_015_grpo_g4_bf16
3049	SPEC.server: rtx5090-4x
3050	SPEC.gpu: ['cuda:0']
3051	SPEC.pid: 222937
3052	SPEC.log_path: ~/runs/faith-evidence-ie/plan_015_grpo_g4_bf16.log
3053	SPEC.submitted_at: 2026-05-15T15:58:43.532Z
3054	SPEC.submitted_via: submit_training_job
3055	SPEC.backend: tmux
3056	SPEC.account: root
3057	SPEC.data_path: /root/autodl-tmp/data/docred
3058	SPEC.data_count: 3027
3059	SPEC.model_name: Qwen3-4B
3060	SPEC.seed: 42
3061	SPEC.wall_clock_seconds: 264.7
3062	SPEC.gpu_hours: 0.07
3063	
3064	========================================================================================================================
3065	EXP_ID: plan_015_grpo_g4_bf16_v2
3066	STATUS: DONE
3067	CREATED_AT: 2026-05-15T16:06:43.308Z
3068	UPDATED_AT: 2026-05-15T16:54:42.310Z
3069	CONCLUSION: killed
3070	COMMAND: python -m freige.training.grpo_trainer --model_name Qwen3-4B --sft_adapter sft_output --data_dir data/docred --output_dir grpo_g4_bf16_control --stage 3 --num_generations 4 --kl_coef 0 --learning_rate 5e-6 --max_steps 100 --no-quantize --wandb_run_name plan_015_grpo_g4_bf16_v2
3071	SPEC.server: rtx5090-4x
3072	SPEC.gpu: ['cuda:3']
3073	SPEC.pid: 222942
3074	SPEC.data_path: /root/autodl-tmp/data/docred
3075	SPEC.data_count: 3027
3076	SPEC.model_name: Qwen3-4B + SFT adapter
3077	SPEC.seed: 42
3078	SPEC.notes: kl_coef=0 配置错误最终确认 kill。Director 指令以 plan_015_v3 (kl=0.01) 替代。
3079	SPEC.checkpoint_source: /root/autodl-tmp/sft_output
3080	SPEC.eval_data: N/A (training)
3081	SPEC.checkpoint_path: /root/autodl-tmp/grpo_g4_bf16_control
3082	SPEC.log_path: ~/runs/faith-evidence-ie/plan_015_grpo_g4_bf16_v2.log
3083	
3084	========================================================================================================================
3085	EXP_ID: plan_015_grpo_g4_bf16_v3
3086	STATUS: DONE
3087	CREATED_AT: 2026-05-15T16:27:09.496Z
3088	UPDATED_AT: 2026-05-15T16:54:54.376Z
3089	CONCLUSION: killed
3090	COMMAND: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.training.grpo_trainer --model_name /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_dir /root/autodl-tmp/data/docred --stage 3 --tau_start 0.3 --tau_end 0.5 --output_dir /root/autodl-tmp/grpo_g4_bf16_kl001 --num_generations 4 --reward_device cuda --per_device_batch_size 1 --gradient_accumulation_steps 16 --num_epochs 1 --learning_rate 5e-6 --seed 42 --kl_coef 0.01 --save_steps 20 --save_total_limit 20 --max_steps 200 --format_reward_weight 0.3 --f1_reward_weight 3.0 --ced_reward_weight 1.0 --num_iterations 1 --no-quantize --wandb_run_name plan_015_grpo_g4_bf16_v3"
3091	SPEC.server: rtx5090-4x
3092	SPEC.gpu: ['cuda:0']
3093	SPEC.pid: 226476
3094	SPEC.log_path: ~/runs/faith-evidence-ie/plan_015_grpo_g4_bf16_v3.log
3095	SPEC.submitted_at: 2026-05-15T16:32:42.980Z
3096	SPEC.submitted_via: submit_training_job
3097	SPEC.backend: tmux
3098	SPEC.account: root
3099	SPEC.data_path: /root/autodl-tmp/data/docred
3100	SPEC.data_count: 3027
3101	SPEC.model_name: Qwen3-4B + SFT adapter
3102	SPEC.seed: 42
3103	SPEC.checkpoint_source: /root/autodl-tmp/sft_output
3104	SPEC.eval_data: N/A (training)
3105	SPEC.checkpoint_path: /root/autodl-tmp/grpo_g4_bf16_kl001
3106	SPEC.notes: D052: plan_011 vs mvp2_grpo_ced_kl001_r4 已是 clean ablation。v3 取消，cuda:0 腾给 plan_001 eval。
3107	SPEC.wall_clock_seconds: 1331.4
3108	SPEC.gpu_hours: 0.37
3109	
3110	========================================================================================================================
3111	EXP_ID: random_rsft_k1_eval
3112	STATUS: DONE
3113	CREATED_AT: 2026-05-18T16:34:48.815Z
3114	UPDATED_AT: 2026-05-18T20:08:52.336Z
3115	CONCLUSION: success
3116	METRICS: {
3117	  "ign_f1": 0.4114,
3118	  "f1": 0.4198,
3119	  "evi_f1": 0.7964,
3120	  "evi_f1_joint": 0.3216,
3121	  "EDCR": 0.6971,
3122	  "format_compliance": 0.999,
3123	  "field_compliance": 0.7482,
3124	  "truncated": 235,
3125	  "n_total": 985,
3126	  "n_predictions": 16110,
3127	  "inference_time_seconds": 11778.5
3128	}
3129	COMMAND: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_random_k1/checkpoint-1020 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output/ --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/random_rsft_k1_eval"
3130	SPEC.server: rtx5090-4x
3131	SPEC.gpu: ['cuda:1']
3132	SPEC.pid: 558320
3133	SPEC.log_path: ~/runs/faith-evidence-ie/random_rsft_k1_eval.log
3134	SPEC.submitted_at: 2026-05-18T16:35:12.562Z
3135	SPEC.submitted_via: submit_training_job
3136	SPEC.backend: tmux
3137	SPEC.account: root
3138	SPEC.data_path: /root/autodl-tmp/data/docred
3139	SPEC.data_count: 985
3140	SPEC.model_name: Qwen3-4B + SFT + Random-RSFT-k1
3141	SPEC.seed: 42
3142	SPEC.checkpoint_source: random_rsft_k1_baseline
3143	SPEC.eval_data: DocRED dev
3144	SPEC.checkpoint_path: /root/autodl-tmp/eval_results/random_rsft_k1_eval
3145	SPEC.wall_clock_seconds: 12819.8
3146	SPEC.gpu_hours: 3.56
3147	
3148	========================================================================================================================
3149	EXP_ID: reeval_ced_s42
3150	STATUS: DONE
3151	CREATED_AT: 2026-05-16T02:37:58.498Z
3152	UPDATED_AT: 2026-05-16T10:14:00.520Z
3153	CONCLUSION: success
3154	METRICS: {
3155	  "ign_f1": 0.4423,
3156	  "rel_f1": 0.4517,
3157	  "evi_f1": 0.8175,
3158	  "evi_f1_joint": 0.3518,
3159	  "edcr": 0.6569,
3160	  "format_compliance_rate": 1,
3161	  "field_compliance_rate": 0.7756,
3162	  "n_truncated": 214,
3163	  "inference_time_seconds": 10815.5
3164	}
3165	COMMAND: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=2 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output/checkpoint-510 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/rsft_ced_s42_reeval --no-quantize"
3166	SPEC.server: rtx5090-4x
3167	SPEC.gpu: ['cuda:2']
3168	SPEC.pid: 298018
3169	SPEC.log_path: /root/autodl-tmp/eval_results/rsft_ced_s42_reeval/metrics.json
3170	SPEC.submitted_at: 2026-05-16T04:24:05.849Z
3171	SPEC.submitted_via: submit_training_job
3172	SPEC.backend: tmux
3173	SPEC.account: root
3174	SPEC.checkpoint_path: /root/autodl-tmp/eval_results/rsft_ced_s42_reeval
3175	SPEC.wall_clock_seconds: 20994.7
3176	SPEC.gpu_hours: 5.83
3177	
3178	========================================================================================================================
3179	EXP_ID: reeval_ced_s44
3180	STATUS: DONE
3181	CREATED_AT: 2026-05-16T02:38:00.052Z
3182	UPDATED_AT: 2026-05-16T10:14:02.479Z
3183	CONCLUSION: success
3184	METRICS: {
3185	  "ign_f1": 0.4511,
3186	  "rel_f1": 0.4621,
3187	  "evi_f1": 0.805,
3188	  "evi_f1_joint": 0.3677,
3189	  "edcr": 0.635,
3190	  "format_compliance_rate": 1,
3191	  "field_compliance_rate": 0.802,
3192	  "n_truncated": 190,
3193	  "inference_time_seconds": 13077.6
3194	}
3195	COMMAND: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_s44/checkpoint-510 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 44 --output_dir /root/autodl-tmp/eval_results/rsft_ced_s44_reeval --no-quantize"
3196	SPEC.server: rtx5090-4x
3197	SPEC.gpu: ['cuda:0']
3198	SPEC.pid: 297190
3199	SPEC.log_path: /root/autodl-tmp/eval_results/rsft_ced_s44_reeval/metrics.json
3200	SPEC.submitted_at: 2026-05-16T04:18:28.117Z
3201	SPEC.submitted_via: submit_training_job
3202	SPEC.backend: tmux
3203	SPEC.account: root
3204	SPEC.checkpoint_path: /root/autodl-tmp/eval_results/rsft_ced_s44_reeval
3205	SPEC.wall_clock_seconds: 21334.4
3206	SPEC.gpu_hours: 5.93
3207	
3208	========================================================================================================================
3209	EXP_ID: reeval_flat_nli_s42
3210	STATUS: DONE
3211	CREATED_AT: 2026-05-16T02:38:03.120Z
3212	UPDATED_AT: 2026-05-16T10:14:04.270Z
3213	CONCLUSION: success
3214	METRICS: {
3215	  "ign_f1": 0.4448,
3216	  "rel_f1": 0.4535,
3217	  "evi_f1": 0.8039,
3218	  "evi_f1_joint": 0.3558,
3219	  "edcr": 0.6458,
3220	  "format_compliance_rate": 1,
3221	  "field_compliance_rate": 0.7787,
3222	  "n_truncated": 205,
3223	  "inference_time_seconds": 13253.1
3224	}
3225	COMMAND: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_flat_nli/checkpoint-507 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/rsft_flat_nli_s42_reeval --no-quantize"
3226	SPEC.server: rtx5090-4x
3227	SPEC.gpu: ['cuda:0']
3228	SPEC.pid: 296732
3229	SPEC.log_path: /root/autodl-tmp/eval_results/rsft_flat_nli_s42_reeval/metrics.json
3230	SPEC.submitted_at: 2026-05-16T04:16:19.584Z
3231	SPEC.submitted_via: submit_training_job
3232	SPEC.backend: tmux
3233	SPEC.account: root
3234	SPEC.data_path: /root/autodl-tmp/data/docred
3235	SPEC.data_count: 985
3236	SPEC.model_name: Qwen3-4B + SFT + flat-NLI RSFT s42
3237	SPEC.seed: 42
3238	SPEC.checkpoint_source: /root/autodl-tmp/rsft_output_flat_nli/checkpoint-507
3239	SPEC.eval_data: docred dev (985 docs)
3240	SPEC.checkpoint_path: /root/autodl-tmp/eval_results/rsft_flat_nli_s42_reeval
3241	SPEC.wall_clock_seconds: 21464.7
3242	SPEC.gpu_hours: 5.96
3243	
3244	========================================================================================================================
3245	EXP_ID: reeval_flat_nli_s43
3246	STATUS: DONE
3247	CREATED_AT: 2026-05-15T22:00:33.691Z
3248	UPDATED_AT: 2026-05-15T23:59:33.440Z
3249	CONCLUSION: success
3250	METRICS: {
3251	  "rel_f1": 0.4523,
3252	  "ign_f1": 0.4523,
3253	  "evi_f1": 0.8158,
3254	  "edcr": 0.6505,
3255	  "num_preds": 15357,
3256	  "format_ok": "984/985",
3257	  "truncated": "211/985",
3258	  "inference_time_s": 3515.8
3259	}
3260	COMMAND: Re-eval flat-NLI RSFT seed=43 with --sft_adapter (D064 fix)
3261	SPEC.server: rtx5090-4x
3262	SPEC.gpu: cuda:1
3263	SPEC.pid: 266178
3264	SPEC.log_path: /root/runs/faith-evidence-ie/reeval_flat_nli_s43.log
3265	SPEC.submitted_at: 2026-05-15T22:57:10.223Z
3266	SPEC.submitted_via: submit_training_job
3267	SPEC.backend: tmux
3268	SPEC.account: root
3269	SPEC.data_path: /root/autodl-tmp/data/docred
3270	SPEC.data_count: 0
3271	SPEC.model_name: Qwen3-4B + SFT + flat-NLI RSFT s43
3272	SPEC.seed: 43
3273	SPEC.checkpoint_source: plan_001_flat_nli_s43
3274	SPEC.eval_data: docred_dev
3275	SPEC.checkpoint_path: /root/autodl-tmp/rsft_output_flat_nli_s43/checkpoint-507
3276	SPEC.eval_output_dir: /root/autodl-tmp/eval_results/rsft_flat_nli_s43_reeval
3277	SPEC.sft_adapter: /root/autodl-tmp/sft_output
3278	SPEC.base_model: /root/autodl-tmp/models/Qwen3-4B
3279	SPEC.wall_clock_seconds: 3743.2
3280	SPEC.gpu_hours: 1.04
3281	
3282	========================================================================================================================
3283	EXP_ID: reeval_flat_nli_s43_r2
3284	STATUS: DONE
3285	CREATED_AT: 2026-05-16T02:32:45.507Z
3286	UPDATED_AT: 2026-05-16T06:10:14.112Z
3287	CONCLUSION: success
3288	METRICS: {
3289	  "rel_f1": 0.4586,
3290	  "rel_precision": 0.4732,
3291	  "rel_recall": 0.4449,
3292	  "ign_f1": 0.4503,
3293	  "evi_f1": 0.8113,
3294	  "evi_precision": 0.8035,
3295	  "evi_recall": 0.8192,
3296	  "evi_f1_joint": 0.358,
3297	  "edcr": 0.6552,
3298	  "format_ok_rate": 0.999,
3299	  "n_truncated": 184,
3300	  "n_predictions": 15015
3301	}
3302	COMMAND: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=3 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_flat_nli_s43/checkpoint-507 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 43 --output_dir /root/autodl-tmp/eval_results/rsft_flat_nli_s43_reeval_r2 --no-quantize"
3303	SPEC.server: rtx5090-4x
3304	SPEC.gpu: ['cuda:3']
3305	SPEC.pid: 291003
3306	SPEC.log_path: ~/runs/faith-evidence-ie/reeval_flat_nli_s43_r2.log
3307	SPEC.submitted_at: 2026-05-16T03:05:10.815Z
3308	SPEC.submitted_via: submit_training_job
3309	SPEC.backend: tmux
3310	SPEC.account: root
3311	SPEC.wall_clock_seconds: 11103.3
3312	SPEC.gpu_hours: 3.08
3313	
3314	========================================================================================================================
3315	EXP_ID: reeval_flat_nli_s44
3316	STATUS: DONE
3317	CREATED_AT: 2026-05-16T08:56:36.565Z
3318	UPDATED_AT: 2026-05-16T09:26:04.920Z
3319	CONCLUSION: killed
3320	COMMAND: CUDA_VISIBLE_DEVICES=0 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_flat_nli_s44/checkpoint-507 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 44 --output_dir /root/autodl-tmp/eval_results/rsft_flat_nli_s44_reeval --no-quantize
3321	SPEC.server: rtx5090-4x
3322	SPEC.gpu_id: 0
3323	SPEC.pid: 322215
3324	SPEC.data_path: /root/autodl-tmp/data/docred
3325	SPEC.model_name: Qwen3-4B + sft_adapter + rsft_flat_nli_s44/checkpoint-507
3326	SPEC.seed: 44
3327	SPEC.checkpoint_source: /root/autodl-tmp/rsft_output_flat_nli_s44/checkpoint-507
3328	SPEC.eval_data: docred dev
3329	SPEC.log_path: /root/autodl-tmp/logs/reeval_flat_nli_s44.log
3330	SPEC.parent: plan_001_flat_nli_seed44
3331	SPEC.hypothesis: Re-eval flat-NLI RSFT s44 with D076 unified protocol. 之前 eval_flat_nli_seed44 被 killed。Paired t-test 最后一块拼图。
3332	
3333	========================================================================================================================
3334	EXP_ID: reeval_rsft_topk3
3335	STATUS: DONE
3336	CREATED_AT: 2026-05-15T22:00:34.722Z
3337	UPDATED_AT: 2026-05-16T00:24:22.091Z
3338	CONCLUSION: negative
3339	METRICS: {
3340	  "rel_f1": 0.4454,
3341	  "rel_precision": 0.4512,
3342	  "rel_recall": 0.4398,
3343	  "ign_f1": 0.4364,
3344	  "evi_f1": 0.8088,
3345	  "edcr": 0.6635,
3346	  "format_ok_rate": 0.999,
3347	  "n_truncated": 214,
3348	  "n_predictions": 16020,
3349	  "inference_time_seconds": 3546.4,
3350	  "ign_f1_corrected": true
3351	}
3352	COMMAND: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_topk3_output/checkpoint-1509 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/rsft_topk3_reeval --no-quantize"
3353	SPEC.server: rtx5090-4x
3354	SPEC.gpu: ['cuda:2']
3355	SPEC.pid: 268485
3356	SPEC.log_path: ~/runs/faith-evidence-ie/reeval_rsft_topk3.log
3357	SPEC.submitted_at: 2026-05-15T23:10:49.243Z
3358	SPEC.submitted_via: submit_training_job
3359	SPEC.backend: tmux
3360	SPEC.account: root
3361	SPEC.data_path: /root/autodl-tmp/data/docred
3362	SPEC.data_count: 985
3363	SPEC.model_name: RSFT top_k=3 + SFT adapter
3364	SPEC.seed: 42
3365	SPEC.checkpoint_source: rsft_topk3_output/checkpoint-1509
3366	SPEC.eval_data: docred dev
3367	SPEC.wall_clock_seconds: 3798.3
3368	SPEC.gpu_hours: 1.06
3369	
3370	========================================================================================================================
3371	EXP_ID: reeval_sft_baseline_d076
3372	STATUS: DONE
3373	CREATED_AT: 2026-05-16T05:26:37.542Z
3374	UPDATED_AT: 2026-05-17T02:56:09.813Z
3375	CONCLUSION: success
3376	METRICS: {
3377	  "rel_f1": 0.4049,
3378	  "ign_f1": 0.3974,
3379	  "evi_f1": 0.7986,
3380	  "edcr": 0.6982,
3381	  "evi_f1_joint": 0.3147,
3382	  "format_compliance_rate": 0.998,
3383	  "n_truncated": 288,
3384	  "n_documents": 985,
3385	  "n_predictions": 16880,
3386	  "inference_time_sec": 7056.5
3387	}
3388	COMMAND: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/sft_baseline_d076_reeval --no-quantize"
3389	SPEC.server: rtx5090-4x
3390	SPEC.gpu: ['cuda:1']
3391	SPEC.pid: 303065
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "08ab8230-402d-4256-831f-988bbe28dbac"
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
  "task_id": "aa0dedafabeeb8ab6",
  "tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "description": "Reading /tmp/4b_experiments_full.txt",
  "usage": {
    "total_tokens": 106155,
    "tool_uses": 19,
    "duration_ms": 95029
  },
  "last_tool_name": "Read",
  "uuid": "82cec714-c4b0-4019-97e6-644c2b78db49",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0"
}
```

---


### Tool call

_source line 70_

<details open><summary>🔧 Tool call — Read · `toolu_01EgjP3d8K2MhbXHP8gSSuhX`</summary>

```json
{
  "file_path": "/tmp/4b_experiments_full.txt",
  "offset": 3391,
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "b6c0575c-0200-4f9d-921f-67a5bd7ce8a5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DUPe4LX5sxhSXsdmqqevs6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9446,
      "cache_read_input_tokens": 96166,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9446,
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

_source line 71 · 2026-05-18T22:03:58.161Z_

<details><summary>↩ Tool result · `toolu_01EgjP3d8K2MhbXHP8gSSuhX`</summary>

```text
3391	SPEC.pid: 303065
3392	SPEC.log_path: ~/runs/faith-evidence-ie/reeval_sft_baseline_d076.log
3393	SPEC.submitted_at: 2026-05-16T05:26:46.170Z
3394	SPEC.submitted_via: submit_training_job
3395	SPEC.backend: tmux
3396	SPEC.account: root
3397	SPEC.data_path: /root/autodl-tmp/data/docred
3398	SPEC.data_count: 985
3399	SPEC.model_name: Qwen3-4B + SFT baseline (no RSFT)
3400	SPEC.seed: 42
3401	SPEC.checkpoint_source: /root/autodl-tmp/sft_output
3402	SPEC.eval_data: docred dev (985 docs)
3403	SPEC.checkpoint_path: /root/autodl-tmp/sft_output
3404	SPEC.output_dir: /root/autodl-tmp/eval_results/sft_baseline_d076_reeval
3405	SPEC.wall_clock_seconds: 11187.5
3406	SPEC.gpu_hours: 3.11
3407	
3408	========================================================================================================================
3409	EXP_ID: rsft_ced_s43_train
3410	STATUS: DONE
3411	CREATED_AT: 2026-05-16T00:05:46.635Z
3412	UPDATED_AT: 2026-05-16T00:10:42.131Z
3413	CONCLUSION: failed
3414	COMMAND: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.training.rsft_trainer --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output_ced_s43 --seed 43 --weighted_sampling --eval_data_dir /root/autodl-tmp/data/docred --wandb_run_name rsft_ced_s43 --bf16"
3415	SPEC.server: rtx5090-4x
3416	SPEC.gpu: ['cuda:1']
3417	SPEC.pid: unknown
3418	SPEC.log_path: ~/runs/faith-evidence-ie/rsft_ced_s43_train.log
3419	SPEC.submitted_at: 2026-05-16T00:06:16.826Z
3420	SPEC.submitted_via: submit_training_job
3421	SPEC.backend: tmux
3422	SPEC.account: root
3423	SPEC.wall_clock_seconds: 34.8
3424	SPEC.gpu_hours: 0.01
3425	
3426	========================================================================================================================
3427	EXP_ID: rsft_ced_s43_train_r2
3428	STATUS: DONE
3429	CREATED_AT: 2026-05-16T00:09:34.266Z
3430	UPDATED_AT: 2026-05-16T00:25:38.818Z
3431	CONCLUSION: failed
3432	COMMAND: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output_ced_s43 --lr 2e-5 --epochs 3 --batch 1 --grad_accum 16 --lora_rank 64 --lora_alpha 128 --seed 43 --weighted_sampling"
3433	SPEC.data_path: /root/autodl-tmp/rsft_filtered/rsft_train.jsonl
3434	SPEC.data_count: 2718
3435	SPEC.model_name: Qwen3-4B + LoRA on SFT adapter
3436	SPEC.seed: 43
3437	SPEC.server: rtx5090-4x
3438	SPEC.gpu: ['cuda:1']
3439	SPEC.account: root
3440	SPEC.pid: 275269
3441	SPEC.checkpoint_source: /root/autodl-tmp/sft_output
3442	SPEC.eval_data: N/A (training, not eval)
3443	SPEC.log_path: ~/runs/faith-evidence-ie/rsft_ced_s43_train_r2.log
3444	SPEC.output_dir: /root/autodl-tmp/rsft_output_ced_s43
3445	SPEC.hyperparams: {'lr': '2e-5', 'epochs': 3, 'batch': 1, 'grad_accum': 16, 'lora_rank': 64, 'lora_alpha': 128, 'bf16': True, 'weighted_sampling': True}
3446	
3447	========================================================================================================================
3448	EXP_ID: rsft_ced_s43_train_r3
3449	STATUS: DONE
3450	CREATED_AT: 2026-05-16T00:20:57.272Z
3451	UPDATED_AT: 2026-05-16T02:14:46.064Z
3452	CONCLUSION: success
3453	METRICS: {
3454	  "train_loss": 0.6151,
3455	  "eval_loss": 0.7618,
3456	  "task_eval_f1": 0.5026,
3457	  "task_eval_ign_f1": 0.4932,
3458	  "task_eval_evi_f1": 0.7624,
3459	  "task_eval_edcr": 0.6516,
3460	  "total_steps": 510,
3461	  "epochs": 3,
3462	  "training_hours": 1.82
3463	}
3464	SPEC.checkpoint_path: /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510
3465	SPEC.log_path: ~/runs/faith-evidence-ie/rsft_ced_s43_train_r3.log
3466	
3467	========================================================================================================================
3468	EXP_ID: rsft_ced_s45_train
3469	STATUS: DONE
3470	CREATED_AT: 2026-05-16T00:03:17.851Z
3471	UPDATED_AT: 2026-05-16T00:05:24.862Z
3472	CONCLUSION: killed
3473	SPEC.hypothesis: CED RSFT seed=45 训练，补全 paired t-test 所需的第 3 个 CED seed（现有 s42/s43/s44）。训练数据 2718 samples，3 epochs，~2h。plan_id=plan_mvp2_rsft, claim=3。
3474	SPEC.plan_id: plan_mvp2_rsft
3475	SPEC.model_name: Qwen3-4B + LoRA on SFT adapter
3476	SPEC.data_path: /root/autodl-tmp/rsft_filtered/rsft_train.jsonl
3477	SPEC.data_count: 2718
3478	SPEC.seed: 45
3479	SPEC.server: rtx5090-4x
3480	SPEC.gpu: ['cuda:1']
3481	SPEC.account: root
3482	SPEC.checkpoint_path: N/A
3483	SPEC.log_path: N/A
3484	SPEC.kill_reason: Director 重排优先级: CED s43 先于 s45, cuda:1 改分配给 rsft_ced_s43_train
3485	
3486	========================================================================================================================
3487	EXP_ID: rsft_ced_s45_train_r2
3488	STATUS: DONE
3489	CREATED_AT: 2026-05-16T00:09:11.100Z
3490	UPDATED_AT: 2026-05-16T00:25:40.284Z
3491	CONCLUSION: killed
3492	COMMAND: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.training.rsft_trainer --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --rsft_data_path /root/autodl-tmp/rsft_filtered/rsft_train.jsonl --output_dir /root/autodl-tmp/rsft_output_ced_s45 --learning_rate 2e-5 --num_epochs 3 --per_device_batch_size 4 --gradient_accumulation_steps 4 --lora_rank 64 --lora_alpha 128 --weighted_sampling --eval_data_dir /root/autodl-tmp/data/docred --eval_max_docs 50 --wandb_run_name rsft-ced-s45-r2 --seed 45"
3493	SPEC.server: rtx5090-4x
3494	SPEC.gpu: ['cuda:2']
3495	SPEC.pid: 276143
3496	SPEC.log_path: ~/runs/faith-evidence-ie/rsft_ced_s45_train_r2.log
3497	SPEC.submitted_at: 2026-05-16T00:16:52.439Z
3498	SPEC.submitted_via: submit_training_job
3499	SPEC.backend: tmux
3500	SPEC.account: root
3501	SPEC.wall_clock_seconds: 225.7
3502	SPEC.gpu_hours: 0.06
3503	
3504	========================================================================================================================
3505	EXP_ID: rsft_ced_s45_train_r3
3506	STATUS: DONE
3507	CREATED_AT: 2026-05-16T00:21:01.099Z
3508	UPDATED_AT: 2026-05-16T00:31:23.730Z
3509	CONCLUSION: failed
3510	COMMAND: python -m freige.training.rsft_trainer --seed 45 --data_path rsft_filtered --output_dir rsft_output_ced_s45 --batch_size 4 --gradient_accumulation_steps 4 --weighted_sampling
3511	SPEC.server: rtx5090-4x
3512	SPEC.gpu: ['cuda:2']
3513	SPEC.pid: 277407
3514	SPEC.log_path: ~/runs/faith-evidence-ie/rsft_ced_s45_train_r3.log
3515	SPEC.submitted_at: 2026-05-16T00:21:15.972Z
3516	SPEC.submitted_via: submit_training_job
3517	SPEC.backend: tmux
3518	SPEC.account: root
3519	SPEC.data_path: rsft_filtered
3520	SPEC.data_count: 2718
3521	SPEC.model_name: sft_base + ced_rsft
3522	SPEC.seed: 45
3523	SPEC.wall_clock_seconds: 368.8
3524	SPEC.gpu_hours: 0.1
3525	SPEC.notes: CUDA OOM — GPU 2 被 orphan 进程 PID 276148 占用 31.6GB。Worker 正在清理，将创建 r4 重提交。
3526	
3527	========================================================================================================================
3528	EXP_ID: rsft_ced_s45_train_r4
3529	STATUS: DONE
3530	CREATED_AT: 2026-05-16T00:33:12.797Z
3531	UPDATED_AT: 2026-05-16T02:15:34.043Z
3532	CONCLUSION: success
3533	METRICS: {
3534	  "training_completed": true,
3535	  "checkpoint": "checkpoint-510",
3536	  "note": "Training metrics not captured (r4 retry after OOM). Eval running as eval_rsft_ced_s45."
3537	}
3538	SPEC.checkpoint_path: /root/autodl-tmp/rsft_output_ced_s45/checkpoint-510
3539	SPEC.log_path: /tmp/rsft_ced_s45_r4.log
3540	
3541	========================================================================================================================
3542	EXP_ID: rsft_s43_dev_eval_preds
3543	STATUS: DONE
3544	CREATED_AT: 2026-05-17T08:35:42.135Z
3545	UPDATED_AT: 2026-05-17T23:18:03.147Z
3546	CONCLUSION: success
3547	METRICS: {
3548	  "ign_f1": 0.4512,
3549	  "f1": 0.4601,
3550	  "evi_f1": 0.8063,
3551	  "edcr": 0.6542,
3552	  "evi_f1_joint": 0.3605,
3553	  "format_compliance_rate": 1,
3554	  "field_compliance_rate": 0.809,
3555	  "n_truncated": 184,
3556	  "inference_time_seconds": 10982
3557	}
3558	COMMAND: bash -c "source /root/miniconda3/bin/activate && cd /root/autodl-tmp/freige && python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/rsft_s43_dev_eval_preds"
3559	SPEC.server: rtx5090-4x
3560	SPEC.gpu: ['cuda:0']
3561	SPEC.pid: 431303
3562	SPEC.log_path: ~/runs/faith-evidence-ie/rsft_s43_dev_eval_preds.log
3563	SPEC.submitted_at: 2026-05-17T08:38:45.685Z
3564	SPEC.submitted_via: submit_training_job
3565	SPEC.backend: tmux
3566	SPEC.account: root
3567	SPEC.data_path: /root/autodl-tmp/data/docred
3568	SPEC.data_count: 985
3569	SPEC.model_name: Qwen3-4B + SFT + RSFT-s43(CED)
3570	SPEC.seed: 42
3571	SPEC.checkpoint_source: /root/autodl-tmp/rsft_output_ced_s43/checkpoint-510
3572	SPEC.eval_data: docred_dev
3573	SPEC.checkpoint_path: /root/autodl-tmp/eval_results/rsft_s43_dev_eval_preds
3574	SPEC.wall_clock_seconds: 52757.5
3575	SPEC.gpu_hours: 14.65
3576	
3577	========================================================================================================================
3578	EXP_ID: rsft_s44_dev_eval_preds
3579	STATUS: DONE
3580	CREATED_AT: 2026-05-17T05:02:50.832Z
3581	UPDATED_AT: 2026-05-17T08:25:22.846Z
3582	CONCLUSION: failed
3583	COMMAND: CUDA_VISIBLE_DEVICES=0 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_s44/checkpoint-510 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/rsft_s44_dev_with_preds
3584	SPEC.server: rtx5090-4x
3585	SPEC.gpu: cuda:0
3586	SPEC.pid: 414832
3587	SPEC.log_path: ~/runs/faith-evidence-ie/rsft_s44_dev_eval_preds.log
3588	SPEC.submitted_at: 2026-05-17T05:02:50.357Z
3589	SPEC.submitted_via: submit_training_job
3590	SPEC.backend: tmux
3591	SPEC.account: root
3592	SPEC.data_path: /root/autodl-tmp/data/docred
3593	SPEC.data_count: 985
3594	SPEC.model_name: Qwen3-4B + SFT + RSFT-s44
3595	SPEC.seed: 42
3596	SPEC.checkpoint_source: /root/autodl-tmp/rsft_output_s44/checkpoint-510
3597	SPEC.eval_data: docred_dev
3598	SPEC.checkpoint_path: N/A (eval)
3599	SPEC.failure_reason: Disk full - EXIT_CODE=124 timeout at 97% progress
3600	SPEC.wall_clock_seconds: 12152.5
3601	SPEC.gpu_hours: 3.38
3602	
3603	========================================================================================================================
3604	EXP_ID: wave1_grpo_bf16_g4
3605	STATUS: DONE
3606	CREATED_AT: 2026-05-18T12:46:19.740Z
3607	UPDATED_AT: 2026-05-18T20:09:28.981Z
3608	CONCLUSION: success
3609	METRICS: {
3610	  "reward_mean": 1.7646,
3611	  "steps_completed": 200,
3612	  "max_steps": 200
3613	}
3614	COMMAND: bash /root/autodl-tmp/freige/scripts/d102_next_batch/grpo_bf16_g4.sh
3615	SPEC.server: rtx5090-4x
3616	SPEC.gpu: ['cuda:2']
3617	SPEC.pid: 542121
3618	SPEC.data_path: /root/autodl-tmp/data/docred/train_annotated.json
3619	SPEC.data_count: 3027
3620	SPEC.model_name: Qwen3-4B
3621	SPEC.seed: 42
3622	SPEC.checkpoint_source: /root/autodl-tmp/sft_output
3623	SPEC.output_dir: /root/autodl-tmp/grpo_bf16_g4
3624	SPEC.log_path: /root/autodl-tmp/grpo_bf16_g4.log
3625	SPEC.method: GRPO bf16 no-quantize
3626	SPEC.num_generations: 4
3627	SPEC.gradient_accumulation_steps: 16
3628	SPEC.max_steps: 200
3629	SPEC.kl_coef: 0
3630	SPEC.reward_weights: {'format': 0.3, 'f1': 3, 'ced': 1}
3631	SPEC.plan_id: plan_015
3632	
3633	========================================================================================================================
3634	EXP_ID: wave1_sft_4b_s43
3635	STATUS: DONE
3636	CREATED_AT: 2026-05-18T12:44:52.340Z
3637	UPDATED_AT: 2026-05-18T14:01:01.015Z
3638	CONCLUSION: success
3639	COMMAND: bash scripts/d102_next_batch/sft_seed43.sh
3640	SPEC.server: rtx5090-4x
3641	SPEC.gpu_id: 0
3642	SPEC.pid: 540777
3643	SPEC.data_path: /root/autodl-tmp/data/docred/train_annotated.json
3644	SPEC.data_count: 3027
3645	SPEC.model_name: Qwen3-4B
3646	SPEC.seed: 43
3647	SPEC.output_dir: /root/autodl-tmp/sft_output_seed43
3648	SPEC.plan_id: plan_w3_sft_seeds
3649	SPEC.wandb_run_name: sft-4b-seed43
3650	SPEC.checkpoint_path: /root/autodl-tmp/sft_output_seed43/
3651	SPEC.log_path: /root/autodl-tmp/sft_output_seed43/training.log
3652	SPEC.train_loss: 0.7011
3653	SPEC.eval_loss: 0.7482
3654	SPEC.train_steps: 144
3655	SPEC.epochs: 3
3656	SPEC.eval_mean_token_accuracy: 0.83
3657	
3658	========================================================================================================================
3659	EXP_ID: wave1_sft_4b_s43_eval
3660	STATUS: DONE
3661	CREATED_AT: 2026-05-18T14:01:42.261Z
3662	UPDATED_AT: 2026-05-18T15:43:30.104Z
3663	CONCLUSION: failed
3664	COMMAND: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.eval.inference --model_path /root/autodl-tmp/sft_output_seed43/ --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/sft_4b_s43_eval"
3665	SPEC.server: rtx5090-4x
3666	SPEC.gpu: ['cuda:0']
3667	SPEC.pid: 548328
3668	SPEC.log_path: ~/runs/faith-evidence-ie/wave1_sft_4b_s43_eval.log
3669	SPEC.submitted_at: 2026-05-18T14:02:15.167Z
3670	SPEC.submitted_via: submit_training_job
3671	SPEC.backend: tmux
3672	SPEC.account: root
3673	SPEC.data_path: /root/autodl-tmp/data/docred
3674	SPEC.data_count: 985
3675	SPEC.model_name: Qwen3-4B + SFT-s43
3676	SPEC.seed: 42
3677	SPEC.checkpoint_source: wave1_sft_4b_s43
3678	SPEC.eval_data: DocRED dev
3679	SPEC.failure_reason: inference.py adapter validation bug: detects LoRA adapter_config.json and requires --sft_adapter, but SFT adapter as model_path should not trigger this. Fix: use --model_path=base_model --sft_adapter=adapter_path
3680	SPEC.wall_clock_seconds: 6074.9
3681	SPEC.gpu_hours: 1.69
3682	
3683	========================================================================================================================
3684	EXP_ID: wave1_sft_4b_s43_eval_r2
3685	STATUS: DONE
3686	CREATED_AT: 2026-05-18T19:29:28.052Z
3687	UPDATED_AT: 2026-05-18T21:34:25.964Z
3688	CONCLUSION: success
3689	METRICS: {
3690	  "ign_f1": 0.4365,
3691	  "rel_f1": 0.4429,
3692	  "evi_f1_joint": 0.3462,
3693	  "evi_f1_tp": 0.8021,
3694	  "edcr": 0.6827,
3695	  "format_compliance_rate": 1,
3696	  "n_truncated": 318,
3697	  "n_predictions": 17055,
3698	  "inference_time_seconds": 7157.9
3699	}
3700	COMMAND: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output_seed43/ --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/wave1_sft_4b_s43_eval_r2"
3701	SPEC.server: rtx5090-4x
3702	SPEC.gpu: ['cuda:2']
3703	SPEC.pid: 568649
3704	SPEC.log_path: ~/runs/faith-evidence-ie/wave1_sft_4b_s43_eval_r2.log
3705	SPEC.submitted_at: 2026-05-18T19:29:27.427Z
3706	SPEC.submitted_via: submit_training_job
3707	SPEC.backend: tmux
3708	SPEC.account: root
3709	SPEC.data_path: /root/autodl-tmp/data/docred
3710	SPEC.data_count: 985
3711	SPEC.model_name: Qwen3-4B + SFT-s43
3712	SPEC.seed: 42
3713	SPEC.checkpoint_source: wave1_sft_4b_s43
3714	SPEC.eval_data: DocRED dev
3715	SPEC.wall_clock_seconds: 7498.5
3716	SPEC.gpu_hours: 2.08
3717	
3718	========================================================================================================================
3719	EXP_ID: wave1_sft_4b_s44
3720	STATUS: DONE
3721	CREATED_AT: 2026-05-18T12:44:43.563Z
3722	UPDATED_AT: 2026-05-18T14:01:03.605Z
3723	CONCLUSION: success
3724	COMMAND: bash /root/autodl-tmp/freige/scripts/d102_next_batch/sft_seed44.sh
3725	SPEC.server: rtx5090-4x
3726	SPEC.gpu_id: 1
3727	SPEC.pid: 540984
3728	SPEC.data_path: /root/autodl-tmp/data/docred/train_annotated.json
3729	SPEC.data_count: 3027
3730	SPEC.model_name: Qwen3-4B
3731	SPEC.seed: 44
3732	SPEC.plan_id: plan_w3_sft_seeds
3733	SPEC.checkpoint_source: /root/autodl-tmp/models/Qwen3-4B
3734	SPEC.log_path: /root/autodl-tmp/sft_output_seed44/training.log
3735	SPEC.checkpoint_path: /root/autodl-tmp/sft_output_seed44/
3736	SPEC.train_loss: 0.7008
3737	SPEC.eval_loss: 0.7478
3738	SPEC.train_steps: 144
3739	SPEC.epochs: 3
3740	SPEC.eval_mean_token_accuracy: 0.8299
3741	
3742	========================================================================================================================
3743	EXP_ID: wave1_sft_4b_s44_eval
3744	STATUS: DONE
3745	CREATED_AT: 2026-05-18T14:01:43.597Z
3746	UPDATED_AT: 2026-05-18T15:43:33.593Z
3747	CONCLUSION: failed
3748	COMMAND: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && python -m freige.eval.inference --model_path /root/autodl-tmp/sft_output_seed44/ --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/sft_4b_s44_eval"
3749	SPEC.server: rtx5090-4x
3750	SPEC.gpu: ['cuda:1']
3751	SPEC.pid: 548407
3752	SPEC.log_path: ~/runs/faith-evidence-ie/wave1_sft_4b_s44_eval.log
3753	SPEC.submitted_at: 2026-05-18T14:02:17.363Z
3754	SPEC.submitted_via: submit_training_job
3755	SPEC.backend: tmux
3756	SPEC.account: root
3757	SPEC.data_path: /root/autodl-tmp/data/docred
3758	SPEC.data_count: 985
3759	SPEC.model_name: Qwen3-4B + SFT-s44
3760	SPEC.seed: 42
3761	SPEC.checkpoint_source: wave1_sft_4b_s44
3762	SPEC.eval_data: DocRED dev
3763	SPEC.failure_reason: Same inference.py adapter validation bug as s43 eval
3764	SPEC.wall_clock_seconds: 6076.2
3765	SPEC.gpu_hours: 1.69
3766	
3767	========================================================================================================================
3768	EXP_ID: wave1_sft_4b_s44_eval_r2
3769	STATUS: ANALYZING
3770	CREATED_AT: 2026-05-18T20:05:57.119Z
3771	UPDATED_AT: 2026-05-18T21:59:29.645Z
3772	COMMAND: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=1 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output_seed44/ --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/wave1_sft_4b_s44_eval_r2"
3773	SPEC.server: rtx5090-4x
3774	SPEC.gpu: ['cuda:1']
3775	SPEC.pid: 571192
3776	SPEC.log_path: ~/runs/faith-evidence-ie/wave1_sft_4b_s44_eval_r2.log
3777	SPEC.submitted_at: 2026-05-18T20:06:13.257Z
3778	SPEC.submitted_via: submit_training_job
3779	SPEC.backend: tmux
3780	SPEC.account: root
3781	SPEC.data_path: /root/autodl-tmp/data/docred
3782	SPEC.data_count: 985
3783	SPEC.model_name: Qwen3-4B + SFT-s44
3784	SPEC.seed: 42
3785	SPEC.checkpoint_source: wave1_sft_4b_s44
3786	SPEC.eval_data: DocRED dev
3787	SPEC.checkpoint_path: /root/autodl-tmp/eval_results/wave1_sft_4b_s44_eval_r2
3788	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "2c26ffc7-a699-4645-be29-5d999350a4ed"
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
  "task_id": "aa0dedafabeeb8ab6",
  "tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "description": "Running Produce summary table of all eval experiments with metrics",
  "usage": {
    "total_tokens": 114915,
    "tool_uses": 20,
    "duration_ms": 115028
  },
  "last_tool_name": "Bash",
  "uuid": "b35d2c6e-b8e1-4ba3-a775-5d966e9f8da6",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0"
}
```

---


### Tool call

_source line 73_

<details open><summary>🔧 Tool call — Bash · `toolu_018iLT6fUEBQTep3oEdcTP74`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/596d8411-63f5-4757-a2a4-2c57b1fcaba0/tool-results/mcp-agent-ml-research-read_registry-1779141732674.txt\"\n\nwith open(fpath, 'r') as f:\n    raw = json.load(f)\n\ndata = json.loads(raw[\"result\"])\nexperiments = data[\"data\"][\"experiments\"]\n\n# Count by status for all matched experiments\ndef matches(exp_id, exp_data):\n    eid_lower = exp_id.lower()\n    if \"4b\" in eid_lower: return True\n    if \"wave1_sft\" in eid_lower: return True\n    if \"rsft_ced\" in eid_lower: return True\n    if \"flat_nli\" in eid_lower: return True\n    spec = exp_data.get(\"spec\", {}) or {}\n    spec_str = json.dumps(spec).lower()\n    if \"qwen3-4b\" in spec_str or \"qwen3_4b\" in spec_str: return True\n    return False\n\nmatched = {eid: edata for eid, edata in experiments.items() if matches(eid, edata)}\n\n# Status summary\nfrom collections import Counter\nstatus_counts = Counter(e.get('status', 'N/A') for e in matched.values())\nconclusion_counts = Counter(e.get('conclusion', 'N/A') for e in matched.values())\n\nprint(\"STATUS DISTRIBUTION:\")\nfor s, c in sorted(status_counts.items()):\n    print(f\"  {s}: {c}\")\nprint()\nprint(\"CONCLUSION DISTRIBUTION:\")\nfor s, c in sorted(conclusion_counts.items()):\n    print(f\"  {s}: {c}\")\nprint()\n\n# Specifically: successful eval experiments with ign_f1 metrics\nprint(\"=\" * 100)\nprint(\"SUCCESSFUL EVAL EXPERIMENTS WITH ign_f1 METRICS\")\nprint(\"=\" * 100)\neval_results = []\nfor eid in sorted(matched.keys()):\n    e = matched[eid]\n    metrics = e.get('metrics', {}) or {}\n    conclusion = e.get('conclusion', '')\n    if not metrics:\n        continue\n    # Look for ign_f1 in metrics (could be nested for batch evals)\n    ign_f1 = metrics.get('ign_f1', None)\n    rel_f1 = metrics.get('rel_f1', metrics.get('f1', None))\n    evi_f1 = metrics.get('evi_f1', None)\n    edcr = metrics.get('edcr', metrics.get('EDCR', None))\n    evi_joint = metrics.get('evi_f1_joint', None)\n    \n    if ign_f1 is not None or rel_f1 is not None:\n        model = (e.get('spec', {}) or {}).get('model_name', 'N/A')\n        seed = (e.get('spec', {}) or {}).get('seed', 'N/A')\n        eval_results.append({\n            'exp_id': eid,\n            'status': e.get('status'),\n            'conclusion': conclusion,\n            'model_name': model,\n            'seed': seed,\n            'ign_f1': ign_f1,\n            'rel_f1': rel_f1,\n            'evi_f1': evi_f1,\n            'edcr': edcr,\n            'evi_f1_joint': evi_joint,\n        })\n\n# Sort by ign_f1 descending\neval_results.sort(key=lambda x: x.get('ign_f1') or x.get('rel_f1') or 0, reverse=True)\nfor r in eval_results:\n    print(f\"\\n  {r['exp_id']}\")\n    print(f\"    status={r['status']}, conclusion={r['conclusion']}\")\n    print(f\"    model: {r['model_name']}, seed: {r['seed']}\")\n    print(f\"    ign_f1={r['ign_f1']}, rel_f1={r['rel_f1']}, evi_f1={r['evi_f1']}, edcr={r['edcr']}, evi_f1_joint={r['evi_f1_joint']}\")\n\nprint(f\"\\n\\nTotal experiments with metrics: {len(eval_results)}\")\nPYEOF",
  "description": "Produce summary table of all eval experiments with metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "05fd3abe-c7e2-49ef-80c9-5299172ed5de",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U9o4TT6vHPZuYp99jWsfDw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8758,
      "cache_read_input_tokens": 105612,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8758,
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

_source line 74 · 2026-05-18T22:04:18.328Z_

<details><summary>↩ Tool result · `toolu_018iLT6fUEBQTep3oEdcTP74`</summary>

```text
STATUS DISTRIBUTION:
  ANALYZING: 1
  DONE: 131
  RUNNING: 1

CONCLUSION DISTRIBUTION:
  N/A: 2
  failed: 29
  killed: 27
  negative: 18
  success: 57

====================================================================================================
SUCCESSFUL EVAL EXPERIMENTS WITH ign_f1 METRICS
====================================================================================================

  eval_plan_014_no_evidence_r2
    status=DONE, conclusion=success
    model: N/A, seed: N/A
    ign_f1=0.4721, rel_f1=0.4876, evi_f1=0, edcr=0, evi_f1_joint=0

  plan_014_no_evidence_eval_d076
    status=DONE, conclusion=success
    model: Qwen3-4B (no-evidence SFT), seed: 42
    ign_f1=0.4721, rel_f1=0.4876, evi_f1=None, edcr=None, evi_f1_joint=None

  mvp2_eval_rsft_s43_r2
    status=DONE, conclusion=success
    model: N/A, seed: N/A
    ign_f1=0.4683, rel_f1=0.4683, evi_f1=0.8156, edcr=0.6388, evi_f1_joint=0.3711

  mvp2_rsft_train_r1_s44
    status=DONE, conclusion=success
    model: N/A, seed: N/A
    ign_f1=None, rel_f1=0.4655, evi_f1=0.8087, edcr=0.635, evi_f1_joint=0.3713

  plan_011_grpo_g8_bf16_eval
    status=DONE, conclusion=success
    model: N/A, seed: N/A
    ign_f1=0.4549, rel_f1=0.4549, evi_f1=0.8086, edcr=0.6318, evi_f1_joint=None

  eval_plan_001_flat_nli
    status=DONE, conclusion=success
    model: Qwen3-4B + SFT + RSFT-flat-NLI, seed: 42
    ign_f1=0.4539, rel_f1=0.4539, evi_f1=0.8043, edcr=0.6431, evi_f1_joint=None

  lead2_ckpt20_eval
    status=DONE, conclusion=success
    model: Qwen3-4B (SFT+RSFT_CED_s43 merged + GRPO ckpt-20), seed: 42
    ign_f1=0.4533, rel_f1=0.4617, evi_f1=0.8103, edcr=0.6465, evi_f1_joint=0.3642

  reeval_flat_nli_s43
    status=DONE, conclusion=success
    model: Qwen3-4B + SFT + flat-NLI RSFT s43, seed: 43
    ign_f1=0.4523, rel_f1=0.4523, evi_f1=0.8158, edcr=0.6505, evi_f1_joint=None

  eval_flat_nli_s44
    status=DONE, conclusion=success
    model: N/A, seed: N/A
    ign_f1=0.452126, rel_f1=0.461506, evi_f1=0.813123, edcr=0.645808, evi_f1_joint=0.359673

  eval_rsft_ced_s43
    status=DONE, conclusion=success
    model: N/A, seed: N/A
    ign_f1=0.4512, rel_f1=0.4601, evi_f1=0.8063, edcr=0.6542, evi_f1_joint=0.3605

  rsft_s43_dev_eval_preds
    status=DONE, conclusion=success
    model: Qwen3-4B + SFT + RSFT-s43(CED), seed: 42
    ign_f1=0.4512, rel_f1=0.4601, evi_f1=0.8063, edcr=0.6542, evi_f1_joint=0.3605

  reeval_ced_s44
    status=DONE, conclusion=success
    model: N/A, seed: N/A
    ign_f1=0.4511, rel_f1=0.4621, evi_f1=0.805, edcr=0.635, evi_f1_joint=0.3677

  mvp2_eval_rsft_r2b_maxtok1536_r2
    status=DONE, conclusion=negative
    model: N/A, seed: N/A
    ign_f1=0.4504, rel_f1=0.4504, evi_f1=0.8102, edcr=0.674, evi_f1_joint=None

  reeval_flat_nli_s43_r2
    status=DONE, conclusion=success
    model: N/A, seed: N/A
    ign_f1=0.4503, rel_f1=0.4586, evi_f1=0.8113, edcr=0.6552, evi_f1_joint=0.358

  mvp2_eval_rsft_r2a
    status=DONE, conclusion=success
    model: Qwen3-4B + SFT + RSFT r2a, seed: 42
    ign_f1=0.4494, rel_f1=0.4494, evi_f1=0.8108, edcr=0.6641, evi_f1_joint=0.3509

  mvp2_rsft_r2a
    status=DONE, conclusion=success
    model: N/A, seed: N/A
    ign_f1=None, rel_f1=0.4494, evi_f1=0.8108, edcr=0.6641, evi_f1_joint=None

  mvp2_eval_rsft_r2b
    status=DONE, conclusion=success
    model: Qwen3-4B + SFT + RSFT r2b, seed: 42
    ign_f1=0.4493, rel_f1=0.4493, evi_f1=0.8128, edcr=0.6609, evi_f1_joint=0.349

  mvp2_rsft_r2b
    status=DONE, conclusion=success
    model: N/A, seed: N/A
    ign_f1=None, rel_f1=0.4493, evi_f1=0.8128, edcr=0.6609, evi_f1_joint=None

  eval_flat_nli_seed45
    status=DONE, conclusion=success
    model: Qwen3-4B, seed: 45
    ign_f1=0.446181, rel_f1=0.455052, evi_f1=0.815399, edcr=0.652133, evi_f1_joint=0.355612

  mvp2_eval_rsft_r1
    status=DONE, conclusion=success
    model: Qwen3-4B + SFT + RSFT r1, seed: 42
    ign_f1=None, rel_f1=0.4449, evi_f1=0.8187, edcr=0.6565, evi_f1_joint=0.3468

  reeval_flat_nli_s42
    status=DONE, conclusion=success
    model: Qwen3-4B + SFT + flat-NLI RSFT s42, seed: 42
    ign_f1=0.4448, rel_f1=0.4535, evi_f1=0.8039, edcr=0.6458, evi_f1_joint=0.3558

  grpo_bf16_g4_ckpt100_eval
    status=DONE, conclusion=success
    model: Qwen3-4B + SFT + GRPO-bf16-G4-ckpt100, seed: 42
    ign_f1=0.4431, rel_f1=0.4511, evi_f1=0.801, edcr=0.6453, evi_f1_joint=0.3532

  reeval_ced_s42
    status=DONE, conclusion=success
    model: N/A, seed: N/A
    ign_f1=0.4423, rel_f1=0.4517, evi_f1=0.8175, edcr=0.6569, evi_f1_joint=0.3518

  eval_rsft_ced_s45
    status=DONE, conclusion=success
    model: N/A, seed: N/A
    ign_f1=0.4416, rel_f1=0.4514, evi_f1=0.8174, edcr=0.655, evi_f1_joint=0.3558

  wave1_sft_4b_s43_eval_r2
    status=DONE, conclusion=success
    model: Qwen3-4B + SFT-s43, seed: 42
    ign_f1=0.4365, rel_f1=0.4429, evi_f1=None, edcr=0.6827, evi_f1_joint=0.3462

  reeval_rsft_topk3
    status=DONE, conclusion=negative
    model: RSFT top_k=3 + SFT adapter, seed: 42
    ign_f1=0.4364, rel_f1=0.4454, evi_f1=0.8088, edcr=0.6635, evi_f1_joint=None

  plan_007_redocred_rsft_eval_r5
    status=DONE, conclusion=success
    model: Qwen3-4B + SFT + RSFT-CED-s43-ckpt510, seed: 42
    ign_f1=0.4145, rel_f1=0.4234, evi_f1=0.8182, edcr=0.621, evi_f1_joint=None

  random_rsft_k1_eval
    status=DONE, conclusion=success
    model: Qwen3-4B + SFT + Random-RSFT-k1, seed: 42
    ign_f1=0.4114, rel_f1=0.4198, evi_f1=0.7964, edcr=0.6971, evi_f1_joint=0.3216

  eval_sft_baseline_noquant
    status=DONE, conclusion=success
    model: Qwen3-4B + SFT LoRA (no quantization), seed: 42
    ign_f1=None, rel_f1=0.4106, evi_f1=0.8013, edcr=0.7039, evi_f1_joint=0.3216

  mvp2_eval_sft_baseline
    status=DONE, conclusion=success
    model: Qwen3-4B + SFT LoRA adapter, seed: 42
    ign_f1=None, rel_f1=0.4057, evi_f1=0.7979, edcr=0.7118, evi_f1_joint=0.3117

  mvp2_sft_eval_r2
    status=DONE, conclusion=success
    model: Qwen3-4B, seed: 42
    ign_f1=0.4057, rel_f1=0.4057, evi_f1=0.7979, edcr=0.7118, evi_f1_joint=None

  mvp2_sft_eval_r3
    status=DONE, conclusion=success
    model: Qwen3-4B, seed: 42
    ign_f1=0.4057, rel_f1=0.4057, evi_f1=0.7979, edcr=0.7118, evi_f1_joint=None

  eval_plan_012_dpo_1ep_fixed_r2
    status=DONE, conclusion=negative
    model: Qwen3-4B + SFT + DPO 1ep, seed: 42
    ign_f1=0.4034, rel_f1=0.4034, evi_f1=0.8088, edcr=0.7139, evi_f1_joint=None

  reeval_sft_baseline_d076
    status=DONE, conclusion=success
    model: Qwen3-4B + SFT baseline (no RSFT), seed: 42
    ign_f1=0.3974, rel_f1=0.4049, evi_f1=0.7986, edcr=0.6982, evi_f1_joint=0.3147

  plan_007_redocred_4b_sft_eval_r2
    status=DONE, conclusion=success
    model: N/A, seed: N/A
    ign_f1=0.3659, rel_f1=0.3706, evi_f1=0.817, edcr=0.6674, evi_f1_joint=None

  plan_012_dpo_ced
    status=DONE, conclusion=negative
    model: Qwen3-4B + SFT + CED-DPO, seed: 42
    ign_f1=None, rel_f1=0.3429, evi_f1=0.8403, edcr=0.7294, evi_f1_joint=None

  mvp2_eval_ced_kl001_r4_step100
    status=DONE, conclusion=negative
    model: Qwen3-4B + SFT adapter + GRPO ced_kl001 step-100, seed: 42
    ign_f1=0.2167, rel_f1=0.2167, evi_f1=0.5746, edcr=0.8539, evi_f1_joint=None

  mvp2_eval_ced_kl001_r4_step90
    status=DONE, conclusion=negative
    model: Qwen3-4B + SFT + GRPO ced_kl001 step-90, seed: 42
    ign_f1=0.2108, rel_f1=0.2108, evi_f1=0.5666, edcr=0.8584, evi_f1_joint=None

  mvp2_eval_ced_kl001_r4_early
    status=DONE, conclusion=negative
    model: Qwen3-4B, seed: 42
    ign_f1=0.1563, rel_f1=0.1563, evi_f1=0.5643, edcr=0.8858, evi_f1_joint=None

  mvp2_rsft_train_r1
    status=DONE, conclusion=success
    model: N/A, seed: N/A
    ign_f1=None, rel_f1=0.0483, evi_f1=None, edcr=None, evi_f1_joint=None

  mvp2_eval_lr5e6_r1_ckpt100
    status=DONE, conclusion=negative
    model: N/A, seed: N/A
    ign_f1=0.0138, rel_f1=0.0138, evi_f1=0.8504, edcr=0.9876, evi_f1_joint=None

  mvp2_eval_lr5e6_r1_ckpt80
    status=DONE, conclusion=negative
    model: Qwen3-4B + SFT + GRPO lr5e6 ckpt-80, seed: 42
    ign_f1=0.0116, rel_f1=0.0116, evi_f1=0.828, edcr=0.993, evi_f1_joint=None

  mvp2_eval_lr5e6_r1_ckpt60_r2
    status=DONE, conclusion=negative
    model: Qwen3-4B + SFT + GRPO lr5e6 ckpt-60, seed: 42
    ign_f1=None, rel_f1=0.0093, evi_f1=0.81, edcr=0.993, evi_f1_joint=None

  mvp2_eval_lr5e6_r1_ckpt20
    status=DONE, conclusion=negative
    model: Qwen3-4B + SFT + GRPO lr5e6 ckpt-20, seed: 42
    ign_f1=None, rel_f1=0.0077, evi_f1=0.628, edcr=0.993, evi_f1_joint=None

  mvp2_eval_lr5e6_r1_ckpt40_r2
    status=DONE, conclusion=negative
    model: Qwen3-4B + SFT + GRPO lr5e6 ckpt-40, seed: 42
    ign_f1=None, rel_f1=0.0071, evi_f1=0.7584, edcr=0.9942, evi_f1_joint=None

  mvp2_eval_ced_kl001_r4_ckpt10
    status=DONE, conclusion=success
    model: Qwen3-4B, seed: 42
    ign_f1=None, rel_f1=0.00296, evi_f1=0.72, edcr=0.9983, evi_f1_joint=None

  eval_plan_001_flat_nli_s43
    status=DONE, conclusion=failed
    model: Qwen3-4B + flat-NLI RSFT s43 adapter, seed: 43
    ign_f1=0.0022, rel_f1=0.0022, evi_f1=0.8533, edcr=0.9982, evi_f1_joint=None

  eval_plan_012_dpo_ced_1ep
    status=DONE, conclusion=negative
    model: Qwen3-4B + DPO-CED-1ep LoRA, seed: 42
    ign_f1=0.0022, rel_f1=0.0022, evi_f1=0.75, edcr=0.9982, evi_f1_joint=None

  plan_012_dpo_ced_1ep
    status=DONE, conclusion=negative
    model: Qwen3-4B + SFT + CED-DPO (1ep), seed: 42
    ign_f1=None, rel_f1=0.0022, evi_f1=0.75, edcr=0.9982, evi_f1_joint=None


Total experiments with metrics: 49
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "3c1b2d23-f363-4576-bb42-86c976744de2"
}
```

</details>

---


### System

_source line 75_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "aa0dedafabeeb8ab6",
  "tool_use_id": "toolu_01GK9KaSv83WhaAJmvpUVdYs",
  "status": "completed",
  "output_file": "",
  "summary": "Parse 4B eval experiments from registry",
  "usage": {
    "total_tokens": 121163,
    "tool_uses": 20,
    "duration_ms": 154478
  },
  "uuid": "c5b74289-5443-4f22-8023-ec6c26303351",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0"
}
```

---


### Tool result

_source line 76 · 2026-05-18T22:04:57.587Z_

<details><summary>↩ Tool result · `toolu_01GK9KaSv83WhaAJmvpUVdYs`</summary>

```text
Here is the complete analysis of all 4B-related experiments from the registry.

---

## Summary

**133 total experiments** matched the filter criteria (all referencing Qwen3-4B in their spec). Status breakdown: 131 DONE, 1 RUNNING (`grpo_bf16_g4_ckpt200_eval`), 1 ANALYZING (`wave1_sft_4b_s44_eval_r2`). Conclusion breakdown: 57 success, 29 failed, 27 killed, 18 negative, 2 pending.

**49 experiments** had quantitative metrics (ign_f1 or rel_f1).

---

## Explicitly 4B-named experiments (wave1_sft_4b_*)

### Training
| exp_id | status | conclusion | seed | train_loss | eval_loss |
|--------|--------|------------|------|------------|-----------|
| `wave1_sft_4b_s43` | DONE | success | 43 | 0.7011 | 0.7482 |
| `wave1_sft_4b_s44` | DONE | success | 44 | 0.7008 | 0.7478 |

### Eval
| exp_id | status | conclusion | ign_f1 | rel_f1 | evi_f1 | edcr | evi_f1_joint |
|--------|--------|------------|--------|--------|--------|------|--------------|
| `wave1_sft_4b_s43_eval` | DONE | **failed** | -- | -- | -- | -- | -- |
| `wave1_sft_4b_s43_eval_r2` | DONE | success | **0.4365** | 0.4429 | 0.8021 | 0.6827 | 0.3462 |
| `wave1_sft_4b_s44_eval` | DONE | **failed** | -- | -- | -- | -- | -- |
| `wave1_sft_4b_s44_eval_r2` | **ANALYZING** | pending | -- | -- | -- | -- | -- |

Both initial eval attempts (`wave1_sft_4b_s43_eval`, `wave1_sft_4b_s44_eval`) failed due to `inference.py adapter validation bug: detects LoRA adapter_config.json and requires --sft_adapter`. The r2 fixes used `--model_path=base_model --sft_adapter=adapter_path` instead.

Key commands:
- **s43_eval (failed)**: `python -m freige.eval.inference --model_path /root/autodl-tmp/sft_output_seed43/ --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/sft_4b_s43_eval`
- **s43_eval_r2 (success)**: `python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output_seed43/ --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/wave1_sft_4b_s43_eval_r2`
- **s44_eval_r2 (running)**: `CUDA_VISIBLE_DEVICES=1 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output_seed44/ --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/wave1_sft_4b_s44_eval_r2`

---

## Re-DocRED 4B eval (`plan_007_redocred_4b_sft_eval*`)

| exp_id | conclusion | ign_f1 | f1 | evi_f1 | edcr |
|--------|------------|--------|-----|--------|------|
| `plan_007_redocred_4b_sft_eval` | failed | -- | -- | -- | -- |
| `plan_007_redocred_4b_sft_eval_r2` | success | **0.3659** | 0.3706 | 0.817 | 0.6674 |

Command for r2: `CUDA_VISIBLE_DEVICES=0 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/re-docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/plan_007_redocred_4b_sft_eval`

Re-DocRED RSFT eval (`plan_007_redocred_rsft_eval_r5`): ign_f1=**0.4145**, f1=0.4234, evi_f1=0.8182, edcr=0.621 (improvement of +4.86pp over SFT baseline on Re-DocRED).

---

## Top eval results leaderboard (ign_f1, all successful/valid experiments)

| Rank | exp_id | Model | seed | ign_f1 | rel_f1 | evi_f1 | edcr | evi_f1_joint |
|------|--------|-------|------|--------|--------|--------|------|--------------|
| 1 | `eval_plan_014_no_evidence_r2` | Qwen3-4B no-evidence SFT | 42 | **0.4721** | 0.4876 | 0 | 0 | 0 |
| 2 | `mvp2_eval_rsft_s43_r2` | SFT+RSFT s43 | 42 | **0.4683** | 0.4683 | 0.8156 | 0.6388 | 0.3711 |
| 3 | `plan_011_grpo_g8_bf16_eval` | SFT+GRPO-G8-bf16 | 42 | **0.4549** | 0.4549 | 0.8086 | 0.6318 | -- |
| 4 | `eval_plan_001_flat_nli` | SFT+RSFT-flat-NLI | 42 | **0.4539** | 0.4539 | 0.8043 | 0.6431 | -- |
| 5 | `lead2_ckpt20_eval` | SFT+RSFT merged+GRPO ckpt-20 | 42 | **0.4533** | 0.4617 | 0.8103 | 0.6465 | 0.3642 |
| 6 | `reeval_flat_nli_s43` | SFT+flat-NLI RSFT s43 | 43 | **0.4523** | 0.4523 | 0.8158 | 0.6505 | -- |
| 7 | `eval_flat_nli_s44` | SFT+RSFT flat-NLI s44 | 44 | **0.4521** | 0.4615 | 0.8131 | 0.6458 | 0.3597 |
| 8 | `eval_rsft_ced_s43` | SFT+RSFT CED s43 | 43 | **0.4512** | 0.4601 | 0.8063 | 0.6542 | 0.3605 |
| 9 | `reeval_ced_s44` | SFT+RSFT CED s44 | 44 | **0.4511** | 0.4621 | 0.805 | 0.635 | 0.3677 |
| 10 | `reeval_flat_nli_s43_r2` | SFT+flat-NLI RSFT s43 | 43 | **0.4503** | 0.4586 | 0.8113 | 0.6552 | 0.358 |

---

## Currently active experiments

1. **`grpo_bf16_g4_ckpt200_eval`** (RUNNING): evaluating GRPO bf16 G4 checkpoint-200 on DocRED dev
2. **`wave1_sft_4b_s44_eval_r2`** (ANALYZING): SFT seed=44 eval, inference likely complete but metrics not yet extracted

---

## Notable bugs found in eval configurations

1. **Missing `--sft_adapter` bug**: `eval_plan_001_flat_nli_s43`, `eval_plan_008_rsft_topk3`, `eval_plan_012_dpo_ced_1ep` all produced garbage metrics (ign_f1 near 0.002) because `--sft_adapter` was omitted. These were later re-run with the fix.

2. **Adapter path ordering bug**: `plan_007_redocred_rsft_eval` through `r4` failed because `--model_path` and `--sft_adapter` args were in wrong order (RSFT LoRA merged to bare Qwen3-4B without SFT base). Fixed in `r5` with correct 3-param ordering: `--model_path RSFT_ckpt --base_model Qwen3-4B --sft_adapter sft_output`.

3. **wave1_sft_4b eval bug**: Initial `wave1_sft_4b_s43_eval` and `wave1_sft_4b_s44_eval` failed because `inference.py` detected LoRA `adapter_config.json` inside `--model_path` and required `--sft_adapter`. Fix: swap to `--model_path=base_model --sft_adapter=adapter_path`.

agentId: aa0dedafabeeb8ab6 (use SendMessage with to: 'aa0dedafabeeb8ab6' to continue this agent)
&lt;usage>total_tokens: 123296
tool_uses: 20
duration_ms: 154480&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "315df784-40a1-4717-a954-27fbb2fb9d0a",
  "tool_use_result": {
    "status": "completed",
    "prompt": "I need you to analyze a large JSON registry file and extract all 4B-related experiments (especially eval experiments).\n\nThe file is at: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/596d8411-63f5-4757-a2a4-2c57b1fcaba0/tool-results/mcp-agent-ml-research-read_registry-1779141732674.txt\n\nIt's JSON with schema: {result: string} where result is a JSON string that needs to be parsed.\n\nSteps:\n1. First probe the structure with jq (type, length, keys)\n2. Parse the nested JSON (result is a JSON string containing the actual data)\n3. Filter for ALL experiments that match ANY of these criteria:\n   - exp_id contains \"4b\" or \"4B\" (case insensitive)\n   - exp_id contains \"wave1_sft\" \n   - exp_id contains \"rsft_ced\" or \"flat_nli\"\n   - Any experiment whose command/spec references \"Qwen3-4B\" or \"qwen3-4b\"\n4. For each matching experiment, extract:\n   - exp_id\n   - status\n   - conclusion (if any)\n   - The full spec.command (the actual shell command used)\n   - Any metrics (especially ign_f1)\n   - created_at / updated_at\n\nOutput ALL of this information verbatim - do not summarize or truncate commands. I need the full command strings to audit eval configurations.\n\nUse python for the parsing since jq may struggle with nested JSON strings.",
    "agentId": "aa0dedafabeeb8ab6",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is the complete analysis of all 4B-related experiments from the registry.\n\n---\n\n## Summary\n\n**133 total experiments** matched the filter criteria (all referencing Qwen3-4B in their spec). Status breakdown: 131 DONE, 1 RUNNING (`grpo_bf16_g4_ckpt200_eval`), 1 ANALYZING (`wave1_sft_4b_s44_eval_r2`). Conclusion breakdown: 57 success, 29 failed, 27 killed, 18 negative, 2 pending.\n\n**49 experiments** had quantitative metrics (ign_f1 or rel_f1).\n\n---\n\n## Explicitly 4B-named experiments (wave1_sft_4b_*)\n\n### Training\n| exp_id | status | conclusion | seed | train_loss | eval_loss |\n|--------|--------|------------|------|------------|-----------|\n| `wave1_sft_4b_s43` | DONE | success | 43 | 0.7011 | 0.7482 |\n| `wave1_sft_4b_s44` | DONE | success | 44 | 0.7008 | 0.7478 |\n\n### Eval\n| exp_id | status | conclusion | ign_f1 | rel_f1 | evi_f1 | edcr | evi_f1_joint |\n|--------|--------|------------|--------|--------|--------|------|--------------|\n| `wave1_sft_4b_s43_eval` | DONE | **failed** | -- | -- | -- | -- | -- |\n| `wave1_sft_4b_s43_eval_r2` | DONE | success | **0.4365** | 0.4429 | 0.8021 | 0.6827 | 0.3462 |\n| `wave1_sft_4b_s44_eval` | DONE | **failed** | -- | -- | -- | -- | -- |\n| `wave1_sft_4b_s44_eval_r2` | **ANALYZING** | pending | -- | -- | -- | -- | -- |\n\nBoth initial eval attempts (`wave1_sft_4b_s43_eval`, `wave1_sft_4b_s44_eval`) failed due to `inference.py adapter validation bug: detects LoRA adapter_config.json and requires --sft_adapter`. The r2 fixes used `--model_path=base_model --sft_adapter=adapter_path` instead.\n\nKey commands:\n- **s43_eval (failed)**: `python -m freige.eval.inference --model_path /root/autodl-tmp/sft_output_seed43/ --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/sft_4b_s43_eval`\n- **s43_eval_r2 (success)**: `python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output_seed43/ --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/wave1_sft_4b_s43_eval_r2`\n- **s44_eval_r2 (running)**: `CUDA_VISIBLE_DEVICES=1 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output_seed44/ --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/wave1_sft_4b_s44_eval_r2`\n\n---\n\n## Re-DocRED 4B eval (`plan_007_redocred_4b_sft_eval*`)\n\n| exp_id | conclusion | ign_f1 | f1 | evi_f1 | edcr |\n|--------|------------|--------|-----|--------|------|\n| `plan_007_redocred_4b_sft_eval` | failed | -- | -- | -- | -- |\n| `plan_007_redocred_4b_sft_eval_r2` | success | **0.3659** | 0.3706 | 0.817 | 0.6674 |\n\nCommand for r2: `CUDA_VISIBLE_DEVICES=0 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/re-docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/plan_007_redocred_4b_sft_eval`\n\nRe-DocRED RSFT eval (`plan_007_redocred_rsft_eval_r5`): ign_f1=**0.4145**, f1=0.4234, evi_f1=0.8182, edcr=0.621 (improvement of +4.86pp over SFT baseline on Re-DocRED).\n\n---\n\n## Top eval results leaderboard (ign_f1, all successful/valid experiments)\n\n| Rank | exp_id | Model | seed | ign_f1 | rel_f1 | evi_f1 | edcr | evi_f1_joint |\n|------|--------|-------|------|--------|--------|--------|------|--------------|\n| 1 | `eval_plan_014_no_evidence_r2` | Qwen3-4B no-evidence SFT | 42 | **0.4721** | 0.4876 | 0 | 0 | 0 |\n| 2 | `mvp2_eval_rsft_s43_r2` | SFT+RSFT s43 | 42 | **0.4683** | 0.4683 | 0.8156 | 0.6388 | 0.3711 |\n| 3 | `plan_011_grpo_g8_bf16_eval` | SFT+GRPO-G8-bf16 | 42 | **0.4549** | 0.4549 | 0.8086 | 0.6318 | -- |\n| 4 | `eval_plan_001_flat_nli` | SFT+RSFT-flat-NLI | 42 | **0.4539** | 0.4539 | 0.8043 | 0.6431 | -- |\n| 5 | `lead2_ckpt20_eval` | SFT+RSFT merged+GRPO ckpt-20 | 42 | **0.4533** | 0.4617 | 0.8103 | 0.6465 | 0.3642 |\n| 6 | `reeval_flat_nli_s43` | SFT+flat-NLI RSFT s43 | 43 | **0.4523** | 0.4523 | 0.8158 | 0.6505 | -- |\n| 7 | `eval_flat_nli_s44` | SFT+RSFT flat-NLI s44 | 44 | **0.4521** | 0.4615 | 0.8131 | 0.6458 | 0.3597 |\n| 8 | `eval_rsft_ced_s43` | SFT+RSFT CED s43 | 43 | **0.4512** | 0.4601 | 0.8063 | 0.6542 | 0.3605 |\n| 9 | `reeval_ced_s44` | SFT+RSFT CED s44 | 44 | **0.4511** | 0.4621 | 0.805 | 0.635 | 0.3677 |\n| 10 | `reeval_flat_nli_s43_r2` | SFT+flat-NLI RSFT s43 | 43 | **0.4503** | 0.4586 | 0.8113 | 0.6552 | 0.358 |\n\n---\n\n## Currently active experiments\n\n1. **`grpo_bf16_g4_ckpt200_eval`** (RUNNING): evaluating GRPO bf16 G4 checkpoint-200 on DocRED dev\n2. **`wave1_sft_4b_s44_eval_r2`** (ANALYZING): SFT seed=44 eval, inference likely complete but metrics not yet extracted\n\n---\n\n## Notable bugs found in eval configurations\n\n1. **Missing `--sft_adapter` bug**: `eval_plan_001_flat_nli_s43`, `eval_plan_008_rsft_topk3`, `eval_plan_012_dpo_ced_1ep` all produced garbage metrics (ign_f1 near 0.002) because `--sft_adapter` was omitted. These were later re-run with the fix.\n\n2. **Adapter path ordering bug**: `plan_007_redocred_rsft_eval` through `r4` failed because `--model_path` and `--sft_adapter` args were in wrong order (RSFT LoRA merged to bare Qwen3-4B without SFT base). Fixed in `r5` with correct 3-param ordering: `--model_path RSFT_ckpt --base_model Qwen3-4B --sft_adapter sft_output`.\n\n3. **wave1_sft_4b eval bug**: Initial `wave1_sft_4b_s43_eval` and `wave1_sft_4b_s44_eval` failed because `inference.py` detected LoRA `adapter_config.json` inside `--model_path` and required `--sft_adapter`. Fix: swap to `--model_path=base_model --sft_adapter=adapter_path`."
      }
    ],
    "totalDurationMs": 154480,
    "totalTokens": 123296,
    "totalToolUseCount": 20,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6247,
      "cache_read_input_tokens": 114370,
      "output_tokens": 2678,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6247
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2678,
          "cache_read_input_tokens": 114370,
          "cache_creation_input_tokens": 6247,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6247,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 12,
      "searchCount": 0,
      "bashCount": 8,
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

_source line 77_

<details><summary>Logged reasoning block</summary>

```text
Good, I have a comprehensive overview. Now let me get the specific eval commands for ALL 4B eval experiments to do the D076 audit. Let me extract the detailed commands for each eval experiment. I need to specifically check:

1. All SFT eval experiments (s42, s43, s44)
2. All RSFT eval experiments (CED k=1 for various seeds)
3. Any other 4B eval

Let me use a more targeted approach to get the full commands for each eval experiment.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "9f262177-077a-41b8-9dd4-ad85cea87086",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01An1S1C9fr7xDWY1VmWbs1U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3292,
      "cache_read_input_tokens": 26804,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3292
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

已有概览。现在需要提取所有 4B eval 实验的完整命令来逐一审计 D076 合规性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "f4e38f86-4d0b-4bc2-8629-d77de3f4e30d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01An1S1C9fr7xDWY1VmWbs1U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3292,
      "cache_read_input_tokens": 26804,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3292
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

<details open><summary>🔧 Tool call — Agent · `toolu_01TeEH97guEfBfH5188hkZEb`</summary>

```json
{
  "description": "Extract all 4B eval commands for D076 audit",
  "prompt": "I need you to extract the FULL eval command for every 4B eval experiment from the registry file.\n\nThe file is at: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/596d8411-63f5-4757-a2a4-2c57b1fcaba0/tool-results/mcp-agent-ml-research-read_registry-1779141732674.txt\n\nIt's JSON with schema: {result: string} where result is a JSON string containing an array of experiment objects.\n\nUse Python to parse and extract. For EVERY experiment that:\n1. References Qwen3-4B in its spec\n2. AND is an \"eval\" experiment (exp_id contains \"eval\" or the experiment type/purpose is evaluation)\n\nExtract and print:\n- exp_id\n- status\n- conclusion\n- metrics (especially ign_f1)\n- The FULL spec.command string (do NOT truncate)\n- notes/error if any\n\nI need to check D076 protocol compliance for each eval:\n- batch_size=4\n- max_new_tokens=1024\n- seed=42\n- --no-quantize present\n- --model_path points to base model (Qwen3-4B)\n- --sft_adapter points to adapter\n\nFor each eval, parse the command and check each D076 parameter. Output a table with columns:\nexp_id | ign_f1 | batch_size | max_new_tokens | seed | no_quantize | model_path | sft_adapter | D076_compliant | non_compliance_reasons\n\nBe exhaustive - include ALL eval experiments, even failed ones. Include the full command string for each.\n\nAlso specifically look for:\n- Any eval that uses --model_path pointing to an adapter directory instead of base model\n- Any eval missing --no-quantize\n- Any eval with different batch_size or max_new_tokens\n- Any eval for SFT s42 (the original seed) - what adapter path does it use?\n\nWrite a Python script to do this analysis and run it."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "2c6789ec-bf2e-49b1-b45f-fb5d741d4aa9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01An1S1C9fr7xDWY1VmWbs1U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3292,
      "cache_read_input_tokens": 26804,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3292
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

_source line 80_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a35180a8a436e895f",
  "tool_use_id": "toolu_01TeEH97guEfBfH5188hkZEb",
  "description": "Extract all 4B eval commands for D076 audit",
  "task_type": "local_agent",
  "prompt": "I need you to extract the FULL eval command for every 4B eval experiment from the registry file.\n\nThe file is at: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/596d8411-63f5-4757-a2a4-2c57b1fcaba0/tool-results/mcp-agent-ml-research-read_registry-1779141732674.txt\n\nIt's JSON with schema: {result: string} where result is a JSON string containing an array of experiment objects.\n\nUse Python to parse and extract. For EVERY experiment that:\n1. References Qwen3-4B in its spec\n2. AND is an \"eval\" experiment (exp_id contains \"eval\" or the experiment type/purpose is evaluation)\n\nExtract and print:\n- exp_id\n- status\n- conclusion\n- metrics (especially ign_f1)\n- The FULL spec.command string (do NOT truncate)\n- notes/error if any\n\nI need to check D076 protocol compliance for each eval:\n- batch_size=4\n- max_new_tokens=1024\n- seed=42\n- --no-quantize present\n- --model_path points to base model (Qwen3-4B)\n- --sft_adapter points to adapter\n\nFor each eval, parse the command and check each D076 parameter. Output a table with columns:\nexp_id | ign_f1 | batch_size | max_new_tokens | seed | no_quantize | model_path | sft_adapter | D076_compliant | non_compliance_reasons\n\nBe exhaustive - include ALL eval experiments, even failed ones. Include the full command string for each.\n\nAlso specifically look for:\n- Any eval that uses --model_path pointing to an adapter directory instead of base model\n- Any eval missing --no-quantize\n- Any eval with different batch_size or max_new_tokens\n- Any eval for SFT s42 (the original seed) - what adapter path does it use?\n\nWrite a Python script to do this analysis and run it.",
  "uuid": "2992f850-de30-48d7-bb62-35a1293ca648",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0"
}
```

---


## Round 2

## Round 2

121 recorded events


### User

_source line 81 · 2026-05-18T22:05:12.792Z_

I need you to extract the FULL eval command for every 4B eval experiment from the registry file.

The file is at: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/596d8411-63f5-4757-a2a4-2c57b1fcaba0/tool-results/mcp-agent-ml-research-read_registry-1779141732674.txt

It's JSON with schema: {result: string} where result is a JSON string containing an array of experiment objects.

Use Python to parse and extract. For EVERY experiment that:
1. References Qwen3-4B in its spec
2. AND is an "eval" experiment (exp_id contains "eval" or the experiment type/purpose is evaluation)

Extract and print:
- exp_id
- status
- conclusion
- metrics (especially ign_f1)
- The FULL spec.command string (do NOT truncate)
- notes/error if any

I need to check D076 protocol compliance for each eval:
- batch_size=4
- max_new_tokens=1024
- seed=42
- --no-quantize present
- --model_path points to base model (Qwen3-4B)
- --sft_adapter points to adapter

For each eval, parse the command and check each D076 parameter. Output a table with columns:
exp_id | ign_f1 | batch_size | max_new_tokens | seed | no_quantize | model_path | sft_adapter | D076_compliant | non_compliance_reasons

Be exhaustive - include ALL eval experiments, even failed ones. Include the full command string for each.

Also specifically look for:
- Any eval that uses --model_path pointing to an adapter directory instead of base model
- Any eval missing --no-quantize
- Any eval with different batch_size or max_new_tokens
- Any eval for SFT s42 (the original seed) - what adapter path does it use?

Write a Python script to do this analysis and run it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01TeEH97guEfBfH5188hkZEb",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "30534343-ad0c-4659-a8ea-3fea992379ba"
}
```

</details>

---


### System

_source line 82_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a35180a8a436e895f",
  "tool_use_id": "toolu_01TeEH97guEfBfH5188hkZEb",
  "description": "Reading ~/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/596d8411-63f5-4757-a2a4-2c57b1fcaba0/tool-results/mcp-agent-ml-research-read_registry-1779141732674.txt",
  "usage": {
    "total_tokens": 16149,
    "tool_uses": 1,
    "duration_ms": 3896
  },
  "last_tool_name": "Read",
  "uuid": "787d0e78-ff4a-4a8d-afa8-26449da199e9",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0"
}
```

---


### Tool call

_source line 83_

<details open><summary>🔧 Tool call — Read · `toolu_019myGo3GDdxEvUCPQieS48V`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/596d8411-63f5-4757-a2a4-2c57b1fcaba0/tool-results/mcp-agent-ml-research-read_registry-1779141732674.txt",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01TeEH97guEfBfH5188hkZEb",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "469ce32a-047b-4d32-be9d-176e1c9303d5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017QN46myk35YftPfosyCgjr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7889,
      "cache_read_input_tokens": 8249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7889,
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

_source line 84 · 2026-05-18T22:05:16.968Z_

<details><summary>↩ Tool result · reported error · `toolu_019myGo3GDdxEvUCPQieS48V`</summary>

```text
File content (177098 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01TeEH97guEfBfH5188hkZEb",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "d54d8da2-9406-4c42-8cd4-ddeea24b6186",
  "tool_use_result": "Error: File content (177098 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---


### System

_source line 85_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a35180a8a436e895f",
  "tool_use_id": "toolu_01TeEH97guEfBfH5188hkZEb",
  "description": "Reading ~/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/596d8411-63f5-4757-a2a4-2c57b1fcaba0/tool-results/mcp-agent-ml-research-read_registry-1779141732674.txt",
  "usage": {
    "total_tokens": 17235,
    "tool_uses": 2,
    "duration_ms": 7503
  },
  "last_tool_name": "Read",
  "uuid": "b2475837-bf8c-4b72-a2ec-9f46f70e6e4c",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0"
}
```

---


### Tool call

_source line 86_

<details open><summary>🔧 Tool call — Read · `toolu_01Fc5bzeeigDrs9XGsgqDERi`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/596d8411-63f5-4757-a2a4-2c57b1fcaba0/tool-results/mcp-agent-ml-research-read_registry-1779141732674.txt",
  "limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01TeEH97guEfBfH5188hkZEb",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "12d082a4-d783-4d4a-a4c8-9adef49f16d3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017bsBD9Yia5W4DVhmRVzfhc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1086,
      "cache_read_input_tokens": 16138,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1086,
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

_source line 87 · 2026-05-18T22:05:20.741Z_

<details><summary>↩ Tool result · reported error · `toolu_01Fc5bzeeigDrs9XGsgqDERi`</summary>

```text
File content (177098 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01TeEH97guEfBfH5188hkZEb",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "ecde8619-d5d3-40a9-b35f-0735c6f7ed54",
  "tool_use_result": "Error: File content (177098 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---


### System

_source line 88_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a35180a8a436e895f",
  "tool_use_id": "toolu_01TeEH97guEfBfH5188hkZEb",
  "description": "Running Count lines in registry file",
  "usage": {
    "total_tokens": 17534,
    "tool_uses": 3,
    "duration_ms": 11194
  },
  "last_tool_name": "Bash",
  "uuid": "fd508b35-0526-4d11-80f3-c07910c15d64",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0"
}
```

---


### Tool call

_source line 89_

<details open><summary>🔧 Tool call — Bash · `toolu_01GEXh7N9FbLoxKCDhGzEa2P`</summary>

```json
{
  "command": "wc -l \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/596d8411-63f5-4757-a2a4-2c57b1fcaba0/tool-results/mcp-agent-ml-research-read_registry-1779141732674.txt\"",
  "description": "Count lines in registry file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01TeEH97guEfBfH5188hkZEb",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "e72e289e-a044-4f26-b77b-7f4828513fe3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HY1SvYSgvY3bbBKJXRD9GM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 241,
      "cache_read_input_tokens": 17224,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 241,
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

_source line 90 · 2026-05-18T22:05:24.108Z_

<details><summary>↩ Tool result · `toolu_01GEXh7N9FbLoxKCDhGzEa2P`</summary>

```text
0 /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/596d8411-63f5-4757-a2a4-2c57b1fcaba0/tool-results/mcp-agent-ml-research-read_registry-1779141732674.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01TeEH97guEfBfH5188hkZEb",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "ef8efb58-f8b0-4f66-91da-9fe07bfdf6df"
}
```

</details>

---


### System

_source line 91_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a35180a8a436e895f",
  "tool_use_id": "toolu_01TeEH97guEfBfH5188hkZEb",
  "description": "Running Parse registry JSON structure",
  "usage": {
    "total_tokens": 17807,
    "tool_uses": 4,
    "duration_ms": 18462
  },
  "last_tool_name": "Bash",
  "uuid": "fa6424e5-73da-46f6-8738-64a13947fcfa",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0"
}
```

---


### Tool call

_source line 92_

<details open><summary>🔧 Tool call — Bash · `toolu_01Gbdrd988GgTGGgbNnXYd3H`</summary>

```json
{
  "command": "python3 -c \"\nimport json, sys\n\nfpath = '/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/596d8411-63f5-4757-a2a4-2c57b1fcaba0/tool-results/mcp-agent-ml-research-read_registry-1779141732674.txt'\n\nwith open(fpath, 'r') as f:\n    raw = json.load(f)\n\n# The outer structure is {result: string}\nresult_str = raw.get('result', raw)\nif isinstance(result_str, str):\n    data = json.loads(result_str)\nelse:\n    data = result_str\n\nprint(f'Type of data: {type(data)}')\nif isinstance(data, list):\n    print(f'Number of experiments: {len(data)}')\n    if data:\n        print(f'Keys in first entry: {list(data[0].keys())}')\nelif isinstance(data, dict):\n    print(f'Top-level keys: {list(data.keys())}')\n    for k,v in data.items():\n        if isinstance(v, list):\n            print(f'  {k}: list of {len(v)} items')\n            if v:\n                print(f'  Keys in first item: {list(v[0].keys())}')\n\"\n",
  "description": "Parse registry JSON structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01TeEH97guEfBfH5188hkZEb",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "0048e621-4e3f-445c-9983-59bd358a5a36",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B8wmmYPSppp7PNiLsRkz67",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 271,
      "cache_read_input_tokens": 17465,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 271,
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

_source line 93 · 2026-05-18T22:05:31.359Z_

<details><summary>↩ Tool result · `toolu_01Gbdrd988GgTGGgbNnXYd3H`</summary>

```text
Type of data: &lt;class 'dict'>
Top-level keys: ['success', 'data', 'error', 'metadata']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01TeEH97guEfBfH5188hkZEb",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "3a6b3b02-850e-409b-9a38-43eb2edc210e"
}
```

</details>

---


### System

_source line 94_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a35180a8a436e895f",
  "tool_use_id": "toolu_01TeEH97guEfBfH5188hkZEb",
  "description": "Running Explore nested data structure",
  "usage": {
    "total_tokens": 18363,
    "tool_uses": 5,
    "duration_ms": 24746
  },
  "last_tool_name": "Bash",
  "uuid": "08a0ecbb-908a-46a8-b4b5-3a17f6c12cce",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0"
}
```

---


### Tool call

_source line 95_

<details open><summary>🔧 Tool call — Bash · `toolu_01MuBrtQeLLV6QcVespKfZwb`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nfpath = '/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/596d8411-63f5-4757-a2a4-2c57b1fcaba0/tool-results/mcp-agent-ml-research-read_registry-1779141732674.txt'\n\nwith open(fpath, 'r') as f:\n    raw = json.load(f)\n\nresult_str = raw.get('result', raw)\nif isinstance(result_str, str):\n    data = json.loads(result_str)\nelse:\n    data = result_str\n\nexperiments = data.get('data', data)\nif isinstance(experiments, dict):\n    # Maybe experiments is under another key\n    for k, v in experiments.items():\n        print(f'{k}: {type(v)}')\n        if isinstance(v, list):\n            print(f'  len={len(v)}')\n            if v:\n                print(f'  first item keys: {list(v[0].keys()) if isinstance(v[0], dict) else type(v[0])}')\n        elif isinstance(v, dict):\n            print(f'  keys: {list(v.keys())[:10]}')\n        else:\n            print(f'  value: {str(v)[:200]}')\n\"\n",
  "description": "Explore nested data structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01TeEH97guEfBfH5188hkZEb",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "d92ebc98-1b76-4f52-9e0e-f24bb16f9bc0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E6HPeZzqT2SbXe9VSExP5D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 485,
      "cache_read_input_tokens": 17736,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 485,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 71,
      "service_tier": "standard",
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

_source line 96 · 2026-05-18T22:05:37.644Z_

<details><summary>↩ Tool result · `toolu_01MuBrtQeLLV6QcVespKfZwb`</summary>

```text
experiments: &lt;class 'dict'>
  keys: ['wave1_sft_4b_s44_eval_r2', 'plan019_8b_sft_s44_eval', 'wave1_sft_4b_s43_eval_r2', 'plan019_1_7b_sft_s43_eval', 'plan019_8b_sft_s44', 'plan019_1_7b_sft_s43_r2', 'grpo_bf16_g4_ckpt200_eval', 'wave1_grpo_bf16_g4', 'random_rsft_k1_eval', 'grpo_bf16_g4_ckpt100_eval']
count: &lt;class 'int'>
  value: 222
total: &lt;class 'int'>
  value: 222
baseline: &lt;class 'NoneType'>
  value: None
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01TeEH97guEfBfH5188hkZEb",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "028f6977-aec5-4c7d-bed2-63643ef0baef"
}
```

</details>

---


### System

_source line 97_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a35180a8a436e895f",
  "tool_use_id": "toolu_01TeEH97guEfBfH5188hkZEb",
  "description": "Running Examine single experiment structure",
  "usage": {
    "total_tokens": 19090,
    "tool_uses": 6,
    "duration_ms": 29816
  },
  "last_tool_name": "Bash",
  "uuid": "3bea7a9f-f3b5-4d59-9d27-9f3b9cc28abf",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0"
}
```

---


### Tool call

_source line 98_

<details open><summary>🔧 Tool call — Bash · `toolu_01QBvVMyarzFmXbJcbJhgAoy`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nfpath = '/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/596d8411-63f5-4757-a2a4-2c57b1fcaba0/tool-results/mcp-agent-ml-research-read_registry-1779141732674.txt'\n\nwith open(fpath, 'r') as f:\n    raw = json.load(f)\n\nresult_str = raw.get('result', raw)\nif isinstance(result_str, str):\n    data = json.loads(result_str)\nelse:\n    data = result_str\n\nexperiments = data['data']['experiments']\n\n# Look at one experiment to see its structure\nfirst_key = list(experiments.keys())[0]\nexp = experiments[first_key]\nprint(f'Experiment: {first_key}')\nprint(f'Keys: {list(exp.keys())}')\nprint(json.dumps(exp, indent=2)[:3000])\n\"\n",
  "description": "Examine single experiment structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01TeEH97guEfBfH5188hkZEb",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "ded5c957-aef1-49b5-b5c6-31d7e24971f0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E9mdhW4Hz2fdEUoD9nHhj1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 654,
      "cache_read_input_tokens": 18221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 654,
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

_source line 99 · 2026-05-18T22:05:42.734Z_

<details><summary>↩ Tool result · `toolu_01QBvVMyarzFmXbJcbJhgAoy`</summary>

```text
Experiment: wave1_sft_4b_s44_eval_r2
Keys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'spec', 'reproduce', 'extra']
{
  "status": "ANALYZING",
  "retry_count": 0,
  "created_at": "2026-05-18T20:05:57.119Z",
  "updated_at": "2026-05-18T21:59:29.645Z",
  "hypothesis": "4B SFT seed44 eval r2 (corrected D076 command: --model_path=base --sft_adapter=adapter). Re-run of failed wave1_sft_4b_s44_eval. Expected rel_f1 ~50.5 based on canonical 4B SFT s42.",
  "parent": "wave1_sft_4b_s44",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=1 python -m freige.eval.inference --model_path /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output_seed44/ --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 42 --no-quantize --output_dir /root/autodl-tmp/eval_results/wave1_sft_4b_s44_eval_r2\"",
    "server": "rtx5090-4x",
    "gpu": [
      "cuda:1"
    ],
    "pid": "571192",
    "log_path": "~/runs/faith-evidence-ie/wave1_sft_4b_s44_eval_r2.log",
    "submitted_at": "2026-05-18T20:06:13.257Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "/root/autodl-tmp/data/docred",
    "data_count": 985,
    "model_name": "Qwen3-4B + SFT-s44",
    "seed": 42,
    "checkpoint_source": "wave1_sft_4b_s44",
    "eval_data": "DocRED dev",
    "checkpoint_path": "/root/autodl-tmp/eval_results/wave1_sft_4b_s44_eval_r2"
  },
  "reproduce": {
    "finished_at": "2026-05-18T21:59:27.684Z"
  },
  "extra": {
    "hook_events": [
      {
        "event": "on_complete",
        "action": "agent",
        "ts": "2026-05-18T21:59:33.106103+00:00"
      }
    ]
  }
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01TeEH97guEfBfH5188hkZEb",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "4e430f4d-38df-4ecf-b9f6-9ec22b31d049"
}
```

</details>

---


### System

_source line 100_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a35180a8a436e895f",
  "tool_use_id": "toolu_01TeEH97guEfBfH5188hkZEb",
  "description": "Writing artifacts/d076_eval_audit.py",
  "usage": {
    "total_tokens": 20230,
    "tool_uses": 7,
    "duration_ms": 87038
  },
  "last_tool_name": "Write",
  "uuid": "5c2f0dfc-9c81-4e6e-b4d4-9e64950f5120",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0"
}
```

---


### Tool call

_source line 101_

<details open><summary>🔧 Tool call — Write · `toolu_015awc5JNyFhDZQXUx7fqLb7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/d076_eval_audit.py",
  "content": "#!/usr/bin/env python3\n\"\"\"D076 Protocol Compliance Audit for all 4B eval experiments.\"\"\"\n\nimport json\nimport re\nimport sys\n\nfpath = '/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/596d8411-63f5-4757-a2a4-2c57b1fcaba0/tool-results/mcp-agent-ml-research-read_registry-1779141732674.txt'\n\nwith open(fpath, 'r') as f:\n    raw = json.load(f)\n\nresult_str = raw.get('result', raw)\nif isinstance(result_str, str):\n    data = json.loads(result_str)\nelse:\n    data = result_str\n\nexperiments = data['data']['experiments']\n\n# Collect all 4B eval experiments\neval_exps = []\nfor exp_id, exp in experiments.items():\n    # Check if it references Qwen3-4B (in spec command, hypothesis, model_name, or exp_id)\n    is_4b = False\n    cmd = exp.get('spec', {}).get('command', '')\n    hypothesis = exp.get('hypothesis', '')\n    model_name = exp.get('spec', {}).get('model_name', '')\n\n    checks = [cmd, hypothesis, model_name, exp_id]\n    for c in checks:\n        if c and ('4b' in c.lower() or '4B' in c or 'Qwen3-4B' in c):\n            is_4b = True\n            break\n\n    if not is_4b:\n        continue\n\n    # Check if it's an eval experiment\n    is_eval = False\n    if 'eval' in exp_id.lower():\n        is_eval = True\n    if 'eval' in cmd.lower() and ('inference' in cmd.lower() or 'eval' in cmd.lower()):\n        is_eval = True\n    if 'eval' in hypothesis.lower():\n        is_eval = True\n\n    if not is_eval:\n        continue\n\n    eval_exps.append((exp_id, exp))\n\nprint(f\"=\" * 120)\nprint(f\"D076 PROTOCOL COMPLIANCE AUDIT - All Qwen3-4B Eval Experiments\")\nprint(f\"Total experiments in registry: {len(experiments)}\")\nprint(f\"4B eval experiments found: {len(eval_exps)}\")\nprint(f\"=\" * 120)\n\n# D076 expected values\nD076 = {\n    'batch_size': '4',\n    'max_new_tokens': '1024',\n    'seed': '42',\n    'no_quantize': True,\n    'model_path_is_base': True,  # should point to base model, not adapter\n    'sft_adapter_present': True,\n}\n\ndef parse_command(cmd):\n    \"\"\"Parse command string to extract D076-relevant parameters.\"\"\"\n    result = {\n        'batch_size': None,\n        'max_new_tokens': None,\n        'seed': None,\n        'no_quantize': False,\n        'model_path': None,\n        'sft_adapter': None,\n    }\n\n    if not cmd:\n        return result\n\n    # batch_size\n    m = re.search(r'--batch_size\\s+(\\S+)', cmd)\n    if m:\n        result['batch_size'] = m.group(1)\n\n    # max_new_tokens\n    m = re.search(r'--max_new_tokens\\s+(\\S+)', cmd)\n    if m:\n        result['max_new_tokens'] = m.group(1)\n\n    # seed\n    m = re.search(r'--seed\\s+(\\S+)', cmd)\n    if m:\n        result['seed'] = m.group(1)\n\n    # no-quantize\n    if '--no-quantize' in cmd or '--no_quantize' in cmd:\n        result['no_quantize'] = True\n\n    # model_path\n    m = re.search(r'--model_path\\s+(\\S+)', cmd)\n    if m:\n        result['model_path'] = m.group(1)\n\n    # sft_adapter\n    m = re.search(r'--sft_adapter\\s+(\\S+)', cmd)\n    if m:\n        result['sft_adapter'] = m.group(1)\n\n    return result\n\ndef check_model_path_is_base(model_path):\n    \"\"\"Check if model_path points to base model (not adapter directory).\"\"\"\n    if not model_path:\n        return False, \"missing\"\n    # Base model patterns\n    base_patterns = ['Qwen3-4B', 'models/Qwen', 'Qwen/Qwen']\n    # Adapter/SFT output patterns (non-compliant)\n    adapter_patterns = ['sft_output', 'adapter', 'checkpoint', 'lora', 'grpo_output', 'rsft_output']\n\n    is_base = any(p in model_path for p in base_patterns)\n    is_adapter = any(p in model_path for p in adapter_patterns)\n\n    if is_adapter:\n        return False, f\"points to adapter dir: {model_path}\"\n    if is_base:\n        return True, \"OK\"\n    return False, f\"unknown path: {model_path}\"\n\ndef check_d076(parsed):\n    \"\"\"Check D076 compliance and return (compliant, reasons).\"\"\"\n    reasons = []\n\n    if parsed['batch_size'] != '4':\n        reasons.append(f\"batch_size={parsed['batch_size']} (expected 4)\")\n    if parsed['max_new_tokens'] != '1024':\n        reasons.append(f\"max_new_tokens={parsed['max_new_tokens']} (expected 1024)\")\n    if parsed['seed'] != '42':\n        reasons.append(f\"seed={parsed['seed']} (expected 42)\")\n    if not parsed['no_quantize']:\n        reasons.append(\"--no-quantize MISSING\")\n\n    base_ok, base_msg = check_model_path_is_base(parsed['model_path'])\n    if not base_ok:\n        reasons.append(f\"model_path: {base_msg}\")\n\n    if not parsed['sft_adapter']:\n        reasons.append(\"--sft_adapter MISSING\")\n\n    compliant = len(reasons) == 0\n    return compliant, reasons\n\n# Sort by exp_id\neval_exps.sort(key=lambda x: x[0])\n\n# Print detailed info for each experiment\nprint()\nfor i, (exp_id, exp) in enumerate(eval_exps):\n    cmd = exp.get('spec', {}).get('command', '')\n    status = exp.get('status', 'UNKNOWN')\n    hypothesis = exp.get('hypothesis', '')\n    metrics = exp.get('spec', {}).get('metrics', exp.get('reproduce', {}).get('metrics', {}))\n    # Also check for metrics in other locations\n    if not metrics:\n        for key in ['results', 'metrics']:\n            if key in exp:\n                metrics = exp[key]\n                break\n    # Check extra for metrics\n    if not metrics and 'extra' in exp:\n        extra = exp['extra']\n        if isinstance(extra, dict):\n            for key in ['metrics', 'results', 'eval_metrics']:\n                if key in extra:\n                    metrics = extra[key]\n                    break\n\n    # Get conclusion and notes\n    conclusion = exp.get('reproduce', {}).get('conclusion', '')\n    if not conclusion:\n        conclusion = exp.get('extra', {}).get('conclusion', '')\n    notes = exp.get('reproduce', {}).get('notes', '')\n    if not notes:\n        notes = exp.get('extra', {}).get('notes', '')\n    error = exp.get('reproduce', {}).get('error', '')\n    if not error:\n        error = exp.get('extra', {}).get('error', '')\n\n    parsed = parse_command(cmd)\n    compliant, reasons = check_d076(parsed)\n\n    print(f\"\\n{'─' * 120}\")\n    print(f\"[{i+1}/{len(eval_exps)}] exp_id: {exp_id}\")\n    print(f\"  status:     {status}\")\n    print(f\"  hypothesis: {hypothesis[:200]}\")\n    print(f\"  parent:     {exp.get('parent', 'N/A')}\")\n    print(f\"  model_name: {exp.get('spec', {}).get('model_name', 'N/A')}\")\n    print()\n    print(f\"  FULL COMMAND:\")\n    print(f\"    {cmd}\")\n    print()\n    print(f\"  PARSED D076 PARAMS:\")\n    print(f\"    batch_size:     {parsed['batch_size']}\")\n    print(f\"    max_new_tokens: {parsed['max_new_tokens']}\")\n    print(f\"    seed:           {parsed['seed']}\")\n    print(f\"    no_quantize:    {parsed['no_quantize']}\")\n    print(f\"    model_path:     {parsed['model_path']}\")\n    print(f\"    sft_adapter:    {parsed['sft_adapter']}\")\n    print()\n    print(f\"  D076 COMPLIANT:   {'YES' if compliant else 'NO'}\")\n    if reasons:\n        print(f\"  NON-COMPLIANCE:   {'; '.join(reasons)}\")\n    print()\n\n    # Print all extra fields that might contain metrics/conclusion\n    print(f\"  metrics:    {json.dumps(metrics, indent=4) if metrics else 'N/A'}\")\n    print(f\"  conclusion: {conclusion if conclusion else 'N/A'}\")\n    print(f\"  notes:      {notes if notes else 'N/A'}\")\n    print(f\"  error:      {error if error else 'N/A'}\")\n\n    # Dump all keys in reproduce and extra for completeness\n    reproduce = exp.get('reproduce', {})\n    if reproduce:\n        extra_keys = [k for k in reproduce.keys() if k not in ('finished_at', 'conclusion', 'notes', 'error', 'metrics')]\n        if extra_keys:\n            print(f\"  reproduce extra keys: {extra_keys}\")\n            for k in extra_keys:\n                v = reproduce[k]\n                v_str = json.dumps(v) if isinstance(v, (dict, list)) else str(v)\n                if len(v_str) > 500:\n                    v_str = v_str[:500] + '...'\n                print(f\"    reproduce.{k}: {v_str}\")\n\n    extra = exp.get('extra', {})\n    if extra:\n        extra_keys = [k for k in extra.keys() if k not in ('hook_events', 'conclusion', 'notes', 'error', 'metrics')]\n        if extra_keys:\n            print(f\"  extra keys: {extra_keys}\")\n            for k in extra_keys:\n                v = extra[k]\n                v_str = json.dumps(v) if isinstance(v, (dict, list)) else str(v)\n                if len(v_str) > 500:\n                    v_str = v_str[:500] + '...'\n                print(f\"    extra.{k}: {v_str}\")\n\n# Now print summary table\nprint(f\"\\n\\n{'=' * 200}\")\nprint(\"SUMMARY TABLE\")\nprint(f\"{'=' * 200}\")\n\nheader = f\"{'exp_id':<45} | {'status':<12} | {'ign_f1':<8} | {'bs':<4} | {'max_tok':<8} | {'seed':<5} | {'no_q':<5} | {'model_path':<55} | {'sft_adapter':<55} | {'D076':<5} | non_compliance\"\nprint(header)\nprint(\"─\" * len(header))\n\nfor exp_id, exp in eval_exps:\n    cmd = exp.get('spec', {}).get('command', '')\n    status = exp.get('status', '?')\n    parsed = parse_command(cmd)\n    compliant, reasons = check_d076(parsed)\n\n    # Try to find ign_f1\n    ign_f1 = 'N/A'\n    for loc in [exp.get('reproduce', {}), exp.get('extra', {}), exp.get('spec', {})]:\n        if isinstance(loc, dict):\n            if 'metrics' in loc and isinstance(loc['metrics'], dict):\n                if 'ign_f1' in loc['metrics']:\n                    ign_f1 = str(loc['metrics']['ign_f1'])\n                    break\n            if 'ign_f1' in loc:\n                ign_f1 = str(loc['ign_f1'])\n                break\n    # Also check nested results\n    for loc in [exp.get('reproduce', {}), exp.get('extra', {})]:\n        if isinstance(loc, dict):\n            for k, v in loc.items():\n                if isinstance(v, dict) and 'ign_f1' in v:\n                    ign_f1 = str(v['ign_f1'])\n                    break\n\n    mp = parsed['model_path'] or 'MISSING'\n    sa = parsed['sft_adapter'] or 'MISSING'\n    # Shorten paths for table\n    mp_short = mp[-55:] if len(mp) > 55 else mp\n    sa_short = sa[-55:] if len(sa) > 55 else sa\n\n    row = f\"{exp_id:<45} | {status:<12} | {ign_f1:<8} | {parsed['batch_size'] or '?':<4} | {parsed['max_new_tokens'] or '?':<8} | {parsed['seed'] or '?':<5} | {'Y' if parsed['no_quantize'] else 'N':<5} | {mp_short:<55} | {sa_short:<55} | {'YES' if compliant else 'NO':<5} | {'; '.join(reasons) if reasons else ''}\"\n    print(row)\n\n# Special analysis: SFT s42 eval experiments\nprint(f\"\\n\\n{'=' * 120}\")\nprint(\"SPECIAL ANALYSIS: SFT s42 (original seed) eval experiments\")\nprint(f\"{'=' * 120}\")\nfor exp_id, exp in eval_exps:\n    if 's42' in exp_id.lower() or 'seed42' in exp_id.lower() or ('sft' in exp_id.lower() and 's42' in exp.get('hypothesis', '').lower()):\n        cmd = exp.get('spec', {}).get('command', '')\n        parsed = parse_command(cmd)\n        print(f\"\\n  exp_id: {exp_id}\")\n        print(f\"  status: {exp.get('status', '?')}\")\n        print(f\"  model_path:  {parsed['model_path']}\")\n        print(f\"  sft_adapter: {parsed['sft_adapter']}\")\n        print(f\"  FULL CMD: {cmd}\")\n\n# Also check: any eval using the original SFT output (no seed suffix)\nprint(f\"\\n\\n{'=' * 120}\")\nprint(\"SPECIAL ANALYSIS: Evals with model_path pointing to adapter directories\")\nprint(f\"{'=' * 120}\")\nfor exp_id, exp in eval_exps:\n    cmd = exp.get('spec', {}).get('command', '')\n    parsed = parse_command(cmd)\n    if parsed['model_path']:\n        base_ok, base_msg = check_model_path_is_base(parsed['model_path'])\n        if not base_ok:\n            print(f\"\\n  exp_id:     {exp_id}\")\n            print(f\"  status:     {exp.get('status', '?')}\")\n            print(f\"  model_path: {parsed['model_path']}\")\n            print(f\"  issue:      {base_msg}\")\n            print(f\"  FULL CMD:   {cmd}\")\n\nprint(f\"\\n\\n{'=' * 120}\")\nprint(\"SPECIAL ANALYSIS: Evals MISSING --no-quantize\")\nprint(f\"{'=' * 120}\")\nfor exp_id, exp in eval_exps:\n    cmd = exp.get('spec', {}).get('command', '')\n    parsed = parse_command(cmd)\n    if not parsed['no_quantize']:\n        print(f\"\\n  exp_id:  {exp_id}\")\n        print(f\"  status:  {exp.get('status', '?')}\")\n        print(f\"  FULL CMD: {cmd}\")\n\nprint(f\"\\n\\n{'=' * 120}\")\nprint(\"SPECIAL ANALYSIS: Evals with non-standard batch_size or max_new_tokens\")\nprint(f\"{'=' * 120}\")\nfor exp_id, exp in eval_exps:\n    cmd = exp.get('spec', {}).get('command', '')\n    parsed = parse_command(cmd)\n    issues = []\n    if parsed['batch_size'] and parsed['batch_size'] != '4':\n        issues.append(f\"batch_size={parsed['batch_size']}\")\n    if parsed['max_new_tokens'] and parsed['max_new_tokens'] != '1024':\n        issues.append(f\"max_new_tokens={parsed['max_new_tokens']}\")\n    if issues:\n        print(f\"\\n  exp_id:  {exp_id}\")\n        print(f\"  status:  {exp.get('status', '?')}\")\n        print(f\"  issues:  {', '.join(issues)}\")\n        print(f\"  FULL CMD: {cmd}\")\n\n# Count compliant vs non-compliant\ncompliant_count = 0\nnon_compliant_count = 0\nfor exp_id, exp in eval_exps:\n    cmd = exp.get('spec', {}).get('command', '')\n    parsed = parse_command(cmd)\n    compliant, _ = check_d076(parsed)\n    if compliant:\n        compliant_count += 1\n    else:\n        non_compliant_count += 1\n\nprint(f\"\\n\\n{'=' * 120}\")\nprint(f\"OVERALL D076 COMPLIANCE: {compliant_count}/{len(eval_exps)} compliant, {non_compliant_count}/{len(eval_exps)} non-compliant\")\nprint(f\"{'=' * 120}\")\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01TeEH97guEfBfH5188hkZEb",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "ddd39e3e-274c-4597-a1b6-f386fb1a0bb5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TNEiC75nPnzZGc9WpLM4Mk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1138,
      "cache_read_input_tokens": 18875,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1138,
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

_source line 102 · 2026-05-18T22:06:39.865Z_

<details><summary>↩ Tool result · `toolu_015awc5JNyFhDZQXUx7fqLb7`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/d076_eval_audit.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01TeEH97guEfBfH5188hkZEb",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "83d6651d-5f0b-448e-8ea3-29dcd458b030"
}
```

</details>

---


### System

_source line 103_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a35180a8a436e895f",
  "tool_use_id": "toolu_01TeEH97guEfBfH5188hkZEb",
  "description": "Running Run D076 compliance audit script",
  "usage": {
    "total_tokens": 25161,
    "tool_uses": 8,
    "duration_ms": 90470
  },
  "last_tool_name": "Bash",
  "uuid": "52df8dff-1142-477b-86df-2fa788d6181c",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0"
}
```

---


### Tool call

_source line 104_

<details open><summary>🔧 Tool call — Bash · `toolu_01HZLvcqQ9v3AhKgdAkXPUMR`</summary>

```json
{
  "command": "python3 artifacts/d076_eval_audit.py 2>&1",
  "description": "Run D076 compliance audit script",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01TeEH97guEfBfH5188hkZEb",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "0d4d4fea-f0e4-4868-8ce6-2de8ee32fb8d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P4pBVYCtj3FwkkhugAaF2r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4871,
      "cache_read_input_tokens": 20013,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4871,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 60,
      "service_tier": "standard",
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

_source line 105 · 2026-05-18T22:06:43.377Z_

<details><summary>↩ Tool result · `toolu_01HZLvcqQ9v3AhKgdAkXPUMR`</summary>

```text
&lt;persisted-output>
Output too large (235.2KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/596d8411-63f5-4757-a2a4-2c57b1fcaba0/tool-results/b432e0wbi.txt

Preview (first 2KB):
========================================================================================================================
D076 PROTOCOL COMPLIANCE AUDIT - All Qwen3-4B Eval Experiments
Total experiments in registry: 222
4B eval experiments found: 84
========================================================================================================================


────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
[1/84] exp_id: eval_flat_nli_s44
  status:     DONE
  hypothesis: Full dev eval of flat-NLI RSFT seed=44 with --sft_adapter + --no-quantize. C3 统计显著性数据点 (s42=0.4539, s43 pending, s44 本次, s45 pending)。
  parent:     plan_001_flat_nli_seed44
  model_name: N/A

  FULL COMMAND:
    bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_flat_nli_s44/checkpoint-507 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 1024 --seed 44 --output_dir /root/autodl-tmp/eval_results/rsft_flat_nli_s44 --no-quantize"

  PARSED D076 PARAMS:
    batch_size:     4
    max_new_tokens: 1024
    seed:           44
    no_quantize:    True
    model_path:     /root/autodl-tmp/rsft_output_flat_nli_s44/checkpoint-507
    sft_adapter:    /root/autodl-tmp/sft_output

  D076 COMPLIANT:   NO
  NON-COMPLIANCE:   seed=44 (expected 42); model_path: points to adapter dir: /root/autodl-tmp/rsft_output_flat_nli_s44/checkpoint-507

  metrics:    {
    "rel_f1": 0.461506,
    "ign_f1": 0.452126,
    "evi_f1": 0.813123,
    "edcr": 0.645808,
    "evi_f1_joint": 0.359673
}
  conclusion: N/A
  notes:      N/A
  error:      N/A
  reproduce extra keys: ['command']
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01TeEH97guEfBfH5188hkZEb",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "56fc02e3-6904-4933-9d90-d8a0f5571c21"
}
```

</details>

---


### System

_source line 106_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a35180a8a436e895f",
  "tool_use_id": "toolu_01TeEH97guEfBfH5188hkZEb",
  "description": "Running Read summary table from audit output",
  "usage": {
    "total_tokens": 26111,
    "tool_uses": 9,
    "duration_ms": 95097
  },
  "last_tool_name": "Bash",
  "uuid": "38e5b2b6-3ce4-4854-b5eb-2f42dfb7700d",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0"
}
```

---


### Tool call

_source line 107_

<details open><summary>🔧 Tool call — Bash · `toolu_01UR1G4TZeTThrUnuqmk3vDH`</summary>

```json
{
  "command": "python3 -c \"\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/596d8411-63f5-4757-a2a4-2c57b1fcaba0/tool-results/b432e0wbi.txt', 'r') as f:\n    content = f.read()\n\n# Find the SUMMARY TABLE section\nidx = content.find('SUMMARY TABLE')\nif idx != -1:\n    print(content[idx:])\n\"\n",
  "description": "Read summary table from audit output",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01TeEH97guEfBfH5188hkZEb",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "50ee8def-f9db-43bf-b3d8-5da54bb80049",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017EXYpUWToqyRVEVbX45BtJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5819,
      "cache_read_input_tokens": 20013,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5819,
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

_source line 108 · 2026-05-18T22:06:47.969Z_

<details><summary>↩ Tool result · `toolu_01UR1G4TZeTThrUnuqmk3vDH`</summary>

```text
&lt;persisted-output>
Output too large (83.7KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/596d8411-63f5-4757-a2a4-2c57b1fcaba0/tool-results/bbsbky2j1.txt

Preview (first 2KB):
SUMMARY TABLE
========================================================================================================================================================================================================
exp_id                                        | status       | ign_f1   | bs   | max_tok  | seed  | no_q  | model_path                                              | sft_adapter                                             | D076  | non_compliance
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
eval_flat_nli_s44                             | DONE         | N/A      | 4    | 1024     | 44    | Y     | root/autodl-tmp/rsft_output_flat_nli_s44/checkpoint-507 | /root/autodl-tmp/sft_output                             | NO    | seed=44 (expected 42); model_path: points to adapter dir: /root/autodl-tmp/rsft_output_flat_nli_s44/checkpoint-507
eval_flat_nli_seed44                          | DONE         | N/A      | 4    | 1024     | 44    | Y     | root/autodl-tmp/rsft_output_flat_nli_s44/checkpoint-507 | /root/autodl-tmp/sft_output                             | NO    | seed=44 (expected 42); model_path: points to adapter dir: /root/autodl-tmp/rsft_output_flat_nli_s44/checkpoint-507
eval_flat_nli_seed45                          | DONE         | N/A      | 4    | 1024     | 45    | Y     | root/autodl-tmp/rsft_output_flat_nli_s45/checkpoint-507 | /root/autodl-tmp/sft_output                             | NO    | seed=45 (expected 42); model_path: points to adapter dir: /root/autodl-tmp/rsft_output_flat_nli_s45/checkpoint-507
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01TeEH97guEfBfH5188hkZEb",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "84c7fdd7-7215-40af-b47b-8402a7f04f80"
}
```

</details>

---


### System

_source line 109_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a35180a8a436e895f",
  "tool_use_id": "toolu_01TeEH97guEfBfH5188hkZEb",
  "description": "Reading ~/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/596d8411-63f5-4757-a2a4-2c57b1fcaba0/tool-results/bbsbky2j1.txt",
  "usage": {
    "total_tokens": 27048,
    "tool_uses": 10,
    "duration_ms": 98022
  },
  "last_tool_name": "Read",
  "uuid": "6f279496-f4d0-4816-a254-66925bbadaf9",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0"
}
```

---


### Tool call

_source line 110_

<details open><summary>🔧 Tool call — Read · `toolu_01TZ8f6yoKynx7Z3ZFuDFzo8`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/596d8411-63f5-4757-a2a4-2c57b1fcaba0/tool-results/bbsbky2j1.txt",
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01TeEH97guEfBfH5188hkZEb",
  "session_id": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "uuid": "fe76e3a7-4430-43a3-8755-f09af1abef0e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014BRBrTmNxMhiUVNRzm7oC8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 872,
      "cache_read_input_tokens": 25832,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 872,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---
