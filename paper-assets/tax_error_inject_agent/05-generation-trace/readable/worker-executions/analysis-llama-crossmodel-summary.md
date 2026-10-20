# analysis llama crossmodel summary

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 60
- **Recorded user turns:** 1
- **Tool calls:** 18
- **Original source:** `logs/workers/worker_analysis_llama-crossmodel-summary_20260516T145311.log`
- **Structured JSON:** [`c05f8f012d18471f719a.json`](../../sessions/c0/c05f8f012d18471f719a.json)

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55",
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
  "uuid": "27067193-12ba-41a6-9df6-f2d8418e9c15",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/memory/"
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
    "resetsAt": 1778955600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "38830793-99ed-449e-9aa2-93aed7ac1f03",
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the registry to get all llama31-* experiment metrics.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55",
  "uuid": "aa18d791-0e51-4b9c-8e01-3da807af81a9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WXtZGDBSBUH7XuEqXzizpY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11741,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11741
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

_source line 5_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Sr9FF8zmMLTMWtM8wUeRh1`</summary>

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
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55",
  "uuid": "d84b12db-b74f-4ce0-be0c-21a4df9693f1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WXtZGDBSBUH7XuEqXzizpY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11741,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11741
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

_source line 6 · 2026-05-16T14:53:26.873Z_

<details><summary>↩ Tool result · `toolu_01Sr9FF8zmMLTMWtM8wUeRh1`</summary>

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
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55",
  "uuid": "1ac63ef7-7816-464e-bb50-91a6fdc6bbb1",
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
Let me read the registry to get all llama31-* experiment data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55",
  "uuid": "3bc5ad3e-eaf6-40b5-8660-98fe28ff2701",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U7fQTDg8YtH9TZoqBbvL3S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1358,
      "cache_read_input_tokens": 23582,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1358
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

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01Bv9Q9w1nTDbXGnFaqrzqTm`</summary>

```json
{
  "project": "tax_error_inject_agent",
  "filters": {
    "status": "DONE"
  },
  "fields": [
    "*"
  ],
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
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55",
  "uuid": "88555b8a-cd85-4ba3-b82f-7088a4c2553e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U7fQTDg8YtH9TZoqBbvL3S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1358,
      "cache_read_input_tokens": 23582,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1358
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01Hdy4jeVY8PrRs3uUijW5Fd`</summary>

```json
{
  "project": "tax_error_inject_agent",
  "filters": {
    "status": "RUNNING"
  },
  "fields": [
    "*"
  ],
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
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55",
  "uuid": "e7cb726f-c6cb-4161-8118-ba19618dc9f3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U7fQTDg8YtH9TZoqBbvL3S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1358,
      "cache_read_input_tokens": 23582,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1358
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

_source line 10 · 2026-05-16T14:53:32.159Z_

<details><summary>↩ Tool result · `toolu_01Bv9Q9w1nTDbXGnFaqrzqTm`</summary>

```text
Error: result (189,288 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/ae491a69-2268-4f52-bbd5-112d75ec9c55/tool-results/mcp-agent-ml-research-read_registry-1778943212143.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/ae491a69-2268-4f52-bbd5-112d75ec9c55/tool-results/mcp-agent-ml-research-read_registry-1778943212143.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/ae491a69-2268-4f52-bbd5-112d75ec9c55/tool-results/mcp-agent-ml-research-read_registry-1778943212143.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55",
  "uuid": "8540a05e-7e55-4d46-a57b-90e981fb3b2f",
  "tool_use_result": {
    "content": "Error: result (189,288 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/ae491a69-2268-4f52-bbd5-112d75ec9c55/tool-results/mcp-agent-ml-research-read_registry-1778943212143.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/ae491a69-2268-4f52-bbd5-112d75ec9c55/tool-results/mcp-agent-ml-research-read_registry-1778943212143.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/ae491a69-2268-4f52-bbd5-112d75ec9c55/tool-results/mcp-agent-ml-research-read_registry-1778943212143.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"recovery-random-s7\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T14:37:24.534Z\", \"updated_at\": \"2026-05-16T14:49:59.675Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python eval/injected_eval.py --model_path checkpoints/mini_random_sft_v4_seed7/v0-20260515-233427/checkpoint-3387 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --model_variant random --num_episodes 47 --output eval_results/v4_random_recovery_eval_s7.json --device cuda:0 --seed 42\", \"server\": \"autodl-5090\", \"data_path\": \"eval/alfworld_tasks\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + mini_random_sft_v4_seed7\", \"seed\": 7, \"checkpoint_source\": \"checkpoints/mini_random_sft_v4_seed7/v0-20260515-233427/checkpoint-3387\", \"eval_data\": \"47 ALFWorld tasks with error injection\", \"parent\": \"mini_random_sft_v4_seed7\", \"checkpoint_path\": \"checkpoints/mini_random_sft_v4_seed7/v0-20260515-233427/checkpoint-3387\", \"log_path\": \"eval_results/v4_random_recovery_eval_s7.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T14:37:52.029Z\", \"metrics\": {\"recovery_rate\": 0.532, \"detection_rate\": 0, \"total_episodes\": 47}}, \"recovery-random-s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T14:37:23.085Z\", \"updated_at\": \"2026-05-16T14:49:58.929Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python eval/injected_eval.py --model_path checkpoints/mini_random_sft_v4_seed1/v0-20260515-232340/checkpoint-3387 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --model_variant random --num_episodes 47 --output eval_results/v4_random_recovery_eval_s1.json --device cuda:0 --seed 42\", \"server\": \"autodl-5090\", \"data_path\": \"eval/alfworld_tasks\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + mini_random_sft_v4_seed1\", \"seed\": 1, \"checkpoint_source\": \"checkpoints/mini_random_sft_v4_seed1/v0-20260515-232340/checkpoint-3387\", \"eval_data\": \"47 ALFWorld tasks with error injection\", \"parent\": \"mini_random_sft_v4_seed1\", \"checkpoint_path\": \"checkpoints/mini_random_sft_v4_seed1/v0-20260515-232340/checkpoint-3387\", \"log_path\": \"eval_results/v4_random_recovery_eval_s1.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T14:37:50.738Z\", \"metrics\": {\"recovery_rate\": 0.511, \"detection_rate\": 0, \"total_episodes\": 47}}, \"llama31-vanilla-s123-clean\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T14:36:07.599Z\", \"updated_at\": \"2026-05-16T14:36:39.967Z\", \"conclusion\": \"success\", \"spec\": {\"command\": \"python eval/recovery.py --model_path output/llama31-vanilla-s123/v0-20260516-205231/checkpoint-1635 --base_model /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct/ --task_list eval/eval_tasks_47.json --num_episodes 47 --output eval_results/llama31_vanilla_s123_clean.json --no_inject --seed 123 --device cuda:0\", \"server\": \"autodl-5090\", \"data_path\": \"eval/eval_tasks_47.json\", \"data_count\": 47, \"model_name\": \"llama31-vanilla-s123\", \"seed\": 123, \"checkpoint_source\": \"output/llama31-vanilla-s123/v0-20260516-205231/checkpoint-1635\", \"eval_data\": \"valid_unseen\", \"checkpoint_path\": \"output/llama31-vanilla-s123/v0-20260516-205231/checkpoint-1635\", \"log_path\": \"eval_results/llama31_vanilla_s123_clean.log\", \"parent\": \"llama31-vanilla-s123\"}, \"completed_at\": \"2026-05-16T14:36:32.828Z\", \"metrics\": {\"success_rate\": 0.723, \"total_episodes\": 47, \"eval_type\": \"clean\", \"eval_script\": \"eval/recovery.py\", \"output_file\": \"eval_results/llama31_vanilla_s123_clean.json\", \"by_task_type\": {\"look_at_obj_in_light\": 0.833, \"pick_and_place_simple\": 0.625, \"pick_clean_then_place_in_recep\": 0.545, \"pick_cool_then_place_in_recep\": 0.571, \"pick_heat_then_place_in_recep\": 1, \"pick_two_obj_and_place\": 0.857}}}, \"llama31-vanilla-s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T12:52:22.460Z\", \"updated_at\": \"2026-05-16T14:26:04.356Z\", \"spec\": {\"command\": \"swift sft --model /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct --dataset data/mini_pipeline_v4/sft_vanilla_v4.jsonl --output_dir output/llama31-vanilla-s123 --lora_rank 16 --num_train_epochs 3 --per_device_train_batch_size 4 --gradient_accumulation_steps 2 --learning_rate 1e-4 --max_length 4096 --seed 123 --data_seed 123 --logging_steps 10 --gradient_checkpointing true --bf16 true --save_strategy epoch\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"277341\", \"log_path\": \"~/runs/tax_error_inject_agent/llama31-vanilla-s123.log\", \"submitted_at\": \"2026-05-16T12:52:22.085Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/mini_pipeline_v4/sft_vanilla_v4.jsonl\", \"data_count\": 4358, \"model_name\": \"Meta-Llama-3.1-8B-Instruct\", \"seed\": 123, \"wall_clock_seconds\": 4992.9, \"gpu_hours\": 1.39}, \"hypothesis\": \"Cross-model: LLaMA Vanilla s123 - 3rd seed for 3-seed cross-model validation\", \"checkpoint_path\": \"output/llama31-vanilla-s123/v0-20260516-205231/checkpoint-1635\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T14:15:35.008Z\", \"metrics\": {\"train_loss\": 0.4, \"final_loss\": 0.254, \"token_acc\": 0.894, \"steps\": 1635, \"epochs\": 3, \"runtime_seconds\": 4234, \"memory_gib\": 29.85}}, \"llama31-taxei-s0-clean\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T14:05:45.875Z\", \"updated_at\": \"2026-05-16T14:06:24.173Z\", \"hypothesis\": \"Cross-model: LLaMA TaxEI s0 clean eval — baseline task success without injection\", \"spec\": {\"command\": \"python3 eval/recovery.py --model_path output/llama31-taxei-s0/v1-20260516-181826/checkpoint-3387 --base_model /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct --num_episodes 47 --task_list eval/eval_tasks_47.json --output eval_results/llama31_taxei_s0_clean.json\", \"server\": \"autodl-5090\", \"data_path\": \"eval/eval_tasks_47.json\", \"data_count\": 47, \"model_name\": \"Meta-Llama-3.1-8B-Instruct + taxei-s0 LoRA\", \"seed\": 0, \"checkpoint_source\": \"output/llama31-taxei-s0/v1-20260516-181826/checkpoint-3387\", \"eval_data\": \"clean_eval_47ep\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/llama31-taxei-s0/v1-20260516-181826/checkpoint-3387\", \"log_path\": \"/root/autodl-tmp/tax_error_inject_agent/eval_results/llama31_taxei_s0_clean.json\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.766, \"total_episodes\": 47}, \"completed_at\": \"2026-05-16T14:06:24.173Z\"}, \"llama31-taxei-s0-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T12:52:20.766Z\", \"updated_at\": \"2026-05-16T14:04:47.458Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && python3 eval/injected_eval.py --model_path output/llama31-taxei-s0/v1-20260516-181826/checkpoint-3387 --base_model /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct --model_variant taxei --output eval_results/llama31_taxei_s0_eval.json --seed 42 --num_episodes 47\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"278309\", \"log_path\": \"/root/autodl-tmp/tax_error_inject_agent/eval_results/llama31_taxei_s0_eval.json\", \"submitted_at\": \"2026-05-16T12:52:40.445Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"parent\": \"llama31-taxei-s0\", \"checkpoint_source\": \"output/llama31-taxei-s0/v1-20260516-181826/checkpoint-3387\", \"eval_data\": \"injected_eval_47ep\", \"model_name\": \"Meta-Llama-3.1-8B-Instruct + taxei-s0 LoRA\", \"seed\": 42, \"data_path\": \"eval/injected_eval.py (built-in ALFWorld tasks)\", \"data_count\": 47, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/llama31-taxei-s0/v1-20260516-181826/checkpoint-3387\", \"wall_clock_seconds\": 4327.0, \"gpu_hours\": 1.2}, \"hypothesis\": \"Cross-model: LLaMA TaxEI s0 injected eval — does taxonomy injection help on LLaMA seed 0?\", \"conclusion\": \"success\", \"metrics\": {\"recovery_rate\": 0.745, \"success_rate\": 0.745, \"total_episodes\": 47}, \"completed_at\": \"2026-05-16T14:04:47.458Z\"}, \"llama31-random-s42-clean\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T11:30:37.651Z\", \"updated_at\": \"2026-05-16T13:19:33.606Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python3 eval/recovery.py --model_path output/llama31-random-s42/v0-20260516-142300/checkpoint-3387 --base_model /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct --num_episodes 47 --task_list eval/eval_tasks_47.json --output eval_results/llama31_random_s42_clean.json\", \"server\": \"autodl-5090\", \"data_path\": \"eval/eval_tasks_47.json\", \"data_count\": 47, \"model_name\": \"Meta-Llama-3.1-8B-Instruct + llama31-random-s42 LoRA\", \"seed\": 42, \"checkpoint_source\": \"output/llama31-random-s42/v0-20260516-142300/checkpoint-3387\", \"eval_data\": \"ALFWorld clean eval 47 tasks\", \"hypothesis\": \"LLaMA Random s42 clean eval - baseline success rate without injection\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.766, \"eval_type\": \"clean\", \"eval_script\": \"eval/recovery.py\", \"total_episodes\": 47, \"output_file\": \"eval_results/llama31_random_s42_clean.json\"}, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/llama31-random-s42/v0-20260516-142300/checkpoint-3387\", \"log_path\": \"eval_results/llama31_random_s42_clean.json\", \"completed_at\": \"2026-05-16T11:50:54.372Z\"}, \"llama31-taxei-s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T09:15:57.399Z\", \"updated_at\": \"2026-05-16T12:39:46.148Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 swift sft --model Meta-Llama-3.1-8B-Instruct --dataset sft_taxei_v4.jsonl --output_dir output/llama31-taxei-s0 --lora_rank 16 --num_train_epochs 3 --seed 0\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"262833\", \"log_path\": \"~/runs/tax_error_inject_agent/llama31-taxei-s0.log\", \"submitted_at\": \"2026-05-16T09:15:57.070Z\", \"submitted_via\": \"manual_retry_v1\", \"backend\": \"interactive_pts\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/tax_error_inject_agent/data/mini_pipeline_v4/sft_taxei_v4.jsonl\", \"data_count\": 9029, \"model_name\": \"Meta-Llama-3.1-8B-Instruct\", \"seed\": 0, \"hypothesis\": \"Cross-model: LLaMA TaxEI s0 - 2nd seed for 3-seed cross-model validation\", \"wall_clock_seconds\": 11561.0, \"gpu_hours\": 3.21}, \"reproduce\": {\"finished_at\": \"2026-05-16T12:28:37.402Z\"}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"conclusion\": \"success\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T10:20:11.090300+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T12:28:42.837165+00:00\"}]}, \"completed_at\": \"2026-05-16T12:28:38.032Z\", \"metrics\": {\"final_train_loss\": 0.32, \"final_token_acc\": 0.88, \"train_steps\": 3387, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/llama31-taxei-s0/v1-20260516-181826/checkpoint-3387\"}, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/llama31-taxei-s0/v1-20260516-181826/checkpoint-3387\"}, \"v4-random-recovery-eval-s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T12:44:11.530Z\", \"updated_at\": \"2026-05-16T12:38:01.309Z\", \"spec\": {\"model_name\": \"Qwen3-8B + Random LoRA s123\", \"seed\": 42, \"method\": \"random\", \"eval_type\": \"recovery\", \"parent\": \"v4-random-sft-s123\", \"checkpoint_source\": \"checkpoints/mini_random_sft_v4_seed123/v0-20260515-055925/checkpoint-3387\", \"eval_data\": \"ALFWorld injected eval (47 episodes)\", \"server\": \"autodl-5090\", \"command\": \"CUDA_VISIBLE_DEVICES=3 python3 eval/injected_eval.py --model_path checkpoints/mini_random_sft_v4_seed123/v0-20260515-055925/checkpoint-3387 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --model_variant random --output eval_results/v4_random_recovery_eval_s123.json --seed 42 --num_episodes 47\", \"data_path\": \"eval/injected_eval.py\", \"data_count\": 47, \"checkpoint_path\": \"checkpoints/mini_random_sft_v4_seed123/v0-20260515-055925/checkpoint-3387\", \"log_path\": \"eval_results/v4_random_recovery_eval_s123.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T12:07:20.925Z\", \"metrics\": {\"recovery_rate\": 0.66, \"detection_rate\": 0, \"total_episodes\": 47, \"by_operator\": {\"C1_context_truncation\": {\"recovery_rate\": 0.75, \"recovered\": 9, \"total\": 12}, \"P2_sub_goal_deletion\": {\"recovery_rate\": 0.75, \"recovered\": 9, \"total\": 12}, \"P1_step_order_swap\": {\"recovery_rate\": 0.583, \"recovered\": 7, \"total\": 12}, \"C4_observation_masking\": {\"recovery_rate\": 0.545, \"recovered\": 6, \"total\": 11}}}}, \"llama31-vanilla-s0-clean\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T12:14:53.046Z\", \"updated_at\": \"2026-05-16T12:35:41.228Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 eval/recovery.py --model_path output/llama31-vanilla-s0/v0-20260516-171603/checkpoint-1635 --base_model /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct --num_episodes 47 --task_list eval/eval_tasks_47.json --output eval_results/llama31_vanilla_s0_clean.json\", \"server\": \"autodl-5090\", \"data_path\": \"eval/eval_tasks_47.json\", \"data_count\": 47, \"model_name\": \"Meta-Llama-3.1-8B-Instruct + llama31-vanilla-s0 LoRA\", \"seed\": 0, \"checkpoint_source\": \"output/llama31-vanilla-s0/v0-20260516-171603/checkpoint-1635\", \"eval_data\": \"ALFWorld clean eval 47 tasks\", \"hypothesis\": \"LLaMA Vanilla s0 clean eval - baseline success rate without injection\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.723, \"eval_type\": \"clean\", \"eval_script\": \"eval/recovery.py\", \"total_episodes\": 47, \"output_file\": \"eval_results/llama31_vanilla_s0_clean.json\"}, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/llama31-vanilla-s0/v0-20260516-171603/checkpoint-1635\", \"log_path\": \"eval_results/llama31_vanilla_s0_clean.json\", \"completed_at\": \"2026-05-16T12:35:41.228Z\"}, \"llama31-vanilla-s42-clean\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T12:14:50.470Z\", \"updated_at\": \"2026-05-16T12:35:18.899Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 eval/recovery.py --model_path output/llama31-vanilla-s42/v0-20260516-143227/checkpoint-1635 --base_model /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct --num_episodes 47 --task_list eval/eval_tasks_47.json --output eval_results/llama31_vanilla_s42_clean.json\", \"server\": \"autodl-5090\", \"data_path\": \"eval/eval_tasks_47.json\", \"data_count\": 47, \"model_name\": \"Meta-Llama-3.1-8B-Instruct + llama31-vanilla-s42 LoRA\", \"seed\": 42, \"checkpoint_source\": \"output/llama31-vanilla-s42/v0-20260516-143227/checkpoint-1635\", \"eval_data\": \"ALFWorld clean eval 47 tasks\", \"hypothesis\": \"LLaMA Vanilla s42 clean eval - baseline success rate without injection\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.723, \"eval_type\": \"clean\", \"eval_script\": \"eval/recovery.py\", \"total_episodes\": 47, \"output_file\": \"eval_results/llama31_vanilla_s42_clean.json\"}, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/llama31-vanilla-s42/v0-20260516-143227/checkpoint-1635\", \"log_path\": \"eval_results/llama31_vanilla_s42_clean.json\", \"completed_at\": \"2026-05-16T12:35:18.899Z\"}, \"recovery-taxei-s7\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T11:53:18.146Z\", \"updated_at\": \"2026-05-16T12:13:31.737Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python3 eval/injected_eval.py --model_path checkpoints/mini_taxei_sft_v4_seed7/.../checkpoint-3387 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --model_variant taxei --output_file eval_results/v4_taxei_recovery_eval_s7.json\", \"server\": \"autodl-5090\", \"data_path\": \"eval/injected_eval.py\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + TaxEI s7 LoRA\", \"seed\": 7, \"checkpoint_source\": \"checkpoints/mini_taxei_sft_v4_seed7\", \"eval_data\": \"ALFWorld injected eval 47 tasks\", \"hypothesis\": \"Recovery eval TaxEI s7 - complete 5-seed recovery validation\"}, \"conclusion\": \"success\", \"metrics\": {\"recovery_rate\": 0.574, \"detection_rate\": 0, \"total_episodes\": 47}, \"checkpoint_path\": \"checkpoints/mini_taxei_sft_v4_seed7\", \"log_path\": \"eval_results/v4_taxei_recovery_eval_s7.json\", \"completed_at\": \"2026-05-16T12:13:31.737Z\"}, \"llama31-random-s0-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T11:58:20.799Z\", \"updated_at\": \"2026-05-16T11:59:00.205Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python3 eval/injected_eval.py --model_path output/llama31-random-s0/v0-20260516-171608/checkpoint-3387 --base_model /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct --model_variant random --num_episodes 47 --output eval_results/llama31_random_s0_injected.json\", \"server\": \"autodl-5090\", \"data_path\": \"eval/eval_tasks_47.json\", \"data_count\": 47, \"model_name\": \"Meta-Llama-3.1-8B-Instruct + LoRA random s0\", \"seed\": 42, \"checkpoint_source\": \"output/llama31-random-s0/v0-20260516-171608/checkpoint-3387\", \"eval_data\": \"ALFWorld valid_unseen 47 episodes injected\"}, \"checkpoint_path\": \"output/llama31-random-s0/v0-20260516-171608/checkpoint-3387\", \"log_path\": \"eval_results/llama31_random_s0_injected.json\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T11:58:51.624Z\", \"metrics\": {\"recovery_rate\": 0.745, \"detection_rate\": 0.255, \"success_rate\": 0.745, \"total_episodes\": 47, \"by_operator\": {\"C1_context_truncation\": {\"total\": 12, \"recovered\": 10, \"detected\": 1, \"recovery_rate\": 0.833, \"detection_rate\": 0.083}, \"C4_observation_masking\": {\"total\": 11, \"recovered\": 8, \"detected\": 4, \"recovery_rate\": 0.727, \"detection_rate\": 0.364}, \"P1_step_order_swap\": {\"total\": 12, \"recovered\": 8, \"detected\": 4, \"recovery_rate\": 0.667, \"detection_rate\": 0.333}, \"P2_sub_goal_deletion\": {\"total\": 12, \"recovered\": 9, \"detected\": 3, \"recovery_rate\": 0.75, \"detection_rate\": 0.25}}}}, \"llama31-random-s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T09:16:00.115Z\", \"updated_at\": \"2026-05-16T11:28:10.720Z\", \"spec\": {\"command\": \"swift sft --model /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct --dataset data/mini_pipeline_v4/sft_random_v4.jsonl --output_dir output/llama31-random-s0 --lora_rank 16 --num_train_epochs 3 --per_device_train_batch_size 4 --gradient_accumulation_steps 2 --learning_rate 1e-4 --max_length 4096 --seed 0 --data_seed 0 --logging_steps 10 --gradient_checkpointing true --bf16 true --save_strategy epoch\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"260936\", \"log_path\": \"~/runs/tax_error_inject_agent/llama31-random-s0.log\", \"submitted_at\": \"2026-05-16T09:15:59.761Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/mini_pipeline_v4/sft_random_v4.jsonl\", \"data_count\": 9031, \"model_name\": \"Meta-Llama-3.1-8B-Instruct\", \"seed\": 0, \"wall_clock_seconds\": 7931.0, \"gpu_hours\": 2.2}, \"reproduce\": {\"finished_at\": \"2026-05-16T11:24:56.461Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T11:24:59.790065+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"final_train_loss\": 0.3368, \"epoch1_loss\": 0.452, \"epoch2_loss\": 0.238, \"epoch3_loss\": 0.134, \"final_token_acc\": 0.9357, \"train_runtime_sec\": 7622, \"train_steps\": 3387, \"peak_memory_gib\": 30.74, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/llama31-random-s0/v0-20260516-171608/checkpoint-3387\"}, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/llama31-random-s0/v0-20260516-171608/checkpoint-3387\", \"log_path\": \"~/runs/tax_error_inject_agent/llama31-random-s0.log\", \"completed_at\": \"2026-05-16T11:28:10.720Z\"}, \"llama31-vanilla-s0-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T10:39:37.086Z\", \"updated_at\": \"2026-05-16T11:21:29.608Z\", \"hypothesis\": \"LLaMA-3.1-8B Vanilla s0 injected eval - cross-model validation seed 0\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python3 eval/injected_eval.py --model_path output/llama31-vanilla-s0/v0-20260516-171603/checkpoint-1635 --base_model /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct --model_variant vanilla --seed 0 --num_episodes 47 --output eval_results/llama31_vanilla_s0_injected.json\", \"server\": \"autodl-5090\", \"data_path\": \"eval/injected_eval.py\", \"data_count\": 47, \"model_name\": \"Meta-Llama-3.1-8B-Instruct + llama31-vanilla-s0 LoRA\", \"seed\": 0, \"checkpoint_source\": \"output/llama31-vanilla-s0/v0-20260516-171603/checkpoint-1635\", \"eval_data\": \"ALFWorld injected eval 47 tasks\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T11:05:01.407Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T11:05:03.246Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T11:05:05.820946+00:00\"}]}, \"metrics\": {\"recovery_rate\": 0.745, \"recovery_count\": \"35/47\", \"detection_rate\": 0.277, \"eval_type\": \"injected\", \"eval_script\": \"injected_eval.py\", \"output_file\": \"eval_results/llama31_vanilla_s0_injected.json\", \"C1_context_truncation\": {\"recovery\": 0.667, \"detection\": 0.167}, \"C4_observation_masking\": {\"recovery\": 0.727, \"detection\": 0.364}, \"P1_step_order_swap\": {\"recovery\": 0.917, \"detection\": 0.333}, \"P2_sub_goal_deletion\": {\"recovery\": 0.667, \"detection\": 0.25}}}, \"v4-random-recovery-eval-s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T12:44:10.000Z\", \"updated_at\": \"2026-05-16T10:54:26.532Z\", \"spec\": {\"model_name\": \"Qwen3-8B + LoRA (mini_random_sft_v4_seed0)\", \"seed\": 0, \"method\": \"random\", \"eval_type\": \"recovery\", \"parent\": \"v4-random-sft-s0\", \"checkpoint_source\": \"checkpoints/mini_random_sft_v4_seed0/v0-20260515-014329/checkpoint-3387\", \"eval_data\": \"ALFWorld 47 episodes with error injection\", \"server\": \"autodl-5090\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python eval/injected_eval.py --model_path checkpoints/mini_random_sft_v4_seed0/v0-20260515-014329/checkpoint-3387 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --model_variant random --output eval_results/v4_random_recovery_eval_s0.json --device cuda:0 --seed 42 --num_episodes 47\", \"data_path\": \"/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_random_recovery_eval_s0.json\", \"data_count\": 47}, \"conclusion\": \"success\", \"checkpoint_path\": \"checkpoints/mini_random_sft_v4_seed0/v0-20260515-014329/checkpoint-3387\", \"log_path\": \"eval_results/v4_random_recovery_eval_s0.json\", \"completed_at\": \"2026-05-16T10:54:19.062Z\", \"metrics\": {\"recovery_rate\": 0.553, \"detection_rate\": 0, \"success_rate\": 0.553, \"total_episodes\": 47, \"by_operator\": {\"C1_context_truncation\": {\"total\": 12, \"recovered\": 7, \"recovery_rate\": 0.583}, \"C4_observation_masking\": {\"total\": 11, \"recovered\": 6, \"recovery_rate\": 0.545}, \"P1_step_order_swap\": {\"total\": 12, \"recovered\": 7, \"recovery_rate\": 0.583}, \"P2_sub_goal_deletion\": {\"total\": 12, \"recovered\": 6, \"recovery_rate\": 0.5}}}}, \"llama31-vanilla-s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T09:15:55.388Z\", \"updated_at\": \"2026-05-16T10:29:59.217Z\", \"spec\": {\"command\": \"swift sft --model Meta-Llama-3.1-8B-Instruct --dataset sft_vanilla_v4.jsonl\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"257144\", \"log_path\": \"~/runs/tax_error_inject_agent/llama31-vanilla-s0.log\", \"submitted_at\": \"2026-05-16T09:15:54.991Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_count\": 4358, \"data_path\": \"data/mini_pipeline_v4/sft_vanilla_v4.jsonl\", \"model_name\": \"Meta-Llama-3.1-8B-Instruct\", \"seed\": 0, \"wall_clock_seconds\": 4158.6, \"gpu_hours\": 1.16, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/llama31-vanilla-s0/v0-20260516-171603/checkpoint-1635\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T10:26:48.334Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T10:26:50.786934+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/llama31-vanilla-s0/v0-20260516-171603/checkpoint-1635\", \"log_path\": \"/root/runs/tax_error_inject_agent/llama31-vanilla-s0.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T10:29:44.360Z\", \"metrics\": {\"final_train_loss\": 0.398, \"epoch1_loss\": 0.481, \"epoch2_loss\": 0.362, \"epoch3_loss\": 0.273, \"final_token_acc\": 0.909, \"train_runtime_sec\": 4158.6}}, \"eval-rp-s7\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T10:25:59.082Z\", \"updated_at\": \"2026-05-16T10:26:30.070Z\", \"spec\": {\"hypothesis\": \"TaxEI-RP s7 eval - complete 5-seed recovery-paired injection assessment\", \"model_name\": \"Qwen3-8B + TaxEI-RP LoRA\", \"seed\": 7, \"checkpoint_source\": \"/root/autodl-tmp/tax_error_inject_agent/output/v4-taxei-rp-s7/v0-20260516-142303/checkpoint-5415\", \"eval_data\": \"ALFWorld 47 injected tasks\", \"data_path\": \"eval/injected_eval.py (47 ALFWorld tasks)\", \"data_count\": 47, \"command\": \"CUDA_VISIBLE_DEVICES=3 python3 eval/injected_eval.py --model_path output/v4-taxei-rp-s7/v0-20260516-142303/checkpoint-5415 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --model_variant taxei --output_file eval_results/v4_taxei_rp_recovery_eval_s7.json\", \"server\": \"autodl-5090\"}, \"metrics\": {\"recovery_rate\": 0.596, \"recovery_count\": \"28/47\", \"detection_rate\": 0}, \"conclusion\": \"success\", \"log_path\": \"/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_taxei_rp_recovery_eval_s7.json\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/v4-taxei-rp-s7/v0-20260516-142303/checkpoint-5415\", \"completed_at\": \"2026-05-16T10:26:30.070Z\"}, \"v4-taxei-rp-s7\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T06:22:54.703Z\", \"updated_at\": \"2026-05-16T10:15:30.071Z\", \"spec\": {\"command\": \"swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset sft_taxei_rp.jsonl --lora_rank 16 --num_train_epochs 3 --bs 4 --ga 2 --lr 1e-4 --max_length 4096 --seed 7\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/tax_error_inject_agent/data/recovery_paired/sft_taxei_rp.jsonl\", \"data_count\": 14437, \"model_name\": \"Qwen3-8B\", \"seed\": 7, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/v4-taxei-rp-s7/v0-20260516-142303/checkpoint-5415\", \"log_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/v4-taxei-rp-s7/v0-20260516-142303/logging.jsonl\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T10:11:07.987Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T10:11:10.984555+00:00\"}]}, \"metrics\": {\"train_loss\": 0.3855, \"token_acc\": 0.9103, \"duration_minutes\": 226.6, \"peak_memory_gib\": 30.25, \"train_samples_per_second\": 3.185}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T10:14:13.073Z\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/v4-taxei-rp-s7/v0-20260516-142303/checkpoint-5415\"}, \"recovery-taxei-s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T09:40:11.652Z\", \"updated_at\": \"2026-05-16T09:40:44.285Z\", \"spec\": {\"hypothesis\": \"Recovery eval TaxEI s1 - does TaxEI-trained model recover from injected errors?\", \"model_name\": \"Qwen3-8B + TaxEI LoRA\", \"seed\": 1, \"checkpoint_source\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_taxei_sft_v4_seed1/v0-20260515-214035/checkpoint-3387\", \"eval_data\": \"ALFWorld 47 injected tasks\", \"data_path\": \"eval/injected_eval.py (47 ALFWorld tasks)\", \"data_count\": 47, \"command\": \"CUDA_VISIBLE_DEVICES=0 python3 eval/injected_eval.py --model_path checkpoints/mini_taxei_sft_v4_seed1/v0-20260515-214035/checkpoint-3387 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --model_variant taxei --output_file eval_results/v4_taxei_recovery_eval_s1.json\", \"server\": \"autodl-5090\"}, \"metrics\": {\"recovery_rate\": 0.617, \"recovery_count\": \"29/47\", \"detection_rate\": 0, \"C1_context_truncation\": 0.75, \"C4_observation_masking\": 0.636, \"P1_step_order_swap\": 0.583, \"P2_sub_goal_deletion\": 0.5}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_taxei_sft_v4_seed1/v0-20260515-214035/checkpoint-3387\", \"log_path\": \"/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_taxei_recovery_eval_s1.json\", \"completed_at\": \"2026-05-16T09:40:44.285Z\"}, \"llama31-random-s42-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T09:14:41.175Z\", \"updated_at\": \"2026-05-16T09:15:28.130Z\", \"spec\": {\"hypothesis\": \"Cross-model: LLaMA Random s42 eval — random injection control on LLaMA\", \"model_name\": \"Meta-Llama-3.1-8B-Instruct + Random LoRA\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/tax_error_inject_agent/output/llama31-random-s42/v0-20260516-142300/checkpoint-3387\", \"eval_data\": \"ALFWorld 47 injected tasks\", \"data_path\": \"eval/injected_eval.py (47 ALFWorld tasks)\", \"data_count\": 47, \"command\": \"CUDA_VISIBLE_DEVICES=2 python3 eval/injected_eval.py --model_path output/llama31-random-s42/v0-20260516-142300/checkpoint-3387 --base_model /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct --model_variant random --output_file eval_results/llama31_random_s42.json\", \"server\": \"autodl-5090\"}, \"metrics\": {\"recovery_rate\": 0.766, \"recovery_count\": \"36/47\", \"detection_rate\": 0.298, \"C1_context_truncation\": 0.667, \"C4_observation_masking\": 0.727, \"P1_step_order_swap\": 0.917, \"P2_sub_goal_deletion\": 0.75, \"C1_detection\": 0.417, \"C4_detection\": 0.364, \"P1_detection\": 0.333, \"P2_detection\": 0.083}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/llama31-random-s42/v0-20260516-142300/checkpoint-3387\", \"log_path\": \"/root/autodl-tmp/tax_error_inject_agent/eval_results/llama31_random_s42.json\", \"completed_at\": \"2026-05-16T09:15:28.130Z\"}, \"llama31-taxei-s42-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T09:14:40.025Z\", \"updated_at\": \"2026-05-16T09:15:26.908Z\", \"spec\": {\"hypothesis\": \"Cross-model: LLaMA TaxEI s42 eval — does taxonomy-guided injection help on LLaMA?\", \"model_name\": \"Meta-Llama-3.1-8B-Instruct + TaxEI LoRA\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/tax_error_inject_agent/output/llama31-taxei-s42/v0-20260516-142258/checkpoint-3387\", \"eval_data\": \"ALFWorld 47 injected tasks\", \"data_path\": \"eval/injected_eval.py (47 ALFWorld tasks)\", \"data_count\": 47, \"command\": \"CUDA_VISIBLE_DEVICES=1 python3 eval/injected_eval.py --model_path output/llama31-taxei-s42/v0-20260516-142258/checkpoint-3387 --base_model /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct --model_variant taxei --output_file eval_results/llama31_taxei_s42.json\", \"server\": \"autodl-5090\"}, \"metrics\": {\"recovery_rate\": 0.745, \"recovery_count\": \"35/47\", \"detection_rate\": 0.298, \"C1_context_truncation\": 0.833, \"C4_observation_masking\": 0.727, \"P1_step_order_swap\": 0.583, \"P2_sub_goal_deletion\": 0.833, \"C1_detection\": 0.167, \"C4_detection\": 0.364, \"P1_detection\": 0.25, \"P2_detection\": 0.417}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/llama31-taxei-s42/v0-20260516-142258/checkpoint-3387\", \"log_path\": \"/root/autodl-tmp/tax_error_inject_agent/eval_results/llama31_taxei_s42.json\", \"completed_at\": \"2026-05-16T09:15:26.908Z\"}, \"recovery-vanilla-s7\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T08:53:10.619Z\", \"updated_at\": \"2026-05-16T08:53:54.916Z\", \"spec\": {\"hypothesis\": \"Recovery eval Vanilla s7 - confirm Recovery≈Resilience\", \"model_name\": \"Qwen3-8B + Vanilla LoRA\", \"seed\": 7, \"checkpoint_source\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_vanilla_sft_v4_seed7/v1-20260515-214032/checkpoint-1635\", \"eval_data\": \"ALFWorld 47 injected tasks\", \"data_path\": \"eval/injected_eval.py (47 ALFWorld tasks)\", \"data_count\": 47, \"command\": \"CUDA_VISIBLE_DEVICES=0 python3 eval/injected_eval.py --model_path checkpoints/mini_vanilla_sft_v4_seed7/v1-20260515-214032/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --model_variant vanilla --output_file eval_results/v4_vanilla_recovery_eval_s7.json\", \"server\": \"autodl-5090\"}, \"conclusion\": \"success\", \"metrics\": {\"recovery_rate\": 0.745, \"recovery_count\": \"35/47\", \"detection_rate\": 0, \"C1_context_truncation\": 0.75, \"C4_observation_masking\": 0.727, \"P1_step_order_swap\": 0.75, \"P2_sub_goal_deletion\": 0.75}, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_vanilla_sft_v4_seed7/v1-20260515-214032/checkpoint-1635\", \"log_path\": \"/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_vanilla_recovery_eval_s7.json\", \"completed_at\": \"2026-05-16T08:53:54.916Z\"}, \"recovery-vanilla-s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T08:26:23.215Z\", \"updated_at\": \"2026-05-16T08:49:34.621Z\", \"spec\": {\"hypothesis\": \"Recovery eval Vanilla s1 - confirm Recovery≈Resilience\", \"model_name\": \"Qwen3-8B + Vanilla LoRA\", \"seed\": 1, \"checkpoint_source\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_vanilla_sft_v4_seed1/v0-20260515-214031/checkpoint-1635\", \"eval_data\": \"ALFWorld 47 injected tasks\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T08:32:46.932Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T08:32:48.721Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T08:32:54.320388+00:00\"}]}, \"metrics\": {\"recovery_rate\": 0.66, \"recovery_count\": \"31/47\", \"detection_rate\": 0, \"C1_context_truncation\": 0.667, \"C4_observation_masking\": 0.545, \"P1_step_order_swap\": 0.667, \"P2_sub_goal_deletion\": 0.75}}, \"llama31-random-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T06:22:51.516Z\", \"updated_at\": \"2026-05-16T08:46:26.260Z\", \"spec\": {\"data_path\": \"/root/autodl-tmp/tax_error_inject_agent/data/mini_pipeline_v4/sft_random_v4.jsonl\", \"data_count\": 9029, \"model_name\": \"Meta-Llama-3.1-8B-Instruct\", \"seed\": 42, \"hypothesis\": \"Cross-model generalizability: LLaMA-3.1-8B Random condition control\", \"command\": \"llamafactory train\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:2\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/llama31-random-s42/v0-20260516-142300/checkpoint-3387/\", \"log_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/llama31-random-s42/v0-20260516-142300/logging.jsonl\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T08:32:16.672Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T08:32:20.396930+00:00\"}]}, \"metrics\": {\"train_loss\": 0.3366, \"token_acc\": 0.9364, \"train_steps\": 3387, \"train_duration_s\": 7622}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T08:39:26.528Z\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/llama31-random-s42/v0-20260516-142300/checkpoint-3387\"}, \"llama31-taxei-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T06:22:49.346Z\", \"updated_at\": \"2026-05-16T08:46:25.092Z\", \"spec\": {\"data_path\": \"/root/autodl-tmp/tax_error_inject_agent/data/mini_pipeline_v4/sft_taxei_v4.jsonl\", \"data_count\": 9029, \"model_name\": \"Meta-Llama-3.1-8B-Instruct\", \"seed\": 42, \"hypothesis\": \"Cross-model generalizability: LLaMA-3.1-8B TaxEI condition to verify Qwen3-8B findings transfer\", \"command\": \"swift sft --model /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct --dataset sft_taxei_v4.jsonl --lora_rank 16 --num_train_epochs 3 --bs 4 --ga 2 --lr 1e-4 --max_length 4096 --seed 42\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/llama31-taxei-s42/v0-20260516-142258/checkpoint-3387\", \"log_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/llama31-taxei-s42/v0-20260516-142258/logging.jsonl\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T08:36:00.235Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T08:36:05.288585+00:00\"}]}, \"metrics\": {\"train_loss\": 0.3366, \"token_acc\": 0.9357, \"train_steps\": 3387, \"train_duration_s\": 7782}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T08:39:34.756Z\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/llama31-taxei-s42/v0-20260516-142258/checkpoint-3387\"}, \"llama31-vanilla-s42-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T08:07:12.328Z\", \"updated_at\": \"2026-05-16T08:36:24.810Z\", \"spec\": {\"hypothesis\": \"LLaMA-3.1-8B Vanilla s42 injected eval - cross-model baseline\", \"model_name\": \"LLaMA-3.1-8B-Instruct + Vanilla LoRA\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/tax_error_inject_agent/output/llama31-vanilla-s42/v0-20260516-143227/checkpoint-1635\", \"eval_data\": \"ALFWorld 47 injected tasks\"}, \"metrics\": {\"recovery_rate\": 0.745, \"recovery_count\": \"35/47\", \"detection_rate\": 0.213, \"C1_context_truncation\": 0.75, \"C4_observation_masking\": 0.727, \"P1_step_order_swap\": 0.75, \"P2_sub_goal_deletion\": 0.75}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/llama31-vanilla-s42/v0-20260516-143227/checkpoint-1635\", \"log_path\": \"~/runs/tax_error_inject_agent/llama31-vanilla-s42-eval.log\", \"completed_at\": \"2026-05-16T08:36:24.810Z\"}, \"llama31-vanilla-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T06:32:19.082Z\", \"updated_at\": \"2026-05-16T07:48:06.140Z\", \"spec\": {\"command\": \"swift sft --model Meta-Llama-3.1-8B-Instruct --dataset sft_vanilla_v4.jsonl --lora_rank 16 --epochs 3 --bs 4 --ga 2 --lr 1e-4 --max_length 4096 --seed 42\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"pid\": \"244644\", \"log_path\": \"~/runs/tax_error_inject_agent/llama31-vanilla-s42.log\", \"submitted_at\": \"2026-05-16T06:32:18.732Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/tax_error_inject_agent/data/mini_pipeline_v4/sft_vanilla_v4.jsonl\", \"data_count\": 9029, \"model_name\": \"Meta-Llama-3.1-8B-Instruct\", \"seed\": 42, \"hypothesis\": \"Cross-model generalizability: LLaMA-3.1-8B Vanilla baseline\", \"wall_clock_seconds\": 4547.4, \"gpu_hours\": 1.26}, \"reproduce\": {\"finished_at\": \"2026-05-16T07:44:55.468Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T07:44:59.077032+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/llama31-vanilla-s42/v0-20260516-143227/checkpoint-1635\", \"metrics\": {\"train_loss\": 0.40025, \"token_acc\": 0.9067, \"train_steps\": 1635, \"train_duration_s\": 4157}, \"conclusion\": \"success\", \"log_path\": \"~/runs/tax_error_inject_agent/llama31-vanilla-s42.log\", \"completed_at\": \"2026-05-16T07:48:06.140Z\"}, \"eval-rp-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T06:32:34.645Z\", \"updated_at\": \"2026-05-16T06:33:18.281Z\", \"spec\": {\"hypothesis\": \"TaxEI-RP recovery eval seed=42\", \"model_name\": \"Qwen3-8B + TaxEI-RP LoRA\", \"seed\": 42, \"command\": \"python eval/injected_eval.py --model_path v4-taxei-rp-s42 checkpoint --model_variant taxei --seed 42\", \"server\": \"autodl-5090\", \"data_path\": \"ALFWorld injected tasks\", \"data_count\": 47, \"gpu\": \"cuda:0\"}, \"metrics\": {\"recovery_rate\": 0.383, \"recovery_count\": \"18/47\", \"C1_context_truncation\": 0.5, \"C4_observation_masking\": 0.273, \"P1_step_order_swap\": 0.5, \"P2_sub_goal_deletion\": 0.25, \"detection_rate\": 0}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/v4-taxei-rp-s42/v0-20260516-101703/checkpoint-5415\", \"log_path\": \"/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_taxei_rp_s42_injected.json\", \"completed_at\": \"2026-05-16T06:33:18.281Z\"}, \"eval-rp-s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T06:27:34.660Z\", \"updated_at\": \"2026-05-16T06:30:59.753Z\", \"failure_reason\": \"\", \"conclusion\": \"success\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T06:27:37.861045+00:00\"}]}, \"metrics\": {\"recovery_rate\": 0.489, \"detection_rate\": 0, \"episodes\": 47, \"recovered\": 23}, \"spec\": {\"command\": \"python eval_recovery.py --seed 1\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/tax_error_inject_agent/data/recovery_paired/\", \"data_count\": 47, \"model_name\": \"Qwen3-8B (TaxEI-RP s1)\", \"seed\": 1, \"checkpoint_source\": \"v4-taxei-rp-s1\", \"eval_data\": \"47 ALFWorld clean tasks with error injection\"}, \"log_path\": \"/tmp/eval_rp_s1.log\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/eval_outputs/v4_taxei_rp_s1_injected.json\", \"completed_at\": \"2026-05-16T06:30:48.894Z\"}, \"eval-rp-s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T06:27:52.208Z\", \"updated_at\": \"2026-05-16T06:30:58.894Z\", \"failure_reason\": \"\", \"conclusion\": \"success\", \"reproduce\": {\"finished_at\": \"2026-05-16T06:27:54.715Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T06:28:01.102430+00:00\"}]}, \"metrics\": {\"recovery_rate\": 0.468, \"detection_rate\": 0, \"episodes\": 47, \"recovered\": 22}, \"spec\": {\"command\": \"python eval_recovery.py --seed 0\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/tax_error_inject_agent/data/recovery_paired/\", \"data_count\": 47, \"model_name\": \"Qwen3-8B (TaxEI-RP s0)\", \"seed\": 0, \"checkpoint_source\": \"v4-taxei-rp-s0\", \"eval_data\": \"47 ALFWorld clean tasks with error injection\"}, \"log_path\": \"/tmp/eval_rp_s0.log\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/eval_outputs/v4_taxei_rp_s0_injected.json\", \"completed_at\": \"2026-05-16T06:30:47.736Z\"}, \"eval-rp-s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T06:27:26.558Z\", \"updated_at\": \"2026-05-16T06:30:58.290Z\", \"failure_reason\": \"\", \"conclusion\": \"success\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T06:27:29.414786+00:00\"}]}, \"metrics\": {\"recovery_rate\": 0.574, \"detection_rate\": 0, \"episodes\": 47, \"recovered\": 27}, \"spec\": {\"command\": \"python eval_recovery.py --seed 123\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/tax_error_inject_agent/data/recovery_paired/\", \"data_count\": 47, \"model_name\": \"Qwen3-8B (TaxEI-RP s123)\", \"seed\": 123, \"checkpoint_source\": \"v4-taxei-rp-s123\", \"eval_data\": \"47 ALFWorld clean tasks with error injection\"}, \"log_path\": \"/tmp/eval_rp_s123.log\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/eval_outputs/v4_taxei_rp_s123_injected.json\", \"completed_at\": \"2026-05-16T06:30:46.571Z\"}, \"v4-taxei-rp-s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T02:16:59.271Z\", \"updated_at\": \"2026-05-16T06:15:41.090Z\", \"spec\": {\"command\": \"swift sft --model Qwen3-8B --dataset sft_taxei_rp.jsonl --lora_rank 16 --epochs 3 --bs 4 --ga 2 --lr 1e-4 --max_length 4096 --seed 123\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"223254\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-rp-s123.log\", \"submitted_at\": \"2026-05-16T02:16:58.962Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/tax_error_inject_agent/data/recovery_paired/sft_taxei_rp.jsonl\", \"data_count\": 14437, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"hypothesis\": \"Recovery-paired training multi-seed replication (seed=123)\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/v4-taxei-rp-s123/v0-20260516-101708/checkpoint-5415\", \"wall_clock_seconds\": 13954.9, \"gpu_hours\": 3.88}, \"reproduce\": {\"finished_at\": \"2026-05-16T06:05:08.878Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T06:05:14.118671+00:00\"}]}, \"metrics\": {\"train_loss\": 0.38524182, \"eval_loss\": null, \"duration_minutes\": 226.5, \"token_acc\": 0.91372913, \"train_samples_per_second\": 3.187, \"peak_memory_gib\": 30.66}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T06:09:33.865Z\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/v4-taxei-rp-s123/v0-20260516-101708/checkpoint-5415\"}, \"v4-taxei-rp-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T02:16:54.022Z\", \"updated_at\": \"2026-05-16T06:15:40.096Z\", \"spec\": {\"command\": \"swift sft --model Qwen3-8B --dataset sft_taxei_rp.jsonl --lora_rank 16 --epochs 3 --bs 4 --ga 2 --lr 1e-4 --max_length 4096 --seed 42\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"222969\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-rp-s42.log\", \"submitted_at\": \"2026-05-16T02:16:53.716Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/tax_error_inject_agent/data/recovery_paired/sft_taxei_rp.jsonl\", \"data_count\": 14437, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"hypothesis\": \"If recovery-paired training (TaxEI-RP) also fails to improve over Vanilla, task structure is the primary factor. If it works, recovery pairing is the key missing ingredient from PALADIN.\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/v4-taxei-rp-s42/v0-20260516-101703/checkpoint-5415\", \"wall_clock_seconds\": 13958.9, \"gpu_hours\": 3.88}, \"reproduce\": {\"finished_at\": \"2026-05-16T06:04:57.317Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T06:04:59.869491+00:00\"}]}, \"metrics\": {\"train_loss\": 0.38469276, \"eval_loss\": null, \"duration_minutes\": 226.67, \"token_acc\": 0.92487562, \"train_samples_per_second\": 3.185, \"peak_memory_gib\": 30.68}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T06:09:32.658Z\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/v4-taxei-rp-s42/v0-20260516-101703/checkpoint-5415\"}, \"v4-taxei-rp-s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T02:18:24.897Z\", \"updated_at\": \"2026-05-16T06:15:38.814Z\", \"spec\": {\"command\": \"swift sft --model Qwen3-8B --dataset sft_taxei_rp.jsonl --lora_rank 16 --epochs 3 --bs 4 --ga 2 --lr 1e-4 --max_length 4096 --seed 1\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"224231\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-rp-s1.log\", \"submitted_at\": \"2026-05-16T02:18:24.590Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/tax_error_inject_agent/data/recovery_paired/sft_taxei_rp.jsonl\", \"data_count\": 14437, \"model_name\": \"Qwen3-8B\", \"seed\": 1, \"hypothesis\": \"Recovery-paired training multi-seed replication (seed=1)\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/v4-taxei-rp-s1/v0-20260516-101834/checkpoint-5415\", \"wall_clock_seconds\": 13870.4, \"gpu_hours\": 3.85}, \"reproduce\": {\"finished_at\": \"2026-05-16T06:05:21.988Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T06:05:27.447822+00:00\"}]}, \"metrics\": {\"train_loss\": 0.38530399, \"eval_loss\": null, \"duration_minutes\": 226.3, \"token_acc\": 0.91761223, \"train_samples_per_second\": 3.19, \"peak_memory_gib\": 30.17}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T06:09:35.005Z\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/v4-taxei-rp-s1/v0-20260516-101834/checkpoint-5415\"}, \"v4-taxei-rp-s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T02:16:56.691Z\", \"updated_at\": \"2026-05-16T06:15:37.765Z\", \"spec\": {\"command\": \"swift sft --model Qwen3-8B --dataset sft_taxei_rp.jsonl --lora_rank 16 --epochs 3 --bs 4 --ga 2 --lr 1e-4 --max_length 4096 --seed 0\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"223049\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-rp-s0.log\", \"submitted_at\": \"2026-05-16T02:16:56.390Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/tax_error_inject_agent/data/recovery_paired/sft_taxei_rp.jsonl\", \"data_count\": 14437, \"model_name\": \"Qwen3-8B\", \"seed\": 0, \"hypothesis\": \"Recovery-paired training multi-seed replication (seed=0)\", \"wall_clock_seconds\": 14321.4, \"gpu_hours\": 3.98}, \"reproduce\": {\"finished_at\": \"2026-05-16T06:10:47.000Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T06:10:49.871145+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.3847, \"token_acc\": 0.9065, \"duration_min\": 231.07, \"peak_memory_gib\": 30.37, \"train_samples_per_second\": 3.124}, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/output/v4-taxei-rp-s0/v0-20260516-101706/checkpoint-5415\", \"log_path\": \"/root/runs/tax_error_inject_agent/v4-taxei-rp-s0.log\", \"completed_at\": \"2026-05-16T06:15:37.765Z\"}, \"v4-taxei-recovery-eval-s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T12:43:43.113Z\", \"updated_at\": \"2026-05-16T03:23:08.899Z\", \"spec\": {\"checkpoint_path\": \"eval_results/v4_taxei_recovery_eval_s123.json\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-recovery-eval-s123.log\"}, \"metrics\": {\"recovery_rate\": 0.617, \"successes\": 29, \"total\": 47, \"detection_rate\": 0}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T03:23:08.899Z\"}, \"v4-taxei-recovery-eval-s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T12:43:41.449Z\", \"updated_at\": \"2026-05-16T03:23:07.706Z\", \"spec\": {\"checkpoint_path\": \"eval_results/v4_taxei_recovery_eval_s0.json\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-recovery-eval-s0.log\"}, \"metrics\": {\"recovery_rate\": 0.468, \"successes\": 22, \"total\": 47, \"detection_rate\": 0}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T03:23:07.706Z\"}, \"v4-vanilla-recovery-eval-s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T12:43:39.466Z\", \"updated_at\": \"2026-05-16T03:23:06.630Z\", \"spec\": {\"checkpoint_path\": \"eval_results/v4_vanilla_recovery_eval_s123.json\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-vanilla-recovery-eval-s123.log\"}, \"metrics\": {\"recovery_rate\": 0.66, \"successes\": 31, \"total\": 47, \"detection_rate\": 0}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T03:23:06.630Z\"}, \"v4-vanilla-recovery-eval-s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T12:43:38.052Z\", \"updated_at\": \"2026-05-16T03:23:05.513Z\", \"spec\": {\"checkpoint_path\": \"eval_results/v4_vanilla_recovery_eval_s0.json\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-vanilla-recovery-eval-s0.log\"}, \"metrics\": {\"recovery_rate\": 0.681, \"successes\": 32, \"total\": 47, \"detection_rate\": 0}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T03:23:05.513Z\"}, \"v4-random-fixed-inject50-s1-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:09:38.067Z\", \"updated_at\": \"2026-05-16T01:31:24.055Z\", \"spec\": {\"command\": \"python3 eval/recovery.py --model_path checkpoints/v4_random_fixed_inject50_s1/v1-20260516-075754/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --task_list eval/eval_tasks_47.json --num_episodes 47 --seed 42 --device cuda:0 --output eval_results/v4_random_fixed_inject50_s1_eval.json\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"data_path\": \"eval/eval_tasks_47.json\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (random fixed inject50 s1)\", \"seed\": 42, \"checkpoint_source\": \"v4-random-fixed-inject50-s1\", \"eval_data\": \"eval_tasks_47.json\", \"hypothesis\": \"v4 Random 50% seed=1 eval — 47 ALFWorld clean tasks. Dose-response 5-seed expansion.\"}, \"metrics\": {\"success_rate\": 0.702, \"successes\": 33, \"total\": 47, \"by_task_type\": {\"look_at_obj_in_light\": {\"total\": 6, \"success\": 5, \"rate\": 0.833}, \"pick_and_place_simple\": {\"total\": 8, \"success\": 5, \"rate\": 0.625}, \"pick_clean_then_place_in_recep\": {\"total\": 11, \"success\": 8, \"rate\": 0.727}, \"pick_cool_then_place_in_recep\": {\"total\": 7, \"success\": 4, \"rate\": 0.571}, \"pick_heat_then_place_in_recep\": {\"total\": 8, \"success\": 6, \"rate\": 0.75}, \"pick_two_obj_and_place\": {\"total\": 7, \"success\": 5, \"rate\": 0.714}}}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_random_fixed_inject50_s1_eval.json\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-fixed-inject50-s1-eval.log\", \"completed_at\": \"2026-05-16T01:31:24.055Z\"}, \"v4-taxei-fixed-inject50-s1-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:09:36.875Z\", \"updated_at\": \"2026-05-16T01:31:23.037Z\", \"spec\": {\"command\": \"python3 eval/recovery.py --model_path checkpoints/v4_taxei_fixed_inject50_s1/v0-20260516-075747/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --task_list eval/eval_tasks_47.json --num_episodes 47 --seed 42 --device cuda:0 --output eval_results/v4_taxei_fixed_inject50_s1_eval.json\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"data_path\": \"eval/eval_tasks_47.json\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (taxei fixed inject50 s1)\", \"seed\": 42, \"checkpoint_source\": \"v4-taxei-fixed-inject50-s1\", \"eval_data\": \"eval_tasks_47.json\", \"hypothesis\": \"v4 TaxEI 50% seed=1 eval — 47 ALFWorld clean tasks. Dose-response 5-seed expansion.\"}, \"metrics\": {\"success_rate\": 0.638, \"successes\": 30, \"total\": 47, \"by_task_type\": {\"look_at_obj_in_light\": {\"total\": 6, \"success\": 6, \"rate\": 1}, \"pick_and_place_simple\": {\"total\": 8, \"success\": 5, \"rate\": 0.625}, \"pick_clean_then_place_in_recep\": {\"total\": 11, \"success\": 7, \"rate\": 0.636}, \"pick_cool_then_place_in_recep\": {\"total\": 7, \"success\": 4, \"rate\": 0.571}, \"pick_heat_then_place_in_recep\": {\"total\": 8, \"success\": 5, \"rate\": 0.625}, \"pick_two_obj_and_place\": {\"total\": 7, \"success\": 3, \"rate\": 0.429}}}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_taxei_fixed_inject50_s1_eval.json\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-fixed-inject50-s1-eval.log\", \"completed_at\": \"2026-05-16T01:31:23.037Z\"}, \"v4-random-fixed-inject50-s7-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:09:39.957Z\", \"updated_at\": \"2026-05-16T01:21:18.406Z\", \"spec\": {\"command\": \"python3 eval/recovery.py --model_path checkpoints/v4_random_fixed_inject50_s7/v0-20260516-075756/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --task_list eval/eval_tasks_47.json --num_episodes 47 --seed 42 --device cuda:0 --output eval_results/v4_random_fixed_inject50_s7_eval.json\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"data_path\": \"eval/eval_tasks_47.json\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (random fixed inject50 s7)\", \"seed\": 42, \"checkpoint_source\": \"v4-random-fixed-inject50-s7\", \"eval_data\": \"eval_tasks_47.json\", \"hypothesis\": \"v4 Random 50% seed=7 eval — 47 ALFWorld clean tasks. Dose-response 5-seed expansion.\", \"checkpoint_path\": \"checkpoints/v4_random_fixed_inject50_s7/v0-20260516-075756/checkpoint-1635\", \"log_path\": \"eval_results/v4_random_fixed_inject50_s7_eval.json\"}, \"metrics\": {\"success_rate\": 0.468, \"successes\": 22, \"total\": 47, \"by_task_type\": {\"look_at_obj_in_light\": {\"total\": 6, \"success\": 4, \"rate\": 0.667}, \"pick_and_place_simple\": {\"total\": 8, \"success\": 4, \"rate\": 0.5}, \"pick_clean_then_place_in_recep\": {\"total\": 11, \"success\": 5, \"rate\": 0.455}, \"pick_cool_then_place_in_recep\": {\"total\": 7, \"success\": 1, \"rate\": 0.143}, \"pick_heat_then_place_in_recep\": {\"total\": 8, \"success\": 5, \"rate\": 0.625}, \"pick_two_obj_and_place\": {\"total\": 7, \"success\": 3, \"rate\": 0.429}}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T01:21:18.406Z\"}, \"v4-taxei-fixed-inject50-s7-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:09:39.016Z\", \"updated_at\": \"2026-05-16T01:21:17.391Z\", \"spec\": {\"command\": \"python3 eval/recovery.py --model_path checkpoints/v4_taxei_fixed_inject50_s7/v0-20260516-075754/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --task_list eval/eval_tasks_47.json --num_episodes 47 --seed 42 --device cuda:0 --output eval_results/v4_taxei_fixed_inject50_s7_eval.json\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:2\", \"data_path\": \"eval/eval_tasks_47.json\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (taxei fixed inject50 s7)\", \"seed\": 42, \"checkpoint_source\": \"v4-taxei-fixed-inject50-s7\", \"eval_data\": \"eval_tasks_47.json\", \"hypothesis\": \"v4 TaxEI 50% seed=7 eval — 47 ALFWorld clean tasks. Dose-response 5-seed expansion.\", \"checkpoint_path\": \"checkpoints/v4_taxei_fixed_inject50_s7/v0-20260516-075754/checkpoint-1635\", \"log_path\": \"eval_results/v4_taxei_fixed_inject50_s7_eval.json\"}, \"metrics\": {\"success_rate\": 0.553, \"successes\": 26, \"total\": 47, \"by_task_type\": {\"look_at_obj_in_light\": {\"total\": 6, \"success\": 5, \"rate\": 0.833}, \"pick_and_place_simple\": {\"total\": 8, \"success\": 4, \"rate\": 0.5}, \"pick_clean_then_place_in_recep\": {\"total\": 11, \"success\": 6, \"rate\": 0.545}, \"pick_cool_then_place_in_recep\": {\"total\": 7, \"success\": 2, \"rate\": 0.286}, \"pick_heat_then_place_in_recep\": {\"total\": 8, \"success\": 6, \"rate\": 0.75}, \"pick_two_obj_and_place\": {\"total\": 7, \"success\": 3, \"rate\": 0.429}}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T01:21:17.391Z\"}, \"v4-random-fixed-inject50-s7\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T23:58:49.123Z\", \"updated_at\": \"2026-05-16T01:06:27.238Z\", \"spec\": {\"command\": \"swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/ablation_fixed/sft_random_v4_fixed_inject50.jsonl --output_dir checkpoints/v4_random_fixed_inject50_s7 --lora_rank 16 --lora_alpha 32 --num_train_epochs 3 --per_device_train_batch_size 4 --gradient_accumulation_steps 2 --learning_rate 1e-4 --warmup_ratio 0.03 --save_strategy epoch --logging_steps 10 --seed 7 --data_seed 7 --bf16 true\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"data_path\": \"data/mini_pipeline_v4/ablation_fixed/sft_random_v4_fixed_inject50.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 7}, \"hypothesis\": \"v4 Random fixed-size ablation: 50% injection ratio seed=7 (4,358 total). Dose-response 5-seed expansion — Wave 2.\", \"metrics\": {\"train_loss\": 0.4672, \"token_acc\": 0.9156, \"train_runtime_sec\": 3832, \"memory_gib\": 29.94}, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_random_fixed_inject50_s7/v0-20260516-075756/checkpoint-1635\", \"log_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_random_fixed_inject50_s7/v0-20260516-075756/logging.jsonl\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T01:06:27.238Z\"}, \"v4-taxei-fixed-inject50-s7\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T23:58:48.153Z\", \"updated_at\": \"2026-05-16T01:06:25.547Z\", \"spec\": {\"command\": \"swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject50.jsonl --output_dir checkpoints/v4_taxei_fixed_inject50_s7 --lora_rank 16 --lora_alpha 32 --num_train_epochs 3 --per_device_train_batch_size 4 --gradient_accumulation_steps 2 --learning_rate 1e-4 --warmup_ratio 0.03 --save_strategy epoch --logging_steps 10 --seed 7 --data_seed 7 --bf16 true\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:2\", \"data_path\": \"data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject50.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 7}, \"hypothesis\": \"v4 TaxEI fixed-size ablation: 50% injection ratio seed=7 (4,358 total). Dose-response 5-seed expansion — Wave 2.\", \"metrics\": {\"train_loss\": 0.4674, \"token_acc\": 0.9189, \"train_runtime_sec\": 3834, \"memory_gib\": 29.94}, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject50_s7/v0-20260516-075754/checkpoint-1635\", \"log_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject50_s7/v0-20260516-075754/logging.jsonl\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T01:06:25.547Z\"}, \"v4-random-fixed-inject50-s1-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T23:59:00.237Z\", \"updated_at\": \"2026-05-16T01:06:21.982Z\", \"spec\": {\"command\": \"swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/ablation_fixed/sft_random_v4_fixed_inject50.jsonl --output_dir checkpoints/v4_random_fixed_inject50_s1 --lora_rank 16 --lora_alpha 32 --num_train_epochs 3 --per_device_train_batch_size 4 --gradient_accumulation_steps 2 --learning_rate 1e-4 --warmup_ratio 0.03 --save_strategy epoch --logging_steps 10 --seed 1 --data_seed 1 --bf16 true\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"data_path\": \"data/mini_pipeline_v4/ablation_fixed/sft_random_v4_fixed_inject50.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 1}, \"hypothesis\": \"v4 Random fixed-size ablation: 50% injection ratio seed=1 (4,358 total). Dose-response 5-seed expansion — Wave 2. Retry: bs=4, ga=2.\", \"metrics\": {\"train_loss\": 0.4664, \"token_acc\": 0.9012, \"train_runtime_sec\": 3928, \"memory_gib\": 30.37}, \"log_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_random_fixed_inject50_s1/v1-20260516-075754/logging.jsonl\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_random_fixed_inject50_s1/v1-20260516-075754/checkpoint-1635\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T00:03:39.204Z\"}, \"v4-taxei-fixed-inject50-s1-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T23:58:59.221Z\", \"updated_at\": \"2026-05-16T01:05:57.456Z\", \"spec\": {\"command\": \"swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject50.jsonl --output_dir checkpoints/v4_taxei_fixed_inject50_s1 --lora_rank 16 --lora_alpha 32 --num_train_epochs 3 --per_device_train_batch_size 4 --gradient_accumulation_steps 2 --learning_rate 1e-4 --warmup_ratio 0.03 --save_strategy epoch --logging_steps 10 --seed 1 --data_seed 1 --bf16 true\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"data_path\": \"data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject50.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 1}, \"hypothesis\": \"v4 TaxEI fixed-size ablation: 50% injection ratio seed=1 (4,358 total). Dose-response 5-seed expansion — Wave 2. Retry: bs=4, ga=2.\", \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject50_s1/v0-20260516-075747/checkpoint-1635\", \"log_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject50_s1/v0-20260516-075747/logging.jsonl\", \"completed_at\": \"2026-05-16T01:05:15.340Z\", \"metrics\": {\"train_loss\": 0.4667, \"token_acc\": 0.9072, \"train_runtime_sec\": 3858, \"memory_gib\": 30.37}}, \"v4-random-fixed-inject50-s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:58:26.928Z\", \"updated_at\": \"2026-05-15T23:56:49.997Z\", \"hypothesis\": \"v4 Random fixed-size ablation: 50% injection ratio seed=1 (4,358 total). Dose-response 5-seed expansion — Wave 2.\", \"spec\": {\"log_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_random_fixed_inject50_s1/train.log\", \"checkpoint_path\": \"N/A\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T23:55:00.127Z\"}, \"v4-taxei-fixed-inject50-s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:54:03.984Z\", \"updated_at\": \"2026-05-15T23:56:49.235Z\", \"hypothesis\": \"v4 TaxEI fixed-size ablation: 50% injection ratio seed=1 (4,358 total). Dose-response 5-seed expansion — Wave 2.\", \"spec\": {\"log_path\": \"/tmp/v4-taxei-fixed-inject50-s1.log\", \"checkpoint_path\": \"N/A\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T23:55:01.050Z\"}, \"v4-random-fixed-inject25-s7-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:35:00.186Z\", \"updated_at\": \"2026-05-15T23:54:59.193Z\", \"hypothesis\": \"v4 Random 25% seed=7 eval — 47 ALFWorld clean tasks. Dose-response 5-seed expansion.\", \"parent\": \"v4-random-fixed-inject25-s7\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_random_fixed_inject25_s7/v0-20260516-061742/checkpoint-1635\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-fixed-inject25-s7-eval.log\"}, \"metrics\": {\"success_rate\": 0.596, \"successes\": 28, \"total\": 47, \"by_task_type\": {\"look_at_obj_in_light\": {\"total\": 6, \"success\": 4, \"rate\": 0.667}, \"pick_and_place_simple\": {\"total\": 8, \"success\": 5, \"rate\": 0.625}, \"pick_clean_then_place_in_recep\": {\"total\": 11, \"success\": 6, \"rate\": 0.545}, \"pick_cool_then_place_in_recep\": {\"total\": 7, \"success\": 3, \"rate\": 0.429}, \"pick_heat_then_place_in_recep\": {\"total\": 8, \"success\": 6, \"rate\": 0.75}, \"pick_two_obj_and_place\": {\"total\": 7, \"success\": 4, \"rate\": 0.571}}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T23:54:59.193Z\"}, \"v4-taxei-fixed-inject25-s7-eval-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:49:33.992Z\", \"updated_at\": \"2026-05-15T23:54:58.200Z\", \"hypothesis\": \"v4 TaxEI 25% seed=7 eval (retry, cwd fix) — 47 ALFWorld clean tasks. Dose-response 5-seed expansion.\", \"parent\": \"v4-taxei-fixed-inject25-s7\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject25_s7/v0-20260516-053222/checkpoint-1635\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-fixed-inject25-s7-eval-r2.log\"}, \"metrics\": {\"success_rate\": 0.574, \"successes\": 27, \"total\": 47, \"by_task_type\": {\"look_at_obj_in_light\": {\"total\": 6, \"success\": 5, \"rate\": 0.833}, \"pick_and_place_simple\": {\"total\": 8, \"success\": 3, \"rate\": 0.375}, \"pick_clean_then_place_in_recep\": {\"total\": 11, \"success\": 5, \"rate\": 0.455}, \"pick_cool_then_place_in_recep\": {\"total\": 7, \"success\": 3, \"rate\": 0.429}, \"pick_heat_then_place_in_recep\": {\"total\": 8, \"success\": 6, \"rate\": 0.75}, \"pick_two_obj_and_place\": {\"total\": 7, \"success\": 5, \"rate\": 0.714}}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T23:54:58.200Z\"}, \"v4-random-fixed-inject25-s7\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:17:33.574Z\", \"updated_at\": \"2026-05-15T23:19:01.837Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_random_fixed_inject25_s7/v0-20260516-061742/checkpoint-1635\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-fixed-inject25-s7.log\"}, \"hypothesis\": \"v4 Random fixed-size ablation: 25% injection ratio seed=7 (4,358 total = 3,269 clean + 1,089 injected). Dose-response 5-seed expansion.\", \"reproduce\": {\"finished_at\": \"2026-05-15T23:15:25.217Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T23:15:27.886821+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.4254, \"final_step_loss\": 0.265, \"token_acc\": 0.899, \"epochs\": 3, \"steps\": 1635, \"train_runtime_sec\": 3407}, \"completed_at\": \"2026-05-15T23:19:01.837Z\"}, \"v4-recovery-paired-datagen\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:07:23.715Z\", \"updated_at\": \"2026-05-15T23:09:15.501Z\", \"hypothesis\": \"Recovery-paired injection data generation: 711 injected variants × GPT API recovery demos. Each injected trajectory gets a paired recovery continuation from the error state. For recovery-paired SFT training.\", \"metrics\": {\"total_injected_variants\": 760, \"successfully_processed\": 711, \"skipped_no_source_match\": 49, \"operators\": {\"C1_ContextTruncation\": 182, \"C4_ObservationMasking\": 175, \"P1_StepOrderSwap\": 170, \"P2_SubGoalDeletion\": 184}, \"recovery_steps_mean\": 7.6, \"recovery_steps_min\": 1, \"recovery_steps_max\": 46, \"total_recovery_api_calls\": 5408, \"output_file\": \"/root/autodl-tmp/tax_error_inject_agent/data/recovery_paired/recovery_paired.jsonl\", \"output_lines\": 711, \"output_size_mb\": 20.8, \"log_file\": \"/root/autodl-tmp/tax_error_inject_agent/logs/recovery_paired_gen.log\"}, \"spec\": {\"command\": \"python scripts/generate_recovery_paired.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/tax_error_inject_agent/data/mini_pipeline_v2/injected_variants.jsonl\", \"data_count\": 760, \"model_name\": \"gpt-4o\", \"seed\": 42}, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/data/recovery_paired/recovery_paired.jsonl\", \"log_path\": \"/root/autodl-tmp/tax_error_inject_agent/logs/recovery_paired_gen.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T23:09:15.501Z\"}, \"v4-taxei-fixed-inject25-s1-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:34:57.410Z\", \"updated_at\": \"2026-05-15T22:55:45.780Z\", \"hypothesis\": \"v4 TaxEI 25% seed=1 eval — 47 ALFWorld clean tasks. Dose-response 5-seed expansion.\", \"parent\": \"v4-taxei-fixed-inject25-s1\", \"spec\": {\"checkpoint_path\": \"checkpoints/v4_taxei_fixed_inject25_s1/v0-20260516-052917/checkpoint-1635\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-fixed-inject25-s1-eval.log\"}, \"metrics\": {\"success_rate\": 0.638, \"successes\": 30, \"total\": 47, \"eval_split\": \"valid_unseen\", \"by_task_type\": {\"look_at_obj_in_light\": {\"total\": 6, \"success\": 4, \"rate\": 0.667}, \"pick_and_place_simple\": {\"total\": 8, \"success\": 5, \"rate\": 0.625}, \"pick_clean_then_place_in_recep\": {\"total\": 11, \"success\": 6, \"rate\": 0.545}, \"pick_cool_then_place_in_recep\": {\"total\": 7, \"success\": 3, \"rate\": 0.429}, \"pick_heat_then_place_in_recep\": {\"total\": 8, \"success\": 6, \"rate\": 0.75}, \"pick_two_obj_and_place\": {\"total\": 7, \"success\": 6, \"rate\": 0.857}}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T22:55:45.780Z\"}, \"v4-random-fixed-inject25-s1-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:34:59.280Z\", \"updated_at\": \"2026-05-15T22:51:47.662Z\", \"hypothesis\": \"v4 Random 25% seed=1 eval — 47 ALFWorld clean tasks. Dose-response 5-seed expansion.\", \"parent\": \"v4-random-fixed-inject25-s1\", \"spec\": {\"checkpoint_path\": \"checkpoints/v4_random_fixed_inject25_s1/v0-20260516-053219/checkpoint-1635\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-fixed-inject25-s1-eval.log\"}, \"metrics\": {\"success_rate\": 0.723, \"successes\": 34, \"total\": 47, \"by_task_type\": {\"look_at_obj_in_light\": {\"total\": 6, \"success\": 5, \"rate\": 0.833}, \"pick_and_place_simple\": {\"total\": 8, \"success\": 5, \"rate\": 0.625}, \"pick_clean_then_place_in_recep\": {\"total\": 11, \"success\": 7, \"rate\": 0.636}, \"pick_cool_then_place_in_recep\": {\"total\": 7, \"success\": 4, \"rate\": 0.571}, \"pick_heat_then_place_in_recep\": {\"total\": 8, \"success\": 7, \"rate\": 0.875}, \"pick_two_obj_and_place\": {\"total\": 7, \"success\": 6, \"rate\": 0.857}}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T22:51:47.662Z\"}, \"v4-taxei-fixed-inject25-s7-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:34:58.385Z\", \"updated_at\": \"2026-05-15T22:49:15.451Z\", \"hypothesis\": \"v4 TaxEI 25% seed=7 eval — 47 ALFWorld clean tasks. Dose-response 5-seed expansion.\", \"parent\": \"v4-taxei-fixed-inject25-s7\", \"spec\": {\"command\": \"python3 eval/recovery.py --model_path checkpoints/v4_taxei_fixed_inject25_s7/v0-20260516-053222/checkpoint-1635 --num_episodes 47 --seed 42\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"unknown\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-fixed-inject25-s7-eval.log\", \"submitted_at\": \"2026-05-15T22:45:20.960Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"eval/eval_tasks_47.json\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (taxei fixed inject25 s7)\", \"seed\": 42, \"checkpoint_source\": \"v4-taxei-fixed-inject25-s7\", \"eval_data\": \"eval_tasks_47.json\", \"wall_clock_seconds\": 67.9, \"gpu_hours\": 0.02}, \"reproduce\": {\"finished_at\": \"2026-05-15T22:46:27.057Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T22:46:28.849Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T22:46:31.066271+00:00\"}]}, \"notes\": \"失败原因: cd /root/tax_error_inject_agent 路径不存在，正确路径为 /root/autodl-tmp/tax_error_inject_agent | 已有成果: 无（启动即失败） | 建议: 修正 cwd 后重试为 v4-taxei-fixed-inject25-s7-eval-r2，等当前 2 个 eval 完成后提交（eval 并行 ≤ 2）\"}, \"v4-taxei-fixed-inject25-s1-eval-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T22:38:37.902Z\", \"updated_at\": \"2026-05-15T22:45:10.397Z\", \"spec\": {\"command\": \"python3 eval/recovery.py --model_path checkpoints/v4_taxei_fixed_inject25_s1/v0-20260516-052917/checkpoint-1635 --num_episodes 47 --seed 42\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"205858\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-fixed-inject25-s1-eval-r2.log\", \"submitted_at\": \"2026-05-15T22:38:37.371Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"eval/eval_tasks_47.json\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (taxei fixed inject25 s1)\", \"seed\": 42, \"checkpoint_source\": \"v4-taxei-fixed-inject25-s1\", \"eval_data\": \"eval_tasks_47.json\", \"wall_clock_seconds\": 393.0, \"gpu_hours\": 0.11}, \"hypothesis\": \"v4 TaxEI 25% seed=1 eval — 47 ALFWorld clean tasks. Dose-response 5-seed expansion.\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T22:45:10.397Z\"}, \"v4-taxei-fixed-inject25-s7\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T21:32:12.446Z\", \"updated_at\": \"2026-05-15T22:33:00.087Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject25_s7/v0-20260516-053222/checkpoint-1635\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-fixed-inject25-s7.log\"}, \"hypothesis\": \"v4 TaxEI fixed-size ablation: 25% injection ratio seed=7 (4,358 total = 3,269 clean + 1,089 injected). Dose-response 5-seed expansion.\", \"reproduce\": {\"finished_at\": \"2026-05-15T22:30:32.348Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T22:30:36.683523+00:00\"}]}, \"metrics\": {\"train_loss\": 0.4242, \"final_step_loss\": 0.2571, \"token_accuracy\": 0.904, \"train_steps\": 1635, \"train_epochs\": 3, \"train_runtime_sec\": 3430.48, \"train_duration_min\": 57.17, \"train_samples_per_second\": 3.811, \"train_steps_per_second\": 0.477, \"memory_gib\": 17.55, \"data_count\": 4358}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T22:32:54.528Z\"}, \"v4-random-fixed-inject25-s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T21:32:10.005Z\", \"updated_at\": \"2026-05-15T22:32:58.843Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_random_fixed_inject25_s1/v0-20260516-053219/checkpoint-1635\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-fixed-inject25-s1.log\"}, \"hypothesis\": \"v4 Random fixed-size ablation: 25% injection ratio seed=1 (4,358 total = 3,269 clean + 1,089 injected). Dose-response 5-seed expansion.\", \"reproduce\": {\"finished_at\": \"2026-05-15T22:30:26.273Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T22:30:28.937887+00:00\"}]}, \"metrics\": {\"train_loss\": 0.4261, \"final_step_loss\": 0.2442, \"token_accuracy\": 0.9123, \"train_steps\": 1635, \"train_epochs\": 3, \"train_runtime_sec\": 3417.56, \"train_duration_min\": 56.96, \"train_samples_per_second\": 3.826, \"train_steps_per_second\": 0.478, \"memory_gib\": 18, \"data_count\": 4358}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T22:32:56.713Z\"}, \"v4-taxei-fixed-inject25-s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T21:29:07.506Z\", \"updated_at\": \"2026-05-15T22:29:56.310Z\", \"spec\": {\"command\": \"swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject25.jsonl --lora_rank 16 --num_train_epochs 3 --seed 1 --data_seed 1 --output_dir checkpoints/v4_taxei_fixed_inject25_s1 --gradient_accumulation_steps 8 --learning_rate 1e-4 --lr_scheduler_type cosine --gradient_checkpointing true --save_strategy epoch --logging_steps 5 --weight_decay 0.1 --adam_beta1 0.9 --adam_beta2 0.95\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"199599\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-fixed-inject25-s1.log\", \"submitted_at\": \"2026-05-15T21:29:07.235Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject25.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 1, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject25_s1/v0-20260516-052917/checkpoint-1635\", \"wall_clock_seconds\": 3649.1, \"gpu_hours\": 1.01}, \"hypothesis\": \"v4 TaxEI fixed-size ablation: 25% injection ratio seed=1 (4,358 total = 3,269 clean + 1,089 injected). Dose-response 5-seed expansion.\", \"reproduce\": {\"finished_at\": \"2026-05-15T22:27:46.845Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T22:27:49.896536+00:00\"}]}, \"metrics\": {\"train_loss\": 0.4243, \"train_duration_min\": 57.5, \"train_steps\": 1635, \"train_epochs\": 3, \"data_count\": 4358}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T22:29:56.310Z\"}, \"v4-random-fixed-inject10-s7-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T21:57:41.705Z\", \"updated_at\": \"2026-05-15T22:15:41.386Z\", \"spec\": {\"command\": \"python3 eval/recovery.py --model_path checkpoints/v4_random_fixed_inject10_s7/v1-20260516-045440/checkpoint-1635 --num_episodes 47 --seed 42\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"202328\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-fixed-inject10-s7-eval.log\", \"submitted_at\": \"2026-05-15T21:57:41.444Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"eval/eval_tasks_47.json\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (random fixed inject10 s7)\", \"seed\": 42, \"checkpoint_source\": \"v4-random-fixed-inject10-s7\", \"eval_data\": \"eval_tasks_47.json\", \"checkpoint_path\": \"checkpoints/v4_random_fixed_inject10_s7/v1-20260516-045440/checkpoint-1635\", \"wall_clock_seconds\": 818, \"gpu_hours\": 0.23}, \"hypothesis\": \"v4 Random 10% seed=7 eval — 47 ALFWorld clean tasks. Dose-response 5-seed expansion. 最后一个 10% eval。\", \"reproduce\": {\"finished_at\": \"2026-05-15T22:12:57.609Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T22:12:59.982752+00:00\"}]}, \"metrics\": {\"success_rate\": 0.617, \"successes\": 29, \"total\": 47, \"by_task_type\": {\"look_at_obj_in_light\": {\"success\": 5, \"total\": 6, \"rate\": 0.833}, \"pick_and_place_simple\": {\"success\": 4, \"total\": 8, \"rate\": 0.5}, \"pick_clean_then_place_in_recep\": {\"success\": 5, \"total\": 11, \"rate\": 0.455}, \"pick_cool_then_place_in_recep\": {\"success\": 4, \"total\": 7, \"rate\": 0.571}, \"pick_heat_then_place_in_recep\": {\"success\": 7, \"total\": 8, \"rate\": 0.875}, \"pick_two_obj_and_place\": {\"success\": 4, \"total\": 7, \"rate\": 0.571}}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T22:15:41.386Z\"}, \"v4-random-fixed-inject10-s7\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:57:08.353Z\", \"updated_at\": \"2026-05-15T21:57:11.016Z\", \"hypothesis\": \"v4 Random fixed-size ablation: 10% injection ratio seed=7 (4,358 total). Dose-response 5-seed expansion — 最后一个 10% 训练。\", \"spec\": {\"data_path\": \"data/mini_pipeline_v4/ablation_fixed/sft_random_v4_fixed_inject10.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B + LoRA (random fixed inject10 s7)\", \"seed\": 7}, \"reproduce\": {\"finished_at\": \"2026-05-15T21:54:51.217Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T21:54:53.698171+00:00\"}]}, \"metrics\": {\"final_loss\": 0.2352, \"train_loss_avg\": 0.4209, \"final_token_acc\": 0.9066, \"total_steps\": 1635, \"epochs\": 3, \"train_runtime_sec\": 3511.93, \"memory_gib\": 18.15, \"train_speed_s_per_it\": 2.148}, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_random_fixed_inject10_s7/v1-20260516-045440/checkpoint-1635\", \"conclusion\": \"success\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-fixed-inject10-s7.log\", \"completed_at\": \"2026-05-15T21:57:11.016Z\"}, \"v4-random-fixed-inject10-s1-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T21:05:18.654Z\", \"updated_at\": \"2026-05-15T21:27:48.360Z\", \"spec\": {\"command\": \"python3 eval/recovery.py --model_path checkpoints/v4_random_fixed_inject10_s1/v1-20260516-040130/checkpoint-1635 --num_episodes 47 --seed 42\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"198045\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-fixed-inject10-s1-eval.log\", \"submitted_at\": \"2026-05-15T21:05:18.393Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"eval/eval_tasks_47.json\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (random fixed inject10 s1)\", \"seed\": 42, \"checkpoint_source\": \"v4-random-fixed-inject10-s1\", \"eval_data\": \"eval_tasks_47.json\", \"checkpoint_path\": \"checkpoints/v4_random_fixed_inject10_s1/v1-20260516-040130/checkpoint-1635\", \"wall_clock_seconds\": 1350.0, \"gpu_hours\": 0.37}, \"hypothesis\": \"v4 Random 10% seed=1 eval — 47 ALFWorld clean tasks. Dose-response 5-seed expansion.\", \"reproduce\": {\"finished_at\": \"2026-05-15T21:25:33.786Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T21:25:36.468478+00:00\"}]}, \"metrics\": {\"success_rate\": 0.681, \"successes\": 32, \"total\": 47, \"by_task_type\": {\"look_at_obj_in_light\": {\"total\": 6, \"success\": 5, \"rate\": 0.833}, \"pick_and_place_simple\": {\"total\": 8, \"success\": 5, \"rate\": 0.625}, \"pick_clean_then_place_in_recep\": {\"total\": 10, \"success\": 5, \"rate\": 0.5}, \"pick_cool_then_place_in_recep\": {\"total\": 7, \"success\": 6, \"rate\": 0.857}, \"pick_heat_then_place_in_recep\": {\"total\": 8, \"success\": 7, \"rate\": 0.875}, \"pick_two_obj_and_place\": {\"total\": 7, \"success\": 4, \"rate\": 0.571}}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T21:27:48.360Z\"}, \"v4-taxei-fixed-inject10-s7-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T21:02:22.234Z\", \"updated_at\": \"2026-05-15T21:27:44.185Z\", \"spec\": {\"command\": \"python3 eval/recovery.py --model_path checkpoints/v4_taxei_fixed_inject10_s7/v1-20260516-040128/checkpoint-1635 --num_episodes 47 --seed 42\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"197555\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-fixed-inject10-s7-eval.log\", \"submitted_at\": \"2026-05-15T21:02:21.785Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"eval/eval_tasks_47.json\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (taxei fixed inject10 s7)\", \"seed\": 42, \"checkpoint_source\": \"v4-taxei-fixed-inject10-s7\", \"eval_data\": \"eval_tasks_47.json\", \"wall_clock_seconds\": 1522.4, \"gpu_hours\": 0.42}, \"hypothesis\": \"v4 TaxEI 10% seed=7 eval — 47 ALFWorld clean tasks. Dose-response 5-seed expansion.\", \"reproduce\": {\"finished_at\": \"2026-05-15T21:19:30.996Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T21:19:33.518373+00:00\"}]}, \"metrics\": {\"success_rate\": 0.681, \"successes\": 32, \"total\": 47, \"by_task_type\": {\"look_at_obj_in_light\": {\"total\": 6, \"success\": 5, \"rate\": 0.833}, \"pick_and_place_simple\": {\"total\": 8, \"success\": 5, \"rate\": 0.625}, \"pick_clean_then_place_in_recep\": {\"total\": 11, \"success\": 7, \"rate\": 0.636}, \"pick_cool_then_place_in_recep\": {\"total\": 7, \"success\": 4, \"rate\": 0.571}, \"pick_heat_then_place_in_recep\": {\"total\": 8, \"success\": 7, \"rate\": 0.875}, \"pick_two_obj_and_place\": {\"total\": 7, \"success\": 4, \"rate\": 0.571}}}, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_taxei_fixed_inject10_s7_eval.json\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T21:27:44.185Z\"}, \"v4-taxei-fixed-inject10-s1-eval-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:54:05.248Z\", \"updated_at\": \"2026-05-15T21:06:11.418Z\", \"spec\": {\"parent\": \"v4-taxei-fixed-inject10-s1\", \"checkpoint_source\": \"v4-taxei-fixed-inject10-s1\", \"eval_data\": \"eval_tasks_47.json\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (taxei fixed inject10 s1)\", \"seed\": 42, \"data_path\": \"eval/eval_tasks_47.json\"}, \"hypothesis\": \"v4 TaxEI 10% seed=1 eval (r2, dedicated GPU) — 47 ALFWorld clean tasks.\", \"reproduce\": {\"finished_at\": \"2026-05-15T21:04:33.190Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T21:04:36.432028+00:00\"}]}, \"metrics\": {\"success_rate\": 0.511, \"successes\": 24, \"total\": 47, \"by_task_type\": {\"look_at_obj_in_light\": {\"total\": 6, \"success\": 4, \"rate\": 0.667}, \"pick_and_place_simple\": {\"total\": 8, \"success\": 4, \"rate\": 0.5}, \"pick_clean_then_place_in_recep\": {\"total\": 11, \"success\": 5, \"rate\": 0.455}, \"pick_cool_then_place_in_recep\": {\"total\": 7, \"success\": 2, \"rate\": 0.286}, \"pick_heat_then_place_in_recep\": {\"total\": 8, \"success\": 6, \"rate\": 0.75}, \"pick_two_obj_and_place\": {\"total\": 7, \"success\": 3, \"rate\": 0.429}}}, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_taxei_fixed_inject10_s1_eval.json\", \"log_path\": \"/root/runs/tax_error_inject_agent/v4-taxei-fixed-inject10-s1-eval-r2.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T21:06:11.418Z\"}, \"v4-taxei-fixed-inject10-s7\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:57:05.524Z\", \"updated_at\": \"2026-05-15T21:05:01.494Z\", \"hypothesis\": \"v4 TaxEI fixed-size ablation: 10% injection ratio seed=7 (4,358 total). Dose-response 5-seed expansion.\", \"spec\": {\"command\": \"swift sft --model Qwen3-8B --dataset sft_taxei_v4_fixed_inject10.jsonl --seed 7\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"191997\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-fixed-inject10-s7.log\", \"submitted_at\": \"2026-05-15T20:01:19.314Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject10.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 7, \"wall_clock_seconds\": 3683.3, \"gpu_hours\": 1.02}, \"reproduce\": {\"finished_at\": \"2026-05-15T20:59:13.748Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T20:59:16.071667+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject10_s7/v1-20260516-040128/checkpoint-1635\", \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.237, \"train_loss_avg\": 0.4212, \"final_token_acc\": 0.905, \"total_steps\": 1635, \"epochs\": 3, \"train_runtime_sec\": 3437, \"memory_gib\": 18.15, \"train_speed_s_per_it\": 2.102}, \"completed_at\": \"2026-05-15T21:02:42.621Z\"}, \"v4-random-fixed-inject10-s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:57:07.390Z\", \"updated_at\": \"2026-05-15T21:04:23.738Z\", \"hypothesis\": \"v4 Random fixed-size ablation: 10% injection ratio seed=1 (4,358 total). Dose-response 5-seed expansion.\", \"spec\": {\"command\": \"swift sft --model Qwen3-8B --dataset sft_random_v4_fixed_inject10.jsonl --seed 1\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"192077\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-fixed-inject10-s1.log\", \"submitted_at\": \"2026-05-15T20:01:21.468Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/mini_pipeline_v4/ablation_fixed/sft_random_v4_fixed_inject10.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 1, \"wall_clock_seconds\": 3782.3, \"gpu_hours\": 1.05}, \"reproduce\": {\"finished_at\": \"2026-05-15T21:01:51.221Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T21:01:53.909162+00:00\"}]}, \"metrics\": {\"final_loss\": 0.3096, \"train_loss_avg\": 0.4238, \"final_token_acc\": 0.8902, \"total_steps\": 1635, \"epochs\": 3, \"train_runtime_sec\": 3488, \"memory_gib\": 18.13, \"train_speed_s_per_it\": 2.132}, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_random_fixed_inject10_s1/v1-20260516-040130/checkpoint-1635\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T21:04:23.738Z\"}, \"v4-taxei-fixed-inject10-s123-eval-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:40:05.773Z\", \"updated_at\": \"2026-05-15T20:54:14.378Z\", \"spec\": {\"command\": \"python3 eval/recovery.py --model_path checkpoints/v4_taxei_fixed_inject10_s123/v0-20260516-014833/checkpoint-1635 --num_episodes 47 --seed 42\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"194978\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-fixed-inject10-s123-eval-r3.log\", \"submitted_at\": \"2026-05-15T20:40:05.519Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"parent\": \"v4-taxei-fixed-inject10-s123\", \"checkpoint_source\": \"v4-taxei-fixed-inject10-s123\", \"eval_data\": \"eval_tasks_47.json\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (taxei fixed inject10 s123)\", \"seed\": 42, \"data_path\": \"eval/eval_tasks_47.json\", \"wall_clock_seconds\": 848.9, \"gpu_hours\": 0.24}, \"hypothesis\": \"v4 TaxEI 10% seed=123 eval (r3, dedicated GPU) — 47 ALFWorld clean tasks.\", \"reproduce\": {\"finished_at\": \"2026-05-15T20:50:16.884Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T20:50:19.215245+00:00\"}]}, \"metrics\": {\"success_rate\": 0.553, \"successes\": 26, \"total\": 47, \"by_task_type\": {\"look_at_obj_in_light\": {\"total\": 6, \"success\": 5, \"rate\": 0.833}, \"pick_and_place_simple\": {\"total\": 8, \"success\": 4, \"rate\": 0.5}, \"pick_clean_then_place_in_recep\": {\"total\": 11, \"success\": 5, \"rate\": 0.455}, \"pick_cool_then_place_in_recep\": {\"total\": 7, \"success\": 2, \"rate\": 0.286}, \"pick_heat_then_place_in_recep\": {\"total\": 8, \"success\": 6, \"rate\": 0.75}, \"pick_two_obj_and_place\": {\"total\": 7, \"success\": 4, \"rate\": 0.571}}}, \"conclusion\": \"success\", \"checkpoint_path\": \"checkpoints/v4_taxei_fixed_inject10_s123/v0-20260516-014833/checkpoint-1635\", \"completed_at\": \"2026-05-15T20:54:14.378Z\"}, \"v4-random-fixed-inject10-s0-eval-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:40:07.402Z\", \"updated_at\": \"2026-05-15T20:52:32.204Z\", \"spec\": {\"command\": \"python3 eval/recovery.py --model_path checkpoints/v4_random_fixed_inject10_s0/v0-20260516-014835/checkpoint-1635 --num_episodes 47 --seed 42\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"195118\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-fixed-inject10-s0-eval-r3.log\", \"submitted_at\": \"2026-05-15T20:40:07.156Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"parent\": \"v4-random-fixed-inject10-s0\", \"checkpoint_source\": \"v4-random-fixed-inject10-s0\", \"eval_data\": \"eval_tasks_47.json\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (random fixed inject10 s0)\", \"seed\": 42, \"data_path\": \"eval/eval_tasks_47.json\", \"wall_clock_seconds\": 745.0, \"gpu_hours\": 0.21}, \"hypothesis\": \"v4 Random 10% seed=0 eval (r3, dedicated GPU) — 47 ALFWorld clean tasks.\", \"reproduce\": {\"finished_at\": \"2026-05-15T20:50:22.439Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T20:50:26.585713+00:00\"}]}, \"metrics\": {\"success_rate\": 0.66, \"successes\": 31, \"total\": 47, \"by_task_type\": {\"look_at_obj_in_light\": {\"success\": 5, \"total\": 6, \"rate\": 0.833}, \"pick_and_place_simple\": {\"success\": 4, \"total\": 8, \"rate\": 0.5}, \"pick_clean_then_place_in_recep\": {\"success\": 7, \"total\": 11, \"rate\": 0.636}, \"pick_cool_then_place_in_recep\": {\"success\": 4, \"total\": 7, \"rate\": 0.571}, \"pick_heat_then_place_in_recep\": {\"success\": 7, \"total\": 8, \"rate\": 0.875}, \"pick_two_obj_and_place\": {\"success\": 4, \"total\": 7, \"rate\": 0.571}}}, \"conclusion\": \"success\", \"checkpoint_path\": \"checkpoints/v4_random_fixed_inject10_s0/v0-20260516-014835/checkpoint-1635\", \"completed_at\": \"2026-05-15T20:52:32.204Z\"}, \"v4-random-fixed-inject10-s0-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:57:43.603Z\", \"updated_at\": \"2026-05-15T20:04:12.753Z\", \"spec\": {\"command\": \"eval\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"188022\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-fixed-inject10-s0-eval.log\", \"submitted_at\": \"2026-05-15T18:57:43.056Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"parent\": \"v4-random-fixed-inject10-s0\", \"checkpoint_source\": \"v4-random-fixed-inject10-s0\", \"eval_data\": \"valid_unseen\", \"data_count\": 47, \"data_path\": \"N/A\", \"model_name\": \"v4_random_fixed_inject10_s0\", \"seed\": 0, \"wall_clock_seconds\": 3975.6, \"gpu_hours\": 1.1}, \"hypothesis\": \"v4 Random 10% seed=0 eval — 47 ALFWorld clean tasks. Dose-response 5-seed expansion.\", \"conclusion\": \"failed\", \"checkpoint_path\": \"N/A-OOM\", \"completed_at\": \"2026-05-15T20:03:58.662Z\", \"metrics\": {\"error\": \"CUDA OOM during model loading on GPU 0\"}}, \"v4-taxei-fixed-inject10-s123-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:57:41.337Z\", \"updated_at\": \"2026-05-15T20:04:11.865Z\", \"spec\": {\"command\": \"eval\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"187785\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-fixed-inject10-s123-eval.log\", \"submitted_at\": \"2026-05-15T18:57:40.646Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"parent\": \"v4-taxei-fixed-inject10-s123\", \"checkpoint_source\": \"v4-taxei-fixed-inject10-s123\", \"eval_data\": \"valid_unseen\", \"data_count\": 47, \"data_path\": \"N/A\", \"model_name\": \"v4_taxei_fixed_inject10_s123\", \"seed\": 123, \"wall_clock_seconds\": 3977.2, \"gpu_hours\": 1.1}, \"hypothesis\": \"v4 TaxEI 10% seed=123 eval — 47 ALFWorld clean tasks. Dose-response 5-seed expansion.\", \"conclusion\": \"failed\", \"checkpoint_path\": \"N/A-OOM\", \"completed_at\": \"2026-05-15T20:03:57.889Z\", \"metrics\": {\"error\": \"CUDA OOM during model loading on GPU 0\"}}, \"v4-taxei-fixed-inject10-s1-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:57:45.002Z\", \"updated_at\": \"2026-05-15T20:04:10.985Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && python3 eval/recovery.py --model_path /root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject10_s1/v0-20260516-015427/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --task_list eval/eval_tasks_47.json --num_episodes 47 --seed 42 --device cuda:0 --output eval_results/v4_taxei_fixed_inject10_s1_eval.json\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"188906\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-fixed-inject10-s1-eval.log\", \"submitted_at\": \"2026-05-15T18:57:44.756Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"parent\": \"v4-taxei-fixed-inject10-s1\", \"checkpoint_source\": \"v4-taxei-fixed-inject10-s1\", \"eval_data\": \"eval_tasks_47.json\", \"data_count\": 47, \"data_path\": \"eval/eval_tasks_47.json\", \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"wall_clock_seconds\": 3927.9, \"gpu_hours\": 1.09}, \"hypothesis\": \"v4 TaxEI 10% seed=1 eval — 47 ALFWorld clean tasks. Dose-response 5-seed expansion.\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T20:03:12.659Z\", \"metrics\": {\"error\": \"CUDA OOM during model loading on GPU 0\"}}, \"v4-random-fixed-inject10-s123-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:59:20.398Z\", \"updated_at\": \"2026-05-15T20:04:09.526Z\", \"hypothesis\": \"v4 Random fixed-size 10% injection seed=123 eval — 47 ALFWorld tasks, dose-response 5-seed expansion\", \"parent\": \"v4-random-fixed-inject10-s123\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && python3 eval/recovery.py --model_path checkpoints/v4_random_fixed_inject10_s123/v0-20260516-015429/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --task_list eval/eval_tasks_47.json --num_episodes 47 --seed 42 --device cuda:0 --output eval_results/v4_random_fixed_inject10_s123_eval.json\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"data_path\": \"eval/eval_tasks_47.json\", \"data_count\": 47, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_source\": \"v4-random-fixed-inject10-s123\", \"eval_data\": \"eval/eval_tasks_47.json\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-fixed-inject10-s123-eval.log\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_random_fixed_inject10_s123_eval.json\", \"completed_at\": \"2026-05-15T20:03:32.060Z\", \"metrics\": {\"success_rate\": 0.553, \"successes\": 26, \"total\": 47, \"by_task_type\": {\"look_at_obj_in_light\": {\"total\": 6, \"success\": 5, \"rate\": 0.833}, \"pick_and_place_simple\": {\"total\": 8, \"success\": 5, \"rate\": 0.625}, \"pick_clean_then_place_in_recep\": {\"total\": 11, \"success\": 5, \"rate\": 0.455}, \"pick_cool_then_place_in_recep\": {\"total\": 7, \"success\": 2, \"rate\": 0.286}, \"pick_heat_then_place_in_recep\": {\"total\": 8, \"success\": 6, \"rate\": 0.75}, \"pick_two_obj_and_place\": {\"total\": 7, \"success\": 3, \"rate\": 0.429}}}}, \"v4-taxei-fixed-inject10-s0-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:57:46.985Z\", \"updated_at\": \"2026-05-15T20:04:06.775Z\", \"spec\": {\"command\": \"eval\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"188410\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-fixed-inject10-s0-eval.log\", \"submitted_at\": \"2026-05-15T18:57:46.725Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"parent\": \"v4-taxei-fixed-inject10-s0\", \"checkpoint_source\": \"v4-taxei-fixed-inject10-s0\", \"eval_data\": \"valid_unseen\", \"data_count\": 47, \"data_path\": \"eval_results/v4_taxei_fixed_inject10_s0_eval.json\", \"model_name\": \"v4_taxei_fixed_inject10_s0\", \"seed\": 0, \"wall_clock_seconds\": 3970.2, \"gpu_hours\": 1.1}, \"hypothesis\": \"v4 TaxEI 10% seed=0 eval — 47 ALFWorld clean tasks. Dose-response 5-seed expansion.\", \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_taxei_fixed_inject10_s0_eval.json\", \"completed_at\": \"2026-05-15T20:03:56.888Z\", \"metrics\": {\"success_rate\": 0.702, \"successes\": 33, \"total\": 47, \"by_task_type\": {\"look_at_obj_in_light\": {\"total\": 6, \"success\": 5, \"rate\": 0.833}, \"pick_and_place_simple\": {\"total\": 8, \"success\": 5, \"rate\": 0.625}, \"pick_clean_then_place_in_recep\": {\"total\": 11, \"success\": 8, \"rate\": 0.727}, \"pick_cool_then_place_in_recep\": {\"total\": 7, \"success\": 4, \"rate\": 0.571}, \"pick_heat_then_place_in_recep\": {\"total\": 8, \"success\": 7, \"rate\": 0.875}, \"pick_two_obj_and_place\": {\"total\": 7, \"success\": 4, \"rate\": 0.571}}}}, \"v4-taxei-fixed-inject10-s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:54:17.800Z\", \"updated_at\": \"2026-05-15T18:57:47.705Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject10.jsonl --lora_rank 16 --num_train_epochs 3 --seed 1 --data_seed 1 --output_dir checkpoints/v4_taxei_fixed_inject10_s1 --gradient_accumulation_steps 8 --learning_rate 1e-4 --lr_scheduler_type cosine --gradient_checkpointing true --save_strategy epoch --logging_steps 5 --weight_decay 0.1 --adam_beta1 0.9 --adam_beta2 0.95\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"182703\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-fixed-inject10-s1.log\", \"submitted_at\": \"2026-05-15T17:54:17.595Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject10.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 1, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject10_s1/v0-20260516-015427/checkpoint-1635\", \"wall_clock_seconds\": 3728.4, \"gpu_hours\": 1.04}, \"hypothesis\": \"v4 TaxEI fixed-size ablation: 10% injection ratio seed=1 (4,358 total). Dose-response 5-seed expansion.\", \"reproduce\": {\"finished_at\": \"2026-05-15T18:53:12.812Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T18:53:14.974953+00:00\"}]}, \"metrics\": {\"final_loss\": 0.3013, \"train_loss_avg\": 0.4225, \"final_token_acc\": 0.8947, \"total_steps\": 1635, \"epochs\": 3, \"train_runtime_sec\": 3469, \"memory_gib\": 18.13, \"train_speed_s_per_it\": 2.121}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T18:56:25.993Z\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject10_s1/v0-20260516-015427/checkpoint-1635\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-fixed-inject10-s1.log\"}, \"v4-random-fixed-inject10-s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:54:20.390Z\", \"updated_at\": \"2026-05-15T18:57:42.428Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/ablation_fixed/sft_random_v4_fixed_inject10.jsonl --lora_rank 16 --num_train_epochs 3 --seed 123 --data_seed 123 --output_dir checkpoints/v4_random_fixed_inject10_s123 --gradient_accumulation_steps 8 --learning_rate 1e-4 --lr_scheduler_type cosine --gradient_checkpointing true --save_strategy epoch --logging_steps 5 --weight_decay 0.1 --adam_beta1 0.9 --adam_beta2 0.95\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"182781\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-fixed-inject10-s123.log\", \"submitted_at\": \"2026-05-15T17:54:20.028Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/mini_pipeline_v4/ablation_fixed/sft_random_v4_fixed_inject10.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"wall_clock_seconds\": 3802.4, \"gpu_hours\": 1.06}, \"hypothesis\": \"v4 Random fixed-size ablation: 10% injection ratio seed=123 (4,358 total). Dose-response 5-seed expansion.\", \"reproduce\": {\"finished_at\": \"2026-05-15T18:54:38.478Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T18:54:40.603963+00:00\"}]}, \"metrics\": {\"final_loss\": 0.3124, \"train_loss_avg\": 0.4236, \"final_token_acc\": 0.8867, \"total_steps\": 1635, \"epochs\": 3, \"train_runtime_sec\": 3535.7, \"train_samples_per_second\": 3.698, \"train_steps_per_second\": 0.462, \"memory_gib\": 18.95}, \"checkpoint_path\": \"checkpoints/v4_random_fixed_inject10_s123/v0-20260516-015429/checkpoint-1635\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-fixed-inject10-s123.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T18:57:42.428Z\"}, \"v4-taxei-fixed-inject10-s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:48:24.290Z\", \"updated_at\": \"2026-05-15T18:56:29.231Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject10.jsonl --lora_rank 16 --num_train_epochs 3 --seed 123 --data_seed 123 --output_dir checkpoints/v4_taxei_fixed_inject10_s123 --gradient_accumulation_steps 8 --learning_rate 1e-4 --lr_scheduler_type cosine --gradient_checkpointing true --save_strategy epoch --logging_steps 5 --weight_decay 0.1 --adam_beta1 0.9 --adam_beta2 0.95\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"180877\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-fixed-inject10-s123.log\", \"submitted_at\": \"2026-05-15T17:48:23.907Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject10.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject10_s123/v0-20260516-014833/checkpoint-1635\", \"wall_clock_seconds\": 4085.3, \"gpu_hours\": 1.13}, \"hypothesis\": \"v4 TaxEI fixed-size ablation: 10% injection ratio seed=123 (4,358 total = 3,922 clean + 436 injected). Dose-response 5-seed expansion — 补齐 10% 数据点。\", \"reproduce\": {\"finished_at\": \"2026-05-15T18:47:28.139Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T18:47:30.511963+00:00\"}]}, \"metrics\": {\"train_loss\": 0.4234, \"final_loss\": 0.3097, \"final_token_acc\": 0.8882, \"epochs\": 3, \"total_steps\": 1635, \"train_runtime_sec\": 3497, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject10_s123/v0-20260516-014833/checkpoint-1635\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T18:56:29.231Z\"}, \"v4-random-fixed-inject10-s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:48:26.373Z\", \"updated_at\": \"2026-05-15T18:56:27.890Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/ablation_fixed/sft_random_v4_fixed_inject10.jsonl --lora_rank 16 --num_train_epochs 3 --seed 0 --data_seed 0 --output_dir checkpoints/v4_random_fixed_inject10_s0 --gradient_accumulation_steps 8 --learning_rate 1e-4 --lr_scheduler_type cosine --gradient_checkpointing true --save_strategy epoch --logging_steps 5 --weight_decay 0.1 --adam_beta1 0.9 --adam_beta2 0.95\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"180956\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-fixed-inject10-s0.log\", \"submitted_at\": \"2026-05-15T17:48:26.104Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/mini_pipeline_v4/ablation_fixed/sft_random_v4_fixed_inject10.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 0, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_random_fixed_inject10_s0/v0-20260516-014835/checkpoint-1635\", \"wall_clock_seconds\": 4081.8, \"gpu_hours\": 1.13}, \"hypothesis\": \"v4 Random fixed-size ablation: 10% injection ratio seed=0 (4,358 total). Dose-response 5-seed expansion — 与 TaxEI 10% 对比 taxonomy 标签效果。\", \"reproduce\": {\"finished_at\": \"2026-05-15T18:47:48.342Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T18:47:53.242073+00:00\"}]}, \"metrics\": {\"train_loss\": 0.4227, \"final_loss\": 0.276, \"final_token_acc\": 0.9067, \"epochs\": 3, \"total_steps\": 1635, \"train_runtime_sec\": 3531, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_random_fixed_inject10_s0/v0-20260516-014835/checkpoint-1635\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T18:56:27.890Z\"}, \"v4-training-dynamics-forward-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:56:31.230Z\", \"updated_at\": \"2026-05-15T17:55:40.616Z\", \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/tax_error_inject_agent && CUDA_VISIBLE_DEVICES=2 bash scripts/run_training_dynamics_v2.sh\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"180322\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-training-dynamics-forward-v2.log\", \"submitted_at\": \"2026-05-15T16:56:31.040Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"training_dynamics\", \"data_count\": 0, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/artifacts/training_dynamics_v2/\", \"wall_clock_seconds\": 3546.9, \"gpu_hours\": 0.99}, \"conclusion\": \"success\", \"metrics\": {\"subsets_computed\": [\"vanilla_full\", \"taxei_full\", \"random_full\", \"taxei_inject10\", \"taxei_inject25\", \"taxei_inject50\"], \"taxei_inject50_injected_mean_loss\": 0.8185, \"taxei_inject50_clean_mean_loss\": 0.8514, \"per_operator\": {\"C1_ContextTruncation\": {\"mean\": 0.6489, \"n\": 101}, \"C4_ObservationMasking\": {\"mean\": 0.6782, \"n\": 92}, \"P1_StepOrderSwap\": {\"mean\": 0.6374, \"n\": 89}, \"P2_SubGoalDeletion\": {\"mean\": 0.6542, \"n\": 88}}, \"plots\": [\"subset_comparison\", \"operator_breakdown\", \"dose_response\"], \"output_dir\": \"/root/autodl-tmp/tax_error_inject_agent/artifacts/training_dynamics_v2/\"}, \"completed_at\": \"2026-05-15T17:55:37.917Z\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/artifacts/training_dynamics_v2/\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-training-dynamics-forward-v2.log\"}, \"v4-taxei-fixed-inject10-s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:52:30.170Z\", \"updated_at\": \"2026-05-15T17:55:38.973Z\", \"hypothesis\": \"v4 TaxEI fixed-size ablation: 10% injection ratio seed=0 (4,358 total = 3,922 clean + 436 injected). Dose-response 5-seed expansion — 10% 是最薄弱环节，仅有 seed=42 一个数据点。\", \"spec\": {\"data_path\": \"data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject10.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 0, \"injection_ratio\": 0.1, \"clean_count\": 3922, \"injected_count\": 436, \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject10.jsonl --lora_rank 16 --num_train_epochs 3 --seed 0 --data_seed 0 --output_dir checkpoints/v4_taxei_fixed_inject10_s0 --gradient_accumulation_steps 8 --learning_rate 1e-4 --lr_scheduler_type cosine --gradient_checkpointing true --save_strategy epoch --logging_steps 5 --weight_decay 0.1 --adam_beta1 0.9 --adam_beta2 0.95\\\"\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject10_s0/v0-20260516-005247/checkpoint-1635\", \"log_path\": \"checkpoints/v4_taxei_fixed_inject10_s0/v0-20260516-005247/logging.jsonl\"}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.4238, \"final_loss\": 0.3102, \"final_token_acc\": 0.8822, \"epochs\": 3, \"total_steps\": 1635, \"train_runtime_sec\": 3494, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject10_s0/v0-20260516-005247/checkpoint-1635\"}, \"completed_at\": \"2026-05-15T17:55:36.626Z\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject10_s0/v0-20260516-005247/checkpoint-1635\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-fixed-inject10-s0.log\"}, \"v4-random-seed7-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:29:15.592Z\", \"updated_at\": \"2026-05-15T17:43:36.723Z\", \"spec\": {\"command\": \"python3 eval/recovery.py --model_path checkpoints/mini_random_sft_v4_seed7/v0-20260515-233427/checkpoint-3387 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --task_list eval/eval_tasks_47.json --num_episodes 47 --seed 42 --device cuda:0 --output eval_results/v4_random_seed7_eval.json\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"179098\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-seed7-eval.log\", \"submitted_at\": \"2026-05-15T17:29:24.122Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"eval/eval_tasks_47.json\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (random SFT seed=7)\", \"seed\": 42, \"checkpoint_source\": \"v4-random-seed7\", \"eval_data\": \"eval_tasks_47.json\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_random_sft_v4_seed7/v0-20260515-233427/checkpoint-3387\", \"wall_clock_seconds\": 852.6, \"gpu_hours\": 0.24}, \"hypothesis\": \"v4 Random SFT seed=7 eval — 47 ALFWorld tasks, 5-seed expansion ← 基于 v4-random-seed7\", \"reproduce\": {\"finished_at\": \"2026-05-15T17:40:45.965Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:40:48.585893+00:00\"}]}, \"metrics\": {\"success_rate\": 0.553, \"successes\": 26, \"total\": 47, \"by_task_type\": {\"look_at_obj_in_light\": {\"total\": 6, \"success\": 5, \"rate\": 0.833}, \"pick_and_place_simple\": {\"total\": 8, \"success\": 4, \"rate\": 0.5}, \"pick_clean_then_place_in_recep\": {\"total\": 11, \"success\": 6, \"rate\": 0.545}, \"pick_cool_then_place_in_recep\": {\"total\": 7, \"success\": 3, \"rate\": 0.429}, \"pick_heat_then_place_in_recep\": {\"total\": 8, \"success\": 5, \"rate\": 0.625}, \"pick_two_obj_and_place\": {\"total\": 7, \"success\": 3, \"rate\": 0.429}}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T17:43:36.723Z\"}, \"v4-random-seed1-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:17:51.435Z\", \"updated_at\": \"2026-05-15T17:32:36.551Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && mkdir -p eval_results && CUDA_VISIBLE_DEVICES=0 python3 eval/recovery.py --model_path checkpoints/mini_random_sft_v4_seed1/v0-20260515-232340/checkpoint-3387 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --task_list eval/eval_tasks_47.json --num_episodes 47 --seed 42 --device cuda:0 --output eval_results/v4_random_seed1_eval.json\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"178005\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-seed1-eval.log\", \"submitted_at\": \"2026-05-15T17:18:03.664Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 872.9, \"gpu_hours\": 0.24}, \"reproduce\": {\"finished_at\": \"2026-05-15T17:30:35.329Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:30:38.085288+00:00\"}]}, \"metrics\": {\"success_rate\": 0.468, \"successes\": 22, \"total\": 47, \"by_task_type\": {\"look_at_obj_in_light\": {\"success\": 5, \"total\": 6, \"rate\": 0.833}, \"pick_and_place_simple\": {\"success\": 2, \"total\": 8, \"rate\": 0.25}, \"pick_clean_then_place_in_recep\": {\"success\": 5, \"total\": 11, \"rate\": 0.455}, \"pick_cool_then_place_in_recep\": {\"success\": 2, \"total\": 7, \"rate\": 0.286}, \"pick_heat_then_place_in_recep\": {\"success\": 5, \"total\": 8, \"rate\": 0.625}, \"pick_two_obj_and_place\": {\"success\": 3, \"total\": 7, \"rate\": 0.429}}}, \"checkpoint_path\": \"checkpoints/mini_random_sft_v4_seed1/v0-20260515-232340/checkpoint-3387\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-seed1-eval.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T17:32:36.551Z\"}, \"v4-random-seed7\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:34:10.206Z\", \"updated_at\": \"2026-05-15T17:29:09.688Z\", \"hypothesis\": \"v4 Random SFT seed=7 (5-seed expansion) — 9,029 samples, LoRA rank=16, 3 epochs\", \"spec\": {\"command\": \"swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/sft_random_v4.jsonl --lora_rank 16 --lora_alpha 32 --num_train_epochs 3 --seed 7 --output_dir checkpoints/mini_random_sft_v4_seed7 --gradient_accumulation_steps 8 --learning_rate 1e-4 --lr_scheduler_type cosine --gradient_checkpointing true --save_strategy epoch --logging_steps 5 --weight_decay 0.1 --adam_beta1 0.9 --adam_beta2 0.95\", \"server\": \"autodl-5090\", \"data_path\": \"data/mini_pipeline_v4/sft_random_v4.jsonl\", \"data_count\": 9029, \"model_name\": \"Qwen3-8B\", \"seed\": 7, \"gpu\": \"cuda:1\", \"pid\": 164126, \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-seed7.log\", \"checkpoint_path\": \"checkpoints/mini_random_sft_v4_seed7/v0-20260515-233427\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T17:26:13.042Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:26:15.009112+00:00\"}]}, \"metrics\": {\"final_loss\": 0.173, \"final_token_acc\": 0.935, \"initial_loss\": 4.017, \"total_steps\": 3387, \"epochs\": 3, \"total_flos\": 697192362530058200, \"train_runtime_sec\": 6672, \"memory_gib\": 18.49}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_random_sft_v4_seed7/v0-20260515-233427/checkpoint-3387\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-seed7.log\", \"completed_at\": \"2026-05-15T17:29:09.688Z\"}, \"v4-random-seed1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:21:02.077Z\", \"updated_at\": \"2026-05-15T17:17:33.614Z\", \"spec\": {\"hypothesis\": \"v4 Random SFT seed=1 (5-seed expansion) — 9,029 samples, LoRA rank=16, 3 epochs\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python3 train/sft_train.py --config configs/mini_random_sft_v4_seed1.yaml\", \"server\": \"autodl-5090\", \"data_path\": \"data/mini_random_v4\", \"data_count\": 1129, \"model_name\": \"Qwen3-8B\", \"seed\": 1, \"gpu\": [\"cuda:0\"], \"pid\": \"163009\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-seed1.log\", \"checkpoint_path\": \"checkpoints/mini_random_sft_v4_seed1/v0-20260515-232340/\", \"submitted_at\": \"2026-05-15T15:23:31Z\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 6842.6, \"gpu_hours\": 1.9}, \"conclusion\": \"success\", \"checkpoint_path\": \"checkpoints/mini_random_sft_v4_seed1/v0-20260515-232340/checkpoint-3387\", \"metrics\": {\"final_loss\": 0.167, \"final_token_acc\": 0.938, \"initial_loss\": 4.017, \"total_steps\": 3387, \"epochs\": 3, \"total_flos\": 697000000000000000}, \"completed_at\": \"2026-05-15T17:17:33.614Z\"}, \"v4-taxei-seed1-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:39:59.021Z\", \"updated_at\": \"2026-05-15T16:53:41.245Z\", \"hypothesis\": \"v4 TaxEI SFT seed=1 eval — 47 ALFWorld tasks, 5-seed expansion\", \"parent\": \"v4-taxei-seed1\", \"spec\": {\"command\": \"python eval_agent.py --checkpoint checkpoints/mini_taxei_sft_v4_seed1/v0-20260515-214035/checkpoint-3387 --split valid_unseen\", \"server\": \"autodl-5090\", \"data_path\": \"valid_unseen\", \"data_count\": 47, \"model_name\": \"mini_taxei_sft_v4_seed1/checkpoint-3387\", \"seed\": 1, \"checkpoint_source\": \"v4-taxei-seed1\", \"eval_data\": \"valid_unseen\", \"gpu\": [\"cuda:2\"], \"pid\": 173824, \"log_path\": \"eval_results/v4_taxei_seed1_eval.json\", \"checkpoint_path\": \"checkpoints/mini_taxei_sft_v4_seed1/v0-20260515-214035/checkpoint-3387\", \"parent\": \"v4-taxei-seed1\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T16:53:35.955Z\", \"metrics\": {\"success_rate\": 0.596, \"successes\": 28, \"total\": 47, \"by_task_type\": {\"look_at_obj_in_light\": {\"total\": 6, \"success\": 5, \"rate\": 0.833}, \"pick_and_place_simple\": {\"total\": 8, \"success\": 4, \"rate\": 0.5}, \"pick_clean_then_place_in_recep\": {\"total\": 11, \"success\": 5, \"rate\": 0.455}, \"pick_cool_then_place_in_recep\": {\"total\": 7, \"success\": 2, \"rate\": 0.286}, \"pick_heat_then_place_in_recep\": {\"total\": 8, \"success\": 7, \"rate\": 0.875}, \"pick_two_obj_and_place\": {\"total\": 7, \"success\": 5, \"rate\": 0.714}}}}, \"v4-vanilla-seed1-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:49:28.411Z\", \"updated_at\": \"2026-05-15T16:43:19.834Z\", \"hypothesis\": \"v4 Vanilla SFT seed=1 eval — 47 ALFWorld tasks, 5-seed expansion\", \"parent\": \"v4-vanilla-seed1\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 eval/recovery.py --model_path checkpoints/mini_vanilla_sft_v4_seed1/v0-20260515-214031/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --task_list eval/eval_tasks_47.json --num_episodes 47 --seed 42 --device cuda:0 --output eval_results/v4_vanilla_seed1_eval.json\", \"server\": \"autodl-5090\", \"data_path\": \"eval/eval_tasks_47.json\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (vanilla v4 seed=1)\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/mini_vanilla_sft_v4_seed1/v0-20260515-214031/checkpoint-1635\", \"eval_data\": \"47 ALFWorld tasks (clean, no injection)\", \"gpu\": [\"cuda:0\"]}, \"log_path\": \"~/runs/tax_error_inject_agent/v4-vanilla-seed1-eval.log\", \"checkpoint_path\": \"eval_results/v4_vanilla_seed1_eval.json\", \"conclusion\": \"success\", \"metrics\": {\"eval_success_rate\": 0.66, \"eval_successes\": 31, \"eval_total\": 47, \"vs_seed42_pp\": 4.3}, \"completed_at\": \"2026-05-15T16:42:21.398Z\"}, \"v4-taxei-seed7-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:40:01.513Z\", \"updated_at\": \"2026-05-15T16:40:14.867Z\", \"hypothesis\": \"v4 TaxEI SFT seed=7 eval — 47 ALFWorld tasks, 5-seed expansion\", \"parent\": \"v4-taxei-seed7\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python3 eval/recovery.py --model_path checkpoints/mini_taxei_sft_v4_seed7/v0-20260515-214039/checkpoint-3387 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --task_list eval/eval_tasks_47.json --num_episodes 47 --seed 42 --device cuda:0 --output eval_results/v4_taxei_seed7_eval.json\", \"server\": \"autodl-5090\", \"data_path\": \"eval/eval_tasks_47.json\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (TaxEI v4 seed=7)\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/mini_taxei_sft_v4_seed7/v0-20260515-214039/checkpoint-3387\", \"eval_data\": \"47 ALFWorld tasks (clean, no injection)\", \"parent\": \"v4-taxei-seed7\", \"gpu\": [\"cuda:3\"], \"pid\": \"165338\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-seed7-eval.log\", \"checkpoint_path\": \"eval_results/v4_taxei_seed7_eval.json\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.617, \"successes\": 29, \"total\": 47, \"by_task\": {\"look_at_obj_in_light\": \"4/6 (0.667)\", \"pick_and_place_simple\": \"5/8 (0.625)\", \"pick_clean_then_place_in_recep\": \"5/11 (0.455)\", \"pick_cool_then_place_in_recep\": \"4/7 (0.571)\", \"pick_heat_then_place_in_recep\": \"7/8 (0.875)\", \"pick_two_obj_and_place\": \"4/7 (0.571)\"}}, \"completed_at\": \"2026-05-15T16:40:14.867Z\"}, \"v4-training-dynamics-forward\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:48:36.487Z\", \"updated_at\": \"2026-05-15T16:37:23.642Z\", \"hypothesis\": \"D027 Training Dynamics: Post-hoc forward pass on seed=42 checkpoints (Vanilla/TaxEI/Random + dose-response 10%/25%/50%) — compute per-subset loss (clean vs injected) and per-operator loss (P1/P2/C1/C4). Key finding: training loss SD=0.0004 across seeds but eval SD=8.6pp — memorization-generalization dissociation.\", \"spec\": {\"command\": \"bash scripts/run_training_dynamics.sh\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/tax_error_inject_agent/data/mini_pipeline_v4/\", \"data_count\": 6, \"model_name\": \"Qwen3-8B\", \"seed\": 42}, \"metrics\": {\"vanilla_full\": {\"clean_loss\": 0.6853, \"clean_n\": 4358}, \"taxei_full\": {\"clean_loss\": 0.7712, \"injected_loss\": 0.6139, \"clean_n\": 8269, \"injected_n\": 760, \"per_operator\": {\"P1_StepOrderSwap\": 0.6165, \"P2_SubGoalDeletion\": 0.6161, \"C1_ContextTruncation\": 0.5932, \"C4_ObservationMasking\": 0.6298}}, \"random_full\": {\"clean_loss\": 0.7354, \"injected_loss\": 0.5902, \"clean_n\": 8269, \"injected_n\": 760}, \"dose_response\": {\"taxei_10pct\": {\"clean_loss\": 0.6628, \"injected_loss\": 0.6464, \"gap\": -0.0164, \"injected_n\": 70}, \"taxei_25pct\": {\"clean_loss\": 0.701, \"injected_loss\": 0.574, \"gap\": -0.127, \"injected_n\": 168}, \"taxei_50pct\": {\"clean_loss\": 0.8516, \"injected_loss\": 0.6547, \"gap\": -0.1969, \"injected_n\": 370}}, \"key_findings\": \"Clear dose-response: injected-clean gap widens from -0.016 (10%) to -0.127 (25%) to -0.197 (50%). TaxEI operators C1_ContextTruncation consistently lowest loss. Higher injection rates also degrade clean sample loss (0.663→0.701→0.852).\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/artifacts/training_dynamics/\", \"log_path\": \"/root/autodl-tmp/tax_error_inject_agent/artifacts/training_dynamics/\", \"completed_at\": \"2026-05-15T16:35:47.805Z\"}, \"v4-taxei-seed1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:40:26.898Z\", \"updated_at\": \"2026-05-15T15:39:39.545Z\", \"spec\": {\"command\": \"swift sft --model Qwen3-8B --dataset sft_taxei_v4.jsonl --seed 1 --lora_rank 16 --lora_alpha 32 --num_train_epochs 3\", \"server\": \"autodl-5090\", \"data_path\": \"data/mini_pipeline_v4/sft_taxei_v4.jsonl\", \"data_count\": 9029, \"model_name\": \"Qwen3-8B\", \"seed\": 1, \"gpu\": \"cuda:2\", \"pid\": 154937}, \"metrics\": {\"final_loss\": 0.1667, \"avg_loss\": 0.3561, \"token_accuracy\": 0.915, \"final_token_acc\": 0.942, \"train_steps\": 3387, \"train_epochs\": 3, \"train_duration_min\": 108.9, \"memory_gib\": 18.49, \"checkpoint_path\": \"checkpoints/mini_taxei_sft_v4_seed1/v0-20260515-214035/checkpoint-3387\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T15:30:06.293Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T15:30:07.753494+00:00\"}]}, \"conclusion\": \"success\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-seed1.log\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_taxei_sft_v4_seed1/v0-20260515-214035/checkpoint-3387\", \"completed_at\": \"2026-05-15T15:39:39.545Z\"}, \"v4-taxei-seed7\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:40:29.737Z\", \"updated_at\": \"2026-05-15T15:39:16.334Z\", \"spec\": {\"command\": \"swift sft --model Qwen3-8B --dataset sft_taxei_v4.jsonl --seed 7 --lora_rank 16 --lora_alpha 32 --3epochs\", \"server\": \"autodl-5090\", \"data_path\": \"data/mini_pipeline_v4/sft_taxei_v4.jsonl\", \"data_count\": 9029, \"model_name\": \"Qwen3-8B\", \"seed\": 7, \"gpu\": \"cuda:3\", \"pid\": 155145}, \"metrics\": {\"current_step\": 3387, \"total_steps\": 3387, \"progress_pct\": 100, \"train_loss\": 0.3568, \"final_step_loss\": 0.1753, \"token_acc\": 0.9009, \"final_token_acc\": 0.9328, \"train_runtime_s\": 6591.9, \"epochs\": 3, \"peak_memory_gib\": 18.49, \"gpu\": \"cuda:3\", \"pid\": 155145}, \"reproduce\": {\"finished_at\": \"2026-05-15T15:32:43.183Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T15:32:44.276153+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_taxei_sft_v4_seed7/v0-20260515-214039/checkpoint-3387\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-seed7.log\", \"completed_at\": \"2026-05-15T15:36:45.958Z\"}, \"v4-vanilla-seed7-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:49:11.983Z\", \"updated_at\": \"2026-05-15T15:32:42.490Z\", \"hypothesis\": \"v4 Vanilla SFT seed=7 eval — 47 ALFWorld tasks, 5-seed expansion\", \"parent\": \"v4-vanilla-seed7\", \"spec\": {\"command\": \"python3 eval/recovery.py --model_path checkpoints/mini_vanilla_sft_v4_seed7/v1-20260515-214032/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --num_episodes 47 --output eval_results/v4_vanilla_seed7_eval.json --device cuda:1 --seed 42\", \"server\": \"autodl-5090\", \"data_path\": \"eval/47 ALFWorld valid_unseen\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (vanilla v4 seed=7)\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/mini_vanilla_sft_v4_seed7/v1-20260515-214032/checkpoint-1635\", \"eval_data\": \"47 ALFWorld tasks (clean, no injection)\", \"parent\": \"v4-vanilla-seed7\", \"gpu\": [\"cuda:1\"], \"pid\": \"160587\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-vanilla-seed7-eval.log\", \"checkpoint_path\": \"eval_results/v4_vanilla_seed7_eval.json\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"success\", \"metrics\": {\"eval_success_rate\": 0.745, \"eval_successes\": 35, \"eval_total\": 47, \"vs_seed42_pp\": 12.8}, \"completed_at\": \"2026-05-15T15:32:42.490Z\"}, \"v4-vanilla-seed1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:40:21.621Z\", \"updated_at\": \"2026-05-15T14:49:23.447Z\", \"spec\": {\"command\": \"swift sft --model Qwen3-8B --dataset sft_vanilla_v4.jsonl --seed 1 --lora_rank 16 --lora_alpha 32 --3epochs\", \"server\": \"autodl-5090\", \"data_path\": \"data/mini_pipeline_v4/sft_vanilla_v4.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 1, \"gpu\": \"cuda:0\", \"pid\": 154589, \"checkpoint_path\": \"checkpoints/mini_vanilla_sft_v4_seed1/v0-20260515-214031/checkpoint-1635\", \"log_path\": \"checkpoints/mini_vanilla_sft_v4_seed1/v0-20260515-214031/\"}, \"metrics\": {\"final_loss\": 0.292, \"avg_loss\": 0.416, \"token_accuracy\": 0.903, \"train_steps\": 1635, \"train_epochs\": 3, \"train_duration_min\": 58.8, \"memory_gib\": 17.63, \"checkpoint_path\": \"checkpoints/mini_vanilla_sft_v4_seed1/v0-20260515-214031/checkpoint-1635\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T14:39:36.578Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T14:39:37.963564+00:00\"}]}, \"conclusion\": \"success\", \"hypothesis\": \"D010 Phase 1: v4 Vanilla SFT seed=1 多种子验证 — 4,358 samples, LoRA rank=16, 3 epochs, 与 seed=42 的 61.7% 对比波动范围\", \"completed_at\": \"2026-05-15T14:49:23.447Z\"}, \"v4-vanilla-seed7\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:45:24.536Z\", \"updated_at\": \"2026-05-15T14:46:55.133Z\", \"hypothesis\": \"D010 Phase 1: v4 Vanilla SFT seed=7 多种子验证 — 4,358 samples, LoRA rank=16, 3 epochs, 与 seed=42 的 61.7% 对比波动范围\", \"spec\": {\"command\": \"swift sft --model Qwen3-8B --dataset sft_vanilla_v4.jsonl --seed 7 --lora_rank 16 --lora_alpha 32 --3epochs\", \"server\": \"autodl-5090\", \"data_path\": \"data/mini_pipeline_v4/sft_vanilla_v4.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 7, \"gpu\": \"cuda:1\", \"pid\": 154666}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T18:20:48.185Z\", \"metrics\": {\"final_loss\": 0.295, \"avg_loss\": 0.415, \"token_accuracy\": 0.898, \"train_steps\": 1635, \"train_epochs\": 3, \"train_duration_min\": 59.4, \"checkpoint_path\": \"checkpoints/mini_vanilla_sft_v4_seed7/v0-20260515-214031/checkpoint-1635\"}}, \"v4-vanilla-recovery-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T19:30:18.314Z\", \"updated_at\": \"2026-05-15T03:29:56.077Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 eval/injected_eval.py --model_path checkpoints/mini_vanilla_sft_v4/v0-20260514-201441/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --model_variant vanilla --num_episodes 47 --seed 42 --device cuda:0 --output eval_results/v4_vanilla_recovery_eval.json\", \"server\": \"autodl-5090\", \"model_name\": \"Qwen3-8B + LoRA (vanilla v4 seed=42)\", \"checkpoint_source\": \"checkpoints/mini_vanilla_sft_v4/v0-20260514-201441/checkpoint-1635\", \"eval_data\": \"47 ALFWorld tasks with error injection\", \"seed\": 42, \"parent\": \"mini-vanilla-sft-v4\", \"checkpoint_path\": \"eval_results/v4_vanilla_recovery_eval.json\", \"log_path\": \"eval_results/v4_vanilla_recovery_eval.json\"}, \"hypothesis\": \"v4 Vanilla SFT seed=42 recovery eval (injected_eval.py) — 47 episodes with error injection, measuring detection/recovery/success rates under P1/P2/C1/C4 operators\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.617, \"successes\": 29, \"total\": 47, \"recovery_rate\": 0.617, \"detection_rate\": 0, \"per_operator\": {\"C1_context_truncation\": {\"recovered\": 9, \"total\": 12, \"rate\": 0.75}, \"C4_observation_masking\": {\"recovered\": 6, \"total\": 11, \"rate\": 0.545}, \"P1_step_order_swap\": {\"recovered\": 7, \"total\": 12, \"rate\": 0.583}, \"P2_sub_goal_deletion\": {\"recovered\": 7, \"total\": 12, \"rate\": 0.583}}}, \"completed_at\": \"2026-05-14T21:20:15.791Z\"}, \"v4-random-fixed-inject50-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T01:43:46.913Z\", \"updated_at\": \"2026-05-15T02:03:49.013Z\", \"hypothesis\": \"v4 Random 50% injection fixed-size eval — 47 tasks clean eval. 与 TaxEI 50% (51.1%) 对比。Random dose-response 最后一点。\", \"spec\": {\"gpu\": [\"cuda:3\"]}, \"reproduce\": {\"finished_at\": \"2026-05-15T01:56:26.837Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T01:56:28.410747+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"eval_success_rate\": 0.574, \"eval_successes\": 27, \"eval_total\": 47, \"vs_vanilla_seed42_pp\": -4.3, \"vs_taxei_50_pp\": 6.3}, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_random_fixed_inject50_eval.json\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-fixed-inject50-eval.log\", \"completed_at\": \"2026-05-15T02:00:22.858Z\"}, \"v4-random-fixed-inject25-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T01:48:25.777Z\", \"updated_at\": \"2026-05-15T02:03:46.203Z\", \"hypothesis\": \"v4 Random 25% injection fixed-size eval — 47 ALFWorld tasks (clean). 与 TaxEI 25% (48.9%) 对比。\", \"parent\": \"v4-random-fixed-inject25\", \"spec\": {\"command\": \"python3 eval/recovery.py --model_path /root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_random_fixed_inject25/v1-20260515-084707/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_random_fixed_inject25_eval.json --device cuda:0\", \"server\": \"autodl-5090\", \"parent\": \"v4-random-fixed-inject25\", \"checkpoint_source\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_random_fixed_inject25/v1-20260515-084707/checkpoint-1635\", \"eval_data\": \"47 ALFWorld tasks (clean, no injection)\", \"data_path\": \"eval/alfworld_47_clean\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (random fixed inject25)\", \"seed\": 42, \"gpu\": [\"cuda:0\"], \"pid\": \"112516\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-fixed-inject25-eval.log\"}, \"conclusion\": \"success\", \"metrics\": {\"eval_success_rate\": 0.553, \"eval_successes\": 26, \"eval_total\": 47, \"vs_vanilla_seed42_pp\": -6.4, \"vs_taxei_25_pp\": 6.4}, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_random_fixed_inject25_eval.json\", \"completed_at\": \"2026-05-15T01:59:41.894Z\"}, \"v4-random-fixed-inject50\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T00:45:08.375Z\", \"updated_at\": \"2026-05-15T02:02:45.338Z\", \"hypothesis\": \"v4 Random fixed-size ablation: 50% injection (4,358 total = 2,179 clean + 2,179 injected). 与 TaxEI 50% 对比 taxonomy 标签在高注入比例下是否有差异。\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/random_fixed_inject50/v0-20260515-084528/checkpoint-1635\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T01:39:15.464Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T01:39:17.014804+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"train_steps\": 1635, \"train_epochs\": 3, \"data_count\": 4358, \"train_loss\": 0.4338, \"final_step_loss\": 0.2618, \"token_accuracy\": 0.91, \"train_duration_min\": 53.1, \"memory_gib\": 18, \"train_speed_s_per_it\": 1.95}, \"completed_at\": \"2026-05-15T01:43:35.237Z\"}, \"v4-random-fixed-inject25\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T00:25:44.436Z\", \"updated_at\": \"2026-05-15T01:48:07.606Z\", \"hypothesis\": \"v4 Random fixed-size ablation: 25% injection (4,358 total). 与 TaxEI 25% (48.9%) 对比 taxonomy 标签在中等注入比例下是否有差异。\", \"spec\": {\"command\": \"swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/ablation_fixed/sft_random_v4_fixed_inject25.jsonl --lora_rank 16 --num_train_epochs 3 --seed 42 --output_dir checkpoints/v4_random_fixed_inject25 --gradient_accumulation_steps 8 --learning_rate 1e-4 --lr_scheduler_type cosine --gradient_checkpointing true --save_strategy epoch --logging_steps 5 --weight_decay 0.1 --adam_beta1 0.9 --adam_beta2 0.95\", \"server\": \"autodl-5090\", \"data_path\": \"data/mini_pipeline_v4/ablation_fixed/sft_random_v4_fixed_inject25.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"gpu\": \"cuda:1\", \"max_steps\": 1635, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_random_fixed_inject25/v1-20260515-084707/checkpoint-1635\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-fixed-inject25.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T01:43:59.432Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T01:44:03.491274+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"train_steps\": 1635, \"train_epochs\": 3, \"data_count\": 4358}, \"completed_at\": \"2026-05-15T01:48:05.171Z\"}, \"v4-random-fixed-inject10-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T01:28:17.994Z\", \"updated_at\": \"2026-05-15T01:42:40.302Z\", \"hypothesis\": \"v4 Random 10% injection fixed-size eval — 47 ALFWorld tasks (clean). 与 TaxEI 10% (61.7%) 对比。\", \"spec\": {\"command\": \"python3 eval/recovery.py --model_path /root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_random_fixed_inject10/v0-20260515-082828/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_random_fixed_inject10_eval.json --device cuda:2\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"110187\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-fixed-inject10-eval.log\", \"submitted_at\": \"2026-05-15T01:28:27.422Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"parent\": \"v4-random-fixed-inject10\", \"checkpoint_source\": \"v4-random-fixed-inject10\", \"eval_data\": \"47 ALFWorld tasks (clean, no injection)\", \"data_count\": 47, \"data_path\": \"eval/alfworld_47_clean\", \"model_name\": \"Qwen3-8B + LoRA (random fixed inject10)\", \"seed\": 42, \"wall_clock_seconds\": 852.9, \"gpu_hours\": 0.24}, \"parent\": \"v4-random-fixed-inject10\", \"metrics\": {\"eval_success_rate\": 0.681, \"eval_successes\": 32, \"eval_total\": 47, \"by_task\": {\"look_at_obj_in_light\": {\"total\": 6, \"success\": 5, \"rate\": 0.833}, \"pick_and_place_simple\": {\"total\": 8, \"success\": 5, \"rate\": 0.625}, \"pick_clean_then_place_in_recep\": {\"total\": 11, \"success\": 6, \"rate\": 0.545}, \"pick_cool_then_place_in_recep\": {\"total\": 7, \"success\": 4, \"rate\": 0.571}, \"pick_heat_then_place_in_recep\": {\"total\": 8, \"success\": 7, \"rate\": 0.875}, \"pick_two_obj_and_place\": {\"total\": 7, \"success\": 5, \"rate\": 0.714}}}, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_random_fixed_inject10_eval.json\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-fixed-inject10-eval.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T01:42:40.303Z\"}, \"v4-taxei-fixed-inject50-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T01:28:14.823Z\", \"updated_at\": \"2026-05-15T01:38:54.383Z\", \"spec\": {\"command\": \"python eval/recovery.py --model_path checkpoints/v4_taxei_fixed_inject50/v0-20260515-082759/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --num_episodes 47 --output eval_results/v4_taxei_fixed_inject50_eval.json --device cuda:0 --seed 42\", \"server\": \"autodl-5090\", \"data_path\": \"ALFWorld valid_unseen\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (v4-taxei-fixed-inject50)\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/v4_taxei_fixed_inject50/v0-20260515-082759/checkpoint-1635\", \"eval_data\": \"ALFWorld valid_unseen 47 tasks clean eval\"}, \"hypothesis\": \"v4 TaxEI fixed-size ablation: 50% injection eval — 47 tasks clean eval. Dose-response 最后一个数据点。已有：0%=61.7%, 10%=61.7%, 25%=48.9%, 50%=待测。\", \"metrics\": {\"eval_success_rate\": 0.511, \"eval_successes\": 24, \"eval_total\": 47, \"vs_vanilla_seed42_pp\": -10.6}, \"checkpoint_path\": \"checkpoints/v4_taxei_fixed_inject50/v0-20260515-082759/checkpoint-1635\", \"log_path\": \"/tmp/eval_inject50.log\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-15T01:37:38.792Z\"}, \"v4-random-fixed-inject10\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T00:25:41.996Z\", \"updated_at\": \"2026-05-15T01:31:01.715Z\", \"hypothesis\": \"v4 Random fixed-size ablation: 10% injection (4,358 total). 与 TaxEI 10% (61.7%) 对比 taxonomy 标签在低注入比例下是否有差异。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export CUDA_VISIBLE_DEVICES=2 && cd /root/autodl-tmp/tax_error_inject_agent && swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/ablation_fixed/sft_random_v4_fixed_inject10.jsonl --lora_rank 16 --num_train_epochs 3 --seed 42 --output_dir checkpoints/v4_random_fixed_inject10 --gradient_accumulation_steps 8 --learning_rate 1e-4 --lr_scheduler_type cosine --gradient_checkpointing true --save_strategy epoch --logging_steps 5 --weight_decay 0.1 --adam_beta1 0.9 --adam_beta2 0.95\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"104655\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-fixed-inject10.log\", \"submitted_at\": \"2026-05-15T00:28:19.537Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/mini_pipeline_v4/ablation_fixed/sft_random_v4_fixed_inject10.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_path\": \"checkpoints/v4_random_fixed_inject10/v0-20260515-082828/checkpoint-1635\", \"wall_clock_seconds\": 3546.1, \"gpu_hours\": 0.99}, \"reproduce\": {\"finished_at\": \"2026-05-15T01:26:29.568Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T01:26:31.003606+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.4226, \"final_step_loss\": 0.3079, \"token_accuracy\": 0.9, \"train_steps\": 1635, \"train_epochs\": 3, \"train_duration_min\": 57}, \"completed_at\": \"2026-05-15T01:27:25.646Z\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_random_fixed_inject10/v0-20260515-082828/checkpoint-1635\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-fixed-inject10.log\"}, \"v4-taxei-fixed-inject50\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T00:25:38.284Z\", \"updated_at\": \"2026-05-15T01:25:47.611Z\", \"hypothesis\": \"v4 TaxEI fixed-size ablation: 50% injection ratio (4,358 total = 2,179 clean + 2,179 injected). Dose-response 最后一个点，完成后有完整曲线 0%→10%→25%→50%。\", \"spec\": {\"command\": \"swift sft --model Qwen3-8B --dataset sft_taxei_v4_fixed_inject50.jsonl --lora_rank 16 --num_train_epochs 3 --seed 42 --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --learning_rate 1e-4\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"104236\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-fixed-inject50.log\", \"submitted_at\": \"2026-05-15T00:27:51.219Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject50.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_path\": \"checkpoints/v4_taxei_fixed_inject50/v0-20260515-082759/checkpoint-1635\", \"wall_clock_seconds\": 3476.4, \"gpu_hours\": 0.97}, \"reproduce\": {\"finished_at\": \"2026-05-15T01:22:23.688Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T01:22:25.093365+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.259, \"token_accuracy\": 0.911, \"train_steps\": 1635, \"train_epochs\": 3, \"train_duration_min\": 53.1}, \"completed_at\": \"2026-05-15T01:25:47.611Z\"}, \"v4-random-seed123-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T00:14:30.699Z\", \"updated_at\": \"2026-05-15T00:27:24.291Z\", \"hypothesis\": \"v4 Random SFT seed=123 eval — 47 tasks clean eval. Multi-seed: seed=42 66.0%, seed=0 55.3%, seed=123 待测。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export CUDA_VISIBLE_DEVICES=1 && cd /root/autodl-tmp/tax_error_inject_agent && python eval/recovery.py --model_path checkpoints/mini_random_sft_v4_seed123/v0-20260515-055925/checkpoint-3387 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_random_seed123_eval.json --device cuda:0\\\"\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"pid\": 102888, \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-seed123-eval.log\", \"submitted_at\": \"2026-05-15T00:14:42.930Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"eval/eval_tasks_47.json\", \"data_count\": 47, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"checkpoint_source\": \"checkpoints/mini_random_sft_v4_seed123/v0-20260515-055925/checkpoint-3387\", \"eval_data\": \"47 tasks clean eval (no injection)\", \"parent\": \"v4-random-seed123\", \"tmux_session\": \"v4-random-seed123-eval\", \"log_file\": \"~/runs/tax_error_inject_agent/v4-random-seed123-eval.log\", \"wall_clock_seconds\": 740.0, \"gpu_hours\": 0.21}, \"conclusion\": \"negative\", \"checkpoint_path\": \"checkpoints/mini_random_sft_v4_seed123/v0-20260515-055925/checkpoint-3387\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-seed123-eval.log\", \"completed_at\": \"2026-05-15T00:27:02.930Z\", \"metrics\": {\"eval_success_rate\": 0.681, \"eval_successes\": 32, \"eval_total\": 47, \"by_task\": {\"look_at_obj_in_light\": {\"total\": 6, \"success\": 5, \"rate\": 0.833}, \"pick_and_place_simple\": {\"total\": 8, \"success\": 5, \"rate\": 0.625}, \"pick_clean_then_place_in_recep\": {\"total\": 11, \"success\": 7, \"rate\": 0.636}, \"pick_cool_then_place_in_recep\": {\"total\": 7, \"success\": 4, \"rate\": 0.571}, \"pick_heat_then_place_in_recep\": {\"total\": 8, \"success\": 6, \"rate\": 0.75}, \"pick_two_obj_and_place\": {\"total\": 7, \"success\": 5, \"rate\": 0.714}}}}, \"v4-taxei-fixed-inject25-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T23:50:53.016Z\", \"updated_at\": \"2026-05-15T00:14:40.327Z\", \"hypothesis\": \"v4 TaxEI 25% injection fixed-size eval — 48.9% (23/47), 显著低于 vanilla baseline 65.3%（-16.4pp）。Dose-response 数据点。\", \"spec\": {\"command\": \"python3 eval/recovery.py --model_path output/v4-fixed-inject25/v0-20260515-063144/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_taxei_fixed_inject25_eval.json --device cuda:0\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"checkpoint_source\": \"output/v4-fixed-inject25/v0-20260515-063144/checkpoint-1635\", \"eval_data\": \"47 ALFWorld tasks (clean)\", \"parent\": \"v4-taxei-fixed-inject25-r2\", \"data_path\": \"eval/valid_unseen\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (taxei fixed inject25)\", \"seed\": 42}, \"metrics\": {\"eval_success_rate\": 0.489, \"eval_successes\": 23, \"eval_total\": 47, \"by_task\": {\"look_at_obj_in_light\": {\"success\": 4, \"total\": 6, \"rate\": 0.667}, \"pick_and_place_simple\": {\"success\": 3, \"total\": 8, \"rate\": 0.375}, \"pick_clean_then_place_in_recep\": {\"success\": 5, \"total\": 11, \"rate\": 0.455}, \"pick_cool_then_place_in_recep\": {\"success\": 2, \"total\": 7, \"rate\": 0.286}, \"pick_heat_then_place_in_recep\": {\"success\": 5, \"total\": 8, \"rate\": 0.625}, \"pick_two_obj_and_place\": {\"success\": 4, \"total\": 7, \"rate\": 0.571}}}, \"checkpoint_path\": \"eval_results/v4_taxei_fixed_inject25_eval.json\", \"log_path\": \"/tmp/v4_taxei_fixed_inject25_eval.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T00:14:30.429Z\"}, \"v4-taxei-fixed-inject10-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T23:50:52.584Z\", \"updated_at\": \"2026-05-15T00:14:38.874Z\", \"hypothesis\": \"v4 TaxEI 10% injection fixed-size eval — 61.7% (29/47), 低于 vanilla baseline 65.3%（-3.6pp）。Dose-response 数据点。\", \"spec\": {\"command\": \"python3 eval/recovery.py --model_path output/v4-fixed-inject10/v0-20260515-061243/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_taxei_fixed_inject10_eval.json --device cuda:0\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:2\", \"tmux_session\": \"eval_inject10\", \"checkpoint_source\": \"output/v4-fixed-inject10/v0-20260515-061243/checkpoint-1635\", \"eval_data\": \"47 ALFWorld tasks (clean)\", \"parent\": \"v4-taxei-fixed-inject10\", \"data_path\": \"eval/valid_unseen\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (taxei fixed inject10)\", \"seed\": 42, \"log_path\": \"/tmp/v4_taxei_fixed_inject10_eval.log\"}, \"metrics\": {\"eval_success_rate\": 0.617, \"eval_successes\": 29, \"eval_total\": 47, \"by_task\": {\"look_at_obj_in_light\": {\"success\": 5, \"total\": 6, \"rate\": 0.833}, \"pick_and_place_simple\": {\"success\": 5, \"total\": 8, \"rate\": 0.625}, \"pick_clean_then_place_in_recep\": {\"success\": 5, \"total\": 11, \"rate\": 0.455}, \"pick_cool_then_place_in_recep\": {\"success\": 4, \"total\": 7, \"rate\": 0.571}, \"pick_heat_then_place_in_recep\": {\"success\": 6, \"total\": 8, \"rate\": 0.75}, \"pick_two_obj_and_place\": {\"success\": 4, \"total\": 7, \"rate\": 0.571}}}, \"checkpoint_path\": \"eval_results/v4_taxei_fixed_inject10_eval.json\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T00:14:29.992Z\"}, \"v4-taxei-seed123-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T23:44:07.489Z\", \"updated_at\": \"2026-05-15T00:14:37.513Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 eval/recovery.py --model_path checkpoints/mini_taxei_sft_v4_seed123/v0-20260515-055026/checkpoint-3387 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_taxei_seed123_eval.json --device cuda:0\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"pid\": 100600, \"model_name\": \"Qwen3-8B + LoRA (taxei v4 seed=123)\", \"seed\": 123, \"checkpoint_source\": \"checkpoints/mini_taxei_sft_v4_seed123/v0-20260515-055026/checkpoint-3387\", \"eval_data\": \"47 ALFWorld tasks (clean, no injection)\", \"parent\": \"v4-taxei-seed123\", \"checkpoint_path\": \"eval_results/v4_taxei_seed123_eval.json\", \"log_path\": \"/tmp/v4_taxei_seed123_eval.log\", \"data_path\": \"eval/valid_unseen\", \"data_count\": 47}, \"hypothesis\": \"v4 TaxEI SFT seed=123 eval — 61.7% (29/47), 低于 vanilla baseline 65.3%（-3.6pp）。multi-seed verification, 9029 samples。\", \"metrics\": {\"eval_success_rate\": 0.617, \"eval_successes\": 29, \"eval_total\": 47, \"by_task\": {\"look_at_obj_in_light\": {\"success\": 5, \"total\": 6, \"rate\": 0.833}, \"pick_and_place_simple\": {\"success\": 4, \"total\": 8, \"rate\": 0.5}, \"pick_clean_then_place_in_recep\": {\"success\": 7, \"total\": 11, \"rate\": 0.636}, \"pick_cool_then_place_in_recep\": {\"success\": 3, \"total\": 7, \"rate\": 0.429}, \"pick_heat_then_place_in_recep\": {\"success\": 6, \"total\": 8, \"rate\": 0.75}, \"pick_two_obj_and_place\": {\"success\": 4, \"total\": 7, \"rate\": 0.571}}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T00:14:29.055Z\"}, \"v4-random-seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:49:34.441Z\", \"updated_at\": \"2026-05-14T23:52:15.056Z\", \"hypothesis\": \"v4 Random SFT seed=123 (P1 multi-seed补齐) — 9,029 samples, same hyperparams as seed=42/0, 配齐3-seed统计分析\", \"spec\": {\"command\": \"swift sft --model Qwen3-8B --dataset sft_random_v4.jsonl --seed 123 --lora_rank 16 --num_train_epochs 3\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"pid\": 93477, \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-seed123.log\", \"submitted_at\": \"2026-05-14T21:59:16.545Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/tax_error_inject_agent/data/mini_pipeline_v4/sft_random_v4.jsonl\", \"data_count\": 9029, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"wall_clock_seconds\": 6778.5, \"gpu_hours\": 1.88}, \"reproduce\": {\"finished_at\": \"2026-05-14T23:50:09.168Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T23:50:10.389568+00:00\"}]}, \"metrics\": {\"train_loss\": 0.35484016, \"final_loss\": 0.16766574, \"token_accuracy\": 0.94187103, \"avg_token_accuracy\": 0.90849673, \"train_steps\": 3387, \"train_epochs\": 3, \"train_runtime_sec\": 6609.3556, \"train_duration_min\": 110.2, \"train_samples_per_second\": 4.098, \"train_steps_per_second\": 0.512, \"train_speed_s_per_it\": 1.951, \"memory_gib\": 18.49}, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_random_sft_v4_seed123/v0-20260515-055925/checkpoint-3387\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T23:52:15.056Z\"}, \"v4-taxei-fixed-inject25-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:32:41.837Z\", \"updated_at\": \"2026-05-14T23:50:46.230Z\", \"hypothesis\": \"v4 TaxEI fixed-size ablation: 25% injection ratio retry (4,358 total = 3,268 clean + 1,090 injected). 修复 CUDA_VISIBLE_DEVICES，显式设 =3。\", \"spec\": {\"command\": \"export CUDA_VISIBLE_DEVICES=3 && swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject25.jsonl --output_dir checkpoints/taxei_fixed_inject25 --lora_rank 16 --lora_alpha 32 --lora_dropout 0.05 --target_modules all-linear --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --max_length 4096 --num_train_epochs 3 --learning_rate 1e-4 --seed 42 --torch_dtype bfloat16 --logging_steps 5 --save_strategy epoch --gradient_checkpointing true\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"pid\": 96835, \"data_path\": \"data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject25.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"injection_ratio\": 0.25, \"clean_count\": 3268, \"injected_count\": 1090, \"log_path\": \"/tmp/v4-fixed-inject25.log\", \"note\": \"manual tmux with explicit CUDA_VISIBLE_DEVICES=3, fixing r1 OOM\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"output/v4-fixed-inject25/v0-20260515-063144/checkpoint-1635\", \"metrics\": {\"final_loss\": 0.285, \"token_accuracy\": 0.893, \"train_steps\": 1635, \"train_epochs\": 3, \"train_duration_min\": 58}, \"completed_at\": \"2026-05-14T23:50:46.230Z\"}, \"v4-taxei-fixed-inject10\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:09:52.707Z\", \"updated_at\": \"2026-05-14T23:50:45.829Z\", \"hypothesis\": \"v4 TaxEI fixed-size ablation: 10% injection ratio (4,358 total = 3,922 clean + 436 injected). Fixed-size = vanilla 大小，控制数据量变量。Dose-response: 10%/25%/50%。\", \"spec\": {\"command\": \"swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset sft_taxei_v4_fixed_inject10.jsonl --output_dir output/v4-fixed-inject10 --num_train_epochs 3 --learning_rate 1e-4 --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --lora_rank 16 --lora_alpha 32 --lora_dropout 0.05 --seed 42 --data_seed 42 --bf16 true --gradient_checkpointing true\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"94635\", \"log_path\": \"/tmp/v4-fixed-inject10.log\", \"submitted_at\": \"2026-05-15T06:12:34Z\", \"submitted_via\": \"manual_tmux\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject10.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"injection_ratio\": 0.1, \"clean_count\": 3922, \"injected_count\": 436}, \"conclusion\": \"success\", \"checkpoint_path\": \"output/v4-fixed-inject10/v0-20260515-061243/checkpoint-1635\", \"metrics\": {\"final_loss\": 0.308, \"token_accuracy\": 0.888, \"train_steps\": 1635, \"train_epochs\": 3, \"train_duration_min\": 58}, \"completed_at\": \"2026-05-14T23:50:45.829Z\"}, \"v4-taxei-fixed-inject25\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:09:53.209Z\", \"updated_at\": \"2026-05-14T23:45:26.890Z\", \"hypothesis\": \"v4 TaxEI fixed-size ablation: 25% injection ratio (4,358 total = 3,268 clean + 1,090 injected). Fixed-size = vanilla 大小，控制数据量变量。Dose-response: 10%/25%/50%。\", \"spec\": {\"command\": \"swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset sft_taxei_v4_fixed_inject25.jsonl --output_dir output/v4-fixed-inject25 --num_train_epochs 3 --learning_rate 1e-4 --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --lora_rank 16 --lora_alpha 32 --lora_dropout 0.05 --seed 42 --data_seed 42 --bf16 true --gradient_checkpointing true\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"96835\", \"log_path\": \"/tmp/v4-fixed-inject25.log\", \"submitted_at\": \"2026-05-15T06:31:44Z\", \"submitted_via\": \"manual_tmux\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject25.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"injection_ratio\": 0.25, \"clean_count\": 3268, \"injected_count\": 1090, \"note\": \"r1 (PID 95170) OOM on cuda:0 — submit_training_job failed to pass CUDA_VISIBLE_DEVICES. Resubmitted manually via tmux with explicit export CUDA_VISIBLE_DEVICES=3.\"}, \"conclusion\": \"failed\", \"failure_reason\": \"CUDA_VISIBLE_DEVICES 未生效，模型加载到 cuda:0 导致 OOM（与 seed123 训练冲突）\", \"completed_at\": \"2026-05-14T23:45:26.890Z\"}, \"v4-taxei-seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:49:34.191Z\", \"updated_at\": \"2026-05-14T23:43:38.819Z\", \"hypothesis\": \"v4 TaxEI SFT seed=123 (P1 multi-seed补齐) — 9,029 samples, same hyperparams as seed=42/0, 配齐3-seed统计分析\", \"spec\": {\"command\": \"swift sft --model Qwen3-8B --dataset sft_taxei_v4.jsonl --seed 123 --lora_rank 16 --num_train_epochs 3\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"pid\": 92263, \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-seed123.log\", \"submitted_at\": \"2026-05-14T21:50:17.845Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/tax_error_inject_agent/data/mini_pipeline_v4/sft_taxei_v4.jsonl\", \"data_count\": 9029, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"wall_clock_seconds\": 6801.0, \"gpu_hours\": 1.89}, \"reproduce\": {\"finished_at\": \"2026-05-14T23:41:32.774Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T23:41:33.984355+00:00\"}]}, \"metrics\": {\"final_loss\": 0.35506879, \"token_accuracy\": 0.89978214, \"train_steps\": 3387, \"train_epochs\": 3, \"train_duration_min\": 109.2, \"train_runtime_sec\": 6549.432, \"train_speed_s_per_it\": 1.934, \"memory_gib\": 18.49}, \"checkpoint_path\": \"checkpoints/mini_taxei_sft_v4_seed123/v0-20260515-055026/checkpoint-3387\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T23:43:38.819Z\"}, \"v4-random-recovery-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:04:57.591Z\", \"updated_at\": \"2026-05-14T22:00:43.285Z\", \"hypothesis\": \"v4 Random SFT seed=42 recovery eval (injected_eval.py) — 47 episodes with error injection, measuring detection/recovery/success rates under P1/P2/C1/C4 operators. Phase 2 counterpart to vanilla/taxei recovery eval.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 eval/injected_eval.py --model_path checkpoints/mini_random_sft_v4/v1-20260514-213104/checkpoint-3387 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --model_variant random --num_episodes 47 --seed 42 --device cuda:0 --output eval_results/v4_random_recovery_eval.json\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"pid\": 90124, \"model_name\": \"Qwen3-8B + LoRA (random SFT v4)\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/mini_random_sft_v4/v1-20260514-213104/checkpoint-3387\", \"eval_data\": \"valid_unseen (47 episodes)\", \"log_path\": \"/tmp/v4_random_recovery_eval.log\", \"output_path\": \"eval_results/v4_random_recovery_eval.json\", \"data_path\": \"valid_unseen\", \"data_count\": 47}, \"conclusion\": \"success\", \"checkpoint_path\": \"eval_results/v4_random_recovery_eval.json\", \"completed_at\": \"2026-05-14T21:42:07.544Z\", \"metrics\": {\"recovery_rate\": 0.638, \"detection_rate\": 0, \"successes\": 30, \"total\": 47, \"source\": \"json-file-verified\", \"note\": \"r1=29/47, r2=30/47, ±2pp run-to-run variance on P1 non-determinism\"}}, \"v4-taxei-recovery-eval-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:23:55.110Z\", \"updated_at\": \"2026-05-14T21:46:19.993Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 eval/injected_eval.py --model_path checkpoints/mini_taxei_sft_v4/v1-20260514-213102/checkpoint-3387 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --model_variant taxei --num_episodes 47 --seed 42 --device cuda:0 --output eval_results/v4_taxei_recovery_eval_r2.json\", \"server\": \"autodl-5090\", \"model_name\": \"Qwen3-8B + LoRA (mini_taxei_sft_v4 checkpoint-3387)\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/mini_taxei_sft_v4/v1-20260514-213102/checkpoint-3387\", \"eval_data\": \"47 episodes with error injection (4 operators: C1_context_truncation, C4_observation_masking, P1_step_order_swap, P2_sub_goal_deletion)\", \"data_path\": \"eval/injected_eval.py\", \"data_count\": 47, \"hypothesis\": \"v4 TaxEI SFT seed=42 recovery eval retry — 47 episodes with error injection, measuring detection/recovery/success rates. Previous attempt reported process dead 5x.\", \"pid\": 90519, \"log_path\": \"/tmp/v4_taxei_recovery_eval_r2.log\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"eval_results/v4_taxei_recovery_eval_r2.json\", \"completed_at\": \"2026-05-14T21:42:08.000Z\", \"metrics\": {\"recovery_rate\": 0.596, \"detection_rate\": 0, \"total_episodes\": 47, \"per_operator\": {\"C1_context_truncation\": {\"recovered\": 8, \"total\": 12, \"rate\": 0.667}, \"C4_observation_masking\": {\"recovered\": 7, \"total\": 11, \"rate\": 0.636}, \"P1_step_order_swap\": {\"recovered\": 7, \"total\": 12, \"rate\": 0.583}, \"P2_sub_goal_deletion\": {\"recovered\": 6, \"total\": 12, \"rate\": 0.5}}}}, \"v4-taxei-seed0-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:30:26.278Z\", \"updated_at\": \"2026-05-14T21:21:53.154Z\", \"hypothesis\": \"v4 TaxEI SFT seed=0 eval — multi-seed verification, 9029 samples, testing TaxEI injection stability\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 eval/recovery.py --model_path checkpoints/mini_taxei_sft_v4_seed0/v0-20260515-014320/checkpoint-3387 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_taxei_seed0_eval.json --device cuda:0\", \"server\": \"autodl-5090\", \"data_path\": \"eval/valid_unseen\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (taxei v4 seed=0)\", \"seed\": 0, \"checkpoint_source\": \"checkpoints/mini_taxei_sft_v4_seed0/v0-20260515-014320/checkpoint-3387\", \"eval_data\": \"47 ALFWorld tasks (clean, no injection)\", \"parent\": \"v4-taxei-seed0\", \"checkpoint_path\": \"eval_results/v4_taxei_seed0_eval.json\", \"log_path\": \"eval_results/v4_taxei_seed0_eval.log\"}, \"conclusion\": \"success\", \"metrics\": {\"eval_success_rate\": 0.468, \"eval_successes\": 22, \"eval_total\": 47, \"vs_seed42_pp\": -14.9}, \"completed_at\": \"2026-05-14T21:20:13.351Z\"}, \"v4-random-seed0-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:30:26.456Z\", \"updated_at\": \"2026-05-14T21:21:52.271Z\", \"hypothesis\": \"v4 Random SFT seed=0 eval — multi-seed verification, 9029 samples, testing random injection stability\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python3 eval/recovery.py --model_path checkpoints/mini_random_sft_v4_seed0/v0-20260515-014329/checkpoint-3387 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_random_seed0_eval.json --device cuda:0\", \"server\": \"autodl-5090\", \"data_path\": \"eval/valid_unseen\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (random v4 seed=0)\", \"seed\": 0, \"checkpoint_source\": \"checkpoints/mini_random_sft_v4_seed0/v0-20260515-014329/checkpoint-3387\", \"eval_data\": \"47 ALFWorld tasks (clean, no injection)\", \"parent\": \"v4-random-seed0\", \"log_path\": \"eval_results/v4_random_seed0_eval.log\"}, \"conclusion\": \"success\", \"metrics\": {\"eval_success_rate\": 0.553, \"eval_successes\": 26, \"eval_total\": 47, \"vs_seed42_pp\": -10.7}, \"checkpoint_path\": \"eval_results/v4_random_seed0_eval.json\", \"completed_at\": \"2026-05-14T21:20:14.339Z\"}, \"v4-taxei-recovery-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:40:41.154Z\", \"updated_at\": \"2026-05-14T21:20:17.664Z\", \"spec\": {\"hypothesis\": \"D010 Phase 2: Recovery eval with action injection on TaxEI seed=42 checkpoint — measuring TaxEI-trained model's recovery ability vs vanilla\", \"command\": \"CUDA_VISIBLE_DEVICES=3 python3 eval/injected_eval.py --model_path /root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_taxei_sft_v4/v1-20260514-213102/checkpoint-3387 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --model_variant taxei --device cuda:0 --seed 42 --output eval_results/v4_taxei_recovery_eval.json\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"pid\": 87614, \"data_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_taxei_sft_v4/v1-20260514-213102/checkpoint-3387\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + TaxEI LoRA v4 checkpoint-3387\", \"seed\": 42, \"checkpoint_source\": \"mini_taxei_sft_v4/v1-20260514-213102/checkpoint-3387\", \"eval_data\": \"ALFWorld valid_unseen 47 tasks with action injection\", \"checkpoint_path\": \"eval_results/v4_taxei_recovery_eval.json\", \"log_path\": \"/root/runs/tax_error_inject_agent/v4-taxei-recovery-eval.log\"}, \"hypothesis\": \"v4 TaxEI SFT seed=42 recovery eval (injected_eval.py) — 47 episodes with error injection, measuring detection/recovery/success rates under P1/P2/C1/C4 operators. Phase 2 counterpart to vanilla recovery eval.\", \"reproduce\": {\"finished_at\": \"2026-05-14T20:58:38.335Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T20:58:38.665Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T20:58:39.601019+00:00\"}]}, \"metrics\": {\"success_rate\": 0.596, \"successes\": 28, \"total\": 47, \"recovery_rate\": 0.596, \"detection_rate\": 0}}, \"v4-vanilla-seed123-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:30:26.635Z\", \"updated_at\": \"2026-05-14T20:43:48.780Z\", \"hypothesis\": \"v4 Vanilla SFT seed=123 eval — multi-seed verification, 4358 samples, comparing with seed=42 baseline (61.7%)\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python3 eval/recovery.py --model_path checkpoints/mini_vanilla_sft_v4_seed123/v1-20260515-022602/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_vanilla_seed123_eval.json --device cuda:0\", \"server\": \"autodl-5090\", \"model_name\": \"Qwen3-8B + LoRA (vanilla v4 seed=123)\", \"seed\": 123, \"checkpoint_source\": \"checkpoints/mini_vanilla_sft_v4_seed123/v1-20260515-022602/checkpoint-1635\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_vanilla_sft_v4_seed123/v1-20260515-022602/checkpoint-1635\", \"log_path\": \"/tmp/v4_vanilla_seed123_eval.log\", \"eval_data\": \"47 ALFWorld tasks (clean, no injection)\", \"parent\": \"v4-vanilla-seed123\", \"data_path\": \"eval/valid_unseen\", \"data_count\": 47}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T20:37:11.382Z\", \"metrics\": {\"eval_success_rate\": 0.66, \"eval_successes\": 31, \"eval_total\": 47, \"vs_seed42_pp\": 4.3, \"vs_seed0_pp\": -2.1, \"per_task\": {\"look_at_obj_in_light\": {\"success\": 5, \"total\": 6, \"rate\": 0.833}, \"pick_and_place_simple\": {\"success\": 6, \"total\": 8, \"rate\": 0.75}, \"pick_clean_then_place_in_recep\": {\"success\": 5, \"total\": 11, \"rate\": 0.455}, \"pick_cool_then_place_in_recep\": {\"success\": 4, \"total\": 7, \"rate\": 0.571}, \"pick_heat_then_place_in_recep\": {\"success\": 7, \"total\": 8, \"rate\": 0.875}, \"pick_two_obj_and_place\": {\"success\": 4, \"total\": 7, \"rate\": 0.571}}}}, \"v4-random-seed0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:42:03.440Z\", \"updated_at\": \"2026-05-14T19:36:31.263Z\", \"hypothesis\": \"v4 Random SFT seed=0 (multi-seed verification) — 9,029 samples, same hyperparams as seed=42, testing result stability\", \"spec\": {\"data_path\": \"data/mini_pipeline_v4/sft_random_v4.jsonl\", \"data_count\": 9029, \"model_name\": \"Qwen3-8B\", \"seed\": 0, \"server\": \"autodl-5090\", \"command\": \"swift sft --model Qwen3-8B --dataset sft_random_v4.jsonl --seed 0\", \"gpu\": \"cuda:2\", \"pid\": 72303, \"log_path\": \"/root/runs/tax_error_inject_agent/v4-random-seed0.log\", \"checkpoint_path\": \"checkpoints/mini_random_sft_v4_seed0/v0-20260515-014329/checkpoint-3387\"}, \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.355, \"token_accuracy\": 0.912, \"train_steps\": 3387, \"train_epochs\": 3, \"train_duration_min\": 110}, \"completed_at\": \"2026-05-14T19:35:39.420Z\"}, \"v4-taxei-seed0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:42:02.696Z\", \"updated_at\": \"2026-05-14T19:36:29.716Z\", \"hypothesis\": \"v4 TaxEI SFT seed=0 (multi-seed verification) — 9,029 samples, same hyperparams as seed=42, testing result stability\", \"spec\": {\"data_path\": \"data/mini_pipeline_v4/sft_taxei_v4.jsonl\", \"data_count\": 9029, \"model_name\": \"Qwen3-8B\", \"seed\": 0, \"server\": \"autodl-5090\", \"command\": \"swift sft --model Qwen3-8B --dataset sft_taxei_v4.jsonl --seed 0\", \"gpu\": \"cuda:1\", \"pid\": 71822, \"log_path\": \"/root/runs/tax_error_inject_agent/v4-taxei-seed0.log\", \"checkpoint_path\": \"checkpoints/mini_taxei_sft_v4_seed0/v0-20260515-014320/checkpoint-3387\"}, \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.355, \"token_accuracy\": 0.917, \"train_steps\": 3387, \"train_epochs\": 3, \"train_duration_min\": 110}, \"completed_at\": \"2026-05-14T19:35:37.503Z\"}, \"v4-vanilla-seed0-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:30:26.093Z\", \"updated_at\": \"2026-05-14T19:30:45.170Z\", \"hypothesis\": \"v4 Vanilla SFT seed=0 eval — multi-seed verification, 4358 samples, comparing with seed=42 baseline (61.7%)\", \"spec\": {\"checkpoint_path\": \"eval_results/v4_vanilla_seed0_eval.json\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-vanilla-seed0-eval.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T19:01:19.696Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T19:01:20.697938+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"eval_success_rate\": 0.681, \"eval_successes\": 32, \"eval_total\": 47, \"vs_seed42_pp\": 6.4, \"mcnemar_vs_seed42_p\": 0.375, \"discordant_pairs\": 5, \"per_task\": {\"look_at_obj_in_light\": \"5/6 (83.3%)\", \"pick_and_place_simple\": \"5/8 (62.5%)\", \"pick_clean_then_place\": \"6/11 (54.5%)\", \"pick_cool_then_place\": \"4/7 (57.1%)\", \"pick_heat_then_place\": \"7/8 (87.5%)\", \"pick_two_obj_and_place\": \"5/7 (71.4%)\"}}, \"completed_at\": \"2026-05-14T19:29:37.198Z\"}, \"v4-vanilla-seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:45:23.836Z\", \"updated_at\": \"2026-05-14T19:29:24.021Z\", \"hypothesis\": \"D010 Phase 1: v4 Vanilla SFT seed=123 多种子验证 — 4,358 samples, LoRA rank=16, 3 epochs, 与 seed=42 的 61.7% 对比波动范围\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/sft_vanilla_v4.jsonl --output_dir checkpoints/mini_vanilla_sft_v4_seed123 --lora_rank 16 --lora_alpha 32 --lora_dropout 0.05 --target_modules all-linear --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --max_length 4096 --num_train_epochs 3 --learning_rate 1e-4 --seed 123 --torch_dtype bfloat16 --logging_steps 5 --save_strategy epoch --gradient_checkpointing true\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"pid\": 77937, \"log_path\": \"checkpoints/mini_vanilla_sft_v4_seed123/v1-20260515-022602/logging.jsonl\", \"submitted_at\": \"2026-05-14T18:20:42.388Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/mini_pipeline_v4/sft_vanilla_v4.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"checkpoint_path\": \"checkpoints/mini_vanilla_sft_v4_seed123\", \"note\": \"OOM on first attempt (v0), restarted as v1 with PID 77937\", \"wall_clock_seconds\": 3941.6, \"gpu_hours\": 1.09}, \"reproduce\": {\"finished_at\": \"2026-05-14T19:26:23.312Z\"}, \"failure_reason\": \"v0 OOM at model loading (GPU 3 occupied by another process, 18.21 GiB in use). v1 (PID 77937) actually completed 1635/1635 steps. Cron caught v0's EXIT_CODE=1. Verifying checkpoint validity...\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T19:26:23.949Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T19:26:24.909318+00:00\"}]}, \"metrics\": {\"final_loss\": 0.288, \"token_accuracy\": 0.903, \"train_steps\": 1635, \"train_epochs\": 3, \"train_duration_min\": 58.9}}, \"v4-vanilla-seed0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:42:01.929Z\", \"updated_at\": \"2026-05-14T18:46:58.919Z\", \"hypothesis\": \"D010 Phase 1: v4 Vanilla SFT seed=0 多种子验证 — 4,358 samples, LoRA rank=16, 3 epochs, 与 seed=42 的 61.7% 对比波动范围\", \"spec\": {\"data_path\": \"data/mini_pipeline_v4/sft_vanilla_v4.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 0, \"server\": \"autodl-5090\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && CUDA_VISIBLE_DEVICES=0 swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/sft_vanilla_v4.jsonl --output_dir checkpoints/mini_vanilla_sft_v4_seed0 --lora_rank 16 --lora_alpha 32 --lora_dropout 0.05 --target_modules all-linear --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --max_length 4096 --num_train_epochs 3 --learning_rate 1e-4 --seed 0 --torch_dtype bfloat16 --logging_steps 5 --save_strategy epoch --gradient_checkpointing true\", \"gpu\": \"cuda:0\", \"pid\": 71959, \"log_path\": \"checkpoints/mini_vanilla_sft_v4_seed0/v0-20260515-014317/logging.jsonl\", \"checkpoint_path\": \"checkpoints/mini_vanilla_sft_v4_seed0/v0-20260515-014317/checkpoint-1635\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T18:42:56.365Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T18:42:57.338365+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.297, \"avg_loss\": 0.416, \"token_accuracy\": 0.902, \"train_steps\": 1635, \"train_epochs\": 3, \"train_duration_min\": 58}, \"completed_at\": \"2026-05-14T18:45:18.121Z\"}, \"traj_collect_500\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T06:45:21.504Z\", \"updated_at\": \"2026-05-14T16:28:02.238Z\", \"spec\": {\"command\": \"python collect_trajectories.py --target 500\", \"server\": \"autodl-5090\", \"data_path\": \"data/trajectories/\", \"data_count\": 575, \"model_name\": \"trajectory_collector\", \"seed\": 0, \"pid\": 11045, \"gpu\": \"none (CPU task)\", \"hypothesis\": \"GPT-5.2 可作为 teacher 在 ALFWorld 中收集高质量成功轨迹（预期成功率≥93%）\"}, \"metrics\": {\"successful_trajectories\": 501, \"failed_trajectories\": 213, \"total_attempts\": 714, \"success_rate\": 0.702, \"api_cost_usd\": 8.86, \"collection_time_sec\": 5245}, \"conclusion\": \"negative\", \"checkpoint_path\": \"data/trajectories/successful_trajectories.jsonl\", \"log_path\": \"/tmp/collect_500.log\", \"completed_at\": \"2026-05-14T12:21:11.941Z\"}, \"mini-vanilla-sft\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T10:51:41.382Z\", \"updated_at\": \"2026-05-14T10:54:48.860Z\", \"hypothesis\": \"Vanilla trajectory SFT baseline for comparison with TaxEI\", \"spec\": {\"command\": \"python3 scripts/train_sft.py --data data/sft_data/vanilla_train.jsonl --output checkpoints/mini_vanilla_sft/ --model Qwen3-8B --lora_rank 16 --seed 42 --epochs 3 --lr 1e-4\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"pid\": \"41874\", \"log_path\": \"eval_results/mini_vanilla_clean.json\", \"submitted_at\": \"2026-05-14T10:54:31.029Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/sft_data/vanilla_train.jsonl\", \"data_count\": 278, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"hypothesis\": \"Vanilla SFT on clean trajectories as baseline for comparison\", \"checkpoint_path\": \"checkpoints/mini_vanilla_sft/v0-20260514-181708/checkpoint-54\", \"wall_clock_seconds\": 17.8, \"gpu_hours\": 0.0}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T10:54:20.210Z\", \"metrics\": {\"eval_success_rate\": 0.149, \"eval_successes\": 7, \"eval_total\": 47, \"vs_baseline_pp\": -27.7, \"per_task\": {\"look_at_obj_in_light\": \"0/6 (0%)\", \"pick_and_place_simple\": \"2/8 (25.0%)\", \"pick_clean_then_place\": \"2/11 (18.2%)\", \"pick_cool_then_place\": \"0/7 (0%)\", \"pick_heat_then_place\": \"3/8 (37.5%)\", \"pick_two_obj_and_place\": \"0/7 (0%)\"}, \"train_steps\": 54, \"train_duration_min\": 5}}, \"mini-taxei-sft\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T10:51:40.784Z\", \"updated_at\": \"2026-05-14T10:54:46.174Z\", \"hypothesis\": \"TaxEI injection + recovery SFT improves over vanilla SFT on ALFWorld 47-task eval\", \"spec\": {\"command\": \"python3 scripts/train_sft.py --data data/sft_data/taxei_train.jsonl --output checkpoints/mini_taxei_sft/ --model Qwen3-8B --lora_rank 16 --seed 42 --epochs 3 --lr 1e-4\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"pid\": \"41263\", \"log_path\": \"eval_results/mini_taxei_clean.json\", \"submitted_at\": \"2026-05-14T10:53:16.579Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/sft_data/taxei_train.jsonl\", \"data_count\": 278, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_path\": \"checkpoints/mini_taxei_sft/v0-20260514-181630/checkpoint-195\", \"hypothesis\": \"TaxEI error injection + recovery SFT improves over vanilla SFT and baseline\", \"wall_clock_seconds\": 63.1, \"gpu_hours\": 0.04}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T10:54:19.721Z\", \"metrics\": {\"eval_success_rate\": 0.447, \"eval_successes\": 21, \"eval_total\": 47, \"vs_baseline_pp\": 2.1, \"per_task\": {\"look_at_obj_in_light\": \"3/6 (50.0%)\", \"pick_and_place_simple\": \"2/8 (25.0%)\", \"pick_clean_then_place\": \"6/11 (54.5%)\", \"pick_cool_then_place\": \"1/7 (14.3%)\", \"pick_heat_then_place\": \"6/8 (75.0%)\", \"pick_two_obj_and_place\": \"3/7 (42.9%)\"}, \"train_steps\": 195, \"train_duration_min\": 16.3}}, \"vanilla-react-baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:20:00.119Z\", \"updated_at\": \"2026-05-14T10:54:35.171Z\", \"spec\": {\"command\": \"python3 eval/recovery.py --model_path /root/autodl-tmp/models/Qwen/Qwen3-8B --eval_split valid_unseen --no_inject (MAX_STEPS=50 hardcoded)\", \"server\": \"autodl-5090\", \"data_path\": \"ALFWorld valid_unseen (47/85 tasks, solvable=True filter, pick_and_place_with_movable_recep excluded 0/11)\", \"data_count\": 47, \"model_name\": \"Qwen3-8B (zero-shot, enable_thinking=False)\", \"seed\": 42, \"gpu\": \"cuda:1\", \"hypothesis\": \"Qwen3-8B zero-shot ReAct 在 ALFWorld valid_unseen 的基线成功率，作为 SFT 对比的 lower bound\", \"checkpoint_path\": \"N/A (zero-shot, no training)\", \"log_path\": \"/root/autodl-tmp/tax_error_inject_agent/eval_results/vanilla_react_baseline.json\"}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.426, \"total_tasks\": 47, \"successes\": 20, \"per_task_type\": {\"pick_heat_then_place\": {\"success\": 5, \"total\": 8, \"rate\": 0.625}, \"look_at_obj_in_light\": {\"success\": 3, \"total\": 6, \"rate\": 0.5}, \"pick_and_place_simple\": {\"success\": 4, \"total\": 8, \"rate\": 0.5}, \"pick_clean_then_place\": {\"success\": 5, \"total\": 11, \"rate\": 0.455}, \"pick_two_obj_and_place\": {\"success\": 3, \"total\": 7, \"rate\": 0.429}, \"pick_cool_then_place\": {\"success\": 0, \"total\": 7, \"rate\": 0}}}, \"completed_at\": \"2026-05-14T08:58:00.892Z\"}, \"sft-dryrun-73\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:19:34.694Z\", \"updated_at\": \"2026-05-14T08:20:00.752Z\", \"spec\": {\"command\": \"swift sft --config configs/sft_vanilla.yaml (dry-run, 1 epoch, bs=1, max_length=2048)\", \"server\": \"autodl-5090\", \"data_path\": \"data/trajectories/ (124 successful trajectories)\", \"data_count\": 124, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"gpu\": \"cuda:0\", \"hypothesis\": \"SFT pipeline 端到端验证：注入→格式化→训练流程是否正常工作\", \"checkpoint_path\": \"checkpoints/dryrun_sft_v2/v0-20260514-161410/checkpoint-8/\", \"log_path\": \"checkpoints/dryrun_sft_v2/v0-20260514-161410/\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T08:19:52.165Z\", \"metrics\": {\"train_loss_init\": 2.436, \"train_loss_final\": 1.543, \"train_loss_avg\": 1.894, \"peak_memory_gib\": 19.22, \"steps\": 8, \"duration_sec\": 42, \"data_vanilla\": 124, \"data_injected_dryrun\": 96, \"injected_failed\": 4}}}, \"count\": 128, \"total\": 128, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5366}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-16T14:53:32.600Z_

<details><summary>↩ Tool result · `toolu_01Hdy4jeVY8PrRs3uUijW5Fd`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"llama31-random-s123\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T12:52:25.749Z\", \"updated_at\": \"2026-05-16T12:53:57.052Z\", \"spec\": {\"command\": \"swift sft --model /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct --dataset data/mini_pipeline_v4/sft_random_v4.jsonl --output_dir output/llama31-random-s123 --lora_rank 16 --num_train_epochs 3 --per_device_train_batch_size 4 --gradient_accumulation_steps 2 --learning_rate 1e-4 --max_length 4096 --seed 123 --data_seed 123 --logging_steps 10 --gradient_checkpointing true --bf16 true --save_strategy epoch\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"277565\", \"log_path\": \"~/runs/tax_error_inject_agent/llama31-random-s123.log\", \"submitted_at\": \"2026-05-16T12:52:25.330Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/mini_pipeline_v4/sft_random_v4.jsonl\", \"data_count\": 9029, \"model_name\": \"Meta-Llama-3.1-8B-Instruct\", \"seed\": 123}, \"hypothesis\": \"Cross-model: LLaMA Random s123 - 3rd seed for 3-seed cross-model validation\"}, \"llama31-taxei-s123\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T12:52:24.059Z\", \"updated_at\": \"2026-05-16T12:53:54.498Z\", \"spec\": {\"command\": \"swift sft --model /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct --dataset data/mini_pipeline_v4/sft_taxei_v4.jsonl --output_dir output/llama31-taxei-s123 --lora_rank 16 --num_train_epochs 3 --per_device_train_batch_size 4 --gradient_accumulation_steps 2 --learning_rate 1e-4 --max_length 4096 --seed 123 --data_seed 123 --logging_steps 10 --gradient_checkpointing true --bf16 true --save_strategy epoch\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"277419\", \"log_path\": \"~/runs/tax_error_inject_agent/llama31-taxei-s123.log\", \"submitted_at\": \"2026-05-16T12:52:23.670Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/mini_pipeline_v4/sft_taxei_v4.jsonl\", \"data_count\": 9029, \"model_name\": \"Meta-Llama-3.1-8B-Instruct\", \"seed\": 123}, \"hypothesis\": \"Cross-model: LLaMA TaxEI s123 - 3rd seed for 3-seed cross-model validation\"}}, \"count\": 2, \"total\": 2, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4226}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55",
  "uuid": "57d54223-a1cd-4bde-af6c-c1d8a84c67ab",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"llama31-random-s123\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-16T12:52:25.749Z\\\", \\\"updated_at\\\": \\\"2026-05-16T12:53:57.052Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"swift sft --model /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct --dataset data/mini_pipeline_v4/sft_random_v4.jsonl --output_dir output/llama31-random-s123 --lora_rank 16 --num_train_epochs 3 --per_device_train_batch_size 4 --gradient_accumulation_steps 2 --learning_rate 1e-4 --max_length 4096 --seed 123 --data_seed 123 --logging_steps 10 --gradient_checkpointing true --bf16 true --save_strategy epoch\\\", \\\"server\\\": \\\"autodl-5090\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"pid\\\": \\\"277565\\\", \\\"log_path\\\": \\\"~/runs/tax_error_inject_agent/llama31-random-s123.log\\\", \\\"submitted_at\\\": \\\"2026-05-16T12:52:25.330Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"data/mini_pipeline_v4/sft_random_v4.jsonl\\\", \\\"data_count\\\": 9029, \\\"model_name\\\": \\\"Meta-Llama-3.1-8B-Instruct\\\", \\\"seed\\\": 123}, \\\"hypothesis\\\": \\\"Cross-model: LLaMA Random s123 - 3rd seed for 3-seed cross-model validation\\\"}, \\\"llama31-taxei-s123\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-16T12:52:24.059Z\\\", \\\"updated_at\\\": \\\"2026-05-16T12:53:54.498Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"swift sft --model /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct --dataset data/mini_pipeline_v4/sft_taxei_v4.jsonl --output_dir output/llama31-taxei-s123 --lora_rank 16 --num_train_epochs 3 --per_device_train_batch_size 4 --gradient_accumulation_steps 2 --learning_rate 1e-4 --max_length 4096 --seed 123 --data_seed 123 --logging_steps 10 --gradient_checkpointing true --bf16 true --save_strategy epoch\\\", \\\"server\\\": \\\"autodl-5090\\\", \\\"gpu\\\": [\\\"cuda:2\\\"], \\\"pid\\\": \\\"277419\\\", \\\"log_path\\\": \\\"~/runs/tax_error_inject_agent/llama31-taxei-s123.log\\\", \\\"submitted_at\\\": \\\"2026-05-16T12:52:23.670Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"data/mini_pipeline_v4/sft_taxei_v4.jsonl\\\", \\\"data_count\\\": 9029, \\\"model_name\\\": \\\"Meta-Llama-3.1-8B-Instruct\\\", \\\"seed\\\": 123}, \\\"hypothesis\\\": \\\"Cross-model: LLaMA TaxEI s123 - 3rd seed for 3-seed cross-model validation\\\"}}, \\\"count\\\": 2, \\\"total\\\": 2, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4226}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"llama31-random-s123\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T12:52:25.749Z\", \"updated_at\": \"2026-05-16T12:53:57.052Z\", \"spec\": {\"command\": \"swift sft --model /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct --dataset data/mini_pipeline_v4/sft_random_v4.jsonl --output_dir output/llama31-random-s123 --lora_rank 16 --num_train_epochs 3 --per_device_train_batch_size 4 --gradient_accumulation_steps 2 --learning_rate 1e-4 --max_length 4096 --seed 123 --data_seed 123 --logging_steps 10 --gradient_checkpointing true --bf16 true --save_strategy epoch\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"277565\", \"log_path\": \"~/runs/tax_error_inject_agent/llama31-random-s123.log\", \"submitted_at\": \"2026-05-16T12:52:25.330Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/mini_pipeline_v4/sft_random_v4.jsonl\", \"data_count\": 9029, \"model_name\": \"Meta-Llama-3.1-8B-Instruct\", \"seed\": 123}, \"hypothesis\": \"Cross-model: LLaMA Random s123 - 3rd seed for 3-seed cross-model validation\"}, \"llama31-taxei-s123\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T12:52:24.059Z\", \"updated_at\": \"2026-05-16T12:53:54.498Z\", \"spec\": {\"command\": \"swift sft --model /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct --dataset data/mini_pipeline_v4/sft_taxei_v4.jsonl --output_dir output/llama31-taxei-s123 --lora_rank 16 --num_train_epochs 3 --per_device_train_batch_size 4 --gradient_accumulation_steps 2 --learning_rate 1e-4 --max_length 4096 --seed 123 --data_seed 123 --logging_steps 10 --gradient_checkpointing true --bf16 true --save_strategy epoch\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"277419\", \"log_path\": \"~/runs/tax_error_inject_agent/llama31-taxei-s123.log\", \"submitted_at\": \"2026-05-16T12:52:23.670Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/mini_pipeline_v4/sft_taxei_v4.jsonl\", \"data_count\": 9029, \"model_name\": \"Meta-Llama-3.1-8B-Instruct\", \"seed\": 123}, \"hypothesis\": \"Cross-model: LLaMA TaxEI s123 - 3rd seed for 3-seed cross-model validation\"}}, \"count\": 2, \"total\": 2, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4226}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Agent · `toolu_01BbmLXayvRWQ5YLrpnBLT8u`</summary>

```json
{
  "description": "Extract llama31 registry data",
  "prompt": "I need to extract all experiments with IDs starting with \"llama31\" from a large JSON file. The file is at:\n/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/ae491a69-2268-4f52-bbd5-112d75ec9c55/tool-results/mcp-agent-ml-research-read_registry-1778943212143.txt\n\nThe file has schema: {result: string} where result is a JSON string containing experiment data.\n\nI need ALL experiments whose ID starts with \"llama31\" — extract their full details including: status, metrics, spec (seed, model, data_path), hypothesis, conclusion, and any eval results.\n\nAlso extract any experiments with \"qwen\" in the ID that have metrics/eval data for comparison.\n\nUse jq or python to parse. Report the extracted data verbatim — I need exact numbers.",
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
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55",
  "uuid": "d09aaea0-d388-4d9b-b15d-34ea2e61f111",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011rE9iyaJhxu4duja3rGNq2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1862,
      "cache_read_input_tokens": 24940,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1862
      },
      "output_tokens": 34,
      "service_tier": "standard",
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
  "task_id": "a1b20f795e02ae461",
  "tool_use_id": "toolu_01BbmLXayvRWQ5YLrpnBLT8u",
  "description": "Extract llama31 registry data",
  "task_type": "local_agent",
  "prompt": "I need to extract all experiments with IDs starting with \"llama31\" from a large JSON file. The file is at:\n/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/ae491a69-2268-4f52-bbd5-112d75ec9c55/tool-results/mcp-agent-ml-research-read_registry-1778943212143.txt\n\nThe file has schema: {result: string} where result is a JSON string containing experiment data.\n\nI need ALL experiments whose ID starts with \"llama31\" — extract their full details including: status, metrics, spec (seed, model, data_path), hypothesis, conclusion, and any eval results.\n\nAlso extract any experiments with \"qwen\" in the ID that have metrics/eval data for comparison.\n\nUse jq or python to parse. Report the extracted data verbatim — I need exact numbers.",
  "uuid": "ec076ac8-0335-4768-b2fc-2e234ea297f1",
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55"
}
```

---

## Round 1

47 recorded events

### User

_source line 14 · 2026-05-16T14:53:40.654Z_

I need to extract all experiments with IDs starting with "llama31" from a large JSON file. The file is at:
/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/ae491a69-2268-4f52-bbd5-112d75ec9c55/tool-results/mcp-agent-ml-research-read_registry-1778943212143.txt

The file has schema: {result: string} where result is a JSON string containing experiment data.

I need ALL experiments whose ID starts with "llama31" — extract their full details including: status, metrics, spec (seed, model, data_path), hypothesis, conclusion, and any eval results.

Also extract any experiments with "qwen" in the ID that have metrics/eval data for comparison.

Use jq or python to parse. Report the extracted data verbatim — I need exact numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01BbmLXayvRWQ5YLrpnBLT8u",
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55",
  "uuid": "0f53a98b-4cad-4a05-aae8-a33d00bc026d"
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
  "task_id": "a1b20f795e02ae461",
  "tool_use_id": "toolu_01BbmLXayvRWQ5YLrpnBLT8u",
  "description": "Reading ~/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/ae491a69-2268-4f52-bbd5-112d75ec9c55/tool-results/mcp-agent-ml-research-read_registry-1778943212143.txt",
  "usage": {
    "total_tokens": 14386,
    "tool_uses": 1,
    "duration_ms": 3186
  },
  "last_tool_name": "Read",
  "uuid": "bd0f0c45-04b8-4717-b608-f255f253ae0a",
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55"
}
```

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Read · `toolu_015D7mc11mMAw7EXg1mxiLkY`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/ae491a69-2268-4f52-bbd5-112d75ec9c55/tool-results/mcp-agent-ml-research-read_registry-1778943212143.txt",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01BbmLXayvRWQ5YLrpnBLT8u",
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55",
  "uuid": "c0f30018-f5d4-4aa9-b6b0-0008d9e2cf30",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0127yYyTHq5c62zVca2wgAT1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6656,
      "cache_read_input_tokens": 7667,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6656,
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

_source line 17 · 2026-05-16T14:53:44.155Z_

<details><summary>↩ Tool result · reported error · `toolu_015D7mc11mMAw7EXg1mxiLkY`</summary>

```text
File content (80951 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01BbmLXayvRWQ5YLrpnBLT8u",
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55",
  "uuid": "c956af13-556e-4dba-a0ce-23a1bec2e3fc",
  "tool_use_result": "Error: File content (80951 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
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
  "task_id": "a1b20f795e02ae461",
  "tool_use_id": "toolu_01BbmLXayvRWQ5YLrpnBLT8u",
  "description": "Running cd /home/ubuntu/.claude-account-3/projects/-home-…",
  "usage": {
    "total_tokens": 15447,
    "tool_uses": 2,
    "duration_ms": 9417
  },
  "last_tool_name": "Bash",
  "uuid": "53c8e9f7-e013-40a0-97d8-26aec66b52b9",
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55"
}
```

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Bash · `toolu_01HvnHq1nkyZm5LAATWq7XjV`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/ae491a69-2268-4f52-bbd5-112d75ec9c55/tool-results && python3 -c \"\nimport json\n\nwith open('mcp-agent-ml-research-read_registry-1778943212143.txt', 'r') as f:\n    raw = json.load(f)\n\n# The result field is a JSON string\ndata = json.loads(raw['result'])\n\n# Check the structure\nif isinstance(data, dict):\n    print('Top-level keys:', list(data.keys())[:20])\n    print('Type:', type(data))\nelif isinstance(data, list):\n    print('List of', len(data), 'items')\n    if data:\n        print('First item keys:', list(data[0].keys()) if isinstance(data[0], dict) else type(data[0]))\n\"\n",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01BbmLXayvRWQ5YLrpnBLT8u",
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55",
  "uuid": "c506b3fa-058b-448c-9c5a-0b07d2fb2e02",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0132mgbpyRLKhUzqGV2nqLJv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1061,
      "cache_read_input_tokens": 14323,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1061,
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

_source line 20 · 2026-05-16T14:53:50.812Z_

<details><summary>↩ Tool result · `toolu_01HvnHq1nkyZm5LAATWq7XjV`</summary>

```text
Top-level keys: ['success', 'data', 'error', 'metadata']
Type: &lt;class 'dict'>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01BbmLXayvRWQ5YLrpnBLT8u",
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55",
  "uuid": "c78946ed-fb23-46b0-a775-6fd0b7585ae4"
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
  "task_id": "a1b20f795e02ae461",
  "tool_use_id": "toolu_01BbmLXayvRWQ5YLrpnBLT8u",
  "description": "Running cd /home/ubuntu/.claude-account-3/projects/-home-…",
  "usage": {
    "total_tokens": 15895,
    "tool_uses": 3,
    "duration_ms": 16361
  },
  "last_tool_name": "Bash",
  "uuid": "e5b77bf5-2782-4f8c-886f-f4f8bd93f568",
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55"
}
```

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Bash · `toolu_019WjWsxYw619DJgWyhx4iGS`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/ae491a69-2268-4f52-bbd5-112d75ec9c55/tool-results && python3 -c \"\nimport json\n\nwith open('mcp-agent-ml-research-read_registry-1778943212143.txt', 'r') as f:\n    raw = json.load(f)\n\ndata = json.loads(raw['result'])\nprint('success:', data.get('success'))\nprint('error:', data.get('error'))\nprint('metadata:', data.get('metadata'))\n\ninner = data.get('data')\nif isinstance(inner, dict):\n    print('data keys:', list(inner.keys())[:30])\nelif isinstance(inner, list):\n    print('data is list of', len(inner), 'items')\nelif isinstance(inner, str):\n    # Maybe another layer of JSON\n    print('data is string, length:', len(inner))\n    try:\n        inner2 = json.loads(inner)\n        print('parsed inner type:', type(inner2))\n    except:\n        print('not parseable as JSON')\n\"\n",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01BbmLXayvRWQ5YLrpnBLT8u",
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55",
  "uuid": "5145af95-8a1a-4ea9-863f-73ed9640a3aa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LEERgMdYxSC7axu5Z7c7rX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 376,
      "cache_read_input_tokens": 15384,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 376,
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

_source line 23 · 2026-05-16T14:53:57.127Z_

<details><summary>↩ Tool result · `toolu_019WjWsxYw619DJgWyhx4iGS`</summary>

```text
success: True
error: None
metadata: {'elapsed_seconds': 0.5366}
data keys: ['experiments', 'count', 'total', 'baseline']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01BbmLXayvRWQ5YLrpnBLT8u",
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55",
  "uuid": "f3ba34c1-39e3-4a73-bcaa-04226799b6c7"
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
  "task_id": "a1b20f795e02ae461",
  "tool_use_id": "toolu_01BbmLXayvRWQ5YLrpnBLT8u",
  "description": "Running cd /home/ubuntu/.claude-account-3/projects/-home-…",
  "usage": {
    "total_tokens": 16388,
    "tool_uses": 4,
    "duration_ms": 25146
  },
  "last_tool_name": "Bash",
  "uuid": "bd4a6ed7-61f9-4a3b-a5cf-a806e66ade22",
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55"
}
```

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Bash · `toolu_01Rb3231xXiWnP6fDP3zWCfv`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/ae491a69-2268-4f52-bbd5-112d75ec9c55/tool-results && python3 -c \"\nimport json\n\nwith open('mcp-agent-ml-research-read_registry-1778943212143.txt', 'r') as f:\n    raw = json.load(f)\n\ndata = json.loads(raw['result'])\ninner = data['data']\nexperiments = inner['experiments']\n\nprint('Total experiments:', inner['total'])\nprint('Count in this response:', inner['count'])\nprint('Baseline:', inner.get('baseline'))\nprint()\n\n# Find all llama31 experiments\nllama31_exps = {k: v for k, v in experiments.items() if k.startswith('llama31')}\nprint(f'Found {len(llama31_exps)} experiments with ID starting with \\\"llama31\\\":')\nfor k in sorted(llama31_exps.keys()):\n    print(f'  - {k}')\n\nprint()\n\n# Find all qwen experiments with metrics/eval\nqwen_exps = {k: v for k, v in experiments.items() if 'qwen' in k.lower()}\nprint(f'Found {len(qwen_exps)} experiments with \\\"qwen\\\" in ID:')\nfor k in sorted(qwen_exps.keys()):\n    has_metrics = bool(v.get('metrics')) if isinstance((v := qwen_exps[k]), dict) else False\n    print(f'  - {k} (has metrics: {has_metrics})')\n\"\n",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01BbmLXayvRWQ5YLrpnBLT8u",
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55",
  "uuid": "53d6d4a4-efcf-4244-8bae-8af8af97d6e6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0155aLpFChaaiLyjP5NAww8y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 421,
      "cache_read_input_tokens": 15760,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 421,
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

_source line 26 · 2026-05-16T14:54:05.910Z_

<details><summary>↩ Tool result · `toolu_01Rb3231xXiWnP6fDP3zWCfv`</summary>

```text
Total experiments: 128
Count in this response: 128
Baseline: None

Found 18 experiments with ID starting with "llama31":
  - llama31-random-s0
  - llama31-random-s0-eval
  - llama31-random-s42
  - llama31-random-s42-clean
  - llama31-random-s42-eval
  - llama31-taxei-s0
  - llama31-taxei-s0-clean
  - llama31-taxei-s0-eval
  - llama31-taxei-s42
  - llama31-taxei-s42-eval
  - llama31-vanilla-s0
  - llama31-vanilla-s0-clean
  - llama31-vanilla-s0-eval
  - llama31-vanilla-s123
  - llama31-vanilla-s123-clean
  - llama31-vanilla-s42
  - llama31-vanilla-s42-clean
  - llama31-vanilla-s42-eval

Found 0 experiments with "qwen" in ID:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01BbmLXayvRWQ5YLrpnBLT8u",
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55",
  "uuid": "b5cfcacf-e496-49f7-836c-8619d67e7105"
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
  "task_id": "a1b20f795e02ae461",
  "tool_use_id": "toolu_01BbmLXayvRWQ5YLrpnBLT8u",
  "description": "Running cd /home/ubuntu/.claude-account-3/projects/-home-…",
  "usage": {
    "total_tokens": 17233,
    "tool_uses": 5,
    "duration_ms": 34893
  },
  "last_tool_name": "Bash",
  "uuid": "6c0382d9-4f82-4a4a-938f-43eaea477527",
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55"
}
```

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — Bash · `toolu_018T9oeL3qgCEtqrU57PFRZM`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/ae491a69-2268-4f52-bbd5-112d75ec9c55/tool-results && python3 -c \"\nimport json\n\nwith open('mcp-agent-ml-research-read_registry-1778943212143.txt', 'r') as f:\n    raw = json.load(f)\n\ndata = json.loads(raw['result'])\nexperiments = data['data']['experiments']\n\n# Check for qwen with different casing or partial match\nqwen_exps = {k: v for k, v in experiments.items() if 'qwen' in k.lower() or 'Qwen' in str(v)}\nprint(f'Qwen experiments (broader search): {len(qwen_exps)}')\nfor k in sorted(qwen_exps.keys()):\n    print(f'  - {k}')\n\n# Also list all experiment IDs to find qwen-like ones\nprint()\nprint('All experiment IDs:')\nfor k in sorted(experiments.keys()):\n    print(f'  {k}')\n\"\n",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01BbmLXayvRWQ5YLrpnBLT8u",
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55",
  "uuid": "0447f0f5-fb24-4a54-b7c0-35a9ad49904f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ajp8pyPNXbYk6VBDoRFqti",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 772,
      "cache_read_input_tokens": 16181,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 772,
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

_source line 29 · 2026-05-16T14:54:15.661Z_

<details><summary>↩ Tool result · `toolu_018T9oeL3qgCEtqrU57PFRZM`</summary>

```text
Qwen experiments (broader search): 89
  - eval-rp-s0
  - eval-rp-s1
  - eval-rp-s123
  - eval-rp-s42
  - eval-rp-s7
  - llama31-taxei-s42
  - mini-taxei-sft
  - mini-vanilla-sft
  - recovery-random-s1
  - recovery-random-s7
  - recovery-taxei-s1
  - recovery-taxei-s7
  - recovery-vanilla-s1
  - recovery-vanilla-s7
  - sft-dryrun-73
  - v4-random-fixed-inject10
  - v4-random-fixed-inject10-eval
  - v4-random-fixed-inject10-s0
  - v4-random-fixed-inject10-s0-eval-r3
  - v4-random-fixed-inject10-s1
  - v4-random-fixed-inject10-s1-eval
  - v4-random-fixed-inject10-s123
  - v4-random-fixed-inject10-s123-eval
  - v4-random-fixed-inject10-s7
  - v4-random-fixed-inject10-s7-eval
  - v4-random-fixed-inject25
  - v4-random-fixed-inject25-eval
  - v4-random-fixed-inject50-s1-eval
  - v4-random-fixed-inject50-s1-r2
  - v4-random-fixed-inject50-s7
  - v4-random-fixed-inject50-s7-eval
  - v4-random-recovery-eval
  - v4-random-recovery-eval-s0
  - v4-random-recovery-eval-s123
  - v4-random-seed0
  - v4-random-seed0-eval
  - v4-random-seed1
  - v4-random-seed1-eval
  - v4-random-seed123
  - v4-random-seed123-eval
  - v4-random-seed7
  - v4-random-seed7-eval
  - v4-taxei-fixed-inject10
  - v4-taxei-fixed-inject10-eval
  - v4-taxei-fixed-inject10-s0
  - v4-taxei-fixed-inject10-s1
  - v4-taxei-fixed-inject10-s1-eval
  - v4-taxei-fixed-inject10-s1-eval-r2
  - v4-taxei-fixed-inject10-s123
  - v4-taxei-fixed-inject10-s123-eval-r3
  - v4-taxei-fixed-inject10-s7
  - v4-taxei-fixed-inject10-s7-eval
  - v4-taxei-fixed-inject25
  - v4-taxei-fixed-inject25-eval
  - v4-taxei-fixed-inject25-r2
  - v4-taxei-fixed-inject25-s1
  - v4-taxei-fixed-inject25-s1-eval-r2
  - v4-taxei-fixed-inject25-s7-eval
  - v4-taxei-fixed-inject50
  - v4-taxei-fixed-inject50-eval
  - v4-taxei-fixed-inject50-s1-eval
  - v4-taxei-fixed-inject50-s1-r2
  - v4-taxei-fixed-inject50-s7
  - v4-taxei-fixed-inject50-s7-eval
  - v4-taxei-recovery-eval
  - v4-taxei-recovery-eval-r2
  - v4-taxei-rp-s0
  - v4-taxei-rp-s1
  - v4-taxei-rp-s123
  - v4-taxei-rp-s42
  - v4-taxei-rp-s7
  - v4-taxei-seed0
  - v4-taxei-seed0-eval
  - v4-taxei-seed1
  - v4-taxei-seed123
  - v4-taxei-seed123-eval
  - v4-taxei-seed7
  - v4-taxei-seed7-eval
  - v4-training-dynamics-forward
  - v4-training-dynamics-forward-v2
  - v4-vanilla-recovery-eval
  - v4-vanilla-seed0
  - v4-vanilla-seed1
  - v4-vanilla-seed1-eval
  - v4-vanilla-seed123
  - v4-vanilla-seed123-eval
  - v4-vanilla-seed7
  - v4-vanilla-seed7-eval
  - vanilla-react-baseline

All experiment IDs:
  eval-rp-s0
  eval-rp-s1
  eval-rp-s123
  eval-rp-s42
  eval-rp-s7
  llama31-random-s0
  llama31-random-s0-eval
  llama31-random-s42
  llama31-random-s42-clean
  llama31-random-s42-eval
  llama31-taxei-s0
  llama31-taxei-s0-clean
  llama31-taxei-s0-eval
  llama31-taxei-s42
  llama31-taxei-s42-eval
  llama31-vanilla-s0
  llama31-vanilla-s0-clean
  llama31-vanilla-s0-eval
  llama31-vanilla-s123
  llama31-vanilla-s123-clean
  llama31-vanilla-s42
  llama31-vanilla-s42-clean
  llama31-vanilla-s42-eval
  mini-taxei-sft
  mini-vanilla-sft
  recovery-random-s1
  recovery-random-s7
  recovery-taxei-s1
  recovery-taxei-s7
  recovery-vanilla-s1
  recovery-vanilla-s7
  sft-dryrun-73
  traj_collect_500
  v4-random-fixed-inject10
  v4-random-fixed-inject10-eval
  v4-random-fixed-inject10-s0
  v4-random-fixed-inject10-s0-eval
  v4-random-fixed-inject10-s0-eval-r3
  v4-random-fixed-inject10-s1
  v4-random-fixed-inject10-s1-eval
  v4-random-fixed-inject10-s123
  v4-random-fixed-inject10-s123-eval
  v4-random-fixed-inject10-s7
  v4-random-fixed-inject10-s7-eval
  v4-random-fixed-inject25
  v4-random-fixed-inject25-eval
  v4-random-fixed-inject25-s1
  v4-random-fixed-inject25-s1-eval
  v4-random-fixed-inject25-s7
  v4-random-fixed-inject25-s7-eval
  v4-random-fixed-inject50
  v4-random-fixed-inject50-eval
  v4-random-fixed-inject50-s1
  v4-random-fixed-inject50-s1-eval
  v4-random-fixed-inject50-s1-r2
  v4-random-fixed-inject50-s7
  v4-random-fixed-inject50-s7-eval
  v4-random-recovery-eval
  v4-random-recovery-eval-s0
  v4-random-recovery-eval-s123
  v4-random-seed0
  v4-random-seed0-eval
  v4-random-seed1
  v4-random-seed1-eval
  v4-random-seed123
  v4-random-seed123-eval
  v4-random-seed7
  v4-random-seed7-eval
  v4-recovery-paired-datagen
  v4-taxei-fixed-inject10
  v4-taxei-fixed-inject10-eval
  v4-taxei-fixed-inject10-s0
  v4-taxei-fixed-inject10-s0-eval
  v4-taxei-fixed-inject10-s1
  v4-taxei-fixed-inject10-s1-eval
  v4-taxei-fixed-inject10-s1-eval-r2
  v4-taxei-fixed-inject10-s123
  v4-taxei-fixed-inject10-s123-eval
  v4-taxei-fixed-inject10-s123-eval-r3
  v4-taxei-fixed-inject10-s7
  v4-taxei-fixed-inject10-s7-eval
  v4-taxei-fixed-inject25
  v4-taxei-fixed-inject25-eval
  v4-taxei-fixed-inject25-r2
  v4-taxei-fixed-inject25-s1
  v4-taxei-fixed-inject25-s1-eval
  v4-taxei-fixed-inject25-s1-eval-r2
  v4-taxei-fixed-inject25-s7
  v4-taxei-fixed-inject25-s7-eval
  v4-taxei-fixed-inject25-s7-eval-r2
  v4-taxei-fixed-inject50
  v4-taxei-fixed-inject50-eval
  v4-taxei-fixed-inject50-s1
  v4-taxei-fixed-inject50-s1-eval
  v4-taxei-fixed-inject50-s1-r2
  v4-taxei-fixed-inject50-s7
  v4-taxei-fixed-inject50-s7-eval
  v4-taxei-recovery-eval
  v4-taxei-recovery-eval-r2
  v4-taxei-recovery-eval-s0
  v4-taxei-recovery-eval-s123
  v4-taxei-rp-s0
  v4-taxei-rp-s1
  v4-taxei-rp-s123
  v4-taxei-rp-s42
  v4-taxei-rp-s7
  v4-taxei-seed0
  v4-taxei-seed0-eval
  v4-taxei-seed1
  v4-taxei-seed1-eval
  v4-taxei-seed123
  v4-taxei-seed123-eval
  v4-taxei-seed7
  v4-taxei-seed7-eval
  v4-training-dynamics-forward
  v4-training-dynamics-forward-v2
  v4-vanilla-recovery-eval
  v4-vanilla-recovery-eval-s0
  v4-vanilla-recovery-eval-s123
  v4-vanilla-seed0
  v4-vanilla-seed0-eval
  v4-vanilla-seed1
  v4-vanilla-seed1-eval
  v4-vanilla-seed123
  v4-vanilla-seed123-eval
  v4-vanilla-seed7
  v4-vanilla-seed7-eval
  vanilla-react-baseline
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01BbmLXayvRWQ5YLrpnBLT8u",
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55",
  "uuid": "50029ec5-6290-419c-8908-b9992f0b97a1"
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
  "task_id": "a1b20f795e02ae461",
  "tool_use_id": "toolu_01BbmLXayvRWQ5YLrpnBLT8u",
  "description": "Running cd /home/ubuntu/.claude-account-3/projects/-home-…",
  "usage": {
    "total_tokens": 20436,
    "tool_uses": 6,
    "duration_ms": 41486
  },
  "last_tool_name": "Bash",
  "uuid": "64870561-8c72-4949-8b49-7f564ec7bc04",
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55"
}
```

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Bash · `toolu_0168iwbVjiQ5Whz57FTDb1Q7`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/ae491a69-2268-4f52-bbd5-112d75ec9c55/tool-results && python3 -c \"\nimport json\n\nwith open('mcp-agent-ml-research-read_registry-1778943212143.txt', 'r') as f:\n    raw = json.load(f)\n\ndata = json.loads(raw['result'])\nexperiments = data['data']['experiments']\n\n# Extract all llama31 experiments with full details\nllama31_exps = {k: v for k, v in experiments.items() if k.startswith('llama31')}\n\nprint('='*80)\nprint('ALL LLAMA31 EXPERIMENTS - FULL DETAILS')\nprint('='*80)\n\nfor k in sorted(llama31_exps.keys()):\n    exp = llama31_exps[k]\n    print()\n    print('-'*80)\n    print(f'ID: {k}')\n    print('-'*80)\n    print(json.dumps(exp, indent=2, ensure_ascii=False))\n\" 2>&1",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01BbmLXayvRWQ5YLrpnBLT8u",
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55",
  "uuid": "169a0501-24a4-458b-9ab4-1bfe0df825dc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014x5AwMkTY4WwHM6MKniKTb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3201,
      "cache_read_input_tokens": 16953,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3201,
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

_source line 32 · 2026-05-16T14:54:22.322Z_

<details><summary>↩ Tool result · `toolu_0168iwbVjiQ5Whz57FTDb1Q7`</summary>

```text
&lt;persisted-output>
Output too large (30.3KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/ae491a69-2268-4f52-bbd5-112d75ec9c55/tool-results/bdn71yn3d.txt

Preview (first 2KB):
================================================================================
ALL LLAMA31 EXPERIMENTS - FULL DETAILS
================================================================================

--------------------------------------------------------------------------------
ID: llama31-random-s0
--------------------------------------------------------------------------------
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-16T09:16:00.115Z",
  "updated_at": "2026-05-16T11:28:10.720Z",
  "spec": {
    "command": "swift sft --model /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct --dataset data/mini_pipeline_v4/sft_random_v4.jsonl --output_dir output/llama31-random-s0 --lora_rank 16 --num_train_epochs 3 --per_device_train_batch_size 4 --gradient_accumulation_steps 2 --learning_rate 1e-4 --max_length 4096 --seed 0 --data_seed 0 --logging_steps 10 --gradient_checkpointing true --bf16 true --save_strategy epoch",
    "server": "autodl-5090",
    "gpu": [
      "cuda:2"
    ],
    "pid": "260936",
    "log_path": "~/runs/tax_error_inject_agent/llama31-random-s0.log",
    "submitted_at": "2026-05-16T09:15:59.761Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "data/mini_pipeline_v4/sft_random_v4.jsonl",
    "data_count": 9031,
    "model_name": "Meta-Llama-3.1-8B-Instruct",
    "seed": 0,
    "wall_clock_seconds": 7931.0,
    "gpu_hours": 2.2
  },
  "reproduce": {
    "finished_at": "2026-05-16T11:24:56.461Z"
  },
  "extra": {
    "hook_events": [
      {
        "event": "on_complete",
        "action": "agent",
        "ts": "2026-05-16T11:24:59.790065+00:00"
      }
    ]
  },
  "conclusion": "success",
  "metrics": {
    "final_train_loss": 0.3368,
    "epoch1_loss": 0.452,
    "epoch2_loss": 0.238,
    "epoch3_loss": 0.134,
    "final_token_acc": 0.9357,
    "train_runtime_sec": 7622,
    "train_steps": 3387,
    "peak_memory_gib": 30.74,
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01BbmLXayvRWQ5YLrpnBLT8u",
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55",
  "uuid": "2699b208-6b08-4b8f-8ac6-2ff7caf352a4"
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
  "task_id": "a1b20f795e02ae461",
  "tool_use_id": "toolu_01BbmLXayvRWQ5YLrpnBLT8u",
  "description": "Reading ~/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/ae491a69-2268-4f52-bbd5-112d75ec9c55/tool-results/bdn71yn3d.txt",
  "usage": {
    "total_tokens": 21750,
    "tool_uses": 7,
    "duration_ms": 44557
  },
  "last_tool_name": "Read",
  "uuid": "096f0603-7089-4bfe-9d7c-825ec689147a",
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55"
}
```

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Read · `toolu_011Tra6U54nTq5tQ2oHAayfw`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/ae491a69-2268-4f52-bbd5-112d75ec9c55/tool-results/bdn71yn3d.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01BbmLXayvRWQ5YLrpnBLT8u",
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55",
  "uuid": "0441932b-def7-4a68-af6e-803f108b7c63",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DK2kaKtHDXzbAgKLJeUnYv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1252,
      "cache_read_input_tokens": 20154,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1252,
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

_source line 35 · 2026-05-16T14:54:25.553Z_

<details><summary>↩ Tool result · `toolu_011Tra6U54nTq5tQ2oHAayfw`</summary>

```text
1	================================================================================
2	ALL LLAMA31 EXPERIMENTS - FULL DETAILS
3	================================================================================
4	
5	--------------------------------------------------------------------------------
6	ID: llama31-random-s0
7	--------------------------------------------------------------------------------
8	{
9	  "status": "DONE",
10	  "retry_count": 0,
11	  "created_at": "2026-05-16T09:16:00.115Z",
12	  "updated_at": "2026-05-16T11:28:10.720Z",
13	  "spec": {
14	    "command": "swift sft --model /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct --dataset data/mini_pipeline_v4/sft_random_v4.jsonl --output_dir output/llama31-random-s0 --lora_rank 16 --num_train_epochs 3 --per_device_train_batch_size 4 --gradient_accumulation_steps 2 --learning_rate 1e-4 --max_length 4096 --seed 0 --data_seed 0 --logging_steps 10 --gradient_checkpointing true --bf16 true --save_strategy epoch",
15	    "server": "autodl-5090",
16	    "gpu": [
17	      "cuda:2"
18	    ],
19	    "pid": "260936",
20	    "log_path": "~/runs/tax_error_inject_agent/llama31-random-s0.log",
21	    "submitted_at": "2026-05-16T09:15:59.761Z",
22	    "submitted_via": "submit_training_job",
23	    "backend": "tmux",
24	    "account": "root",
25	    "data_path": "data/mini_pipeline_v4/sft_random_v4.jsonl",
26	    "data_count": 9031,
27	    "model_name": "Meta-Llama-3.1-8B-Instruct",
28	    "seed": 0,
29	    "wall_clock_seconds": 7931.0,
30	    "gpu_hours": 2.2
31	  },
32	  "reproduce": {
33	    "finished_at": "2026-05-16T11:24:56.461Z"
34	  },
35	  "extra": {
36	    "hook_events": [
37	      {
38	        "event": "on_complete",
39	        "action": "agent",
40	        "ts": "2026-05-16T11:24:59.790065+00:00"
41	      }
42	    ]
43	  },
44	  "conclusion": "success",
45	  "metrics": {
46	    "final_train_loss": 0.3368,
47	    "epoch1_loss": 0.452,
48	    "epoch2_loss": 0.238,
49	    "epoch3_loss": 0.134,
50	    "final_token_acc": 0.9357,
51	    "train_runtime_sec": 7622,
52	    "train_steps": 3387,
53	    "peak_memory_gib": 30.74,
54	    "checkpoint_path": "/root/autodl-tmp/tax_error_inject_agent/output/llama31-random-s0/v0-20260516-171608/checkpoint-3387"
55	  },
56	  "checkpoint_path": "/root/autodl-tmp/tax_error_inject_agent/output/llama31-random-s0/v0-20260516-171608/checkpoint-3387",
57	  "log_path": "~/runs/tax_error_inject_agent/llama31-random-s0.log",
58	  "completed_at": "2026-05-16T11:28:10.720Z"
59	}
60	
61	--------------------------------------------------------------------------------
62	ID: llama31-random-s0-eval
63	--------------------------------------------------------------------------------
64	{
65	  "status": "DONE",
66	  "retry_count": 0,
67	  "created_at": "2026-05-16T11:58:20.799Z",
68	  "updated_at": "2026-05-16T11:59:00.205Z",
69	  "spec": {
70	    "command": "CUDA_VISIBLE_DEVICES=2 python3 eval/injected_eval.py --model_path output/llama31-random-s0/v0-20260516-171608/checkpoint-3387 --base_model /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct --model_variant random --num_episodes 47 --output eval_results/llama31_random_s0_injected.json",
71	    "server": "autodl-5090",
72	    "data_path": "eval/eval_tasks_47.json",
73	    "data_count": 47,
74	    "model_name": "Meta-Llama-3.1-8B-Instruct + LoRA random s0",
75	    "seed": 42,
76	    "checkpoint_source": "output/llama31-random-s0/v0-20260516-171608/checkpoint-3387",
77	    "eval_data": "ALFWorld valid_unseen 47 episodes injected"
78	  },
79	  "checkpoint_path": "output/llama31-random-s0/v0-20260516-171608/checkpoint-3387",
80	  "log_path": "eval_results/llama31_random_s0_injected.json",
81	  "conclusion": "success",
82	  "completed_at": "2026-05-16T11:58:51.624Z",
83	  "metrics": {
84	    "recovery_rate": 0.745,
85	    "detection_rate": 0.255,
86	    "success_rate": 0.745,
87	    "total_episodes": 47,
88	    "by_operator": {
89	      "C1_context_truncation": {
90	        "total": 12,
91	        "recovered": 10,
92	        "detected": 1,
93	        "recovery_rate": 0.833,
94	        "detection_rate": 0.083
95	      },
96	      "C4_observation_masking": {
97	        "total": 11,
98	        "recovered": 8,
99	        "detected": 4,
100	        "recovery_rate": 0.727,
101	        "detection_rate": 0.364
102	      },
103	      "P1_step_order_swap": {
104	        "total": 12,
105	        "recovered": 8,
106	        "detected": 4,
107	        "recovery_rate": 0.667,
108	        "detection_rate": 0.333
109	      },
110	      "P2_sub_goal_deletion": {
111	        "total": 12,
112	        "recovered": 9,
113	        "detected": 3,
114	        "recovery_rate": 0.75,
115	        "detection_rate": 0.25
116	      }
117	    }
118	  }
119	}
120	
121	--------------------------------------------------------------------------------
122	ID: llama31-random-s42
123	--------------------------------------------------------------------------------
124	{
125	  "status": "DONE",
126	  "retry_count": 0,
127	  "created_at": "2026-05-16T06:22:51.516Z",
128	  "updated_at": "2026-05-16T08:46:26.260Z",
129	  "spec": {
130	    "data_path": "/root/autodl-tmp/tax_error_inject_agent/data/mini_pipeline_v4/sft_random_v4.jsonl",
131	    "data_count": 9029,
132	    "model_name": "Meta-Llama-3.1-8B-Instruct",
133	    "seed": 42,
134	    "hypothesis": "Cross-model generalizability: LLaMA-3.1-8B Random condition control",
135	    "command": "llamafactory train",
136	    "server": "autodl-5090",
137	    "gpu": "cuda:2",
138	    "checkpoint_path": "/root/autodl-tmp/tax_error_inject_agent/output/llama31-random-s42/v0-20260516-142300/checkpoint-3387/",
139	    "log_path": "/root/autodl-tmp/tax_error_inject_agent/output/llama31-random-s42/v0-20260516-142300/logging.jsonl"
140	  },
141	  "reproduce": {
142	    "finished_at": "2026-05-16T08:32:16.672Z"
143	  },
144	  "extra": {
145	    "hook_events": [
146	      {
147	        "event": "on_complete",
148	        "action": "agent",
149	        "ts": "2026-05-16T08:32:20.396930+00:00"
150	      }
151	    ]
152	  },
153	  "metrics": {
154	    "train_loss": 0.3366,
155	    "token_acc": 0.9364,
156	    "train_steps": 3387,
157	    "train_duration_s": 7622
158	  },
159	  "conclusion": "success",
160	  "completed_at": "2026-05-16T08:39:26.528Z",
161	  "checkpoint_path": "/root/autodl-tmp/tax_error_inject_agent/output/llama31-random-s42/v0-20260516-142300/checkpoint-3387"
162	}
163	
164	--------------------------------------------------------------------------------
165	ID: llama31-random-s42-clean
166	--------------------------------------------------------------------------------
167	{
168	  "status": "DONE",
169	  "retry_count": 0,
170	  "created_at": "2026-05-16T11:30:37.651Z",
171	  "updated_at": "2026-05-16T13:19:33.606Z",
172	  "spec": {
173	    "command": "CUDA_VISIBLE_DEVICES=3 python3 eval/recovery.py --model_path output/llama31-random-s42/v0-20260516-142300/checkpoint-3387 --base_model /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct --num_episodes 47 --task_list eval/eval_tasks_47.json --output eval_results/llama31_random_s42_clean.json",
174	    "server": "autodl-5090",
175	    "data_path": "eval/eval_tasks_47.json",
176	    "data_count": 47,
177	    "model_name": "Meta-Llama-3.1-8B-Instruct + llama31-random-s42 LoRA",
178	    "seed": 42,
179	    "checkpoint_source": "output/llama31-random-s42/v0-20260516-142300/checkpoint-3387",
180	    "eval_data": "ALFWorld clean eval 47 tasks",
181	    "hypothesis": "LLaMA Random s42 clean eval - baseline success rate without injection"
182	  },
183	  "conclusion": "success",
184	  "metrics": {
185	    "success_rate": 0.766,
186	    "eval_type": "clean",
187	    "eval_script": "eval/recovery.py",
188	    "total_episodes": 47,
189	    "output_file": "eval_results/llama31_random_s42_clean.json"
190	  },
191	  "checkpoint_path": "/root/autodl-tmp/tax_error_inject_agent/output/llama31-random-s42/v0-20260516-142300/checkpoint-3387",
192	  "log_path": "eval_results/llama31_random_s42_clean.json",
193	  "completed_at": "2026-05-16T11:50:54.372Z"
194	}
195	
196	--------------------------------------------------------------------------------
197	ID: llama31-random-s42-eval
198	--------------------------------------------------------------------------------
199	{
200	  "status": "DONE",
201	  "retry_count": 0,
202	  "created_at": "2026-05-16T09:14:41.175Z",
203	  "updated_at": "2026-05-16T09:15:28.130Z",
204	  "spec": {
205	    "hypothesis": "Cross-model: LLaMA Random s42 eval — random injection control on LLaMA",
206	    "model_name": "Meta-Llama-3.1-8B-Instruct + Random LoRA",
207	    "seed": 42,
208	    "checkpoint_source": "/root/autodl-tmp/tax_error_inject_agent/output/llama31-random-s42/v0-20260516-142300/checkpoint-3387",
209	    "eval_data": "ALFWorld 47 injected tasks",
210	    "data_path": "eval/injected_eval.py (47 ALFWorld tasks)",
211	    "data_count": 47,
212	    "command": "CUDA_VISIBLE_DEVICES=2 python3 eval/injected_eval.py --model_path output/llama31-random-s42/v0-20260516-142300/checkpoint-3387 --base_model /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct --model_variant random --output_file eval_results/llama31_random_s42.json",
213	    "server": "autodl-5090"
214	  },
215	  "metrics": {
216	    "recovery_rate": 0.766,
217	    "recovery_count": "36/47",
218	    "detection_rate": 0.298,
219	    "C1_context_truncation": 0.667,
220	    "C4_observation_masking": 0.727,
221	    "P1_step_order_swap": 0.917,
222	    "P2_sub_goal_deletion": 0.75,
223	    "C1_detection": 0.417,
224	    "C4_detection": 0.364,
225	    "P1_detection": 0.333,
226	    "P2_detection": 0.083
227	  },
228	  "conclusion": "success",
229	  "checkpoint_path": "/root/autodl-tmp/tax_error_inject_agent/output/llama31-random-s42/v0-20260516-142300/checkpoint-3387",
230	  "log_path": "/root/autodl-tmp/tax_error_inject_agent/eval_results/llama31_random_s42.json",
231	  "completed_at": "2026-05-16T09:15:28.130Z"
232	}
233	
234	--------------------------------------------------------------------------------
235	ID: llama31-taxei-s0
236	--------------------------------------------------------------------------------
237	{
238	  "status": "DONE",
239	  "retry_count": 0,
240	  "created_at": "2026-05-16T09:15:57.399Z",
241	  "updated_at": "2026-05-16T12:39:46.148Z",
242	  "spec": {
243	    "command": "CUDA_VISIBLE_DEVICES=1 swift sft --model Meta-Llama-3.1-8B-Instruct --dataset sft_taxei_v4.jsonl --output_dir output/llama31-taxei-s0 --lora_rank 16 --num_train_epochs 3 --seed 0",
244	    "server": "autodl-5090",
245	    "gpu": [
246	      "cuda:1"
247	    ],
248	    "pid": "262833",
249	    "log_path": "~/runs/tax_error_inject_agent/llama31-taxei-s0.log",
250	    "submitted_at": "2026-05-16T09:15:57.070Z",
251	    "submitted_via": "manual_retry_v1",
252	    "backend": "interactive_pts",
253	    "account": "root",
254	    "data_path": "/root/autodl-tmp/tax_error_inject_agent/data/mini_pipeline_v4/sft_taxei_v4.jsonl",
255	    "data_count": 9029,
256	    "model_name": "Meta-Llama-3.1-8B-Instruct",
257	    "seed": 0,
258	    "hypothesis": "Cross-model: LLaMA TaxEI s0 - 2nd seed for 3-seed cross-model validation",
259	    "wall_clock_seconds": 11561.0,
260	    "gpu_hours": 3.21
261	  },
262	  "reproduce": {
263	    "finished_at": "2026-05-16T12:28:37.402Z"
264	  },
265	  "failure_reason": "EXIT_CODE=129 (non-zero)",
266	  "conclusion": "success",
267	  "extra": {
268	    "hook_events": [
269	      {
270	        "event": "on_failed",
271	        "action": "agent",
272	        "ts": "2026-05-16T10:20:11.090300+00:00"
273	      },
274	      {
275	        "event": "on_failed",
276	        "action": "agent",
277	        "ts": "2026-05-16T12:28:42.837165+00:00"
278	      }
279	    ]
280	  },
281	  "completed_at": "2026-05-16T12:28:38.032Z",
282	  "metrics": {
283	    "final_train_loss": 0.32,
284	    "final_token_acc": 0.88,
285	    "train_steps": 3387,
286	    "checkpoint_path": "/root/autodl-tmp/tax_error_inject_agent/output/llama31-taxei-s0/v1-20260516-181826/checkpoint-3387"
287	  },
288	  "checkpoint_path": "/root/autodl-tmp/tax_error_inject_agent/output/llama31-taxei-s0/v1-20260516-181826/checkpoint-3387"
289	}
290	
291	--------------------------------------------------------------------------------
292	ID: llama31-taxei-s0-clean
293	--------------------------------------------------------------------------------
294	{
295	  "status": "DONE",
296	  "retry_count": 0,
297	  "created_at": "2026-05-16T14:05:45.875Z",
298	  "updated_at": "2026-05-16T14:06:24.173Z",
299	  "hypothesis": "Cross-model: LLaMA TaxEI s0 clean eval — baseline task success without injection",
300	  "spec": {
301	    "command": "python3 eval/recovery.py --model_path output/llama31-taxei-s0/v1-20260516-181826/checkpoint-3387 --base_model /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct --num_episodes 47 --task_list eval/eval_tasks_47.json --output eval_results/llama31_taxei_s0_clean.json",
302	    "server": "autodl-5090",
303	    "data_path": "eval/eval_tasks_47.json",
304	    "data_count": 47,
305	    "model_name": "Meta-Llama-3.1-8B-Instruct + taxei-s0 LoRA",
306	    "seed": 0,
307	    "checkpoint_source": "output/llama31-taxei-s0/v1-20260516-181826/checkpoint-3387",
308	    "eval_data": "clean_eval_47ep",
309	    "checkpoint_path": "/root/autodl-tmp/tax_error_inject_agent/output/llama31-taxei-s0/v1-20260516-181826/checkpoint-3387",
310	    "log_path": "/root/autodl-tmp/tax_error_inject_agent/eval_results/llama31_taxei_s0_clean.json"
311	  },
312	  "conclusion": "success",
313	  "metrics": {
314	    "success_rate": 0.766,
315	    "total_episodes": 47
316	  },
317	  "completed_at": "2026-05-16T14:06:24.173Z"
318	}
319	
320	--------------------------------------------------------------------------------
321	ID: llama31-taxei-s0-eval
322	--------------------------------------------------------------------------------
323	{
324	  "status": "DONE",
325	  "retry_count": 0,
326	  "created_at": "2026-05-16T12:52:20.766Z",
327	  "updated_at": "2026-05-16T14:04:47.458Z",
328	  "spec": {
329	    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && python3 eval/injected_eval.py --model_path output/llama31-taxei-s0/v1-20260516-181826/checkpoint-3387 --base_model /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct --model_variant taxei --output eval_results/llama31_taxei_s0_eval.json --seed 42 --num_episodes 47\"",
330	    "server": "autodl-5090",
331	    "gpu": [
332	      "cuda:0"
333	    ],
334	    "pid": "278309",
335	    "log_path": "/root/autodl-tmp/tax_error_inject_agent/eval_results/llama31_taxei_s0_eval.json",
336	    "submitted_at": "2026-05-16T12:52:40.445Z",
337	    "submitted_via": "submit_training_job",
338	    "backend": "tmux",
339	    "account": "root",
340	    "parent": "llama31-taxei-s0",
341	    "checkpoint_source": "output/llama31-taxei-s0/v1-20260516-181826/checkpoint-3387",
342	    "eval_data": "injected_eval_47ep",
343	    "model_name": "Meta-Llama-3.1-8B-Instruct + taxei-s0 LoRA",
344	    "seed": 42,
345	    "data_path": "eval/injected_eval.py (built-in ALFWorld tasks)",
346	    "data_count": 47,
347	    "checkpoint_path": "/root/autodl-tmp/tax_error_inject_agent/output/llama31-taxei-s0/v1-20260516-181826/checkpoint-3387",
348	    "wall_clock_seconds": 4327.0,
349	    "gpu_hours": 1.2
350	  },
351	  "hypothesis": "Cross-model: LLaMA TaxEI s0 injected eval — does taxonomy injection help on LLaMA seed 0?",
352	  "conclusion": "success",
353	  "metrics": {
354	    "recovery_rate": 0.745,
355	    "success_rate": 0.745,
356	    "total_episodes": 47
357	  },
358	  "completed_at": "2026-05-16T14:04:47.458Z"
359	}
360	
361	--------------------------------------------------------------------------------
362	ID: llama31-taxei-s42
363	--------------------------------------------------------------------------------
364	{
365	  "status": "DONE",
366	  "retry_count": 0,
367	  "created_at": "2026-05-16T06:22:49.346Z",
368	  "updated_at": "2026-05-16T08:46:25.092Z",
369	  "spec": {
370	    "data_path": "/root/autodl-tmp/tax_error_inject_agent/data/mini_pipeline_v4/sft_taxei_v4.jsonl",
371	    "data_count": 9029,
372	    "model_name": "Meta-Llama-3.1-8B-Instruct",
373	    "seed": 42,
374	    "hypothesis": "Cross-model generalizability: LLaMA-3.1-8B TaxEI condition to verify Qwen3-8B findings transfer",
375	    "command": "swift sft --model /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct --dataset sft_taxei_v4.jsonl --lora_rank 16 --num_train_epochs 3 --bs 4 --ga 2 --lr 1e-4 --max_length 4096 --seed 42",
376	    "server": "autodl-5090",
377	    "gpu": "cuda:1",
378	    "checkpoint_path": "/root/autodl-tmp/tax_error_inject_agent/output/llama31-taxei-s42/v0-20260516-142258/checkpoint-3387",
379	    "log_path": "/root/autodl-tmp/tax_error_inject_agent/output/llama31-taxei-s42/v0-20260516-142258/logging.jsonl"
380	  },
381	  "reproduce": {
382	    "finished_at": "2026-05-16T08:36:00.235Z"
383	  },
384	  "extra": {
385	    "hook_events": [
386	      {
387	        "event": "on_complete",
388	        "action": "agent",
389	        "ts": "2026-05-16T08:36:05.288585+00:00"
390	      }
391	    ]
392	  },
393	  "metrics": {
394	    "train_loss": 0.3366,
395	    "token_acc": 0.9357,
396	    "train_steps": 3387,
397	    "train_duration_s": 7782
398	  },
399	  "conclusion": "success",
400	  "completed_at": "2026-05-16T08:39:34.756Z",
401	  "checkpoint_path": "/root/autodl-tmp/tax_error_inject_agent/output/llama31-taxei-s42/v0-20260516-142258/checkpoint-3387"
402	}
403	
404	--------------------------------------------------------------------------------
405	ID: llama31-taxei-s42-eval
406	--------------------------------------------------------------------------------
407	{
408	  "status": "DONE",
409	  "retry_count": 0,
410	  "created_at": "2026-05-16T09:14:40.025Z",
411	  "updated_at": "2026-05-16T09:15:26.908Z",
412	  "spec": {
413	    "hypothesis": "Cross-model: LLaMA TaxEI s42 eval — does taxonomy-guided injection help on LLaMA?",
414	    "model_name": "Meta-Llama-3.1-8B-Instruct + TaxEI LoRA",
415	    "seed": 42,
416	    "checkpoint_source": "/root/autodl-tmp/tax_error_inject_agent/output/llama31-taxei-s42/v0-20260516-142258/checkpoint-3387",
417	    "eval_data": "ALFWorld 47 injected tasks",
418	    "data_path": "eval/injected_eval.py (47 ALFWorld tasks)",
419	    "data_count": 47,
420	    "command": "CUDA_VISIBLE_DEVICES=1 python3 eval/injected_eval.py --model_path output/llama31-taxei-s42/v0-20260516-142258/checkpoint-3387 --base_model /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct --model_variant taxei --output_file eval_results/llama31_taxei_s42.json",
421	    "server": "autodl-5090"
422	  },
423	  "metrics": {
424	    "recovery_rate": 0.745,
425	    "recovery_count": "35/47",
426	    "detection_rate": 0.298,
427	    "C1_context_truncation": 0.833,
428	    "C4_observation_masking": 0.727,
429	    "P1_step_order_swap": 0.583,
430	    "P2_sub_goal_deletion": 0.833,
431	    "C1_detection": 0.167,
432	    "C4_detection": 0.364,
433	    "P1_detection": 0.25,
434	    "P2_detection": 0.417
435	  },
436	  "conclusion": "success",
437	  "checkpoint_path": "/root/autodl-tmp/tax_error_inject_agent/output/llama31-taxei-s42/v0-20260516-142258/checkpoint-3387",
438	  "log_path": "/root/autodl-tmp/tax_error_inject_agent/eval_results/llama31_taxei_s42.json",
439	  "completed_at": "2026-05-16T09:15:26.908Z"
440	}
441	
442	--------------------------------------------------------------------------------
443	ID: llama31-vanilla-s0
444	--------------------------------------------------------------------------------
445	{
446	  "status": "DONE",
447	  "retry_count": 0,
448	  "created_at": "2026-05-16T09:15:55.388Z",
449	  "updated_at": "2026-05-16T10:29:59.217Z",
450	  "spec": {
451	    "command": "swift sft --model Meta-Llama-3.1-8B-Instruct --dataset sft_vanilla_v4.jsonl",
452	    "server": "autodl-5090",
453	    "gpu": [
454	      "cuda:0"
455	    ],
456	    "pid": "257144",
457	    "log_path": "~/runs/tax_error_inject_agent/llama31-vanilla-s0.log",
458	    "submitted_at": "2026-05-16T09:15:54.991Z",
459	    "submitted_via": "submit_training_job",
460	    "backend": "tmux",
461	    "account": "root",
462	    "data_count": 4358,
463	    "data_path": "data/mini_pipeline_v4/sft_vanilla_v4.jsonl",
464	    "model_name": "Meta-Llama-3.1-8B-Instruct",
465	    "seed": 0,
466	    "wall_clock_seconds": 4158.6,
467	    "gpu_hours": 1.16,
468	    "checkpoint_path": "/root/autodl-tmp/tax_error_inject_agent/output/llama31-vanilla-s0/v0-20260516-171603/checkpoint-1635"
469	  },
470	  "reproduce": {
471	    "finished_at": "2026-05-16T10:26:48.334Z"
472	  },
473	  "extra": {
474	    "hook_events": [
475	      {
476	        "event": "on_complete",
477	        "action": "agent",
478	        "ts": "2026-05-16T10:26:50.786934+00:00"
479	      }
480	    ]
481	  },
482	  "checkpoint_path": "/root/autodl-tmp/tax_error_inject_agent/output/llama31-vanilla-s0/v0-20260516-171603/checkpoint-1635",
483	  "log_path": "/root/runs/tax_error_inject_agent/llama31-vanilla-s0.log",
484	  "conclusion": "success",
485	  "completed_at": "2026-05-16T10:29:44.360Z",
486	  "metrics": {
487	    "final_train_loss": 0.398,
488	    "epoch1_loss": 0.481,
489	    "epoch2_loss": 0.362,
490	    "epoch3_loss": 0.273,
491	    "final_token_acc": 0.909,
492	    "train_runtime_sec": 4158.6
493	  }
494	}
495	
496	--------------------------------------------------------------------------------
497	ID: llama31-vanilla-s0-clean
498	--------------------------------------------------------------------------------
499	{
500	  "status": "DONE",
501	  "retry_count": 0,
502	  "created_at": "2026-05-16T12:14:53.046Z",
503	  "updated_at": "2026-05-16T12:35:41.228Z",
504	  "spec": {
505	    "command": "CUDA_VISIBLE_DEVICES=0 python3 eval/recovery.py --model_path output/llama31-vanilla-s0/v0-20260516-171603/checkpoint-1635 --base_model /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct --num_episodes 47 --task_list eval/eval_tasks_47.json --output eval_results/llama31_vanilla_s0_clean.json",
506	    "server": "autodl-5090",
507	    "data_path": "eval/eval_tasks_47.json",
508	    "data_count": 47,
509	    "model_name": "Meta-Llama-3.1-8B-Instruct + llama31-vanilla-s0 LoRA",
510	    "seed": 0,
511	    "checkpoint_source": "output/llama31-vanilla-s0/v0-20260516-171603/checkpoint-1635",
512	    "eval_data": "ALFWorld clean eval 47 tasks",
513	    "hypothesis": "LLaMA Vanilla s0 clean eval - baseline success rate without injection"
514	  },
515	  "conclusion": "success",
516	  "metrics": {
517	    "success_rate": 0.723,
518	    "eval_type": "clean",
519	    "eval_script": "eval/recovery.py",
520	    "total_episodes": 47,
521	    "output_file": "eval_results/llama31_vanilla_s0_clean.json"
522	  },
523	  "checkpoint_path": "/root/autodl-tmp/tax_error_inject_agent/output/llama31-vanilla-s0/v0-20260516-171603/checkpoint-1635",
524	  "log_path": "eval_results/llama31_vanilla_s0_clean.json",
525	  "completed_at": "2026-05-16T12:35:41.228Z"
526	}
527	
528	--------------------------------------------------------------------------------
529	ID: llama31-vanilla-s0-eval
530	--------------------------------------------------------------------------------
531	{
532	  "status": "DONE",
533	  "retry_count": 0,
534	  "created_at": "2026-05-16T10:39:37.086Z",
535	  "updated_at": "2026-05-16T11:21:29.608Z",
536	  "hypothesis": "LLaMA-3.1-8B Vanilla s0 injected eval - cross-model validation seed 0",
537	  "spec": {
538	    "command": "CUDA_VISIBLE_DEVICES=3 python3 eval/injected_eval.py --model_path output/llama31-vanilla-s0/v0-20260516-171603/checkpoint-1635 --base_model /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct --model_variant vanilla --seed 0 --num_episodes 47 --output eval_results/llama31_vanilla_s0_injected.json",
539	    "server": "autodl-5090",
540	    "data_path": "eval/injected_eval.py",
541	    "data_count": 47,
542	    "model_name": "Meta-Llama-3.1-8B-Instruct + llama31-vanilla-s0 LoRA",
543	    "seed": 0,
544	    "checkpoint_source": "output/llama31-vanilla-s0/v0-20260516-171603/checkpoint-1635",
545	    "eval_data": "ALFWorld injected eval 47 tasks"
546	  },
547	  "reproduce": {
548	    "finished_at": "2026-05-16T11:05:01.407Z"
549	  },
550	  "failure_reason": "process dead 5× with no sentinel/W&B — auto-resolved as failed",
551	  "conclusion": "success",
552	  "completed_at": "2026-05-16T11:05:03.246Z",
553	  "extra": {
554	    "hook_events": [
555	      {
556	        "event": "on_failed",
557	        "action": "agent",
558	        "ts": "2026-05-16T11:05:05.820946+00:00"
559	      }
560	    ]
561	  },
562	  "metrics": {
563	    "recovery_rate": 0.745,
564	    "recovery_count": "35/47",
565	    "detection_rate": 0.277,
566	    "eval_type": "injected",
567	    "eval_script": "injected_eval.py",
568	    "output_file": "eval_results/llama31_vanilla_s0_injected.json",
569	    "C1_context_truncation": {
570	      "recovery": 0.667,
571	      "detection": 0.167
572	    },
573	    "C4_observation_masking": {
574	      "recovery": 0.727,
575	      "detection": 0.364
576	    },
577	    "P1_step_order_swap": {
578	      "recovery": 0.917,
579	      "detection": 0.333
580	    },
581	    "P2_sub_goal_deletion": {
582	      "recovery": 0.667,
583	      "detection": 0.25
584	    }
585	  }
586	}
587	
588	--------------------------------------------------------------------------------
589	ID: llama31-vanilla-s123
590	--------------------------------------------------------------------------------
591	{
592	  "status": "DONE",
593	  "retry_count": 0,
594	  "created_at": "2026-05-16T12:52:22.460Z",
595	  "updated_at": "2026-05-16T14:26:04.356Z",
596	  "spec": {
597	    "command": "swift sft --model /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct --dataset data/mini_pipeline_v4/sft_vanilla_v4.jsonl --output_dir output/llama31-vanilla-s123 --lora_rank 16 --num_train_epochs 3 --per_device_train_batch_size 4 --gradient_accumulation_steps 2 --learning_rate 1e-4 --max_length 4096 --seed 123 --data_seed 123 --logging_steps 10 --gradient_checkpointing true --bf16 true --save_strategy epoch",
598	    "server": "autodl-5090",
599	    "gpu": [
600	      "cuda:1"
601	    ],
602	    "pid": "277341",
603	    "log_path": "~/runs/tax_error_inject_agent/llama31-vanilla-s123.log",
604	    "submitted_at": "2026-05-16T12:52:22.085Z",
605	    "submitted_via": "submit_training_job",
606	    "backend": "tmux",
607	    "account": "root",
608	    "data_path": "data/mini_pipeline_v4/sft_vanilla_v4.jsonl",
609	    "data_count": 4358,
610	    "model_name": "Meta-Llama-3.1-8B-Instruct",
611	    "seed": 123,
612	    "wall_clock_seconds": 4992.9,
613	    "gpu_hours": 1.39
614	  },
615	  "hypothesis": "Cross-model: LLaMA Vanilla s123 - 3rd seed for 3-seed cross-model validation",
616	  "checkpoint_path": "output/llama31-vanilla-s123/v0-20260516-205231/checkpoint-1635",
617	  "conclusion": "success",
618	  "completed_at": "2026-05-16T14:15:35.008Z",
619	  "metrics": {
620	    "train_loss": 0.4,
621	    "final_loss": 0.254,
622	    "token_acc": 0.894,
623	    "steps": 1635,
624	    "epochs": 3,
625	    "runtime_seconds": 4234,
626	    "memory_gib": 29.85
627	  }
628	}
629	
630	--------------------------------------------------------------------------------
631	ID: llama31-vanilla-s123-clean
632	--------------------------------------------------------------------------------
633	{
634	  "status": "DONE",
635	  "retry_count": 0,
636	  "created_at": "2026-05-16T14:36:07.599Z",
637	  "updated_at": "2026-05-16T14:36:39.967Z",
638	  "conclusion": "success",
639	  "spec": {
640	    "command": "python eval/recovery.py --model_path output/llama31-vanilla-s123/v0-20260516-205231/checkpoint-1635 --base_model /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct/ --task_list eval/eval_tasks_47.json --num_episodes 47 --output eval_results/llama31_vanilla_s123_clean.json --no_inject --seed 123 --device cuda:0",
641	    "server": "autodl-5090",
642	    "data_path": "eval/eval_tasks_47.json",
643	    "data_count": 47,
644	    "model_name": "llama31-vanilla-s123",
645	    "seed": 123,
646	    "checkpoint_source": "output/llama31-vanilla-s123/v0-20260516-205231/checkpoint-1635",
647	    "eval_data": "valid_unseen",
648	    "checkpoint_path": "output/llama31-vanilla-s123/v0-20260516-205231/checkpoint-1635",
649	    "log_path": "eval_results/llama31_vanilla_s123_clean.log",
650	    "parent": "llama31-vanilla-s123"
651	  },
652	  "completed_at": "2026-05-16T14:36:32.828Z",
653	  "metrics": {
654	    "success_rate": 0.723,
655	    "total_episodes": 47,
656	    "eval_type": "clean",
657	    "eval_script": "eval/recovery.py",
658	    "output_file": "eval_results/llama31_vanilla_s123_clean.json",
659	    "by_task_type": {
660	      "look_at_obj_in_light": 0.833,
661	      "pick_and_place_simple": 0.625,
662	      "pick_clean_then_place_in_recep": 0.545,
663	      "pick_cool_then_place_in_recep": 0.571,
664	      "pick_heat_then_place_in_recep": 1,
665	      "pick_two_obj_and_place": 0.857
666	    }
667	  }
668	}
669	
670	--------------------------------------------------------------------------------
671	ID: llama31-vanilla-s42
672	--------------------------------------------------------------------------------
673	{
674	  "status": "DONE",
675	  "retry_count": 0,
676	  "created_at": "2026-05-16T06:32:19.082Z",
677	  "updated_at": "2026-05-16T07:48:06.140Z",
678	  "spec": {
679	    "command": "swift sft --model Meta-Llama-3.1-8B-Instruct --dataset sft_vanilla_v4.jsonl --lora_rank 16 --epochs 3 --bs 4 --ga 2 --lr 1e-4 --max_length 4096 --seed 42",
680	    "server": "autodl-5090",
681	    "gpu": "cuda:0",
682	    "pid": "244644",
683	    "log_path": "~/runs/tax_error_inject_agent/llama31-vanilla-s42.log",
684	    "submitted_at": "2026-05-16T06:32:18.732Z",
685	    "submitted_via": "submit_training_job",
686	    "backend": "tmux",
687	    "account": "root",
688	    "data_path": "/root/autodl-tmp/tax_error_inject_agent/data/mini_pipeline_v4/sft_vanilla_v4.jsonl",
689	    "data_count": 9029,
690	    "model_name": "Meta-Llama-3.1-8B-Instruct",
691	    "seed": 42,
692	    "hypothesis": "Cross-model generalizability: LLaMA-3.1-8B Vanilla baseline",
693	    "wall_clock_seconds": 4547.4,
694	    "gpu_hours": 1.26
695	  },
696	  "reproduce": {
697	    "finished_at": "2026-05-16T07:44:55.468Z"
698	  },
699	  "extra": {
700	    "hook_events": [
701	      {
702	        "event": "on_complete",
703	        "action": "agent",
704	        "ts": "2026-05-16T07:44:59.077032+00:00"
705	      }
706	    ]
707	  },
708	  "checkpoint_path": "/root/autodl-tmp/tax_error_inject_agent/output/llama31-vanilla-s42/v0-20260516-143227/checkpoint-1635",
709	  "metrics": {
710	    "train_loss": 0.40025,
711	    "token_acc": 0.9067,
712	    "train_steps": 1635,
713	    "train_duration_s": 4157
714	  },
715	  "conclusion": "success",
716	  "log_path": "~/runs/tax_error_inject_agent/llama31-vanilla-s42.log",
717	  "completed_at": "2026-05-16T07:48:06.140Z"
718	}
719	
720	--------------------------------------------------------------------------------
721	ID: llama31-vanilla-s42-clean
722	--------------------------------------------------------------------------------
723	{
724	  "status": "DONE",
725	  "retry_count": 0,
726	  "created_at": "2026-05-16T12:14:50.470Z",
727	  "updated_at": "2026-05-16T12:35:18.899Z",
728	  "spec": {
729	    "command": "CUDA_VISIBLE_DEVICES=0 python3 eval/recovery.py --model_path output/llama31-vanilla-s42/v0-20260516-143227/checkpoint-1635 --base_model /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct --num_episodes 47 --task_list eval/eval_tasks_47.json --output eval_results/llama31_vanilla_s42_clean.json",
730	    "server": "autodl-5090",
731	    "data_path": "eval/eval_tasks_47.json",
732	    "data_count": 47,
733	    "model_name": "Meta-Llama-3.1-8B-Instruct + llama31-vanilla-s42 LoRA",
734	    "seed": 42,
735	    "checkpoint_source": "output/llama31-vanilla-s42/v0-20260516-143227/checkpoint-1635",
736	    "eval_data": "ALFWorld clean eval 47 tasks",
737	    "hypothesis": "LLaMA Vanilla s42 clean eval - baseline success rate without injection"
738	  },
739	  "conclusion": "success",
740	  "metrics": {
741	    "success_rate": 0.723,
742	    "eval_type": "clean",
743	    "eval_script": "eval/recovery.py",
744	    "total_episodes": 47,
745	    "output_file": "eval_results/llama31_vanilla_s42_clean.json"
746	  },
747	  "checkpoint_path": "/root/autodl-tmp/tax_error_inject_agent/output/llama31-vanilla-s42/v0-20260516-143227/checkpoint-1635",
748	  "log_path": "eval_results/llama31_vanilla_s42_clean.json",
749	  "completed_at": "2026-05-16T12:35:18.899Z"
750	}
751	
752	--------------------------------------------------------------------------------
753	ID: llama31-vanilla-s42-eval
754	--------------------------------------------------------------------------------
755	{
756	  "status": "DONE",
757	  "retry_count": 0,
758	  "created_at": "2026-05-16T08:07:12.328Z",
759	  "updated_at": "2026-05-16T08:36:24.810Z",
760	  "spec": {
761	    "hypothesis": "LLaMA-3.1-8B Vanilla s42 injected eval - cross-model baseline",
762	    "model_name": "LLaMA-3.1-8B-Instruct + Vanilla LoRA",
763	    "seed": 42,
764	    "checkpoint_source": "/root/autodl-tmp/tax_error_inject_agent/output/llama31-vanilla-s42/v0-20260516-143227/checkpoint-1635",
765	    "eval_data": "ALFWorld 47 injected tasks"
766	  },
767	  "metrics": {
768	    "recovery_rate": 0.745,
769	    "recovery_count": "35/47",
770	    "detection_rate": 0.213,
771	    "C1_context_truncation": 0.75,
772	    "C4_observation_masking": 0.727,
773	    "P1_step_order_swap": 0.75,
774	    "P2_sub_goal_deletion": 0.75
775	  },
776	  "conclusion": "success",
777	  "checkpoint_path": "/root/autodl-tmp/tax_error_inject_agent/output/llama31-vanilla-s42/v0-20260516-143227/checkpoint-1635",
778	  "log_path": "~/runs/tax_error_inject_agent/llama31-vanilla-s42-eval.log",
779	  "completed_at": "2026-05-16T08:36:24.810Z"
780	}
781	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01BbmLXayvRWQ5YLrpnBLT8u",
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55",
  "uuid": "95d3f140-15d7-47df-88e5-296f2a73f137"
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
  "task_id": "a1b20f795e02ae461",
  "tool_use_id": "toolu_01BbmLXayvRWQ5YLrpnBLT8u",
  "description": "Running cd /home/ubuntu/.claude-account-3/projects/-home-…",
  "usage": {
    "total_tokens": 35535,
    "tool_uses": 8,
    "duration_ms": 60251
  },
  "last_tool_name": "Bash",
  "uuid": "95565a2d-a2c8-4c08-82ed-e24c65cfeb4d",
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55"
}
```

---

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — Bash · `toolu_01FoGcRE9cck1gpSvjGxAKhL`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/ae491a69-2268-4f52-bbd5-112d75ec9c55/tool-results && python3 -c \"\nimport json\n\nwith open('mcp-agent-ml-research-read_registry-1778943212143.txt', 'r') as f:\n    raw = json.load(f)\n\ndata = json.loads(raw['result'])\nexperiments = data['data']['experiments']\n\n# Find experiments that reference Qwen in their model_name or spec and have eval metrics\nqwen_with_eval = {}\nfor k, v in experiments.items():\n    if not isinstance(v, dict):\n        continue\n    # Check if Qwen is in model_name\n    model_name = ''\n    if isinstance(v.get('spec'), dict):\n        model_name = v['spec'].get('model_name', '')\n    \n    has_qwen = 'qwen' in model_name.lower() or 'Qwen' in model_name\n    \n    # Check if it has meaningful eval metrics (recovery_rate or success_rate in metrics)\n    metrics = v.get('metrics', {})\n    has_eval = False\n    if isinstance(metrics, dict):\n        has_eval = 'recovery_rate' in metrics or 'success_rate' in metrics\n    \n    if has_qwen and has_eval:\n        qwen_with_eval[k] = v\n\nprint(f'Found {len(qwen_with_eval)} Qwen experiments with eval metrics:')\nfor k in sorted(qwen_with_eval.keys()):\n    print(f'  - {k}')\nprint()\nprint('='*80)\nprint('QWEN EXPERIMENTS WITH EVAL METRICS - FULL DETAILS')\nprint('='*80)\nfor k in sorted(qwen_with_eval.keys()):\n    exp = qwen_with_eval[k]\n    print()\n    print('-'*80)\n    print(f'ID: {k}')\n    print('-'*80)\n    print(json.dumps(exp, indent=2, ensure_ascii=False))\n\" 2>&1",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01BbmLXayvRWQ5YLrpnBLT8u",
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55",
  "uuid": "7551169a-78d9-4613-9924-1ea53b3dfb38",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bd1UAFKALV9dtAAf4jiVbV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13781,
      "cache_read_input_tokens": 21406,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13781,
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

_source line 38 · 2026-05-16T14:54:41.206Z_

<details><summary>↩ Tool result · `toolu_01FoGcRE9cck1gpSvjGxAKhL`</summary>

```text
&lt;persisted-output>
Output too large (55.7KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/ae491a69-2268-4f52-bbd5-112d75ec9c55/tool-results/bt0rx9074.txt

Preview (first 2KB):
Found 30 Qwen experiments with eval metrics:
  - eval-rp-s0
  - eval-rp-s1
  - eval-rp-s123
  - eval-rp-s42
  - eval-rp-s7
  - recovery-random-s1
  - recovery-random-s7
  - recovery-taxei-s1
  - recovery-taxei-s7
  - recovery-vanilla-s1
  - recovery-vanilla-s7
  - v4-random-fixed-inject10-s0-eval-r3
  - v4-random-fixed-inject10-s1-eval
  - v4-random-fixed-inject10-s123-eval
  - v4-random-fixed-inject10-s7-eval
  - v4-random-fixed-inject50-s1-eval
  - v4-random-fixed-inject50-s7-eval
  - v4-random-recovery-eval
  - v4-random-recovery-eval-s0
  - v4-random-recovery-eval-s123
  - v4-random-seed7-eval
  - v4-taxei-fixed-inject10-s1-eval-r2
  - v4-taxei-fixed-inject10-s123-eval-r3
  - v4-taxei-fixed-inject10-s7-eval
  - v4-taxei-fixed-inject50-s1-eval
  - v4-taxei-fixed-inject50-s7-eval
  - v4-taxei-recovery-eval
  - v4-taxei-recovery-eval-r2
  - v4-taxei-seed7-eval
  - v4-vanilla-recovery-eval

================================================================================
QWEN EXPERIMENTS WITH EVAL METRICS - FULL DETAILS
================================================================================

--------------------------------------------------------------------------------
ID: eval-rp-s0
--------------------------------------------------------------------------------
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-16T06:27:52.208Z",
  "updated_at": "2026-05-16T06:30:58.894Z",
  "failure_reason": "",
  "conclusion": "success",
  "reproduce": {
    "finished_at": "2026-05-16T06:27:54.715Z"
  },
  "extra": {
    "hook_events": [
      {
        "event": "on_failed",
        "action": "agent",
        "ts": "2026-05-16T06:28:01.102430+00:00"
      }
    ]
  },
  "metrics": {
    "recovery_rate": 0.468,
    "detection_rate": 0,
    "episodes": 47,
    "recovered": 22
  },
  "spec": {
    "command": "python eval_recovery.py --seed 0",
    "server": "autodl-5090",
    "data_path": "/root/autodl-tmp/tax_error_inject_agent/data/recovery_paired/",
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01BbmLXayvRWQ5YLrpnBLT8u",
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55",
  "uuid": "b04dba45-3de2-4afc-8bc6-48d7de295a60"
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
  "task_id": "a1b20f795e02ae461",
  "tool_use_id": "toolu_01BbmLXayvRWQ5YLrpnBLT8u",
  "description": "Reading ~/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/ae491a69-2268-4f52-bbd5-112d75ec9c55/tool-results/bt0rx9074.txt",
  "usage": {
    "total_tokens": 37247,
    "tool_uses": 9,
    "duration_ms": 63983
  },
  "last_tool_name": "Read",
  "uuid": "f46dbf6f-09eb-4343-bcc7-6f96721b84d9",
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55"
}
```

---

### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Read · `toolu_01VZzSW8CBSVMTXTuRCPQ5BA`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/ae491a69-2268-4f52-bbd5-112d75ec9c55/tool-results/bt0rx9074.txt",
  "offset": 0,
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01BbmLXayvRWQ5YLrpnBLT8u",
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55",
  "uuid": "51ff498c-1749-4843-8595-1d1dca81424b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014HWoNr8WubZvzDDbAzrCjv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1650,
      "cache_read_input_tokens": 35187,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1650,
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

_source line 41 · 2026-05-16T14:54:44.654Z_

<details><summary>↩ Tool result · `toolu_01VZzSW8CBSVMTXTuRCPQ5BA`</summary>

```text
0	Found 30 Qwen experiments with eval metrics:
1	  - eval-rp-s0
2	  - eval-rp-s1
3	  - eval-rp-s123
4	  - eval-rp-s42
5	  - eval-rp-s7
6	  - recovery-random-s1
7	  - recovery-random-s7
8	  - recovery-taxei-s1
9	  - recovery-taxei-s7
10	  - recovery-vanilla-s1
11	  - recovery-vanilla-s7
12	  - v4-random-fixed-inject10-s0-eval-r3
13	  - v4-random-fixed-inject10-s1-eval
14	  - v4-random-fixed-inject10-s123-eval
15	  - v4-random-fixed-inject10-s7-eval
16	  - v4-random-fixed-inject50-s1-eval
17	  - v4-random-fixed-inject50-s7-eval
18	  - v4-random-recovery-eval
19	  - v4-random-recovery-eval-s0
20	  - v4-random-recovery-eval-s123
21	  - v4-random-seed7-eval
22	  - v4-taxei-fixed-inject10-s1-eval-r2
23	  - v4-taxei-fixed-inject10-s123-eval-r3
24	  - v4-taxei-fixed-inject10-s7-eval
25	  - v4-taxei-fixed-inject50-s1-eval
26	  - v4-taxei-fixed-inject50-s7-eval
27	  - v4-taxei-recovery-eval
28	  - v4-taxei-recovery-eval-r2
29	  - v4-taxei-seed7-eval
30	  - v4-vanilla-recovery-eval
31	
32	================================================================================
33	QWEN EXPERIMENTS WITH EVAL METRICS - FULL DETAILS
34	================================================================================
35	
36	--------------------------------------------------------------------------------
37	ID: eval-rp-s0
38	--------------------------------------------------------------------------------
39	{
40	  "status": "DONE",
41	  "retry_count": 0,
42	  "created_at": "2026-05-16T06:27:52.208Z",
43	  "updated_at": "2026-05-16T06:30:58.894Z",
44	  "failure_reason": "",
45	  "conclusion": "success",
46	  "reproduce": {
47	    "finished_at": "2026-05-16T06:27:54.715Z"
48	  },
49	  "extra": {
50	    "hook_events": [
51	      {
52	        "event": "on_failed",
53	        "action": "agent",
54	        "ts": "2026-05-16T06:28:01.102430+00:00"
55	      }
56	    ]
57	  },
58	  "metrics": {
59	    "recovery_rate": 0.468,
60	    "detection_rate": 0,
61	    "episodes": 47,
62	    "recovered": 22
63	  },
64	  "spec": {
65	    "command": "python eval_recovery.py --seed 0",
66	    "server": "autodl-5090",
67	    "data_path": "/root/autodl-tmp/tax_error_inject_agent/data/recovery_paired/",
68	    "data_count": 47,
69	    "model_name": "Qwen3-8B (TaxEI-RP s0)",
70	    "seed": 0,
71	    "checkpoint_source": "v4-taxei-rp-s0",
72	    "eval_data": "47 ALFWorld clean tasks with error injection"
73	  },
74	  "log_path": "/tmp/eval_rp_s0.log",
75	  "checkpoint_path": "/root/autodl-tmp/tax_error_inject_agent/eval_outputs/v4_taxei_rp_s0_injected.json",
76	  "completed_at": "2026-05-16T06:30:47.736Z"
77	}
78	
79	--------------------------------------------------------------------------------
80	ID: eval-rp-s1
81	--------------------------------------------------------------------------------
82	{
83	  "status": "DONE",
84	  "retry_count": 0,
85	  "created_at": "2026-05-16T06:27:34.660Z",
86	  "updated_at": "2026-05-16T06:30:59.753Z",
87	  "failure_reason": "",
88	  "conclusion": "success",
89	  "extra": {
90	    "hook_events": [
91	      {
92	        "event": "on_failed",
93	        "action": "agent",
94	        "ts": "2026-05-16T06:27:37.861045+00:00"
95	      }
96	    ]
97	  },
98	  "metrics": {
99	    "recovery_rate": 0.489,
100	    "detection_rate": 0,
101	    "episodes": 47,
102	    "recovered": 23
103	  },
104	  "spec": {
105	    "command": "python eval_recovery.py --seed 1",
106	    "server": "autodl-5090",
107	    "data_path": "/root/autodl-tmp/tax_error_inject_agent/data/recovery_paired/",
108	    "data_count": 47,
109	    "model_name": "Qwen3-8B (TaxEI-RP s1)",
110	    "seed": 1,
111	    "checkpoint_source": "v4-taxei-rp-s1",
112	    "eval_data": "47 ALFWorld clean tasks with error injection"
113	  },
114	  "log_path": "/tmp/eval_rp_s1.log",
115	  "checkpoint_path": "/root/autodl-tmp/tax_error_inject_agent/eval_outputs/v4_taxei_rp_s1_injected.json",
116	  "completed_at": "2026-05-16T06:30:48.894Z"
117	}
118	
119	--------------------------------------------------------------------------------
120	ID: eval-rp-s123
121	--------------------------------------------------------------------------------
122	{
123	  "status": "DONE",
124	  "retry_count": 0,
125	  "created_at": "2026-05-16T06:27:26.558Z",
126	  "updated_at": "2026-05-16T06:30:58.290Z",
127	  "failure_reason": "",
128	  "conclusion": "success",
129	  "extra": {
130	    "hook_events": [
131	      {
132	        "event": "on_failed",
133	        "action": "agent",
134	        "ts": "2026-05-16T06:27:29.414786+00:00"
135	      }
136	    ]
137	  },
138	  "metrics": {
139	    "recovery_rate": 0.574,
140	    "detection_rate": 0,
141	    "episodes": 47,
142	    "recovered": 27
143	  },
144	  "spec": {
145	    "command": "python eval_recovery.py --seed 123",
146	    "server": "autodl-5090",
147	    "data_path": "/root/autodl-tmp/tax_error_inject_agent/data/recovery_paired/",
148	    "data_count": 47,
149	    "model_name": "Qwen3-8B (TaxEI-RP s123)",
150	    "seed": 123,
151	    "checkpoint_source": "v4-taxei-rp-s123",
152	    "eval_data": "47 ALFWorld clean tasks with error injection"
153	  },
154	  "log_path": "/tmp/eval_rp_s123.log",
155	  "checkpoint_path": "/root/autodl-tmp/tax_error_inject_agent/eval_outputs/v4_taxei_rp_s123_injected.json",
156	  "completed_at": "2026-05-16T06:30:46.571Z"
157	}
158	
159	--------------------------------------------------------------------------------
160	ID: eval-rp-s42
161	--------------------------------------------------------------------------------
162	{
163	  "status": "DONE",
164	  "retry_count": 0,
165	  "created_at": "2026-05-16T06:32:34.645Z",
166	  "updated_at": "2026-05-16T06:33:18.281Z",
167	  "spec": {
168	    "hypothesis": "TaxEI-RP recovery eval seed=42",
169	    "model_name": "Qwen3-8B + TaxEI-RP LoRA",
170	    "seed": 42,
171	    "command": "python eval/injected_eval.py --model_path v4-taxei-rp-s42 checkpoint --model_variant taxei --seed 42",
172	    "server": "autodl-5090",
173	    "data_path": "ALFWorld injected tasks",
174	    "data_count": 47,
175	    "gpu": "cuda:0"
176	  },
177	  "metrics": {
178	    "recovery_rate": 0.383,
179	    "recovery_count": "18/47",
180	    "C1_context_truncation": 0.5,
181	    "C4_observation_masking": 0.273,
182	    "P1_step_order_swap": 0.5,
183	    "P2_sub_goal_deletion": 0.25,
184	    "detection_rate": 0
185	  },
186	  "conclusion": "success",
187	  "checkpoint_path": "/root/autodl-tmp/tax_error_inject_agent/output/v4-taxei-rp-s42/v0-20260516-101703/checkpoint-5415",
188	  "log_path": "/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_taxei_rp_s42_injected.json",
189	  "completed_at": "2026-05-16T06:33:18.281Z"
190	}
191	
192	--------------------------------------------------------------------------------
193	ID: eval-rp-s7
194	--------------------------------------------------------------------------------
195	{
196	  "status": "DONE",
197	  "retry_count": 0,
198	  "created_at": "2026-05-16T10:25:59.082Z",
199	  "updated_at": "2026-05-16T10:26:30.070Z",
200	  "spec": {
201	    "hypothesis": "TaxEI-RP s7 eval - complete 5-seed recovery-paired injection assessment",
202	    "model_name": "Qwen3-8B + TaxEI-RP LoRA",
203	    "seed": 7,
204	    "checkpoint_source": "/root/autodl-tmp/tax_error_inject_agent/output/v4-taxei-rp-s7/v0-20260516-142303/checkpoint-5415",
205	    "eval_data": "ALFWorld 47 injected tasks",
206	    "data_path": "eval/injected_eval.py (47 ALFWorld tasks)",
207	    "data_count": 47,
208	    "command": "CUDA_VISIBLE_DEVICES=3 python3 eval/injected_eval.py --model_path output/v4-taxei-rp-s7/v0-20260516-142303/checkpoint-5415 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --model_variant taxei --output_file eval_results/v4_taxei_rp_recovery_eval_s7.json",
209	    "server": "autodl-5090"
210	  },
211	  "metrics": {
212	    "recovery_rate": 0.596,
213	    "recovery_count": "28/47",
214	    "detection_rate": 0
215	  },
216	  "conclusion": "success",
217	  "log_path": "/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_taxei_rp_recovery_eval_s7.json",
218	  "checkpoint_path": "/root/autodl-tmp/tax_error_inject_agent/output/v4-taxei-rp-s7/v0-20260516-142303/checkpoint-5415",
219	  "completed_at": "2026-05-16T10:26:30.070Z"
220	}
221	
222	--------------------------------------------------------------------------------
223	ID: recovery-random-s1
224	--------------------------------------------------------------------------------
225	{
226	  "status": "DONE",
227	  "retry_count": 0,
228	  "created_at": "2026-05-16T14:37:23.085Z",
229	  "updated_at": "2026-05-16T14:49:58.929Z",
230	  "spec": {
231	    "command": "CUDA_VISIBLE_DEVICES=1 python eval/injected_eval.py --model_path checkpoints/mini_random_sft_v4_seed1/v0-20260515-232340/checkpoint-3387 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --model_variant random --num_episodes 47 --output eval_results/v4_random_recovery_eval_s1.json --device cuda:0 --seed 42",
232	    "server": "autodl-5090",
233	    "data_path": "eval/alfworld_tasks",
234	    "data_count": 47,
235	    "model_name": "Qwen3-8B + mini_random_sft_v4_seed1",
236	    "seed": 1,
237	    "checkpoint_source": "checkpoints/mini_random_sft_v4_seed1/v0-20260515-232340/checkpoint-3387",
238	    "eval_data": "47 ALFWorld tasks with error injection",
239	    "parent": "mini_random_sft_v4_seed1",
240	    "checkpoint_path": "checkpoints/mini_random_sft_v4_seed1/v0-20260515-232340/checkpoint-3387",
241	    "log_path": "eval_results/v4_random_recovery_eval_s1.json"
242	  },
243	  "conclusion": "success",
244	  "completed_at": "2026-05-16T14:37:50.738Z",
245	  "metrics": {
246	    "recovery_rate": 0.511,
247	    "detection_rate": 0,
248	    "total_episodes": 47
249	  }
250	}
251	
252	--------------------------------------------------------------------------------
253	ID: recovery-random-s7
254	--------------------------------------------------------------------------------
255	{
256	  "status": "DONE",
257	  "retry_count": 0,
258	  "created_at": "2026-05-16T14:37:24.534Z",
259	  "updated_at": "2026-05-16T14:49:59.675Z",
260	  "spec": {
261	    "command": "CUDA_VISIBLE_DEVICES=1 python eval/injected_eval.py --model_path checkpoints/mini_random_sft_v4_seed7/v0-20260515-233427/checkpoint-3387 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --model_variant random --num_episodes 47 --output eval_results/v4_random_recovery_eval_s7.json --device cuda:0 --seed 42",
262	    "server": "autodl-5090",
263	    "data_path": "eval/alfworld_tasks",
264	    "data_count": 47,
265	    "model_name": "Qwen3-8B + mini_random_sft_v4_seed7",
266	    "seed": 7,
267	    "checkpoint_source": "checkpoints/mini_random_sft_v4_seed7/v0-20260515-233427/checkpoint-3387",
268	    "eval_data": "47 ALFWorld tasks with error injection",
269	    "parent": "mini_random_sft_v4_seed7",
270	    "checkpoint_path": "checkpoints/mini_random_sft_v4_seed7/v0-20260515-233427/checkpoint-3387",
271	    "log_path": "eval_results/v4_random_recovery_eval_s7.json"
272	  },
273	  "conclusion": "success",
274	  "completed_at": "2026-05-16T14:37:52.029Z",
275	  "metrics": {
276	    "recovery_rate": 0.532,
277	    "detection_rate": 0,
278	    "total_episodes": 47
279	  }
280	}
281	
282	--------------------------------------------------------------------------------
283	ID: recovery-taxei-s1
284	--------------------------------------------------------------------------------
285	{
286	  "status": "DONE",
287	  "retry_count": 0,
288	  "created_at": "2026-05-16T09:40:11.652Z",
289	  "updated_at": "2026-05-16T09:40:44.285Z",
290	  "spec": {
291	    "hypothesis": "Recovery eval TaxEI s1 - does TaxEI-trained model recover from injected errors?",
292	    "model_name": "Qwen3-8B + TaxEI LoRA",
293	    "seed": 1,
294	    "checkpoint_source": "/root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_taxei_sft_v4_seed1/v0-20260515-214035/checkpoint-3387",
295	    "eval_data": "ALFWorld 47 injected tasks",
296	    "data_path": "eval/injected_eval.py (47 ALFWorld tasks)",
297	    "data_count": 47,
298	    "command": "CUDA_VISIBLE_DEVICES=0 python3 eval/injected_eval.py --model_path checkpoints/mini_taxei_sft_v4_seed1/v0-20260515-214035/checkpoint-3387 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --model_variant taxei --output_file eval_results/v4_taxei_recovery_eval_s1.json",
299	    "server": "autodl-5090"
300	  },
301	  "metrics": {
302	    "recovery_rate": 0.617,
303	    "recovery_count": "29/47",
304	    "detection_rate": 0,
305	    "C1_context_truncation": 0.75,
306	    "C4_observation_masking": 0.636,
307	    "P1_step_order_swap": 0.583,
308	    "P2_sub_goal_deletion": 0.5
309	  },
310	  "conclusion": "success",
311	  "checkpoint_path": "/root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_taxei_sft_v4_seed1/v0-20260515-214035/checkpoint-3387",
312	  "log_path": "/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_taxei_recovery_eval_s1.json",
313	  "completed_at": "2026-05-16T09:40:44.285Z"
314	}
315	
316	--------------------------------------------------------------------------------
317	ID: recovery-taxei-s7
318	--------------------------------------------------------------------------------
319	{
320	  "status": "DONE",
321	  "retry_count": 0,
322	  "created_at": "2026-05-16T11:53:18.146Z",
323	  "updated_at": "2026-05-16T12:13:31.737Z",
324	  "spec": {
325	    "command": "CUDA_VISIBLE_DEVICES=3 python3 eval/injected_eval.py --model_path checkpoints/mini_taxei_sft_v4_seed7/.../checkpoint-3387 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --model_variant taxei --output_file eval_results/v4_taxei_recovery_eval_s7.json",
326	    "server": "autodl-5090",
327	    "data_path": "eval/injected_eval.py",
328	    "data_count": 47,
329	    "model_name": "Qwen3-8B + TaxEI s7 LoRA",
330	    "seed": 7,
331	    "checkpoint_source": "checkpoints/mini_taxei_sft_v4_seed7",
332	    "eval_data": "ALFWorld injected eval 47 tasks",
333	    "hypothesis": "Recovery eval TaxEI s7 - complete 5-seed recovery validation"
334	  },
335	  "conclusion": "success",
336	  "metrics": {
337	    "recovery_rate": 0.574,
338	    "detection_rate": 0,
339	    "total_episodes": 47
340	  },
341	  "checkpoint_path": "checkpoints/mini_taxei_sft_v4_seed7",
342	  "log_path": "eval_results/v4_taxei_recovery_eval_s7.json",
343	  "completed_at": "2026-05-16T12:13:31.737Z"
344	}
345	
346	--------------------------------------------------------------------------------
347	ID: recovery-vanilla-s1
348	--------------------------------------------------------------------------------
349	{
350	  "status": "DONE",
351	  "retry_count": 0,
352	  "created_at": "2026-05-16T08:26:23.215Z",
353	  "updated_at": "2026-05-16T08:49:34.621Z",
354	  "spec": {
355	    "hypothesis": "Recovery eval Vanilla s1 - confirm Recovery≈Resilience",
356	    "model_name": "Qwen3-8B + Vanilla LoRA",
357	    "seed": 1,
358	    "checkpoint_source": "/root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_vanilla_sft_v4_seed1/v0-20260515-214031/checkpoint-1635",
359	    "eval_data": "ALFWorld 47 injected tasks"
360	  },
361	  "reproduce": {
362	    "finished_at": "2026-05-16T08:32:46.932Z"
363	  },
364	  "failure_reason": "process dead 5× with no sentinel/W&B — auto-resolved as failed",
365	  "conclusion": "success",
366	  "completed_at": "2026-05-16T08:32:48.721Z",
367	  "extra": {
368	    "hook_events": [
369	      {
370	        "event": "on_failed",
371	        "action": "agent",
372	        "ts": "2026-05-16T08:32:54.320388+00:00"
373	      }
374	    ]
375	  },
376	  "metrics": {
377	    "recovery_rate": 0.66,
378	    "recovery_count": "31/47",
379	    "detection_rate": 0,
380	    "C1_context_truncation": 0.667,
381	    "C4_observation_masking": 0.545,
382	    "P1_step_order_swap": 0.667,
383	    "P2_sub_goal_deletion": 0.75
384	  }
385	}
386	
387	--------------------------------------------------------------------------------
388	ID: recovery-vanilla-s7
389	--------------------------------------------------------------------------------
390	{
391	  "status": "DONE",
392	  "retry_count": 0,
393	  "created_at": "2026-05-16T08:53:10.619Z",
394	  "updated_at": "2026-05-16T08:53:54.916Z",
395	  "spec": {
396	    "hypothesis": "Recovery eval Vanilla s7 - confirm Recovery≈Resilience",
397	    "model_name": "Qwen3-8B + Vanilla LoRA",
398	    "seed": 7,
399	    "checkpoint_source": "/root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_vanilla_sft_v4_seed7/v1-20260515-214032/checkpoint-1635",
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01BbmLXayvRWQ5YLrpnBLT8u",
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55",
  "uuid": "786d9377-1a55-4fdf-9cce-ec144f8b07c4"
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
  "task_id": "a1b20f795e02ae461",
  "tool_use_id": "toolu_01BbmLXayvRWQ5YLrpnBLT8u",
  "description": "Reading ~/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/ae491a69-2268-4f52-bbd5-112d75ec9c55/tool-results/bt0rx9074.txt",
  "usage": {
    "total_tokens": 43968,
    "tool_uses": 10,
    "duration_ms": 70928
  },
  "last_tool_name": "Read",
  "uuid": "3eadbfb2-a2ab-4e75-81ec-edaa03c8e1d3",
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55"
}
```

---

### Tool call

_source line 43_

<details open><summary>🔧 Tool call — Read · `toolu_01AM6Nbo95kfahLkSE3NaLJC`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/ae491a69-2268-4f52-bbd5-112d75ec9c55/tool-results/bt0rx9074.txt",
  "offset": 400,
  "limit": 600
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01BbmLXayvRWQ5YLrpnBLT8u",
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55",
  "uuid": "38a0187b-8d43-450c-9030-de7a3a75185c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SwkEgrjMsBPc3RN2KeZznz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6687,
      "cache_read_input_tokens": 36837,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6687,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 34,
      "service_tier": "standard",
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

_source line 44 · 2026-05-16T14:54:51.616Z_

<details><summary>↩ Tool result · `toolu_01AM6Nbo95kfahLkSE3NaLJC`</summary>

```text
400	    "checkpoint_source": "/root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_vanilla_sft_v4_seed7/v1-20260515-214032/checkpoint-1635",
401	    "eval_data": "ALFWorld 47 injected tasks",
402	    "data_path": "eval/injected_eval.py (47 ALFWorld tasks)",
403	    "data_count": 47,
404	    "command": "CUDA_VISIBLE_DEVICES=0 python3 eval/injected_eval.py --model_path checkpoints/mini_vanilla_sft_v4_seed7/v1-20260515-214032/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --model_variant vanilla --output_file eval_results/v4_vanilla_recovery_eval_s7.json",
405	    "server": "autodl-5090"
406	  },
407	  "conclusion": "success",
408	  "metrics": {
409	    "recovery_rate": 0.745,
410	    "recovery_count": "35/47",
411	    "detection_rate": 0,
412	    "C1_context_truncation": 0.75,
413	    "C4_observation_masking": 0.727,
414	    "P1_step_order_swap": 0.75,
415	    "P2_sub_goal_deletion": 0.75
416	  },
417	  "checkpoint_path": "/root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_vanilla_sft_v4_seed7/v1-20260515-214032/checkpoint-1635",
418	  "log_path": "/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_vanilla_recovery_eval_s7.json",
419	  "completed_at": "2026-05-16T08:53:54.916Z"
420	}
421	
422	--------------------------------------------------------------------------------
423	ID: v4-random-fixed-inject10-s0-eval-r3
424	--------------------------------------------------------------------------------
425	{
426	  "status": "DONE",
427	  "retry_count": 0,
428	  "created_at": "2026-05-15T20:40:07.402Z",
429	  "updated_at": "2026-05-15T20:52:32.204Z",
430	  "spec": {
431	    "command": "python3 eval/recovery.py --model_path checkpoints/v4_random_fixed_inject10_s0/v0-20260516-014835/checkpoint-1635 --num_episodes 47 --seed 42",
432	    "server": "autodl-5090",
433	    "gpu": [
434	      "cuda:3"
435	    ],
436	    "pid": "195118",
437	    "log_path": "~/runs/tax_error_inject_agent/v4-random-fixed-inject10-s0-eval-r3.log",
438	    "submitted_at": "2026-05-15T20:40:07.156Z",
439	    "submitted_via": "submit_training_job",
440	    "backend": "tmux",
441	    "account": "root",
442	    "parent": "v4-random-fixed-inject10-s0",
443	    "checkpoint_source": "v4-random-fixed-inject10-s0",
444	    "eval_data": "eval_tasks_47.json",
445	    "data_count": 47,
446	    "model_name": "Qwen3-8B + LoRA (random fixed inject10 s0)",
447	    "seed": 42,
448	    "data_path": "eval/eval_tasks_47.json",
449	    "wall_clock_seconds": 745.0,
450	    "gpu_hours": 0.21
451	  },
452	  "hypothesis": "v4 Random 10% seed=0 eval (r3, dedicated GPU) — 47 ALFWorld clean tasks.",
453	  "reproduce": {
454	    "finished_at": "2026-05-15T20:50:22.439Z"
455	  },
456	  "extra": {
457	    "hook_events": [
458	      {
459	        "event": "on_complete",
460	        "action": "agent",
461	        "ts": "2026-05-15T20:50:26.585713+00:00"
462	      }
463	    ]
464	  },
465	  "metrics": {
466	    "success_rate": 0.66,
467	    "successes": 31,
468	    "total": 47,
469	    "by_task_type": {
470	      "look_at_obj_in_light": {
471	        "success": 5,
472	        "total": 6,
473	        "rate": 0.833
474	      },
475	      "pick_and_place_simple": {
476	        "success": 4,
477	        "total": 8,
478	        "rate": 0.5
479	      },
480	      "pick_clean_then_place_in_recep": {
481	        "success": 7,
482	        "total": 11,
483	        "rate": 0.636
484	      },
485	      "pick_cool_then_place_in_recep": {
486	        "success": 4,
487	        "total": 7,
488	        "rate": 0.571
489	      },
490	      "pick_heat_then_place_in_recep": {
491	        "success": 7,
492	        "total": 8,
493	        "rate": 0.875
494	      },
495	      "pick_two_obj_and_place": {
496	        "success": 4,
497	        "total": 7,
498	        "rate": 0.571
499	      }
500	    }
501	  },
502	  "conclusion": "success",
503	  "checkpoint_path": "checkpoints/v4_random_fixed_inject10_s0/v0-20260516-014835/checkpoint-1635",
504	  "completed_at": "2026-05-15T20:52:32.204Z"
505	}
506	
507	--------------------------------------------------------------------------------
508	ID: v4-random-fixed-inject10-s1-eval
509	--------------------------------------------------------------------------------
510	{
511	  "status": "DONE",
512	  "retry_count": 0,
513	  "created_at": "2026-05-15T21:05:18.654Z",
514	  "updated_at": "2026-05-15T21:27:48.360Z",
515	  "spec": {
516	    "command": "python3 eval/recovery.py --model_path checkpoints/v4_random_fixed_inject10_s1/v1-20260516-040130/checkpoint-1635 --num_episodes 47 --seed 42",
517	    "server": "autodl-5090",
518	    "gpu": [
519	      "cuda:1"
520	    ],
521	    "pid": "198045",
522	    "log_path": "~/runs/tax_error_inject_agent/v4-random-fixed-inject10-s1-eval.log",
523	    "submitted_at": "2026-05-15T21:05:18.393Z",
524	    "submitted_via": "submit_training_job",
525	    "backend": "tmux",
526	    "account": "root",
527	    "data_path": "eval/eval_tasks_47.json",
528	    "data_count": 47,
529	    "model_name": "Qwen3-8B + LoRA (random fixed inject10 s1)",
530	    "seed": 42,
531	    "checkpoint_source": "v4-random-fixed-inject10-s1",
532	    "eval_data": "eval_tasks_47.json",
533	    "checkpoint_path": "checkpoints/v4_random_fixed_inject10_s1/v1-20260516-040130/checkpoint-1635",
534	    "wall_clock_seconds": 1350.0,
535	    "gpu_hours": 0.37
536	  },
537	  "hypothesis": "v4 Random 10% seed=1 eval — 47 ALFWorld clean tasks. Dose-response 5-seed expansion.",
538	  "reproduce": {
539	    "finished_at": "2026-05-15T21:25:33.786Z"
540	  },
541	  "extra": {
542	    "hook_events": [
543	      {
544	        "event": "on_complete",
545	        "action": "agent",
546	        "ts": "2026-05-15T21:25:36.468478+00:00"
547	      }
548	    ]
549	  },
550	  "metrics": {
551	    "success_rate": 0.681,
552	    "successes": 32,
553	    "total": 47,
554	    "by_task_type": {
555	      "look_at_obj_in_light": {
556	        "total": 6,
557	        "success": 5,
558	        "rate": 0.833
559	      },
560	      "pick_and_place_simple": {
561	        "total": 8,
562	        "success": 5,
563	        "rate": 0.625
564	      },
565	      "pick_clean_then_place_in_recep": {
566	        "total": 10,
567	        "success": 5,
568	        "rate": 0.5
569	      },
570	      "pick_cool_then_place_in_recep": {
571	        "total": 7,
572	        "success": 6,
573	        "rate": 0.857
574	      },
575	      "pick_heat_then_place_in_recep": {
576	        "total": 8,
577	        "success": 7,
578	        "rate": 0.875
579	      },
580	      "pick_two_obj_and_place": {
581	        "total": 7,
582	        "success": 4,
583	        "rate": 0.571
584	      }
585	    }
586	  },
587	  "conclusion": "success",
588	  "completed_at": "2026-05-15T21:27:48.360Z"
589	}
590	
591	--------------------------------------------------------------------------------
592	ID: v4-random-fixed-inject10-s123-eval
593	--------------------------------------------------------------------------------
594	{
595	  "status": "DONE",
596	  "retry_count": 0,
597	  "created_at": "2026-05-15T18:59:20.398Z",
598	  "updated_at": "2026-05-15T20:04:09.526Z",
599	  "hypothesis": "v4 Random fixed-size 10% injection seed=123 eval — 47 ALFWorld tasks, dose-response 5-seed expansion",
600	  "parent": "v4-random-fixed-inject10-s123",
601	  "spec": {
602	    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && python3 eval/recovery.py --model_path checkpoints/v4_random_fixed_inject10_s123/v0-20260516-015429/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --task_list eval/eval_tasks_47.json --num_episodes 47 --seed 42 --device cuda:0 --output eval_results/v4_random_fixed_inject10_s123_eval.json\"",
603	    "server": "autodl-5090",
604	    "gpu": [
605	      "cuda:3"
606	    ],
607	    "data_path": "eval/eval_tasks_47.json",
608	    "data_count": 47,
609	    "model_name": "Qwen3-8B",
610	    "seed": 42,
611	    "checkpoint_source": "v4-random-fixed-inject10-s123",
612	    "eval_data": "eval/eval_tasks_47.json",
613	    "log_path": "~/runs/tax_error_inject_agent/v4-random-fixed-inject10-s123-eval.log",
614	    "backend": "tmux",
615	    "account": "root"
616	  },
617	  "conclusion": "success",
618	  "checkpoint_path": "/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_random_fixed_inject10_s123_eval.json",
619	  "completed_at": "2026-05-15T20:03:32.060Z",
620	  "metrics": {
621	    "success_rate": 0.553,
622	    "successes": 26,
623	    "total": 47,
624	    "by_task_type": {
625	      "look_at_obj_in_light": {
626	        "total": 6,
627	        "success": 5,
628	        "rate": 0.833
629	      },
630	      "pick_and_place_simple": {
631	        "total": 8,
632	        "success": 5,
633	        "rate": 0.625
634	      },
635	      "pick_clean_then_place_in_recep": {
636	        "total": 11,
637	        "success": 5,
638	        "rate": 0.455
639	      },
640	      "pick_cool_then_place_in_recep": {
641	        "total": 7,
642	        "success": 2,
643	        "rate": 0.286
644	      },
645	      "pick_heat_then_place_in_recep": {
646	        "total": 8,
647	        "success": 6,
648	        "rate": 0.75
649	      },
650	      "pick_two_obj_and_place": {
651	        "total": 7,
652	        "success": 3,
653	        "rate": 0.429
654	      }
655	    }
656	  }
657	}
658	
659	--------------------------------------------------------------------------------
660	ID: v4-random-fixed-inject10-s7-eval
661	--------------------------------------------------------------------------------
662	{
663	  "status": "DONE",
664	  "retry_count": 0,
665	  "created_at": "2026-05-15T21:57:41.705Z",
666	  "updated_at": "2026-05-15T22:15:41.386Z",
667	  "spec": {
668	    "command": "python3 eval/recovery.py --model_path checkpoints/v4_random_fixed_inject10_s7/v1-20260516-045440/checkpoint-1635 --num_episodes 47 --seed 42",
669	    "server": "autodl-5090",
670	    "gpu": [
671	      "cuda:3"
672	    ],
673	    "pid": "202328",
674	    "log_path": "~/runs/tax_error_inject_agent/v4-random-fixed-inject10-s7-eval.log",
675	    "submitted_at": "2026-05-15T21:57:41.444Z",
676	    "submitted_via": "submit_training_job",
677	    "backend": "tmux",
678	    "account": "root",
679	    "data_path": "eval/eval_tasks_47.json",
680	    "data_count": 47,
681	    "model_name": "Qwen3-8B + LoRA (random fixed inject10 s7)",
682	    "seed": 42,
683	    "checkpoint_source": "v4-random-fixed-inject10-s7",
684	    "eval_data": "eval_tasks_47.json",
685	    "checkpoint_path": "checkpoints/v4_random_fixed_inject10_s7/v1-20260516-045440/checkpoint-1635",
686	    "wall_clock_seconds": 818,
687	    "gpu_hours": 0.23
688	  },
689	  "hypothesis": "v4 Random 10% seed=7 eval — 47 ALFWorld clean tasks. Dose-response 5-seed expansion. 最后一个 10% eval。",
690	  "reproduce": {
691	    "finished_at": "2026-05-15T22:12:57.609Z"
692	  },
693	  "extra": {
694	    "hook_events": [
695	      {
696	        "event": "on_complete",
697	        "action": "agent",
698	        "ts": "2026-05-15T22:12:59.982752+00:00"
699	      }
700	    ]
701	  },
702	  "metrics": {
703	    "success_rate": 0.617,
704	    "successes": 29,
705	    "total": 47,
706	    "by_task_type": {
707	      "look_at_obj_in_light": {
708	        "success": 5,
709	        "total": 6,
710	        "rate": 0.833
711	      },
712	      "pick_and_place_simple": {
713	        "success": 4,
714	        "total": 8,
715	        "rate": 0.5
716	      },
717	      "pick_clean_then_place_in_recep": {
718	        "success": 5,
719	        "total": 11,
720	        "rate": 0.455
721	      },
722	      "pick_cool_then_place_in_recep": {
723	        "success": 4,
724	        "total": 7,
725	        "rate": 0.571
726	      },
727	      "pick_heat_then_place_in_recep": {
728	        "success": 7,
729	        "total": 8,
730	        "rate": 0.875
731	      },
732	      "pick_two_obj_and_place": {
733	        "success": 4,
734	        "total": 7,
735	        "rate": 0.571
736	      }
737	    }
738	  },
739	  "conclusion": "success",
740	  "completed_at": "2026-05-15T22:15:41.386Z"
741	}
742	
743	--------------------------------------------------------------------------------
744	ID: v4-random-fixed-inject50-s1-eval
745	--------------------------------------------------------------------------------
746	{
747	  "status": "DONE",
748	  "retry_count": 0,
749	  "created_at": "2026-05-16T01:09:38.067Z",
750	  "updated_at": "2026-05-16T01:31:24.055Z",
751	  "spec": {
752	    "command": "python3 eval/recovery.py --model_path checkpoints/v4_random_fixed_inject50_s1/v1-20260516-075754/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --task_list eval/eval_tasks_47.json --num_episodes 47 --seed 42 --device cuda:0 --output eval_results/v4_random_fixed_inject50_s1_eval.json",
753	    "server": "autodl-5090",
754	    "gpu": "cuda:1",
755	    "data_path": "eval/eval_tasks_47.json",
756	    "data_count": 47,
757	    "model_name": "Qwen3-8B + LoRA (random fixed inject50 s1)",
758	    "seed": 42,
759	    "checkpoint_source": "v4-random-fixed-inject50-s1",
760	    "eval_data": "eval_tasks_47.json",
761	    "hypothesis": "v4 Random 50% seed=1 eval — 47 ALFWorld clean tasks. Dose-response 5-seed expansion."
762	  },
763	  "metrics": {
764	    "success_rate": 0.702,
765	    "successes": 33,
766	    "total": 47,
767	    "by_task_type": {
768	      "look_at_obj_in_light": {
769	        "total": 6,
770	        "success": 5,
771	        "rate": 0.833
772	      },
773	      "pick_and_place_simple": {
774	        "total": 8,
775	        "success": 5,
776	        "rate": 0.625
777	      },
778	      "pick_clean_then_place_in_recep": {
779	        "total": 11,
780	        "success": 8,
781	        "rate": 0.727
782	      },
783	      "pick_cool_then_place_in_recep": {
784	        "total": 7,
785	        "success": 4,
786	        "rate": 0.571
787	      },
788	      "pick_heat_then_place_in_recep": {
789	        "total": 8,
790	        "success": 6,
791	        "rate": 0.75
792	      },
793	      "pick_two_obj_and_place": {
794	        "total": 7,
795	        "success": 5,
796	        "rate": 0.714
797	      }
798	    }
799	  },
800	  "conclusion": "success",
801	  "checkpoint_path": "/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_random_fixed_inject50_s1_eval.json",
802	  "log_path": "~/runs/tax_error_inject_agent/v4-random-fixed-inject50-s1-eval.log",
803	  "completed_at": "2026-05-16T01:31:24.055Z"
804	}
805	
806	--------------------------------------------------------------------------------
807	ID: v4-random-fixed-inject50-s7-eval
808	--------------------------------------------------------------------------------
809	{
810	  "status": "DONE",
811	  "retry_count": 0,
812	  "created_at": "2026-05-16T01:09:39.957Z",
813	  "updated_at": "2026-05-16T01:21:18.406Z",
814	  "spec": {
815	    "command": "python3 eval/recovery.py --model_path checkpoints/v4_random_fixed_inject50_s7/v0-20260516-075756/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --task_list eval/eval_tasks_47.json --num_episodes 47 --seed 42 --device cuda:0 --output eval_results/v4_random_fixed_inject50_s7_eval.json",
816	    "server": "autodl-5090",
817	    "gpu": "cuda:3",
818	    "data_path": "eval/eval_tasks_47.json",
819	    "data_count": 47,
820	    "model_name": "Qwen3-8B + LoRA (random fixed inject50 s7)",
821	    "seed": 42,
822	    "checkpoint_source": "v4-random-fixed-inject50-s7",
823	    "eval_data": "eval_tasks_47.json",
824	    "hypothesis": "v4 Random 50% seed=7 eval — 47 ALFWorld clean tasks. Dose-response 5-seed expansion.",
825	    "checkpoint_path": "checkpoints/v4_random_fixed_inject50_s7/v0-20260516-075756/checkpoint-1635",
826	    "log_path": "eval_results/v4_random_fixed_inject50_s7_eval.json"
827	  },
828	  "metrics": {
829	    "success_rate": 0.468,
830	    "successes": 22,
831	    "total": 47,
832	    "by_task_type": {
833	      "look_at_obj_in_light": {
834	        "total": 6,
835	        "success": 4,
836	        "rate": 0.667
837	      },
838	      "pick_and_place_simple": {
839	        "total": 8,
840	        "success": 4,
841	        "rate": 0.5
842	      },
843	      "pick_clean_then_place_in_recep": {
844	        "total": 11,
845	        "success": 5,
846	        "rate": 0.455
847	      },
848	      "pick_cool_then_place_in_recep": {
849	        "total": 7,
850	        "success": 1,
851	        "rate": 0.143
852	      },
853	      "pick_heat_then_place_in_recep": {
854	        "total": 8,
855	        "success": 5,
856	        "rate": 0.625
857	      },
858	      "pick_two_obj_and_place": {
859	        "total": 7,
860	        "success": 3,
861	        "rate": 0.429
862	      }
863	    }
864	  },
865	  "conclusion": "success",
866	  "completed_at": "2026-05-16T01:21:18.406Z"
867	}
868	
869	--------------------------------------------------------------------------------
870	ID: v4-random-recovery-eval
871	--------------------------------------------------------------------------------
872	{
873	  "status": "DONE",
874	  "retry_count": 0,
875	  "created_at": "2026-05-14T21:04:57.591Z",
876	  "updated_at": "2026-05-14T22:00:43.285Z",
877	  "hypothesis": "v4 Random SFT seed=42 recovery eval (injected_eval.py) — 47 episodes with error injection, measuring detection/recovery/success rates under P1/P2/C1/C4 operators. Phase 2 counterpart to vanilla/taxei recovery eval.",
878	  "spec": {
879	    "command": "CUDA_VISIBLE_DEVICES=0 python3 eval/injected_eval.py --model_path checkpoints/mini_random_sft_v4/v1-20260514-213104/checkpoint-3387 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --model_variant random --num_episodes 47 --seed 42 --device cuda:0 --output eval_results/v4_random_recovery_eval.json",
880	    "server": "autodl-5090",
881	    "gpu": "cuda:0",
882	    "pid": 90124,
883	    "model_name": "Qwen3-8B + LoRA (random SFT v4)",
884	    "seed": 42,
885	    "checkpoint_source": "checkpoints/mini_random_sft_v4/v1-20260514-213104/checkpoint-3387",
886	    "eval_data": "valid_unseen (47 episodes)",
887	    "log_path": "/tmp/v4_random_recovery_eval.log",
888	    "output_path": "eval_results/v4_random_recovery_eval.json",
889	    "data_path": "valid_unseen",
890	    "data_count": 47
891	  },
892	  "conclusion": "success",
893	  "checkpoint_path": "eval_results/v4_random_recovery_eval.json",
894	  "completed_at": "2026-05-14T21:42:07.544Z",
895	  "metrics": {
896	    "recovery_rate": 0.638,
897	    "detection_rate": 0,
898	    "successes": 30,
899	    "total": 47,
900	    "source": "json-file-verified",
901	    "note": "r1=29/47, r2=30/47, ±2pp run-to-run variance on P1 non-determinism"
902	  }
903	}
904	
905	--------------------------------------------------------------------------------
906	ID: v4-random-recovery-eval-s0
907	--------------------------------------------------------------------------------
908	{
909	  "status": "DONE",
910	  "retry_count": 0,
911	  "created_at": "2026-05-15T12:44:10.000Z",
912	  "updated_at": "2026-05-16T10:54:26.532Z",
913	  "spec": {
914	    "model_name": "Qwen3-8B + LoRA (mini_random_sft_v4_seed0)",
915	    "seed": 0,
916	    "method": "random",
917	    "eval_type": "recovery",
918	    "parent": "v4-random-sft-s0",
919	    "checkpoint_source": "checkpoints/mini_random_sft_v4_seed0/v0-20260515-014329/checkpoint-3387",
920	    "eval_data": "ALFWorld 47 episodes with error injection",
921	    "server": "autodl-5090",
922	    "command": "CUDA_VISIBLE_DEVICES=0 python eval/injected_eval.py --model_path checkpoints/mini_random_sft_v4_seed0/v0-20260515-014329/checkpoint-3387 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --model_variant random --output eval_results/v4_random_recovery_eval_s0.json --device cuda:0 --seed 42 --num_episodes 47",
923	    "data_path": "/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_random_recovery_eval_s0.json",
924	    "data_count": 47
925	  },
926	  "conclusion": "success",
927	  "checkpoint_path": "checkpoints/mini_random_sft_v4_seed0/v0-20260515-014329/checkpoint-3387",
928	  "log_path": "eval_results/v4_random_recovery_eval_s0.json",
929	  "completed_at": "2026-05-16T10:54:19.062Z",
930	  "metrics": {
931	    "recovery_rate": 0.553,
932	    "detection_rate": 0,
933	    "success_rate": 0.553,
934	    "total_episodes": 47,
935	    "by_operator": {
936	      "C1_context_truncation": {
937	        "total": 12,
938	        "recovered": 7,
939	        "recovery_rate": 0.583
940	      },
941	      "C4_observation_masking": {
942	        "total": 11,
943	        "recovered": 6,
944	        "recovery_rate": 0.545
945	      },
946	      "P1_step_order_swap": {
947	        "total": 12,
948	        "recovered": 7,
949	        "recovery_rate": 0.583
950	      },
951	      "P2_sub_goal_deletion": {
952	        "total": 12,
953	        "recovered": 6,
954	        "recovery_rate": 0.5
955	      }
956	    }
957	  }
958	}
959	
960	--------------------------------------------------------------------------------
961	ID: v4-random-recovery-eval-s123
962	--------------------------------------------------------------------------------
963	{
964	  "status": "DONE",
965	  "retry_count": 0,
966	  "created_at": "2026-05-15T12:44:11.530Z",
967	  "updated_at": "2026-05-16T12:38:01.309Z",
968	  "spec": {
969	    "model_name": "Qwen3-8B + Random LoRA s123",
970	    "seed": 42,
971	    "method": "random",
972	    "eval_type": "recovery",
973	    "parent": "v4-random-sft-s123",
974	    "checkpoint_source": "checkpoints/mini_random_sft_v4_seed123/v0-20260515-055925/checkpoint-3387",
975	    "eval_data": "ALFWorld injected eval (47 episodes)",
976	    "server": "autodl-5090",
977	    "command": "CUDA_VISIBLE_DEVICES=3 python3 eval/injected_eval.py --model_path checkpoints/mini_random_sft_v4_seed123/v0-20260515-055925/checkpoint-3387 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --model_variant random --output eval_results/v4_random_recovery_eval_s123.json --seed 42 --num_episodes 47",
978	    "data_path": "eval/injected_eval.py",
979	    "data_count": 47,
980	    "checkpoint_path": "checkpoints/mini_random_sft_v4_seed123/v0-20260515-055925/checkpoint-3387",
981	    "log_path": "eval_results/v4_random_recovery_eval_s123.log"
982	  },
983	  "conclusion": "success",
984	  "completed_at": "2026-05-16T12:07:20.925Z",
985	  "metrics": {
986	    "recovery_rate": 0.66,
987	    "detection_rate": 0,
988	    "total_episodes": 47,
989	    "by_operator": {
990	      "C1_context_truncation": {
991	        "recovery_rate": 0.75,
992	        "recovered": 9,
993	        "total": 12
994	      },
995	      "P2_sub_goal_deletion": {
996	        "recovery_rate": 0.75,
997	        "recovered": 9,
998	        "total": 12
999	      },
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01BbmLXayvRWQ5YLrpnBLT8u",
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55",
  "uuid": "21b10f1f-9ce3-4382-a7c1-a4e956b13399"
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
  "task_id": "a1b20f795e02ae461",
  "tool_use_id": "toolu_01BbmLXayvRWQ5YLrpnBLT8u",
  "description": "Reading ~/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/ae491a69-2268-4f52-bbd5-112d75ec9c55/tool-results/bt0rx9074.txt",
  "usage": {
    "total_tokens": 53233,
    "tool_uses": 11,
    "duration_ms": 77127
  },
  "last_tool_name": "Read",
  "uuid": "b88fefb2-9fa6-4044-9302-49509765ffc9",
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55"
}
```

---

### Tool call

_source line 46_

<details open><summary>🔧 Tool call — Read · `toolu_01AUkMFou34pXEwx1WNC6ve8`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/ae491a69-2268-4f52-bbd5-112d75ec9c55/tool-results/bt0rx9074.txt",
  "offset": 1000,
  "limit": 600
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01BbmLXayvRWQ5YLrpnBLT8u",
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55",
  "uuid": "e1d8ef3e-a3ae-45d0-a743-e573ff2882d2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019AcfEPQsqaRavk98pK5HgS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9230,
      "cache_read_input_tokens": 43524,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9230,
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

_source line 47 · 2026-05-16T14:54:57.825Z_

<details><summary>↩ Tool result · `toolu_01AUkMFou34pXEwx1WNC6ve8`</summary>

```text
1000	      "P1_step_order_swap": {
1001	        "recovery_rate": 0.583,
1002	        "recovered": 7,
1003	        "total": 12
1004	      },
1005	      "C4_observation_masking": {
1006	        "recovery_rate": 0.545,
1007	        "recovered": 6,
1008	        "total": 11
1009	      }
1010	    }
1011	  }
1012	}
1013	
1014	--------------------------------------------------------------------------------
1015	ID: v4-random-seed7-eval
1016	--------------------------------------------------------------------------------
1017	{
1018	  "status": "DONE",
1019	  "retry_count": 0,
1020	  "created_at": "2026-05-15T17:29:15.592Z",
1021	  "updated_at": "2026-05-15T17:43:36.723Z",
1022	  "spec": {
1023	    "command": "python3 eval/recovery.py --model_path checkpoints/mini_random_sft_v4_seed7/v0-20260515-233427/checkpoint-3387 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --task_list eval/eval_tasks_47.json --num_episodes 47 --seed 42 --device cuda:0 --output eval_results/v4_random_seed7_eval.json",
1024	    "server": "autodl-5090",
1025	    "gpu": [
1026	      "cuda:1"
1027	    ],
1028	    "pid": "179098",
1029	    "log_path": "~/runs/tax_error_inject_agent/v4-random-seed7-eval.log",
1030	    "submitted_at": "2026-05-15T17:29:24.122Z",
1031	    "submitted_via": "submit_training_job",
1032	    "backend": "tmux",
1033	    "account": "root",
1034	    "data_path": "eval/eval_tasks_47.json",
1035	    "data_count": 47,
1036	    "model_name": "Qwen3-8B + LoRA (random SFT seed=7)",
1037	    "seed": 42,
1038	    "checkpoint_source": "v4-random-seed7",
1039	    "eval_data": "eval_tasks_47.json",
1040	    "checkpoint_path": "/root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_random_sft_v4_seed7/v0-20260515-233427/checkpoint-3387",
1041	    "wall_clock_seconds": 852.6,
1042	    "gpu_hours": 0.24
1043	  },
1044	  "hypothesis": "v4 Random SFT seed=7 eval — 47 ALFWorld tasks, 5-seed expansion ← 基于 v4-random-seed7",
1045	  "reproduce": {
1046	    "finished_at": "2026-05-15T17:40:45.965Z"
1047	  },
1048	  "extra": {
1049	    "hook_events": [
1050	      {
1051	        "event": "on_complete",
1052	        "action": "agent",
1053	        "ts": "2026-05-15T17:40:48.585893+00:00"
1054	      }
1055	    ]
1056	  },
1057	  "metrics": {
1058	    "success_rate": 0.553,
1059	    "successes": 26,
1060	    "total": 47,
1061	    "by_task_type": {
1062	      "look_at_obj_in_light": {
1063	        "total": 6,
1064	        "success": 5,
1065	        "rate": 0.833
1066	      },
1067	      "pick_and_place_simple": {
1068	        "total": 8,
1069	        "success": 4,
1070	        "rate": 0.5
1071	      },
1072	      "pick_clean_then_place_in_recep": {
1073	        "total": 11,
1074	        "success": 6,
1075	        "rate": 0.545
1076	      },
1077	      "pick_cool_then_place_in_recep": {
1078	        "total": 7,
1079	        "success": 3,
1080	        "rate": 0.429
1081	      },
1082	      "pick_heat_then_place_in_recep": {
1083	        "total": 8,
1084	        "success": 5,
1085	        "rate": 0.625
1086	      },
1087	      "pick_two_obj_and_place": {
1088	        "total": 7,
1089	        "success": 3,
1090	        "rate": 0.429
1091	      }
1092	    }
1093	  },
1094	  "conclusion": "success",
1095	  "completed_at": "2026-05-15T17:43:36.723Z"
1096	}
1097	
1098	--------------------------------------------------------------------------------
1099	ID: v4-taxei-fixed-inject10-s1-eval-r2
1100	--------------------------------------------------------------------------------
1101	{
1102	  "status": "DONE",
1103	  "retry_count": 0,
1104	  "created_at": "2026-05-15T20:54:05.248Z",
1105	  "updated_at": "2026-05-15T21:06:11.418Z",
1106	  "spec": {
1107	    "parent": "v4-taxei-fixed-inject10-s1",
1108	    "checkpoint_source": "v4-taxei-fixed-inject10-s1",
1109	    "eval_data": "eval_tasks_47.json",
1110	    "data_count": 47,
1111	    "model_name": "Qwen3-8B + LoRA (taxei fixed inject10 s1)",
1112	    "seed": 42,
1113	    "data_path": "eval/eval_tasks_47.json"
1114	  },
1115	  "hypothesis": "v4 TaxEI 10% seed=1 eval (r2, dedicated GPU) — 47 ALFWorld clean tasks.",
1116	  "reproduce": {
1117	    "finished_at": "2026-05-15T21:04:33.190Z"
1118	  },
1119	  "extra": {
1120	    "hook_events": [
1121	      {
1122	        "event": "on_complete",
1123	        "action": "agent",
1124	        "ts": "2026-05-15T21:04:36.432028+00:00"
1125	      }
1126	    ]
1127	  },
1128	  "metrics": {
1129	    "success_rate": 0.511,
1130	    "successes": 24,
1131	    "total": 47,
1132	    "by_task_type": {
1133	      "look_at_obj_in_light": {
1134	        "total": 6,
1135	        "success": 4,
1136	        "rate": 0.667
1137	      },
1138	      "pick_and_place_simple": {
1139	        "total": 8,
1140	        "success": 4,
1141	        "rate": 0.5
1142	      },
1143	      "pick_clean_then_place_in_recep": {
1144	        "total": 11,
1145	        "success": 5,
1146	        "rate": 0.455
1147	      },
1148	      "pick_cool_then_place_in_recep": {
1149	        "total": 7,
1150	        "success": 2,
1151	        "rate": 0.286
1152	      },
1153	      "pick_heat_then_place_in_recep": {
1154	        "total": 8,
1155	        "success": 6,
1156	        "rate": 0.75
1157	      },
1158	      "pick_two_obj_and_place": {
1159	        "total": 7,
1160	        "success": 3,
1161	        "rate": 0.429
1162	      }
1163	    }
1164	  },
1165	  "checkpoint_path": "/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_taxei_fixed_inject10_s1_eval.json",
1166	  "log_path": "/root/runs/tax_error_inject_agent/v4-taxei-fixed-inject10-s1-eval-r2.log",
1167	  "conclusion": "success",
1168	  "completed_at": "2026-05-15T21:06:11.418Z"
1169	}
1170	
1171	--------------------------------------------------------------------------------
1172	ID: v4-taxei-fixed-inject10-s123-eval-r3
1173	--------------------------------------------------------------------------------
1174	{
1175	  "status": "DONE",
1176	  "retry_count": 0,
1177	  "created_at": "2026-05-15T20:40:05.773Z",
1178	  "updated_at": "2026-05-15T20:54:14.378Z",
1179	  "spec": {
1180	    "command": "python3 eval/recovery.py --model_path checkpoints/v4_taxei_fixed_inject10_s123/v0-20260516-014833/checkpoint-1635 --num_episodes 47 --seed 42",
1181	    "server": "autodl-5090",
1182	    "gpu": [
1183	      "cuda:2"
1184	    ],
1185	    "pid": "194978",
1186	    "log_path": "~/runs/tax_error_inject_agent/v4-taxei-fixed-inject10-s123-eval-r3.log",
1187	    "submitted_at": "2026-05-15T20:40:05.519Z",
1188	    "submitted_via": "submit_training_job",
1189	    "backend": "tmux",
1190	    "account": "root",
1191	    "parent": "v4-taxei-fixed-inject10-s123",
1192	    "checkpoint_source": "v4-taxei-fixed-inject10-s123",
1193	    "eval_data": "eval_tasks_47.json",
1194	    "data_count": 47,
1195	    "model_name": "Qwen3-8B + LoRA (taxei fixed inject10 s123)",
1196	    "seed": 42,
1197	    "data_path": "eval/eval_tasks_47.json",
1198	    "wall_clock_seconds": 848.9,
1199	    "gpu_hours": 0.24
1200	  },
1201	  "hypothesis": "v4 TaxEI 10% seed=123 eval (r3, dedicated GPU) — 47 ALFWorld clean tasks.",
1202	  "reproduce": {
1203	    "finished_at": "2026-05-15T20:50:16.884Z"
1204	  },
1205	  "extra": {
1206	    "hook_events": [
1207	      {
1208	        "event": "on_complete",
1209	        "action": "agent",
1210	        "ts": "2026-05-15T20:50:19.215245+00:00"
1211	      }
1212	    ]
1213	  },
1214	  "metrics": {
1215	    "success_rate": 0.553,
1216	    "successes": 26,
1217	    "total": 47,
1218	    "by_task_type": {
1219	      "look_at_obj_in_light": {
1220	        "total": 6,
1221	        "success": 5,
1222	        "rate": 0.833
1223	      },
1224	      "pick_and_place_simple": {
1225	        "total": 8,
1226	        "success": 4,
1227	        "rate": 0.5
1228	      },
1229	      "pick_clean_then_place_in_recep": {
1230	        "total": 11,
1231	        "success": 5,
1232	        "rate": 0.455
1233	      },
1234	      "pick_cool_then_place_in_recep": {
1235	        "total": 7,
1236	        "success": 2,
1237	        "rate": 0.286
1238	      },
1239	      "pick_heat_then_place_in_recep": {
1240	        "total": 8,
1241	        "success": 6,
1242	        "rate": 0.75
1243	      },
1244	      "pick_two_obj_and_place": {
1245	        "total": 7,
1246	        "success": 4,
1247	        "rate": 0.571
1248	      }
1249	    }
1250	  },
1251	  "conclusion": "success",
1252	  "checkpoint_path": "checkpoints/v4_taxei_fixed_inject10_s123/v0-20260516-014833/checkpoint-1635",
1253	  "completed_at": "2026-05-15T20:54:14.378Z"
1254	}
1255	
1256	--------------------------------------------------------------------------------
1257	ID: v4-taxei-fixed-inject10-s7-eval
1258	--------------------------------------------------------------------------------
1259	{
1260	  "status": "DONE",
1261	  "retry_count": 0,
1262	  "created_at": "2026-05-15T21:02:22.234Z",
1263	  "updated_at": "2026-05-15T21:27:44.185Z",
1264	  "spec": {
1265	    "command": "python3 eval/recovery.py --model_path checkpoints/v4_taxei_fixed_inject10_s7/v1-20260516-040128/checkpoint-1635 --num_episodes 47 --seed 42",
1266	    "server": "autodl-5090",
1267	    "gpu": [
1268	      "cuda:0"
1269	    ],
1270	    "pid": "197555",
1271	    "log_path": "~/runs/tax_error_inject_agent/v4-taxei-fixed-inject10-s7-eval.log",
1272	    "submitted_at": "2026-05-15T21:02:21.785Z",
1273	    "submitted_via": "submit_training_job",
1274	    "backend": "tmux",
1275	    "account": "root",
1276	    "data_path": "eval/eval_tasks_47.json",
1277	    "data_count": 47,
1278	    "model_name": "Qwen3-8B + LoRA (taxei fixed inject10 s7)",
1279	    "seed": 42,
1280	    "checkpoint_source": "v4-taxei-fixed-inject10-s7",
1281	    "eval_data": "eval_tasks_47.json",
1282	    "wall_clock_seconds": 1522.4,
1283	    "gpu_hours": 0.42
1284	  },
1285	  "hypothesis": "v4 TaxEI 10% seed=7 eval — 47 ALFWorld clean tasks. Dose-response 5-seed expansion.",
1286	  "reproduce": {
1287	    "finished_at": "2026-05-15T21:19:30.996Z"
1288	  },
1289	  "extra": {
1290	    "hook_events": [
1291	      {
1292	        "event": "on_complete",
1293	        "action": "agent",
1294	        "ts": "2026-05-15T21:19:33.518373+00:00"
1295	      }
1296	    ]
1297	  },
1298	  "metrics": {
1299	    "success_rate": 0.681,
1300	    "successes": 32,
1301	    "total": 47,
1302	    "by_task_type": {
1303	      "look_at_obj_in_light": {
1304	        "total": 6,
1305	        "success": 5,
1306	        "rate": 0.833
1307	      },
1308	      "pick_and_place_simple": {
1309	        "total": 8,
1310	        "success": 5,
1311	        "rate": 0.625
1312	      },
1313	      "pick_clean_then_place_in_recep": {
1314	        "total": 11,
1315	        "success": 7,
1316	        "rate": 0.636
1317	      },
1318	      "pick_cool_then_place_in_recep": {
1319	        "total": 7,
1320	        "success": 4,
1321	        "rate": 0.571
1322	      },
1323	      "pick_heat_then_place_in_recep": {
1324	        "total": 8,
1325	        "success": 7,
1326	        "rate": 0.875
1327	      },
1328	      "pick_two_obj_and_place": {
1329	        "total": 7,
1330	        "success": 4,
1331	        "rate": 0.571
1332	      }
1333	    }
1334	  },
1335	  "checkpoint_path": "/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_taxei_fixed_inject10_s7_eval.json",
1336	  "conclusion": "success",
1337	  "completed_at": "2026-05-15T21:27:44.185Z"
1338	}
1339	
1340	--------------------------------------------------------------------------------
1341	ID: v4-taxei-fixed-inject50-s1-eval
1342	--------------------------------------------------------------------------------
1343	{
1344	  "status": "DONE",
1345	  "retry_count": 0,
1346	  "created_at": "2026-05-16T01:09:36.875Z",
1347	  "updated_at": "2026-05-16T01:31:23.037Z",
1348	  "spec": {
1349	    "command": "python3 eval/recovery.py --model_path checkpoints/v4_taxei_fixed_inject50_s1/v0-20260516-075747/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --task_list eval/eval_tasks_47.json --num_episodes 47 --seed 42 --device cuda:0 --output eval_results/v4_taxei_fixed_inject50_s1_eval.json",
1350	    "server": "autodl-5090",
1351	    "gpu": "cuda:0",
1352	    "data_path": "eval/eval_tasks_47.json",
1353	    "data_count": 47,
1354	    "model_name": "Qwen3-8B + LoRA (taxei fixed inject50 s1)",
1355	    "seed": 42,
1356	    "checkpoint_source": "v4-taxei-fixed-inject50-s1",
1357	    "eval_data": "eval_tasks_47.json",
1358	    "hypothesis": "v4 TaxEI 50% seed=1 eval — 47 ALFWorld clean tasks. Dose-response 5-seed expansion."
1359	  },
1360	  "metrics": {
1361	    "success_rate": 0.638,
1362	    "successes": 30,
1363	    "total": 47,
1364	    "by_task_type": {
1365	      "look_at_obj_in_light": {
1366	        "total": 6,
1367	        "success": 6,
1368	        "rate": 1
1369	      },
1370	      "pick_and_place_simple": {
1371	        "total": 8,
1372	        "success": 5,
1373	        "rate": 0.625
1374	      },
1375	      "pick_clean_then_place_in_recep": {
1376	        "total": 11,
1377	        "success": 7,
1378	        "rate": 0.636
1379	      },
1380	      "pick_cool_then_place_in_recep": {
1381	        "total": 7,
1382	        "success": 4,
1383	        "rate": 0.571
1384	      },
1385	      "pick_heat_then_place_in_recep": {
1386	        "total": 8,
1387	        "success": 5,
1388	        "rate": 0.625
1389	      },
1390	      "pick_two_obj_and_place": {
1391	        "total": 7,
1392	        "success": 3,
1393	        "rate": 0.429
1394	      }
1395	    }
1396	  },
1397	  "conclusion": "success",
1398	  "checkpoint_path": "/root/autodl-tmp/tax_error_inject_agent/eval_results/v4_taxei_fixed_inject50_s1_eval.json",
1399	  "log_path": "~/runs/tax_error_inject_agent/v4-taxei-fixed-inject50-s1-eval.log",
1400	  "completed_at": "2026-05-16T01:31:23.037Z"
1401	}
1402	
1403	--------------------------------------------------------------------------------
1404	ID: v4-taxei-fixed-inject50-s7-eval
1405	--------------------------------------------------------------------------------
1406	{
1407	  "status": "DONE",
1408	  "retry_count": 0,
1409	  "created_at": "2026-05-16T01:09:39.016Z",
1410	  "updated_at": "2026-05-16T01:21:17.391Z",
1411	  "spec": {
1412	    "command": "python3 eval/recovery.py --model_path checkpoints/v4_taxei_fixed_inject50_s7/v0-20260516-075754/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --task_list eval/eval_tasks_47.json --num_episodes 47 --seed 42 --device cuda:0 --output eval_results/v4_taxei_fixed_inject50_s7_eval.json",
1413	    "server": "autodl-5090",
1414	    "gpu": "cuda:2",
1415	    "data_path": "eval/eval_tasks_47.json",
1416	    "data_count": 47,
1417	    "model_name": "Qwen3-8B + LoRA (taxei fixed inject50 s7)",
1418	    "seed": 42,
1419	    "checkpoint_source": "v4-taxei-fixed-inject50-s7",
1420	    "eval_data": "eval_tasks_47.json",
1421	    "hypothesis": "v4 TaxEI 50% seed=7 eval — 47 ALFWorld clean tasks. Dose-response 5-seed expansion.",
1422	    "checkpoint_path": "checkpoints/v4_taxei_fixed_inject50_s7/v0-20260516-075754/checkpoint-1635",
1423	    "log_path": "eval_results/v4_taxei_fixed_inject50_s7_eval.json"
1424	  },
1425	  "metrics": {
1426	    "success_rate": 0.553,
1427	    "successes": 26,
1428	    "total": 47,
1429	    "by_task_type": {
1430	      "look_at_obj_in_light": {
1431	        "total": 6,
1432	        "success": 5,
1433	        "rate": 0.833
1434	      },
1435	      "pick_and_place_simple": {
1436	        "total": 8,
1437	        "success": 4,
1438	        "rate": 0.5
1439	      },
1440	      "pick_clean_then_place_in_recep": {
1441	        "total": 11,
1442	        "success": 6,
1443	        "rate": 0.545
1444	      },
1445	      "pick_cool_then_place_in_recep": {
1446	        "total": 7,
1447	        "success": 2,
1448	        "rate": 0.286
1449	      },
1450	      "pick_heat_then_place_in_recep": {
1451	        "total": 8,
1452	        "success": 6,
1453	        "rate": 0.75
1454	      },
1455	      "pick_two_obj_and_place": {
1456	        "total": 7,
1457	        "success": 3,
1458	        "rate": 0.429
1459	      }
1460	    }
1461	  },
1462	  "conclusion": "success",
1463	  "completed_at": "2026-05-16T01:21:17.391Z"
1464	}
1465	
1466	--------------------------------------------------------------------------------
1467	ID: v4-taxei-recovery-eval
1468	--------------------------------------------------------------------------------
1469	{
1470	  "status": "DONE",
1471	  "retry_count": 0,
1472	  "created_at": "2026-05-14T20:40:41.154Z",
1473	  "updated_at": "2026-05-14T21:20:17.664Z",
1474	  "spec": {
1475	    "hypothesis": "D010 Phase 2: Recovery eval with action injection on TaxEI seed=42 checkpoint — measuring TaxEI-trained model's recovery ability vs vanilla",
1476	    "command": "CUDA_VISIBLE_DEVICES=3 python3 eval/injected_eval.py --model_path /root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_taxei_sft_v4/v1-20260514-213102/checkpoint-3387 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --model_variant taxei --device cuda:0 --seed 42 --output eval_results/v4_taxei_recovery_eval.json",
1477	    "server": "autodl-5090",
1478	    "gpu": "cuda:3",
1479	    "pid": 87614,
1480	    "data_path": "/root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_taxei_sft_v4/v1-20260514-213102/checkpoint-3387",
1481	    "data_count": 47,
1482	    "model_name": "Qwen3-8B + TaxEI LoRA v4 checkpoint-3387",
1483	    "seed": 42,
1484	    "checkpoint_source": "mini_taxei_sft_v4/v1-20260514-213102/checkpoint-3387",
1485	    "eval_data": "ALFWorld valid_unseen 47 tasks with action injection",
1486	    "checkpoint_path": "eval_results/v4_taxei_recovery_eval.json",
1487	    "log_path": "/root/runs/tax_error_inject_agent/v4-taxei-recovery-eval.log"
1488	  },
1489	  "hypothesis": "v4 TaxEI SFT seed=42 recovery eval (injected_eval.py) — 47 episodes with error injection, measuring detection/recovery/success rates under P1/P2/C1/C4 operators. Phase 2 counterpart to vanilla recovery eval.",
1490	  "reproduce": {
1491	    "finished_at": "2026-05-14T20:58:38.335Z"
1492	  },
1493	  "failure_reason": "process dead 5× with no sentinel/W&B — auto-resolved as failed",
1494	  "conclusion": "negative",
1495	  "completed_at": "2026-05-14T20:58:38.665Z",
1496	  "extra": {
1497	    "hook_events": [
1498	      {
1499	        "event": "on_failed",
1500	        "action": "agent",
1501	        "ts": "2026-05-14T20:58:39.601019+00:00"
1502	      }
1503	    ]
1504	  },
1505	  "metrics": {
1506	    "success_rate": 0.596,
1507	    "successes": 28,
1508	    "total": 47,
1509	    "recovery_rate": 0.596,
1510	    "detection_rate": 0
1511	  }
1512	}
1513	
1514	--------------------------------------------------------------------------------
1515	ID: v4-taxei-recovery-eval-r2
1516	--------------------------------------------------------------------------------
1517	{
1518	  "status": "DONE",
1519	  "retry_count": 0,
1520	  "created_at": "2026-05-14T21:23:55.110Z",
1521	  "updated_at": "2026-05-14T21:46:19.993Z",
1522	  "spec": {
1523	    "command": "CUDA_VISIBLE_DEVICES=1 python3 eval/injected_eval.py --model_path checkpoints/mini_taxei_sft_v4/v1-20260514-213102/checkpoint-3387 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --model_variant taxei --num_episodes 47 --seed 42 --device cuda:0 --output eval_results/v4_taxei_recovery_eval_r2.json",
1524	    "server": "autodl-5090",
1525	    "model_name": "Qwen3-8B + LoRA (mini_taxei_sft_v4 checkpoint-3387)",
1526	    "seed": 42,
1527	    "checkpoint_source": "checkpoints/mini_taxei_sft_v4/v1-20260514-213102/checkpoint-3387",
1528	    "eval_data": "47 episodes with error injection (4 operators: C1_context_truncation, C4_observation_masking, P1_step_order_swap, P2_sub_goal_deletion)",
1529	    "data_path": "eval/injected_eval.py",
1530	    "data_count": 47,
1531	    "hypothesis": "v4 TaxEI SFT seed=42 recovery eval retry — 47 episodes with error injection, measuring detection/recovery/success rates. Previous attempt reported process dead 5x.",
1532	    "pid": 90519,
1533	    "log_path": "/tmp/v4_taxei_recovery_eval_r2.log"
1534	  },
1535	  "conclusion": "success",
1536	  "checkpoint_path": "eval_results/v4_taxei_recovery_eval_r2.json",
1537	  "completed_at": "2026-05-14T21:42:08.000Z",
1538	  "metrics": {
1539	    "recovery_rate": 0.596,
1540	    "detection_rate": 0,
1541	    "total_episodes": 47,
1542	    "per_operator": {
1543	      "C1_context_truncation": {
1544	        "recovered": 8,
1545	        "total": 12,
1546	        "rate": 0.667
1547	      },
1548	      "C4_observation_masking": {
1549	        "recovered": 7,
1550	        "total": 11,
1551	        "rate": 0.636
1552	      },
1553	      "P1_step_order_swap": {
1554	        "recovered": 7,
1555	        "total": 12,
1556	        "rate": 0.583
1557	      },
1558	      "P2_sub_goal_deletion": {
1559	        "recovered": 6,
1560	        "total": 12,
1561	        "rate": 0.5
1562	      }
1563	    }
1564	  }
1565	}
1566	
1567	--------------------------------------------------------------------------------
1568	ID: v4-taxei-seed7-eval
1569	--------------------------------------------------------------------------------
1570	{
1571	  "status": "DONE",
1572	  "retry_count": 0,
1573	  "created_at": "2026-05-15T15:40:01.513Z",
1574	  "updated_at": "2026-05-15T16:40:14.867Z",
1575	  "hypothesis": "v4 TaxEI SFT seed=7 eval — 47 ALFWorld tasks, 5-seed expansion",
1576	  "parent": "v4-taxei-seed7",
1577	  "spec": {
1578	    "command": "CUDA_VISIBLE_DEVICES=3 python3 eval/recovery.py --model_path checkpoints/mini_taxei_sft_v4_seed7/v0-20260515-214039/checkpoint-3387 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --task_list eval/eval_tasks_47.json --num_episodes 47 --seed 42 --device cuda:0 --output eval_results/v4_taxei_seed7_eval.json",
1579	    "server": "autodl-5090",
1580	    "data_path": "eval/eval_tasks_47.json",
1581	    "data_count": 47,
1582	    "model_name": "Qwen3-8B + LoRA (TaxEI v4 seed=7)",
1583	    "seed": 42,
1584	    "checkpoint_source": "checkpoints/mini_taxei_sft_v4_seed7/v0-20260515-214039/checkpoint-3387",
1585	    "eval_data": "47 ALFWorld tasks (clean, no injection)",
1586	    "parent": "v4-taxei-seed7",
1587	    "gpu": [
1588	      "cuda:3"
1589	    ],
1590	    "pid": "165338",
1591	    "log_path": "~/runs/tax_error_inject_agent/v4-taxei-seed7-eval.log",
1592	    "checkpoint_path": "eval_results/v4_taxei_seed7_eval.json",
1593	    "backend": "tmux",
1594	    "account": "root"
1595	  },
1596	  "conclusion": "success",
1597	  "metrics": {
1598	    "success_rate": 0.617,
1599	    "successes": 29,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01BbmLXayvRWQ5YLrpnBLT8u",
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55",
  "uuid": "531dca5a-7555-4098-844e-68490f5ebb4b"
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
  "task_id": "a1b20f795e02ae461",
  "tool_use_id": "toolu_01BbmLXayvRWQ5YLrpnBLT8u",
  "description": "Reading ~/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/ae491a69-2268-4f52-bbd5-112d75ec9c55/tool-results/bt0rx9074.txt",
  "usage": {
    "total_tokens": 62880,
    "tool_uses": 12,
    "duration_ms": 83214
  },
  "last_tool_name": "Read",
  "uuid": "5dc58b41-00eb-4f40-8cd8-83d545875cac",
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55"
}
```

---

### Tool call

_source line 49_

<details open><summary>🔧 Tool call — Read · `toolu_015gvm1ijBiJM7N2KkQYoo3A`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/ae491a69-2268-4f52-bbd5-112d75ec9c55/tool-results/bt0rx9074.txt",
  "offset": 1600,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01BbmLXayvRWQ5YLrpnBLT8u",
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55",
  "uuid": "e9af2cb3-cac9-4abb-b23c-71e13d31bb25",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BFcyezy95wtwpPPxuUstQr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9612,
      "cache_read_input_tokens": 52754,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9612,
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

_source line 50 · 2026-05-16T14:55:03.876Z_

<details><summary>↩ Tool result · `toolu_015gvm1ijBiJM7N2KkQYoo3A`</summary>

```text
1600	    "total": 47,
1601	    "by_task": {
1602	      "look_at_obj_in_light": "4/6 (0.667)",
1603	      "pick_and_place_simple": "5/8 (0.625)",
1604	      "pick_clean_then_place_in_recep": "5/11 (0.455)",
1605	      "pick_cool_then_place_in_recep": "4/7 (0.571)",
1606	      "pick_heat_then_place_in_recep": "7/8 (0.875)",
1607	      "pick_two_obj_and_place": "4/7 (0.571)"
1608	    }
1609	  },
1610	  "completed_at": "2026-05-15T16:40:14.867Z"
1611	}
1612	
1613	--------------------------------------------------------------------------------
1614	ID: v4-vanilla-recovery-eval
1615	--------------------------------------------------------------------------------
1616	{
1617	  "status": "DONE",
1618	  "retry_count": 0,
1619	  "created_at": "2026-05-14T19:30:18.314Z",
1620	  "updated_at": "2026-05-15T03:29:56.077Z",
1621	  "spec": {
1622	    "command": "CUDA_VISIBLE_DEVICES=0 python3 eval/injected_eval.py --model_path checkpoints/mini_vanilla_sft_v4/v0-20260514-201441/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --model_variant vanilla --num_episodes 47 --seed 42 --device cuda:0 --output eval_results/v4_vanilla_recovery_eval.json",
1623	    "server": "autodl-5090",
1624	    "model_name": "Qwen3-8B + LoRA (vanilla v4 seed=42)",
1625	    "checkpoint_source": "checkpoints/mini_vanilla_sft_v4/v0-20260514-201441/checkpoint-1635",
1626	    "eval_data": "47 ALFWorld tasks with error injection",
1627	    "seed": 42,
1628	    "parent": "mini-vanilla-sft-v4",
1629	    "checkpoint_path": "eval_results/v4_vanilla_recovery_eval.json",
1630	    "log_path": "eval_results/v4_vanilla_recovery_eval.json"
1631	  },
1632	  "hypothesis": "v4 Vanilla SFT seed=42 recovery eval (injected_eval.py) — 47 episodes with error injection, measuring detection/recovery/success rates under P1/P2/C1/C4 operators",
1633	  "conclusion": "success",
1634	  "metrics": {
1635	    "success_rate": 0.617,
1636	    "successes": 29,
1637	    "total": 47,
1638	    "recovery_rate": 0.617,
1639	    "detection_rate": 0,
1640	    "per_operator": {
1641	      "C1_context_truncation": {
1642	        "recovered": 9,
1643	        "total": 12,
1644	        "rate": 0.75
1645	      },
1646	      "C4_observation_masking": {
1647	        "recovered": 6,
1648	        "total": 11,
1649	        "rate": 0.545
1650	      },
1651	      "P1_step_order_swap": {
1652	        "recovered": 7,
1653	        "total": 12,
1654	        "rate": 0.583
1655	      },
1656	      "P2_sub_goal_deletion": {
1657	        "recovered": 7,
1658	        "total": 12,
1659	        "rate": 0.583
1660	      }
1661	    }
1662	  },
1663	  "completed_at": "2026-05-14T21:20:15.791Z"
1664	}
1665	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01BbmLXayvRWQ5YLrpnBLT8u",
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55",
  "uuid": "1b0f392d-f8c6-4ee7-b8d4-730bf8157688"
}
```

</details>

---

### System

_source line 51_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a1b20f795e02ae461",
  "tool_use_id": "toolu_01BbmLXayvRWQ5YLrpnBLT8u",
  "status": "completed",
  "output_file": "",
  "summary": "Extract llama31 registry data",
  "usage": {
    "total_tokens": 64159,
    "tool_uses": 12,
    "duration_ms": 153712
  },
  "uuid": "d4e2f4df-9129-45d0-b970-f054ad2f3ac2",
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55"
}
```

---

### Tool result

_source line 52 · 2026-05-16T14:56:14.370Z_

<details><summary>↩ Tool result · `toolu_01BbmLXayvRWQ5YLrpnBLT8u`</summary>

```text
Here is the complete extracted data:

---

## ALL LLAMA31 EXPERIMENTS (18 total)

### llama31-random-s0
- **Status:** DONE | **Conclusion:** success
- **Model:** Meta-Llama-3.1-8B-Instruct | **Seed:** 0
- **Data:** data/mini_pipeline_v4/sft_random_v4.jsonl (9031 samples)
- **Training Metrics:**
  - final_train_loss: 0.3368
  - epoch1_loss: 0.452, epoch2_loss: 0.238, epoch3_loss: 0.134
  - final_token_acc: 0.9357
  - train_steps: 3387, train_runtime_sec: 7622
  - peak_memory_gib: 30.74
- **Checkpoint:** /root/autodl-tmp/tax_error_inject_agent/output/llama31-random-s0/v0-20260516-171608/checkpoint-3387

### llama31-random-s0-eval
- **Status:** DONE | **Conclusion:** success
- **Eval type:** injected (47 ALFWorld episodes)
- **Metrics:**
  - recovery_rate: 0.745
  - detection_rate: 0.255
  - success_rate: 0.745
  - **By operator:**
    - C1_context_truncation: recovery=0.833, detection=0.083 (12 total, 10 recovered)
    - C4_observation_masking: recovery=0.727, detection=0.364 (11 total, 8 recovered)
    - P1_step_order_swap: recovery=0.667, detection=0.333 (12 total, 8 recovered)
    - P2_sub_goal_deletion: recovery=0.75, detection=0.25 (12 total, 9 recovered)

### llama31-random-s42
- **Status:** DONE | **Conclusion:** success
- **Model:** Meta-Llama-3.1-8B-Instruct | **Seed:** 42
- **Data:** sft_random_v4.jsonl (9029 samples)
- **Hypothesis:** Cross-model generalizability: LLaMA-3.1-8B Random condition control
- **Training Metrics:**
  - train_loss: 0.3366
  - token_acc: 0.9364
  - train_steps: 3387, train_duration_s: 7622
- **Checkpoint:** /root/autodl-tmp/tax_error_inject_agent/output/llama31-random-s42/v0-20260516-142300/checkpoint-3387

### llama31-random-s42-clean
- **Status:** DONE | **Conclusion:** success
- **Eval type:** clean (47 ALFWorld tasks, no injection)
- **Metrics:**
  - success_rate: 0.766
  - total_episodes: 47

### llama31-random-s42-eval
- **Status:** DONE | **Conclusion:** success
- **Hypothesis:** Cross-model: LLaMA Random s42 eval -- random injection control on LLaMA
- **Eval type:** injected (47 episodes)
- **Metrics:**
  - recovery_rate: 0.766, recovery_count: 36/47
  - detection_rate: 0.298
  - **By operator (recovery):**
    - C1_context_truncation: 0.667
    - C4_observation_masking: 0.727
    - P1_step_order_swap: 0.917
    - P2_sub_goal_deletion: 0.75
  - **By operator (detection):**
    - C1_detection: 0.417
    - C4_detection: 0.364
    - P1_detection: 0.333
    - P2_detection: 0.083

### llama31-taxei-s0
- **Status:** DONE | **Conclusion:** success
- **Model:** Meta-Llama-3.1-8B-Instruct | **Seed:** 0
- **Data:** sft_taxei_v4.jsonl (9029 samples)
- **Hypothesis:** Cross-model: LLaMA TaxEI s0 - 2nd seed for 3-seed cross-model validation
- **Training Metrics:**
  - final_train_loss: 0.32
  - final_token_acc: 0.88
  - train_steps: 3387
- **Checkpoint:** /root/autodl-tmp/tax_error_inject_agent/output/llama31-taxei-s0/v1-20260516-181826/checkpoint-3387

### llama31-taxei-s0-clean
- **Status:** DONE | **Conclusion:** success
- **Eval type:** clean (47 episodes)
- **Metrics:**
  - success_rate: 0.766
  - total_episodes: 47

### llama31-taxei-s0-eval
- **Status:** DONE | **Conclusion:** success
- **Hypothesis:** Cross-model: LLaMA TaxEI s0 injected eval -- does taxonomy injection help on LLaMA seed 0?
- **Eval type:** injected (47 episodes)
- **Metrics:**
  - recovery_rate: 0.745
  - success_rate: 0.745
  - total_episodes: 47

### llama31-taxei-s42
- **Status:** DONE | **Conclusion:** success
- **Model:** Meta-Llama-3.1-8B-Instruct | **Seed:** 42
- **Data:** sft_taxei_v4.jsonl (9029 samples)
- **Hypothesis:** Cross-model generalizability: LLaMA-3.1-8B TaxEI condition to verify Qwen3-8B findings transfer
- **Training Metrics:**
  - train_loss: 0.3366
  - token_acc: 0.9357
  - train_steps: 3387, train_duration_s: 7782
- **Checkpoint:** /root/autodl-tmp/tax_error_inject_agent/output/llama31-taxei-s42/v0-20260516-142258/checkpoint-3387

### llama31-taxei-s42-eval
- **Status:** DONE | **Conclusion:** success
- **Hypothesis:** Cross-model: LLaMA TaxEI s42 eval -- does taxonomy-guided injection help on LLaMA?
- **Eval type:** injected (47 episodes)
- **Metrics:**
  - recovery_rate: 0.745, recovery_count: 35/47
  - detection_rate: 0.298
  - **By operator (recovery):**
    - C1_context_truncation: 0.833
    - C4_observation_masking: 0.727
    - P1_step_order_swap: 0.583
    - P2_sub_goal_deletion: 0.833
  - **By operator (detection):**
    - C1_detection: 0.167
    - C4_detection: 0.364
    - P1_detection: 0.25
    - P2_detection: 0.417

### llama31-vanilla-s0
- **Status:** DONE | **Conclusion:** success
- **Model:** Meta-Llama-3.1-8B-Instruct | **Seed:** 0
- **Data:** sft_vanilla_v4.jsonl (4358 samples)
- **Training Metrics:**
  - final_train_loss: 0.398
  - epoch1_loss: 0.481, epoch2_loss: 0.362, epoch3_loss: 0.273
  - final_token_acc: 0.909
  - train_runtime_sec: 4158.6
- **Checkpoint:** /root/autodl-tmp/tax_error_inject_agent/output/llama31-vanilla-s0/v0-20260516-171603/checkpoint-1635

### llama31-vanilla-s0-clean
- **Status:** DONE | **Conclusion:** success
- **Eval type:** clean (47 episodes)
- **Metrics:**
  - success_rate: 0.723
  - total_episodes: 47

### llama31-vanilla-s0-eval
- **Status:** DONE | **Conclusion:** success
- **Hypothesis:** LLaMA-3.1-8B Vanilla s0 injected eval - cross-model validation seed 0
- **Eval type:** injected (47 episodes)
- **Metrics:**
  - recovery_rate: 0.745, recovery_count: 35/47
  - detection_rate: 0.277
  - **By operator:**
    - C1_context_truncation: recovery=0.667, detection=0.167
    - C4_observation_masking: recovery=0.727, detection=0.364
    - P1_step_order_swap: recovery=0.917, detection=0.333
    - P2_sub_goal_deletion: recovery=0.667, detection=0.25

### llama31-vanilla-s123
- **Status:** DONE | **Conclusion:** success
- **Model:** Meta-Llama-3.1-8B-Instruct | **Seed:** 123
- **Data:** sft_vanilla_v4.jsonl (4358 samples)
- **Hypothesis:** Cross-model: LLaMA Vanilla s123 - 3rd seed for 3-seed cross-model validation
- **Training Metrics:**
  - train_loss: 0.4, final_loss: 0.254
  - token_acc: 0.894
  - steps: 1635, epochs: 3, runtime_seconds: 4234
  - memory_gib: 29.85

### llama31-vanilla-s123-clean
- **Status:** DONE | **Conclusion:** success
- **Eval type:** clean (47 episodes)
- **Metrics:**
  - success_rate: 0.723
  - total_episodes: 47
  - **By task type:**
    - look_at_obj_in_light: 0.833
    - pick_and_place_simple: 0.625
    - pick_clean_then_place_in_recep: 0.545
    - pick_cool_then_place_in_recep: 0.571
    - pick_heat_then_place_in_recep: 1.0
    - pick_two_obj_and_place: 0.857

### llama31-vanilla-s42
- **Status:** DONE | **Conclusion:** success
- **Model:** Meta-Llama-3.1-8B-Instruct | **Seed:** 42
- **Data:** sft_vanilla_v4.jsonl (9029 samples)
- **Hypothesis:** Cross-model generalizability: LLaMA-3.1-8B Vanilla baseline
- **Training Metrics:**
  - train_loss: 0.40025
  - token_acc: 0.9067
  - train_steps: 1635, train_duration_s: 4157
- **Checkpoint:** /root/autodl-tmp/tax_error_inject_agent/output/llama31-vanilla-s42/v0-20260516-143227/checkpoint-1635

### llama31-vanilla-s42-clean
- **Status:** DONE | **Conclusion:** success
- **Eval type:** clean (47 episodes)
- **Metrics:**
  - success_rate: 0.723
  - total_episodes: 47

### llama31-vanilla-s42-eval
- **Status:** DONE | **Conclusion:** success
- **Hypothesis:** LLaMA-3.1-8B Vanilla s42 injected eval - cross-model baseline
- **Eval type:** injected (47 episodes)
- **Metrics:**
  - recovery_rate: 0.745, recovery_count: 35/47
  - detection_rate: 0.213
  - **By operator (recovery):**
    - C1_context_truncation: 0.75
    - C4_observation_masking: 0.727
    - P1_step_order_swap: 0.75
    - P2_sub_goal_deletion: 0.75

---

## QWEN3-8B EXPERIMENTS WITH EVAL METRICS (30 total)

### eval-rp-s0 (Qwen3-8B TaxEI-RP s0)
- recovery_rate: 0.468, detection_rate: 0, episodes: 47, recovered: 22

### eval-rp-s1 (Qwen3-8B TaxEI-RP s1)
- recovery_rate: 0.489, detection_rate: 0, episodes: 47, recovered: 23

### eval-rp-s123 (Qwen3-8B TaxEI-RP s123)
- recovery_rate: 0.574, detection_rate: 0, episodes: 47, recovered: 27

### eval-rp-s42 (Qwen3-8B TaxEI-RP s42)
- recovery_rate: 0.383, recovery_count: 18/47, detection_rate: 0
- C1: 0.5, C4: 0.273, P1: 0.5, P2: 0.25

### eval-rp-s7 (Qwen3-8B TaxEI-RP s7)
- recovery_rate: 0.596, recovery_count: 28/47, detection_rate: 0

### recovery-random-s1 (Qwen3-8B + mini_random_sft_v4_seed1)
- recovery_rate: 0.511, detection_rate: 0, total_episodes: 47

### recovery-random-s7 (Qwen3-8B + mini_random_sft_v4_seed7)
- recovery_rate: 0.532, detection_rate: 0, total_episodes: 47

### recovery-taxei-s1 (Qwen3-8B + TaxEI LoRA s1)
- recovery_rate: 0.617, recovery_count: 29/47, detection_rate: 0
- C1: 0.75, C4: 0.636, P1: 0.583, P2: 0.5

### recovery-taxei-s7 (Qwen3-8B + TaxEI s7 LoRA)
- recovery_rate: 0.574, detection_rate: 0, total_episodes: 47

### recovery-vanilla-s1 (Qwen3-8B + Vanilla LoRA s1)
- recovery_rate: 0.66, recovery_count: 31/47, detection_rate: 0
- C1: 0.667, C4: 0.545, P1: 0.667, P2: 0.75

### recovery-vanilla-s7 (Qwen3-8B + Vanilla LoRA s7)
- recovery_rate: 0.745, recovery_count: 35/47, detection_rate: 0
- C1: 0.75, C4: 0.727, P1: 0.75, P2: 0.75

### v4-random-fixed-inject10-s0-eval-r3 (Qwen3-8B, random 10% inject, s0)
- success_rate: 0.66 (31/47, clean eval)

### v4-random-fixed-inject10-s1-eval (Qwen3-8B, random 10% inject, s1)
- success_rate: 0.681 (32/47, clean eval)

### v4-random-fixed-inject10-s123-eval (Qwen3-8B, random 10% inject, s123)
- success_rate: 0.553 (26/47, clean eval)

### v4-random-fixed-inject10-s7-eval (Qwen3-8B, random 10% inject, s7)
- success_rate: 0.617 (29/47, clean eval)

### v4-random-fixed-inject50-s1-eval (Qwen3-8B, random 50% inject, s1)
- success_rate: 0.702 (33/47, clean eval)

### v4-random-fixed-inject50-s7-eval (Qwen3-8B, random 50% inject, s7)
- success_rate: 0.468 (22/47, clean eval)

### v4-random-recovery-eval (Qwen3-8B + random SFT v4, s42, injected)
- recovery_rate: 0.638, detection_rate: 0, successes: 30/47

### v4-random-recovery-eval-s0 (Qwen3-8B + Random LoRA s0, injected)
- recovery_rate: 0.553, detection_rate: 0, total_episodes: 47
- C1: 0.583 (7/12), C4: 0.545 (6/11), P1: 0.583 (7/12), P2: 0.5 (6/12)

### v4-random-recovery-eval-s123 (Qwen3-8B + Random LoRA s123, injected)
- recovery_rate: 0.66, detection_rate: 0, total_episodes: 47
- C1: 0.75 (9/12), P2: 0.75 (9/12), P1: 0.583 (7/12), C4: 0.545 (6/11)

### v4-random-seed7-eval (Qwen3-8B + random SFT seed=7, clean)
- success_rate: 0.553 (26/47)

### v4-taxei-fixed-inject10-s1-eval-r2 (Qwen3-8B, taxei 10% inject, s1)
- success_rate: 0.511 (24/47, clean eval)

### v4-taxei-fixed-inject10-s123-eval-r3 (Qwen3-8B, taxei 10% inject, s123)
- success_rate: 0.553 (26/47, clean eval)

### v4-taxei-fixed-inject10-s7-eval (Qwen3-8B, taxei 10% inject, s7)
- success_rate: 0.681 (32/47, clean eval)

### v4-taxei-fixed-inject50-s1-eval (Qwen3-8B, taxei 50% inject, s1)
- success_rate: 0.638 (30/47, clean eval)

### v4-taxei-fixed-inject50-s7-eval (Qwen3-8B, taxei 50% inject, s7)
- success_rate: 0.553 (26/47, clean eval)

### v4-taxei-recovery-eval (Qwen3-8B + TaxEI LoRA v4, s42, injected)
- **Conclusion: negative**
- recovery_rate: 0.596, detection_rate: 0, successes: 28/47

### v4-taxei-recovery-eval-r2 (Qwen3-8B + TaxEI LoRA v4, s42, injected retry)
- recovery_rate: 0.596, detection_rate: 0, total_episodes: 47
- C1: 0.667 (8/12), C4: 0.636 (7/11), P1: 0.583 (7/12), P2: 0.5 (6/12)

### v4-taxei-seed7-eval (Qwen3-8B + TaxEI v4 seed=7, clean)
- success_rate: 0.617 (29/47)

### v4-vanilla-recovery-eval (Qwen3-8B + Vanilla v4, s42, injected)
- recovery_rate: 0.617, detection_rate: 0, successes: 29/47
- C1: 0.75 (9/12), C4: 0.545 (6/11), P1: 0.583 (7/12), P2: 0.583 (7/12)

---

## Key Comparative Observations

**LLaMA-3.1-8B (llama31) injected eval recovery rates:**
| Condition | s0 | s42 | Mean |
|-----------|-----|------|------|
| Vanilla | 0.745 | 0.745 | 0.745 |
| TaxEI | 0.745 | 0.745 | 0.745 |
| Random | 0.745 | 0.766 | 0.756 |

**LLaMA-3.1-8B detection rates:**
| Condition | s0 | s42 |
|-----------|-----|------|
| Vanilla | 0.277 | 0.213 |
| TaxEI | -- | 0.298 |
| Random | 0.255 | 0.298 |

**LLaMA-3.1-8B clean eval success rates:**
| Condition | s0 | s42 | s123 |
|-----------|-----|------|------|
| Vanilla | 0.723 | 0.723 | 0.723 |
| TaxEI | 0.766 | -- | -- |
| Random | -- | 0.766 | -- |

**Qwen3-8B injected eval recovery rates (for comparison):**
| Condition | s42 | s0 | s1 | s7 | s123 |
|-----------|------|-----|-----|-----|------|
| Vanilla | 0.617 | -- | 0.66 | 0.745 | -- |
| TaxEI | 0.596 | -- | 0.617 | 0.574 | -- |
| Random | 0.638 | 0.553 | 0.511 | 0.532 | 0.66 |
| TaxEI-RP | 0.383 | 0.468 | 0.489 | 0.596 | 0.574 |

Notable: LLaMA-3.1-8B shows uniformly high recovery (~0.745) across all conditions with non-zero detection rates (0.21-0.30), while Qwen3-8B shows more variance (0.38-0.75) with zero detection rate in most cases. The LLaMA results suggest the larger/newer model already has strong inherent resilience, making condition differences less distinguishable.

agentId: a1b20f795e02ae461 (use SendMessage with to: 'a1b20f795e02ae461' to continue this agent)
&lt;usage>total_tokens: 69349
tool_uses: 12
duration_ms: 153714&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55",
  "uuid": "e92fbbbe-60fb-48c4-97c2-1616f39af084",
  "tool_use_result": {
    "status": "completed",
    "prompt": "I need to extract all experiments with IDs starting with \"llama31\" from a large JSON file. The file is at:\n/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/ae491a69-2268-4f52-bbd5-112d75ec9c55/tool-results/mcp-agent-ml-research-read_registry-1778943212143.txt\n\nThe file has schema: {result: string} where result is a JSON string containing experiment data.\n\nI need ALL experiments whose ID starts with \"llama31\" — extract their full details including: status, metrics, spec (seed, model, data_path), hypothesis, conclusion, and any eval results.\n\nAlso extract any experiments with \"qwen\" in the ID that have metrics/eval data for comparison.\n\nUse jq or python to parse. Report the extracted data verbatim — I need exact numbers.",
    "agentId": "a1b20f795e02ae461",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is the complete extracted data:\n\n---\n\n## ALL LLAMA31 EXPERIMENTS (18 total)\n\n### llama31-random-s0\n- **Status:** DONE | **Conclusion:** success\n- **Model:** Meta-Llama-3.1-8B-Instruct | **Seed:** 0\n- **Data:** data/mini_pipeline_v4/sft_random_v4.jsonl (9031 samples)\n- **Training Metrics:**\n  - final_train_loss: 0.3368\n  - epoch1_loss: 0.452, epoch2_loss: 0.238, epoch3_loss: 0.134\n  - final_token_acc: 0.9357\n  - train_steps: 3387, train_runtime_sec: 7622\n  - peak_memory_gib: 30.74\n- **Checkpoint:** /root/autodl-tmp/tax_error_inject_agent/output/llama31-random-s0/v0-20260516-171608/checkpoint-3387\n\n### llama31-random-s0-eval\n- **Status:** DONE | **Conclusion:** success\n- **Eval type:** injected (47 ALFWorld episodes)\n- **Metrics:**\n  - recovery_rate: 0.745\n  - detection_rate: 0.255\n  - success_rate: 0.745\n  - **By operator:**\n    - C1_context_truncation: recovery=0.833, detection=0.083 (12 total, 10 recovered)\n    - C4_observation_masking: recovery=0.727, detection=0.364 (11 total, 8 recovered)\n    - P1_step_order_swap: recovery=0.667, detection=0.333 (12 total, 8 recovered)\n    - P2_sub_goal_deletion: recovery=0.75, detection=0.25 (12 total, 9 recovered)\n\n### llama31-random-s42\n- **Status:** DONE | **Conclusion:** success\n- **Model:** Meta-Llama-3.1-8B-Instruct | **Seed:** 42\n- **Data:** sft_random_v4.jsonl (9029 samples)\n- **Hypothesis:** Cross-model generalizability: LLaMA-3.1-8B Random condition control\n- **Training Metrics:**\n  - train_loss: 0.3366\n  - token_acc: 0.9364\n  - train_steps: 3387, train_duration_s: 7622\n- **Checkpoint:** /root/autodl-tmp/tax_error_inject_agent/output/llama31-random-s42/v0-20260516-142300/checkpoint-3387\n\n### llama31-random-s42-clean\n- **Status:** DONE | **Conclusion:** success\n- **Eval type:** clean (47 ALFWorld tasks, no injection)\n- **Metrics:**\n  - success_rate: 0.766\n  - total_episodes: 47\n\n### llama31-random-s42-eval\n- **Status:** DONE | **Conclusion:** success\n- **Hypothesis:** Cross-model: LLaMA Random s42 eval -- random injection control on LLaMA\n- **Eval type:** injected (47 episodes)\n- **Metrics:**\n  - recovery_rate: 0.766, recovery_count: 36/47\n  - detection_rate: 0.298\n  - **By operator (recovery):**\n    - C1_context_truncation: 0.667\n    - C4_observation_masking: 0.727\n    - P1_step_order_swap: 0.917\n    - P2_sub_goal_deletion: 0.75\n  - **By operator (detection):**\n    - C1_detection: 0.417\n    - C4_detection: 0.364\n    - P1_detection: 0.333\n    - P2_detection: 0.083\n\n### llama31-taxei-s0\n- **Status:** DONE | **Conclusion:** success\n- **Model:** Meta-Llama-3.1-8B-Instruct | **Seed:** 0\n- **Data:** sft_taxei_v4.jsonl (9029 samples)\n- **Hypothesis:** Cross-model: LLaMA TaxEI s0 - 2nd seed for 3-seed cross-model validation\n- **Training Metrics:**\n  - final_train_loss: 0.32\n  - final_token_acc: 0.88\n  - train_steps: 3387\n- **Checkpoint:** /root/autodl-tmp/tax_error_inject_agent/output/llama31-taxei-s0/v1-20260516-181826/checkpoint-3387\n\n### llama31-taxei-s0-clean\n- **Status:** DONE | **Conclusion:** success\n- **Eval type:** clean (47 episodes)\n- **Metrics:**\n  - success_rate: 0.766\n  - total_episodes: 47\n\n### llama31-taxei-s0-eval\n- **Status:** DONE | **Conclusion:** success\n- **Hypothesis:** Cross-model: LLaMA TaxEI s0 injected eval -- does taxonomy injection help on LLaMA seed 0?\n- **Eval type:** injected (47 episodes)\n- **Metrics:**\n  - recovery_rate: 0.745\n  - success_rate: 0.745\n  - total_episodes: 47\n\n### llama31-taxei-s42\n- **Status:** DONE | **Conclusion:** success\n- **Model:** Meta-Llama-3.1-8B-Instruct | **Seed:** 42\n- **Data:** sft_taxei_v4.jsonl (9029 samples)\n- **Hypothesis:** Cross-model generalizability: LLaMA-3.1-8B TaxEI condition to verify Qwen3-8B findings transfer\n- **Training Metrics:**\n  - train_loss: 0.3366\n  - token_acc: 0.9357\n  - train_steps: 3387, train_duration_s: 7782\n- **Checkpoint:** /root/autodl-tmp/tax_error_inject_agent/output/llama31-taxei-s42/v0-20260516-142258/checkpoint-3387\n\n### llama31-taxei-s42-eval\n- **Status:** DONE | **Conclusion:** success\n- **Hypothesis:** Cross-model: LLaMA TaxEI s42 eval -- does taxonomy-guided injection help on LLaMA?\n- **Eval type:** injected (47 episodes)\n- **Metrics:**\n  - recovery_rate: 0.745, recovery_count: 35/47\n  - detection_rate: 0.298\n  - **By operator (recovery):**\n    - C1_context_truncation: 0.833\n    - C4_observation_masking: 0.727\n    - P1_step_order_swap: 0.583\n    - P2_sub_goal_deletion: 0.833\n  - **By operator (detection):**\n    - C1_detection: 0.167\n    - C4_detection: 0.364\n    - P1_detection: 0.25\n    - P2_detection: 0.417\n\n### llama31-vanilla-s0\n- **Status:** DONE | **Conclusion:** success\n- **Model:** Meta-Llama-3.1-8B-Instruct | **Seed:** 0\n- **Data:** sft_vanilla_v4.jsonl (4358 samples)\n- **Training Metrics:**\n  - final_train_loss: 0.398\n  - epoch1_loss: 0.481, epoch2_loss: 0.362, epoch3_loss: 0.273\n  - final_token_acc: 0.909\n  - train_runtime_sec: 4158.6\n- **Checkpoint:** /root/autodl-tmp/tax_error_inject_agent/output/llama31-vanilla-s0/v0-20260516-171603/checkpoint-1635\n\n### llama31-vanilla-s0-clean\n- **Status:** DONE | **Conclusion:** success\n- **Eval type:** clean (47 episodes)\n- **Metrics:**\n  - success_rate: 0.723\n  - total_episodes: 47\n\n### llama31-vanilla-s0-eval\n- **Status:** DONE | **Conclusion:** success\n- **Hypothesis:** LLaMA-3.1-8B Vanilla s0 injected eval - cross-model validation seed 0\n- **Eval type:** injected (47 episodes)\n- **Metrics:**\n  - recovery_rate: 0.745, recovery_count: 35/47\n  - detection_rate: 0.277\n  - **By operator:**\n    - C1_context_truncation: recovery=0.667, detection=0.167\n    - C4_observation_masking: recovery=0.727, detection=0.364\n    - P1_step_order_swap: recovery=0.917, detection=0.333\n    - P2_sub_goal_deletion: recovery=0.667, detection=0.25\n\n### llama31-vanilla-s123\n- **Status:** DONE | **Conclusion:** success\n- **Model:** Meta-Llama-3.1-8B-Instruct | **Seed:** 123\n- **Data:** sft_vanilla_v4.jsonl (4358 samples)\n- **Hypothesis:** Cross-model: LLaMA Vanilla s123 - 3rd seed for 3-seed cross-model validation\n- **Training Metrics:**\n  - train_loss: 0.4, final_loss: 0.254\n  - token_acc: 0.894\n  - steps: 1635, epochs: 3, runtime_seconds: 4234\n  - memory_gib: 29.85\n\n### llama31-vanilla-s123-clean\n- **Status:** DONE | **Conclusion:** success\n- **Eval type:** clean (47 episodes)\n- **Metrics:**\n  - success_rate: 0.723\n  - total_episodes: 47\n  - **By task type:**\n    - look_at_obj_in_light: 0.833\n    - pick_and_place_simple: 0.625\n    - pick_clean_then_place_in_recep: 0.545\n    - pick_cool_then_place_in_recep: 0.571\n    - pick_heat_then_place_in_recep: 1.0\n    - pick_two_obj_and_place: 0.857\n\n### llama31-vanilla-s42\n- **Status:** DONE | **Conclusion:** success\n- **Model:** Meta-Llama-3.1-8B-Instruct | **Seed:** 42\n- **Data:** sft_vanilla_v4.jsonl (9029 samples)\n- **Hypothesis:** Cross-model generalizability: LLaMA-3.1-8B Vanilla baseline\n- **Training Metrics:**\n  - train_loss: 0.40025\n  - token_acc: 0.9067\n  - train_steps: 1635, train_duration_s: 4157\n- **Checkpoint:** /root/autodl-tmp/tax_error_inject_agent/output/llama31-vanilla-s42/v0-20260516-143227/checkpoint-1635\n\n### llama31-vanilla-s42-clean\n- **Status:** DONE | **Conclusion:** success\n- **Eval type:** clean (47 episodes)\n- **Metrics:**\n  - success_rate: 0.723\n  - total_episodes: 47\n\n### llama31-vanilla-s42-eval\n- **Status:** DONE | **Conclusion:** success\n- **Hypothesis:** LLaMA-3.1-8B Vanilla s42 injected eval - cross-model baseline\n- **Eval type:** injected (47 episodes)\n- **Metrics:**\n  - recovery_rate: 0.745, recovery_count: 35/47\n  - detection_rate: 0.213\n  - **By operator (recovery):**\n    - C1_context_truncation: 0.75\n    - C4_observation_masking: 0.727\n    - P1_step_order_swap: 0.75\n    - P2_sub_goal_deletion: 0.75\n\n---\n\n## QWEN3-8B EXPERIMENTS WITH EVAL METRICS (30 total)\n\n### eval-rp-s0 (Qwen3-8B TaxEI-RP s0)\n- recovery_rate: 0.468, detection_rate: 0, episodes: 47, recovered: 22\n\n### eval-rp-s1 (Qwen3-8B TaxEI-RP s1)\n- recovery_rate: 0.489, detection_rate: 0, episodes: 47, recovered: 23\n\n### eval-rp-s123 (Qwen3-8B TaxEI-RP s123)\n- recovery_rate: 0.574, detection_rate: 0, episodes: 47, recovered: 27\n\n### eval-rp-s42 (Qwen3-8B TaxEI-RP s42)\n- recovery_rate: 0.383, recovery_count: 18/47, detection_rate: 0\n- C1: 0.5, C4: 0.273, P1: 0.5, P2: 0.25\n\n### eval-rp-s7 (Qwen3-8B TaxEI-RP s7)\n- recovery_rate: 0.596, recovery_count: 28/47, detection_rate: 0\n\n### recovery-random-s1 (Qwen3-8B + mini_random_sft_v4_seed1)\n- recovery_rate: 0.511, detection_rate: 0, total_episodes: 47\n\n### recovery-random-s7 (Qwen3-8B + mini_random_sft_v4_seed7)\n- recovery_rate: 0.532, detection_rate: 0, total_episodes: 47\n\n### recovery-taxei-s1 (Qwen3-8B + TaxEI LoRA s1)\n- recovery_rate: 0.617, recovery_count: 29/47, detection_rate: 0\n- C1: 0.75, C4: 0.636, P1: 0.583, P2: 0.5\n\n### recovery-taxei-s7 (Qwen3-8B + TaxEI s7 LoRA)\n- recovery_rate: 0.574, detection_rate: 0, total_episodes: 47\n\n### recovery-vanilla-s1 (Qwen3-8B + Vanilla LoRA s1)\n- recovery_rate: 0.66, recovery_count: 31/47, detection_rate: 0\n- C1: 0.667, C4: 0.545, P1: 0.667, P2: 0.75\n\n### recovery-vanilla-s7 (Qwen3-8B + Vanilla LoRA s7)\n- recovery_rate: 0.745, recovery_count: 35/47, detection_rate: 0\n- C1: 0.75, C4: 0.727, P1: 0.75, P2: 0.75\n\n### v4-random-fixed-inject10-s0-eval-r3 (Qwen3-8B, random 10% inject, s0)\n- success_rate: 0.66 (31/47, clean eval)\n\n### v4-random-fixed-inject10-s1-eval (Qwen3-8B, random 10% inject, s1)\n- success_rate: 0.681 (32/47, clean eval)\n\n### v4-random-fixed-inject10-s123-eval (Qwen3-8B, random 10% inject, s123)\n- success_rate: 0.553 (26/47, clean eval)\n\n### v4-random-fixed-inject10-s7-eval (Qwen3-8B, random 10% inject, s7)\n- success_rate: 0.617 (29/47, clean eval)\n\n### v4-random-fixed-inject50-s1-eval (Qwen3-8B, random 50% inject, s1)\n- success_rate: 0.702 (33/47, clean eval)\n\n### v4-random-fixed-inject50-s7-eval (Qwen3-8B, random 50% inject, s7)\n- success_rate: 0.468 (22/47, clean eval)\n\n### v4-random-recovery-eval (Qwen3-8B + random SFT v4, s42, injected)\n- recovery_rate: 0.638, detection_rate: 0, successes: 30/47\n\n### v4-random-recovery-eval-s0 (Qwen3-8B + Random LoRA s0, injected)\n- recovery_rate: 0.553, detection_rate: 0, total_episodes: 47\n- C1: 0.583 (7/12), C4: 0.545 (6/11), P1: 0.583 (7/12), P2: 0.5 (6/12)\n\n### v4-random-recovery-eval-s123 (Qwen3-8B + Random LoRA s123, injected)\n- recovery_rate: 0.66, detection_rate: 0, total_episodes: 47\n- C1: 0.75 (9/12), P2: 0.75 (9/12), P1: 0.583 (7/12), C4: 0.545 (6/11)\n\n### v4-random-seed7-eval (Qwen3-8B + random SFT seed=7, clean)\n- success_rate: 0.553 (26/47)\n\n### v4-taxei-fixed-inject10-s1-eval-r2 (Qwen3-8B, taxei 10% inject, s1)\n- success_rate: 0.511 (24/47, clean eval)\n\n### v4-taxei-fixed-inject10-s123-eval-r3 (Qwen3-8B, taxei 10% inject, s123)\n- success_rate: 0.553 (26/47, clean eval)\n\n### v4-taxei-fixed-inject10-s7-eval (Qwen3-8B, taxei 10% inject, s7)\n- success_rate: 0.681 (32/47, clean eval)\n\n### v4-taxei-fixed-inject50-s1-eval (Qwen3-8B, taxei 50% inject, s1)\n- success_rate: 0.638 (30/47, clean eval)\n\n### v4-taxei-fixed-inject50-s7-eval (Qwen3-8B, taxei 50% inject, s7)\n- success_rate: 0.553 (26/47, clean eval)\n\n### v4-taxei-recovery-eval (Qwen3-8B + TaxEI LoRA v4, s42, injected)\n- **Conclusion: negative**\n- recovery_rate: 0.596, detection_rate: 0, successes: 28/47\n\n### v4-taxei-recovery-eval-r2 (Qwen3-8B + TaxEI LoRA v4, s42, injected retry)\n- recovery_rate: 0.596, detection_rate: 0, total_episodes: 47\n- C1: 0.667 (8/12), C4: 0.636 (7/11), P1: 0.583 (7/12), P2: 0.5 (6/12)\n\n### v4-taxei-seed7-eval (Qwen3-8B + TaxEI v4 seed=7, clean)\n- success_rate: 0.617 (29/47)\n\n### v4-vanilla-recovery-eval (Qwen3-8B + Vanilla v4, s42, injected)\n- recovery_rate: 0.617, detection_rate: 0, successes: 29/47\n- C1: 0.75 (9/12), C4: 0.545 (6/11), P1: 0.583 (7/12), P2: 0.583 (7/12)\n\n---\n\n## Key Comparative Observations\n\n**LLaMA-3.1-8B (llama31) injected eval recovery rates:**\n| Condition | s0 | s42 | Mean |\n|-----------|-----|------|------|\n| Vanilla | 0.745 | 0.745 | 0.745 |\n| TaxEI | 0.745 | 0.745 | 0.745 |\n| Random | 0.745 | 0.766 | 0.756 |\n\n**LLaMA-3.1-8B detection rates:**\n| Condition | s0 | s42 |\n|-----------|-----|------|\n| Vanilla | 0.277 | 0.213 |\n| TaxEI | -- | 0.298 |\n| Random | 0.255 | 0.298 |\n\n**LLaMA-3.1-8B clean eval success rates:**\n| Condition | s0 | s42 | s123 |\n|-----------|-----|------|------|\n| Vanilla | 0.723 | 0.723 | 0.723 |\n| TaxEI | 0.766 | -- | -- |\n| Random | -- | 0.766 | -- |\n\n**Qwen3-8B injected eval recovery rates (for comparison):**\n| Condition | s42 | s0 | s1 | s7 | s123 |\n|-----------|------|-----|-----|-----|------|\n| Vanilla | 0.617 | -- | 0.66 | 0.745 | -- |\n| TaxEI | 0.596 | -- | 0.617 | 0.574 | -- |\n| Random | 0.638 | 0.553 | 0.511 | 0.532 | 0.66 |\n| TaxEI-RP | 0.383 | 0.468 | 0.489 | 0.596 | 0.574 |\n\nNotable: LLaMA-3.1-8B shows uniformly high recovery (~0.745) across all conditions with non-zero detection rates (0.21-0.30), while Qwen3-8B shows more variance (0.38-0.75) with zero detection rate in most cases. The LLaMA results suggest the larger/newer model already has strong inherent resilience, making condition differences less distinguishable."
      }
    ],
    "totalDurationMs": 153714,
    "totalTokens": 69349,
    "totalToolUseCount": 12,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1278,
      "cache_read_input_tokens": 62366,
      "output_tokens": 5704,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1278
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5704,
          "cache_read_input_tokens": 62366,
          "cache_creation_input_tokens": 1278,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1278,
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
      "bashCount": 6,
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

_source line 53_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data I need. Let me also check if there's a llama31-taxei-s42-clean eval or llama31-random-s0-clean eval in the data. Looking at what was extracted:

LLaMA experiments found:
- llama31-vanilla-s42: train done, eval done (injected), clean done
- llama31-vanilla-s0: train done, eval done (injected), clean done
- llama31-vanilla-s123: train done, clean done (no injected eval yet? Let me check... no injected eval mentioned)


- llama31-taxei-s42: train done, eval done (injected), no clean mentioned
- llama31-taxei-s0: train done, eval done (injected), clean done
- llama31-taxei-s123: currently running
- llama31-random-s42: train done, eval done (injected), clean done
- llama31-random-s0: train done, eval done (injected), no clean mentioned
- llama31-random-s123: currently running

Now let me look more carefully at the actual training metrics to see what values I'm working with.

Looking at the training loss and token accuracy across all the models, the taxei and random variants are performing better than vanilla across the board. The taxei-s42 and random-s42 are showing particularly strong token accuracy around 0.936, while vanilla models are hovering around 0.89-0.91. The injected eval metrics show recovery rates around 0.745 for the vanilla models, and I need to see the full picture for the other variants. I'm noticing some gaps in the clean eval results—specifically missing entries for llama31-taxei-s42-clean and llama31-random-s0-clean. Let me cross-reference what was actually extracted to see which evaluations are still unaccounted for.

Looking at the vanilla-s123 experiments, the training and clean eval are both marked as done, but there's no injected eval listed yet, so that one appears to still be pending. The task notes mention that s123 for taxei and random are still training, so those would explain why their evals aren't complete.

Now I'm compiling the results into summary tables with the loss metrics across all seeds and methods. Looking at the clean eval results more carefully, I see vanilla completed across all seeds, TaxEI only has s0, and Random only has s42 — the missing ones for TaxEI and Random are probably still waiting for their evaluations to finish since only the s123 variants are currently running.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55",
  "uuid": "7545e5a7-2661-4e8e-bc25-4ddbd0269c41",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Paogrk2MJPXhfjydwQibq9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6103,
      "cache_read_input_tokens": 26802,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6103
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

_source line 54_

I have all the data. Now I'll compile the summary and write the artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55",
  "uuid": "1871a677-1c55-45ed-87f8-5765cd375181",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Paogrk2MJPXhfjydwQibq9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6103,
      "cache_read_input_tokens": 26802,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6103
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

_source line 55_

<details open><summary>🔧 Tool call — Write · `toolu_01KkzLZpxiN8Zc9YkNNj9sFC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/llama_crossmodel_summary.md",
  "content": "# LLaMA-3.1-8B Cross-Model Validation Summary\n\n**Date:** 2026-05-16  \n**Purpose:** Validate Qwen3-8B negative result (TaxEI ≈ Random) on a second model architecture.\n\n---\n\n## 1. Training Metrics\n\n| Seed | Vanilla loss | TaxEI loss | Random loss |\n|------|-------------|------------|-------------|\n| s42  | 0.400 | 0.337 | 0.337 |\n| s0   | 0.398 | 0.320 | 0.337 |\n| s123 | 0.400 | (running) | (running) |\n\nNotes:\n- Vanilla trains on 4358 samples (clean only), TaxEI/Random on 9029 samples (clean + injected)\n- Loss difference reflects data composition, not model quality\n- Token accuracy: Vanilla ~0.90, TaxEI/Random ~0.93\n\n---\n\n## 2. Injected Eval — Recovery Rate (47 episodes, 4 error operators)\n\n| Seed | Vanilla | TaxEI | Random |\n|------|---------|-------|--------|\n| s42  | 74.5% | 74.5% | 76.6% |\n| s0   | 74.5% | 74.5% | 74.5% |\n| s123 | (pending) | (pending) | (pending) |\n| **Mean (s0+s42)** | **74.5%** | **74.5%** | **75.5%** |\n\nDetection rates (non-zero, unlike Qwen3-8B):\n| Seed | Vanilla | TaxEI | Random |\n|------|---------|-------|--------|\n| s42  | 21.3% | 29.8% | 29.8% |\n| s0   | 27.7% | — | 25.5% |\n\n---\n\n## 3. Clean Eval — Success Rate (47 episodes, no injection)\n\n| Seed | Vanilla | TaxEI | Random |\n|------|---------|-------|--------|\n| s42  | 72.3% | (not run) | 76.6% |\n| s0   | 72.3% | 76.6% | (not run) |\n| s123 | 72.3% | (pending) | (pending) |\n| **Mean** | **72.3%** | **76.6%** | **76.6%** |\n\n---\n\n## 4. Per-Operator Recovery Breakdown (Injected Eval)\n\n### s42\n| Operator | Vanilla | TaxEI | Random |\n|----------|---------|-------|--------|\n| C1_context_truncation | 75.0% | 83.3% | 66.7% |\n| C4_observation_masking | 72.7% | 72.7% | 72.7% |\n| P1_step_order_swap | 75.0% | 58.3% | 91.7% |\n| P2_sub_goal_deletion | 75.0% | 83.3% | 75.0% |\n\n### s0\n| Operator | Vanilla | TaxEI | Random |\n|----------|---------|-------|--------|\n| C1_context_truncation | 66.7% | — | 83.3% |\n| C4_observation_masking | 72.7% | — | 72.7% |\n| P1_step_order_swap | 91.7% | — | 66.7% |\n| P2_sub_goal_deletion | 66.7% | — | 75.0% |\n\n---\n\n## 5. LLaMA vs Qwen3-8B Comparison\n\n### Key Metrics Side-by-Side\n\n| Metric | Qwen3-8B (5-seed) | LLaMA-3.1-8B (2-seed) |\n|--------|-------------------|------------------------|\n| **Vanilla recovery** | 67.3 ± 4.7% | 74.5 ± 0.0% |\n| **TaxEI recovery** | 58.3 ± 6.5% | 74.5 ± 0.0% |\n| **Random recovery** | 58.3 ± 8.7% | 75.5 ± 1.1% |\n| **Injection penalty** | ~9pp (67.3→58.3) | **None** (74.5→74.5) |\n| **Detection rate** | 0% (all seeds) | 21-30% |\n| **Clean success (Vanilla)** | ~65% | 72.3% |\n\n### Critical Findings\n\n1. **No injection penalty on LLaMA:** All three conditions achieve ~74.5% recovery — injection training neither helps nor hurts. On Qwen3-8B, injection training *reduced* performance by ~9pp.\n\n2. **All conditions converge:** LLaMA shows near-zero variance across conditions (74.5% vs 74.5% vs 76.6%), suggesting the model's baseline capability dominates over training signal differences.\n\n3. **Non-zero detection on LLaMA:** LLaMA detects errors 21-30% of the time (Qwen3-8B: 0%), indicating stronger intrinsic error awareness regardless of training condition.\n\n4. **Higher absolute performance:** LLaMA outperforms Qwen3-8B across the board (+7-16pp recovery, +7pp clean success), consistent with it being a stronger instruction-following model.\n\n5. **Strengthens negative result:** The cross-model validation confirms TaxEI provides no advantage — but for a *different reason* than Qwen3-8B:\n   - Qwen3-8B: TaxEI = Random (both hurt vs Vanilla)\n   - LLaMA: TaxEI = Random = Vanilla (nothing helps because baseline is already strong)\n\n---\n\n## 6. Pending Experiments\n\n| Experiment | Status | ETA |\n|-----------|--------|-----|\n| llama31-taxei-s123 | Training | ~2h |\n| llama31-random-s123 | Training | ~2h |\n| llama31-vanilla-s123-eval (injected) | Not submitted | After training completes |\n| llama31-taxei-s42-clean | Not submitted | — |\n| llama31-random-s0-clean | Not submitted | — |\n\n---\n\n## 7. Implications for Paper\n\nThe LLaMA cross-model validation provides a **second mechanism** supporting the negative result:\n- **Qwen3-8B story:** TaxEI doesn't outperform Random injection (both degrade vs Vanilla)\n- **LLaMA story:** Model already resilient — no injection method adds value when baseline is strong\n\nTogether these argue that taxonomy-guided error injection is not a robust training strategy: it fails to help weak models (Qwen) and is unnecessary for strong ones (LLaMA).\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55",
  "uuid": "2de87046-f680-4cd0-95b2-329e75245121",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Paogrk2MJPXhfjydwQibq9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6103,
      "cache_read_input_tokens": 26802,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6103
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

_source line 56 · 2026-05-16T14:57:16.389Z_

<details><summary>↩ Tool result · `toolu_01KkzLZpxiN8Zc9YkNNj9sFC`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/llama_crossmodel_summary.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55",
  "uuid": "3f6195f0-e94f-425c-9e71-ae8369e01ee6",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/llama_crossmodel_summary.md",
    "content": "# LLaMA-3.1-8B Cross-Model Validation Summary\n\n**Date:** 2026-05-16  \n**Purpose:** Validate Qwen3-8B negative result (TaxEI ≈ Random) on a second model architecture.\n\n---\n\n## 1. Training Metrics\n\n| Seed | Vanilla loss | TaxEI loss | Random loss |\n|------|-------------|------------|-------------|\n| s42  | 0.400 | 0.337 | 0.337 |\n| s0   | 0.398 | 0.320 | 0.337 |\n| s123 | 0.400 | (running) | (running) |\n\nNotes:\n- Vanilla trains on 4358 samples (clean only), TaxEI/Random on 9029 samples (clean + injected)\n- Loss difference reflects data composition, not model quality\n- Token accuracy: Vanilla ~0.90, TaxEI/Random ~0.93\n\n---\n\n## 2. Injected Eval — Recovery Rate (47 episodes, 4 error operators)\n\n| Seed | Vanilla | TaxEI | Random |\n|------|---------|-------|--------|\n| s42  | 74.5% | 74.5% | 76.6% |\n| s0   | 74.5% | 74.5% | 74.5% |\n| s123 | (pending) | (pending) | (pending) |\n| **Mean (s0+s42)** | **74.5%** | **74.5%** | **75.5%** |\n\nDetection rates (non-zero, unlike Qwen3-8B):\n| Seed | Vanilla | TaxEI | Random |\n|------|---------|-------|--------|\n| s42  | 21.3% | 29.8% | 29.8% |\n| s0   | 27.7% | — | 25.5% |\n\n---\n\n## 3. Clean Eval — Success Rate (47 episodes, no injection)\n\n| Seed | Vanilla | TaxEI | Random |\n|------|---------|-------|--------|\n| s42  | 72.3% | (not run) | 76.6% |\n| s0   | 72.3% | 76.6% | (not run) |\n| s123 | 72.3% | (pending) | (pending) |\n| **Mean** | **72.3%** | **76.6%** | **76.6%** |\n\n---\n\n## 4. Per-Operator Recovery Breakdown (Injected Eval)\n\n### s42\n| Operator | Vanilla | TaxEI | Random |\n|----------|---------|-------|--------|\n| C1_context_truncation | 75.0% | 83.3% | 66.7% |\n| C4_observation_masking | 72.7% | 72.7% | 72.7% |\n| P1_step_order_swap | 75.0% | 58.3% | 91.7% |\n| P2_sub_goal_deletion | 75.0% | 83.3% | 75.0% |\n\n### s0\n| Operator | Vanilla | TaxEI | Random |\n|----------|---------|-------|--------|\n| C1_context_truncation | 66.7% | — | 83.3% |\n| C4_observation_masking | 72.7% | — | 72.7% |\n| P1_step_order_swap | 91.7% | — | 66.7% |\n| P2_sub_goal_deletion | 66.7% | — | 75.0% |\n\n---\n\n## 5. LLaMA vs Qwen3-8B Comparison\n\n### Key Metrics Side-by-Side\n\n| Metric | Qwen3-8B (5-seed) | LLaMA-3.1-8B (2-seed) |\n|--------|-------------------|------------------------|\n| **Vanilla recovery** | 67.3 ± 4.7% | 74.5 ± 0.0% |\n| **TaxEI recovery** | 58.3 ± 6.5% | 74.5 ± 0.0% |\n| **Random recovery** | 58.3 ± 8.7% | 75.5 ± 1.1% |\n| **Injection penalty** | ~9pp (67.3→58.3) | **None** (74.5→74.5) |\n| **Detection rate** | 0% (all seeds) | 21-30% |\n| **Clean success (Vanilla)** | ~65% | 72.3% |\n\n### Critical Findings\n\n1. **No injection penalty on LLaMA:** All three conditions achieve ~74.5% recovery — injection training neither helps nor hurts. On Qwen3-8B, injection training *reduced* performance by ~9pp.\n\n2. **All conditions converge:** LLaMA shows near-zero variance across conditions (74.5% vs 74.5% vs 76.6%), suggesting the model's baseline capability dominates over training signal differences.\n\n3. **Non-zero detection on LLaMA:** LLaMA detects errors 21-30% of the time (Qwen3-8B: 0%), indicating stronger intrinsic error awareness regardless of training condition.\n\n4. **Higher absolute performance:** LLaMA outperforms Qwen3-8B across the board (+7-16pp recovery, +7pp clean success), consistent with it being a stronger instruction-following model.\n\n5. **Strengthens negative result:** The cross-model validation confirms TaxEI provides no advantage — but for a *different reason* than Qwen3-8B:\n   - Qwen3-8B: TaxEI = Random (both hurt vs Vanilla)\n   - LLaMA: TaxEI = Random = Vanilla (nothing helps because baseline is already strong)\n\n---\n\n## 6. Pending Experiments\n\n| Experiment | Status | ETA |\n|-----------|--------|-----|\n| llama31-taxei-s123 | Training | ~2h |\n| llama31-random-s123 | Training | ~2h |\n| llama31-vanilla-s123-eval (injected) | Not submitted | After training completes |\n| llama31-taxei-s42-clean | Not submitted | — |\n| llama31-random-s0-clean | Not submitted | — |\n\n---\n\n## 7. Implications for Paper\n\nThe LLaMA cross-model validation provides a **second mechanism** supporting the negative result:\n- **Qwen3-8B story:** TaxEI doesn't outperform Random injection (both degrade vs Vanilla)\n- **LLaMA story:** Model already resilient — no injection method adds value when baseline is strong\n\nTogether these argue that taxonomy-guided error injection is not a robust training strategy: it fails to help weak models (Qwen) and is unnecessary for strong ones (LLaMA).\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 57_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01Fev2xDAaw9g5QpuctX6iCn`</summary>

```json
{
  "name": "LLaMA-3.1-8B Cross-Model Validation Summary",
  "type": "report",
  "description": "Complete results table for LLaMA-3.1-8B cross-model validation: training metrics, injected eval recovery rates, clean eval success rates, per-operator breakdown, and comparison with Qwen3-8B findings.",
  "project": "tax_error_inject_agent",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/llama_crossmodel_summary.md",
  "tags": [
    "llama31",
    "cross-model",
    "results",
    "negative-result"
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
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55",
  "uuid": "d4e1c308-ad18-4348-81b3-95d2fe52cee2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018PFqcEBZZFdEpi9CgEfPBi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3822,
      "cache_read_input_tokens": 32905,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3822
      },
      "output_tokens": 64,
      "service_tier": "standard",
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

_source line 58 · 2026-05-16T14:57:22.698Z_

<details><summary>↩ Tool result · `toolu_01Fev2xDAaw9g5QpuctX6iCn`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_0dc6e0\", \"name\": \"LLaMA-3.1-8B Cross-Model Validation Summary\", \"type\": \"report\", \"description\": \"Complete results table for LLaMA-3.1-8B cross-model validation: training metrics, injected eval recovery rates, clean eval success rates, per-operator breakdown, and comparison with Qwen3-8B findings.\", \"path\": \"projects/tax_error_inject_agent/artifacts/_project/report/llama_crossmodel_summary.md\", \"url\": null, \"project\": \"tax_error_inject_agent\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T14:57:22.600477+00:00\", \"tags\": [\"llama31\", \"cross-model\", \"results\", \"negative-result\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55",
  "uuid": "7be7b0f4-00fa-4a32-bd9c-e8ab361c5008",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260516_0dc6e0\\\", \\\"name\\\": \\\"LLaMA-3.1-8B Cross-Model Validation Summary\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Complete results table for LLaMA-3.1-8B cross-model validation: training metrics, injected eval recovery rates, clean eval success rates, per-operator breakdown, and comparison with Qwen3-8B findings.\\\", \\\"path\\\": \\\"projects/tax_error_inject_agent/artifacts/_project/report/llama_crossmodel_summary.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"tax_error_inject_agent\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-16T14:57:22.600477+00:00\\\", \\\"tags\\\": [\\\"llama31\\\", \\\"cross-model\\\", \\\"results\\\", \\\"negative-result\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_0dc6e0\", \"name\": \"LLaMA-3.1-8B Cross-Model Validation Summary\", \"type\": \"report\", \"description\": \"Complete results table for LLaMA-3.1-8B cross-model validation: training metrics, injected eval recovery rates, clean eval success rates, per-operator breakdown, and comparison with Qwen3-8B findings.\", \"path\": \"projects/tax_error_inject_agent/artifacts/_project/report/llama_crossmodel_summary.md\", \"url\": null, \"project\": \"tax_error_inject_agent\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T14:57:22.600477+00:00\", \"tags\": [\"llama31\", \"cross-model\", \"results\", \"negative-result\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 59_

已完成。核心发现：

**LLaMA-3.1-8B (2-seed):** Vanilla=74.5%, TaxEI=74.5%, Random=75.5% — 三个条件完全收敛，无 injection penalty。

**与 Qwen3-8B 的关键差异：**
- Qwen3-8B: injection 训练降低性能 ~9pp（67.3→58.3），但 TaxEI≈Random
- LLaMA: 模型本身已足够强，任何 injection 方法都不增加价值（也不损害）
- LLaMA 有 21-30% detection rate（Qwen3-8B 为 0%）

**Pending:** s123 的 taxei 和 random 仍在训练中，另外 taxei-s42-clean 和 random-s0-clean 未提交。

Artifact 已注册：`art_20260516_0dc6e0`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55",
  "uuid": "4bdd911a-c594-4b81-861c-b36f51060d62",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016tUNyeKFSwSjz9EjooFyJK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 593,
      "cache_read_input_tokens": 36727,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 593
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

_source line 60_

已完成。核心发现：

**LLaMA-3.1-8B (2-seed):** Vanilla=74.5%, TaxEI=74.5%, Random=75.5% — 三个条件完全收敛，无 injection penalty。

**与 Qwen3-8B 的关键差异：**
- Qwen3-8B: injection 训练降低性能 ~9pp（67.3→58.3），但 TaxEI≈Random
- LLaMA: 模型本身已足够强，任何 injection 方法都不增加价值（也不损害）
- LLaMA 有 21-30% detection rate（Qwen3-8B 为 0%）

**Pending:** s123 的 taxei 和 random 仍在训练中，另外 taxei-s42-clean 和 random-s0-clean 未提交。

Artifact 已注册：`art_20260516_0dc6e0`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 251903,
  "duration_api_ms": 250155,
  "num_turns": 7,
  "stop_reason": "end_turn",
  "session_id": "ae491a69-2268-4f52-bbd5-112d75ec9c55",
  "total_cost_usd": 1.1262785,
  "usage": {
    "input_tokens": 10,
    "cache_creation_input_tokens": 25479,
    "cache_read_input_tokens": 156797,
    "output_tokens": 5040,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 25479,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 263,
        "cache_read_input_tokens": 36727,
        "cache_creation_input_tokens": 593,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 593
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1562,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001657,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 25,
      "outputTokens": 14310,
      "cacheReadInputTokens": 515293,
      "cacheCreationInputTokens": 81456,
      "webSearchRequests": 0,
      "costUSD": 1.1246215,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "6ce9b254-4b43-40cc-850b-4c39d4858478"
}
```

</details>

---
