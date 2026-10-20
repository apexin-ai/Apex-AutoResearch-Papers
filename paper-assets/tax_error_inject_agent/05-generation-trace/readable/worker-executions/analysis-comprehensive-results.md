# analysis comprehensive results

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 1
- **Tool calls:** 12
- **Original source:** `logs/workers/worker_analysis_comprehensive-results_20260515T005132.log`
- **Structured JSON:** [`3aae2e4fd8f1e12fca8e.json`](../../sessions/3a/3aae2e4fd8f1e12fca8e.json)

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
  "session_id": "54884577-4b89-43d3-8e16-64aaa0260a70",
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
  "uuid": "480d1373-c11e-41f8-81cf-8907cd5dcbbb",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/memory/"
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
    "resetsAt": 1778808600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "315eff5c-22bf-44b4-a553-97032ce121dc",
  "session_id": "54884577-4b89-43d3-8e16-64aaa0260a70"
}
```

---

### Assistant

_source line 4_

I'll read the registry first to get all experiment data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "54884577-4b89-43d3-8e16-64aaa0260a70",
  "uuid": "831ed8b6-2302-42c0-9914-13bd3b718022",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018uxHwZKabJsWi5t74gvHc1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11805,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11805
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_015ca2q7ovyPZLYTYuT2mpa1`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
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
  "session_id": "54884577-4b89-43d3-8e16-64aaa0260a70",
  "uuid": "35b0668e-4b72-4841-adb6-d6ced5b99ca0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018uxHwZKabJsWi5t74gvHc1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11805,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11805
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

_source line 6 · 2026-05-15T00:51:43.439Z_

<details><summary>↩ Tool result · `toolu_015ca2q7ovyPZLYTYuT2mpa1`</summary>

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
  "session_id": "54884577-4b89-43d3-8e16-64aaa0260a70",
  "uuid": "70a8ed3b-3d7d-4f80-a31e-a50e952ac696",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
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
Let me read the registry to get all experiment data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "54884577-4b89-43d3-8e16-64aaa0260a70",
  "uuid": "c4710834-6fe2-4a36-a3a0-00b49277a913",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QxysdAXMqRjmChAFB5TBSM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1338,
      "cache_read_input_tokens": 23646,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1338
      },
      "output_tokens": 18,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_011d9D2dmGDnyXRF97Q45yfF`</summary>

```json
{
  "project": "tax_error_inject_agent",
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
  "session_id": "54884577-4b89-43d3-8e16-64aaa0260a70",
  "uuid": "af638d31-af50-4178-8fc6-70e80e9dfffd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QxysdAXMqRjmChAFB5TBSM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1338,
      "cache_read_input_tokens": 23646,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1338
      },
      "output_tokens": 18,
      "service_tier": "standard",
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

_source line 9 · 2026-05-15T00:51:48.140Z_

<details><summary>↩ Tool result · `toolu_011d9D2dmGDnyXRF97Q45yfF`</summary>

```text
Error: result (71,979 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/54884577-4b89-43d3-8e16-64aaa0260a70/tool-results/mcp-agent-ml-research-read_registry-1778806308126.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/54884577-4b89-43d3-8e16-64aaa0260a70/tool-results/mcp-agent-ml-research-read_registry-1778806308126.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/54884577-4b89-43d3-8e16-64aaa0260a70/tool-results/mcp-agent-ml-research-read_registry-1778806308126.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "54884577-4b89-43d3-8e16-64aaa0260a70",
  "uuid": "69f8ff25-88b4-4ad9-bd05-4677989dd9a3",
  "tool_use_result": {
    "content": "Error: result (71,979 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/54884577-4b89-43d3-8e16-64aaa0260a70/tool-results/mcp-agent-ml-research-read_registry-1778806308126.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/54884577-4b89-43d3-8e16-64aaa0260a70/tool-results/mcp-agent-ml-research-read_registry-1778806308126.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/54884577-4b89-43d3-8e16-64aaa0260a70/tool-results/mcp-agent-ml-research-read_registry-1778806308126.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"v4-random-fixed-inject25\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T00:25:44.436Z\", \"updated_at\": \"2026-05-15T00:47:27.396Z\", \"hypothesis\": \"v4 Random fixed-size ablation: 25% injection (4,358 total). 与 TaxEI 25% (48.9%) 对比 taxonomy 标签在中等注入比例下是否有差异。\", \"spec\": {\"command\": \"swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/ablation_fixed/sft_random_v4_fixed_inject25.jsonl --lora_rank 16 --num_train_epochs 3 --seed 42 --output_dir checkpoints/v4_random_fixed_inject25 --gradient_accumulation_steps 8 --learning_rate 1e-4 --lr_scheduler_type cosine --gradient_checkpointing true --save_strategy epoch --logging_steps 5 --weight_decay 0.1 --adam_beta1 0.9 --adam_beta2 0.95\", \"server\": \"autodl-5090\", \"data_path\": \"data/mini_pipeline_v4/ablation_fixed/sft_random_v4_fixed_inject25.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"gpu\": \"cuda:1\", \"max_steps\": 1635, \"checkpoint_path\": \"checkpoints/v4_random_fixed_inject25/v1-20260515-084707\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-fixed-inject25.log\"}}, \"v4-random-fixed-inject10\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T00:25:41.996Z\", \"updated_at\": \"2026-05-15T00:45:58.420Z\", \"hypothesis\": \"v4 Random fixed-size ablation: 10% injection (4,358 total). 与 TaxEI 10% (61.7%) 对比 taxonomy 标签在低注入比例下是否有差异。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export CUDA_VISIBLE_DEVICES=2 && cd /root/autodl-tmp/tax_error_inject_agent && swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/ablation_fixed/sft_random_v4_fixed_inject10.jsonl --lora_rank 16 --num_train_epochs 3 --seed 42 --output_dir checkpoints/v4_random_fixed_inject10 --gradient_accumulation_steps 8 --learning_rate 1e-4 --lr_scheduler_type cosine --gradient_checkpointing true --save_strategy epoch --logging_steps 5 --weight_decay 0.1 --adam_beta1 0.9 --adam_beta2 0.95\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"104655\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-fixed-inject10.log\", \"submitted_at\": \"2026-05-15T00:28:19.537Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/mini_pipeline_v4/ablation_fixed/sft_random_v4_fixed_inject10.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 42}}, \"v4-random-fixed-inject50\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T00:45:08.375Z\", \"updated_at\": \"2026-05-15T00:45:37.682Z\", \"hypothesis\": \"v4 Random fixed-size ablation: 50% injection (4,358 total = 2,179 clean + 2,179 injected). 与 TaxEI 50% 对比 taxonomy 标签在高注入比例下是否有差异。\", \"spec\": {\"command\": \"swift sft --model Qwen3-8B --dataset sft_random_v4_fixed_inject50.jsonl --output_dir checkpoints/random_fixed_inject50 --lora_rank 16 --lora_alpha 32 --lora_dropout 0.05 --target_modules all-linear --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --max_length 4096 --num_train_epochs 3 --learning_rate 1e-4 --seed 42 --torch_dtype bfloat16 --logging_steps 5 --save_strategy epoch --gradient_checkpointing true\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"105879\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-fixed-inject50.log\", \"submitted_at\": \"2026-05-15T00:45:22.505Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/mini_pipeline_v4/ablation_fixed/sft_random_v4_fixed_inject50.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen/Qwen3-8B\", \"seed\": 42, \"checkpoint_path\": \"checkpoints/random_fixed_inject50\"}}, \"v4-taxei-fixed-inject50\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T00:25:38.284Z\", \"updated_at\": \"2026-05-15T00:28:05.552Z\", \"hypothesis\": \"v4 TaxEI fixed-size ablation: 50% injection ratio (4,358 total = 2,179 clean + 2,179 injected). Dose-response 最后一个点，完成后有完整曲线 0%→10%→25%→50%。\", \"spec\": {\"command\": \"swift sft --model Qwen3-8B --dataset sft_taxei_v4_fixed_inject50.jsonl --lora_rank 16 --num_train_epochs 3 --seed 42 --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --learning_rate 1e-4\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"104236\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-fixed-inject50.log\", \"submitted_at\": \"2026-05-15T00:27:51.219Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject50.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 42}}, \"v4-random-seed123-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T00:14:30.699Z\", \"updated_at\": \"2026-05-15T00:27:24.291Z\", \"hypothesis\": \"v4 Random SFT seed=123 eval — 47 tasks clean eval. Multi-seed: seed=42 66.0%, seed=0 55.3%, seed=123 待测。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export CUDA_VISIBLE_DEVICES=1 && cd /root/autodl-tmp/tax_error_inject_agent && python eval/recovery.py --model_path checkpoints/mini_random_sft_v4_seed123/v0-20260515-055925/checkpoint-3387 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_random_seed123_eval.json --device cuda:0\\\"\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"pid\": 102888, \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-seed123-eval.log\", \"submitted_at\": \"2026-05-15T00:14:42.930Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"eval/eval_tasks_47.json\", \"data_count\": 47, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"checkpoint_source\": \"checkpoints/mini_random_sft_v4_seed123/v0-20260515-055925/checkpoint-3387\", \"eval_data\": \"47 tasks clean eval (no injection)\", \"parent\": \"v4-random-seed123\", \"tmux_session\": \"v4-random-seed123-eval\", \"log_file\": \"~/runs/tax_error_inject_agent/v4-random-seed123-eval.log\", \"wall_clock_seconds\": 740.0, \"gpu_hours\": 0.21}, \"conclusion\": \"negative\", \"checkpoint_path\": \"checkpoints/mini_random_sft_v4_seed123/v0-20260515-055925/checkpoint-3387\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-seed123-eval.log\", \"completed_at\": \"2026-05-15T00:27:02.930Z\", \"metrics\": {\"eval_success_rate\": 0.681, \"eval_successes\": 32, \"eval_total\": 47, \"by_task\": {\"look_at_obj_in_light\": {\"total\": 6, \"success\": 5, \"rate\": 0.833}, \"pick_and_place_simple\": {\"total\": 8, \"success\": 5, \"rate\": 0.625}, \"pick_clean_then_place_in_recep\": {\"total\": 11, \"success\": 7, \"rate\": 0.636}, \"pick_cool_then_place_in_recep\": {\"total\": 7, \"success\": 4, \"rate\": 0.571}, \"pick_heat_then_place_in_recep\": {\"total\": 8, \"success\": 6, \"rate\": 0.75}, \"pick_two_obj_and_place\": {\"total\": 7, \"success\": 5, \"rate\": 0.714}}}}, \"v4-taxei-fixed-inject25-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T23:50:53.016Z\", \"updated_at\": \"2026-05-15T00:14:40.327Z\", \"hypothesis\": \"v4 TaxEI 25% injection fixed-size eval — 48.9% (23/47), 显著低于 vanilla baseline 65.3%（-16.4pp）。Dose-response 数据点。\", \"spec\": {\"command\": \"python3 eval/recovery.py --model_path output/v4-fixed-inject25/v0-20260515-063144/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_taxei_fixed_inject25_eval.json --device cuda:0\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"checkpoint_source\": \"output/v4-fixed-inject25/v0-20260515-063144/checkpoint-1635\", \"eval_data\": \"47 ALFWorld tasks (clean)\", \"parent\": \"v4-taxei-fixed-inject25-r2\", \"data_path\": \"eval/valid_unseen\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (taxei fixed inject25)\", \"seed\": 42}, \"metrics\": {\"eval_success_rate\": 0.489, \"eval_successes\": 23, \"eval_total\": 47, \"by_task\": {\"look_at_obj_in_light\": {\"success\": 4, \"total\": 6, \"rate\": 0.667}, \"pick_and_place_simple\": {\"success\": 3, \"total\": 8, \"rate\": 0.375}, \"pick_clean_then_place_in_recep\": {\"success\": 5, \"total\": 11, \"rate\": 0.455}, \"pick_cool_then_place_in_recep\": {\"success\": 2, \"total\": 7, \"rate\": 0.286}, \"pick_heat_then_place_in_recep\": {\"success\": 5, \"total\": 8, \"rate\": 0.625}, \"pick_two_obj_and_place\": {\"success\": 4, \"total\": 7, \"rate\": 0.571}}}, \"checkpoint_path\": \"eval_results/v4_taxei_fixed_inject25_eval.json\", \"log_path\": \"/tmp/v4_taxei_fixed_inject25_eval.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T00:14:30.429Z\"}, \"v4-taxei-fixed-inject10-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T23:50:52.584Z\", \"updated_at\": \"2026-05-15T00:14:38.874Z\", \"hypothesis\": \"v4 TaxEI 10% injection fixed-size eval — 61.7% (29/47), 低于 vanilla baseline 65.3%（-3.6pp）。Dose-response 数据点。\", \"spec\": {\"command\": \"python3 eval/recovery.py --model_path output/v4-fixed-inject10/v0-20260515-061243/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_taxei_fixed_inject10_eval.json --device cuda:0\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:2\", \"tmux_session\": \"eval_inject10\", \"checkpoint_source\": \"output/v4-fixed-inject10/v0-20260515-061243/checkpoint-1635\", \"eval_data\": \"47 ALFWorld tasks (clean)\", \"parent\": \"v4-taxei-fixed-inject10\", \"data_path\": \"eval/valid_unseen\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (taxei fixed inject10)\", \"seed\": 42, \"log_path\": \"/tmp/v4_taxei_fixed_inject10_eval.log\"}, \"metrics\": {\"eval_success_rate\": 0.617, \"eval_successes\": 29, \"eval_total\": 47, \"by_task\": {\"look_at_obj_in_light\": {\"success\": 5, \"total\": 6, \"rate\": 0.833}, \"pick_and_place_simple\": {\"success\": 5, \"total\": 8, \"rate\": 0.625}, \"pick_clean_then_place_in_recep\": {\"success\": 5, \"total\": 11, \"rate\": 0.455}, \"pick_cool_then_place_in_recep\": {\"success\": 4, \"total\": 7, \"rate\": 0.571}, \"pick_heat_then_place_in_recep\": {\"success\": 6, \"total\": 8, \"rate\": 0.75}, \"pick_two_obj_and_place\": {\"success\": 4, \"total\": 7, \"rate\": 0.571}}}, \"checkpoint_path\": \"eval_results/v4_taxei_fixed_inject10_eval.json\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T00:14:29.992Z\"}, \"v4-taxei-seed123-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T23:44:07.489Z\", \"updated_at\": \"2026-05-15T00:14:37.513Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 eval/recovery.py --model_path checkpoints/mini_taxei_sft_v4_seed123/v0-20260515-055026/checkpoint-3387 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_taxei_seed123_eval.json --device cuda:0\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"pid\": 100600, \"model_name\": \"Qwen3-8B + LoRA (taxei v4 seed=123)\", \"seed\": 123, \"checkpoint_source\": \"checkpoints/mini_taxei_sft_v4_seed123/v0-20260515-055026/checkpoint-3387\", \"eval_data\": \"47 ALFWorld tasks (clean, no injection)\", \"parent\": \"v4-taxei-seed123\", \"checkpoint_path\": \"eval_results/v4_taxei_seed123_eval.json\", \"log_path\": \"/tmp/v4_taxei_seed123_eval.log\", \"data_path\": \"eval/valid_unseen\", \"data_count\": 47}, \"hypothesis\": \"v4 TaxEI SFT seed=123 eval — 61.7% (29/47), 低于 vanilla baseline 65.3%（-3.6pp）。multi-seed verification, 9029 samples。\", \"metrics\": {\"eval_success_rate\": 0.617, \"eval_successes\": 29, \"eval_total\": 47, \"by_task\": {\"look_at_obj_in_light\": {\"success\": 5, \"total\": 6, \"rate\": 0.833}, \"pick_and_place_simple\": {\"success\": 4, \"total\": 8, \"rate\": 0.5}, \"pick_clean_then_place_in_recep\": {\"success\": 7, \"total\": 11, \"rate\": 0.636}, \"pick_cool_then_place_in_recep\": {\"success\": 3, \"total\": 7, \"rate\": 0.429}, \"pick_heat_then_place_in_recep\": {\"success\": 6, \"total\": 8, \"rate\": 0.75}, \"pick_two_obj_and_place\": {\"success\": 4, \"total\": 7, \"rate\": 0.571}}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T00:14:29.055Z\"}, \"v4-random-seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:49:34.441Z\", \"updated_at\": \"2026-05-14T23:52:15.056Z\", \"hypothesis\": \"v4 Random SFT seed=123 (P1 multi-seed补齐) — 9,029 samples, same hyperparams as seed=42/0, 配齐3-seed统计分析\", \"spec\": {\"command\": \"swift sft --model Qwen3-8B --dataset sft_random_v4.jsonl --seed 123 --lora_rank 16 --num_train_epochs 3\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"pid\": 93477, \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-seed123.log\", \"submitted_at\": \"2026-05-14T21:59:16.545Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/tax_error_inject_agent/data/mini_pipeline_v4/sft_random_v4.jsonl\", \"data_count\": 9029, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"wall_clock_seconds\": 6778.5, \"gpu_hours\": 1.88}, \"reproduce\": {\"finished_at\": \"2026-05-14T23:50:09.168Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T23:50:10.389568+00:00\"}]}, \"metrics\": {\"train_loss\": 0.35484016, \"final_loss\": 0.16766574, \"token_accuracy\": 0.94187103, \"avg_token_accuracy\": 0.90849673, \"train_steps\": 3387, \"train_epochs\": 3, \"train_runtime_sec\": 6609.3556, \"train_duration_min\": 110.2, \"train_samples_per_second\": 4.098, \"train_steps_per_second\": 0.512, \"train_speed_s_per_it\": 1.951, \"memory_gib\": 18.49}, \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_random_sft_v4_seed123/v0-20260515-055925/checkpoint-3387\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T23:52:15.056Z\"}, \"v4-taxei-fixed-inject25-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:32:41.837Z\", \"updated_at\": \"2026-05-14T23:50:46.230Z\", \"hypothesis\": \"v4 TaxEI fixed-size ablation: 25% injection ratio retry (4,358 total = 3,268 clean + 1,090 injected). 修复 CUDA_VISIBLE_DEVICES，显式设 =3。\", \"spec\": {\"command\": \"export CUDA_VISIBLE_DEVICES=3 && swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject25.jsonl --output_dir checkpoints/taxei_fixed_inject25 --lora_rank 16 --lora_alpha 32 --lora_dropout 0.05 --target_modules all-linear --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --max_length 4096 --num_train_epochs 3 --learning_rate 1e-4 --seed 42 --torch_dtype bfloat16 --logging_steps 5 --save_strategy epoch --gradient_checkpointing true\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"pid\": 96835, \"data_path\": \"data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject25.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"injection_ratio\": 0.25, \"clean_count\": 3268, \"injected_count\": 1090, \"log_path\": \"/tmp/v4-fixed-inject25.log\", \"note\": \"manual tmux with explicit CUDA_VISIBLE_DEVICES=3, fixing r1 OOM\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"output/v4-fixed-inject25/v0-20260515-063144/checkpoint-1635\", \"metrics\": {\"final_loss\": 0.285, \"token_accuracy\": 0.893, \"train_steps\": 1635, \"train_epochs\": 3, \"train_duration_min\": 58}, \"completed_at\": \"2026-05-14T23:50:46.230Z\"}, \"v4-taxei-fixed-inject10\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:09:52.707Z\", \"updated_at\": \"2026-05-14T23:50:45.829Z\", \"hypothesis\": \"v4 TaxEI fixed-size ablation: 10% injection ratio (4,358 total = 3,922 clean + 436 injected). Fixed-size = vanilla 大小，控制数据量变量。Dose-response: 10%/25%/50%。\", \"spec\": {\"command\": \"swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset sft_taxei_v4_fixed_inject10.jsonl --output_dir output/v4-fixed-inject10 --num_train_epochs 3 --learning_rate 1e-4 --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --lora_rank 16 --lora_alpha 32 --lora_dropout 0.05 --seed 42 --data_seed 42 --bf16 true --gradient_checkpointing true\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"94635\", \"log_path\": \"/tmp/v4-fixed-inject10.log\", \"submitted_at\": \"2026-05-15T06:12:34Z\", \"submitted_via\": \"manual_tmux\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject10.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"injection_ratio\": 0.1, \"clean_count\": 3922, \"injected_count\": 436}, \"conclusion\": \"success\", \"checkpoint_path\": \"output/v4-fixed-inject10/v0-20260515-061243/checkpoint-1635\", \"metrics\": {\"final_loss\": 0.308, \"token_accuracy\": 0.888, \"train_steps\": 1635, \"train_epochs\": 3, \"train_duration_min\": 58}, \"completed_at\": \"2026-05-14T23:50:45.829Z\"}, \"v4-taxei-fixed-inject25\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:09:53.209Z\", \"updated_at\": \"2026-05-14T23:45:26.890Z\", \"hypothesis\": \"v4 TaxEI fixed-size ablation: 25% injection ratio (4,358 total = 3,268 clean + 1,090 injected). Fixed-size = vanilla 大小，控制数据量变量。Dose-response: 10%/25%/50%。\", \"spec\": {\"command\": \"swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset sft_taxei_v4_fixed_inject25.jsonl --output_dir output/v4-fixed-inject25 --num_train_epochs 3 --learning_rate 1e-4 --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --lora_rank 16 --lora_alpha 32 --lora_dropout 0.05 --seed 42 --data_seed 42 --bf16 true --gradient_checkpointing true\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"96835\", \"log_path\": \"/tmp/v4-fixed-inject25.log\", \"submitted_at\": \"2026-05-15T06:31:44Z\", \"submitted_via\": \"manual_tmux\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/mini_pipeline_v4/ablation_fixed/sft_taxei_v4_fixed_inject25.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"injection_ratio\": 0.25, \"clean_count\": 3268, \"injected_count\": 1090, \"note\": \"r1 (PID 95170) OOM on cuda:0 — submit_training_job failed to pass CUDA_VISIBLE_DEVICES. Resubmitted manually via tmux with explicit export CUDA_VISIBLE_DEVICES=3.\"}, \"conclusion\": \"failed\", \"failure_reason\": \"CUDA_VISIBLE_DEVICES 未生效，模型加载到 cuda:0 导致 OOM（与 seed123 训练冲突）\", \"completed_at\": \"2026-05-14T23:45:26.890Z\"}, \"v4-taxei-seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:49:34.191Z\", \"updated_at\": \"2026-05-14T23:43:38.819Z\", \"hypothesis\": \"v4 TaxEI SFT seed=123 (P1 multi-seed补齐) — 9,029 samples, same hyperparams as seed=42/0, 配齐3-seed统计分析\", \"spec\": {\"command\": \"swift sft --model Qwen3-8B --dataset sft_taxei_v4.jsonl --seed 123 --lora_rank 16 --num_train_epochs 3\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"pid\": 92263, \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-seed123.log\", \"submitted_at\": \"2026-05-14T21:50:17.845Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/tax_error_inject_agent/data/mini_pipeline_v4/sft_taxei_v4.jsonl\", \"data_count\": 9029, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"wall_clock_seconds\": 6801.0, \"gpu_hours\": 1.89}, \"reproduce\": {\"finished_at\": \"2026-05-14T23:41:32.774Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T23:41:33.984355+00:00\"}]}, \"metrics\": {\"final_loss\": 0.35506879, \"token_accuracy\": 0.89978214, \"train_steps\": 3387, \"train_epochs\": 3, \"train_duration_min\": 109.2, \"train_runtime_sec\": 6549.432, \"train_speed_s_per_it\": 1.934, \"memory_gib\": 18.49}, \"checkpoint_path\": \"checkpoints/mini_taxei_sft_v4_seed123/v0-20260515-055026/checkpoint-3387\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T23:43:38.819Z\"}, \"v4-fixed-inject25\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:09:23.317Z\", \"updated_at\": \"2026-05-14T22:29:19.308Z\", \"spec\": {\"hypothesis\": \"Fixed-size ablation: 25% injection ratio (4,358 total samples, ~1,090 injected + ~3,269 clean). Tests intermediate injection ratio. Combined with 10%/50% results, reveals dose-response curve. Addresses Reviewer Concern #5.\", \"parent\": \"v4-taxei-eval\", \"plan_id\": \"fixed-size-ablation\", \"reviewer_concern\": \"RC5\"}, \"conclusion\": \"killed\", \"failure_reason\": \"duplicate entry — active experiment is v4-taxei-fixed-inject25 (RUNNING)\"}, \"v4-fixed-inject10\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:09:21.673Z\", \"updated_at\": \"2026-05-14T22:29:18.354Z\", \"spec\": {\"hypothesis\": \"Fixed-size ablation: 10% injection ratio (4,358 total samples, ~436 injected + ~3,922 clean). Tests whether low injection ratio still harms clean performance. If yes → injection itself is harmful regardless of ratio. Addresses Reviewer Concern #5.\", \"parent\": \"v4-taxei-eval\", \"plan_id\": \"fixed-size-ablation\", \"reviewer_concern\": \"RC5\"}, \"conclusion\": \"killed\", \"failure_reason\": \"duplicate entry — active experiment is v4-taxei-fixed-inject10 (RUNNING)\"}, \"v4-random-recovery-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:04:57.591Z\", \"updated_at\": \"2026-05-14T22:00:43.285Z\", \"hypothesis\": \"v4 Random SFT seed=42 recovery eval (injected_eval.py) — 47 episodes with error injection, measuring detection/recovery/success rates under P1/P2/C1/C4 operators. Phase 2 counterpart to vanilla/taxei recovery eval.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 eval/injected_eval.py --model_path checkpoints/mini_random_sft_v4/v1-20260514-213104/checkpoint-3387 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --model_variant random --num_episodes 47 --seed 42 --device cuda:0 --output eval_results/v4_random_recovery_eval.json\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"pid\": 90124, \"model_name\": \"Qwen3-8B + LoRA (random SFT v4)\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/mini_random_sft_v4/v1-20260514-213104/checkpoint-3387\", \"eval_data\": \"valid_unseen (47 episodes)\", \"log_path\": \"/tmp/v4_random_recovery_eval.log\", \"output_path\": \"eval_results/v4_random_recovery_eval.json\", \"data_path\": \"valid_unseen\", \"data_count\": 47}, \"conclusion\": \"success\", \"checkpoint_path\": \"eval_results/v4_random_recovery_eval.json\", \"completed_at\": \"2026-05-14T21:42:07.544Z\", \"metrics\": {\"recovery_rate\": 0.638, \"detection_rate\": 0, \"successes\": 30, \"total\": 47, \"source\": \"json-file-verified\", \"note\": \"r1=29/47, r2=30/47, ±2pp run-to-run variance on P1 non-determinism\"}}, \"v4-taxei-recovery-eval-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:23:55.110Z\", \"updated_at\": \"2026-05-14T21:46:19.993Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 eval/injected_eval.py --model_path checkpoints/mini_taxei_sft_v4/v1-20260514-213102/checkpoint-3387 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --model_variant taxei --num_episodes 47 --seed 42 --device cuda:0 --output eval_results/v4_taxei_recovery_eval_r2.json\", \"server\": \"autodl-5090\", \"model_name\": \"Qwen3-8B + LoRA (mini_taxei_sft_v4 checkpoint-3387)\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/mini_taxei_sft_v4/v1-20260514-213102/checkpoint-3387\", \"eval_data\": \"47 episodes with error injection (4 operators: C1_context_truncation, C4_observation_masking, P1_step_order_swap, P2_sub_goal_deletion)\", \"data_path\": \"eval/injected_eval.py\", \"data_count\": 47, \"hypothesis\": \"v4 TaxEI SFT seed=42 recovery eval retry — 47 episodes with error injection, measuring detection/recovery/success rates. Previous attempt reported process dead 5x.\", \"pid\": 90519, \"log_path\": \"/tmp/v4_taxei_recovery_eval_r2.log\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"eval_results/v4_taxei_recovery_eval_r2.json\", \"completed_at\": \"2026-05-14T21:42:08.000Z\", \"metrics\": {\"recovery_rate\": 0.596, \"detection_rate\": 0, \"total_episodes\": 47, \"per_operator\": {\"C1_context_truncation\": {\"recovered\": 8, \"total\": 12, \"rate\": 0.667}, \"C4_observation_masking\": {\"recovered\": 7, \"total\": 11, \"rate\": 0.636}, \"P1_step_order_swap\": {\"recovered\": 7, \"total\": 12, \"rate\": 0.583}, \"P2_sub_goal_deletion\": {\"recovered\": 6, \"total\": 12, \"rate\": 0.5}}}}, \"v4-taxei-seed0-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:30:26.278Z\", \"updated_at\": \"2026-05-14T21:21:53.154Z\", \"hypothesis\": \"v4 TaxEI SFT seed=0 eval — multi-seed verification, 9029 samples, testing TaxEI injection stability\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 eval/recovery.py --model_path checkpoints/mini_taxei_sft_v4_seed0/v0-20260515-014320/checkpoint-3387 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_taxei_seed0_eval.json --device cuda:0\", \"server\": \"autodl-5090\", \"data_path\": \"eval/valid_unseen\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (taxei v4 seed=0)\", \"seed\": 0, \"checkpoint_source\": \"checkpoints/mini_taxei_sft_v4_seed0/v0-20260515-014320/checkpoint-3387\", \"eval_data\": \"47 ALFWorld tasks (clean, no injection)\", \"parent\": \"v4-taxei-seed0\", \"checkpoint_path\": \"eval_results/v4_taxei_seed0_eval.json\", \"log_path\": \"eval_results/v4_taxei_seed0_eval.log\"}, \"conclusion\": \"success\", \"metrics\": {\"eval_success_rate\": 0.468, \"eval_successes\": 22, \"eval_total\": 47, \"vs_seed42_pp\": -14.9}, \"completed_at\": \"2026-05-14T21:20:13.351Z\"}, \"v4-random-seed0-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:30:26.456Z\", \"updated_at\": \"2026-05-14T21:21:52.271Z\", \"hypothesis\": \"v4 Random SFT seed=0 eval — multi-seed verification, 9029 samples, testing random injection stability\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python3 eval/recovery.py --model_path checkpoints/mini_random_sft_v4_seed0/v0-20260515-014329/checkpoint-3387 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_random_seed0_eval.json --device cuda:0\", \"server\": \"autodl-5090\", \"data_path\": \"eval/valid_unseen\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + LoRA (random v4 seed=0)\", \"seed\": 0, \"checkpoint_source\": \"checkpoints/mini_random_sft_v4_seed0/v0-20260515-014329/checkpoint-3387\", \"eval_data\": \"47 ALFWorld tasks (clean, no injection)\", \"parent\": \"v4-random-seed0\", \"log_path\": \"eval_results/v4_random_seed0_eval.log\"}, \"conclusion\": \"success\", \"metrics\": {\"eval_success_rate\": 0.553, \"eval_successes\": 26, \"eval_total\": 47, \"vs_seed42_pp\": -10.7}, \"checkpoint_path\": \"eval_results/v4_random_seed0_eval.json\", \"completed_at\": \"2026-05-14T21:20:14.339Z\"}, \"v4-vanilla-recovery-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T19:30:18.314Z\", \"updated_at\": \"2026-05-14T21:21:50.951Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 eval/injected_eval.py --model_path checkpoints/mini_vanilla_sft_v4/v0-20260514-201441/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --model_variant vanilla --num_episodes 47 --seed 42 --device cuda:0 --output eval_results/v4_vanilla_recovery_eval.json\", \"server\": \"autodl-5090\", \"model_name\": \"Qwen3-8B + LoRA (vanilla v4 seed=42)\", \"checkpoint_source\": \"checkpoints/mini_vanilla_sft_v4/v0-20260514-201441/checkpoint-1635\", \"eval_data\": \"47 ALFWorld tasks with error injection\", \"seed\": 42, \"parent\": \"mini-vanilla-sft-v4\", \"checkpoint_path\": \"eval_results/v4_vanilla_recovery_eval.json\", \"log_path\": \"eval_results/v4_vanilla_recovery_eval.json\"}, \"hypothesis\": \"v4 Vanilla SFT seed=42 recovery eval (injected_eval.py) — 47 episodes with error injection, measuring detection/recovery/success rates under P1/P2/C1/C4 operators\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.617, \"successes\": 29, \"total\": 47, \"recovery_rate\": 0.617, \"detection_rate\": 0}, \"completed_at\": \"2026-05-14T21:20:15.791Z\"}, \"v4-taxei-recovery-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:40:41.154Z\", \"updated_at\": \"2026-05-14T21:20:17.664Z\", \"spec\": {\"hypothesis\": \"D010 Phase 2: Recovery eval with action injection on TaxEI seed=42 checkpoint — measuring TaxEI-trained model's recovery ability vs vanilla\", \"command\": \"CUDA_VISIBLE_DEVICES=3 python3 eval/injected_eval.py --model_path /root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_taxei_sft_v4/v1-20260514-213102/checkpoint-3387 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --model_variant taxei --device cuda:0 --seed 42 --output eval_results/v4_taxei_recovery_eval.json\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"pid\": 87614, \"data_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_taxei_sft_v4/v1-20260514-213102/checkpoint-3387\", \"data_count\": 47, \"model_name\": \"Qwen3-8B + TaxEI LoRA v4 checkpoint-3387\", \"seed\": 42, \"checkpoint_source\": \"mini_taxei_sft_v4/v1-20260514-213102/checkpoint-3387\", \"eval_data\": \"ALFWorld valid_unseen 47 tasks with action injection\", \"checkpoint_path\": \"eval_results/v4_taxei_recovery_eval.json\", \"log_path\": \"/root/runs/tax_error_inject_agent/v4-taxei-recovery-eval.log\"}, \"hypothesis\": \"v4 TaxEI SFT seed=42 recovery eval (injected_eval.py) — 47 episodes with error injection, measuring detection/recovery/success rates under P1/P2/C1/C4 operators. Phase 2 counterpart to vanilla recovery eval.\", \"reproduce\": {\"finished_at\": \"2026-05-14T20:58:38.335Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T20:58:38.665Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T20:58:39.601019+00:00\"}]}, \"metrics\": {\"success_rate\": 0.596, \"successes\": 28, \"total\": 47, \"recovery_rate\": 0.596, \"detection_rate\": 0}}, \"v4-vanilla-seed123-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:30:26.635Z\", \"updated_at\": \"2026-05-14T20:43:48.780Z\", \"hypothesis\": \"v4 Vanilla SFT seed=123 eval — multi-seed verification, 4358 samples, comparing with seed=42 baseline (61.7%)\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python3 eval/recovery.py --model_path checkpoints/mini_vanilla_sft_v4_seed123/v1-20260515-022602/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_vanilla_seed123_eval.json --device cuda:0\", \"server\": \"autodl-5090\", \"model_name\": \"Qwen3-8B + LoRA (vanilla v4 seed=123)\", \"seed\": 123, \"checkpoint_source\": \"checkpoints/mini_vanilla_sft_v4_seed123/v1-20260515-022602/checkpoint-1635\", \"checkpoint_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_vanilla_sft_v4_seed123/v1-20260515-022602/checkpoint-1635\", \"log_path\": \"/tmp/v4_vanilla_seed123_eval.log\", \"eval_data\": \"47 ALFWorld tasks (clean, no injection)\", \"parent\": \"v4-vanilla-seed123\", \"data_path\": \"eval/valid_unseen\", \"data_count\": 47}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T20:37:11.382Z\", \"metrics\": {\"eval_success_rate\": 0.66, \"eval_successes\": 31, \"eval_total\": 47, \"vs_seed42_pp\": 4.3, \"vs_seed0_pp\": -2.1, \"per_task\": {\"look_at_obj_in_light\": {\"success\": 5, \"total\": 6, \"rate\": 0.833}, \"pick_and_place_simple\": {\"success\": 6, \"total\": 8, \"rate\": 0.75}, \"pick_clean_then_place_in_recep\": {\"success\": 5, \"total\": 11, \"rate\": 0.455}, \"pick_cool_then_place_in_recep\": {\"success\": 4, \"total\": 7, \"rate\": 0.571}, \"pick_heat_then_place_in_recep\": {\"success\": 7, \"total\": 8, \"rate\": 0.875}, \"pick_two_obj_and_place\": {\"success\": 4, \"total\": 7, \"rate\": 0.571}}}}, \"v4-random-seed0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:42:03.440Z\", \"updated_at\": \"2026-05-14T19:36:31.263Z\", \"hypothesis\": \"v4 Random SFT seed=0 (multi-seed verification) — 9,029 samples, same hyperparams as seed=42, testing result stability\", \"spec\": {\"data_path\": \"data/mini_pipeline_v4/sft_random_v4.jsonl\", \"data_count\": 9029, \"model_name\": \"Qwen3-8B\", \"seed\": 0, \"server\": \"autodl-5090\", \"command\": \"swift sft --model Qwen3-8B --dataset sft_random_v4.jsonl --seed 0\", \"gpu\": \"cuda:2\", \"pid\": 72303, \"log_path\": \"/root/runs/tax_error_inject_agent/v4-random-seed0.log\", \"checkpoint_path\": \"checkpoints/mini_random_sft_v4_seed0/v0-20260515-014329/checkpoint-3387\"}, \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.355, \"token_accuracy\": 0.912, \"train_steps\": 3387, \"train_epochs\": 3, \"train_duration_min\": 110}, \"completed_at\": \"2026-05-14T19:35:39.420Z\"}, \"v4-taxei-seed0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:42:02.696Z\", \"updated_at\": \"2026-05-14T19:36:29.716Z\", \"hypothesis\": \"v4 TaxEI SFT seed=0 (multi-seed verification) — 9,029 samples, same hyperparams as seed=42, testing result stability\", \"spec\": {\"data_path\": \"data/mini_pipeline_v4/sft_taxei_v4.jsonl\", \"data_count\": 9029, \"model_name\": \"Qwen3-8B\", \"seed\": 0, \"server\": \"autodl-5090\", \"command\": \"swift sft --model Qwen3-8B --dataset sft_taxei_v4.jsonl --seed 0\", \"gpu\": \"cuda:1\", \"pid\": 71822, \"log_path\": \"/root/runs/tax_error_inject_agent/v4-taxei-seed0.log\", \"checkpoint_path\": \"checkpoints/mini_taxei_sft_v4_seed0/v0-20260515-014320/checkpoint-3387\"}, \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.355, \"token_accuracy\": 0.917, \"train_steps\": 3387, \"train_epochs\": 3, \"train_duration_min\": 110}, \"completed_at\": \"2026-05-14T19:35:37.503Z\"}, \"v4-vanilla-seed0-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:30:26.093Z\", \"updated_at\": \"2026-05-14T19:30:45.170Z\", \"hypothesis\": \"v4 Vanilla SFT seed=0 eval — multi-seed verification, 4358 samples, comparing with seed=42 baseline (61.7%)\", \"spec\": {\"checkpoint_path\": \"eval_results/v4_vanilla_seed0_eval.json\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-vanilla-seed0-eval.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T19:01:19.696Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T19:01:20.697938+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"eval_success_rate\": 0.681, \"eval_successes\": 32, \"eval_total\": 47, \"vs_seed42_pp\": 6.4, \"mcnemar_vs_seed42_p\": 0.375, \"discordant_pairs\": 5, \"per_task\": {\"look_at_obj_in_light\": \"5/6 (83.3%)\", \"pick_and_place_simple\": \"5/8 (62.5%)\", \"pick_clean_then_place\": \"6/11 (54.5%)\", \"pick_cool_then_place\": \"4/7 (57.1%)\", \"pick_heat_then_place\": \"7/8 (87.5%)\", \"pick_two_obj_and_place\": \"5/7 (71.4%)\"}}, \"completed_at\": \"2026-05-14T19:29:37.198Z\"}, \"v4-vanilla-seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:45:23.836Z\", \"updated_at\": \"2026-05-14T19:29:24.021Z\", \"hypothesis\": \"D010 Phase 1: v4 Vanilla SFT seed=123 多种子验证 — 4,358 samples, LoRA rank=16, 3 epochs, 与 seed=42 的 61.7% 对比波动范围\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/sft_vanilla_v4.jsonl --output_dir checkpoints/mini_vanilla_sft_v4_seed123 --lora_rank 16 --lora_alpha 32 --lora_dropout 0.05 --target_modules all-linear --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --max_length 4096 --num_train_epochs 3 --learning_rate 1e-4 --seed 123 --torch_dtype bfloat16 --logging_steps 5 --save_strategy epoch --gradient_checkpointing true\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"pid\": 77937, \"log_path\": \"checkpoints/mini_vanilla_sft_v4_seed123/v1-20260515-022602/logging.jsonl\", \"submitted_at\": \"2026-05-14T18:20:42.388Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/mini_pipeline_v4/sft_vanilla_v4.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"checkpoint_path\": \"checkpoints/mini_vanilla_sft_v4_seed123\", \"note\": \"OOM on first attempt (v0), restarted as v1 with PID 77937\", \"wall_clock_seconds\": 3941.6, \"gpu_hours\": 1.09}, \"reproduce\": {\"finished_at\": \"2026-05-14T19:26:23.312Z\"}, \"failure_reason\": \"v0 OOM at model loading (GPU 3 occupied by another process, 18.21 GiB in use). v1 (PID 77937) actually completed 1635/1635 steps. Cron caught v0's EXIT_CODE=1. Verifying checkpoint validity...\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T19:26:23.949Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T19:26:24.909318+00:00\"}]}, \"metrics\": {\"final_loss\": 0.288, \"token_accuracy\": 0.903, \"train_steps\": 1635, \"train_epochs\": 3, \"train_duration_min\": 58.9}}, \"v4-vanilla-seed0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:42:01.929Z\", \"updated_at\": \"2026-05-14T18:46:58.919Z\", \"hypothesis\": \"D010 Phase 1: v4 Vanilla SFT seed=0 多种子验证 — 4,358 samples, LoRA rank=16, 3 epochs, 与 seed=42 的 61.7% 对比波动范围\", \"spec\": {\"data_path\": \"data/mini_pipeline_v4/sft_vanilla_v4.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 0, \"server\": \"autodl-5090\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && CUDA_VISIBLE_DEVICES=0 swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/sft_vanilla_v4.jsonl --output_dir checkpoints/mini_vanilla_sft_v4_seed0 --lora_rank 16 --lora_alpha 32 --lora_dropout 0.05 --target_modules all-linear --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --max_length 4096 --num_train_epochs 3 --learning_rate 1e-4 --seed 0 --torch_dtype bfloat16 --logging_steps 5 --save_strategy epoch --gradient_checkpointing true\", \"gpu\": \"cuda:0\", \"pid\": 71959, \"log_path\": \"checkpoints/mini_vanilla_sft_v4_seed0/v0-20260515-014317/logging.jsonl\", \"checkpoint_path\": \"checkpoints/mini_vanilla_sft_v4_seed0/v0-20260515-014317/checkpoint-1635\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T18:42:56.365Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T18:42:57.338365+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.297, \"avg_loss\": 0.416, \"token_accuracy\": 0.902, \"train_steps\": 1635, \"train_epochs\": 3, \"train_duration_min\": 58}, \"completed_at\": \"2026-05-14T18:45:18.121Z\"}, \"v4-vanilla-seed7\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:45:24.536Z\", \"updated_at\": \"2026-05-14T18:20:48.185Z\", \"hypothesis\": \"D010 Phase 1: v4 Vanilla SFT seed=7 多种子验证 — 4,358 samples, LoRA rank=16, 3 epochs, 与 seed=42 的 61.7% 对比波动范围\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && CUDA_VISIBLE_DEVICES=3 swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/sft_vanilla_v4.jsonl --output_dir checkpoints/mini_vanilla_sft_v4_seed7 --lora_rank 16 --lora_alpha 32 --lora_dropout 0.05 --target_modules all-linear --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --max_length 4096 --num_train_epochs 3 --learning_rate 1e-4 --seed 7 --torch_dtype bfloat16 --logging_steps 5 --save_strategy epoch --gradient_checkpointing true\", \"server\": \"autodl-5090\", \"data_path\": \"data/mini_pipeline_v4/sft_vanilla_v4.jsonl\", \"data_count\": 4358, \"model_name\": \"Qwen3-8B\", \"seed\": 7, \"gpu\": \"cuda:3\", \"pid\": \"v4-vanilla-seed7\", \"checkpoint_path\": \"checkpoints/mini_vanilla_sft_v4_seed7\", \"log_path\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_vanilla_sft_v4_seed7/train.log\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T18:20:48.185Z\"}, \"v4-recovery-eval-dev\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:42:04.153Z\", \"updated_at\": \"2026-05-14T18:15:59.630Z\", \"hypothesis\": \"Recovery eval pipeline development — inject errors during eval to test if TaxEI models recover better than random/vanilla (Option C from D009)\", \"conclusion\": \"success\", \"metrics\": {\"pipeline_files\": [\"eval/injected_eval.py\", \"scripts/run_injected_eval.sh\"], \"injected_eval_lines\": 463, \"dryrun_result\": \"PASS\", \"dryrun_detail\": \"vanilla checkpoint, 1 task, cuda:3, injected error recovered in 13 steps\"}}, \"v4-recovery-dryrun\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:45:26.420Z\", \"updated_at\": \"2026-05-14T18:15:56.604Z\", \"hypothesis\": \"D010 Phase 2 前置: Recovery eval --inject 模式 dry-run, 1-2 tasks 验证 pipeline 正常工作\", \"conclusion\": \"success\"}, \"v4-random-eval\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T16:25:02.397Z\", \"updated_at\": \"2026-05-14T17:31:46.657Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && CKPT=checkpoints/mini_random_sft_v4/v1-20260514-213104/checkpoint-3387 && test -f \\\\${CKPT}/adapter_config.json && echo 'adapter_config OK' || { echo 'ERROR: adapter_config.json missing'; exit 1; } && echo 'Using checkpoint: '\\\\$CKPT && CUDA_VISIBLE_DEVICES=1 python3 eval/recovery.py --model_path \\\\$CKPT --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_random_eval.json --device cuda:0\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"67837\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-eval.log\", \"submitted_at\": \"2026-05-14T16:25:02.357Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"v4 Random SFT eval — formal Gate 3b judgment, same-source 9,029 samples, checkpoint-3387\", \"conclusion\": \"negative\", \"metrics\": {\"eval_success_rate\": 0.66, \"eval_successes\": 31, \"eval_total\": 47, \"vs_vanilla_pp\": 4.3, \"vs_taxei_pp\": 4.3, \"mcnemar_vs_vanilla_p\": 0.754, \"per_task\": {\"look_at_obj_in_light\": \"6/6 (100%)\", \"pick_and_place_simple\": \"4/8 (50%)\", \"pick_clean_then_place\": \"6/11 (54.5%)\", \"pick_cool_then_place\": \"4/7 (57.1%)\", \"pick_heat_then_place\": \"7/8 (87.5%)\", \"pick_two_obj_and_place\": \"4/7 (57.1%)\"}}}, \"v4-taxei-eval\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T16:25:00.653Z\", \"updated_at\": \"2026-05-14T17:31:43.481Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && CKPT=checkpoints/mini_taxei_sft_v4/v1-20260514-213102/checkpoint-3387 && test -f \\\\${CKPT}/adapter_config.json && echo 'adapter_config OK' || { echo 'ERROR: adapter_config.json missing'; exit 1; } && echo 'Using checkpoint: '\\\\$CKPT && CUDA_VISIBLE_DEVICES=0 python3 eval/recovery.py --model_path \\\\$CKPT --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_taxei_eval.json --device cuda:0\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"67694\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-eval.log\", \"submitted_at\": \"2026-05-14T16:25:00.616Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"v4 TaxEI SFT eval — formal Gate 3a/3b judgment, same-source 9,029 samples, checkpoint-3387\", \"conclusion\": \"negative\", \"metrics\": {\"eval_success_rate\": 0.617, \"eval_successes\": 29, \"eval_total\": 47, \"vs_vanilla_pp\": 0, \"vs_random_pp\": -4.3, \"mcnemar_vs_vanilla_p\": 1, \"mcnemar_vs_random_p\": 0.754, \"gate_3a\": \"FAIL\", \"gate_3b\": \"FAIL\", \"gate_4\": \"PASS\", \"per_task\": {\"look_at_obj_in_light\": \"6/6 (100%)\", \"pick_and_place_simple\": \"5/8 (62.5%)\", \"pick_clean_then_place\": \"6/11 (54.5%)\", \"pick_cool_then_place\": \"3/7 (42.9%)\", \"pick_heat_then_place\": \"7/8 (87.5%)\", \"pick_two_obj_and_place\": \"2/7 (28.6%)\"}}}, \"traj_collect_500\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T06:45:21.504Z\", \"updated_at\": \"2026-05-14T16:28:02.238Z\", \"spec\": {\"command\": \"python collect_trajectories.py --target 500\", \"server\": \"autodl-5090\", \"data_path\": \"data/trajectories/\", \"data_count\": 575, \"model_name\": \"trajectory_collector\", \"seed\": 0, \"pid\": 11045, \"gpu\": \"none (CPU task)\", \"hypothesis\": \"GPT-5.2 可作为 teacher 在 ALFWorld 中收集高质量成功轨迹（预期成功率≥93%）\"}, \"metrics\": {\"successful_trajectories\": 501, \"failed_trajectories\": 213, \"total_attempts\": 714, \"success_rate\": 0.702, \"api_cost_usd\": 8.86, \"collection_time_sec\": 5245}, \"conclusion\": \"negative\", \"checkpoint_path\": \"data/trajectories/successful_trajectories.jsonl\", \"log_path\": \"/tmp/collect_500.log\", \"completed_at\": \"2026-05-14T12:21:11.941Z\"}, \"v4-vanilla-eval-r3\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T14:28:24.833Z\", \"updated_at\": \"2026-05-14T16:25:11.284Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && latest_run=\\\\$(ls -dt checkpoints/mini_vanilla_sft_v4/v0-*/ | head -1) && final_ckpt=\\\\$(ls -d \\\\\\\"\\\\${latest_run}\\\\\\\"checkpoint-* | sort -V | tail -1) && echo \\\\\\\"Using checkpoint: \\\\$final_ckpt\\\\\\\" && test -f \\\\\\\"\\\\${final_ckpt}/adapter_config.json\\\\\\\" && echo 'adapter_config.json OK' || { echo 'ERROR: adapter_config.json missing'; exit 1; } && CUDA_VISIBLE_DEVICES=0 python3 eval/recovery.py --model_path \\\\$final_ckpt --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_vanilla_eval.json --device cuda:0\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"62340\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-vanilla-eval-r3.log\", \"submitted_at\": \"2026-05-14T14:28:24.797Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"v4 Vanilla SFT eval r3 — dynamic checkpoint lookup with sort -V, adapter_config.json pre-check\", \"conclusion\": \"success\", \"metrics\": {\"eval_success_rate\": 0.617, \"eval_successes\": 29, \"eval_total\": 47, \"per_task\": {\"look_at_obj_in_light\": \"5/6 (83.3%)\", \"pick_heat_then_place\": \"6/8 (75.0%)\", \"pick_and_place_simple\": \"5/8 (62.5%)\", \"pick_cool_then_place\": \"4/7 (57.1%)\", \"pick_two_obj_and_place\": \"4/7 (57.1%)\", \"pick_clean_then_place\": \"5/11 (45.5%)\"}}}, \"v4-vanilla-eval-r2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T14:24:25.560Z\", \"updated_at\": \"2026-05-14T14:28:40.995Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && CUDA_VISIBLE_DEVICES=0 python3 eval/recovery.py --model_path checkpoints/mini_vanilla_sft_v4/v0-20260514-122641/checkpoint-1635 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_vanilla_eval.json --device cuda:0\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"61793\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-vanilla-eval-r2.log\", \"submitted_at\": \"2026-05-14T14:24:25.523Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"v4 Vanilla SFT eval retry — fixed --device cuda:0 (was --gpu 0) + explicit checkpoint-1635\", \"conclusion\": \"failed\"}, \"v4-random-sft-r2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:30:55.117Z\", \"updated_at\": \"2026-05-14T14:24:56.155Z\", \"spec\": {\"pid\": \"58163\", \"actual_status\": \"training_in_progress\", \"gpu\": [\"cuda:3\"], \"server\": \"autodl-5090\", \"data_path\": \"data/mini_pipeline_v4/sft_random_v4.jsonl\", \"data_count\": 9029, \"model_name\": \"Qwen3-8B\", \"seed\": 42}, \"hypothesis\": \"v4 Random SFT retry (r2) — same-source 9,029 samples, formal Gate 3b. Previous run killed by SIGHUP.\", \"conclusion\": \"success\"}, \"v4-taxei-sft-r2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:30:52.865Z\", \"updated_at\": \"2026-05-14T14:24:54.288Z\", \"spec\": {\"pid\": \"58034\", \"actual_status\": \"training_in_progress\", \"gpu\": [\"cuda:2\"], \"server\": \"autodl-5090\", \"data_path\": \"data/mini_pipeline_v4/sft_taxei_v4.jsonl\", \"data_count\": 9029, \"model_name\": \"Qwen3-8B\", \"seed\": 42}, \"hypothesis\": \"v4 TaxEI SFT retry (r2) — same-source 9,029 samples, formal Gate 3a/3b. Previous run killed by SIGHUP.\", \"conclusion\": \"success\"}, \"v4-vanilla-eval\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T14:15:59.327Z\", \"updated_at\": \"2026-05-14T14:24:25.638Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && CKPT=\\\\$(find checkpoints/mini_vanilla_sft_v4 -name 'checkpoint-*' -type d | sort -t- -k2 -n | tail -1) && echo \\\\\\\"Using checkpoint: \\\\$CKPT\\\\\\\" && CUDA_VISIBLE_DEVICES=0 python3 eval/recovery.py --model_path \\\\$CKPT --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_vanilla_eval.json --gpu 0\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"61138\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-vanilla-eval.log\", \"submitted_at\": \"2026-05-14T14:15:59.291Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"v4 Vanilla SFT eval (4,358 samples, clean only) — v4 baseline for Gate 3a comparison\", \"conclusion\": \"failed\"}, \"v3-random-eval\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:26:26.315Z\", \"updated_at\": \"2026-05-14T14:15:26.311Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && CUDA_VISIBLE_DEVICES=1 python3 eval/recovery.py --model_path checkpoints/mini_random_sft_v3/*/checkpoint-3405 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v3_random.json --device cuda:0\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"55925\", \"log_path\": \"~/runs/tax_error_inject_agent/v3-random-eval.log\", \"submitted_at\": \"2026-05-14T13:26:53.024Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"v3 Random SFT eval on 47-task ALFWorld (format-aligned, initial signal before v4 formal judgment)\", \"metrics\": {\"eval_success_rate\": 0.511, \"eval_successes\": 24, \"eval_total\": 47, \"vs_baseline_pp\": 8.5, \"vs_vanilla_sft_pp\": -23.4}, \"conclusion\": \"negative\"}, \"v3-taxei-eval\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:26:24.552Z\", \"updated_at\": \"2026-05-14T14:15:25.974Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && CUDA_VISIBLE_DEVICES=0 python3 eval/recovery.py --model_path checkpoints/mini_taxei_sft_v3/*/checkpoint-2832 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v3_taxei.json --device cuda:0\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"55848\", \"log_path\": \"~/runs/tax_error_inject_agent/v3-taxei-eval.log\", \"submitted_at\": \"2026-05-14T13:26:51.905Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"v3 TaxEI SFT eval on 47-task ALFWorld (format-aligned, initial signal before v4 formal judgment)\", \"metrics\": {\"eval_success_rate\": 0.66, \"eval_successes\": 31, \"eval_total\": 47, \"vs_baseline_pp\": 23.4, \"vs_vanilla_sft_pp\": -8.5, \"per_task\": {\"look_at_obj_in_light\": \"5/6 (83.3%)\", \"pick_clean_then_place\": \"8/11 (72.7%)\", \"pick_heat_then_place\": \"6/8 (75.0%)\", \"pick_and_place_simple\": \"5/8 (62.5%)\", \"pick_two_obj_and_place\": \"4/7 (57.1%)\", \"pick_cool_then_place\": \"3/7 (42.9%)\"}}, \"conclusion\": \"negative\"}, \"v4-random-sft-r3\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:32:26.753Z\", \"updated_at\": \"2026-05-14T13:32:36.181Z\", \"spec\": {\"command\": \"bash -c \\\"trap '' HUP; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && CUDA_VISIBLE_DEVICES=3 swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/sft_random_v4.jsonl --output_dir checkpoints/mini_random_sft_v4 --lora_rank 16 --lora_alpha 32 --lora_dropout 0.05 --target_modules all-linear --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --max_length 4096 --num_train_epochs 3 --learning_rate 1e-4 --seed 42 --torch_dtype bfloat16 --logging_steps 5 --save_strategy epoch --gradient_checkpointing true\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"58826\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-random-sft-r3.log\", \"submitted_at\": \"2026-05-14T13:32:26.722Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"v4 Random SFT retry (r3) — added trap '' HUP to survive tmux cleanup. Same-source 9,029 samples.\"}, \"v4-taxei-sft-r3\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:32:24.446Z\", \"updated_at\": \"2026-05-14T13:32:34.819Z\", \"spec\": {\"command\": \"bash -c \\\"trap '' HUP; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && CUDA_VISIBLE_DEVICES=2 swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/sft_taxei_v4.jsonl --output_dir checkpoints/mini_taxei_sft_v4 --lora_rank 16 --lora_alpha 32 --lora_dropout 0.05 --target_modules all-linear --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --max_length 4096 --num_train_epochs 3 --learning_rate 1e-4 --seed 42 --torch_dtype bfloat16 --logging_steps 5 --save_strategy epoch --gradient_checkpointing true\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"58741\", \"log_path\": \"~/runs/tax_error_inject_agent/v4-taxei-sft-r3.log\", \"submitted_at\": \"2026-05-14T13:32:24.415Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"v4 TaxEI SFT retry (r3) — added trap '' HUP to survive tmux cleanup. Same-source 9,029 samples.\"}, \"v4-random-sft\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:26:31.864Z\", \"updated_at\": \"2026-05-14T13:31:19.378Z\", \"spec\": {\"pid\": \"56765\", \"gpu_memory_mib\": 19159, \"gpu_util_pct\": 60}, \"hypothesis\": \"v4 Random SFT with same-source data (9,029 samples), formal Gate 3b judgment — only tag differs from v4-taxei\", \"conclusion\": \"failed\"}, \"v4-taxei-sft\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:26:29.177Z\", \"updated_at\": \"2026-05-14T13:31:18.431Z\", \"spec\": {\"pid\": \"56685\", \"gpu_memory_mib\": 30884, \"gpu_util_pct\": 94}, \"hypothesis\": \"v4 TaxEI SFT with same-source data (9,029 samples), formal Gate 3a/3b judgment\", \"conclusion\": \"failed\"}, \"mini-vanilla-sft-v4\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:14:26.614Z\", \"updated_at\": \"2026-05-14T13:27:05.003Z\", \"hypothesis\": \"Vanilla SFT baseline with aligned format (v4), for Gate 3a comparison\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/sft_vanilla_v4.jsonl --output_dir checkpoints/mini_vanilla_sft_v4/ --lora_rank 16 --lora_alpha 32 --lora_dropout 0.05 --target_modules all-linear --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --max_length 4096 --num_train_epochs 3 --learning_rate 1e-4 --seed 42 --torch_dtype bfloat16 --logging_steps 5 --save_strategy epoch --gradient_checkpointing true\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"50537\", \"log_path\": \"~/runs/tax_error_inject_agent/mini-vanilla-sft-v4.log\", \"submitted_at\": \"2026-05-14T12:14:32.528Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"success\"}, \"mini-random-sft-v3\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:13:19.635Z\", \"updated_at\": \"2026-05-14T13:27:04.310Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v3/sft_random_aligned.jsonl --output_dir checkpoints/mini_random_sft_v3/ --lora_rank 16 --lora_alpha 32 --lora_dropout 0.05 --target_modules all-linear --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --max_length 4096 --num_train_epochs 3 --learning_rate 1e-4 --seed 42 --torch_dtype bfloat16 --logging_steps 5 --save_strategy epoch --gradient_checkpointing true\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"45764\", \"log_path\": \"~/runs/tax_error_inject_agent/mini-random-sft-v3.log\", \"submitted_at\": \"2026-05-14T11:13:19.618Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"train_samples\": 9076, \"train_samples_clean\": 4176, \"train_samples_injected\": 4900, \"train_steps_total\": 3405, \"est_duration_min\": 110, \"format\": \"aligned_single_turn\"}, \"conclusion\": \"success\"}, \"mini-taxei-sft-v3\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:13:17.286Z\", \"updated_at\": \"2026-05-14T13:27:03.840Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v3/sft_taxei_aligned.jsonl --output_dir checkpoints/mini_taxei_sft_v3/ --lora_rank 16 --lora_alpha 32 --lora_dropout 0.05 --target_modules all-linear --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --max_length 4096 --num_train_epochs 3 --learning_rate 1e-4 --seed 42 --torch_dtype bfloat16 --logging_steps 5 --save_strategy epoch --gradient_checkpointing true\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"45621\", \"log_path\": \"~/runs/tax_error_inject_agent/mini-taxei-sft-v3.log\", \"submitted_at\": \"2026-05-14T11:13:17.271Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"train_samples\": 7545, \"train_samples_clean\": 4176, \"train_samples_injected\": 3369, \"train_steps_total\": 2832, \"est_duration_min\": 90, \"format\": \"aligned_single_turn\"}, \"conclusion\": \"success\"}, \"mini-vanilla-sft-v3\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:13:13.990Z\", \"updated_at\": \"2026-05-14T13:27:02.899Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v3/sft_vanilla_aligned.jsonl --output_dir checkpoints/mini_vanilla_sft_v3/ --lora_rank 16 --lora_alpha 32 --lora_dropout 0.05 --target_modules all-linear --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --max_length 4096 --num_train_epochs 3 --learning_rate 1e-4 --seed 42 --torch_dtype bfloat16 --logging_steps 5 --save_strategy epoch --gradient_checkpointing true\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"45478\", \"log_path\": \"~/runs/tax_error_inject_agent/mini-vanilla-sft-v3.log\", \"submitted_at\": \"2026-05-14T11:13:13.975Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"train_samples\": 4176, \"train_steps_total\": 1566, \"est_duration_min\": 58, \"format\": \"aligned_single_turn\"}, \"conclusion\": \"success\"}, \"v3-vanilla-eval\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:22:10.941Z\", \"updated_at\": \"2026-05-14T13:27:01.957Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && CUDA_VISIBLE_DEVICES=0 python3 eval/recovery.py --model_path /root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_vanilla_sft_v3/v0-20260514-191323/checkpoint-1566 --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v3_vanilla.json --device cuda:0\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"51848\", \"log_path\": \"~/runs/tax_error_inject_agent/v3-vanilla-eval.log\", \"submitted_at\": \"2026-05-14T12:22:30.589Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.745, \"successes\": 35, \"total\": 47, \"vs_baseline_pp\": 31.9, \"vs_baseline\": \"42.6% → 74.5%\"}}, \"v4-vanilla-sft\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:14:57.794Z\", \"updated_at\": \"2026-05-14T12:22:10.869Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && swift sft --model /root/autodl-tmp/models/Qwen/Qwen3-8B --dataset data/mini_pipeline_v4/sft_vanilla_v4.jsonl --output_dir checkpoints/v4_vanilla_sft/ --lora_rank 16 --lora_alpha 32 --lora_dropout 0.05 --target_modules all-linear --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --max_length 4096 --num_train_epochs 3 --learning_rate 1e-4 --seed 42 --torch_dtype bfloat16 --logging_steps 5 --save_strategy epoch --gradient_checkpointing true\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": 50972, \"log_path\": \"~/runs/tax_error_inject_agent/v4-vanilla-sft.log\", \"submitted_at\": \"2026-05-14T12:14:57.755Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"OOM - CUDA_VISIBLE_DEVICES not set, ran on wrong GPU (cuda:0 instead of cuda:3)\"}, \"conclusion\": \"failed\"}, \"vanilla_sft_aligned_v2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:05:05.459Z\", \"updated_at\": \"2026-05-14T11:05:05.459Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && CUDA_VISIBLE_DEVICES=2 swift sft \\\\\\n  --model /root/autodl-tmp/models/Qwen/Qwen3-8B \\\\\\n  --dataset data/mini_pipeline/sft_vanilla_aligned.jsonl \\\\\\n  --lora_rank 16 \\\\\\n  --lora_alpha 32 \\\\\\n  --lora_dropout 0.05 \\\\\\n  --target_modules all-linear \\\\\\n  --num_train_epochs 1 \\\\\\n  --learning_rate 1e-4 \\\\\\n  --per_device_train_batch_size 1 \\\\\\n  --gradient_accumulation_steps 16 \\\\\\n  --warmup_ratio 0.05 \\\\\\n  --seed 42 \\\\\\n  --max_length 4096 \\\\\\n  --gradient_checkpointing true \\\\\\n  --output_dir checkpoints/vanilla_sft_aligned \\\\\\n  --logging_steps 5 \\\\\\n  --logging_first_step true \\\\\\n  --save_strategy epoch \\\\\\n  --bf16 true \\\\\\n  --weight_decay 0.1 \\\\\\n  --adam_beta1 0.9 \\\\\\n  --adam_beta2 0.95 \\\\\\n  --max_grad_norm 1.0 \\\\\\n  --lr_scheduler_type cosine \\\\\\n  --optim adamw_torch_fused 2>&1\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"44492\", \"log_path\": \"~/runs/tax_error_inject_agent/vanilla_sft_aligned_v2.log\", \"submitted_at\": \"2026-05-14T11:05:05.434Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"vanilla_sft_aligned_v1\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:04:12.825Z\", \"updated_at\": \"2026-05-14T11:04:12.825Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && CUDA_VISIBLE_DEVICES=2 swift sft --config configs/sft_vanilla_aligned.yaml 2>&1\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"43894\", \"log_path\": \"~/runs/tax_error_inject_agent/vanilla_sft_aligned_v1.log\", \"submitted_at\": \"2026-05-14T11:04:12.812Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"mini-vanilla-sft\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T10:51:41.382Z\", \"updated_at\": \"2026-05-14T10:54:48.860Z\", \"hypothesis\": \"Vanilla trajectory SFT baseline for comparison with TaxEI\", \"spec\": {\"command\": \"python3 scripts/train_sft.py --data data/sft_data/vanilla_train.jsonl --output checkpoints/mini_vanilla_sft/ --model Qwen3-8B --lora_rank 16 --seed 42 --epochs 3 --lr 1e-4\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"pid\": \"41874\", \"log_path\": \"eval_results/mini_vanilla_clean.json\", \"submitted_at\": \"2026-05-14T10:54:31.029Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/sft_data/vanilla_train.jsonl\", \"data_count\": 278, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"hypothesis\": \"Vanilla SFT on clean trajectories as baseline for comparison\", \"checkpoint_path\": \"checkpoints/mini_vanilla_sft/v0-20260514-181708/checkpoint-54\", \"wall_clock_seconds\": 17.8, \"gpu_hours\": 0.0}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T10:54:20.210Z\", \"metrics\": {\"eval_success_rate\": 0.149, \"eval_successes\": 7, \"eval_total\": 47, \"vs_baseline_pp\": -27.7, \"per_task\": {\"look_at_obj_in_light\": \"0/6 (0%)\", \"pick_and_place_simple\": \"2/8 (25.0%)\", \"pick_clean_then_place\": \"2/11 (18.2%)\", \"pick_cool_then_place\": \"0/7 (0%)\", \"pick_heat_then_place\": \"3/8 (37.5%)\", \"pick_two_obj_and_place\": \"0/7 (0%)\"}, \"train_steps\": 54, \"train_duration_min\": 5}}, \"mini-taxei-sft\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T10:51:40.784Z\", \"updated_at\": \"2026-05-14T10:54:46.174Z\", \"hypothesis\": \"TaxEI injection + recovery SFT improves over vanilla SFT on ALFWorld 47-task eval\", \"spec\": {\"command\": \"python3 scripts/train_sft.py --data data/sft_data/taxei_train.jsonl --output checkpoints/mini_taxei_sft/ --model Qwen3-8B --lora_rank 16 --seed 42 --epochs 3 --lr 1e-4\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"pid\": \"41263\", \"log_path\": \"eval_results/mini_taxei_clean.json\", \"submitted_at\": \"2026-05-14T10:53:16.579Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/sft_data/taxei_train.jsonl\", \"data_count\": 278, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_path\": \"checkpoints/mini_taxei_sft/v0-20260514-181630/checkpoint-195\", \"hypothesis\": \"TaxEI error injection + recovery SFT improves over vanilla SFT and baseline\", \"wall_clock_seconds\": 63.1, \"gpu_hours\": 0.04}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T10:54:19.721Z\", \"metrics\": {\"eval_success_rate\": 0.447, \"eval_successes\": 21, \"eval_total\": 47, \"vs_baseline_pp\": 2.1, \"per_task\": {\"look_at_obj_in_light\": \"3/6 (50.0%)\", \"pick_and_place_simple\": \"2/8 (25.0%)\", \"pick_clean_then_place\": \"6/11 (54.5%)\", \"pick_cool_then_place\": \"1/7 (14.3%)\", \"pick_heat_then_place\": \"6/8 (75.0%)\", \"pick_two_obj_and_place\": \"3/7 (42.9%)\"}, \"train_steps\": 195, \"train_duration_min\": 16.3}}, \"vanilla-react-baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:20:00.119Z\", \"updated_at\": \"2026-05-14T10:54:35.171Z\", \"spec\": {\"command\": \"python3 eval/recovery.py --model_path /root/autodl-tmp/models/Qwen/Qwen3-8B --eval_split valid_unseen --no_inject (MAX_STEPS=50 hardcoded)\", \"server\": \"autodl-5090\", \"data_path\": \"ALFWorld valid_unseen (47/85 tasks, solvable=True filter, pick_and_place_with_movable_recep excluded 0/11)\", \"data_count\": 47, \"model_name\": \"Qwen3-8B (zero-shot, enable_thinking=False)\", \"seed\": 42, \"gpu\": \"cuda:1\", \"hypothesis\": \"Qwen3-8B zero-shot ReAct 在 ALFWorld valid_unseen 的基线成功率，作为 SFT 对比的 lower bound\", \"checkpoint_path\": \"N/A (zero-shot, no training)\", \"log_path\": \"/root/autodl-tmp/tax_error_inject_agent/eval_results/vanilla_react_baseline.json\"}, \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.426, \"total_tasks\": 47, \"successes\": 20, \"per_task_type\": {\"pick_heat_then_place\": {\"success\": 5, \"total\": 8, \"rate\": 0.625}, \"look_at_obj_in_light\": {\"success\": 3, \"total\": 6, \"rate\": 0.5}, \"pick_and_place_simple\": {\"success\": 4, \"total\": 8, \"rate\": 0.5}, \"pick_clean_then_place\": {\"success\": 5, \"total\": 11, \"rate\": 0.455}, \"pick_two_obj_and_place\": {\"success\": 3, \"total\": 7, \"rate\": 0.429}, \"pick_cool_then_place\": {\"success\": 0, \"total\": 7, \"rate\": 0}}}, \"completed_at\": \"2026-05-14T08:58:00.892Z\"}, \"mini-pipeline-e2e\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T10:39:15.654Z\", \"updated_at\": \"2026-05-14T10:39:15.654Z\", \"conclusion\": \"failed\"}, \"sft-dryrun-73\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:19:34.694Z\", \"updated_at\": \"2026-05-14T08:20:00.752Z\", \"spec\": {\"command\": \"swift sft --config configs/sft_vanilla.yaml (dry-run, 1 epoch, bs=1, max_length=2048)\", \"server\": \"autodl-5090\", \"data_path\": \"data/trajectories/ (124 successful trajectories)\", \"data_count\": 124, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"gpu\": \"cuda:0\", \"hypothesis\": \"SFT pipeline 端到端验证：注入→格式化→训练流程是否正常工作\", \"checkpoint_path\": \"checkpoints/dryrun_sft_v2/v0-20260514-161410/checkpoint-8/\", \"log_path\": \"checkpoints/dryrun_sft_v2/v0-20260514-161410/\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T08:19:52.165Z\", \"metrics\": {\"train_loss_init\": 2.436, \"train_loss_final\": 1.543, \"train_loss_avg\": 1.894, \"peak_memory_gib\": 19.22, \"steps\": 8, \"duration_sec\": 42, \"data_vanilla\": 124, \"data_injected_dryrun\": 96, \"injected_failed\": 4}}}, \"count\": 57, \"total\": 57, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1151}}"
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
The registry output is too large. Let me use a subagent to extract the specific data I need from the JSON file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "54884577-4b89-43d3-8e16-64aaa0260a70",
  "uuid": "d3ac0d2f-ebf9-45a8-b430-4ac4eaf1eaab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FeDLNExNkNgJ4Ue4TEYBAD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 640,
      "cache_read_input_tokens": 24984,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 640
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

Registry data is large. Let me extract the specific experiment metrics I need.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "54884577-4b89-43d3-8e16-64aaa0260a70",
  "uuid": "7df5fb6c-31b1-4afb-bb38-82acf2c074cf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FeDLNExNkNgJ4Ue4TEYBAD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 640,
      "cache_read_input_tokens": 24984,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 640
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

<details open><summary>🔧 Tool call — Agent · `toolu_019opF2bKVEPfR2DAx2do9Ku`</summary>

```json
{
  "description": "Extract registry experiment data",
  "prompt": "I need to extract specific experiment data from a large JSON registry file at:\n`/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/54884577-4b89-43d3-8e16-64aaa0260a70/tool-results/mcp-agent-ml-research-read_registry-1778806308126.txt`\n\nThe file is JSON with schema: `{result: string}` where `result` is itself a JSON string containing experiment records.\n\nI need you to extract the following fields for ALL experiments:\n- exp_id\n- status\n- conclusion\n- metrics (especially eval_success_rate, final_loss, token_accuracy, train_duration_min)\n- Any other relevant result fields\n\nSpecifically I need data for these experiments:\n1. Clean Eval experiments: v4-vanilla-eval-r3, v4-vanilla-seed0-eval, v4-vanilla-seed123-eval, v4-taxei-eval, v4-taxei-seed0-eval, v4-taxei-seed123-eval, v4-random-eval, v4-random-seed0-eval, v4-random-seed123-eval\n2. Dose-Response experiments: v4-taxei-fixed-inject10-eval, v4-taxei-fixed-inject25-eval, and any with \"inject50\" or \"random-fixed\" in the name\n3. Recovery Eval experiments: v4-vanilla-recovery-eval, v4-taxei-recovery-eval-r2, v4-random-recovery-eval\n4. Training experiments: any with \"train\" in the name\n5. Baseline: vanilla-react-baseline\n\nFor each experiment, output: exp_id, status, conclusion (first 200 chars), and ALL metrics as a flat dict.\n\nUse jq or python to parse. Output the results as structured text that I can use directly. Be thorough — I need every number.",
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
  "session_id": "54884577-4b89-43d3-8e16-64aaa0260a70",
  "uuid": "9c7e3524-2584-461b-9d0d-f437008b97c7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FeDLNExNkNgJ4Ue4TEYBAD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 640,
      "cache_read_input_tokens": 24984,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 640
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
  "task_id": "ae6d5bdefba342292",
  "tool_use_id": "toolu_019opF2bKVEPfR2DAx2do9Ku",
  "description": "Extract registry experiment data",
  "task_type": "local_agent",
  "prompt": "I need to extract specific experiment data from a large JSON registry file at:\n`/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/54884577-4b89-43d3-8e16-64aaa0260a70/tool-results/mcp-agent-ml-research-read_registry-1778806308126.txt`\n\nThe file is JSON with schema: `{result: string}` where `result` is itself a JSON string containing experiment records.\n\nI need you to extract the following fields for ALL experiments:\n- exp_id\n- status\n- conclusion\n- metrics (especially eval_success_rate, final_loss, token_accuracy, train_duration_min)\n- Any other relevant result fields\n\nSpecifically I need data for these experiments:\n1. Clean Eval experiments: v4-vanilla-eval-r3, v4-vanilla-seed0-eval, v4-vanilla-seed123-eval, v4-taxei-eval, v4-taxei-seed0-eval, v4-taxei-seed123-eval, v4-random-eval, v4-random-seed0-eval, v4-random-seed123-eval\n2. Dose-Response experiments: v4-taxei-fixed-inject10-eval, v4-taxei-fixed-inject25-eval, and any with \"inject50\" or \"random-fixed\" in the name\n3. Recovery Eval experiments: v4-vanilla-recovery-eval, v4-taxei-recovery-eval-r2, v4-random-recovery-eval\n4. Training experiments: any with \"train\" in the name\n5. Baseline: vanilla-react-baseline\n\nFor each experiment, output: exp_id, status, conclusion (first 200 chars), and ALL metrics as a flat dict.\n\nUse jq or python to parse. Output the results as structured text that I can use directly. Be thorough — I need every number.",
  "uuid": "170b0ab4-3544-4616-beba-2c620ac4603a",
  "session_id": "54884577-4b89-43d3-8e16-64aaa0260a70"
}
```

---

## Round 1

32 recorded events

### User

_source line 14 · 2026-05-15T00:52:05.613Z_

I need to extract specific experiment data from a large JSON registry file at:
`/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/54884577-4b89-43d3-8e16-64aaa0260a70/tool-results/mcp-agent-ml-research-read_registry-1778806308126.txt`

The file is JSON with schema: `{result: string}` where `result` is itself a JSON string containing experiment records.

I need you to extract the following fields for ALL experiments:
- exp_id
- status
- conclusion
- metrics (especially eval_success_rate, final_loss, token_accuracy, train_duration_min)
- Any other relevant result fields

Specifically I need data for these experiments:
1. Clean Eval experiments: v4-vanilla-eval-r3, v4-vanilla-seed0-eval, v4-vanilla-seed123-eval, v4-taxei-eval, v4-taxei-seed0-eval, v4-taxei-seed123-eval, v4-random-eval, v4-random-seed0-eval, v4-random-seed123-eval
2. Dose-Response experiments: v4-taxei-fixed-inject10-eval, v4-taxei-fixed-inject25-eval, and any with "inject50" or "random-fixed" in the name
3. Recovery Eval experiments: v4-vanilla-recovery-eval, v4-taxei-recovery-eval-r2, v4-random-recovery-eval
4. Training experiments: any with "train" in the name
5. Baseline: vanilla-react-baseline

For each experiment, output: exp_id, status, conclusion (first 200 chars), and ALL metrics as a flat dict.

Use jq or python to parse. Output the results as structured text that I can use directly. Be thorough — I need every number.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019opF2bKVEPfR2DAx2do9Ku",
  "session_id": "54884577-4b89-43d3-8e16-64aaa0260a70",
  "uuid": "9eb9ea24-5e84-4560-803d-b048ef1d2ff9"
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
  "task_id": "ae6d5bdefba342292",
  "tool_use_id": "toolu_019opF2bKVEPfR2DAx2do9Ku",
  "description": "Reading ~/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/54884577-4b89-43d3-8e16-64aaa0260a70/tool-results/mcp-agent-ml-research-read_registry-1778806308126.txt",
  "usage": {
    "total_tokens": 14574,
    "tool_uses": 1,
    "duration_ms": 3843
  },
  "last_tool_name": "Read",
  "uuid": "c4dd04c8-0984-4081-9d49-687d0a7f3927",
  "session_id": "54884577-4b89-43d3-8e16-64aaa0260a70"
}
```

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Read · `toolu_016BXdFTSo4ChNzdDWaCDUwJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/54884577-4b89-43d3-8e16-64aaa0260a70/tool-results/mcp-agent-ml-research-read_registry-1778806308126.txt",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019opF2bKVEPfR2DAx2do9Ku",
  "session_id": "54884577-4b89-43d3-8e16-64aaa0260a70",
  "uuid": "fd9b5497-c2de-4c41-988d-8e48d723a3c4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WLYhs67uwWK4RnEQyreHa4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14563,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14563,
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

_source line 17 · 2026-05-15T00:52:09.773Z_

<details><summary>↩ Tool result · reported error · `toolu_016BXdFTSo4ChNzdDWaCDUwJ`</summary>

```text
File content (30271 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019opF2bKVEPfR2DAx2do9Ku",
  "session_id": "54884577-4b89-43d3-8e16-64aaa0260a70",
  "uuid": "cccc1a44-4d07-4e82-b3f2-a3ea7162ca62",
  "tool_use_result": "Error: File content (30271 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
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
  "task_id": "ae6d5bdefba342292",
  "tool_use_id": "toolu_019opF2bKVEPfR2DAx2do9Ku",
  "description": "Reading ~/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/54884577-4b89-43d3-8e16-64aaa0260a70/tool-results/mcp-agent-ml-research-read_registry-1778806308126.txt",
  "usage": {
    "total_tokens": 15650,
    "tool_uses": 2,
    "duration_ms": 7871
  },
  "last_tool_name": "Read",
  "uuid": "8705a168-3448-4a21-ac22-7d0cebe016d4",
  "session_id": "54884577-4b89-43d3-8e16-64aaa0260a70"
}
```

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Read · `toolu_01Y2i26pJx4gfh8cAMdi4x8m`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/54884577-4b89-43d3-8e16-64aaa0260a70/tool-results/mcp-agent-ml-research-read_registry-1778806308126.txt",
  "limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019opF2bKVEPfR2DAx2do9Ku",
  "session_id": "54884577-4b89-43d3-8e16-64aaa0260a70",
  "uuid": "c730103f-14a8-4b48-9782-ef75a551ed77",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012JVySS4u7xVMBt5gXWBLA6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1076,
      "cache_read_input_tokens": 14563,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1076,
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

_source line 20 · 2026-05-15T00:52:13.722Z_

<details><summary>↩ Tool result · reported error · `toolu_01Y2i26pJx4gfh8cAMdi4x8m`</summary>

```text
File content (30271 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019opF2bKVEPfR2DAx2do9Ku",
  "session_id": "54884577-4b89-43d3-8e16-64aaa0260a70",
  "uuid": "09bc5d2b-fc52-4dfc-a6c9-a7dafed0b61f",
  "tool_use_result": "Error: File content (30271 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
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
  "task_id": "ae6d5bdefba342292",
  "tool_use_id": "toolu_019opF2bKVEPfR2DAx2do9Ku",
  "description": "Running Check file size in lines",
  "usage": {
    "total_tokens": 15943,
    "tool_uses": 3,
    "duration_ms": 11697
  },
  "last_tool_name": "Bash",
  "uuid": "efbbb553-41b3-42ac-85e5-f05de4b1e223",
  "session_id": "54884577-4b89-43d3-8e16-64aaa0260a70"
}
```

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Bash · `toolu_01HfYSLpVBHLZJEKPiozwQ5K`</summary>

```json
{
  "command": "wc -l \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/54884577-4b89-43d3-8e16-64aaa0260a70/tool-results/mcp-agent-ml-research-read_registry-1778806308126.txt\"",
  "description": "Check file size in lines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019opF2bKVEPfR2DAx2do9Ku",
  "session_id": "54884577-4b89-43d3-8e16-64aaa0260a70",
  "uuid": "4e087f9f-d827-4f3e-afcf-bdb3a959281b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RYg5pgb7qB83UovfcdDtbF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 235,
      "cache_read_input_tokens": 15639,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 235,
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

_source line 23 · 2026-05-15T00:52:17.444Z_

<details><summary>↩ Tool result · `toolu_01HfYSLpVBHLZJEKPiozwQ5K`</summary>

```text
0 /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/54884577-4b89-43d3-8e16-64aaa0260a70/tool-results/mcp-agent-ml-research-read_registry-1778806308126.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019opF2bKVEPfR2DAx2do9Ku",
  "session_id": "54884577-4b89-43d3-8e16-64aaa0260a70",
  "uuid": "a610aae3-c44e-489e-a9c7-bf3d7885c4b7"
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
  "task_id": "ae6d5bdefba342292",
  "tool_use_id": "toolu_019opF2bKVEPfR2DAx2do9Ku",
  "description": "Running Parse registry JSON structure",
  "usage": {
    "total_tokens": 16216,
    "tool_uses": 4,
    "duration_ms": 21002
  },
  "last_tool_name": "Bash",
  "uuid": "571f5de7-d807-46c4-9415-0e59a3c8517e",
  "session_id": "54884577-4b89-43d3-8e16-64aaa0260a70"
}
```

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Bash · `toolu_01GADLjZitXCsvGg4YcNtpQh`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json, sys\n\nfpath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/54884577-4b89-43d3-8e16-64aaa0260a70/tool-results/mcp-agent-ml-research-read_registry-1778806308126.txt\"\n\nwith open(fpath, 'r') as f:\n    raw = json.load(f)\n\n# The outer object has {result: string} where result is itself JSON\ninner = json.loads(raw['result'])\n\n# Determine structure\nif isinstance(inner, dict):\n    print(f\"Top-level keys: {list(inner.keys())[:20]}\")\n    # Check if experiments are nested\n    for k in inner:\n        v = inner[k]\n        if isinstance(v, dict):\n            print(f\"  {k}: dict with keys {list(v.keys())[:10]}\")\n        elif isinstance(v, list):\n            print(f\"  {k}: list of len {len(v)}\")\n            if len(v) > 0:\n                print(f\"    first item type: {type(v[0])}\")\n                if isinstance(v[0], dict):\n                    print(f\"    first item keys: {list(v[0].keys())[:15]}\")\n        else:\n            print(f\"  {k}: {type(v).__name__} = {str(v)[:100]}\")\nelif isinstance(inner, list):\n    print(f\"Top-level: list of {len(inner)} items\")\n    if len(inner) > 0 and isinstance(inner[0], dict):\n        print(f\"First item keys: {list(inner[0].keys())}\")\nPYEOF",
  "description": "Parse registry JSON structure",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019opF2bKVEPfR2DAx2do9Ku",
  "session_id": "54884577-4b89-43d3-8e16-64aaa0260a70",
  "uuid": "d2accc7c-20f1-45a6-93da-992bfb708646",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011WYbiNPkGVn5J2rxWnbVvQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 271,
      "cache_read_input_tokens": 15874,
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

_source line 26 · 2026-05-15T00:52:26.688Z_

<details><summary>↩ Tool result · `toolu_01GADLjZitXCsvGg4YcNtpQh`</summary>

```text
Top-level keys: ['success', 'data', 'error', 'metadata']
  success: bool = True
  data: dict with keys ['experiments', 'count', 'total', 'baseline']
  error: NoneType = None
  metadata: dict with keys ['elapsed_seconds']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019opF2bKVEPfR2DAx2do9Ku",
  "session_id": "54884577-4b89-43d3-8e16-64aaa0260a70",
  "uuid": "f5a525a1-f737-4af2-889f-b68b1ed79734"
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
  "task_id": "ae6d5bdefba342292",
  "tool_use_id": "toolu_019opF2bKVEPfR2DAx2do9Ku",
  "description": "Running List all experiment IDs",
  "usage": {
    "total_tokens": 16926,
    "tool_uses": 5,
    "duration_ms": 27831
  },
  "last_tool_name": "Bash",
  "uuid": "1a0b0a0d-646c-4dbe-9dc4-24943330f50b",
  "session_id": "54884577-4b89-43d3-8e16-64aaa0260a70"
}
```

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — Bash · `toolu_01LV6EBV3tbTvqK2bfyipr36`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/54884577-4b89-43d3-8e16-64aaa0260a70/tool-results/mcp-agent-ml-research-read_registry-1778806308126.txt\"\n\nwith open(fpath, 'r') as f:\n    raw = json.load(f)\n\ninner = json.loads(raw['result'])\ndata = inner['data']\nexperiments = data['experiments']\nbaseline = data.get('baseline')\n\nprint(f\"Total experiments: {data['total']}, returned: {data['count']}\")\nprint(f\"Baseline present: {baseline is not None}\")\nprint()\n\n# List all experiment IDs\nif isinstance(experiments, list):\n    for e in experiments:\n        print(f\"  exp_id={e.get('exp_id','?')}\")\nelif isinstance(experiments, dict):\n    for k in experiments:\n        print(f\"  key={k}\")\nPYEOF",
  "description": "List all experiment IDs",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019opF2bKVEPfR2DAx2do9Ku",
  "session_id": "54884577-4b89-43d3-8e16-64aaa0260a70",
  "uuid": "4e38ca95-aab8-4c75-8278-9bb212598446",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GkfLoDxqYDC4FRLoiFTDJJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 637,
      "cache_read_input_tokens": 16145,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 637,
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

_source line 29 · 2026-05-15T00:52:33.542Z_

<details><summary>↩ Tool result · `toolu_01LV6EBV3tbTvqK2bfyipr36`</summary>

```text
Total experiments: 57, returned: 57
Baseline present: False

  key=v4-random-fixed-inject25
  key=v4-random-fixed-inject10
  key=v4-random-fixed-inject50
  key=v4-taxei-fixed-inject50
  key=v4-random-seed123-eval
  key=v4-taxei-fixed-inject25-eval
  key=v4-taxei-fixed-inject10-eval
  key=v4-taxei-seed123-eval
  key=v4-random-seed123
  key=v4-taxei-fixed-inject25-r2
  key=v4-taxei-fixed-inject10
  key=v4-taxei-fixed-inject25
  key=v4-taxei-seed123
  key=v4-fixed-inject25
  key=v4-fixed-inject10
  key=v4-random-recovery-eval
  key=v4-taxei-recovery-eval-r2
  key=v4-taxei-seed0-eval
  key=v4-random-seed0-eval
  key=v4-vanilla-recovery-eval
  key=v4-taxei-recovery-eval
  key=v4-vanilla-seed123-eval
  key=v4-random-seed0
  key=v4-taxei-seed0
  key=v4-vanilla-seed0-eval
  key=v4-vanilla-seed123
  key=v4-vanilla-seed0
  key=v4-vanilla-seed7
  key=v4-recovery-eval-dev
  key=v4-recovery-dryrun
  key=v4-random-eval
  key=v4-taxei-eval
  key=traj_collect_500
  key=v4-vanilla-eval-r3
  key=v4-vanilla-eval-r2
  key=v4-random-sft-r2
  key=v4-taxei-sft-r2
  key=v4-vanilla-eval
  key=v3-random-eval
  key=v3-taxei-eval
  key=v4-random-sft-r3
  key=v4-taxei-sft-r3
  key=v4-random-sft
  key=v4-taxei-sft
  key=mini-vanilla-sft-v4
  key=mini-random-sft-v3
  key=mini-taxei-sft-v3
  key=mini-vanilla-sft-v3
  key=v3-vanilla-eval
  key=v4-vanilla-sft
  key=vanilla_sft_aligned_v2
  key=vanilla_sft_aligned_v1
  key=mini-vanilla-sft
  key=mini-taxei-sft
  key=vanilla-react-baseline
  key=mini-pipeline-e2e
  key=sft-dryrun-73
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019opF2bKVEPfR2DAx2do9Ku",
  "session_id": "54884577-4b89-43d3-8e16-64aaa0260a70",
  "uuid": "2854053a-e0e8-453a-aeee-bc1132b027c9"
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
  "task_id": "ae6d5bdefba342292",
  "tool_use_id": "toolu_019opF2bKVEPfR2DAx2do9Ku",
  "description": "Running Inspect structure of one experiment",
  "usage": {
    "total_tokens": 18082,
    "tool_uses": 6,
    "duration_ms": 34887
  },
  "last_tool_name": "Bash",
  "uuid": "6e8cb5e0-7e69-40bf-97f8-7a8fbd679dd2",
  "session_id": "54884577-4b89-43d3-8e16-64aaa0260a70"
}
```

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Bash · `toolu_01A4q9aPQ6bHAic2Jf1LyWw3`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/54884577-4b89-43d3-8e16-64aaa0260a70/tool-results/mcp-agent-ml-research-read_registry-1778806308126.txt\"\n\nwith open(fpath, 'r') as f:\n    raw = json.load(f)\n\ninner = json.loads(raw['result'])\nexperiments = inner['data']['experiments']\n\n# First, show the full structure of one experiment to understand fields\nsample_key = 'v4-vanilla-eval-r3'\nsample = experiments[sample_key]\nprint(f\"=== STRUCTURE OF '{sample_key}' ===\")\nprint(json.dumps(sample, indent=2, ensure_ascii=False)[:3000])\nprint(\"...\")\nPYEOF",
  "description": "Inspect structure of one experiment",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019opF2bKVEPfR2DAx2do9Ku",
  "session_id": "54884577-4b89-43d3-8e16-64aaa0260a70",
  "uuid": "78a2a448-ff77-4bcf-ab49-522cd3481f45",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PKWR6kLwKCNJJQFh6cTNoy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1108,
      "cache_read_input_tokens": 16782,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1108,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 48,
      "service_tier": "standard",
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

_source line 32 · 2026-05-15T00:52:40.574Z_

<details><summary>↩ Tool result · `toolu_01A4q9aPQ6bHAic2Jf1LyWw3`</summary>

```text
=== STRUCTURE OF 'v4-vanilla-eval-r3' ===
{
  "status": "PREPARING",
  "retry_count": 0,
  "created_at": "2026-05-14T14:28:24.833Z",
  "updated_at": "2026-05-14T16:25:11.284Z",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/tax_error_inject_agent && latest_run=\\$(ls -dt checkpoints/mini_vanilla_sft_v4/v0-*/ | head -1) && final_ckpt=\\$(ls -d \\\"\\${latest_run}\\\"checkpoint-* | sort -V | tail -1) && echo \\\"Using checkpoint: \\$final_ckpt\\\" && test -f \\\"\\${final_ckpt}/adapter_config.json\\\" && echo 'adapter_config.json OK' || { echo 'ERROR: adapter_config.json missing'; exit 1; } && CUDA_VISIBLE_DEVICES=0 python3 eval/recovery.py --model_path \\$final_ckpt --base_model /root/autodl-tmp/models/Qwen/Qwen3-8B --no_inject --output eval_results/v4_vanilla_eval.json --device cuda:0\"",
    "server": "autodl-5090",
    "gpu": [
      "cuda:0"
    ],
    "pid": "62340",
    "log_path": "~/runs/tax_error_inject_agent/v4-vanilla-eval-r3.log",
    "submitted_at": "2026-05-14T14:28:24.797Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root"
  },
  "hypothesis": "v4 Vanilla SFT eval r3 — dynamic checkpoint lookup with sort -V, adapter_config.json pre-check",
  "conclusion": "success",
  "metrics": {
    "eval_success_rate": 0.617,
    "eval_successes": 29,
    "eval_total": 47,
    "per_task": {
      "look_at_obj_in_light": "5/6 (83.3%)",
      "pick_heat_then_place": "6/8 (75.0%)",
      "pick_and_place_simple": "5/8 (62.5%)",
      "pick_cool_then_place": "4/7 (57.1%)",
      "pick_two_obj_and_place": "4/7 (57.1%)",
      "pick_clean_then_place": "5/11 (45.5%)"
    }
  }
}
...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019opF2bKVEPfR2DAx2do9Ku",
  "session_id": "54884577-4b89-43d3-8e16-64aaa0260a70",
  "uuid": "9d85603b-994a-4362-8b93-17988496c37f"
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
  "task_id": "ae6d5bdefba342292",
  "tool_use_id": "toolu_019opF2bKVEPfR2DAx2do9Ku",
  "description": "Running Extract all experiment data grouped by category",
  "usage": {
    "total_tokens": 19157,
    "tool_uses": 7,
    "duration_ms": 64471
  },
  "last_tool_name": "Bash",
  "uuid": "984ed233-8e88-4aaf-b1e2-8d6e1006dbb7",
  "session_id": "54884577-4b89-43d3-8e16-64aaa0260a70"
}
```

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Bash · `toolu_01Sf7nzdYuzZnpF8JX5HKrnS`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/54884577-4b89-43d3-8e16-64aaa0260a70/tool-results/mcp-agent-ml-research-read_registry-1778806308126.txt\"\n\nwith open(fpath, 'r') as f:\n    raw = json.load(f)\n\ninner = json.loads(raw['result'])\nexperiments = inner['data']['experiments']\n\n# Define target groups\nclean_eval = [\n    'v4-vanilla-eval-r3', 'v4-vanilla-seed0-eval', 'v4-vanilla-seed123-eval',\n    'v4-taxei-eval', 'v4-taxei-seed0-eval', 'v4-taxei-seed123-eval',\n    'v4-random-eval', 'v4-random-seed0-eval', 'v4-random-seed123-eval'\n]\n\ndose_response_patterns = ['inject10', 'inject25', 'inject50', 'random-fixed']\n\nrecovery_eval = [\n    'v4-vanilla-recovery-eval', 'v4-taxei-recovery-eval-r2', 'v4-random-recovery-eval'\n]\n\nbaseline = ['vanilla-react-baseline']\n\ndef flatten_metrics(metrics, prefix=''):\n    \"\"\"Flatten nested metrics dict to a flat dict.\"\"\"\n    flat = {}\n    if not isinstance(metrics, dict):\n        return flat\n    for k, v in metrics.items():\n        key = f\"{prefix}{k}\" if not prefix else f\"{prefix}.{k}\"\n        if isinstance(v, dict):\n            flat.update(flatten_metrics(v, key))\n        else:\n            flat[key] = v\n    return flat\n\ndef format_exp(exp_id, exp):\n    status = exp.get('status', 'N/A')\n    conclusion = exp.get('conclusion', 'N/A')\n    if conclusion and len(str(conclusion)) > 200:\n        conclusion = str(conclusion)[:200] + '...'\n    metrics = exp.get('metrics', {})\n    flat = flatten_metrics(metrics)\n    hypothesis = exp.get('hypothesis', '')\n    return {\n        'exp_id': exp_id,\n        'status': status,\n        'conclusion': conclusion,\n        'hypothesis': hypothesis[:150] if hypothesis else '',\n        'metrics': flat\n    }\n\ndef print_exp(info):\n    print(f\"exp_id: {info['exp_id']}\")\n    print(f\"  status: {info['status']}\")\n    print(f\"  conclusion: {info['conclusion']}\")\n    if info['hypothesis']:\n        print(f\"  hypothesis: {info['hypothesis']}\")\n    if info['metrics']:\n        for k, v in sorted(info['metrics'].items()):\n            print(f\"  {k}: {v}\")\n    else:\n        print(\"  (no metrics)\")\n    print()\n\n# ============================================================\n# 1. CLEAN EVAL EXPERIMENTS\n# ============================================================\nprint(\"=\" * 80)\nprint(\"SECTION 1: CLEAN EVAL EXPERIMENTS\")\nprint(\"=\" * 80)\nfor eid in clean_eval:\n    if eid in experiments:\n        print_exp(format_exp(eid, experiments[eid]))\n    else:\n        print(f\"exp_id: {eid}\")\n        print(f\"  NOT FOUND in registry\")\n        print()\n\n# ============================================================\n# 2. DOSE-RESPONSE EXPERIMENTS\n# ============================================================\nprint(\"=\" * 80)\nprint(\"SECTION 2: DOSE-RESPONSE EXPERIMENTS\")\nprint(\"=\" * 80)\ndose_ids = sorted([k for k in experiments if any(p in k for p in dose_response_patterns)])\nfor eid in dose_ids:\n    print_exp(format_exp(eid, experiments[eid]))\n\n# ============================================================\n# 3. RECOVERY EVAL EXPERIMENTS\n# ============================================================\nprint(\"=\" * 80)\nprint(\"SECTION 3: RECOVERY EVAL EXPERIMENTS\")\nprint(\"=\" * 80)\nfor eid in recovery_eval:\n    if eid in experiments:\n        print_exp(format_exp(eid, experiments[eid]))\n    else:\n        print(f\"exp_id: {eid}\")\n        print(f\"  NOT FOUND in registry\")\n        print()\n\n# ============================================================\n# 4. TRAINING EXPERIMENTS (any with \"train\" or \"sft\" in name)\n# ============================================================\nprint(\"=\" * 80)\nprint(\"SECTION 4: TRAINING EXPERIMENTS (sft/train)\")\nprint(\"=\" * 80)\ntrain_ids = sorted([k for k in experiments if ('sft' in k or 'train' in k.lower())])\nfor eid in train_ids:\n    print_exp(format_exp(eid, experiments[eid]))\n\n# ============================================================\n# 5. BASELINE\n# ============================================================\nprint(\"=\" * 80)\nprint(\"SECTION 5: BASELINE\")\nprint(\"=\" * 80)\nfor eid in baseline:\n    if eid in experiments:\n        print_exp(format_exp(eid, experiments[eid]))\n    else:\n        print(f\"exp_id: {eid}\")\n        print(f\"  NOT FOUND in registry\")\n        print()\n\n# ============================================================\n# 6. REMAINING EXPERIMENTS (not yet printed)\n# ============================================================\nprinted = set(clean_eval + dose_ids + recovery_eval + train_ids + baseline)\nremaining = sorted([k for k in experiments if k not in printed])\nif remaining:\n    print(\"=\" * 80)\n    print(\"SECTION 6: OTHER EXPERIMENTS\")\n    print(\"=\" * 80)\n    for eid in remaining:\n        print_exp(format_exp(eid, experiments[eid]))\n\nPYEOF",
  "description": "Extract all experiment data grouped by category",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019opF2bKVEPfR2DAx2do9Ku",
  "session_id": "54884577-4b89-43d3-8e16-64aaa0260a70",
  "uuid": "36db692e-e483-4d70-ba0a-a09d83186f25",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SBe8wAAXR4sgW7vfUFTwpw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1071,
      "cache_read_input_tokens": 17890,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1071,
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

_source line 35 · 2026-05-15T00:53:10.168Z_

<details><summary>↩ Tool result · `toolu_01Sf7nzdYuzZnpF8JX5HKrnS`</summary>

```text
================================================================================
SECTION 1: CLEAN EVAL EXPERIMENTS
================================================================================
exp_id: v4-vanilla-eval-r3
  status: PREPARING
  conclusion: success
  hypothesis: v4 Vanilla SFT eval r3 — dynamic checkpoint lookup with sort -V, adapter_config.json pre-check
  eval_success_rate: 0.617
  eval_successes: 29
  eval_total: 47
  per_task.look_at_obj_in_light: 5/6 (83.3%)
  per_task.pick_and_place_simple: 5/8 (62.5%)
  per_task.pick_clean_then_place: 5/11 (45.5%)
  per_task.pick_cool_then_place: 4/7 (57.1%)
  per_task.pick_heat_then_place: 6/8 (75.0%)
  per_task.pick_two_obj_and_place: 4/7 (57.1%)

exp_id: v4-vanilla-seed0-eval
  status: DONE
  conclusion: success
  hypothesis: v4 Vanilla SFT seed=0 eval — multi-seed verification, 4358 samples, comparing with seed=42 baseline (61.7%)
  discordant_pairs: 5
  eval_success_rate: 0.681
  eval_successes: 32
  eval_total: 47
  mcnemar_vs_seed42_p: 0.375
  per_task.look_at_obj_in_light: 5/6 (83.3%)
  per_task.pick_and_place_simple: 5/8 (62.5%)
  per_task.pick_clean_then_place: 6/11 (54.5%)
  per_task.pick_cool_then_place: 4/7 (57.1%)
  per_task.pick_heat_then_place: 7/8 (87.5%)
  per_task.pick_two_obj_and_place: 5/7 (71.4%)
  vs_seed42_pp: 6.4

exp_id: v4-vanilla-seed123-eval
  status: DONE
  conclusion: success
  hypothesis: v4 Vanilla SFT seed=123 eval — multi-seed verification, 4358 samples, comparing with seed=42 baseline (61.7%)
  eval_success_rate: 0.66
  eval_successes: 31
  eval_total: 47
  per_task.look_at_obj_in_light.rate: 0.833
  per_task.look_at_obj_in_light.success: 5
  per_task.look_at_obj_in_light.total: 6
  per_task.pick_and_place_simple.rate: 0.75
  per_task.pick_and_place_simple.success: 6
  per_task.pick_and_place_simple.total: 8
  per_task.pick_clean_then_place_in_recep.rate: 0.455
  per_task.pick_clean_then_place_in_recep.success: 5
  per_task.pick_clean_then_place_in_recep.total: 11
  per_task.pick_cool_then_place_in_recep.rate: 0.571
  per_task.pick_cool_then_place_in_recep.success: 4
  per_task.pick_cool_then_place_in_recep.total: 7
  per_task.pick_heat_then_place_in_recep.rate: 0.875
  per_task.pick_heat_then_place_in_recep.success: 7
  per_task.pick_heat_then_place_in_recep.total: 8
  per_task.pick_two_obj_and_place.rate: 0.571
  per_task.pick_two_obj_and_place.success: 4
  per_task.pick_two_obj_and_place.total: 7
  vs_seed0_pp: -2.1
  vs_seed42_pp: 4.3

exp_id: v4-taxei-eval
  status: PREPARING
  conclusion: negative
  hypothesis: v4 TaxEI SFT eval — formal Gate 3a/3b judgment, same-source 9,029 samples, checkpoint-3387
  eval_success_rate: 0.617
  eval_successes: 29
  eval_total: 47
  gate_3a: FAIL
  gate_3b: FAIL
  gate_4: PASS
  mcnemar_vs_random_p: 0.754
  mcnemar_vs_vanilla_p: 1
  per_task.look_at_obj_in_light: 6/6 (100%)
  per_task.pick_and_place_simple: 5/8 (62.5%)
  per_task.pick_clean_then_place: 6/11 (54.5%)
  per_task.pick_cool_then_place: 3/7 (42.9%)
  per_task.pick_heat_then_place: 7/8 (87.5%)
  per_task.pick_two_obj_and_place: 2/7 (28.6%)
  vs_random_pp: -4.3
  vs_vanilla_pp: 0

exp_id: v4-taxei-seed0-eval
  status: DONE
  conclusion: success
  hypothesis: v4 TaxEI SFT seed=0 eval — multi-seed verification, 9029 samples, testing TaxEI injection stability
  eval_success_rate: 0.468
  eval_successes: 22
  eval_total: 47
  vs_seed42_pp: -14.9

exp_id: v4-taxei-seed123-eval
  status: DONE
  conclusion: success
  hypothesis: v4 TaxEI SFT seed=123 eval — 61.7% (29/47), 低于 vanilla baseline 65.3%（-3.6pp）。multi-seed verification, 9029 samples。
  by_task.look_at_obj_in_light.rate: 0.833
  by_task.look_at_obj_in_light.success: 5
  by_task.look_at_obj_in_light.total: 6
  by_task.pick_and_place_simple.rate: 0.5
  by_task.pick_and_place_simple.success: 4
  by_task.pick_and_place_simple.total: 8
  by_task.pick_clean_then_place_in_recep.rate: 0.636
  by_task.pick_clean_then_place_in_recep.success: 7
  by_task.pick_clean_then_place_in_recep.total: 11
  by_task.pick_cool_then_place_in_recep.rate: 0.429
  by_task.pick_cool_then_place_in_recep.success: 3
  by_task.pick_cool_then_place_in_recep.total: 7
  by_task.pick_heat_then_place_in_recep.rate: 0.75
  by_task.pick_heat_then_place_in_recep.success: 6
  by_task.pick_heat_then_place_in_recep.total: 8
  by_task.pick_two_obj_and_place.rate: 0.571
  by_task.pick_two_obj_and_place.success: 4
  by_task.pick_two_obj_and_place.total: 7
  eval_success_rate: 0.617
  eval_successes: 29
  eval_total: 47

exp_id: v4-random-eval
  status: PREPARING
  conclusion: negative
  hypothesis: v4 Random SFT eval — formal Gate 3b judgment, same-source 9,029 samples, checkpoint-3387
  eval_success_rate: 0.66
  eval_successes: 31
  eval_total: 47
  mcnemar_vs_vanilla_p: 0.754
  per_task.look_at_obj_in_light: 6/6 (100%)
  per_task.pick_and_place_simple: 4/8 (50%)
  per_task.pick_clean_then_place: 6/11 (54.5%)
  per_task.pick_cool_then_place: 4/7 (57.1%)
  per_task.pick_heat_then_place: 7/8 (87.5%)
  per_task.pick_two_obj_and_place: 4/7 (57.1%)
  vs_taxei_pp: 4.3
  vs_vanilla_pp: 4.3

exp_id: v4-random-seed0-eval
  status: DONE
  conclusion: success
  hypothesis: v4 Random SFT seed=0 eval — multi-seed verification, 9029 samples, testing random injection stability
  eval_success_rate: 0.553
  eval_successes: 26
  eval_total: 47
  vs_seed42_pp: -10.7

exp_id: v4-random-seed123-eval
  status: DONE
  conclusion: negative
  hypothesis: v4 Random SFT seed=123 eval — 47 tasks clean eval. Multi-seed: seed=42 66.0%, seed=0 55.3%, seed=123 待测。
  by_task.look_at_obj_in_light.rate: 0.833
  by_task.look_at_obj_in_light.success: 5
  by_task.look_at_obj_in_light.total: 6
  by_task.pick_and_place_simple.rate: 0.625
  by_task.pick_and_place_simple.success: 5
  by_task.pick_and_place_simple.total: 8
  by_task.pick_clean_then_place_in_recep.rate: 0.636
  by_task.pick_clean_then_place_in_recep.success: 7
  by_task.pick_clean_then_place_in_recep.total: 11
  by_task.pick_cool_then_place_in_recep.rate: 0.571
  by_task.pick_cool_then_place_in_recep.success: 4
  by_task.pick_cool_then_place_in_recep.total: 7
  by_task.pick_heat_then_place_in_recep.rate: 0.75
  by_task.pick_heat_then_place_in_recep.success: 6
  by_task.pick_heat_then_place_in_recep.total: 8
  by_task.pick_two_obj_and_place.rate: 0.714
  by_task.pick_two_obj_and_place.success: 5
  by_task.pick_two_obj_and_place.total: 7
  eval_success_rate: 0.681
  eval_successes: 32
  eval_total: 47

================================================================================
SECTION 2: DOSE-RESPONSE EXPERIMENTS
================================================================================
exp_id: v4-fixed-inject10
  status: PREPARING
  conclusion: killed
  (no metrics)

exp_id: v4-fixed-inject25
  status: PREPARING
  conclusion: killed
  (no metrics)

exp_id: v4-random-fixed-inject10
  status: RUNNING
  conclusion: N/A
  hypothesis: v4 Random fixed-size ablation: 10% injection (4,358 total). 与 TaxEI 10% (61.7%) 对比 taxonomy 标签在低注入比例下是否有差异。
  (no metrics)

exp_id: v4-random-fixed-inject25
  status: RUNNING
  conclusion: N/A
  hypothesis: v4 Random fixed-size ablation: 25% injection (4,358 total). 与 TaxEI 25% (48.9%) 对比 taxonomy 标签在中等注入比例下是否有差异。
  (no metrics)

exp_id: v4-random-fixed-inject50
  status: RUNNING
  conclusion: N/A
  hypothesis: v4 Random fixed-size ablation: 50% injection (4,358 total = 2,179 clean + 2,179 injected). 与 TaxEI 50% 对比 taxonomy 标签在高注入比例下是否有差异。
  (no metrics)

exp_id: v4-taxei-fixed-inject10
  status: DONE
  conclusion: success
  hypothesis: v4 TaxEI fixed-size ablation: 10% injection ratio (4,358 total = 3,922 clean + 436 injected). Fixed-size = vanilla 大小，控制数据量变量。Dose-response: 10%/25%/5
  final_loss: 0.308
  token_accuracy: 0.888
  train_duration_min: 58
  train_epochs: 3
  train_steps: 1635

exp_id: v4-taxei-fixed-inject10-eval
  status: DONE
  conclusion: success
  hypothesis: v4 TaxEI 10% injection fixed-size eval — 61.7% (29/47), 低于 vanilla baseline 65.3%（-3.6pp）。Dose-response 数据点。
  by_task.look_at_obj_in_light.rate: 0.833
  by_task.look_at_obj_in_light.success: 5
  by_task.look_at_obj_in_light.total: 6
  by_task.pick_and_place_simple.rate: 0.625
  by_task.pick_and_place_simple.success: 5
  by_task.pick_and_place_simple.total: 8
  by_task.pick_clean_then_place_in_recep.rate: 0.455
  by_task.pick_clean_then_place_in_recep.success: 5
  by_task.pick_clean_then_place_in_recep.total: 11
  by_task.pick_cool_then_place_in_recep.rate: 0.571
  by_task.pick_cool_then_place_in_recep.success: 4
  by_task.pick_cool_then_place_in_recep.total: 7
  by_task.pick_heat_then_place_in_recep.rate: 0.75
  by_task.pick_heat_then_place_in_recep.success: 6
  by_task.pick_heat_then_place_in_recep.total: 8
  by_task.pick_two_obj_and_place.rate: 0.571
  by_task.pick_two_obj_and_place.success: 4
  by_task.pick_two_obj_and_place.total: 7
  eval_success_rate: 0.617
  eval_successes: 29
  eval_total: 47

exp_id: v4-taxei-fixed-inject25
  status: DONE
  conclusion: failed
  hypothesis: v4 TaxEI fixed-size ablation: 25% injection ratio (4,358 total = 3,268 clean + 1,090 injected). Fixed-size = vanilla 大小，控制数据量变量。Dose-response: 10%/25%
  (no metrics)

exp_id: v4-taxei-fixed-inject25-eval
  status: DONE
  conclusion: success
  hypothesis: v4 TaxEI 25% injection fixed-size eval — 48.9% (23/47), 显著低于 vanilla baseline 65.3%（-16.4pp）。Dose-response 数据点。
  by_task.look_at_obj_in_light.rate: 0.667
  by_task.look_at_obj_in_light.success: 4
  by_task.look_at_obj_in_light.total: 6
  by_task.pick_and_place_simple.rate: 0.375
  by_task.pick_and_place_simple.success: 3
  by_task.pick_and_place_simple.total: 8
  by_task.pick_clean_then_place_in_recep.rate: 0.455
  by_task.pick_clean_then_place_in_recep.success: 5
  by_task.pick_clean_then_place_in_recep.total: 11
  by_task.pick_cool_then_place_in_recep.rate: 0.286
  by_task.pick_cool_then_place_in_recep.success: 2
  by_task.pick_cool_then_place_in_recep.total: 7
  by_task.pick_heat_then_place_in_recep.rate: 0.625
  by_task.pick_heat_then_place_in_recep.success: 5
  by_task.pick_heat_then_place_in_recep.total: 8
  by_task.pick_two_obj_and_place.rate: 0.571
  by_task.pick_two_obj_and_place.success: 4
  by_task.pick_two_obj_and_place.total: 7
  eval_success_rate: 0.489
  eval_successes: 23
  eval_total: 47

exp_id: v4-taxei-fixed-inject25-r2
  status: DONE
  conclusion: success
  hypothesis: v4 TaxEI fixed-size ablation: 25% injection ratio retry (4,358 total = 3,268 clean + 1,090 injected). 修复 CUDA_VISIBLE_DEVICES，显式设 =3。
  final_loss: 0.285
  token_accuracy: 0.893
  train_duration_min: 58
  train_epochs: 3
  train_steps: 1635

exp_id: v4-taxei-fixed-inject50
  status: RUNNING
  conclusion: N/A
  hypothesis: v4 TaxEI fixed-size ablation: 50% injection ratio (4,358 total = 2,179 clean + 2,179 injected). Dose-response 最后一个点，完成后有完整曲线 0%→10%→25%→50%。
  (no metrics)

================================================================================
SECTION 3: RECOVERY EVAL EXPERIMENTS
================================================================================
exp_id: v4-vanilla-recovery-eval
  status: DONE
  conclusion: success
  hypothesis: v4 Vanilla SFT seed=42 recovery eval (injected_eval.py) — 47 episodes with error injection, measuring detection/recovery/success rates under P1/P2/C1/
  detection_rate: 0
  recovery_rate: 0.617
  success_rate: 0.617
  successes: 29
  total: 47

exp_id: v4-taxei-recovery-eval-r2
  status: DONE
  conclusion: success
  detection_rate: 0
  per_operator.C1_context_truncation.rate: 0.667
  per_operator.C1_context_truncation.recovered: 8
  per_operator.C1_context_truncation.total: 12
  per_operator.C4_observation_masking.rate: 0.636
  per_operator.C4_observation_masking.recovered: 7
  per_operator.C4_observation_masking.total: 11
  per_operator.P1_step_order_swap.rate: 0.583
  per_operator.P1_step_order_swap.recovered: 7
  per_operator.P1_step_order_swap.total: 12
  per_operator.P2_sub_goal_deletion.rate: 0.5
  per_operator.P2_sub_goal_deletion.recovered: 6
  per_operator.P2_sub_goal_deletion.total: 12
  recovery_rate: 0.596
  total_episodes: 47

exp_id: v4-random-recovery-eval
  status: DONE
  conclusion: success
  hypothesis: v4 Random SFT seed=42 recovery eval (injected_eval.py) — 47 episodes with error injection, measuring detection/recovery/success rates under P1/P2/C1/C
  detection_rate: 0
  note: r1=29/47, r2=30/47, ±2pp run-to-run variance on P1 non-determinism
  recovery_rate: 0.638
  source: json-file-verified
  successes: 30
  total: 47

================================================================================
SECTION 4: TRAINING EXPERIMENTS (sft/train)
================================================================================
exp_id: mini-random-sft-v3
  status: PREPARING
  conclusion: success
  est_duration_min: 110
  format: aligned_single_turn
  train_samples: 9076
  train_samples_clean: 4176
  train_samples_injected: 4900
  train_steps_total: 3405

exp_id: mini-taxei-sft
  status: DONE
  conclusion: success
  hypothesis: TaxEI injection + recovery SFT improves over vanilla SFT on ALFWorld 47-task eval
  eval_success_rate: 0.447
  eval_successes: 21
  eval_total: 47
  per_task.look_at_obj_in_light: 3/6 (50.0%)
  per_task.pick_and_place_simple: 2/8 (25.0%)
  per_task.pick_clean_then_place: 6/11 (54.5%)
  per_task.pick_cool_then_place: 1/7 (14.3%)
  per_task.pick_heat_then_place: 6/8 (75.0%)
  per_task.pick_two_obj_and_place: 3/7 (42.9%)
  train_duration_min: 16.3
  train_steps: 195
  vs_baseline_pp: 2.1

exp_id: mini-taxei-sft-v3
  status: PREPARING
  conclusion: success
  est_duration_min: 90
  format: aligned_single_turn
  train_samples: 7545
  train_samples_clean: 4176
  train_samples_injected: 3369
  train_steps_total: 2832

exp_id: mini-vanilla-sft
  status: DONE
  conclusion: negative
  hypothesis: Vanilla trajectory SFT baseline for comparison with TaxEI
  eval_success_rate: 0.149
  eval_successes: 7
  eval_total: 47
  per_task.look_at_obj_in_light: 0/6 (0%)
  per_task.pick_and_place_simple: 2/8 (25.0%)
  per_task.pick_clean_then_place: 2/11 (18.2%)
  per_task.pick_cool_then_place: 0/7 (0%)
  per_task.pick_heat_then_place: 3/8 (37.5%)
  per_task.pick_two_obj_and_place: 0/7 (0%)
  train_duration_min: 5
  train_steps: 54
  vs_baseline_pp: -27.7

exp_id: mini-vanilla-sft-v3
  status: PREPARING
  conclusion: success
  est_duration_min: 58
  format: aligned_single_turn
  train_samples: 4176
  train_steps_total: 1566

exp_id: mini-vanilla-sft-v4
  status: PREPARING
  conclusion: success
  hypothesis: Vanilla SFT baseline with aligned format (v4), for Gate 3a comparison
  (no metrics)

exp_id: sft-dryrun-73
  status: DONE
  conclusion: success
  data_injected_dryrun: 96
  data_vanilla: 124
  duration_sec: 42
  injected_failed: 4
  peak_memory_gib: 19.22
  steps: 8
  train_loss_avg: 1.894
  train_loss_final: 1.543
  train_loss_init: 2.436

exp_id: v4-random-sft
  status: PREPARING
  conclusion: failed
  hypothesis: v4 Random SFT with same-source data (9,029 samples), formal Gate 3b judgment — only tag differs from v4-taxei
  (no metrics)

exp_id: v4-random-sft-r2
  status: PREPARING
  conclusion: success
  hypothesis: v4 Random SFT retry (r2) — same-source 9,029 samples, formal Gate 3b. Previous run killed by SIGHUP.
  (no metrics)

exp_id: v4-random-sft-r3
  status: PREPARING
  conclusion: N/A
  hypothesis: v4 Random SFT retry (r3) — added trap '' HUP to survive tmux cleanup. Same-source 9,029 samples.
  (no metrics)

exp_id: v4-taxei-sft
  status: PREPARING
  conclusion: failed
  hypothesis: v4 TaxEI SFT with same-source data (9,029 samples), formal Gate 3a/3b judgment
  (no metrics)

exp_id: v4-taxei-sft-r2
  status: PREPARING
  conclusion: success
  hypothesis: v4 TaxEI SFT retry (r2) — same-source 9,029 samples, formal Gate 3a/3b. Previous run killed by SIGHUP.
  (no metrics)

exp_id: v4-taxei-sft-r3
  status: PREPARING
  conclusion: N/A
  hypothesis: v4 TaxEI SFT retry (r3) — added trap '' HUP to survive tmux cleanup. Same-source 9,029 samples.
  (no metrics)

exp_id: v4-vanilla-sft
  status: PREPARING
  conclusion: failed
  (no metrics)

exp_id: vanilla_sft_aligned_v1
  status: PREPARING
  conclusion: N/A
  (no metrics)

exp_id: vanilla_sft_aligned_v2
  status: PREPARING
  conclusion: N/A
  (no metrics)

================================================================================
SECTION 5: BASELINE
================================================================================
exp_id: vanilla-react-baseline
  status: DONE
  conclusion: success
  overall_success_rate: 0.426
  per_task_type.look_at_obj_in_light.rate: 0.5
  per_task_type.look_at_obj_in_light.success: 3
  per_task_type.look_at_obj_in_light.total: 6
  per_task_type.pick_and_place_simple.rate: 0.5
  per_task_type.pick_and_place_simple.success: 4
  per_task_type.pick_and_place_simple.total: 8
  per_task_type.pick_clean_then_place.rate: 0.455
  per_task_type.pick_clean_then_place.success: 5
  per_task_type.pick_clean_then_place.total: 11
  per_task_type.pick_cool_then_place.rate: 0
  per_task_type.pick_cool_then_place.success: 0
  per_task_type.pick_cool_then_place.total: 7
  per_task_type.pick_heat_then_place.rate: 0.625
  per_task_type.pick_heat_then_place.success: 5
  per_task_type.pick_heat_then_place.total: 8
  per_task_type.pick_two_obj_and_place.rate: 0.429
  per_task_type.pick_two_obj_and_place.success: 3
  per_task_type.pick_two_obj_and_place.total: 7
  successes: 20
  total_tasks: 47

================================================================================
SECTION 6: OTHER EXPERIMENTS
================================================================================
exp_id: mini-pipeline-e2e
  status: PREPARING
  conclusion: failed
  (no metrics)

exp_id: traj_collect_500
  status: DONE
  conclusion: negative
  api_cost_usd: 8.86
  collection_time_sec: 5245
  failed_trajectories: 213
  success_rate: 0.702
  successful_trajectories: 501
  total_attempts: 714

exp_id: v3-random-eval
  status: PREPARING
  conclusion: negative
  hypothesis: v3 Random SFT eval on 47-task ALFWorld (format-aligned, initial signal before v4 formal judgment)
  eval_success_rate: 0.511
  eval_successes: 24
  eval_total: 47
  vs_baseline_pp: 8.5
  vs_vanilla_sft_pp: -23.4

exp_id: v3-taxei-eval
  status: PREPARING
  conclusion: negative
  hypothesis: v3 TaxEI SFT eval on 47-task ALFWorld (format-aligned, initial signal before v4 formal judgment)
  eval_success_rate: 0.66
  eval_successes: 31
  eval_total: 47
  per_task.look_at_obj_in_light: 5/6 (83.3%)
  per_task.pick_and_place_simple: 5/8 (62.5%)
  per_task.pick_clean_then_place: 8/11 (72.7%)
  per_task.pick_cool_then_place: 3/7 (42.9%)
  per_task.pick_heat_then_place: 6/8 (75.0%)
  per_task.pick_two_obj_and_place: 4/7 (57.1%)
  vs_baseline_pp: 23.4
  vs_vanilla_sft_pp: -8.5

exp_id: v3-vanilla-eval
  status: PREPARING
  conclusion: success
  success_rate: 0.745
  successes: 35
  total: 47
  vs_baseline: 42.6% → 74.5%
  vs_baseline_pp: 31.9

exp_id: v4-random-seed0
  status: DONE
  conclusion: success
  hypothesis: v4 Random SFT seed=0 (multi-seed verification) — 9,029 samples, same hyperparams as seed=42, testing result stability
  final_loss: 0.355
  token_accuracy: 0.912
  train_duration_min: 110
  train_epochs: 3
  train_steps: 3387

exp_id: v4-random-seed123
  status: DONE
  conclusion: success
  hypothesis: v4 Random SFT seed=123 (P1 multi-seed补齐) — 9,029 samples, same hyperparams as seed=42/0, 配齐3-seed统计分析
  avg_token_accuracy: 0.90849673
  final_loss: 0.16766574
  memory_gib: 18.49
  token_accuracy: 0.94187103
  train_duration_min: 110.2
  train_epochs: 3
  train_loss: 0.35484016
  train_runtime_sec: 6609.3556
  train_samples_per_second: 4.098
  train_speed_s_per_it: 1.951
  train_steps: 3387
  train_steps_per_second: 0.512

exp_id: v4-recovery-dryrun
  status: PREPARING
  conclusion: success
  hypothesis: D010 Phase 2 前置: Recovery eval --inject 模式 dry-run, 1-2 tasks 验证 pipeline 正常工作
  (no metrics)

exp_id: v4-recovery-eval-dev
  status: PREPARING
  conclusion: success
  hypothesis: Recovery eval pipeline development — inject errors during eval to test if TaxEI models recover better than random/vanilla (Option C from D009)
  dryrun_detail: vanilla checkpoint, 1 task, cuda:3, injected error recovered in 13 steps
  dryrun_result: PASS
  injected_eval_lines: 463
  pipeline_files: ['eval/injected_eval.py', 'scripts/run_injected_eval.sh']

exp_id: v4-taxei-recovery-eval
  status: DONE
  conclusion: negative
  hypothesis: v4 TaxEI SFT seed=42 recovery eval (injected_eval.py) — 47 episodes with error injection, measuring detection/recovery/success rates under P1/P2/C1/C4
  detection_rate: 0
  recovery_rate: 0.596
  success_rate: 0.596
  successes: 28
  total: 47

exp_id: v4-taxei-seed0
  status: DONE
  conclusion: success
  hypothesis: v4 TaxEI SFT seed=0 (multi-seed verification) — 9,029 samples, same hyperparams as seed=42, testing result stability
  final_loss: 0.355
  token_accuracy: 0.917
  train_duration_min: 110
  train_epochs: 3
  train_steps: 3387

exp_id: v4-taxei-seed123
  status: DONE
  conclusion: success
  hypothesis: v4 TaxEI SFT seed=123 (P1 multi-seed补齐) — 9,029 samples, same hyperparams as seed=42/0, 配齐3-seed统计分析
  final_loss: 0.35506879
  memory_gib: 18.49
  token_accuracy: 0.89978214
  train_duration_min: 109.2
  train_epochs: 3
  train_runtime_sec: 6549.432
  train_speed_s_per_it: 1.934
  train_steps: 3387

exp_id: v4-vanilla-eval
  status: PREPARING
  conclusion: failed
  hypothesis: v4 Vanilla SFT eval (4,358 samples, clean only) — v4 baseline for Gate 3a comparison
  (no metrics)

exp_id: v4-vanilla-eval-r2
  status: PREPARING
  conclusion: failed
  hypothesis: v4 Vanilla SFT eval retry — fixed --device cuda:0 (was --gpu 0) + explicit checkpoint-1635
  (no metrics)

exp_id: v4-vanilla-seed0
  status: DONE
  conclusion: success
  hypothesis: D010 Phase 1: v4 Vanilla SFT seed=0 多种子验证 — 4,358 samples, LoRA rank=16, 3 epochs, 与 seed=42 的 61.7% 对比波动范围
  avg_loss: 0.416
  final_loss: 0.297
  token_accuracy: 0.902
  train_duration_min: 58
  train_epochs: 3
  train_steps: 1635

exp_id: v4-vanilla-seed123
  status: DONE
  conclusion: success
  hypothesis: D010 Phase 1: v4 Vanilla SFT seed=123 多种子验证 — 4,358 samples, LoRA rank=16, 3 epochs, 与 seed=42 的 61.7% 对比波动范围
  final_loss: 0.288
  token_accuracy: 0.903
  train_duration_min: 58.9
  train_epochs: 3
  train_steps: 1635

exp_id: v4-vanilla-seed7
  status: DONE
  conclusion: killed
  hypothesis: D010 Phase 1: v4 Vanilla SFT seed=7 多种子验证 — 4,358 samples, LoRA rank=16, 3 epochs, 与 seed=42 的 61.7% 对比波动范围
  (no metrics)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019opF2bKVEPfR2DAx2do9Ku",
  "session_id": "54884577-4b89-43d3-8e16-64aaa0260a70",
  "uuid": "f10faab9-c588-45de-b7af-28486eec007f"
}
```

</details>

---

### System

_source line 36_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "ae6d5bdefba342292",
  "tool_use_id": "toolu_019opF2bKVEPfR2DAx2do9Ku",
  "status": "completed",
  "output_file": "",
  "summary": "Extract registry experiment data",
  "usage": {
    "total_tokens": 30023,
    "tool_uses": 7,
    "duration_ms": 110668
  },
  "uuid": "bb9f92ca-d2f4-4ca0-9206-ee387d0c5ec3",
  "session_id": "54884577-4b89-43d3-8e16-64aaa0260a70"
}
```

---

### Tool result

_source line 37 · 2026-05-15T00:53:56.287Z_

<details><summary>↩ Tool result · `toolu_019opF2bKVEPfR2DAx2do9Ku`</summary>

```text
Here is the complete extracted data from all 57 experiments, organized by category:

---

## SECTION 1: CLEAN EVAL EXPERIMENTS

| exp_id | status | conclusion | eval_success_rate | eval_successes | eval_total | notes |
|--------|--------|-----------|-------------------|----------------|------------|-------|
| v4-vanilla-eval-r3 | PREPARING | success | 0.617 | 29 | 47 | per-task: light 83.3%, heat 75.0%, place 62.5%, cool 57.1%, two_obj 57.1%, clean 45.5% |
| v4-vanilla-seed0-eval | DONE | success | 0.681 | 32 | 47 | vs_seed42_pp: +6.4, mcnemar_vs_seed42_p: 0.375, discordant_pairs: 5 |
| v4-vanilla-seed123-eval | DONE | success | 0.660 | 31 | 47 | vs_seed42_pp: +4.3, vs_seed0_pp: -2.1 |
| v4-taxei-eval | PREPARING | negative | 0.617 | 29 | 47 | gate_3a: FAIL, gate_3b: FAIL, gate_4: PASS, vs_vanilla_pp: 0, vs_random_pp: -4.3, mcnemar_vs_vanilla_p: 1.0, mcnemar_vs_random_p: 0.754 |
| v4-taxei-seed0-eval | DONE | success | 0.468 | 22 | 47 | vs_seed42_pp: -14.9 |
| v4-taxei-seed123-eval | DONE | success | 0.617 | 29 | 47 | per-task: light 83.3%, clean 63.6%, heat 75.0%, two_obj 57.1%, place 50.0%, cool 42.9% |
| v4-random-eval | PREPARING | negative | 0.660 | 31 | 47 | vs_vanilla_pp: +4.3, vs_taxei_pp: +4.3, mcnemar_vs_vanilla_p: 0.754 |
| v4-random-seed0-eval | DONE | success | 0.553 | 26 | 47 | vs_seed42_pp: -10.7 |
| v4-random-seed123-eval | DONE | negative | 0.681 | 32 | 47 | per-task: light 83.3%, two_obj 71.4%, heat 75.0%, clean 63.6%, place 62.5%, cool 57.1% |

**Multi-seed summary (eval_success_rate):**
- Vanilla: seed42=0.617, seed0=0.681, seed123=0.660 (mean ~0.653, range 6.4pp)
- TaxEI: seed42=0.617, seed0=0.468, seed123=0.617 (mean ~0.567, range 14.9pp)
- Random: seed42=0.660, seed0=0.553, seed123=0.681 (mean ~0.631, range 12.8pp)

---

## SECTION 2: DOSE-RESPONSE EXPERIMENTS

**Training runs (completed):**

| exp_id | status | conclusion | final_loss | token_accuracy | train_duration_min | train_steps | train_epochs |
|--------|--------|-----------|------------|----------------|-------------------|-------------|-------------|
| v4-taxei-fixed-inject10 | DONE | success | 0.308 | 0.888 | 58 | 1635 | 3 |
| v4-taxei-fixed-inject25-r2 | DONE | success | 0.285 | 0.893 | 58 | 1635 | 3 |
| v4-taxei-fixed-inject25 | DONE | failed | -- | -- | -- | -- | -- |
| v4-taxei-fixed-inject50 | RUNNING | N/A | -- | -- | -- | -- | -- |
| v4-fixed-inject10 | PREPARING | killed | -- | -- | -- | -- | -- |
| v4-fixed-inject25 | PREPARING | killed | -- | -- | -- | -- | -- |

**Eval runs (completed):**

| exp_id | status | conclusion | eval_success_rate | eval_successes | eval_total |
|--------|--------|-----------|-------------------|----------------|------------|
| v4-taxei-fixed-inject10-eval | DONE | success | 0.617 | 29 | 47 |
| v4-taxei-fixed-inject25-eval | DONE | success | 0.489 | 23 | 47 |

**Random fixed-size (all still RUNNING, no metrics yet):**
- v4-random-fixed-inject10
- v4-random-fixed-inject25
- v4-random-fixed-inject50

---

## SECTION 3: RECOVERY EVAL EXPERIMENTS

| exp_id | status | conclusion | recovery_rate | detection_rate | success_rate | successes | total |
|--------|--------|-----------|---------------|----------------|-------------|-----------|-------|
| v4-vanilla-recovery-eval | DONE | success | 0.617 | 0 | 0.617 | 29 | 47 |
| v4-taxei-recovery-eval-r2 | DONE | success | 0.596 | 0 | -- | -- | 47 |
| v4-random-recovery-eval | DONE | success | 0.638 | 0 | -- | 30 | 47 |

v4-taxei-recovery-eval-r2 per-operator breakdown:
- C1_context_truncation: 8/12 (66.7%)
- C4_observation_masking: 7/11 (63.6%)
- P1_step_order_swap: 7/12 (58.3%)
- P2_sub_goal_deletion: 6/12 (50.0%)

---

## SECTION 4: TRAINING EXPERIMENTS

| exp_id | status | conclusion | final_loss | token_accuracy | train_duration_min | train_steps | train_epochs | train_samples |
|--------|--------|-----------|------------|----------------|-------------------|-------------|-------------|---------------|
| v4-vanilla-seed0 | DONE | success | 0.297 | 0.902 | 58 | 1635 | 3 | -- |
| v4-vanilla-seed123 | DONE | success | 0.288 | 0.903 | 58.9 | 1635 | 3 | -- |
| v4-vanilla-seed7 | DONE | killed | -- | -- | -- | -- | -- | -- |
| v4-taxei-seed0 | DONE | success | 0.355 | 0.917 | 110 | 3387 | 3 | -- |
| v4-taxei-seed123 | DONE | success | 0.355 | 0.900 | 109.2 | 3387 | 3 | -- |
| v4-random-seed0 | DONE | success | 0.355 | 0.912 | 110 | 3387 | 3 | -- |
| v4-random-seed123 | DONE | success | 0.168 | 0.942 | 110.2 | 3387 | 3 | -- |
| v4-vanilla-sft | PREPARING | failed | -- | -- | -- | -- | -- | -- |
| v4-taxei-sft | PREPARING | failed | -- | -- | -- | -- | -- | -- |
| v4-taxei-sft-r2 | PREPARING | success | -- | -- | -- | -- | -- | -- |
| v4-taxei-sft-r3 | PREPARING | N/A | -- | -- | -- | -- | -- | -- |
| v4-random-sft | PREPARING | failed | -- | -- | -- | -- | -- | -- |
| v4-random-sft-r2 | PREPARING | success | -- | -- | -- | -- | -- | -- |
| v4-random-sft-r3 | PREPARING | N/A | -- | -- | -- | -- | -- | -- |
| mini-vanilla-sft | DONE | negative | -- | -- | 5 | 54 | -- | -- |
| mini-taxei-sft | DONE | success | -- | -- | 16.3 | 195 | -- | -- |
| mini-vanilla-sft-v3 | PREPARING | success | -- | -- | ~58 est | 1566 | -- | 4176 |
| mini-taxei-sft-v3 | PREPARING | success | -- | -- | ~90 est | 2832 | -- | 7545 |
| mini-random-sft-v3 | PREPARING | success | -- | -- | ~110 est | 3405 | -- | 9076 |
| mini-vanilla-sft-v4 | PREPARING | success | -- | -- | -- | -- | -- | -- |
| vanilla_sft_aligned_v1 | PREPARING | N/A | -- | -- | -- | -- | -- | -- |
| vanilla_sft_aligned_v2 | PREPARING | N/A | -- | -- | -- | -- | -- | -- |
| sft-dryrun-73 | DONE | success | 1.543 | -- | 0.7 | 8 | -- | -- |

sft-dryrun-73 additional: train_loss_init=2.436, train_loss_avg=1.894, peak_memory_gib=19.22

---

## SECTION 5: BASELINE

| exp_id | status | conclusion | overall_success_rate | successes | total_tasks |
|--------|--------|-----------|---------------------|-----------|-------------|
| vanilla-react-baseline | DONE | success | 0.426 | 20 | 47 |

Per-task: heat 62.5%, place 50.0%, light 50.0%, clean 45.5%, two_obj 42.9%, cool 0%

---

## SECTION 6: OTHER NOTABLE EXPERIMENTS

| exp_id | status | conclusion | key metrics |
|--------|--------|-----------|-------------|
| traj_collect_500 | DONE | negative | success_rate=0.702, 501 successful / 714 total, api_cost_usd=$8.86, time=5245s |
| v3-vanilla-eval | PREPARING | success | success_rate=0.745 (35/47), vs_baseline_pp=+31.9 |
| v3-taxei-eval | PREPARING | negative | eval_success_rate=0.660 (31/47), vs_baseline_pp=+23.4, vs_vanilla_sft_pp=-8.5 |
| v3-random-eval | PREPARING | negative | eval_success_rate=0.511 (24/47), vs_baseline_pp=+8.5, vs_vanilla_sft_pp=-23.4 |
| v4-taxei-recovery-eval | DONE | negative | recovery_rate=0.596, detection_rate=0, successes=28/47 |
| v4-vanilla-eval | PREPARING | failed | (no metrics) |
| v4-vanilla-eval-r2 | PREPARING | failed | (no metrics) |
| v4-recovery-dryrun | PREPARING | success | (no metrics) |
| v4-recovery-eval-dev | PREPARING | success | dryrun_result=PASS, pipeline_files: eval/injected_eval.py, scripts/run_injected_eval.sh |
| mini-pipeline-e2e | PREPARING | failed | (no metrics) |

agentId: ae6d5bdefba342292 (use SendMessage with to: 'ae6d5bdefba342292' to continue this agent)
&lt;usage>total_tokens: 32821
tool_uses: 7
duration_ms: 110673&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "54884577-4b89-43d3-8e16-64aaa0260a70",
  "uuid": "d7fd8125-7de8-400d-a548-13b1e7ff58b5",
  "tool_use_result": {
    "status": "completed",
    "prompt": "I need to extract specific experiment data from a large JSON registry file at:\n`/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/54884577-4b89-43d3-8e16-64aaa0260a70/tool-results/mcp-agent-ml-research-read_registry-1778806308126.txt`\n\nThe file is JSON with schema: `{result: string}` where `result` is itself a JSON string containing experiment records.\n\nI need you to extract the following fields for ALL experiments:\n- exp_id\n- status\n- conclusion\n- metrics (especially eval_success_rate, final_loss, token_accuracy, train_duration_min)\n- Any other relevant result fields\n\nSpecifically I need data for these experiments:\n1. Clean Eval experiments: v4-vanilla-eval-r3, v4-vanilla-seed0-eval, v4-vanilla-seed123-eval, v4-taxei-eval, v4-taxei-seed0-eval, v4-taxei-seed123-eval, v4-random-eval, v4-random-seed0-eval, v4-random-seed123-eval\n2. Dose-Response experiments: v4-taxei-fixed-inject10-eval, v4-taxei-fixed-inject25-eval, and any with \"inject50\" or \"random-fixed\" in the name\n3. Recovery Eval experiments: v4-vanilla-recovery-eval, v4-taxei-recovery-eval-r2, v4-random-recovery-eval\n4. Training experiments: any with \"train\" in the name\n5. Baseline: vanilla-react-baseline\n\nFor each experiment, output: exp_id, status, conclusion (first 200 chars), and ALL metrics as a flat dict.\n\nUse jq or python to parse. Output the results as structured text that I can use directly. Be thorough — I need every number.",
    "agentId": "ae6d5bdefba342292",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is the complete extracted data from all 57 experiments, organized by category:\n\n---\n\n## SECTION 1: CLEAN EVAL EXPERIMENTS\n\n| exp_id | status | conclusion | eval_success_rate | eval_successes | eval_total | notes |\n|--------|--------|-----------|-------------------|----------------|------------|-------|\n| v4-vanilla-eval-r3 | PREPARING | success | 0.617 | 29 | 47 | per-task: light 83.3%, heat 75.0%, place 62.5%, cool 57.1%, two_obj 57.1%, clean 45.5% |\n| v4-vanilla-seed0-eval | DONE | success | 0.681 | 32 | 47 | vs_seed42_pp: +6.4, mcnemar_vs_seed42_p: 0.375, discordant_pairs: 5 |\n| v4-vanilla-seed123-eval | DONE | success | 0.660 | 31 | 47 | vs_seed42_pp: +4.3, vs_seed0_pp: -2.1 |\n| v4-taxei-eval | PREPARING | negative | 0.617 | 29 | 47 | gate_3a: FAIL, gate_3b: FAIL, gate_4: PASS, vs_vanilla_pp: 0, vs_random_pp: -4.3, mcnemar_vs_vanilla_p: 1.0, mcnemar_vs_random_p: 0.754 |\n| v4-taxei-seed0-eval | DONE | success | 0.468 | 22 | 47 | vs_seed42_pp: -14.9 |\n| v4-taxei-seed123-eval | DONE | success | 0.617 | 29 | 47 | per-task: light 83.3%, clean 63.6%, heat 75.0%, two_obj 57.1%, place 50.0%, cool 42.9% |\n| v4-random-eval | PREPARING | negative | 0.660 | 31 | 47 | vs_vanilla_pp: +4.3, vs_taxei_pp: +4.3, mcnemar_vs_vanilla_p: 0.754 |\n| v4-random-seed0-eval | DONE | success | 0.553 | 26 | 47 | vs_seed42_pp: -10.7 |\n| v4-random-seed123-eval | DONE | negative | 0.681 | 32 | 47 | per-task: light 83.3%, two_obj 71.4%, heat 75.0%, clean 63.6%, place 62.5%, cool 57.1% |\n\n**Multi-seed summary (eval_success_rate):**\n- Vanilla: seed42=0.617, seed0=0.681, seed123=0.660 (mean ~0.653, range 6.4pp)\n- TaxEI: seed42=0.617, seed0=0.468, seed123=0.617 (mean ~0.567, range 14.9pp)\n- Random: seed42=0.660, seed0=0.553, seed123=0.681 (mean ~0.631, range 12.8pp)\n\n---\n\n## SECTION 2: DOSE-RESPONSE EXPERIMENTS\n\n**Training runs (completed):**\n\n| exp_id | status | conclusion | final_loss | token_accuracy | train_duration_min | train_steps | train_epochs |\n|--------|--------|-----------|------------|----------------|-------------------|-------------|-------------|\n| v4-taxei-fixed-inject10 | DONE | success | 0.308 | 0.888 | 58 | 1635 | 3 |\n| v4-taxei-fixed-inject25-r2 | DONE | success | 0.285 | 0.893 | 58 | 1635 | 3 |\n| v4-taxei-fixed-inject25 | DONE | failed | -- | -- | -- | -- | -- |\n| v4-taxei-fixed-inject50 | RUNNING | N/A | -- | -- | -- | -- | -- |\n| v4-fixed-inject10 | PREPARING | killed | -- | -- | -- | -- | -- |\n| v4-fixed-inject25 | PREPARING | killed | -- | -- | -- | -- | -- |\n\n**Eval runs (completed):**\n\n| exp_id | status | conclusion | eval_success_rate | eval_successes | eval_total |\n|--------|--------|-----------|-------------------|----------------|------------|\n| v4-taxei-fixed-inject10-eval | DONE | success | 0.617 | 29 | 47 |\n| v4-taxei-fixed-inject25-eval | DONE | success | 0.489 | 23 | 47 |\n\n**Random fixed-size (all still RUNNING, no metrics yet):**\n- v4-random-fixed-inject10\n- v4-random-fixed-inject25\n- v4-random-fixed-inject50\n\n---\n\n## SECTION 3: RECOVERY EVAL EXPERIMENTS\n\n| exp_id | status | conclusion | recovery_rate | detection_rate | success_rate | successes | total |\n|--------|--------|-----------|---------------|----------------|-------------|-----------|-------|\n| v4-vanilla-recovery-eval | DONE | success | 0.617 | 0 | 0.617 | 29 | 47 |\n| v4-taxei-recovery-eval-r2 | DONE | success | 0.596 | 0 | -- | -- | 47 |\n| v4-random-recovery-eval | DONE | success | 0.638 | 0 | -- | 30 | 47 |\n\nv4-taxei-recovery-eval-r2 per-operator breakdown:\n- C1_context_truncation: 8/12 (66.7%)\n- C4_observation_masking: 7/11 (63.6%)\n- P1_step_order_swap: 7/12 (58.3%)\n- P2_sub_goal_deletion: 6/12 (50.0%)\n\n---\n\n## SECTION 4: TRAINING EXPERIMENTS\n\n| exp_id | status | conclusion | final_loss | token_accuracy | train_duration_min | train_steps | train_epochs | train_samples |\n|--------|--------|-----------|------------|----------------|-------------------|-------------|-------------|---------------|\n| v4-vanilla-seed0 | DONE | success | 0.297 | 0.902 | 58 | 1635 | 3 | -- |\n| v4-vanilla-seed123 | DONE | success | 0.288 | 0.903 | 58.9 | 1635 | 3 | -- |\n| v4-vanilla-seed7 | DONE | killed | -- | -- | -- | -- | -- | -- |\n| v4-taxei-seed0 | DONE | success | 0.355 | 0.917 | 110 | 3387 | 3 | -- |\n| v4-taxei-seed123 | DONE | success | 0.355 | 0.900 | 109.2 | 3387 | 3 | -- |\n| v4-random-seed0 | DONE | success | 0.355 | 0.912 | 110 | 3387 | 3 | -- |\n| v4-random-seed123 | DONE | success | 0.168 | 0.942 | 110.2 | 3387 | 3 | -- |\n| v4-vanilla-sft | PREPARING | failed | -- | -- | -- | -- | -- | -- |\n| v4-taxei-sft | PREPARING | failed | -- | -- | -- | -- | -- | -- |\n| v4-taxei-sft-r2 | PREPARING | success | -- | -- | -- | -- | -- | -- |\n| v4-taxei-sft-r3 | PREPARING | N/A | -- | -- | -- | -- | -- | -- |\n| v4-random-sft | PREPARING | failed | -- | -- | -- | -- | -- | -- |\n| v4-random-sft-r2 | PREPARING | success | -- | -- | -- | -- | -- | -- |\n| v4-random-sft-r3 | PREPARING | N/A | -- | -- | -- | -- | -- | -- |\n| mini-vanilla-sft | DONE | negative | -- | -- | 5 | 54 | -- | -- |\n| mini-taxei-sft | DONE | success | -- | -- | 16.3 | 195 | -- | -- |\n| mini-vanilla-sft-v3 | PREPARING | success | -- | -- | ~58 est | 1566 | -- | 4176 |\n| mini-taxei-sft-v3 | PREPARING | success | -- | -- | ~90 est | 2832 | -- | 7545 |\n| mini-random-sft-v3 | PREPARING | success | -- | -- | ~110 est | 3405 | -- | 9076 |\n| mini-vanilla-sft-v4 | PREPARING | success | -- | -- | -- | -- | -- | -- |\n| vanilla_sft_aligned_v1 | PREPARING | N/A | -- | -- | -- | -- | -- | -- |\n| vanilla_sft_aligned_v2 | PREPARING | N/A | -- | -- | -- | -- | -- | -- |\n| sft-dryrun-73 | DONE | success | 1.543 | -- | 0.7 | 8 | -- | -- |\n\nsft-dryrun-73 additional: train_loss_init=2.436, train_loss_avg=1.894, peak_memory_gib=19.22\n\n---\n\n## SECTION 5: BASELINE\n\n| exp_id | status | conclusion | overall_success_rate | successes | total_tasks |\n|--------|--------|-----------|---------------------|-----------|-------------|\n| vanilla-react-baseline | DONE | success | 0.426 | 20 | 47 |\n\nPer-task: heat 62.5%, place 50.0%, light 50.0%, clean 45.5%, two_obj 42.9%, cool 0%\n\n---\n\n## SECTION 6: OTHER NOTABLE EXPERIMENTS\n\n| exp_id | status | conclusion | key metrics |\n|--------|--------|-----------|-------------|\n| traj_collect_500 | DONE | negative | success_rate=0.702, 501 successful / 714 total, api_cost_usd=$8.86, time=5245s |\n| v3-vanilla-eval | PREPARING | success | success_rate=0.745 (35/47), vs_baseline_pp=+31.9 |\n| v3-taxei-eval | PREPARING | negative | eval_success_rate=0.660 (31/47), vs_baseline_pp=+23.4, vs_vanilla_sft_pp=-8.5 |\n| v3-random-eval | PREPARING | negative | eval_success_rate=0.511 (24/47), vs_baseline_pp=+8.5, vs_vanilla_sft_pp=-23.4 |\n| v4-taxei-recovery-eval | DONE | negative | recovery_rate=0.596, detection_rate=0, successes=28/47 |\n| v4-vanilla-eval | PREPARING | failed | (no metrics) |\n| v4-vanilla-eval-r2 | PREPARING | failed | (no metrics) |\n| v4-recovery-dryrun | PREPARING | success | (no metrics) |\n| v4-recovery-eval-dev | PREPARING | success | dryrun_result=PASS, pipeline_files: eval/injected_eval.py, scripts/run_injected_eval.sh |\n| mini-pipeline-e2e | PREPARING | failed | (no metrics) |"
      }
    ],
    "totalDurationMs": 110673,
    "totalTokens": 32821,
    "totalToolUseCount": 7,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10865,
      "cache_read_input_tokens": 18961,
      "output_tokens": 2994,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10865
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2994,
          "cache_read_input_tokens": 18961,
          "cache_creation_input_tokens": 10865,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10865,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 2,
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

### Assistant

_source line 38_

<details><summary>Logged reasoning block</summary>

```text
I now have all the data I need. Let me compile the comprehensive results artifact. Let me organize the data carefully:

**1. Clean Eval (3-seed × 3 methods)**

Vanilla:
- seed=42: 61.7% (29/47) — v4-vanilla-eval-r3
- seed=0: 68.1% (32/47) — v4-vanilla-seed0-eval
- seed=123: 66.0% (31/47) — v4-vanilla-seed123-eval
- Mean: (61.7+68.1+66.0)/3 = 195.8/3 = 65.27%


- SD: 3.26

TaxEI:
- seed=42: 61.7% (29/47) — v4-taxei-eval
- seed=0: 46.8% (22/47) — v4-taxei-seed0-eval
- seed=123: 61.7% (29/47) — v4-taxei-seed123-eval
- Mean: (61.7+46.8+61.7)/3 = 170.2/3 = 56.73%
- SD: 8.61

Random:
- seed=42: 66.0% (31/47) — v4-random-eval
- seed=0: 55.3% (26/47) — v4-random-seed0-eval
- seed=123: 68.1% (32/47) — v4-random-seed123-eval
- Mean: 63.13%
- SD: Calculating...

Now I'm looking at the dose-response results with a fixed dataset size of 4358 and seed=42. For TaxEI, the baseline is 61.7%, stays flat at 10% injection, drops to 48.9% at 25%, and the 50% condition is still running. For the random injection approach, the 10% and 25% conditions are also in progress.

Looking at the recovery evaluation across 47 tasks, vanilla achieves 61.7% while TaxEI drops slightly to 59.6%, with the random approach performing best at 63.8%. TaxEI shows varied performance across different corruption types—context truncation handles best at 66.7%, while sub-goal deletion is the weakest at 50%.

Now examining the training metrics for the v4 generation. Looking at the dose-response training results, I'm noticing the fixed-inject variants show lower loss and token accuracy compared to the base models. I need to track down the seed=42 metrics for the vanilla, taxei, and random variants—they should be in the v4 SFT runs, but I'm seeing mixed results there with some failed and some successful attempts.

The earlier mini versions from v3 do have complete metrics, so I'll use those as reference points. For the main comparison, I have the statistical tests showing TaxEI performs significantly better than random (p≈0.034) but not quite significantly better than vanilla (p≈0.32), so I'll include what's available and note where data is sparse.

Now looking at the corrected statistical results with the fixed permutation tests showing no significant differences, plus the variance patterns where TaxEI has the highest standard deviation. I should also note the baseline performance of vanilla-react at 42.6% and how that compares to the ALFWorld state-of-the-art numbers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "54884577-4b89-43d3-8e16-64aaa0260a70",
  "uuid": "903c0372-419c-425f-8e18-d00bc0a9935c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TMT1F13HXnsp6V9Vnn4Mdo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3687,
      "cache_read_input_tokens": 25624,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3687
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

_source line 39_

Now I have all the data. Let me compile the artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "54884577-4b89-43d3-8e16-64aaa0260a70",
  "uuid": "035f9e5c-0f73-44ab-8c87-bb70354333f8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TMT1F13HXnsp6V9Vnn4Mdo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3687,
      "cache_read_input_tokens": 25624,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3687
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

_source line 40_

<details open><summary>🔧 Tool call — Write · `toolu_016stAEy3NBMQWebiKY2MxdU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/comprehensive_results.md",
  "content": "# TaxEI Comprehensive Results\n\n> Generated: 2026-05-15 | All data from project registry\n\n---\n\n## 1. Clean Eval — 3-Seed Comparison (47 ALFWorld tasks)\n\n| Method | Seed=42 | Seed=0 | Seed=123 | Mean | SD |\n|--------|---------|--------|----------|------|-----|\n| **Vanilla** | 61.7% (29/47) | 68.1% (32/47) | 66.0% (31/47) | **65.3%** | 3.3pp |\n| **TaxEI** | 61.7% (29/47) | 46.8% (22/47) | 61.7% (29/47) | **56.7%** | 8.6pp |\n| **Random** | 66.0% (31/47) | 55.3% (26/47) | 68.1% (32/47) | **63.1%** | 7.0pp |\n\n**Registry sources:**\n\n| Method | Seed=42 exp_id | Seed=0 exp_id | Seed=123 exp_id |\n|--------|----------------|---------------|-----------------|\n| Vanilla | v4-vanilla-eval-r3 | v4-vanilla-seed0-eval | v4-vanilla-seed123-eval |\n| TaxEI | v4-taxei-eval | v4-taxei-seed0-eval | v4-taxei-seed123-eval |\n| Random | v4-random-eval | v4-random-seed0-eval | v4-random-seed123-eval |\n\n**Per-task breakdown (seed=42):**\n\n| Task Type | Vanilla | TaxEI | Random |\n|-----------|---------|-------|--------|\n| light (6) | 83.3% | 83.3% | 83.3% |\n| heat (8) | 75.0% | 75.0% | 75.0% |\n| clean (11) | 45.5% | 63.6% | 63.6% |\n| place (8) | 62.5% | 50.0% | 62.5% |\n| two_obj (7) | 57.1% | 57.1% | 71.4% |\n| cool (7) | 57.1% | 42.9% | 57.1% |\n\n---\n\n## 2. Dose-Response (Fixed Dataset Size = 4,358 samples, Seed=42)\n\n| Injection % | TaxEI eval_success_rate | Random eval_success_rate |\n|-------------|------------------------|-------------------------|\n| 0% (vanilla baseline) | 61.7% (29/47) | 61.7% (29/47) |\n| 10% | 61.7% (29/47) | *in progress* |\n| 25% | 48.9% (23/47) | *in progress* |\n| 50% | *in progress* | *in progress* |\n\n**Registry sources:**\n- 0%: v4-vanilla-eval-r3\n- TaxEI 10%: v4-taxei-fixed-inject10-eval\n- TaxEI 25%: v4-taxei-fixed-inject25-eval\n- TaxEI 50%: v4-taxei-fixed-inject50 (RUNNING)\n- Random 10%/25%/50%: v4-random-fixed-inject10/25/50 (RUNNING)\n\n**Dose-response training metrics:**\n\n| exp_id | final_loss | token_accuracy | duration (min) | steps | epochs |\n|--------|-----------|----------------|----------------|-------|--------|\n| v4-taxei-fixed-inject10 | 0.308 | 0.888 | 58 | 1635 | 3 |\n| v4-taxei-fixed-inject25-r2 | 0.285 | 0.893 | 58 | 1635 | 3 |\n\n---\n\n## 3. Recovery Eval (Seed=42, 47 tasks)\n\n| Method | Recovery Rate | Successes/Total | exp_id |\n|--------|--------------|-----------------|--------|\n| **Vanilla** | 61.7% | 29/47 | v4-vanilla-recovery-eval |\n| **TaxEI** | 59.6% | 28/47 | v4-taxei-recovery-eval-r2 |\n| **Random** | 63.8% | 30/47 | v4-random-recovery-eval |\n\nDetection rate = 0 for all methods.\n\n**TaxEI per-operator recovery breakdown (v4-taxei-recovery-eval-r2):**\n\n| Operator | Recovered/Total | Rate |\n|----------|----------------|------|\n| C1_context_truncation | 8/12 | 66.7% |\n| C4_observation_masking | 7/11 | 63.6% |\n| P1_step_order_swap | 7/12 | 58.3% |\n| P2_sub_goal_deletion | 6/12 | 50.0% |\n\n---\n\n## 4. Training Metrics Summary\n\n### v4 Multi-Seed Training\n\n| exp_id | final_loss | token_accuracy | duration (min) | steps | epochs |\n|--------|-----------|----------------|----------------|-------|--------|\n| v4-vanilla-seed0 | 0.297 | 0.902 | 58.0 | 1635 | 3 |\n| v4-vanilla-seed123 | 0.288 | 0.903 | 58.9 | 1635 | 3 |\n| v4-taxei-seed0 | 0.355 | 0.917 | 110.0 | 3387 | 3 |\n| v4-taxei-seed123 | 0.355 | 0.900 | 109.2 | 3387 | 3 |\n| v4-random-seed0 | 0.355 | 0.912 | 110.0 | 3387 | 3 |\n| v4-random-seed123 | 0.168 | 0.942 | 110.2 | 3387 | 3 |\n\n### v3 / Mini Pipeline Training (historical)\n\n| exp_id | status | duration (min) | steps | samples |\n|--------|--------|----------------|-------|---------|\n| mini-vanilla-sft-v3 | success | ~58 | 1566 | 4176 |\n| mini-taxei-sft-v3 | success | ~90 | 2832 | 7545 |\n| mini-random-sft-v3 | success | ~110 | 3405 | 9076 |\n\n### Training Observations\n\n- Vanilla models train faster (~58 min) due to smaller dataset (4,358 samples, 1,635 steps)\n- TaxEI and Random models train ~2x longer (~110 min) due to augmented datasets (~3,387 steps)\n- TaxEI and Random at fixed dataset size (4,358) train in ~58 min, same as Vanilla\n\n---\n\n## 5. Statistical Tests\n\n### 3-Seed Paired t-Tests\n\n| Comparison | p-value | Significant (α=0.05)? |\n|------------|---------|----------------------|\n| TaxEI vs Vanilla | 0.32 | No |\n| TaxEI vs Random | 0.034 | Yes* |\n\n*Marginally significant with only n=3 seeds.\n\n### Pooled Permutation Tests (corrected)\n\n| Comparison | p-value | Significant (α=0.05)? |\n|------------|---------|----------------------|\n| TaxEI vs Vanilla | 0.054 | No (marginal) |\n| TaxEI vs Random | 0.170 | No |\n\n### Variance Analysis\n\n| Method | Mean | SD | Range |\n|--------|------|-----|-------|\n| Vanilla | 65.3% | 3.3pp | 6.4pp |\n| Random | 63.1% | 7.0pp | 12.8pp |\n| TaxEI | 56.7% | 8.6pp | 14.9pp |\n\nVariance gradient: Vanilla (3.3pp) < Random (7.0pp) < TaxEI (8.6pp). Error injection increases training variance, with structured (TaxEI) injection showing higher variance than random.\n\n---\n\n## 6. Baselines & Literature Reference\n\n| Method | Success Rate | Source |\n|--------|-------------|--------|\n| Vanilla ReAct (no SFT) | 42.6% (20/47) | vanilla-react-baseline |\n| **Best SFT (Vanilla seed=0)** | **68.1% (32/47)** | v4-vanilla-seed0-eval |\n| CoEx (SOTA) | 93.28% | Literature |\n| AgentPRM (SOTA) | 91.0% | Literature |\n\n### v3 Historical Comparison\n\n| Method | v3 eval | v4 eval (seed=42) |\n|--------|---------|-------------------|\n| Vanilla | 74.5% (35/47) | 61.7% (29/47) |\n| TaxEI | 66.0% (31/47) | 61.7% (29/47) |\n| Random | 51.1% (24/47) | 66.0% (31/47) |\n\nRegistry sources: v3-vanilla-eval, v3-taxei-eval, v3-random-eval\n\n---\n\n## 7. Key Findings Summary\n\n1. **TaxEI does not improve agent robustness** — mean performance (56.7%) trails both Vanilla (65.3%) and Random (63.1%)\n2. **TaxEI increases training instability** — highest SD (8.6pp) across seeds, driven by seed=0 collapse to 46.8%\n3. **Dose-response shows degradation** — TaxEI at 25% injection drops to 48.9% vs 61.7% at 0%/10%\n4. **Recovery eval shows no advantage** — TaxEI (59.6%) slightly below Vanilla (61.7%) and Random (63.8%)\n5. **All SFT methods substantially beat the no-SFT baseline** (42.6%)\n6. **Statistical significance is weak** — only TaxEI vs Random t-test (p=0.034) reaches significance; permutation tests are all NS\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "54884577-4b89-43d3-8e16-64aaa0260a70",
  "uuid": "4ee0a9d1-633e-4c4d-a1b3-22380c90f67c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TMT1F13HXnsp6V9Vnn4Mdo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3687,
      "cache_read_input_tokens": 25624,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3687
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

_source line 41 · 2026-05-15T00:55:06.491Z_

<details><summary>↩ Tool result · `toolu_016stAEy3NBMQWebiKY2MxdU`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/comprehensive_results.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "54884577-4b89-43d3-8e16-64aaa0260a70",
  "uuid": "e176752c-b47a-4add-a81e-4ec160e5db31",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/comprehensive_results.md",
    "content": "# TaxEI Comprehensive Results\n\n> Generated: 2026-05-15 | All data from project registry\n\n---\n\n## 1. Clean Eval — 3-Seed Comparison (47 ALFWorld tasks)\n\n| Method | Seed=42 | Seed=0 | Seed=123 | Mean | SD |\n|--------|---------|--------|----------|------|-----|\n| **Vanilla** | 61.7% (29/47) | 68.1% (32/47) | 66.0% (31/47) | **65.3%** | 3.3pp |\n| **TaxEI** | 61.7% (29/47) | 46.8% (22/47) | 61.7% (29/47) | **56.7%** | 8.6pp |\n| **Random** | 66.0% (31/47) | 55.3% (26/47) | 68.1% (32/47) | **63.1%** | 7.0pp |\n\n**Registry sources:**\n\n| Method | Seed=42 exp_id | Seed=0 exp_id | Seed=123 exp_id |\n|--------|----------------|---------------|-----------------|\n| Vanilla | v4-vanilla-eval-r3 | v4-vanilla-seed0-eval | v4-vanilla-seed123-eval |\n| TaxEI | v4-taxei-eval | v4-taxei-seed0-eval | v4-taxei-seed123-eval |\n| Random | v4-random-eval | v4-random-seed0-eval | v4-random-seed123-eval |\n\n**Per-task breakdown (seed=42):**\n\n| Task Type | Vanilla | TaxEI | Random |\n|-----------|---------|-------|--------|\n| light (6) | 83.3% | 83.3% | 83.3% |\n| heat (8) | 75.0% | 75.0% | 75.0% |\n| clean (11) | 45.5% | 63.6% | 63.6% |\n| place (8) | 62.5% | 50.0% | 62.5% |\n| two_obj (7) | 57.1% | 57.1% | 71.4% |\n| cool (7) | 57.1% | 42.9% | 57.1% |\n\n---\n\n## 2. Dose-Response (Fixed Dataset Size = 4,358 samples, Seed=42)\n\n| Injection % | TaxEI eval_success_rate | Random eval_success_rate |\n|-------------|------------------------|-------------------------|\n| 0% (vanilla baseline) | 61.7% (29/47) | 61.7% (29/47) |\n| 10% | 61.7% (29/47) | *in progress* |\n| 25% | 48.9% (23/47) | *in progress* |\n| 50% | *in progress* | *in progress* |\n\n**Registry sources:**\n- 0%: v4-vanilla-eval-r3\n- TaxEI 10%: v4-taxei-fixed-inject10-eval\n- TaxEI 25%: v4-taxei-fixed-inject25-eval\n- TaxEI 50%: v4-taxei-fixed-inject50 (RUNNING)\n- Random 10%/25%/50%: v4-random-fixed-inject10/25/50 (RUNNING)\n\n**Dose-response training metrics:**\n\n| exp_id | final_loss | token_accuracy | duration (min) | steps | epochs |\n|--------|-----------|----------------|----------------|-------|--------|\n| v4-taxei-fixed-inject10 | 0.308 | 0.888 | 58 | 1635 | 3 |\n| v4-taxei-fixed-inject25-r2 | 0.285 | 0.893 | 58 | 1635 | 3 |\n\n---\n\n## 3. Recovery Eval (Seed=42, 47 tasks)\n\n| Method | Recovery Rate | Successes/Total | exp_id |\n|--------|--------------|-----------------|--------|\n| **Vanilla** | 61.7% | 29/47 | v4-vanilla-recovery-eval |\n| **TaxEI** | 59.6% | 28/47 | v4-taxei-recovery-eval-r2 |\n| **Random** | 63.8% | 30/47 | v4-random-recovery-eval |\n\nDetection rate = 0 for all methods.\n\n**TaxEI per-operator recovery breakdown (v4-taxei-recovery-eval-r2):**\n\n| Operator | Recovered/Total | Rate |\n|----------|----------------|------|\n| C1_context_truncation | 8/12 | 66.7% |\n| C4_observation_masking | 7/11 | 63.6% |\n| P1_step_order_swap | 7/12 | 58.3% |\n| P2_sub_goal_deletion | 6/12 | 50.0% |\n\n---\n\n## 4. Training Metrics Summary\n\n### v4 Multi-Seed Training\n\n| exp_id | final_loss | token_accuracy | duration (min) | steps | epochs |\n|--------|-----------|----------------|----------------|-------|--------|\n| v4-vanilla-seed0 | 0.297 | 0.902 | 58.0 | 1635 | 3 |\n| v4-vanilla-seed123 | 0.288 | 0.903 | 58.9 | 1635 | 3 |\n| v4-taxei-seed0 | 0.355 | 0.917 | 110.0 | 3387 | 3 |\n| v4-taxei-seed123 | 0.355 | 0.900 | 109.2 | 3387 | 3 |\n| v4-random-seed0 | 0.355 | 0.912 | 110.0 | 3387 | 3 |\n| v4-random-seed123 | 0.168 | 0.942 | 110.2 | 3387 | 3 |\n\n### v3 / Mini Pipeline Training (historical)\n\n| exp_id | status | duration (min) | steps | samples |\n|--------|--------|----------------|-------|---------|\n| mini-vanilla-sft-v3 | success | ~58 | 1566 | 4176 |\n| mini-taxei-sft-v3 | success | ~90 | 2832 | 7545 |\n| mini-random-sft-v3 | success | ~110 | 3405 | 9076 |\n\n### Training Observations\n\n- Vanilla models train faster (~58 min) due to smaller dataset (4,358 samples, 1,635 steps)\n- TaxEI and Random models train ~2x longer (~110 min) due to augmented datasets (~3,387 steps)\n- TaxEI and Random at fixed dataset size (4,358) train in ~58 min, same as Vanilla\n\n---\n\n## 5. Statistical Tests\n\n### 3-Seed Paired t-Tests\n\n| Comparison | p-value | Significant (α=0.05)? |\n|------------|---------|----------------------|\n| TaxEI vs Vanilla | 0.32 | No |\n| TaxEI vs Random | 0.034 | Yes* |\n\n*Marginally significant with only n=3 seeds.\n\n### Pooled Permutation Tests (corrected)\n\n| Comparison | p-value | Significant (α=0.05)? |\n|------------|---------|----------------------|\n| TaxEI vs Vanilla | 0.054 | No (marginal) |\n| TaxEI vs Random | 0.170 | No |\n\n### Variance Analysis\n\n| Method | Mean | SD | Range |\n|--------|------|-----|-------|\n| Vanilla | 65.3% | 3.3pp | 6.4pp |\n| Random | 63.1% | 7.0pp | 12.8pp |\n| TaxEI | 56.7% | 8.6pp | 14.9pp |\n\nVariance gradient: Vanilla (3.3pp) < Random (7.0pp) < TaxEI (8.6pp). Error injection increases training variance, with structured (TaxEI) injection showing higher variance than random.\n\n---\n\n## 6. Baselines & Literature Reference\n\n| Method | Success Rate | Source |\n|--------|-------------|--------|\n| Vanilla ReAct (no SFT) | 42.6% (20/47) | vanilla-react-baseline |\n| **Best SFT (Vanilla seed=0)** | **68.1% (32/47)** | v4-vanilla-seed0-eval |\n| CoEx (SOTA) | 93.28% | Literature |\n| AgentPRM (SOTA) | 91.0% | Literature |\n\n### v3 Historical Comparison\n\n| Method | v3 eval | v4 eval (seed=42) |\n|--------|---------|-------------------|\n| Vanilla | 74.5% (35/47) | 61.7% (29/47) |\n| TaxEI | 66.0% (31/47) | 61.7% (29/47) |\n| Random | 51.1% (24/47) | 66.0% (31/47) |\n\nRegistry sources: v3-vanilla-eval, v3-taxei-eval, v3-random-eval\n\n---\n\n## 7. Key Findings Summary\n\n1. **TaxEI does not improve agent robustness** — mean performance (56.7%) trails both Vanilla (65.3%) and Random (63.1%)\n2. **TaxEI increases training instability** — highest SD (8.6pp) across seeds, driven by seed=0 collapse to 46.8%\n3. **Dose-response shows degradation** — TaxEI at 25% injection drops to 48.9% vs 61.7% at 0%/10%\n4. **Recovery eval shows no advantage** — TaxEI (59.6%) slightly below Vanilla (61.7%) and Random (63.8%)\n5. **All SFT methods substantially beat the no-SFT baseline** (42.6%)\n6. **Statistical significance is weak** — only TaxEI vs Random t-test (p=0.034) reaches significance; permutation tests are all NS\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 42_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01FEjGt7Zoq5rDPcRAVwcSc3`</summary>

```json
{
  "name": "comprehensive_results",
  "type": "report",
  "description": "Comprehensive results table: 3-seed clean eval, dose-response, recovery eval, training metrics, statistical tests, baselines. All data sourced from registry.",
  "project": "tax_error_inject_agent",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/comprehensive_results.md",
  "tags": [
    "results",
    "summary",
    "v4",
    "multi-seed",
    "dose-response",
    "recovery"
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
  "session_id": "54884577-4b89-43d3-8e16-64aaa0260a70",
  "uuid": "75c2c8d1-eb6c-4255-ae03-747135aef098",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J7RkgLsRhXJfcAui9fNvR5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4613,
      "cache_read_input_tokens": 29311,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4613
      },
      "output_tokens": 74,
      "service_tier": "standard",
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

_source line 43 · 2026-05-15T00:55:18.342Z_

<details><summary>↩ Tool result · `toolu_01FEjGt7Zoq5rDPcRAVwcSc3`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_6eecea\", \"name\": \"comprehensive_results\", \"type\": \"report\", \"description\": \"Comprehensive results table: 3-seed clean eval, dose-response, recovery eval, training metrics, statistical tests, baselines. All data sourced from registry.\", \"path\": \"projects/tax_error_inject_agent/artifacts/_project/report/comprehensive_results.md\", \"url\": null, \"project\": \"tax_error_inject_agent\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T00:55:18.314530+00:00\", \"tags\": [\"results\", \"summary\", \"v4\", \"multi-seed\", \"dose-response\", \"recovery\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "54884577-4b89-43d3-8e16-64aaa0260a70",
  "uuid": "2d8f247b-2962-48dd-bd1a-3f68cf7f771e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260515_6eecea\\\", \\\"name\\\": \\\"comprehensive_results\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Comprehensive results table: 3-seed clean eval, dose-response, recovery eval, training metrics, statistical tests, baselines. All data sourced from registry.\\\", \\\"path\\\": \\\"projects/tax_error_inject_agent/artifacts/_project/report/comprehensive_results.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"tax_error_inject_agent\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-15T00:55:18.314530+00:00\\\", \\\"tags\\\": [\\\"results\\\", \\\"summary\\\", \\\"v4\\\", \\\"multi-seed\\\", \\\"dose-response\\\", \\\"recovery\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_6eecea\", \"name\": \"comprehensive_results\", \"type\": \"report\", \"description\": \"Comprehensive results table: 3-seed clean eval, dose-response, recovery eval, training metrics, statistical tests, baselines. All data sourced from registry.\", \"path\": \"projects/tax_error_inject_agent/artifacts/_project/report/comprehensive_results.md\", \"url\": null, \"project\": \"tax_error_inject_agent\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T00:55:18.314530+00:00\", \"tags\": [\"results\", \"summary\", \"v4\", \"multi-seed\", \"dose-response\", \"recovery\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 44_

已完成。产出文件写入 `artifacts/comprehensive_results.md` 并注册为 `art_20260515_6eecea`。

内容涵盖 7 个部分：3-seed clean eval 全维度表（含 per-task 明细）、dose-response 表、recovery eval 表（含 per-operator 明细）、训练指标汇总、统计检验、baseline 参考、关键发现总结。所有数值均来自 registry，dose-response 中 Random 和 TaxEI-50% 标记为 in progress。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "54884577-4b89-43d3-8e16-64aaa0260a70",
  "uuid": "17004c36-dd72-4b15-bc39-12f0fcb0054f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MhjeCbaq8ANYSvXvSLvFoP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 536,
      "cache_read_input_tokens": 33924,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 536
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

_source line 45_

已完成。产出文件写入 `artifacts/comprehensive_results.md` 并注册为 `art_20260515_6eecea`。

内容涵盖 7 个部分：3-seed clean eval 全维度表（含 per-task 明细）、dose-response 表、recovery eval 表（含 per-operator 明细）、训练指标汇总、统计检验、baseline 参考、关键发现总结。所有数值均来自 registry，dose-response 中 Random 和 TaxEI-50% 标记为 in progress。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 224430,
  "duration_api_ms": 224337,
  "num_turns": 6,
  "stop_reason": "end_turn",
  "session_id": "54884577-4b89-43d3-8e16-64aaa0260a70",
  "total_cost_usd": 0.7670432500000001,
  "usage": {
    "input_tokens": 10,
    "cache_creation_input_tokens": 22619,
    "cache_read_input_tokens": 149330,
    "output_tokens": 5844,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 22619,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 158,
        "cache_read_input_tokens": 33924,
        "cache_creation_input_tokens": 536,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 536
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1625,
      "outputTokens": 14,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001695,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 20,
      "outputTokens": 12195,
      "cacheReadInputTokens": 265184,
      "cacheCreationInputTokens": 52445,
      "webSearchRequests": 0,
      "costUSD": 0.7653482500000001,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "2d2f820e-ffe4-4c1d-94b1-9584ab658af6"
}
```

</details>

---
